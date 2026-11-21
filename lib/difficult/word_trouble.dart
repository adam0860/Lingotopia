/// The "difficult words" rules. Pure Dart (no Flutter, no storage) so the
/// whole policy can be unit-tested.
///
/// A word is a *difficult word* once it has been answered wrongly several
/// times in a row, wherever it was asked: a flashcard, Lingo Ladder, Lingo
/// Rally, Word Match or Quick Recall all count, in one shared run of answers.
/// It leaves the bank again after a few right answers in a row, so the bank is
/// "the words giving me trouble now", not a graveyard of every slip.
library;

/// Where an answer came from. Stored by [name], so adding a value is safe.
enum AnswerSource {
  flashcard,
  drill,
  ladder,
  rally,
  match,
  recall;

  static AnswerSource byName(String? name) {
    for (final s in values) {
      if (s.name == name) return s;
    }
    return flashcard;
  }

  /// Wording for "last missed in ...".
  String get label => switch (this) {
        AnswerSource.flashcard => 'Flashcards',
        AnswerSource.drill => 'Difficult words practice',
        AnswerSource.ladder => 'Lingo Ladder',
        AnswerSource.rally => 'Lingo Rally',
        AnswerSource.match => 'Word Match',
        AnswerSource.recall => 'Quick Recall',
      };
}

/// How many wrong or right answers in a row move a word in or out of the bank.
class TroubleRules {
  const TroubleRules({this.missesToAdd = 2, this.correctToClear = 3})
      : assert(missesToAdd >= 1),
        assert(correctToClear >= 1);

  /// Wrong answers in a row that put a word in the bank.
  final int missesToAdd;

  /// Right answers in a row that take a banked word out again.
  final int correctToClear;

  static const standard = TroubleRules();

  /// The values the settings offer.
  static const missChoices = [2, 3, 4];
  static const clearChoices = [2, 3, 5];
}

/// What an answer did to the bank.
enum TroubleEvent {
  /// Nothing worth telling the learner.
  none,

  /// The word has just joined the bank.
  added,

  /// The word has just left the bank: it is no longer a problem.
  cleared,
}

/// Everything remembered about one word's answers. A word only has a row once
/// it has been missed.
class WordTrouble {
  const WordTrouble({
    required this.cardId,
    required this.deckId,
    this.missStreak = 0,
    this.hitStreak = 0,
    this.totalMisses = 0,
    this.timesAdded = 0,
    this.inBank = false,
    this.addedAt,
    this.lastMissAt,
    this.lastAnswerAt,
    this.clearedAt,
    this.lastSource = AnswerSource.flashcard,
  });

  final String cardId;
  final String deckId;

  /// Wrong answers in a row right now.
  final int missStreak;

  /// Right answers in a row since the last miss (counted while in the bank).
  final int hitStreak;

  /// Every wrong answer ever, across all appearances.
  final int totalMisses;

  /// How many times the word has joined the bank (it can come back).
  final int timesAdded;

  final bool inBank;
  final DateTime? addedAt;
  final DateTime? lastMissAt;
  final DateTime? lastAnswerAt;
  final DateTime? clearedAt;

  /// Where the latest miss happened.
  final AnswerSource lastSource;

  /// Right answers still needed to leave the bank (0 when not in it).
  int correctStillNeeded(TroubleRules rules) =>
      inBank ? (rules.correctToClear - hitStreak).clamp(0, 1 << 20) : 0;

