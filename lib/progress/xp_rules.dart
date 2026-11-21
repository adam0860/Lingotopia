import 'dart:math';

import '../srs/scheduler.dart';

/// Where a level starts and ends, and what it is called.
class LevelInfo {
  const LevelInfo({
    required this.level,
    required this.startXp,
    required this.nextXp,
    required this.xp,
  });

  final int level;

  /// Total XP at which this level began, and at which the next one begins.
  final int startXp;
  final int nextXp;

  /// The learner's total XP.
  final int xp;

  /// XP earned inside this level, and the size of the level.
  int get into => xp - startXp;
  int get span => nextXp - startXp;
  int get remaining => nextXp - xp;

  /// 0..1 through the current level.
  double get progress => span == 0 ? 0 : (into / span).clamp(0.0, 1.0);

  String get title => XpRules.titleFor(level);
}

/// How much XP each kind of effort is worth, and how XP becomes a level.
///
/// The numbers are deliberately small and round so the learner can see where
/// they came from: a "Good" card is 4, a first-time lesson is 15 plus 3 per
/// right answer. A normal day of study lands around the default goal.
class XpRules {
  XpRules._();

  /// One flashcard answer.
  static int forGrade(Grade g) => switch (g) {
        Grade.again => 1,
        Grade.hard => 2,
        Grade.good => 4,
        Grade.easy => 5,
      };

  /// Extra for the first time a card is ever answered.
  static const int newCardBonus = 3;

  /// A lesson attempt. [correct] is first-try right answers out of [total].
  /// The first time a lesson is passed pays in full; repeats, and attempts
  /// that do not pass, are worth half.
  static int lesson({
    required int correct,
    required int total,
    required bool firstCompletion,
  }) {
    final perfect = total > 0 && correct == total;
    final xp = 15 + 3 * correct + (perfect ? 10 : 0);
    return firstCompletion ? xp : (xp / 2).ceil();
  }

  /// A finished reading or listening test: 8 for finishing, 4 per right
  /// answer, 8 more for all of them. The first pass of a passage pays in
  /// full; repeats, and attempts that do not pass, pay half.
  static int reading({
    required int correct,
    required int total,
    required bool firstPass,
  }) {
    final perfect = total > 0 && correct == total;
    final xp = 8 + 4 * correct + (perfect ? 8 : 0);
    return firstPass ? xp : (xp / 2).ceil();
  }

  /// A finished character in Writing practice. Watching earns nothing.
  ///
  /// A character still being learned (never written from memory with a star)
  /// pays in full: 4 for tracing, 6 for writing, 4 more for three stars or 2
  /// for two, 1 more per 6 strokes, and 3 extra the very first time it is
  /// finished. Once it is known the same effort pays about a third: 1 for
  /// tracing, 2 for writing, 1 more for three stars.
  static int writing({
    required bool write,
    required int stars,
    required int strokes,
    required bool known,
    required bool firstEver,
  }) {
    if (known) {
      return write ? 2 + (stars >= 3 ? 1 : 0) : 1;
    }
    var xp = write ? 6 + (stars >= 3 ? 4 : (stars == 2 ? 2 : 0)) : 4;
    xp += strokes ~/ 6;
    if (firstEver) xp += 3;
    return xp;
  }

  /// A finished quiz in the Russian military section. A term still being
  /// learned pays 3 for a right answer, a term already known pays 1; 5 more
  /// for finishing and 5 for getting every question right.
  static int militaryQuiz({
    required int newCorrect,
    required int knownCorrect,
    required int total,
  }) {
    final perfect = total > 0 && newCorrect + knownCorrect == total;
    return 3 * newCorrect +
        knownCorrect +
        (total > 0 ? 5 : 0) +
        (perfect ? 5 : 0);
  }

  /// "Got it" on a flashcard in the military section: 2 the first time, and
  /// nothing for a term already known, so the card deck cannot be farmed.
  static int militaryCard({required bool known}) => known ? 0 : 2;

  /// A finished Lingo Ladder game.
  static int ladder({required int correct, required bool won}) =>
      10 * correct + (won ? 150 : 0);

  /// Bonus for beating each Lingo Rally bot, weakest to strongest.
  static const List<int> rallyBotBonus = [0, 10, 20, 35, 60];

  /// A finished Lingo Rally match. [botTier] is the bot's position, 0 to 4.
  static int rally({
    required bool won,
    required int correct,
    required int botTier,
  }) {
    final tier = botTier.clamp(0, rallyBotBonus.length - 1);
    final base = won ? 40 + rallyBotBonus[tier] : 10;
    return base + min(2 * correct, 40);
  }

  /// A finished Word Match run: 2 per pair, 5 for each board cleared without a
  /// wrong pick, and 15 for clearing every board.
  static int wordMatch({
    required int pairs,
    required int flawless,
    required bool finished,
  }) =>
      2 * pairs + 5 * flawless + (finished ? 15 : 0);

  /// One Quick Recall round: 2 per word recalled, up to 80.
  static int quickRecall({required int correct}) => min(2 * correct, 80);

  // --- Levels ---------------------------------------------------------------

  /// Level n begins at 50 * (n - 1)^2 XP: level 2 at 50, level 5 at 800,
  /// level 10 at 4,050, level 30 at 42,050.
  static const int _unit = 50;

  static int startOf(int level) => _unit * (level - 1) * (level - 1);

  static LevelInfo levelFor(int xp) {
    final safe = xp < 0 ? 0 : xp;
    final level = sqrt(safe / _unit).floor() + 1;
    return LevelInfo(
      level: level,
      startXp: startOf(level),
      nextXp: startOf(level + 1),
      xp: safe,
    );
  }

  static const List<(int, String)> _titles = [
    (1, 'Newcomer'),
    (3, 'Tourist'),
    (5, 'Wanderer'),
    (8, 'Explorer'),
    (12, 'Traveler'),
    (16, 'Pathfinder'),
    (20, 'Local'),
    (25, 'Insider'),
    (30, 'Polyglot'),
    (40, 'Linguist'),
    (50, 'Lingotopian'),
  ];

  static String titleFor(int level) {
    var name = _titles.first.$2;
    for (final (from, title) in _titles) {
      if (level >= from) name = title;
    }
    return name;
  }

  // --- Daily goal -----------------------------------------------------------

  static const int defaultGoal = 60;

  static const List<(String, int)> goalPresets = [
    ('Casual', 30),
    ('Regular', 60),
    ('Serious', 100),
    ('Intense', 200),
  ];
}
