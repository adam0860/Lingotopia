#!/usr/bin/env python3
"""
Extend the Russian core deck from 5,000 to 10,000 words WITHOUT touching the
first 5,000 cards.

Card ids are rank-based (ru_00001 ...) and learner progress is keyed by card id,
so the existing cards, their ids and their order must not change. This script
runs the same pipeline as generate_deck.py (wordfreq -> spaCy lemmas ->
Wiktionary glosses -> Tatoeba sentences), drops every lemma already in the base
deck, filters out what makes a poor flashcard, and appends the next 5,000 as
ranks 5001-10000.

Extra filters at this depth (the long tail of a web frequency list is full of
junk that the top 5,000 never meets):
  - no glossless lemmas, no "form of" / "inflection of" entries
  - no proper nouns, abbreviations or single letters
  - no entries whose first sense is vulgar, offensive or an ethnic slur
  - no lemmas whose only dictionary sense is obsolete/archaic/dialectal
  - hand edits from tools/overrides/ru_ext.json (drop / regloss / repos)

Usage
-----
    LINGO_SRC=tools/sources python3 tools/extend_deck_russian.py \
        --base assets/decks/russian_core.json --to 10000 \
        --out assets/decks/russian_core.json
"""

import argparse
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generate_deck as g  # noqa: E402

BAD_FIRST_SENSE = re.compile(
    r"^\((?:[^)]*\b)?(vulgar|offensive|ethnic slur|slur|derogatory|obscene)\b",
    re.I)
BAD_ANYWHERE = re.compile(r"\b(ethnic slur|racial slur|offensive term)\b", re.I)
FORM_OF = re.compile(
    r"\b(form of|inflection of|plural of|genitive|dative|accusative|"
    r"instrumental|prepositional|nominative|vocative|locative|"
    r"singular of|participle of|gerund of|imperative of|past of|"
    r"alternative|misspelling|abbreviation|initialism|acronym|"
    r"diminutive of|short form|superlative of|comparative of|"
    r"clipping of|synonym of|obsolete spelling)\b", re.I)
OLD_ONLY = re.compile(r"^\((?:[^)]*\b)?(obsolete|archaic|dated|dialectal|historical|rare)\b[^)]*\)", re.I)


def norm(s):
    return s.replace("ё", "е")


_TRANSLIT = re.compile(r"([А-Яа-яЁё\u0301]+) \(([^()“”]+), “([^”]+)”\)")
_MF = re.compile(r"\s*\(?\b(?:m or f|f or m)\b\)?")


def tidy(gloss):
    """Wiktionary glosses carry romanisations and gender tags that clutter a card."""
    gloss = _TRANSLIT.sub(r"\1 (“\3”)", gloss)
    gloss = _MF.sub("", gloss)
    return gloss.strip(" ;,")


