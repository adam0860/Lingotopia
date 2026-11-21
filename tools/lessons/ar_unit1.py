"""Unit 1: the Arabic script and its sounds (an original primer; the textbook assumes a
separate script course, so the book is not a source for these lessons)."""
from dsl_ar import *
from arabic_text import tl

NOJOIN = set("ادذرزو")
LT_HEAD = ["Letter", "Name", "Sound", "Shapes (read right to left)"]


def shapes(ch):
    if ch in NOJOIN:
        return f"{ch} ـ{ch}"
    return f"{ch}ـ ـ{ch}ـ ـ{ch}"


def lt(rows, note=None, title=None):
    """rows: (letter, name, sound)"""
    return table(LT_HEAD, [[c, n, s, shapes(c)] for c, n, s in rows], say=[1], note=note, title=title)


def rd(w, others, why=None):
    return M(f"How do you read {w}?", tl(w), [tl(o) for o in others],
             why or f"{w} is read “{tl(w)}”: sound out the letters from right to left.")


def mn(w, en, others, why=None):
    return M(f"What does {w} mean?", en, others, why or f"{w} ({tl(w)}) means “{en}”.")


def letter_q(prompt, ans, wrong, why):
    return M(prompt, ans, wrong, why)


# ---------------------------------------------------------------------------- 1
L1 = lesson(
    "Reading Arabic",
    "Direction, joined letters and vowel marks",
    requires=[],
    loose=True,
    cards=[
        card("Right to left",
             "Arabic is written and read from right to left, so the first letter of a word is on the right and "
             "a page starts at the right-hand edge. There are no capital letters. The alphabet has 28 letters, "
             "and all of them are consonants, though three also stand for long vowels.",
             examples=[
                 ex("كِتَاب", "a book"),
                 ex("بَيْت", "a house"),
                 ex("مَدْرَسَة", "a school"),
             ]),
        card("Letters join up",
             "Arabic is always joined up, in print as well as by hand. Most letters change shape a little "
             "depending on whether they join to the letter before, to the one after, or both. The table shows "
             "how separate letters become a word. Read each row from right to left.",
             tables=[table(["Separate letters", "Joined word"],
                           [["ك ت ا ب", "كِتَاب"], ["ب ي ت", "بَيْت"], ["ب ا ب", "بَاب"]],
                           say=[1], tlit=[1])]),
        card("The vowels are usually left out",
             "Arabic has three short vowels, and ordinary texts do not write them: a newspaper prints "
             "كتاب, not كِتَاب. Fluent readers fill them in from the word and the sentence. In this course every "
             "word is written with its vowel marks so you can learn how to say it, and a transliteration "
             "(the Latin-letter “Sound”) is shown beside it at first. Treat the transliteration as scaffolding "
             "and learn to read the Arabic itself.",
             examples=[ex("كِتَاب", "with vowel marks, as in this course"),
                       ex("كتاب", "without them, as in a newspaper", tlit=False)]),
    ],
    exercises=[
        M("Which way is Arabic written and read?", "From right to left", ["From left to right", "From top to bottom", "In both directions"],
          "Arabic runs right to left: the first letter of a word is on the right."),
        M("How many letters are in the Arabic alphabet?", "28", ["22", "26", "32"],
          "The alphabet has 28 letters."),
        M("What can you say about capital letters in Arabic?", "There are none", ["Names are capitalised", "Sentences start with one", "Only the first word of a title has one"],
          "Arabic has no capital letters at all."),
        M("In a newspaper, how are the short vowels usually shown?", "They are not written", ["Above every letter", "Only on the last letter", "With dots"],
          "Ordinary texts leave short vowels out; readers supply them from context."),
        F("Arabic is written from ___ to left.", "right", ["left", "top", "bottom"],
          "The first letter of an Arabic word is on the right."),
        M("The word بَيْت has how many letters?", "3", ["2", "4", "5"],
          "ب, ي and ت: three letters. The small marks above and below them are vowel signs (and a sukūn), not letters."),
        M("Why does this course print a transliteration beside Arabic words?", "To help you at first while you learn to read",
          ["Because Arabic is normally written in Latin letters", "Because Arabic has no vowels", "Because the transliteration is what the voice reads"],
          "It is scaffolding; the aim is to read the Arabic itself."),
        M("When letters join, in which order do you read a joined word?", "Right to left, letter by letter", ["Left to right", "Middle outwards", "Last letter first, then the rest left to right"],
          "Each letter is read in the order it is written, starting from the right."),
    ],
)

