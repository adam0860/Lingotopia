import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../progress/progress_service.dart';
import '../progress/progress_session.dart';
import '../theme/app_theme.dart';
import 'app_card.dart';
import 'format.dart';
import 'level_widgets.dart';
import 'medal.dart';

/// "What you earned" for the end of a session: XP, the level bar, and any
/// level-ups, goal, streak or trophies that came with it. Shows nothing if the
/// session earned no XP.
class SessionSummary extends StatelessWidget {
  const SessionSummary({super.key, required this.session});

  final ProgressSession session;

  @override
  Widget build(BuildContext context) {
    if (session.xp <= 0) return const SizedBox.shrink();

    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final level = context.watch<ProgressService>().level;

    return ConstrainedBox(
      constraints: const BoxConstraints(maxWidth: 420),
      child: AppCard(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Center(child: XpChip(session.xp, big: true)),
            const SizedBox(height: 14),
            Row(
              children: [
                LevelBadge(level: level.level, size: 40),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      XpBar(info: level),
                      const SizedBox(height: 4),
                      Text(
                        '${groupedInt(level.remaining)} XP to level ${level.level + 1}',
                        style: text.bodySmall,
                      ),
                    ],
                  ),
                ),
              ],
            ),
            if (session.hasHighlights) const SizedBox(height: 14),
            if (session.levelsGained > 0)
              _line(context, Icons.arrow_circle_up_rounded, c.accent,
                  'Level ${session.level} reached'),
            if (session.goalReached)
              _line(context, Icons.check_circle_rounded, c.success,
                  'Daily goal reached'),
            if (session.streakExtended && session.streakDays > 0)
              _line(context, Icons.local_fire_department, c.accent,
                  '${session.streakDays}-day streak'),
            for (final t in session.trophies)
              Padding(
                padding: const EdgeInsets.only(top: 8),
                child: Row(
                  children: [
                    TrophyMedal(trophy: t, unlocked: true, size: 36),
                    const SizedBox(width: 10),
                    Expanded(
                      child: Text('${t.title} · ${t.tier.label} trophy',
                          style: text.bodyMedium),
                    ),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }

  Widget _line(BuildContext context, IconData icon, Color color, String label) {
    final text = Theme.of(context).textTheme;
    return Padding(
      padding: const EdgeInsets.only(top: 6),
      child: Row(
        children: [
          Icon(icon, color: color, size: 22),
          const SizedBox(width: 10),
          Expanded(child: Text(label, style: text.bodyMedium)),
        ],
      ),
    );
  }
}
