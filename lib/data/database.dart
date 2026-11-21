import 'dart:io';

import 'package:path/path.dart' as p;
import 'package:path_provider/path_provider.dart';
// sqflite_ffi re-exports everything from sqflite, so importing both is
// redundant. The ffi variant is what supplies databaseFactoryFfi.
import 'package:sqflite_common_ffi/sqflite_ffi.dart';

/// Opens the learner's local database.
///
/// The same sqflite API backs every target: Android and iOS use the platform
/// SQLite directly, while Windows, macOS and Linux go through the ffi factory.
/// Call [AppDatabase.initPlatform] once before [open].
class AppDatabase {
  AppDatabase._(this.db);
  final Database db;

  static const int _schemaVersion = 5;

  /// Wire up the right sqflite backend for the host platform. Safe to call
  /// more than once.
  static void initPlatform() {
    if (Platform.isWindows || Platform.isLinux || Platform.isMacOS) {
      sqfliteFfiInit();
      databaseFactory = databaseFactoryFfi;
    }
  }

  static Future<AppDatabase> open({String fileName = 'lingotopia.db'}) async {
    final dir = await getApplicationSupportDirectory();
    await dir.create(recursive: true);
    final path = p.join(dir.path, fileName);

    final db = await databaseFactory.openDatabase(
      path,
      options: OpenDatabaseOptions(
        version: _schemaVersion,
        onConfigure: (d) => d.execute('PRAGMA foreign_keys = ON'),
        onCreate: _create,
        onUpgrade: _upgrade,
      ),
    );
    return AppDatabase._(db);
  }

  static Future<void> _create(Database db, int version) async {
    // Scheduling state, one row per card the learner has met. Cards not in
    // this table are still new. Deck content itself is NOT stored here — it
    // lives in the asset JSON, so a deck update never risks the learner's
    // progress.
    await db.execute('''
      CREATE TABLE card_state (
        card_id       TEXT PRIMARY KEY,
        deck_id       TEXT NOT NULL,
        phase         INTEGER NOT NULL DEFAULT 0,
        stability     REAL    NOT NULL DEFAULT 0,
        difficulty    REAL    NOT NULL DEFAULT 0,
        due           INTEGER,
        last_review   INTEGER,
        reps          INTEGER NOT NULL DEFAULT 0,
        lapses        INTEGER NOT NULL DEFAULT 0,
        interval_days INTEGER NOT NULL DEFAULT 0,
        learning_step INTEGER NOT NULL DEFAULT 0,
        ease          REAL    NOT NULL DEFAULT 2.5,
        suspended     INTEGER NOT NULL DEFAULT 0
      )
    ''');
    await db.execute('CREATE INDEX idx_card_state_due ON card_state(deck_id, due)');

    // Full review log. Keeping every answer is what makes it possible to
    // re-optimise FSRS weights against this learner later, or to replay the
    // history through a different scheduler.
    await db.execute('''
      CREATE TABLE review_log (
        id             INTEGER PRIMARY KEY AUTOINCREMENT,
        card_id        TEXT    NOT NULL,
        deck_id        TEXT    NOT NULL,
        reviewed_at    INTEGER NOT NULL,
        grade          INTEGER NOT NULL,
        elapsed_days   REAL    NOT NULL,
        scheduled_days INTEGER NOT NULL,
        stability      REAL    NOT NULL,
        difficulty     REAL    NOT NULL,
        phase_before   INTEGER NOT NULL,
        duration_ms    INTEGER NOT NULL DEFAULT 0
      )
    ''');
    await db.execute('CREATE INDEX idx_review_log_card ON review_log(card_id)');
    await db.execute('CREATE INDEX idx_review_log_time ON review_log(reviewed_at)');

    // One row per calendar day, for the streak counter on the home screen.
    await db.execute('''
      CREATE TABLE daily_activity (
        day            TEXT PRIMARY KEY,
        reviews_done   INTEGER NOT NULL DEFAULT 0,
        new_introduced INTEGER NOT NULL DEFAULT 0,
        seconds_spent  INTEGER NOT NULL DEFAULT 0
      )
    ''');

    // Index of synthesized audio on disk, so a clip is only ever generated
    // once per (text, voice, provider).
    await db.execute('''
      CREATE TABLE audio_cache (
        key        TEXT PRIMARY KEY,
        file_path  TEXT NOT NULL,
        provider   TEXT NOT NULL,
        voice      TEXT NOT NULL,
        bytes      INTEGER NOT NULL,
        created_at INTEGER NOT NULL
      )
    ''');

    // One row per lesson the learner has attempted at least once. Lesson
    // content itself lives in assets/lessons/*.json, same split as decks: an
    // updated lesson file can never disturb recorded progress.
    await db.execute('''
      CREATE TABLE lesson_progress (
        lesson_id    TEXT PRIMARY KEY,
        completed    INTEGER NOT NULL DEFAULT 0,
        best_score   REAL    NOT NULL DEFAULT 0,
        attempts     INTEGER NOT NULL DEFAULT 0,
        last_attempt INTEGER
      )
    ''');
    await _createProgressTables(db);
    await _createDifficultWordsTable(db);
    await _createReadingTables(db);
  }

