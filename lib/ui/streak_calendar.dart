import 'package:flutter/material.dart';

import '../progress/progress_service.dart';
import '../progress/streak.dart';
import '../theme/app_theme.dart';
import 'gradients.dart';

/// What happened on a day, for the calendar, the week strip and the heatmap.
enum DayStatus { none, active, goal, frozen }

/// Colour used for a day a streak freeze covered.
const Color kFreezeBlue = Color(0xFF6CC4FF);

const List<String> _monthNames = [
  'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
  'September', 'October', 'November', 'December',
];
const List<String> _monthShort = [
  'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov',
  'Dec',
];
const List<String> _weekdayLetters = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];

/// A read-only picture of the learner's days, taken from the progress service.
class ActivityView {
  const ActivityView({
    required this.dailyXp,
    required this.frozen,
    required this.goal,
    required this.today,
  });

  factory ActivityView.of(ProgressService p) => ActivityView(
        dailyXp: p.dailyXp,
        frozen: p.streak.frozenDays,
        goal: p.dailyGoal,
        today: p.now,
      );

  final Map<String, int> dailyXp;
  final Set<String> frozen;
  final int goal;
  final DateTime today;

  int xpOn(DateTime d) => dailyXp[dayKey(d)] ?? 0;

  DayStatus statusOf(DateTime d) {
    final k = dayKey(d);
    final xp = dailyXp[k] ?? 0;
    if (xp >= goal) return DayStatus.goal;
    if (xp > 0) return DayStatus.active;
    if (frozen.contains(k)) return DayStatus.frozen;
    return DayStatus.none;
  }

  bool isToday(DateTime d) => dayKey(d) == dayKey(today);

  bool isFuture(DateTime d) => daysBetween(today, d) > 0;
}

String monthName(int month) => _monthNames[month - 1];

// -----------------------------------------------------------------------------
// Month calendar
// -----------------------------------------------------------------------------

/// A month at a time, with arrows to go back through the last year. Flames for
/// days with study, a gradient flame for days that reached the goal, a
/// snowflake for days a freeze saved.
class StreakCalendar extends StatefulWidget {
  const StreakCalendar({super.key, required this.activity});

  final ActivityView activity;

  @override
  State<StreakCalendar> createState() => _StreakCalendarState();
}

class _StreakCalendarState extends State<StreakCalendar> {
  late DateTime _month =
      DateTime(widget.activity.today.year, widget.activity.today.month);

  void _go(int delta) =>
      setState(() => _month = DateTime(_month.year, _month.month + delta));

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final a = widget.activity;

    final daysInMonth = DateTime(_month.year, _month.month + 1, 0).day;
    final lead = (_month.weekday + 6) % 7; // Monday first
    final rows = ((lead + daysInMonth) / 7).ceil();
    final thisMonth = DateTime(a.today.year, a.today.month);
    final earliest = DateTime(a.today.year, a.today.month - 11);
    final canForward = _month.isBefore(thisMonth);
    final canBack = _month.isAfter(earliest);

    var activeDays = 0;
    var goalDays = 0;
    for (var d = 1; d <= daysInMonth; d++) {
      final s = a.statusOf(DateTime(_month.year, _month.month, d));
      if (s == DayStatus.active || s == DayStatus.goal) activeDays++;
      if (s == DayStatus.goal) goalDays++;
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        Row(
          children: [
            IconButton(
              tooltip: 'Previous month',
              onPressed: canBack ? () => _go(-1) : null,
              icon: const Icon(Icons.chevron_left),
            ),
            Expanded(
              child: Text(
                '${monthName(_month.month)} ${_month.year}',
                textAlign: TextAlign.center,
                style: text.titleMedium,
              ),
            ),
            IconButton(
              tooltip: 'Next month',
              onPressed: canForward ? () => _go(1) : null,
              icon: const Icon(Icons.chevron_right),
            ),
          ],
        ),
        const SizedBox(height: 6),
        Row(
          children: [
            for (final letter in _weekdayLetters)
              Expanded(
                child: Center(
                  child: Text(letter,
                      style: text.bodySmall?.copyWith(fontWeight: FontWeight.w700)),
                ),
              ),
          ],
        ),
        const SizedBox(height: 4),
        for (var r = 0; r < rows; r++)
          Row(
            children: [
              for (var col = 0; col < 7; col++)
                Expanded(
                  child: _cellFor(a, r * 7 + col - lead + 1, daysInMonth),
                ),
            ],
          ),
        const SizedBox(height: 10),
        Text(
          activeDays == 0
              ? 'No study this month.'
              : '$activeDays ${activeDays == 1 ? 'day' : 'days'} studied'
                  '${goalDays > 0 ? ' · $goalDays on goal' : ''}',
          textAlign: TextAlign.center,
          style: text.bodySmall?.copyWith(color: c.inkMuted),
        ),
      ],
    );
  }

  Widget _cellFor(ActivityView a, int day, int daysInMonth) {
    if (day < 1 || day > daysInMonth) {
      return const AspectRatio(aspectRatio: 1, child: SizedBox.shrink());
    }
    final date = DateTime(_month.year, _month.month, day);
    return _DayCell(
      day: day,
      status: a.statusOf(date),
      isToday: a.isToday(date),
      isFuture: a.isFuture(date),
    );
  }
}

