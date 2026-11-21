import 'dart:math' as math;

/// How the learner graded a card. Matches Anki's four buttons.
enum Grade {
  again(1),
  hard(2),
  good(3),
  easy(4);

  const Grade(this.value);
  final int value;
}

/// Where a card is in its life.
enum CardPhase { newCard, learning, review, relearning }

/// The scheduling state the database stores for one card.
class SchedulingState {
  const SchedulingState({
    required this.phase,
    required this.stability,
    required this.difficulty,
    required this.due,
    required this.lastReview,
    required this.reps,
    required this.lapses,
    required this.intervalDays,
    required this.learningStep,
    // SM-2 only
    required this.ease,
  });

  final CardPhase phase;

  /// FSRS memory stability, in days. The interval at which recall probability
  /// has decayed to the target retention.
  final double stability;

  /// FSRS difficulty, clamped to 1..10.
  final double difficulty;

  final DateTime? due;
  final DateTime? lastReview;
  final int reps;
  final int lapses;
  final int intervalDays;

  /// Index into the learning-step ladder while in [CardPhase.learning] or
  /// [CardPhase.relearning].
  final int learningStep;

  /// SM-2 ease factor (2.5 default). Unused by FSRS but persisted so a learner
  /// can switch schedulers without losing their history.
  final double ease;

  static const SchedulingState fresh = SchedulingState(
    phase: CardPhase.newCard,
    stability: 0,
    difficulty: 0,
    due: null,
    lastReview: null,
    reps: 0,
    lapses: 0,
    intervalDays: 0,
    learningStep: 0,
    ease: 2.5,
  );

  SchedulingState copyWith({
    CardPhase? phase,
    double? stability,
    double? difficulty,
    DateTime? due,
    DateTime? lastReview,
    int? reps,
    int? lapses,
    int? intervalDays,
    int? learningStep,
    double? ease,
  }) {
    return SchedulingState(
      phase: phase ?? this.phase,
      stability: stability ?? this.stability,
      difficulty: difficulty ?? this.difficulty,
      due: due ?? this.due,
      lastReview: lastReview ?? this.lastReview,
      reps: reps ?? this.reps,
      lapses: lapses ?? this.lapses,
      intervalDays: intervalDays ?? this.intervalDays,
      learningStep: learningStep ?? this.learningStep,
      ease: ease ?? this.ease,
    );
  }

  Map<String, Object?> toMap() => {
        'phase': phase.index,
        'stability': stability,
        'difficulty': difficulty,
        'due': due?.millisecondsSinceEpoch,
        'last_review': lastReview?.millisecondsSinceEpoch,
        'reps': reps,
        'lapses': lapses,
        'interval_days': intervalDays,
        'learning_step': learningStep,
        'ease': ease,
      };

  static SchedulingState fromMap(Map<String, Object?> m) => SchedulingState(
        phase: CardPhase.values[(m['phase'] as int?) ?? 0],
        stability: (m['stability'] as num?)?.toDouble() ?? 0,
        difficulty: (m['difficulty'] as num?)?.toDouble() ?? 0,
        due: m['due'] == null
            ? null
            : DateTime.fromMillisecondsSinceEpoch(m['due'] as int),
        lastReview: m['last_review'] == null
            ? null
            : DateTime.fromMillisecondsSinceEpoch(m['last_review'] as int),
        reps: (m['reps'] as int?) ?? 0,
        lapses: (m['lapses'] as int?) ?? 0,
        intervalDays: (m['interval_days'] as int?) ?? 0,
        learningStep: (m['learning_step'] as int?) ?? 0,
        ease: (m['ease'] as num?)?.toDouble() ?? 2.5,
      );
}

/// The four intervals shown on the grading buttons, so the learner can see
/// what each choice costs before they press it.
class SchedulingPreview {
  const SchedulingPreview(this.byGrade);
  final Map<Grade, SchedulingState> byGrade;
  SchedulingState operator [](Grade g) => byGrade[g]!;
}

abstract class Scheduler {
  String get name;

  /// What each of the four buttons would do to [state] if pressed at [now].
  SchedulingPreview preview(SchedulingState state, DateTime now);

  SchedulingState apply(SchedulingState state, Grade grade, DateTime now) =>
      preview(state, now)[grade];
}

/// Shared config for both schedulers.
class SchedulerConfig {
  const SchedulerConfig({
    this.targetRetention = 0.9,
    this.learningStepsMinutes = const [1, 10],
    this.relearningStepsMinutes = const [10],
    this.maximumIntervalDays = 36500,
    this.fsrsWeights,
  });

  final double targetRetention;
  final List<int> learningStepsMinutes;
  final List<int> relearningStepsMinutes;
  final int maximumIntervalDays;

  /// Override the FSRS weight vector — this is what a learner's own review
  /// history gets optimised into. Null means use [Fsrs.defaultWeights].
  final List<double>? fsrsWeights;
}

