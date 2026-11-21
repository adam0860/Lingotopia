#!/usr/bin/env python3
"""
Compile the Arabic (MSA) lessons (tools/lessons/ar_unit*.py) into
assets/lessons/ar_lessons.json, running every automatic check first.

    python3 tools/lessons/build_ar_lessons.py            # build + check
    python3 tools/lessons/build_ar_lessons.py --units 1  # only some units
    python3 tools/lessons/build_ar_lessons.py --force    # write despite errors

The spelling / vowelling / gloss checks read the Arabic Wiktionary dictionary
that tools/fetch_sources.sh downloads. If it is missing those checks are
skipped and only structure, script and vowel-completeness are verified.
"""
import argparse
import glob
import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

from dsl_ar import check_ar, compile_course, load_deck_ranks, load_wiktionary_ar, write_json  # noqa: E402

SRC = os.environ.get("LINGO_SRC", os.path.join(ROOT, "tools", "sources"))
DECK = os.path.join(ROOT, "assets", "decks", "arabic_msa_core.json")
WIKT = os.path.join(SRC, "Arabic-English_Wiktionary_dictionary.tsv")
OUT = os.path.join(ROOT, "assets", "lessons", "ar_lessons.json")

found = sorted(int(re.search(r"ar_unit(\d+)\.py", p).group(1))
               for p in glob.glob(os.path.join(HERE, "ar_unit*.py")))
ap = argparse.ArgumentParser()
ap.add_argument("--units", nargs="*", type=int, default=found)
ap.add_argument("--force", action="store_true")
ap.add_argument("--quiet", action="store_true", help="hide info lines")
args = ap.parse_args()

units = [importlib.import_module(f"ar_unit{n}").UNIT for n in args.units]
app, meta = compile_course(units, language="ar", deck_id="ar_core", prefix="ar")
deck = load_deck_ranks(DECK)

wk = None
if os.path.exists(WIKT):
    print("loading Wiktionary data...", flush=True)
    wk = load_wiktionary_ar(WIKT)
else:
    print(f"NOTE: {WIKT} not found: skipping spelling/vowelling/gloss checks")

errors, warns, info = check_ar(app, meta, deck, wk)

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


def scrub(o):
    """Drop authoring-only keys (leading underscore) before writing."""
    if isinstance(o, dict):
        return {k: scrub(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [scrub(x) for x in o]
    return o


write_json(scrub(app), OUT)
print("wrote", OUT)
