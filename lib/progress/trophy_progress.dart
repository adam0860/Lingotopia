import 'trophies.dart';

/// How far along a trophy is, from 0 to 1.
double trophyFraction(Trophy t, int Function(String metric) metric) {
  if (t.target <= 0) return 1;
  final v = metric(t.metric);
  return (v / t.target).clamp(0.0, 1.0);
}

/// The locked trophies the learner is closest to, nearest first. Ties go to
/// the cheaper tier, so the list favours the next small win.
List<Trophy> closestTrophies(
  Map<String, int> unlocked,
  int Function(String metric) metric, {
  int count = 3,
}) {
  final locked = [
    for (final t in TrophyCatalog.all)
      if (!unlocked.containsKey(t.id)) t,
  ];
  locked.sort((a, b) {
    final f = trophyFraction(b, metric).compareTo(trophyFraction(a, metric));
    if (f != 0) return f;
    return a.tier.index.compareTo(b.tier.index);
  });
  return locked.take(count).toList();
}

/// Unlocked trophies, newest first.
List<Trophy> recentTrophies(Map<String, int> unlocked, {int count = 6}) {
  final entries = unlocked.entries.toList()
    ..sort((a, b) => b.value.compareTo(a.value));
  final out = <Trophy>[];
  for (final e in entries) {
    final t = TrophyCatalog.byId(e.key);
    if (t != null) out.add(t);
    if (out.length == count) break;
  }
  return out;
}
