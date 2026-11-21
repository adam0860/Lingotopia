"""Unit 18 (chapter 16): the airport and flights, verbs before plural things, assimilated verbs, instructions."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 261
L261 = lesson(
    "At the airport: places, people, papers",
    "مَطَار · طَائِرَة · رِحْلَة · تَذْكِرَة · جَوَاز سَفَر",
    requires=["مطار", "طائرة", "رحلة", "تذكرة", "جواز", "سفر", "حقيبة", "بوابة", "صالة", "راكب", "موظف"],
    cards=[
        card("Words you will see and hear",
             "At an airport you meet a small set of words again and again. A passenger is رَاكِب (plural رُكَّاب). The passport is جَوَاز سَفَر, literally “a pass of travel”.",
             tables=[table(["English", "Arabic"],
                           [["airport", "مَطَار"], ["plane", "طَائِرَة"], ["flight, trip", "رِحْلَة"], ["ticket", "تَذْكِرَة"], ["passport", "جَوَاز سَفَر"],
                            ["bag", "حَقِيبَة"], ["gate", "بَوَّابَة"], ["hall", "صَالَة"], ["passenger", "رَاكِب"], ["employee, official", "مُوَظَّف"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Short sentences",
             "These sentences use only words and patterns you already know.",
             examples=[
                 ex("أَنَا فِي الْمَطَار الْآن.", "I am at the airport now.", "الْمَطَار"),
                 ex("الطَّائِرَة كَبِيرَة وَجَدِيدَة.", "The plane is big and new.", "الطَّائِرَة"),
                 ex("مَعِي حَقِيبَة صَغِيرَة وَجَوَاز سَفَر.", "I have a small bag and a passport.", "جَوَاز سَفَر"),
                 ex("الْمُوَظَّف يَطْلُب الْجَوَاز وَالتَّذْكِرَة.", "The official asks for the passport and the ticket.", "الْمُوَظَّف"),
                 ex("الرُّكَّاب فِي صَالَة الْمُغَادَرَة.", "The passengers are in the departure hall.", "صَالَة"),
                 ex("أَيْنَ بَوَّابَة رِحْلَتِي؟", "Where is the gate for my flight?", "بَوَّابَة"),
             ]),
    ],
    exercises=[
        M("Which word means “passport”?", "جَوَاز سَفَر", ["تَذْكِرَة", "حَقِيبَة", "بَوَّابَة"], "جَوَاز سَفَر = passport."),
        M("Which word means “gate”?", "بَوَّابَة", ["صَالَة", "طَائِرَة", "مَطَار"], "بَوَّابَة = gate."),
        M("Which word means “passenger”?", "رَاكِب", ["مُوَظَّف", "رِحْلَة", "حَقِيبَة"], "رَاكِب = passenger."),
        M("What does الْمُوَظَّف يَطْلُب الْجَوَاز وَالتَّذْكِرَة mean?", "The official asks for the passport and the ticket", ["The official sells the passport and the ticket", "The passenger loses the passport and the ticket", "The official opens the bag"], "يَطْلُب = asks for."),
        M("What does مَعِي حَقِيبَة صَغِيرَة mean?", "I have a small bag", ["I want a small plane", "I am in a small hall", "I see a small gate"], "مَعِي = with me, I have."),
        M("What does أَيْنَ بَوَّابَة رِحْلَتِي؟ ask?", "Where is the gate for my flight?", ["When does my flight leave?", "Where is my bag?", "Who is the passenger?"], "أَيْنَ = where."),
        F("الرُّكَّاب فِي ___ الْمُغَادَرَة.", "صَالَة", ["حَقِيبَة", "تَذْكِرَة", "رِحْلَة"], "A hall, not a bag.", tr="The passengers are in the departure hall."),
        F("أَنَا فِي ___ الْآن.", "الْمَطَار", ["الْجَوَاز", "الْحَقِيبَة", "التَّذْكِرَة"], "You are in a place.", tr="I am at the airport now."),
        F("الْمُوَظَّف يَطْلُب الْجَوَاز وَ___.", "التَّذْكِرَة", ["الْمَطَار", "الْبَوَّابَة", "الْمُوَظَّف"], "Papers belong together.", tr="The official asks for the passport and the ticket."),
    ],
    verify=vw("مَطَار", "الْمَطَار", "طَائِرَة", "الطَّائِرَة", "رِحْلَة", "رِحْلَتِي", "تَذْكِرَة", "التَّذْكِرَة", "جَوَاز", "الْجَوَاز", "سَفَر", "حَقِيبَة", "بَوَّابَة", "صَالَة", "رَاكِب", "الرُّكَّاب", "الْمُوَظَّف", "مُوَظَّف", "الْمُغَادَرَة", "يَطْلُب", "مَعِي"),
)

# ---------------------------------------------------------------------------- 262
L262 = lesson(
    "Flights: leaving, arriving, delays",
    "تُغَادِر الرِّحْلَة فِي الثَّامِنَة · تَصِل فِي الْعَاشِرَة",
    requires=["مغادرة", "وصول", "إقلاع", "هبوط", "تأخير", "مباشر", "رحلة", "وصل", "غادر"],
    cards=[
        card("Departure and arrival",
             "Flights are announced with a few nouns: مُغَادَرَة (departure), وُصُول (arrival), إِقْلَاع (take-off), هُبُوط (landing) and تَأْخِير (delay). "
             "A flight without a stop is a رِحْلَة مُبَاشِرَة. The verbs are تُغَادِر (it leaves) and تَصِل (it arrives); the subject رِحْلَة is feminine, so the verb starts with تـ.",
             tables=[table(["English", "Arabic"],
                           [["departure", "مُغَادَرَة"], ["arrival", "وُصُول"], ["take-off", "إِقْلَاع"], ["landing", "هُبُوط"], ["delay", "تَأْخِير"],
                            ["direct flight", "رِحْلَة مُبَاشِرَة"], ["it leaves (the flight)", "تُغَادِر"], ["it arrives (the flight)", "تَصِل"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Reading a flight board",
             "The board gives the time after فِي. Add صَبَاحًا (in the morning) or مَسَاءً (in the evening) when the hour could be either.",
             examples=[
                 ex("تُغَادِر الرِّحْلَة فِي الثَّامِنَة صَبَاحًا.", "The flight leaves at eight in the morning.", "تُغَادِر"),
                 ex("تَصِل الرِّحْلَة فِي الْعَاشِرَة مَسَاءً.", "The flight arrives at ten in the evening.", "تَصِل"),
                 ex("هَذِهِ رِحْلَة مُبَاشِرَة إِلَى الْقَاهِرَة.", "This is a direct flight to Cairo.", "مُبَاشِرَة"),
                 ex("هُنَاك تَأْخِير فِي الرِّحْلَة.", "There is a delay in the flight.", "تَأْخِير"),
                 ex("رَقْم الْبَوَّابَة سَبْعَة.", "The gate number is seven.", "رَقْم"),
                 ex("الْإِقْلَاع فِي الْوَاحِدَة وَالْهُبُوط فِي الرَّابِعَة.", "The take-off is at one and the landing at four.", "الْهُبُوط"),
             ]),
    ],
    exercises=[
        M("Which word means “delay”?", "تَأْخِير", ["إِقْلَاع", "وُصُول", "مُغَادَرَة"], "تَأْخِير = delay."),
        M("Which word means “landing”?", "هُبُوط", ["إِقْلَاع", "مُغَادَرَة", "رِحْلَة"], "هُبُوط = landing."),
        M("What is a رِحْلَة مُبَاشِرَة?", "a direct flight", ["a late flight", "a cancelled flight", "a night flight"], "مُبَاشِرَة = direct."),
        M("What does تُغَادِر الرِّحْلَة فِي الثَّامِنَة صَبَاحًا mean?", "The flight leaves at eight in the morning", ["The flight arrives at eight in the evening", "The flight is late by eight hours", "The flight has eight seats"], "تُغَادِر = it leaves."),
        M("Why does تَصِل start with تـ in تَصِل الرِّحْلَة؟", "رِحْلَة is feminine", ["رِحْلَة is plural", "it is a question", "it is a command"], "A feminine subject gives تـ."),
        M("What does هُنَاك تَأْخِير فِي الرِّحْلَة mean?", "There is a delay in the flight", ["The flight is direct", "The flight has landed", "The flight is cheap"], "هُنَاك = there is."),
        F("___ الرِّحْلَة فِي الْعَاشِرَة مَسَاءً.", "تَصِل", ["يَصِل", "أَصِل", "نَصِل"], "A feminine subject: تـ.", tr="The flight arrives at ten in the evening.", lemma="وصل:pres:hiya"),
        F("هَذِهِ رِحْلَة ___ إِلَى الْقَاهِرَة.", "مُبَاشِرَة", ["مُبَاشِر", "مُبَاشِرُون", "مُبَاشِرَات"], "Feminine singular, like رِحْلَة.", tr="This is a direct flight to Cairo."),
        F("الْإِقْلَاع فِي الْوَاحِدَة وَ___ فِي الرَّابِعَة.", "الْهُبُوط", ["التَّأْخِير", "الْجَوَاز", "الْمُوَظَّف"], "Take-off, then landing.", tr="The take-off is at one and the landing at four."),
    ],
    verify=(vv("وصل", "pres", hiya="تَصِل", huwa="يَصِل", ana="أَصِل", nahnu="نَصِل")
            + vv("غدر#3", "pres", hiya="تُغَادِر")
            + vw("مُغَادَرَة", "وُصُول", "إِقْلَاع", "هُبُوط", "تَأْخِير", "مُبَاشِرَة", "صَبَاحًا", "مَسَاءً", "الثَّامِنَة", "الْعَاشِرَة", "الْوَاحِدَة", "الرَّابِعَة", "الْقَاهِرَة", "هُنَاك", "رَقْم", "سَبْعَة", "الْإِقْلَاع", "الْهُبُوط", "التَّأْخِير")),
)

# ---------------------------------------------------------------------------- 263
L263 = lesson(
    "Booking a ticket",
    "أُرِيد أَنْ أَحْجِز تَذْكِرَة ذَهَاب وَإِيَاب",
    requires=["حجز", "تذكرة", "ذهاب", "درجة", "سعر", "مقعد", "رحلة", "أول", "فقط"],
    cards=[
        card("One way or return",
             "To book is حَجَزَ (he booked), present يَحْجِز: أُرِيد أَنْ أَحْجِز تَذْكِرَة (I want to book a ticket). "
             "A one-way ticket is تَذْكِرَة ذَهَاب and a return ticket is تَذْكِرَة ذَهَاب وَإِيَاب. The class of seat is دَرَجَة: الدَّرَجَة الْأُولَى is first class.",
             tables=[table(["English", "Arabic"],
                           [["I want to book a ticket", "أُرِيد أَنْ أَحْجِز تَذْكِرَة"], ["one-way ticket", "تَذْكِرَة ذَهَاب"], ["return ticket", "تَذْكِرَة ذَهَاب وَإِيَاب"],
                            ["first class", "الدَّرَجَة الْأُولَى"], ["seat", "مَقْعَد"], ["price", "سِعْر"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("At the booking desk",
             "These are the questions and answers you need most.",
             examples=[
                 ex("أُرِيد أَنْ أَحْجِز تَذْكِرَة إِلَى عَمَّان.", "I want to book a ticket to Amman.", "أَحْجِز"),
                 ex("هَلْ تُرِيد ذَهَابًا فَقَط؟", "Do you want to go one way only?", "فَقَط"),
                 ex("لَا، أُرِيد تَذْكِرَة ذَهَاب وَإِيَاب.", "No, I want a return ticket.", "إِيَاب"),
                 ex("كَمْ سِعْر التَّذْكِرَة؟", "How much is the ticket?", "سِعْر"),
                 ex("هَلْ عِنْدَكُمْ مَقْعَد فِي الدَّرَجَة الْأُولَى؟", "Do you have a seat in first class?", "الدَّرَجَة الْأُولَى"),
                 ex("حَجَزْتُ مَقْعَدًا عِنْدَ النَّافِذَة.", "I booked a seat by the window.", "حَجَزْتُ"),
             ]),
    ],
    exercises=[
        M("What does يَحْجِز mean?", "he books", ["he cancels", "he pays", "he flies"], "حَجَزَ = to book."),
        M("Which is a return ticket?", "تَذْكِرَة ذَهَاب وَإِيَاب", ["تَذْكِرَة ذَهَاب", "تَذْكِرَة مَجَّانِيَّة", "تَذْكِرَة الْمَطَار"], "ذَهَاب وَإِيَاب = going and coming back."),
        M("Which word means “price”?", "سِعْر", ["مَقْعَد", "دَرَجَة", "رِحْلَة"], "سِعْر = price."),
        M("What does كَمْ سِعْر التَّذْكِرَة؟ ask?", "How much is the ticket?", ["When is the ticket?", "Where is the ticket?", "Whose is the ticket?"], "كَمْ = how much."),
        M("What does حَجَزْتُ مَقْعَدًا عِنْدَ النَّافِذَة mean?", "I booked a seat by the window", ["I closed the window", "I lost my seat", "I paid for a window"], "حَجَزْتُ = I booked."),
        M("What is الدَّرَجَة الْأُولَى?", "first class", ["last class", "second floor", "the first flight"], "أُولَى = first."),
        F("أُرِيد أَنْ ___ تَذْكِرَة إِلَى عَمَّان.", "أَحْجِز", ["يَحْجِز", "تَحْجِز", "نَحْجِز"], "I want to book.", tr="I want to book a ticket to Amman.", lemma="حجز:pres:ana"),
        F("كَمْ ___ التَّذْكِرَة؟", "سِعْر", ["مَقْعَد", "بَوَّابَة", "رَاكِب"], "Asking about the price.", tr="How much is the ticket?"),
        F("هَلْ عِنْدَكُمْ ___ فِي الدَّرَجَة الْأُولَى؟", "مَقْعَد", ["جَوَاز", "مَطَار", "حَقِيبَة"], "A seat in a class.", tr="Do you have a seat in first class?"),
    ],
    verify=(vv("حجز", "pres", ana="أَحْجِز", huwa="يَحْجِز") + vv("حجز", "past", ana="حَجَزْتُ")
            + vw("أَحْجِز", "يَحْجِز", "حَجَزْتُ", "عَمَّان", "ذَهَاب", "ذَهَابًا", "إِيَاب", "فَقَط", "سِعْر", "مَقْعَد", "مَقْعَدًا", "الدَّرَجَة", "الْأُولَى", "عِنْدَكُمْ", "النَّافِذَة", "مَجَّانِيَّة", "تُرِيد")),
)

# ---------------------------------------------------------------------------- 264
L264 = lesson(
    "A verb before things in the plural",
    "تَصِل الرِّحْلَات · تُغَادِر الطَّائِرَات",
    requires=["رحلة", "طائرة", "حقيبة", "وصل", "بدأ", "غادر", "بوابة", "مطار", "راكب"],
    cards=[
        card("The rule",
             "You already know that a verb at the start of a sentence agrees with its subject in gender only and stays singular, even before a dual or plural subject: وَصَلَ الرُّكَّاب (the passengers arrived). "
             "When the subject is a plural of things (planes, flights, bags, and also animals), the verb is feminine singular, however many there are.",
             tables=[table(["Subject", "Verb", "Sentence"],
                           [["men or mixed groups", "masculine singular", "يَصِل الرُّكَّاب"], ["things (plural)", "feminine singular", "تَصِل الرِّحْلَات"],
                            ["men or mixed groups", "masculine singular", "يُغَادِر الرُّكَّاب"], ["things (plural)", "feminine singular", "تُغَادِر الطَّائِرَات"]],
                           say=[2], tlit=[2], gloss=False)]),
        card("Examples",
             "Notice that the verb starts with تـ before these plurals: رِحْلَات (flights), طَائِرَات (planes), حَقَائِب (bags). The same goes for the past: وَصَلَتِ الرِّحْلَات.",
             examples=[
                 ex("تَصِل الرِّحْلَات مِنَ الْقَاهِرَة كُلّ يَوْم.", "Flights arrive from Cairo every day.", "تَصِل"),
                 ex("تُغَادِر الطَّائِرَات الْمَطَار فِي الصَّبَاح.", "The planes leave the airport in the morning.", "تُغَادِر"),
                 ex("وَصَلَتِ الْحَقَائِب فِي وَقْتِهَا.", "The bags arrived on time.", "وَصَلَتِ"),
                 ex("تَبْدَأ الرِّحْلَات إِلَى عَمَّان فِي الْخَامِسَة.", "The flights to Amman begin at five.", "تَبْدَأ"),
                 ex("يَصِل الرُّكَّاب إِلَى الْبَوَّابَة.", "The passengers arrive at the gate.", "يَصِل"),
                 ex("تَقِف الطَّائِرَات قُرْب الْبَوَّابَات.", "The planes stand near the gates.", "تَقِف"),
             ]),
    ],
    exercises=[
        M("Which verb fits: ___ الرِّحْلَات مِنَ الْقَاهِرَة؟", "تَصِل", ["يَصِل", "أَصِل", "نَصِل"], "Things in the plural → feminine singular."),
        M("Which verb fits: ___ الرُّكَّاب إِلَى الْبَوَّابَة؟", "يَصِل", ["تَصِل", "أَصِل", "نَصِل"], "A group of men or a mixed group → masculine singular."),
        M("Which is correct for “The planes leave”?", "تُغَادِر الطَّائِرَات", ["يُغَادِر الطَّائِرَات", "تُغَادِرُون الطَّائِرَات", "أُغَادِر الطَّائِرَات"], "Planes are things."),
        M("What does وَصَلَتِ الْحَقَائِب فِي وَقْتِهَا mean?", "The bags arrived on time", ["The bags were lost", "The bags are heavy", "The bags left early"], "وَصَلَتْ = she/it arrived."),
        M("What does تَبْدَأ الرِّحْلَات فِي الْخَامِسَة mean?", "The flights begin at five", ["The flights end at five", "The flight is number five", "The flights are five"], "تَبْدَأ = begins."),
        M("Which noun is a plural of things?", "الْحَقَائِب", ["الرُّكَّاب", "الْمُوَظَّف", "الْمُوَظَّفُون"], "Bags are things; the others are people."),
        F("___ الطَّائِرَات قُرْب الْبَوَّابَات.", "تَقِف", ["يَقِف", "أَقِف", "نَقِف"], "Things → feminine singular.", tr="The planes stand near the gates.", lemma="وقف:pres:hiya"),
        F("___ الرِّحْلَات إِلَى عَمَّان فِي الْخَامِسَة.", "تَبْدَأ", ["يَبْدَأ", "أَبْدَأ", "نَبْدَأ"], "Flights are things.", tr="The flights to Amman begin at five.", lemma="بدأ:pres:hiya"),
        F("وَصَلَ ___ إِلَى الْمَطَار.", "الرُّكَّاب", ["الرِّحْلَات", "الْحَقَائِب", "الطَّائِرَات"], "A masculine singular verb goes with people.", tr="The passengers arrived at the airport."),
    ],
    verify=(vv("وصل", "pres", huwa="يَصِل", hiya="تَصِل") + vv("وقف", "pres", hiya="تَقِف") + vv("بدأ", "pres", hiya="تَبْدَأ")
            + vw("الرِّحْلَات", "الطَّائِرَات", "الْحَقَائِب", "الْبَوَّابَات", "وَصَلَتِ", "وَصَلَ", "الرُّكَّاب", "الْوَقْت", "الْخَامِسَة", "تَقِف", "قُرْب", "الْمُوَظَّفُون", "يُغَادِر", "تُغَادِرُون", "أُغَادِر")),
)

# ---------------------------------------------------------------------------- 265
L265 = lesson(
    "Airline adverts",
    "تُقَدِّم الشَّرِكَة رِحْلَات يَوْمِيَّة",
    requires=["شركة", "يومي", "قدم", "رحلة", "طائرة", "مقعد", "سعر", "سفر", "سياحة"],
    cards=[
        card("What adverts promise",
             "Adverts are full of verbs in front of plural things. Read the pattern: the verb is feminine singular, the plural noun follows it, and any adjective after the plural noun is feminine singular too (رِحْلَات يَوْمِيَّة, daily flights).",
             tables=[table(["English", "Arabic"],
                           [["The company offers daily flights.", "تُقَدِّم الشَّرِكَة رِحْلَات يَوْمِيَّة"], ["The planes are comfortable.", "الطَّائِرَات مُرِيحَة"],
                            ["The prices are low.", "الْأَسْعَار مُنْخَفِضَة"], ["The seats are wide.", "الْمَقَاعِد وَاسِعَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("An invented advert",
             "This advert is made up for practice; the company does not exist.",
             examples=[
                 ex("شَرِكَة «النَّجْمَة» تُقَدِّم رِحْلَات يَوْمِيَّة إِلَى عَمَّان وَالْكُوَيْت.", "The company “Star” offers daily flights to Amman and Kuwait.", "تُقَدِّم"),
                 ex("تُغَادِر الطَّائِرَات فِي الْوَقْت الْمُنَاسِب.", "The planes leave at the right time.", "تُغَادِر"),
                 ex("الْمَقَاعِد وَاسِعَة وَالْأَسْعَار مُنْخَفِضَة.", "The seats are wide and the prices are low.", "وَاسِعَة"),
                 ex("تَبْدَأ الْأَسْعَار مِنْ مِئَة دِينَار.", "Prices start from a hundred dinars.", "تَبْدَأ"),
                 ex("تَصِل الطَّائِرَات إِلَى الْمَطَار قَبْل الْمَسَاء.", "The planes reach the airport before evening.", "تَصِل"),
                 ex("اِحْجِزْ تَذْكِرَتَكَ الْيَوْم!", "Book your ticket today! (to a man)", "اِحْجِزْ"),
             ]),
    ],
    exercises=[
        M("What does تُقَدِّم الشَّرِكَة رِحْلَات يَوْمِيَّة mean?", "The company offers daily flights", ["The company cancels daily flights", "The company buys planes", "The company has one flight"], "تُقَدِّم = offers."),
        M("Which adjective goes with رِحْلَات (flights)?", "يَوْمِيَّة", ["يَوْمِيّ", "يَوْمِيُّون", "يَوْمِيَّتَان"], "Plural of things → feminine singular adjective."),
        M("What does الْأَسْعَار مُنْخَفِضَة mean?", "The prices are low", ["The prices are high", "The prices are fixed", "The price is free"], "مُنْخَفِضَة = low."),
        M("What does اِحْجِزْ تَذْكِرَتَكَ الْيَوْم mean?", "Book your ticket today", ["Pay for your ticket tomorrow", "Show your passport", "Open your bag"], "اِحْجِزْ = book!"),
        M("Which sentence is correct for “The planes leave at the right time”?", "تُغَادِر الطَّائِرَات فِي الْوَقْت الْمُنَاسِب", ["يُغَادِر الطَّائِرَات فِي الْوَقْت الْمُنَاسِب", "تُغَادِرُون الطَّائِرَات فِي الْوَقْت الْمُنَاسِب", "أُغَادِر الطَّائِرَات فِي الْوَقْت الْمُنَاسِب"], "Planes are things."),
        M("What does تَبْدَأ الْأَسْعَار مِنْ مِئَة دِينَار mean?", "Prices start from a hundred dinars", ["Prices end at a hundred dinars", "The price is one dinar", "A hundred dinars are lost"], "تَبْدَأ مِنْ = starts from."),
        F("الْمَقَاعِد ___ وَالْأَسْعَار مُنْخَفِضَة.", "وَاسِعَة", ["وَاسِع", "وَاسِعُون", "وَاسِعَتَان"], "Plural of things → feminine singular.", tr="The seats are wide and the prices are low."),
        F("___ الشَّرِكَة رِحْلَات يَوْمِيَّة.", "تُقَدِّم", ["يُقَدِّم", "أُقَدِّم", "نُقَدِّم"], "The company is feminine.", tr="The company offers daily flights.", lemma="قدم#2:pres:hiya"),
        F("___ تَذْكِرَتَكَ الْيَوْم!", "اِحْجِزْ", ["تَحْجِز", "أَحْجِز", "حَجَزَ"], "A command to a man.", tr="Book your ticket today! (to a man)", lemma="حجز:imp:anta"),
    ],
    verify=(vv("قدم#2", "pres", hiya="تُقَدِّم") + vv("حجز", "imp", anta="اِحْجِزْ")
            + vw("الشَّرِكَة", "شَرِكَة", "تُقَدِّم", "رِحْلَات", "يَوْمِيَّة", "الْكُوَيْت", "الْوَقْت", "الْمُنَاسِب", "الْمَقَاعِد", "وَاسِعَة", "الْأَسْعَار", "مُنْخَفِضَة", "مُرِيحَة", "دِينَار", "الْمَسَاء", "تَذْكِرَتَكَ", "الْيَوْم", "يَوْمِيّ", "يَوْمِيُّون", "وَاسِعُون", "وَاسِعَتَان", "النَّجْمَة")),
)


# ---------------------------------------------------------------------------- 266
L266 = lesson(
    "Passport control and customs",
    "هَلْ مَعَكَ شَيْء مَمْنُوع؟ · اِفْتَحْ حَقِيبَتَكَ",
    requires=["تفتيش", "ضريبة", "ممنوع", "هدية", "فتح", "حقيبة", "جواز", "دفع", "شيء"],
    cards=[
        card("Words at the desk",
             "Customs is الْجَمَارِك. The officer does a تَفْتِيش (inspection). Tax is ضَرِيبَة. Something forbidden is مَمْنُوع, and a gift is هَدِيَّة (plural هَدَايَا).",
             tables=[table(["English", "Arabic"],
                           [["customs", "الْجَمَارِك"], ["inspection", "تَفْتِيش"], ["tax", "ضَرِيبَة"], ["forbidden", "مَمْنُوع"], ["gift", "هَدِيَّة"], ["gifts", "هَدَايَا"],
                            ["Please.", "مِنْ فَضْلِك"], ["Here you are.", "تَفَضَّلْ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A short conversation (an invented practice text)",
             "The officer talks to a traveller. Read it line by line.",
             examples=[
                 ex("جَوَاز السَّفَر مِنْ فَضْلِك.", "Your passport, please.", "مِنْ فَضْلِك"),
                 ex("تَفَضَّلْ.", "Here you are.", "تَفَضَّلْ"),
                 ex("هَلْ مَعَكَ شَيْء مَمْنُوع؟", "Do you have anything forbidden?", "مَمْنُوع"),
                 ex("لَا، مَعِي هَدَايَا فَقَط.", "No, I only have gifts.", "هَدَايَا"),
                 ex("اِفْتَحْ هَذِهِ الْحَقِيبَة مِنْ فَضْلِك.", "Open this bag, please. (to a man)", "اِفْتَحْ"),
                 ex("هَلْ أَدْفَع ضَرِيبَة؟ لَا، لَا تَدْفَع شَيْئًا.", "Do I pay tax? No, you do not pay anything.", "ضَرِيبَة"),
             ]),
    ],
    exercises=[
        M("Which word means “forbidden”?", "مَمْنُوع", ["مَفْتُوح", "مُنَاسِب", "مُهِمّ"], "مَمْنُوع = forbidden."),
        M("Which word means “gifts”?", "هَدَايَا", ["ضَرِيبَة", "جَمَارِك", "تَفْتِيش"], "هَدَايَا = gifts."),
        M("A clerk hands back your passport and says تَفَضَّلْ. What does it mean?", "Here you are", ["Goodbye", "Sit down", "I am sorry"], "Said when you hand something over."),
        M("What does اِفْتَحْ هَذِهِ الْحَقِيبَة مِنْ فَضْلِك mean?", "Open this bag, please", ["Close this bag, please", "Carry this bag, please", "Buy this bag, please"], "اِفْتَحْ = open!"),
        M("What does هَلْ مَعَكَ شَيْء مَمْنُوع؟ ask?", "Do you have anything forbidden?", ["Do you have a ticket?", "Do you have a gift?", "Do you pay tax?"], "مَمْنُوع = forbidden."),
        M("What does لَا تَدْفَع شَيْئًا mean?", "You do not pay anything", ["You paid a lot", "You must pay now", "I do not see anything"], "لَا + present = does not."),
        F("جَوَاز السَّفَر مِنْ ___.", "فَضْلِك", ["حَقِيبَتِك", "بَوَّابَتِك", "تَذْكِرَتِك"], "A polite request.", tr="Your passport, please."),
        F("___ هَذِهِ الْحَقِيبَة مِنْ فَضْلِك.", "اِفْتَحْ", ["يَفْتَح", "فَتَحْتُ", "أَفْتَح"], "A command to a man.", tr="Open this bag, please. (to a man)", lemma="فتح:imp:anta"),
        F("هَلْ ___ ضَرِيبَة؟", "أَدْفَع", ["يَدْفَع", "تَدْفَعِين", "نَدْفَع"], "I pay.", tr="Do I pay tax?", lemma="دفع:pres:ana"),
    ],
    verify=(vv("فتح", "imp", anta="اِفْتَحْ") + vv("دفع", "pres", ana="أَدْفَع", anta="تَدْفَع")
            + vw("الْجَمَارِك", "تَفْتِيش", "ضَرِيبَة", "مَمْنُوع", "هَدِيَّة", "هَدَايَا", "فَضْلِك", "تَفَضَّلْ", "مَعَكَ", "شَيْئًا", "شَيْء", "حَقِيبَتَكَ", "مَفْتُوح", "مُنَاسِب", "مُهِمّ", "بَوَّابَتِك", "تَذْكِرَتِك", "حَقِيبَتِك")),
)

# ---------------------------------------------------------------------------- 267
L267 = lesson(
    "Announcements at the gate",
    "بِطَاقَة الصُّعُود · تَبْدَأ عَمَلِيَّة الصُّعُود",
    requires=["بطاقة", "صعود", "بوابة", "رحلة", "بدأ", "ذهب", "تأخر", "رقم"],
    cards=[
        card("Listen for these",
             "Gate announcements repeat the same few phrases. A boarding pass is بِطَاقَة الصُّعُود. Boarding is عَمَلِيَّة الصُّعُود. "
             "The announcer gives commands in the plural: اِذْهَبُوا (go!). Listen for the number after رَقْم.",
             tables=[table(["English", "Arabic"],
                           [["boarding pass", "بِطَاقَة الصُّعُود"], ["boarding (the process)", "عَمَلِيَّة الصُّعُود"], ["Go! (to a group)", "اِذْهَبُوا"],
                            ["flight number", "رَقْم الرِّحْلَة"], ["now", "الْآن"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What you might hear",
             "These announcements are invented for practice.",
             examples=[
                 ex("بِطَاقَة الصُّعُود مِنْ فَضْلِكُمْ.", "Your boarding pass, please. (to a group)", "بِطَاقَة الصُّعُود"),
                 ex("تَبْدَأ عَمَلِيَّة الصُّعُود إِلَى الطَّائِرَة الْآن.", "Boarding the plane begins now.", "تَبْدَأ"),
                 ex("اِذْهَبُوا إِلَى الْبَوَّابَة رَقْم سِتَّة.", "Go to gate number six. (to a group)", "اِذْهَبُوا"),
                 ex("الرِّحْلَة إِلَى الْكُوَيْت تَأَخَّرَتْ سَاعَة.", "The flight to Kuwait has been delayed by an hour.", "تَأَخَّرَتْ"),
                 ex("رَقْم الرِّحْلَة خَمْسُون.", "The flight number is fifty.", "رَقْم"),
                 ex("عَلَى الرُّكَّاب أَنْ يَذْهَبُوا إِلَى الْبَوَّابَة الْآن.", "The passengers must go to the gate now.", "عَلَى الرُّكَّاب"),
             ]),
    ],
    exercises=[
        M("What is بِطَاقَة الصُّعُود?", "a boarding pass", ["a passport", "a seat", "a tax"], "بِطَاقَة = card, pass."),
        M("What does اِذْهَبُوا إِلَى الْبَوَّابَة رَقْم سِتَّة mean?", "Go to gate number six", ["Leave gate number six", "Open gate number six", "Wait at gate number six"], "اِذْهَبُوا = go! (plural)."),
        M("Who is addressed by اِذْهَبُوا?", "a group", ["one man", "one woman", "two women"], "ـُوا = several people."),
        M("What does الرِّحْلَة إِلَى الْكُوَيْت تَأَخَّرَتْ سَاعَة mean?", "The flight to Kuwait has been delayed by an hour", ["The flight to Kuwait leaves early", "The flight to Kuwait has landed", "The flight to Kuwait is cancelled"], "تَأَخَّرَتْ = it was late."),
        M("What does تَبْدَأ عَمَلِيَّة الصُّعُود الْآن mean?", "Boarding begins now", ["Boarding ended", "The plane landed", "The gate is closed"], "تَبْدَأ = begins."),
        M("Why does تَأَخَّرَتْ end in تْ?", "الرِّحْلَة is feminine", ["it is a command", "it is plural", "it is a question"], "A feminine subject gives تْ in the past."),
        F("___ الصُّعُود مِنْ فَضْلِكُمْ.", "بِطَاقَة", ["حَقِيبَة", "بَوَّابَة", "شَرِكَة"], "A card you show.", tr="Your boarding pass, please. (to a group)"),
        F("___ إِلَى الْبَوَّابَة رَقْم سِتَّة.", "اِذْهَبُوا", ["اِذْهَبْ", "يَذْهَب", "ذَهَبَ"], "The announcer speaks to a group.", tr="Go to gate number six. (to a group)", lemma="ذهب:imp:antum"),
        F("الرِّحْلَة إِلَى الْكُوَيْت ___ سَاعَة.", "تَأَخَّرَتْ", ["تَأَخَّرَ", "يَتَأَخَّر", "تَأَخَّرُوا"], "A feminine subject in the past.", tr="The flight to Kuwait has been delayed by an hour."),
    ],
    verify=(vv("ذهب", "imp", antum="اِذْهَبُوا") + vv("ذهب", "pres", hum="يَذْهَبُون")
            + vw("بِطَاقَة", "الصُّعُود", "عَمَلِيَّة", "اِذْهَبُوا", "اِذْهَبْ", "فَضْلِكُمْ", "تَأَخَّرَتْ", "تَأَخَّرَ", "يَتَأَخَّر", "تَأَخَّرُوا", "سِتَّة", "سَاعَة", "الْكُوَيْت", "يَذْهَبُوا", "خَمْسُون", "شَرِكَة")),
)

# ---------------------------------------------------------------------------- 268
L268 = lesson(
    "Assimilated verbs: the و that disappears",
    "وَصَلَ ← يَصِل · وَقَفَ ← يَقِف · وَجَدَ ← يَجِد",
    requires=["وصل", "وقف", "وجد", "وضع", "وصف", "وعد", "فعل", "ماضي"],
    cards=[
        card("A verb whose first root letter is و",
             "Some verbs begin with the root letter و. In the past they look normal: وَصَلَ (he arrived), وَقَفَ (he stood). In the present the و disappears: يَصِل, يَقِف. "
             "Grammarians call these assimilated verbs (the first letter “melts away”). Most take a kasra on the second letter in the present, and a few take a fatḥa (يَضَع).",
             tables=[table(["Past (he)", "Present (he)", "English"],
                           [["وَصَلَ", "يَصِل", "arrives"], ["وَقَفَ", "يَقِف", "stands, stops"], ["وَجَدَ", "يَجِد", "finds"], ["وَضَعَ", "يَضَع", "puts"],
                            ["وَصَفَ", "يَصِف", "describes"], ["وَعَدَ", "يَعِد", "promises"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("In sentences",
             "The present loses the و (and so does the command, which you will meet soon). The past keeps it, and so do nouns such as وُصُول, “arrival”.",
             examples=[
                 ex("وَصَلَ أَخِي أَمْس.", "My brother arrived yesterday.", "وَصَلَ"),
                 ex("يَصِل أَخِي غَدًا.", "My brother arrives tomorrow.", "يَصِل"),
                 ex("وَقَفْتُ فِي الصَّفّ.", "I stood in the line.", "وَقَفْتُ"),
                 ex("يَقِف الرُّكَّاب أَمَامَ الْبَوَّابَة.", "The passengers stand in front of the gate.", "يَقِف"),
                 ex("وَجَدْتُ جَوَازِي.", "I found my passport.", "وَجَدْتُ"),
                 ex("أَجِد مَقْعَدِي بِسُهُولَة.", "I find my seat easily.", "أَجِد"),
             ]),
    ],
    exercises=[
        M("What happens to the و of وَصَلَ in the present?", "it disappears", ["it becomes ي", "it doubles", "it moves to the end"], "يَصِل has no و."),
        M("Which is the present of وَقَفَ?", "يَقِف", ["يَوْقِف", "يَوَقِف", "وَقَفَ"], "The و drops."),
        M("Which is the present of وَجَدَ?", "يَجِد", ["يَوْجِد", "يَجَد", "جَدَّ"], "يَجِد = he finds."),
        M("What does يَضَع mean?", "he puts", ["he stands", "he finds", "he promises"], "وَضَعَ → يَضَع."),
        M("What does وَجَدْتُ جَوَازِي mean?", "I found my passport", ["I lost my passport", "I showed my passport", "I wanted my passport"], "وَجَدْتُ = I found."),
        M("Which sentence is in the present?", "يَصِل أَخِي غَدًا", ["وَصَلَ أَخِي أَمْس", "وَصَلْتُ أَمْس", "وَقَفْتُ أَمْس"], "غَدًا = tomorrow."),
        F("___ الرُّكَّاب أَمَامَ الْبَوَّابَة.", "يَقِف", ["يَوْقِف", "وَقَفَ", "يَقَف"], "The present of وَقَفَ.", tr="The passengers stand in front of the gate.", lemma="وقف:pres:huwa"),
        F("أَنَا ___ مَقْعَدِي بِسُهُولَة.", "أَجِد", ["أَوْجِد", "نَجِد", "يَجِد"], "I find: the و is gone.", tr="I find my seat easily.", lemma="وجد:pres:ana"),
        F("___ أَخِي أَمْس.", "وَصَلَ", ["يَصِل", "تَصِل", "أَصِل"], "Yesterday needs the past.", tr="My brother arrived yesterday."),
    ],
    verify=(vv("وصل", "past", huwa="وَصَلَ") + vv("وصل", "pres", huwa="يَصِل") + vv("وقف", "past", huwa="وَقَفَ", ana="وَقَفْتُ") + vv("وقف", "pres", huwa="يَقِف")
            + vv("وجد", "past", huwa="وَجَدَ", ana="وَجَدْتُ") + vv("وجد", "pres", huwa="يَجِد", ana="أَجِد") + vv("وضع", "past", huwa="وَضَعَ") + vv("وضع", "pres", huwa="يَضَع")
            + vv("وصف", "past", huwa="وَصَفَ") + vv("وصف", "pres", huwa="يَصِف") + vv("وعد", "past", huwa="وَعَدَ") + vv("وعد", "pres", huwa="يَعِد")
            + vw("بِسُهُولَة", "أَمَامَ", "الصَّفّ", "أَمْس", "غَدًا", "جَوَازِي", "مَقْعَدِي", "أَخِي", "يَوْقِف", "يَوَقِف", "يَجَد", "جَدَّ", "يَقَف", "أَوْجِد")),
)

# ---------------------------------------------------------------------------- 269
L269 = lesson(
    "Assimilated verbs in the present: the main persons",
    "أَصِل · تَصِل · تَصِلِين · يَصِلُون",
    requires=["وصل", "وقف", "وجد", "وضع", "أنا", "أنت", "هو", "هي", "نحن", "هم"],
    cards=[
        card("One pattern for every person",
             "After the و has dropped, the present behaves like any other verb: the prefix shows the person, and the same endings are added. Learn يَصِل once and you know the rest.",
             tables=[table(["Pronoun", "Present of وَصَلَ", "English"],
                           [["أَنَا", "أَصِل", "I arrive"], ["أَنْتَ", "تَصِل", "you arrive (man)"], ["أَنْتِ", "تَصِلِين", "you arrive (woman)"], ["هُوَ", "يَصِل", "he arrives"],
                            ["هِيَ", "تَصِل", "she arrives"], ["نَحْنُ", "نَصِل", "we arrive"], ["أَنْتُمْ", "تَصِلُون", "you arrive (men)"], ["هُمْ", "يَصِلُون", "they arrive (men)"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("The past is regular",
             "In the past the و stays, and the endings are the ones you know: وَصَلْتُ (I arrived), وَصَلْنَا (we arrived), وَصَلُوا (they arrived).",
             examples=[
                 ex("أَصِل إِلَى الْمَطَار فِي الصَّبَاح.", "I arrive at the airport in the morning.", "أَصِل"),
                 ex("تَصِلِين إِلَى الْبَيْت قَبْل الْمَسَاء.", "You arrive home before evening. (to a woman)", "تَصِلِين"),
                 ex("نَقِف أَمَامَ الْجَمَارِك.", "We stand in front of customs.", "نَقِف"),
                 ex("يَجِدُون حَقَائِبَهُمْ بِسُرْعَة.", "They find their bags quickly.", "يَجِدُون"),
                 ex("وَصَلْنَا أَمْس فِي الْعَاشِرَة.", "We arrived yesterday at ten.", "وَصَلْنَا"),
                 ex("وَصَلُوا مُتَأَخِّرِين.", "They arrived late.", "وَصَلُوا"),
             ]),
    ],
    exercises=[
        M("Which means “we arrive”?", "نَصِل", ["أَصِل", "تَصِل", "يَصِل"], "نـ = we."),
        M("Which means “you arrive” (to a woman)?", "تَصِلِين", ["تَصِل", "تَصِلُون", "أَصِل"], "ـِين = you (woman)."),
        M("Which means “they arrive” (men)?", "يَصِلُون", ["تَصِلُون", "يَصِل", "نَصِل"], "يـ…ـُون = they (men)."),
        M("Which means “we arrived”?", "وَصَلْنَا", ["نَصِل", "وَصَلُوا", "وَصَلْتُ"], "ـنَا = we, in the past."),
        M("What does يَجِدُون حَقَائِبَهُمْ بِسُرْعَة mean?", "They find their bags quickly", ["They lose their bags quickly", "They carry their bags slowly", "He finds his bag"], "يَجِدُون = they find."),
        M("What does وَصَلُوا مُتَأَخِّرِين mean?", "They arrived late", ["They left early", "They will arrive soon", "They arrive every day"], "مُتَأَخِّرِين = late (people)."),
        F("أَنَا ___ إِلَى الْمَطَار فِي الصَّبَاح.", "أَصِل", ["تَصِل", "نَصِل", "يَصِل"], "I arrive.", tr="I arrive at the airport in the morning.", lemma="وصل:pres:ana"),
        F("نَحْنُ ___ أَمَامَ الْجَمَارِك.", "نَقِف", ["أَقِف", "تَقِف", "يَقِف"], "We stand.", tr="We stand in front of customs.", lemma="وقف:pres:nahnu"),
        F("هُمْ ___ حَقَائِبَهُمْ بِسُرْعَة.", "يَجِدُون", ["يَجِد", "نَجِد", "تَجِدِين"], "They (men) find.", tr="They find their bags quickly.", lemma="وجد:pres:hum"),
    ],
    verify=(vv("وصل", "pres", ana="أَصِل", anta="تَصِل", anti="تَصِلِين", huwa="يَصِل", hiya="تَصِل", nahnu="نَصِل", antum="تَصِلُون", hum="يَصِلُون")
            + vv("وصل", "past", ana="وَصَلْتُ", nahnu="وَصَلْنَا", hum="وَصَلُوا") + vv("وقف", "pres", nahnu="نَقِف") + vv("وجد", "pres", hum="يَجِدُون")
            + vw("حَقَائِبَهُمْ", "بِسُرْعَة", "مُتَأَخِّرِين", "الْبَيْت", "الْمَسَاء", "الصَّبَاح", "الْجَمَارِك", "أَمَامَ", "الْعَاشِرَة")),
)

# ---------------------------------------------------------------------------- 270
L270 = lesson(
    "Assimilated verbs: future and negation",
    "سَأَصِل · لَنْ أَصِل · لَمْ أَصِلْ",
    requires=["وصل", "وقف", "وجد", "سوف", "لن", "لم", "أمس"],
    cards=[
        card("The و stays away",
             "The future, the negations with لَا and لَنْ, and the past negation with لَمْ all use the present stem. So the و never comes back. "
             "After لَمْ the ending is cut short: لَمْ يَصِلْ.",
             tables=[table(["Meaning", "Form for أَنَا", "Form for هِيَ", "Form for هُمْ"],
                           [["will arrive", "سَأَصِل", "سَتَصِل", "سَيَصِلُون"], ["does not arrive", "لَا أَصِل", "لَا تَصِل", "لَا يَصِلُون"],
                            ["will not arrive", "لَنْ أَصِل", "لَنْ تَصِل", "لَنْ يَصِلُوا"], ["did not arrive", "لَمْ أَصِلْ", "لَمْ تَصِلْ", "لَمْ يَصِلُوا"]],
                           say=[1, 2, 3], tlit=[1], gloss=False)]),
        card("In use",
             "Use سَـ or سَوْفَ for the future, and watch the time word: غَدًا (tomorrow) goes with the future, أَمْس (yesterday) with لَمْ.",
             examples=[
                 ex("سَأَصِل إِلَى الْكُوَيْت غَدًا.", "I will arrive in Kuwait tomorrow.", "سَأَصِل"),
                 ex("سَوْفَ تَصِل الرِّحْلَة فِي الثَّانِيَة.", "The flight will arrive at two.", "سَوْفَ تَصِل"),
                 ex("لَنْ أَقِف فِي الصَّفّ الْيَوْم.", "I will not stand in line today.", "لَنْ أَقِف"),
                 ex("لَا يَجِد الرُّكَّاب حَقَائِبَهُمْ.", "The passengers do not find their bags.", "لَا يَجِد"),
                 ex("لَمْ أَجِدْ جَوَازِي أَمْس.", "I did not find my passport yesterday.", "لَمْ أَجِدْ"),
                 ex("لَمْ تَصِلْ حَقِيبَتِي.", "My bag did not arrive.", "لَمْ تَصِلْ"),
             ]),
    ],
    exercises=[
        M("Which means “I will arrive”?", "سَأَصِل", ["لَنْ أَصِل", "وَصَلْتُ", "لَمْ أَصِلْ"], "سَـ = will."),
        M("Which means “I will not arrive”?", "لَنْ أَصِل", ["سَأَصِل", "لَمْ أَصِلْ", "أَصِل"], "لَنْ = will not."),
        M("Which means “I did not arrive”?", "لَمْ أَصِلْ", ["لَنْ أَصِل", "سَأَصِل", "لَا أَصِل"], "لَمْ + short form = did not."),
        M("What does لَمْ أَجِدْ جَوَازِي أَمْس mean?", "I did not find my passport yesterday", ["I will not find my passport tomorrow", "I do not find my passport", "I found my passport yesterday"], "أَمْس = yesterday."),
        M("What does سَوْفَ تَصِل الرِّحْلَة فِي الثَّانِيَة mean?", "The flight will arrive at two", ["The flight arrived at two", "The flight did not arrive at two", "The flight leaves at two"], "سَوْفَ = will."),
        M("Which time word goes with لَنْ?", "غَدًا", ["أَمْس", "مُنْذُ سَنَة", "قَبْل أُسْبُوع"], "لَنْ looks forward."),
        F("___ أَقِف فِي الصَّفّ الْيَوْم.", "لَنْ", ["لَمْ", "سَـ", "قَدْ"], "Will not.", tr="I will not stand in line today."),
        F("لَمْ ___ حَقِيبَتِي.", "تَصِلْ", ["تَصِلِين", "يَصِلُون", "أَصِل"], "A feminine subject after لَمْ.", tr="My bag did not arrive.", lemma="وصل:jus:hiya"),
        F("___ الرُّكَّاب حَقَائِبَهُمْ.", "لَا يَجِد", ["لَا يَجِدُون", "لَا تَجِدِين", "لَا أَجِد"], "A singular verb before the subject; لَا + present = does not.", tr="The passengers do not find their bags."),
    ],
    verify=(vv("وصل", "fut", ana="سَأَصِل", hiya="سَتَصِل", hum="سَيَصِلُون") + vv("وصل", "sub", ana="أَصِل", hiya="تَصِل", hum="يَصِلُوا")
            + vv("وصل", "jus", ana="أَصِلْ", hiya="تَصِلْ", hum="يَصِلُوا") + vv("وجد", "jus", ana="أَجِدْ") + vv("وقف", "sub", ana="أَقِف")
            + vw("سَأَصِل", "سَوْفَ", "الثَّانِيَة", "الْيَوْم", "حَقِيبَتِي", "قَدْ", "مُنْذُ", "أُسْبُوع", "سَنَة")),
)


# ---------------------------------------------------------------------------- 271
L271 = lesson(
    "Commands from assimilated verbs",
    "صِلْ · قِفْ · ضَعْ · جِدْ",
    requires=["وصل", "وقف", "وضع", "وجد", "أخذ", "أمر", "فعل", "صف"],
    cards=[
        card("Take the present stem and drop the prefix",
             "The command is easy for assimilated verbs: take the present stem and drop the prefix, with no helping alif. يَقِف becomes قِفْ, and يَضَع becomes ضَعْ. "
             "The endings are the usual ones: nothing (with a sukūn) for a man, ـِي for a woman, ـُوا for a group.",
             tables=[table(["English", "To a man", "To a woman", "To a group"],
                           [["arrive!", "صِلْ", "صِلِي", "صِلُوا"], ["stand, stop!", "قِفْ", "قِفِي", "قِفُوا"], ["put!", "ضَعْ", "ضَعِي", "ضَعُوا"], ["find!", "جِدْ", "جِدِي", "جِدُوا"]],
                           say=[1, 2, 3], tlit=[1], gloss=False),
                    table(["English", "To a man", "To a woman", "To a group"],
                          [["take!", "خُذْ", "خُذِي", "خُذُوا"], ["eat!", "كُلْ", "كُلِي", "كُلُوا"]],
                          title="Two irregular verbs: the hamza at the start also drops in the command (learn them as they are)",
                          note="أَخَذَ and أَكَلَ begin with hamza, not و, but they also drop their first letter in the command.",
                          say=[1, 2, 3], tlit=[1], gloss=False)]),
        card("In use",
             "Before a word with ال, a command that ends in a sukūn takes a helping kasra: ضَعِ الْحَقِيبَة. To forbid, use لَا + the short present: لَا تَقِفْ.",
             examples=[
                 ex("قِفْ هُنَا مِنْ فَضْلِك.", "Stand here, please. (to a man)", "قِفْ"),
                 ex("قِفِي أَمَامَ الْبَوَّابَة.", "Stand in front of the gate. (to a woman)", "قِفِي"),
                 ex("ضَعِ الْحَقِيبَة عَلَى الطَّاوِلَة.", "Put the bag on the table. (to a man)", "ضَعِ"),
                 ex("ضَعُوا الْجَوَازَات هُنَا.", "Put the passports here. (to a group)", "ضَعُوا"),
                 ex("خُذْ تَذْكِرَتَكَ يَا أَخِي.", "Take your ticket, brother.", "خُذْ"),
                 ex("لَا تَقِفْ أَمَامَ الْبَاب.", "Do not stand in front of the door. (to a man)", "لَا تَقِفْ"),
             ]),
    ],
    exercises=[
        M("Which is the command “stand!” to a man?", "قِفْ", ["يَقِف", "وَقَفَ", "أَقِف"], "Drop the prefix of يَقِف."),
        M("Which is the command “put!” to a man?", "ضَعْ", ["يَضَع", "وَضَعَ", "وَضْع"], "Drop the prefix of يَضَع."),
        M("Which is “stand!” to a woman?", "قِفِي", ["قِفْ", "قِفُوا", "تَقِفِين"], "ـِي = to a woman."),
        M("Which is “put!” to a group?", "ضَعُوا", ["ضَعْ", "ضَعِي", "يَضَعُون"], "ـُوا = to a group."),
        M("What does لَا تَقِفْ أَمَامَ الْبَاب mean?", "Do not stand in front of the door", ["Stand in front of the door", "I did not stand in front of the door", "He will not stand there"], "لَا تَ… = do not."),
        M("Which command means “take!” (to a man)?", "خُذْ", ["كُلْ", "ضَعْ", "قِفْ"], "أَخَذَ → خُذْ."),
        F("___ الْحَقِيبَة عَلَى الطَّاوِلَة.", "ضَعِ", ["ضَعُوا", "ضَعِي", "يَضَع"], "A man is spoken to; the sukūn becomes kasra before ال.", tr="Put the bag on the table. (to a man)"),
        F("___ أَمَامَ الْبَوَّابَة يَا سَلْمَى.", "قِفِي", ["قِفْ", "قِفُوا", "لَا تَقِفْ"], "Salma is a woman.", tr="Stand in front of the gate, Salma.", lemma="وقف:imp:anti"),
        F("لَا ___ أَمَامَ الْبَاب.", "تَقِفْ", ["قِفْ", "يَقِف", "وَقَفَ"], "Forbid with لَا + the short present.", tr="Do not stand in front of the door. (to a man)", lemma="وقف:jus:anta"),
    ],
    verify=(vv("وصل", "imp", anta="صِلْ", anti="صِلِي", antum="صِلُوا") + vv("وقف", "imp", anta="قِفْ", anti="قِفِي", antum="قِفُوا")
            + vv("وضع", "imp", anta="ضَعْ", anti="ضَعِي", antum="ضَعُوا") + vv("وجد", "imp", anta="جِدْ", anti="جِدِي", antum="جِدُوا")
            + vv("وقف", "neg", anta="لَا تَقِفْ")
            + vw("اِسْتَمِعُوا", "خُذْ", "خُذِي", "خُذُوا", "كُلْ", "كُلِي", "كُلُوا", "ضَعِ", "الْجَوَازَات", "تَذْكِرَتَكَ", "الطَّاوِلَة", "سَلْمَى", "الْبَاب", "وَضْع", "تَقِفِين", "يَضَعُون")),
)

# ---------------------------------------------------------------------------- 272
L272 = lesson(
    "Using a machine: step by step",
    "ضَعِ الْعُمْلَة · اِضْغَطِ الزِّرّ · خُذِ الْمَشْرُوب",
    requires=["عملة", "آلة", "زر", "ضغط", "مشروب", "وضع", "رقم", "بطاقة", "لغة"],
    cards=[
        card("Steps use commands",
             "Instructions on machines use commands, one for each step, joined by أَوَّلًا (first), ثُمَّ (then) and أَخِيرًا (finally). "
             "The commands here are all to a man (or to anyone, on a sign). Each one that comes before ال ends in a kasra.",
             tables=[table(["Step", "Instruction", "English"],
                           [["أَوَّلًا", "ضَعِ الْعُمْلَة فِي الْآلَة", "put the coin in the machine"], ["ثُمَّ", "اِخْتَرِ الْمَشْرُوب", "choose the drink"],
                            ["ثُمَّ", "اِضْغَطِ الزِّرّ", "press the button"], ["ثُمَّ", "اِنْتَظِرْ قَلِيلًا", "wait a little"], ["أَخِيرًا", "خُذِ الْمَشْرُوب", "take the drink"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("A cash machine (an invented text)",
             "The same pattern works for a cash machine (ATM).",
             examples=[
                 ex("أَوَّلًا اِخْتَرِ اللُّغَة.", "First choose the language.", "اِخْتَرِ"),
                 ex("ثُمَّ ضَعِ الْبِطَاقَة فِي الْآلَة.", "Then put the card in the machine.", "ضَعِ"),
                 ex("ثُمَّ اُكْتُبِ الرَّقْم.", "Then write the number.", "اُكْتُبِ"),
                 ex("اِضْغَطِ الزِّرّ الْأَخْضَر.", "Press the green button.", "اِضْغَطِ"),
                 ex("اِنْتَظِرْ دَقِيقَة وَاحِدَة.", "Wait one minute.", "اِنْتَظِرْ"),
                 ex("أَخِيرًا خُذِ الْبِطَاقَة وَالْمَال.", "Finally take the card and the money. (to a man)", "خُذِ"),
             ]),
    ],
    exercises=[
        M("Which word means “first”?", "أَوَّلًا", ["أَخِيرًا", "ثُمَّ", "قَلِيلًا"], "أَوَّلًا = firstly."),
        M("Which word means “finally”?", "أَخِيرًا", ["أَوَّلًا", "ثُمَّ", "الْآن"], "أَخِيرًا = finally."),
        M("What does اِضْغَطِ الزِّرّ mean?", "Press the button", ["Choose the drink", "Take the card", "Wait a minute"], "اِضْغَطْ = press!"),
        M("What does اِنْتَظِرْ دَقِيقَة وَاحِدَة mean?", "Wait one minute", ["Run for one minute", "Press for one minute", "Pay one dinar"], "اِنْتَظِرْ = wait!"),
        M("In which order are the steps on the card?", "put the coin in, choose, press, take", ["take, press, choose, put the coin in", "choose, take, put the coin in, press", "press, take, choose, put the coin in"], "You take the drink last."),
        M("Why does ضَعِ الْعُمْلَة end in a kasra?", "a command ending in a sukūn takes a helping vowel before ال", ["it is a question", "it is plural", "it is a woman"], "ضَعْ + ال → ضَعِ ال."),
        F("ضَعِ ___ فِي الْآلَة.", "الْعُمْلَة", ["الزِّرّ", "الشَّاشَة", "الصَّبَاح"], "A coin goes in the machine.", tr="Put the coin in the machine."),
        F("اُكْتُبِ ___ مِنْ فَضْلِك.", "الرَّقْم", ["الْمَطَر", "الْمُوَظَّف", "الْقَمَر"], "You write a number.", tr="Write the number, please.", lemma=None),
        F("أَخِيرًا ___ الْبِطَاقَة وَالْمَال.", "خُذِ", ["خُذُوا", "يَأْخُذ", "أَخَذَ"], "A command ending in a sukūn takes a kasra before ال.", tr="Finally take the card and the money. (to a man)"),
    ],
    verify=(vv("ضغط", "imp", anta="اِضْغَطْ") + vv("نظر#8", "imp", anta="اِنْتَظِرْ") + vv("كتب", "imp", anta="اُكْتُبْ") + vv("وضع", "imp", anta="ضَعْ")
            + vw("الْعُمْلَة", "الْآلَة", "الزِّرّ", "اِخْتَرِ", "الْمَشْرُوب", "اِضْغَطِ", "اِنْتَظِرْ", "قَلِيلًا", "أَخِيرًا", "أَوَّلًا", "ثُمَّ", "الْبِطَاقَة", "اللُّغَة", "الرَّقْم", "اُكْتُبِ", "الْأَخْضَر", "دَقِيقَة", "الْمَال", "خُذِ", "الشَّاشَة", "الصَّبَاح", "الْمَطَر", "الْقَمَر", "يَأْخُذ", "أَخَذَ")),
)

# ---------------------------------------------------------------------------- 273
L273 = lesson(
    "Safety announcements on board",
    "اِرْبِطُوا حِزَام الْأَمَان · لَا تُدَخِّنُوا",
    requires=["ربط", "حزام", "أمان", "ضغط", "جلس", "وضع", "سمع", "مقعد", "حقيبة", "تحت"],
    cards=[
        card("The captain speaks to everyone",
             "On a plane the crew speaks to the whole cabin, so the commands end in ـُوا. The safety belt is حِزَام الْأَمَان (literally “the belt of safety”).",
             tables=[table(["English", "Arabic"],
                           [["Fasten the safety belt.", "اِرْبِطُوا حِزَام الْأَمَان"], ["Sit in your seats.", "اِجْلِسُوا فِي مَقَاعِدِكُمْ"], ["Put the bags under the seat.", "ضَعُوا الْحَقَائِب تَحْتَ الْمَقْعَد"],
                            ["Listen carefully.", "اِسْتَمِعُوا جَيِّدًا"], ["Do not smoke.", "لَا تُدَخِّنُوا"], ["Do not stand during landing.", "لَا تَقِفُوا أَثْنَاءَ الْهُبُوط"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What you hear in the cabin",
             "These announcements are invented for practice.",
             examples=[
                 ex("أَيُّهَا الرُّكَّاب، اِرْبِطُوا حِزَام الْأَمَان.", "Passengers, fasten your safety belt.", "اِرْبِطُوا"),
                 ex("اِجْلِسُوا فِي مَقَاعِدِكُمْ مِنْ فَضْلِكُمْ.", "Please sit in your seats.", "اِجْلِسُوا"),
                 ex("ضَعُوا الْحَقَائِب الصَّغِيرَة تَحْتَ الْمَقْعَد.", "Put the small bags under the seat.", "ضَعُوا"),
                 ex("لَا تُدَخِّنُوا فِي الطَّائِرَة.", "Do not smoke on the plane.", "لَا تُدَخِّنُوا"),
                 ex("اِسْتَمِعُوا جَيِّدًا إِلَى تَعْلِيمَات الْأَمَان.", "Listen carefully to the safety instructions.", "اِسْتَمِعُوا"),
                 ex("لَا تَقِفُوا أَثْنَاءَ الْهُبُوط.", "Do not stand during landing.", "لَا تَقِفُوا"),
             ]),
    ],
    exercises=[
        M("What does اِرْبِطُوا حِزَام الْأَمَان mean?", "Fasten the safety belt", ["Open the safety belt", "Pay the safety tax", "Leave the plane"], "اِرْبِطْ = tie, fasten!"),
        M("What does لَا تُدَخِّنُوا mean?", "Do not smoke", ["Do not stand", "Do not speak", "Do not sit"], "دَخَّنَ = to smoke."),
        M("Why does اِجْلِسُوا end in ـُوا?", "it speaks to a group", ["it speaks to one woman", "it is a question", "it is the past"], "ـُوا = several people."),
        M("What does لَا تَقِفُوا mean?", "Do not stand (all of you)", ["Stand (all of you)", "He did not stand", "I will not stand"], "لَا تَ… ـُوا = do not (group)."),
        M("Where do you put small bags?", "under the seat", ["on the wing", "outside the plane", "in the pilot’s hand"], "تَحْتَ الْمَقْعَد."),
        M("What does حِزَام الْأَمَان mean?", "the safety belt", ["the airport gate", "the boarding pass", "the emergency exit"], "أَمَان = safety."),
        F("___ حِزَام الْأَمَان.", "اِرْبِطُوا", ["اِرْبِطْ", "يَرْبِطُون", "رَبَطَ"], "The crew speaks to the cabin.", tr="Fasten the safety belt. (to the passengers)", lemma="ربط:imp:antum"),
        F("اِجْلِسُوا فِي ___ مِنْ فَضْلِكُمْ.", "مَقَاعِدِكُمْ", ["بَوَّابَتِكُمْ", "مَطَارِكُمْ", "شَرِكَتِكُمْ"], "You sit in seats.", tr="Please sit in your seats."),
        F("لَا ___ فِي الطَّائِرَة.", "تُدَخِّنُوا", ["تُدَخِّنْ", "يُدَخِّنُون", "دَخَّنَ"], "Forbid a group.", tr="Do not smoke on the plane. (to the passengers)", lemma="دخن#2:jus:antum"),
    ],
    verify=(vv("ربط", "imp", antum="اِرْبِطُوا") + vv("جلس", "imp", antum="اِجْلِسُوا") + vv("وضع", "imp", antum="ضَعُوا") + vv("سمع", "imp", antum="اِسْمَعُوا")
            + vv("دخن#2", "jus", antum="تُدَخِّنُوا") + vv("وقف", "neg", antum="لَا تَقِفُوا")
            + vw("أَيُّهَا", "مَقَاعِدِكُمْ", "جَيِّدًا", "تَعْلِيمَات", "أَثْنَاءَ", "الْهُبُوط", "الْأَمَان", "حِزَام", "الْمَقْعَد", "بَوَّابَتِكُمْ", "مَطَارِكُمْ", "شَرِكَتِكُمْ", "تُدَخِّنْ", "يُدَخِّنُون", "دَخَّنَ", "يَرْبِطُون", "رَبَطَ")),
)

# ---------------------------------------------------------------------------- 274
L274 = lesson(
    "Good manners for a guest: do and don’t",
    "اِخْلَعْ حِذَاءَكَ · لَا تَضَعْ قَدَمَيْكَ عَلَى الطَّاوِلَة",
    requires=["خلع", "حذاء", "وضع", "رفض", "قهوة", "يد", "ضيف", "سلام", "أهل", "بدأ"],
    cards=[
        card("Advice with commands",
             "A friend might give advice to a guest with short commands. The advice here is general and simple. Customs differ from country to country and from family to family, "
             "so treat it as a starting point, not a rule. In many Arab homes guests take off their shoes at the door, and in many places people greet first and ask about the family before getting down to business.",
             tables=[table(["Do", "Don’t"],
                           [["اِخْلَعْ حِذَاءَكَ", "لَا تَضَعْ قَدَمَيْكَ عَلَى الطَّاوِلَة"], ["اِبْدَأْ بِالسَّلَام", "لَا تَرْفُضِ الْقَهْوَة بِسُرْعَة"], ["قِفْ عِنْدَمَا يَدْخُل ضَيْف كَبِير فِي السِّنّ", "لَا تَبْدَأْ بِالْعَمَل فَوْرًا"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("A friend explains (an invented practice text)",
             "Notice that a positive command and a negative one use different forms of the same verb: خُذْ but لَا تَأْخُذْ, ضَعْ but لَا تَضَعْ.",
             examples=[
                 ex("اِخْلَعْ حِذَاءَكَ عِنْدَ الْبَاب، فَهَذَا مُنَاسِب فِي كَثِير مِنَ الْبُيُوت.", "Take off your shoes at the door; this is suitable in many homes.", "اِخْلَعْ"),
                 ex("لَا تَضَعْ قَدَمَيْكَ عَلَى الطَّاوِلَة.", "Do not put your feet on the table.", "لَا تَضَعْ"),
                 ex("اِبْدَأْ بِالسَّلَام ثُمَّ اِسْأَلْ عَنِ الْأَهْل.", "Start with the greeting, then ask about the family.", "اِبْدَأْ"),
                 ex("قِفْ عِنْدَمَا يَدْخُل ضَيْف كَبِير فِي السِّنّ.", "Stand up when an older guest comes in.", "قِفْ"),
                 ex("لَا تَرْفُضِ الْقَهْوَة بِسُرْعَة؛ خُذْ قَلِيلًا عَلَى الْأَقَلّ.", "Do not refuse the coffee quickly; take a little at least.", "لَا تَرْفُضِ"),
                 ex("كُلْ بِيَدِكَ الْيُمْنَى.", "Eat with your right hand (often expected at the table).", "كُلْ"),
             ]),
    ],
    exercises=[
        M("What does اِخْلَعْ حِذَاءَكَ mean?", "Take off your shoes", ["Wash your hands", "Open your bag", "Put on your coat"], "حِذَاء = shoes."),
        M("What does لَا تَضَعْ قَدَمَيْكَ عَلَى الطَّاوِلَة mean?", "Do not put your feet on the table", ["Put your bag on the table", "Wash the table", "Do not sit at the table"], "قَدَمَيْكَ = your two feet."),
        M("Which command is polite at the start of a visit?", "اِبْدَأْ بِالسَّلَام", ["اِبْدَأْ بِالْعَمَل", "اُتْرُكِ الْبَيْت", "اُسْكُتْ"], "Greet first."),
        M("Which means “do not refuse the coffee”?", "لَا تَرْفُضِ الْقَهْوَة", ["اِرْفُضِ الْقَهْوَة", "تَرْفُض الْقَهْوَة", "رَفَضَ الْقَهْوَة"], "لَا تَرْفُضْ = do not refuse."),
        M("Which sentence means “Stand up when an older guest comes in”?", "قِفْ عِنْدَمَا يَدْخُل ضَيْف كَبِير فِي السِّنّ", ["اِجْلِسْ عِنْدَمَا يَدْخُل ضَيْف", "لَا تَقِفْ عِنْدَ الْبَاب", "كُلْ مَعَ الضَّيْف"], "قِفْ = stand!"),
        M("What is the right attitude to this advice?", "customs differ, so it is a starting point", ["every family does exactly this", "it only applies to one country", "it is a law"], "Customs vary."),
        F("___ حِذَاءَكَ عِنْدَ الْبَاب.", "اِخْلَعْ", ["اِخْلَعُوا", "يَخْلَع", "خَلَعَ"], "A command to a man.", tr="Take off your shoes at the door. (to a man)", lemma="خلع:imp:anta"),
        F("لَا ___ قَدَمَيْكَ عَلَى الطَّاوِلَة.", "تَضَعْ", ["ضَعْ", "يَضَع", "وَضَعَ"], "Forbid with لَا + the short present.", tr="Do not put your feet on the table.", lemma="وضع:jus:anta"),
        F("___ بِيَدِكَ الْيُمْنَى.", "كُلْ", ["كَلَّ", "يَأْكُل", "أَكَلَ"], "A command to a man.", tr="Eat with your right hand. (to a man)"),
    ],
    verify=(vv("خلع", "imp", anta="اِخْلَعْ") + vv("وضع", "jus", anta="تَضَعْ") + vv("رفض", "jus", anta="تَرْفُضْ") + vv("بدأ", "imp", anta="اِبْدَأْ") + vv("وقف", "imp", anta="قِفْ")
            + vw("حِذَاءَكَ", "قَدَمَيْكَ", "الطَّاوِلَة", "بِالسَّلَام", "اِسْأَلْ", "الْأَهْل", "عِنْدَمَا", "السِّنّ", "الْقَهْوَة", "الْيُمْنَى", "بِيَدِكَ", "بِالْعَمَل", "فَوْرًا", "الْأَقَلّ", "مُنَاسِب", "الْبُيُوت", "اُتْرُكِ", "اُسْكُتْ", "كُلْ", "رَفَضَ", "اِجْلِسْ", "الضَّيْف", "خَلَعَ", "اِخْلَعُوا", "كَلَّ", "يَأْكُل", "أَكَلَ")),
)

# ---------------------------------------------------------------------------- 275
L275 = lesson(
    "Weather and delays on the board",
    "بِسَبَب الضَّبَاب تَأَخَّرَتِ الرِّحْلَات",
    requires=["طقس", "ضباب", "مطر", "عاصفة", "سبب", "تأخر", "رحلة", "موعد", "سيء", "رملي"],
    cards=[
        card("Why flights are late",
             "Weather words: الطَّقْس (weather), الضَّبَاب (fog), الْمَطَر (rain), عَاصِفَة رَمْلِيَّة (sandstorm). The reason comes after بِسَبَب (because of). "
             "A flight can be مُتَأَخِّرَة (late), مُؤَجَّلَة (postponed), مُلْغَاة (cancelled) or فِي الْمَوْعِد (on time).",
             tables=[table(["Flight", "To", "Status"],
                           [["١٠٢", "الْقَاهِرَة", "فِي الْمَوْعِد"], ["٢٠٥", "الْكُوَيْت", "مُتَأَخِّرَة"], ["٣١٠", "عَمَّان", "مُؤَجَّلَة"], ["٤٠٤", "بَيْرُوت", "مُلْغَاة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("What the announcer says",
             "The verbs تَأَخَّرَ (it was late) and تَوَقَّفَ (it stopped) take the feminine singular form before a plural of things, exactly as you learned: تَأَخَّرَتِ الرِّحْلَات (not تَأَخَّرَ). These sentences are invented.",
             examples=[
                 ex("الطَّقْس سَيِّئ الْيَوْم.", "The weather is bad today.", "الطَّقْس"),
                 ex("بِسَبَب الضَّبَاب تَأَخَّرَتِ الرِّحْلَات.", "Because of the fog the flights were late.", "تَأَخَّرَتِ"),
                 ex("تَوَقَّفَتِ الرِّحْلَات بِسَبَب الْعَاصِفَة.", "The flights stopped because of the storm.", "تَوَقَّفَتِ"),
                 ex("هُنَاك عَاصِفَة رَمْلِيَّة فِي الْمَدِينَة.", "There is a sandstorm in the city.", "عَاصِفَة رَمْلِيَّة"),
                 ex("سَتَصِل الطَّائِرَة بَعْد سَاعَتَيْن.", "The plane will arrive in two hours.", "سَتَصِل"),
                 ex("رِحْلَتِي فِي الْمَوْعِد وَلَيْسَ هُنَاك تَأْخِير.", "My flight is on time and there is no delay.", "فِي الْمَوْعِد"),
             ]),
    ],
    exercises=[
        M("Which word means “fog”?", "الضَّبَاب", ["الْمَطَر", "الطَّقْس", "الْمَوْعِد"], "ضَبَاب = fog."),
        M("What is a عَاصِفَة رَمْلِيَّة?", "a sandstorm", ["a rainstorm", "a heat wave", "a snowfall"], "رَمْلِيَّة comes from رَمْل (sand)."),
        M("What does مُلْغَاة mean?", "cancelled", ["postponed", "on time", "direct"], "مُلْغَاة = cancelled."),
        M("What does بِسَبَب الضَّبَاب تَأَخَّرَتِ الرِّحْلَات mean?", "Because of the fog the flights were late", ["Because of the flights the fog was late", "The fog cleared the flights", "The flights avoided the fog"], "بِسَبَب = because of."),
        M("Why does the verb end in تِ in تَأَخَّرَتِ الرِّحْلَات؟", "a plural of things takes feminine singular", ["it is a command", "the flights are people", "it is a question"], "Rule: things in the plural → feminine singular."),
        M("What does فِي الْمَوْعِد mean?", "on time", ["in the evening", "at the gate", "in the plane"], "مَوْعِد = appointed time."),
        F("بِسَبَب الضَّبَاب ___ الرِّحْلَات.", "تَأَخَّرَتِ", ["تَأَخَّرَ", "تَأَخَّرُوا", "يَتَأَخَّر"], "Things in the plural → feminine singular.", tr="Because of the fog the flights were late."),
        F("___ سَيِّئ الْيَوْم.", "الطَّقْس", ["الْجَوَاز", "الْمَقْعَد", "الْمُوَظَّف"], "Something that can be bad.", tr="The weather is bad today."),
        F("___ الطَّائِرَة بَعْد سَاعَتَيْن.", "سَتَصِل", ["سَيَصِل", "لَنْ يَصِلُوا", "وَصَلْتُ"], "A feminine subject, future.", tr="The plane will arrive in two hours.", lemma="وصل:fut:hiya"),
    ],
    verify=(vv("وصل", "fut", hiya="سَتَصِل")
            + vw("الطَّقْس", "الضَّبَاب", "الْمَطَر", "عَاصِفَة", "رَمْلِيَّة", "بِسَبَب", "مُتَأَخِّرَة", "مُؤَجَّلَة", "مُلْغَاة", "الْمَوْعِد", "تَأَخَّرَتِ", "تَوَقَّفَتِ", "سَاعَتَيْن", "بَيْرُوت", "سَيِّئ", "الْمَدِينَة", "وَلَيْسَ", "تَأْخِير", "تَأَخَّرَ", "تَأَخَّرُوا", "يَتَأَخَّر", "الْجَوَاز", "الْمَقْعَد", "الْمُوَظَّف", "سَيَصِل", "يَصِلُوا")),
)

# ---------------------------------------------------------------------------- 276
L276 = lesson(
    "Review: a journey to Kuwait",
    "رِحْلَتِي إِلَى الْكُوَيْت: حَجَزْتُ · وَصَلْتُ · وَقَفْتُ",
    requires=["حجز", "تذكرة", "مطار", "وصل", "وقف", "وضع", "ضباب", "تأخر", "رحلة", "فندق"],
    cards=[
        card("What to remember",
             "Three ideas from this chapter. First, before a plural of things the verb is feminine singular: تَأَخَّرَتِ الرِّحْلَات. "
             "Second, an assimilated verb loses its و in the present (يَصِل, يَقِف, يَضَع) and in the command (صِلْ, قِفْ, ضَعْ). "
             "Third, the future and the negations keep the short stem: سَأَصِل, لَنْ أَصِل, لَمْ أَصِلْ.",
             tables=[table(["English", "Arabic"],
                           [["The flights arrived late.", "وَصَلَتِ الرِّحْلَات مُتَأَخِّرَة"], ["We stand in line.", "نَقِف فِي الصَّفّ"], ["Put the bag here! (to a man)", "ضَعِ الْحَقِيبَة هُنَا"],
                            ["I will not arrive before the evening.", "لَنْ أَصِل قَبْل الْمَسَاء"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("My journey (an invented practice text)",
             "A traveller tells the story of one day. The person and the story are made up.",
             examples=[
                 ex("حَجَزْتُ تَذْكِرَة ذَهَاب وَإِيَاب إِلَى الْكُوَيْت.", "I booked a return ticket to Kuwait.", "حَجَزْتُ"),
                 ex("وَصَلْتُ إِلَى الْمَطَار فِي السَّادِسَة صَبَاحًا.", "I arrived at the airport at six in the morning.", "وَصَلْتُ"),
                 ex("وَقَفْتُ فِي الصَّفّ أَمَامَ الْمُوَظَّف.", "I stood in line in front of the official.", "وَقَفْتُ"),
                 ex("قَالَ الْمُوَظَّف: ضَعِ الْحَقِيبَة هُنَا.", "The official said: put the bag here.", "ضَعِ"),
                 ex("بِسَبَب الضَّبَاب تَأَخَّرَتِ الرِّحْلَات سَاعَتَيْن.", "Because of the fog the flights were two hours late.", "تَأَخَّرَتِ"),
                 ex("سَأَصِل إِلَى الْفُنْدُق بَعْد الظُّهْر.", "I will arrive at the hotel in the afternoon.", "سَأَصِل"),
             ]),
    ],
    exercises=[
        M("What did the traveller book?", "a return ticket to Kuwait", ["a hotel in Cairo", "a bus to Amman", "a one-way ticket to Beirut"], "حَجَزْتُ تَذْكِرَة ذَهَاب وَإِيَاب."),
        M("When did the traveller reach the airport?", "at six in the morning", ["at six in the evening", "at noon", "at midnight"], "السَّادِسَة صَبَاحًا."),
        M("What did the official say?", "Put the bag here", ["Open the window", "Stand at the gate", "Show your ticket"], "ضَعِ الْحَقِيبَة هُنَا."),
        M("Why were the flights late?", "because of the fog", ["because of the rain", "because of the tax", "because of the bags"], "بِسَبَب الضَّبَاب."),
        M("Which is correct for “The flights arrived”?", "وَصَلَتِ الرِّحْلَات", ["وَصَلَ الرِّحْلَات", "وَصَلُوا الرِّحْلَات", "وَصَلْتُ الرِّحْلَات"], "Things in the plural → feminine singular."),
        M("Which means “I will not arrive”?", "لَنْ أَصِل", ["سَأَصِل", "لَمْ أَصِلْ", "وَصَلْتُ"], "لَنْ + short present."),
        F("___ فِي الصَّفّ أَمَامَ الْمُوَظَّف.", "وَقَفْتُ", ["أَقِف", "قِفْ", "وَقَفَ"], "I stood: past, with تُ.", tr="I stood in line in front of the official.", lemma="وقف:past:ana"),
        F("___ الْحَقِيبَة هُنَا مِنْ فَضْلِك.", "ضَعِ", ["ضَعُوا", "يَضَع", "وَضَعَ"], "A command to a man.", tr="Put the bag here, please. (to a man)"),
        F("بِسَبَب الضَّبَاب ___ الرِّحْلَات.", "تَأَخَّرَتِ", ["تَأَخَّرَ", "تَأَخَّرُوا", "يَتَأَخَّرُون"], "Things in the plural → feminine singular.", tr="Because of the fog the flights were late."),
    ],
    verify=(vv("وقف", "past", ana="وَقَفْتُ") + vv("حجز", "past", ana="حَجَزْتُ") + vv("وصل", "past", ana="وَصَلْتُ") + vv("وصل", "fut", ana="سَأَصِل") + vv("وقف", "pres", nahnu="نَقِف")
            + vw("السَّادِسَة", "صَبَاحًا", "الْفُنْدُق", "الظُّهْر", "قَالَ", "مُتَأَخِّرَة", "الْمَسَاء", "سَاعَتَيْن", "ضَعُوا", "يَتَأَخَّرُون", "وَصَلَتِ", "وَصَلُوا", "أَقِف", "قِفْ")),
)


UNIT = unit("الْمَطَار وَالسَّفَر: flights, plural things, assimilated verbs and instructions", [L261, L262, L263, L264, L265, L266, L267, L268, L269, L270, L271, L272, L273, L274, L275, L276])
