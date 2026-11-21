import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/difficult/difficult_words_service.dart';
import 'package:lingotopia/difficult/trouble_store.dart';
import 'package:lingotopia/difficult/word_trouble.dart';
import 'package:lingotopia/progress/progress_models.dart';
import 'package:lingotopia/progress/trophies.dart';
import 'package:lingotopia/progress/xp_rules.dart';
import 'package:lingotopia/reading/reading_models.dart';
import 'package:lingotopia/reading/reading_repository.dart';
import 'package:lingotopia/reading/reading_rules.dart';
import 'package:lingotopia/reading/reading_store.dart';
import 'package:lingotopia/reading/word_knowledge.dart';
import 'package:lingotopia/reading/word_practice_service.dart';
import 'package:lingotopia/reading/word_practice_store.dart';
import 'package:lingotopia/srs/scheduler.dart';

const _readingsPath = 'assets/readings/ru_readings.json';

ReadingBook loadBook() => ReadingBook.fromJson(
    json.decode(File(_readingsPath).readAsStringSync()) as Map<String, dynamic>);

SchedulingState card({
  CardPhase phase = CardPhase.review,
  double stability = 0,
  int interval = 0,
}) =>
    SchedulingState(
      phase: phase,
      stability: stability,
      difficulty: 5,
      due: null,
      lastReview: null,
      reps: 3,
      lapses: 0,
      intervalDays: interval,
      learningStep: 0,
      ease: 2.5,
    );

WordPractice practice(int right, int wrong) =>
    WordPractice(cardId: 'c', deckId: 'd', right: right, wrong: wrong);

class _Lang {
  const _Lang(this.code, this.readings, this.deck, this.lessons, this.minPassages);
  final String code;
  final String readings;
  final String deck;
  final String lessons;
  final int minPassages;
}

const _langs = [
  _Lang('ru', _readingsPath, 'assets/decks/russian_core.json',
      'assets/lessons/russian_lessons.json', 170),
  _Lang('es', 'assets/readings/es_readings.json', 'assets/decks/spanish_core.json',
      'assets/lessons/es_lessons.json', 184),
  _Lang('ar', 'assets/readings/ar_readings.json', 'assets/decks/arabic_msa_core.json',
      'assets/lessons/ar_lessons.json', 104),
];

