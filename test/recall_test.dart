import 'dart:convert';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';
import 'package:lingotopia/games/recall/recall_engine.dart';
import 'package:lingotopia/games/recall/recall_stats.dart';

// Unique, pronounceable fake words: base-70 digits, each one a consonant and
// a vowel. Three syllables are always six letters, so a made-up English gloss
// can never be a stop word and no two cards ever share a content word.
const _cons = ['b', 'd', 'f', 'g', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z'];
const _vows = ['a', 'e', 'i', 'o', 'u'];

String _word(int n, int syllables) {
  final b = StringBuffer();
  var rest = n;
  for (var k = 0; k < syllables; k++) {
    final s = rest % 70;
    rest ~/= 70;
    b.write(_cons[s % 14]);
    b.write(_vows[s ~/ 14]);
  }
  return b.toString();
}

/// A deck of [n] usable cards: card i has rank i + 1.
Deck fakeDeck(int n) => Deck(
      id: 'xx_test',
      name: 'Test deck',
      language: 'xx',
      languageName: 'Testish',
      targetVoice: '',
      cards: [
        for (var i = 0; i < n; i++)
          VocabCard(
            id: 'xx_$i',
            rank: i + 1,
            lemma: _word(i + 1000, 3),
            pos: 'n',
            posName: 'noun',
            gloss: _word(i + 20000, 3),
            sentences: const [],
          ),
      ],
    );

RecallRound newRound(
  Deck deck, {
  RecallPool pool = const RecallPool(),
  int seed = 1,
}) =>
    RecallRound(RecallQuestionSource(deck, pool, Random(seed)));

int right(RecallRound r) => r.current!.question.correctIndex;

int wrong(RecallRound r) => (r.current!.question.correctIndex + 1) % 4;

void main() {
  final deck = fakeDeck(1000);

  group('rules', () {
    test('the centre rank is 40 x 1.16^depth', () {
      expect(RecallRules.centerRank(0), closeTo(40, 1e-9));
      expect(RecallRules.centerRank(1), closeTo(46.4, 1e-9));
      expect(RecallRules.centerRank(10), closeTo(40 * pow(1.16, 10), 1e-9));
    });

    test('reach is rounded to the nearest 50 and never below 100', () {
      expect(RecallRules.reachRounded(0), 0);
      expect(RecallRules.reachRounded(3), 100);
      expect(RecallRules.reachRounded(120), 100);
      expect(RecallRules.reachRounded(125), 150);
      expect(RecallRules.reachRounded(1224), 1200);
      expect(RecallRules.reachRounded(1225), 1250);
    });
  });

  group('depth', () {
    test('a right answer goes one deeper, a miss two back, never below zero', () {
      final r = newRound(deck);
      expect(r.depth, 0);
      for (var i = 1; i <= 5; i++) {
        r.answer(right(r));
        expect(r.depth, i);
      }
      r.answer(wrong(r));
      expect(r.depth, 3);
      r.answer(wrong(r));
      expect(r.depth, 1);
      r.answer(wrong(r));
      expect(r.depth, 0);
      r.answer(wrong(r));
      expect(r.depth, 0);
    });

    test('every question lies within 0.6 to 1.4 times its centre rank', () {
      final src = RecallQuestionSource(deck, const RecallPool(), Random(3));
      for (var d = 0; d < 40; d++) {
        final q = src.next(d)!;
        final c = min(RecallRules.centerRank(d), 1000.0);
        expect(q.rank, greaterThanOrEqualTo(0.6 * c), reason: 'depth $d');
        expect(q.rank, lessThanOrEqualTo(1.4 * c), reason: 'depth $d');
      }
    });

    test('deeper questions are rarer words', () {
      double meanRank(int depth) {
        var total = 0;
        const n = 30;
        for (var seed = 0; seed < n; seed++) {
          final src = RecallQuestionSource(deck, const RecallPool(), Random(seed));
          total += src.next(depth)!.rank;
        }
        return total / n;
      }

      expect(meanRank(0), lessThan(80));
      expect(meanRank(10), greaterThan(meanRank(0) * 2));
      expect(meanRank(20), greaterThan(meanRank(10) * 2));
    });
  });

  group('restricted pools', () {
    test('a rank cap keeps every question inside the cap', () {
      final src = RecallQuestionSource(deck, const RecallPool(maxRank: 300), Random(4));
      for (var i = 0; i < 80; i++) {
        final rq = src.next(i % 40)!;
        expect(rq.rank, lessThanOrEqualTo(300));
      }
    });

    test('tiny pools never come up empty and never throw', () {
      const pools = <RecallPool>[
        RecallPool(maxRank: 1),
        RecallPool(maxRank: 3),
        RecallPool(cardIds: {'xx_500'}),
        RecallPool(cardIds: {'xx_10', 'xx_990'}),
      ];
      for (final p in pools) {
        final r = newRound(deck, pool: p, seed: 5);
        for (var i = 0; i < 60; i++) {
          expect(r.current, isNotNull, reason: 'question $i');
          expect(r.answer(right(r)), isNotNull);
        }
      }
    });

    test('an empty pool or a deck too small gives no question, not an error', () {
      final empty = RecallQuestionSource(
          deck, const RecallPool(cardIds: <String>{}), Random(1));
      expect(empty.next(0), isNull);
      final r = RecallRound(empty);
      expect(r.current, isNull);
      expect(r.isOver, isTrue);
      expect(r.answer(0), isNull);

      final small = RecallQuestionSource(fakeDeck(3), const RecallPool(), Random(1));
      expect(small.next(0), isNull);
    });

    test('words I have studied: only those cards, climbed in rank order', () {
      // Ranks 10, 20, ... 600: sixty cards.
      final studied = {for (var i = 9; i < 600; i += 10) deck.cards[i].id};
      for (var seed = 0; seed < 20; seed++) {
        final src = RecallQuestionSource(
            deck, RecallPool(cardIds: studied), Random(seed));
        // Depth 0 is centred on place 40 of 60: places 24 to 56, ranks 240 to 560.
        final early = src.next(0)!;
        expect(studied, contains(early.card.id));
        expect(early.rank, inInclusiveRange(240, 560));
      }
      for (var seed = 0; seed < 20; seed++) {
        final src = RecallQuestionSource(
            deck, RecallPool(cardIds: studied), Random(seed));
        // Far down the ladder the centre is capped at the last place.
        final deep = src.next(40)!;
        expect(studied, contains(deep.card.id));
        expect(deep.rank, inInclusiveRange(350, 600));
      }
      final src = RecallQuestionSource(deck, RecallPool(cardIds: studied), Random(9));
      for (var i = 0; i < 100; i++) {
        expect(studied, contains(src.next(i % 25)!.card.id));
      }
    });

    test('no card repeats until the whole pool has been used', () {
      final studied = {for (var i = 0; i < 45; i++) deck.cards[i * 20].id};
      final src = RecallQuestionSource(deck, RecallPool(cardIds: studied), Random(9));
      final seen = <String>{};
      for (var i = 0; i < 45; i++) {
        final rq = src.next(i % 20)!;
        expect(seen.add(rq.card.id), isTrue, reason: 'repeat at question $i');
      }
      expect(src.next(0), isNotNull, reason: 'starts over instead of running dry');
    });
  });

  group('questions', () {
    test('ids resolve back to the card, its rank and the right answer', () {
      final byId = {for (final c in deck.cards) c.id: c};
      final src = RecallQuestionSource(deck, const RecallPool(), Random(7));
      var toEnglish = 0;
      const n = 600;
      for (var i = 0; i < n; i++) {
        final rq = src.next(i % 30)!;
        final q = rq.question;
        final id = RecallQuestionSource.cardIdOf(q.id);
        final card = byId[id];
        expect(card, isNotNull, reason: q.id);
        expect(rq.card.id, id);
        expect(rq.rank, card!.rank);

        expect(q.options.length, 4, reason: q.id);
        expect(q.options.where((o) => o.correct).length, 1, reason: q.id);
        expect({for (final o in q.options) o.text}.length, 4,
            reason: 'duplicate options in ${q.id}');

        if (q.promptIsTarget) {
          toEnglish++;
          expect(q.id, startsWith('t2e_'));
          expect(rq.promptText, card.displayLemma);
          expect(q.speakPrompt, card.speakableLemma);
          expect(q.correctOption.text, rq.gloss);
        } else {
          expect(q.id, startsWith('v2t_'));
          expect(rq.promptText, rq.gloss);
          expect(q.correctOption.text, card.displayLemma);
        }
      }
      // About 60% ask for the English meaning.
      expect(toEnglish / n, inInclusiveRange(0.5, 0.7));
    });

    test('a card is not asked twice while others in reach are unused', () {
      final src = RecallQuestionSource(deck, const RecallPool(), Random(2));
      final seen = <String>{};
      for (var i = 0; i < 200; i++) {
        expect(seen.add(src.next(i % 25)!.card.id), isTrue, reason: 'question $i');
      }
    });
  });

  group('clock', () {
    test('a wrong answer costs 3 seconds, a right one nothing', () {
      final r = newRound(deck);
      r.advance(10);
      expect(r.remaining, closeTo(50, 1e-9));
      r.answer(right(r));
      expect(r.remaining, closeTo(50, 1e-9));
      final a = r.answer(wrong(r))!;
      expect(a.correct, isFalse);
      expect(a.penaltySeconds, 3);
      expect(r.remaining, closeTo(47, 1e-9));
    });

    test('every fifth right answer in a row adds 3 seconds', () {
      final r = newRound(deck);
      for (var i = 1; i <= 4; i++) {
        r.answer(right(r));
      }
      expect(r.remaining, closeTo(60, 1e-9));
      final fifth = r.answer(right(r))!;
      expect(fifth.bonusSeconds, closeTo(3, 1e-9));
      expect(r.remaining, closeTo(63, 1e-9));
      for (var i = 6; i <= 9; i++) {
        r.answer(right(r));
      }
      expect(r.remaining, closeTo(63, 1e-9));
      r.answer(right(r));
      expect(r.remaining, closeTo(66, 1e-9));
    });

    test('a miss resets the streak, so the next bonus needs five fresh rights', () {
      final r = newRound(deck);
      for (var i = 0; i < 4; i++) {
        r.answer(right(r));
      }
      r.answer(wrong(r));
      expect(r.streak, 0);
      expect(r.bestStreak, 4);
      expect(r.remaining, closeTo(57, 1e-9));
      for (var i = 0; i < 4; i++) {
        r.answer(right(r));
      }
      expect(r.remaining, closeTo(57, 1e-9));
      r.answer(right(r));
      expect(r.remaining, closeTo(60, 1e-9));
      expect(r.bestStreak, 5);
    });

    test('the clock never goes above 75 seconds', () {
      final r = newRound(deck);
      var highest = 0.0;
      for (var i = 0; i < 100; i++) {
        r.answer(right(r));
        highest = max(highest, r.remaining);
      }
      expect(highest, closeTo(75, 1e-9));
      expect(r.remaining, closeTo(75, 1e-9));

      // The bonus is trimmed to fit under the cap: 59 + 5 x 3 = 74, then +1.
      final r2 = newRound(deck, seed: 2);
      r2.advance(1);
      RecallAnswer? last;
      for (var i = 0; i < 30; i++) {
        last = r2.answer(right(r2));
      }
      expect(r2.remaining, closeTo(75, 1e-9));
      expect(last!.bonusSeconds, closeTo(1, 1e-9));
    });

    test('the round is over when the clock reaches zero', () {
      final r = newRound(deck);
      r.advance(59.5);
      expect(r.isOver, isFalse);
      r.advance(1);
      expect(r.isOver, isTrue);
      expect(r.remaining, 0);

      // Nothing counts any more.
      expect(r.answer(right(r)), isNull);
      expect(r.answered, 0);
      expect(r.correct, 0);
    });

    test('a miss that empties the clock ends the round', () {
      final r = newRound(deck);
      r.advance(58);
      r.answer(wrong(r));
      expect(r.remaining, 0);
      expect(r.isOver, isTrue);
      expect(r.missed.length, 1);
    });

    test('advance ignores zero and negative time', () {
      final r = newRound(deck);
      r.advance(0);
      r.advance(-5);
      expect(r.remaining, 60);
    });
  });

  group('reach and score', () {
    test('reach is the highest rank answered right, misses do not count', () {
      final r = newRound(deck, seed: 11);
      expect(r.reach, 0);
      final rnd = Random(2);
      var best = 0;
      for (var i = 0; i < 60 && !r.isOver; i++) {
        final q = r.current!;
        final good = rnd.nextDouble() < 0.7;
        if (good) best = max(best, q.rank);
        r.answer(good ? q.question.correctIndex : (q.question.correctIndex + 1) % 4);
        expect(r.reach, best, reason: 'after question $i');
      }
      expect(best, greaterThan(0));
    });

    test('a bad index is ignored', () {
      final r = newRound(deck);
      expect(r.answer(-1), isNull);
      expect(r.answer(4), isNull);
      expect(r.answered, 0);
    });

    test('the summary carries the score, reach, streak and misses', () {
      final r = newRound(deck);
      r.answer(right(r));
      r.answer(right(r));
      final missedCard = r.current!.card.id;
      r.answer(wrong(r));
      final s = r.summary;
      expect(s.correct, 2);
      expect(s.answered, 3);
      expect(s.bestStreak, 2);
      expect(s.reach, r.reach);
      expect(s.missed.map((m) => m.card.id), [missedCard]);
    });

    test('simulated rounds always end and keep their books straight', () {
      for (var seed = 0; seed < 6; seed++) {
        final rnd = Random(seed);
        final r = newRound(deck, seed: seed);
        var guard = 0;
        while (!r.isOver && guard++ < 500) {
          r.advance(1 + rnd.nextDouble() * 2);
          if (r.isOver) break;
          final q = r.current!;
          final good = rnd.nextDouble() < 0.8;
          r.answer(good ? q.question.correctIndex : (q.question.correctIndex + 1) % 4);
          expect(r.remaining, inInclusiveRange(0, 75));
          expect(r.depth, greaterThanOrEqualTo(0));
        }
        expect(r.isOver, isTrue, reason: 'seed $seed');
        expect(r.correct + r.missed.length, r.answered);
        expect(r.bestStreak, greaterThanOrEqualTo(r.streak));
      }
    });
  });

  group('stats', () {
    test('records the bests, flags records after the first round, survives JSON', () {
      final s = RecallStats();
      final first = s.record(score: 12, reach: 480, streak: 6);
      expect(first.any, isFalse, reason: 'nothing to beat on the first round');
      expect(s.played, 1);
      expect(s.bestScore, 12);
      expect(s.bestReach, 480);
      expect(s.bestStreak, 6);

      // 490 rounds to the same 500 as 480, so it is not a new reach.
      final second = s.record(score: 15, reach: 490, streak: 4);
      expect(second.score, isTrue);
      expect(second.reach, isFalse);
      expect(second.streak, isFalse);
      expect(s.played, 2);
      expect(s.bestScore, 15);
      expect(s.bestReach, 490);
      expect(s.bestStreak, 6);

      final third = s.record(score: 9, reach: 900, streak: 7);
      expect(third.score, isFalse);
      expect(third.reach, isTrue);
      expect(third.streak, isTrue);
      expect(third.any, isTrue);

      s.lastRange = 'studied';
      final back = RecallStats.fromJson(
          jsonDecode(jsonEncode(s.toJson())) as Map<String, dynamic>);
      expect(back.played, 3);
      expect(back.bestScore, 15);
      expect(back.bestReach, 900);
      expect(back.bestStreak, 7);
      expect(back.lastRange, 'studied');
    });

    test('an empty or partial record reads as zeros', () {
      final s = RecallStats.fromJson(<String, dynamic>{});
      expect(s.played, 0);
      expect(s.bestScore, 0);
      expect(s.bestReach, 0);
      expect(s.bestStreak, 0);
      expect(s.lastRange, isNull);
    });
  });
}
