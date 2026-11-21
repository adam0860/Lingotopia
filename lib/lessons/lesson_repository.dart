import 'dart:convert';

import 'package:flutter/services.dart' show rootBundle;
import 'package:sqflite/sqflite.dart';

import '../data/database.dart';
import '../data/deck_repository.dart';
import 'lesson_models.dart';

/// Loads a language's lesson content, decides which lessons are unlocked
/// against that language's flashcard progress, and records attempts.
class LessonRepository {
  LessonRepository(this._appDb, this._decks);

  final AppDatabase _appDb;
  final DeckRepository _decks;
  Database get _db => _appDb.db;

  final Map<String, LessonCourse> _courses = {};

  Future<LessonCourse?> loadCourse(String assetPath) async {
    try {
      final raw = await rootBundle.loadString(assetPath);
      final course = LessonCourse.fromJson(json.decode(raw) as Map<String, dynamic>);
      _courses[course.language] = course;
      return course;
    } catch (_) {
      // No lesson content for this language yet. Callers treat null as
      // "Lessons not available here" rather than crashing the home screen.
      return null;
    }
  }

  LessonCourse? courseFor(String language) => _courses[language];

  /// Fraction of [lemmas] the learner has reviewed at least once in the
  /// paired deck. "Reviewed once" means it has a row in card_state at all —
  /// SchedulingState.fresh cards (never shown) have none. This deliberately
  /// does not require mastery: the lesson is allowed to be part of how a
  /// word gets learned, not a reward for already knowing it.
  Future<double> _exposureFraction(String deckId, List<String> lemmas) async {
    if (lemmas.isEmpty) return 1.0;

    // Card ids are "{lang}_{rank}_{slug}" or "{lang}_{rank}", not the bare
    // lemma, so match by the deck's own card list rather than guessing the
    // id format here.
    final deck = _decks.deck(deckId);
    if (deck == null) return 0.0;

    final idsForLemmas = <String>{
      for (final c in deck.cards)
        if (lemmas.contains(c.lemma)) c.id,
    };
    if (idsForLemmas.isEmpty) return 0.0;

    final states = await _decks.allStates(deckId);
    final seen = idsForLemmas.where((id) => states.containsKey(id)).length;
    return seen / idsForLemmas.length;
  }

  Future<bool> isUnlocked(String deckId, Lesson lesson) async {
    final frac = await _exposureFraction(deckId, lesson.requiredLemmas);
    return frac >= lesson.unlockThreshold;
  }

  /// Unlock state for every lesson in a course, computed in one pass so the
  /// lesson list screen doesn't issue a query per lesson.
  Future<Map<String, bool>> unlockedMap(LessonCourse course) async {
    final states = await _decks.allStates(course.deckId);
    final deck = _decks.deck(course.deckId);
    if (deck == null) return {for (final l in course.allLessons) l.id: false};

    final lemmaToId = <String, String>{
      for (final c in deck.cards) c.lemma: c.id,
    };

    final out = <String, bool>{};
    for (final lesson in course.allLessons) {
      if (lesson.requiredLemmas.isEmpty) {
        out[lesson.id] = true;
        continue;
      }
      var seen = 0;
      var total = 0;
      for (final lemma in lesson.requiredLemmas) {
        final id = lemmaToId[lemma];
        if (id == null) continue; // Word not in this deck; don't count it.
        total++;
        if (states.containsKey(id)) seen++;
      }
      out[lesson.id] = total == 0 ? true : (seen / total) >= lesson.unlockThreshold;
    }
    return out;
  }

  Future<LessonProgress> progressFor(String lessonId) async {
    final rows = await _db.query(
      'lesson_progress',
      where: 'lesson_id = ?',
      whereArgs: [lessonId],
    );
    return rows.isEmpty
        ? LessonProgress.empty(lessonId)
        : LessonProgress.fromMap(rows.first);
  }

  Future<Map<String, LessonProgress>> allProgress() async {
    final rows = await _db.query('lesson_progress');
    return {
      for (final r in rows)
        r['lesson_id'] as String: LessonProgress.fromMap(r),
    };
  }

  /// Record one completed attempt. [score] is the fraction of exercises
  /// answered correctly on the first try within this attempt.
  Future<LessonProgress> recordAttempt({
    required String lessonId,
    required double score,
    DateTime? at,
  }) async {
    final now = at ?? DateTime.now();
    final prior = await progressFor(lessonId);

    final next = LessonProgress(
      lessonId: lessonId,
      completed: prior.completed || score >= 0.8,
      bestScore: score > prior.bestScore ? score : prior.bestScore,
      attempts: prior.attempts + 1,
      lastAttempt: now,
    );

    await _db.insert(
      'lesson_progress',
      next.toMap(),
      conflictAlgorithm: ConflictAlgorithm.replace,
    );
    return next;
  }
}
