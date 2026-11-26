#!/usr/bin/env python3
"""Builds assets/writing/ko_strokes.json and assets/writing/ko_readings.json.

Hangul is composed, so the stroke data is composed too: each letter (jamo) is
authored once as centerline strokes in a 100 x 100 box, then placed into the
cell its position in the syllable block calls for (initial / vowel / final).
Stroke order in a syllable is initial, vowel, final, and the order inside each
letter follows the standard Hangul stroke-order diagrams (the open
MagisterAdamus/hangeul-stroke-order set, CC BY-SA 4.0, was used to check it).

The teaching order is: the 19 consonants, the 21 vowels, then every syllable
that occurs in the Korean deck, most common first.

Usage: python3 tools/build_hangul_strokes.py [--preview DIR]
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- jamo shapes
# Each shape is a list of strokes, each stroke a list of (x, y) in 0..100, y down.


def ellipse(cx, cy, rx, ry, n=22):
    """Hangul circles are drawn counter-clockwise from the top."""
    pts = []
    for i in range(n + 1):
        a = -math.pi / 2 - 2 * math.pi * 1.04 * i / n
        pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    return pts


C = {}  # consonants
C["ㄱ"] = [[(10, 10), (90, 10), (90, 90)]]
C["ㄴ"] = [[(10, 10), (10, 90), (90, 90)]]
C["ㄷ"] = [[(10, 10), (90, 10)], [(10, 12), (10, 90), (90, 90)]]
C["ㄹ"] = [[(10, 8), (90, 8), (90, 40)], [(10, 40), (90, 40)], [(10, 40), (10, 92), (90, 92)]]
C["ㅁ"] = [[(12, 10), (12, 90)], [(12, 10), (88, 10), (88, 90)], [(12, 90), (88, 90)]]
C["ㅂ"] = [[(15, 8), (15, 92)], [(85, 8), (85, 92)], [(15, 42), (85, 42)], [(15, 92), (85, 92)]]
C["ㅅ"] = [[(50, 8), (42, 45), (25, 74), (8, 92)], [(40, 45), (65, 72), (92, 92)]]
C["ㅇ"] = [ellipse(50, 50, 40, 40)]
C["ㅈ"] = [[(8, 14), (92, 14)], [(50, 14), (41, 50), (25, 76), (6, 94)], [(40, 52), (64, 74), (94, 94)]]
C["ㅊ"] = [[(36, 4), (64, 4)], [(8, 26), (92, 26)], [(50, 26), (41, 58), (25, 80), (6, 95)],
           [(40, 60), (64, 78), (94, 95)]]
C["ㅋ"] = [[(10, 10), (90, 10), (90, 90)], [(12, 50), (90, 50)]]
C["ㅌ"] = [[(10, 10), (90, 10)], [(12, 50), (90, 50)], [(10, 10), (10, 90), (90, 90)]]
C["ㅍ"] = [[(8, 10), (92, 10)], [(30, 12), (36, 90)], [(72, 12), (66, 90)], [(8, 90), (92, 90)]]
C["ㅎ"] = [[(36, 5), (64, 5)], [(10, 30), (90, 30)], ellipse(50, 74, 26, 20)]

V = {}  # vowels
V["ㅏ"] = [[(30, 5), (30, 95)], [(30, 50), (82, 50)]]
V["ㅑ"] = [[(30, 5), (30, 95)], [(30, 33), (82, 33)], [(30, 67), (82, 67)]]
V["ㅓ"] = [[(18, 50), (70, 50)], [(70, 5), (70, 95)]]
V["ㅕ"] = [[(18, 33), (70, 33)], [(18, 67), (70, 67)], [(70, 5), (70, 95)]]
V["ㅗ"] = [[(50, 8), (50, 62)], [(5, 62), (95, 62)]]
V["ㅛ"] = [[(30, 10), (30, 62)], [(70, 10), (70, 62)], [(5, 62), (95, 62)]]
V["ㅜ"] = [[(5, 30), (95, 30)], [(50, 30), (50, 92)]]
V["ㅠ"] = [[(5, 30), (95, 30)], [(30, 30), (30, 92)], [(70, 30), (70, 92)]]
V["ㅡ"] = [[(5, 50), (95, 50)]]
V["ㅣ"] = [[(50, 5), (50, 95)]]
V["ㅐ"] = [[(26, 5), (26, 95)], [(26, 50), (72, 50)], [(72, 5), (72, 95)]]
V["ㅒ"] = [[(26, 5), (26, 95)], [(26, 33), (72, 33)], [(26, 67), (72, 67)], [(72, 5), (72, 95)]]
V["ㅔ"] = [[(8, 50), (46, 50)], [(46, 5), (46, 95)], [(86, 5), (86, 95)]]
V["ㅖ"] = [[(8, 33), (46, 33)], [(8, 67), (46, 67)], [(46, 5), (46, 95)], [(86, 5), (86, 95)]]
# compound vowels: the left part sits in the lower half, so a consonant fits above it
V["ㅚ"] = [[(32, 46), (32, 72)], [(5, 72), (72, 72)], [(72, 5), (72, 95)]]
V["ㅘ"] = [[(30, 46), (30, 72)], [(5, 72), (70, 72)], [(70, 5), (70, 95)], [(70, 50), (95, 50)]]
V["ㅙ"] = [[(20, 46), (20, 72)], [(3, 72), (52, 72)], [(52, 5), (52, 95)], [(52, 50), (74, 50)],
           [(74, 5), (74, 95)]]
V["ㅟ"] = [[(5, 46), (72, 46)], [(30, 46), (30, 90)], [(72, 5), (72, 95)]]
V["ㅝ"] = [[(5, 46), (72, 46)], [(30, 46), (30, 90)], [(48, 70), (72, 70)], [(72, 5), (72, 95)]]
V["ㅞ"] = [[(3, 46), (52, 46)], [(22, 46), (22, 90)], [(38, 70), (52, 70)], [(52, 5), (52, 95)],
           [(76, 5), (76, 95)]]
V["ㅢ"] = [[(5, 72), (70, 72)], [(70, 5), (70, 95)]]

CHO = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
JUNG = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ",
        "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]
# a doubled or clustered letter is its parts side by side
PARTS = {
    "ㄲ": "ㄱㄱ", "ㄸ": "ㄷㄷ", "ㅃ": "ㅂㅂ", "ㅆ": "ㅅㅅ", "ㅉ": "ㅈㅈ",
    "ㄳ": "ㄱㅅ", "ㄵ": "ㄴㅈ", "ㄶ": "ㄴㅎ", "ㄺ": "ㄹㄱ", "ㄻ": "ㄹㅁ", "ㄼ": "ㄹㅂ",
    "ㄽ": "ㄹㅅ", "ㄾ": "ㄹㅌ", "ㄿ": "ㄹㅍ", "ㅀ": "ㄹㅎ", "ㅄ": "ㅂㅅ",
}

VERTICAL = set("ㅏㅑㅓㅕㅣ")
VERTICAL_WIDE = set("ㅐㅒㅔㅖ")
HORIZONTAL = set("ㅗㅛㅜㅠㅡ")
COMPOUND = set("ㅘㅙㅚㅝㅞㅟㅢ")


def place(strokes, box):
    x0, y0, x1, y1 = box
    return [[(x0 + (x / 100.0) * (x1 - x0), y0 + (y / 100.0) * (y1 - y0)) for x, y in s] for s in strokes]


def consonant(ch, box):
    """Strokes of [ch] (single, doubled or clustered) filling [box]."""
    parts = PARTS.get(ch, ch)
    x0, y0, x1, y1 = box
    n = len(parts)
    gap = 30 if n > 1 else 0
    w = (x1 - x0 - gap * (n - 1)) / n
    out = []
    for i, p in enumerate(parts):
        bx = x0 + i * (w + gap)
        out += place(C[p], fit(p, (bx, y0, bx + w, y1)))
    return out


def fit(p, box):
    """Keeps a letter from being stretched out of shape in a tall or wide
    cell: the circle and the square stay roundish, the rest may be taller."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    hi = 1.1 if p in "ㅇㅁ" else 1.6
    lo = 0.7
    if h > hi * w:
        nh = hi * w
        y0 += (h - nh) / 2
        y1 = y0 + nh
    elif h < lo * w:
        nw = h / lo
        x0 += (w - nw) / 2
        x1 = x0 + nw
    return (x0, y0, x1, y1)