# ---------------------------------------------------------------------------- 2
L2 = lesson(
    "The first six letters",
    "ا ب ت ث ن ي",
    requires=[],
    loose=True,
    cards=[
        card("Five letters, one shape",
             "Four of these letters share one boat-like body and are told apart by their dots (the final ن also has a deeper, rounder bowl): "
             "ب has one dot below, ت two dots above, ث three dots above and ن one dot above. ي is nearly the "
             "same shape, with two dots below. The dots are part of the letter, so never leave them out.",
             tables=[lt([("ب", "بَاء", "b as in bed"), ("ت", "تَاء", "t as in ten"),
                         ("ث", "ثَاء", "th as in think"), ("ن", "نُون", "n as in net"),
                         ("ي", "يَاء", "y as in yes; also a long ee")],
                        note="Tap a name to hear it. Each letter has a form for the start of a word, the middle and the end.")]),
        card("Alif stands alone",
             "ا (alif) is a straight line with no dots. It is a long “aa” as in father, and it is one of six letters "
             "that never join to the letter after them, so the next letter starts a new shape.",
             tables=[lt([("ا", "أَلِف", "a long aa, as in father")])]),
    ],
    exercises=[
        letter_q("Which letter has one dot below?", "ب", ["ت", "ث", "ن"], "ب (bāʾ) has a single dot under its body."),
        letter_q("Which letter has three dots above?", "ث", ["ت", "ب", "ن"], "ث (thāʾ) has three dots above."),
        letter_q("Which letter has two dots above?", "ت", ["ث", "ب", "ن"], "ت (tāʾ) has two dots above."),
        letter_q("Which letter has one dot above?", "ن", ["ب", "ت", "ث"], "ن (nūn) has one dot above."),
        letter_q("Which letter makes the sound “th” as in think?", "ث", ["ت", "ن", "ب"], "ث is th, as in think."),
        letter_q("Which letter is called tāʾ?", "ت", ["ب", "ث", "ن"], "ت is tāʾ, the letter for t."),
        letter_q("Which letter does NOT join to the letter after it?", "ا", ["ب", "ت", "ن"], "Alif never joins forward."),
        letter_q("Which is the form of ب that starts a word?", "بـ", ["ـب", "ـبـ", "ـتـ"], "The starting form has its tail cut off and joins to the left."),
        letter_q("Which is the form of ن that ends a word?", "ـن", ["نـ", "ـنـ", "ـب"], "The ending form joins to the letter on its right and keeps its full curve."),
    ],
)

# ---------------------------------------------------------------------------- 3
L3 = lesson(
    "The short vowels",
    "فَتْحَة · كَسْرَة · ضَمَّة · سُكُون",
    requires=[],
    loose=True,
    drills=["بَتَ", "بَنَ"],
    cards=[
        card("Three vowels and a zero",
             "Short vowels are small marks written above or below a consonant. The fatḥa is a short stroke above "
             "(a), the kasra a short stroke below (i) and the ḍamma a little loop above (u). The sukūn, a small "
             "circle above, means the letter carries no vowel at all.",
             tables=[table(["Mark", "Name", "Sound", "On ب"],
                           [["ـَ", "فَتْحَة", "a, like the u in cut", "بَ"],
                            ["ـِ", "كَسْرَة", "i, like the i in sit", "بِ"],
                            ["ـُ", "ضَمَّة", "u, like the u in put", "بُ"],
                            ["ـْ", "سُكُون", "no vowel", "بْ"]],
                           say=[1, 3], tlit=[3])]),
        card("Syllables",
             "A consonant plus a short vowel makes a syllable, and a syllable can end in a consonant with a sukūn. "
             "Read the table across, then try the word below it.",
             tables=[table(["Letter", "With a, i, u"],
                           [["ب", "بَ · بِ · بُ"], ["ت", "تَ · تِ · تُ"], ["ث", "ثَ · ثِ · ثُ"], ["ن", "نَ · نِ · نُ"]],
                           say=[1], tlit=[1])],
             examples=[ex("بِنْت", "a girl; a daughter", "بِنْت")]),
    ],
    exercises=[
        M("Which mark is the fatḥa?", "ـَ", ["ـِ", "ـُ", "ـْ"], "The fatḥa is a short stroke above the letter."),
        M("Which mark is the kasra?", "ـِ", ["ـَ", "ـُ", "ـْ"], "The kasra is a short stroke below the letter."),
        M("Which mark is the sukūn (no vowel)?", "ـْ", ["ـَ", "ـِ", "ـُ"], "The sukūn is a small circle above the letter."),
        rd("بِ", ["بَ", "بُ", "بْ"]),
        rd("تُ", ["تَ", "تِ", "تْ"]),
        rd("ثَ", ["ثِ", "ثُ", "ثْ"]),
        M("Which syllable is read “ni”?", "نِ", ["نَ", "نُ", "نْ"], "A kasra gives the vowel i."),
        rd("بِنْت", ["بَنَت", "بُنْت", "بِنَت"], "ب has a kasra (bi), ن has a sukūn (n) and ت is bare at the end: bint."),
        M("In بِنْت, what sits on the letter ن?", "a sukūn", ["a fatḥa", "a kasra", "a ḍamma"],
          "The small circle over ن means it has no vowel, so it closes the syllable: bint is a single syllable."),
    ],
)

