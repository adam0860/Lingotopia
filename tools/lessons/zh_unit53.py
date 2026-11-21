"""Unit 53: Lesson 18 (Unit 3 review), the glossary: all 346 entries of the book's Unit 3 glossary, in the book's order (pinyin
order), with the traditional form where it differs and the book's lesson reference in brackets (13.1 = Lesson 13, Presentation 1).
Data comes from zh_glossary3_data.py (read from the book's glossary table by column position)."""
from zh_auto import *
from zh_glossary3_data import GLOSSARY3

SIZE = 24
chunks = [GLOSSARY3[i:i + SIZE] for i in range(0, len(GLOSSARY3), SIZE)]
LESSONS = []
for n, c in enumerate(chunks, 1):
    first, last = c[0][0], c[-1][0]
    LESSONS.append(vocab_lesson(f"Unit 3 glossary {n} of {len(chunks)} ({first} … {last})", f"{first} … {last}",
                                f"Glossary, part {n} of {len(chunks)}",
                                "From the Unit 3 glossary at the back of the review book, in the book’s order (pinyin order). Each line gives the word, its pinyin, the part of speech, the meaning, and the traditional form where it differs. The number in brackets is the book’s lesson reference (13.1 = Lesson 13, Presentation 1).", c))

UNIT = unit("第十八课 Unit 3 review: glossary", LESSONS)
