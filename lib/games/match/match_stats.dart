import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

/// Lifetime numbers for one language's Word Match.
class WordMatchStats {
  WordMatchStats({
    this.played = 0,
    this.totalBoards = 0,
    this.flawlessBoards = 0,
    this.lastRange,
    this.lastLength,
    Map<String, int>? bestTimeMs,
  }) : bestTimeMs = bestTimeMs ?? <String, int>{};

  /// Runs finished.
  int played;

  /// Boards cleared in finished runs.
  int totalBoards;

  /// Boards cleared with no wrong pick, in finished runs.
  int flawlessBoards;

  /// What was picked last time, so the lobby opens ready to go again.
  String? lastRange;
  String? lastLength;

  /// Best final time (clock plus penalties) in milliseconds, by length id.
  final Map<String, int> bestTimeMs;

  static String _key(String language) => 'match_stats_v1_$language';

  /// Count a finished run. Returns true when [timeMs] is a new best for
  /// [lengthId] (the first run of a length is its first best).
  ///
  /// A run that [ranked] is false for (the word list was too small for the
  /// full length) counts towards the totals but never as a best time.
  bool record({
    required String lengthId,
    required int timeMs,
    required int boards,
    required int flawless,
    bool ranked = true,
  }) {
    played++;
    totalBoards += boards;
    flawlessBoards += flawless;
    if (!ranked) return false;
    final best = bestTimeMs[lengthId];
    if (best == null || timeMs < best) {
      bestTimeMs[lengthId] = timeMs;
      return true;
    }
    return false;
  }

  Map<String, dynamic> toJson() => {
        'played': played,
        'totalBoards': totalBoards,
        'flawlessBoards': flawlessBoards,
        'lastRange': lastRange,
        'lastLength': lastLength,
        'bestTimeMs': bestTimeMs,
      };

  factory WordMatchStats.fromJson(Map<String, dynamic> j) => WordMatchStats(
        played: (j['played'] as num?)?.toInt() ?? 0,
        totalBoards: (j['totalBoards'] as num?)?.toInt() ?? 0,
        flawlessBoards: (j['flawlessBoards'] as num?)?.toInt() ?? 0,
        lastRange: j['lastRange'] as String?,
        lastLength: j['lastLength'] as String?,
        bestTimeMs: {
          for (final e in ((j['bestTimeMs'] as Map?) ?? const {}).entries)
            e.key as String: (e.value as num).toInt(),
        },
      );

  static Future<WordMatchStats> load(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final raw = prefs.getString(_key(language));
      if (raw == null) return WordMatchStats();
      return WordMatchStats.fromJson(json.decode(raw) as Map<String, dynamic>);
    } catch (_) {
      return WordMatchStats();
    }
  }

  Future<void> save(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(_key(language), json.encode(toJson()));
    } catch (_) {}
  }
}
