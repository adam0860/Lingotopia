#!/usr/bin/env python3
"""
Compile the Korean lessons (tools/lessons/ko_unit*.py) into assets/lessons/ko_lessons.json,
running every automatic check first.

    python3 tools/lessons/build_ko_lessons.py            # build + check + write
    python3 tools/lessons/build_ko_lessons.py --units 1  # only some units (ids then start at 1 again: for testing)
    python3 tools/lessons/build_ko_lessons.py --force    # write despite errors
    python3 tools/lessons/build_ko_lessons.py --selftest # only the engine's own tests (no lessons)

Each ko_unitN.py exports UNIT = unit("...", [lesson(...), ...]). Unit files are picked up automatically
in numeric order; lesson ids (ko_01, ko_02 ...) follow that order, so ADD new units at the end.
Romanization is generated, not typed: see dsl_ko.py and ko_rom.py.
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

import dsl_ko as Z  # noqa: E402
import ko_selftest  # noqa: E402

DECK = os.path.join(ROOT, "assets", "decks", "korean_core.json")
OUT = os.path.join(ROOT, "assets", "lessons", "ko_lessons.json")

found = sorted(int(re.search(r"ko_unit(\d+)\.py", p).group(1)) for p in glob.glob(os.path.join(HERE, "ko_unit*.py")))
ap = argparse.ArgumentParser()
ap.add_argument("--units", nargs="*", type=int, default=found)
ap.add_argument("--force", action="store_true")
ap.add_argument("--quiet", action="store_true")
ap.add_argument("--selftest", action="store_true")
args = ap.parse_args()

bad = ko_selftest.run()
print(f"engine self-test: {ko_selftest.COUNT} cases, {len(bad)} wrong")
for b in bad:
    print("  ", b)
if bad:
    sys.exit(1)
if args.selftest:
    sys.exit(0)

units = [importlib.import_module(f"ko_unit{n}").UNIT for n in args.units]
app, meta = Z.build(units)
Z.convert_app(app)

deck = Z.load_deck_readings(DECK)
errors, warns, info = Z.check_ko(app, meta, deck)

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
