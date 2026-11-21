import 'dart:async';

import 'word_knowledge.dart';
import 'word_practice_store.dart';

/// The games tally: how often each word was answered right and wrong in the
/// games and drills. Held in memory and written behind the scenes, one write
/// at a time and in order, so a fast game never waits on the database.
/// Storage failures are swallowed: this is a study aid.
class WordPracticeService {
  WordPracticeService(this._store);

  final WordPracticeStore _store;
  final Map<String, WordPractice> _rows = {};
  Future<void> _writes = Future.value();

  Future<void> init() async {
    try {
      for (final r in await _store.loadAll()) {
        _rows[r.cardId] = r;
      }
    } catch (_) {
      // Start with an empty tally rather than failing to start the app.
    }
  }

  /// Count one answer.
  void record({
    required String deckId,
    required String cardId,
    required bool correct,
    DateTime? at,
  }) {
    final row = (_rows[cardId] ?? WordPractice(cardId: cardId, deckId: deckId))
        .after(correct: correct, at: at ?? DateTime.now());
    _rows[cardId] = row;
    _writes = _writes.then((_) => _store.save(row)).catchError((_) {});
  }

  WordPractice? practiceFor(String cardId) => _rows[cardId];

  /// Resolves once every write made so far has finished. For tests.
  Future<void> flush() => _writes;
}
