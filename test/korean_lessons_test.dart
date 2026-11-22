import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/lessons/lesson_models.dart';

/// Structure of the Korean lessons (assets/lessons/ko_lessons.json). The build script
/// (tools/lessons/build_ko_lessons.py) already checks the pronunciation engine against the
/// book's printed pronunciations, every romanization against the deck, and that every spoken
/// text is Hangul only; these tests make sure the file the app loads is shaped as the lesson
/// player expects.
void main() {
  final raw = jsonDecode(File('assets/lessons/ko_lessons.json').readAsStringSync())
      as Map<String, dynamic>;
  final course = LessonCourse.fromJson(raw);
  final deck = jsonDecode(File('assets/decks/korean_core.json').readAsStringSync())
      as Map<String, dynamic>;

  test('the course belongs to the Korean deck', () {
    expect(course.language, 'ko');
    expect(course.deckId, deck['id']);
  });

  test('lesson ids are ko_01.. in order and unique', () {
    final ids = course.allLessons.map((l) => l.id).toList();
    expect(ids.toSet().length, ids.length);
    for (var i = 0; i < ids.length; i++) {
      expect(ids[i], 'ko_${(i + 1).toString().padLeft(2, '0')}');
    }
    expect(ids.length, greaterThanOrEqualTo(612));
  });

  test('every lesson teaches something and asks enough questions', () {
    for (final l in course.allLessons) {
      expect(l.explanations, isNotEmpty, reason: l.id);
      expect(l.exercises.length, greaterThanOrEqualTo(6), reason: l.id);
    }
  });

  test('every exercise has a valid answer and distinct options', () {
    for (final l in course.allLessons) {
      for (final e in l.exercises) {
        expect(e.options.length, inInclusiveRange(2, 6), reason: '${l.id}/${e.id}');
        expect(e.correctIndex, inInclusiveRange(0, e.options.length - 1), reason: '${l.id}/${e.id}');
        expect(e.options.toSet().length, e.options.length, reason: '${l.id}/${e.id}');
        if (e.type == ExerciseType.fillBlank) {
          expect('___'.allMatches(e.prompt).length, 1, reason: '${l.id}/${e.id}');
        }
      }
    }
  });

  test('no authoring markup is left in the text', () {
    // the Hangul in the file is NFC syllables and compatibility jamo, never conjoining jamo
    final conjoining = RegExp(r'[\u1100-\u11FF\uA960-\uA97F\uD7B0-\uD7FF]');
    void walk(Object? o, String path) {
      if (o is String) {
        expect(o.contains('[['), isFalse, reason: path);
        expect(o.contains(']]'), isFalse, reason: path);
        expect(conjoining.hasMatch(o), isFalse, reason: '$path: $o');
      } else if (o is List) {
        for (var i = 0; i < o.length; i++) {
          walk(o[i], '$path[$i]');
        }
      } else if (o is Map) {
        o.forEach((k, v) => walk(v, '$path.$k'));
      }
    }

    walk(raw, 'ko');
  });

  test('tables that name speakable columns point at real columns', () {
    for (final l in course.allLessons) {
      for (final x in l.explanations) {
        for (final t in x.tables) {
          for (final c in t.speakCols ?? const <int>[]) {
            expect(c, lessThan(t.headers.length), reason: '${l.id}: ${x.title}');
            for (final r in t.rows) {
              expect(r.length, t.headers.length, reason: '${l.id}: ${x.title}');
            }
          }
        }
      }
    }
  });

  test('spoken table cells and example lines are Hangul only', () {
    final hangul = RegExp(r'[가-힣ㄱ-ㅣ]');
    final latin = RegExp(r'[A-Za-z0-9]');
    for (final l in course.allLessons) {
      for (final x in l.explanations) {
        for (final t in x.tables) {
          for (final c in t.speakCols ?? const <int>[]) {
            for (final r in t.rows) {
              expect(hangul.hasMatch(r[c]) && !latin.hasMatch(r[c]), isTrue,
                  reason: '${l.id}: ${r[c]}');
            }
          }
        }
        for (final e in x.examples) {
          expect(hangul.hasMatch(e.text) && !latin.hasMatch(e.text), isTrue,
              reason: '${l.id}: ${e.text}');
        }
      }
    }
  });
}
