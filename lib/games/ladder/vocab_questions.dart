import 'dart:math';

import '../../data/models.dart';
import 'ladder_models.dart';

/// One deck card prepared for question writing.
class _Entry {
  _Entry(this.card, this.gloss, this.words, this.allWords);

  final VocabCard card;

  /// A short, clean English meaning ("dog", "to eat, to have a meal").
  final String gloss;

  /// Content words of [gloss].
  final Set<String> words;

  /// Content words of the card's whole gloss, every sense included.
  final Set<String> allWords;
}

/// Writes vocabulary questions from any deck.
///
/// Three kinds: English -> target word, target word -> English, and a real
/// example sentence with one word blanked (translation shown, so there is
/// exactly one right answer). The deck's frequency rank is the difficulty: a
/// question about rank 40 is easy, one about rank 4,500 is hard.
class VocabQuestionFactory {
  VocabQuestionFactory(this.deck, this._rnd) {
    for (final card in deck.cards) {
      final e = _prepare(card);
      if (e != null) _entries.add(e);
    }
    for (final e in _entries) {
      if (e.card.rank > _maxUsableRank) _maxUsableRank = e.card.rank;
    }
  }

  final Deck deck;
  final Random _rnd;
  final List<_Entry> _entries = [];
  int _maxUsableRank = 0;

  int get usableCards => _entries.length;

  /// The rank of the rarest card that can be asked about (0 when none can).
  /// Language packs whose difficulty plan is relative to the deck's size scale
  /// their rank windows by this.
  int get maxUsableRank => _maxUsableRank;

  /// Lemmas of the usable cards whose short English meaning is one of
  /// [glosses] (all lower case, e.g. "dog", "to drink"). The first of a
  /// two-part meaning counts, so "house, home" matches "house". This is how a
  /// pack finds its picture-book words in any deck without listing them in the
  /// deck's own language. Only cards ranked [maxRank] or better count: a
  /// picture-book meaning such as "dog" is also the meaning of rare words far
  /// down a 10,000-word deck, and those make a poor first question.
  Set<String> lemmasForGlosses(Set<String> glosses, {int maxRank = 1 << 30}) {
    final out = <String>{};
    for (final e in _entries) {
      if (e.card.rank > maxRank) continue;
      final first = e.gloss.split(',').first.trim().toLowerCase();
      if (glosses.contains(first)) out.add(e.card.lemma);
    }
    return out;
  }

  // --- Preparing cards -------------------------------------------------------

  static const _okPos = {'n', 'v', 'adj', 'adv'};

  static const _stop = {
    'to', 'a', 'an', 'the', 'of', 'be', 'in', 'on', 'or', 'and', 'one', 's',
  };

  /// "plural past of быть", "genitive singular of ..." - a form, not a word.
  static final _formOf = RegExp(
    r'\b(form|plural|singular|genitive|dative|accusative|instrumental|'
    r'prepositional|nominative|vocative|locative|past|present|future|'
    r'imperative|participle|gerund|comparative|superlative|diminutive|'
    r'abbreviation|initialism|acronym|alternative|misspelling)\b[^;]*\bof\b',
    caseSensitive: false,
  );

  static final _cleanGloss = RegExp(r"^[A-Za-z][A-Za-z' ,\-/]*$");

  /// Latin or Cyrillic words with no vowel at all are abbreviations (км, кг),
  /// which make poor answers and worse wrong answers.
  static final _latinCyrillic = RegExp('^[a-zA-Zа-яА-ЯёЁ]+\$');
  static final _vowel = RegExp('[aeiouyAEIOUYаеёиоуыэюяАЕЁИОУЫЭЮЯ]');

  static Set<String> contentWords(String s) => {
        for (final m in RegExp(r"[a-z']+").allMatches(s.toLowerCase()))
          if (m[0]!.length > 1 && !_stop.contains(m[0]!)) m[0]!,
      };

  /// First sense of a Wiktionary-style gloss, parentheticals removed, at most
  /// two comma-separated meanings. Null when nothing clean is left.
  static String? shortGloss(String raw) {
    if (_formOf.hasMatch(raw)) return null;
    var g = raw.split(';').first.trim();
    g = g.replaceAll(RegExp(r'\s*\([^)]*\)'), '').trim();
    final parts = g
        .split(',')
        .map((e) => e.trim())
        .where((e) => e.isNotEmpty)
        .toList();
    if (parts.isEmpty) return null;
    g = parts.take(2).join(', ');
    if (g.length > 30) g = parts.first;
    if (g.length < 2 || g.length > 30) return null;
    if (!_cleanGloss.hasMatch(g)) return null;
    return g;
  }

