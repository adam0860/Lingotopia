import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../../audio/tts_service.dart';
import '../../data/models.dart';
import '../../difficult/difficult_words_service.dart';
import '../../difficult/word_trouble.dart';
import '../../feedback/feedback_service.dart';
import '../../lessons/bidi.dart';
import '../../progress/progress_models.dart';
import '../../progress/progress_service.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../../ui/streak_flame.dart';
import '../ladder/ladder_widgets.dart';
import 'recall_engine.dart';
import 'recall_result_view.dart';
import 'recall_stats.dart';

enum _Phase { countdown, playing, over }

/// One 60-second round of Quick Recall.
///
/// The clock is driven by a [Ticker]: every frame the real time since the last
/// frame is handed to the round. Whenever the round must not run (a dialog is
/// open, the app is in the background) the ticker is stopped, so no time is
/// lost or gained. The short colour feedback after an answer is counted on the
/// same ticker, so it pauses with everything else.
///
/// Pops with a [RecallExit] telling the lobby what to do next.
class RecallScreen extends StatefulWidget {
  const RecallScreen({
    super.key,
    required this.deck,
    required this.pool,
    required this.stats,
  });

  final Deck deck;
  final RecallPool pool;
  final RecallStats stats;

  @override
  State<RecallScreen> createState() => _RecallScreenState();
}

