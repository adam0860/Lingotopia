import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart' show rootBundle;

import '../data/deck_repository.dart';
import '../difficult/difficult_words_service.dart';
import '../srs/scheduler.dart';
import 'reading_models.dart';
import 'reading_rules.dart';
import 'reading_store.dart';
import 'word_knowledge.dart';
import 'word_practice_service.dart';

/// What recording a finished test produced.
class RecordedAttempt {
  const RecordedAttempt({
    required this.score,
    required this.progress,
    required this.firstPass,
    required this.newBest,
  });

  final QuizScore score;
  final ReadingProgress progress;

  /// This was the first time the passage was passed in this mode.
  final bool firstPass;

  /// The score beat the previous best.
  final bool newBest;
}

/// Loads the passages and keeps the learner's results on them.
class ReadingRepository extends ChangeNotifier {
  ReadingRepository(
    this._store, {
    Future<String> Function(String path)? loadAsset,
  }) : _loadAsset = loadAsset ?? rootBundle.loadString;

  final ReadingProgressStore _store;
  final Future<String> Function(String path) _loadAsset;

  final Map<String, ReadingBook> _books = {};
  final Map<String, ReadingProgress> _progress = {};

  /// The passages of the book for [language] (a deck language code such as
  /// "ru"), or null when this install has none (the feature is hidden).
  ReadingBook? bookFor(String language) => _books[language];

  /// The book that belongs to a deck id such as "ru_core", or null.
  ReadingBook? bookForDeck(String deckId) {
    for (final b in _books.values) {
      if (b.deckId == deckId) return b;
    }
    return null;
  }

  /// Load one language's passages and the saved results. Call it once per
  /// language. A missing or broken file leaves that language without the
  /// feature rather than stopping the app.
  Future<void> init(String assetPath) async {
    try {
      final raw = await _loadAsset(assetPath);
      final book =
          ReadingBook.fromJson(json.decode(raw) as Map<String, dynamic>);
      _books[book.language] = book;
    } catch (_) {
      // This language has no passages.
    }
    try {
      for (final r in await _store.loadAll()) {
        _progress[_key(r.passageId, r.mode)] = r;
      }
    } catch (_) {
      // Start with no results rather than failing to start.
    }
    notifyListeners();
  }

  static String _key(String id, ReadingMode m) => '$id|${m.name}';

  ReadingProgress progressFor(String passageId, ReadingMode mode) =>
      _progress[_key(passageId, mode)] ?? ReadingProgress.empty(passageId, mode);

  /// Passages of [language] that are written for [mode], and how many of them
  /// have been passed. A passage only ever has results in its own mode.
  int passedCount(String language, ReadingMode mode) {
    final b = _books[language];
    if (b == null) return 0;
    return b.passagesFor(mode).where((p) => progressFor(p.id, mode).passed).length;
  }

  int totalCount(String language, ReadingMode mode) =>
      _books[language]?.passagesFor(mode).length ?? 0;

  /// Save a finished test and say what it changed. Writes are made in the
  /// background; a failure to save never loses the result on screen.
  RecordedAttempt record({
    required ReadingPassage passage,
    required ReadingMode mode,
    required QuizScore score,
    DateTime? at,
  }) {
    final before = progressFor(passage.id, mode);
    final after = before.afterAttempt(score.fraction, at ?? DateTime.now());
    _progress[_key(passage.id, mode)] = after;
    _store.save(after).catchError((_) {});
    notifyListeners();
    return RecordedAttempt(
      score: score,
      progress: after,
      firstPass: score.passed && !before.passed,
      newBest: score.fraction > before.bestScore,
    );
  }
}

/// The learner's evidence about words, gathered once for a screen.
///
/// Flashcard states are read from the database once, when the snapshot is
/// made; the games tally and the difficult bank are looked up live.
class KnowledgeSnapshot {
  KnowledgeSnapshot._(this._states, this._practice, this._difficult);

  /// A snapshot with no flashcard history: for tests and for a deck that has
  /// not been loaded.
  KnowledgeSnapshot.empty()
      : _states = const {},
        _practice = null,
        _difficult = null;

  final Map<String, SchedulingState> _states;
  final WordPracticeService? _practice;
  final DifficultWordsService? _difficult;

  static Future<KnowledgeSnapshot> load({
    required DeckRepository decks,
    required String deckId,
    required WordPracticeService practice,
    required DifficultWordsService difficult,
  }) async {
    final states = await decks.allStates(deckId);
    return KnowledgeSnapshot._(states, practice, difficult);
  }

  WordEvidence evidenceOf(String cardId) {
    final row = _difficult?.rowFor(cardId);
    return WordEvidence(
      srs: _states[cardId],
      practice: _practice?.practiceFor(cardId),
      inDifficultBank: _difficult?.isDifficult(cardId) ?? false,
      missStreak: row?.missStreak ?? 0,
    );
  }

  /// The label for a word, or null for a word that has no card (names,
  /// numerals): those are shown without colour.
  Knowledge? levelOf(String? cardId) =>
      cardId == null ? null : classifyWord(evidenceOf(cardId));

  /// Counts of each label among a passage's distinct tracked words.
  Map<Knowledge, int> summary(Iterable<String> cardIds) {
    final out = {for (final k in Knowledge.values) k: 0};
    for (final id in cardIds) {
      final k = levelOf(id)!;
      out[k] = out[k]! + 1;
    }
    return out;
  }
}
