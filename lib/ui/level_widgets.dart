import 'package:flutter/material.dart';

import '../progress/xp_rules.dart';
import '../theme/app_theme.dart';
import 'gradients.dart';

/// A round badge with the level number in it.
class LevelBadge extends StatelessWidget {
  const LevelBadge({super.key, required this.level, this.size = 44});

  final int level;
  final double size;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      width: size,
      height: size,
      alignment: Alignment.center,
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        gradient: c.accentGradient,
        boxShadow: [
          BoxShadow(
            color: c.accent.withValues(alpha: 0.35),
            blurRadius: size * 0.3,
            offset: Offset(0, size * 0.08),
          ),
        ],
      ),
      child: Text(
        '$level',
        style: TextStyle(
          fontFamily: c.display,
          fontSize: size * 0.42,
          fontWeight: FontWeight.w800,
          color: c.onAccent,
          height: 1,
        ),
      ),
    );
  }
}

/// A rounded bar showing how far through the level the learner is.
class XpBar extends StatelessWidget {
  const XpBar({super.key, required this.info, this.height = 10});

  final LevelInfo info;
  final double height;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return TweenAnimationBuilder<double>(
      tween: Tween<double>(begin: 0, end: info.progress),
      duration: const Duration(milliseconds: 700),
      curve: Curves.easeOutCubic,
      builder: (context, v, _) => ClipRRect(
        borderRadius: BorderRadius.circular(height),
        child: SizedBox(
          height: height,
          child: Stack(
            fit: StackFit.expand,
            children: [
              ColoredBox(color: c.track),
              FractionallySizedBox(
                alignment: Alignment.centerLeft,
                widthFactor: v.clamp(0.0, 1.0),
                child: DecoratedBox(decoration: BoxDecoration(gradient: c.xpGradient)),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// "+35 XP", as a small pill.
class XpChip extends StatelessWidget {
  const XpChip(this.amount, {super.key, this.big = false});

  final int amount;
  final bool big;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return Container(
      padding: EdgeInsets.symmetric(horizontal: big ? 14 : 9, vertical: big ? 7 : 3),
      decoration: BoxDecoration(
        color: c.caution.withValues(alpha: 0.18),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          Icon(Icons.bolt, size: big ? 20 : 14, color: c.caution),
          const SizedBox(width: 3),
          Text(
            '+$amount XP',
            style: TextStyle(
              color: c.caution,
              fontWeight: FontWeight.w800,
              fontSize: big ? 17 : 12,
            ),
          ),
        ],
      ),
    );
  }
}
