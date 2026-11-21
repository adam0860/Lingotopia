import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../audio/tts_service.dart';
import '../../data/app_settings.dart';
import '../../data/models.dart';
import '../../difficult/difficult_words_service.dart';
import '../../difficult/word_trouble.dart';
import '../../feedback/feedback_service.dart';
import '../../lessons/bidi.dart';
import '../../progress/progress_models.dart';
import '../../progress/progress_service.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../ladder/ladder_widgets.dart' show kLadderWrong;
import 'match_game.dart';
import 'match_result_view.dart';
import 'match_stats.dart';

/// One run of Word Match: [MatchLength.boards] boards against the clock.
///
/// The clock counts up from the moment the player presses Start. A wrong pick
/// adds three seconds, shown on the clock straight away. Leaving part way asks
/// first and then records nothing and earns nothing.
///
/// Pops with a [MatchExit] telling the lobby what to do next.
class MatchScreen extends StatefulWidget {
  const MatchScreen({
    super.key,
    required this.deck,
    required this.pool,
    required this.length,
    required this.stats,
  });

  final Deck deck;
  final MatchPool pool;
  final MatchLength length;
  final WordMatchStats stats;

  @override
  State<MatchScreen> createState() => _MatchScreenState();
}

class _MatchScreenState extends State<MatchScreen>
    with SingleTickerProviderStateMixin {
  late final MatchGame _game;
  late final ProgressSession _session;

  /// Drives the red flash and shake on a wrong pick.
  late final AnimationController _flash;

  final Stopwatch _watch = Stopwatch();

  /// Milliseconds on the clock, before penalties. Only the clock text listens
  /// to it, so ten updates a second rebuild one small widget.
  final ValueNotifier<int> _elapsed = ValueNotifier<int>(0);

  Timer? _ticker;
  Timer? _advanceTimer;

  bool _started = false;
  bool _showResults = false;
  bool _recorded = false;

  /// The two tiles of the last wrong pick, while they flash.
  int? _flashLeft;
  int? _flashRight;

  MatchResult? _result;
  int? _previousBest;
  bool _newBest = false;
  bool _ranked = true;

  @override
  void initState() {
    super.initState();
    _game = MatchGame(
      deck: widget.deck,
      pool: widget.pool,
      boards: widget.length.boards,
    );
    _session = ProgressSession(
        startLevel: context.read<ProgressService>().level.level);
    _flash = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 460),
    )..addStatusListener(_onFlashStatus);
  }

  @override
  void dispose() {
    _ticker?.cancel();
    _advanceTimer?.cancel();
    _watch.stop();
    _flash.dispose();
    _elapsed.dispose();
    super.dispose();
  }

  // --- Flow ------------------------------------------------------------------

  /// The Start button: the first board appears and the clock starts.
  void _begin() {
    if (_started || !_game.isPlayable) return;
    _watch
      ..reset()
      ..start();
    _ticker = Timer.periodic(const Duration(milliseconds: 100), (_) {
      _elapsed.value = _watch.elapsedMilliseconds;
    });
    setState(() => _started = true);
  }

  void _onFlashStatus(AnimationStatus status) {
    if (status != AnimationStatus.completed || !mounted) return;
    setState(() {
      _flashLeft = null;
      _flashRight = null;
    });
  }

  void _tap(MatchSide side, int row) {
    if (!_started || _showResults) return;
    final pick = _game.pick(side, row);
    switch (pick.outcome) {
      case MatchOutcome.ignored:
        return;
      case MatchOutcome.selected:
      case MatchOutcome.deselected:
        setState(() {});
      case MatchOutcome.wrong:
        _onWrong(pick);
      case MatchOutcome.matched:
        _onMatched(pick);
    }
  }

  /// Words already missed on the board in play. A word counts once per board:
  /// one bad tap, however many, is one miss; a clean match is one hit.
  final Set<String> _missedOnBoard = {};

  void _onWrong(MatchPick pick) {
    context.read<FeedbackService>().onQuickAnswer(correct: false);
    // The word tile is the one being translated, so it carries the miss (the
    // meaning it was wrongly joined to may be perfectly well known).
    final row = pick.leftRow;
    if (row != null) {
      final card = _game.board.pairAt(MatchSide.left, row).card;
      if (_missedOnBoard.add(card.id)) {
        context.read<DifficultWordsService>().record(
              deckId: widget.deck.id,
              cardId: card.id,
              correct: false,
              source: AnswerSource.match,
            );
      }
    }
    _elapsed.value = _watch.elapsedMilliseconds;
    setState(() {
      _flashLeft = pick.leftRow;
      _flashRight = pick.rightRow;
    });
    _flash.forward(from: 0);
  }

  void _onMatched(MatchPick pick) {
    final pair = pick.pair;
    if (pair != null && !_missedOnBoard.contains(pair.card.id)) {
      context.read<DifficultWordsService>().record(
            deckId: widget.deck.id,
            cardId: pair.card.id,
            correct: true,
            source: AnswerSource.match,
          );
    }
    if (pair != null) {
      if (context.read<AppSettings>().autoPlayWord) {
        unawaited(_speak(pair.card.speakableLemma, 'match_${pair.card.id}',
            warn: false));
      } else {
        context.read<FeedbackService>().onQuickAnswer(correct: true);
      }
    }
    if (pick.finished) {
      _finish();
    } else if (pick.boardCleared) {
      _advanceTimer?.cancel();
      _advanceTimer = Timer(const Duration(milliseconds: 380), () {
        if (!mounted) return;
        if (_game.nextBoard()) {
          setState(() {
            _flashLeft = null;
            _flashRight = null;
          });
        }
      });
    }
    setState(() {});
  }

  /// The last pair of the last board: stop the clock, count the run, and show
  /// the result a moment later.
  void _finish() {
    _watch.stop();
    _ticker?.cancel();
    _elapsed.value = _watch.elapsedMilliseconds;
    _recordOnce();
    _advanceTimer?.cancel();
    _advanceTimer = Timer(const Duration(milliseconds: 900), () {
      if (mounted) setState(() => _showResults = true);
    });
  }

  /// Stats and XP for a finished run, exactly once. An abandoned run never
  /// gets here.
  void _recordOnce() {
    if (_recorded) return;
    _recorded = true;

    final result = _game.result(_watch.elapsedMilliseconds);
    // A run cut short by a small word list is not comparable with the others.
    final ranked = _game.boardCount == widget.length.boards;
    final previous = widget.stats.bestTimeMs[widget.length.id];
    final best = widget.stats.record(
      lengthId: widget.length.id,
      timeMs: result.finalMs,
      boards: result.boards,
      flawless: result.flawless,
      ranked: ranked,
    );
    unawaited(widget.stats.save(widget.deck.language));

    _session.add(context.read<ProgressService>().record(ProgressEvent.wordMatch(
          boards: result.boards,
          pairs: result.pairs,
          flawless: result.flawless,
          finished: true,
          deckId: widget.deck.id,
        )));

    _result = result;
    _previousBest = previous;
    _newBest = best;
    _ranked = ranked;
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

  // --- Quitting --------------------------------------------------------------

  Future<void> _confirmQuit() async {
    if (_game.isFinished && _result != null) {
      // The run is already counted: go straight to the result.
      _advanceTimer?.cancel();
      setState(() => _showResults = true);
      return;
    }
    if (!_started || _showResults) {
      Navigator.of(context).pop(MatchExit.settings);
      return;
    }
    _watch.stop();
    final quit = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Leave the game?'),
        content: const Text('The run will end and won’t be counted.'),
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
      Navigator.of(context).pop(MatchExit.settings);
    } else if (!_game.isFinished) {
      _watch.start();
    }
  }

  // --- Build -----------------------------------------------------------------

  @override
  Widget build(BuildContext context) {
    final result = _result;
    if (_showResults && result != null) {
      return MatchResultView(
        deck: widget.deck,
        result: result,
        length: widget.length,
        stats: widget.stats,
        session: _session,
        previousBest: _previousBest,
        newBest: _newBest,
        ranked: _ranked,
        onSpeak: (t, id) => _speak(t, id),
      );
    }

    final c = context.lingo;
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _confirmQuit();
      },
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Word Match'),
          leading: IconButton(
            icon: const Icon(Icons.close),
            tooltip: 'Leave game',
            onPressed: _confirmQuit,
          ),
        ),
        body: SafeArea(
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 680),
              child: !_game.isPlayable
                  ? _empty(c)
                  : (_started ? _playing(c) : _intro(c)),
            ),
          ),
        ),
      ),
    );
  }

  Widget _empty(LingoColors c) {
    final text = Theme.of(context).textTheme;
    return Padding(
      padding: const EdgeInsets.all(24),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Icon(Icons.grid_view_outlined, size: 36, color: c.inkMuted),
          const SizedBox(height: 12),
          Text(
            'There are not enough words in this list to build a board. '
            'Choose a bigger list and try again.',
            textAlign: TextAlign.center,
            style: text.bodyMedium?.copyWith(color: c.inkMuted, height: 1.4),
          ),
          const SizedBox(height: 18),
          FilledButton(
            onPressed: () => Navigator.of(context).pop(MatchExit.settings),
            child: const Text('Back'),
          ),
        ],
      ),
    );
  }

  Widget _intro(LingoColors c) {
    final text = Theme.of(context).textTheme;
    final boards = _game.boardCount;
    const secs = MatchGame.missPenaltyMs ~/ 1000;
    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.fromLTRB(20, 8, 20, 28),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: c.raised,
                border: Border.all(color: c.hairline),
                borderRadius: BorderRadius.circular(6),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                      '${widget.length.label} · $boards '
                      '${boards == 1 ? 'board' : 'boards'}',
                      style: text.bodySmall),
                  const SizedBox(height: 8),
                  Text(
                    'Pick a word, then its meaning. A right pair locks in; a '
                    'wrong one adds $secs seconds to your time.',
                    style: text.titleLarge?.copyWith(height: 1.3),
                  ),
                  const SizedBox(height: 10),
                  Text(
                    'The clock starts when you press Start.',
                    style: text.bodyMedium?.copyWith(color: c.inkMuted),
                  ),
                  if (boards < widget.length.boards) ...[
                    const SizedBox(height: 10),
                    Text(
                      'This word list only has enough words for $boards '
                      '${boards == 1 ? 'board' : 'boards'}, so this run will '
                      'not count towards your best times.',
                      style: text.bodySmall,
                    ),
                  ],
                ],
              ),
            ),
            const SizedBox(height: 18),
            FilledButton(onPressed: _begin, child: const Text('Start')),
          ],
        ),
      ),
    );
  }

  Widget _playing(LingoColors c) {
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 4, 16, 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          _hud(),
          const SizedBox(height: 8),
          _progressRow(c),
          const SizedBox(height: 10),
          Expanded(child: ClipRect(child: _board())),
        ],
      ),
    );
  }

  Widget _hud() {
    final text = Theme.of(context).textTheme;
    final misses = _game.misses;
    final penaltySeconds = _game.penaltyMs ~/ 1000;
    final timeStyle = text.headlineSmall?.copyWith(
      fontFeatures: const [FontFeature.tabularFigures()],
    );
    return Row(
      children: [
        Expanded(
          child: _Stat(
            label: 'Board',
            value: '${_game.boardIndex + 1}/${_game.boardCount}',
          ),
        ),
        Expanded(
          flex: 2,
          child: ValueListenableBuilder<int>(
            valueListenable: _elapsed,
            builder: (context, ms, _) => _Stat(
              label: 'Time',
              value: formatMatchTime(ms + _game.penaltyMs),
              style: timeStyle,
            ),
          ),
        ),
        Expanded(
          child: _Stat(
            label: misses == 0 ? 'Misses' : 'Misses · +${penaltySeconds}s',
            value: '$misses',
            color: misses > 0 ? kLadderWrong : null,
          ),
        ),
      ],
    );
  }

  /// A thin bar of pairs matched so far, and the combo flame once it is
  /// running. The flame has a slot of its own so the bar does not jump.
  Widget _progressRow(LingoColors c) {
    final total = max(1, _game.totalPairs);
    return SizedBox(
      height: 26,
      child: Row(
        children: [
          Expanded(
            child: ClipRRect(
              borderRadius: BorderRadius.circular(3),
              child: LinearProgressIndicator(
                value: _game.pairsMatched / total,
                minHeight: 5,
                backgroundColor: c.track,
                color: c.accent,
              ),
            ),
          ),
          SizedBox(
            width: 68,
            child: Align(
              alignment: Alignment.centerRight,
              child: _game.combo >= 3 ? _ComboChip(_game.combo) : null,
            ),
          ),
        ],
      ),
    );
  }

  Widget _board() {
    return TweenAnimationBuilder<double>(
      // A new key per board: each board slides in from the right.
      key: ValueKey<int>(_game.boardIndex),
      tween: Tween<double>(begin: 1, end: 0),
      duration: const Duration(milliseconds: 280),
      curve: Curves.easeOutCubic,
      builder: (context, t, child) =>
          FractionalTranslation(translation: Offset(t, 0), child: child),
      child: _BoardView(
        game: _game,
        deck: widget.deck,
        flashLeft: _flashLeft,
        flashRight: _flashRight,
        flash: _flash,
        onTap: _tap,
      ),
    );
  }
}

