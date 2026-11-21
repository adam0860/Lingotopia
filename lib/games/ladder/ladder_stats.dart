import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import 'ladder_game.dart';

/// Lifetime numbers for one language's Lingo Ladder, kept in
/// shared_preferences as a small JSON string.
class LadderStats {
  LadderStats({
    this.gamesPlayed = 0,
    this.gamesWon = 0,
    this.bestPrize = 0,
    this.bestStreak = 0,
    this.totalCorrect = 0,
    Set<String>? seen,
  }) : seen = seen ?? <String>{};

  int gamesPlayed;
  int gamesWon;
  int bestPrize;

  /// Most questions answered correctly in one game.
  int bestStreak;
  int totalCorrect;

  /// Bank question ids already met, oldest first (a Set keeps insertion order).
  final Set<String> seen;

  static const _maxSeen = 400;

  static String _key(String language) => 'ladder_stats_v1_$language';

  void record(LadderOutcome o) {
    gamesPlayed++;
    if (o.status == GameStatus.won) gamesWon++;
    if (o.prize > bestPrize) bestPrize = o.prize;
    if (o.correctCount > bestStreak) bestStreak = o.correctCount;
    totalCorrect += o.correctCount;
    for (final r in o.history) {
      seen.add(r.question.id);
    }
    while (seen.length > _maxSeen) {
      seen.remove(seen.first);
    }
  }

  Map<String, dynamic> toJson() => {
        'gamesPlayed': gamesPlayed,
        'gamesWon': gamesWon,
        'bestPrize': bestPrize,
        'bestStreak': bestStreak,
        'totalCorrect': totalCorrect,
        'seen': seen.toList(),
      };

  factory LadderStats.fromJson(Map<String, dynamic> j) => LadderStats(
        gamesPlayed: j['gamesPlayed'] as int? ?? 0,
        gamesWon: j['gamesWon'] as int? ?? 0,
        bestPrize: j['bestPrize'] as int? ?? 0,
        bestStreak: j['bestStreak'] as int? ?? 0,
        totalCorrect: j['totalCorrect'] as int? ?? 0,
        seen: {...((j['seen'] as List?) ?? const []).cast<String>()},
      );

  static Future<LadderStats> load(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final raw = prefs.getString(_key(language));
      if (raw == null) return LadderStats();
      return LadderStats.fromJson(json.decode(raw) as Map<String, dynamic>);
    } catch (_) {
      // Statistics are a nicety; a corrupt value must never block the game.
      return LadderStats();
    }
  }

  Future<void> save(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(_key(language), json.encode(toJson()));
    } catch (_) {}
  }
}
