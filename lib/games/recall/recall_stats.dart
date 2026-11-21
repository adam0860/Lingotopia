import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import 'recall_engine.dart';

/// Which personal bests a round has just beaten. Nothing is flagged on the
/// very first round, when there was nothing to beat.
class RecallRecords {
  const RecallRecords({
    this.score = false,
    this.reach = false,
    this.streak = false,
  });

  final bool score;
  final bool reach;
  final bool streak;

  bool get any => score || reach || streak;
}

/// Lifetime numbers for one language's Quick Recall.
class RecallStats {
  RecallStats({
    this.played = 0,
    this.bestScore = 0,
    this.bestReach = 0,
    this.bestStreak = 0,
    this.lastRange,
  });

  int played;

  /// Most words recalled in one round.
  int bestScore;

  /// Highest card rank ever answered correctly.
  int bestReach;

  /// Longest run of right answers inside a round.
  int bestStreak;

  /// What was picked last time ('all', 'r3000', 'r1000' or 'studied'), so the
  /// lobby opens ready to go again.
  String? lastRange;

  static String _key(String language) => 'recall_stats_v1_$language';

  /// Add one finished round and say which bests it beat. A new reach only
  /// counts when it rounds to a higher figure than before, since that is what
  /// the player is shown.
  RecallRecords record({
    required int score,
    required int reach,
    required int streak,
  }) {
    final first = played == 0;
    final records = RecallRecords(
      score: !first && score > bestScore,
      reach: !first &&
          RecallRules.reachRounded(reach) > RecallRules.reachRounded(bestReach),
      streak: !first && streak > bestStreak,
    );
    played++;
    if (score > bestScore) bestScore = score;
    if (reach > bestReach) bestReach = reach;
    if (streak > bestStreak) bestStreak = streak;
    return records;
  }

  Map<String, dynamic> toJson() => {
        'played': played,
        'bestScore': bestScore,
        'bestReach': bestReach,
        'bestStreak': bestStreak,
        'lastRange': lastRange,
      };

  factory RecallStats.fromJson(Map<String, dynamic> j) => RecallStats(
        played: (j['played'] as num?)?.toInt() ?? 0,
        bestScore: (j['bestScore'] as num?)?.toInt() ?? 0,
        bestReach: (j['bestReach'] as num?)?.toInt() ?? 0,
        bestStreak: (j['bestStreak'] as num?)?.toInt() ?? 0,
        lastRange: j['lastRange'] as String?,
      );

  static Future<RecallStats> load(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final raw = prefs.getString(_key(language));
      if (raw == null) return RecallStats();
      return RecallStats.fromJson(json.decode(raw) as Map<String, dynamic>);
    } catch (_) {
      return RecallStats();
    }
  }

  Future<void> save(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(_key(language), json.encode(toJson()));
    } catch (_) {}
  }
}
