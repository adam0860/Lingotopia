import 'package:sqflite/sqflite.dart';

import '../data/database.dart';
import 'word_knowledge.dart';

/// Where the games tally is kept (table `word_practice`, schema v5).
abstract class WordPracticeStore {
  Future<List<WordPractice>> loadAll();
  Future<void> save(WordPractice row);
  Future<void> deleteDeck(String deckId);
}

/// Keeps rows in memory. For tests.
class MemoryWordPracticeStore implements WordPracticeStore {
  final Map<String, WordPractice> rows = {};
  int saves = 0;

  @override
  Future<List<WordPractice>> loadAll() async => rows.values.toList();

  @override
  Future<void> save(WordPractice row) async {
    saves++;
    rows[row.cardId] = row;
  }

  @override
  Future<void> deleteDeck(String deckId) async {
    rows.removeWhere((_, r) => r.deckId == deckId);
  }
}

class SqliteWordPracticeStore implements WordPracticeStore {
  SqliteWordPracticeStore(this._appDb);

  final AppDatabase _appDb;
  Database get _db => _appDb.db;

  @override
  Future<List<WordPractice>> loadAll() async {
    final rows = await _db.query('word_practice');
    return [for (final r in rows) WordPractice.fromMap(r)];
  }

  @override
  Future<void> save(WordPractice row) => _db.insert(
        'word_practice',
        row.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace,
      );

  @override
  Future<void> deleteDeck(String deckId) =>
      _db.delete('word_practice', where: 'deck_id = ?', whereArgs: [deckId]);
}
