#!/usr/bin/env python3
"""
Compile the Spanish lessons (tools/lessons/es_unit*.py) into
assets/lessons/es_lessons.json, running every automatic check first.

    python3 tools/lessons/build_es_lessons.py            # build + check
    python3 tools/lessons/build_es_lessons.py --units 1  # only some units
    python3 tools/lessons/build_es_lessons.py --force    # write despite errors

The spelling / gender / morphology checks read the Wiktionary dictionary and
noun-gender file that tools/fetch_sources.sh downloads. If they are missing,
those checks are skipped and only structure and gating are verified.
"""
import argparse
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from dsl_es import (check_es, compile_course, load_deck_ranks, load_genders,  # noqa: E402
                    load_wiktionary_es, write_json)

SRC = os.environ.get("LINGO_SRC", os.path.join(ROOT, "tools", "sources"))
DECK = os.path.join(ROOT, "assets", "decks", "spanish_core.json")
WIKT = os.path.join(SRC, "Spanish-English_Wiktionary_dictionary.tsv")
GENDERS = os.path.join(SRC, "es-en.data")
OUT = os.path.join(ROOT, "assets", "lessons", "es_lessons.json")

ap = argparse.ArgumentParser()
_found = sorted(int(f[7:-3]) for f in os.listdir(HERE) if f.startswith("es_unit") and f.endswith(".py"))
ap.add_argument("--units", nargs="*", type=int, default=_found)
ap.add_argument("--force", action="store_true")
ap.add_argument("--quiet", action="store_true", help="hide info lines")
args = ap.parse_args()

units = []
for n in args.units:
    mod = importlib.import_module(f"es_unit{n}")
    units.append(mod.UNIT)

app, meta = compile_course(units, language="es", deck_id="es_core", prefix="es")
deck = load_deck_ranks(DECK)

wk = None
if os.path.exists(WIKT):
    print("loading Wiktionary data (about 20 s)...", flush=True)
    wk = load_wiktionary_es(WIKT)
else:
    print(f"NOTE: {WIKT} not found: skipping spelling/morphology checks")
genders = load_genders(GENDERS)
if not genders:
    print(f"NOTE: {GENDERS} not found: skipping the article/gender check")

errors, warns, info = check_es(app, meta, deck, wk, genders)

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

if errors and not args.force:
    print("not written (fix the errors, or use --force)")
    sys.exit(1)
write_json(app, OUT)
print("wrote", OUT)
