"""Unit 10: numbers to a thousand, telling the time, my day, Measures II and V, the future (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 139
L139 = lesson(
    "Eleven to nineteen",
    "أَحَدَ عَشَرَ كِتَابًا · خَمْسَ عَشْرَةَ طَاوِلَةً",
    requires=["عشرة", "واحد", "كتاب", "طالب", "سنة", "عمر"],
    cards=[
        card("The teens",
             "From 11 to 19 the number is two words: a unit and “ten” (عَشَرَ or عَشْرَةَ). For 11 and 12 the unit "
             "agrees with the noun. For 13 to 19 the unit takes the opposite gender, as in 3–10, but the word for “ten” "
             "agrees with the noun. Apart from 12, both parts keep their ending whatever their job in the sentence is.",
             tables=[table(["Number", "With a masculine noun", "With a feminine noun"],
                           [["١١", "أَحَدَ عَشَرَ", "إِحْدَى عَشْرَةَ"], ["١٢", "اِثْنَا عَشَرَ", "اِثْنَتَا عَشْرَةَ"],
                            ["١٣", "ثَلَاثَةَ عَشَرَ", "ثَلَاثَ عَشْرَةَ"], ["١٤", "أَرْبَعَةَ عَشَرَ", "أَرْبَعَ عَشْرَةَ"],
                            ["١٥", "خَمْسَةَ عَشَرَ", "خَمْسَ عَشْرَةَ"], ["١٦", "سِتَّةَ عَشَرَ", "سِتَّ عَشْرَةَ"],
                            ["١٧", "سَبْعَةَ عَشَرَ", "سَبْعَ عَشْرَةَ"], ["١٨", "ثَمَانِيَةَ عَشَرَ", "ثَمَانِيَ عَشْرَةَ"],
                            ["١٩", "تِسْعَةَ عَشَرَ", "تِسْعَ عَشْرَةَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("What comes after the number",
             "The thing you count is SINGULAR and takes the ending ـًا (ـَةً for a feminine word): أَحَدَ عَشَرَ "
             "كِتَابًا (eleven books, literally “eleven a book”). The number 12 shows ـَا in the nominative, as اِثْنَا "
             "عَشَرَ; after a preposition or as an object it shows ـَيْ instead.",
             examples=[
                 ex("فِي الصَّفّ أَحَدَ عَشَرَ طَالِبًا.", "There are eleven students in the class.", "أَحَدَ عَشَرَ"),
                 ex("فِي الْمَكْتَبَة خَمْسَ عَشْرَةَ طَاوِلَةً.", "There are fifteen tables in the library.", "خَمْسَ عَشْرَةَ"),
                 ex("عِنْدِي ثَلَاثَةَ عَشَرَ كِتَابًا.", "I have thirteen books.", "ثَلَاثَةَ عَشَرَ"),
                 ex("فِي السَّنَة اِثْنَا عَشَرَ شَهْرًا.", "There are twelve months in the year.", "اِثْنَا عَشَرَ"),
                 ex("كَمْ عُمْرُكَ؟", "How old are you? (to a man)", "كَمْ"),
                 ex("عُمْرِي تِسْعَ عَشْرَةَ سَنَةً.", "I am nineteen years old.", "تِسْعَ عَشْرَةَ"),
             ]),
    ],
    exercises=[
        M("Which is “eleven” with a masculine noun?", "أَحَدَ عَشَرَ", ["إِحْدَى عَشْرَةَ", "عَشَرَة", "اِثْنَا عَشَرَ"], "11 + masculine: أَحَدَ عَشَرَ."),
        M("Which is “fifteen” with a feminine noun?", "خَمْسَ عَشْرَةَ", ["خَمْسَةَ عَشَرَ", "خَمْس", "خَمْسُون"], "The unit has no ة and “ten” is عَشْرَةَ."),
        M("Which means “twelve students”? (masculine)", "اِثْنَا عَشَرَ طَالِبًا", ["اِثْنَا عَشَرَ طُلَّابًا", "اِثْنَتَا عَشْرَةَ طَالِبًا", "ثَلَاثَةَ عَشَرَ طَالِبًا"], "The noun is singular."),
        M("Which means “fifteen tables”? (طَاوِلَة is feminine)", "خَمْسَ عَشْرَةَ طَاوِلَةً", ["خَمْسَةَ عَشَرَ طَاوِلَةً", "خَمْسَ عَشْرَةَ طَاوِلَات", "خَمْسُون طَاوِلَةً"], "Feminine, singular."),
        M("Which means “She is nineteen years old”?", "عُمْرُهَا تِسْعَ عَشْرَةَ سَنَةً", ["عُمْرُهَا تِسْعَةَ عَشَرَ سَنَةً", "عُمْرُهَا تِسْعَ عَشْرَةَ سَنَوَات", "عُمْرُهُ تِسْعَ عَشْرَةَ سَنَةً"], "سَنَة is feminine, singular."),
        M("What does «كَمْ عُمْرُكَ؟» ask?", "How old are you?", ["Where are you?", "What is your name?", "What time is it?"], "عُمْر = age."),
        F("فِي الصَّفّ أَحَدَ عَشَرَ ___.", "طَالِبًا", ["طَالِبَةً", "طَالِبَات", "طُلَّابًا"], "A masculine singular noun."  , tr="There are eleven students in the class."),
        F("عِنْدِي ___ كِتَابًا.", "ثَلَاثَةَ عَشَرَ", ["ثَلَاثَ عَشْرَةَ", "ثَلَاثُون", "ثَلَاثَة"], "كِتَاب is masculine.", tr="I have thirteen books."),
        F("فِي السَّنَة اِثْنَا عَشَرَ ___.", "شَهْرًا", ["شُهُور", "شَهْرَيْن", "أُسْبُوعًا"], "A singular noun after 12.", tr="There are twelve months in the year."),
    ],
    verify=vw("أَحَدَ", "عَشَرَ", "إِحْدَى", "عَشْرَةَ", "اِثْنَا", "اِثْنَتَا", "ثَلَاثَةَ", "ثَلَاثَ", "أَرْبَعَةَ", "أَرْبَعَ", "خَمْسَةَ", "خَمْسَ",
              "سِتَّةَ", "سِتَّ", "سَبْعَةَ", "سَبْعَ", "ثَمَانِيَةَ", "ثَمَانِيَ", "تِسْعَةَ", "تِسْعَ", "عُمْرُكَ", "عُمْرِي", "عُمْرُهَا", "طَاوِلَةً"),
)

# ---------------------------------------------------------------------------- 140
L140 = lesson(
    "Twenty to ninety-nine",
    "عِشْرُون · خَمْسَة وَعِشْرُون · ثَلَاث وَثَلَاثُون",
    requires=["عشرون", "عشرة", "طالب", "سنة", "عمر", "كتاب"],
    cards=[
        card("The tens",
             "The tens end in ـُون (the sound masculine plural). They are the same for men and women. After a "
             "preposition or as an object ـُون becomes ـِين, just as in the plural of men.",
             tables=[table(["Number", "Arabic"],
                           [["٢٠", "عِشْرُون"], ["٣٠", "ثَلَاثُون"], ["٤٠", "أَرْبَعُون"], ["٥٠", "خَمْسُون"],
                            ["٦٠", "سِتُّون"], ["٧٠", "سَبْعُون"], ["٨٠", "ثَمَانُون"], ["٩٠", "تِسْعُون"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Units and tens: 21 to 99",
             "Say the unit first, then وَ (“and”), then the ten: خَمْسَة وَعِشْرُون (“five and twenty”). The unit "
             "follows the rules you know: 1 and 2 agree with the noun, and 3–9 take the opposite gender. The thing you "
             "count is singular and takes ـًا, as after 11–19.",
             tables=[table(["Number", "With a masculine noun", "With a feminine noun"],
                           [["٢١", "وَاحِد وَعِشْرُون", "إِحْدَى وَعِشْرُون"], ["٢٥", "خَمْسَة وَعِشْرُون", "خَمْس وَعِشْرُون"],
                            ["٣٨", "ثَمَانِيَة وَثَلَاثُون", "ثَمَانِي وَثَلَاثُون"], ["٤٧", "سَبْعَة وَأَرْبَعُون", "سَبْع وَأَرْبَعُون"],
                            ["٩٩", "تِسْعَة وَتِسْعُون", "تِسْع وَتِسْعُون"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("فِي الصَّفّ خَمْسَة وَعِشْرُون طَالِبًا.", "There are twenty-five students in the class.", "خَمْسَة وَعِشْرُون"),
                 ex("فِي الْكُلِّيَّة ثَلَاثُون مُدَرِّسَةً.", "There are thirty (women) teachers in the college.", "ثَلَاثُون"),
                 ex("عُمْرُ أَبِي سِتّ وَخَمْسُون سَنَةً.", "My father is fifty-six years old.", "سِتّ وَخَمْسُون"),
                 ex("مَعِي أَرْبَعُون دِينَارًا.", "I have forty dinars with me.", "أَرْبَعُون"),
                 ex("فِي الْكِتَاب تِسْعُون صَفْحَةً.", "There are ninety pages in the book.", "تِسْعُون"),
             ]),
    ],
    exercises=[
        M("Which number is 30?", "ثَلَاثُون", ["ثَلَاثَة", "ثَلَاثَةَ عَشَرَ", "ثَمَانُون"], "ثَلَاثُون = 30."),
        M("Which number is 50?", "خَمْسُون", ["خَمْسَة", "سِتُّون", "خَمْسَةَ عَشَرَ"], "خَمْسُون = 50."),
        M("Which number is 80?", "ثَمَانُون", ["ثَلَاثُون", "ثَمَانِيَة", "تِسْعُون"], "ثَمَانُون = 80."),
        M("Which is “twenty-five students”? (masculine)", "خَمْسَة وَعِشْرُون طَالِبًا", ["خَمْس وَعِشْرُون طَالِبًا", "عِشْرُون وَخَمْسَة طَالِبًا", "خَمْسَة وَعِشْرُون طُلَّابًا"], "Unit, وَ, ten; the noun is singular."),
        M("Which is “twenty-five students”? (women, طَالِبَة)", "خَمْس وَعِشْرُون طَالِبَةً", ["خَمْسَة وَعِشْرُون طَالِبَةً", "خَمْس وَعِشْرُون طَالِبَات", "خَمْسُون طَالِبَةً"], "Opposite gender for the unit: خَمْس."),
        M("Which means “My father is fifty-six years old”?", "عُمْرُ أَبِي سِتّ وَخَمْسُون سَنَةً", ["عُمْرُ أَبِي سِتَّة وَخَمْسُون سَنَةً", "عُمْرُ أَبِي خَمْسُون وَسِتّ سَنَةً", "عُمْرِي سِتّ وَخَمْسُون سَنَةً"], "سَنَة is feminine, so the unit is سِتّ."),
        M("Which means “I have forty dinars”?", "مَعِي أَرْبَعُون دِينَارًا", ["مَعِي أَرْبَعَة دَنَانِير", "مَعِي أَرْبَعُون دَنَانِير", "مَعِي أَرْبَعَةَ عَشَرَ دِينَارًا"], "Singular noun after the tens."),
        F("فِي الْكِتَاب تِسْعُون ___.", "صَفْحَةً", ["صَفَحَات", "صَفْحَتَيْن", "الصَّفْحَة"], "A singular noun after the tens.", tr="There are ninety pages in the book."),
        F("خَمْسَة ___ طَالِبًا.", "وَعِشْرُون", ["وَثَلَاثُون", "وَعَشَرَ", "وَعَشْرَة"], "Unit + وَ + ten.", tr="Twenty-five students."),
    ],
    verify=vw("عِشْرُون", "ثَلَاثُون", "أَرْبَعُون", "خَمْسُون", "سِتُّون", "سَبْعُون", "ثَمَانُون", "تِسْعُون", "وَعِشْرُون", "وَثَلَاثُون", "وَأَرْبَعُون", "وَخَمْسُون",
              "وَتِسْعُون", "سِتّ", "ثَمَانِي", "صَفْحَةً", "دِينَارًا", "مُدَرِّسَةً", "دَنَانِير"),
)

# ---------------------------------------------------------------------------- 141
L141 = lesson(
    "A hundred, a thousand, and prices",
    "مِئَة دِينَار · أَلْف دُولَار · كَمْ ثَمَنُهُ؟",
    requires=["مئة", "ألف", "دولار", "سعر", "ثمن", "كم"],
    cards=[
        card("100 and 1000",
             "After مِئَة (100) and أَلْف (1000) the thing counted is a singular noun with no ـًا: it is the second "
             "part of an iḍāfa, like بَاب الْبَيْت. So you say مِئَة دِينَار and أَلْف دُولَار. For 3–10 you still "
             "use the plural: ثَلَاثَة دُولَارَات.",
             tables=[table(["Number", "Arabic", "English"],
                           [["١٠٠", "مِئَة دِينَار", "a hundred dinars"], ["١٠٠٠", "أَلْف دُولَار", "a thousand dollars"],
                            ["٥", "خَمْسَة دُولَارَات", "five dollars"], ["٢٠", "عِشْرُون دُولَارًا", "twenty dollars"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("How much is it?",
             "كَمْ ثَمَنُهُ؟ and كَمْ سِعْرُهُ؟ both mean “how much is it?”. The prices go in a noun sentence. رَخِيص is "
             "“cheap” and غَالِي is “expensive”.",
             examples=[
                 ex("كَمْ ثَمَن هَذَا الْكِتَاب؟", "How much is this book?", "كَمْ ثَمَن"),
                 ex("ثَمَنُهُ عِشْرُون دُولَارًا.", "It costs twenty dollars.", "عِشْرُون دُولَارًا"),
                 ex("هَذَا غَالِي. سِعْرُهُ مِئَة دُولَار.", "This is expensive. Its price is a hundred dollars.", "غَالِي"),
                 ex("الْقَهْوَة رَخِيصَة هُنَا.", "The coffee is cheap here.", "رَخِيصَة"),
                 ex("سِعْر الشَّقَّة مِئَة أَلْف دُولَار.", "The price of the flat is a hundred thousand dollars.", "مِئَة أَلْف"),
                 ex("بِكَمْ هَذِه الْحَقِيبَة؟", "How much is this bag?", "بِكَمْ"),
             ]),
    ],
    exercises=[
        M("What does كَمْ ثَمَنُهُ؟ mean?", "How much is it?", ["Where is it?", "What is it?", "Who bought it?"], "ثَمَن = price."),
        M("What does رَخِيص mean?", "cheap", ["expensive", "new", "big"], "رَخِيص = cheap."),
        M("What does غَالِي mean?", "expensive", ["cheap", "old", "small"], "غَالِي = expensive."),
        M("Which means “a hundred dinars”?", "مِئَة دِينَار", ["مِئَة دَنَانِير", "مِئَة دِينَارًا", "عَشْرَة دِينَار"], "مِئَة + singular noun."),
        M("Which means “a thousand dollars”?", "أَلْف دُولَار", ["أَلْف دُولَارَات", "أَلْف دُولَارًا", "مِئَة دُولَار"], "أَلْف + singular noun."),
        M("Which means “five dollars”?", "خَمْسَة دُولَارَات", ["خَمْسَة دُولَار", "خَمْس دُولَارَات", "خَمْسُون دُولَارًا"], "5 + plural noun."),
        M("Which means “twenty dollars”?", "عِشْرُون دُولَارًا", ["عِشْرُون دُولَار", "عِشْرُون دُولَارَات", "عَشْرَة دُولَارَات"], "Tens + singular noun with ـًا."),
        F("___ ثَمَن هَذَا الْكِتَاب؟", "كَمْ", ["مَنْ", "أَيْنَ", "هَلْ"], "“How much”.", tr="How much is this book?"),
        F("ثَمَنُهُ مِئَة ___.", "دُولَار", ["دُولَارًا", "دُولَارَات", "دُولَارَيْن"], "100 + singular noun.", tr="It costs a hundred dollars."),
    ],
    verify=vw("مِئَة", "أَلْف", "دُولَار", "دُولَارَات", "دُولَارًا", "دِينَار", "دَنَانِير", "ثَمَنُهُ", "سِعْرُهُ", "رَخِيصَة", "غَالِي", "الشَّقَّة", "الْحَقِيبَة"),
)

# ---------------------------------------------------------------------------- 142
L142 = lesson(
    "What time is it?",
    "كَمِ السَّاعَة؟ · السَّاعَة الثَّالِثَة",
    requires=["ساعة", "كم", "صباح", "مساء", "ظهر", "ليل"],
    cards=[
        card("The hours",
             "Ask كَمِ السَّاعَة؟ (“how much is the hour?”). The answer is السَّاعَة and a feminine ordinal: السَّاعَة "
             "الثَّالِثَة (the third hour = three o’clock). One o’clock is السَّاعَة الْوَاحِدَة. After 10 the hours use "
             "الْحَادِيَةَ عَشْرَةَ and الثَّانِيَةَ عَشْرَةَ.",
             tables=[table(["Time", "Arabic"],
                           [["1:00", "الْوَاحِدَة"], ["2:00", "الثَّانِيَة"], ["3:00", "الثَّالِثَة"], ["4:00", "الرَّابِعَة"],
                            ["5:00", "الْخَامِسَة"], ["6:00", "السَّادِسَة"], ["7:00", "السَّابِعَة"], ["8:00", "الثَّامِنَة"],
                            ["9:00", "التَّاسِعَة"], ["10:00", "الْعَاشِرَة"], ["11:00", "الْحَادِيَةَ عَشْرَةَ"], ["12:00", "الثَّانِيَةَ عَشْرَةَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In the morning, in the evening",
             "To say “at three”, use فِي السَّاعَة الثَّالِثَة. Add صَبَاحًا (in the morning), ظُهْرًا (around midday), مَسَاءً "
             "(in the afternoon or evening) or لَيْلًا (at night).",
             examples=[
                 ex("كَمِ السَّاعَة الْآن؟", "What time is it now?", "كَمِ السَّاعَة"),
                 ex("السَّاعَة الثَّالِثَة.", "It is three o’clock.", "الثَّالِثَة"),
                 ex("السَّاعَة الثَّامِنَة صَبَاحًا.", "It is eight in the morning.", "صَبَاحًا"),
                 ex("أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة.", "I wake up at six o’clock.", "فِي السَّاعَة السَّادِسَة"),
                 ex("الدَّرْس فِي السَّاعَة التَّاسِعَة.", "The lesson is at nine o’clock.", "التَّاسِعَة"),
                 ex("نَتَغَدَّى فِي السَّاعَة الْوَاحِدَة ظُهْرًا.", "We have lunch at one o’clock in the afternoon.", "ظُهْرًا"),
             ]),
    ],
    exercises=[
        M("Which asks “What time is it?”", "كَمِ السَّاعَة؟", ["كَمْ سَاعَةً؟", "مَتَى السَّاعَة؟", "أَيْنَ السَّاعَة؟"], "كَمِ السَّاعَة؟"),
        M("Which means “It is three o’clock”?", "السَّاعَة الثَّالِثَة", ["السَّاعَة الثَّلَاثَة", "السَّاعَة الثَّالِث", "السَّاعَة الثَّلَاث"], "A feminine ordinal: الثَّالِثَة."),
        M("Which means “seven o’clock”?", "السَّاعَة السَّابِعَة", ["السَّاعَة السَّادِسَة", "السَّاعَة السَّبْعَة", "السَّاعَة الثَّامِنَة"], "السَّابِعَة = seventh."),
        M("Which means “one o’clock”?", "السَّاعَة الْوَاحِدَة", ["السَّاعَة الْوَاحِد", "السَّاعَة الثَّانِيَة", "السَّاعَة الْعَاشِرَة"], "One o’clock uses الْوَاحِدَة."),
        M("Which means “eight in the morning”?", "الثَّامِنَة صَبَاحًا", ["الثَّامِنَة مَسَاءً", "الثَّامِنَة ظُهْرًا", "الثَّامِنَة لَيْلًا"], "صَبَاحًا = in the morning."),
        M("Which means “I wake up at six”?", "أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة", ["أَسْتَيْقِظ فِي السَّاعَة السَّابِعَة", "اِسْتَيْقَظْتُ فِي السَّاعَة السَّادِسَة", "نَسْتَيْقِظ فِي السَّاعَة السَّادِسَة"], "أَسْتَيْقِظ = I wake up."),
        M("What is 11 o’clock?", "الْحَادِيَةَ عَشْرَةَ", ["الْوَاحِدَة عَشْرَةَ", "الْعَاشِرَة", "الثَّانِيَةَ عَشْرَةَ"], "الْحَادِيَةَ عَشْرَةَ."),
        F("___ السَّاعَة الْآن؟", "كَمِ", ["مَنِ", "أَيْنَ", "هَلِ"], "Asking for the time.", tr="What time is it now?"),
        F("نَتَغَدَّى فِي السَّاعَة الْوَاحِدَة ___.", "ظُهْرًا", ["صَبَاحًا", "لَيْلًا", "غَدًا"], "ظُهْرًا = around midday.", tr="We have lunch at one in the afternoon."),
    ],
    verify=vw("كَمِ", "السَّاعَة", "الْوَاحِدَة", "الثَّانِيَة", "الثَّالِثَة", "الرَّابِعَة", "الْخَامِسَة", "السَّادِسَة", "السَّابِعَة", "الثَّامِنَة",
              "التَّاسِعَة", "الْعَاشِرَة", "الْحَادِيَة", "صَبَاحًا", "ظُهْرًا", "مَسَاءً", "لَيْلًا", "أَسْتَيْقِظ", "نَتَغَدَّى", "اِسْتَيْقَظْتُ"),
)

# ---------------------------------------------------------------------------- 143
L143 = lesson(
    "Half past, quarter to, ten minutes",
    "وَالنِّصْف · وَالرُّبْع · إِلَّا رُبْعًا",
    requires=["نصف", "ربع", "دقيقة", "ساعة", "إلا", "قبل"],
    cards=[
        card("Parts of the hour",
             "Add the part after the hour with وَ: وَالنِّصْف (and the half), وَالرُّبْع (and the quarter), وَالثُّلُث "
             "(and the third = twenty minutes). To say “to”, use إِلَّا (“except”): إِلَّا رُبْعًا (a quarter to), إِلَّا "
             "ثُلُثًا (twenty to). Minutes follow the hour with وَ and a number: وَعَشْر دَقَائِق (and ten minutes).",
             tables=[table(["Time", "Arabic"],
                           [["3:30", "الثَّالِثَة وَالنِّصْف"], ["4:15", "الرَّابِعَة وَالرُّبْع"], ["5:20", "الْخَامِسَة وَالثُّلُث"],
                            ["6:45", "السَّابِعَة إِلَّا رُبْعًا"], ["7:40", "الثَّامِنَة إِلَّا ثُلُثًا"],
                            ["8:10", "الثَّامِنَة وَعَشْر دَقَائِق"], ["9:05", "التَّاسِعَة وَخَمْس دَقَائِق"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "A time can end a sentence or follow فِي السَّاعَة.",
             examples=[
                 ex("السَّاعَة الثَّالِثَة وَالنِّصْف.", "It is half past three.", "وَالنِّصْف"),
                 ex("الدَّرْس فِي السَّاعَة الْعَاشِرَة وَالرُّبْع.", "The lesson is at a quarter past ten.", "وَالرُّبْع"),
                 ex("وَصَلَ الْقِطَار فِي السَّاعَة الْخَامِسَة إِلَّا رُبْعًا.", "The train arrived at a quarter to five.", "إِلَّا رُبْعًا"),
                 ex("السَّاعَة الثَّامِنَة وَعَشْر دَقَائِق.", "It is ten past eight.", "وَعَشْر دَقَائِق"),
                 ex("نَتَغَدَّى فِي السَّاعَة الثَّانِيَة وَالنِّصْف.", "We have lunch at half past two.", "وَالنِّصْف"),
                 ex("أَنَام فِي السَّاعَة الْحَادِيَةَ عَشْرَةَ مَسَاءً.", "I go to bed at eleven in the evening.", "أَنَام"),
             ]),
    ],
    exercises=[
        M("Which means “half past three”?", "الثَّالِثَة وَالنِّصْف", ["الثَّالِثَة وَالرُّبْع", "الثَّالِثَة إِلَّا رُبْعًا", "الرَّابِعَة وَالنِّصْف"], "وَالنِّصْف = and the half."),
        M("Which means “a quarter past four”?", "الرَّابِعَة وَالرُّبْع", ["الرَّابِعَة إِلَّا رُبْعًا", "الرَّابِعَة وَالنِّصْف", "الْخَامِسَة وَالرُّبْع"], "وَالرُّبْع = and the quarter."),
        M("Which means “a quarter to seven”?", "السَّابِعَة إِلَّا رُبْعًا", ["السَّابِعَة وَالرُّبْع", "السَّادِسَة إِلَّا رُبْعًا", "السَّابِعَة وَالنِّصْف"], "إِلَّا = to, except."),
        M("What is وَالثُّلُث after the hour?", "twenty past", ["quarter past", "half past", "five past"], "ثُلُث = a third of an hour."),
        M("Which means “ten past eight”?", "الثَّامِنَة وَعَشْر دَقَائِق", ["الثَّامِنَة وَعَشَرَة دَقَائِق", "التَّاسِعَة وَعَشْر دَقَائِق", "الثَّامِنَة إِلَّا عَشْر"], "10 minutes (دَقَائِق is feminine): عَشْر."),
        M("Which means “We have lunch at half past two”?", "نَتَغَدَّى فِي السَّاعَة الثَّانِيَة وَالنِّصْف", ["أَتَغَدَّى فِي السَّاعَة الثَّانِيَة وَالنِّصْف", "نَتَغَدَّى فِي السَّاعَة الثَّالِثَة وَالنِّصْف", "نَتَغَدَّى فِي السَّاعَة الثَّانِيَة وَالرُّبْع"], "نَـ = we."),
        F("السَّاعَة الثَّامِنَة ___ رُبْعًا. (7:45)", "إِلَّا", ["وَ", "فِي", "مِنْ"], "“Quarter to”.", tr="It is a quarter to eight."),
        F("السَّاعَة الثَّالِثَة ___. (3:30)", "وَالنِّصْف", ["وَالرُّبْع", "إِلَّا رُبْعًا", "وَعَشْر"], "Half past three.", tr="It is half past three."),
        F("أَنَام فِي السَّاعَة الْحَادِيَةَ عَشْرَةَ ___.", "مَسَاءً", ["صَبَاحًا", "ظُهْرًا", "غَدًا"], "In the evening.", tr="I go to bed at eleven in the evening."),
    ],
    verify=(vpb("دَقِيقَة", "دَقَائِق")
            + vw("وَالنِّصْف", "وَالرُّبْع", "وَالثُّلُث", "رُبْعًا", "ثُلُثًا", "إِلَّا", "عَشْر", "خَمْس", "أَنَام", "الْقِطَار", "وَصَلَ")),
)

# ---------------------------------------------------------------------------- 144
L144 = lesson(
    "My morning",
    "أَسْتَيْقِظ · أَسْتَحِمّ · أَتَنَاوَل الْإِفْطَار",
    requires=["ساعة", "صباح", "وجه", "بيت", "مدرسة", "أسرة"],
    cards=[
        card("Getting ready",
             "These verbs describe a morning. أَسْتَيْقِظ (I wake up) and أَسْتَحِمّ (I take a shower) are built on a pattern "
             "with an initial سْتـ; for now, learn them as whole words.",
             tables=[table(["English", "Arabic"],
                           [["I wake up", "أَسْتَيْقِظ"], ["I wash my face", "أَغْسِل وَجْهِي"], ["I take a shower", "أَسْتَحِمّ"],
                            ["I put on my clothes", "أَلْبَس ثِيَابِي"], ["I have breakfast", "أَتَنَاوَل الْإِفْطَار"],
                            ["I leave the house", "أَخْرُج مِنَ الْبَيْت"], ["I go to school", "أَذْهَب إِلَى الْمَدْرَسَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A morning in order",
             "Use فِي السَّاعَة for the time, ثُمَّ for “then” and وَ for “and”.",
             examples=[
                 ex("أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة صَبَاحًا.", "I wake up at six in the morning.", "أَسْتَيْقِظ"),
                 ex("أَغْسِل وَجْهِي وَأَسْتَحِمّ.", "I wash my face and take a shower.", "أَغْسِل وَجْهِي"),
                 ex("ثُمَّ أَلْبَس ثِيَابِي.", "Then I put on my clothes.", "أَلْبَس"),
                 ex("أَتَنَاوَل الْإِفْطَار مَعَ أُخْتِي.", "I have breakfast with my sister.", "أَتَنَاوَل"),
                 ex("أَخْرُج مِنَ الْبَيْت فِي السَّاعَة السَّابِعَة وَالنِّصْف.", "I leave the house at half past seven.", "أَخْرُج"),
                 ex("أَذْهَب إِلَى الْمَدْرَسَة بِالدَّرَّاجَة.", "I go to school by bicycle.", "بِالدَّرَّاجَة"),
             ]),
    ],
    exercises=[
        M("What does أَسْتَيْقِظ mean?", "I wake up", ["I go to sleep", "I wash", "I leave"], "أَسْتَيْقِظ = I wake up."),
        M("What does أَسْتَحِمّ mean?", "I take a shower", ["I have breakfast", "I wake up", "I study"], "أَسْتَحِمّ = I bathe."),
        M("Which means “I have breakfast”?", "أَتَنَاوَل الْإِفْطَار", ["أَسْتَحِمّ الْإِفْطَار", "أَلْبَس الْإِفْطَار", "أَغْسِل الْإِفْطَار"], "أَتَنَاوَل = I have (a meal)."),
        M("Which means “I put on my clothes”?", "أَلْبَس ثِيَابِي", ["أَغْسِل ثِيَابِي", "أَخْرُج ثِيَابِي", "أَسْتَيْقِظ ثِيَابِي"], "لَبِسَ = to wear, put on."),
        M("Which means “I leave the house”?", "أَخْرُج مِنَ الْبَيْت", ["أَدْخُل الْبَيْت", "أَذْهَب إِلَى الْبَيْت", "أَسْكُن فِي الْبَيْت"], "خَرَجَ مِنْ."),
        M("Which means “I go to school by bicycle”?", "أَذْهَب إِلَى الْمَدْرَسَة بِالدَّرَّاجَة", ["أَذْهَب إِلَى الْمَدْرَسَة مَعَ الدَّرَّاجَة", "أَذْهَب إِلَى الْبَيْت بِالدَّرَّاجَة", "أَذْهَب إِلَى الدَّرَّاجَة بِالْمَدْرَسَة"], "بِـ = by (means)."),
        F("أَغْسِل ___ وَأَسْتَحِمّ.", "وَجْهِي", ["أُخْتِي", "مَدْرَسَتِي", "إِفْطَارِي"], "You wash your face.", tr="I wash my face and take a shower."),
        F("ثُمَّ ___ ثِيَابِي.", "أَلْبَس", ["أَسْتَحِمّ", "أَخْرُج", "أَسْتَيْقِظ"], "You put on clothes.", tr="Then I put on my clothes."),
        F("أَخْرُج ___ الْبَيْت فِي السَّاعَة السَّابِعَة.", "مِنَ", ["إِلَى", "عَلَى", "مَعَ"], "Leave = خَرَجَ مِنْ.", tr="I leave the house at seven o’clock."),
    ],
    verify=vv("غسل", "pres", ana="أَغْسِل")
    + vv("خرج", "pres", ana="أَخْرُج") + vv("ذهب", "pres", ana="أَذْهَب")
    + vw("أَسْتَيْقِظ", "أَسْتَحِمّ", "أَتَنَاوَل", "الْإِفْطَار", "وَجْهِي", "ثِيَابِي", "أَلْبَس", "بِالدَّرَّاجَة"),
)

# ---------------------------------------------------------------------------- 145
L145 = lesson(
    "Afternoon and evening",
    "أَتَغَدَّى · أَتَعَشَّى · أَنَام",
    requires=["رجع", "درس", "لعب", "نام", "قبل", "بعد", "غداء", "عشاء"],
    cards=[
        card("After school",
             "Here is the second half of a day. أَرْجِع (I come back), أَدْرُس (I study) and أَلْعَب (I play) are ordinary "
             "verbs you know how to conjugate. أَتَغَدَّى (I have lunch) and أَتَعَشَّى (I have dinner) belong to "
             "a verb pattern that gets its own lesson soon; for now learn them as whole words.",
             tables=[table(["English", "Arabic"],
                           [["I come back home", "أَرْجِع إِلَى الْبَيْت"], ["I have lunch", "أَتَغَدَّى"],
                            ["I study my lessons", "أَدْرُس دُرُوسِي"], ["I play", "أَلْعَب"],
                            ["I have dinner", "أَتَعَشَّى"], ["I go to bed", "أَنَام"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("To sleep",
             "نَامَ (to sleep) has a long vowel ā in the middle of the present. The long vowel stays in the singular and "
             "the plural with ـُون, so the verb looks like this:",
             tables=[table(["Person", "Arabic"],
                           [["I", "أَنَام"], ["we", "نَنَام"], ["you (to a man)", "تَنَام"], ["you (to a woman)", "تَنَامِين"],
                            ["he", "يَنَام"], ["she", "تَنَام"], ["they (men)", "يَنَامُون"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أَرْجِع إِلَى الْبَيْت فِي السَّاعَة الرَّابِعَة مَسَاءً.", "I come back home at four in the afternoon.", "أَرْجِع"),
                 ex("بَعْدَ الْغَدَاء أَدْرُس دُرُوسِي.", "After lunch I study my lessons.", "بَعْدَ الْغَدَاء"),
                 ex("قَبْلَ الْعَشَاء أَلْعَب مَعَ أَخِي.", "Before dinner I play with my brother.", "قَبْلَ الْعَشَاء"),
                 ex("نَتَعَشَّى فِي السَّاعَة السَّابِعَة.", "We have dinner at seven o’clock.", "نَتَعَشَّى"),
                 ex("هَلْ تَنَامِين فِي السَّاعَة الْعَاشِرَة؟", "Do you go to bed at ten o’clock? (to a woman)", "تَنَامِين"),
                 ex("أَخِي يَنَام فِي السَّاعَة الْحَادِيَةَ عَشْرَةَ.", "My brother goes to bed at eleven o’clock.", "يَنَام"),
             ]),
    ],
    exercises=[
        M("What does أَتَعَشَّى mean?", "I have dinner", ["I have lunch", "I have breakfast", "I go to bed"], "عَشَاء = dinner."),
        M("What does أَتَغَدَّى mean?", "I have lunch", ["I have dinner", "I wake up", "I play"], "غَدَاء = lunch."),
        M("What does أَنَام mean?", "I go to sleep", ["I wake up", "I come back", "I study"], "نَامَ = to sleep."),
        M("Which means “After lunch I study my lessons”?", "بَعْدَ الْغَدَاء أَدْرُس دُرُوسِي", ["قَبْلَ الْغَدَاء أَدْرُس دُرُوسِي", "بَعْدَ الْغَدَاء أَلْعَب", "بَعْدَ الْعَشَاء أَدْرُس دُرُوسِي"], "بَعْدَ = after."),
        M("Which means “Before dinner I play with my brother”?", "قَبْلَ الْعَشَاء أَلْعَب مَعَ أَخِي", ["بَعْدَ الْعَشَاء أَلْعَب مَعَ أَخِي", "قَبْلَ الْغَدَاء أَلْعَب مَعَ أَخِي", "قَبْلَ الْعَشَاء أَدْرُس مَعَ أَخِي"], "قَبْلَ = before."),
        M("Which means “you sleep” (to a woman)?", "أَنْتِ تَنَامِين", ["أَنْتَ تَنَام", "هُوَ يَنَام", "أَنَا أَنَام"], "The ـِين ending is for “you” (to a woman)."),
        M("Which means “they sleep” (men)?", "هُمْ يَنَامُون", ["هُمْ يَنَام", "نَحْنُ نَنَام", "أَنْتُمْ تَنَامُون"], "يَـ ... ـُون = they (men)."),
        F("بَعْدَ ___ أَدْرُس دُرُوسِي.", "الْغَدَاء", ["أَتَغَدَّى", "نَتَغَدَّى", "تَغَدَّى"], "بَعْدَ is followed by a noun.", tr="After lunch I study my lessons."),
        F("أَرْجِع ___ الْبَيْت فِي السَّاعَة الرَّابِعَة.", "إِلَى", ["مِنَ", "عَلَى", "عَنِ"], "Come back to = رَجَعَ إِلَى.", tr="I come back home at four o’clock."),
        F("هَلْ ___ فِي السَّاعَة الْعَاشِرَة؟ (to a woman)", "تَنَامِين", ["تَنَامُون", "يَنَامُون", "نَنَام"], "“You” (to a woman) ends in ـِين.", tr="Do you go to bed at ten o’clock?"),
    ],
    verify=vv("رجع", "pres", ana="أَرْجِع") + vv("درس", "pres", ana="أَدْرُس") + vv("لعب", "pres", ana="أَلْعَب")
    + vw("أَتَغَدَّى", "نَتَعَشَّى", "أَتَعَشَّى", "أَنَام", "نَنَام", "تَنَام", "تَنَامِين", "يَنَام", "يَنَامُون", "الْغَدَاء", "الْعَشَاء", "قَبْلَ", "بَعْدَ", "دُرُوسِي"),
)

# ---------------------------------------------------------------------------- 146
L146 = lesson(
    "Measure II: the doubled middle letter",
    "دَرَسَ ← دَرَّسَ · يُدَرِّس",
    requires=["درس", "علم", "حضر", "مدرس", "كبر", "غرفة"],
    cards=[
        card("Doubling the middle",
             "Arabic builds many verbs from one root by changing the pattern. If you double the middle letter of a root you "
             "get Measure II, written فَعَّلَ. It often means “to cause someone to do it”: دَرَسَ (he studied) becomes "
             "دَرَّسَ (he taught).",
             tables=[table(["Meaning", "Measure I", "Measure II"],
                           [["studied → taught", "دَرَسَ", "دَرَّسَ"], ["knew → taught", "عَلِمَ", "عَلَّمَ"],
                            ["attended → prepared", "حَضَرَ", "حَضَّرَ"], ["was clean → cleaned", "نَظُفَ", "نَظَّفَ"],
                            ["was big → made bigger", "كَبُرَ", "كَبَّرَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("The present tense",
             "In the present tense every Measure II verb has a prefix with ḍamma (أُ نُ تُ يُ) and a kasra before the "
             "last letter: يُدَرِّس, أُدَرِّس. The endings are the ones you already know. The teacher is مُدَرِّس, “the one "
             "who teaches”.",
             tables=[table(["Person", "Arabic"],
                           [["I", "أُدَرِّس"], ["we", "نُدَرِّس"], ["you (to a man)", "تُدَرِّس"], ["you (to a woman)", "تُدَرِّسِين"],
                            ["he", "يُدَرِّس"], ["she", "تُدَرِّس"], ["they (men)", "يُدَرِّسُون"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُمِّي تُدَرِّس الْعَرَبِيَّة فِي الْمَدْرَسَة.", "My mother teaches Arabic at school.", "تُدَرِّس"),
                 ex("عَلَّمَتْنِي مُدَرِّسَتِي الْكِتَابَة.", "My teacher taught me writing.", "عَلَّمَتْنِي"),
                 ex("حَضَّرَتْ أُمِّي الْعَشَاء.", "My mother prepared dinner.", "حَضَّرَتْ"),
                 ex("نَظَّفْتُ الْغُرْفَة أَمْس.", "I cleaned the room yesterday.", "نَظَّفْتُ"),
                 ex("أُرَتِّب غُرْفَتِي كُلّ يَوْم.", "I tidy my room every day.", "أُرَتِّب"),
                 ex("هُمْ يُنَظِّفُون الْمَدْرَسَة بَعْدَ الدَّرْس.", "They clean the school after the lesson.", "يُنَظِّفُون"),
             ]),
    ],
    exercises=[
        M("What does دَرَّسَ mean?", "he taught", ["he studied", "he asked", "he wrote"], "Doubling the middle: “cause to study” = teach."),
        M("Which verb means “he prepared”?", "حَضَّرَ", ["حَضَرَ", "دَرَّسَ", "نَظَّفَ"], "حَضَّرَ is Measure II."),
        M("Which verb means “he cleaned”?", "نَظَّفَ", ["نَظُفَ", "حَضَّرَ", "عَلَّمَ"], "Measure II of the root ن-ظ-ف."),
        M("Which is “I teach”?", "أُدَرِّس", ["أَدْرُس", "يُدَرِّس", "نُدَرِّس"], "The prefix أُ and a kasra before the last letter."),
        M("Which is “they teach” (men)?", "يُدَرِّسُون", ["يُدَرِّس", "تُدَرِّسِين", "نُدَرِّس"], "يُـ ... ـُون."),
        M("What does مُدَرِّس mean?", "teacher", ["student", "lesson", "school"], "“The one who teaches”."),
        M("Which means “I cleaned the room yesterday”?", "نَظَّفْتُ الْغُرْفَة أَمْس", ["أُنَظِّف الْغُرْفَة أَمْس", "نَظَّفَ الْغُرْفَة أَمْس", "نَظَّفْنَا الْغُرْفَة أَمْس"], "ـتُ = I (past)."),
        M("Which means “My mother prepared dinner”?", "حَضَّرَتْ أُمِّي الْعَشَاء", ["حَضَّرْتُ الْعَشَاء", "أُمِّي تُحَضِّر الْعَشَاء", "حَضَّرَ أَبِي الْعَشَاء"], "ـتْ = she (past)."),
        F("أُمِّي ___ الْعَرَبِيَّة فِي الْمَدْرَسَة.", "تُدَرِّس", ["يُدَرِّس", "أُدَرِّس", "تُدَرِّسِين"], "“She” in the present: تُـ.", tr="My mother teaches Arabic at school."),
        F("___ أُمِّي الْعَشَاء.", "حَضَّرَتْ", ["أُحَضِّر", "حَضَّرْتُ", "تُحَضِّرِين"], "A past verb for “she”.", tr="My mother prepared dinner."),
    ],
    verify=vw("دَرَّسَ", "عَلَّمَ", "حَضَّرَ", "نَظَّفَ", "كَبَّرَ", "دَرَسَ", "عَلِمَ", "حَضَرَ", "نَظُفَ", "كَبُرَ", "أُدَرِّس", "نُدَرِّس", "تُدَرِّس", "تُدَرِّسِين",
              "يُدَرِّس", "يُدَرِّسُون", "عَلَّمَتْنِي", "حَضَّرَتْ", "نَظَّفْتُ", "أُرَتِّب", "يُنَظِّفُون", "مُدَرِّس", "أُحَضِّر", "تُحَضِّر", "الْكِتَابَة"),
)

# ---------------------------------------------------------------------------- 147
L147 = lesson(
    "Measure V: tafaʿʿala",
    "تَعَلَّمَ · تَكَلَّمَ · تَحَدَّثَ",
    requires=["علم", "كلم", "حدث", "عربي", "صف", "غداء"],
    cards=[
        card("Adding تَـ to Measure II",
             "Put تَـ in front of a Measure II verb and you get Measure V, written تَفَعَّلَ. It often means doing the "
             "action to yourself, or the result of the Measure II action: عَلَّمَ (he taught) gives تَعَلَّمَ (he learned). "
             "In the present, the usual person prefix goes in front of the تَـ: أَتَعَلَّم, تَتَعَلَّم, يَتَعَلَّم.",
             tables=[table(["Meaning", "Measure II", "Measure V"],
                           [["taught → learned", "عَلَّمَ", "تَعَلَّمَ"], ["spoke to → spoke", "كَلَّمَ", "تَكَلَّمَ"],
                            ["told → talked", "حَدَّثَ", "تَحَدَّثَ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False),
                     table(["Person", "Arabic"],
                           [["I", "أَتَكَلَّم"], ["we", "نَتَكَلَّم"], ["you (to a man)", "تَتَكَلَّم"], ["you (to a woman)", "تَتَكَلَّمِين"],
                            ["he", "يَتَكَلَّم"], ["she", "تَتَكَلَّم"], ["they (men)", "يَتَكَلَّمُون"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "The past tense is easy to spot: the verb begins with تَـ and has a doubled middle letter, as in تَكَلَّمْتُ "
             "(I spoke). The verbs for lunch and dinner you met before belong here: تَغَدَّى and تَعَشَّى.",
             examples=[
                 ex("أَتَعَلَّم الْعَرَبِيَّة مُنْذُ سَنَة.", "I have been learning Arabic for a year.", "أَتَعَلَّم"),
                 ex("هَلْ تَتَكَلَّم الْعَرَبِيَّة؟", "Do you speak Arabic? (to a man)", "تَتَكَلَّم"),
                 ex("تَكَلَّمْتُ مَعَ مُدَرِّسِي أَمْس.", "I spoke with my teacher yesterday.", "تَكَلَّمْتُ"),
                 ex("نَتَحَدَّث عَنِ الْعَمَل.", "We talk about work.", "نَتَحَدَّث"),
                 ex("تَعَلَّمَ أَخِي الْقِرَاءَة فِي الصَّفّ الْأَوَّل.", "My brother learned to read in the first grade.", "تَعَلَّمَ"),
                 ex("تَغَدَّيْنَا مَعَ الْأُسْرَة.", "We had lunch with the family.", "تَغَدَّيْنَا"),
             ]),
    ],
    exercises=[
        M("What does تَعَلَّمَ mean?", "he learned", ["he taught", "he asked", "he knew"], "Measure V of the root ع-ل-م."),
        M("What does تَكَلَّمَ mean?", "he spoke", ["he wrote", "he listened", "he went"], "Measure V: “he spoke”."),
        M("Which is “I speak”?", "أَتَكَلَّم", ["أُكَلِّم", "يَتَكَلَّم", "نَتَكَلَّم"], "Prefix أَ + تَـ + the doubled letter."),
        M("Which is “we speak”?", "نَتَكَلَّم", ["أَتَكَلَّم", "يَتَكَلَّم", "تَتَكَلَّمُون"], "نَـ + تَـ."),
        M("Which is “you speak” (to a woman)?", "تَتَكَلَّمِين", ["تَتَكَلَّمُون", "تَتَكَلَّم", "يَتَكَلَّمُون"], "The ـِين ending."),
        M("Which means “I spoke with my teacher yesterday”?", "تَكَلَّمْتُ مَعَ مُدَرِّسِي أَمْس", ["أَتَكَلَّم مَعَ مُدَرِّسِي أَمْس", "تَكَلَّمَ مَعَ مُدَرِّسِي أَمْس", "تَكَلَّمْنَا مَعَ مُدَرِّسِي أَمْس"], "ـتُ = I (past)."),
        M("Which means “We talk about work”?", "نَتَحَدَّث عَنِ الْعَمَل", ["أَتَحَدَّث عَنِ الْعَمَل", "يَتَحَدَّثُون عَنِ الْعَمَل", "نَتَحَدَّث مِنَ الْعَمَل"], "عَنْ = about."),
        F("هَلْ ___ الْعَرَبِيَّة؟ (to a man)", "تَتَكَلَّم", ["أَتَكَلَّم", "يَتَكَلَّمُون", "تَتَكَلَّمِين"], "“You” (to a man): تَـ + a plain ending.", tr="Do you speak Arabic?"),
        F("___ أَخِي الْقِرَاءَة فِي الصَّفّ الْأَوَّل.", "تَعَلَّمَ", ["تَعَلَّمْتُ", "أَتَعَلَّم", "يَتَعَلَّمُون"], "A past verb for “he”.", tr="My brother learned to read in the first grade."),
    ],
    verify=vw("تَعَلَّمَ", "تَكَلَّمَ", "تَحَدَّثَ", "كَلَّمَ", "حَدَّثَ", "أَتَعَلَّم", "أَتَكَلَّم", "نَتَكَلَّم", "تَتَكَلَّم", "تَتَكَلَّمِين", "يَتَكَلَّم", "يَتَكَلَّمُون",
              "تَكَلَّمْتُ", "نَتَحَدَّث", "تَغَدَّيْنَا", "تَغَدَّى", "تَعَشَّى", "الْقِرَاءَة", "الْأَوَّل", "مُدَرِّسِي"),
)

# ---------------------------------------------------------------------------- 148
L148 = lesson(
    "Next week and in three days",
    "غَدًا · الْأُسْبُوع الْقَادِم · بَعْدَ ثَلَاثَة أَيَّام",
    requires=["غد", "أسبوع", "شهر", "سنة", "قادم", "بعد", "يوم"],
    cards=[
        card("Time words for the future",
             "You already know سَـ and سَوْفَ. Now add words for when. بَعْدَ before a time means “in”: بَعْدَ أُسْبُوع is "
             "“in a week”. الْقَادِم (“coming”) follows the noun and agrees with it: الْأُسْبُوع الْقَادِم, السَّنَة الْقَادِمَة.",
             tables=[table(["English", "Arabic"],
                           [["tomorrow", "غَدًا"], ["the day after tomorrow", "بَعْدَ غَد"], ["next week", "الْأُسْبُوع الْقَادِم"],
                            ["next month", "الشَّهْر الْقَادِم"], ["next year", "السَّنَة الْقَادِمَة"],
                            ["in a week", "بَعْدَ أُسْبُوع"], ["in three days", "بَعْدَ ثَلَاثَة أَيَّام"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Plans",
             "The time word can come first or last. Look at how سَـ is joined to the verb.",
             tables=[table(["Person", "Arabic"],
                           [["I", "سَأَذْهَب"], ["we", "سَنَذْهَب"], ["you (to a man)", "سَتَذْهَب"], ["you (to a woman)", "سَتَذْهَبِين"],
                            ["he", "سَيَذْهَب"], ["she", "سَتَذْهَب"], ["they (men)", "سَيَذْهَبُون"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("غَدًا سَأَذْهَب إِلَى الْمَكْتَبَة.", "Tomorrow I will go to the library.", "غَدًا"),
                 ex("سَنَرْجِع إِلَى الْبَيْت بَعْدَ ثَلَاثَة أَيَّام.", "We will go back home in three days.", "بَعْدَ ثَلَاثَة أَيَّام"),
                 ex("فِي الْأُسْبُوع الْقَادِم سَأَعْمَل فِي الْمَكْتَب.", "Next week I will work in the office.", "الْأُسْبُوع الْقَادِم"),
                 ex("فِي الشَّهْر الْقَادِم سَتَدْرُس أُخْتِي فِي الْجَامِعَة.", "Next month my sister will study at the university.", "الشَّهْر الْقَادِم"),
                 ex("سَأَكْتُب إِلَيْكَ بَعْدَ أُسْبُوع.", "I will write to you in a week. (to a man)", "بَعْدَ أُسْبُوع"),
                 ex("فِي السَّنَة الْقَادِمَة سَيَفْتَح أَخِي مَطْعَم.", "Next year my brother will open a restaurant.", "السَّنَة الْقَادِمَة"),
             ]),
    ],
    exercises=[
        M("What does الْأُسْبُوع الْقَادِم mean?", "next week", ["last week", "this week", "every week"], "قَادِم = coming."),
        M("What does السَّنَة الْقَادِمَة mean?", "next year", ["last year", "this year", "next month"], "A feminine noun takes الْقَادِمَة."),
        M("What does بَعْدَ أُسْبُوع mean?", "in a week", ["a week ago", "for a week", "every week"], "بَعْدَ + a time = in..."),
        M("Which means “in three days”?", "بَعْدَ ثَلَاثَة أَيَّام", ["قَبْلَ ثَلَاثَة أَيَّام", "بَعْدَ ثَلَاثَة يَوْم", "مُنْذُ ثَلَاثَة أَيَّام"], "3–10 take a plural noun."),
        M("Which means “Next month my sister will study at the university”?", "فِي الشَّهْر الْقَادِم سَتَدْرُس أُخْتِي فِي الْجَامِعَة", ["فِي الشَّهْر الْمَاضِي سَتَدْرُس أُخْتِي فِي الْجَامِعَة", "فِي الشَّهْر الْقَادِم سَيَدْرُس أَخِي فِي الْجَامِعَة", "فِي الْأُسْبُوع الْقَادِم سَتَدْرُس أُخْتِي فِي الْجَامِعَة"], "الشَّهْر = month."),
        M("Which is “we will go”?", "سَنَذْهَب", ["سَأَذْهَب", "سَتَذْهَب", "سَيَذْهَبُون"], "سَـ + نَـ."),
        M("Which is “they will go” (men)?", "سَيَذْهَبُون", ["سَيَذْهَب", "سَنَذْهَب", "سَتَذْهَبِين"], "سَيَـ ... ـُون."),
        F("___ سَأَذْهَب إِلَى الْمَكْتَبَة.", "غَدًا", ["أَمْس", "كُلّ", "مُنْذُ"], "A future time word.", tr="Tomorrow I will go to the library."),
        F("سَنَرْجِع إِلَى الْبَيْت ___ ثَلَاثَة أَيَّام.", "بَعْدَ", ["قَبْلَ", "مَعَ", "عَلَى"], "“In three days”.", tr="We will go back home in three days."),
        F("فِي السَّنَة ___ سَيَفْتَح أَخِي مَطْعَم.", "الْقَادِمَة", ["الْقَادِم", "الْمَاضِي", "الْمَاضِيَة"], "سَنَة is feminine and the year is still to come.", tr="Next year my brother will open a restaurant."),
    ],
    verify=vv("ذهب", "fut", ana="سَأَذْهَب", nahnu="سَنَذْهَب", anta="سَتَذْهَب", anti="سَتَذْهَبِين", huwa="سَيَذْهَب", hiya="سَتَذْهَب", hum="سَيَذْهَبُون")
    + vv("رجع", "fut", nahnu="سَنَرْجِع") + vv("درس", "fut", hiya="سَتَدْرُس") + vv("كتب", "fut", ana="سَأَكْتُب") + vv("فتح", "fut", huwa="سَيَفْتَح") + vv("عمل", "fut", ana="سَأَعْمَل")
    + vw("غَدًا", "الْقَادِم", "الْقَادِمَة", "أُسْبُوع", "أَيَّام", "إِلَيْكَ", "مَطْعَم", "الْمَكْتَبَة", "الْمَكْتَب"),
)

# ---------------------------------------------------------------------------- 149
L149 = lesson(
    "Will not: لَنْ",
    "لَنْ أَذْهَب · لَنْ يَكْتُبُوا",
    requires=["ذهب", "رجع", "كتب", "درس", "غد", "عشاء"],
    cards=[
        card("لَنْ + verb",
             "لَنْ means “will not”. Put it in front of the present verb, with no سَـ. After لَنْ the verb takes the "
             "same shortened form as after أَنْ: the final ن of ـِينَ, ـَانِ and ـُونَ falls away, and ـُوا gets a silent alif. "
             "The women’s plural ـْنَ keeps its ن.",
             tables=[table(["Person", "Will", "Will not"],
                           [["I", "سَأَذْهَب", "لَنْ أَذْهَب"], ["we", "سَنَذْهَب", "لَنْ نَذْهَب"],
                            ["you (to a man)", "سَتَذْهَب", "لَنْ تَذْهَب"], ["you (to a woman)", "سَتَذْهَبِين", "لَنْ تَذْهَبِي"],
                            ["he", "سَيَذْهَب", "لَنْ يَذْهَب"], ["she", "سَتَذْهَب", "لَنْ تَذْهَب"],
                            ["they (men)", "سَيَذْهَبُون", "لَنْ يَذْهَبُوا"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Past, present, future",
             "You now have three ways to say no, one for each time. لَمْ is for the past, لَا for the present and لَنْ for the future.",
             tables=[table(["Time", "Arabic", "English"],
                           [["past", "لَمْ أَذْهَب", "I did not go"], ["present", "لَا أَذْهَب", "I do not go"],
                            ["future", "لَنْ أَذْهَب", "I will not go"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("لَنْ أَذْهَب إِلَى الْمَدْرَسَة غَدًا.", "I will not go to school tomorrow.", "لَنْ أَذْهَب"),
                 ex("لَنْ نَرْجِع إِلَى الْبَيْت قَبْلَ الْعَشَاء.", "We will not go back home before dinner.", "لَنْ نَرْجِع"),
                 ex("أُخْتِي لَنْ تَدْرُس غَدًا.", "My sister will not study tomorrow.", "لَنْ تَدْرُس"),
                 ex("لَنْ يَكْتُبُوا الْوَاجِب الْيَوْم.", "They will not do the homework today.", "لَنْ يَكْتُبُوا"),
                 ex("لَنْ تَجْلِسِي هُنَا.", "You will not sit here. (to a woman)", "لَنْ تَجْلِسِي"),
                 ex("لَمْ أَذْهَب أَمْس وَلَنْ أَذْهَب غَدًا.", "I did not go yesterday and I will not go tomorrow.", "وَلَنْ أَذْهَب"),
             ]),
    ],
    exercises=[
        M("What does لَنْ mean?", "will not", ["did not", "will", "do not"], "لَنْ negates the future."),
        M("Which means “I will not go”?", "لَنْ أَذْهَب", ["لَمْ أَذْهَب", "لَا أَذْهَب", "سَأَذْهَب"], "لَنْ + present."),
        M("Which means “I did not go”?", "لَمْ أَذْهَب", ["لَنْ أَذْهَب", "سَأَذْهَب", "لَا أَذْهَب"], "لَمْ is for the past."),
        M("Which means “they (men) will not go”?", "لَنْ يَذْهَبُوا", ["لَنْ يَذْهَبُون", "لَنْ يَذْهَب", "لَنْ تَذْهَبُوا"], "After لَنْ the final ن falls away."),
        M("Which means “you (to a woman) will not go”?", "لَنْ تَذْهَبِي", ["لَنْ تَذْهَبِين", "لَنْ تَذْهَب", "لَنْ يَذْهَبُوا"], "ـِين loses its ن after لَنْ."),
        M("Which means “My sister will not study tomorrow”?", "أُخْتِي لَنْ تَدْرُس غَدًا", ["أُخْتِي لَنْ يَدْرُس غَدًا", "أُخْتِي لَمْ تَدْرُس غَدًا", "أَخِي لَنْ تَدْرُس غَدًا"], "She: تَـ."),
        M("Which means “We will not go back before dinner”?", "لَنْ نَرْجِع قَبْلَ الْعَشَاء", ["لَنْ أَرْجِع قَبْلَ الْعَشَاء", "لَنْ نَرْجِع بَعْدَ الْعَشَاء", "لَمْ نَرْجِع قَبْلَ الْعَشَاء"], "نَـ = we."),
        F("___ أَذْهَب إِلَى الْمَدْرَسَة غَدًا. (will not)", "لَنْ", ["لَمْ", "سَوْفَ", "قَدْ"], "Will not.", tr="I will not go to school tomorrow."),
        F("لَنْ ___ الْوَاجِب الْيَوْم. (they, men)", "يَكْتُبُوا", ["يَكْتُبُون", "يَكْتُب", "تَكْتُبُوا"], "They (men) after لَنْ: ـُوا.", tr="They will not do the homework today."),
        F("لَنْ ___ إِلَى الْبَيْت قَبْلَ الْعَشَاء. (we)", "نَرْجِع", ["أَرْجِع", "يَرْجِعُوا", "تَرْجِعِي"], "We: نَـ.", tr="We will not go back home before dinner."),
    ],
    verify=vv("ذهب", "sub", ana="أَذْهَب", nahnu="نَذْهَب", anta="تَذْهَب", anti="تَذْهَبِي", huwa="يَذْهَب", hum="يَذْهَبُوا")
    + vv("رجع", "sub", nahnu="نَرْجِع") + vv("درس", "sub", hiya="تَدْرُس") + vv("كتب", "sub", hum="يَكْتُبُوا") + vv("جلس", "sub", anti="تَجْلِسِي")
    + vv("ذهب", "jus", ana="أَذْهَب") + vw("لَنْ", "لَمْ", "وَلَنْ", "الْوَاجِب"),
)

# ---------------------------------------------------------------------------- 150
L150 = lesson(
    "Could you repeat?",
    "كَرِّرْ مِنْ فَضْلِكَ · هَلْ يُمْكِنُكَ أَنْ تُكَرِّر؟",
    requires=["فضل", "فهم", "كلمة", "معنى", "قول", "هنا"],
    cards=[
        card("Asking for help in class",
             "A command for Measure II is the present stem without its prefix: تُكَرِّر (you repeat) gives كَرِّرْ (repeat!). "
             "A command for Measure V drops one تَـ: تَتَكَلَّم gives تَكَلَّمْ. The endings for a woman and a group are the "
             "same as for any command: ـِي and ـُوا.",
             tables=[table(["English", "Arabic"],
                           [["Please repeat. (to a man)", "كَرِّرْ مِنْ فَضْلِكَ"], ["Please repeat. (to a woman)", "كَرِّرِي مِنْ فَضْلِكِ"],
                            ["Speak slowly. (to a man)", "تَكَلَّمْ بِبُطْء"], ["I did not understand.", "لَمْ أَفْهَمْ"],
                            ["What does this word mean?", "مَا مَعْنَى هَذِه الْكَلِمَة؟"],
                            ["How do I say “three” in English?", "كَيْفَ أَقُول «ثَلَاثَة» بِالْإِنْجِلِيزِيَّة؟"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Can you…? May I…?",
             "يُمْكِن means “it is possible”. Add an ending to say who: يُمْكِنُنِي (it is possible for me), يُمْكِنُكَ (for "
             "you, to a man), يُمْكِنُكِ (for you, to a woman). Then use أَنْ and a verb, as after يَجِب.",
             examples=[
                 ex("هَلْ يُمْكِنُكَ أَنْ تُكَرِّر؟", "Can you repeat? (to a man)", "يُمْكِنُكَ"),
                 ex("هَلْ يُمْكِنُكِ أَنْ تَتَكَلَّمِي بِبُطْء؟", "Can you speak slowly? (to a woman)", "يُمْكِنُكِ"),
                 ex("هَلْ يُمْكِنُنِي أَنْ أَجْلِس هُنَا؟", "May I sit here?", "يُمْكِنُنِي"),
                 ex("لَمْ أَفْهَمْ هَذِه الْكَلِمَة.", "I did not understand this word.", "لَمْ أَفْهَمْ"),
                 ex("مَا مَعْنَى هَذِه الْكَلِمَة؟", "What does this word mean?", "مَعْنَى"),
                 ex("كَرِّرُوا مِنْ فَضْلِكُمْ.", "Please repeat. (to a group)", "كَرِّرُوا"),
             ]),
    ],
    exercises=[
        M("Which means “Please repeat” (to a man)?", "كَرِّرْ مِنْ فَضْلِكَ", ["كَرِّرِي مِنْ فَضْلِكِ", "أُكَرِّر مِنْ فَضْلِكَ", "كَرَّرَ مِنْ فَضْلِكَ"], "The command has no prefix."),
        M("Which means “Please repeat” (to a woman)?", "كَرِّرِي مِنْ فَضْلِكِ", ["كَرِّرْ مِنْ فَضْلِكَ", "كَرِّرُوا مِنْ فَضْلِكُمْ", "تُكَرِّرِين مِنْ فَضْلِكِ"], "ـِي is added for a woman."),
        M("Which means “Speak slowly” (to a man)?", "تَكَلَّمْ بِبُطْء", ["أَتَكَلَّم بِبُطْء", "تَكَلَّمْتُ بِبُطْء", "يَتَكَلَّم بِبُطْء"], "The command from تَتَكَلَّم."),
        M("What does لَمْ أَفْهَمْ mean?", "I did not understand", ["I will not understand", "I do not know", "I understood"], "لَمْ + present = did not."),
        M("What does مَا مَعْنَى هَذِه الْكَلِمَة؟ ask?", "What does this word mean?", ["Where is this word?", "Who wrote this word?", "How do you spell this word?"], "مَعْنَى = meaning."),
        M("Which asks a man “Can you repeat?”", "هَلْ يُمْكِنُكَ أَنْ تُكَرِّر؟", ["هَلْ يُمْكِنُكِ أَنْ تُكَرِّر؟", "هَلْ يُمْكِنُنِي أَنْ أُكَرِّر؟", "هَلْ يُمْكِنُكَ أَنْ تَكَلَّمْ؟"], "يُمْكِنُكَ = for you (to a man)."),
        M("Which means “May I sit here?”", "هَلْ يُمْكِنُنِي أَنْ أَجْلِس هُنَا؟", ["هَلْ يُمْكِنُكَ أَنْ تَجْلِس هُنَا؟", "هَلْ يُمْكِنُنِي أَنْ نَجْلِس هُنَا؟", "هَلْ يُمْكِنُهُ أَنْ أَجْلِس هُنَا؟"], "ـنِي = me."),
        F("___ مِنْ فَضْلِكَ. (Please repeat, to a man)", "كَرِّرْ", ["كَرِّرِي", "تُكَرِّر", "كَرَّرْتُ"], "The command to a man.", tr="Please repeat."),
        F("هَلْ يُمْكِنُكِ أَنْ ___ بِبُطْء؟ (to a woman)", "تَتَكَلَّمِي", ["تَتَكَلَّمِين", "تَتَكَلَّم", "أَتَكَلَّم"], "After أَنْ the ـِين loses its ن.", tr="Can you speak slowly?"),
    ],
    verify=vw("كَرِّرْ", "كَرِّرِي", "كَرِّرُوا", "تَكَلَّمْ", "تَتَكَلَّمِي", "فَضْلِكَ", "فَضْلِكِ", "فَضْلِكُمْ", "بِبُطْء", "أَفْهَمْ", "مَعْنَى", "الْكَلِمَة",
              "يُمْكِنُكَ", "يُمْكِنُكِ", "يُمْكِنُنِي", "بِالْإِنْجِلِيزِيَّة", "أَقُول", "تُكَرِّر"),
)


# ---------------------------------------------------------------------------- 151
L151 = lesson(
    "The date",
    "الْيَوْم هُوَ الْخَامِس مِنْ مَارِس",
    requires=["تاريخ", "يوم", "شهر", "سادس", "سابع", "ثامن", "تاسع", "عاشر"],
    cards=[
        card("Ordinals for the days of the month",
             "The days of the month are numbered with masculine ordinals, because يَوْم is masculine. You know 1–5. Here "
             "are the next ones and some larger days. For 11–19 the ordinal is followed by عَشَرَ. From 21 the ordinal is "
             "joined with وَ to the ten, and the ten takes the ال: الْخَامِس وَالْعِشْرُون.",
             tables=[table(["Day", "Arabic"],
                           [["6th", "السَّادِس"], ["7th", "السَّابِع"], ["8th", "الثَّامِن"], ["9th", "التَّاسِع"], ["10th", "الْعَاشِر"],
                            ["11th", "الْحَادِيَ عَشَرَ"], ["12th", "الثَّانِيَ عَشَرَ"], ["15th", "الْخَامِسَ عَشَرَ"],
                            ["20th", "الْعِشْرُون"], ["25th", "الْخَامِس وَالْعِشْرُون"], ["30th", "الثَّلَاثُون"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Saying the date",
             "Ask مَا تَارِيخ الْيَوْم؟ (“what is today’s date?”). The answer is الْيَوْم هُوَ and the day, then مِنْ and the "
             "month. To say “on the 10th”, put فِي in front of the ordinal. After فِي the ending ـُون changes to ـِين.",
             examples=[
                 ex("مَا تَارِيخ الْيَوْم؟", "What is today’s date?", "تَارِيخ"),
                 ex("الْيَوْم هُوَ الْخَامِس مِنْ مَارِس.", "Today is the fifth of March.", "الْخَامِس مِنْ مَارِس"),
                 ex("الْيَوْم هُوَ الْحَادِيَ عَشَرَ مِنْ دِيسَمْبِر.", "Today is the eleventh of December.", "الْحَادِيَ عَشَرَ"),
                 ex("عِيد مِيلَادِي فِي الْعَاشِر مِنْ أُكْتُوبَر.", "My birthday is on the tenth of October.", "فِي الْعَاشِر"),
                 ex("سَنَذْهَب إِلَى الْمَكْتَبَة فِي الْعِشْرِين مِنْ نُوفِمْبِر.", "We will go to the library on the twentieth of November.", "فِي الْعِشْرِين"),
                 ex("اِمْتِحَانِي فِي الثَّالِث وَالْعِشْرِين مِنْ يَنَايِر.", "My exam is on the twenty-third of January.", "الثَّالِث وَالْعِشْرِين"),
             ]),
    ],
    exercises=[
        M("Which asks “What is today’s date?”", "مَا تَارِيخ الْيَوْم؟", ["مَا اِسْم الْيَوْم؟", "كَمِ السَّاعَة؟", "أَيْنَ الْيَوْم؟"], "تَارِيخ = date."),
        M("Which is “the seventh”? (masculine)", "السَّابِع", ["السَّادِس", "السَّابِعَة", "الثَّامِن"], "A day of the month is masculine."),
        M("Which is “the tenth”? (masculine)", "الْعَاشِر", ["الْعَاشِرَة", "التَّاسِع", "الْعِشْرُون"], "الْعَاشِر = tenth."),
        M("Which is “the eleventh”? (masculine)", "الْحَادِيَ عَشَرَ", ["الْحَادِيَةَ عَشْرَةَ", "الْعَاشِر", "أَحَدَ عَشَرَ"], "Masculine ordinal + عَشَرَ."),
        M("Which means “Today is the fifth of March”?", "الْيَوْم هُوَ الْخَامِس مِنْ مَارِس", ["الْيَوْم هُوَ الْخَامِسَة مِنْ مَارِس", "الْيَوْم هُوَ الْخَامِس مِنْ مَايُو", "غَدًا هُوَ الْخَامِس مِنْ مَارِس"], "الْيَوْم هُوَ + day + مِنْ + month."),
        M("Which means “My birthday is on the tenth of October”?", "عِيد مِيلَادِي فِي الْعَاشِر مِنْ أُكْتُوبَر", ["عِيد مِيلَادِي فِي التَّاسِع مِنْ أُكْتُوبَر", "عِيد مِيلَادِي فِي الْعَاشِر مِنْ نُوفِمْبِر", "عِيد مِيلَادِي فِي الْعَاشِرَة مِنْ أُكْتُوبَر"], "فِي + ordinal + مِنْ + month."),
        M("Which means “the twenty-fifth”? (masculine)", "الْخَامِس وَالْعِشْرُون", ["الْخَامِسَ عَشَرَ", "الْعِشْرُون وَالْخَامِس", "خَمْسَة وَعِشْرُون"], "Ordinal, وَ, then الْعِشْرُون."),
        F("الْيَوْم هُوَ الْحَادِيَ عَشَرَ ___ دِيسَمْبِر.", "مِنْ", ["فِي", "عَلَى", "مَعَ"], "“Of the month”.", tr="Today is the eleventh of December."),
        F("سَنَذْهَب إِلَى الْمَكْتَبَة فِي ___ مِنْ نُوفِمْبِر.", "الْعِشْرِين", ["الْعِشْرُون", "عِشْرِين", "الْعَاشِر"], "After فِي the ending is ـِين.", tr="We will go to the library on the twentieth of November."),
    ],
    verify=vw("تَارِيخ", "السَّادِس", "السَّابِع", "الثَّامِن", "التَّاسِع", "الْعَاشِر", "الْحَادِي", "الثَّانِي", "الْخَامِس", "عَشَرَ", "الْعِشْرُون", "الْعِشْرِين",
              "الثَّلَاثُون", "وَالْعِشْرُون", "وَالْعِشْرِين", "الثَّالِث", "مِيلَادِي", "اِمْتِحَانِي", "أُكْتُوبَر", "نُوفِمْبِر", "دِيسَمْبِر", "يَنَايِر"),
)

# ---------------------------------------------------------------------------- 152
L152 = lesson(
    "Holidays and good wishes",
    "عِيد سَعِيد · كُلّ عَام وَأَنْتَ بِخَيْر · مَبْرُوك",
    requires=["عيد", "عطلة", "سنة", "مبروك", "سعيد", "طويل"],
    cards=[
        card("Words for holidays",
             "عِيد is a feast or a holiday that comes back every year, such as a national day or a religious festival. "
             "عُطْلَة is time off work or school. A birthday is عِيد مِيلَاد, literally “a feast of birth”.",
             tables=[table(["English", "Arabic"],
                           [["holiday, feast", "عِيد"], ["time off, vacation", "عُطْلَة"], ["birthday", "عِيد مِيلَاد"],
                            ["New Year", "رَأْس السَّنَة"], ["national day", "الْعِيد الْوَطَنِيّ"], ["a long holiday", "عُطْلَة طَوِيلَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What to say",
             "On a feast or a birthday people say عِيد سَعِيد (“a happy feast”) or كُلّ عَام وَأَنْتَ بِخَيْر (“every year "
             "and you are well”). The answer is وَأَنْتَ بِخَيْر, “and you too”. For a woman the words change to وَأَنْتِ "
             "and for a group to وَأَنْتُمْ. For good news, say مَبْرُوك, “congratulations”. Many Arab countries have the "
             "feasts of the Islamic calendar, and Christian communities also celebrate عِيد الْمِيلَاد (Christmas).",
             examples=[
                 ex("عِيد سَعِيد!", "Happy holiday!", "عِيد سَعِيد"),
                 ex("كُلّ عَام وَأَنْتَ بِخَيْر.", "Many happy returns. (to a man)", "كُلّ عَام وَأَنْتَ بِخَيْر"),
                 ex("وَأَنْتِ بِخَيْر.", "And you too. (to a woman)", "وَأَنْتِ"),
                 ex("غَدًا عِيد مِيلَاد أُخْتِي.", "Tomorrow is my sister’s birthday.", "عِيد مِيلَاد"),
                 ex("عِنْدَنَا عُطْلَة طَوِيلَة فِي الْعِيد.", "We have a long holiday for the Eid.", "عُطْلَة طَوِيلَة"),
                 ex("أَيْنَ سَتَكُون فِي الْعُطْلَة؟", "Where will you be during the holiday? (to a man)", "سَتَكُون"),
             ]),
    ],
    exercises=[
        M("What does عِيد سَعِيد mean?", "Happy holiday", ["Good morning", "Welcome", "Good luck"], "سَعِيد = happy."),
        M("What does مَبْرُوك mean?", "congratulations", ["thank you", "welcome", "goodbye"], "مَبْرُوك = congratulations."),
        M("What does عُطْلَة mean?", "time off, vacation", ["birthday", "lesson", "exam"], "عُطْلَة = vacation."),
        M("Which means “birthday”?", "عِيد مِيلَاد", ["رَأْس السَّنَة", "عُطْلَة طَوِيلَة", "الْعِيد الْوَطَنِيّ"], "“Feast of birth”."),
        M("A man says كُلّ عَام وَأَنْتَ بِخَيْر. What do you answer?", "وَأَنْتَ بِخَيْر", ["مَبْرُوك", "عِيد مِيلَاد", "أَهْلًا"], "“And you too”."),
        M("How do you answer a woman who says كُلّ عَام وَأَنْتِ بِخَيْر?", "وَأَنْتِ بِخَيْر", ["وَأَنْتَ بِخَيْر", "وَأَنْتُمْ بِخَيْر", "وَهُوَ بِخَيْر"], "أَنْتِ = you (to a woman)."),
        M("Which means “We have a long holiday”?", "عِنْدَنَا عُطْلَة طَوِيلَة", ["عِنْدِي عُطْلَة طَوِيلَة", "عِنْدَنَا عُطْلَة قَصِيرَة", "عِنْدَهُمْ عُطْلَة طَوِيلَة"], "عِنْدَنَا = we have."),
        F("غَدًا عِيد ___ أُخْتِي.", "مِيلَاد", ["مِيلَادِي", "سَعِيد", "عُطْلَة"], "A birthday: عِيد مِيلَاد.", tr="Tomorrow is my sister’s birthday."),
        F("___ سَعِيد!", "عِيد", ["عُطْلَة", "مَبْرُوك", "غَدًا"], "A happy feast.", tr="Happy holiday!"),
    ],
    verify=vw("عِيد", "عُطْلَة", "مِيلَاد", "رَأْس", "الْوَطَنِيّ", "طَوِيلَة", "سَعِيد", "كُلّ", "عَام", "وَأَنْتَ", "وَأَنْتِ", "وَأَنْتُمْ", "بِخَيْر", "مَبْرُوك", "الْمِيلَاد",
              "عِنْدَنَا", "سَتَكُون", "الْعُطْلَة", "قَصِيرَة"),
)

# ---------------------------------------------------------------------------- 153
L153 = lesson(
    "Plans for the long weekend",
    "مَاذَا سَتَفْعَل؟ · سَنَذْهَب · لَنْ أَدْرُس",
    requires=["فعل", "ذهب", "لعب", "غد", "صديق", "أسبوع"],
    cards=[
        card("Asking about plans",
             "Use مَاذَا سَتَفْعَل؟ (“what will you do?”) and answer with سَـ for what you will do and لَنْ for what you "
             "will not do. A friend can invite you with هَلْ تُرِيد أَنْ تَذْهَب مَعِي؟",
             tables=[table(["Speaker A", "Speaker B"],
                           [["مَاذَا سَتَفْعَل غَدًا؟", "سَأَلْعَب مَعَ أَصْدِقَائِي."],
                            ["هَلْ تُرِيد أَنْ تَذْهَب مَعِي؟", "نَعَمْ، فِي أَيّ سَاعَة؟"],
                            ["فِي السَّاعَة الرَّابِعَة.", "حَسَنًا، سَنَذْهَب."]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("A holiday plan",
             "Here is a short text. Read it, then answer the questions.",
             examples=[
                 ex("فِي الْأُسْبُوع الْقَادِم عِنْدَنَا عُطْلَة طَوِيلَة.", "Next week we have a long holiday.", "الْأُسْبُوع الْقَادِم"),
                 ex("سَنَسْتَيْقِظ فِي السَّاعَة التَّاسِعَة وَلَنْ نَذْهَب إِلَى الْمَدْرَسَة.", "We will wake up at nine and we will not go to school.", "وَلَنْ نَذْهَب"),
                 ex("بَعْدَ الْإِفْطَار سَأُنَظِّف غُرْفَتِي وَأُرَتِّب كُتُبِي.", "After breakfast I will clean my room and tidy my books.", "سَأُنَظِّف"),
                 ex("فِي السَّاعَة الثَّانِيَة سَنَتَغَدَّى مَعَ الْأُسْرَة.", "At two o’clock we will have lunch with the family.", "سَنَتَغَدَّى"),
                 ex("يَجِب أَنْ أَكْتُب الْوَاجِب قَبْلَ الْعَشَاء.", "I must do my homework before dinner.", "يَجِب أَنْ أَكْتُب"),
                 ex("بَعْدَ ثَلَاثَة أَيَّام سَنَرْجِع إِلَى الْمَدْرَسَة.", "In three days we will go back to school.", "بَعْدَ ثَلَاثَة أَيَّام"),
             ]),
    ],
    exercises=[
        M("What does مَاذَا سَتَفْعَل غَدًا؟ ask?", "What will you do tomorrow?", ["What did you do yesterday?", "Where are you going?", "What time is it?"], "سَـ makes it future."),
        M("Which means “I will play with my friends”?", "سَأَلْعَب مَعَ أَصْدِقَائِي", ["لَعِبْتُ مَعَ أَصْدِقَائِي", "لَنْ أَلْعَب مَعَ أَصْدِقَائِي", "سَنَلْعَب مَعَ أَصْدِقَائِي"], "سَـ + أَلْعَب."),
        M("Which means “We will not go to school”?", "لَنْ نَذْهَب إِلَى الْمَدْرَسَة", ["سَنَذْهَب إِلَى الْمَدْرَسَة", "لَمْ نَذْهَب إِلَى الْمَدْرَسَة", "لَنْ أَذْهَب إِلَى الْمَدْرَسَة"], "لَنْ + نَـ."),
        M("Which means “After breakfast I will clean my room”?", "بَعْدَ الْإِفْطَار سَأُنَظِّف غُرْفَتِي", ["قَبْلَ الْإِفْطَار سَأُنَظِّف غُرْفَتِي", "بَعْدَ الْإِفْطَار نَظَّفْتُ غُرْفَتِي", "بَعْدَ الْإِفْطَار لَنْ أُنَظِّف غُرْفَتِي"], "Measure II in the future: سَأُنَظِّف."),
        M("Which means “I must do my homework before dinner”?", "يَجِب أَنْ أَكْتُب الْوَاجِب قَبْلَ الْعَشَاء", ["يَجِب أَنْ أَكْتُب الْوَاجِب بَعْدَ الْعَشَاء", "يَجِب أَنْ نَكْتُب الْوَاجِب قَبْلَ الْعَشَاء", "كَتَبْتُ الْوَاجِب قَبْلَ الْعَشَاء"], "يَجِب أَنْ + أَكْتُب."),
        M("Which means “In three days we will go back to school”?", "بَعْدَ ثَلَاثَة أَيَّام سَنَرْجِع إِلَى الْمَدْرَسَة", ["قَبْلَ ثَلَاثَة أَيَّام سَنَرْجِع إِلَى الْمَدْرَسَة", "بَعْدَ ثَلَاثَة أَيَّام لَنْ نَرْجِع إِلَى الْمَدْرَسَة", "بَعْدَ ثَلَاثَة أَيَّام سَأَرْجِع إِلَى الْمَدْرَسَة"], "بَعْدَ = in (a time)."),
        M("How does a friend invite you?", "هَلْ تُرِيد أَنْ تَذْهَب مَعِي؟", ["هَلْ ذَهَبْتَ مَعِي؟", "لَنْ تَذْهَب مَعِي", "مَاذَا فَعَلْتَ مَعِي؟"], "“Do you want to go with me?”"),
        F("مَاذَا ___ غَدًا؟ (to a man)", "سَتَفْعَل", ["سَأَفْعَل", "سَيَفْعَل", "فَعَلْتَ"], "You (man), future.", tr="What will you do tomorrow?"),
        F("سَنَسْتَيْقِظ فِي السَّاعَة التَّاسِعَة وَ___ نَذْهَب إِلَى الْمَدْرَسَة. (will not)", "لَنْ", ["لَمْ", "سَوْفَ", "قَدْ"], "A negative future.", tr="We will wake up at nine and we will not go to school."),
    ],
    verify=vv("فعل", "fut", anta="سَتَفْعَل") + vv("لعب", "fut", ana="سَأَلْعَب", nahnu="سَنَلْعَب") + vv("كتب", "pres", ana="أَكْتُب", nahnu="نَكْتُب")
    + vv("فعل", "past", anta="فَعَلْتَ") + vv("ذهب", "past", anta="ذَهَبْتَ")
    + vw("مَاذَا", "تُرِيد", "أَصْدِقَائِي", "سَنَسْتَيْقِظ", "سَأُنَظِّف", "وَأُرَتِّب", "غُرْفَتِي", "كُتُبِي", "سَنَتَغَدَّى", "الْإِفْطَار", "حَسَنًا", "لَعِبْتُ"),
)

# ---------------------------------------------------------------------------- 154
L154 = lesson(
    "Buying things",
    "كَمْ ثَمَن الْقَمِيص؟ · أَدْفَع خَمْسَة وَعِشْرِين دِينَارًا",
    requires=["ثمن", "دفع", "حقيبة", "كتاب", "سعر", "كم"],
    cards=[
        card("In the shop",
             "Use the numbers you know. أَدْفَع (I pay) is a regular verb. أُرِيد أَنْ أَشْتَرِي (“I want to "
             "buy”) is a phrase to learn as it is for now.",
             tables=[table(["English", "Arabic"],
                           [["shirt", "قَمِيص"], ["bag", "حَقِيبَة"], ["shoes", "حِذَاء"], ["watch", "سَاعَة"], ["book", "كِتَاب"],
                            ["I want to buy…", "أُرِيد أَنْ أَشْتَرِي"], ["I pay", "أَدْفَع"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Prices",
             "Ask كَمْ ثَمَن…؟ or بِكَمْ…؟ and answer with the number and the money.",
             examples=[
                 ex("كَمْ ثَمَن هَذَا الْقَمِيص؟", "How much is this shirt?", "كَمْ ثَمَن"),
                 ex("ثَمَنُهُ خَمْسَة وَعِشْرُون دِينَارًا.", "It costs twenty-five dinars.", "خَمْسَة وَعِشْرُون"),
                 ex("هَذِه الْحَقِيبَة غَالِيَة. ثَمَنُهَا مِئَة دُولَار.", "This bag is expensive. It costs a hundred dollars.", "غَالِيَة"),
                 ex("أُرِيد أَنْ أَشْتَرِي حِذَاء.", "I want to buy shoes.", "أُرِيد أَنْ أَشْتَرِي"),
                 ex("أَدْفَع ثَلَاثِين دِينَارًا.", "I pay thirty dinars.", "أَدْفَع"),
                 ex("هَلْ يُمْكِنُكَ أَنْ تُخَفِّض السِّعْر؟", "Can you lower the price? (to a man)", "تُخَفِّض"),
             ]),
    ],
    exercises=[
        M("What does قَمِيص mean?", "shirt", ["shoes", "bag", "watch"], "قَمِيص = shirt."),
        M("What does حِذَاء mean?", "shoes", ["shirt", "bag", "book"], "حِذَاء = shoes."),
        M("What does أَدْفَع mean?", "I pay", ["I buy", "I want", "I wear"], "دَفَعَ = to pay."),
        M("Which means “How much is this shirt?”", "كَمْ ثَمَن هَذَا الْقَمِيص؟", ["أَيْنَ هَذَا الْقَمِيص؟", "مَنْ هَذَا الْقَمِيص؟", "هَلْ هَذَا الْقَمِيص؟"], "كَمْ ثَمَن…؟"),
        M("Which means “It costs twenty-five dinars”?", "ثَمَنُهُ خَمْسَة وَعِشْرُون دِينَارًا", ["ثَمَنُهُ خَمْس وَعِشْرُون دِينَارًا", "ثَمَنُهُ خَمْسَة وَعِشْرُون دِينَار", "ثَمَنُهُ عِشْرُون دِينَارًا"], "Masculine noun: خَمْسَة; the noun is singular with ـًا."),
        M("Which means “I pay thirty dinars”?", "أَدْفَع ثَلَاثِين دِينَارًا", ["أَدْفَع ثَلَاثَة دَنَانِير", "أَدْفَع ثَلَاثَة عَشَرَ دِينَارًا", "نَدْفَع ثَلَاثِين دِينَارًا"], "30 + singular noun."),
        M("Which means “I want to buy shoes”?", "أُرِيد أَنْ أَشْتَرِي حِذَاء", ["أُرِيد أَنْ أَدْفَع حِذَاء", "أُرِيد أَنْ أَبِيع حِذَاء", "أَشْتَرِي أَنْ أُرِيد حِذَاء"], "أَشْتَرِي = I buy."),
        F("كَمْ ___ هَذَا الْقَمِيص؟", "ثَمَن", ["ثَمَنُهُ", "مِئَة", "غَالِي"], "“Price of…” is the first part of an iḍāfa.", tr="How much is this shirt?"),
        F("هَذِه الْحَقِيبَة ___.", "غَالِيَة", ["غَالِي", "رَخِيص", "كَبِير"], "حَقِيبَة is feminine.", tr="This bag is expensive."),
    ],
    verify=vv("دفع", "pres", ana="أَدْفَع") + vw("قَمِيص", "حَقِيبَة", "حِذَاء", "أَدْفَع", "أَشْتَرِي", "أَبِيع", "ثَمَنُهَا", "غَالِيَة", "ثَلَاثِين", "دِينَارًا", "تُخَفِّض", "السِّعْر", "الْقَمِيص"),
)


# ---------------------------------------------------------------------------- 155
L155 = lesson(
    "Review: time and numbers",
    "كَمِ السَّاعَة؟ · خَمْسَة وَعِشْرُون · مِئَة دِينَار",
    requires=["ساعة", "كم", "طالب", "عمر", "ثمن", "درس"],
    cards=[
        card("Questions with كَمْ",
             "Five short exchanges use the time, a count, an age and a price.",
             examples=[
                 ex("كَمِ السَّاعَة الْآن؟ السَّاعَة الثَّالِثَة وَالرُّبْع.", "What time is it now? It is a quarter past three."),
                 ex("مَتَى الدَّرْس؟ الدَّرْس فِي السَّاعَة الْخَامِسَة إِلَّا رُبْعًا.", "When is the lesson? The lesson is at a quarter to five."),
                 ex("كَمْ طَالِبًا فِي الصَّفّ؟ فِي الصَّفّ ثَمَانِيَةَ عَشَرَ طَالِبًا.", "How many students are in the class? There are eighteen students in the class."),
                 ex("كَمْ عُمْرُكِ؟ عُمْرِي خَمْس وَعِشْرُون سَنَةً.", "How old are you? (to a woman) I am twenty-five years old."),
                 ex("كَمْ ثَمَن هَذَا الْكِتَاب؟ ثَمَنُهُ مِئَة دِينَار.", "How much is this book? It costs a hundred dinars."),
                 ex("نَتَغَدَّى فِي السَّاعَة الثَّانِيَة وَالنِّصْف.", "We have lunch at half past two."),
             ]),
    ],
    exercises=[
        M("Which means “It is a quarter past three”?", "السَّاعَة الثَّالِثَة وَالرُّبْع", ["السَّاعَة الثَّالِثَة إِلَّا رُبْعًا", "السَّاعَة الرَّابِعَة وَالرُّبْع", "السَّاعَة الثَّالِثَة وَالنِّصْف"], "وَالرُّبْع = and a quarter."),
        M("Which means “a quarter to five”?", "الْخَامِسَة إِلَّا رُبْعًا", ["الْخَامِسَة وَالرُّبْع", "الرَّابِعَة إِلَّا رُبْعًا", "الْخَامِسَة وَالنِّصْف"], "إِلَّا = to."),
        M("Which means “eighteen students”? (masculine)", "ثَمَانِيَةَ عَشَرَ طَالِبًا", ["ثَمَانِي عَشْرَةَ طَالِبًا", "ثَمَانِيَةَ عَشَرَ طُلَّابًا", "ثَمَانُون طَالِبًا"], "18 + masculine singular."),
        M("Which means “twenty-five years old” (سَنَة is feminine)?", "خَمْس وَعِشْرُون سَنَةً", ["خَمْسَة وَعِشْرُون سَنَةً", "خَمْس وَعِشْرُون سَنَوَات", "خَمْسُون سَنَةً"], "Unit has the opposite gender: خَمْس."),
        M("Which means “a hundred dinars”?", "مِئَة دِينَار", ["مِئَة دِينَارًا", "مِئَة دَنَانِير", "عَشَرَة دَنَانِير"], "مِئَة + singular, no ـًا."),
        M("Which means “thirty”?", "ثَلَاثُون", ["ثَلَاثَة", "ثَمَانُون", "ثَلَاثَةَ عَشَرَ"], "ثَلَاثُون = 30."),
        M("Which asks “How old are you?” (to a woman)", "كَمْ عُمْرُكِ؟", ["كَمْ عُمْرُكَ؟", "كَمْ عُمْرِي؟", "كَمْ ثَمَنُكِ؟"], "ـكِ = your (to a woman)."),
        F("السَّاعَة ___ صَبَاحًا.", "الثَّامِنَة", ["الثَّمَانِيَة", "الثَّامِن", "ثَمَانُون"], "A feminine ordinal.", tr="It is eight o’clock in the morning."),
        F("فِي الصَّفّ اِثْنَا عَشَرَ ___.", "طَالِبًا", ["طَالِبَات", "طُلَّاب", "طَالِبَةً"], "Singular noun after 12.", tr="There are twelve students in the class."),
    ],
    verify=vw("الرُّبْع", "رُبْعًا", "النِّصْف", "الْخَامِسَة", "الثَّالِثَة", "الثَّامِنَة", "ثَمَانِيَة", "عَشَرَ", "عُمْرُكِ", "عُمْرُكَ", "عُمْرِي", "خَمْس", "وَعِشْرُون", "مِئَة", "دِينَار",
              "ثَلَاثُون", "ثَمَانُون", "ثَلَاثَةَ", "مَتَى", "اِثْنَا"),
)

# ---------------------------------------------------------------------------- 156
L156 = lesson(
    "Review: my day and my plans",
    "أَسْتَيْقِظ · أُنَظِّف · أَتَكَلَّم · لَنْ أَنَام",
    requires=["ساعة", "درس", "نام", "غد", "أسبوع", "عمل"],
    cards=[
        card("My day, my plans",
             "A student describes today and next week, with times, new verb patterns and لَنْ.",
             examples=[
                 ex("أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة وَأَتَنَاوَل الْإِفْطَار مَعَ أُسْرَتِي.", "I wake up at six and have breakfast with my family."),
                 ex("أَتَكَلَّم مَعَ مُدَرِّسِي بَعْدَ الدَّرْس وَأَتَعَلَّم كَلِمَات جَدِيدَة.", "I talk with my teacher after the lesson and learn new words."),
                 ex("أَتَغَدَّى فِي السَّاعَة الْوَاحِدَة ثُمَّ أُنَظِّف غُرْفَتِي.", "I have lunch at one and then I clean my room."),
                 ex("أَنَام فِي السَّاعَة الْعَاشِرَة وَالنِّصْف.", "I go to bed at half past ten."),
                 ex("فِي الْأُسْبُوع الْقَادِم عِنْدِي عُطْلَة، وَلَنْ أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة.", "Next week I have a holiday, and I will not wake up at six."),
                 ex("بَعْدَ ثَلَاثَة أَيَّام سَأَذْهَب مَعَ أَصْدِقَائِي إِلَى الْمَدِينَة.", "In three days I will go to the city with my friends."),
             ]),
    ],
    exercises=[
        M("Which means “I wake up at six”?", "أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة", ["أَنَام فِي السَّاعَة السَّادِسَة", "أَسْتَيْقِظ فِي السَّاعَة السَّابِعَة", "اِسْتَيْقَظْتُ فِي السَّاعَة السَّادِسَة"], "أَسْتَيْقِظ = I wake up."),
        M("Which means “I talk with my teacher”?", "أَتَكَلَّم مَعَ مُدَرِّسِي", ["أُدَرِّس مَعَ مُدَرِّسِي", "كَرِّرْ مَعَ مُدَرِّسِي", "أَتَكَلَّم عَنْ مُدَرِّسِي"], "Measure V: أَتَكَلَّم."),
        M("Which means “I learn new words”?", "أَتَعَلَّم كَلِمَات جَدِيدَة", ["أُعَلِّم كَلِمَات جَدِيدَة", "عَلَّمْتُ كَلِمَات جَدِيدَة", "أَتَكَلَّم كَلِمَات جَدِيدَة"], "تَعَلَّمَ = learn; عَلَّمَ = teach."),
        M("Which means “I clean my room”?", "أُنَظِّف غُرْفَتِي", ["أَنَام فِي غُرْفَتِي", "نَظَّفَ غُرْفَتِي", "لَنْ أَدْخُل غُرْفَتِي"], "Measure II present: أُنَظِّف."),
        M("Which means “I will not wake up at six”?", "لَنْ أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة", ["لَمْ أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة", "سَأَسْتَيْقِظ فِي السَّاعَة السَّادِسَة", "لَا أَسْتَيْقِظ فِي السَّاعَة السَّابِعَة"], "لَنْ for the future."),
        M("Which means “In three days I will go to the city”?", "بَعْدَ ثَلَاثَة أَيَّام سَأَذْهَب إِلَى الْمَدِينَة", ["قَبْلَ ثَلَاثَة أَيَّام ذَهَبْتُ إِلَى الْمَدِينَة", "بَعْدَ ثَلَاثَة أَيَّام لَنْ أَذْهَب إِلَى الْمَدِينَة", "بَعْدَ ثَلَاثَة أَيَّام سَنَذْهَب إِلَى الْمَدِينَة"], "بَعْدَ = in..."),
        M("Which means “I go to bed at half past ten”?", "أَنَام فِي السَّاعَة الْعَاشِرَة وَالنِّصْف", ["أَنَام فِي السَّاعَة الْعَاشِرَة وَالرُّبْع", "أَنَام فِي السَّاعَة الْحَادِيَةَ عَشْرَةَ وَالنِّصْف", "أَسْتَيْقِظ فِي السَّاعَة الْعَاشِرَة وَالنِّصْف"], "وَالنِّصْف = and a half."),
        F("أَتَغَدَّى فِي السَّاعَة الْوَاحِدَة ثُمَّ ___ غُرْفَتِي.", "أُنَظِّف", ["أَنَام", "أَسْتَيْقِظ", "أَذْهَب"], "Clean = Measure II.", tr="I have lunch at one and then I clean my room."),
        F("فِي الْأُسْبُوع الْقَادِم عِنْدِي عُطْلَة، وَ___ أَسْتَيْقِظ فِي السَّاعَة السَّادِسَة. (will not)", "لَنْ", ["لَمْ", "قَدْ", "مَا"], "A future negative.", tr="Next week I have a holiday, and I will not wake up at six."),
    ],
    verify=vw("أَسْتَيْقِظ", "أَتَنَاوَل", "أَتَكَلَّم", "أَتَعَلَّم", "أُنَظِّف", "أُدَرِّس", "أَتَغَدَّى", "أَنَام", "كَلِمَات", "جَدِيدَة", "الْمَدِينَة", "مُدَرِّسِي", "غُرْفَتِي",
              "ثُمَّ", "اِسْتَيْقَظْتُ", "عَلَّمْتُ", "نَظَّفَ", "كَرِّرْ"),
)

UNIT = unit("الْيَوْم وَالْغَد: my day, numbers and the future",
            [L139, L140, L141, L142, L143, L144, L145, L146, L147, L148, L149, L150, L151, L152, L153, L154, L155, L156])
