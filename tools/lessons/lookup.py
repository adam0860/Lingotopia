#!/usr/bin/env python3
"""Is this word in the 10,000-word deck?  What lemma is it, and how is it stressed?

    LINGO_SRC=/tmp/claude-0/ru10k/sources python3 tools/lessons/lookup.py пациент вакцина вылечить ...

Give any word form. For each one it prints the dictionary lemma(s), the deck rank
(or OUT, meaning the word belongs in the lesson's vocab list) and the attested
stressed spellings of that form."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import themed  # noqa: E402

SRC = os.environ.get("LINGO_SRC", os.path.join(ROOT, "tools", "sources"))
by, fl, lf = themed.load_wk_ext(os.path.join(SRC, "Russian-English_Wiktionary_dictionary.tsv"))
deck = json.load(open(os.path.join(ROOT, "assets", "decks", "russian_core.json"), encoding="utf-8"))
rank = {c["lemma"]: c["rank"] for c in deck["cards"]}
gloss = {c["lemma"]: c["gloss"] for c in deck["cards"]}

for w in sys.argv[1:]:
    w = w.lower().replace("́", "")
    lems = sorted(fl.get(w, set()) | ({w} if w in rank else set()))
    if not lems:
        print(f"{w}: NOT A KNOWN WORD FORM")
        continue
    for l in lems:
        r = rank.get(l)
        st = sorted(set().union(*by[w].values())) if w in by else []
        print(f"{w}: lemma {l}  " + (f"deck #{r} ({gloss[l][:40]})" if r else "OUT of deck")
              + (f"  stress: {', '.join(st)}" if st else ""))
