import 'package:flutter_test/flutter_test.dart';

import 'package:lingotopia/progress/progress_engine.dart';
import 'package:lingotopia/progress/progress_models.dart';
import 'package:lingotopia/progress/progress_session.dart';
import 'package:lingotopia/progress/trophy_progress.dart';
import 'package:lingotopia/srs/scheduler.dart';
import 'package:lingotopia/theme/app_theme.dart';
import 'package:lingotopia/ui/format.dart';
import 'package:lingotopia/ui/streak_calendar.dart';

void main() {
  group('groupedInt', () {
    test('adds thousands separators', () {
      expect(groupedInt(0), '0');
      expect(groupedInt(999), '999');
      expect(groupedInt(1000), '1,000');
      expect(groupedInt(1234567), '1,234,567');
      expect(groupedInt(-4321), '-4,321');
    });
  });

  group('ActivityView', () {
    final view = ActivityView(
      dailyXp: const {'2026-11-03': 70, '2026-11-02': 20},
      frozen: const {'2026-11-01'},
      goal: 60,
      today: DateTime(2026, 11, 3, 15),
    );

    test('tells goal, studied, frozen and idle days apart', () {
      expect(view.statusOf(DateTime(2026, 11, 3)), DayStatus.goal);
      expect(view.statusOf(DateTime(2026, 11, 2)), DayStatus.active);
      expect(view.statusOf(DateTime(2026, 11, 1)), DayStatus.frozen);
      expect(view.statusOf(DateTime(2026, 10, 31)), DayStatus.none);
    });

    test('knows today and the future', () {
      expect(view.isToday(DateTime(2026, 11, 3, 23, 59)), isTrue);
      expect(view.isToday(DateTime(2026, 11, 2)), isFalse);
      expect(view.isFuture(DateTime(2026, 11, 4)), isTrue);
      expect(view.isFuture(DateTime(2026, 11, 3)), isFalse);
    });

    test('reports the XP on a day', () {
      expect(view.xpOn(DateTime(2026, 11, 2)), 20);
      expect(view.xpOn(DateTime(2026, 10, 1)), 0);
    });
  });

  group('trophy helpers', () {
    int metric(String key) => switch (key) {
          'streak_best' => 6,
          'xp_total' => 450,
          'level' => 1,
          _ => 0,
        };

    test('closestTrophies picks the nearest locked ones, nearest first', () {
      final next = closestTrophies({'streak_best_3': 1}, metric, count: 2);
      expect(next.map((t) => t.id).toList(), ['xp_total_500', 'streak_best_7']);
    });

    test('closestTrophies skips trophies already earned', () {
      final next = closestTrophies(
          {'streak_best_3': 1, 'xp_total_500': 1}, metric, count: 1);
      expect(next.single.id, 'streak_best_7');
    });

    test('recentTrophies is newest first and ignores unknown ids', () {
      final recent = recentTrophies(
        {'streak_best_3': 100, 'xp_total_500': 300, 'gone_forever_9': 999},
        count: 5,
      );
      expect(recent.map((t) => t.id).toList(), ['xp_total_500', 'streak_best_3']);
    });
  });

  group('ProgressSession', () {
    test('adds up what an event earned, trophies included', () {
      final engine = ProgressEngine(ProgressState(), dailyGoal: () => 60);
      final delta = engine.apply(
        ProgressEvent.review(grade: Grade.good, wasNew: true, deckId: 'ru_core'),
        DateTime(2026, 11, 3, 12),
      );
      final session = ProgressSession(startLevel: 1)..add(delta);
      expect(session.xp, delta.xpGained);
      expect(session.actions, 1);
      expect(session.trophies.length, delta.newTrophies.length);
      expect(session.level, delta.levelAfter);
    });
  });

  group('accent colours', () {
    test('an index overrides the skin accent', () {
      expect(AppTheme.colorsFor(AppSkin.wayfareDark, accentIndex: 0).accent,
          AppAccents.all[0].onDark);
      expect(AppTheme.colorsFor(AppSkin.wayfareLight, accentIndex: 0).accent,
          AppAccents.all[0].onLight);
    });

    test('-1 and out-of-range keep the skin accent', () {
      final base = AppTheme.colorsFor(AppSkin.pulse).accent;
      expect(AppTheme.colorsFor(AppSkin.pulse, accentIndex: -1).accent, base);
      expect(AppTheme.colorsFor(AppSkin.pulse, accentIndex: 99).accent, base);
    });
  });
}
