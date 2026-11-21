import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';
import 'package:lingotopia/games/ladder/ladder_builder.dart';
import 'package:lingotopia/games/ladder/ladder_game.dart';
import 'package:lingotopia/games/ladder/ladder_models.dart';
import 'package:lingotopia/games/ladder/ladder_pack.dart';
import 'package:lingotopia/games/ladder/ladder_rules.dart';
import 'package:lingotopia/games/ladder/ladder_stats.dart';
import 'package:lingotopia/games/ladder/lifelines.dart';
import 'package:lingotopia/games/ladder/question_bank.dart';
import 'package:lingotopia/games/ladder/vocab_questions.dart';

/// A knowledge question whose right answer is option `i % 4`.
LadderQuestion mkQ(int i, {String? translation, String category = 'history'}) =>
    LadderQuestion(
      id: 'q$i',
      kind: QuestionKind.knowledge,
      prompt: 'Question $i?',
      translation: translation,
      category: category,
      options: [
        for (var k = 0; k < 4; k++)
          AnswerOption(text: 'option $k', correct: k == i % 4),
      ],
    );

List<LadderQuestion> mkLadder({String? translation}) =>
    [for (var i = 0; i < LadderRules.length; i++) mkQ(i, translation: translation)];

int wrongPick(LadderQuestion q) => (q.correctIndex + 1) % 4;

// --- Fake decks ---------------------------------------------------------------

const _syllables = [
  'ba', 'ko', 'di', 'mu', 'se', 'ta', 'no', 'ri', 'pe', 'lu', //
  'ga', 'fi', 'ho', 'ze', 'wa', 've', 'ju', 'ny', 'qa', 'xo',
];

/// A unique pronounceable pseudo-word for [i] (so glosses never share a word
/// and never clash as distractors).
String _pseudo(int i) {
  final b = StringBuffer();
  var n = i;
  for (var k = 0; k < 4; k++) {
    b.write(_syllables[n % _syllables.length]);
    n ~/= _syllables.length;
  }
  return b.toString();
}

const _adjectiveStarters = {
  'red', 'blue', 'green', 'white', 'black', 'big', 'small', 'good', 'bad',
  'new', 'old', 'hot', 'cold', 'fast',
};

/// A deck of [size] cards ranked 1..size. [starters] of them carry the
/// picture-book glosses ("dog", "to drink"...) at low ranks, the rest unique
/// made-up glosses. Sentences contain the lemma as a word of its own, or, with
/// [unspaced], inside a run of CJK text where no word can be blanked out.
Deck fakeDeck({
  String language = 'es',
  int size = 5000,
  bool sentences = true,
  int starters = 87,
  bool unspaced = false,
  bool rtl = false,
  String? reading,
}) {
  final glosses = kStarterGlosses.toList();
  final n = max(0, min(min(starters, glosses.length), (size - 10) ~/ 3));
  final starterAt = <int, String>{
    for (var k = 0; k < n; k++) 10 + 3 * k: glosses[k],
  };
  final cards = <VocabCard>[];
  for (var rank = 1; rank <= size; rank++) {
    final i = rank - 1;
    final starter = starterAt[rank];
    final String pos;
    final String gloss;
    if (starter != null) {
      gloss = starter;
      pos = starter.startsWith('to ')
          ? 'v'
          : (_adjectiveStarters.contains(starter) ? 'adj' : 'n');
    } else {
      pos = const ['n', 'v', 'adj', 'n'][i % 4];
      final w = _pseudo(i + 40000);
      gloss = pos == 'v' ? 'to $w' : w;
    }
    final lemma = 'l${_pseudo(i)}';
    cards.add(VocabCard(
      id: 'c$rank',
      rank: rank,
      lemma: lemma,
      pos: pos,
      posName: pos,
      gloss: gloss,
      reading: reading,
      sentences: !sentences
          ? const []
          : [
              ExampleSentence(
                id: 's$rank',
                text: unspaced
                    ? '我喜欢$lemma。'
                    : '$lemma ${_pseudo(i + 90000)} ${_pseudo(i + 120000)}.',
                translation: 'This is a sentence.',
              ),
            ],
    ));
  }
  return Deck(
    id: '${language}_fake',
    name: 'Fake $language',
    language: language,
    languageName: 'Fakish',
    targetVoice: '',
    rtl: rtl,
    cards: cards,
  );
}

/// The short English meaning a vocabulary question is about, lower case and
/// without any reading in front. Null for the other kinds.
String? correctGloss(LadderQuestion q) {
  String clean(String t) {
    final bare = t.contains(' · ') ? t.split(' · ').last : t;
    return bare.split(',').first.trim().toLowerCase();
  }

  if (q.kind == QuestionKind.vocabToTarget) {
    final t = q.correctOption.translation;
    return t == null ? null : clean(t);
  }
  if (q.kind == QuestionKind.vocabToEnglish) return clean(q.correctOption.text);
  return null;
}

/// The card a generated question was written from (its id after the prefix).
String cardIdOf(LadderQuestion q) => q.id.substring(q.id.indexOf('_') + 1);

/// The frequency rank of the card behind a generated question (the fake decks
/// name card number N "cN").
int rankOf(LadderQuestion q) => int.parse(cardIdOf(q).substring(1));

/// Whether a generated vocabulary question lies in the rank window its step
/// asks for, using the arithmetic the builder uses for a relative pack.
bool inPlan(LadderPack pack, int step, LadderQuestion q, int top) {
  final rank = rankOf(q);
  for (final spec in pack.blueprint[step]) {
    if (spec.kind != q.kind) continue;
    final lo = spec.minRank <= 1 ? 1 : (top * spec.minRank / 1000).round();
    var hi = (top * spec.maxRank / 1000).round();
    if (hi < lo + 20) hi = lo + 20;
    if (rank >= lo && rank <= hi) return true;
  }
  return false;
}

const _allCodes = [
  'es', 'ja', 'ar', 'arz', 'zh', 'ko', 'it', 'tl', 'pl', 'sw', 'tr', 'pt',
];

/// The fourteen question subjects friends can be strong at.
const _subjects = {
  'language', 'literature', 'arts', 'food', 'science', 'technology', 'nature',
  'sports', 'health', 'history', 'politics', 'geography', 'economics', 'society',
};

void expectValidGame(List<LadderQuestion> qs, String where) {
  expect(qs.length, 15, reason: where);
  expect(qs.map((q) => q.id).toSet().length, 15, reason: '$where: duplicate ids');
  for (final q in qs) {
    expect(q.options.length, 4, reason: '$where ${q.id}');
    expect(q.options.where((o) => o.correct).length, 1, reason: '$where ${q.id}');
    expect(q.options.map((o) => o.text.toLowerCase()).toSet().length, 4,
        reason: '$where ${q.id}: duplicate options');
    expect(q.prompt.trim(), isNotEmpty, reason: '$where ${q.id}');
  }
}

