import 'package:flutter/material.dart';

import '../srs/scheduler.dart';
import '../theme/app_theme.dart';

/// The four Anki-style grading buttons, each labelled with the interval it
/// would schedule. Showing the cost up front is most of what makes grading
/// feel honest rather than arbitrary.
class GradeButtons extends StatelessWidget {
  const GradeButtons({
    super.key,
    required this.preview,
    required this.now,
    required this.onGrade,
    this.showHard = true,
  });

  final SchedulingPreview preview;
  final DateTime now;
  final void Function(Grade) onGrade;

  /// Hiding Hard leaves a simpler three-button layout, which some learners
  /// prefer and which matches the Pulse mockup.
  final bool showHard;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final grades = showHard
        ? Grade.values
        : [Grade.again, Grade.good, Grade.easy];

    return Row(
      children: [
        for (final g in grades) ...[
          Expanded(
            child: _GradeButton(
              grade: g,
              interval: formatInterval(preview[g], now),
              filled: g != Grade.again,
              background: switch (g) {
                Grade.again => Colors.transparent,
                Grade.hard => c.hairline,
                Grade.good => c.success,
                Grade.easy => c.caution,
              },
              foreground: switch (g) {
                Grade.again => c.accent,
                Grade.hard => c.ink,
                Grade.good => c.onSuccess,
                Grade.easy => c.onCaution,
              },
              border: g == Grade.again ? c.accent : null,
              onPressed: () => onGrade(g),
            ),
          ),
          if (g != grades.last) const SizedBox(width: 10),
        ],
      ],
    );
  }
}

class _GradeButton extends StatelessWidget {
  const _GradeButton({
    required this.grade,
    required this.interval,
    required this.filled,
    required this.background,
    required this.foreground,
    required this.onPressed,
    this.border,
  });

  final Grade grade;
  final String interval;
  final bool filled;
  final Color background;
  final Color foreground;
  final Color? border;
  final VoidCallback onPressed;

  static const _labels = {
    Grade.again: 'Again',
    Grade.hard: 'Hard',
    Grade.good: 'Good',
    Grade.easy: 'Easy',
  };

  @override
  Widget build(BuildContext context) {
    final label = _labels[grade]!;
    return Semantics(
      button: true,
      label: '$label, next review in $interval',
      excludeSemantics: true,
      child: Material(
        color: background,
        shape: StadiumBorder(
          side: border == null
              ? BorderSide.none
              : BorderSide(color: border!, width: 1.5),
        ),
        clipBehavior: Clip.antiAlias,
        child: InkWell(
          onTap: onPressed,
          child: Container(
            constraints: const BoxConstraints(minHeight: 56),
            alignment: Alignment.center,
            padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 4),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  label,
                  style: TextStyle(
                    color: foreground,
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                  ),
                ),
                const SizedBox(height: 2),
                Text(
                  interval,
                  style: TextStyle(
                    color: foreground.withValues(alpha: 0.85),
                    fontSize: 11,
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
