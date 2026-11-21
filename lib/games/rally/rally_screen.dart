import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../../audio/tts_service.dart';
import '../../data/app_settings.dart';
import '../../data/models.dart';
import '../../difficult/difficult_words_service.dart';
import '../../difficult/word_trouble.dart';
import '../../feedback/feedback_service.dart';
import '../../progress/progress_models.dart';
import '../../progress/progress_service.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../ladder/ladder_widgets.dart';
import 'rally_court.dart';
import 'rally_match.dart';
import 'rally_models.dart';
import 'rally_questions.dart';
import 'rally_result_view.dart';
import 'rally_stats.dart';

enum _Phase { flight, reveal, over }

/// One match of Lingo Rally.
///
/// The ball always travels towards whoever has to answer, and its flight is the
/// clock: when it reaches the paddle, time is up. Answer in time and it goes
/// back; fail and it sails past.
///
/// Pops with a [RallyExit] telling the lobby what to do next.
class RallyScreen extends StatefulWidget {
  const RallyScreen({
    super.key,
    required this.deck,
    required this.bot,
    required this.rules,
    required this.pool,
    required this.stats,
  });

  final Deck deck;
  final BotProfile bot;
  final RallyRules rules;
  final RallyPool pool;
  final RallyStats stats;

  @override
  State<RallyScreen> createState() => _RallyScreenState();
}

