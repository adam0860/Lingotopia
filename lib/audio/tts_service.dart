import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:crypto/crypto.dart';
import 'package:flutter/foundation.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';
import 'package:sqflite/sqflite.dart';

import '../data/database.dart';
import 'providers/system_tts_provider.dart';
import 'tts_provider.dart';

/// Speaks Turkish words and sentences, as well as it can on whatever machine
/// it finds itself on.
///
/// The strategy, in order:
///   1. If the clip is already on disk, play the file. Instant, offline, free.
///   2. Otherwise ask the best configured synthesizing provider for bytes,
///      write them to the cache, then play them.
///   3. If that fails or nothing is configured, fall back to the device's own
///      speech engine.
///
/// Because step 2 writes through to disk, a learner who reviews a deck once
/// while online then has permanent high-quality audio for it. [prefetch] uses
/// the same path to warm the whole deck ahead of a flight.
enum TtsSource { none, cloud, device }

class TtsService extends ChangeNotifier {
  TtsService({
    required AppDatabase database,
    required this.languageTag,
    SystemTtsProvider? systemProvider,
  })  : _db = database.db,
        _system = systemProvider ?? SystemTtsProvider();

  final Database _db;
  final SystemTtsProvider _system;

  /// e.g. "ru-RU". Changes when the learner switches decks.
  String languageTag;

  /// Point the service at a new language. Cached clips are keyed by text and
  /// voice, not by language, so nothing needs invalidating — a switch back
  /// still finds everything already synthesised.
  void setLanguage(String tag) {
    if (tag == languageTag) return;
    languageTag = tag;
    _preferredVoiceId = null;
    _clearVoiceCache();
    notifyListeners();
  }

  /// Synthesizing providers, best first.
  final List<TtsProvider> _cloudProviders = [];

  /// The one clip player, created together with the service at app start.
  ///
  /// History, so this is not "improved" the wrong way again:
  ///  - created at startup, default release mode: produced sound, sometimes
  ///    played twice;
  ///  - a fresh player per clip, destroyed on completion: no sound;
  ///  - created lazily on first use with setReleaseMode awaited: no sound, and
  ///    the log showed requests entering speak() and never leaving, i.e. an
  ///    awaited plugin call that never answered.
  /// So: created eagerly, and nothing awaited on it is allowed to wait forever.
  final AudioPlayer _player = AudioPlayer();

  /// True while the device voice may be speaking, so it is only asked to stop
  /// when it was actually started. Calling into the speech plugin on every
  /// request, when the neural clip is what plays, only adds ways to hang.
  bool _deviceActive = false;

  /// Rolling in-memory log, shown/copied from Settings so a problem can be
  /// reported without digging through a terminal.
  final List<String> _logLines = [];
  String get logText => _logLines.join('\n');

  void _log(String message) {
    final t = DateTime.now().toIso8601String().substring(11, 23);
    final line = '$t $message';
    _logLines.add(line);
    if (_logLines.length > 300) _logLines.removeAt(0);
    debugPrint('[Lingotopia/Audio] $line');
  }
  Directory? _cacheDir;

  String? _preferredVoiceId;
  String? _speakingKey;

  /// Which clip is playing right now, so the UI can light up the matching row.
  String? get speakingKey => _speakingKey;

  /// Where the most recently played clip actually came from. This exists so
  /// the learner never has to guess whether the neural voice is working — the
  /// UI can just say so. A cloud provider that silently fails (wrong region,
  /// expired key, rate limit) falls through to the device voice with no
  /// exception thrown, so without this flag that failure is invisible.
  TtsSource lastSource = TtsSource.none;

  /// Set when the most recent [speak] call produced no audio at all — no
  /// cloud provider configured or reachable, AND the device has no voice for
  /// this language. The UI surfaces this once rather than failing silently,
  /// which is what happens by default: Windows in particular will accept a
  /// request to speak an uninstalled language and simply do nothing.
  bool _lastSpeakFailed = false;
  bool get lastSpeakFailed => _lastSpeakFailed;

  bool get hasNeuralVoice => _cloudProviders.isNotEmpty;

  void registerProvider(TtsProvider provider) {
    if (!provider.canSynthesizeToFile) return;
    _cloudProviders.add(provider);
    _clearVoiceCache();
    // Invalidate any clips cached by a different (lower-quality) provider.
    // They were synthesised before this better voice was available, and the
    // cache key embeds the provider id, so they will never be found again
    // anyway — but the db rows waste space and can confuse diagnostics.
    _invalidateOtherProviderClips(provider.id);
    notifyListeners();
  }

