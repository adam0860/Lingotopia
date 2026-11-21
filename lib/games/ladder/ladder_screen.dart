import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:provider/provider.dart';

import '../../audio/tts_service.dart';
import '../../data/app_settings.dart';
import '../../data/models.dart';
import '../../difficult/difficult_words_service.dart';
import '../../difficult/word_trouble.dart';
import '../../difficult/question_ids.dart';
import '../../feedback/feedback_service.dart';
import '../../lessons/bidi.dart';
import '../../progress/progress_models.dart';
import '../../progress/progress_service.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import 'ladder_game.dart';
import 'ladder_models.dart';
import 'ladder_pack.dart';
import 'ladder_result_view.dart';
import 'ladder_rules.dart';
import 'ladder_stats.dart';
import 'ladder_widgets.dart';
import 'lifelines.dart';

/// One game of Lingo Ladder: the question, four answers, the lifelines.
///
/// Pops with `true` when the player asks to play again, so the lobby can start
/// the next game straight away.
class LadderScreen extends StatefulWidget {
  const LadderScreen({
    super.key,
    required this.deck,
    required this.pack,
    required this.questions,
    required this.stats,
  });

  final Deck deck;
  final LadderPack pack;
  final List<LadderQuestion> questions;
  final LadderStats stats;

  @override
  State<LadderScreen> createState() => _LadderScreenState();
}

class _LadderScreenState extends State<LadderScreen> {
  late final LadderGame _game = LadderGame(
    questions: widget.questions,
    lifelines: widget.pack.lifelines,
  );
  final ScrollController _scroll = ScrollController();

  /// The answer the player has tapped but not yet locked in.
  int? _selected;

  bool _showResults = false;
  bool _recorded = false;

  late final ProgressSession _session = ProgressSession(
      startLevel: context.read<ProgressService>().level.level);

  @override
  void dispose() {
    _scroll.dispose();
    super.dispose();
  }

  // --- Speech ---------------------------------------------------------------

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

  // --- Actions --------------------------------------------------------------

  void _select(int i) {
    if (!_game.isSelectable(i)) return;
    setState(() => _selected = i);
  }

  void _lockIn() {
    final pick = _selected;
    if (pick == null || !_game.isSelectable(pick)) return;

    final asked = _game.current;
    final result = _game.answer(pick);
    final cardId = vocabCardIdOf(asked.id);
    if (cardId != null) {
      context.read<DifficultWordsService>().record(
            deckId: widget.deck.id,
            cardId: cardId,
            correct: result.correct,
            source: AnswerSource.ladder,
          );
    }

    // Feedback first, before any await, so the context is still valid.
    context.read<FeedbackService>().onAnswer(
          context,
          correct: result.correct,
          streak: _game.correctCount,
        );

    setState(() {});
    if (_game.isOver) _recordOnce();

    final q = _game.current;
    if (context.read<AppSettings>().autoPlayWord) {
      final say = q.revealSpeak ??
          (q.optionsAreTarget ? q.correctOption.speak : null);
      if (say != null) _speak(say, '${q.id}_reveal', warn: false);
    }
  }

  void _next() {
    _game.next();
    setState(() => _selected = null);
    if (_scroll.hasClients) _scroll.jumpTo(0);
  }

  /// Enter: lock in the chosen answer, or move on once it is revealed.
  void _onEnter() {
    if (!_game.revealed) {
      if (_selected != null) _lockIn();
    } else if (_game.isOver) {
      _recordOnce();
      setState(() => _showResults = true);
    } else {
      _next();
    }
  }

  void _recordOnce() {
    if (_recorded) return;
    _recorded = true;
    final outcome = _game.outcome;
    widget.stats.record(outcome);
    widget.stats.save(widget.pack.language);
    _session.add(context.read<ProgressService>().record(ProgressEvent.ladder(
          correct: outcome.correctCount,
          won: outcome.status == GameStatus.won,
          prize: outcome.prize,
          deckId: widget.deck.id,
        )));
  }

