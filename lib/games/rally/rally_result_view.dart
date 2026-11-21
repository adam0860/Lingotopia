import 'package:flutter/material.dart';

import '../../data/models.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../../ui/session_summary.dart';
import 'rally_match.dart';
import 'rally_models.dart';
import 'rally_questions.dart';
import 'rally_stats.dart';

/// What the player chose after a match.
enum RallyExit { rematch, changeOpponent, home }

/// The end-of-match page: who won, how it went, and the words that got away.
class RallyResultView extends StatelessWidget {
  const RallyResultView({
    super.key,
    required this.deck,
    required this.match,
    required this.bot,
    required this.stats,
    required this.missed,
    required this.averageSeconds,
    required this.onSpeak,
    this.session,
  });

  /// What this match earned in XP, trophies and so on.
  final ProgressSession? session;

  final Deck deck;
  final RallyMatch match;
  final BotProfile bot;
  final RallyStats stats;
  final List<RallyQuestion> missed;
  final double? averageSeconds;
  final void Function(String text, String id) onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final won = match.winner == RallySide.you;
    final you = match.you;
    final foe = match.bot;
    final accuracy =
        you.answered == 0 ? 0 : (100 * you.correct / you.answered).round();

    final why = won
        ? (match.bot.lives <= 0
            ? '${bot.name} ran out of lives.'
            : 'You reached ${match.rules.targetScore} points.')
        : (match.you.lives <= 0
            ? 'You ran out of lives.'
            : '${bot.name} reached ${match.rules.targetScore} points.');

    // One entry per word: a word missed twice is listed once.
    final seen = <String>{};
    final unique = [
      for (final m in missed)
        if (seen.add(m.question.id)) m,
    ];

    return Scaffold(
      appBar: AppBar(
        title: const Text('Lingo Rally'),
        leading: IconButton(
          icon: const Icon(Icons.close),
          tooltip: 'Back to games',
          onPressed: () => Navigator.of(context).pop(RallyExit.home),
        ),
      ),
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
                    border: Border.all(color: won ? c.success : c.hairline, width: won ? 2 : 1),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Column(
                    children: [
                      Icon(won ? Icons.emoji_events_outlined : Icons.sports_tennis,
                          size: 36, color: won ? c.caution : c.inkMuted),
                      const SizedBox(height: 8),
                      Text(won ? 'You win!' : '${bot.name} wins',
                          style: text.headlineMedium),
                      const SizedBox(height: 4),
                      Text('${you.score} – ${foe.score}',
                          style: text.titleLarge?.copyWith(
                              color: won ? c.success : c.inkMuted)),
                      const SizedBox(height: 4),
                      Text(why, style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                    ],
                  ),
                ),
                const SizedBox(height: 16),
                Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    border: Border.all(color: c.hairline),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      _Figure('Accuracy', '$accuracy%'),
                      _Figure('Avg. time',
                          averageSeconds == null ? '–' : '${averageSeconds!.toStringAsFixed(1)}s'),
                      _Figure('Best streak', '${you.bestStreak}'),
                      _Figure('Power-ups',
                          '${you.shieldsEarned + you.smashesEarned + you.blastsLanded}'),
                    ],
                  ),
                ),
                if (stats.played > 0) ...[
                  const SizedBox(height: 8),
                  Text(
                    'Overall in ${deck.languageName}: ${stats.won} won of ${stats.played} · '
                    'best streak ${stats.bestStreak}',
                    textAlign: TextAlign.center,
                    style: text.bodySmall,
                  ),
                ],
                if (session != null && session!.xp > 0) ...[
                  const SizedBox(height: 14),
                  Center(child: SessionSummary(session: session!)),
                ],
                const SizedBox(height: 18),
                if (unique.isEmpty)
                  Text('No misses. A clean sheet.', style: text.bodyMedium)
                else ...[
                  Text('Words to review', style: text.titleMedium),
                  const SizedBox(height: 8),
                  for (final m in unique) _MissedRow(m: m, onSpeak: onSpeak),
                ],
                const SizedBox(height: 22),
                FilledButton(
                  onPressed: () => Navigator.of(context).pop(RallyExit.rematch),
                  child: const Text('Rematch'),
                ),
                const SizedBox(height: 8),
                OutlinedButton(
                  onPressed: () =>
                      Navigator.of(context).pop(RallyExit.changeOpponent),
                  child: const Text('Change opponent'),
                ),
                const SizedBox(height: 8),
                TextButton(
                  onPressed: () => Navigator.of(context).pop(RallyExit.home),
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

class _MissedRow extends StatelessWidget {
  const _MissedRow({required this.m, required this.onSpeak});

  final RallyQuestion m;
  final void Function(String text, String id) onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final q = m.question;

    // Always show the target-language text on one line and its meaning on the
    // other, whichever way round the question was asked.
    final String target;
    final String english;
    String? speak;
    if (q.promptIsTarget) {
      target = q.prompt;
      english = q.correctOption.text;
      speak = q.speakPrompt;
    } else {
      target = q.correctOption.text;
      english = q.correctOption.translation ?? '';
      speak = q.correctOption.speak;
    }

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
                  Text(target, style: text.titleMedium),
                  if (english.isNotEmpty)
                    Text(english, style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                ],
              ),
            ),
            if (speak != null)
              IconButton(
                tooltip: 'Listen',
                icon: Icon(Icons.volume_up_outlined, color: c.inkMuted),
                onPressed: () => onSpeak(speak!, 'rally_miss_${q.id}'),
              ),
          ],
        ),
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