  Future<void> _invalidateOtherProviderClips(String newProviderId) async {
    // Run async, no need to await — the next speak will already miss the old
    // cache entries because the key changed, so this is purely housekeeping.
    try {
      await _db.delete(
        'audio_cache',
        where: 'provider != ?',
        whereArgs: [newProviderId],
      );
    } catch (_) {}
  }

  void clearProviders() {
    _cloudProviders.clear();
    _clearVoiceCache();
    notifyListeners();
  }

  void setPreferredVoice(String? voiceId) {
    _preferredVoiceId = voiceId;
    _clearVoiceCache();
    notifyListeners();
  }

  Future<Directory> _dir() async {
    if (_cacheDir != null) return _cacheDir!;
    final base = await getApplicationSupportDirectory();
    final dir = Directory(p.join(base.path, 'tts_cache'));
    await dir.create(recursive: true);
    return _cacheDir = dir;
  }

  /// Cache key. Rate is deliberately part of it — a half-speed clip is a
  /// different recording, and learners flip between the two constantly.
  String _key(String text, String providerId, String voiceId, double rate) {
    final digest = sha1.convert(utf8.encode('$providerId|$voiceId|$rate|$text'));
    return digest.toString();
  }

  Future<File?> _cachedFile(String key) async {
    final rows = await _db.query(
      'audio_cache',
      columns: ['file_path'],
      where: 'key = ?',
      whereArgs: [key],
    );
    if (rows.isEmpty) return null;
    final file = File(rows.first['file_path'] as String);
    if (await file.exists()) return file;
    // Index and disk disagreed — drop the stale row so it gets re-synthesized.
    await _db.delete('audio_cache', where: 'key = ?', whereArgs: [key]);
    return null;
  }

  // Voice id cache: provider.id+languageTag -> voice id string.
  // Avoids an HTTP round-trip to the voice listing endpoint on every word.
  final Map<String, String> _voiceIdCache = {};

  String _voiceCacheKey(String providerId, String tag) =>
      '$providerId|${tag.toLowerCase()}';

  /// Resolve the voice id to use for the current language, using a cached
  /// result or the preferred id directly when possible, so we don't hit the
  /// Azure voice-listing endpoint on every single word.
  Future<String?> _resolveVoiceId(TtsProvider provider) async {
    // If the caller already knows which voice they want, trust it — we checked
    // it is valid when it was set.
    if (_preferredVoiceId != null && _preferredVoiceId!.isNotEmpty) {
      return _preferredVoiceId;
    }

    final cacheKey = _voiceCacheKey(provider.id, languageTag);
    if (_voiceIdCache.containsKey(cacheKey)) return _voiceIdCache[cacheKey];

    final voices = await provider.voicesFor(languageTag);
    final id = _pickVoice(voices);
    if (id != null) _voiceIdCache[cacheKey] = id;
    return id;
  }

  /// Wipe the voice-id cache. Called when credentials or language changes
  /// so the next speak picks up a fresh voice for the new context.
  void _clearVoiceCache() => _voiceIdCache.clear();

  /// Requests currently being fetched, keyed by language+rate+text. Two calls
  /// for the same phrase (card shown, then revealed) share ONE network request
  /// instead of firing two. The duplicate is what a rate-limited account
  /// rejects, and a rejected duplicate is what used to fall back to the device
  /// voice and play over the real clip.
  final Map<String, Future<File?>> _inFlight = {};

  /// Generate and cache audio without playing it. Returns the file, or null if
  /// no synthesizing provider could produce one.
  Future<File?> ensureCached(String text, {double rate = 1.0}) {
    final k = '$languageTag|$rate|$text';
    return _inFlight[k] ??= _ensureCachedOnce(text, rate: rate).whenComplete(() {
      // Block body on purpose. `() => _inFlight.remove(k)` RETURNS the removed
      // future, and whenComplete waits for any future its callback returns.
      // The removed future is the one whenComplete itself produces, so it
      // waited on itself forever: every audio request hung, silently, and the
      // device-voice fallback never ran because nothing ever returned.
      _inFlight.remove(k);
    });
  }

