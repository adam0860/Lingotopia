"""Unit 108: Lesson 30 (Unit 5 review), the glossary: the entries of the book's Unit 5 glossary, in the book's order (pinyin order),
with the traditional form where it differs and the book's lesson reference in brackets (29.1 = Lesson 29, Presentation 1).
Data comes from zh_glossary5_data.py (read from the book's glossary table by column position). Suffix entries the book prints with a
hyphen (-不起, -代, -化, -热) are listed without the hyphen, with a note; two headwords the book prints in quotation marks are listed
without them, with a note; 双11 is written 双十一. The book prints the pinyin of the entry 国外 as zhǔyào (a copy slip from the line above);
the correct reading guówài is used here."""
from zh_auto import *
from zh_glossary5_data import GLOSSARY5

SIZE = 24
chunks = [GLOSSARY5[i:i + SIZE] for i in range(0, len(GLOSSARY5), SIZE)]
LESSONS = []
for n, c in enumerate(chunks, 1):
    first, last = c[0][0], c[-1][0]
    LESSONS.append(vocab_lesson(f"Unit 5 glossary {n} of {len(chunks)} ({first} … {last})", f"{first} … {last}",
                                f"Glossary, part {n} of {len(chunks)}",
                                "From the Unit 5 glossary at the back of the review book, in the book’s order (pinyin order). Each line gives the word, its pinyin, the part of speech, the meaning, and the traditional form where it differs. The number in brackets is the book’s lesson reference (29.1 = Lesson 29, Presentation 1).", c))

UNIT = unit("第三十课 Unit 5 review: glossary", LESSONS)