/// FSRS v4.5 — the scheduler modern Anki uses.
///
/// Two variables describe a card: stability (how many days until recall
/// probability falls to the target) and difficulty (1..10, how much a good
/// answer grows stability). A review updates both, then the next interval is
/// solved from the forgetting curve.
///
/// IMPORTANT: [defaultWeights] is the published FSRS-4.5 default vector. Before
/// shipping, diff it against the reference implementation at
/// https://github.com/open-spaced-repetition/fsrs4anki — a wrong constant here
/// degrades scheduling quietly rather than crashing. `SM2Scheduler` is wired up
/// as a conservative alternative and is switchable in Settings.
class Fsrs implements Scheduler {
  Fsrs({SchedulerConfig config = const SchedulerConfig()})
      : _config = config,
        _w = config.fsrsWeights ?? defaultWeights;

  final SchedulerConfig _config;
  final List<double> _w;

  @override
  String get name => 'FSRS 4.5';

  static const List<double> defaultWeights = [
    0.4872, 1.4003, 3.7145, 13.8206, // w0..w3  initial stability per grade
    5.1618, 1.2298, // w4, w5  initial difficulty
    0.8975, 0.0310, // w6, w7  difficulty update + mean reversion
    1.6474, 0.1367, 1.0461, // w8..w10  stability on success
    2.1072, 0.0793, 0.3246, 1.5870, // w11..w14  stability on lapse
    0.2272, 2.8755, // w15, w16  hard penalty / easy bonus
  ];

  /// Exponent of the power forgetting curve.
  static const double _decay = -0.5;

  /// Chosen so R(t = S) == 0.9 exactly.
  static const double _factor = 19.0 / 81.0;

  /// Probability of recall after [elapsedDays] with memory [stability].
  static double retrievability(double elapsedDays, double stability) {
    if (stability <= 0) return 0;
    return math.pow(1 + _factor * elapsedDays / stability, _decay).toDouble();
  }

  /// Invert the forgetting curve: days until recall drops to [retention].
  double _intervalFor(double stability) {
    final r = _config.targetRetention;
    final days = (stability / _factor) * (math.pow(r, 1 / _decay) - 1);
    return days.clamp(1.0, _config.maximumIntervalDays.toDouble());
  }

  double _initialStability(Grade g) => math.max(_w[g.value - 1], 0.1);

  double _initialDifficulty(Grade g) =>
      (_w[4] - (g.value - 3) * _w[5]).clamp(1.0, 10.0);

  double _nextDifficulty(double d, Grade g) {
    final delta = d - _w[6] * (g.value - 3);
    // Mean-revert towards the difficulty an "easy" first answer would imply,
    // so a card's difficulty doesn't drift permanently after one bad day.
    final reverted = _w[7] * _initialDifficulty(Grade.easy) + (1 - _w[7]) * delta;
    return reverted.clamp(1.0, 10.0);
  }

  double _stabilityOnSuccess(double d, double s, double r, Grade g) {
    final hardPenalty = g == Grade.hard ? _w[15] : 1.0;
    final easyBonus = g == Grade.easy ? _w[16] : 1.0;
    return s *
        (1 +
            math.exp(_w[8]) *
                (11 - d) *
                math.pow(s, -_w[9]) *
                (math.exp(_w[10] * (1 - r)) - 1) *
                hardPenalty *
                easyBonus);
  }

  double _stabilityOnLapse(double d, double s, double r) {
    final next = _w[11] *
        math.pow(d, -_w[12]) *
        (math.pow(s + 1, _w[13]) - 1) *
        math.exp(_w[14] * (1 - r));
    // FSRS 4.5: a lapse never increases stability.
    return math.min(next.toDouble(), s);
  }

  @override
  SchedulingPreview preview(SchedulingState state, DateTime now) {
    final out = <Grade, SchedulingState>{};
    for (final g in Grade.values) {
      out[g] = _applyOne(state, g, now);
    }
    return SchedulingPreview(out);
  }

