"""Unit 16 (chapter 14): Arab communities abroad, media, verbs with plural endings, verbal nouns."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 231
L231 = lesson(
    "Arab communities in big cities",
    "تَعِيش جَالِيَة عَرَبِيَّة فِي هَذِهِ الْمَدِينَة",
    requires=["مهاجر", "هجرة", "جالية", "ولاية", "عاش", "مدينة", "حي", "أصل", "وصل"],
    cards=[
        card("Words for communities",
             "People who move to another country to live there are مُهَاجِرُون (immigrants). The move itself is هِجْرَة. "
             "A group of people from one country who live together abroad is a جَالِيَة (community). "
             "A state inside a country such as the United States is a وِلَايَة, and a neighbourhood is a حَيّ.",
             tables=[table(["English", "Arabic"],
                           [["immigrant", "مُهَاجِر"], ["immigration; emigrating", "هِجْرَة"], ["community abroad", "جَالِيَة"],
                            ["state (in a country)", "وِلَايَة"], ["neighbourhood", "حَيّ"], ["origin", "أَصْل"],
                            ["big city", "مَدِينَة كَبِيرَة"], ["big cities", "الْمُدُن الْكَبِيرَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Talking about where people live",
             "The verb عَاشَ means “to live”. Its present is يَعِيش (he lives), أَعِيش (I live), تَعِيش (she lives or you live). "
             "Use مِنْ to say where a family comes from and فِي to say where it lives.",
             examples=[
                 ex("يَعِيش كَثِير مِنَ الْعَرَب فِي الْمُدُن الْكَبِيرَة.", "Many Arabs live in big cities.", "يَعِيش"),
                 ex("فِي هَذِهِ الْمَدِينَة حَيّ عَرَبِيّ قَدِيم.", "In this city there is an old Arab neighbourhood.", "حَيّ"),
                 ex("أَصْل عَائِلَتِي مِنْ لُبْنَان وَأَنَا أَعِيش هُنَا.", "My family’s origin is Lebanon, and I live here.", "أَصْل"),
                 ex("وَصَلَ الْمُهَاجِرُون الْجُدُد فِي الصَّيْف.", "The new immigrants arrived in the summer.", "الْمُهَاجِرُون"),
                 ex("تَعِيش الْجَالِيَة الْعَرَبِيَّة فِي هَذِهِ الْوِلَايَة مُنْذُ سَنَوَات.", "The Arab community has lived in this state for years.", "الْجَالِيَة"),
                 ex("الْهِجْرَة قَرَار كَبِير.", "Emigrating is a big decision.", "الْهِجْرَة"),
             ]),
    ],
    exercises=[
        M("What does جَالِيَة mean?", "a community living abroad", ["a market", "a shop", "a family name"], "A group from one country living together abroad."),
        M("What does مُهَاجِر mean?", "immigrant", ["tourist", "guide", "driver"], "Someone who moves to live in another country."),
        M("Which word means “state” (in a country)?", "وِلَايَة", ["عَاصِمَة", "حَيّ", "نَهْر"], "وِلَايَة = state."),
        M("Which word means “neighbourhood”?", "حَيّ", ["جَبَل", "بَحْر", "شَارِع"], "حَيّ = neighbourhood."),
        M("What does يَعِيش كَثِير مِنَ الْعَرَب فِي الْمُدُن الْكَبِيرَة mean?", "Many Arabs live in big cities", ["Many Arabs visit small towns", "Few Arabs live in big cities", "Many cities are very old"], "يَعِيش = lives."),
        M("Which word means “origin”?", "أَصْل", ["أَهْل", "أَمْر", "أَرْض"], "أَصْل = origin."),
        F("أَنَا ___ فِي مَدِينَة كَبِيرَة.", "أَعِيش", ["يَعِيش", "تَعِيش", "نَعِيش"], "I live: the prefix is أ.", tr="I live in a big city.", lemma="عيش:pres:ana"),
        F("وَصَلَ ___ الْجُدُد فِي الصَّيْف.", "الْمُهَاجِرُون", ["الْمُهَاجِر", "الْهِجْرَة", "الْجَالِيَة"], "A plural noun to go with the plural adjective الْجُدُد.", tr="The new immigrants arrived in the summer."),
        F("فِي هَذِهِ الْمَدِينَة ___ عَرَبِيّ قَدِيم.", "حَيّ", ["جَبَل", "بَحْر", "نَهْر"], "A neighbourhood is part of a city.", tr="In this city there is an old Arab neighbourhood."),
    ],
    verify=(vv("عيش", "pres", ana="أَعِيش", huwa="يَعِيش", hiya="تَعِيش", nahnu="نَعِيش")
            + vps("مُهَاجِر", "مُهَاجِرُون") + vpb("مَدِينَة", "مُدُن")
            + vw("مُهَاجِر", "هِجْرَة", "جَالِيَة", "وِلَايَة", "حَيّ", "أَصْل", "الْمُدُن", "الْجُدُد", "مُنْذُ", "سَنَوَات", "قَرَار", "لُبْنَان", "جَبَل", "بَحْر", "نَهْر", "أَهْل", "أَمْر", "أَرْض")),
)

# ---------------------------------------------------------------------------- 232
L232 = lesson(
    "Most, many, some: أَغْلَب · كَثِير · بَعْض",
    "أَغْلَب الطُّلَّاب · كَثِير مِنَ النَّاس · بَعْض الْجِيرَان",
    requires=["أغلب", "معظم", "بعض", "كثير", "قليل", "جميع", "كل", "طفل", "جار", "لغة"],
    cards=[
        card("Words for “how many”",
             "These words come before a definite plural noun. أَغْلَب (most), مُعْظَم (most), بَعْض (some), جَمِيع and كُلّ (all) are joined to the noun like an iḍāfa: "
             "the noun after them has ال. The words كَثِير (many) and قَلِيل (few) usually take مِنْ: كَثِير مِنَ الطُّلَّاب.",
             tables=[table(["English", "Arabic"],
                           [["most of the students", "أَغْلَب الطُّلَّاب"], ["most of the shops", "مُعْظَم الْمَحَلَّات"], ["some of the neighbours", "بَعْض الْجِيرَان"],
                            ["all the students", "جَمِيع الطُّلَّاب"], ["many of the children", "كَثِير مِنَ الْأَطْفَال"], ["few of the people", "قَلِيل مِنَ النَّاس"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Majority and minority",
             "The majority is أَغْلَبِيَّة and a minority is أَقَلِّيَّة. After words like أَغْلَب and كَثِير, a verb about people is usually plural: يَدْرُسُون.",
             examples=[
                 ex("أَغْلَب الطُّلَّاب فِي صَفِّي يَدْرُسُون الْعَرَبِيَّة.", "Most of the students in my class study Arabic.", "أَغْلَب الطُّلَّاب"),
                 ex("بَعْض الْجِيرَان عَرَب وَبَعْضُهُم مِنْ بُلْدَان أُخْرَى.", "Some of the neighbours are Arabs and some are from other countries.", "بَعْض الْجِيرَان"),
                 ex("كَثِير مِنَ الْأَطْفَال يَتَكَلَّمُون لُغَتَيْن.", "Many of the children speak two languages.", "كَثِير مِنَ الْأَطْفَال"),
                 ex("الْأَغْلَبِيَّة تُحِبّ هَذَا الْمَطْعَم.", "The majority like this restaurant.", "الْأَغْلَبِيَّة"),
                 ex("هَذِهِ أَقَلِّيَّة صَغِيرَة فِي الْمَدِينَة.", "This is a small minority in the city.", "أَقَلِّيَّة"),
                 ex("قَلِيل مِنَ النَّاس يَعْرِفُون هَذَا الْحَيّ.", "Few people know this neighbourhood.", "قَلِيل مِنَ النَّاس"),
             ]),
    ],
    exercises=[
        M("Which means “most of the students”?", "أَغْلَب الطُّلَّاب", ["بَعْض الطُّلَّاب", "قَلِيل مِنَ الطُّلَّاب", "طَالِب وَاحِد"], "أَغْلَب = most."),
        M("Which means “some of the neighbours”?", "بَعْض الْجِيرَان", ["أَغْلَب الْجِيرَان", "جَمِيع الْجِيرَان", "جَار وَاحِد"], "بَعْض = some."),
        M("What does أَقَلِّيَّة mean?", "minority", ["majority", "origin", "visit"], "The smaller group."),
        M("What does أَغْلَبِيَّة mean?", "majority", ["minority", "city", "festival"], "The larger group."),
        M("Which means “many of the children”?", "كَثِير مِنَ الْأَطْفَال", ["قَلِيل مِنَ الْأَطْفَال", "بَعْض الْأَطْفَال", "طِفْل وَاحِد"], "كَثِير مِنْ = many of."),
        M("What does قَلِيل مِنَ النَّاس mean?", "few people", ["many people", "all the people", "no people"], "قَلِيل = few."),
        F("___ مِنَ الْأَطْفَال يَتَكَلَّمُون لُغَتَيْن.", "كَثِير", ["قَلِيل", "أَغْلَب", "مُعْظَم"], "“Many of” takes مِنَ; أَغْلَب and مُعْظَم do not.", tr="Many of the children speak two languages."),
        F("___ الطُّلَّاب فِي صَفِّي يَدْرُسُون الْعَرَبِيَّة.", "أَغْلَب", ["كَثِير", "قَلِيل", "جَمِيع"], "No مِنْ after أَغْلَب: the noun follows it directly.", tr="Most of the students in my class study Arabic."),
        F("___ الْجِيرَان عَرَب وَبَعْضُهُم مِنْ بُلْدَان أُخْرَى.", "بَعْض", ["أَقَلِّيَّة", "هِجْرَة", "جَالِيَة"], "Some … and some.", tr="Some of the neighbours are Arabs and some are from other countries."),
    ],
    verify=vw("أَغْلَب", "مُعْظَم", "بَعْض", "جَمِيع", "كَثِير", "قَلِيل", "أَغْلَبِيَّة", "أَقَلِّيَّة", "الْجِيرَان", "الْأَطْفَال", "الطُّلَّاب", "لُغَتَيْن", "بَعْضُهُم", "بُلْدَان", "أُخْرَى", "يَتَكَلَّمُون", "يَدْرُسُون", "يَعْرِفُون", "الْمَحَلَّات", "طِفْل"),
)

# ---------------------------------------------------------------------------- 233
L233 = lesson(
    "Nationality and residence permits",
    "جِنْسِيَّتِي مِصْرِيَّة · عِنْدِي إِقَامَة دَائِمَة",
    requires=["جنسية", "إقامة", "حصل", "وثيقة", "سفارة", "جواز", "سفر", "طلب"],
    cards=[
        card("Papers and permission",
             "Four words are useful for life abroad: جِنْسِيَّة (nationality or citizenship), إِقَامَة (residence), وَثِيقَة (a document; plural وَثَائِق) and جَوَاز سَفَر (passport). "
             "A permanent residence permit is إِقَامَة دَائِمَة. An embassy is سِفَارَة.",
             tables=[table(["English", "Arabic"],
                           [["nationality; citizenship", "جِنْسِيَّة"], ["residence", "إِقَامَة"], ["permanent residence", "إِقَامَة دَائِمَة"],
                            ["document", "وَثِيقَة"], ["documents", "وَثَائِق"], ["passport", "جَوَاز سَفَر"], ["embassy", "سِفَارَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Getting something",
             "To say “got” or “obtained”, use حَصَلَ عَلَى. Its past tense is regular: حَصَلْتُ (I got), حَصَلَ (he got), حَصَلَتْ (she got).",
             examples=[
                 ex("جِنْسِيَّتِي مِصْرِيَّة.", "My nationality is Egyptian.", "جِنْسِيَّتِي"),
                 ex("حَصَلَ أَخِي عَلَى الْجِنْسِيَّة الْجَدِيدَة.", "My brother obtained the new citizenship.", "حَصَلَ"),
                 ex("عِنْدِي إِقَامَة دَائِمَة فِي هَذَا الْبَلَد.", "I have permanent residence in this country.", "إِقَامَة دَائِمَة"),
                 ex("هَلْ حَصَلْتِ عَلَى الْإِقَامَة؟", "Did you get the residence permit? (to a woman)", "حَصَلْتِ"),
                 ex("تَطْلُب السِّفَارَة وَثَائِق كَثِيرَة.", "The embassy asks for many documents.", "وَثَائِق"),
                 ex("أَيْنَ جَوَاز سَفَرِي؟", "Where is my passport?", "جَوَاز سَفَرِي"),
             ]),
    ],
    exercises=[
        M("What does إِقَامَة دَائِمَة mean?", "permanent residence", ["a short visit", "a passport", "a new job"], "دَائِمَة = permanent."),
        M("What does جَوَاز سَفَر mean?", "passport", ["airport", "embassy", "hotel"], "سَفَر = travel."),
        M("Which word means “embassy”?", "سِفَارَة", ["جِنْسِيَّة", "وَثِيقَة", "إِقَامَة"], "سِفَارَة = embassy."),
        M("What does حَصَلَ أَخِي عَلَى الْجِنْسِيَّة mean?", "My brother obtained citizenship", ["My brother lost his passport", "My brother left the embassy", "My brother visited the city"], "حَصَلَ عَلَى = obtained."),
        M("Which means “documents”?", "وَثَائِق", ["وَثِيقَة", "وِلَايَة", "جَالِيَة"], "وَثَائِق = documents (plural)."),
        M("Which means “I got”?", "حَصَلْتُ", ["حَصَلَ", "حَصَلَتْ", "حَصَلْنَا"], "ـتُ = I."),
        F("أَنَا ___ عَلَى الْإِقَامَة.", "حَصَلْتُ", ["حَصَلَ", "حَصَلَتْ", "حَصَلْنَا"], "I got.", tr="I got the residence permit.", lemma="حصل:past:ana"),
        F("هِيَ ___ عَلَى الْجِنْسِيَّة.", "حَصَلَتْ", ["حَصَلَ", "حَصَلُوا", "حَصَلْتُ"], "She got.", tr="She obtained the citizenship.", lemma="حصل:past:hiya"),
        F("تَطْلُب السِّفَارَة ___ كَثِيرَة.", "وَثَائِق", ["جِنْسِيَّة", "إِقَامَة", "وِلَايَة"], "The embassy asks for papers.", tr="The embassy asks for many documents."),
    ],
    verify=(vv("حصل", "past", ana="حَصَلْتُ", huwa="حَصَلَ", hiya="حَصَلَتْ", anti="حَصَلْتِ", nahnu="حَصَلْنَا", hum="حَصَلُوا")
            + vpb("وَثِيقَة", "وَثَائِق")
            + vw("جِنْسِيَّة", "إِقَامَة", "دَائِمَة", "وَثِيقَة", "جَوَاز", "سَفَر", "السِّفَارَة", "الْجِنْسِيَّة", "الْإِقَامَة", "مِصْرِيَّة", "وِلَايَة", "جَالِيَة", "تَطْلُب")),
)

# ---------------------------------------------------------------------------- 234
L234 = lesson(
    "Work in the community: shops and free business",
    "أَبِي صَاحِب مَحَلّ صَغِير · أُمِّي طَبِيبَة",
    requires=["عمل", "حر", "تجارة", "تاجر", "صاحب", "محل", "شركة", "موظف", "طبيب", "مستشفى", "فتح"],
    cards=[
        card("Working for yourself",
             "Many people work for a company: مُوَظَّف (employee). Others own a business: صَاحِب مَحَلّ (shop owner) or تَاجِر (merchant). "
             "Work that you run yourself is الْعَمَل الْحُرّ (free work, self-employment). The word حُرّ means “free”.",
             tables=[table(["English", "Arabic"],
                           [["employee", "مُوَظَّف"], ["shop owner", "صَاحِب مَحَلّ"], ["merchant", "تَاجِر"],
                            ["company", "شَرِكَة"], ["self-employment", "الْعَمَل الْحُرّ"], ["a job", "وَظِيفَة"], ["doctor", "طَبِيب"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Describing a family’s work",
             "Use a simple sentence without “is”: أَبِي صَاحِب مَحَلّ. The verb فَتَحَ (he opened) is also useful, "
             "and its object takes tanwīn with fatḥa: فَتَحَ مَحَلًّا. Ask “Do you have a job?” with عِنْدَك وَظِيفَة؟",
             examples=[
                 ex("أَبِي صَاحِب مَحَلّ صَغِير.", "My father owns a small shop.", "صَاحِب مَحَلّ"),
                 ex("أُمِّي طَبِيبَة فِي مُسْتَشْفَى كَبِير.", "My mother is a doctor in a big hospital.", "طَبِيبَة"),
                 ex("فَتَحَ جَارِي مَحَلًّا صَغِيرًا فِي الْحَيّ.", "My neighbour opened a small shop in the neighbourhood.", "فَتَحَ"),
                 ex("يُفَضِّل خَالِد الْعَمَل الْحُرّ.", "Khalid prefers self-employment.", "الْعَمَل الْحُرّ"),
                 ex("أُخْتِي مُوَظَّفَة فِي شَرِكَة كَبِيرَة.", "My sister is an employee in a big company.", "مُوَظَّفَة"),
                 ex("هَلْ عِنْدَك وَظِيفَة؟", "Do you have a job? (to a man)", "وَظِيفَة"),
             ]),
    ],
    exercises=[
        M("What does الْعَمَل الْحُرّ mean?", "self-employment", ["a night job", "a school lesson", "a holiday"], "حُرّ = free."),
        M("What does صَاحِب مَحَلّ mean?", "shop owner", ["customer", "guest", "teacher"], "صَاحِب = owner."),
        M("Which word means “employee”?", "مُوَظَّف", ["تَاجِر", "طَبِيب", "جَار"], "مُوَظَّف works for a company."),
        M("What does فَتَحَ جَارِي مَحَلًّا mean?", "My neighbour opened a shop", ["My neighbour closed a shop", "My neighbour visited a shop", "My neighbour sold a shop"], "فَتَحَ = he opened."),
        M("What does هَلْ عِنْدَك وَظِيفَة؟ ask?", "Do you have a job?", ["Where is your house?", "What is your name?", "How old are you?"], "وَظِيفَة = job."),
        M("What is the Arabic for “company”?", "شَرِكَة", ["مُسْتَشْفَى", "مَحَلّ", "مَدْرَسَة"], "شَرِكَة = company."),
        F("أُمِّي ___ فِي مُسْتَشْفَى كَبِير.", "طَبِيبَة", ["طَبِيبَان", "تَاجِر", "مُوَظَّفُون"], "A woman: add ة.", tr="My mother is a doctor in a big hospital."),
        F("أَبِي ___ مَحَلّ صَغِير.", "صَاحِب", ["مُوَظَّف", "طَبِيبَة", "شَرِكَة"], "Owner of a shop.", tr="My father owns a small shop."),
        F("فَتَحَ جَارِي ___ صَغِيرًا فِي الْحَيّ.", "مَحَلًّا", ["مَحَلّ", "شَرِكَة", "وَظِيفَة"], "Object: tanwīn with fatḥa, and masculine to match صَغِيرًا.", tr="My neighbour opened a small shop in the neighbourhood."),
    ],
    verify=vw("مُوَظَّف", "مُوَظَّفَة", "صَاحِب", "مَحَلّ", "تَاجِر", "شَرِكَة", "الْعَمَل", "الْحُرّ", "وَظِيفَة", "طَبِيب", "طَبِيبَة", "مُسْتَشْفَى", "فَتَحَ", "مَحَلًّا", "صَغِيرًا", "يُفَضِّل", "خَالِد", "مُوَظَّفُون", "مَدْرَسَة", "عِنْدَك"),
)

# ---------------------------------------------------------------------------- 235
L235 = lesson(
    "Shops in the neighbourhood: grocery, butcher, bakery",
    "أَشْتَرِي الْخُبْز مِنَ الْمَخْبَز الْقَرِيب",
    requires=["خبز", "لحم", "مطعم", "سوق", "قريب", "محل", "باع", "فتح"],
    cards=[
        card("Who sells what",
             "The pattern فَعَّال, with a doubled middle letter, names a seller (جَزَّار); with ـَة it often names the shop (بَقَّالَة). "
             "Words that start with مَـ often name a place where something is done: مَخْبَز is the place where bread (خُبْز) is baked, and مَطْعَم is where you eat.",
             tables=[table(["English", "Arabic"],
                           [["grocery store", "بَقَّالَة"], ["butcher", "جَزَّار"], ["bakery", "مَخْبَز"], ["restaurant", "مَطْعَم"],
                            ["market", "سُوق"], ["bread", "خُبْز"], ["meat", "لَحْم"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Shopping sentences",
             "The verb بَاعَ (he sold) is a hollow verb. Its present is يَبِيع (he sells). To say where you buy something, use مِنْ: أَشْتَرِي الْخُبْز مِنَ الْمَخْبَز.",
             examples=[
                 ex("أَشْتَرِي الْخُبْز مِنَ الْمَخْبَز الْقَرِيب.", "I buy the bread from the nearby bakery.", "الْمَخْبَز"),
                 ex("يَبِيع الْجَزَّار اللَّحْم.", "The butcher sells meat.", "يَبِيع"),
                 ex("أَبِي يَذْهَب إِلَى الْبَقَّالَة كُلّ يَوْم.", "My father goes to the grocery store every day.", "الْبَقَّالَة"),
                 ex("فِي الْحَيّ مَطْعَم وَمَخْبَز وَبَقَّالَة.", "In the neighbourhood there is a restaurant, a bakery and a grocery store.", "مَخْبَز"),
                 ex("الْبَقَّالَة قَرِيبَة مِنْ بَيْتِنَا.", "The grocery store is near our house.", "قَرِيبَة"),
                 ex("يَفْتَح الْمَخْبَز فِي السَّادِسَة صَبَاحًا.", "The bakery opens at six in the morning.", "يَفْتَح"),
             ]),
    ],
    exercises=[
        M("Where do you buy bread?", "مِنَ الْمَخْبَز", ["مِنَ الْجَزَّار", "مِنَ الْمَطْعَم", "مِنَ الْمَكْتَبَة"], "مَخْبَز = bakery."),
        M("Who sells meat?", "الْجَزَّار", ["الطَّبِيب", "الْمُدَرِّس", "السَّائِق"], "جَزَّار = butcher."),
        M("What does بَقَّالَة mean?", "grocery store", ["school", "airport", "hospital"], "A small shop for food."),
        M("What does يَبِيع الْجَزَّار اللَّحْم mean?", "The butcher sells meat", ["The butcher buys meat", "The butcher eats meat", "The butcher cooks bread"], "يَبِيع = he sells."),
        M("What does يَفْتَح الْمَخْبَز فِي السَّادِسَة صَبَاحًا mean?", "The bakery opens at six in the morning", ["The bakery closes at six in the evening", "The grocery opens at six", "The restaurant opens at noon"], "يَفْتَح = opens."),
        M("Which means “market”?", "سُوق", ["مَخْبَز", "جَزَّار", "لَحْم"], "سُوق = market."),
        F("أَشْتَرِي الْخُبْز مِنَ ___ الْقَرِيب.", "الْمَخْبَز", ["الْجَزَّار", "اللَّحْم", "الْخُبْز"], "The place where bread is made.", tr="I buy the bread from the nearby bakery."),
        F("الْجَزَّار ___ اللَّحْم.", "يَبِيع", ["يَقُول", "يَنَام", "يَسِير"], "A butcher sells.", tr="The butcher sells meat.", lemma="بيع:pres:huwa"),
        F("أَبِي يَذْهَب إِلَى ___ كُلّ يَوْم.", "الْبَقَّالَة", ["الْجَزَّار", "الْخُبْز", "اللَّحْم"], "A place you go to.", tr="My father goes to the grocery store every day."),
    ],
    verify=(vv("بيع", "pres", huwa="يَبِيع", ana="أَبِيع", hiya="تَبِيع") + vv("قول", "pres", huwa="يَقُول") + vv("نوم", "pres", huwa="يَنَام") + vv("سير", "pres", huwa="يَسِير")
            + vw("بَقَّالَة", "الْبَقَّالَة", "جَزَّار", "الْجَزَّار", "مَخْبَز", "الْمَخْبَز", "مَطْعَم", "سُوق", "خُبْز", "الْخُبْز", "لَحْم", "اللَّحْم", "أَشْتَرِي", "الْقَرِيب", "بَيْتِنَا", "السَّادِسَة", "صَبَاحًا", "السَّائِق", "الطَّبِيب", "الْمُدَرِّس")),
)

# ---------------------------------------------------------------------------- 236
L236 = lesson(
    "Mosque, church and festivals",
    "فِي الْحَيّ مَسْجِد وَكَنِيسَة قَرِيبَان",
    requires=["مسجد", "كنيسة", "إمام", "عيد", "مهرجان", "صلى", "حضر", "ميلاد", "زار"],
    cards=[
        card("Places of worship and festivals",
             "Arab communities abroad often have both a مَسْجِد (mosque) and a كَنِيسَة (church), because Arab communities include Muslims, Christians and others. "
             "The leader of the prayer in a mosque is an إِمَام. A holiday is عِيد, and a public festival is مَهْرَجَان. "
             "The Christmas holiday is عِيد الْمِيلَاد.",
             tables=[table(["English", "Arabic"],
                           [["mosque", "مَسْجِد"], ["church", "كَنِيسَة"], ["imam", "إِمَام"], ["holiday", "عِيد"],
                            ["festival", "مَهْرَجَان"], ["Christmas", "عِيد الْمِيلَاد"], ["prayer", "صَلَاة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Two things together take a dual adjective: مَسْجِد وَكَنِيسَة قَرِيبَان (a mosque and a church, both near). "
             "Use يَوْم الْجُمْعَة for “on Friday” and كُلّ سَنَة for “every year”.",
             examples=[
                 ex("فِي الْحَيّ مَسْجِد وَكَنِيسَة قَرِيبَان.", "In the neighbourhood there are a mosque and a church, both nearby.", "قَرِيبَان"),
                 ex("يُصَلِّي أَبِي فِي الْمَسْجِد يَوْم الْجُمْعَة.", "My father prays at the mosque on Friday.", "يُصَلِّي"),
                 ex("تَزُور عَائِلَتِي الْكَنِيسَة فِي عِيد الْمِيلَاد.", "My family visits the church at Christmas.", "الْكَنِيسَة"),
                 ex("يَتَكَلَّم الْإِمَام مَعَ النَّاس بَعْد الصَّلَاة.", "The imam talks with people after the prayer.", "الْإِمَام"),
                 ex("يَحْضُر كَثِير مِنَ النَّاس الْمَهْرَجَان الْعَرَبِيّ كُلّ سَنَة.", "Many people attend the Arab festival every year.", "الْمَهْرَجَان"),
                 ex("عِيد سَعِيد!", "Happy holiday!", "عِيد سَعِيد"),
             ]),
    ],
    exercises=[
        M("Which word means “mosque”?", "مَسْجِد", ["كَنِيسَة", "مَهْرَجَان", "مَطْعَم"], "مَسْجِد = mosque."),
        M("Which word means “church”?", "كَنِيسَة", ["مَسْجِد", "مَدْرَسَة", "مَخْبَز"], "كَنِيسَة = church."),
        M("What does عِيد الْمِيلَاد mean?", "Christmas", ["Friday prayer", "the festival", "the new year"], "مِيلَاد = birth."),
        M("What is an إِمَام?", "the leader of the prayer", ["a shop owner", "a doctor", "a bus driver"], "The imam leads the prayer."),
        M("Why is قَرِيبَان in the dual in “مَسْجِد وَكَنِيسَة قَرِيبَان”?", "It describes two things", ["It describes one thing", "It is a plural", "It is a verb"], "Two things → dual adjective."),
        M("What does يَحْضُر النَّاس الْمَهْرَجَان mean?", "People attend the festival", ["People leave the festival", "People close the festival", "People forget the festival"], "حَضَرَ = attended."),
        F("يُصَلِّي أَبِي فِي ___ يَوْم الْجُمْعَة.", "الْمَسْجِد", ["الْكَنِيسَة", "الْمَطْعَم", "الْمَخْبَز"], "Friday prayer is at the mosque.", tr="My father prays at the mosque on Friday."),
        F("تَزُور عَائِلَتِي الْكَنِيسَة فِي عِيد ___.", "الْمِيلَاد", ["الْجُمْعَة", "الْمَسْجِد", "الصَّلَاة"], "Christmas holiday.", tr="My family visits the church at Christmas."),
        F("يَحْضُر كَثِير مِنَ النَّاس ___ الْعَرَبِيّ كُلّ سَنَة.", "الْمَهْرَجَان", ["الْإِمَام", "الصَّلَاة", "الْحَيّ"], "A public event.", tr="Many people attend the Arab festival every year."),
    ],
    verify=vw("مَسْجِد", "كَنِيسَة", "إِمَام", "الْإِمَام", "عِيد", "مَهْرَجَان", "الْمَهْرَجَان", "الْمِيلَاد", "الصَّلَاة", "صَلَاة", "يُصَلِّي", "الْجُمْعَة", "الْكَنِيسَة", "الْمَسْجِد", "قَرِيبَان", "سَعِيد", "مَهْرَجَان", "الْمَخْبَز", "الْمَطْعَم", "يَتَكَلَّم", "يَحْضُر"),
)


# ---------------------------------------------------------------------------- 237
L237 = lesson(
    "Far from home: الْغُرْبَة",
    "أَشْتَاق إِلَى أَهْلِي فِي الْوَطَن",
    requires=["وطن", "أهل", "بداية", "صعب", "قلب", "كلم", "شعر", "بعيد", "هاتف", "أسبوع"],
    cards=[
        card("Words for missing home",
             "Your homeland is وَطَن and your family and relatives are أَهْل. "
             "الْغُرْبَة is the feeling of being a stranger far from home. The verb اِشْتَاقَ إِلَى means “to long for” or “to miss”. "
             "Its present tense is أَشْتَاق (I miss), يَشْتَاق (he misses).",
             tables=[table(["English", "Arabic"],
                           [["homeland", "وَطَن"], ["family; relatives", "أَهْل"], ["life abroad; homesickness", "غُرْبَة"],
                            ["far from", "بَعِيد عَنْ"], ["beginning", "بِدَايَة"], ["heart", "قَلْب"], ["hard; difficult", "صَعْب"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Feelings and contact",
             "To say “I feel …”, use أَشْعُر بِ + noun: أَشْعُر بِالْغُرْبَة. To stay in touch you can call or talk: أُكَلِّم أُمِّي بِالْهَاتِف.",
             examples=[
                 ex("أَشْتَاق إِلَى أَهْلِي فِي الْوَطَن.", "I miss my family in my homeland.", "أَشْتَاق"),
                 ex("أَشْعُر بِالْغُرْبَة فِي الْأَيَّام الْأُولَى.", "I feel homesick in the first days.", "أَشْعُر"),
                 ex("أَنَا بَعِيد عَنْ وَطَنِي، لَكِنْ قَلْبِي هُنَاكَ.", "I am far from my homeland, but my heart is there.", "بَعِيد عَنْ"),
                 ex("أُكَلِّم أُمِّي بِالْهَاتِف كُلّ أُسْبُوع.", "I talk to my mother on the phone every week.", "أُكَلِّم"),
                 ex("الْأَيَّام الْأُولَى فِي بَلَد جَدِيد صَعْبَة.", "The first days in a new country are hard.", "صَعْبَة"),
                 ex("يَشْتَاق جَدِّي إِلَيْنَا.", "My grandfather misses us.", "يَشْتَاق"),
             ]),
    ],
    exercises=[
        M("What does وَطَن mean?", "homeland", ["neighbourhood", "passport", "market"], "وَطَن = homeland."),
        M("What does أَهْل mean?", "family; relatives", ["neighbours", "teachers", "tourists"], "أَهْلِي = my family."),
        M("What does أَشْتَاق إِلَى أَهْلِي mean?", "I miss my family", ["I visit my family", "I call my family", "I leave my family"], "اِشْتَاقَ إِلَى = to long for."),
        M("What does أَنَا بَعِيد عَنْ وَطَنِي mean?", "I am far from my homeland", ["I am in my homeland", "I am near the airport", "I am leaving my city"], "بَعِيد عَنْ = far from."),
        M("What does الْغُرْبَة describe?", "the feeling of being far from home", ["a kind of food", "a holiday", "a kind of job"], "غُرْبَة = being abroad, homesickness."),
        M("What does أُكَلِّم أُمِّي بِالْهَاتِف mean?", "I talk to my mother on the phone", ["I buy my mother a phone", "I visit my mother", "I write to my mother"], "كَلَّمَ = to talk to."),
        F("أَنَا ___ إِلَى أَهْلِي.", "أَشْتَاق", ["يَشْتَاق", "تَشْتَاق", "نَشْتَاق"], "I: the prefix is أ.", tr="I miss my family."),
        F("أَنَا ___ أُمِّي كُلّ أُسْبُوع.", "أُكَلِّم", ["يُكَلِّم", "تُكَلِّم", "نُكَلِّم"], "I talk to: the prefix is أُ.", tr="I talk to my mother every week.", lemma="كلم#2:pres:ana"),
        F("أَشْعُر ___ فِي الْأَيَّام الْأُولَى.", "بِالْغُرْبَة", ["الْغُرْبَة", "فِي الْغُرْبَة", "مِنَ الْغُرْبَة"], "أَشْعُر takes بِ.", tr="I feel homesick in the first days."),
    ],
    verify=(vv("شعر", "pres", ana="أَشْعُر", huwa="يَشْعُر") + vv("كلم#2", "pres", ana="أُكَلِّم", huwa="يُكَلِّم")
            + vw("وَطَن", "وَطَنِي", "أَهْل", "أَهْلِي", "غُرْبَة", "الْغُرْبَة", "بِالْغُرْبَة", "بِدَايَة", "قَلْب", "قَلْبِي", "صَعْب", "صَعْبَة", "بَعِيد", "اِشْتَاق", "أُسْبُوع", "بِالْهَاتِف", "الْأُولَى", "إِلَيْنَا", "جَدِّي", "هُنَاكَ", "لَكِنْ")),
)

# ---------------------------------------------------------------------------- 238
L238 = lesson(
    "The media: television, radio, newspapers",
    "تُقَدِّم هَذِهِ الْقَنَاة بَرَامِج عَرَبِيَّة",
    requires=["وسيلة", "إعلام", "إذاعة", "جريدة", "مجلة", "قناة", "موقع", "برنامج", "سمع", "قرأ"],
    cards=[
        card("Ways to get the news",
             "The media are وَسَائِل الْإِعْلَام. The singular وَسِيلَة means “a means” and إِعْلَام means “informing”. "
             "Each medium has its own word. A plural of things (such as وَسَائِل) is treated as a feminine singular, so the adjective is feminine: وَسَائِل الْإِعْلَام مُهِمَّة.",
             tables=[table(["English", "Arabic"],
                           [["the media", "وَسَائِل الْإِعْلَام"], ["television", "تِلْفَاز"], ["radio; broadcasting", "إِذَاعَة"], ["newspaper", "جَرِيدَة"],
                            ["magazine", "مَجَلَّة"], ["TV channel", "قَنَاة"], ["website", "مَوْقِع"], ["programme", "بَرْنَامَج"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What people do with them",
             "You watch (شَاهَدَ) television, listen to (سَمِعَ) the radio, and read (قَرَأَ) a paper or a magazine. A channel presents (تُقَدِّم) programmes.",
             examples=[
                 ex("تُقَدِّم هَذِهِ الْقَنَاة بَرَامِج عَرَبِيَّة.", "This channel presents Arabic programmes.", "تُقَدِّم"),
                 ex("أَسْمَع الْإِذَاعَة فِي السَّيَّارَة.", "I listen to the radio in the car.", "الْإِذَاعَة"),
                 ex("يَقْرَأ أَبِي الْجَرِيدَة كُلّ صَبَاح.", "My father reads the newspaper every morning.", "الْجَرِيدَة"),
                 ex("نَشْتَرِي الْمَجَلَّة كُلّ شَهْر.", "We buy the magazine every month.", "الْمَجَلَّة"),
                 ex("أَقْرَأ الْأَخْبَار عَلَى الْمَوْقِع.", "I read the news on the website.", "الْمَوْقِع"),
                 ex("وَسَائِل الْإِعْلَام مُهِمَّة.", "The media are important.", "وَسَائِل الْإِعْلَام"),
             ]),
    ],
    exercises=[
        M("What does وَسَائِل الْإِعْلَام mean?", "the media", ["the schools", "the markets", "the airports"], "وَسَائِل = means."),
        M("Which word means “newspaper”?", "جَرِيدَة", ["مَجَلَّة", "قَنَاة", "مَوْقِع"], "جَرِيدَة = newspaper."),
        M("Which word means “magazine”?", "مَجَلَّة", ["جَرِيدَة", "إِذَاعَة", "بَرْنَامَج"], "مَجَلَّة = magazine."),
        M("Where do you listen to the news by voice only?", "فِي الْإِذَاعَة", ["فِي الْمَجَلَّة", "عَلَى الْمَوْقِع", "فِي الْجَرِيدَة"], "إِذَاعَة = radio."),
        M("What does تُقَدِّم هَذِهِ الْقَنَاة بَرَامِج عَرَبِيَّة mean?", "This channel presents Arabic programmes", ["This channel closes at night", "This school teaches Arabic", "This magazine is new"], "قَنَاة = channel, بَرَامِج = programmes."),
        M("Why is مُهِمَّة feminine in وَسَائِل الْإِعْلَام مُهِمَّة?", "a plural of things takes a feminine singular adjective", ["it describes a woman", "it is a verb", "it is a dual"], "Plural things → feminine singular."),
        F("يَقْرَأ أَبِي ___ كُلّ صَبَاح.", "الْجَرِيدَة", ["الْإِذَاعَة", "الْقَنَاة", "الْبَرْنَامَج"], "You read a newspaper.", tr="My father reads the newspaper every morning."),
        F("أَسْمَع ___ فِي السَّيَّارَة.", "الْإِذَاعَة", ["الْجَرِيدَة", "الْمَجَلَّة", "الْمَوْقِع"], "You listen to the radio.", tr="I listen to the radio in the car."),
        F("وَسَائِل الْإِعْلَام ___.", "مُهِمَّة", ["مُهِمّ", "مُهِمُّون", "مُهِمَّتَان"], "A plural of things → feminine singular.", tr="The media are important."),
    ],
    verify=(vv("سمع", "pres", ana="أَسْمَع", huwa="يَسْمَع") + vv("قرأ", "pres", huwa="يَقْرَأ", ana="أَقْرَأ")
            + vw("وَسَائِل", "الْإِعْلَام", "تِلْفَاز", "إِذَاعَة", "الْإِذَاعَة", "جَرِيدَة", "الْجَرِيدَة", "مَجَلَّة", "الْمَجَلَّة", "قَنَاة", "الْقَنَاة", "مَوْقِع", "الْمَوْقِع", "بَرْنَامَج", "بَرَامِج", "الْبَرْنَامَج",
                  "تُقَدِّم", "الْأَخْبَار", "السَّيَّارَة", "مُهِمَّة", "مُهِمّ", "نَشْتَرِي", "شَهْر")),
)

# ---------------------------------------------------------------------------- 239
L239 = lesson(
    "In the newspaper: sections and headlines",
    "أَبْدَأ بِصَفْحَة الرِّيَاضَة",
    requires=["سياسة", "رياضة", "ثقافة", "مقال", "عنوان", "صورة", "صفحة", "خبر", "كاتب", "طقس"],
    cards=[
        card("The sections",
             "A newspaper is divided into sections, each with a صَفْحَة (page). The usual ones are السِّيَاسَة (politics), الرِّيَاضَة (sport), "
             "الِاقْتِصَاد (economy), الثَّقَافَة (culture) and الطَّقْس (weather). An article is مَقَال, a headline is عُنْوَان, and a single piece of news is خَبَر (plural أَخْبَار).",
             tables=[table(["English", "Arabic"],
                           [["politics", "السِّيَاسَة"], ["sport", "الرِّيَاضَة"], ["the economy", "الِاقْتِصَاد"], ["culture", "الثَّقَافَة"],
                            ["page", "صَفْحَة"], ["article", "مَقَال"], ["headline", "عُنْوَان"], ["a piece of news", "خَبَر"], ["picture", "صُورَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Reading the paper",
             "Pages are named with an iḍāfa: صَفْحَة الرِّيَاضَة (the sports page). The second word has ال and no tanwīn. The article “about” a subject uses عَنْ.",
             examples=[
                 ex("أَبْدَأ بِصَفْحَة الرِّيَاضَة.", "I start with the sports page.", "صَفْحَة الرِّيَاضَة"),
                 ex("عُنْوَان الْمَقَال طَوِيل.", "The headline of the article is long.", "عُنْوَان"),
                 ex("يَكْتُب الْكَاتِب مَقَالًا عَنِ الِاقْتِصَاد.", "The writer writes an article about the economy.", "مَقَالًا"),
                 ex("فِي الصَّفْحَة الْأُولَى صُورَة كَبِيرَة.", "On the first page there is a big picture.", "صُورَة"),
                 ex("هَذَا خَبَر مُهِمّ عَنِ الطَّقْس.", "This is an important piece of news about the weather.", "خَبَر"),
                 ex("تُحِبّ أُخْتِي صَفْحَة الثَّقَافَة.", "My sister likes the culture page.", "صَفْحَة الثَّقَافَة"),
             ]),
    ],
    exercises=[
        M("Which means “sports page”?", "صَفْحَة الرِّيَاضَة", ["صَفْحَة السِّيَاسَة", "صَفْحَة الطَّقْس", "صَفْحَة الثَّقَافَة"], "رِيَاضَة = sport."),
        M("What does عُنْوَان mean?", "headline", ["picture", "writer", "page"], "عُنْوَان = headline (also address)."),
        M("What does مَقَال mean?", "article", ["magazine", "programme", "channel"], "مَقَال = article."),
        M("What does السِّيَاسَة mean?", "politics", ["sport", "weather", "culture"], "سِيَاسَة = politics."),
        M("Which section would tell you about the rain tomorrow?", "الطَّقْس", ["الرِّيَاضَة", "الثَّقَافَة", "السِّيَاسَة"], "طَقْس = weather."),
        M("What does يَكْتُب الْكَاتِب مَقَالًا عَنِ الِاقْتِصَاد mean?", "The writer writes an article about the economy", ["The writer reads a book about sport", "The writer sells a newspaper", "The writer opens a shop"], "عَنْ = about."),
        F("أَبْدَأ بِصَفْحَة ___.", "الرِّيَاضَة", ["رِيَاضَة", "رِيَاضِيّ", "يَلْعَب"], "In an iḍāfa the second word keeps ال.", tr="I start with the sports page."),
        F("فِي الصَّفْحَة الْأُولَى ___ كَبِيرَة.", "صُورَة", ["صُوَر", "صُورَتَان", "مَقَال"], "One picture, feminine to match كَبِيرَة.", tr="On the first page there is a big picture."),
        F("هَذَا ___ مُهِمّ عَنِ الطَّقْس.", "خَبَر", ["أَخْبَار", "صَفْحَة", "صُورَة"], "One piece of news; masculine to match مُهِمّ.", tr="This is an important piece of news about the weather."),
    ],
    verify=(vv("كتب", "pres", huwa="يَكْتُب") + vpb("خَبَر", "أَخْبَار")
            + vw("السِّيَاسَة", "الرِّيَاضَة", "الِاقْتِصَاد", "الثَّقَافَة", "الطَّقْس", "صَفْحَة", "الصَّفْحَة", "مَقَال", "مَقَالًا", "عُنْوَان", "خَبَر", "صُورَة", "الْكَاتِب", "رِيَاضَة", "رِيَاضِيّ", "طَوِيل", "الْأُولَى", "أَبْدَأ", "رِيَاضَة")),
)

# ---------------------------------------------------------------------------- 240
L240 = lesson(
    "News bulletins and live broadcasts",
    "تَبْدَأ نَشْرَة الْأَخْبَار فِي التَّاسِعَة مَسَاءً",
    requires=["نشرة", "بث", "مباشر", "مذيع", "تقرير", "إعلان", "برنامج", "مراسل", "شاهد", "بدأ"],
    cards=[
        card("On the air",
             "A news bulletin is نَشْرَة الْأَخْبَار. A programme sent live is بَثّ مُبَاشِر. The person who reads the news is the مُذِيع (announcer), "
             "and the person who reports from the field is the مُرَاسِل (correspondent). A report is تَقْرِير, and an advertisement is إِعْلَان.",
             tables=[table(["English", "Arabic"],
                           [["news bulletin", "نَشْرَة الْأَخْبَار"], ["live broadcast", "بَثّ مُبَاشِر"], ["announcer", "مُذِيع"],
                            ["correspondent", "مُرَاسِل"], ["report", "تَقْرِير"], ["advertisement", "إِعْلَان"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Examples",
             "Notice the time expression التَّاسِعَة مَسَاءً (at nine in the evening) and the verb شَاهَدَ (he watched), whose past with “I” is شَاهَدْتُ.",
             examples=[
                 ex("تَبْدَأ نَشْرَة الْأَخْبَار فِي التَّاسِعَة مَسَاءً.", "The news bulletin starts at nine in the evening.", "نَشْرَة الْأَخْبَار"),
                 ex("هَذَا بَثّ مُبَاشِر مِنَ الْمَدِينَة.", "This is a live broadcast from the city.", "بَثّ مُبَاشِر"),
                 ex("يَقْرَأ الْمُذِيع الْأَخْبَار.", "The announcer reads the news.", "الْمُذِيع"),
                 ex("الْمُرَاسِل فِي الْمَطَار الْآن.", "The correspondent is at the airport now.", "الْمُرَاسِل"),
                 ex("بَعْد الْإِعْلَان يَبْدَأ الْبَرْنَامَج.", "After the advertisement the programme starts.", "الْإِعْلَان"),
                 ex("شَاهَدْتُ تَقْرِيرًا عَنِ الْمَهْرَجَان.", "I watched a report about the festival.", "شَاهَدْتُ"),
             ]),
    ],
    exercises=[
        M("What does نَشْرَة الْأَخْبَار mean?", "news bulletin", ["weather map", "school timetable", "newspaper page"], "نَشْرَة = bulletin."),
        M("What does بَثّ مُبَاشِر mean?", "live broadcast", ["old film", "advertisement", "magazine"], "مُبَاشِر = direct."),
        M("Who reads the news on television?", "الْمُذِيع", ["الْمُرَاسِل", "الْجَزَّار", "الْإِمَام"], "مُذِيع = announcer."),
        M("Who reports from outside the studio?", "الْمُرَاسِل", ["الْمُذِيع", "الطَّبِيب", "السَّائِق"], "مُرَاسِل = correspondent."),
        M("What does إِعْلَان mean?", "advertisement", ["report", "headline", "channel"], "إِعْلَان = advertisement."),
        M("What does شَاهَدْتُ تَقْرِيرًا mean?", "I watched a report", ["I wrote a report", "I sold a report", "I lost a report"], "شَاهَدْتُ = I watched."),
        F("تَبْدَأ ___ فِي التَّاسِعَة مَسَاءً.", "نَشْرَة الْأَخْبَار", ["الْمُذِيع", "الْإِعْلَان", "الْمُرَاسِل"], "The bulletin starts at a time.", tr="The news bulletin starts at nine in the evening."),
        F("يَقْرَأ ___ الْأَخْبَار.", "الْمُذِيع", ["الْمُرَاسِل", "الْإِعْلَان", "الْمَطَار"], "He reads the news in the studio.", tr="The announcer reads the news."),
        F("هَذَا ___ مِنَ الْمَدِينَة.", "بَثّ مُبَاشِر", ["نَشْرَة", "إِعْلَان", "مُذِيع"], "Live from the city.", tr="This is a live broadcast from the city."),
    ],
    verify=vw("نَشْرَة", "الْأَخْبَار", "بَثّ", "مُبَاشِر", "مُذِيع", "الْمُذِيع", "مُرَاسِل", "الْمُرَاسِل", "تَقْرِير", "تَقْرِيرًا", "إِعْلَان", "الْإِعْلَان", "التَّاسِعَة", "مَسَاءً", "الْمَطَار", "شَاهَدْتُ", "يَبْدَأ", "الْبَرْنَامَج", "الْمَهْرَجَان", "الْجَزَّار", "الْإِمَام", "السَّائِق", "الطَّبِيب"),
)


# ---------------------------------------------------------------------------- 241
L241 = lesson(
    "In order to: لِـ and كَيْ",
    "جِئْنَا لِنَتَعَلَّم · ذَهَبُوا كَيْ يَلْعَبُوا",
    requires=["كي", "ملعب", "نجح", "لعب", "جلس", "درس", "علم", "بنت", "ولد", "معا"],
    cards=[
        card("Saying the purpose",
             "To say why someone does something, put لِـ (in order to) or كَيْ (so that) before a present verb. "
             "Both are followed by the shortened present that you know from أَنْ and لَنْ. "
             "A final ن of ـُونَ, ـِينَ and ـَانِ falls away, and ـُوا gets a silent alif. The women’s plural ـْنَ keeps its ن. "
             "لِـ is joined to the verb: لِ + يَلْعَبُوا = لِيَلْعَبُوا. كَيْ stands alone.",
             tables=[table(["English", "With ن (plain present)", "After لِـ or كَيْ"],
                           [["they (men) play", "يَلْعَبُون", "كَيْ يَلْعَبُوا"], ["the two boys study", "يَدْرُسَان", "كَيْ يَدْرُسَا"],
                            ["you (woman) learn", "تَتَعَلَّمِين", "كَيْ تَتَعَلَّمِي"], ["they (women) drink", "يَشْرَبْنَ", "كَيْ يَشْرَبْنَ"],
                            ["we learn", "نَتَعَلَّم", "كَيْ نَتَعَلَّم"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Examples",
             "The first verb says what is or was done, and the second verb gives the purpose.",
             examples=[
                 ex("أَدْرُس كَثِيرًا لِأَنْجَح فِي الِامْتِحَان.", "I study a lot in order to pass the exam.", "لِأَنْجَح"),
                 ex("جِئْنَا إِلَى هُنَا لِنَتَعَلَّم الْعَرَبِيَّة.", "We came here to learn Arabic.", "لِنَتَعَلَّم"),
                 ex("ذَهَبَ الْأَطْفَال إِلَى الْمَلْعَب لِيَلْعَبُوا.", "The children went to the playground to play.", "لِيَلْعَبُوا"),
                 ex("جَاءَ الْوَلَدَان كَيْ يَدْرُسَا مَعًا.", "The two boys came to study together.", "كَيْ يَدْرُسَا"),
                 ex("تَجْلِس الْبِنْت قَرِيبًا مِنَ الْمُدَرِّسَة كَيْ تَسْمَع جَيِّدًا.", "The girl sits near the teacher so that she hears well.", "كَيْ تَسْمَع"),
                 ex("ذَهَبَتِ الْبَنَات إِلَى الْمَقْهَى لِيَشْرَبْنَ الْقَهْوَة.", "The girls went to the café to drink coffee.", "لِيَشْرَبْنَ"),
             ]),
    ],
    exercises=[
        M("What does لِـ + a present verb often mean?", "in order to", ["because", "although", "after"], "لِـ + verb gives the purpose."),
        M("Which means “We came here to learn Arabic”?", "جِئْنَا إِلَى هُنَا لِنَتَعَلَّم الْعَرَبِيَّة", ["جِئْنَا إِلَى هُنَا لِيَتَعَلَّمُوا الْعَرَبِيَّة", "جِئْتُ إِلَى هُنَا لِنَتَعَلَّم الْعَرَبِيَّة", "جَاءَ إِلَى هُنَا لِنَتَعَلَّم الْعَرَبِيَّة"], "لِنَتَعَلَّم = in order that we learn."),
        M("What happens to the ن of يَلْعَبُون after لِـ?", "it falls away", ["it stays", "it becomes م", "it moves to the front"], "لِيَلْعَبُوا."),
        M("Which means “so that she hears well”?", "كَيْ تَسْمَع جَيِّدًا", ["كَيْ تَسْمَعُون جَيِّدًا", "كَيْ يَسْمَعُوا جَيِّدًا", "كَيْ أَسْمَع جَيِّدًا"], "She → تَـ."),
        M("Which is correct for “the two boys … so that they study”?", "كَيْ يَدْرُسَا", ["كَيْ يَدْرُسَان", "كَيْ يَدْرُسُوا", "كَيْ يَدْرُسْنَ"], "ـَان → ـَا."),
        M("Which one keeps its ن after لِـ?", "لِيَشْرَبْنَ", ["لِيَشْرَبُوا", "لِيَشْرَبَا", "لِتَشْرَبِي"], "The women’s plural ـْنَ keeps its ن."),
        F("ذَهَبَ الْأَطْفَال إِلَى الْمَلْعَب كَيْ ___.", "يَلْعَبُوا", ["يَلْعَبُون", "يَلْعَبَان", "يَلْعَبْنَ"], "They (men): ـُوا with a silent alif.", tr="The children went to the playground to play.", lemma="لعب:sub:hum"),
        F("جِئْنَا إِلَى هُنَا كَيْ ___ الْعَرَبِيَّة.", "نَتَعَلَّم", ["أَتَعَلَّم", "يَتَعَلَّم", "تَتَعَلَّمِين"], "We: the prefix is نَـ.", tr="We came here to learn Arabic.", lemma="علم#5:sub:nahnu"),
        F("جَاءَ الْوَلَدَان كَيْ ___ مَعًا.", "يَدْرُسَا", ["يَدْرُسَان", "يَدْرُسُوا", "يَدْرُسْنَ"], "The two boys: ـَا without ن.", tr="The two boys came to study together.", lemma="درس:sub:huma_m"),
    ],
    verify=(vv("لعب", "sub", hum="يَلْعَبُوا", huma_m="يَلْعَبَا", hunna="يَلْعَبْنَ") + vv("لعب", "pres", hum="يَلْعَبُون")
            + vv("درس", "sub", huma_m="يَدْرُسَا") + vv("درس", "pres", huma_m="يَدْرُسَان")
            + vv("علم#5", "sub", nahnu="نَتَعَلَّم", anti="تَتَعَلَّمِي") + vv("علم#5", "pres", anti="تَتَعَلَّمِين", ana="أَتَعَلَّم", huwa="يَتَعَلَّم")
            + vv("شرب", "sub", hunna="يَشْرَبْنَ", hum="يَشْرَبُوا", huma_m="يَشْرَبَا", anti="تَشْرَبِي") + vv("شرب", "pres", hunna="يَشْرَبْنَ")
            + vv("سمع", "sub", hiya="تَسْمَع", antum="تَسْمَعُوا", hum="يَسْمَعُوا", ana="أَسْمَع") + vv("نجح", "sub", ana="أَنْجَح")
            + vw("لِأَنْجَح", "لِنَتَعَلَّم", "لِيَلْعَبُوا", "لِيَشْرَبْنَ", "الِامْتِحَان", "الْمَلْعَب", "الْمَقْهَى", "الْقَهْوَة", "الْبَنَات", "الْوَلَدَان", "الْبِنْت", "مَعًا", "جَيِّدًا", "قَرِيبًا", "كَيْ", "جِئْنَا", "جَاءَ", "ذَهَبَتِ")),
)

# ---------------------------------------------------------------------------- 242
L242 = lesson(
    "With ن or without ن? A summary",
    "يَكْتُبُون · لَنْ يَكْتُبُوا · لَمْ يَكْتُبُوا · سَيَكْتُبُون",
    requires=["كتب", "رسالة", "واجب", "غد", "درس", "ذهب", "كي", "نجح"],
    cards=[
        card("Where the ن goes",
             "A present verb with the endings ـِينَ, ـَانِ and ـُونَ keeps its ن in a plain statement or question, and after سَـ, لَا and هَلْ. "
             "The ن falls away after أَنْ, لَنْ, كَيْ and لِـ, and also after لَمْ (“did not”). The women’s plural ـْنَ never changes. "
             "So you only have to remember one shortened form for all five words.",
             tables=[table(["English", "Plain present", "After أَنْ · لَنْ · كَيْ · لِـ · لَمْ"],
                           [["you (woman) write", "تَكْتُبِين", "تَكْتُبِي"], ["you two write", "تَكْتُبَان", "تَكْتُبَا"], ["you (men) write", "تَكْتُبُون", "تَكْتُبُوا"],
                            ["they (men) write", "يَكْتُبُون", "يَكْتُبُوا"], ["they two write", "يَكْتُبَان", "يَكْتُبَا"], ["they (women) write", "يَكْتُبْنَ", "يَكْتُبْنَ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("The same verb in six sentences",
             "Compare what happens to the ending. After سَـ and هَلْ the ن stays; after لَنْ, لَمْ and أَنْ it is gone.",
             examples=[
                 ex("سَيَكْتُبُون الرِّسَالَة غَدًا.", "They will write the letter tomorrow.", "سَيَكْتُبُون"),
                 ex("لَنْ يَكْتُبُوا الرِّسَالَة غَدًا.", "They will not write the letter tomorrow.", "لَنْ يَكْتُبُوا"),
                 ex("لَمْ يَكْتُبُوا الرِّسَالَة أَمْس.", "They did not write the letter yesterday.", "لَمْ يَكْتُبُوا"),
                 ex("هَلْ تَكْتُبِين الرِّسَالَة؟", "Are you writing the letter? (to a woman)", "تَكْتُبِين"),
                 ex("أُرِيد أَنْ تَكْتُبِي الرِّسَالَة.", "I want you to write the letter. (to a woman)", "أَنْ تَكْتُبِي"),
                 ex("لَا يَكْتُبَان الْوَاجِب فِي الْمَسَاء.", "The two of them do not write the homework in the evening.", "لَا يَكْتُبَان"),
             ]),
    ],
    exercises=[
        M("Which word keeps the ن of ـُونَ?", "سَـ", ["لَنْ", "لَمْ", "كَيْ"], "سَيَكْتُبُون keeps its ن."),
        M("Which means “They will not write the letter”?", "لَنْ يَكْتُبُوا الرِّسَالَة", ["لَنْ يَكْتُبُون الرِّسَالَة", "لَمْ يَكْتُبُون الرِّسَالَة", "سَيَكْتُبُوا الرِّسَالَة"], "لَنْ drops the ن."),
        M("Which means “They did not write the letter”?", "لَمْ يَكْتُبُوا الرِّسَالَة", ["لَنْ يَكْتُبُون الرِّسَالَة", "لَا يَكْتُبُوا الرِّسَالَة", "سَيَكْتُبُوا الرِّسَالَة"], "لَمْ also drops the ن."),
        M("Which is correct after أَنْ for “you (woman) write”?", "أَنْ تَكْتُبِي", ["أَنْ تَكْتُبِين", "أَنْ تَكْتُبْنَ", "أَنْ تَكْتُبَا"], "ـِين → ـِي."),
        M("Which one never loses its ن?", "يَكْتُبْنَ", ["يَكْتُبُون", "يَكْتُبَان", "تَكْتُبِين"], "ـْنَ belongs to the stem."),
        M("Which means “Are you writing the letter?” (to a woman)", "هَلْ تَكْتُبِين الرِّسَالَة؟", ["هَلْ تَكْتُبِي الرِّسَالَة؟", "هَلْ تَكْتُبُوا الرِّسَالَة؟", "هَلْ تَكْتُبَا الرِّسَالَة؟"], "After هَلْ the ن stays."),
        F("لَنْ ___ الرِّسَالَة غَدًا.", "يَكْتُبُوا", ["يَكْتُبُون", "يَكْتُبَان", "يَكْتُبِين"], "After لَنْ the ن falls away.", tr="They will not write the letter tomorrow.", lemma="كتب:sub:hum"),
        F("هَلْ ___ الرِّسَالَة؟", "تَكْتُبِين", ["تَكْتُبِي", "تَكْتُبُوا", "تَكْتُبَا"], "After هَلْ the ن stays.", tr="Are you writing the letter? (to a woman)", lemma="كتب:pres:anti"),
        F("لَمْ ___ الرِّسَالَة أَمْس.", "يَكْتُبُوا", ["يَكْتُبُون", "يَكْتُبَان", "تَكْتُبِين"], "After لَمْ the ن falls away.", tr="They did not write the letter yesterday.", lemma="كتب:jus:hum"),
    ],
    verify=(vv("كتب", "pres", anti="تَكْتُبِين", huma_m="يَكْتُبَان", antuma="تَكْتُبَان", antum="تَكْتُبُون", hum="يَكْتُبُون", hunna="يَكْتُبْنَ")
            + vv("كتب", "sub", anti="تَكْتُبِي", antuma="تَكْتُبَا", antum="تَكْتُبُوا", hum="يَكْتُبُوا", huma_m="يَكْتُبَا", hunna="يَكْتُبْنَ")
            + vv("كتب", "jus", hum="يَكْتُبُوا") + vv("كتب", "fut", hum="سَيَكْتُبُون")
            + vw("الرِّسَالَة", "الْوَاجِب", "سَيَكْتُبُون", "أُرِيد", "غَدًا", "أَمْس", "الْمَسَاء")),
)


# ---------------------------------------------------------------------------- 243
L243 = lesson(
    "Verbal nouns of Measure I: دُخُول · كِتَابَة · فَتْح",
    "دَخَلَ ← دُخُول · كَتَبَ ← كِتَابَة · فَتَحَ ← فَتْح",
    requires=["دخول", "خروج", "جلوس", "وصول", "حضور", "قراءة", "كتابة", "قيادة", "زيارة", "دراسة", "فتح", "فهم"],
    cards=[
        card("A noun for the action",
             "A verbal noun (maṣdar) names an action, like “entering”, “writing” or “reading”. English uses -ing for this. "
             "In Arabic it is a real noun: it can have ال, take an adjective, and be the subject of a sentence. "
             "For Measure I verbs there is no single rule, so learn the verbal noun together with the verb. Several patterns are common.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["enter", "دَخَلَ", "دُخُول"], ["go out", "خَرَجَ", "خُرُوج"], ["sit", "جَلَسَ", "جُلُوس"], ["arrive", "وَصَلَ", "وُصُول"], ["attend", "حَضَرَ", "حُضُور"]],
                           say=[1, 2], tlit=[2], gloss=False),
                    table(["English", "Verb", "Verbal noun"],
                          [["write", "كَتَبَ", "كِتَابَة"], ["read", "قَرَأَ", "قِرَاءَة"], ["drive; lead", "قَادَ", "قِيَادَة"], ["visit", "زَارَ", "زِيَارَة"], ["study", "دَرَسَ", "دِرَاسَة"], ["swim", "سَبَحَ", "سِبَاحَة"]],
                          say=[1, 2], tlit=[2], gloss=False),
                    table(["English", "Verb", "Verbal noun"],
                          [["open", "فَتَحَ", "فَتْح"], ["understand", "فَهِمَ", "فَهْم"], ["drink", "شَرِبَ", "شُرْب"], ["go", "ذَهَبَ", "ذَهَاب"], ["succeed", "نَجَحَ", "نَجَاح"]],
                          say=[1, 2], tlit=[2], gloss=False)]),
        card("Verbal nouns as subjects",
             "A verbal noun can start a sentence, and any adjective after it is singular and masculine or feminine to match the noun. Most of the nouns ending in ـَة are feminine.",
             examples=[
                 ex("الْكِتَابَة بِالْعَرَبِيَّة صَعْبَة فِي الْبِدَايَة.", "Writing in Arabic is hard at the beginning.", "الْكِتَابَة"),
                 ex("الْقِرَاءَة مُفِيدَة.", "Reading is useful.", "الْقِرَاءَة"),
                 ex("الدُّخُول مَمْنُوع.", "Entering is forbidden.", "الدُّخُول"),
                 ex("الْخُرُوج مِنَ الْمَدْرَسَة فِي الثَّالِثَة.", "Leaving school is at three o’clock.", "الْخُرُوج"),
                 ex("السِّبَاحَة رِيَاضَة جَمِيلَة.", "Swimming is a beautiful sport.", "السِّبَاحَة"),
                 ex("زِيَارَة الْمَتْحَف مُمْتِعَة.", "Visiting the museum is enjoyable.", "زِيَارَة الْمَتْحَف"),
             ]),
    ],
    exercises=[
        M("What is the verbal noun of كَتَبَ?", "كِتَابَة", ["كَاتِب", "مَكْتَب", "مَكْتُوب"], "كِتَابَة = writing."),
        M("What is the verbal noun of دَخَلَ?", "دُخُول", ["مَدْخَل", "دَاخِل", "دَخْل"], "دُخُول = entering."),
        M("What is the verbal noun of قَرَأَ?", "قِرَاءَة", ["قَارِئ", "مَقْرُوء", "قَرْيَة"], "قِرَاءَة = reading."),
        M("What is the verbal noun of زَارَ?", "زِيَارَة", ["زَائِر", "مَزَار", "زِيَادَة"], "زِيَارَة = visiting."),
        M("What does السِّبَاحَة رِيَاضَة جَمِيلَة mean?", "Swimming is a beautiful sport", ["Reading is a useful habit", "Driving is hard", "The beach is far"], "سِبَاحَة = swimming."),
        M("What does الدُّخُول مَمْنُوع mean?", "Entering is forbidden", ["Leaving is forbidden", "Sitting is forbidden", "Reading is forbidden"], "دُخُول = entering."),
        F("___ بِالْعَرَبِيَّة صَعْبَة فِي الْبِدَايَة.", "الْكِتَابَة", ["الْكَاتِب", "الْمَكْتَب", "الْكِتَاب"], "The action of writing.", tr="Writing in Arabic is hard at the beginning."),
        F("___ مُفِيدَة.", "الْقِرَاءَة", ["الْقَارِئ", "الْقُرْآن", "الْمَقْرُوء"], "The action of reading; feminine to match مُفِيدَة.", tr="Reading is useful."),
        F("___ الْمَتْحَف مُمْتِعَة.", "زِيَارَة", ["زَائِر", "مَزَار", "زَائِرَة"], "A verbal noun at the start of an iḍāfa.", tr="Visiting the museum is enjoyable."),
    ],
    verify=vw("دُخُول", "خُرُوج", "جُلُوس", "وُصُول", "حُضُور", "كِتَابَة", "قِرَاءَة", "قِيَادَة", "زِيَارَة", "دِرَاسَة", "سِبَاحَة", "فَتْح", "فَهْم", "شُرْب", "ذَهَاب", "نَجَاح",
              "دَخَلَ", "خَرَجَ", "جَلَسَ", "وَصَلَ", "حَضَرَ", "كَتَبَ", "قَرَأَ", "قَادَ", "زَارَ", "دَرَسَ", "سَبَحَ", "فَتَحَ", "فَهِمَ", "شَرِبَ", "ذَهَبَ", "نَجَحَ",
              "الدُّخُول", "الْخُرُوج", "السِّبَاحَة", "الْقِرَاءَة", "الْكِتَابَة", "مُفِيدَة", "مُمْتِعَة", "الْمَتْحَف", "الثَّالِثَة", "مَدْخَل", "دَاخِل", "كَاتِب", "مَكْتَب", "كِتَاب",
              "قَارِئ", "مَقْرُوء", "قُرْآن", "زَائِر", "مَزَار", "زَوْر", "الْكَاتِب", "الْمَكْتَب", "الْكِتَاب", "الْقَارِئ", "الْقُرْآن", "الْمَقْرُوء", "زِيَارَات", "زِيَادَة", "زَائِرَة"),
)

# ---------------------------------------------------------------------------- 244
L244 = lesson(
    "Using verbal nouns: after prepositions and instead of أَنْ",
    "أُحِبّ الْقِرَاءَة · بَعْد الْوُصُول · مَمْنُوع الْجُلُوس",
    requires=["قراءة", "وصول", "جلوس", "دراسة", "ذهاب", "نجاح", "خروج", "سبب"],
    cards=[
        card("Two ways to say the same thing",
             "After verbs like أُحِبّ (I like), أُرِيد (I want) and يَجِب (it is necessary), you can use أَنْ + verb or a verbal noun. "
             "The verbal noun is shorter and sounds more formal. If the verbal noun has an object, join them in an iḍāfa: "
             "أُحِبّ قِرَاءَة الْجَرِيدَة. The second word is genitive, but in our spelling no ending shows.",
             tables=[table(["With أَنْ + verb", "With a verbal noun"],
                           [["أُحِبّ أَنْ أَقْرَأ", "أُحِبّ الْقِرَاءَة"], ["أُحِبّ أَنْ أَدْرُس اللُّغَات", "أُحِبّ دِرَاسَة اللُّغَات"], ["أُرِيد أَنْ أَذْهَب إِلَى الْمَطَار", "أُرِيد الذَّهَاب إِلَى الْمَطَار"]],
                           say=[0, 1], gloss=False)]),
        card("After a preposition",
             "After بَعْد (after), قَبْل (before), عَنْ (about) and لِـ (for), Arabic uses a verbal noun where English uses -ing. "
             "A sign like مَمْنُوع (forbidden) is followed by a verbal noun too.",
             examples=[
                 ex("بَعْد الْوُصُول إِلَى الْفُنْدُق نَامَ الْجَمِيع.", "After arriving at the hotel everyone slept.", "بَعْد الْوُصُول"),
                 ex("قَبْل الْخُرُوج أَغْلِقِ الْبَاب.", "Before going out, close the door.", "قَبْل الْخُرُوج"),
                 ex("مَمْنُوع الْجُلُوس هُنَا.", "No sitting here.", "الْجُلُوس"),
                 ex("أُحِبّ دِرَاسَة اللُّغَات.", "I like studying languages.", "دِرَاسَة اللُّغَات"),
                 ex("سَبَب نَجَاحِهِ هُوَ الدِّرَاسَة.", "The reason for his success is studying.", "نَجَاحِهِ"),
                 ex("الذَّهَاب إِلَى الْمَطَار بِالْقِطَار سَرِيع.", "Going to the airport by train is quick.", "الذَّهَاب"),
             ]),
    ],
    exercises=[
        M("Which says the same as أُحِبّ أَنْ أَقْرَأ?", "أُحِبّ الْقِرَاءَة", ["أُحِبّ الْقَارِئ", "أُحِبّ الْكِتَابَة", "أُحِبّ قَرَأَ"], "The verbal noun replaces أَنْ + verb."),
        M("What does مَمْنُوع الْجُلُوس mean?", "no sitting", ["no entry", "no parking", "no smoking"], "جُلُوس = sitting."),
        M("What does بَعْد الْوُصُول إِلَى الْفُنْدُق mean?", "after arriving at the hotel", ["before leaving the hotel", "instead of the hotel", "near the hotel"], "بَعْد = after, وُصُول = arriving."),
        M("Which means “Before going out”?", "قَبْل الْخُرُوج", ["بَعْد الْخُرُوج", "قَبْل الدُّخُول", "قَبْل الْجُلُوس"], "قَبْل = before; خُرُوج = going out."),
        M("Which says the same as أُرِيد أَنْ أَذْهَب إِلَى الْمَطَار?", "أُرِيد الذَّهَاب إِلَى الْمَطَار", ["أُرِيد الْوُصُول إِلَى الْمَطَار", "أُرِيد الدُّخُول فِي الْمَطَار", "أُرِيد الْجُلُوس فِي الْمَطَار"], "ذَهَاب = going."),
        M("What does أُحِبّ دِرَاسَة اللُّغَات mean?", "I like studying languages", ["I like teaching languages", "I like reading books", "I like writing letters"], "دِرَاسَة = studying."),
        F("أُحِبّ ___ اللُّغَات.", "دِرَاسَة", ["دَرَسَ", "يَدْرُس", "دَارِس"], "A verbal noun joined to its object in an iḍāfa.", tr="I like studying languages."),
        F("مَمْنُوع ___ هُنَا.", "الْجُلُوس", ["جَلَسَ", "يَجْلِس", "الْجَالِس"], "A verbal noun after مَمْنُوع.", tr="No sitting here."),
        F("بَعْد ___ إِلَى الْفُنْدُق نَامَ الْجَمِيع.", "الْوُصُول", ["وَصَلَ", "يَصِل", "الْوَاصِل"], "A verbal noun after بَعْد.", tr="After arriving at the hotel everyone slept."),
    ],
    verify=vw("أُحِبّ", "أَقْرَأ", "الْقِرَاءَة", "دِرَاسَة", "اللُّغَات", "الذَّهَاب", "الْمَطَار", "الْوُصُول", "الْخُرُوج", "الْجُلُوس", "الدُّخُول", "الْكِتَابَة", "أُرِيد", "أَغْلِقِ", "الْبَاب", "نَجَاحِهِ", "الدِّرَاسَة", "سَبَب", "الْجَمِيع", "الْقِطَار", "سَرِيع", "نَامَ", "دَارِس", "الْجَالِس", "الْوَاصِل", "يَصِل", "الْقَارِئ", "قَرَأَ")
            + vv("جلس", "pres", huwa="يَجْلِس") + vv("درس", "pres", huwa="يَدْرُس"),
)

# ---------------------------------------------------------------------------- 245
L245 = lesson(
    "Verbal nouns of Measures II and III",
    "عَلَّمَ ← تَعْلِيم · شَاهَدَ ← مُشَاهَدَة",
    requires=["تعليم", "تدريب", "تحضير", "تقديم", "تهنئة", "مشاهدة", "مقابلة", "مساعدة", "محاولة", "مغادرة", "مناقشة"],
    cards=[
        card("Measure II: تَفْعِيل",
             "These two measures have fixed patterns, so they are easy. For Measure II, the verbal noun is تَفْعِيل: put تَـ in front, a sukūn on the first root letter and a long ī (ـِي) before the last one. "
             "عَلَّمَ becomes تَعْلِيم. If the last radical is hamza, the pattern is تَفْعِلَة: هَنَّأَ becomes تَهْنِئَة.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["teach", "عَلَّمَ", "تَعْلِيم"], ["train", "دَرَّبَ", "تَدْرِيب"], ["prepare", "حَضَّرَ", "تَحْضِير"], ["present", "قَدَّمَ", "تَقْدِيم"], ["congratulate", "هَنَّأَ", "تَهْنِئَة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Measure III: مُفَاعَلَة",
             "For Measure III, the verbal noun is مُفَاعَلَة. Put مُـ in front of the stem, keep the long ā, and end in ـَة: شَاهَدَ becomes مُشَاهَدَة.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["watch", "شَاهَدَ", "مُشَاهَدَة"], ["meet", "قَابَلَ", "مُقَابَلَة"], ["help", "سَاعَدَ", "مُسَاعَدَة"], ["try", "حَاوَلَ", "مُحَاوَلَة"],
                            ["leave", "غَادَرَ", "مُغَادَرَة"], ["discuss", "نَاقَشَ", "مُنَاقَشَة"]],
                           say=[1, 2], tlit=[2], gloss=False)],
             examples=[
                 ex("تَعْلِيم الْأَطْفَال مُهِمّ.", "Teaching children is important.", "تَعْلِيم"),
                 ex("يَبْدَأ التَّدْرِيب فِي الصَّبَاح.", "The training begins in the morning.", "التَّدْرِيب"),
                 ex("أُحِبّ مُشَاهَدَة الْأَخْبَار.", "I like watching the news.", "مُشَاهَدَة"),
                 ex("بَعْد الْمُقَابَلَة حَصَلَ عَلَى الْوَظِيفَة.", "After the interview he got the job.", "الْمُقَابَلَة"),
                 ex("شُكْرًا عَلَى الْمُسَاعَدَة.", "Thank you for the help.", "الْمُسَاعَدَة"),
                 ex("مُغَادَرَة الْفُنْدُق قَبْل الظُّهْر.", "Hotel check-out is before noon.", "مُغَادَرَة"),
             ]),
    ],
    exercises=[
        M("What is the verbal noun of عَلَّمَ?", "تَعْلِيم", ["تَعَلُّم", "مُعَلِّم", "عِلْم"], "تَفْعِيل: ت + kasra + ي."),
        M("What is the verbal noun of دَرَّبَ?", "تَدْرِيب", ["تَدَرُّب", "مُدَرِّب", "دَرْب"], "تَفْعِيل."),
        M("What is the verbal noun of شَاهَدَ?", "مُشَاهَدَة", ["مُشَاهِد", "شَاهِد", "مَشْهَد"], "مُفَاعَلَة."),
        M("What is the verbal noun of غَادَرَ?", "مُغَادَرَة", ["مُغَادِر", "غَدَر", "غِيَاب"], "مُفَاعَلَة."),
        M("What does بَعْد الْمُقَابَلَة mean?", "after the interview", ["before the interview", "during the lesson", "after the holiday"], "مُقَابَلَة = meeting; interview."),
        M("What is the verbal noun of هَنَّأَ?", "تَهْنِئَة", ["تَقْدِيم", "تَعْلِيم", "مُهَنِّئ"], "Last radical hamza → تَفْعِلَة."),
        F("أُحِبّ ___ الْأَخْبَار.", "مُشَاهَدَة", ["شَاهَدَ", "يُشَاهِد", "مُشَاهِد"], "Measure III verbal noun.", tr="I like watching the news."),
        F("___ الْأَطْفَال مُهِمّ.", "تَعْلِيم", ["عَلَّمَ", "مُعَلِّم", "يُعَلِّم"], "Measure II verbal noun.", tr="Teaching children is important."),
        F("شُكْرًا عَلَى ___.", "الْمُسَاعَدَة", ["سَاعَدَ", "الْمُسَاعِد", "يُسَاعِد"], "Measure III verbal noun.", tr="Thank you for the help."),
    ],
    verify=vw("تَعْلِيم", "تَدْرِيب", "تَحْضِير", "تَقْدِيم", "تَهْنِئَة", "مُشَاهَدَة", "مُقَابَلَة", "مُسَاعَدَة", "مُحَاوَلَة", "مُغَادَرَة", "مُنَاقَشَة",
              "عَلَّمَ", "دَرَّبَ", "حَضَّرَ", "قَدَّمَ", "هَنَّأَ", "شَاهَدَ", "قَابَلَ", "سَاعَدَ", "حَاوَلَ", "غَادَرَ", "نَاقَشَ",
              "التَّدْرِيب", "الْمُقَابَلَة", "الْمُسَاعَدَة", "الظُّهْر", "الْوَظِيفَة", "تَعَلُّم", "مُعَلِّم", "عِلْم", "تَدَرُّب", "مُدَرِّب", "دَرْب", "مُشَاهِد", "شَاهِد", "مَشْهَد",
              "مُغَادِر", "غَدَر", "غِيَاب", "مُهَنِّئ", "يُشَاهِد", "يُعَلِّم", "الْمُسَاعِد", "يُسَاعِد", "شُكْرًا"),
)

# ---------------------------------------------------------------------------- 246
L246 = lesson(
    "Verbal nouns of Measures IV and VI",
    "أَغْلَقَ ← إِغْلَاق · تَبَادَلَ ← تَبَادُل",
    requires=["إغلاق", "إرسال", "إعلان", "إقامة", "تبادل", "تعاون", "تنافس", "تعادل", "تفاهم"],
    cards=[
        card("Measure IV: إِفْعَال",
             "For Measure IV, the verbal noun is إِفْعَال. The verb أَغْلَقَ (he closed) gives إِغْلَاق. "
             "If the middle radical is weak, a ـَة ending is added and the weak letter becomes a long ā: أَقَامَ becomes إِقَامَة.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["close", "أَغْلَقَ", "إِغْلَاق"], ["send", "أَرْسَلَ", "إِرْسَال"], ["announce", "أَعْلَنَ", "إِعْلَان"], ["stay; establish", "أَقَامَ", "إِقَامَة"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Measure VI: تَفَاعُل",
             "For Measure VI, the verbal noun is تَفَاعُل. Compare the verb تَبَادَلَ (he exchanged) with تَبَادُل: the ā stays, the vowel before the last letter becomes ḍamma. "
             "Measure VI usually describes something done between two or more sides.",
             tables=[table(["English", "Verb", "Verbal noun"],
                           [["exchange", "تَبَادَلَ", "تَبَادُل"], ["cooperate", "تَعَاوَنَ", "تَعَاوُن"], ["compete", "تَنَافَسَ", "تَنَافُس"], ["tie; be equal", "تَعَادَلَ", "تَعَادُل"], ["understand each other", "تَفَاهَمَ", "تَفَاهُم"]],
                           say=[1, 2], tlit=[2], gloss=False)],
             examples=[
                 ex("إِغْلَاق الْمَحَلّ فِي التَّاسِعَة.", "The shop closes at nine.", "إِغْلَاق"),
                 ex("شُكْرًا عَلَى إِرْسَال الرِّسَالَة.", "Thank you for sending the letter.", "إِرْسَال"),
                 ex("الْإِعْلَان عَنِ الْمَهْرَجَان فِي الْجَرِيدَة.", "The announcement of the festival is in the newspaper.", "الْإِعْلَان"),
                 ex("التَّعَاوُن بَيْنَ الْجِيرَان مُهِمّ.", "Cooperation between neighbours is important.", "التَّعَاوُن"),
                 ex("بَدَأْنَا تَبَادُل الرَّسَائِل.", "We started exchanging letters.", "تَبَادُل"),
                 ex("التَّنَافُس بَيْنَ الْفَرِيقَيْن قَوِيّ.", "The competition between the two teams is strong.", "التَّنَافُس"),
             ]),
    ],
    exercises=[
        M("What is the verbal noun of أَغْلَقَ?", "إِغْلَاق", ["غَلْق", "مُغْلِق", "غَالِق"], "إِفْعَال."),
        M("What is the verbal noun of أَرْسَلَ?", "إِرْسَال", ["رَسُول", "مُرْسِل", "رِسَالَة"], "إِفْعَال."),
        M("What is the verbal noun of أَقَامَ?", "إِقَامَة", ["قِيَام", "مَقَام", "مُقِيم"], "Weak middle radical → إِقَامَة."),
        M("What is the verbal noun of تَعَاوَنَ?", "تَعَاوُن", ["تَعَاوَنَ", "مُتَعَاوِن", "عَوْن"], "تَفَاعُل."),
        M("What is the verbal noun of تَنَافَسَ?", "تَنَافُس", ["مُنَافَسَة", "نَفْس", "مُتَنَافِس"], "تَفَاعُل."),
        M("What does التَّعَاوُن بَيْنَ الْجِيرَان مُهِمّ mean?", "Cooperation between neighbours is important", ["Neighbours are very old", "Competition among shops is strong", "The neighbourhood is far"], "تَعَاوُن = cooperation."),
        F("شُكْرًا عَلَى ___ الرِّسَالَة.", "إِرْسَال", ["أَرْسَلَ", "مُرْسِل", "رِسَالَة"], "Measure IV verbal noun.", tr="Thank you for sending the letter."),
        F("___ بَيْنَ الْفَرِيقَيْن قَوِيّ.", "التَّنَافُس", ["تَنَافَسَ", "الْمُنَافِس", "النَّافِس"], "Measure VI verbal noun.", tr="The competition between the two teams is strong."),
        F("بَدَأْنَا ___ الرَّسَائِل.", "تَبَادُل", ["تَبَادَلَ", "مُبَادِل", "بَدَل"], "Measure VI verbal noun.", tr="We started exchanging letters."),
    ],
    verify=vw("إِغْلَاق", "إِرْسَال", "إِعْلَان", "إِقَامَة", "تَبَادُل", "تَعَاوُن", "تَنَافُس", "تَعَادُل", "تَفَاهُم",
              "أَغْلَقَ", "أَرْسَلَ", "أَعْلَنَ", "أَقَامَ", "تَبَادَلَ", "تَعَاوَنَ", "تَنَافَسَ", "تَعَادَلَ", "تَفَاهَمَ",
              "الْإِعْلَان", "التَّعَاوُن", "التَّنَافُس", "الْفَرِيقَيْن", "الْجِيرَان", "الرَّسَائِل", "بَدَأْنَا", "غَلْق", "مُغْلِق", "غَالِق", "رَسُول", "مُرْسِل", "قِيَام",
              "مَقَام", "مُقِيم", "مُتَعَاوِن", "عَوْن", "مُنَافَسَة", "نَفْس", "مُتَنَافِس", "الْمُنَافِس", "النَّافِس", "مُبَادِل", "بَدَل", "قَوِيّ"),
)


# ---------------------------------------------------------------------------- 247
L247 = lesson(
    "A map of verbal nouns: Measures I to VI",
    "تَعْلِيم · مُشَاهَدَة · إِغْلَاق · تَعَلُّم · تَبَادُل",
    requires=["تعليم", "مشاهدة", "إغلاق", "تعلم", "تبادل", "مغادرة", "وصول", "مقابلة", "وثيقة"],
    cards=[
        card("One picture of all six",
             "Every measure from II to VI has its own pattern, and Measure I has several. If you know the verb’s measure, you can build the verbal noun.",
             tables=[table(["Measure", "Pattern", "Verb", "Verbal noun"],
                           [["I", "فُعُول · فِعَالَة · فَعْل", "دَخَلَ", "دُخُول"], ["II", "تَفْعِيل", "عَلَّمَ", "تَعْلِيم"], ["III", "مُفَاعَلَة", "شَاهَدَ", "مُشَاهَدَة"],
                            ["IV", "إِفْعَال", "أَغْلَقَ", "إِغْلَاق"], ["V", "تَفَعُّل", "تَعَلَّمَ", "تَعَلُّم"], ["VI", "تَفَاعُل", "تَبَادَلَ", "تَبَادُل"]],
                           say=[1, 2, 3], tlit=[3], gloss=False)]),
        card("Saying it with a verbal noun",
             "A verbal noun can replace أَنْ + verb. When the action belongs to a person, a pronoun ending goes on the verbal noun: بَعْد وُصُولِنَا (after our arrival). "
             "A verbal noun can have its own object: مُغَادَرَة الْفُنْدُق (leaving the hotel).",
             tables=[table(["With أَنْ + verb", "With a verbal noun"],
                           [["أُرِيد أَنْ أُغَادِر الْفُنْدُق", "أُرِيد مُغَادَرَة الْفُنْدُق"], ["يَجِب أَنْ نُغْلِق الْمَحَلّ", "يَجِب إِغْلَاق الْمَحَلّ"], ["بَعْد أَنْ وَصَلْنَا", "بَعْد وُصُولِنَا"]],
                           say=[0, 1], gloss=False)],
             examples=[
                 ex("أُرِيد مُغَادَرَة الْفُنْدُق غَدًا.", "I want to leave the hotel tomorrow.", "مُغَادَرَة"),
                 ex("يَجِب إِغْلَاق الْمَحَلّ فِي التَّاسِعَة.", "The shop must close at nine.", "إِغْلَاق"),
                 ex("بَعْد وُصُولِنَا إِلَى الْمَدِينَة زُرْنَا الْمَتْحَف.", "After our arrival in the city we visited the museum.", "وُصُولِنَا"),
                 ex("التَّعَلُّم وَالتَّعْلِيم مُهِمَّان لِلْجَالِيَة.", "Learning and teaching are important for the community.", "مُهِمَّان"),
                 ex("أُحِبّ مُشَاهَدَة الْأَخْبَار وَقِرَاءَة الْجَرِيدَة.", "I like watching the news and reading the newspaper.", "مُشَاهَدَة"),
                 ex("قَبْل مُقَابَلَة الْمُدِير أَقْرَأ الْوَثَائِق.", "Before meeting the director I read the documents.", "مُقَابَلَة"),
             ]),
    ],
    exercises=[
        M("Which verbal noun belongs to Measure IV?", "إِغْلَاق", ["تَعْلِيم", "مُقَابَلَة", "تَبَادُل"], "إِفْعَال."),
        M("Which verbal noun belongs to Measure VI?", "تَبَادُل", ["تَعَلُّم", "إِرْسَال", "مُشَاهَدَة"], "تَفَاعُل."),
        M("Which verbal noun belongs to Measure III?", "مُشَاهَدَة", ["تَعْلِيم", "إِغْلَاق", "تَعَلُّم"], "مُفَاعَلَة."),
        M("Which says the same as أُرِيد أَنْ أُغَادِر الْفُنْدُق?", "أُرِيد مُغَادَرَة الْفُنْدُق", ["أُرِيد إِغْلَاق الْفُنْدُق", "أُرِيد مُشَاهَدَة الْفُنْدُق", "أُرِيد تَعْلِيم الْفُنْدُق"], "غَادَرَ → مُغَادَرَة."),
        M("How do you say “after our arrival”?", "بَعْد وُصُولِنَا", ["بَعْد وُصُولِي", "بَعْد وُصُولِهِم", "قَبْل وُصُولِنَا"], "نَا = our."),
        M("Which measure has the verbal noun pattern تَفَعُّل?", "Measure V", ["Measure II", "Measure IV", "Measure VI"], "تَعَلَّمَ → تَعَلُّم."),
        F("يَجِب ___ الْمَحَلّ فِي التَّاسِعَة.", "إِغْلَاق", ["تَعْلِيم", "مُشَاهَدَة", "تَبَادُل"], "Closing: Measure IV.", tr="The shop must close at nine."),
        F("قَبْل ___ الْمُدِير أَقْرَأ الْوَثَائِق.", "مُقَابَلَة", ["إِقَامَة", "تَعَاوُن", "تَقْدِيم"], "Meeting: Measure III.", tr="Before meeting the director I read the documents."),
        F("التَّعَلُّم وَالتَّعْلِيم ___ لِلْجَالِيَة.", "مُهِمَّان", ["مُهِمَّة", "مُهِمُّون", "مُهِمَّات"], "Two subjects → dual predicate.", tr="Learning and teaching are important for the community."),
    ],
    verify=(vv("زور", "past", nahnu="زُرْنَا")
            + vw("مُغَادَرَة", "إِغْلَاق", "وُصُولِنَا", "وُصُولِي", "وُصُولِهِم", "الْفُنْدُق", "الْمَحَلّ", "التَّاسِعَة", "التَّعَلُّم", "التَّعْلِيم", "مُهِمَّان", "لِلْجَالِيَة", "مُشَاهَدَة", "قِرَاءَة", "مُقَابَلَة", "الْمُدِير", "الْوَثَائِق", "أُغَادِر", "نُغْلِق",
                 "وَصَلْنَا", "زُرْنَا", "إِقَامَة", "تَعَاوُن", "تَقْدِيم", "تَعْلِيم", "تَبَادُل", "إِرْسَال", "تَعَلُّم", "دُخُول")),
)

# ---------------------------------------------------------------------------- 248
L248 = lesson(
    "Review: community life, media and verbal nouns",
    "رِسَالَة مِنْ سَلْمَى: أَعِيش فِي مَدِينَة كَبِيرَة",
    requires=["مدينة", "أصل", "عائلة", "مسجد", "جريدة", "نشرة", "أهل", "كلم", "قراءة"],
    cards=[
        card("What to remember",
             "This lesson brings together community words, the media, the ن rule and verbal nouns. Remember: the ن of ـُونَ, ـِينَ and ـَانِ falls away after أَنْ, لَنْ, كَيْ, لِـ and لَمْ; "
             "and a verbal noun can replace أَنْ + verb.",
             tables=[table(["English", "Arabic"],
                           [["Many of the children speak two languages.", "كَثِير مِنَ الْأَطْفَال يَتَكَلَّمُون لُغَتَيْن"], ["They will not write the letter.", "لَنْ يَكْتُبُوا الرِّسَالَة"],
                            ["I like reading the newspaper.", "أُحِبّ قِرَاءَة الْجَرِيدَة"], ["The news bulletin starts at nine.", "تَبْدَأ نَشْرَة الْأَخْبَار فِي التَّاسِعَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A letter from Salma (an invented practice text)",
             "Salma is an invented character who lives far from her family’s homeland. The text is made up for practice.",
             examples=[
                 ex("أَنَا سَلْمَى، أَعِيش فِي مَدِينَة كَبِيرَة مُنْذُ ثَلَاث سَنَوَات.", "I am Salma, and I have lived in a big city for three years.", "أَعِيش"),
                 ex("أَصْل عَائِلَتِي مِنَ الْأُرْدُنّ.", "My family’s origin is Jordan.", "أَصْل"),
                 ex("فِي حَيِّنَا مَخْبَز وَبَقَّالَة وَمَسْجِد.", "In our neighbourhood there is a bakery, a grocery store and a mosque.", "حَيِّنَا"),
                 ex("أَشْتَاق إِلَى أَهْلِي، لَكِنْ أُكَلِّم أُمِّي كُلّ أُسْبُوع.", "I miss my family, but I talk to my mother every week.", "أَشْتَاق"),
                 ex("أُحِبّ قِرَاءَة الْجَرِيدَة الْعَرَبِيَّة.", "I like reading the Arabic newspaper.", "قِرَاءَة"),
                 ex("وَأُحِبّ مُشَاهَدَة نَشْرَة الْأَخْبَار فِي الْمَسَاء.", "And I like watching the news bulletin in the evening.", "مُشَاهَدَة"),
             ]),
    ],
    exercises=[
        M("Where does Salma’s family come from?", "Jordan", ["Egypt", "Lebanon", "Sudan"], "أَصْل عَائِلَتِي مِنَ الْأُرْدُنّ."),
        M("How long has Salma lived in the city?", "three years", ["three months", "thirty years", "one week"], "مُنْذُ ثَلَاث سَنَوَات."),
        M("What does Salma do every week?", "She talks to her mother", ["She visits the mosque", "She writes an article", "She sells bread"], "أُكَلِّم أُمِّي كُلّ أُسْبُوع."),
        M("Which is correct after لَنْ for “they (men) write”?", "لَنْ يَكْتُبُوا", ["لَنْ يَكْتُبُون", "لَنْ يَكْتُبَان", "لَنْ يَكْتُبْنَ"], "The ن falls away."),
        M("Which verbal noun means “watching”?", "مُشَاهَدَة", ["مُشَاهِد", "شَاهَدَ", "مَشْهَد"], "Measure III verbal noun."),
        M("In which newspaper section would you find the forecast?", "الطَّقْس", ["الرِّيَاضَة", "السِّيَاسَة", "الثَّقَافَة"], "طَقْس = weather."),
        F("أُحِبّ ___ الْجَرِيدَة الْعَرَبِيَّة.", "قِرَاءَة", ["قَرَأَ", "قَارِئ", "يَقْرَأ"], "A verbal noun joined to its object.", tr="I like reading the Arabic newspaper."),
        F("هَلْ ___ الرِّسَالَة الْآن؟", "تَكْتُبِين", ["تَكْتُبِي", "تَكْتُبُوا", "تَكْتُبَا"], "After هَلْ the ن stays.", tr="Are you writing the letter now? (to a woman)", lemma="كتب:pres:anti"),
        F("الْمَخْبَز وَالْبَقَّالَة وَالْمَسْجِد فِي ___.", "الْحَيّ", ["الْجَرِيدَة", "الْإِذَاعَة", "الْعُنْوَان"], "Places are in a neighbourhood.", tr="The bakery, the grocery store and the mosque are in the neighbourhood."),
    ],
    verify=(vv("عيش", "pres", ana="أَعِيش") + vn(3, "f", "ثَلَاث")
            + vw("سَلْمَى", "الْأُرْدُنّ", "حَيِّنَا", "الْجَرِيدَة", "الْعَرَبِيَّة", "الْأَخْبَار", "الْمَسَاء", "أُسْبُوع", "الْآن", "الْحَيّ", "الْإِذَاعَة", "الْعُنْوَان", "مُشَاهِد", "مَشْهَد", "الْمَسْجِد", "الْبَقَّالَة", "الْمَخْبَز", "لُغَتَيْن", "يَتَكَلَّمُون")),
)


UNIT = unit("الْعَرَب فِي أَمْرِيكَا: communities, media and verbal nouns", [L231, L232, L233, L234, L235, L236, L237, L238, L239, L240, L241, L242, L243, L244, L245, L246, L247, L248])
