"""Unit 26 (chapter 24): renting and repairing a car in Morocco, connectors, Measure IX, theft and reports."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 417
L417 = lesson(
    "Renting a car",
    "أُرِيد أَنْ أَسْتَأْجِرَ سَيَّارَة · صَغِيرَة أَمْ كَبِيرَة؟",
    requires=["سيارة", "إيجار", "مطار", "صغير", "كبير", "متوسط", "أسبوع", "أرخص", "نوع", "مدة"],
    cards=[
        card("At the rental desk",
             "To rent a car you say أُرِيد أَنْ أَسْتَأْجِرَ سَيَّارَة. The verb اِسْتَأْجَرَ (Measure X) means “to rent (for yourself)”. The noun for renting is إِيجَار, “rent, hire”. "
             "Cars come in sizes: صَغِيرَة, مُتَوَسِّطَة and كَبِيرَة. The conversation takes place at an airport in Morocco and is invented.",
             tables=[table(["English", "Arabic"],
                           [["to rent", "اِسْتَأْجَرَ"], ["rent", "إِيجَار"], ["small car", "سَيَّارَة صَغِيرَة"], ["medium car", "سَيَّارَة مُتَوَسِّطَة"], ["large car", "سَيَّارَة كَبِيرَة"], ["for a week", "لِمُدَّة أُسْبُوع"], ["weekly", "أُسْبُوعِيّ"], ["cheaper", "أَرْخَص"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُرِيد أَنْ أَسْتَأْجِرَ سَيَّارَة لِمُدَّة أُسْبُوع.", "I want to rent a car for a week.", "أَنْ أَسْتَأْجِرَ"),
                 ex("أَيَّ نَوْع تُرِيد؟ صَغِيرَة أَمْ كَبِيرَة؟", "Which type do you want? Small or large?", "أَيَّ نَوْع"),
                 ex("نُرِيد سَيَّارَة كَبِيرَة لِأَنَّ مَعَنَا حَقَائِب كَثِيرَة.", "We want a large car because we have many bags.", "لِأَنَّ"),
                 ex("كَمْ سِعْر الْإِيجَار فِي الْيَوْم؟", "How much is the rent per day?", "الْإِيجَار"),
                 ex("الْإِيجَار الْأُسْبُوعِيّ أَرْخَص.", "The weekly rent is cheaper.", "أَرْخَص"),
                 ex("سَأَسْتَأْجِر السَّيَّارَة الْمُتَوَسِّطَة.", "I will rent the medium car.", "سَأَسْتَأْجِر"),
             ]),
    ],
    exercises=[
        M("What does اِسْتَأْجَرَ mean?", "to rent", ["to buy", "to drive", "to repair"], "Measure X of أَجَرَ."),
        M("What does إِيجَار mean?", "rent", ["fuel", "insurance", "licence"], "إِيجَار = rent, hire."),
        M("What does أَيَّ نَوْع تُرِيد؟ ask?", "which type you want", ["how old you are", "where you live", "when you return"], "نَوْع = type."),
        M("What does لِمُدَّة أُسْبُوع mean?", "for a week", ["after a week", "in a week", "a week ago"], "مُدَّة = period."),
        M("What does أَرْخَص mean?", "cheaper", ["more expensive", "bigger", "later"], "أَرْخَص = cheaper."),
        M("Why لِأَنَّ in نُرِيد سَيَّارَة كَبِيرَة لِأَنَّ مَعَنَا حَقَائِب?", "to give a reason", ["to ask a question", "to give a command", "to say ‘if’"], "لِأَنَّ = because."),
        F("أُرِيد أَنْ ___ سَيَّارَة لِمُدَّة أُسْبُوع.", "أَسْتَأْجِرَ", ["أَسْتَأْجِرُ", "اِسْتَأْجَرْتُ"], "After أَنْ: ـَ.", tr="I want to rent a car for a week."),
        F("كَمْ سِعْر ___ فِي الْيَوْم؟", "الْإِيجَار", ["الْمُحَرِّك", "الْخَزَّان"], "The price of renting.", tr="How much is the rent per day?"),
        F("الْإِيجَار الْأُسْبُوعِيّ ___.", "أَرْخَص", ["أَكْبَر", "أَقْدَم"], "A weekly rent costs less.", tr="The weekly rent is cheaper."),
        F("نُرِيد سَيَّارَة ___ لِأَنَّ مَعَنَا حَقَائِب كَثِيرَة.", "كَبِيرَة", ["صَغِيرَة", "رَخِيصَة"], "Many bags need a large car.", tr="We want a large car because we have many bags."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 418
L418 = lesson(
    "Terms and conditions",
    "رُخْصَة الْقِيَادَة · رَسْم إِضَافِيّ · خَزَّان مُمْتَلِئ",
    requires=["رخصة", "قيادة", "رسم", "إضافي", "خزان", "كيلومتر", "إعادة", "شرط", "عمر", "سن"],
    cards=[
        card("What the contract says",
             "A rental brochure lists conditions (شُرُوط). You must show your driving licence (رُخْصَة الْقِيَادَة). The driver must be old enough: عُمْر السَّائِق. "
             "A second driver may cost an extra fee (رَسْم إِضَافِيّ). When you return the car (إِعَادَة السَّيَّارَة), the tank should be full (الْخَزَّان مُمْتَلِئ). The terms below are invented.",
             tables=[table(["English", "Arabic"],
                           [["conditions", "شُرُوط"], ["driving licence", "رُخْصَة الْقِيَادَة"], ["age of the driver", "عُمْر السَّائِق"], ["extra fee", "رَسْم إِضَافِيّ"], ["returning the car", "إِعَادَة السَّيَّارَة"], ["full tank", "خَزَّان مُمْتَلِئ"], ["unlimited kilometres", "كِيلُومِتْرَات غَيْر مَحْدُودَة"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أَحْضِرْ رُخْصَة الْقِيَادَة مِنْ فَضْلِكَ.", "Bring your driving licence, please.", "رُخْصَة الْقِيَادَة"),
                 ex("يَجِب أَنْ يَكُونَ عُمْر السَّائِق مُنَاسِبًا.", "The driver’s age must be suitable.", "أَنْ يَكُونَ"),
                 ex("الْكِيلُومِتْرَات غَيْر مَحْدُودَة.", "The kilometres are unlimited.", "غَيْر مَحْدُودَة"),
                 ex("هُنَاكَ رَسْم إِضَافِيّ لِلسَّائِق الثَّانِي.", "There is an extra fee for a second driver.", "رَسْم إِضَافِيّ"),
                 ex("يَجِب أَنْ تُعِيدَ السَّيَّارَة وَالْخَزَّان مُمْتَلِئ.", "You must return the car with the tank full.", "أَنْ تُعِيدَ"),
                 ex("اِقْرَأِ الشُّرُوط قَبْلَ أَنْ تُوَقِّعَ.", "Read the conditions before you sign.", "قَبْلَ أَنْ تُوَقِّعَ"),
             ]),
    ],
    exercises=[
        M("What is رُخْصَة الْقِيَادَة?", "a driving licence", ["a rental fee", "a train ticket", "a map"], "رُخْصَة = licence."),
        M("What does رَسْم إِضَافِيّ mean?", "an extra fee", ["a free gift", "a discount", "a tax refund"], "إِضَافِيّ = additional."),
        M("What does غَيْر مَحْدُودَة mean?", "unlimited", ["short", "forbidden", "cheap"], "مَحْدُود = limited; غَيْر = not."),
        M("What does إِعَادَة السَّيَّارَة mean?", "returning the car", ["renting the car", "washing the car", "buying the car"], "إِعَادَة = return, giving back."),
        M("What does الْخَزَّان مُمْتَلِئ mean?", "the tank is full", ["the tank is empty", "the tank is broken", "the tank is small"], "مُمْتَلِئ = full."),
        M("What does قَبْلَ أَنْ تُوَقِّعَ mean?", "before you sign", ["after you sign", "if you sign", "because you sign"], "قَبْلَ أَنْ + accusative."),
        F("أَحْضِرْ ___ الْقِيَادَة مِنْ فَضْلِكَ.", "رُخْصَة", ["رَسْم", "خَزَّان"], "A licence is shown.", tr="Bring your driving licence, please."),
        F("هُنَاكَ ___ إِضَافِيّ لِلسَّائِق الثَّانِي.", "رَسْم", ["شَرْط", "إِطَار"], "A fee, not a condition.", tr="There is an extra fee for a second driver."),
        F("الْكِيلُومِتْرَات ___ مَحْدُودَة.", "غَيْر", ["لَا", "لَنْ"], "“not limited”.", tr="The kilometres are unlimited."),
        F("اِقْرَأِ الشُّرُوط قَبْلَ أَنْ ___.", "تُوَقِّعَ", ["تُوَقِّعُ", "وَقَّعْتَ"], "After قَبْلَ أَنْ: ـَ.", tr="Read the conditions before you sign."),
    ],
    verify=(vv("وقع#2", "sub", anta="تُوَقِّعَ") + vv("قرأ", "imp", anta="اِقْرَأْ")),
)

# ---------------------------------------------------------------------------- 419
L419 = lesson(
    "Insurance and extras",
    "تَأْمِين شَامِل · هَلِ السِّعْر يَشْمَل؟",
    requires=["تأمين", "شامل", "شمل", "سعر", "خريطة", "ملاحة", "طفل", "مقعد", "إضافي"],
    cards=[
        card("Is it included?",
             "A rental agent offers insurance (تَأْمِين). Full insurance is تَأْمِين شَامِل. To ask whether something is included, use يَشْمَل, “includes”: هَلِ السِّعْر يَشْمَل التَّأْمِين؟ "
             "Extras are things like a navigation system (نِظَام مِلَاحَة) or a child seat (مَقْعَد لِلْأَطْفَال). The sentences are invented.",
             examples=[
                 ex("هَلِ السِّعْر يَشْمَل التَّأْمِين؟", "Does the price include insurance?", "يَشْمَل"),
                 ex("نَعَمْ، السِّعْر يَشْمَل تَأْمِينًا شَامِلًا.", "Yes, the price includes full insurance.", "تَأْمِينًا شَامِلًا"),
                 ex("نِظَام الْمِلَاحَة بِرَسْم إِضَافِيّ.", "The navigation system costs an extra fee.", "نِظَام الْمِلَاحَة"),
                 ex("مَقْعَد الْأَطْفَال مَجَّانًا.", "The child seat is free.", "مَجَّانًا"),
                 ex("هَلْ تُرِيد أَنْ تَأْخُذَ خَرِيطَة؟", "Do you want to take a map?", "خَرِيطَة"),
                 ex("لَنْ أَدْفَعَ رَسْمًا آخَر.", "I will not pay another fee.", "لَنْ أَدْفَعَ"),
             ]),
    ],
    exercises=[
        M("What does تَأْمِين شَامِل mean?", "full insurance", ["no insurance", "weekly rent", "a licence"], "شَامِل = comprehensive."),
        M("What does هَلِ السِّعْر يَشْمَل التَّأْمِين؟ ask?", "whether the price includes insurance", ["how much the insurance costs", "who pays for the insurance", "when the insurance ends"], "يَشْمَل = includes."),
        M("What does مَجَّانًا mean?", "for free", ["quickly", "slowly", "in advance"], "مَجَّانًا = free of charge."),
        M("What is a نِظَام مِلَاحَة?", "a navigation system", ["a fuel tank", "a licence", "a parcel"], "مِلَاحَة = navigation."),
        M("What does لَنْ أَدْفَعَ mean?", "I will not pay", ["I did not pay", "I am paying", "pay!"], "لَنْ + accusative."),
        M("What does مَقْعَد الْأَطْفَال mean?", "the children’s seat", ["the front seat", "the driver’s seat", "the last seat"], "أَطْفَال = children."),
        F("هَلِ السِّعْر ___ التَّأْمِين؟", "يَشْمَل", ["يَدْفَع", "يُغَادِر"], "“includes”.", tr="Does the price include insurance?"),
        F("نِظَام الْمِلَاحَة بِرَسْم ___.", "إِضَافِيّ", ["مُمْتَلِئ", "مَفْتُوح"], "An extra fee.", tr="The navigation system costs an extra fee."),
        F("مَقْعَد الْأَطْفَال ___.", "مَجَّانًا", ["مُغْلَقًا", "غَدًا"], "No charge.", tr="The child seat is free."),
        F("لَنْ ___ رَسْمًا آخَر.", "أَدْفَعَ", ["أَدْفَعُ", "دَفَعْتُ"], "After لَنْ: ـَ.", tr="I will not pay another fee."),
    ],
    verify=(vv("شمل", "pres", huwa="يَشْمَل") + vv("دفع", "sub", ana="أَدْفَعَ")),
)

# ---------------------------------------------------------------------------- 420
L420 = lesson(
    "Parts of the car and its condition",
    "مُحَرِّك · إِطَار · فَرَامِل · بَطَّارِيَّة",
    requires=["محرك", "إطار", "بطارية", "زجاج", "بنزين", "وقود", "خزان", "حالة", "جيد", "مكسور"],
    cards=[
        card("Inside and outside",
             "Before you drive away, you read the description of the car’s condition. The parts have names: the engine (مُحَرِّك), the tyres (إِطَارَات), the brakes (فَرَامِل), the battery (بَطَّارِيَّة), the window glass (زُجَاج), the steering wheel (مِقْوَد) and the lights (مَصَابِيح). "
             "The plural of things takes a feminine singular adjective: الْإِطَارَات جَدِيدَة. The description is invented.",
             tables=[table(["English", "Arabic"],
                           [["engine", "مُحَرِّك"], ["tyre", "إِطَار"], ["tyres", "إِطَارَات"], ["brakes", "فَرَامِل"], ["battery", "بَطَّارِيَّة"], ["glass, windows", "زُجَاج"], ["steering wheel", "مِقْوَد"], ["lights", "مَصَابِيح"], ["petrol", "بِنْزِين"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("الْمُحَرِّك جَيِّد وَالْإِطَارَات جَدِيدَة.", "The engine is good and the tyres are new.", "الْإِطَارَات جَدِيدَة"),
                 ex("الْفَرَامِل تَعْمَل جَيِّدًا.", "The brakes work well.", "الْفَرَامِل"),
                 ex("زُجَاج الْبَاب الْأَيْمَن مَكْسُور.", "The glass of the right door is broken.", "مَكْسُور"),
                 ex("فِي الْبَاب الْأَيْسَر خَدْش صَغِير.", "On the left door there is a small scratch.", "الْأَيْسَر"),
                 ex("الْمَصَابِيح تَعْمَل وَالْخَزَّان مُمْتَلِئ بِالْبِنْزِين.", "The lights work and the tank is full of petrol.", "بِالْبِنْزِين"),
             ]),
    ],
    exercises=[
        M("What is a مُحَرِّك?", "an engine", ["a tyre", "a door", "a licence"], "مُحَرِّك = engine."),
        M("What are فَرَامِل?", "brakes", ["lights", "tyres", "windows"], "فَرَامِل = brakes."),
        M("What does زُجَاج الْبَاب مَكْسُور mean?", "the door glass is broken", ["the door is open", "the door is new", "the door is closed"], "مَكْسُور = broken."),
        M("What does خَدْش mean?", "a scratch", ["a stamp", "a tank", "a light"], "خَدْش = scratch."),
        M("Why جَدِيدَة in الْإِطَارَات جَدِيدَة?", "the plural of things is feminine singular", ["it is a dual", "it is a verb", "it refers to men"], "Plural things → feminine singular."),
        M("What does الْفَرَامِل تَعْمَل جَيِّدًا mean?", "the brakes work well", ["the brakes are broken", "the brakes are new", "the brakes are missing"], "عَمِلَ = to work."),
        F("___ جَيِّد وَالْإِطَارَات جَدِيدَة.", "الْمُحَرِّك", ["الْخَدْش", "الْمِقْوَد"], "The engine is good.", tr="The engine is good and the tyres are new."),
        F("الْإِطَارَات ___.", "جَدِيدَة", ["جَدِيد", "جَدِيدُون"], "Plural of things: feminine singular.", tr="The tyres are new."),
        F("فِي الْبَاب الْأَيْسَر ___ صَغِير.", "خَدْش", ["مُحَرِّك", "رَسْم"], "A small scratch.", tr="On the left door there is a small scratch."),
        F("الْخَزَّان مُمْتَلِئ ___.", "بِالْبِنْزِين", ["بِالْبَطَّارِيَّة", "بِالزُّجَاج"], "A tank is full of petrol.", tr="The tank is full of petrol."),
    ],
    verify=(vv("عمل", "pres", hiya="تَعْمَل")),
)


# ---------------------------------------------------------------------------- 421
L421 = lesson(
    "The car breaks down",
    "تَعَطَّلَتِ السَّيَّارَة · نَفِدَ الْوَقُود",
    requires=["محرك", "إطار", "بطارية", "وقود", "ساخن", "دخان", "توقف", "طريق", "مشكلة"],
    cards=[
        card("What went wrong?",
             "On the road something may go wrong. The car breaks down (تَعَطَّلَتِ السَّيَّارَة), the engine overheats (الْمُحَرِّك سَاخِن), a tyre is punctured (مَثْقُوب), the battery is flat (فَارِغَة) or the fuel runs out (نَفِدَ الْوَقُود). "
             "A feminine noun like سَيَّارَة takes a feminine verb: تَوَقَّفَتْ. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["the car broke down", "تَعَطَّلَتِ السَّيَّارَة"], ["the engine is hot", "الْمُحَرِّك سَاخِن"], ["the tyre is punctured", "الْإِطَار مَثْقُوب"], ["the battery is flat", "الْبَطَّارِيَّة فَارِغَة"], ["the fuel ran out", "نَفِدَ الْوَقُود"], ["smoke", "دُخَان"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("تَعَطَّلَتِ السَّيَّارَة عَلَى الطَّرِيق.", "The car broke down on the road.", "تَعَطَّلَتِ"),
                 ex("الْمُحَرِّك سَاخِن وَيَخْرُج مِنْهُ دُخَان.", "The engine is hot and smoke comes out of it.", "دُخَان"),
                 ex("الْإِطَار مَثْقُوب وَالْبَطَّارِيَّة فَارِغَة.", "The tyre is punctured and the battery is flat.", "مَثْقُوب"),
                 ex("نَفِدَ الْوَقُود فَجْأَةً.", "The fuel ran out suddenly.", "نَفِدَ"),
                 ex("تَوَقَّفَتِ السَّيَّارَة عَلَى جَانِب الطَّرِيق.", "The car stopped at the side of the road.", "جَانِب الطَّرِيق"),
                 ex("مَا الْمُشْكِلَة؟", "What is the problem?", "الْمُشْكِلَة"),
             ]),
    ],
    exercises=[
        M("What does تَعَطَّلَتِ السَّيَّارَة mean?", "The car broke down", ["The car was sold", "The car is new", "The car is fast"], "تَعَطَّلَ = to break down."),
        M("What does الْإِطَار مَثْقُوب mean?", "The tyre is punctured", ["The tyre is new", "The tyre is lost", "The tyre is big"], "مَثْقُوب = pierced."),
        M("What does نَفِدَ الْوَقُود mean?", "The fuel ran out", ["The fuel is cheap", "The fuel is hot", "The fuel is full"], "نَفِدَ = to run out."),
        M("What does الْبَطَّارِيَّة فَارِغَة mean?", "The battery is flat", ["The battery is new", "The battery is full", "The battery is hot"], "فَارِغ = empty."),
        M("What is دُخَان?", "smoke", ["fuel", "glass", "wheel"], "دُخَان = smoke."),
        M("Why تَوَقَّفَتِ and not تَوَقَّفَ?", "سَيَّارَة is feminine", ["it is a dual", "it is a command", "it is plural"], "A feminine subject → ـَتْ."),
        F("___ السَّيَّارَة عَلَى الطَّرِيق.", "تَعَطَّلَتِ", ["تَعَطَّلَ", "تَعَطَّلْتَ"], "A feminine past verb.", tr="The car broke down on the road."),
        F("الْمُحَرِّك سَاخِن وَيَخْرُج مِنْهُ ___.", "دُخَان", ["وَقُود", "إِطَار"], "Smoke comes out of an overheated engine.", tr="The engine is hot and smoke comes out of it."),
        F("___ الْوَقُود فَجْأَةً.", "نَفِدَ", ["نَفِدَتْ", "يَنْفَد"], "الْوَقُود is masculine.", tr="The fuel ran out suddenly."),
        F("تَوَقَّفَتِ السَّيَّارَة عَلَى ___ الطَّرِيق.", "جَانِب", ["سَقْف", "رَسْم"], "“at the side of the road”.", tr="The car stopped at the side of the road."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 422
L422 = lesson(
    "At the mechanic’s",
    "كَمْ تَكْلِفَة الْإِصْلَاح؟ · سَتَكُون جَاهِزَة غَدًا",
    requires=["إصلاح", "ورشة", "فني", "صلح", "فحص", "مشكلة", "مرتفع", "جاهز", "غد"],
    cards=[
        card("Talking about the repair",
             "At the workshop (وَرْشَة), the technician (فَنِّيّ) first examines the car (فَحَصَ). He names the problem, a spare part (قِطْعَة غِيَار), the cost (تَكْلِفَة) and the time. "
             "The verb أَصْلَحَ (Measure IV) means “to repair”; the noun is إِصْلَاح. You can bargain politely. The conversation is invented.",
             examples=[
                 ex("مَا الْمُشْكِلَة؟", "What is the problem?", "مَا"),
                 ex("الْمُحَرِّك سَاخِن جِدًّا.", "The engine is very hot.", "سَاخِن"),
                 ex("سَأَفْحَص السَّيَّارَة الْآن.", "I will examine the car now.", "سَأَفْحَص"),
                 ex("نَحْتَاج إِلَى قِطْعَة غِيَار جَدِيدَة.", "We need a new spare part.", "قِطْعَة غِيَار"),
                 ex("كَمْ تَكْلِفَة الْإِصْلَاح؟", "How much does the repair cost?", "تَكْلِفَة"),
                 ex("السِّعْر مُرْتَفِع، أَرْجُو أَنْ تُخَفِّضَهُ.", "The price is high, please lower it.", "أَنْ تُخَفِّضَهُ"),
                 ex("هَلْ يُمْكِن أَنْ تُصْلِحَهَا الْيَوْم؟", "Can you repair it today?", "أَنْ تُصْلِحَهَا"),
                 ex("سَتَكُون جَاهِزَة غَدًا مَسَاءً.", "It will be ready tomorrow evening.", "سَتَكُون"),
             ]),
    ],
    exercises=[
        M("What is a قِطْعَة غِيَار?", "a spare part", ["a spare key", "a tyre", "a ticket"], "غِيَار = change, spare."),
        M("What does كَمْ تَكْلِفَة الْإِصْلَاح؟ ask?", "how much the repair costs", ["when the repair ends", "who repairs it", "where the workshop is"], "تَكْلِفَة = cost."),
        M("What does سَأَفْحَص السَّيَّارَة mean?", "I will examine the car", ["I examined the car", "I will sell the car", "Examine the car"], "فَحَصَ = to examine."),
        M("What does السِّعْر مُرْتَفِع mean?", "the price is high", ["the price is low", "the price is fair", "the price is free"], "مُرْتَفِع = high."),
        M("What does سَتَكُون جَاهِزَة غَدًا مَسَاءً mean?", "It will be ready tomorrow evening", ["It was ready yesterday", "It is not ready", "It is ready now"], "سَـ + كَانَ = will be."),
        M("What does أَصْلَحَ mean?", "to repair", ["to break", "to drive", "to rent"], "Measure IV: to repair."),
        F("نَحْتَاج إِلَى قِطْعَة ___ جَدِيدَة.", "غِيَار", ["مُحَرِّك", "رَصِيف"], "A spare part.", tr="We need a new spare part."),
        F("كَمْ ___ الْإِصْلَاح؟", "تَكْلِفَة", ["رُخْصَة", "قِيَادَة"], "The cost of a repair.", tr="How much does the repair cost?"),
        F("هَلْ يُمْكِن أَنْ ___ الْيَوْم؟", "تُصْلِحَهَا", ["تُصْلِحُهَا", "أَصْلِحْهَا"], "After أَنْ: ـَ.", tr="Can you repair it today?"),
        F("سَتَكُون ___ غَدًا مَسَاءً.", "جَاهِزَة", ["جَاهِز", "جَاهِزُون"], "السَّيَّارَة is feminine.", tr="It will be ready tomorrow evening."),
    ],
    verify=(vv("صلح#4", "sub", anta="تُصْلِحَ") + vv("فحص", "pres", ana="أَفْحَص")),
)

# ---------------------------------------------------------------------------- 423
L423 = lesson(
    "Connectors: adding, giving reasons, drawing results",
    "وَ · كَمَا · لِأَنَّ · بِسَبَب · لِذَلِكَ",
    requires=["سيارة", "محرك", "وقود", "طريق", "طويل", "هاتف", "توقف", "سبب"],
    cards=[
        card("Joining sentences",
             "To tell a story, join the sentences. For adding information use وَ, “and”, كَمَا, “also, moreover”, أَيْضًا, “also”, and بِالْإِضَافَة إِلَى ذَلِكَ, “in addition to that”. "
             "For a reason use لِأَنَّ, “because”, or بِسَبَب, “because of”. For a result use لِذَلِكَ, “therefore”. After لِأَنَّ comes a noun or a pronoun suffix: لِأَنَّهُ, لِأَنَّهَا.",
             tables=[table(["Function", "Connector", "English"],
                           [["adding", "كَمَا", "moreover"], ["adding", "بِالْإِضَافَة إِلَى ذَلِكَ", "in addition to that"], ["reason", "لِأَنَّ", "because"], ["reason", "بِسَبَب", "because of"], ["result", "لِذَلِكَ", "therefore"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A breakdown story (invented)",
             "A traveller tells what happened.",
             examples=[
                 ex("تَوَقَّفَتِ السَّيَّارَة لِأَنَّ الْوَقُود نَفِدَ.", "The car stopped because the fuel ran out.", "لِأَنَّ"),
                 ex("تَوَقَّفْنَا بِسَبَب الدُّخَان.", "We stopped because of the smoke.", "بِسَبَب"),
                 ex("الْمُحَرِّك سَاخِن، لِذَلِكَ تَوَقَّفْنَا.", "The engine is hot, therefore we stopped.", "لِذَلِكَ"),
                 ex("كَمَا أَنَّ الطَّرِيق طَوِيل.", "Moreover, the road is long.", "كَمَا أَنَّ"),
                 ex("بِالْإِضَافَة إِلَى ذَلِكَ، الْهَاتِف لَا يَعْمَل.", "In addition to that, the phone does not work.", "بِالْإِضَافَة إِلَى ذَلِكَ"),
                 ex("لَمْ نَصِلْ لِأَنَّهَا تَعَطَّلَتْ.", "We did not arrive because it (the car) broke down.", "لِأَنَّهَا"),
             ]),
    ],
    exercises=[
        M("What does لِأَنَّ mean?", "because", ["therefore", "but", "if"], "لِأَنَّ gives a reason."),
        M("What does لِذَلِكَ mean?", "therefore", ["because", "although", "until"], "لِذَلِكَ gives a result."),
        M("What does بِسَبَب mean?", "because of", ["in spite of", "after", "instead of"], "سَبَب = cause."),
        M("What does كَمَا أَنَّ mean?", "moreover", ["however", "because", "in order to"], "It adds information."),
        M("What does لِأَنَّهَا refer to?", "a feminine thing", ["a man", "a group of men", "two things"], "ـهَا = she, it (f.)."),
        M("Which connector adds information?", "بِالْإِضَافَة إِلَى ذَلِكَ", ["لَكِنْ", "لِأَنَّ", "لِذَلِكَ"], "‘In addition to that’."),
        F("تَوَقَّفَتِ السَّيَّارَة ___ الْوَقُود نَفِدَ.", "لِأَنَّ", ["لِذَلِكَ", "لَكِنْ"], "A reason follows.", tr="The car stopped because the fuel ran out."),
        F("الْمُحَرِّك سَاخِن، ___ تَوَقَّفْنَا.", "لِذَلِكَ", ["لِأَنَّ", "رَغْمَ"], "A result follows.", tr="The engine is hot, therefore we stopped."),
        F("تَوَقَّفْنَا ___ الدُّخَان.", "بِسَبَب", ["بَعْدَ أَنْ", "لَوْ"], "A noun follows: because of the smoke.", tr="We stopped because of the smoke."),
        F("لَمْ نَصِلْ ___ تَعَطَّلَتْ.", "لِأَنَّهَا", ["لِأَنَّهُ", "لِأَنَّهُمْ"], "The car is feminine.", tr="We did not arrive because it broke down."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 424
L424 = lesson(
    "Connectors: contrast",
    "لَكِنَّ · أَمَّا… فَـ · بَيْنَمَا · رَغْمَ أَنَّ",
    requires=["قديم", "قوي", "جديد", "سعر", "مرتفع", "إطار", "سيارة", "كبير"],
    cards=[
        card("But, while, although",
             "To set two things against each other use لَكِنَّ, “but”, بَيْنَمَا, “while”, and أَمَّا … فَـ, “as for … ”. To say “although” use رَغْمَ أَنَّ; to say “even so” use مَعَ ذَلِكَ. To correct a statement use بَلْ, “but rather”. "
             "After لَكِنَّ and رَغْمَ أَنَّ a noun is accusative or takes a pronoun suffix: لَكِنَّهَا, “but it”.",
             tables=[table(["Connector", "English"],
                           [["لَكِنَّ", "but"], ["بَيْنَمَا", "while"], ["أَمَّا", "as for … (then …)"], ["رَغْمَ أَنَّ", "although"], ["مَعَ ذَلِكَ", "even so"], ["بَلْ", "but rather"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("In sentences (invented)",
             "Comparing two rental cars.",
             examples=[
                 ex("السَّيَّارَة قَدِيمَة لَكِنَّهَا قَوِيَّة.", "The car is old but it is strong.", "لَكِنَّهَا"),
                 ex("أَمَّا الْمُحَرِّك فَجَيِّد.", "As for the engine, it is good.", "فَجَيِّد"),
                 ex("بَيْنَمَا الْإِطَارَات جَدِيدَة، الْفَرَامِل قَدِيمَة.", "While the tyres are new, the brakes are old.", "بَيْنَمَا"),
                 ex("رَغْمَ أَنَّ السِّعْر مُرْتَفِع، سَنَسْتَأْجِر السَّيَّارَة.", "Although the price is high, we shall rent the car.", "رَغْمَ أَنَّ"),
                 ex("مَعَ ذَلِكَ، لَمْ نَدْفَع رَسْمًا إِضَافِيًّا.", "Even so, we did not pay an extra fee.", "مَعَ ذَلِكَ"),
                 ex("لَيْسَت السَّيَّارَة صَغِيرَة بَلْ كَبِيرَة.", "The car is not small but large.", "بَلْ"),
             ]),
    ],
    exercises=[
        M("What does لَكِنَّ mean?", "but", ["because", "if", "until"], "It contrasts."),
        M("What does بَيْنَمَا mean?", "while", ["because", "after", "so that"], "It sets two things against each other."),
        M("What does رَغْمَ أَنَّ mean?", "although", ["because", "when", "unless"], "A concession."),
        M("What does مَعَ ذَلِكَ mean?", "even so", ["therefore", "first", "for example"], "Concession after a statement."),
        M("What does بَلْ do in لَيْسَت صَغِيرَة بَلْ كَبِيرَة?", "corrects the first statement", ["adds a reason", "gives a condition", "marks time"], "‘Not small but rather large’."),
        M("What does أَمَّا الْمُحَرِّك فَجَيِّد mean?", "As for the engine, it is good", ["The engine is not good", "The engine was good", "If the engine is good"], "أَمَّا … فَـ."),
        F("السَّيَّارَة قَدِيمَة ___ قَوِيَّة.", "لَكِنَّهَا", ["لِأَنَّهَا", "لِذَلِكَ"], "A contrast: old but strong.", tr="The car is old but it is strong."),
        F("___ الْإِطَارَات جَدِيدَة، الْفَرَامِل قَدِيمَة.", "بَيْنَمَا", ["لِأَنَّ", "كَمَا"], "A contrast between two parts.", tr="While the tyres are new, the brakes are old."),
        F("___ أَنَّ السِّعْر مُرْتَفِع، سَنَسْتَأْجِر السَّيَّارَة.", "رَغْمَ", ["بِسَبَب", "بَعْدَ"], "“although”.", tr="Although the price is high, we shall rent the car."),
        F("لَيْسَت السَّيَّارَة صَغِيرَة ___ كَبِيرَة.", "بَلْ", ["لِأَنَّ", "ثُمَّ"], "“but rather”.", tr="The car is not small but large."),
    ],
    verify=(),
)


# ---------------------------------------------------------------------------- 425
L425 = lesson(
    "Connectors: time",
    "عِنْدَمَا · بَعْدَ أَنْ · قَبْلَ أَنْ · أَثْنَاءَ · حَتَّى",
    requires=["وصل", "توقف", "فحص", "سمع", "صوت", "فني", "رحلة", "إطار"],
    cards=[
        card("When did it happen?",
             "To say when something happened relative to something else, use time connectors. عِنْدَمَا, “when”, and بَعْدَ أَنْ, “after”, are followed by a past verb in a story. قَبْلَ أَنْ, “before”, is followed by the accusative (ـَ). "
             "أَثْنَاءَ, “during”, and مُنْذُ, “since, for”, are followed by a noun. حَتَّى, “until”, can be followed by a past verb in a story, or by the accusative when it is still to come. كُلَّمَا means “whenever”.",
             tables=[table(["Connector", "English"],
                           [["عِنْدَمَا", "when"], ["بَعْدَ أَنْ", "after"], ["قَبْلَ أَنْ", "before"], ["أَثْنَاءَ", "during"], ["مُنْذُ", "since, for"], ["حَتَّى", "until"], ["كُلَّمَا", "whenever"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("A journey (invented)",
             "Things happening on a trip to Rabat.",
             examples=[
                 ex("عِنْدَمَا وَصَلْنَا إِلَى الرِّبَاط، تَوَقَّفَتِ السَّيَّارَة.", "When we reached Rabat, the car stopped.", "عِنْدَمَا"),
                 ex("بَعْدَ أَنْ تَوَقَّفْنَا، نَزَلْنَا مِنَ السَّيَّارَة.", "After we stopped, we got out of the car.", "بَعْدَ أَنْ"),
                 ex("قَبْلَ أَنْ نَتَحَرَّكَ، فَحَصْنَا الْإِطَارَات.", "Before we set off, we checked the tyres.", "قَبْلَ أَنْ"),
                 ex("أَثْنَاءَ الرِّحْلَة، سَمِعْنَا صَوْتًا غَرِيبًا.", "During the trip, we heard a strange sound.", "أَثْنَاءَ"),
                 ex("اِنْتَظَرْنَا حَتَّى وَصَلَ الْفَنِّيّ.", "We waited until the technician arrived.", "حَتَّى"),
                 ex("مُنْذُ يَوْمَيْن وَالسَّيَّارَة فِي الْوَرْشَة.", "For two days the car has been in the workshop.", "مُنْذُ"),
             ]),
    ],
    exercises=[
        M("What does عِنْدَمَا mean?", "when", ["until", "because", "if"], "A time connector."),
        M("What does قَبْلَ أَنْ mean?", "before", ["after", "during", "whenever"], "قَبْل = before."),
        M("What does أَثْنَاءَ mean?", "during", ["since", "after", "until"], "أَثْنَاء = during."),
        M("What does مُنْذُ يَوْمَيْن mean?", "for two days", ["in two days", "after two days", "two days later"], "مُنْذُ = since, for."),
        M("Which mood follows قَبْلَ أَنْ?", "accusative", ["jussive", "past", "command"], "أَنْ takes ـَ."),
        M("What does كُلَّمَا mean?", "whenever", ["although", "so that", "unless"], "A repeated time."),
        F("___ وَصَلْنَا إِلَى الرِّبَاط، تَوَقَّفَتِ السَّيَّارَة.", "عِنْدَمَا", ["قَبْلَ", "مُنْذُ"], "“when we arrived”.", tr="When we reached Rabat, the car stopped."),
        F("قَبْلَ أَنْ ___، فَحَصْنَا الْإِطَارَات.", "نَتَحَرَّكَ", ["نَتَحَرَّكُ", "تَحَرَّكْنَا"], "After قَبْلَ أَنْ: ـَ.", tr="Before we set off, we checked the tyres."),
        F("___ الرِّحْلَة، سَمِعْنَا صَوْتًا غَرِيبًا.", "أَثْنَاءَ", ["بَعْدَ أَنْ", "حَتَّى"], "A noun follows: during the trip.", tr="During the trip, we heard a strange sound."),
        F("اِنْتَظَرْنَا ___ وَصَلَ الْفَنِّيّ.", "حَتَّى", ["لِأَنَّ", "رَغْمَ"], "“until”.", tr="We waited until the technician arrived."),
    ],
    verify=(vv("حرك#5", "sub", nahnu="نَتَحَرَّكَ") + vv("فحص", "past", nahnu="فَحَصْنَا")),
)

# ---------------------------------------------------------------------------- 426
L426 = lesson(
    "Connectors: if",
    "إِذَا · لَوْ · إِذَا لَمْ",
    requires=["شركة", "وقود", "محرك", "ورشة", "غد", "جاهز"],
    cards=[
        card("Conditions",
             "Use إِذَا for a condition that may well happen: إِذَا تَعَطَّلَتِ السَّيَّارَة, “if the car breaks down”. The verb after إِذَا is in the past form, even for the future. "
             "Use لَوْ for a condition that is unlikely or impossible, and put لَـ before the result: لَوْ كَانَ مَعَنَا وَقُود لَوَصَلْنَا. For ‘if not’ use إِذَا لَمْ with the jussive. The result of a command often starts with فَـ.",
             tables=[table(["Connector", "English"],
                           [["إِذَا", "if (likely)"], ["لَوْ", "if (unlikely)"], ["إِذَا لَمْ", "if … not"], ["إِنْ شَاءَ اللَّه", "God willing"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("In sentences (invented)",
             "Advice on the road.",
             examples=[
                 ex("إِذَا تَعَطَّلَتِ السَّيَّارَة، فَتَوَقَّفْ عَلَى الْجَانِب.", "If the car breaks down, stop at the side.", "إِذَا"),
                 ex("إِذَا سَخُنَ الْمُحَرِّك، فَأَطْفِئْهُ.", "If the engine gets hot, switch it off.", "سَخُنَ"),
                 ex("لَوْ كَانَ مَعَنَا وَقُود لَوَصَلْنَا.", "If we had had fuel, we would have arrived.", "لَوْ"),
                 ex("إِذَا لَمْ يَعْمَلِ الْمُحَرِّك، سَنَنْتَظِر الْفَنِّيّ.", "If the engine does not work, we will wait for the technician.", "إِذَا لَمْ"),
                 ex("سَتَكُون السَّيَّارَة جَاهِزَة غَدًا إِنْ شَاءَ اللَّه.", "The car will be ready tomorrow, God willing.", "إِنْ شَاءَ اللَّه"),
             ]),
    ],
    exercises=[
        M("What does إِذَا mean?", "if (likely)", ["because", "until", "although"], "A condition."),
        M("What does لَوْ كَانَ مَعَنَا وَقُود لَوَصَلْنَا mean?", "If we had had fuel, we would have arrived", ["We have fuel, so we arrived", "We arrived without fuel", "If we have fuel, we will arrive"], "لَوْ = unreal condition."),
        M("What does إِذَا لَمْ يَعْمَلِ الْمُحَرِّك mean?", "if the engine does not work", ["when the engine works", "because the engine works", "after the engine worked"], "إِذَا لَمْ + jussive."),
        M("Which verb form follows إِذَا?", "past form", ["command", "dual", "passive only"], "The past is used for the condition."),
        M("What does إِنْ شَاءَ اللَّه mean?", "God willing", ["thank God", "good luck", "goodbye"], "A common phrase about the future."),
        M("What starts the result in لَوْ … لَوَصَلْنَا?", "لَـ", ["فَـ", "سَـ", "بَـ"], "The result of لَوْ takes لَـ."),
        F("___ تَعَطَّلَتِ السَّيَّارَة، فَتَوَقَّفْ عَلَى الْجَانِب.", "إِذَا", ["لِأَنَّ", "حَتَّى"], "A likely condition.", tr="If the car breaks down, stop at the side."),
        F("___ كَانَ مَعَنَا وَقُود لَوَصَلْنَا.", "لَوْ", ["إِذَا", "بَلْ"], "An unreal condition: لَوَصَلْنَا.", tr="If we had had fuel, we would have arrived."),
        F("إِذَا ___ يَعْمَلِ الْمُحَرِّك، سَنَنْتَظِر الْفَنِّيّ.", "لَمْ", ["لَنْ", "لَا"], "“does not work”: لَمْ + jussive.", tr="If the engine does not work, we will wait for the technician."),
        F("سَتَكُون جَاهِزَة غَدًا إِنْ ___ اللَّه.", "شَاءَ", ["شَاءَتْ", "يَشَاء"], "The fixed phrase.", tr="It will be ready tomorrow, God willing."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 427
L427 = lesson(
    "Telling the whole story",
    "أَوَّلًا · لِأَنَّ · لَكِنَّ · عِنْدَمَا · لِذَلِكَ",
    requires=["سيارة", "رحلة", "طريق", "ورشة", "فني", "إصلاح", "غد", "صديق"],
    cards=[
        card("A letter about the trip (invented)",
             "Connectors turn single sentences into a story. Read this short letter to a friend and notice each connector: أَوَّلًا, عِنْدَمَا, لَكِنَّ, لِأَنَّ, لِذَلِكَ, بَعْدَ أَنْ, أَخِيرًا.",
             examples=[
                 ex("صَدِيقِي الْعَزِيز، سَافَرْنَا مِنْ فَاس إِلَى طَنْجَة بِسَيَّارَة مُسْتَأْجَرَة.", "My dear friend, we travelled from Fez to Tangier in a rented car.", "بِسَيَّارَة مُسْتَأْجَرَة"),
                 ex("أَوَّلًا حَجَزْنَا السَّيَّارَة مِنْ شَرِكَة صَغِيرَة.", "First we booked the car from a small company.", "أَوَّلًا"),
                 ex("كَانَ الطَّرِيق جَمِيلًا لَكِنَّهُ طَوِيل.", "The road was beautiful but long.", "لَكِنَّهُ"),
                 ex("عِنْدَمَا وَصَلْنَا إِلَى الْجَبَل، سَخُنَ الْمُحَرِّك.", "When we reached the mountain, the engine got hot.", "سَخُنَ"),
                 ex("لِذَلِكَ تَوَقَّفْنَا لِأَنَّ الدُّخَان كَانَ كَثِيرًا.", "So we stopped, because there was a lot of smoke.", "لِذَلِكَ"),
                 ex("بَعْدَ أَنْ كَلَّمْنَا الشَّرِكَة، وَصَلَ الْفَنِّيّ.", "After we spoke to the company, the technician arrived.", "بَعْدَ أَنْ"),
                 ex("أَخِيرًا أَصْلَحَ الْمُحَرِّك، وَسَافَرْنَا مَسَاءً.", "Finally he repaired the engine, and we travelled in the evening.", "أَخِيرًا"),
             ]),
    ],
    exercises=[
        M("What does لَكِنَّهُ طَوِيل mean?", "but it is long", ["because it is long", "so it is long", "although it is long"], "لَكِنَّ + ـهُ."),
        M("Which connector gives the result in ‘so we stopped’?", "لِذَلِكَ", ["لَكِنَّ", "حَتَّى", "رَغْمَ"], "Result."),
        M("Which connector gives the reason in ‘because there was smoke’?", "لِأَنَّ", ["لِذَلِكَ", "بَلْ", "مُنْذُ"], "Reason."),
        M("What does عِنْدَمَا وَصَلْنَا mean?", "when we arrived", ["until we arrived", "because we arrived", "if we arrive"], "Time."),
        M("What does أَخِيرًا mean?", "finally", ["first", "however", "also"], "The last step."),
        M("What does سَافَرْنَا بِسَيَّارَة مُسْتَأْجَرَة mean?", "We travelled in a rented car", ["We rented a car for a friend", "We bought a car", "We sold a car"], "مُسْتَأْجَرَة = rented."),
        F("كَانَ الطَّرِيق جَمِيلًا ___ طَوِيل.", "لَكِنَّهُ", ["لِأَنَّهُ", "لِذَلِكَ"], "A contrast.", tr="The road was beautiful but long."),
        F("___ وَصَلْنَا إِلَى الْجَبَل، سَخُنَ الْمُحَرِّك.", "عِنْدَمَا", ["لَوْ", "رَغْمَ"], "A time connector.", tr="When we reached the mountain, the engine got hot."),
        F("تَوَقَّفْنَا ___ الدُّخَان كَانَ كَثِيرًا.", "لِأَنَّ", ["لِذَلِكَ", "بَعْدَ"], "A reason.", tr="We stopped because there was a lot of smoke."),
        F("___ أَصْلَحَ الْفَنِّيّ الْمُحَرِّك، وَسَافَرْنَا مَسَاءً.", "أَخِيرًا", ["أَوَّلًا", "أَبَدًا"], "The end of the story.", tr="Finally the technician repaired the engine, and we travelled in the evening."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 428
L428 = lesson(
    "Measure IX: turning a colour",
    "اِحْمَرَّ · اِصْفَرَّ · اِخْضَرَّ · اِسْوَدَّ",
    requires=["أحمر", "أصفر", "أخضر", "أزرق", "أسود", "أبيض", "لون", "وجه"],
    cards=[
        card("The pattern اِفْعَلَّ",
             "Measure IX is used for colours and bodily defects. It means “to become that colour” or “to become more strongly that colour”. The pattern is اِفْعَلَّ: the last two letters are joined with a shadda. "
             "From the colour أَحْمَر, “red”, comes اِحْمَرَّ, “turned red”. The present is يَحْمَرُّ.",
             tables=[table(["English", "Colour (m.)", "Colour (f.)", "Verb: became …"],
                           [["red", "أَحْمَر", "حَمْرَاء", "اِحْمَرَّ"], ["yellow", "أَصْفَر", "صَفْرَاء", "اِصْفَرَّ"], ["green", "أَخْضَر", "خَضْرَاء", "اِخْضَرَّ"], ["blue", "أَزْرَق", "زَرْقَاء", "اِزْرَقَّ"], ["black", "أَسْوَد", "سَوْدَاء", "اِسْوَدَّ"], ["white", "أَبْيَض", "بَيْضَاء", "اِبْيَضَّ"]],
                           say=[1, 2, 3], tlit=[1, 2, 3], gloss=False)]),
        card("In sentences (invented)",
             "Things that change colour.",
             examples=[
                 ex("اِحْمَرَّ وَجْهُهُ مِنَ الْغَضَب.", "His face turned red with anger.", "اِحْمَرَّ"),
                 ex("اِصْفَرَّتْ أَوْرَاق الشَّجَرَة فِي الْخَرِيف.", "The leaves of the tree turned yellow in autumn.", "اِصْفَرَّتْ"),
                 ex("اِخْضَرَّ الْعُشْب بَعْدَ الْمَطَر.", "The grass turned green after the rain.", "اِخْضَرَّ"),
                 ex("اِسْوَدَّتِ السَّمَاء قَبْلَ الْمَطَر.", "The sky turned dark before the rain.", "اِسْوَدَّتِ"),
                 ex("اِبْيَضَّ شَعْرُهُ.", "His hair turned white.", "اِبْيَضَّ"),
             ]),
    ],
    exercises=[
        M("What does اِحْمَرَّ mean?", "turned red", ["is red", "painted red", "likes red"], "Measure IX: become red."),
        M("What is the pattern of Measure IX?", "اِفْعَلَّ", ["فَعَّلَ", "فَاعَلَ", "اِسْتَفْعَلَ"], "A shadda on the last letter."),
        M("What does اِخْضَرَّ الْعُشْب mean?", "the grass turned green", ["the grass was cut", "the grass is dry", "the grass burned"], "Measure IX."),
        M("What does اِصْفَرَّتْ mean?", "turned yellow (f.)", ["turned yellow (m.)", "turned red", "is yellow"], "ـَتْ marks a feminine subject."),
        M("What does اِسْوَدَّتِ السَّمَاء mean?", "the sky turned dark", ["the sky was blue", "the sky was clear", "the sky turned red"], "أَسْوَد = black."),
        M("What is the feminine of أَحْمَر?", "حَمْرَاء", ["أَحْمَرَة", "حَمْرَة", "أَحْمَرِيَّة"], "Colour adjectives use فَعْلَاء for the feminine."),
        F("___ وَجْهُهُ مِنَ الْغَضَب.", "اِحْمَرَّ", ["اِحْمَرَّتْ", "أَحْمَر"], "A masculine subject.", tr="His face turned red with anger.", lemma="حمر#9:past:huwa"),
        F("___ أَوْرَاق الشَّجَرَة فِي الْخَرِيف.", "اِصْفَرَّتْ", ["اِصْفَرَّ", "اِصْفَرَرْتُ"], "Things take a feminine singular verb.", tr="The leaves of the tree turned yellow in autumn.", lemma="صفر#9:past:hiya"),
        F("اِخْضَرَّ الْعُشْب بَعْدَ ___.", "الْمَطَر", ["الْمُحَرِّك", "الْمِقْوَد"], "Grass turns green after rain.", tr="The grass turned green after the rain."),
        F("___ شَعْرُهُ.", "اِبْيَضَّ", ["اِبْيَضَّتْ", "أَبْيَض"], "His hair turned white.", tr="His hair turned white.", lemma="بيض#9:past:huwa"),
    ],
    verify=(vv("حمر#9", "past", huwa="اِحْمَرَّ", hiya="اِحْمَرَّتْ") + vv("صفر#9", "past", hiya="اِصْفَرَّتْ") + vv("خضر#9", "past", huwa="اِخْضَرَّ") + vv("سود#9", "past", hiya="اِسْوَدَّتْ") + vv("بيض#9", "past", huwa="اِبْيَضَّ")),
)

# ---------------------------------------------------------------------------- 429
L429 = lesson(
    "Measure IX: all the forms",
    "اِحْمَرَرْتُ · يَحْمَرُّونَ · اِحْمَرَّتَا",
    requires=["أحمر", "أصفر", "أخضر", "أزرق", "وجه", "لون", "خجل", "طفل"],
    cards=[
        card("Joined and split",
             "Measure IX behaves like other doubled verbs. When the ending begins with a vowel (he, she, they), the last two letters stay joined: اِحْمَرَّ, اِحْمَرَّتْ, اِحْمَرُّوا. "
             "When the ending begins with a consonant (I, you, we), the two letters split: اِحْمَرَرْتُ, اِحْمَرَرْنَا. The present is يَحْمَرُّ, تَحْمَرُّ, أَحْمَرُّ, and the women’s plural splits: يَحْمَرِرْنَ.",
             tables=[table(["Person", "Past", "Present"],
                           [["he", "اِحْمَرَّ", "يَحْمَرُّ"], ["she", "اِحْمَرَّتْ", "تَحْمَرُّ"], ["you (m.)", "اِحْمَرَرْتَ", "تَحْمَرُّ"], ["I", "اِحْمَرَرْتُ", "أَحْمَرُّ"], ["we", "اِحْمَرَرْنَا", "نَحْمَرُّ"], ["they (m.)", "اِحْمَرُّوا", "يَحْمَرُّونَ"], ["they (f.)", "اِحْمَرَرْنَ", "يَحْمَرِرْنَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences (invented)",
             "Faces and skies.",
             examples=[
                 ex("اِحْمَرَرْتُ مِنَ الْخَجَل.", "I turned red with embarrassment.", "اِحْمَرَرْتُ"),
                 ex("اِحْمَرَّتْ وُجُوه الْأَطْفَال.", "The children’s faces turned red.", "اِحْمَرَّتْ"),
                 ex("تَحْمَرُّ الشَّمْس عِنْدَ الْغُرُوب.", "The sun turns red at sunset.", "تَحْمَرُّ"),
                 ex("اِزْرَقَّ الْبَحْر بَعْدَ الصَّبَاح.", "The sea turned bluer after the morning.", "اِزْرَقَّ"),
                 ex("يَصْفَرُّ وَرَق الشَّجَر فِي الْخَرِيف.", "The leaves of the trees turn yellow in autumn.", "يَصْفَرُّ"),
             ]),
    ],
    exercises=[
        M("Why do the two letters split in اِحْمَرَرْتُ?", "the ending starts with a consonant", ["the verb is passive", "the verb is a command", "the verb is a dual"], "ـتُ is a consonant ending."),
        M("Which form is ‘they (m.) turned red’?", "اِحْمَرُّوا", ["اِحْمَرَرْنَ", "اِحْمَرَّتْ", "اِحْمَرَرْتُمَا"], "A vowel ending: the letters stay joined."),
        M("What is the present of اِحْمَرَّ (he)?", "يَحْمَرُّ", ["يَحْمُرُ", "يُحَمِّر", "يَحْمَرُ"], "A shadda on the last letter."),
        M("What does تَحْمَرُّ الشَّمْس mean?", "the sun turns red", ["the sun is hot", "the sun rises", "the sun is cold"], "الشَّمْس is feminine: تَـ."),
        M("What does اِحْمَرَرْتُ مِنَ الْخَجَل mean?", "I turned red with embarrassment", ["I painted it red", "I like red", "I was ashamed of red"], "First person."),
        M("Which form is ‘they (f.)’ in the present?", "يَحْمَرِرْنَ", ["يَحْمَرُّونَ", "تَحْمَرُّ", "يَحْمَرَّانِ"], "The women’s plural splits."),
        F("___ مِنَ الْخَجَل.", "اِحْمَرَرْتُ", ["اِحْمَرَّ", "اِحْمَرَّتْ"], "I (consonant ending).", tr="I turned red with embarrassment.", lemma="حمر#9:past:ana"),
        F("___ وُجُوه الْأَطْفَال.", "اِحْمَرَّتْ", ["اِحْمَرَرْتُ", "اِحْمَرُّوا"], "Plural of things → feminine singular.", tr="The children’s faces turned red.", lemma="حمر#9:past:hiya"),
        F("___ الشَّمْس عِنْدَ الْغُرُوب.", "تَحْمَرُّ", ["يَحْمَرُّ", "اِحْمَرَّ"], "A feminine present.", tr="The sun turns red at sunset.", lemma="حمر#9:pres:hiya"),
        F("اِزْرَقَّ الْبَحْر بَعْدَ ___.", "الصَّبَاح", ["الْخَجَل", "الْفَنِّيّ"], "Time of day.", tr="The sea turned bluer after the morning."),
    ],
    verify=(vv("حمر#9", "past", anta="اِحْمَرَرْتَ", ana="اِحْمَرَرْتُ", nahnu="اِحْمَرَرْنَا", hum="اِحْمَرُّوا", hunna="اِحْمَرَرْنَ") + vv("حمر#9", "pres", huwa="يَحْمَرُّ", hiya="تَحْمَرُّ", ana="أَحْمَرُّ", hunna="يَحْمَرِرْنَ") + vv("صفر#9", "pres", huwa="يَصْفَرُّ")),
)

# ---------------------------------------------------------------------------- 430
L430 = lesson(
    "Reporting a theft",
    "سُرِقَتْ حَقِيبَتِي · أُرِيد أَنْ أُبَلِّغَ",
    requires=["شرطة", "سرقة", "سرق", "مسروق", "بلاغ", "حقيبة", "هاتف", "جواز", "زجاج"],
    cards=[
        card("At the police station",
             "If something is stolen, you report it to the police (الشُّرْطَة). The passive سُرِقَتْ, “was stolen”, hides the thief: سُرِقَتْ حَقِيبَتِي. The glass can be broken too: كُسِرَ الزُّجَاج. "
             "To report a crime, say أُرِيد أَنْ أُبَلِّغَ عَنْ سَرِقَة. The officer asks when and where it happened. These lines are invented.",
             tables=[table(["English", "Arabic"],
                           [["police", "الشُّرْطَة"], ["theft", "سَرِقَة"], ["was stolen (f.)", "سُرِقَتْ"], ["was stolen (m.)", "سُرِقَ"], ["was broken (m.)", "كُسِرَ"], ["report", "تَقْرِير"], ["wallet", "مِحْفَظَة"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُرِيد أَنْ أُبَلِّغَ عَنْ سَرِقَة.", "I want to report a theft.", "أَنْ أُبَلِّغَ"),
                 ex("سُرِقَتْ حَقِيبَتِي مِنَ السَّيَّارَة.", "My bag was stolen from the car.", "سُرِقَتْ"),
                 ex("كُسِرَ زُجَاج السَّيَّارَة أَيْضًا.", "The car’s window was also broken.", "كُسِرَ"),
                 ex("مَتَى وَأَيْنَ حَدَثَتِ السَّرِقَة؟", "When and where did the theft happen?", "حَدَثَتِ"),
                 ex("حَدَثَتْ أَمْس مَسَاءً أَمَامَ السُّوق.", "It happened yesterday evening in front of the market.", "أَمَامَ السُّوق"),
                 ex("سَنَكْتُب تَقْرِيرًا وَنَتَّصِل بِكَ.", "We will write a report and call you.", "تَقْرِيرًا"),
             ]),
    ],
    exercises=[
        M("What does سُرِقَتْ حَقِيبَتِي mean?", "My bag was stolen", ["I stole a bag", "My bag is heavy", "I bought a bag"], "The passive of سَرَقَ."),
        M("What does أُرِيد أَنْ أُبَلِّغَ عَنْ سَرِقَة mean?", "I want to report a theft", ["I want to rent a car", "I want to sign a form", "I want to see the police"], "بَلَّغَ عَنْ = to report."),
        M("What does كُسِرَ الزُّجَاج mean?", "the glass was broken", ["the glass is clean", "the glass is new", "the glass was bought"], "Passive of كَسَرَ."),
        M("Why سُرِقَتْ and not سُرِقَ?", "حَقِيبَة is feminine", ["the bag is big", "it is a question", "it is a command"], "A feminine subject → ـَتْ."),
        M("What does مَتَى وَأَيْنَ حَدَثَتِ السَّرِقَة؟ ask?", "when and where it happened", ["who did it", "how much was lost", "why it happened"], "مَتَى = when; أَيْنَ = where."),
        M("What does حَدَثَ mean?", "happened", ["stopped", "started", "ended"], "حَدَثَ = to happen."),
        F("أُرِيد أَنْ ___ عَنْ سَرِقَة.", "أُبَلِّغَ", ["أُبَلِّغُ", "بَلَّغْتُ"], "After أَنْ: ـَ.", tr="I want to report a theft."),
        F("___ حَقِيبَتِي مِنَ السَّيَّارَة.", "سُرِقَتْ", ["سُرِقَ", "سَرَقَتْ"], "Passive, feminine.", tr="My bag was stolen from the car.", lemma="سرق:ppast:hiya"),
        F("___ زُجَاج السَّيَّارَة أَيْضًا.", "كُسِرَ", ["كُسِرَتْ", "كَسَرَ"], "الزُّجَاج is masculine: passive.", tr="The car’s window was also broken.", lemma="كسر:ppast:huwa"),
        F("سَنَكْتُب ___ وَنَتَّصِل بِكَ.", "تَقْرِيرًا", ["تَقْرِيرٌ", "تَقْرِير الْ"], "The object of a verb: accusative tanwīn.", tr="We will write a report and call you."),
    ],
    verify=(vv("سرق", "ppast", hiya="سُرِقَتْ", huwa="سُرِقَ") + vv("كسر", "ppast", huwa="كُسِرَ") + vv("حدث", "past", hiya="حَدَثَتْ")),
)

# ---------------------------------------------------------------------------- 431
L431 = lesson(
    "Describing what was stolen",
    "حَقِيبَة سَوْدَاء · هَاتِف أَسْوَد · اِتَّصِلْ بِالتَّأْمِين",
    requires=["لون", "أسود", "أزرق", "أحمر", "حقيبة", "هاتف", "جواز", "تأمين", "تعويض", "شركة"],
    cards=[
        card("Colour, size, contents",
             "The officer asks you to describe the items. Colours agree with the noun: حَقِيبَة سَوْدَاء (f.), هَاتِف أَسْوَد (m.). Say what was in the bag: فِيهَا, “in it”. "
             "Then call the insurance company (شَرِكَة التَّأْمِين) to ask for compensation (تَعْوِيض). This dialogue is invented.",
             examples=[
                 ex("مَا لَوْن الْحَقِيبَة؟", "What colour is the bag?", "لَوْن"),
                 ex("هِيَ حَقِيبَة سَوْدَاء كَبِيرَة.", "It is a big black bag.", "سَوْدَاء"),
                 ex("فِيهَا هَاتِف أَسْوَد وَمِحْفَظَة زَرْقَاء.", "In it are a black phone and a blue wallet.", "زَرْقَاء"),
                 ex("وَفِيهَا أَيْضًا جَوَاز سَفَرِي.", "And in it also is my passport.", "فِيهَا"),
                 ex("اِتَّصِلْ بِشَرِكَة التَّأْمِين غَدًا.", "Call the insurance company tomorrow.", "اِتَّصِلْ"),
                 ex("أُرِيد أَنْ أَطْلُبَ تَعْوِيضًا.", "I want to ask for compensation.", "تَعْوِيضًا"),
             ]),
    ],
    exercises=[
        M("What does مَا لَوْن الْحَقِيبَة؟ ask?", "what colour the bag is", ["how big the bag is", "where the bag is", "who owns the bag"], "لَوْن = colour."),
        M("Which is correct for a black bag?", "حَقِيبَة سَوْدَاء", ["حَقِيبَة أَسْوَد", "حَقِيبَة سَوْدَاء كَبِيرَ", "حَقِيبَة سُود"], "A feminine noun takes a feminine colour."),
        M("Which is correct for a black phone?", "هَاتِف أَسْوَد", ["هَاتِف سَوْدَاء", "هَاتِف سُودَة", "هَاتِف سَوَد"], "A masculine noun takes أَسْوَد."),
        M("What does فِيهَا mean?", "in it (f.)", ["in him", "in them (m.)", "in you"], "فِي + هَا."),
        M("What is a تَعْوِيض?", "compensation", ["a ticket", "a form", "a licence"], "تَعْوِيض = compensation."),
        M("What does اِتَّصِلْ بِشَرِكَة التَّأْمِين mean?", "Call the insurance company", ["Pay the insurance company", "Visit the police", "Write to the manager"], "اِتَّصَلَ بِـ = to call."),
        F("هِيَ حَقِيبَة ___ كَبِيرَة.", "سَوْدَاء", ["أَسْوَد", "سُود"], "A feminine noun.", tr="It is a big black bag."),
        F("فِيهَا هَاتِف ___.", "أَسْوَد", ["سَوْدَاء", "سَوْدَاوَان"], "A masculine noun.", tr="In it is a black phone."),
        F("وَمِحْفَظَة ___.", "زَرْقَاء", ["أَزْرَق", "زُرْق"], "A feminine noun.", tr="and a blue wallet."),
        F("أُرِيد أَنْ أَطْلُبَ ___.", "تَعْوِيضًا", ["تَعْوِيضٌ", "تَعْوِيض الْ"], "The object of a verb: accusative tanwīn.", tr="I want to ask for compensation."),
    ],
    verify=(vv("طلب", "sub", ana="أَطْلُبَ")),
)


# ---------------------------------------------------------------------------- 432
L432 = lesson(
    "A letter of explanation",
    "أَكْتُب إِلَيْكُمْ لِأَشْرَحَ مَا حَدَثَ",
    requires=["شركة", "تأمين", "إصلاح", "شكر", "رسالة", "تحية", "إيصال", "مرفق"],
    cards=[
        card("Writing to the insurance company",
             "A formal letter has a greeting, the explanation, a request and a polite ending. Open with تَحِيَّة طَيِّبَة وَبَعْد, “greetings, and now”. State your purpose with أَكْتُب إِلَيْكُمْ لِأَشْرَحَ …, “I am writing to you to explain …”. "
             "Tell the story with connectors, ask for what you want with أَرْجُو أَنْ …, and finish with وَشُكْرًا لِتَعَاوُنِكُمْ, “and thank you for your cooperation”. The letter below is invented.",
             examples=[
                 ex("إِلَى شَرِكَة التَّأْمِين الْمُحْتَرَمَة، تَحِيَّة طَيِّبَة وَبَعْد،", "To the esteemed insurance company, kind greetings, and now:", "تَحِيَّة طَيِّبَة وَبَعْد"),
                 ex("أَكْتُب إِلَيْكُمْ لِأَشْرَحَ مَا حَدَثَ أَثْنَاءَ رِحْلَتِي.", "I am writing to you to explain what happened during my trip.", "لِأَشْرَحَ"),
                 ex("عِنْدَمَا كُنْتُ عَلَى الطَّرِيق بَيْنَ الرِّبَاط وَفَاس، تَعَطَّلَتِ السَّيَّارَة.", "When I was on the road between Rabat and Fez, the car broke down.", "عِنْدَمَا كُنْتُ"),
                 ex("لِذَلِكَ اِتَّصَلْتُ بِالْوَرْشَة، وَأَصْلَحُوهَا فِي يَوْم وَاحِد.", "So I called the workshop, and they repaired it in one day.", "لِذَلِكَ"),
                 ex("دَفَعْتُ تَكْلِفَة الْإِصْلَاح، وَأَرْجُو أَنْ تُعِيدُوهَا إِلَيَّ.", "I paid the cost of the repair, and I hope you will pay it back to me.", "أَرْجُو أَنْ"),
                 ex("مَرْفَق بِهَذِهِ الرِّسَالَة الْإِيصَال.", "The receipt is attached to this letter.", "مَرْفَق"),
                 ex("وَشُكْرًا لِتَعَاوُنِكُمْ، مَعَ فَائِق الِاحْتِرَام.", "And thank you for your cooperation, with the highest respect.", "فَائِق الِاحْتِرَام"),
             ]),
    ],
    exercises=[
        M("What does تَحِيَّة طَيِّبَة وَبَعْد begin?", "a formal letter", ["a shopping list", "a recipe", "a bill"], "A usual opening of a letter."),
        M("What does أَكْتُب إِلَيْكُمْ لِأَشْرَحَ mean?", "I am writing to you to explain", ["I wrote to you yesterday", "Write to us to explain", "He explained to you"], "لِـ + accusative = purpose."),
        M("What does مَرْفَق بِهَذِهِ الرِّسَالَة الْإِيصَال mean?", "The receipt is attached to this letter", ["The receipt was lost", "The letter is a receipt", "Send the receipt"], "مَرْفَق = attached."),
        M("What does وَشُكْرًا لِتَعَاوُنِكُمْ express?", "thanks for cooperation", ["a complaint", "an apology", "a request for money"], "تَعَاوُن = cooperation."),
        M("What does أَرْجُو أَنْ تُعِيدُوهَا إِلَيَّ ask?", "that they give it back to me", ["that they repair it", "that they sell it", "that they keep it"], "أَعَادَ = to return."),
        M("Who is addressed in إِلَيْكُمْ?", "a group or company", ["one woman", "one man", "the writer"], "ـكُمْ = you (pl.)."),
        F("أَكْتُب إِلَيْكُمْ ___ مَا حَدَثَ.", "لِأَشْرَحَ", ["لِأَشْرَحْ", "شَرَحْتُ"], "Purpose: لِـ + ـَ.", tr="I am writing to you to explain what happened."),
        F("___ كُنْتُ عَلَى الطَّرِيق، تَعَطَّلَتِ السَّيَّارَة.", "عِنْدَمَا", ["لَكِنَّ", "بَلْ"], "A time connector.", tr="When I was on the road, the car broke down."),
        F("دَفَعْتُ تَكْلِفَة ___، وَأَرْجُو أَنْ تُعِيدُوهَا إِلَيَّ.", "الْإِصْلَاح", ["الْقِيَادَة", "الْمِلَاحَة"], "The cost of the repair.", tr="I paid the cost of the repair, and I hope you will pay it back to me."),
        F("وَشُكْرًا ___، مَعَ فَائِق الِاحْتِرَام.", "لِتَعَاوُنِكُمْ", ["لِتَعَاوُنِكَ", "لِتَعَاوُنِي"], "To a company: ـكُمْ.", tr="And thank you for your cooperation, with the highest respect."),
    ],
    verify=(vv("شرح", "sub", ana="أَشْرَحَ")),
)

# ---------------------------------------------------------------------------- 433
L433 = lesson(
    "The repair report form",
    "تَارِيخ الْعُطْل · مَكَان الْعُطْل · تَكْلِفَة الْإِصْلَاح",
    requires=["تاريخ", "مكان", "عطل", "إصلاح", "مدة", "توقيع"],
    cards=[
        card("Fields on the form",
             "When you return a rented car you may have to fill in a form about any repair. The usual boxes are: تَارِيخ الْعُطْل, “date of the breakdown”, مَكَان الْعُطْل, “place of the breakdown”, نَوْع الْعُطْل, “type of fault”, تَكْلِفَة الْإِصْلَاح, “cost of the repair”, مُدَّة الْإِصْلَاح, “duration of the repair”, and التَّوْقِيع, “signature”. "
             "The agent gives you commands. The lines are invented.",
             tables=[table(["English", "Arabic"],
                           [["date of the breakdown", "تَارِيخ الْعُطْل"], ["place of the breakdown", "مَكَان الْعُطْل"], ["type of fault", "نَوْع الْعُطْل"], ["cost of the repair", "تَكْلِفَة الْإِصْلَاح"], ["duration of the repair", "مُدَّة الْإِصْلَاح"], ["renter", "مُسْتَأْجِر"], ["signature", "التَّوْقِيع"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("اُكْتُبْ تَارِيخ الْعُطْل وَمَكَانَهُ.", "Write the date and place of the breakdown.", "مَكَانَهُ"),
                 ex("اُكْتُبْ نَوْع الْعُطْل: الْمُحَرِّك سَاخِن.", "Write the type of fault: the engine is hot.", "نَوْع الْعُطْل"),
                 ex("سَجِّلْ تَكْلِفَة الْإِصْلَاح وَمُدَّتَهُ.", "Record the cost of the repair and its duration.", "سَجِّلْ"),
                 ex("لَا تَنْسَ اِسْمَ الْمُسْتَأْجِر.", "Do not forget the name of the renter.", "الْمُسْتَأْجِر"),
                 ex("وَقِّعْ فِي الْمَكَان الْمُنَاسِب.", "Sign in the right place.", "وَقِّعْ"),
             ]),
    ],
    exercises=[
        M("What does تَارِيخ الْعُطْل mean?", "date of the breakdown", ["place of the breakdown", "cost of the repair", "type of the car"], "تَارِيخ = date."),
        M("What does مَكَان الْعُطْل mean?", "place of the breakdown", ["date of the breakdown", "name of the garage", "type of fault"], "مَكَان = place."),
        M("What does مُدَّة الْإِصْلَاح mean?", "duration of the repair", ["cost of the repair", "place of the repair", "name of the mechanic"], "مُدَّة = period."),
        M("What does سَجِّلْ mean?", "record! (to one man)", ["sign!", "send!", "wait!"], "Measure II command."),
        M("What does لَا تَنْسَ اِسْمَ الْمُسْتَأْجِر mean?", "Do not forget the renter’s name", ["Write the manager’s name", "I forgot the name", "The name is wrong"], "لَا + jussive."),
        M("Who is the مُسْتَأْجِر?", "the person who rents", ["the person who owns", "the person who repairs", "the person who drives"], "Active participle of اِسْتَأْجَرَ."),
        F("اُكْتُبْ تَارِيخ ___ وَمَكَانَهُ.", "الْعُطْل", ["الْمُحَرِّك", "الْمَقْعَد"], "Date and place of the fault.", tr="Write the date and place of the breakdown."),
        F("___ تَكْلِفَة الْإِصْلَاح وَمُدَّتَهُ.", "سَجِّلْ", ["سَجَّلَ", "يُسَجِّل"], "A command to one man.", tr="Record the cost of the repair and its duration.", lemma="سجل#2:imp:anta"),
        F("لَا ___ اِسْمَ الْمُسْتَأْجِر.", "تَنْسَ", ["تَنْسَى", "نَسِيَ"], "After لَا, the short present.", tr="Do not forget the name of the renter."),
        F("___ فِي الْمَكَان الْمُنَاسِب.", "وَقِّعْ", ["وَقَّعَ", "تُوَقِّع"], "A command to one man.", tr="Sign in the right place.", lemma="وقع#2:imp:anta"),
    ],
    verify=(vv("سجل#2", "imp", anta="سَجِّلْ")),
)

# ---------------------------------------------------------------------------- 434
L434 = lesson(
    "Review: cars, connectors, colours and reports",
    "مُرَاجَعَة الْوَحْدَة",
    requires=["سيارة", "إيجار", "إصلاح", "شرطة", "أحمر", "تأمين", "حقيبة", "رحلة"],
    cards=[
        card("What to remember",
             "Renting: اِسْتَأْجَرَ, إِيجَار, شُرُوط, تَأْمِين. Problems: تَعَطَّلَتِ السَّيَّارَة, نَفِدَ الْوَقُود, تَكْلِفَة الْإِصْلَاح. "
             "Connectors: لِأَنَّ and بِسَبَب (reason), لِذَلِكَ (result), لَكِنَّ and بَيْنَمَا (contrast), عِنْدَمَا and بَعْدَ أَنْ (time), إِذَا and لَوْ (condition). "
             "Measure IX: اِحْمَرَّ, اِصْفَرَّ, اِخْضَرَّ, اِزْرَقَّ, اِسْوَدَّ, اِبْيَضَّ.",
             tables=[table(["Function", "Connector"],
                           [["reason", "لِأَنَّ"], ["result", "لِذَلِكَ"], ["contrast", "لَكِنَّ"], ["time", "عِنْدَمَا"], ["condition", "إِذَا"]],
                           say=[1], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("What does اِسْتَأْجَرَ mean?", "to rent", ["to repair", "to drive", "to steal"], "Measure X."),
        M("What does رَسْم إِضَافِيّ mean?", "an extra fee", ["a free gift", "a licence", "a map"], "إِضَافِيّ = additional."),
        M("What does لِذَلِكَ mean?", "therefore", ["because", "although", "until"], "A result."),
        M("What does بَيْنَمَا mean?", "while", ["after", "so that", "because of"], "A contrast."),
        M("What does اِصْفَرَّتْ mean?", "turned yellow (f.)", ["turned red", "painted yellow", "is yellow (m.)"], "Measure IX."),
        M("What does سُرِقَتْ حَقِيبَتِي mean?", "My bag was stolen", ["I sold my bag", "My bag is new", "I lost my ticket"], "Passive of سَرَقَ."),
        F("تَوَقَّفَتِ السَّيَّارَة ___ الْوَقُود نَفِدَ.", "لِأَنَّ", ["لِذَلِكَ", "بَلْ"], "A reason.", tr="The car stopped because the fuel ran out."),
        F("السَّيَّارَة قَدِيمَة ___ قَوِيَّة.", "لَكِنَّهَا", ["لِذَلِكَ", "عِنْدَمَا"], "A contrast.", tr="The car is old but it is strong."),
        F("___ تَعَطَّلَتِ السَّيَّارَة، فَتَوَقَّفْ عَلَى الْجَانِب.", "إِذَا", ["لِأَنَّ", "حَتَّى"], "A condition.", tr="If the car breaks down, stop at the side."),
        F("اِزْرَقَّ الْبَحْر بَعْدَ ___.", "الصَّبَاح", ["الْإِصْلَاح", "التَّأْمِين"], "Time of day.", tr="The sea turned bluer after the morning."),
        F("هِيَ حَقِيبَة ___ كَبِيرَة.", "سَوْدَاء", ["أَسْوَد", "سُود"], "A feminine noun takes a feminine colour.", tr="It is a big black bag."),
        F("أُرِيد أَنْ ___ عَنْ سَرِقَة.", "أُبَلِّغَ", ["أُبَلِّغُ", "بَلَّغْتُ"], "After أَنْ: ـَ.", tr="I want to report a theft."),
    ],
    verify=(),
)


UNIT = unit("السَّيَّارَة فِي الْمَغْرِب: cars, connectors and Measure IX", [L417, L418, L419, L420, L421, L422, L423, L424, L425, L426, L427, L428, L429, L430, L431, L432, L433, L434])
