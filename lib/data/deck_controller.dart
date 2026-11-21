import 'package:flutter/foundation.dart';

import '../audio/tts_service.dart';
import 'app_settings.dart';
import 'deck_repository.dart';
import 'models.dart';

/// Owns which language is being studied, and swaps the loaded deck when the
/// learner changes it.
///
/// Only one deck is held in memory at a time. Each is 1.5–1.8 MB of JSON and
/// parsing costs a noticeable beat on a phone, so loading all four up front
/// would slow every cold start to pay for decks the learner isn't using.
class DeckController extends ChangeNotifier {
  DeckController({
    required DeckRepository repository,
    required AppSettings settings,
    required TtsService tts,
  })  : _repo = repository,
        _settings = settings,
        _tts = tts;

  final DeckRepository _repo;
  final AppSettings _settings;
  final TtsService _tts;

  Deck? _deck;
  DeckDescriptor? _descriptor;
  bool _loading = false;
  Object? _error;

  Deck? get deck => _deck;
  DeckDescriptor? get descriptor => _descriptor;
  bool get isLoading => _loading;
  Object? get error => _error;

  List<DeckDescriptor> get available => DeckDescriptor.all;

  /// Load whichever deck the learner last had open.
  Future<void> init() => load(DeckDescriptor.byId(_settings.activeDeckId));

  Future<void> load(DeckDescriptor d) async {
    _loading = true;
    _error = null;
    notifyListeners();

    try {
      // Stop any clip from the previous language mid-sentence.
      await _tts.stop();

      final deck = await _repo.loadDeck(d.assetPath);
      _deck = deck;
      _descriptor = d;

      _settings.activeDeckId = d.id;
      _tts.setLanguage(d.languageTag);
      _tts.setPreferredVoice(_settings.voiceId ?? deck.targetVoice);
    } catch (e) {
      _error = e;
    } finally {
      _loading = false;
      notifyListeners();
    }
  }

  Future<void> switchTo(String deckId) async {
    if (deckId == _descriptor?.id) return;
    await load(DeckDescriptor.byId(deckId));
  }
}
