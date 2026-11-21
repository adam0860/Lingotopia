import 'dart:math';

import '../../data/models.dart';
import '../ladder/ladder_models.dart';
import '../ladder/vocab_questions.dart';

/// The numbers that define a round of Quick Recall, in one place.
///
/// Pure Dart (no Flutter imports) so the whole game can be unit tested.
class RecallRules {
  const RecallRules._();

  /// A round starts with this many seconds on the clock.
  static const double roundSeconds = 60;

  /// The clock can never be topped up beyond this.
  static const double maxSeconds = 75;

  /// A wrong answer costs this many seconds.
  static const double wrongPenalty = 3;

  /// Every this-many right answers in a row...
  static const int streakBonusEvery = 5;

  /// ...adds this many seconds.
  static const double streakBonus = 3;

  /// A wrong answer sends the depth back by this many steps.
  static const int dropOnMiss = 2;

  /// Depth 0 asks about words around this rank; each step is [growth] deeper.
  static const double baseRank = 40;
  static const double growth = 1.16;

  /// A question's card lies within [windowLow] to [windowHigh] times the
  /// centre rank.
  static const double windowLow = 0.6;
  static const double windowHigh = 1.4;

  /// Share of questions that show the target-language word and ask for the
  /// English meaning (the rest ask for the target-language word).
  static const double toEnglishShare = 0.6;

  /// "Words I've studied" needs at least this many studied cards.
  static const int minimumStudied = 40;

  /// The rank the questions are centred on at [depth]: 40 * 1.16^depth.
  static double centerRank(int depth) => baseRank * pow(growth, depth);

  /// [reach] rounded to the nearest 50, but never below 100 once anything was
  /// recalled (the screens show 100 as "Top 100"). 0 when nothing was.
  static int reachRounded(int reach) {
    if (reach <= 0) return 0;
    final r = ((reach + 25) ~/ 50) * 50;
    return r < 100 ? 100 : r;
  }
}

/// Which part of the deck a round draws from.
class RecallPool {
  const RecallPool({this.maxRank = 100000, this.cardIds});

  /// Only cards up to this teaching rank.
  final int maxRank;

  /// When set, only these cards ("words I've studied"). The depth then climbs
  /// through them by their position in rank order, not by absolute rank.
  final Set<String>? cardIds;

  bool get studiedOnly => cardIds != null;
}

/// One question of a round, with the card it came from.
class RecallQuestion {
  const RecallQuestion({
    required this.question,
    required this.card,
    required this.gloss,
    this.promptReading,
    this.optionReadings = const [],
  });

  final LadderQuestion question;

  /// The deck card the question is about (the right answer).
  final VocabCard card;

  /// The card's short English meaning.
  final String gloss;

  /// Pronunciation line under a target-language prompt (kana, pinyin, romanised
  /// Korean), when the deck has one.
  final String? promptReading;

  /// The same for each target-language option, in display order. Empty when
  /// the options are English.
  final List<String?> optionReadings;

  /// The frequency rank of the card: the difficulty of the question.
  int get rank => card.rank;

  /// True when the prompt is the target-language word (answers are English).
  bool get targetPrompt => question.promptIsTarget;

  /// What to print big: the word itself, or its English meaning.
  String get promptText => question.promptIsTarget ? card.displayLemma : gloss;
}

/// A stretch of the pool, as indexes into its rank-ordered card list.
class _Span {
  const _Span(this.lo, this.hi);

  final int lo;
  final int hi;
}

/// Writes the questions of a round: asks for one at a given depth and gets a
/// card from the matching band of the pool.
///
/// Questions come from the Lingo Ladder question writer, so the wrong options
/// are the same quality as in the other games. A card is not asked twice in a
/// round until the whole pool has been used. [next] returns null (it never
/// throws) when no question can be written at all.
class RecallQuestionSource {
  RecallQuestionSource(this.deck, this.pool, [Random? rnd])
      : _rnd = rnd ?? Random() {
    _factory = VocabQuestionFactory(deck, _rnd);
    final ids = pool.cardIds;
    final lemmas = <String>{};
    for (final c in deck.cards) {
      final hint = c.pronunciationHint;
      if (hint != null && hint.isNotEmpty) {
        _readingByText.putIfAbsent(c.displayLemma, () => hint);
      }
      if (c.rank > pool.maxRank) continue;
      if (ids != null && !ids.contains(c.id)) continue;
      if (VocabQuestionFactory.usableGloss(c) == null) continue;
      _cards.add(c);
      lemmas.add(c.lemma);
    }
    _cards.sort((a, b) => a.rank.compareTo(b.rank));
    for (final c in _cards) {
      _byId[c.id] = c;
    }
    _only = ids == null ? null : lemmas;
  }

  final Deck deck;
  final RecallPool pool;
  final Random _rnd;

  late final VocabQuestionFactory _factory;

  /// The usable cards of the pool, easiest (lowest rank) first.
  final List<VocabCard> _cards = [];
  final Map<String, VocabCard> _byId = {};

  /// Restricts the question writer to these lemmas for a studied-words pool.
  Set<String>? _only;

