import 'progress_models.dart';
import 'streak.dart';
import 'trophies.dart';
import 'xp_rules.dart';

/// The rules of progress, with no database and no widgets.
///
/// [apply] takes one thing the learner did and updates XP, counters, the
/// streak and trophies, then reports what changed ([ProgressDelta]) both for
/// the celebration on screen and for the store to write down.
class ProgressEngine {
  ProgressEngine(this.state, {required this.dailyGoal});

  final ProgressState state;

  /// Today's XP target. A callback so a change in Settings applies at once.
  final int Function() dailyGoal;

  Set<String> get activeDays => {
        for (final e in state.dailyXp.entries)
          if (e.value > 0) e.key,
      };

  StreakState streak(DateTime now) => computeStreak(activeDays, now);

  LevelInfo get level => XpRules.levelFor(state.totalXp);

  int todayXp(DateTime now) => state.dailyXp[dayKey(now)] ?? 0;

  /// The number a trophy of this metric is counting.
  int metric(String key, DateTime now) {
    switch (key) {
      case 'xp_total':
        return state.totalXp;
      case 'level':
        return level.level;
      case 'streak_best':
        return streak(now).best;
      case 'languages':
        return state.counters.keys.where((k) => k.startsWith('deck_')).length;
      default:
        return state.counters[key] ?? 0;
    }
  }

  /// Apply [event] (or null, to only check for trophies the learner has
  /// already earned but not been given, as after an update).
  ProgressDelta apply(ProgressEvent? event, DateTime now) {
    final today = dayKey(now);
    final streakBefore = streak(now);
    final levelBefore = level.level;
    final todayBefore = state.dailyXp[today] ?? 0;
    final goal = dailyGoal();

    final rows = <XpRow>[];
    final counterWrites = <String, int>{};
    final trophyWrites = <String, int>{};
    final unlocked = <Trophy>[];
    var eventXp = 0;
    var trophyXp = 0;

    void addXp(int amount, ProgressSource source, String? deckId) {
      if (amount <= 0) return;
      state.totalXp += amount;
      // Trophy XP is a bonus on top: it raises the total (and the level) but
      // is not "studying", so it never makes a day count towards the streak
      // or the daily goal.
      if (source != ProgressSource.trophy) {
        state.dailyXp[today] = (state.dailyXp[today] ?? 0) + amount;
      }
      rows.add(XpRow(
        at: now,
        day: today,
        amount: amount,
        source: source,
        deckId: deckId,
      ));
    }

    void setCounter(String key, int value) {
      state.counters[key] = value;
      counterWrites[key] = value;
    }

    void bump(String key, int by) => setCounter(key, (state.counters[key] ?? 0) + by);

    void raiseTo(String key, int value) {
      if (value > (state.counters[key] ?? 0)) setCounter(key, value);
    }

    void once(String key) {
      if ((state.counters[key] ?? 0) == 0) setCounter(key, 1);
    }

    if (event != null) {
      // Coming back after a week away: judged before today is recorded.
      if (todayBefore == 0) {
        String? last;
        for (final d in activeDays) {
          if (d.compareTo(today) < 0 && (last == null || d.compareTo(last) > 0)) {
            last = d;
          }
        }
        if (last != null && daysBetween(parseDay(last), now) >= 8) {
          bump('comebacks', 1);
        }
      }

      addXp(event.xp, event.source, event.deckId);
      eventXp = event.xp;
      event.increments.forEach(bump);
      event.maxes.forEach(raiseTo);
      if (event.deckId != null) once('deck_${event.deckId}');

      final hour = now.hour;
      if (hour >= 22 || hour < 4) once('night_owl');
      if (hour >= 4 && hour < 7) once('early_bird');
    }

    final streakAfter = streak(now);

    final todayNow = state.dailyXp[today] ?? 0;
    final goalReached =
        event != null && goal > 0 && todayBefore < goal && todayNow >= goal;
    if (goalReached) bump('goal_days', 1);

    // Trophies pay XP, and that XP can itself unlock the next trophy (reach
    // 500 XP, say), so repeat until nothing new turns up.
    for (var pass = 0; pass < 8; pass++) {
      final fresh = <Trophy>[
        for (final t in TrophyCatalog.all)
          if (!state.trophies.containsKey(t.id) &&
              _metricWith(t.metric, now, streakAfter) >= t.target)
            t,
      ];
      if (fresh.isEmpty) break;

      for (final t in fresh) {
        final at = now.millisecondsSinceEpoch;
        state.trophies[t.id] = at;
        trophyWrites[t.id] = at;
        unlocked.add(t);
        addXp(t.tier.xp, ProgressSource.trophy, null);
        trophyXp += t.tier.xp;
      }
    }

    return ProgressDelta(
      at: now,
      eventXp: eventXp,
      trophyXp: trophyXp,
      levelBefore: levelBefore,
      levelAfter: level.level,
      streakBefore: streakBefore,
      streakAfter: streakAfter,
      streakExtended: event != null &&
          todayBefore == 0 &&
          streakAfter.current > streakBefore.current,
      freezeEarned: streakAfter.freezes > streakBefore.freezes,
      goalReached: goalReached,
      todayXp: state.dailyXp[today] ?? 0,
      newTrophies: unlocked,
      xpRows: rows,
      counterWrites: counterWrites,
      trophyWrites: trophyWrites,
    );
  }

  int _metricWith(String key, DateTime now, StreakState s) =>
      key == 'streak_best' ? s.best : metric(key, now);
}
