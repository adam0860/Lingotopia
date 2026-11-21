"""Unit 4: places, position words, plurals, adjective agreement, family
(textbook Chapter 3; all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 49
L49 = lesson(
    "Places in the city",
    "شَارِع · مَسْجِد · مَكْتَبَة · حَدِيقَة",
    requires=["شارع", "مسجد", "مكتبة", "حديقة", "متحف", "سوق", "بنك", "مستشفى", "محطة"],
    cards=[
        card("Public places",
             "These are the words you need to find your way around a city. Nouns that end in ة are feminine; "
             "the others here are masculine.",
             tables=[table(["English", "Arabic"],
                           [["street", "شَارِع"], ["mosque", "مَسْجِد"], ["church", "كَنِيسَة"], ["hospital", "مُسْتَشْفَى"],
                            ["station", "مَحَطَّة"], ["library", "مَكْتَبَة"], ["park, garden", "حَدِيقَة"],
                            ["museum", "مَتْحَف"]],
                           say=[1], tlit=[1])]),
        card("More places",
             "Some of these you saw in the last unit. Together they cover most of a city centre.",
             tables=[table(["English", "Arabic"],
                           [["market", "سُوق"], ["bank", "بَنْك"], ["café", "مَقْهَى"], ["post office", "مَكْتَب الْبَرِيد"],
                            ["square", "مَيْدَان"], ["bridge", "جِسْر"], ["building", "مَبْنَى"], ["hotel", "فُنْدُق"]],
                           say=[1], tlit=[1])],
             examples=[
                 ex("أَيْنَ الْمُسْتَشْفَى؟", "Where is the hospital?"),
                 ex("الْمُسْتَشْفَى قَرِيب مِنَ الْمَحَطَّة.", "The hospital is near the station."),
                 ex("فِي الْمَدِينَة مَتْحَف وَمَكْتَبَة وَحَدِيقَة.", "In the city there is a museum, a library and a park."),
                 ex("مَكْتَب الْبَرِيد قَرِيب مِنَ الْبَنْك.", "The post office is near the bank."),
             ]),
    ],
    exercises=[
        M("Which word means “street”?", "شَارِع", ["جِسْر", "مَيْدَان", "سُوق"], "شَارِع = street."),
        M("Which word means “hospital”?", "مُسْتَشْفَى", ["مَكْتَبَة", "مَحَطَّة", "مَسْجِد"], "مُسْتَشْفَى = hospital."),
        M("Which word means “library”?", "مَكْتَبَة", ["مَتْحَف", "حَدِيقَة", "بَنْك"], "مَكْتَبَة = library (a place for books)."),
        M("Which word means “park”?", "حَدِيقَة", ["مَقْهَى", "مَحَطَّة", "مَبْنَى"], "حَدِيقَة = garden, park."),
        M("Which word means “museum”?", "مَتْحَف", ["مَسْجِد", "مُسْتَشْفَى", "كَنِيسَة"], "مَتْحَف = museum."),
        M("Which word means “market”?", "سُوق", ["بَنْك", "جِسْر", "مَقْهَى"], "سُوق = market."),
        M("Which means “post office”?", "مَكْتَب الْبَرِيد", ["مَكْتَب الْبَنْك", "مَحَطَّة الْبَرِيد", "الْبَرِيد مَكْتَب"], "مَكْتَب الْبَرِيد = office of the mail."),
        M("Which means “The hospital is near the station”?", "الْمُسْتَشْفَى قَرِيب مِنَ الْمَحَطَّة", ["الْمُسْتَشْفَى بَعِيد عَنِ الْمَحَطَّة", "الْمُسْتَشْفَى قَرِيب مِنَ الْمَطَار", "الْمُسْتَشْفَى فِي الْمَحَطَّة"], "قَرِيب مِنَ = near."),
        F("أَيْنَ ___؟", "الْمُسْتَشْفَى", ["مَتَى", "كَيْفَ", "قَرِيب"], "A question about a place.", tr="Where is the hospital?"),
        F("فِي الْمَدِينَة ___ وَمَكْتَبَة.", "مَتْحَف", ["بَحْر", "جَبَل", "نَهْر"], "Buildings of a city.", tr="In the city there is a museum and a library."),
    ],
    verify=vw("شَارِع", "مَسْجِد", "كَنِيسَة", "مُسْتَشْفَى", "مَحَطَّة", "مَكْتَبَة", "حَدِيقَة", "مَتْحَف", "سُوق", "بَنْك",
              "مَقْهَى", "الْبَرِيد", "مَيْدَان", "جِسْر", "مَبْنَى", "فُنْدُق"),
)

# ---------------------------------------------------------------------------- 50
L50 = lesson(
    "In front of, behind, between",
    "أَمَام · خَلْف · فَوْق · تَحْت · بَيْنَ",
    requires=["أمام", "وراء", "فوق", "تحت", "بين", "عند", "شارع"],
    cards=[
        card("Position words",
             "These words say where something is in relation to something else. The first word never takes ال, and the "
             "noun after it completes the phrase, just as in عَاصِمَة مِصْر.",
             tables=[table(["English", "Arabic", "Example"],
                           [["in front of", "أَمَام", "الْمَدْرَسَة أَمَام الْمَسْجِد"],
                            ["behind", "خَلْف", "الْحَدِيقَة خَلْف الْمَتْحَف"],
                            ["above, on top of", "فَوْق", "الْكِتَاب فَوْق الْمَكْتَب"],
                            ["under", "تَحْت", "الْقَلَم تَحْت الْكِتَاب"],
                            ["between", "بَيْنَ", "الْبَنْك بَيْنَ الْمَكْتَبَة وَالْمَطْعَم"],
                            ["next to", "بِجَانِب", "الْمَقْهَى بِجَانِب الْفُنْدُق"],
                            ["at (someone’s place)", "عِنْد", "أَنَا عِنْد صَدِيقِي"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("Asking and answering",
             "Questions about places start with أَيْنَ. The answer is a noun sentence with one of these words.",
             examples=[
                 ex("أَيْنَ الْبَنْك؟", "Where is the bank?"),
                 ex("الْبَنْك بَيْنَ الْمَكْتَبَة وَالْمَطْعَم.", "The bank is between the library and the restaurant.", "بَيْنَ"),
                 ex("هَلِ الْمَتْحَف خَلْف الْحَدِيقَة؟", "Is the museum behind the park?"),
                 ex("لَا، هُوَ أَمَام الْحَدِيقَة.", "No, it is in front of the park.", "أَمَام"),
                 ex("الْمَحَطَّة بِجَانِب السُّوق.", "The station is next to the market.", "بِجَانِب"),
             ]),
    ],
    exercises=[
        M("Which word means “in front of”?", "أَمَام", ["خَلْف", "تَحْت", "بَيْنَ"], "أَمَام = in front of."),
        M("Which word means “behind”?", "خَلْف", ["أَمَام", "فَوْق", "عِنْد"], "خَلْف = behind."),
        M("Which word means “under”?", "تَحْت", ["فَوْق", "بَيْنَ", "أَمَام"], "تَحْت = under."),
        M("Which word means “above, on top of”?", "فَوْق", ["تَحْت", "بِجَانِب", "خَلْف"], "فَوْق = above."),
        M("Which word means “between”?", "بَيْنَ", ["أَمَام", "عِنْد", "بِجَانِب"], "بَيْنَ = between."),
        M("Which means “The school is in front of the mosque”?", "الْمَدْرَسَة أَمَام الْمَسْجِد", ["الْمَدْرَسَة خَلْف الْمَسْجِد", "الْمَسْجِد أَمَام الْمَدْرَسَة", "الْمَدْرَسَة فَوْق الْمَسْجِد"], "أَمَام = in front of."),
        M("The bank is between the library and the restaurant. What is between them?", "الْبَنْك", ["الْمَكْتَبَة", "الْمَطْعَم", "الْمَسْجِد"], "الْبَنْك بَيْنَ الْمَكْتَبَة وَالْمَطْعَم."),
        F("الْقَلَم ___ الْكِتَاب.", "تَحْت", ["فَوْق", "بَيْنَ", "أَمَام"], "The pen is below the book.", tr="The pen is under the book."),
        F("الْمَقْهَى ___ الْفُنْدُق.", "بِجَانِب", ["تَحْت", "فَوْق", "عَنْ"], "Side by side.", tr="The café is next to the hotel."),
        F("أَنَا ___ صَدِيقِي.", "عِنْد", ["فَوْق", "تَحْت", "بَيْنَ"], "At a person’s place.", tr="I am at my friend’s."),
    ],
    verify=vw("أَمَام", "خَلْف", "فَوْق", "تَحْت", "بَيْنَ", "بِجَانِب", "عِنْد", "قَلَم", "صَدِيقِي"),
)

# ---------------------------------------------------------------------------- 51
L51 = lesson(
    "Plural of men and masculine nisbas: ـُون",
    "مُدَرِّسُون · مُهَنْدِسُون · مِصْرِيُّون",
    requires=["مدرس", "مهندس", "موظف", "مصري", "عربي"],
    cards=[
        card("A group of men: ـُون",
             "The regular plural for a group of men, or a mixed group, adds ـُون to the singular. It is called the "
             "sound masculine plural, and it works for many jobs and nationalities. Words ending in ـِيّ keep the "
             "doubled ي: مِصْرِيّ becomes مِصْرِيُّون.",
             tables=[table(["English", "Singular", "Plural"],
                           [["teacher", "مُدَرِّس", "مُدَرِّ{سُون}"], ["engineer", "مُهَنْدِس", "مُهَنْدِ{سُون}"],
                            ["employee", "مُوَظَّف", "مُوَظَّ{فُون}"], ["Egyptian", "مِصْرِيّ", "مِصْرِ{يُّون}"],
                            ["Syrian", "سُورِيّ", "سُورِ{يُّون}"], ["Muslim", "مُسْلِم", "مُسْلِ{مُون}"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("A second ending: ـِين",
             "After a preposition, or when the plural is the object of a verb, ـُون changes to ـِين. In a plain "
             "sentence where the plural is the subject, it stays ـُون. After لَيْسَ, the predicate takes ـِين too: "
             "لَيْسُوا مُدَرِّسِين.",
             tables=[table(["Arabic", "English"],
                           [["هُم مُدَرِّ{سُون}", "They are teachers."], ["الْمُهَنْدِ{سُون} فِي الْمَكْتَب", "The engineers are in the office."],
                            ["مَعَ الْمُدَرِّ{سِين}", "with the teachers"], ["أَتَكَلَّم مَعَ الْمُهَنْدِ{سِين}", "I talk with the engineers."]],
                           say=[0], tlit=[0], gloss=False)]),
    ],
    exercises=[
        M("Which is the plural of مُدَرِّس (teacher)?", "مُدَرِّسُون", ["مُدَرِّسَات", "مُدَرِّسَة", "مُدَرِّسَان"], "Add ـُون."),
        M("Which is the plural of مُهَنْدِس (engineer)?", "مُهَنْدِسُون", ["مُهَنْدِسَات", "مُهَنْدِسَة", "مُهَنْدِسِيّ"], "Add ـُون."),
        M("Which is the plural of مِصْرِيّ?", "مِصْرِيُّون", ["مِصْرِيَّات", "مِصْرِيُّ", "مِصْرِيَّة"], "Keep the doubled ي and add ـُون."),
        M("Which means “They (men) are employees”?", "هُم مُوَظَّفُون", ["هُنَّ مُوَظَّفَات", "هُوَ مُوَظَّف", "هُم مُوَظَّفِين"], "Subject plural: ـُون."),
        M("Which masculine plural ending is used after a preposition?", "ـِين", ["ـُون", "ـَات", "ـَان"], "مَعَ الْمُدَرِّسِين."),
        M("Which means “with the (male) teachers”?", "مَعَ الْمُدَرِّسِين", ["مَعَ الْمُدَرِّسُون", "مَعَ الْمُدَرِّسَات", "مَعَ مُدَرِّسُون"], "A preposition is followed by ـِين."),
        M("Which means “The (male) engineers are in the office”?", "الْمُهَنْدِسُون فِي الْمَكْتَب", ["الْمُهَنْدِسِين فِي الْمَكْتَب", "الْمُهَنْدِسَات فِي الْمَكْتَب", "الْمُهَنْدِس فِي الْمَكْتَب"], "The plural is the subject: ـُون."),
        F("هُم ___.", "مُهَنْدِسُون", ["مُهَنْدِس", "مُهَنْدِسَات", "مُهَنْدِسَة"], "A group of men.", tr="They are engineers."),
        F("أَتَكَلَّم مَعَ ___.", "الْمُدَرِّسِين", ["الْمُدَرِّسُون", "الْمُدَرِّس", "الْمُدَرِّسَات"], "After مَعَ the plural ends in ـِين.", tr="I talk with the (male) teachers."),
    ],
    verify=(vps("مُدَرِّس", "مُدَرِّسُون") + vps("مُهَنْدِس", "مُهَنْدِسُون") + vps("مُوَظَّف", "مُوَظَّفُون")
            + vps("مِصْرِيّ", "مِصْرِيُّون") + vps("سُورِيّ", "سُورِيُّون") + vps("مُسْلِم", "مُسْلِمُون")
            + vps("مُدَرِّس", "مُدَرِّسِين", "obl") + vps("مُهَنْدِس", "مُهَنْدِسِين", "obl")),
)

# ---------------------------------------------------------------------------- 52
L52 = lesson(
    "Plural of women and many things: ـَات",
    "طَالِبَات · مُدَرِّسَات · سَيَّارَات",
    requires=["طالب", "مدرس", "جامعة", "سيارة", "ساعة"],
    cards=[
        card("Drop ة, add ـَات",
             "The sound feminine plural is made by removing the ة and adding ـَات. It is the usual plural of "
             "feminine jobs and nationalities, and it also serves many feminine nouns that name things.",
             tables=[table(["English", "Singular", "Plural"],
                           [["student (f)", "طَالِبَة", "طَالِبَ{ات}"], ["teacher (f)", "مُدَرِّسَة", "مُدَرِّسَ{ات}"],
                            ["engineer (f)", "مُهَنْدِسَة", "مُهَنْدِسَ{ات}"], ["employee (f)", "مُوَظَّفَة", "مُوَظَّفَ{ات}"],
                            ["university", "جَامِعَة", "جَامِعَ{ات}"], ["car", "سَيَّارَة", "سَيَّارَ{ات}"],
                            ["hour", "سَاعَة", "سَاعَ{ات}"], ["library", "مَكْتَبَة", "مَكْتَبَ{ات}"],
                            ["company", "شَرِكَة", "شَرِكَ{ات}"], ["word", "كَلِمَة", "كَلِمَ{ات}"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("In sentences",
             "Not every feminine noun uses this plural: مَدْرَسَة (school) has a different one, which you will "
             "meet in the next lesson. Where this plural is available, it is the same in every position in the sentence.",
             examples=[
                 ex("هُنَّ طَالِبَات فِي الْجَامِعَة.", "They (women) are students at the university.", "طَالِبَات"),
                 ex("الْمُهَنْدِسَات فِي الْمَكْتَب.", "The (women) engineers are in the office.", "الْمُهَنْدِسَات"),
                 ex("فِي الْمَدِينَة جَامِعَات كَثِيرَة.", "There are many universities in the city.", "جَامِعَات"),
                 ex("أَدْرُس سَاعَات كَثِيرَة.", "I study for many hours.", "سَاعَات"),
             ]),
    ],
    exercises=[
        M("Which is the plural of طَالِبَة?", "طَالِبَات", ["طَالِبُون", "طُلَّاب", "طَالِبَان"], "Drop ة, add ـَات."),
        M("Which is the plural of مُدَرِّسَة?", "مُدَرِّسَات", ["مُدَرِّسُون", "مُدَرِّسَة", "مُدَرِّسَان"], "Drop ة, add ـَات."),
        M("Which is the plural of سَيَّارَة (car)?", "سَيَّارَات", ["سَيَّارُون", "سَيَّارَة", "سَيَّارِين"], "Drop ة, add ـَات."),
        M("Which is the plural of جَامِعَة?", "جَامِعَات", ["جَامِعُون", "جَامِعَة", "جَامِعَان"], "Drop ة, add ـَات."),
        M("Which means “They (women) are engineers”?", "هُنَّ مُهَنْدِسَات", ["هُم مُهَنْدِسُون", "هُنَّ مُهَنْدِسَة", "هِيَ مُهَنْدِسَات"], "هُنَّ is the feminine plural “they”."),
        M("Which means “many hours”?", "سَاعَات كَثِيرَة", ["سَاعَة كَثِيرَة", "سَاعُون كَثِيرَة", "سَاعَتَان"], "سَاعَة → سَاعَات."),
        M("What is removed from a feminine noun before ـَات is added?", "The ة", ["The first letter", "The ال", "Nothing"], "طَالِبَة → طَالِبَات."),
        F("هُنَّ ___ فِي الْجَامِعَة.", "طَالِبَات", ["طَالِبَة", "طَالِبُون", "طُلَّاب"], "A group of women.", tr="They (women) are students at the university."),
        F("فِي الْمَدِينَة ___ كَثِيرَة.", "جَامِعَات", ["جَامِعَة", "جَامِعُون", "مَدِينَة"], "More than one university.", tr="There are many universities in the city."),
    ],
    verify=(vps("طَالِبَة", "طَالِبَات") + vps("مُدَرِّسَة", "مُدَرِّسَات") + vps("مُهَنْدِسَة", "مُهَنْدِسَات")
            + vps("مُوَظَّفَة", "مُوَظَّفَات") + vps("جَامِعَة", "جَامِعَات") + vps("سَيَّارَة", "سَيَّارَات")
            + vps("سَاعَة", "سَاعَات") + vps("مَكْتَبَة", "مَكْتَبَات") + vps("شَرِكَة", "شَرِكَات") + vps("كَلِمَة", "كَلِمَات")),
)

# ---------------------------------------------------------------------------- 53
L53 = lesson(
    "Broken plurals",
    "كِتَاب ← كُتُب · بَيْت ← بُيُوت",
    requires=["كتاب", "بيت", "مدينة", "شارع", "درس", "سوق", "مسجد"],
    cards=[
        card("Plurals made by rearranging the word",
             "Most other nouns form the plural by changing the vowels and sometimes adding letters inside the word, as "
             "in English man and men. These are called broken plurals. There are patterns, but no reliable rule, so "
             "learn each plural together with its singular.",
             tables=[table(["English", "Singular", "Plural"],
                           [["house", "بَيْت", "بُيُوت"], ["lesson", "دَرْس", "دُرُوس"], ["pen", "قَلَم", "أَقْلَام"],
                            ["market", "سُوق", "أَسْوَاق"], ["river", "نَهْر", "أَنْهَار"], ["child, boy", "وَلَد", "أَوْلَاد"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("More common plurals",
             "Say each pair aloud until the plural feels natural.",
             tables=[table(["English", "Singular", "Plural"],
                           [["book", "كِتَاب", "كُتُب"], ["city", "مَدِينَة", "مُدُن"], ["mosque", "مَسْجِد", "مَسَاجِد"],
                            ["school", "مَدْرَسَة", "مَدَارِس"], ["street", "شَارِع", "شَوَارِع"], ["country", "بَلَد", "بُلْدَان"],
                            ["mountain", "جَبَل", "جِبَال"], ["sea", "بَحْر", "بِحَار"], ["man", "رَجُل", "رِجَال"],
                            ["student", "طَالِب", "طُلَّاب"], ["garden", "حَدِيقَة", "حَدَائِق"], ["restaurant", "مَطْعَم", "مَطَاعِم"]],
                           say=[1, 2], tlit=[2], gloss=False)],
             examples=[
                 ex("فِي الْمَدِينَة مَسَاجِد وَمَدَارِس وَشَوَارِع كَثِيرَة.", "In the city there are many mosques, schools and streets."),
                 ex("هَذِهِ كُتُب.", "These are books."),
                 ex("الطُّلَّاب فِي الْمَكْتَبَة.", "The students are in the library."),
             ]),
    ],
    exercises=[
        M("Which is the plural of كِتَاب (book)?", "كُتُب", ["كِتَابَات", "كُتُوب", "كِتَابُون"], "كِتَاب → كُتُب."),
        M("Which is the plural of بَيْت (house)?", "بُيُوت", ["بَيْتَات", "بُيُت", "بَيْتُون"], "بَيْت → بُيُوت."),
        M("Which is the plural of مَدِينَة (city)?", "مُدُن", ["مَدِينَات", "مَدَانِين", "مَدِينُون"], "مَدِينَة → مُدُن."),
        M("Which is the plural of مَدْرَسَة (school)?", "مَدَارِس", ["مَدْرَسَات", "مَدَارِسَات", "مُدَرِّسُون"], "مَدْرَسَة → مَدَارِس."),
        M("Which is the plural of شَارِع (street)?", "شَوَارِع", ["شَارِعَات", "شَارِعُون", "شُرُوع"], "شَارِع → شَوَارِع."),
        M("Which is the plural of رَجُل (man)?", "رِجَال", ["رَجُلُون", "رَجُلَات", "رُجُول"], "رَجُل → رِجَال."),
        M("Which is the plural of طَالِب?", "طُلَّاب", ["طَالِبَات", "طُلُب", "طُلَّابَات"], "طَالِب → طُلَّاب (the broken plural; women are طَالِبَات)."),
        M("How should you learn a broken plural?", "Together with its singular", ["By adding ـُون", "By removing ة", "From the gender"], "There is no single rule."),
        F("هَذِهِ ___.", "كُتُب", ["كِتَاب", "كُتُبَات", "كِتَابُون"], "Several books.", tr="These are books."),
        F("الطُّلَّاب فِي ___.", "الْمَكْتَبَة", ["الْمَكْتَبَات", "كُتُب", "الْبُيُوت"], "A place, singular.", tr="The students are in the library."),
    ],
    verify=(vpb("بَيْت", "بُيُوت") + vpb("دَرْس", "دُرُوس") + vpb("قَلَم", "أَقْلَام") + vpb("سُوق", "أَسْوَاق")
            + vpb("نَهْر", "أَنْهَار") + vpb("وَلَد", "أَوْلَاد") + vpb("كِتَاب", "كُتُب") + vpb("مَدِينَة", "مُدُن")
            + vpb("مَسْجِد", "مَسَاجِد") + vpb("مَدْرَسَة", "مَدَارِس") + vpb("شَارِع", "شَوَارِع") + vpb("بَلَد", "بُلْدَان")
            + vpb("جَبَل", "جِبَال") + vpb("بَحْر", "بِحَار") + vpb("رَجُل", "رِجَال") + vpb("طَالِب", "طُلَّاب")
            + vpb("حَدِيقَة", "حَدَائِق") + vpb("مَطْعَم", "مَطَاعِم")),
)

# ---------------------------------------------------------------------------- 54
L54 = lesson(
    "Adjectives agree: masculine and feminine",
    "بَيْت كَبِير · مَدْرَسَة كَبِيرَة",
    requires=["كبير", "صغير", "جديد", "قديم", "جميل"],
    cards=[
        card("The adjective follows the noun",
             "In Arabic the adjective comes after its noun and matches it in gender. For a feminine noun, add ة to "
             "the masculine adjective. Nouns that end in ة are nearly always feminine.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["big", "كَبِير", "كَبِيرَة"], ["small", "صَغِير", "صَغِيرَة"], ["new", "جَدِيد", "جَدِيدَة"],
                            ["old", "قَدِيم", "قَدِيمَة"], ["beautiful", "جَمِيل", "جَمِيلَة"], ["long, tall", "طَوِيل", "طَوِيلَة"],
                            ["short", "قَصِير", "قَصِيرَة"], ["good", "جَيِّد", "جَيِّدَة"], ["fast", "سَرِيع", "سَرِيعَة"],
                            ["clean", "نَظِيف", "نَظِيفَة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Noun and adjective together",
             "A few feminine nouns do not end in ة, such as شَمْس (sun). You have to learn them one by one. "
             "Compare the pairs below.",
             examples=[
                 ex("بَيْت كَبِير", "a big house"),
                 ex("مَدْرَسَة كَبِيرَة", "a big school"),
                 ex("كِتَاب جَدِيد", "a new book"),
                 ex("مَدِينَة جَمِيلَة", "a beautiful city"),
                 ex("شَارِع طَوِيل", "a long street"),
                 ex("حَدِيقَة صَغِيرَة", "a small park"),
                 ex("الشَّمْس حَارَّة.", "The sun is hot."),
             ]),
    ],
    exercises=[
        M("Which is “a big house” (بَيْت is masculine)?", "بَيْت كَبِير", ["بَيْت كَبِيرَة", "كَبِير بَيْت", "بَيْت الْكَبِير"], "Masculine noun, masculine adjective."),
        M("Which is “a big school” (مَدْرَسَة is feminine)?", "مَدْرَسَة كَبِيرَة", ["مَدْرَسَة كَبِير", "كَبِيرَة مَدْرَسَة", "مَدْرَسَة الْكَبِيرَة"], "Feminine noun, feminine adjective."),
        M("Which is “a new book”?", "كِتَاب جَدِيد", ["كِتَاب جَدِيدَة", "جَدِيد كِتَاب", "كِتَابَة جَدِيد"], "كِتَاب is masculine."),
        M("Which is “a beautiful city”?", "مَدِينَة جَمِيلَة", ["مَدِينَة جَمِيل", "جَمِيلَة مَدِينَة", "مَدِينَة جَمِيلُون"], "مَدِينَة is feminine."),
        M("Which is “a long street”?", "شَارِع طَوِيل", ["شَارِع طَوِيلَة", "طَوِيل شَارِع", "شَوَارِع طَوِيل"], "شَارِع is masculine."),
        M("Where does the adjective go?", "After the noun", ["Before the noun", "At the end of the sentence", "It can go anywhere"], "Arabic adjectives follow the noun."),
        M("What do you add to make a masculine adjective feminine?", "ة", ["ـُون", "ـَات", "ـِي"], "كَبِير → كَبِيرَة."),
        F("حَدِيقَة ___.", "صَغِيرَة", ["صَغِير", "صِغَار", "الصَّغِيرَة"], "حَدِيقَة is feminine.", tr="a small park"),
        F("كِتَاب ___.", "جَدِيد", ["جَدِيدَة", "جُدُد", "الْجَدِيد"], "كِتَاب is masculine.", tr="a new book"),
    ],
    verify=(vf("كَبِير", "كَبِيرَة") + vf("صَغِير", "صَغِيرَة") + vf("جَدِيد", "جَدِيدَة") + vf("قَدِيم", "قَدِيمَة")
            + vf("جَمِيل", "جَمِيلَة") + vf("طَوِيل", "طَوِيلَة") + vf("قَصِير", "قَصِيرَة") + vf("جَيِّد", "جَيِّدَة")
            + vf("سَرِيع", "سَرِيعَة") + vf("نَظِيف", "نَظِيفَة") + vw("حَارَّة")),
)

# ---------------------------------------------------------------------------- 55
L55 = lesson(
    "The big house or the house is big?",
    "بَيْت كَبِير · الْبَيْت الْكَبِير · الْبَيْت كَبِير",
    requires=["كبير", "بيت", "مدرسة", "جديد"],
    cards=[
        card("Three patterns, three meanings",
             "An adjective also agrees with its noun in definiteness. If the noun has ال, a describing adjective "
             "must have ال too, and together they are a phrase: “the big house”. If only the noun has ال, there is "
             "no ال on the adjective and you get a sentence: “the house is big”.",
             tables=[table(["Arabic", "English", "What it is"],
                           [["بَيْت كَبِير", "a big house", "phrase"], ["الْبَيْت الْكَبِير", "the big house", "phrase"],
                            ["الْبَيْت كَبِير", "the house is big", "sentence"],
                            ["مَدْرَسَة جَدِيدَة", "a new school", "phrase"], ["الْمَدْرَسَة الْجَدِيدَة", "the new school", "phrase"],
                            ["الْمَدْرَسَة جَدِيدَة", "the school is new", "sentence"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("With هَذَا and with two adjectives",
             "هَذَا + a noun with ال means “this …”. Compare هَذَا بَيْت كَبِير (this is a big house) with "
             "هَذَا الْبَيْت كَبِير (this house is big). Two adjectives can follow one another, and each takes ال if the noun does; joining them with و is also possible.",
             examples=[
                 ex("هَذَا بَيْت كَبِير.", "This is a big house."),
                 ex("هَذَا الْبَيْت كَبِير.", "This house is big."),
                 ex("أَسْكُن فِي الْبَيْت الْجَدِيد.", "I live in the new house."),
                 ex("الْمَدِينَة الْقَدِيمَة جَمِيلَة.", "The old city is beautiful."),
                 ex("الْفُنْدُق الْكَبِير الْجَدِيد قَرِيب مِنَ الْمَحَطَّة.", "The big, new hotel is near the station."),
             ]),
    ],
    exercises=[
        M("Which means “the big house”?", "الْبَيْت الْكَبِير", ["الْبَيْت كَبِير", "بَيْت الْكَبِير", "بَيْت كَبِير"], "Both words take ال: a phrase."),
        M("Which means “the house is big”?", "الْبَيْت كَبِير", ["الْبَيْت الْكَبِير", "بَيْت الْكَبِير", "بَيْت كَبِير"], "Only the noun takes ال: a sentence."),
        M("Which means “a big house”?", "بَيْت كَبِير", ["الْبَيْت الْكَبِير", "الْبَيْت كَبِير", "بَيْت الْكَبِير"], "Neither word takes ال."),
        M("Which means “the new school”?", "الْمَدْرَسَة الْجَدِيدَة", ["الْمَدْرَسَة جَدِيدَة", "مَدْرَسَة الْجَدِيدَة", "الْمَدْرَسَة الْجَدِيد"], "ال on both, feminine adjective."),
        M("Which means “The school is new”?", "الْمَدْرَسَة جَدِيدَة", ["الْمَدْرَسَة الْجَدِيدَة", "مَدْرَسَة الْجَدِيدَة", "الْمَدْرَسَة جَدِيد"], "ال on the noun only, feminine adjective."),
        M("Which means “This house is big”?", "هَذَا الْبَيْت كَبِير", ["هَذَا بَيْت كَبِير", "هَذَا الْبَيْت الْكَبِير", "هَذِهِ الْبَيْت كَبِير"], "هَذَا + noun with ال + adjective without ال."),
        M("Which means “This is a big house”?", "هَذَا بَيْت كَبِير", ["هَذَا الْبَيْت كَبِير", "هَذَا الْبَيْت الْكَبِير", "هَذِهِ بَيْت كَبِير"], "No ال anywhere."),
        F("الْمَدِينَة ___ جَمِيلَة.", "الْقَدِيمَة", ["قَدِيمَة", "الْقَدِيم", "قَدِيم"], "The old city: ال on both words.", tr="The old city is beautiful."),
        F("أَسْكُن فِي الْبَيْت ___.", "الْجَدِيد", ["جَدِيد", "الْجَدِيدَة", "جَدِيدَة"], "The new house: ال on both words.", tr="I live in the new house."),
    ],
    verify=vw("الْبَيْت", "الْكَبِير", "الْمَدْرَسَة", "الْجَدِيدَة", "الْقَدِيمَة", "الْجَدِيد"),
)

# ---------------------------------------------------------------------------- 56
L56 = lesson(
    "Opposites: describing things",
    "جَدِيد ≠ قَدِيم · سَهْل ≠ صَعْب",
    requires=["جديد", "قديم", "سهل", "صعب", "جيد", "سريع", "رخيص", "غالي"],
    cards=[
        card("Pairs of opposites",
             "Learning adjectives in pairs makes them easy to remember. Each is shown in the masculine form.",
             tables=[table(["English", "Adjective", "Opposite"],
                           [["new – old", "جَدِيد", "قَدِيم"], ["easy – difficult", "سَهْل", "صَعْب"],
                            ["fast – slow", "سَرِيع", "بَطِيء"], ["cheap – expensive", "رَخِيص", "غَالِي"],
                            ["big – small", "كَبِير", "صَغِير"], ["long – short", "طَوِيل", "قَصِير"],
                            ["beautiful – ugly", "جَمِيل", "قَبِيح"], ["good – bad", "جَيِّد", "سَيِّئ"],
                            ["hot – cold", "حَارّ", "بَارِد"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Describing things",
             "Remember to match the gender, and to use و between two adjectives in a predicate.",
             examples=[
                 ex("الْفُنْدُق جَدِيد وَنَظِيف.", "The hotel is new and clean."),
                 ex("الدَّرْس سَهْل وَالْكِتَاب جَيِّد.", "The lesson is easy and the book is good."),
                 ex("الْقِطَار سَرِيع.", "The train is fast."),
                 ex("السَّيَّارَة سَرِيعَة وَغَالِيَة.", "The car is fast and expensive."),
                 ex("الْمَطْعَم قَدِيم وَرَخِيص.", "The restaurant is old and cheap."),
                 ex("هَلِ الْمَطْعَم غَالِي؟ لَا، هُوَ رَخِيص.", "Is the restaurant expensive? No, it is cheap."),
             ]),
    ],
    exercises=[
        M("Which word is the opposite of جَدِيد?", "قَدِيم", ["سَهْل", "كَبِير", "رَخِيص"], "new ≠ old."),
        M("Which word is the opposite of سَهْل?", "صَعْب", ["قَدِيم", "سَرِيع", "جَيِّد"], "easy ≠ difficult."),
        M("Which word is the opposite of سَرِيع?", "بَطِيء", ["صَعْب", "جَدِيد", "قَصِير"], "fast ≠ slow."),
        M("Which word is the opposite of رَخِيص?", "غَالِي", ["جَيِّد", "قَدِيم", "بَطِيء"], "cheap ≠ expensive."),
        M("Which word is the opposite of جَمِيل?", "قَبِيح", ["جَيِّد", "صَغِير", "طَوِيل"], "beautiful ≠ ugly."),
        M("Which means “The train is fast”?", "الْقِطَار سَرِيع", ["الْقِطَار بَطِيء", "الْقِطَار سَرِيعَة", "قِطَار السَّرِيع"], "الْقِطَار is masculine."),
        M("Which means “The car is fast and expensive”?", "السَّيَّارَة سَرِيعَة وَغَالِيَة", ["السَّيَّارَة سَرِيع وَغَالِي", "السَّيَّارَة سَرِيعَة وَرَخِيصَة", "السَّيَّارَة بَطِيئَة وَغَالِيَة"], "السَّيَّارَة is feminine."),
        F("الدَّرْس ___.", "سَهْل", ["سَهْلَة", "صَعْبَة", "قَدِيمَة"], "The lesson is easy; الدَّرْس is masculine.", tr="The lesson is easy."),
        F("هَلِ الْمَطْعَم غَالِي؟ لَا، هُوَ ___.", "رَخِيص", ["غَالِي", "جَدِيدَة", "رَخِيصَة"], "The opposite of expensive, masculine.", tr="Is the restaurant expensive? No, it is cheap."),
    ],
    verify=(vf("سَرِيع", "سَرِيعَة") + vf("غَالِي", "غَالِيَة") + vf("رَخِيص", "رَخِيصَة")
            + vw("سَهْل", "صَعْب", "بَطِيء", "رَخِيص", "غَالِي", "قَبِيح", "سَيِّئ", "الْقِطَار", "نَظِيف")),
)

# ---------------------------------------------------------------------------- 57
L57 = lesson(
    "Plural nouns and their adjectives",
    "مُهَنْدِسُون مِصْرِيُّون · كُتُب جَدِيدَة",
    requires=["كتاب", "بيت", "مدينة", "طالب", "مهندس", "جديد"],
    cards=[
        card("People: a plural adjective",
             "When the noun is a group of people, the adjective is plural too: ـُون for men and ـَات for women (طُلَّاب مِصْرِيُّون, طَالِبَات مِصْرِيَّات).",
             tables=[table(["Arabic", "English"],
                           [["مُهَنْدِسُون مِصْرِيُّون", "Egyptian engineers"], ["مُدَرِّسُون سُورِيُّون", "Syrian teachers"],
                            ["مُدَرِّسَات سُورِيَّات", "Syrian teachers (women)"], ["طَالِبَات مِصْرِيَّات", "Egyptian students (women)"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("Things: a feminine singular adjective",
             "When the plural names things or animals, the adjective is feminine singular, whatever the gender of the "
             "noun in the singular. A plural of things is treated as one feminine group.",
             tables=[table(["Arabic", "English"],
                           [["كُتُب جَدِيدَة", "new books"], ["مُدُن كَبِيرَة", "big cities"], ["بُيُوت قَدِيمَة", "old houses"],
                            ["شَوَارِع طَوِيلَة", "long streets"], ["سَيَّارَات سَرِيعَة", "fast cars"]],
                           say=[0], tlit=[0], gloss=False)],
             examples=[
                 ex("هَذِهِ كُتُب جَدِيدَة.", "These are new books."),
                 ex("الْبُيُوت الْقَدِيمَة جَمِيلَة.", "The old houses are beautiful."),
                 ex("الْمُدُن الْكَبِيرَة بَعِيدَة.", "The big cities are far."),
                 ex("الْمُهَنْدِسُون الْمِصْرِيُّون فِي الْمَكْتَب.", "The Egyptian engineers are in the office."),
             ]),
    ],
    exercises=[
        M("Which means “Egyptian engineers”?", "مُهَنْدِسُون مِصْرِيُّون", ["مُهَنْدِسُون مِصْرِيَّة", "مُهَنْدِسَات مِصْرِيُّون", "مُهَنْدِس مِصْرِيُّون"], "People: the adjective is plural too."),
        M("Which means “Syrian teachers (women)”?", "مُدَرِّسَات سُورِيَّات", ["مُدَرِّسَات سُورِيُّون", "مُدَرِّسُون سُورِيَّات", "مُدَرِّسَة سُورِيَّات"], "Feminine sound plural for both."),
        M("Which means “new books”?", "كُتُب جَدِيدَة", ["كُتُب جَدِيد", "كُتُب جَدِيدُون", "كِتَاب جَدِيدَة"], "Things: feminine singular adjective."),
        M("Which means “big cities”?", "مُدُن كَبِيرَة", ["مُدُن كَبِير", "مُدُن كَبِيرُون", "مَدِينَة كَبِيرَات"], "Things: feminine singular adjective."),
        M("Which means “old houses”?", "بُيُوت قَدِيمَة", ["بُيُوت قَدِيم", "بَيْت قَدِيمَة", "بُيُوت قَدِيمُون"], "Things: feminine singular adjective."),
        M("An adjective for a plural of things is…", "feminine singular", ["masculine plural", "feminine plural", "masculine singular"], "A plural of things is treated as feminine singular."),
        M("An adjective for a plural group of people is…", "plural, like the noun", ["always feminine singular", "always masculine singular", "dual"], "Match the people."),
        F("هَذِهِ ___ جَدِيدَة.", "كُتُب", ["كِتَاب", "طُلَّاب", "مُهَنْدِسُون"], "Books are things.", tr="These are new books."),
        F("الْبُيُوت ___ جَمِيلَة.", "الْقَدِيمَة", ["الْقَدِيم", "الْقُدَمَاء", "الْقَدِيمُون"], "A plural of things takes the feminine singular, with ال.", tr="The old houses are beautiful."),
    ],
    verify=(vps("مِصْرِيّ", "مِصْرِيُّون") + vps("سُورِيّ", "سُورِيُّون") + vps("سُورِيَّة", "سُورِيَّات") + vps("مِصْرِيَّة", "مِصْرِيَّات")
            + vps("مُدَرِّسَة", "مُدَرِّسَات") + vps("طَالِبَة", "طَالِبَات") + vps("مُدَرِّس", "مُدَرِّسُون")
            + vw("جَدِيدَة", "كَبِيرَة", "قَدِيمَة", "طَوِيلَة", "سَرِيعَة")),
)

# ---------------------------------------------------------------------------- 58
L58 = lesson(
    "The family",
    "أَب · أُمّ · أَخ · أُخْت · اِبْن · اِبْنَة",
    requires=["أب", "أم", "أخ", "أخت", "ولد", "بنت", "زوج", "زوجة", "جد", "عائلة"],
    cards=[
        card("Close family",
             "Pairs of masculine and feminine words. Most follow the usual rule of adding ة; أَخ and أُخْت, أَب and "
             "أُمّ are separate words.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["father – mother", "أَب", "أُمّ"], ["brother – sister", "أَخ", "أُخْت"],
                            ["son – daughter", "اِبْن", "اِبْنَة"], ["husband – wife", "زَوْج", "زَوْجَة"],
                            ["grandfather – grandmother", "جَدّ", "جَدَّة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Uncles, aunts and the family as a whole",
             "Arabic names relatives on the father’s side and on the mother’s side separately.",
             tables=[table(["English", "Arabic"],
                           [["father’s brother (uncle)", "عَمّ"], ["father’s sister (aunt)", "عَمَّة"],
                            ["mother’s brother (uncle)", "خَال"], ["mother’s sister (aunt)", "خَالَة"],
                            ["family", "عَائِلَة · أُسْرَة"], ["boy, child", "وَلَد"], ["girl, daughter", "بِنْت"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Plurals for the family",
             "These plurals are broken plurals, so learn them as they are. إِخْوَة can mean brothers, or brothers "
             "and sisters together.",
             tables=[table(["English", "Singular", "Plural"],
                           [["brother", "أَخ", "إِخْوَة"], ["sister", "أُخْت", "أَخَوَات"],
                            ["son, child", "اِبْن", "أَبْنَاء"], ["boy", "وَلَد", "أَوْلَاد"]],
                           say=[1, 2], tlit=[2], gloss=False)],
             examples=[
                 ex("هَذِهِ أُسْرَة كَبِيرَة.", "This is a big family."),
                 ex("الْأَب وَالْأُمّ وَالْأَوْلَاد فِي الْبَيْت.", "The father, the mother and the children are in the house."),
                 ex("الْجَدّ سَعِيد وَالْجَدَّة سَعِيدَة.", "The grandfather is happy and the grandmother is happy."),
             ]),
    ],
    exercises=[
        M("Which word means “mother”?", "أُمّ", ["أَب", "أُخْت", "جَدَّة"], "أُمّ = mother."),
        M("Which word means “father”?", "أَب", ["أَخ", "جَدّ", "عَمّ"], "أَب = father."),
        M("Which word means “sister”?", "أُخْت", ["أُمّ", "اِبْنَة", "خَالَة"], "أُخْت = sister."),
        M("Which word means “brother”?", "أَخ", ["أَب", "اِبْن", "عَمّ"], "أَخ = brother."),
        M("Which word means “daughter”?", "اِبْنَة", ["اِبْن", "زَوْجَة", "أُخْت"], "اِبْنَة = daughter."),
        M("Which word means “wife”?", "زَوْجَة", ["زَوْج", "أُخْت", "عَمَّة"], "زَوْجَة = wife."),
        M("Which word means “mother’s brother”?", "خَال", ["عَمّ", "جَدّ", "أَخ"], "خَال = mother’s brother; عَمّ = father’s brother."),
        M("Which is the plural of أَخ?", "إِخْوَة", ["أَخَوَات", "أَخُون", "أَخَات"], "أَخ → إِخْوَة."),
        M("Which is the plural of أُخْت?", "أَخَوَات", ["إِخْوَة", "أُخْتَات", "أُخْتُون"], "أُخْت → أَخَوَات."),
        F("الْجَدّ سَعِيد وَ___ سَعِيدَة.", "الْجَدَّة", ["الْجَدّ", "الْعَمّ", "الْأَب"], "A woman, feminine adjective.", tr="The grandfather is happy and the grandmother is happy."),
    ],
    verify=(vf("اِبْن", "اِبْنَة") + vf("زَوْج", "زَوْجَة") + vf("جَدّ", "جَدَّة") + vf("عَمّ", "عَمَّة") + vf("خَال", "خَالَة")
            + vpb("أَخ", "إِخْوَة") + vpb("أُخْت", "أَخَوَات") + vpb("اِبْن", "أَبْنَاء") + vpb("وَلَد", "أَوْلَاد")
            + vw("أَب", "أُمّ", "أَخ", "أُخْت", "بِنْت", "عَائِلَة", "أُسْرَة")),
)

# ---------------------------------------------------------------------------- 59
L59 = lesson(
    "My mother, your father",
    "أُمِّي · أَبُوكَ · أُخْتُهَا",
    requires=["أب", "أم", "أخ", "أخت", "جد", "عم", "أسرة"],
    cards=[
        card("Endings on family words",
             "The endings you learned in unit 2 attach to family nouns exactly as they do to كِتَاب. Two small points: "
             "a doubled letter keeps its shadda (أُمّ → أُمِّي), and ة turns into ت (جَدَّة → جَدَّتِي).",
             tables=[table(["English", "my", "your (man)", "his", "her"],
                           [["mother", "أُمِّي", "أُمُّكَ", "أُمُّهُ", "أُمُّهَا"], ["sister", "أُخْتِي", "أُخْتُكَ", "أُخْتُهُ", "أُخْتُهَا"],
                            ["son", "اِبْنِي", "اِبْنُكَ", "اِبْنُهُ", "اِبْنُهَا"], ["grandfather", "جَدِّي", "جَدُّكَ", "جَدُّهُ", "جَدُّهَا"],
                            ["grandmother", "جَدَّتِي", "جَدَّتُكَ", "جَدَّتُهُ", "جَدَّتُهَا"]],
                           say=[1, 2, 3, 4], tlit=[1], gloss=False)]),
        card("Father and brother are different",
             "أَب and أَخ add a long vowel ـُو before ـكَ ـهُ ـهَا. With ـِي they are regular. Use the long-vowel "
             "forms below when the word is the subject of a sentence; in other positions the form changes.",
             tables=[table(["English", "my", "your (man)", "his", "her"],
                           [["father", "أَبِي", "أَبُوكَ", "أَبُوهُ", "أَبُوهَا"], ["brother", "أَخِي", "أَخُوكَ", "أَخُوهُ", "أَخُوهَا"]],
                           say=[1, 2, 3, 4], tlit=[1], gloss=False)],
             examples=[
                 ex("أَبِي طَبِيب وَأُمِّي مُدَرِّسَة.", "My father is a doctor and my mother is a teacher."),
                 ex("أَخِي كَبِير وَأُخْتِي صَغِيرَة.", "My brother is grown-up and my sister is little."),
                 ex("هَلْ أَبُوكَ مُهَنْدِس؟", "Is your father an engineer?"),
                 ex("أَبُوهَا مُدَرِّس وَأُمُّهَا طَبِيبَة.", "Her father is a teacher and her mother is a doctor."),
                 ex("جَدِّي كَبِير وَجَدَّتِي سَعِيدَة.", "My grandfather is old and my grandmother is happy."),
             ]),
    ],
    exercises=[
        M("How do you say “my mother”?", "أُمِّي", ["أُمُّكَ", "أُمُّهَا", "أُمَّتِي"], "أُمّ + ـِي, with the shadda."),
        M("How do you say “my grandmother”?", "جَدَّتِي", ["جَدَّةِي", "جَدُّكَ", "جَدَّتُهُ"], "ة becomes ت."),
        M("How do you say “her sister”?", "أُخْتُهَا", ["أُخْتُهُ", "أُخْتِي", "أُخْتُكَ"], "ـهَا = her."),
        M("How do you say “his mother”?", "أُمُّهُ", ["أُمُّهَا", "أُمِّي", "أُمُّكَ"], "ـهُ = his."),
        M("How do you say “your (man’s) son”?", "اِبْنُكَ", ["اِبْنِي", "اِبْنُهُ", "اِبْنُكِ"], "ـكَ = your (to a man)."),
        M("How do you say “her father”?", "أَبُوهَا", ["أَخُوهَا", "أَبُوهُ", "أَبُوكَ"], "أَب lengthens to أَبُو before ـهَا."),
        M("How do you say “his brother”?", "أَخُوهُ", ["أَخُوهَا", "أَبُوهُ", "أَخُوكَ"], "أَخ lengthens to أَخُو before ـهُ."),
        M("How do you say “my father”?", "أَبِي", ["أَبُوكَ", "أَبُوهُ", "أَبَاهُ"], "ـِي is added directly."),
        F("أَخِي كَبِير وَ___ صَغِيرَة.", "أُخْتِي", ["أَخُوهُ", "أُخْتُكَ", "أَبِي"], "A feminine word for the little one.", tr="My brother is grown-up and my sister is little."),
        F("هَلْ ___ مُهَنْدِس؟", "أَبُوكَ", ["أَبِي", "أَبُوهَا", "أُمُّكَ"], "Asking a man about his father.", tr="Is your father an engineer?"),
    ],
    verify=vw("أُمِّي", "أُمُّكَ", "أُمُّهُ", "أُمُّهَا", "أُخْتِي", "أُخْتُكَ", "أُخْتُهُ", "أُخْتُهَا", "اِبْنِي", "اِبْنُكَ", "اِبْنُهُ",
              "اِبْنُهَا", "جَدِّي", "جَدُّكَ", "جَدُّهُ", "جَدُّهَا", "جَدَّتِي", "جَدَّتُكَ", "جَدَّتُهُ", "جَدَّتُهَا", "أَبِي", "أَخِي",
              "أَبُوكَ", "أَبُوهُ", "أَبُوهَا", "أَخُوكَ", "أَخُوهُ", "أَخُوهَا"),
)

# ---------------------------------------------------------------------------- 60
L60 = lesson(
    "Describing people",
    "طَوِيل · سَعِيد · مَشْغُول · لَطِيف",
    requires=["طويل", "قصير", "سعيد", "كبير", "صغير", "شاب", "مريض"],
    cards=[
        card("Adjectives for people",
             "The same adjective-agreement rules apply: add ة for a woman. Remember that a man says "
             "أَنَا مَشْغُول and a woman says أَنَا مَشْغُولَة.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["tall", "طَوِيل", "طَوِيلَة"], ["short", "قَصِير", "قَصِيرَة"], ["happy", "سَعِيد", "سَعِيدَة"],
                            ["sad", "حَزِين", "حَزِينَة"], ["ill", "مَرِيض", "مَرِيضَة"], ["young", "شَابّ", "شَابَّة"],
                            ["busy", "مَشْغُول", "مَشْغُولَة"], ["kind, nice", "لَطِيف", "لَطِيفَة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("With family words",
             "A noun with an attached pronoun is definite. So if you add an adjective to it as a description, that "
             "adjective takes ال: أَخِي الْكَبِير means “my older brother”.",
             examples=[
                 ex("أَخِي طَوِيل وَأُخْتِي قَصِيرَة.", "My brother is tall and my sister is short."),
                 ex("أُمِّي سَعِيدَة.", "My mother is happy."),
                 ex("أَخِي الْكَبِير مُهَنْدِس.", "My older brother is an engineer.", "أَخِي الْكَبِير"),
                 ex("أُخْتِي الصَّغِيرَة طَالِبَة.", "My younger sister is a student.", "أُخْتِي الصَّغِيرَة"),
                 ex("هَلْ أَنْتِ سَعِيدَة؟", "Are you happy? (to a woman)"),
                 ex("أَنَا مَشْغُول الْيَوْم.", "I am busy today. (a man speaking)"),
             ]),
    ],
    exercises=[
        M("Which means “tall” (for a woman)?", "طَوِيلَة", ["طَوِيل", "طُوَال", "قَصِيرَة"], "Add ة for a woman."),
        M("Which means “happy” (for a man)?", "سَعِيد", ["سَعِيدَة", "حَزِين", "مَرِيض"], "Masculine form."),
        M("A woman says she is busy. She says…", "أَنَا مَشْغُولَة", ["أَنَا مَشْغُول", "أَنَا مَشْغُولُون", "هِيَ مَشْغُول"], "A woman uses the feminine adjective."),
        M("Which means “my older brother”?", "أَخِي الْكَبِير", ["أَخِي كَبِير", "الْأَخ الْكَبِير", "أَخِي الْكَبِيرَة"], "Possessed noun is definite, so the adjective takes ال."),
        M("Which means “my younger sister”?", "أُخْتِي الصَّغِيرَة", ["أُخْتِي صَغِيرَة", "أُخْتِي الصَّغِير", "الْأُخْت صَغِيرَة"], "ال plus the feminine adjective."),
        M("Which means “My brother is tall”?", "أَخِي طَوِيل", ["أَخِي الطَّوِيل", "أَخِي طَوِيلَة", "الْأَخ طَوِيلَة"], "A sentence: no ال on the adjective."),
        M("Which word means “sad”?", "حَزِين", ["سَعِيد", "لَطِيف", "مَشْغُول"], "حَزِين = sad."),
        F("أُخْتِي ___.", "قَصِيرَة", ["قَصِير", "قَصِيرُون", "الْقَصِيرَة"], "أُخْتِي is feminine.", tr="My sister is short."),
        F("أَخِي ___ مُهَنْدِس.", "الْكَبِير", ["كَبِير", "الْكَبِيرَة", "كَبِيرَة"], "“My older brother”: ال on the adjective.", tr="My older brother is an engineer."),
    ],
    verify=(vf("طَوِيل", "طَوِيلَة") + vf("قَصِير", "قَصِيرَة") + vf("سَعِيد", "سَعِيدَة") + vf("حَزِين", "حَزِينَة")
            + vf("مَرِيض", "مَرِيضَة") + vf("شَابّ", "شَابَّة") + vf("مَشْغُول", "مَشْغُولَة") + vf("لَطِيف", "لَطِيفَة")),
)

# ---------------------------------------------------------------------------- 61
L61 = lesson(
    "What does your father do?",
    "أَبِي طَبِيب · إِخْوَتِي مُهَنْدِسُون",
    requires=["طبيب", "مهندس", "مدرس", "موظف", "أب", "أم"],
    cards=[
        card("Jobs, masculine and feminine",
             "Jobs have a masculine and a feminine form. Use the one that matches the person you are describing.",
             tables=[table(["English", "Man", "Woman"],
                           [["doctor", "طَبِيب", "طَبِيبَة"], ["teacher", "مُدَرِّس", "مُدَرِّسَة"],
                            ["engineer", "مُهَنْدِس", "مُهَنْدِسَة"], ["nurse", "مُمَرِّض", "مُمَرِّضَة"],
                            ["employee", "مُوَظَّف", "مُوَظَّفَة"], ["driver", "سَائِق", "سَائِقَة"],
                            ["merchant", "تَاجِر", "تَاجِرَة"], ["cook", "طَبَّاخ", "طَبَّاخَة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Talking about the family’s work",
             "To ask about work, use مَاذَا يَعْمَل …؟ (for a man) or مَاذَا تَعْمَل …؟ (for a woman); أَيْنَ يَعْمَل and أَيْنَ تَعْمَل ask where. With plural family words "
             "like إِخْوَتِي (my brothers and sisters), use the plural job words from the lessons on plurals.",
             examples=[
                 ex("مَاذَا يَعْمَل أَبُوكَ؟", "What does your father do?"),
                 ex("أَبِي طَبِيب.", "My father is a doctor."),
                 ex("أَيْنَ تَعْمَل أُمُّكَ؟", "Where does your mother work?"),
                 ex("تَعْمَل أُمِّي فِي مُسْتَشْفَى.", "My mother works in a hospital."),
                 ex("إِخْوَتِي مُهَنْدِسُون وَأَخَوَاتِي مُدَرِّسَات.", "My brothers are engineers and my sisters are teachers."),
                 ex("زَوْجِي مُوَظَّف فِي بَنْك.", "My husband is a bank employee."),
             ]),
    ],
    exercises=[
        M("Which means “My father is a doctor”?", "أَبِي طَبِيب", ["أَبِي طَبِيبَة", "أُمِّي طَبِيب", "أَبِي طُلَّاب"], "أَبِي is masculine."),
        M("Which means “My mother is a doctor”?", "أُمِّي طَبِيبَة", ["أُمِّي طَبِيب", "أَبِي طَبِيبَة", "أُمِّي أَطِبَّاء"], "A woman: ة."),
        M("Which question asks “What does your father do?”", "مَاذَا يَعْمَل أَبُوكَ؟", ["أَيْنَ يَعْمَل أَبُوكَ؟", "مَاذَا تَعْمَل أَبُوكَ؟", "مَنْ يَعْمَل أَبُوكَ؟"], "مَاذَا + يَعْمَل (he works)."),
        M("Which means “My sisters are teachers”?", "أَخَوَاتِي مُدَرِّسَات", ["أَخَوَاتِي مُدَرِّسُون", "أُخْتِي مُدَرِّسَات", "أَخَوَاتِي مُدَرِّسَة"], "Feminine human plural: ـَات."),
        M("Which means “My brothers are engineers”?", "إِخْوَتِي مُهَنْدِسُون", ["إِخْوَتِي مُهَنْدِسَات", "أَخِي مُهَنْدِسُون", "إِخْوَتِي مُهَنْدِس"], "Masculine human plural: ـُون."),
        M("Which job word is feminine?", "مُمَرِّضَة", ["مُمَرِّض", "طَبِيب", "تَاجِر"], "ة marks the feminine."),
        M("Which means “Where does your mother work?”", "أَيْنَ تَعْمَل أُمُّكَ؟", ["أَيْنَ يَعْمَل أُمُّكَ؟", "مَاذَا تَعْمَل أُمُّكَ؟", "كَيْفَ تَعْمَل أُمُّكَ؟"], "A feminine subject takes تَـ."),
        F("تَعْمَل أُمِّي فِي ___.", "مُسْتَشْفَى", ["جَبَل", "نَهْر", "غَابَة"], "A place where doctors work.", tr="My mother works in a hospital."),
        F("زَوْجِي ___ فِي بَنْك.", "مُوَظَّف", ["مُوَظَّفَة", "مُوَظَّفُون", "مُوَظَّفَات"], "زَوْجِي (my husband) is masculine.", tr="My husband is a bank employee."),
    ],
    verify=(vf("طَبِيب", "طَبِيبَة") + vf("مُدَرِّس", "مُدَرِّسَة") + vf("مُهَنْدِس", "مُهَنْدِسَة") + vf("مُمَرِّض", "مُمَرِّضَة")
            + vf("مُوَظَّف", "مُوَظَّفَة") + vf("سَائِق", "سَائِقَة") + vf("تَاجِر", "تَاجِرَة") + vf("طَبَّاخ", "طَبَّاخَة")
            + vv("عمل", "pres", huwa="يَعْمَل", hiya="تَعْمَل") + vps("مُهَنْدِس", "مُهَنْدِسُون") + vps("مُدَرِّسَة", "مُدَرِّسَات")
            + vpb("أُخْت", "أَخَوَات") + vpb("أَخ", "إِخْوَة") + vw("إِخْوَتِي", "أَخَوَاتِي", "زَوْجِي", "مُسْتَشْفَى")),
)

# ---------------------------------------------------------------------------- 62
L62 = lesson(
    "Phone numbers and addresses",
    "رَقْم الْهَاتِف · الْعُنْوَان",
    requires=["هاتف", "رقم", "عنوان", "شارع", "مدينة"],
    cards=[
        card("Asking",
             "رَقْم is “number”. Add the ending to ask for someone’s phone number, with ـكَ for a man and ـكِ for a woman.",
             examples=[
                 ex("مَا رَقْم هَاتِفِكَ؟", "What is your phone number? (to a man)", "هَاتِفِكَ"),
                 ex("مَا رَقْم هَاتِفِكِ؟", "What is your phone number? (to a woman)", "هَاتِفِكِ"),
                 ex("مَا عُنْوَانُكَ؟", "What is your address? (to a man)"),
                 ex("أَسْكُن فِي شَارِع الْجَامِعَة.", "I live on University Street."),
                 ex("مَا رَقْم الشَّقَّة؟", "What is the apartment number?"),
             ]),
        card("Saying a phone number",
             "A phone number is usually read one digit at a time, in the order you see it from left to right, using the "
             "counting words from unit 1. The numbers below are made up.",
             tables=[table(["Digits", "Said aloud"],
                           [["٠١٢ ٣٤٥", "صِفْر · وَاحِد · اِثْنَان · ثَلَاثَة · أَرْبَعَة · خَمْسَة"],
                            ["٥٥٥ ٠١٠٠", "خَمْسَة · خَمْسَة · خَمْسَة · صِفْر · وَاحِد · صِفْر · صِفْر"],
                            ["٩٨٧ ٦٥٤", "تِسْعَة · ثَمَانِيَة · سَبْعَة · سِتَّة · خَمْسَة · أَرْبَعَة"]],
                           say=[1], gloss=False)]),
    ],
    exercises=[
        M("How do you ask a man for his phone number?", "مَا رَقْم هَاتِفِكَ؟", ["مَا رَقْم هَاتِفِكِ؟", "مَا رَقْم هَاتِفِي؟", "مَا عُنْوَانُكَ؟"], "ـكَ for a man."),
        M("How do you ask a woman for her phone number?", "مَا رَقْم هَاتِفِكِ؟", ["مَا رَقْم هَاتِفِكَ؟", "مَا رَقْم هَاتِفِهَا؟", "مَا رَقْم هَاتِفِنَا؟"], "ـكِ for a woman."),
        M("What does مَا عُنْوَانُكَ؟ ask for?", "an address", ["a phone number", "a name", "an age"], "عُنْوَان = address."),
        M("What does مَا رَقْم الشَّقَّة؟ ask for?", "the apartment number", ["the street name", "the phone number", "the floor"], "شَقَّة = apartment."),
        M("How is the digit ٣ said?", "ثَلَاثَة", ["اِثْنَان", "أَرْبَعَة", "وَاحِد"], "٣ = three."),
        M("How is the digit ٧ said?", "سَبْعَة", ["سِتَّة", "ثَمَانِيَة", "خَمْسَة"], "٧ = seven."),
        M("How is the digit ٠ said?", "صِفْر", ["وَاحِد", "عَشَرَة", "تِسْعَة"], "٠ = zero."),
        M("In which order is a phone number read?", "digit by digit, left to right", ["as one big number", "right to left", "in pairs only"], "Phone numbers are spelled out digit by digit."),
        F("مَا ___ هَاتِفِكَ؟", "رَقْم", ["عُمْر", "اِسْم", "بَيْت"], "A number is رَقْم.", tr="What is your phone number?"),
        F("أَسْكُن فِي ___ الْجَامِعَة.", "شَارِع", ["بَحْر", "جَبَل", "نَهْر"], "Where an address begins.", tr="I live on University Street."),
    ],
    verify=vw("رَقْم", "هَاتِفِكَ", "هَاتِفِكِ", "عُنْوَانُكَ", "شَقَّة", "صِفْر", "وَاحِد", "اِثْنَان", "ثَلَاثَة", "أَرْبَعَة", "خَمْسَة",
              "سِتَّة", "سَبْعَة", "ثَمَانِيَة", "تِسْعَة"),
)

# ---------------------------------------------------------------------------- 63
L63 = lesson(
    "My city",
    "مَدِينَتِي كَبِيرَة وَجَمِيلَة",
    requires=["مدينة", "شارع", "مسجد", "سوق", "جامعة", "جميل", "كبير"],
    cards=[
        card("A short text",
             "Read this description line by line. Everything in it uses the grammar of unit 4: plurals, "
             "adjectives that agree, and position words.",
             examples=[
                 ex("مَدِينَتِي كَبِيرَة وَجَمِيلَة.", "My city is big and beautiful."),
                 ex("فِي الْمَدِينَة شَوَارِع طَوِيلَة وَحَدَائِق كَثِيرَة.", "In the city there are long streets and many parks."),
                 ex("الْمَدِينَة الْقَدِيمَة فِي الشَّمَال وَالْجَامِعَة فِي الْجَنُوب.", "The old city is in the north and the university is in the south."),
                 ex("بِجَانِب الْجَامِعَة مَكْتَبَة كَبِيرَة وَمَقْهَى صَغِير.", "Next to the university there is a big library and a small café."),
                 ex("السُّوق الْقَدِيم رَخِيص وَالْمَطَاعِم جَيِّدَة.", "The old market is cheap and the restaurants are good."),
                 ex("أُحِبّ مَدِينَتِي لِأَنَّ النَّاس لَطِيفُون.", "I like my city because the people are kind."),
             ]),
    ],
    exercises=[
        M("«الْمَدِينَة الْقَدِيمَة فِي الشَّمَال وَالْجَامِعَة فِي الْجَنُوب.» Where is the university?", "In the south", ["In the north", "In the east", "In the west"], "الْجَنُوب = south."),
        M("«بِجَانِب الْجَامِعَة مَكْتَبَة كَبِيرَة وَمَقْهَى صَغِير.» What is next to the university?", "A big library and a small café", ["A small library and a big café", "A museum and a park", "A hotel and a bank"], "كَبِيرَة goes with مَكْتَبَة; صَغِير goes with مَقْهَى."),
        M("«السُّوق الْقَدِيم رَخِيص.» What is the old market like?", "Cheap", ["Expensive", "New", "Far"], "رَخِيص = cheap."),
        M("«فِي الْمَدِينَة شَوَارِع طَوِيلَة.» What are the streets like?", "Long", ["Short", "Beautiful", "Cheap"], "طَوِيلَة = long."),
        M("«أُحِبّ مَدِينَتِي لِأَنَّ النَّاس لَطِيفُون.» Why does the writer like the city?", "The people are kind", ["The market is cheap", "The streets are long", "The weather is warm"], "لِأَنَّ = because; لَطِيفُون = kind."),
        M("Which means “the old city”?", "الْمَدِينَة الْقَدِيمَة", ["الْمَدِينَة قَدِيمَة", "مَدِينَة الْقَدِيمَة", "الْمَدِينَة الْقَدِيم"], "ال on both, feminine adjective."),
        M("Which means “my city is big”?", "مَدِينَتِي كَبِيرَة", ["مَدِينَتِي كَبِير", "الْمَدِينَة مَدِينَتِي", "مَدِينَةِي كَبِيرَة"], "ة becomes ت before ـِي."),
        F("فِي الْمَدِينَة شَوَارِع ___.", "طَوِيلَة", ["طَوِيل", "طَوِيلُون", "الطَّوِيلَة"], "A plural of things takes the feminine singular.", tr="In the city there are long streets."),
        F("النَّاس ___.", "لَطِيفُون", ["لَطِيف", "لَطِيفَة", "لَطِيفَات"], "People: a plural adjective.", tr="The people are kind."),
    ],
    verify=vw("مَدِينَتِي", "الْمَدِينَة", "حَدَائِق", "الْمَطَاعِم", "النَّاس", "لَطِيفُون", "الْقَدِيمَة"),
)

# ---------------------------------------------------------------------------- 64
L64 = lesson(
    "Review: my family and my home town",
    "A student introduces her family",
    requires=["أب", "أم", "عائلة", "مدينة", "كبير", "جميل", "جامعة"],
    cards=[
        card("Sara introduces her family",
             "Read what Sara says, then answer the questions.",
             examples=[
                 ex("اِسْمِي سَارَة وَأَنَا طَالِبَة فِي الْجَامِعَة.", "My name is Sara and I am a student at the university."),
                 ex("أَسْكُن فِي بَيْت كَبِير فِي مَدِينَة جَمِيلَة.", "I live in a big house in a beautiful city."),
                 ex("أَبِي مُهَنْدِس وَأُمِّي طَبِيبَة.", "My father is an engineer and my mother is a doctor."),
                 ex("أَخِي الْكَبِير مُوَظَّف فِي بَنْك وَأُخْتِي الصَّغِيرَة طَالِبَة.", "My older brother is a bank employee and my younger sister is a student."),
                 ex("جَدَّتِي لَطِيفَة وَتُحِبّ الشِّتَاء.", "My grandmother is kind and likes winter."),
                 ex("أُحِبّ عَائِلَتِي لِأَنَّهُم سَعِيدُون.", "I love my family because they are happy."),
             ]),
    ],
    exercises=[
        M("What does Sara’s father do?", "He is an engineer", ["He is a doctor", "He is a teacher", "He works at a bank"], "أَبِي مُهَنْدِس."),
        M("What does Sara’s mother do?", "She is a doctor", ["She is an engineer", "She is a teacher", "She is a student"], "أُمِّي طَبِيبَة."),
        M("Who works at a bank?", "Her older brother", ["Her father", "Her younger sister", "Her grandmother"], "أَخِي الْكَبِير مُوَظَّف فِي بَنْك."),
        M("Which means “my older brother”?", "أَخِي الْكَبِير", ["أَخِي كَبِير", "الْأَخ كَبِير", "أَخُوكَ الْكَبِير"], "ال on the adjective."),
        M("Which means “Egyptian engineers (women)”?", "مُهَنْدِسَات مِصْرِيَّات", ["مُهَنْدِسُون مِصْرِيُّون", "مُهَنْدِسَة مِصْرِيَّات", "مُهَنْدِسَات مِصْرِيّ"], "Feminine sound plural for both."),
        M("Which is the plural of كِتَاب?", "كُتُب", ["كِتَابَات", "كُتَّاب", "كِتَابُون"], "كِتَاب → كُتُب."),
        M("Which means “the old houses are beautiful”?", "الْبُيُوت الْقَدِيمَة جَمِيلَة", ["الْبُيُوت الْقَدِيمُون جَمِيلُون", "الْبُيُوت قَدِيمَة الْجَمِيلَة", "بُيُوت الْقَدِيم جَمِيل"], "A plural of things: feminine singular adjective."),
        M("Which means “her father”?", "أَبُوهَا", ["أَبُوهُ", "أَبِي", "أُمُّهَا"], "ـهَا = her."),
        M("The bank is between the library and the restaurant. Which word means “between”?", "بَيْنَ", ["أَمَام", "خَلْف", "فَوْق"], "بَيْنَ = between."),
        F("جَدَّتِي ___ وَتُحِبّ الشِّتَاء.", "لَطِيفَة", ["لَطِيف", "لَطِيفُون", "لَطِيفَات"], "جَدَّة is feminine singular.", tr="My grandmother is kind and likes winter."),
    ],
    verify=vw("لِأَنَّهُم", "سَعِيدُون", "عَائِلَتِي", "لَطِيفَة"),
)

UNIT = unit("المدينة والأسرة: the city, plurals and the family", [L49, L50, L51, L52, L53, L54, L55, L56, L57, L58, L59, L60, L61, L62, L63, L64])
