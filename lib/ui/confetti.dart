import 'dart:math' as math;

import 'package:flutter/material.dart';

/// A one-shot burst of confetti from the two lower corners. Put it in a
/// Stack above the content; call [ConfettiBurstState.fire] (through a
/// GlobalKey) to set it off, or let [autoPlay] start it when it appears.
class ConfettiBurst extends StatefulWidget {
  const ConfettiBurst({
    super.key,
    this.pieces = 110,
    this.duration = const Duration(milliseconds: 3000),
    this.autoPlay = false,
  });

  final int pieces;
  final Duration duration;
  final bool autoPlay;

  @override
  State<ConfettiBurst> createState() => ConfettiBurstState();
}

class _Piece {
  _Piece({
    required this.fromLeft,
    required this.angle,
    required this.speed,
    required this.w,
    required this.h,
    required this.spin,
    required this.phase,
    required this.color,
    required this.round,
  });

  final bool fromLeft;
  final double angle;
  final double speed;
  final double w;
  final double h;
  final double spin;
  final double phase;
  final Color color;
  final bool round;
}

class ConfettiBurstState extends State<ConfettiBurst>
    with SingleTickerProviderStateMixin {
  static const _colors = [
    Color(0xFF3B82F6),
    Color(0xFF22C55E),
    Color(0xFFF59E0B),
    Color(0xFFEF4444),
    Color(0xFFA855F7),
    Color(0xFF06B6D4),
    Color(0xFFF472B6),
    Color(0xFFFACC15),
  ];

  late final AnimationController _c =
      AnimationController(vsync: this, duration: widget.duration);
  List<_Piece> _pieces = const [];

  @override
  void initState() {
    super.initState();
    if (widget.autoPlay) {
      WidgetsBinding.instance.addPostFrameCallback((_) => fire());
    }
  }

  /// Start (or restart) the burst. Does nothing when the system asks for
  /// reduced motion.
  void fire() {
    if (!mounted) return;
    if (MediaQuery.of(context).disableAnimations) return;
    final rnd = math.Random();
    _pieces = List.generate(widget.pieces, (i) {
      final left = i.isEven;
      // Aim up and towards the middle, with some spread.
      final base = left ? -62.0 : -118.0;
      final deg = base + (rnd.nextDouble() - 0.5) * 50;
      return _Piece(
        fromLeft: left,
        angle: deg * math.pi / 180,
        speed: 520 + rnd.nextDouble() * 520,
        w: 6 + rnd.nextDouble() * 6,
        h: 8 + rnd.nextDouble() * 8,
        spin: (rnd.nextDouble() - 0.5) * 14,
        phase: rnd.nextDouble() * math.pi,
        color: _colors[i % _colors.length],
        round: rnd.nextDouble() < 0.3,
      );
    });
    _c.forward(from: 0);
    setState(() {});
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return IgnorePointer(
      child: RepaintBoundary(
        child: AnimatedBuilder(
          animation: _c,
          builder: (context, _) => CustomPaint(
            size: Size.infinite,
            painter: _ConfettiPainter(
              pieces: _pieces,
              seconds: _c.value * widget.duration.inMilliseconds / 1000,
              fade: _c.value < 0.75 ? 1.0 : (1 - (_c.value - 0.75) / 0.25),
              active: _c.isAnimating,
            ),
          ),
        ),
      ),
    );
  }
}

class _ConfettiPainter extends CustomPainter {
  _ConfettiPainter({
    required this.pieces,
    required this.seconds,
    required this.fade,
    required this.active,
  });

  final List<_Piece> pieces;
  final double seconds;
  final double fade;
  final bool active;

  static const double _gravity = 1100;

  @override
  void paint(Canvas canvas, Size size) {
    if (!active || pieces.isEmpty) return;
    final t = seconds;
    for (final p in pieces) {
      final x0 = size.width * (p.fromLeft ? 0.06 : 0.94);
      final y0 = size.height * 0.78;
      // Air drag slows the sideways drift a little.
      final drag = math.exp(-1.1 * t);
      final x = x0 + math.cos(p.angle) * p.speed * (1 - drag) / 1.1;
      final y = y0 + math.sin(p.angle) * p.speed * t + 0.5 * _gravity * t * t;
      if (y > size.height + 40) continue;

      final paint = Paint()..color = p.color.withValues(alpha: fade.clamp(0.0, 1.0));
      canvas.save();
      canvas.translate(x, y);
      canvas.rotate(p.phase + p.spin * t);
      if (p.round) {
        canvas.drawCircle(Offset.zero, p.w / 2, paint);
      } else {
        // Flutter-style tumble: the height squashes as the piece turns.
        final squash = (math.cos(p.phase + p.spin * t * 2)).abs() * 0.8 + 0.2;
        canvas.drawRect(
          Rect.fromCenter(center: Offset.zero, width: p.w, height: p.h * squash),
          paint,
        );
      }
      canvas.restore();
    }
  }

  @override
  bool shouldRepaint(_ConfettiPainter old) =>
      old.seconds != seconds || old.pieces != pieces || old.active != active;
}
