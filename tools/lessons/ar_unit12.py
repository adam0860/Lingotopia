"""Unit 12: weekends, places and transport, weather plans, suggestions, the verb patterns together (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 169
L169 = lesson(
    "A map of the verb patterns",
    "كَتَبَ · دَرَّسَ · سَاعَدَ · تَعَلَّمَ · تَقَابَلَ",
    requires=["كتب", "درس", "ساعد", "علم", "قابل", "كلم"],
    cards=[
        card("Five patterns side by side",
             "You now know five verb patterns, called Measures. Each one has a clue you can see in the verb. If you see "
             "a verb you do not know, look at the clue first and you already know part of what it will do.",
             tables=[table(["Measure", "Past (he)", "Present (he)", "The clue"],
                           [["I", "كَتَبَ", "يَكْتُب", "just the three root letters"], ["II", "دَرَّسَ", "يُدَرِّس", "the middle letter is doubled"],
                            ["III", "سَاعَدَ", "يُسَاعِد", "a long ā after the first letter"],
                            ["V", "تَعَلَّمَ", "يَتَعَلَّم", "تَـ at the start and the middle letter doubled"],
                            ["VI", "تَقَابَلَ", "يَتَقَابَل", "تَـ at the start and a long ā"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Reading a verb",
             "Measure II often means “cause” (دَرَّسَ, to teach) and Measure V often means “do it to yourself” (تَعَلَّمَ, to learn). Measure III and VI are about other people: "
             "with someone, or to each other.",
             examples=[
                 ex("يَكْتُب أَخِي رِسَالَة.", "My brother writes a letter.", "يَكْتُب"),
                 ex("تُدَرِّس أُخْتِي الْعَرَبِيَّة.", "My sister teaches Arabic.", "تُدَرِّس"),
                 ex("يُسَاعِد أَبِي أُمِّي فِي الْمَطْبَخ.", "My father helps my mother in the kitchen.", "يُسَاعِد"),
                 ex("يَتَعَلَّم أَخِي الْعَرَبِيَّة.", "My brother learns Arabic.", "يَتَعَلَّم"),
                 ex("يَتَقَابَل الطُّلَّاب فِي الْمَكْتَبَة.", "The students meet each other in the library.", "يَتَقَابَل"),
                 ex("تَكَلَّمَتْ مُدَرِّسَتِي مَعَ أُمِّي.", "My teacher spoke with my mother.", "تَكَلَّمَتْ"),
             ]),
    ],
    exercises=[
        M("Which verb has a long ā after the first letter?", "سَاعَدَ", ["دَرَّسَ", "كَتَبَ", "تَعَلَّمَ"], "That is Measure III."),
        M("Which verb has a doubled middle letter and no تَـ?", "دَرَّسَ", ["تَعَلَّمَ", "سَاعَدَ", "كَتَبَ"], "That is Measure II."),
        M("Which present is Measure V?", "يَتَعَلَّم", ["يُدَرِّس", "يَتَقَابَل", "يَكْتُب"], "تَـ + doubled letter."),
        M("Which present is Measure VI?", "يَتَقَابَل", ["يَتَعَلَّم", "يُسَاعِد", "يُدَرِّس"], "تَـ + long ā."),
        M("Which present is Measure I?", "يَكْتُب", ["يُدَرِّس", "يُسَاعِد", "يَتَقَابَل"], "No extra letters."),
        M("What does تَقَابَلَ suggest?", "people did it to each other", ["he did it to himself", "he did it many times", "he did it alone"], "Measure VI is reciprocal."),
        M("Which means “My sister teaches Arabic”?", "تُدَرِّس أُخْتِي الْعَرَبِيَّة", ["تَتَعَلَّم أُخْتِي الْعَرَبِيَّة", "تَدْرُس أُخْتِي الْعَرَبِيَّة", "تُسَاعِد أُخْتِي الْعَرَبِيَّة"], "Measure II: teach."),
        F("يَتَقَابَل ___ فِي الْمَكْتَبَة.", "الطُّلَّاب", ["الْمَكْتَب", "الْكُتُب", "الطَّالِبَة"], "Several people meet each other.", tr="The students meet each other in the library."),
        F("___ أَخِي الْعَرَبِيَّة.", "يَتَعَلَّم", ["يُدَرِّس", "يَتَقَابَل", "يُسَاعِد"], "Measure V: learn.", tr="My brother learns Arabic."),
    ],
    verify=vw("كَتَبَ", "يَكْتُب", "دَرَّسَ", "يُدَرِّس", "سَاعَدَ", "يُسَاعِد", "تَعَلَّمَ", "يَتَعَلَّم", "تَقَابَلَ", "يَتَقَابَل", "رِسَالَة", "الْمَطْبَخ", "تَكَلَّمَتْ", "تُدَرِّس",
              "تَدْرُس", "تَتَعَلَّم", "تُسَاعِد", "الْمَكْتَب", "الْكُتُب"),
)

# ---------------------------------------------------------------------------- 170
L170 = lesson(
    "Last weekend",
    "ذَهَبْنَا · رَكِبْنَا · سَبَحْنَا · رَجَعْنَا",
    requires=["أسبوع", "ذهب", "ركب", "سبح", "رجع", "لعب"],
    cards=[
        card("Telling the story in order",
             "Use the past tense for what happened and small words to put the events in order. The weekend is نِهَايَة "
             "الْأُسْبُوع (“the end of the week”).",
             tables=[table(["English", "Arabic"],
                           [["last weekend", "فِي نِهَايَة الْأُسْبُوع الْمَاضِي"], ["first", "أَوَّلًا"], ["then", "ثُمَّ"],
                            ["after that", "بَعْدَهَا"], ["finally", "أَخِيرًا"], ["on Saturday", "يَوْم السَّبْت"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A story in the past",
             "The verbs about what we did are in the past tense with ـنَا (“we”).",
             examples=[
                 ex("فِي نِهَايَة الْأُسْبُوع الْمَاضِي ذَهَبْنَا إِلَى الْبَحْر.", "Last weekend we went to the sea.", "ذَهَبْنَا"),
                 ex("أَوَّلًا رَكِبْنَا الْحَافِلَة إِلَى الشَّاطِئ.", "First we took the bus to the beach.", "رَكِبْنَا"),
                 ex("ثُمَّ سَبَحْنَا وَلَعِبْنَا كُرَة الْقَدَم.", "Then we swam and played football.", "سَبَحْنَا"),
                 ex("بَعْدَهَا تَغَدَّيْنَا فِي مَطْعَم صَغِير.", "After that we had lunch in a small restaurant.", "بَعْدَهَا"),
                 ex("أَخِيرًا رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة التَّاسِعَة.", "Finally we went home at nine o’clock.", "أَخِيرًا"),
                 ex("كَانَ الْجَوّ جَمِيلًا يَوْم السَّبْت.", "The weather was nice on Saturday.", "كَانَ الْجَوّ جَمِيلًا"),
             ]),
    ],
    exercises=[
        M("What does نِهَايَة الْأُسْبُوع mean?", "the weekend", ["the week", "the end of the month", "the holiday"], "“The end of the week”."),
        M("Which word means “first” in a story?", "أَوَّلًا", ["أَخِيرًا", "بَعْدَهَا", "غَدًا"], "أَوَّلًا = first."),
        M("Which word means “finally”?", "أَخِيرًا", ["أَوَّلًا", "ثُمَّ", "أَمْس"], "أَخِيرًا = finally."),
        M("Which means “we went”?", "ذَهَبْنَا", ["ذَهَبْتُ", "نَذْهَب", "ذَهَبَ"], "ـنَا = we (past)."),
        M("Which means “we swam”?", "سَبَحْنَا", ["أَسْبَح", "سَبَحْتُ", "سَبَحَ"], "سَبَحَ + ـنَا."),
        M("Which means “First we took the bus to the beach”?", "أَوَّلًا رَكِبْنَا الْحَافِلَة إِلَى الشَّاطِئ", ["أَوَّلًا رَكِبْتُ الْحَافِلَة إِلَى الشَّاطِئ", "أَخِيرًا رَكِبْنَا الْحَافِلَة إِلَى الشَّاطِئ", "أَوَّلًا نَرْكَب الْحَافِلَة إِلَى الشَّاطِئ"], "رَكِبْنَا = we rode."),
        M("Which means “Finally we went home at nine”?", "أَخِيرًا رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة التَّاسِعَة", ["أَخِيرًا رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة الثَّامِنَة", "أَوَّلًا رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة التَّاسِعَة", "أَخِيرًا سَنَرْجِع إِلَى الْبَيْت فِي السَّاعَة التَّاسِعَة"], "التَّاسِعَة = ninth."),
        F("___ رَكِبْنَا الْحَافِلَة إِلَى الشَّاطِئ.", "أَوَّلًا", ["أَخِيرًا", "غَدًا", "لَنْ"], "The first step of the story.", tr="First we took the bus to the beach."),
        F("ثُمَّ ___ وَلَعِبْنَا كُرَة الْقَدَم.", "سَبَحْنَا", ["أَسْبَح", "سَبَحَ", "يَسْبَحُون"], "Past, we.", tr="Then we swam and played football."),
    ],
    verify=vv("ذهب", "past", nahnu="ذَهَبْنَا") + vv("ركب", "past", nahnu="رَكِبْنَا") + vv("سبح", "past", nahnu="سَبَحْنَا") + vv("لعب", "past", nahnu="لَعِبْنَا")
    + vv("رجع", "past", nahnu="رَجَعْنَا")
    + vw("نِهَايَة", "الْمَاضِي", "أَوَّلًا", "ثُمَّ", "بَعْدَهَا", "أَخِيرًا", "تَغَدَّيْنَا", "الْحَافِلَة", "الشَّاطِئ", "السَّبْت", "ذَهَبْتُ", "سَبَحْتُ", "رَكِبْتُ", "أَسْبَح", "نَرْكَب"),
)

# ---------------------------------------------------------------------------- 171
L171 = lesson(
    "Visiting places: زَارَ",
    "زُرْنَا الْمُتْحَف · أَزُور السُّوق",
    requires=["زار", "متحف", "سوق", "قلعة", "مدينة", "قديم"],
    cards=[
        card("Visit",
             "The verb زَارَ (“to visit”) has a long ā in the middle. In the past, when an ending like ـتُ or ـنَا is added, "
             "the long vowel becomes short: زُرْتُ, زُرْنَا. In the present it has a long ū: أَزُور. The place comes "
             "straight after the verb, with no preposition.",
             tables=[table(["Person", "Past", "Present"],
                           [["I", "زُرْتُ", "أَزُور"], ["we", "زُرْنَا", "نَزُور"], ["you (to a man)", "زُرْتَ", "تَزُور"],
                            ["you (to a woman)", "زُرْتِ", "تَزُورِين"], ["he", "زَارَ", "يَزُور"], ["she", "زَارَتْ", "تَزُور"],
                            ["they (men)", "زَارُوا", "يَزُورُون"]],
                           say=[1, 2], tlit=[1, 2], gloss=False),
                     table(["English", "Arabic"],
                           [["museum", "الْمُتْحَف"], ["castle", "الْقَلْعَة"], ["market", "السُّوق"],
                            ["the old city", "الْمَدِينَة الْقَدِيمَة"], ["port", "الْمِينَاء"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Use زَارَ for places and for people.",
             examples=[
                 ex("زُرْنَا الْمُتْحَف يَوْم السَّبْت.", "We visited the museum on Saturday.", "زُرْنَا"),
                 ex("زُرْتُ الْقَلْعَة مَعَ أُسْرَتِي.", "I visited the castle with my family.", "زُرْتُ"),
                 ex("هَلْ زُرْتَ الْمَدِينَة الْقَدِيمَة؟", "Have you visited the old city? (to a man)", "زُرْتَ"),
                 ex("نَزُور السُّوق كُلّ أُسْبُوع.", "We visit the market every week.", "نَزُور"),
                 ex("سَأَزُور جَدِّي غَدًا.", "I will visit my grandfather tomorrow.", "سَأَزُور"),
                 ex("زَارَتْ أُخْتِي الْمِينَاء أَمْس.", "My sister visited the port yesterday.", "زَارَتْ"),
             ]),
    ],
    exercises=[
        M("What does زَارَ mean?", "he visited", ["he saw", "he helped", "he travelled"], "زَارَ = to visit."),
        M("Which means “I visited”?", "زُرْتُ", ["أَزُور", "زَارَ", "زُرْنَا"], "The long vowel shortens before ـتُ."),
        M("Which means “we visit”?", "نَزُور", ["زُرْنَا", "أَزُور", "يَزُورُون"], "نَـ + ـزُور."),
        M("Which means “you (to a woman) visit”?", "تَزُورِين", ["تَزُور", "زُرْتِ", "يَزُورُون"], "The ـِين ending."),
        M("Which means “We visited the museum on Saturday”?", "زُرْنَا الْمُتْحَف يَوْم السَّبْت", ["نَزُور الْمُتْحَف يَوْم السَّبْت", "زُرْتُ الْمُتْحَف يَوْم السَّبْت", "زُرْنَا الْقَلْعَة يَوْم السَّبْت"], "زُرْنَا = we visited."),
        M("Which means “I will visit my grandfather tomorrow”?", "سَأَزُور جَدِّي غَدًا", ["زُرْتُ جَدِّي غَدًا", "لَنْ أَزُور جَدِّي غَدًا", "سَنَزُور جَدِّي غَدًا"], "سَـ + أَزُور."),
        M("Does زَارَ need a preposition before the place?", "No, the place follows directly", ["Yes, إِلَى", "Yes, فِي", "Yes, مِنْ"], "زَارَ الْمُتْحَف."),
        F("___ الْقَلْعَة مَعَ أُسْرَتِي.", "زُرْتُ", ["زَارَ", "أَزُور", "زُرْنَا"], "Past, I.", tr="I visited the castle with my family."),
        F("هَلْ ___ الْمَدِينَة الْقَدِيمَة؟ (to a man)", "زُرْتَ", ["زُرْتِ", "زُرْتُ", "زَارَتْ"], "Past, you (to a man).", tr="Have you visited the old city?"),
    ],
    verify=vw("زُرْتُ", "زُرْنَا", "زُرْتَ", "زُرْتِ", "زَارَ", "زَارَتْ", "زَارُوا", "أَزُور", "نَزُور", "تَزُور", "تَزُورِين", "يَزُور", "يَزُورُون", "سَأَزُور", "الْمُتْحَف", "الْقَلْعَة",
              "السُّوق", "الْمَدِينَة", "الْقَدِيمَة", "الْمِينَاء", "جَدِّي"),
)

# ---------------------------------------------------------------------------- 172
L172 = lesson(
    "Getting around",
    "بِالْقِطَار · بِالطَّائِرَة · نَزَلْنَا · وَصَلْنَا",
    requires=["سيارة", "قطار", "طائرة", "نزل", "وصل", "سافر", "ركب", "محطة"],
    cards=[
        card("Vehicles and places",
             "To say “by train”, use بِـ: بِالْقِطَار. A taxi is سَيَّارَة أُجْرَة, literally “a hired car”. The verbs "
             "رَكِبَ (to ride, to board), نَزَلَ (to get off), وَصَلَ إِلَى (to arrive at) and سَافَرَ (to travel) go with them.",
             tables=[table(["English", "Arabic"],
                           [["car", "السَّيَّارَة"], ["bus", "الْحَافِلَة"], ["train", "الْقِطَار"], ["plane", "الطَّائِرَة"],
                            ["taxi", "سَيَّارَة أُجْرَة"], ["bicycle", "الدَّرَّاجَة"], ["airport", "الْمَطَار"], ["station", "الْمَحَطَّة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Travelling",
             "Notice the prepositions: بِـ for the vehicle, إِلَى for the destination, مِنْ for where you left.",
             examples=[
                 ex("سَافَرْنَا بِالطَّائِرَة إِلَى الْأُرْدُنّ.", "We travelled by plane to Jordan.", "بِالطَّائِرَة"),
                 ex("أَذْهَب إِلَى الْمَدْرَسَة بِالْحَافِلَة.", "I go to school by bus.", "بِالْحَافِلَة"),
                 ex("رَكِبْتُ الْقِطَار فِي الْمَحَطَّة.", "I took the train at the station.", "رَكِبْتُ"),
                 ex("وَصَلْنَا إِلَى الْمَطَار فِي السَّاعَة الْخَامِسَة.", "We arrived at the airport at five o’clock.", "وَصَلْنَا"),
                 ex("نَزَلْنَا مِنَ الْحَافِلَة أَمَامَ الْمُتْحَف.", "We got off the bus in front of the museum.", "نَزَلْنَا"),
                 ex("هَلْ تَذْهَب بِالسَّيَّارَة أَمْ بِالْقِطَار؟", "Are you going by car or by train? (to a man)", "بِالسَّيَّارَة"),
             ]),
    ],
    exercises=[
        M("What does الْحَافِلَة mean?", "the bus", ["the train", "the plane", "the car"], "حَافِلَة = bus."),
        M("What does سَيَّارَة أُجْرَة mean?", "taxi", ["bus", "bicycle", "train"], "“A hired car”."),
        M("Which means “by train”?", "بِالْقِطَار", ["فِي الْقِطَار الْمَحَطَّة", "إِلَى الْقِطَار", "مِنَ الْقِطَار"], "بِـ = by."),
        M("Which means “We travelled by plane”?", "سَافَرْنَا بِالطَّائِرَة", ["سَافَرْتُ بِالطَّائِرَة", "نُسَافِر بِالطَّائِرَة", "سَافَرْنَا بِالْقِطَار"], "ـنَا = we (past)."),
        M("Which means “We arrived at the airport”?", "وَصَلْنَا إِلَى الْمَطَار", ["وَصَلْنَا مِنَ الْمَطَار", "وَصَلْتُ إِلَى الْمَطَار", "نَزَلْنَا فِي الْمَطَار"], "وَصَلَ إِلَى."),
        M("Which means “We got off the bus”?", "نَزَلْنَا مِنَ الْحَافِلَة", ["رَكِبْنَا الْحَافِلَة", "نَزَلْتُ مِنَ الْحَافِلَة", "نَزَلْنَا إِلَى الْحَافِلَة"], "نَزَلَ مِنْ."),
        M("Which means “I took the train at the station”?", "رَكِبْتُ الْقِطَار فِي الْمَحَطَّة", ["رَكِبْنَا الْقِطَار فِي الْمَحَطَّة", "أَرْكَب الْقِطَار فِي الْمَحَطَّة", "رَكِبْتُ الْحَافِلَة فِي الْمَحَطَّة"], "رَكِبْتُ = I rode."),
        F("أَذْهَب إِلَى الْمَدْرَسَة ___الْحَافِلَة.", "بِ", ["إِلَى", "عَنْ", "مِنْ"], "“By”.", tr="I go to school by bus."),
        F("وَصَلْنَا ___ الْمَطَار فِي السَّاعَة الْخَامِسَة.", "إِلَى", ["مِنَ", "عَنِ", "بِ"], "Arrive at: وَصَلَ إِلَى.", tr="We arrived at the airport at five o’clock."),
    ],
    verify=vv("ركب", "past", ana="رَكِبْتُ") + vv("ركب", "pres", ana="أَرْكَب") + vv("نزل", "past", nahnu="نَزَلْنَا")
    + vw("الْحَافِلَة", "الْقِطَار", "الطَّائِرَة", "الدَّرَّاجَة", "الْمَطَار", "الْمَحَطَّة", "السَّيَّارَة", "سَافَرْنَا", "سَافَرْتُ", "نُسَافِر", "وَصَلْنَا", "وَصَلْتُ", "نَزَلْتُ", "الْمُتْحَف",
         "أُجْرَة", "رَكِبْنَا"),
)


# ---------------------------------------------------------------------------- 173
L173 = lesson(
    "If the weather is nice: إِذَا",
    "إِذَا كَانَ الْجَوّ جَمِيلًا فَسَنَذْهَب",
    requires=["إذا", "جو", "مطر", "شمس", "حار", "بارد"],
    cards=[
        card("إِذَا + كَانَ",
             "إِذَا means “if” (or “when”) for something that may well happen. After إِذَا the verb is usually in the PAST tense, "
             "even though the sentence is about the future (for “if … not”, use إِذَا لَمْ يَكُنِ …). The second part of the sentence often starts with فَـ (“then”) and has سَـ or the present: فَسَنَذْهَب. "
             "Remember that the predicate of كَانَ takes ـًا.",
             tables=[table(["English", "Arabic"],
                           [["sunny", "مُشْمِس"], ["rainy", "مُمْطِر"], ["hot", "حَارّ"], ["cold", "بَارِد"], ["nice", "جَمِيل"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("إِذَا كَانَ الْجَوّ جَمِيلًا غَدًا فَسَنَذْهَب إِلَى الشَّاطِئ.", "If the weather is nice tomorrow, we will go to the beach.", "إِذَا كَانَ الْجَوّ جَمِيلًا"),
                 ex("إِذَا كَانَ الْجَوّ حَارًّا فَسَأَسْبَح فِي الْمَسْبَح.", "If the weather is hot, I will swim in the pool.", "حَارًّا"),
                 ex("إِذَا كَانَ الْجَوّ مُمْطِرًا فَسَنُشَاهِد فِيلْم فِي الْبَيْت.", "If the weather is rainy, we will watch a film at home.", "مُمْطِرًا"),
                 ex("إِذَا كَانَ عِنْدِي وَقْت فَسَأُرَافِقُكَ إِلَى السُّوق.", "If I have time, I will go with you to the market. (to a man)", "إِذَا كَانَ عِنْدِي وَقْت"),
                 ex("إِذَا لَمْ يَكُنِ الْجَوّ بَارِدًا فَسَنَلْعَب فِي الْحَدِيقَة.", "If the weather is not cold, we will play in the park.", "إِذَا لَمْ يَكُنِ"),
                 ex("كَيْفَ سَيَكُون الْجَوّ غَدًا؟", "What will the weather be like tomorrow?", "كَيْفَ سَيَكُون"),
             ]),
    ],
    exercises=[
        M("What does إِذَا mean?", "if", ["because", "but", "when (a question)"], "إِذَا introduces a condition."),
        M("What does مُمْطِر mean?", "rainy", ["sunny", "cold", "hot"], "مَطَر = rain."),
        M("What does مُشْمِس mean?", "sunny", ["rainy", "cold", "nice"], "شَمْس = sun."),
        M("Which tense follows إِذَا in the first half?", "the past (كَانَ)", ["the present", "the future with سَـ", "a command"], "إِذَا كَانَ …"),
        M("Which means “If the weather is nice tomorrow, we will go to the beach”?", "إِذَا كَانَ الْجَوّ جَمِيلًا غَدًا فَسَنَذْهَب إِلَى الشَّاطِئ", ["إِذَا يَكُون الْجَوّ جَمِيلًا غَدًا فَسَنَذْهَب إِلَى الشَّاطِئ", "إِذَا كَانَ الْجَوّ جَمِيلًا غَدًا فَسَيَذْهَبُون إِلَى الشَّاطِئ", "إِذَا كَانَ الْجَوّ بَارِدًا غَدًا فَسَنَذْهَب إِلَى الشَّاطِئ"], "إِذَا كَانَ … سَنَذْهَب."),
        M("Which means “If the weather is rainy, we will watch a film at home”?", "إِذَا كَانَ الْجَوّ مُمْطِرًا فَسَنُشَاهِد فِيلْم فِي الْبَيْت", ["إِذَا كَانَ الْجَوّ مُشْمِسًا فَسَنُشَاهِد فِيلْم فِي الْبَيْت", "إِذَا كَانَ الْجَوّ مُمْطِرًا فَسَيُشَاهِدُون فِيلْم فِي الْبَيْت", "إِذَا كَانَ الْجَوّ مُمْطِرًا فَلَنْ نُشَاهِد فِيلْم فِي الْبَيْت"], "مُمْطِر = rainy."),
        M("Which means “If the weather is not cold”?", "إِذَا لَمْ يَكُنِ الْجَوّ بَارِدًا", ["إِذَا لَنْ يَكُنِ الْجَوّ بَارِدًا", "إِذَا كَانَ الْجَوّ بَارِدًا", "إِذَا لَا يَكُون الْجَوّ بَارِدًا"], "After إِذَا, لَمْ يَكُنْ = is not."),
        F("إِذَا ___ الْجَوّ حَارًّا فَسَأَسْبَح فِي الْمَسْبَح.", "كَانَ", ["يَكُون", "سَيَكُون", "كُنْ"], "The past tense after إِذَا.", tr="If the weather is hot, I will swim in the pool."),
        F("إِذَا كَانَ الْجَوّ ___ فَسَنُشَاهِد فِيلْم فِي الْبَيْت.", "مُمْطِرًا", ["مُمْطِر", "الْمُمْطِر", "مُشْمِسًا"], "The predicate of كَانَ takes ـًا.", tr="If the weather is rainy, we will watch a film at home."),
    ],
    verify=vv("سبح", "fut", ana="سَأَسْبَح") + vv("لعب", "fut", nahnu="سَنَلْعَب") + vv("ذهب", "fut", nahnu="سَنَذْهَب")
    + vw("إِذَا", "مُمْطِر", "مُمْطِرًا", "مُشْمِس", "مُشْمِسًا", "حَارًّا", "بَارِدًا", "جَمِيلًا", "سَنُشَاهِد", "سَأُرَافِقُكَ", "يَكُنِ", "الْمَسْبَح", "الْحَدِيقَة", "كَيْفَ", "يَكُون", "سَيَكُون", "كُنْ"),
)

# ---------------------------------------------------------------------------- 174
L174 = lesson(
    "Sightseeing and photos",
    "صَوَّرْتُ · الْمَنْظَر · الْجَبَل · الصُّوَر",
    requires=["صور", "منظر", "جبل", "نهر", "قديم", "صحراء"],
    cards=[
        card("What there is to see",
             "On a trip you look at views and take photographs. صَوَّرَ is Measure II: its present is أُصَوِّر, "
             "and a photo is صُورَة (plural صُوَر). Add an ending for “it”: صَوَّرَهَا (he photographed her or it).",
             tables=[table(["English", "Arabic"],
                           [["view", "الْمَنْظَر"], ["mountain", "الْجَبَل"], ["river", "النَّهْر"], ["desert", "الصَّحْرَاء"],
                            ["photo", "الصُّورَة"], ["photos", "الصُّوَر"], ["old", "قَدِيم"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Describing a visit",
             "Past verbs tell what you did, and كَانَ tells what it was like.",
             examples=[
                 ex("صَوَّرْتُ الْقَلْعَة وَالْمَدِينَة الْقَدِيمَة.", "I photographed the castle and the old city.", "صَوَّرْتُ"),
                 ex("كَانَ الْمَنْظَر جَمِيلًا جِدًّا.", "The view was very beautiful.", "الْمَنْظَر"),
                 ex("هَلْ يُمْكِنُنِي أَنْ أُصَوِّر هُنَا؟", "May I take photos here?", "أُصَوِّر"),
                 ex("الصُّورَة جَمِيلَة. مَنْ صَوَّرَهَا؟", "The photo is nice. Who took it?", "صَوَّرَهَا"),
                 ex("الْجَبَل كَبِير وَالنَّهْر طَوِيل.", "The mountain is big and the river is long.", "الْجَبَل"),
                 ex("الصَّحْرَاء كَبِيرَة وَالْجَوّ فِيهَا حَارّ.", "The desert is big and the weather in it is hot.", "الصَّحْرَاء"),
             ]),
    ],
    exercises=[
        M("What does الْمَنْظَر mean?", "the view", ["the photo", "the mountain", "the river"], "مَنْظَر = view."),
        M("What does الصَّحْرَاء mean?", "the desert", ["the sea", "the river", "the mountain"], "صَحْرَاء = desert."),
        M("What does صَوَّرْتُ mean?", "I photographed", ["I visited", "I travelled", "I watched"], "صَوَّرَ = to photograph."),
        M("Which means “May I take photos here?”", "هَلْ يُمْكِنُنِي أَنْ أُصَوِّر هُنَا؟", ["هَلْ يُمْكِنُكَ أَنْ تُصَوِّر هُنَا؟", "هَلْ صَوَّرْتُ هُنَا؟", "هَلْ يُمْكِنُنِي أَنْ أُسَافِر هُنَا؟"], "أُصَوِّر = I photograph."),
        M("Which means “Who took it?” (a photo)", "مَنْ صَوَّرَهَا؟", ["مَنْ صَوَّرَهُ؟", "مَنْ يُصَوِّرُهَا؟", "مَاذَا صَوَّرَهَا؟"], "ـهَا = it (feminine): صُورَة is feminine."),
        M("Which means “The view was very beautiful”?", "كَانَ الْمَنْظَر جَمِيلًا جِدًّا", ["الْمَنْظَر جَمِيل جِدًّا غَدًا", "كَانَ الْمَنْظَر قَدِيمًا", "كَانَتِ الصُّورَة جَمِيلَةً جِدًّا"], "كَانَ + a predicate with ـًا."),
        M("Which means “I photographed the castle”?", "صَوَّرْتُ الْقَلْعَة", ["أُصَوِّر الْقَلْعَة", "زُرْتُ الْقَلْعَة", "صَوَّرْنَا الْقَلْعَة"], "ـتُ = I (past)."),
        F("___ الْمَنْظَر جَمِيلًا جِدًّا.", "كَانَ", ["يَكُون", "لَنْ", "كُنْ"], "Past.", tr="The view was very beautiful."),
        F("الصُّورَة جَمِيلَة. مَنْ ___؟", "صَوَّرَهَا", ["صَوَّرَهُ", "تُصَوِّر", "صُورَة"], "“It” = the photo (feminine).", tr="The photo is nice. Who took it?"),
    ],
    verify=vw("صَوَّرْتُ", "صَوَّرَ", "أُصَوِّر", "صَوَّرَهَا", "صَوَّرَهُ", "الصُّورَة", "الصُّوَر", "الْمَنْظَر", "الْجَبَل", "النَّهْر", "الصَّحْرَاء", "فِيهَا", "يُصَوِّرُهَا", "تُصَوِّر",
              "يُمْكِنُكَ", "كَانَتِ", "الْقَلْعَة", "جَمِيلَةً"),
)

# ---------------------------------------------------------------------------- 175
L175 = lesson(
    "Making suggestions",
    "هَيَّا نَذْهَب · لِمَاذَا لَا نَزُور؟ · أَقْتَرِح أَنْ",
    requires=["هيا", "لماذا", "رأي", "ذهب", "زار", "ركب"],
    cards=[
        card("Ways to suggest",
             "To suggest something to a friend, use هَيَّا (“come on”) and a verb with نَـ (“we”), or ask لِمَاذَا لَا نَـ… "
             "(“why don’t we…?”), or say أَقْتَرِح أَنْ (“I suggest that”). Ask for an opinion with مَا رَأْيُكَ؟ (to a man) or "
             "مَا رَأْيُكِ؟ (to a woman).",
             tables=[table(["English", "Arabic"],
                           [["Let’s go!", "هَيَّا نَذْهَب"], ["Why don’t we visit…?", "لِمَاذَا لَا نَزُور…؟"],
                            ["Shall we play?", "هَلْ نَلْعَب؟"], ["I suggest that we go", "أَقْتَرِح أَنْ نَذْهَب"],
                            ["What do you think? (to a man)", "مَا رَأْيُكَ؟"], ["What do you think? (to a woman)", "مَا رَأْيُكِ؟"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "After أَنْ the verb takes the shortened endings you know.",
             examples=[
                 ex("هَيَّا نَذْهَب إِلَى الشَّاطِئ!", "Let’s go to the beach!", "هَيَّا نَذْهَب"),
                 ex("لِمَاذَا لَا نَزُور الْمُتْحَف؟", "Why don’t we visit the museum?", "لِمَاذَا لَا نَزُور"),
                 ex("أَقْتَرِح أَنْ نَرْكَب الْقِطَار.", "I suggest that we take the train.", "أَقْتَرِح أَنْ"),
                 ex("هَلْ نَلْعَب كُرَة الْقَدَم؟", "Shall we play football?", "هَلْ نَلْعَب"),
                 ex("مَا رَأْيُكَ فِي هَذِه الْفِكْرَة؟", "What do you think of this idea? (to a man)", "مَا رَأْيُكَ"),
                 ex("أَقْتَرِح أَنْ تَذْهَبُوا بِالْحَافِلَة.", "I suggest that you (all) go by bus.", "تَذْهَبُوا"),
             ]),
    ],
    exercises=[
        M("What does هَيَّا نَذْهَب mean?", "Let’s go", ["I went", "Do not go", "They will go"], "هَيَّا = come on."),
        M("Which means “Why don’t we visit the museum?”", "لِمَاذَا لَا نَزُور الْمُتْحَف؟", ["لِمَاذَا لَا تَزُور الْمُتْحَف؟", "لِمَاذَا لَا أَزُور الْمُتْحَف؟", "لَنْ نَزُور الْمُتْحَف"], "نَـ = we."),
        M("Which means “I suggest that we take the train”?", "أَقْتَرِح أَنْ نَرْكَب الْقِطَار", ["أَقْتَرِح أَنْ أَرْكَب الْقِطَار", "اِقْتَرَحْنَا أَنْ نَرْكَب الْقِطَار", "أَقْتَرِح أَنْ يَرْكَبُوا الْقِطَار"], "أَقْتَرِح أَنْ + نَرْكَب."),
        M("Which asks a woman for her opinion?", "مَا رَأْيُكِ؟", ["مَا رَأْيُكَ؟", "مَا رَأْيِي؟", "مَا رَأْيُهُ؟"], "ـكِ = your (to a woman)."),
        M("Which asks a man for his opinion?", "مَا رَأْيُكَ؟", ["مَا رَأْيُكِ؟", "مَا رَأْيُهَا؟", "مَا رَأْيُنَا؟"], "ـكَ = your (to a man)."),
        M("Which means “Shall we play football?”", "هَلْ نَلْعَب كُرَة الْقَدَم؟", ["هَلْ لَعِبْنَا كُرَة الْقَدَم؟", "هَلْ أَلْعَب كُرَة الْقَدَم؟", "هَلْ تَلْعَب كُرَة الْقَدَم؟"], "هَلْ + نَلْعَب."),
        M("Which means “I suggest that you (all) go by bus”?", "أَقْتَرِح أَنْ تَذْهَبُوا بِالْحَافِلَة", ["أَقْتَرِح أَنْ تَذْهَبُون بِالْحَافِلَة", "أَقْتَرِح أَنْ تَذْهَب بِالْحَافِلَة", "أَقْتَرِح أَنْ يَذْهَبُوا بِالْحَافِلَة"], "After أَنْ the ن of ـُون falls away."),
        F("___ نَذْهَب إِلَى الشَّاطِئ!", "هَيَّا", ["لَنْ", "هَلْ", "إِذَا"], "“Come on”.", tr="Let’s go to the beach!"),
        F("أَقْتَرِح ___ نَرْكَب الْقِطَار.", "أَنْ", ["لَنْ", "إِذَا", "لِأَنَّ"], "“That” before a verb.", tr="I suggest that we take the train."),
    ],
    verify=vv("ذهب", "sub", hum="يَذْهَبُوا", antum="تَذْهَبُوا") + vv("ركب", "sub", nahnu="نَرْكَب")
    + vw("هَيَّا", "نَذْهَب", "لِمَاذَا", "نَزُور", "أَقْتَرِح", "اِقْتَرَحْنَا", "نَلْعَب", "رَأْيُكَ", "رَأْيُكِ", "رَأْيِي", "رَأْيُهُ", "رَأْيُهَا", "رَأْيُنَا", "لَعِبْنَا", "تَذْهَبُون"),
)

# ---------------------------------------------------------------------------- 176
L176 = lesson(
    "Agreeing and disagreeing",
    "أَنَا مُوَافِق · لَا أُوَافِق · أُفَضِّل أَنْ",
    requires=["موافق", "فكرة", "فضل", "بدل", "لكن", "رأي"],
    cards=[
        card("Saying yes, no and “rather”",
             "A man says أَنَا مُوَافِق and a woman أَنَا مُوَافِقَة. To say no, use لَا أُوَافِق, and give a reason. "
             "To say what you would prefer, use أُفَضِّل أَنْ and a verb. بَدَلًا مِنْ means “instead of”.",
             tables=[table(["English", "Arabic"],
                           [["I agree. (a man speaking)", "أَنَا مُوَافِق"], ["I agree. (a woman speaking)", "أَنَا مُوَافِقَة"],
                            ["I do not agree.", "لَا أُوَافِق"], ["I would rather we go", "أُفَضِّل أَنْ نَذْهَب"],
                            ["instead of…", "بَدَلًا مِنْ"], ["but", "لَكِنْ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A short exchange",
             "Two friends decide where to go.",
             examples=[
                 ex("هَيَّا نَذْهَب إِلَى الشَّاطِئ. مَا رَأْيُكَ؟", "Let’s go to the beach. What do you think? (to a man)", "مَا رَأْيُكَ"),
                 ex("لَا أُوَافِق. الْجَوّ بَارِد.", "I do not agree. The weather is cold.", "لَا أُوَافِق"),
                 ex("أُفَضِّل أَنْ نَزُور الْمُتْحَف.", "I would rather we visit the museum.", "أُفَضِّل أَنْ"),
                 ex("أَنَا مُوَافِق، فِكْرَة جَيِّدَة.", "I agree, good idea. (a man speaking)", "أَنَا مُوَافِق"),
                 ex("بَدَلًا مِنَ الشَّاطِئ نَزُور الْقَلْعَة.", "Instead of the beach, we’ll visit the castle.", "بَدَلًا مِنَ"),
                 ex("أَنَا مُوَافِقَة، لَكِنْ لَنْ أَسْبَح.", "I agree, but I will not swim. (a woman speaking)", "مُوَافِقَة"),
             ]),
    ],
    exercises=[
        M("Which does a woman say to agree?", "أَنَا مُوَافِقَة", ["أَنَا مُوَافِق", "لَا أُوَافِق", "أَنَا آسِف"], "The feminine adds ـَة."),
        M("Which does a man say to agree?", "أَنَا مُوَافِق", ["أَنَا مُوَافِقَة", "لَا أُوَافِق", "لَنْ أُوَافِق"], "Masculine: no ـَة."),
        M("What does لَا أُوَافِق mean?", "I do not agree", ["I will agree", "I agreed", "I suggest"], "لَا + present."),
        M("What does بَدَلًا مِنْ mean?", "instead of", ["because of", "after", "with"], "بَدَل = replacement."),
        M("Which means “I would rather we visit the museum”?", "أُفَضِّل أَنْ نَزُور الْمُتْحَف", ["أُفَضِّل أَنْ أَزُور الْمُتْحَف", "أُفَضِّل الْمُتْحَف عَلَى نَزُور", "زُرْنَا الْمُتْحَف"], "أُفَضِّل أَنْ + نَزُور."),
        M("Which means “I do not agree. The weather is cold”?", "لَا أُوَافِق. الْجَوّ بَارِد", ["لَا أُوَافِق. كَانَ الْجَوّ بَارِدًا", "أَنَا مُوَافِق. الْجَوّ بَارِد", "لَنْ أُوَافِق. الْجَوّ حَارّ"], "لَا أُوَافِق + a reason."),
        M("Which means “Instead of the beach, we’ll visit the castle”?", "بَدَلًا مِنَ الشَّاطِئ نَزُور الْقَلْعَة", ["بَدَلًا مِنَ الْقَلْعَة نَزُور الشَّاطِئ", "بَعْدَ الشَّاطِئ نَزُور الْقَلْعَة", "بَدَلًا مِنَ الشَّاطِئ زُرْنَا الْقَلْعَة"], "بَدَلًا مِنَ الشَّاطِئ."),
        F("___ مُوَافِقَة، لَكِنْ لَنْ أَسْبَح. (a woman speaking)", "أَنَا", ["هُوَ", "أَنْتَ", "نَحْنُ"], "The speaker is a woman.", tr="I agree, but I will not swim."),
        F("لَا ___. الْجَوّ بَارِد.", "أُوَافِق", ["مُوَافِق", "وَافَقْتُ", "أَقْتَرِح"], "لَا + present.", tr="I do not agree. The weather is cold."),
    ],
    verify=vv("سبح", "sub", ana="أَسْبَح") + vw("مُوَافِق", "مُوَافِقَة", "أُوَافِق", "بَدَلًا", "وَافَقْتُ", "أَقْتَرِح", "نَزُور", "أَسْبَح", "آسِف"),
)


# ---------------------------------------------------------------------------- 177
L177 = lesson(
    "A trip report",
    "زُرْنَا · صَوَّرْتُ · شَرِبْنَا · رَجَعْنَا",
    requires=["زار", "مدينة", "صور", "جو", "رجع", "شرب"],
    cards=[
        card("What I did on Saturday",
             "Read this short report about a day trip. It uses places, transport, weather and the past tense together.",
             examples=[
                 ex("فِي يَوْم السَّبْت زُرْنَا الْمَدِينَة الْقَدِيمَة وَذَهَبْنَا بِالْحَافِلَة.", "On Saturday we visited the old city and went by bus."),
                 ex("كَانَ الْجَوّ حَارًّا، فَشَرِبْنَا الشَّايْ بِالنَّعْنَاع.", "The weather was hot, so we drank tea with mint."),
                 ex("صَوَّرْتُ الْقَلْعَة وَالْمَنْظَر مِنَ الْجَبَل.", "I photographed the castle and the view from the mountain."),
                 ex("قَابَلْتُ أَصْدِقَائِي أَمَامَ الْمُتْحَف.", "I met my friends in front of the museum."),
                 ex("رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة الثَّامِنَة مَسَاءً.", "We went back home at eight in the evening."),
                 ex("كَانَ يَوْمًا جَمِيلًا جِدًّا.", "It was a very nice day.", "يَوْمًا"),
             ]),
    ],
    exercises=[
        M("How did they travel to the old city?", "by bus", ["by train", "by plane", "by bicycle"], "ذَهَبْنَا بِالْحَافِلَة."),
        M("What was the weather like?", "hot", ["cold", "rainy", "snowy"], "كَانَ الْجَوّ حَارًّا."),
        M("What did they drink?", "tea with mint", ["coffee", "water", "juice"], "الشَّايْ بِالنَّعْنَاع."),
        M("Which means “I photographed the castle”?", "صَوَّرْتُ الْقَلْعَة", ["زُرْتُ الْقَلْعَة", "صَوَّرْنَا الْقَلْعَة", "أُصَوِّر الْقَلْعَة"], "صَوَّرْتُ."),
        M("Which means “I met my friends in front of the museum”?", "قَابَلْتُ أَصْدِقَائِي أَمَامَ الْمُتْحَف", ["قَابَلْنَا أَصْدِقَائِي أَمَامَ الْمُتْحَف", "أُقَابِل أَصْدِقَائِي أَمَامَ الْمُتْحَف", "قَابَلْتُ أَصْدِقَائِي خَلْفَ الْمُتْحَف"], "قَابَلْتُ."),
        M("Which means “We went back home at eight in the evening”?", "رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة الثَّامِنَة مَسَاءً", ["رَجَعْنَا إِلَى الْبَيْت فِي السَّاعَة الثَّامِنَة صَبَاحًا", "سَنَرْجِع إِلَى الْبَيْت فِي السَّاعَة الثَّامِنَة مَسَاءً", "رَجَعْتُ إِلَى الْبَيْت فِي السَّاعَة الثَّامِنَة مَسَاءً"], "مَسَاءً = in the evening."),
        M("Which means “It was a very nice day”?", "كَانَ يَوْمًا جَمِيلًا جِدًّا", ["يَكُون يَوْمًا جَمِيلًا جِدًّا", "كَانَ يَوْمًا جَمِيلًا غَدًا", "سَيَكُون يَوْمًا جَمِيلًا جِدًّا"], "كَانَ … جَمِيلًا."),
        F("كَانَ الْجَوّ حَارًّا، ___شَرِبْنَا الشَّايْ بِالنَّعْنَاع.", "فَ", ["لَنْ", "إِذَا", "أَمْ"], "“So”.", tr="The weather was hot, so we drank tea with mint."),
        F("قَابَلْتُ ___ أَمَامَ الْمُتْحَف.", "أَصْدِقَائِي", ["أَصْدِقَاءُ", "صَدِيقِي", "الْأَصْدِقَاء"], "“My friends”.", tr="I met my friends in front of the museum."),
    ],
    verify=vv("شرب", "past", nahnu="شَرِبْنَا") + vv("رجع", "past", nahnu="رَجَعْنَا") + vv("ذهب", "past", nahnu="ذَهَبْنَا")
    + vw("زُرْنَا", "حَارًّا", "فَشَرِبْنَا", "النَّعْنَاع", "صَوَّرْتُ", "قَابَلْتُ", "أَصْدِقَائِي", "يَوْمًا", "جَمِيلًا", "الْمَدِينَة", "الْقَدِيمَة", "الْحَافِلَة", "الْجَبَل", "الْمُتْحَف", "قَابَلْنَا",
         "سَيَكُون", "صَدِيقِي", "أَصْدِقَاءُ", "الْأَصْدِقَاء"),
)

# ---------------------------------------------------------------------------- 178
L178 = lesson(
    "Planning next weekend",
    "سَنُسَافِر · سَأَحْجِز · لَنْ نَرْكَب الطَّائِرَة",
    requires=["أسبوع", "سافر", "حجز", "قطار", "فندق", "صباح"],
    cards=[
        card("A plan with conditions",
             "A plan combines the future with سَـ, لَنْ for what you will not do, يَجِب أَنْ for what you must do, and إِذَا "
             "for what depends on the weather.",
             examples=[
                 ex("فِي نِهَايَة الْأُسْبُوع الْقَادِم سَنُسَافِر إِلَى الشَّاطِئ.", "Next weekend we will travel to the beach.", "سَنُسَافِر"),
                 ex("لَنْ نَرْكَب الطَّائِرَة، سَنَذْهَب بِالْقِطَار.", "We will not take the plane, we will go by train.", "لَنْ نَرْكَب"),
                 ex("يَجِب أَنْ أَحْجِز الْفُنْدُق غَدًا.", "I must book the hotel tomorrow.", "يَجِب أَنْ أَحْجِز"),
                 ex("أَقْتَرِح أَنْ نَتَقَابَل فِي الْمَحَطَّة فِي السَّاعَة السَّابِعَة صَبَاحًا.", "I suggest that we meet at the station at seven in the morning.", "نَتَقَابَل"),
                 ex("إِذَا كَانَ الْجَوّ جَمِيلًا فَسَنَسْبَح فِي الْبَحْر.", "If the weather is nice we will swim in the sea.", "إِذَا كَانَ"),
                 ex("سَأُصَوِّر الْمَنْظَر وَسَأَكْتُب رِسَالَة إِلَى أُسْرَتِي.", "I will photograph the view and write a letter to my family.", "سَأُصَوِّر"),
             ]),
    ],
    exercises=[
        M("Which means “Next weekend we will travel to the beach”?", "فِي نِهَايَة الْأُسْبُوع الْقَادِم سَنُسَافِر إِلَى الشَّاطِئ", ["فِي نِهَايَة الْأُسْبُوع الْمَاضِي سَافَرْنَا إِلَى الشَّاطِئ", "فِي نِهَايَة الْأُسْبُوع الْقَادِم لَنْ نُسَافِر إِلَى الشَّاطِئ", "فِي نِهَايَة الْأُسْبُوع الْقَادِم سَأُسَافِر إِلَى الشَّاطِئ"], "سَـ + نُسَافِر."),
        M("Which means “We will not take the plane”?", "لَنْ نَرْكَب الطَّائِرَة", ["لَمْ نَرْكَب الطَّائِرَة", "سَنَرْكَب الطَّائِرَة", "لَنْ أَرْكَب الطَّائِرَة"], "لَنْ + نَرْكَب."),
        M("Which means “I must book the hotel tomorrow”?", "يَجِب أَنْ أَحْجِز الْفُنْدُق غَدًا", ["يَجِب أَنْ نَحْجِز الْفُنْدُق غَدًا", "حَجَزْتُ الْفُنْدُق غَدًا", "لَنْ أَحْجِز الْفُنْدُق غَدًا"], "يَجِب أَنْ + أَحْجِز."),
        M("Which means “I will photograph the view”?", "سَأُصَوِّر الْمَنْظَر", ["صَوَّرْتُ الْمَنْظَر", "لَنْ أُصَوِّر الْمَنْظَر", "سَنُصَوِّر الْمَنْظَر"], "سَـ + أُصَوِّر."),
        M("Which means “I suggest that we meet at the station at seven”?", "أَقْتَرِح أَنْ نَتَقَابَل فِي الْمَحَطَّة فِي السَّاعَة السَّابِعَة", ["أَقْتَرِح أَنْ نَتَقَابَل فِي الْمَطَار فِي السَّاعَة السَّابِعَة", "أَقْتَرِح أَنْ نَتَقَابَل فِي الْمَحَطَّة فِي السَّاعَة الثَّامِنَة", "تَقَابَلْنَا فِي الْمَحَطَّة فِي السَّاعَة السَّابِعَة"], "الْمَحَطَّة = station."),
        M("Which means “If the weather is nice we will swim in the sea”?", "إِذَا كَانَ الْجَوّ جَمِيلًا فَسَنَسْبَح فِي الْبَحْر", ["إِذَا كَانَ الْجَوّ جَمِيلًا فَسَيَسْبَحُون فِي الْبَحْر", "إِذَا لَمْ يَكُنِ الْجَوّ جَمِيلًا فَسَنَسْبَح فِي الْبَحْر", "إِذَا كَانَ الْجَوّ جَمِيلًا فَلَنْ نَسْبَح فِي الْبَحْر"], "إِذَا كَانَ … فَسَـ."),
        M("Which means “We will go by train”?", "سَنَذْهَب بِالْقِطَار", ["ذَهَبْنَا بِالْقِطَار", "لَنْ نَذْهَب بِالْقِطَار", "سَأَذْهَب بِالْقِطَار"], "سَـ + نَذْهَب."),
        F("لَنْ ___ الطَّائِرَة، سَنَذْهَب بِالْقِطَار.", "نَرْكَب", ["رَكِبْنَا", "تَرْكَبُون", "سَنَرْكَب"], "لَنْ + present.", tr="We will not take the plane, we will go by train."),
        F("يَجِب أَنْ ___ الْفُنْدُق غَدًا.", "أَحْجِز", ["حَجَزْتُ", "يَحْجِز", "حَجْز"], "يَجِب أَنْ + present.", tr="I must book the hotel tomorrow."),
    ],
    verify=vv("ركب", "sub", nahnu="نَرْكَب") + vv("سبح", "fut", nahnu="سَنَسْبَح") + vv("ذهب", "fut", nahnu="سَنَذْهَب") + vv("كتب", "fut", ana="سَأَكْتُب")
    + vw("سَنُسَافِر", "سَأُسَافِر", "نُسَافِر", "سَافَرْنَا", "الْفُنْدُق", "أَحْجِز", "نَحْجِز", "حَجَزْتُ", "يَحْجِز", "سَأُصَوِّر", "سَنُصَوِّر", "رِسَالَة", "الْمَحَطَّة", "الْمَطَار",
         "الطَّائِرَة", "تَرْكَبُون", "سَنَرْكَب", "رَكِبْنَا"),
)

# ---------------------------------------------------------------------------- 179
L179 = lesson(
    "Review: places, transport and the past",
    "زُرْنَا · رَكِبْنَا · وَصَلْنَا · قَابَلْنَا",
    requires=["زار", "ركب", "وصل", "قابل", "متحف", "قطار"],
    cards=[
        card("Two friends compare their weekends",
             "Huda and Yusuf talk about what they did.",
             examples=[
                 ex("مَاذَا فَعَلْتِ فِي نِهَايَة الْأُسْبُوع يَا هُدَى؟", "What did you do at the weekend, Huda? (to a woman)"),
                 ex("زُرْتُ الْمُتْحَف مَعَ أَصْدِقَائِي، ثُمَّ تَغَدَّيْنَا فِي السُّوق.", "I visited the museum with my friends, then we had lunch at the market."),
                 ex("كَيْفَ ذَهَبْتُمْ؟", "How did you (all) go?"),
                 ex("رَكِبْنَا الْقِطَار، وَوَصَلْنَا فِي السَّاعَة الْعَاشِرَة.", "We took the train, and we arrived at ten o’clock."),
                 ex("وَأَنْتَ يَا يُوسُف؟ هَلْ شَاهَدْتَ الْمُبَارَاة؟", "And you, Yusuf? Did you watch the match? (to a man)"),
                 ex("نَعَمْ، شَاهَدْتُ الْمُبَارَاة فِي النَّادِي وَتَقَابَلْنَا بَعْدَهَا.", "Yes, I watched the match at the club and we met afterwards."),
             ]),
    ],
    exercises=[
        M("Which asks Huda “What did you do?” (to a woman)", "مَاذَا فَعَلْتِ؟", ["مَاذَا فَعَلْتَ؟", "مَاذَا تَفْعَلِين؟", "مَاذَا سَتَفْعَلِين؟"], "ـتِ = you (to a woman), past."),
        M("Which means “I visited the museum with my friends”?", "زُرْتُ الْمُتْحَف مَعَ أَصْدِقَائِي", ["زُرْنَا الْمُتْحَف مَعَ أَصْدِقَائِي", "أَزُور الْمُتْحَف مَعَ أَصْدِقَائِي", "زَارَ الْمُتْحَف مَعَ أَصْدِقَائِي"], "زُرْتُ = I visited."),
        M("Which means “We took the train”?", "رَكِبْنَا الْقِطَار", ["رَكِبْتُ الْقِطَار", "نَرْكَب الْقِطَار", "نَزَلْنَا مِنَ الْقِطَار"], "رَكِبْنَا = we rode."),
        M("Which means “we arrived”?", "وَصَلْنَا", ["وَصَلْتُ", "نَصِل", "نَزَلْنَا"], "وَصَلَ + ـنَا."),
        M("Which asks a group “How did you go?”", "كَيْفَ ذَهَبْتُمْ؟", ["كَيْفَ ذَهَبْتَ؟", "كَيْفَ ذَهَبْنَا؟", "كَيْفَ تَذْهَبُون؟"], "ـتُمْ = you (all), past."),
        M("Which means “Did you watch the match?” (to a man)", "هَلْ شَاهَدْتَ الْمُبَارَاة؟", ["هَلْ شَاهَدْتِ الْمُبَارَاة؟", "هَلْ شَاهَدْتُ الْمُبَارَاة؟", "هَلْ تُشَاهِد الْمُبَارَاة؟"], "ـتَ = you (to a man)."),
        M("Which means “we met afterwards”?", "تَقَابَلْنَا بَعْدَهَا", ["قَابَلْتُ بَعْدَهَا", "نَتَقَابَل بَعْدَهَا", "تَقَابَلْنَا قَبْلَهَا"], "Measure VI past, we."),
        F("زُرْتُ الْمُتْحَف ثُمَّ ___ فِي السُّوق.", "تَغَدَّيْنَا", ["نَتَغَدَّى", "تَغَدَّيْتُ", "سَنَتَغَدَّى"], "Past, we.", tr="I visited the museum, then we had lunch at the market."),
        F("رَكِبْنَا الْقِطَار، ___ فِي السَّاعَة الْعَاشِرَة.", "وَوَصَلْنَا", ["وَنَصِل", "وَوَصَلْتُ", "وَنَزَلْنَا"], "Past, we.", tr="We took the train, and we arrived at ten o’clock."),
    ],
    verify=vv("فعل", "past", anti="فَعَلْتِ", anta="فَعَلْتَ") + vv("ذهب", "past", antum="ذَهَبْتُمْ", anta="ذَهَبْتَ", nahnu="ذَهَبْنَا")
    + vw("هُدَى", "يُوسُف", "زُرْتُ", "تَغَدَّيْنَا", "تَغَدَّيْتُ", "وَوَصَلْنَا", "وَصَلْتُ", "رَكِبْتُ", "نَزَلْنَا", "شَاهَدْتَ", "شَاهَدْتِ", "شَاهَدْتُ", "قَابَلْتُ", "قَبْلَهَا", "بَعْدَهَا",
         "تَفْعَلِين", "سَتَفْعَلِين", "تَذْهَبُون", "نَصِل", "وَنَصِل", "وَنَزَلْنَا", "وَوَصَلْتُ"),
)

# ---------------------------------------------------------------------------- 180
L180 = lesson(
    "Review: planning a weekend",
    "هَيَّا نَذْهَب · إِذَا كَانَ الْجَوّ جَمِيلًا · لَنْ أَسْبَح",
    requires=["هيا", "إذا", "جو", "ساعة", "أسبوع", "سبح"],
    cards=[
        card("Planning with a friend",
             "Hind and Karim decide what to do next weekend.",
             examples=[
                 ex("هَيَّا نَذْهَب إِلَى الشَّاطِئ فِي نِهَايَة الْأُسْبُوع الْقَادِم. مَا رَأْيُكَ يَا كَرِيم؟", "Let’s go to the beach next weekend. What do you think, Karim?"),
                 ex("أَنَا مُوَافِق، لَكِنْ إِذَا كَانَ الْجَوّ مُمْطِرًا فَلَنْ نَذْهَب.", "I agree, but if the weather is rainy, we will not go."),
                 ex("حَسَنًا، سَنَزُور الْمُتْحَف بَدَلًا مِنَ الشَّاطِئ.", "Fine, we will visit the museum instead of the beach."),
                 ex("أَقْتَرِح أَنْ نَتَقَابَل فِي الْمَحَطَّة فِي السَّاعَة التَّاسِعَة.", "I suggest that we meet at the station at nine."),
                 ex("وَيَجِب أَنْ أَحْجِز تَذْكِرَة الْقِطَار غَدًا.", "And I must book the train ticket tomorrow."),
                 ex("فِكْرَة جَيِّدَة. إِلَى اللِّقَاء!", "Good idea. See you!"),
             ]),
    ],
    exercises=[
        M("Which means “Let’s go to the beach”?", "هَيَّا نَذْهَب إِلَى الشَّاطِئ", ["سَنَذْهَب إِلَى الشَّاطِئ", "لَنْ نَذْهَب إِلَى الشَّاطِئ", "ذَهَبْنَا إِلَى الشَّاطِئ"], "هَيَّا + نَذْهَب."),
        M("Which means “if the weather is rainy”?", "إِذَا كَانَ الْجَوّ مُمْطِرًا", ["إِذَا يَكُون الْجَوّ مُمْطِرًا", "إِذَا كَانَ الْجَوّ مُمْطِر", "لَوْ كَانَ الْجَوّ مُشْمِسًا"], "إِذَا كَانَ … ـًا."),
        M("Which means “we will not go”?", "لَنْ نَذْهَب", ["لَمْ نَذْهَب", "لَا نَذْهَب", "سَنَذْهَب"], "لَنْ for the future."),
        M("Which means “we will visit the museum instead of the beach”?", "سَنَزُور الْمُتْحَف بَدَلًا مِنَ الشَّاطِئ", ["زُرْنَا الْمُتْحَف بَدَلًا مِنَ الشَّاطِئ", "سَنَزُور الشَّاطِئ بَدَلًا مِنَ الْمُتْحَف", "لَنْ نَزُور الْمُتْحَف بَدَلًا مِنَ الشَّاطِئ"], "بَدَلًا مِنَ = instead of."),
        M("Which means “I suggest that we meet at nine”?", "أَقْتَرِح أَنْ نَتَقَابَل فِي السَّاعَة التَّاسِعَة", ["أَقْتَرِح أَنْ أَتَقَابَل فِي السَّاعَة التَّاسِعَة", "تَقَابَلْنَا فِي السَّاعَة التَّاسِعَة", "أَقْتَرِح أَنْ نَتَقَابَل فِي السَّاعَة الثَّامِنَة"], "أَقْتَرِح أَنْ + نَتَقَابَل."),
        M("Which means “I must book the train ticket tomorrow”?", "يَجِب أَنْ أَحْجِز تَذْكِرَة الْقِطَار غَدًا", ["حَجَزْتُ الْقِطَار غَدًا", "لَنْ أَحْجِز تَذْكِرَة الْقِطَار غَدًا", "يَجِب أَنْ نَحْجِز الْقِطَار غَدًا"], "يَجِب أَنْ + أَحْجِز."),
        M("Which sentence is about the past?", "زُرْنَا الْمُتْحَف", ["سَنَزُور الْمُتْحَف", "لَنْ نَزُور الْمُتْحَف", "نَزُور الْمُتْحَف كُلّ أُسْبُوع"], "زُرْنَا = we visited."),
        F("أَنَا مُوَافِق، لَكِنْ إِذَا كَانَ الْجَوّ مُمْطِرًا فَ___ نَذْهَب.", "لَنْ", ["قَدْ", "هَيَّا", "إِلَى"], "A future negative.", tr="I agree, but if the weather is rainy, we will not go."),
        F("أَقْتَرِح ___ نَتَقَابَل فِي الْمَحَطَّة.", "أَنْ", ["لَنْ", "إِذَا", "ثُمَّ"], "“That” + a verb.", tr="I suggest that we meet at the station."),
    ],
    verify=vv("ذهب", "fut", nahnu="سَنَذْهَب") + vv("ذهب", "sub", nahnu="نَذْهَب") + vv("ذهب", "jus", nahnu="نَذْهَب")
    + vw("هَيَّا", "كَرِيم", "مُمْطِرًا", "مُشْمِسًا", "بَدَلًا", "الشَّاطِئ", "الْمُتْحَف", "الْمَحَطَّة", "اللِّقَاء", "حَسَنًا", "نَتَقَابَل", "أَتَقَابَل", "تَقَابَلْنَا", "سَنَزُور", "زُرْنَا",
         "أَحْجِز", "نَحْجِز", "حَجَزْتُ", "لَوْ", "نَزُور", "لَنْ"),
)

UNIT = unit("نِهَايَة الْأُسْبُوع: weekends, trips, weather plans and suggestions",
            [L169, L170, L171, L172, L173, L174, L175, L176, L177, L178, L179, L180])
