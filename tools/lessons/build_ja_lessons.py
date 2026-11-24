#!/usr/bin/env python3
"""
Compile the Japanese lessons (tools/lessons/ja_unit*.py) into assets/lessons/ja_lessons.json, running every
automatic check first.

    python3 tools/lessons/build_ja_lessons.py            # build + check + write
    python3 tools/lessons/build_ja_lessons.py --units 1  # only some units (not written)
    python3 tools/lessons/build_ja_lessons.py --force    # write despite errors
    python3 tools/lessons/build_ja_lessons.py --units 1 --review   # print every Japanese line with its romaji

Each ja_unitN.py exports UNIT = unit("...", [lesson(...), ...]). Unit files are picked up in numeric order;
lesson ids (ja_01, ja_02 ...) follow that order, so ADD new units at the end.
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

import dsl_ja as Z  # noqa: E402

DECK = os.path.join(ROOT, "assets", "decks", "japanese_core.json")
OUT = os.path.join(ROOT, "assets", "lessons", "ja_lessons.json")

found = sorted(int(re.search(r"ja_unit(\d+)\.py", p).group(1)) for p in glob.glob(os.path.join(HERE, "ja_unit*.py")))
ap = argparse.ArgumentParser()
ap.add_argument("--units", nargs="*", type=int, default=found)
ap.add_argument("--force", action="store_true")
ap.add_argument("--quiet", action="store_true")
ap.add_argument("--review", action="store_true")
args = ap.parse_args()

units = [importlib.import_module(f"ja_unit{n}").UNIT for n in args.units]
app, meta = Z.build(units)
Z.convert_app(app)
deck = Z.load_deck(DECK)
errors, warns, info = Z.check_ja(app, meta, deck)

if args.review:
    seen = set()
    for ja, over, r in Z.SHOWN:
        key = (ja, tuple(sorted(over.items())) if over else None)
        if key not in seen:
            seen.add(key)
            print(f"{ja}\t{r}")
    sys.exit(0)

if not args.quiet:
    print("--- info ---")
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
print(f"\n{len(app['units'])} units, {lessons} lessons, {exercises} exercises")

if errors and not args.force:
    print("not written (fix the errors, or use --force)")
    sys.exit(1)


def scrub(o):
    if isinstance(o, dict):
        return {k: scrub(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [scrub(x) for x in o]
    return o


if args.units != found:
    print("partial build (--units): not written")
    sys.exit(0)

Z.write_json(scrub(app), OUT)
print("wrote", OUT)
