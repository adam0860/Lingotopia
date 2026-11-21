import 'dart:convert';
import 'dart:io';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';
import 'package:lingotopia/games/ladder/vocab_questions.dart';
import 'package:lingotopia/games/match/match_game.dart';
import 'package:lingotopia/games/match/match_stats.dart';

/// Sixty unrelated English words: no two share a content word.
const _words = [
  'apple', 'river', 'mountain', 'window', 'garden', 'bridge', 'candle',
  'dragon', 'forest', 'hammer', 'island', 'jacket', 'kitchen', 'ladder',
  'mirror', 'needle', 'orange', 'pencil', 'quarter', 'rabbit', 'saddle',
  'tunnel', 'umbrella', 'valley', 'wagon', 'yellow', 'zebra', 'anchor',
  'basket', 'castle', 'desert', 'engine', 'feather', 'glove', 'harbor',
  'insect', 'jungle', 'kettle', 'lemon', 'market', 'napkin', 'ocean',
  'pillow', 'rocket', 'spoon', 'tiger', 'violin', 'whistle', 'bottle',
  'carpet', 'doctor', 'eagle', 'flower', 'guitar', 'helmet', 'ladle',
  'magnet', 'nickel', 'paddle', 'ribbon',
];

VocabCard card(
  int i,
  String gloss, {
  String? lemma,
  String pos = 'n',
  int? rank,
}) =>
    VocabCard(
      id: 'c$i',
      rank: rank ?? i + 1,
      lemma: lemma ?? 'lem$i',
      pos: pos,
      posName: pos,
      gloss: gloss,
      sentences: const [],
    );

Deck deckOfCards(List<VocabCard> cards) => Deck(
      id: 'xx_test',
      name: 'Test',
      language: 'xx',
      languageName: 'Testish',
      targetVoice: '',
      cards: cards,
    );

/// [n] usable cards (at most 60) with unrelated meanings, ranked 1..n.
Deck cleanDeck(int n) =>
    deckOfCards([for (var i = 0; i < n; i++) card(i, _words[i])]);

MatchGame newGame({
  int cards = 40,
  int boards = 3,
  int seed = 1,
  MatchPool pool = const MatchPool(),
}) =>
    MatchGame(
      deck: cleanDeck(cards),
      pool: pool,
      boards: boards,
      rnd: Random(seed),
    );

/// Tap the word and the meaning of pair [p] (an index into board.pairs).
MatchPick matchPair(MatchGame g, int p) {
  final b = g.board;
  g.pick(MatchSide.left, b.leftOrder.indexOf(p));
  return g.pick(MatchSide.right, b.rightOrder.indexOf(p));
}

/// Tap the word of pair [wordPair] and the meaning of pair [meaningPair].
MatchPick tapPair(MatchGame g, int wordPair, int meaningPair) {
  final b = g.board;
  g.pick(MatchSide.left, b.leftOrder.indexOf(wordPair));
  return g.pick(MatchSide.right, b.rightOrder.indexOf(meaningPair));
}

void solveBoard(MatchGame g) {
  for (var p = 0; p < g.board.size; p++) {
    matchPair(g, p);
  }
}

/// Clears every board without a miss; returns the boards in the order played.
List<MatchBoard> playThrough(MatchGame g) {
  final seen = <MatchBoard>[];
  while (g.isPlayable && !g.isFinished) {
    seen.add(g.board);
    solveBoard(g);
    if (!g.isFinished) expect(g.nextBoard(), isTrue);
  }
  return seen;
}

Set<String> words(MatchPair p) => VocabQuestionFactory.contentWords(p.gloss);

