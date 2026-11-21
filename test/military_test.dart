import 'dart:io';
import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/military/military_models.dart';
import 'package:lingotopia/military/military_quiz.dart';
import 'package:lingotopia/military/military_repository.dart';
import 'package:lingotopia/progress/progress_models.dart';
import 'package:lingotopia/progress/xp_rules.dart';
import 'package:shared_preferences/shared_preferences.dart';

MilitaryData load() =>
    MilitaryData.parse(File('assets/military/ru_military.json').readAsStringSync());

void main() {
  group('data file', () {
    final data = load();

    test('is large and every section is non-empty', () {
      expect(data.sections.length, greaterThanOrEqualTo(20));
      expect(data.termCount, greaterThan(4000));
      expect(data.acronyms.length, greaterThan(400));
      for (final s in data.sections) {
        expect(s.count, greaterThan(20), reason: s.id);
        expect(s.groups, isNotEmpty, reason: s.id);
      }
    });

    test('asked-for sections exist', () {
      for (final id in ['infantry', 'artillery', 'airdefense', 'radio', 'comms']) {
        expect(data.section(id), isNotNull, reason: id);
      }
    });

    test('every term has Russian and English, and no stray apostrophes', () {
      for (final s in data.sections) {
        for (final t in s.terms) {
          expect(t.ru.trim(), isNotEmpty, reason: s.id);
          expect(t.en.trim(), isNotEmpty, reason: t.ru);
          expect(t.ru.contains("'"), isFalse, reason: t.ru);
          expect(t.plain.contains('́'), isFalse);
        }
      }
    });

    test('keys are unique', () {
      final termKeys = <String>{};
      for (final s in data.sections) {
        for (final t in s.terms) {
          // The same Russian with the same meaning may appear in two sections;
          // within one section it never does.
          expect(termKeys.add('${s.id}:${t.key}'), isTrue, reason: t.ru);
        }
      }
      final acr = data.acronyms.map((a) => a.key).toSet();
      expect(acr.length, data.acronyms.length);
    });

    test('every acronym says what it stands for and how it is said', () {
      for (final a in data.acronyms) {
        expect(a.abbr, isNotEmpty);
        expect(a.full.trim(), isNotEmpty, reason: a.abbr);
        expect(a.en.trim(), isNotEmpty, reason: a.abbr);
        expect(a.reading.trim(), isNotEmpty, reason: a.abbr);
        expect(a.speakable.contains('-'), isFalse, reason: a.abbr);
      }
    });

    test('well-known acronyms are present with the right expansion', () {
      String full(String abbr) =>
          data.acronyms.firstWhere((a) => a.abbr == abbr).plainFull;
      expect(full('ВДВ'), 'Воздушно-десантные войска');
      expect(full('БМП'), 'боевая машина пехоты');
      expect(full('РЭБ'), 'радиоэлектронная борьба');
      expect(full('НАТО'), 'Организация Североатлантического договора');
    });
  });

  group('text helpers', () {
    test('stripStress removes only the accent', () {
      expect(stripStress('артилле́рия'), 'артиллерия');
      expect(searchForm('Ёж Ста́вка'), 'еж ставка');
    });

    test('fnv1a is stable', () {
      expect(fnv1a(''), 0x811c9dc5);
      expect(fnv1a('a'), 0xe40c292c);
    });
  });

  group('search', () {
    final data = load();

    test('finds by abbreviation first', () {
      final hits = data.search('бмп');
      expect(hits, isNotEmpty);
      expect(hits.first.acronym?.abbr, 'БМП');
    });

    test('ignores stress marks and ё/е', () {
      final a = data.search('артиллерия');
      final b = data.search('артилле́рия');
      expect(a, isNotEmpty);
      expect(a.length, b.length);
    });

    test('works in English and returns nothing for an empty query', () {
      expect(data.search('howitzer'), isNotEmpty);
      expect(data.search('   '), isEmpty);
    });
  });

  group('quiz', () {
    final data = load();
    final pool = data.section('artillery')!.terms;

    test('every question has four different options and a valid answer', () {
      final qs = MilQuizBuilder.terms(pool, (_) => false, rng: Random(7));
      expect(qs.length, 10);
      for (final q in qs) {
        expect(q.options.length, 4);
        expect(q.options.toSet().length, 4);
        expect(q.correct, inInclusiveRange(0, 3));
      }
    });

    test('terms not yet known are asked first', () {
      final known = {for (final t in pool.take(pool.length - 5)) t.key};
      final qs = MilQuizBuilder.terms(pool, known.contains, count: 5, rng: Random(3));
      expect(qs.every((q) => !q.wasKnown), isTrue);
    });

    test('acronym questions can be built from the real list', () {
      final qs = MilQuizBuilder.acronyms(data.acronyms, (_) => false, rng: Random(5));
      expect(qs.length, 10);
      for (final q in qs) {
        expect(q.options.toSet().length, 4);
      }
    });

    test('a pool that is too small yields no question instead of a bad one', () {
      final tiny = pool.take(3).toList();
      expect(MilQuizBuilder.terms(tiny, (_) => false), isEmpty);
    });
  });

  group('XP', () {
    test('a term still being learned pays more than a known one', () {
      final fresh = XpRules.militaryQuiz(newCorrect: 10, knownCorrect: 0, total: 10);
      final old = XpRules.militaryQuiz(newCorrect: 0, knownCorrect: 10, total: 10);
      expect(fresh, 40);
      expect(old, 20);
      expect(fresh, greaterThan(old));
    });

    test('finishing pays and a perfect run pays more', () {
      expect(XpRules.militaryQuiz(newCorrect: 0, knownCorrect: 0, total: 10), 5);
      expect(XpRules.militaryQuiz(newCorrect: 3, knownCorrect: 2, total: 10), 16);
      expect(XpRules.militaryQuiz(newCorrect: 0, knownCorrect: 0, total: 0), 0);
    });

    test('flashcards pay only for new terms', () {
      expect(XpRules.militaryCard(known: false), 2);
      expect(XpRules.militaryCard(known: true), 0);
    });

    test('the events carry source, XP and counters', () {
      final e = ProgressEvent.militaryQuiz(
          newCorrect: 4, knownCorrect: 1, total: 10, deckId: 'ru_core');
      expect(e.source, ProgressSource.military);
      expect(e.xp, 3 * 4 + 1 + 5);
      expect(e.increments['military_quizzes'], 1);
      expect(e.increments['military_terms_learned'], 4);

      final none = ProgressEvent.militaryQuiz(
          newCorrect: 0, knownCorrect: 2, total: 10, deckId: 'ru_core');
      expect(none.increments.containsKey('military_terms_learned'), isFalse);

      final card = ProgressEvent.militaryCard(deckId: 'ru_core');
      expect(card.xp, 2);
      expect(card.increments['military_terms_learned'], 1);
    });

    test('the source is stored by name', () {
      expect(ProgressSource.values.map((s) => s.name), contains('military'));
    });
  });

  group('MilitaryRepository', () {
    setUp(() => SharedPreferences.setMockInitialValues({}));

    test('only Russian has the section', () {
      expect(MilitaryRepository.supports('ru'), isTrue);
      expect(MilitaryRepository.supports('es'), isFalse);
    });

    test('known terms are remembered across restarts', () async {
      final prefs = await SharedPreferences.getInstance();
      final repo = MilitaryRepository(prefs);
      expect(await repo.setKnown(['a', 'b'], true), 2);
      expect(await repo.setKnown(['a'], true), 0);
      expect(repo.isKnown('a'), isTrue);

      final again = MilitaryRepository(prefs);
      expect(again.isKnown('b'), isTrue);
      expect(again.knownAmong(['a', 'b', 'c']), 2);

      await again.setKnown(['a'], false);
      expect(MilitaryRepository(prefs).isKnown('a'), isFalse);
    });

    test('loads the real data through the loader', () async {
      final prefs = await SharedPreferences.getInstance();
      final repo = MilitaryRepository(
        prefs,
        loader: (path) async => File(path).readAsString(),
      );
      final data = await repo.data();
      expect(data, isNotNull);
      expect(data!.termCount, greaterThan(4000));
      expect(identical(await repo.data(), data), isTrue);
    });

    test('a missing file just yields null', () async {
      final prefs = await SharedPreferences.getInstance();
      final repo = MilitaryRepository(prefs, loader: (_) async => throw 'gone');
      expect(await repo.data(), isNull);
    });
  });
}