  /// XP, counters and trophies (schema v3).
  static Future<void> _createProgressTables(Database db) async {
    // Every XP award, one row each. The day totals drive the streak, the
    // calendar and the daily goal, so they can always be rebuilt from here.
    await db.execute('''
      CREATE TABLE IF NOT EXISTS xp_log (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        at      INTEGER NOT NULL,
        day     TEXT    NOT NULL,
        amount  INTEGER NOT NULL,
        source  TEXT    NOT NULL,
        deck_id TEXT
      )
    ''');
    await db.execute('CREATE INDEX IF NOT EXISTS idx_xp_log_day ON xp_log(day)');

    // Named running totals that trophies count (reviews, games won...).
    await db.execute('''
      CREATE TABLE IF NOT EXISTS progress_counters (
        key   TEXT PRIMARY KEY,
        value INTEGER NOT NULL
      )
    ''');

    await db.execute('''
      CREATE TABLE IF NOT EXISTS trophies (
        id          TEXT PRIMARY KEY,
        unlocked_at INTEGER NOT NULL
      )
    ''');
  }

  /// Words answered wrongly, and the bank they join (schema v4). One row per
  /// word that has ever been missed; a word never missed has no row.
  static Future<void> _createDifficultWordsTable(Database db) async {
    await db.execute('''
      CREATE TABLE IF NOT EXISTS difficult_words (
        card_id        TEXT PRIMARY KEY,
        deck_id        TEXT NOT NULL,
        miss_streak    INTEGER NOT NULL DEFAULT 0,
        hit_streak     INTEGER NOT NULL DEFAULT 0,
        total_misses   INTEGER NOT NULL DEFAULT 0,
        times_added    INTEGER NOT NULL DEFAULT 0,
        in_bank        INTEGER NOT NULL DEFAULT 0,
        added_at       INTEGER,
        last_miss_at   INTEGER,
        last_answer_at INTEGER,
        cleared_at     INTEGER,
        last_source    TEXT
      )
    ''');
    await db.execute(
      'CREATE INDEX IF NOT EXISTS idx_difficult_bank ON difficult_words(deck_id, in_bank)',
    );
  }

  /// Reading and listening tests, and the games tally that colours words
  /// (schema v5).
  static Future<void> _createReadingTables(Database db) async {
    await db.execute('''
      CREATE TABLE IF NOT EXISTS word_practice (
        card_id     TEXT PRIMARY KEY,
        deck_id     TEXT NOT NULL,
        right_count INTEGER NOT NULL DEFAULT 0,
        wrong_count INTEGER NOT NULL DEFAULT 0,
        last_at     INTEGER
      )
    ''');
    await db.execute('''
      CREATE TABLE IF NOT EXISTS reading_progress (
        passage_id TEXT NOT NULL,
        mode       TEXT NOT NULL,
        best_score REAL NOT NULL DEFAULT 0,
        attempts   INTEGER NOT NULL DEFAULT 0,
        last_at    INTEGER,
        PRIMARY KEY (passage_id, mode)
      )
    ''');
  }

