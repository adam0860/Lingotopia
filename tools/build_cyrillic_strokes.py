#!/usr/bin/env python3
"""Builds assets/writing/ru_strokes.json and assets/writing/ru_readings.json.

The 33 Russian letters, capital and small, authored as centerline strokes on the
1000 x 1000 grid (y down) in printed form, with the usual stroke order: stems
first, top to bottom, then bars and bowls, left to right. Most small letters are
the capital scaled down to the x-height (as in print); a, b, e, yo, r, u and f
have their own shapes.

Baseline y = 760, cap height y = 150, x-height y = 330, descender y = 960.

Usage: python3 tools/build_cyrillic_strokes.py [--preview DIR]
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

T, B = 150, 760  # cap top and baseline
XH = 330  # x-height


def arc(cx, cy, rx, ry, a0, a1):
    """Counter-clockwise visual angles in degrees (0 = right, 90 = top)."""
    n = max(6, int(abs(a1 - a0) / 10))
    return [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy - ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


def oval(cx, cy, rx, ry):
    return arc(cx, cy, rx, ry, 90, 450)


def bowl(xl, yt, yb, xc, rx):
    """A bowl open to the left: top edge, a half-round on the right, bottom edge."""
    cy = (yt + yb) / 2
    return [(xl, yt)] + arc(xc, cy, rx, (yb - yt) / 2, 90, -90) + [(xl, yb)]


def dots(*pts):
    return [[(x, y), (x + 8, y + 6)] for x, y in pts]


CAP = {}
CAP["А"] = [[(500, T), (250, B)], [(500, T), (750, B)], [(340, 560), (660, 560)]]
CAP["Б"] = [[(300, T), (300, B)], [(300, T), (700, T)], bowl(300, 440, B, 520, 175)]
CAP["В"] = [[(290, T), (290, B)], bowl(290, T, 450, 480, 165), bowl(290, 450, B, 500, 185)]
CAP["Г"] = [[(310, T), (310, B)], [(310, T), (680, T)]]
CAP["Д"] = [[(330, T), (710, T)], [(440, T), (350, 700)], [(650, T), (690, 700)],
            [(240, 830), (240, 700), (780, 700), (780, 830)]]
CAP["Е"] = [[(300, T), (300, B)], [(300, T), (700, T)], [(300, 455), (640, 455)], [(300, B), (700, B)]]
CAP["Ё"] = CAP["Е"] + dots((400, 70), (600, 70))
CAP["Ж"] = [[(500, T), (500, B)], [(210, T), (500, 455), (210, B)], [(790, T), (500, 455), (790, B)]]
CAP["З"] = [arc(480, 300, 170, 150, 155, -90) + arc(480, 605, 195, 155, 90, -155)[1:]]
CAP["И"] = [[(290, T), (290, B)], [(710, T), (710, B)], [(710, T), (290, B)]]
CAP["Й"] = CAP["И"] + [arc(500, 70, 105, 45, 200, 340)]
CAP["К"] = [[(300, T), (300, B)], [(700, T), (300, 500)], [(450, 385), (720, B)]]
CAP["Л"] = [[(430, T), (250, B)], [(430, T), (720, T), (720, B)]]
CAP["М"] = [[(240, T), (240, B)], [(240, T), (500, 560), (760, T)], [(760, T), (760, B)]]
CAP["Н"] = [[(300, T), (300, B)], [(700, T), (700, B)], [(300, 455), (700, 455)]]
CAP["О"] = [oval(500, 455, 260, 305)]
CAP["П"] = [[(300, T), (300, B)], [(300, T), (700, T), (700, B)]]
CAP["Р"] = [[(300, T), (300, B)], [(300, T), (480, T)] + arc(480, 305, 200, 155, 90, -90)[1:] + [(300, 460)]]
CAP["С"] = [arc(520, 455, 265, 305, 40, 320)]
CAP["Т"] = [[(230, T), (770, T)], [(500, T), (500, B)]]
CAP["У"] = [[(250, T), (510, 600)], [(770, T), (500, 610), (380, 860)]]
CAP["Ф"] = [[(500, T), (500, B)], oval(500, 455, 235, 195)]
CAP["Х"] = [[(250, T), (750, B)], [(750, T), (250, B)]]
CAP["Ц"] = [[(270, T), (270, 700)], [(620, T), (620, 700)], [(270, 700), (700, 700), (700, 830)]]
CAP["Ч"] = [[(280, T), (280, 330), (310, 400), (380, 440), (480, 455), (580, 452), (700, 435)], [(700, T), (700, B)]]
CAP["Ш"] = [[(220, T), (220, B)], [(500, T), (500, B)], [(780, T), (780, B)], [(220, B), (780, B)]]
CAP["Щ"] = [[(210, T), (210, 700)], [(460, T), (460, 700)], [(710, T), (710, 700)],
            [(210, 700), (780, 700), (780, 830)]]
CAP["Ъ"] = [[(180, T), (330, T), (330, B)], bowl(330, 440, B, 500, 175)]
CAP["Ы"] = [[(220, T), (220, B)], bowl(220, 440, B, 430, 170), [(780, T), (780, B)]]
CAP["Ь"] = [[(260, T), (260, B)], bowl(260, 440, B, 480, 190)]
CAP["Э"] = [arc(480, 455, 265, 305, 140, -140), [(330, 455), (700, 455)]]
CAP["Ю"] = [[(200, T), (200, B)], [(200, 455), (360, 455)], oval(600, 455, 215, 305)]
CAP["Я"] = [[(700, T), (700, B)], [(700, T), (520, T)] + arc(520, 305, 200, 155, 90, 270)[1:] + [(700, 460)],
            [(520, 460), (260, B)]]

ORDER_UP = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ORDER_LO = ORDER_UP.lower()


def shrink(strokes):
    """The capital scaled down to the x-height, as printed small letters are."""
    k = (B - XH) / (B - T)
    return [[(500 + (x - 500) * 0.9, XH + (y - T) * k) for x, y in s] for s in strokes]


LOW = {}
for up in ORDER_UP:
    lo = up.lower()
    if lo in "абеёруф":
        continue
    LOW[lo] = shrink(CAP[up])
LOW["а"] = [arc(470, 545, 190, 215, 50, 410), [(660, 335), (660, B)]]
LOW["б"] = [[(650, 140), (540, 165), (440, 265), (372, 405), (333, 560)], oval(510, 590, 180, 170)]
LOW["е"] = [[(330, 545), (670, 545)] + arc(500, 545, 170, 215, 0, 330)]
LOW["ё"] = LOW["е"] + dots((400, 240), (600, 240))
LOW["р"] = [[(330, XH), (330, 960)], arc(515, 545, 185, 215, 168, -168)]
LOW["у"] = [[(270, XH), (490, 690)], [(730, XH), (490, 700), (370, 960)]]
LOW["ф"] = [[(500, 130), (500, 960)], oval(500, 545, 215, 200)]

# ---------------------------------------------------------------- readings
# letter: (sound as in English, name in Cyrillic, name romanized)
INFO = {
    "а": ("a", "а", "a"), "б": ("b", "бэ", "be"), "в": ("v", "вэ", "ve"), "г": ("g", "гэ", "ge"),
    "д": ("d", "дэ", "de"), "е": ("ye", "е", "ye"), "ё": ("yo", "ё", "yo"), "ж": ("zh", "жэ", "zhe"),
    "з": ("z", "зэ", "ze"), "и": ("ee", "и", "ee"), "й": ("y", "и краткое", "ee kratkoye"),
    "к": ("k", "ка", "ka"), "л": ("l", "эль", "el"), "м": ("m", "эм", "em"), "н": ("n", "эн", "en"),
    "о": ("o", "о", "o"), "п": ("p", "пэ", "pe"), "р": ("r", "эр", "er"), "с": ("s", "эс", "es"),
    "т": ("t", "тэ", "te"), "у": ("oo", "у", "oo"), "ф": ("f", "эф", "ef"), "х": ("kh", "ха", "kha"),
    "ц": ("ts", "цэ", "tse"), "ч": ("ch", "че", "che"), "ш": ("sh", "ша", "sha"),
    "щ": ("shch", "ща", "shcha"), "ъ": ("hard sign", "твёрдый знак", "tvyordy znak"),
    "ы": ("ih", "ы", "y"), "ь": ("soft sign", "мягкий знак", "myagky znak"),
    "э": ("e", "э", "e"), "ю": ("yu", "ю", "yu"), "я": ("ya", "я", "ya"),
}
DETAIL = {
    "й": "a short i that ends a syllable, like the y in boy", "р": "a rolled or tapped r",
    "ы": "a hard, back-of-the-mouth i that does not exist in English",
    "ъ": "no sound of its own: it separates a prefix from the next vowel",
    "ь": "no sound of its own: it softens the consonant before it", "е": "ye, or e after a soft consonant",
    "и": "ee, as in see", "у": "oo, as in moon", "х": "like ch in Scottish loch",
    "ц": "ts, as in cats", "щ": "a long, soft sh", "ж": "like the s in measure", "э": "e, as in met",
}
VOWELS = "аеёиоуыэюя"
# what the voice says for the sound: a consonant is said with а so it can be pronounced
SOUND_SAY = {c: c + "а" for c in "бвгджзклмнпрстфхцчшщ"}
SOUND_SAY.update({c: c for c in VOWELS})
SOUND_SAY["й"] = "и краткое"
SOUND_SAY["ъ"] = "твёрдый знак"
SOUND_SAY["ь"] = "мягкий знак"


def flat(strokes):
    return [[int(round(v)) for p in s for v in p] for s in strokes]


def main():
    preview = Path(sys.argv[sys.argv.index("--preview") + 1]) if "--preview" in sys.argv else None
    chars, readings = {}, {}
    for ch in ORDER_UP:
        chars[ch] = flat(CAP[ch])
    for ch in ORDER_LO:
        chars[ch] = flat(LOW[ch])
    for ch in chars:
        snd, name, rom = INFO[ch.lower()]
        readings[ch] = {
            "r": [snd, "%s (%s)" % (name, rom)] if name != rom else [snd, name],
            "says": [SOUND_SAY[ch.lower()], name],
            "say": SOUND_SAY[ch.lower()],
            "m": ([DETAIL[ch.lower()]] if ch.lower() in DETAIL else []) + ["letter name: %s" % name],
        }
    out = ROOT / "assets" / "writing"
    (out / "ru_strokes.json").write_text(json.dumps(
        {"v": 1, "src": "Authored for Lingotopia: printed Cyrillic letters, centerline strokes",
         "chars": chars}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (out / "ru_readings.json").write_text(json.dumps(
        {"v": 1, "src": "Letter names and approximate English sounds", "chars": readings},
        ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print("letters", len(chars), "strokes file", (out / "ru_strokes.json").stat().st_size // 1024, "KB")

    if preview:
        from PIL import Image, ImageDraw, ImageFont
        preview.mkdir(parents=True, exist_ok=True)
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
        lst = list(chars)
        cell, cols = 150, 11
        rows = (len(lst) + cols - 1) // cols
        img = Image.new("RGB", (cols * cell, rows * cell), "white")
        d = ImageDraw.Draw(img)
        for n, ch in enumerate(lst):
            ox, oy = (n % cols) * cell, (n // cols) * cell
            d.rectangle([ox + 3, oy + 3, ox + cell - 3, oy + cell - 3], outline="#ccc")
            for k, s in enumerate(chars[ch]):
                pts = [(ox + 3 + s[i] * (cell - 6) / 1000, oy + 3 + s[i + 1] * (cell - 6) / 1000)
                       for i in range(0, len(s), 2)]
                col = ["#c0392b", "#2471a3", "#1e8449", "#b7950b", "#7d3c98", "#117a65"][k % 6]
                d.line(pts, fill=col, width=3)
            d.text((ox + 6, oy + 4), ch, fill="black", font=font)
        img.save(preview / "ru.png")


if __name__ == "__main__":
    main()
