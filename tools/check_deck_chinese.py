#!/usr/bin/env python3
"""
Structural checks for the Mandarin deck. Exits non-zero on any failure, so it
can sit in CI or a pre-commit hook.

These catch the mechanical errors a review pass is bad at — a typo in a pinyin
syllable, a card whose reading has the wrong number of syllables, a leftover
numbered-pinyin reference in a gloss. They do NOT check that glosses are
*right*; that needs a person (or a very careful second pass).

    python3 tools/check_deck_chinese.py assets/decks/chinese_core.json
"""

import collections
import json
import re
import sys

HAN = re.compile(r"[一-鿿]")
HAN_ONLY = re.compile(r"^[一-鿿]+$")
LATIN = re.compile(r"[A-Za-z]")
POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}

TONED = "āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜńňǹḿ"
SYL = re.compile(r"^[a-zü" + TONED + r"]+$", re.I)


def syllables(reading):
    """Split a reading into syllables, ignoring punctuation."""
    out = []
    for tok in reading.split():
        tok = re.sub(r"^[^\w]+|[^\w]+$", "", tok)
        if tok:
            out.append(tok)
    return out


def main(path):
    deck = json.load(open(path, encoding="utf-8"))
    cards = deck["cards"]
    errors = []

    def err(msg):
        errors.append(msg)

    if deck.get("cardCount") != len(cards):
        err(f"cardCount {deck.get('cardCount')} != {len(cards)}")
    ids, lemmas = set(), set()
    n_sent = 0
    for i, c in enumerate(cards, 1):
        cid = c["id"]
        if c["rank"] != i:
            err(f"{cid}: rank {c['rank']} != position {i}")
        if cid != f"zh_{i:05d}":
            err(f"{cid}: id does not match position {i}")
        if cid in ids:
            err(f"{cid}: duplicate id")
        ids.add(cid)

        w = c["lemma"]
        if not HAN_ONLY.match(w):
            err(f"{cid} {w}: lemma is not pure Han")
        if w in lemmas:
            err(f"{cid} {w}: duplicate lemma")
        lemmas.add(w)

        r = c.get("reading", "")
        if not r:
            err(f"{cid} {w}: no reading")
        else:
            syls = syllables(r)
            for s in syls:
                if not SYL.match(s):
                    err(f"{cid} {w}: odd character in reading {r!r}")
                    break
            erhua = w.endswith("儿") and len(w) > 1
            expect = len(w) - (1 if erhua else 0)
            # Erhua forms and the odd word written with fewer syllables than
            # characters are tolerated; anything else must line up.
            if len(syls) != len(w) and len(syls) != expect:
                err(f"{cid} {w}: {len(syls)} syllables for {len(w)} characters ({r!r})")
            if re.search(r"[0-9]", r):
                err(f"{cid} {w}: digit in reading {r!r}")

        g = c.get("gloss", "")
        if not g.strip():
            err(f"{cid} {w}: empty gloss")
        if len(g) > 260:
            err(f"{cid} {w}: gloss too long ({len(g)})")
        if re.search(r"\[[A-Za-z]+[1-5]", g) or "CL:" in g or re.search(r"\S\|\S", g):
            err(f"{cid} {w}: raw CEDICT markup in gloss: {g[:80]!r}")
        if HAN.search(g) and len(HAN.findall(g)) > 12:
            err(f"{cid} {w}: gloss is mostly Chinese")
        if c.get("pos") not in POS_CODES:
            err(f"{cid} {w}: unknown pos {c.get('pos')!r}")
        if not c.get("posName"):
            err(f"{cid} {w}: no posName")

        seen_text = set()
        for j, s in enumerate(c.get("sentences", []), 1):
            n_sent += 1
            if s["id"] != f"{cid}_s{j}":
                err(f"{s['id']}: expected {cid}_s{j}")
            t = s["text"]
            if w not in t:
                err(f"{s['id']}: sentence does not contain {w}: {t}")
            if LATIN.search(t):
                err(f"{s['id']}: Latin letters in Chinese text: {t}")
            if t in seen_text:
                err(f"{s['id']}: duplicate sentence on card")
            seen_text.add(t)
            if not s.get("translation", "").strip():
                err(f"{s['id']}: no translation")
            rd = s.get("reading", "")
            if not rd:
                err(f"{s['id']}: no sentence pinyin")
            else:
                n_han = len(HAN.findall(t))
                syls = [x for x in syllables(rd) if SYL.match(x)]
                # Erhua (儿 read as r) makes the syllable count one short.
                tol = t.count("儿")
                if not (n_han - tol <= len(syls) <= n_han):
                    err(f"{s['id']}: {len(syls)} pinyin syllables for {n_han} characters: {t} / {rd}")

    if deck.get("sentenceCount") != n_sent:
        err(f"sentenceCount {deck.get('sentenceCount')} != {n_sent}")
    with_s = sum(1 for c in cards if c["sentences"])
    cov = deck.get("coverage", {})
    if cov.get("cardsWithSentences") != with_s:
        err(f"coverage.cardsWithSentences {cov.get('cardsWithSentences')} != {with_s}")

    pos_counts = collections.Counter(c["pos"] for c in cards)
    print(f"{len(cards)} cards, {n_sent} sentences, {with_s} cards with sentences")
    print("pos:", dict(pos_counts))
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors[:80]:
            print("  -", e)
        if len(errors) > 80:
            print(f"  ... and {len(errors) - 80} more")
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "assets/decks/chinese_core.json")
