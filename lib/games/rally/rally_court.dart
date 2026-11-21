import 'dart:math';

import 'package:flutter/material.dart';

import '../../theme/app_theme.dart';
import 'rally_models.dart';

/// Where everything is at one instant of the rally. The screen builds one of
/// these every animation frame; the painter just draws it.
class CourtFrame {
  const CourtFrame({
    required this.ballX,
    required this.phase,
    required this.towards,
    this.smash = false,
    this.missed,
    this.flash = 0,
    this.youShield = false,
    this.botShield = false,
    this.youCharged = false,
    this.botCharged = false,
  });

  /// 0 is your paddle, 1 is the opponent's. Past those values the ball has
  /// gone through.
  final double ballX;

  /// Varies the ball's path from rally to rally.
  final double phase;

  /// The side the ball is travelling towards (the one that must answer).
  final RallySide towards;

  final bool smash;

  /// The side whose paddle just failed to return the ball.
  final RallySide? missed;

  /// 0..1 strength of the goal flash behind [missed].
  final double flash;

  final bool youShield;
  final bool botShield;

  /// A smash is charged for this side's next return.
  final bool youCharged;
  final bool botCharged;
}

/// The pong court: two paddles, a ball that wobbles across the court, and a
/// flash when someone is scored on. It carries no information the HUD does not
/// also show, so it can be ignored by screen readers.
class RallyCourtPainter extends CustomPainter {
  RallyCourtPainter({
    required this.frame,
    required this.youColor,
    required this.botColor,
    required this.lineColor,
    required this.ballColor,
    required this.smashColor,
    required this.shieldColor,
  });

  final CourtFrame frame;
  final Color youColor;
  final Color botColor;
  final Color lineColor;
  final Color ballColor;
  final Color smashColor;
  final Color shieldColor;

  static const double youX = 0.06;
  static const double botX = 0.94;

  /// The ball's height at a given x, 0..1.
  static double yAt(double x, double phase) =>
      0.5 + 0.30 * sin((x * 2.1 + phase) * pi);

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width;
    final h = size.height;

    // Goal zones, tinted.
    final zone = Paint()..style = PaintingStyle.fill;
    zone.color = youColor.withValues(alpha: 0.10);
    canvas.drawRect(Rect.fromLTWH(0, 0, w * 0.11, h), zone);
    zone.color = botColor.withValues(alpha: 0.10);
    canvas.drawRect(Rect.fromLTWH(w * 0.89, 0, w * 0.11, h), zone);

    // Goal flash behind the paddle that missed.
    if (frame.missed != null && frame.flash > 0) {
      final flash = Paint()
        ..color = (frame.missed == RallySide.you ? botColor : youColor)
            .withValues(alpha: 0.55 * frame.flash);
      final left = frame.missed == RallySide.you;
      canvas.drawRect(
          left ? Rect.fromLTWH(0, 0, w * 0.16, h) : Rect.fromLTWH(w * 0.84, 0, w * 0.16, h),
          flash);
    }

    // Centre line.
    final dash = Paint()
      ..color = lineColor
      ..strokeWidth = 1.5;
    for (var y = 6.0; y < h - 6; y += 14) {
      canvas.drawLine(Offset(w / 2, y), Offset(w / 2, y + 7), dash);
    }

    final ballY = yAt(frame.ballX.clamp(0.0, 1.0), frame.phase) * h;
    final ball = Offset(frame.ballX * w, ballY);

    // Paddles. The one the ball is heading to lines up with it as it nears;
    // the one that has just missed stays well away from it.
    double paddleY(RallySide side) {
      final isTarget = frame.towards == side;
      final x = side == RallySide.you ? youX : botX;
      if (frame.missed == side) {
        final aim = yAt(x, frame.phase);
        return (aim < 0.5 ? aim + 0.34 : aim - 0.34).clamp(0.15, 0.85) * h;
      }
      if (!isTarget) return h * 0.5;
      final dist = (frame.ballX - x).abs();
      final near = (1 - dist / 0.55).clamp(0.0, 1.0);
      return h * (0.5 + (ballY / h - 0.5) * near);
    }

    final padH = h * 0.30;
    void paddle(RallySide side, Color color, bool shield, bool charged) {
      final cx = (side == RallySide.you ? youX : botX) * w;
      final cy = paddleY(side);
      final r = RRect.fromRectAndRadius(
        Rect.fromCenter(center: Offset(cx, cy), width: 9, height: padH),
        const Radius.circular(4),
      );
      if (shield) {
        final ring = Paint()
          ..color = shieldColor.withValues(alpha: 0.9)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2.5;
        canvas.drawRRect(r.inflate(5), ring);
      }
      canvas.drawRRect(r, Paint()..color = charged ? smashColor : color);
    }

    paddle(RallySide.you, youColor, frame.youShield, frame.youCharged);
    paddle(RallySide.bot, botColor, frame.botShield, frame.botCharged);

    // Trail behind the ball, along the path it has just travelled.
    final dir = frame.towards == RallySide.bot ? 1.0 : -1.0;
    final color = frame.smash ? smashColor : ballColor;
    final steps = frame.smash ? 7 : 4;
    for (var i = steps; i >= 1; i--) {
      final tx = frame.ballX - dir * i * (frame.smash ? 0.028 : 0.018);
      if (tx < -0.05 || tx > 1.05) continue;
      final ty = yAt(tx.clamp(0.0, 1.0), frame.phase) * h;
      canvas.drawCircle(
        Offset(tx * w, ty),
        (frame.smash ? 8.0 : 6.5) * (1 - i / (steps + 2)),
        Paint()..color = color.withValues(alpha: 0.28 * (1 - i / (steps + 1))),
      );
    }
    if (frame.smash) {
      canvas.drawCircle(ball, 13, Paint()..color = smashColor.withValues(alpha: 0.22));
    }
    canvas.drawCircle(ball, frame.smash ? 8.5 : 7, Paint()..color = color);
  }

  @override
  bool shouldRepaint(RallyCourtPainter old) => true;
}

/// The court, framed, in the app's colours.
class RallyCourt extends StatelessWidget {
  const RallyCourt({super.key, required this.frame});

  final CourtFrame frame;

  @override
  Widget build(BuildContext context) {
    final c = context.lingo;
    return AspectRatio(
      aspectRatio: 2.5,
      child: Container(
        decoration: BoxDecoration(
          color: c.raised,
          border: Border.all(color: c.hairline),
          borderRadius: BorderRadius.circular(8),
        ),
        clipBehavior: Clip.antiAlias,
        child: CustomPaint(
          size: Size.infinite,
          painter: RallyCourtPainter(
            frame: frame,
            youColor: c.accent,
            botColor: kRallyBot,
            lineColor: c.hairline,
            ballColor: c.ink,
            smashColor: kRallySmash,
            shieldColor: c.success,
          ),
        ),
      ),
    );
  }
}

/// The opponent's colour and the smash colour. Fixed, so the same side is the
/// same colour in every theme.
const Color kRallyBot = Color(0xFF5BA4D6);
const Color kRallySmash = Color(0xFFE5533D);
