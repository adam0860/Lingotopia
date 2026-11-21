/// How well the learner knows a word, from their flashcards and from the
/// games. Pure Dart (no Flutter, no storage), so the policy is unit-tested.
///
/// Two independent streams of evidence feed one label:
///
///  * Flashcards: the spaced-repetition state of the word's card. How long
///    the scheduler thinks the word will be remembered is the best single
///    measure there is.
///  * Games and drills: a plain tally of right and wrong answers, since
///    games do not schedule anything.
///
/// The better of the two wins, then two caps pull the label down for a word
/// that is giving trouble right now.
library;

import '../srs/scheduler.dart';

/// Ordered from least to most known.
enum Knowledge {
  /// No evidence at all: never met on a card or in a game.
  unknown,

  /// Met, but not learned yet.
  seen,

  /// Getting there: remembered for days, or mostly right in games.
  familiar,

  /// Remembered for weeks, or reliably right in games.
  known;

  String get label => switch (this) {
        Knowledge.unknown => 'Unknown',
        Knowledge.seen => 'Seen before',
        Knowledge.familiar => 'Familiar',
        Knowledge.known => 'Known',
      };

  bool operator <(Knowledge o) => index < o.index;
  bool operator >(Knowledge o) => index > o.index;
}

/// The thresholds. Written down once so the settings text, the legend and the
/// tests all quote the same numbers.
class KnowledgeRules {
  KnowledgeRules._();

  /// A card the scheduler expects to remember for this many days is
  /// [Knowledge.familiar], and for this many, [Knowledge.known].
  static const int familiarDays = 4;
  static const int knownDays = 21;

  /// Games: answers needed, and the share of them that must be right.
  static const int familiarAnswers = 3;
  static const double familiarAccuracy = 0.75;
  static const int knownAnswers = 8;
  static const double knownAccuracy = 0.90;
}

/// Right and wrong answers to one word in the games and drills (not the
/// flashcards, which have their own schedule).
class WordPractice {
  const WordPractice({
    required this.cardId,
    required this.deckId,
    this.right = 0,
    this.wrong = 0,
    this.lastAt,
  });

  final String cardId;
  final String deckId;
  final int right;
  final int wrong;
  final DateTime? lastAt;

  int get answers => right + wrong;
  double get accuracy => answers == 0 ? 0 : right / answers;

  WordPractice after({required bool correct, required DateTime at}) =>
      WordPractice(
        cardId: cardId,
        deckId: deckId,
        right: right + (correct ? 1 : 0),
        wrong: wrong + (correct ? 0 : 1),
        lastAt: at,
      );

  Map<String, Object?> toMap() => {
        'card_id': cardId,
        'deck_id': deckId,
        'right_count': right,
        'wrong_count': wrong,
        'last_at': lastAt?.millisecondsSinceEpoch,
      };

  factory WordPractice.fromMap(Map<String, Object?> m) {
    final at = m['last_at'] as int?;
    return WordPractice(
      cardId: m['card_id'] as String,
      deckId: m['deck_id'] as String,
      right: (m['right_count'] as int?) ?? 0,
      wrong: (m['wrong_count'] as int?) ?? 0,
      lastAt: at == null ? null : DateTime.fromMillisecondsSinceEpoch(at),
    );
  }
}

/// Everything known about one word.
class WordEvidence {
  const WordEvidence({
    this.srs,
    this.practice,
    this.inDifficultBank = false,
    this.missStreak = 0,
  });

  /// The flashcard's scheduling state; null when the card was never studied.
  final SchedulingState? srs;

  /// The games tally; null when the word never came up in a game.
  final WordPractice? practice;

  /// The word is in the difficult-words bank.
  final bool inDifficultBank;

  /// Wrong answers in a row, anywhere, right now.
  final int missStreak;
}

/// The level the flashcard alone gives.
Knowledge levelFromCard(SchedulingState? s) {
  if (s == null || s.phase == CardPhase.newCard) return Knowledge.unknown;
  if (s.phase == CardPhase.learning || s.phase == CardPhase.relearning) {
    return Knowledge.seen;
  }
  final days = s.stability > s.intervalDays ? s.stability : s.intervalDays.toDouble();
  if (days >= KnowledgeRules.knownDays) return Knowledge.known;
  if (days >= KnowledgeRules.familiarDays) return Knowledge.familiar;
  return Knowledge.seen;
}

/// The level the games alone give.
Knowledge levelFromPractice(WordPractice? p) {
  if (p == null || p.answers == 0) return Knowledge.unknown;
  if (p.answers >= KnowledgeRules.knownAnswers &&
      p.accuracy >= KnowledgeRules.knownAccuracy) {
    return Knowledge.known;
  }
  if (p.answers >= KnowledgeRules.familiarAnswers &&
      p.accuracy >= KnowledgeRules.familiarAccuracy) {
    return Knowledge.familiar;
  }
  return Knowledge.seen;
}

Knowledge _lower(Knowledge a, Knowledge b) => a < b ? a : b;

/// The one label for a word: the better stream, held down while the word is
/// in the difficult bank (at most [Knowledge.seen]) or was missed last time
/// (at most [Knowledge.familiar]).
Knowledge classifyWord(WordEvidence e) {
  final fromCard = levelFromCard(e.srs);
  final fromGames = levelFromPractice(e.practice);
  var level = fromCard > fromGames ? fromCard : fromGames;
  if (e.inDifficultBank) level = _lower(level, Knowledge.seen);
  if (e.missStreak >= 1) level = _lower(level, Knowledge.familiar);
  return level;
}

/// Why a word has its label, in a line, for the word sheet.
String explainKnowledge(WordEvidence e) {
  final parts = <String>[];
  final s = e.srs;
  if (s != null && s.phase != CardPhase.newCard) {
    if (s.phase == CardPhase.learning || s.phase == CardPhase.relearning) {
      parts.add('Flashcard: still being learned');
    } else {
      final days = s.stability > s.intervalDays ? s.stability : s.intervalDays.toDouble();
      parts.add('Flashcard: remembered for about ${days.round()} days');
    }
  }
  final p = e.practice;
  if (p != null && p.answers > 0) {
    parts.add('Games: ${p.right} of ${p.answers} right');
  }
  if (e.inDifficultBank) parts.add('In your difficult words');
  if (parts.isEmpty) return 'Not met on a card or in a game yet';
  return parts.join(' · ');
}
