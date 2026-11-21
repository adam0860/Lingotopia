import 'package:flutter/material.dart';

import '../progress/trophies.dart';
import '../theme/app_theme.dart';
import 'app_card.dart';
import 'format.dart';
import 'medal.dart';

/// One trophy as a card row: medal, name, what it asks for, and either a
/// progress bar (locked) or the date it was earned.
class TrophyProgressRow extends StatelessWidget {
  const TrophyProgressRow({
    super.key,
    required this.trophy,
    required this.value,
    this.unlockedAt,
    this.card = true,
  });

  final Trophy trophy;

  /// Current number for the trophy's metric.
  final int value;

  /// Unlock time in milliseconds since the epoch, or null while locked.
  final int? unlockedAt;

  /// Wrap in a bordered card. Off when the row sits inside another card.
  final bool card;

  bool get unlocked => unlockedAt != null;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final shown = value > trophy.target ? trophy.target : value;
    final frac = trophy.target <= 0 ? 1.0 : shown / trophy.target;
    final tier = TierColors.of(trophy.tier);

    final row = Row(
      children: [
        TrophyMedal(trophy: trophy, unlocked: unlocked, size: 54),
        const SizedBox(width: 14),
        Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Flexible(
                    child: Text(
                      trophy.title,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: text.titleMedium?.copyWith(
                        color: unlocked ? c.ink : c.inkMuted,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding:
                        const EdgeInsets.symmetric(horizontal: 7, vertical: 2),
                    decoration: BoxDecoration(
                      color: (unlocked ? tier.body : c.hairline)
                          .withValues(alpha: 0.25),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      trophy.tier.label,
                      style: TextStyle(
                        fontSize: 10,
                        fontWeight: FontWeight.w800,
                        color: unlocked ? tier.body : c.inkMuted,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 2),
              Text(trophy.description, style: text.bodySmall),
              const SizedBox(height: 8),
              if (unlocked)
                Text(
                  'Earned ${shortDate(DateTime.fromMillisecondsSinceEpoch(unlockedAt!))} · +${trophy.tier.xp} XP',
                  style: text.bodySmall?.copyWith(
                    color: c.success,
                    fontWeight: FontWeight.w700,
                  ),
                )
              else
                Row(
                  children: [
                    Expanded(
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(6),
                        child: LinearProgressIndicator(
                          value: frac,
                          minHeight: 7,
                          backgroundColor: c.track,
                          valueColor: AlwaysStoppedAnimation(c.accent),
                        ),
                      ),
                    ),
                    const SizedBox(width: 10),
                    Text(
                      '${groupedInt(shown)} / ${groupedInt(trophy.target)}',
                      style: text.bodySmall?.copyWith(fontWeight: FontWeight.w700),
                    ),
                  ],
                ),
            ],
          ),
        ),
      ],
    );

    return Semantics(
      container: true,
      label: '${trophy.title}, ${trophy.tier.label}. ${trophy.description} '
          '${unlocked ? 'Earned.' : 'Progress ${groupedInt(shown)} of ${groupedInt(trophy.target)}.'}',
      child: card ? AppCard(child: row) : row,
    );
  }
}
