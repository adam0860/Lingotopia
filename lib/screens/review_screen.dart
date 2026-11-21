import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/app_settings.dart';
import '../data/deck_repository.dart';
import '../data/models.dart';
import '../difficult/difficult_words_service.dart';
import '../difficult/word_trouble.dart';
import '../feedback/feedback_service.dart';
import '../progress/progress_models.dart';
import '../progress/progress_service.dart';
import '../progress/progress_session.dart';
import '../srs/scheduler.dart';
import '../srs/session_queue.dart';
import '../theme/app_theme.dart';
import '../ui/level_widgets.dart';
import '../ui/session_summary.dart';
import '../widgets/flashcard.dart';
import '../widgets/grade_buttons.dart';
import 'settings_screen.dart';

/// One study session over a deck's due queue.
///
/// A card the learner fails goes back into the same session rather than
/// disappearing until tomorrow — that is the whole point of the learning-step
/// ladder in the scheduler.
class ReviewScreen extends StatefulWidget {
  const ReviewScreen({super.key, required this.deck});
  final Deck deck;

  @override
  State<ReviewScreen> createState() => _ReviewScreenState();
}

class _ReviewScreenState extends State<ReviewScreen> {
  late final DeckRepository _repo = context.read<DeckRepository>();
  late final TtsService _tts = context.read<TtsService>();
  late final AppSettings _settings = context.read<AppSettings>();
  late final ProgressService _progress = context.read<ProgressService>();
  late final DifficultWordsService _difficult =
      context.read<DifficultWordsService>();
  late final ProgressSession _session =
      ProgressSession(startLevel: _progress.level.level);

  List<ReviewItem> _queue = [];
  bool _loading = true;
  bool _revealed = false;
  String? _expandedSentenceId;
  DateTime _shownAt = DateTime.now();
  int _answered = 0;
  int _startingQueueLength = 0;

  Scheduler get _scheduler => _settings.schedulerId == 'sm2'
      ? SM2Scheduler(config: _config)
      : Fsrs(config: _config);