class _DayCell extends StatelessWidget {
  const _DayCell({
    required this.day,
    required this.status,
    required this.isToday,
    required this.isFuture,
  });

  final int day;
  final DayStatus status;
  final bool isToday;
  final bool isFuture;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final label = switch (status) {
      DayStatus.goal => 'goal reached',
      DayStatus.active => 'studied',
      DayStatus.frozen => 'saved by a streak freeze',
      DayStatus.none => isFuture ? '' : 'no study',
    };

    Widget face;
    switch (status) {
      case DayStatus.goal:
        face = _disc(
          gradient: c.accentGradient,
          child: Icon(Icons.local_fire_department, color: c.onAccent, size: 20),
        );
      case DayStatus.active:
        face = _disc(
          border: Border.all(color: c.accent, width: 2),
          child: Icon(Icons.local_fire_department, color: c.accent, size: 20),
        );
      case DayStatus.frozen:
        face = _disc(
          color: kFreezeBlue.withValues(alpha: 0.2),
          border: Border.all(color: kFreezeBlue, width: 2),
          child: const Icon(Icons.ac_unit, color: kFreezeBlue, size: 18),
        );
      case DayStatus.none:
        face = _disc(
          border: isToday ? Border.all(color: c.ink, width: 2) : null,
          child: Text(
            '$day',
            style: TextStyle(
              fontSize: 13,
              fontWeight: isToday ? FontWeight.w800 : FontWeight.w500,
              color: isFuture ? c.inkMuted.withValues(alpha: 0.4) : c.inkMuted,
            ),
          ),
        );
    }

    return Semantics(
      label: 'Day $day, $label',
      excludeSemantics: true,
      child: Padding(
        padding: const EdgeInsets.all(3),
        child: AspectRatio(aspectRatio: 1, child: face),
      ),
    );
  }

  Widget _disc({
    Widget? child,
    Color? color,
    Gradient? gradient,
    Border? border,
  }) =>
      Container(
        alignment: Alignment.center,
        decoration: BoxDecoration(
          shape: BoxShape.circle,
          color: color,
          gradient: gradient,
          border: border,
        ),
        child: child,
      );
}

// -----------------------------------------------------------------------------
// Week strip
// -----------------------------------------------------------------------------

/// Monday to Sunday of the current week, a flame on each day studied.
class WeekStrip extends StatelessWidget {
  const WeekStrip({super.key, required this.activity});

  final ActivityView activity;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final today = activity.today;
    final monday = addDays(DateTime(today.year, today.month, today.day),
        -((today.weekday + 6) % 7));

    return Row(
      children: [
        for (var i = 0; i < 7; i++)
          Expanded(
            child: _weekDay(context, c, text, addDays(monday, i), i),
          ),
      ],
    );
  }

  Widget _weekDay(BuildContext context, LingoColors c, TextTheme text,
      DateTime date, int i) {
    final status = activity.statusOf(date);
    final isToday = activity.isToday(date);
    final future = activity.isFuture(date);
    final done = status == DayStatus.active || status == DayStatus.goal;
    final frozen = status == DayStatus.frozen;

    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text(
          _weekdayLetters[i],
          style: text.bodySmall?.copyWith(
            fontWeight: isToday ? FontWeight.w800 : FontWeight.w500,
            color: isToday ? c.ink : c.inkMuted,
          ),
        ),
        const SizedBox(height: 6),
        Container(
          width: 34,
          height: 34,
          alignment: Alignment.center,
          decoration: BoxDecoration(
            shape: BoxShape.circle,
            gradient: status == DayStatus.goal ? c.accentGradient : null,
            color: frozen
                ? kFreezeBlue.withValues(alpha: 0.2)
                : (done && status != DayStatus.goal
                    ? c.accent.withValues(alpha: 0.18)
                    : null),
            border: Border.all(
              color: frozen
                  ? kFreezeBlue
                  : done
                      ? c.accent
                      : (isToday ? c.ink : c.hairline),
              width: isToday || done || frozen ? 2 : 1,
            ),
          ),
          child: done
              ? Icon(
                  Icons.local_fire_department,
                  size: 19,
                  color: status == DayStatus.goal ? c.onAccent : c.accent,
                )
              : frozen
                  ? const Icon(Icons.ac_unit, size: 17, color: kFreezeBlue)
                  : (future
                      ? null
                      : Icon(Icons.circle,
                          size: 6, color: c.inkMuted.withValues(alpha: 0.5))),
        ),
      ],
    );
  }
}