  WordTrouble copyWith({
    int? missStreak,
    int? hitStreak,
    int? totalMisses,
    int? timesAdded,
    bool? inBank,
    DateTime? addedAt,
    DateTime? lastMissAt,
    DateTime? lastAnswerAt,
    DateTime? clearedAt,
    AnswerSource? lastSource,
  }) =>
      WordTrouble(
        cardId: cardId,
        deckId: deckId,
        missStreak: missStreak ?? this.missStreak,
        hitStreak: hitStreak ?? this.hitStreak,
        totalMisses: totalMisses ?? this.totalMisses,
        timesAdded: timesAdded ?? this.timesAdded,
        inBank: inBank ?? this.inBank,
        addedAt: addedAt ?? this.addedAt,
        lastMissAt: lastMissAt ?? this.lastMissAt,
        lastAnswerAt: lastAnswerAt ?? this.lastAnswerAt,
        clearedAt: clearedAt ?? this.clearedAt,
        lastSource: lastSource ?? this.lastSource,
      );

  /// The state after one answer, and what it did to the bank.
  ///
  /// A right answer ends a run of misses. For a word in the bank it also
  /// counts towards leaving; a wrong answer there starts the count again.
  /// A word not in the bank joins it when its misses in a row reach
  /// [TroubleRules.missesToAdd].
  (WordTrouble, TroubleEvent) answered({
    required bool correct,
    required DateTime at,
    required AnswerSource source,
    TroubleRules rules = TroubleRules.standard,
  }) {
    if (correct) {
      if (!inBank) {
        // Keeps the run of misses broken; nothing else to remember.
        return (copyWith(missStreak: 0, hitStreak: 0, lastAnswerAt: at), TroubleEvent.none);
      }
      final hits = hitStreak + 1;
      if (hits >= rules.correctToClear) {
        return (
          copyWith(
            missStreak: 0,
            hitStreak: 0,
            inBank: false,
            clearedAt: at,
            lastAnswerAt: at,
          ),
          TroubleEvent.cleared,
        );
      }
      return (
        copyWith(missStreak: 0, hitStreak: hits, lastAnswerAt: at),
        TroubleEvent.none,
      );
    }

    final misses = missStreak + 1;
    final base = copyWith(
      missStreak: misses,
      hitStreak: 0,
      totalMisses: totalMisses + 1,
      lastMissAt: at,
      lastAnswerAt: at,
      lastSource: source,
    );
    if (!inBank && misses >= rules.missesToAdd) {
      return (
        base.copyWith(inBank: true, addedAt: at, timesAdded: timesAdded + 1),
        TroubleEvent.added,
      );
    }
    return (base, TroubleEvent.none);
  }

  /// A word with no history, for its first answer.
  static WordTrouble fresh(String cardId, String deckId) =>
      WordTrouble(cardId: cardId, deckId: deckId);

  Map<String, Object?> toMap() => {
        'card_id': cardId,
        'deck_id': deckId,
        'miss_streak': missStreak,
        'hit_streak': hitStreak,
        'total_misses': totalMisses,
        'times_added': timesAdded,
        'in_bank': inBank ? 1 : 0,
        'added_at': addedAt?.millisecondsSinceEpoch,
        'last_miss_at': lastMissAt?.millisecondsSinceEpoch,
        'last_answer_at': lastAnswerAt?.millisecondsSinceEpoch,
        'cleared_at': clearedAt?.millisecondsSinceEpoch,
        'last_source': lastSource.name,
      };

  static DateTime? _time(Object? v) =>
      v is int ? DateTime.fromMillisecondsSinceEpoch(v) : null;

  factory WordTrouble.fromMap(Map<String, Object?> m) => WordTrouble(
        cardId: m['card_id'] as String,
        deckId: m['deck_id'] as String,
        missStreak: (m['miss_streak'] as int?) ?? 0,
        hitStreak: (m['hit_streak'] as int?) ?? 0,
        totalMisses: (m['total_misses'] as int?) ?? 0,
        timesAdded: (m['times_added'] as int?) ?? 0,
        inBank: ((m['in_bank'] as int?) ?? 0) != 0,
        addedAt: _time(m['added_at']),
        lastMissAt: _time(m['last_miss_at']),
        lastAnswerAt: _time(m['last_answer_at']),
        clearedAt: _time(m['cleared_at']),
        lastSource: AnswerSource.byName(m['last_source'] as String?),
      );
}
