import 'dart:math';

import '../../data/models.dart';
import 'ladder_models.dart';
import 'ladder_pack.dart';
import 'ladder_rules.dart';
import 'question_bank.dart';
import 'vocab_questions.dart';

/// Assembles the fifteen questions of one game from a language pack, a deck and
/// a question bank. The same inputs and the same [Random] seed give the same
/// game, which is what the tests rely on.
///
/// A step lists several ways to fill it (see [SourceSpec]); the builder tries
/// them in a weighted random order. When none works for this deck (a deck
/// without sentences cannot make a sentence-gap question, a tiny deck may have
/// no word of the right rank) it falls back, in order, to the same kind over
/// the whole deck, to the other vocabulary kinds, and finally to any
/// knowledge question, so a game is always built.
class LadderBuilder {
  LadderBuilder({
    required this.deck,
    required this.pack,
    required this.bank,
    Random? rnd,
    this.seen = const {},
  }) : _rnd = rnd ?? Random();

  final Deck deck;
  final LadderPack pack;
  final QuestionBank bank;

  /// Bank question ids the player has met before. Unseen questions are
  /// preferred, so repeated games keep feeling fresh.
  final Set<String> seen;

  final Random _rnd;

  late final VocabQuestionFactory _vocab = VocabQuestionFactory(deck, _rnd);

  /// Wider than any deck: the "whole deck" window of the fallbacks.
  static const int _anyRank = 100000;

  /// A relative window is never narrower than this many ranks.
  static const int _minWidth = 20;

  /// A deck with fewer picture-book words than this plays its first rungs from
  /// its commonest words instead.
  static const int _minStarters = 8;

  final Set<String> _usedIds = {};
  final Set<String> _usedCards = {};
  final Set<String> _usedCategories = {};

  Set<String>? _starterCache;

  /// The picture-book lemmas of this deck: the pack's own list, or the cards
  /// whose short English meaning is one of the pack's starter glosses.
  Set<String> get _starters => _starterCache ??= _resolveStarters();

  Set<String> _resolveStarters() {
    if (pack.starterLemmas.isNotEmpty) return pack.starterLemmas;
    if (pack.starterGlosses.isEmpty) return const <String>{};
    return _vocab.lemmasForGlosses(pack.starterGlosses, maxRank: _starterCap);
  }

  /// Picture-book words are searched for among a deck's commonest 30% (never
  /// fewer than its [_lowRank]): "dog" is also the meaning of rare words deep
  /// in a big deck, which would be a strange way to open the game.
  int get _starterCap => max(_lowRank, (_vocab.maxUsableRank * 0.3).round());

  /// The rank below which a deck's commonest words lie: the stand-in for the
  /// picture-book words when a deck has too few of them.
  int get _lowRank {
    final top = _vocab.maxUsableRank;
    return max(40, (top * 0.06).round());
  }

  List<LadderQuestion> build() {
    if (pack.blueprint.length != LadderRules.length) {
      throw StateError('Blueprint must have ${LadderRules.length} steps.');
    }
    _usedIds.clear();
    _usedCards.clear();
    _usedCategories.clear();

    final out = <LadderQuestion>[];
    for (var step = 0; step < LadderRules.length; step++) {
      final q = _buildStep(step);
      if (q == null) {
        throw StateError('Could not build question ${step + 1}.');
      }
      _usedIds.add(q.id);
      if (q.kind == QuestionKind.knowledge && q.category != null) {
        _usedCategories.add(q.category!);
      }
      out.add(q);
    }
    return out;
  }

  /// Specs of a step in a random order, heavier weights tending to come first.
  List<SourceSpec> _order(List<SourceSpec> specs) {
    final pool = List.of(specs);
    final out = <SourceSpec>[];
    while (pool.isNotEmpty) {
      final total = pool.fold<int>(0, (a, s) => a + s.weight);
      var roll = _rnd.nextInt(total);
      for (var i = 0; i < pool.length; i++) {
        roll -= pool[i].weight;
        if (roll < 0) {
          out.add(pool.removeAt(i));
          break;
        }
      }
    }
    return out;
  }

