import 'rally_models.dart';

/// Everything that can happen as a result of one answer, in order. The screen
/// turns these into banners and sounds; the engine only reports them.
enum RallyEventType {
  /// The ball was sent back.
  returned,

  /// The ball got past: the other side scores.
  missed,

  /// A shield soaked up a miss.
  shieldUsed,
  shieldEarned,

  /// The return is a smash: faster, and worth extra if it is not returned.
  smashEarned,

  /// A smash that was returned anyway.
  smashBlocked,

  /// The opponent lost a life to a long streak.
  blast,
  matchOver,
}

class RallyEvent {
  const RallyEvent(this.type, this.side, {this.points = 0, this.smash = false});

  final RallyEventType type;

  /// The side the event is about: who earned the power-up, who missed, who won.
  final RallySide side;

  /// Points scored by the other side (for [RallyEventType.missed]).
  final int points;

  /// For [RallyEventType.missed]: the ball was a smash.
  final bool smash;
}

class SideState {
  SideState(this.lives);

  int score = 0;
  int lives;

  /// Correct answers in a row, and quick ones in a row.
  int streak = 0;
  int fastStreak = 0;
  int bestStreak = 0;

  bool shield = false;

  int answered = 0;
  int correct = 0;
  int fast = 0;

  int shieldsEarned = 0;
  int smashesEarned = 0;
  int blastsLanded = 0;
}

/// The rules of one match, with no UI and no randomness in it.
///
/// Each call to [answer] resolves the ball that is currently with [toAnswer].
/// Human and bot answers go through exactly the same path.
class RallyMatch {
  RallyMatch({required this.rules})
      : you = SideState(rules.lives),
        bot = SideState(rules.lives);

  final RallyRules rules;
  final SideState you;
  final SideState bot;

  /// Who has the ball and must answer.
  RallySide toAnswer = RallySide.you;

  /// Exchanges since the last point; drives the speed-up.
  int rallyLength = 0;

  /// The ball now with [toAnswer] is a smash.
  bool smashIncoming = false;

  RallySide? winner;

  bool get isOver => winner != null;

  SideState state(RallySide s) => s == RallySide.you ? you : bot;

  /// Seconds allowed on the ball that is with [toAnswer] now.
  double limitFor({required bool phrase}) => RallyRules.limitSeconds(
        phrase: phrase,
        rallyLength: rallyLength,
        smashed: smashIncoming,
      );

  List<RallyEvent> answer({
    required bool correct,
    required double seconds,
    required double limit,
  }) {
    if (isOver) throw StateError('The match is over.');

    final side = toAnswer;
    final me = state(side);
    final foe = state(side.other);
    final events = <RallyEvent>[];
    me.answered++;

    if (correct) {
      me.correct++;
      me.streak++;
      if (me.streak > me.bestStreak) me.bestStreak = me.streak;
      final fast = seconds <= limit * RallyRules.fastFraction;
      if (fast) me.fast++;
      me.fastStreak = fast ? me.fastStreak + 1 : 0;
      events.add(RallyEvent(RallyEventType.returned, side));

      if (smashIncoming) {
        events.add(RallyEvent(RallyEventType.smashBlocked, side));
        smashIncoming = false;
      }

      if (me.streak == RallyRules.shieldStreak && !me.shield) {
        me.shield = true;
        me.shieldsEarned++;
        events.add(RallyEvent(RallyEventType.shieldEarned, side));
      }

      var smashing = false;
      if (me.fastStreak >= RallyRules.smashFastStreak) {
        me.fastStreak = 0;
        me.smashesEarned++;
        smashing = true;
        events.add(RallyEvent(RallyEventType.smashEarned, side));
      }

      if (me.streak % RallyRules.blastEvery == 0) {
        foe.lives--;
        me.blastsLanded++;
        events.add(RallyEvent(RallyEventType.blast, side));
        if (foe.lives <= 0) {
          winner = side;
          events.add(RallyEvent(RallyEventType.matchOver, side));
          return events;
        }
      }

      smashIncoming = smashing;
      rallyLength++;
      toAnswer = side.other;
      return events;
    }

    // A miss.
    me.streak = 0;
    me.fastStreak = 0;
    final wasSmash = smashIncoming;
    smashIncoming = false;
    rallyLength = 0;

    if (me.shield) {
      me.shield = false;
      events.add(RallyEvent(RallyEventType.shieldUsed, side));
      return events; // the same side receives the ball again
    }

    me.lives--;
    final points = wasSmash ? 1 + RallyRules.smashBonus : 1;
    foe.score += points;
    events.add(RallyEvent(RallyEventType.missed, side, points: points, smash: wasSmash));

    if (foe.score >= rules.targetScore || me.lives <= 0) {
      winner = side.other;
      events.add(RallyEvent(RallyEventType.matchOver, side.other));
    }
    // The side that just missed receives the next serve.
    return events;
  }
}
