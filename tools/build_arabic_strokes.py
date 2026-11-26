#!/usr/bin/env python3
"""Builds assets/writing/ar_strokes.json and assets/writing/ar_readings.json.

The Arabic letters in their isolated form (the 28 letters plus taa marbuuta, alif
maqsuura, hamza and laam-alif) as centerline strokes on the 1000 x 1000 grid.

The geometry is traced, not drawn by hand: each glyph is rendered from DejaVu Sans
(free licence, see below), thinned to a one-pixel skeleton, and the skeleton is walked
into strokes. The body of the letter is one pen movement that starts at its right
end (Arabic is written right to left; loops and branches become further strokes in
the order a hand would take them) and the dots come last, right to left.

Needs: Pillow, numpy, scipy, scikit-image. DejaVu Sans is Bitstream Vera plus
public-domain additions; its licence allows this use.

Usage: python3 tools/build_arabic_strokes.py [--preview DIR]
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage
from skimage.morphology import skeletonize

ROOT = Path(__file__).resolve().parent.parent
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SIZE = 420  # render size in px; geometry is scaled to the grid afterwards

# ---------------------------------------------------------------- the letters
# letter: (name, name romanized, sound, spoken sound, joins both sides)
LETTERS = [
    ("ا", "ألف", "alif", "aa", "أَ", False),
    ("ب", "باء", "baa", "b", "بَ", True),
    ("ت", "تاء", "taa", "t", "تَ", True),
    ("ث", "ثاء", "thaa", "th", "ثَ", True),
    ("ج", "جيم", "jeem", "j", "جَ", True),
    ("ح", "حاء", "haa", "h (throat)", "حَ", True),
    ("خ", "خاء", "khaa", "kh", "خَ", True),
    ("د", "دال", "daal", "d", "دَ", False),
    ("ذ", "ذال", "dhaal", "dh", "ذَ", False),
    ("ر", "راء", "raa", "r (rolled)", "رَ", False),
    ("ز", "زاي", "zaay", "z", "زَ", False),
    ("س", "سين", "seen", "s", "سَ", True),
    ("ش", "شين", "sheen", "sh", "شَ", True),
    ("ص", "صاد", "saad", "s (heavy)", "صَ", True),
    ("ض", "ضاد", "daad", "d (heavy)", "ضَ", True),
    ("ط", "طاء", "taa (heavy)", "t (heavy)", "طَ", True),
    ("ظ", "ظاء", "dhaa (heavy)", "dh (heavy)", "ظَ", True),
    ("ع", "عين", "ayn", "a (throat)", "عَ", True),
    ("غ", "غين", "ghayn", "gh", "غَ", True),
    ("ف", "فاء", "faa", "f", "فَ", True),
    ("ق", "قاف", "qaaf", "q", "قَ", True),
    ("ك", "كاف", "kaaf", "k", "كَ", True),
    ("ل", "لام", "laam", "l", "لَ", True),
    ("م", "ميم", "meem", "m", "مَ", True),
    ("ن", "نون", "noon", "n", "نَ", True),
    ("ه", "هاء", "haa", "h", "هَ", True),
    ("و", "واو", "waaw", "w / oo", "وَ", False),
    ("ي", "ياء", "yaa", "y / ee", "يَ", True),
    ("ة", "تاء مربوطة", "taa marbuuta", "-a / -at", "تاء مربوطة", False),
    ("ى", "ألف مقصورة", "alif maqsuura", "aa", "آ", False),
    ("ء", "همزة", "hamza", "glottal stop", "أَ", False),
    ("لا", "لام ألف", "laam-alif", "laa", "لَا", False),
]
DETAIL = {
    "ا": "a long aa sound (or the carrier of a vowel)", "ث": "like th in think", "ح": "a breathy h from the throat",
    "خ": "like ch in Scottish loch", "ذ": "like th in this", "ر": "a tapped or rolled r",
    "ص": "a heavy, deep s", "ض": "a heavy, deep d", "ط": "a heavy, deep t", "ظ": "a heavy, deep dh",
    "ع": "a sound made deep in the throat", "غ": "like a gargled r", "ق": "a k made further back in the throat",
    "و": "w as a consonant, long oo as a vowel", "ي": "y as a consonant, long ee as a vowel",
    "ة": "written only at the end of a word: -a, or -at when joined to another word",
    "ى": "a long aa written like a yaa without dots, only at the end of a word",
    "ء": "a catch in the throat, as in uh-oh", "لا": "lam and alif always join into this shape",
}

# ---------------------------------------------------------------- geometry
def render(ch):
    font = ImageFont.truetype(FONT, SIZE)
    img = Image.new("L", (SIZE * 2, SIZE * 2), 0)
    ImageDraw.Draw(img).text((SIZE // 2, int(SIZE * 1.3)), ch, font=font, fill=255, anchor="ls")
    a = np.array(img) > 128
    ys, xs = np.where(a)
    if len(xs) == 0:
        return None
    return a[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


NB = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def neighbors(p, pix):
    return [(p[0] + dy, p[1] + dx) for dy, dx in NB if (p[0] + dy, p[1] + dx) in pix]


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = math.hypot(dx, dy)
    best, idx = -1, 0
    for i in range(1, len(pts) - 1):
        x, y = pts[i]
        d = (math.hypot(x - x1, y - y1) if norm == 0
             else abs(dy * x - dx * y + x2 * y1 - y2 * x1) / norm)
        if d > best:
            best, idx = d, i
    if best > eps:
        return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]


def trace(skel, min_spur=16):
    """Walk a skeleton (bool array) into strokes of (x, y) pixel points."""
    pix = {(int(y), int(x)) for y, x in zip(*np.where(skel))}
    if not pix:
        return []
    for _ in range(3):  # prune short spurs
        deg = {p: len(neighbors(p, pix)) for p in pix}
        for e in [p for p, d in deg.items() if d == 1]:
            path, cur, prev = [e], e, None
            while True:
                nxt = [n for n in neighbors(cur, pix) if n != prev and n not in path]
                if len(nxt) != 1:
                    break
                prev, cur = cur, nxt[0]
                if len(neighbors(cur, pix)) >= 3:
                    break
                path.append(cur)
            if len(path) < min_spur and len(neighbors(cur, pix)) >= 3:
                for q in path:
                    pix.discard(q)
    deg = {p: len(neighbors(p, pix)) for p in pix}
    nodes = {p for p, d in deg.items() if d != 2}
    # cluster adjacent junction pixels into one node
    rep = {}
    for p in nodes:
        if p in rep:
            continue
        stack, comp = [p], {p}
        while stack:
            c = stack.pop()
            for n in neighbors(c, nodes):
                if n not in comp:
                    comp.add(n)
                    stack.append(n)
        r = min(comp)
        for c in comp:
            rep[c] = r
    if not rep:  # a pure ring: open it at its right-most pixel
        start = max(pix, key=lambda p: (p[1], -p[0]))
        pix.discard(start)
        return trace_ring(start, pix)
    edges = []  # (node_a, node_b, [pixels a..b])
    seen = set()
    for p in nodes:
        for n in neighbors(p, pix):
            if rep.get(n) == rep[p] or (p, n) in seen:
                continue
            path, prev, cur = [p, n], p, n
            while cur not in rep:
                nxt = [q for q in neighbors(cur, pix) if q != prev and q not in path[-3:]]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                path.append(cur)
            seen.add((p, n))
            seen.add((path[-1], path[-2]))
            edges.append([rep[p], rep.get(cur, cur), path])
    used = [False] * len(edges)
    strokes = []

    def score(p):
        return p[1] * 1.0 - p[0] * 0.25

    def start_node(avail):
        ends = [rep[p] for p in nodes if deg[p] == 1]
        cand = [n for n in set(rep.values()) if any(
            (e[0] == n or e[1] == n) for i, e in enumerate(edges) if i in avail)]
        pool = [n for n in cand if n in ends] or cand
        return max(pool, key=score)

    while not all(used):
        avail = {i for i, u in enumerate(used) if not u}
        cur = start_node(avail)
        pts, direction = [], None
        while True:
            opts = []
            for i in avail:
                a, b, path = edges[i]
                if a == cur:
                    opts.append((i, path))
                elif b == cur:
                    opts.append((i, path[::-1]))
            if not opts:
                break

            def turn(o):
                if direction is None:
                    return 0
                p = o[1]
                q = p[min(len(p) - 1, 10)]
                v = (q[1] - p[0][1], q[0] - p[0][0])
                n1, n2 = math.hypot(*v) or 1, math.hypot(*direction) or 1
                return -(v[0] * direction[0] + v[1] * direction[1]) / (n1 * n2)

            i, path = min(opts, key=turn)
            used[i] = True
            avail.discard(i)
            pts += [(x, y) for y, x in path] if not pts else [(x, y) for y, x in path[1:]]
            k = max(0, len(path) - 11)
            direction = (path[-1][1] - path[k][1], path[-1][0] - path[k][0])
            e = edges[i]
            cur = e[1] if path == e[2] else e[0]
        strokes.append(pts)
    return strokes


def trace_ring(start, pix):
    pts, cur, prev = [(start[1], start[0])], start, None
    while True:
        nxt = [n for n in neighbors(cur, pix) if n != prev]
        if not nxt:
            break
        pix.discard(cur)
        prev, cur = cur, nxt[0]
        pts.append((cur[1], cur[0]))
    return [pts]


def path_len(st):
    return sum(math.hypot(a[0] - b[0], a[1] - b[1]) for a, b in zip(st, st[1:]))


def J(*parts):
    """Joins strokes end to start into one pen movement."""
    out = list(parts[0])
    for p in parts[1:]:
        out += list(p)[1:]
    return out


def rev(st):
    return list(reversed(st))


# The skeleton walk is right for most letters; these are the ones where a hand
# would take one continuous stroke, or start from the other end.
FIX = {
    "ج": lambda b: [J(b[1], rev(b[0]))],
    "ح": lambda b: [J(b[1], rev(b[0]))],
    "خ": lambda b: [J(b[1], rev(b[0]))],
    "س": lambda b: [J(b[0], rev(b[1]))],
    "ش": lambda b: [J(b[0], rev(b[1]))],
    "ص": lambda b: [J(b[0], rev(b[1]))],
    "ض": lambda b: [J(b[0], rev(b[1]))],
    "ط": lambda b: [J(b[0], rev(b[1]))],
    "ظ": lambda b: [J(b[0], rev(b[1]))],
    "ف": lambda b: [rev(b[0])] + b[1:],
    "ق": lambda b: [rev(b[0])] + b[1:],
    "م": lambda b: [rev(b[0])],
    "و": lambda b: [rev(b[0])],
}


def glyph_strokes(ch):
    """Strokes (lists of (x, y) on the 1000 grid) for one rendered glyph."""
    a = render(ch)
    if a is None:
        return None
    lab, n = ndimage.label(a, structure=np.ones((3, 3)))
    comps = []
    for i in range(1, n + 1):
        ys, xs = np.where(lab == i)
        comps.append((i, len(xs), xs.min(), xs.max(), ys.min(), ys.max()))
    big = max(c[1] for c in comps)
    body, dots = [], []
    for c in comps:
        i, area, x0, x1, y0, y1 = c
        if len(comps) > 1 and area < big * 0.3 and (x1 - x0) < 95 and (y1 - y0) < 95:
            dots.append(((x0 + x1) / 2, (y0 + y1) / 2))
        else:
            body.append(c)
    strokes = []
    for c in sorted(body, key=lambda c: -c[3]):  # right-most piece first
        i, _, x0, x1, y0, y1 = c
        sk = skeletonize(lab == i)
        spur = max(16, 0.11 * max(x1 - x0, y1 - y0))
        for s in trace(sk, min_spur=spur):
            strokes.append(rdp(s, 4.0))
    dots.sort(key=lambda p: -p[0])
    ys, xs = np.where(a)
    h, w = a.shape
    s = min(700 / max(w, 1), 700 / max(h, 1), 1.9)
    ox, oy = (1000 - w * s) / 2, (1000 - h * s) / 2

    def g(p):
        return (ox + p[0] * s, oy + p[1] * s)

    bodies = [[g(p) for p in st] for st in strokes if len(st) >= 2]
    if ch in FIX:
        bodies = FIX[ch](bodies)
    out = [b for i, b in enumerate(bodies) if i == 0 or path_len(b) > 60]
    for d in dots:
        x, y = g(d)
        out.append([(x, y), (x + 8, y + 6)])
    return out


def flat(strokes):
    return [[int(round(v)) for p in s for v in p] for s in strokes]


def main():
    preview = Path(sys.argv[sys.argv.index("--preview") + 1]) if "--preview" in sys.argv else None
    chars, readings = {}, {}
    isolated = []
    for base, name, rom, sound, say, joins in LETTERS:
        ch = base
        st = glyph_strokes(ch)
        if st is None:
            print("no glyph", base)
            continue
        chars[ch] = flat(st)
        isolated.append(ch)
        readings[ch] = {"r": [sound, "%s (%s)" % (name, rom)], "says": [say, name], "say": say,
                        "m": [DETAIL.get(ch, ""), "letter name: %s" % name][1 - bool(DETAIL.get(ch)):]}
    out = ROOT / "assets" / "writing"
    (out / "ar_strokes.json").write_text(json.dumps(
        {"v": 1, "src": "Traced from DejaVu Sans (Bitstream Vera licence) glyph skeletons; stroke order set "
                        "by Lingotopia", "chars": chars}, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    (out / "ar_readings.json").write_text(json.dumps(
        {"v": 1, "src": "Letter names and approximate English sounds", "chars": readings},
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("glyphs", len(chars), "isolated", len(isolated), "KB", (out / "ar_strokes.json").stat().st_size // 1024)

    if preview:
        preview.mkdir(parents=True, exist_ok=True)
        lst = list(chars)
        cell, cols = 230, 8
        rows = (len(lst) + cols - 1) // cols
        img = Image.new("RGB", (cols * cell, rows * cell), "white")
        d = ImageDraw.Draw(img)
        k = (cell - 4) / 1000
        for n, ch in enumerate(lst):
            ox, oy = (n % cols) * cell, (n // cols) * cell
            d.rectangle([ox + 2, oy + 2, ox + cell - 2, oy + cell - 2], outline="#ccc")
            gl = render(ch)  # the font glyph in light grey, for comparison
            h, w = gl.shape
            sc = min(700 / max(w, 1), 700 / max(h, 1), 1.9)
            gx, gy = (1000 - w * sc) / 2, (1000 - h * sc) / 2
            mask = Image.fromarray((gl * 255).astype("uint8")).resize(
                (max(1, int(w * sc * k)), max(1, int(h * sc * k))))
            img.paste(Image.new("RGB", mask.size, "#dddddd"), (int(ox + 2 + gx * k), int(oy + 2 + gy * k)), mask)
            for i, s in enumerate(chars[ch]):
                pts = [(ox + 2 + s[j] * k, oy + 2 + s[j + 1] * k) for j in range(0, len(s), 2)]
                col = ["#c0392b", "#2471a3", "#1e8449", "#b7950b", "#7d3c98"][i % 5]
                if len(pts) > 1:
                    d.line(pts, fill=col, width=3)
                d.ellipse([pts[0][0] - 5, pts[0][1] - 5, pts[0][0] + 5, pts[0][1] + 5], fill=col)
        img.save(preview / "ar.png")


if __name__ == "__main__":
    main()
