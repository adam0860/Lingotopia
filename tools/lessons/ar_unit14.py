"""Unit 14: sights of a town, transport, traffic signs, hollow verbs (present and imperative) and directions (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 199
L199 = lesson(
    "Sights of a seaside town",
    "الْمَتْحَف · الْفَنَار · الشَّاطِئ · الرَّصِيف · مَرْكَز الشُّرْطَة",
    requires=["معلم", "متحف", "شاطئ", "خليج", "حديقة", "ملعب", "مستشفى", "شرطة", "مركز", "ميناء", "مكتب"],
    cards=[
        card("Places to see",
             "A visitor to a town looks for its landmarks (مَعَالِم, the plural of مَعْلَم). Here are common places in a town by the sea. "
             "Many of them are an iḍāfa (“the station of the police”), so the first noun has no ال.",
             tables=[table(["English", "Arabic"],
                           [["landmark, sight", "مَعْلَم"], ["landmarks, sights", "مَعَالِم"], ["museum", "مَتْحَف"],
                            ["lighthouse", "فَنَار"], ["beach", "شَاطِئ"], ["bay", "خَلِيج"], ["harbour", "مِينَاء"],
                            ["pier, quay", "رَصِيف"], ["park", "حَدِيقَة"], ["playing field", "مَلْعَب"],
                            ["hospital", "مُسْتَشْفَى"]],
                           say=[1], tlit=[1], gloss=False),
                    table(["English", "Arabic"],
                          [["police station", "مَرْكَز الشُّرْطَة"], ["fire station", "مَرْكَز الْإِطْفَاء"],
                           ["emergency room", "قِسْم الطَّوَارِئ"], ["information office", "مَكْتَب الِاسْتِعْلَامَات"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("Describing a town",
             "Use the nominal sentences you know: a place + فِي + the town, or a place + قَرِيب مِنْ (near) another. Use فِيهِ / "
             "فِيهَا for “in it”: فِيهِ means “in it” for a masculine noun and فِيهَا for a feminine noun.",
             examples=[
                 ex("فِي الْمَدِينَة السَّاحِلِيَّة مَعَالِم كَثِيرَة.", "There are many sights in the coastal town.", "مَعَالِم"),
                 ex("الْمَتْحَف قَرِيب مِنَ الشَّاطِئ.", "The museum is near the beach.", "قَرِيب مِنَ"),
                 ex("يُشَاهِد الزَّائِر الْفَنَار مِنْ بَعِيد.", "The visitor sees the lighthouse from far away.", "الْفَنَار"),
                 ex("عَلَى الرَّصِيف مَطَاعِم كَثِيرَة وَفِيهِ مَتْجَر لِلْهَدَايَا.", "On the pier there are many restaurants and in it there is a gift shop.", "فِيهِ"),
                 ex("مَكْتَب الِاسْتِعْلَامَات فِي وَسَط الْمَدِينَة.", "The information office is in the middle of the town.", "مَكْتَب الِاسْتِعْلَامَات"),
                 ex("مَرْكَز الشُّرْطَة قَرِيب مِنَ الْمُسْتَشْفَى.", "The police station is near the hospital.", "مَرْكَز الشُّرْطَة"),
             ]),
    ],
    exercises=[
        M("What is the plural of مَعْلَم (landmark)?", "مَعَالِم", ["مَعْلَمَات", "مُعَلِّمُون", "مَعْلَمُون"], "A broken plural."),
        M("Which word means “lighthouse”?", "فَنَار", ["رَصِيف", "شَاطِئ", "مَلْعَب"], "فَنَار = lighthouse."),
        M("Which word means “bay”?", "خَلِيج", ["مِينَاء", "حَدِيقَة", "مَتْحَف"], "خَلِيج = bay, gulf."),
        M("Which means “the police station”?", "مَرْكَز الشُّرْطَة", ["الْمَرْكَز الشُّرْطَة", "مَرْكَز الشُّرْطَة الْ", "شُرْطَة مَرْكَزٌ"], "The first noun of an iḍāfa has no ال."),
        M("Which means “the emergency room”?", "قِسْم الطَّوَارِئ", ["مَكْتَب الِاسْتِعْلَامَات", "مَرْكَز الْإِطْفَاء", "رَصِيف الْمِينَاء"], "طَوَارِئ = emergencies."),
        M("Which place gives visitors information?", "مَكْتَب الِاسْتِعْلَامَات", ["مَرْكَز الشُّرْطَة", "قِسْم الطَّوَارِئ", "مَلْعَب"], "اِسْتِعْلَامَات = enquiries."),
        F("الْمَتْحَف قَرِيب ___ الشَّاطِئ.", "مِنَ", ["فِي", "عَنِ", "عَلَى"], "قَرِيب مِنْ = near.", tr="The museum is near the beach."),
        F("مَكْتَب الِاسْتِعْلَامَات ___ وَسَط الْمَدِينَة.", "فِي", ["مِنْ", "عَنْ", "مَعَ"], "In the middle of.", tr="The information office is in the middle of the town."),
        F("عَلَى الرَّصِيف مَطَاعِم كَثِيرَة وَ___ مَتْجَر لِلْهَدَايَا.", "فِيهِ", ["فِيهَا", "مِنْهُ", "عَلَيْهِ"], "رَصِيف is masculine: in it = فِيهِ.", tr="On the pier there are many restaurants and in it there is a gift shop."),
    ],
    verify=vw("مَعْلَم", "مَعَالِم", "مَتْحَف", "فَنَار", "شَاطِئ", "خَلِيج", "مِينَاء", "رَصِيف", "حَدِيقَة", "مَلْعَب", "مُسْتَشْفَى", "مَرْكَز", "الشُّرْطَة",
              "الْإِطْفَاء", "قِسْم", "الطَّوَارِئ", "الِاسْتِعْلَامَات", "السَّاحِلِيَّة", "الزَّائِر", "بَعِيد", "الْهَدَايَا", "لِلْهَدَايَا"),
)

# ---------------------------------------------------------------------------- 200
L200 = lesson(
    "What can you do there?",
    "يُمْكِنُكَ أَنْ تَمْشِي عَلَى الشَّاطِئ · تُحِبّ زِيَارَة الْمَتْحَف",
    requires=["مشي", "شاطئ", "منظر", "جميل", "ممتع", "سفينة", "غروب", "رحلة", "إذا"],
    cards=[
        card("You can…",
             "To say what is possible, use يُمْكِنُكَ أَنْ (“you can”, to a man) or يُمْكِنُكِ أَنْ (to a woman), then a present verb. "
             "To say what you like, use أُحِبّ and a verbal noun (a noun made from a verb): زِيَارَة الْمَتْحَف (“visiting the museum”). "
             "When the verbal noun is followed by its object, it is the first noun of an iḍāfa and has no ال.",
             tables=[table(["English", "Arabic"],
                           [["strolling on the pier", "التَّجَوُّل عَلَى الرَّصِيف"], ["visiting the museum", "زِيَارَة الْمَتْحَف"],
                            ["watching the sunset", "مُشَاهَدَة غُرُوب الشَّمْس"], ["eating fresh fish", "أَكْل السَّمَك الطَّازَج"],
                            ["a boat trip", "رِحْلَة بِسَفِينَة صَغِيرَة"], ["a beautiful view", "مَنْظَر جَمِيل"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Suggestions for a visitor",
             "With إِذَا (“if”) you can say what to do when you like something: إِذَا كُنْتَ تُحِبّ … فَ …",
             examples=[
                 ex("يُمْكِنُكَ أَنْ تَمْشِي عَلَى الشَّاطِئ فِي الصَّبَاح.", "You can walk on the beach in the morning.", "يُمْكِنُكَ أَنْ"),
                 ex("يُمْكِنُكِ أَنْ تَأْكُلِي السَّمَك الطَّازَج فِي الْمَطْعَم.", "You can eat fresh fish at the restaurant. (to a woman)", "يُمْكِنُكِ أَنْ"),
                 ex("إِذَا كُنْتَ تُحِبّ الْمَتَاحِف فَزُرِ الْمَتْحَف الْقَدِيم.", "If you like museums, visit the old museum.", "إِذَا كُنْتَ تُحِبّ"),
                 ex("أُحِبّ مُشَاهَدَة غُرُوب الشَّمْس مِنَ الرَّصِيف.", "I like watching the sunset from the pier.", "مُشَاهَدَة"),
                 ex("فِي الْمَسَاء مَنْظَر جَمِيل عَلَى الْخَلِيج.", "In the evening there is a beautiful view over the bay.", "مَنْظَر جَمِيل"),
                 ex("يُمْكِنُكُمْ أَنْ تَرْكَبُوا سَفِينَة صَغِيرَة.", "You can take a small boat. (to several people)", "يُمْكِنُكُمْ"),
             ]),
    ],
    exercises=[
        M("Which means “You can walk on the beach”? (to a man)", "يُمْكِنُكَ أَنْ تَمْشِي عَلَى الشَّاطِئ", ["يُمْكِنُكِ أَنْ تَمْشِي عَلَى الشَّاطِئ", "يُمْكِنُنِي أَنْ أَمْشِي عَلَى الشَّاطِئ", "لَا يُمْكِنُكَ أَنْ تَمْشِي"], "يُمْكِنُكَ = you (m.) can."),
        M("Which is the form for a woman?", "يُمْكِنُكِ أَنْ", ["يُمْكِنُكَ أَنْ", "يُمْكِنُهُ أَنْ", "يُمْكِنُنَا أَنْ"], "A kasra for a woman."),
        M("What does مُشَاهَدَة غُرُوب الشَّمْس mean?", "watching the sunset", ["watching the sunrise", "visiting the beach", "buying a boat"], "غُرُوب = setting."),
        M("What does مَنْظَر جَمِيل mean?", "a beautiful view", ["a small boat", "a fresh fish", "a cold wind"], "مَنْظَر = view."),
        M("Which means “If you like museums, visit the old museum”?", "إِذَا كُنْتَ تُحِبّ الْمَتَاحِف فَزُرِ الْمَتْحَف الْقَدِيم", ["إِذَا كُنْتَ تُحِبّ الْمَتَاحِف فَلَا تَزُرِ الْمَتْحَف", "لَوْ كُنْتَ فِي الْمَتْحَف", "إِذَا زُرْتَ الْمَتْحَف"], "إِذَا … فَ …"),
        M("The verbal noun in أُحِبّ مُشَاهَدَة غُرُوب الشَّمْس has…", "no ال", ["ال", "a dual ending", "a feminine plural ending"], "It is the first noun of an iḍāfa."),
        F("يُمْكِنُكِ أَنْ ___ السَّمَك الطَّازَج.", "تَأْكُلِي", ["تَأْكُلُ", "أَكَلَ", "نَأْكُل"], "To a woman: ـِي.", tr="You can eat the fresh fish. (to a woman)"),
        F("أُحِبّ ___ غُرُوب الشَّمْس مِنَ الرَّصِيف.", "مُشَاهَدَة", ["الْمُشَاهَدَة", "شَاهَدْتُ", "مُشَاهِد"], "A verbal noun with no ال.", tr="I like watching the sunset from the pier."),
        F("إِذَا ___ تُحِبّ الْمَتَاحِف فَزُرِ الْمَتْحَف الْقَدِيم.", "كُنْتَ", ["كَانَ", "كُنْتُ", "كُنَّا"], "To a man: ـتَ.", tr="If you like museums, visit the old museum."),
    ],
    verify=(vv("كون", "past", anta="كُنْتَ") + vv("زور", "imp", anta="زُرْ")
            + vw("يُمْكِنُكَ", "يُمْكِنُكِ", "يُمْكِنُكُمْ", "غُرُوب", "مَنْظَر", "جَمِيل", "الْمَتَاحِف", "الْمَتْحَف", "سَفِينَة", "الشَّاطِئ", "الطَّازَج", "السَّمَك",
                 "تَمْشِي", "تَأْكُلِي", "تَرْكَبُوا", "مُشَاهَدَة", "رِحْلَة", "التَّجَوُّل")),
)

# ---------------------------------------------------------------------------- 201
L201 = lesson(
    "A tourist brochure",
    "تُنَظِّم لَكَ الشَّرِكَة رِحْلَات رَائِعَة",
    requires=["رحلة", "مهرجان", "خدمة", "آمن", "ممتع", "مركز", "شركة", "زيارة"],
    cards=[
        card("Words you meet in a brochure",
             "A brochure speaks to “you” (the reader) in the present tense and uses many verbal nouns. These words help you read it.",
             tables=[table(["English", "Arabic"],
                           [["trips", "رِحْلَات"], ["festival", "مَهْرَجَان"], ["annual, yearly", "سَنَوِيّ"], ["services", "خَدَمَات"],
                            ["information", "مَعْلُومَات"], ["safe", "آمِن"], ["enjoyable", "مُمْتِع"], ["wonderful", "رَائِع"],
                            ["to organise", "يُنَظِّم"], ["to enjoy", "يَسْتَمْتِع"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Read the brochure (an invented practice text)",
             "The text is invented for practice. A travel company describes a weekend by the sea.",
             examples=[
                 ex("تُنَظِّم لَكَ شَرِكَتُنَا رِحْلَات رَائِعَة إِلَى الشَّاطِئ.", "Our company organises wonderful trips to the beach for you.", "تُنَظِّم"),
                 ex("يُمْكِنُكَ أَنْ تَسْتَمْتِع بِالْمَهْرَجَان السَّنَوِيّ لِلْمُوسِيقَى.", "You can enjoy the annual music festival.", "تَسْتَمْتِع"),
                 ex("إِذَا كُنْتَ تُحِبّ الْأَسْوَاق الْقَدِيمَة فَسَتَجِد أَشْيَاء كَثِيرَة.", "If you like old markets, you will find many things.", "فَسَتَجِد"),
                 ex("تَجِد الْمَزِيد مِنَ الْمَعْلُومَات فِي مَكْتَب الِاسْتِعْلَامَات.", "You find more information at the information office.", "الْمَزِيد"),
                 ex("كُلّ هَذِهِ الْمَرَاكِز تَجْعَل إِقَامَتَكَ آمِنَة وَمُمْتِعَة.", "All these centres make your stay safe and enjoyable.", "إِقَامَتَكَ"),
                 ex("نَتَمَنَّى لَكَ رِحْلَة سَعِيدَة.", "We wish you a happy trip.", "رِحْلَة سَعِيدَة"),
             ]),
    ],
    exercises=[
        M("What does رِحْلَات mean?", "trips", ["festivals", "services", "museums"], "The plural of رِحْلَة."),
        M("What does مَهْرَجَان سَنَوِيّ mean?", "an annual festival", ["a daily market", "a new museum", "a safe trip"], "سَنَوِيّ = yearly."),
        M("Which word means “services”?", "خَدَمَات", ["مَعْلُومَات", "رِحْلَات", "مَعَالِم"], "خِدْمَة → خَدَمَات."),
        M("Which means “safe”?", "آمِن", ["مُمْتِع", "رَائِع", "سَنَوِيّ"], "آمِن = safe."),
        M("What does نَتَمَنَّى لَكَ رِحْلَة سَعِيدَة mean?", "We wish you a happy trip", ["We organise a trip for you", "You wish us a trip", "We visited a trip"], "نَتَمَنَّى = we wish."),
        M("What does تَجِد الْمَزِيد مِنَ الْمَعْلُومَات mean?", "you find more information", ["you lose the information", "you send the information", "you asked for information"], "الْمَزِيد = more."),
        F("تُنَظِّم لَكَ شَرِكَتُنَا ___ رَائِعَة.", "رِحْلَات", ["رِحْلَة", "الرِّحْلَات", "رَحَلَ"], "Several trips.", tr="Our company organises wonderful trips for you."),
        F("كُلّ هَذِهِ الْمَرَاكِز تَجْعَل إِقَامَتَكَ آمِنَة ___.", "وَمُمْتِعَة", ["وَمُمْتِع", "وَمُمْتِعُونَ", "وَالْمُمْتِعَة"], "Feminine إِقَامَة.", tr="All these centres make your stay safe and enjoyable."),
        F("يُمْكِنُكَ أَنْ ___ بِالْمَهْرَجَان.", "تَسْتَمْتِع", ["تَمْتَعَ", "اِسْتَمْتَعْتُ", "تَسْمَعَ"], "Measure X: يَسْتَمْتِع بِـ.", tr="You can enjoy the festival."),
    ],
    verify=vw("رِحْلَات", "مَهْرَجَان", "الْمَهْرَجَان", "السَّنَوِيّ", "خَدَمَات", "مَعْلُومَات", "الْمَعْلُومَات", "آمِن", "آمِنَة", "مُمْتِع", "مُمْتِعَة", "رَائِع", "رَائِعَة",
              "يُنَظِّم", "تُنَظِّم", "يَسْتَمْتِع", "تَسْتَمْتِع", "الْمَزِيد", "إِقَامَة", "إِقَامَتَكَ", "نَتَمَنَّى", "سَعِيدَة", "الْأَسْوَاق", "شَرِكَتُنَا", "لِلْمُوسِيقَى")
    + vv("نظم#2", "pres", hiya="تُنَظِّم"),
)


# ---------------------------------------------------------------------------- 202
L202 = lesson(
    "Hollow verbs in the present: قَالَ → يَقُول",
    "قَالَ يَقُول · زَارَ يَزُور · عَاشَ يَعِيش · نَامَ يَنَام · بَاعَ يَبِيع",
    requires=["قال", "زار", "عاش", "باع", "نام", "سار", "دار", "قاد", "عاد", "قام"],
    cards=[
        card("A long ā in the middle of the past",
             "Some verbs have a long ā in the middle of the he-form of the past: قَالَ, زَارَ, عَاشَ, بَاعَ, نَامَ. They are called hollow verbs, "
             "because the middle of the root is a weak letter, wāw or yāʾ, hidden inside the ā. In the present tense the weak "
             "letter comes back: يَقُول (wāw), يَبِيع (yāʾ). When the present has a long ā (يَنَام), the weak letter is not "
             "visible, so look the verb up in a dictionary.",
             tables=[table(["English", "Past (he)", "Present (he)", "Middle letter"],
                           [["to say", "قَالَ", "يَقُول", "wāw"], ["to visit", "زَارَ", "يَزُور", "wāw"],
                            ["to turn, to go round", "دَارَ", "يَدُور", "wāw"], ["to drive, to lead", "قَادَ", "يَقُود", "wāw"],
                            ["to live", "عَاشَ", "يَعِيش", "yāʾ"], ["to go, to walk", "سَارَ", "يَسِير", "yāʾ"],
                            ["to sell", "بَاعَ", "يَبِيع", "yāʾ"], ["to sleep", "نَامَ", "يَنَام", "hidden (alif)"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Present tense in sentences",
             "The prefixes are the same as for sound verbs (أَ, نَ, تَ, يَ). Only the middle changes, and the long vowel stays long.",
             examples=[
                 ex("أَقُول صَبَاح الْخَيْر لِلْمُدَرِّس.", "I say good morning to the teacher.", "أَقُول"),
                 ex("أَزُور جَدِّي كُلّ أُسْبُوع.", "I visit my grandfather every week.", "أَزُور"),
                 ex("يَعِيش أَخِي فِي مَدِينَة سَاحِلِيَّة.", "My brother lives in a coastal town.", "يَعِيش"),
                 ex("يَبِيع الصَّيَّاد السَّمَك عَلَى الرَّصِيف.", "The fisherman sells fish on the pier.", "يَبِيع"),
                 ex("تَنَام أُخْتِي مُبَكِّرًا.", "My sister goes to sleep early.", "تَنَام"),
                 ex("أَبِي يَقُود السَّيَّارَة بِبُطْء.", "My father drives the car slowly.", "يَقُود"),
             ]),
    ],
    exercises=[
        M("Which is the present (he) of قَالَ?", "يَقُول", ["يَقُوم", "يَقُود", "يَقِف"], "قَالَ → يَقُول."),
        M("Which is the present (he) of بَاعَ?", "يَبِيع", ["يَبِيت", "يَبِين", "يَبْنِي"], "بَاعَ → يَبِيع."),
        M("Which is the present (he) of عَاشَ?", "يَعِيش", ["يَعُود", "يَعْمَل", "يَعْرِف"], "عَاشَ → يَعِيش."),
        M("What does يَزُور mean?", "he visits", ["he drives", "he sells", "he sleeps"], "زَارَ = to visit."),
        M("Which means “I sleep”?", "أَنَام", ["يَنَام", "نَنَام", "تَنَام"], "أَ- is the I-prefix."),
        M("Why are verbs like قَالَ and بَاعَ called hollow?", "the middle of the root is a weak letter", ["they have a doubled letter", "they begin with hamza", "they end in a long vowel"], "The weak letter hides inside the ā."),
        F("أَخِي ___ فِي مَدِينَة سَاحِلِيَّة.", "يَعِيش", ["يَعُود", "يَبِيع", "يَقُول"], "He lives.", tr="My brother lives in a coastal town.", lemma="عيش:pres:huwa"),
        F("أَنَا ___ جَدِّي كُلّ أُسْبُوع.", "أَزُور", ["أَقُود", "أَبِيع", "أَنَام"], "I visit.", tr="I visit my grandfather every week.", lemma="زور:pres:ana"),
        F("الصَّيَّاد ___ السَّمَك عَلَى الرَّصِيف.", "يَبِيع", ["يَقُول", "يَزُور", "يَسِير"], "He sells.", tr="The fisherman sells fish on the pier.", lemma="بيع:pres:huwa"),
    ],
    verify=(vv("قول", "pres", huwa="يَقُول", ana="أَقُول") + vv("زور", "pres", huwa="يَزُور", ana="أَزُور") + vv("دور", "pres", huwa="يَدُور")
            + vv("قود", "pres", huwa="يَقُود") + vv("عيش", "pres", huwa="يَعِيش") + vv("سير", "pres", huwa="يَسِير")
            + vv("بيع", "pres", huwa="يَبِيع") + vv("نوم", "pres", huwa="يَنَام", ana="أَنَام", hiya="تَنَام")
            + vv("قول", "past", huwa="قَالَ") + vv("زور", "past", huwa="زَارَ") + vv("دور", "past", huwa="دَارَ") + vv("قود", "past", huwa="قَادَ")
            + vv("عيش", "past", huwa="عَاشَ") + vv("سير", "past", huwa="سَارَ") + vv("بيع", "past", huwa="بَاعَ") + vv("نوم", "past", huwa="نَامَ")
            + vw("جَدِّي", "أُسْبُوع", "الصَّيَّاد", "مُبَكِّرًا", "يَقُوم", "يَقِيل", "يَبِيت", "يَبِين", "يَعُود", "يَعْرِف", "يَعْمَل", "يَبْنِي", "يَقُود")),
)

# ---------------------------------------------------------------------------- 203
L203 = lesson(
    "Hollow verbs: all the persons",
    "أَقُول · تَقُولِين · يَقُولُون · نَبِيع · تَنَامُون",
    requires=["قال", "باع", "نام", "كان", "قاد"],
    cards=[
        card("Three verbs, the whole present",
             "Learn the three patterns once. The long vowel stays long in all persons with a vowel ending, and with the endings "
             "ـِين, ـُون and ـَان nothing else changes.",
             tables=[table(["English", "قَالَ (wāw)", "بَاعَ (yāʾ)", "نَامَ (alif)"],
                           [["I", "أَقُول", "أَبِيع", "أَنَام"], ["we", "نَقُول", "نَبِيع", "نَنَام"],
                            ["you (to a man)", "تَقُول", "تَبِيع", "تَنَام"], ["you (to a woman)", "تَقُولِين", "تَبِيعِين", "تَنَامِين"],
                            ["he", "يَقُول", "يَبِيع", "يَنَام"], ["she", "تَقُول", "تَبِيع", "تَنَام"],
                            ["they (men)", "يَقُولُون", "يَبِيعُون", "يَنَامُون"], ["you all (men)", "تَقُولُون", "تَبِيعُون", "تَنَامُون"],
                            ["the two (he)", "يَقُولَان", "يَبِيعَان", "يَنَامَان"]],
                           say=[1, 2, 3], tlit=[1], gloss=False)]),
        card("The short forms for women in the plural",
             "With the plural “they / you (all women)”, the long vowel becomes short and a sukūn comes before the ending ـْنَ: "
             "يَقُلْنَ, تَقُلْنَ, يَبِعْنَ, يَنَمْنَ. The past tense does this for I, you and we, too: قُلْتُ, بِعْتُ, نِمْتُ. In these forms, ā disappears.",
             tables=[table(["English", "Present", "Past"],
                           [["they (women) say", "يَقُلْنَ", "قُلْنَ"], ["you all (women) sell", "تَبِعْنَ", "بِعْتُنَّ"],
                            ["I said", "—", "قُلْتُ"], ["I sold", "—", "بِعْتُ"], ["I slept", "—", "نِمْتُ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("هَلْ تَقُولِين ذَلِكَ لِأُمِّكِ؟", "Do you say that to your mother? (to a woman)", "تَقُولِين"),
                 ex("نَبِيع السَّمَك كُلّ يَوْم.", "We sell fish every day.", "نَبِيع"),
                 ex("الْأَوْلَاد يَنَامُون فِي الْغُرْفَة الْكَبِيرَة.", "The boys sleep in the big room.", "يَنَامُون"),
                 ex("الْبَنَات يَقُلْنَ مَرْحَبًا.", "The girls say hello.", "يَقُلْنَ"),
                 ex("قُلْتُ لَهُ ذَلِكَ أَمْس.", "I told him that yesterday.", "قُلْتُ"),
                 ex("بِعْتُ سَيَّارَتِي الْقَدِيمَة.", "I sold my old car.", "بِعْتُ"),
             ]),
    ],
    exercises=[
        M("Which means “you say” (to a woman)?", "تَقُولِين", ["تَقُول", "تَقُولُون", "يَقُولُون"], "ـِين for a woman."),
        M("Which means “they sell” (men)?", "يَبِيعُون", ["يَبِيع", "يَبِعْنَ", "تَبِيعِين"], "ـُون for men."),
        M("Which means “we sleep”?", "نَنَام", ["أَنَام", "تَنَامُون", "يَنَامُون"], "نَ- is the we-prefix."),
        M("What happens to the long vowel in يَقُلْنَ?", "it becomes short", ["it becomes longer", "it moves to the front", "nothing changes"], "Before ـْنَ the vowel is short."),
        M("Which means “I said”?", "قُلْتُ", ["قَالَ", "قَالُوا", "أَقُول"], "In the past, I = ـْتُ and ā disappears."),
        M("Which means “I slept”?", "نِمْتُ", ["نَامَ", "أَنَام", "نَامُوا"], "نَامَ → نِمْتُ."),
        F("هَلْ ___ ذَلِكَ لِأُمِّكِ؟ (to a woman)", "تَقُولِين", ["تَقُول", "يَقُول", "تَقُولُون"], "Feminine you.", tr="Do you say that to your mother?", lemma="قول:pres:anti"),
        F("الْأَوْلَاد ___ فِي الْغُرْفَة الْكَبِيرَة.", "يَنَامُون", ["يَنَام", "تَنَامِين", "نَنَام"], "Several boys.", tr="The boys sleep in the big room.", lemma="نوم:pres:hum"),
        F("أَمْس ___ سَيَّارَتِي الْقَدِيمَة.", "بِعْتُ", ["بَاعَ", "أَبِيع", "بِعْنَا"], "I sold.", tr="Yesterday I sold my old car.", lemma="بيع:past:ana"),
    ],
    verify=(vv("قول", "pres", ana="أَقُول", nahnu="نَقُول", anta="تَقُول", anti="تَقُولِين", huwa="يَقُول", hiya="تَقُول", hum="يَقُولُون", antum="تَقُولُون", huma_m="يَقُولَان", hunna="يَقُلْنَ")
            + vv("بيع", "pres", ana="أَبِيع", nahnu="نَبِيع", anta="تَبِيع", anti="تَبِيعِين", huwa="يَبِيع", hum="يَبِيعُون", antum="تَبِيعُون", huma_m="يَبِيعَان", antunna="تَبِعْنَ", hunna="يَبِعْنَ")
            + vv("نوم", "pres", ana="أَنَام", nahnu="نَنَام", anta="تَنَام", anti="تَنَامِين", huwa="يَنَام", hum="يَنَامُون", antum="تَنَامُون", huma_m="يَنَامَان", hunna="يَنَمْنَ")
            + vv("قول", "past", ana="قُلْتُ", hunna="قُلْنَ") + vv("بيع", "past", ana="بِعْتُ", antunna="بِعْتُنَّ") + vv("نوم", "past", ana="نِمْتُ")
            + vw("الْأَوْلَاد", "الْبَنَات", "مَرْحَبًا", "أُمِّكِ", "لِأُمِّكِ")),
)

# ---------------------------------------------------------------------------- 204
L204 = lesson(
    "Hollow verbs in conversation",
    "هَلْ تَعِيش هُنَا؟ · مَاذَا تَقُولِين؟ · لَا أَبِيعُهَا",
    requires=["عاش", "قال", "نام", "قاد", "باع", "زار", "هنا", "أسرة"],
    cards=[
        card("Questions and answers",
             "Hollow verbs are very frequent in speech. Here are short exchanges that use them. The question and the answer use the "
             "same verb in a different person: you → I, you → we.",
             examples=[
                 ex("هَلْ تَعِيش فِي الْمَدِينَة؟", "Do you live in the city?", "تَعِيش"),
                 ex("نَعَمْ، أَعِيش هُنَا مَعَ أُسْرَتِي.", "Yes, I live here with my family.", "أَعِيش"),
                 ex("مَاذَا تَقُولِين لِصَدِيقَتِكِ؟", "What do you say to your friend? (to a woman)", "تَقُولِين"),
                 ex("أَقُول لَهَا شُكْرًا.", "I say thank you to her.", "أَقُول"),
                 ex("مَتَى تَنَامُون؟", "When do you all sleep?", "تَنَامُون"),
                 ex("نَنَام فِي السَّاعَة الْعَاشِرَة.", "We go to sleep at ten.", "نَنَام"),
             ]),
        card("Who does what?",
             "With a negative, put لَا before the present verb: لَا أَبِيعُهَا (“I do not sell it”). An object pronoun is attached to the verb "
             "as an ending.",
             examples=[
                 ex("مَنْ يَقُود السَّيَّارَة؟", "Who drives the car?", "يَقُود"),
                 ex("أَبِي يَقُود وَأُمِّي تَنَام.", "My father drives and my mother sleeps.", "تَنَام"),
                 ex("هَلْ تَبِيع سَيَّارَتَكَ؟", "Are you selling your car? (to a man)", "تَبِيع"),
                 ex("لَا، لَا أَبِيعُهَا.", "No, I am not selling it.", "لَا أَبِيعُهَا"),
                 ex("أُخْتِي تَزُور جَدَّتِي كُلّ جُمْعَة.", "My sister visits my grandmother every Friday.", "تَزُور"),
                 ex("هُمْ لَا يَعِيشُون بَعِيدًا عَنَّا.", "They do not live far from us.", "لَا يَعِيشُون"),
             ]),
    ],
    exercises=[
        M("How do you answer هَلْ تَعِيش هُنَا؟ with “Yes, I live here”?", "نَعَمْ، أَعِيش هُنَا", ["نَعَمْ، تَعِيش هُنَا", "نَعَمْ، يَعِيش هُنَا", "نَعَمْ، عِشْتُ هُنَا"], "You → I: أَعِيش."),
        M("What does مَاذَا تَقُولِين؟ ask?", "What do you say? (to a woman)", ["What do you drive?", "Where do you live?", "When do you sleep?"], "تَقُولِين = you (f.) say."),
        M("Which means “We go to sleep at ten”?", "نَنَام فِي السَّاعَة الْعَاشِرَة", ["يَنَامُون فِي السَّاعَة الْعَاشِرَة", "نِمْتُ فِي السَّاعَة الْعَاشِرَة", "أَنَام فِي السَّاعَة الْعَاشِرَة"], "نَ- = we."),
        M("Which means “I do not sell it”?", "لَا أَبِيعُهَا", ["لَا يَبِيعُهَا", "لَا نَبِيعُهَا", "بِعْتُهَا"], "لَا + present."),
        M("Which means “Who drives the car?”", "مَنْ يَقُود السَّيَّارَة؟", ["مَنْ قَادَ السَّيَّارَة؟", "مَاذَا يَقُود السَّيَّارَة؟", "هَلْ تَقُود السَّيَّارَة؟"], "مَنْ = who."),
        M("Which means “They do not live far from us”?", "هُمْ لَا يَعِيشُون بَعِيدًا عَنَّا", ["هُمْ لَا يَعِيش بَعِيدًا عَنَّا", "نَحْنُ لَا نَعِيش بَعِيدًا عَنْهُمْ", "هُمْ عَاشُوا بَعِيدًا عَنَّا"], "لَا + يَعِيشُون."),
        F("أَبِي ___ السَّيَّارَة وَأُمِّي تَنَام.", "يَقُود", ["يَبِيع", "يَزُور", "يَنَام"], "He drives.", tr="My father drives the car and my mother sleeps.", lemma="قود:pres:huwa"),
        F("أُخْتِي ___ جَدَّتِي كُلّ جُمْعَة.", "تَزُور", ["يَزُور", "أَزُور", "تَزُورِين"], "My sister = she.", tr="My sister visits my grandmother every Friday.", lemma="زور:pres:hiya"),
        F("مَتَى ___؟ (to a group)", "تَنَامُون", ["تَنَام", "تَنَامِين", "نَنَام"], "You all.", tr="When do you all sleep?", lemma="نوم:pres:antum"),
    ],
    verify=(vv("عيش", "pres", anta="تَعِيش", ana="أَعِيش", hum="يَعِيشُون") + vv("قول", "pres", anti="تَقُولِين", ana="أَقُول")
            + vv("نوم", "pres", antum="تَنَامُون", nahnu="نَنَام", hiya="تَنَام") + vv("قود", "pres", huwa="يَقُود") + vv("بيع", "pres", anta="تَبِيع", ana="أَبِيع")
            + vv("زور", "pres", hiya="تَزُور") + vw("أُسْرَتِي", "شُكْرًا", "لِصَدِيقَتِكِ", "جَدَّتِي", "سَيَّارَتَكَ", "بَعِيدًا", "عَنَّا", "أَبِيعُهَا", "يَعِيشُون")),
)


# ---------------------------------------------------------------------------- 205
L205 = lesson(
    "Means of transport",
    "الْحَافِلَة · الْقِطَار · الطَّائِرَة · سَيَّارَة الْأُجْرَة",
    requires=["حافلة", "قطار", "طائرة", "سفينة", "شاحنة", "دراجة", "مطار", "محطة", "موقف", "أجرة", "تذكرة", "سائق", "ركب", "نزل", "وصل", "غادر"],
    cards=[
        card("How do you get there?",
             "The general word for transport is مُوَاصَلَات. Most means of transport are feminine nouns. The train, قِطَار, is masculine, and so are "
             "مَطَار (airport) and مَوْقِف (stop). To say “by bus”, use بِـ: بِالْحَافِلَة.",
             tables=[table(["English", "Arabic"],
                           [["bus", "حَافِلَة"], ["train", "قِطَار"], ["plane", "طَائِرَة"], ["ship", "سَفِينَة"], ["truck", "شَاحِنَة"],
                            ["bicycle", "دَرَّاجَة"], ["motorbike", "دَرَّاجَة نَارِيَّة"], ["taxi", "سَيَّارَة أُجْرَة"],
                            ["station", "مَحَطَّة"], ["airport", "مَطَار"], ["bus stop", "مَوْقِف الْحَافِلَات"],
                            ["ticket", "تَذْكِرَة"], ["driver", "سَائِق"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Verbs of travel",
             "Four verbs are useful for any journey. وَصَلَ (to arrive) has a missing و in the present: يَصِل.",
             tables=[table(["English", "Past (he)", "Present (he)"],
                           [["to ride, to board", "رَكِبَ", "يَرْكَب"], ["to get off", "نَزَلَ", "يَنْزِل"],
                            ["to arrive", "وَصَلَ", "يَصِل"], ["to leave", "غَادَرَ", "يُغَادِر"]],
                           say=[1, 2], tlit=[2], gloss=False)],
             examples=[
                 ex("أَرْكَب الْحَافِلَة إِلَى الْمَحَطَّة.", "I take the bus to the station.", "أَرْكَب"),
                 ex("أَنْزِل مِنَ الْقِطَار فِي الْمَحَطَّة الْأَخِيرَة.", "I get off the train at the last station.", "أَنْزِل"),
                 ex("يَصِل الْقِطَار فِي السَّاعَة الثَّالِثَة.", "The train arrives at three o’clock.", "يَصِل"),
                 ex("تُغَادِر الطَّائِرَة الْمَطَار فِي الصَّبَاح.", "The plane leaves the airport in the morning.", "تُغَادِر"),
                 ex("آخُذ سَيَّارَة أُجْرَة مِنَ الْمَطَار إِلَى الْفُنْدُق.", "I take a taxi from the airport to the hotel.", "سَيَّارَة أُجْرَة"),
                 ex("الْمَوْقِف أَمَامَ الْمَحَطَّة.", "The stop is in front of the station.", "الْمَوْقِف"),
             ]),
    ],
    exercises=[
        M("Which means “train”?", "قِطَار", ["حَافِلَة", "طَائِرَة", "شَاحِنَة"], "قِطَار = train."),
        M("Which means “taxi”?", "سَيَّارَة أُجْرَة", ["سَيَّارَة نَارِيَّة", "دَرَّاجَة نَارِيَّة", "مَوْقِف الْحَافِلَات"], "أُجْرَة = fare."),
        M("What does يَصِل mean?", "he arrives", ["he leaves", "he boards", "he gets off"], "وَصَلَ = to arrive."),
        M("What does تُغَادِر الطَّائِرَة الْمَطَار mean?", "The plane leaves the airport", ["The plane arrives at the airport", "The plane is in the airport", "The airport is far"], "غَادَرَ = to leave."),
        M("Which means “I get off the train”?", "أَنْزِل مِنَ الْقِطَار", ["أَرْكَب الْقِطَار", "أَصِل إِلَى الْقِطَار", "أَشْتَرِي الْقِطَار"], "نَزَلَ مِنْ = to get off."),
        M("Which preposition means “by” in بِالْحَافِلَة?", "بِـ", ["فِي", "إِلَى", "مَعَ"], "بِـ + means of transport."),
        F("أَرْكَب ___ إِلَى الْمَحَطَّة.", "الْحَافِلَة", ["الْمَحَطَّة", "الْمَطَار", "الْمَوْقِف"], "Something you ride.", tr="I take the bus to the station."),
        F("آخُذ سَيَّارَة ___ مِنَ الْمَطَار.", "أُجْرَة", ["أُجْرَةً", "الْأُجْرَة", "أَجِير"], "Taxi: an iḍāfa with no ال.", tr="I take a taxi from the airport."),
        F("يَصِل ___ فِي السَّاعَة الثَّالِثَة.", "الْقِطَار", ["الْمَحَطَّة", "الدَّرَّاجَة", "الْمَوْقِف"], "Something that arrives at a station.", tr="The train arrives at three o’clock."),
    ],
    verify=(vv("ركب", "past", huwa="رَكِبَ") + vv("ركب", "pres", huwa="يَرْكَب", ana="أَرْكَب") + vv("نزل", "past", huwa="نَزَلَ") + vv("نزل", "pres", huwa="يَنْزِل", ana="أَنْزِل")
            + vv("غدر#3", "past", huwa="غَادَرَ") + vv("غدر#3", "pres", huwa="يُغَادِر", hiya="تُغَادِر")
            + vw("حَافِلَة", "قِطَار", "طَائِرَة", "سَفِينَة", "شَاحِنَة", "دَرَّاجَة", "نَارِيَّة", "أُجْرَة", "مَحَطَّة", "مَطَار", "مَوْقِف", "الْحَافِلَات", "تَذْكِرَة", "سَائِق",
                 "مُوَاصَلَات", "وَصَلَ", "يَصِل", "آخُذ", "الْفُنْدُق", "الْأَخِيرَة", "الثَّالِثَة")),
)

# ---------------------------------------------------------------------------- 206
L206 = lesson(
    "Which is faster? Comparing transport and journey times",
    "الطَّائِرَة أَسْرَع مِنَ الْقِطَار · تَسْتَغْرِق الرِّحْلَة سَاعَتَيْن",
    requires=["أسرع", "أرخص", "أغلى", "مدة", "ساعة", "دقيقة", "وسيلة", "رحلة", "بطيء", "سريع"],
    cards=[
        card("Faster, slower, cheaper",
             "You already know the pattern أَفْعَل + مِنْ. Use it to compare ways of travelling. The pattern for “slow” is أَبْطَأ (slower).",
             tables=[table(["English", "Adjective", "Comparative"],
                           [["fast", "سَرِيع", "أَسْرَع"], ["slow", "بَطِيء", "أَبْطَأ"], ["cheap", "رَخِيص", "أَرْخَص"],
                            ["expensive", "غَالِي", "أَغْلَى"], ["comfortable", "مُرِيح", "أَرْيَح"], ["safe", "آمِن", "أَكْثَر أَمَانًا"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("How long does it take?",
             "To say how long a journey takes, use تَسْتَغْرِق (“takes”) and a length of time. The numbers 3–10 take the opposite "
             "gender of the noun: سَاعَة is feminine, so ثَلَاث سَاعَات. Two is a dual: سَاعَتَيْن.",
             examples=[
                 ex("الطَّائِرَة أَسْرَع مِنَ الْقِطَار.", "The plane is faster than the train.", "أَسْرَع"),
                 ex("الْقِطَار أَرْخَص مِنَ الطَّائِرَة.", "The train is cheaper than the plane.", "أَرْخَص"),
                 ex("الْحَافِلَة أَبْطَأ مِنَ الْقِطَار.", "The bus is slower than the train.", "أَبْطَأ"),
                 ex("تَسْتَغْرِق الرِّحْلَة بِالْقِطَار سَاعَتَيْن.", "The trip by train takes two hours.", "تَسْتَغْرِق"),
                 ex("تَسْتَغْرِق الرِّحْلَة بِالْحَافِلَة ثَلَاث سَاعَات.", "The trip by bus takes three hours.", "ثَلَاث سَاعَات"),
                 ex("أَفْضَل وَسِيلَة إِلَى الْمَطَار هِيَ سَيَّارَة الْأُجْرَة.", "The best way to the airport is a taxi.", "أَفْضَل وَسِيلَة"),
             ]),
    ],
    exercises=[
        M("Which means “slower”?", "أَبْطَأ", ["أَسْرَع", "أَرْخَص", "أَغْلَى"], "بَطِيء → أَبْطَأ."),
        M("Which means “The plane is faster than the train”?", "الطَّائِرَة أَسْرَع مِنَ الْقِطَار", ["الْقِطَار أَسْرَع مِنَ الطَّائِرَة", "الطَّائِرَة أَبْطَأ مِنَ الْقِطَار", "الطَّائِرَة أَرْخَص مِنَ الْقِطَار"], "أَسْرَع = faster."),
        M("Which means “The train is cheaper than the plane”?", "الْقِطَار أَرْخَص مِنَ الطَّائِرَة", ["الْقِطَار أَغْلَى مِنَ الطَّائِرَة", "الطَّائِرَة أَرْخَص مِنَ الْقِطَار", "الْقِطَار أَبْطَأ مِنَ الطَّائِرَة"], "أَرْخَص = cheaper."),
        M("Which means “three hours”?", "ثَلَاث سَاعَات", ["ثَلَاثَة سَاعَات", "ثَلَاثَة سَاعَة", "سَاعَتَيْن"], "سَاعَة is feminine: opposite gender, ثَلَاث."),
        M("Which means “two hours”?", "سَاعَتَيْن", ["ثَلَاث سَاعَات", "سَاعَة وَاحِدَة", "نِصْف سَاعَة"], "The dual."),
        M("What does تَسْتَغْرِق الرِّحْلَة سَاعَتَيْن mean?", "The trip takes two hours", ["The trip is two hours late", "The trip costs two hours", "The trip left two hours ago"], "تَسْتَغْرِق = takes (time)."),
        F("الْحَافِلَة ___ مِنَ الْقِطَار.", "أَبْطَأ", ["بَطِيئَة", "أَسْرَع", "أَبْطَأَة"], "Slower than the train.", tr="The bus is slower than the train."),
        F("تَسْتَغْرِق الرِّحْلَة بِالْحَافِلَة ___ سَاعَات.", "ثَلَاث", ["ثَلَاثَة", "سَاعَتَيْن", "ثَالِث"], "Opposite gender: feminine noun → ثَلَاث.", tr="The trip by bus takes three hours."),
        F("أَفْضَل ___ إِلَى الْمَطَار هِيَ سَيَّارَة الْأُجْرَة.", "وَسِيلَة", ["الْوَسِيلَة", "وَسِيلَتَيْن", "وَسِيلَةً"], "Best + noun without ال.", tr="The best way to the airport is a taxi."),
    ],
    verify=(vn(3, "f", "ثَلَاث") + vn(10, "f", "عَشْر") + vd("سَاعَة", "سَاعَتَانِ", "سَاعَتَيْنِ")
            + vw("أَسْرَع", "أَبْطَأ", "أَرْخَص", "أَغْلَى", "أَرْيَح", "مُرِيح", "أَمَانًا", "تَسْتَغْرِق", "وَسِيلَة", "بِالْقِطَار", "بِالْحَافِلَة", "سَاعَات", "ثَلَاث", "سَاعَتَيْن", "نِصْف", "أَفْضَل")),
)

# ---------------------------------------------------------------------------- 207
L207 = lesson(
    "Road signs",
    "مَمْنُوع الدُّخُول · مَمْنُوع الْوُقُوف · اِتِّجَاه وَاحِد",
    requires=["ممنوع", "مغلق", "مرور", "سرعة", "إشارة", "طريق", "موقف", "وقف", "أقصى", "أدنى"],
    cards=[
        card("Signs that forbid",
             "مَمْنُوع means “forbidden”. After it comes a verbal noun (a noun made from a verb) with ال, or مُرُور (“passing”) + the "
             "thing that may not pass. Other signs are just short noun phrases.",
             tables=[table(["English", "Arabic"],
                           [["no entry", "مَمْنُوع الدُّخُول"], ["no stopping", "مَمْنُوع الْوُقُوف"],
                            ["no left turn", "مَمْنُوع الدَّوَرَان إِلَى الْيَسَار"], ["no trucks", "مَمْنُوع مُرُور الشَّاحِنَات"],
                            ["no bicycles", "مَمْنُوع مُرُور الدَّرَّاجَات"]],
                           say=[1], tlit=[1], gloss=False),
                    table(["English", "Arabic"],
                          [["road closed", "طَرِيق مُغْلَق"], ["one way", "اِتِّجَاه وَاحِد"], ["bus stop", "مَوْقِف حَافِلَات"],
                           ["maximum speed", "أَقْصَى سُرْعَة"], ["minimum speed", "أَدْنَى سُرْعَة"], ["stop", "قِفْ"], ["danger", "خَطَر"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("Reading signs in sentences",
             "A sign is usually a short phrase without a verb. In a sentence you can explain it: هَذِهِ الْعَلَامَة تَعْنِي …",
             examples=[
                 ex("هَذِهِ الْعَلَامَة تَعْنِي مَمْنُوع الدُّخُول.", "This sign means no entry.", "تَعْنِي"),
                 ex("الطَّرِيق مُغْلَق، فَلَا تَدْخُل.", "The road is closed, so do not enter.", "لَا تَدْخُل"),
                 ex("عِنْدَ إِشَارَة الْمُرُور قِفْ.", "At the traffic light, stop.", "قِفْ"),
                 ex("هَذَا الطَّرِيق السَّرِيع اِتِّجَاه وَاحِد.", "This highway is one way.", "اِتِّجَاه وَاحِد"),
                 ex("أَقْصَى سُرْعَة فِي الْمَدِينَة أَقَلّ مِنْ أَقْصَى سُرْعَة عَلَى الطَّرِيق السَّرِيع.", "The maximum speed in the city is less than the maximum speed on the highway.", "أَقْصَى سُرْعَة"),
                 ex("مَمْنُوع مُرُور الشَّاحِنَات فِي شَوَارِع الْمَدِينَة.", "Trucks may not pass in the city streets.", "مُرُور الشَّاحِنَات"),
             ]),
    ],
    exercises=[
        M("What does مَمْنُوع الدُّخُول mean?", "no entry", ["no stopping", "one way", "bus stop"], "دُخُول = entering."),
        M("What does مَمْنُوع الْوُقُوف mean?", "no stopping", ["no entry", "no left turn", "road closed"], "وُقُوف = stopping."),
        M("Which sign means “one way”?", "اِتِّجَاه وَاحِد", ["طَرِيق مُغْلَق", "مَوْقِف حَافِلَات", "أَقْصَى سُرْعَة"], "اِتِّجَاه = direction."),
        M("Which sign means “road closed”?", "طَرِيق مُغْلَق", ["مَمْنُوع الدُّخُول", "اِتِّجَاه وَاحِد", "خَطَر"], "مُغْلَق = closed."),
        M("What does أَقْصَى سُرْعَة mean?", "maximum speed", ["minimum speed", "no speed", "average speed"], "أَقْصَى = farthest, maximum."),
        M("What does قِفْ mean on a sign?", "stop", ["go", "turn", "wait for the bus"], "قِفْ = stop! (a command)."),
        F("___ مُرُور الشَّاحِنَات فِي شَوَارِع الْمَدِينَة.", "مَمْنُوع", ["مَمْنُوعَة", "مَنَعَ", "مَانِع"], "Forbidden.", tr="Trucks may not pass in the city streets."),
        F("الطَّرِيق ___ فَلَا تَدْخُل.", "مُغْلَق", ["مَفْتُوح", "مَمْنُوعَة", "سَرِيع"], "Closed.", tr="The road is closed, so do not enter."),
        F("هَذِهِ الْعَلَامَة تَعْنِي ___ الدُّخُول.", "مَمْنُوع", ["مُغْلَق", "قِفْ", "أَدْنَى"], "No entry.", tr="This sign means no entry."),
    ],
    verify=(vv("دخل", "neg", anta="لَا تَدْخُل")
            + vw("مَمْنُوع", "الدُّخُول", "الْوُقُوف", "الدَّوَرَان", "مُرُور", "الشَّاحِنَات", "الدَّرَّاجَات", "مُغْلَق", "اِتِّجَاه", "مَوْقِف", "أَقْصَى", "أَدْنَى", "قِفْ", "خَطَر",
                 "الْعَلَامَة", "تَعْنِي", "إِشَارَة", "الْمُرُور", "السَّرِيع", "شَوَارِع", "أَقَلّ")),
)

# ---------------------------------------------------------------------------- 208
L208 = lesson(
    "Rules of the road: must and must not",
    "يَجِب أَنْ تَقِف · لَا يَجُوز أَنْ تَقُود بِسُرْعَة",
    requires=["قاد", "سرعة", "إشارة", "حذر", "مرور", "قيادة", "رخصة"],
    cards=[
        card("Must, may and may not",
             "To say “you must”, use يَجِب أَنْ + a present verb (or عَلَيْكَ أَنْ). To say “it is not allowed”, use لَا يَجُوز أَنْ. "
             "The verb after أَنْ is the present form, but the endings ـِين and ـُون lose their final ن: تَقِفِي, تَقُودُوا. Some roads have their own rules.",
             tables=[table(["English", "Arabic"],
                           [["you must stop (to a man)", "يَجِب أَنْ تَقِف"], ["you must stop (to a woman)", "يَجِب أَنْ تَقِفِي"],
                            ["you may not stop", "لَا يَجُوز أَنْ تَقِف"], ["driving licence", "رُخْصَة الْقِيَادَة"],
                            ["traffic light", "إِشَارَة الْمُرُور"], ["seat belt", "حِزَام الْأَمَان"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("The driver’s rules",
             "Notice that قَادَ (to drive) is a hollow verb: تَقُود. Another useful verb is وَقَفَ (to stop, to stand), which loses its "
             "first و in the present: تَقِف.",
             examples=[
                 ex("يَجِب أَنْ تَقِف عِنْدَ إِشَارَة الْمُرُور.", "You must stop at the traffic light.", "تَقِف"),
                 ex("يَجِب أَنْ تَقُود بِحَذَر.", "You must drive carefully.", "تَقُود"),
                 ex("لَا يَجُوز أَنْ تَقُود بِسُرْعَة كَبِيرَة فِي الْمَدِينَة.", "You may not drive at a high speed in the city.", "لَا يَجُوز"),
                 ex("عَلَيْكِ أَنْ تَقُودِي بِبُطْء فِي الشَّارِع الْمُزْدَحِم.", "You must drive slowly in the crowded street. (to a woman)", "تَقُودِي"),
                 ex("يَجِب أَنْ تَأْخُذ رُخْصَة الْقِيَادَة.", "You must get a driving licence.", "رُخْصَة الْقِيَادَة"),
                 ex("لَا يَجُوز الْوُقُوف أَمَامَ مَوْقِف الْحَافِلَات.", "Stopping in front of the bus stop is not allowed.", "لَا يَجُوز"),
             ]),
    ],
    exercises=[
        M("Which means “You must stop at the light”?", "يَجِب أَنْ تَقِف عِنْدَ إِشَارَة الْمُرُور", ["لَا يَجُوز أَنْ تَقِف عِنْدَ إِشَارَة الْمُرُور", "يَجِب أَنْ تَسِير عِنْدَ إِشَارَة الْمُرُور", "يَجِب أَنْ تَقُول عِنْدَ إِشَارَة الْمُرُور"], "يَجِب أَنْ = must."),
        M("What does لَا يَجُوز أَنْ تَقُود بِسُرْعَة mean?", "You may not drive fast", ["You must drive fast", "You drove fast", "You can drive fast"], "لَا يَجُوز = not allowed."),
        M("Which is “you drive” (to a man)?", "تَقُود", ["تَقُودِين", "يَقُود", "قَادَ"], "قَادَ → تَقُود."),
        M("Which is the form for a woman: “you drive”?", "تَقُودِين", ["تَقُود", "تَقُودُون", "تَقُلْنَ"], "ـِين for a woman."),
        M("What does رُخْصَة الْقِيَادَة mean?", "driving licence", ["traffic light", "seat belt", "road sign"], "قِيَادَة = driving."),
        M("Which is the present “you stop” (to a man)?", "تَقِف", ["تَقُول", "تَقُود", "تَقْطَع"], "وَقَفَ loses its و."),
        F("يَجِب أَنْ ___ بِحَذَر.", "تَقُود", ["تَقُول", "تَقُودُون", "تَقُودِين"], "You (to a man) drive.", tr="You must drive carefully.", lemma="قود:pres:anta"),
        F("لَا ___ أَنْ تَقُود بِسُرْعَة كَبِيرَة.", "يَجُوز", ["يَكُون", "يَصِل", "يُرِيد"], "Not allowed.", tr="You may not drive at a high speed."),
        F("يَجِب أَنْ تَقِف عِنْدَ ___ الْمُرُور.", "إِشَارَة", ["الْإِشَارَة", "إِشَارَةً", "أَشَار"], "An iḍāfa: no ال on the first noun.", tr="You must stop at the traffic light."),
    ],
    verify=(vv("قود", "pres", anta="تَقُود", anti="تَقُودِين", huwa="يَقُود")
            + vw("يَجِب", "يَجُوز", "تَقِف", "رُخْصَة", "الْقِيَادَة", "حِزَام", "الْأَمَان", "بِحَذَر", "بِبُطْء", "الْمُزْدَحِم", "الْوُقُوف", "تَقُودِي", "تَأْخُذ", "عَلَيْكِ")),
)


# ---------------------------------------------------------------------------- 209
L209 = lesson(
    "Commands with hollow verbs: قُلْ · سِرْ · نَمْ",
    "قُلْ · زُرْ · دُرْ · سِرْ · بِعْ · نَمْ · كُنْ",
    requires=["قال", "زار", "دار", "سار", "باع", "نام", "كان", "قاد", "عاش"],
    cards=[
        card("Two steps",
             "To make a command to one man from a hollow verb, take the present form and (1) drop the prefix يَـ, (2) delete the long vowel in the middle, "
             "(3) put the vowel of that long vowel on the first root letter: ُ for يَقُول, ِ for يَبِيع and َ for يَنَام. The last letter gets a sukūn.",
             tables=[table(["English", "Present (he)", "Command (to a man)"],
                           [["say", "يَقُول", "قُلْ"], ["visit", "يَزُور", "زُرْ"], ["turn", "يَدُور", "دُرْ"], ["drive", "يَقُود", "قُدْ"],
                            ["live", "يَعِيش", "عِشْ"], ["go, walk", "يَسِير", "سِرْ"], ["sell", "يَبِيع", "بِعْ"],
                            ["sleep", "يَنَام", "نَمْ"], ["be", "يَكُون", "كُنْ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Commands in use",
             "When the next word starts with ال, a short kasra joins the two words: قُدِ السَّيَّارَة, نَمِ الْآن. "
             "To forbid, use لَا and the present with a sukūn: لَا تَقُلْ (“do not say”), لَا تَنَمْ.",
             examples=[
                 ex("قُلْ لِي أَيْنَ الْمَحَطَّة.", "Tell me where the station is.", "قُلْ"),
                 ex("دُرْ إِلَى الْيَمِين عِنْدَ الْإِشَارَة.", "Turn right at the light.", "دُرْ"),
                 ex("سِرْ إِلَى نِهَايَة الشَّارِع.", "Go to the end of the street.", "سِرْ"),
                 ex("قُدِ السَّيَّارَة بِبُطْء.", "Drive the car slowly.", "قُدِ"),
                 ex("نَمِ الْآن، فَالْوَقْت مُتَأَخِّر.", "Go to sleep now, it is late.", "نَمِ"),
                 ex("لَا تَقُلْ ذَلِكَ لِأَحَد.", "Do not say that to anyone.", "لَا تَقُلْ"),
             ]),
    ],
    exercises=[
        M("Which is the command (to a man) from يَقُول?", "قُلْ", ["قَالَ", "يَقُلْ", "قُولِي"], "Delete the middle, ُ on the first letter, sukūn at the end."),
        M("Which is the command from يَبِيع?", "بِعْ", ["بَاعَ", "بُعْ", "بِيعِي"], "يَبِيع has a kasra."),
        M("Which is the command from يَنَام?", "نَمْ", ["نِمْ", "نُمْ", "نَامَ"], "يَنَام has fatḥa."),
        M("Which is the command from يَدُور?", "دُرْ", ["دَرْ", "دِرْ", "دَارَ"], "ُ for wāw verbs."),
        M("Which means “Do not say that”?", "لَا تَقُلْ ذَلِكَ", ["قُلْ ذَلِكَ", "لَا تَقُول ذَلِكَ", "لَمْ يَقُلْ ذَلِكَ"], "لَا + present with a sukūn."),
        M("Why is it نَمِ الْآن, with a kasra?", "to join the sukūn to ال", ["it is feminine", "it is plural", "it is the past"], "A helping vowel before ال."),
        F("___ إِلَى نِهَايَة الشَّارِع.", "سِرْ", ["سَارَ", "يَسِير", "سِيرِي"], "Command to a man.", tr="Go to the end of the street. (to a man)", lemma="سير:imp:anta"),
        F("___ لِي أَيْنَ الْمَحَطَّة.", "قُلْ", ["قُولِي", "يَقُول", "قَالَ"], "Command to a man.", tr="Tell me where the station is. (to a man)", lemma="قول:imp:anta"),
        F("___ ذَلِكَ لِأَحَد.", "لَا تَقُلْ", ["قُلْ", "لَا تَقُول", "لَمْ تَقُلْ"], "Negative command: لَا + short present.", tr="Do not say that to anyone.", lemma="قول:neg:anta"),
    ],
    verify=(vv("قول", "imp", anta="قُلْ") + vv("زور", "imp", anta="زُرْ") + vv("دور", "imp", anta="دُرْ") + vv("قود", "imp", anta="قُدْ")
            + vv("عيش", "imp", anta="عِشْ") + vv("سير", "imp", anta="سِرْ") + vv("بيع", "imp", anta="بِعْ") + vv("نوم", "imp", anta="نَمْ") + vv("كون", "imp", anta="كُنْ")
            + vv("قول", "neg", anta="لَا تَقُلْ") + vv("نوم", "neg", anta="لَا تَنَمْ")
            + vw("نِهَايَة", "الشَّارِع", "مُتَأَخِّر", "الْمَحَطَّة", "أَحَد", "لِأَحَد")),
)

# ---------------------------------------------------------------------------- 210
L210 = lesson(
    "Commands to a woman and to a group",
    "قُولِي · سِيرِي · نَامِي · قُولُوا · سِيرُوا · لَا تَقُولُوا",
    requires=["قال", "سار", "نام", "باع", "كان", "قاد", "عاش"],
    cards=[
        card("Women and groups",
             "For a woman add ـِي to the command stem, and for a group of men add ـُوا. Because the ending is a long vowel, the "
             "middle vowel comes back and is long again: قُولِي, قُولُوا. Only the form for one man is short.",
             tables=[table(["English", "To a man", "To a woman", "To a group"],
                           [["say", "قُلْ", "قُولِي", "قُولُوا"], ["go, walk", "سِرْ", "سِيرِي", "سِيرُوا"],
                            ["sell", "بِعْ", "بِيعِي", "بِيعُوا"], ["sleep", "نَمْ", "نَامِي", "نَامُوا"],
                            ["drive", "قُدْ", "قُودِي", "قُودُوا"], ["be", "كُنْ", "كُونِي", "كُونُوا"],
                            ["live", "عِشْ", "عِيشِي", "عِيشُوا"]],
                           say=[1, 2, 3], tlit=[2, 3], gloss=False)]),
        card("In sentences",
             "The negative command also changes: لَا تَقُلْ (man), لَا تَقُولِي (woman), لَا تَقُولُوا (group).",
             examples=[
                 ex("كُونِي هُنَاكَ فِي الْخَامِسَة تَمَامًا.", "Be there at exactly five. (to a woman)", "كُونِي"),
                 ex("قُولِي ذَلِكَ لِأَبِيكِ.", "Tell that to your father. (to a woman)", "قُولِي"),
                 ex("بِيعِي السَّيَّارَة الْقَدِيمَة.", "Sell the old car. (to a woman)", "بِيعِي"),
                 ex("سِيرُوا خَلْفِي.", "Walk behind me. (to a group)", "سِيرُوا"),
                 ex("نَامُوا مُبَكِّرِين.", "Go to bed early. (to a group)", "نَامُوا"),
                 ex("لَا تَقُولُوا ذَلِكَ.", "Do not say that. (to a group)", "لَا تَقُولُوا"),
             ]),
    ],
    exercises=[
        M("Which is the command “Tell it!” to a woman?", "قُولِي", ["قُلْ", "قُولُوا", "تَقُولِين"], "ـِي for a woman."),
        M("Which is the command to a group from يَسِير?", "سِيرُوا", ["سِرْ", "سِيرِي", "يَسِيرُون"], "ـُوا for a group."),
        M("Which is the command to a woman from يَنَام?", "نَامِي", ["نَمْ", "نَامُوا", "تَنَامِين"], "ـِي."),
        M("Which means “Sell the car” (to a woman)?", "بِيعِي السَّيَّارَة", ["بِعْ السَّيَّارَة", "بِيعُوا السَّيَّارَة", "تَبِيعِين السَّيَّارَة"], "ـِي."),
        M("Which means “Do not say that” (to a group)?", "لَا تَقُولُوا ذَلِكَ", ["لَا تَقُلْ ذَلِكَ", "لَا تَقُولِي ذَلِكَ", "قُولُوا ذَلِكَ"], "لَا + ـُوا."),
        M("In قُولِي, why does the vowel come back long?", "the ending is a long vowel", ["it is the past", "it is a noun", "the verb is sound"], "Only the one-man form is short."),
        F("___ خَلْفِي. (to a group)", "سِيرُوا", ["سِرْ", "سِيرِي", "يَسِيرُون"], "Group command.", tr="Walk behind me.", lemma="سير:imp:antum"),
        F("___ هُنَاكَ فِي الْخَامِسَة. (to a woman)", "كُونِي", ["كُنْ", "كُونُوا", "تَكُونِين"], "Woman command.", tr="Be there at five.", lemma="كون:imp:anti"),
        F("___ ذَلِكَ لِأَبِيكِ. (to a woman)", "لَا تَقُولِي", ["لَا تَقُلْ", "لَا تَقُولُوا", "قُولِي"], "Negative, feminine.", tr="Do not say that to your father.", lemma="قول:neg:anti"),
    ],
    verify=(vv("قول", "imp", anta="قُلْ", anti="قُولِي", antum="قُولُوا") + vv("سير", "imp", anta="سِرْ", anti="سِيرِي", antum="سِيرُوا")
            + vv("بيع", "imp", anta="بِعْ", anti="بِيعِي", antum="بِيعُوا") + vv("نوم", "imp", anta="نَمْ", anti="نَامِي", antum="نَامُوا")
            + vv("قود", "imp", anta="قُدْ", anti="قُودِي", antum="قُودُوا") + vv("كون", "imp", anta="كُنْ", anti="كُونِي", antum="كُونُوا")
            + vv("عيش", "imp", anta="عِشْ", anti="عِيشِي", antum="عِيشُوا")
            + vv("قول", "neg", anta="لَا تَقُلْ", anti="لَا تَقُولِي", antum="لَا تَقُولُوا")
            + vw("الْخَامِسَة", "تَمَامًا", "لِأَبِيكِ", "خَلْفِي", "هُنَاكَ") + vps("مُبَكِّر", "مُبَكِّرِينَ", "obl")),
)

# ---------------------------------------------------------------------------- 211
L211 = lesson(
    "Giving directions: go straight, turn, continue",
    "سِرْ مُسْتَقِيمًا · دُرْ إِلَى الْيَسَار · اِسْتَمِرّ حَتَّى النِّهَايَة",
    requires=["سار", "دار", "مستقيم", "يمين", "يسار", "نهاية", "طريق", "شارع", "مخرج", "بنزين", "وقف", "محطة"],
    cards=[
        card("Words for finding the way",
             "Directions are made of commands plus a few place words. The command for a man is also used when you speak to one person and do not know whether it is a man or a woman.",
             tables=[table(["English", "Arabic"],
                           [["continue", "اِسْتَمِرّ"], ["go straight", "سِرْ مُسْتَقِيمًا"], ["turn left", "دُرْ إِلَى الْيَسَار"],
                            ["turn right", "دُرْ إِلَى الْيَمِين"], ["follow", "اِتَّبِعْ"], ["stop", "تَوَقَّفْ"], ["stay on the right", "اِبْقَ عَلَى الْيَمِين"]],
                           say=[1], tlit=[1], gloss=False),
                    table(["English", "Arabic"],
                          [["the end of the street", "نِهَايَة الشَّارِع"], ["the junction", "الْمُفْتَرَق"], ["the exit", "الْمَخْرَج"],
                           ["the sign", "اللَّافِتَة"], ["the petrol station", "مَحَطَّة الْبَنْزِين"], ["straight ahead", "مُسْتَقِيمًا"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("A set of directions",
             "To say where something will be, use عَلَى يَمِينِكَ / عَلَى يَسَارِكَ (“on your right / left”), with the ending for “you”. "
             "To say what you will see, use سَتَجِد or سَتَرَى (“you will find”, “you will see”).",
             examples=[
                 ex("اِسْتَمِرّ عَلَى هَذَا الطَّرِيق حَتَّى نِهَايَة الشَّارِع.", "Continue on this road to the end of the street.", "اِسْتَمِرّ"),
                 ex("عِنْدَ الْمُفْتَرَق دُرْ إِلَى الْيَسَار.", "At the junction turn left.", "الْمُفْتَرَق"),
                 ex("سِرْ مُسْتَقِيمًا ثُمَّ دُرْ إِلَى الْيَمِين.", "Go straight and then turn right.", "مُسْتَقِيمًا"),
                 ex("سَتَرَى لَافِتَة كَبِيرَة قَبْلَ الْمَخْرَج.", "You will see a big sign before the exit.", "سَتَرَى"),
                 ex("سَتَجِد مَحَطَّة بَنْزِين عَلَى يَسَارِكَ.", "You will find a petrol station on your left.", "عَلَى يَسَارِكَ"),
                 ex("اِبْقَ عَلَى الْيَمِين وَتَوَقَّفْ عِنْدَ الْإِشَارَة.", "Stay on the right and stop at the light.", "اِبْقَ"),
             ]),
    ],
    exercises=[
        M("Which means “go straight”?", "سِرْ مُسْتَقِيمًا", ["دُرْ إِلَى الْيَمِين", "اِتَّبِعْ", "تَوَقَّفْ"], "مُسْتَقِيم = straight."),
        M("Which means “turn left”?", "دُرْ إِلَى الْيَسَار", ["دُرْ إِلَى الْيَمِين", "سِرْ مُسْتَقِيمًا", "اِبْقَ عَلَى الْيَمِين"], "يَسَار = left."),
        M("Which means “continue”?", "اِسْتَمِرّ", ["تَوَقَّفْ", "غَادِرْ", "اِتَّبِعْ"], "اِسْتَمِرّ = continue."),
        M("What does مَحَطَّة الْبَنْزِين mean?", "the petrol station", ["the bus stop", "the airport", "the exit"], "بَنْزِين = petrol."),
        M("Which means “on your left” (to a man)?", "عَلَى يَسَارِكَ", ["عَلَى يَمِينِكَ", "عَلَى يَسَارِي", "عَلَى يَسَارِكِ"], "ـكَ = you (m.)."),
        M("What does سَتَرَى لَافِتَة mean?", "you will see a sign", ["you saw a sign", "I will see a sign", "he made a sign"], "سَـ + present = will."),
        F("عِنْدَ الْمُفْتَرَق ___ إِلَى الْيَسَار.", "دُرْ", ["دَارَ", "يَدُور", "دُورِي"], "Command to a man.", tr="At the junction turn left. (to a man)", lemma="دور:imp:anta"),
        F("سَتَجِد مَحَطَّة بَنْزِين عَلَى ___.", "يَسَارِكَ", ["يَسَارِي", "يَسَارِهِ", "الْيَسَار"], "Your left (m.).", tr="You will find a petrol station on your left."),
        F("اِسْتَمِرّ حَتَّى ___ الشَّارِع.", "نِهَايَة", ["النِّهَايَة", "نِهَايَةً", "نَهَى"], "An iḍāfa: no ال.", tr="Continue to the end of the street."),
    ],
    verify=(vv("دور", "imp", anta="دُرْ") + vv("سير", "imp", anta="سِرْ")
            + vw("اِسْتَمِرّ", "اِتَّبِعْ", "تَوَقَّفْ", "اِبْقَ", "مُسْتَقِيمًا", "الْمُفْتَرَق", "الْمَخْرَج", "اللَّافِتَة", "لَافِتَة", "الْبَنْزِين", "بَنْزِين", "يَسَارِكَ", "يَمِينِكَ",
                 "سَتَجِد", "سَتَرَى", "النِّهَايَة", "قَبْلَ")),
)


# ---------------------------------------------------------------------------- 212
L212 = lesson(
    "A route, step by step",
    "أَوَّلًا · ثُمَّ · بَعْدَ ذَلِكَ · حَتَّى · مُبَاشَرَةً",
    requires=["أول", "ثم", "بعد", "قبل", "حتى", "عند", "مباشرة", "طريق", "إرشاد", "وصل"],
    cards=[
        card("Linking the steps",
             "A route has an order. These small words put the steps in sequence. After حَتَّى (“until”) the verb is in the present "
             "with the same form you use after أَنْ.",
             tables=[table(["English", "Arabic"],
                           [["first", "أَوَّلًا"], ["then", "ثُمَّ"], ["after that", "بَعْدَ ذَلِكَ"], ["until", "حَتَّى"],
                            ["when, at the time", "عِنْدَمَا"], ["right after", "بَعْدَ … مُبَاشَرَةً"], ["before", "قَبْلَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("At the hotel desk (an invented practice dialogue)",
             "A visitor asks how to reach a fish restaurant. To ask for directions, use كَيْفَ أَصِل إِلَى … (“How do I get to…?”) "
             "or هَلْ يُمْكِنُكَ أَنْ تُعْطِينِي بَعْض الْإِرْشَادَات؟",
             examples=[
                 ex("كَيْفَ أَصِل إِلَى مَطْعَم السَّمَك؟", "How do I get to the fish restaurant?", "كَيْفَ أَصِل"),
                 ex("أَوَّلًا غَادِرِ الْفُنْدُق وَسِرْ إِلَى الْيَمِين.", "First leave the hotel and go to the right.", "أَوَّلًا"),
                 ex("ثُمَّ اِسْتَمِرّ حَتَّى تَصِل إِلَى الْإِشَارَة.", "Then continue until you reach the traffic light.", "حَتَّى تَصِل"),
                 ex("بَعْدَ ذَلِكَ دُرْ إِلَى الْيَسَار.", "After that turn left.", "بَعْدَ ذَلِكَ"),
                 ex("الْمَطْعَم عَلَى يَمِينِكَ بَعْدَ مَحَطَّة الْبَنْزِين مُبَاشَرَةً.", "The restaurant is on your right, right after the petrol station.", "مُبَاشَرَةً"),
                 ex("شُكْرًا جَزِيلًا.", "Thank you very much.", "شُكْرًا"),
             ]),
    ],
    exercises=[
        M("Which word means “first”?", "أَوَّلًا", ["ثُمَّ", "حَتَّى", "قَبْلَ"], "أَوَّلًا = firstly."),
        M("Which word means “until”?", "حَتَّى", ["ثُمَّ", "عِنْدَمَا", "بَعْدَ"], "حَتَّى + present = until."),
        M("Which means “How do I get to the restaurant?”", "كَيْفَ أَصِل إِلَى الْمَطْعَم؟", ["أَيْنَ أَصِل إِلَى الْمَطْعَم؟", "كَيْفَ تَصِل الْمَطْعَم؟", "مَتَى يَصِل الْمَطْعَم؟"], "أَصِل = I arrive."),
        M("Which means “After that turn left”?", "بَعْدَ ذَلِكَ دُرْ إِلَى الْيَسَار", ["قَبْلَ ذَلِكَ دُرْ إِلَى الْيَمِين", "ثُمَّ سِرْ مُسْتَقِيمًا", "أَوَّلًا قِفْ"], "بَعْدَ ذَلِكَ = after that."),
        M("What does مُبَاشَرَةً add in بَعْدَ مَحَطَّة الْبَنْزِين مُبَاشَرَةً?", "right after", ["far from", "instead of", "before"], "مُبَاشَرَةً = directly."),
        M("Which is the command to a man, “leave the hotel”?", "غَادِرِ الْفُنْدُق", ["غَادَرَ الْفُنْدُق", "يُغَادِر الْفُنْدُق", "غَادِرِي الْفُنْدُق"], "Command; kasra before ال."),
        F("أَوَّلًا ___ الْفُنْدُق وَسِرْ إِلَى الْيَمِين.", "غَادِرِ", ["غَادَرَ", "يُغَادِر", "غَادِرِي"], "A command to a man.", tr="First leave the hotel and go right."),
        F("اِسْتَمِرّ ___ تَصِل إِلَى الْإِشَارَة.", "حَتَّى", ["ثُمَّ", "قَبْلَ", "عِنْدَ"], "Until.", tr="Continue until you reach the traffic light."),
        F("الْمَطْعَم عَلَى ___ بَعْدَ مَحَطَّة الْبَنْزِين.", "يَمِينِكَ", ["يَمِينِي", "يَمِينِهِ", "الْيَسَار"], "Your right.", tr="The restaurant is on your right after the petrol station."),
    ],
    verify=(vv("غدر#3", "imp", anta="غَادِرْ")
            + vw("أَوَّلًا", "ثُمَّ", "حَتَّى", "عِنْدَمَا", "مُبَاشَرَةً", "تُعْطِينِي", "الْإِرْشَادَات", "غَادِرِ", "الْفُنْدُق", "يَمِينِكَ", "جَزِيلًا", "أَصِل")),
)

# ---------------------------------------------------------------------------- 213
L213 = lesson(
    "Review: hollow verbs and commands",
    "يَا بُنَيَّ، قُدِ السَّيَّارَة بِحَذَر",
    requires=["قاد", "قال", "زار", "نام", "سار", "كان", "باع", "عاش"],
    cards=[
        card("What to remember",
             "Hollow verbs keep a long vowel in the present (يَقُول, يَبِيع, يَنَام) and drop it in short forms (قُلْتُ, يَقُلْنَ, قُلْ). "
             "A command to one man is short (قُلْ, سِرْ, نَمْ). To a woman it ends in ـِي (قُولِي) and to a group in ـُوا (قُولُوا).",
             tables=[table(["English", "To a man", "To a woman", "To a group"],
                           [["be", "كُنْ", "كُونِي", "كُونُوا"], ["go, walk", "سِرْ", "سِيرِي", "سِيرُوا"],
                            ["say", "قُلْ", "قُولِي", "قُولُوا"], ["do not sleep", "لَا تَنَمْ", "لَا تَنَامِي", "لَا تَنَامُوا"]],
                           say=[1, 2, 3], tlit=[1], gloss=False)]),
        card("A father’s advice (an invented practice text)",
             "A father speaks to his son and daughter before a trip. Read the commands and notice who each one is for.",
             examples=[
                 ex("يَا بُنَيَّ، قُدِ السَّيَّارَة بِحَذَر وَكُنْ مُنْتَبِهًا دَائِمًا.", "My son, drive the car carefully and always be alert.", "قُدِ"),
                 ex("عِنْدَمَا تَصِل إِلَى الْمَدِينَة زُرْ عَمَّكَ.", "When you reach the city, visit your uncle.", "زُرْ"),
                 ex("وَأَنْتِ يَا بِنْتِي، كُونِي بِجَانِبِهِ وَقُولِي لَهُ لَا تُسْرِعْ.", "And you, my daughter, be beside him and tell him not to hurry.", "كُونِي"),
                 ex("سِيرُوا فِي النَّهَار فَهَذَا أَفْضَل.", "Travel in the daytime, that is better. (to both)", "سِيرُوا"),
                 ex("لَا تَنَامُوا فِي السَّيَّارَة.", "Do not sleep in the car. (to both)", "لَا تَنَامُوا"),
                 ex("وَأَنَا أَنَام مُرْتَاحًا إِذَا وَصَلْتُمْ.", "And I will sleep easy if you arrive.", "أَنَام"),
             ]),
    ],
    exercises=[
        M("Which is a command to a woman?", "كُونِي", ["كُنْ", "كُونُوا", "تَكُونِين"], "ـِي."),
        M("Which is a command to a group?", "سِيرُوا", ["سِرْ", "سِيرِي", "يَسِير"], "ـُوا."),
        M("Which means “Do not sleep in the car” (to a group)?", "لَا تَنَامُوا فِي السَّيَّارَة", ["لَا تَنَمْ فِي السَّيَّارَة", "نَامُوا فِي السَّيَّارَة", "لَا تَنَامِي فِي السَّيَّارَة"], "لَا تَنَامُوا."),
        M("Which means “I sleep”?", "أَنَام", ["أَقُول", "أَبِيع", "أَزُور"], "نَامَ → أَنَام."),
        M("Which means “I said”?", "قُلْتُ", ["قَالَ", "أَقُول", "قُلْ"], "Past, I: قُلْتُ."),
        M("What does يَا بُنَيَّ mean?", "my son", ["my brother", "my friend", "my uncle"], "A form of address to a boy."),
        F("يَا بُنَيَّ، ___ السَّيَّارَة بِحَذَر.", "قُدِ", ["قَادَ", "يَقُود", "قُودِي"], "Command to a son.", tr="My son, drive the car carefully."),
        F("وَأَنْتِ يَا بِنْتِي، ___ بِجَانِبِهِ.", "كُونِي", ["كُنْ", "كُونُوا", "تَكُونُ"], "Command to a daughter.", tr="And you, my daughter, be beside him."),
        F("___ فِي النَّهَار فَهَذَا أَفْضَل. (to both)", "سِيرُوا", ["سِرْ", "سِيرِي", "سَارَ"], "Command to a group.", tr="Travel in the daytime, that is better."),
    ],
    verify=(vv("قود", "imp", anta="قُدْ") + vv("كون", "imp", anta="كُنْ", anti="كُونِي", antum="كُونُوا") + vv("سير", "imp", anta="سِرْ", anti="سِيرِي", antum="سِيرُوا")
            + vv("قول", "imp", anta="قُلْ", anti="قُولِي", antum="قُولُوا") + vv("نوم", "neg", anta="لَا تَنَمْ", anti="لَا تَنَامِي", antum="لَا تَنَامُوا")
            + vv("زور", "imp", anta="زُرْ") + vv("نوم", "pres", ana="أَنَام") + vv("قول", "past", ana="قُلْتُ")
            + vw("بُنَيَّ", "مُنْتَبِهًا", "دَائِمًا", "عَمَّكَ", "بِنْتِي", "بِجَانِبِهِ", "تُسْرِعْ", "النَّهَار", "مُرْتَاحًا", "وَصَلْتُمْ")),
)

# ---------------------------------------------------------------------------- 214
L214 = lesson(
    "Review: a day out in a seaside city",
    "الْإِسْكَنْدَرِيَّة مَدِينَة عَلَى الْبَحْر",
    requires=["مدينة", "بحر", "قطار", "سريع", "أبيض", "فندق", "مطعم", "ساعة", "طريق", "وصل"],
    cards=[
        card("What to remember",
             "This lesson brings together places and sights, transport, journey times and directions. Remember: أَفْعَل + مِنْ to compare, "
             "تَسْتَغْرِق + a time for how long, a command for directions, and حَتَّى + a present verb.",
             tables=[table(["English", "Arabic"],
                           [["The train is faster than the bus.", "الْقِطَار أَسْرَع مِنَ الْحَافِلَة"], ["The trip takes two hours.", "تَسْتَغْرِق الرِّحْلَة سَاعَتَيْن"],
                            ["Go straight, then turn right.", "سِرْ مُسْتَقِيمًا ثُمَّ دُرْ إِلَى الْيَمِين"], ["Trucks may not pass.", "مَمْنُوع مُرُور الشَّاحِنَات"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A day in Alexandria (an invented practice text)",
             "Alexandria (الْإِسْكَنْدَرِيَّة) is a large port city in Egypt on the Mediterranean Sea. The story below is invented for practice.",
             examples=[
                 ex("الْإِسْكَنْدَرِيَّة مَدِينَة كَبِيرَة عَلَى الْبَحْر الْأَبْيَض الْمُتَوَسِّط فِي مِصْر.", "Alexandria is a large city on the Mediterranean Sea in Egypt.", "الْإِسْكَنْدَرِيَّة"),
                 ex("تَسْتَغْرِق الرِّحْلَة بِالْقِطَار مِنَ الْقَاهِرَة نَحْوَ ثَلَاث سَاعَات.", "The trip by train from Cairo takes about three hours.", "نَحْوَ ثَلَاث سَاعَات"),
                 ex("وَصَلْنَا إِلَى الْمَحَطَّة وَأَخَذْنَا سَيَّارَة أُجْرَة إِلَى الْفُنْدُق.", "We arrived at the station and took a taxi to the hotel.", "وَصَلْنَا"),
                 ex("قَالَ لَنَا مُوَظَّف الِاسْتِقْبَال سِيرُوا إِلَى نِهَايَة الشَّارِع ثُمَّ دُورُوا إِلَى الْيَمِين.", "The receptionist told us, “Walk to the end of the street, then turn right.”", "سِيرُوا"),
                 ex("رَأَيْنَا لَافِتَة كَبِيرَة قَبْلَ الْمَطْعَم.", "We saw a big sign before the restaurant.", "لَافِتَة"),
                 ex("كُنَّا جَائِعِين فَأَكَلْنَا السَّمَك الطَّازَج.", "We were hungry, so we ate fresh fish.", "جَائِعِين"),
             ]),
    ],
    exercises=[
        M("Where is Alexandria, according to the text?", "on the Mediterranean Sea in Egypt", ["in the desert of Sudan", "on the Red Sea in Jordan", "in the mountains of Lebanon"], "عَلَى الْبَحْر الْأَبْيَض الْمُتَوَسِّط."),
        M("Which means “The trip takes about three hours”?", "تَسْتَغْرِق الرِّحْلَة نَحْوَ ثَلَاث سَاعَات", ["تَسْتَغْرِق الرِّحْلَة نَحْوَ ثَلَاثَة سَاعَات", "الرِّحْلَة أَسْرَع مِنْ ثَلَاث سَاعَات", "تَصِل الرِّحْلَة ثَلَاث سَاعَات"], "Feminine noun: ثَلَاث."),
        M("Which means “We arrived at the station”?", "وَصَلْنَا إِلَى الْمَحَطَّة", ["وَصَلْتُ إِلَى الْمَحَطَّة", "يَصِلُون إِلَى الْمَحَطَّة", "غَادَرْنَا الْمَحَطَّة"], "We = ـنَا."),
        M("What did the receptionist say?", "Walk to the end of the street", ["Take the train", "Stop at the hotel", "Sell the car"], "سِيرُوا إِلَى نِهَايَة الشَّارِع."),
        M("Which means “We were hungry”?", "كُنَّا جَائِعِين", ["كُنْتُ جَائِعًا", "كَانُوا جَائِعِين", "نَكُون جَائِعِين"], "كَانَ → كُنَّا."),
        M("Which means “We saw a big sign”?", "رَأَيْنَا لَافِتَة كَبِيرَة", ["رَأَيْتُ لَافِتَة كَبِيرَة", "سَتَرَى لَافِتَة كَبِيرَة", "رَأَوْا لَافِتَة كَبِيرَة"], "We = ـنَا."),
        F("قَالَ لَنَا الْمُوَظَّف ___ إِلَى نِهَايَة الشَّارِع.", "سِيرُوا", ["سِرْ", "سِيرِي", "سَارُوا"], "Command to a group.", tr="The employee told us, “Walk to the end of the street.”"),
        F("تَسْتَغْرِق الرِّحْلَة بِالْقِطَار نَحْوَ ___ سَاعَات.", "ثَلَاث", ["ثَلَاثَة", "ثَالِث", "سَاعَتَيْن"], "Opposite gender.", tr="The trip by train takes about three hours."),
        F("الْقِطَار ___ مِنَ الْحَافِلَة.", "أَسْرَع", ["سَرِيع", "أَبْطَأ", "سَرِيعَة"], "Faster than.", tr="The train is faster than the bus."),
    ],
    verify=(vv("سير", "imp", antum="سِيرُوا") + vv("كون", "past", nahnu="كُنَّا") + vn(3, "f", "ثَلَاث")
            + vw("الْإِسْكَنْدَرِيَّة", "الْمُتَوَسِّط", "الْأَبْيَض", "الْقَاهِرَة", "نَحْوَ", "وَصَلْنَا", "أَخَذْنَا", "الِاسْتِقْبَال", "رَأَيْنَا", "جَائِعِين", "فَأَكَلْنَا", "دُورُوا", "مُوَظَّف", "الْمُوَظَّف")),
)


UNIT = unit("الْمَدِينَة وَالطُّرُق: sights, transport, directions and hollow verbs", [L199, L200, L201, L202, L203, L204, L205, L206, L207, L208, L209, L210, L211, L212, L213, L214])
