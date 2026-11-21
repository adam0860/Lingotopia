import 'package:flutter/foundation.dart' show debugPrint;
import 'package:flutter_tts/flutter_tts.dart';

import '../tts_provider.dart';

/// The operating system's built-in speech engine.
///
/// Quality varies enormously by platform. On Android, Google's Turkish voice
/// is respectable. On Windows, SAPI often has no Turkish voice installed at
/// all, in which case [isAvailable] reports false and the app routes around
/// it. Treat this as the offline floor, not the target.
class SystemTtsProvider implements TtsProvider {
  SystemTtsProvider();

  final FlutterTts _tts = FlutterTts();
  bool _configured = false;

  @override
  String get id => 'system';

  @override
  String get displayName => 'Device voice';

  @override
  bool get canSynthesizeToFile => false;

  @override
  bool get worksOffline => true;

  Future<void> _configure() async {
    if (_configured) return;
    await _tts.awaitSpeakCompletion(true);
    await _tts.setVolume(1.0);
    await _tts.setPitch(1.0);
    _configured = true;
  }

  @override
  Future<bool> isAvailable() async {
    try {
      final languages = await _tts.getLanguages;
      return languages is List && languages.isNotEmpty;
    } catch (_) {
      return false;
    }
  }

  /// Whether the host has a voice for this language.
  ///
  /// Deliberately lenient. `isLanguageAvailable` is unreliable on Windows —
  /// it returns false for languages the engine will happily speak — so a
  /// strict check here silently kills working audio. The rule instead:
  /// report false only when the engine gives a usable language list AND
  /// nothing in it matches, which is the case that actually produces
  /// silence. Anything ambiguous returns true and lets `speak` try.
  Future<bool> supportsLanguage(String languageTag) async {
    final base = languageTag.split('-').first.toLowerCase();

    final cached = _languageSupport[base];
    if (cached != null) return cached;

    bool result = true;
    try {
      final languages = await _tts.getLanguages;
      if (languages is List && languages.isNotEmpty) {
        final available = languages
            .map((l) => l.toString().toLowerCase().replaceAll('_', '-'))
            .toList();
        final matches = available.any((l) => l.split('-').first == base);
        if (matches) {
          result = true;
        } else {
          // The list looks real and has no match — but confirm with the
          // engine's own check before declaring failure, since some
          // platforms report a partial list.
          try {
            result = (await _tts.isLanguageAvailable(languageTag)) == true;
          } catch (_) {
            result = false;
          }
        }
      }
    } catch (_) {
      // Could not enumerate — assume it might work rather than block.
      result = true;
    }

    _languageSupport[base] = result;
    return result;
  }

  /// Cached per base language code; enumerating voices is slow enough that
  /// doing it on every card tap is noticeable.
  final Map<String, bool> _languageSupport = {};

  @override
  Future<List<TtsVoice>> voicesFor(String languageTag) async {
    try {
      final raw = await _tts.getVoices;
      if (raw is! List) return const [];
      final prefix = languageTag.split('-').first.toLowerCase();
      return raw
          .whereType<Map>()
          .where((v) => (v['locale'] as String? ?? '').toLowerCase().startsWith(prefix))
          .map((v) => TtsVoice(
                id: v['name'] as String? ?? '',
                displayName: v['name'] as String? ?? 'Device voice',
                languageTag: v['locale'] as String? ?? languageTag,
              ))
          .toList();
    } catch (_) {
      return const [];
    }
  }

  @override
  Future<TtsAudio?> synthesize({
    required String text,
    required String languageTag,
    required String voiceId,
    double rate = 1.0,
  }) async =>
      null; // Speaks directly; produces no file.

  /// Voice chosen per base language, so the voice list is only walked once.
  final Map<String, Map<String, String>?> _chosenVoice = {};

  /// Pick an installed voice whose locale matches [languageTag].
  ///
  /// On Windows `setLanguage('es-ES')` is not reliable: when it cannot match
  /// it silently keeps whatever voice was active, which is usually English, so
  /// Spanish text gets read with English letter sounds ("que" as the letter Q).
  /// Naming an actual voice avoids depending on that. Exact locale match wins
  /// (es-ES over es-MX), then any voice of the same base language.
  Future<Map<String, String>?> _pickVoice(String languageTag) async {
    final tag = languageTag.toLowerCase().replaceAll('_', '-');
    final base = tag.split('-').first;
    if (_chosenVoice.containsKey(tag)) return _chosenVoice[tag];

    Map<String, String>? choice;
    try {
      final raw = await _tts.getVoices;
      if (raw is List) {
        final voices = raw.whereType<Map>().map((v) => {
              'name': (v['name'] ?? '').toString(),
              'locale': (v['locale'] ?? '').toString(),
            }).where((v) => v['name']!.isNotEmpty).toList();

        String norm(String l) => l.toLowerCase().replaceAll('_', '-');
        final exact = voices.where((v) => norm(v['locale']!) == tag);
        final sameBase =
            voices.where((v) => norm(v['locale']!).split('-').first == base);
        final pick = exact.isNotEmpty
            ? exact.first
            : (sameBase.isNotEmpty ? sameBase.first : null);
        if (pick != null) choice = {'name': pick['name']!, 'locale': pick['locale']!};
      }
    } catch (_) {}

    debugPrint('[Lingotopia/Device TTS] voice for $languageTag: '
        '${choice == null ? '(none found — using setLanguage only)' : choice['name']}');
    _chosenVoice[tag] = choice;
    return choice;
  }

  @override
  Future<void> speak({
    required String text,
    required String languageTag,
    String? voiceId,
    double rate = 1.0,
  }) async {
    await _configure();
    await _tts.setLanguage(languageTag);
    // flutter_tts rate is not a uniform scale across platforms: Android treats
    // 1.0 as normal, iOS treats ~0.5 as normal. Map the app's 1.0 accordingly.
    await _tts.setSpeechRate(rate * 0.5);

    if (voiceId != null && voiceId.isNotEmpty) {
      await _tts.setVoice({'name': voiceId, 'locale': languageTag});
    } else {
      final chosen = await _pickVoice(languageTag);
      if (chosen != null) await _tts.setVoice(chosen);
    }
    await _tts.speak(text);
  }

  @override
  Future<void> stop() => _tts.stop();
}
