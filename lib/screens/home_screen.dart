import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../data/app_settings.dart';
import '../data/deck_controller.dart';
import '../data/models.dart';
import '../data/study_stats.dart';
import '../lessons/lessons_screen.dart';
import '../progress/progress_service.dart';
import '../progress/trophies.dart';
import '../progress/trophy_progress.dart';
import '../theme/app_theme.dart';
import '../ui/action_tile.dart';
import '../ui/app_card.dart';
import '../ui/format.dart';
import '../ui/gradients.dart';
import '../ui/level_widgets.dart';
import '../ui/medal.dart';
import '../ui/progress_ring.dart';
import '../ui/streak_calendar.dart';
import '../ui/streak_flame.dart';
import '../ui/trophy_row.dart';
import '../widgets/deck_gate.dart';
import '../widgets/language_picker.dart';
import 'app_shell.dart';
import 'review_screen.dart';
import 'trophies_screen.dart';

/// The Home tab: today's goal, the streak, the level, and what to do next.
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) =>
      DeckGate(builder: (context, deck) => _HomeBody(deck: deck));
}

String _greeting(int hour) {
  if (hour < 5) return 'Up late';
  if (hour < 12) return 'Good morning';
  if (hour < 18) return 'Good afternoon';
  return 'Good evening';
}

class _HomeBody extends StatelessWidget {
  const _HomeBody({required this.deck});

  final Deck deck;

  void _openReview(BuildContext context) => Navigator.of(context).push(
        MaterialPageRoute(builder: (_) => ReviewScreen(deck: deck)),
      );

  void _openLessons(BuildContext context) => Navigator.of(context).push(
        MaterialPageRoute(builder: (_) => LessonsScreen(deck: deck)),
      );

  @override
  Widget build(BuildContext context) {
    final progress = context.watch<ProgressService>();
    final settings = context.watch<AppSettings>();
    final stats = context.watch<StudyStats>().statsFor(deck);
    final controller = context.watch<DeckController>();
    final c = context.lingo;
    final text = Theme.of(context).textTheme;

    final level = progress.level;
    final streak = progress.streak;
    final activity = ActivityView.of(progress);
    final name = settings.displayName;
    final greeting = _greeting(progress.now.hour);

    return Scaffold(
      body: SafeArea(
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: RefreshIndicator(
              onRefresh: () => context.read<StudyStats>().refresh(deck),
              child: ListView(
                padding: const EdgeInsets.fromLTRB(20, 14, 20, 32),
                children: [
                  // Header
                  Row(
                    children: [
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              name.isEmpty ? greeting : '$greeting, $name',
                              style: text.headlineSmall,
                              maxLines: 1,
                              overflow: TextOverflow.ellipsis,
                            ),
                            const SizedBox(height: 2),
                            Text('Level ${level.level} · ${level.title}',
                                style: text.bodySmall),
                          ],
                        ),
                      ),
                      const SizedBox(width: 12),
                      InkWell(
                        onTap: controller.isLoading
                            ? null
                            : () => LanguagePicker.show(context),
                        borderRadius: BorderRadius.circular(999),
                        child: Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 12, vertical: 8),
                          decoration: BoxDecoration(
                            color: c.raised,
                            border: Border.all(color: c.hairline),
                            borderRadius: BorderRadius.circular(999),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Text(controller.descriptor?.flag ?? '',
                                  style: const TextStyle(fontSize: 16)),
                              const SizedBox(width: 6),
                              Text(controller.descriptor?.languageName ?? '…',
                                  style: text.bodyMedium),
                              Icon(Icons.expand_more,
                                  size: 16, color: c.inkMuted),
                            ],
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 18),

                  // Daily goal
                  _GoalCard(
                    todayXp: progress.todayXp,
                    goal: progress.dailyGoal,
                    queued: stats?.queued,
                    onReview: () => _openReview(context),
                    onLessons: () => _openLessons(context),
                  ),
                  const SizedBox(height: 14),

                  // Streak
                  AppCard(
                    onTap: () =>
                        ShellScope.maybeOf(context)?.select(AppTab.profile),
                    child: Column(
                      children: [
                        Row(
                          children: [
                            StreakFlame(size: 46, lit: streak.current > 0),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    streak.current == 1
                                        ? '1 day streak'
                                        : '${streak.current} day streak',
                                    style: text.titleLarge,
                                  ),
                                  const SizedBox(height: 2),
                                  Text(
                                    _streakLine(streak.current, streak.doneToday,
                                        settings.streakNudge),
                                    style: text.bodySmall,
                                  ),
                                ],
                              ),
                            ),
                            if (streak.freezes > 0)
                              Tooltip(
                                message:
                                    '${streak.freezes} streak freeze${streak.freezes == 1 ? '' : 's'}: '
                                    'one is used automatically if you miss a day',
                                child: Container(
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
                                      Text('${streak.freezes}',
                                          style: const TextStyle(
                                            color: kFreezeBlue,
                                            fontWeight: FontWeight.w800,
                                          )),
                                    ],
                                  ),
                                ),
                              ),
                          ],
                        ),
                        const SizedBox(height: 16),
                        WeekStrip(activity: activity),
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
                                    child: Text(level.title,
                                        style: text.titleMedium),
                                  ),
                                  Text('${groupedInt(progress.totalXp)} XP',
                                      style: text.bodySmall?.copyWith(
                                          fontWeight: FontWeight.w700)),
                                ],
                              ),
                              const SizedBox(height: 8),
                              XpBar(info: level),
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

                  // What to do
                  const SectionHeader('Today'),
                  ActionTile(
                    icon: Icons.style_outlined,
                    title: 'Flashcards',
                    subtitle: stats == null
                        ? 'Loading…'
                        : stats.queued == 0
                            ? 'All caught up'
                            : '${stats.dueForReview} to review · ${stats.learning} learning'
                                '${stats.newCards > 0 ? ' · new available' : ''}',
                    badge: stats != null && stats.queued > 0
                        ? '${stats.queued}'
                        : null,
                    color: c.accent,
                    onTap: () => _openReview(context),
                  ),
                  const SizedBox(height: 10),
                  ActionTile(
                    icon: Icons.menu_book_outlined,
                    title: 'Lessons',
                    subtitle: 'Grammar and sentence building',
                    color: c.success,
                    onTap: () => _openLessons(context),
                  ),
                  const SizedBox(height: 10),
                  ActionTile(
                    icon: Icons.sports_esports_outlined,
                    title: 'Games',
                    subtitle: 'Lingo Ladder and Lingo Rally',
                    color: c.caution,
                    onTap: () =>
                        ShellScope.maybeOf(context)?.select(AppTab.games),
                  ),

                  // Trophies
                  _TrophiesSection(progress: progress),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  static String _streakLine(int current, bool doneToday, bool nudge) {
    if (current == 0) {
      return doneToday ? 'Streak started. Come back tomorrow.' : 'Study today to start one.';
    }
    if (doneToday) return 'Done for today. See you tomorrow.';
    return nudge ? 'Study today to keep it going.' : 'Keep it going.';
  }
}

