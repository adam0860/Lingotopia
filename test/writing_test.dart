import 'dart:io';
import 'dart:ui' show Offset;

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/progress/progress_models.dart';
import 'package:lingotopia/progress/xp_rules.dart';
import 'package:lingotopia/writing/stroke_matcher.dart';
import 'package:lingotopia/writing/writing_models.dart';
import 'package:lingotopia/writing/writing_repository.dart';
import 'package:shared_preferences/shared_preferences.dart';

List<Offset> line(double x1, double y1, double x2, double y2, [int n = 20]) => [
      for (var i = 0; i < n; i++)
        Offset(x1 + (x2 - x1) * i / (n - 1), y1 + (y2 - y1) * i / (n - 1)),
    ];

StrokeSet load(String lang) =>
    StrokeSet.parse(File('assets/writing/${lang}_strokes.json').readAsStringSync());

void main() {
  group('StrokeMatcher', () {
    final horizontal = line(200, 500, 800, 500);

    test('accepts a slightly shifted copy', () {
      final user = line(230, 520, 790, 480, 40);
      expect(StrokeMatcher.match(user: user, target: horizontal).ok, isTrue);
    });

    test('rejects a stroke drawn the wrong way', () {
      final user = line(800, 500, 200, 500);
      final r = StrokeMatcher.match(user: user, target: horizontal);
      expect(r.ok, isFalse);
      expect(r.issue, MatchIssue.wrongDirection);
    });

    test('rejects a tiny scratch', () {
      final user = line(450, 500, 520, 500);
      final r = StrokeMatcher.match(user: user, target: horizontal);
      expect(r.issue, MatchIssue.tooShort);
    });

    test('rejects a stroke in the wrong place', () {
      final user = line(200, 150, 800, 150);
      final r = StrokeMatcher.match(user: user, target: horizontal);
      expect(r.issue, MatchIssue.offTarget);
    });

    test('reports a stroke that belongs later as wrong order', () {
      final vertical = line(500, 150, 500, 850);
      final r = StrokeMatcher.match(
        user: vertical,
        target: horizontal,
        later: [vertical],
      );
      expect(r.issue, MatchIssue.wrongOrder);
    });

    test('dots only need to be in the right place', () {
      final dot = [const Offset(700, 300), const Offset(712, 318)];
      expect(
        StrokeMatcher.match(user: [const Offset(690, 310)], target: dot).ok,
        isTrue,
      );
      expect(
        StrokeMatcher.match(user: [const Offset(100, 900)], target: dot).ok,
        isFalse,
      );
    });

    test('leniency forgives a rough stroke', () {
      final rough = line(200, 700, 800, 700); // 200 units too low
      expect(StrokeMatcher.match(user: rough, target: horizontal).ok, isFalse);
      final near = line(200, 640, 800, 640);
      expect(
          StrokeMatcher.match(user: near, target: horizontal, leniency: 1.3).ok,
          isTrue);
    });

    test('resample keeps ends and count', () {
      final r = StrokeMatcher.resample(line(0, 0, 100, 0, 7), 24);
      expect(r.length, 24);
      expect(r.first, const Offset(0, 0));
      expect(r.last, const Offset(100, 0));
      expect(r[12].dx, closeTo(52, 3));
    });

    test('stars', () {
      expect(StrokeMatcher.starsFor(misses: 0, hints: 0), 3);
      expect(StrokeMatcher.starsFor(misses: 2, hints: 1), 2);
      expect(StrokeMatcher.starsFor(misses: 9, hints: 0), 1);
      expect(StrokeMatcher.starsFor(misses: 0, hints: 3), 1);
    });
  });

  group('stroke files', () {
    final ja = load('ja');
    final zh = load('zh');

    test('known stroke counts', () {
      expect(ja['人']!.strokeCount, 2);
      expect(ja['日']!.strokeCount, 4);
      expect(ja['本']!.strokeCount, 5);
      expect(ja['語']!.strokeCount, 14);
      expect(ja['あ']!.strokeCount, 3);
      expect(zh['你']!.strokeCount, 7);
      expect(zh['好']!.strokeCount, 6);
    });

    test('kana come first in Japanese, kanji after', () {
      final order = ja.order;
      final firstKanji = order.indexWhere((c) => !StrokeChar.isKanaChar(c));
      expect(firstKanji, greaterThan(100));
      expect(order.take(firstKanji).every(StrokeChar.isKanaChar), isTrue);
      expect(order.skip(firstKanji).any(StrokeChar.isKanaChar), isFalse);
    });

    test('every point is on the grid and every stroke can be drawn', () {
      for (final set in [ja, zh]) {
        for (final ch in set.chars.values) {
          expect(ch.strokes, isNotEmpty, reason: ch.char);
          for (final s in ch.strokes) {
            expect(s.length, greaterThanOrEqualTo(2), reason: ch.char);
            for (final p in s) {
              expect(p.dx, inInclusiveRange(0, 1000), reason: ch.char);
              expect(p.dy, inInclusiveRange(0, 1000), reason: ch.char);
            }
          }
        }
      }
    });

    test('each model stroke matches itself', () {
      for (final set in [ja, zh]) {
        for (final ch in set.chars.values.take(300)) {
          for (final s in ch.strokes) {
            expect(StrokeMatcher.match(user: s, target: s).ok, isTrue,
                reason: ch.char);
          }
        }
      }
    });
  });

  group('WritingRepository progress', () {
    test('keeps the best stars and counts runs, and survives a restart', () async {
      SharedPreferences.setMockInitialValues({});
      final prefs = await SharedPreferences.getInstance();
      final repo = WritingRepository(prefs);

      expect(repo.progressOf('ja', '人').runs, 0);
      await repo.recordFinished('ja', '人'); // traced
      expect(repo.progressOf('ja', '人').stars, 0);
      expect(repo.progressOf('ja', '人').runs, 1);

      await repo.recordFinished('ja', '人', stars: 3);
      await repo.recordFinished('ja', '人', stars: 1);
      expect(repo.progressOf('ja', '人').stars, 3);
      expect(repo.progressOf('ja', '人').runs, 3);
      expect(repo.mastered('ja'), 1);
      expect(repo.mastered('zh'), 0);

      final again = WritingRepository(prefs);
      expect(again.progressOf('ja', '人').stars, 3);
    });

    test('only Japanese and Chinese have stroke data', () {
      expect(WritingRepository.supports('ja'), isTrue);
      expect(WritingRepository.supports('zh'), isTrue);
      expect(WritingRepository.supports('ru'), isFalse);
    });
  });

  group('Writing XP', () {
    int xp({
      bool write = true,
      int stars = 3,
      int strokes = 5,
      bool known = false,
      bool firstEver = false,
    }) =>
        XpRules.writing(
            write: write,
            stars: stars,
            strokes: strokes,
            known: known,
            firstEver: firstEver);

    test('learning pays in full', () {
      expect(xp(write: false, stars: 0), 4); // trace, 5 strokes
      expect(xp(stars: 3), 10); // 6 + 4
      expect(xp(stars: 2), 8);
      expect(xp(stars: 1), 6);
      expect(xp(stars: 3, strokes: 14), 12); // +2 for a long character
      expect(xp(write: false, stars: 0, firstEver: true), 7); // +3 first time
    });

    test('a known character pays less, whatever the mode', () {
      expect(xp(write: false, stars: 0, known: true), 1);
      expect(xp(stars: 1, known: true), 2);
      expect(xp(stars: 3, known: true), 3);
      for (final stars in [1, 2, 3]) {
        expect(xp(stars: stars, known: true), lessThan(xp(stars: stars)));
      }
    });

    test('the event carries the XP, the source and the counters', () {
      final e = ProgressEvent.writing(
          write: true,
          stars: 3,
          strokes: 5,
          known: false,
          firstEver: false,
          deckId: 'ja_core');
      expect(e.source, ProgressSource.writing);
      expect(e.xp, 10);
      expect(e.increments['characters_practised'], 1);
      expect(e.increments['characters_learned'], 1);

      final again = ProgressEvent.writing(
          write: true,
          stars: 3,
          strokes: 5,
          known: true,
          firstEver: false,
          deckId: 'ja_core');
      expect(again.increments.containsKey('characters_learned'), isFalse);
    });
  });

  group('KanjiReading', () {
    final readings = KanjiReading.parse(File('assets/writing/ja_readings.json').readAsStringSync());

    test('the common kanji have on and kun readings', () {
      expect(readings['人']!.on, contains('ジン'));
      expect(readings['人']!.kun, contains('ひと'));
      expect(readings['生']!.kun.first, 'い.きる');
    });

    test('every kanji with strokes has a reading', () {
      final set = load('ja');
      final missing = [
        for (final ch in set.order)
          if (!set[ch]!.isKana && (readings[ch]?.isEmpty ?? true)) ch
      ];
      expect(missing, isEmpty);
    });

    test('readings are kana only and the voice text has no markup', () {
      final kana = RegExp(r'^[\u3041-\u3096\u30A1-\u30FA\u30FC.]+$');
      for (final e in readings.entries) {
        for (final r in [...e.value.on, ...e.value.kun]) {
          expect(kana.hasMatch(r), isTrue, reason: '${e.key} $r');
          expect(KanjiReading.spoken(r).contains('.'), isFalse);
        }
      }
      expect(KanjiReading.shown('い.きる'), 'い\u30FBきる');
      expect(KanjiReading.spoken('い.きる'), 'いきる');
    });

    test('the primary reading is the first kun, else the first on', () {
      expect(readings['人']!.primary, 'ひと');
      expect(const KanjiReading(on: ['ニチ']).primary, 'ニチ');
      expect(const KanjiReading().primary, isNull);
    });
  });
}
