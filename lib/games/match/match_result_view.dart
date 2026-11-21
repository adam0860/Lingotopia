import 'package:flutter/material.dart';

import '../../data/models.dart';
import '../../lessons/bidi.dart';
import '../../progress/progress_session.dart';
import '../../theme/app_theme.dart';
import '../../ui/session_summary.dart';
import 'match_game.dart';
import 'match_stats.dart';

/// What the player chose after a run.
enum MatchExit { again, settings, home }

/// How many words "Worth another look" lists at most.
const int _kMaxTrouble = 12;

/// The end-of-run page: the time, how clean it was, and the words that tripped
/// the player up.
class MatchResultView extends StatelessWidget {
  const MatchResultView({
    super.key,
    required this.deck,
    required this.result,
    required this.length,
    required this.stats,
    required this.previousBest,
    required this.newBest,
    required this.ranked,
    required this.onSpeak,
    this.session,
  });

  /// What this run earned in XP, trophies and so on.
  final ProgressSession? session;

  final Deck deck;
  final MatchResult result;
  final MatchLength length;
  final WordMatchStats stats;

  /// The best time for this length before this run, if there was one.
  final int? previousBest;

  /// This run beat [previousBest] (or set the first best time).
  final bool newBest;

  /// False when the word list was too small for a full-length run, so the time
  /// is not comparable with the others.
  final bool ranked;

  final void Function(String text, String id) onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final trouble = result.trouble;
    final shown = trouble.take(_kMaxTrouble).toList();

    final String breakdown;
    if (result.misses == 0) {
      breakdown = 'Clock ${formatMatchTime(result.elapsedMs)} · no penalties';
    } else {
      const secs = MatchGame.missPenaltyMs ~/ 1000;
      breakdown = 'Clock ${formatMatchTime(result.elapsedMs)} + '
          '${formatMatchTime(result.penaltyMs)} penalty '
          '(${result.misses} ${result.misses == 1 ? 'miss' : 'misses'} × $secs s)';
    }

    return Scaffold(
      appBar: AppBar(
        title: const Text('Word Match'),
        leading: IconButton(
          icon: const Icon(Icons.close),
          tooltip: 'Back to games',
          onPressed: () => Navigator.of(context).pop(MatchExit.home),
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
                    border: Border.all(
                        color: newBest ? c.caution : c.hairline,
                        width: newBest ? 2 : 1),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Column(
                    children: [
                      Icon(Icons.timer_outlined,
                          size: 34, color: newBest ? c.caution : c.inkMuted),
                      const SizedBox(height: 6),
                      Text('${length.label} · ${deck.languageName}',
                          style: text.bodySmall),
                      const SizedBox(height: 4),
                      Text(
                        formatMatchTime(result.finalMs),
                        style: text.displaySmall?.copyWith(
                          fontSize: 44,
                          fontFeatures: const [FontFeature.tabularFigures()],
                        ),
                      ),
                      const SizedBox(height: 8),
                      if (newBest)
                        Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 12, vertical: 4),
                          decoration: BoxDecoration(
                            color: c.caution,
                            borderRadius: BorderRadius.circular(20),
                          ),
                          child: Text('New best!',
                              style: TextStyle(
                                  color: c.onCaution,
                                  fontWeight: FontWeight.w800,
                                  fontSize: 13)),
                        )
                      else if (!ranked)
                        Text('Short run: not counted for best times',
                            textAlign: TextAlign.center,
                            style: text.bodySmall)
                      else if (previousBest != null)
                        Text('Best: ${formatMatchTime(previousBest!)}',
                            style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                      const SizedBox(height: 6),
                      Text(breakdown,
                          textAlign: TextAlign.center,
                          style: text.bodySmall),
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
                      _Figure('Misses', '${result.misses}'),
                      _Figure('Flawless boards',
                          '${result.flawless}/${result.boards}'),
                      _Figure('Best combo', '${result.bestCombo}'),
                    ],
                  ),
                ),
                if (stats.played > 0) ...[
                  const SizedBox(height: 8),
                  Text(
                    'Overall in ${deck.languageName}: ${stats.played} '
                    '${stats.played == 1 ? 'run' : 'runs'} · '
                    '${stats.totalBoards} boards · '
                    '${stats.flawlessBoards} flawless',
                    textAlign: TextAlign.center,
                    style: text.bodySmall,
                  ),
                ],
                if (session != null && session!.xp > 0) ...[
                  const SizedBox(height: 14),
                  Center(child: SessionSummary(session: session!)),
                ],
                const SizedBox(height: 18),
                if (trouble.isEmpty)
                  Text('Not one wrong pick. A clean run.',
                      style: text.bodyMedium)
                else ...[
                  Text('Worth another look', style: text.titleMedium),
                  const SizedBox(height: 4),
                  Text('Words that were part of a wrong pick.',
                      style: text.bodySmall),
                  const SizedBox(height: 8),
                  for (final p in shown)
                    _TroubleRow(deck: deck, pair: p, onSpeak: onSpeak),
                  if (trouble.length > shown.length)
                    Padding(
                      padding: const EdgeInsets.only(top: 2),
                      child: Text(
                          '+ ${trouble.length - shown.length} more',
                          style: text.bodySmall),
                    ),
                ],
                const SizedBox(height: 22),
                FilledButton(
                  onPressed: () => Navigator.of(context).pop(MatchExit.again),
                  child: const Text('Play again'),
                ),
                const SizedBox(height: 8),
                OutlinedButton(
                  onPressed: () => Navigator.of(context).pop(MatchExit.settings),
                  child: const Text('Change settings'),
                ),
                const SizedBox(height: 8),
                TextButton(
                  onPressed: () => Navigator.of(context).pop(MatchExit.home),
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

class _TroubleRow extends StatelessWidget {
  const _TroubleRow({
    required this.deck,
    required this.pair,
    required this.onSpeak,
  });

  final Deck deck;
  final MatchPair pair;
  final void Function(String text, String id) onSpeak;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final card = pair.card;
    final reading = card.reading;

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
                  Text(
                    card.displayLemma,
                    textDirection:
                        deck.rtl ? TextDirection.rtl : TextDirection.ltr,
                    style: arabicStyle(card.displayLemma, text.titleMedium),
                  ),
                  if (reading != null && reading.isNotEmpty)
                    Text(reading, style: text.bodySmall),
                  Text(pair.gloss,
                      style: text.bodyMedium?.copyWith(color: c.inkMuted)),
                ],
              ),
            ),
            IconButton(
              tooltip: 'Listen',
              icon: Icon(Icons.volume_up_outlined, color: c.inkMuted),
              onPressed: () =>
                  onSpeak(card.speakableLemma, 'match_trouble_${card.id}'),
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