# ---------------------------------------------------------------------------- 4
L4 = lesson(
    "Long vowels and و",
    "ā ī ū, and the glides ay and aw",
    requires=[],
    loose=True,
    drills=["بَا", "بُو"],
    cards=[
        card("A vowel plus a letter makes it long",
             "Three letters double as long vowels. Alif after a fatḥa gives ā, yāʾ after a kasra gives ī and "
             "wāw after a ḍamma gives ū. The new letter و (wāw) is also a consonant w, as in water, and like alif "
             "it never joins to the letter after it.",
             tables=[table(["Long vowel", "Spelled", "Example"],
                           [["ā", "فَتْحَة + ا", "بَا"], ["ī", "كَسْرَة + ي", "بِي"], ["ū", "ضَمَّة + و", "بُو"]],
                           say=[1, 2], tlit=[2]),
                     lt([("و", "وَاو", "w as in water; also a long oo")])]),
        card("Glides: ay and aw",
             "A fatḥa followed by ي with a sukūn gives the glide ay, as in the English word eye said as one sound. "
             "A fatḥa followed by و with a sukūn gives aw, as in cow.",
             examples=[ex("بَيْت", "a house", "يْ"), ex("ثَوْب", "a garment; a dress", "وْ"),
                       ex("بَاب", "a door", "ا"), ex("تِين", "figs", "ي")]),
        card("The word “and”",
             "وَ means “and”. It is written as one letter, attached to the word after it with no space.",
             examples=[ex("بَاب وَبَيْت", "a door and a house", "وَبَيْت")]),
    ],
    exercises=[
        rd("بَاب", ["بُوب", "بِيب", "بَيْب"]),
        rd("تِين", ["تَيْن", "تُون", "تَان"]),
        rd("ثَوْب", ["ثُوب", "ثَيْب", "ثَاب"]),
        rd("بَيْت", ["بَاتْ", "بِيت", "بُوت"]),
        mn("بَاب", "a door", ["a house", "a garment", "figs"]),
        mn("بَيْت", "a house", ["a door", "figs", "a garment"]),
        mn("تِين", "figs", ["a door", "a house", "a garment"]),
        M("Which letter, after a kasra, makes a long ī?", "ي", ["ا", "و", "ن"], "Yāʾ after a kasra gives ī."),
        M("Which letter, after a ḍamma, makes a long ū?", "و", ["ا", "ي", "ت"], "Wāw after a ḍamma gives ū."),
        M("What does وَ mean?", "and", ["or", "in", "with"], "وَ is the word “and”, written attached to the next word."),
    ],
)

