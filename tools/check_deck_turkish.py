#!/usr/bin/env python3
"""
Structural checks for the Turkish deck. Exits non-zero on any failure.

These catch the mechanical errors a review pass is bad at: a leftover "TODO" or
wiki markup in a gloss, a sentence with stray characters, duplicate lemmas,
broken counts. They do NOT check that glosses are *right* - that needs a person.

    python3 tools/check_deck_turkish.py assets/decks/turkish_core.json
    python3 tools/check_deck_turkish.py assets/decks/turkish_core.json --lemmas

--lemmas additionally runs Zeyrek (pl_core_news_sm) over every example sentence and
reports sentences in which no token lemmatises to the card's headword. Zeyrek's
small model misses some forms, so this is a warning list (a few percent is
expected), not a failure, unless more than 4% of sentences are flagged.
"""

import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = re.compile(r"^[a-zçğıöşüâîû]+(?: [a-zçğıöşüâîû]+)?$|^[A-ZÇĞİÖŞÜ][a-zçğıöşüâîû]+$")
SENT_OK = re.compile(r"^[A-Za-zÇĞİıÖŞÜçğöşüÂÎÛâîû ,.?!\"\-:;…']+$")
POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}


def sentence_has_word(forms, lemma):
    """forms: lower-cased tokens of the sentence plus every lemma Zeyrek proposes for them."""
    key = lemma.lower()
    if " " in key:                       # the four legacy phrases: every part must occur
        return all(sentence_has_word(forms, k) for k in key.split())
    return key in forms or any(f.startswith(key[:max(3, len(key) - 3)]) for f in forms if len(key) >= 5)


def main(path, check_lemmas):
    deck = json.load(open(path, encoding="utf-8"))
    cards = deck["cards"]
    errors = []

    def err(msg):
        errors.append(msg)

    if deck.get("cardCount") != len(cards):
        err(f"cardCount {deck.get('cardCount')} != {len(cards)}")
    nlp = None
    warn = []
    n_checked = 0
    az = None
    if check_lemmas:
        import generate_deck_turkish as g
        src = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "tr")
        wk, _ = g.load_wikt(os.path.join(src, "tr_en.tsv"))
        az = g.Analyser({w for w, bl in wk.items() if any(p in ("noun", "adj", "verb", "adv") for p, _ in bl)})
        nlp = True
    ids, lemmas = set(), set()
    n_sent = 0
    for i, c in enumerate(cards, 1):
        cid, w = c["id"], c["lemma"]
        if c["rank"] != i:
            err(f"{cid}: rank {c['rank']} != position {i}")
        if cid != f"tr_{i:05d}" and not re.match(r"^tr_\d{5}_[a-z_]+$", cid):
            err(f"{cid}: id is neither tr_NNNNN (position {i}) nor a legacy id")
        if cid in ids:
            err(f"{cid}: duplicate id")
        ids.add(cid)
        if not WORD.match(w):
            err(f"{cid} {w}: odd lemma")
        if w in lemmas:
            err(f"{cid} {w}: duplicate lemma")
        lemmas.add(w)
        g_ = c.get("gloss", "")
        if not g_.strip() or g_.strip().upper() == "TODO":
            err(f"{cid} {w}: empty/TODO gloss")
        if len(g_) > 200:
            err(f"{cid} {w}: gloss too long ({len(g_)})")
        if re.search(r"\{\{|\}\}|\[\[|\]\]|<[a-z/]+>|&[a-z]+;", g_):
            err(f"{cid} {w}: markup in gloss: {g_[:80]!r}")
        if c.get("pos") not in POS_CODES:
            err(f"{cid} {w}: unknown pos {c.get('pos')!r}")
        if not c.get("posName"):
            err(f"{cid} {w}: no posName")
        seen = set()
        for j, s in enumerate(c.get("sentences", []), 1):
            n_sent += 1
            if not re.fullmatch(re.escape(cid) + r"_s\d+", s["id"]) or s["id"] in {x["id"] for x in c["sentences"][:j - 1]}:
                err(f"{s['id']}: bad or duplicate sentence id on {cid}")
            t = s["text"]
            if not SENT_OK.match(t):
                err(f"{s['id']}: unexpected characters: {t}")
            if t in seen:
                err(f"{s['id']}: duplicate sentence on card")
            seen.add(t)
            if not s.get("translation", "").strip():
                err(f"{s['id']}: no translation")
            if nlp is not None:
                n_checked += 1
                forms = set()
                for tok in g.TOKEN.findall(t):
                    low = g.tr_lower(tok)
                    forms.add(low)
                    for lem, _p, _pr, _r in az.analyse(low):
                        forms.add(g.tr_lower(lem))
                if not sentence_has_word(forms, w):
                    warn.append(f"{s['id']}: no form of {w} found in: {t}")
    if deck.get("sentenceCount") != n_sent:
        err(f"sentenceCount {deck.get('sentenceCount')} != {n_sent}")
    with_s = sum(1 for c in cards if c["sentences"])
    if deck.get("coverage", {}).get("cardsWithSentences") != with_s:
        err(f"coverage.cardsWithSentences {deck.get('coverage', {}).get('cardsWithSentences')} != {with_s}")

    print(f"{len(cards)} cards, {n_sent} sentences, {with_s} cards with sentences")
    print("pos:", dict(collections.Counter(c["pos"] for c in cards)))
    if warn:
        print(f"\n{len(warn)} of {n_checked} sentences without a lemma match (Zeyrek): first 15")
        for x in warn[:15]:
            print("  ?", x)
        if len(warn) > 0.04 * n_checked:
            err(f"{len(warn)} sentences without a lemma match (> 4%)")
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
    main(args[0] if args else "assets/decks/turkish_core.json", "--lemmas" in sys.argv)