class _GoalCard extends StatelessWidget {
  const _GoalCard({
    required this.todayXp,
    required this.goal,
    required this.queued,
    required this.onReview,
    required this.onLessons,
  });

  final int todayXp;
  final int goal;
  final int? queued;
  final VoidCallback onReview;
  final VoidCallback onLessons;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final reached = todayXp >= goal;
    final left = goal - todayXp;
    final hasCards = (queued ?? 0) > 0;

    return AppCard(
      gradient: c.accentGradient,
      shadow: true,
      padding: const EdgeInsets.all(18),
      child: Row(
        children: [
          ProgressRing(
            value: goal <= 0 ? 1 : todayXp / goal,
            size: 104,
            stroke: 11,
            color: c.onAccent,
            trackColor: c.onAccent.withValues(alpha: 0.22),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                if (reached)
                  Icon(Icons.check_rounded, color: c.onAccent, size: 34)
                else
                  Text(
                    '$todayXp',
                    style: TextStyle(
                      fontFamily: c.display,
                      fontSize: 28,
                      fontWeight: FontWeight.w800,
                      color: c.onAccent,
                      height: 1,
                    ),
                  ),
                const SizedBox(height: 2),
                Text(
                  reached ? '$todayXp XP' : 'of $goal XP',
                  style: TextStyle(
                    color: c.onAccent.withValues(alpha: 0.8),
                    fontSize: 12,
                    fontWeight: FontWeight.w600,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(width: 18),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  reached ? 'Daily goal reached' : 'Daily goal',
                  style: text.titleLarge?.copyWith(color: c.onAccent),
                ),
                const SizedBox(height: 4),
                Text(
                  reached
                      ? 'Nice work. Anything more is a bonus.'
                      : '$left XP to go today.',
                  style: text.bodyMedium?.copyWith(
                    color: c.onAccent.withValues(alpha: 0.85),
                  ),
                ),
                const SizedBox(height: 14),
                FilledButton(
                  style: FilledButton.styleFrom(
                    backgroundColor: c.onAccent,
                    foregroundColor: c.accent,
                    minimumSize: const Size(0, 44),
                  ),
                  onPressed: hasCards ? onReview : onLessons,
                  child: Text(hasCards
                      ? 'Review $queued ${queued == 1 ? 'card' : 'cards'}'
                      : 'Start a lesson'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _TrophiesSection extends StatelessWidget {
  const _TrophiesSection({required this.progress});

  final ProgressService progress;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final unlocked = progress.trophies;
    final recent = recentTrophies(unlocked, count: 5);
    final next = closestTrophies(unlocked, progress.metric, count: 2);

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        SectionHeader(
          'Trophies · ${unlocked.length}/${TrophyCatalog.all.length}',
          action: 'See all',
          onAction: () => Navigator.of(context).push(
            MaterialPageRoute(builder: (_) => const TrophiesScreen()),
          ),
        ),
        if (recent.isNotEmpty) ...[
          AppCard(
            child: Wrap(
              spacing: 14,
              runSpacing: 12,
              children: [
                for (final t in recent)
                  Tooltip(
                    message: t.title,
                    child: TrophyMedal(trophy: t, unlocked: true, size: 52),
                  ),
              ],
            ),
          ),
          const SizedBox(height: 10),
        ],
        if (next.isNotEmpty) ...[
          Padding(
            padding: const EdgeInsets.fromLTRB(2, 4, 2, 8),
            child: Text('Almost there', style: text.bodySmall?.copyWith(color: c.inkMuted)),
          ),
          for (final t in next) ...[
            TrophyProgressRow(trophy: t, value: progress.metric(t.metric)),
            const SizedBox(height: 10),
          ],
        ],
      ],
    );
  }
}