# ---------------------------------------------------------------------------- 5
L5 = lesson(
    "ج ح خ",
    "Three letters from one shape",
    requires=[],
    loose=True,
    cards=[
        card("One body, three sounds",
             "These three share a hooked body and are told apart by one dot. ج has a dot inside, ح has none, "
             "and خ has a dot above.",
             tables=[lt([("ج", "جِيم", "j as in jam"),
                         ("ح", "حَاء", "ḥ: a breathy h from deep in the throat, like fogging a mirror"),
                         ("خ", "خَاء", "kh: like ch in Scottish loch")])]),
        card("Your first words",
             "You can now read words that use all the letters so far. Sound each one out, then tap it.",
             tables=[table(["Word", "English"],
                           [["جَيْب", "pocket"], ["نَحْنُ", "we"], ["تَحْت", "under; below"],
                            ["جَنُوب", "south"], ["حَبِيب", "dear; beloved"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        letter_q("Which letter has a dot inside its body?", "ج", ["ح", "خ", "ن"], "ج has a dot inside (below the line); ح has none and خ has one above."),
        letter_q("Which of these has NO dot?", "ح", ["ج", "خ", "ب"], "ح is the plain hooked letter."),
        letter_q("Which letter sounds like ch in Scottish loch?", "خ", ["ج", "ح", "ث"], "خ is kh."),
        letter_q("Which letter is a breathy h from the throat?", "ح", ["خ", "ج", "ن"], "ح (ḥ) is a strong, breathy h."),
        rd("نَحْنُ", ["نَجْن", "نَخْن", "بَحْن"]),
        rd("جَيْب", ["حَيْب", "خَيْب", "جَاب"]),
        mn("تَحْت", "under; below", ["we", "south", "pocket"]),
        mn("نَحْنُ", "we", ["under; below", "south", "pocket"]),
        mn("جَنُوب", "south", ["pocket", "we", "dear; beloved"]),
        mn("حَبِيب", "dear; beloved", ["south", "pocket", "under; below"]),
    ],
)

# ---------------------------------------------------------------------------- 6
L6 = lesson(
    "د ذ ر ز",
    "Four letters that never join forward",
    requires=[],
    loose=True,
    cards=[
        card("Short letters",
             "These four are small and, like alif and wāw, never join to the letter after them. A word simply "
             "leaves a small gap after them.",
             tables=[lt([("د", "دَال", "d as in dog"), ("ذ", "ذَال", "dh as in this"),
                         ("ر", "رَاء", "r, tapped or rolled, as in Spanish pero"), ("ز", "زَاي", "z as in zoo")],
                        note="ذ is د with a dot, and ز is ر with a dot.")]),
        card("Words you can read now",
             "With these letters you can read some of the most useful words in Arabic.",
             tables=[table(["Word", "English"],
                           [["جَدِيد", "new"], ["وَاحِد", "one"], ["خَيْر", "good; well-being"],
                            ["بَحْر", "sea"], ["زَوْج", "husband; spouse"], ["دَار", "home; house"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        letter_q("Which letter is d as in dog?", "د", ["ذ", "ر", "ز"], "د (dāl) is d."),
        letter_q("Which letter is dh as in this?", "ذ", ["د", "ر", "ز"], "ذ (dhāl) is د with a dot above."),
        letter_q("Which letter has a dot above and is read z?", "ز", ["ر", "د", "ذ"], "ز (zāy) is ر with a dot."),
        letter_q("Which letter is the rolled r?", "ر", ["ز", "د", "ذ"], "ر (rāʾ) is r."),
        M("What is special about د ذ ر ز و ا?", "They do not join to the letter after them",
          ["They have no dots", "They are always vowels", "They only appear at the end of words"],
          "These six letters join only to the letter before them."),
        rd("جَدِيد", ["جَدَد", "جُدُود", "جِيدِيد"]),
        rd("بَحْر", ["بَهْر", "بَخْر", "بَحْز"]),
        mn("جَدِيد", "new", ["one", "sea", "good; well-being"]),
        mn("وَاحِد", "one", ["new", "sea", "husband; spouse"]),
        mn("بَحْر", "sea", ["new", "one", "home; house"]),
    ],
)

# ---------------------------------------------------------------------------- 7
L7 = lesson(
    "س ش ص ض",
    "The “teeth” letters and two heavy ones",
    requires=[],
    loose=True,
    cards=[
        card("Plain and heavy",
             "س and ش have three small teeth; ص and ض have a closed loop. ص and ض are “emphatic” letters: "
             "you say them with the tongue pulled back and the mouth hollow, which gives the neighbouring vowels a darker, "
             "heavier sound. English has nothing like it, so listen and copy.",
             tables=[lt([("س", "سِين", "s as in sun"), ("ش", "شِين", "sh as in ship"),
                         ("ص", "صَاد", "ṣ: a heavy s, with the mouth hollow"),
                         ("ض", "ضَاد", "ḍ: a heavy d, with the mouth hollow")],
                        note="ش is س with three dots; ض is ص with one dot.")]),
        card("More words",
             "Read these aloud. The first one is the first word of “good morning”, صَبَاح الْخَيْر.",
             tables=[table(["Word", "English"],
                           [["صَبَاح", "morning"], ["شَخْص", "person"], ["صَحِيح", "correct; true"],
                            ["سَبَب", "reason"], ["وَاضِح", "clear"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        letter_q("Which letter is sh as in ship?", "ش", ["س", "ص", "ض"], "ش (shīn) has three dots above."),
        letter_q("Which letter is a plain s?", "س", ["ش", "ص", "ض"], "س (sīn) is the plain s."),
        letter_q("Which letter is the heavy s?", "ص", ["س", "ش", "ض"], "ص (ṣād) is the emphatic s."),
        letter_q("Which letter is the heavy d, with a dot above?", "ض", ["ص", "د", "ذ"], "ض (ḍād) is ص with a dot."),
        letter_q("Which letter has three dots above its teeth?", "ش", ["س", "ث", "ص"], "ش has three dots above; س has none."),
        rd("صَبَاح", ["سَبَاح", "صَبَاخ", "ضَبَاح"]),
        rd("شَخْص", ["سَخْص", "شَحْص", "شَخْس"]),
        mn("صَبَاح", "morning", ["person", "reason", "clear"]),
        mn("شَخْص", "person", ["morning", "reason", "correct; true"]),
        mn("سَبَب", "reason", ["person", "clear", "morning"]),
    ],
)

# ---------------------------------------------------------------------------- 8
L8 = lesson(
    "ط ظ ع غ",
    "Two heavy letters and two throat letters",
    requires=[],
    loose=True,
    cards=[
        card("Heavy ṭ and ẓ",
             "ط and ظ are the emphatic partners of ت and ذ: the same sounds, said with the tongue pulled back and the "
             "mouth hollow. ظ is ط with a dot above.",
             tables=[lt([("ط", "طَاء", "ṭ: a heavy t"), ("ظ", "ظَاء", "ẓ: a heavy dh, as in this")])]),
        card("Two sounds with no English letter",
             "ع (ʿayn) is made by squeezing the throat while voicing; it is the sound many learners find hardest, so "
             "listen to it often. غ (ghayn) is ع with a dot above and sounds like a gargled French r. Both have four "
             "shapes, and the middle shape of ع looks like a small triangle.",
             tables=[lt([("ع", "عَيْن", "ʿ: a voiced squeeze deep in the throat"),
                         ("غ", "غَيْن", "gh: like a gargled French r")])]),
        card("More words",
             "Some useful words made of the letters you know.",
             tables=[table(["Word", "English"],
                           [["طَبِيب", "doctor"], ["عَيْن", "eye"], ["عِنْد", "at; with"],
                            ["غَرِيب", "strange; foreign"], ["عَدَد", "number"], ["بَعِيد", "far"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        letter_q("Which letter is the heavy t?", "ط", ["ت", "ظ", "ع"], "ط (ṭāʾ) is the emphatic t."),
        letter_q("Which letter is the heavy dh, with a dot above?", "ظ", ["ط", "ذ", "غ"], "ظ (ẓāʾ) is ط with a dot."),
        letter_q("Which letter is the throat squeeze ʿ?", "ع", ["غ", "ح", "ه"], "ع (ʿayn) has no dot; غ (ghayn) has one."),
        letter_q("Which letter sounds like a gargled French r?", "غ", ["ع", "خ", "ق"], "غ (ghayn) is gh."),
        rd("طَبِيب", ["تَبِيب", "طَبِيت", "طَبَب"]),
        rd("عَيْن", ["غَيْن", "حَيْن", "عَان"]),
        mn("طَبِيب", "doctor", ["eye", "number", "far"]),
        mn("عَيْن", "eye", ["doctor", "at; with", "strange; foreign"]),
        mn("عِنْد", "at; with", ["eye", "far", "number"]),
        mn("بَعِيد", "far", ["number", "doctor", "eye"]),
    ],
)

# ---------------------------------------------------------------------------- 9
L9 = lesson(
    "ف ق ك ل",
    "Four letters, and the lām-alif",
    requires=[],
    loose=True,
    cards=[
        card("Four more",
             "ف has one dot above and ق two, both with a round head. ك, in its separate and final forms, has a small zigzag above a flat base "
             "and ل is a tall stroke with a hook. ق (qāf) is a k said far back in the throat.",
             tables=[lt([("ف", "فَاء", "f as in fan"), ("ق", "قَاف", "q: a deep k from the back of the throat"),
                         ("ك", "كَاف", "k as in kit"), ("ل", "لَام", "l as in lamp")])]),
        card("Lām plus alif",
             "When ل is followed by ا the two letters fuse into one shape, لا, which is read lā. It is not a new "
             "letter, just how those two always look together. It is also the word لَا: no, not.",
             examples=[ex("لَا", "no; not", "لَا")]),
        card("Words with the new letters",
             "Read these aloud, then tap them.",
             tables=[table(["Word", "English"],
                           [["كِتَاب", "book"], ["كَبِير", "big; old"], ["قَرِيب", "near"],
                            ["فِي", "in"], ["لَيْل", "night"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        letter_q("Which letter has two dots above and a round head?", "ق", ["ف", "ت", "ن"], "ق (qāf) has two dots; ف has one."),
        letter_q("Which letter is a k said far back in the throat?", "ق", ["ك", "ف", "غ"], "ق (qāf) is q."),
        letter_q("Which letter is the plain k, with a zigzag?", "ك", ["ق", "ل", "ف"], "ك (kāf) is k."),
        letter_q("Which letter is l?", "ل", ["ك", "ا", "ن"], "ل (lām) is l."),
        M("What do ل and ا make when they meet?", "The single shape لا", ["A new letter, ك", "The shape لل", "Nothing: they stay apart"],
          "Lām and alif always fuse into لا."),
        rd("كِتَاب", ["قِتَاب", "كِتَات", "كَتَب"]),
        rd("قَرِيب", ["كَرِيب", "قَرِين", "غَرِيب"]),
        mn("كِتَاب", "book", ["night", "in", "big; old"]),
        mn("كَبِير", "big; old", ["near", "night", "book"]),
        mn("قَرِيب", "near", ["far", "big; old", "night"]),
        mn("لَيْل", "night", ["book", "near", "in"]),
    ],
)

# ---------------------------------------------------------------------------- 10
L10 = lesson(
    "م ه and the whole alphabet",
    "The last letters, and the alphabet in order",
    requires=[],
    loose=True,
    cards=[
        card("The last two",
             "م is a small round head on a line and ه has four quite different shapes, so look at it carefully. "
             "ه is a light h as in hat, breathed out.",
             tables=[lt([("م", "مِيم", "m as in man"), ("ه", "هَاء", "h as in hat, but lighter")])]),
        card("The alphabet in order",
             "This is the traditional order. Dictionaries and word lists follow it. You now know every letter.",
             tables=[table(["Letters (right to left)", "Names"],
                           [["ا ب ت ث", "أَلِف · بَاء · تَاء · ثَاء"],
                            ["ج ح خ د", "جِيم · حَاء · خَاء · دَال"],
                            ["ذ ر ز س", "ذَال · رَاء · زَاي · سِين"],
                            ["ش ص ض ط", "شِين · صَاد · ضَاد · طَاء"],
                            ["ظ ع غ ف", "ظَاء · عَيْن · غَيْن · فَاء"],
                            ["ق ك ل م", "قَاف · كَاف · لَام · مِيم"],
                            ["ن ه و ي", "نُون · هَاء · وَاو · يَاء"]],
                           say=[1])]),
        card("Small, useful words",
             "These very common words are all built from letters you have met.",
             tables=[table(["Word", "English"],
                           [["هُوَ", "he"], ["هِيَ", "she"], ["مِنْ", "from"], ["مَعَ", "with"],
                            ["هُنَا", "here"], ["قَلَم", "pen"], ["مَكْتَب", "office; desk"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        letter_q("Which letter is m?", "م", ["ن", "ه", "ف"], "م (mīm) is m."),
        letter_q("Which letter is a light h as in hat?", "ه", ["ح", "خ", "م"], "ه (hāʾ) is the light h; ح is the heavy throat h."),
        M("Which letter comes right after ا in the alphabet?", "ب", ["ت", "ن", "ج"], "The order starts ا ب ت ث."),
        M("Which letter comes last in the alphabet?", "ي", ["و", "ه", "ن"], "The alphabet ends ... ن ه و ي."),
        M("Which letter comes right before م in the alphabet?", "ل", ["ك", "ن", "ق"], "... ق ك ل م ن ..."),
        rd("هُوَ", ["هُوُ", "هَوَ", "هِيَ"]),
        rd("مِنْ", ["مَنْ", "مُنْ", "مِيْن"]),
        mn("هِيَ", "she", ["he", "here", "from"]),
        mn("هُنَا", "here", ["she", "from", "with"]),
        mn("قَلَم", "pen", ["office; desk", "book", "eye"]),
        mn("مَكْتَب", "office; desk", ["pen", "book", "night"]),
    ],
)

# ---------------------------------------------------------------------------- 11
L11 = lesson(
    "Shadda and tanwīn",
    "Doubled letters and the -an ending",
    requires=[],
    loose=True,
    cards=[
        card("Shadda: say it twice",
             "The shadda ـّ, a small w-shaped mark, doubles a consonant: the letter is held a little longer, as in "
             "the English “book-case” or the Italian “nonno”. The vowel goes on the shadda, above or below it.",
             examples=[ex("مُدَرِّس", "a teacher", "رِّ"), ex("عَرَبِيّ", "Arab; Arabic", "يّ"),
                       ex("جَيِّد", "good", "يِّ")]),
        card("Tanwīn: the -an ending",
             "Tanwīn is a doubled vowel mark at the end of a word that adds an n sound. The most common one, the "
             "double fatḥa ـً, is usually written with an extra alif (but not after ة or ـاء) and forms many adverbs and greetings.",
             tables=[table(["Word", "English"],
                           [["شُكْرًا", "thank you"], ["عَفْوًا", "you are welcome; pardon"],
                            ["مَرْحَبًا", "hello"], ["جِدًّا", "very"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        M("What does the shadda do?", "It doubles the consonant", ["It makes a vowel long", "It removes the vowel", "It adds an n"],
          "The shadda holds the letter for twice as long."),
        M("What does a tanwīn on the end of a word add?", "an n sound after the vowel", ["a long vowel", "a doubled consonant", "nothing: it is silent"],
          "ـً is read -an, ـٌ is read -un and ـٍ is read -in."),
        rd("مُدَرِّس", ["مُدَرِس", "مُدَرَّس", "مُذَرِّس"]),
        rd("عَرَبِيّ", ["عَرَبِي", "غَرَبِيّ", "عَرَبَيّ"]),
        rd("شُكْرًا", ["شُكْرٌ", "شَكْرًا", "سُكْرًا"]),
        mn("مَرْحَبًا", "hello", ["thank you", "very", "pardon"]),
        mn("شُكْرًا", "thank you", ["hello", "very", "a teacher"]),
        mn("جِدًّا", "very", ["thank you", "good", "hello"]),
        mn("مُدَرِّس", "a teacher", ["good", "Arab; Arabic", "very"]),
        M("Which word carries a shadda?", "جِدًّا", ["شُكْرًا", "مَرْحَبًا", "عَفْوًا"],
          "The د in جِدًّا is doubled (jid-dan); the others have only a tanwīn."),
    ],
)

# ---------------------------------------------------------------------------- 12
L12 = lesson(
    "Hamza, tāʾ marbūṭa and alif maqṣūra",
    "Letters that look like other letters",
    requires=[],
    loose=True,
    cards=[
        card("Hamza ء",
             "The hamza is the catch in the throat in the middle of “uh-oh”. It is not one of the 28 letters, but "
             "it appears all the time. It sits on a “chair” that depends on the neighbouring vowels: on an alif "
             "(أ above, إ below), on a و (ؤ), on a ي without dots (ئ), or alone (ء). At the start of a word the chair "
             "is always an alif.",
             tables=[table(["Written", "Example", "English"],
                           [["أ", "أَنَا", "I"], ["إ", "إِلَى", "to"], ["ؤ", "سُؤَال", "a question"],
                            ["ئ", "سَائِل", "a liquid"], ["ء", "مَاء", "water"]],
                           say=[1], tlit=[1])]),
        card("Two endings",
             "ة (tāʾ marbūṭa) is a ه with two dots and marks most feminine words. At the end of a word it is read "
             "simply a, not t. ى (alif maqṣūra) looks like ي without dots but is read as a long ā.",
             tables=[table(["Word", "English"],
                           [["مَدْرَسَة", "school"], ["مَكْتَبَة", "library"], ["عَلَى", "on"],
                            ["مَتَى", "when"], ["سَيَّارَة", "car"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        M("What is the hamza?", "A catch in the throat, as in uh-oh", ["A long vowel", "A doubled letter", "The sound h"],
          "Hamza is a glottal stop."),
        M("On which letter does a hamza always sit at the start of a word?", "alif", ["wāw", "yāʾ", "none"], "At the start of a word the chair is an alif."),
        M("How is ة read at the end of a word?", "a", ["t", "h", "n"], "ة ends feminine words and is read a (it becomes t when more is added)."),
        M("How is ى at the end of a word read?", "a long ā", ["ī", "ū", "ay"], "Alif maqṣūra is a long ā written with the yāʾ shape and no dots."),
        rd("أَنَا", ["أَنُو", "إِنَا", "أُنَا"]),
        rd("مَدْرَسَة", ["مَدْرَسَت", "مَذْرَسَة", "مُدْرِسَة"]),
        rd("عَلَى", ["عَلِي", "عِلْم", "عُلَى"]),
        mn("مَاء", "water", ["school", "on", "library"]),
        mn("مَكْتَبَة", "library", ["school", "office; desk", "car"]),
        mn("مَتَى", "when", ["on", "to", "I"]),
    ],
)

# ---------------------------------------------------------------------------- 13
L13 = lesson(
    "The article ال",
    "Sun letters and moon letters",
    requires=[],
    loose=True,
    cards=[
        card("One word for “the”",
             "Arabic has one word for “the”: the prefix ال, written attached to the noun and the same for masculine, "
             "feminine, singular and plural. A noun without it is indefinite, so كِتَاب is “a book” and الْكِتَاب is "
             "“the book”.",
             examples=[ex("الْكِتَاب", "the book", "الْ"), ex("الْبَيْت", "the house", "الْ"),
                       ex("الْمَدْرَسَة", "the school", "الْ")]),
        card("Moon letters and sun letters",
             "The ل of ال is pronounced before 14 letters, called moon letters (الْقَمَر, al-qamar). Before the 14 "
             "sun letters it is not heard: it melts into the next letter, which is doubled and marked with a shadda "
             "(الشَّمْس, ash-shams, not al-shams). The spelling does not change; only the pronunciation and the marks do.",
             tables=[table(["Type", "Letters", "Example"],
                           [["moon", "ا ب ج ح خ ع غ ف ق ك م ه و ي", "الْقَمَر"],
                            ["sun", "ت ث د ذ ر ز س ش ص ض ط ظ ل ن", "الشَّمْس"]],
                           say=[2], tlit=[2])]),
        card("Practice with both kinds",
             "Sun letters: the shadda is your clue. Moon letters: the lām carries a sukūn.",
             tables=[table(["Moon", "English", "Sun", "English"],
                           [["الْبَاب", "the door", "الطَّبِيب", "the doctor"],
                            ["الْعَيْن", "the eye", "الرَّجُل", "the man"],
                            ["الْبَحْر", "the sea", "النَّوْم", "sleep"],
                            ["الْكَبِير", "the big one", "الدَّرْس", "the lesson"]],
                           say=[0, 2], tlit=[0, 2], gloss=False)]),
    ],
    exercises=[
        M("How many words for “the” does Arabic have?", "One: ال", ["Two: masculine and feminine", "Four, like Spanish", "None"],
          "ال is used for every noun."),
        M("Which is “the book”?", "الْكِتَاب", ["كِتَاب", "كِتَابُ الْ", "كِتَابَة"], "ال is attached to the front of the noun."),
        M("Which kind of letter is ك after ال?", "a moon letter", ["a sun letter", "a vowel", "a letter that cannot follow ال"],
          "ك is a moon letter: الْكِتَاب, with a sukūn on ل."),
        M("Which kind of letter is ش after ال?", "a sun letter", ["a moon letter", "a vowel", "a letter that cannot follow ال"],
          "ش is a sun letter: الشَّمْس."),
        rd("الْقَمَر", ["الشَّمْس", "الْكَمَر", "القَمَر"]),
        rd("الشَّمْس", ["الْشَمْس", "الشَّمْز", "الصَّمْس"]),
        rd("الطَّبِيب", ["الْطَبِيب", "التَّبِيب", "الطَّبِيت"]),
        M("What marks a sun letter after ال?", "a shadda on it", ["a sukūn on the lām", "a tanwīn", "a fatḥa on the alif"],
          "The lām is not pronounced; the sun letter is doubled instead."),
        M("Which is read “ad-dars”?", "الدَّرْس", ["الْدَرْس", "الدَّرْز", "الذَّرْس"], "د is a sun letter, so ال is assimilated and د is doubled."),
        M("Which is read “al-bāb”?", "الْبَاب", ["البَّاب", "الدَّاب", "الْنَاب"], "ب is a moon letter, so the lām is pronounced."),
    ],
)

# ---------------------------------------------------------------------------- 14
L14 = lesson(
    "Signs and notices",
    "First real reading",
    requires=[],
    loose=True,
    cards=[
        card("Words you will see around town",
             "These words are on signs in any Arab city. Sound them out first, then check the transliteration.",
             tables=[table(["Word", "English"],
                           [["مَطْعَم", "restaurant"], ["مَطَار", "airport"], ["فُنْدُق", "hotel"],
                            ["مُسْتَشْفَى", "hospital"], ["صَيْدَلِيَّة", "pharmacy"], ["بَنْك", "bank"]],
                           say=[0], tlit=[0])]),
        card("More signs",
             "Entrances, exits and places to go.",
             tables=[table(["Word", "English"],
                           [["مَدْخَل", "entrance"], ["مَخْرَج", "exit"], ["مَحَطَّة", "station"],
                            ["سُوق", "market"], ["جَامِعَة", "university"], ["مَسْجِد", "mosque"]],
                           say=[0], tlit=[0])]),
    ],
    exercises=[
        mn("مَطْعَم", "restaurant", ["airport", "hotel", "bank"]),
        mn("مَطَار", "airport", ["restaurant", "station", "market"]),
        mn("فُنْدُق", "hotel", ["hospital", "pharmacy", "exit"]),
        mn("مُسْتَشْفَى", "hospital", ["pharmacy", "hotel", "bank"]),
        mn("صَيْدَلِيَّة", "pharmacy", ["hospital", "market", "university"]),
        mn("مَدْخَل", "entrance", ["exit", "station", "bank"]),
        mn("مَخْرَج", "exit", ["entrance", "airport", "market"]),
        mn("سُوق", "market", ["station", "mosque", "university"]),
        rd("جَامِعَة", ["جَامِعَت", "جَامَعَة", "جَمِعَة"]),
        rd("مَحَطَّة", ["مَحَطَة", "مَحَتَّة", "مُحَطَّة"]),
    ],
)

# ---------------------------------------------------------------------------- 15
L15 = lesson(
    "Numerals",
    "٠ ١ ٢ ٣ ٤ ٥ ٦ ٧ ٨ ٩ and the words for 0–10",
    requires=[],
    loose=True,
    cards=[
        card("The digits",
             "Most Arab countries write numbers with the Eastern Arabic digits, and the tables in this course use them. "
             "Although Arabic letters run right to left, a number is still read left to right: ١٢ is twelve, written "
             "with the one first. (Morocco, Algeria, Tunisia and Libya mostly use 0 1 2 3 like English.)",
             tables=[table(["Digit", "Word", "English"],
                           [["٠", "صِفْر", "zero"], ["١", "وَاحِد", "one"], ["٢", "اِثْنَان", "two"],
                            ["٣", "ثَلَاثَة", "three"], ["٤", "أَرْبَعَة", "four"], ["٥", "خَمْسَة", "five"]],
                           say=[1], tlit=[1])]),
        card("Six to ten",
             "The words for three to ten have a second form without ة (ثَلَاث، أَرْبَع…), and the rule for choosing "
             "between them is one of the stranger ones in Arabic; it comes in a later unit. For now, learn these as a counting list.",
             tables=[table(["Digit", "Word", "English"],
                           [["٦", "سِتَّة", "six"], ["٧", "سَبْعَة", "seven"], ["٨", "ثَمَانِيَة", "eight"],
                            ["٩", "تِسْعَة", "nine"], ["١٠", "عَشَرَة", "ten"]],
                           say=[1], tlit=[1])]),
    ],
    exercises=[
        M("Which direction is the number ١٢ read?", "Left to right: twelve", ["Right to left: twenty-one", "Top to bottom", "It depends on the word"],
          "Numbers are read left to right even inside Arabic text."),
        M("Which digit is five?", "٥", ["٤", "٦", "٠"], "٥ looks like a small circle, ٠ is a dot, ٤ and ٦ differ in shape."),
        M("Which digit is zero?", "٠", ["٥", "١", "٩"], "٠ is a plain dot."),
        M("Which digit is one?", "١", ["٧", "٨", "٩"], "١ is a single vertical stroke."),
        mn("وَاحِد", "one", ["two", "three", "ten"]),
        mn("خَمْسَة", "five", ["three", "four", "nine"]),
        mn("عَشَرَة", "ten", ["six", "seven", "one"]),
        M("Which word is “three”?", "ثَلَاثَة", ["اِثْنَان", "أَرْبَعَة", "سِتَّة"], "ثَلَاثَة = ٣."),
        M("Which word is “eight”?", "ثَمَانِيَة", ["سَبْعَة", "تِسْعَة", "ثَلَاثَة"], "ثَمَانِيَة = ٨."),
        M("Which digit matches تِسْعَة?", "٩", ["٧", "٦", "٣"], "تِسْعَة = ٩."),
    ],
)

UNIT = unit("الحروف: the Arabic script", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14, L15])