  Future<File?> _ensureCachedOnce(String text, {double rate = 1.0}) async {
    for (final provider in _cloudProviders) {
      if (!await provider.isAvailable()) continue;

      final voiceId = await _resolveVoiceId(provider);
      if (voiceId == null) continue;

      final key = _key(text, provider.id, voiceId, rate);
      final existing = await _cachedFile(key);
      if (existing != null) return existing;

      final audio = await provider.synthesize(
        text: text,
        languageTag: languageTag,
        voiceId: voiceId,
        rate: rate,
      );
      if (audio == null) continue;

      final dir = await _dir();
      final file = File(p.join(dir.path, '$key.${audio.fileExtension}'));
      await file.writeAsBytes(audio.bytes, flush: true);

      await _db.insert(
        'audio_cache',
        {
          'key': key,
          'file_path': file.path,
          'provider': provider.id,
          'voice': voiceId,
          'bytes': audio.bytes.length,
          'created_at': DateTime.now().millisecondsSinceEpoch,
        },
        conflictAlgorithm: ConflictAlgorithm.replace,
      );
      return file;
    }
    return null;
  }

  String? _pickVoice(List<TtsVoice> voices) {
    if (voices.isEmpty) return null;
    if (_preferredVoiceId != null &&
        voices.any((v) => v.id == _preferredVoiceId)) {
      return _preferredVoiceId;
    }
    final neural = voices.where((v) => v.isNeural);
    return (neural.isNotEmpty ? neural.first : voices.first).id;
  }

  /// Speak [text]. [id] is an arbitrary tag the UI can watch via
  /// [speakingKey] to show which row is sounding.
  Future<void> speak(String text, {String? id, double rate = 1.0}) async {
    if (text.trim().isEmpty) return;

    // Only the most recent call may clear the "speaking" state when it ends.
    // Otherwise a superseded call finishing late would switch off the
    // highlight of the clip that is actually playing now.
    final generation = ++_speakGeneration;
    _log('#$generation speak "$text" (id: ${id ?? '-'})');

    _speakingKey = id ?? text;
    _lastSpeakFailed = false;
    notifyListeners();

    // A new request replaces whatever is sounding. Both engines are stopped:
    // stopping only the clip player leaves the device voice talking over the
    // new audio, because they are separate engines.
    await _silence();

    try {
      final file = await ensureCached(text, rate: rate).timeout(
        const Duration(seconds: 30),
        onTimeout: () {
          _log('#$generation "$text": clip request timed out after 30 s');
          return null;
        },
      );
      _log('#$generation "$text": clip ${file == null ? 'unavailable' : 'ready'}');

      // While we waited on the network a newer request may have taken over.
      // Playing now would talk over it, so this call just ends.
      if (generation != _speakGeneration) {
        _log('#$generation "$text": superseded, dropped');
        return;
      }

      if (file != null) {
        final played = await _playFile(file, generation);
        if (played) {
          _log('#$generation "$text": played neural clip');
          return;
        }
        _log('#$generation "$text": clip would not '
            'play, using the device voice');
      } else {
        _log('#$generation "$text": no neural clip '
            '(${_cloudProviders.isEmpty ? 'none configured' : 'synthesis failed, see log above'}), '
            'using the device voice');
      }

      if (generation != _speakGeneration) return;

      // Before asking the system engine to speak, check it actually has this
      // language: Windows accepts the request and produces silence otherwise.
      if (await _system.supportsLanguage(languageTag)) {
        lastSource = TtsSource.device;
        notifyListeners();
        _deviceActive = true;
        await _system
            .speak(text: text, languageTag: languageTag, rate: rate)
            .timeout(const Duration(seconds: 30), onTimeout: () {
          _log('#$generation device voice did not finish within 30 s');
        });
        _deviceActive = false;
      } else {
        lastSource = TtsSource.none;
        _lastSpeakFailed = true;
      }
    } catch (e) {
      _log('#$generation speak failed: $e');
      lastSource = TtsSource.none;
      _lastSpeakFailed = true;
    } finally {
      if (generation == _speakGeneration) {
        _speakingKey = null;
        notifyListeners();
      }
    }
  }

