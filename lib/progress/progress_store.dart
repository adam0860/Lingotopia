import 'package:sqflite/sqflite.dart';

import '../data/database.dart';
import 'progress_models.dart';

/// Where progress is kept. The engine never touches storage; the service asks
/// a store to load once at start-up and to write each change.
abstract class ProgressStore {
  Future<ProgressState> load();

  Future<void> persist(ProgressDelta delta);
}

/// Keeps everything in memory. For tests.
class MemoryProgressStore implements ProgressStore {
  MemoryProgressStore([ProgressState? initial]) : _initial = initial ?? ProgressState();

  final ProgressState _initial;

  /// Every delta written, in order.
  final List<ProgressDelta> written = [];

  @override
  Future<ProgressState> load() async => _initial;

  @override
  Future<void> persist(ProgressDelta delta) async {
    written.add(delta);
  }
}

/// The learner's database: an XP log, counters and unlocked trophies.
class SqliteProgressStore implements ProgressStore {
  SqliteProgressStore(this._appDb);

  final AppDatabase _appDb;
  Database get _db => _appDb.db;

  @override
  Future<ProgressState> load() async {
    final state = ProgressState();

    // The total counts everything. The per-day figures leave out trophy
    // bonuses: only studying makes a day active.
    final total = await _db.rawQuery('SELECT SUM(amount) AS xp FROM xp_log');
    state.totalXp = (total.first['xp'] as num?)?.toInt() ?? 0;

    final days = await _db.rawQuery(
      "SELECT day, SUM(amount) AS xp FROM xp_log WHERE source != 'trophy' "
      'GROUP BY day',
    );
    for (final r in days) {
      state.dailyXp[r['day'] as String] = (r['xp'] as num?)?.toInt() ?? 0;
    }

    final counters = await _db.query('progress_counters');
    for (final r in counters) {
      state.counters[r['key'] as String] = (r['value'] as num).toInt();
    }

    final trophies = await _db.query('trophies');
    for (final r in trophies) {
      state.trophies[r['id'] as String] = (r['unlocked_at'] as num).toInt();
    }
    return state;
  }

  @override
  Future<void> persist(ProgressDelta delta) async {
    if (delta.isEmpty) return;
    await _db.transaction((txn) async {
      for (final r in delta.xpRows) {
        await txn.insert('xp_log', {
          'at': r.at.millisecondsSinceEpoch,
          'day': r.day,
          'amount': r.amount,
          'source': r.source.name,
          'deck_id': r.deckId,
        });
      }
      for (final e in delta.counterWrites.entries) {
        await txn.insert(
          'progress_counters',
          {'key': e.key, 'value': e.value},
          conflictAlgorithm: ConflictAlgorithm.replace,
        );
      }
      for (final e in delta.trophyWrites.entries) {
        await txn.insert(
          'trophies',
          {'id': e.key, 'unlocked_at': e.value},
          conflictAlgorithm: ConflictAlgorithm.ignore,
        );
      }
    });
  }
}
