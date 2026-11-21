import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/deck_controller.dart';
import '../data/models.dart';
import '../progress/progress_service.dart';
import '../progress/trophies.dart';
import '../progress/trophy_progress.dart';
import '../theme/app_theme.dart';
import '../ui/action_tile.dart';
import '../ui/app_card.dart';
import '../ui/daily_goal_sheet.dart';
import '../ui/format.dart';
import '../ui/gradients.dart';
import '../ui/level_widgets.dart';
import '../ui/medal.dart';
import '../ui/streak_calendar.dart';
import '../ui/streak_flame.dart';
import 'settings_screen.dart';
import 'trophies_screen.dart';

/// The Profile tab: who you are in the app, your numbers, and your history.
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final progress = context.watch<ProgressService>();
    final settings = context.watch<AppSettings>();
    final deck = context.watch<DeckController>().deck;
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    final level = progress.level;
    final streak = progress.streak;
    final activity = ActivityView.of(progress);
    final name = settings.displayName.trim();
    final unlocked = progress.trophies;

    int m(String key) => progress.metric(key);

    final stats = <_Stat>[
      _Stat(Icons.bolt, groupedInt(progress.totalXp), 'Total XP', c.caution),
      _Stat(Icons.local_fire_department, '${streak.current}', 'Day streak', c.accent),
      _Stat(Icons.military_tech, '${streak.best}', 'Best streak', c.accent),
      _Stat(Icons.style_outlined, groupedInt(m('cards_learned')), 'Words learned', c.success),
      _Stat(Icons.check_circle_outline, groupedInt(m('reviews')), 'Cards reviewed', c.success),
      _Stat(Icons.menu_book_outlined, groupedInt(m('lessons')), 'Lessons done', c.success),
      _Stat(Icons.sports_esports_outlined,
          groupedInt(m('ladder_played') + m('rally_played')), 'Games played', c.caution),
      _Stat(Icons.emoji_events_outlined,
          '${unlocked.length}/${TrophyCatalog.all.length}', 'Trophies', c.caution),
    ];

    final studiedLanguages = [
      for (final d in DeckDescriptor.all)
        if (m('deck_${d.id}') > 0) d,
    ];

    return Scaffold(
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: ListView(
              padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
              children: [
                // Header
                AppCard(
                  gradient: c.accentGradient,
                  shadow: true,
                  padding: const EdgeInsets.all(18),
                  child: Row(
                    children: [
                      Container(
                        width: 64,
                        height: 64,
                        alignment: Alignment.center,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          color: c.onAccent.withValues(alpha: 0.2),
                          border: Border.all(
                              color: c.onAccent.withValues(alpha: 0.6), width: 2),
                        ),
                        child: name.isEmpty
                            ? Icon(Icons.person_rounded, color: c.onAccent, size: 34)
                            : Text(
                                String.fromCharCode(name.runes.first).toUpperCase(),
                                style: TextStyle(
                                  fontFamily: c.display,
                                  fontSize: 30,
                                  fontWeight: FontWeight.w800,
                                  color: c.onAccent,
                                ),
                              ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              name.isEmpty ? 'Learner' : name,
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                              style: text.headlineSmall?.copyWith(color: c.onAccent),
                            ),
                            const SizedBox(height: 2),
                            Text(
                              'Level ${level.level} · ${level.title}',
                              style: text.bodyMedium?.copyWith(
                                  color: c.onAccent.withValues(alpha: 0.85)),
                            ),
                          ],
                        ),
                      ),
                      IconButton(
                        tooltip: 'Settings',
                        onPressed: deck == null
                            ? null
                            : () => Navigator.of(context).push(
                                  MaterialPageRoute(
                                      builder: (_) => SettingsScreen(deck: deck)),
                                ),
                        icon: Icon(Icons.settings_outlined, color: c.onAccent),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 14),

                // Level
                AppCard(
                  child: Row(
                    children: [
                      LevelBadge(level: level.level, size: 54),
                      const SizedBox(width: 14),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Row(
                              children: [
                                Expanded(
                                    child: Text('Level ${level.level}',
                                        style: text.titleMedium)),
                                Text(
                                  '${groupedInt(level.into)} / ${groupedInt(level.span)} XP',
                                  style: text.bodySmall
                                      ?.copyWith(fontWeight: FontWeight.w700),
                                ),
                              ],
                            ),
                            const SizedBox(height: 8),
                            XpBar(info: level, height: 12),
                            const SizedBox(height: 6),
                            Text(
                              '${groupedInt(level.remaining)} XP to level ${level.level + 1}',
                              style: text.bodySmall,
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),

                // Numbers
                const SectionHeader('Your numbers'),
                LayoutBuilder(
                  builder: (context, box) {
                    const gap = 10.0;
                    final cols = box.maxWidth >= 560 ? 4 : 2;
                    final w = (box.maxWidth - gap * (cols - 1)) / cols;
                    return Wrap(
                      spacing: gap,
                      runSpacing: gap,
                      children: [
                        for (final s in stats)
                          SizedBox(width: w, child: _StatTile(stat: s)),
                      ],
                    );
                  },
                ),

                // Streak
                const SectionHeader('Streak'),
                AppCard(
                  child: Column(
                    children: [
                      Row(
                        children: [
                          StreakFlame(size: 40, lit: streak.current > 0),
                          const SizedBox(width: 12),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  streak.current == 1
                                      ? '1 day'
                                      : '${streak.current} days',
                                  style: text.titleLarge,
                                ),
                                Text('Best: ${streak.best}', style: text.bodySmall),
                              ],
                            ),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(
                                horizontal: 10, vertical: 6),
                            decoration: BoxDecoration(
                              color: kFreezeBlue.withValues(alpha: 0.16),
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                const Icon(Icons.ac_unit,
                                    size: 16, color: kFreezeBlue),
                                const SizedBox(width: 4),
                                Text(
                                  '${streak.freezes} ${streak.freezes == 1 ? 'freeze' : 'freezes'}',
                                  style: const TextStyle(
                                    color: kFreezeBlue,
                                    fontWeight: FontWeight.w800,
                                    fontSize: 12,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Align(
                        alignment: Alignment.centerLeft,
                        child: Text(
                          'Every 7 days of streak earns a freeze (up to 2). '
                          'If you miss a day, one is used automatically.',
                          style: text.bodySmall,
                        ),
                      ),
                      const SizedBox(height: 12),
                      StreakCalendar(activity: activity),
                    ],
                  ),
                ),

                // Heatmap
                const SectionHeader('Activity'),
                AppCard(child: ActivityHeatmap(activity: activity)),
                const SizedBox(height: 10),
                ActionTile(
                  icon: Icons.flag_outlined,
                  title: 'Daily goal',
                  subtitle: '${progress.dailyGoal} XP a day · tap to change',
                  color: c.accent,
                  onTap: () => DailyGoalSheet.show(context),
                ),

                // Trophies
                SectionHeader(
                  'Trophies · ${unlocked.length}/${TrophyCatalog.all.length}',
                  action: 'See all',
                  onAction: () => Navigator.of(context).push(
                    MaterialPageRoute(builder: (_) => const TrophiesScreen()),
                  ),
                ),
                AppCard(
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(builder: (_) => const TrophiesScreen()),
                  ),
                  child: unlocked.isEmpty
                      ? Text(
                          'No trophies yet. Review a few cards and your first one is close.',
                          style: text.bodyMedium,
                        )
                      : Wrap(
                          spacing: 14,
                          runSpacing: 12,
                          children: [
                            for (final t in recentTrophies(unlocked, count: 8))
                              Tooltip(
                                message: t.title,
                                child: TrophyMedal(
                                    trophy: t, unlocked: true, size: 52),
                              ),
                          ],
                        ),
                ),

                // Languages
                if (studiedLanguages.isNotEmpty) ...[
                  const SectionHeader('Languages'),
                  Wrap(
                    spacing: 8,
                    runSpacing: 8,
                    children: [
                      for (final d in studiedLanguages)
                        Chip(
                          avatar: Text(d.flag, style: const TextStyle(fontSize: 15)),
                          label: Text(d.languageName),
                          backgroundColor: c.raised,
                          side: BorderSide(color: c.hairline),
                        ),
                    ],
                  ),
                ],
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class _Stat {
  const _Stat(this.icon, this.value, this.label, this.color);

  final IconData icon;
  final String value;
  final String label;
  final Color color;
}

class _StatTile extends StatelessWidget {
  const _StatTile({required this.stat});

  final _Stat stat;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    return Semantics(
      container: true,
      label: '${stat.label}: ${stat.value}',
      excludeSemantics: true,
      child: AppCard(
        padding: const EdgeInsets.all(14),
        child: Row(
          children: [
            Container(
              width: 38,
              height: 38,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: stat.color.withValues(alpha: 0.16),
              ),
              child: Icon(stat.icon, color: stat.color, size: 20),
            ),
            const SizedBox(width: 10),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  FittedBox(
                    fit: BoxFit.scaleDown,
                    alignment: Alignment.centerLeft,
                    child: Text(
                      stat.value,
                      style: TextStyle(
                        fontFamily: c.display,
                        fontSize: 20,
                        fontWeight: FontWeight.w800,
                        color: c.ink,
                      ),
                    ),
                  ),
                  Text(stat.label,
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: text.bodySmall),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
