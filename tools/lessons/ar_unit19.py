"""Unit 19 (chapter 17): relative pronouns, the passive, Measure VII and the geography of the Arab world."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 277
L277 = lesson(
    "“Who” and “which”: الَّذِي and الَّتِي",
    "الرَّجُل الَّذِي يَعْمَل هُنَا · الْمَرْأَة الَّتِي تَسْكُن هُنَا",
    requires=["الذي", "رجل", "مهندس", "معلم", "عمل", "سكن", "كتاب", "مدرسة"],
    cards=[
        card("Joining two sentences",
             "A relative pronoun links a describing clause to a noun that is already definite (it has ال, or it is a name). English uses who, which or that. "
             "Arabic uses one of six words, and it must match the noun in gender and number. For a masculine singular noun use الَّذِي. For a feminine singular noun use الَّتِي.",
             tables=[table(["Noun", "Pronoun", "Phrase"],
                           [["الرَّجُل", "الَّذِي", "الرَّجُل الَّذِي يَعْمَل هُنَا"], ["الْمَرْأَة", "الَّتِي", "الْمَرْأَة الَّتِي تَعْمَل هُنَا"],
                            ["الْكِتَاب", "الَّذِي", "الْكِتَاب الَّذِي عَلَى الطَّاوِلَة"], ["الْمَدِينَة", "الَّتِي", "الْمَدِينَة الَّتِي فِي الشَّمَال"]],
                           say=[0, 1, 2], tlit=[2], gloss=False)]),
        card("What follows the pronoun",
             "After the pronoun comes a normal clause: a verb, or a prepositional phrase. When the noun is the doer of the verb, the verb agrees with it (يَعْمَل for a man, تَعْمَل for a woman), and you add nothing else.",
             examples=[
                 ex("الرَّجُل الَّذِي يَعْمَل هُنَا مُهَنْدِس.", "The man who works here is an engineer.", "الَّذِي"),
                 ex("الْمَرْأَة الَّتِي تَسْكُن بِجَانِبِي مُعَلِّمَة.", "The woman who lives next to me is a teacher.", "الَّتِي"),
                 ex("الطَّالِب الَّذِي يَدْرُس مَعِي يَتَكَلَّم الرُّوسِيَّة.", "The student who studies with me speaks Russian.", "الَّذِي"),
                 ex("الْمُدَرِّسَة الَّتِي تُدَرِّس الْعَرَبِيَّة مِنْ مِصْر.", "The teacher who teaches Arabic is from Egypt.", "الَّتِي"),
                 ex("الْكِتَاب الَّذِي عَلَى الطَّاوِلَة جَدِيد.", "The book that is on the table is new.", "الَّذِي"),
                 ex("الْمَدِينَة الَّتِي فِي الشَّمَال كَبِيرَة.", "The city that is in the north is big.", "الَّتِي"),
             ]),
    ],
    exercises=[
        M("Which pronoun goes with الرَّجُل?", "الَّذِي", ["الَّتِي", "الَّذِين", "اللَّاتِي"], "Masculine singular."),
        M("Which pronoun goes with الْمَرْأَة?", "الَّتِي", ["الَّذِي", "الَّذِين", "اللَّذَان"], "Feminine singular."),
        M("Which pronoun goes with الْكِتَاب?", "الَّذِي", ["الَّتِي", "اللَّاتِي", "اللَّتَان"], "كِتَاب is masculine."),
        M("Which pronoun goes with الْمَدِينَة?", "الَّتِي", ["الَّذِي", "الَّذِين", "اللَّذَان"], "مَدِينَة is feminine."),
        M("What does الرَّجُل الَّذِي يَعْمَل هُنَا مُهَنْدِس mean?", "The man who works here is an engineer", ["The man works here as an engineer", "An engineer is working", "The engineer who works there is a man"], "الَّذِي = who."),
        M("What does الْمُدَرِّسَة الَّتِي تُدَرِّس الْعَرَبِيَّة مِنْ مِصْر mean?", "The teacher who teaches Arabic is from Egypt", ["The teacher teaches Arabic in Egypt", "Arabic is taught by a woman", "Egypt has a teacher"], "الَّتِي = who."),
        F("الْمَرْأَة ___ تَسْكُن بِجَانِبِي مُعَلِّمَة.", "الَّتِي", ["الَّذِي", "الَّذِين", "اللَّذَان"], "A woman: feminine singular.", tr="The woman who lives next to me is a teacher."),
        F("الطَّالِب ___ يَدْرُس مَعِي يَتَكَلَّم الرُّوسِيَّة.", "الَّذِي", ["الَّتِي", "اللَّاتِي", "اللَّتَان"], "A male student: masculine singular.", tr="The student who studies with me speaks Russian."),
        F("الْكِتَاب الَّذِي عَلَى الطَّاوِلَة ___.", "جَدِيد", ["جَدِيدَة", "جَدِيدُون", "جَدِيدَتَان"], "The book is masculine.", tr="The book that is on the table is new."),
    ],
    verify=(vv("عمل", "pres", huwa="يَعْمَل", hiya="تَعْمَل") + vv("سكن", "pres", hiya="تَسْكُن") + vv("درس", "pres", huwa="يَدْرُس") + vv("درس#2", "pres", hiya="تُدَرِّس")
            + vw("الَّذِي", "الَّتِي", "الرَّجُل", "الْمَرْأَة", "مُهَنْدِس", "بِجَانِبِي", "مُعَلِّمَة", "الطَّالِب", "الرُّوسِيَّة", "الْمُدَرِّسَة", "الْعَرَبِيَّة", "مِصْر", "الشَّمَال", "الَّذِين", "اللَّاتِي", "اللَّذَان", "اللَّتَان")),
)

# ---------------------------------------------------------------------------- 278
L278 = lesson(
    "No pronoun for an indefinite noun",
    "رَجُل يَعْمَل هُنَا · الرَّجُل الَّذِي يَعْمَل هُنَا",
    requires=["الذي", "رجل", "طالب", "كتاب", "عمل", "درس", "معرفة"],
    cards=[
        card("Definite or indefinite?",
             "Use a relative pronoun only after a definite noun. After an indefinite noun, just put the clause next to it, and English will add “who” or “that” for you.",
             tables=[table(["Indefinite: no pronoun", "Definite: with pronoun"],
                           [["رَجُل يَعْمَل هُنَا", "الرَّجُل الَّذِي يَعْمَل هُنَا"], ["طَالِبَة تَدْرُس الْعَرَبِيَّة", "الطَّالِبَة الَّتِي تَدْرُس الْعَرَبِيَّة"],
                            ["كِتَاب عَلَى الطَّاوِلَة", "الْكِتَاب الَّذِي عَلَى الطَّاوِلَة"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Same idea, two shapes",
             "A noun with a name counts as definite: مُحَمَّد الَّذِي يَعْمَل هُنَا is “Muhammad, who works here”. These sentences are invented.",
             examples=[
                 ex("أَعْرِف رَجُلًا يَعْمَل فِي الْمَطَار.", "I know a man who works at the airport.", "رَجُلًا يَعْمَل"),
                 ex("أَعْرِف الرَّجُل الَّذِي يَعْمَل فِي الْمَطَار.", "I know the man who works at the airport.", "الَّذِي"),
                 ex("هَذِهِ طَالِبَة تَدْرُس الْعَرَبِيَّة.", "This is a student who studies Arabic.", "طَالِبَة تَدْرُس"),
                 ex("هَذِهِ هِيَ الطَّالِبَة الَّتِي تَدْرُس الْعَرَبِيَّة.", "This is the student who studies Arabic.", "الَّتِي"),
                 ex("قَرَأْتُ كِتَابًا عَنِ الْجُغْرَافِيَا.", "I read a book about geography.", "كِتَابًا"),
                 ex("سَلْمَى الَّتِي تَعْمَل فِي الْمَكْتَبَة صَدِيقَتِي.", "Salma, who works in the library, is my friend.", "سَلْمَى الَّتِي"),
             ]),
    ],
    exercises=[
        M("Which phrase means “a woman who works here”?", "اِمْرَأَة تَعْمَل هُنَا", ["اِمْرَأَة الَّتِي تَعْمَل هُنَا", "الْمَرْأَة تَعْمَل هُنَا", "الْمَرْأَة الَّذِي تَعْمَل هُنَا"], "An indefinite noun takes no pronoun."),
        M("Which phrase means “the woman who works here”?", "الْمَرْأَة الَّتِي تَعْمَل هُنَا", ["اِمْرَأَة تَعْمَل هُنَا", "الْمَرْأَة الَّذِي تَعْمَل هُنَا", "اِمْرَأَة الَّتِي تَعْمَل هُنَا"], "A definite noun takes a pronoun."),
        M("Is a relative pronoun used after رَجُل (a man)?", "no, the noun is indefinite", ["yes, always", "yes, but only الَّتِي", "only in questions"], "Pronouns follow definite nouns."),
        M("What does أَعْرِف رَجُلًا يَعْمَل فِي الْمَطَار mean?", "I know a man who works at the airport", ["I know the man who works at the airport", "I work at the airport", "A man knows me"], "رَجُلًا is indefinite."),
        M("What does هَذِهِ هِيَ الطَّالِبَة الَّتِي تَدْرُس الْعَرَبِيَّة mean?", "This is the student who studies Arabic", ["This is a student who studies Arabic", "She studies the Arabic student", "The student is Arabic"], "الطَّالِبَة is definite."),
        M("Is سَلْمَى (a name) definite or indefinite?", "definite", ["indefinite", "plural", "dual"], "Names are definite."),
        F("هَذِهِ طَالِبَة ___ الْعَرَبِيَّة.", "تَدْرُس", ["الَّتِي تَدْرُس", "الَّذِي يَدْرُس", "الَّذِين يَدْرُسُون"], "An indefinite noun: no pronoun.", tr="This is a student who studies Arabic."),
        F("أَعْرِف الرَّجُل ___ يَعْمَل فِي الْمَطَار.", "الَّذِي", ["الَّتِي", "الَّذِين", "اللَّذَان"], "A definite noun: use a pronoun.", tr="I know the man who works at the airport."),
        F("___ الَّتِي تَعْمَل فِي الْمَكْتَبَة صَدِيقَتِي.", "سَلْمَى", ["رَجُل", "الْكِتَاب", "طَالِب"], "A name is definite.", tr="Salma, who works in the library, is my friend."),
    ],
    verify=(vv("عمل", "pres", huwa="يَعْمَل", hiya="تَعْمَل") + vv("درس", "pres", hiya="تَدْرُس")
            + vw("اِمْرَأَة", "رَجُلًا", "كِتَابًا", "الْجُغْرَافِيَا", "الْمَكْتَبَة", "صَدِيقَتِي", "أَعْرِف", "قَرَأْتُ", "مُحَمَّد", "الْمَطَار")),
)

# ---------------------------------------------------------------------------- 279
L279 = lesson(
    "Two of them: اللَّذَان and اللَّتَان",
    "الْمُهَنْدِسَان اللَّذَان يَعْمَلَان هُنَا",
    requires=["الذي", "مهندس", "معلم", "عمل", "كتاب", "صديق", "درس"],
    cards=[
        card("Dual pronouns",
             "For two people or things, the relative pronoun is dual too. Masculine: اللَّذَان (nominative) and اللَّذَيْن (accusative and genitive). Feminine: اللَّتَان and اللَّتَيْن. "
             "The verb in the clause is also dual: يَعْمَلَان (two men work), تَعْمَلَان (two women work).",
             tables=[table(["Case", "Masculine dual", "Feminine dual"],
                           [["subject (nominative)", "اللَّذَان", "اللَّتَان"], ["object or after a preposition", "اللَّذَيْن", "اللَّتَيْن"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Examples",
             "The pronoun copies the case of the noun it follows: الْمُهَنْدِسَان (subject) takes اللَّذَان; الْمُهَنْدِسَيْن (object) takes اللَّذَيْن.",
             examples=[
                 ex("الْمُهَنْدِسَان اللَّذَان يَعْمَلَان هُنَا مِنْ مِصْر.", "The two engineers who work here are from Egypt.", "اللَّذَان"),
                 ex("الْمُعَلِّمَتَان اللَّتَان تُدَرِّسَان الْعَرَبِيَّة مِنَ الْأُرْدُنّ.", "The two teachers who teach Arabic are from Jordan.", "اللَّتَان"),
                 ex("شَاهَدْتُ الْمُهَنْدِسَيْن اللَّذَيْن يَعْمَلَان هُنَا.", "I saw the two engineers who work here.", "اللَّذَيْن"),
                 ex("تَكَلَّمْتُ مَعَ الْمُعَلِّمَتَيْن اللَّتَيْن تُدَرِّسَان الْعَرَبِيَّة.", "I spoke with the two teachers who teach Arabic.", "اللَّتَيْن"),
                 ex("الصَّدِيقَان اللَّذَان يَدْرُسَان مَعِي طَالِبَان جَيِّدَان.", "The two friends who study with me are good students.", "اللَّذَان"),
                 ex("الْكِتَابَان اللَّذَان عَلَى الطَّاوِلَة جَدِيدَان.", "The two books that are on the table are new.", "اللَّذَان"),
             ]),
    ],
    exercises=[
        M("Which pronoun goes with الْمُهَنْدِسَان (two engineers, subject)?", "اللَّذَان", ["اللَّتَان", "الَّذِي", "الَّذِين"], "Masculine dual, nominative."),
        M("Which pronoun goes with الْمُعَلِّمَتَان (two teachers, subject)?", "اللَّتَان", ["اللَّذَان", "الَّتِي", "اللَّاتِي"], "Feminine dual, nominative."),
        M("Which pronoun goes with الْمُهَنْدِسَيْن (two engineers, object)?", "اللَّذَيْن", ["اللَّذَان", "اللَّتَيْن", "الَّذِي"], "Masculine dual, accusative."),
        M("Which pronoun goes with الْمُعَلِّمَتَيْن after مَعَ?", "اللَّتَيْن", ["اللَّتَان", "اللَّذَيْن", "الَّتِي"], "Feminine dual, genitive."),
        M("What does الْكِتَابَان اللَّذَان عَلَى الطَّاوِلَة جَدِيدَان mean?", "The two books that are on the table are new", ["The book on the table is new", "The books are on two tables", "Two tables are new"], "كِتَابَان = two books."),
        M("What does the verb in the clause look like after اللَّذَان?", "dual (يَعْمَلَان)", ["singular (يَعْمَل)", "plural (يَعْمَلُون)", "feminine (تَعْمَل)"], "Two doers → dual verb."),
        F("الْمُهَنْدِسَان ___ يَعْمَلَان هُنَا مِنْ مِصْر.", "اللَّذَان", ["اللَّتَان", "الَّذِي", "اللَّذَيْن"], "Subject, masculine dual.", tr="The two engineers who work here are from Egypt."),
        F("شَاهَدْتُ الْمُهَنْدِسَيْن ___ يَعْمَلَان هُنَا.", "اللَّذَيْن", ["اللَّذَان", "اللَّتَيْن", "الَّذِين"], "Object, masculine dual.", tr="I saw the two engineers who work here."),
        F("الْمُعَلِّمَتَان اللَّتَان ___ الْعَرَبِيَّة مِنَ الْأُرْدُنّ.", "تُدَرِّسَان", ["تُدَرِّس", "يُدَرِّسَان", "تُدَرِّسْنَ"], "Two women: dual feminine verb.", tr="The two teachers who teach Arabic are from Jordan."),
    ],
    verify=(vd("مُهَنْدِس", "مُهَنْدِسَان", "مُهَنْدِسَيْن") + vd("كِتَاب", "كِتَابَان", "كِتَابَيْن")
            + vv("عمل", "pres", huma_m="يَعْمَلَان") + vv("درس#2", "pres", huma_f="تُدَرِّسَان")
            + vw("اللَّذَان", "اللَّذَيْن", "اللَّتَان", "اللَّتَيْن", "الْمُهَنْدِسَان", "الْمُهَنْدِسَيْن", "الْمُعَلِّمَتَان", "الْمُعَلِّمَتَيْن", "يَعْمَلَان", "تُدَرِّسَان", "الصَّدِيقَان", "طَالِبَان", "جَيِّدَان", "الْكِتَابَان", "جَدِيدَان", "تُدَرِّسْنَ", "يُدَرِّسَان", "شَاهَدْتُ", "تَكَلَّمْتُ")),
)

# ---------------------------------------------------------------------------- 280
L280 = lesson(
    "Many of them: الَّذِين and اللَّاتِي",
    "الرِّجَال الَّذِين · الْمُعَلِّمَات اللَّاتِي · الْكُتُب الَّتِي",
    requires=["الذي", "رجل", "معلم", "كتاب", "عمل", "طالب", "مهندس", "درس"],
    cards=[
        card("The six pronouns in one chart",
             "For three or more people, men take الَّذِين and women take اللَّاتِي. Some writers also use الَّتِي for women in the plural, but this course teaches اللَّاتِي. For a plural of things, remember the rule you learned earlier: it counts as feminine singular, so use الَّتِي.",
             tables=[table(["", "Masculine", "Feminine"],
                           [["singular", "الَّذِي", "الَّتِي"], ["dual, subject", "اللَّذَان", "اللَّتَان"], ["dual, object", "اللَّذَيْن", "اللَّتَيْن"],
                            ["plural (people)", "الَّذِين", "اللَّاتِي"], ["plural (things)", "الَّتِي", "الَّتِي"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "The verb inside the clause agrees with the antecedent: يَعْمَلُون for men, يَعْمَلْنَ for women, تَقَع or تَكُون for things.",
             examples=[
                 ex("الرِّجَال الَّذِين يَعْمَلُون هُنَا مِنْ مِصْر.", "The men who work here are from Egypt.", "الَّذِين"),
                 ex("الْمُعَلِّمَات اللَّاتِي يُدَرِّسْنَ الْعَرَبِيَّة مِنَ الْأُرْدُنّ.", "The women teachers who teach Arabic are from Jordan.", "اللَّاتِي"),
                 ex("الطُّلَّاب الَّذِين وَصَلُوا أَمْس يَدْرُسُون مَعَنَا.", "The students who arrived yesterday are studying with us.", "الَّذِين"),
                 ex("الْكُتُب الَّتِي عَلَى الطَّاوِلَة قَدِيمَة.", "The books that are on the table are old.", "الَّتِي"),
                 ex("الْمُدُن الَّتِي عَلَى السَّاحِل كَبِيرَة.", "The cities that are on the coast are big.", "الَّتِي"),
                 ex("الْبَنَات اللَّاتِي يَلْعَبْنَ فِي الْحَدِيقَة صَغِيرَات.", "The girls who are playing in the garden are small.", "اللَّاتِي"),
             ]),
    ],
    exercises=[
        M("Which pronoun goes with الرِّجَال (men)?", "الَّذِين", ["اللَّاتِي", "الَّذِي", "اللَّذَان"], "Plural masculine people."),
        M("Which pronoun goes with الْمُعَلِّمَات (women teachers)?", "اللَّاتِي", ["الَّذِين", "الَّذِي", "اللَّتَان"], "Plural feminine people."),
        M("Which pronoun goes with الْكُتُب (books)?", "الَّتِي", ["الَّذِين", "اللَّتَان", "الَّذِي"], "A plural of things counts as feminine singular."),
        M("Which pronoun goes with الْمُدُن (cities)?", "الَّتِي", ["اللَّذَان", "الَّذِين", "اللَّتَان"], "Cities are things."),
        M("What does الطُّلَّاب الَّذِين وَصَلُوا أَمْس يَدْرُسُون مَعَنَا mean?", "The students who arrived yesterday are studying with us", ["The students who studied arrived yesterday", "We arrived with the students", "The students will study tomorrow"], "الَّذِين = who (men)."),
        M("Which verb fits: الْبَنَات اللَّاتِي ___ فِي الْحَدِيقَة", "يَلْعَبْنَ", ["يَلْعَبُون", "يَلْعَب", "تَلْعَبَان"], "Women (plural): ـْنَ."),
        F("الرِّجَال ___ يَعْمَلُون هُنَا مِنْ مِصْر.", "الَّذِين", ["اللَّاتِي", "الَّذِي", "الَّتِي"], "Men, plural.", tr="The men who work here are from Egypt."),
        F("الْكُتُب ___ عَلَى الطَّاوِلَة قَدِيمَة.", "الَّتِي", ["الَّذِين", "اللَّاتِي", "الَّذِي"], "A plural of things.", tr="The books that are on the table are old."),
        F("الْمُعَلِّمَات اللَّاتِي ___ الْعَرَبِيَّة مِنَ الْأُرْدُنّ.", "يُدَرِّسْنَ", ["يُدَرِّسُون", "تُدَرِّس", "يُدَرِّسَان"], "Women (plural).", tr="The women teachers who teach Arabic are from Jordan."),
    ],
    verify=(vv("عمل", "pres", hum="يَعْمَلُون", hunna="يَعْمَلْنَ") + vv("لعب", "pres", hunna="يَلْعَبْنَ", hum="يَلْعَبُون") + vv("درس#2", "pres", hunna="يُدَرِّسْنَ", hum="يُدَرِّسُون")
            + vv("درس", "pres", hum="يَدْرُسُون") + vv("وصل", "past", hum="وَصَلُوا")
            + vpb("رَجُل", "رِجَال") + vpb("كِتَاب", "كُتُب") + vpb("مَدِينَة", "مُدُن") + vpb("طَالِب", "طُلَّاب") + vpb("بِنْت", "بَنَات")
            + vw("الرِّجَال", "الْمُعَلِّمَات", "الطُّلَّاب", "الْكُتُب", "الْمُدُن", "السَّاحِل", "الْبَنَات", "الْحَدِيقَة", "صَغِيرَات", "قَدِيمَة", "يَلْعَبْنَ", "يُدَرِّسْنَ", "تَلْعَبَان", "تَقَع", "تَكُون")),
)

# ---------------------------------------------------------------------------- 281
L281 = lesson(
    "A pronoun that points back",
    "الْكِتَاب الَّذِي قَرَأْتُهُ · الْمَدِينَة الَّتِي أَسْكُن فِيهَا",
    requires=["الذي", "كتاب", "قرأ", "مدينة", "سكن", "مع", "في", "هو", "هي"],
    cards=[
        card("When the noun is not the doer",
             "In “the man who works here”, the man is the doer and is already the subject of the clause, so nothing more is needed. But in “the book that I read”, the book is the object of the verb, not its subject. "
             "Arabic then adds a pronoun inside the clause that points back to the noun: “the book that I read it”. Match it to the noun: ـهُ for a masculine singular, ـهَا for a feminine singular or a plural of things, ـهُمْ for several men.",
             tables=[table(["English", "Arabic"],
                           [["the book that I read", "الْكِتَاب الَّذِي قَرَأْتُهُ"], ["the city that I live in", "الْمَدِينَة الَّتِي أَسْكُن فِيهَا"], ["the woman that I spoke with", "الْمَرْأَة الَّتِي تَكَلَّمْتُ مَعَهَا"],
                            ["the books that I read", "الْكُتُب الَّتِي قَرَأْتُهَا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("More examples",
             "Compare these with the lesson on الَّذِي and الَّتِي: there the noun was the doer, so no pronoun was added.",
             examples=[
                 ex("الْكِتَاب الَّذِي قَرَأْتُهُ جَمِيل.", "The book that I read is beautiful.", "قَرَأْتُهُ"),
                 ex("الْمَدِينَة الَّتِي أَسْكُن فِيهَا كَبِيرَة.", "The city that I live in is big.", "فِيهَا"),
                 ex("الرَّجُل الَّذِي رَأَيْتُهُ فِي الْمَطَار مُهَنْدِس.", "The man whom I saw at the airport is an engineer.", "رَأَيْتُهُ"),
                 ex("الْمَرْأَة الَّتِي تَكَلَّمْتُ مَعَهَا مُعَلِّمَة.", "The woman I spoke with is a teacher.", "مَعَهَا"),
                 ex("الْكُتُب الَّتِي قَرَأْتُهَا قَدِيمَة.", "The books that I read are old.", "قَرَأْتُهَا"),
                 ex("الطُّلَّاب الَّذِين تَكَلَّمْتُ مَعَهُمْ مِنْ مِصْر.", "The students I spoke with are from Egypt.", "مَعَهُمْ"),
             ]),
    ],
    exercises=[
        M("Which completes “الْكِتَاب الَّذِي قَرَأْتُ…”?", "ـهُ", ["ـهَا", "ـهُمْ", "ـكَ"], "كِتَاب is masculine singular."),
        M("Which completes “الْمَدِينَة الَّتِي أَسْكُن فِي…”?", "ـهَا", ["ـهُ", "ـهُمْ", "ـكَ"], "مَدِينَة is feminine singular."),
        M("Which completes “الْكُتُب الَّتِي قَرَأْتُ…”?", "ـهَا", ["ـهُ", "ـهُمْ", "ـنَا"], "Books are things: ـهَا."),
        M("Which completes “الطُّلَّاب الَّذِين تَكَلَّمْتُ مَعَ…”?", "ـهُمْ", ["ـهُ", "ـهَا", "ـهُنَّ"], "Several men."),
        M("In which phrase is no returning pronoun needed?", "الرَّجُل الَّذِي يَعْمَل هُنَا", ["الْكِتَاب الَّذِي قَرَأْتُ", "الْمَدِينَة الَّتِي أَسْكُن فِي", "الْمَرْأَة الَّتِي تَكَلَّمْتُ مَعَ"], "The man is the doer."),
        M("What does الرَّجُل الَّذِي رَأَيْتُهُ فِي الْمَطَار مُهَنْدِس mean?", "The man whom I saw at the airport is an engineer", ["The man who saw me is an engineer", "The engineer works at the airport", "I am the engineer"], "رَأَيْتُهُ = I saw him."),
        F("الْكِتَاب الَّذِي ___ جَمِيل.", "قَرَأْتُهُ", ["قَرَأْتُهَا", "قَرَأْتُهُمْ", "قَرَأَ"], "The book is masculine; I read it.", tr="The book that I read is beautiful."),
        F("الْمَدِينَة الَّتِي أَسْكُن ___ كَبِيرَة.", "فِيهَا", ["فِيهِ", "فِيهِمْ", "فِيكَ"], "The city is feminine.", tr="The city that I live in is big."),
        F("الْمَرْأَة الَّتِي تَكَلَّمْتُ ___ مُعَلِّمَة.", "مَعَهَا", ["مَعَهُ", "مَعَهُمْ", "مَعَهُنَّ"], "The woman is feminine singular.", tr="The woman I spoke with is a teacher."),
    ],
    verify=(vv("قرأ", "past", ana="قَرَأْتُ") + vv("سكن", "pres", ana="أَسْكُن")
            + vw("قَرَأْتُهُ", "قَرَأْتُهَا", "قَرَأْتُهُمْ", "فِيهَا", "فِيهِ", "فِيهِمْ", "فِيكَ", "رَأَيْتُهُ", "مَعَهَا", "مَعَهُ", "مَعَهُمْ", "مَعَهُنَّ", "تَكَلَّمْتُ", "جَمِيل", "مُهَنْدِس", "الْمَطَار", "قَرَأَ")),
)

# ---------------------------------------------------------------------------- 282
L282 = lesson(
    "Choosing the right pronoun: practice",
    "الدَّوْلَة الَّتِي تَقَع فِي الشَّمَال · الطُّلَّاب الَّذِين يَدْرُسُون",
    requires=["الذي", "دولة", "عاصمة", "مدينة", "طالب", "كتاب", "وقع", "شمال", "جنوب", "لغة"],
    cards=[
        card("A four-step check",
             "To pick the right pronoun, ask four questions. (1) Is the noun definite? If not, use no pronoun. (2) Is it masculine or feminine? "
             "(3) Is it one, two, or more? (4) Is it a person or a thing? Plural things count as feminine singular. Then decide whether the clause needs a returning pronoun.",
             tables=[table(["Noun", "Check", "Result"],
                           [["الدَّوْلَة", "feminine singular", "الَّتِي"], ["الدُّوَل", "plural things", "الَّتِي"], ["الطَّالِبَان", "masculine dual, subject", "اللَّذَان"],
                            ["الْمُدَرِّسَات", "feminine plural people", "اللَّاتِي"], ["الطُّلَّاب", "masculine plural people", "الَّذِين"]],
                           say=[0, 2], tlit=[2], gloss=False)]),
        card("Geography and people (invented sentences)",
             "These sentences use most of the pronouns you know.",
             examples=[
                 ex("الدَّوْلَة الَّتِي تَقَع فِي شَمَال أَفْرِيقِيَا كَبِيرَة.", "The country that lies in the north of Africa is big.", "الَّتِي"),
                 ex("بَعْض الدُّوَل الَّتِي عَلَى الْخَلِيج غَنِيَّة بِالنَّفْط.", "Some of the countries on the Gulf are rich in oil.", "الَّتِي"),
                 ex("الْعَاصِمَة الَّتِي زُرْتُهَا جَمِيلَة.", "The capital that I visited is beautiful.", "زُرْتُهَا"),
                 ex("الطُّلَّاب الَّذِين يَدْرُسُون مَعِي مِنْ بِلَاد مُخْتَلِفَة.", "The students who study with me are from different countries.", "الَّذِين"),
                 ex("الْمُدَرِّسَات اللَّاتِي يُدَرِّسْنَ اللُّغَة مِنْ بَلَد عَرَبِيّ.", "The women teachers who teach the language are from an Arab country.", "اللَّاتِي"),
                 ex("الْمُهَنْدِسَان اللَّذَان وَصَلَا أَمْس يَعْمَلَان هُنَا.", "The two engineers who arrived yesterday work here.", "اللَّذَان"),
             ]),
    ],
    exercises=[
        M("Which pronoun goes with الدُّوَل (countries)?", "الَّتِي", ["الَّذِين", "اللَّاتِي", "الَّذِي"], "A plural of things."),
        M("Which pronoun goes with الطُّلَّاب (students, men)?", "الَّذِين", ["اللَّاتِي", "الَّتِي", "اللَّذَان"], "Masculine plural people."),
        M("Which pronoun goes with الطَّالِبَان (two students, subject)?", "اللَّذَان", ["اللَّتَان", "الَّذِين", "الَّذِي"], "Masculine dual."),
        M("Which phrase needs a returning pronoun?", "الْعَاصِمَة الَّتِي زُرْتُ…", ["الدَّوْلَة الَّتِي تَقَع", "الطَّالِب الَّذِي يَدْرُس", "الْمُدَرِّسَات اللَّاتِي يُدَرِّسْنَ"], "The capital is what I visited, not the doer."),
        M("What does بَعْض الدُّوَل الَّتِي عَلَى الْخَلِيج غَنِيَّة بِالنَّفْط mean?", "Some of the countries on the Gulf are rich in oil", ["The Gulf is rich in countries", "The oil is in one country", "Countries need oil"], "غَنِيَّة بِـ = rich in."),
        M("Which is correct?", "الْعَاصِمَة الَّتِي زُرْتُهَا", ["الْعَاصِمَة الَّذِي زُرْتُهَا", "الْعَاصِمَة الَّتِي زُرْتُهُ", "عَاصِمَة الَّتِي زُرْتُهَا"], "Feminine pronoun, feminine returning pronoun, definite noun."),
        F("الدَّوْلَة ___ تَقَع فِي شَمَال أَفْرِيقِيَا كَبِيرَة.", "الَّتِي", ["الَّذِي", "الَّذِين", "اللَّاتِي"], "Feminine singular.", tr="The country that lies in the north of Africa is big."),
        F("الطُّلَّاب ___ يَدْرُسُون مَعِي مِنْ بِلَاد مُخْتَلِفَة.", "الَّذِين", ["الَّتِي", "اللَّاتِي", "الَّذِي"], "Masculine plural people.", tr="The students who study with me are from different countries."),
        F("الْعَاصِمَة الَّتِي ___ جَمِيلَة.", "زُرْتُهَا", ["زُرْتُهُ", "زُرْتُهُمْ", "زَارَ"], "The capital is feminine.", tr="The capital that I visited is beautiful.", lemma=None),
    ],
    verify=(vv("زور", "past", ana="زُرْتُ") + vv("وصل", "past", huma_m="وَصَلَا") + vv("درس", "pres", hum="يَدْرُسُون") + vv("درس#2", "pres", hunna="يُدَرِّسْنَ")
            + vpb("دَوْلَة", "دُوَل") + vpb("بَلَد", "بِلَاد")
            + vw("الدَّوْلَة", "الدُّوَل", "أَفْرِيقِيَا", "الْخَلِيج", "غَنِيَّة", "بِالنَّفْط", "الْعَاصِمَة", "زُرْتُهَا", "زُرْتُهُ", "زُرْتُهُمْ", "زَارَ", "مُخْتَلِفَة", "بِلَاد", "عَرَبِيّ", "وَصَلَا", "الْمُدَرِّسَات", "الطَّالِبَان", "اللُّغَة")),
)


# ---------------------------------------------------------------------------- 283
L283 = lesson(
    "Active and passive: who did it?",
    "كَتَبَ الْمُدِير الرِّسَالَة ← كُتِبَتِ الرِّسَالَة",
    requires=["كتب", "فتح", "حمل", "درس", "رسالة", "باب", "حقيبة", "مدير"],
    cards=[
        card("Same event, two angles",
             "In an active sentence the doer is the subject: “the director wrote the letter”. In a passive sentence the thing that receives the action becomes the subject: “the letter was written”, and the doer is usually left out. "
             "In Arabic the passive of a Measure I verb is shown by the vowels alone: ḍamma on the first letter and kasra on the second. The one who receives the action becomes the subject (nominative).",
             tables=[table(["Active (he did)", "Passive (it was done)", "English"],
                           [["كَتَبَ", "كُتِبَ", "wrote → was written"], ["فَتَحَ", "فُتِحَ", "opened → was opened"], ["حَمَلَ", "حُمِلَ", "carried → was carried"], ["دَرَسَ", "دُرِسَ", "studied → was studied"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Matching the receiver",
             "The passive verb agrees with the receiver, which is now the subject: كُتِبَتِ الرِّسَالَة (feminine), فُتِحَ الْبَاب (masculine). A plural of things takes the feminine singular, as always.",
             examples=[
                 ex("كَتَبَ الْمُدِير الرِّسَالَة أَمْس.", "The director wrote the letter yesterday.", "كَتَبَ"),
                 ex("كُتِبَتِ الرِّسَالَة أَمْس.", "The letter was written yesterday.", "كُتِبَتِ"),
                 ex("فَتَحَ الْمُوَظَّف الْبَاب.", "The employee opened the door.", "فَتَحَ"),
                 ex("فُتِحَ الْبَاب فِي الصَّبَاح.", "The door was opened in the morning.", "فُتِحَ"),
                 ex("حُمِلَتِ الْحَقَائِب إِلَى الطَّائِرَة.", "The bags were carried to the plane.", "حُمِلَتِ"),
                 ex("دُرِسَتِ الْمَسْأَلَة بِدِقَّة.", "The issue was studied carefully.", "دُرِسَتِ"),
             ]),
    ],
    exercises=[
        M("Which verb is passive?", "كُتِبَ", ["كَتَبَ", "يَكْتُب", "اُكْتُبْ"], "ḍamma + kasra = passive."),
        M("Which is the passive of فَتَحَ?", "فُتِحَ", ["فَتَحَ", "يَفْتَح", "اِفْتَحْ"], "فُ + تِ…"),
        M("What does فُتِحَ الْبَاب mean?", "The door was opened", ["The door opens", "He opens the door", "Open the door"], "Passive past."),
        M("What does كُتِبَتِ الرِّسَالَة mean?", "The letter was written", ["The letter writes", "She wrote the letter", "The writer is here"], "Passive past, feminine."),
        M("In a passive sentence, who becomes the subject?", "the one who receives the action", ["the one who does the action", "the teacher", "the verb’s root"], "The receiver becomes the subject; the doer is usually left out."),
        M("Why is it كُتِبَتِ الرِّسَالَة but فُتِحَ الْبَاب؟", "the verb agrees with the receiver", ["the letter is plural", "the door is a person", "it is a command"], "رِسَالَة is feminine; بَاب is masculine."),
        F("___ الْبَاب فِي الصَّبَاح.", "فُتِحَ", ["فَتَحَ", "يَفْتَح", "فَتَحَتْ"], "The door received the action.", tr="The door was opened in the morning.", lemma="فتح:ppast:huwa"),
        F("___ الْحَقَائِب إِلَى الطَّائِرَة.", "حُمِلَتِ", ["حُمِلَ", "حَمَلَتِ", "يُحْمَل"], "A plural of things → feminine singular, passive.", tr="The bags were carried to the plane."),
        F("___ الْمُدِير الرِّسَالَة أَمْس.", "كَتَبَ", ["كُتِبَ", "كُتِبَتْ", "يُكْتَب"], "The director is the doer: active.", tr="The director wrote the letter yesterday."),
    ],
    verify=(vv("كتب", "ppast", huwa="كُتِبَ", hiya="كُتِبَتْ") + vv("فتح", "ppast", huwa="فُتِحَ") + vv("حمل", "ppast", hiya="حُمِلَتْ") + vv("درس", "ppast", hiya="دُرِسَتْ", huwa="دُرِسَ")
            + vv("كتب", "past", huwa="كَتَبَ") + vv("فتح", "past", huwa="فَتَحَ") + vv("حمل", "past", huwa="حَمَلَ") + vv("درس", "past", huwa="دَرَسَ")
            + vw("الْمُدِير", "الرِّسَالَة", "كُتِبَتِ", "حُمِلَتِ", "دُرِسَتِ", "الْمَسْأَلَة", "بِدِقَّة", "جَيِّدًا", "الْحَقَائِب", "الْبَاب", "فَتَحَتْ", "يُحْمَل", "يُكْتَب", "كُتِبَتْ", "اُكْتُبْ", "اِفْتَحْ")),
)

# ---------------------------------------------------------------------------- 284
L284 = lesson(
    "The past passive: all third persons",
    "كُتِبَ · كُتِبَتْ · كُتِبَا · كُتِبُوا",
    requires=["كتب", "كتاب", "رسالة", "قصة", "مدينة", "فتح", "بنى", "طالب"],
    cards=[
        card("Endings are the usual ones",
             "The passive past changes only the inside vowels. The endings stay the ones you know, and, when the receiver comes first, they match it in gender and number.",
             tables=[table(["Receiver", "Passive of كَتَبَ", "English"],
                           [["one male", "كُتِبَ", "it/he was written"], ["one female", "كُتِبَتْ", "it/she was written"], ["two males", "كُتِبَا", "the two were written"],
                            ["two females", "كُتِبَتَا", "the two (f.) were written"], ["men (plural)", "كُتِبُوا", "they were written"], ["women (plural)", "كُتِبْنَ", "they (f.) were written"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("After the subject, the verb agrees fully",
             "When the receiver comes first, the verb after it agrees in gender and number. Remember that plural things take the feminine singular, so a passive verb after الْكُتُب is كُتِبَتْ.",
             examples=[
                 ex("الْكِتَاب كُتِبَ فِي الْقَاهِرَة.", "The book was written in Cairo.", "كُتِبَ"),
                 ex("الْقِصَّة كُتِبَتْ قَبْل سَنَوَات.", "The story was written years ago.", "كُتِبَتْ"),
                 ex("الْكِتَابَان كُتِبَا فِي سَنَة وَاحِدَة.", "The two books were written in one year.", "كُتِبَا"),
                 ex("الْكُتُب كُتِبَتْ بِالْعَرَبِيَّة.", "The books were written in Arabic.", "كُتِبَتْ"),
                 ex("فُتِحَتِ الْمَدْرَسَة قَبْل سَنَة.", "The school was opened a year ago.", "فُتِحَتِ"),
                 ex("فُتِحَتِ الْمَدَارِس فِي أُكْتُوبَر.", "The schools were opened in October.", "فُتِحَتِ"),
             ]),
    ],
    exercises=[
        M("Which means “the story was written”?", "كُتِبَتِ الْقِصَّة", ["كُتِبَ الْقِصَّة", "كَتَبَتِ الْقِصَّة", "كُتِبُوا الْقِصَّة"], "Feminine receiver."),
        M("The receiver comes first: الْكِتَابَان ___ (the two books were written). Which fits?", "كُتِبَا", ["كُتِبَ", "كُتِبَتْ", "كُتِبُوا"], "Dual masculine."),
        M("Which fits الْكُتُب (books, things)?", "كُتِبَتْ", ["كُتِبُوا", "كُتِبَ", "كُتِبَا"], "Plural of things → feminine singular."),
        M("Which is the masculine plural passive past of كَتَبَ (they were written)?", "كُتِبُوا", ["كُتِبَتْ", "كُتِبَا", "كُتِبْنَ"], "Plural masculine people."),
        M("What does فُتِحَتِ الْمَدْرَسَة قَبْل سَنَة mean?", "The school was opened a year ago", ["The school opens every year", "The teacher opened the school", "The school will open next year"], "قَبْل = before, ago."),
        M("What does الْكُتُب كُتِبَتْ بِالْعَرَبِيَّة mean?", "The books were written in Arabic", ["The books write in Arabic", "He wrote the books", "The books are for Arabs"], "بِالْعَرَبِيَّة = in Arabic."),
        F("الْكِتَاب ___ فِي الْقَاهِرَة.", "كُتِبَ", ["كُتِبَتْ", "كُتِبَا", "كُتِبُوا"], "Masculine singular.", tr="The book was written in Cairo.", lemma="كتب:ppast:huwa"),
        F("الْقِصَّة ___ قَبْل سَنَوَات.", "كُتِبَتْ", ["كُتِبَ", "كُتِبَا", "كُتِبُوا"], "Feminine singular.", tr="The story was written years ago.", lemma="كتب:ppast:hiya"),
        F("الْكِتَابَان ___ فِي سَنَة وَاحِدَة.", "كُتِبَا", ["كُتِبَ", "كُتِبَتْ", "كُتِبُوا"], "Two books: dual.", tr="The two books were written in one year.", lemma="كتب:ppast:huma_m"),
    ],
    verify=(vv("كتب", "ppast", huwa="كُتِبَ", hiya="كُتِبَتْ", huma_m="كُتِبَا", huma_f="كُتِبَتَا", hum="كُتِبُوا", hunna="كُتِبْنَ") + vv("فتح", "ppast", hiya="فُتِحَتْ")
            + vd("كِتَاب", "كِتَابَان", "كِتَابَيْن") + vpb("كِتَاب", "كُتُب") + vpb("مَدْرَسَة", "مَدَارِس")
            + vw("الْقِصَّة", "الْكِتَابَان", "كُتِبَتَا", "سَنَوَات", "بِالْعَرَبِيَّة", "فُتِحَتِ", "الْمَدْرَسَة", "الْمَدَارِس", "أُكْتُوبَر", "كَتَبَتِ", "الْقَاهِرَة", "كُتِبْنَ")),
)

# ---------------------------------------------------------------------------- 285
L285 = lesson(
    "The present passive: يُكْتَب · يُفْتَح",
    "تُكْتَب الْعَرَبِيَّة مِنَ الْيَمِين إِلَى الْيَسَار",
    requires=["كتب", "فتح", "سمع", "قرأ", "يمين", "يسار", "متحف", "جريدة", "صوت"],
    cards=[
        card("Prefix with ḍamma, middle letter with fatḥa",
             "In the present, the passive has a ḍamma on the prefix and a fatḥa on the second root letter: يَكْتُب (he writes) becomes يُكْتَب (it is written). The endings stay the same.",
             tables=[table(["Active (he does)", "Passive (it is done)", "English"],
                           [["يَكْتُب", "يُكْتَب", "writes → is written"], ["يَفْتَح", "يُفْتَح", "opens → is opened"], ["يَسْمَع", "يُسْمَع", "hears → is heard"], ["يَقْرَأ", "يُقْرَأ", "reads → is read"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("General facts",
             "The passive present is perfect for facts about how things are done or where things can be found, without naming a doer. These sentences are simple facts.",
             examples=[
                 ex("تُكْتَب الْعَرَبِيَّة مِنَ الْيَمِين إِلَى الْيَسَار.", "Arabic is written from right to left.", "تُكْتَب"),
                 ex("يُفْتَح الْمَتْحَف فِي التَّاسِعَة صَبَاحًا.", "The museum is opened at nine in the morning.", "يُفْتَح"),
                 ex("تُقْرَأ الْجَرِيدَة كُلّ يَوْم.", "The newspaper is read every day.", "تُقْرَأ"),
                 ex("يُسْمَع الصَّوْت مِنْ بَعِيد.", "The sound is heard from far away.", "يُسْمَع"),
                 ex("تُفْتَح الْمَحَلَّات فِي الصَّبَاح.", "The shops are opened in the morning.", "تُفْتَح"),
                 ex("سَتُكْتَب الرِّسَالَة غَدًا.", "The letter will be written tomorrow.", "سَتُكْتَب"),
             ]),
    ],
    exercises=[
        M("Which is the present passive of يَكْتُب?", "يُكْتَب", ["يَكْتُب", "كُتِبَ", "اُكْتُبْ"], "يُ + كْتَب."),
        M("Which is the present passive of يَفْتَح?", "يُفْتَح", ["فُتِحَ", "يَفْتَح", "اِفْتَحْ"], "ḍamma on the prefix, fatḥa on the middle."),
        M("What does تُقْرَأ الْجَرِيدَة كُلّ يَوْم mean?", "The newspaper is read every day", ["She reads the newspaper every day", "The newspaper was read yesterday", "Read the newspaper"], "Present passive."),
        M("What does تُكْتَب الْعَرَبِيَّة مِنَ الْيَمِين إِلَى الْيَسَار mean?", "Arabic is written from right to left", ["Arabic writes from left to right", "Arabs write letters", "Arabic was written in the north"], "مِنَ الْيَمِين = from the right."),
        M("Why is it تُفْتَح الْمَحَلَّات, not يُفْتَح؟", "a plural of things takes the feminine singular", ["shops are always feminine people", "it is a command", "it is the past"], "Plural things → feminine singular."),
        M("Which sentence is in the future?", "سَتُكْتَب الرِّسَالَة غَدًا", ["تُكْتَب الرِّسَالَة", "كُتِبَتِ الرِّسَالَة", "كَتَبَتِ الرِّسَالَة"], "سَـ = will."),
        F("___ الْمَتْحَف فِي التَّاسِعَة صَبَاحًا.", "يُفْتَح", ["يَفْتَح", "فُتِحَ", "تُفْتَح"], "A masculine receiver, present, passive.", tr="The museum is opened at nine in the morning.", lemma="فتح:ppres:huwa"),
        F("___ الْمَحَلَّات فِي الصَّبَاح.", "تُفْتَح", ["يُفْتَح", "تَفْتَح", "فُتِحَتْ"], "Things in the plural → feminine singular.", tr="The shops are opened in the morning.", lemma="فتح:ppres:hiya"),
        F("___ الصَّوْت مِنْ بَعِيد.", "يُسْمَع", ["يَسْمَع", "سُمِعَ", "تُسْمَع"], "Masculine singular, passive.", tr="The sound is heard from far away.", lemma="سمع:ppres:huwa"),
    ],
    verify=(vv("كتب", "ppres", huwa="يُكْتَب", hiya="تُكْتَب") + vv("فتح", "ppres", huwa="يُفْتَح", hiya="تُفْتَح") + vv("سمع", "ppres", huwa="يُسْمَع") + vv("قرأ", "ppres", hiya="تُقْرَأ", huwa="يُقْرَأ")
            + vv("كتب", "fut", hiya="سَتَكْتُب")
            + vw("تُكْتَب", "الْيَمِين", "الْيَسَار", "الْمَتْحَف", "التَّاسِعَة", "الْجَرِيدَة", "الصَّوْت", "بَعِيد", "الْمَحَلَّات", "سَتُكْتَب", "الْعَرَبِيَّة", "يَسْمَع", "تَفْتَح", "تُسْمَع")),
)

# ---------------------------------------------------------------------------- 286
L286 = lesson(
    "Passive of hollow, defective and assimilated verbs",
    "قِيلَ · بِيعَ · بُنِيَ · وُجِدَ",
    requires=["قال", "باع", "بنى", "وجد", "سوق", "مسجد", "قديم", "فاكهة", "مطعم"],
    cards=[
        card("Verbs with a weak letter follow their own patterns",
             "Hollow verbs (middle و or ي) have a long ī in the passive past: قَالَ becomes قِيلَ, and بَاعَ becomes بِيعَ. In the present they have a long ā: يُقَال, يُبَاع. "
             "Defective verbs end in a long ā or a short ī: بَنَى becomes بُنِيَ, يُبْنَى. Assimilated verbs bring back their و: وَجَدَ becomes وُجِدَ and يُوجَد.",
             tables=[table(["Active past", "Passive past", "Passive present", "English"],
                           [["قَالَ", "قِيلَ", "يُقَال", "said → was said, is said"], ["بَاعَ", "بِيعَ", "يُبَاع", "sold → was sold, is sold"], ["بَنَى", "بُنِيَ", "يُبْنَى", "built → was built, is built"],
                            ["وَجَدَ", "وُجِدَ", "يُوجَد", "found → was found, is found"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "يُوجَد is very common and means “there is” or “there exists”. يُقَال إِنَّ… means “it is said that…”. The sentences are invented.",
             examples=[
                 ex("يُوجَد مَطْعَم قَرِيب مِنَ الْفُنْدُق.", "There is a restaurant close to the hotel.", "يُوجَد"),
                 ex("بُنِيَ هَذَا الْمَسْجِد قَبْل مِئَة سَنَة.", "This mosque was built a hundred years ago.", "بُنِيَ"),
                 ex("تُبَاع الْفَوَاكِه فِي السُّوق.", "Fruit is sold in the market.", "تُبَاع"),
                 ex("بِيعَ الْبَيْت الْقَدِيم أَمْس.", "The old house was sold yesterday.", "بِيعَ"),
                 ex("وُجِدَتِ الْحَقِيبَة فِي الْمَطَار.", "The bag was found at the airport.", "وُجِدَتِ"),
                 ex("يُقَال إِنَّ الطَّقْس جَمِيل فِي الرَّبِيع.", "It is said that the weather is lovely in spring.", "يُقَال"),
             ]),
    ],
    exercises=[
        M("Which is the passive past of قَالَ?", "قِيلَ", ["قَالَ", "يُقَال", "قُلْ"], "Long ī in the middle."),
        M("Which is the passive past of بَاعَ?", "بِيعَ", ["بَاعَ", "يُبَاع", "بِعْ"], "بِيعَ = was sold."),
        M("Which is the passive present of وَجَدَ?", "يُوجَد", ["يَجِد", "وُجِدَ", "جِدْ"], "The و returns in the passive."),
        M("What does يُوجَد مَطْعَم قَرِيب مِنَ الْفُنْدُق mean?", "There is a restaurant close to the hotel", ["He finds a restaurant", "A restaurant was built", "The hotel is a restaurant"], "يُوجَد = there is."),
        M("What does بُنِيَ هَذَا الْمَسْجِد قَبْل مِئَة سَنَة mean?", "This mosque was built a hundred years ago", ["This mosque will be built soon", "A hundred mosques were built", "He builds mosques"], "بُنِيَ = was built."),
        M("What does يُقَال إِنَّ… introduce?", "something people say", ["a command", "a question", "a name"], "يُقَال إِنَّ = it is said that."),
        F("___ الْفَوَاكِه فِي السُّوق.", "تُبَاع", ["يُبَاع", "بَاعَ", "تَبِيع"], "Things in the plural → feminine singular, passive.", tr="Fruit is sold in the market.", lemma="بيع:ppres:hiya"),
        F("___ هَذَا الْمَسْجِد قَبْل مِئَة سَنَة.", "بُنِيَ", ["بَنَى", "يُبْنَى", "بُنِيَتْ"], "A masculine receiver, past, passive.", tr="This mosque was built a hundred years ago.", lemma="بني:ppast:huwa"),
        F("___ الْحَقِيبَة فِي الْمَطَار.", "وُجِدَتِ", ["وُجِدَ", "وَجَدَتِ", "تُوجَد"], "A feminine receiver, past, passive.", tr="The bag was found at the airport."),
    ],
    verify=(vv("قول", "ppast", huwa="قِيلَ") + vv("قول", "ppres", huwa="يُقَال") + vv("بيع", "ppast", huwa="بِيعَ") + vv("بيع", "ppres", huwa="يُبَاع", hiya="تُبَاع")
            + vv("بني", "ppast", huwa="بُنِيَ") + vv("بني", "ppres", huwa="يُبْنَى") + vv("وجد", "ppast", huwa="وُجِدَ", hiya="وُجِدَتْ") + vv("وجد", "ppres", huwa="يُوجَد")
            + vw("مَطْعَم", "قَرِيب", "الْفُنْدُق", "الْمَسْجِد", "تُبَاع", "الْفَوَاكِه", "السُّوق", "الْقَدِيم", "الرَّبِيع", "وُجِدَتِ", "الْبَيْت", "قُلْ", "بِعْ", "جِدْ", "تَبِيع", "بُنِيَتْ", "وَجَدَتِ", "تُوجَد", "يَجِد")),
)

# ---------------------------------------------------------------------------- 287
L287 = lesson(
    "Using the passive well",
    "يُسَمَّى · يُعْرَف · يُسْتَخْدَم · تُسَمَّى الْقَاهِرَة…",
    requires=["سمى", "عرف", "نيل", "طول", "فعل", "مجهول"],
    cards=[
        card("When Arabic uses the passive",
             "Choose the passive when the doer is unknown, unimportant, or obvious, and in news and general descriptions. A few passive verbs are so common that you should learn them as phrases: "
             "يُسَمَّى (is called), يُعْرَف بِـ (is known for), يُسْتَخْدَم (is used).",
             tables=[table(["English", "Arabic"],
                           [["is called", "يُسَمَّى"], ["is known for its length", "يُعْرَف بِطُولِهِ"], ["is used", "يُسْتَخْدَم"], ["is said", "يُقَال"], ["there is", "يُوجَد"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Descriptions",
             "These sentences describe well-known things in a simple way.",
             examples=[
                 ex("تُسَمَّى الْقَاهِرَة مَدِينَة الْأَلْف مِئْذَنَة.", "Cairo is called the city of a thousand minarets.", "تُسَمَّى"),
                 ex("يُعْرَف النِّيل بِطُولِهِ.", "The Nile is known for its length.", "يُعْرَف"),
                 ex("يُسْتَخْدَم الْهَاتِف فِي كُلّ مَكَان.", "The telephone is used everywhere.", "يُسْتَخْدَم"),
                 ex("تُسْتَخْدَم الْعَرَبِيَّة فِي كَثِير مِنَ الْبِلَاد.", "Arabic is used in many countries.", "تُسْتَخْدَم"),
                 ex("يُعْرَف هَذَا الْمَطْعَم بِالْقَهْوَة الْجَيِّدَة.", "This restaurant is known for good coffee.", "يُعْرَف"),
                 ex("يُقَال إِنَّ الْمَدِينَة قَدِيمَة جِدًّا.", "It is said that the city is very old.", "يُقَال"),
             ]),
    ],
    exercises=[
        M("What does يُسَمَّى mean?", "is called", ["is used", "is known for", "is opened"], "سَمَّى = to name."),
        M("What does يُسْتَخْدَم mean?", "is used", ["is called", "is built", "is found"], "اِسْتَخْدَمَ = to use."),
        M("What does يُعْرَف النِّيل بِطُولِهِ mean?", "The Nile is known for its length", ["The Nile knows its length", "The Nile was measured yesterday", "The Nile is short"], "يُعْرَف بِـ = is known for."),
        M("What does تُسْتَخْدَم الْعَرَبِيَّة فِي كَثِير مِنَ الْبِلَاد mean?", "Arabic is used in many countries", ["Arabs use one country", "Arabic was used yesterday", "Many countries speak one Arab"], "كَثِير مِنَ = many of."),
        M("When is the passive a good choice?", "when the doer is unknown or unimportant", ["when you give a command", "when you ask a question", "when you count things"], "The passive hides the doer."),
        M("What does يُوجَد mean?", "there is", ["he finds", "it was found yesterday", "find!"], "Passive of وَجَدَ."),
        F("___ الْقَاهِرَة مَدِينَة الْأَلْف مِئْذَنَة.", "تُسَمَّى", ["يُسَمَّى", "سَمَّتْ", "تُسَمِّي"], "Cairo is feminine; it receives the name.", tr="Cairo is called the city of a thousand minarets."),
        F("___ النِّيل بِطُولِهِ.", "يُعْرَف", ["يَعْرِف", "عَرَفَ", "تُعْرَف"], "Masculine, passive, present.", tr="The Nile is known for its length.", lemma="عرف:ppres:huwa"),
        F("___ الْهَاتِف فِي كُلّ مَكَان.", "يُسْتَخْدَم", ["يَسْتَخْدِم", "اِسْتَخْدَمَ", "تُسْتَخْدَم"], "Masculine, passive.", tr="The telephone is used everywhere."),
    ],
    verify=(vv("عرف", "ppres", huwa="يُعْرَف") + vv("خدم#10", "pres", huwa="يَسْتَخْدِم") + vv("خدم#10", "past", huwa="اِسْتَخْدَمَ")
            + vw("تُسَمَّى", "يُسَمَّى", "يُعْرَف", "يُسْتَخْدَم", "تُسْتَخْدَم", "الْقَاهِرَة", "الْأَلْف", "مِئْذَنَة", "النِّيل", "بِطُولِهِ", "الْهَاتِف", "مَكَان", "الْبِلَاد", "بِالْقَهْوَة", "الْجَيِّدَة", "جِدًّا", "سَمَّتْ", "تُسَمِّي", "يَعْرِف", "عَرَفَ", "تُعْرَف", "يَسْتَخْدِم", "اِسْتَخْدَمَ")),
)

# ---------------------------------------------------------------------------- 288
L288 = lesson(
    "Measure VII: اِنْفَعَلَ",
    "كَسَرَ ← اِنْكَسَرَ · فَتَحَ ← اِنْفَتَحَ",
    requires=["كسر", "فتح", "قطع", "طريق", "سيارة", "طائرة", "باب", "زجاج"],
    cards=[
        card("It happened by itself",
             "Measure VII has the pattern اِنْفَعَلَ: add اِنْ before the root. It describes something that happens to a thing without a doer: كَسَرَ (he broke) → اِنْكَسَرَ (it broke). "
             "The meaning is a bit like the passive, but the vowels are those of an active verb, not the passive pattern, and no doer is mentioned. The present is يَنْفَعِل.",
             tables=[table(["Measure I", "Measure VII (past)", "Measure VII (present)", "English"],
                           [["كَسَرَ", "اِنْكَسَرَ", "يَنْكَسِر", "it broke"], ["فَتَحَ", "اِنْفَتَحَ", "يَنْفَتِح", "it opened"], ["قَطَعَ", "اِنْقَطَعَ", "يَنْقَطِع", "it was cut off"],
                            ["قَلَبَ", "اِنْقَلَبَ", "يَنْقَلِب", "it turned over"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("Compare I and VII",
             "A transitive Measure I verb needs a doer. Measure VII does not: the door simply opened.",
             examples=[
                 ex("فَتَحَ الْمُوَظَّف الْبَاب.", "The employee opened the door.", "فَتَحَ"),
                 ex("اِنْفَتَحَ الْبَاب.", "The door opened.", "اِنْفَتَحَ"),
                 ex("اِنْكَسَرَ الزُّجَاج.", "The glass broke.", "اِنْكَسَرَ"),
                 ex("اِنْقَطَعَ الطَّرِيق بِسَبَب الْمَطَر.", "The road was cut off because of the rain.", "اِنْقَطَعَ"),
                 ex("اِنْطَلَقَتِ الطَّائِرَة فِي الْعَاشِرَة.", "The plane set off at ten.", "اِنْطَلَقَتِ"),
                 ex("اِنْقَلَبَتِ السَّيَّارَة عَلَى الطَّرِيق.", "The car overturned on the road.", "اِنْقَلَبَتِ"),
             ]),
    ],
    exercises=[
        M("Which is the Measure VII verb of كَسَرَ?", "اِنْكَسَرَ", ["كُسِرَ", "يَكْسِر", "كَسَّرَ"], "اِنْ + the root."),
        M("What does اِنْفَتَحَ الْبَاب mean?", "The door opened", ["He opened the door", "The door was opened by him", "Open the door"], "No doer is mentioned."),
        M("What does اِنْقَطَعَ الطَّرِيق mean?", "The road was cut off", ["He cut the road", "The road is long", "The road opened"], "اِنْقَطَعَ = got cut off."),
        M("What does اِنْطَلَقَتِ الطَّائِرَة فِي الْعَاشِرَة mean?", "The plane set off at ten", ["The plane landed at ten", "The plane was late", "The plane was sold at ten"], "اِنْطَلَقَ = to set off."),
        M("Which of these is Measure VII?", "اِنْقَلَبَ", ["قَلَبَ", "قُلِبَ", "قَالَ"], "اِنْ at the start."),
        M("What is the present of اِنْكَسَرَ?", "يَنْكَسِر", ["يَكْسِر", "يُكْسَر", "اِنْكَسِرْ"], "يَنْ + كَسِر."),
        F("___ الزُّجَاج.", "اِنْكَسَرَ", ["كَسَرَ", "يَكْسِر", "كَسَّرَ"], "No doer: Measure VII.", tr="The glass broke.", lemma="كسر#7:past:huwa"),
        F("___ الْبَاب.", "اِنْفَتَحَ", ["فَتَحَ", "يَفْتَح", "يُفْتَح"], "The door opened by itself.", tr="The door opened.", lemma="فتح#7:past:huwa"),
        F("___ الطَّائِرَة فِي الْعَاشِرَة.", "اِنْطَلَقَتِ", ["اِنْطَلَقَ", "تَنْطَلِق"], "Feminine subject, past.", tr="The plane set off at ten."),
    ],
    verify=(vv("كسر#7", "past", huwa="اِنْكَسَرَ", hiya="اِنْكَسَرَتْ") + vv("كسر#7", "pres", huwa="يَنْكَسِر") + vv("فتح#7", "past", huwa="اِنْفَتَحَ") + vv("فتح#7", "pres", huwa="يَنْفَتِح")
            + vv("قطع#7", "past", huwa="اِنْقَطَعَ") + vv("قطع#7", "pres", huwa="يَنْقَطِع") + vv("قلب#7", "past", huwa="اِنْقَلَبَ") + vv("قلب#7", "pres", huwa="يَنْقَلِب")
            + vv("طلق#7", "past", huwa="اِنْطَلَقَ") + vv("طلق#7", "pres", huwa="يَنْطَلِق")
            + vw("اِنْقَلَبَتِ", "اِنْطَلَقَتِ", "الزُّجَاج", "الطَّرِيق", "السَّيَّارَة", "كَسَّرَ", "يُكْسَر", "كُسِرَ", "اِنْكَسِرْ", "قَلَبَ", "قُلِبَ", "طَلَقَ", "قَطَعَ", "تَنْطَلِق", "قَالَ")),
)

# ---------------------------------------------------------------------------- 289
L289 = lesson(
    "Verbal nouns of Measure VII: اِنْفِعَال",
    "اِنْطِلَاق · اِنْقِطَاع · اِنْفِتَاح · اِنْقِلَاب",
    requires=["كسر", "فتح", "قطع", "سوق", "طائرة", "رحلة", "طريق", "قلب"],
    cards=[
        card("The pattern",
             "The verbal noun of Measure VII is اِنْفِعَال: a kasra on the first root letter and a long ā before the last root letter. It names the event: اِنْطَلَقَ (set off) gives اِنْطِلَاق (departure, launch).",
             tables=[table(["Verb", "Verbal noun", "English"],
                           [["اِنْطَلَقَ", "اِنْطِلَاق", "setting off, start"], ["اِنْقَطَعَ", "اِنْقِطَاع", "interruption, cutting off"], ["اِنْفَتَحَ", "اِنْفِتَاح", "opening up"],
                            ["اِنْكَسَرَ", "اِنْكِسَار", "breaking"], ["اِنْقَلَبَ", "اِنْقِلَاب", "overturning, turn"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Verbal nouns in sentences",
             "Like any verbal noun, these can follow بَعْد or قَبْل, and be the first word of a phrase with another noun after it.",
             examples=[
                 ex("بَعْد اِنْطِلَاق الرِّحْلَة قَرَأْتُ الْجَرِيدَة.", "After the flight’s departure I read the newspaper.", "اِنْطِلَاق"),
                 ex("سَبَب اِنْقِطَاع الطَّرِيق هُوَ الْمَطَر.", "The reason the road is cut off is the rain.", "اِنْقِطَاع"),
                 ex("اِنْفِتَاح الْأَسْوَاق مُهِمّ لِلْبَلَد.", "The opening up of markets is important for the country.", "اِنْفِتَاح"),
                 ex("اِنْكِسَار الزُّجَاج كَانَ بِسَبَب الرِّيح.", "The breaking of the glass was because of the wind.", "اِنْكِسَار"),
                 ex("اِنْقِطَاع الْمَاء مُشْكِلَة كَبِيرَة.", "A cut in the water supply is a big problem.", "اِنْقِطَاع"),
                 ex("قَبْل اِنْطِلَاق الطَّائِرَة نُغْلِق الْأَبْوَاب.", "Before the plane sets off we close the doors.", "اِنْطِلَاق"),
             ]),
    ],
    exercises=[
        M("Which is the verbal noun of اِنْطَلَقَ?", "اِنْطِلَاق", ["اِنْطَلَقَ", "يَنْطَلِق", "مُنْطَلِق"], "اِنْفِعَال pattern."),
        M("Which is the verbal noun of اِنْقَطَعَ?", "اِنْقِطَاع", ["قَطْع", "يَنْقَطِع", "مَقْطُوع"], "اِنْفِعَال pattern."),
        M("Which one is a Measure VII verbal noun?", "اِنْفِتَاح", ["فَتْح", "فُتِحَ", "اِفْتَتَحَ"], "اِنْ…ِ…ا…"),
        M("What does اِنْقِطَاع الْمَاء مُشْكِلَة كَبِيرَة mean?", "A cut in the water supply is a big problem", ["Water is a big problem", "He cut the water", "The big water is gone"], "اِنْقِطَاع = cutting off."),
        M("What does بَعْد اِنْطِلَاق الرِّحْلَة mean?", "after the flight’s departure", ["before the flight’s arrival", "during the delay", "because of the gate"], "بَعْد = after."),
        M("Which pattern is the Measure VII verbal noun?", "اِنْفِعَال", ["تَفْعِيل", "مُفَاعَلَة", "إِفْعَال"], "اِنْفِعَال."),
        F("بَعْد ___ الرِّحْلَة قَرَأْتُ الْجَرِيدَة.", "اِنْطِلَاق", ["اِنْطَلَقَ", "يَنْطَلِق", "اِنْطَلِقْ"], "A noun follows بَعْد.", tr="After the flight’s departure I read the newspaper."),
        F("___ الْأَسْوَاق مُهِمّ لِلْبَلَد.", "اِنْفِتَاح", ["اِنْفَتَحَ", "فَاتِح", "فُتِحَ"], "The Measure VII noun.", tr="The opening up of markets is important for the country."),
        F("قَبْل ___ الطَّائِرَة نُغْلِق الْأَبْوَاب.", "اِنْطِلَاق", ["اِنْطَلَقَتِ", "تَنْطَلِق", "اِنْقِطَاع"], "Before the plane’s departure.", tr="Before the plane sets off we close the doors."),
    ],
    verify=(vv("غلق#4", "pres", nahnu="نُغْلِق")
            + vw("اِنْطِلَاق", "اِنْقِطَاع", "اِنْفِتَاح", "اِنْكِسَار", "اِنْقِلَاب", "الْأَسْوَاق", "لِلْبَلَد", "الرِّيح", "مُشْكِلَة", "الْأَبْوَاب", "مُنْطَلِق", "قَطْع", "مَقْطُوع", "فَتْح", "اِفْتَتَحَ", "فَاتِح", "تَفْعِيل", "اِنْفِعَال", "نُغْلِق", "الْمَاء", "سَبَب")),
)


# ---------------------------------------------------------------------------- 290
L290 = lesson(
    "Where is it? تَقَع فِي…",
    "تَقَع مِصْر فِي شَمَال شَرْق أَفْرِيقِيَا",
    requires=["وقع", "شمال", "جنوب", "غرب", "شبه", "جزيرة", "خليج", "دولة", "بين"],
    cards=[
        card("Compass words and the verb “lie”",
             "The four directions are شَمَال (north), جَنُوب (south), شَرْق (east) and غَرْب (west). Put two together for a corner: شَمَال شَرْق (north-east). "
             "To say where a place lies, use the assimilated verb وَقَعَ: يَقَع (masculine) or تَقَع (feminine), followed by فِي or عَلَى. Many country names are treated as feminine (مِصْر, السُّعُودِيَّة), but some as masculine (الْمَغْرِب, الْيَمَن). Learn each one, or say دَوْلَة + تَقَع.",
             tables=[table(["English", "Arabic"],
                           [["north", "شَمَال"], ["south", "جَنُوب"], ["east", "شَرْق"], ["west", "غَرْب"], ["north-east", "شَمَال شَرْق"], ["it lies (f.)", "تَقَع"], ["it lies (m.)", "يَقَع"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Where in the Arab world",
             "These are simple, well-known facts about where places lie.",
             examples=[
                 ex("تَقَع مِصْر فِي شَمَال شَرْق أَفْرِيقِيَا.", "Egypt lies in the north-east of Africa.", "تَقَع"),
                 ex("يَقَع الْمَغْرِب فِي شَمَال غَرْب أَفْرِيقِيَا.", "Morocco lies in the north-west of Africa.", "يَقَع"),
                 ex("تَقَع السُّعُودِيَّة فِي شِبْه الْجَزِيرَة الْعَرَبِيَّة.", "Saudi Arabia lies in the Arabian Peninsula.", "شِبْه الْجَزِيرَة"),
                 ex("تَقَع الْكُوَيْت عَلَى الْخَلِيج الْعَرَبِيّ.", "Kuwait lies on the Arabian Gulf .", "عَلَى"),
                 ex("تَقَع تُونِس بَيْن الْجَزَائِر وَلِيبِيَا.", "Tunisia lies between Algeria and Libya.", "بَيْن"),
                 ex("يَقَع الْيَمَن فِي جَنُوب شِبْه الْجَزِيرَة.", "Yemen lies in the south of the peninsula.", "جَنُوب"),
             ]),
    ],
    exercises=[
        M("Which word means “east”?", "شَرْق", ["غَرْب", "شَمَال", "جَنُوب"], "شَرْق = east."),
        M("Which word means “south”?", "جَنُوب", ["شَمَال", "شَرْق", "غَرْب"], "جَنُوب = south."),
        M("What does شَمَال غَرْب mean?", "north-west", ["south-east", "north-east", "south-west"], "شَمَال + غَرْب."),
        M("What does تَقَع تُونِس بَيْن الْجَزَائِر وَلِيبِيَا mean?", "Tunisia lies between Algeria and Libya", ["Tunisia is north of Algeria", "Algeria and Libya border Tunisia’s sea", "Tunisia is in Libya"], "بَيْن = between."),
        M("What does the و of وَقَعَ do in يَقَع?", "it disappears", ["it doubles", "it becomes ا", "it stays"], "Assimilated verb."),
        M("What does تَقَع الْكُوَيْت عَلَى الْخَلِيج الْعَرَبِيّ mean?", "Kuwait lies on the Arabian Gulf", ["Kuwait is far from the Gulf", "The Gulf lies in Kuwait", "Kuwait is a gulf"], "عَلَى = on."),
        F("___ مِصْر فِي شَمَال شَرْق أَفْرِيقِيَا.", "تَقَع", ["يَقَع", "وَقَعَ", "أَقَع"], "Egypt is treated as feminine.", tr="Egypt lies in the north-east of Africa.", lemma="وقع:pres:hiya"),
        F("تَقَع تُونِس ___ الْجَزَائِر وَلِيبِيَا.", "بَيْن", ["فِي", "عَلَى", "مِنْ"], "Between two places.", tr="Tunisia lies between Algeria and Libya."),
        F("يَقَع الْيَمَن فِي ___ شِبْه الْجَزِيرَة.", "جَنُوب", ["شَمَال", "شَرْق", "مَعَ"], "Yemen is at the southern end.", tr="Yemen lies in the south of the peninsula."),
    ],
    verify=(vv("وقع", "pres", huwa="يَقَع", hiya="تَقَع", ana="أَقَع") + vv("وقع", "past", huwa="وَقَعَ")
            + vw("شَمَال", "جَنُوب", "شَرْق", "غَرْب", "مِصْر", "أَفْرِيقِيَا", "الْمَغْرِب", "السُّعُودِيَّة", "شِبْه", "الْجَزِيرَة", "الْعَرَبِيَّة", "الْكُوَيْت", "الْخَلِيج", "الْعَرَبِيّ", "تُونِس", "بَيْن", "الْجَزَائِر", "لِيبِيَا", "الْيَمَن", "أَقَع", "وَقَعَ")),
)

# ---------------------------------------------------------------------------- 291
L291 = lesson(
    "Seas, rivers, deserts and mountains",
    "الْبَحْر الْأَحْمَر · نَهْر النِّيل · الصَّحْرَاء الْكُبْرَى",
    requires=["بحر", "نهر", "صحراء", "جبل", "ساحل", "خليج", "محيط", "جزيرة", "قناة", "مر", "وصل"],
    cards=[
        card("Landforms and waters",
             "Learn the type of feature first, then its name. A sea is بَحْر, an ocean مُحِيط, a gulf خَلِيج, a river نَهْر, a desert صَحْرَاء, a mountain جَبَل (plural جِبَال), a coast سَاحِل, an island جَزِيرَة and a canal قَنَاة.",
             tables=[table(["Feature", "Example"],
                           [["بَحْر", "الْبَحْر الْأَحْمَر"], ["بَحْر", "الْبَحْر الْمُتَوَسِّط"], ["مُحِيط", "الْمُحِيط الْأَطْلَسِيّ"], ["نَهْر", "نَهْر النِّيل"], ["صَحْرَاء", "الصَّحْرَاء الْكُبْرَى"],
                            ["جِبَال", "جِبَال الْأَطْلَس"], ["قَنَاة", "قَنَاة السُّوَيْس"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Facts about the region",
             "Two familiar verbs appear in descriptions: تَصِل (it connects, from وَصَلَ) and يَمُرّ (it passes, from مَرَّ). All of these are simple, widely known facts.",
             examples=[
                 ex("تَصِل قَنَاة السُّوَيْس الْبَحْر الْمُتَوَسِّط بِالْبَحْر الْأَحْمَر.", "The Suez Canal connects the Mediterranean Sea with the Red Sea.", "تَصِل"),
                 ex("يَمُرّ نَهْر النِّيل فِي مِصْر.", "The Nile flows through Egypt.", "يَمُرّ"),
                 ex("فِي الْعِرَاق نَهْرَان كَبِيرَان: دِجْلَة وَالْفُرَات.", "In Iraq there are two big rivers: the Tigris and the Euphrates.", "نَهْرَان"),
                 ex("الصَّحْرَاء الْكُبْرَى فِي شَمَال أَفْرِيقِيَا.", "The Sahara is in the north of Africa.", "الصَّحْرَاء"),
                 ex("الْبَحْر الَّذِي بَيْن أَفْرِيقِيَا وَآسِيَا هُوَ الْبَحْر الْأَحْمَر.", "The sea that lies between Africa and Asia is the Red Sea.", "الَّذِي"),
                 ex("تُوجَد جِبَال الْأَطْلَس فِي الْمَغْرِب.", "The Atlas Mountains are found in Morocco.", "تُوجَد"),
             ]),
    ],
    exercises=[
        M("Which word means “river”?", "نَهْر", ["بَحْر", "جَبَل", "سَاحِل"], "نَهْر = river."),
        M("Which word means “desert”?", "صَحْرَاء", ["جَزِيرَة", "خَلِيج", "قَنَاة"], "صَحْرَاء = desert."),
        M("What does قَنَاة السُّوَيْس do?", "it connects two seas", ["it separates two cities", "it crosses a desert only", "it is a mountain"], "تَصِل … بِـ = connects … with."),
        M("What does يَمُرّ نَهْر النِّيل فِي مِصْر mean?", "The Nile flows through Egypt", ["The Nile begins in Egypt", "Egypt has no river", "The Nile is in the sea"], "يَمُرّ = passes."),
        M("What does تُوجَد جِبَال الْأَطْلَس فِي الْمَغْرِب mean?", "The Atlas Mountains are found in Morocco", ["Morocco has one mountain", "The Atlas is a sea", "The mountains are far from Morocco"], "تُوجَد = is found (f.)."),
        M("Which pronoun goes with الْبَحْر (the sea)?", "الَّذِي", ["الَّتِي", "الَّذِين", "اللَّذَان"], "الْبَحْر is masculine singular."),
        F("تَصِل قَنَاة السُّوَيْس الْبَحْر الْمُتَوَسِّط بِالْبَحْر ___.", "الْأَحْمَر", ["الْمَيِّت", "الْأَسْوَد", "الْأَخْضَر"], "The canal joins the Mediterranean to the Red Sea.", tr="The Suez Canal connects the Mediterranean Sea with the Red Sea."),
        F("___ نَهْر النِّيل فِي مِصْر.", "يَمُرّ", ["تَمُرّ", "مَرَّ", "نَمُرّ"], "نَهْر is masculine.", tr="The Nile flows through Egypt.", lemma="مرر:pres:huwa"),
        F("الصَّحْرَاء الْكُبْرَى فِي ___ أَفْرِيقِيَا.", "شَمَال", ["جَنُوب", "الْبَحْر", "النَّهْر"], "The Sahara lies in the north.", tr="The Sahara is in the north of Africa."),
    ],
    verify=(vv("وصل", "pres", hiya="تَصِل") + vv("مرر", "pres", huwa="يَمُرّ", hiya="تَمُرّ", ana="أَمُرّ") + vv("مرر", "past", huwa="مَرَّ")
            + vd("نَهْر", "نَهْرَان", "نَهْرَيْن") + vpb("جَبَل", "جِبَال")
            + vw("الْبَحْر", "الْأَحْمَر", "الْمُتَوَسِّط", "الْمُحِيط", "الْأَطْلَسِيّ", "نَهْر", "النِّيل", "الصَّحْرَاء", "الْكُبْرَى", "جِبَال", "الْأَطْلَس", "قَنَاة", "السُّوَيْس", "الْعِرَاق", "نَهْرَان", "كَبِيرَان", "دِجْلَة", "الْفُرَات", "آسِيَا", "تُوجَد", "بِالْبَحْر", "سَاحِل", "جَزِيرَة", "خَلِيج", "مُحِيط", "تَمُرّ", "نَمُرّ", "مَرَّ")),
)

# ---------------------------------------------------------------------------- 292
L292 = lesson(
    "A short country profile: Morocco",
    "الْمَغْرِب: الْمَوْقِع وَالْعَاصِمَة وَاللُّغَات",
    requires=["دولة", "عاصمة", "لغة", "ساحل", "جبل", "عملة", "غرب", "وجد", "وقع"],
    cards=[
        card("What a profile tells you",
             "A country profile answers a few questions: Where is it? What is its capital? Which languages are official? What are its main features? "
             "Morocco is a good model, because it uses most of the words of the chapter. The facts below are standard reference facts.",
             tables=[table(["Question", "Answer"],
                           [["location", "شَمَال غَرْب أَفْرِيقِيَا"], ["capital", "الرِّبَاط"], ["official languages", "الْعَرَبِيَّة وَالْأَمَازِيغِيَّة"], ["currency", "الدِّرْهَم"],
                            ["mountains", "جِبَال الْأَطْلَس"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("The profile in sentences",
             "Notice تَقَع (it lies), تُوجَد (is found) and الَّتِي after a feminine noun.",
             examples=[
                 ex("الْمَغْرِب دَوْلَة عَرَبِيَّة تَقَع فِي شَمَال غَرْب أَفْرِيقِيَا.", "Morocco is an Arab country that lies in the north-west of Africa.", "تَقَع"),
                 ex("لَهَا سَاحِل عَلَى الْمُحِيط الْأَطْلَسِيّ وَسَاحِل عَلَى الْبَحْر الْمُتَوَسِّط.", "It has a coast on the Atlantic Ocean and a coast on the Mediterranean Sea.", "سَاحِل"),
                 ex("عَاصِمَة الْمَغْرِب هِيَ الرِّبَاط.", "The capital of Morocco is Rabat.", "الرِّبَاط"),
                 ex("اللُّغَتَان الرَّسْمِيَّتَان هُمَا الْعَرَبِيَّة وَالْأَمَازِيغِيَّة.", "The two official languages are Arabic and Amazigh.", "اللُّغَتَان"),
                 ex("تُوجَد جِبَال الْأَطْلَس فِي وَسَط الْبِلَاد.", "The Atlas Mountains are found in the middle of the country.", "تُوجَد"),
                 ex("الْعُمْلَة الَّتِي تُسْتَخْدَم هِيَ الدِّرْهَم.", "The currency that is used is the dirham.", "الَّتِي"),
             ]),
    ],
    exercises=[
        M("Where does Morocco lie?", "in the north-west of Africa", ["in the north-east of Africa", "in the south of Asia", "in the middle of Europe"], "شَمَال غَرْب أَفْرِيقِيَا."),
        M("What is the capital of Morocco?", "Rabat", ["Cairo", "Tunis", "Amman"], "الرِّبَاط."),
        M("Which two languages are official in Morocco?", "Arabic and Amazigh", ["Arabic and Persian", "Arabic and Kurdish", "Arabic and Russian"], "الْعَرَبِيَّة وَالْأَمَازِيغِيَّة."),
        M("Which mountains are found in the middle of Morocco?", "the Atlas Mountains", ["the Sahara Mountains", "the Nile Mountains", "the Gulf Mountains"], "جِبَال الْأَطْلَس."),
        M("Which two bodies of water meet Morocco’s coasts?", "the Atlantic Ocean and the Mediterranean Sea", ["the Red Sea and the Gulf", "the Gulf and the Black Sea", "the Nile and the Suez Canal"], "الْمُحِيط الْأَطْلَسِيّ وَالْبَحْر الْمُتَوَسِّط."),
        M("Why is it الْعُمْلَة الَّتِي تُسْتَخْدَم؟", "عُمْلَة is feminine singular", ["it is plural", "it is a person", "it is dual"], "الَّتِي for a feminine singular noun."),
        F("الْمَغْرِب دَوْلَة عَرَبِيَّة ___ فِي شَمَال غَرْب أَفْرِيقِيَا.", "تَقَع", ["يَقَع", "وَقَعَ", "نَقَع"], "Feminine (دَوْلَة).", tr="Morocco is an Arab country that lies in the north-west of Africa.", lemma="وقع:pres:hiya"),
        F("___ جِبَال الْأَطْلَس فِي وَسَط الْبِلَاد.", "تُوجَد", ["يُوجَد", "تَجِد", "وَجَدَ"], "A plural of things: feminine singular, passive.", tr="The Atlas Mountains are found in the middle of the country.", lemma="وجد:ppres:hiya"),
        F("عَاصِمَة الْمَغْرِب ___ الرِّبَاط.", "هِيَ", ["هُوَ", "هُمْ", "أَنَا"], "عَاصِمَة is feminine.", tr="The capital of Morocco is Rabat."),
    ],
    verify=(vv("وقع", "pres", hiya="تَقَع") + vv("وجد", "ppres", hiya="تُوجَد")
            + vw("الْمَغْرِب", "دَوْلَة", "عَرَبِيَّة", "سَاحِل", "الْمُحِيط", "الْأَطْلَسِيّ", "الْبَحْر", "الْمُتَوَسِّط", "عَاصِمَة", "الرِّبَاط", "اللُّغَتَان", "الرَّسْمِيَّتَان", "الْأَمَازِيغِيَّة", "وَسَط", "الْبِلَاد", "الْعُمْلَة", "الدِّرْهَم", "تُسْتَخْدَم", "الْمَوْقِع", "نَقَع", "أَفْرِيقِيَا", "الْمَيِّت", "الْأَسْوَد", "الْأَخْضَر")),
)

# ---------------------------------------------------------------------------- 293
L293 = lesson(
    "Review: pronouns, passive and Measure VII",
    "الْكِتَاب الَّذِي فُتِحَ · الْبَاب الَّذِي اِنْفَتَحَ",
    requires=["الذي", "كتاب", "فتح", "كسر", "بنى", "مدينة", "قديم", "باب", "مسجد"],
    cards=[
        card("What to remember",
             "(1) A definite noun takes a relative pronoun that matches it: الَّذِي, الَّتِي, اللَّذَان, اللَّتَان, الَّذِين, اللَّاتِي; plural things take الَّتِي. "
             "(2) If the noun is the object of a verb or preposition inside the clause (not its subject), add a returning pronoun. "
             "(3) The passive past has ḍamma and kasra (كُتِبَ); the passive present has ḍamma and fatḥa (يُكْتَب). "
             "(4) Measure VII is اِنْفَعَلَ, with no doer, and its verbal noun is اِنْفِعَال.",
             tables=[table(["English", "Arabic"],
                           [["The book that was opened", "الْكِتَاب الَّذِي فُتِحَ"], ["The door that opened", "الْبَاب الَّذِي اِنْفَتَحَ"], ["The mosque that was built", "الْمَسْجِد الَّذِي بُنِيَ"],
                            ["The city that I visited", "الْمَدِينَة الَّتِي زُرْتُهَا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Mixed sentences",
             "Each of these combines two ideas from the chapter. They are invented.",
             examples=[
                 ex("الْمَسْجِد الَّذِي بُنِيَ قَبْل سَنَوَات قَدِيم.", "The mosque that was built years ago is old.", "بُنِيَ"),
                 ex("الْكُتُب الَّتِي كُتِبَتْ بِالْعَرَبِيَّة مُهِمَّة.", "The books that were written in Arabic are important.", "الَّتِي كُتِبَتْ"),
                 ex("الزُّجَاج الَّذِي اِنْكَسَرَ كَانَ جَدِيدًا.", "The glass that broke was new.", "اِنْكَسَرَ"),
                 ex("الْمَدِينَة الَّتِي زُرْتُهَا تَقَع عَلَى السَّاحِل.", "The city I visited lies on the coast.", "زُرْتُهَا"),
                 ex("الْمُهَنْدِسَان اللَّذَان بَنَيَا الْجِسْر مِنْ لُبْنَان.", "The two engineers who built the bridge are from Lebanon.", "اللَّذَان"),
                 ex("بَعْد اِنْقِطَاع الطَّرِيق تَأَخَّرَتِ الْحَافِلَات.", "After the road was cut off, the buses were late.", "اِنْقِطَاع"),
             ]),
    ],
    exercises=[
        M("Which pronoun fits الْمَسْجِد (the mosque)?", "الَّذِي", ["الَّتِي", "الَّذِين", "اللَّاتِي"], "مَسْجِد is masculine."),
        M("Which pronoun fits الْكُتُب (the books)?", "الَّتِي", ["الَّذِين", "الَّذِي", "اللَّذَان"], "Plural things."),
        M("Which fits الْمُهَنْدِسَان (the two engineers, subject)?", "اللَّذَان", ["الَّذِين", "اللَّتَان", "اللَّذَيْن"], "Masculine dual."),
        M("What does الزُّجَاج الَّذِي اِنْكَسَرَ كَانَ جَدِيدًا mean?", "The glass that broke was new", ["He broke the new glass", "The new glass was broken by him", "The glass will break"], "Measure VII = no doer."),
        M("Which verb is passive?", "بُنِيَ", ["بَنَى", "يَبْنِي", "اِبْنِ"], "ḍamma + kasra."),
        M("What does the returning pronoun ـهَا do in الْمَدِينَة الَّتِي زُرْتُهَا؟", "it points back to the city", ["it shows the speaker", "it shows the tense", "it makes the verb passive"], "Feminine singular, pointing back."),
        F("الْكُتُب ___ كُتِبَتْ بِالْعَرَبِيَّة مُهِمَّة.", "الَّتِي", ["الَّذِين", "الَّذِي", "اللَّاتِي"], "Plural things.", tr="The books that were written in Arabic are important."),
        F("الْمَدِينَة الَّتِي ___ تَقَع عَلَى السَّاحِل.", "زُرْتُهَا", ["زُرْتُهُ", "زُرْتُهُمْ", "زُرْنَا"], "Feminine singular returning pronoun.", tr="The city I visited lies on the coast."),
        F("بَعْد ___ الطَّرِيق تَأَخَّرَتِ الْحَافِلَات.", "اِنْقِطَاع", ["اِنْقَطَعَ", "قَطَعَ", "يَنْقَطِع"], "A verbal noun after بَعْد.", tr="After the road was cut off, the buses were late."),
    ],
    verify=(vv("زور", "past", ana="زُرْتُ") + vv("فتح", "ppast", huwa="فُتِحَ") + vv("بني", "ppast", huwa="بُنِيَ") + vv("فتح#7", "past", huwa="اِنْفَتَحَ") + vv("كسر#7", "past", huwa="اِنْكَسَرَ")
            + vw("الْمَسْجِد", "بُنِيَ", "سَنَوَات", "كُتِبَتْ", "بِالْعَرَبِيَّة", "مُهِمَّة", "الزُّجَاج", "جَدِيدًا", "زُرْتُهَا", "زُرْتُهُ", "زُرْتُهُمْ", "زُرْنَا", "الْمُهَنْدِسَان", "بَنَيَا", "الْجِسْر", "لُبْنَان", "اِنْقِطَاع", "الْحَافِلَات", "تَأَخَّرَتِ", "يَبْنِي", "اِبْنِ", "قَطَعَ", "يَنْقَطِع", "اِنْقَطَعَ", "السَّاحِل")),
)


UNIT = unit("الْجُغْرَافِيَا وَالتَّارِيخ: relative pronouns, the passive and Measure VII", [L277, L278, L279, L280, L281, L282, L283, L284, L285, L286, L287, L288, L289, L290, L291, L292, L293])