def tidy_deck(deck, ext):
    """Re-apply tidy() and the hand glosses in ru_ext.json to ranks 5001+ only."""
    n = 0
    for c in deck["cards"]:
        if c["rank"] <= 5000:
            continue
        old = c["gloss"]
        ov = ext.get(c["lemma"], {}).get("gloss")
        c["gloss"] = ov if ov else tidy(old)
        n += c["gloss"] != old
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", required=True)
    ap.add_argument("--to", type=int, default=10000)
    ap.add_argument("--candidates", type=int, default=150000)
    ap.add_argument("--sentences", type=int, default=2)
    ap.add_argument("--out", required=True)
    ap.add_argument("--tidy-only", action="store_true",
                    help="only re-apply gloss clean-up and ru_ext.json glosses to an already extended deck")
    a = ap.parse_args()

    if a.tidy_only:
        deck = json.load(io.open(a.base, encoding="utf-8"))
        ext_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "overrides", "ru_ext.json")
        ext = {k: v for k, v in json.load(io.open(ext_path, encoding="utf-8")).items() if not k.startswith("_")}
        n = tidy_deck(deck, ext)
        with io.open(a.out, "w", encoding="utf-8") as fh:
            json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
        print(f"{n} glosses changed")
        return

    base = json.load(io.open(a.base, encoding="utf-8"))
    cards = [c for c in base["cards"] if c["rank"] <= 5000]
    assert len(cards) == 5000 and cards[-1]["id"] == "ru_05000", "base must be the 5,000-card deck"
    have = {norm(c["lemma"]) for c in cards}

    cfg = dict(g.LANGS["ru"])
    cfg["code"] = "ru"
    import spacy
    g.log("[1/5] frequency candidates")
    cands = g.frequency_candidates("ru", a.candidates)
    g.log("[2/5] lemmatising")
    nlp = spacy.load(cfg["spacy"])
    ranked = g.lemmatise_candidates(nlp, cands, cfg)
    g.log(f"      {len(ranked)} lemmas")

    g.log("[3/5] glosses")
    wikt, forms, stress_index = g.load_wiktionary(os.path.join(g.SRC, cfg["dict"]))

    g.log("[4/5] sentences")
    pairs = list(g.load_sentence_pairs(os.path.join(g.SRC, cfg["sentences"]), cfg["sentence_format"]))
    sent_index = g.index_sentences(nlp, pairs, "ru")

    ext_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "overrides", "ru_ext.json")
    ext = {}
    if os.path.exists(ext_path):
        ext = {k: v for k, v in json.load(io.open(ext_path, encoding="utf-8")).items() if not k.startswith("_")}
    drop = {k for k, v in ext.items() if v.get("drop")}

    g.log("[5/5] assembling ranks 5001-%d" % a.to)
    new = []
    stats = {"base": 0, "nogloss": 0, "formof": 0, "proper": 0, "vulgar": 0, "old": 0, "dropped": 0, "short": 0}
    for lemma, spos, score in ranked:
        if len(cards) + len(new) >= a.to:
            break
        if norm(lemma) in have:
            stats["base"] += 1
            continue
        if lemma in drop:
            stats["dropped"] += 1
            continue
        if len(lemma) < 3 and lemma not in ext:
            stats["short"] += 1
            continue
        blocks = wikt.get(lemma)
        via = None
        if blocks is None:
            alt = forms.get(lemma)
            blocks = wikt.get(alt) if alt else None
            via = alt if blocks else None
        if via:                       # a bare inflected form: not a lemma card
            stats["formof"] += 1
            continue
        entry = g.choose_sense(blocks, spos) if blocks else None
        if entry is None or entry.get("deprioritised") or not entry.get("gloss"):
            stats["nogloss"] += 1
            continue
        ov = ext.get(lemma, {})
        entry.update({k: v for k, v in ov.items() if k in ("pos", "posName", "gloss")})
        gloss = entry["gloss"]
        if entry.get("posName") == "proper noun":
            stats["proper"] += 1
            continue
        if FORM_OF.search(gloss.split(";")[0]) and "gloss" not in ov:
            stats["formof"] += 1
            continue
        if (BAD_FIRST_SENSE.search(gloss) or BAD_ANYWHERE.search(gloss)) and "gloss" not in ov:
            stats["vulgar"] += 1
            continue
        if OLD_ONLY.match(gloss) and ";" not in gloss and "gloss" not in ov:
            stats["old"] += 1
            continue

        rank = len(cards) + len(new) + 1
        cid = f"ru_{rank:05d}"
        sents = [{"id": f"{cid}_s{i}", "text": t, "translation": e}
                 for i, (t, e, _n) in enumerate(sent_index.get(lemma, [])[: a.sentences], 1)]
        card = {"id": cid, "rank": rank, "lemma": lemma, "pos": entry.get("pos") or g.POS_SHORT.get(spos, ""),
                "posName": entry.get("posName") or spos.lower(), "gloss": tidy(gloss), "sentences": sents}
        st = stress_index.get(lemma)
        if st and sum(1 for ch in lemma if ch in g.RU_VOWELS) >= 2:
            card["stressed"] = st
        new.append(card)

    allc = cards + new
    with_s = sum(1 for c in allc if c["sentences"])
    deck = dict(base)
    deck.update({
        "cardCount": len(allc),
        "sentenceCount": sum(len(c["sentences"]) for c in allc),
        "coverage": {"cardsWithSentences": with_s, "cardsWithoutSentences": len(allc) - with_s},
        "cards": allc,
    })
    with io.open(a.out, "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False, separators=(",", ":"))
    g.log(f"      {len(new)} new cards; total {len(allc)}; with sentences {with_s}")
    g.log(f"      skipped: {stats}")


if __name__ == "__main__":
    main()
