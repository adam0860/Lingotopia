import 'dart:math';

/// The two players of a rally. In this version "bot" is always a computer
/// opponent; the engine treats both sides identically, so a human opponent
/// would only need a different source of answers.
enum RallySide { you, bot }

extension RallySideX on RallySide {
  RallySide get other => this == RallySide.you ? RallySide.bot : RallySide.you;
}

/// How long a match is, and the numbers that shape play.
///
/// A match ends when someone reaches [targetScore] points or runs out of
/// [lives], whichever happens first. A miss costs the misser a life and gives
/// the other side a point, so the two counters move together; power-ups are
/// what pull them apart (a smash scores extra points, a blast takes a life
/// without a point).
class RallyRules {
  const RallyRules({
    required this.id,
    required this.label,
    required this.targetScore,
    required this.lives,
  });

  final String id;
  final String label;
  final int targetScore;
  final int lives;

  static const quick = RallyRules(id: 'quick', label: 'Quick', targetScore: 5, lives: 3);
  static const standard = RallyRules(id: 'standard', label: 'Standard', targetScore: 7, lives: 5);
  static const long = RallyRules(id: 'long', label: 'Long', targetScore: 10, lives: 7);

  static const all = [quick, standard, long];

  static RallyRules byId(String? id) =>
      all.firstWhere((r) => r.id == id, orElse: () => standard);

  // --- Power-ups ------------------------------------------------------------

  /// Correct answers in a row that earn a shield.
  static const int shieldStreak = 3;

  /// Quick correct answers in a row that earn a smash.
  static const int smashFastStreak = 3;

  /// Every this-many correct answers in a row the opponent loses a life.
  static const int blastEvery = 6;

  /// A correct answer within this fraction of the time limit is "fast".
  static const double fastFraction = 0.4;

  /// Extra points when a smash is not returned.
  static const int smashBonus = 1;

  /// A smash leaves the receiver this fraction of the normal time.
  static const double smashTimeFactor = 0.55;

  // --- Time -----------------------------------------------------------------

  static const double wordSeconds = 9;
  static const double phraseSeconds = 14;

  /// Seconds allowed for one answer. The ball speeds up as a rally goes on
  /// (down to 60% of the base time), and a smash cuts the time again.
  static double limitSeconds({
    required bool phrase,
    required int rallyLength,
    required bool smashed,
  }) {
    final base = phrase ? phraseSeconds : wordSeconds;
    final squeeze = max(0.6, 1 - 0.04 * rallyLength);
    return base * squeeze * (smashed ? smashTimeFactor : 1.0);
  }
}

/// A computer opponent. Difficulty is how often it is right and how long it
/// takes: a slow, error-prone bot is easy to beat and rarely earns power-ups.
class BotProfile {
  const BotProfile({
    required this.id,
    required this.name,
    required this.tagline,
    required this.accuracy,
    required this.meanSeconds,
    required this.spreadSeconds,
  });

  final String id;
  final String name;
  final String tagline;

  /// Chance of a right answer when it answers in time (0..1).
  final double accuracy;

  /// Typical thinking time, and how much it varies.
  final double meanSeconds;
  final double spreadSeconds;

  static const rookie = BotProfile(
    id: 'rookie',
    name: 'Rookie',
    tagline: 'Still learning the words',
    accuracy: 0.55,
    meanSeconds: 6.5,
    spreadSeconds: 1.8,
  );
  static const casual = BotProfile(
    id: 'casual',
    name: 'Casual',
    tagline: 'Gets there, eventually',
    accuracy: 0.68,
    meanSeconds: 5.4,
    spreadSeconds: 1.6,
  );
  static const skilled = BotProfile(
    id: 'skilled',
    name: 'Skilled',
    tagline: 'Solid and steady',
    accuracy: 0.80,
    meanSeconds: 4.2,
    spreadSeconds: 1.3,
  );
  static const expert = BotProfile(
    id: 'expert',
    name: 'Expert',
    tagline: 'Fast and rarely wrong',
    accuracy: 0.90,
    meanSeconds: 3.2,
    spreadSeconds: 1.0,
  );
  static const champion = BotProfile(
    id: 'champion',
    name: 'Champion',
    tagline: 'Almost unbeatable',
    accuracy: 0.96,
    meanSeconds: 2.3,
    spreadSeconds: 0.7,
  );

  static const all = [rookie, casual, skilled, expert, champion];

  static BotProfile byId(String? id) =>
      all.firstWhere((b) => b.id == id, orElse: () => casual);
}

/// What the bot did with one ball.
class BotAnswer {
  const BotAnswer({
    required this.correct,
    required this.seconds,
    required this.timedOut,
  });

  final bool correct;

  /// When it answered (or the time limit, if it ran out).
  final double seconds;
  final bool timedOut;
}

double _gaussian(Random rnd) {
  // Box-Muller; the 1 - x keeps log() away from zero.
  final u1 = 1 - rnd.nextDouble();
  final u2 = rnd.nextDouble();
  return sqrt(-2 * log(u1)) * cos(2 * pi * u2);
}

/// Decide how the bot answers a ball with [limit] seconds on the clock.
///
/// It always "thinks" for a random time around its mean; if that is longer than
/// the limit it times out, so a slow bot loses points to speed alone as well as
/// to mistakes. A smash rattles it: accuracy drops by 15 points. Sentences take
/// half as long again.
BotAnswer botAnswer(
  BotProfile bot, {
  required double limit,
  required bool smashed,
  required Random rnd,
  bool phrase = false,
}) {
  // A sentence takes longer to read than a word, for a bot as for a person.
  final scale = phrase ? 1.5 : 1.0;
  final t = max(
      0.8, (bot.meanSeconds + _gaussian(rnd) * bot.spreadSeconds) * scale);
  if (t >= limit) {
    return BotAnswer(correct: false, seconds: limit, timedOut: true);
  }
  final accuracy = (bot.accuracy - (smashed ? 0.15 : 0)).clamp(0.05, 0.99);
  return BotAnswer(
    correct: rnd.nextDouble() < accuracy,
    seconds: t,
    timedOut: false,
  );
}
