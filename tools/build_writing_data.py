#!/usr/bin/env python3
"""Build the stroke-order data used by the Writing practice feature.

Outputs (all on a 0..1000 square grid, y pointing DOWN, strokes in order):
  assets/writing/ja_strokes.json   kanji used by japanese_core + hiragana + katakana
  assets/writing/zh_strokes.json   hanzi used by chinese_core

Each file is  {"v":1,"src":"...","chars":{"人":[[x1,y1,x2,y2,...],[...]], ...}}
i.e. one centerline polyline per stroke, flattened [x,y,x,y,...].

Sources
  Japanese  KanjiVG  (c) Ulrich Apel, CC BY-SA 3.0  http://kanjivg.tagaini.net
            fetched from raw.githubusercontent.com/KanjiVG/kanjivg/master/kanji/<hex5>.svg
  Chinese   hanzi-writer-data 2.0.1 (npm), derived from Make Me a Hanzi,
            Arphic Public License.  Obtain with:  npm pack hanzi-writer-data@2.0.1
            and extract; pass the extracted "package" directory as --hwd.

Usage
  python3 -I tools/build_writing_data.py --cache DIR --hwd DIR/package
  python3 -I tools/build_writing_data.py --check        # validate existing output only

--cache is a directory where downloaded SVGs are kept (so reruns are offline).
Downloaded files are treated as untrusted: they are only ever read with regexes,
never handed to an XML parser (the KanjiVG DOCTYPE declares entities).
"""
import argparse
import json
import math
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "writing"
KVG_URL = "https://raw.githubusercontent.com/KanjiVG/kanjivg/master/kanji/{:05x}.svg"
DP_TOL = 3.0  # Douglas-Peucker tolerance on the 1000 grid


# ----------------------------------------------------------------- geometry
def is_cjk(ch):
    return "一" <= ch <= "鿿" or "㐀" <= ch <= "䶿"


def is_kana(ch):
    return "ぁ" <= ch <= "ゖ" or "ァ" <= ch <= "ヺ"


def dp(points, tol):
    """Douglas-Peucker on a list of (x, y)."""
    if len(points) < 3:
        return points
    keep = [False] * len(points)
    keep[0] = keep[-1] = True
    stack = [(0, len(points) - 1)]
    while stack:
        a, b = stack.pop()
        (ax, ay), (bx, by) = points[a], points[b]
        dx, dy = bx - ax, by - ay
        norm = math.hypot(dx, dy)
        best, idx = -1.0, -1
        for i in range(a + 1, b):
            px, py = points[i]
            if norm == 0:
                d = math.hypot(px - ax, py - ay)
            else:
                d = abs(dy * (px - ax) - dx * (py - ay)) / norm
            if d > best:
                best, idx = d, i
        if best > tol:
            keep[idx] = True
            stack.append((a, idx))
            stack.append((idx, b))
    return [p for p, k in zip(points, keep) if k]


def flatten_cubic(p0, p1, p2, p3, n=10):
    out = []
    for i in range(1, n + 1):
        t = i / n
        u = 1 - t
        out.append((
            u * u * u * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t * t * t * p3[0],
            u * u * u * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t * t * t * p3[1],
        ))
    return out


def flatten_quad(p0, p1, p2, n=8):
    out = []
    for i in range(1, n + 1):
        t = i / n
        u = 1 - t
        out.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return out


_TOK = re.compile(r"([MmLlHhVvCcSsQqTtZz])|(-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?)")


