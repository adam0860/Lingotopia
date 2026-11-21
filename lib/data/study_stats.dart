import 'dart:async';

import 'package:flutter/foundation.dart';

import 'deck_repository.dart';
import 'models.dart';

/// Flashcard counts for the deck being studied, shared by the Home and Learn
/// tabs so each one does not run the same query. The app shell refreshes it
/// when the deck changes and shortly after the learner earns anything.
class StudyStats extends ChangeNotifier {
  StudyStats(this._repo);

  final DeckRepository _repo;

  DeckStats? _stats;
  String? _forDeck;
  Timer? _debounce;
  bool _disposed = false;

  /// The counts for [deck], or null while they load or if they belong to a
  /// different deck.
  DeckStats? statsFor(Deck? deck) =>
      deck != null && deck.id == _forDeck ? _stats : null;

  Future<void> refresh(Deck deck) async {
    try {
      final s = await _repo.stats(deck);
      if (_disposed) return;
      _stats = s;
      _forDeck = deck.id;
      notifyListeners();
    } catch (e) {
      debugPrint('[Lingotopia/StudyStats] refresh failed: $e');
    }
  }

  void refreshSoon(Deck deck) {
    _debounce?.cancel();
    _debounce = Timer(const Duration(milliseconds: 300), () => refresh(deck));
  }

  @override
  void dispose() {
    _disposed = true;
    _debounce?.cancel();
    super.dispose();
  }
}
