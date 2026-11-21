#!/usr/bin/env python3
"""
Structural checks for the Tagalog deck. Exits non-zero on any failure.

These catch the mechanical errors a review pass is bad at: a leftover "TODO" or
wiki markup in a gloss, a sentence with stray characters, duplicate lemmas,
broken counts. They do NOT check that glosses are *right* - that needs a person.

    python3 tools/check_deck_tagalog.py assets/decks/tagalog_core.json
    python3 tools/check_deck_tagalog.py assets/decks/tagalog_core.json --lemmas

--lemmas additionally requires every example sentence to contain a form of the
card's headword (or of the root it is built on), using tools/tagalog_morph.py
and the Wiktionary dump (LINGO_SRC/tl/tl_en.tsv).
"""

import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = re.compile(r"^[A-Za-zÑñ][A-Za-zÑñ'\-]*$")
SENT_OK = re.compile(r"^[A-Za-zÑñ ,.?!'’\"\-:;…]+$")
POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}


def sentence_has_word(lex, tm, lemma, text, cache):
    cids = tm.card_ids(lex, lemma)
    if not cids:
        return True  # headword not in the dictionary dump (added by hand): cannot check
    fam = tm.family(lex, cids)
    for tok in re.findall(r"[A-Za-zÑñ][A-Za-zÑñ'\-]*", text):
        t = tok.lower()
        if t not in cache:
            cache[t] = tm.all_roots(t, lex)
        if cache[t] & fam:
            return True
    return False


def main(path, check_lemmas):
    deck = json.load(open(path, encoding="utf-8"))
    cards = deck["cards"]
    errors = []

    def err(msg):
        errors.append(msg)

    if deck.get("cardCount") != len(cards):
        err(f"cardCount {deck.get('cardCount')} != {len(cards)}")
    lex = tm = None
    cache = {}
    if check_lemmas:
        import tagalog_morph as tm
        src = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "tl", "tl_en.tsv")
        lex = tm.Lexicon(src)
    ids, lemmas = set(), set()
    n_sent = 0
    for i, c in enumerate(cards, 1):
        cid, w = c["id"], c["lemma"]
        if c["rank"] != i:
            err(f"{cid}: rank {c['rank']} != position {i}")
        if cid != f"tl_{i:05d}":
            err(f"{cid}: id does not match position {i}")
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
            if lex is not None and not sentence_has_word(lex, tm, w, t, cache):
                err(f"{s['id']}: no form of {w} found in: {t}")
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
    main(args[0] if args else "assets/decks/tagalog_core.json", "--lemmas" in sys.argv)
