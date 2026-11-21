#!/usr/bin/env python3
"""Render the Lingotopia app icons from icon_fg.svg (chameleon, globe, speech bubble) and
icon_bg.svg (purple gradient), once for the neutral icon and once per language (the character in the
speech bubble changes: Я for Russian, あ for Japanese, ...; see icon_keys.py).

Needs: rsvg-convert (librsvg) and Pillow.   Run from the project root:
    python3 tools/icon/build_icons.py

Writes
  assets/icon/app_icon_1024.png                      neutral icon, rounded square (store / preview)
  assets/icon/win/<key>.ico                          window and taskbar icons, switched at run time on Windows
  windows/runner/resources/app_icon.ico              the .exe's own icon (neutral)
  android/app/src/main/res/mipmap-*/ic_launcher.png  legacy launcher icons (neutral) and ic_launcher_<key>.png
  android/app/src/main/res/mipmap-anydpi-v26/ic_launcher[_<key>].xml   adaptive icons
  android/app/src/main/res/drawable-*/ic_launcher_[<key>_]foreground.png, ic_launcher_background.png
  tools/icon/preview.png                             contact sheet of every variant
The android/ and windows/ folders hold only the icon files: extract the zip over your project.
Android needs a one-time manifest change for the language icons: see patch_android_manifest.py.
"""
import io, os, re, subprocess, sys
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from icon_keys import VARIANTS, DEFAULT_GLYPH  # noqa: E402

ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
S = 1024
FG_SVG = open(os.path.join(HERE, "icon_fg.svg"), encoding="utf-8").read()
TEXT_RE = re.compile(r"<text\b[^>]*>.*?</text>", re.S)


def svg_with_glyph(glyph):
    n = len(glyph)
    size = 84 if n >= 2 else 112
    font = "DejaVu Sans" if re.search(r"[A-Za-zЀ-ӿ؀-ۿÀ-ɏ’]", glyph) else "Noto Sans CJK SC"
    text = (f'<text x="685" y="{322 if n >= 2 else 335}" font-family="{font}, Noto Sans CJK SC, sans-serif" font-weight="700" '
            f'font-size="{size}" fill="#fff" text-anchor="middle">{glyph}</text>')
    assert TEXT_RE.search(FG_SVG), "icon_fg.svg has no <text> element"
    return TEXT_RE.sub(text, FG_SVG, count=1)


def render_svg(svg_text, size=S):
    out = subprocess.run(["rsvg-convert", "-w", str(size), "-h", str(size)], input=svg_text.encode("utf-8"),
                         check=True, capture_output=True).stdout
    return Image.open(io.BytesIO(out)).convert("RGBA")


bg = render_svg(open(os.path.join(HERE, "icon_bg.svg"), encoding="utf-8").read())


def centred(img, scale, box=None):
    """Crop to the artwork, centre it on a transparent canvas, longest side = scale of the canvas."""
    art = img.crop(box or img.getbbox())
    k = scale * S / max(art.size)
    art = art.resize((round(art.width * k), round(art.height * k)), Image.LANCZOS)
    canvas = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    canvas.paste(art, ((S - art.width) // 2, (S - art.height) // 2), art)
    return canvas


def rounded(img, radius_frac=0.22):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius=int(img.width * radius_frac), fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def save(img, path, size=None):
    p = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    if size:
        img = img.resize((size, size), Image.LANCZOS)
    img.save(p)


RES = "android/app/src/main/res"
DENS_LEGACY = (("mdpi", 48), ("hdpi", 72), ("xhdpi", 96), ("xxhdpi", 144), ("xxxhdpi", 192))
DENS_ADAPT = (("mdpi", 108), ("hdpi", 162), ("xhdpi", 216), ("xxhdpi", 324), ("xxxhdpi", 432))

# The artwork box is fixed by the neutral icon, so every variant sits in exactly the same place.
neutral_fg = render_svg(svg_with_glyph(DEFAULT_GLYPH))
BOX = neutral_fg.getbbox()

sheet = []
for key, _deck, glyph, lang in [("default", None, DEFAULT_GLYPH, "neutral")] + VARIANTS:
    fg = neutral_fg if key == "default" else render_svg(svg_with_glyph(glyph))
    legacy = rounded(Image.alpha_composite(bg, centred(fg, 0.74, BOX)))
    adaptive_fg = centred(fg, 0.56, BOX)
    sheet.append((key, legacy))
    suffix = "" if key == "default" else f"_{key}"
    for d, px in DENS_LEGACY:
        save(legacy, f"{RES}/mipmap-{d}/ic_launcher{suffix}.png", px)
    for d, px in DENS_ADAPT:
        save(adaptive_fg, f"{RES}/drawable-{d}/ic_launcher{suffix}_foreground.png", px)
        if key == "default":
            save(bg, f"{RES}/drawable-{d}/ic_launcher_background.png", px)
    xml = os.path.join(ROOT, RES, "mipmap-anydpi-v26", f"ic_launcher{suffix}.xml")
    os.makedirs(os.path.dirname(xml), exist_ok=True)
    open(xml, "w").write(f'''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/ic_launcher_background"/>
    <foreground android:drawable="@drawable/ic_launcher{suffix}_foreground"/>
</adaptive-icon>
''')
    ico = os.path.join(ROOT, "assets/icon/win", f"{key}.ico")
    os.makedirs(os.path.dirname(ico), exist_ok=True)
    legacy.save(ico, sizes=[(n, n) for n in (16, 24, 32, 48, 64, 128, 256)])
    if key == "default":
        save(legacy, "assets/icon/app_icon_1024.png")
        save(legacy, f"{RES}/mipmap-xxxhdpi/ic_launcher_playstore.png", 512)
        exe = os.path.join(ROOT, "windows/runner/resources/app_icon.ico")
        os.makedirs(os.path.dirname(exe), exist_ok=True)
        legacy.save(exe, sizes=[(n, n) for n in (16, 24, 32, 48, 64, 128, 256)])

cols = 7
rows = (len(sheet) + cols - 1) // cols
cell = 200
img = Image.new("RGBA", (cols * cell, rows * cell), (235, 235, 240, 255))
for i, (key, im) in enumerate(sheet):
    t = im.resize((cell - 20, cell - 20), Image.LANCZOS)
    img.paste(t, ((i % cols) * cell + 10, (i // cols) * cell + 10), t)
img.save(os.path.join(HERE, "preview.png"))
print("icons written:", len(sheet))
