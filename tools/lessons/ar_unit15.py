"""Unit 15: landforms, directions on the map, climate, time zones, TV programmes, “still” (مَا زَالَ) and Measure V verbs (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 215
L215 = lesson(
    "Landforms: mountains, valleys, lakes",
    "جَبَل · وَادِي · سَهْل · صَحْرَاء · بُحَيْرَة · غَابَة · سَاحِل",
    requires=["جبل", "سلسلة", "قمة", "تل", "وادي", "سهل", "صحراء", "بحيرة", "نهر", "غابة", "جزيرة", "ساحل", "بحر", "محيط"],
    cards=[
        card("The shape of the land",
             "Geography begins with the words for the land. The plural of جَبَل is جِبَال, and a line of mountains is a "
             "سِلْسِلَة جِبَال (an iḍāfa: “a chain of mountains”). The top of a mountain is a قِمَّة.",
             tables=[table(["English", "Arabic"],
                           [["mountain", "جَبَل"], ["mountains", "جِبَال"], ["mountain range", "سِلْسِلَة جِبَال"], ["peak, summit", "قِمَّة"],
                            ["hill", "تَلّ"], ["valley", "وَادِي"], ["plain", "سَهْل"], ["desert", "صَحْرَاء"], ["lake", "بُحَيْرَة"],
                            ["river", "نَهْر"], ["forest", "غَابَة"], ["island", "جَزِيرَة"], ["coast", "سَاحِل"], ["sea", "بَحْر"], ["ocean", "مُحِيط"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Describing a landscape",
             "Use the nominal sentence and adjectives you know. A plural of things (not people) takes a feminine singular adjective: "
             "جِبَال عَالِيَة (“high mountains”).",
             examples=[
                 ex("فِي الْغَرْب سِلْسِلَة جِبَال عَالِيَة.", "In the west there is a high mountain range.", "سِلْسِلَة جِبَال"),
                 ex("عَلَى قِمَّة الْجَبَل ثَلْج كَثِير.", "On the mountain top there is a lot of snow.", "قِمَّة"),
                 ex("بُحَيْرَة كَبِيرَة فِي وَسَط الْغَابَة.", "A big lake is in the middle of the forest.", "بُحَيْرَة"),
                 ex("يَمُرّ نَهْر طَوِيل فِي السَّهْل.", "A long river runs through the plain.", "نَهْر"),
                 ex("عَلَى السَّاحِل شَوَاطِئ جَمِيلَة.", "On the coast there are beautiful beaches.", "السَّاحِل"),
                 ex("الصَّحْرَاء وَاسِعَة وَجَافَّة.", "The desert is wide and dry.", "الصَّحْرَاء"),
             ]),
    ],
    exercises=[
        M("What is the plural of جَبَل?", "جِبَال", ["جَبَلَات", "جَبَلُون", "أَجْبَل"], "A broken plural."),
        M("What does سِلْسِلَة جِبَال mean?", "mountain range", ["mountain peak", "mountain valley", "mountain village"], "سِلْسِلَة = chain."),
        M("Which word means “lake”?", "بُحَيْرَة", ["بَحْر", "نَهْر", "جَزِيرَة"], "بُحَيْرَة = a small sea."),
        M("Which word means “valley”?", "وَادِي", ["تَلّ", "سَهْل", "قِمَّة"], "وَادِي = valley."),
        M("Which means “On the coast there are beautiful beaches”?", "عَلَى السَّاحِل شَوَاطِئ جَمِيلَة", ["فِي الْغَابَة شَوَاطِئ جَمِيلَة", "عَلَى الْجَبَل شَوَاطِئ جَمِيلَة", "عَلَى السَّاحِل جِبَال جَمِيلَة"], "سَاحِل = coast."),
        M("Why is it جِبَال عَالِيَة, with a feminine adjective?", "plural things take a feminine singular adjective", ["جَبَل is feminine", "عَالِيَة is a noun", "the adjective is dual"], "A plural of things behaves like a feminine singular."),
        F("الصَّحْرَاء وَاسِعَة وَ___.", "جَافَّة", ["جَافّ", "جَافُّون", "جَافَّات"], "Feminine singular for صَحْرَاء.", tr="The desert is wide and dry."),
        F("بُحَيْرَة كَبِيرَة فِي وَسَط ___.", "الْغَابَة", ["الْغَابَةُ", "غَابَة", "الْجَبَلَات"], "In the middle of the forest.", tr="A big lake is in the middle of the forest."),
        F("فِي الْغَرْب ___ جِبَال عَالِيَة.", "سِلْسِلَة", ["سِلْسِلَةً", "السِّلْسِلَة", "سَلَاسِل"], "Range = iḍāfa, first noun without ال.", tr="In the west there is a high mountain range."),
    ],
    verify=(vf("جَاف", "جَافَّة") if False else [])
    + vw("جَبَل", "جِبَال", "سِلْسِلَة", "قِمَّة", "تَلّ", "وَادِي", "سَهْل", "صَحْرَاء", "بُحَيْرَة", "نَهْر", "غَابَة", "جَزِيرَة", "سَاحِل", "بَحْر", "مُحِيط",
         "عَالِيَة", "جَافَّة", "وَاسِعَة", "شَوَاطِئ", "ثَلْج", "يَمُرّ", "الْغَابَة"),
)

# ---------------------------------------------------------------------------- 216
L216 = lesson(
    "Where is it? تَقَع · تَمْتَدّ · تَشْتَهِر",
    "تَقَع الْمَدِينَة عَلَى السَّاحِل · تَمْتَدّ الْجِبَال",
    requires=["ساحل", "جبل", "مدينة", "منطقة", "بحر", "شمال", "جنوب"],
    cards=[
        card("Four verbs for a geography text",
             "A text about a place uses a few verbs again and again. They are mostly in the “she” form, because the subject is "
             "usually a feminine noun (مَدِينَة, مِنْطَقَة, جَزِيرَة, سِلْسِلَة). For a masculine subject, use يَـ.",
             tables=[table(["English", "She", "He"],
                           [["is located", "تَقَع", "يَقَع"], ["extends, stretches", "تَمْتَدّ", "يَمْتَدّ"], ["is famous for", "تَشْتَهِر بِ", "يَشْتَهِر بِ"],
                            ["borders", "تَحُدّ", "يَحُدّ"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("A paragraph about a place",
             "These are invented sentences for practice. Read them aloud and notice the preposition after each verb.",
             examples=[
                 ex("تَقَع الْمَدِينَة عَلَى سَاحِل الْبَحْر.", "The city is located on the sea coast.", "تَقَع"),
                 ex("تَمْتَدّ الْجِبَال مِنَ الشَّمَال إِلَى الْجَنُوب.", "The mountains extend from north to south.", "تَمْتَدّ"),
                 ex("تَشْتَهِر الْمِنْطَقَة بِالْبُحَيْرَات.", "The region is famous for its lakes.", "تَشْتَهِر"),
                 ex("يَحُدّ الْبَحْر الْبَلَد مِنَ الْغَرْب.", "The sea borders the country on the west.", "يَحُدّ"),
                 ex("يَقَع الْمَتْحَف قَرِيبًا مِنَ النَّهْر.", "The museum is located near the river.", "يَقَع"),
                 ex("تَتَمَيَّز الْجَزِيرَة بِالشَّوَاطِئ الْجَمِيلَة.", "The island is distinguished by its beautiful beaches.", "تَتَمَيَّز"),
             ]),
    ],
    exercises=[
        M("Which means “is located” (she)?", "تَقَع", ["تَمْتَدّ", "تَشْتَهِر", "تَحُدّ"], "تَقَع = lies."),
        M("Which means “extends” (she)?", "تَمْتَدّ", ["تَقَع", "تَحُدّ", "تَشْتَهِر"], "مَدَّ → تَمْتَدّ."),
        M("Which preposition goes with تَشْتَهِر?", "بِـ", ["فِي", "عَنْ", "إِلَى"], "تَشْتَهِر بِـ = is famous for."),
        M("Which means “The mountains extend from north to south”?", "تَمْتَدّ الْجِبَال مِنَ الشَّمَال إِلَى الْجَنُوب", ["تَقَع الْجِبَال مِنَ الشَّمَال إِلَى الْجَنُوب", "تَحُدّ الْجِبَال الشَّمَال وَالْجَنُوب", "تَمْتَدّ الْجِبَال مِنَ الْجَنُوب إِلَى الشَّمَال"], "مِنْ … إِلَى …"),
        M("Why تَقَع and not يَقَع in تَقَع الْمَدِينَة?", "مَدِينَة is feminine", ["مَدِينَة is plural", "it is the past", "it is a question"], "A feminine subject takes the تَـ form."),
        M("Which means “The sea borders the country on the west”?", "يَحُدّ الْبَحْر الْبَلَد مِنَ الْغَرْب", ["يَحُدّ الْبَلَد الْبَحْر مِنَ الْغَرْب", "يَحُدّ الْبَحْر الْبَلَد مِنَ الشَّرْق", "تَقَع الْبَحْر مِنَ الْغَرْب"], "غَرْب = west."),
        F("___ الْمَدِينَة عَلَى سَاحِل الْبَحْر.", "تَقَع", ["يَقَع", "تَمْتَدّ", "تَحُدّ"], "Is located.", tr="The city is located on the sea coast."),
        F("تَشْتَهِر الْمِنْطَقَة ___ الْبُحَيْرَات.", "بِ", ["فِي", "عَنِ", "مِنَ"], "Famous for.", tr="The region is famous for its lakes."),
        F("___ الْمَتْحَف قَرِيبًا مِنَ النَّهْر.", "يَقَع", ["تَقَع", "تَمْتَدّ", "نَقَع"], "مَتْحَف is masculine.", tr="The museum is located near the river."),
    ],
    verify=vw("تَقَع", "يَقَع", "تَمْتَدّ", "يَمْتَدّ", "تَشْتَهِر", "يَشْتَهِر", "تَحُدّ", "يَحُدّ", "الْمَدِينَة", "الْجِبَال", "الشَّمَال", "الْجَنُوب", "الْبُحَيْرَات", "الْمَتْحَف", "قَرِيبًا", "الْغَرْب", "الشَّوَاطِئ")
    + vw("تَتَمَيَّز", "الْمِنْطَقَة"),
)

# ---------------------------------------------------------------------------- 217
L217 = lesson(
    "North, south, east, west",
    "شَمَال · جَنُوب · شَرْق · غَرْب · الْبَوْصَلَة",
    requires=["شمال", "جنوب", "غرب", "وسط", "ساحل", "خريطة"],
    cards=[
        card("The four directions",
             "Each direction has a noun and an adjective (ending in ـِيّ, like the nationality words). Use the noun after فِي or مِنْ and the "
             "adjective after a noun: فِي شَمَال الْبَلَد (“in the north of the country”), السَّاحِل الشَّرْقِيّ (“the eastern coast”).",
             tables=[table(["English", "Noun", "Adjective (m.)", "Adjective (f.)"],
                           [["north", "شَمَال", "شَمَالِيّ", "شَمَالِيَّة"], ["south", "جَنُوب", "جَنُوبِيّ", "جَنُوبِيَّة"],
                            ["east", "شَرْق", "شَرْقِيّ", "شَرْقِيَّة"], ["west", "غَرْب", "غَرْبِيّ", "غَرْبِيَّة"],
                            ["middle", "وَسَط", "أَوْسَط", "وُسْطَى"]],
                           say=[1, 2, 3], tlit=[1, 2], gloss=False)]),
        card("On the map",
             "To say a place lies in a direction from another, use فِي شَمَال / جَنُوب / شَرْق / غَرْب + the place. For a compass, "
             "the word is بَوْصَلَة.",
             examples=[
                 ex("تَقَع الْمَدِينَة فِي شَمَال الْبَلَد.", "The city is in the north of the country.", "فِي شَمَال"),
                 ex("الْجِبَال فِي الْغَرْب وَالْبَحْر فِي الشَّرْق.", "The mountains are in the west and the sea is in the east.", "الْغَرْب"),
                 ex("تَقَع الْمَدِينَة عَلَى السَّاحِل الْغَرْبِيّ.", "The city is on the western coast.", "الْغَرْبِيّ"),
                 ex("الشَّمْس تَطْلُع مِنَ الشَّرْق وَتَغْرُب فِي الْغَرْب.", "The sun rises in the east and sets in the west.", "الشَّرْق"),
                 ex("نَسْتَخْدِم الْبَوْصَلَة لِمَعْرِفَة الِاتِّجَاه.", "We use the compass to know the direction.", "الْبَوْصَلَة"),
                 ex("الْمَدِينَة الْجَنُوبِيَّة أَكْبَر مِنَ الْمَدِينَة الشَّمَالِيَّة.", "The southern city is bigger than the northern city.", "الْجَنُوبِيَّة"),
             ]),
    ],
    exercises=[
        M("Which word means “east”?", "شَرْق", ["غَرْب", "شَمَال", "جَنُوب"], "شَرْق = east."),
        M("Which word means “south”?", "جَنُوب", ["شَمَال", "وَسَط", "غَرْب"], "جَنُوب = south."),
        M("Which means “the western coast”?", "السَّاحِل الْغَرْبِيّ", ["السَّاحِل الشَّرْقِيّ", "الْغَرْب السَّاحِل", "سَاحِل الْجَنُوبِيّ"], "غَرْبِيّ = western."),
        M("Where does the sun rise?", "مِنَ الشَّرْق", ["مِنَ الْغَرْب", "مِنَ الشَّمَال", "مِنَ الْجَنُوب"], "The sun rises in the east."),
        M("Which is the feminine of شَمَالِيّ?", "شَمَالِيَّة", ["شَمَالِيَّات", "شَمَالِيُّون", "شَمَالِيَّتَان"], "ـِيَّة for the feminine."),
        M("What does بَوْصَلَة mean?", "compass", ["map", "road", "valley"], "بَوْصَلَة = compass."),
        F("تَقَع الْمَدِينَة فِي ___ الْبَلَد.", "شَمَال", ["الشَّمَال", "شَمَالِيّ", "الشَّمَالِيّ"], "An iḍāfa: no ال on the first noun.", tr="The city is in the north of the country."),
        F("الْمَدِينَة ___ أَكْبَر مِنَ الْمَدِينَة الشَّمَالِيَّة.", "الْجَنُوبِيَّة", ["الْجَنُوبِيّ", "الْجَنُوب", "جَنُوبِيَّات"], "Feminine, with ال.", tr="The southern city is bigger than the northern city."),
        F("الشَّمْس تَطْلُع مِنَ ___.", "الشَّرْق", ["الْغَرْب", "الْبَوْصَلَة", "الْوَسَط"], "East.", tr="The sun rises in the east.", ),
    ],
    verify=(vf("شَمَالِيّ", "شَمَالِيَّة") + vf("جَنُوبِيّ", "جَنُوبِيَّة") + vf("شَرْقِيّ", "شَرْقِيَّة") + vf("غَرْبِيّ", "غَرْبِيَّة")
            + vv("طلع", "pres", hiya="تَطْلُع")
            + vw("شَمَال", "جَنُوب", "شَرْق", "غَرْب", "الْغَرْبِيّ", "الشَّمَالِيَّة", "الْجَنُوبِيَّة", "بَوْصَلَة", "الْبَوْصَلَة", "أَوْسَط", "وُسْطَى", "وَسَط", "تَغْرُب", "نَسْتَخْدِم", "لِمَعْرِفَة", "الِاتِّجَاه")),
)

# ---------------------------------------------------------------------------- 218
L218 = lesson(
    "Climate and the seasons",
    "حَارّ · بَارِد · مُعْتَدِل · جَاف · رَطْب · مُمْطِر",
    requires=["مناخ", "طقس", "حار", "بارد", "معتدل", "دافئ", "جاف", "رطب", "صيف", "شتاء", "خريف", "مطر", "ثلج", "فصل"],
    cards=[
        card("Words for the weather",
             "مُنَاخ is the climate of a place and طَقْس is the weather of a day. Most weather words are adjectives. The names of "
             "the four seasons are nouns.",
             tables=[table(["English", "Arabic"],
                           [["hot", "حَارّ"], ["cold", "بَارِد"], ["mild, moderate", "مُعْتَدِل"], ["warm", "دَافِئ"], ["dry", "جَاف"],
                            ["humid", "رَطْب"], ["rainy", "مُمْطِر"], ["tropical", "اِسْتِوَائِيّ"], ["desert-like", "صَحْرَاوِيّ"]],
                           say=[1], tlit=[1], gloss=False),
                    table(["English", "Arabic"],
                          [["summer", "الصَّيْف"], ["winter", "الشِّتَاء"], ["spring", "الرَّبِيع"], ["autumn", "الْخَرِيف"],
                           ["rain", "مَطَر"], ["snow", "ثَلْج"], ["wind(s)", "رِيَاح"], ["heat", "حَرَارَة"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("Talking about the climate",
             "The climate and the weather are masculine, so their adjectives are masculine. Rain and snow are said with يَسْقُط "
             "(“falls”): يَسْقُط الثَّلْج, يَسْقُط الْمَطَر.",
             examples=[
                 ex("مُنَاخ الْمِنْطَقَة مُعْتَدِل.", "The climate of the region is mild.", "مُعْتَدِل"),
                 ex("الصَّيْف حَارّ وَجَاف فِي الصَّحْرَاء.", "The summer is hot and dry in the desert.", "حَارّ وَجَاف"),
                 ex("فِي الشِّتَاء يَسْقُط الثَّلْج عَلَى الْجِبَال.", "In winter snow falls on the mountains.", "يَسْقُط"),
                 ex("الطَّقْس الْيَوْم دَافِئ وَمُمْطِر.", "The weather today is warm and rainy.", "دَافِئ"),
                 ex("الْمُنَاخ فِي الْجَزِيرَة اِسْتِوَائِيّ وَرَطْب.", "The climate on the island is tropical and humid.", "اِسْتِوَائِيّ"),
                 ex("الرَّبِيع جَمِيل فِي الْغَابَة.", "Spring is beautiful in the forest.", "الرَّبِيع"),
             ]),
    ],
    exercises=[
        M("Which word means “humid”?", "رَطْب", ["جَاف", "بَارِد", "دَافِئ"], "رَطْب = damp, humid."),
        M("Which word means “mild”?", "مُعْتَدِل", ["حَارّ", "جَاف", "مُمْطِر"], "مُعْتَدِل = moderate."),
        M("Which word means “autumn”?", "الْخَرِيف", ["الرَّبِيع", "الصَّيْف", "الشِّتَاء"], "خَرِيف = autumn."),
        M("What does يَسْقُط الثَّلْج mean?", "snow falls", ["snow melts", "rain falls", "the wind blows"], "سَقَطَ = to fall."),
        M("Which means “The climate of the region is mild”?", "مُنَاخ الْمِنْطَقَة مُعْتَدِل", ["مُنَاخ الْمِنْطَقَة مُعْتَدِلَة", "طَقْس الْمِنْطَقَة جَاف", "مُنَاخ الْمِنْطَقَة مُمْطِرُون"], "مُنَاخ is masculine."),
        M("Which means “tropical”?", "اِسْتِوَائِيّ", ["صَحْرَاوِيّ", "شَمَالِيّ", "مُعْتَدِل"], "اِسْتِوَائِيّ = tropical."),
        F("الصَّيْف حَارّ وَ___ فِي الصَّحْرَاء.", "جَاف", ["جَافَّة", "جَافُّون", "الْجَاف"], "Masculine: الصَّيْف.", tr="The summer is hot and dry in the desert."),
        F("فِي الشِّتَاء ___ الثَّلْج عَلَى الْجِبَال.", "يَسْقُط", ["تَسْقُط", "سَقَطَتْ", "نَسْقُط"], "Snow is masculine here.", tr="In winter snow falls on the mountains.", lemma="سقط:pres:huwa"),
        F("الطَّقْس الْيَوْم دَافِئ وَ___.", "مُمْطِر", ["مُمْطِرَة", "مَطَر", "مُمْطِرُون"], "Masculine.", tr="The weather today is warm and rainy."),
    ],
    verify=(vv("سقط", "pres", huwa="يَسْقُط", hiya="تَسْقُط")
            + vw("مُنَاخ", "طَقْس", "حَارّ", "بَارِد", "مُعْتَدِل", "دَافِئ", "جَاف", "رَطْب", "مُمْطِر", "اِسْتِوَائِيّ", "صَحْرَاوِيّ", "الصَّيْف", "الشِّتَاء", "الرَّبِيع", "الْخَرِيف",
                 "مَطَر", "ثَلْج", "رِيَاح", "حَرَارَة", "الْمِنْطَقَة", "الْغَابَة", "الْجَزِيرَة", "جَمِيل")),
)

# ---------------------------------------------------------------------------- 219
L219 = lesson(
    "A weather report",
    "الطَّقْس غَدًا · دَرَجَة الْحَرَارَة · الرِّيَاح قَوِيَّة",
    requires=["طقس", "حرارة", "درجة", "قوي", "أحسن", "غد"],
    cards=[
        card("Comparing weather",
             "Weather reports compare days and regions. Use the patterns you know: أَفْعَل + مِنْ. Warm: دَافِئ → أَدْفَأ; "
             "cold: بَارِد → أَبْرَد; hot: حَارّ → أَحَرّ (two identical letters join). Two comparatives come from other words: أَعْلَى (higher) and أَقَلّ (lower, less).",
             tables=[table(["English", "Adjective", "Comparative"],
                           [["hot", "حَارّ", "أَحَرّ"], ["cold", "بَارِد", "أَبْرَد"], ["warm", "دَافِئ", "أَدْفَأ"],
                            ["strong", "قَوِيّ", "أَقْوَى"], ["high", "مُرْتَفِع", "أَعْلَى"], ["low", "مُنْخَفِض", "أَقَلّ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("An invented weather report",
             "Read this short report. The place names are left out so you can apply it to any country.",
             examples=[
                 ex("الطَّقْس الْيَوْم فِي الشَّمَال بَارِد وَمُمْطِر.", "The weather today in the north is cold and rainy.", "بَارِد وَمُمْطِر"),
                 ex("فِي الْجَنُوب الْجَوّ أَدْفَأ مِنْهُ فِي الشَّمَال.", "In the south the weather is warmer than in the north.", "أَدْفَأ"),
                 ex("فِي الشَّرْق رِيَاح قَوِيَّة عَلَى السَّاحِل.", "In the east there are strong winds on the coast.", "رِيَاح قَوِيَّة"),
                 ex("دَرَجَة الْحَرَارَة مُنْخَفِضَة فِي الْجِبَال.", "The temperature is low in the mountains.", "دَرَجَة الْحَرَارَة"),
                 ex("يَخْتَلِف الْمُنَاخ حَسَب الْمِنْطَقَة.", "The climate differs according to the region.", "يَخْتَلِف"),
                 ex("غَدًا سَيَكُون الطَّقْس أَحْسَن.", "Tomorrow the weather will be better.", "سَيَكُون"),
             ]),
    ],
    exercises=[
        M("Which is the comparative of بَارِد?", "أَبْرَد", ["أَبْرَدَة", "بُرْدَى", "مُبَرَّد"], "ب-ر-د → أَبْرَد."),
        M("Which is the comparative of حَارّ?", "أَحَرّ", ["أَحْرَر", "حَرْرَى", "حَارَّة"], "Two identical letters join."),
        M("Which is the comparative of دَافِئ?", "أَدْفَأ", ["أَدْفَئ", "دُفْأَى", "دَافِئَة"], "د-ف-ء → أَدْفَأ."),
        M("What does دَرَجَة الْحَرَارَة mean?", "temperature", ["rainfall", "wind speed", "season"], "حَرَارَة = heat."),
        M("Which means “Tomorrow the weather will be better”?", "غَدًا سَيَكُون الطَّقْس أَحْسَن", ["غَدًا كَانَ الطَّقْس أَحْسَن", "غَدًا لَنْ يَكُون الطَّقْس أَحْسَن", "أَمْس سَيَكُون الطَّقْس أَحْسَن"], "سَـ + present = will."),
        M("What does يَخْتَلِف الْمُنَاخ حَسَب الْمِنْطَقَة mean?", "the climate differs by region", ["the climate is the same everywhere", "the region has no climate", "the climate changed yesterday"], "يَخْتَلِف = differs."),
        F("فِي الْجَنُوب الْجَوّ ___ مِنْهُ فِي الشَّمَال.", "أَدْفَأ", ["دَافِئ", "دَافِئَة", "أَدْفَأَة"], "Warmer than.", tr="In the south the weather is warmer than in the north."),
        F("فِي الشَّرْق رِيَاح ___ عَلَى السَّاحِل.", "قَوِيَّة", ["قَوِيّ", "قَوِيُّون", "أَقْوَى"], "Plural of things: feminine singular.", tr="In the east there are strong winds on the coast."),
        F("غَدًا ___ الطَّقْس أَحْسَن.", "سَيَكُون", ["كَانَ", "تَكُون", "كُنْ"], "Will be.", tr="Tomorrow the weather will be better."),
    ],
    verify=(vv("كون", "pres", huwa="يَكُون") + vf("قَوِيّ", "قَوِيَّة")
            + vw("أَحَرّ", "أَبْرَد", "أَدْفَأ", "أَقْوَى", "أَعْلَى", "مُرْتَفِع", "مُنْخَفِض", "مُنْخَفِضَة", "الْحَرَارَة", "دَرَجَة", "رِيَاح", "قَوِيَّة", "يَخْتَلِف", "حَسَب", "أَحْسَن", "الْجَوّ", "غَدًا", "سَيَكُون")),
)


# ---------------------------------------------------------------------------- 220
L220 = lesson(
    "Time zones",
    "مِنْطَقَة زَمَنِيَّة · فَرْق التَّوْقِيت · هُنَا الْعَاشِرَة وَعِنْدَكُمُ السَّابِعَة",
    requires=["توقيت", "منطقة", "فرق", "ساعة", "هنا", "عند", "بين"],
    cards=[
        card("When it is ten here…",
             "A large country has more than one time zone (مِنْطَقَة زَمَنِيَّة). The difference between two zones is the فَرْق التَّوْقِيت. "
             "To compare clocks, use عِنْدَ with an ending: عِنْدَنَا (“at our place”), عِنْدَكُمْ (“at your place”).",
             tables=[table(["English", "Arabic"],
                           [["time zone", "مِنْطَقَة زَمَنِيَّة"], ["time (of day), standard time", "تَوْقِيت"], ["difference", "فَرْق"],
                            ["the time difference", "فَرْق التَّوْقِيت"], ["at our place", "عِنْدَنَا"], ["at your place (plural)", "عِنْدَكُمْ"],
                            ["there", "هُنَاكَ"], ["here", "هُنَا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Comparing the clocks",
             "These sentences are invented for practice. Practise them with other numbers.",
             examples=[
                 ex("الْبِلَاد الْكَبِيرَة فِيهَا أَكْثَر مِنْ مِنْطَقَة زَمَنِيَّة.", "Large countries have more than one time zone.", "مِنْطَقَة زَمَنِيَّة"),
                 ex("فَرْق التَّوْقِيت بَيْنَ الْمَدِينَتَيْن ثَلَاث سَاعَات.", "The time difference between the two cities is three hours.", "فَرْق التَّوْقِيت"),
                 ex("هُنَا الْعَاشِرَة وَعِنْدَكُمُ السَّابِعَة.", "Here it is ten and at your place it is seven.", "عِنْدَكُمُ"),
                 ex("تَتْبَع الْمَدِينَة تَوْقِيت السَّاحِل الْغَرْبِيّ.", "The city follows the time of the western coast.", "تَتْبَع"),
                 ex("لِذَلِكَ أَتَّصِل بِكَ فِي التَّاسِعَة مَسَاءً.", "That is why I call you at nine in the evening.", "أَتَّصِل"),
                 ex("لَا تَنْسَ فَرْق التَّوْقِيت.", "Do not forget the time difference.", "لَا تَنْسَ"),
             ]),
    ],
    exercises=[
        M("What does فَرْق التَّوْقِيت mean?", "the time difference", ["the time zone", "the weather", "the season"], "فَرْق = difference."),
        M("Which means “time zone”?", "مِنْطَقَة زَمَنِيَّة", ["فَرْق زَمَنِيّ", "تَوْقِيت وَاحِد", "مِنْطَقَة جَافَّة"], "زَمَن = time."),
        M("What does عِنْدَكُمُ السَّابِعَة mean?", "at your place it is seven", ["at our place it is seven", "in seven days", "seven of you"], "عِنْدَكُمْ = at your (pl.) place."),
        M("Which means “Do not forget the time difference”?", "لَا تَنْسَ فَرْق التَّوْقِيت", ["نَسِيتُ فَرْق التَّوْقِيت", "تَنْسَى فَرْق التَّوْقِيت", "فَرْق التَّوْقِيت كَبِير"], "لَا + short present."),
        M("Which means “Here it is ten and at your place it is seven”?", "هُنَا الْعَاشِرَة وَعِنْدَكُمُ السَّابِعَة", ["هُنَاكَ الْعَاشِرَة وَعِنْدَنَا السَّابِعَة", "هُنَا السَّابِعَة وَعِنْدَكُمْ الْعَاشِرَة", "هُنَا الْعَاشِرَة وَهُنَاكَ الْعَاشِرَة"], "هُنَا = here."),
        M("Which means “three hours” (the noun is feminine)?", "ثَلَاث سَاعَات", ["ثَلَاثَة سَاعَات", "سَاعَتَيْن", "ثَالِثَة سَاعَة"], "Opposite gender."),
        F("فَرْق التَّوْقِيت بَيْنَ الْمَدِينَتَيْن ___ سَاعَات.", "ثَلَاث", ["ثَلَاثَة", "ثَالِث", "سَاعَتَيْن"], "سَاعَة is feminine.", tr="The time difference between the two cities is three hours."),
        F("هُنَا الْعَاشِرَة وَ___ السَّابِعَة.", "عِنْدَكُمُ", ["عِنْدَنَا", "عِنْدِي", "عِنْدَهُ"], "Your (pl.) place.", tr="Here it is ten and at your place it is seven."),
        F("لِذَلِكَ ___ بِكَ فِي التَّاسِعَة مَسَاءً.", "أَتَّصِل", ["أَتَّصِلُ بِ", "اِتَّصَلَ", "نَتَّصِل"], "I call you.", tr="That is why I call you at nine in the evening."),
    ],
    verify=(vn(3, "f", "ثَلَاث")
            + vw("مِنْطَقَة", "زَمَنِيَّة", "تَوْقِيت", "فَرْق", "عِنْدَنَا", "عِنْدَكُمْ", "هُنَاكَ", "هُنَا", "بَيْنَ", "الْمَدِينَتَيْن", "تَتْبَع", "لِذَلِكَ", "أَتَّصِل", "تَنْسَ",
                 "السَّابِعَة", "الْعَاشِرَة", "التَّاسِعَة", "الْغَرْبِيّ")),
)

# ---------------------------------------------------------------------------- 221
L221 = lesson(
    "A phone call across the time zones",
    "هَلِ اِتَّصَلْتَ بِصَدِيقِنَا؟ · نَسِيتُ فَرْق التَّوْقِيت",
    requires=["فرق", "نسي", "غد", "صباح", "مساء", "بعد", "لكن"],
    cards=[
        card("Calling a friend",
             "Calling someone is اِتَّصَلَ بِـ (past) and يَتَّصِل بِـ (present). The person you call comes after بِـ with an ending: "
             "بِهِ (him), بِكَ (you). Read the conversation below. It is invented for practice.",
             tables=[table(["English", "Arabic"],
                           [["I called", "اِتَّصَلْتُ"], ["I call", "أَتَّصِل"], ["call! (to a man)", "اِتَّصِلْ"], ["I forgot", "نَسِيتُ"],
                            ["him", "بِهِ"], ["you (m.)", "بِكَ"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("هَلِ اِتَّصَلْتَ بِصَدِيقِنَا خَالِد؟", "Did you call our friend Khalid?", "اِتَّصَلْتَ"),
                 ex("لَا، سَأَتَّصِل بِهِ فِي التَّاسِعَة مَسَاءً.", "No, I will call him at nine in the evening.", "سَأَتَّصِل"),
                 ex("لَكِنَّ الْوَقْت الْآن الْعَاشِرَة هُنَاكَ.", "But the time there is now ten.", "هُنَاكَ"),
                 ex("آه، نَسِيتُ فَرْق التَّوْقِيت.", "Ah, I forgot the time difference.", "نَسِيتُ"),
                 ex("إِذَنْ اِتَّصِلْ بِهِ غَدًا فِي الصَّبَاح.", "Then call him tomorrow morning.", "اِتَّصِلْ"),
                 ex("حَسَنًا، شُكْرًا عَلَى التَّذْكِير.", "Fine, thanks for the reminder.", "التَّذْكِير"),
             ]),
    ],
    exercises=[
        M("Which means “I will call him”?", "سَأَتَّصِل بِهِ", ["اِتَّصَلْتُ بِهِ", "أَتَّصِل بِكَ", "سَيَتَّصِل بِي"], "سَـ + present, بِهِ = him."),
        M("Which means “Did you call our friend?” (to a man)", "هَلِ اِتَّصَلْتَ بِصَدِيقِنَا؟", ["هَلِ اِتَّصَلْتِ بِصَدِيقِنَا؟", "هَلِ اِتَّصَلْتُ بِصَدِيقِنَا؟", "هَلْ يَتَّصِل بِصَدِيقِنَا؟"], "ـتَ = you (m.)."),
        M("What does نَسِيتُ mean?", "I forgot", ["I called", "I remembered", "I slept"], "نَسِيَ = to forget."),
        M("Which means “Call him tomorrow morning”? (to a man)", "اِتَّصِلْ بِهِ غَدًا فِي الصَّبَاح", ["اِتَّصَلَ بِهِ غَدًا فِي الصَّبَاح", "اِتَّصِلِي بِهِ غَدًا فِي الصَّبَاح", "لَا تَتَّصِلْ بِهِ"], "A command to a man."),
        M("Why does the speaker decide to call tomorrow morning instead?", "because of the time difference", ["because the friend is travelling", "because of the weather", "because the phone is broken"], "فَرْق التَّوْقِيت."),
        M("Which means “But the time there is now ten”?", "لَكِنَّ الْوَقْت الْآن الْعَاشِرَة هُنَاكَ", ["لَكِنَّ الْوَقْت الْآن الْعَاشِرَة هُنَا", "وَالْوَقْت الْآن الْعَاشِرَة هُنَاكَ", "لَكِنَّ الْوَقْت الْعَاشِرَة أَمْس"], "هُنَاكَ = there."),
        F("هَلِ ___ بِصَدِيقِنَا خَالِد؟", "اِتَّصَلْتَ", ["اِتَّصَلْتِ", "اِتَّصَلْتُ", "اِتَّصَلُوا"], "To a man.", tr="Did you call our friend Khalid?"),
        F("آه، ___ فَرْق التَّوْقِيت.", "نَسِيتُ", ["نَسِيَ", "تَنْسَى", "اُنْسَ"], "I forgot.", tr="Ah, I forgot the time difference."),
        F("إِذَنْ ___ بِهِ غَدًا فِي الصَّبَاح.", "اِتَّصِلْ", ["اِتَّصَلَ", "أَتَّصِل", "يَتَّصِل"], "Command.", tr="Then call him tomorrow morning."),
    ],
    verify=vw("اِتَّصَلْتَ", "اِتَّصَلْتُ", "اِتَّصَلْتِ", "أَتَّصِل", "سَأَتَّصِل", "يَتَّصِل", "اِتَّصِلْ", "نَسِيتُ", "لَكِنَّ", "إِذَنْ", "هُنَاكَ", "التَّذْكِير", "حَسَنًا", "بِصَدِيقِنَا", "غَدًا"),
)

# ---------------------------------------------------------------------------- 222
L222 = lesson(
    "Television programmes",
    "بَرْنَامَج وَثَائِقِيّ · نَشْرَة الْأَخْبَار · يُعْرَض",
    requires=["برنامج", "قناة", "عرض", "وثائقي", "مسلسل", "فيلم", "بدأ", "لهجة"],
    cards=[
        card("A TV vocabulary",
             "A television channel is a قَنَاة. A programme is a بَرْنَامَج (plural بَرَامِج), and a list of programmes is a جَدْوَل. "
             "To say that something is shown, use يُعْرَض, the passive of عَرَضَ (“to show”).",
             tables=[table(["English", "Arabic"],
                           [["channel", "قَنَاة"], ["programme", "بَرْنَامَج"], ["programmes", "بَرَامِج"], ["schedule", "جَدْوَل"],
                            ["documentary film", "فِيلْم وَثَائِقِيّ"], ["series", "مُسَلْسَل"], ["news bulletin", "نَشْرَة الْأَخْبَار"],
                            ["weather bulletin", "نَشْرَة الطَّقْس"], ["dialect", "لَهْجَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Reading a programme guide",
             "These are invented entries. Notice يَبْدَأ (begins) and يَنْتَهِي (ends), with مِنَ السَّاعَة … إِلَى السَّاعَة … for times.",
             examples=[
                 ex("يُعْرَض الْبَرْنَامَج الْوَثَائِقِيّ يَوْم الْأَحَد.", "The documentary programme is shown on Sunday.", "يُعْرَض"),
                 ex("نَشْرَة الْأَخْبَار عَلَى هَذِهِ الْقَنَاة فِي السَّابِعَة مَسَاءً.", "The news bulletin is on this channel at seven in the evening.", "نَشْرَة الْأَخْبَار"),
                 ex("يَبْدَأ الْمُسَلْسَل فِي الثَّامِنَة وَيَنْتَهِي فِي التَّاسِعَة.", "The series begins at eight and ends at nine.", "يَبْدَأ"),
                 ex("هُنَاكَ بَرْنَامَج عَنِ الْجِبَال وَالْأَنْهَار.", "There is a programme about mountains and rivers.", "عَنِ"),
                 ex("نُحِبّ مُشَاهَدَة الْأَفْلَام الْوَثَائِقِيَّة.", "We like watching documentary films.", "الْوَثَائِقِيَّة"),
                 ex("جَدْوَل الْبَرَامِج عَلَى مَوْقِع الْقَنَاة.", "The programme schedule is on the channel’s website.", "جَدْوَل"),
             ]),
    ],
    exercises=[
        M("What is the plural of بَرْنَامَج?", "بَرَامِج", ["بَرْنَامَجَات", "بَرْنَامَجُون", "أَبْرَمَة"], "A broken plural."),
        M("What does جَدْوَل الْبَرَامِج mean?", "the programme schedule", ["the news channel", "the weather", "the documentary"], "جَدْوَل = table, schedule."),
        M("What does يُعْرَض mean?", "is shown", ["is sold", "is opened", "is closed"], "عَرَضَ = to show."),
        M("Which means “The series begins at eight and ends at nine”?", "يَبْدَأ الْمُسَلْسَل فِي الثَّامِنَة وَيَنْتَهِي فِي التَّاسِعَة", ["يَبْدَأ الْمُسَلْسَل فِي التَّاسِعَة وَيَنْتَهِي فِي الثَّامِنَة", "يُعْرَض الْمُسَلْسَل يَوْم الْأَحَد", "يَنْتَهِي الْمُسَلْسَل وَلَا يَبْدَأ"], "يَبْدَأ = begins, يَنْتَهِي = ends."),
        M("Which means “documentary film”?", "فِيلْم وَثَائِقِيّ", ["مُسَلْسَل أَخْبَار", "نَشْرَة الطَّقْس", "لَهْجَة"], "وَثَائِقِيّ = documentary."),
        M("Which preposition means “about” in بَرْنَامَج عَنِ الْجِبَال?", "عَنْ", ["فِي", "مَعَ", "إِلَى"], "عَنْ = about."),
        F("يُعْرَض الْبَرْنَامَج ___ يَوْم الْأَحَد.", "الْوَثَائِقِيّ", ["الْوَثَائِقِيَّة", "وَثَائِقِيّ", "الْوَثَائِقِيُّون"], "Masculine, with ال.", tr="The documentary programme is shown on Sunday."),
        F("نَشْرَة ___ عَلَى هَذِهِ الْقَنَاة فِي السَّابِعَة.", "الْأَخْبَار", ["الْخَبَر", "أَخْبَار", "مُخْبِر"], "The news bulletin: iḍāfa.", tr="The news bulletin is on this channel at seven."),
        F("___ الْمُسَلْسَل فِي الثَّامِنَة.", "يَبْدَأ", ["يَنْتَهِي", "تَبْدَأ", "بَدَأْتُ"], "Begins.", tr="The series begins at eight."),
    ],
    verify=vw("قَنَاة", "بَرْنَامَج", "بَرَامِج", "جَدْوَل", "وَثَائِقِيّ", "الْوَثَائِقِيّ", "الْوَثَائِقِيَّة", "مُسَلْسَل", "نَشْرَة", "الْأَخْبَار", "لَهْجَة", "يُعْرَض", "يَبْدَأ", "يَنْتَهِي",
              "الثَّامِنَة", "الْأَنْهَار", "الْأَفْلَام", "مَوْقِع", "نُحِبّ"),
)

# ---------------------------------------------------------------------------- 223
L223 = lesson(
    "Choosing a programme from a schedule",
    "مِنَ السَّاعَة الرَّابِعَة إِلَى الْخَامِسَة · بَعْدَ الدِّرَاسَة",
    requires=["برنامج", "قناة", "ساعة", "بعد", "يوم", "جغرافيا", "دراسة"],
    cards=[
        card("A schedule (invented)",
             "Here is an invented schedule. Read each line and decide when you can watch. School ends at half past three.",
             tables=[table(["Day", "Programme", "Time"],
                           [["الْأَحَد", "بَرْنَامَج عَنِ الْجِبَال", "مِنَ الرَّابِعَة إِلَى الْخَامِسَة"],
                            ["الِاثْنَيْن", "نَشْرَة الْأَخْبَار", "فِي السَّابِعَة مَسَاءً"],
                            ["الثُّلَاثَاء", "فِيلْم وَثَائِقِيّ عَنِ الصَّحْرَاء", "مِنَ الثَّالِثَة إِلَى الرَّابِعَة"],
                            ["الْأَرْبِعَاء", "مُسَلْسَل بِاللَّهْجَة الْمِصْرِيَّة", "مِنَ الْخَامِسَة إِلَى السَّادِسَة"]],
                           say=[0, 1, 2], tlit=[], gloss=False)]),
        card("Choosing",
             "To say what fits your day, use يُنَاسِبُنِي (“it suits me”) and بَعْدَ الدِّرَاسَة (“after school”).",
             examples=[
                 ex("الدِّرَاسَة تَنْتَهِي فِي الثَّالِثَة وَالنِّصْف.", "School ends at half past three.", "تَنْتَهِي"),
                 ex("بَرْنَامَج الْجِبَال يُنَاسِبُنِي لِأَنَّهُ بَعْدَ الدِّرَاسَة.", "The mountains programme suits me because it is after school.", "يُنَاسِبُنِي"),
                 ex("فِيلْم الصَّحْرَاء لَا يُنَاسِبُنِي لِأَنَّهُ قَبْلَ نِهَايَة الدِّرَاسَة.", "The desert film does not suit me because it is before the end of school.", "قَبْلَ"),
                 ex("سَأُشَاهِد الْبَرْنَامَج يَوْم الْأَحَد.", "I will watch the programme on Sunday.", "سَأُشَاهِد"),
                 ex("وَيَوْم الْأَرْبِعَاء أُشَاهِد الْمُسَلْسَل.", "And on Wednesday I watch the series.", "الْأَرْبِعَاء"),
                 ex("أَيّ قَنَاة تَعْرِض الْأَخْبَار؟", "Which channel shows the news?", "أَيّ"),
             ]),
    ],
    exercises=[
        M("According to the schedule, which programme is on Sunday?", "a programme about mountains", ["a news bulletin", "a desert documentary", "a series in Egyptian dialect"], "الْأَحَد: بَرْنَامَج عَنِ الْجِبَال."),
        M("When is the news bulletin?", "on Monday at seven in the evening", ["on Sunday at four", "on Tuesday at three", "on Wednesday at five"], "الِاثْنَيْن: فِي السَّابِعَة مَسَاءً."),
        M("School ends at half past three. Which programme is too early?", "the desert documentary on Tuesday (three to four)", ["the mountains programme on Sunday", "the series on Wednesday", "the news on Monday"], "It starts at three, before school ends."),
        M("What does يُنَاسِبُنِي mean?", "it suits me", ["it frightens me", "it teaches me", "it follows me"], "نَاسَبَ = to suit."),
        M("Which means “after school”?", "بَعْدَ الدِّرَاسَة", ["قَبْلَ الدِّرَاسَة", "أَثْنَاءَ الدِّرَاسَة", "بِدُونِ دِرَاسَة"], "بَعْدَ = after."),
        M("Which means “Which channel shows the news?”", "أَيّ قَنَاة تَعْرِض الْأَخْبَار؟", ["مَنْ يَعْرِض الْأَخْبَار؟", "أَيْنَ قَنَاة الْأَخْبَار؟", "مَتَى تَبْدَأ الْأَخْبَار؟"], "أَيّ = which."),
        F("بَرْنَامَج الْجِبَال ___ لِأَنَّهُ بَعْدَ الدِّرَاسَة.", "يُنَاسِبُنِي", ["يُنَاسِبُك", "يُنَاسِبُهُ", "نَاسَبَ"], "It suits me.", tr="The mountains programme suits me because it is after school."),
        F("سَأُشَاهِد الْبَرْنَامَج ___ الْأَحَد.", "يَوْم", ["لَيْلَة", "مِنْ", "إِلَى"], "On Sunday = يَوْم الْأَحَد, with no preposition.", tr="I will watch the programme on Sunday."),
        F("الدِّرَاسَة ___ فِي الثَّالِثَة وَالنِّصْف.", "تَنْتَهِي", ["تَبْدَأ", "يَنْتَهِي", "نَنْتَهِي"], "She ends.", tr="School ends at half past three."),
    ],
    verify=vw("الْأَحَد", "الِاثْنَيْن", "الثُّلَاثَاء", "الْأَرْبِعَاء", "الرَّابِعَة", "الْخَامِسَة", "السَّادِسَة", "السَّابِعَة", "الثَّالِثَة", "الدِّرَاسَة", "يُنَاسِبُنِي", "تَنْتَهِي", "سَأُشَاهِد", "أُشَاهِد", "تَعْرِض", "الْمِصْرِيَّة", "بِاللَّهْجَة", "الْأَخْبَار", "وَالنِّصْف"),
)


# ---------------------------------------------------------------------------- 224
L224 = lesson(
    "Still: مَا زَالَ",
    "مَا زِلْتُ فِي الْمَكْتَبَة · مَا زَالَتْ سَارَة هُنَاكَ",
    requires=["زال", "مكتبة", "جامعة", "هنا", "طريق", "فندق"],
    cards=[
        card("How to say “still”",
             "Arabic says “still” with the verb زَالَ and the word مَا before it: مَا زَالَ. The word مَا makes it negative in form, "
             "but the meaning is positive: مَا زِلْتُ فِي الْمَكْتَبَة means “I am still in the library”. The verb is conjugated like a hollow verb: "
             "the long ā becomes short before the endings ـتُ, ـتَ, ـنَا and ـنَ. The short vowel is a kasra (زِلْتُ), where قَالَ has a ḍamma (قُلْتُ).",
             tables=[table(["English", "Arabic"],
                           [["I am still", "مَا زِلْتُ"], ["we are still", "مَا زِلْنَا"], ["you are still (to a man)", "مَا زِلْتَ"],
                            ["you are still (to a woman)", "مَا زِلْتِ"], ["he is still", "مَا زَالَ"], ["she is still", "مَا زَالَتْ"],
                            ["they are still (men)", "مَا زَالُوا"], ["you are still (all men)", "مَا زِلْتُمْ"],
                            ["the two (men) are still", "مَا زَالَا"], ["the two (women) are still", "مَا زَالَتَا"],
                            ["they are still (women)", "مَا زِلْنَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("With a place",
             "The simplest use is with a place or time. Put the place after the verb. To ask “Are you still…?”, put هَلْ before مَا زِلْتَ.",
             examples=[
                 ex("مَا زِلْتُ فِي الْمَكْتَبَة.", "I am still in the library.", "مَا زِلْتُ"),
                 ex("هَلْ مَا زِلْتَ هُنَا؟", "Are you still here? (to a man)", "مَا زِلْتَ"),
                 ex("مَا زَالَتْ سَارَة فِي الْجَامِعَة.", "Sara is still at the university.", "مَا زَالَتْ"),
                 ex("مَا زِلْنَا فِي الطَّرِيق.", "We are still on the way.", "مَا زِلْنَا"),
                 ex("الطُّلَّاب مَا زَالُوا فِي الصَّفّ.", "The students are still in the classroom.", "مَا زَالُوا"),
                 ex("مَا زَالَ أَخِي فِي الْفُنْدُق.", "My brother is still in the hotel.", "مَا زَالَ"),
             ]),
    ],
    exercises=[
        M("What does مَا زِلْتُ فِي الْمَكْتَبَة mean?", "I am still in the library", ["I was not in the library", "I am not in the library", "I left the library"], "مَا زَالَ = still (positive meaning)."),
        M("Which means “we are still”?", "مَا زِلْنَا", ["مَا زِلْتُ", "مَا زَالُوا", "مَا زَالَتْ"], "ـنَا = we."),
        M("Which means “she is still”?", "مَا زَالَتْ", ["مَا زَالَ", "مَا زَالُوا", "مَا زِلْنَ"], "تْ = she."),
        M("Which means “they are still” (men)?", "مَا زَالُوا", ["مَا زَالَ", "مَا زِلْتُمْ", "مَا زَالَتَا"], "ـُوا = they (men)."),
        M("Which means “Sara is still at the university”?", "مَا زَالَتْ سَارَة فِي الْجَامِعَة", ["مَا زَالَ سَارَة فِي الْجَامِعَة", "مَا زَالَتْ سَارَة فِي الْفُنْدُق", "مَا زِلْتُ سَارَة فِي الْجَامِعَة"], "A woman: مَا زَالَتْ."),
        M("To which verb is زَالَ conjugated like?", "قَالَ (a hollow verb)", ["كَتَبَ (a sound verb)", "رَأَى", "دَرَّسَ"], "The ā shortens before ـتُ, ـنَا."),
        F("مَا ___ سَارَة فِي الْجَامِعَة.", "زَالَتْ", ["زَالَ", "زَالُوا", "زِلْنَا"], "Sara is a woman.", tr="Sara is still at the university.", lemma="زول:past:hiya"),
        F("الطُّلَّاب مَا ___ فِي الصَّفّ.", "زَالُوا", ["زَالَتْ", "زِلْنَا", "زَالَ"], "Several men.", tr="The students are still in the classroom.", lemma="زول:past:hum"),
        F("مَا ___ فِي الطَّرِيق. (we)", "زِلْنَا", ["زِلْتُ", "زَالُوا", "زَالَتْ"], "We.", tr="We are still on the way.", lemma="زول:past:nahnu"),
    ],
    verify=(vv("زول", "past", ana="زِلْتُ", nahnu="زِلْنَا", anta="زِلْتَ", anti="زِلْتِ", huwa="زَالَ", hiya="زَالَتْ", hum="زَالُوا", antum="زِلْتُمْ", huma_m="زَالَا", huma_f="زَالَتَا", hunna="زِلْنَ")
            + vw("زِلْتُ", "زِلْنَا", "زِلْتَ", "زِلْتِ", "زَالَ", "زَالَتْ", "زَالُوا", "زِلْتُمْ", "زَالَا", "زَالَتَا", "زِلْنَ", "الْمَكْتَبَة", "الْجَامِعَة", "الطَّرِيق", "الْفُنْدُق")),
)

# ---------------------------------------------------------------------------- 225
L225 = lesson(
    "Still, with a noun or an adjective after it",
    "مَا زَالَ الطَّقْس بَارِدًا · مَا زَالَتْ مَسْرُورَةً",
    requires=["زال", "طقس", "بارد", "ولد", "طالب"],
    cards=[
        card("The second part goes into the accusative",
             "A nominal sentence has a subject and a predicate: الطَّقْس بَارِد. After مَا زَالَ the subject stays as it is, but the "
             "predicate changes into the accusative case. For one man it adds ـًا; for one woman ـَةً; for two ـَيْنِ; for several men ـِينَ.",
             tables=[table(["Without مَا زَالَ", "With مَا زَالَ"],
                           [["الطَّقْس بَارِد", "مَا زَالَ الطَّقْس بَارِدًا"], ["الْمُدَرِّسَة مَسْرُورَة", "مَا زَالَتِ الْمُدَرِّسَة مَسْرُورَةً"],
                            ["الْوَلَدَانِ مُجْتَهِدَانِ", "مَا زَالَ الْوَلَدَانِ مُجْتَهِدَيْنِ"], ["الطُّلَّاب مُجْتَهِدُون", "مَا زَالَ الطُّلَّاب مُجْتَهِدِينَ"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Remember that a helping kasra joins مَا زَالَتْ to ال: مَا زَالَتِ الْمُدَرِّسَة. The subject after مَا زَالَ keeps its normal nominative form (for example the dual "
             "الْوَلَدَانِ); only the predicate changes.",
             examples=[
                 ex("مَا زَالَ الطَّقْس بَارِدًا.", "The weather is still cold.", "بَارِدًا"),
                 ex("مَا زَالَتِ الْمُدَرِّسَة مَسْرُورَةً.", "The teacher is still happy.", "مَسْرُورَةً"),
                 ex("مَا زَالَ الْوَلَدَانِ مُجْتَهِدَيْنِ.", "The two boys are still hard-working.", "مُجْتَهِدَيْنِ"),
                 ex("مَا زَالَ الطُّلَّاب مُجْتَهِدِينَ.", "The students are still hard-working.", "مُجْتَهِدِينَ"),
                 ex("هَلْ مَا زَالَتِ الْمَكْتَبَة مَفْتُوحَةً؟", "Is the library still open?", "مَفْتُوحَةً"),
                 ex("مَا زِلْتُ مُتْعَبًا بَعْدَ الرِّحْلَة.", "I am still tired after the trip.", "مُتْعَبًا"),
             ]),
    ],
    exercises=[
        M("What case is the predicate in after مَا زَالَ?", "the accusative", ["the nominative", "the genitive", "it does not change"], "The predicate takes an accusative ending."),
        M("Which means “The weather is still cold”?", "مَا زَالَ الطَّقْس بَارِدًا", ["مَا زَالَ الطَّقْس بَارِدٌ", "مَا زَالَتِ الطَّقْس بَارِدًا", "الطَّقْس مَا بَارِدًا"], "The predicate takes an accusative ending."),
        M("Which means “The teacher (f.) is still happy”?", "مَا زَالَتِ الْمُدَرِّسَة مَسْرُورَةً", ["مَا زَالَ الْمُدَرِّسَة مَسْرُورَةً", "مَا زَالَتِ الْمُدَرِّسَة مَسْرُورٌ", "مَا زَالَتِ الْمُدَرِّسَة مَسْرُورِينَ"], "Feminine: مَا زَالَتْ … ـَةً."),
        M("Which ending shows the accusative of a dual predicate?", "ـَيْنِ", ["ـَانِ", "ـُونَ", "ـَاتٌ"], "Dual accusative: ـَيْنِ."),
        M("Which ending shows the accusative of a sound masculine plural predicate?", "ـِينَ", ["ـُونَ", "ـَيْنِ", "ـَاتٍ"], "Plural accusative: ـِينَ."),
        M("Why is it مَا زَالَتِ with a kasra in مَا زَالَتِ الْمُدَرِّسَة?", "to join the sukūn to ال", ["it is plural", "it is a question", "it is masculine"], "A helping vowel."),
        F("مَا زَالَ الطُّلَّاب ___.", "مُجْتَهِدِينَ", ["مُجْتَهِدُونَ", "مُجْتَهِدَيْنِ", "مُجْتَهِدَةً"], "Several men, accusative.", tr="The students are still hard-working."),
        F("مَا زَالَتِ الْمُدَرِّسَة ___.", "مَسْرُورَةً", ["مَسْرُورًا", "مَسْرُورَةٌ", "مَسْرُورِينَ"], "One woman, accusative.", tr="The teacher is still happy."),
        F("مَا زَالَ الطَّقْس ___.", "بَارِدًا", ["بَارِدٌ", "بَارِدَةً", "بَارِدِينَ"], "One man or thing, masculine, accusative.", tr="The weather is still cold."),
    ],
    verify=(vd("مُجْتَهِد", "مُجْتَهِدَانِ", "مُجْتَهِدَيْنِ") + vps("مُجْتَهِد", "مُجْتَهِدُونَ", "nom") + vps("مُجْتَهِد", "مُجْتَهِدِينَ", "obl") + vf("مَسْرُور", "مَسْرُورَة")
            + vw("بَارِدًا", "مَسْرُورَةً", "مُجْتَهِدَيْنِ", "مُجْتَهِدِينَ", "مَفْتُوحَةً", "مُتْعَبًا", "الرِّحْلَة", "الْوَلَدَانِ", "وَالِدَاهَا", "الطَّقْس")),
)

# ---------------------------------------------------------------------------- 226
L226 = lesson(
    "Still doing something: مَا زِلْتُ أَدْرُس",
    "مَا زِلْتُ أَدْرُس · لَا يَزَال يَعِيش هُنَا · مَا زِلْنَا نُفَكِّر",
    requires=["زال", "درس", "عاش", "فكر", "علم", "رحلة", "عمل"],
    cards=[
        card("A verb after مَا زَالَ",
             "To say “still doing”, put the present verb after مَا زَالَ. Both verbs agree with the person: مَا زِلْتُ أَدْرُس (“I am still "
             "studying”), مَا زَالُوا يَدْرُسُون. The present-tense twin of مَا زَالَ is لَا يَزَال (“he is still”), which means the same.",
             tables=[table(["English", "لَا يَزَال", "مَا زَالَ"],
                           [["I am still", "لَا أَزَال", "مَا زِلْتُ"], ["we are still", "لَا نَزَال", "مَا زِلْنَا"], ["you are still (m.)", "لَا تَزَال", "مَا زِلْتَ"],
                            ["you are still (f.)", "لَا تَزَالِين", "مَا زِلْتِ"], ["he is still", "لَا يَزَال", "مَا زَالَ"], ["she is still", "لَا تَزَال", "مَا زَالَتْ"],
                            ["they are still (m.)", "لَا يَزَالُون", "مَا زَالُوا"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("In sentences",
             "With لَا يَزَال, the predicate is accusative too: لَا تَزَال الْمَكْتَبَة مَفْتُوحَةً.",
             examples=[
                 ex("مَا زِلْتُ أَدْرُس الْعَرَبِيَّة.", "I am still studying Arabic.", "مَا زِلْتُ أَدْرُس"),
                 ex("مَا زَالَ أَخِي يَعِيش فِي الْمَدِينَة.", "My brother still lives in the city.", "يَعِيش"),
                 ex("لَا تَزَال الْمَكْتَبَة مَفْتُوحَةً.", "The library is still open.", "لَا تَزَال"),
                 ex("لَا يَزَالُون يَنْتَظِرُون الْحَافِلَة.", "They are still waiting for the bus.", "لَا يَزَالُون"),
                 ex("هَلْ مَا زِلْتِ تَتَعَلَّمِين السِّبَاحَة؟", "Are you still learning to swim? (to a woman)", "مَا زِلْتِ"),
                 ex("مَا زِلْنَا نُفَكِّر فِي الرِّحْلَة.", "We are still thinking about the trip.", "نُفَكِّر"),
             ]),
    ],
    exercises=[
        M("Which means “I am still studying”?", "مَا زِلْتُ أَدْرُس", ["مَا زَالَ يَدْرُس", "مَا زِلْنَا نَدْرُس", "كُنْتُ أَدْرُس"], "مَا زِلْتُ + أَدْرُس."),
        M("Which means “he is still” (the present twin)?", "لَا يَزَال", ["مَا زَالَتْ", "لَا أَزَال", "لَا تَزَالُون"], "لَا يَزَال = مَا زَالَ."),
        M("Which means “We are still thinking about the trip”?", "مَا زِلْنَا نُفَكِّر فِي الرِّحْلَة", ["مَا زِلْتُ أُفَكِّر فِي الرِّحْلَة", "مَا زَالُوا يُفَكِّرُون فِي الرِّحْلَة", "فَكَّرْنَا فِي الرِّحْلَة"], "نَا + نُفَكِّر."),
        M("Which means “They are still waiting for the bus”?", "لَا يَزَالُون يَنْتَظِرُون الْحَافِلَة", ["لَا يَزَال يَنْتَظِر الْحَافِلَة", "مَا زِلْنَا نَنْتَظِر الْحَافِلَة", "لَا تَزَال تَنْتَظِر الْحَافِلَة"], "Men, plural."),
        M("Which means “Are you still learning?” (to a woman)", "هَلْ مَا زِلْتِ تَتَعَلَّمِين؟", ["هَلْ مَا زِلْتَ تَتَعَلَّم؟", "هَلْ مَا زَالَتْ تَتَعَلَّم؟", "هَلْ مَا زِلْنَ يَتَعَلَّمْنَ؟"], "A kasra for a woman."),
        M("What case is the predicate in لَا تَزَال الْمَكْتَبَة مَفْتُوحَةً?", "accusative", ["nominative", "genitive", "there is no case"], "ـَةً."),
        F("مَا ___ أَخِي يَعِيش فِي الْمَدِينَة.", "زَالَ", ["زَالَتْ", "زَالُوا", "زِلْتُ"], "My brother = he.", tr="My brother still lives in the city.", lemma="زول:past:huwa"),
        F("لَا ___ الْمَكْتَبَة مَفْتُوحَةً.", "تَزَال", ["يَزَال", "أَزَال", "تَزَالُون"], "Library is feminine.", tr="The library is still open.", lemma="زول:pres:hiya"),
        F("مَا زِلْنَا ___ فِي الرِّحْلَة.", "نُفَكِّر", ["أُفَكِّر", "يُفَكِّرُون", "فَكَّرْنَا"], "We.", tr="We are still thinking about the trip.", lemma="فكر#2:pres:nahnu"),
    ],
    verify=(vv("زول", "pres", ana="أَزَال", nahnu="نَزَال", anta="تَزَال", anti="تَزَالِين", huwa="يَزَال", hiya="تَزَال", hum="يَزَالُون")
            + vv("درس", "pres", ana="أَدْرُس") + vv("عيش", "pres", huwa="يَعِيش") + vv("فكر#2", "pres", nahnu="نُفَكِّر") + vv("علم#5", "pres", anti="تَتَعَلَّمِين")
            + vw("يَنْتَظِرُون", "السِّبَاحَة", "الْحَافِلَة", "مَفْتُوحَةً", "الْعَرَبِيَّة")),
)


# ---------------------------------------------------------------------------- 227
L227 = lesson(
    "Measure V in the past: تَعَلَّمَ · تَخَرَّجَ · تَوَقَّفَ",
    "تَعَلَّمْتُ · تَخَرَّجَ أَخِي · تَوَقَّفَتِ الْحَافِلَة",
    requires=["علم", "درب", "خرج", "وقف", "غير", "تعلم", "تخرج", "تغير"],
    cards=[
        card("Measure II + تَـ = Measure V",
             "You know Measure V from Unit 10. To make it, put تَـ in front of a Measure II verb: عَلَّمَ (he taught) → تَعَلَّمَ (he learned). "
             "Measure V often says that the action is carried out by the subject itself, or that a result is reached. "
             "In the past, the doubled middle letter keeps a fatḥa: تَفَعَّلَ.",
             tables=[table(["English", "Measure II", "Measure V"],
                           [["teach → learn", "عَلَّمَ", "تَعَلَّمَ"], ["train (someone) → train", "دَرَّبَ", "تَدَرَّبَ"],
                            ["graduate (someone) → graduate", "خَرَّجَ", "تَخَرَّجَ"], ["stop (something) → stop", "وَقَّفَ", "تَوَقَّفَ"],
                            ["delay → be late", "أَخَّرَ", "تَأَخَّرَ"], ["change (something) → change", "غَيَّرَ", "تَغَيَّرَ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("The past tense of Measure V",
             "The endings are the same as for every past tense. Practise them with تَعَلَّمَ.",
             tables=[table(["English", "Arabic"],
                           [["I learned", "تَعَلَّمْتُ"], ["we learned", "تَعَلَّمْنَا"], ["you learned (m.)", "تَعَلَّمْتَ"], ["you learned (f.)", "تَعَلَّمْتِ"],
                            ["he learned", "تَعَلَّمَ"], ["she learned", "تَعَلَّمَتْ"], ["they learned (m.)", "تَعَلَّمُوا"], ["you learned (all m.)", "تَعَلَّمْتُمْ"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("تَعَلَّمَ الطُّلَّاب كَثِيرًا فِي الْمَدْرَسَة.", "The students learned a lot at school.", "تَعَلَّمَ"),
                 ex("تَخَرَّجَ أَخِي مِنَ الْجَامِعَة.", "My brother graduated from the university.", "تَخَرَّجَ"),
                 ex("تَدَرَّبَ الْوَلَد عَلَى قِيَادَة الدَّرَّاجَة.", "The boy practised riding the bicycle.", "تَدَرَّبَ"),
                 ex("تَوَقَّفَتِ الْحَافِلَة أَمَامَ الْمَحَطَّة.", "The bus stopped in front of the station.", "تَوَقَّفَتِ"),
                 ex("تَأَخَّرَ الْقِطَار نِصْف سَاعَة.", "The train was half an hour late.", "تَأَخَّرَ"),
                 ex("تَغَيَّرَ الطَّقْس فِي الصَّبَاح.", "The weather changed in the morning.", "تَغَيَّرَ"),
             ]),
    ],
    exercises=[
        M("Which is Measure V of عَلَّمَ?", "تَعَلَّمَ", ["أَعْلَمَ", "عَالَمَ", "تَعَالَمَ"], "تَـ + Measure II."),
        M("What does تَخَرَّجَ mean?", "he graduated", ["he left the house", "he drove", "he stopped"], "تَخَرَّجَ مِنْ = to graduate from."),
        M("What does تَوَقَّفَتِ الْحَافِلَة mean?", "The bus stopped", ["The bus was late", "The bus left", "The bus arrived"], "تَوَقَّفَ = to stop."),
        M("Which means “they learned” (men)?", "تَعَلَّمُوا", ["تَعَلَّمَ", "تَعَلَّمَتْ", "تَعَلَّمْنَا"], "ـُوا = they (men)."),
        M("Which means “she learned”?", "تَعَلَّمَتْ", ["تَعَلَّمَ", "تَعَلَّمُوا", "تَعَلَّمْتِ"], "تْ = she."),
        M("Which means “The train was half an hour late”?", "تَأَخَّرَ الْقِطَار نِصْف سَاعَة", ["تَوَقَّفَ الْقِطَار نِصْف سَاعَة", "غَادَرَ الْقِطَار نِصْف سَاعَة", "تَغَيَّرَ الْقِطَار نِصْف سَاعَة"], "تَأَخَّرَ = to be late."),
        F("الطُّلَّاب ___ كَثِيرًا فِي الْمَدْرَسَة.", "تَعَلَّمُوا", ["تَعَلَّمَ", "تَعَلَّمَتْ", "تَعَلَّمْنَا"], "The subject comes first, so the verb agrees: they (men).", tr="The students learned a lot at school.", lemma="علم#5:past:hum"),
        F("أَنَا ___ كَثِيرًا مِنْ مُدَرِّسِي.", "تَعَلَّمْتُ", ["تَعَلَّمَتْ", "تَعَلَّمُوا", "تَعَلَّمْنَا"], "I.", tr="I learned a lot from my teacher."),
        F("هِيَ ___ مِنَ الْجَامِعَة.", "تَخَرَّجَتْ", ["تَخَرَّجَ", "تَخَرَّجُوا", "تَخَرَّجْتَ"], "She.", tr="She graduated from the university.", lemma="خرج#5:past:hiya"),
    ],
    verify=(vv("علم#5", "past", ana="تَعَلَّمْتُ", nahnu="تَعَلَّمْنَا", anta="تَعَلَّمْتَ", anti="تَعَلَّمْتِ", huwa="تَعَلَّمَ", hiya="تَعَلَّمَتْ", hum="تَعَلَّمُوا", antum="تَعَلَّمْتُمْ")
            + vv("درب#5", "past", huwa="تَدَرَّبَ") + vv("خرج#5", "past", huwa="تَخَرَّجَ", ana="تَخَرَّجْتُ") + vv("خرج#2", "past", huwa="خَرَّجَ")
            + vv("درب#2", "past", huwa="دَرَّبَ") + vv("علم#2", "past", huwa="عَلَّمَ")
            + vw("تَوَقَّفَ", "تَوَقَّفَتِ", "وَقَّفَ", "تَأَخَّرَ", "أَخَّرَ", "تَغَيَّرَ", "غَيَّرَ", "قِيَادَة", "السِّبَاحَة", "الدَّرَّاجَة", "نِصْف")),
)

# ---------------------------------------------------------------------------- 228
L228 = lesson(
    "Measure V verbal nouns: التَّعَلُّم · التَّوَقُّف",
    "تَعَلَّمَ ← تَعَلُّم · تَخَرَّجَ ← تَخَرُّج · تَوَقَّفَ ← تَوَقُّف",
    requires=["تعلم", "تخرج", "توقف", "تغير", "تطور", "تكلم", "حفلة"],
    cards=[
        card("From the verb to the noun",
             "A verbal noun (masdar) names the action: “learning”, “stopping”. For Measure V, take the past verb and change the "
             "fatḥa on the doubled letter into a ḍamma, then drop the last fatḥa: تَعَلَّمَ → تَعَلُّم. The result has the pattern تَفَعُّل. "
             "As with other verbal nouns, ال is added when you mean “the learning”.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["learn", "تَعَلَّمَ", "تَعَلُّم"], ["train", "تَدَرَّبَ", "تَدَرُّب"], ["graduate", "تَخَرَّجَ", "تَخَرُّج"],
                            ["stop", "تَوَقَّفَ", "تَوَقُّف"], ["be late", "تَأَخَّرَ", "تَأَخُّر"], ["change", "تَغَيَّرَ", "تَغَيُّر"],
                            ["develop", "تَطَوَّرَ", "تَطَوُّر"], ["speak", "تَكَلَّمَ", "تَكَلُّم"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Verbal nouns in use",
             "Verbal nouns often follow another noun in an iḍāfa (حَفْلَة التَّخَرُّج, “the graduation ceremony”) or follow مَمْنُوع on a sign.",
             examples=[
                 ex("مَمْنُوع التَّوَقُّف عَلَى الطَّرِيق السَّرِيع.", "Stopping on the highway is forbidden.", "التَّوَقُّف"),
                 ex("سَيَحْضُر الْمُدِير حَفْلَة التَّخَرُّج.", "The director will attend the graduation ceremony.", "حَفْلَة التَّخَرُّج"),
                 ex("يَبْدَأ التَّدَرُّب الصَّبَاحِيّ فِي الْخَامِسَة وَالنِّصْف.", "The morning training begins at half past five.", "التَّدَرُّب"),
                 ex("اِعْتَذَرَ عَنِ التَّأَخُّر.", "He apologised for the delay.", "التَّأَخُّر"),
                 ex("التَّغَيُّر فِي الطَّقْس سَرِيع.", "The change in the weather is fast.", "التَّغَيُّر"),
                 ex("التَّعَلُّم مُهِمّ لِكُلّ طَالِب.", "Learning is important for every student.", "التَّعَلُّم"),
             ]),
    ],
    exercises=[
        M("What is the verbal noun of تَعَلَّمَ?", "تَعَلُّم", ["تَعْلِيم", "مُتَعَلِّم", "عِلْم"], "تَفَعُّل: ḍamma on the doubled letter."),
        M("What is the verbal noun of تَوَقَّفَ?", "تَوَقُّف", ["وُقُوف", "تَوْقِيف", "مَوْقِف"], "تَفَعُّل."),
        M("What is the verbal noun of تَخَرَّجَ?", "تَخَرُّج", ["خُرُوج", "تَخْرِيج", "مُخَرِّج"], "تَفَعُّل."),
        M("What does حَفْلَة التَّخَرُّج mean?", "the graduation ceremony", ["the school bus", "the swimming class", "the news"], "تَخَرُّج = graduating."),
        M("What does مَمْنُوع التَّوَقُّف mean?", "no stopping", ["no entry", "no left turn", "road closed"], "تَوَقُّف = stopping."),
        M("How does the pattern تَفَعُّل differ from the verb تَفَعَّلَ?", "the doubled letter has a ḍamma", ["it has a kasra", "the first letter is dropped", "it has no doubled letter"], "ـَّ → ـُّ."),
        F("مَمْنُوع ___ عَلَى الطَّرِيق السَّرِيع.", "التَّوَقُّف", ["تَوَقَّفَ", "يَتَوَقَّف", "تَوَقَّفُوا"], "A verbal noun after مَمْنُوع.", tr="Stopping on the highway is forbidden."),
        F("سَيَحْضُر الْمُدِير حَفْلَة ___.", "التَّخَرُّج", ["تَخَرَّجَ", "الْخُرُوج", "الْمُتَخَرِّج"], "The ceremony of graduation.", tr="The director will attend the graduation ceremony."),
        F("اِعْتَذَرَ عَنِ ___.", "التَّأَخُّر", ["تَأَخَّرَ", "يَتَأَخَّر", "الْمُتَأَخِّر"], "The delay.", tr="He apologised for the delay."),
    ],
    verify=vw("تَعَلُّم", "التَّعَلُّم", "تَدَرُّب", "التَّدَرُّب", "تَخَرُّج", "التَّخَرُّج", "تَوَقُّف", "التَّوَقُّف", "تَأَخُّر", "التَّأَخُّر", "تَغَيُّر", "التَّغَيُّر", "تَطَوُّر", "تَكَلُّم",
              "حَفْلَة", "الصَّبَاحِيّ", "اِعْتَذَرَ", "سَيَحْضُر", "الْمُدِير", "الْخُرُوج", "الْمُتَخَرِّج", "تَعْلِيم", "تَوْقِيف", "وُقُوف", "مَوْقِف"),
)

# ---------------------------------------------------------------------------- 229
L229 = lesson(
    "A country profile",
    "تَقَع مِصْر فِي شَمَال إِفْرِيقِيَا وَعَاصِمَتُهَا الْقَاهِرَة",
    requires=["عاصمة", "لغة", "رسمي", "نهر", "شمال", "غرب", "بحر", "دولة"],
    cards=[
        card("The parts of a profile",
             "An area study follows a fixed order: where the country is, its capital, its neighbours and seas, and its language. These "
             "words build the profile. Use the verbs from this unit (تَقَع, يَحُدّ, تَشْتَهِر) and an ending for “its”: ـهَا for a feminine "
             "country, ـهُ for a masculine one.",
             tables=[table(["English", "Arabic"],
                           [["country, state", "دَوْلَة"], ["capital", "عَاصِمَة"], ["its capital", "عَاصِمَتُهَا"], ["official language", "اللُّغَة الرَّسْمِيَّة"],
                            ["neighbour", "جَار"], ["red", "أَحْمَر"], ["the Red Sea", "الْبَحْر الْأَحْمَر"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Three short profiles (simple facts)",
             "These sentences state well-known facts in short form. Read them aloud, then write a profile for another country.",
             examples=[
                 ex("تَقَع مِصْر فِي شَمَال إِفْرِيقِيَا وَعَاصِمَتُهَا الْقَاهِرَة.", "Egypt is in the north of Africa and its capital is Cairo.", "عَاصِمَتُهَا"),
                 ex("يَمُرّ نَهْر النِّيل فِي مِصْر وَالسُّودَان.", "The Nile flows through Egypt and Sudan.", "يَمُرّ"),
                 ex("اللُّغَة الرَّسْمِيَّة فِي مِصْر هِيَ اللُّغَة الْعَرَبِيَّة.", "The official language in Egypt is Arabic.", "اللُّغَة الرَّسْمِيَّة"),
                 ex("يَقَع الْأُرْدُنّ فِي غَرْب آسِيَا وَعَاصِمَتُهُ عَمَّان.", "Jordan is in west Asia and its capital is Amman.", "عَاصِمَتُهُ"),
                 ex("يَحُدّ الْبَحْر الْأَحْمَر السُّعُودِيَّة مِنَ الْغَرْب.", "The Red Sea borders Saudi Arabia on the west.", "الْبَحْر الْأَحْمَر"),
                 ex("عَاصِمَة السُّودَان هِيَ الْخُرْطُوم.", "The capital of Sudan is Khartoum.", "عَاصِمَة"),
             ]),
    ],
    exercises=[
        M("What does عَاصِمَتُهَا mean?", "its capital (of a feminine country)", ["its river", "its language", "its sea"], "ـهَا = her/its."),
        M("Which is the capital of Egypt, according to the lesson?", "الْقَاهِرَة", ["عَمَّان", "الْخُرْطُوم", "الرِّيَاض"], "عَاصِمَتُهَا الْقَاهِرَة."),
        M("Which country has the capital عَمَّان?", "الْأُرْدُنّ", ["مِصْر", "السُّودَان", "السُّعُودِيَّة"], "Amman is the capital of Jordan."),
        M("Which means “the official language”?", "اللُّغَة الرَّسْمِيَّة", ["لُغَة رَسْمِيَّة الْ", "الرَّسْمِيَّة اللُّغَة", "لُغَات الرَّسْمِيَّة"], "A noun and an adjective with ال."),
        M("Which means “The Nile flows through Egypt and Sudan”?", "يَمُرّ نَهْر النِّيل فِي مِصْر وَالسُّودَان", ["يَقَع نَهْر النِّيل فِي الْأُرْدُنّ وَالسُّودَان", "يَمُرّ نَهْر النِّيل فِي الْجَزِيرَة", "يَحُدّ نَهْر النِّيل الْبَحْر"], "يَمُرّ = passes."),
        M("Why عَاصِمَتُهُ for Jordan and عَاصِمَتُهَا for Egypt?", "الْأُرْدُنّ is masculine, مِصْر is feminine", ["both are masculine", "both are feminine", "they are plural"], "ـهُ = his/its, ـهَا = her/its."),
        F("تَقَع مِصْر فِي شَمَال ___.", "إِفْرِيقِيَا", ["آسِيَا", "الْقَاهِرَة", "الْأَحْمَر"], "Egypt’s continent.", tr="Egypt is in the north of Africa."),
        F("يَقَع الْأُرْدُنّ فِي غَرْب آسِيَا وَ___ عَمَّان.", "عَاصِمَتُهُ", ["عَاصِمَتُهَا", "عَاصِمَتِي", "عَاصِمَتُك"], "Masculine country.", tr="Jordan is in west Asia and its capital is Amman."),
        F("يَحُدّ ___ السُّعُودِيَّة مِنَ الْغَرْب.", "الْبَحْر الْأَحْمَر", ["الْبَحْر الْأَبْيَض", "نَهْر النِّيل", "الْخُرْطُوم"], "The sea in the west of Saudi Arabia.", tr="The Red Sea borders Saudi Arabia on the west."),
    ],
    verify=vw("مِصْر", "إِفْرِيقِيَا", "الْقَاهِرَة", "الْأُرْدُنّ", "آسِيَا", "عَمَّان", "السُّودَان", "الْخُرْطُوم", "السُّعُودِيَّة", "الرِّيَاض", "النِّيل", "الرَّسْمِيَّة", "اللُّغَة", "الْعَرَبِيَّة",
              "الْأَحْمَر", "الْأَبْيَض", "عَاصِمَة", "دَوْلَة", "جَار", "يَمُرّ"),
)

# ---------------------------------------------------------------------------- 230
L230 = lesson(
    "Review: still, Measure V, climate and place",
    "مَا زِلْتُ أَدْرُس · تَخَرَّجْتُ · مَا زَالَ الطَّقْس بَارِدًا",
    requires=["زال", "علم", "خرج", "وقف", "غير", "طقس", "مناخ", "برنامج"],
    cards=[
        card("What to remember",
             "مَا زَالَ (“still”) is conjugated like a hollow past verb and puts its predicate into the accusative: مَا زَالَ الطَّقْس بَارِدًا. "
             "Before a verb: مَا زِلْتُ أَدْرُس. Measure V = تَـ + Measure II; the past is تَفَعَّلَ and the verbal noun is تَفَعُّل.",
             tables=[table(["English", "Arabic"],
                           [["I am still studying.", "مَا زِلْتُ أَدْرُس"], ["The weather is still cold.", "مَا زَالَ الطَّقْس بَارِدًا"],
                            ["I graduated.", "تَخَرَّجْتُ"], ["the graduation ceremony", "حَفْلَة التَّخَرُّج"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A letter from a student (an invented practice text)",
             "A student writes to a friend about school, the weather and a trip. Read the sentences and find every use of “still” and every Measure V verb.",
             examples=[
                 ex("تَخَرَّجْتُ مِنَ الْمَدْرَسَة وَتَعَلَّمْتُ كَثِيرًا.", "I graduated from school and I learned a lot.", "تَخَرَّجْتُ"),
                 ex("مَا زِلْتُ أَدْرُس فِي الْجَامِعَة.", "I am still studying at the university.", "مَا زِلْتُ"),
                 ex("تَغَيَّرَ الْمُنَاخ فِي الشَّمَال وَلَا يَزَال الْجَوّ مُمْطِرًا.", "The climate in the north changed and the weather is still rainy.", "لَا يَزَال"),
                 ex("مَا زَالَ الطَّقْس بَارِدًا فِي الشِّتَاء.", "The weather is still cold in winter.", "بَارِدًا"),
                 ex("تَوَقَّفَتِ الْحَافِلَة وَمَا زِلْنَا فِي الطَّرِيق.", "The bus stopped and we are still on the way.", "تَوَقَّفَتِ"),
                 ex("مَمْنُوع التَّأَخُّر عَنِ الْمَوْعِد.", "Being late for the appointment is not allowed.", "التَّأَخُّر"),
             ]),
    ],
    exercises=[
        M("Which means “I am still studying at the university”?", "مَا زِلْتُ أَدْرُس فِي الْجَامِعَة", ["كُنْتُ أَدْرُس فِي الْجَامِعَة", "لَنْ أَدْرُس فِي الْجَامِعَة", "مَا زَالَ يَدْرُس فِي الْجَامِعَة"], "I = ـتُ."),
        M("Which means “The weather is still cold in winter”?", "مَا زَالَ الطَّقْس بَارِدًا فِي الشِّتَاء", ["مَا زَالَ الطَّقْس بَارِدٌ فِي الشِّتَاء", "الطَّقْس بَارِدًا مَا زَالَ", "مَا زَالَتِ الطَّقْس بَارِدًا"], "Accusative predicate."),
        M("Which is the Measure V verb in the lesson text for “I graduated”?", "تَخَرَّجْتُ", ["خَرَجْتُ", "أَخْرَجْتُ", "خَرَّجْتُ"], "تَـ + Measure II."),
        M("Which means “The bus stopped”?", "تَوَقَّفَتِ الْحَافِلَة", ["تَأَخَّرَتِ الْحَافِلَة", "تَغَيَّرَتِ الْحَافِلَة", "تَعَلَّمَتِ الْحَافِلَة"], "تَوَقَّفَ = to stop."),
        M("What is the verbal noun of تَأَخَّرَ?", "تَأَخُّر", ["تَأْخِير", "أَخَّرَ", "مُتَأَخِّر"], "تَفَعُّل."),
        M("Which means “still” in the present twin form (he)?", "لَا يَزَال", ["مَا زَالَتْ", "لَنْ يَزَال", "لَا أَزَال"], "لَا يَزَال = مَا زَالَ."),
        F("تَغَيَّرَ الْمُنَاخ فِي الشَّمَال وَلَا ___ الْجَوّ مُمْطِرًا.", "يَزَال", ["تَزَال", "يَزَالُون", "أَزَال"], "Weather = masculine.", tr="The climate in the north changed and the weather is still rainy."),
        F("مَمْنُوع ___ عَنِ الْمَوْعِد.", "التَّأَخُّر", ["تَأَخَّرَ", "تَأَخَّرُوا", "الْمُتَأَخِّر"], "Verbal noun.", tr="Being late for the appointment is not allowed."),
        F("تَوَقَّفَتِ الْحَافِلَة وَمَا ___ فِي الطَّرِيق.", "زِلْنَا", ["زِلْتُ", "زَالُوا", "زَالَتْ"], "We.", tr="The bus stopped and we are still on the way.", lemma="زول:past:nahnu"),
    ],
    verify=(vv("زول", "past", nahnu="زِلْنَا", ana="زِلْتُ") + vv("زول", "pres", huwa="يَزَال") + vv("خرج#5", "past", ana="تَخَرَّجْتُ") + vv("علم#5", "past", ana="تَعَلَّمْتُ")
            + vw("تَغَيَّرَ", "تَوَقَّفَتِ", "التَّأَخُّر", "الْمَوْعِد", "الْمُنَاخ", "مُمْطِرًا", "بَارِدًا", "تَأْخِير", "مُتَأَخِّر", "الْحَافِلَة", "الشِّتَاء")),
)


UNIT = unit("الْجُغْرَافِيَا: terrain, climate, “still” and Measure V", [L215, L216, L217, L218, L219, L220, L221, L222, L223, L224, L225, L226, L227, L228, L229, L230])