/// Every board: distinct cards, distinct lemmas, and no two meanings that
/// share a content word.
void expectFairBoard(MatchBoard b, String where) {
  expect({for (final p in b.pairs) p.card.id}.length, b.size,
      reason: '$where: a card twice');
  expect({for (final p in b.pairs) p.card.lemma}.length, b.size,
      reason: '$where: a lemma twice');
  expect({for (final p in b.pairs) p.gloss.toLowerCase()}.length, b.size,
      reason: '$where: a meaning twice');
  for (var i = 0; i < b.size; i++) {
    for (var j = i + 1; j < b.size; j++) {
      final shared = words(b.pairs[i]).intersection(words(b.pairs[j]));
      expect(shared, isEmpty,
          reason: '$where: "${b.pairs[i].gloss}" and "${b.pairs[j].gloss}" '
              'share $shared');
    }
  }
  final left = [...b.leftOrder]..sort();
  final right = [...b.rightOrder]..sort();
  final all = [for (var i = 0; i < b.size; i++) i];
  expect(left, all, reason: '$where: left order is not a permutation');
  expect(right, all, reason: '$where: right order is not a permutation');
}

void main() {
  group('boards', () {
    test('six distinct pairs, no conflicting meanings, columns shuffled', () {
      for (var seed = 1; seed <= 25; seed++) {
        final g = newGame(cards: 60, boards: 8, seed: seed);
        expect(g.boardCount, 8);
        final boards = playThrough(g);
        expect(boards.length, 8);
        for (var i = 0; i < boards.length; i++) {
          expect(boards[i].size, 6);
          expectFairBoard(boards[i], 'seed $seed board $i');
          expect(boards[i].leftOrder, isNot(boards[i].rightOrder),
              reason: 'seed $seed board $i: both columns in the same order');
        }
      }
    });

    test('meanings that share a content word never share a board', () {
      final glosses = [
        'big house', 'small house', 'old house', 'new house', 'red house',
        'house', // all say "house"
        'to run', 'run fast', 'run quickly', 'to run away', // all say "run"
        ..._words.take(30),
      ];
      final deck = deckOfCards([
        for (var i = 0; i < glosses.length; i++) card(i, glosses[i]),
      ]);
      for (var seed = 1; seed <= 25; seed++) {
        final g = MatchGame(
            deck: deck, pool: const MatchPool(), boards: 4, rnd: Random(seed));
        expect(g.boardCount, 4);
        final boards = playThrough(g);
        for (var i = 0; i < boards.length; i++) {
          expect(boards[i].size, 6);
          expectFairBoard(boards[i], 'seed $seed board $i');
        }
      }
    });

    test('another sense in the whole gloss counts as a conflict too', () {
      // "to look" is the short meaning of the first card, but its whole gloss
      // also says "watch": both cards are right for "to watch".
      final cards = [
        card(0, 'to look; to watch'),
        card(1, 'to watch'),
        for (var i = 0; i < 30; i++) card(i + 2, _words[i]),
      ];
      final deck = deckOfCards(cards);
      for (var seed = 1; seed <= 25; seed++) {
        final g = MatchGame(
            deck: deck, pool: const MatchPool(), boards: 4, rnd: Random(seed));
        for (final b in playThrough(g)) {
          final ids = {for (final p in b.pairs) p.card.id};
          expect(ids.containsAll({'c0', 'c1'}), isFalse, reason: 'seed $seed');
        }
      }
    });

    test('two cards with the same lemma never share a board', () {
      final cards = [
        for (var i = 0; i < 30; i++) card(i, _words[i]),
        // Six more cards whose lemma repeats one of the first six.
        for (var i = 0; i < 6; i++) card(30 + i, _words[30 + i], lemma: 'lem$i'),
      ];
      final deck = deckOfCards(cards);
      for (var seed = 1; seed <= 25; seed++) {
        final g = MatchGame(
            deck: deck, pool: const MatchPool(), boards: 5, rnd: Random(seed));
        for (final b in playThrough(g)) {
          expectFairBoard(b, 'seed $seed');
        }
      }
    });

    test('no card is used twice in a game', () {
      for (var seed = 1; seed <= 25; seed++) {
        final g = newGame(cards: 60, boards: 8, seed: seed);
        final ids = <String>[];
        for (final b in playThrough(g)) {
          ids.addAll(b.pairs.map((p) => p.card.id));
        }
        expect(ids.length, 48);
        expect(ids.toSet().length, 48, reason: 'seed $seed repeated a card');
      }
    });

    test('a pool with exactly enough cards uses each one once', () {
      final g = newGame(cards: 30, boards: 5, seed: 4);
      expect(g.boardCount, 5);
      final ids = <String>[];
      for (final b in playThrough(g)) {
        ids.addAll(b.pairs.map((p) => p.card.id));
      }
      expect(ids.toSet().length, 30);
    });

    test('the same seed deals the same game', () {
      List<String> deal(int seed) {
        final g = newGame(cards: 60, boards: 5, seed: seed);
        final out = <String>[];
        for (final b in playThrough(g)) {
          out.add('${b.pairs.map((p) => p.card.id)} ${b.leftOrder} ${b.rightOrder}');
        }
        return out;
      }

      expect(deal(7), deal(7));
      expect(deal(7), isNot(deal(8)));
    });

    test('pairs carry the shared short meaning of the card', () {
      final g = newGame(cards: 40, boards: 3, seed: 2);
      for (final b in playThrough(g)) {
        for (final p in b.pairs) {
          expect(p.gloss, VocabQuestionFactory.usableGloss(p.card));
        }
      }
    });
  });

  group('picking', () {
    test('a right pair matches and locks both tiles', () {
      final g = newGame();
      final b = g.board;
      final l = b.leftOrder.indexOf(0);
      final r = b.rightOrder.indexOf(0);

      final first = g.pick(MatchSide.left, l);
      expect(first.outcome, MatchOutcome.selected);
      expect(g.selectedLeft, l);

      final second = g.pick(MatchSide.right, r);
      expect(second.outcome, MatchOutcome.matched);
      expect(second.leftRow, l);
      expect(second.rightRow, r);
      expect(second.pair, same(b.pairs[0]));
      expect(second.boardCleared, isFalse);
      expect(g.pairsMatched, 1);
      expect(g.misses, 0);
      expect(g.combo, 1);
      expect(g.isMatched(MatchSide.left, l), isTrue);
      expect(g.isMatched(MatchSide.right, r), isTrue);
      expect(g.selectedLeft, isNull);
      expect(g.selectedRight, isNull);

      // Locked tiles do nothing.
      expect(g.pick(MatchSide.left, l).outcome, MatchOutcome.ignored);
      expect(g.pick(MatchSide.right, r).outcome, MatchOutcome.ignored);
      expect(g.selectedLeft, isNull);
    });

    test('the order of the two taps does not matter', () {
      final g = newGame();
      final b = g.board;
      g.pick(MatchSide.right, b.rightOrder.indexOf(3));
      final r = g.pick(MatchSide.left, b.leftOrder.indexOf(3));
      expect(r.outcome, MatchOutcome.matched);
      expect(r.pair, same(b.pairs[3]));
    });

    test('a wrong pair adds exactly one miss and a 3000 ms penalty', () {
      final g = newGame();
      final b = g.board;
      g.pick(MatchSide.left, b.leftOrder.indexOf(0));
      final r = g.pick(MatchSide.right, b.rightOrder.indexOf(1));
      expect(r.outcome, MatchOutcome.wrong);
      expect(r.leftRow, b.leftOrder.indexOf(0));
      expect(r.rightRow, b.rightOrder.indexOf(1));
      expect(g.misses, 1);
      expect(g.boardMisses, 1);
      expect(MatchGame.missPenaltyMs, 3000);
      expect(g.penaltyMs, 3000);
      expect(g.pairsMatched, 0);
      expect(g.result(10000).finalMs, 13000);

      // Both tiles are free again, and nothing is selected.
      expect(g.selectedLeft, isNull);
      expect(g.selectedRight, isNull);
      expect(g.isMatched(MatchSide.left, b.leftOrder.indexOf(0)), isFalse);

      tapPair(g, 2, 3);
      expect(g.misses, 2);
      expect(g.penaltyMs, 6000);
      expect(g.result(10000).finalMs, 16000);
      expect(g.result(10000).penaltyMs, 6000);
    });

    test('tapping a selected tile again puts it back', () {
      final g = newGame();
      expect(g.pick(MatchSide.left, 2).outcome, MatchOutcome.selected);
      expect(g.selectedLeft, 2);
      expect(g.pick(MatchSide.left, 2).outcome, MatchOutcome.deselected);
      expect(g.selectedLeft, isNull);
      expect(g.pick(MatchSide.right, 4).outcome, MatchOutcome.selected);
      expect(g.pick(MatchSide.right, 4).outcome, MatchOutcome.deselected);
      expect(g.selectedRight, isNull);
      expect(g.misses, 0);
    });

    test('tapping another tile in the same column moves the selection', () {
      final g = newGame();
      g.pick(MatchSide.left, 1);
      final r = g.pick(MatchSide.left, 3);
      expect(r.outcome, MatchOutcome.selected);
      expect(g.selectedLeft, 3);
      expect(g.misses, 0);
    });

    test('rows out of range are ignored', () {
      final g = newGame();
      expect(g.pick(MatchSide.left, -1).outcome, MatchOutcome.ignored);
      expect(g.pick(MatchSide.right, 6).outcome, MatchOutcome.ignored);
      expect(g.selectedLeft, isNull);
      expect(g.selectedRight, isNull);
    });

    test('combo counts right picks in a row and a miss resets it', () {
      final g = newGame();
      matchPair(g, 0);
      matchPair(g, 1);
      matchPair(g, 2);
      expect(g.combo, 3);
      tapPair(g, 3, 4);
      expect(g.combo, 0);
      expect(g.bestCombo, 3);
      matchPair(g, 3);
      matchPair(g, 4);
      expect(g.combo, 2);
      expect(g.bestCombo, 3);
      matchPair(g, 5);
      expect(g.combo, 3);
      expect(g.result(0).bestCombo, 3);
    });

    test('words in a wrong pick are listed, the most confused first', () {
      final g = newGame();
      final b = g.board;
      tapPair(g, 0, 1); // involves 0 and 1
      tapPair(g, 2, 1); // involves 2 and 1 again
      final trouble = g.troubleWords.map((p) => p.card.id).toList();
      expect(trouble.length, 3);
      expect(trouble.first, b.pairs[1].card.id, reason: 'involved twice');
      expect(trouble.toSet(),
          {b.pairs[0].card.id, b.pairs[1].card.id, b.pairs[2].card.id});
      expect(g.result(0).trouble.length, 3);
    });

    test('a clean game has no trouble words', () {
      final g = newGame(boards: 2);
      playThrough(g);
      expect(g.troubleWords, isEmpty);
    });
  });

  group('boards and the end', () {
    test('a board with no misses counts as flawless, one with a miss does not', () {
      final g = newGame(boards: 2);
      expect(g.flawlessBoards, 0);

      final last = [for (var p = 0; p < 6; p++) matchPair(g, p)].last;
      expect(last.boardCleared, isTrue);
      expect(last.finished, isFalse);
      expect(g.boardCleared, isTrue);
      expect(g.flawlessBoards, 1);
      expect(g.boardsCleared, 1);
      expect(g.isFinished, isFalse);

      expect(g.nextBoard(), isTrue);
      expect(g.boardIndex, 1);
      expect(g.boardCleared, isFalse);
      expect(g.boardMisses, 0);

      tapPair(g, 0, 1);
      solveBoard(g);
      expect(g.isFinished, isTrue);
      expect(g.boardsCleared, 2);
      expect(g.flawlessBoards, 1, reason: 'the second board had a miss');
      expect(g.misses, 1);
    });

    test('a miss on one board does not spoil the next one', () {
      final g = newGame(boards: 3);
      tapPair(g, 0, 1);
      solveBoard(g);
      expect(g.flawlessBoards, 0);
      g.nextBoard();
      solveBoard(g);
      expect(g.flawlessBoards, 1);
    });

    test('the game finishes after N boards, and only then', () {
      for (final n in [1, 3, 5, 8]) {
        final g = newGame(cards: 60, boards: n, seed: n);
        expect(g.boardCount, n);
        expect(g.requestedBoards, n);
        var played = 0;
        while (!g.isFinished) {
          expect(g.boardIndex, played);
          solveBoard(g);
          played++;
          if (!g.isFinished) expect(g.nextBoard(), isTrue);
        }
        expect(played, n);
        expect(g.boardsCleared, n);
        expect(g.pairsMatched, 6 * n);
        expect(g.flawlessBoards, n);
      }
    });

    test('the last pick reports the end of the game', () {
      final g = newGame(boards: 1);
      final picks = [for (var p = 0; p < 6; p++) matchPair(g, p)];
      expect(picks.take(5).every((p) => !p.boardCleared && !p.finished), isTrue);
      expect(picks.last.boardCleared, isTrue);
      expect(picks.last.finished, isTrue);
      expect(g.isFinished, isTrue);
    });

    test('nothing changes after the end, and there is no next board', () {
      final g = newGame(boards: 1);
      solveBoard(g);
      expect(g.nextBoard(), isFalse);
      final misses = g.misses;
      expect(g.pick(MatchSide.left, 0).outcome, MatchOutcome.ignored);
      expect(g.pick(MatchSide.right, 0).outcome, MatchOutcome.ignored);
      expect(g.misses, misses);
      expect(g.pairsMatched, 6);
    });

    test('picks wait while a cleared board is on show; nextBoard needs a cleared board', () {
      final g = newGame(boards: 2);
      expect(g.nextBoard(), isFalse, reason: 'nothing cleared yet');
      solveBoard(g);
      expect(g.pick(MatchSide.left, 0).outcome, MatchOutcome.ignored);
      expect(g.selectedLeft, isNull);
      expect(g.nextBoard(), isTrue);
      expect(g.pick(MatchSide.left, 0).outcome, MatchOutcome.selected);
    });

    test('the result carries the run\'s numbers', () {
      final g = newGame(boards: 2);
      solveBoard(g);
      g.nextBoard();
      tapPair(g, 0, 1);
      tapPair(g, 2, 3);
      solveBoard(g);
      final r = g.result(41200);
      expect(r.boards, 2);
      expect(r.pairs, 12);
      expect(r.flawless, 1);
      expect(r.misses, 2);
      expect(r.elapsedMs, 41200);
      expect(r.penaltyMs, 6000);
      expect(r.finalMs, 47200);
    });

    test('time format is mm:ss.s', () {
      expect(formatMatchTime(0), '00:00.0');
      expect(formatMatchTime(7400), '00:07.4');
      expect(formatMatchTime(7499), '00:07.4');
      expect(formatMatchTime(67300), '01:07.3');
      expect(formatMatchTime(599999), '09:59.9');
      expect(formatMatchTime(-5), '00:00.0');
    });

    test('lengths: quick 3, standard 5, marathon 8; unknown ids give standard', () {
      expect(MatchLength.quick.boards, 3);
      expect(MatchLength.standard.boards, 5);
      expect(MatchLength.marathon.boards, 8);
      expect(MatchLength.all.map((l) => l.id).toSet().length, 3);
      expect(MatchLength.byId('marathon').boards, 8);
      expect(MatchLength.byId('nope').id, 'standard');
      expect(MatchLength.byId(null).id, 'standard');
    });
  });

  group('pools', () {
    test('maxRank keeps every card within the range', () {
      final g = newGame(
          cards: 60, boards: 5, seed: 3, pool: const MatchPool(maxRank: 30));
      // Cards are ranked 1..60, so 30 are in range: exactly five boards.
      expect(g.boardCount, 5);
      for (final b in playThrough(g)) {
        for (final p in b.pairs) {
          expect(p.card.rank, lessThanOrEqualTo(30));
        }
      }
    });

    test('a range with fewer cards than the run needs gives a shorter run', () {
      // 20 cards in range: three boards of six, and the two left over are too
      // few for a board.
      final g = newGame(
          cards: 60, boards: 8, seed: 3, pool: const MatchPool(maxRank: 20));
      expect(g.requestedBoards, 8);
      expect(g.boardCount, 3);
      for (final b in playThrough(g)) {
        for (final p in b.pairs) {
          expect(p.card.rank, lessThanOrEqualTo(20));
        }
      }
      expect(g.isFinished, isTrue);
    });

    test('cardIds restricts the game to those cards', () {
      final ids = {for (var i = 10; i < 34; i++) 'c$i'};
      final g = newGame(
          cards: 60, boards: 4, seed: 5, pool: MatchPool(cardIds: ids));
      expect(g.boardCount, 4);
      final used = <String>{};
      for (final b in playThrough(g)) {
        for (final p in b.pairs) {
          expect(ids, contains(p.card.id));
          used.add(p.card.id);
        }
      }
      expect(used.length, 24);
    });

    test('maxRank and cardIds work together', () {
      final ids = {for (var i = 0; i < 40; i++) 'c$i'};
      final pool = MatchPool(maxRank: 24, cardIds: ids);
      expect(pool.accepts(card(5, 'x')), isTrue);
      expect(pool.accepts(card(30, 'x')), isFalse, reason: 'rank 31 is too deep');
      expect(pool.accepts(card(50, 'x', rank: 1)), isFalse,
          reason: 'not one of the ids');
    });

    test('usableCards leaves out names, forms, phrases and other parts of speech', () {
      final deck = deckOfCards([
        for (var i = 0; i < 20; i++) card(i, _words[i]),
        card(20, 'in', pos: 'prep'),
        card(21, 'the capital of France', lemma: 'Paris'),
        card(22, 'plural of apple'),
        card(23, 'good morning', lemma: 'good morning'),
        card(24, 'a very very long meaning that goes on and on and on'),
        card(25, 'km', lemma: 'km'),
      ]);
      final usable = MatchGame.usableCards(deck);
      expect(usable.length, 20);
      expect(usable.map((c) => c.id), [for (var i = 0; i < 20; i++) 'c$i']);
      expect(MatchGame.usableCards(deck, const MatchPool(maxRank: 5)).length, 5);
    });

    test('unusable cards are never put on a board', () {
      final deck = deckOfCards([
        for (var i = 0; i < 30; i++) card(i, _words[i]),
        for (var i = 30; i < 40; i++) card(i, 'in', pos: 'prep'),
      ]);
      final g = MatchGame(
          deck: deck, pool: const MatchPool(), boards: 5, rnd: Random(1));
      expect(g.boardCount, 5);
      for (final b in playThrough(g)) {
        for (final p in b.pairs) {
          expect(p.card.pos, 'n');
        }
      }
    });

    test('the minimum pool size is 18, enough for a Quick run', () {
      expect(MatchPool.minimumCards, 18);
      expect(MatchLength.quick.boards * MatchGame.defaultPairsPerBoard,
          MatchPool.minimumCards);
      final g = newGame(cards: 18, boards: MatchLength.quick.boards, seed: 9);
      expect(g.boardCount, 3);
      expect(playThrough(g).every((b) => b.size == 6), isTrue);
    });
  });

  group('small pools', () {
    test('a pool for part of a run gives fewer boards and a short last board', () {
      // 40 usable cards, 10 boards asked for: six full boards and one of four.
      final g = newGame(cards: 40, boards: 10, seed: 2);
      expect(g.requestedBoards, 10);
      expect(g.boardCount, 7);
      final boards = playThrough(g);
      expect(boards.map((b) => b.size), [6, 6, 6, 6, 6, 6, 4]);
      expect(g.isFinished, isTrue);
      expect(g.boardsCleared, 7);
      expect(g.pairsMatched, 40);
    });

    test('ten cards give a board of six and a board of four', () {
      final g = newGame(cards: 10, boards: 3, seed: 2);
      expect(g.boardCount, 2);
      expect(g.totalPairs, 10);
      final boards = playThrough(g);
      expect(boards.map((b) => b.size), [6, 4]);
      expect(g.isFinished, isTrue);
    });

    test('five cards give one smaller board', () {
      final g = newGame(cards: 5, boards: 2, seed: 2);
      expect(g.boardCount, 1);
      expect(g.board.size, 5);
      expectFairBoard(g.board, 'five cards');
      solveBoard(g);
      expect(g.isFinished, isTrue);
    });

    test('too few cards for even a small board is not playable, and does not crash', () {
      final g = newGame(cards: 3, boards: 3, seed: 2);
      expect(g.isPlayable, isFalse);
      expect(g.boardCount, 0);
      expect(g.totalPairs, 0);
      expect(g.isFinished, isFalse);
      expect(g.pick(MatchSide.left, 0).outcome, MatchOutcome.ignored);
      expect(g.nextBoard(), isFalse);
      expect(g.isMatched(MatchSide.left, 0), isFalse);
      expect(g.troubleWords, isEmpty);
      expect(g.result(0).finalMs, 0);
    });

    test('an empty pool and zero boards are not playable either', () {
      final none = MatchGame(
          deck: cleanDeck(40),
          pool: const MatchPool(maxRank: 0),
          boards: 3,
          rnd: Random(1));
      expect(none.isPlayable, isFalse);

      final zero = newGame(boards: 0);
      expect(zero.isPlayable, isFalse);
      expect(zero.pick(MatchSide.left, 0).outcome, MatchOutcome.ignored);
    });

    test('a pool of near-twins cannot make a board, and does not crash', () {
      // Eight cards that all say "house" cannot make a fair board of more than
      // one pair, so there is nothing to play: no crash, no unfair board.
      final deck = deckOfCards([
        for (var i = 0; i < 8; i++) card(i, 'house'),
      ]);
      final g = MatchGame(
          deck: deck, pool: const MatchPool(), boards: 3, rnd: Random(1));
      expect(g.isPlayable, isFalse);
    });
  });

  group('word match stats', () {
    test('the first run of a length is its best, later ones must beat it', () {
      final s = WordMatchStats();
      expect(
          s.record(lengthId: 'quick', timeMs: 50000, boards: 3, flawless: 1),
          isTrue);
      expect(s.bestTimeMs['quick'], 50000);
      expect(
          s.record(lengthId: 'quick', timeMs: 60000, boards: 3, flawless: 0),
          isFalse);
      expect(s.bestTimeMs['quick'], 50000);
      expect(
          s.record(lengthId: 'quick', timeMs: 45500, boards: 3, flawless: 3),
          isTrue);
      expect(s.bestTimeMs['quick'], 45500);
      expect(
          s.record(lengthId: 'standard', timeMs: 99000, boards: 5, flawless: 2),
          isTrue);
      expect(s.bestTimeMs['standard'], 99000);

      expect(s.played, 4);
      expect(s.totalBoards, 14);
      expect(s.flawlessBoards, 6);
    });

    test('an equal time is not a new best', () {
      final s = WordMatchStats();
      s.record(lengthId: 'quick', timeMs: 30000, boards: 3, flawless: 0);
      expect(
          s.record(lengthId: 'quick', timeMs: 30000, boards: 3, flawless: 0),
          isFalse);
    });

    test('an unranked run counts in the totals but never as a best time', () {
      final s = WordMatchStats();
      final best = s.record(
          lengthId: 'marathon',
          timeMs: 1000,
          boards: 6,
          flawless: 2,
          ranked: false);
      expect(best, isFalse);
      expect(s.bestTimeMs, isEmpty);
      expect(s.played, 1);
      expect(s.totalBoards, 6);
      expect(s.flawlessBoards, 2);
    });

    test('survives JSON, including what the lobby remembers', () {
      final s = WordMatchStats()
        ..lastRange = 'studied'
        ..lastLength = 'marathon';
      s.record(lengthId: 'quick', timeMs: 41200, boards: 3, flawless: 2);
      s.record(lengthId: 'standard', timeMs: 98000, boards: 5, flawless: 1);

      final back = WordMatchStats.fromJson(
          jsonDecode(jsonEncode(s.toJson())) as Map<String, dynamic>);
      expect(back.played, 2);
      expect(back.totalBoards, 8);
      expect(back.flawlessBoards, 3);
      expect(back.bestTimeMs, {'quick': 41200, 'standard': 98000});
      expect(back.lastRange, 'studied');
      expect(back.lastLength, 'marathon');
    });

    test('an empty or odd JSON gives a fresh record', () {
      final s = WordMatchStats.fromJson(<String, dynamic>{});
      expect(s.played, 0);
      expect(s.bestTimeMs, isEmpty);
      expect(s.lastRange, isNull);
      expect(s.lastLength, isNull);

      final odd = WordMatchStats.fromJson(<String, dynamic>{
        'played': 2.0,
        'bestTimeMs': {'quick': 31000.0},
      });
      expect(odd.played, 2);
      expect(odd.bestTimeMs['quick'], 31000);
    });
  });

  group('real decks', () {
    final files = Directory('assets/decks')
        .listSync()
        .whereType<File>()
        .where((f) => f.path.endsWith('.json'))
        .toList()
      ..sort((a, b) => a.path.compareTo(b.path));

    Deck load(File f) => Deck.fromJson(
        jsonDecode(f.readAsStringSync()) as Map<String, dynamic>);

    test('there are decks to test', () => expect(files.length, greaterThanOrEqualTo(13)));

    for (final f in files) {
      test('every deck can feed a Marathon: ${f.uri.pathSegments.last}', () {
        final deck = load(f);
        final g = MatchGame(
            deck: deck,
            pool: const MatchPool(),
            boards: MatchLength.marathon.boards,
            rnd: Random(4));
        expect(g.boardCount, MatchLength.marathon.boards, reason: deck.id);
        final ids = <String>{};
        var n = 0;
        for (final b in playThrough(g)) {
          expect(b.size, 6, reason: deck.id);
          expectFairBoard(b, deck.id);
          for (final p in b.pairs) {
            expect(p.gloss, VocabQuestionFactory.usableGloss(p.card),
                reason: deck.id);
            expect(p.card.displayLemma, isNotEmpty);
            ids.add(p.card.id);
            n++;
          }
        }
        expect(ids.length, n, reason: '${deck.id}: a card repeated');
        expect(g.flawlessBoards, MatchLength.marathon.boards);
      });

      test('the first 500 words are enough for a run: ${f.uri.pathSegments.last}', () {
        final deck = load(f);
        final usable = MatchGame.usableCards(deck, const MatchPool(maxRank: 500));
        expect(usable.length,
            greaterThanOrEqualTo(MatchLength.marathon.boards * 6),
            reason: deck.id);
        final g = MatchGame(
            deck: deck,
            pool: const MatchPool(maxRank: 500),
            boards: MatchLength.marathon.boards,
            rnd: Random(6));
        expect(g.boardCount, MatchLength.marathon.boards, reason: deck.id);
        for (final b in playThrough(g)) {
          for (final p in b.pairs) {
            expect(p.card.rank, lessThanOrEqualTo(500), reason: deck.id);
          }
        }
      });
    }
  });
}
