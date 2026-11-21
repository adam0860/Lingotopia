import 'dart:convert';

import 'package:flutter/foundation.dart' show compute;
import 'package:flutter/services.dart' show rootBundle;
import 'package:sqflite/sqflite.dart';

import '../difficult/difficult_pool.dart';
import '../srs/scheduler.dart';
import 'database.dart';
import 'models.dart';

/// Parses a deck file. Top-level so [compute] can run it on a background
/// isolate: a 10,000-card deck is several megabytes of JSON, and decoding it
/// on the UI thread would freeze the loading animation on a phone.
Deck _parseDeck(String raw) =>
    Deck.fromJson(json.decode(raw) as Map<String, dynamic>);

/// Owns deck content (from bundled assets) and learner progress (from SQLite),
/// and joins the two into a review queue.
class DeckRepository {
  DeckRepository(this._appDb);

  final AppDatabase _appDb;
  Database get _db => _appDb.db;

  final Map<String, Deck> _decks = {};

  /// How many cards the learner has never seen may enter the queue per day.
  int newCardsPerDay = 20;

  Future<Deck> loadDeck(String assetPath) async {
    final raw = await rootBundle.loadString(assetPath);
    final deck = await compute(_parseDeck, raw);
    _decks[deck.id] = deck;
    return deck;
  }

  Deck? deck(String id) => _decks[id];

  Future<Map<String, SchedulingState>> _statesFor(String deckId) async {
    final rows = await _db.query(
      'card_state',
      where: 'deck_id = ? AND suspended = 0',
      whereArgs: [deckId],
    );
    return {
      for (final r in rows) r['card_id'] as String: SchedulingState.fromMap(r),
    };
  }

  Future<DeckStats> stats(Deck deck, {DateTime? at}) async {
    final now = at ?? DateTime.now();
    final states = await _statesFor(deck.id);

    var learning = 0;
    var due = 0;
    for (final s in states.values) {
      final isDue = s.due != null && !s.due!.isAfter(now);
      if (s.phase == CardPhase.learning || s.phase == CardPhase.relearning) {
        if (isDue) learning++;
      } else if (s.phase == CardPhase.review && isDue) {
        due++;
      }
    }

    return DeckStats(
      total: deck.cards.length,
      newCards: deck.cards.length - states.length,
      learning: learning,
      dueForReview: due,
    );
  }

  /// Build today's queue.
  ///
  /// Order: anything overdue first (most overdue leads), then learning-step
  /// cards whose timer has elapsed, then new cards in teaching-rank order up
  /// to [newCardsPerDay] minus however many were already introduced today.
  ///
  /// [focusIds] are the learner's difficult words. When given, those lead
  /// their group (overdue, learning, new), and up to [extraFocus] of them that
  /// are not due yet are added at the end as extra practice. Passing none
  /// leaves the queue exactly as scheduled.
  Future<List<ReviewItem>> buildQueue(
    Deck deck, {
    DateTime? at,
    Set<String> focusIds = const {},
    int extraFocus = 0,
  }) async {
    final now = at ?? DateTime.now();
    final states = await _statesFor(deck.id);

    final review = <ReviewItem>[];
    final learning = <ReviewItem>[];
    final fresh = <ReviewItem>[];
    final notDueFocus = <ReviewItem>[];

    for (final card in deck.cards) {
      final state = states[card.id];
      if (state == null) {
        fresh.add(ReviewItem(card: card, state: SchedulingState.fresh));
        continue;
      }
      if (state.due == null || state.due!.isAfter(now)) {
        if (focusIds.contains(card.id) && state.due != null) {
          notDueFocus.add(ReviewItem(card: card, state: state));
        }
        continue;
      }

      final item = ReviewItem(card: card, state: state);
      if (state.phase == CardPhase.learning || state.phase == CardPhase.relearning) {
        learning.add(item);
      } else {
        review.add(item);
      }
    }

    review.sort((a, b) => a.state.due!.compareTo(b.state.due!));
    learning.sort((a, b) => a.state.due!.compareTo(b.state.due!));
    fresh.sort((a, b) => a.card.rank.compareTo(b.card.rank));

    final introducedToday = await _newIntroducedToday(now);
    final budget = newCardsPerDay < 0
        ? fresh.length // -1 sentinel = unlimited
        : (newCardsPerDay - introducedToday).clamp(0, fresh.length);

    if (focusIds.isEmpty) {
      return [...review, ...learning, ...fresh.take(budget)];
    }

    bool isFocus(ReviewItem i) => focusIds.contains(i.card.id);
    notDueFocus.sort((a, b) => a.state.due!.compareTo(b.state.due!));
    final extras = extraFocus > 0
        ? notDueFocus.take(extraFocus).toList()
        : const <ReviewItem>[];
    return [
      ...focusFirst(review, isFocus),
      ...focusFirst(learning, isFocus),
      ...focusFirst(fresh, isFocus).take(budget),
      ...extras,
    ];
  }

