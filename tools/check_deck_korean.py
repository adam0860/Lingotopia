#!/usr/bin/env python3
"""
Structural checks for the Korean deck. Exits non-zero on any failure.

These catch the mechanical errors a review pass is bad at: a leftover "TODO"
or wiki markup in a gloss, a romanization with stray characters, a sentence
that is not Hangul, duplicate lemmas, broken counts. They do NOT check that
glosses are *right* - that needs a person.

    python3 tools/check_deck_korean.py assets/decks/korean_core.json
    python3 tools/check_deck_korean.py assets/decks/korean_core.json --lemmas

--lemmas additionally runs the Kiwi analyser over every example sentence and
requires the card's lemma to be one of the sentence's lemmas (needs kiwipiepy).
"""

import collections
import json
import re
import sys

HANGUL = re.compile(r"[가-힣]")
HANGUL_WORD = re.compile(r"^[가-힣]+(/[가-힣]+)?$")
SENT_OK = re.compile(r"^[가-힣 ,.?!'\"\-~…·]+$")
ROMAN_OK = re.compile(r"^[a-z]+(?: [a-z]+)*(?:/[a-z]+)?$")
POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}


SUFFIXES = ("하다", "되다", "스럽다", "롭다", "시키다", "적")


def lemma_ok(w, t, lem):
    """Does the sentence plausibly contain headword w? The analyser's lemma list
    must contain it, or a derived form (noun + 하다/되다 ...), or - for words it
    segments differently - the headword (nouns) / its stem (verbs) must appear."""
    import generate_deck_korean as g
    if w in lem or g.PARTICLE_OF.get(w) in lem:
        return True
    if any((w + sfx) in lem for sfx in SUFFIXES):
        return True
    if w.endswith("다"):
        pre = w[:-2] if len(w) >= 4 else w[:-1]
        return pre in t
    return len(w) >= 2 and w in t


def main(path, check_lemmas):
    deck = json.load(open(path, encoding="utf-8"))
    cards = deck["cards"]
    errors = []

    def err(msg):
        errors.append(msg)

    if deck.get("cardCount") != len(cards):
        err(f"cardCount {deck.get('cardCount')} != {len(cards)}")
    an = None
    if check_lemmas:
        sys.path.insert(0, "tools")
        import generate_deck_korean as g
        an = g.Analyzer(set())
    ids, lemmas = set(), set()
    n_sent = lemma_miss = 0
    for i, c in enumerate(cards, 1):
        cid, w = c["id"], c["lemma"]
        if c["rank"] != i:
            err(f"{cid}: rank {c['rank']} != position {i}")
        if cid != f"ko_{i:05d}":
            err(f"{cid}: id does not match position {i}")
        if cid in ids:
            err(f"{cid}: duplicate id")
        ids.add(cid)
        if not HANGUL_WORD.match(w):
            err(f"{cid} {w}: lemma is not pure Hangul")
        if w in lemmas:
            err(f"{cid} {w}: duplicate lemma")
        lemmas.add(w)

        r = c.get("reading", "")
        if not r or not ROMAN_OK.match(r):
            err(f"{cid} {w}: odd romanization {r!r}")

        g_ = c.get("gloss", "")
        if not g_.strip() or g_.strip().upper() == "TODO":
            err(f"{cid} {w}: empty/TODO gloss")
        if len(g_) > 200:
            err(f"{cid} {w}: gloss too long ({len(g_)})")
        if re.search(r"\{\{|\}\}|\[\[|\]\]|<[a-z/]+>|&[a-z]+;", g_):
            err(f"{cid} {w}: markup in gloss: {g_[:80]!r}")
        if len(HANGUL.findall(g_)) > 14:
            err(f"{cid} {w}: gloss has a lot of Hangul")
        if c.get("pos") not in POS_CODES:
            err(f"{cid} {w}: unknown pos {c.get('pos')!r}")
        if not c.get("posName"):
            err(f"{cid} {w}: no posName")

        seen = set()
        for j, s in enumerate(c.get("sentences", []), 1):
            n_sent += 1
            if s["id"] != f"{cid}_s{j}":
                err(f"{s['id']}: expected {cid}_s{j}")
            t = s["text"]
            if not SENT_OK.match(t):
                err(f"{s['id']}: unexpected characters: {t}")
            if t in seen:
                err(f"{s['id']}: duplicate sentence on card")
            seen.add(t)
            if not s.get("translation", "").strip():
                err(f"{s['id']}: no translation")
            if an is not None:
                lem = {l for l, _ in an.lemmas(t)}
                if not lemma_ok(w, t, lem):
                    lemma_miss += 1
                    err(f"{s['id']}: lemma {w} not found in analysis of: {t}")

    if deck.get("sentenceCount") != n_sent:
        err(f"sentenceCount {deck.get('sentenceCount')} != {n_sent}")
    with_s = sum(1 for c in cards if c["sentences"])
    if deck.get("coverage", {}).get("cardsWithSentences") != with_s:
        err(f"coverage.cardsWithSentences {deck.get('coverage', {}).get('cardsWithSentences')} != {with_s}")

    print(f"{len(cards)} cards, {n_sent} sentences, {with_s} cards with sentences")
    print("pos:", dict(collections.Counter(c["pos"] for c in cards)))
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors[:80]:
            print("  -", e)
        if len(errors) > 80:
            print(f"  ... and {len(errors) - 80} more")
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main(args[0] if args else "assets/decks/korean_core.json", "--lemmas" in sys.argv)