  /// Pronunciation lines by displayed word, for the options of a question.
  final Map<String, String> _readingByText = {};

  /// Cards already asked this round.
  final Set<String> _used = {};

  /// Fewer unused cards than this in the window and it is widened, so the
  /// early questions do not come from a handful of cards.
  static const int _minCandidates = 3;

  /// How many cards the pool holds.
  int get poolSize => _cards.length;

  /// The highest rank in the pool (0 when it is empty).
  int get maxRank => _cards.isEmpty ? 0 : _cards.last.rank;

  /// The deck card a question id such as `v2t_ru_12` or `t2e_ru_12` is about.
  static String cardIdOf(String questionId) {
    for (final p in const ['v2t_', 't2e_']) {
      if (questionId.startsWith(p)) return questionId.substring(p.length);
    }
    return questionId;
  }

  /// The position that the window is measured in: the card's rank, or for a
  /// studied-words pool its 1-based place in the rank-ordered pool.
  int _key(int index) => pool.studiedOnly ? index + 1 : _cards[index].rank;

  /// Index of the first card whose key is at least [v] (the length if none).
  int _firstAtLeast(double v) {
    var lo = 0;
    var hi = _cards.length;
    while (lo < hi) {
      final mid = (lo + hi) >> 1;
      if (_key(mid) >= v) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }
    return lo;
  }

  /// Index of the last card whose key is at most [v] (-1 if none).
  int _lastAtMost(double v) {
    var lo = 0;
    var hi = _cards.length;
    while (lo < hi) {
      final mid = (lo + hi) >> 1;
      if (_key(mid) <= v) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }
    return lo - 1;
  }

  /// The cards whose key lies in [0.6, 1.4] times the centre at [depth]. The
  /// centre is capped at the pool's last key, so the window never runs off the
  /// end. Never empty: with no card inside, the nearest one is taken.
  _Span _window(int depth) {
    final last = _cards.length - 1;
    final center = min(RecallRules.centerRank(depth), _key(last).toDouble());
    var lo = _firstAtLeast(center * RecallRules.windowLow);
    var hi = _lastAtMost(center * RecallRules.windowHigh);
    if (hi < lo) {
      lo = min(lo, last);
      hi = lo;
    }
    lo = max(0, min(lo, last));
    hi = max(0, min(hi, last));
    return _Span(lo, hi);
  }

  bool _whole(_Span s) => s.lo == 0 && s.hi == _cards.length - 1;

  /// A wider band around [s]: half again on each side, at least two cards.
  _Span _widen(_Span s) {
    final grow = max(2, (s.hi - s.lo + 1) ~/ 2);
    return _Span(max(0, s.lo - grow), min(_cards.length - 1, s.hi + grow));
  }

  /// How many cards in [lo]..[hi] have not been asked yet, counting only up
  /// to [limit].
  int _unusedIn(int lo, int hi, int limit) {
    var n = 0;
    for (var i = max(0, lo); i <= hi && i < _cards.length; i++) {
      if (!_used.contains(_cards[i].id)) {
        n++;
        if (n >= limit) return n;
      }
    }
    return n;
  }

  /// The next question for a player at [depth], or null when the pool cannot
  /// produce one (empty pool, or a deck too small to write four options).
  RecallQuestion? next(int depth) {
    if (_cards.isEmpty) return null;
    // Everything has been asked: start over rather than ever running dry.
    if (_unusedIn(0, _cards.length - 1, 1) == 0) _used.clear();

    final d = max(0, depth);
    final difficulty = min(1.0, d / 30.0);
    final englishFirst = _rnd.nextDouble() < RecallRules.toEnglishShare;

    var span = _window(d);
    while (true) {
      final whole = _whole(span);
      if (whole || _unusedIn(span.lo, span.hi, _minCandidates) >= _minCandidates) {
        final rq = _write(span, englishFirst, difficulty);
        if (rq != null) return rq;
      }
      if (whole) {
        if (_used.isEmpty) return null;
        _used.clear();
        return _write(span, englishFirst, difficulty);
      }
      span = _widen(span);
    }
  }

  RecallQuestion? _write(_Span span, bool englishFirst, double difficulty) {
    final loRank = _cards[span.lo].rank;
    final hiRank = _cards[span.hi].rank;

    LadderQuestion? make(bool toEnglish) => toEnglish
        ? _factory.vocabToEnglish(
            minRank: loRank,
            maxRank: hiRank,
            difficulty: difficulty,
            usedCards: _used,
            only: _only,
          )
        : _factory.vocabToTarget(
            minRank: loRank,
            maxRank: hiRank,
            difficulty: difficulty,
            usedCards: _used,
            only: _only,
          );

    // A few tries: the writer matches studied words by lemma, so now and then
    // it offers a namesake that is not in the pool. That card is marked used
    // and the next try goes elsewhere.
    for (var attempt = 0; attempt < 5; attempt++) {
      var q = make(englishFirst);
      q ??= make(!englishFirst);
      if (q == null) return null;
      final rq = _wrap(q);
      if (rq != null) return rq;
    }
    return null;
  }

