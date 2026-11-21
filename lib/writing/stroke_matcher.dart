import 'dart:math' as math;
import 'dart:ui' show Offset;

/// Why a drawn stroke was not accepted.
enum MatchIssue { tooShort, tooLong, wrongDirection, wrongOrder, offTarget }

class StrokeMatch {
  const StrokeMatch.ok() : issue = null;
  const StrokeMatch.fail(MatchIssue this.issue);

  final MatchIssue? issue;
  bool get ok => issue == null;
}

/// All coordinates are on the 1000 x 1000 character grid.
///
/// The test is deliberately forgiving: a finger is not a brush. A stroke is
/// accepted when it starts and ends near the model stroke's ends, stays near
/// its path on average, runs the same way and is roughly the same length.
class StrokeMatcher {
  const StrokeMatcher._();

  static const int samples = 24;

  /// Largest allowed distance of the start and of the end, grid units.
  static const double endpointTolerance = 210;

  /// Largest allowed average distance between corresponding points.
  static const double averageTolerance = 125;

  /// Shortest and longest accepted length, relative to the model stroke.
  static const double minLengthRatio = 0.35;
  static const double maxLengthRatio = 2.6;

  /// Model strokes shorter than this are treated as dots or ticks.
  static const double dotLength = 90;

  static double pathLength(List<Offset> p) {
    var len = 0.0;
    for (var i = 1; i < p.length; i++) {
      len += (p[i] - p[i - 1]).distance;
    }
    return len;
  }

  /// [n] points spaced evenly along the path (first and last included).
  static List<Offset> resample(List<Offset> p, [int n = samples]) {
    if (p.isEmpty) return const [];
    if (p.length == 1) return List.filled(n, p.first);
    final total = pathLength(p);
    if (total == 0) return List.filled(n, p.first);
    final step = total / (n - 1);
    final out = <Offset>[p.first];
    var acc = 0.0;
    var prev = p.first;
    var i = 1;
    var need = step;
    while (i < p.length && out.length < n - 1) {
      final seg = (p[i] - prev).distance;
      if (seg == 0) {
        prev = p[i];
        i++;
        continue;
      }
      if (acc + seg >= need) {
        final t = (need - acc) / seg;
        final q = Offset.lerp(prev, p[i], t)!;
        out.add(q);
        prev = q;
        acc = 0;
        need = step;
      } else {
        acc += seg;
        prev = p[i];
        i++;
      }
    }
    while (out.length < n) {
      out.add(p.last);
    }
    out[n - 1] = p.last;
    return out;
  }

  static Offset _centroid(List<Offset> p) {
    var x = 0.0, y = 0.0;
    for (final o in p) {
      x += o.dx;
      y += o.dy;
    }
    return Offset(x / p.length, y / p.length);
  }

  /// Whether [user] is an acceptable drawing of [target] (ignoring order).
  static MatchIssue? _issueFor(List<Offset> user, List<Offset> target,
      double leniency) {
    final userLen = pathLength(user);
    final targetLen = pathLength(target);

    if (targetLen < dotLength) {
      // A dot or a short tick: where it is matters, how it runs does not.
      final d = (_centroid(user) - _centroid(target)).distance;
      if (d > 230 * leniency) return MatchIssue.offTarget;
      if (userLen > math.max(260, targetLen * 4)) return MatchIssue.tooLong;
      return null;
    }

    if (userLen < targetLen * minLengthRatio / leniency) {
      return MatchIssue.tooShort;
    }
    if (userLen > targetLen * maxLengthRatio * leniency) {
      return MatchIssue.tooLong;
    }

    final u = resample(user);
    final t = resample(target);
    final start = (u.first - t.first).distance;
    final end = (u.last - t.last).distance;
    final tol = endpointTolerance * leniency;

    if (start > tol || end > tol) {
      final rs = (u.first - t.last).distance;
      final re = (u.last - t.first).distance;
      if (rs <= tol && re <= tol) return MatchIssue.wrongDirection;
      return MatchIssue.offTarget;
    }

    var sum = 0.0;
    for (var i = 0; i < samples; i++) {
      sum += (u[i] - t[i]).distance;
    }
    if (sum / samples > averageTolerance * leniency) return MatchIssue.offTarget;

    // A hook or a bend can fool the end-point test; the overall heading
    // still has to agree when the stroke has a real chord.
    final uv = u.last - u.first;
    final tv = t.last - t.first;
    if (uv.distance > 60 && tv.distance > 60) {
      final cos = (uv.dx * tv.dx + uv.dy * tv.dy) / (uv.distance * tv.distance);
      if (cos < 0.4) return MatchIssue.wrongDirection;
    }
    return null;
  }

  /// Checks [user] against the stroke that is due ([target]).
  ///
  /// [later] are the strokes still to come; a drawing that fits one of those
  /// but not the due stroke is reported as being in the wrong order.
  /// [leniency] above 1 forgives more (used after repeated misses).
  static StrokeMatch match({
    required List<Offset> user,
    required List<Offset> target,
    List<List<Offset>> later = const [],
    double leniency = 1.0,
  }) {
    if (user.isEmpty || target.isEmpty) {
      return const StrokeMatch.fail(MatchIssue.tooShort);
    }
    final issue = _issueFor(user, target, leniency);
    if (issue == null) return const StrokeMatch.ok();
    for (final other in later) {
      if (_issueFor(user, other, 1.0) == null) {
        return const StrokeMatch.fail(MatchIssue.wrongOrder);
      }
    }
    return StrokeMatch.fail(issue);
  }

  /// 3 stars for a clean run, 2 for a few slips, 1 for finishing with help.
  static int starsFor({required int misses, required int hints}) {
    if (misses == 0 && hints == 0) return 3;
    if (misses <= 3 && hints <= 1) return 2;
    return 1;
  }
}