class _RallyScreenState extends State<RallyScreen>
    with SingleTickerProviderStateMixin {
  final Random _rnd = Random();
  late final RallyMatch _match = RallyMatch(rules: widget.rules);
  late final RallyQuestionSource _source =
      RallyQuestionSource(widget.deck, widget.pool, _rnd);
  late final AnimationController _ball = AnimationController(vsync: this)
    ..addStatusListener(_onBallStatus);

  late final ProgressSession _session = ProgressSession(
      startLevel: context.read<ProgressService>().level.level);

  bool _started = false;
  _Phase _phase = _Phase.flight;
  late RallyQuestion _rq;
  double _limit = 9;
  bool _smash = false;
  BotAnswer? _plan;
  int? _picked;
  int? _botPick;
  bool _youTimedOut = false;

  // Ball path.
  double _segFrom = 0.5;
  double _segTo = 0.5;
  double _pathPhase = 0;
  RallySide _towards = RallySide.you;

  // Goal flash and banner.
  RallySide? _missed;
  double _flash = 0;
  Timer? _flashTimer;
  String? _banner;
  Color _bannerColor = Colors.white;
  Timer? _bannerTimer;

  Timer? _revealTimer;
  bool _paused = false;
  bool _showResults = false;
  bool _recorded = false;

  final List<RallyQuestion> _missedByYou = [];
  final List<double> _yourTimes = [];

  @override
  void dispose() {
    _ball.dispose();
    _revealTimer?.cancel();
    _flashTimer?.cancel();
    _bannerTimer?.cancel();
    super.dispose();
  }

  // --- Round flow ------------------------------------------------------------

  double _paddleX(RallySide s) =>
      s == RallySide.you ? RallyCourtPainter.youX : RallyCourtPainter.botX;

  double get _ballX => _segFrom + (_segTo - _segFrom) * _ball.value;

  /// The Start button: the first ball.
  void _begin() {
    _prepareRound();
    setState(() => _started = true);
    _speakIfYours();
  }

  void _startRound() {
    if (!mounted) return;
    _prepareRound();
    setState(() {});
    _speakIfYours();
  }

  void _speakIfYours() {
    if (_towards == RallySide.you) _speakPrompt();
  }

  /// Write the next question and send the ball towards the side that answers.
  /// The ball always starts at the other side's paddle: that is where it was
  /// last hit, or where it is served from after a point.
  void _prepareRound() {
    final side = _match.toAnswer;
    final rq = _source.next();
    final limit = _match.limitFor(phrase: rq.phrase);
    final smash = _match.smashIncoming;

    _rq = rq;
    _limit = limit;
    _smash = smash;
    _picked = null;
    _botPick = null;
    _youTimedOut = false;
    _missed = null;
    _flash = 0;
    _towards = side;
    _phase = _Phase.flight;
    if (_match.rallyLength == 0) _pathPhase = _rnd.nextDouble() * 2;

    var seconds = limit;
    if (side == RallySide.bot) {
      final plan = botAnswer(widget.bot,
          limit: limit, smashed: smash, rnd: _rnd, phrase: rq.phrase);
      _plan = plan;
      seconds = plan.seconds;
      // The bot's wrong answer, chosen now so it can be shown at the end.
      if (!plan.correct && !plan.timedOut) {
        final wrong = [
          for (var i = 0; i < rq.question.options.length; i++)
            if (!rq.question.options[i].correct) i,
        ];
        _botPick = wrong[_rnd.nextInt(wrong.length)];
      }
    } else {
      _plan = null;
    }

    _segFrom = _paddleX(side.other);
    _segTo = _paddleX(side);
    _ball
      ..duration = Duration(milliseconds: max(200, (seconds * 1000).round()))
      ..forward(from: 0);
  }

  void _onBallStatus(AnimationStatus status) {
    if (status != AnimationStatus.completed || _phase != _Phase.flight) return;
    if (_towards == RallySide.you) {
      // Out of time.
      _youTimedOut = true;
      _resolve(correct: false, seconds: _limit);
    } else {
      final plan = _plan!;
      _resolve(correct: plan.correct, seconds: plan.seconds);
    }
  }

  void _answer(int i) {
    if (!_started || _phase != _Phase.flight || _towards != RallySide.you || _paused) {
      return;
    }
    final seconds = _ball.value * _limit;
    _ball.stop();
    _picked = i;
    _resolve(correct: _rq.question.options[i].correct, seconds: seconds);
  }

  void _resolve({required bool correct, required double seconds}) {
    if (_phase != _Phase.flight) return;
    final side = _towards;
    final fromX = _ballX;
    final events = _match.answer(correct: correct, seconds: seconds, limit: _limit);

    if (side == RallySide.you) {
      context.read<FeedbackService>().onQuickAnswer(correct: correct);
      _yourTimes.add(seconds);
      if (!correct) _missedByYou.add(_rq);
      // A phrase question is about a sentence, not one word.
      if (!_rq.phrase) {
        context.read<DifficultWordsService>().record(
              deckId: widget.deck.id,
              cardId: _rq.cardId,
              correct: correct,
              source: AnswerSource.rally,
            );
      }
    }

    // The ball finishes its journey: back off the paddle, or through it.
    final missed = events.any((e) => e.type == RallyEventType.missed);
    _segFrom = fromX;
    _segTo = missed
        ? (side == RallySide.you ? -0.08 : 1.08)
        : _paddleX(side);
    _ball
      ..duration = const Duration(milliseconds: 320)
      ..forward(from: 0);

    _phase = _Phase.reveal;
    if (missed) {
      _missed = side;
      _flashGoal();
    }
    _announce(events);

    final over = _match.isOver;
    if (over) _recordOnce();
    setState(() {});

    if (side == RallySide.you && context.read<AppSettings>().autoPlayWord) {
      final q = _rq.question;
      final say = q.optionsAreTarget ? q.correctOption.speak : null;
      if (say != null) _speak(say, '${q.id}_reveal', warn: false);
    }

    final hold = over
        ? 1500
        : (side == RallySide.you && !correct)
            ? 2000
            : 1150;
    _revealTimer?.cancel();
    _revealTimer = Timer(Duration(milliseconds: hold), _afterReveal);
  }

  void _afterReveal() {
    if (!mounted) return;
    _revealTimer?.cancel();
    if (_match.isOver) {
      setState(() {
        _phase = _Phase.over;
        _showResults = true;
      });
      return;
    }
    _startRound();
  }

  /// Enter or a tap while an answer is on show: carry on now.
  void _skipReveal() {
    if (_phase == _Phase.reveal && !_paused) _afterReveal();
  }

  void _flashGoal() {
    _flash = 1;
    _flashTimer?.cancel();
    _flashTimer = Timer.periodic(const Duration(milliseconds: 60), (t) {
      if (!mounted) return t.cancel();
      setState(() => _flash = max(0, _flash - 0.1));
      if (_flash <= 0) t.cancel();
    });
  }

  void _announce(List<RallyEvent> events) {
    final c = context.lingo;
    String? text;
    Color color = c.accent;
    for (final e in events) {
      final mine = e.side == RallySide.you;
      switch (e.type) {
        case RallyEventType.blast:
          text = mine ? 'BLAST! −1 life for ${widget.bot.name}' : '${widget.bot.name} BLAST! −1 life';
          color = kRallySmash;
        case RallyEventType.smashEarned:
          text = mine ? 'SMASH! Next ball is fast' : '${widget.bot.name} charges a SMASH';
          color = kRallySmash;
        case RallyEventType.shieldEarned:
          text = mine ? 'SHIELD! Your next miss is free' : '${widget.bot.name} earns a shield';
          color = c.success;
        case RallyEventType.shieldUsed:
          text = mine ? 'Shield saved you!' : '${widget.bot.name}’s shield held';
          color = c.success;
        case RallyEventType.missed:
          final who = mine ? widget.bot.name : 'You';
          text = e.smash
              ? '$who score${mine ? 's' : ''} ${e.points} (smash!)'
              : '$who score${mine ? 's' : ''}!';
          color = mine ? kRallyBot : c.accent;
        case RallyEventType.smashBlocked:
          text = mine ? 'Smash returned!' : '${widget.bot.name} returns your smash';
          color = c.success;
        default:
          break;
      }
    }
    _banner = text;
    _bannerColor = color;
    _bannerTimer?.cancel();
    if (text != null) {
      _bannerTimer = Timer(const Duration(milliseconds: 1500), () {
        if (mounted) setState(() => _banner = null);
      });
    }
  }

  void _recordOnce() {
    if (_recorded) return;
    _recorded = true;
    widget.stats.record(_match, widget.bot);
    widget.stats.save(widget.deck.language);

    final tier = BotProfile.all.indexWhere((b) => b.id == widget.bot.id);
    final you = _match.you;
    _session.add(context.read<ProgressService>().record(ProgressEvent.rally(
          won: _match.winner == RallySide.you,
          correct: you.correct,
          botTier: tier < 0 ? 0 : tier,
          bestStreak: you.bestStreak,
          blasts: you.blastsLanded,
          smashes: you.smashesEarned,
          deckId: widget.deck.id,
        )));
  }

  // --- Speech ----------------------------------------------------------------

  Future<void> _speak(String text, String id, {bool warn = true}) async {
    final tts = context.read<TtsService>();
    await tts.speak(text, id: id);
    if (warn && tts.lastSpeakFailed && mounted) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text('No voice available for ${widget.deck.languageName} on '
            'this device. Add a neural voice key in Settings for audio.'),
      ));
    }
  }

  void _speakPrompt() {
    final q = _rq.question;
    if (q.speakPrompt == null) return;
    if (!context.read<AppSettings>().autoPlayWord) return;
    _speak(q.speakPrompt!, '${q.id}_prompt', warn: false);
  }

  // --- Quitting --------------------------------------------------------------

  Future<void> _confirmQuit() async {
    if (!_started || _showResults || _match.isOver) {
      Navigator.of(context).pop(RallyExit.home);
      return;
    }
    _pause();
    final quit = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Leave the match?'),
        content: const Text('The match will end and won’t be counted.'),
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
    if (quit == true) {
      Navigator.of(context).pop(RallyExit.home);
    } else {
      _resume();
    }
  }

  void _pause() {
    _paused = true;
    _ball.stop(canceled: false);
    _revealTimer?.cancel();
  }

  void _resume() {
    _paused = false;
    if (_phase == _Phase.flight) {
      _ball.forward();
    } else if (_phase == _Phase.reveal) {
      _ball.forward();
      _revealTimer = Timer(const Duration(milliseconds: 600), _afterReveal);
    }
    setState(() {});
  }

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

  // --- Build -----------------------------------------------------------------

  CourtFrame _frame() => CourtFrame(
        ballX: _ballX,
        phase: _pathPhase,
        towards: _towards,
        smash: _smash,
        missed: _missed,
        flash: _flash,
        youShield: _match.you.shield,
        botShield: _match.bot.shield,
        youCharged: _match.smashIncoming && _match.toAnswer == RallySide.bot,
        botCharged: _match.smashIncoming && _match.toAnswer == RallySide.you,
      );

  @override
  Widget build(BuildContext context) {
    if (_showResults) {
      return RallyResultView(
        deck: widget.deck,
        match: _match,
        bot: widget.bot,
        stats: widget.stats,
        session: _session,
        missed: _missedByYou,
        averageSeconds: _yourTimes.isEmpty
            ? null
            : _yourTimes.reduce((a, b) => a + b) / _yourTimes.length,
        onSpeak: (t, id) => _speak(t, id),
      );
    }

    final c = context.lingo;
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _confirmQuit();
      },
      child: CallbackShortcuts(
        bindings: {
          for (var i = 0; i < _letterKeys.length; i++) ...{
            SingleActivator(_letterKeys[i]): () => _answer(i),
            SingleActivator(_digitKeys[i]): () => _answer(i),
          },
          const SingleActivator(LogicalKeyboardKey.enter): _skipReveal,
          const SingleActivator(LogicalKeyboardKey.space): _skipReveal,
        },
        child: Focus(
          autofocus: true,
          child: Scaffold(
            appBar: AppBar(
              title: const Text('Lingo Rally'),
              leading: IconButton(
                icon: const Icon(Icons.close),
                tooltip: 'Leave match',
                onPressed: _confirmQuit,
              ),
            ),
            body: SafeArea(
              child: Center(
                child: ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 680),
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.fromLTRB(16, 4, 16, 24),
                    child: AnimatedBuilder(
                      animation: _ball,
                      builder: (context, _) => Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: _started ? [
                          _hud(c),
                          const SizedBox(height: 10),
                          Stack(
                            alignment: Alignment.center,
                            children: [
                              RallyCourt(frame: _frame()),
                              if (_banner != null) _bannerChip(),
                            ],
                          ),
                          const SizedBox(height: 8),
                          _clock(c),
                          const SizedBox(height: 10),
                          _questionArea(c),
                        ] : _intro(c),
                      ),
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

  List<Widget> _intro(LingoColors c) {
    final text = Theme.of(context).textTheme;
    return [
      _hud(c),
      const SizedBox(height: 10),
      RallyCourt(frame: _frame()),
      const SizedBox(height: 18),
      Text('${widget.bot.name} · ${widget.bot.tagline}', style: text.titleMedium),
      const SizedBox(height: 6),
      Text(
        'First to ${widget.rules.targetScore} points wins, or run '
        '${widget.bot.name} out of lives. The ball flies to whoever has to '
        'answer: pick the right translation before it arrives and it goes back. '
        'Get it wrong and the other side scores.',
        style: text.bodyMedium?.copyWith(color: c.inkMuted, height: 1.4),
      ),
      const SizedBox(height: 18),
      FilledButton(onPressed: _begin, child: const Text('Serve')),
    ];
  }

  Widget _bannerChip() => Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
        decoration: BoxDecoration(
          color: _bannerColor.withValues(alpha: 0.92),
          borderRadius: BorderRadius.circular(20),
        ),
        child: Text(_banner!,
            textAlign: TextAlign.center,
            style: const TextStyle(
                color: Colors.white, fontWeight: FontWeight.w800, fontSize: 14)),
      );

  Widget _hud(LingoColors c) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Expanded(
          child: _SideHud(
            name: 'You',
            color: c.accent,
            state: _match.you,
            maxLives: widget.rules.lives,
            charged: _match.smashIncoming && _match.toAnswer == RallySide.bot,
            alignEnd: false,
          ),
        ),
        Padding(
          padding: const EdgeInsets.fromLTRB(8, 6, 8, 0),
          child: Column(
            children: [
              Text('First to', style: Theme.of(context).textTheme.bodySmall),
              Text('${widget.rules.targetScore}',
                  style: Theme.of(context).textTheme.titleLarge),
            ],
          ),
        ),
        Expanded(
          child: _SideHud(
            name: widget.bot.name,
            color: kRallyBot,
            state: _match.bot,
            maxLives: widget.rules.lives,
            charged: _match.smashIncoming && _match.toAnswer == RallySide.you,
            alignEnd: true,
          ),
        ),
      ],
    );
  }

  /// A thin bar that drains while it is your ball, plus a line saying whose
  /// ball it is.
  Widget _clock(LingoColors c) {
    final yours = _towards == RallySide.you;
    final inFlight = _phase == _Phase.flight;
    final left = yours && inFlight ? (1 - _ball.value).clamp(0.0, 1.0) : 0.0;
    final label = switch (_phase) {
      _Phase.flight when yours => _smash ? 'Smash coming — quick!' : 'Your ball — answer!',
      _Phase.flight => '${widget.bot.name} is answering…',
      _ => _youTimedOut ? 'Out of time' : '',
    };
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        ClipRRect(
          borderRadius: BorderRadius.circular(3),
          child: LinearProgressIndicator(
            value: left,
            minHeight: 5,
            backgroundColor: c.track,
            color: left < 0.3 ? kLadderWrong : (_smash ? kRallySmash : c.accent),
          ),
        ),
        const SizedBox(height: 4),
        SizedBox(
          height: 18,
          child: Text(label,
              style: Theme.of(context)
                  .textTheme
                  .bodySmall
                  ?.copyWith(color: c.inkMuted)),
        ),
      ],
    );
  }

  Widget _questionArea(LingoColors c) {
    final q = _rq.question;
    final text = Theme.of(context).textTheme;
    final revealing = _phase != _Phase.flight;
    final yours = _towards == RallySide.you;
    final target = q.promptIsTarget;

    TileState stateFor(int i) {
      final o = q.options[i];
      if (revealing) {
        if (o.correct) return TileState.correct;
        if (i == _picked || i == _botPick) return TileState.wrong;
        return TileState.dimmed;
      }
      return TileState.normal;
    }

    return GestureDetector(
      behavior: HitTestBehavior.translucent,
      onTap: revealing ? _skipReveal : null,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: c.raised,
              border: Border.all(color: c.hairline),
              borderRadius: BorderRadius.circular(6),
            ),
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.stretch,
                    children: [
                      Directionality(
                        textDirection: target && widget.deck.rtl
                            ? TextDirection.rtl
                            : TextDirection.ltr,
                        child: Text(
                          q.prompt,
                          textAlign: target && widget.deck.rtl
                              ? TextAlign.right
                              : TextAlign.start,
                          style: (_rq.phrase ? text.titleLarge : text.headlineSmall)
                              ?.copyWith(height: 1.3),
                        ),
                      ),
                      // The reading (pinyin, kana, romanised Korean) of a word
                      // whose script does not show how it is said.
                      if (q.detail != null && q.detail!.isNotEmpty)
                        Padding(
                          padding: const EdgeInsets.only(top: 4),
                          child: Text(
                            q.detail!,
                            style: text.bodyMedium?.copyWith(
                                color: c.inkMuted, fontStyle: FontStyle.italic),
                          ),
                        ),
                    ],
                  ),
                ),
                if (q.speakPrompt != null)
                  IconButton(
                    tooltip: 'Listen',
                    icon: Icon(Icons.volume_up_outlined, color: c.inkMuted),
                    onPressed: () => _speak(q.speakPrompt!, '${q.id}_prompt'),
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
                state: stateFor(i),
                subtext: revealing ? q.options[i].translation : null,
                onTap: (!revealing && yours) ? () => _answer(i) : null,
                onSpeak: revealing && q.optionsAreTarget && q.options[i].speak != null
                    ? () => _speak(q.options[i].speak!, '${q.id}_o$i')
                    : null,
              ),
            ),
          if (revealing && !_match.isOver)
            Padding(
              padding: const EdgeInsets.only(top: 2),
              child: Text(
                q.explanation == null
                    ? 'Tap or press Enter to continue'
                    : '${q.explanation}${q.explanationEn == null ? '' : '\n${q.explanationEn}'}',
                style: text.bodySmall?.copyWith(color: c.inkMuted, height: 1.4),
              ),
            ),
        ],
      ),
    );
  }
}

