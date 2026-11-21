"""Unit 18: Lesson 6 (Unit 1 review), the glossary: all 236 entries of the book's Unit 1 glossary, in the book's order,
with the traditional form where it differs. Data comes from zh_glossary_data.py (generated from the book's glossary)."""
import re

from zh_auto import *
from zh_glossary_data import GLOSSARY

# a few of the book's glosses are cut short; these say what the word really means (the book's gloss is kept otherwise)
GLOSS_FIX = {"大学生": "college student", "多": "how (before an adjective)", "对了": "right, oh yes", "多少": "how many, how much",
             "几": "how many (a few)", "千": "thousand", "有意思": "interesting, funny", "平均": "on average", "巧": "coincidental, lucky",
             "过": "observe (a holiday), spend", "号": "date, number", "请": "please, to invite", "还": "also, in addition", "刘": "a Chinese surname"}
STOP = {"a", "an", "the", "of", "for", "to", "be", "in", "or", "and", "from", "at", "with"}


def words(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP}


rows = []
for hz, py, pos, en, trad in GLOSSARY:
    en = GLOSS_FIX.get(hz, en)
    pos = pos.replace(" ", "") if pos in ("v. o.", "v. c") else pos
    shown = f"{pos} {en}" + (f" (trad. {trad})" if trad else "")
    rows.append((hz, py, en, shown))

_count = {}
for r in rows:
    _count[r[2]] = _count.get(r[2], 0) + 1


def pick(i, chunk, k=3, step=5):
    """k distractor meanings from the same lesson that share no word with the right answer or each other."""
    hz, py, en, _ = chunk[i]
    out, used = [], words(en)
    n = len(chunk)
    for s in range(1, n):
        c = chunk[(i + s * step) % n]
        if c[2] == en or (words(c[2]) & used) or c[0] in hz or hz in c[0]:
            continue
        out.append(c)
        used |= words(c[2])
        if len(out) == k:
            break
    assert len(out) == k, (hz, en)
    return out


def glossary_lesson(num, total, chunk):
    first, last = chunk[0][0], chunk[-1][0]
    exs = []
    for i, (hz, py, en, shown) in enumerate(chunk):
        wrong = pick(i, chunk)
        exs.append(mean(hz, py, en, [w[2] for w in wrong]))
        if _count[en] == 1 and en not in ("a Chinese surname",):
            exs.append(M(f"Which word means “{en}”?", hz, [w[0] for w in wrong], f"{hz} ([[{py}]]) means “{en}”."))
    return lesson(f"Unit 1 glossary {num} of {total} ({first} … {last})", f"{first} … {last}", requires=[],
                  cards=[card(f"Glossary, part {num} of {total}",
                              "From the Unit 1 glossary at the back of the review book, in the book’s order (pinyin order). Each line gives the word, its pinyin, the part of speech, the meaning, and the traditional form where it differs.",
                              tables=[wtable([(hz, py, shown) for hz, py, en, shown in chunk])])],
                  exercises=exs)


SIZE = 24
chunks = [rows[i:i + SIZE] for i in range(0, len(rows), SIZE)]
LESSONS = [glossary_lesson(n + 1, len(chunks), c) for n, c in enumerate(chunks)]

UNIT = unit("第六课 Unit 1 review: glossary", LESSONS)