class _RecallScreenState extends State<RecallScreen>
    with SingleTickerProviderStateMixin, WidgetsBindingObserver {
  /// How long the right and wrong colours stay before the next question.
  static const double _feedbackSeconds = 0.45;

  /// "3, 2, 1" before the clock starts.
  static const double _countStep = 0.6;
  static const double _countdownSeconds = 3 * _countStep;

  /// A frame that took longer than this (a stall, or a muted ticker waking
  /// up) is counted as this long, so a hiccup cannot eat the clock.
  static const double _maxFrameGap = 0.25;

  /// How long the "+3s" / "-3s" chip stays on.
  static const double _flashSeconds = 0.8;

  late final RecallQuestionSource _source;
  late final RecallRound _round;
  late final Ticker _ticker;

  /// The seconds left, repainted every frame without rebuilding the screen.
  final ValueNotifier<double> _clock =
      ValueNotifier<double>(RecallRules.roundSeconds);

  _Phase _phase = _Phase.countdown;

  /// True when not a single question could be written from this word list.
  bool _unavailable = false;

  double _countdownLeft = _countdownSeconds;
  int _countShown = 3;
  Duration _lastElapsed = Duration.zero;

  bool _dialogOpen = false;
  bool _background = false;
  bool _recorded = false;
  bool _warnedNoVoice = false;

  /// The question on screen. While an answer is on show it is the question
  /// that was answered, although the round has already drawn the next one.
  RecallQuestion? _shown;
  RecallAnswer? _feedback;
  double _feedbackLeft = 0;

  String? _flashText;
  bool _flashGood = false;
  double _flashLeft = 0;

  ProgressSession? _session;
  RecallRecords _records = const RecallRecords();

  static const _letterKeys = [
    LogicalKeyboardKey.keyA,
    LogicalKeyboardKey.keyB,
    LogicalKeyboardKey.keyC,
    LogicalKeyboardKey.keyD,
  ];
  static const _digitKeys = [
    LogicalKeyboardKey.digit1,
    LogicalKeyboardKey.digit2,
    LogicalKeyboardKey.digit3,
    LogicalKeyboardKey.digit4,
  ];

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    _source = RecallQuestionSource(widget.deck, widget.pool);
    _round = RecallRound(_source);
    _shown = _round.current;
    _unavailable = _shown == null;
    _ticker = createTicker(_onTick);
    _syncTicker();
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    _ticker.dispose();
    _clock.dispose();
    super.dispose();
  }

  @override
  void didChangeAppLifecycleState(AppLifecycleState state) {
    _background = state != AppLifecycleState.resumed;
    _syncTicker();
  }

  // --- The clock -------------------------------------------------------------

  /// Run the ticker exactly when the round may run. Restarting it resets its
  /// elapsed time, which is why [_onTick] works with differences.
  void _syncTicker() {
    final shouldRun =
        !_unavailable && _phase != _Phase.over && !_dialogOpen && !_background;
    if (shouldRun && !_ticker.isActive) {
      _lastElapsed = Duration.zero;
      _ticker.start();
    } else if (!shouldRun && _ticker.isActive) {
      _ticker.stop();
    }
  }

  void _onTick(Duration elapsed) {
    var dt = (elapsed - _lastElapsed).inMicroseconds / 1000000.0;
    _lastElapsed = elapsed;
    if (dt <= 0) return;
    if (dt > _maxFrameGap) dt = _maxFrameGap;

    if (_phase == _Phase.countdown) {
      _countdownLeft -= dt;
      if (_countdownLeft <= 0) {
        setState(() => _phase = _Phase.playing);
      } else {
        final shown = (_countdownLeft / _countStep).ceil();
        if (shown != _countShown) setState(() => _countShown = shown);
      }
      return;
    }
    if (_phase != _Phase.playing) return;

    var changed = false;
    _round.advance(dt);
    _clock.value = _round.remaining;

    if (_feedback != null) {
      _feedbackLeft -= dt;
      if (_feedbackLeft <= 0) {
        _feedback = null;
        _shown = _round.current;
        changed = true;
      }
    }
    if (_flashLeft > 0) {
      _flashLeft -= dt;
      if (_flashLeft <= 0) changed = true;
    }

    // Out of time. A last answer that emptied the clock still gets its colours
    // for a moment first.
    if (_round.isOver && _feedback == null) {
      _finish();
      return;
    }
    if (changed) setState(() {});
  }

  // --- Answering -------------------------------------------------------------

  void _answer(int i) {
    if (_shown == null || _phase != _Phase.playing || _feedback != null) return;
    if (_dialogOpen || _background) return;
    final result = _round.answer(i);
    if (result == null) return;

    context.read<FeedbackService>().onQuickAnswer(correct: result.correct);
    context.read<DifficultWordsService>().record(
          deckId: widget.deck.id,
          cardId: result.question.card.id,
          correct: result.correct,
          source: AnswerSource.recall,
        );
    _clock.value = _round.remaining;
    _feedback = result;
    _feedbackLeft = _feedbackSeconds;
    if (result.penaltySeconds > 0) {
      _flashText = '−${result.penaltySeconds.round()}s';
      _flashGood = false;
      _flashLeft = _flashSeconds;
    } else if (result.bonusSeconds >= 0.5) {
      _flashText = '+${result.bonusSeconds.round()}s';
      _flashGood = true;
      _flashLeft = _flashSeconds;
    }
    setState(() {});
  }

  /// The round is over: save the bests, count it towards XP and trophies once,
  /// and switch to the result page.
  void _finish() {
    if (_recorded) return;
    _recorded = true;
    _ticker.stop();

    final summary = _round.summary;
    final records = widget.stats.record(
      score: summary.correct,
      reach: summary.reach,
      streak: summary.bestStreak,
    );
    widget.stats.save(widget.deck.language);

    final progress = context.read<ProgressService>();
    final session = ProgressSession(startLevel: progress.level.level);
    session.add(progress.record(ProgressEvent.quickRecall(
      correct: summary.correct,
      reach: summary.reach,
      bestStreak: summary.bestStreak,
      deckId: widget.deck.id,
    )));

    _warnedNoVoice = false;
    setState(() {
      _phase = _Phase.over;
      _records = records;
      _session = session;
    });
  }

  // --- Speech ----------------------------------------------------------------

  Future<void> _speak(String text, String id) async {
    final tts = context.read<TtsService>();
    await tts.speak(text, id: id);
    if (tts.lastSpeakFailed && !_warnedNoVoice && mounted) {
      _warnedNoVoice = true;
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text('No voice available for ${widget.deck.languageName} on '
            'this device. Add a neural voice key in Settings for audio.'),
      ));
    }
  }

  // --- Quitting --------------------------------------------------------------

  Future<void> _confirmQuit() async {
    if (_dialogOpen) return;
    if (_phase == _Phase.over || _unavailable) {
      Navigator.of(context).pop(RecallExit.settings);
      return;
    }
    // The clock stands still while the question is on the table.
    _dialogOpen = true;
    _syncTicker();
    final quit = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Leave the round?'),
        content: const Text('The round will end and won’t be counted.'),
        actions: [
          TextButton(
              onPressed: () => Navigator.pop(ctx, false),
              child: const Text('Keep playing')),
          TextButton(
              onPressed: () => Navigator.pop(ctx, true),
              child: const Text('Leave')),
        ],
      ),
    );
    if (!mounted) return;
    _dialogOpen = false;
    if (quit == true) {
      Navigator.of(context).pop(RecallExit.settings);
    } else {
      _syncTicker();
    }
  }

  // --- Build -----------------------------------------------------------------

  @override
  Widget build(BuildContext context) {
    if (_phase == _Phase.over) {
      return RecallResultView(
        deck: widget.deck,
        summary: _round.summary,
        stats: widget.stats,
        records: _records,
        session: _session,
        onSpeak: _speak,
      );
    }

    final c = context.lingo;
    return PopScope(
      canPop: _unavailable,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _confirmQuit();
      },
      child: CallbackShortcuts(
        bindings: {
          for (var i = 0; i < _letterKeys.length; i++) ...{
            SingleActivator(_letterKeys[i]): () => _answer(i),
            SingleActivator(_digitKeys[i]): () => _answer(i),
          },
        },
        child: Focus(
          autofocus: true,
          child: Scaffold(
            appBar: AppBar(
              title: const Text('Quick Recall'),
              leading: IconButton(
                icon: const Icon(Icons.close),
                tooltip: 'Leave round',
                onPressed: _confirmQuit,
              ),
            ),
            body: SafeArea(
              child: Center(
                child: ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 680),
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.fromLTRB(16, 8, 16, 24),
                    child: _unavailable
                        ? _unavailableView(c)
                        : Column(
                            crossAxisAlignment: CrossAxisAlignment.stretch,
                            children: [
                              _hud(c),
                              const SizedBox(height: 12),
                              _depthMeter(c),
                              const SizedBox(height: 14),
                              if (_phase == _Phase.countdown)
                                _countdown(c)
                              else
                                ..._questionArea(c),
                            ],
                          ),
                  ),
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _unavailableView(LingoColors c) {
    final text = Theme.of(context).textTheme;
    return Padding(
      padding: const EdgeInsets.only(top: 48),
      child: Column(
        children: [
          Icon(Icons.info_outline, size: 36, color: c.inkMuted),
          const SizedBox(height: 12),
          Text('Not enough words to play',
              textAlign: TextAlign.center, style: text.titleLarge),
          const SizedBox(height: 6),
          Text(
            'Quick Recall could not write questions from this word list. '
            'Try “Whole deck” instead.',
            textAlign: TextAlign.center,
            style: text.bodyMedium?.copyWith(color: c.inkMuted),
          ),
          const SizedBox(height: 18),
          FilledButton(
            onPressed: () => Navigator.of(context).pop(RecallExit.settings),
            child: const Text('Back'),
          ),
        ],
      ),
    );
  }

  Widget _hud(LingoColors c) {
    final text = Theme.of(context).textTheme;
    final streak = _round.streak;
    final flash = _flashText;
    return Row(
      children: [
        SizedBox(
          width: 76,
          height: 76,
          child: Stack(
            clipBehavior: Clip.none,
            alignment: Alignment.center,
            children: [
              ValueListenableBuilder<double>(
                valueListenable: _clock,
                builder: (context, remaining, _) =>
                    _ClockRing(remaining: remaining),
              ),
              if (_flashLeft > 0 && flash != null)
                Positioned(
                  right: -12,
                  top: -8,
                  child: _FlashChip(label: flash, good: _flashGood),
                ),
            ],
          ),
        ),
        const SizedBox(width: 16),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('${_round.correct}',
                  style: text.headlineLarge
                      ?.copyWith(fontWeight: FontWeight.w800, height: 1.05)),
              Text(_round.correct == 1 ? 'word recalled' : 'words recalled',
                  style: text.bodySmall),
            ],
          ),
        ),
        Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                StreakFlame(size: 28, lit: streak > 0),
                const SizedBox(width: 2),
                Text('$streak',
                    style: text.titleLarge
                        ?.copyWith(fontWeight: FontWeight.w800)),
              ],
            ),
            Text('bonus in ${_round.nextBonusIn}',
                style: text.bodySmall?.copyWith(color: c.inkMuted)),
          ],
        ),
      ],
    );
  }

  /// A slim bar for how deep the deepest right answer was, labelled with its
  /// rank.
  Widget _depthMeter(LingoColors c) {
    final text = Theme.of(context).textTheme;
    final reach = _round.reach;
    final top = _source.maxRank;
    final value = top <= 0 ? 0.0 : min(1.0, reach / top);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          children: [
            Text('Depth', style: text.bodySmall),
            const Spacer(),
            Text(reach == 0 ? 'Warming up' : recallReachLabel(reach),
                style: text.bodySmall?.copyWith(
                    color: c.inkMuted, fontWeight: FontWeight.w700)),
          ],
        ),
        const SizedBox(height: 4),
        ClipRRect(
          borderRadius: BorderRadius.circular(3),
          child: LinearProgressIndicator(
            value: value,
            minHeight: 6,
            backgroundColor: c.track,
            color: c.success,
          ),
        ),
      ],
    );
  }

  Widget _countdown(LingoColors c) {
    final text = Theme.of(context).textTheme;
    return SizedBox(
      height: 300,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Text('Get ready',
              style: text.titleMedium?.copyWith(color: c.inkMuted)),
          Text('$_countShown',
              style: text.displayLarge
                  ?.copyWith(fontWeight: FontWeight.w800, color: c.accent)),
        ],
      ),
    );
  }

  TileState _stateFor(RecallQuestion rq, int i) {
    final fb = _feedback;
    if (fb == null) return TileState.normal;
    if (rq.question.options[i].correct) return TileState.correct;
    if (i == fb.picked) return TileState.wrong;
    return TileState.dimmed;
  }

  List<Widget> _questionArea(LingoColors c) {
    final rq = _shown;
    if (rq == null) return const <Widget>[];
    final q = rq.question;
    final text = Theme.of(context).textTheme;
    final reading = rq.promptReading;
    final speak = q.speakPrompt;

    return [
      Container(
        padding: const EdgeInsets.fromLTRB(16, 12, 8, 12),
        decoration: BoxDecoration(
          color: c.raised,
          border: Border.all(color: c.hairline),
          borderRadius: BorderRadius.circular(6),
        ),
        child: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Text(
                    rq.targetPrompt
                        ? 'What does it mean?'
                        : 'Say it in ${widget.deck.languageName}',
                    textAlign: TextAlign.center,
                    style: text.bodySmall?.copyWith(color: c.inkMuted),
                  ),
                  const SizedBox(height: 4),
                  BidiText(
                    rq.promptText,
                    textAlign: TextAlign.center,
                    style: text.headlineMedium
                        ?.copyWith(fontWeight: FontWeight.w700),
                  ),
                  if (reading != null && reading.isNotEmpty)
                    Text(
                      reading,
                      textAlign: TextAlign.center,
                      style: text.bodyLarge?.copyWith(color: c.inkMuted),
                    ),
                ],
              ),
            ),
            if (speak != null)
              IconButton(
                tooltip: 'Listen',
                icon: Icon(Icons.volume_up_outlined, color: c.inkMuted),
                onPressed: () => _speak(speak, '${q.id}_prompt'),
              ),
          ],
        ),
      ),
      const SizedBox(height: 10),
      for (var i = 0; i < q.options.length; i++)
        Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: AnswerTile(
            letter: letterFor(i),
            text: q.options[i].text,
            state: _stateFor(rq, i),
            subtext: i < rq.optionReadings.length ? rq.optionReadings[i] : null,
            onTap: _feedback == null ? () => _answer(i) : null,
          ),
        ),
    ];
  }
}

