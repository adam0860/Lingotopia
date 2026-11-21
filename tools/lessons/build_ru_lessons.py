#!/usr/bin/env python3
"""
Compile the Russian lessons (tools/lessons/ru_unit*.py) into
assets/lessons/russian_lessons.json, running every automatic check first.

    python3 tools/lessons/build_ru_lessons.py            # build + check
    python3 tools/lessons/build_ru_lessons.py --units 1  # only some units
    python3 tools/lessons/build_ru_lessons.py --force    # write despite errors

The spelling / stress / morphology checks read the Wiktionary dictionary that
tools/fetch_sources.sh downloads. If it is missing, those checks are skipped
and only structure and gating are verified.
"""
import argparse
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from dsl import check, compile_course, load_deck_ranks, load_wiktionary, write_json  # noqa: E402

SRC = os.environ.get("LINGO_SRC", os.path.join(ROOT, "tools", "sources"))
DECK = os.path.join(ROOT, "assets", "decks", "russian_core.json")
WIKT = os.path.join(SRC, "Russian-English_Wiktionary_dictionary.tsv")
OUT = os.path.join(ROOT, "assets", "lessons", "russian_lessons.json")

ap = argparse.ArgumentParser()
ap.add_argument("--units", nargs="*", type=int, default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] + list(range(34, 60)))
ap.add_argument("--force", action="store_true")
ap.add_argument("--no-write", action="store_true", help="check only; leave the JSON alone")
ap.add_argument("--quiet", action="store_true", help="hide info lines")
args = ap.parse_args()

units = []
for n in args.units:
    try:
        mod = importlib.import_module(f"ru_unit{n}")
    except ModuleNotFoundError as exc:
        if exc.name == f"ru_unit{n}":
            continue          # unit numbers that do not exist yet
        raise
    units.append(mod.UNIT)

multi = None
if any(u.get("themed") or u.get("autostress") for u in units) and os.path.exists(WIKT):
    import themed
    by, multi, _lf = themed.load_wk_ext(WIKT)
    if any(u.get("autostress") for u in units):
        import spacy
        print("auto-stressing themed readings...", flush=True)
        auto = themed.AutoStress(by, multi, spacy.load("ru_core_news_sm", disable=["parser", "ner"]))
        themed.autostress_units(units, auto)
        print(f"  marked {auto.marked} words; {len(auto.unresolved)} left for hand-marking")

app, meta = compile_course(units)
deck = load_deck_ranks(DECK)

wk = None
if os.path.exists(WIKT):
    print("loading Wiktionary inflection data (about 20 s)...", flush=True)
    wk = load_wiktionary(WIKT)
else:
    print(f"NOTE: {WIKT} not found: skipping spelling/stress/morphology checks")

known_extra = set()
themed_ids = {m["id"]: m["src"].get("themed") for m in meta}
if multi is not None:
    # words the learner has already met in the 340 course lessons count as known
    from dsl import words as _words, strip_acute as _sa
    for u in app["units"]:
        for l in u["lessons"]:
            if themed_ids.get(l["id"]):
                continue
            for e in l["explanations"]:
                bag = [e["body"], e["title"]] + [x["text"] for x in e["examples"]]
                for t in e["tables"]:
                    bag += [c for r in t["rows"] for c in r]
                for q in l["exercises"]:
                    bag += [q["prompt"]] + q["options"]
                for text in bag:
                    known_extra.update(_sa(w).lower() for w in _words(text))
errors, warns, info = check(app, meta, deck, wk, multi=multi, known_extra=known_extra)

if not args.quiet:
    print("\n--- info ---")
    for line in info:
        print(line)
print(f"\n--- {len(warns)} warnings ---")
for w in warns:
    print("  ", w)
print(f"\n--- {len(errors)} ERRORS ---")
for e in errors:
    print("  ", e)

lessons = sum(len(u["lessons"]) for u in app["units"])
exercises = sum(len(l["exercises"]) for u in app["units"] for l in u["lessons"])
print(f"\n{lessons} lessons, {exercises} exercises")

if args.no_write:
    sys.exit(1 if errors else 0)
if errors and not args.force:
    print("not written (fix the errors, or use --force)")
    sys.exit(1)
write_json(app, OUT)
print("wrote", OUT)
