import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import 'rally_match.dart';
import 'rally_models.dart';

/// Lifetime numbers for one language's Lingo Rally.
class RallyStats {
  RallyStats({
    this.played = 0,
    this.won = 0,
    this.bestStreak = 0,
    this.lastBot,
    this.lastRules,
    this.lastRange,
    Map<String, int>? beaten,
  }) : beaten = beaten ?? <String, int>{};

  int played;
  int won;
  int bestStreak;

  /// What was picked last time, so the lobby opens ready for a rematch.
  String? lastBot;
  String? lastRules;
  String? lastRange;

  /// Wins per bot id, to show which opponents have been beaten.
  final Map<String, int> beaten;

  static String _key(String language) => 'rally_stats_v1_$language';

  void record(RallyMatch m, BotProfile bot) {
    played++;
    if (m.winner == RallySide.you) {
      won++;
      beaten[bot.id] = (beaten[bot.id] ?? 0) + 1;
    }
    if (m.you.bestStreak > bestStreak) bestStreak = m.you.bestStreak;
  }

  Map<String, dynamic> toJson() => {
        'played': played,
        'won': won,
        'bestStreak': bestStreak,
        'lastBot': lastBot,
        'lastRules': lastRules,
        'lastRange': lastRange,
        'beaten': beaten,
      };

  factory RallyStats.fromJson(Map<String, dynamic> j) => RallyStats(
        played: j['played'] as int? ?? 0,
        won: j['won'] as int? ?? 0,
        bestStreak: j['bestStreak'] as int? ?? 0,
        lastBot: j['lastBot'] as String?,
        lastRules: j['lastRules'] as String?,
        lastRange: j['lastRange'] as String?,
        beaten: {
          for (final e in ((j['beaten'] as Map?) ?? const {}).entries)
            e.key as String: (e.value as num).toInt(),
        },
      );

  static Future<RallyStats> load(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final raw = prefs.getString(_key(language));
      if (raw == null) return RallyStats();
      return RallyStats.fromJson(json.decode(raw) as Map<String, dynamic>);
    } catch (_) {
      return RallyStats();
    }
  }

  Future<void> save(String language) async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setString(_key(language), json.encode(toJson()));
    } catch (_) {}
  }
}
