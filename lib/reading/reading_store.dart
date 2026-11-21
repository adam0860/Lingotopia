import 'package:sqflite/sqflite.dart';

import '../data/database.dart';
import 'reading_rules.dart';

/// Where results of reading and listening tests are kept (table
/// `reading_progress`, schema v5).
abstract class ReadingProgressStore {
  Future<List<ReadingProgress>> loadAll();
  Future<void> save(ReadingProgress row);
}

/// Keeps rows in memory. For tests.
class MemoryReadingProgressStore implements ReadingProgressStore {
  final Map<String, ReadingProgress> rows = {};

  @override
  Future<List<ReadingProgress>> loadAll() async => rows.values.toList();

  @override
  Future<void> save(ReadingProgress row) async {
    rows['${row.passageId}|${row.mode.name}'] = row;
  }
}

class SqliteReadingProgressStore implements ReadingProgressStore {
  SqliteReadingProgressStore(this._appDb);

  final AppDatabase _appDb;
  Database get _db => _appDb.db;

  @override
  Future<List<ReadingProgress>> loadAll() async {
    final rows = await _db.query('reading_progress');
    return [for (final r in rows) ReadingProgress.fromMap(r)];
  }

  @override
  Future<void> save(ReadingProgress row) => _db.insert(
        'reading_progress',
        row.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace,
      );
}