  LadderQuestion? _buildStep(int step) {
    final difficulty = step / (LadderRules.length - 1);
    final specs = _order(pack.blueprint[step]);

    // 1. What the plan asks for.
    for (final spec in specs) {
      final q = _try(spec, difficulty);
      if (q != null) return q;
    }

    // Fallbacks, so a thin bank or an odd deck never blocks a game.

    // 2. A sentence-gap that cannot be written (no sentences, or none where
    //    the word stands alone) becomes an ordinary vocabulary question over
    //    the same words.
    for (final spec in specs) {
      if (spec.kind != QuestionKind.sentenceGap) continue;
      for (final kind in const [
        QuestionKind.vocabToTarget,
        QuestionKind.vocabToEnglish,
      ]) {
        final w = _window(spec);
        final q = _vocabQuestion(kind, w.$1, w.$2, null, difficulty);
        if (q != null) return q;
      }
    }

    // 3. Widen the window to the whole deck (for a picture-book rung, to the
    //    deck's commonest words), or borrow from the neighbouring bank tiers.
    final starterStep = specs.any((s) => s.starter);
    final wideHi = starterStep ? _lowRank : _anyRank;
    for (final spec in specs) {
      if (spec.kind == QuestionKind.knowledge) {
        for (final tier in [spec.tier - 1, spec.tier + 1, spec.tier - 2, spec.tier + 2]) {
          if (tier < 1 || tier > 5) continue;
          final q = _knowledge(tier);
          if (q != null) return q;
        }
      } else {
        final q = _vocabQuestion(spec.kind, 1, wideHi, null, difficulty);
        if (q != null) return q;
      }
    }

    // 4. Any vocabulary question at all, then any knowledge question.
    for (final kind in const [
      QuestionKind.vocabToTarget,
      QuestionKind.vocabToEnglish,
    ]) {
      final q = _vocabQuestion(kind, 1, wideHi, null, difficulty);
      if (q != null) return q;
    }
    return _anyKnowledge(difficulty);
  }

  /// The absolute rank window of a vocabulary spec for this deck.
  (int, int) _window(SourceSpec spec) {
    if (!pack.relativeRanks) return (spec.minRank, spec.maxRank);
    final top = _vocab.maxUsableRank;
    if (top <= 0) return (1, _anyRank);
    var lo = spec.minRank <= 1 ? 1 : (top * spec.minRank / 1000).round();
    var hi = (top * spec.maxRank / 1000).round();
    if (lo < 1) lo = 1;
    if (hi < lo + _minWidth) hi = lo + _minWidth;
    return (lo, hi);
  }

  LadderQuestion? _try(SourceSpec spec, double difficulty) {
    if (spec.kind == QuestionKind.knowledge) return _knowledge(spec.tier);

    final w = _window(spec);
    final lo = w.$1;
    var hi = w.$2;
    Set<String>? only;
    if (spec.starter) {
      final starters = _starters;
      if (starters.length >= _minStarters) {
        only = starters;
      } else {
        // Too few picture-book words in this deck: use its commonest words.
        hi = min(hi, _lowRank);
      }
    }
    return _vocabQuestion(spec.kind, lo, hi, only, difficulty);
  }

  /// One vocabulary question of [kind] from cards ranked [lo] to [hi],
  /// remembering the card so it is not asked twice. [only] restricts the cards
  /// to those lemmas (it is ignored by sentence-gap questions).
  LadderQuestion? _vocabQuestion(
    QuestionKind kind,
    int lo,
    int hi,
    Set<String>? only,
    double difficulty,
  ) {
    switch (kind) {
      case QuestionKind.vocabToTarget:
        return _remember(_vocab.vocabToTarget(
          minRank: lo,
          maxRank: hi,
          difficulty: difficulty,
          usedCards: _usedCards,
          only: only,
        ));
      case QuestionKind.vocabToEnglish:
        return _remember(_vocab.vocabToEnglish(
          minRank: lo,
          maxRank: hi,
          difficulty: difficulty,
          usedCards: _usedCards,
          only: only,
        ));
      case QuestionKind.sentenceGap:
        return _remember(_vocab.sentenceGap(
          minRank: lo,
          maxRank: hi,
          difficulty: difficulty,
          usedCards: _usedCards,
        ));
      case QuestionKind.knowledge:
        return null;
    }
  }

  /// Note which card a generated question used, so it is not asked twice.
  LadderQuestion? _remember(LadderQuestion? q) {
    if (q == null) return null;
    final underscore = q.id.indexOf('_');
    _usedCards.add(q.id.substring(underscore + 1));
    return q;
  }

  LadderQuestion? _knowledge(int tier) {
    var candidates =
        bank.tier(tier).where((b) => !_usedIds.contains(b.id)).toList();
    if (candidates.isEmpty) return null;

    // Prefer questions not seen in earlier games, then new subjects.
    final fresh = candidates.where((b) => !seen.contains(b.id)).toList();
    if (fresh.isNotEmpty) candidates = fresh;
    final varied =
        candidates.where((b) => !_usedCategories.contains(b.category)).toList();
    if (varied.isNotEmpty) candidates = varied;

    final pick = candidates[_rnd.nextInt(candidates.length)];
    return pick.toQuestion(_rnd);
  }

  /// The last resort: a knowledge question from whichever tier still has one,
  /// the tier nearest this step's difficulty first.
  LadderQuestion? _anyKnowledge(double difficulty) {
    final target = 1 + (difficulty * 4).round();
    final tiers = [1, 2, 3, 4, 5]
      ..sort((a, b) => (a - target).abs().compareTo((b - target).abs()));
    for (final tier in tiers) {
      final q = _knowledge(tier);
      if (q != null) return q;
    }
    return null;
  }
}
