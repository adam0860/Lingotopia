#!/usr/bin/env python3
"""
Structural checks for the Italian deck. Exits non-zero on any failure.

These catch the mechanical errors a review pass is bad at: a leftover "TODO"
or wiki markup in a gloss, a noun with no gender, a sentence with stray
characters, duplicate lemmas, broken counts. They do NOT check that glosses
are *right* - that needs a person.

    python3 tools/check_deck_italian.py assets/decks/italian_core.json
    python3 tools/check_deck_italian.py assets/decks/italian_core.json --lemmas

--lemmas additionally runs spaCy over every example sentence and requires the
card's lemma (or an inflected form of it) to occur (needs spacy + it_core_news_sm).
"""

import collections
import json
import re
import sys

WORD = re.compile(r"^[A-Za-zàèéìíîòóùú]+$")
SENT_OK = re.compile(r"^[A-Za-zÀ-ÿ ,.?!'’\"\-:;…]+$")
POS_CODES = {"n", "v", "adj", "adv", "pron", "det", "post", "conj", "part", "interj", "num"}
GENDER = {"masculine noun", "feminine noun", "noun (m/f)"}


def lemma_ok(w, text, forms):
    """Does the sentence plausibly contain headword w? spaCy's lemma/surface set
    must contain it, or (for words it analyses differently) a stem must occur."""
    if w in forms:
        return True
    t = text.lower()
    if w.endswith("arsi") or w.endswith("ersi") or w.endswith("irsi"):
        base = w[:-2] + "e" if w.endswith(("ersi",)) else w[:-2]
        if base in forms:
            return True
    stem = w[:-3] if w.endswith(("are", "ere", "ire")) and len(w) > 5 else w[:-1] if len(w) > 3 else w
    return len(stem) >= 3 and stem in t


def main(path, check_lemmas):
    deck = json.load(open(path, encoding="utf-8"))
    cards = deck["cards"]
    errors = []

    def err(msg):
        errors.append(msg)

    if deck.get("cardCount") != len(cards):
        err(f"cardCount {deck.get('cardCount')} != {len(cards)}")
    nlp = None
    if check_lemmas:
        import spacy
        nlp = spacy.load("it_core_news_sm")
    ids, lemmas = set(), set()
    n_sent = 0
    pending = []
    for i, c in enumerate(cards, 1):
        cid, w = c["id"], c["lemma"]
        if c["rank"] != i:
            err(f"{cid}: rank {c['rank']} != position {i}")
        if cid != f"it_{i:05d}":
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
        pn = c.get("posName")
        if not pn:
            err(f"{cid} {w}: no posName")
        if c.get("pos") == "n" and pn not in GENDER and pn != "proper noun":
            err(f"{cid} {w}: noun without gender label ({pn!r})")
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
            if nlp is not None:
                pending.append((s["id"], w, t))
    if pending:
        for (sid, w, t), doc in zip(pending, nlp.pipe([p[2] for p in pending], batch_size=500,
                                                       disable=["parser", "ner"])):
            forms = set()
            for tok in doc:
                forms.add(tok.lemma_.lower())
                forms.add(tok.text.lower())
            if not lemma_ok(w.lower(), t, forms):
                err(f"{sid}: lemma {w} not found in analysis of: {t}")
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
    main(args[0] if args else "assets/decks/italian_core.json", "--lemmas" in sys.argv)
