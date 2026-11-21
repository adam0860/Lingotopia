import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/srs/scheduler.dart';

void main() {
  final now = DateTime(2026, 1, 1, 9, 0);

  group('FSRS', () {
    final fsrs = Fsrs();

    test('a new card graded Good goes to the second learning step', () {
      final next = fsrs.apply(SchedulingState.fresh, Grade.good, now);
      expect(next.phase, CardPhase.learning);
      expect(next.due!.difference(now).inMinutes, 10);
      expect(next.reps, 1);
    });

    test('a new card graded Easy skips the ladder and schedules in days', () {
      final next = fsrs.apply(SchedulingState.fresh, Grade.easy, now);
      expect(next.phase, CardPhase.review);
      expect(next.intervalDays, greaterThan(1));
    });

    test('Again on a review card sends it to relearning and counts a lapse', () {
      final mature = SchedulingState.fresh.copyWith(
        phase: CardPhase.review,
        stability: 30,
        difficulty: 5,
        intervalDays: 30,
        lastReview: now.subtract(const Duration(days: 30)),
        reps: 6,
      );
      final next = fsrs.apply(mature, Grade.again, now);
      expect(next.phase, CardPhase.relearning);
      expect(next.lapses, 1);
      expect(next.stability, lessThanOrEqualTo(mature.stability));
    });

    test('intervals are ordered Again < Hard < Good < Easy', () {
      final mature = SchedulingState.fresh.copyWith(
        phase: CardPhase.review,
        stability: 20,
        difficulty: 5,
        intervalDays: 20,
        lastReview: now.subtract(const Duration(days: 20)),
        reps: 5,
      );
      final p = fsrs.preview(mature, now);
      final durations = [Grade.again, Grade.hard, Grade.good, Grade.easy]
          .map((g) => p[g].due!.difference(now))
          .toList();
      for (var i = 1; i < durations.length; i++) {
        expect(durations[i], greaterThan(durations[i - 1]),
            reason: 'grade ${Grade.values[i]} should schedule further out');
      }
    });

    test('retrievability is the target retention at t = stability', () {
      expect(Fsrs.retrievability(10, 10), closeTo(0.9, 0.001));
      expect(Fsrs.retrievability(0, 10), closeTo(1.0, 0.001));
      expect(Fsrs.retrievability(100, 10), lessThan(0.5));
    });

    test('a higher target retention shortens intervals', () {
      final state = SchedulingState.fresh.copyWith(
        phase: CardPhase.review,
        stability: 40,
        difficulty: 5,
        intervalDays: 40,
        lastReview: now.subtract(const Duration(days: 40)),
      );
      final strict = Fsrs(config: const SchedulerConfig(targetRetention: 0.95));
      final loose = Fsrs(config: const SchedulerConfig(targetRetention: 0.85));
      expect(
        strict.apply(state, Grade.good, now).intervalDays,
        lessThan(loose.apply(state, Grade.good, now).intervalDays),
      );
    });

    test('difficulty stays inside 1..10 under repeated extreme grading', () {
      var s = SchedulingState.fresh;
      var t = now;
      for (var i = 0; i < 40; i++) {
        s = fsrs.apply(s, Grade.again, t);
        t = t.add(const Duration(minutes: 2));
      }
      expect(s.difficulty, inInclusiveRange(1.0, 10.0));
      for (var i = 0; i < 40; i++) {
        s = fsrs.apply(s, Grade.easy, t);
        t = t.add(Duration(days: s.intervalDays));
      }
      expect(s.difficulty, inInclusiveRange(1.0, 10.0));
    });
  });

  group('SM-2', () {
    final sm2 = SM2Scheduler();

    test('ease never falls below 1.3', () {
      var s = SchedulingState.fresh.copyWith(
        phase: CardPhase.review,
        intervalDays: 10,
        ease: 1.4,
      );
      for (var i = 0; i < 20; i++) {
        s = sm2.apply(s, Grade.again, now);
      }
      expect(s.ease, greaterThanOrEqualTo(1.3));
    });

    test('successive Good answers grow the interval', () {
      var s = SchedulingState.fresh;
      var t = now;
      final seen = <int>[];
      for (var i = 0; i < 6; i++) {
        s = sm2.apply(s, Grade.good, t);
        t = t.add(Duration(days: s.intervalDays == 0 ? 0 : s.intervalDays));
        if (s.intervalDays > 0) seen.add(s.intervalDays);
      }
      for (var i = 1; i < seen.length; i++) {
        expect(seen[i], greaterThan(seen[i - 1]));
      }
    });
  });

  group('state round-trip', () {
    test('toMap/fromMap preserves every field', () {
      final s = SchedulingState(
        phase: CardPhase.review,
        stability: 12.5,
        difficulty: 6.25,
        due: DateTime(2026, 3, 4),
        lastReview: DateTime(2026, 2, 1),
        reps: 9,
        lapses: 2,
        intervalDays: 31,
        learningStep: 0,
        ease: 2.35,
      );
      final back = SchedulingState.fromMap(s.toMap());
      expect(back.phase, s.phase);
      expect(back.stability, s.stability);
      expect(back.difficulty, s.difficulty);
      expect(back.due, s.due);
      expect(back.lastReview, s.lastReview);
      expect(back.reps, s.reps);
      expect(back.lapses, s.lapses);
      expect(back.intervalDays, s.intervalDays);
      expect(back.ease, s.ease);
    });
  });

  group('formatInterval', () {
    test('picks a sensible unit', () {
      SchedulingState at(Duration d) =>
          SchedulingState.fresh.copyWith(due: now.add(d));
      expect(formatInterval(at(const Duration(minutes: 10)), now), '10m');
      expect(formatInterval(at(const Duration(hours: 5)), now), '5h');
      expect(formatInterval(at(const Duration(days: 4)), now), '4d');
      expect(formatInterval(at(const Duration(days: 400)), now), '1.1y');
    });
  });
}