  SchedulerConfig get _config =>
      SchedulerConfig(targetRetention: _settings.targetRetention);

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    _repo.newCardsPerDay = _settings.newCardsPerDay;
    // Difficult words lead the queue, and a few more that are not due yet join
    // it as extra practice, unless the learner has turned that off.
    final extra = _settings.difficultExtraCards;
    final queue = await _repo.buildQueue(
      widget.deck,
      focusIds: extra > 0 ? _difficult.bankIds(widget.deck.id) : const {},
      extraFocus: extra,
    );
    if (!mounted) return;
    setState(() {
      // Learning cards left over from earlier whose timer has run out go first.
      _queue = SessionQueue.arrange(queue, DateTime.now());
      _startingQueueLength = queue.length;
      _loading = false;
      _shownAt = DateTime.now();
    });
    _maybeAutoPlay();
  }

  ReviewItem? get _current => _queue.isEmpty ? null : _queue.first;

  void _maybeAutoPlay() {
    final item = _current;
    if (item == null) return;
    if (!_settings.autoPlayWord) return;
    _speakAndWarn(item.card.speakableLemma, id: item.card.id);
  }

  void _reveal() {
    // The word is spoken once, when the card appears (see _maybeAutoPlay).
    // It used to be spoken again here, so every card played twice; the learner
    // can still replay it with the Play button or the R key.
    setState(() => _revealed = true);
  }

  /// Speak a phrase, then tell the learner plainly if nothing could be played
  /// — rather than leaving a tap that just produces silence, which is what a
  /// missing Windows voice does by default.
  Future<void> _speakAndWarn(String text, {required String id}) async {
    await _tts.speak(text, id: id);
    _warnIfFailed();
  }

  void _warnIfFailed() {
    if (!_tts.lastSpeakFailed || !mounted) return;
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(
          'No voice available for ${widget.deck.languageName} on this '
          'device. Add a neural voice key in Settings for audio.',
        ),
        action: SnackBarAction(
          label: 'Settings',
          onPressed: () => Navigator.of(context).push(
            MaterialPageRoute(
              builder: (_) => SettingsScreen(deck: widget.deck),
            ),
          ),
        ),
      ),
    );
  }

  bool _grading = false;

  /// One grade at a time: a quick double tap or key repeat must not award XP
  /// (or reschedule the card) twice while the first answer is being saved.
  Future<void> _grade(Grade grade) async {
    if (_grading) return;
    _grading = true;
    try {
      await _gradeCard(grade);
    } finally {
      _grading = false;
    }
  }

  Future<void> _gradeCard(Grade grade) async {
    final item = _current;
    if (item == null) return;

    final now = DateTime.now();
    final thinking = now.difference(_shownAt);

    // Feedback first, before any await, so it appears the instant the button
    // is pressed rather than after the answer has been saved.
    context.read<FeedbackService>().onGrade(
          context,
          grade,
          nextIn: formatInterval(_scheduler.preview(item.state, now)[grade], now),
        );

    final wasNew = item.state.phase == CardPhase.newCard;

    final newState = await _repo.recordAnswer(
      deck: widget.deck,
      item: item,
      grade: grade,
      scheduler: _scheduler,
      thinkingTime: thinking,
      at: now,
    );

    // The answer is saved, so it counts: XP, the streak and trophies.
    _session.add(_progress.record(ProgressEvent.review(
      grade: grade,
      wasNew: wasNew,
      deckId: widget.deck.id,
    )));

    // "Again" is a miss; Hard, Good and Easy all mean the word was recalled.
    final trouble = _difficult.record(
      deckId: widget.deck.id,
      cardId: item.card.id,
      correct: grade != Grade.again,
      source: AnswerSource.flashcard,
    );

    if (!mounted) return;
    _announceTrouble(trouble);

    final rest = _queue.sublist(1);

    // A card still on its learning steps (a new card marked Good is due in 10
    // minutes, an Again in 1) goes back into the session, but it is shown when
    // its time comes, not after a fixed number of other cards. If nothing else
    // is left it is shown early, as in Anki. See SessionQueue.
    if (SessionQueue.staysInSession(newState, now)) {
      rest.add(item.withState(newState));
    }
    final arranged = SessionQueue.arrange(
      rest,
      DateTime.now(),
      avoidId: item.card.id,
    );

    setState(() {
      _queue = arranged;
      _revealed = false;
      _expandedSentenceId = null;
      _answered++;
      _shownAt = DateTime.now();
    });

    if (_queue.isEmpty) {
      await _tts.stop();
    } else {
      _maybeAutoPlay();
    }
  }

  /// A short note when a word joins or leaves the difficult-words bank.
  void _announceTrouble(TroubleEvent event) {
    final text = switch (event) {
      TroubleEvent.added => 'Added to your difficult words',
      TroubleEvent.cleared => 'Back on track: off your difficult words',
      TroubleEvent.none => null,
    };
    if (text == null) return;
    final messenger = ScaffoldMessenger.of(context);
    messenger.hideCurrentSnackBar();
    messenger.showSnackBar(SnackBar(
      content: Text(text),
      duration: const Duration(milliseconds: 1600),
    ));
  }

  void _onSentenceTap(ExampleSentence s) {
    setState(() {
      _expandedSentenceId = _expandedSentenceId == s.id ? null : s.id;
    });
    if (_expandedSentenceId == s.id) {
      _tts.speak(s.text, id: s.id);
    }
  }

  @override
  Widget build(BuildContext context) {
    if (_loading) {
      return Scaffold(
        appBar: AppBar(title: const Text('Flashcards')),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    final item = _current;
    if (item == null) return _buildDone(context);

    final preview = _scheduler.preview(item.state, DateTime.now());
    final done = _answered;
    final remaining = _queue.length;
    final progress = (done + remaining) == 0 ? 1.0 : done / (done + remaining);

    // Desktop keyboard grading: space reveals, 1-4 grade. Autofocus so the
    // keys work the moment the session opens, with no click needed first.
    return CallbackShortcuts(
      bindings: {
        const SingleActivator(LogicalKeyboardKey.space): () =>
            _revealed ? _grade(Grade.good) : _reveal(),
        const SingleActivator(LogicalKeyboardKey.enter): () =>
            _revealed ? _grade(Grade.good) : _reveal(),
        const SingleActivator(LogicalKeyboardKey.digit1): () =>
            _revealed ? _grade(Grade.again) : null,
        const SingleActivator(LogicalKeyboardKey.digit2): () =>
            _revealed ? _grade(Grade.hard) : null,
        const SingleActivator(LogicalKeyboardKey.digit3): () =>
            _revealed ? _grade(Grade.good) : null,
        const SingleActivator(LogicalKeyboardKey.digit4): () =>
            _revealed ? _grade(Grade.easy) : null,
        const SingleActivator(LogicalKeyboardKey.keyR): () {
          final i = _current;
          if (i != null) _tts.speak(i.card.speakableLemma, id: i.card.id);
        },
      },
      child: Focus(
        autofocus: true,
        child: _buildSession(context, item, preview, done, remaining, progress),
      ),
    );
  }

  Widget _buildSession(
    BuildContext context,
    ReviewItem item,
    SchedulingPreview preview,
    int done,
    int remaining,
    double progress,
  ) {
    final c = context.lingo;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Flashcards'),
        actions: [
          if (_session.xp > 0)
            Center(
              child: Padding(
                padding: const EdgeInsets.only(right: 8),
                child: XpChip(_session.xp),
              ),
            ),
          const _VoiceSourceChip(),
          Center(
            child: Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Text(
                '$done / ${done + remaining}',
                style: Theme.of(context).textTheme.bodySmall,
              ),
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
                    // Keeps the card a readable width on a 27" monitor
                    // instead of stretching to the full window.
                    constraints: const BoxConstraints(maxWidth: 520),
                    child: Flashcard(
                      card: item.card,
                      revealed: _revealed,
                      languageName: widget.deck.languageName,
                      rtl: widget.deck.rtl,
                      speakingKey: context.watch<TtsService>().speakingKey,
                      expandedSentenceId: _expandedSentenceId,
                      onSpeakWord: () => _speakAndWarn(
                          item.card.speakableLemma, id: item.card.id),
                      onSpeakSlow: () => _tts.speak(
                        item.card.speakableLemma,
                        id: '${item.card.id}_slow',
                        rate: _settings.slowRate,
                      ).then((_) => _warnIfFailed()),
                      onSpeakSentence: (s) => _speakAndWarn(s.text, id: s.id),
                      onToggleSentence: _onSentenceTap,
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
                    ? GradeButtons(
                        preview: preview,
                        now: DateTime.now(),
                        onGrade: _grade,
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

    return Scaffold(
      appBar: AppBar(title: const Text('Flashcards')),
      body: Center(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(32),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.check_circle_outline, size: 56, color: c.success),
              const SizedBox(height: 20),
              Text(
                _startingQueueLength == 0 ? 'Nothing due' : 'Session complete',
                style: text.headlineSmall,
              ),
              const SizedBox(height: 10),
              Text(
                _startingQueueLength == 0
                    ? 'Everything in this deck is scheduled for later. Raise the daily new-card limit in Settings to get ahead.'
                    : 'You answered $_answered ${_answered == 1 ? 'card' : 'cards'}. The next batch unlocks when their intervals come due.',
                textAlign: TextAlign.center,
                style: text.bodyMedium?.copyWith(color: c.inkMuted, height: 1.4),
              ),
              if (_session.xp > 0) ...[
                const SizedBox(height: 22),
                SessionSummary(session: _session),
              ],
              const SizedBox(height: 28),
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

/// Shows exactly which voice spoke the most recent word or sentence.
///
/// This exists because a failed cloud provider falls through to the device
/// voice with no exception and no visible error — silence about the failure
/// is precisely what made a mispronounced word look like "the app is
/// broken" rather than "Azure didn't answer this one, here's the backup."
/// Now it says so plainly, and updates on every tap.
class _VoiceSourceChip extends StatelessWidget {
  const _VoiceSourceChip();

  @override
  Widget build(BuildContext context) {
    final tts = context.watch<TtsService>();
    final c = context.lingo;

    final (label, color) = switch (tts.lastSource) {
      TtsSource.cloud => ('Neural voice', c.success),
      TtsSource.device => ('Device voice', c.caution),
      TtsSource.none => ('—', c.inkMuted),
    };

    return Padding(
      padding: const EdgeInsets.only(right: 4),
      child: Center(
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
          decoration: BoxDecoration(
            border: Border.all(color: color),
            borderRadius: BorderRadius.circular(999),
          ),
          child: Text(
            label,
            style: TextStyle(fontSize: 11, color: color, fontWeight: FontWeight.w600),
          ),
        ),
      ),
    );
  }
}

