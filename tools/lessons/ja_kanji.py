"""Helpers for the kanji lessons of the Genki I and II Reading and Writing sections.

A kanji block is plain text, one kanji per line:

    一|one|いち・いっ|ひと|1|一(いち)=one;一時(いちじ)=one o'clock;...

fields: kanji | meaning | on-yomi | kun-yomi ("-" when none) | strokes | words (WORD(kana)=English separated by ;)
"""
import re
from dsl_ja import *
from ja_unit4 import three


def parse(block):
    rows = []
    for line in block.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        k, mean, on, kun, st, words = [p.strip() for p in line.split("|")]
        ws = []
        for w in words.split(";"):
            w = w.strip()
            if not w:
                continue
            m = re.match(r"^([^()]+)\(([^()]+)\)\s*=\s*(.+)$", w)
            assert m, (line, w)
            ws.append((m.group(1).strip(), m.group(2).strip(), m.group(3).strip()))
        rows.append(dict(k=k, mean=mean, on=on, kun=kun, strokes=int(st), words=ws))
    return rows


def _words(rows):
    seen, out = set(), []
    for r in rows:
        for w, kana, en in r["words"]:
            if w not in seen:
                seen.add(w)
                out.append((w, kana, en))
    return out


def _wtable(ws, over=None):
    """Words table: reading (spoken), word, romaji, meaning. A reading with two forms (しち・なな) is romanised part by part."""
    rows = []
    for w, kana, en in ws:
        parts = kana.split("・")
        rm = " / ".join(R.romanize(p, over) for p in parts)
        for p in parts:
            SHOWN.append((p, over, R.romanize(p, over)))
        rows.append([kana, w, rm, en])
    return table(["Reading", "Word", "Romaji", "Meaning"], rows, say=[0])


def kanji_cards(rows, per=4, over=None):
    """Cards of `per` kanji: a table of readings and a table of the book's example words."""
    cards = []
    for i in range(0, len(rows), per):
        grp = rows[i:i + per]
        ks = " ".join(r["k"] for r in grp)
        reads = table(["Kanji", "Meaning", "On-yomi ▶", "Kun-yomi ▷", "Strokes"],
                      [[r["k"], r["mean"], r["on"], r["kun"], str(r["strokes"])] for r in grp], say=[])
        words = _wtable(_words(grp), over)
        cards.append(card(f"Kanji: {ks}",
                          "▶ is the on-yomi (the reading borrowed from Chinese) and ▷ is the kun-yomi (the native Japanese reading). The reading of each word is spoken when you tap it.",
                          tables=[reads, words]))
    return cards


def _near(n):
    out = []
    for d in (1, -1, 2, -2, 3):
        v = n + d
        if v >= 1 and v != n and v not in out:
            out.append(v)
    return out[:3]


def kanji_exercises(rows, allrows=None):
    """Meaning, kanji, stroke-count, reading and word questions for the kanji in `rows`."""
    allrows = allrows or rows
    out = []
    means = [r["mean"] for r in allrows]
    ks = [r["k"] for r in allrows]
    for r in rows:
        j = ks.index(r["k"])
        rm, rk = means[j + 1:] + means[:j], ks[j + 1:] + ks[:j]
        out.append(M(f"What does {r['k']} mean?", r["mean"], three([m for m in rm if m != r["mean"]]), f"{r['k']} means “{r['mean']}”."))
        out.append(M(f"Which kanji means “{r['mean']}”?", r["k"], three([k for k in rk if k != r["k"]]), f"{r['mean']} is {r['k']}."))
        out.append(M(f"How many strokes does {r['k']} have?", f"{r['strokes']}", [str(x) for x in _near(r["strokes"])], f"{r['k']} is written with {r['strokes']} strokes."))
    aw = _words(allrows)
    for w, kana, en in _words(rows):
        i = [x for x, _, _ in aw].index(w)
        rot = aw[i + 1:] + aw[:i]
        out.append(M(f"How do you read {w}?", kana, three([k for _, k, _ in rot if k != kana]), f"{w} is read {kana} ({romaji(kana)}): {en}."))
        if sum(1 for _, _, e in aw if e == en) == 1:
            out.append(M(f"Which word means “{en}”?", w, three([x for x, _, e in rot if x != w and e != en]), f"{en} is {w} ({kana})."))
    return out
