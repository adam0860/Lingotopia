"""One-off: turn the Unit 1 glossary text (pdftotext -layout of the review book) into zh_glossary_data.py.
Usage: python3 make_glossary.py gl_raw.txt > zh_glossary_data.py   (gl_raw.txt: the 5-column glossary rows)"""
import re, sys, unicodedata
from zh_auto import auto_py

TONE = {"̄": 1, "́": 2, "̌": 3, "̀": 4}

def book_letters(py):
    """-> list of (letter, tone_or_0) for the tone-marked pinyin, ü as v, no spaces or apostrophes."""
    s = unicodedata.normalize("NFD", py)
    out = []
    for ch in s:
        if ch in TONE:
            if out:
                out[-1] = (out[-1][0], TONE[ch])
            continue
        if ch == "̈":
            out[-1] = ("v", out[-1][1]); continue
        if ch in " '’-":
            continue
        out.append((ch.lower(), 0))
    return out

OVERRIDE = {"都": "dou1", "跟…一样": "gen1 yi1 yang4", "那儿": "na4r5", "哪儿": "na3r5", "为什么": "wei4 shen2 me5", "好吃": "hao3 chi1"}

def to_numeric(hanzi, py):
    if hanzi in OVERRIDE:
        return OVERRIDE[hanzi], []
    h = hanzi.replace("…", "")
    auto = auto_py(h).split()
    letters = book_letters(py)
    i = 0; res = []; notes = []
    for a in auto:
        m = re.match(r"([a-zv]+)([1-5])$", a)
        syl, at = m.group(1), int(m.group(2))
        if syl == "r":              # erhua: book writes 'er'
            want = "er"
            got = "".join(l for l, _ in letters[i:i + 2])
            if got != want: raise ValueError(f"{hanzi} {py}: erhua mismatch")
            i += 2
            res[-1] = res[-1] + "r5"
            continue
        got = "".join(l for l, _ in letters[i:i + len(syl)])
        if got != syl:
            raise ValueError(f"{hanzi} {py}: expected {syl} at {i}, book has {got}")
        tones = [t for _, t in letters[i:i + len(syl)] if t]
        bt = tones[0] if tones else 5
        i += len(syl)
        if bt != at:
            c = h[len(res)] if len(res) < len(h) else "?"
            notes.append((hanzi, a, bt))
            if a.startswith(("bu", "yi")) and ("不" in h or "一" in h) and {at, bt} <= {1, 2, 4}:
                res.append(a); continue      # keep the spoken (sandhi) tone
            res.append(f"{syl}{bt}")
        else:
            res.append(a)
    if i != len(letters): raise ValueError(f"{hanzi} {py}: leftover letters")
    return " ".join(res), notes

rows = []
allnotes = []
for line in open(sys.argv[1], encoding="utf8"):
    p = [x for x in re.split(r"\s{2,}", line.strip()) if x]
    py, hz, fan, pos, en = p
    num, notes = to_numeric(hz, py)
    allnotes += notes
    rows.append((hz, num, pos, en, fan if fan != hz else ""))
print('"""Unit 1 glossary of the review book: (characters, numeric pinyin, part of speech, English, traditional if different)."""')
print("GLOSSARY = [")
for r in rows:
    print("    " + repr(r) + ",")
print("]")
sys.stderr.write(f"{len(rows)} rows; tone differences between pypinyin and the book: {len(allnotes)}\n")
for n in allnotes: sys.stderr.write("  %s auto %s book %s\n" % n)