void main() {
  for (final lang in _langs) {
    if (!File(lang.readings).existsSync()) continue;
    _passageFileTests(lang);
  }

  group('joinTokens', () {
    test('keeps punctuation against the word before it', () {
      expect(joinTokens(['Это', 'дом', '?']), 'Это дом?');
      expect(joinTokens(['Он', 'сказал', ':', '«', 'Да', '»', '.']), 'Он сказал: «Да».');
      expect(joinTokens(['А', '—', 'Б']), 'А — Б');
      expect(joinTokens(['¿', 'Dónde', 'estás', '?']), '¿Dónde estás?');
      expect(joinTokens(['¡', 'Hola', '!', '¿', 'Qué', 'tal', '?']), '¡Hola! ¿Qué tal?');
      expect(joinTokens([]), '');
    });

    test('keeps Arabic punctuation against the word before it', () {
      expect(joinTokens(['هَلْ', 'أَنْتَ', 'طَالِب', '؟']), 'هَلْ أَنْتَ طَالِب؟');
      expect(joinTokens(['نَعَم', '،', 'أَنَا', 'طَالِب', '.']), 'نَعَم، أَنَا طَالِب.');
      expect(joinTokens(['قَالَ', ':', '«', 'شُكْرًا', '»', '.']), 'قَالَ: «شُكْرًا».');
      expect(joinTokens(['جَاءَ', '؛', 'ثُمَّ', 'ذَهَبَ']), 'جَاءَ؛ ثُمَّ ذَهَبَ');
    });
  });

  group('word knowledge', () {
    test('a card never studied, or still new, is unknown', () {
      expect(levelFromCard(null), Knowledge.unknown);
      expect(levelFromCard(card(phase: CardPhase.newCard)), Knowledge.unknown);
    });

    test('a card in learning is only seen', () {
      expect(levelFromCard(card(phase: CardPhase.learning)), Knowledge.seen);
      expect(
        levelFromCard(card(phase: CardPhase.relearning, stability: 30)),
        Knowledge.seen,
      );
    });

    test('a reviewed card is judged by how long it will be remembered', () {
      expect(levelFromCard(card(stability: 1, interval: 1)), Knowledge.seen);
      expect(levelFromCard(card(stability: 3.9, interval: 3)), Knowledge.seen);
      expect(levelFromCard(card(stability: 4, interval: 2)), Knowledge.familiar);
      expect(levelFromCard(card(stability: 1, interval: 20)), Knowledge.familiar);
      expect(levelFromCard(card(stability: 21, interval: 3)), Knowledge.known);
      expect(levelFromCard(card(stability: 2, interval: 40)), Knowledge.known);
    });

    test('games: a tally of answers', () {
      expect(levelFromPractice(null), Knowledge.unknown);
      expect(levelFromPractice(practice(0, 0)), Knowledge.unknown);
      expect(levelFromPractice(practice(1, 0)), Knowledge.seen);
      expect(levelFromPractice(practice(2, 0)), Knowledge.seen);
      expect(levelFromPractice(practice(3, 0)), Knowledge.familiar);
      expect(levelFromPractice(practice(3, 1)), Knowledge.familiar);
      expect(levelFromPractice(practice(2, 2)), Knowledge.seen);
      expect(levelFromPractice(practice(7, 0)), Knowledge.familiar);
      expect(levelFromPractice(practice(8, 0)), Knowledge.known);
      expect(levelFromPractice(practice(9, 1)), Knowledge.known);
      expect(levelFromPractice(practice(7, 3)), Knowledge.seen);
    });

    test('the better of the two streams wins', () {
      final e = WordEvidence(
        srs: card(phase: CardPhase.learning),
        practice: practice(9, 0),
      );
      expect(classifyWord(e), Knowledge.known);
      final f = WordEvidence(srs: card(stability: 30), practice: practice(1, 0));
      expect(classifyWord(f), Knowledge.known);
    });

    test('no evidence at all is unknown', () {
      expect(classifyWord(const WordEvidence()), Knowledge.unknown);
    });

    test('a word in the difficult bank is at most seen', () {
      final e = WordEvidence(srs: card(stability: 60), inDifficultBank: true);
      expect(classifyWord(e), Knowledge.seen);
      // ...but a bank word with no evidence stays unknown rather than rising.
      expect(classifyWord(const WordEvidence(inDifficultBank: true)), Knowledge.unknown);
    });

    test('a word missed last time is at most familiar', () {
      final e = WordEvidence(srs: card(stability: 60), missStreak: 1);
      expect(classifyWord(e), Knowledge.familiar);
      final seenOnly = WordEvidence(srs: card(stability: 1), missStreak: 1);
      expect(classifyWord(seenOnly), Knowledge.seen);
    });

    test('the explanation names the evidence', () {
      expect(explainKnowledge(const WordEvidence()), contains('Not met'));
      final e = WordEvidence(
        srs: card(stability: 30),
        practice: practice(5, 1),
        inDifficultBank: true,
      );
      final text = explainKnowledge(e);
      expect(text, contains('30 days'));
      expect(text, contains('5 of 6'));
      expect(text, contains('difficult'));
    });
  });

  group('games tally', () {
    test('counts right and wrong answers and persists them', () async {
      final store = MemoryWordPracticeStore();
      final svc = WordPracticeService(store);
      await svc.init();
      svc.record(deckId: 'd', cardId: 'a', correct: true);
      svc.record(deckId: 'd', cardId: 'a', correct: true);
      svc.record(deckId: 'd', cardId: 'a', correct: false);
      svc.record(deckId: 'd', cardId: 'b', correct: true);
      await svc.flush();
      expect(svc.practiceFor('a')!.right, 2);
      expect(svc.practiceFor('a')!.wrong, 1);
      expect(svc.practiceFor('c'), isNull);
      expect(store.rows['a']!.answers, 3);

      final again = WordPracticeService(store);
      await again.init();
      expect(again.practiceFor('a')!.right, 2);
    });

    test('rows survive a round trip through the database map', () {
      final p = WordPractice(
        cardId: 'x',
        deckId: 'd',
        right: 4,
        wrong: 2,
        lastAt: DateTime(2026, 11, 7, 9),
      );
      final back = WordPractice.fromMap(p.toMap());
      expect(back.right, 4);
      expect(back.wrong, 2);
      expect(back.lastAt, p.lastAt);
    });

    test('the difficult-words service reports every answer to the tally', () {
      final seen = <String>[];
      final svc = DifficultWordsService(
        store: MemoryTroubleStore(),
        onAnswer: (deckId, cardId, correct, source) =>
            seen.add('$cardId:$correct:${source.name}'),
      );
      // A right answer to a word that was never missed still reaches the tally.
      svc.record(deckId: 'd', cardId: 'a', correct: true, source: AnswerSource.match);
      svc.record(deckId: 'd', cardId: 'a', correct: false, source: AnswerSource.flashcard);
      expect(seen, ['a:true:match', 'a:false:flashcard']);
    });

    test('a listener that throws does not stop the answer counting', () {
      final svc = DifficultWordsService(
        store: MemoryTroubleStore(),
        onAnswer: (_, __, ___, ____) => throw StateError('boom'),
      );
      svc.record(deckId: 'd', cardId: 'a', correct: false, source: AnswerSource.recall);
      final e = svc.record(
          deckId: 'd', cardId: 'a', correct: false, source: AnswerSource.recall);
      expect(e, TroubleEvent.added);
      expect(svc.isDifficult('a'), isTrue);
    });
  });

  group('quiz scoring and progress', () {
    final book = loadBook();
    final p = book.passages.first;

    test('scoreQuiz counts right answers and applies the pass mark', () {
      final right = [for (final q in p.questions) q.correctIndex];
      final all = scoreQuiz(p, right);
      expect(all.correct, p.questions.length);
      expect(all.perfect, isTrue);
      expect(all.passed, isTrue);

      final none = scoreQuiz(p, List<int?>.filled(p.questions.length, null));
      expect(none.correct, 0);
      expect(none.passed, isFalse);

      // Exactly at the mark passes; just under does not.
      expect(const QuizScore(correct: 7, total: 10).passed, isTrue);
      expect(const QuizScore(correct: 6, total: 10).passed, isFalse);
      expect(const QuizScore(correct: 0, total: 0).passed, isFalse);
    });

    test('a passage opens with its lesson', () {
      expect(passageUnlocked(p, {p.pairedLessonId: true}), isTrue);
      expect(passageUnlocked(p, {p.pairedLessonId: false}), isFalse);
      expect(passageUnlocked(p, const {}), isTrue);
    });

    test('the repository keeps the best score and spots a first pass', () async {
      final store = MemoryReadingProgressStore();
      final repo = ReadingRepository(
        store,
        loadAsset: (_) async => File(_readingsPath).readAsString(),
      );
      await repo.init(_readingsPath);
      expect(repo.bookFor('ru'), isNotNull);

      final fail = repo.record(
        passage: p,
        mode: ReadingMode.read,
        score: QuizScore(correct: 1, total: p.questions.length),
      );
      expect(fail.firstPass, isFalse);
      expect(fail.newBest, isTrue);
      expect(repo.passedCount('ru', ReadingMode.read), 0);

      final pass = repo.record(
        passage: p,
        mode: ReadingMode.read,
        score: QuizScore(correct: p.questions.length, total: p.questions.length),
      );
      expect(pass.firstPass, isTrue);
      expect(pass.progress.attempts, 2);
      expect(repo.passedCount('ru', ReadingMode.read), 1);
      // Listening is tracked separately.
      expect(repo.passedCount('ru', ReadingMode.listen), 0);

      final worse = repo.record(
        passage: p,
        mode: ReadingMode.read,
        score: QuizScore(correct: 0, total: p.questions.length),
      );
      expect(worse.firstPass, isFalse);
      expect(worse.newBest, isFalse);
      expect(worse.progress.bestScore, 1.0);

      // A fresh repository sees what was saved.
      final again = ReadingRepository(
        store,
        loadAsset: (_) async => File(_readingsPath).readAsString(),
      );
      await again.init(_readingsPath);
      expect(again.progressFor(p.id, ReadingMode.read).attempts, 3);
      expect(again.progressFor(p.id, ReadingMode.read).passed, isTrue);
    });

    test('a missing file switches the feature off without failing', () async {
      final repo = ReadingRepository(
        MemoryReadingProgressStore(),
        loadAsset: (_) async => throw StateError('no file'),
      );
      await repo.init('nope.json');
      expect(repo.bookFor('ru'), isNull);
      expect(repo.passedCount('ru', ReadingMode.read), 0);
    });

    test('progress rows round-trip through the database map', () {
      final r = ReadingProgress(
        passageId: 'ru_r01',
        mode: ReadingMode.listen,
        bestScore: 0.8,
        attempts: 3,
        lastAt: DateTime(2026, 11, 7, 10),
      );
      final back = ReadingProgress.fromMap(r.toMap());
      expect(back.mode, ReadingMode.listen);
      expect(back.bestScore, 0.8);
      expect(back.attempts, 3);
      expect(back.passed, isTrue);
    });
  });

  group('XP and trophies', () {
    test('XP: 8 to finish, 4 per right answer, 8 for a perfect score', () {
      expect(XpRules.reading(correct: 3, total: 5, firstPass: true), 8 + 12);
      expect(XpRules.reading(correct: 5, total: 5, firstPass: true), 8 + 20 + 8);
      // Repeats pay half, rounded up.
      expect(XpRules.reading(correct: 3, total: 5, firstPass: false), 10);
      expect(XpRules.reading(correct: 0, total: 5, firstPass: false), 4);
    });

    test('the event counts a pass once, in the right counter', () {
      final read = ProgressEvent.reading(
        listening: false,
        correct: 4,
        total: 5,
        passed: true,
        firstPass: true,
        deckId: 'ru_core',
      );
      expect(read.source, ProgressSource.reading);
      expect(read.increments, {'readings': 1});

      final heard = ProgressEvent.reading(
        listening: true,
        correct: 5,
        total: 5,
        passed: true,
        firstPass: true,
        deckId: 'ru_core',
      );
      expect(heard.increments, {'listenings': 1, 'reading_perfect': 1});

      final repeat = ProgressEvent.reading(
        listening: false,
        correct: 5,
        total: 5,
        passed: true,
        firstPass: false,
        deckId: 'ru_core',
      );
      expect(repeat.increments, isEmpty);

      final failed = ProgressEvent.reading(
        listening: false,
        correct: 1,
        total: 5,
        passed: false,
        firstPass: false,
        deckId: 'ru_core',
      );
      expect(failed.increments, isEmpty);
      expect(failed.xp, greaterThan(0));
    });

    test('the new trophies exist and use the counters the event writes', () {
      final metrics = TrophyCatalog.all.map((t) => t.metric).toSet();
      expect(metrics, containsAll(['readings', 'listenings', 'reading_perfect']));
    });

    test('the new source is stored by name and read back', () {
      expect(ProgressSource.values.map((s) => s.name), contains('reading'));
    });
  });
}

