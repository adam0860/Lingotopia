import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/data/models.dart';
import 'package:lingotopia/difficult/difficult_lists.dart';
import 'package:lingotopia/difficult/difficult_pool.dart';
import 'package:lingotopia/difficult/difficult_words_service.dart';
import 'package:lingotopia/difficult/question_ids.dart';
import 'package:lingotopia/difficult/trouble_store.dart';
import 'package:lingotopia/difficult/word_trouble.dart';

final _t0 = DateTime(2026, 11, 7, 9);
DateTime _at(int minutes) => _t0.add(Duration(minutes: minutes));

/// Feeds a list of answers (true = right) to one word and returns the final
/// state and the events, in order.
(WordTrouble, List<TroubleEvent>) run(
  List<bool> answers, {
  TroubleRules rules = TroubleRules.standard,
  WordTrouble? start,
}) {
  var w = start ?? WordTrouble.fresh('c1', 'd1');
  final events = <TroubleEvent>[];
  for (var i = 0; i < answers.length; i++) {
    final (next, e) = w.answered(
      correct: answers[i],
      at: _at(i),
      source: AnswerSource.flashcard,
      rules: rules,
    );
    w = next;
    events.add(e);
  }
  return (w, events);
}

void main() {
  group('WordTrouble rules', () {
    test('one miss is not enough', () {
      final (w, events) = run([false]);
      expect(w.inBank, isFalse);
      expect(w.missStreak, 1);
      expect(events, [TroubleEvent.none]);
    });

    test('two misses in a row put the word in the bank', () {
      final (w, events) = run([false, false]);
      expect(w.inBank, isTrue);
      expect(events, [TroubleEvent.none, TroubleEvent.added]);
      expect(w.timesAdded, 1);
      expect(w.totalMisses, 2);
      expect(w.addedAt, _at(1));
      expect(w.lastMissAt, _at(1));
    });

    test('a right answer between two misses starts the count again', () {
      final (w, _) = run([false, true, false]);
      expect(w.inBank, isFalse);
      expect(w.missStreak, 1);
      expect(w.totalMisses, 2);
      final (w2, _) = run([false, true, false, false]);
      expect(w2.inBank, isTrue);
    });

    test('the number of misses needed is a rule', () {
      const rules = TroubleRules(missesToAdd: 3);
      expect(run([false, false], rules: rules).$1.inBank, isFalse);
      expect(run([false, false, false], rules: rules).$1.inBank, isTrue);
      const one = TroubleRules(missesToAdd: 1);
      expect(run([false], rules: one).$1.inBank, isTrue);
    });

    test('three right answers in a row take a word out of the bank', () {
      final (w, events) = run([false, false, true, true, true]);
      expect(w.inBank, isFalse);
      expect(events.last, TroubleEvent.cleared);
      expect(events.where((e) => e == TroubleEvent.cleared).length, 1);
      expect(w.clearedAt, _at(4));
      // The history stays.
      expect(w.totalMisses, 2);
      expect(w.timesAdded, 1);
    });

    test('a miss while recovering starts the recovery again', () {
      final (w, events) = run([false, false, true, true, false, true, true]);
      expect(w.inBank, isTrue, reason: 'two hits after the miss are not three');
      expect(events.contains(TroubleEvent.cleared), isFalse);
      // One more right answer makes three in a row.
      final (w2, e2) = run([true], start: w);
      expect(w2.inBank, isFalse);
      expect(e2.single, TroubleEvent.cleared);
    });

    test('a word that left can come back, and is counted again', () {
      final (w, events) =
          run([false, false, true, true, true, false, false]);
      expect(w.inBank, isTrue);
      expect(w.timesAdded, 2);
      expect(events.where((e) => e == TroubleEvent.added).length, 2);
    });

    test('correctStillNeeded counts down while in the bank', () {
      final (a, _) = run([false, false]);
      expect(a.correctStillNeeded(TroubleRules.standard), 3);
      final (b, _) = run([true], start: a);
      expect(b.correctStillNeeded(TroubleRules.standard), 2);
      final (c, _) = run([false, false]);
      expect(run([true, true], start: c).$1.correctStillNeeded(TroubleRules.standard), 1);
      expect(WordTrouble.fresh('x', 'd').correctStillNeeded(TroubleRules.standard), 0);
    });

    test('rules for leaving are a setting too', () {
      const quick = TroubleRules(correctToClear: 2);
      final (w, _) = run([false, false, true, true], rules: quick);
      expect(w.inBank, isFalse);
    });

    test('the source of the latest miss is remembered', () {
      var w = WordTrouble.fresh('c1', 'd1');
      (w, _) = w.answered(correct: false, at: _at(0), source: AnswerSource.match);
      (w, _) = w.answered(correct: false, at: _at(1), source: AnswerSource.recall);
      (w, _) = w.answered(correct: true, at: _at(2), source: AnswerSource.ladder);
      expect(w.lastSource, AnswerSource.recall);
    });

    test('rows survive a round trip through a map', () {
      final (w, _) = run([false, false, true]);
      final back = WordTrouble.fromMap(w.toMap());
      expect(back.cardId, w.cardId);
      expect(back.deckId, w.deckId);
      expect(back.inBank, w.inBank);
      expect(back.missStreak, w.missStreak);
      expect(back.hitStreak, w.hitStreak);
      expect(back.totalMisses, w.totalMisses);
      expect(back.timesAdded, w.timesAdded);
      expect(back.addedAt, w.addedAt);
      expect(back.lastMissAt, w.lastMissAt);
      expect(back.lastAnswerAt, w.lastAnswerAt);
      expect(back.lastSource, w.lastSource);
      expect(back.clearedAt, isNull);
    });

    test('an unknown source name reads as flashcards', () {
      expect(AnswerSource.byName('zzz'), AnswerSource.flashcard);
      expect(AnswerSource.byName(null), AnswerSource.flashcard);
      for (final s in AnswerSource.values) {
        expect(AnswerSource.byName(s.name), s);
        expect(s.label, isNotEmpty);
      }
    });
  });

  group('DifficultWordsService', () {
    late MemoryTroubleStore store;
    late DifficultWordsService service;
    var rules = TroubleRules.standard;
    // Each answer is a minute after the last, so "most recent" is unambiguous.
    var tick = 0;

    setUp(() {
      store = MemoryTroubleStore();
      rules = TroubleRules.standard;
      tick = 0;
      service = DifficultWordsService(store: store, rules: () => rules);
    });

    TroubleEvent answer(String id, bool correct,
            {String deck = 'd1', AnswerSource source = AnswerSource.flashcard}) =>
        service.record(
          deckId: deck,
          cardId: id,
          correct: correct,
          source: source,
          at: _at(tick++),
        );

    test('a word never missed leaves no trace', () async {
      expect(answer('a', true), TroubleEvent.none);
      await service.flush();
      expect(store.rows, isEmpty);
      expect(service.rowFor('a'), isNull);
      expect(service.count('d1'), 0);
    });

    test('misses from different places add up', () async {
      answer('a', false, source: AnswerSource.match);
      final e = answer('a', false, source: AnswerSource.recall);
      expect(e, TroubleEvent.added);
      expect(service.isDifficult('a'), isTrue);
      expect(service.count('d1'), 1);
      expect(service.bankIds('d1'), {'a'});
      await service.flush();
      expect(store.rows['a']!.inBank, isTrue);
      expect(store.rows['a']!.lastSource, AnswerSource.recall);
    });

    test('the bank is kept per deck', () {
      answer('a', false);
      answer('a', false);
      answer('b', false, deck: 'd2');
      answer('b', false, deck: 'd2');
      expect(service.bankIds('d1'), {'a'});
      expect(service.bankIds('d2'), {'b'});
    });

    test('recovering removes the word and lists it as recovered', () async {
      answer('a', false);
      answer('a', false);
      answer('a', true);
      answer('a', true);
      expect(answer('a', true), TroubleEvent.cleared);
      expect(service.isDifficult('a'), isFalse);
      expect(service.recovered('d1').map((r) => r.cardId), ['a']);
      await service.flush();
      expect(store.rows['a']!.inBank, isFalse);
      expect(store.rows['a']!.clearedAt, isNotNull);
    });

    test('hits on an ordinary word do not write to the store', () async {
      answer('a', false);
      answer('a', true); // breaks the run of misses: one write
      await service.flush();
      final writes = store.saves;
      for (var i = 0; i < 5; i++) {
        answer('a', true);
      }
      await service.flush();
      expect(store.saves, writes);
    });

    test('the bank is ordered by misses, then by how recent', () async {
      answer('a', false);
      answer('a', false); // 2 misses
      answer('b', false);
      answer('b', false);
      answer('b', true);
      answer('b', false);
      answer('b', false); // 4 misses
      answer('c', false);
      answer('c', false); // 2 misses, later than a
      expect(service.bank('d1').map((r) => r.cardId), ['b', 'c', 'a']);
    });

    test('thresholds are read at the time of each answer', () {
      rules = const TroubleRules(missesToAdd: 3);
      answer('a', false);
      expect(answer('a', false), TroubleEvent.none);
      rules = const TroubleRules(missesToAdd: 2);
      expect(answer('a', false), TroubleEvent.added);
    });

    test('remove forgets the word entirely, in memory and in the store', () async {
      answer('a', false);
      answer('a', false);
      await service.remove('a');
      expect(service.isDifficult('a'), isFalse);
      expect(service.rowFor('a'), isNull);
      expect(store.rows, isEmpty);
    });

    test('removeAll empties one deck only', () async {
      for (final id in ['a', 'b']) {
        answer(id, false);
        answer(id, false);
      }
      answer('z', false, deck: 'd2');
      answer('z', false, deck: 'd2');
      await service.removeAll('d1');
      expect(service.count('d1'), 0);
      expect(service.count('d2'), 1);
    });

    test('a new service starts from what the store holds', () async {
      answer('a', false);
      answer('a', false);
      await service.flush();
      final again = DifficultWordsService(store: store);
      await again.init();
      expect(again.isDifficult('a'), isTrue);
      expect(again.bankIds('d1'), {'a'});
    });

    test('the bank notifies when its membership changes, not on every answer', () {
      var calls = 0;
      service.addListener(() => calls++);
      answer('a', false); // miss: no change to the bank
      expect(calls, 0);
      answer('a', false); // added
      expect(calls, 1);
      answer('a', true); // recovering: no change yet
      expect(calls, 1);
      answer('a', true);
      answer('a', true); // cleared
      expect(calls, 2);
    });

    test('a failing store never breaks answering', () async {
      final broken = DifficultWordsService(store: _BrokenStore());
      await broken.init();
      expect(
        broken.record(deckId: 'd', cardId: 'a', correct: false, source: AnswerSource.drill),
        TroubleEvent.none,
      );
      expect(
        broken.record(deckId: 'd', cardId: 'a', correct: false, source: AnswerSource.drill),
        TroubleEvent.added,
      );
      await broken.flush();
      expect(broken.isDifficult('a'), isTrue);
    });
  });

  group('vocabCardIdOf', () {
    test('reads the card from generated question ids', () {
      expect(vocabCardIdOf('v2t_es_00042'), 'es_00042');
      expect(vocabCardIdOf('t2e_tr_00001_bir'), 'tr_00001_bir');
      expect(vocabCardIdOf('gap_ru_00007'), 'ru_00007');
    });

    test('gives null for questions that are not about one word', () {
      expect(vocabCardIdOf('s2e_ru_00007_s1'), isNull);
      expect(vocabCardIdOf('ru_t3_017'), isNull);
      expect(vocabCardIdOf('v2t_'), isNull);
      expect(vocabCardIdOf(''), isNull);
    });
  });

  group('focusFirst', () {
    test('moves focus items to the front and keeps each group in order', () {
      final out = focusFirst<int>([5, 1, 4, 2, 3], (n) => n.isEven);
      expect(out, [4, 2, 5, 1, 3]);
    });

    test('changes nothing when nothing or everything is in focus', () {
      expect(focusFirst<int>([3, 1, 2], (_) => false), [3, 1, 2]);
      expect(focusFirst<int>([3, 1, 2], (_) => true), [3, 1, 2]);
      expect(focusFirst<int>(<int>[], (_) => true), isEmpty);
    });
  });

  group('difficultGamePool', () {
    VocabCard card(int rank, String gloss, {String pos = 'n', String? lemma}) =>
        VocabCard(
          id: 'c$rank',
          rank: rank,
          lemma: lemma ?? 'w$rank',
          pos: pos,
          posName: pos,
          gloss: gloss,
          sentences: const [],
        );

    // Ranks 1-40 are usable words; 41 is a name and 42 a preposition.
    final deck = Deck(
      id: 'd1',
      name: 'Test',
      language: 'es',
      languageName: 'Spanish',
      targetVoice: '',
      cards: [
        for (var r = 1; r <= 40; r++) card(r, 'meaning'),
        card(41, 'Madrid', lemma: 'Madrid'),
        card(42, 'with', pos: 'prep'),
      ],
    );

    test('the usable bank leaves out words the games cannot ask about', () {
      final cards = usableBankCards(deck, {'c3', 'c41', 'c42', 'c7', 'zzz'});
      expect(cards.map((c) => c.id), ['c3', 'c7']);
    });

    test('a small bank is topped up with studied words first', () {
      final ids = difficultGamePool(
        deck: deck,
        bankIds: {'c30', 'c31'},
        studiedIds: {'c5', 'c6', 'c7', 'c8', 'c9', 'c10'},
        minimum: 6,
        random: Random(1),
      );
      expect(ids.length, 6);
      expect(ids.containsAll(['c30', 'c31']), isTrue);
      // Four fillers, all from the studied words.
      final fillers = ids.difference({'c30', 'c31'});
      expect(fillers.every((id) => {'c5', 'c6', 'c7', 'c8', 'c9', 'c10'}.contains(id)),
          isTrue);
    });

    test('with too few studied words the commonest unstudied ones fill the rest', () {
      final ids = difficultGamePool(
        deck: deck,
        bankIds: {'c30'},
        studiedIds: {'c20'},
        minimum: 5,
        random: Random(1),
      );
      expect(ids, {'c30', 'c20', 'c1', 'c2', 'c3'});
    });

    test('a bank at least as big as the minimum is used alone', () {
      final bank = {for (var r = 10; r < 20; r++) 'c$r'};
      final ids = difficultGamePool(
        deck: deck,
        bankIds: bank,
        studiedIds: {'c1', 'c2'},
        minimum: 8,
      );
      expect(ids, bank);
    });

    test('unusable cards are never used as filler', () {
      final ids = difficultGamePool(
        deck: deck,
        bankIds: {'c1'},
        studiedIds: {'c41', 'c42'},
        minimum: 100,
      );
      expect(ids.contains('c41'), isFalse);
      expect(ids.contains('c42'), isFalse);
      expect(ids.length, 40);
    });
  });

  group('difficultPoolIds', () {
    test('keeps every banked word and tops up to the minimum', () {
      final ids = difficultPoolIds(
        bank: ['b1', 'b2', 'b3'],
        filler: ['f1', 'f2', 'f3', 'f4', 'f5'],
        minimum: 5,
      );
      expect(ids, {'b1', 'b2', 'b3', 'f1', 'f2'});
    });

    test('a bank bigger than the minimum is used as it is', () {
      final ids = difficultPoolIds(
        bank: ['b1', 'b2', 'b3', 'b4'],
        filler: ['f1', 'f2'],
        minimum: 3,
      );
      expect(ids, {'b1', 'b2', 'b3', 'b4'});
    });

    test('filler that is already banked is not counted twice', () {
      final ids = difficultPoolIds(
        bank: ['b1', 'b2'],
        filler: ['b1', 'f1', 'b2', 'f2'],
        minimum: 4,
      );
      expect(ids, {'b1', 'b2', 'f1', 'f2'});
    });

    test('runs out of filler gracefully', () {
      final ids = difficultPoolIds(bank: ['b1'], filler: ['f1'], minimum: 10);
      expect(ids, {'b1', 'f1'});
    });

    test('a bank is playable from five usable words', () {
      expect(bankIsPlayable(4), isFalse);
      expect(bankIsPlayable(5), isTrue);
      expect(bankIsPlayable(2, floor: 2), isTrue);
    });
  });
}

class _BrokenStore implements TroubleStore {
  @override
  Future<List<WordTrouble>> loadAll() async => throw StateError('no disk');

  @override
  Future<void> save(WordTrouble row) async => throw StateError('no disk');

  @override
  Future<void> delete(Iterable<String> cardIds) async => throw StateError('no disk');
}
