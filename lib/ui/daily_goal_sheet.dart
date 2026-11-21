import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../progress/xp_rules.dart';
import '../theme/app_theme.dart';

/// Pick how much XP counts as a good day.
class DailyGoalSheet extends StatelessWidget {
  const DailyGoalSheet({super.key});

  static Future<void> show(BuildContext context) => showModalBottomSheet<void>(
        context: context,
        isScrollControlled: true,
        backgroundColor: context.lingo.raised,
        shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
        ),
        builder: (_) => const DailyGoalSheet(),
      );

  /// A rough idea of the time each goal takes, for the labels.
  static String minutesFor(int xp) {
    final m = (xp / 6).round();
    return 'about $m minutes';
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final settings = context.watch<AppSettings>();

    return SafeArea(
      child: SingleChildScrollView(
        padding: const EdgeInsets.fromLTRB(20, 20, 20, 12),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text('Daily goal', style: text.titleLarge),
            const SizedBox(height: 4),
            Text('XP to earn each day. Reach it to keep the ring full.',
                style: text.bodySmall),
            const SizedBox(height: 12),
            for (final (label, xp) in XpRules.goalPresets)
              RadioListTile<int>(
                value: xp,
                groupValue: settings.dailyGoal,
                activeColor: c.accent,
                contentPadding: EdgeInsets.zero,
                title: Text('$label · $xp XP', style: text.titleMedium),
                subtitle: Text(minutesFor(xp), style: text.bodySmall),
                onChanged: (v) {
                  if (v == null) return;
                  settings.dailyGoal = v;
                  Navigator.of(context).pop();
                },
              ),
          ],
        ),
      ),
    );
  }
}