  SchedulingState _applyOne(SchedulingState state, Grade g, DateTime now) {
    double stability;
    double difficulty;

    if (state.phase == CardPhase.newCard) {
      stability = _initialStability(g);
      difficulty = _initialDifficulty(g);
    } else {
      final elapsed = state.lastReview == null
          ? 0.0
          : now.difference(state.lastReview!).inSeconds / 86400.0;
      final r = retrievability(elapsed, state.stability);
      difficulty = _nextDifficulty(state.difficulty, g);
      stability = g == Grade.again
          ? _stabilityOnLapse(difficulty, state.stability, r)
          : _stabilityOnSuccess(difficulty, state.stability, r, g);
    }

    final lapsed = g == Grade.again;

    // Short intervals stay on the minute-level learning ladder so a card the
    // learner just failed comes back in the same session rather than tomorrow.
    final inLadder = state.phase == CardPhase.newCard ||
        state.phase == CardPhase.learning ||
        state.phase == CardPhase.relearning;

    if (lapsed || (inLadder && g == Grade.hard)) {
      final steps = state.phase == CardPhase.review || state.phase == CardPhase.relearning
          ? _config.relearningStepsMinutes
          : _config.learningStepsMinutes;
      final step = lapsed ? 0 : state.learningStep;
      final minutes = steps[step.clamp(0, steps.length - 1)];
      return state.copyWith(
        phase: state.phase == CardPhase.review || state.phase == CardPhase.relearning
            ? CardPhase.relearning
            : CardPhase.learning,
        stability: stability,
        difficulty: difficulty,
        due: now.add(Duration(minutes: minutes)),
        lastReview: now,
        reps: state.reps + 1,
        lapses: state.lapses + (lapsed && state.phase == CardPhase.review ? 1 : 0),
        intervalDays: 0,
        learningStep: step,
      );
    }

    if (inLadder && g == Grade.good) {
      final steps = state.phase == CardPhase.relearning
          ? _config.relearningStepsMinutes
          : _config.learningStepsMinutes;
      final nextStep = state.learningStep + 1;
      if (nextStep < steps.length) {
        return state.copyWith(
          phase: state.phase == CardPhase.newCard ? CardPhase.learning : state.phase,
          stability: stability,
          difficulty: difficulty,
          due: now.add(Duration(minutes: steps[nextStep])),
          lastReview: now,
          reps: state.reps + 1,
          intervalDays: 0,
          learningStep: nextStep,
        );
      }
      // Ladder complete — graduate to real interval scheduling.
    }

    final days = _intervalFor(stability).round().clamp(1, _config.maximumIntervalDays);
    return state.copyWith(
      phase: CardPhase.review,
      stability: stability,
      difficulty: difficulty,
      due: now.add(Duration(days: days)),
      lastReview: now,
      reps: state.reps + 1,
      intervalDays: days,
      learningStep: 0,
    );
  }

  @override
  SchedulingState apply(SchedulingState state, Grade grade, DateTime now) =>
      _applyOne(state, grade, now);
}

/// SM-2, the classic SuperMemo/original-Anki algorithm.
///
/// Simpler and fully specified, so it makes a safe default while FSRS weights
/// are being validated. Selectable in Settings.
class SM2Scheduler implements Scheduler {
  SM2Scheduler({this.config = const SchedulerConfig()});
  final SchedulerConfig config;

  @override
  String get name => 'SM-2';

  @override
  SchedulingPreview preview(SchedulingState state, DateTime now) => SchedulingPreview({
        for (final g in Grade.values) g: apply(state, g, now),
      });

  @override
  SchedulingState apply(SchedulingState state, Grade grade, DateTime now) {
    if (grade == Grade.again) {
      return state.copyWith(
        phase: CardPhase.relearning,
        due: now.add(Duration(minutes: config.relearningStepsMinutes.first)),
        lastReview: now,
        reps: state.reps + 1,
        lapses: state.lapses + 1,
        intervalDays: 0,
        learningStep: 0,
        ease: math.max(1.3, state.ease - 0.20),
      );
    }

    final inLadder = state.phase == CardPhase.newCard ||
        state.phase == CardPhase.learning ||
        state.phase == CardPhase.relearning;

    if (inLadder && grade != Grade.easy) {
      final steps = config.learningStepsMinutes;
      final next = state.learningStep + (grade == Grade.good ? 1 : 0);
      if (next < steps.length) {
        return state.copyWith(
          phase: CardPhase.learning,
          due: now.add(Duration(minutes: steps[next])),
          lastReview: now,
          reps: state.reps + 1,
          learningStep: next,
          intervalDays: 0,
        );
      }
    }

    final ease = switch (grade) {
      Grade.hard => math.max(1.3, state.ease - 0.15),
      Grade.easy => state.ease + 0.15,
      _ => state.ease,
    };

    final int days;
    if (state.intervalDays == 0) {
      days = grade == Grade.easy ? 4 : 1;
    } else if (state.intervalDays == 1) {
      days = grade == Grade.hard ? 2 : (grade == Grade.easy ? 6 : 3);
    } else {
      final multiplier = switch (grade) {
        Grade.hard => 1.2,
        Grade.easy => ease * 1.3,
        _ => ease,
      };
      days = (state.intervalDays * multiplier).round();
    }

    final clamped = days.clamp(1, config.maximumIntervalDays);
    return state.copyWith(
      phase: CardPhase.review,
      due: now.add(Duration(days: clamped)),
      lastReview: now,
      reps: state.reps + 1,
      intervalDays: clamped,
      learningStep: 0,
      ease: ease,
    );
  }
}

/// "10m", "3d", "1.2mo" — what goes under each grading button.
String formatInterval(SchedulingState next, DateTime now) {
  final d = next.due?.difference(now) ?? Duration.zero;
  if (d.inMinutes < 60) return '${math.max(1, d.inMinutes)}m';
  if (d.inHours < 24) return '${d.inHours}h';
  final days = d.inDays;
  if (days < 30) return '${math.max(1, days)}d';
  if (days < 365) return '${(days / 30).toStringAsFixed(days < 60 ? 1 : 0)}mo';
  return '${(days / 365).toStringAsFixed(1)}y';
}
