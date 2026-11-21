import 'dart:math';

import '../../data/models.dart';
import '../ladder/ladder_models.dart';
import '../ladder/vocab_questions.dart';

/// One question for a rally, with the little extra the match needs.
class RallyQuestion {
  const RallyQuestion({
    required this.question,
    required this.phrase,
    required this.cardId,
  });

  final LadderQuestion question;

  /// A whole sentence rather than a single word: more time on the clock.
  final bool phrase;

  /// The deck card it came from, for the "words to review" list.
  final String cardId;
}

/// Which part of the deck a match draws from.
class RallyPool {
  const RallyPool({this.maxRank = 100000, this.cardIds});

  /// Only cards up to this teaching rank.
  final int maxRank;

  /// When set, only these cards ("words I've studied").
  final Set<String>? cardIds;

  /// Fewer than this many usable cards and the questions repeat too soon.
  static const minimumCards = 12;
}

/// One choice of "Words" in the Rally lobby: the top-N commonest words, or the
/// whole deck.
class RallyRange {
  const RallyRange(this.key, this.label, this.maxRank);

  /// Stored in the rally statistics as the last choice.
  final String key;
  final String label;

  /// Only cards up to this rank are used.
  final int maxRank;
}

/// The word ranges worth offering for a deck of [deckSize] cards: Top 500,
/// 1,500, 3,000 and 6,000, each only when the deck is bigger than the previous
/// one, and a last "Everything" that stands in for the first range to reach the
/// deck's end (so a 5,000-word deck offers 500, 1,500, 3,000 and Everything,
/// never a "Top 6,000" that is the same set).
List<RallyRange> rallyRangesFor(int deckSize) {
  const caps = <(String, String, int)>[
    ('r500', 'Top 500', 500),
    ('r1500', 'Top 1,500', 1500),
    ('r3000', 'Top 3,000', 3000),
    ('r6000', 'Top 6,000', 6000),
  ];
  final out = <RallyRange>[];
  var previous = 0;
  for (final c in caps) {
    if (deckSize <= previous) break;
    if (deckSize <= c.$3) {
      out.add(const RallyRange('all', 'Everything', 100000));
      return out;
    }
    out.add(RallyRange(c.$1, c.$2, c.$3));
    previous = c.$3;
  }
  out.add(const RallyRange('all', 'Everything', 100000));
  return out;
}

/// Which range the lobby should have selected: the one remembered from last
/// time if this deck still offers it ("studied" only when [studiedOk], that is
/// enough words have been studied), otherwise Top 1,500, otherwise the widest.
/// A stale or unknown key never crashes: it just falls back.
String rallyRangeKey(
  String? remembered,
  List<RallyRange> ranges, {
  required bool studiedOk,
}) {
  if (remembered == 'studied' && studiedOk) return 'studied';
  for (final r in ranges) {
    if (r.key == remembered) return r.key;
  }
  for (final r in ranges) {
    if (r.key == 'r1500') return r.key;
  }
  return ranges.last.key;
}

/// Endless supply of word and phrase questions for one deck.
///
/// Words reuse the Lingo Ladder question writer (so distractors are the same
/// quality there). Phrases are new: a real sentence from the deck is shown and
/// the player picks its English translation from three other sentences' translations
/// of similar length and different wording.
class RallyQuestionSource {
  RallyQuestionSource(this.deck, this.pool, [Random? rnd])
      : _rnd = rnd ?? Random() {
    _words = VocabQuestionFactory(deck, _rnd);
    final ids = pool.cardIds;
    final lemmas = <String>{};
    for (final c in deck.cards) {
      if (c.rank > pool.maxRank) continue;
      if (ids != null && !ids.contains(c.id)) continue;
      _poolCards.add(c);
      lemmas.add(c.lemma);
      for (final s in c.sentences) {
        if (_phraseOk(s)) _phrases.add((c, s));
      }
    }
    _only = ids == null ? null : lemmas;
    // For phrase distractors any sentence in the deck will do, so a small
    // "studied" pool still has plenty of wrong answers to draw on.
    for (final c in deck.cards) {
      for (final s in c.sentences) {
        if (_phraseOk(s)) _anyPhrase.add(s);
      }
    }
  }

  final Deck deck;
  final RallyPool pool;
  final Random _rnd;

  late final VocabQuestionFactory _words;
  final List<VocabCard> _poolCards = [];
  final List<(VocabCard, ExampleSentence)> _phrases = [];
  final List<ExampleSentence> _anyPhrase = [];
  Set<String>? _only;

  /// Cards already asked this match.
  final Set<String> _used = {};
  final Set<String> _usedPhrases = {};

  int get cardCount => _poolCards.length;

  bool get _logographic => const {'zh', 'ja', 'ko'}.contains(deck.language);

