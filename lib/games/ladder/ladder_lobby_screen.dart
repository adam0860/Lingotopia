import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../audio/tts_service.dart';
import '../../data/models.dart';
import '../../lessons/bidi.dart';
import '../../theme/app_theme.dart';
import 'ladder_builder.dart';
import 'ladder_pack.dart';
import 'ladder_rules.dart';
import 'ladder_screen.dart';
import 'ladder_stats.dart';
import 'ladder_widgets.dart';
import 'lifelines.dart';
import 'question_bank.dart';

/// The front door of Lingo Ladder: how it works, the ladder, your record, and
/// the Start button.
class LadderLobbyScreen extends StatefulWidget {
  const LadderLobbyScreen({super.key, required this.deck, required this.pack});

  final Deck deck;
  final LadderPack pack;

  @override
  State<LadderLobbyScreen> createState() => _LadderLobbyScreenState();
}

class _LadderLobbyScreenState extends State<LadderLobbyScreen> {
  QuestionBank? _bank;
  LadderStats? _stats;
  bool _starting = false;
  String? _error;

  @override
  void initState() {
    super.initState();
    _loadStats();
  }

  Future<void> _loadStats() async {
    final s = await LadderStats.load(widget.pack.language);
    if (mounted) setState(() => _stats = s);
  }

  Future<void> _start() async {
    if (_starting) return;
    setState(() {
      _starting = true;
      _error = null;
    });
    try {
      _bank ??= await QuestionBank.load(
        widget.pack.bankAsset,
        english: widget.pack.bankIsEnglish,
      );
      final stats = _stats ?? await LadderStats.load(widget.pack.language);
      final questions = LadderBuilder(
        deck: widget.deck,
        pack: widget.pack,
        bank: _bank!,
        seen: stats.seen,
      ).build();
      if (!mounted) return;
      setState(() => _starting = false);

      final again = await Navigator.of(context).push<bool>(
        MaterialPageRoute(
          builder: (_) => LadderScreen(
            deck: widget.deck,
            pack: widget.pack,
            questions: questions,
            stats: stats,
          ),
        ),
      );
      if (!mounted) return;
      setState(() => _stats = stats);
      if (again == true) _start();
    } catch (e) {
      if (!mounted) return;
      setState(() {
        _starting = false;
        _error = 'Could not set up a game: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final stats = _stats;
    final intro = widget.pack.hostIntro;

    return Scaffold(
      appBar: AppBar(title: const Text(LadderRules.title)),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 680),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 8, 20, 28),
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
                      Text('${widget.deck.languageName} · ${LadderRules.length} questions',
                          style: text.bodySmall),
                      const SizedBox(height: 8),
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Expanded(
                            child: BidiText(intro.target,
                                style: text.headlineSmall?.copyWith(height: 1.3)),
                          ),
                          IconButton(
                            tooltip: 'Listen',
                            icon: Icon(Icons.volume_up_outlined, color: c.inkMuted),
                            onPressed: () => context
                                .read<TtsService>()
                                .speak(intro.target, id: 'ladder_intro'),
                          ),
                        ],
                      ),
                      Text(intro.english,
                          style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                    ],
                  ),
                ),
                const SizedBox(height: 18),
                Text('How it works', style: text.titleMedium),
                const SizedBox(height: 8),
                _Bullet(widget.pack.bankIsEnglish
                    ? 'Answer ${LadderRules.length} questions in a row. They start with '
                        'everyday ${widget.deck.languageName} words and climb to the rarest '
                        'words in the deck, with general-knowledge questions in between.'
                    : 'Answer ${LadderRules.length} questions in a row. They start with '
                        'everyday words and end with politics, science and history written '
                        'entirely in ${widget.deck.languageName}.'),
                const _Bullet('Tap an answer, then lock it in with “Final answer”.'),
                const _Bullet('Stars on the ladder are safe havens: reach one and you keep '
                    'its points even if you miss the next question.'),
                const _Bullet('Not sure? Walk away any time and keep what you have won.'),
                const SizedBox(height: 18),
                Text('Your lifelines', style: text.titleMedium),
                const SizedBox(height: 8),
                for (final l in widget.pack.lifelines)
                  Padding(
                    padding: const EdgeInsets.only(bottom: 6),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        SizedBox(
                          width: 84,
                          child: Text(l.label,
                              style: TextStyle(
                                  color: c.caution, fontWeight: FontWeight.w700)),
                        ),
                        Expanded(
                            child: Text(l.description,
                                style: text.bodyMedium?.copyWith(color: c.inkMuted))),
                      ],
                    ),
                  ),
                const SizedBox(height: 14),
                if (stats != null && stats.gamesPlayed > 0)
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      border: Border.all(color: c.hairline),
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceAround,
                      children: [
                        _Figure('Games', '${stats.gamesPlayed}'),
                        _Figure('Wins', '${stats.gamesWon}'),
                        _Figure('Best score', LadderRules.format(stats.bestPrize)),
                        _Figure('Best run', '${stats.bestStreak}/${LadderRules.length}'),
                      ],
                    ),
                  ),
                const SizedBox(height: 14),
                Text('The ladder', style: text.titleMedium),
                const SizedBox(height: 6),
                const PrizeLadder(currentIndex: -1, dense: true),
                if (_error != null) ...[
                  const SizedBox(height: 12),
                  Text(_error!, style: const TextStyle(color: kLadderWrong)),
                ],
                const SizedBox(height: 18),
                FilledButton(
                  onPressed: _starting ? null : _start,
                  child: _starting
                      ? const SizedBox(
                          height: 18,
                          width: 18,
                          child: CircularProgressIndicator(strokeWidth: 2))
                      : const Text('Start the game'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _Bullet extends StatelessWidget {
  const _Bullet(this.text);

  final String text;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Padding(
      padding: const EdgeInsets.only(bottom: 6),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 7, right: 10),
            child: Icon(Icons.circle, size: 6, color: c.accent),
          ),
          Expanded(
            child: Text(text,
                style: Theme.of(context)
                    .textTheme
                    .bodyMedium
                    ?.copyWith(color: c.inkMuted, height: 1.35)),
          ),
        ],
      ),
    );
  }
}

class _Figure extends StatelessWidget {
  const _Figure(this.label, this.value);

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    final text = Theme.of(context).textTheme;
    return Column(
      children: [
        Text(value, style: text.titleMedium),
        const SizedBox(height: 2),
        Text(label, style: text.bodySmall),
      ],
    );
  }
}