  Future<void> _useLifeline(Lifeline l) async {
    if (!_game.canUse(l)) {
      final why = _game.whyNot(l);
      if (why != null) {
        ScaffoldMessenger.of(context)
          ..hideCurrentSnackBar()
          ..showSnackBar(SnackBar(content: Text('${l.label}: $why')));
      }
      return;
    }
    switch (l) {
      case Lifeline.fiftyFifty:
        _game.useFiftyFifty();
        if (_selected != null && _game.eliminated.contains(_selected)) {
          _selected = null;
        }
      case Lifeline.translate:
        _game.useTranslate();
      case Lifeline.audience:
        _game.useAudience();
      case Lifeline.friend:
        final friend = await _pickFriend();
        if (friend == null || !mounted) return;
        _game.useFriend(friend, widget.pack.friendLines);
    }
    if (mounted) setState(() {});
  }

  Future<Friend?> _pickFriend() {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return showModalBottomSheet<Friend>(
      context: context,
      backgroundColor: c.raised,
      builder: (ctx) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 20),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Who do you want to call?', style: text.titleLarge),
              const SizedBox(height: 4),
              Text('Each friend knows some subjects better than others.',
                  style: text.bodySmall?.copyWith(color: c.inkMuted)),
              const SizedBox(height: 12),
              for (final f in widget.pack.friends)
                ListTile(
                  contentPadding: EdgeInsets.zero,
                  leading: CircleAvatar(
                    backgroundColor: c.accent,
                    child: Text(f.name[0],
                        style: TextStyle(
                            color: c.onAccent, fontWeight: FontWeight.w700)),
                  ),
                  title: Text(_friendTitle(f)),
                  subtitle: Text('${f.role} · ${_strengthsLabel(f)}'),
                  onTap: () => Navigator.of(ctx).pop(f),
                ),
            ],
          ),
        ),
      ),
    );
  }

  static String _strengthsLabel(Friend f) =>
      (f.strengths.toList()..sort()).take(4).join(', ');

  /// "田中先生 (Tanaka-sensei)"; just "Lucía" when both spellings are the same.
  static String _friendTitle(Friend f) {
    final target = f.nameTarget;
    if (target == null || target == f.name) return f.name;
    return '$target (${f.name})';
  }

  Future<void> _walkAway() async {
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Walk away?'),
        content: Text(_game.banked == 0
            ? 'You have not won any points yet. The game ends now.'
            : 'You keep ${LadderRules.format(_game.banked)} points and the game ends now.'),
        actions: [
          TextButton(
              onPressed: () => Navigator.of(ctx).pop(false),
              child: const Text('Keep playing')),
          FilledButton(
              onPressed: () => Navigator.of(ctx).pop(true),
              child: const Text('Walk away')),
        ],
      ),
    );
    if (ok != true || !mounted) return;
    _game.walkAway();
    _recordOnce();
    setState(() => _showResults = true);
  }

  Future<bool> _confirmQuit() async {
    final ok = await showDialog<bool>(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Leave the game?'),
        content: const Text(
            'Leaving now loses this game. Use “Walk away” to keep your points.'),
        actions: [
          TextButton(
              onPressed: () => Navigator.of(ctx).pop(false),
              child: const Text('Stay')),
          FilledButton(
              onPressed: () => Navigator.of(ctx).pop(true),
              child: const Text('Leave')),
        ],
      ),
    );
    return ok == true;
  }

  void _showLadderSheet() {
    final c = context.lingo;
    showModalBottomSheet<void>(
      context: context,
      backgroundColor: c.raised,
      isScrollControlled: true,
      builder: (_) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 16),
          child: SingleChildScrollView(
            child: PrizeLadder(currentIndex: _game.index),
          ),
        ),
      ),
    );
  }

  // --- Build ----------------------------------------------------------------

  @override
  Widget build(BuildContext context) {
    if (_showResults) return _results();

    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final q = _game.current;

    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) async {
        if (didPop) return;
        if (_game.isOver || await _confirmQuit()) {
          if (context.mounted) Navigator.of(context).pop();
        }
      },
      child: CallbackShortcuts(
        bindings: {
          const SingleActivator(LogicalKeyboardKey.keyA): () => _select(0),
          const SingleActivator(LogicalKeyboardKey.keyB): () => _select(1),
          const SingleActivator(LogicalKeyboardKey.keyC): () => _select(2),
          const SingleActivator(LogicalKeyboardKey.keyD): () => _select(3),
          const SingleActivator(LogicalKeyboardKey.enter): _onEnter,
          const SingleActivator(LogicalKeyboardKey.numpadEnter): _onEnter,
        },
        child: Focus(
          autofocus: true,
          child: Scaffold(
        appBar: AppBar(
          title: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Question ${_game.index + 1} of ${LadderRules.length}'),
              Text(
                'For ${LadderRules.format(LadderRules.prizes[_game.index])}'
                '${LadderRules.milestones.contains(_game.index) ? ' · safe haven' : ''}',
                style: text.bodySmall?.copyWith(color: c.caution),
              ),
            ],
          ),
          actions: [
            IconButton(
              tooltip: 'Prize ladder',
              icon: const Icon(Icons.format_list_numbered),
              onPressed: _showLadderSheet,
            ),
          ],
        ),
        body: SafeArea(
          child: LayoutBuilder(
            builder: (context, box) {
              final wide = box.maxWidth >= 900;
              final main = Center(
                child: ConstrainedBox(
                  constraints: const BoxConstraints(maxWidth: 680),
                  child: _body(q),
                ),
              );
              if (!wide) return main;
              return Row(
                children: [
                  Expanded(child: main),
                  SizedBox(
                    width: 250,
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: SingleChildScrollView(
                        child: PrizeLadder(currentIndex: _game.index),
                      ),
                    ),
                  ),
                ],
              );
            },
          ),
        ),
      ),
        ),
      ),
    );
  }

  Widget _results() {
    return LadderResultView(
      deck: widget.deck,
      outcome: _game.outcome,
      stats: widget.stats,
      lifelineCount: widget.pack.lifelines.length,
      session: _session,
      onPlayAgain: () => Navigator.of(context).pop(true),
      onClose: () => Navigator.of(context).pop(),
    );
  }

  String _kindLabel(LadderQuestion q) => switch (q.kind) {
        QuestionKind.vocabToTarget || QuestionKind.vocabToEnglish => 'Vocabulary',
        QuestionKind.sentenceGap => 'Complete the sentence',
        QuestionKind.knowledge => _title(q.category ?? 'general knowledge'),
      };

  static String _title(String s) =>
      s.isEmpty ? s : s[0].toUpperCase() + s.substring(1);

  Widget _body(LadderQuestion q) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final revealed = _game.revealed;
    final poll = _game.poll;

    TileState tileState(int i) {
      if (_game.eliminated.contains(i)) return TileState.eliminated;
      if (revealed) {
        if (q.options[i].correct) return TileState.correct;
        if (i == _game.chosenIndex) return TileState.wrong;
        return TileState.dimmed;
      }
      return i == _selected ? TileState.selected : TileState.normal;
    }

    return Column(
      children: [
        Expanded(
          child: ListView(
            controller: _scroll,
            padding: const EdgeInsets.fromLTRB(16, 12, 16, 12),
            children: [
              // Question card.
              Container(
                padding: const EdgeInsets.all(18),
                decoration: BoxDecoration(
                  color: c.raised,
                  border: Border.all(color: c.hairline),
                  borderRadius: BorderRadius.circular(6),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 9, vertical: 3),
                          decoration: BoxDecoration(
                            border: Border.all(color: c.hairline),
                            borderRadius: BorderRadius.circular(999),
                          ),
                          child: Text(_kindLabel(q),
                              style: TextStyle(
                                  color: c.inkMuted,
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600)),
                        ),
                        const Spacer(),
                        if (q.speakPrompt != null)
                          IconButton(
                            tooltip: 'Listen',
                            visualDensity: VisualDensity.compact,
                            icon: Icon(Icons.volume_up_outlined,
                                color: c.inkMuted),
                            onPressed: () =>
                                _speak(q.speakPrompt!, '${q.id}_prompt'),
                          ),
                      ],
                    ),
                    const SizedBox(height: 10),
                    // Direction follows the text (Arabic sentences run right to
                    // left); every other prompt is unchanged.
                    BidiText(q.prompt,
                        style: text.headlineSmall?.copyWith(height: 1.3)),
                    if (q.detail != null) ...[
                      const SizedBox(height: 10),
                      Text(q.detail!,
                          style: text.bodyMedium?.copyWith(
                              color: c.inkMuted,
                              fontStyle: FontStyle.italic)),
                    ],
                  ],
                ),
              ),
              const SizedBox(height: 12),

              if (_game.translateShown) ...[
                TranslatePanel(question: q),
                const SizedBox(height: 12),
              ],
              if (poll != null) ...[
                PollPanel(poll: poll, optionCount: q.options.length),
                const SizedBox(height: 12),
              ],
              if (_game.advice != null) ...[
                FriendPanel(
                  advice: _game.advice!,
                  onSpeak: () => _speak(
                      _game.advice!.line.target, '${q.id}_friend'),
                ),
                const SizedBox(height: 12),
              ],

              // Answers.
              for (var i = 0; i < q.options.length; i++) ...[
                AnswerTile(
                  letter: letterFor(i),
                  text: q.options[i].text,
                  state: tileState(i),
                  percent: poll?.percents[i],
                  subtext: revealed ? q.options[i].translation : null,
                  onTap: revealed ? null : () => _select(i),
                  onSpeak: revealed && q.options[i].speak != null
                      ? () => _speak(q.options[i].speak!, '${q.id}_o$i')
                      : null,
                ),
                const SizedBox(height: 8),
              ],

              if (revealed) _explanation(q),
            ],
          ),
        ),
        _bottomBar(),
      ],
    );
  }

  Widget _explanation(LadderQuestion q) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final correct = _game.history.last.correct;
    return Container(
      margin: const EdgeInsets.only(top: 4),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: c.raised,
        border: Border.all(color: correct ? c.success : kLadderWrong),
        borderRadius: BorderRadius.circular(6),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            correct
                ? (_game.status == GameStatus.won
                    ? 'Correct! You reached the top of the ladder.'
                    : 'Correct!')
                : 'Not quite. The answer was ${letterFor(q.correctIndex)}: ${q.correctOption.text}',
            style: text.titleMedium?.copyWith(
                color: correct ? c.success : kLadderWrong),
          ),
          if (q.explanation != null) ...[
            const SizedBox(height: 8),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(child: BidiText(q.explanation!, style: text.bodyLarge)),
                if (q.optionsAreTarget || q.promptIsTarget)
                  IconButton(
                    visualDensity: VisualDensity.compact,
                    tooltip: 'Listen',
                    icon: Icon(Icons.volume_up_outlined,
                        size: 20, color: c.inkMuted),
                    onPressed: () =>
                        _speak(q.revealSpeak ?? q.explanation!, '${q.id}_exp'),
                  ),
              ],
            ),
          ],
          if (q.explanationEn != null) ...[
            const SizedBox(height: 4),
            Text(q.explanationEn!,
                style: text.bodySmall?.copyWith(color: c.inkMuted)),
          ],
        ],
      ),
    );
  }

  Widget _bottomBar() {
    final c = context.lingo;
    final revealed = _game.revealed;

    return Container(
      padding: const EdgeInsets.fromLTRB(16, 8, 16, 12),
      decoration: BoxDecoration(
        color: c.ground,
        border: Border(top: BorderSide(color: c.hairline)),
      ),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (!revealed) ...[
            LifelineBar(
              lifelines: widget.pack.lifelines,
              used: _game.usedLifelines,
              usable: _game.canUse,
              onTap: _useLifeline,
            ),
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(
                  child: OutlinedButton(
                    onPressed: _walkAway,
                    child: Text('Walk away · ${LadderRules.format(_game.banked)}'),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: FilledButton(
                    onPressed: _selected == null ? null : _lockIn,
                    child: const Text('Final answer'),
                  ),
                ),
              ],
            ),
          ] else
            SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _game.isOver
                    ? () {
                        _recordOnce();
                        setState(() => _showResults = true);
                      }
                    : _next,
                child: Text(_game.isOver ? 'See results' : 'Next question'),
              ),
            ),
        ],
      ),
    );
  }
}
