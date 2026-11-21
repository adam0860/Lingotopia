#!/usr/bin/env python3
"""
Structural checks for the Swahili deck. Exits non-zero on any failure.

These catch the mechanical errors a review pass is bad at: a leftover "TODO" or
wiki markup in a gloss, a sentence with stray characters, duplicate lemmas,
broken counts. They do NOT check that glosses are *right* - that needs a person.

    python3 tools/check_deck_swahili.py assets/decks/swahili_core.json
    python3 tools/check_deck_swahili.py assets/decks/swahili_core.json --lemmas

--lemmas additionally requires every example sentence to contain a form of the
card's headword, using tools/swahili_morph.py (the same word-family analyser the
generator uses) and the corpus counts it needs (LINGO_SRC/sw/). It reports
sentences without a match as a warning list and fails only above 3%.
"""

import collections
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = re.compile(r"^(?:-[A-Za-z]+-[A-Za-z]+|-?[A-Za-z]+(?:'[A-Za-z]+)*(?: na)?)$")  # -o-ote is the conventional entry for the -o-ote series
SENT_OK = re.compile(r"^[A-Za-z ,.?!'’\"\-:;…]+$")
POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}


def sentence_has_word(an, sm, fam, lemma, text):
    low = lemma.lower().lstrip("-")
    root = low[2:] if low.startswith(("ku", "kw")) else None
    for tok in re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text):
        t = tok.lower()
        if an.analyze(t) in fam or t == low:
            return True
        if root and len(root) >= 2 and any(r == root for r, _k, _p in sm.verb_parses(t)):
            return True
        if root and len(root) >= 4 and root in t:
            return True
        if not root and len(low) >= 4 and (low[1:] in t):
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
    an = sm = None
    warn, n_checked = [], 0
    if check_lemmas:
        import swahili_morph as sm
        src = os.path.join(os.environ.get("LINGO_SRC", "tools/sources"), "sw")
        lex = sm.Lexicon(os.path.join(src, "sw_en.tsv"))
        counts, votes, _docs = sm.load_corpus(src)
        an = sm.Analyzer(lex, counts, votes)
        fams = {}
    ids, lemmas = set(), set()
    n_sent = 0
    for i, c in enumerate(cards, 1):
        cid, w = c["id"], c["lemma"]
        if c["rank"] != i:
            err(f"{cid}: rank {c['rank']} != position {i}")
        if cid != f"sw_{i:05d}":
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
            if an is not None:
                n_checked += 1
                fam = fams.get(w)
                if fam is None:
                    fam = fams[w] = {an.analyze(w.lower().lstrip("-"))} | (
                        {an.analyze("ku" + w[2:])} if w.startswith("ku") else set())
                if not sentence_has_word(an, sm, fam, w, t):
                    warn.append(f"{s['id']}: no form of {w} found in: {t}")
    if deck.get("sentenceCount") != n_sent:
        err(f"sentenceCount {deck.get('sentenceCount')} != {n_sent}")
    with_s = sum(1 for c in cards if c["sentences"])
    if deck.get("coverage", {}).get("cardsWithSentences") != with_s:
        err(f"coverage.cardsWithSentences {deck.get('coverage', {}).get('cardsWithSentences')} != {with_s}")

    print(f"{len(cards)} cards, {n_sent} sentences, {with_s} cards with sentences")
    print("pos:", dict(collections.Counter(c["pos"] for c in cards)))
    if warn:
        print(f"\n{len(warn)} of {n_checked} sentences without a lemma match: first 15")
        for x in warn[:15]:
            print("  ?", x)
        if len(warn) > 0.03 * n_checked:
            err(f"{len(warn)} sentences without a lemma match (> 3%)")
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
    main(args[0] if args else "assets/decks/swahili_core.json", "--lemmas" in sys.argv)
