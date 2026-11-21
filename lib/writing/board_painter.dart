import 'dart:math' as math;
import 'dart:ui' as ui;

import 'package:flutter/material.dart';

/// One stroke to draw on the board, in 1000-grid coordinates.
class StrokeLayer {
  const StrokeLayer(this.points, this.color,
      {this.progress = 1, this.width = 44, this.opacity = 1});

  final List<Offset> points;
  final Color color;

  /// 0..1 of the stroke's length to draw (used for the animations).
  final double progress;
  final double width;
  final double opacity;
}

/// A small numbered badge at a stroke's start.
class NumberMark {
  const NumberMark(this.at, this.number, this.color);

  final Offset at;
  final int number;
  final Color color;
}

/// A smooth path through [pts]: quadratic curves through the midpoints, so a
/// finger trace of straight segments does not look jagged.
Path smoothPath(List<Offset> pts) {
  final path = Path();
  if (pts.isEmpty) return path;
  path.moveTo(pts.first.dx, pts.first.dy);
  if (pts.length == 1) {
    // A zero-length line still draws a dot with a round cap.
    path.lineTo(pts.first.dx + 0.01, pts.first.dy);
    return path;
  }
  if (pts.length == 2) {
    path.lineTo(pts[1].dx, pts[1].dy);
    return path;
  }
  for (var i = 1; i < pts.length - 1; i++) {
    final mid = Offset((pts[i].dx + pts[i + 1].dx) / 2,
        (pts[i].dy + pts[i + 1].dy) / 2);
    path.quadraticBezierTo(pts[i].dx, pts[i].dy, mid.dx, mid.dy);
  }
  path.lineTo(pts.last.dx, pts.last.dy);
  return path;
}

/// Draws the practice square: guide lines, then stroke layers, then the
/// stroke being drawn. Everything is in 1000-grid units and scaled to fit.
class BoardPainter extends CustomPainter {
  BoardPainter({
    required this.layers,
    required this.gridColor,
    required this.frameColor,
    this.marks = const [],
    this.live,
    this.liveColor = Colors.white,
    this.dot,
    this.dotColor = Colors.white,
  });

  final List<StrokeLayer> layers;
  final List<NumberMark> marks;
  final List<Offset>? live;
  final Color liveColor;
  final Color gridColor;
  final Color frameColor;

  /// A ring that marks where the next stroke starts.
  final Offset? dot;
  final Color dotColor;

  @override
  void paint(Canvas canvas, Size size) {
    final s = size.width / 1000;
    canvas.save();
    canvas.scale(s);

    _grid(canvas);

    for (final l in layers) {
      if (l.points.isEmpty || l.progress <= 0) continue;
      final paint = Paint()
        ..color = l.color.withValues(alpha: l.opacity)
        ..style = PaintingStyle.stroke
        ..strokeCap = StrokeCap.round
        ..strokeJoin = StrokeJoin.round
        ..strokeWidth = l.width;
      var path = smoothPath(l.points);
      if (l.progress < 1) {
        final metrics = path.computeMetrics().toList();
        if (metrics.isEmpty) continue;
        final m = metrics.first;
        path = m.extractPath(0, m.length * l.progress);
      }
      canvas.drawPath(path, paint);
    }

    final pts = live;
    if (pts != null && pts.isNotEmpty) {
      canvas.drawPath(
        smoothPath(pts),
        Paint()
          ..color = liveColor
          ..style = PaintingStyle.stroke
          ..strokeCap = StrokeCap.round
          ..strokeJoin = StrokeJoin.round
          ..strokeWidth = 40,
      );
    }

    if (dot != null) {
      canvas.drawCircle(
          dot!, 34, Paint()..color = dotColor.withValues(alpha: 0.25));
      canvas.drawCircle(
        dot!,
        34,
        Paint()
          ..color = dotColor
          ..style = PaintingStyle.stroke
          ..strokeWidth = 7,
      );
    }

    for (final m in marks) {
      _badge(canvas, m);
    }
    canvas.restore();
  }

  void _grid(Canvas canvas) {
    final frame = Paint()
      ..color = frameColor
      ..style = PaintingStyle.stroke
      ..strokeWidth = 5;
    canvas.drawRRect(
      RRect.fromRectAndRadius(
          const Rect.fromLTWH(2.5, 2.5, 995, 995), const Radius.circular(28)),
      frame,
    );
    final p = Paint()
      ..color = gridColor
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke;
    _dashed(canvas, const Offset(500, 12), const Offset(500, 988), p);
    _dashed(canvas, const Offset(12, 500), const Offset(988, 500), p);
    _dashed(canvas, const Offset(12, 12), const Offset(988, 988), p);
    _dashed(canvas, const Offset(988, 12), const Offset(12, 988), p);
  }

  void _dashed(Canvas canvas, Offset a, Offset b, Paint paint) {
    const dash = 16.0, gap = 14.0;
    final total = (b - a).distance;
    final dir = (b - a) / total;
    var d = 0.0;
    while (d < total) {
      final e = math.min(d + dash, total);
      canvas.drawLine(a + dir * d, a + dir * e, paint);
      d += dash + gap;
    }
  }

  void _badge(Canvas canvas, NumberMark m) {
    // Nudge the badge up and left of the stroke start so it does not sit on
    // top of the ink.
    final c = m.at + const Offset(-26, -26);
    canvas.drawCircle(c, 24, Paint()..color = m.color);
    final tp = TextPainter(
      text: TextSpan(
        text: '${m.number}',
        style: const TextStyle(
            color: Colors.white, fontSize: 30, fontWeight: FontWeight.w800),
      ),
      textDirection: ui.TextDirection.ltr,
    )..layout();
    tp.paint(canvas, c - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(covariant BoardPainter old) => true;
}