// -----------------------------------------------------------------------------
// Heatmap
// -----------------------------------------------------------------------------

/// The last [weeks] weeks as a grid of small squares, darker for more XP, like
/// a contribution graph. Columns are weeks (Monday at the top).
class ActivityHeatmap extends StatelessWidget {
  const ActivityHeatmap({super.key, required this.activity, this.weeks = 18});

  final ActivityView activity;
  final int weeks;

  Color _shade(LingoColors c, int xp) {
    if (xp <= 0) return c.track;
    final goal = activity.goal <= 0 ? 60 : activity.goal;
    if (xp < goal * 0.5) return c.accent.withValues(alpha: 0.30);
    if (xp < goal) return c.accent.withValues(alpha: 0.55);
    if (xp < goal * 2) return c.accent;
    return c.accent2;
  }

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final text = Theme.of(context).textTheme;
    final today = DateTime(
        activity.today.year, activity.today.month, activity.today.day);
    final thisMonday = addDays(today, -((today.weekday + 6) % 7));
    final firstMonday = addDays(thisMonday, -7 * (weeks - 1));

    return LayoutBuilder(
      builder: (context, box) {
        const gap = 3.0;
        final cell =
            ((box.maxWidth - gap * (weeks - 1)) / weeks).clamp(6.0, 22.0);

        // A month label above the first week that starts in a new month.
        final labels = <Widget>[];
        var lastMonth = -1;
        for (var w = 0; w < weeks; w++) {
          final monday = addDays(firstMonday, 7 * w);
          final show = monday.month != lastMonth && monday.day <= 7 ||
              (w == 0 && monday.month != lastMonth);
          lastMonth = monday.month;
          labels.add(SizedBox(
            width: cell + (w == weeks - 1 ? 0 : gap),
            child: show
                ? OverflowBox(
                    alignment: Alignment.centerLeft,
                    maxWidth: 40,
                    child: Text(_monthShort[monday.month - 1],
                        maxLines: 1,
                        softWrap: false,
                        style: text.bodySmall?.copyWith(fontSize: 10)),
                  )
                : null,
          ));
        }

        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            SizedBox(height: 14, child: Row(children: labels)),
            const SizedBox(height: 4),
            Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                for (var w = 0; w < weeks; w++)
                  Padding(
                    padding: EdgeInsets.only(right: w == weeks - 1 ? 0 : gap),
                    child: Column(
                      children: [
                        for (var d = 0; d < 7; d++)
                          _square(c, addDays(firstMonday, 7 * w + d), cell, gap),
                      ],
                    ),
                  ),
              ],
            ),
            const SizedBox(height: 10),
            Row(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Text('Less', style: text.bodySmall?.copyWith(fontSize: 11)),
                const SizedBox(width: 6),
                for (final xp in [0, 1, activity.goal ~/ 2 + 1, activity.goal, activity.goal * 2])
                  Container(
                    width: 11,
                    height: 11,
                    margin: const EdgeInsets.only(right: 3),
                    decoration: BoxDecoration(
                      color: _shade(c, xp),
                      borderRadius: BorderRadius.circular(3),
                    ),
                  ),
                const SizedBox(width: 3),
                Text('More', style: text.bodySmall?.copyWith(fontSize: 11)),
              ],
            ),
          ],
        );
      },
    );
  }

  Widget _square(LingoColors c, DateTime date, double cell, double gap) {
    if (activity.isFuture(date)) {
      return SizedBox(width: cell, height: cell + gap);
    }
    final xp = activity.xpOn(date);
    final frozen = xp == 0 && activity.frozen.contains(dayKey(date));
    return Padding(
      padding: EdgeInsets.only(bottom: gap),
      child: Tooltip(
        message: '${_monthShort[date.month - 1]} ${date.day}: $xp XP',
        child: Container(
          width: cell,
          height: cell,
          decoration: BoxDecoration(
            color: frozen ? kFreezeBlue.withValues(alpha: 0.5) : _shade(c, xp),
            borderRadius: BorderRadius.circular(cell > 12 ? 4 : 2),
          ),
        ),
      ),
    );
  }
}