  Future<int> _newIntroducedToday(DateTime now) async {
    final rows = await _db.query(
      'daily_activity',
      columns: ['new_introduced'],
      where: 'day = ?',
      whereArgs: [_dayKey(now)],
    );
    return rows.isEmpty ? 0 : (rows.first['new_introduced'] as int?) ?? 0;
  }

  /// Persist one answer: the new scheduling state, the log row, and the day's
  /// activity counters. Written as a single transaction so a crash mid-review
  /// can't leave a card scheduled without a matching log entry.
  Future<SchedulingState> recordAnswer({
    required Deck deck,
    required ReviewItem item,
    required Grade grade,
    required Scheduler scheduler,
    Duration thinkingTime = Duration.zero,
    DateTime? at,
  }) async {
    final now = at ?? DateTime.now();
    final before = item.state;
    final after = scheduler.apply(before, grade, now);

    final elapsedDays = before.lastReview == null
        ? 0.0
        : now.difference(before.lastReview!).inSeconds / 86400.0;

    await _db.transaction((txn) async {
      await txn.insert(
        'card_state',
        {'card_id': item.card.id, 'deck_id': deck.id, ...after.toMap()},
        conflictAlgorithm: ConflictAlgorithm.replace,
      );

      await txn.insert('review_log', {
        'card_id': item.card.id,
        'deck_id': deck.id,
        'reviewed_at': now.millisecondsSinceEpoch,
        'grade': grade.value,
        'elapsed_days': elapsedDays,
        'scheduled_days': before.intervalDays,
        'stability': after.stability,
        'difficulty': after.difficulty,
        'phase_before': before.phase.index,
        'duration_ms': thinkingTime.inMilliseconds,
      });

      final wasNew = before.phase == CardPhase.newCard ? 1 : 0;
      await txn.rawInsert(
        '''
        INSERT INTO daily_activity (day, reviews_done, new_introduced, seconds_spent)
        VALUES (?, 1, ?, ?)
        ON CONFLICT(day) DO UPDATE SET
          reviews_done   = reviews_done + 1,
          new_introduced = new_introduced + ?,
          seconds_spent  = seconds_spent + ?
        ''',
        [_dayKey(now), wasNew, thinkingTime.inSeconds, wasNew, thinkingTime.inSeconds],
      );
    });

    return after;
  }

  Future<void> setSuspended(String cardId, bool suspended) async {
    await _db.update(
      'card_state',
      {'suspended': suspended ? 1 : 0},
      where: 'card_id = ?',
      whereArgs: [cardId],
    );
  }

  /// Consecutive days ending today (or yesterday, if today hasn't started yet)
  /// on which at least one review was answered.
  Future<int> currentStreak({DateTime? at}) async {
    final now = at ?? DateTime.now();
    final rows = await _db.query(
      'daily_activity',
      columns: ['day'],
      where: 'reviews_done > 0',
      orderBy: 'day DESC',
      limit: 400,
    );
    final days = rows.map((r) => r['day'] as String).toSet();
    if (days.isEmpty) return 0;

    var cursor = DateTime(now.year, now.month, now.day);
    // Not having studied yet today shouldn't read as a broken streak.
    if (!days.contains(_dayKey(cursor))) {
      cursor = cursor.subtract(const Duration(days: 1));
      if (!days.contains(_dayKey(cursor))) return 0;
    }

    var streak = 0;
    while (days.contains(_dayKey(cursor))) {
      streak++;
      cursor = cursor.subtract(const Duration(days: 1));
    }
    return streak;
  }

  Future<int> reviewsToday({DateTime? at}) async {
    final rows = await _db.query(
      'daily_activity',
      columns: ['reviews_done'],
      where: 'day = ?',
      whereArgs: [_dayKey(at ?? DateTime.now())],
    );
    return rows.isEmpty ? 0 : (rows.first['reviews_done'] as int?) ?? 0;
  }

  /// Every card's state, for the deck browser.
  Future<Map<String, SchedulingState>> allStates(String deckId) => _statesFor(deckId);

  static String _dayKey(DateTime d) =>
      '${d.year.toString().padLeft(4, '0')}-'
      '${d.month.toString().padLeft(2, '0')}-'
      '${d.day.toString().padLeft(2, '0')}';
}
