"""Unit 75: Lesson 24 (Unit 4 review), the glossary: the entries of the book's Unit 4 glossary, in the book's order (pinyin order),
with the traditional form where it differs and the book's lesson reference in brackets (22.2 = Lesson 22, Presentation 2).
Data comes from zh_glossary4_data.py (read from the book's glossary table by column position). The book prints 嗯 (ok) as an
entry; it is left out here because the sound has no usable pinyin spelling in this app. Headwords printed with bracketed optional
characters (开(药), 泡(茶), 上(百), 加(上), 多亏(了)) are written out as whole words; (x)号, (x)号线 and (x)路 keep the headword
without the letter, with a note."""
from zh_auto import *
from zh_glossary4_data import GLOSSARY4

SIZE = 24
chunks = [GLOSSARY4[i:i + SIZE] for i in range(0, len(GLOSSARY4), SIZE)]
LESSONS = []
for n, c in enumerate(chunks, 1):
    first, last = c[0][0], c[-1][0]
    LESSONS.append(vocab_lesson(f"Unit 4 glossary {n} of {len(chunks)} ({first} … {last})", f"{first} … {last}",
                                f"Glossary, part {n} of {len(chunks)}",
                                "From the Unit 4 glossary at the back of the review book, in the book’s order (pinyin order). Each line gives the word, its pinyin, the part of speech, the meaning, and the traditional form where it differs. The number in brackets is the book’s lesson reference (22.2 = Lesson 22, Presentation 2).", c))

UNIT = unit("第二十四课 Unit 4 review: glossary", LESSONS)
