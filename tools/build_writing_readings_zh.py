"""Builds assets/writing/zh_readings.json: tone-marked pinyin and short English meanings of every hanzi
in zh_strokes.json.

Pinyin comes from pypinyin (heteronym lists, most common reading first) and is kept only when CC-CEDICT
(bundled with the hanzipy pip package) also lists it; meanings are the first glosses of CC-CEDICT's entry
for the main reading. Up to 3 readings and 3 meanings per character.

Usage:  pip install pypinyin hanzipy && python3 tools/build_writing_readings_zh.py
"""
import json
import logging
import os
import re

from hanzipy.dictionary import HanziDictionary
from pypinyin import Style, pinyin
from pypinyin.contrib.tone_convert import to_tone

logging.disable(logging.CRITICAL)
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STROKES = os.path.join(ROOT, "assets", "writing", "zh_strokes.json")
OUT = os.path.join(ROOT, "assets", "writing", "zh_readings.json")

SKIP = re.compile(r"^(CL:|see |variant of|old variant|erhua variant|abbr\. for|used in|also pr\.|surname|"
                  r"Kangxi radical|archaic|\(archaic\)|\(dialect\)|Taiwan pr\.|same as|\(Cantonese)", re.I)


def glosses(defn):
    out = []
    for g in defn.split("/"):
        g = re.sub(r"\s*\([^)]*\)\s*", " ", g).strip()  # drop (bracketed) asides
        if not g or SKIP.match(g) or len(g) > 28:
            continue
        if g.lower() not in [x.lower() for x in out]:
            out.append(g)
    return out[:3]


def main():
    chars = list(json.load(open(STROKES, encoding="utf-8"))["chars"])
    dic = HanziDictionary()
    out = {}
    for ch in chars:
        entries = [e for e in (dic.definition_lookup(ch) or []) if e["simplified"] == ch or e["traditional"] == ch]
        cedict = {}
        for e in entries:
            try:
                p = to_tone(e["pinyin"].replace("u:", "ü").replace(" ", ""))
            except Exception:
                continue
            cedict.setdefault(p, []).append(e["definition"])
        cand = [p for x in pinyin(ch, style=Style.TONE, heteronym=True) for p in x]
        reads = [p for p in cand if p in cedict] or [p for p in cand if p] or list(cedict)
        reads = list(dict.fromkeys(reads))[:3]
        e = {"r": reads}
        if reads:
            gl = []
            for d in cedict.get(reads[0], []):
                gl += glosses(d)
            if not gl:
                for d in sum(cedict.values(), []):
                    gl += glosses(d)
            gl = list(dict.fromkeys(gl))[:3]
            if gl:
                e["m"] = gl
        out[ch] = e
    json.dump({"v": 1, "src": "pypinyin (MIT) and CC-CEDICT (CC BY-SA 4.0, MDBG) via hanzipy", "chars": out},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    print(len(out), "chars;", sum(1 for v in out.values() if not v["r"]), "without a reading;",
          sum(1 for v in out.values() if "m" not in v), "without meaning;", os.path.getsize(OUT) // 1024, "KB")


if __name__ == "__main__":
    main()