  /// The short English meaning to use for [card] in any game, or null when
  /// the card makes a poor question (a name, an abbreviation, a mere form of
  /// another word, a long or messy gloss). Shared by Ladder, Rally, Word Match
  /// and Quick Recall so they all agree on which cards are fair game.
  static String? usableGloss(VocabCard card) {
    if (!_okPos.contains(card.pos)) return null;
    final lemma = card.lemma;
    if (lemma.isEmpty || lemma.contains(' ')) return null;
    // Capitalised lemmas are names and place names.
    if (lemma[0] != lemma[0].toLowerCase()) return null;
    if (_latinCyrillic.hasMatch(lemma) && !_vowel.hasMatch(lemma)) return null;
    return shortGloss(card.gloss);
  }

  _Entry? _prepare(VocabCard card) {
    final gloss = usableGloss(card);
    if (gloss == null) return null;
    final words = contentWords(gloss);
    return _Entry(card, gloss, words, contentWords(card.gloss));
  }

  /// The pronunciation line for languages whose script hides it (pinyin for
  /// Chinese, kana for Japanese kanji, romanised Korean). Null for the rest.
  static String? _reading(VocabCard card) {
    final r = card.reading;
    return (r == null || r.isEmpty) ? null : r;
  }

  /// What the reveal shows under an answer: the English meaning, led by the
  /// reading when the card has one.
  static String _meaning(_Entry e) {
    final r = _reading(e.card);
    return r == null ? e.gloss : '$r · ${e.gloss}';
  }

  /// The card's word in quotes for an explanation, with its reading if any.
  static String _quoted(VocabCard card) {
    final r = _reading(card);
    return r == null ? '“${card.lemma}”' : '“${card.lemma}” ($r)';
  }

  // --- Distractors -----------------------------------------------------------

  /// Two cards that could both be "right": same meaning, or one's short meaning
  /// appears anywhere in the other's full gloss.
  static bool _conflict(_Entry a, _Entry b) {
    if (a.gloss.toLowerCase() == b.gloss.toLowerCase()) return true;
    if (a.words.any(b.allWords.contains)) return true;
    if (b.words.any(a.allWords.contains)) return true;
    return false;
  }

  /// Three wrong options for [answer]. [difficulty] runs 0 (easy) to 1 (hard):
  /// easy questions get common, unlike words; hard ones get words of similar
  /// frequency and length, which look alike.
  List<_Entry> _distractors(
    _Entry answer,
    double difficulty, {
    Set<String> blockedWords = const {},
    Set<String>? pool,
  }) {
    // A starter question draws its wrong answers from the same short list of
    // familiar words, so "dog" is surrounded by "cat", "house" and "water".
    if (pool != null) {
      final r = _pick(answer, difficulty, blockedWords, pool);
      if (r.length == 3) return r;
    }
    return _pick(answer, difficulty, blockedWords, null);
  }

  List<_Entry> _pick(
    _Entry answer,
    double difficulty,
    Set<String> blockedWords,
    Set<String>? pool,
  ) {
    final easyCap = max(350.0, answer.card.rank * 1.8);
    final keyed = <(double, _Entry)>[];
    for (final e in _entries) {
      if (e.card.id == answer.card.id) continue;
      // A homograph of the answer (same spelling, another card) would show two
      // identical buttons, one of them marked wrong.
      if (e.card.lemma.toLowerCase() == answer.card.lemma.toLowerCase()) continue;
      if (e.card.pos != answer.card.pos) continue;
      if (_conflict(answer, e)) continue;
      if (e.words.any(blockedWords.contains)) continue;
      if (pool != null && !pool.contains(e.card.lemma)) continue;
      if (pool == null && difficulty < 0.5 && e.card.rank > easyCap) continue;
      final rankGap =
          (e.card.rank - answer.card.rank).abs() / (answer.card.rank + 200);
      final lenGap =
          (e.card.lemma.length - answer.card.lemma.length).abs() / 8.0;
      final jitter = _rnd.nextDouble() * (1.5 - 1.2 * difficulty);
      keyed.add((rankGap + lenGap + jitter, e));
    }
    keyed.sort((a, b) => a.$1.compareTo(b.$1));

    final chosen = <_Entry>[];
    for (final (_, e) in keyed) {
      if (chosen.any((c) => _conflict(c, e) || c.card.lemma == e.card.lemma)) {
        continue;
      }
      chosen.add(e);
      if (chosen.length == 3) break;
    }
    return chosen;
  }

  Iterable<_Entry> _candidates(
    int minRank,
    int maxRank,
    Set<String> usedCards, {
    Set<String>? only,
  }) {
    final pool = _entries
        .where((e) =>
            e.card.rank >= minRank &&
            e.card.rank <= maxRank &&
            (only == null || only.contains(e.card.lemma)) &&
            !usedCards.contains(e.card.id))
        .toList()
      ..shuffle(_rnd);
    return pool;
  }

  List<AnswerOption> _shuffled(List<AnswerOption> options) =>
      (List.of(options)..shuffle(_rnd));

  // --- Question kinds --------------------------------------------------------

