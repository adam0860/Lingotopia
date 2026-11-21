import 'dart:async';

import 'package:flutter/foundation.dart';

import 'trouble_store.dart';
import 'word_trouble.dart';

/// The learner's difficult-word bank.
///
/// Every place a word is answered (flashcards, the drill, and the four games)
/// reports to [record]. A word that is missed [TroubleRules.missesToAdd] times
/// in a row joins the bank; a banked word leaves after
/// [TroubleRules.correctToClear] right answers in a row.
///
/// State is held in memory and written behind the scenes, one write at a time
/// and in order, so a fast game (Quick Recall can ask a word every two
/// seconds) never waits on the database. Storage failures are swallowed: this
/// is a study aid, and must never stop an answer from counting elsewhere.
class DifficultWordsService extends ChangeNotifier {
  DifficultWordsService({
    required TroubleStore store,
    TroubleRules Function()? rules,
    this.onAnswer,
  })  : _store = store,
        _rules = rules ?? (() => TroubleRules.standard);

  /// Told about every answer before the bank looks at it, including right
  /// answers to words that were never missed. The reading feature uses this
  /// to tally how each word does in the games.
  final void Function(
    String deckId,
    String cardId,
    bool correct,
    AnswerSource source,
  )? onAnswer;

  final TroubleStore _store;
  final TroubleRules Function() _rules;

  final Map<String, WordTrouble> _rows = {};
  Future<void> _writes = Future.value();

  /// The thresholds currently in force.
  TroubleRules get rules => _rules();

  Future<void> init() async {
    try {
      for (final r in await _store.loadAll()) {
        _rows[r.cardId] = r;
      }
    } catch (_) {
      // Start with an empty bank rather than failing to start the app.
    }
    notifyListeners();
  }

  /// Report one answer. Returns what it did to the bank, so a screen can say
  /// "added to difficult words" or "back on track".
  TroubleEvent record({
    required String deckId,
    required String cardId,
    required bool correct,
    required AnswerSource source,
    DateTime? at,
  }) {
    try {
      onAnswer?.call(deckId, cardId, correct, source);
    } catch (_) {
      // A listener must never stop an answer from counting.
    }
    final before = _rows[cardId];
    // A right answer for a word that has never been missed changes nothing.
    if (before == null && correct) return TroubleEvent.none;

    final (after, event) = (before ?? WordTrouble.fresh(cardId, deckId)).answered(
      correct: correct,
      at: at ?? DateTime.now(),
      source: source,
      rules: rules,
    );
    _rows[cardId] = after;
    // A right answer for a word that is not in the bank and has no misses
    // running changes nothing worth a write (only the time of the answer).
    final nothingToSave =
        correct && before != null && !before.inBank && before.missStreak == 0;
    if (!nothingToSave) _queue(() => _store.save(after));
    // The bank only changes shape on these; a plain miss or hit does not need
    // every listener to rebuild.
    if (event != TroubleEvent.none) notifyListeners();
    return event;
  }

  /// Words in the bank for a deck: the most missed first, then the most
  /// recently missed.
  List<WordTrouble> bank(String deckId) {
    final out = [
      for (final r in _rows.values)
        if (r.inBank && r.deckId == deckId) r,
    ]..sort((a, b) {
        final byMisses = b.totalMisses.compareTo(a.totalMisses);
        if (byMisses != 0) return byMisses;
        final at = a.lastMissAt?.millisecondsSinceEpoch ?? 0;
        final bt = b.lastMissAt?.millisecondsSinceEpoch ?? 0;
        return bt.compareTo(at);
      });
    return out;
  }

  Set<String> bankIds(String deckId) => {
        for (final r in _rows.values)
          if (r.inBank && r.deckId == deckId) r.cardId,
      };

  int count(String deckId) {
    var n = 0;
    for (final r in _rows.values) {
      if (r.inBank && r.deckId == deckId) n++;
    }
    return n;
  }

  bool isDifficult(String cardId) => _rows[cardId]?.inBank ?? false;

  WordTrouble? rowFor(String cardId) => _rows[cardId];

  /// Words that left the bank, most recent first: the ones to be proud of.
  List<WordTrouble> recovered(String deckId, {int limit = 50}) {
    final out = [
      for (final r in _rows.values)
        if (!r.inBank && r.clearedAt != null && r.deckId == deckId) r,
    ]..sort((a, b) => b.clearedAt!.compareTo(a.clearedAt!));
    return out.length > limit ? out.sublist(0, limit) : out;
  }

  /// Take a word out of the bank by hand, and forget its history.
  Future<void> remove(String cardId) => removeMany([cardId]);

  Future<void> removeMany(Iterable<String> cardIds) {
    final ids = cardIds.toList();
    for (final id in ids) {
      _rows.remove(id);
    }
    notifyListeners();
    return _queue(() => _store.delete(ids));
  }

  /// Empty one deck's bank. Its history goes too, including the words listed
  /// as recovered.
  Future<void> removeAll(String deckId) => removeMany([
        for (final r in _rows.values)
          if (r.deckId == deckId) r.cardId,
      ]);

  /// Tell listeners to redraw. Answers only notify when the bank changes
  /// shape, so a screen that shows streaks and counts calls this when it
  /// comes back from practice.
  void refresh() => notifyListeners();

  /// Resolves once every write made so far has finished. For tests, and for a
  /// screen that is about to be torn down.
  Future<void> flush() => _writes;

  Future<void> _queue(Future<void> Function() job) {
    _writes = _writes.then((_) => job()).catchError((_) {});
    return _writes;
  }
}
