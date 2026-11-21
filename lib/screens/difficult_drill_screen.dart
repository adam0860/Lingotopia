import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/app_settings.dart';
import '../data/models.dart';
import '../difficult/difficult_words_service.dart';
import '../difficult/word_trouble.dart';
import '../theme/app_theme.dart';
import '../widgets/flashcard.dart';

/// A short practice session on nothing but the difficult-word bank.
///
/// It is separate from the flashcard schedule on purpose: it does not move any
/// card's due date and writes nothing to the review log, so drilling a word as
/// often as you like never disturbs your spaced repetition. It does count as
/// answers for the bank (so a word can recover here). It earns no XP, so it
/// cannot be farmed.
///
/// A word you get right leaves the session. A word you miss comes back a few
/// cards later, until you have it.
class DifficultDrillScreen extends StatefulWidget {
  const DifficultDrillScreen({super.key, required this.deck});

  final Deck deck;

  /// The most words one drill takes, worst first. A long bank is worked
  /// through a session at a time.
  static const maxWords = 20;

  @override
  State<DifficultDrillScreen> createState() => _DifficultDrillScreenState();
}

class _DifficultDrillScreenState extends State<DifficultDrillScreen> {
  late final TtsService _tts = context.read<TtsService>();
  late final AppSettings _settings = context.read<AppSettings>();
  late final DifficultWordsService _difficult =
      context.read<DifficultWordsService>();

  /// Cards still to answer, current first.
  List<VocabCard> _queue = [];
  bool _revealed = false;
  String? _expandedSentenceId;
  bool _busy = false;

  int _startCount = 0;
  int _answers = 0;
  int _gotIt = 0;
  int _stillHard = 0;
  int _cleared = 0;

  @override
  void initState() {
    super.initState();
    _begin();
  }

  void _begin() {
    final byId = {for (final c in widget.deck.cards) c.id: c};
    final cards = <VocabCard>[
      for (final t in _difficult.bank(widget.deck.id))
        if (byId[t.cardId] != null) byId[t.cardId]!,
    ];
    final take = cards.length > DifficultDrillScreen.maxWords
        ? cards.sublist(0, DifficultDrillScreen.maxWords)
        : cards;
    // Shuffled, so the order is not the same worst-first list every time.
    final queue = [...take]..shuffle();
    setState(() {
      _queue = queue;
      _startCount = queue.length;
      _revealed = false;
      _expandedSentenceId = null;
      _answers = 0;
      _gotIt = 0;
      _stillHard = 0;
      _cleared = 0;
    });
    _maybeAutoPlay();
  }

  VocabCard? get _current => _queue.isEmpty ? null : _queue.first;

  void _maybeAutoPlay() {
    final card = _current;
    if (card == null || !_settings.autoPlayWord) return;
    _speak(card.speakableLemma, id: card.id);
  }

