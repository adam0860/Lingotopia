import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../progress/progress_service.dart';
import '../progress/trophies.dart';
import '../theme/app_theme.dart';
import '../ui/app_card.dart';
import '../ui/format.dart';
import '../ui/medal.dart';
import '../ui/trophy_row.dart';

/// Every trophy in the app, by category, with progress towards the locked ones.
class TrophiesScreen extends StatefulWidget {
  const TrophiesScreen({super.key});

  @override
  State<TrophiesScreen> createState() => _TrophiesScreenState();
}

class _TrophiesScreenState extends State<TrophiesScreen> {
  TrophyCategory? _category; // null = all

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final progress = context.watch<ProgressService>();
    final unlocked = progress.trophies;

    final shown = [
      for (final t in TrophyCatalog.all)
        if (_category == null || t.category == _category) t,
    ];

    final byTier = {for (final tier in TrophyTier.values) tier: 0};
    var trophyXp = 0;
    for (final id in unlocked.keys) {
      final t = TrophyCatalog.byId(id);
      if (t == null) continue;
      byTier[t.tier] = (byTier[t.tier] ?? 0) + 1;
      trophyXp += t.tier.xp;
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Trophies')),
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 4, 20, 32),
              children: [
                AppCard(
                  child: Column(
                    children: [
                      Text(
                        '${unlocked.length} of ${TrophyCatalog.all.length} earned',
                        style: text.titleLarge,
                      ),
                      const SizedBox(height: 4),
                      Text('${groupedInt(trophyXp)} bonus XP from trophies',
                          style: text.bodySmall),
                      const SizedBox(height: 14),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceAround,
                        children: [
                          for (final tier in TrophyTier.values)
                            Column(
                              children: [
                                Container(
                                  width: 30,
                                  height: 30,
                                  decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    gradient: LinearGradient(
                                      colors: [
                                        TierColors.of(tier).light,
                                        TierColors.of(tier).body,
                                      ],
                                    ),
                                    border: Border.all(
                                        color: TierColors.of(tier).edge, width: 1.5),
                                  ),
                                ),
                                const SizedBox(height: 6),
                                Text('${byTier[tier]}',
                                    style: text.titleMedium),
                                Text(tier.label, style: text.bodySmall),
                              ],
                            ),
                        ],
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 14),
                SizedBox(
                  height: 42,
                  child: ListView(
                    scrollDirection: Axis.horizontal,
                    children: [
                      Padding(
                        padding: const EdgeInsets.only(right: 8),
                        child: ChoiceChip(
                          label: const Text('All'),
                          selected: _category == null,
                          onSelected: (_) => setState(() => _category = null),
                          selectedColor: c.accent.withValues(alpha: 0.25),
                        ),
                      ),
                      for (final cat in TrophyCatalog.categories)
                        Padding(
                          padding: const EdgeInsets.only(right: 8),
                          child: ChoiceChip(
                            label: Text(cat.label),
                            selected: _category == cat,
                            onSelected: (_) => setState(() => _category = cat),
                            selectedColor: c.accent.withValues(alpha: 0.25),
                          ),
                        ),
                    ],
                  ),
                ),
                const SizedBox(height: 12),
                for (final t in shown) ...[
                  TrophyProgressRow(
                    trophy: t,
                    value: progress.metric(t.metric),
                    unlockedAt: unlocked[t.id],
                  ),
                  const SizedBox(height: 10),
                ],
              ],
            ),
          ),
        ),
      ),
    );
  }
}