void _passageFileTests(_Lang lang) {
  group('passage file (${lang.code})', () {
    final raw = json.decode(File(lang.readings).readAsStringSync())
        as Map<String, dynamic>;
    final book = ReadingBook.fromJson(raw);
    final deck = json.decode(File(lang.deck).readAsStringSync())
        as Map<String, dynamic>;
    final lessons = json.decode(File(lang.lessons).readAsStringSync())
        as Map<String, dynamic>;
    final cardIds = {
      for (final c in deck['cards'] as List) (c as Map<String, dynamic>)['id'] as String,
    };
    final lessonOrder = <String, int>{};
    final unitOf = <String, String>{};
    for (final u in lessons['units'] as List) {
      final unit = u as Map<String, dynamic>;
      for (final l in unit['lessons'] as List) {
        final id = (l as Map<String, dynamic>)['id'] as String;
        lessonOrder[id] = lessonOrder.length;
        unitOf[id] = unit['id'] as String;
      }
    }

    test('is for the right language and deck', () {
      expect(book.language, lang.code);
      expect(book.deckId, deck['id']);
      expect(book.passages.length, greaterThanOrEqualTo(lang.minPassages));
    });

    test('ids and titles are unique', () {
      final ids = book.passages.map((p) => p.id).toList();
      expect(ids.toSet().length, ids.length);
      final titles = book.passages.map((p) => p.title).toList();
      expect(titles.toSet().length, titles.length);
    });

    test('every passage is paired with a real lesson', () {
      for (final p in book.passages) {
        expect(lessonOrder.containsKey(p.pairedLessonId), isTrue, reason: p.id);
      }
    });

    test('every passage says whether it is read or heard', () {
      for (final p in raw['passages'] as List) {
        final m = (p as Map<String, dynamic>)['mode'];
        expect(m == 'read' || m == 'listen', isTrue, reason: p['id'] as String);
      }
      expect(book.passagesFor(ReadingMode.read), isNotEmpty);
      expect(book.passagesFor(ReadingMode.listen), isNotEmpty);
    });

    test('what is read is never what is heard', () {
      // The two sets share no sentence, so one cannot be used to pass the other.
      final read = {
        for (final p in book.passagesFor(ReadingMode.read))
          for (final s in p.sentences) s.ru,
      };
      for (final p in book.passagesFor(ReadingMode.listen)) {
        for (final s in p.sentences) {
          expect(read.contains(s.ru), isFalse, reason: '${p.id}: ${s.ru}');
        }
      }
      // And no two passages have the same questions.
      final prompts = <String>{};
      for (final p in book.passages) {
        for (final q in p.questions) {
          expect(prompts.add('${p.id}|${q.prompt}'), isTrue);
        }
      }
    });

    test('every unit has some reading and some listening', () {
      final read = <String, int>{};
      final heard = <String, int>{};
      for (final p in book.passages) {
        final u = unitOf[p.pairedLessonId]!;
        final m = p.isListening ? heard : read;
        m[u] = (m[u] ?? 0) + 1;
      }
      final units = {for (final p in book.passages) unitOf[p.pairedLessonId]!};
      for (final u in units) {
        expect(read[u] ?? 0, greaterThanOrEqualTo(1), reason: '$u has nothing to read');
        expect(heard[u] ?? 0, greaterThanOrEqualTo(1), reason: '$u has nothing to hear');
      }
    });

    test('passages get no easier as the lessons go on, and cover every level', () {
      var lastLesson = -1;
      var lastLevel = 0;
      for (final p in book.passages) {
        final at = lessonOrder[p.pairedLessonId]!;
        expect(at, greaterThanOrEqualTo(lastLesson), reason: '${p.id} is out of lesson order');
        expect(p.level, greaterThanOrEqualTo(lastLevel), reason: p.id);
        lastLesson = at;
        lastLevel = p.level;
      }
      expect(book.passages.map((p) => p.level).toSet(), {for (var l = 1; l <= ReadingRules.levels; l++) l});
    });

    test('they get longer: the average length rises with the level', () {
      final byLevel = <int, List<int>>{};
      for (final p in book.passages) {
        byLevel.putIfAbsent(p.level, () => []).add(p.wordCount);
      }
      double avg(int l) => byLevel[l]!.reduce((a, b) => a + b) / byLevel[l]!.length;
      for (var l = 2; l <= ReadingRules.levels; l++) {
        expect(avg(l), greaterThan(avg(l - 1)), reason: 'level $l');
      }
    });

    test('tokens rebuild each sentence, and the word count is right', () {
      for (final p in book.passages) {
        expect(p.words.length, p.wordCount, reason: p.id);
        for (final s in p.sentences) {
          expect(joinTokens(s.tokens.map((t) => t.text)), s.ru, reason: p.id);
          expect(s.en.trim(), isNotEmpty, reason: p.id);
        }
      }
    });

    test('every word resolves in the lexicon, and every card id is in the deck', () {
      for (final p in book.passages) {
        for (final t in p.words) {
          final e = book.entry(t.key);
          expect(e, isNotNull, reason: '${p.id}: ${t.text}');
          expect(e!.gloss, isNotEmpty, reason: '${p.id}: ${t.text}');
          final id = e.cardId;
          if (id != null) expect(cardIds.contains(id), isTrue, reason: '${p.id}: $id');
        }
      }
      for (final e in book.lexicon.values) {
        final id = e.cardId;
        if (id != null) expect(cardIds.contains(id), isTrue, reason: id);
      }
    });

    test('questions are well formed', () {
      for (final p in book.passages) {
        expect(p.questions.length, inInclusiveRange(2, 7), reason: p.id);
        for (final q in p.questions) {
          expect(q.options.length, greaterThanOrEqualTo(3), reason: p.id);
          expect(q.correctIndex, inInclusiveRange(0, q.options.length - 1), reason: p.id);
          expect(q.options.toSet().length, q.options.length, reason: '${p.id}: ${q.prompt}');
          expect(q.why, isNotEmpty, reason: '${p.id}: ${q.prompt}');
        }
      }
    });

    test('the correct answer is not always in the same place', () {
      final counts = List<int>.filled(4, 0);
      var total = 0;
      for (final p in book.passages) {
        for (final q in p.questions) {
          if (q.options.length == 4) {
            counts[q.correctIndex]++;
            total++;
          }
        }
      }
      for (final n in counts) {
        expect(n / total, lessThan(0.4));
      }
    });

    test('the file declares what the loader reads', () {
      expect(raw['version'], 1);
    });
  });
}

