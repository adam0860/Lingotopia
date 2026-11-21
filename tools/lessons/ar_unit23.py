"""Unit 23 (chapter 21): planning a trip, conjunctions, security, comparatives, luggage, banking."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 355
L355 = lesson(
    "At the travel agency",
    "أُرِيد أَنْ أَحْجِز رِحْلَة · خَصْم لِحَجْز مَجْمُوعَة",
    requires=["وكالة", "رحلة", "حجز", "خصم", "سياحة", "مجموعة", "أسبوع", "فندق"],
    cards=[
        card("Words for booking a trip",
             "A travel agency is وِكَالَة سِيَاحَة and a tour is رِحْلَة سِيَاحِيَّة. To book is حَجَزَ يَحْجِز, and a booking is حَجْز. A booking for a whole group is حَجْز لِمَجْمُوعَة, and a discount is خَصْم. "
             "After أُرِيد you can use أَنْ and a present verb: أُرِيد أَنْ أَحْجِز, “I want to book”.",
             tables=[table(["English", "Arabic"],
                           [["travel agency", "وِكَالَة سِيَاحَة"], ["tour, trip", "رِحْلَة سِيَاحِيَّة"], ["booking", "حَجْز"], ["group booking", "حَجْز لِمَجْمُوعَة"], ["discount", "خَصْم"],
                            ["group", "مَجْمُوعَة"], ["tourist", "سَائِح"], ["tour guide", "مُرْشِد سِيَاحِيّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("At the agency (invented)",
             "A traveller talks to an agent about a holiday for six people.",
             examples=[
                 ex("أُرِيد أَنْ أَحْجِز رِحْلَة سِيَاحِيَّة لِسِتَّة أَفْرَاد.", "I want to book a tour for six people.", "أَحْجِز"),
                 ex("هَلْ هُنَاكَ خَصْم لِحَجْز مَجْمُوعَة؟", "Is there a discount for a group booking?", "حَجْز مَجْمُوعَة"),
                 ex("نَعَمْ، الْخَصْم عِشْرُون بِالْمِئَة.", "Yes, the discount is twenty per cent.", "الْخَصْم"),
                 ex("نُرِيد إِجَازَة لِمُدَّة أُسْبُوعَيْن.", "We want a holiday of two weeks.", "أُسْبُوعَيْن"),
                 ex("سَنَزُور سُورِيَا وَالْأُرْدُنّ وَمِصْر وَالْمَغْرِب.", "We will visit Syria, Jordan, Egypt and Morocco.", "سَنَزُور"),
                 ex("نُرِيد فَنَادِق جَيِّدَة بِسِعْر مُنَاسِب.", "We want good hotels at a suitable price.", "فَنَادِق"),
             ]),
    ],
    exercises=[
        M("What is a وِكَالَة سِيَاحَة?", "a travel agency", ["a school", "a bank", "a hotel"], "وِكَالَة = agency; سِيَاحَة = tourism."),
        M("What does حَجْز mean?", "booking", ["discount", "tour guide", "passport"], "حَجَزَ = to book."),
        M("What does خَصْم mean?", "discount", ["price", "ticket", "hotel"], "خَصْم = discount."),
        M("What does أُرِيد أَنْ أَحْجِز رِحْلَة mean?", "I want to book a trip", ["I want to cancel a trip", "I booked a trip yesterday", "I will pay for a trip"], "أُرِيد أَنْ = I want to."),
        M("What is a حَجْز لِمَجْمُوعَة?", "a group booking", ["a single ticket", "a free ticket", "a hotel key"], "لِـ = for; مَجْمُوعَة = group."),
        M("What does سَنَزُور سُورِيَا وَالْأُرْدُنّ mean?", "We will visit Syria and Jordan", ["We visited Syria and Jordan", "We live in Syria and Jordan", "We will leave Syria and Jordan"], "سَنَزُور = we will visit."),
        F("أُرِيد أَنْ ___ رِحْلَة لِسِتَّة أَفْرَاد.", "أَحْجِز", ["حَجَزْتُ", "يَحْجِز"], "After أَنْ, with أَنَا: أَحْجِز.", tr="I want to book a trip for six people.", lemma="حجز:sub:ana"),
        F("هَلْ هُنَاكَ ___ لِحَجْز مَجْمُوعَة؟", "خَصْم", ["فُنْدُق", "مُرْشِد"], "A booking can get a discount.", tr="Is there a discount for a group booking?"),
        F("نُرِيد إِجَازَة لِمُدَّة ___.", "أُسْبُوعَيْن", ["أُسْبُوعَان", "أُسْبُوعِين"], "After لِمُدَّة a dual noun takes the genitive form: ـَيْن.", tr="We want a holiday of two weeks."),
    ],
    verify=(vv("حجز", "sub", ana="أَحْجِز") + vv("زور", "fut", nahnu="سَنَزُور")),
)

# ---------------------------------------------------------------------------- 356
L356 = lesson(
    "Planning the route",
    "سَنَبِيت فِي دِمَشْق لَيْلَتَيْن · نَنْوِي أَنْ نَزُور أَرْبَع دُوَل",
    requires=["زار", "سافر", "عاد", "بات", "نوى", "خطط", "ليلة", "دولة", "شهر"],
    cards=[
        card("Verbs of a journey",
             "These verbs are useful when you plan a route. زَارَ يَزُور (“to visit”) and عَادَ يَعُود (“to return”) are hollow; بَاتَ يَبِيت (“to spend the night”) is hollow too; نَوَى يَنْوِي (“to intend”) is defective. "
             "Time words help to order the plan: بِدَايَة الشَّهْر (“the beginning of the month”), مُنْتَصَف الشَّهْر (“the middle of the month”) and نِهَايَة الشَّهْر (“the end of the month”).",
             tables=[table(["English", "Past", "Present"],
                           [["visit", "زَارَ", "يَزُور"], ["travel", "سَافَرَ", "يُسَافِر"], ["spend the night", "بَاتَ", "يَبِيت"], ["return", "عَادَ", "يَعُود"], ["intend", "نَوَى", "يَنْوِي"], ["plan", "خَطَّطَ", "يُخَطِّط"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("A plan for the trip (invented)",
             "Six friends plan a two-week journey.",
             examples=[
                 ex("نَنْوِي أَنْ نَزُور أَرْبَع دُوَل.", "We intend to visit four countries.", "نَنْوِي"),
                 ex("سَنَبِيت فِي دِمَشْق لَيْلَتَيْن.", "We will spend two nights in Damascus.", "سَنَبِيت"),
                 ex("بَعْد ذَلِكَ نُسَافِر بِالْحَافِلَة إِلَى عَمَّان.", "After that we travel by bus to Amman.", "نُسَافِر"),
                 ex("سَنَصِل إِلَى الْمَغْرِب فِي مُنْتَصَف الشَّهْر.", "We will arrive in Morocco in the middle of the month.", "مُنْتَصَف الشَّهْر"),
                 ex("وَفِي نِهَايَة الرِّحْلَة نَعُود إِلَى الْكُوَيْت.", "And at the end of the trip we return to Kuwait.", "نَعُود"),
                 ex("خَطَّطْنَا لِلرِّحْلَة مُنْذُ شَهْر.", "We have been planning the trip for a month.", "خَطَّطْنَا"),
             ]),
    ],
    exercises=[
        M("What does نَنْوِي أَنْ نَزُور mean?", "we intend to visit", ["we visited", "we refuse to visit", "we forgot to visit"], "نَوَى يَنْوِي = to intend."),
        M("What does سَنَبِيت فِي دِمَشْق mean?", "We will spend the night in Damascus", ["We spent the night in Damascus", "We will leave Damascus", "We live in Damascus"], "سَنَبِيت = we will spend the night."),
        M("What does مُنْتَصَف الشَّهْر mean?", "the middle of the month", ["the beginning of the month", "the end of the month", "every month"], "مُنْتَصَف = middle."),
        M("Which word means “end”?", "نِهَايَة", ["بِدَايَة", "مُنْتَصَف", "لَيْلَة"], "نِهَايَة = end."),
        M("What does نَعُود إِلَى الْكُوَيْت mean?", "we return to Kuwait", ["we leave Kuwait", "we visit Kuwait", "we love Kuwait"], "عَادَ يَعُود = to return."),
        M("What does لَيْلَتَيْن mean?", "two nights", ["two days", "three nights", "one night"], "A dual noun: ـَيْن."),
        F("___ أَنْ نَزُور أَرْبَع دُوَل.", "نَنْوِي", ["نَوَيْتُ", "يَنْوِي"], "“We intend”: نَنْوِي.", tr="We intend to visit four countries.", lemma="نوي:pres:nahnu"),
        F("سَنَصِل إِلَى الْمَغْرِب فِي ___ الشَّهْر.", "مُنْتَصَف", ["نِهَايَة", "لَيْلَة"], "In the middle of the month.", tr="We will arrive in Morocco in the middle of the month."),
        F("وَفِي نِهَايَة الرِّحْلَة ___ إِلَى الْكُوَيْت.", "نَعُود", ["نَزُور", "نَبِيت"], "We return to Kuwait.", tr="And at the end of the trip we return to Kuwait."),
    ],
    verify=(vv("نوي", "pres", nahnu="نَنْوِي") + vv("بيت", "fut", nahnu="سَنَبِيت") + vv("عود", "pres", nahnu="نَعُود")
            + vv("زور", "pres", nahnu="نَزُور", huwa="يَزُور") + vv("بيت", "pres", huwa="يَبِيت") + vv("عود", "pres", huwa="يَعُود")
            + vv("نوي", "past", huwa="نَوَى") + vv("زور", "past", huwa="زَارَ") + vv("عود", "past", huwa="عَادَ") + vv("بيت", "past", huwa="بَاتَ")),
)

# ---------------------------------------------------------------------------- 357
L357 = lesson(
    "Class, price and what is included",
    "الدَّرَجَة الْأُولَى · الدَّرَجَة السِّيَاحِيَّة · هَلِ السِّعْر يَشْمَل الْفُنْدُق؟",
    requires=["درجة", "تذكرة", "سعر", "شمل", "إقامة", "فندق", "مطار", "أغلى", "أرخص"],
    cards=[
        card("First class and economy",
             "A ticket can be in the first class, الدَّرَجَة الْأُولَى, or in the tourist class, الدَّرَجَة السِّيَاحِيَّة (“economy”). The verb شَمِلَ is used for “to include” here as يَشْمَل: السِّعْر يَشْمَل التَّذَاكِر, “the price includes the tickets”. "
             "To compare, use أَغْلَى مِنْ (“more expensive than”) and أَرْخَص مِنْ (“cheaper than”).",
             tables=[table(["English", "Arabic"],
                           [["ticket", "تَذْكِرَة"], ["tickets", "تَذَاكِر"], ["first class", "الدَّرَجَة الْأُولَى"], ["economy class", "الدَّرَجَة السِّيَاحِيَّة"], ["price", "سِعْر"], ["stay, accommodation", "إِقَامَة"], ["it includes", "يَشْمَل"], ["free", "مَجَّانِيّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Questions about the price (invented)",
             "These are typical questions and answers at an agency.",
             examples=[
                 ex("هَلِ السِّعْر يَشْمَل الْفُنْدُق؟", "Does the price include the hotel?", "يَشْمَل"),
                 ex("السِّعْر يَشْمَل التَّذَاكِر وَالْإِقَامَة وَمُرْشِد سِيَاحِيّ.", "The price includes the tickets, the stay and a tour guide.", "الْإِقَامَة"),
                 ex("تَذْكِرَة الدَّرَجَة الْأُولَى أَغْلَى مِنْ تَذْكِرَة الدَّرَجَة السِّيَاحِيَّة.", "A first-class ticket is more expensive than an economy ticket.", "أَغْلَى"),
                 ex("نُرِيد الدَّرَجَة السِّيَاحِيَّة.", "We want economy class.", "السِّيَاحِيَّة"),
                 ex("هَلِ التَّوْصِيل مِنَ الْمَطَار مَجَّانِيّ؟", "Is the transfer from the airport free?", "مَجَّانِيّ"),
                 ex("نَعَمْ، التَّوْصِيل مَجَّانِيّ.", "Yes, the transfer is free.", "التَّوْصِيل"),
             ]),
    ],
    exercises=[
        M("What is الدَّرَجَة السِّيَاحِيَّة?", "economy class", ["first class", "a free ticket", "a hotel room"], "سِيَاحِيّ = tourist."),
        M("What does يَشْمَل mean?", "it includes", ["it costs", "it leaves", "it opens"], "شَمِلَ/يَشْمَل = to include."),
        M("What does هَلِ السِّعْر يَشْمَل الْفُنْدُق؟ ask?", "Does the price include the hotel?", ["Where is the hotel?", "Is the hotel big?", "How many nights?"], "يَشْمَل = includes."),
        M("What does مَجَّانِيّ mean?", "free of charge", ["expensive", "late", "far"], "مَجَّانِيّ = free."),
        M("Which ticket costs more?", "الدَّرَجَة الْأُولَى", ["الدَّرَجَة السِّيَاحِيَّة", "both are the same", "neither"], "أَغْلَى = more expensive."),
        M("What does أَرْخَص مِنْ mean?", "cheaper than", ["more expensive than", "bigger than", "later than"], "أَرْخَص = cheaper."),
        F("هَلِ السِّعْر ___ الْفُنْدُق؟", "يَشْمَل", ["يَفْتَح", "يَكْتُب"], "The price includes the hotel.", tr="Does the price include the hotel?"),
        F("تَذْكِرَة الدَّرَجَة الْأُولَى ___ مِنْ تَذْكِرَة الدَّرَجَة السِّيَاحِيَّة.", "أَغْلَى", ["غَالِي", "الْأَغْلَى"], "Comparative + مِنْ.", tr="A first-class ticket is more expensive than an economy ticket."),
        F("هَلِ التَّوْصِيل مِنَ الْمَطَار ___؟", "مَجَّانِيّ", ["مُرْشِد", "تَذْكِرَة"], "The transfer can be free.", tr="Is the transfer from the airport free?"),
    ],
    verify=vv("شمل", "pres", huwa="يَشْمَل"),
)

# ---------------------------------------------------------------------------- 358
L358 = lesson(
    "And, and then at once: وَ and فَ",
    "ذَهَبْنَا إِلَى الْمَطَار وَرَكِبْنَا الطَّائِرَة · وَصَلْنَا فَرَكِبْنَا الْحَافِلَة",
    requires=["ركب", "وصل", "مطار", "حافلة", "دخل", "ذهب"],
    cards=[
        card("Two small conjunctions",
             "A conjunction joins two words or two clauses. وَ (“and”) simply adds one thing to another. فَ (“and so, and then at once”) joins two actions that follow each other without a break. "
             "Both are written as part of the next word: وَرَكِبْنَا, فَرَكِبْنَا.",
             tables=[table(["Conjunction", "Meaning", "Example"],
                           [["وَ", "and (adds)", "ذَهَبْنَا وَرَكِبْنَا"], ["فَ", "and then at once", "وَصَلْنَا فَرَكِبْنَا"]],
                           say=[0, 2], tlit=[0, 2], gloss=False)]),
        card("Examples",
             "In each pair, notice which action follows the other immediately.",
             examples=[
                 ex("ذَهَبْنَا إِلَى الْمَطَار وَرَكِبْنَا الطَّائِرَة.", "We went to the airport and boarded the plane.", "وَرَكِبْنَا"),
                 ex("وَصَلْنَا فَرَكِبْنَا الْحَافِلَة.", "We arrived and at once took the bus.", "فَرَكِبْنَا"),
                 ex("دَخَلَ الْمُوَظَّف فَسَلَّمَ عَلَيْنَا.", "The employee came in and at once greeted us.", "فَسَلَّمَ"),
                 ex("سَنَذْهَب إِلَى دِمَشْق فَعَمَّان بِدُون تَوَقُّف.", "We will go to Damascus and then straight to Amman without stopping.", "فَعَمَّان"),
                 ex("زُرْنَا الْمَتْحَف وَالسُّوق وَالْفُنْدُق.", "We visited the museum, the market and the hotel.", "وَالسُّوق"),
                 ex("كَتَبْتُ الْبِطَاقَة وَأَرْسَلْتُهَا.", "I wrote the card and sent it.", "وَأَرْسَلْتُهَا"),
             ]),
    ],
    exercises=[
        M("Which conjunction means “and then at once”?", "فَ", ["وَ", "أَوْ", "لَا"], "فَ = immediate sequence."),
        M("What does وَ do?", "adds one thing to another", ["asks a question", "says no", "shows the past"], "وَ = and."),
        M("What does وَصَلْنَا فَرَكِبْنَا الْحَافِلَة mean?", "We arrived and at once took the bus", ["We took the bus and then arrived", "We did not take the bus", "We will take the bus"], "فَ = at once."),
        M("In دَخَلَ الْمُوَظَّف فَسَلَّمَ عَلَيْنَا, what does فَ show?", "the greeting came right after he entered", ["a choice", "a long wait", "a question"], "فَ links actions that follow without a break."),
        M("How is the conjunction written?", "joined to the next word", ["as a separate word", "after the word", "with a space and a dash"], "وَ and فَ are attached to the next word."),
        M("Which sentence means “We visited the museum and the market”?", "زُرْنَا الْمَتْحَف وَالسُّوق", ["زُرْنَا الْمَتْحَف أَوِ السُّوق", "سَنَزُور الْمَتْحَف وَالسُّوق", "لَمْ نَزُر الْمَتْحَف"], "وَ = and; زُرْنَا = we visited."),
        F("ذَهَبْنَا إِلَى الْمَطَار ___ رَكِبْنَا الطَّائِرَة.", "وَ", ["لَا", "هَلْ"], "A simple “and”: written وَرَكِبْنَا.", tr="We went to the airport and boarded the plane."),
        F("زُرْنَا الْمَتْحَف ___ السُّوق.", "وَ", ["أَوْ", "لَمْ"], "“and”: وَالسُّوق.", tr="We visited the museum and the market."),
        F("كَتَبْتُ الْبِطَاقَة ___ أَرْسَلْتُهَا.", "وَ", ["هَلْ", "لَنْ"], "“and”: وَأَرْسَلْتُهَا.", tr="I wrote the card and sent it."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 359
L359 = lesson(
    "Then, or: ثُمَّ and أَوْ",
    "ثُمَّ نُسَافِر إِلَى الْمَغْرِب · الدَّرَجَة الْأُولَى أَوِ السِّيَاحِيَّة",
    requires=["ثم", "أو", "درجة", "سافر", "بعد", "يوم"],
    cards=[
        card("Later: ثُمَّ. A choice: أَوْ",
             "ثُمَّ (“then, after that”) is a separate word. It joins two actions with a gap of time between them, unlike فَ. أَوْ (“or”) gives a choice. Before ال it takes a helping vowel: أَوِ السِّيَاحِيَّة.",
             tables=[table(["Conjunction", "Meaning", "Example"],
                           [["وَ", "and (adds)", "الْمَطَار وَالْفُنْدُق"], ["فَ", "and then at once", "وَصَلْنَا فَدَخَلْنَا"], ["ثُمَّ", "then, after a time", "نَبِيت خَمْسَة أَيَّام ثُمَّ نُسَافِر"], ["أَوْ", "or (a choice)", "الْأُولَى أَوِ السِّيَاحِيَّة"]],
                           say=[0, 2], tlit=[0, 2], gloss=False)]),
        card("Examples",
             "Read the sentences and decide: add, at once, later, or choose.",
             examples=[
                 ex("سَنَبِيت خَمْسَة أَيَّام ثُمَّ نُسَافِر إِلَى الْمَغْرِب.", "We will stay five days and then travel to Morocco.", "ثُمَّ"),
                 ex("هَلْ تُرِيدُون الدَّرَجَة الْأُولَى أَوِ السِّيَاحِيَّة؟", "Do you want first class or economy?", "أَوِ"),
                 ex("نَذْهَب بِالطَّائِرَة أَوْ بِالْحَافِلَة.", "We go by plane or by bus.", "أَوْ"),
                 ex("زُرْنَا عَمَّان ثُمَّ ذَهَبْنَا إِلَى الْقُدْس.", "We visited Amman and then went on to Jerusalem.", "ثُمَّ"),
                 ex("اِشْتَرَيْنَا التَّذَاكِر ثُمَّ حَجَزْنَا الْفُنْدُق.", "We bought the tickets and then booked the hotel.", "ثُمَّ"),
                 ex("مَاذَا تُفَضِّل: الْعَصِير أَوِ الْقَهْوَة؟", "Which do you prefer: juice or coffee?", "أَوِ"),
             ]),
    ],
    exercises=[
        M("What does ثُمَّ mean?", "then, after a time", ["or", "and at once", "because"], "ثُمَّ = then."),
        M("What does أَوْ mean?", "or", ["and", "then", "but"], "أَوْ = or."),
        M("Which word gives a choice?", "أَوْ", ["ثُمَّ", "فَ", "وَ"], "أَوْ = or."),
        M("What is the difference between ثُمَّ and فَ?", "ثُمَّ leaves a gap of time", ["ثُمَّ asks a question", "فَ means or", "there is none"], "فَ = at once; ثُمَّ = after a time."),
        M("What does سَنَبِيت خَمْسَة أَيَّام ثُمَّ نُسَافِر mean?", "We will stay five days and then travel", ["We will travel and then stay", "We will stay or travel", "We did not travel"], "ثُمَّ = then."),
        M("Why is it أَوِ السِّيَاحِيَّة with a kasra?", "the sukūn takes a helping vowel before ال", ["it is a plural", "it is a question", "it is a command"], "A final sukūn before ال takes a helping vowel."),
        F("نَبِيت خَمْسَة أَيَّام ___ نُسَافِر.", "ثُمَّ", ["أَوْ", "هَلْ"], "A gap of time: then.", tr="We stay five days and then travel."),
        F("نَذْهَب بِالطَّائِرَة ___ بِالْحَافِلَة.", "أَوْ", ["ثُمَّ", "لَمْ"], "A choice: or.", tr="We go by plane or by bus."),
        F("هَلْ تُرِيدُون الدَّرَجَة الْأُولَى ___ السِّيَاحِيَّة؟", "أَوِ", ["أَوْ", "ثُمَّ"], "Before ال the sukūn takes a helping vowel.", tr="Do you want first class or economy?"),
    ],
    verify=(),
)


# ---------------------------------------------------------------------------- 360
L360 = lesson(
    "After a conjunction: the same case",
    "رَأَيْتُ الْمُدِيرَ وَالْمُوَظَّفَ · وَصَلَ الْمُدِيرُ وَالْمُوَظَّفُ",
    requires=["مدير", "موظف", "وصل", "تكلم", "مع"],
    cards=[
        card("The second part follows the first",
             "A conjunction joins two things of the same kind, so the second noun takes the same case as the first. In this lesson the case endings are written out, although in most of the course they are left off: "
             "the nominative ends in ḍamma (ـُ), the accusative in fatḥa (ـَ) and the genitive in kasra (ـِ).",
             tables=[table(["Case", "Example", "English"],
                           [["nominative", "وَصَلَ الْمُدِيرُ وَالْمُوَظَّفُ.", "The manager and the employee arrived."], ["accusative", "رَأَيْتُ الْمُدِيرَ وَالْمُوَظَّفَ.", "I saw the manager and the employee."], ["genitive", "تَكَلَّمْتُ مَعَ الْمُدِيرِ وَالْمُوَظَّفِ.", "I spoke with the manager and the employee."]],
                           say=[1], tlit=[1], gloss=False)]),
        card("More examples",
             "Notice that both nouns always end in the same vowel.",
             examples=[
                 ex("وَصَلَ الْمُدِيرُ وَالْمُوَظَّفُ.", "The manager and the employee arrived.", "وَالْمُوَظَّفُ"),
                 ex("رَأَيْتُ الْمُدِيرَ وَالْمُوَظَّفَ.", "I saw the manager and the employee.", "وَالْمُوَظَّفَ"),
                 ex("تَكَلَّمْتُ مَعَ الْمُدِيرِ وَالْمُوَظَّفِ.", "I spoke with the manager and the employee.", "وَالْمُوَظَّفِ"),
                 ex("الْمَطَارُ وَالْفُنْدُقُ قَرِيبَانِ.", "The airport and the hotel are near.", "وَالْفُنْدُقُ"),
                 ex("زُرْتُ الْمَتْحَفَ وَالسُّوقَ.", "I visited the museum and the market.", "وَالسُّوقَ"),
                 ex("ذَهَبْتُ إِلَى الْمَتْحَفِ وَالسُّوقِ.", "I went to the museum and the market.", "وَالسُّوقِ"),
             ]),
    ],
    exercises=[
        M("Which vowel mark is the accusative ending?", "fatḥa", ["ḍamma", "kasra", "sukūn"], "Accusative = fatḥa."),
        M("Which vowel mark is the genitive ending?", "kasra", ["fatḥa", "ḍamma", "sukūn"], "Genitive = kasra."),
        M("Which case follows a preposition such as مَعَ or إِلَى?", "genitive", ["nominative", "accusative", "none"], "A preposition is followed by the genitive."),
        M("What is the rule for a conjunction?", "the second noun has the same case as the first", ["the second noun is always nominative", "the second noun has no ending", "the second noun is always genitive"], "Equal grammatical weight → equal case."),
        M("Which sentence has matching endings?", "رَأَيْتُ الْمُدِيرَ وَالْمُوَظَّفَ", ["رَأَيْتُ الْمُدِيرَ وَالْمُوَظَّفُ", "رَأَيْتُ الْمُدِيرُ وَالْمُوَظَّفِ"], "Both are accusative: ـَ and ـَ."),
        M("Why does الْمُوَظَّفِ end in a kasra in تَكَلَّمْتُ مَعَ الْمُدِيرِ وَالْمُوَظَّفِ?", "it follows the genitive الْمُدِيرِ after مَعَ", ["it is the subject", "it is a question", "it is a command"], "The second noun copies the case of the first."),
        F("رَأَيْتُ الْمُدِيرَ وَ___.", "الْمُوَظَّفَ", ["الْمُوَظَّفُ", "الْمُوَظَّفِ"], "The first noun is accusative, so the second is accusative.", tr="I saw the manager and the employee."),
        F("وَصَلَ الْمُدِيرُ وَ___.", "الْمُوَظَّفُ", ["الْمُوَظَّفَ", "الْمُوَظَّفِ"], "The first noun is nominative, so the second is nominative.", tr="The manager and the employee arrived."),
        F("تَكَلَّمْتُ مَعَ الْمُدِيرِ وَ___.", "الْمُوَظَّفِ", ["الْمُوَظَّفُ", "الْمُوَظَّفَ"], "The first noun is genitive, so the second is genitive.", tr="I spoke with the manager and the employee."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 361
L361 = lesson(
    "Choosing the right conjunction",
    "وَ · فَ · ثُمَّ · أَوْ فِي قِصَّة قَصِيرَة",
    requires=["حجز", "مطار", "طائرة", "رحلة", "مقعد", "نافذة", "باب"],
    cards=[
        card("A short story (invented)",
             "Sara plans a trip. Read the story and notice which conjunction fits each step: addition (وَ), an immediate next step (فَ), a later step (ثُمَّ) or a choice (أَوْ).",
             examples=[
                 ex("حَجَزَتْ سَارَة رِحْلَة إِلَى الْمَغْرِب ثُمَّ اِشْتَرَتْ تَذْكِرَتَيْن.", "Sara booked a trip to Morocco and then bought two tickets.", "ثُمَّ"),
                 ex("وَصَلَتْ إِلَى الْمَطَار فَدَخَلَتْ مُبَاشَرَةً.", "She arrived at the airport and went straight in.", "فَدَخَلَتْ"),
                 ex("هَلْ تُفَضِّلِينَ الْمَقْعَد قُرْب النَّافِذَة أَوْ قُرْب الْبَاب؟", "Do you prefer a seat near the window or near the door?", "أَوْ"),
                 ex("رَكِبَتِ الطَّائِرَة وَقَرَأَتْ جَرِيدَة.", "She boarded the plane and read a newspaper.", "وَقَرَأَتْ"),
                 ex("بَعْد سَاعَتَيْن وَصَلَتِ الطَّائِرَة.", "After two hours the plane arrived.", "سَاعَتَيْن"),
                 ex("نَزَلَتْ مِنَ الطَّائِرَة فَوَجَدَتْ أَخَاهَا.", "She got off the plane and at once found her brother.", "فَوَجَدَتْ"),
             ]),
    ],
    exercises=[
        M("Which word fits: حَجَزَتْ رِحْلَة ___ اِشْتَرَتْ تَذْكِرَتَيْن (a later step)?", "ثُمَّ", ["أَوْ", "لَا", "هَلْ"], "A later step: ثُمَّ."),
        M("Which conjunction fits: هَلْ تُفَضِّلِينَ النَّافِذَة ___ الْبَاب?", "أَوِ", ["ثُمَّ", "فَ", "لَنْ"], "A choice: أَوْ (أَوِ before الـ)."),
        M("In وَصَلَتْ فَدَخَلَتْ, what does فَ tell us?", "she went in at once", ["she waited a long time", "she did not go in", "she went in or out"], "فَ = immediate sequence."),
        M("Which sentence adds one action to another?", "رَكِبَتِ الطَّائِرَة وَقَرَأَتْ جَرِيدَة", ["رَكِبَتِ الطَّائِرَة أَوْ قَرَأَتْ", "رَكِبَتِ الطَّائِرَة ثُمَّ لَمْ تَقْرَأْ", "هَلْ رَكِبَتِ الطَّائِرَة"], "وَ adds."),
        M("Which sentence means “She got off the plane and at once found her brother”?", "نَزَلَتْ مِنَ الطَّائِرَة فَوَجَدَتْ أَخَاهَا", ["نَزَلَتْ مِنَ الطَّائِرَة أَوْ وَجَدَتْ أَخَاهَا", "سَتَنْزِل مِنَ الطَّائِرَة", "لَمْ تَنْزِلْ مِنَ الطَّائِرَة"], "فَ = at once."),
        M("Which conjunction is a separate word, not joined to the next one?", "ثُمَّ", ["وَ", "فَ", "all of them"], "وَ and فَ are attached; ثُمَّ and أَوْ are separate words."),
        F("حَجَزْتُ التَّذْكِرَة ___ دَفَعْتُ الْمَبْلَغ بَعْد يَوْمَيْن.", "ثُمَّ", ["أَوْ", "هَلْ"], "A gap of two days: then.", tr="I booked the ticket and then paid the amount two days later."),
        F("هَلْ سَتَسْكُنِينَ فِي فُنْدُق ___ فِي شَقَّة؟", "أَوْ", ["ثُمَّ", "لَنْ"], "A choice between two places.", tr="Will you live in a hotel or in an apartment?"),
        F("دَخَلَ الْمُوَظَّف الْغُرْفَة ___ سَلَّمَ عَلَيْنَا.", "فَ", ["هَلْ", "لَمْ"], "Written attached: فَسَلَّمَ. No wait between the two actions.", tr="The employee came into the room and at once greeted us."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 362
L362 = lesson(
    "Security precautions",
    "الْإِجْرَاءَات الْأَمْنِيَّة · جِهَاز كَشْف الْمَعَادِن · أَبْرِزْ جَوَاز السَّفَر",
    requires=["أمن", "تفتيش", "جواز", "سفر", "جهاز", "بطاقة", "حقيبة", "خلال"],
    cards=[
        card("At the security check",
             "Security at an airport is أَمْن, and the security procedures are الْإِجْرَاءَات الْأَمْنِيَّة. A search is تَفْتِيش, and the verb is فَتَّشَ (Measure II). "
             "The commands you hear are short: أَبْرِزْ (Measure IV, “show!”), ضَعْ (“put!”), اِمْشِ (“walk!”). Rules differ from one airport to another.",
             tables=[table(["English", "Arabic"],
                           [["security", "أَمْن"], ["security procedures", "الْإِجْرَاءَات الْأَمْنِيَّة"], ["search, inspection", "تَفْتِيش"], ["metal detector", "جِهَاز كَشْف الْمَعَادِن"], ["passport", "جَوَاز سَفَر"], ["boarding pass", "بِطَاقَة صُعُود"], ["bag", "حَقِيبَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What the officer says (invented)",
             "These are typical lines at a checkpoint.",
             examples=[
                 ex("الْإِجْرَاءَات الْأَمْنِيَّة فِي الْمَطَارَات مُشَدَّدَة.", "Security procedures at airports are strict.", "مُشَدَّدَة"),
                 ex("أَبْرِزْ جَوَاز السَّفَر وَبِطَاقَة الصُّعُود.", "Show your passport and boarding pass.", "أَبْرِزْ"),
                 ex("ضَعْ حَقِيبَتَكَ عَلَى الْجِهَاز.", "Put your bag on the machine.", "ضَعْ"),
                 ex("اِمْشِ مِنْ خِلَال جِهَاز كَشْف الْمَعَادِن.", "Walk through the metal detector.", "اِمْشِ"),
                 ex("فَتَّشَ الْمُوَظَّف حَقِيبَتِي.", "The officer searched my bag.", "فَتَّشَ"),
                 ex("لَا تَتْرُكْ حَقِيبَتَكَ وَحْدَهَا.", "Do not leave your bag alone.", "لَا تَتْرُكْ"),
             ]),
    ],
    exercises=[
        M("What does تَفْتِيش mean?", "search, inspection", ["booking", "discount", "ticket"], "فَتَّشَ = to search."),
        M("What is جِهَاز كَشْف الْمَعَادِن?", "a metal detector", ["a ticket machine", "a passport", "a suitcase"], "كَشْف = detecting; مَعَادِن = metals."),
        M("What does أَبْرِزْ جَوَاز السَّفَر mean?", "Show your passport", ["Lose your passport", "Write your passport", "Buy a passport"], "أَبْرِزْ = show! (command)."),
        M("What does لَا تَتْرُكْ حَقِيبَتَكَ وَحْدَهَا mean?", "Do not leave your bag alone", ["Take your bag home", "Leave your bag here", "I left my bag"], "لَا + short form = do not."),
        M("What does مُشَدَّدَة mean in الْإِجْرَاءَات مُشَدَّدَة?", "strict", ["free", "late", "cheap"], "مُشَدَّد = strengthened, strict."),
        M("Who does فَتَّشَ الْمُوَظَّف حَقِيبَتِي describe?", "the officer searched my bag", ["I searched the officer", "the officer lost my bag", "the officer will search my bag"], "Past tense: فَتَّشَ."),
        F("___ جَوَاز السَّفَر وَبِطَاقَة الصُّعُود.", "أَبْرِزْ", ["أَبْرَزَ", "يُبْرِز"], "A command to one man (Measure IV): أَبْرِزْ.", tr="Show the passport and the boarding pass.", lemma="برز#4:imp:anta"),
        F("___ الْمُوَظَّف حَقِيبَتِي.", "فَتَّشَ", ["فَتِّشْ", "يُفَتِّش"], "Past, he: فَتَّشَ.", tr="The officer searched my bag.", lemma="فتش#2:past:huwa"),
        F("اِمْشِ مِنْ ___ جِهَاز كَشْف الْمَعَادِن.", "خِلَال", ["فَوْق", "قَبْل"], "“through”: مِنْ خِلَال.", tr="Walk through the metal detector."),
    ],
    verify=(vv("برز#4", "imp", anta="أَبْرِزْ") + vv("فتش#2", "past", huwa="فَتَّشَ")),
)

# ---------------------------------------------------------------------------- 363
L363 = lesson(
    "What may you carry?",
    "حَقِيبَة الْيَد · الْأَمْتِعَة · الْحَدّ الْأَقْصَى لِلْوَزْن",
    requires=["حقيبة", "وزن", "ممنوع", "كيلو", "مكتب"],
    cards=[
        card("Hand luggage and checked bags",
             "Your hand bag is حَقِيبَة الْيَد. The bags you check in are الْأَمْتِعَة الْمُسَجَّلَة. The heaviest weight allowed is الْحَدّ الْأَقْصَى لِلْوَزْن. Something not allowed is مَمْنُوع. Airlines and airports have their own rules, so always read the notice.",
             tables=[table(["English", "Arabic"],
                           [["hand bag", "حَقِيبَة الْيَد"], ["checked luggage", "الْأَمْتِعَة الْمُسَجَّلَة"], ["weight", "وَزْن"], ["maximum", "الْحَدّ الْأَقْصَى"], ["forbidden, not allowed", "مَمْنُوع"], ["knives", "سَكَاكِين"], ["scissors", "مِقَصّ"], ["liquids", "سَوَائِل"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A notice (invented)",
             "A notice at the check-in desk of an invented airline.",
             examples=[
                 ex("الْحَدّ الْأَقْصَى لِلْوَزْن عِشْرُون كِيلُو.", "The maximum weight is twenty kilos.", "الْحَدّ الْأَقْصَى"),
                 ex("حَقِيبَة الْيَد تَدْخُل الطَّائِرَة مَعَكَ.", "The hand bag goes into the plane with you.", "حَقِيبَة الْيَد"),
                 ex("السَّكَاكِين وَالْمِقَصَّات مَمْنُوعَة فِي حَقِيبَة الْيَد.", "Knives and scissors are not allowed in the hand bag.", "مَمْنُوعَة"),
                 ex("السَّوَائِل فِي زُجَاجَات كَبِيرَة مَمْنُوعَة.", "Liquids in large bottles are not allowed.", "السَّوَائِل"),
                 ex("نُسَجِّل الْأَمْتِعَة عِنْدَ الْمَكْتَب.", "We check in the bags at the desk.", "نُسَجِّل"),
                 ex("قِفْ هُنَا مِنْ فَضْلِكَ.", "Stand here, please.", "قِفْ"),
             ]),
    ],
    exercises=[
        M("What is حَقِيبَة الْيَد?", "hand luggage", ["a passport", "a ticket", "a key"], "يَد = hand."),
        M("What does مَمْنُوع mean?", "not allowed", ["free", "big", "late"], "مَمْنُوع = forbidden."),
        M("What does الْحَدّ الْأَقْصَى لِلْوَزْن mean?", "the maximum weight", ["the minimum price", "the first class", "the departure time"], "أَقْصَى = furthest, maximum."),
        M("Which are forbidden in the notice?", "knives and scissors in the hand bag", ["clothes in the hand bag", "books in the hand bag", "tickets in the hand bag"], "السَّكَاكِين وَالْمِقَصَّات مَمْنُوعَة."),
        M("Why is it مَمْنُوعَة with ـَة in السَّكَاكِين وَالْمِقَصَّات مَمْنُوعَة?", "a plural of things takes the feminine singular", ["the knives are women", "it is a question", "it is a command"], "Plural things → feminine singular adjective."),
        M("What does نُسَجِّل الْأَمْتِعَة mean?", "we check in the bags", ["we lose the bags", "we open the bags", "we buy bags"], "سَجَّلَ = to register, check in."),
        F("___ لِلْوَزْن عِشْرُون كِيلُو.", "الْحَدّ الْأَقْصَى", ["الْحَدّ الْأَدْنَى", "الْأَمْتِعَة"], "The top limit.", tr="The maximum weight is twenty kilos."),
        F("السَّكَاكِين ___ فِي حَقِيبَة الْيَد.", "مَمْنُوعَة", ["مَمْنُوع", "مَمْنُوعُون"], "Plural things: feminine singular.", tr="Knives are not allowed in the hand bag."),
        F("___ الْأَمْتِعَة عِنْدَ الْمَكْتَب.", "نُسَجِّل", ["أُسَجِّل", "يُسَجِّل"], "“We check in”: نُسَجِّل.", tr="We check in the bags at the desk.", lemma="سجل#2:pres:nahnu"),
    ],
    verify=vv("سجل#2", "pres", nahnu="نُسَجِّل"),
)

# ---------------------------------------------------------------------------- 364
L364 = lesson(
    "At the check-in desk (a dialogue)",
    "جَوَاز سَفَرِكَ مِنْ فَضْلِكَ · هَلْ مَعَكَ حَقِيبَة يَد؟",
    requires=["جواز", "سفر", "حقيبة", "وزن", "بوابة", "رحلة", "سعيد"],
    cards=[
        card("A conversation (invented)",
             "A passenger and an employee talk at an invented airline desk. Read the lines in order.",
             examples=[
                 ex("جَوَاز سَفَرِكَ وَتَذْكِرَتُكَ مِنْ فَضْلِكَ.", "Your passport and your ticket, please.", "جَوَاز سَفَرِكَ"),
                 ex("تَفَضَّلْ.", "Here you are.", "تَفَضَّلْ"),
                 ex("هَلْ مَعَكَ حَقِيبَة يَد؟", "Do you have a hand bag with you?", "مَعَكَ"),
                 ex("نَعَمْ، حَقِيبَة صَغِيرَة فَقَط.", "Yes, only a small bag.", "صَغِيرَة"),
                 ex("ضَعِ الْحَقِيبَة الْكَبِيرَة عَلَى الْمِيزَان.", "Put the big bag on the scale.", "ضَعِ"),
                 ex("وَزْنُهَا اِثْنَان وَعِشْرُون كِيلُو.", "Its weight is twenty-two kilos.", "وَزْنُهَا"),
                 ex("آسِف، الْحَدّ الْأَقْصَى عِشْرُون كِيلُو.", "I am sorry, the maximum is twenty kilos.", "آسِف"),
                 ex("رِحْلَة سَعِيدَة، الْبَوَّابَة رَقْم خَمْسَة.", "Have a good trip. Gate number five.", "رِحْلَة سَعِيدَة"),
             ]),
    ],
    exercises=[
        M("What does تَفَضَّلْ mean here?", "Here you are", ["Sit down", "Wait", "Goodbye"], "تَفَضَّلْ is said when you hand something over."),
        M("What does هَلْ مَعَكَ حَقِيبَة يَد؟ ask?", "Do you have a hand bag with you?", ["Where is the hand bag?", "Whose hand bag is this?", "How much is the hand bag?"], "مَعَكَ = with you."),
        M("What does the clerk ask for first?", "the passport and the ticket", ["the hotel key", "the money", "the bag"], "جَوَاز سَفَرِكَ وَتَذْكِرَتُكَ."),
        M("How heavy is the big bag?", "twenty-two kilos", ["twelve kilos", "twenty kilos", "two kilos"], "وَزْنُهَا اِثْنَان وَعِشْرُون كِيلُو."),
        M("What does آسِف، الْحَدّ الْأَقْصَى عِشْرُون كِيلُو mean?", "I am sorry, the maximum is twenty kilos", ["I am sorry, the bag is lost", "I am happy, the bag is light", "I am sorry, the plane is late"], "آسِف = sorry."),
        M("Which gate is mentioned?", "gate five", ["gate three", "gate ten", "gate one"], "الْبَوَّابَة رَقْم خَمْسَة."),
        F("جَوَاز سَفَرِكَ ___ فَضْلِكَ.", "مِنْ", ["فِي", "عَلَى"], "“please”: مِنْ فَضْلِكَ.", tr="Your passport, please."),
        F("ضَعِ الْحَقِيبَة ___ الْمِيزَان.", "عَلَى", ["تَحْت", "بَعْد"], "Put it on the scale.", tr="Put the bag on the scale."),
        F("رِحْلَة ___.", "سَعِيدَة", ["سَعِيد", "سُعَدَاء"], "رِحْلَة is feminine.", tr="Have a good trip."),
    ],
    verify=(),
)


# ---------------------------------------------------------------------------- 365
L365 = lesson(
    "More crowded, less used: أَكْثَر with a verbal noun",
    "أَكْثَر اِزْدِحَامًا مِنْ · أَقَلّ اِسْتِخْدَامًا مِنْ",
    requires=["أكثر", "أقل", "راحة", "نجاح", "طريق", "سريع"],
    cards=[
        card("When there is no أَفْعَل adjective",
             "You know comparatives such as أَكْبَر مِنْ and أَسْرَع مِنْ. When a quality has no short comparative of that kind, say أَكْثَر (“more”) or أَقَلّ (“less”) followed by a verbal noun with the accusative tanwīn (ـًا or ـَةً): "
             "أَكْثَر اِزْدِحَامًا, “more crowded”. The word مِنْ means “than”. The verbal noun is the one of the verb: اِزْدَحَمَ → اِزْدِحَام.",
             tables=[table(["English", "Arabic"],
                           [["more crowded", "أَكْثَر اِزْدِحَامًا"], ["less crowded", "أَقَلّ اِزْدِحَامًا"], ["more comfortable", "أَكْثَر رَاحَةً"], ["more successful", "أَكْثَر نَجَاحًا"], ["less used", "أَقَلّ اِسْتِخْدَامًا"], ["cheaper in price", "أَقَلّ سِعْرًا"], ["than", "مِنْ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Examples",
             "Read the comparisons.",
             examples=[
                 ex("الْقِطَار أَسْرَع مِنَ الْحَافِلَة وَأَقَلّ اِزْدِحَامًا.", "The train is faster than the bus and less crowded.", "أَقَلّ اِزْدِحَامًا"),
                 ex("هَذَا الطَّرِيق أَكْثَر اِزْدِحَامًا فِي الصَّبَاح.", "This road is more crowded in the morning.", "أَكْثَر اِزْدِحَامًا"),
                 ex("هَذَا الْفُنْدُق أَكْثَر رَاحَةً مِنْ ذَلِكَ الْفُنْدُق.", "This hotel is more comfortable than that hotel.", "أَكْثَر رَاحَةً"),
                 ex("هَذِهِ الشَّرِكَة أَكْثَر نَجَاحًا مِنَ الشَّرِكَة الْأُخْرَى.", "This company is more successful than the other company.", "أَكْثَر نَجَاحًا"),
                 ex("فُنْدُقُنَا أَقَلّ سِعْرًا.", "Our hotel is lower in price.", "أَقَلّ سِعْرًا"),
                 ex("الْخِطَابَات أَقَلّ اِسْتِخْدَامًا مِنَ الْبَرِيد الْإِلِكْتْرُونِيّ.", "Letters are used less than email.", "أَقَلّ اِسْتِخْدَامًا"),
             ]),
    ],
    exercises=[
        M("What does أَكْثَر اِزْدِحَامًا mean?", "more crowded", ["less crowded", "faster", "cheaper"], "أَكْثَر = more; اِزْدِحَام = crowding."),
        M("What does أَقَلّ سِعْرًا mean?", "lower in price", ["higher in price", "more comfortable", "more crowded"], "أَقَلّ = less."),
        M("Which word means “than”?", "مِنْ", ["إِلَى", "عَلَى", "فِي"], "مِنْ = than (after a comparative)."),
        M("What does هَذَا الْفُنْدُق أَكْثَر رَاحَةً مِنْ ذَلِكَ الْفُنْدُق mean?", "This hotel is more comfortable than that hotel", ["That hotel is more comfortable", "Both hotels are cheap", "This hotel is far"], "رَاحَة = comfort."),
        M("What ending does the verbal noun take after أَكْثَر?", "accusative tanwīn", ["no ending at all", "the dual ending", "the plural ending"], "أَكْثَر اِزْدِحَامًا، أَكْثَر رَاحَةً."),
        M("What does الْقِطَار أَسْرَع مِنَ الْحَافِلَة وَأَقَلّ اِزْدِحَامًا mean?", "The train is faster than the bus and less crowded", ["The bus is faster than the train", "The train is slower and more crowded", "The bus is less crowded than the plane"], "أَسْرَع = faster; أَقَلّ اِزْدِحَامًا = less crowded."),
        F("هَذَا الطَّرِيق أَكْثَر ___ فِي الصَّبَاح.", "اِزْدِحَامًا", ["مُزْدَحِم", "اِزْدَحَمَ"], "The verbal noun with tanwīn follows أَكْثَر.", tr="This road is more crowded in the morning."),
        F("هَذِهِ الشَّرِكَة أَكْثَر نَجَاحًا ___ الشَّرِكَة الْأُخْرَى.", "مِنَ", ["إِلَى", "فِي"], "“than”: مِنَ before ال.", tr="This company is more successful than the other company."),
        F("الْخِطَابَات أَقَلّ ___ مِنَ الْبَرِيد الْإِلِكْتْرُونِيّ.", "اِسْتِخْدَامًا", ["اِسْتِخْدَام", "اِسْتَخْدَمَ"], "A verbal noun with tanwīn: less used.", tr="Letters are used less than email."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 366
L366 = lesson(
    "The most crowded, the cheapest: الْأَكْثَر and الْأَقَلّ",
    "هُوَ الْأَكْثَر اِزْدِحَامًا · هِيَ الْأَقَلّ سِعْرًا",
    requires=["أكثر", "أقل", "شارع", "فندق", "حافلة", "شركة", "نجاح"],
    cards=[
        card("The superlative with a verbal noun",
             "To say “the most …”, put ال on أَكْثَر or أَقَلّ and keep the verbal noun with tanwīn: الْأَكْثَر اِزْدِحَامًا, “the most crowded”. The sentence usually has هُوَ or هِيَ before it. "
             "For “most of the …” use أَكْثَر with a plural noun: أَكْثَر السُّيَّاح, “most of the tourists”.",
             tables=[table(["English", "Arabic"],
                           [["the most crowded (m.)", "هُوَ الْأَكْثَر اِزْدِحَامًا"], ["the most comfortable (f.)", "هِيَ الْأَكْثَر رَاحَةً"], ["the cheapest (m.)", "هُوَ الْأَقَلّ سِعْرًا"], ["the most successful (f.)", "هِيَ الْأَكْثَر نَجَاحًا"], ["most of the tourists", "أَكْثَر السُّيَّاح"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Examples",
             "Notice هُوَ for a masculine noun and هِيَ for a feminine noun.",
             examples=[
                 ex("هَذَا الشَّارِع هُوَ الْأَكْثَر اِزْدِحَامًا فِي الْمَدِينَة.", "This street is the most crowded in the city.", "الْأَكْثَر اِزْدِحَامًا"),
                 ex("أَيّ فُنْدُق هُوَ الْأَقَلّ سِعْرًا؟", "Which hotel is the cheapest?", "الْأَقَلّ سِعْرًا"),
                 ex("هَذِهِ الْحَافِلَة هِيَ الْأَكْثَر رَاحَةً.", "This bus is the most comfortable.", "هِيَ"),
                 ex("هَذِهِ الشَّرِكَة هِيَ الْأَكْثَر نَجَاحًا.", "This company is the most successful.", "هِيَ الْأَكْثَر نَجَاحًا"),
                 ex("أَكْثَر السُّيَّاح يَزُورُون السُّوق الْقَدِيم.", "Most of the tourists visit the old market.", "أَكْثَر السُّيَّاح"),
                 ex("الْفُنْدُق الْجَدِيد هُوَ الْأَكْثَر رَاحَةً.", "The new hotel is the most comfortable.", "هُوَ"),
             ]),
    ],
    exercises=[
        M("What does الْأَكْثَر اِزْدِحَامًا mean?", "the most crowded", ["the least crowded", "more crowded", "crowded"], "ال + أَكْثَر = the most."),
        M("What does الْأَقَلّ سِعْرًا mean?", "the cheapest", ["the most expensive", "the fastest", "the biggest"], "الْأَقَلّ = the least."),
        M("Which pronoun goes with الْحَافِلَة (feminine)?", "هِيَ", ["هُوَ", "هُمْ", "أَنَا"], "حَافِلَة is feminine."),
        M("Which pronoun goes with الشَّارِع (masculine)?", "هُوَ", ["هِيَ", "هُنَّ", "أَنْتِ"], "شَارِع is masculine."),
        M("What does أَكْثَر السُّيَّاح mean?", "most of the tourists", ["the best tourist", "one tourist", "no tourists"], "أَكْثَر + plural = most of."),
        M("What is the difference between أَكْثَر اِزْدِحَامًا and الْأَكْثَر اِزْدِحَامًا?", "the second means “the most crowded”", ["the second means “less crowded”", "there is none", "the first is a question"], "ال makes it a superlative."),
        F("هَذِهِ الْحَافِلَة ___ الْأَكْثَر رَاحَةً.", "هِيَ", ["هُوَ", "هُنَّ"], "Feminine singular: هِيَ.", tr="This bus is the most comfortable."),
        F("أَيّ فُنْدُق هُوَ ___ سِعْرًا؟", "الْأَقَلّ", ["أَقَلّ", "قَلِيل"], "The cheapest: الْأَقَلّ.", tr="Which hotel is the cheapest?"),
        F("___ السُّيَّاح يَزُورُون السُّوق الْقَدِيم.", "أَكْثَر", ["الْأَكْثَر", "كَثِير"], "“most of”: أَكْثَر without ال before a plural.", tr="Most of the tourists visit the old market."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 367
L367 = lesson(
    "A walk through an old market (invented guide)",
    "مِنْ أَشْهَر الْأَسْوَاق · مَا أَجْمَلَ هَذِهِ الْأَقْمِشَةَ!",
    requires=["سوق", "مشهور", "هدية", "قماش", "أرخص", "آخر", "جميل"],
    cards=[
        card("What the guide says",
             "A guide shows a group around an old market. The phrase مِنْ أَشْهَر الْأَسْوَاق means “one of the most famous markets”: مِنْ is followed by a plural. This text is invented and describes no particular market.",
             examples=[
                 ex("هَذَا السُّوق مِنْ أَشْهَر الْأَسْوَاق فِي الْمَدِينَة.", "This market is one of the most famous markets in the city.", "مِنْ أَشْهَر"),
                 ex("هُوَ أَكْثَر اِزْدِحَامًا مِنَ الْمَرْكَز التِّجَارِيّ الْحَدِيث.", "It is more crowded than the modern shopping centre.", "أَكْثَر اِزْدِحَامًا"),
                 ex("الْأَسْعَار هُنَا أَرْخَص وَالْمُسَاوَمَة شَائِعَة.", "The prices here are cheaper and bargaining is common.", "أَرْخَص"),
                 ex("مَا أَجْمَلَ هَذِهِ الْأَقْمِشَةَ!", "How beautiful these fabrics are!", "مَا أَجْمَلَ"),
                 ex("أَيْنَ أَجِد هَدَايَا لِلْأَصْدِقَاء؟", "Where can I find gifts for my friends?", "أَجِد"),
                 ex("اِمْشُوا مَعِي إِلَى آخِر السُّوق.", "Walk with me to the end of the market (all of you).", "اِمْشُوا"),
             ]),
    ],
    exercises=[
        M("What does مِنْ أَشْهَر الْأَسْوَاق mean?", "one of the most famous markets", ["the only market", "a cheap market", "a closed market"], "مِنْ + plural = one of."),
        M("What does هُوَ أَكْثَر اِزْدِحَامًا مِنَ الْمَرْكَز mean?", "It is more crowded than the centre", ["It is cheaper than the centre", "It is far from the centre", "It is in the centre"], "أَكْثَر اِزْدِحَامًا مِنْ."),
        M("What does الْمُسَاوَمَة شَائِعَة mean?", "bargaining is common", ["bargaining is forbidden", "bargaining is expensive", "bargaining is late"], "شَائِعَة = common."),
        M("What does مَا أَجْمَلَ هَذِهِ الْأَقْمِشَةَ! express?", "admiration", ["a question", "a command", "a thanks"], "مَا + أَفْعَلَ = how …!"),
        M("What does اِمْشُوا مَعِي mean?", "Walk with me (to a group)", ["Walk with me (to one man)", "I walked with you", "We will walk"], "ـُوا = a group."),
        M("What does أَيْنَ أَجِد هَدَايَا؟ ask?", "Where can I find gifts?", ["Who sells gifts?", "How much are gifts?", "When do gifts arrive?"], "أَجِد = I find."),
        F("هَذَا السُّوق ___ أَشْهَر الْأَسْوَاق.", "مِنْ", ["فِي", "عَنْ"], "“one of the most famous”.", tr="This market is one of the most famous markets."),
        F("اِمْشُوا مَعِي إِلَى ___ السُّوق.", "آخِر", ["أَوَّل", "قَبْل"], "“to the end of”.", tr="Walk with me to the end of the market."),
        F("أَيْنَ ___ هَدَايَا لِلْأَصْدِقَاء؟", "أَجِد", ["وَجَدْتُ", "يَجِد"], "“I find”: أَجِد.", tr="Where can I find gifts for my friends?", lemma="وجد:pres:ana"),
    ],
    verify=(vv("وجد", "pres", ana="أَجِد") + vv("مشي", "imp", antum="اِمْشُوا")),
)

# ---------------------------------------------------------------------------- 368
L368 = lesson(
    "Lost luggage",
    "ضَاعَتْ حَقِيبَتِي · لَمْ تَصِلْ مَعَ الطَّائِرَة",
    requires=["ضاع", "حقيبة", "مفقود", "لون", "حجم", "عنوان", "وصل"],
    cards=[
        card("Reporting a lost bag",
             "When your bag does not arrive, you report it at the lost-luggage desk. The verb ضَاعَ يَضِيع means “to be lost”; for a feminine noun: ضَاعَتْ. You describe the bag by its colour (لَوْن), size (حَجْم) and number (رَقْم). "
             "The clerk gives you a form (an اِسْتِمَارَة) and promises to call you.",
             tables=[table(["English", "Arabic"],
                           [["it was lost (f.)", "ضَاعَتْ"], ["lost-luggage desk", "مَكْتَب الْأَمْتِعَة الْمَفْقُودَة"], ["colour", "لَوْن"], ["size", "حَجْم"], ["number", "رَقْم"], ["address", "عُنْوَان"], ["form", "اِسْتِمَارَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("At the desk (invented)",
             "A passenger reports a lost bag.",
             examples=[
                 ex("ضَاعَتْ حَقِيبَتِي فِي الْمَطَار.", "My bag was lost at the airport.", "ضَاعَتْ"),
                 ex("لَمْ تَصِلْ حَقِيبَتِي مَعَ الطَّائِرَة.", "My bag did not arrive with the plane.", "لَمْ تَصِلْ"),
                 ex("حَقِيبَتِي كَبِيرَة وَلَوْنُهَا أَزْرَق.", "My bag is big and its colour is blue.", "وَلَوْنُهَا"),
                 ex("اِمْلَأْ هَذِهِ الِاسْتِمَارَة مِنْ فَضْلِكَ.", "Fill in this form, please.", "اِمْلَأْ"),
                 ex("اُكْتُبْ رَقْم الْحَقِيبَة وَعُنْوَانَكَ.", "Write the number of the bag and your address.", "اُكْتُبْ"),
                 ex("سَنُرْسِل الْحَقِيبَة إِلَى الْفُنْدُق.", "We will send the bag to the hotel.", "سَنُرْسِل"),
             ]),
    ],
    exercises=[
        M("What does ضَاعَتْ حَقِيبَتِي mean?", "My bag was lost", ["My bag is heavy", "My bag is new", "I found my bag"], "ضَاعَ = to be lost."),
        M("What does لَمْ تَصِلْ حَقِيبَتِي mean?", "My bag did not arrive", ["My bag will arrive", "My bag arrived", "I did not pack a bag"], "لَمْ + short present = did not."),
        M("What does لَوْن mean?", "colour", ["size", "number", "address"], "لَوْن = colour."),
        M("What does اِمْلَأْ هَذِهِ الِاسْتِمَارَة mean?", "Fill in this form", ["Read this letter", "Sign this ticket", "Open this bag"], "اِمْلَأْ = fill! (to one man)."),
        M("What does سَنُرْسِل الْحَقِيبَة إِلَى الْفُنْدُق mean?", "We will send the bag to the hotel", ["We sent the bag to the hotel", "We lost the bag in the hotel", "I will pay for the hotel"], "سَنُرْسِل = we will send."),
        M("Why is it ضَاعَتْ and not ضَاعَ?", "حَقِيبَة is feminine", ["the bag is big", "it is a command", "it is a plural"], "A feminine subject → ـَتْ."),
        F("ضَاعَتْ ___ فِي الْمَطَار.", "حَقِيبَتِي", ["فُنْدُقِي", "جَوَازِي"], "The lost thing is a bag.", tr="My bag was lost at the airport."),
        F("حَقِيبَتِي كَبِيرَة وَ___ أَزْرَق.", "لَوْنُهَا", ["لَوْنُهُ", "اِسْمُهَا"], "“its colour”, for a feminine bag: لَوْنُهَا.", tr="My bag is big and its colour is blue."),
        F("___ رَقْم الْحَقِيبَة وَعُنْوَانَكَ.", "اُكْتُبْ", ["اِكْتِبْ", "كَتَبَ"], "A command from كَتَبَ يَكْتُب: اُكْتُبْ.", tr="Write the number of the bag and your address.", lemma="كتب:imp:anta"),
    ],
    verify=(vv("كتب", "imp", anta="اُكْتُبْ") + vv("وصل", "jus", hiya="تَصِلْ")),
)

# ---------------------------------------------------------------------------- 369
L369 = lesson(
    "At customs: what do you declare?",
    "هَلْ مَعَكَ شَيْء لِلتَّصْرِيح؟ · عُمْلَة أَجْنَبِيَّة",
    requires=["جمرك", "صرح", "عملة", "هدية", "مبلغ", "جهاز", "حقيبة"],
    cards=[
        card("The customs desk",
             "At customs you may be asked whether you have anything to declare. The verb is صَرَّحَ (Measure II) and the noun is التَّصْرِيح. Typical things to declare are foreign currency (عُمْلَة أَجْنَبِيَّة), large sums of money (مَبْلَغ كَبِير), electronic devices (أَجْهِزَة إِلِكْتْرُونِيَّة) and gifts (هَدَايَا). "
             "Rules differ from country to country, so these lines are only examples.",
             tables=[table(["English", "Arabic"],
                           [["customs", "الْجُمْرُك"], ["to declare", "يُصَرِّح"], ["foreign currency", "عُمْلَة أَجْنَبِيَّة"], ["a large sum", "مَبْلَغ كَبِير"], ["electronic devices", "أَجْهِزَة إِلِكْتْرُونِيَّة"], ["gifts", "هَدَايَا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("The customs officer asks (invented)",
             "An officer and a traveller.",
             examples=[
                 ex("هَلْ مَعَكَ شَيْء لِلتَّصْرِيح؟", "Do you have anything to declare?", "لِلتَّصْرِيح"),
                 ex("لَا، مَعِي هَدَايَا صَغِيرَة فَقَط.", "No, I only have small gifts.", "هَدَايَا"),
                 ex("هَلْ مَعَكَ عُمْلَة أَجْنَبِيَّة؟", "Do you have foreign currency?", "عُمْلَة أَجْنَبِيَّة"),
                 ex("نَعَمْ، مَعِي مَبْلَغ صَغِير بِالدُّولَار.", "Yes, I have a small amount in dollars.", "مَبْلَغ"),
                 ex("اِفْتَحْ هَذِهِ الْحَقِيبَة مِنْ فَضْلِكَ.", "Open this bag, please.", "اِفْتَحْ"),
                 ex("اِمْلَأْ اِسْتِمَارَة الْجُمْرُك.", "Fill in the customs form.", "اِسْتِمَارَة الْجُمْرُك"),
             ]),
    ],
    exercises=[
        M("What does التَّصْرِيح mean here?", "declaring", ["booking", "searching", "paying"], "صَرَّحَ = to declare."),
        M("What does هَلْ مَعَكَ شَيْء لِلتَّصْرِيح؟ ask?", "Do you have anything to declare?", ["Do you have a ticket?", "Where is your hotel?", "How long will you stay?"], "لِلتَّصْرِيح = to declare."),
        M("What is عُمْلَة أَجْنَبِيَّة?", "foreign currency", ["foreign food", "a foreign language", "a foreign hotel"], "عُمْلَة = currency."),
        M("What does اِفْتَحْ هَذِهِ الْحَقِيبَة mean?", "Open this bag", ["Close this bag", "Carry this bag", "Lose this bag"], "اِفْتَحْ = open!"),
        M("What does مَعِي هَدَايَا صَغِيرَة mean?", "I have small gifts with me", ["I sent small gifts", "I need small gifts", "I lost the gifts"], "مَعِي = with me, I have."),
        M("What does اِسْتِمَارَة الْجُمْرُك mean?", "the customs form", ["the hotel form", "the bank form", "the school form"], "اِسْتِمَارَة = form."),
        F("هَلْ مَعَكَ ___ أَجْنَبِيَّة؟", "عُمْلَة", ["هَدِيَّة", "حَقِيبَة"], "Foreign currency is عُمْلَة أَجْنَبِيَّة.", tr="Do you have foreign currency?"),
        F("اِمْلَأْ ___ الْجُمْرُك.", "اِسْتِمَارَة", ["جَوَاز", "فُنْدُق"], "The form.", tr="Fill in the customs form."),
        F("مَعِي ___ صَغِيرَة فَقَط.", "هَدَايَا", ["هَدِيَّة", "هَدَايَا كَثِيرَة"], "Plural of هَدِيَّة (a plural of things → feminine singular adjective صَغِيرَة).", tr="I only have small gifts."),
    ],
    verify=vv("فتح", "imp", anta="اِفْتَحْ"),
)

# ---------------------------------------------------------------------------- 370
L370 = lesson(
    "At the bank: opening an account",
    "أُرِيد أَنْ أَفْتَح حِسَابًا · بِطَاقَة الصَّرَّاف الْآلِيّ",
    requires=["بنك", "حساب", "بطاقة", "فتح", "جواز", "عنوان", "آلي"],
    cards=[
        card("Accounts and cards",
             "A bank is بَنْك or مَصْرِف. You open an account with the verb فَتَحَ: أَفْتَح حِسَابًا. A savings account is حِسَاب التَّوْفِير and a checking account is الْحِسَاب الْجَارِي. "
             "A cash machine is الصَّرَّاف الْآلِيّ, so the card for it is بِطَاقَة الصَّرَّاف الْآلِيّ. Banks have different conditions, so ask before you sign.",
             tables=[table(["English", "Arabic"],
                           [["bank", "بَنْك"], ["account", "حِسَاب"], ["savings account", "حِسَاب التَّوْفِير"], ["checking account", "الْحِسَاب الْجَارِي"], ["joint account", "حِسَاب مُشْتَرَك"], ["cash machine", "الصَّرَّاف الْآلِيّ"], ["card", "بِطَاقَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("At the bank (invented)",
             "A customer talks to a clerk.",
             examples=[
                 ex("أُرِيد أَنْ أَفْتَح حِسَابًا فِي الْبَنْك.", "I want to open an account at the bank.", "أَفْتَح"),
                 ex("مَا الْفَرْق بَيْن حِسَاب التَّوْفِير وَالْحِسَاب الْجَارِي؟", "What is the difference between a savings account and a checking account?", "الْفَرْق"),
                 ex("أُرِيد بِطَاقَة لِلصَّرَّاف الْآلِيّ.", "I want a card for the cash machine.", "بِطَاقَة"),
                 ex("اُكْتُبِ اِسْمَكَ وَعُنْوَانَكَ فِي الِاسْتِمَارَة.", "Write your name and address on the form.", "اُكْتُبِ"),
                 ex("تَحْتَاج إِلَى جَوَاز السَّفَر.", "You need your passport.", "تَحْتَاج"),
                 ex("اِسْأَلِ الْبَنْك عَنْ شُرُوط الْحِسَاب.", "Ask the bank about the conditions of the account.", "اِسْأَلِ"),
             ]),
    ],
    exercises=[
        M("What does أُرِيد أَنْ أَفْتَح حِسَابًا mean?", "I want to open an account", ["I want to close an account", "I want to pay a bill", "I want to buy a ticket"], "فَتَحَ = to open."),
        M("What is حِسَاب التَّوْفِير?", "a savings account", ["a joint account", "a card", "a form"], "تَوْفِير = saving."),
        M("What is الصَّرَّاف الْآلِيّ?", "the cash machine", ["the bank clerk", "the passport", "the form"], "آلِيّ = automatic."),
        M("What does تَحْتَاج إِلَى جَوَاز السَّفَر mean?", "You need your passport", ["You lost your passport", "You have a passport", "You gave your passport"], "تَحْتَاج إِلَى = you need."),
        M("What does اِسْأَلِ الْبَنْك mean?", "Ask the bank", ["Pay the bank", "Visit the bank", "Call the bank tomorrow"], "اِسْأَلْ = ask! (command)."),
        M("What does شُرُوط الْحِسَاب mean?", "the conditions of the account", ["the number of the account", "the owner of the account", "the end of the account"], "شُرُوط = conditions."),
        F("أُرِيد أَنْ ___ حِسَابًا فِي الْبَنْك.", "أَفْتَح", ["فَتَحْتُ", "يَفْتَح"], "After أَنْ with أَنَا: أَفْتَح.", tr="I want to open an account at the bank.", lemma="فتح:sub:ana"),
        F("أُرِيد بِطَاقَة لِلصَّرَّاف ___.", "الْآلِيّ", ["الْجَارِي", "الْمُشْتَرَك"], "The cash machine is الصَّرَّاف الْآلِيّ.", tr="I want a card for the cash machine."),
        F("___ اِسْمَكَ وَعُنْوَانَكَ فِي الِاسْتِمَارَة.", "اُكْتُبِ", ["كَتَبَ", "يَكْتُب"], "A command: اُكْتُبِ (a helping kasra before the hamzat al-waṣl of اِسْمَكَ).", tr="Write your name and address on the form."),
    ],
    verify=(vv("فتح", "sub", ana="أَفْتَح") + vv("كتب", "imp", anta="اُكْتُبْ")),
)

# ---------------------------------------------------------------------------- 371
L371 = lesson(
    "Deposits, withdrawals and transfers",
    "أَسْحَب · أُحَوِّل · رَصِيدِي قَلِيل",
    requires=["سحب", "حول", "رصيد", "فائدة", "مال", "حساب", "أخ"],
    cards=[
        card("Money and your account",
             "To withdraw money is سَحَبَ يَسْحَب, to transfer is حَوَّلَ يُحَوِّل (Measure II), and the money in your account is رَصِيد (“balance”). A fee is رُسُوم. Interest is فَائِدَة. "
             "Some banks that follow Islamic principles do not use interest in the usual way, so it is wise to ask the bank how its accounts work.",
             tables=[table(["English", "Arabic"],
                           [["balance", "رَصِيد"], ["to withdraw", "يَسْحَب"], ["to transfer", "يُحَوِّل"], ["interest", "فَائِدَة"], ["money", "مَال"], ["a fee", "رُسُوم"], ["transfer (noun)", "تَحْوِيل"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Typical sentences (invented)",
             "Customers and a clerk use these lines.",
             examples=[
                 ex("أُرِيد أَنْ أَسْحَب خَمْسِين دِينَارًا.", "I want to withdraw fifty dinars.", "أَسْحَب"),
                 ex("رَصِيدِي فِي الْحِسَاب قَلِيل.", "My balance in the account is low.", "رَصِيدِي"),
                 ex("أُرِيد أَنْ أُحَوِّل الْمَال إِلَى حِسَاب أَخِي.", "I want to transfer the money to my brother’s account.", "أُحَوِّل"),
                 ex("هَلْ يَدْفَع الْبَنْك فَائِدَة؟", "Does the bank pay interest?", "فَائِدَة"),
                 ex("هُنَاكَ رُسُوم عَلَى كُلّ تَحْوِيل.", "There is a fee on every transfer.", "رُسُوم"),
                 ex("سَحَبْتُ الْمَال أَمْسِ.", "I withdrew the money yesterday.", "سَحَبْتُ"),
             ]),
    ],
    exercises=[
        M("What does رَصِيد mean?", "balance", ["fee", "card", "form"], "رَصِيد = the amount in the account."),
        M("What does أَسْحَب mean?", "I withdraw", ["I deposit", "I transfer", "I count"], "سَحَبَ = to withdraw."),
        M("What does حَوَّلَ mean?", "he transferred", ["he withdrew", "he opened", "he closed"], "Measure II: حَوَّلَ = transferred."),
        M("What does رُسُوم mean?", "fees", ["gifts", "cards", "letters"], "رُسُوم = fees."),
        M("What does رَصِيدِي قَلِيل mean?", "My balance is low", ["My balance is high", "My card is lost", "My account is closed"], "قَلِيل = little."),
        M("What does هَلْ يَدْفَع الْبَنْك فَائِدَة؟ ask?", "Does the bank pay interest?", ["Does the bank open today?", "Where is the bank?", "Who is the clerk?"], "فَائِدَة = interest."),
        F("أُرِيد أَنْ ___ خَمْسِين دِينَارًا.", "أَسْحَب", ["سَحَبْتُ", "يَسْحَب"], "After أَنْ: أَسْحَب.", tr="I want to withdraw fifty dinars.", lemma="سحب:sub:ana"),
        F("أُرِيد أَنْ ___ الْمَال إِلَى حِسَاب أَخِي.", "أُحَوِّل", ["حَوَّلْتُ", "يُحَوِّل"], "Measure II after أَنْ with أَنَا: أُحَوِّل.", tr="I want to transfer the money to my brother’s account.", lemma="حول#2:sub:ana"),
        F("هُنَاكَ ___ عَلَى كُلّ تَحْوِيل.", "رُسُوم", ["رَصِيد", "جَوَاز"], "A fee on each transfer.", tr="There is a fee on every transfer."),
    ],
    verify=(vv("سحب", "sub", ana="أَسْحَب") + vv("حول#2", "sub", ana="أُحَوِّل") + vv("سحب", "past", ana="سَحَبْتُ")),
)

# ---------------------------------------------------------------------------- 372
L372 = lesson(
    "A letter of complaint",
    "أَكْتُب إِلَيْكُمْ بِخُصُوص حَقِيبَتِي · أَرْجُو الرَّدّ",
    requires=["خطاب", "شكوى", "رد", "تعويض", "شكر", "ضاع", "وصل"],
    cards=[
        card("The parts of a formal letter",
             "A letter of complaint is formal and polite. It usually has a greeting, the reason for writing, what went wrong, what you ask for, and a closing. Here is an invented letter to an airline about a lost bag.",
             examples=[
                 ex("السَّيِّد الْمُحْتَرَم، تَحِيَّة طَيِّبَة وَبَعْد،", "Dear Sir, kind greetings, and then:", "السَّيِّد الْمُحْتَرَم"),
                 ex("أَكْتُب إِلَيْكُمْ بِخُصُوص حَقِيبَتِي الَّتِي ضَاعَتْ.", "I am writing to you about my bag, which was lost.", "بِخُصُوص"),
                 ex("وَصَلْتُ إِلَى الْمَطَار يَوْم الْأَحَد، وَلَمْ تَصِلْ حَقِيبَتِي.", "I arrived at the airport on Sunday, and my bag did not arrive.", "لَمْ تَصِلْ"),
                 ex("أَطْلُب مِنْكُمْ تَعْوِيضًا عَنْ هَذِهِ الْمُشْكِلَة.", "I ask you for compensation for this problem.", "أَطْلُب"),
                 ex("أَرْجُو الرَّدّ فِي أَقْرَب وَقْت.", "I hope for a reply as soon as possible.", "أَرْجُو"),
                 ex("مَعَ الشُّكْر، سَامِي.", "With thanks, Sami.", "مَعَ الشُّكْر"),
             ]),
    ],
    exercises=[
        M("What does بِخُصُوص mean?", "about, concerning", ["without", "after", "against"], "بِخُصُوص = regarding."),
        M("What does أَكْتُب إِلَيْكُمْ mean?", "I am writing to you (all)", ["I received from you", "I read your letter", "You wrote to me"], "إِلَيْكُمْ = to you (plural)."),
        M("What does أَطْلُب تَعْوِيضًا mean?", "I ask for compensation", ["I give a gift", "I pay a fee", "I open an account"], "تَعْوِيض = compensation."),
        M("What does أَرْجُو الرَّدّ mean?", "I hope for a reply", ["I refuse to reply", "I have replied", "I will travel"], "أَرْجُو = I hope."),
        M("Which closing fits the end of a formal letter?", "مَعَ الشُّكْر", ["أَيْنَ الْمَطَار", "مَا اِسْمُكَ", "هَلْ وَصَلْتَ"], "مَعَ الشُّكْر = with thanks."),
        M("What does الَّتِي ضَاعَتْ refer to?", "the bag", ["the airport", "the airline", "Sunday"], "الَّتِي agrees with the feminine noun حَقِيبَتِي."),
        F("أَكْتُب إِلَيْكُمْ ___ حَقِيبَتِي.", "بِخُصُوص", ["قَبْل", "تَحْت"], "“about”.", tr="I am writing to you about my bag."),
        F("أَطْلُب مِنْكُمْ ___ عَنْ هَذِهِ الْمُشْكِلَة.", "تَعْوِيضًا", ["تَذْكِرَة", "فَائِدَة"], "Compensation for a problem.", tr="I ask you for compensation for this problem."),
        F("أَرْجُو ___ فِي أَقْرَب وَقْت.", "الرَّدّ", ["الْحَجْز", "الْخَصْم"], "A reply.", tr="I hope for a reply as soon as possible."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 373
L373 = lesson(
    "Review: chapter 21",
    "وَ · فَ · ثُمَّ · أَوْ · أَكْثَر اِزْدِحَامًا · الْأَمْن وَالْمَصْرِف",
    requires=["رحلة", "حجز", "أمن", "حقيبة", "بنك", "حساب", "أكثر", "أقل"],
    cards=[
        card("What the unit taught",
             "Conjunctions join equal parts, and the second part copies the case of the first. وَ adds, فَ follows at once, ثُمَّ follows after a gap, and أَوْ gives a choice. "
             "Comparatives without a short أَفْعَل adjective use أَكْثَر or أَقَلّ with a verbal noun in the accusative: أَكْثَر اِزْدِحَامًا; with ال they are superlatives.",
             tables=[table(["Topic", "Example", "English"],
                           [["booking", "أُرِيد أَنْ أَحْجِز رِحْلَة", "I want to book a trip"], ["and then at once", "وَصَلْنَا فَدَخَلْنَا", "We arrived and at once went in"], ["then / or", "ثُمَّ · أَوْ", "then · or"],
                            ["comparing", "أَقَلّ سِعْرًا مِنْ", "lower in price than"], ["security", "أَبْرِزْ جَوَاز السَّفَر", "Show your passport"], ["lost bag", "ضَاعَتْ حَقِيبَتِي", "My bag was lost"], ["bank", "أُرِيد أَنْ أَسْحَب الْمَال", "I want to withdraw the money"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A short summary (invented)",
             "Read the lines, which use everything from the unit.",
             examples=[
                 ex("حَجَزْنَا الرِّحْلَة ثُمَّ دَفَعْنَا الْمَبْلَغ فِي الْبَنْك.", "We booked the trip and then paid the amount at the bank.", "ثُمَّ"),
                 ex("وَصَلْنَا إِلَى الْمَطَار فَأَبْرَزْنَا جَوَازَاتِ السَّفَر.", "We arrived at the airport and at once showed our passports.", "فَأَبْرَزْنَا"),
                 ex("هَلْ تُفَضِّلُونَ الْقِطَار أَوِ الطَّائِرَة؟", "Do you prefer the train or the plane?", "أَوِ"),
                 ex("الطَّائِرَة أَكْثَر رَاحَةً وَأَقَلّ اِزْدِحَامًا.", "The plane is more comfortable and less crowded.", "أَقَلّ اِزْدِحَامًا"),
                 ex("ضَاعَتْ حَقِيبَتِي فَكَتَبْتُ خِطَابًا إِلَى الشَّرِكَة.", "My bag was lost, so I wrote a letter to the company.", "فَكَتَبْتُ"),
                 ex("هَذِهِ الشَّرِكَة هِيَ الْأَكْثَر نَجَاحًا.", "This company is the most successful.", "الْأَكْثَر نَجَاحًا"),
             ]),
    ],
    exercises=[
        M("Which conjunction means “and then at once”?", "فَ", ["ثُمَّ", "أَوْ", "وَ"], "فَ = immediate sequence."),
        M("Which conjunction gives a choice?", "أَوْ", ["فَ", "ثُمَّ", "وَ"], "أَوْ = or."),
        M("What does الْأَكْثَر نَجَاحًا mean?", "the most successful", ["less successful", "more successful", "successful"], "ال makes the superlative."),
        M("What does أَقَلّ اِزْدِحَامًا mean?", "less crowded", ["more crowded", "faster", "cheaper"], "أَقَلّ = less."),
        M("What does أَبْرِزْ جَوَاز السَّفَر mean?", "Show your passport", ["Lose your passport", "Write your passport", "Buy a passport"], "أَبْرِزْ = show!"),
        M("Why do both nouns in مَعَ الْمُدِيرِ وَالْمُوَظَّفِ end in a kasra?", "the second noun copies the case of the first", ["it is always a kasra", "it is a plural", "it is a question"], "Same case after a conjunction."),
        F("وَصَلْنَا إِلَى الْمَطَار ___ أَبْرَزْنَا جَوَازَاتِ السَّفَر.", "فَ", ["أَوْ", "لَمْ"], "At once: فَ (written attached).", tr="We arrived at the airport and at once showed our passports."),
        F("هَلْ تُفَضِّلُونَ الْقِطَار ___ الطَّائِرَة؟", "أَوِ", ["ثُمَّ", "فَ"], "A choice, with a helping vowel before ال.", tr="Do you prefer the train or the plane?"),
        F("الطَّائِرَة أَكْثَر رَاحَةً وَأَقَلّ ___.", "اِزْدِحَامًا", ["اِزْدِحَام", "مُزْدَحِم"], "A verbal noun with tanwīn.", tr="The plane is more comfortable and less crowded."),
    ],
    verify=(),
)


UNIT = unit("السَّفَر وَالْمَصْرِف: trip planning, conjunctions, security and banking", [L355, L356, L357, L358, L359, L360, L361, L362, L363, L364, L365, L366, L367, L368, L369, L370, L371, L372, L373])
