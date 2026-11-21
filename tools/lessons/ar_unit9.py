"""Unit 9: the past tense, saying no with لَمْ, school and jobs (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 119
L119 = lesson(
    "Women in the plural: هُنَّ · أَنْتُنَّ",
    "هُنَّ يَدْرُسْنَ · بَيْتُهُنَّ",
    requires=["طالب", "مدرس", "هو", "هي", "درس", "عمل"],
    cards=[
        card("A plural for women",
             "You met هُنَّ and أَنْتُنَّ with كَانَ (كُنَّ, كُنْتُنَّ). Ordinary verbs have the same separate plural for “you” and “they” when every person is a woman: أَنْتُنَّ and هُنَّ. "
             "(A group with even one man in it uses the masculine plural.) The present verb ends in ـْنَ for both. "
             "Most words for women, and adjectives describing them, that end in ة take ـَات.",
             tables=[table(["Pronoun", "English", "Verb"],
                           [["أَنْتُنَّ", "you (women) study", "تَدْرُسْنَ"], ["هُنَّ", "they (women) study", "يَدْرُسْنَ"],
                            ["أَنْتُنَّ", "you (women) work", "تَعْمَلْنَ"], ["هُنَّ", "they (women) work", "يَعْمَلْنَ"],
                            ["أَنْتُنَّ", "you (women) write", "تَكْتُبْنَ"], ["هُنَّ", "they (women) write", "يَكْتُبْنَ"]],
                           say=[0, 2], tlit=[0, 2], gloss=False),
                    table(["One woman", "Women"],
                          [["مُدَرِّسَة", "مُدَرِّسَات"], ["طَالِبَة", "طَالِبَات"], ["سَعِيدَة", "سَعِيدَات"], ["مَشْغُولَة", "مَشْغُولَات"]],
                          say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "The plural pronoun can be dropped, since the verb already shows who is meant.",
             examples=[
                 ex("هُنَّ مُدَرِّسَات فِي مَدْرَسَة كَبِيرَة.", "They (women) are teachers at a big school.", "هُنَّ"),
                 ex("أَنْتُنَّ طَالِبَات فِي الْجَامِعَة.", "You (women) are students at the university.", "أَنْتُنَّ"),
                 ex("هُنَّ يَدْرُسْنَ الْعَرَبِيَّة.", "They (women) study Arabic.", "يَدْرُسْنَ"),
                 ex("أَنْتُنَّ تَعْمَلْنَ فِي الْمَكْتَب.", "You (women) work in the office.", "تَعْمَلْنَ"),
                 ex("الْبَنَات يَلْعَبْنَ فِي الْحَدِيقَة.", "The girls are playing in the garden.", "يَلْعَبْنَ"),
                 ex("هَلْ أَنْتُنَّ مَشْغُولَات؟", "Are you (women) busy?", "أَنْتُنَّ"),
             ]),
        card("Their, your: ـهُنَّ and ـكُنَّ",
             "The matching endings attach to nouns and to prepositions, just as ـهُم and ـكُم do for men.",
             tables=[table(["Ending", "Arabic", "English"],
                           [["ـهُنَّ", "بَيْتُهُنَّ", "their (women’s) house"], ["ـكُنَّ", "بَيْتُكُنَّ", "your (women’s) house"],
                            ["ـهُنَّ", "لَهُنَّ · مَعَهُنَّ · عِنْدَهُنَّ", "for them · with them · they have"],
                            ["ـكُنَّ", "لَكُنَّ · مَعَكُنَّ · عِنْدَكُنَّ", "for you · with you · you have"]],
                           say=[1], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("Which pronoun means “they (women)”?", "هُنَّ", ["هُمْ", "هِيَ", "أَنْتُنَّ"], "هُنَّ = they (all women)."),
        M("Which pronoun means “you (women)”?", "أَنْتُنَّ", ["أَنْتُمْ", "أَنْتِ", "هُنَّ"], "أَنْتُنَّ = you (all women)."),
        M("Which means “they (women) study”?", "يَدْرُسْنَ", ["يَدْرُسُون", "تَدْرُسْنَ", "يَدْرُسَان"], "يَـ … ـْنَ."),
        M("Which means “you (women) work”?", "تَعْمَلْنَ", ["تَعْمَلِين", "تَعْمَلُون", "يَعْمَلْنَ"], "تَـ … ـْنَ."),
        M("Which is the plural of طَالِبَة (women only)?", "طَالِبَات", ["طَالِبُون", "طُلَّاب", "طَالِبَتَان"], "ـَات is the plural of women."),
        M("Which means “their (women’s) house”?", "بَيْتُهُنَّ", ["بَيْتُهُمْ", "بَيْتُهَا", "بَيْتُكُنَّ"], "ـهُنَّ."),
        M("Which means “with you (women)”?", "مَعَكُنَّ", ["مَعَهُنَّ", "مَعَكُمْ", "مَعَكِ"], "ـكُنَّ."),
        F("هُنَّ ___ فِي الْمَكْتَب.", "يَعْمَلْنَ", ["يَعْمَلُون", "تَعْمَل", "يَعْمَلَان"], "Women: ـْنَ.", tr="They (women) work in the office."),
        F("أَنْتُنَّ ___ فِي الْجَامِعَة.", "طَالِبَات", ["طَالِبَة", "طُلَّاب", "طَالِبَتَان"], "The plural of women.", tr="You (women) are students at the university."),
    ],
    verify=(vv("درس", "pres", antunna="تَدْرُسْنَ", hunna="يَدْرُسْنَ") + vv("عمل", "pres", antunna="تَعْمَلْنَ", hunna="يَعْمَلْنَ")
            + vv("كتب", "pres", antunna="تَكْتُبْنَ", hunna="يَكْتُبْنَ") + vv("لعب", "pres", hunna="يَلْعَبْنَ")
            + vps("مُدَرِّسَة", "مُدَرِّسَات") + vps("طَالِبَة", "طَالِبَات") + vps("سَعِيدَة", "سَعِيدَات") + vps("مَشْغُولَة", "مَشْغُولَات")
            + vw("أَنْتُنَّ", "هُنَّ", "بَيْتُهُنَّ", "بَيْتُكُنَّ", "لَهُنَّ", "لَكُنَّ", "مَعَهُنَّ", "مَعَكُنَّ", "عِنْدَهُنَّ", "عِنْدَكُنَّ", "الْبَنَات")),
)

# ---------------------------------------------------------------------------- 120
L120 = lesson(
    "Yesterday: the past tense, he and she",
    "كَتَبَ · كَتَبَتْ · ذَهَبَ · ذَهَبَتْ",
    requires=["كتب", "ذهب", "دخل", "خرج", "فتح", "جلس"],
    cards=[
        card("The past tense: he and she",
             "The simplest form of an Arabic verb is the past tense for “he”: usually three consonants with a fatḥa on each: "
             "كَتَبَ (he wrote). For “she” add ـَتْ: كَتَبَتْ. There is no prefix. Compare the present يَكْتُب (he "
             "writes) with the past كَتَبَ (he wrote). Dictionaries list a verb under this “he” form.",
             tables=[table(["English", "he…", "she…"],
                           [["wrote", "كَتَبَ", "كَتَبَتْ"], ["went", "ذَهَبَ", "ذَهَبَتْ"], ["entered", "دَخَلَ", "دَخَلَتْ"],
                            ["left", "خَرَجَ", "خَرَجَتْ"], ["opened", "فَتَحَ", "فَتَحَتْ"], ["sat", "جَلَسَ", "جَلَسَتْ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("The verb comes first",
             "As in the present, the verb usually comes first and agrees with its subject in gender. Before ال the "
             "ـَتْ ending takes a helping kasra: جَلَسَتِ الطَّالِبَة.",
             examples=[
                 ex("كَتَبَ أَحْمَد رِسَالَة.", "Ahmad wrote a letter.", "كَتَبَ"),
                 ex("ذَهَبَتْ سَارَة إِلَى السُّوق.", "Sara went to the market.", "ذَهَبَتْ"),
                 ex("دَخَلَ الْمُدَرِّس الْغُرْفَة.", "The teacher entered the room.", "دَخَلَ"),
                 ex("خَرَجَتْ لَيْلَى مِنَ الْبَيْت.", "Layla left the house.", "خَرَجَتْ"),
                 ex("فَتَحَ الْمُدِير النَّافِذَة.", "The manager opened the window.", "فَتَحَ"),
                 ex("جَلَسَتِ الطَّالِبَة هُنَا.", "The student sat here.", "جَلَسَتِ"),
             ]),
    ],
    exercises=[
        M("What does كَتَبَ mean?", "he wrote", ["he writes", "I wrote", "she wrote"], "Past tense, “he”."),
        M("Which means “she went”?", "ذَهَبَتْ", ["ذَهَبَ", "يَذْهَب", "ذَهَبْتُ"], "ـَتْ = she."),
        M("Which means “he opened”?", "فَتَحَ", ["فَتَحَتْ", "يَفْتَح", "اِفْتَحْ"], "فَتَحَ."),
        M("Which of these is a past tense verb?", "دَخَلَ", ["يَدْخُل", "اُدْخُلْ", "تَدْخُل"], "The past has no prefix."),
        M("Which means “Sara went to the market”?", "ذَهَبَتْ سَارَة إِلَى السُّوق", ["ذَهَبَ سَارَة إِلَى السُّوق", "تَذْهَب سَارَة إِلَى السُّوق", "سَارَة ذَهَبَ إِلَى السُّوق"], "Feminine past: ذَهَبَتْ."),
        M("Which means “Layla left the house”?", "خَرَجَتْ لَيْلَى مِنَ الْبَيْت", ["خَرَجَ لَيْلَى مِنَ الْبَيْت", "خَرَجْتُ لَيْلَى مِنَ الْبَيْت", "يَخْرُج لَيْلَى مِنَ الْبَيْت"], "Feminine past: خَرَجَتْ."),
        F("___ أَحْمَد رِسَالَة.", "كَتَبَ", ["كَتَبَتْ", "تَكْتُب", "اُكْتُبْ"], "Masculine past.", tr="Ahmad wrote a letter."),
        F("___ سَارَة إِلَى السُّوق.", "ذَهَبَتْ", ["ذَهَبَ", "ذَهَبْتُ", "ذَهَبُوا"], "Feminine past.", tr="Sara went to the market."),
        F("جَلَسَتِ ___ هُنَا.", "الطَّالِبَة", ["الطَّالِب", "الطُّلَّاب", "طَالِب"], "A feminine verb needs a feminine subject.", tr="The student sat here."),
    ],
    verify=(vv("كتب", "past", huwa="كَتَبَ", hiya="كَتَبَتْ") + vv("ذهب", "past", huwa="ذَهَبَ", hiya="ذَهَبَتْ")
            + vv("دخل", "past", huwa="دَخَلَ", hiya="دَخَلَتْ") + vv("خرج", "past", huwa="خَرَجَ", hiya="خَرَجَتْ")
            + vv("فتح", "past", huwa="فَتَحَ", hiya="فَتَحَتْ") + vv("جلس", "past", huwa="جَلَسَ", hiya="جَلَسَتْ")
            + vw("جَلَسَتِ", "الطَّالِبَة", "النَّافِذَة", "الْغُرْفَة", "رِسَالَة")),
)

# ---------------------------------------------------------------------------- 121
L121 = lesson(
    "I, you, we in the past",
    "كَتَبْتُ · كَتَبْتَ · كَتَبْتِ · كَتَبْنَا",
    requires=["كتب", "ذهب", "دخل", "خرج", "فتح", "جلس"],
    cards=[
        card("Endings for I, you, we",
             "For these persons the last letter of the stem gets a sukūn and an ending is added: ـْتُ (I), ـْتَ (you, "
             "man), ـْتِ (you, woman), ـْنَا (we). They are the same endings you saw in كُنْتُ, كُنْتَ, كُنْتِ, كُنَّا.",
             tables=[table(["Pronoun", "كَتَبَ", "English"],
                           [["أَنَا", "كَتَبْتُ", "I wrote"], ["أَنْتَ", "كَتَبْتَ", "you (man) wrote"], ["أَنْتِ", "كَتَبْتِ", "you (woman) wrote"],
                            ["نَحْنُ", "كَتَبْنَا", "we wrote"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Now the verb carries the person, so the pronoun is not needed.",
             examples=[
                 ex("كَتَبْتُ رِسَالَة إِلَى صَدِيقِي.", "I wrote a letter to my friend.", "كَتَبْتُ"),
                 ex("ذَهَبْتَ إِلَى الْمَدْرَسَة أَمْس.", "You went to school yesterday. (to a man)", "ذَهَبْتَ"),
                 ex("دَخَلْتِ الْمَكْتَب يَا سَارَة.", "You entered the office, Sara. (to a woman)", "دَخَلْتِ"),
                 ex("خَرَجْنَا مِنَ الْبَيْت.", "We left the house.", "خَرَجْنَا"),
                 ex("فَتَحْتُ الْبَاب.", "I opened the door.", "فَتَحْتُ"),
                 ex("جَلَسْنَا فِي الْحَدِيقَة.", "We sat in the garden.", "جَلَسْنَا"),
             ]),
    ],
    exercises=[
        M("Which means “I wrote”?", "كَتَبْتُ", ["كَتَبْتَ", "كَتَبَ", "كَتَبْنَا"], "ـْتُ = I."),
        M("Which means “you (man) went”?", "ذَهَبْتَ", ["ذَهَبْتِ", "ذَهَبْتُ", "ذَهَبَتْ"], "ـْتَ = you (man)."),
        M("Which means “you (woman) entered”?", "دَخَلْتِ", ["دَخَلْتَ", "دَخَلْتُ", "دَخَلَتْ"], "ـْتِ = you (woman)."),
        M("Which means “we left”?", "خَرَجْنَا", ["خَرَجْتُ", "خَرَجُوا", "خَرَجَتْ"], "ـْنَا = we."),
        M("Which ending means “I” on a past verb?", "ـْتُ", ["ـْتَ", "ـْنَا", "ـَتْ"], "كُنْتُ، كَتَبْتُ."),
        M("Which means “I opened the door”?", "فَتَحْتُ الْبَاب", ["فَتَحَ الْبَاب", "فَتَحْتَ الْبَاب", "فَتَحْنَا الْبَاب"], "فَتَحْتُ = I opened."),
        F("أَنَا ___ إِلَى الْمَدْرَسَة أَمْس.", "ذَهَبْتُ", ["ذَهَبْتَ", "ذَهَبَتْ", "ذَهَبْنَا"], "The sentence is about “I”.", tr="I went to school yesterday."),
        F("نَحْنُ ___ فِي الْحَدِيقَة.", "جَلَسْنَا", ["جَلَسْتُ", "جَلَسَتْ", "جَلَسُوا"], "ـْنَا = we.", tr="We sat in the garden."),
        F("أَنْتِ ___ الْمَكْتَب يَا سَارَة.", "دَخَلْتِ", ["دَخَلْتَ", "دَخَلْتُ", "دَخَلَتْ"], "To a woman: ـْتِ.", tr="You entered the office, Sara."),
    ],
    verify=(vv("كتب", "past", ana="كَتَبْتُ", anta="كَتَبْتَ", anti="كَتَبْتِ", nahnu="كَتَبْنَا")
            + vv("ذهب", "past", ana="ذَهَبْتُ", anta="ذَهَبْتَ") + vv("دخل", "past", anti="دَخَلْتِ")
            + vv("خرج", "past", nahnu="خَرَجْنَا") + vv("فتح", "past", ana="فَتَحْتُ") + vv("جلس", "past", nahnu="جَلَسْنَا")
            + vw("الْمَكْتَب", "الْبَاب", "الْحَدِيقَة")),
)

# ---------------------------------------------------------------------------- 122
L122 = lesson(
    "They, you all, the two in the past",
    "كَتَبُوا · كَتَبْنَ · كَتَبَا · كَتَبْتُمْ",
    requires=["كتب", "ذهب", "دخل", "خرج", "جلس", "طالب"],
    cards=[
        card("The rest of the past tense",
             "Here is the whole past tense of كَتَبَ. A group of men ends in ـُوا (with a silent alif), a group of "
             "women in ـْنَ, and two people in ـَا (men) or ـَتَا (women). For “you” the ـْتـ stays and the ending "
             "follows: ـْتُمَا, ـْتُمْ, ـْتُنَّ.",
             tables=[table(["Person", "Arabic", "English"],
                           [["هُمَا", "كَتَبَا", "the two of them (men) wrote"], ["هُمَا", "كَتَبَتَا", "the two of them (women) wrote"],
                            ["هُمْ", "كَتَبُوا", "they (men) wrote"], ["هُنَّ", "كَتَبْنَ", "they (women) wrote"],
                            ["أَنْتُمَا", "كَتَبْتُمَا", "you two wrote"], ["أَنْتُمْ", "كَتَبْتُمْ", "you (men) wrote"],
                            ["أَنْتُنَّ", "كَتَبْتُنَّ", "you (women) wrote"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Remember that a verb which comes before a plural subject stays singular: دَخَلَ الطُّلَّاب. When the "
             "subject comes first, or is only a pronoun, the verb takes the plural ending. Before ال, a final ـْتُمْ "
             "takes a helping ḍamma.",
             examples=[
                 ex("دَخَلَ الطُّلَّاب الصَّفّ.", "The students entered the classroom.", "دَخَلَ"),
                 ex("الطُّلَّاب دَخَلُوا الصَّفّ.", "The students entered the classroom.", "دَخَلُوا"),
                 ex("الْبَنَات ذَهَبْنَ إِلَى الْمَكْتَبَة.", "The girls went to the library.", "ذَهَبْنَ"),
                 ex("الْوَلَدَان جَلَسَا هُنَا.", "The two boys sat here.", "جَلَسَا"),
                 ex("هَلْ كَتَبْتُمُ الْوَاجِب؟", "Did you (men) write the homework?", "كَتَبْتُمُ"),
                 ex("هُنَّ خَرَجْنَ مِنَ الْمَدْرَسَة.", "They (women) left the school.", "خَرَجْنَ"),
             ]),
    ],
    exercises=[
        M("Which means “they (men) wrote”?", "كَتَبُوا", ["كَتَبْنَ", "كَتَبَا", "كَتَبْتُمْ"], "ـُوا for a group of men."),
        M("Which means “they (women) wrote”?", "كَتَبْنَ", ["كَتَبُوا", "كَتَبَتَا", "كَتَبْتُنَّ"], "ـْنَ for women."),
        M("Which means “the two boys wrote”?", "كَتَبَا", ["كَتَبَتَا", "كَتَبُوا", "كَتَبْتُمَا"], "ـَا for two men."),
        M("Which means “the two girls wrote”?", "كَتَبَتَا", ["كَتَبَا", "كَتَبْتُمَا", "كَتَبْنَ"], "ـَتَا for two women."),
        M("Which means “you (men) wrote”?", "كَتَبْتُمْ", ["كَتَبْتُنَّ", "كَتَبُوا", "كَتَبْنَا"], "ـْتُمْ."),
        M("Which means “you (women) wrote”?", "كَتَبْتُنَّ", ["كَتَبْتُمْ", "كَتَبْنَ", "كَتَبْتِ"], "ـْتُنَّ."),
        M("Which sentence puts the verb first? “The students entered the classroom”", "دَخَلَ الطُّلَّاب الصَّفّ", ["دَخَلُوا الطُّلَّاب الصَّفّ", "دَخَلْنَ الطُّلَّاب الصَّفّ", "دَخَلْتُ الطُّلَّاب الصَّفّ"], "A verb before its subject stays singular."),
        F("الْبَنَات ___ إِلَى الْمَكْتَبَة.", "ذَهَبْنَ", ["ذَهَبُوا", "ذَهَبَا", "ذَهَبْتُنَّ"], "The girls: ـْنَ.", tr="The girls went to the library."),
        F("هَلْ أَنْتُمْ ___ الْوَاجِب؟", "كَتَبْتُمُ", ["كَتَبْتُ", "كَتَبُوا", "كَتَبَا"], "To a group: ـْتُمْ.", tr="Did you (men) write the homework?"),
    ],
    verify=(vv("كتب", "past", huma_m="كَتَبَا", huma_f="كَتَبَتَا", hum="كَتَبُوا", hunna="كَتَبْنَ", antuma="كَتَبْتُمَا", antum="كَتَبْتُمْ", antunna="كَتَبْتُنَّ")
            + vv("دخل", "past", huwa="دَخَلَ", hum="دَخَلُوا", ana="دَخَلْتُ", hunna="دَخَلْنَ") + vv("ذهب", "past", hunna="ذَهَبْنَ")
            + vv("جلس", "past", huma_m="جَلَسَا") + vv("خرج", "past", hunna="خَرَجْنَ")
            + vw("الصَّفّ", "الْمَكْتَبَة", "الْوَلَدَان", "الْوَاجِب")),
)

# ---------------------------------------------------------------------------- 123
L123 = lesson(
    "Past verbs with a kasra: شَرِبَ · فَهِمَ",
    "شَرِبْتُ الشَّايْ · فَهِمْتُ الدَّرْس",
    requires=["شرب", "فهم", "سمع", "عمل", "لعب", "ركب"],
    cards=[
        card("Another past vowel",
             "In most past verbs the middle letter has a fatḥa (كَتَبَ). A group of common verbs have a kasra instead: "
             "شَرِبَ (drank), فَهِمَ (understood), سَمِعَ (heard), عَمِلَ (worked, did), لَعِبَ (played), رَكِبَ (rode). "
             "The endings are exactly the same as before. Learn the middle vowel with each verb; the dictionary shows "
             "it.",
             tables=[table(["English", "he", "I", "they (men)"],
                           [["drank", "شَرِبَ", "شَرِبْتُ", "شَرِبُوا"], ["understood", "فَهِمَ", "فَهِمْتُ", "فَهِمُوا"],
                            ["heard", "سَمِعَ", "سَمِعْتُ", "سَمِعُوا"], ["worked", "عَمِلَ", "عَمِلْتُ", "عَمِلُوا"],
                            ["played", "لَعِبَ", "لَعِبْتُ", "لَعِبُوا"], ["rode", "رَكِبَ", "رَكِبْتُ", "رَكِبُوا"]],
                           say=[1, 2, 3], tlit=[1, 2, 3], gloss=False)]),
        card("In sentences",
             "Sentences about what happened yesterday.",
             examples=[
                 ex("شَرِبْتُ الشَّايْ.", "I drank the tea.", "شَرِبْتُ"),
                 ex("فَهِمْتُ الدَّرْس.", "I understood the lesson.", "فَهِمْتُ"),
                 ex("سَمِعَتْ سَارَة الْمُوسِيقَى.", "Sara heard the music.", "سَمِعَتْ"),
                 ex("لَعِبَ الْأَوْلَاد كُرَة الْقَدَم.", "The boys played football.", "لَعِبَ"),
                 ex("عَمِلْنَا فِي الْحَدِيقَة.", "We worked in the garden.", "عَمِلْنَا"),
                 ex("رَكِبْتُ الدَّرَّاجَة.", "I rode the bicycle.", "رَكِبْتُ"),
             ]),
    ],
    exercises=[
        M("What does شَرِبَ mean?", "he drank", ["he heard", "he played", "he rode"], "شَرِبَ = to drink."),
        M("Which means “I understood”?", "فَهِمْتُ", ["فَهِمْتَ", "فَهِمَتْ", "فَهِمْنَا"], "ـْتُ = I."),
        M("Which means “they (men) played”?", "لَعِبُوا", ["لَعِبْنَ", "لَعِبَا", "لَعِبْتُمْ"], "ـُوا."),
        M("Which means “she heard”?", "سَمِعَتْ", ["سَمِعَ", "سَمِعْتُ", "سَمِعْنَ"], "ـَتْ = she."),
        M("Which means “I drank the tea”?", "شَرِبْتُ الشَّايْ", ["شَرِبْتَ الشَّايْ", "يَشْرَب الشَّايْ", "شَرِبَ الشَّايْ"], "شَرِبْتُ = I drank."),
        M("Which verb has a kasra on the middle letter in the past?", "فَهِمَ", ["كَتَبَ", "ذَهَبَ", "دَخَلَ"], "فَهِمَ."),
        F("أَنَا ___ الدَّرْس.", "فَهِمْتُ", ["فَهِمَ", "فَهِمُوا", "فَهِمْتَ"], "“I”.", tr="I understood the lesson."),
        F("لَعِبَ ___ كُرَة الْقَدَم.", "الْأَوْلَاد", ["الْبَنَات", "الْبِنْت", "الْأُمّ"], "A masculine verb needs masculine boys.", tr="The boys played football."),
        F("سَمِعَتْ ___ الْمُوسِيقَى.", "سَارَة", ["أَحْمَد", "الْوَلَد", "خَالِد"], "A feminine verb needs a woman.", tr="Sara heard the music."),
    ],
    verify=(vv("شرب", "past", huwa="شَرِبَ", ana="شَرِبْتُ", hum="شَرِبُوا") + vv("فهم", "past", huwa="فَهِمَ", ana="فَهِمْتُ", hum="فَهِمُوا")
            + vv("سمع", "past", huwa="سَمِعَ", ana="سَمِعْتُ", hum="سَمِعُوا", hiya="سَمِعَتْ")
            + vv("عمل", "past", huwa="عَمِلَ", ana="عَمِلْتُ", hum="عَمِلُوا", nahnu="عَمِلْنَا")
            + vv("لعب", "past", huwa="لَعِبَ", ana="لَعِبْتُ", hum="لَعِبُوا") + vv("ركب", "past", huwa="رَكِبَ", ana="رَكِبْتُ", hum="رَكِبُوا")
            + vw("الشَّايْ", "الدَّرْس", "الْأَوْلَاد", "الْمُوسِيقَى")),
)

# ---------------------------------------------------------------------------- 124
L124 = lesson(
    "Questions about yesterday",
    "هَلْ ذَهَبْتَ؟ · مَاذَا فَعَلْتَ؟ · أَيْنَ ذَهَبْتِ؟",
    requires=["هل", "ماذا", "أين", "متى", "من", "فعل"],
    cards=[
        card("Asking in the past",
             "Question words work with the past tense exactly as with the present: they go first and the past verb "
             "follows. The person asked decides the ending (ـْتَ to a man, ـْتِ to a woman).",
             tables=[table(["Question", "Answer"],
                           [["هَلْ ذَهَبْتَ إِلَى الْمَدْرَسَة؟", "نَعَمْ، ذَهَبْتُ."], ["مَاذَا فَعَلْتَ أَمْس؟", "دَرَسْتُ فِي الْمَكْتَبَة."],
                            ["أَيْنَ ذَهَبْتِ؟", "ذَهَبْتُ إِلَى السُّوق."], ["مَتَى خَرَجْتَ مِنَ الْبَيْت؟", "خَرَجْتُ فِي الصَّبَاح."],
                            ["مَنْ فَتَحَ النَّافِذَة؟", "فَتَحَ أَحْمَد النَّافِذَة."]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("A conversation",
             "A yes–no question can be answered with نَعَمْ followed by the verb; when you are asked “did you…?”, the verb is in the “I” form.",
             examples=[
                 ex("مَاذَا فَعَلْتِ أَمْس يَا سَارَة؟", "What did you do yesterday, Sara? (to a woman)", "فَعَلْتِ"),
                 ex("دَرَسْتُ فِي الْمَكْتَبَة، ثُمَّ ذَهَبْتُ إِلَى السُّوق.", "I studied in the library, then I went to the market.", "ثُمَّ"),
                 ex("هَلْ شَرِبْتِ الْقَهْوَة هُنَاك؟", "Did you drink coffee there? (to a woman)", "شَرِبْتِ"),
                 ex("نَعَمْ، شَرِبْتُ الْقَهْوَة وَالشَّايْ.", "Yes, I drank coffee and tea.", "نَعَمْ"),
                 ex("وَمَتَى رَجَعْتِ إِلَى الْبَيْت؟", "And when did you go back home? (to a woman)", "رَجَعْتِ"),
                 ex("رَجَعْتُ فِي الْمَسَاء.", "I went back in the evening.", "رَجَعْتُ"),
             ]),
    ],
    exercises=[
        M("Which asks a man “Did you go to school?”", "هَلْ ذَهَبْتَ إِلَى الْمَدْرَسَة؟", ["هَلْ ذَهَبْتِ إِلَى الْمَدْرَسَة؟", "هَلْ ذَهَبْتُ إِلَى الْمَدْرَسَة؟", "هَلْ ذَهَبَ إِلَى الْمَدْرَسَة؟"], "ـْتَ = you (man)."),
        M("Which asks a woman “What did you do yesterday?”", "مَاذَا فَعَلْتِ أَمْس؟", ["مَاذَا فَعَلْتَ أَمْس؟", "مَاذَا فَعَلَتْ أَمْس؟", "أَيْنَ فَعَلْتِ أَمْس؟"], "ـْتِ = you (woman)."),
        M("Which asks a woman “Where did you go?”", "أَيْنَ ذَهَبْتِ؟", ["أَيْنَ ذَهَبْتَ؟", "أَيْنَ ذَهَبْتُ؟", "مَتَى ذَهَبْتِ؟"], "أَيْنَ = where."),
        M("Which asks “Who opened the window?”", "مَنْ فَتَحَ النَّافِذَة؟", ["مَاذَا فَتَحَ النَّافِذَة؟", "أَيْنَ فَتَحَ النَّافِذَة؟", "مَنْ يَفْتَحُون النَّافِذَة؟"], "مَنْ = who."),
        M("Which answers «أَيْنَ ذَهَبْتَ؟»?", "ذَهَبْتُ إِلَى السُّوق", ["دَرَسْتُ الْعَرَبِيَّة", "خَرَجْتُ فِي الصَّبَاح", "فَتَحَ أَحْمَد النَّافِذَة"], "“Where” asks for a place."),
        M("Which answers «مَتَى خَرَجْتَ؟»?", "خَرَجْتُ فِي الصَّبَاح", ["خَرَجْتُ إِلَى السُّوق", "خَرَجَ أَحْمَد", "خَرَجْنَا مِنَ الْبَيْت"], "“When” asks for a time."),
        M("Which answers «هَلْ شَرِبْتِ الْقَهْوَة؟» with yes?", "نَعَمْ، شَرِبْتُ الْقَهْوَة", ["نَعَمْ، شَرِبْتِ الْقَهْوَة", "نَعَمْ، شَرِبَتِ الْقَهْوَة", "نَعَمْ، تَشْرَبِين الْقَهْوَة"], "The answer uses “I”."),
        F("___ فَعَلْتَ أَمْس؟", "مَاذَا", ["أَيْنَ", "مَنْ", "هَلْ"], "“What”.", tr="What did you do yesterday?"),
        F("هَلْ ___ أَنْتَ إِلَى السُّوق؟", "ذَهَبْتَ", ["ذَهَبْتُ", "ذَهَبَتْ", "ذَهَبْنَا"], "To a man.", tr="Did you go to the market? (to a man)"),
    ],
    verify=(vv("ذهب", "past", anta="ذَهَبْتَ", anti="ذَهَبْتِ", ana="ذَهَبْتُ") + vv("فعل", "past", anta="فَعَلْتَ", anti="فَعَلْتِ")
            + vv("درس", "past", ana="دَرَسْتُ") + vv("شرب", "past", anti="شَرِبْتِ", ana="شَرِبْتُ") + vv("رجع", "past", anti="رَجَعْتِ", ana="رَجَعْتُ")
            + vv("خرج", "past", anta="خَرَجْتَ", ana="خَرَجْتُ") + vv("فتح", "past", huwa="فَتَحَ")
            + vw("الصَّبَاح", "الْمَسَاء", "الْقَهْوَة", "ثُمَّ", "هُنَاك")),
)

# ---------------------------------------------------------------------------- 125
L125 = lesson(
    "Verbs with an object, verbs with a preposition",
    "كَتَبْتُهَا · فَتَحَهُ · ذَهَبَ إِلَى · بَحَثَ عَنْ",
    requires=["كتب", "فتح", "ذهب", "بحث", "حصل", "شكر"],
    cards=[
        card("Direct object, or a preposition?",
             "Some verbs act directly on something: كَتَبَ الرِّسَالَة (wrote the letter). These are transitive and "
             "take their object with no preposition (the last column is empty; دَخَلَ is like this, though دَخَلَ إِلَى is also used). Other verbs need a preposition before the next word: ذَهَبَ "
             "إِلَى الْمَدْرَسَة (went to school). The preposition is part of what you learn with the verb.",
             tables=[table(["English", "Arabic", "Preposition"],
                           [["wrote the letter", "كَتَبَ الرِّسَالَة", ""], ["opened the door", "فَتَحَ الْبَاب", ""],
                            ["entered the room", "دَخَلَ الْغُرْفَة", ""],
                            ["went to school", "ذَهَبَ إِلَى الْمَدْرَسَة", "إِلَى"], ["left the house", "خَرَجَ مِنَ الْبَيْت", "مِنْ"],
                            ["sat in the garden", "جَلَسَ فِي الْحَدِيقَة", "فِي"], ["looked for a job", "بَحَثَ عَنْ عَمَل", "عَنْ"],
                            ["got a certificate", "حَصَلَ عَلَى شَهَادَة", "عَلَى"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("Replacing the object: ـهُ ـهَا ـكَ ـنِي",
             "To avoid repeating a noun, attach a pronoun to the verb. It is the same set you know on nouns, except that "
             "“me” is ـنِي: ـنِي (me), ـكَ (you, man), ـهُ (him, it), ـهَا (her, it), ـنَا (us).",
             examples=[
                 ex("كَتَبْتُ الرِّسَالَة. كَتَبْتُهَا أَمْس.", "I wrote the letter. I wrote it yesterday.", "كَتَبْتُهَا"),
                 ex("غَسَلَ الْمُدِير الْكُوب، ثُمَّ حَمَلَهُ.", "The manager washed the cup, then carried it.", "حَمَلَهُ"),
                 ex("شَكَرْتُكَ أَمْس.", "I thanked you yesterday. (to a man)", "شَكَرْتُكَ"),
                 ex("شَكَرَتْنِي سَارَة.", "Sara thanked me.", "شَكَرَتْنِي"),
                 ex("بَحَثْتُ عَنْ عَمَل وَحَصَلْتُ عَلَى وَظِيفَة.", "I looked for work and got a job.", "بَحَثْتُ عَنْ"),
             ]),
    ],
    exercises=[
        M("Which means “He went to school”?", "ذَهَبَ إِلَى الْمَدْرَسَة", ["ذَهَبَ الْمَدْرَسَة", "ذَهَبَ مِنَ الْمَدْرَسَة", "ذَهَبَ عَنِ الْمَدْرَسَة"], "ذَهَبَ إِلَى."),
        M("Which means “She left the house”?", "خَرَجَتْ مِنَ الْبَيْت", ["خَرَجَتِ الْبَيْت", "خَرَجَتْ إِلَى الْبَيْت", "خَرَجَتْ عَلَى الْبَيْت"], "خَرَجَ مِنْ."),
        M("Which means “I wrote it” (the letter, الرِّسَالَة)?", "كَتَبْتُهَا", ["كَتَبْتُهُ", "كَتَبْتَهَا", "كَتَبَتْهَا"], "ـهَا for a feminine thing."),
        M("Which means “He opened it” (the door, الْبَاب)?", "فَتَحَهُ", ["فَتَحَهَا", "فَتَحْتُهُ", "فَتَحَتْهُ"], "ـهُ for a masculine thing."),
        M("Which means “Sara thanked me”?", "شَكَرَتْنِي سَارَة", ["شَكَرَنِي سَارَة", "شَكَرْتُهَا سَارَة", "شَكَرَتْكَ سَارَة"], "ـنِي = me; the verb is feminine."),
        M("Which means “I looked for a job”?", "بَحَثْتُ عَنْ عَمَل", ["بَحَثْتُ فِي عَمَل", "بَحَثْتُ إِلَى عَمَل", "بَحَثْتُ عَلَى عَمَل"], "بَحَثَ عَنْ."),
        F("حَصَلْتُ ___ شَهَادَة.", "عَلَى", ["إِلَى", "مِنْ", "عَنْ"], "حَصَلَ عَلَى.", tr="I got a certificate."),
        F("بَحَثْتُ ___ عَمَل.", "عَنْ", ["إِلَى", "مِنْ", "عَلَى"], "بَحَثَ عَنْ.", tr="I looked for a job."),
        F("ذَهَبْنَا ___ السُّوق.", "إِلَى", ["مِنْ", "عَنْ", "عَلَى"], "ذَهَبَ إِلَى.", tr="We went to the market."),
    ],
    verify=(vv("كتب", "past", ana="كَتَبْتُ") + vv("فتح", "past", huwa="فَتَحَ") + vv("شكر", "past", ana="شَكَرْتُ", hiya="شَكَرَتْ")
            + vv("بحث", "past", ana="بَحَثْتُ") + vv("حصل", "past", ana="حَصَلْتُ") + vv("ذهب", "past", nahnu="ذَهَبْنَا")
            + vw("مَرَّةً", "أُخْرَى", "وَظِيفَة", "شَهَادَة")),
)

# ---------------------------------------------------------------------------- 126
L126 = lesson(
    "Not in the past: لَمْ",
    "لَمْ أَكْتُبْ · لَمْ تَذْهَبْ",
    requires=["لم", "كتب", "ذهب", "درس", "سمع", "فتح"],
    cards=[
        card("لَمْ + the “short” present",
             "To say that something did NOT happen, put لَمْ in front of a present verb. The verb looks like the present "
             "but loses its final vowel: it ends in a sukūn (and the ن of ـِين falls away), as in لَا تَدْخُلْ. The meaning is past even though the "
             "verb looks present. Before ال, the sukūn becomes a helping kasra: لَمْ أَكْتُبِ الْوَاجِب.",
             tables=[table(["Pronoun", "Present", "With لَمْ"],
                           [["أَنَا", "أَكْتُب", "لَمْ أَكْتُبْ"], ["أَنْتَ", "تَكْتُب", "لَمْ تَكْتُبْ"], ["أَنْتِ", "تَكْتُبِين", "لَمْ تَكْتُبِي"],
                            ["هُوَ", "يَكْتُب", "لَمْ يَكْتُبْ"], ["هِيَ", "تَكْتُب", "لَمْ تَكْتُبْ"], ["نَحْنُ", "نَكْتُب", "لَمْ نَكْتُبْ"]],
                           say=[0, 1, 2], tlit=[2], gloss=False)]),
        card("In sentences",
             "Use لَمْ for what did not happen yesterday, last week or last year.",
             examples=[
                 ex("لَمْ أَذْهَبْ إِلَى الْمَدْرَسَة أَمْس.", "I did not go to school yesterday.", "لَمْ أَذْهَبْ"),
                 ex("لَمْ أَكْتُبِ الْوَاجِب.", "I did not write the homework.", "لَمْ أَكْتُبِ"),
                 ex("لَمْ تَدْرُسْ سَارَة أَمْس.", "Sara did not study yesterday.", "لَمْ تَدْرُسْ"),
                 ex("لَمْ يَفْتَحِ الْمُدِير الْبَاب.", "The manager did not open the door.", "لَمْ يَفْتَحِ"),
                 ex("لَمْ نَسْمَعِ الْمُوسِيقَى.", "We did not hear the music.", "لَمْ نَسْمَعِ"),
                 ex("لِمَاذَا لَمْ تَذْهَبْ؟", "Why didn’t you go? (to a man)", "لَمْ تَذْهَبْ"),
             ]),
    ],
    exercises=[
        M("Which means “I did not write”?", "لَمْ أَكْتُبْ", ["لَا أَكْتُب", "لَمْ كَتَبْتُ", "لَيْسَ أَكْتُب"], "لَمْ + أَكْتُبْ."),
        M("Which means “he did not go”?", "لَمْ يَذْهَبْ", ["لَمْ ذَهَبَ", "لَا يَذْهَب", "لَمْ تَذْهَبْ"], "لَمْ + يَذْهَبْ."),
        M("Which means “she did not study”?", "لَمْ تَدْرُسْ", ["لَمْ يَدْرُسْ", "لَمْ أَدْرُسْ", "لَمْ تَدْرُسِي"], "لَمْ + تَدْرُسْ."),
        M("Which means “we did not hear”?", "لَمْ نَسْمَعْ", ["لَمْ أَسْمَعْ", "لَمْ يَسْمَعْ", "لَمْ تَسْمَعْ"], "نَـ = we."),
        M("Which means “You (woman) did not go”?", "لَمْ تَذْهَبِي", ["لَمْ تَذْهَبْ", "لَمْ تَذْهَبِينَ", "لَمْ يَذْهَبِي"], "The ن of ـِين falls away."),
        M("What time does a sentence with لَمْ describe?", "the past", ["the present", "the future", "a command"], "لَمْ + present-looking verb = did not."),
        F("لَمْ ___ إِلَى الْمَدْرَسَة أَمْس.", "أَذْهَبْ", ["ذَهَبْتُ", "تَذْهَبْ", "يَذْهَبْ"], "“I”: أَـ.", tr="I did not go to school yesterday."),
        F("لَمْ ___ سَارَة أَمْس.", "تَدْرُسْ", ["يَدْرُسْ", "أَدْرُسْ", "نَدْرُسْ"], "Sara = she.", tr="Sara did not study yesterday."),
        F("لِمَاذَا لَمْ ___؟", "تَذْهَبْ", ["ذَهَبْتَ", "تَذْهَبِي", "أَذْهَبْ"], "To a man: تَـ + sukūn.", tr="Why didn’t you go? (to a man)"),
    ],
    verify=(vv("كتب", "jus", ana="أَكْتُبْ", anta="تَكْتُبْ", anti="تَكْتُبِي", huwa="يَكْتُبْ", hiya="تَكْتُبْ", nahnu="نَكْتُبْ")
            + vv("كتب", "pres", ana="أَكْتُب", anta="تَكْتُب", anti="تَكْتُبِين", huwa="يَكْتُب", hiya="تَكْتُب", nahnu="نَكْتُب")
            + vv("ذهب", "jus", ana="أَذْهَبْ", huwa="يَذْهَبْ", anta="تَذْهَبْ", anti="تَذْهَبِي") + vv("درس", "jus", hiya="تَدْرُسْ")
            + vv("سمع", "jus", nahnu="نَسْمَعْ") + vv("فتح", "jus", huwa="يَفْتَحْ")
            + vw("لَمْ", "لِمَاذَا", "الْمُوسِيقَى", "الْوَاجِب")),
)

# ---------------------------------------------------------------------------- 127
L127 = lesson(
    "لَمْ with plurals, and لَمْ يَكُنْ",
    "لَمْ يَكْتُبُوا · لَمْ يَكْتُبْنَ · لَمْ أَكُنْ",
    requires=["لم", "كتب", "دخل", "خرج", "كان", "طالب"],
    cards=[
        card("Plurals after لَمْ",
             "The same rule you know from أَنْ applies: endings that finish in ن lose it. The “short” present of the "
             "plurals is therefore the same as the form after أَنْ. The feminine plural ـْنَ keeps its ن.",
             tables=[table(["Person", "Present", "With لَمْ"],
                           [["هُمْ", "يَكْتُبُون", "لَمْ يَكْتُبُوا"], ["هُمَا", "يَكْتُبَان", "لَمْ يَكْتُبَا"], ["هُنَّ", "يَكْتُبْنَ", "لَمْ يَكْتُبْنَ"],
                            ["أَنْتُمْ", "تَكْتُبُون", "لَمْ تَكْتُبُوا"], ["أَنْتُنَّ", "تَكْتُبْنَ", "لَمْ تَكْتُبْنَ"]],
                           say=[0, 1, 2], tlit=[2], gloss=False)]),
        card("Saying “was not”",
             "To say that something was not so, use لَمْ with the present of كَانَ. The middle letter of يَكُون is "
             "dropped: لَمْ يَكُنْ, لَمْ أَكُنْ, لَمْ تَكُنْ, لَمْ نَكُنْ. Before ال the sukūn becomes a kasra. You may also "
             "meet مَا + the past tense (مَا ذَهَبْتُ) with the same meaning, but it is less common in modern writing.",
             examples=[
                 ex("لَمْ يَكُنْ أَخِي فِي الْبَيْت.", "My brother was not at home.", "لَمْ يَكُنْ"),
                 ex("لَمْ أَكُنْ مَشْغُولًا أَمْس.", "I was not busy yesterday. (a man speaking)", "لَمْ أَكُنْ"),
                 ex("لَمْ يَكُنِ الْجَوّ جَمِيلًا.", "The weather was not nice.", "لَمْ يَكُنِ"),
                 ex("الطُّلَّاب لَمْ يَدْخُلُوا الصَّفّ.", "The students did not enter the classroom.", "لَمْ يَدْخُلُوا"),
                 ex("هُنَّ لَمْ يَخْرُجْنَ مِنَ الْبَيْت.", "They (women) did not leave the house.", "لَمْ يَخْرُجْنَ"),
                 ex("أَلَمْ تَذْهَبَا إِلَى الْحَفْلَة؟", "Didn’t you two go to the party?", "لَمْ تَذْهَبَا"),
             ]),
    ],
    exercises=[
        M("Which means “they (men) did not write”?", "لَمْ يَكْتُبُوا", ["لَمْ يَكْتُبُون", "لَمْ يَكْتُبْنَ", "لَمْ يَكْتُبَا"], "The ن falls away."),
        M("Which means “they (women) did not write”?", "لَمْ يَكْتُبْنَ", ["لَمْ يَكْتُبُوا", "لَمْ يَكْتُبْ", "لَمْ تَكْتُبْ"], "ـْنَ stays."),
        M("Which means “the two (men) did not write”?", "لَمْ يَكْتُبَا", ["لَمْ يَكْتُبَان", "لَمْ يَكْتُبُوا", "لَمْ يَكْتُبْنَ"], "ـَان → ـَا."),
        M("Which means “I was not busy” (a man speaking)?", "لَمْ أَكُنْ مَشْغُولًا", ["لَمْ كُنْتُ مَشْغُولًا", "لَمْ أَكُونْ مَشْغُولًا", "لَمْ يَكُنْ مَشْغُولًا"], "لَمْ + أَكُنْ."),
        M("Which means “My brother was not at home”?", "لَمْ يَكُنْ أَخِي فِي الْبَيْت", ["لَمْ كَانَ أَخِي فِي الْبَيْت", "كَانَ أَخِي فِي الْبَيْت", "لَيْسَ أَخِي فِي الْبَيْت"], "لَمْ يَكُنْ."),
        M("What happens to the middle letter of يَكُون after لَمْ?", "it drops out: لَمْ يَكُنْ", ["it stays: لَمْ يَكُونْ", "it becomes ا", "it is doubled"], "يَكُون → يَكُنْ."),
        F("الطُّلَّاب لَمْ ___ الصَّفّ.", "يَدْخُلُوا", ["يَدْخُلُون", "يَدْخُلْنَ", "يَدْخُلْ"], "A group of men.", tr="The students did not enter the classroom."),
        F("هُنَّ لَمْ ___ مِنَ الْبَيْت.", "يَخْرُجْنَ", ["يَخْرُجُوا", "يَخْرُجَا", "تَخْرُجْ"], "A group of women.", tr="They (women) did not leave the house."),
        F("لَمْ ___ الْجَوّ جَمِيلًا.", "يَكُنِ", ["كَانَ", "تَكُنِ", "أَكُنِ"], "الْجَوّ is masculine.", tr="The weather was not nice."),
    ],
    verify=(vv("كتب", "jus", hum="يَكْتُبُوا", huma_m="يَكْتُبَا", hunna="يَكْتُبْنَ", antum="تَكْتُبُوا", antunna="تَكْتُبْنَ")
            + vv("كتب", "pres", hum="يَكْتُبُون", huma_m="يَكْتُبَان", hunna="يَكْتُبْنَ", antum="تَكْتُبُون", antunna="تَكْتُبْنَ")
            + vv("دخل", "jus", hum="يَدْخُلُوا") + vv("خرج", "jus", hunna="يَخْرُجْنَ") + vv("ذهب", "jus", antuma="تَذْهَبَا")
            + vw("يَكُنْ", "أَكُنْ", "تَكُنْ", "نَكُنْ", "يَكُنِ", "مَشْغُولًا", "الْحَفْلَة")),
)


# ---------------------------------------------------------------------------- 128
L128 = lesson(
    "Schools and grades",
    "الْمَدْرَسَة الثَّانَوِيَّة · الْجَامِعَة · الصَّفّ الْخَامِس",
    requires=["مدرسة", "جامعة", "طالب", "كلية", "صف", "مرحلة"],
    cards=[
        card("Stages of education",
             "The names and the number of years differ from country to country, but these words are "
             "widely understood. A school adjective follows the noun and agrees with it (feminine, with ال).",
             tables=[table(["English", "Arabic"],
                           [["primary school", "الْمَدْرَسَة الِابْتِدَائِيَّة"], ["middle school", "الْمَدْرَسَة الْمُتَوَسِّطَة"],
                            ["secondary school", "الْمَدْرَسَة الثَّانَوِيَّة"], ["university", "الْجَامِعَة"],
                            ["college, faculty", "الْكُلِّيَّة"], ["class, grade", "الصَّفّ"], ["year (of study)", "السَّنَة"],
                            ["pupil (boy · girl)", "تِلْمِيذ · تِلْمِيذَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Where do you study?",
             "Grades and years use the ordinal numbers: الْأَوَّل, الثَّانِي, الثَّالِث … الْعَاشِر. With a feminine "
             "noun the ordinal is feminine (السَّنَة الثَّانِيَة).",
             examples=[
                 ex("أَنَا فِي الصَّفّ الْخَامِس.", "I am in the fifth grade.", "الصَّفّ الْخَامِس"),
                 ex("أُخْتِي تِلْمِيذَة فِي الْمَدْرَسَة الِابْتِدَائِيَّة.", "My sister is a pupil at primary school.", "الِابْتِدَائِيَّة"),
                 ex("أَخِي طَالِب فِي الْمَدْرَسَة الثَّانَوِيَّة.", "My brother is a student at secondary school.", "الثَّانَوِيَّة"),
                 ex("أَدْرُس فِي كُلِّيَّة الْهَنْدَسَة.", "I study at the engineering college.", "كُلِّيَّة"),
                 ex("هِيَ فِي السَّنَة الثَّانِيَة فِي الْجَامِعَة.", "She is in her second year at the university.", "السَّنَة الثَّانِيَة"),
                 ex("دَرَسَ أَبِي فِي كُلِّيَّة الطِّبّ.", "My father studied at the medical college.", "دَرَسَ"),
             ]),
    ],
    exercises=[
        M("What does الْجَامِعَة mean?", "the university", ["the school", "the class", "the city"], "جَامِعَة = university."),
        M("What does الصَّفّ mean at school?", "class, grade", ["row of houses", "street", "library"], "الصَّفّ = the class or grade."),
        M("Which means “secondary school”?", "الْمَدْرَسَة الثَّانَوِيَّة", ["الْمَدْرَسَة الِابْتِدَائِيَّة", "الْجَامِعَة الثَّانَوِيَّة", "الْمَدْرَسَة الْمُتَوَسِّطَة"], "ثَانَوِيَّة = secondary."),
        M("Which means “I am in the fifth grade”?", "أَنَا فِي الصَّفّ الْخَامِس", ["أَنَا فِي الصَّفّ الْخَامِسَة", "أَنَا فِي الصَّفّ الثَّانِي", "أَنَا مِنَ الصَّفّ الْخَامِس"], "الصَّفّ is masculine: الْخَامِس."),
        M("Which means “She is in her second year”?", "هِيَ فِي السَّنَة الثَّانِيَة", ["هِيَ فِي السَّنَة الثَّانِي", "هُوَ فِي السَّنَة الثَّانِيَة", "هِيَ فِي الصَّفّ الثَّانِيَة"], "السَّنَة is feminine: الثَّانِيَة."),
        M("Which means “My father studied at the medical college”?", "دَرَسَ أَبِي فِي كُلِّيَّة الطِّبّ", ["دَرَسَتْ أَبِي فِي كُلِّيَّة الطِّبّ", "يَدْرُس أَبِي فِي كُلِّيَّة الطِّبّ", "دَرَسْتُ فِي كُلِّيَّة الطِّبّ"], "دَرَسَ = he studied."),
        F("أَنَا ___ الصَّفّ الْخَامِس.", "فِي", ["مِنْ", "إِلَى", "عَنْ"], "In = فِي.", tr="I am in the fifth grade."),
        F("أَخِي طَالِب فِي الْمَدْرَسَة ___.", "الثَّانَوِيَّة", ["الثَّانَوِيّ", "الثَّانَوِيُّون", "ثَانَوِيَّة"], "Feminine, with ال.", tr="My brother is a student at secondary school."),
        F("هِيَ فِي السَّنَة ___ فِي الْجَامِعَة.", "الثَّانِيَة", ["الثَّانِي", "الثَّانِيَان", "الثَّلَاث"], "Feminine ordinal.", tr="She is in her second year at the university."),
    ],
    verify=(vv("درس", "past", huwa="دَرَسَ")
            + vw("الِابْتِدَائِيَّة", "الْمُتَوَسِّطَة", "الثَّانَوِيَّة", "الْجَامِعَة", "الْكُلِّيَّة", "تِلْمِيذ", "تِلْمِيذَة", "الْخَامِس",
                 "الثَّانِيَة", "الْهَنْدَسَة", "الطِّبّ")),
)

# ---------------------------------------------------------------------------- 129
L129 = lesson(
    "School subjects",
    "الرِّيَاضِيَّات · الْعُلُوم · التَّارِيخ · الْجُغْرَافِيَا",
    requires=["مادة", "تاريخ", "علم", "لغة", "أدب", "درس"],
    cards=[
        card("Subjects",
             "Ten subjects you may study. They all take ال when you talk about them.",
             tables=[table(["English", "Arabic"],
                           [["mathematics", "الرِّيَاضِيَّات"], ["science", "الْعُلُوم"], ["history", "التَّارِيخ"],
                            ["geography", "الْجُغْرَافِيَا"], ["literature", "الْأَدَب"], ["physics", "الْفِيزِيَاء"],
                            ["chemistry", "الْكِيمِيَاء"], ["computing", "الْحَاسُوب"], ["art", "الْفَنّ"], ["language", "اللُّغَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Talking about subjects",
             "You know أَدْرُس (I study) and أُحِبّ (I like). Add a subject after them, and use صَعْب and سَهْل to "
             "describe it.",
             examples=[
                 ex("أُحِبّ التَّارِيخ وَالْجُغْرَافِيَا.", "I like history and geography.", "التَّارِيخ"),
                 ex("أَدْرُس الرِّيَاضِيَّات وَالْفِيزِيَاء.", "I study mathematics and physics.", "الرِّيَاضِيَّات"),
                 ex("الْكِيمِيَاء صَعْبَة وَالْجُغْرَافِيَا سَهْلَة.", "Chemistry is difficult and geography is easy.", "الْكِيمِيَاء"),
                 ex("مَاذَا تَدْرُس فِي الْجَامِعَة؟", "What do you study at the university? (to a man)", "تَدْرُس"),
                 ex("أَدْرُس الْأَدَب الْعَرَبِيّ.", "I study Arabic literature.", "الْأَدَب"),
                 ex("عِنْدِي اِمْتِحَان فِي الرِّيَاضِيَّات.", "I have an exam in mathematics.", "اِمْتِحَان"),
             ]),
    ],
    exercises=[
        M("What does الرِّيَاضِيَّات mean?", "mathematics", ["sport", "history", "science"], "الرِّيَاضِيَّات = maths."),
        M("What does الْجُغْرَافِيَا mean?", "geography", ["history", "literature", "physics"], "الْجُغْرَافِيَا = geography."),
        M("What does الْكِيمِيَاء mean?", "chemistry", ["physics", "computing", "art"], "الْكِيمِيَاء = chemistry."),
        M("Which means “I study physics”?", "أَدْرُس الْفِيزِيَاء", ["أُحِبّ الْفِيزِيَاء", "دَرَسْتُ الْفِيزِيَاء", "أَدْرُس الْكِيمِيَاء"], "أَدْرُس = I study."),
        M("Which means “I like history”?", "أُحِبّ التَّارِيخ", ["أَدْرُس التَّارِيخ", "أُحِبّ الْفَنّ", "أُحِبّ الْجُغْرَافِيَا"], "أُحِبّ = I like."),
        M("Which means “Chemistry is difficult”?", "الْكِيمِيَاء صَعْبَة", ["الْكِيمِيَاء سَهْلَة", "الْكِيمِيَاء صَعْب", "الْفِيزِيَاء صَعْبَة"], "كِيمِيَاء is feminine: صَعْبَة."),
        M("Which asks a man “What do you study at the university?”", "مَاذَا تَدْرُس فِي الْجَامِعَة؟", ["مَاذَا تَدْرُسِين فِي الْجَامِعَة؟", "أَيْنَ تَدْرُس فِي الْجَامِعَة؟", "مَاذَا أَدْرُس فِي الْجَامِعَة؟"], "تَدْرُس = you (man) study."),
        F("أَدْرُس ___ الْعَرَبِيّ.", "الْأَدَب", ["الْفِيزِيَاء", "الْحَاسُوب", "الرِّيَاضِيَّات"], "Arabic literature.", tr="I study Arabic literature."),
        F("عِنْدِي ___ فِي الرِّيَاضِيَّات.", "اِمْتِحَان", ["جَامِعَة", "مَدْرَسَة", "مَطْعَم"], "An exam.", tr="I have an exam in mathematics."),
    ],
    verify=(vv("درس", "pres", ana="أَدْرُس", anta="تَدْرُس", anti="تَدْرُسِين")
            + vw("الرِّيَاضِيَّات", "الْعُلُوم", "التَّارِيخ", "الْجُغْرَافِيَا", "الْأَدَب", "الْفِيزِيَاء", "الْكِيمِيَاء", "الْحَاسُوب", "الْفَنّ",
                 "اللُّغَة", "اِمْتِحَان", "صَعْبَة", "سَهْلَة")),
)

# ---------------------------------------------------------------------------- 130
L130 = lesson(
    "The days of the week",
    "الْأَحَد · الِاثْنَيْن · الثُّلَاثَاء · الْأَرْبِعَاء",
    requires=["يوم", "أسبوع", "أحد", "سبت", "أمس", "بعد"],
    cards=[
        card("Seven days",
             "The names of Sunday to Thursday come from the numbers one to five (one, two, three …). Friday "
             "is الْجُمْعَة, and in many Arab countries Friday and Saturday are the weekend. After يَوْم, "
             "the name of the day gives “on …”.",
             tables=[table(["English", "Arabic"],
                           [["Sunday", "الْأَحَد"], ["Monday", "الِاثْنَيْن"], ["Tuesday", "الثُّلَاثَاء"], ["Wednesday", "الْأَرْبِعَاء"],
                            ["Thursday", "الْخَمِيس"], ["Friday", "الْجُمْعَة"], ["Saturday", "السَّبْت"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Today, tomorrow, yesterday",
             "الْيَوْم is “today”, غَدًا “tomorrow” and أَمْس “yesterday”. To talk about yesterday’s day, use كَانَ.",
             examples=[
                 ex("الْيَوْم يَوْم الثُّلَاثَاء.", "Today is Tuesday.", "الْيَوْم"),
                 ex("غَدًا يَوْم الْأَرْبِعَاء.", "Tomorrow is Wednesday.", "غَدًا"),
                 ex("أَمْس كَانَ يَوْم الِاثْنَيْن.", "Yesterday was Monday.", "أَمْس"),
                 ex("أَذْهَب إِلَى الْمَدْرَسَة مِنَ الْأَحَد إِلَى الْخَمِيس.", "I go to school from Sunday to Thursday.", "مِنَ الْأَحَد إِلَى الْخَمِيس"),
                 ex("لَا أَذْهَب إِلَى الْمَدْرَسَة يَوْم الْجُمْعَة وَيَوْم السَّبْت.", "I do not go to school on Friday and Saturday.", "يَوْم الْجُمْعَة"),
                 ex("مَاذَا تَفْعَل يَوْم السَّبْت؟", "What do you do on Saturday? (to a man)", "يَوْم السَّبْت"),
             ]),
    ],
    exercises=[
        M("Which day comes after الْأَرْبِعَاء?", "الْخَمِيس", ["الثُّلَاثَاء", "السَّبْت", "الِاثْنَيْن"], "Wednesday, then Thursday."),
        M("Which day comes before الْجُمْعَة?", "الْخَمِيس", ["السَّبْت", "الْأَحَد", "الثُّلَاثَاء"], "Thursday, then Friday."),
        M("Which day name comes from the number five?", "الْخَمِيس", ["الْأَحَد", "الثُّلَاثَاء", "السَّبْت"], "خَمْسَة = five."),
        M("What does غَدًا mean?", "tomorrow", ["yesterday", "today", "last week"], "غَدًا = tomorrow."),
        M("Which means “on Saturday”?", "يَوْم السَّبْت", ["مِنَ السَّبْت", "بَعْد السَّبْت", "قَبْل السَّبْت"], "يَوْم + the day."),
        M("Which means “Yesterday was Monday”?", "أَمْس كَانَ يَوْم الِاثْنَيْن", ["غَدًا يَوْم الِاثْنَيْن", "الْيَوْم يَوْم الِاثْنَيْن", "أَمْس كُنْتُ يَوْم الِاثْنَيْن"], "كَانَ = was."),
        M("Which means “from Sunday to Thursday”?", "مِنَ الْأَحَد إِلَى الْخَمِيس", ["إِلَى الْأَحَد مِنَ الْخَمِيس", "مَعَ الْأَحَد وَالْخَمِيس", "عَلَى الْأَحَد فِي الْخَمِيس"], "مِنْ … إِلَى …"),
        F("الْيَوْم يَوْم ___.", "الثُّلَاثَاء", ["غَدًا", "أَمْس", "مَاذَا"], "A day name.", tr="Today is Tuesday."),
        F("___ يَوْم الْأَرْبِعَاء.", "غَدًا", ["أَمْس", "هَلْ", "مِنَ"], "Tomorrow.", tr="Tomorrow is Wednesday."),
    ],
    verify=vw("الْأَحَد", "الِاثْنَيْن", "الثُّلَاثَاء", "الْأَرْبِعَاء", "الْخَمِيس", "الْجُمْعَة", "السَّبْت", "غَدًا", "الْيَوْم", "أَمْس", "يَوْم"),
)

# ---------------------------------------------------------------------------- 131
L131 = lesson(
    "The school timetable",
    "جَدْوَل الدُّرُوس · الدَّرْس الْأَوَّل · الْوَاجِب",
    requires=["جدول", "درس", "واجب", "حصة", "يوم", "صباح"],
    cards=[
        card("A week of lessons",
             "Here is a timetable. A lesson is دَرْس (plural دُرُوس). The ordinals give the order: الدَّرْس الْأَوَّل "
             "(the first lesson), الدَّرْس الثَّانِي (the second).",
             tables=[table(["Day", "Lessons"],
                           [["الْأَحَد", "الرِّيَاضِيَّات وَالْعُلُوم"], ["الِاثْنَيْن", "التَّارِيخ وَالْجُغْرَافِيَا"],
                            ["الثُّلَاثَاء", "اللُّغَة الْعَرَبِيَّة وَالْفِيزِيَاء"], ["الْأَرْبِعَاء", "الْكِيمِيَاء وَالْفَنّ"],
                            ["الْخَمِيس", "الرِّيَاضِيَّات وَالْحَاسُوب"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Talking about the week",
             "Use عِنْدِي (I have) with a lesson or an exam, and عَلَيَّ أَنْ (I have to) for work you must do.",
             examples=[
                 ex("هَذَا هُوَ جَدْوَل الدُّرُوس.", "This is the timetable.", "جَدْوَل"),
                 ex("عِنْدِي دَرْس التَّارِيخ يَوْم الِاثْنَيْن.", "I have the history lesson on Monday.", "عِنْدِي"),
                 ex("الدَّرْس الْأَوَّل هُوَ الرِّيَاضِيَّات.", "The first lesson is mathematics.", "الدَّرْس الْأَوَّل"),
                 ex("هَلْ عِنْدَكَ اِمْتِحَان يَوْم الْخَمِيس؟", "Do you have an exam on Thursday? (to a man)", "اِمْتِحَان"),
                 ex("نَعَمْ، وَعَلَيَّ أَنْ أَدْرُس الْيَوْم.", "Yes, and I have to study today.", "عَلَيَّ أَنْ"),
                 ex("لَمْ أَكْتُبِ الْوَاجِب أَمْس.", "I did not write the homework yesterday.", "الْوَاجِب"),
             ]),
    ],
    exercises=[
        M("What does جَدْوَل الدُّرُوس mean?", "the timetable", ["the homework", "the exam", "the school"], "جَدْوَل = table, schedule."),
        M("What does الْوَاجِب mean at school?", "homework", ["exam", "timetable", "grade"], "الْوَاجِب = the homework."),
        M("Which means “the first lesson”?", "الدَّرْس الْأَوَّل", ["الدَّرْس الثَّانِي", "الدَّرْس الْأَوَّلَة", "دَرْس أَوَّل الْأَوَّل"], "Masculine: الْأَوَّل."),
        M("Which means “I have the history lesson on Monday”?", "عِنْدِي دَرْس التَّارِيخ يَوْم الِاثْنَيْن", ["عِنْدِي دَرْس التَّارِيخ يَوْم الثُّلَاثَاء", "كَانَ عِنْدِي دَرْس التَّارِيخ", "عِنْدَكَ دَرْس التَّارِيخ يَوْم الِاثْنَيْن"], "عِنْدِي = I have."),
        M("Which asks a man “Do you have an exam on Thursday?”", "هَلْ عِنْدَكَ اِمْتِحَان يَوْم الْخَمِيس؟", ["هَلْ عِنْدَكِ اِمْتِحَان يَوْم الْخَمِيس؟", "هَلْ عِنْدِي اِمْتِحَان يَوْم الْخَمِيس؟", "مَتَى عِنْدَكَ اِمْتِحَان يَوْم الْخَمِيس؟"], "عِنْدَكَ = you (man) have."),
        M("Which means “I did not write the homework”?", "لَمْ أَكْتُبِ الْوَاجِب", ["لَا أَكْتُب الْوَاجِب", "لَمْ كَتَبْتُ الْوَاجِب", "لَيْسَ أَكْتُب الْوَاجِب"], "لَمْ + أَكْتُبِ."),
        F("عِنْدِي ___ يَوْم الْخَمِيس.", "اِمْتِحَان", ["جَدْوَل", "مَدْرَسَة", "غَدًا"], "An exam.", tr="I have an exam on Thursday."),
        F("الدَّرْس ___ هُوَ الرِّيَاضِيَّات.", "الْأَوَّل", ["الْأُولَى", "الثَّلَاثَة", "الْأَحَد"], "Masculine ordinal.", tr="The first lesson is mathematics."),
        F("___ أَنْ أَدْرُس الْيَوْم.", "عَلَيَّ", ["لِي", "مَعِي", "عِنْدِي"], "I have to = عَلَيَّ أَنْ.", tr="I have to study today."),
    ],
    verify=(vv("كتب", "jus", ana="أَكْتُبْ") + vv("درس", "pres", ana="أَدْرُس")
            + vpb("دَرْس", "دُرُوس") + vw("جَدْوَل", "الدُّرُوس", "الْوَاجِب", "الْأَوَّل", "الثَّانِي", "عَلَيَّ", "عِنْدَكَ")),
)

# ---------------------------------------------------------------------------- 132
L132 = lesson(
    "Months and calendars",
    "يَنَايِر · مَارِس · سِبْتَمْبِر · رَمَضَان",
    requires=["شهر", "سنة", "أسبوع", "يوم", "مارس", "تقويم"],
    cards=[
        card("The twelve months",
             "Most Arab countries use these names, which sound like the English ones. A month is شَهْر (plural "
             "شُهُور). “In the month of March” is فِي شَهْر مَارِس.",
             tables=[table(["English", "Arabic", "English", "Arabic"],
                           [["January", "يَنَايِر", "July", "يُولْيُو"], ["February", "فِبْرَايِر", "August", "أَغُسْطُس"],
                            ["March", "مَارِس", "September", "سِبْتَمْبِر"], ["April", "أَبْرِيل", "October", "أُكْتُوبَر"],
                            ["May", "مَايُو", "November", "نُوفِمْبِر"], ["June", "يُونْيُو", "December", "دِيسَمْبِر"]],
                           say=[1, 3], tlit=[1, 3], gloss=False)]),
        card("Other names and another calendar",
             "In Syria, Lebanon, Jordan, Palestine and Iraq the months have different names, for example آذَار (March), "
             "أَيَّار (May), حَزِيرَان (June), تَمُّوز (July) and أَيْلُول (September). Many Arab countries also use "
             "the Islamic calendar, which follows the moon, so its year is about eleven days shorter. Its months include "
             "مُحَرَّم, رَمَضَان and شَوَّال.",
             examples=[
                 ex("فِي شَهْر مَارِس يَكُون الْجَوّ جَمِيلًا.", "In the month of March the weather is nice.", "فِي شَهْر مَارِس"),
                 ex("نَذْهَب إِلَى الْجَامِعَة فِي سِبْتَمْبِر.", "We go to university in September.", "سِبْتَمْبِر"),
                 ex("الشِّتَاء فِي دِيسَمْبِر وَيَنَايِر وَفِبْرَايِر.", "Winter is in December, January and February.", "دِيسَمْبِر"),
                 ex("أَيَّار هُوَ شَهْر مَايُو.", "Ayyar is the month of May.", "أَيَّار"),
                 ex("آذَار هُوَ شَهْر مَارِس.", "Adhar is the month of March.", "آذَار"),
                 ex("رَمَضَان شَهْر فِي التَّقْوِيم الْإِسْلَامِيّ.", "Ramadan is a month in the Islamic calendar.", "رَمَضَان"),
             ]),
    ],
    exercises=[
        M("What does شَهْر mean?", "month", ["week", "year", "day"], "شَهْر = month."),
        M("Which month is مَارِس?", "March", ["May", "June", "April"], "مَارِس = March."),
        M("Which month is أُكْتُوبَر?", "October", ["August", "November", "December"], "أُكْتُوبَر = October."),
        M("Which month is يَنَايِر?", "January", ["July", "June", "February"], "يَنَايِر = January."),
        M("Which month is سِبْتَمْبِر?", "September", ["December", "November", "October"], "سِبْتَمْبِر = September."),
        M("Which means “in the month of May”?", "فِي شَهْر مَايُو", ["مِنْ شَهْر مَايُو", "فِي أُسْبُوع مَايُو", "فِي يَوْم مَايُو"], "فِي شَهْر + the name."),
        M("In Syria, Lebanon and Jordan, which name is used for March?", "آذَار", ["أَيَّار", "تَمُّوز", "أَيْلُول"], "آذَار = March in the Levant."),
        M("What does the Islamic calendar follow?", "the moon", ["the sun", "the seasons", "the weeks"], "Its year is about eleven days shorter."),
        F("فِي شَهْر ___ يَكُون الْجَوّ جَمِيلًا.", "مَارِس", ["الْأَحَد", "غَدًا", "الْجُمْعَة"], "A month name.", tr="In the month of March the weather is nice."),
    ],
    verify=vw("يَنَايِر", "فِبْرَايِر", "مَارِس", "أَبْرِيل", "مَايُو", "يُونْيُو", "يُولْيُو", "أَغُسْطُس", "سِبْتَمْبِر", "أُكْتُوبَر", "نُوفِمْبِر",
              "دِيسَمْبِر", "آذَار", "أَيَّار", "حَزِيرَان", "تَمُّوز", "أَيْلُول", "مُحَرَّم", "رَمَضَان", "شَوَّال", "الْإِسْلَامِيّ", "التَّقْوِيم", "شَهْر"),
)

# ---------------------------------------------------------------------------- 133
L133 = lesson(
    "Professions and workplaces",
    "مُحَاسِب · مُبَرْمِج · صَيْدَلِيّ · مَصْنَع",
    requires=["مهنة", "مصنع", "طيار", "شركة", "مكتب", "عمل"],
    cards=[
        card("More professions",
             "Add ة for a woman, as before. The ـيّ ending takes a feminine ـِيَّة.",
             tables=[table(["English", "Man", "Woman"],
                           [["accountant", "مُحَاسِب", "مُحَاسِبَة"], ["programmer", "مُبَرْمِج", "مُبَرْمِجَة"],
                            ["pharmacist", "صَيْدَلِيّ", "صَيْدَلِيَّة"], ["pilot", "طَيَّار", "طَيَّارَة"],
                            ["baker", "خَبَّاز", "خَبَّازَة"], ["cook", "طَبَّاخ", "طَبَّاخَة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False),
                    table(["English", "Arabic"],
                          [["factory", "مَصْنَع"], ["hospital", "مُسْتَشْفَى"], ["pharmacy", "صَيْدَلِيَّة"], ["bakery", "مَخْبِز"],
                           ["restaurant", "مَطْعَم"], ["office", "مَكْتَب"], ["company", "شَرِكَة"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("Who works where?",
             "A person’s job is a noun sentence (أَبِي طَيَّار). To say where, add يَعْمَل فِي. To say “I want to be …”, use "
             "أُرِيد أَنْ أَكُون, and the job takes the ـًا ending.",
             examples=[
                 ex("أَخِي مُبَرْمِج فِي شَرِكَة كَبِيرَة.", "My brother is a programmer at a big company.", "مُبَرْمِج"),
                 ex("أُخْتِي صَيْدَلِيَّة. تَعْمَل فِي صَيْدَلِيَّة قَرِيبَة مِنَ الْبَيْت.", "My sister is a pharmacist. She works at a pharmacy near home.", "صَيْدَلِيَّة"),
                 ex("الْخَبَّاز يَعْمَل فِي الْمَخْبِز.", "The baker works at the bakery.", "الْخَبَّاز"),
                 ex("الطَّبَّاخ يَعْمَل فِي الْمَطْعَم.", "The cook works in the restaurant.", "الطَّبَّاخ"),
                 ex("أَبِي طَيَّار وَهُوَ مَشْغُول دَائِمًا.", "My father is a pilot and he is always busy.", "طَيَّار"),
                 ex("أُرِيد أَنْ أَكُون مُبَرْمِجًا.", "I want to be a programmer. (a man speaking)", "أَكُون مُبَرْمِجًا"),
             ]),
    ],
    exercises=[
        M("What does مُحَاسِب mean?", "accountant", ["programmer", "pilot", "baker"], "مُحَاسِب = accountant."),
        M("What does مُبَرْمِج mean?", "programmer", ["accountant", "cook", "pharmacist"], "مُبَرْمِج = programmer."),
        M("What does مَصْنَع mean?", "factory", ["bakery", "hospital", "office"], "مَصْنَع = factory."),
        M("Where does the baker work?", "فِي الْمَخْبِز", ["فِي الْمُسْتَشْفَى", "فِي الْمَصْنَع", "فِي الْمَكْتَب"], "خَبَّاز → مَخْبِز."),
        M("Where does the pharmacist work?", "فِي الصَّيْدَلِيَّة", ["فِي الْمَطْعَم", "فِي الْمَخْبِز", "فِي الْمَدْرَسَة"], "صَيْدَلِيّ → صَيْدَلِيَّة."),
        M("Which means “My sister is a pharmacist”?", "أُخْتِي صَيْدَلِيَّة", ["أُخْتِي صَيْدَلِيّ", "أَخِي صَيْدَلِيَّة", "أُخْتِي صَيْدَلِيَّات"], "A woman: ـِيَّة."),
        M("Which means “I want to be a programmer” (a man speaking)?", "أُرِيد أَنْ أَكُون مُبَرْمِجًا", ["أُرِيد أَنْ كُنْتُ مُبَرْمِجًا", "أُرِيد أَنْ أَكُون مُبَرْمِجَةً", "أَنْ أُرِيد أَكُون مُبَرْمِجًا"], "أَنْ + أَكُون + ـًا."),
        F("الْخَبَّاز يَعْمَل فِي ___.", "الْمَخْبِز", ["الْمَصْنَع", "الْمُسْتَشْفَى", "الْمَدْرَسَة"], "A baker works at a bakery.", tr="The baker works at the bakery."),
        F("أَبِي ___ وَهُوَ مَشْغُول.", "طَيَّار", ["طَيَّارَة", "طَيَّارُون", "طَيَّارَات"], "A man, singular.", tr="My father is a pilot and he is busy."),
    ],
    verify=(vf("مُحَاسِب", "مُحَاسِبَة") + vf("مُبَرْمِج", "مُبَرْمِجَة") + vf("صَيْدَلِيّ", "صَيْدَلِيَّة") + vf("طَيَّار", "طَيَّارَة")
            + vf("خَبَّاز", "خَبَّازَة") + vf("طَبَّاخ", "طَبَّاخَة")
            + vw("مَصْنَع", "مُسْتَشْفَى", "صَيْدَلِيَّة", "مَخْبِز", "مَطْعَم", "الْمَخْبِز", "الْمَصْنَع", "الْمُسْتَشْفَى", "مُبَرْمِجًا", "أَكُون")),
)

# ---------------------------------------------------------------------------- 134
L134 = lesson(
    "What do you do?",
    "مَاذَا تَعْمَل؟ · أَيْنَ تَعْمَل؟ · كَمْ سَنَةً عَمِلْتَ؟",
    requires=["عمل", "ماذا", "أين", "كم", "سنة", "أحب"],
    cards=[
        card("Asking about work",
             "Questions about what you do now use the present, and questions about the past use the past or كَانَ. "
             "Remember that «تَعْمَل» is for a man and «تَعْمَلِين» for a woman.",
             tables=[table(["Question", "Answer"],
                           [["مَاذَا تَعْمَل؟", "أَنَا مُحَاسِب."], ["أَيْنَ تَعْمَل؟", "أَعْمَل فِي شَرِكَة."],
                            ["كَمْ سَنَةً عَمِلْتَ هُنَاك؟", "عَمِلْتُ هُنَاك خَمْس سَنَوَات."],
                            ["هَلْ تُحِبّ عَمَلَكَ؟", "نَعَمْ، أُحِبّ عَمَلِي كَثِيرًا."], ["هَلْ عَمَلُكَ صَعْب؟", "لَا، سَهْل."]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("At a party",
             "Two people meet at a party, and one asks about the other’s work.",
             examples=[
                 ex("مَاذَا تَعْمَلِين يَا هِنْد؟", "What do you do, Hind? (to a woman)", "تَعْمَلِين"),
                 ex("أَنَا مُصَمِّمَة. أَعْمَل فِي شَرِكَة صَغِيرَة.", "I am a designer. I work at a small company.", "مُصَمِّمَة"),
                 ex("وَأَيْنَ كُنْتِ تَعْمَلِين قَبْل سَنَتَيْن؟", "And where were you working two years ago? (to a woman)", "كُنْتِ تَعْمَلِين"),
                 ex("عَمِلْتُ فِي مَكْتَب لِمُدَّة ثَلَاث سَنَوَات.", "I worked in an office for three years.", "عَمِلْتُ"),
                 ex("هَلْ تُحِبِّين عَمَلَكِ؟", "Do you like your job? (to a woman)", "تُحِبِّين"),
                 ex("نَعَمْ، أُحِبّ عَمَلِي كَثِيرًا.", "Yes, I like my job a lot.", "عَمَلِي"),
             ]),
    ],
    exercises=[
        M("Which asks a man “What do you do?”", "مَاذَا تَعْمَل؟", ["مَاذَا تَعْمَلِين؟", "أَيْنَ تَعْمَل؟", "مَنْ تَعْمَل؟"], "تَعْمَل = you (man) work."),
        M("Which asks a woman “What do you do?”", "مَاذَا تَعْمَلِين؟", ["مَاذَا تَعْمَل؟", "مَاذَا يَعْمَلُون؟", "مَاذَا عَمِلْتَ؟"], "تَعْمَلِين = you (woman) work."),
        M("Which asks a man “Where do you work?”", "أَيْنَ تَعْمَل؟", ["مَاذَا تَعْمَل؟", "مَتَى تَعْمَل؟", "أَيْنَ عَمِلْتُ؟"], "أَيْنَ = where."),
        M("Which asks a man “How many years did you work there?”", "كَمْ سَنَةً عَمِلْتَ هُنَاك؟", ["كَمْ سَنَةً تَعْمَل هُنَاك؟", "كَمْ سَنَةً عَمِلْتِ هُنَاك؟", "كَمْ سَنَةً عَمِلْتُ هُنَاك؟"], "عَمِلْتَ = you (man) worked."),
        M("Which means “I worked for three years”?", "عَمِلْتُ لِمُدَّة ثَلَاث سَنَوَات", ["أَعْمَل لِمُدَّة ثَلَاث سَنَوَات", "عَمِلَ لِمُدَّة ثَلَاث سَنَوَات", "لَمْ أَعْمَلْ لِمُدَّة ثَلَاث سَنَوَات"], "عَمِلْتُ = I worked."),
        M("Which means “I like my job a lot”?", "أُحِبّ عَمَلِي كَثِيرًا", ["أُحِبّ عَمَلَكَ كَثِيرًا", "لَا أُحِبّ عَمَلِي", "كُنْتُ أُحِبّ عَمَلِي"], "عَمَلِي = my work."),
        M("A woman asks a woman: “Do you like your job?”", "هَلْ تُحِبِّين عَمَلَكِ؟", ["هَلْ تُحِبّ عَمَلَكَ؟", "هَلْ أُحِبّ عَمَلِي؟", "هَلْ تُحِبُّونَ عَمَلَكُمْ؟"], "تُحِبِّين and ـكِ."),
        F("أَيْنَ ___ قَبْل سَنَتَيْن؟ (to a woman)", "كُنْتِ تَعْمَلِين", ["كُنْتَ تَعْمَل", "كُنْتُ أَعْمَل", "تَعْمَلِين"], "To a woman, in the past.", tr="Where were you working two years ago?"),
        F("عَمِلْتُ فِي ___ لِمُدَّة سَنَتَيْن.", "مَكْتَب", ["أَمْس", "كَثِيرًا", "غَدًا"], "A place.", tr="I worked in an office for two years."),
    ],
    verify=(vv("عمل", "pres", anta="تَعْمَل", anti="تَعْمَلِين", ana="أَعْمَل") + vv("عمل", "past", anta="عَمِلْتَ", ana="عَمِلْتُ")
            + vw("عَمَلَكَ", "عَمَلُكَ", "عَمَلِي", "عَمَلَكِ", "تُحِبِّين", "مُصَمِّمَة", "كَثِيرًا", "قَبْل", "سَنَتَيْن")),
)

# ---------------------------------------------------------------------------- 135
L135 = lesson(
    "My education and work",
    "دَرَسْتُ · تَخَرَّجْتُ · حَصَلْتُ عَلَى · عَمِلْتُ",
    requires=["درس", "حصل", "عمل", "تخرج", "جامعة", "شهادة"],
    cards=[
        card("Telling your story",
             "A short biography is a list of past verbs with “I”. Join the steps with ثُمَّ (“then”) and use لِمُدَّة and "
             "بَعْد for how long and when. The verbs تَخَرَّجَ (“graduated”) and تَعَلَّمَ (“learned”) are a new kind of verb, with تَـ in front and a "
             "doubled middle letter; their past endings are the same.",
             tables=[table(["English", "I…"],
                           [["I studied", "دَرَسْتُ"], ["I graduated", "تَخَرَّجْتُ"], ["I got", "حَصَلْتُ عَلَى"],
                            ["I worked", "عَمِلْتُ"], ["I looked for", "بَحَثْتُ عَنْ"], ["I learned", "تَعَلَّمْتُ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A short biography",
             "One person tells where she studied and worked.",
             examples=[
                 ex("دَرَسْتُ الْهَنْدَسَة فِي جَامِعَة كَبِيرَة.", "I studied engineering at a big university.", "دَرَسْتُ"),
                 ex("تَخَرَّجْتُ بَعْد خَمْس سَنَوَات.", "I graduated after five years.", "تَخَرَّجْتُ"),
                 ex("حَصَلْتُ عَلَى شَهَادَة فِي الْهَنْدَسَة.", "I got a degree in engineering.", "حَصَلْتُ عَلَى"),
                 ex("بَحَثْتُ عَنْ عَمَل لِمُدَّة شَهْرَيْن.", "I looked for a job for two months.", "بَحَثْتُ عَنْ"),
                 ex("ثُمَّ عَمِلْتُ فِي شَرِكَة لِمُدَّة سَنَتَيْن.", "Then I worked at a company for two years.", "ثُمَّ"),
                 ex("تَعَلَّمْتُ الْعَرَبِيَّة فِي الْجَامِعَة.", "I learned Arabic at the university.", "تَعَلَّمْتُ"),
             ]),
    ],
    exercises=[
        M("Which means “I graduated”?", "تَخَرَّجْتُ", ["تَخْرُجْ", "خَرَجْتُ", "تَعَلَّمْتُ"], "تَخَرَّجَ = to graduate."),
        M("Which means “I studied”?", "دَرَسْتُ", ["أَدْرُس", "دَرَسَ", "لَمْ أَدْرُسْ"], "ـْتُ = I; past."),
        M("Which means “I got a degree”?", "حَصَلْتُ عَلَى شَهَادَة", ["حَصَلْتُ مِنْ شَهَادَة", "بَحَثْتُ عَنْ شَهَادَة", "حَصَلَ عَلَى شَهَادَة"], "حَصَلَ عَلَى = to get."),
        M("Which means “I looked for a job for two months”?", "بَحَثْتُ عَنْ عَمَل لِمُدَّة شَهْرَيْن", ["بَحَثْتُ عَنْ عَمَل لِمُدَّة سَنَتَيْن", "أَبْحَث عَنْ عَمَل لِمُدَّة شَهْرَيْن", "عَمِلْتُ لِمُدَّة شَهْرَيْن"], "شَهْرَيْن = two months."),
        M("Which means “Then I worked at a company”?", "ثُمَّ عَمِلْتُ فِي شَرِكَة", ["ثُمَّ أَعْمَل فِي شَرِكَة", "قَبْل عَمِلْتُ فِي شَرِكَة", "ثُمَّ عَمِلَتْ فِي شَرِكَة"], "ثُمَّ = then."),
        M("What does تَعَلَّمْتُ mean?", "I learned", ["I taught", "I graduated", "I studied"], "تَعَلَّمَ = to learn."),
        F("___ بَعْد خَمْس سَنَوَات.", "تَخَرَّجْتُ", ["خَرَجْتُ", "دَرَسْتُ", "تَعَلَّمَ"], "I graduated.", tr="I graduated after five years."),
        F("حَصَلْتُ ___ شَهَادَة فِي الْهَنْدَسَة.", "عَلَى", ["مِنْ", "إِلَى", "عَنْ"], "حَصَلَ عَلَى.", tr="I got a degree in engineering."),
        F("___ عَمِلْتُ فِي شَرِكَة.", "ثُمَّ", ["هَلْ", "لَمْ", "أَيْنَ"], "“Then”.", tr="Then I worked at a company."),
    ],
    verify=(vv("درس", "past", ana="دَرَسْتُ") + vv("حصل", "past", ana="حَصَلْتُ") + vv("عمل", "past", ana="عَمِلْتُ") + vv("بحث", "past", ana="بَحَثْتُ")
            + vw("تَخَرَّجْتُ", "تَعَلَّمْتُ", "الْهَنْدَسَة", "شَهْرَيْن", "شَهَادَة", "لِمُدَّة", "ثُمَّ")),
)

# ---------------------------------------------------------------------------- 136
L136 = lesson(
    "Making an appointment",
    "هَلْ أَنْتَ مُتَفَرِّغ يَوْم الثُّلَاثَاء؟ · الْمَوْعِد مُنَاسِب",
    requires=["موعد", "مناسب", "فارغ", "مشغول", "يوم", "صباح"],
    cards=[
        card("Words for an appointment",
             "A meeting needs a day and a time of day. Here are the key words and the parts of the day.",
             tables=[table(["English", "Arabic"],
                           [["appointment", "مَوْعِد"], ["suitable", "مُنَاسِب"], ["free (not busy)", "مُتَفَرِّغ"], ["busy", "مَشْغُول"],
                            ["in the morning", "فِي الصَّبَاح"], ["in the afternoon", "بَعْد الظُّهْر"], ["in the evening", "فِي الْمَسَاء"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Fixing a time",
             "Ask when the other person is free, say when you are busy, and agree on a day.",
             examples=[
                 ex("أُرِيد مَوْعِد مَعَ الْمُدِير.", "I would like an appointment with the manager.", "مَوْعِد"),
                 ex("هَلْ أَنْتَ مُتَفَرِّغ يَوْم الثُّلَاثَاء؟", "Are you free on Tuesday? (to a man)", "مُتَفَرِّغ"),
                 ex("لَا، أَنَا مَشْغُول فِي الصَّبَاح.", "No, I am busy in the morning.", "مَشْغُول"),
                 ex("وَبَعْد الظُّهْر؟", "And in the afternoon?", "بَعْد الظُّهْر"),
                 ex("نَعَمْ، هَذَا الْمَوْعِد مُنَاسِب.", "Yes, this appointment is suitable.", "مُنَاسِب"),
                 ex("حَسَنًا، الْمَوْعِد يَوْم الثُّلَاثَاء بَعْد الظُّهْر.", "Good, the appointment is on Tuesday afternoon.", "الْمَوْعِد"),
             ]),
    ],
    exercises=[
        M("What does مَوْعِد mean?", "appointment", ["office", "homework", "weekend"], "مَوْعِد = appointment."),
        M("What does مُتَفَرِّغ mean?", "free, not busy", ["busy", "suitable", "late"], "مُتَفَرِّغ = free."),
        M("Which means “in the afternoon”?", "بَعْد الظُّهْر", ["فِي الصَّبَاح", "فِي الْمَسَاء", "قَبْل الظُّهْر"], "بَعْد الظُّهْر."),
        M("Which means “in the morning”?", "فِي الصَّبَاح", ["بَعْد الظُّهْر", "فِي الْمَسَاء", "بَعْد الصَّبَاح"], "صَبَاح = morning."),
        M("Which asks a man “Are you free on Tuesday?”", "هَلْ أَنْتَ مُتَفَرِّغ يَوْم الثُّلَاثَاء؟", ["هَلْ أَنْتِ مُتَفَرِّغَة يَوْم الثُّلَاثَاء؟", "هَلْ أَنَا مُتَفَرِّغ يَوْم الثُّلَاثَاء؟", "هَلْ كُنْتَ مُتَفَرِّغًا يَوْم الثُّلَاثَاء؟"], "أَنْتَ + مُتَفَرِّغ."),
        M("Which means “I am busy in the morning”?", "أَنَا مَشْغُول فِي الصَّبَاح", ["أَنَا مُتَفَرِّغ فِي الصَّبَاح", "أَنَا مَشْغُول فِي الْمَسَاء", "كُنْتُ مَشْغُولًا فِي الصَّبَاح"], "مَشْغُول = busy."),
        M("Which means “I would like an appointment with the manager”?", "أُرِيد مَوْعِد مَعَ الْمُدِير", ["أُرِيد مَوْعِد عَلَى الْمُدِير", "كَانَ عِنْدِي مَوْعِد مَعَ الْمُدِير", "لَمْ أَكُنْ مَعَ الْمُدِير"], "مَعَ = with."),
        F("هَلْ أَنْتَ ___ يَوْم الثُّلَاثَاء؟", "مُتَفَرِّغ", ["مُتَفَرِّغَة", "مُتَفَرِّغُون", "مُتَفَرِّغَات"], "To a man.", tr="Are you free on Tuesday?"),
        F("هَذَا الْمَوْعِد ___.", "مُنَاسِب", ["مُنَاسِبَة", "مُنَاسِبُون", "مُنَاسِبَات"], "مَوْعِد is masculine.", tr="This appointment is suitable."),
    ],
    verify=vw("مَوْعِد", "مُنَاسِب", "مُتَفَرِّغ", "مَشْغُول", "مُتَفَرِّغَة", "الصَّبَاح", "الظُّهْر", "الْمَسَاء", "حَسَنًا", "الْمُدِير"),
)

# ---------------------------------------------------------------------------- 137
L137 = lesson(
    "Review: what I did yesterday",
    "دَرَسْتُ · ذَهَبْتُ · لَمْ أَكْتُبْ",
    requires=["كتب", "ذهب", "درس", "أمس", "فعل", "رجع"],
    cards=[
        card("The past tense on one page",
             "The past tense of ذَهَبَ: the stem ذَهَبـ with an ending. Negative: لَمْ + the short present: لَمْ يَذْهَبْ.",
             tables=[table(["Pronoun", "Past", "Negative"],
                           [["أَنَا", "ذَهَبْتُ", "لَمْ أَذْهَبْ"], ["أَنْتَ", "ذَهَبْتَ", "لَمْ تَذْهَبْ"], ["أَنْتِ", "ذَهَبْتِ", "لَمْ تَذْهَبِي"],
                            ["هُوَ", "ذَهَبَ", "لَمْ يَذْهَبْ"], ["هِيَ", "ذَهَبَتْ", "لَمْ تَذْهَبْ"], ["نَحْنُ", "ذَهَبْنَا", "لَمْ نَذْهَبْ"],
                            ["هُمْ", "ذَهَبُوا", "لَمْ يَذْهَبُوا"], ["هُنَّ", "ذَهَبْنَ", "لَمْ يَذْهَبْنَ"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("My day yesterday",
             "A woman tells what she did, and what she did not do.",
             examples=[
                 ex("أَمْس خَرَجْتُ مِنَ الْبَيْت فِي الصَّبَاح.", "Yesterday I left the house in the morning."),
                 ex("ذَهَبْتُ إِلَى الْجَامِعَة وَدَرَسْتُ فِي الْمَكْتَبَة.", "I went to the university and studied in the library."),
                 ex("سَمِعْتُ الْمُوسِيقَى مَعَ صَدِيقَتِي.", "I heard music with my friend (a woman)."),
                 ex("لَمْ أَكْتُبِ الْوَاجِب لِأَنِّي كُنْتُ مَشْغُولَةً.", "I did not write the homework because I was busy."),
                 ex("رَجَعْتُ إِلَى الْبَيْت فِي الْمَسَاء.", "I went back home in the evening."),
             ]),
    ],
    exercises=[
        M("Which means “you (woman) went”?", "ذَهَبْتِ", ["ذَهَبْتَ", "ذَهَبَتْ", "ذَهَبْنَا"], "ـْتِ."),
        M("Which means “they (men) went”?", "ذَهَبُوا", ["ذَهَبْنَ", "ذَهَبَا", "ذَهَبْتُمْ"], "ـُوا."),
        M("Which means “we did not go”?", "لَمْ نَذْهَبْ", ["لَمْ أَذْهَبْ", "لَا نَذْهَب", "ذَهَبْنَا"], "لَمْ + نَذْهَبْ."),
        M("Which means “she did not go”?", "لَمْ تَذْهَبْ", ["لَمْ يَذْهَبْ", "لَمْ تَذْهَبِي", "لَمْ أَذْهَبْ"], "لَمْ + تَذْهَبْ."),
        M("Which means “they (women) did not go”?", "لَمْ يَذْهَبْنَ", ["لَمْ يَذْهَبُوا", "لَمْ تَذْهَبْ", "لَمْ يَذْهَبَا"], "ـْنَ stays."),
        M("Which means “I went to the university and studied”?", "ذَهَبْتُ إِلَى الْجَامِعَة وَدَرَسْتُ", ["ذَهَبْتُ إِلَى الْجَامِعَة وَأَدْرُس", "أَذْهَب إِلَى الْجَامِعَة وَدَرَسْتُ", "ذَهَبَتْ إِلَى الْجَامِعَة وَدَرَسَتْ"], "Two past verbs with “I”."),
        M("Which means “I was busy (a woman speaking) and did not write”?", "كُنْتُ مَشْغُولَةً وَلَمْ أَكْتُبْ", ["كُنْتُ مَشْغُولًا وَلَمْ أَكْتُبْ", "كَانَتْ مَشْغُولَةً وَلَمْ تَكْتُبْ", "كُنْتُ مَشْغُولَةً وَلَا أَكْتُب"], "ـَةً for a woman."),
        F("أَمْس ___ إِلَى الْمَكْتَبَة. (I went)", "ذَهَبْتُ", ["أَذْهَب", "ذَهَبْنَا", "ذَهَبَتْ"], "Past with “I”.", tr="Yesterday I went to the library."),
        F("لَمْ ___ الْوَاجِب أَمْس.", "أَكْتُبِ", ["كَتَبْتُ", "تَكْتُبِي", "يَكْتُبِ"], "لَمْ + the short present.", tr="I did not write the homework yesterday."),
    ],
    verify=(vv("ذهب", "past", ana="ذَهَبْتُ", anta="ذَهَبْتَ", anti="ذَهَبْتِ", huwa="ذَهَبَ", hiya="ذَهَبَتْ", nahnu="ذَهَبْنَا", hum="ذَهَبُوا", hunna="ذَهَبْنَ")
            + vv("ذهب", "jus", ana="أَذْهَبْ", anta="تَذْهَبْ", anti="تَذْهَبِي", huwa="يَذْهَبْ", hiya="تَذْهَبْ", nahnu="نَذْهَبْ", hum="يَذْهَبُوا", hunna="يَذْهَبْنَ")
            + vv("خرج", "past", ana="خَرَجْتُ") + vv("درس", "past", ana="دَرَسْتُ") + vv("سمع", "past", ana="سَمِعْتُ") + vv("رجع", "past", ana="رَجَعْتُ")
            + vw("صَدِيقَتِي", "لِأَنِّي", "مَشْغُولَةً")),
)

# ---------------------------------------------------------------------------- 138
L138 = lesson(
    "Review: school and work",
    "طَالِب · مُدَرِّس · مَوْعِد · عَمِلْتُ فِي شَرِكَة",
    requires=["مدرسة", "جامعة", "عمل", "شركة", "طالب", "أستاذ"],
    cards=[
        card("A conversation at the university",
             "Two students meet and talk about school, subjects, work and the days of the week.",
             examples=[
                 ex("مَرْحَبًا يَا سَامِي. مَاذَا تَدْرُس فِي الْجَامِعَة؟", "Hello, Sami. What do you study at the university? (to a man)"),
                 ex("أَدْرُس الْحَاسُوب. عِنْدِي دَرْس يَوْم الْأَحَد وَيَوْم الثُّلَاثَاء.", "I study computing. I have lessons on Sunday and Tuesday."),
                 ex("هَلْ عَمِلْتَ قَبْل الْجَامِعَة؟", "Did you work before university? (to a man)"),
                 ex("نَعَمْ، عَمِلْتُ فِي مَطْعَم لِمُدَّة سَنَة.", "Yes, I worked at a restaurant for a year."),
                 ex("وَالْآن؟ هَلْ أَنْتَ مَشْغُول يَوْم الْخَمِيس؟", "And now? Are you busy on Thursday? (to a man)"),
                 ex("لَا، أَنَا مُتَفَرِّغ. لَيْسَ عِنْدِي اِمْتِحَان.", "No, I am free. I do not have an exam."),
                 ex("لَمْ يَكُنْ عِنْدِي اِمْتِحَان يَوْم الْأَحَد الْمَاضِي.", "I did not have an exam last Sunday."),
             ]),
    ],
    exercises=[
        M("What does الْحَاسُوب mean?", "computing, the computer", ["history", "geography", "the library"], "الْحَاسُوب."),
        M("Which means “I have a lesson on Sunday”?", "عِنْدِي دَرْس يَوْم الْأَحَد", ["كَانَ عِنْدِي دَرْس يَوْم الْأَحَد", "عِنْدَكَ دَرْس يَوْم الْأَحَد", "عِنْدِي دَرْس مِنَ الْأَحَد"], "عِنْدِي = I have."),
        M("Which asks a man “Did you work?”", "هَلْ عَمِلْتَ؟", ["هَلْ تَعْمَل؟", "هَلْ عَمِلْتِ؟", "هَلْ عَمِلْتُ؟"], "عَمِلْتَ = you (man) worked."),
        M("Which means “I worked at a restaurant for a year”?", "عَمِلْتُ فِي مَطْعَم لِمُدَّة سَنَة", ["أَعْمَل فِي مَطْعَم لِمُدَّة سَنَة", "عَمِلْتُ فِي مَطْعَم لِمُدَّة سَنَتَيْن", "عَمِلَ فِي مَطْعَم لِمُدَّة سَنَة"], "عَمِلْتُ = I worked."),
        M("Which means “I did not have an exam”?", "لَمْ يَكُنْ عِنْدِي اِمْتِحَان", ["كَانَ عِنْدِي اِمْتِحَان", "لَيْسَ عِنْدِي اِمْتِحَان", "لَمْ أَكُنْ عِنْدِي اِمْتِحَان"], "لَمْ يَكُنْ + عِنْدِي."),
        M("Which means “Are you busy on Thursday?” (to a man)", "هَلْ أَنْتَ مَشْغُول يَوْم الْخَمِيس؟", ["هَلْ أَنْتَ مَشْغُول يَوْم السَّبْت؟", "هَلْ كُنْتَ مَشْغُولًا يَوْم الْخَمِيس؟", "هَلْ أَنْتِ مَشْغُولَة يَوْم الْخَمِيس؟"], "الْخَمِيس = Thursday."),
        M("Which is the correct word order for “the second year”?", "السَّنَة الثَّانِيَة", ["السَّنَة الثَّانِي", "الثَّانِيَة السَّنَة", "سَنَة الثَّانِيَة"], "Feminine noun, feminine ordinal."),
        F("مَاذَا ___ فِي الْجَامِعَة؟ (to a man)", "تَدْرُس", ["دَرَسْتَ", "تَدْرُسِين", "أَدْرُس"], "Present, you (man).", tr="What do you study at the university?"),
        F("لَا، أَنَا ___.", "مُتَفَرِّغ", ["مُنَاسِبَة", "مَوْعِد", "الْأَحَد"], "A man says he is free.", tr="No, I am free."),
    ],
    verify=(vv("درس", "pres", anta="تَدْرُس") + vv("عمل", "past", anta="عَمِلْتَ", ana="عَمِلْتُ")
            + vw("مَرْحَبًا", "سَامِي", "الْحَاسُوب", "الْآن")),
)

UNIT = unit("الْمَاضِي وَالدِّرَاسَة: the past tense, school and work",
            [L119, L120, L121, L122, L123, L124, L125, L126, L127, L128, L129, L130, L131, L132, L133, L134, L135, L136, L137, L138])