  /// "How do you say 'dog' in Spanish?"
  LadderQuestion? vocabToTarget({
    required int minRank,
    required int maxRank,
    required double difficulty,
    required Set<String> usedCards,
    Set<String>? only,
  }) {
    for (final a in _candidates(minRank, maxRank, usedCards, only: only).take(40)) {
      final wrong = _distractors(a, difficulty, pool: only);
      if (wrong.length < 3) continue;
      final example = a.card.sentences.isEmpty ? null : a.card.sentences.first;
      return LadderQuestion(
        id: 'v2t_${a.card.id}',
        kind: QuestionKind.vocabToTarget,
        prompt: 'How do you say “${a.gloss}” in ${deck.languageName}?',
        category: 'language',
        optionsAreTarget: true,
        options: _shuffled([
          AnswerOption(
            text: a.card.displayLemma,
            speak: a.card.speakableLemma,
            correct: true,
            translation: _meaning(a),
          ),
          for (final w in wrong)
            AnswerOption(
              text: w.card.displayLemma,
              speak: w.card.speakableLemma,
              correct: false,
              translation: _meaning(w),
            ),
        ]),
        explanation: example?.text,
        explanationEn: example == null
            ? '${_quoted(a.card)} means “${a.gloss}”.'
            : '${_quoted(a.card)} means “${a.gloss}”. ${example.translation}',
      );
    }
    return null;
  }

  /// "What does 'perro' mean?"
  LadderQuestion? vocabToEnglish({
    required int minRank,
    required int maxRank,
    required double difficulty,
    required Set<String> usedCards,
    Set<String>? only,
  }) {
    for (final a in _candidates(minRank, maxRank, usedCards, only: only).take(40)) {
      final wrong = _distractors(a, difficulty, pool: only);
      if (wrong.length < 3) continue;
      final example = a.card.sentences.isEmpty ? null : a.card.sentences.first;
      return LadderQuestion(
        id: 't2e_${a.card.id}',
        kind: QuestionKind.vocabToEnglish,
        prompt: 'What does “${a.card.displayLemma}” mean?',
        promptIsTarget: true,
        speakPrompt: a.card.speakableLemma,
        // Pinyin / kana / romanisation, where the script does not show it.
        detail: _reading(a.card),
        category: 'language',
        options: _shuffled([
          AnswerOption(text: a.gloss, correct: true),
          for (final w in wrong) AnswerOption(text: w.gloss, correct: false),
        ]),
        explanation: example?.text,
        explanationEn: example == null
            ? '${_quoted(a.card)} means “${a.gloss}”.'
            : '${_quoted(a.card)} means “${a.gloss}”. ${example.translation}',
      );
    }
    return null;
  }

  static final _letters = RegExp(r'[\p{L}\-]+', unicode: true);

  /// A real sentence from the deck with one word blanked out. The English
  /// translation is shown under it, so the blank has exactly one sensible fill.
  LadderQuestion? sentenceGap({
    required int minRank,
    required int maxRank,
    required double difficulty,
    required Set<String> usedCards,
  }) {
    for (final a in _candidates(minRank, maxRank, usedCards).take(120)) {
      if (a.card.sentences.isEmpty) continue;
      final sentences = List.of(a.card.sentences)..shuffle(_rnd);
      for (final s in sentences) {
        if (s.text.length > 90) continue;
        final lemma = a.card.lemma.toLowerCase();
        final hits = _letters
            .allMatches(s.text)
            .where((m) => m[0]!.toLowerCase() == lemma)
            .toList();
        // Exactly one occurrence, in its dictionary form, so blanking it
        // leaves one clear gap.
        if (hits.length != 1) continue;
        final hit = hits.first;
        final surface = hit[0]!;

        final translationWords = contentWords(s.translation);
        final wrong =
            _distractors(a, difficulty, blockedWords: translationWords);
        if (wrong.length < 3) continue;

        final capital = surface[0] != surface[0].toLowerCase();
        String form(String lemma) =>
            capital ? lemma[0].toUpperCase() + lemma.substring(1) : lemma;

        final blanked = s.text.replaceRange(hit.start, hit.end, '_____');
        return LadderQuestion(
          id: 'gap_${a.card.id}',
          kind: QuestionKind.sentenceGap,
          prompt: blanked,
          promptIsTarget: true,
          detail: s.translation,
          category: 'language',
          optionsAreTarget: true,
          revealSpeak: s.text,
          options: _shuffled([
            AnswerOption(
              text: surface,
              speak: surface,
              correct: true,
              translation: _meaning(a),
            ),
            for (final w in wrong)
              AnswerOption(
                text: form(w.card.lemma),
                speak: w.card.speakableLemma,
                correct: false,
                translation: _meaning(w),
              ),
          ]),
          explanation: s.text,
          explanationEn: '“$surface” means “${a.gloss}”.',
        );
      }
    }
    return null;
  }
}
