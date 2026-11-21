import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/progress/progress_engine.dart';
import 'package:lingotopia/progress/progress_models.dart';
import 'package:lingotopia/progress/progress_service.dart';
import 'package:lingotopia/progress/progress_store.dart';
import 'package:lingotopia/progress/streak.dart';
import 'package:lingotopia/progress/trophies.dart';
import 'package:lingotopia/progress/xp_rules.dart';
import 'package:lingotopia/srs/scheduler.dart';

final t0 = DateTime(2026, 11, 3, 14, 0);

/// Day keys for offsets from t0: 0 is today, -1 yesterday.
Set<String> days(Iterable<int> offsets) =>
    {for (final o in offsets) dayKey(addDays(t0, o))};

Iterable<int> range(int from, int to) => [for (var i = from; i <= to; i++) i];

ProgressEngine engine({int goal = 60, ProgressState? state}) =>
    ProgressEngine(state ?? ProgressState(), dailyGoal: () => goal);

ProgressEvent xp(int n, {String? deck, Map<String, int> inc = const {}}) =>
    ProgressEvent(
      source: ProgressSource.review,
      xp: n,
      deckId: deck,
      increments: inc,
    );

Set<String> ids(ProgressDelta d) => {for (final t in d.newTrophies) t.id};

void main() {
  group('XP and levels', () {
    test('flashcard grades are worth 1, 2, 4 and 5', () {
      expect(XpRules.forGrade(Grade.again), 1);
      expect(XpRules.forGrade(Grade.hard), 2);
      expect(XpRules.forGrade(Grade.good), 4);
      expect(XpRules.forGrade(Grade.easy), 5);
    });

    test('a first-time card adds the new-card bonus', () {
      final e = ProgressEvent.review(grade: Grade.good, wasNew: true, deckId: 'ru_core');
      expect(e.xp, 4 + XpRules.newCardBonus);
      expect(e.increments, {'reviews': 1, 'cards_learned': 1});
      final again = ProgressEvent.review(grade: Grade.good, wasNew: false, deckId: 'ru_core');
      expect(again.xp, 4);
      expect(again.increments, {'reviews': 1});
    });

    test('lessons: perfect bonus, and half for a repeat', () {
      expect(XpRules.lesson(correct: 10, total: 10, firstCompletion: true), 55);
      expect(XpRules.lesson(correct: 8, total: 10, firstCompletion: true), 39);
      expect(XpRules.lesson(correct: 10, total: 10, firstCompletion: false), 28);
    });

    test('ladder and rally awards', () {
      expect(XpRules.ladder(correct: 7, won: false), 70);
      expect(XpRules.ladder(correct: 15, won: true), 300);
      expect(XpRules.rally(won: true, correct: 12, botTier: 4), 40 + 60 + 24);
      expect(XpRules.rally(won: false, correct: 5, botTier: 2), 10 + 10);
      // The per-answer part is capped.
      expect(XpRules.rally(won: true, correct: 100, botTier: 0), 40 + 40);
    });

    test('level boundaries', () {
      expect(XpRules.levelFor(0).level, 1);
      expect(XpRules.levelFor(49).level, 1);
      expect(XpRules.levelFor(50).level, 2);
      expect(XpRules.levelFor(199).level, 2);
      expect(XpRules.levelFor(200).level, 3);
      expect(XpRules.levelFor(800).level, 5);
      expect(XpRules.levelFor(4050).level, 10);
      expect(XpRules.levelFor(-5).level, 1);
    });

    test('progress through a level', () {
      final l = XpRules.levelFor(125);
      expect(l.level, 2);
      expect(l.startXp, 50);
      expect(l.nextXp, 200);
      expect(l.into, 75);
      expect(l.remaining, 75);
      expect(l.progress, closeTo(0.5, 1e-9));
    });

    test('level titles', () {
      expect(XpRules.titleFor(1), 'Newcomer');
      expect(XpRules.titleFor(2), 'Newcomer');
      expect(XpRules.titleFor(3), 'Tourist');
      expect(XpRules.titleFor(7), 'Wanderer');
      expect(XpRules.titleFor(50), 'Lingotopian');
      expect(XpRules.titleFor(500), 'Lingotopian');
    });
  });

  group('streaks', () {
    test('no activity, no streak', () {
      final s = computeStreak({}, t0);
      expect(s.current, 0);
      expect(s.best, 0);
      expect(s.atRisk, isFalse);
    });

    test('days in a row ending today', () {
      final s = computeStreak(days([-2, -1, 0]), t0);
      expect(s.current, 3);
      expect(s.best, 3);
      expect(s.doneToday, isTrue);
      expect(s.atRisk, isFalse);
    });

    test('today is not missed yet: a streak through yesterday stands, at risk', () {
      final s = computeStreak(days([-3, -2, -1]), t0);
      expect(s.current, 3);
      expect(s.doneToday, isFalse);
      expect(s.atRisk, isTrue);
    });

    test('a missed day with no freeze ends the streak but keeps the best', () {
      final s = computeStreak(days([-4, -3, -2]), t0);
      expect(s.current, 0);
      expect(s.best, 3);
      expect(s.atRisk, isFalse);
    });

    test('seven days earn a freeze', () {
      final s = computeStreak(days(range(-6, 0)), t0);
      expect(s.current, 7);
      expect(s.freezes, 1);
    });

    test('a freeze covers one missed day and the streak carries on', () {
      final s = computeStreak(days([...range(-8, -2), 0]), t0);
      expect(s.current, 8);
      expect(s.best, 8);
      expect(s.freezes, 0);
      expect(s.frozenDays, {dayKey(addDays(t0, -1))});
    });

    test('a second missed day with no freeze left ends it', () {
      final s = computeStreak(days([...range(-9, -3), 0]), t0);
      expect(s.current, 1);
      expect(s.best, 7);
      expect(s.frozenDays, {dayKey(addDays(t0, -2))});
    });

    test('at most two freezes are kept', () {
      expect(computeStreak(days(range(-13, 0)), t0).freezes, 2);
      expect(computeStreak(days(range(-20, 0)), t0).freezes, 2);
    });

    test('daysBetween counts calendar days', () {
      expect(daysBetween(DateTime(2026, 3, 8), DateTime(2026, 3, 9)), 1);
      expect(daysBetween(DateTime(2026, 10, 31), DateTime(2026, 11, 3)), 3);
      expect(daysBetween(DateTime(2026, 11, 3), DateTime(2026, 11, 1)), -2);
    });

    test('day keys round-trip', () {
      expect(dayKey(DateTime(2026, 1, 5)), '2026-01-05');
      expect(parseDay('2026-01-05'), DateTime(2026, 1, 5));
    });
  });

  group('trophy catalog', () {
    test('ids and titles are unique', () {
      final ids = TrophyCatalog.all.map((t) => t.id).toList();
      expect(ids.toSet().length, ids.length);
      final titles = TrophyCatalog.all.map((t) => t.title).toList();
      expect(titles.toSet().length, titles.length);
    });

    test('there is a decent number, in every category', () {
      expect(TrophyCatalog.all.length, greaterThanOrEqualTo(45));
      for (final c in TrophyCatalog.categories) {
        expect(TrophyCatalog.inCategory(c), isNotEmpty, reason: c.label);
      }
    });

    test('every trophy has a positive target and a lookup by id', () {
      for (final t in TrophyCatalog.all) {
        expect(t.target, greaterThan(0), reason: t.id);
        expect(TrophyCatalog.byId(t.id), same(t));
      }
      expect(TrophyCatalog.byId('nope'), isNull);
    });

    test('higher targets in one metric never have a lower tier', () {
      final byMetric = <String, List<Trophy>>{};
      for (final t in TrophyCatalog.all) {
        byMetric.putIfAbsent(t.metric, () => []).add(t);
      }
      for (final list in byMetric.values) {
        list.sort((a, b) => a.target.compareTo(b.target));
        for (var i = 1; i < list.length; i++) {
          expect(list[i].tier.index, greaterThanOrEqualTo(list[i - 1].tier.index),
              reason: list[i].id);
        }
      }
    });
  });

  group('engine', () {
    test('XP goes to the total and to today', () {
      final e = engine();
      final d = e.apply(xp(10), t0);
      expect(d.eventXp, 10);
      expect(e.state.totalXp, 10);
      expect(e.todayXp(t0), 10);
      expect(d.todayXp, 10);
      expect(d.xpRows.single.amount, 10);
      expect(d.xpRows.single.day, dayKey(t0));
    });

    test('the first activity of a day extends the streak, the second does not', () {
      final e = engine();
      final a = e.apply(xp(5), t0);
      expect(a.streakExtended, isTrue);
      expect(a.streakAfter.current, 1);
      final b = e.apply(xp(5), t0);
      expect(b.streakExtended, isFalse);
    });

    test('a streak carried over from yesterday grows today', () {
      final state = ProgressState(
        totalXp: 20,
        dailyXp: {dayKey(addDays(t0, -2)): 10, dayKey(addDays(t0, -1)): 10},
      );
      final e = engine(state: state);
      final d = e.apply(xp(5), t0);
      expect(d.streakBefore.current, 2);
      expect(d.streakAfter.current, 3);
      expect(d.streakExtended, isTrue);
      expect(ids(d), contains('streak_best_3'));
    });

    test('the daily goal is reached once, on the event that crosses it', () {
      final e = engine(goal: 10);
      final a = e.apply(xp(6), t0);
      expect(a.goalReached, isFalse);
      final b = e.apply(xp(6), t0);
      expect(b.goalReached, isTrue);
      expect(e.state.counters['goal_days'], 1);
      expect(ids(b), contains('goal_days_1'));
      final c = e.apply(xp(6), t0);
      expect(c.goalReached, isFalse);
      expect(e.state.counters['goal_days'], 1);
    });

    test('a goal of zero is never "reached"', () {
      final e = engine(goal: 0);
      expect(e.apply(xp(50), t0).goalReached, isFalse);
    });

    test('levelling up is reported', () {
      final e = engine(state: ProgressState(totalXp: 45));
      final d = e.apply(xp(10), t0);
      expect(d.levelBefore, 1);
      expect(d.levelAfter, 2);
      expect(d.leveledUp, isTrue);
      expect(d.hasCelebration, isTrue);
    });

    test('a counter reaching its target unlocks the trophy and pays its XP', () {
      final e = engine(state: ProgressState(counters: {'reviews': 99}));
      final d = e.apply(xp(4, inc: {'reviews': 1}), t0);
      expect(ids(d), {'reviews_100'});
      expect(d.trophyXp, TrophyTier.bronze.xp);
      expect(d.xpGained, 4 + TrophyTier.bronze.xp);
      expect(e.state.trophies.containsKey('reviews_100'), isTrue);
      expect(d.trophyWrites.keys, ['reviews_100']);
    });

    test('a trophy is only ever unlocked once', () {
      final e = engine(state: ProgressState(counters: {'reviews': 99}));
      e.apply(xp(4, inc: {'reviews': 1}), t0);
      final again = e.apply(xp(4, inc: {'reviews': 1}), t0);
      expect(again.newTrophies, isEmpty);
    });

    test('trophy XP counts towards the total but not the day', () {
      final e = engine(state: ProgressState(counters: {'reviews': 150}));
      final d = e.apply(null, t0);
      expect(d.trophyXp, 25);
      expect(e.state.totalXp, 25);
      expect(e.todayXp(t0), 0, reason: 'a bonus is not studying');
      expect(e.streak(t0).current, 0);
    });

    test('trophy XP can unlock the next trophy', () {
      final e = engine(
        state: ProgressState(totalXp: 480, counters: {'reviews': 99}),
      );
      final d = e.apply(xp(4, inc: {'reviews': 1}), t0);
      expect(d.newTrophies.map((t) => t.id), ['reviews_100', 'xp_total_500']);
      expect(d.trophyXp, 50);
      expect(e.state.totalXp, 534);
    });

    test('XP rows add up to the XP gained', () {
      final e = engine(
        state: ProgressState(totalXp: 480, counters: {'reviews': 99}),
      );
      final d = e.apply(xp(4, inc: {'reviews': 1}), t0);
      expect(d.xpRows.fold<int>(0, (a, r) => a + r.amount), d.xpGained);
      expect(d.xpRows.where((r) => r.source == ProgressSource.trophy), hasLength(2));
    });

    test('coming back after a week away', () {
      final away = ProgressState(dailyXp: {dayKey(addDays(t0, -8)): 20}, totalXp: 20);
      final d = engine(state: away).apply(xp(5), t0);
      expect(ids(d), contains('comebacks_1'));

      final notAway = ProgressState(dailyXp: {dayKey(addDays(t0, -7)): 20}, totalXp: 20);
      final d2 = engine(state: notAway).apply(xp(5), t0);
      expect(ids(d2), isNot(contains('comebacks_1')));
    });

    test('a brand-new learner has not "come back"', () {
      final d = engine().apply(xp(5), t0);
      expect(ids(d), isNot(contains('comebacks_1')));
    });

    test('night owl and early bird', () {
      final owl = engine()..apply(xp(5), DateTime(2026, 11, 3, 23, 30));
      expect(owl.state.counters['night_owl'], 1);
      expect(owl.state.counters['early_bird'], isNull);
      final bird = engine()..apply(xp(5), DateTime(2026, 11, 3, 5, 15));
      expect(bird.state.counters['early_bird'], 1);
      expect(bird.state.counters['night_owl'], isNull);
      final noon = engine()..apply(xp(5), DateTime(2026, 11, 3, 12, 0));
      expect(noon.state.counters['night_owl'], isNull);
      expect(noon.state.counters['early_bird'], isNull);
    });

    test('studying two decks counts as two languages', () {
      final e = engine();
      e.apply(xp(5, deck: 'ru_core'), t0);
      expect(e.metric('languages', t0), 1);
      final d = e.apply(xp(5, deck: 'es_core'), t0);
      expect(e.metric('languages', t0), 2);
      expect(ids(d), contains('languages_2'));
    });

    test('catching up awards earned trophies once, silently', () {
      final e = engine(state: ProgressState(counters: {'reviews': 150}));
      final first = e.apply(null, t0);
      expect(ids(first), {'reviews_100'});
      expect(first.eventXp, 0);
      expect(first.streakExtended, isFalse);
      final second = e.apply(null, t0);
      expect(second.isEmpty, isTrue);
    });

    test('lesson events', () {
      final e = engine();
      final d = e.apply(
        ProgressEvent.lesson(
          correct: 10,
          total: 10,
          firstCompletion: true,
          passed: true,
          deckId: 'ru_core',
        ),
        t0,
      );
      expect(d.eventXp, 55);
      expect(ids(d), containsAll(['lessons_1', 'lessons_perfect_1']));

      final repeat = ProgressEvent.lesson(
        correct: 10,
        total: 10,
        firstCompletion: false,
        passed: true,
        deckId: 'ru_core',
      );
      expect(repeat.increments.containsKey('lessons'), isFalse);

      final failed = ProgressEvent.lesson(
        correct: 3,
        total: 10,
        firstCompletion: true,
        passed: false,
        deckId: 'ru_core',
      );
      expect(failed.increments, isEmpty);
    });

    test('ladder events', () {
      final e = ProgressEvent.ladder(correct: 11, won: false, prize: 32000, deckId: 'ru_core');
      expect(e.increments['ladder_played'], 1);
      expect(e.increments['ladder_correct'], 11);
      expect(e.increments['ladder_h1'], 1);
      expect(e.increments['ladder_h2'], 1);
      expect(e.increments.containsKey('ladder_won'), isFalse);

      final low = ProgressEvent.ladder(correct: 2, won: false, prize: 200, deckId: 'ru_core');
      expect(low.increments.containsKey('ladder_h1'), isFalse);

      final win = ProgressEvent.ladder(correct: 15, won: true, prize: 1000000, deckId: 'ru_core');
      expect(win.increments['ladder_won'], 1);
      final d = engine().apply(win, t0);
      expect(ids(d), containsAll(['ladder_won_1', 'ladder_played_1', 'ladder_h1_1', 'ladder_h2_1']));
    });

    test('rally events', () {
      final e = ProgressEvent.rally(
        won: true,
        correct: 12,
        botTier: 4,
        bestStreak: 9,
        blasts: 2,
        smashes: 3,
        deckId: 'ru_core',
      );
      expect(e.xp, 124);
      expect(e.increments['rally_played'], 1);
      expect(e.increments['rally_won'], 1);
      expect(e.increments['rally_beat_champion'], 1);
      expect(e.increments['rally_blasts'], 2);
      expect(e.increments['rally_smashes'], 3);
      expect(e.maxes['rally_best_streak'], 9);

      final eng = engine();
      eng.apply(e, t0);
      eng.apply(
        ProgressEvent.rally(
          won: false,
          correct: 3,
          botTier: 1,
          bestStreak: 4,
          blasts: 0,
          smashes: 0,
          deckId: 'ru_core',
        ),
        t0,
      );
      expect(eng.state.counters['rally_best_streak'], 9, reason: 'a max never goes down');
      expect(eng.state.counters['rally_played'], 2);
    });

    test('the streak trophy follows the best streak, not just today', () {
      final state = ProgressState(
        totalXp: 90,
        dailyXp: {for (final d in days(range(-12, -5))) d: 10},
      );
      final e = engine(state: state);
      // 8 days a while ago (best 8), then a break, then today.
      final d = e.apply(xp(5), t0);
      expect(d.streakAfter.best, 8);
      expect(ids(d), containsAll(['streak_best_3', 'streak_best_7']));
    });
  });

  group('service', () {
    test('records, notifies listeners and persists', () async {
      final store = MemoryProgressStore();
      final svc = ProgressService(
        store: store,
        dailyGoal: () => 60,
        clock: () => t0,
      );
      await svc.init();
      expect(svc.ready, isTrue);
      expect(svc.totalXp, 0);

      var notified = 0;
      svc.addListener(() => notified++);
      final seen = <ProgressDelta>[];
      svc.deltas.listen(seen.add);

      final d = svc.record(xp(70, deck: 'ru_core'));
      expect(d.goalReached, isTrue);
      expect(svc.todayXp, greaterThanOrEqualTo(70));
      expect(svc.streak.current, 1);
      expect(notified, 1);

      await Future<void>.delayed(Duration.zero);
      expect(seen, hasLength(1));
      expect(store.written, hasLength(1));
      expect(store.written.single.eventXp, 70);
    });

    test('a plain answer does not raise a celebration', () async {
      final svc = ProgressService(
        store: MemoryProgressStore(),
        dailyGoal: () => 1000,
        clock: () => t0,
      );
      await svc.init();
      svc.record(xp(5)); // first of the day: streak starts, so celebrate
      final seen = <ProgressDelta>[];
      svc.deltas.listen(seen.add);
      svc.record(xp(5));
      await Future<void>.delayed(Duration.zero);
      expect(seen, isEmpty);
    });

    test('init hands out trophies earned before this version', () async {
      final store = MemoryProgressStore(ProgressState(counters: {'reviews': 150}));
      final svc = ProgressService(store: store, dailyGoal: () => 60, clock: () => t0);
      await svc.init();
      expect(svc.trophies.containsKey('reviews_100'), isTrue);
      expect(store.written, hasLength(1));
    });

    test('using the service before init is an error', () {
      final svc = ProgressService(
        store: MemoryProgressStore(),
        dailyGoal: () => 60,
        clock: () => t0,
      );
      expect(svc.ready, isFalse);
      expect(() => svc.record(xp(1)), throwsStateError);
    });

    test('a changed daily goal applies straight away', () async {
      var goal = 100;
      final svc = ProgressService(
        store: MemoryProgressStore(),
        dailyGoal: () => goal,
        clock: () => t0,
      );
      await svc.init();
      svc.record(xp(30));
      goal = 40;
      final d = svc.record(xp(20));
      expect(d.goalReached, isTrue);
    });
  });
}