// --- Board ------------------------------------------------------------------

enum _TileState { normal, selected, matched }

/// Both columns of the board in play.
class _BoardView extends StatelessWidget {
  const _BoardView({
    required this.game,
    required this.deck,
    required this.flashLeft,
    required this.flashRight,
    required this.flash,
    required this.onTap,
  });

  final MatchGame game;
  final Deck deck;
  final int? flashLeft;
  final int? flashRight;
  final Animation<double> flash;
  final void Function(MatchSide side, int row) onTap;

  static const double _gap = 8;

  @override
  Widget build(BuildContext context) {
    final n = game.board.size;
    return LayoutBuilder(builder: (context, box) {
      // Fill the height when it allows; on a short screen keep the tiles
      // comfortable to hit and let the board scroll instead.
      final fit = (box.maxHeight - _gap * (n - 1)) / n;
      final tileHeight = max(60.0, min(96.0, fit));
      final total = tileHeight * n + _gap * (n - 1);
      final grid = SizedBox(
        height: total,
        child: Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Expanded(child: _column(MatchSide.left, tileHeight)),
            const SizedBox(width: 12),
            Expanded(child: _column(MatchSide.right, tileHeight)),
          ],
        ),
      );
      if (total > box.maxHeight) return SingleChildScrollView(child: grid);
      return Align(alignment: Alignment.topCenter, child: grid);
    });
  }

  Widget _column(MatchSide side, double tileHeight) {
    final board = game.board;
    final flashRow = side == MatchSide.left ? flashLeft : flashRight;
    return Column(
      children: [
        for (var row = 0; row < board.size; row++) ...[
          if (row > 0) const SizedBox(height: _gap),
          SizedBox(
            height: tileHeight,
            child: _MatchTile(
              side: side,
              pair: board.pairAt(side, row),
              rtl: deck.rtl,
              state: game.isMatched(side, row)
                  ? _TileState.matched
                  : (game.selectedRow(side) == row
                      ? _TileState.selected
                      : _TileState.normal),
              flash: (flashRow == row && !game.isMatched(side, row))
                  ? flash
                  : null,
              onTap: () => onTap(side, row),
            ),
          ),
        ],
      ],
    );
  }
}

