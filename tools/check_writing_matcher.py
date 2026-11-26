#!/usr/bin/env python3
"""Python mirror of lib/writing/stroke_matcher.dart, run over the real stroke
data. Dart is not available where this was written, so this is how the
thresholds were tuned. Keep it in step with the Dart file.

  python3 -I tools/check_writing_matcher.py
"""
import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAMPLES = 24
END_TOL = 210.0
AVG_TOL = 125.0
MIN_RATIO, MAX_RATIO = 0.35, 2.6
DOT = 90.0


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def length(p):
    return sum(dist(p[i - 1], p[i]) for i in range(1, len(p)))


def resample(p, n=SAMPLES):
    if not p:
        return []
    if len(p) == 1 or length(p) == 0:
        return [p[0]] * n
    step = length(p) / (n - 1)
    out = [p[0]]
    acc, prev, i, need = 0.0, p[0], 1, step
    while i < len(p) and len(out) < n - 1:
        seg = dist(p[i], prev)
        if seg == 0:
            prev = p[i]
            i += 1
            continue
        if acc + seg >= need:
            t = (need - acc) / seg
            q = (prev[0] + (p[i][0] - prev[0]) * t, prev[1] + (p[i][1] - prev[1]) * t)
            out.append(q)
            prev, acc, need = q, 0.0, step
        else:
            acc += seg
            prev = p[i]
            i += 1
    while len(out) < n:
        out.append(p[-1])
    out[n - 1] = p[-1]
    return out


def centroid(p):
    return (sum(x for x, _ in p) / len(p), sum(y for _, y in p) / len(p))


def issue_for(user, target, leniency=1.0):
    ul, tl = length(user), length(target)
    if tl < DOT:
        if dist(centroid(user), centroid(target)) > 230 * leniency:
            return "off"
        if ul > max(260, tl * 4):
            return "long"
        return None
    if ul < tl * MIN_RATIO / leniency:
        return "short"
    if ul > tl * MAX_RATIO * leniency:
        return "long"
    u, t = resample(user), resample(target)
    tol = END_TOL * leniency
    s, e = dist(u[0], t[0]), dist(u[-1], t[-1])
    if s > tol or e > tol:
        if dist(u[0], t[-1]) <= tol and dist(u[-1], t[0]) <= tol:
            return "reverse"
        return "off"
    if sum(dist(a, b) for a, b in zip(u, t)) / SAMPLES > AVG_TOL * leniency:
        return "off"
    uv = (u[-1][0] - u[0][0], u[-1][1] - u[0][1])
    tv = (t[-1][0] - t[0][0], t[-1][1] - t[0][1])
    if math.hypot(*uv) > 60 and math.hypot(*tv) > 60:
        cos = (uv[0] * tv[0] + uv[1] * tv[1]) / (math.hypot(*uv) * math.hypot(*tv))
        if cos < 0.4:
            return "reverse"
    return None


def pairs(flat):
    return [(flat[i], flat[i + 1]) for i in range(0, len(flat), 2)]


def finger(stroke, rnd, wobble=28.0, shift=45.0):
    """A plausible finger drawing of a stroke: dense points, a smooth wobble
    (a hand drifts, it does not jitter), a shift, and a little digitiser noise."""
    n = max(12, int(length(stroke) / 8))
    base = resample(stroke, n)
    dx, dy = rnd.uniform(-shift, shift), rnd.uniform(-shift, shift)
    f1, f2 = rnd.uniform(0.5, 2.0), rnd.uniform(0.5, 2.0)
    p1, p2 = rnd.uniform(0, 6.28), rnd.uniform(0, 6.28)
    out = []
    for i, (x, y) in enumerate(base):
        t = i / (n - 1)
        out.append((x + dx + wobble * math.sin(6.28 * f1 * t + p1) + rnd.gauss(0, 1.5),
                    y + dy + wobble * math.sin(6.28 * f2 * t + p2) + rnd.gauss(0, 1.5)))
    return out


def main():
    rnd = random.Random(7)
    for lang in ("ja", "zh", "ko", "ru", "ar"):
        data = json.load(open(ROOT / "assets" / "writing" / ("%s_strokes.json" % lang)))["chars"]
        chars = list(data.items())
        rnd.shuffle(chars)
        chars = chars[:600]
        n_ok = n = rev_ok = rev_n = near_ok = near_n = 0
        for ch, strokes in chars:
            st = [pairs(s) for s in strokes]
            for i, target in enumerate(st):
                n += 1
                if issue_for(finger(target, rnd), target) is None:
                    n_ok += 1
                # drawn backwards must not be accepted (skip dots / near-symmetric)
                if length(target) > 200 and dist(target[0], target[-1]) > 150:
                    rev_n += 1
                    if issue_for(list(reversed(finger(target, rnd, 10, 10))), target) is not None:
                        rev_ok += 1
                # a different stroke of the same character must not be accepted
                for j, other in enumerate(st):
                    if j != i and length(other) > 120 and length(target) > 120:
                        near_n += 1
                        if issue_for(finger(other, rnd, 10, 10), target) is not None:
                            near_ok += 1
        print("%s  %d chars | good strokes accepted %.1f%% | reversed rejected %.1f%% | other strokes rejected %.1f%%"
              % (lang, len(chars), 100 * n_ok / n, 100 * rev_ok / max(rev_n, 1), 100 * near_ok / max(near_n, 1)))


if __name__ == "__main__":
    main()
