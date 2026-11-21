// Calendar helpers and the streak rule. Pure Dart, no clock of its own: the
// caller says what "today" is, so tests can walk through months in a blink.

String dayKey(DateTime d) =>
    '${d.year.toString().padLeft(4, '0')}-'
    '${d.month.toString().padLeft(2, '0')}-'
    '${d.day.toString().padLeft(2, '0')}';

DateTime parseDay(String key) {
  final p = key.split('-');
  return DateTime(int.parse(p[0]), int.parse(p[1]), int.parse(p[2]));
}

/// Whole days from [a] to [b] (negative when b is earlier). Works on dates,
/// so a daylight-saving change never turns a day into 23 or 25 hours.
int daysBetween(DateTime a, DateTime b) {
  final x = DateTime.utc(a.year, a.month, a.day);
  final y = DateTime.utc(b.year, b.month, b.day);
  return y.difference(x).inDays;
}

DateTime addDays(DateTime d, int n) => DateTime(d.year, d.month, d.day + n);

class StreakState {
  const StreakState({
    required this.current,
    required this.best,
    required this.freezes,
    required this.frozenDays,
    required this.doneToday,
  });

  /// Consecutive days with activity (frozen days hold the streak but do not
  /// add to it). Today does not break it until the day is over.
  final int current;
  final int best;

  /// Streak freezes in the bag right now.
  final int freezes;

  /// Missed days a freeze covered, as day keys.
  final Set<String> frozenDays;

  final bool doneToday;

  /// There is a streak to lose and nothing has been done yet today.
  bool get atRisk => !doneToday && current > 0;

  static const empty = StreakState(
    current: 0,
    best: 0,
    freezes: 0,
    frozenDays: {},
    doneToday: false,
  );
}

/// The streak, worked out from scratch from the days that had any activity.
///
/// - Every active day adds one.
/// - Every [freezeEvery] days of streak earns a freeze, up to [maxFreezes].
/// - A missed day spends a freeze if there is one and the streak carries on;
///   with none, the streak falls to zero.
/// - Today is never counted as missed: there is still time.
///
/// Working it out from the history each time means there is no streak state
/// to store, and it can never drift from the real activity log.
StreakState computeStreak(
  Set<String> activeDays,
  DateTime today, {
  int freezeEvery = 7,
  int maxFreezes = 2,
}) {
  if (activeDays.isEmpty) return StreakState.empty;

  final todayDate = DateTime(today.year, today.month, today.day);
  final todayKey = dayKey(todayDate);
  final sorted = activeDays.toList()..sort();

  var d = parseDay(sorted.first);
  var current = 0;
  var best = 0;
  var freezes = 0;
  final frozen = <String>{};

  while (!d.isAfter(todayDate)) {
    final k = dayKey(d);
    if (activeDays.contains(k)) {
      current++;
      if (current % freezeEvery == 0 && freezes < maxFreezes) freezes++;
      if (current > best) best = current;
    } else if (k != todayKey && current > 0) {
      if (freezes > 0) {
        freezes--;
        frozen.add(k);
      } else {
        current = 0;
      }
    }
    d = addDays(d, 1);
  }

  return StreakState(
    current: current,
    best: best,
    freezes: freezes,
    frozenDays: frozen,
    doneToday: activeDays.contains(todayKey),
  );
}
