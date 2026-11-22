import 'dart:convert';
import 'dart:io';

import 'package:flutter_test/flutter_test.dart';
import 'package:lingotopia/lessons/lesson_models.dart';

/// Structure of the Tagalog lessons (assets/lessons/tl_lessons.json). The build script
/// (tools/lessons/build_tl_lessons.py) already checks that every spoken text is plain Tagalog
/// (letters, spaces and basic punctuation, no digits or abbreviations); these tests make sure the
/// file the app loads is shaped as the lesson player expects.
void main() {
  final raw = jsonDecode(File('assets/lessons/tl_lessons.json').readAsStringSync())
      as Map<String, dynamic>;
  final course = LessonCourse.fromJson(raw);
  final spoken = RegExp(r"^[A-Za-zÑñ\s.,?!\-'’]*$");

  test('the course belongs to the Tagalog deck', () {
    expect(course.language, 'tl');
    expect(course.deckId, 'tl_core');
  });

  test('lesson ids are tl_01.. in order and unique', () {
    final ids = course.allLessons.map((l) => l.id).toList();
    expect(ids.toSet().length, ids.length);
    for (var i = 0; i < ids.length; i++) {
      expect(ids[i], 'tl_${(i + 1).toString().padLeft(2, '0')}');
    }
    expect(ids.length, greaterThanOrEqualTo(394));
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
    void walk(Object? o, String path) {
      if (o is String) {
        expect(o.contains('[['), isFalse, reason: path);
        expect(o.contains(']]'), isFalse, reason: path);
      } else if (o is List) {
        for (var i = 0; i < o.length; i++) {
          walk(o[i], '$path[$i]');
        }
      } else if (o is Map) {
        o.forEach((k, v) => walk(v, '$path.$k'));
      }
    }

    walk(raw, 'tl');
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

  test('spoken table cells and example lines are plain Tagalog', () {
    for (final l in course.allLessons) {
      for (final x in l.explanations) {
        for (final t in x.tables) {
          for (final c in t.speakCols ?? const <int>[]) {
            for (final r in t.rows) {
              expect(spoken.hasMatch(r[c]), isTrue, reason: '${l.id}: ${r[c]}');
            }
          }
        }
        for (final e in x.examples) {
          expect(spoken.hasMatch(e.text), isTrue, reason: '${l.id}: ${e.text}');
        }
      }
    }
  });
}
