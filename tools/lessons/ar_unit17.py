"""Unit 17 (chapter 15): biographies — birth, generations, studies, careers, prizes, writers and artists, then review."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 249
L249 = lesson(
    "Where were you born? وُلِدْتُ",
    "وُلِدْتُ فِي مَدِينَة كَبِيرَة · وُلِدَتْ أُمِّي فِي قَرْيَة",
    requires=["ولد", "مدينة", "قرية", "بلد", "صيف", "شتاء", "مارس", "أب", "أم"],
    cards=[
        card("“Was born”",
             "To talk about a person’s life, you need the verb وُلِدَ (he was born). It is a passive verb: the first letter has a ḍamma and the second a kasra. "
             "You do not need the rest of the passive for now, only these forms. The endings are the same as for any past verb.",
             tables=[table(["English", "Arabic"],
                           [["I was born", "وُلِدْتُ"], ["you were born (to a man)", "وُلِدْتَ"], ["you were born (to a woman)", "وُلِدْتِ"], ["he was born", "وُلِدَ"],
                            ["she was born", "وُلِدَتْ"], ["we were born", "وُلِدْنَا"], ["they were born (men)", "وُلِدُوا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Where and when",
             "Use فِي for a place, a season or a month. To ask “Where were you born?”, put أَيْنَ first.",
             examples=[
                 ex("وُلِدْتُ فِي مَدِينَة كَبِيرَة.", "I was born in a big city.", "وُلِدْتُ"),
                 ex("أَيْنَ وُلِدْتَ؟", "Where were you born? (to a man)", "وُلِدْتَ"),
                 ex("وُلِدَتْ أُمِّي فِي قَرْيَة صَغِيرَة.", "My mother was born in a small village.", "وُلِدَتْ"),
                 ex("وُلِدَ أَبِي فِي الصَّيْف.", "My father was born in the summer.", "وُلِدَ"),
                 ex("وُلِدْنَا فِي أَمْرِيكَا، لَكِنْ أَصْل عَائِلَتِنَا مِنْ لُبْنَان.", "We were born in America, but our family’s origin is Lebanon.", "وُلِدْنَا"),
                 ex("وُلِدُوا فِي شَهْر مَارِس.", "They were born in the month of March.", "وُلِدُوا"),
             ]),
    ],
    exercises=[
        M("What does وُلِدْتُ mean?", "I was born", ["I lived", "I studied", "I travelled"], "وُلِدَ = he was born."),
        M("Which means “she was born”?", "وُلِدَتْ", ["وُلِدَ", "وُلِدْتُ", "وُلِدُوا"], "تْ = she."),
        M("Which means “we were born”?", "وُلِدْنَا", ["وُلِدْتُ", "وُلِدَتْ", "وُلِدُوا"], "ـنَا = we."),
        M("Which means “they were born” (men)?", "وُلِدُوا", ["وُلِدَ", "وُلِدْنَا", "وُلِدَتْ"], "ـُوا = they (men)."),
        M("What does أَيْنَ وُلِدْتَ؟ ask?", "Where were you born?", ["When did you arrive?", "Where do you live?", "What do you study?"], "أَيْنَ = where."),
        M("What does وُلِدَتْ أُمِّي فِي قَرْيَة صَغِيرَة mean?", "My mother was born in a small village", ["My mother lives in a small village", "My mother visited a small village", "My father was born in a village"], "وُلِدَتْ = she was born."),
        F("أَنَا ___ فِي مَدِينَة كَبِيرَة.", "وُلِدْتُ", ["وُلِدَ", "وُلِدَتْ", "وُلِدْنَا"], "I was born.", tr="I was born in a big city."),
        F("أُمِّي ___ فِي قَرْيَة صَغِيرَة.", "وُلِدَتْ", ["وُلِدَ", "وُلِدُوا", "وُلِدْتُ"], "She was born.", tr="My mother was born in a small village."),
        F("نَحْنُ ___ فِي أَمْرِيكَا.", "وُلِدْنَا", ["وُلِدْتُ", "وُلِدَ", "وُلِدُوا"], "We were born.", tr="We were born in America."),
    ],
    verify=vw("وُلِدَ", "وُلِدْتُ", "وُلِدْتَ", "وُلِدْتِ", "وُلِدَتْ", "وُلِدْنَا", "وُلِدُوا", "قَرْيَة", "أَمْرِيكَا", "لُبْنَان", "الصَّيْف", "مَارِس", "عَائِلَتِنَا", "لَكِنْ", "أُمِّي", "أَبِي"),
)

# ---------------------------------------------------------------------------- 250
L250 = lesson(
    "Grandparents and generations",
    "هَاجَرَ جَدِّي إِلَى أَمْرِيكَا · أَنَا مِنَ الْجِيل الثَّانِي",
    requires=["جد", "جدة", "جيل", "أول", "ثاني", "هاجر", "عائلة", "مدينة"],
    cards=[
        card("Family history words",
             "A grandfather is جَدّ and a grandmother is جَدَّة. A generation is جِيل. The first generation (الْجِيل الْأَوَّل) is the people who moved to the new country, "
             "and the second generation (الْجِيل الثَّانِي) is their children who grew up there. Grandchildren are أَحْفَاد.",
             tables=[table(["English", "Arabic"],
                           [["grandfather", "جَدّ"], ["grandmother", "جَدَّة"], ["generation", "جِيل"], ["first generation", "الْجِيل الْأَوَّل"],
                            ["second generation", "الْجِيل الثَّانِي"], ["grandchildren", "أَحْفَاد"], ["he emigrated", "هَاجَرَ"], ["he settled", "اِسْتَقَرَّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Telling a family story",
             "The verb هَاجَرَ (he emigrated) is followed by إِلَى and the new country. Use فِي to say where a family settled.",
             examples=[
                 ex("هَاجَرَ جَدِّي إِلَى أَمْرِيكَا.", "My grandfather emigrated to America.", "هَاجَرَ"),
                 ex("اِسْتَقَرَّ جَدِّي فِي مَدِينَة صَغِيرَة.", "My grandfather settled in a small town.", "اِسْتَقَرَّ"),
                 ex("جَدَّتِي تَعِيش مَعَنَا.", "My grandmother lives with us.", "جَدَّتِي"),
                 ex("الْجِيل الْأَوَّل مِنَ الْمُهَاجِرِين عَمِلَ كَثِيرًا.", "The first generation of immigrants worked a lot.", "الْجِيل الْأَوَّل"),
                 ex("أَنَا مِنَ الْجِيل الثَّانِي.", "I am of the second generation.", "الْجِيل الثَّانِي"),
                 ex("جَدِّي وَجَدَّتِي يَتَكَلَّمَان الْعَرَبِيَّة مَعَ الْأَحْفَاد.", "My grandparents speak Arabic with the grandchildren.", "يَتَكَلَّمَان"),
             ]),
    ],
    exercises=[
        M("Which means “grandmother”?", "جَدَّة", ["جَدّ", "جِيل", "أُمّ"], "جَدَّة = grandmother."),
        M("Which means “generation”?", "جِيل", ["جَدّ", "عَائِلَة", "عَام"], "جِيل = generation."),
        M("What does هَاجَرَ جَدِّي إِلَى أَمْرِيكَا mean?", "My grandfather emigrated to America", ["My grandfather visited America", "My grandfather was born in America", "My grandfather studied in America"], "هَاجَرَ = emigrated."),
        M("What does الْجِيل الثَّانِي mean?", "the second generation", ["the first generation", "the last year", "the second floor"], "ثَانِي = second."),
        M("Who are أَحْفَاد?", "grandchildren", ["grandparents", "neighbours", "teachers"], "أَحْفَاد = grandchildren."),
        M("Why is يَتَكَلَّمَان dual in “جَدِّي وَجَدَّتِي يَتَكَلَّمَان”?", "two people are speaking", ["it is a question", "it is a past verb", "it is a command"], "Two subjects → dual verb."),
        F("___ جَدِّي إِلَى أَمْرِيكَا.", "هَاجَرَ", ["هَاجَرُوا", "يُهَاجِر", "مُهَاجِر"], "A past verb for he.", tr="My grandfather emigrated to America."),
        F("أَنَا مِنَ الْجِيل ___.", "الثَّانِي", ["الثَّانِيَة", "ثَانِيًا", "اِثْنَان"], "Masculine ordinal to match جِيل.", tr="I am of the second generation."),
        F("جَدَّتِي ___ مَعَنَا.", "تَعِيش", ["يَعِيش", "أَعِيش", "نَعِيش"], "She lives.", tr="My grandmother lives with us.", lemma="عيش:pres:hiya"),
    ],
    verify=(vv("عيش", "pres", hiya="تَعِيش", huwa="يَعِيش", ana="أَعِيش", nahnu="نَعِيش")
            + vps("مُهَاجِر", "مُهَاجِرِين", "gen")
            + vw("جَدّ", "جَدَّة", "جَدِّي", "جَدَّتِي", "جِيل", "الْجِيل", "الْأَوَّل", "الثَّانِي", "أَحْفَاد", "الْأَحْفَاد", "هَاجَرَ", "اِسْتَقَرَّ", "الْمُهَاجِرِين", "يَتَكَلَّمَان", "مَعَنَا", "الثَّانِيَة", "ثَانِيًا", "اِثْنَان", "هَاجَرُوا", "يُهَاجِر", "مُهَاجِر", "عَائِلَة", "عَام")),
)

# ---------------------------------------------------------------------------- 251
L251 = lesson(
    "Studies and degrees",
    "دَرَسَ الْهَنْدَسَة · تَخَرَّجَتْ مِنَ الْجَامِعَة",
    requires=["درس", "تخرج", "جامعة", "شهادة", "معروف", "كيمياء", "هندسة", "طب", "ماجستير"],
    cards=[
        card("Degrees and subjects",
             "A degree or certificate is شَهَادَة. The main university degrees are الْبَكَالُورْيُوس (bachelor’s), الْمَاجِسْتِير (master’s) and الدُّكْتُورَاه (doctorate). "
             "You study a subject with دَرَسَ + the subject, you graduate with تَخَرَّجَ مِنْ + the university, and you receive a degree with حَصَلَ عَلَى.",
             tables=[table(["English", "Arabic"],
                           [["certificate; degree", "شَهَادَة"], ["master’s degree", "شَهَادَة الْمَاجِسْتِير"], ["doctorate", "شَهَادَة الدُّكْتُورَاه"],
                            ["well-known", "مَعْرُوف"], ["engineering", "الْهَنْدَسَة"], ["medicine", "الطِّبّ"], ["chemistry", "الْكِيمِيَاء"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A student’s history",
             "Put the facts in the order they happened: studied, graduated, received a degree. The verb حَصَلَ is followed by عَلَى.",
             examples=[
                 ex("دَرَسَ أَخِي الْهَنْدَسَة فِي جَامِعَة مَعْرُوفَة.", "My brother studied engineering at a well-known university.", "دَرَسَ"),
                 ex("تَخَرَّجَتْ لَيْلَى مِنَ الْجَامِعَة الْعَام الْمَاضِي.", "Laila graduated from the university last year.", "تَخَرَّجَتْ"),
                 ex("حَصَلَ عَادِل عَلَى شَهَادَة الْمَاجِسْتِير.", "Adel received a master’s degree.", "شَهَادَة الْمَاجِسْتِير"),
                 ex("تَدْرُس سَلْمَى الطِّبّ.", "Salma studies medicine.", "تَدْرُس"),
                 ex("بَعْد التَّخَرُّج عَمِلَ فِي شَرِكَة.", "After graduating he worked in a company.", "التَّخَرُّج"),
                 ex("سَتَحْصُل عَلَى شَهَادَة الدُّكْتُورَاه بَعْد سَنَتَيْن.", "She will receive the doctorate in two years.", "سَتَحْصُل"),
             ]),
    ],
    exercises=[
        M("What does شَهَادَة الْمَاجِسْتِير mean?", "master’s degree", ["school report", "driving licence", "birth certificate"], "شَهَادَة = certificate."),
        M("What does تَخَرَّجَتْ مِنَ الْجَامِعَة mean?", "she graduated from the university", ["she entered the university", "she left her house", "she visited the library"], "تَخَرَّجَ مِنْ = graduate from."),
        M("What does حَصَلَ عَادِل عَلَى شَهَادَة mean?", "Adel obtained a degree", ["Adel lost a certificate", "Adel taught a class", "Adel opened a shop"], "حَصَلَ عَلَى = obtained."),
        M("Which means “medicine”?", "الطِّبّ", ["الْهَنْدَسَة", "الْكِيمِيَاء", "الْأَدَب"], "طِبّ = medicine."),
        M("Which means “after graduating”?", "بَعْد التَّخَرُّج", ["قَبْل التَّخَرُّج", "بَعْد الْوُصُول", "بَعْد الْمُقَابَلَة"], "التَّخَرُّج = graduating."),
        M("Which means “She will receive”?", "سَتَحْصُل", ["حَصَلَتْ", "تَحْصُلِين", "سَيَحْصُل"], "سَـ + تَـ = she will."),
        F("دَرَسَ أَخِي ___ فِي جَامِعَة مَعْرُوفَة.", "الْهَنْدَسَة", ["الْمَاجِسْتِير", "شَهَادَة", "التَّخَرُّج"], "A subject.", tr="My brother studied engineering at a well-known university."),
        F("حَصَلَ عَادِل ___ شَهَادَة الْمَاجِسْتِير.", "عَلَى", ["مِنْ", "فِي", "إِلَى"], "حَصَلَ عَلَى.", tr="Adel received a master’s degree."),
        F("هِيَ ___ مِنَ الْجَامِعَة الْعَام الْمَاضِي.", "تَخَرَّجَتْ", ["تَخَرَّجَ", "تَخَرَّجُوا", "تَخَرَّجْتُ"], "She.", tr="She graduated from the university last year.", lemma="خرج#5:past:hiya"),
    ],
    verify=(vv("خرج#5", "past", hiya="تَخَرَّجَتْ", huwa="تَخَرَّجَ") + vv("حصل", "pres", hiya="تَحْصُل", huwa="يَحْصُل") + vv("درس", "pres", hiya="تَدْرُس") + vv("حصل", "fut", hiya="سَتَحْصُل")
            + vw("شَهَادَة", "الْمَاجِسْتِير", "الدُّكْتُورَاه", "الْبَكَالُورْيُوس", "مَعْرُوف", "مَعْرُوفَة", "الْهَنْدَسَة", "الطِّبّ", "الْكِيمِيَاء", "الْأَدَب", "جَامِعَة", "الْمَاضِي", "التَّخَرُّج", "عَادِل", "لَيْلَى", "سَلْمَى", "سَنَتَيْن", "الْوُصُول", "الْمُقَابَلَة", "تَحْصُلِين", "سَيَحْصُل")),
)

# ---------------------------------------------------------------------------- 252
L252 = lesson(
    "Careers and retiring",
    "عَمِلَ أَبِي مُدِيرًا · تَقَاعَدَ جَدِّي",
    requires=["عمل", "مدير", "منصب", "شركة", "تقاعد", "مهندس", "طبيب", "عام", "سن"],
    cards=[
        card("Working as…",
             "To say “worked as a manager”, put the job after عَمِلَ with tanwīn fatḥa: عَمِلَ مُدِيرًا. A job or position is مَنْصِب, a general manager is مُدِير عَامّ, "
             "and to retire is تَقَاعَدَ (a Measure VI verb). The verbal noun is التَّقَاعُد (retirement).",
             tables=[table(["English", "Arabic"],
                           [["he worked as a manager", "عَمِلَ مُدِيرًا"], ["she worked as a doctor", "عَمِلَتْ طَبِيبَةً"], ["he will work as an engineer", "سَيَعْمَل مُهَنْدِسًا"],
                            ["position", "مَنْصِب"], ["general manager", "مُدِير عَامّ"], ["he retired", "تَقَاعَدَ"], ["retirement", "التَّقَاعُد"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A career story",
             "Use ثُمَّ (then) and بَعْد (after) to put events in order.",
             examples=[
                 ex("عَمِلَ أَبِي مُدِيرًا فِي شَرِكَة كَبِيرَة.", "My father worked as a manager in a big company.", "مُدِيرًا"),
                 ex("عَمِلَتْ أُمِّي طَبِيبَةً فِي مُسْتَشْفَى الْمَدِينَة.", "My mother worked as a doctor in the city hospital.", "طَبِيبَةً"),
                 ex("هَذَا هُوَ الْمَنْصِب الْجَدِيد.", "This is the new position.", "الْمَنْصِب"),
                 ex("تَقَاعَدَ جَدِّي قَبْل سَنَتَيْن.", "My grandfather retired two years ago.", "تَقَاعَدَ"),
                 ex("بَعْد التَّقَاعُد يُحِبّ جَدِّي قِرَاءَة الْجَرِيدَة.", "After retirement my grandfather likes reading the newspaper.", "التَّقَاعُد"),
                 ex("سَيَعْمَل أَخِي مُهَنْدِسًا فِي شَرِكَة مَعْرُوفَة.", "My brother will work as an engineer in a well-known company.", "مُهَنْدِسًا"),
             ]),
    ],
    exercises=[
        M("What does عَمِلَ أَبِي مُدِيرًا mean?", "My father worked as a manager", ["My father met a manager", "My father visited a manager", "My father became a doctor"], "عَمِلَ + job = worked as."),
        M("What does تَقَاعَدَ جَدِّي mean?", "My grandfather retired", ["My grandfather travelled", "My grandfather got a job", "My grandfather was born"], "تَقَاعَدَ = he retired."),
        M("What does مَنْصِب mean?", "position", ["salary", "holiday", "desk"], "مَنْصِب = post, position."),
        M("What is the verbal noun of تَقَاعَدَ?", "التَّقَاعُد", ["التَّعَاوُن", "التَّبَادُل", "التَّنَافُس"], "تَفَاعُل pattern."),
        M("Which means “she worked as a doctor”?", "عَمِلَتْ طَبِيبَةً", ["عَمِلَ طَبِيبًا", "سَتَعْمَل طَبِيبَةً", "عَمِلُوا أَطِبَّاءَ"], "تْ = she; feminine job."),
        M("Which means “he will work as an engineer”?", "سَيَعْمَل مُهَنْدِسًا", ["عَمِلَ مُهَنْدِسًا", "سَتَعْمَل مُهَنْدِسَةً", "لَنْ يَعْمَلُوا مُهَنْدِسِين"], "سَـ + يَـ."),
        F("عَمِلَ أَبِي ___ فِي شَرِكَة كَبِيرَة.", "مُدِيرًا", ["مُدِير", "مُدِيرَة", "مُدَرِّس"], "Job after عَمِلَ, with tanwīn fatḥa.", tr="My father worked as a manager in a big company."),
        F("___ جَدِّي قَبْل سَنَتَيْن.", "تَقَاعَدَ", ["تَقَاعَدَتْ", "يَتَقَاعَد", "التَّقَاعُد"], "A past verb for he.", tr="My grandfather retired two years ago."),
        F("بَعْد ___ يُحِبّ جَدِّي قِرَاءَة الْجَرِيدَة.", "التَّقَاعُد", ["تَقَاعَدَ", "يَتَقَاعَد", "مُتَقَاعِد"], "A verbal noun after بَعْد.", tr="After retirement my grandfather likes reading the newspaper."),
    ],
    verify=(vv("عمل", "past", huwa="عَمِلَ", hiya="عَمِلَتْ") + vv("عمل", "pres", huwa="يَعْمَل") + vv("عمل", "fut", huwa="سَيَعْمَل", hiya="سَتَعْمَل")
            + vw("عَمِلَ", "عَمِلَتْ", "مُدِيرًا", "مُدِير", "مُدِيرَة", "مُدَرِّس", "طَبِيبَةً", "طَبِيبًا", "مُهَنْدِسًا", "مَنْصِب", "الْمَنْصِب", "عَامّ", "تَقَاعَدَ", "التَّقَاعُد", "سَنَتَيْن", "التَّعَاوُن", "التَّبَادُل", "التَّنَافُس",
                  "مُسْتَشْفَى", "مَعْرُوفَة", "قِرَاءَة", "جَدِّي", "تَقَاعَدَتْ", "يَتَقَاعَد", "مُتَقَاعِد")),
)

# ---------------------------------------------------------------------------- 253
L253 = lesson(
    "Winning a prize: فَازَ بِـ",
    "فَازَ الْفَرِيق بِالْمُبَارَاة · فَازَتْ سَلْمَى بِجَائِزَة",
    requires=["فاز", "جائزة", "فريق", "مباراة", "علم", "كيمياء", "مصري", "أمريكي"],
    cards=[
        card("A hollow verb: فَازَ",
             "The verb فَازَ (he won) is hollow, like قَالَ: the middle letter is و. Before the endings ـتُ, ـتَ, ـتِ, ـنَا and ـنَ the long ā drops and the first letter takes a ḍamma: فُزْتُ (I won), فُزْنَا (we won). "
             "The present is يَفُوز (he wins), أَفُوز (I win). After فَازَ the prize takes بِـ: فَازَ بِجَائِزَة.",
             tables=[table(["English", "Arabic"],
                           [["I won", "فُزْتُ"], ["we won", "فُزْنَا"], ["he won", "فَازَ"], ["she won", "فَازَتْ"], ["they won (men)", "فَازُوا"],
                            ["he wins", "يَفُوز"], ["we will win", "سَنَفُوز"], ["they (men) will not win", "لَنْ يَفُوزُوا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Winners",
             "A prize is جَائِزَة. The Nobel Prize is جَائِزَة نُوبِل. As a real example, the Egyptian-American scientist أَحْمَد زُوَيْل won the Nobel Prize in Chemistry near the end of the twentieth century. "
             "Other sentences below are invented.",
             examples=[
                 ex("فَازَ الْفَرِيق بِالْمُبَارَاة.", "The team won the match.", "فَازَ"),
                 ex("فَازَتْ سَلْمَى بِجَائِزَة فِي الْمَدْرَسَة.", "Salma won a prize at school.", "فَازَتْ"),
                 ex("فَازَ الْعَالِم أَحْمَد زُوَيْل بِجَائِزَة نُوبِل فِي الْكِيمِيَاء.", "The scientist Ahmed Zewail won the Nobel Prize in Chemistry.", "جَائِزَة نُوبِل"),
                 ex("فُزْنَا بِالْمُبَارَاة الْأُولَى.", "We won the first match.", "فُزْنَا"),
                 ex("سَنَفُوز غَدًا.", "We will win tomorrow.", "سَنَفُوز"),
                 ex("لَنْ يَفُوزُوا بِهَذِهِ الْجَائِزَة.", "They will not win this prize.", "لَنْ يَفُوزُوا"),
             ]),
    ],
    exercises=[
        M("What does فَازَ الْفَرِيق بِالْمُبَارَاة mean?", "The team won the match", ["The team lost the match", "The team left the match", "The team watched the match"], "فَازَ بِـ = won."),
        M("Which means “we won”?", "فُزْنَا", ["فَازَ", "فُزْتُ", "فَازُوا"], "ـنَا = we; the long ā drops and the first letter takes a ḍamma."),
        M("Which means “I won”?", "فُزْتُ", ["فُزْنَا", "فَازَتْ", "فَازَ"], "ـتُ = I."),
        M("Which means “she won”?", "فَازَتْ", ["فَازَ", "فَازُوا", "فُزْتِ"], "تْ = she."),
        M("What does جَائِزَة نُوبِل mean?", "the Nobel Prize", ["the Nobel School", "a Nobel book", "the Nobel team"], "جَائِزَة = prize."),
        M("Which means “They will not win”? (men)", "لَنْ يَفُوزُوا", ["لَنْ يَفُوزُون", "لَمْ يَفُوزُوا", "سَيَفُوزُوا"], "لَنْ + the shortened present."),
        F("أَنَا ___ بِالْجَائِزَة.", "فُزْتُ", ["فَازَ", "فَازَتْ", "فُزْنَا"], "I won.", tr="I won the prize.", lemma="فوز:past:ana"),
        F("الْفَرِيق ___ غَدًا.", "سَيَفُوز", ["فَازَ", "فُزْنَا", "لَنْ يَفُوزُوا"], "Tomorrow: future with سَـ.", tr="The team will win tomorrow.", lemma="فوز:fut:huwa"),
        F("فَازَتْ سَلْمَى ___ جَائِزَة فِي الْمَدْرَسَة.", "بِ", ["فِي", "مِنْ", "إِلَى"], "فَازَ is followed by بِـ.", tr="Salma won a prize at school."),
    ],
    verify=(vv("فوز", "past", ana="فُزْتُ", nahnu="فُزْنَا", huwa="فَازَ", hiya="فَازَتْ", hum="فَازُوا", anta="فُزْتَ")
            + vv("فوز", "pres", huwa="يَفُوز", ana="أَفُوز") + vv("فوز", "fut", nahnu="سَنَفُوز", huwa="سَيَفُوز") + vv("فوز", "sub", hum="يَفُوزُوا") + vv("فوز", "jus", hum="يَفُوزُوا")
            + vw("فَازَ", "فَازَتْ", "فُزْتُ", "فُزْنَا", "جَائِزَة", "نُوبِل", "زُوَيْل", "أَحْمَد", "الْفَرِيق", "بِالْمُبَارَاة", "بِجَائِزَة", "الْعَالِم", "الْكِيمِيَاء", "الْأُولَى", "بِالْجَائِزَة")),
)

# ---------------------------------------------------------------------------- 254
L254 = lesson(
    "Writers, poets and artists",
    "جُبْرَان خَلِيل جُبْرَان شَاعِر وَرَسَّام",
    requires=["شاعر", "رسام", "فنان", "أديب", "عالم", "مشهور", "معروف", "رواية", "قصيدة", "أدب"],
    cards=[
        card("Creative people",
             "A poet is شَاعِر, a painter is رَسَّام, an artist is فَنَّان, a man of letters is أَدِيب (a woman: أَدِيبَة) and a scientist is عَالِم. "
             "Famous is مَشْهُور and well-known is مَعْرُوف. To say what someone is famous for, use بِـ: مَشْهُور بِرِوَايَاتِهِ (famous for his novels).",
             tables=[table(["English", "Arabic"],
                           [["poet", "شَاعِر"], ["painter", "رَسَّام"], ["artist", "فَنَّان"], ["man of letters", "أَدِيب"], ["scientist", "عَالِم"],
                            ["novel", "رِوَايَة"], ["poem", "قَصِيدَة"], ["literature", "الْأَدَب"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A famous example",
             "Khalil Gibran (جُبْرَان خَلِيل جُبْرَان) is a well-known real example: a poet and painter from Lebanon who lived in America and wrote in both Arabic and English. "
             "The other sentences are invented for practice.",
             examples=[
                 ex("جُبْرَان خَلِيل جُبْرَان شَاعِر وَرَسَّام مِنْ لُبْنَان.", "Khalil Gibran is a poet and painter from Lebanon.", "شَاعِر وَرَسَّام"),
                 ex("عَاشَ فِي أَمْرِيكَا وَكَتَبَ بِالْعَرَبِيَّة وَالْإِنْجِلِيزِيَّة.", "He lived in America and wrote in Arabic and English.", "عَاشَ"),
                 ex("هَذِهِ الْأَدِيبَة مَشْهُورَة بِرِوَايَاتِهَا.", "This woman writer is famous for her novels.", "مَشْهُورَة"),
                 ex("هُوَ فَنَّان مَعْرُوف فِي الْمَدِينَة.", "He is a well-known artist in the city.", "مَعْرُوف"),
                 ex("كَتَبَ الشَّاعِر قَصِيدَة جَمِيلَة.", "The poet wrote a beautiful poem.", "قَصِيدَة"),
                 ex("أُحِبّ هَذَا الرَّسَّام.", "I like this painter.", "هَذَا الرَّسَّام"),
             ]),
    ],
    exercises=[
        M("Which word means “poet”?", "شَاعِر", ["رَسَّام", "عَالِم", "فَنَّان"], "شَاعِر = poet."),
        M("Which word means “painter”?", "رَسَّام", ["شَاعِر", "أَدِيب", "عَالِم"], "رَسَّام = painter."),
        M("What does مَشْهُور بِرِوَايَاتِهِ mean?", "famous for his novels", ["famous for his house", "famous for his school", "famous for his paintings"], "رِوَايَة = novel."),
        M("What does عَاشَ فِي أَمْرِيكَا وَكَتَبَ بِالْعَرَبِيَّة وَالْإِنْجِلِيزِيَّة mean?", "He lived in America and wrote in Arabic and English", ["He studied in America and worked in Arabic", "He visited America and read English", "He was born in America and sang in English"], "عَاشَ = lived; كَتَبَ = wrote."),
        M("Which is the feminine of أَدِيب?", "أَدِيبَة", ["أَدِيبَات", "أَدِيبَان", "أَدَب"], "Add ـَة."),
        M("Which means “scientist”?", "عَالِم", ["عَالَم", "عِلْم", "مُعَلِّم"], "عَالِم = scientist; عَالَم = world."),
        F("هَذِهِ الْأَدِيبَة ___ بِرِوَايَاتِهَا.", "مَشْهُورَة", ["مَشْهُور", "مَشْهُورُون", "شَهِيرَان"], "Feminine to match الْأَدِيبَة.", tr="This woman writer is famous for her novels."),
        F("كَتَبَ الشَّاعِر ___ جَمِيلَة.", "قَصِيدَة", ["رِوَايَة", "رَسَّام", "جَائِزَة"], "A poet writes a poem.", tr="The poet wrote a beautiful poem."),
        F("هُوَ ___ مَعْرُوف فِي الْمَدِينَة.", "فَنَّان", ["فَنَّانَة", "شَاعِرَة", "أَدِيبَة"], "Masculine to match مَعْرُوف.", tr="He is a well-known artist in the city."),
    ],
    verify=(vv("عيش", "past", huwa="عَاشَ") + vv("كتب", "past", huwa="كَتَبَ")
            + vw("شَاعِر", "رَسَّام", "فَنَّان", "أَدِيب", "أَدِيبَة", "عَالِم", "مَشْهُور", "مَشْهُورَة", "مَعْرُوف", "رِوَايَة", "رِوَايَاتِهَا", "رِوَايَاتِهِ", "قَصِيدَة", "الْأَدَب", "جُبْرَان", "خَلِيل", "بِالْعَرَبِيَّة", "وَالْإِنْجِلِيزِيَّة",
                  "الْأَدِيبَة", "الشَّاعِر", "الرَّسَّام", "أَدِيبَات", "أَدِيبَان", "أَدَب", "عَالَم", "عِلْم", "مُعَلِّم", "مَشْهُورُون", "شَهِيرَان", "فَنَّانَة", "شَاعِرَة", "جَائِزَة")),
)


# ---------------------------------------------------------------------------- 255
L255 = lesson(
    "Entertainment and sport: actors, singers, players",
    "هُوَ مُمَثِّل مَعْرُوف · غَنَّى الْمُطْرِب فِي حَفْل كَبِير",
    requires=["ممثل", "مخرج", "فيلم", "حفل", "لاعب", "فريق", "غنى", "جائزة", "أفضل", "موسيقى"],
    cards=[
        card("People of the stage and the pitch",
             "An actor is مُمَثِّل, a film director is مُخْرِج, a singer is مُطْرِب, and a player is لَاعِب. A film is فِيلْم, a concert or party is حَفْل, and music is مُوسِيقَى. "
             "The word أَفْضَل (best) can stand before a singular noun: أَفْضَل مُمَثِّل (best actor).",
             tables=[table(["English", "Arabic"],
                           [["actor", "مُمَثِّل"], ["film director", "مُخْرِج"], ["singer", "مُطْرِب"], ["player", "لَاعِب"],
                            ["film", "فِيلْم"], ["concert", "حَفْل"], ["team", "فَرِيق"], ["best actor", "أَفْضَل مُمَثِّل"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "The verb غَنَّى means “he sang”. It is a Measure II verb whose last letter is ى, so it ends in a long ā: غَنَّى.",
             examples=[
                 ex("هُوَ مُمَثِّل مَعْرُوف.", "He is a well-known actor.", "مُمَثِّل"),
                 ex("شَاهَدْنَا فِيلْمًا جَدِيدًا.", "We watched a new film.", "فِيلْمًا"),
                 ex("غَنَّى الْمُطْرِب فِي حَفْل كَبِير.", "The singer sang at a big concert.", "غَنَّى"),
                 ex("يَلْعَب اللَّاعِب فِي فَرِيق مَعْرُوف.", "The player plays in a well-known team.", "اللَّاعِب"),
                 ex("حَصَلَ الْمُمَثِّل عَلَى جَائِزَة أَفْضَل مُمَثِّل.", "The actor received the prize for best actor.", "أَفْضَل مُمَثِّل"),
                 ex("الْمُخْرِج الْجَدِيد شَابّ.", "The new director is a young man.", "الْمُخْرِج"),
             ]),
    ],
    exercises=[
        M("Which word means “actor”?", "مُمَثِّل", ["مُخْرِج", "لَاعِب", "مُطْرِب"], "مُمَثِّل = actor."),
        M("Which word means “singer”?", "مُطْرِب", ["مُمَثِّل", "شَاعِر", "رَسَّام"], "مُطْرِب = singer."),
        M("What does حَفْل mean?", "concert", ["market", "prize", "page"], "حَفْل = concert, party."),
        M("What does أَفْضَل مُمَثِّل mean?", "best actor", ["new actor", "old actor", "famous director"], "أَفْضَل = best."),
        M("What does غَنَّى الْمُطْرِب فِي حَفْل كَبِير mean?", "The singer sang at a big concert", ["The singer left a big concert", "The player won a big prize", "The actor watched a big film"], "غَنَّى = he sang."),
        M("Which means “We watched a new film”?", "شَاهَدْنَا فِيلْمًا جَدِيدًا", ["شَاهَدْتُ فِيلْمًا جَدِيدًا", "سَنُشَاهِد فِيلْمًا جَدِيدًا", "شَاهَدُوا فِيلْمًا جَدِيدًا"], "ـنَا = we."),
        F("هُوَ ___ مَعْرُوف.", "مُمَثِّل", ["فِيلْم", "حَفْل", "جَائِزَة"], "A person.", tr="He is a well-known actor."),
        F("يَلْعَب اللَّاعِب فِي ___ مَعْرُوف.", "فَرِيق", ["فِيلْم", "حَفْل", "مُخْرِج"], "A team.", tr="The player plays in a well-known team."),
        F("غَنَّى الْمُطْرِب فِي ___ كَبِير.", "حَفْل", ["فَرِيق", "مُمَثِّل", "جَائِزَة"], "A concert.", tr="The singer sang at a big concert."),
    ],
    verify=vw("مُمَثِّل", "الْمُمَثِّل", "مُخْرِج", "الْمُخْرِج", "مُطْرِب", "الْمُطْرِب", "لَاعِب", "اللَّاعِب", "فِيلْم", "فِيلْمًا", "حَفْل", "فَرِيق", "مُوسِيقَى", "أَفْضَل", "غَنَّى", "شَاهَدْنَا", "شَاهَدْتُ", "سَنُشَاهِد", "شَاهَدُوا", "جَائِزَة", "شَاعِر", "رَسَّام", "شَاب"),
)

# ---------------------------------------------------------------------------- 256
L256 = lesson(
    "Review: this and that, with people and the genitive",
    "هَذَا الشَّاعِر وَتِلْكَ الْأَدِيبَة · كُتُب هَؤُلَاءِ الْكُتَّاب",
    requires=["هذا", "ذلك", "كتاب", "كاتب", "عالم", "مشهور", "قصة", "كتب"],
    cards=[
        card("What to remember",
             "Demonstratives agree with the noun: هَذَا and ذَلِكَ for masculine singular, هَذِهِ and تِلْكَ for feminine singular, هَؤُلَاءِ and أُولَئِكَ for people in the plural. "
             "The noun after a demonstrative has ال. After a preposition, or after the first noun of an iḍāfa, the next noun is genitive (no ending shows in our spelling).",
             tables=[table(["English", "Arabic"],
                           [["this poet", "هَذَا الشَّاعِر"], ["that writer (woman)", "تِلْكَ الْأَدِيبَة"], ["these scientists", "هَؤُلَاءِ الْعُلَمَاء"],
                            ["those artists", "أُولَئِكَ الْفَنَّانُون"], ["this writer’s books", "كُتُب هَذَا الْكَاتِب"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In use",
             "A demonstrative can come before a definite noun (هَذَا الشَّاعِر, “this poet”) or stand alone as the subject: هَذَا شَاعِر (this is a poet).",
             examples=[
                 ex("هَذَا الشَّاعِر مِنْ لُبْنَان وَتِلْكَ الْأَدِيبَة مِنْ مِصْر.", "This poet is from Lebanon and that woman writer is from Egypt.", "هَذَا الشَّاعِر"),
                 ex("مَنْ هَؤُلَاءِ الْعُلَمَاء؟", "Who are these scientists?", "هَؤُلَاءِ"),
                 ex("أُولَئِكَ الْفَنَّانُون مَشْهُورُون فِي الْعَالَم الْعَرَبِيّ.", "Those artists are famous in the Arab world.", "أُولَئِكَ"),
                 ex("أُحِبّ كُتُب هَذَا الْكَاتِب.", "I like the books of this writer.", "كُتُب هَذَا الْكَاتِب"),
                 ex("قَرَأْتُ قِصَّة ذَلِكَ الْأَدِيب.", "I read the story of that man of letters.", "ذَلِكَ"),
                 ex("هَذِهِ الرِّوَايَة جَمِيلَة وَتِلْكَ الْقَصِيدَة قَصِيرَة.", "This novel is beautiful and that poem is short.", "تِلْكَ"),
             ]),
    ],
    exercises=[
        M("Which goes with الْأَدِيبَة (woman writer)?", "هَذِهِ", ["هَذَا", "هَؤُلَاءِ", "ذَلِكَ"], "Feminine singular."),
        M("Which means “those artists”?", "أُولَئِكَ الْفَنَّانُون", ["هَذَا الْفَنَّان", "هَؤُلَاءِ الْفَنَّانُون", "تِلْكَ الْفَنَّانَة"], "أُولَئِكَ = those (people)."),
        M("Which means “these scientists”?", "هَؤُلَاءِ الْعُلَمَاء", ["أُولَئِكَ الْعُلَمَاء", "هَذَا الْعَالِم", "هَذِهِ الْعَالِمَة"], "هَؤُلَاءِ = these (people)."),
        M("What does كُتُب هَذَا الْكَاتِب mean?", "the books of this writer", ["this writer’s house", "these writers’ books", "a book by that poet"], "كُتُب = books; الْكَاتِب = writer."),
        M("What does مَنْ هَؤُلَاءِ الْعُلَمَاء؟ ask?", "Who are these scientists?", ["Where are those artists?", "What does this poet write?", "When did they graduate?"], "مَنْ = who."),
        M("Which is feminine singular, “that”?", "تِلْكَ", ["ذَلِكَ", "أُولَئِكَ", "هَؤُلَاءِ"], "تِلْكَ = that (f.)."),
        F("___ الشَّاعِر مِنْ لُبْنَان.", "هَذَا", ["هَذِهِ", "هَؤُلَاءِ", "تِلْكَ"], "Masculine singular, near.", tr="This poet is from Lebanon."),
        F("قَرَأْتُ قِصَّة ___ الْأَدِيب.", "ذَلِكَ", ["تِلْكَ", "أُولَئِكَ", "هَذِهِ"], "Masculine singular, far.", tr="I read the story of that man of letters."),
        F("أُولَئِكَ الْفَنَّانُون ___ فِي الْعَالَم الْعَرَبِيّ.", "مَشْهُورُون", ["مَشْهُور", "مَشْهُورَة", "مَشْهُورَان"], "Men in the plural.", tr="Those artists are famous in the Arab world."),
    ],
    verify=(vpb("كِتَاب", "كُتُب") + vpb("عَالِم", "عُلَمَاء") + vps("فَنَّان", "فَنَّانُون")
            + vw("هَذَا", "هَذِهِ", "ذَلِكَ", "تِلْكَ", "هَؤُلَاءِ", "أُولَئِكَ", "الشَّاعِر", "الْأَدِيبَة", "الْعُلَمَاء", "الْفَنَّانُون", "الْفَنَّان", "الْفَنَّانَة", "كُتُب", "الْكَاتِب", "الْكُتَّاب", "قِصَّة", "الْأَدِيب", "الْعَالَم", "الْعَرَبِيّ",
                  "الرِّوَايَة", "الْقَصِيدَة", "قَصِيرَة", "مَشْهُورُون", "مَشْهُورَان", "الْعَالِم", "الْعَالِمَة", "قَرَأْتُ")),
)

# ---------------------------------------------------------------------------- 257
L257 = lesson(
    "Review: the most famous, the best, older than",
    "أَشْهَر شَاعِر · أَفْضَل لَاعِب · أَكْبَر مِنِّي",
    requires=["أكبر", "أجمل", "أفضل", "مشهور", "شاعر", "لاعب", "فرد", "شهرة", "رواية"],
    cards=[
        card("What to remember",
             "The comparative أَفْعَل is followed by مِنْ for “than”: أَكْبَر مِنِّي (older than me). "
             "For the superlative there are two ways. With an indefinite singular noun, the أَفْعَل word comes first: أَشْهَر شَاعِر (the most famous poet). "
             "With ال, it comes after the noun: الشَّاعِر الْأَشْهَر.",
             tables=[table(["English", "Arabic"],
                           [["the most famous poet", "أَشْهَر شَاعِر"], ["the best player", "أَفْضَل لَاعِب"], ["older than me", "أَكْبَر مِنِّي"],
                            ["more beautiful than that", "أَجْمَل مِنْ تِلْكَ"], ["the oldest member of the family", "أَكْبَر فَرْد فِي الْعَائِلَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("About people",
             "Remember that the superlative stays singular and masculine before an indefinite noun, even when the person is a woman: أَشْهَر أَدِيبَة. "
             "To say “the most famous of the poets”, put the superlative before a definite plural noun: أَشْهَر الشُّعَرَاء.",
             examples=[
                 ex("هُوَ أَشْهَر شَاعِر فِي الْمَدِينَة.", "He is the most famous poet in the city.", "أَشْهَر شَاعِر"),
                 ex("هِيَ أَكْبَر مِنْ أَخِي.", "She is older than my brother.", "أَكْبَر مِنْ"),
                 ex("هُوَ أَفْضَل لَاعِب فِي الْفَرِيق.", "He is the best player in the team.", "أَفْضَل لَاعِب"),
                 ex("هَذِهِ الرِّوَايَة أَجْمَل مِنْ تِلْكَ.", "This novel is more beautiful than that one.", "أَجْمَل مِنْ"),
                 ex("جَدِّي أَكْبَر فَرْد فِي الْعَائِلَة.", "My grandfather is the oldest member of the family.", "أَكْبَر فَرْد"),
                 ex("هِيَ أَشْهَر أَدِيبَة فِي الْقَرْيَة.", "She is the most famous woman writer in the village.", "أَشْهَر أَدِيبَة"),
             ]),
    ],
    exercises=[
        M("Which means “the best player”?", "أَفْضَل لَاعِب", ["أَشْهَر لَاعِب", "أَشْهَر شَاعِر", "أَكْبَر فَرْد"], "أَفْضَل before an indefinite noun."),
        M("What does هِيَ أَكْبَر مِنْ أَخِي mean?", "She is older than my brother", ["She is the oldest girl", "She is smaller than my brother", "My brother is older than she"], "أَكْبَر مِنْ = older than."),
        M("Which means “This novel is more beautiful than that one”?", "هَذِهِ الرِّوَايَة أَجْمَل مِنْ تِلْكَ", ["هَذِهِ الرِّوَايَة أَكْبَر مِنْ تِلْكَ", "هَذَا الْكِتَاب أَجْمَل مِنْ تِلْكَ", "تِلْكَ الرِّوَايَة أَجْمَل مِنْ هَذِهِ"], "تِلْكَ = that one (f.), because الرِّوَايَة is feminine."),
        M("Which means “the most famous poet”?", "أَشْهَر شَاعِر", ["شَاعِر أَشْهَر مِنْ", "الشَّاعِر مَشْهُور", "شُعَرَاء مَشْهُورُون"], "أَفْعَل + indefinite noun."),
        M("What does جَدِّي أَكْبَر فَرْد فِي الْعَائِلَة mean?", "My grandfather is the oldest member of the family", ["My grandfather is older than the family", "My grandfather is the family’s only member", "My grandfather is the tallest man"], "أَكْبَر فَرْد = the oldest member."),
        M("Which means “older than me”?", "أَكْبَر مِنِّي", ["أَكْبَر مِنَّا", "أَكْبَر مِنْهُ", "أَصْغَر مِنِّي"], "مِنِّي = than me."),
        F("هُوَ ___ شَاعِر فِي الْمَدِينَة.", "أَشْهَر", ["مَشْهُور", "الْمَشْهُور", "شُهْرَة"], "Superlative before an indefinite noun.", tr="He is the most famous poet in the city."),
        F("هَذِهِ الرِّوَايَة ___ مِنْ تِلْكَ.", "أَجْمَل", ["جَمِيلَة", "الْجَمِيل", "جَمِيل"], "Comparative + مِنْ.", tr="This novel is more beautiful than that one."),
        F("هِيَ ___ مِنْ أَخِي.", "أَكْبَر", ["كَبِيرَة", "كِبَار", "الْكَبِيرَة"], "Comparative + مِنْ.", tr="She is older than my brother."),
    ],
    verify=vw("أَشْهَر", "أَفْضَل", "أَكْبَر", "أَصْغَر", "أَجْمَل", "مِنِّي", "مِنَّا", "مِنْهُ", "شَاعِر", "لَاعِب", "لَاعِبَة", "فَرْد", "أَدِيبَة", "الرِّوَايَة", "الْقَرْيَة", "الْفَرِيق", "شُعَرَاء", "مَشْهُورُون", "الْمَشْهُور", "شُهْرَة", "جَمِيلَة", "الْجَمِيل", "كِبَار", "الْكَبِيرَة", "كَبِيرَة", "أَخِي"),
)

# ---------------------------------------------------------------------------- 258
L258 = lesson(
    "Review: hollow verbs and verbal nouns",
    "عَادَ ← عَوْدَة · فَازَ ← فَوْز · زَارَ ← زِيَارَة",
    requires=["عاد", "فاز", "زار", "نوم", "قول", "سير", "عودة", "فوز", "زيارة", "قيادة"],
    cards=[
        card("Verb to noun",
             "Hollow verbs (verbs with و or ي in the middle) are common in biographies. Their verbal nouns often have the pattern فَعْل, فَعْلَة or فِعَالَة, with the weak letter showing as و or ي: "
             "عَادَ → عَوْدَة, فَازَ → فَوْز, سَارَ → سَيْر, نَامَ → نَوْم, قَالَ → قَوْل, زَارَ → زِيَارَة, قَادَ → قِيَادَة.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["return", "عَادَ", "عَوْدَة"], ["win", "فَازَ", "فَوْز"], ["walk; go", "سَارَ", "سَيْر"], ["sleep", "نَامَ", "نَوْم"],
                            ["say", "قَالَ", "قَوْل"], ["visit", "زَارَ", "زِيَارَة"], ["drive; lead", "قَادَ", "قِيَادَة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("In sentences",
             "A verbal noun can take a pronoun ending: عَوْدَتُهُ (his return), and can follow بَعْد: بَعْد عَوْدَتِهِ (after his return).",
             examples=[
                 ex("بَعْد عَوْدَتِهِ إِلَى لُبْنَان كَتَبَ كِتَابًا.", "After his return to Lebanon he wrote a book.", "عَوْدَتِهِ"),
                 ex("فَرِحْنَا بِفَوْز الْفَرِيق.", "We rejoiced at the team’s win.", "فَوْز"),
                 ex("زِيَارَة الْجَدَّة كُلّ أُسْبُوع جَمِيلَة.", "Visiting grandmother every week is lovely.", "زِيَارَة"),
                 ex("النَّوْم مُهِمّ لِلْأَطْفَال.", "Sleep is important for children.", "النَّوْم"),
                 ex("زَارَ الشَّاعِر قَرْيَتَهُ وَعَادَ إِلَى أَمْرِيكَا.", "The poet visited his village and returned to America.", "عَادَ"),
                 ex("فَازَ الْفَرِيق، وَقَالَ الْمُدَرِّب كَلِمَة جَمِيلَة.", "The team won, and the coach said a nice word.", "قَالَ"),
             ]),
    ],
    exercises=[
        M("What is the verbal noun of عَادَ?", "عَوْدَة", ["عَيْش", "عَادَة", "عُود"], "عَوْدَة = return."),
        M("What is the verbal noun of فَازَ?", "فَوْز", ["فَاز", "فُوز", "فَيْز"], "فَوْز = winning."),
        M("What is the verbal noun of زَارَ?", "زِيَارَة", ["زِيَادَة", "زَائِر", "مَزَار"], "زِيَارَة = visiting."),
        M("What does بَعْد عَوْدَتِهِ mean?", "after his return", ["before his return", "after her return", "after our return"], "ـهِ = his."),
        M("What does النَّوْم مُهِمّ لِلْأَطْفَال mean?", "Sleep is important for children", ["Food is important for children", "Children are tired", "Reading is useful"], "نَوْم = sleep."),
        M("Which means “he returned”?", "عَادَ", ["عَاشَ", "عَامَ", "غَابَ"], "عَادَ = he returned."),
        F("بَعْد ___ إِلَى لُبْنَان كَتَبَ كِتَابًا.", "عَوْدَتِهِ", ["عَادَ", "يَعُود", "عَوْدَتُهُمْ"], "بَعْد + verbal noun + his.", tr="After his return to Lebanon he wrote a book."),
        F("زَارَ الشَّاعِر قَرْيَتَهُ وَ___ إِلَى أَمْرِيكَا.", "عَادَ", ["عَادُوا", "عُدْتُ", "عَادَتْ"], "He returned.", tr="The poet visited his village and returned to America.", lemma="عود:past:huwa"),
        F("فَرِحْنَا بِ___ الْفَرِيق.", "فَوْز", ["فَازَ", "يَفُوز", "فَائِز"], "A verbal noun after بِـ.", tr="We rejoiced at the team’s win."),
    ],
    verify=(vv("عود", "past", huwa="عَادَ", ana="عُدْتُ", nahnu="عُدْنَا", hum="عَادُوا", hiya="عَادَتْ") + vv("عود", "pres", huwa="يَعُود")
            + vv("زور", "past", huwa="زَارَ") + vv("قول", "past", huwa="قَالَ") + vv("سير", "past", huwa="سَارَ") + vv("نوم", "past", huwa="نَامَ") + vv("قود", "past", huwa="قَادَ")
            + vw("عَوْدَة", "فَوْز", "سَيْر", "نَوْم", "قَوْل", "زِيَارَة", "قِيَادَة", "عَوْدَتِهِ", "عَوْدَتُهُمْ", "فَرِحْنَا", "كِتَابًا", "الْجَدَّة", "النَّوْم", "لِلْأَطْفَال", "قَرْيَتَهُ", "الْمُدَرِّب", "كَلِمَة", "عِيَادَة", "عَيْش", "زِيَادَة", "عَادَة", "عُود", "فَاز", "فُوز", "فَيْز", "زَوْر", "زَائِر", "مَزَار", "عَاشَ", "عَامَ", "غَابَ", "فَائِز", "يَفُوز")),
)

# ---------------------------------------------------------------------------- 259
L259 = lesson(
    "Asking for biographical information",
    "أَيْنَ وُلِدْتِ؟ · مَاذَا دَرَسْتِ؟ · لِمَاذَا هَاجَرْتِ؟",
    requires=["أين", "متى", "ماذا", "لماذا", "ولد", "درس", "كتب", "عمل", "هاجر", "رواية"],
    cards=[
        card("Questions for a life story",
             "A question word comes first, then the past verb with the ending for “you”. To a man the ending is ـتَ, to a woman ـتِ. "
             "The answer uses ـتُ for “I”. Compare: أَيْنَ دَرَسْتِ؟ (Where did you study? to a woman) and دَرَسْتُ فِي جَامِعَة مَعْرُوفَة.",
             tables=[table(["Question (to a woman)", "Answer (“I”)"],
                           [["أَيْنَ وُلِدْتِ؟", "وُلِدْتُ فِي قَرْيَة صَغِيرَة"], ["مَتَى هَاجَرْتِ؟", "هَاجَرْتُ بَعْد التَّخَرُّج"], ["مَاذَا دَرَسْتِ؟", "دَرَسْتُ الْأَدَب"],
                            ["مَاذَا كَتَبْتِ؟", "كَتَبْتُ رِوَايَتَيْن"], ["لِمَاذَا هَاجَرْتِ؟", "هَاجَرْتُ لِأَدْرُس"]],
                           say=[0, 1], gloss=False)]),
        card("An interview (an invented practice dialogue)",
             "A journalist asks a made-up writer about her life. The questions are to a woman.",
             examples=[
                 ex("أَيْنَ وُلِدْتِ؟", "Where were you born?", "وُلِدْتِ"),
                 ex("وُلِدْتُ فِي قَرْيَة صَغِيرَة فِي لُبْنَان.", "I was born in a small village in Lebanon.", "وُلِدْتُ"),
                 ex("مَاذَا دَرَسْتِ فِي الْجَامِعَة؟", "What did you study at university?", "دَرَسْتِ"),
                 ex("دَرَسْتُ الْأَدَب ثُمَّ هَاجَرْتُ لِأَدْرُس فِي أَمْرِيكَا.", "I studied literature and then emigrated to study in America.", "هَاجَرْتُ"),
                 ex("مَاذَا كَتَبْتِ بَعْد ذَلِكَ؟", "What did you write after that?", "كَتَبْتِ"),
                 ex("كَتَبْتُ رِوَايَتَيْن وَقَصِيدَة طَوِيلَة.", "I wrote two novels and a long poem.", "رِوَايَتَيْن"),
             ]),
    ],
    exercises=[
        M("Which question asks “Where were you born?” (to a woman)", "أَيْنَ وُلِدْتِ؟", ["مَتَى وُلِدْتِ؟", "أَيْنَ دَرَسْتِ؟", "أَيْنَ عَمِلْتِ؟"], "أَيْنَ = where."),
        M("Which question asks “What did you study?” (to a woman)", "مَاذَا دَرَسْتِ؟", ["مَاذَا كَتَبْتِ؟", "لِمَاذَا دَرَسْتِ؟", "أَيْنَ دَرَسْتِ؟"], "مَاذَا = what."),
        M("What does لِمَاذَا هَاجَرْتِ؟ ask?", "Why did you emigrate?", ["When did you emigrate?", "Where did you emigrate?", "Who emigrated?"], "لِمَاذَا = why."),
        M("What does كَتَبْتُ رِوَايَتَيْن mean?", "I wrote two novels", ["I read two novels", "I sold two books", "I bought two stories"], "رِوَايَتَيْن = two novels."),
        M("Which ending is the answer for “I”?", "ـتُ", ["ـتِ", "ـتَ", "ـنَا"], "دَرَسْتُ = I studied."),
        M("What does مَتَى هَاجَرْتِ؟ ask?", "When did you emigrate?", ["Where did you live?", "Why did you travel?", "What did you write?"], "مَتَى = when."),
        F("مَاذَا ___ بَعْد ذَلِكَ؟ (to a woman)", "كَتَبْتِ", ["كَتَبْتُ", "كَتَبَتْ", "كَتَبْنَا"], "You (f.): ـتِ.", tr="What did you write after that?"),
        F("أَنَا ___ الْأَدَب.", "دَرَسْتُ", ["دَرَسْتِ", "دَرَسَتْ", "دَرَسْنَا"], "I: ـتُ.", tr="I studied literature."),
        F("أَيْنَ ___؟ (to a woman)", "وُلِدْتِ", ["وُلِدْتُ", "وُلِدَتْ", "وُلِدْنَا"], "You (f.): ـتِ.", tr="Where were you born?"),
    ],
    verify=(vv("كتب", "past", ana="كَتَبْتُ", anti="كَتَبْتِ", anta="كَتَبْتَ") + vv("درس", "past", ana="دَرَسْتُ", anti="دَرَسْتِ") + vv("درس", "sub", ana="أَدْرُس")
            + vw("وُلِدْتِ", "هَاجَرْتِ", "هَاجَرْتُ", "عَمِلْتِ", "دَرَسْتِ", "كَتَبْتِ", "رِوَايَتَيْن", "قَصِيدَة", "طَوِيلَة", "الْأَدَب", "التَّخَرُّج", "لِأَدْرُس", "مَتَى", "مَاذَا", "لِمَاذَا", "ذَلِكَ")),
)

# ---------------------------------------------------------------------------- 260
L260 = lesson(
    "Review: the life of Hind",
    "حَيَاة هِنْد: وُلِدَتْ فِي قَرْيَة صَغِيرَة",
    requires=["ولد", "هاجر", "درس", "تخرج", "عمل", "طبيب", "فاز", "جائزة", "تقاعد", "جد"],
    cards=[
        card("What to remember",
             "This lesson brings together the vocabulary of life stories: وُلِدَ (was born), هَاجَرَ (emigrated), دَرَسَ and تَخَرَّجَ (studied, graduated), عَمِلَ + job (worked as), "
             "فَازَ بِـ (won), تَقَاعَدَ (retired). Verbal nouns such as التَّخَرُّج and التَّقَاعُد can follow بَعْد.",
             tables=[table(["English", "Arabic"],
                           [["She was born in a village.", "وُلِدَتْ فِي قَرْيَة"], ["He emigrated to America.", "هَاجَرَ إِلَى أَمْرِيكَا"], ["She worked as a doctor.", "عَمِلَتْ طَبِيبَةً"],
                            ["She won a prize.", "فَازَتْ بِجَائِزَة"], ["After retirement…", "بَعْد التَّقَاعُد"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("The life of Hind (an invented practice text)",
             "Hind is an invented character. Her story is made up for practice.",
             examples=[
                 ex("وُلِدَتْ هِنْد فِي قَرْيَة صَغِيرَة فِي لُبْنَان.", "Hind was born in a small village in Lebanon.", "وُلِدَتْ"),
                 ex("هَاجَرَ جَدُّهَا إِلَى أَمْرِيكَا وَاسْتَقَرَّ فِي مَدِينَة كَبِيرَة.", "Her grandfather emigrated to America and settled in a big city.", "هَاجَرَ"),
                 ex("دَرَسَتْ هِنْد الطِّبّ فِي جَامِعَة مَعْرُوفَة وَتَخَرَّجَتْ بَعْد سِتّ سَنَوَات.", "Hind studied medicine at a well-known university and graduated after six years.", "تَخَرَّجَتْ"),
                 ex("بَعْد التَّخَرُّج عَمِلَتْ طَبِيبَةً فِي مُسْتَشْفَى كَبِير.", "After graduating she worked as a doctor in a big hospital.", "عَمِلَتْ طَبِيبَةً"),
                 ex("فَازَتْ بِجَائِزَة لِأَنَّهَا سَاعَدَتْ كَثِيرًا مِنَ النَّاس.", "She won a prize because she helped many people.", "فَازَتْ"),
                 ex("تَقَاعَدَتْ هِنْد وَهِيَ الْآن تَكْتُب رِوَايَة.", "Hind has retired and is now writing a novel.", "تَقَاعَدَتْ"),
             ]),
    ],
    exercises=[
        M("Where was Hind born?", "In a small village in Lebanon", ["In a big city in America", "In Egypt", "In a hospital"], "وُلِدَتْ فِي قَرْيَة صَغِيرَة فِي لُبْنَان."),
        M("What did Hind study?", "Medicine", ["Engineering", "Literature", "Chemistry"], "دَرَسَتْ الطِّبّ."),
        M("How long did she study?", "Six years", ["Two years", "Ten years", "One year"], "سِتّ سَنَوَات."),
        M("Why did she win a prize?", "Because she helped many people", ["Because she wrote a poem", "Because she graduated", "Because she emigrated"], "سَاعَدَتْ كَثِيرًا مِنَ النَّاس."),
        M("What is Hind doing now?", "Writing a novel", ["Working as a manager", "Studying medicine", "Singing"], "تَكْتُب رِوَايَة."),
        M("Who emigrated to America?", "Her grandfather", ["Her father", "Her sister", "Hind’s teacher"], "هَاجَرَ جَدُّهَا."),
        F("بَعْد ___ عَمِلَتْ طَبِيبَةً فِي مُسْتَشْفَى كَبِير.", "التَّخَرُّج", ["تَخَرَّجَتْ", "تَخْرِيج", "تَخَرَّجُوا"], "A verbal noun after بَعْد.", tr="After graduating she worked as a doctor in a big hospital."),
        F("___ هِنْد فِي قَرْيَة صَغِيرَة.", "وُلِدَتْ", ["وُلِدَ", "وُلِدْتُ", "وُلِدُوا"], "She was born.", tr="Hind was born in a small village."),
        F("فَازَتْ هِنْد ___ جَائِزَة.", "بِ", ["فِي", "مِنْ", "عَلَى"], "فَازَ is followed by بِـ.", tr="Hind won a prize."),
    ],
    verify=(vv("علم#5", "past", hiya="تَعَلَّمَتْ") + vv("خرج#5", "past", hiya="تَخَرَّجَتْ") + vv("فوز", "past", hiya="فَازَتْ") + vv("درس", "past", hiya="دَرَسَتْ") + vv("عمل", "past", hiya="عَمِلَتْ")
            + vv("كتب", "pres", hiya="تَكْتُب") + vn(3, "f", "ثَلَاث")
            + vw("هِنْد", "جَدُّهَا", "وَاسْتَقَرَّ", "سِتّ", "سَنَوَات", "لِأَنَّهَا", "سَاعَدَتْ", "كَثِيرًا", "تَقَاعَدَتْ", "الْآن", "تَخْرِيج", "طَبِيبَةً", "التَّخَرُّج")),
)


UNIT = unit("الْمُجْتَمَع وَالْأَعْلَام: people, generations and review", [L249, L250, L251, L252, L253, L254, L255, L256, L257, L258, L259, L260])
