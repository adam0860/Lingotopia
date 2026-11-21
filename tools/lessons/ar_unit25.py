"""Unit 25 (chapter 23): Egypt, buildings, the subjunctive, train tickets, the Nile, temples and the post office."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 395
L395 = lesson(
    "The pyramids of Giza",
    "الْهَرَم الْأَكْبَر · أَقْدَم عَجِيبَة",
    requires=["هرم", "ضخم", "حجر", "بنى", "عامل", "سائح", "قديم", "عجيبة", "كبير"],
    cards=[
        card("A huge, ancient tomb",
             "A pyramid is a هَرَم, and the plural is أَهْرَام. The most famous pyramids stand at Giza (الْجِيزَة), near Cairo. "
             "The biggest one is called الْهَرَم الْأَكْبَر, “the Great Pyramid”. It is often described as the oldest of the Seven Wonders of the Ancient World. "
             "The sentences below are simple invented descriptions.",
             tables=[table(["English", "Arabic"],
                           [["pyramid", "هَرَم"], ["pyramids", "أَهْرَام"], ["huge", "ضَخْم"], ["stone", "حَجَر"], ["worker", "عَامِل"], ["wonder", "عَجِيبَة"], ["the Great Pyramid", "الْهَرَم الْأَكْبَر"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("الْهَرَم الْأَكْبَر فِي الْجِيزَة.", "The Great Pyramid is in Giza.", "الْهَرَم الْأَكْبَر"),
                 ex("هُوَ مِنْ أَقْدَم عَجَائِب الْعَالَم.", "It is one of the oldest wonders of the world.", "أَقْدَم"),
                 ex("بَنَى الْعُمَّال الْهَرَم بِالْحِجَارَة.", "Workers built the pyramid with stones.", "بَنَى"),
                 ex("بُنِيَ الْهَرَم مُنْذُ آلَاف السِّنِين.", "The pyramid was built thousands of years ago.", "بُنِيَ"),
                 ex("الْهَرَم ضَخْم وَقَدِيم جِدًّا.", "The pyramid is huge and very old.", "ضَخْم"),
                 ex("يَزُور السُّيَّاح الْأَهْرَام كُلَّ يَوْم.", "Tourists visit the pyramids every day.", "الْأَهْرَام"),
             ]),
    ],
    exercises=[
        M("What is a هَرَم?", "a pyramid", ["a temple", "a bridge", "a tower"], "هَرَم = pyramid."),
        M("What is the plural of هَرَم?", "أَهْرَام", ["هَرَمَات", "هَرَمُون", "هُرُوم"], "A broken plural."),
        M("What does الْهَرَم الْأَكْبَر mean?", "the Great Pyramid", ["the small pyramid", "the new pyramid", "the Nile"], "أَكْبَر = bigger, biggest."),
        M("What does بَنَى الْعُمَّال الْهَرَم mean?", "Workers built the pyramid", ["Workers visited the pyramid", "The pyramid was sold", "Tourists left the pyramid"], "بَنَى = he built."),
        M("What does بُنِيَ mean?", "was built", ["built", "is building", "will build"], "The passive of بَنَى."),
        M("What does ضَخْم mean?", "huge", ["tiny", "cheap", "quiet"], "ضَخْم = huge."),
        F("الْهَرَم الْأَكْبَر فِي ___.", "الْجِيزَة", ["الْمَتْحَف", "الْفُنْدُق"], "The great pyramids are at Giza.", tr="The Great Pyramid is in Giza."),
        F("___ الْعُمَّال الْهَرَم بِالْحِجَارَة.", "بَنَى", ["بُنِيَ", "يَبْنِي"], "The workers are the doers: an active verb.", tr="Workers built the pyramid with stones.", lemma="بني:past:huwa"),
        F("___ الْهَرَم مُنْذُ آلَاف السِّنِين.", "بُنِيَ", ["بَنَى", "يُبْنَى"], "No doer is named: the passive.", tr="The pyramid was built thousands of years ago."),
        F("الْهَرَم ضَخْم وَ___ جِدًّا.", "قَدِيم", ["قَدِيمَة", "قَدِيمُون"], "الْهَرَم is masculine.", tr="The pyramid is huge and very old."),
    ],
    verify=vv("بني", "past", huwa="بَنَى"),
)

# ---------------------------------------------------------------------------- 396
L396 = lesson(
    "The Sphinx and the Hanging Church",
    "رَأْس إِنْسَان وَجِسْم أَسَد · فَوْقَ بُرْجَيْن",
    requires=["تمثال", "رأس", "جسم", "إنسان", "برج", "كنيسة", "معلق", "قرب", "فوق"],
    cards=[
        card("Two famous places in and near Cairo",
             "The Sphinx, أَبُو الْهَوْل in Arabic, is a huge statue near the pyramids at Giza. It has the head of a human and the body of a lion (أَسَد). "
             "The Hanging Church, الْكَنِيسَة الْمُعَلَّقَة, stands in Old Cairo. It is called ‘hanging’ because it was built on top of two old towers. The sentences are invented and simple.",
             examples=[
                 ex("أَبُو الْهَوْل تِمْثَال ضَخْم قَرِيب مِنَ الْأَهْرَام.", "The Sphinx is a huge statue near the pyramids.", "تِمْثَال"),
                 ex("رَأْسُهُ رَأْس إِنْسَان وَجِسْمُهُ جِسْم أَسَد.", "Its head is a human head and its body is a lion’s body.", "رَأْسُهُ"),
                 ex("الْكَنِيسَة الْمُعَلَّقَة فِي الْقَاهِرَة الْقَدِيمَة.", "The Hanging Church is in Old Cairo.", "الْمُعَلَّقَة"),
                 ex("بُنِيَتْ فَوْقَ بُرْجَيْن قَدِيمَيْن.", "It was built above two old towers.", "بُرْجَيْن"),
                 ex("يَدْخُل الزَّائِرُون مِنْ بَاب صَغِير.", "The visitors enter by a small door.", "الزَّائِرُون"),
                 ex("أَحَبَّ السُّيَّاح الْكَنِيسَة.", "The tourists liked the church.", "أَحَبَّ"),
             ]),
    ],
    exercises=[
        M("What is أَبُو الْهَوْل?", "the Sphinx", ["a pyramid", "a church", "a river"], "The Arabic name of the Sphinx."),
        M("What has the head of a human?", "the Sphinx", ["the Nile", "the Hanging Church", "a pyramid"], "رَأْس إِنْسَان."),
        M("What is an أَسَد?", "a lion", ["a bird", "a camel", "a fish"], "أَسَد = lion."),
        M("What does فَوْقَ بُرْجَيْن mean?", "above two towers", ["below two towers", "near two doors", "inside two rooms"], "بُرْجَيْن = two towers (dual, oblique)."),
        M("What does بُنِيَتْ mean?", "was built (f.)", ["was built (m.)", "she builds", "they built"], "The passive past with a feminine subject."),
        M("What does الْكَنِيسَة الْمُعَلَّقَة mean?", "the Hanging Church", ["the Great Church", "the new church", "the red church"], "مُعَلَّقَة = hung, suspended."),
        F("رَأْسُهُ رَأْس ___.", "إِنْسَان", ["أَسَد", "جِسْر"], "The Sphinx has a human head.", tr="Its head is a human head."),
        F("وَجِسْمُهُ جِسْم ___.", "أَسَد", ["إِنْسَان", "هَرَم"], "…and a lion’s body.", tr="and its body is a lion’s body."),
        F("بُنِيَتْ فَوْقَ ___ قَدِيمَيْن.", "بُرْجَيْن", ["بُرْج", "بُرُوج"], "“two towers” needs the dual.", tr="It was built above two old towers."),
        F("الْكَنِيسَة ___ فِي الْقَاهِرَة الْقَدِيمَة.", "الْمُعَلَّقَة", ["الْمُعَلَّق", "الْمُعَلَّقُون"], "The adjective agrees with a feminine definite noun.", tr="The Hanging Church is in Old Cairo."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 397
L397 = lesson(
    "Describing a building",
    "قُبَّة · بُرْج · عَمُود · جِدَار · سَقْف",
    requires=["قبة", "برج", "عمود", "جدار", "سقف", "نافذة", "باب", "طابق", "حجر", "مسجد"],
    cards=[
        card("Parts of a building",
             "To describe a building, name its parts. A mosque may have a dome (قُبَّة) and a tower; an old temple may have columns (أَعْمِدَة) and thick walls (جُدْرَان). "
             "The plural of a thing takes a feminine singular adjective: جُدْرَان طَوِيلَة, “tall walls”. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["dome", "قُبَّة"], ["tower", "بُرْج"], ["column", "عَمُود"], ["columns", "أَعْمِدَة"], ["wall", "جِدَار"], ["walls", "جُدْرَان"], ["ceiling, roof", "سَقْف"], ["floor, storey", "طَابِق"], ["window", "نَافِذَة"], ["door", "بَاب"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("لِلْمَسْجِد قُبَّة كَبِيرَة وَبُرْج عَالٍ.", "The mosque has a big dome and a tall tower.", "قُبَّة كَبِيرَة"),
                 ex("فِي الْمَعْبَد أَعْمِدَة كَثِيرَة.", "In the temple there are many columns.", "أَعْمِدَة كَثِيرَة"),
                 ex("جُدْرَانُهُ طَوِيلَة وَسَقْفُهُ قَدِيم.", "Its walls are tall and its ceiling is old.", "جُدْرَانُهُ طَوِيلَة"),
                 ex("الْمَبْنَى مَصْنُوع مِنَ الْحَجَر.", "The building is made of stone.", "مَصْنُوع"),
                 ex("لَهُ ثَلَاثَة طَوَابِق وَنَوَافِذ صَغِيرَة.", "It has three floors and small windows.", "نَوَافِذ صَغِيرَة"),
             ]),
    ],
    exercises=[
        M("What is a قُبَّة?", "a dome", ["a door", "a floor", "a stone"], "قُبَّة = dome."),
        M("What is a سَقْف?", "a ceiling, a roof", ["a wall", "a window", "a column"], "سَقْف = roof, ceiling."),
        M("What are أَعْمِدَة?", "columns", ["towers", "walls", "doors"], "The plural of عَمُود."),
        M("What does مَصْنُوع مِنَ الْحَجَر mean?", "made of stone", ["made of gold", "made of wood", "made in Egypt"], "حَجَر = stone."),
        M("Why is it جُدْرَان طَوِيلَة?", "the plural of a thing takes a feminine singular adjective", ["جُدْرَان is a person", "the adjective is a dual", "the adjective is a verb"], "Plural things behave as feminine singular."),
        M("What does ثَلَاثَة طَوَابِق mean?", "three floors", ["three doors", "three towers", "three walls"], "طَابِق = floor, storey."),
        F("لِلْمَسْجِد ___ كَبِيرَة.", "قُبَّة", ["جِدَار", "عَمُود"], "A dome is feminine, like كَبِيرَة.", tr="The mosque has a big dome."),
        F("فِي الْمَعْبَد أَعْمِدَة ___.", "كَثِيرَة", ["كَثِيرُون", "كَثِير"], "The plural of a thing: feminine singular.", tr="In the temple there are many columns."),
        F("جُدْرَانُهُ ___ وَسَقْفُهُ قَدِيم.", "طَوِيلَة", ["طَوِيل", "طَوِيلُون"], "The plural of a thing: feminine singular.", tr="Its walls are tall and its ceiling is old."),
        F("الْمَبْنَى مَصْنُوع مِنَ ___.", "الْحَجَر", ["النَّافِذَة", "السَّقْف"], "Made of stone.", tr="The building is made of stone."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 398
L398 = lesson(
    "The Nile and the four directions",
    "شَمَال · جَنُوب · شَرْق · غَرْب",
    requires=["نيل", "شمال", "جنوب", "غرب", "عالم", "مدينة", "قرب", "بعيد"],
    cards=[
        card("Directions on the map",
             "The four directions are شَمَال, جَنُوب, شَرْق and غَرْب. Add ـِيّ for the adjective: شَمَالِيّ, “northern”, غَرْبِيّ, “western”. "
             "The Nile (النِّيل) flows from the south to the north, so Aswan lies in the south of Egypt and Cairo lies in the north. Cities on the river have two banks: الضِّفَّة الْغَرْبِيَّة and الضِّفَّة الشَّرْقِيَّة. The sentences are simple and invented.",
             tables=[table(["English", "Arabic"],
                           [["north", "شَمَال"], ["south", "جَنُوب"], ["east", "شَرْق"], ["west", "غَرْب"], ["the Nile", "النِّيل"], ["bank", "ضِفَّة"], ["western", "غَرْبِيّ"], ["eastern", "شَرْقِيّ"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("يَجْرِي النِّيل مِنَ الْجَنُوب إِلَى الشَّمَال.", "The Nile flows from the south to the north.", "يَجْرِي"),
                 ex("تَقَع الْقَاهِرَة فِي الشَّمَال وَأَسْوَان فِي الْجَنُوب.", "Cairo is in the north and Aswan is in the south.", "فِي الشَّمَال"),
                 ex("فُنْدُقُنَا عَلَى الضِّفَّة الشَّرْقِيَّة.", "Our hotel is on the eastern bank.", "الشَّرْقِيَّة"),
                 ex("الْمَعْبَد عَلَى الضِّفَّة الْغَرْبِيَّة.", "The temple is on the western bank.", "الْغَرْبِيَّة"),
                 ex("الْمَتْحَف إِلَى الشَّمَال مِنَ الْفُنْدُق.", "The museum is to the north of the hotel.", "إِلَى الشَّمَال"),
             ]),
    ],
    exercises=[
        M("What does جَنُوب mean?", "south", ["north", "east", "west"], "جَنُوب = south."),
        M("What does شَرْق mean?", "east", ["west", "north", "south"], "شَرْق = east."),
        M("What does غَرْبِيّ mean?", "western", ["eastern", "northern", "southern"], "ـِيّ makes the adjective."),
        M("Which way does the Nile flow?", "from south to north", ["from north to south", "from east to west", "round the city"], "يَجْرِي مِنَ الْجَنُوب إِلَى الشَّمَال."),
        M("Where is Aswan?", "in the south", ["in the north", "in the west", "in the sea"], "تَقَع أَسْوَان فِي الْجَنُوب."),
        M("Why الشَّرْقِيَّة in الضِّفَّة الشَّرْقِيَّة?", "ضِفَّة is feminine", ["it is a plural", "it is a verb", "it is a dual"], "A feminine noun takes a feminine adjective."),
        F("يَجْرِي النِّيل مِنَ ___ إِلَى الشَّمَال.", "الْجَنُوب", ["الشَّرْق", "الْمَتْحَف"], "It flows north from the south.", tr="The Nile flows from the south to the north."),
        F("الْمَعْبَد عَلَى الضِّفَّة ___.", "الْغَرْبِيَّة", ["الْغَرْبِيّ", "غَرْبِيَّة"], "The bank is feminine and definite.", tr="The temple is on the western bank."),
        F("تَقَع الْقَاهِرَة فِي ___.", "الشَّمَال", ["الْجَنُوب", "الْجِسْر"], "Cairo is in the north.", tr="Cairo is in the north."),
        F("الْمَتْحَف إِلَى ___ مِنَ الْفُنْدُق.", "الشَّمَال", ["الشَّمَالِيّ", "شَمَال"], "“to the north of”.", tr="The museum is to the north of the hotel."),
    ],
    verify=vv("جري", "pres", huwa="يَجْرِي"),
)


# ---------------------------------------------------------------------------- 399
L399 = lesson(
    "After the particles: the ending ـَ",
    "أَنْ أَكْتُبَ · لَنْ يَصِلَ · حَتَّى يَصِلَ",
    requires=["كتب", "وصل", "زار", "جلس", "أراد", "قطار", "مدير"],
    cards=[
        card("The accusative present",
             "A present verb is normally followed by ـُ in careful speech: أَكْتُبُ. After certain particles it changes to ـَ: أَنْ أَكْتُبَ. This is the accusative (also called the subjunctive) of the present tense. "
             "You already know the particles أَنْ, لَنْ, كَيْ and لِـ. A new one is حَتَّى, “until”. The particles do not change the order of the sentence. In this lesson the endings are written in full.",
             tables=[table(["Particle", "Meaning"],
                           [["أَنْ", "that, to"], ["لَنْ", "will not"], ["كَيْ", "so that"], ["لِ", "in order to"], ["حَتَّى", "until"]],
                           say=[0], tlit=[0], gloss=False),
                     table(["Person", "Present", "After أَنْ"],
                           [["I", "أَكْتُبُ", "أَنْ أَكْتُبَ"], ["you (m.)", "تَكْتُبُ", "أَنْ تَكْتُبَ"], ["he", "يَكْتُبُ", "أَنْ يَكْتُبَ"], ["she", "تَكْتُبُ", "أَنْ تَكْتُبَ"], ["we", "نَكْتُبُ", "أَنْ نَكْتُبَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences (invented)",
             "Plans for a trip.",
             examples=[
                 ex("أُرِيد أَنْ أَكْتُبَ بِطَاقَة.", "I want to write a card.", "أَنْ أَكْتُبَ"),
                 ex("لَنْ يَصِلَ الْقِطَار مُبَكِّرًا.", "The train will not arrive early.", "لَنْ يَصِلَ"),
                 ex("جِئْتُ لِأَزُورَ الْأَهْرَام.", "I came to visit the pyramids.", "لِأَزُورَ"),
                 ex("سَافَرْنَا كَيْ نَزُورَ الْمَعَابِد.", "We travelled in order to visit the temples.", "كَيْ نَزُورَ"),
                 ex("سَأَنْتَظِر حَتَّى يَصِلَ الْمُدِير.", "I will wait until the manager arrives.", "حَتَّى يَصِلَ"),
                 ex("أَيْنَ تُرِيد أَنْ تَجْلِسَ؟", "Where do you want to sit?", "أَنْ تَجْلِسَ"),
             ]),
    ],
    exercises=[
        M("Which ending follows أَنْ?", "ـَ (fatḥa)", ["ـُ (ḍamma)", "ـِ (kasra)", "ـْ (sukūn)"], "After a particle the verb is accusative: ـَ."),
        M("What does حَتَّى mean in سَأَنْتَظِر حَتَّى يَصِلَ الْمُدِير?", "until", ["because", "although", "if"], "حَتَّى = until."),
        M("What does لَنْ يَصِلَ mean?", "will not arrive", ["did not arrive", "does not arrive", "has arrived"], "لَنْ = will not."),
        M("What does لِأَزُورَ mean?", "in order to visit", ["I visited", "he visits", "do not visit"], "لِـ + accusative = purpose."),
        M("Which particle means ‘so that’?", "كَيْ", ["لَنْ", "حَتَّى", "هَلْ"], "كَيْ = so that."),
        F("أُرِيد أَنْ ___ بِطَاقَة.", "أَكْتُبَ", ["أَكْتُبُ", "كَتَبْتُ"], "After أَنْ: ـَ.", tr="I want to write a card."),
        F("لَنْ ___ الْقِطَار مُبَكِّرًا.", "يَصِلَ", ["يَصِلُ", "وَصَلَ"], "After لَنْ: ـَ.", tr="The train will not arrive early."),
        F("سَأَنْتَظِر ___ يَصِلَ الْمُدِير.", "حَتَّى", ["لَنْ", "هَلْ"], "“until”.", tr="I will wait until the manager arrives."),
        F("جِئْتُ لِ___ الْأَهْرَام.", "أَزُورَ", ["أَزُورُ", "زُرْتُ"], "After لِـ: ـَ.", tr="I came to visit the pyramids."),
        F("أَيْنَ تُرِيد أَنْ ___؟", "تَجْلِسَ", ["تَجْلِسُ", "جَلَسْتَ"], "After أَنْ: ـَ.", tr="Where do you want to sit?"),
    ],
    verify=(vv("كتب", "sub", ana="أَكْتُبَ", anta="تَكْتُبَ", huwa="يَكْتُبَ") + vv("زور", "sub", ana="أَزُورَ", nahnu="نَزُورَ") + vv("وصل", "sub", huwa="يَصِلَ") + vv("جلس", "sub", anta="تَجْلِسَ")),
)

# ---------------------------------------------------------------------------- 400
L400 = lesson(
    "Pairs, women and groups: the ن falls away",
    "أَنْ يَكْتُبُوا · أَنْ تَكْتُبِي · أَنْ يَكْتُبَا",
    requires=["كتب", "ذهب", "جلس", "دخل", "خرج", "أراد", "طالب", "ضيف"],
    cards=[
        card("Loss of the final ن",
             "Some present forms end in ن: ـُونَ (they), ـِينَ (you, f.), ـَانِ (the pair). After a particle this ن is dropped: يَكْتُبُونَ → أَنْ يَكْتُبُوا. "
             "After the group ending ـُوا a silent alif is written. The women’s plural ـْنَ is the exception: it keeps its ن and does not change.",
             tables=[table(["Who", "Present", "After أَنْ"],
                           [["they (m.)", "يَكْتُبُون", "أَنْ يَكْتُبُوا"], ["you (f.)", "تَكْتُبِين", "أَنْ تَكْتُبِي"], ["you two", "تَكْتُبَان", "أَنْ تَكْتُبَا"], ["they two (m.)", "يَكْتُبَان", "أَنْ يَكْتُبَا"], ["they (f.)", "يَكْتُبْنَ", "أَنْ يَكْتُبْنَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences (invented)",
             "At the hotel entrance.",
             examples=[
                 ex("يُرِيد الضُّيُوف أَنْ يَدْخُلُوا الْآن.", "The guests want to enter now.", "أَنْ يَدْخُلُوا"),
                 ex("أُرِيد أَنْ تَجْلِسِي هُنَا يَا سَلْمَى.", "I want you to sit here, Salma.", "أَنْ تَجْلِسِي"),
                 ex("لَنْ يَذْهَبَا إِلَى الْمَتْحَف.", "The two of them will not go to the museum.", "لَنْ يَذْهَبَا"),
                 ex("الْبَنَات يُرِدْنَ أَنْ يَخْرُجْنَ.", "The girls want to go out.", "أَنْ يَخْرُجْنَ"),
                 ex("لَنْ تَكْتُبُوا الرِّسَالَة الْيَوْم.", "You (pl.) will not write the letter today.", "لَنْ تَكْتُبُوا"),
                 ex("جَاءَ الطُّلَّاب لِيَكْتُبُوا الدَّرْس.", "The students came to write the lesson.", "لِيَكْتُبُوا"),
             ]),
    ],
    exercises=[
        M("What happens to the ن of يَكْتُبُونَ after أَنْ?", "it falls away", ["it stays", "it doubles", "it becomes ت"], "The ن of the group ending is dropped."),
        M("Which ending needs a silent alif?", "ـُوا", ["ـِي", "ـَا", "ـْنَ"], "A written alif follows a group و in a verb."),
        M("Which form keeps its ن after أَنْ?", "يَكْتُبْنَ", ["يَكْتُبُونَ", "تَكْتُبِينَ", "يَكْتُبَانِ"], "The women’s plural is the exception."),
        M("What does لَنْ يَذْهَبَا mean?", "the two will not go", ["the two went", "they will go", "he will not go"], "ـَا marks a pair."),
        M("Who is addressed in أَنْ تَجْلِسِي?", "a woman", ["a man", "a group of men", "two men"], "ـِي marks a woman."),
        M("What does لِيَكْتُبُوا mean?", "in order that they write", ["he wrote", "they did not write", "do not write"], "لِـ + accusative."),
        F("يُرِيد الضُّيُوف أَنْ ___ الْآن.", "يَدْخُلُوا", ["يَدْخُلُونَ", "يَدْخُلْنَ"], "A group, after أَنْ: no ن.", tr="The guests want to enter now."),
        F("أُرِيد أَنْ ___ هُنَا يَا سَلْمَى.", "تَجْلِسِي", ["تَجْلِسِينَ", "تَجْلِسَ"], "A woman, after أَنْ: no ن.", tr="I want you to sit here, Salma."),
        F("لَنْ ___ إِلَى الْمَتْحَف.", "يَذْهَبَا", ["يَذْهَبَانِ", "يَذْهَبُوا"], "A pair: ـَا without ن.", tr="The two of them will not go to the museum."),
        F("الْبَنَات يُرِدْنَ أَنْ ___.", "يَخْرُجْنَ", ["يَخْرُجُوا", "يَخْرُجَ"], "Women’s plural keeps ـْنَ.", tr="The girls want to go out."),
    ],
    verify=(vv("كتب", "sub", hum="يَكْتُبُوا", anti="تَكْتُبِي", huma_m="يَكْتُبَا", hunna="يَكْتُبْنَ") + vv("دخل", "sub", hum="يَدْخُلُوا") + vv("جلس", "sub", anti="تَجْلِسِي") + vv("ذهب", "sub", huma_m="يَذْهَبَا") + vv("خرج", "sub", hunna="يَخْرُجْنَ")),
)

# ---------------------------------------------------------------------------- 401
L401 = lesson(
    "Weak verbs after the particles",
    "أَنْ يَمْشِيَ · أَنْ يَدْعُوَ · أَنْ يَقُولَ",
    requires=["مشي", "دعا", "نسي", "قال", "نام", "وصل", "رمى", "أراد"],
    cards=[
        card("Verbs with a long vowel at the end or in the middle",
             "Verbs whose last letter is ي or و (defective verbs) show the accusative ـَ on that letter: يَمْشِي → أَنْ يَمْشِيَ; يَدْعُو → أَنْ يَدْعُوَ. "
             "If the last letter is an alif maqṣūra, nothing can show: يَنْسَى → أَنْ يَنْسَى. Hollow and assimilated verbs behave like sound verbs: يَقُولُ → أَنْ يَقُولَ, يَنَامُ → أَنْ يَنَامَ, يَصِلُ → أَنْ يَصِلَ. "
             "Groups of defective verbs lose their ن and the long vowel changes: يَمْشُونَ → أَنْ يَمْشُوا.",
             tables=[table(["Present", "After أَنْ", "English"],
                           [["يَمْشِي", "أَنْ يَمْشِيَ", "to walk"], ["يَدْعُو", "أَنْ يَدْعُوَ", "to invite"], ["يَنْسَى", "أَنْ يَنْسَى", "to forget"], ["يَقُولُ", "أَنْ يَقُولَ", "to say"], ["يَنَامُ", "أَنْ يَنَامَ", "to sleep"], ["يَصِلُ", "أَنْ يَصِلَ", "to arrive"], ["يَمْشُون", "أَنْ يَمْشُوا", "to walk (they)"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("In sentences (invented)",
             "Plans and wishes.",
             examples=[
                 ex("نُرِيد أَنْ نَمْشِيَ إِلَى السُّوق.", "We want to walk to the market.", "أَنْ نَمْشِيَ"),
                 ex("أُرِيد أَنْ أَدْعُوَ أَصْدِقَائِي.", "I want to invite my friends.", "أَنْ أَدْعُوَ"),
                 ex("لَنْ أَنْسَى هَذِهِ الرِّحْلَة.", "I will not forget this trip.", "لَنْ أَنْسَى"),
                 ex("يَجِب أَنْ تَقُولَ الْحَقِيقَة.", "You must tell the truth.", "أَنْ تَقُولَ"),
                 ex("أُرِيد أَنْ أَنَامَ مُبَكِّرًا.", "I want to sleep early.", "أَنْ أَنَامَ"),
                 ex("لَنْ يَمْشُوا إِلَى الْمَحَطَّة.", "They will not walk to the station.", "لَنْ يَمْشُوا"),
             ]),
    ],
    exercises=[
        M("What is يَمْشِي after أَنْ?", "أَنْ يَمْشِيَ", ["أَنْ يَمْشِي", "أَنْ يَمْشُوا", "أَنْ يَمْشِينَ"], "Defective verbs show ـَ on the last ي."),
        M("What is يَدْعُو after أَنْ?", "أَنْ يَدْعُوَ", ["أَنْ يَدْعِيَ", "أَنْ يَدْعُوا", "أَنْ يَدْعُونَ"], "The last و takes fatḥa."),
        M("What happens to يَنْسَى after أَنْ?", "nothing visible", ["it gets ـَ on the alif", "it loses the alif", "it gets a ن"], "Alif maqṣūra cannot carry a vowel."),
        M("What does أَنْ تَقُولَ mean?", "that you say", ["that you said", "do not say", "I say"], "قَالَ → يَقُولُ."),
        M("What is يَمْشُونَ after أَنْ?", "أَنْ يَمْشُوا", ["أَنْ يَمْشُونَ", "أَنْ يَمْشِيَ", "أَنْ يَمْشِينَ"], "A group loses its ن."),
        M("What does لَنْ أَنْسَى mean?", "I will not forget", ["I forgot", "I do not forget", "do not forget"], "لَنْ + present = will not."),
        F("نُرِيد أَنْ ___ إِلَى السُّوق.", "نَمْشِيَ", ["نَمْشِي", "نَمْشُوا"], "The last ي takes fatḥa.", tr="We want to walk to the market."),
        F("أُرِيد أَنْ ___ أَصْدِقَائِي.", "أَدْعُوَ", ["أَدْعُو", "أَدْعُوا"], "The last و takes fatḥa.", tr="I want to invite my friends."),
        F("يَجِب أَنْ ___ الْحَقِيقَة.", "تَقُولَ", ["تَقُولُ", "قُلْتَ"], "Hollow verb: ـَ at the end.", tr="You must tell the truth."),
        F("لَنْ ___ إِلَى الْمَحَطَّة.", "يَمْشُوا", ["يَمْشُونَ", "يَمْشِيَ"], "A group: the ن falls away.", tr="They will not walk to the station."),
    ],
    verify=(vv("مشي", "sub", huwa="يَمْشِيَ", hum="يَمْشُوا") + vv("دعو", "sub", ana="أَدْعُوَ") + vv("نسي", "sub", ana="أَنْسَى") + vv("قول", "sub", anta="تَقُولَ") + vv("نوم", "sub", ana="أَنَامَ")),
)

# ---------------------------------------------------------------------------- 402
L402 = lesson(
    "Derived verbs after the particles",
    "أَنْ يُسَاعِدَ · أَنْ يَتَكَلَّمَ · أَنْ يَنْتَظِرَ",
    requires=["ساعد", "تكلم", "أرسل", "قدم", "ضيف", "مدير"],
    cards=[
        card("The same ending on every measure",
             "The accusative works the same way on the derived measures. Take the present form and put ـَ on the last letter: يُسَاعِدُ → أَنْ يُسَاعِدَ; يَتَكَلَّمُ → أَنْ يَتَكَلَّمَ; يَنْتَظِرُ → أَنْ يَنْتَظِرَ; يَسْتَخْدِمُ → أَنْ يَسْتَخْدِمَ. "
             "There is no helping alif in the present, so nothing is added at the front.",
             tables=[table(["Measure", "Present", "After أَنْ"],
                           [["II", "يُوَقِّعُ", "أَنْ يُوَقِّعَ"], ["III", "يُسَاعِدُ", "أَنْ يُسَاعِدَ"], ["IV", "يُرْسِلُ", "أَنْ يُرْسِلَ"], ["V", "يَتَكَلَّمُ", "أَنْ يَتَكَلَّمَ"], ["VIII", "يَنْتَظِرُ", "أَنْ يَنْتَظِرَ"], ["X", "يَسْتَخْدِمُ", "أَنْ يَسْتَخْدِمَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences (invented)",
             "At the hotel.",
             examples=[
                 ex("أُرِيد أَنْ أُوَقِّعَ هُنَا.", "I want to sign here.", "أَنْ أُوَقِّعَ"),
                 ex("هَلْ تُرِيد أَنْ أُسَاعِدَكَ؟", "Do you want me to help you?", "أَنْ أُسَاعِدَكَ"),
                 ex("سَنَذْهَب لِنُرْسِلَ الطَّرْد.", "We will go in order to send the parcel.", "لِنُرْسِلَ"),
                 ex("يَجِب أَنْ تَتَكَلَّمَ مَعَ الْمُدِير.", "You must speak with the manager.", "أَنْ تَتَكَلَّمَ"),
                 ex("لَنْ نَنْتَظِرَ طَوِيلًا.", "We will not wait long.", "لَنْ نَنْتَظِرَ"),
                 ex("أُرِيد أَنْ أَسْتَخْدِمَ الْهَاتِف.", "I want to use the telephone.", "أَنْ أَسْتَخْدِمَ"),
             ]),
    ],
    exercises=[
        M("What is يُسَاعِدُ after أَنْ?", "أَنْ يُسَاعِدَ", ["أَنْ يُسَاعِدُ", "أَنْ سَاعِدْ", "أَنْ سَاعَدَ"], "Put ـَ on the last letter."),
        M("What is يَتَكَلَّمُ after أَنْ?", "أَنْ يَتَكَلَّمَ", ["أَنْ تَكَلَّمَ", "أَنْ يَتَكَلَّمُ", "أَنْ يُكَلِّمَ"], "Keep the prefix of the present."),
        M("What does لَنْ نَنْتَظِرَ mean?", "we will not wait", ["we waited", "we are waiting", "wait!"], "لَنْ + accusative = will not."),
        M("What does أَنْ أَسْتَخْدِمَ mean?", "that I use", ["that I used", "use!", "that he uses"], "Measure X, first person."),
        M("Is a helping alif added in the present of Measures VIII and X?", "no", ["yes, always", "only for women", "only after لَنْ"], "The alif belongs to the past and the command only."),
        M("What does لِنُرْسِلَ mean?", "in order to send", ["we sent", "send!", "they send"], "لِـ + accusative."),
        F("أُرِيد أَنْ ___ هُنَا.", "أُوَقِّعَ", ["أُوَقِّعُ", "وَقِّعْ"], "Measure II, after أَنْ.", tr="I want to sign here."),
        F("هَلْ تُرِيد أَنْ ___؟", "أُسَاعِدَكَ", ["أُسَاعِدُكَ", "سَاعِدْكَ"], "Measure III, with the suffix ـكَ.", tr="Do you want me to help you?"),
        F("يَجِب أَنْ ___ مَعَ الْمُدِير.", "تَتَكَلَّمَ", ["تَتَكَلَّمُ", "تَكَلَّمْ"], "Measure V, after أَنْ.", tr="You must speak with the manager."),
        F("أُرِيد أَنْ ___ الْهَاتِف.", "أَسْتَخْدِمَ", ["أَسْتَخْدِمُ", "اِسْتَخْدِمْ"], "Measure X, after أَنْ.", tr="I want to use the telephone."),
    ],
    verify=(vv("وقع#2", "sub", ana="أُوَقِّعَ") + vv("سعد#3", "sub", ana="أُسَاعِدَ") + vv("رسل#4", "sub", nahnu="نُرْسِلَ") + vv("كلم#5", "sub", anta="تَتَكَلَّمَ") + vv("نظر#8", "sub", nahnu="نَنْتَظِرَ") + vv("خدم#10", "sub", ana="أَسْتَخْدِمَ")),
)


# ---------------------------------------------------------------------------- 403
L403 = lesson(
    "Booking train tickets",
    "ذَهَاب وَعَوْدَة · الدَّرَجَة الْأُولَى",
    requires=["قطار", "تذكرة", "درجة", "ذهاب", "عودة", "مقعد", "رصيف", "محطة", "حجز"],
    cards=[
        card("At the ticket window",
             "A one-way ticket is ذَهَاب فَقَط, a return ticket is ذَهَاب وَعَوْدَة. Trains have classes: الدَّرَجَة الْأُولَى, “first class”, and الدَّرَجَة الثَّانِيَة, “second class”. "
             "You get a seat (مَقْعَد) with a number and a platform (رَصِيف) to wait on. Use the accusative you just learned: أُرِيد أَنْ أَحْجِزَ …. The conversation is invented.",
             tables=[table(["English", "Arabic"],
                           [["one way", "ذَهَاب فَقَط"], ["return", "ذَهَاب وَعَوْدَة"], ["first class", "الدَّرَجَة الْأُولَى"], ["second class", "الدَّرَجَة الثَّانِيَة"], ["seat", "مَقْعَد"], ["platform", "رَصِيف"], ["station", "مَحَطَّة"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُرِيد أَنْ أَحْجِزَ تَذْكِرَتَيْن إِلَى أَسْوَان.", "I want to book two tickets to Aswan.", "تَذْكِرَتَيْن"),
                 ex("ذَهَاب فَقَط أَمْ ذَهَاب وَعَوْدَة؟", "One way or return?", "أَمْ"),
                 ex("ذَهَاب وَعَوْدَة فِي الدَّرَجَة الْأُولَى مِنْ فَضْلِكَ.", "Return, in first class, please.", "الدَّرَجَة الْأُولَى"),
                 ex("كَمْ سِعْر التَّذْكِرَتَيْن؟", "How much are the two tickets?", "التَّذْكِرَتَيْن"),
                 ex("يُغَادِر الْقِطَار مِنَ الرَّصِيف الثَّالِث.", "The train leaves from the third platform.", "الرَّصِيف الثَّالِث"),
                 ex("مَقْعَدُكَ رَقْم عِشْرِين.", "Your seat is number twenty.", "مَقْعَدُكَ"),
             ]),
    ],
    exercises=[
        M("What does ذَهَاب فَقَط mean?", "one way only", ["return", "first class", "late"], "فَقَط = only."),
        M("What does ذَهَاب وَعَوْدَة mean?", "return (going and coming back)", ["one way", "second class", "two seats"], "عَوْدَة = return."),
        M("What is a رَصِيف?", "a platform", ["a seat", "a ticket", "a bridge"], "رَصِيف = platform, pavement."),
        M("What does أَنْ أَحْجِزَ mean?", "that I book", ["that I booked", "book!", "that he books"], "After أَنْ: ـَ."),
        M("What does تَذْكِرَتَيْن mean?", "two tickets", ["one ticket", "three tickets", "the ticket"], "The dual ending ـَيْن."),
        M("What does الدَّرَجَة الثَّانِيَة mean?", "second class", ["first class", "third platform", "the other train"], "ثَانِيَة = second (f.)."),
        F("أُرِيد أَنْ ___ تَذْكِرَتَيْن إِلَى أَسْوَان.", "أَحْجِزَ", ["أَحْجِزُ", "حَجَزْتُ"], "After أَنْ: ـَ.", tr="I want to book two tickets to Aswan."),
        F("ذَهَاب فَقَط ___ ذَهَاب وَعَوْدَة؟", "أَمْ", ["لَكِنْ", "ثُمَّ"], "A choice between two: أَمْ.", tr="One way or return?"),
        F("يُغَادِر الْقِطَار مِنَ ___ الثَّالِث.", "الرَّصِيف", ["الْمَقْعَد", "التَّذْكِرَة"], "A train leaves from a platform.", tr="The train leaves from the third platform."),
        F("كَمْ سِعْر ___؟", "التَّذْكِرَتَيْن", ["التَّذْكِرَة", "التَّذَاكِر"], "Two tickets: the dual.", tr="How much are the two tickets?"),
    ],
    verify=(vv("حجز", "sub", ana="أَحْجِزَ")),
)

# ---------------------------------------------------------------------------- 404
L404 = lesson(
    "The timetable and delays",
    "مَتَى يُغَادِر الْقِطَار؟ · تَأَخَّرَ نِصْف سَاعَة",
    requires=["قطار", "موعد", "ساعة", "دقيقة", "محطة", "وصل", "تأخر", "متأخر", "مساء"],
    cards=[
        card("Departures and arrivals",
             "The verb غَادَرَ يُغَادِر means “to leave (a place)”, and وَصَلَ يَصِل “to arrive”. Times use the feminine ordinals: السَّاعَة الثَّامِنَة, “eight o’clock”. "
             "A late train is مُتَأَخِّر, and تَأَخَّرَ means “was late”. These lines are an invented timetable.",
             examples=[
                 ex("مَتَى يُغَادِر الْقِطَار؟", "When does the train leave?", "مَتَى"),
                 ex("يُغَادِر الْقِطَار الْقَاهِرَة السَّاعَة الثَّامِنَة صَبَاحًا.", "The train leaves Cairo at eight in the morning.", "السَّاعَة الثَّامِنَة"),
                 ex("وَيَصِل إِلَى أَسْوَان السَّاعَة التَّاسِعَة مَسَاءً.", "And it arrives at Aswan at nine in the evening.", "وَيَصِل"),
                 ex("هَلِ الْقِطَار مُتَأَخِّر؟", "Is the train late?", "مُتَأَخِّر"),
                 ex("تَأَخَّرَ الْقِطَار نِصْف سَاعَة.", "The train was half an hour late.", "تَأَخَّرَ"),
                 ex("لَنْ يُغَادِرَ الْقِطَار قَبْلَ الْعَاشِرَة.", "The train will not leave before ten.", "لَنْ يُغَادِرَ"),
             ]),
    ],
    exercises=[
        M("What does مَتَى يُغَادِر الْقِطَار؟ ask?", "when the train leaves", ["where the train goes", "who the driver is", "how much the ticket costs"], "مَتَى = when."),
        M("What does وَيَصِل mean?", "and it arrives", ["and it leaves", "and it waits", "and it stops"], "وَصَلَ يَصِل = to arrive."),
        M("What does السَّاعَة الثَّامِنَة mean?", "eight o’clock", ["seven o’clock", "nine o’clock", "half past eight"], "ثَامِن = eighth."),
        M("What does تَأَخَّرَ الْقِطَار mean?", "The train was late", ["The train is early", "The train left", "The train is full"], "تَأَخَّرَ = to be late."),
        M("What does لَنْ يُغَادِرَ mean?", "will not leave", ["did not leave", "is leaving", "left"], "لَنْ + accusative."),
        M("Which means ‘in the evening’?", "مَسَاءً", ["صَبَاحًا", "غَدًا", "مُبَكِّرًا"], "An adverb of time."),
        F("___ الْقِطَار الْقَاهِرَة السَّاعَة الثَّامِنَة صَبَاحًا.", "يُغَادِر", ["يَصِل", "يَنْتَظِر"], "It leaves its starting city.", tr="The train leaves Cairo at eight in the morning.", lemma="غدر#3:pres:huwa"),
        F("يَصِل إِلَى أَسْوَان السَّاعَة التَّاسِعَة ___.", "مَسَاءً", ["صَبَاحًا", "غَدًا"], "Nine in the evening.", tr="It arrives at Aswan at nine in the evening."),
        F("___ الْقِطَار نِصْف سَاعَة.", "تَأَخَّرَ", ["تَأَخَّرْتُ", "يَتَأَخَّر"], "A past verb for the train.", tr="The train was half an hour late.", lemma="أخر#5:past:huwa"),
        F("لَنْ ___ الْقِطَار قَبْلَ الْعَاشِرَة.", "يُغَادِرَ", ["يُغَادِرُ", "غَادَرَ"], "After لَنْ: ـَ.", tr="The train will not leave before ten."),
    ],
    verify=(vv("غدر#3", "pres", huwa="يُغَادِر") + vv("وصل", "pres", huwa="يَصِل")),
)

# ---------------------------------------------------------------------------- 405
L405 = lesson(
    "Aswan and the High Dam",
    "السَّدّ الْعَالِي · الْكَهْرَبَاء وَالْفَيَضَان",
    requires=["سد", "كهرباء", "فيضان", "بحيرة", "نيل", "جنوب", "سائح", "زار"],
    cards=[
        card("A dam on the Nile",
             "Aswan lies in the south of Egypt. Near the city there is a big dam on the Nile, السَّدّ الْعَالِي, “the High Dam”. It was built in the twentieth century. "
             "A large lake lies behind it (بُحَيْرَة). The dam gives electricity (كَهْرَبَاء) and helps to control the flood (فَيَضَان) of the river. The sentences are simple and invented.",
             tables=[table(["English", "Arabic"],
                           [["dam", "سَدّ"], ["lake", "بُحَيْرَة"], ["electricity", "كَهْرَبَاء"], ["flood", "فَيَضَان"], ["Aswan", "أَسْوَان"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("تَقَع أَسْوَان فِي جَنُوب مِصْر.", "Aswan is situated in the south of Egypt.", "جَنُوب مِصْر"),
                 ex("السَّدّ الْعَالِي سَدّ كَبِير عَلَى النِّيل.", "The High Dam is a big dam on the Nile.", "السَّدّ الْعَالِي"),
                 ex("بُنِيَ السَّدّ فِي الْقَرْن الْعِشْرِين.", "The dam was built in the twentieth century.", "الْقَرْن الْعِشْرِين"),
                 ex("خَلْفَ السَّدّ بُحَيْرَة كَبِيرَة.", "Behind the dam there is a big lake.", "خَلْفَ السَّدّ"),
                 ex("يُنْتِج السَّدّ الْكَهْرَبَاء.", "The dam produces electricity.", "يُنْتِج"),
                 ex("يَمْنَع السَّدّ الْفَيَضَان.", "The dam prevents flooding.", "يَمْنَع"),
                 ex("يُرِيد السُّيَّاح أَنْ يَزُورُوا السَّدّ.", "The tourists want to visit the dam.", "أَنْ يَزُورُوا"),
             ]),
    ],
    exercises=[
        M("What is a سَدّ?", "a dam", ["a bridge", "a lake", "a boat"], "سَدّ = dam."),
        M("Where is Aswan?", "in the south of Egypt", ["in the north of Egypt", "in Syria", "in the sea"], "تَقَع أَسْوَان فِي جَنُوب مِصْر."),
        M("What does the dam produce?", "electricity", ["bread", "ice", "stones"], "كَهْرَبَاء = electricity."),
        M("What does يَمْنَع السَّدّ الْفَيَضَان mean?", "The dam prevents flooding", ["The dam causes flooding", "The dam is closed", "The dam is old"], "مَنَعَ = to prevent."),
        M("What does خَلْفَ السَّدّ mean?", "behind the dam", ["in front of the dam", "on the dam", "near the dam"], "خَلْفَ = behind."),
        M("Why is it بُنِيَ السَّدّ?", "a passive verb with a masculine subject", ["a command", "a feminine verb", "a dual noun"], "No doer is named."),
        F("تَقَع أَسْوَان فِي ___ مِصْر.", "جَنُوب", ["شَمَال", "وَسَط"], "Aswan is in the south.", tr="Aswan is situated in the south of Egypt."),
        F("___ السَّدّ الْكَهْرَبَاء.", "يُنْتِج", ["يَمْنَع", "يَزُور"], "The dam produces electricity.", tr="The dam produces electricity."),
        F("خَلْفَ السَّدّ ___ كَبِيرَة.", "بُحَيْرَة", ["جِسْر", "جَبَل"], "A lake is feminine, like كَبِيرَة.", tr="Behind the dam there is a big lake."),
        F("يُرِيد السُّيَّاح أَنْ ___ السَّدّ.", "يَزُورُوا", ["يَزُورُونَ", "يَزُورَ"], "A group after أَنْ: no ن.", tr="The tourists want to visit the dam."),
    ],
    verify=(vv("زور", "sub", hum="يَزُورُوا")),
)

# ---------------------------------------------------------------------------- 406
L406 = lesson(
    "The temples of Luxor",
    "مَعْبَدَان كَبِيرَان · الْأُقْصُر وَالْكَرْنَك",
    requires=["معبد", "أقصر", "غرب", "تمثال", "طريق", "قديم", "مدينة", "وسط"],
    cards=[
        card("A city of ancient remains",
             "Luxor, الْأُقْصُر, is a city on the Nile with many ancient remains. It has two large temples, مَعْبَد الْأُقْصُر and مَعْبَد الْكَرْنَك. "
             "A long road with many statues is said to join them. On the western bank there are old tombs. The sentences are simple and invented.",
             examples=[
                 ex("فِي الْأُقْصُر مَعْبَدَان كَبِيرَان.", "In Luxor there are two large temples.", "مَعْبَدَان كَبِيرَان"),
                 ex("اِسْمُ الْأَوَّل مَعْبَد الْأُقْصُر وَالثَّانِي مَعْبَد الْكَرْنَك.", "The first is called the Luxor temple and the second the Karnak temple.", "الثَّانِي"),
                 ex("بَيْنَهُمَا طَرِيق فِيهِ تَمَاثِيل كَثِيرَة.", "Between them is a road with many statues.", "بَيْنَهُمَا"),
                 ex("الْمَقَابِر الْقَدِيمَة عَلَى الضِّفَّة الْغَرْبِيَّة.", "The old tombs are on the western bank.", "الْمَقَابِر الْقَدِيمَة"),
                 ex("يَزُور السُّيَّاح الْمَعْبَدَيْن كُلَّ يَوْم.", "The tourists visit the two temples every day.", "الْمَعْبَدَيْن"),
                 ex("اِذْهَبْ إِلَى الْكَرْنَك صَبَاحًا لِأَنَّ الْجَوّ حَارّ.", "Go to Karnak in the morning because the weather is hot.", "اِذْهَبْ"),
             ]),
    ],
    exercises=[
        M("What does مَعْبَدَان mean?", "two temples", ["one temple", "three temples", "the temple"], "The dual ـَان."),
        M("What does بَيْنَهُمَا mean?", "between the two of them", ["behind them", "above them", "with them"], "بَيْنَ + هُمَا."),
        M("Where are the old tombs?", "on the western bank", ["on the eastern bank", "in the museum", "on the train"], "الضِّفَّة الْغَرْبِيَّة."),
        M("Why كَبِيرَان in مَعْبَدَان كَبِيرَان?", "the adjective agrees with a dual noun", ["مَعْبَد is feminine", "it is a verb", "it is a plural of people"], "A dual noun takes a dual adjective."),
        M("What does الْمَعْبَدَيْن mean here?", "the two temples (object)", ["the two temples (subject)", "the temple", "two doors"], "The oblique dual ends in ـَيْن."),
        M("What does اِذْهَبْ إِلَى الْكَرْنَك صَبَاحًا advise?", "go to Karnak in the morning", ["go to Karnak at night", "do not go to Karnak", "I went to Karnak"], "A command to one man."),
        F("فِي الْأُقْصُر ___ كَبِيرَان.", "مَعْبَدَان", ["مَعْبَد", "مَعَابِد"], "Two temples: the dual.", tr="In Luxor there are two large temples."),
        F("بَيْنَهُمَا ___ فِيهِ تَمَاثِيل كَثِيرَة.", "طَرِيق", ["جِسْر", "سَدّ"], "A road with statues.", tr="Between them is a road with many statues."),
        F("الْمَقَابِر الْقَدِيمَة عَلَى الضِّفَّة ___.", "الْغَرْبِيَّة", ["الْغَرْبِيّ", "غَرْبِيَّة"], "ضِفَّة is feminine.", tr="The old tombs are on the western bank."),
        F("يَزُور السُّيَّاح ___ كُلَّ يَوْم.", "الْمَعْبَدَيْن", ["الْمَعْبَدَان", "الْمَعْبَد"], "The object of a verb: ـَيْن.", tr="The tourists visit the two temples every day."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 407
L407 = lesson(
    "A Nile cruise",
    "رِحْلَة نِيلِيَّة · تُغَادِر الْبَاخِرَة الْمَرْسَى",
    requires=["رحلة", "سفينة", "مرسى", "عشاء", "نهر", "ساعة", "مساء", "ميناء"],
    cards=[
        card("On the river",
             "Many tourists travel on the Nile between Aswan and Luxor by boat, a رِحْلَة نِيلِيَّة, “Nile trip”. The boat is a بَاخِرَة or a سَفِينَة. It stops at a landing place (مَرْسَى) and sails again. "
             "Dinner (عَشَاء) is served on board. The timetable below is invented.",
             tables=[table(["English", "Arabic"],
                           [["Nile trip", "رِحْلَة نِيلِيَّة"], ["steamer, ship", "بَاخِرَة"], ["ship", "سَفِينَة"], ["landing place, pier", "مَرْسَى"], ["dinner", "عَشَاء"], ["roof, deck", "سَطْح"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("نُرِيد رِحْلَة نِيلِيَّة مِنْ أَسْوَان إِلَى الْأُقْصُر.", "We want a Nile trip from Aswan to Luxor.", "رِحْلَة نِيلِيَّة"),
                 ex("تُغَادِر الْبَاخِرَة الْمَرْسَى السَّاعَة السَّابِعَة مَسَاءً.", "The boat leaves the pier at seven in the evening.", "تُغَادِر"),
                 ex("نَتَعَشَّى عَلَى سَطْح الْبَاخِرَة.", "We have dinner on the deck of the boat.", "سَطْح الْبَاخِرَة"),
                 ex("تَقِف الْبَاخِرَة عِنْدَ الْمَرْسَى لِسَاعَتَيْن.", "The boat stops at the pier for two hours.", "لِسَاعَتَيْن"),
                 ex("يَجِب أَنْ نَرْجِعَ قَبْلَ الْعَاشِرَة.", "We must come back before ten.", "أَنْ نَرْجِعَ"),
                 ex("لَنْ تَتَحَرَّكَ الْبَاخِرَة قَبْلَ الصَّبَاح.", "The boat will not move before morning.", "لَنْ تَتَحَرَّكَ"),
             ]),
    ],
    exercises=[
        M("What is a بَاخِرَة?", "a steamer, a ship", ["a train", "a temple", "a bridge"], "بَاخِرَة = steamship."),
        M("What is a مَرْسَى?", "a landing place, a pier", ["a deck", "a ticket", "a cabin"], "A boat ties up at the مَرْسَى."),
        M("What does رِحْلَة نِيلِيَّة mean?", "a Nile trip", ["a night train", "a sea trip", "a long road"], "نِيلِيَّة = of the Nile."),
        M("What does تُغَادِر الْبَاخِرَة الْمَرْسَى mean?", "The boat leaves the pier", ["The boat reaches the pier", "The pier is closed", "The boat is old"], "غَادَرَ = to leave."),
        M("What does لِسَاعَتَيْن mean?", "for two hours", ["after two hours", "in two days", "two o’clock"], "لِـ + dual."),
        M("What does لَنْ تَتَحَرَّكَ الْبَاخِرَة mean?", "The boat will not move", ["The boat moved", "The boat is moving", "Move the boat"], "لَنْ + accusative."),
        F("تُغَادِر ___ الْمَرْسَى السَّاعَة السَّابِعَة.", "الْبَاخِرَة", ["الْقِطَار", "الْمَعْبَد"], "A boat leaves a pier.", tr="The boat leaves the pier at seven."),
        F("نَتَعَشَّى عَلَى ___ الْبَاخِرَة.", "سَطْح", ["بَاب", "رَصِيف"], "On the deck.", tr="We have dinner on the deck of the boat."),
        F("يَجِب أَنْ ___ قَبْلَ الْعَاشِرَة.", "نَرْجِعَ", ["نَرْجِعُ", "رَجَعْنَا"], "After أَنْ: ـَ.", tr="We must come back before ten."),
        F("لَنْ ___ الْبَاخِرَة قَبْلَ الصَّبَاح.", "تَتَحَرَّكَ", ["تَتَحَرَّكُ", "تَحَرَّكَتْ"], "After لَنْ: ـَ.", tr="The boat will not move before morning."),
    ],
    verify=(vv("رجع", "sub", nahnu="نَرْجِعَ") + vv("حرك#5", "sub", hiya="تَتَحَرَّكَ")),
)

# ---------------------------------------------------------------------------- 408
L408 = lesson(
    "The sound and light show",
    "عَرْض الصَّوْت وَالضَّوْء · يَحْكِي قِصَّة الْمَعْبَد",
    requires=["عرض", "صوت", "ضوء", "قصة", "بدأ", "معبد", "غروب", "زوجة", "أعجب"],
    cards=[
        card("An evening at the temple",
             "In the evening there may be a show of sound and light at a temple, عَرْض الصَّوْت وَالضَّوْء. Voices and lights tell the story of the place (يَحْكِي قِصَّة الْمَعْبَد). "
             "The show starts after sunset (بَعْدَ الْغُرُوب). The verb أَعْجَبَ means “to please”: أَعْجَبَنِي الْعَرْض, “the show pleased me”. The sentences are invented.",
             examples=[
                 ex("مَتَى يَبْدَأ عَرْض الصَّوْت وَالضَّوْء؟", "When does the sound and light show begin?", "يَبْدَأ"),
                 ex("يَبْدَأ الْعَرْض بَعْدَ الْغُرُوب.", "The show begins after sunset.", "بَعْدَ الْغُرُوب"),
                 ex("يَحْكِي الْعَرْض قِصَّة الْمَعْبَد.", "The show tells the story of the temple.", "يَحْكِي"),
                 ex("اِشْتَرَيْنَا تَذَاكِر لِلْعَرْض.", "We bought tickets for the show.", "لِلْعَرْض"),
                 ex("أَعْجَبَنِي الْعَرْض كَثِيرًا.", "I liked the show very much.", "أَعْجَبَنِي"),
                 ex("أَعْجَبَ الْعَرْض زَوْجَتِي أَيْضًا.", "The show pleased my wife too.", "زَوْجَتِي"),
             ]),
    ],
    exercises=[
        M("What does عَرْض الصَّوْت وَالضَّوْء mean?", "the sound and light show", ["the train timetable", "the ticket office", "the hotel bill"], "صَوْت = sound; ضَوْء = light."),
        M("When does the show begin?", "after sunset", ["before dawn", "at noon", "after midnight"], "بَعْدَ الْغُرُوب."),
        M("What does يَحْكِي الْعَرْض قِصَّة الْمَعْبَد mean?", "The show tells the story of the temple", ["The show closes the temple", "The show sells tickets", "The show ends at the temple"], "حَكَى = to tell."),
        M("What does أَعْجَبَنِي الْعَرْض mean?", "I liked the show", ["I missed the show", "I paid for the show", "I left the show"], "أَعْجَبَ = to please."),
        M("What does ـنِي mean in أَعْجَبَنِي?", "me", ["you", "him", "us"], "The object suffix."),
        M("What does زَوْجَتِي mean?", "my wife", ["my sister", "my mother", "my friend"], "زَوْجَة = wife."),
        F("يَبْدَأ الْعَرْض بَعْدَ ___.", "الْغُرُوب", ["الْمَرْسَى", "السَّطْح"], "After sunset.", tr="The show begins after sunset."),
        F("اِشْتَرَيْنَا ___ لِلْعَرْض.", "تَذَاكِر", ["بَاخِرَة", "مَقَابِر"], "We buy tickets.", tr="We bought tickets for the show."),
        F("___ الْعَرْض كَثِيرًا.", "أَعْجَبَنِي", ["أَعْجَبْتُ", "يُعْجِبُنِي"], "The show pleased me.", tr="I liked the show very much."),
        F("أَعْجَبَ الْعَرْض ___ أَيْضًا.", "زَوْجَتِي", ["زَوْجِي", "زَوْجَتُكَ"], "My wife.", tr="The show pleased my wife too."),
    ],
    verify=(vv("عجب#4", "past", huwa="أَعْجَبَ")),
)


# ---------------------------------------------------------------------------- 409
L409 = lesson(
    "Let us, let him: لِـ with the jussive",
    "لِنَذْهَبْ · لِيَدْخُلِ الضُّيُوف",
    requires=["ذهب", "جلس", "دخل", "كتب", "ضيف", "بريد", "مكتب"],
    cards=[
        card("A command for ‘we’, ‘he’ and ‘she’",
             "The command form exists only for ‘you’. To give an order or a suggestion to ‘we’, ‘he’, ‘she’ or ‘they’, put لِـ before the short present (the jussive): لِنَذْهَبْ, “let us go”; لِيَدْخُلْ, “let him enter”; لِتَجْلِسْ, “let her sit”. "
             "The jussive ends in sukūn, like the command. Compare: لِيَكْتُبْ, “let him write”, and لِيَكْتُبَ, “so that he writes” (purpose, accusative). Only the final vowel tells them apart.",
             tables=[table(["Person", "Short present", "With لِـ"],
                           [["we", "نَذْهَبْ", "لِنَذْهَبْ"], ["he", "يَدْخُلْ", "لِيَدْخُلْ"], ["she", "تَجْلِسْ", "لِتَجْلِسْ"], ["they (m.)", "يَكْتُبُوا", "لِيَكْتُبُوا"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences (invented)",
             "At the post office.",
             examples=[
                 ex("لِنَذْهَبْ إِلَى مَكْتَب الْبَرِيد.", "Let us go to the post office.", "لِنَذْهَبْ"),
                 ex("لِنَجْلِسْ هُنَا قَلِيلًا.", "Let us sit here a little.", "لِنَجْلِسْ"),
                 ex("لِيَدْخُلِ الضُّيُوف الْآن.", "Let the guests enter now.", "لِيَدْخُلِ"),
                 ex("لِتَجْلِسْ سَلْمَى هُنَا.", "Let Salma sit here.", "لِتَجْلِسْ"),
                 ex("لِيَكْتُبْ كُلّ وَاحِد اِسْمَهُ.", "Let each one write his name.", "لِيَكْتُبْ"),
                 ex("جِئْنَا لِنَكْتُبَ الْعَنَاوِين.", "We came in order to write the addresses.", "لِنَكْتُبَ"),
             ]),
    ],
    exercises=[
        M("What does لِنَذْهَبْ mean?", "let us go", ["we went", "we will go", "do not go"], "لِـ + short present = let …"),
        M("What does لِيَدْخُلِ الضُّيُوف mean?", "Let the guests enter", ["The guests entered", "The guests will enter", "Do not let the guests enter"], "A request about the third person."),
        M("Which ending does the jussive have?", "ـْ (sukūn)", ["ـَ (fatḥa)", "ـُ (ḍamma)", "ـِ (kasra)"], "The short present ends in sukūn."),
        M("What is the difference between لِيَكْتُبْ and لِيَكْتُبَ?", "let him write / so that he writes", ["past / future", "man / woman", "one / two"], "Sukūn = command; fatḥa = purpose."),
        M("Who is spoken about in لِتَجْلِسْ سَلْمَى?", "Salma, a woman", ["a man", "a group", "the speaker"], "تَـ + a feminine subject."),
        M("What does جِئْنَا لِنَكْتُبَ الْعَنَاوِين mean?", "We came to write the addresses", ["Let us write the addresses", "We wrote the addresses", "Do not write the addresses"], "لِنَكْتُبَ with fatḥa is purpose."),
        F("___ إِلَى مَكْتَب الْبَرِيد.", "لِنَذْهَبْ", ["لِنَذْهَبَ", "ذَهَبْنَا"], "A suggestion, with the sukūn.", tr="Let us go to the post office."),
        F("___ سَلْمَى هُنَا.", "لِتَجْلِسْ", ["لِيَجْلِسْ", "جَلَسَتْ"], "A woman: تَـ.", tr="Let Salma sit here."),
        F("لِيَكْتُبْ كُلّ وَاحِد ___.", "اِسْمَهُ", ["اِسْمَكَ", "اِسْمِي"], "His own name: ـهُ.", tr="Let each one write his name."),
        F("جِئْنَا لِ___ الْعَنَاوِين.", "نَكْتُبَ", ["نَكْتُبْ", "كَتَبْنَا"], "Purpose: with fatḥa.", tr="We came in order to write the addresses."),
    ],
    verify=(vv("ذهب", "jus", nahnu="نَذْهَبْ") + vv("دخل", "jus", huwa="يَدْخُلْ") + vv("جلس", "jus", hiya="تَجْلِسْ") + vv("كتب", "jus", huwa="يَكْتُبْ", hum="يَكْتُبُوا") + vv("كتب", "sub", nahnu="نَكْتُبَ")),
)

# ---------------------------------------------------------------------------- 410
L410 = lesson(
    "Three moods side by side",
    "يَكْتُبُ · أَنْ يَكْتُبَ · لَمْ يَكْتُبْ",
    requires=["كتب", "ذهب", "وصل", "رسالة", "بريد", "أراد", "فتح", "قطار"],
    cards=[
        card("Which ending after which word?",
             "A present verb has three moods, and the word before it decides which one you need. With nothing before it, the verb is indicative (ـُ). After أَنْ, لَنْ, كَيْ, لِـ (purpose) or حَتَّى it is accusative (ـَ). After لَمْ, لَا (a command) or لِـ (a command) it is jussive (ـْ). "
             "The group forms lose their ن in the accusative and the jussive, the women’s plural never does.",
             tables=[table(["Mood", "he", "they"],
                           [["indicative", "يَكْتُبُ", "يَكْتُبُون"], ["accusative", "أَنْ يَكْتُبَ", "أَنْ يَكْتُبُوا"], ["jussive", "لَمْ يَكْتُبْ", "لَمْ يَكْتُبُوا"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("One verb, many sentences (invented)",
             "The same verb, three moods.",
             examples=[
                 ex("يَصِلُ الْقِطَار فِي الصَّبَاح.", "The train arrives in the morning.", "يَصِلُ"),
                 ex("أُرِيد أَنْ يَصِلَ الْقِطَار مُبَكِّرًا.", "I want the train to arrive early.", "أَنْ يَصِلَ"),
                 ex("لَنْ يَصِلَ الْقِطَار الْيَوْم.", "The train will not arrive today.", "لَنْ يَصِلَ"),
                 ex("لَمْ يَصِلِ الْقِطَار أَمْس.", "The train did not arrive yesterday.", "لَمْ يَصِلِ"),
                 ex("لَا تَذْهَبْ إِلَى الْمَحَطَّة الْآن.", "Do not go to the station now.", "لَا تَذْهَبْ"),
                 ex("هَلْ يَفْتَحُ الْمَكْتَب غَدًا؟", "Does the office open tomorrow?", "يَفْتَحُ"),
             ]),
    ],
    exercises=[
        M("Which mood follows لَنْ?", "accusative", ["indicative", "jussive", "none"], "لَنْ takes ـَ."),
        M("Which mood follows لَمْ?", "jussive", ["accusative", "indicative", "none"], "لَمْ takes ـْ."),
        M("Which mood has no particle before it?", "indicative", ["accusative", "jussive", "none of them"], "The plain present ends in ـُ."),
        M("What does لَمْ يَصِلْ mean?", "did not arrive", ["will not arrive", "does not arrive", "arrives"], "لَمْ + jussive = past negative."),
        M("What does لَا تَذْهَبْ mean?", "do not go", ["you do not go", "you went", "go!"], "لَا + jussive in the second person = prohibition."),
        M("Which word is followed by the accusative?", "حَتَّى", ["لَمْ", "هَلْ", "مَتَى"], "حَتَّى takes ـَ."),
        F("لَنْ ___ الْقِطَار الْيَوْم.", "يَصِلَ", ["يَصِلْ", "يَصِلُ"], "After لَنْ: ـَ.", tr="The train will not arrive today."),
        F("لَمْ ___ الْقِطَار أَمْس.", "يَصِلِ", ["يَصِلَ", "يَصِلُ"], "After لَمْ: ـْ (a helping kasra before الـ).", tr="The train did not arrive yesterday."),
        F("أُرِيد أَنْ ___ الْقِطَار مُبَكِّرًا.", "يَصِلَ", ["يَصِلْ", "يَصِلُ"], "After أَنْ: ـَ.", tr="I want the train to arrive early."),
        F("___ الْقِطَار فِي الصَّبَاح.", "يَصِلُ", ["يَصِلَ", "يَصِلْ"], "No particle: ـُ.", tr="The train arrives in the morning."),
        F("لَا ___ إِلَى الْمَحَطَّة الْآن.", "تَذْهَبْ", ["تَذْهَبَ", "تَذْهَبُ"], "A prohibition: ـْ.", tr="Do not go to the station now."),
    ],
    verify=(vv("وصل", "sub", huwa="يَصِلَ") + vv("وصل", "jus", huwa="يَصِلْ") + vv("كتب", "jus", hum="يَكْتُبُوا") + vv("كتب", "sub", hum="يَكْتُبُوا")),
)

# ---------------------------------------------------------------------------- 411
L411 = lesson(
    "At the post office: stamps and parcels",
    "طَابِع · ظَرْف · طَرْد · بَرِيد جَوِّيّ",
    requires=["بريد", "طابع", "ظرف", "بطاقة", "طرد", "مسجل", "جوي", "وزن", "كيلو", "ثقيل", "خفيف"],
    cards=[
        card("Words for the post",
             "At the post office, مَكْتَب الْبَرِيد, you buy stamps (طَوَابِع), send postcards (بِطَاقَات بَرِيدِيَّة), letters in envelopes (ظُرُوف) and parcels (طُرُود). "
             "You can choose ordinary mail, registered mail (بَرِيد مُسَجَّل) or air mail (بَرِيد جَوِّيّ). The clerk weighs the parcel: its weight is its وَزْن. The conversation is invented.",
             tables=[table(["English", "Arabic"],
                           [["post office", "مَكْتَب الْبَرِيد"], ["stamp", "طَابِع"], ["envelope", "ظَرْف"], ["postcard", "بِطَاقَة بَرِيدِيَّة"], ["parcel", "طَرْد"], ["registered mail", "بَرِيد مُسَجَّل"], ["air mail", "بَرِيد جَوِّيّ"], ["weight", "وَزْن"], ["heavy", "ثَقِيل"], ["light", "خَفِيف"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُرِيد طَوَابِع لِخَمْس بِطَاقَات بَرِيدِيَّة.", "I want stamps for five postcards.", "لِخَمْس بِطَاقَات"),
                 ex("كَمْ وَزْن هَذَا الطَّرْد؟", "How much does this parcel weigh?", "وَزْن"),
                 ex("وَزْنُهُ ثَلَاثَة كِيلُو.", "Its weight is three kilos.", "ثَلَاثَة كِيلُو"),
                 ex("هَلْ تُرِيد بَرِيدًا عَادِيًّا أَمْ مُسَجَّلًا؟", "Do you want ordinary or registered mail?", "مُسَجَّلًا"),
                 ex("بِالْبَرِيد الْجَوِّيّ مِنْ فَضْلِكَ.", "By air mail, please.", "الْجَوِّيّ"),
             ]),
    ],
    exercises=[
        M("What is a طَرْد?", "a parcel", ["a stamp", "a postcard", "an envelope"], "طَرْد = parcel."),
        M("What is a طَابِع?", "a stamp", ["a parcel", "a clerk", "a box"], "طَابِع = (postage) stamp."),
        M("What does بَرِيد جَوِّيّ mean?", "air mail", ["registered mail", "a train ticket", "a postcard"], "جَوّ = air, sky."),
        M("What does كَمْ وَزْن هَذَا الطَّرْد؟ ask?", "how much the parcel weighs", ["how much the parcel costs", "where the parcel is", "when the parcel leaves"], "وَزْن = weight."),
        M("What does ثَقِيل mean?", "heavy", ["light", "cheap", "late"], "ثَقِيل = heavy."),
        M("Which noun follows خَمْس in لِخَمْس بِطَاقَات?", "a plural noun", ["a singular noun", "a dual noun", "a verb"], "3–10 + plural."),
        F("أُرِيد ___ لِخَمْس بِطَاقَات بَرِيدِيَّة.", "طَوَابِع", ["طُرُود", "ظُرُوف"], "Stamps for postcards.", tr="I want stamps for five postcards."),
        F("كَمْ ___ هَذَا الطَّرْد؟", "وَزْن", ["سَدّ", "جِسْر"], "“weight”.", tr="How much does this parcel weigh?"),
        F("هَذَا الطَّرْد ___، وَزْنُهُ عِشْرُون كِيلُو.", "ثَقِيل", ["خَفِيف", "قَصِير"], "Twenty kilos is heavy.", tr="This parcel is heavy, its weight is twenty kilos."),
        F("بِالْبَرِيد ___ مِنْ فَضْلِكَ.", "الْجَوِّيّ", ["الْجَوِّيَّة", "جَوِّيّ"], "The noun is masculine and definite.", tr="By air mail, please."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 412
L412 = lesson(
    "Sending gifts home",
    "أُرِيد أَنْ أُرْسِلَ هَذِهِ الْهَدَايَا · سَيَصِل بَعْدَ أُسْبُوعَيْن",
    requires=["هدية", "عائلة", "طرد", "عنوان", "إيصال", "أسبوع", "دفع", "كتب"],
    cards=[
        card("A conversation at the counter (invented)",
             "A tourist sends presents to her family. The clerk answers with commands and with the future.",
             examples=[
                 ex("أُرِيد أَنْ أُرْسِلَ هَذِهِ الْهَدَايَا إِلَى عَائِلَتِي.", "I want to send these presents to my family.", "أَنْ أُرْسِلَ"),
                 ex("اُكْتُبِي الْعُنْوَان عَلَى الطَّرْد.", "Write the address on the parcel (to a woman).", "اُكْتُبِي"),
                 ex("كَمْ يَوْمًا يَحْتَاج الطَّرْد؟", "How many days does the parcel need?", "يَحْتَاج"),
                 ex("سَيَصِل الطَّرْد بَعْدَ أُسْبُوعَيْن.", "The parcel will arrive after two weeks.", "بَعْدَ أُسْبُوعَيْن"),
                 ex("هَلْ تُرِيدِينَ أَنْ تَدْفَعِي الْآن؟", "Do you want to pay now? (to a woman)", "أَنْ تَدْفَعِي"),
                 ex("خُذِي هَذَا الْإِيصَال مِنْ فَضْلِكِ.", "Take this receipt, please. (to a woman)", "خُذِي"),
             ]),
    ],
    exercises=[
        M("What does أُرِيد أَنْ أُرْسِلَ mean?", "I want to send", ["I sent", "send!", "he wants to send"], "أَنْ + accusative."),
        M("What does بَعْدَ أُسْبُوعَيْن mean?", "after two weeks", ["for two weeks", "two weeks ago", "in two days"], "أُسْبُوعَيْن = two weeks (dual)."),
        M("What is an إِيصَال?", "a receipt", ["a stamp", "a parcel", "a form"], "إِيصَال = receipt."),
        M("Who is addressed in خُذِي?", "a woman", ["a man", "a group", "two men"], "ـِي marks a woman."),
        M("What does اُكْتُبِي الْعُنْوَان mean?", "Write the address (to a woman)", ["I wrote the address", "He lost the address", "The address is long"], "A command to one woman."),
        M("What does سَيَصِل الطَّرْد mean?", "The parcel will arrive", ["The parcel arrived", "The parcel is heavy", "The parcel is open"], "سَـ = will."),
        F("أُرِيد أَنْ ___ هَذِهِ الْهَدَايَا.", "أُرْسِلَ", ["أُرْسِلُ", "أَرْسَلْتُ"], "After أَنْ: ـَ.", tr="I want to send these presents."),
        F("___ الْعُنْوَان عَلَى الطَّرْد.", "اُكْتُبِي", ["كَتَبَ", "يَكْتُبُ"], "A command to one woman.", tr="Write the address on the parcel."),
        F("سَيَصِل الطَّرْد بَعْدَ ___.", "أُسْبُوعَيْن", ["أُسْبُوع", "أُسْبُوعَان"], "After بَعْدَ the dual is ـَيْن.", tr="The parcel will arrive after two weeks."),
        F("هَلْ تُرِيدِينَ أَنْ ___ الْآن؟", "تَدْفَعِي", ["تَدْفَعِينَ", "تَدْفَعَ"], "A woman, after أَنْ: no ن.", tr="Do you want to pay now?"),
    ],
    verify=(vv("رسل#4", "sub", ana="أُرْسِلَ") + vv("دفع", "sub", anti="تَدْفَعِي") + vv("وصل", "fut", huwa="سَيَصِل")),
)

# ---------------------------------------------------------------------------- 413
L413 = lesson(
    "Filling in a form",
    "اِمْلَأِ الِاسْتِمَارَة · اُكْتُبْ بِوُضُوح",
    requires=["عنوان", "هاتف", "تاريخ", "قيمة", "توقيع", "واضح"],
    cards=[
        card("The boxes on a form",
             "A form (اِسْتِمَارَة) asks for your name (الِاسْم), address (الْعُنْوَان), telephone number (رَقْم الْهَاتِف), the contents of the parcel (مُحْتَوَيَات الطَّرْد), its value (الْقِيمَة), the date (التَّارِيخ) and your signature (التَّوْقِيع). "
             "The clerk gives orders: fill in, write, sign. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["name", "الِاسْم"], ["address", "الْعُنْوَان"], ["telephone number", "رَقْم الْهَاتِف"], ["contents", "مُحْتَوَيَات الطَّرْد"], ["value", "الْقِيمَة"], ["date", "التَّارِيخ"], ["signature", "التَّوْقِيع"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("اِمْلَأِ الِاسْتِمَارَة مِنْ فَضْلِكَ.", "Fill in the form, please.", "اِمْلَأِ"),
                 ex("اُكْتُبْ بِحُرُوف وَاضِحَة.", "Write in clear letters.", "بِحُرُوف وَاضِحَة"),
                 ex("اُكْتُبِي مُحْتَوَيَات الطَّرْد وَقِيمَتَهَا.", "Write the contents of the parcel and their value.", "قِيمَتَهَا"),
                 ex("لَا تَنْسَ التَّارِيخ.", "Do not forget the date.", "لَا تَنْسَ"),
                 ex("وَقِّعْ فِي الْأَسْفَل.", "Sign at the bottom.", "وَقِّعْ"),
             ]),
    ],
    exercises=[
        M("What is an اِسْتِمَارَة?", "a form", ["a stamp", "a parcel", "a receipt"], "اِسْتِمَارَة = form."),
        M("What does اِمْلَأِ الِاسْتِمَارَة mean?", "Fill in the form", ["Tear the form", "Read the form", "Sign the form"], "مَلَأَ = to fill."),
        M("What does وَقِّعْ فِي الْأَسْفَل mean?", "Sign at the bottom", ["Write at the top", "Wait here", "Pay below"], "وَقِّعْ = sign!"),
        M("What does مُحْتَوَيَات mean?", "contents", ["value", "weight", "address"], "What is inside."),
        M("What does بِحُرُوف وَاضِحَة mean?", "in clear letters", ["in red ink", "in a hurry", "in Arabic only"], "وَاضِح = clear."),
        M("What does لَا تَنْسَ التَّارِيخ mean?", "Do not forget the date", ["Write the date", "I forgot the date", "The date is wrong"], "نَسِيَ = to forget."),
        F("___ الِاسْتِمَارَة مِنْ فَضْلِكَ.", "اِمْلَأِ", ["مَلَأَ", "يَمْلَأُ"], "A command to one man.", tr="Fill in the form, please."),
        F("اُكْتُبْ بِحُرُوف ___.", "وَاضِحَة", ["وَاضِح", "وَاضِحُون"], "Plural of a thing: feminine singular.", tr="Write in clear letters."),
        F("اُكْتُبِي مُحْتَوَيَات الطَّرْد وَ___.", "قِيمَتَهَا", ["قِيمَتَهُمْ", "قِيمَتَكَ"], "The contents are plural: ـهَا.", tr="Write the contents of the parcel and their value."),
        F("___ فِي الْأَسْفَل.", "وَقِّعْ", ["وَقَّعَ", "يُوَقِّع"], "A command to one man.", tr="Sign at the bottom.", lemma="وقع#2:imp:anta"),
    ],
    verify=(vv("وقع#2", "imp", anta="وَقِّعْ") + vv("نسي", "neg", anta="لَا تَنْسَ")),
)

# ---------------------------------------------------------------------------- 414
L414 = lesson(
    "A postcard from Luxor",
    "أُمِّي الْعَزِيزَة · أَكْتُب لَكِ مِنَ الْأُقْصُر",
    requires=["بطاقة", "عزيز", "حب", "لقاء", "أقصر", "معبد", "حار", "جميل"],
    cards=[
        card("How to write a postcard",
             "A postcard has a greeting, a short message and a closing. A greeting can be أُمِّي الْعَزِيزَة, “my dear mother”, or أَبِي الْعَزِيز, “my dear father”. "
             "The closing can be مَعَ حُبِّي, “with my love”, or إِلَى اللِّقَاء, “until we meet”. The card below is invented.",
             examples=[
                 ex("أُمِّي الْعَزِيزَة،", "My dear mother,", "أُمِّي الْعَزِيزَة"),
                 ex("أَكْتُب لَكِ مِنَ الْأُقْصُر.", "I am writing to you from Luxor.", "لَكِ"),
                 ex("الْجَوّ حَارّ وَالْمَعَابِد جَمِيلَة جِدًّا.", "The weather is hot and the temples are very beautiful.", "جَمِيلَة"),
                 ex("زُرْنَا الْكَرْنَك صَبَاحًا وَسَنَرْكَب الْبَاخِرَة غَدًا.", "We visited Karnak in the morning and will take the boat tomorrow.", "سَنَرْكَب"),
                 ex("سَأُرْسِل لَكِ هَدِيَّة صَغِيرَة.", "I will send you a small present.", "سَأُرْسِل"),
                 ex("مَعَ حُبِّي، وَإِلَى اللِّقَاء.", "With my love, and until we meet.", "إِلَى اللِّقَاء"),
             ]),
    ],
    exercises=[
        M("What does أُمِّي الْعَزِيزَة mean?", "my dear mother", ["my dear father", "my dear friend", "my mother’s house"], "عَزِيز = dear."),
        M("What does لَكِ mean in أَكْتُب لَكِ?", "to you (a woman)", ["to you (a man)", "to him", "to us"], "ـكِ = you (f.)."),
        M("What does مَعَ حُبِّي mean?", "with my love", ["with my thanks", "with my apologies", "with my bag"], "حُبّ = love."),
        M("What does إِلَى اللِّقَاء mean?", "until we meet", ["good morning", "thank you", "I am sorry"], "A closing."),
        M("What does سَنَرْكَب الْبَاخِرَة غَدًا mean?", "We will take the boat tomorrow", ["We took the boat yesterday", "We sell the boat", "We do not like boats"], "سَـ = will; غَدًا = tomorrow."),
        M("Why جَمِيلَة in الْمَعَابِد جَمِيلَة?", "the plural of a thing is feminine singular", ["it is a dual", "it is a verb", "it is a man"], "Plural things → feminine singular."),
        F("أَكْتُب ___ مِنَ الْأُقْصُر.", "لَكِ", ["لَكَ", "لَهُ"], "To a woman: ـكِ.", tr="I am writing to you from Luxor."),
        F("الْجَوّ حَارّ وَالْمَعَابِد ___ جِدًّا.", "جَمِيلَة", ["جَمِيل", "جَمِيلُون"], "Plural of a thing: feminine singular.", tr="The weather is hot and the temples are very beautiful."),
        F("زُرْنَا الْكَرْنَك ___ وَسَنَرْكَب الْبَاخِرَة غَدًا.", "صَبَاحًا", ["أَمْس", "قَبْل"], "In the morning.", tr="We visited Karnak in the morning and will take the boat tomorrow."),
        F("مَعَ ___، وَإِلَى اللِّقَاء.", "حُبِّي", ["حُبِّكَ", "حُبِّهَا"], "“with my love”.", tr="With my love, and until we meet."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 415
L415 = lesson(
    "Problems at the post office",
    "الْمَكْتَب مُغْلَق · الْعُنْوَان خَطَأ · الطَّرْد ثَقِيل",
    requires=["مغلق", "مفتوح", "إغلاق", "خطأ", "عنوان", "طرد", "ثقيل", "خفيف", "غير"],
    cards=[
        card("When something goes wrong",
             "A clerk may say that the office is closed (مُغْلَق) and will open tomorrow, that the address is wrong (خَطَأ), or that the parcel is too heavy. "
             "He may then give a command with a Measure IV or II verb: أَخْرِجْ, “take out”, غَيِّرْ, “change”. Notice the accusative after يَجِب أَنْ. The lines are invented.",
             examples=[
                 ex("آسِف، الْمَكْتَب مُغْلَق الْآن.", "Sorry, the office is closed now.", "مُغْلَق"),
                 ex("يَفْتَح الْمَكْتَب غَدًا السَّاعَة الثَّامِنَة.", "The office opens tomorrow at eight.", "يَفْتَح"),
                 ex("الْعُنْوَان خَطَأ، يَجِب أَنْ تُغَيِّرَهُ.", "The address is wrong, you must change it.", "أَنْ تُغَيِّرَهُ"),
                 ex("الطَّرْد ثَقِيل جِدًّا، أَخْرِجْ بَعْض الْأَشْيَاء.", "The parcel is very heavy, take some things out.", "أَخْرِجْ"),
                 ex("لَنْ نَقْبَلَ طَرْدًا مَفْتُوحًا.", "We will not accept an open parcel.", "لَنْ نَقْبَلَ"),
                 ex("لَا بَأْس، سَأَرْجِع غَدًا.", "No problem, I will come back tomorrow.", "سَأَرْجِع"),
             ]),
    ],
    exercises=[
        M("What does الْمَكْتَب مُغْلَق mean?", "The office is closed", ["The office is open", "The office is new", "The office is far"], "مُغْلَق = closed."),
        M("What does الْعُنْوَان خَطَأ mean?", "The address is wrong", ["The address is long", "The address is new", "The address is missing"], "خَطَأ = mistake, wrong."),
        M("What does أَخْرِجْ mean?", "take out!", ["put in!", "send!", "wait!"], "Measure IV command."),
        M("What does لَنْ نَقْبَلَ mean?", "we will not accept", ["we accepted", "we are accepting", "accept!"], "لَنْ + accusative."),
        M("What does يَجِب أَنْ تُغَيِّرَهُ mean?", "you must change it", ["you changed it", "do not change it", "he changed it"], "أَنْ + accusative."),
        M("What does لَا بَأْس mean?", "no problem", ["I am sorry", "excuse me", "thank you"], "A phrase for accepting a delay."),
        F("آسِف، الْمَكْتَب ___ الْآن.", "مُغْلَق", ["مَفْتُوح", "جَدِيد"], "It is closed.", tr="Sorry, the office is closed now."),
        F("يَجِب أَنْ ___ الْعُنْوَان.", "تُغَيِّرَ", ["تُغَيِّرُ", "غَيِّرْ"], "After أَنْ: ـَ.", tr="You must change the address."),
        F("___ بَعْض الْأَشْيَاء مِنَ الطَّرْد.", "أَخْرِجْ", ["أَخْرَجَ", "يُخْرِج"], "A command from Measure IV.", tr="Take some things out of the parcel.", lemma="خرج#4:imp:anta"),
        F("لَنْ ___ طَرْدًا مَفْتُوحًا.", "نَقْبَلَ", ["نَقْبَلُ", "قَبِلْنَا"], "After لَنْ: ـَ.", tr="We will not accept an open parcel."),
    ],
    verify=(vv("خرج#4", "imp", anta="أَخْرِجْ") + vv("غير#2", "sub", anta="تُغَيِّرَ")),
)

# ---------------------------------------------------------------------------- 416
L416 = lesson(
    "Review: Egypt, moods and the post office",
    "مُرَاجَعَة الْوَحْدَة",
    requires=["هرم", "قطار", "تذكرة", "سد", "معبد", "بريد", "طرد", "كتب"],
    cards=[
        card("What to remember",
             "After أَنْ, لَنْ, كَيْ, حَتَّى and purpose لِـ the present is accusative (ـَ). After لَمْ, a command لِـ and a prohibition لَا it is jussive (ـْ). "
             "Groups lose their ن, women’s plurals keep it, and defective verbs show ـَ on their last ي or و. Egypt’s sites, trains, ships and the post office give the vocabulary.",
             tables=[table(["Particle", "Example", "Mood"],
                           [["أَنْ", "أَنْ أَكْتُبَ", "accusative"], ["لَنْ", "لَنْ يَصِلَ", "accusative"], ["لَمْ", "لَمْ يَصِلْ", "jussive"], ["لِ", "لِنَذْهَبْ", "jussive (command)"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
    ],
    exercises=[
        M("What is a هَرَم?", "a pyramid", ["a dam", "a ship", "a stamp"], "هَرَم = pyramid."),
        M("What does ذَهَاب وَعَوْدَة mean?", "return", ["one way", "second class", "a seat"], "A return ticket."),
        M("What does السَّدّ الْعَالِي give?", "electricity", ["bread", "mail", "fish"], "كَهْرَبَاء."),
        M("Which is the accusative of يَمْشِي after أَنْ?", "أَنْ يَمْشِيَ", ["أَنْ يَمْشِي", "أَنْ يَمْشُوا", "أَنْ يَمْشِينَ"], "ـَ on the last ي."),
        M("What does لِنَذْهَبْ mean?", "let us go", ["we went", "we will go", "do not go"], "لِـ + jussive."),
        M("What is a بَرِيد جَوِّيّ?", "air mail", ["a postcard", "a stamp", "a parcel"], "جَوّ = air."),
        F("أُرِيد أَنْ ___ تَذْكِرَتَيْن.", "أَحْجِزَ", ["أَحْجِزُ", "أَحْجِزْ"], "After أَنْ: ـَ.", tr="I want to book two tickets."),
        F("لَمْ ___ الْقِطَار أَمْس.", "يَصِلِ", ["يَصِلَ", "يَصِلُ"], "After لَمْ: ـْ (a helping kasra before الـ).", tr="The train did not arrive yesterday."),
        F("يُرِيد السُّيَّاح أَنْ ___ السَّدّ.", "يَزُورُوا", ["يَزُورُونَ", "يَزُورَ"], "A group after أَنْ: no ن.", tr="The tourists want to visit the dam."),
        F("اِذْهَبْ إِلَى الْكَرْنَك ___.", "صَبَاحًا", ["أَمْس", "قَبْل"], "In the morning.", tr="Go to Karnak in the morning."),
        F("كَمْ ___ هَذَا الطَّرْد؟", "وَزْن", ["جِسْر", "قُبَّة"], "How much does this parcel weigh?", tr="How much does this parcel weigh?"),
        F("اُكْتُبِي ___ عَلَى الطَّرْد.", "الْعُنْوَان", ["الرَّصِيف", "السَّطْح"], "Write the address on the parcel.", tr="Write the address on the parcel."),
    ],
    verify=(),
)


UNIT = unit("جَوْلَة فِي مِصْر: Egypt, the subjunctive, the jussive and the post office", [L395, L396, L397, L398, L399, L400, L401, L402, L403, L404, L405, L406, L407, L408, L409, L410, L411, L412, L413, L414, L415, L416])
