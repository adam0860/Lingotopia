import '../srs/scheduler.dart';
import 'streak.dart';
import 'trophies.dart';
import 'xp_rules.dart';

/// Where XP came from. Stored with each XP entry.
enum ProgressSource {
  review,
  lesson,
  ladder,
  rally,
  trophy,
  backfill,
  match,
  recall,
  reading,
  writing,
  military,
}

/// One thing the learner did that is worth XP and moves some counters.
///
/// Counters are plain named numbers; trophies and the profile read them. An
/// event only says what happened: [ProgressEngine] decides what it unlocks.
class ProgressEvent {
  const ProgressEvent({
    required this.source,
    required this.xp,
    this.deckId,
    this.increments = const {},
    this.maxes = const {},
  });

  final ProgressSource source;
  final int xp;

  /// The deck it happened in, when there is one.
  final String? deckId;

  /// Counters to add to.
  final Map<String, int> increments;

  /// Counters that keep the highest value ever seen.
  final Map<String, int> maxes;

  /// One flashcard answer.
  factory ProgressEvent.review({
    required Grade grade,
    required bool wasNew,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.review,
        xp: XpRules.forGrade(grade) + (wasNew ? XpRules.newCardBonus : 0),
        deckId: deckId,
        increments: {'reviews': 1, if (wasNew) 'cards_learned': 1},
      );

  /// A lesson attempt that was finished (passed or not).
  factory ProgressEvent.lesson({
    required int correct,
    required int total,
    required bool firstCompletion,
    required bool passed,
    required String deckId,
  }) {
    final perfect = total > 0 && correct == total;
    return ProgressEvent(
      source: ProgressSource.lesson,
      xp: XpRules.lesson(
        correct: correct,
        total: total,
        firstCompletion: firstCompletion,
      ),
      deckId: deckId,
      increments: {
        if (passed && firstCompletion) 'lessons': 1,
        if (perfect) 'lessons_perfect': 1,
      },
    );
  }

  /// A finished reading or listening test. [passed] is the pass mark
  /// (see ReadingRules); [firstPass] is the first time this passage was
  /// passed in this mode.
  factory ProgressEvent.reading({
    required bool listening,
    required int correct,
    required int total,
    required bool passed,
    required bool firstPass,
    required String deckId,
  }) {
    final perfect = total > 0 && correct == total;
    final counter = listening ? 'listenings' : 'readings';
    return ProgressEvent(
      source: ProgressSource.reading,
      xp: XpRules.reading(correct: correct, total: total, firstPass: firstPass),
      deckId: deckId,
      increments: {
        if (passed && firstPass) counter: 1,
        if (perfect && firstPass) 'reading_perfect': 1,
      },
    );
  }

  /// A finished character in Writing practice. [known] is whether it had
  /// already been written from memory with a star; [firstEver] whether it had
  /// never been finished before. [stars] is 0 for Watch and Trace.
  factory ProgressEvent.writing({
    required bool write,
    required int stars,
    required int strokes,
    required bool known,
    required bool firstEver,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.writing,
        xp: XpRules.writing(
          write: write,
          stars: stars,
          strokes: strokes,
          known: known,
          firstEver: firstEver,
        ),
        deckId: deckId,
        increments: {
          'characters_practised': 1,
          if (write && stars > 0 && !known) 'characters_learned': 1,
        },
      );

  /// A finished quiz in the Russian military section. [newCorrect] counts
  /// right answers on terms not yet known, [knownCorrect] on known ones.
  factory ProgressEvent.militaryQuiz({
    required int newCorrect,
    required int knownCorrect,
    required int total,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.military,
        xp: XpRules.militaryQuiz(
          newCorrect: newCorrect,
          knownCorrect: knownCorrect,
          total: total,
        ),
        deckId: deckId,
        increments: {
          'military_quizzes': 1,
          if (newCorrect > 0) 'military_terms_learned': newCorrect,
        },
      );

  /// "Got it" on a new term in the military flashcards.
  factory ProgressEvent.militaryCard({required String deckId}) => ProgressEvent(
        source: ProgressSource.military,
        xp: XpRules.militaryCard(known: false),
        deckId: deckId,
        increments: {'military_terms_learned': 1},
      );

  /// The prizes at the two safe havens of Lingo Ladder.
  static const int ladderHaven1 = 1000;
  static const int ladderHaven2 = 32000;

  /// A finished Lingo Ladder game.
  factory ProgressEvent.ladder({
    required int correct,
    required bool won,
    required int prize,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.ladder,
        xp: XpRules.ladder(correct: correct, won: won),
        deckId: deckId,
        increments: {
          'ladder_played': 1,
          if (correct > 0) 'ladder_correct': correct,
          if (won) 'ladder_won': 1,
          if (prize >= ladderHaven1) 'ladder_h1': 1,
          if (prize >= ladderHaven2) 'ladder_h2': 1,
        },
      );

  /// A finished Lingo Rally match against a bot ([botTier] 0 to 4).
  factory ProgressEvent.rally({
    required bool won,
    required int correct,
    required int botTier,
    required int bestStreak,
    required int blasts,
    required int smashes,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.rally,
        xp: XpRules.rally(won: won, correct: correct, botTier: botTier),
        deckId: deckId,
        increments: {
          'rally_played': 1,
          if (won) 'rally_won': 1,
          if (won && botTier >= 4) 'rally_beat_champion': 1,
          if (blasts > 0) 'rally_blasts': blasts,
          if (smashes > 0) 'rally_smashes': smashes,
        },
        maxes: {'rally_best_streak': bestStreak},
      );

  /// A finished Word Match run: [boards] cleared of the [pairs] matched, and
  /// how many of those boards had no wrong pick at all ([flawless]).
  factory ProgressEvent.wordMatch({
    required int boards,
    required int pairs,
    required int flawless,
    required bool finished,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.match,
        xp: XpRules.wordMatch(pairs: pairs, flawless: flawless, finished: finished),
        deckId: deckId,
        increments: {
          'match_played': 1,
          if (boards > 0) 'match_boards': boards,
          if (flawless > 0) 'match_flawless': flawless,
        },
      );

  /// A finished Quick Recall round. [reach] is the deepest frequency rank the
  /// player got right, a rough measure of how far into the deck they know.
  factory ProgressEvent.quickRecall({
    required int correct,
    required int reach,
    required int bestStreak,
    required String deckId,
  }) =>
      ProgressEvent(
        source: ProgressSource.recall,
        xp: XpRules.quickRecall(correct: correct),
        deckId: deckId,
        increments: {'recall_played': 1},
        maxes: {
          'recall_best': correct,
          'recall_reach': reach,
          'recall_best_streak': bestStreak,
        },
      );
}

/// One entry in the XP log.
class XpRow {
  const XpRow({
    required this.at,
    required this.day,
    required this.amount,
    required this.source,
    this.deckId,
  });

  final DateTime at;
  final String day;
  final int amount;
  final ProgressSource source;
  final String? deckId;
}

/// Everything the progress system remembers.
class ProgressState {
  ProgressState({
    this.totalXp = 0,
    Map<String, int>? dailyXp,
    Map<String, int>? counters,
    Map<String, int>? trophies,
  })  : dailyXp = dailyXp ?? {},
        counters = counters ?? {},
        trophies = trophies ?? {};

  int totalXp;

  /// XP per calendar day, by day key.
  final Map<String, int> dailyXp;

  /// Named counters.
  final Map<String, int> counters;

  /// Trophy id to the time it was unlocked, in epoch milliseconds.
  final Map<String, int> trophies;
}

/// What one event changed: what to celebrate, and what to write to disk.
class ProgressDelta {
  const ProgressDelta({
    required this.at,
    required this.eventXp,
    required this.trophyXp,
    required this.levelBefore,
    required this.levelAfter,
    required this.streakBefore,
    required this.streakAfter,
    required this.streakExtended,
    required this.freezeEarned,
    required this.goalReached,
    required this.todayXp,
    required this.newTrophies,
    required this.xpRows,
    required this.counterWrites,
    required this.trophyWrites,
  });

  final DateTime at;

  /// XP from the event itself, and from trophies it unlocked.
  final int eventXp;
  final int trophyXp;

  final int levelBefore;
  final int levelAfter;

  final StreakState streakBefore;
  final StreakState streakAfter;

  /// This was the first activity of the day and the streak grew (or began).
  final bool streakExtended;

  /// The streak reached a multiple that earns a freeze.
  final bool freezeEarned;

  /// This crossed today's goal.
  final bool goalReached;

  /// Total XP earned today after this event.
  final int todayXp;

  final List<Trophy> newTrophies;

  // What the store must write.
  final List<XpRow> xpRows;
  final Map<String, int> counterWrites;
  final Map<String, int> trophyWrites;

  int get xpGained => eventXp + trophyXp;
  bool get leveledUp => levelAfter > levelBefore;

  /// Worth interrupting the learner for: a toast, a sound.
  bool get hasCelebration =>
      leveledUp || newTrophies.isNotEmpty || streakExtended || goalReached;

  /// Nothing to write.
  bool get isEmpty =>
      xpRows.isEmpty && counterWrites.isEmpty && trophyWrites.isEmpty;
}
