"""Collect word -> English pairs from the lessons' vocabulary tables.

The deck's glosses come from a dictionary and are often a rare sense; the
lesson tables were written for learners. Run by ar_lexicon on demand and cached.
Only single-word Arabic cells are used. Writes nothing itself.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'lessons'))
import arabic_text as AT  # noqa: E402

LESSONS = Path(__file__).resolve().parents[2] / 'assets' / 'lessons' / 'ar_lessons.json'


def _clean_en(s):
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\s*\(.*?\)\s*', ' ', s).strip()
    return s


def harvest():
    d = json.load(open(LESSONS, encoding='utf-8'))
    out = {}
    for u in d['units']:
        for l in u['lessons']:
            for e in l['explanations']:
                for t in e['tables']:
                    h = [x.lower() for x in t['headers']]
                    if 'english' not in h:
                        continue
                    ei = h.index('english')
                    ai = next((i for i, x in enumerate(h) if x in ('arabic', 'verb', 'word', 'masculine', 'singular', 'adjective', 'man')), None)
                    if ai is None or ai == ei:
                        continue
                    for row in t['rows']:
                        if len(row) <= max(ei, ai):
                            continue
                        ar, en = row[ai], _clean_en(row[ei])
                        toks = AT.tokens(ar)
                        if len(toks) != 1 or not en or len(en) > 40:
                            continue
                        out.setdefault(AT.bare(toks[0]), en)
    return out


if __name__ == '__main__':
    g = harvest()
    print(len(g))
    for k in list(g)[:40]:
        print(k, '|', g[k])