/// The ring and the number of seconds left. Red in the last five seconds.
class _ClockRing extends StatelessWidget {
  const _ClockRing({required this.remaining});

  final double remaining;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final fraction = min(1.0, max(0.0, remaining / RecallRules.roundSeconds));
    final color = remaining <= 5
        ? kLadderWrong
        : (remaining <= 10 ? c.caution : c.accent);
    return SizedBox(
      width: 76,
      height: 76,
      child: Stack(
        alignment: Alignment.center,
        children: [
          SizedBox(
            width: 76,
            height: 76,
            child: CircularProgressIndicator(
              value: fraction,
              strokeWidth: 7,
              backgroundColor: c.track,
              color: color,
            ),
          ),
          Text('${remaining.ceil()}',
              style: text.headlineSmall
                  ?.copyWith(fontWeight: FontWeight.w800, color: color)),
        ],
      ),
    );
  }
}

/// "+3s" in green or "-3s" in red, next to the clock.
class _FlashChip extends StatelessWidget {
  const _FlashChip({required this.label, required this.good});

  final String label;
  final bool good;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 3),
      decoration: BoxDecoration(
        color: good ? c.success : kLadderWrong,
        borderRadius: BorderRadius.circular(10),
      ),
      child: Text(label,
          style: TextStyle(
              color: good ? c.onSuccess : Colors.white,
              fontSize: 12,
              fontWeight: FontWeight.w800)),
    );
  }
}
