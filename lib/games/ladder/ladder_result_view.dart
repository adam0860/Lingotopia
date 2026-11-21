import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../audio/tts_service.dart';
import '../../data/models.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../../ui/session_summary.dart';
import 'ladder_game.dart';
import 'ladder_models.dart';
import 'ladder_rules.dart';
import 'ladder_stats.dart';
import 'ladder_widgets.dart';

/// The end-of-game screen: what you won, and every question with its answer so
/// the game doubles as a revision list.
class LadderResultView extends StatelessWidget {
  const LadderResultView({
    super.key,
    required this.deck,
    required this.outcome,
    required this.stats,
    required this.lifelineCount,
    required this.onPlayAgain,
    required this.onClose,
    this.session,
  });

  /// What this game earned in XP, trophies and so on.
  final ProgressSession? session;

  final Deck deck;
  final LadderOutcome outcome;
  final LadderStats stats;

  /// How many lifelines the game offered (the pack's list), for "used 1/3".
  final int lifelineCount;

  final VoidCallback onPlayAgain;
  final VoidCallback onClose;

  (String, String) get _headline => switch (outcome.status) {
        GameStatus.won => (
            'You climbed the whole ladder!',
            'All ${LadderRules.length} questions right.'
          ),
        GameStatus.walkedAway => (
            'A wise exit',
            'You took your points and walked away.'
          ),
        GameStatus.lost => (
            'Not this time',
            outcome.prize > 0
                ? 'You fall back to your last safe haven.'
                : 'You did not reach a safe haven.'
          ),
        GameStatus.playing => ('Game in progress', ''),
      };

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final (title, subtitle) = _headline;
    final won = outcome.status == GameStatus.won;

    return Scaffold(
      appBar: AppBar(
        title: const Text(LadderRules.title),
        leading: IconButton(
          icon: const Icon(Icons.close),
          onPressed: onClose,
        ),
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 680),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 12, 20, 28),
              children: [
                Container(
                  padding: const EdgeInsets.all(22),
                  decoration: BoxDecoration(
                    color: c.raised,
                    border: Border.all(color: won ? c.caution : c.hairline, width: won ? 2 : 1),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Column(
                    children: [
                      Icon(won ? Icons.emoji_events_outlined : Icons.flag_outlined,
                          size: 40, color: won ? c.caution : c.accent),
                      const SizedBox(height: 10),
                      Text(title,
                          textAlign: TextAlign.center,
                          style: text.headlineSmall),
                      const SizedBox(height: 4),
                      Text(subtitle,
                          textAlign: TextAlign.center,
                          style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                      const SizedBox(height: 18),
                      Text(LadderRules.format(outcome.prize),
                          style: TextStyle(
                              fontFamily: c.display,
                              fontSize: 44,
                              fontWeight: FontWeight.w700,
                              color: c.caution)),
                      Text('Lingo points', style: text.bodySmall),
                    ],
                  ),
                ),
                const SizedBox(height: 14),
                Row(
                  children: [
                    _Stat(
                        label: 'Correct',
                        value: '${outcome.correctCount}/${LadderRules.length}'),
                    _Stat(
                        label: 'Lifelines used',
                        value: '${outcome.lifelinesUsed.length}/$lifelineCount'),
                    _Stat(
                        label: 'Best ever',
                        value: LadderRules.format(stats.bestPrize)),
                  ],
                ),
                if (session != null && session!.xp > 0) ...[
                  const SizedBox(height: 14),
                  Center(child: SessionSummary(session: session!)),
                ],
                const SizedBox(height: 22),
                Text('Your questions', style: text.titleMedium),
                const SizedBox(height: 8),
                for (var i = 0; i < outcome.history.length; i++)
                  _ReviewRow(index: i, record: outcome.history[i]),
                const SizedBox(height: 22),
                FilledButton(
                  onPressed: onPlayAgain,
                  child: const Text('Play again'),
                ),
                const SizedBox(height: 10),
                OutlinedButton(
                  onPressed: onClose,
                  child: const Text('Back to games'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _Stat extends StatelessWidget {
  const _Stat({required this.label, required this.value});

  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Expanded(
      child: Container(
        margin: const EdgeInsets.symmetric(horizontal: 4),
        padding: const EdgeInsets.symmetric(vertical: 12),
        decoration: BoxDecoration(
          border: Border.all(color: c.hairline),
          borderRadius: BorderRadius.circular(6),
        ),
        child: Column(
          children: [
            Text(value, style: text.titleMedium),
            const SizedBox(height: 2),
            Text(label, style: text.bodySmall),
          ],
        ),
      ),
    );
  }
}

class _ReviewRow extends StatelessWidget {
  const _ReviewRow({required this.index, required this.record});

  final int index;
  final AnswerRecord record;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final q = record.question;
    final right = record.correct;
    final answer = q.correctOption;

    return Container(
      margin: const EdgeInsets.only(bottom: 8),
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: c.raised,
        border: Border.all(color: c.hairline),
        borderRadius: BorderRadius.circular(6),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(right ? Icons.check_circle_outline : Icons.cancel_outlined,
              size: 20, color: right ? c.success : kLadderWrong),
          const SizedBox(width: 10),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('${index + 1}. ${q.prompt}', style: text.bodyMedium),
                const SizedBox(height: 4),
                Text.rich(TextSpan(children: [
                  TextSpan(
                      text: answer.text,
                      style: const TextStyle(fontWeight: FontWeight.w700)),
                  if (answer.translation != null)
                    TextSpan(
                        text: '  ${answer.translation}',
                        style: TextStyle(color: c.inkMuted)),
                ])),
                if (!right)
                  Padding(
                    padding: const EdgeInsets.only(top: 2),
                    child: Text('You chose: ${q.options[record.chosenIndex].text}',
                        style: text.bodySmall?.copyWith(color: kLadderWrong)),
                  ),
              ],
            ),
          ),
          if (answer.speak != null)
            IconButton(
              visualDensity: VisualDensity.compact,
              tooltip: 'Listen',
              icon: Icon(Icons.volume_up_outlined, size: 18, color: c.inkMuted),
              onPressed: () => context
                  .read<TtsService>()
                  .speak(answer.speak!, id: '${q.id}_review'),
            ),
        ],
      ),
    );
  }
}
