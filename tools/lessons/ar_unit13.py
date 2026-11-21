"""Unit 13: the classroom, comparing things, school places, the genitive, adverbs of manner and “this / that” (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 181
L181 = lesson(
    "Things in the classroom",
    "السَّبُّورَة · الطَّاوِلَة · الْكُرْسِيّ · الْحَاسُوب · الطَّابِعَة",
    requires=["صف", "طاولة", "كرسي", "حاسوب", "حائط", "نافذة", "خريطة", "شاشة"],
    cards=[
        card("Furniture and equipment",
             "Most of these words are feminine because they end in ـَة (السَّبُّورَة, الطَّاوِلَة, الطَّابِعَة), "
             "but الْكُرْسِيّ, الْحَاسُوب, الْبَاب and الْحَائِط are masculine. Two words have more than one name: "
             "a wall is الْحَائِط (the outside or standing wall) or الْجِدَار, and a window is النَّافِذَة or الشُّبَّاك.",
             tables=[table(["English", "Arabic"],
                           [["the board", "السَّبُّورَة"], ["the table, desk", "الطَّاوِلَة"], ["the chair", "الْكُرْسِيّ"],
                            ["the computer", "الْحَاسُوب"], ["the printer", "الطَّابِعَة"], ["the screen", "الشَّاشَة"],
                            ["the lamp", "الْمِصْبَاح"], ["the wall", "الْحَائِط"], ["the window", "النَّافِذَة"],
                            ["the map", "الْخَرِيطَة"], ["the door", "الْبَاب"]],
                           say=[1], tlit=[1])]),
        card("Plural: more than one",
             "Several of these nouns have a broken plural: one chair is كُرْسِيّ, but chairs are كَرَاسِيّ; the plural of "
             "جِدَار (wall) is جُدْرَان. With the numbers 3 to 10 the counted noun is plural, "
             "and the number takes the opposite gender (you met this rule in Unit 5).",
             examples=[
                 ex("فِي الصَّفّ سَبُّورَة كَبِيرَة.", "There is a big board in the classroom.", "سَبُّورَة"),
                 ex("عَلَى الْحَائِط خَرِيطَة لِلْعَالَم.", "On the wall there is a map of the world.", "خَرِيطَة"),
                 ex("الْحَاسُوب وَالطَّابِعَة عَلَى الطَّاوِلَة.", "The computer and the printer are on the table.", "الطَّابِعَة"),
                 ex("هُنَاك عَشَرَة كَرَاسِيّ فِي الصَّفّ.", "There are ten chairs in the classroom.", "كَرَاسِيّ"),
                 ex("لَوْن الْجُدْرَان أَبْيَض.", "The colour of the walls is white.", "الْجُدْرَان"),
                 ex("أَرَى الشَّاشَة جَيِّدًا مِنْ هُنَا.", "I can see the screen well from here.", "الشَّاشَة"),
             ]),
    ],
    exercises=[
        M("What does السَّبُّورَة mean?", "the board", ["the table", "the map", "the lamp"], "سَبُّورَة = a board you write on."),
        M("Which word means “the printer”?", "الطَّابِعَة", ["الشَّاشَة", "الْحَاسُوب", "الْمِصْبَاح"], "طَابِعَة = printer."),
        M("What is the plural of كُرْسِيّ (chair)?", "كَرَاسِيّ", ["كُرْسِيَّات", "كُرْسِيُّون", "كَرْسَى"], "A broken plural."),
        M("Which word is another name for “window”?", "الشُّبَّاك", ["الْجِدَار", "الْبَاب", "السَّقْف"], "نَافِذَة or شُبَّاك."),
        M("Which means “On the wall there is a map of the world”?", "عَلَى الْحَائِط خَرِيطَة لِلْعَالَم", ["تَحْتَ الْحَائِط خَرِيطَة لِلْعَالَم", "عَلَى الطَّاوِلَة خَرِيطَة لِلْعَالَم", "عَلَى الْحَائِط سَبُّورَة لِلْعَالَم"], "عَلَى = on."),
        M("Which means “ten chairs” (a masculine noun)?", "عَشَرَة كَرَاسِيّ", ["عَشْر كَرَاسِيّ", "عَشَرَة كُرْسِيّ", "عَشْر كُرْسِيّ"], "3–10: a plural noun, and the number in the opposite gender."),
        F("الْحَاسُوب وَالطَّابِعَة ___ الطَّاوِلَة.", "عَلَى", ["تَحْتَ", "إِلَى", "مَعَ"], "On the table.", tr="The computer and the printer are on the table."),
        F("فِي الصَّفّ ___ كَبِيرَة.", "سَبُّورَة", ["سَبُّورَات", "طَابِعَات", "كَرَاسِيّ"], "One singular noun with one adjective.", tr="There is a big board in the classroom."),
        F("لَوْن ___ أَبْيَض.", "الْجُدْرَان", ["الْجِدَارَة", "الْجَدَر", "جُدَار"], "The plural of جِدَار.", tr="The colour of the walls is white."),
    ],
    verify=vw("السَّبُّورَة", "الطَّاوِلَة", "الْكُرْسِيّ", "الْحَاسُوب", "الطَّابِعَة", "الشَّاشَة", "الْمِصْبَاح", "الْحَائِط", "النَّافِذَة", "الْخَرِيطَة", "الْجِدَار", "الشُّبَّاك", "كَرَاسِيّ", "الْجُدْرَان", "السَّقْف", "لِلْعَالَم")
    + vpb("كُرْسِيّ", "كَرَاسِيّ") + vpb("جِدَار", "جُدْرَان") + vn(10, "m", "عَشَرَة"),
)

# ---------------------------------------------------------------------------- 182
L182 = lesson(
    "Describing the room: opposites",
    "جَدِيد ≠ قَدِيم · وَاسِع ≠ ضَيِّق · نَظِيف ≠ وَسِخ",
    requires=["جديد", "قديم", "واسع", "ضيق", "نظيف", "قريب", "بعيد", "كثير", "قليل"],
    cards=[
        card("Pairs of opposites",
             "A room, a table or a lamp is described with an adjective that comes AFTER the noun and agrees with it. "
             "Learning adjectives in opposite pairs makes them easy to remember. For a feminine noun add ـَة: "
             "نَافِذَة وَاسِعَة, غُرْفَة ضَيِّقَة.",
             tables=[table(["English", "Arabic", "Opposite"],
                           [["new", "جَدِيد", "قَدِيم"], ["wide, spacious", "وَاسِع", "ضَيِّق"],
                            ["clean", "نَظِيف", "وَسِخ"], ["near", "قَرِيب", "بَعِيد"],
                            ["a lot of", "كَثِير", "قَلِيل"], ["tall, long", "طَوِيل", "قَصِير"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "With a plural noun that is not a person (chairs, walls, windows) the adjective is feminine singular: "
             "كَرَاسِيّ جَدِيدَة, نَوَافِذ وَاسِعَة. After كَثِير and قَلِيل the noun is plural.",
             examples=[
                 ex("صَفِّي جَدِيد وَوَاسِع.", "My classroom is new and spacious.", "جَدِيد"),
                 ex("الْغُرْفَة الْقَدِيمَة ضَيِّقَة.", "The old room is narrow.", "ضَيِّقَة"),
                 ex("كَرَاسِيّ الصَّفّ نَظِيفَة.", "The classroom chairs are clean.", "نَظِيفَة"),
                 ex("الْمَكْتَبَة قَرِيبَة وَالْمَطْعَم بَعِيد.", "The library is near and the restaurant is far.", "قَرِيبَة"),
                 ex("فِي الصَّفّ كَثِير مِنَ الْكُتُب.", "There are a lot of books in the classroom.", "كَثِير"),
                 ex("فِي الْغُرْفَة نَوَافِذ قَلِيلَة.", "There are few windows in the room.", "قَلِيلَة"),
             ]),
    ],
    exercises=[
        M("Which word is the opposite of قَدِيم?", "جَدِيد", ["وَاسِع", "قَرِيب", "كَثِير"], "Old ≠ new."),
        M("Which word is the opposite of ضَيِّق?", "وَاسِع", ["نَظِيف", "قَلِيل", "بَعِيد"], "Narrow ≠ wide."),
        M("Which word is the opposite of وَسِخ?", "نَظِيف", ["قَدِيم", "قَرِيب", "قَلِيل"], "Dirty ≠ clean."),
        M("Which word is the opposite of قَلِيل?", "كَثِير", ["جَدِيد", "نَظِيف", "قَصِير"], "Few ≠ many."),
        M("Which means “The old room is narrow”?", "الْغُرْفَة الْقَدِيمَة ضَيِّقَة", ["الْغُرْفَة الْجَدِيدَة ضَيِّقَة", "الْغُرْفَة الْقَدِيمَة وَاسِعَة", "الْغُرْفَة الْقَدِيم ضَيِّق"], "The adjectives agree with غُرْفَة (feminine)."),
        M("Which is right? “The chairs are clean.”", "الْكَرَاسِيّ نَظِيفَة", ["الْكَرَاسِيّ نَظِيفُون", "الْكَرَاسِيّ نَظِيف", "الْكَرَاسِيّ نَظِيفَان"], "A plural thing takes a feminine singular adjective."),
        F("الْمَكْتَبَة ___ وَالْمَطْعَم بَعِيد.", "قَرِيبَة", ["قَرِيب", "قَرِيبُون", "قَرِيبَات"], "مَكْتَبَة is feminine.", tr="The library is near and the restaurant is far."),
        F("صَفِّي جَدِيد وَ___.", "وَاسِع", ["وَاسِعَة", "ضَيِّقَة", "نَظِيفَة"], "صَفّ is masculine.", tr="My classroom is new and spacious."),
        F("فِي الْغُرْفَة نَوَافِذ ___.", "قَلِيلَة", ["قَلِيل", "كَثِير", "قَلِيلُون"], "A plural thing: feminine singular.", tr="There are few windows in the room."),
    ],
    verify=vw("جَدِيد", "قَدِيم", "وَاسِع", "ضَيِّق", "نَظِيف", "وَسِخ", "قَرِيب", "بَعِيد", "كَثِير", "قَلِيل", "طَوِيل", "قَصِير", "نَوَافِذ", "وَاسِعَة", "ضَيِّقَة", "نَظِيفَة", "الْقَدِيمَة", "قَلِيلَة")
    + vf("جَدِيد", "جَدِيدَة") + vf("نَظِيف", "نَظِيفَة") + vf("قَرِيب", "قَرِيبَة") + vpb("نَافِذَة", "نَوَافِذ"),
)

# ---------------------------------------------------------------------------- 183
L183 = lesson(
    "Where is it? Asking for help in class",
    "فِي الْوَسَط · فِي الزَّاوِيَة · عَلَى الْيَمِين · أَطْفِئِ الضَّوْء",
    requires=["وسط", "زاوية", "يمين", "يسار", "أمام", "خلف", "فتح", "رفع"],
    cards=[
        card("Where in the room?",
             "Words for place come before a noun and put it in the genitive (the case ending is not pronounced in this course, "
             "but you will study it soon). You already know أَمَامَ, خَلْفَ, تَحْتَ, فَوْقَ and بَيْنَ. Add these:",
             tables=[table(["English", "Arabic"],
                           [["in the middle of", "فِي وَسَط"], ["in the corner", "فِي الزَّاوِيَة"],
                            ["on the right", "عَلَى الْيَمِين"], ["on the left", "عَلَى الْيَسَار"],
                            ["inside", "دَاخِل"], ["outside", "خَارِج"], ["opposite", "مُقَابِل"]],
                           say=[1], tlit=[1])]),
        card("Polite requests",
             "To ask someone in the room for something, use a command (see Unit 6) with مِنْ فَضْلِكَ (to a man) or "
             "مِنْ فَضْلِكِ (to a woman). Some useful commands: اِفْتَحْ (open), أَغْلِقْ (close), "
             "أَطْفِئِ الضَّوْء (turn off the light), اِرْفَعْ (raise, lift).",
             examples=[
                 ex("الطَّاوِلَة فِي وَسَط الصَّفّ.", "The table is in the middle of the classroom.", "فِي وَسَط"),
                 ex("الْمِكْنَسَة فِي الزَّاوِيَة.", "The broom is in the corner.", "فِي الزَّاوِيَة"),
                 ex("الْخَرِيطَة عَلَى الْيَمِين وَالسَّبُّورَة عَلَى الْيَسَار.", "The map is on the right and the board is on the left.", "عَلَى الْيَمِين"),
                 ex("اِفْتَحِ النَّافِذَة مِنْ فَضْلِكَ.", "Open the window, please. (to a man)", "اِفْتَحِ"),
                 ex("أَغْلِقِي الْبَاب مِنْ فَضْلِكِ.", "Close the door, please. (to a woman)", "أَغْلِقِي"),
                 ex("هَلْ يُمْكِنُنِي أَنْ أَنْقُل طَاوِلَتِي إِلَى الْأَمَام؟", "May I move my desk to the front?", "هَلْ يُمْكِنُنِي"),
             ]),
    ],
    exercises=[
        M("What does فِي وَسَط الصَّفّ mean?", "in the middle of the classroom", ["in front of the classroom", "outside the classroom", "behind the classroom"], "وَسَط = middle."),
        M("Which word means “corner”?", "زَاوِيَة", ["وَسَط", "يَمِين", "دَاخِل"], "فِي الزَّاوِيَة = in the corner."),
        M("What does عَلَى الْيَسَار mean?", "on the left", ["on the right", "in the middle", "outside"], "يَسَار = left."),
        M("Which command means “Close the door” (to a man)?", "أَغْلِقِ الْبَاب", ["اِفْتَحِ الْبَاب", "أَطْفِئِ الْبَاب", "اِرْفَعِ الْبَاب"], "أَغْلِقْ = close."),
        M("Which means “turn off the light”?", "أَطْفِئِ الضَّوْء", ["اِفْتَحِ الضَّوْء", "أَغْلِقِ الضَّوْء", "اِرْفَعِ الضَّوْء"], "أَطْفِئ is the verb for turning off a light."),
        M("How do you say “Open the window, please” to a woman?", "اِفْتَحِي النَّافِذَة مِنْ فَضْلِكِ", ["اِفْتَحِ النَّافِذَة مِنْ فَضْلِكَ", "تَفْتَح النَّافِذَة مِنْ فَضْلِكِ", "فَتَحْتُ النَّافِذَة"], "To a woman: ـِي."),
        F("الْمِكْنَسَة فِي ___.", "الزَّاوِيَة", ["الْوَسَط", "الشُّبَّاك", "الْيَمِين"], "A corner of the room.", tr="The broom is in the corner."),
        F("الْخَرِيطَة عَلَى ___ وَالسَّبُّورَة عَلَى الْيَسَار.", "الْيَمِين", ["الْيَسَار", "الْوَسَط", "الزَّاوِيَة"], "Opposite of left.", tr="The map is on the right and the board is on the left."),
        F("هَلْ ___ أَنْ أَنْقُل طَاوِلَتِي؟", "يُمْكِنُنِي", ["يُمْكِنُكَ", "يُمْكِنُهُ", "أُمْكِن"], "“May I”.", tr="May I move my desk?"),
    ],
    verify=vw("وَسَط", "الزَّاوِيَة", "الْيَمِين", "الْيَسَار", "دَاخِل", "خَارِج", "مُقَابِل", "الْمِكْنَسَة", "أَغْلِقْ", "اِفْتَحْ", "اِرْفَعْ", "أَطْفِئِ", "الضَّوْء", "يُمْكِنُنِي", "الْأَمَام", "أَنْقُل", "أَغْلِقِي")
    + vv("فتح", "imp", anta="اِفْتَحْ", anti="اِفْتَحِي") + vv("رفع", "imp", anta="اِرْفَعْ") + vv("غلق#4", "imp", anta="أَغْلِقْ", anti="أَغْلِقِي")
    + vv("نقل", "pres", ana="أَنْقُل"),
)


# ---------------------------------------------------------------------------- 184
L184 = lesson(
    "Bigger, smaller, newer: the أَفْعَل pattern",
    "هَذَا الصَّفّ أَكْبَر مِنَ الصَّفّ الْقَدِيم",
    requires=["أكبر", "أصغر", "أطول", "أقصر", "أحدث", "أقدم", "أوسع", "أقرب", "أبعد", "من"],
    cards=[
        card("One pattern for “more”",
             "English has two forms: “big, bigger, biggest”. Arabic makes “bigger” with one pattern, أَفْعَل. Take the three "
             "root letters (ك-ب-ر) and put them in the pattern: أَكْبَر. The word for “than” is مِنْ. This form does not change "
             "for masculine or feminine: الْغُرْفَة أَكْبَر مِنَ الْمَكْتَب, وَالصَّفّ أَكْبَر مِنَ الْمَكْتَب.",
             tables=[table(["English", "Adjective", "Comparative"],
                           [["big", "كَبِير", "أَكْبَر"], ["small", "صَغِير", "أَصْغَر"], ["tall, long", "طَوِيل", "أَطْوَل"],
                            ["short", "قَصِير", "أَقْصَر"], ["modern", "حَدِيث", "أَحْدَث"], ["old (things)", "قَدِيم", "أَقْدَم"],
                            ["wide", "وَاسِع", "أَوْسَع"], ["narrow", "ضَيِّق", "أَضْيَق"], ["near", "قَرِيب", "أَقْرَب"],
                            ["far", "بَعِيد", "أَبْعَد"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Comparing two things",
             "Put the two things on each side of the comparative: A + أَفْعَل + مِنْ + B. When the second thing has ال, "
             "مِنْ and ال join into مِنَ الْ.",
             examples=[
                 ex("هَذَا الصَّفّ أَكْبَر مِنَ الصَّفّ الْقَدِيم.", "This classroom is bigger than the old classroom.", "أَكْبَر مِنَ"),
                 ex("الْمَكْتَبَة أَقْرَب مِنَ الْمَطْعَم.", "The library is nearer than the restaurant.", "أَقْرَب"),
                 ex("هَذِهِ الطَّابِعَة أَحْدَث مِنَ الطَّابِعَة الْأُخْرَى.", "This printer is newer than the other printer.", "أَحْدَث"),
                 ex("نَافِذَة الصَّفّ أَوْسَع مِنْ نَافِذَة الْمَكْتَب.", "The classroom window is wider than the office window.", "أَوْسَع"),
                 ex("الطَّاوِلَة الْقَصِيرَة أَقْصَر مِنَ الْكُرْسِيّ.", "The short table is shorter than the chair.", "أَقْصَر"),
                 ex("بَيْتِي أَبْعَد مِنْ بَيْت أَخِي.", "My house is farther than my brother’s house.", "أَبْعَد"),
             ]),
    ],
    exercises=[
        M("What is the comparative of كَبِير?", "أَكْبَر", ["أَكْبَرَة", "كُبْرَى", "كَبِيرَة"], "The pattern أَفْعَل."),
        M("What is the comparative of قَرِيب?", "أَقْرَب", ["أَقْرَبَة", "قُرْبَى", "قَرِيبَة"], "ق-ر-ب → أَقْرَب."),
        M("What is the comparative of طَوِيل?", "أَطْوَل", ["أَوْطَل", "طُولَى", "مُطَوَّل"], "ط-و-ل → أَطْوَل."),
        M("Which word means “than”?", "مِنْ", ["عَنْ", "فِي", "عَلَى"], "أَكْبَر مِنْ = bigger than."),
        M("Does the comparative change for a feminine noun?", "No, it stays أَفْعَل", ["Yes, it adds ـَة", "Yes, it adds ـُون", "Yes, it adds ـَات"], "أَفْعَل is the same for both."),
        M("Which means “The library is nearer than the restaurant”?", "الْمَكْتَبَة أَقْرَب مِنَ الْمَطْعَم", ["الْمَكْتَبَة أَبْعَد مِنَ الْمَطْعَم", "الْمَطْعَم أَقْرَب مِنَ الْمَكْتَبَة", "الْمَكْتَبَة قَرِيبَة وَالْمَطْعَم"], "أَقْرَب = nearer."),
        F("بَيْتِي ___ مِنْ بَيْت أَخِي.", "أَبْعَد", ["بَعِيدَة", "أَبْعَدَة", "بُعْدَى"], "Farther than.", tr="My house is farther than my brother’s house."),
        F("هَذَا الصَّفّ أَكْبَر ___ الصَّفّ الْقَدِيم.", "مِنَ", ["عَنِ", "فِي", "عَلَى"], "“Than” + ال → مِنَ الْ.", tr="This classroom is bigger than the old classroom."),
        F("نَافِذَة الصَّفّ ___ مِنْ نَافِذَة الْمَكْتَب.", "أَوْسَع", ["وَاسِعَة", "وُسْعَى", "أَوْسَعَة"], "Wider than.", tr="The classroom window is wider than the office window."),
    ],
    verify=vw("أَكْبَر", "أَصْغَر", "أَطْوَل", "أَقْصَر", "أَحْدَث", "أَقْدَم", "أَوْسَع", "أَضْيَق", "أَقْرَب", "أَبْعَد", "حَدِيث", "الْأُخْرَى", "بَيْتِي", "بَيْتِ"),
)

# ---------------------------------------------------------------------------- 185
L185 = lesson(
    "More comparatives: doubled letters and special forms",
    "أَقَلّ · أَشَدّ · أَهَمّ · أَقْوَى · أَغْلَى · أَفْضَل · أَسْوَأ",
    requires=["أقل", "أكثر", "أقوى", "أهم", "أشد", "أغلى", "أرخص", "أفضل", "جيد"],
    cards=[
        card("Doubled letters and final و / ي",
             "Some adjectives have a doubled root letter (قَلِيل: ق-ل-ل). In the comparative the two letters join into one "
             "doubled letter: أَقَلّ. A root ending in a weak letter ends in ـَى: قَوِيّ → أَقْوَى, "
             "غَالِي → أَغْلَى. The others follow the pattern you know.",
             tables=[table(["English", "Adjective", "Comparative"],
                           [["few, little", "قَلِيل", "أَقَلّ"], ["many, much", "كَثِير", "أَكْثَر"], ["strong", "قَوِيّ", "أَقْوَى"],
                            ["intense, severe", "شَدِيد", "أَشَدّ"], ["important", "مُهِمّ", "أَهَمّ"], ["expensive", "غَالِي", "أَغْلَى"],
                            ["cheap", "رَخِيص", "أَرْخَص"], ["weak", "ضَعِيف", "أَضْعَف"], ["good", "جَيِّد", "أَفْضَل"],
                            ["bad", "سَيِّئ", "أَسْوَأ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Comparing in practice",
             "For “better”, أَفْضَل (or أَحْسَن) is used, and for “worse” أَسْوَأ. أَكْثَر means “more” and أَقَلّ means “less”, "
             "both with مِنْ.",
             examples=[
                 ex("هَذَا الْحَاسُوب أَغْلَى مِنَ الْحَاسُوب الْقَدِيم.", "This computer is more expensive than the old computer.", "أَغْلَى"),
                 ex("هَذِهِ الْمِرْوَحَة أَقْوَى مِنْ تِلْكَ.", "This fan is stronger than that one.", "أَقْوَى"),
                 ex("الدَّرْس الثَّانِي أَهَمّ مِنَ الدَّرْس الْأَوَّل.", "The second lesson is more important than the first lesson.", "أَهَمّ"),
                 ex("عِنْدِي وَقْت أَقَلّ مِنْ أَمْس.", "I have less time than yesterday.", "أَقَلّ"),
                 ex("الْمَطْعَم الْجَدِيد أَفْضَل مِنَ الْمَطْعَم الْقَدِيم.", "The new restaurant is better than the old restaurant.", "أَفْضَل"),
                 ex("فِي الصَّفّ طُلَّاب أَكْثَر مِنْ أَمْس.", "There are more students in the class than yesterday.", "أَكْثَر"),
             ]),
    ],
    exercises=[
        M("What is the comparative of قَلِيل?", "أَقَلّ", ["أَقْلَى", "قُلْلَى", "قَلِيلَة"], "Doubled letters join: أَقَلّ."),
        M("What is the comparative of مُهِمّ?", "أَهَمّ", ["أَمْهَم", "أَهْمَم", "مُهَمَّى"], "م-ه-م → أَهَمّ."),
        M("What is the comparative of قَوِيّ?", "أَقْوَى", ["أَقْوَيّ", "قُوْيَى", "قُوِيَّة"], "A final weak letter gives ـَى."),
        M("Which word means “cheaper”?", "أَرْخَص", ["أَغْلَى", "أَقْوَى", "أَكْثَر"], "رَخِيص = cheap."),
        M("Which word means “worse”?", "أَسْوَأ", ["أَفْضَل", "أَقَلّ", "أَهَمّ"], "سَيِّئ → أَسْوَأ."),
        M("Which means “more important than”?", "أَهَمّ مِنْ", ["أَقَلّ مِنْ", "أَقْوَى مِنْ", "أَبْعَد مِنْ"], "مُهِمّ → أَهَمّ."),
        F("هَذَا الْحَاسُوب ___ مِنَ الْحَاسُوب الْقَدِيم.", "أَغْلَى", ["غَالِيَة", "أَغْلَيّ", "غُلْيَى"], "More expensive.", tr="This computer is more expensive than the old computer."),
        F("عِنْدِي وَقْت ___ مِنْ أَمْس.", "أَقَلّ", ["أَكْثَر", "كَثِير", "قَلِيلَة"], "Less time.", tr="I have less time than yesterday."),
        F("الْمَطْعَم الْجَدِيد ___ مِنَ الْمَطْعَم الْقَدِيم.", "أَفْضَل", ["جَيِّد", "أَفْضَلَة", "فُضْلَى"], "Better.", tr="The new restaurant is better than the old restaurant."),
    ],
    verify=vw("أَقَلّ", "أَكْثَر", "أَقْوَى", "أَشَدّ", "أَهَمّ", "أَغْلَى", "أَرْخَص", "أَضْعَف", "أَفْضَل", "أَسْوَأ", "قَوِيّ", "شَدِيد", "مُهِمّ", "غَالِي", "رَخِيص", "ضَعِيف", "جَيِّد", "سَيِّئ", "الْمِرْوَحَة", "تِلْكَ"),
)

# ---------------------------------------------------------------------------- 186
L186 = lesson(
    "Older than me, taller than you",
    "أَخِي أَكْبَر مِنِّي · أَنْتَ أَطْوَل مِنْهُ · هِيَ أَصْغَر مِنْكِ",
    requires=["أكبر", "أطول", "أصغر", "أخ", "أخت", "سنة", "من"],
    cards=[
        card("Than me, than you: مِنِّي · مِنْكَ · مِنْهُ",
             "After مِنْ, a pronoun is attached as an ending. The one for “me” is special: مِنْ + ـِي becomes مِنِّي. "
             "The same endings you used with عِنْدَ and مَعَ (عِنْدِي, مَعَكَ) are used here.",
             tables=[table(["English", "Than…", "Example"],
                           [["than me", "مِنِّي", "أَخِي أَكْبَر مِنِّي"], ["than you (man)", "مِنْكَ", "أَخِي أَطْوَل مِنْكَ"],
                            ["than you (woman)", "مِنْكِ", "هِيَ أَصْغَر مِنْكِ"], ["than him", "مِنْهُ", "أَنَا أَقْصَر مِنْهُ"],
                            ["than her", "مِنْهَا", "هُوَ أَكْبَر مِنْهَا"], ["than us", "مِنَّا", "هُمْ أَسْرَع مِنَّا"],
                            ["than them", "مِنْهُمْ", "نَحْنُ أَقْوَى مِنْهُمْ"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("Age and the difference",
             "To say how much older or younger, add بِ and the difference: بِسَنَة (by a year), بِسَنَتَيْن (by two years). "
             "The Arabic for “my elder / younger brother” is أَخِي الْأَكْبَر / أَخِي الْأَصْغَر.",
             examples=[
                 ex("أَخِي أَكْبَر مِنِّي بِسَنَتَيْن.", "My brother is two years older than me.", "أَكْبَر مِنِّي"),
                 ex("أُخْتِي أَصْغَر مِنِّي بِسَنَة.", "My sister is a year younger than me.", "أَصْغَر مِنِّي"),
                 ex("هَلْ أَنْتَ أَكْبَر مِنْ أَخِيكَ؟", "Are you older than your brother? (to a man)", "أَكْبَر مِنْ"),
                 ex("أَنَا أَقْصَر مِنْهُ وَهُوَ أَطْوَل مِنِّي.", "I am shorter than him and he is taller than me.", "مِنْهُ"),
                 ex("أَنْتِ أَسْرَع مِنِّي يَا سَارَة.", "You are faster than me, Sara. (to a woman)", "أَسْرَع مِنِّي"),
                 ex("أَخِي الْأَكْبَر مُهَنْدِس.", "My older brother is an engineer.", "الْأَكْبَر"),
             ]),
    ],
    exercises=[
        M("Which ending means “than me”?", "مِنِّي", ["مِنْكَ", "مِنْهُ", "مِنَّا"], "مِنْ + ـِي → مِنِّي."),
        M("Which means “than her”?", "مِنْهَا", ["مِنْهُ", "مِنْكِ", "مِنْهُمْ"], "ـهَا = her."),
        M("Which means “than you” (to a woman)?", "مِنْكِ", ["مِنْكَ", "مِنِّي", "مِنَّا"], "A kasra for a woman."),
        M("Which means “My brother is older than me by two years”?", "أَخِي أَكْبَر مِنِّي بِسَنَتَيْن", ["أَخِي أَصْغَر مِنِّي بِسَنَتَيْن", "أَخِي أَكْبَر مِنْكَ بِسَنَة", "أَخِي كَبِير بِسَنَتَيْن"], "بِسَنَتَيْن = by two years."),
        M("What does أَخِي الْأَصْغَر mean?", "my younger brother", ["my older brother", "my only brother", "my best brother"], "أَصْغَر = younger."),
        M("Which means “We are stronger than them”?", "نَحْنُ أَقْوَى مِنْهُمْ", ["هُمْ أَقْوَى مِنَّا", "نَحْنُ أَقْوَى مِنِّي", "أَنَا أَقْوَى مِنْهُمْ"], "مِنْهُمْ = than them."),
        F("أَنَا أَقْصَر ___ وَهُوَ أَطْوَل مِنِّي.", "مِنْهُ", ["مِنِّي", "مِنْكِ", "مِنَّا"], "Than him.", tr="I am shorter than him and he is taller than me."),
        F("أُخْتِي أَصْغَر مِنِّي ___ سَنَة.", "بِ", ["فِي", "عَنْ", "إِلَى"], "“By a year”.", tr="My sister is a year younger than me."),
        F("أَنْتِ أَسْرَع ___ يَا سَارَة.", "مِنِّي", ["مِنْهُ", "مِنْكَ", "مِنْهُمْ"], "Than me.", tr="You are faster than me, Sara."),
    ],
    verify=vw("مِنِّي", "مِنْكَ", "مِنْكِ", "مِنْهُ", "مِنْهَا", "مِنَّا", "مِنْهُمْ", "بِسَنَة", "بِسَنَتَيْن", "أَخِيكَ", "الْأَكْبَر", "الْأَصْغَر", "أَسْرَع", "مُهَنْدِس", "سَارَة"),
)

# ---------------------------------------------------------------------------- 187
L187 = lesson(
    "The biggest, the tallest: the superlative",
    "الْأَكْبَر · الْأَطْوَل · أَكْبَر مَدِينَة · أَطْوَل نَهْر",
    requires=["أكبر", "أطول", "أول", "نهر", "مدينة", "عالم", "طالب"],
    cards=[
        card("Two ways to say “the most”",
             "The same pattern gives the superlative in two ways. (1) With ال after a noun, or alone: الطَّالِب الْأَطْوَل, "
             "هُوَ الْأَطْوَل. (2) Without ال, in front of a singular noun without ال: أَطْوَل نَهْر, أَكْبَر مَدِينَة "
             "(“a longest river”, meaning “the longest river”). A place is added with فِي or مِنْ: فِي الصَّفّ, مِنْ بَيْن الطُّلَّاب.",
             tables=[table(["English", "Arabic"],
                           [["the tallest student", "الطَّالِب الْأَطْوَل"], ["he is the tallest", "هُوَ الْأَطْوَل"],
                            ["the biggest city", "أَكْبَر مَدِينَة"], ["the longest river", "أَطْوَل نَهْر"],
                            ["the oldest in the school", "الْأَقْدَم فِي الْمَدْرَسَة"]],
                           say=[1], tlit=[1])]),
        card("In sentences",
             "Some feminine superlatives have their own form, for example الْكُبْرَى (the greatest) in the name "
             "الصَّحْرَاء الْكُبْرَى (the Sahara). In everyday speech the one form الْأَكْبَر is usual.",
             examples=[
                 ex("مَنِ الْأَطْوَل فِي الصَّفّ؟", "Who is the tallest in the class?", "الْأَطْوَل"),
                 ex("النِّيل أَطْوَل نَهْر فِي أَفْرِيقِيَا.", "The Nile is the longest river in Africa.", "أَطْوَل نَهْر"),
                 ex("الْمُحِيط الْهَادِئ أَكْبَر مُحِيط فِي الْعَالَم.", "The Pacific Ocean is the biggest ocean in the world.", "أَكْبَر مُحِيط"),
                 ex("هَذِهِ أَكْبَر قَاعَة فِي الْمَدْرَسَة.", "This is the biggest hall in the school.", "أَكْبَر قَاعَة"),
                 ex("خَالِد هُوَ الْأَصْغَر فِي الصَّفّ.", "Khalid is the youngest in the class.", "الْأَصْغَر"),
                 ex("هَذَا أَفْضَل مَطْعَم فِي الْمَدِينَة.", "This is the best restaurant in the city.", "أَفْضَل مَطْعَم"),
             ]),
    ],
    exercises=[
        M("Which means “the tallest student”?", "الطَّالِب الْأَطْوَل", ["أَطْوَل طَالِب مِنْ", "الطَّالِب أَطْوَل مِنْ", "طَالِب طَوِيل"], "ال + noun, then الْأَطْوَل."),
        M("Which means “the biggest city”?", "أَكْبَر مَدِينَة", ["الْمَدِينَة أَكْبَر مِنْ", "مَدِينَة كَبِيرَة", "الْمَدِينَة الْكَبِير"], "أَفْعَل + a singular noun without ال."),
        M("How do you say “the longest river”?", "أَطْوَل نَهْر", ["نَهْر أَطْوَل مِنْ", "أَطْوَل النَّهْر", "النَّهْر طَوِيل"], "أَفْعَل + noun without ال."),
        M("Which means “Who is the tallest in the class?”", "مَنِ الْأَطْوَل فِي الصَّفّ؟", ["مَنِ الطَّوِيل فِي الصَّفّ؟", "مَاذَا الْأَطْوَل فِي الصَّفّ؟", "هَلِ الْأَطْوَل فِي الصَّفّ؟"], "مَنْ + الْأَطْوَل."),
        M("Which means “Khalid is the youngest in the class”?", "خَالِد هُوَ الْأَصْغَر فِي الصَّفّ", ["خَالِد هُوَ أَصْغَر مِنَ الصَّفّ", "خَالِد صَغِير فِي الصَّفّ", "خَالِد أَكْبَر فِي الصَّفّ"], "الْأَصْغَر = the youngest."),
        M("What does the word فِي mean in “the best restaurant IN the city”?", "in", ["than", "with", "to"], "فِي الْمَدِينَة = in the city."),
        F("هَذَا ___ مَطْعَم فِي الْمَدِينَة.", "أَفْضَل", ["الْأَفْضَل", "فَاضِل", "أَفْضَلَة"], "Best + noun without ال.", tr="This is the best restaurant in the city."),
        F("النِّيل ___ نَهْر فِي أَفْرِيقِيَا.", "أَطْوَل", ["الْأَطْوَل", "طَوِيل", "طُولَى"], "Longest river.", tr="The Nile is the longest river in Africa."),
        F("خَالِد هُوَ ___ فِي الصَّفّ.", "الْأَصْغَر", ["أَصْغَر", "صَغِيرَة", "الصَّغِير مِنْ"], "ال + أَفْعَل on its own.", tr="Khalid is the youngest in the class."),
    ],
    verify=vw("الْأَطْوَل", "الْأَكْبَر", "الْأَصْغَر", "الْأَقْدَم", "النِّيل", "أَفْرِيقِيَا", "الْمُحِيط", "الْهَادِئ", "الْكُبْرَى", "الصَّحْرَاء", "قَاعَة", "خَالِد"),
)

# ---------------------------------------------------------------------------- 188
L188 = lesson(
    "Colours, and “redder than”",
    "أَحْمَر · أَخْضَر · أَزْرَق · أَكْثَر اِحْمِرَارًا مِنْ",
    requires=["أحمر", "أخضر", "أزرق", "أصفر", "أبيض", "أسود", "لون", "بني", "رمادي"],
    cards=[
        card("Colours agree with the noun",
             "Most basic colours use the pattern أَفْعَل for a masculine noun and a pattern ending in ـَاء for a feminine one: "
             "بَاب أَحْمَر, سَيَّارَة حَمْرَاء. Colours that end in ـِيّ (بُنِّيّ, رَمَادِيّ) take ـِيَّة for the feminine.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["red", "أَحْمَر", "حَمْرَاء"], ["green", "أَخْضَر", "خَضْرَاء"], ["blue", "أَزْرَق", "زَرْقَاء"],
                            ["yellow", "أَصْفَر", "صَفْرَاء"], ["white", "أَبْيَض", "بَيْضَاء"], ["black", "أَسْوَد", "سَوْدَاء"],
                            ["brown", "بُنِّيّ", "بُنِّيَّة"], ["grey", "رَمَادِيّ", "رَمَادِيَّة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("More or less of a colour",
             "A colour cannot take the أَفْعَل pattern again, so Arabic says “more of the colour”: أَكْثَر + the noun of the "
             "colour with ـًا, followed by مِنْ. The nouns are: اِحْمِرَار (redness), خُضْرَة (greenness), زُرْقَة (blueness), "
             "اِصْفِرَار (yellowness), بَيَاض (whiteness). For “less”, use أَقَلّ.",
             examples=[
                 ex("لَوْن الْجُدْرَان أَبْيَض وَلَوْن الْبَاب بُنِّيّ.", "The colour of the walls is white and the colour of the door is brown.", "أَبْيَض"),
                 ex("عِنْدِي سَيَّارَة حَمْرَاء.", "I have a red car.", "حَمْرَاء"),
                 ex("هَذَا الْقَمِيص أَكْثَر اِحْمِرَارًا مِنَ الْقَمِيص الْآخَر.", "This shirt is redder than the other shirt.", "أَكْثَر اِحْمِرَارًا"),
                 ex("السَّمَاء الْيَوْم أَكْثَر زُرْقَةً مِنْ أَمْس.", "The sky today is bluer than yesterday.", "أَكْثَر زُرْقَةً"),
                 ex("هَذِهِ الْحَدِيقَة أَكْثَر خُضْرَةً مِنَ الْحَدِيقَة الْأُخْرَى.", "This garden is greener than the other garden.", "أَكْثَر خُضْرَةً"),
                 ex("الْحَائِط الْقَدِيم أَقَلّ بَيَاضًا مِنَ الْحَائِط الْجَدِيد.", "The old wall is less white than the new wall.", "أَقَلّ بَيَاضًا"),
             ]),
    ],
    exercises=[
        M("Which is the feminine of أَحْمَر?", "حَمْرَاء", ["أَحْمَرَة", "حَمِيرَة", "حُمْرَى"], "The feminine pattern ends in ـَاء."),
        M("Which is the feminine of أَزْرَق?", "زَرْقَاء", ["أَزْرَقَة", "زُرْقَة", "زَرِيقَة"], "زَرْقَاء."),
        M("Which colour is بَيْضَاء?", "white (feminine)", ["black (feminine)", "red (masculine)", "green (feminine)"], "بَيْضَاء = white."),
        M("Which means “a red car”?", "سَيَّارَة حَمْرَاء", ["سَيَّارَة أَحْمَر", "سَيَّارَة حَمْرَاءَات", "حَمْرَاء سَيَّارَة"], "Feminine noun, feminine colour, colour after the noun."),
        M("Which means “bluer than”?", "أَكْثَر زُرْقَةً مِنْ", ["أَزْرَق مِنْ", "زَرْقَاء مِنْ", "أَقَلّ بَيَاضًا مِنْ"], "أَكْثَر + noun of the colour."),
        M("Which means “less white than”?", "أَقَلّ بَيَاضًا مِنْ", ["أَكْثَر بَيَاضًا مِنْ", "أَبْيَض مِنْ", "أَقَلّ سَوَادًا مِنْ"], "أَقَلّ = less."),
        F("لَوْن الْجُدْرَان ___ وَلَوْن الْبَاب بُنِّيّ.", "أَبْيَض", ["بَيْضَاء", "بَيَاض", "أَبْيَضَة"], "لَوْن is masculine.", tr="The colour of the walls is white and the colour of the door is brown."),
        F("عِنْدِي سَيَّارَة ___.", "حَمْرَاء", ["أَحْمَر", "حُمْرَة", "أَحْمَرَة"], "سَيَّارَة is feminine.", tr="I have a red car."),
        F("السَّمَاء الْيَوْم أَكْثَر ___ مِنْ أَمْس.", "زُرْقَةً", ["أَزْرَق", "زَرْقَاء", "زُرْقَة الْ"], "أَكْثَر + a noun with ـًا.", tr="The sky today is bluer than yesterday."),
    ],
    verify=vw("أَحْمَر", "حَمْرَاء", "أَخْضَر", "خَضْرَاء", "أَزْرَق", "زَرْقَاء", "أَصْفَر", "صَفْرَاء", "أَبْيَض", "بَيْضَاء", "أَسْوَد", "سَوْدَاء", "بُنِّيّ", "بُنِّيَّة", "رَمَادِيّ", "رَمَادِيَّة",
              "اِحْمِرَارًا", "زُرْقَةً", "خُضْرَةً", "بَيَاضًا", "السَّمَاء", "الْقَمِيص"),
)


# ---------------------------------------------------------------------------- 189
L189 = lesson(
    "Places around the school",
    "الْبَوَّابَة · الْمَكْتَبَة · الْمَسْجِد · الْكَنِيسَة · الْمَلْعَب · مَكْتَب الْبَرِيد",
    requires=["بوابة", "مكتبة", "مطعم", "مسجد", "كنيسة", "ملعب", "مركز", "رياضي", "بريد", "عيادة", "متجر", "ساحة"],
    cards=[
        card("A school and what is around it",
             "A big school or campus has places for study, food, sport and prayer. The names with two nouns are "
             "the iḍāfa you know: مَكْتَب الْبَرِيد is “the office of the post”, so the first noun has no ال: "
             "مَكْتَب الْبَرِيد, not الْمَكْتَب الْبَرِيد.",
             tables=[table(["English", "Arabic"],
                           [["the gate", "الْبَوَّابَة"], ["the library", "الْمَكْتَبَة"], ["the restaurant", "الْمَطْعَم"],
                            ["the mosque", "الْمَسْجِد"], ["the church", "الْكَنِيسَة"], ["the sports field", "الْمَلْعَب"],
                            ["the sports centre", "الْمَرْكَز الرِّيَاضِيّ"], ["the post office", "مَكْتَب الْبَرِيد"],
                            ["the clinic", "الْعِيَادَة"], ["the store", "الْمَتْجَر"], ["the courtyard", "السَّاحَة"]],
                           say=[1], tlit=[1])]),
        card("Where is it?",
             "Use the place words you know to say where each building is.",
             examples=[
                 ex("الْبَوَّابَة أَمَام الْمَدْرَسَة.", "The gate is in front of the school.", "الْبَوَّابَة"),
                 ex("الْمَكْتَبَة بِجَانِب الْمَسْجِد.", "The library is next to the mosque.", "بِجَانِب"),
                 ex("الْكَنِيسَة قَرِيبَة مِنَ السَّاحَة.", "The church is near the courtyard.", "قَرِيبَة مِنَ"),
                 ex("الْمَلْعَب خَلْف الْمَرْكَز الرِّيَاضِيّ.", "The field is behind the sports centre.", "الْمَلْعَب"),
                 ex("مَكْتَب الْبَرِيد بَيْنَ الْعِيَادَة وَالْمَتْجَر.", "The post office is between the clinic and the shop.", "مَكْتَب الْبَرِيد"),
                 ex("أَتَغَدَّى فِي الْمَطْعَم كُلّ يَوْم.", "I have lunch in the restaurant every day.", "الْمَطْعَم"),
             ]),
    ],
    exercises=[
        M("What does مَكْتَب الْبَرِيد mean?", "the post office", ["the library", "the clinic", "the shop"], "مَكْتَب = office; بَرِيد = mail."),
        M("Which place is for prayer for Christians?", "الْكَنِيسَة", ["الْمَسْجِد", "الْمَلْعَب", "الْمَطْعَم"], "كَنِيسَة = church."),
        M("Which word means “the gate”?", "الْبَوَّابَة", ["السَّاحَة", "الْعِيَادَة", "الْمَتْجَر"], "بَوَّابَة = gate."),
        M("Which place would you go to for football?", "الْمَلْعَب", ["الْمَكْتَبَة", "مَكْتَب الْبَرِيد", "الْعِيَادَة"], "مَلْعَب = field."),
        M("Which is right? “the post office”", "مَكْتَب الْبَرِيد", ["الْمَكْتَب الْبَرِيد", "مَكْتَب بَرِيد الْ", "الْمَكْتَب بَرِيد"], "The first noun of an iḍāfa has no ال."),
        M("Which means “The library is next to the mosque”?", "الْمَكْتَبَة بِجَانِب الْمَسْجِد", ["الْمَسْجِد بِجَانِب الْمَكْتَبَة الْمَسْجِد", "الْمَكْتَبَة خَلْف الْمَسْجِد", "الْمَكْتَبَة فِي الْمَسْجِد"], "بِجَانِب = next to."),
        F("الْمَلْعَب ___ الْمَرْكَز الرِّيَاضِيّ.", "خَلْف", ["أَمَام", "تَحْتَ", "فَوْقَ"], "Behind.", tr="The field is behind the sports centre."),
        F("مَكْتَب الْبَرِيد ___ الْعِيَادَة وَالْمَتْجَر.", "بَيْنَ", ["فِي", "عَلَى", "مَعَ"], "Between two things.", tr="The post office is between the clinic and the shop."),
        F("أَتَغَدَّى فِي ___ كُلّ يَوْم.", "الْمَطْعَم", ["الْمَسْجِد", "الْبَوَّابَة", "الْعِيَادَة"], "Where you eat.", tr="I have lunch in the restaurant every day."),
    ],
    verify=vw("الْبَوَّابَة", "الْمَكْتَبَة", "الْمَطْعَم", "الْمَسْجِد", "الْكَنِيسَة", "الْمَلْعَب", "الْمَرْكَز", "الرِّيَاضِيّ", "مَكْتَب", "الْبَرِيد", "الْعِيَادَة", "الْمَتْجَر", "السَّاحَة", "بِجَانِب", "أَتَغَدَّى"),
)

# ---------------------------------------------------------------------------- 190
L190 = lesson(
    "A place where…: what is it for?",
    "مَكَان يَلْعَب فِيهِ الْأَوْلَاد · مَكَان نَشْتَرِي مِنْهُ",
    requires=["مكان", "لعب", "صلى", "كتاب", "شرب", "أكل", "ولد", "ناس"],
    cards=[
        card("Describing a place with a verb",
             "To say “a place where…”, put a verb sentence straight after the word مَكَان, with no word for “where”. "
             "A pronoun then points back to the place: فِيهِ (in it), مِنْهُ (from it). مَكَان يَلْعَب فِيهِ الْأَوْلَاد "
             "= “a place in which the children play”. The verb stays singular before a plural subject.",
             tables=[table(["English", "Arabic"],
                           [["a place where children play", "مَكَان يَلْعَب فِيهِ الْأَوْلَاد"],
                            ["a place where people eat", "مَكَان يَأْكُل فِيهِ النَّاس"],
                            ["a place where Muslims pray", "مَكَان يُصَلِّي فِيهِ الْمُسْلِمُون"],
                            ["a place where we buy things", "مَكَان نَشْتَرِي مِنْهُ الْأَشْيَاء"]],
                           say=[1], tlit=[1])]),
        card("Riddles: “I am a place…”",
             "Answer these riddles with a place from the last lesson.",
             examples=[
                 ex("أَنَا مَكَان فِيهِ كُتُب كَثِيرَة.", "I am a place with many books in it. (the library)", "فِيهِ"),
                 ex("أَنَا مَكَان يَلْعَب فِيهِ الْأَوْلَاد كُرَة الْقَدَم.", "I am a place where the boys play football. (the field)", "يَلْعَب فِيهِ"),
                 ex("أَنَا مَكَان يَأْكُل فِيهِ النَّاس.", "I am a place where people eat. (the restaurant)", "يَأْكُل فِيهِ"),
                 ex("أَنَا مَكَان يُصَلِّي فِيهِ الْمَسِيحِيُّون.", "I am a place where Christians pray. (the church)", "يُصَلِّي فِيهِ"),
                 ex("أَنَا مَكَان نُرْسِل مِنْهُ رِسَالَة.", "I am a place from which we send a letter. (the post office)", "مِنْهُ"),
                 ex("أَنَا مَكَان يَدْخُل مِنْهُ الطُّلَّاب وَيَخْرُجُون.", "I am a place through which the students enter and leave. (the gate)", "يَدْخُل مِنْهُ"),
             ]),
    ],
    exercises=[
        M("What does فِيهِ mean in مَكَان فِيهِ كُتُب?", "in it", ["from it", "with him", "on it"], "فِي + ـهُ."),
        M("What does مِنْهُ mean in مَكَان نُرْسِل مِنْهُ رِسَالَة?", "from it", ["in it", "to him", "than it"], "مِنْ + ـهُ."),
        M("Which place is “a place where children play”?", "الْمَلْعَب", ["الْمَكْتَبَة", "مَكْتَب الْبَرِيد", "الْعِيَادَة"], "يَلْعَب = plays."),
        M("Which place is “a place where people eat”?", "الْمَطْعَم", ["الْمَسْجِد", "الْبَوَّابَة", "السَّاحَة"], "يَأْكُل = eats."),
        M("Which means “a place where Christians pray”?", "مَكَان يُصَلِّي فِيهِ الْمَسِيحِيُّون", ["مَكَان يُصَلِّي الْمَسِيحِيُّون", "مَكَان فِيهِ كُتُب كَثِيرَة", "مَكَان يَأْكُل فِيهِ الْمَسِيحِيُّون"], "A verb, فِيهِ, then the people."),
        M("Why is the verb يَلْعَب singular in يَلْعَب فِيهِ الْأَوْلَاد?", "A verb before its subject stays singular", ["Because الْأَوْلَاد is feminine", "Because it is a question", "Because it is the past"], "The verb comes first, so it stays singular."),
        F("أَنَا مَكَان ___ كُتُب كَثِيرَة.", "فِيهِ", ["مِنْهُ", "عَلَيْهِ", "مَعَهُ"], "In it.", tr="I am a place with many books in it."),
        F("أَنَا مَكَان يَأْكُل ___ النَّاس.", "فِيهِ", ["مِنْهُ", "بِهِ", "لَهُ"], "A place in which people eat.", tr="I am a place where people eat."),
        F("أَنَا مَكَان نُرْسِل ___ رِسَالَة.", "مِنْهُ", ["فِيهِ", "عَنْهُ", "إِلَيْهِ"], "We send from it.", tr="I am a place from which we send a letter."),
    ],
    verify=vw("فِيهِ", "مِنْهُ", "يَلْعَب", "يَأْكُل", "يُصَلِّي", "الْمُسْلِمُون", "الْمَسِيحِيُّون", "نَشْتَرِي", "نُرْسِل", "الْأَوْلَاد", "الْأَشْيَاء", "يَدْخُل", "يَخْرُجُون")
    + vv("لعب", "pres", huwa="يَلْعَب") + vv("رسل#4", "pres", nahnu="نُرْسِل") + vv("دخل", "pres", huwa="يَدْخُل") + vv("خرج", "pres", hum="يَخْرُجُون"),
)

# ---------------------------------------------------------------------------- 191
L191 = lesson(
    "Using services: post, cash, clinic",
    "أُرِيد أَنْ أُرْسِل طَرْدًا · أَسْحَب نُقُودًا · مَفْتُوح / مُغْلَق",
    requires=["بريد", "طرد", "طابع", "عيادة", "متجر", "مفتوح", "غلق", "سحب"],
    cards=[
        card("What you do at each place",
             "Each service has its own verb. Notice that the post office and the bank machine use verbs you can put "
             "after أُرِيد أَنْ (“I want to…”).",
             tables=[table(["English", "Arabic"],
                           [["to send a letter", "أُرْسِل رِسَالَة"], ["to send a parcel", "أُرْسِل طَرْدًا"],
                            ["to buy stamps", "أَشْتَرِي طَوَابِع"], ["to withdraw money", "أَسْحَب نُقُودًا"],
                            ["the cash machine", "الصَّرَّاف الْآلِيّ"], ["to see the doctor", "أُقَابِل الطَّبِيب"],
                            ["open", "مَفْتُوح"], ["closed", "مُغْلَق"]],
                           say=[1], tlit=[1])]),
        card("At the counter",
             "To ask whether a place is open, use هَلْ and مَفْتُوح / مَفْتُوحَة. Opening hours use مِنَ السَّاعَة … إِلَى "
             "السَّاعَة …",
             examples=[
                 ex("أُرِيد أَنْ أُرْسِل رِسَالَة إِلَى أُمِّي.", "I want to send a letter to my mother.", "أُرْسِل"),
                 ex("كَمْ ثَمَن هَذَا الطَّابِع؟", "How much does this stamp cost?", "الطَّابِع"),
                 ex("أَسْحَب نُقُودًا مِنَ الصَّرَّاف الْآلِيّ.", "I take out money from the cash machine.", "أَسْحَب"),
                 ex("هَلِ الْعِيَادَة مَفْتُوحَة الْيَوْم؟", "Is the clinic open today?", "مَفْتُوحَة"),
                 ex("مَكْتَب الْبَرِيد مَفْتُوح مِنَ السَّاعَة التَّاسِعَة إِلَى الْخَامِسَة.", "The post office is open from nine to five.", "مَفْتُوح"),
                 ex("الْمَتْجَر مُغْلَق يَوْم الْجُمْعَة.", "The shop is closed on Friday.", "مُغْلَق"),
             ]),
    ],
    exercises=[
        M("What does أَسْحَب نُقُودًا mean?", "I withdraw money", ["I send money", "I count money", "I lose money"], "سَحَبَ = to pull, withdraw."),
        M("Which place do you use to send a parcel?", "مَكْتَب الْبَرِيد", ["الْعِيَادَة", "الْمَلْعَب", "الْمَسْجِد"], "طَرْد = parcel."),
        M("What does مُغْلَق mean?", "closed", ["open", "far", "new"], "أَغْلَقَ = to close."),
        M("Which means “Is the clinic open today?” (a feminine noun)", "هَلِ الْعِيَادَة مَفْتُوحَة الْيَوْم؟", ["هَلِ الْعِيَادَة قَرِيبَة أَمْس؟", "هَلِ الْعِيَادَة مَفْتُوح الْيَوْم؟", "هَلِ الْعِيَادَة تَفْتَح؟"], "عِيَادَة is feminine: مَفْتُوحَة."),
        M("Which means “I want to send a letter to my mother”?", "أُرِيد أَنْ أُرْسِل رِسَالَة إِلَى أُمِّي", ["أُرِيد أَنْ أَقْرَأ رِسَالَة مِنْ أُمِّي", "أُرْسِل رِسَالَة أُمِّي", "أُرِيد رِسَالَة"], "أُرْسِل = I send."),
        M("What does the question كَمْ ثَمَن هَذَا الطَّابِع؟ ask?", "the price of a stamp", ["where the stamp is", "who sent the stamp", "when the stamp arrives"], "ثَمَن = price."),
        F("الْمَتْجَر ___ يَوْم الْجُمْعَة.", "مُغْلَق", ["مَفْتُوحَة", "مَفْتُوح", "الْمُغْلَق"], "مَتْجَر is masculine.", tr="The shop is closed on Friday."),
        F("مَكْتَب الْبَرِيد ___ مِنَ السَّاعَة التَّاسِعَة.", "مَفْتُوح", ["مَفْتُوحَة", "الْمَفْتُوح", "فَتَحَ"], "مَكْتَب is masculine.", tr="The post office is open from nine."),
        F("أَسْحَب ___ مِنَ الصَّرَّاف الْآلِيّ.", "نُقُودًا", ["طَوَابِع", "رَسَائِل", "الطَّرْد"], "What you withdraw.", tr="I withdraw money from the cash machine."),
    ],
    verify=vw("أُرْسِل", "طَرْدًا", "طَوَابِع", "أَشْتَرِي", "أَسْحَب", "نُقُودًا", "الصَّرَّاف", "الْآلِيّ", "أُقَابِل", "الطَّبِيب", "مَفْتُوح", "مَفْتُوحَة", "مُغْلَق", "الطَّابِع", "ثَمَن", "التَّاسِعَة", "الْخَامِسَة")
    + vv("رسل#4", "pres", ana="أُرْسِل") + vv("سحب", "pres", ana="أَسْحَب") + vv("قبل#3", "pres", ana="أُقَابِل"),
)


# ---------------------------------------------------------------------------- 192
L192 = lesson(
    "The genitive case: after a preposition and in the iḍāfa",
    "فِي الْبَيْتِ · بَابُ الْبَيْتِ · مِنْ مَدِينَةٍ",
    requires=["في", "من", "على", "إلى", "بيت", "باب", "مدينة", "كتاب", "طالب", "عن"],
    cards=[
        card("Three cases, three endings",
             "In careful Arabic the last letter of a noun shows its job in the sentence. The subject takes ـُ (nominative), the "
             "object takes ـَ (accusative) and a noun after a preposition takes ـِ (genitive). A noun without ال adds a nunation "
             "sign (tanwīn): ـٌ, ـً, ـٍ. Until now this course has left these endings out, as Arabic speakers do when they pause. "
             "From here on you will see them in some lessons, so that you can read fully vowelled texts.",
             tables=[table(["Case", "With ال", "Without ال"],
                           [["nominative (subject)", "الْبَيْتُ", "بَيْتٌ"], ["accusative (object)", "الْبَيْتَ", "بَيْتًا"],
                            ["genitive (after a preposition)", "الْبَيْتِ", "بَيْتٍ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Where the genitive appears",
             "Two places put a noun in the genitive. First, a noun after a preposition (فِي, مِنْ, عَلَى, إِلَى, عَنْ, مَعَ). "
             "Second, the owner in an iḍāfa: the first noun has no ال and no tanwīn, and the second noun is genitive. "
             "An adjective copies the case of its noun.",
             examples=[
                 ex("الْكِتَابُ فِي الْبَيْتِ.", "The book is in the house.", "فِي الْبَيْتِ"),
                 ex("الْقَلَمُ عَلَى الْمَكْتَبِ.", "The pen is on the desk.", "عَلَى الْمَكْتَبِ"),
                 ex("أَنَا مِنْ مَدِينَةٍ كَبِيرَةٍ.", "I am from a big city.", "مِنْ مَدِينَةٍ كَبِيرَةٍ"),
                 ex("بَابُ الْبَيْتِ كَبِيرٌ.", "The door of the house is big.", "بَابُ الْبَيْتِ"),
                 ex("كِتَابُ الطَّالِبِ جَدِيدٌ.", "The student’s book is new.", "كِتَابُ الطَّالِبِ"),
                 ex("مَكْتَبُ الْمُدِيرِ فِي الْبَيْتِ الْقَدِيمِ.", "The director’s desk is in the old house.", "الْقَدِيمِ"),
             ]),
    ],
    exercises=[
        M("Which case does a noun take after a preposition such as فِي?", "the genitive (ـِ)", ["the nominative (ـُ)", "the accusative (ـَ)", "no case at all"], "Prepositions are followed by the genitive."),
        M("Which is the genitive of الْبَيْتُ?", "الْبَيْتِ", ["الْبَيْتَ", "الْبَيْتُ", "بَيْتٌ"], "Genitive: a kasra."),
        M("Which is the genitive of بَيْتٌ (without ال)?", "بَيْتٍ", ["بَيْتٌ", "بَيْتًا", "الْبَيْتِ"], "Genitive with tanwīn: ـٍ."),
        M("Which means “the door of the house”?", "بَابُ الْبَيْتِ", ["بَابٌ الْبَيْتِ", "الْبَابُ الْبَيْتِ", "بَابُ الْبَيْتُ"], "First noun: no ال, no tanwīn. Second noun: genitive."),
        M("Which sentence is correct? “The book is in the house.”", "الْكِتَابُ فِي الْبَيْتِ", ["الْكِتَابُ فِي الْبَيْتُ", "الْكِتَابَ فِي الْبَيْتِ", "الْكِتَابُ فِي الْبَيْتَ"], "Subject: ـُ. After فِي: ـِ."),
        M("In كِتَابُ الطَّالِبِ, which word is in the genitive?", "الطَّالِبِ", ["كِتَابُ", "both words", "neither word"], "The owner is genitive."),
        M("Why does كِتَابُ have no tanwīn in كِتَابُ الطَّالِبِ?", "it is the first noun of an iḍāfa", ["it is feminine", "it is plural", "it follows a verb"], "The first noun of an iḍāfa takes no tanwīn and no ال."),
        F("كِتَابُ ___ جَدِيدٌ.", "الطَّالِبِ", ["الطَّالِبُ", "الطَّالِبَ", "طَالِبٌ"], "The owner in an iḍāfa is genitive and has ال.", tr="The student’s book is new."),
        F("الْقَلَمُ عَلَى ___.", "الْمَكْتَبِ", ["الْمَكْتَبُ", "الْمَكْتَبَ", "مَكْتَبٌ"], "After عَلَى: genitive.", tr="The pen is on the desk."),
    ],
    verify=vw("الْبَيْت", "بَيْت", "الْمَكْتَب", "الْكِتَاب", "الطَّالِب", "الْمُدِير", "مَدِينَة", "كَبِير", "جَدِيد", "الْقَدِيم", "الْقَلَم", "بَاب"),
)

# ---------------------------------------------------------------------------- 193
L193 = lesson(
    "The genitive of the dual and the plural",
    "مَعَ الطَّالِبَيْنِ · مِنَ الْمُهَنْدِسِينَ · بَيْتُ الْمُدَرِّسَاتِ",
    requires=["مع", "من", "طالب", "مدرس", "مهندس", "طاولة", "رسالة"],
    cards=[
        card("Two forms, not three",
             "The dual and the sound masculine plural have only two forms. The subject form is ـَانِ (dual) or ـُونَ (plural). "
             "After a preposition, as the second noun of an iḍāfa and as an object, the form is ـَيْنِ (dual) or ـِينَ (plural). "
             "You have met these forms in earlier units. Now you know why they change.",
             tables=[table(["Singular", "Dual (subject)", "Dual (after a preposition)"],
                           [["طَالِب", "طَالِبَانِ", "طَالِبَيْنِ"], ["مُدَرِّس", "مُدَرِّسَانِ", "مُدَرِّسَيْنِ"],
                            ["طَالِبَة", "طَالِبَتَانِ", "طَالِبَتَيْنِ"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False),
                    table(["Singular", "Plural (subject)", "Plural (after a preposition)"],
                          [["طَالِب", "طَالِبُونَ", "طَالِبِينَ"], ["مُهَنْدِس", "مُهَنْدِسُونَ", "مُهَنْدِسِينَ"]],
                          say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("The sound feminine plural",
             "The sound feminine plural (ـَات) has two forms too. The subject form ends in ـَاتُ. After a preposition, and as an object, "
             "it ends in ـَاتِ with a kasra, not a fatḥa.",
             examples=[
                 ex("أَنَا مَعَ الطَّالِبَيْنِ فِي الْمَكْتَبَةِ.", "I am with the two students in the library.", "الطَّالِبَيْنِ"),
                 ex("الرِّسَالَةُ مِنَ الْمُهَنْدِسِينَ.", "The letter is from the engineers.", "الْمُهَنْدِسِينَ"),
                 ex("الْكُتُبُ عَلَى مَكْتَبِ الْمُدَرِّسَيْنِ.", "The books are on the two teachers’ desk.", "الْمُدَرِّسَيْنِ"),
                 ex("الْكُرَّاسَةُ عَلَى طَاوِلَةِ الطَّالِبَتَيْنِ.", "The notebook is on the two female students’ table.", "الطَّالِبَتَيْنِ"),
                 ex("بَيْتُ الْمُدَرِّسَاتِ قَرِيبٌ مِنَ الْجَامِعَةِ.", "The female teachers’ house is near the university.", "الْمُدَرِّسَاتِ"),
                 ex("أَنَا فِي الصَّفِّ مَعَ الطَّالِبَاتِ.", "I am in class with the female students.", "الطَّالِبَاتِ"),
             ]),
    ],
    exercises=[
        M("Which is the dual of طَالِب after a preposition?", "طَالِبَيْنِ", ["طَالِبَانِ", "طَالِبِينَ", "طَالِبُونَ"], "After a preposition: ـَيْنِ."),
        M("Which is the plural of مُهَنْدِس after a preposition?", "مُهَنْدِسِينَ", ["مُهَنْدِسُونَ", "مُهَنْدِسَيْنِ", "مُهَنْدِسَانِ"], "After a preposition: ـِينَ."),
        M("Which means “with the two students”?", "مَعَ الطَّالِبَيْنِ", ["مَعَ الطَّالِبَانِ", "مَعَ الطَّالِبُونَ", "مَعَ الطَّالِبِ"], "Dual after مَعَ: ـَيْنِ."),
        M("Which means “The letter is from the engineers”?", "الرِّسَالَةُ مِنَ الْمُهَنْدِسِينَ", ["الرِّسَالَةُ مِنَ الْمُهَنْدِسُونَ", "الرِّسَالَةُ مِنَ الْمُهَنْدِسَيْنِ", "الرِّسَالَةُ مِنَ الْمُهَنْدِسِ"], "Plural after مِنْ: ـِينَ."),
        M("Which ending does the sound feminine plural take after a preposition?", "ـَاتِ (kasra)", ["ـَاتُ (ḍamma)", "ـَاتَ (fatḥa)", "ـَيْنِ"], "The genitive is a kasra."),
        M("Why is the ending ـَيْنِ in مَكْتَبُ الْمُدَرِّسَيْنِ?", "the second noun of an iḍāfa is genitive", ["it is the subject", "it follows a verb", "it is feminine"], "The owner is genitive."),
        F("الرِّسَالَةُ مِنَ ___.", "الْمُهَنْدِسَيْنِ", ["الْمُهَنْدِسَانِ", "الْمُهَنْدِسُونَ", "الْمُهَنْدِسِينَ"], "Two engineers, after مِنْ.", tr="The letter is from the two engineers."),
        F("أَنَا فِي الصَّفِّ مَعَ ___.", "الطَّالِبِينَ", ["الطَّالِبُونَ", "الطَّالِبَيْنِ", "الطَّالِبَانِ"], "Plural, after مَعَ.", tr="I am in class with the students."),
        F("الْكُرَّاسَةُ عَلَى طَاوِلَةِ ___.", "الطَّالِبَتَيْنِ", ["الطَّالِبَتَانِ", "الطَّالِبَاتُ", "الطَّالِبَيْنِ"], "Two female students; second noun of an iḍāfa.", tr="The notebook is on the two female students’ table."),
    ],
    verify=(vd("طَالِب", "طَالِبَانِ", "طَالِبَيْنِ") + vd("مُدَرِّس", "مُدَرِّسَانِ", "مُدَرِّسَيْنِ") + vd("طَالِبَة", "طَالِبَتَانِ", "طَالِبَتَيْنِ")
            + vps("طَالِب", "طَالِبُونَ", "nom") + vps("طَالِب", "طَالِبِينَ", "obl") + vps("مُهَنْدِس", "مُهَنْدِسُونَ", "nom")
            + vps("مُهَنْدِس", "مُهَنْدِسِينَ", "obl") + vps("مُدَرِّسَة", "مُدَرِّسَات") + vps("طَالِبَة", "طَالِبَات")
            + vw("الْكُرَّاسَة", "طَاوِلَة", "الرِّسَالَة", "الْمَكْتَبَة", "الْجَامِعَة", "قَرِيب", "الْكُتُب")),
)


# ---------------------------------------------------------------------------- 194
L194 = lesson(
    "An afternoon off: activities and feelings",
    "أَشْعُر بِالرَّاحَة · نَظَّفْتُ الْغُرْفَة · غَسَلْتُ الْمَلَابِس",
    requires=["شعر", "غسل", "قلق", "راحة", "شوق", "حزن", "سعادة", "خوف", "هادئ", "مرتاح", "غاضب", "صامت", "شاهد", "زار"],
    cards=[
        card("How do you feel?",
             "Feelings are adjectives, so they agree with the person: add ـَة for a woman. For “I feel…” Arabic says "
             "أَشْعُر بِـ + a noun, with بِ joined to the noun: أَشْعُر بِالسَّعَادَة (“I feel happiness”).",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["happy, pleased", "مَسْرُور", "مَسْرُورَة"], ["angry", "غَاضِب", "غَاضِبَة"], ["calm", "هَادِئ", "هَادِئَة"],
                            ["relaxed, at ease", "مُرْتَاح", "مُرْتَاحَة"], ["silent, quiet", "صَامِت", "صَامِتَة"],
                            ["worried", "قَلِق", "قَلِقَة"]],
                           say=[1, 2], tlit=[1], gloss=False),
                    table(["English", "I feel…"],
                          [["happiness", "أَشْعُر بِالسَّعَادَة"], ["comfort, rest", "أَشْعُر بِالرَّاحَة"], ["worry", "أَشْعُر بِالْقَلَق"],
                            ["sadness", "أَشْعُر بِالْحُزْن"], ["fear", "أَشْعُر بِالْخَوْف"], ["longing", "أَشْعُر بِالشَّوْق"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What I did",
             "On a day off you can talk about what you did with the past tense you know, in the first person ـْتُ.",
             examples=[
                 ex("نَظَّفْتُ الْغُرْفَة وَغَسَلْتُ الْمَلَابِس.", "I cleaned the room and washed the clothes.", "نَظَّفْتُ"),
                 ex("شَاهَدْتُ فِيلْمًا هَادِئًا فِي الْمَسَاء.", "I watched a quiet film in the evening.", "شَاهَدْتُ"),
                 ex("زُرْتُ صَدِيقِي بَعْدَ الظُّهْر.", "I visited my friend in the afternoon.", "زُرْتُ"),
                 ex("أَنَا مُرْتَاح لِأَنَّ الْيَوْم عُطْلَة.", "I am relaxed because today is a holiday.", "مُرْتَاح"),
                 ex("أَشْعُر بِالشَّوْق إِلَى أُمِّي.", "I miss my mother.", "أَشْعُر بِالشَّوْق"),
                 ex("سَارَة غَاضِبَة وَأَحْمَد صَامِت.", "Sara is angry and Ahmad is silent.", "غَاضِبَة"),
             ]),
        card("A short email (an invented practice text)",
             "Here is a short email from Sara to her friend Ahmad. Read it line by line.",
             examples=[
                 ex("عَزِيزِي أَحْمَد،", "Dear Ahmad,", "عَزِيزِي"),
                 ex("كَانَ الْيَوْم يَوْم رَاحَة.", "Today was a day of rest.", "يَوْم رَاحَة"),
                 ex("نَظَّفْتُ الْغُرْفَة وَغَسَلْتُ الْمَلَابِس.", "I cleaned the room and washed the clothes.", "غَسَلْتُ"),
                 ex("ثُمَّ شَاهَدْتُ فِيلْمًا هَادِئًا.", "Then I watched a quiet film.", "ثُمَّ"),
                 ex("أَشْعُر بِالرَّاحَة، وَأَشْعُر أَيْضًا بِالشَّوْق إِلَى أَهْلِي.", "I feel at ease, and I also miss my family.", "أَيْضًا"),
                 ex("مَعَ تَحِيَّاتِي، سَارَة", "With my greetings, Sara", "تَحِيَّاتِي"),
             ]),
    ],
    exercises=[
        M("What does أَشْعُر بِالرَّاحَة mean?", "I feel at ease", ["I feel afraid", "I feel angry", "I feel hungry"], "رَاحَة = comfort, rest."),
        M("Which is the feminine of غَاضِب?", "غَاضِبَة", ["غَاضِبَانِ", "غَاضِبُونَ", "أَغْضَب"], "Add ـَة for a woman."),
        M("Which is the feminine of مُرْتَاح?", "مُرْتَاحَة", ["مُرْتَاحُونَ", "مُرْتَاحَانِ", "مُرْتَاحَات"], "Add ـَة."),
        M("Which sentence means “I miss my mother”?", "أَشْعُر بِالشَّوْق إِلَى أُمِّي", ["أَشْعُر بِالْخَوْف مِنْ أُمِّي", "أَسْكُن مَعَ أُمِّي", "أُرْسِل رِسَالَة إِلَى أُمِّي"], "شَوْق = longing."),
        M("What does غَسَلْتُ الْمَلَابِس mean?", "I washed the clothes", ["I bought the clothes", "I sold the clothes", "I carried the clothes"], "غَسَلَ = to wash."),
        M("Which verb means “I cleaned”?", "نَظَّفْتُ", ["شَاهَدْتُ", "زُرْتُ", "كَتَبْتُ"], "نَظَّفَ = to clean."),
        F("سَارَة ___ لِأَنَّ الْيَوْم عُطْلَة.", "مَسْرُورَة", ["مَسْرُور", "مَسْرُورُونَ", "مَسْرُورَات"], "Sara is a woman.", tr="Sara is happy because today is a holiday."),
        F("أَنَا ___ بِالشَّوْق إِلَى أَهْلِي.", "أَشْعُر", ["شَعَرْتُ", "تَشْعُر", "نَشْعُر"], "I feel (now).", tr="I miss my family.", lemma="شعر:pres:ana"),
        F("أَمْس ___ فِيلْمًا هَادِئًا.", "شَاهَدْتُ", ["أُشَاهِد", "نُشَاهِد", "سَأُشَاهِد"], "Yesterday: the past tense.", tr="Yesterday I watched a quiet film.", lemma="شهد#3:past:ana"),
    ],
    verify=(vf("مَسْرُور", "مَسْرُورَة") + vf("غَاضِب", "غَاضِبَة") + vf("هَادِئ", "هَادِئَة") + vf("مُرْتَاح", "مُرْتَاحَة")
            + vf("صَامِت", "صَامِتَة") + vf("قَلِق", "قَلِقَة")
            + vv("شعر", "pres", ana="أَشْعُر") + vv("شعر", "past", ana="شَعَرْتُ") + vv("نظف#2", "past", ana="نَظَّفْتُ")
            + vv("شهد#3", "past", ana="شَاهَدْتُ") + vv("غسل", "past", ana="غَسَلْتُ") + vv("زور", "past", ana="زُرْتُ")
            + vw("الْمَلَابِس", "الظُّهْر", "عَزِيزِي", "تَحِيَّاتِي", "أَهْلِي", "الشَّوْق", "الْقَلَق", "الْحُزْن", "الْخَوْف", "السَّعَادَة", "الرَّاحَة")),
)

# ---------------------------------------------------------------------------- 195
L195 = lesson(
    "How? Adverbs of manner",
    "بِسُرْعَة · جَيِّدًا · دَخَلَ مُبْتَسِمًا",
    requires=["سرعة", "سهولة", "جيد", "سريع", "هدوء", "حذر", "حماس", "دخل", "كثير", "قليل"],
    cards=[
        card("Two easy ways to say “how”",
             "(1) بِـ + a noun: بِسُرْعَة (“with speed”) means “quickly”. (2) An adjective with the accusative nunation ـًا: "
             "جَيِّدًا (“well”), سَرِيعًا (“fast”). Both go after the verb.",
             tables=[table(["English", "With بِـ"],
                           [["quickly", "بِسُرْعَة"], ["slowly", "بِبُطْء"], ["calmly", "بِهُدُوء"], ["carefully", "بِحَذَر"],
                            ["easily", "بِسُهُولَة"], ["with enthusiasm", "بِحَمَاس"]],
                           say=[1], tlit=[1], gloss=False),
                    table(["English", "With ـًا"],
                          [["well", "جَيِّدًا"], ["fast", "سَرِيعًا"], ["slowly", "بَطِيئًا"], ["a lot", "كَثِيرًا"],
                           ["a little", "قَلِيلًا"], ["very", "جِدًّا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In what state?",
             "An adjective with ـًا can also describe the state of a person while he does something: دَخَلَ مُبْتَسِمًا (“he came in "
             "smiling”). This one must agree with the person it describes in gender and number, and it stays accusative: "
             "ـًا (one man), ـَةً (one woman), ـَيْنِ (two), ـِينَ (men).",
             examples=[
                 ex("يَتَكَلَّم الْمُدَرِّس بِهُدُوء.", "The teacher speaks calmly.", "بِهُدُوء"),
                 ex("تَعْمَل أُخْتِي جَيِّدًا.", "My sister works well.", "جَيِّدًا"),
                 ex("دَخَلَ الْمُدَرِّس مُبْتَسِمًا.", "The teacher came in smiling.", "مُبْتَسِمًا"),
                 ex("دَخَلَتِ الْمُدَرِّسَة مُبْتَسِمَةً.", "The female teacher came in smiling.", "مُبْتَسِمَةً"),
                 ex("دَخَلَ الطَّالِبَانِ مُبْتَسِمَيْنِ.", "The two students came in smiling.", "مُبْتَسِمَيْنِ"),
                 ex("دَخَلَ الطُّلَّاب مُبْتَسِمِينَ.", "The students came in smiling.", "مُبْتَسِمِينَ"),
             ]),
    ],
    exercises=[
        M("Which means “quickly”?", "بِسُرْعَة", ["بِبُطْء", "بِهُدُوء", "بِحَذَر"], "سُرْعَة = speed."),
        M("Which means “carefully”?", "بِحَذَر", ["بِحَمَاس", "بِسُرْعَة", "بِبُطْء"], "حَذَر = care."),
        M("Which is the adverb “well”?", "جَيِّدًا", ["جَيِّدَةً", "جَيِّدٌ", "جَيِّدُونَ"], "ـًا after the verb."),
        M("Which means “The teacher came in smiling”?", "دَخَلَ الْمُدَرِّس مُبْتَسِمًا", ["دَخَلَ الْمُدَرِّس مُبْتَسِمَةً", "دَخَلَ الْمُدَرِّس مُبْتَسِمِينَ", "دَخَلَ الْمُدَرِّس مُبْتَسِمٌ"], "One man: ـًا."),
        M("Which means “The female teacher came in smiling”?", "دَخَلَتِ الْمُدَرِّسَة مُبْتَسِمَةً", ["دَخَلَتِ الْمُدَرِّسَة مُبْتَسِمًا", "دَخَلَتِ الْمُدَرِّسَة مُبْتَسِمِينَ", "دَخَلَتِ الْمُدَرِّسَة مُبْتَسِمَيْنِ"], "One woman: ـَةً."),
        M("The state word in دَخَلَ مُبْتَسِمًا agrees with the person in…", "gender and number", ["gender only", "number only", "nothing; it never changes"], "It matches the person: one man, one woman, two or several."),
        F("دَخَلَ الطُّلَّاب ___.", "مُبْتَسِمِينَ", ["مُبْتَسِمًا", "مُبْتَسِمَةً", "مُبْتَسِمَيْنِ"], "Many men: ـِينَ.", tr="The students came in smiling."),
        F("يَتَكَلَّم الْمُدَرِّس ___.", "بِهُدُوء", ["هَادِئَةً", "الْهُدُوء", "هَادِئُونَ"], "بِ + noun for how.", tr="The teacher speaks calmly."),
        F("تَعْمَل أُخْتِي ___.", "جَيِّدًا", ["جَيِّدٌ", "جَيِّدُونَ", "الْجَيِّد"], "The adverb “well”.", tr="My sister works well."),
    ],
    verify=(vf("مُبْتَسِم", "مُبْتَسِمَة") + vd("مُبْتَسِم", "مُبْتَسِمَانِ", "مُبْتَسِمَيْنِ") + vps("مُبْتَسِم", "مُبْتَسِمِينَ", "obl") + vv("كلم#5", "pres", huwa="يَتَكَلَّم") + vv("دخل", "past", huwa="دَخَلَ", hiya="دَخَلَتْ") + vv("عمل", "pres", hiya="تَعْمَل")
            + vw("بِسُرْعَة", "بِبُطْء", "بِهُدُوء", "بِحَذَر", "بِسُهُولَة", "بِحَمَاس", "جَيِّدًا", "سَرِيعًا", "بَطِيئًا", "كَثِيرًا", "قَلِيلًا",
                 "جِدًّا", "مُبْتَسِمًا", "مُبْتَسِمَةً", "مُبْتَسِمَيْنِ", "مُبْتَسِمِينَ", "أُخْتِي", "الْمُدَرِّسَة", "الطُّلَّاب")),
)

# ---------------------------------------------------------------------------- 196
L196 = lesson(
    "This and that: demonstratives",
    "هَذَا · هَذِهِ · هَذَانِ · هَاتَانِ · هَؤُلَاءِ · ذَلِكَ · تِلْكَ · أُولَئِكَ",
    requires=["هذا", "ذلك", "كتاب", "مدينة", "طالب"],
    cards=[
        card("“This” and “these”",
             "The word for “this” depends on the noun: masculine هَذَا, feminine هَذِهِ. There are also forms for two things "
             "and for several people. The dual changes like any dual: one form for the subject and one after a preposition.",
             tables=[table(["English", "Arabic"],
                           [["this (masculine)", "هَذَا"], ["this (feminine)", "هَذِهِ"],
                            ["these two (masculine, subject)", "هَذَانِ"], ["these two (masculine, after a preposition)", "هَذَيْنِ"],
                            ["these two (feminine, subject)", "هَاتَانِ"], ["these two (feminine, after a preposition)", "هَاتَيْنِ"],
                            ["these (people)", "هَؤُلَاءِ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("“That” and “those”, and how to use them",
             "For something farther away, use ذَلِكَ (masculine), تِلْكَ (feminine) and أُولَئِكَ (people). With a noun that has ال, "
             "the demonstrative comes first and means “this …” or “that …”: هَذَا الْكِتَاب. With a noun that has no ال, it makes a sentence: "
             "هَذَا كِتَاب (“This is a book”). Several things (not people) take the feminine singular: هَذِهِ الْكُتُب مُفِيدَة.",
             examples=[
                 ex("هَذَا الْكِتَاب جَدِيد وَذَلِكَ الْكِتَاب قَدِيم.", "This book is new and that book is old.", "ذَلِكَ"),
                 ex("هَذَا كِتَاب.", "This is a book.", "هَذَا كِتَاب"),
                 ex("هَذِهِ الْمَدِينَة كَبِيرَة وَتِلْكَ الْمَدِينَة صَغِيرَة.", "This city is big and that city is small.", "تِلْكَ"),
                 ex("هَذَانِ الطَّالِبَانِ فِي الصَّفّ.", "These two students are in the class.", "هَذَانِ"),
                 ex("أَنَا مَعَ هَاتَيْنِ الطَّالِبَتَيْنِ.", "I am with these two female students.", "هَاتَيْنِ"),
                 ex("هَؤُلَاءِ الطُّلَّاب مِنْ كَنَدَا وَأُولَئِكَ الطُّلَّاب مِنَ الْأُرْدُنّ.", "These students are from Canada and those students are from Jordan.", "أُولَئِكَ"),
                 ex("هَذِهِ الْكُتُب مُفِيدَة.", "These books are useful.", "هَذِهِ"),
             ]),
    ],
    exercises=[
        M("Which means “this” (masculine)?", "هَذَا", ["هَذِهِ", "ذَلِكَ", "هَؤُلَاءِ"], "Masculine: هَذَا."),
        M("Which means “that” (feminine)?", "تِلْكَ", ["ذَلِكَ", "هَذِهِ", "أُولَئِكَ"], "Feminine, far: تِلْكَ."),
        M("Which means “This is a book”?", "هَذَا كِتَاب", ["هَذَا الْكِتَاب", "ذَلِكَ الْكِتَاب", "هَذِهِ كِتَاب"], "Without ال it is a full sentence."),
        M("Which is correct? “This city is big.”", "هَذِهِ الْمَدِينَة كَبِيرَة", ["هَذَا الْمَدِينَة كَبِيرَة", "هَذِهِ الْمَدِينَة كَبِير", "هَؤُلَاءِ الْمَدِينَة كَبِيرَة"], "مَدِينَة is feminine."),
        M("Which goes with “the two female students” as the subject?", "هَاتَانِ", ["هَذَانِ", "هَذِهِ", "هَؤُلَاءِ"], "Feminine dual, subject."),
        M("Which means “These books are useful”?", "هَذِهِ الْكُتُب مُفِيدَة", ["هَؤُلَاءِ الْكُتُب مُفِيدُونَ", "هَذَا الْكُتُب مُفِيد", "ذَلِكَ الْكُتُب مُفِيدَة"], "Several things take the feminine singular."),
        F("___ الْكِتَاب جَدِيد وَذَلِكَ الْكِتَاب قَدِيم.", "هَذَا", ["هَذِهِ", "تِلْكَ", "هَؤُلَاءِ"], "A masculine book, near.", tr="This book is new and that book is old."),
        F("أَنَا مَعَ ___ الطَّالِبَتَيْنِ.", "هَاتَيْنِ", ["هَاتَانِ", "هَذَيْنِ", "هَذِهِ"], "Feminine dual, after مَعَ.", tr="I am with these two female students."),
        F("___ الطُّلَّاب مِنْ كَنَدَا.", "هَؤُلَاءِ", ["هَذَا", "هَذِهِ", "تِلْكَ"], "Several people.", tr="These students are from Canada."),
    ],
    verify=vw("هَذَا", "هَذِهِ", "هَذَانِ", "هَذَيْنِ", "هَاتَانِ", "هَاتَيْنِ", "هَؤُلَاءِ", "ذَلِكَ", "تِلْكَ", "أُولَئِكَ", "كَنَدَا", "الْأُرْدُنّ", "مُفِيدَة", "الْكُتُب"),
)


# ---------------------------------------------------------------------------- 197
L197 = lesson(
    "Review: the classroom and comparing",
    "صَفِّي الْجَدِيد أَكْبَر مِنَ الصَّفّ الْقَدِيم",
    requires=["أكبر", "أقرب", "أغلى", "أفضل", "أصغر", "أقصر"],
    cards=[
        card("What to remember",
             "To compare, use أَفْعَل + مِنْ. After مِنْ a pronoun is attached (مِنِّي, مِنْكَ, مِنْهُ). For “the most”, put أَفْعَل in "
             "front of a singular noun without ال, or use الْأَفْعَل on its own. A colour agrees with its noun.",
             tables=[table(["English", "Arabic"],
                           [["bigger than the old classroom", "أَكْبَر مِنَ الصَّفّ الْقَدِيم"], ["nearer than my house", "أَقْرَب مِنْ بَيْتِي"],
                            ["shorter than me", "أَقْصَر مِنِّي"], ["more expensive than", "أَغْلَى مِنْ"],
                            ["the best classroom", "أَفْضَل صَفّ"], ["a red car", "سَيَّارَة حَمْرَاء"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A letter from a new student (an invented practice text)",
             "Read these lines from a student’s letter. Notice how each one compares two things.",
             examples=[
                 ex("صَفِّي الْجَدِيد أَكْبَر مِنَ الصَّفّ الْقَدِيم.", "My new classroom is bigger than the old classroom.", "أَكْبَر مِنَ"),
                 ex("فِيهِ نَوَافِذ أَكْثَر وَضَوْء أَقْوَى.", "It has more windows and a stronger light.", "أَكْثَر"),
                 ex("الْكُرْسِيّ الْجَدِيد أَغْلَى مِنَ الْكُرْسِيّ الْقَدِيم.", "The new chair is more expensive than the old chair.", "أَغْلَى"),
                 ex("الْمَكْتَبَة الْجَدِيدَة أَقْرَب مِنْ بَيْتِي.", "The new library is nearer than my house.", "أَقْرَب"),
                 ex("أَنَا أَصْغَر مِنْ أَخِي بِسَنَتَيْن وَهُوَ أَقْصَر مِنِّي.", "I am two years younger than my brother and he is shorter than me.", "مِنِّي"),
                 ex("هَذَا أَفْضَل صَفّ فِي الْمَدْرَسَة.", "This is the best classroom in the school.", "أَفْضَل صَفّ"),
             ]),
    ],
    exercises=[
        M("Which means “My new classroom is bigger than the old one”?", "صَفِّي الْجَدِيد أَكْبَر مِنَ الصَّفّ الْقَدِيم", ["صَفِّي الْجَدِيد أَصْغَر مِنَ الصَّفّ الْقَدِيم", "صَفِّي الْقَدِيم أَكْبَر مِنَ الصَّفّ الْجَدِيد", "صَفِّي الْجَدِيد كَبِيرَة"], "أَكْبَر مِنْ = bigger than."),
        M("Which means “nearer than my house”?", "أَقْرَب مِنْ بَيْتِي", ["أَبْعَد مِنْ بَيْتِي", "أَقْرَب فِي بَيْتِي", "قَرِيب بَيْتِي"], "أَقْرَب = nearer."),
        M("Which ending means “than me”?", "مِنِّي", ["مِنْكَ", "مِنْهُ", "مِنْهَا"], "مِنْ + ـِي → مِنِّي."),
        M("Which means “the best classroom in the school”?", "أَفْضَل صَفّ فِي الْمَدْرَسَة", ["الصَّفّ أَفْضَل مِنَ الْمَدْرَسَة", "أَفْضَل الصَّفّ مِنْ", "صَفّ جَيِّد مِنَ الْمَدْرَسَة"], "أَفْعَل + a noun without ال."),
        M("Which is correct for “a red car” (a feminine noun)?", "سَيَّارَة حَمْرَاء", ["سَيَّارَة أَحْمَر", "سَيَّارَة حُمْر", "سَيَّارَة حَمْرَاوَات"], "Feminine colour: حَمْرَاء."),
        M("Which word means “more expensive”?", "أَغْلَى", ["أَرْخَص", "أَقْوَى", "أَقَلّ"], "غَالِي → أَغْلَى."),
        F("الْكُرْسِيّ الْجَدِيد ___ مِنَ الْكُرْسِيّ الْقَدِيم.", "أَغْلَى", ["غَالِيَة", "أَغْلَيّ", "غُلْيَى"], "More expensive.", tr="The new chair is more expensive than the old chair."),
        F("أَنَا أَصْغَر ___ أَخِي بِسَنَتَيْن.", "مِنْ", ["فِي", "عَنْ", "إِلَى"], "“Than” = مِنْ.", tr="I am two years younger than my brother."),
        F("هُوَ أَقْصَر ___.", "مِنِّي", ["مِنْكَ", "مِنْهُ", "مِنْهَا"], "Than me.", tr="He is shorter than me."),
    ],
    verify=vw("صَفِّي", "فِيهِ", "نَوَافِذ", "ضَوْء", "أَقْوَى", "أَغْلَى", "الْكُرْسِيّ", "حَمْرَاء", "بِسَنَتَيْن", "مِنِّي", "أَفْضَل", "الْمَدْرَسَة"),
)

# ---------------------------------------------------------------------------- 198
L198 = lesson(
    "Review: school places, the genitive, manner, this and that",
    "هَذِهِ مَدْرَسَتِي · تِلْكَ الْقَاعَة · دَخَلَ بِهُدُوء",
    requires=["مدرسة", "مكتبة", "قاعة", "ملعب", "هذا", "ذلك", "مدرس"],
    cards=[
        card("What to remember",
             "After a preposition and as the owner in an iḍāfa a noun is genitive: فِي الْمَكْتَبَةِ, بَابُ الْمَكْتَبَةِ. The dual "
             "and the plural use ـَيْنِ and ـِينَ there. To say how, use بِ + noun or an adjective with ـًا that agrees with the person. "
             "Use هَذَا / هَذِهِ for “this”, ذَلِكَ / تِلْكَ for “that”, هَؤُلَاءِ for “these” and أُولَئِكَ for “those”.",
             tables=[table(["English", "Arabic"],
                           [["the door of the library", "بَابُ الْمَكْتَبَةِ"], ["with the two teachers", "مَعَ الْمُدَرِّسَيْنِ"],
                            ["with the engineers", "مَعَ الْمُهَنْدِسِينَ"], ["calmly", "بِهُدُوء"],
                            ["this school", "هَذِهِ الْمَدْرَسَة"], ["that hall", "تِلْكَ الْقَاعَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A tour of the school (an invented practice text)",
             "A guide shows a visitor around. The sentences mix everything from this part of the unit.",
             examples=[
                 ex("هَذِهِ مَدْرَسَتِي الْجَدِيدَة.", "This is my new school.", "هَذِهِ"),
                 ex("تِلْكَ الْقَاعَة أَكْبَر مِنْ هَذِهِ الْقَاعَة.", "That hall is bigger than this hall.", "تِلْكَ"),
                 ex("الْكُتُبُ فِي مَكْتَبَةِ الْمَدْرَسَةِ.", "The books are in the school library.", "مَكْتَبَةِ الْمَدْرَسَةِ"),
                 ex("دَخَلَ الْمُدِير الْقَاعَة بِهُدُوء.", "The director entered the hall calmly.", "بِهُدُوء"),
                 ex("هَؤُلَاءِ الطُّلَّاب مَعَ الْمُدَرِّسَيْنِ فِي الْمَلْعَبِ.", "These students are with the two teachers on the playground.", "الْمُدَرِّسَيْنِ"),
                 ex("دَخَلَ الطُّلَّاب مُبْتَسِمِينَ.", "The students came in smiling.", "مُبْتَسِمِينَ"),
             ]),
    ],
    exercises=[
        M("Which is correct for “the door of the library”?", "بَابُ الْمَكْتَبَةِ", ["الْبَابُ الْمَكْتَبَةِ", "بَابٌ الْمَكْتَبَةِ", "بَابُ الْمَكْتَبَةُ"], "The first noun has no ال; the owner is genitive."),
        M("Which means “with the two teachers”?", "مَعَ الْمُدَرِّسَيْنِ", ["مَعَ الْمُدَرِّسَانِ", "مَعَ الْمُدَرِّسُونَ", "مَعَ الْمُدَرِّسِ"], "Dual after a preposition: ـَيْنِ."),
        M("Which means “This is my new school”?", "هَذِهِ مَدْرَسَتِي الْجَدِيدَة", ["هَذَا مَدْرَسَتِي الْجَدِيدَة", "هَؤُلَاءِ مَدْرَسَتِي الْجَدِيدَة", "ذَلِكَ مَدْرَسَتِي الْجَدِيدَة"], "مَدْرَسَة is feminine and singular: هَذِهِ."),
        M("Which means “calmly”?", "بِهُدُوء", ["بِسُرْعَة", "بِحَمَاس", "بِحَذَر"], "هُدُوء = calm."),
        M("Which word means “those” (people)?", "أُولَئِكَ", ["هَؤُلَاءِ", "ذَلِكَ", "تِلْكَ"], "Far, several people."),
        M("Which is correct? “The students came in smiling.”", "دَخَلَ الطُّلَّاب مُبْتَسِمِينَ", ["دَخَلَ الطُّلَّاب مُبْتَسِمًا", "دَخَلَ الطُّلَّاب مُبْتَسِمَةً", "دَخَلَ الطُّلَّاب مُبْتَسِمَيْنِ"], "Several men: ـِينَ."),
        F("الْكُتُبُ فِي مَكْتَبَةِ ___.", "الْمَدْرَسَةِ", ["الْمَدْرَسَةُ", "الْمَدْرَسَةَ", "مَدْرَسَةٌ"], "The owner in an iḍāfa is genitive.", tr="The books are in the school library."),
        F("تِلْكَ الْقَاعَة أَكْبَر مِنْ ___ الْقَاعَة.", "هَذِهِ", ["هَذَا", "هَؤُلَاءِ", "ذَلِكَ"], "قَاعَة is feminine; near.", tr="That hall is bigger than this hall."),
        F("هَؤُلَاءِ الطُّلَّاب مَعَ ___ فِي الْمَلْعَبِ.", "الْمُدَرِّسَيْنِ", ["الْمُدَرِّسَانِ", "الْمُدَرِّسُونَ", "الْمُدَرِّسَةُ"], "Two teachers, after مَعَ.", tr="These students are with the two teachers on the playground."),
    ],
    verify=vw("مَدْرَسَتِي", "الْقَاعَة", "الْمَكْتَبَة", "الْمَدْرَسَة", "الْمُدِير", "الْمَلْعَب", "الطُّلَّاب", "بِهُدُوء", "مُبْتَسِمِينَ", "الْمُدَرِّسَيْنِ"),
)


UNIT = unit("الصَّفّ وَالْمَرَافِق: the classroom, comparing, school places and the genitive", [L181, L182, L183, L184, L185, L186, L187, L188, L189, L190, L191, L192, L193, L194, L195, L196, L197, L198])