  Future<void> _speak(String text, {required String id, double rate = 1.0}) async {
    await _tts.speak(text, id: id, rate: rate);
    if (!_tts.lastSpeakFailed || !mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text('No voice available for ${widget.deck.languageName} on '
          'this device.'),
    ));
  }

  void _reveal() => setState(() => _revealed = true);

  Future<void> _answer({required bool recalled}) async {
    final card = _current;
    if (card == null || _busy) return;
    _busy = true;
    try {
      final event = _difficult.record(
        deckId: widget.deck.id,
        cardId: card.id,
        correct: recalled,
        source: AnswerSource.drill,
      );
      _announce(event);

      final rest = _queue.sublist(1);
      if (!recalled) {
        // Back in a few cards, never straight away.
        rest.insert(rest.length < 3 ? rest.length : 3, card);
      }
      setState(() {
        _queue = rest;
        _revealed = false;
        _expandedSentenceId = null;
        _answers++;
        if (recalled) {
          _gotIt++;
        } else {
          _stillHard++;
        }
        if (event == TroubleEvent.cleared) _cleared++;
      });
      if (rest.isEmpty) {
        await _tts.stop();
      } else {
        _maybeAutoPlay();
      }
    } finally {
      _busy = false;
    }
  }

  void _announce(TroubleEvent event) {
    if (event != TroubleEvent.cleared) return;
    final messenger = ScaffoldMessenger.of(context);
    messenger.hideCurrentSnackBar();
    messenger.showSnackBar(const SnackBar(
      content: Text('Back on track: off your difficult words'),
      duration: Duration(milliseconds: 1600),
    ));
  }

  @override
  Widget build(BuildContext context) {
    final card = _current;
    if (card == null) return _buildDone(context);

    final done = _startCount - _queue.length;
    final progress = _startCount == 0 ? 1.0 : done / _startCount;

    return CallbackShortcuts(
      bindings: {
        const SingleActivator(LogicalKeyboardKey.space): () =>
            _revealed ? _answer(recalled: true) : _reveal(),
        const SingleActivator(LogicalKeyboardKey.enter): () =>
            _revealed ? _answer(recalled: true) : _reveal(),
        const SingleActivator(LogicalKeyboardKey.digit1): () =>
            _revealed ? _answer(recalled: false) : null,
        const SingleActivator(LogicalKeyboardKey.digit2): () =>
            _revealed ? _answer(recalled: true) : null,
        const SingleActivator(LogicalKeyboardKey.keyR): () =>
            _speak(card.speakableLemma, id: card.id),
      },
      child: Focus(
        autofocus: true,
        child: _buildSession(context, card, done, progress),
      ),
    );
  }

  Widget _buildSession(
      BuildContext context, VocabCard card, int done, double progress) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Difficult words'),
        actions: [
          Center(
            child: Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Text('$done / $_startCount', style: text.bodySmall),
            ),
          ),
        ],
      ),
      body: SafeArea(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(24, 0, 24, 0),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(2),
                child: LinearProgressIndicator(
                  value: progress,
                  minHeight: 6,
                  backgroundColor: c.track,
                  valueColor: AlwaysStoppedAnimation(c.success),
                ),
              ),
            ),
            Expanded(
              child: Center(
                child: SingleChildScrollView(
                  padding: const EdgeInsets.fromLTRB(24, 24, 24, 8),
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 520),
                    child: Flashcard(
                      card: card,
                      revealed: _revealed,
                      languageName: widget.deck.languageName,
                      rtl: widget.deck.rtl,
                      speakingKey: context.watch<TtsService>().speakingKey,
                      expandedSentenceId: _expandedSentenceId,
                      onSpeakWord: () =>
                          _speak(card.speakableLemma, id: card.id),
                      onSpeakSlow: () => _speak(card.speakableLemma,
                          id: '${card.id}_slow', rate: _settings.slowRate),
                      onSpeakSentence: (s) => _speak(s.text, id: s.id),
                      onToggleSentence: (s) {
                        setState(() => _expandedSentenceId =
                            _expandedSentenceId == s.id ? null : s.id);
                        if (_expandedSentenceId == s.id) {
                          _speak(s.text, id: s.id);
                        }
                      },
                    ),
                  ),
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(24, 8, 24, 24),
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 520),
                child: _revealed
                    ? Row(
                        children: [
                          Expanded(
                            child: OutlinedButton(
                              onPressed: () => _answer(recalled: false),
                              child: const Text('Still hard'),
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: FilledButton(
                              onPressed: () => _answer(recalled: true),
                              child: const Text('Got it'),
                            ),
                          ),
                        ],
                      )
                    : SizedBox(
                        width: double.infinity,
                        child: FilledButton(
                          onPressed: _reveal,
                          child: const Text('Show answer'),
                        ),
                      ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildDone(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final left = _difficult.count(widget.deck.id);

    final String title;
    final String body;
    if (_startCount == 0) {
      title = 'Nothing to practise';
      body = 'You have no difficult words in this deck right now. Words you '
          'miss ${_difficult.rules.missesToAdd} times in a row will collect '
          'here.';
    } else {
      title = 'Drill complete';
      final parts = <String>[
        'You got $_gotIt right and missed $_stillHard.',
        if (_cleared > 0)
          _cleared == 1
              ? '1 word is off your list.'
              : '$_cleared words are off your list.',
        left == 0
            ? 'Your difficult words are all clear.'
            : '$left ${left == 1 ? 'word is' : 'words are'} still on your list.',
      ];
      body = parts.join(' ');
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Difficult words')),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(32),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.check_circle_outline, size: 56, color: c.success),
              const SizedBox(height: 20),
              Text(title, style: text.headlineSmall),
              const SizedBox(height: 10),
              Text(body,
                  textAlign: TextAlign.center,
                  style:
                      text.bodyMedium?.copyWith(color: c.inkMuted, height: 1.4)),
              const SizedBox(height: 28),
              if (_startCount > 0 && left > 0) ...[
                FilledButton(
                  onPressed: _begin,
                  child: const Text('Drill again'),
                ),
                const SizedBox(height: 10),
                OutlinedButton(
                  onPressed: () => Navigator.of(context).pop(),
                  child: const Text('Done'),
                ),
              ] else
                FilledButton(
                  onPressed: () => Navigator.of(context).pop(),
                  child: const Text('Done'),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
