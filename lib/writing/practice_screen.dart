import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../audio/tts_service.dart';
import '../data/models.dart';
import '../progress/progress_models.dart';
import '../progress/progress_service.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import 'board_painter.dart';
import 'stroke_matcher.dart';
import 'writing_models.dart';
import 'writing_repository.dart';

enum PracticeMode { watch, trace, write }

const _wrongColor = Color(0xFFE5484D);

/// Learn and practise one character at a time.
///
///  * Watch  - the strokes are drawn in order, numbered.
///  * Trace  - faint guide strokes; draw over them one by one.
///  * Write  - an empty square; hints only appear after slips.
class WritingPracticeScreen extends StatefulWidget {
  const WritingPracticeScreen({
    super.key,
    required this.deck,
    required this.strokeSet,
    required this.chars,
    required this.index,
    this.readings = const {},
  });

  final Deck deck;
  final StrokeSet strokeSet;

  /// The list the learner is moving through (previous / next).
  final List<String> chars;
  final int index;

  /// On and kun readings of each kanji (Japanese only); empty otherwise.
  final Map<String, KanjiReading> readings;

  @override
  State<WritingPracticeScreen> createState() => _WritingPracticeScreenState();
}

class _WritingPracticeScreenState extends State<WritingPracticeScreen>
    with TickerProviderStateMixin {
  late int _index = widget.index;
  late final AnimationController _anim =
      AnimationController(vsync: this, duration: const Duration(seconds: 3));
  late final AnimationController _flash = AnimationController(
      vsync: this, duration: const Duration(milliseconds: 450));

  PracticeMode _mode = PracticeMode.watch;
  int _next = 0; // index of the stroke that is due
  List<Offset>? _live;
  List<Offset>? _failed;
  int _pointer = -1;
  bool _sawStylus = false;
  bool _drawing = false;
  int _strokeMisses = 0;
  int _misses = 0;
  int _hints = 0;
  int? _hintStroke;
  MatchIssue? _lastIssue;
  bool _finished = false;
  int _stars = 0;
  List<VocabCard> _examples = const [];
  int _xp = 0;

  String get _ch => widget.chars[_index];
  KanjiReading? get _reading => widget.readings[_ch];
  StrokeChar get _char => widget.strokeSet[_ch]!;
  String get _lang => widget.deck.language;
  Locale get _locale => writingLocale(_lang);

  /// What the voice says for the whole character on screen.
  String get _heard => _reading?.heard(_ch) ?? _ch;

  @override
  void initState() {
    super.initState();
    _anim.addStatusListener((s) {
      if (s == AnimationStatus.completed && mounted) setState(() {});
    });
    _open();
  }

  @override
  void dispose() {
    _anim.dispose();
    _flash.dispose();
    super.dispose();
  }

  /// Sets up the current character. New characters start with Watch; ones
  /// already traced move on to Trace, then Write.
  void _open() {
    final p = context.read<WritingRepository>().progressOf(_lang, _ch);
    final mode = p.runs == 0
        ? PracticeMode.watch
        : (p.stars == 0 ? PracticeMode.trace : PracticeMode.write);
    _examples = [
      for (final c in widget.deck.cards)
        if (c.lemma.contains(_ch)) c
    ].take(4).toList();
    _setMode(mode);
  }

  void _setMode(PracticeMode m) {
    _anim.stop();
    _flash.stop();
    setState(() {
      _mode = m;
      _next = 0;
      _live = null;
      _failed = null;
      _pointer = -1;
      _drawing = false;
      _strokeMisses = 0;
      _misses = 0;
      _hints = 0;
      _hintStroke = null;
      _lastIssue = null;
      _finished = false;
      _xp = 0;
    });
    if (m == PracticeMode.watch) _playWatch();
  }

  /// Says [text] aloud with the deck's voice.
  void _say(String text) => context.read<TtsService>().speak(text);

  /// A tappable reading: a small speaker and the kana. Hiragana is the kun
  /// reading and katakana the on reading, so the script tells them apart.
  Widget _readingChip(LingoColors c, TextTheme text, String r, String label) {
    return Tooltip(
      message: 'Hear $label reading',
      child: ActionChip(
        avatar: Icon(Icons.volume_up_rounded, size: 18, color: c.accent),
        label: Text(KanjiReading.shown(r),
            locale: _locale, style: text.titleMedium),
        visualDensity: VisualDensity.compact,
        onPressed: () => _say(KanjiReading.spoken(r)),
      ),
    );
  }

  /// What to say for one pinyin or romanization [r] of the character.
  /// A voice only reads a lone hanzi its usual way, so a second pinyin is
  /// played through a deck word that uses it; null when there is none.
  String? _soundToSay(String r, {required bool first}) {
    if (_lang != 'zh') return _heard;
    for (final w in _examples) {
      final tokens = (w.reading ?? '').trim().split(RegExp(r'\s+'));
      final at = w.lemma.indexOf(_ch);
      if (at >= 0 && tokens.length == w.lemma.runes.length && tokens[at] == r) {
        return w.lemma;
      }
    }
    return first ? _ch : null;
  }

  /// A pinyin or romanization chip; tappable when the voice can say it.
  Widget _soundChip(LingoColors c, TextTheme text, String r, {required bool first}) {
    final say = _soundToSay(r, first: first);
    final label = Text(r, locale: _locale, style: text.titleMedium);
    if (say == null) {
      return Chip(label: label, visualDensity: VisualDensity.compact);
    }
    return ActionChip(
      avatar: Icon(Icons.volume_up_rounded, size: 18, color: c.accent),
      label: label,
      visualDensity: VisualDensity.compact,
      tooltip: 'Hear it',
      onPressed: () => _say(say),
    );
  }

  /// The readings above the big kanji, each one tappable to hear it.
  Widget _readingsBlock(LingoColors c, TextTheme text) {
    final r = _reading;
    if (r == null || r.isEmpty) return const SizedBox.shrink();
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Wrap(
        spacing: 8,
        runSpacing: 0,
        crossAxisAlignment: WrapCrossAlignment.center,
        children: [
          for (final k in r.kun) _readingChip(c, text, k, 'kun'),
          for (final o in r.on) _readingChip(c, text, o, 'on'),
          for (var i = 0; i < r.sounds.length; i++)
            _soundChip(c, text, r.sounds[i], first: i == 0),
        ],
      ),
    );
  }

  void _playWatch() {
    final n = _char.strokeCount;
    _anim.duration = Duration(milliseconds: 700 * n + 400);
    _anim.forward(from: 0);
  }

  void _go(int delta) {
    final i = _index + delta;
    if (i < 0 || i >= widget.chars.length) return;
    _index = i;
    _open();
  }

  // ------------------------------------------------------------ drawing
  Offset _toGrid(Offset local, double side) => Offset(
        (local.dx * 1000 / side).clamp(0.0, 1000.0),
        (local.dy * 1000 / side).clamp(0.0, 1000.0),
      );

  bool _accepts(PointerEvent e) {
    if (_mode == PracticeMode.watch || _finished) return false;
    if (e.kind == PointerDeviceKind.stylus ||
        e.kind == PointerDeviceKind.invertedStylus) {
      _sawStylus = true;
    } else if (e.kind == PointerDeviceKind.touch && _sawStylus) {
      return false; // palm rejection once a pen has been used
    }
    if (e.kind == PointerDeviceKind.mouse && e.buttons != kPrimaryButton) {
      return false;
    }
    return true;
  }

  void _down(PointerDownEvent e, double side) {
    if (_pointer != -1 || !_accepts(e)) return;
    _pointer = e.pointer;
    _flash.stop();
    setState(() {
      _drawing = true; // freezes the page scroll while a stroke is drawn
      _failed = null;
      _hintStroke = null;
      _live = [_toGrid(e.localPosition, side)];
    });
  }

  void _move(PointerMoveEvent e, double side) {
    if (e.pointer != _pointer || _live == null) return;
    final p = _toGrid(e.localPosition, side);
    if ((p - _live!.last).distance < 2) return;
    setState(() => _live!.add(p));
  }

  void _up(PointerUpEvent e, double side) {
    if (e.pointer != _pointer || _live == null) return;
    final pts = [..._live!, _toGrid(e.localPosition, side)];
    _pointer = -1;
    setState(() {
      _live = null;
      _drawing = false;
    });
    _judge(pts);
  }

  void _cancel(PointerCancelEvent e) {
    if (e.pointer != _pointer) return;
    _pointer = -1;
    setState(() {
      _live = null;
      _drawing = false;
    });
  }

  void _judge(List<Offset> pts) {
    final strokes = _char.strokes;
    final target = strokes[_next];
    final result = StrokeMatcher.match(
      user: pts,
      target: target,
      later: strokes.sublist(_next + 1),
      leniency: _strokeMisses >= 2 ? 1.3 : 1.0,
    );
    if (result.ok) {
      HapticFeedback.selectionClick();
      setState(() {
        _next++;
        _strokeMisses = 0;
        _lastIssue = null;
        if (_next >= strokes.length) _finish();
      });
      return;
    }
    HapticFeedback.lightImpact();
    setState(() {
      _failed = pts;
      _lastIssue = result.issue;
      _strokeMisses++;
      _misses++;
    });
    _flash.forward(from: 0);
    // After a couple of slips show the stroke instead of letting the
    // learner guess again.
    final limit = _mode == PracticeMode.trace ? 2 : 3;
    if (_strokeMisses >= limit) _showHint(auto: true);
  }

  void _finish() {
    _finished = true;
    final write = _mode == PracticeMode.write;
    final stars = write
        ? StrokeMatcher.starsFor(misses: _misses, hints: _hints)
        : null;
    _stars = stars ?? 0;

    final repo = context.read<WritingRepository>();
    final before = repo.progressOf(_lang, _ch);
    final delta = context.read<ProgressService>().record(ProgressEvent.writing(
          write: write,
          stars: _stars,
          strokes: _char.strokeCount,
          known: before.stars > 0,
          firstEver: before.runs == 0,
          deckId: widget.deck.id,
        ));
    _xp = delta.xpGained;
    repo.recordFinished(_lang, _ch, stars: stars);
  }

  void _showHint({bool auto = false}) {
    if (_finished || _mode == PracticeMode.watch) return;
    if (!auto) _hints++;
    setState(() => _hintStroke = _next);
    _anim.duration = const Duration(milliseconds: 900);
    _anim.forward(from: 0);
  }

  // ------------------------------------------------------------- layers
  List<StrokeLayer> _layers(LingoColors c) {
    final strokes = _char.strokes;
    final out = <StrokeLayer>[];
    if (_mode == PracticeMode.watch) {
      final n = strokes.length;
      for (var i = 0; i < n; i++) {
        final p = (_anim.value * n - i).clamp(0.0, 1.0);
        if (p > 0) out.add(StrokeLayer(strokes[i], c.ink, progress: p));
      }
      return out;
    }
    if (_mode == PracticeMode.trace) {
      for (var i = _next; i < strokes.length; i++) {
        out.add(StrokeLayer(strokes[i], c.inkMuted, opacity: 0.22));
      }
    }
    for (var i = 0; i < _next; i++) {
      out.add(StrokeLayer(strokes[i], c.ink));
    }
    if (_hintStroke != null && _hintStroke! < strokes.length && !_finished) {
      out.add(StrokeLayer(strokes[_hintStroke!], c.accent,
          progress: _anim.value, width: 50));
    }
    if (_failed != null) {
      out.add(StrokeLayer(_failed!, _wrongColor,
          width: 36, opacity: 1 - _flash.value));
    }
    return out;
  }

  List<NumberMark> _marks(LingoColors c) {
    final strokes = _char.strokes;
    if (_mode == PracticeMode.watch) {
      final n = strokes.length;
      return [
        for (var i = 0; i < n; i++)
          if (_anim.value * n - i > 0.02) NumberMark(strokes[i].first, i + 1, c.accent)
      ];
    }
    if (_mode == PracticeMode.trace && !_finished) {
      return [
        for (var i = _next; i < strokes.length; i++)
          NumberMark(strokes[i].first, i + 1,
              i == _next ? c.accent : c.inkMuted.withValues(alpha: 0.7))
      ];
    }
    return const [];
  }

  String _xpNote() => _xp > 0 ? ' +$_xp XP' : '';

  String _status() {
    if (_finished) {
      return switch (_mode) {
        PracticeMode.write =>
          'Well done. ${_stars == 3 ? 'No slips.' : '$_misses slip${_misses == 1 ? '' : 's'}.'}${_xpNote()}',
        _ => 'Traced. Try it from memory in Write.${_xpNote()}',
      };
    }
    if (_mode == PracticeMode.watch) {
      return 'Watch the order of the ${_char.strokeCount} strokes, then try Trace.';
    }
    final n = _char.strokeCount;
    final step = 'Stroke ${_next + 1} of $n';
    return switch (_lastIssue) {
      null => step,
      MatchIssue.wrongDirection => '$step. That one runs the other way.',
      MatchIssue.wrongOrder => '$step. Good stroke, but not the next one.',
      MatchIssue.tooShort => '$step. Draw the whole stroke.',
      MatchIssue.tooLong => '$step. One stroke at a time.',
      MatchIssue.offTarget => '$step. Not quite. Try again.',
    };
  }

  // -------------------------------------------------------------- build
  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final repo = context.watch<WritingRepository>();
    final prog = repo.progressOf(_lang, _ch);

    return Scaffold(
      appBar: AppBar(
        title: Text('${_index + 1} of ${widget.chars.length}'),
        actions: [
          IconButton(
            tooltip: 'Previous character',
            onPressed: _index > 0 ? () => _go(-1) : null,
            icon: const Icon(Icons.chevron_left),
          ),
          IconButton(
            tooltip: 'Next character',
            onPressed: _index < widget.chars.length - 1 ? () => _go(1) : null,
            icon: const Icon(Icons.chevron_right),
          ),
        ],
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 560),
            child: ListView(
              physics: _drawing
                  ? const NeverScrollableScrollPhysics()
                  : const ClampingScrollPhysics(),
              padding: const EdgeInsets.fromLTRB(20, 4, 20, 28),
              children: [
                _readingsBlock(c, text),
                Row(
                  children: [
                    InkWell(
                      borderRadius: BorderRadius.circular(12),
                      onTap: () => _say(_heard),
                      child: Text(_ch,
                          locale: _locale,
                          style: text.displayMedium?.copyWith(height: 1.1)),
                    ),
                    IconButton(
                      tooltip: 'Hear it',
                      onPressed: () => _say(_heard),
                      icon: Icon(Icons.volume_up_rounded, color: c.accent),
                    ),
                    const SizedBox(width: 6),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            '${_char.strokeCount} stroke${_char.strokeCount == 1 ? '' : 's'}',
                            style: text.titleMedium,
                          ),
                          if (_reading != null && _reading!.meanings.isNotEmpty)
                            Padding(
                              padding: const EdgeInsets.only(top: 2),
                              child: Text(_reading!.meanings.join(', '),
                                  maxLines: 2,
                                  overflow: TextOverflow.ellipsis,
                                  style: text.bodySmall),
                            ),
                          const SizedBox(height: 2),
                          Row(
                            children: [
                              for (var i = 0; i < 3; i++)
                                Icon(
                                  i < prog.stars
                                      ? Icons.star_rounded
                                      : Icons.star_outline_rounded,
                                  size: 20,
                                  color: i < prog.stars ? c.caution : c.inkMuted,
                                ),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 14),
                SegmentedButton<PracticeMode>(
                  showSelectedIcon: false,
                  segments: const [
                    ButtonSegment(
                        value: PracticeMode.watch,
                        icon: Icon(Icons.play_arrow_rounded),
                        label: Text('Watch')),
                    ButtonSegment(
                        value: PracticeMode.trace,
                        icon: Icon(Icons.gesture),
                        label: Text('Trace')),
                    ButtonSegment(
                        value: PracticeMode.write,
                        icon: Icon(Icons.edit_outlined),
                        label: Text('Write')),
                  ],
                  selected: {_mode},
                  onSelectionChanged: (s) => _setMode(s.first),
                ),
                const SizedBox(height: 14),
                LayoutBuilder(builder: (context, box) {
                  final side = box.maxWidth;
                  return AnimatedBuilder(
                    animation: Listenable.merge([_anim, _flash]),
                    builder: (context, _) => Listener(
                      behavior: HitTestBehavior.opaque,
                      onPointerDown: (e) => _down(e, side),
                      onPointerMove: (e) => _move(e, side),
                      onPointerUp: (e) => _up(e, side),
                      onPointerCancel: _cancel,
                      child: Container(
                        decoration: BoxDecoration(
                          color: c.raised,
                          borderRadius: BorderRadius.circular(28),
                        ),
                        child: CustomPaint(
                          size: Size.square(side),
                          painter: BoardPainter(
                            layers: _layers(c),
                            marks: _marks(c),
                            live: _live,
                            liveColor: c.ink,
                            gridColor: c.hairline,
                            frameColor: c.hairline,
                            dot: _mode == PracticeMode.trace &&
                                    !_finished &&
                                    _next < _char.strokeCount
                                ? _char.strokes[_next].first
                                : null,
                            dotColor: c.accent,
                          ),
                        ),
                      ),
                    ),
                  );
                }),
                const SizedBox(height: 12),
                Text(_status(),
                    textAlign: TextAlign.center, style: text.bodyMedium),
                const SizedBox(height: 12),
                if (_finished) _finishedBar(c, text) else _controls(c),
                if (_examples.isNotEmpty) ...[
                  const SizedBox(height: 22),
                  Text('Words with $_ch', style: text.titleSmall),
                  const SizedBox(height: 8),
                  for (final w in _examples)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 8),
                      child: AppCard(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 14, vertical: 10),
                        // Japanese is said from its kana, the others from the word.
                        onTap: () => _say(
                            _lang == 'ja' && (w.reading ?? '').isNotEmpty
                                ? w.reading!
                                : w.lemma),
                        child: Row(
                          children: [
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                if ((w.reading ?? '').isNotEmpty)
                                  Text(w.reading!,
                                      locale: _locale,
                                      style: text.labelSmall
                                          ?.copyWith(color: c.accent)),
                                Text(w.lemma,
                                    locale: _locale, style: text.titleMedium),
                              ],
                            ),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Text(
                                w.gloss,
                                maxLines: 2,
                                overflow: TextOverflow.ellipsis,
                                style: text.bodySmall,
                              ),
                            ),
                            Icon(Icons.volume_up_rounded,
                                size: 20, color: c.accent),
                          ],
                        ),
                      ),
                    ),
                ],
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _controls(LingoColors c) {
    if (_mode == PracticeMode.watch) {
      return Row(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          OutlinedButton.icon(
            onPressed: _playWatch,
            icon: const Icon(Icons.replay),
            label: const Text('Replay'),
          ),
          const SizedBox(width: 12),
          FilledButton.icon(
            onPressed: () => _setMode(PracticeMode.trace),
            icon: const Icon(Icons.gesture),
            label: const Text('Trace it'),
          ),
        ],
      );
    }
    return Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        OutlinedButton.icon(
          onPressed: _showHint,
          icon: const Icon(Icons.lightbulb_outline),
          label: const Text('Hint'),
        ),
        const SizedBox(width: 12),
        OutlinedButton.icon(
          onPressed: () => _setMode(_mode),
          icon: const Icon(Icons.refresh),
          label: const Text('Start over'),
        ),
      ],
    );
  }

  Widget _finishedBar(LingoColors c, TextTheme text) {
    final more = _index < widget.chars.length - 1;
    return Column(
      children: [
        if (_mode == PracticeMode.write)
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              for (var i = 0; i < 3; i++)
                Icon(
                  i < _stars ? Icons.star_rounded : Icons.star_outline_rounded,
                  size: 40,
                  color: i < _stars ? c.caution : c.inkMuted,
                ),
            ],
          ),
        const SizedBox(height: 8),
        Wrap(
          alignment: WrapAlignment.center,
          spacing: 12,
          runSpacing: 8,
          children: [
            OutlinedButton.icon(
              onPressed: () => _setMode(_mode),
              icon: const Icon(Icons.refresh),
              label: const Text('Again'),
            ),
            if (_mode == PracticeMode.trace)
              FilledButton.icon(
                onPressed: () => _setMode(PracticeMode.write),
                icon: const Icon(Icons.edit_outlined),
                label: const Text('Write it'),
              )
            else if (more)
              FilledButton.icon(
                onPressed: () => _go(1),
                icon: const Icon(Icons.arrow_forward),
                label: const Text('Next character'),
              ),
          ],
        ),
      ],
    );
  }
}