  /// Stop everything that could be making sound. The clip player and the
  /// device voice are separate engines and one does not stop the other. Each
  /// call is time-limited: a plugin that never answers must not be able to
  /// stall every later request.
  Future<void> _silence() async {
    try {
      await _player.stop().timeout(const Duration(seconds: 2));
    } catch (e) {
      _log('silence: player.stop() ${e is TimeoutException ? 'timed out' : 'failed: $e'}');
    }
    if (_deviceActive) {
      _deviceActive = false;
      try {
        await _system.stop().timeout(const Duration(seconds: 2));
      } catch (e) {
        _log('silence: device stop() ${e is TimeoutException ? 'timed out' : 'failed: $e'}');
      }
    }
  }

  int _speakGeneration = 0;

  /// Play a cached clip and wait for it to finish. Returns false only if it
  /// could not be played at all, so the caller may use the device voice.
  ///
  /// Invariant: at most one thing is ever sounding. Before a retry (and before
  /// the caller falls back to the device voice) the player is stopped, so a
  /// clip that began and then reported an error is never heard underneath
  /// whatever plays next.
  ///
  /// [lastSource] becomes cloud only once playback has actually started.
  Future<bool> _playFile(File file, int generation) async {
    for (var attempt = 1; attempt <= 2; attempt++) {
      final clock = Stopwatch()..start();
      var started = false;
      try {
        final player = _player;

        // Subscribe before starting: a short clip can finish before a
        // listener attached afterwards would hear it.
        //
        // The .then<void> matters. onPlayerComplete is declared as a stream of
        // void but actually carries AudioEvent values, and Dart checks the real
        // type at runtime. Calling .timeout(onTimeout: () {}) on the raw
        // future threw "'() => Null' is not a subtype of ... AudioEvent" the
        // instant a clip began, which made the app believe playback had failed.
        // That one error caused both the doubled voice (clip still playing,
        // device voice added on top) and the unwanted device-voice fallback.
        final Future<void> finished =
            player.onPlayerComplete.first.then<void>((_) {});

        await player
            .play(DeviceFileSource(file.path))
            .timeout(const Duration(seconds: 10));
        started = true;
        _log('#$generation attempt $attempt: play() returned after '
            '${clock.elapsedMilliseconds} ms');

        if (generation == _speakGeneration) {
          lastSource = TtsSource.cloud;
          notifyListeners();
        }

        // Ceiling only so a stuck backend cannot wedge the UI permanently.
        await finished.timeout(const Duration(seconds: 45), onTimeout: () {});
        _log('#$generation finished after ${clock.elapsedMilliseconds} ms');
        return true;
      } catch (e) {
        _log('#$generation attempt $attempt failed after '
            '${clock.elapsedMilliseconds} ms: $e');

        // Once the clip is audibly playing, nothing that goes wrong while
        // WAITING for it may restart it or add the device voice. Only a
        // failure to start playback is allowed to retry or fall back.
        if (started) return true;
        if (generation != _speakGeneration) return true; // superseded

        try {
          await _player.stop().timeout(const Duration(seconds: 2));
        } catch (_) {}
      }
    }
    return false;
  }

  Future<void> stop() async {
    _speakGeneration++;
    await _silence();
    _speakingKey = null;
    notifyListeners();
  }

  /// Warm the cache for a batch of phrases, reporting progress 0..1.
  ///
  /// Used by Settings › "Download audio for this deck", which is what makes
  /// the deck usable on a plane. Runs sequentially on purpose: cloud TTS
  /// endpoints rate-limit hard on parallel bursts.
  Future<void> prefetch(
    List<String> phrases, {
    void Function(int done, int total)? onProgress,
    bool Function()? shouldCancel,
  }) async {
    for (var i = 0; i < phrases.length; i++) {
      if (shouldCancel?.call() ?? false) return;
      await ensureCached(phrases[i]);
      onProgress?.call(i + 1, phrases.length);
    }
  }

  Future<({int files, int bytes})> cacheSize() async {
    final rows = await _db.rawQuery(
      'SELECT COUNT(*) AS n, COALESCE(SUM(bytes), 0) AS b FROM audio_cache',
    );
    return (
      files: (rows.first['n'] as int?) ?? 0,
      bytes: (rows.first['b'] as int?) ?? 0,
    );
  }

  Future<void> clearCache() async {
    final dir = await _dir();
    if (await dir.exists()) await dir.delete(recursive: true);
    _cacheDir = null;
    await _db.delete('audio_cache');
    notifyListeners();
  }

  @override
  void dispose() {
    _player.dispose();
    super.dispose();
  }
}
