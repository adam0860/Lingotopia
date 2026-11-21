#!/usr/bin/env python3
"""
Compile the Mandarin lessons (tools/lessons/zh_unit*.py) into assets/lessons/zh_lessons.json,
running every automatic check first.

    python3 tools/lessons/build_zh_lessons.py            # build + check + write
    python3 tools/lessons/build_zh_lessons.py --units 1  # only some units
    python3 tools/lessons/build_zh_lessons.py --force    # write despite errors

Needs `pip install pypinyin` for the character/pinyin check (the build warns if it is missing).
Pinyin is authored numerically inside [[ ]] and converted to tone marks; see dsl_zh.py.
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

import dsl_zh as Z  # noqa: E402

DECK = os.path.join(ROOT, "assets", "decks", "chinese_core.json")
OUT = os.path.join(ROOT, "assets", "lessons", "zh_lessons.json")

found = sorted(int(re.search(r"zh_unit(\d+)\.py", p).group(1)) for p in glob.glob(os.path.join(HERE, "zh_unit*.py")))
ap = argparse.ArgumentParser()
ap.add_argument("--units", nargs="*", type=int, default=found)
ap.add_argument("--force", action="store_true")
ap.add_argument("--quiet", action="store_true")
args = ap.parse_args()

units = [importlib.import_module(f"zh_unit{n}").UNIT for n in args.units]
app, meta = Z.build(units)
try:
    Z.convert_app(app)
except Z.PinyinError as e:
    print("PINYIN ERROR:", e)
    sys.exit(1)

deck = Z.load_deck_ranks(DECK) if hasattr(Z, "load_deck_ranks") else {}
errors, warns, info = Z.check_zh(app, meta, deck)
errors += Z.check_questions(meta, app)

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
print(f"\n{lessons} lessons, {exercises} exercises")

if errors and not args.force:
    print("not written (fix the errors, or use --force)")
    sys.exit(1)


def scrub(o):
    if isinstance(o, dict):
        return {k: scrub(v) for k, v in o.items() if not k.startswith("_")}
    if isinstance(o, list):
        return [scrub(x) for x in o]
    return o


Z.write_json(scrub(app), OUT)
print("wrote", OUT)