/// One side's lives, score and power-up chips.
class _SideHud extends StatelessWidget {
  const _SideHud({
    required this.name,
    required this.color,
    required this.state,
    required this.maxLives,
    required this.charged,
    required this.alignEnd,
  });

  final String name;
  final Color color;
  final SideState state;
  final int maxLives;
  final bool charged;
  final bool alignEnd;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final cross = alignEnd ? CrossAxisAlignment.end : CrossAxisAlignment.start;
    return Column(
      crossAxisAlignment: cross,
      children: [
        Text(name,
            maxLines: 1,
            overflow: TextOverflow.ellipsis,
            style: text.titleSmall?.copyWith(color: color, fontWeight: FontWeight.w700)),
        Text('${state.score}', style: text.headlineMedium?.copyWith(height: 1.1)),
        const SizedBox(height: 2),
        Wrap(
          alignment: alignEnd ? WrapAlignment.end : WrapAlignment.start,
          spacing: 1,
          children: [
            for (var i = 0; i < maxLives; i++)
              Icon(i < state.lives ? Icons.favorite : Icons.favorite_border,
                  size: 15, color: i < state.lives ? kLadderWrong : c.inkMuted),
          ],
        ),
        const SizedBox(height: 4),
        Wrap(
          alignment: alignEnd ? WrapAlignment.end : WrapAlignment.start,
          spacing: 6,
          runSpacing: 4,
          children: [
            if (state.streak >= 2) _Chip(Icons.local_fire_department, '${state.streak}', c.caution),
            if (state.shield) _Chip(Icons.shield, 'Shield', c.success),
            if (charged) const _Chip(Icons.bolt, 'Smash', kRallySmash),
          ],
        ),
      ],
    );
  }
}

class _Chip extends StatelessWidget {
  const _Chip(this.icon, this.label, this.color);

  final IconData icon;
  final String label;
  final Color color;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.16),
        borderRadius: BorderRadius.circular(10),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(icon, size: 13, color: color),
          const SizedBox(width: 3),
          Text(label,
              style: TextStyle(color: color, fontSize: 11, fontWeight: FontWeight.w700)),
        ],
      ),
    );
  }
}
