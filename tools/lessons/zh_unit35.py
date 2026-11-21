"""Unit 35: Lesson 12 (Unit 2 review), the glossary: all 353 entries of the book's Unit 2 glossary, in the book's order,
with the traditional form where it differs. Data comes from zh_glossary2_data.py (parsed from the book's glossary)."""
from zh_auto import *
from zh_glossary2_data import GLOSSARY2

SIZE = 24
chunks = [GLOSSARY2[i:i + SIZE] for i in range(0, len(GLOSSARY2), SIZE)]
LESSONS = []
for n, c in enumerate(chunks, 1):
    first, last = c[0][0], c[-1][0]
    LESSONS.append(vocab_lesson(f"Unit 2 glossary {n} of {len(chunks)} ({first} … {last})", f"{first} … {last}",
                                f"Glossary, part {n} of {len(chunks)}",
                                "From the Unit 2 glossary at the back of the review book, in the book’s order (pinyin order). Each line gives the word, its pinyin, the part of speech, the meaning, and the traditional form where it differs.", c))

UNIT = unit("第十二课 Unit 2 review: glossary", LESSONS)