  static Future<void> _upgrade(Database db, int from, int to) async {
    // Migrations land here as the schema moves past v1. Each step must be
    // additive — the learner's review history is the one thing in this app
    // that can't be regenerated.
    if (from < 2) {
      // v2 added Lessons. Anyone who installed before this update has a v1
      // database and will hit onUpgrade, not onCreate, so the table has to
      // be created here too or their app crashes the first time Lessons
      // tries to read from it.
      await db.execute('''
        CREATE TABLE IF NOT EXISTS lesson_progress (
          lesson_id    TEXT PRIMARY KEY,
          completed    INTEGER NOT NULL DEFAULT 0,
          best_score   REAL    NOT NULL DEFAULT 0,
          attempts     INTEGER NOT NULL DEFAULT 0,
          last_attempt INTEGER
        )
      ''');
    }
    if (from < 3) {
      await _createProgressTables(db);
      // Carry the learner's history over: each day they reviewed cards becomes
      // XP, so the streak and calendar start with what they have already done.
      await db.execute('''
        INSERT INTO xp_log (at, day, amount, source, deck_id)
        SELECT CAST(strftime('%s', day) AS INTEGER) * 1000 + 43200000,
               day, reviews_done * 3, 'backfill', NULL
        FROM daily_activity WHERE reviews_done > 0
      ''');
      // A subquery with WHERE rather than HAVING: older SQLite builds (most
      // Android phones) reject HAVING without a GROUP BY. An empty table sums
      // to NULL, which the WHERE skips.
      await db.execute('''
        INSERT OR REPLACE INTO progress_counters (key, value)
        SELECT 'reviews', total
        FROM (SELECT SUM(reviews_done) AS total FROM daily_activity)
        WHERE total > 0
      ''');
      await db.execute('''
        INSERT OR REPLACE INTO progress_counters (key, value)
        SELECT 'cards_learned', total
        FROM (SELECT SUM(new_introduced) AS total FROM daily_activity)
        WHERE total > 0
      ''');
      await db.execute('''
        INSERT OR REPLACE INTO progress_counters (key, value)
        SELECT 'lessons', total
        FROM (SELECT COUNT(*) AS total FROM lesson_progress WHERE completed = 1)
        WHERE total > 0
      ''');
      await db.execute('''
        INSERT OR REPLACE INTO progress_counters (key, value)
        SELECT 'deck_' || deck_id, 1 FROM (SELECT DISTINCT deck_id FROM card_state)
      ''');
    }
    if (from < 4) {
      await _createDifficultWordsTable(db);
      await _seedDifficultWords(db);
    }
    if (from < 5) {
      await _createReadingTables(db);
    }
  }

  /// Start the bank with what the review history already shows: a card whose
  /// last two flashcard answers were both "Again" is a difficult word. Done in
  /// Dart rather than SQL window functions, which older Android SQLite lacks.
  static Future<void> _seedDifficultWords(Database db) async {
    final rows = await db.rawQuery(
      'SELECT card_id, deck_id, grade, reviewed_at FROM review_log '
      'ORDER BY card_id, reviewed_at DESC',
    );
    String? current;
    var seen = 0;
    var againRun = 0;
    int? latest;
    String? deck;
    final batch = db.batch();
    void finish() {
      if (current != null && seen >= 2 && againRun >= 2) {
        batch.insert(
          'difficult_words',
          {
            'card_id': current,
            'deck_id': deck,
            'miss_streak': againRun,
            'hit_streak': 0,
            'total_misses': againRun,
            'times_added': 1,
            'in_bank': 1,
            'added_at': latest,
            'last_miss_at': latest,
            'last_answer_at': latest,
            'last_source': 'flashcard',
          },
          conflictAlgorithm: ConflictAlgorithm.ignore,
        );
      }
    }

    var streakOpen = true;
    for (final r in rows) {
      final id = r['card_id'] as String;
      if (id != current) {
        finish();
        current = id;
        deck = r['deck_id'] as String;
        latest = r['reviewed_at'] as int;
        seen = 0;
        againRun = 0;
        streakOpen = true;
      }
      seen++;
      // Newest first: count the answers that are "Again" until one is not.
      if (streakOpen && (r['grade'] as int) == 1) {
        againRun++;
      } else {
        streakOpen = false;
      }
    }
    finish();
    await batch.commit(noResult: true);
  }

  Future<void> close() => db.close();
}
