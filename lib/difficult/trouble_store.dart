import 'package:sqflite/sqflite.dart';

import '../data/database.dart';
import 'word_trouble.dart';

/// Where difficult-word history is kept. The service loads everything once at
/// start-up and writes each change; it never reads back during play.
abstract class TroubleStore {
  Future<List<WordTrouble>> loadAll();

  Future<void> save(WordTrouble row);

  /// Forget the history of these cards entirely.
  Future<void> delete(Iterable<String> cardIds);
}

/// Keeps rows in memory. For tests.
class MemoryTroubleStore implements TroubleStore {
  MemoryTroubleStore([Iterable<WordTrouble> initial = const []])
      : rows = {for (final r in initial) r.cardId: r};

  final Map<String, WordTrouble> rows;

  /// How many writes were made, to check that unchanged words are not rewritten.
  int saves = 0;

  @override
  Future<List<WordTrouble>> loadAll() async => rows.values.toList();

  @override
  Future<void> save(WordTrouble row) async {
    saves++;
    rows[row.cardId] = row;
  }

  @override
  Future<void> delete(Iterable<String> cardIds) async {
    for (final id in cardIds) {
      rows.remove(id);
    }
  }
}

/// The learner's database (table `difficult_words`, schema v4).
class SqliteTroubleStore implements TroubleStore {
  SqliteTroubleStore(this._appDb);

  final AppDatabase _appDb;
  Database get _db => _appDb.db;

  @override
  Future<List<WordTrouble>> loadAll() async {
    final rows = await _db.query('difficult_words');
    return [for (final r in rows) WordTrouble.fromMap(r)];
  }

  @override
  Future<void> save(WordTrouble row) => _db.insert(
        'difficult_words',
        row.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace,
      );

  @override
  Future<void> delete(Iterable<String> cardIds) async {
    final ids = cardIds.toList();
    if (ids.isEmpty) return;
    await _db.transaction((txn) async {
      for (final id in ids) {
        await txn.delete('difficult_words', where: 'card_id = ?', whereArgs: [id]);
      }
    });
  }
}