void main() {
  group('prize ladder rules', () {
    test('fifteen increasing prizes ending at one million', () {
      expect(LadderRules.length, 15);
      for (var i = 1; i < LadderRules.length; i++) {
        expect(LadderRules.prizes[i], greaterThan(LadderRules.prizes[i - 1]));
      }
      expect(LadderRules.prizes.last, 1000000);
    });

    test('safe havens guarantee the highest passed milestone', () {
      expect(LadderRules.guaranteedBefore(0), 0);
      expect(LadderRules.guaranteedBefore(4), 0);
      // Question 6 (index 5): the question-5 haven has been passed.
      expect(LadderRules.guaranteedBefore(5), LadderRules.prizes[4]);
      expect(LadderRules.guaranteedBefore(9), LadderRules.prizes[4]);
      expect(LadderRules.guaranteedBefore(10), LadderRules.prizes[9]);
      expect(LadderRules.guaranteedBefore(14), LadderRules.prizes[9]);
    });

    test('bankedAfter and format', () {
      expect(LadderRules.bankedAfter(0), 0);
      expect(LadderRules.bankedAfter(1), 100);
      expect(LadderRules.bankedAfter(15), 1000000);
      expect(LadderRules.format(1000000), '1,000,000');
      expect(LadderRules.format(100), '100');
      expect(LadderRules.format(32000), '32,000');
    });
  });

  group('game engine', () {
    test('needs exactly fifteen questions', () {
      expect(() => LadderGame(questions: [mkQ(0)]), throwsArgumentError);
    });

    test('answering everything correctly wins the top prize', () {
      final g = LadderGame(questions: mkLadder(), rnd: Random(1));
      for (var i = 0; i < LadderRules.length; i++) {
        expect(g.index, i);
        final r = g.answer(g.current.correctIndex);
        expect(r.correct, isTrue);
        if (i < LadderRules.length - 1) {
          expect(r.status, GameStatus.playing);
          g.next();
        }
      }
      expect(g.status, GameStatus.won);
      expect(g.prize, 1000000);
      expect(g.outcome.correctCount, 15);
    });

    test('a wrong answer pays the last safe haven', () {
      for (final (failAt, expected) in [
        (0, 0),
        (3, 0),
        (4, 0),
        (5, 1000),
        (9, 1000),
        (10, 32000),
        (14, 32000),
      ]) {
        final g = LadderGame(questions: mkLadder(), rnd: Random(2));
        for (var i = 0; i < failAt; i++) {
          g.answer(g.current.correctIndex);
          g.next();
        }
        final r = g.answer(wrongPick(g.current));
        expect(r.correct, isFalse);
        expect(g.status, GameStatus.lost, reason: 'fail at $failAt');
        expect(g.prize, expected, reason: 'fail at $failAt');
        expect(g.outcome.correctCount, failAt);
      }
    });

    test('walking away keeps what has been banked', () {
      final g = LadderGame(questions: mkLadder(), rnd: Random(3));
      for (var i = 0; i < 6; i++) {
        g.answer(g.current.correctIndex);
        g.next();
      }
      expect(g.banked, LadderRules.prizes[5]);
      g.walkAway();
      expect(g.status, GameStatus.walkedAway);
      expect(g.prize, LadderRules.prizes[5]);
    });

    test('walking away before answering anything pays nothing', () {
      final g = LadderGame(questions: mkLadder());
      g.walkAway();
      expect(g.prize, 0);
    });

    test('state machine refuses out-of-order calls', () {
      final g = LadderGame(questions: mkLadder(), rnd: Random(4));
      expect(g.next, throwsStateError);
      g.answer(g.current.correctIndex);
      expect(() => g.answer(0), throwsStateError);
      expect(g.walkAway, throwsStateError);
      g.next();
      g.answer(wrongPick(g.current));
      expect(g.next, throwsStateError);
      expect(() => g.answer(0), throwsStateError);
    });

    test('banked rises as soon as a right answer is on screen', () {
      final g = LadderGame(questions: mkLadder(), rnd: Random(5));
      expect(g.banked, 0);
      g.answer(g.current.correctIndex);
      expect(g.banked, 100);
      g.next();
      expect(g.banked, 100);
    });
  });

  group('lifelines', () {
    test('each can be used once per game', () {
      final g = LadderGame(questions: mkLadder(translation: 'x'), rnd: Random(6));
      for (final l in Lifeline.values) {
        expect(g.canUse(l), isTrue, reason: l.label);
      }
      g.useFiftyFifty();
      g.useTranslate();
      g.useAudience();
      g.useFriend(LadderPacks.russian.friends.first, LadderPacks.russian.friendLines);
      for (final l in Lifeline.values) {
        expect(g.canUse(l), isFalse, reason: l.label);
      }
      g.answer(g.current.correctIndex);
      g.next();
      // Still spent on the next question.
      expect(g.canUse(Lifeline.fiftyFifty), isFalse);
      expect(g.usedLifelines.length, 4);
    });

    test('lifeline results reset between questions', () {
      final g = LadderGame(questions: mkLadder(translation: 'x'), rnd: Random(7));
      g.useFiftyFifty();
      g.useAudience();
      g.useTranslate();
      expect(g.eliminated.length, 2);
      g.answer(g.current.correctIndex);
      g.next();
      expect(g.eliminated, isEmpty);
      expect(g.poll, isNull);
      expect(g.translateShown, isFalse);
    });

    test('50:50 removes exactly two wrong answers, never the right one', () {
      for (var seed = 0; seed < 100; seed++) {
        final q = mkQ(seed);
        final gone = fiftyFifty(q, {}, Random(seed));
        expect(gone.length, 2);
        expect(gone.contains(q.correctIndex), isFalse);
      }
    });

    test('an eliminated answer cannot be chosen', () {
      final g = LadderGame(questions: mkLadder(), rnd: Random(8));
      final gone = g.useFiftyFifty().first;
      expect(g.isSelectable(gone), isFalse);
      expect(() => g.answer(gone), throwsStateError);
    });

    test('Translate is unavailable when the question has nothing to translate', () {
      final g = LadderGame(questions: mkLadder(), rnd: Random(9)); // no translations
      expect(g.canUse(Lifeline.translate), isFalse);
      expect(g.whyNot(Lifeline.translate), isNotNull);
      expect(g.useTranslate, throwsStateError);
      // And it was not spent.
      expect(g.usedLifelines, isEmpty);
    });

    test('lifelines are locked once the answer is revealed', () {
      final g = LadderGame(questions: mkLadder(translation: 'x'), rnd: Random(10));
      g.answer(g.current.correctIndex);
      for (final l in Lifeline.values) {
        expect(g.canUse(l), isFalse);
      }
    });

    test('audience bars add up to 100 and skip removed answers', () {
      for (var seed = 0; seed < 200; seed++) {
        final q = mkQ(seed);
        final gone = fiftyFifty(q, {}, Random(seed));
        final poll = audiencePoll(
            q: q, level: seed % 15, eliminated: gone, rnd: Random(seed));
        expect(poll.percents.reduce((a, b) => a + b), 100);
        for (final i in gone) {
          expect(poll.percents[i], 0);
        }
      }
    });

    test('with two answers left the poll leader matches the audience verdict', () {
      for (var seed = 0; seed < 300; seed++) {
        final q = mkQ(seed);
        final wrong = (q.correctIndex + 1) % 4;
        final gone = {for (var i = 0; i < 4; i++) if (i != q.correctIndex && i != wrong) i};
        final poll = audiencePoll(q: q, level: 14, eliminated: gone, rnd: Random(seed));
        expect(poll.percents[poll.leader], greaterThan(50));
      }
    });

    test('the audience is almost always right early and often wrong late', () {
      int rightAt(int level) {
        var right = 0;
        for (var seed = 0; seed < 1000; seed++) {
          final q = mkQ(seed);
          final poll = audiencePoll(
              q: q, level: level, eliminated: {}, rnd: Random(seed));
          if (poll.leader == q.correctIndex) right++;
        }
        return right;
      }

      expect(rightAt(0), greaterThan(880));
      expect(rightAt(14), lessThan(620));
      expect(rightAt(14), greaterThan(380));
    });

    test('a friend is better on their subject and on easy questions', () {
      final ivanov = LadderPacks.russian.friends.firstWhere((f) => f.id == 'ivanov');
      final lines = LadderPacks.russian.friendLines;
      int correct(String category, int level) {
        var n = 0;
        for (var seed = 0; seed < 1000; seed++) {
          final q = mkQ(seed, category: category);
          final a = phoneFriend(
              q: q, level: level, friend: ivanov, eliminated: {}, lines: lines, rnd: Random(seed));
          if (a.optionIndex == q.correctIndex) n++;
        }
        return n;
      }

      expect(correct('history', 2), greaterThan(correct('sports', 2)));
      expect(correct('history', 1), greaterThan(correct('history', 13)));
    });

    test('a friend never names a removed answer, and speaks in the pack lines', () {
      final friend = LadderPacks.russian.friends.first;
      final lines = LadderPacks.russian.friendLines;
      for (var seed = 0; seed < 200; seed++) {
        final q = mkQ(seed);
        final gone = fiftyFifty(q, {}, Random(seed));
        final a = phoneFriend(
            q: q, level: seed % 15, friend: friend, eliminated: gone, lines: lines, rnd: Random(seed));
        expect(gone.contains(a.optionIndex), isFalse);
        expect(a.line.target, isNot(contains('{L}')));
        expect(a.line.english, contains(String.fromCharCode(0x41 + a.optionIndex)));
      }
    });
  });

  group('vocabulary glosses', () {
    test('shortGloss keeps the first sense and drops parentheticals', () {
      expect(VocabQuestionFactory.shortGloss('game; a sport which is played (also спортивная игра)'), 'game');
      expect(VocabQuestionFactory.shortGloss('dog'), 'dog');
      expect(VocabQuestionFactory.shortGloss('to examine, to check, to control, to verify'),
          'to examine, to check');
      expect(VocabQuestionFactory.shortGloss('(time) moment; (figuratively) point'), 'moment');
    });

    test('shortGloss rejects inflected forms and Cyrillic', () {
      expect(VocabQuestionFactory.shortGloss('were; there were (plural past of быть)'), isNull);
      expect(VocabQuestionFactory.shortGloss('genitive singular of дом'), isNull);
      expect(VocabQuestionFactory.shortGloss('спортивная игра'), isNull);
      expect(VocabQuestionFactory.shortGloss(''), isNull);
    });
  });

  group('question bank (Russian)', () {
    final raw = jsonDecode(File('assets/games/ladder/ru_bank.json').readAsStringSync());
    final bank = QuestionBank.fromJson(raw);

    test('has 24 questions in each of the five tiers', () {
      for (var t = 1; t <= 5; t++) {
        expect(bank.tier(t).length, 24, reason: 'tier $t');
      }
    });

    test('every question is playable', () {
      final rnd = Random(11);
      for (final b in bank.questions) {
        final q = b.toQuestion(rnd);
        expect(q.options.length, 4, reason: b.id);
        expect(q.options.where((o) => o.correct).length, 1, reason: b.id);
        expect(q.options.map((o) => o.text).toSet().length, 4, reason: b.id);
        expect(q.canTranslate, isTrue, reason: b.id);
        expect(q.prompt.trim().endsWith('?'), isTrue, reason: b.id);
        for (final g in q.glossary) {
          final blob = '${q.prompt} ${q.options.map((o) => o.text).join(' ')}'.toLowerCase();
          expect(blob.contains(g.word.toLowerCase()), isTrue,
              reason: '${b.id}: glossary word ${g.word} not in question');
        }
      }
    });

    test('rejects a malformed file', () {
      expect(
        () => QuestionBank.fromJson([
          {
            'id': 'x',
            'tier': 1,
            'category': 'nature',
            'text': 'A?',
            'translation': 'A?',
            'correct': {'text': 'a', 'translation': 'a'},
            'distractors': [
              {'text': 'b', 'translation': 'b'},
              {'text': 'c', 'translation': 'c'},
            ],
          }
        ]),
        throwsFormatException,
      );
    });
  });

  group('building a Russian game', () {
    final deck = Deck.fromJson(
        jsonDecode(File('assets/decks/russian_core.json').readAsStringSync())
            as Map<String, dynamic>);
    final bank = QuestionBank.fromJson(
        jsonDecode(File('assets/games/ladder/ru_bank.json').readAsStringSync()));
    final pack = LadderPacks.russian;

    List<LadderQuestion> build(int seed, {Set<String> seen = const {}}) =>
        LadderBuilder(deck: deck, pack: pack, bank: bank, rnd: Random(seed), seen: seen)
            .build();

    test('the pack is registered and its blueprint has a step per rung', () {
      expect(LadderPacks.forLanguage('ru'), same(pack));
      expect(LadderPacks.forLanguage('xx'), isNull);
      expect(pack.blueprint.length, LadderRules.length);
    });

    test('many seeds always give a valid fifteen-question game', () {
      for (var seed = 0; seed < 60; seed++) {
        final qs = build(seed);
        expect(qs.length, 15, reason: 'seed $seed');
        expect(qs.map((q) => q.id).toSet().length, 15, reason: 'seed $seed');
        for (final q in qs) {
          expect(q.options.length, 4, reason: '${q.id} seed $seed');
          expect(q.options.where((o) => o.correct).length, 1, reason: '${q.id} seed $seed');
          expect(q.options.map((o) => o.text.toLowerCase()).toSet().length, 4,
              reason: '${q.id} seed $seed');
        }
        // And the engine accepts it.
        LadderGame(questions: qs);
      }
    });

    test('it starts easy and ends on knowledge questions', () {
      for (var seed = 0; seed < 30; seed++) {
        final qs = build(seed);
        expect(qs.first.kind, QuestionKind.vocabToTarget, reason: 'seed $seed');
        expect(qs.first.prompt, startsWith('How do you say'));
        // The first question is a picture-book word.
        expect(pack.starterLemmas.contains(qs.first.correctOption.speak), isTrue,
            reason: 'seed $seed');
        expect(qs.last.kind, QuestionKind.knowledge, reason: 'seed $seed');
        expect(qs[12].kind, QuestionKind.knowledge, reason: 'seed $seed');
        // The last two rungs come from the hardest bank tiers.
        final tier5 = bank.tier(5).map((b) => b.id).toSet();
        expect(tier5.contains(qs.last.id), isTrue, reason: 'seed $seed');
      }
    });

    test('vocabulary questions get harder up the ladder', () {
      double meanRank(List<int> ranks) =>
          ranks.reduce((a, b) => a + b) / ranks.length;
      final rankById = {for (final c in deck.cards) c.id: c.rank};
      final early = <int>[];
      final deep = <int>[];
      for (var seed = 0; seed < 40; seed++) {
        final qs = build(seed);
        for (var i = 0; i < qs.length; i++) {
          if (qs[i].kind == QuestionKind.knowledge) continue;
          final cardId = qs[i].id.substring(qs[i].id.indexOf('_') + 1);
          final rank = rankById[cardId]!;
          if (i < 5) early.add(rank);
          if (i >= 8) deep.add(rank);
        }
      }
      expect(meanRank(deep), greaterThan(meanRank(early) * 2));
    });

    test('generated questions carry no giveaways', () {
      for (var seed = 0; seed < 40; seed++) {
        for (final q in build(seed)) {
          switch (q.kind) {
            case QuestionKind.vocabToTarget:
              // The English gloss is the prompt, so no option may show it.
              expect(q.canTranslate, isFalse);
              expect(q.optionsAreTarget, isTrue);
            case QuestionKind.vocabToEnglish:
              expect(q.canTranslate, isFalse);
              expect(q.optionsAreTarget, isFalse);
              expect(q.speakPrompt, isNotNull);
            case QuestionKind.sentenceGap:
              expect(q.prompt, contains('_____'));
              expect(q.detail, isNotNull);
              expect(q.revealSpeak, isNotNull);
              expect(q.revealSpeak, isNot(contains('_____')));
              // Speaking the prompt before the answer would give it away.
              expect(q.speakPrompt, isNull);
              final correct = q.correctOption.text;
              expect(q.revealSpeak, contains(correct));
            case QuestionKind.knowledge:
              expect(q.canTranslate, isTrue);
          }
        }
      }
    });

    test('questions the player has seen are avoided while fresh ones remain', () {
      final first = build(1);
      final seen = {
        for (final q in first)
          if (q.kind == QuestionKind.knowledge) q.id,
      };
      // Tier 5 has 24 questions and the game uses at most a few, so a second
      // game with the same seed must not repeat any seen knowledge question.
      final second = build(1, seen: seen);
      for (final q in second) {
        if (q.kind == QuestionKind.knowledge) {
          expect(seen.contains(q.id), isFalse, reason: q.id);
        }
      }
    });
  });

  group('generic pack: every language, any deck', () {
    final en = QuestionBank.fromJson(
        jsonDecode(File('assets/games/ladder/en_bank.json').readAsStringSync()),
        english: true);

    // The twelve deck languages, plus one the app has no texts for.
    const languages = [..._allCodes, 'xx'];

    List<LadderQuestion> build(Deck deck, int seed, {Set<String> seen = const {}}) =>
        LadderBuilder(
          deck: deck,
          pack: LadderPacks.forDeck(deck),
          bank: en,
          rnd: Random(seed),
          seen: seen,
        ).build();

    for (final lang in languages) {
      test('a full game is built at every deck size: $lang', () {
        for (final size in [5000, 3000, 300]) {
          final deck = fakeDeck(
              language: lang, size: size, rtl: lang == 'ar' || lang == 'arz');
          final pack = LadderPacks.forDeck(deck);
          for (var seed = 0; seed < 6; seed++) {
            final qs = build(deck, seed);
            expectValidGame(qs, '$lang/$size/seed $seed');
            // And the engine accepts it with the pack's own lifelines.
            LadderGame(questions: qs, lifelines: pack.lifelines);
          }
        }
      });
    }

    test('the same seed gives the same game', () {
      final deck = fakeDeck(language: 'tr', size: 3000);
      for (var seed = 0; seed < 5; seed++) {
        final a = build(deck, seed);
        final b = build(deck, seed);
        expect(a.map((q) => q.id).toList(), b.map((q) => q.id).toList());
        expect(a.map((q) => q.prompt).toList(), b.map((q) => q.prompt).toList());
      }
    });

    test('it opens with picture-book words and ends on hard facts', () {
      for (final lang in languages) {
        final deck = fakeDeck(language: lang, size: 3000);
        for (var seed = 0; seed < 4; seed++) {
          final qs = build(deck, seed);
          final why = '$lang seed $seed';
          expect(qs[0].kind, QuestionKind.vocabToTarget, reason: why);
          expect(kStarterGlosses.contains(correctGloss(qs[0])), isTrue, reason: why);
          expect(kStarterGlosses.contains(correctGloss(qs[1])), isTrue, reason: why);
          expect(qs[12].kind, QuestionKind.knowledge, reason: why);
          expect(qs[14].kind, QuestionKind.knowledge, reason: why);
          expect(en.tier(4).any((b) => b.id == qs[12].id), isTrue, reason: why);
          expect(en.tier(5).any((b) => b.id == qs[14].id), isTrue, reason: why);
        }
      }
    });

    test('vocabulary questions stay inside their planned rank windows', () {
      for (final size in [5000, 3000, 300]) {
        final deck = fakeDeck(size: size);
        final pack = LadderPacks.forDeck(deck);
        for (var seed = 0; seed < 20; seed++) {
          final qs = build(deck, seed);
          for (var i = 0; i < qs.length; i++) {
            if (qs[i].kind == QuestionKind.knowledge) continue;
            expect(inPlan(pack, i, qs[i], size), isTrue,
                reason: 'size $size seed $seed step ${i + 1} ${qs[i].id}');
          }
        }
      }
    });

    test('vocabulary gets harder up the ladder', () {
      final deck = fakeDeck(size: 5000);
      final early = <int>[];
      final deep = <int>[];
      for (var seed = 0; seed < 30; seed++) {
        final qs = build(deck, seed);
        for (var i = 0; i < qs.length; i++) {
          if (qs[i].kind == QuestionKind.knowledge) continue;
          if (i < 5) early.add(rankOf(qs[i]));
          if (i >= 8) deep.add(rankOf(qs[i]));
        }
      }
      expect(early, isNotEmpty);
      expect(deep, isNotEmpty);
      double mean(List<int> xs) => xs.reduce((a, b) => a + b) / xs.length;
      expect(mean(deep), greaterThan(mean(early) * 2));
      // The deep end of the deck is reached: the rarest words get asked.
      expect(deep.reduce(max), greaterThan(4000));
    });

    test('a deck with too few picture-book words starts from its commonest', () {
      for (final starters in [0, 5]) {
        final deck = fakeDeck(size: 3000, starters: starters);
        for (var seed = 0; seed < 10; seed++) {
          final qs = build(deck, seed);
          for (final q in qs.take(2)) {
            expect(q.kind, isNot(QuestionKind.knowledge));
            // 6% of the deck, the builder's stand-in for "commonest words".
            expect(rankOf(q), lessThanOrEqualTo(180),
                reason: '$starters starters, seed $seed');
          }
        }
      }
    });

    test('a deck without sentences still gives a full game with no gap question', () {
      for (final lang in languages) {
        final deck = fakeDeck(language: lang, size: 2000, sentences: false);
        for (var seed = 0; seed < 4; seed++) {
          final qs = build(deck, seed);
          expectValidGame(qs, '$lang seed $seed');
          expect(qs.where((q) => q.kind == QuestionKind.sentenceGap), isEmpty,
              reason: '$lang seed $seed');
        }
      }
    });

    test('sentences where the word never stands alone fall back to vocabulary', () {
      final deck = fakeDeck(language: 'es', size: 2000, unspaced: true);
      for (var seed = 0; seed < 10; seed++) {
        final qs = build(deck, seed);
        expectValidGame(qs, 'seed $seed');
        expect(qs.where((q) => q.kind == QuestionKind.sentenceGap), isEmpty);
      }
    });

    test('tiny and empty decks still give a full game', () {
      for (final size in [0, 3, 12, 40, 90]) {
        final deck = fakeDeck(language: 'sw', size: size);
        for (var seed = 0; seed < 5; seed++) {
          expectValidGame(build(deck, seed), 'size $size seed $seed');
        }
      }
    });

    test('a gap question is written for a spaced language', () {
      final deck = fakeDeck(language: 'es', size: 3000);
      var gaps = 0;
      for (var seed = 0; seed < 20; seed++) {
        for (final q in build(deck, seed)) {
          if (q.kind != QuestionKind.sentenceGap) continue;
          gaps++;
          expect(q.prompt, contains('_____'));
          expect(q.revealSpeak, isNot(contains('_____')));
          expect(q.speakPrompt, isNull);
          expect(q.revealSpeak, contains(q.correctOption.text));
        }
      }
      expect(gaps, greaterThan(10));
    });

    test('readings show where the script hides the pronunciation', () {
      final deck = fakeDeck(language: 'zh', size: 1500, reading: 'pinyin', unspaced: true);
      var checked = 0;
      for (var seed = 0; seed < 10; seed++) {
        for (final q in build(deck, seed)) {
          if (q.kind == QuestionKind.vocabToEnglish) {
            expect(q.detail, 'pinyin');
            expect(q.explanationEn, contains('(pinyin)'));
            checked++;
          } else if (q.kind == QuestionKind.vocabToTarget) {
            for (final o in q.options) {
              expect(o.translation, startsWith('pinyin · '));
            }
            checked++;
          }
        }
      }
      expect(checked, greaterThan(30));
    });

    test('knowledge questions are plain English with nothing to translate', () {
      final deck = fakeDeck(language: 'it', size: 2000);
      var n = 0;
      for (var seed = 0; seed < 16; seed++) {
        for (final q in build(deck, seed)) {
          if (q.kind != QuestionKind.knowledge) continue;
          n++;
          expect(q.id, startsWith('en_k_'));
          expect(q.promptIsTarget, isFalse);
          expect(q.optionsAreTarget, isFalse);
          expect(q.speakPrompt, isNull);
          expect(q.canTranslate, isFalse);
          expect(q.glossary, isEmpty);
          for (final o in q.options) {
            expect(o.speak, isNull);
            expect(o.translation, isNull);
          }
        }
      }
      expect(n, greaterThan(40));
    });

    test('generated questions carry no giveaways', () {
      final deck = fakeDeck(language: 'pl', size: 3000);
      for (var seed = 0; seed < 15; seed++) {
        for (final q in build(deck, seed)) {
          switch (q.kind) {
            case QuestionKind.vocabToTarget:
              expect(q.canTranslate, isFalse);
              expect(q.optionsAreTarget, isTrue);
              expect(q.prompt, startsWith('How do you say'));
            case QuestionKind.vocabToEnglish:
              expect(q.canTranslate, isFalse);
              expect(q.optionsAreTarget, isFalse);
              expect(q.speakPrompt, isNotNull);
            case QuestionKind.sentenceGap:
              expect(q.speakPrompt, isNull);
              expect(q.revealSpeak, isNotNull);
            case QuestionKind.knowledge:
              expect(q.canTranslate, isFalse);
          }
        }
      }
    });

    test('questions the player has seen are avoided while fresh ones remain', () {
      final deck = fakeDeck(language: 'ko', size: 2000);
      final first = build(deck, 1);
      final seen = {
        for (final q in first)
          if (q.kind == QuestionKind.knowledge) q.id,
      };
      expect(seen, isNotEmpty);
      for (final q in build(deck, 1, seen: seen)) {
        if (q.kind == QuestionKind.knowledge) {
          expect(seen.contains(q.id), isFalse, reason: q.id);
        }
      }
    });
  });

  group('English knowledge bank', () {
    final file = File('assets/games/ladder/en_bank.json');
    final raw = jsonDecode(file.readAsStringSync());
    final bank = QuestionBank.fromJson(raw, english: true);

    test('the asset exists and is listed in the pubspec', () {
      expect(file.existsSync(), isTrue);
      expect(File('pubspec.yaml').readAsStringSync(), contains('assets/games/ladder/'));
      expect(kEnglishBankAsset, 'assets/games/ladder/en_bank.json');
    });

    test('it is flagged English and has enough questions in every tier', () {
      expect(bank.english, isTrue);
      expect(bank.questions.every((q) => q.english), isTrue);
      for (var t = 1; t <= 5; t++) {
        expect(bank.tier(t).length, greaterThanOrEqualTo(18), reason: 'tier $t');
      }
    });

    test('ids are unique and carry their tier', () {
      final ids = bank.questions.map((q) => q.id).toSet();
      expect(ids.length, bank.questions.length);
      for (final b in bank.questions) {
        expect(b.id, startsWith('en_k_${b.tier}_'), reason: b.id);
      }
    });

    test('every question is playable plain English', () {
      final cyrillic = RegExp('[${String.fromCharCode(0x400)}-${String.fromCharCode(0x4ff)}]');
      final rnd = Random(12);
      for (final b in bank.questions) {
        final q = b.toQuestion(rnd);
        expect(q.kind, QuestionKind.knowledge, reason: b.id);
        expect(q.options.length, 4, reason: b.id);
        expect(q.options.where((o) => o.correct).length, 1, reason: b.id);
        expect(q.options.map((o) => o.text.toLowerCase()).toSet().length, 4,
            reason: b.id);
        expect(q.prompt.trim().endsWith('?'), isTrue, reason: b.id);
        expect(_subjects.contains(q.category), isTrue, reason: '${b.id} ${q.category}');
        expect(q.promptIsTarget, isFalse, reason: b.id);
        expect(q.optionsAreTarget, isFalse, reason: b.id);
        expect(q.speakPrompt, isNull, reason: b.id);
        expect(q.canTranslate, isFalse, reason: b.id);
        expect(q.glossary, isEmpty, reason: b.id);
        expect(q.explanationEn, isNull, reason: b.id);
        for (final o in q.options) {
          expect(o.speak, isNull, reason: b.id);
          expect(o.translation, isNull, reason: b.id);
        }
        final blob = '${q.prompt} ${q.options.map((o) => o.text).join(' ')} ${q.explanation}';
        expect(cyrillic.hasMatch(blob), isFalse, reason: '${b.id} has Cyrillic');
      }
    });

    test('the correct answer is shuffled, not always in the same place', () {
      final spots = <int>{};
      for (var seed = 0; seed < 30; seed++) {
        spots.add(bank.questions.first.toQuestion(Random(seed)).correctIndex);
      }
      expect(spots.length, greaterThan(1));
    });

    test('it needs no translations, but a language bank still does', () {
      // The same file read as a Russian-style bank is malformed.
      expect(() => QuestionBank.fromJson(raw), throwsFormatException);
      final one = jsonDecode(jsonEncode([
        {
          'id': 'en_k_1_99',
          'tier': 1,
          'category': 'nature',
          'text': 'What do bees make?',
          'correct': {'text': 'Honey'},
          'distractors': [
            {'text': 'Milk'},
            {'text': 'Bread'},
            {'text': 'Cheese'},
          ],
        }
      ]));
      final b = QuestionBank.fromJson(one, english: true);
      expect(b.questions.single.correct.translation, isEmpty);
      expect(b.questions.single.toQuestion(Random(1)).options.length, 4);
    });

    test('an English option may not be empty, nor may options repeat', () {
      List<Map<String, Object>> distractors(List<String> texts) =>
          [for (final t in texts) {'text': t}];
      Object make(List<String> wrong) => jsonDecode(jsonEncode([
            {
              'id': 'x',
              'tier': 1,
              'category': 'nature',
              'text': 'A?',
              'correct': {'text': 'a'},
              'distractors': distractors(wrong),
            }
          ]));
      expect(QuestionBank.fromJson(make(['b', 'c', 'd']), english: true).questions.length, 1);
      expect(() => QuestionBank.fromJson(make(['b', ' ', 'd']), english: true),
          throwsFormatException);
      expect(() => QuestionBank.fromJson(make(['b', 'b', 'd']), english: true),
          throwsFormatException);
      expect(() => QuestionBank.fromJson(make(['b', 'c']), english: true),
          throwsFormatException);
    });

    test('every generic pack points at it', () {
      for (final c in _allCodes) {
        final pack = LadderPacks.forLanguage(c)!;
        expect(pack.bankAsset, kEnglishBankAsset, reason: c);
        expect(pack.bankIsEnglish, isTrue, reason: c);
        expect(File(pack.bankAsset).existsSync(), isTrue, reason: c);
      }
      expect(LadderPacks.russian.bankIsEnglish, isFalse);
    });
  });

  group('every language has a pack', () {
    const codes = ['ru', ..._allCodes, 'xx'];
    LadderPack packFor(String code) =>
        LadderPacks.forDeck(fakeDeck(language: code, size: 20));

    test('forDeck always gives a pack, the same one each time', () {
      for (final c in codes) {
        final pack = packFor(c);
        expect(pack.language, c);
        expect(packFor(c), same(pack), reason: c);
      }
    });

    test('forLanguage and supports agree', () {
      for (final c in codes) {
        final known = c != 'xx';
        expect(LadderPacks.supports(c), known, reason: c);
        expect(LadderPacks.forLanguage(c) != null, known, reason: c);
        if (known) expect(LadderPacks.forLanguage(c), same(packFor(c)), reason: c);
      }
    });

    test('each pack has fifteen well-formed steps', () {
      for (final c in codes) {
        final pack = packFor(c);
        expect(pack.blueprint.length, LadderRules.length, reason: c);
        for (var i = 0; i < pack.blueprint.length; i++) {
          final step = pack.blueprint[i];
          final why = '$c step ${i + 1}';
          expect(step, isNotEmpty, reason: why);
          for (final spec in step) {
            expect(spec.weight, greaterThan(0), reason: why);
            if (spec.kind == QuestionKind.knowledge) {
              expect(spec.tier, inInclusiveRange(1, 5), reason: why);
            } else {
              expect(spec.minRank, greaterThanOrEqualTo(1), reason: why);
              expect(spec.minRank, lessThanOrEqualTo(spec.maxRank), reason: why);
              if (pack.relativeRanks) {
                expect(spec.maxRank, lessThanOrEqualTo(1000), reason: why);
              }
            }
          }
        }
        // Picture-book words first, facts only at the end.
        for (final i in [0, 1]) {
          expect(pack.blueprint[i].every((s) => s.starter), isTrue, reason: c);
        }
        for (final i in [12, 14]) {
          expect(pack.blueprint[i].every((s) => s.kind == QuestionKind.knowledge),
              isTrue,
              reason: c);
        }
      }
    });

    test('each pack has three friends covering every subject', () {
      for (final c in codes) {
        final pack = packFor(c);
        expect(pack.friends.length, 3, reason: c);
        expect(pack.friends.map((f) => f.id).toSet().length, 3, reason: c);
        final covered = <String>{};
        for (final f in pack.friends) {
          expect(f.name.trim(), isNotEmpty, reason: c);
          expect(f.role.trim(), isNotEmpty, reason: c);
          expect(f.nameTarget?.trim() ?? '', isNotEmpty, reason: c);
          expect(_subjects.containsAll(f.strengths), isTrue, reason: '$c ${f.id}');
          covered.addAll(f.strengths);
        }
        expect(covered, unorderedEquals(_subjects), reason: c);
      }
    });

    test('each pack has two short lines per mood and a host intro', () {
      for (final c in codes) {
        final pack = packFor(c);
        for (final mood in FriendMood.values) {
          final lines = pack.friendLines[mood] ?? const <FriendLine>[];
          expect(lines.length, greaterThanOrEqualTo(2), reason: '$c $mood');
          for (final l in lines) {
            expect(l.target, contains('{L}'), reason: '$c $mood');
            expect(l.english, contains('{L}'), reason: '$c $mood');
            expect(l.target.length, lessThan(60), reason: '$c ${l.target}');
            if (c != 'xx') {
              expect(l.target, isNot(l.english), reason: '$c ${l.target}');
            }
          }
        }
        expect(pack.hostIntro.target.trim(), isNotEmpty, reason: c);
        expect(pack.hostIntro.english.trim(), isNotEmpty, reason: c);
      }
    });

    test('scripts that are not Latin get native names and lines', () {
      bool nonAscii(String t) => t.runes.any((r) => r > 0x7f);
      for (final c in ['ja', 'zh', 'ko', 'ar', 'arz']) {
        final pack = packFor(c);
        for (final f in pack.friends) {
          expect(nonAscii(f.nameTarget ?? ''), isTrue, reason: '$c ${f.id}');
          expect(nonAscii(f.name), isFalse, reason: '$c ${f.id}: name is the Latin form');
        }
        expect(nonAscii(pack.hostIntro.target), isTrue, reason: c);
        for (final lines in pack.friendLines.values) {
          for (final l in lines) {
            expect(nonAscii(l.target), isTrue, reason: '$c ${l.target}');
          }
        }
      }
    });

    test('Russian keeps its own pack, every other language is generic', () {
      final ru = packFor('ru');
      expect(ru, same(LadderPacks.russian));
      expect(ru.lifelines, kAllLifelines);
      expect(ru.bankIsEnglish, isFalse);
      expect(ru.relativeRanks, isFalse);
      expect(ru.starterLemmas, isNotEmpty);
      for (final c in codes.where((c) => c != 'ru')) {
        final p = packFor(c);
        expect(p.bankIsEnglish, isTrue, reason: c);
        expect(p.relativeRanks, isTrue, reason: c);
        expect(p.starterLemmas, isEmpty, reason: c);
        expect(p.starterGlosses.length, greaterThanOrEqualTo(8), reason: c);
        expect(p.lifelines,
            unorderedEquals([Lifeline.fiftyFifty, Lifeline.audience, Lifeline.friend]),
            reason: c);
      }
    });

    test('only languages written without spaces drop the sentence gap', () {
      bool hasGap(LadderPack p) => p.blueprint
          .any((step) => step.any((s) => s.kind == QuestionKind.sentenceGap));
      expect(hasGap(packFor('zh')), isFalse);
      expect(hasGap(packFor('ja')), isFalse);
      expect(hasGap(packFor('es')), isTrue);
      expect(hasGap(packFor('ru')), isTrue);
    });

    test('every friend can be phoned in every pack', () {
      const categories = ['history', 'science', 'language', 'sports', 'society'];
      for (final c in codes) {
        final pack = packFor(c);
        for (final friend in pack.friends) {
          for (var seed = 0; seed < 40; seed++) {
            final q = mkQ(seed, category: categories[seed % categories.length]);
            final a = phoneFriend(
              q: q,
              level: seed % 15,
              friend: friend,
              eliminated: {},
              lines: pack.friendLines,
              rnd: Random(seed),
            );
            expect(a.line.target, isNot(contains('{L}')), reason: c);
            expect(a.line.english, isNot(contains('{L}')), reason: c);
            expect(a.line.english, contains(String.fromCharCode(0x41 + a.optionIndex)),
                reason: c);
          }
        }
      }
    });
  });

  group('lifelines a pack leaves out', () {
    test('every lifeline is offered by default', () {
      expect(kAllLifelines, unorderedEquals(Lifeline.values));
      expect(LadderGame(questions: mkLadder()).lifelines, kAllLifelines);
    });

    test('a lifeline the pack omits can never be used, even when it would work', () {
      final g = LadderGame(
        questions: mkLadder(translation: 'x'), // every question has a translation
        lifelines: kGenericLifelines,
        rnd: Random(13),
      );
      expect(g.canUse(Lifeline.translate), isFalse);
      expect(g.whyNot(Lifeline.translate), isNotNull);
      expect(g.useTranslate, throwsStateError);
      expect(g.usedLifelines, isEmpty);
      for (final l in kGenericLifelines) {
        expect(g.canUse(l), isTrue, reason: l.label);
      }
    });

    test('the offered ones are spent as usual and show in the outcome', () {
      final pack = LadderPacks.forLanguage('es')!;
      final g = LadderGame(
        questions: mkLadder(),
        lifelines: pack.lifelines,
        rnd: Random(14),
      );
      g.useFiftyFifty();
      g.useAudience();
      g.useFriend(pack.friends.first, pack.friendLines);
      expect(g.usedLifelines.length, 3);
      for (final l in pack.lifelines) {
        expect(g.canUse(l), isFalse, reason: l.label);
      }
      final wrong = [
        for (var i = 0; i < 4; i++)
          if (i != g.current.correctIndex && g.isSelectable(i)) i,
      ].first;
      g.answer(wrong);
      expect(g.outcome.lifelinesUsed.length, 3);
      expect(g.outcome.lifelinesUsed.contains(Lifeline.translate), isFalse);
    });
  });

  group('vocabulary factory helpers', () {
    VocabCard card(int rank, String lemma, String gloss, {String pos = 'n'}) =>
        VocabCard(
          id: 'c$rank',
          rank: rank,
          lemma: lemma,
          pos: pos,
          posName: pos,
          gloss: gloss,
          sentences: const [],
        );

    final small = Deck(
      id: 'es_small',
      name: 'Small',
      language: 'es',
      languageName: 'Spanish',
      targetVoice: '',
      cards: [
        card(1, 'perro', 'dog, hound'),
        card(2, 'beber', 'to drink', pos: 'v'),
        card(3, 'Madrid', 'Madrid'), // a name: not fair game
        card(4, 'dogma', 'dogma'),
        card(5, 'el', 'the', pos: 'det'), // not a noun, verb or adjective
        card(6, 'agua', 'water'),
        card(7, 'Roma', 'Rome'),
        card(9000, 'cuando', 'when', pos: 'conj'),
      ],
    );

    test('maxUsableRank is the rarest card that can be asked about', () {
      final f = VocabQuestionFactory(small, Random(1));
      expect(f.usableCards, 4);
      expect(f.maxUsableRank, 6);
    });

    test('maxUsableRank is 0 for a deck with nothing to ask', () {
      final f = VocabQuestionFactory(fakeDeck(size: 0), Random(1));
      expect(f.usableCards, 0);
      expect(f.maxUsableRank, 0);
    });

    test('lemmasForGlosses finds cards by the first part of their short meaning', () {
      final f = VocabQuestionFactory(small, Random(1));
      expect(f.lemmasForGlosses({'dog', 'to drink', 'water'}),
          unorderedEquals(['perro', 'beber', 'agua']));
      expect(f.lemmasForGlosses({'hound'}), isEmpty); // only the first part counts
      expect(f.lemmasForGlosses({'dog'}), unorderedEquals(['perro'])); // not dogma
      expect(f.lemmasForGlosses({'madrid', 'the', 'when'}), isEmpty); // unusable cards
      expect(f.lemmasForGlosses(<String>{}), isEmpty);
    });

    test('lemmasForGlosses can leave out words ranked beyond a cap', () {
      final f = VocabQuestionFactory(small, Random(1));
      expect(f.lemmasForGlosses({'dog', 'to drink', 'water'}, maxRank: 2),
          unorderedEquals(['perro', 'beber']));
      expect(f.lemmasForGlosses({'water'}, maxRank: 5), isEmpty);
      expect(f.lemmasForGlosses({'water'}, maxRank: 6), unorderedEquals(['agua']));
    });

    test('a word that has a reading carries it, one that has none does not', () {
      final withReading = VocabQuestionFactory(
          fakeDeck(language: 'zh', size: 300, reading: 'pin'), Random(1));
      final q = withReading.vocabToEnglish(
          minRank: 1, maxRank: 300, difficulty: 0.3, usedCards: <String>{});
      expect(q, isNotNull);
      expect(q!.detail, 'pin');

      final plain = VocabQuestionFactory(fakeDeck(size: 300), Random(1));
      final p = plain.vocabToEnglish(
          minRank: 1, maxRank: 300, difficulty: 0.3, usedCards: <String>{});
      expect(p, isNotNull);
      expect(p!.detail, isNull);
      final t = plain.vocabToTarget(
          minRank: 1, maxRank: 300, difficulty: 0.3, usedCards: <String>{});
      expect(t, isNotNull);
      for (final o in t!.options) {
        expect(o.translation, isNotNull);
        expect(o.translation, isNot(contains(' · ')));
      }
    });

    test('two cards spelled alike never share a question', () {
      final deck = Deck(
        id: 'es_homographs',
        name: 'Homographs',
        language: 'es',
        languageName: 'Spanish',
        targetVoice: '',
        cards: [
          card(1, 'banco', 'bank'),
          card(2, 'banco', 'bench'),
          card(3, 'mesa', 'table'),
          card(4, 'silla', 'chair'),
          card(5, 'libro', 'book'),
          card(6, 'casa', 'house'),
        ],
      );
      for (var seed = 0; seed < 40; seed++) {
        final f = VocabQuestionFactory(deck, Random(seed));
        final q = f.vocabToTarget(
            minRank: 1, maxRank: 2, difficulty: 0.5, usedCards: <String>{});
        expect(q, isNotNull, reason: 'seed $seed');
        expect(q!.options.map((o) => o.text).toSet().length, 4,
            reason: 'seed $seed');
      }
    });
  });

  group('every real deck', () {
    final files = Directory('assets/decks')
        .listSync()
        .whereType<File>()
        .where((f) => f.path.endsWith('.json'))
        .toList()
      ..sort((a, b) => a.path.compareTo(b.path));
    final en = QuestionBank.fromJson(
        jsonDecode(File('assets/games/ladder/en_bank.json').readAsStringSync()),
        english: true);
    final ru = QuestionBank.fromJson(
        jsonDecode(File('assets/games/ladder/ru_bank.json').readAsStringSync()));

    test('there are decks to test', () => expect(files.length, greaterThanOrEqualTo(13)));

    for (final f in files) {
      test('plays a Lingo Ladder: ${f.uri.pathSegments.last}', () {
        final deck = Deck.fromJson(
            jsonDecode(f.readAsStringSync()) as Map<String, dynamic>);
        final pack = LadderPacks.forDeck(deck);
        expect(pack.language, deck.language);
        final bank = pack.bankIsEnglish ? en : ru;
        for (var seed = 0; seed < 3; seed++) {
          final qs = LadderBuilder(
            deck: deck,
            pack: pack,
            bank: bank,
            rnd: Random(seed),
          ).build();
          expectValidGame(qs, '${deck.id} seed $seed');
          LadderGame(questions: qs, lifelines: pack.lifelines);
          if (pack.bankIsEnglish) {
            expect(qs.first.kind, QuestionKind.vocabToTarget, reason: deck.id);
            expect(kStarterGlosses.contains(correctGloss(qs.first)), isTrue,
                reason: '${deck.id} seed $seed: ${qs.first.prompt}');
          }
        }
      });
    }
  });

  group('statistics', () {
    LadderOutcome outcome(GameStatus s, int prize, int correct, List<String> ids) =>
        LadderOutcome(
          status: s,
          prize: prize,
          correctCount: correct,
          lifelinesUsed: {Lifeline.fiftyFifty},
          history: [
            for (final id in ids)
              AnswerRecord(question: mkQ(int.parse(id.substring(1))), chosenIndex: 0),
          ],
        );

    test('records games, wins and bests', () {
      final s = LadderStats();
      s.record(outcome(GameStatus.lost, 1000, 7, ['q1', 'q2']));
      s.record(outcome(GameStatus.won, 1000000, 15, ['q3']));
      s.record(outcome(GameStatus.walkedAway, 4000, 7, []));
      expect(s.gamesPlayed, 3);
      expect(s.gamesWon, 1);
      expect(s.bestPrize, 1000000);
      expect(s.bestStreak, 15);
      expect(s.totalCorrect, 29);
      expect(s.seen, containsAll(['q1', 'q2', 'q3']));
    });

    test('survives a JSON round trip', () {
      final s = LadderStats()
        ..record(outcome(GameStatus.lost, 100, 2, ['q1', 'q2']));
      final back = LadderStats.fromJson(
          jsonDecode(jsonEncode(s.toJson())) as Map<String, dynamic>);
      expect(back.gamesPlayed, 1);
      expect(back.bestPrize, 100);
      expect(back.seen, s.seen);
    });

    test('keeps only the most recent 400 seen ids', () {
      final s = LadderStats();
      for (var i = 0; i < 500; i++) {
        s.record(outcome(GameStatus.lost, 0, 0, ['q$i']));
      }
      expect(s.seen.length, 400);
      expect(s.seen.contains('q0'), isFalse);
      expect(s.seen.contains('q499'), isTrue);
    });
  });
}