def parse_path(d):
    """SVG path data -> list of (x, y) points (one subpath; KanjiVG strokes are one)."""
    toks = [(m.group(1), m.group(2)) for m in _TOK.finditer(d)]
    i = 0
    cmd = None
    pts = []
    cur = (0.0, 0.0)
    start = cur
    last_c2 = None  # last cubic control (for S)
    last_q = None

    def nums(k):
        nonlocal i
        vals = []
        for _ in range(k):
            if i >= len(toks) or toks[i][1] is None:
                raise ValueError("bad path: " + d)
            vals.append(float(toks[i][1]))
            i += 1
        return vals

    while i < len(toks):
        if toks[i][0]:
            cmd = toks[i][0]
            i += 1
            if cmd in "Zz":
                cur = start
                continue
        elif cmd is None:
            raise ValueError("bad path: " + d)
        rel = cmd.islower()
        c = cmd.upper()
        ox, oy = cur if rel else (0.0, 0.0)
        if c == "M":
            x, y = nums(2)
            cur = (ox + x, oy + y)
            start = cur
            pts.append(cur)
            cmd = "l" if rel else "L"  # implicit lineto
            last_c2 = last_q = None
        elif c == "L":
            x, y = nums(2)
            cur = (ox + x, oy + y)
            pts.append(cur)
            last_c2 = last_q = None
        elif c == "H":
            (x,) = nums(1)
            cur = (ox + x if rel else x, cur[1])
            pts.append(cur)
            last_c2 = last_q = None
        elif c == "V":
            (y,) = nums(1)
            cur = (cur[0], oy + y if rel else y)
            pts.append(cur)
            last_c2 = last_q = None
        elif c == "C":
            x1, y1, x2, y2, x, y = nums(6)
            p1, p2, p3 = (ox + x1, oy + y1), (ox + x2, oy + y2), (ox + x, oy + y)
            pts += flatten_cubic(cur, p1, p2, p3)
            cur, last_c2, last_q = p3, p2, None
        elif c == "S":
            x2, y2, x, y = nums(4)
            p1 = (2 * cur[0] - last_c2[0], 2 * cur[1] - last_c2[1]) if last_c2 else cur
            p2, p3 = (ox + x2, oy + y2), (ox + x, oy + y)
            pts += flatten_cubic(cur, p1, p2, p3)
            cur, last_c2, last_q = p3, p2, None
        elif c == "Q":
            x1, y1, x, y = nums(4)
            p1, p2 = (ox + x1, oy + y1), (ox + x, oy + y)
            pts += flatten_quad(cur, p1, p2)
            cur, last_q, last_c2 = p2, p1, None
        elif c == "T":
            x, y = nums(2)
            p1 = (2 * cur[0] - last_q[0], 2 * cur[1] - last_q[1]) if last_q else cur
            p2 = (ox + x, oy + y)
            pts += flatten_quad(cur, p1, p2)
            cur, last_q, last_c2 = p2, p1, None
        else:
            raise ValueError("unsupported command " + cmd)
    return pts


def finish(points):
    """Simplify, round to ints, drop duplicate points, flatten."""
    pts = dp(points, DP_TOL)
    out = []
    for x, y in pts:
        x = max(0, min(1000, int(round(x))))
        y = max(0, min(1000, int(round(y))))
        if out and out[-2] == x and out[-1] == y:
            continue
        out += [x, y]
    if len(out) == 2:  # a dot: make it a tiny stroke so it can still be drawn
        out += [out[0], out[1]]
    return out


# ------------------------------------------------------------------ sources
_PATH_RE = re.compile(r'<path\b[^>]*?\bid="kvg:[0-9a-f]+-s(\d+)"[^>]*?\bd="([^"]+)"', re.S)


def kanjivg_strokes(svg_text):
    found = [(int(n), d) for n, d in _PATH_RE.findall(svg_text)]
    found.sort()
    scale = 1000.0 / 109.0
    strokes = []
    for _, d in found:
        pts = [(x * scale, y * scale) for x, y in parse_path(d)]
        strokes.append(finish(pts))
    return strokes


def hanzi_strokes(medians):
    strokes = []
    for m in medians:
        pts = [(x * 1000.0 / 1024.0, (900.0 - y) * 1000.0 / 1024.0) for x, y in m]
        strokes.append(finish(pts))
    return strokes


def fetch_kvg(ch, cache):
    f = cache / "{:05x}.svg".format(ord(ch))
    if f.exists():
        return f.read_text(encoding="utf-8") if f.stat().st_size else None
    url = KVG_URL.format(ord(ch))
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = r.read()
            f.write_bytes(data)
            return data.decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                f.write_bytes(b"")
                return None
        except Exception:
            pass
    return None