/// One tile: a word (left) or its meaning (right).
class _MatchTile extends StatelessWidget {
  const _MatchTile({
    required this.side,
    required this.pair,
    required this.rtl,
    required this.state,
    required this.flash,
    required this.onTap,
  });

  final MatchSide side;
  final MatchPair pair;
  final bool rtl;
  final _TileState state;

  /// Set while this tile is flashing red after a wrong pick.
  final Animation<double>? flash;

  final VoidCallback onTap;

  @override
  Widget build(BuildContext context) {
    final anim = flash;
    if (anim == null) return _body(context, 0);
    return AnimatedBuilder(
      animation: anim,
      builder: (context, _) {
        final t = anim.value;
        final dx = sin(t * pi * 5) * 7 * (1 - t);
        return Transform.translate(
          offset: Offset(dx, 0),
          child: _body(context, 1 - t),
        );
      },
    );
  }

  /// [red] runs from 1 (just picked wrong) down to 0.
  Widget _body(BuildContext context, double red) {
    final c = context.lingo;
    final matched = state == _TileState.matched;
    final selected = state == _TileState.selected;

    var border = c.hairline;
    var fill = c.raised;
    var width = 1.0;
    if (matched) {
      border = c.success;
      fill = c.success.withValues(alpha: 0.20);
      width = 2;
    } else if (selected) {
      border = c.accent;
      fill = c.accent.withValues(alpha: 0.14);
      width = 2;
    }
    if (red > 0) {
      border = Color.lerp(border, kLadderWrong, red) ?? border;
      fill = Color.lerp(fill, kLadderWrong.withValues(alpha: 0.24), red) ?? fill;
      width = 2;
    }

    return Semantics(
      button: true,
      selected: selected,
      enabled: !matched,
      child: Material(
        color: fill,
        borderRadius: BorderRadius.circular(8),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: matched ? null : onTap,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 6),
            decoration: BoxDecoration(
              border: Border.all(color: border, width: width),
              borderRadius: BorderRadius.circular(8),
            ),
            child: Stack(
              fit: StackFit.expand,
              children: [
                Center(
                  child: side == MatchSide.left
                      ? _wordContent(context)
                      : _glossContent(context),
                ),
                if (matched)
                  Positioned(
                    top: 0,
                    right: 0,
                    child: Icon(Icons.check_circle, size: 14, color: c.success),
                  ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  /// The word in the target language, with its reading underneath for the
  /// languages that have one. Scaled down rather than wrapped or overflowed.
  Widget _wordContent(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final card = pair.card;
    final lemma = card.displayLemma;
    final reading = card.reading;
    final length = lemma.runes.length;
    final size = length <= 8 ? 21.0 : (length <= 12 ? 18.0 : 15.0);
    final base = text.titleLarge?.copyWith(fontSize: size, height: 1.15);
    final dir = rtl ? TextDirection.rtl : TextDirection.ltr;

    return FittedBox(
      fit: BoxFit.scaleDown,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          Text(
            lemma,
            textAlign: TextAlign.center,
            textDirection: dir,
            style: arabicStyle(lemma, base),
          ),
          if (reading != null && reading.isNotEmpty)
            Text(
              reading,
              textAlign: TextAlign.center,
              style: text.bodySmall?.copyWith(fontSize: 12),
            ),
        ],
      ),
    );
  }

  Widget _glossContent(BuildContext context) {
    final text = Theme.of(context).textTheme;
    final gloss = pair.gloss;
    return Text(
      gloss,
      textAlign: TextAlign.center,
      maxLines: 3,
      overflow: TextOverflow.ellipsis,
      style: text.titleMedium?.copyWith(
        fontSize: gloss.length > 18 ? 14 : 16,
        height: 1.2,
      ),
    );
  }
}

// --- HUD --------------------------------------------------------------------

class _Stat extends StatelessWidget {
  const _Stat({
    required this.label,
    required this.value,
    this.style,
    this.color,
  });

  final String label;
  final String value;
  final TextStyle? style;
  final Color? color;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(label,
            maxLines: 1, overflow: TextOverflow.ellipsis, style: text.bodySmall),
        const SizedBox(height: 2),
        Text(
          value,
          maxLines: 1,
          style: (style ?? text.titleLarge)?.copyWith(color: color),
        ),
      ],
    );
  }
}

/// The combo flame: shown from three right picks in a row. Cosmetic.
class _ComboChip extends StatelessWidget {
  const _ComboChip(this.count);

  final int count;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
      decoration: BoxDecoration(
        color: c.caution.withValues(alpha: 0.18),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.local_fire_department, size: 15, color: c.caution),
          const SizedBox(width: 3),
          Text(
            '$count',
            style: TextStyle(
              color: c.caution,
              fontWeight: FontWeight.w800,
              fontSize: 13,
            ),
          ),
        ],
      ),
    );
  }
}
