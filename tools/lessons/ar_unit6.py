"""Unit 6: commands, pronoun endings on prepositions, "must", food and restaurants
(textbook Chapter 5; all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 80
L80 = lesson(
    "Giving a command",
    "اُكْتُبْ · اِجْلِسْ · اِفْتَحْ",
    requires=["كتب", "جلس", "فتح", "دخل", "باب"],
    cards=[
        card("From the present to the command",
             "To tell one man to do something, start with the present form for “you (man)” and take off the تَـ. "
             "What is left starts with two consonants, so Arabic adds a helping alif in front. The alif gets ُ if the "
             "verb’s present vowel is ُ, and ِ if it is anything else. The end of the verb has a sukūn.",
             tables=[table(["English", "You (man)", "Command"],
                           [["write", "تَكْتُب", "اُكْتُبْ"], ["enter", "تَدْخُل", "اُدْخُلْ"],
                            ["sit", "تَجْلِس", "اِجْلِسْ"], ["open", "تَفْتَح", "اِفْتَحْ"],
                            ["study", "تَدْرُس", "اُدْرُسْ"], ["go", "تَذْهَب", "اِذْهَبْ"]],
                           say=[1, 2], tlit=[2])]),
        card("Commands in use",
             "A command is one word. تَفَضَّل was an invitation; these are plain requests, so add مِنْ فَضْلِكَ "
             "(“please”) when you speak to someone you do not know.",
             examples=[
                 ex("اِجْلِسْ هُنَا.", "Sit here. (to a man)", "اِجْلِسْ"),
                 ex("اُدْخُلْ مِنْ هُنَا.", "Come in this way. (to a man)", "اُدْخُلْ"),
                 ex("اُكْتُبْ هُنَاك.", "Write there. (to a man)", "اُكْتُبْ"),
                 ex("اِذْهَبْ إِلَى الْمَدْرَسَة.", "Go to school. (to a man)", "اِذْهَبْ"),
                 ex("مِنْ فَضْلِكَ، اُدْرُسِ الْيَوْم.", "Please study today. (to a man)", "اُدْرُسِ"),
             ]),
    ],
    exercises=[
        M("Which is the command “Sit!” to a man?", "اِجْلِسْ", ["تَجْلِس", "يَجْلِس", "اَجْلُسْ"], "Drop the تَـ and add اِ because the present vowel is ِ."),
        M("Which is the command “Write!” to a man?", "اُكْتُبْ", ["اِكْتِبْ", "تَكْتُب", "كَتَبَ"], "The present vowel of تَكْتُب is ُ, so the helping alif has ُ."),
        M("Which is the command “Open!” to a man?", "اِفْتَحْ", ["اُفْتُحْ", "تَفْتَح", "فَتَحَ"], "تَفْتَح has the vowel َ, so the helping alif has ِ."),
        M("Which is the command “Enter!” to a man?", "اُدْخُلْ", ["اِدْخِلْ", "تَدْخُل", "دَخَلَ"], "تَدْخُل has ُ."),
        M("What goes on the last letter of a command to a man?", "a sukūn ْ", ["a ḍamma ُ", "a fatḥa َ", "an extra ن"], "The ending is ْ."),
        M("Which means “Go to school”?", "اِذْهَبْ إِلَى الْمَدْرَسَة", ["تَذْهَب إِلَى الْمَدْرَسَة", "اِذْهَبْ فِي الْمَدْرَسَة", "اُذْهُبْ الْمَدْرَسَة"], "اِذْهَبْ is the command; إِلَى = to."),
        M("Which is polite when you ask a stranger to sit?", "مِنْ فَضْلِكَ، اِجْلِسْ", ["اِجْلِسْ، مَعَ السَّلَامَة", "شُكْرًا، تَجْلِس", "أَهْلًا، جَلَسَ"], "مِنْ فَضْلِكَ = please."),
        F("___ هُنَا.", "اِجْلِسْ", ["تَجْلِس", "جَلَسَ", "اُجْلُسْ"], "Command to a man.", tr="Sit here. (to a man)"),
        F("اُدْخُلْ ___ هُنَا.", "مِنْ", ["إِلَى", "عَلَى", "فِي"], "Come in this way = from here.", tr="Come in this way. (to a man)"),
    ],
    verify=(vv("كتب", "imp", anta="اُكْتُبْ") + vv("دخل", "imp", anta="اُدْخُلْ") + vv("جلس", "imp", anta="اِجْلِسْ")
            + vv("فتح", "imp", anta="اِفْتَحْ") + vv("درس", "imp", anta="اُدْرُسْ") + vv("ذهب", "imp", anta="اِذْهَبْ")
            + vv("كتب", "pres", anta="تَكْتُب") + vv("دخل", "pres", anta="تَدْخُل") + vv("جلس", "pres", anta="تَجْلِس")
            + vv("فتح", "pres", anta="تَفْتَح") + vv("درس", "pres", anta="تَدْرُس") + vv("ذهب", "pres", anta="تَذْهَب")
            + vw("مِنْ فَضْلِكَ")),
)

# ---------------------------------------------------------------------------- 81
L81 = lesson(
    "Commands to a woman and to groups",
    "اُكْتُبِي · اُكْتُبَا · اُكْتُبُوا · اُكْتُبْنَ",
    requires=["كتب", "جلس", "طالب", "معلم", "دخل"],
    cards=[
        card("One command, five addressees",
             "Arabic has a command for a man, a woman, two people, a group of men and a group of women. The endings "
             "are those of the present without the final ن: تَكْتُبِين becomes اُكْتُبِي and تَكْتُبُون becomes "
             "اُكْتُبُوا, while ـْنَ stays. In the men’s group form the ending ـُوا has a silent "
             "alif after the و.",
             tables=[table(["To", "Write!", "Sit!"],
                           [["a man", "اُكْتُبْ", "اِجْلِسْ"], ["a woman", "اُكْتُبِي", "اِجْلِسِي"],
                            ["two people", "اُكْتُبَا", "اِجْلِسَا"], ["a group of men", "اُكْتُبُوا", "اِجْلِسُوا"],
                            ["a group of women", "اُكْتُبْنَ", "اِجْلِسْنَ"]],
                           say=[1, 2], tlit=[1])]),
        card("Choosing the right one",
             "A mixed group of men and women takes the masculine group form. Teachers use the group forms all day.",
             examples=[
                 ex("اِجْلِسِي هُنَا يَا سَارَة.", "Sit here, Sara. (to a woman)", "اِجْلِسِي"),
                 ex("اِجْلِسَا مِنْ فَضْلِكُمَا.", "Please sit. (to two people)", "اِجْلِسَا"),
                 ex("اُدْخُلُوا يَا طُلَّاب.", "Come in, students. (to a group)", "اُدْخُلُوا"),
                 ex("اُكْتُبْنَ أَسْمَاءَكُنَّ.", "Write your names. (to a group of women)", "اُكْتُبْنَ"),
                 ex("اُدْرُسِي الْيَوْم يَا لَيْلَى.", "Study today, Layla. (to a woman)", "اُدْرُسِي"),
             ]),
    ],
    exercises=[
        M("Which is “Write!” to a woman?", "اُكْتُبِي", ["اُكْتُبْ", "اُكْتُبُوا", "اُكْتُبْنَ"], "ـِي marks the woman."),
        M("Which is “Write!” to a group of men?", "اُكْتُبُوا", ["اُكْتُبِي", "اُكْتُبَا", "اُكْتُبْ"], "ـُوا for a group."),
        M("Which is “Write!” to two people?", "اُكْتُبَا", ["اُكْتُبُوا", "اُكْتُبِي", "اُكْتُبْنَ"], "ـَا for two."),
        M("Which is “Sit!” to a group of women?", "اِجْلِسْنَ", ["اِجْلِسُوا", "اِجْلِسِي", "اِجْلِسَا"], "ـْنَ for women."),
        M("Which is “Sit!” to a woman?", "اِجْلِسِي", ["اِجْلِسْ", "اِجْلِسُوا", "اِجْلِسْنَ"], "ـِي."),
        M("A teacher talks to a class of men and women. Which does she use?", "اُدْخُلُوا", ["اُدْخُلِي", "اُدْخُلْنَ", "اُدْخُلَا"], "A mixed group takes the masculine plural."),
        M("Which means “Come in, students!”?", "اُدْخُلُوا يَا طُلَّاب", ["اُدْخُلْ يَا طُلَّاب", "اُدْخُلِي يَا طُلَّاب", "اُدْخُلْنَ يَا طُلَّاب"], "The students are a group."),
        F("اِجْلِسِي ___ سَارَة.", "يَا", ["مِنْ", "فِي", "عَلَى"], "Addressing someone: يَا.", tr="Sit, Sara."),
        F("___ يَا طُلَّاب.", "اُدْخُلُوا", ["اُدْخُلْ", "اُدْخُلِي", "اُدْخُلَا"], "Command to a group.", tr="Come in, students."),
    ],
    verify=(vv("كتب", "imp", anta="اُكْتُبْ", anti="اُكْتُبِي", antuma="اُكْتُبَا", antum="اُكْتُبُوا", antunna="اُكْتُبْنَ")
            + vv("جلس", "imp", anta="اِجْلِسْ", anti="اِجْلِسِي", antuma="اِجْلِسَا", antum="اِجْلِسُوا", antunna="اِجْلِسْنَ")
            + vv("دخل", "imp", antum="اُدْخُلُوا", anti="اُدْخُلِي", antunna="اُدْخُلْنَ", antuma="اُدْخُلَا")
            + vv("درس", "imp", anti="اُدْرُسِي") + vw("أَسْمَاءَكُنَّ", "فَضْلِكُمَا", "سَارَة", "يَا")),
)

# ---------------------------------------------------------------------------- 82
L82 = lesson(
    "Commands you hear every day",
    "اِسْمَعْ · اُنْظُرْ · اِقْرَأْ",
    requires=["سمع", "نظر", "قرأ", "طلب", "كتاب"],
    cards=[
        card("More verbs, same pattern",
             "The same rule works for these verbs. For قَرَأَ the last root letter is a hamza, which sits on an "
             "alif with a sukūn: اِقْرَأْ. Before the ـِي of the feminine it sits on a ي seat: اِقْرَئِي.",
             tables=[table(["English", "Command to a man", "Command to a woman"],
                           [["listen", "اِسْمَعْ", "اِسْمَعِي"], ["look", "اُنْظُرْ", "اُنْظُرِي"],
                            ["read", "اِقْرَأْ", "اِقْرَئِي"], ["ask for / order", "اُطْلُبْ", "اُطْلُبِي"],
                            ["carry", "اِحْمِلْ", "اِحْمِلِي"], ["come back", "اِرْجِعْ", "اِرْجِعِي"]],
                           say=[1, 2], tlit=[1])]),
        card("A class and a home",
             "Before ال the final sukūn of a command takes a short kasra, so the two words run together smoothly: "
             "اِفْتَحِ الْبَاب, اِقْرَأِ الْكِتَاب. This is only a matter of pronunciation.",
             examples=[
                 ex("اِسْمَعْ يَا أَحْمَد.", "Listen, Ahmad. (to a man)", "اِسْمَعْ"),
                 ex("اُنْظُرْ إِلَى الْجَبَل.", "Look at the mountain. (to a man)", "اُنْظُرْ"),
                 ex("اِقْرَأِ الْكِتَاب.", "Read the book. (to a man)", "اِقْرَأِ"),
                 ex("اِفْتَحِ الْبَاب مِنْ فَضْلِكَ.", "Open the door, please. (to a man)", "اِفْتَحِ"),
                 ex("اِحْمِلِي الْحَقِيبَة يَا لَيْلَى.", "Carry the bag, Layla. (to a woman)", "اِحْمِلِي"),
             ]),
    ],
    exercises=[
        M("Which is “Listen!” to a man?", "اِسْمَعْ", ["اُسْمُعْ", "تَسْمَع", "سَمِعَ"], "The present vowel is َ, so the alif has ِ."),
        M("Which is “Look!” to a man?", "اُنْظُرْ", ["اِنْظِرْ", "تَنْظُر", "نَظَرَ"], "The present vowel is ُ."),
        M("Which is “Read!” to a man?", "اِقْرَأْ", ["اُقْرُؤْ", "تَقْرَأ", "قَرَأَ"], "اِقْرَأْ."),
        M("Which is “Carry!” to a woman?", "اِحْمِلِي", ["اِحْمِلْ", "اِحْمِلُوا", "اِحْمِلْنَ"], "ـِي marks a woman."),
        M("Which means “Open the door, please”?", "اِفْتَحِ الْبَاب مِنْ فَضْلِكَ", ["فَتَحَ الْبَاب مِنْ فَضْلِكَ", "تَفْتَح الْبَاب مِنْ فَضْلِكَ", "اِفْتَحِ فِي الْبَاب"], "Command + object."),
        M("Which means “Look at the mountain”?", "اُنْظُرْ إِلَى الْجَبَل", ["اِنْظُرْ فِي الْجَبَل", "نَظَرَ إِلَى الْجَبَل", "اُنْظُرْ مِنَ الْجَبَل"], "نَظَرَ إِلَى = look at."),
        M("What happens to the final sukūn of a command before ال?", "it takes a short kasra", ["it is dropped", "it becomes ḍamma", "nothing"], "اِفْتَحِ الْبَاب."),
        F("اِقْرَأِ ___.", "الْكِتَاب", ["الْبَاب", "الْجَبَل", "الْحَقِيبَة"], "What you read.", tr="Read the book."),
        F("اُنْظُرْ ___ الْجَبَل.", "إِلَى", ["مِنْ", "عَنْ", "مَعَ"], "Look at = اُنْظُرْ إِلَى.", tr="Look at the mountain."),
    ],
    verify=(vv("سمع", "imp", anta="اِسْمَعْ", anti="اِسْمَعِي") + vv("نظر", "imp", anta="اُنْظُرْ", anti="اُنْظُرِي")
            + vv("قرأ", "imp", anta="اِقْرَأْ") + vv("طلب", "imp", anta="اُطْلُبْ", anti="اُطْلُبِي")
            + vv("حمل", "imp", anta="اِحْمِلْ", anti="اِحْمِلِي") + vv("رجع", "imp", anta="اِرْجِعْ", anti="اِرْجِعِي")
            + vw("اِقْرَئِي", "الْحَقِيبَة")),
)

# ---------------------------------------------------------------------------- 83
L83 = lesson(
    "Do not! The negative command",
    "لَا تَدْخُلْ · لَا تَجْلِسُوا",
    requires=["دخل", "جلس", "فتح", "لا", "باب"],
    cards=[
        card("لَا + تَـ",
             "A negative command is not built from the positive one. Use لَا and the present form for “you”, but "
             "with a sukūn at the end instead of the usual ḍamma. The endings for a woman, two people and a group are "
             "the same as in the positive command.",
             tables=[table(["To", "Do not enter!", "Do not sit!"],
                           [["a man", "لَا تَدْخُلْ", "لَا تَجْلِسْ"], ["a woman", "لَا تَدْخُلِي", "لَا تَجْلِسِي"],
                            ["two people", "لَا تَدْخُلَا", "لَا تَجْلِسَا"], ["a group of men", "لَا تَدْخُلُوا", "لَا تَجْلِسُوا"],
                            ["a group of women", "لَا تَدْخُلْنَ", "لَا تَجْلِسْنَ"]],
                           say=[1, 2], tlit=[1])]),
        card("Rules and warnings",
             "Compare: اُدْخُلْ is “Enter!” and لَا تَدْخُلْ is “Do not enter!”",
             examples=[
                 ex("لَا تَفْتَحِ الْبَاب.", "Do not open the door. (to a man)", "لَا تَفْتَحِ"),
                 ex("لَا تَدْخُلْ هُنَا.", "Do not come in here. (to a man)", "لَا تَدْخُلْ"),
                 ex("لَا تَجْلِسِي هُنَاك.", "Do not sit over there. (to a woman)", "لَا تَجْلِسِي"),
                 ex("لَا تَذْهَبُوا إِلَى الْجَبَل الْيَوْم.", "Do not go to the mountain today. (to a group)", "لَا تَذْهَبُوا"),
                 ex("لَا تَكْتُبْ هُنَا، اُكْتُبْ هُنَاك.", "Do not write here; write there. (to a man)", "لَا تَكْتُبْ"),
             ]),
    ],
    exercises=[
        M("Which is “Do not enter!” to a man?", "لَا تَدْخُلْ", ["اُدْخُلْ", "لَا يَدْخُلْ", "لَيْسَ تَدْخُلْ"], "لَا + تَـ + sukūn."),
        M("Which is “Do not sit!” to a woman?", "لَا تَجْلِسِي", ["لَا تَجْلِسْ", "لَا تَجْلِسُوا", "اِجْلِسِي"], "ـِي."),
        M("Which is “Do not sit!” to a group of men?", "لَا تَجْلِسُوا", ["لَا تَجْلِسِي", "لَا تَجْلِسَا", "اِجْلِسُوا"], "ـُوا."),
        M("Which is “Do not go!” to a man?", "لَا تَذْهَبْ", ["اِذْهَبْ", "لَا اِذْهَبْ", "لَا يَذْهَبْ"], "لَا تَذْهَبْ."),
        M("Which word is in front of a negative command?", "لَا", ["لَيْسَ", "هَلْ", "مَا"], "لَا."),
        M("Which means “Do not open the door”?", "لَا تَفْتَحِ الْبَاب", ["اِفْتَحِ الْبَاب", "لَا يَفْتَحُ الْبَاب", "لَيْسَ تَفْتَحِ الْبَاب"], "لَا تَفْتَحِ."),
        M("Which is the negative command of اُدْخُلْ؟", "لَا تَدْخُلْ", ["اُخْرُجْ", "تَدْخُل", "دَخَلَ"], "Negative command."),
        F("___ تَدْخُلْ هُنَا.", "لَا", ["لَيْسَ", "هَلْ", "مَا"], "Negative command.", tr="Do not come in here."),
        F("لَا ___ هُنَاك.", "تَجْلِسِي", ["اِجْلِسِي", "تَجْلِسِينَ", "جَلَسَتْ"], "To a woman.", tr="Do not sit over there."),
    ],
    verify=(vv("دخل", "neg", anta="لَا تَدْخُلْ", anti="لَا تَدْخُلِي", antuma="لَا تَدْخُلَا", antum="لَا تَدْخُلُوا", antunna="لَا تَدْخُلْنَ")
            + vv("جلس", "neg", anta="لَا تَجْلِسْ", anti="لَا تَجْلِسِي", antuma="لَا تَجْلِسَا", antum="لَا تَجْلِسُوا", antunna="لَا تَجْلِسْنَ")
            + vv("فتح", "neg", anta="لَا تَفْتَحْ") + vv("ذهب", "neg", anta="لَا تَذْهَبْ", antum="لَا تَذْهَبُوا")
            + vv("كتب", "neg", anta="لَا تَكْتُبْ") + vw("هُنَاك")),
)

# ---------------------------------------------------------------------------- 84
L84 = lesson(
    "To me, to you: لِـ with endings",
    "لِي · لَكَ · لَهُ · لَهَا · لَنَا",
    requires=["لي", "عند", "كتاب", "أخ", "بيت"],
    cards=[
        card("The preposition لِـ",
             "لِـ means “to” or “for”. When a pronoun follows it, the pronoun is not a separate word. It is a short "
             "ending joined to the preposition. Arabic uses لِـ plus an ending to say “I have”: لِي أَخ, literally "
             "“to me a brother”.",
             tables=[table(["English", "Arabic"],
                           [["to me, for me", "لِي"], ["to you (man)", "لَكَ"], ["to you (woman)", "لَكِ"],
                            ["to him", "لَهُ"], ["to her", "لَهَا"], ["to us", "لَنَا"],
                            ["to you (group)", "لَكُم"], ["to them (men)", "لَهُم"], ["to them (women)", "لَهُنَّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Having and giving",
             "To say “I do not have”, put لَيْسَ in front: لَيْسَ لِي أَخ. The thing you have comes after, with no ال.",
             examples=[
                 ex("لِي أَخ وَاحِد.", "I have one brother.", "لِي"),
                 ex("لَهَا أُخْت فِي الْمَدِينَة.", "She has a sister in the city.", "لَهَا"),
                 ex("لَنَا بَيْت كَبِير.", "We have a big house.", "لَنَا"),
                 ex("هَذَا الْمِفْتَاح لِي، وَهَذَا الْمِفْتَاح لَكَ.", "This key is for me, and this key is for you.", "لِي"),
                 ex("لَيْسَ لِي أَخ.", "I do not have a brother.", "لِي"),
             ]),
    ],
    exercises=[
        M("Which means “to me” or “I have”?", "لِي", ["لَكَ", "لَهُ", "لَنَا"], "ي = me."),
        M("Which means “to her”?", "لَهَا", ["لَهُ", "لَكِ", "لَهُم"], "ـهَا = her."),
        M("Which means “to you (woman)”?", "لَكِ", ["لَكَ", "لَكُم", "لَهَا"], "ـكِ for a woman."),
        M("Which means “to us”?", "لَنَا", ["لِي", "لَهُم", "لَكُم"], "ـنَا = us."),
        M("Which means “She has a sister in the city”?", "لَهَا أُخْت فِي الْمَدِينَة", ["لَهُ أُخْت فِي الْمَدِينَة", "لِي أُخْت فِي الْمَدِينَة", "لَهَا أَخ فِي الْمَدِينَة"], "لَهَا = she has."),
        M("Which means “We have a big house”?", "لَنَا بَيْت كَبِير", ["لِي بَيْت كَبِير", "لَهُم بَيْت كَبِير", "لَنَا بَيْتَان"], "لَنَا."),
        M("Which means “I do not have a brother”?", "لَيْسَ لِي أَخ", ["لَا لِي أَخ", "لَيْسَ أَخ لِي", "لَيْسَتْ لِي أَخ"], "لَيْسَ + لِي."),
        F("___ أَخ وَاحِد.", "لِي", ["لَكَ", "لَهَا", "لَنَا"], "I have one brother.", tr="I have one brother."),
        F("هَذَا الْمِفْتَاح ___ .", "لَكَ", ["لِي", "لَهَا", "لَنَا"], "Pick the ending for “you”.", tr="This key is for you."),
    ],
    verify=vw("لِي", "لَكَ", "لَكِ", "لَهُ", "لَهَا", "لَنَا", "لَكُم", "لَهُم", "لَهُنَّ", "أُخْت", "أَخ", "الْمِفْتَاح"),
)

# ---------------------------------------------------------------------------- 85
L85 = lesson(
    "I have: عِنْدِي and مَعِي",
    "هَلْ عِنْدَكَ سَيَّارَة؟ · مَعِي هَاتِف",
    requires=["عند", "مع", "سيارة", "هاتف", "وقت"],
    cards=[
        card("عِنْدَ and مَعَ with endings",
             "عِنْدَ means “at”, and with an ending it is the usual way to say “have”: عِنْدِي سَيَّارَة. مَعَ means "
             "“with”, and with an ending it says that you have something on you right now: مَعِي هَاتِف. The "
             "endings are the same as in the last lesson. عِنْدَ and مَعَ keep their final fatḥa (عِنْدَكَ, مَعَهُ), "
             "except before ـِي, “me”: عِنْدِي, مَعِي.",
             tables=[table(["English", "عِنْدَ (have)", "مَعَ (with)"],
                           [["I", "عِنْدِي", "مَعِي"], ["you (man)", "عِنْدَكَ", "مَعَكَ"], ["you (woman)", "عِنْدَكِ", "مَعَكِ"],
                            ["he", "عِنْدَهُ", "مَعَهُ"], ["she", "عِنْدَهَا", "مَعَهَا"], ["we", "عِنْدَنَا", "مَعَنَا"],
                            ["you (group)", "عِنْدَكُم", "مَعَكُم"], ["they (men)", "عِنْدَهُم", "مَعَهُم"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("Questions and answers",
             "To answer no, use لَيْسَ: لَيْسَ عِنْدِي وَقْت.",
             examples=[
                 ex("هَلْ عِنْدَكَ سَيَّارَة؟", "Do you have a car? (to a man)", "عِنْدَكَ"),
                 ex("نَعَمْ، عِنْدِي سَيَّارَة.", "Yes, I have a car.", "عِنْدِي"),
                 ex("لَا، لَيْسَ عِنْدِي سَيَّارَة.", "No, I do not have a car.", "عِنْدِي"),
                 ex("هَلْ مَعَكِ هَاتِف؟", "Do you have a phone with you? (to a woman)", "مَعَكِ"),
                 ex("لَيْسَ عِنْدِي وَقْت الْيَوْم.", "I do not have time today.", "عِنْدِي"),
                 ex("هُوَ مَعَهَا فِي الْبَيْت.", "He is with her in the house.", "مَعَهَا"),
             ]),
    ],
    exercises=[
        M("Which means “I have a car”?", "عِنْدِي سَيَّارَة", ["لَيْسَ عِنْدِي سَيَّارَة", "عِنْدَهُ سَيَّارَة", "عِنْدَنَا سَيَّارَة"], "عِنْدِي."),
        M("Which means “Do you (man) have a car?”", "هَلْ عِنْدَكَ سَيَّارَة؟", ["هَلْ عِنْدَكِ سَيَّارَة؟", "هَلْ عِنْدِي سَيَّارَة؟", "هَلْ عِنْدَهَا سَيَّارَة؟"], "ـكَ for a man."),
        M("Which means “Do you (woman) have a phone with you?”", "هَلْ مَعَكِ هَاتِف؟", ["هَلْ مَعَكَ هَاتِف؟", "هَلْ مَعِي هَاتِف؟", "هَلْ مَعَهُ هَاتِف؟"], "ـكِ for a woman."),
        M("Which means “We have a house”?", "عِنْدَنَا بَيْت", ["عِنْدِي بَيْت", "عِنْدَهُم بَيْت", "مَعَنَا بَيْتَان"], "عِنْدَنَا."),
        M("Which says that you have no time?", "لَيْسَ عِنْدِي وَقْت", ["لَا عِنْدِي وَقْت", "عِنْدِي لَيْسَ وَقْت", "لَيْسَ وَقْت عِنْدِي"], "لَيْسَ + عِنْدِي."),
        M("Which is best when your phone is in your pocket right now?", "مَعِي هَاتِف", ["لَنَا هَاتِف", "عِنْدَهُ هَاتِف", "لَيْسَ عِنْدِي هَاتِف"], "مَعِي = on me."),
        M("Which means “He is with her in the house”?", "هُوَ مَعَهَا فِي الْبَيْت", ["هُوَ مَعَهُ فِي الْبَيْت", "هِيَ مَعَهُ فِي الْبَيْت", "هُوَ عِنْدِي فِي الْبَيْت"], "مَعَهَا = with her."),
        F("هَلْ ___ هَاتِف؟", "مَعَكِ", ["مَعِي", "مَعَهُ", "مَعَنَا"], "Asking a woman.", tr="Do you have a phone with you? (to a woman)"),
        F("لَا، لَيْسَ ___ سَيَّارَة.", "عِنْدِي", ["عِنْدَكَ", "عِنْدَهَا", "عِنْدَنَا"], "I do not have.", tr="No, I do not have a car."),
    ],
    verify=vw("عِنْدِي", "عِنْدَكَ", "عِنْدَكِ", "عِنْدَهُ", "عِنْدَهَا", "عِنْدَنَا", "عِنْدَكُم", "عِنْدَهُم",
              "مَعِي", "مَعَكَ", "مَعَكِ", "مَعَهُ", "مَعَهَا", "مَعَنَا", "مَعَكُم", "مَعَهُم", "هَاتِف", "وَقْت"),
)

# ---------------------------------------------------------------------------- 86
L86 = lesson(
    "More prepositions with endings",
    "فِيهِ · مِنْهَا · إِلَيْكَ · عَلَيْهِ · بِهَا",
    requires=["في", "من", "إلى", "على", "مع"],
    cards=[
        card("بِـ, فِي and مِنْ",
             "The same endings attach to every preposition. Three things change: after ِ or ـيْ the pronoun ـهُ becomes "
             "ـهِ (and ـهُم becomes ـهِم), “me” after فِي is فِيَّ, and “me” after مِنْ is مِنِّي, with a doubled ن.",
             tables=[table(["English", "بِـ", "فِي", "مِنْ"],
                           [["me", "بِي", "فِيَّ", "مِنِّي"], ["you (man)", "بِكَ", "فِيكَ", "مِنْكَ"],
                            ["you (woman)", "بِكِ", "فِيكِ", "مِنْكِ"], ["him", "بِهِ", "فِيهِ", "مِنْهُ"],
                            ["her", "بِهَا", "فِيهَا", "مِنْهَا"], ["us", "بِنَا", "فِينَا", "مِنَّا"],
                            ["you (group)", "بِكُم", "فِيكُم", "مِنْكُم"], ["them (men)", "بِهِم", "فِيهِم", "مِنْهُم"]],
                           say=[1, 2, 3], tlit=[1], gloss=False)]),
        card("إِلَى and عَلَى",
             "The final ى of these two becomes ـَيْ in front of an ending, and “me” is ـَيَّ.",
             tables=[table(["English", "إِلَى", "عَلَى"],
                           [["me", "إِلَيَّ", "عَلَيَّ"], ["you (man)", "إِلَيْكَ", "عَلَيْكَ"],
                            ["you (woman)", "إِلَيْكِ", "عَلَيْكِ"], ["him", "إِلَيْهِ", "عَلَيْهِ"],
                            ["her", "إِلَيْهَا", "عَلَيْهَا"], ["us", "إِلَيْنَا", "عَلَيْنَا"],
                            ["you (group)", "إِلَيْكُم", "عَلَيْكُم"], ["them (men)", "إِلَيْهِم", "عَلَيْهِم"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("In sentences",
             "The ending refers back to a noun that has already been named.",
             examples=[
                 ex("هَذَا بَيْت. أَنَا أَسْكُن فِيهِ.", "This is a house. I live in it.", "فِيهِ"),
                 ex("هَذِه مَدْرَسَة. أَنَا أَدْرُس فِيهَا.", "This is a school. I study in it.", "فِيهَا"),
                 ex("هَذِه هِيَ الطَّاوِلَة. الْكِتَاب عَلَيْهَا.", "This is the table. The book is on it.", "عَلَيْهَا"),
                 ex("هَذَا صَدِيقِي. أَنَا أَكْتُب إِلَيْهِ.", "This is my friend. I write to him.", "إِلَيْهِ"),
                 ex("هَذِه رِسَالَة مِنْهَا.", "This is a letter from her.", "مِنْهَا"),
                 ex("السَّلَام عَلَيْكُم.", "Peace be upon you. (to a group)", "عَلَيْكُم"),
             ]),
    ],
    exercises=[
        M("Which means “in it” (a masculine thing)?", "فِيهِ", ["فِيهَا", "فِيكَ", "فِينَا"], "ـهِ = him/it."),
        M("Which means “on it” (a feminine thing)?", "عَلَيْهَا", ["عَلَيْهِ", "عَلَيْكَ", "عَلَيَّ"], "ـهَا = her/it."),
        M("Which means “from me”?", "مِنِّي", ["مِنْكَ", "مِنْهُ", "مِنَّا"], "مِنِّي has a doubled ن."),
        M("Which means “to you (man)”, after إِلَى?", "إِلَيْكَ", ["إِلَيْهِ", "إِلَيْكِ", "إِلَيْنَا"], "ـكَ for a man."),
        M("Which means “with it (feminine)”, after بِـ?", "بِهَا", ["بِهِ", "بِكَ", "بِي"], "بِـ + هَا."),
        M("Which means “from us”?", "مِنَّا", ["مِنِّي", "مِنْكُم", "مِنْهُم"], "مِنَّا also has a doubled ن."),
        M("Which means “This is the table. The book is on it.”?", "هَذِه هِيَ الطَّاوِلَة. الْكِتَاب عَلَيْهَا", ["هَذِه هِيَ الطَّاوِلَة. الْكِتَاب عَلَيْهِ", "هَذِه هِيَ الطَّاوِلَة. الْكِتَاب فِيهَا", "هَذَا هُوَ الْبَاب. الْكِتَاب عَلَيْهَا"], "الطَّاوِلَة is feminine."),
        M("Which means “Peace be upon you (group)”?", "السَّلَام عَلَيْكُم", ["السَّلَام عَلَيْهِم", "السَّلَام عَلَيْكَ", "السَّلَام مِنْكُم"], "عَلَيْكُم."),
        F("هَذَا بَيْت. أَنَا أَسْكُن ___.", "فِيهِ", ["فِيهَا", "عَلَيْهِ", "إِلَيْهِ"], "Live in it.", tr="This is a house. I live in it."),
        F("هَذِه رِسَالَة ___.", "مِنْهَا", ["مِنْهُ", "مِنْكَ", "مِنِّي"], "From her.", tr="This is a letter from her."),
    ],
    verify=vw("بِي", "فِيَّ", "مِنِّي", "بِكَ", "فِيكَ", "مِنْكَ", "بِكِ", "فِيكِ", "مِنْكِ", "بِهِ", "فِيهِ", "مِنْهُ",
              "بِهَا", "فِيهَا", "مِنْهَا", "بِنَا", "فِينَا", "مِنَّا", "بِكُم", "فِيكُم", "مِنْكُم", "بِهِم", "فِيهِم", "مِنْهُم",
              "إِلَيَّ", "عَلَيَّ", "إِلَيْكَ", "عَلَيْكَ", "إِلَيْكِ", "عَلَيْكِ", "إِلَيْهِ", "عَلَيْهِ", "إِلَيْهَا", "عَلَيْهَا",
              "إِلَيْنَا", "عَلَيْنَا", "إِلَيْكُم", "عَلَيْكُم", "إِلَيْهِم", "عَلَيْهِم", "رِسَالَة", "صَدِيقِي"),
)

# ---------------------------------------------------------------------------- 87
L87 = lesson(
    "In front of me, behind you",
    "أَمَامِي · خَلْفَكَ · بِجَانِبِهَا",
    requires=["أمام", "خلف", "فوق", "تحت", "بين"],
    cards=[
        card("Position words with endings",
             "The position words you know take the endings too. Because they are nouns in disguise, they keep their "
             "vowels in front of an ending: أَمَامَ becomes أَمَامِي, أَمَامَكَ, أَمَامَهُ. The ending “me” is ـِي, which "
             "forces a kasra on the letter before it, so أَمَامَ turns into أَمَامِي.",
             tables=[table(["English", "Word", "+ me", "+ him", "+ us"],
                           [["in front of", "أَمَامَ", "أَمَامِي", "أَمَامَهُ", "أَمَامَنَا"],
                            ["behind", "خَلْفَ", "خَلْفِي", "خَلْفَهُ", "خَلْفَنَا"],
                            ["above", "فَوْقَ", "فَوْقِي", "فَوْقَهُ", "فَوْقَنَا"],
                            ["under", "تَحْتَ", "تَحْتِي", "تَحْتَهُ", "تَحْتَنَا"],
                            ["next to", "بِجَانِبِ", "بِجَانِبِي", "بِجَانِبِهِ", "بِجَانِبِنَا"],
                            ["after", "بَعْدَ", "بَعْدِي", "بَعْدَهُ", "بَعْدَنَا"]],
                           say=[1, 2, 3, 4], tlit=[1], gloss=False)]),
        card("Where is it?",
             "بَيْنَ means “between”. It needs two things: بَيْنِي وَبَيْنَكَ, “between me and you”.",
             examples=[
                 ex("الْمُدَرِّس أَمَامَنَا وَالْبَاب خَلْفَنَا.", "The teacher is in front of us and the door is behind us.", "أَمَامَنَا"),
                 ex("الْكِتَاب فَوْقَ الطَّاوِلَة، وَالْحَقِيبَة تَحْتَهَا.", "The book is on top of the table, and the bag is under it.", "تَحْتَهَا"),
                 ex("بَيْتِي بِجَانِبِ الْمَدْرَسَة.", "My house is next to the school."),
                 ex("جَلَسَ أَحْمَد بِجَانِبِي.", "Ahmad sat next to me.", "بِجَانِبِي"),
                 ex("بَيْنِي وَبَيْنَكَ جَبَل.", "Between me and you is a mountain.", "بَيْنِي"),
             ]),
    ],
    exercises=[
        M("Which means “in front of me”?", "أَمَامِي", ["خَلْفِي", "فَوْقِي", "تَحْتِي"], "أَمَام = in front of."),
        M("Which means “behind us”?", "خَلْفَنَا", ["أَمَامَنَا", "تَحْتَنَا", "خَلْفَهُ"], "خَلْف + نَا."),
        M("Which means “under it (feminine)”?", "تَحْتَهَا", ["تَحْتَهُ", "فَوْقَهَا", "تَحْتِي"], "تَحْت + هَا."),
        M("Which means “next to me”?", "بِجَانِبِي", ["بِجَانِبِهِ", "بَعْدِي", "بَيْنِي"], "بِجَانِب + ي."),
        M("Which means “between me and you”?", "بَيْنِي وَبَيْنَكَ", ["بَيْنِي وَبَيْنَ", "بَيْنِي فَقَط", "مَعِي وَمَعَكَ"], "With pronouns, بَيْنَ is repeated before each."),
        M("Which means “The teacher is in front of us”?", "الْمُدَرِّس أَمَامَنَا", ["الْمُدَرِّس خَلْفَنَا", "الْمُدَرِّس أَمَامَهُ", "الْمُدَرِّس أَمَامِي"], "أَمَامَنَا."),
        M("Which means “The bag is under it”, speaking of the table?", "الْحَقِيبَة تَحْتَهَا", ["الْحَقِيبَة فَوْقَهَا", "الْحَقِيبَة تَحْتَهُ", "الْحَقِيبَة تَحْتَنَا"], "The table is feminine."),
        F("الْبَاب ___ .", "خَلْفَنَا", ["أَمَامَنَا", "فَوْقَنَا", "بَيْنَنَا"], "Behind us.", tr="The door is behind us."),
        F("جَلَسَ أَحْمَد ___ .", "بِجَانِبِي", ["بِجَانِبِهِ", "تَحْتِي", "مِنِّي"], "Next to me.", tr="Ahmad sat next to me."),
    ],
    verify=vw("أَمَامِي", "أَمَامَهُ", "أَمَامَنَا", "خَلْفِي", "خَلْفَهُ", "خَلْفَنَا", "فَوْقِي", "فَوْقَهُ", "فَوْقَنَا",
              "تَحْتِي", "تَحْتَهُ", "تَحْتَنَا", "تَحْتَهَا", "بِجَانِبِي", "بِجَانِبِهِ", "بِجَانِبِنَا", "بَعْدِي", "بَعْدَهُ",
              "بَعْدَنَا", "بَيْنِي", "بَيْنَكَ", "جَلَسَ", "الْمُدَرِّس") + vv("جلس", "past", huwa="جَلَسَ"),
)

# ---------------------------------------------------------------------------- 88
L88 = lesson(
    "Where is my key?",
    "أَيْنَ مِفْتَاحِي؟ · هُوَ فِيهَا!",
    requires=["مفتاح", "حقيبة", "طاولة", "هاتف", "أين"],
    cards=[
        card("A short conversation",
             "Layla cannot find her key. Notice each ending and what it points to.",
             examples=[
                 ex("لَيْلَى: أَيْنَ مِفْتَاحِي؟", "Layla: Where is my key?"),
                 ex("أَحْمَد: هُوَ عَلَى الطَّاوِلَة.", "Ahmad: It is on the table."),
                 ex("لَيْلَى: لَيْسَ عَلَيْهَا.", "Layla: It is not on it."),
                 ex("أَحْمَد: هَلْ هُوَ مَعَكِ؟", "Ahmad: Do you have it with you?"),
                 ex("لَيْلَى: لَا، لَيْسَ مَعِي.", "Layla: No, I do not have it."),
                 ex("أَحْمَد: اُنْظُرِي فِي الْحَقِيبَة.", "Ahmad: Look in the bag."),
                 ex("لَيْلَى: نَعَمْ! هُوَ فِيهَا. شُكْرًا لَكَ.", "Layla: Yes! It is in it. Thank you."),
             ]),
    ],
    exercises=[
        M("Layla says «أَيْنَ مِفْتَاحِي؟». What is she looking for?", "her key", ["her phone", "her bag", "her book"], "مِفْتَاح = key."),
        M("Ahmad says «هُوَ عَلَى الطَّاوِلَة». Where is the key, he thinks?", "on the table", ["in the bag", "under the table", "at school"], "عَلَى = on."),
        M("«لَيْسَ عَلَيْهَا». What does عَلَيْهَا stand for?", "the table", ["the key", "Layla", "Ahmad"], "طَاوِلَة is feminine, so هَا."),
        M("«هَلْ هُوَ مَعَكِ؟». Who is Ahmad speaking to?", "a woman", ["a man", "a group", "himself"], "مَعَكِ has ـكِ."),
        M("«لَيْسَ مَعِي». What does Layla mean?", "I do not have it with me", ["He does not have it", "It is behind me", "It is for me"], "مَعِي = with me."),
        M("«اُنْظُرِي فِي الْحَقِيبَة». What does Ahmad ask her to do?", "look in the bag", ["open the door", "write a letter", "sit down"], "اُنْظُرِي is a command to a woman."),
        M("«هُوَ فِيهَا». What does فِيهَا stand for?", "the bag", ["the table", "Layla", "the key"], "حَقِيبَة is feminine."),
        F("اُنْظُرِي ___ الْحَقِيبَة.", "فِي", ["عَلَى", "مِنْ", "إِلَى"], "In the bag.", tr="Look in the bag."),
        F("شُكْرًا ___ .", "لَكَ", ["لَكِ", "لِي", "لَهُ"], "Layla thanks Ahmad, a man.", tr="Thank you. (to a man)"),
    ],
    verify=vw("مِفْتَاحِي", "لَيْلَى", "أَحْمَد", "اُنْظُرِي", "الْحَقِيبَة") + vv("نظر", "imp", anti="اُنْظُرِي"),
)

# ---------------------------------------------------------------------------- 89
L89 = lesson(
    "I must: يَجِب أَنْ",
    "يَجِب أَنْ أَدْرُس · يَجِب أَنْ نَذْهَب",
    requires=["درس", "ذهب", "مدرسة", "واجب", "يوم"],
    cards=[
        card("يَجِب + أَنْ + verb",
             "يَجِب means “it is necessary”. It never changes. Put أَنْ after it (“that”), and then the present "
             "verb with the person you mean. The verb carries the person, so the same sentence works for I, you, "
             "he and she.",
             tables=[table(["English", "Arabic"],
                           [["I must study", "يَجِب أَنْ أَدْرُس"], ["you (man) must study", "يَجِب أَنْ تَدْرُس"],
                            ["he must study", "يَجِب أَنْ يَدْرُس"], ["she must study", "يَجِب أَنْ تَدْرُس"],
                            ["we must study", "يَجِب أَنْ نَدْرُس"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Must and must not",
             "To say “must not”, join أَنْ and لَا into أَلَّا: يَجِب أَلَّا تَدْخُل. Here يَجِب is followed by "
             "أَنْ and a verb, so the sentence has this three-part shape.",
             examples=[
                 ex("يَجِب أَنْ أَدْرُس الْيَوْم.", "I must study today.", "يَجِب أَنْ أَدْرُس"),
                 ex("يَجِب أَنْ تَذْهَب إِلَى الْمَدْرَسَة.", "You must go to school. (to a man)", "يَجِب أَنْ تَذْهَب"),
                 ex("يَجِب أَنْ نَكْتُب الْوَاجِب.", "We must write the homework.", "يَجِب أَنْ نَكْتُب"),
                 ex("يَجِب أَنْ تَرْجِع لَيْلَى إِلَى الْبَيْت.", "Layla must go back home.", "يَجِب أَنْ تَرْجِع"),
                 ex("يَجِب أَلَّا تَدْخُل هُنَا.", "You must not come in here. (to a man)", "يَجِب أَلَّا تَدْخُل"),
             ]),
    ],
    exercises=[
        M("Which means “I must study”?", "يَجِب أَنْ أَدْرُس", ["يَجِب أَنْ تَدْرُس", "أَنْ يَجِب أَدْرُس", "أَدْرُس يَجِب أَنْ"], "يَجِب + أَنْ + أَدْرُس."),
        M("Which means “We must write”?", "يَجِب أَنْ نَكْتُب", ["يَجِب أَنْ أَكْتُب", "يَجِب أَنْ يَكْتُب", "يَجِبُونَ أَنْ نَكْتُب"], "نَـ = we."),
        M("Which means “She must go back”?", "يَجِب أَنْ تَرْجِع", ["يَجِب أَنْ يَرْجِع", "يَجِب أَنْ أَرْجِع", "تَجِب أَنْ تَرْجِع"], "تَـ = she. يَجِب does not change."),
        M("Which means “He must study”?", "يَجِب أَنْ يَدْرُس", ["يَجِب أَنْ تَدْرُس", "يَجِب أَنْ نَدْرُس", "يَجِب أَنْ أَدْرُس"], "يَـ = he."),
        M("Which means “You (man) must not come in”?", "يَجِب أَلَّا تَدْخُل", ["يَجِب أَنْ تَدْخُل", "لَيْسَ يَجِب أَنْ تَدْخُل", "لَا تَدْخُل يَجِب"], "أَلَّا = أَنْ + لَا."),
        M("Which part of the sentence changes with the person?", "the verb after أَنْ", ["يَجِب", "أَنْ", "none of them"], "يَجِب never changes."),
        M("Which means “We must go to school”?", "يَجِب أَنْ نَذْهَب إِلَى الْمَدْرَسَة", ["يَجِب أَنْ أَذْهَب إِلَى الْمَدْرَسَة", "يَجِب أَنْ تَذْهَب إِلَى الْمَدْرَسَة", "يَجِب أَنْ نَذْهَب فِي الْمَدْرَسَة"], "نَذْهَب إِلَى."),
        F("___ أَنْ أَدْرُس الْيَوْم.", "يَجِب", ["لَيْسَ", "هَلْ", "مَعَ"], "It is necessary.", tr="I must study today."),
        F("يَجِب أَنْ ___ الْوَاجِب.", "نَكْتُب", ["كَتَبَ", "اُكْتُبْ", "كِتَاب"], "A present verb with نَـ.", tr="We must write the homework."),
    ],
    verify=(vv("درس", "pres", ana="أَدْرُس", anta="تَدْرُس", huwa="يَدْرُس", hiya="تَدْرُس", nahnu="نَدْرُس")
            + vv("كتب", "pres", nahnu="نَكْتُب") + vv("ذهب", "pres", anta="تَذْهَب", nahnu="نَذْهَب")
            + vv("رجع", "pres", hiya="تَرْجِع") + vv("دخل", "pres", anta="تَدْخُل") + vw("يَجِب", "أَنْ", "الْوَاجِب")),
)

# ---------------------------------------------------------------------------- 90
L90 = lesson(
    "After أَنْ: the ن falls away",
    "أَنْ تَكْتُبِي · أَنْ يَكْتُبُوا",
    requires=["كتب", "طالب", "دخل", "جلس", "معلم"],
    cards=[
        card("Dropping the final ن",
             "After أَنْ the verb loses a final ن. Endings that finish in ن (ـِينَ, ـَانِ, ـُونَ) lose that ن. "
             "The ـُوا ending gets a silent alif after the و. The feminine plural ـْنَ keeps its ن. The forms with no ending look the "
             "same in our spelling (in full vowelling they end in fatḥa: أَنْ أَكْتُبَ).",
             tables=[table(["Person", "Normal present", "After أَنْ"],
                           [["you (woman)", "تَكْتُبِين", "أَنْ تَكْتُبِي"], ["you two", "تَكْتُبَان", "أَنْ تَكْتُبَا"],
                            ["you (men)", "تَكْتُبُون", "أَنْ تَكْتُبُوا"], ["they (men)", "يَكْتُبُون", "أَنْ يَكْتُبُوا"],
                            ["they two", "يَكْتُبَان", "أَنْ يَكْتُبَا"], ["they (women)", "يَكْتُبْنَ", "أَنْ يَكْتُبْنَ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Other verbs that take أَنْ",
             "The same rule applies after أُرِيد أَنْ (“I want to”) and after any other word that is followed by أَنْ.",
             examples=[
                 ex("يَجِب أَنْ تَكْتُبِي الْوَاجِب يَا لَيْلَى.", "You must write the homework, Layla.", "تَكْتُبِي"),
                 ex("يَجِب أَنْ تَدْرُسُوا يَا طُلَّاب.", "You must study, students.", "تَدْرُسُوا"),
                 ex("يَجِب أَنْ يَدْخُلَا الْآن.", "The two of them must come in now.", "يَدْخُلَا"),
                 ex("يَجِب أَنْ يَذْهَبُوا إِلَى الْمَدْرَسَة.", "They must go to school.", "يَذْهَبُوا"),
                 ex("أُرِيد أَنْ أَجْلِس هُنَا.", "I want to sit here.", "أُرِيد أَنْ"),
                 ex("يَجِب أَنْ يَجْلِسْنَ هُنَا.", "They (women) must sit here.", "يَجْلِسْنَ"),
             ]),
    ],
    exercises=[
        M("Which is correct after أَنْ for “you (woman) write”?", "أَنْ تَكْتُبِي", ["أَنْ تَكْتُبِين", "أَنْ تَكْتُب", "أَنْ تَكْتُبْنَ"], "The ن of ـِين is dropped."),
        M("Which is correct after أَنْ for “they (men) go”?", "أَنْ يَذْهَبُوا", ["أَنْ يَذْهَبُون", "أَنْ يَذْهَبْنَ", "أَنْ يَذْهَبَان"], "ـُون → ـُوا."),
        M("Which is correct after أَنْ for “the two of them enter”?", "أَنْ يَدْخُلَا", ["أَنْ يَدْخُلَان", "أَنْ يَدْخُلُوا", "أَنْ يَدْخُل"], "ـَان → ـَا."),
        M("Which keeps its ن after أَنْ?", "يَجْلِسْنَ", ["تَجْلِسُونَ", "تَجْلِسِينَ", "يَجْلِسَانِ"], "The feminine plural does not change."),
        M("Which means “You (students) must study”?", "يَجِب أَنْ تَدْرُسُوا", ["يَجِب أَنْ تَدْرُسُون", "يَجِب أَنْ تَدْرُسِي", "يَجِب أَنْ يَدْرُسُوا"], "تَدْرُسُوا is for a group."),
        M("Which means “I want to sit here”?", "أُرِيد أَنْ أَجْلِس هُنَا", ["أُرِيد أَنْ جَلَسَ هُنَا", "أُرِيد أَنْ اِجْلِسْ هُنَا", "أَنْ أُرِيد أَجْلِس هُنَا"], "أُرِيد أَنْ + present."),
        M("In تَكْتُبُوا, why is there an alif after the و?", "it is only a spelling mark and is not pronounced", ["it marks a woman", "it makes the verb past", "it is pronounced as a long vowel"], "The silent alif is written after the plural و."),
        F("يَجِب أَنْ ___ الْوَاجِب يَا لَيْلَى.", "تَكْتُبِي", ["تَكْتُبِين", "تَكْتُب", "تَكْتُبُوا"], "To a woman.", tr="You must write the homework, Layla."),
        F("يَجِب أَنْ ___ يَا طُلَّاب.", "تَدْرُسُوا", ["تَدْرُسُون", "تَدْرُسِي", "تَدْرُسَا"], "To a group.", tr="You must study, students."),
    ],
    verify=(vv("كتب", "pres", anti="تَكْتُبِين", antuma="تَكْتُبَان", antum="تَكْتُبُون", hum="يَكْتُبُون", huma_m="يَكْتُبَان", hunna="يَكْتُبْنَ")
            + vv("كتب", "sub", anti="تَكْتُبِي", antuma="تَكْتُبَا", antum="تَكْتُبُوا", hum="يَكْتُبُوا", huma_m="يَكْتُبَا", hunna="يَكْتُبْنَ")
            + vv("درس", "sub", antum="تَدْرُسُوا") + vv("دخل", "sub", huma_m="يَدْخُلَا") + vv("ذهب", "sub", hum="يَذْهَبُوا")
            + vv("جلس", "sub", ana="أَجْلِس", hunna="يَجْلِسْنَ") + vw("أُرِيد", "الْآن", "طُلَّاب")),
)

# ---------------------------------------------------------------------------- 91
L91 = lesson(
    "I have to: عَلَيَّ أَنْ",
    "عَلَيَّ أَنْ أَغْسِل · لَيْسَ عَلَيْكَ أَنْ تَذْهَب",
    requires=["على", "درس", "غسل", "بيت", "ذهب"],
    cards=[
        card("عَلَى + ending + أَنْ",
             "A second way to say “must” uses عَلَى with an ending, which you met earlier in this unit: عَلَيَّ أَنْ أَدْرُس, "
             "literally “upon me, that I study”. The person is the ending on عَلَى, and the verb after أَنْ agrees "
             "with it.",
             tables=[table(["English", "Arabic"],
                           [["I have to study", "عَلَيَّ أَنْ أَدْرُس"], ["you (man) have to study", "عَلَيْكَ أَنْ تَدْرُس"],
                            ["you (woman) have to study", "عَلَيْكِ أَنْ تَدْرُسِي"], ["he has to study", "عَلَيْهِ أَنْ يَدْرُس"],
                            ["she has to study", "عَلَيْهَا أَنْ تَدْرُس"], ["we have to study", "عَلَيْنَا أَنْ نَدْرُس"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Must not versus do not have to",
             "The two ways of saying “not” have different meanings. يَجِب أَلَّا means “must not” (it is forbidden). "
             "لَيْسَ عَلَيَّ أَنْ means “I do not have to” (it is not required).",
             examples=[
                 ex("عَلَيَّ أَنْ أَغْسِل الصُّحُون.", "I have to wash the dishes.", "عَلَيَّ أَنْ"),
                 ex("عَلَيْهَا أَنْ تَكْتُب رِسَالَة.", "She has to write a letter.", "عَلَيْهَا أَنْ"),
                 ex("عَلَيْنَا أَنْ نَذْهَب إِلَى السُّوق.", "We have to go to the market.", "عَلَيْنَا أَنْ"),
                 ex("لَيْسَ عَلَيْكَ أَنْ تَذْهَب.", "You do not have to go. (to a man)", "لَيْسَ عَلَيْكَ أَنْ"),
                 ex("يَجِب أَلَّا تَذْهَب.", "You must not go. (to a man)", "يَجِب أَلَّا"),
             ]),
    ],
    exercises=[
        M("Which means “I have to wash the dishes”?", "عَلَيَّ أَنْ أَغْسِل الصُّحُون", ["عَلَيْهِ أَنْ أَغْسِل الصُّحُون", "عَلَيَّ أَنْ يَغْسِل الصُّحُون", "لِي أَنْ أَغْسِل الصُّحُون"], "عَلَيَّ + أَنْ + أَغْسِل."),
        M("Which means “She has to write a letter”?", "عَلَيْهَا أَنْ تَكْتُب رِسَالَة", ["عَلَيْهِ أَنْ تَكْتُب رِسَالَة", "عَلَيْهَا أَنْ أَكْتُب رِسَالَة", "عَلَيْكِ أَنْ تَكْتُب رِسَالَة"], "عَلَيْهَا = upon her."),
        M("Which means “We have to go to the market”?", "عَلَيْنَا أَنْ نَذْهَب إِلَى السُّوق", ["عَلَيْهِم أَنْ نَذْهَب إِلَى السُّوق", "عَلَيَّ أَنْ نَذْهَب إِلَى السُّوق", "عَلَيْنَا أَنْ يَذْهَب إِلَى السُّوق"], "عَلَيْنَا + نَذْهَب."),
        M("Which means “You (woman) have to study”?", "عَلَيْكِ أَنْ تَدْرُسِي", ["عَلَيْكَ أَنْ تَدْرُسِي", "عَلَيْكِ أَنْ تَدْرُس", "عَلَيْهَا أَنْ تَدْرُسِي"], "ـكِ and ـِي."),
        M("Which means “You do not have to go”?", "لَيْسَ عَلَيْكَ أَنْ تَذْهَب", ["يَجِب أَلَّا تَذْهَب", "لَيْسَ يَجِب أَنْ تَذْهَب", "عَلَيْكَ لَيْسَ أَنْ تَذْهَب"], "لَيْسَ عَلَى + ending."),
        M("Which means “You must not go”?", "يَجِب أَلَّا تَذْهَب", ["لَيْسَ عَلَيْكَ أَنْ تَذْهَب", "عَلَيْكَ أَنْ تَذْهَب", "لَيْسَ عِنْدَكَ أَنْ تَذْهَب"], "Forbidden = يَجِب أَلَّا."),
        M("A friend says «لَيْسَ عَلَيْكَ أَنْ تَدْرُس الْيَوْم». Does he forbid you?", "no, it is not required", ["yes, it is forbidden", "yes, you must study", "he asks a question"], "لَيْسَ عَلَيْكَ = you need not."),
        F("___ أَنْ أَغْسِل الصُّحُون.", "عَلَيَّ", ["لِي", "عِنْدِي", "مَعِي"], "Upon me.", tr="I have to wash the dishes."),
        F("لَيْسَ ___ أَنْ تَذْهَب.", "عَلَيْكَ", ["عَلَيَّ", "عَلَيْهَا", "عَلَيْنَا"], "Upon you (man).", tr="You do not have to go."),
    ],
    verify=(vv("غسل", "pres", ana="أَغْسِل", huwa="يَغْسِل") + vv("درس", "pres", ana="أَدْرُس", anta="تَدْرُس", huwa="يَدْرُس", nahnu="نَدْرُس")
            + vv("درس", "sub", anti="تَدْرُسِي") + vv("كتب", "pres", hiya="تَكْتُب") + vv("ذهب", "pres", anta="تَذْهَب", nahnu="نَذْهَب")
            + vw("السُّوق", "الصُّحُون", "رِسَالَة")),
)

# ---------------------------------------------------------------------------- 92
L92 = lesson(
    "Chores at home",
    "يَغْسِل الصُّحُون · يَطْبُخ الْعَشَاء",
    requires=["غسل", "فتح", "حمل", "طبخ", "نافذة"],
    cards=[
        card("Everyday jobs",
             "Here are some jobs around the house with the present form for “he” and the command to a man. The "
             "command of غَسَلَ is اِغْسِلْ, with ِ because the present vowel is ِ.",
             tables=[table(["English", "He …", "Command"],
                           [["wash the dishes", "يَغْسِل الصُّحُون", "اِغْسِلِ الصُّحُون"],
                            ["cook dinner", "يَطْبُخ الْعَشَاء", "اُطْبُخِ الْعَشَاء"],
                            ["open the window", "يَفْتَح النَّافِذَة", "اِفْتَحِ النَّافِذَة"],
                            ["carry the bag", "يَحْمِل الْحَقِيبَة", "اِحْمِلِ الْحَقِيبَة"],
                            ["write the homework", "يَكْتُب الْوَاجِب", "اُكْتُبِ الْوَاجِب"],
                            ["go to the market", "يَذْهَب إِلَى السُّوق", "اِذْهَبْ إِلَى السُّوق"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("Who does what",
             "Use the three patterns you now know to ask, order and report.",
             examples=[
                 ex("يَجِب أَنْ أَغْسِل الصُّحُون بَعْد الْعَشَاء.", "I must wash the dishes after dinner.", "أَغْسِل"),
                 ex("عَلَيْهَا أَنْ تَطْبُخ الْعَشَاء الْيَوْم.", "She has to cook dinner today.", "تَطْبُخ"),
                 ex("اِفْتَحِ النَّافِذَة مِنْ فَضْلِكَ.", "Open the window, please. (to a man)", "اِفْتَحِ"),
                 ex("لَا تَحْمِلِ الْحَقِيبَة، هِيَ كَبِيرَة.", "Do not carry the bag; it is big. (to a man)", "لَا تَحْمِلِ"),
                 ex("هَلْ عَلَيْكَ أَنْ تَذْهَب إِلَى السُّوق؟", "Do you have to go to the market? (to a man)", "عَلَيْكَ"),
             ]),
    ],
    exercises=[
        M("Which means “She has to cook dinner”?", "عَلَيْهَا أَنْ تَطْبُخ الْعَشَاء", ["عَلَيْهَا أَنْ يَطْبُخ الْعَشَاء", "عَلَيْهِ أَنْ تَطْبُخ الْعَشَاء", "عَلَيْهَا أَنْ أَطْبُخ الْعَشَاء"], "تَطْبُخ = she cooks."),
        M("Which is the command “Wash the dishes!” to a man?", "اِغْسِلِ الصُّحُون", ["اُغْسُلِ الصُّحُون", "يَغْسِل الصُّحُون", "لَا تَغْسِلِ الصُّحُون"], "Present vowel ِ → alif with ِ."),
        M("Which is the command “Cook dinner!” to a man?", "اُطْبُخِ الْعَشَاء", ["اِطْبِخِ الْعَشَاء", "يَطْبُخ الْعَشَاء", "لَا تَطْبُخِ الْعَشَاء"], "Present vowel ُ → alif with ُ."),
        M("Which means “Do not carry the bag” (to a man)?", "لَا تَحْمِلِ الْحَقِيبَة", ["اِحْمِلِ الْحَقِيبَة", "لَا يَحْمِل الْحَقِيبَة", "لَا تَحْمِلُوا الْحَقِيبَة"], "لَا + تَـ."),
        M("Which means “I must wash the dishes after dinner”?", "يَجِب أَنْ أَغْسِل الصُّحُون بَعْد الْعَشَاء", ["يَجِب أَنْ يَغْسِل الصُّحُون بَعْد الْعَشَاء", "يَجِب أَنْ أَغْسِل الصُّحُون قَبْل الْعَشَاء", "عَلَيْهِ أَنْ أَغْسِل الصُّحُون بَعْد الْعَشَاء"], "بَعْد = after."),
        M("Which means “Open the window, please”?", "اِفْتَحِ النَّافِذَة مِنْ فَضْلِكَ", ["اِفْتَحِ الْبَاب مِنْ فَضْلِكَ", "لَا تَفْتَحِ النَّافِذَة", "يَفْتَح النَّافِذَة"], "نَافِذَة = window."),
        F("يَجِب أَنْ أَغْسِل ___ بَعْد الْعَشَاء.", "الصُّحُون", ["النَّافِذَة", "الْحَقِيبَة", "السُّوق"], "What do you wash after dinner?", tr="I must wash the dishes after dinner."),
        F("عَلَيْهَا أَنْ ___ الْعَشَاء.", "تَطْبُخ", ["أَطْبُخ", "يَطْبُخ", "اُطْبُخْ"], "She cooks.", tr="She has to cook dinner."),
    ],
    verify=(vv("غسل", "pres", huwa="يَغْسِل", ana="أَغْسِل") + vv("غسل", "imp", anta="اِغْسِلْ")
            + vv("طبخ", "pres", huwa="يَطْبُخ", hiya="تَطْبُخ") + vv("طبخ", "imp", anta="اُطْبُخْ")
            + vv("فتح", "pres", huwa="يَفْتَح") + vv("فتح", "imp", anta="اِفْتَحْ") + vv("حمل", "pres", huwa="يَحْمِل")
            + vv("حمل", "imp", anta="اِحْمِلْ") + vv("كتب", "pres", huwa="يَكْتُب") + vv("كتب", "imp", anta="اُكْتُبْ")
            + vv("ذهب", "pres", huwa="يَذْهَب") + vv("ذهب", "imp", anta="اِذْهَبْ") + vv("حمل", "neg", anta="لَا تَحْمِلْ")
            + vw("النَّافِذَة", "الْعَشَاء", "كَبِيرَة", "بَعْد", "الْحَقِيبَة")),
)

# ---------------------------------------------------------------------------- 93
L93 = lesson(
    "Meals and drinks",
    "الْإِفْطَار · الْغَدَاء · الْعَشَاء · شَايْ · قَهْوَة",
    requires=["غداء", "عشاء", "شاي", "قهوة", "ماء", "حليب"],
    cards=[
        card("Meals and what we drink",
             "Arabic has three main meals. For the verb “to eat”, the present is يَأْكُل, with a hamza, and “I eat” is "
             "the special form آكُل.",
             tables=[table(["English", "Arabic"],
                           [["breakfast", "الْإِفْطَار"], ["lunch", "الْغَدَاء"], ["dinner", "الْعَشَاء"],
                            ["food", "طَعَام"], ["water", "مَاء"], ["tea", "شَايْ"], ["coffee", "قَهْوَة"],
                            ["juice", "عَصِير"], ["milk", "حَلِيب"]],
                           say=[1], tlit=[1])]),
        card("Eating and drinking",
             "شَرِبَ has the present يَشْرَب. أَكَلَ has يَأْكُل, نَأْكُل and تَأْكُل. Only “I” is special: آكُل.",
             examples=[
                 ex("آكُل الْإِفْطَار فِي الْبَيْت.", "I eat breakfast at home.", "آكُل"),
                 ex("نَأْكُل الْغَدَاء فِي الْمَدْرَسَة.", "We eat lunch at school.", "نَأْكُل"),
                 ex("أَشْرَب الْقَهْوَة فِي الصَّبَاح.", "I drink coffee in the morning.", "أَشْرَب"),
                 ex("هُوَ يَشْرَب الشَّايْ وَهِيَ تَشْرَب الْحَلِيب.", "He drinks tea and she drinks milk.", "يَشْرَب"),
                 ex("مَاذَا تَأْكُل فِي الْعَشَاء؟", "What do you eat for dinner? (to a man)", "تَأْكُل"),
             ]),
    ],
    exercises=[
        M("What is الْعَشَاء?", "dinner", ["lunch", "breakfast", "milk"], "عَشَاء = dinner."),
        M("What is الْغَدَاء?", "lunch", ["dinner", "breakfast", "tea"], "غَدَاء = lunch."),
        M("What is عَصِير?", "juice", ["water", "milk", "coffee"], "عَصِير = juice."),
        M("Which means “I eat breakfast at home”?", "آكُل الْإِفْطَار فِي الْبَيْت", ["أَكَلْ الْإِفْطَار فِي الْبَيْت", "يَأْكُل الْإِفْطَار فِي الْبَيْت", "نَأْكُل الْإِفْطَار فِي الْبَيْت"], "“I eat” is آكُل."),
        M("Which means “We eat lunch at school”?", "نَأْكُل الْغَدَاء فِي الْمَدْرَسَة", ["آكُل الْغَدَاء فِي الْمَدْرَسَة", "تَأْكُل الْغَدَاء فِي الْمَدْرَسَة", "نَشْرَب الْغَدَاء فِي الْمَدْرَسَة"], "نَـ = we."),
        M("Which means “I drink coffee in the morning”?", "أَشْرَب الْقَهْوَة فِي الصَّبَاح", ["آكُل الْقَهْوَة فِي الصَّبَاح", "أَشْرَب الشَّايْ فِي الْعَشَاء", "يَشْرَب الْقَهْوَة فِي الصَّبَاح"], "شَرِبَ = to drink."),
        M("Which means “What do you eat for dinner?”", "مَاذَا تَأْكُل فِي الْعَشَاء؟", ["مَنْ تَأْكُل فِي الْعَشَاء؟", "أَيْنَ تَأْكُل الْعَشَاء؟", "مَاذَا تَشْرَب فِي الْغَدَاء؟"], "مَاذَا = what."),
        F("___ الْقَهْوَة فِي الصَّبَاح.", "أَشْرَب", ["آكُل", "نَأْكُل", "يَأْكُل"], "I drink.", tr="I drink coffee in the morning."),
        F("نَأْكُل ___ فِي الْمَدْرَسَة.", "الْغَدَاء", ["الْقَهْوَة", "الشَّايْ", "الْمَاء"], "A meal.", tr="We eat lunch at school."),
    ],
    verify=(vv("شرب", "pres", ana="أَشْرَب", huwa="يَشْرَب", hiya="تَشْرَب") + vw("آكُل", "يَأْكُل", "نَأْكُل", "تَأْكُل", "الْإِفْطَار",
            "الْغَدَاء", "الْعَشَاء", "طَعَام", "مَاء", "شَايْ", "قَهْوَة", "عَصِير", "حَلِيب", "الصَّبَاح", "مَاذَا")),
)

# ---------------------------------------------------------------------------- 94
L94 = lesson(
    "Bread, rice, meat and fish",
    "خُبْز · رُزّ · لَحْم · دَجَاج · سَمَك",
    requires=["خبز", "رز", "لحم", "دجاج", "سمك", "بيض"],
    cards=[
        card("Main foods",
             "Many food words are mass or collective nouns. They are singular in form and stand for the food in general, "
             "so you can say الْخُبْز لَذِيذ, “bread is delicious”.",
             tables=[table(["English", "Arabic"],
                           [["bread", "خُبْز"], ["rice", "رُزّ"], ["meat", "لَحْم"], ["chicken", "دَجَاج"],
                            ["fish", "سَمَك"], ["eggs", "بَيْض"], ["cheese", "جُبْن"]],
                           say=[1], tlit=[1])]),
        card("Likes and dislikes",
             "You already know أُحِبّ (“I like”) and the negative لَا أُحِبّ. Add the food directly, with ال, when you "
             "mean it in general.",
             examples=[
                 ex("أُحِبّ السَّمَك وَالرُّزّ.", "I like fish and rice.", "أُحِبّ"),
                 ex("هَلْ تَأْكُل اللَّحْم؟", "Do you eat meat? (to a man)", "تَأْكُل"),
                 ex("لَا، أَنَا لَا آكُل اللَّحْم.", "No, I do not eat meat.", "لَا آكُل"),
                 ex("فِي الْإِفْطَار نَأْكُل الْبَيْض وَالْجُبْن وَالْخُبْز.", "For breakfast we eat eggs, cheese and bread.", "نَأْكُل"),
                 ex("هِيَ تَطْبُخ الدَّجَاج وَالرُّزّ.", "She cooks chicken and rice.", "تَطْبُخ"),
             ]),
    ],
    exercises=[
        M("What is خُبْز?", "bread", ["rice", "cheese", "fish"], "خُبْز = bread."),
        M("What is سَمَك?", "fish", ["meat", "chicken", "eggs"], "سَمَك = fish."),
        M("What is دَجَاج?", "chicken", ["meat", "rice", "bread"], "دَجَاج = chicken."),
        M("What is بَيْض?", "eggs", ["cheese", "bread", "milk"], "بَيْض = eggs."),
        M("Which means “I like fish and rice”?", "أُحِبّ السَّمَك وَالرُّزّ", ["لَا أُحِبّ السَّمَك وَالرُّزّ", "أَنَا آكُل السَّمَك وَالرُّزّ", "أُحِبّ اللَّحْم وَالرُّزّ"], "أُحِبّ = I like."),
        M("Which means “I do not eat meat”?", "أَنَا لَا آكُل اللَّحْم", ["أَنَا لَيْسَ آكُل اللَّحْم", "أَنَا آكُل اللَّحْم", "هِيَ لَا تَأْكُل اللَّحْم"], "لَا + present verb."),
        M("Which means “For breakfast we eat eggs, cheese and bread”?", "فِي الْإِفْطَار نَأْكُل الْبَيْض وَالْجُبْن وَالْخُبْز", ["فِي الْعَشَاء نَأْكُل الْبَيْض وَالْجُبْن وَالْخُبْز", "فِي الْإِفْطَار آكُل الْبَيْض وَالْجُبْن وَالْخُبْز", "فِي الْإِفْطَار نَشْرَب الْبَيْض وَالْجُبْن"], "الْإِفْطَار = breakfast."),
        F("هِيَ تَطْبُخ ___ وَالرُّزّ.", "الدَّجَاج", ["الْقَهْوَة", "الشَّايْ", "الْحَلِيب"], "Cooked with rice.", tr="She cooks chicken and rice."),
        F("لَا، أَنَا ___ آكُل اللَّحْم.", "لَا", ["لَيْسَ", "هَلْ", "لَمْ"], "لَا + present.", tr="No, I do not eat meat."),
    ],
    verify=(vv("طبخ", "pres", hiya="تَطْبُخ") + vw("خُبْز", "رُزّ", "لَحْم", "دَجَاج", "سَمَك", "بَيْض", "جُبْن", "أُحِبّ", "آكُل")),
)

# ---------------------------------------------------------------------------- 95
L95 = lesson(
    "Fruit and vegetables",
    "تُفَّاح · مَوْز · بُرْتُقَال · طَمَاطِم · بَطَاطِس",
    requires=["فاكهة", "تفاح", "موز", "برتقال", "طماطم", "بطاطس"],
    cards=[
        card("From the market",
             "These words are collective nouns too: تُفَّاح stands for apples in general. "
             "فَاكِهَة is the general word for fruit.",
             tables=[table(["English", "Arabic"],
                           [["fruit", "فَاكِهَة"], ["apples", "تُفَّاح"], ["bananas", "مَوْز"], ["oranges", "بُرْتُقَال"],
                            ["tomatoes", "طَمَاطِم"], ["potato / potatoes", "بَطَاطِس"]],
                           say=[1], tlit=[1])]),
        card("At the market and at home",
             "Combine these words with the verbs, the commands and the endings from this unit.",
             examples=[
                 ex("أُحِبّ الْفَاكِهَة، وَخَاصَّةً التُّفَّاح.", "I like fruit, especially apples.", "الْفَاكِهَة"),
                 ex("اِذْهَبْ إِلَى السُّوق، ثُمَّ اُطْلُبْ بُرْتُقَال.", "Go to the market, then ask for oranges. (to a man)", "اِذْهَبْ"),
                 ex("عَلَيْنَا أَنْ نَذْهَب إِلَى السُّوق، لَيْسَ عِنْدَنَا بَطَاطِس.", "We have to go to the market; we do not have potatoes.", "لَيْسَ عِنْدَنَا"),
                 ex("الطَّمَاطِم فِي الْحَقِيبَة، وَالْمَوْز فِيهَا أَيْضًا.", "The tomatoes are in the bag, and the bananas are in it too.", "فِيهَا"),
                 ex("هَلْ عِنْدَكُم تُفَّاح؟", "Do you have apples? (to a shopkeeper)", "عِنْدَكُم"),
             ]),
    ],
    exercises=[
        M("What is تُفَّاح?", "apples", ["oranges", "bananas", "tomatoes"], "تُفَّاح = apples."),
        M("What is مَوْز?", "bananas", ["apples", "potatoes", "fruit"], "مَوْز = bananas."),
        M("What is بَطَاطِس?", "potatoes", ["tomatoes", "oranges", "rice"], "بَطَاطِس = potatoes."),
        M("What is طَمَاطِم?", "tomatoes", ["potatoes", "bananas", "eggs"], "طَمَاطِم = tomatoes."),
        M("Which means “Do you have apples?”", "هَلْ عِنْدَكُم تُفَّاح؟", ["هَلْ عِنْدِي تُفَّاح؟", "هَلْ عِنْدَهَا تُفَّاح؟", "هَلْ مَعَنَا تُفَّاحَان؟"], "عِنْدَكُم = you (group) have."),
        M("Which means “We do not have potatoes”?", "لَيْسَ عِنْدَنَا بَطَاطِس", ["لَيْسَ عِنْدِي بَطَاطِس", "عِنْدَنَا بَطَاطِس", "لَا عِنْدَنَا بَطَاطِس"], "لَيْسَ + عِنْدَنَا."),
        M("«الطَّمَاطِم فِي الْحَقِيبَة، وَالْمَوْز فِيهَا أَيْضًا». What does فِيهَا stand for?", "the bag", ["the tomatoes", "the market", "the bananas"], "حَقِيبَة is feminine."),
        F("أُحِبّ ___ ، وَخَاصَّةً التُّفَّاح.", "الْفَاكِهَة", ["الْخُبْز", "الْقَهْوَة", "السَّمَك"], "General word for fruit.", tr="I like fruit, especially apples."),
        F("اِذْهَبْ إِلَى ___ ، ثُمَّ اُطْلُبْ بُرْتُقَال.", "السُّوق", ["النَّافِذَة", "الْحَقِيبَة", "الْجَبَل"], "Where you buy fruit.", tr="Go to the market, then ask for oranges."),
    ],
    verify=(vv("ذهب", "imp", anta="اِذْهَبْ") + vv("طلب", "imp", anta="اُطْلُبْ")
            + vw("فَاكِهَة", "تُفَّاح", "مَوْز", "بُرْتُقَال", "طَمَاطِم", "بَطَاطِس", "السُّوق", "وَخَاصَّةً", "أَيْضًا")),
)

# ---------------------------------------------------------------------------- 96
L96 = lesson(
    "Cups, plates and spoons",
    "كُوب مِنَ الشَّايْ · طَبَق مِنَ الرُّزّ",
    requires=["طبق", "صحن", "ملعقة", "كأس", "سكر", "شاي"],
    cards=[
        card("A container of something",
             "To say “a cup of tea” put the container first and then مِنْ with the drink: كُوب مِنَ الشَّايْ. The thing "
             "inside is definite after مِنْ. Counting works as before: dual for two, the polarity numbers from three "
             "to ten followed by a plural noun.",
             tables=[table(["English", "Singular", "Plural"],
                           [["cup, glass", "كُوب", "أَكْوَاب"], ["plate, dish", "طَبَق", "أَطْبَاق"],
                            ["spoon", "مِلْعَقَة", "مَلَاعِق"], ["small coffee cup", "فِنْجَان", "فَنَاجِين"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Ordering by the cup",
             "Remember that numbers from 3 to 10 take the form that is opposite in gender to the noun they count.",
             examples=[
                 ex("كُوب مِنَ الشَّايْ مِنْ فَضْلِكَ.", "A cup of tea, please. (to a man)", "كُوب مِنَ الشَّايْ"),
                 ex("فِنْجَان مِنَ الْقَهْوَة.", "A small cup of coffee.", "فِنْجَان مِنَ الْقَهْوَة"),
                 ex("كُوبَان مِنَ الْعَصِير.", "Two glasses of juice.", "كُوبَان"),
                 ex("ثَلَاثَة أَطْبَاق مِنَ الرُّزّ.", "Three plates of rice.", "ثَلَاثَة أَطْبَاق"),
                 ex("ثَلَاث مَلَاعِق مِنَ السُّكَّر.", "Three spoonfuls of sugar.", "ثَلَاث مَلَاعِق"),
             ]),
    ],
    exercises=[
        M("What is a فِنْجَان?", "a small coffee cup", ["a plate", "a spoon", "a bag"], "فِنْجَان = small cup."),
        M("What is a مِلْعَقَة?", "a spoon", ["a plate", "a cup", "a table"], "مِلْعَقَة = spoon."),
        M("Which means “a cup of tea”?", "كُوب مِنَ الشَّايْ", ["كُوب الشَّايْ مِنَ", "شَايْ مِنَ الْكُوب", "كُوبَان مِنَ الشَّايْ"], "container + مِنَ + drink."),
        M("Which means “two glasses of juice”?", "كُوبَان مِنَ الْعَصِير", ["كُوب مِنَ الْعَصِير", "ثَلَاثَة أَكْوَاب مِنَ الْعَصِير", "أَكْوَاب مِنَ الْعَصِير"], "Dual: ـَان."),
        M("Which means “three plates of rice”?", "ثَلَاثَة أَطْبَاق مِنَ الرُّزّ", ["ثَلَاث أَطْبَاق مِنَ الرُّزّ", "ثَلَاثَة طَبَق مِنَ الرُّزّ", "طَبَقَان مِنَ الرُّزّ"], "طَبَق is masculine, so the number ends in ة."),
        M("Which means “three spoonfuls of sugar”?", "ثَلَاث مَلَاعِق مِنَ السُّكَّر", ["ثَلَاثَة مَلَاعِق مِنَ السُّكَّر", "ثَلَاث مِلْعَقَة مِنَ السُّكَّر", "مِلْعَقَتَان مِنَ السُّكَّر"], "مِلْعَقَة is feminine, so the number has no ة."),
        M("What is the plural of طَبَق?", "أَطْبَاق", ["طَبَقَات", "أَكْوَاب", "طَبَقُون"], "Broken plural."),
        F("كُوب ___ الشَّايْ.", "مِنَ", ["فِي", "عَلَى", "مَعَ"], "of tea.", tr="A cup of tea."),
        F("ثَلَاثَة ___ مِنَ الرُّزّ.", "أَطْبَاق", ["طَبَق", "أَطْبَاقَان", "مَلَاعِق"], "Plural after the number.", tr="Three plates of rice."),
    ],
    verify=(vn(3, "m", "ثَلَاثَة") + vn(3, "f", "ثَلَاث") + vd("كُوب", "كُوبَان", "كُوبَيْن") + vpb("كُوب", "أَكْوَاب") + vpb("طَبَق", "أَطْبَاق")
            + vpb("مِلْعَقَة", "مَلَاعِق") + vpb("فِنْجَان", "فَنَاجِين") + vw("فِنْجَان", "مِلْعَقَة", "السُّكَّر")),
)

# ---------------------------------------------------------------------------- 97
L97 = lesson(
    "Hot, cold, sweet and delicious",
    "الْقَهْوَة سَاخِنَة · الشَّايْ حُلْوْ",
    requires=["لذيذ", "ساخن", "بارد", "حلو", "قهوة", "ماء"],
    cards=[
        card("Describing food",
             "An adjective after a definite noun, with no ال of its own, makes a complete sentence: الشَّايْ سَاخِن. "
             "It agrees with the noun in gender. قَهْوَة is feminine and شَايْ is masculine.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["hot", "سَاخِن", "سَاخِنَة"], ["cold", "بَارِد", "بَارِدَة"], ["sweet", "حُلْوْ", "حُلْوَة"],
                            ["salty", "مَالِح", "مَالِحَة"], ["delicious", "لَذِيذ", "لَذِيذَة"], ["hungry", "جَائِع", "جَائِعَة"]],
                           say=[1, 2], tlit=[1, 2])]),
        card("Tasting and wanting",
             "To ask for something, say أُرِيد (“I want”) and then the thing.",
             examples=[
                 ex("الشَّايْ سَاخِن وَالْقَهْوَة سَاخِنَة.", "The tea is hot and the coffee is hot.", "سَاخِن"),
                 ex("الْعَصِير بَارِد جِدًّا.", "The juice is very cold.", "بَارِد"),
                 ex("الْفَاكِهَة حُلْوَة وَلَذِيذَة.", "The fruit is sweet and delicious.", "حُلْوَة"),
                 ex("أَنَا جَائِع. أُرِيد خُبْز وَجُبْن.", "I am hungry. I want bread and cheese. (a man speaking)", "جَائِع"),
                 ex("هِيَ جَائِعَة وَتُرِيد طَبَق مِنَ الرُّزّ.", "She is hungry and wants a plate of rice.", "جَائِعَة"),
             ]),
    ],
    exercises=[
        M("Which means “The coffee is hot”?", "الْقَهْوَة سَاخِنَة", ["الْقَهْوَة سَاخِن", "الْقَهْوَة السَّاخِنَة", "قَهْوَة السَّاخِن"], "قَهْوَة is feminine."),
        M("Which means “The tea is hot”?", "الشَّايْ سَاخِن", ["الشَّايْ سَاخِنَة", "الشَّايْ السَّاخِنَة", "شَايْ سَاخِنَة"], "شَايْ is masculine."),
        M("Which means “The fruit is delicious”?", "الْفَاكِهَة لَذِيذَة", ["الْفَاكِهَة لَذِيذ", "الْفَاكِهَة بَارِد", "الْفَاكِهَة حُلْوْ"], "فَاكِهَة is feminine."),
        M("Which means “The juice is very cold”?", "الْعَصِير بَارِد جِدًّا", ["الْعَصِير بَارِدَة جِدًّا", "الْعَصِير سَاخِن جِدًّا", "الْعَصِير حُلْوْ قَلِيلًا"], "عَصِير is masculine."),
        M("A woman says she is hungry. Which does she say?", "أَنَا جَائِعَة", ["أَنَا جَائِع", "أَنَا جَوْعَان", "أَنَا لَذِيذَة"], "Feminine ـَة."),
        M("Which means “I want bread and cheese”?", "أُرِيد خُبْز وَجُبْن", ["أَنَا خُبْز وَجُبْن", "يُرِيد خُبْز وَجُبْن", "لَا أُرِيد خُبْز"], "أُرِيد = I want."),
        M("What is the opposite of سَاخِن?", "بَارِد", ["حُلْوْ", "لَذِيذ", "مَالِح"], "hot ↔ cold."),
        F("الشَّايْ ___ جِدًّا.", "سَاخِن", ["سَاخِنَة", "السَّاخِن", "بَارِدَة"], "شَايْ is masculine.", tr="The tea is very hot."),
        F("الْفَاكِهَة ___ وَلَذِيذَة.", "حُلْوَة", ["حُلْوْ", "بَارِد", "سَاخِن"], "فَاكِهَة is feminine.", tr="The fruit is sweet and delicious."),
    ],
    verify=(vf("سَاخِن", "سَاخِنَة") + vf("بَارِد", "بَارِدَة") + vf("حُلْو", "حُلْوَة") + vf("مَالِح", "مَالِحَة")
            + vf("لَذِيذ", "لَذِيذَة") + vf("جَائِع", "جَائِعَة") + vw("جِدًّا", "أُرِيد", "تُرِيد", "جَائِع", "مَالِح")),
)

# ---------------------------------------------------------------------------- 98
L98 = lesson(
    "At the restaurant",
    "قَائِمَة الطَّعَام · أُرِيد · الْحِسَاب لَوْ سَمَحْتَ",
    requires=["مطعم", "قائمة", "طلب", "فاتورة", "حساب", "طعام"],
    cards=[
        card("Words for eating out",
             "قَائِمَة الطَّعَام is the menu (literally “the list of the food”, an iḍāfa). You ask the waiter for "
             "things with أُرِيد, and you ask for the bill with الْحِسَاب.",
             tables=[table(["English", "Arabic"],
                           [["restaurant", "مَطْعَم"], ["menu", "قَائِمَة الطَّعَام"], ["waiter", "نَادِل"],
                            ["order", "طَلَب"], ["bill", "فَاتُورَة"], ["the bill, please (to a man)", "الْحِسَاب لَوْ سَمَحْتَ"],
                            ["I would like…", "أُرِيد …"], ["do you have…?", "هَلْ عِنْدَكُم …؟"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A short exchange",
             "When you ask هَلْ عِنْدَكُم…؟ you use the plural because you are asking the whole restaurant. The "
             "waiter answers you with تَفَضَّل (to a man) or تَفَضَّلِي (to a woman).",
             examples=[
                 ex("أُرِيد قَائِمَة الطَّعَام مِنْ فَضْلِكَ.", "I would like the menu, please. (to a man)", "أُرِيد"),
                 ex("هَلْ عِنْدَكُم سَمَك؟", "Do you have fish?", "عِنْدَكُم"),
                 ex("نَعَمْ، عِنْدَنَا سَمَك وَدَجَاج.", "Yes, we have fish and chicken.", "عِنْدَنَا"),
                 ex("أُرِيد طَبَق مِنَ الرُّزّ وَكُوب مِنَ الْعَصِير.", "I would like a plate of rice and a glass of juice.", "أُرِيد"),
                 ex("الطَّعَام لَذِيذ جِدًّا. الْحِسَاب لَوْ سَمَحْتَ.", "The food is very good. The bill, please. (to a man)", "الْحِسَاب"),
             ]),
    ],
    exercises=[
        M("What is a مَطْعَم?", "a restaurant", ["a market", "a kitchen", "a school"], "مَطْعَم = restaurant."),
        M("What is قَائِمَة الطَّعَام?", "the menu", ["the bill", "the waiter", "the kitchen"], "list of food = menu."),
        M("What is نَادِل?", "a waiter", ["a cook", "a guest", "a student"], "نَادِل = waiter."),
        M("Which asks for the menu?", "أُرِيد قَائِمَة الطَّعَام مِنْ فَضْلِكَ", ["أُرِيد الْحِسَاب مِنْ فَضْلِكَ", "أُرِيد مَطْعَم مِنْ فَضْلِكَ", "عِنْدِي قَائِمَة الطَّعَام"], "قَائِمَة الطَّعَام = menu."),
        M("Which asks for the bill?", "الْحِسَاب لَوْ سَمَحْتَ", ["قَائِمَة الطَّعَام لَوْ سَمَحْتَ", "الشَّايْ لَوْ سَمَحْتَ", "تَفَضَّل لَوْ سَمَحْتَ"], "الْحِسَاب = the bill."),
        M("Which asks “Do you have fish?”", "هَلْ عِنْدَكُم سَمَك؟", ["هَلْ عِنْدِي سَمَك؟", "أُرِيد سَمَك؟", "هَلْ هُوَ سَمَك؟"], "عِنْدَكُم = you (all) have."),
        M("Which means “I would like a plate of rice and a glass of juice”?", "أُرِيد طَبَق مِنَ الرُّزّ وَكُوب مِنَ الْعَصِير", ["أُرِيد طَبَقَان مِنَ الرُّزّ وَكُوب مِنَ الْعَصِير", "أُرِيد طَبَق مِنَ الْعَصِير وَكُوب مِنَ الرُّزّ", "عِنْدِي طَبَق مِنَ الرُّزّ وَكُوب"], "Container + مِنَ + food."),
        F("هَلْ ___ سَمَك؟", "عِنْدَكُم", ["عِنْدِي", "مَعِي", "لَهَا"], "Asking the restaurant.", tr="Do you have fish?"),
        F("الْحِسَاب ___ سَمَحْتَ.", "لَوْ", ["هَلْ", "مَا", "لَا"], "Fixed polite phrase.", tr="The bill, please."),
    ],
    verify=vw("مَطْعَم", "قَائِمَة", "نَادِل", "طَلَب", "فَاتُورَة", "الْحِسَاب", "لَوْ", "سَمَحْتَ", "عِنْدَكُم", "عِنْدَنَا", "الطَّعَام"),
)

# ---------------------------------------------------------------------------- 99
L99 = lesson(
    "Dinner at home",
    "الْعَشَاء لَذِيذ · لَا تَفْتَحِ النَّافِذَة",
    requires=["مطبخ", "عشاء", "طبخ", "دجاج", "نافذة", "جو"],
    cards=[
        card("A conversation",
             "Layla and Ahmad are home in the evening. Read it for the commands, the endings and “must”.",
             examples=[
                 ex("لَيْلَى: أَنَا جَائِعَة. يَجِب أَنْ أَطْبُخ الْعَشَاء.", "Layla: I am hungry. I must cook dinner."),
                 ex("أَحْمَد: هَلْ عِنْدَنَا رُزّ؟", "Ahmad: Do we have rice?"),
                 ex("لَيْلَى: نَعَمْ، عِنْدَنَا رُزّ وَدَجَاج. اُنْظُرْ فِي الْمَطْبَخ.", "Layla: Yes, we have rice and chicken. Look in the kitchen."),
                 ex("أَحْمَد: عَلَيَّ أَنْ أَغْسِل الصُّحُون بَعْد الْعَشَاء.", "Ahmad: I have to wash the dishes after dinner."),
                 ex("لَيْلَى: لَا تَفْتَحِ النَّافِذَة، الْجَوّ بَارِد.", "Layla: Do not open the window; the weather is cold."),
                 ex("أَحْمَد: الْعَشَاء لَذِيذ جِدًّا، شُكْرًا لَكِ!", "Ahmad: Dinner is delicious, thank you!"),
             ]),
    ],
    exercises=[
        M("«أَنَا جَائِعَة. يَجِب أَنْ أَطْبُخ الْعَشَاء.» What will Layla do?", "cook dinner", ["wash the dishes", "go to school", "open the window"], "أَطْبُخ = I cook."),
        M("«هَلْ عِنْدَنَا رُزّ؟». What does Ahmad ask?", "whether they have rice", ["whether she is hungry", "where the kitchen is", "whether dinner is ready"], "عِنْدَنَا = we have."),
        M("«نَعَمْ، عِنْدَنَا رُزّ وَدَجَاج». What do they have?", "rice and chicken", ["rice and fish", "bread and cheese", "only chicken"], "رُزّ وَدَجَاج."),
        M("«اُنْظُرْ فِي الْمَطْبَخ». Who is she speaking to, and what does she say?", "a man; look in the kitchen", ["a woman; sit in the kitchen", "a group; cook in the kitchen", "a man; do not enter the kitchen"], "اُنْظُرْ is a command to a man."),
        M("«عَلَيَّ أَنْ أَغْسِل الصُّحُون بَعْد الْعَشَاء». What must Ahmad do?", "wash the dishes after dinner", ["cook dinner", "go to the market", "write a letter"], "عَلَيَّ أَنْ = I have to."),
        M("«لَا تَفْتَحِ النَّافِذَة، الْجَوّ بَارِد». Why not?", "because it is cold", ["because it is hot", "because it is late", "because it is broken"], "بَارِد = cold."),
        M("«الْعَشَاء لَذِيذ جِدًّا، شُكْرًا لَكِ!». Who is thanked?", "a woman", ["a man", "a group", "no one"], "لَكِ is feminine."),
        F("لَا ___ النَّافِذَة.", "تَفْتَحِ", ["اِفْتَحِ", "يَفْتَح", "فَتَحَ"], "Negative command.", tr="Do not open the window."),
        F("عَلَيَّ أَنْ ___ الصُّحُون.", "أَغْسِل", ["يَغْسِل", "اِغْسِلْ", "غَسَلَ"], "I wash.", tr="I have to wash the dishes."),
    ],
    verify=(vv("غسل", "pres", ana="أَغْسِل") + vv("طبخ", "pres", ana="أَطْبُخ") + vv("نظر", "imp", anta="اُنْظُرْ")
            + vv("فتح", "neg", anta="لَا تَفْتَحْ") + vw("الْجَوّ", "الْمَطْبَخ")),
)

# ---------------------------------------------------------------------------- 100
L100 = lesson(
    "Review: commands, endings, obligations and food",
    "اِفْتَحْ · لَا تَدْخُلْ · فِيهِ · يَجِب أَنْ · لَذِيذ",
    requires=["فتح", "باب", "مطبخ", "طعام", "شاي", "عند"],
    cards=[
        card("What you can do now",
             "Commands: اِفْتَحْ, اِفْتَحِي, لَا تَفْتَحْ. Endings: لِي, عِنْدِي, مَعِي, فِيهِ, عَلَيْهَا. Obligation: يَجِب أَنْ + verb, عَلَيَّ أَنْ + verb. Food and drink: خُبْز, رُزّ, شَايْ, قَهْوَة, كُوب, طَبَق.",
             examples=[
                 ex("اِفْتَحِي الْبَاب يَا لَيْلَى.", "Open the door, Layla."),
                 ex("لَا تَدْخُلُوا الْمَطْبَخ.", "Do not enter the kitchen. (to a group)"),
                 ex("عِنْدِي كِتَاب، وَهُوَ عَلَى الطَّاوِلَة.", "I have a book, and it is on the table."),
                 ex("يَجِب أَنْ تَشْرَبِي الْمَاء.", "You must drink water. (to a woman)"),
                 ex("كُوب مِنَ الشَّايْ مِنْ فَضْلِكَ.", "A cup of tea, please. (to a man)"),
             ]),
    ],
    exercises=[
        M("Which tells a woman to open the door?", "اِفْتَحِي الْبَاب", ["اِفْتَحْ الْبَاب", "تَفْتَحِين الْبَاب", "لَا تَفْتَحِي الْبَاب"], "ـِي."),
        M("Which tells a group not to enter the kitchen?", "لَا تَدْخُلُوا الْمَطْبَخ", ["لَا تَدْخُلْ الْمَطْبَخ", "اُدْخُلُوا الْمَطْبَخ", "لَا تَدْخُلِي الْمَطْبَخ"], "لَا تَدْخُلُوا is for a group."),
        M("Which means “I have a book”?", "عِنْدِي كِتَاب", ["عَلَيَّ كِتَاب", "فِيهِ كِتَاب", "مِنِّي كِتَاب"], "عِنْدِي."),
        M("Which means “It is on it” (a book on the table)?", "هُوَ عَلَيْهَا", ["هُوَ فِيهَا", "هُوَ عَلَيْهِ", "هُوَ مِنْهَا"], "طَاوِلَة is feminine."),
        M("Which means “You (woman) must drink water”?", "يَجِب أَنْ تَشْرَبِي الْمَاء", ["يَجِب أَنْ تَشْرَبِين الْمَاء", "يَجِب أَنْ يَشْرَب الْمَاء", "يَجِب أَنْ تَشْرَبُوا الْمَاء"], "أَنْ drops the ن."),
        M("Which means “I do not have to go”?", "لَيْسَ عَلَيَّ أَنْ أَذْهَب", ["يَجِب أَلَّا أَذْهَب", "لَيْسَ عِنْدِي أَنْ أَذْهَب", "عَلَيَّ أَنْ لَا أَذْهَب"], "لَيْسَ عَلَيَّ."),
        M("Which is a correct way to order tea?", "كُوب مِنَ الشَّايْ مِنْ فَضْلِكَ", ["كُوب الشَّايْ فِي فَضْلِكَ", "شَايْ مِنْ كُوب لِي", "مِنْ فَضْلِكَ كُوبَان لِي الشَّايْ"], "container + مِنَ + drink."),
        F("اِفْتَحِي ___ يَا لَيْلَى.", "الْبَاب", ["الْمَاء", "الشَّايْ", "الْخُبْز"], "Something you open.", tr="Open the door, Layla."),
        F("هَذَا مَطْبَخ. الْعَشَاء ___ .", "فِيهِ", ["فِيهَا", "عَلَيْهِ", "إِلَيْكِ"], "In it.", tr="This is a kitchen. Dinner is in it."),
    ],
    verify=(vv("فتح", "imp", anti="اِفْتَحِي") + vv("دخل", "neg", antum="لَا تَدْخُلُوا") + vv("شرب", "sub", anti="تَشْرَبِي")
            + vw("اِفْتَحِي", "كِتَاب", "الْمَطْبَخ")),
)
UNIT = unit("الأوامر والواجبات: commands, endings and obligations", [L80, L81, L82, L83, L84, L85, L86, L87, L88, L89, L90, L91, L92, L93, L94, L95, L96, L97, L98, L99, L100])