# ------------------------------------------------------------------- driver
def deck_chars(name, predicate):
    d = json.load(open(ROOT / "assets" / "decks" / name, encoding="utf-8"))
    seen = {}
    for card in sorted(d["cards"], key=lambda c: c["rank"]):
        for ch in card["lemma"]:
            if predicate(ch) and ch not in seen:
                seen[ch] = card["rank"]
    return list(seen)


def write(name, src, chars):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    with open(path, "w", encoding="utf-8") as f:
        f.write('{"v":1,"src":%s,"chars":{\n' % json.dumps(src, ensure_ascii=False))
        items = list(chars.items())
        for i, (ch, strokes) in enumerate(items):
            f.write(json.dumps(ch, ensure_ascii=False) + ":" +
                    json.dumps(strokes, separators=(",", ":")))
            f.write(",\n" if i < len(items) - 1 else "\n")
        f.write("}}\n")
    print("wrote %s  %d chars  %.0f KB" % (path.relative_to(ROOT), len(chars), path.stat().st_size / 1024))


def check():
    ok = True
    for name, deck, pred in [("ja_strokes.json", "japanese_core.json", is_cjk),
                             ("zh_strokes.json", "chinese_core.json", is_cjk)]:
        data = json.load(open(OUT / name, encoding="utf-8"))
        chars = data["chars"]
        bad = 0
        for ch, strokes in chars.items():
            if not strokes:
                bad += 1
                print("  empty:", ch)
            for s in strokes:
                if len(s) < 4 or len(s) % 2 or any(v < 0 or v > 1000 for v in s):
                    bad += 1
                    print("  bad stroke:", ch, s[:8])
                    break
        want = deck_chars(deck, pred)
        missing = [c for c in want if c not in chars]
        cov = 100.0 * (len(want) - len(missing)) / len(want)
        print("%s: %d chars, deck coverage %.1f%% (%d missing), %d bad"
              % (name, len(chars), cov, len(missing), bad))
        ok = ok and bad == 0
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cache", type=Path)
    ap.add_argument("--hwd", type=Path)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.check:
        sys.exit(0 if check() else 1)
    if not a.cache or not a.hwd:
        ap.error("--cache and --hwd are required unless --check")
    a.cache.mkdir(parents=True, exist_ok=True)

    # ---- Japanese
    ja = deck_chars("japanese_core.json", is_cjk)
    kana = [chr(c) for c in range(0x3041, 0x3097)] + [chr(c) for c in range(0x30A1, 0x30FB)]
    want = ja + kana
    with ThreadPoolExecutor(16) as ex:
        texts = list(ex.map(lambda c: fetch_kvg(c, a.cache), want))
    jd, miss = {}, []
    for ch, t in zip(want, texts):
        if not t:
            miss.append(ch)
            continue
        s = kanjivg_strokes(t)
        if s:
            jd[ch] = s
        else:
            miss.append(ch)
    # order: kana first (they are the beginner set), then kanji by deck rank
    jd = dict(sorted(jd.items(), key=lambda kv: (not is_kana(kv[0]), 0)))
    print("japanese: %d wanted, %d built, missing %d: %s" % (len(want), len(jd), len(miss), "".join(miss[:80])))
    write("ja_strokes.json", "KanjiVG (c) Ulrich Apel, CC BY-SA 3.0, kanjivg.tagaini.net", jd)

    # ---- Chinese
    zh = deck_chars("chinese_core.json", is_cjk)
    zd, miss = {}, []
    for ch in zh:
        f = a.hwd / (ch + ".json")
        if not f.exists():
            miss.append(ch)
            continue
        zd[ch] = hanzi_strokes(json.load(open(f, encoding="utf-8"))["medians"])
    print("chinese: %d wanted, %d built, missing %d: %s" % (len(zh), len(zd), len(miss), "".join(miss[:80])))
    write("zh_strokes.json",
          "hanzi-writer-data 2.0.1 (Make Me a Hanzi), Arphic Public License", zd)
    check()


if __name__ == "__main__":
    main()
