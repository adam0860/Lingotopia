import 'package:flutter/material.dart';

import '../../data/models.dart';
import '../../lessons/bidi.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../../ui/app_card.dart';
import '../../ui/format.dart';
import '../../ui/session_summary.dart';
import 'recall_engine.dart';
import 'recall_stats.dart';

/// What the player chose after a round.
enum RecallExit { playAgain, settings, home }

/// "Top 100", "Rank 1,250" or "–": a rank for a stat tile.
String recallReachLabel(int reach) {
  final r = RecallRules.reachRounded(reach);
  if (r == 0) return '–';
  if (r <= 100) return 'Top 100';
  return 'Rank ${groupedInt(r)}';
}

/// "You reached about rank 1,250." The deepest word recalled, rounded.
String recallReachSentence(int reach) {
  final r = RecallRules.reachRounded(reach);
  if (r == 0) return 'No word recalled this round.';
  if (r <= 100) return 'You reached the Top 100.';
  return 'You reached about rank ${groupedInt(r)}.';
}

/// The end-of-round page: words recalled, how deep it got, the records, what
/// was earned, and the words that got away.
class RecallResultView extends StatelessWidget {
  const RecallResultView({
    super.key,
    required this.deck,
    required this.summary,
    required this.stats,
    required this.records,
    required this.onSpeak,
    this.session,
  });

  final Deck deck;
  final RecallSummary summary;

  /// Lifetime numbers, already including this round.
  final RecallStats stats;

  /// Which records this round broke.
  final RecallRecords records;

  /// What this round earned in XP, trophies and so on.
  final ProgressSession? session;

  final void Function(String text, String id) onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final accuracy = summary.answered == 0
        ? 0
        : (100 * summary.correct / summary.answered).round();

    // One entry per word: a word missed twice is listed once.
    final seen = <String>{};
    final missed = [
      for (final m in summary.missed)
        if (seen.add(m.card.id)) m,
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Quick Recall'),
        leading: IconButton(
          icon: const Icon(Icons.close),
          tooltip: 'Back to games',
          onPressed: () => Navigator.of(context).pop(RecallExit.home),
        ),
      ),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 680),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 8, 20, 28),
              children: [
                AppCard(
                  padding: const EdgeInsets.all(20),
                  borderColor: records.any ? c.success : null,
                  child: Column(
                    children: [
                      Icon(Icons.bolt, size: 36, color: c.caution),
                      const SizedBox(height: 4),
                      Text('Time’s up',
                          style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                      Text('${summary.correct}',
                          style: text.displayMedium
                              ?.copyWith(fontWeight: FontWeight.w800, height: 1.1)),
                      Text(
                          summary.correct == 1
                              ? 'word recalled'
                              : 'words recalled',
                          style: text.titleMedium),
                      const SizedBox(height: 10),
                      Text(recallReachSentence(summary.reach),
                          textAlign: TextAlign.center,
                          style: text.titleMedium?.copyWith(color: c.accent)),
                      if (records.any) ...[
                        const SizedBox(height: 12),
                        Wrap(
                          alignment: WrapAlignment.center,
                          spacing: 8,
                          runSpacing: 6,
                          children: [
                            if (records.score)
                              _Pill('New best score', c.success, c.onSuccess),
                            if (records.reach)
                              _Pill('Deepest reach yet', c.success, c.onSuccess),
                            if (records.streak)
                              _Pill('Best streak yet', c.success, c.onSuccess),
                          ],
                        ),
                      ],
                    ],
                  ),
                ),
                const SizedBox(height: 14),
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    border: Border.all(color: c.hairline),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      RecallFigure('Accuracy', '$accuracy%'),
                      RecallFigure('Answered', '${summary.answered}'),
                      RecallFigure('Best streak', '${summary.bestStreak}'),
                    ],
                  ),
                ),
                const SizedBox(height: 14),
                Text('Your records in ${deck.languageName}',
                    style: text.titleMedium),
                const SizedBox(height: 8),
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    border: Border.all(color: c.hairline),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      RecallFigure('Best score', '${stats.bestScore}'),
                      RecallFigure('Deepest reach', recallReachLabel(stats.bestReach)),
                      RecallFigure('Rounds', '${stats.played}'),
                    ],
                  ),
                ),
                if (session != null && session!.xp > 0) ...[
                  const SizedBox(height: 14),
                  Center(child: SessionSummary(session: session!)),
                ],
                const SizedBox(height: 18),
                if (summary.answered == 0)
                  Text('No questions answered this time.', style: text.bodyMedium)
                else if (missed.isEmpty)
                  Text('No misses. A clean round.', style: text.bodyMedium)
                else ...[
                  Text('Words you missed', style: text.titleMedium),
                  const SizedBox(height: 8),
                  for (final m in missed) _MissedRow(item: m, onSpeak: onSpeak),
                ],
                const SizedBox(height: 22),
                FilledButton(
                  style: FilledButton.styleFrom(
                      minimumSize: const Size.fromHeight(52)),
                  onPressed: () => Navigator.of(context).pop(RecallExit.playAgain),
                  child: const Text('Play again'),
                ),
                const SizedBox(height: 8),
                OutlinedButton(
                  style: OutlinedButton.styleFrom(
                      minimumSize: const Size.fromHeight(48)),
                  onPressed: () => Navigator.of(context).pop(RecallExit.settings),
                  child: const Text('Change settings'),
                ),
                const SizedBox(height: 8),
                TextButton(
                  onPressed: () => Navigator.of(context).pop(RecallExit.home),
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

class _Pill extends StatelessWidget {
  const _Pill(this.label, this.color, this.onColor);

  final String label;
  final Color color;
  final Color onColor;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
      decoration: BoxDecoration(
        color: color,
        borderRadius: BorderRadius.circular(12),
      ),
      child: Text(label,
          style: TextStyle(
              color: onColor, fontSize: 12, fontWeight: FontWeight.w700)),
    );
  }
}

class _MissedRow extends StatelessWidget {
  const _MissedRow({required this.item, required this.onSpeak});

  final RecallQuestion item;
  final void Function(String text, String id) onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final card = item.card;
    final hint = card.pronunciationHint;

    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Container(
        padding: const EdgeInsets.fromLTRB(14, 10, 6, 10),
        decoration: BoxDecoration(
          color: c.raised,
          border: Border.all(color: c.hairline),
          borderRadius: BorderRadius.circular(6),
        ),
        child: Row(
          children: [
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  BidiText(card.displayLemma, style: text.titleMedium),
                  if (hint != null && hint.isNotEmpty)
                    Text(hint,
                        style: text.bodySmall?.copyWith(color: c.inkMuted)),
                  Text(item.gloss,
                      style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                ],
              ),
            ),
            Text('#${card.rank}', style: text.bodySmall),
            IconButton(
              tooltip: 'Listen',
              icon: Icon(Icons.volume_up_outlined, color: c.inkMuted),
              onPressed: () =>
                  onSpeak(card.speakableLemma, 'recall_miss_${card.id}'),
            ),
          ],
        ),
      ),
    );
  }
}

/// A number with its label under it, for the stat rows of the recall pages.
class RecallFigure extends StatelessWidget {
  const RecallFigure(this.label, this.value, {super.key});

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