  bool _phraseOk(ExampleSentence s) {
    final n = s.text.runes.length;
    final lo = _logographic ? 4 : 12;
    final hi = _logographic ? 32 : 70;
    if (n < lo || n > hi) return false;
    final t = s.translation.length;
    return t >= 10 && t <= 80;
  }

  /// The next question: roughly a third each of "say it in the language",
  /// "what does this mean" and a phrase. Falls back to whatever works, and
  /// starts the deck over rather than ever running dry.
  RallyQuestion next() {
    for (var pass = 0; pass < 2; pass++) {
      final order = _kindOrder();
      for (final kind in order) {
        final q = _make(kind);
        if (q != null) return q;
      }
      // Everything in the pool has been asked: start over.
      _used.clear();
      _usedPhrases.clear();
    }
    throw StateError('No questions could be written for ${deck.id}.');
  }

  List<int> _kindOrder() {
    final first = _rnd.nextDouble();
    final k = first < 0.35 ? 0 : (first < 0.70 ? 1 : 2);
    return [k, ...[0, 1, 2].where((e) => e != k)];
  }

  RallyQuestion? _make(int kind) {
    switch (kind) {
      case 0:
        final q = _words.vocabToTarget(
          minRank: 1,
          maxRank: pool.maxRank,
          difficulty: _difficulty,
          usedCards: _used,
          only: _only,
        );
        return _word(q, 'v2t_');
      case 1:
        final q = _words.vocabToEnglish(
          minRank: 1,
          maxRank: pool.maxRank,
          difficulty: _difficulty,
          usedCards: _used,
          only: _only,
        );
        return _word(q, 't2e_');
      default:
        return _phrase();
    }
  }

  /// Distractor similarity. Rally has no ladder of rising difficulty, so use a
  /// middling value: wrong answers are neither trivially different nor twins.
  double get _difficulty => 0.5;

  RallyQuestion? _word(LadderQuestion? q, String prefix) {
    if (q == null) return null;
    final cardId = q.id.substring(prefix.length);
    _used.add(cardId);
    return RallyQuestion(question: q, phrase: false, cardId: cardId);
  }

  static final _wordRe = RegExp(r"[a-z']+");

  static Set<String> _bag(String s) => {
        for (final m in _wordRe.allMatches(s.toLowerCase()))
          if (m[0]!.length > 2) m[0]!,
      };

  static double _overlap(Set<String> a, Set<String> b) {
    if (a.isEmpty || b.isEmpty) return 0;
    final inter = a.where(b.contains).length;
    return inter / min(a.length, b.length);
  }

  RallyQuestion? _phrase() {
    if (_phrases.isEmpty || _anyPhrase.length < 4) return null;
    for (var attempt = 0; attempt < 60; attempt++) {
      final (card, s) = _phrases[_rnd.nextInt(_phrases.length)];
      if (_usedPhrases.contains(s.id)) continue;
      final right = s.translation.trim();
      final rightBag = _bag(right);

      // Candidates of similar length, from anywhere in the deck.
      final scored = <(double, ExampleSentence)>[];
      for (var i = 0; i < 80; i++) {
        final o = _anyPhrase[_rnd.nextInt(_anyPhrase.length)];
        if (o.id == s.id) continue;
        final t = o.translation.trim();
        if (t.toLowerCase() == right.toLowerCase()) continue;
        final lenGap = (t.length - right.length).abs() / max(right.length, 10);
        if (lenGap > 0.5) continue;
        if (_overlap(rightBag, _bag(t)) > 0.4) continue;
        scored.add((lenGap + _rnd.nextDouble() * 0.2, o));
      }
      scored.sort((a, b) => a.$1.compareTo(b.$1));

      final wrong = <ExampleSentence>[];
      for (final (_, o) in scored) {
        final bag = _bag(o.translation);
        if (wrong.any((w) =>
            w.translation.trim().toLowerCase() ==
                o.translation.trim().toLowerCase() ||
            _overlap(_bag(w.translation), bag) > 0.5)) {
          continue;
        }
        wrong.add(o);
        if (wrong.length == 3) break;
      }
      if (wrong.length < 3) continue;

      _usedPhrases.add(s.id);
      _used.add(card.id);
      final options = <AnswerOption>[
        AnswerOption(text: right, correct: true),
        for (final w in wrong) AnswerOption(text: w.translation.trim(), correct: false),
      ]..shuffle(_rnd);
      return RallyQuestion(
        phrase: true,
        cardId: card.id,
        question: LadderQuestion(
          id: 's2e_${s.id}',
          kind: QuestionKind.vocabToEnglish,
          prompt: s.text,
          promptIsTarget: true,
          speakPrompt: s.text,
          category: 'language',
          options: options,
          explanation: s.text,
          explanationEn: right,
        ),
      );
    }
    return null;
  }
}
