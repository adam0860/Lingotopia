import 'package:flutter/material.dart';

import '../progress/trophies.dart';
import '../theme/app_theme.dart';

/// Colours for each trophy tier: a light highlight and a deeper body.
class TierColors {
  const TierColors(this.light, this.body, this.edge);

  final Color light;
  final Color body;
  final Color edge;

  static TierColors of(TrophyTier t) => switch (t) {
        TrophyTier.bronze =>
          const TierColors(Color(0xFFF0B27C), Color(0xFFC77B3C), Color(0xFF8A4F22)),
        TrophyTier.silver =>
          const TierColors(Color(0xFFF1F4F8), Color(0xFFAAB6C4), Color(0xFF6F7C8A)),
        TrophyTier.gold =>
          const TierColors(Color(0xFFFFE98F), Color(0xFFE0B03A), Color(0xFF9A7414)),
        TrophyTier.platinum =>
          const TierColors(Color(0xFFE2F8FF), Color(0xFF63CFE3), Color(0xFF2C8DA3)),
      };
}

/// A round medal for a trophy. Locked ones are grey with a padlock.
class TrophyMedal extends StatelessWidget {
  const TrophyMedal({
    super.key,
    required this.trophy,
    required this.unlocked,
    this.size = 64,
  });

  final Trophy trophy;
  final bool unlocked;
  final double size;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    final t = TierColors.of(trophy.tier);
    final locked = !unlocked;

    final light = locked ? c.track : t.light;
    final body = locked ? c.hairline : t.body;
    final edge = locked ? c.hairline : t.edge;
    final iconColor = locked ? c.inkMuted.withValues(alpha: 0.6) : Colors.white;

    return SizedBox(
      width: size,
      height: size,
      child: Stack(
        alignment: Alignment.center,
        children: [
          Container(
            width: size,
            height: size,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [light, body],
              ),
              border: Border.all(color: edge, width: size * 0.045),
              boxShadow: locked
                  ? null
                  : [
                      BoxShadow(
                        color: body.withValues(alpha: 0.45),
                        blurRadius: size * 0.22,
                        offset: Offset(0, size * 0.06),
                      ),
                    ],
            ),
          ),
          Container(
            width: size * 0.72,
            height: size * 0.72,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              border: Border.all(
                color: Colors.white.withValues(alpha: locked ? 0.08 : 0.35),
                width: size * 0.02,
              ),
            ),
          ),
          Icon(
            trophy.icon,
            size: size * 0.46,
            color: iconColor,
            shadows: locked
                ? null
                : [Shadow(color: edge.withValues(alpha: 0.7), blurRadius: 3)],
          ),
          if (locked)
            Positioned(
              right: size * 0.02,
              bottom: size * 0.02,
              child: Container(
                padding: EdgeInsets.all(size * 0.06),
                decoration: BoxDecoration(color: c.raised, shape: BoxShape.circle),
                child: Icon(Icons.lock, size: size * 0.2, color: c.inkMuted),
              ),
            ),
        ],
      ),
    );
  }
}