def syllable(ch):
    i = ord(ch) - 0xAC00
    L, M, T = CHO[i // 588], JUNG[(i % 588) // 28], JONG[i % 28]
    has_t = T != ""
    out = []
    if M in VERTICAL or M in VERTICAL_WIDE:
        split = 400 if M in VERTICAL_WIDE else 470
        bot = 540 if has_t else 940
        out += consonant(L, (60, 60, split, bot))
        out += place(V[M], (split + 20, 60, 940, bot))
    elif M in HORIZONTAL:
        if has_t:
            out += consonant(L, (220, 60, 780, 330))
            out += place(V[M], (60, 360, 940, 640))
        else:
            out += consonant(L, (200, 60, 800, 500))
            out += place(V[M], (60, 540, 940, 940))
    else:  # compound
        bot = 640 if has_t else 940
        h = bot - 60
        out += consonant(L, (60, 60, 560, 60 + 0.38 * h))
        out += place(V[M], (60, 60, 940, bot))
    if has_t:
        out += consonant(T, (140, 690, 860, 940))
    return out


def standalone(ch):
    if ch in C or ch in PARTS:
        parts = PARTS.get(ch, ch)
        if len(parts) > 1:
            return consonant(ch, (60, 180, 940, 820))
        return place(C[ch], (110, 110, 890, 890))
    return place(V[ch], (110, 110, 890, 890))


def flat(strokes):
    return [[int(round(v)) for p in s for v in p] for s in strokes]


# ------------------------------------------------------------------ readings
SOUND = {
    "ㄱ": ("g / k", "기역", "giyeok"), "ㄴ": ("n", "니은", "nieun"), "ㄷ": ("d / t", "디귿", "digeut"),
    "ㄹ": ("r / l", "리을", "rieul"), "ㅁ": ("m", "미음", "mieum"), "ㅂ": ("b / p", "비읍", "bieup"),
    "ㅅ": ("s", "시옷", "siot"), "ㅇ": ("silent / ng", "이응", "ieung"), "ㅈ": ("j", "지읒", "jieut"),
    "ㅊ": ("ch", "치읓", "chieut"), "ㅋ": ("k", "키읔", "kieuk"), "ㅌ": ("t", "티읕", "tieut"),
    "ㅍ": ("p", "피읖", "pieup"), "ㅎ": ("h", "히읗", "hieut"),
    "ㄲ": ("kk", "쌍기역", "ssanggiyeok"), "ㄸ": ("tt", "쌍디귿", "ssangdigeut"),
    "ㅃ": ("pp", "쌍비읍", "ssangbieup"), "ㅆ": ("ss", "쌍시옷", "ssangsiot"),
    "ㅉ": ("jj", "쌍지읒", "ssangjieut"),
}
ROM_V = dict(zip(JUNG, "a ae ya yae eo e yeo ye o wa wae oe yo u wo we wi yu eu ui i".split()))
ROM_L = dict(zip(CHO, "g kk n d tt r m b pp s ss  j jj ch k t p h".split(" ")))
ROM_L["ㅇ"] = ""
FINAL_SOUND = {}
for t in "ㄱㄲㅋㄳㄺ":
    FINAL_SOUND[t] = "k"
for t in "ㄴㄵㄶ":
    FINAL_SOUND[t] = "n"
for t in "ㄷㅅㅆㅈㅊㅌㅎ":
    FINAL_SOUND[t] = "t"
for t in "ㄹㄼㄽㄾㅀ":
    FINAL_SOUND[t] = "l"
for t in "ㅁㄻ":
    FINAL_SOUND[t] = "m"
for t in "ㅂㅍㅄㄿ":
    FINAL_SOUND[t] = "p"
FINAL_SOUND["ㅇ"] = "ng"
VOWEL_SAY = {v: chr(0xAC00 + (11 * 21 + JUNG.index(v)) * 28) for v in JUNG}  # ㅇ + vowel


def romanize(ch):
    i = ord(ch) - 0xAC00
    L, M, T = CHO[i // 588], JUNG[(i % 588) // 28], JONG[i % 28]
    return ROM_L[L] + ROM_V[M] + FINAL_SOUND.get(T, "")


def main():
    preview = None
    if "--preview" in sys.argv:
        preview = Path(sys.argv[sys.argv.index("--preview") + 1])

    deck = json.load(open(ROOT / "assets" / "decks" / "korean_core.json"))
    seen = []
    have = set()
    for card in deck["cards"]:
        for ch in card["lemma"]:
            if "가" <= ch <= "힣" and ch not in have:
                have.add(ch)
                seen.append(ch)

    letters = [c for c in CHO] + [v for v in JUNG]
    chars = {}
    readings = {}
    for j in letters:
        chars[j] = flat(standalone(j))
        if j in SOUND:
            snd, name, rom = SOUND[j]
            readings[j] = {"r": [snd], "say": name, "m": ["letter name: %s (%s)" % (name, rom)]}
        else:
            readings[j] = {"r": [ROM_V[j]], "say": VOWEL_SAY[j], "m": ["vowel"]}
    for s in seen:
        chars[s] = flat(syllable(s))
        readings[s] = {"r": [romanize(s)]}

    src = ("Authored for Lingotopia: Hangul letter centerlines composed into syllable blocks; stroke "
           "order checked against the open Hangul stroke-order diagrams "
           "(MagisterAdamus/hangeul-stroke-order, CC BY-SA 4.0)")
    out = ROOT / "assets" / "writing"
    (out / "ko_strokes.json").write_text(
        json.dumps({"v": 1, "src": src, "chars": chars}, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8")
    (out / "ko_readings.json").write_text(
        json.dumps({"v": 1, "src": "Revised Romanization of Korean (isolated syllable); letter names",
                    "chars": readings}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("letters %d, syllables %d, strokes file %d KB, readings file %d KB" % (
        len(letters), len(seen), (out / "ko_strokes.json").stat().st_size // 1024,
        (out / "ko_readings.json").stat().st_size // 1024))

    if preview:
        from PIL import Image, ImageDraw, ImageFont
        preview.mkdir(parents=True, exist_ok=True)
        font = None
        for fp in ("/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
                   "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"):
            try:
                font = ImageFont.truetype(fp, 14)
                break
            except OSError:
                pass
        sets = {"letters": letters, "syl": seen[:96], "tricky": [
            s for s in seen if JONG[(ord(s) - 0xAC00) % 28] in "ㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄㄲㅆ"][:24]
            + [s for s in seen if CHO[(ord(s) - 0xAC00) // 588] in "ㄲㄸㅃㅆㅉ"][:24]}
        for name, lst in sets.items():
            cell, cols = 130, 12
            rows = (len(lst) + cols - 1) // cols
            img = Image.new("RGB", (cols * cell, rows * cell), "white")
            d = ImageDraw.Draw(img)
            for n, ch in enumerate(lst):
                ox, oy = (n % cols) * cell, (n // cols) * cell
                d.rectangle([ox + 4, oy + 4, ox + cell - 4, oy + cell - 4], outline="#ccc")
                for k, s in enumerate(chars[ch]):
                    pts = [(ox + 4 + s[i] * (cell - 8) / 1000, oy + 4 + s[i + 1] * (cell - 8) / 1000)
                           for i in range(0, len(s), 2)]
                    col = ["#c0392b", "#2471a3", "#1e8449", "#b7950b", "#7d3c98", "#117a65"][k % 6]
                    d.line(pts, fill=col, width=3)
                if font:
                    d.text((ox + 6, oy + 6), ch, fill="black", font=font)
            img.save(preview / (name + ".png"))


if __name__ == "__main__":
    main()
