import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart' show rootBundle;
import 'package:shared_preferences/shared_preferences.dart';

import 'writing_models.dart';

/// Loads the stroke files on first use and keeps writing progress.
///
/// Progress lives in SharedPreferences (one JSON string per language) so it
/// needs no database change.
class WritingRepository extends ChangeNotifier {
  WritingRepository(this._prefs, {Future<String> Function(String)? loader})
      : _load = loader ?? rootBundle.loadString;

  final SharedPreferences _prefs;
  final Future<String> Function(String) _load;

  static const _assets = {
    'ja': 'assets/writing/ja_strokes.json',
    'zh': 'assets/writing/zh_strokes.json',
    'ko': 'assets/writing/ko_strokes.json',
    'ru': 'assets/writing/ru_strokes.json',
    'ar': 'assets/writing/ar_strokes.json',
    'arz': 'assets/writing/ar_strokes.json', // Egyptian Arabic: the same letters
  };

  /// What is shown above each character: kanji readings (Japanese), pinyin
  /// (Chinese), romanization with letter names (Korean) and the sound and
  /// name of each letter (Russian, Arabic).
  static const _readingAssets = {
    'ja': 'assets/writing/ja_readings.json',
    'zh': 'assets/writing/zh_readings.json',
    'ko': 'assets/writing/ko_readings.json',
    'ru': 'assets/writing/ru_readings.json',
    'ar': 'assets/writing/ar_readings.json',
    'arz': 'assets/writing/ar_readings.json',
  };

  final Map<String, Map<String, KanjiReading>> _readings = {};
  final Map<String, StrokeSet> _sets = {};
  final Map<String, Future<StrokeSet?>> _loading = {};
  final Map<String, Map<String, CharProgress>> _progress = {};

  /// Whether this language has stroke data at all.
  static bool supports(String language) => _assets.containsKey(language);

  /// Parsing a couple of megabytes of JSON happens off the UI thread.
  Future<StrokeSet?> setFor(String language) {
    final cached = _sets[language];
    if (cached != null) return Future.value(cached);
    final path = _assets[language];
    if (path == null) return Future.value(null);
    return _loading[language] ??= () async {
      try {
        final text = await _load(path);
        final set = await compute(StrokeSet.parse, text);
        _sets[language] = set;
        return set;
      } catch (e, s) {
        debugPrint('WritingRepository: could not load $path: $e\n$s');
        _loading.remove(language);
        return null;
      }
    }();
  }

  /// The kanji readings for [language], or an empty map when there are none
  /// (or the file cannot be read: the screens then simply show no readings).
  Future<Map<String, KanjiReading>> readingsFor(String language) async {
    final cached = _readings[language];
    if (cached != null) return cached;
    final path = _readingAssets[language];
    if (path == null) return const {};
    try {
      final text = await _load(path);
      return _readings[language] = KanjiReading.parse(text);
    } catch (e, s) {
      debugPrint('WritingRepository: could not load $path: $e\n$s');
      return const {};
    }
  }

  String _key(String language) => 'writing_progress_$language';

  Map<String, CharProgress> _progressFor(String language) {
    return _progress.putIfAbsent(language, () {
      final out = <String, CharProgress>{};
      final raw = _prefs.getString(_key(language));
      if (raw != null) {
        try {
          (jsonDecode(raw) as Map<String, dynamic>).forEach((k, v) {
            out[k] = CharProgress.fromJson(v);
          });
        } catch (_) {
          // A damaged value just starts again from nothing.
        }
      }
      return out;
    });
  }

  CharProgress progressOf(String language, String ch) =>
      _progressFor(language)[ch] ?? const CharProgress();

  /// Characters with at least one star.
  int mastered(String language, {Iterable<String>? among}) {
    final p = _progressFor(language);
    if (among == null) return p.values.where((e) => e.stars > 0).length;
    return among.where((c) => (p[c]?.stars ?? 0) > 0).length;
  }

  /// Records a finished character. [stars] is null for Watch and Trace.
  Future<void> recordFinished(String language, String ch, {int? stars}) async {
    final p = _progressFor(language);
    p[ch] = (p[ch] ?? const CharProgress()).after(newStars: stars);
    await _prefs.setString(
      _key(language),
      jsonEncode({for (final e in p.entries) e.key: e.value.toJson()}),
    );
    notifyListeners();
  }
}
