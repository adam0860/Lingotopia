"""Builds assets/writing/ja_readings.json: on-yomi, kun-yomi and English meanings of every kanji in
ja_strokes.json, taken from KANJIDIC2 as bundled in the jamdict-data SQLite file (pip install jamdict-data).

Kun readings keep the dot before the okurigana (い.きる); readings with a hyphen (suffix or prefix
forms such as -り) and duplicates that sound the same are dropped; at most 4 kun and 3 on readings.

Usage:  python3 tools/build_writing_readings.py
"""
import collections
import json
import os
import sqlite3

import jamdict_data

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STROKES = os.path.join(ROOT, "assets", "writing", "ja_strokes.json")
OUT = os.path.join(ROOT, "assets", "writing", "ja_readings.json")


def clean(readings, limit):
    seen, out = set(), []
    for r in readings:
        if "-" in r:
            continue
        plain = r.replace(".", "")
        if plain in seen:
            continue
        seen.add(plain)
        out.append(r)
    return out[:limit]


def main():
    chars = json.load(open(STROKES, encoding="utf-8"))["chars"]
    kanji = [c for c in chars if not ("ぁ" <= c <= "ヺ")]
    con = sqlite3.connect("file:%s?mode=ro" % jamdict_data.JAMDICT_DB_PATH, uri=True)
    cur = con.cursor()
    cur.execute("create temp table want(text text primary key)")
    cur.executemany("insert or ignore into want values (?)", ((c,) for c in kanji))
    on, kun, mean = (collections.defaultdict(list) for _ in range(3))
    for lit, ty, val in cur.execute(
            "select ch.literal, r.r_type, r.value from character ch join want w on w.text=ch.literal "
            "join rm_group g on g.cid=ch.ID join reading r on r.gid=g.ID "
            "where r.r_type in ('ja_on','ja_kun') order by ch.literal, r.rowid"):
        (on if ty == "ja_on" else kun)[lit].append(val)
    for lit, val in cur.execute(
            "select ch.literal, m.value from character ch join want w on w.text=ch.literal "
            "join rm_group g on g.cid=ch.ID join meaning m on m.gid=g.ID "
            "where m.m_lang='en' order by ch.literal, m.rowid"):
        mean[lit].append(val)
    out = {}
    for c in kanji:
        e = {}
        o, k = clean(on[c], 3), clean(kun[c], 4)
        if o:
            e["on"] = o
        if k:
            e["kun"] = k
        if (o or k) and mean[c]:
            e["m"] = mean[c][:3]
        if o or k:
            out[c] = e
    json.dump({"v": 1, "src": "KANJIDIC2 (EDRDG, CC BY-SA 4.0) via jamdict-data", "kanji": out},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print("wrote %s: %d of %d kanji have readings" % (OUT, len(out), len(kanji)))


if __name__ == "__main__":
    main()