  RecallQuestion? _wrap(LadderQuestion q) {
    final cardId = cardIdOf(q.id);
    _used.add(cardId);
    final card = _byId[cardId];
    if (card == null) return null;

    final gloss = VocabQuestionFactory.usableGloss(card) ?? card.gloss;
    String? promptReading;
    if (q.promptIsTarget) promptReading = card.pronunciationHint;
    List<String?> optionReadings = const [];
    if (q.optionsAreTarget && _readingByText.isNotEmpty) {
      optionReadings = [
        for (final o in q.options)
          o.correct ? card.pronunciationHint : _readingByText[o.text],
      ];
    }
    return RecallQuestion(
      question: q,
      card: card,
      gloss: gloss,
      promptReading: promptReading,
      optionReadings: optionReadings,
    );
  }
}

/// What one answer did, for the screen's feedback.
class RecallAnswer {
  const RecallAnswer({
    required this.question,
    required this.picked,
    required this.correct,
    required this.penaltySeconds,
    required this.bonusSeconds,
    required this.streak,
  });

  /// The question that was answered (the round has already moved on).
  final RecallQuestion question;

  /// Index of the option that was chosen.
  final int picked;

  final bool correct;

  /// Seconds taken off the clock (3 for a wrong answer).
  final double penaltySeconds;

  /// Seconds added by a streak bonus, after the 75 s cap.
  final double bonusSeconds;

  /// The right-in-a-row count after this answer.
  final int streak;
}

/// The numbers a finished round hands to the result page.
class RecallSummary {
  const RecallSummary({
    required this.correct,
    required this.answered,
    required this.reach,
    required this.bestStreak,
    required this.missed,
  });

  final int correct;
  final int answered;

  /// The highest card rank answered correctly (0 if none).
  final int reach;

  final int bestStreak;

  /// Questions answered wrongly, in the order they were asked.
  final List<RecallQuestion> missed;
}

/// One 60-second round: the clock, the depth, the streak and the score.
///
/// The clock is not a timer inside this class: the screen measures real elapsed
/// time and passes it to [advance], so a pause is simply not calling it.
class RecallRound {
  RecallRound(this.source) {
    _draw();
  }

  final RecallQuestionSource source;

  /// Seconds left on the clock.
  double remaining = RecallRules.roundSeconds;

  /// How deep into the deck the questions are: 0 at the start.
  int depth = 0;

  /// Words recalled (right answers).
  int correct = 0;

  /// Questions answered, right or wrong.
  int answered = 0;

  /// Right answers in a row right now.
  int streak = 0;

  int bestStreak = 0;

  /// The highest card rank answered correctly so far (0 if none).
  int reach = 0;

  /// Questions answered wrongly.
  final List<RecallQuestion> missed = [];

  RecallQuestion? _current;
  bool _stuck = false;

  /// The question waiting for an answer. After the round is over it is the
  /// last one asked; null if no question could be written at all.
  RecallQuestion? get current => _current;

  /// True when the clock has run out (or no more questions can be written).
  bool get isOver => remaining <= 0 || _stuck;

  /// Right answers still needed for the next time bonus.
  int get nextBonusIn =>
      RecallRules.streakBonusEvery - (streak % RecallRules.streakBonusEvery);

  RecallSummary get summary => RecallSummary(
        correct: correct,
        answered: answered,
        reach: reach,
        bestStreak: bestStreak,
        missed: List<RecallQuestion>.unmodifiable(missed),
      );

  /// Let [seconds] of real time pass.
  void advance(double seconds) {
    if (isOver || seconds <= 0) return;
    remaining = max(0.0, remaining - seconds);
  }

  /// Answer the current question with option [index]. Returns null when the
  /// round is over or [index] is not an option. A right answer goes one step
  /// deeper (and every fifth in a row adds time); a wrong one goes two steps
  /// back and costs time.
  RecallAnswer? answer(int index) {
    final q = _current;
    if (q == null || isOver) return null;
    final options = q.question.options;
    if (index < 0 || index >= options.length) return null;

    final right = options[index].correct;
    answered++;
    var penalty = 0.0;
    var bonus = 0.0;
    if (right) {
      correct++;
      streak++;
      if (streak > bestStreak) bestStreak = streak;
      if (q.rank > reach) reach = q.rank;
      depth++;
      if (streak % RecallRules.streakBonusEvery == 0) {
        final before = remaining;
        remaining = min(RecallRules.maxSeconds, remaining + RecallRules.streakBonus);
        bonus = remaining - before;
      }
    } else {
      streak = 0;
      depth = max(0, depth - RecallRules.dropOnMiss);
      penalty = RecallRules.wrongPenalty;
      remaining = max(0.0, remaining - penalty);
      missed.add(q);
    }
    if (!isOver) _draw();
    return RecallAnswer(
      question: q,
      picked: index,
      correct: right,
      penaltySeconds: penalty,
      bonusSeconds: bonus,
      streak: streak,
    );
  }

  void _draw() {
    final q = source.next(depth);
    if (q == null) {
      _stuck = true;
      return;
    }
    _current = q;
  }
}
