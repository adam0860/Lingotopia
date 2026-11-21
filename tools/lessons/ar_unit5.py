"""Unit 5: invitations, the home, the dual, numbers, iḍāfa, durations
(textbook Chapter 4; all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 65
L65 = lesson(
    "Invitations",
    "تَفَضَّل · أَهْلًا بِكَ · أَدْعُوكَ إِلَى الْعَشَاء",
    requires=["دعوة", "ضيف", "زيارة", "عشاء"],
    cards=[
        card("Welcoming a guest",
             "تَفَضَّل is what you say to invite someone in, to offer something, or to say “after you”. It changes for "
             "a woman and for a group. أَهْلًا بِـ plus an ending means “welcome to you”; you will see how these endings "
             "work after a preposition in the next unit.",
             tables=[table(["English", "Arabic"],
                           [["please, come in (to a man)", "تَفَضَّل"], ["please, come in (to a woman)", "تَفَضَّلِي"],
                            ["please, come in (to a group)", "تَفَضَّلُوا"], ["welcome to you (man)", "أَهْلًا بِكَ"],
                            ["welcome to you (woman)", "أَهْلًا بِكِ"], ["welcome to you (group)", "أَهْلًا بِكُم"],
                            ["guest", "ضَيْف"], ["invitation", "دَعْوَة"], ["dinner", "عَشَاء"], ["lunch", "غَدَاء"]],
                           say=[1], tlit=[1])]),
        card("Inviting, accepting, declining",
             "أَدْعُو means “I invite”. The ending ـكَ or ـكِ, the same as in كِتَابُكَ, means “you” when it is added to "
             "a verb. To decline politely, thank the person and give a reason.",
             examples=[
                 ex("أَدْعُوكَ إِلَى الْعَشَاء.", "I invite you (man) to dinner.", "أَدْعُوكَ"),
                 ex("أَدْعُوكِ إِلَى الْغَدَاء.", "I invite you (woman) to lunch.", "أَدْعُوكِ"),
                 ex("شُكْرًا عَلَى الدَّعْوَة.", "Thank you for the invitation."),
                 ex("بِكُلِّ سُرُور!", "With pleasure!"),
                 ex("شُكْرًا، وَلَكِنْ أَنَا مَشْغُول الْيَوْم.", "Thank you, but I am busy today. (a man speaking)"),
                 ex("لِلْأَسَف، أَنَا مَشْغُولَة غَدًا.", "Unfortunately I am busy tomorrow. (a woman speaking)"),
                 ex("أَهْلًا بِكِ فِي بَيْتِي.", "Welcome to my home. (to a woman)"),
             ]),
    ],
    exercises=[
        M("Someone says تَفَضَّلِي. Who are they speaking to?", "a woman", ["a man", "a group", "two men"], "ـِي marks the feminine."),
        M("Which welcomes a man to your home?", "أَهْلًا بِكَ", ["أَهْلًا بِكِ", "أَهْلًا بِكُم", "مَعَ السَّلَامَة"], "ـكَ for a man."),
        M("Which means “Thank you for the invitation”?", "شُكْرًا عَلَى الدَّعْوَة", ["شُكْرًا مِنَ الدَّعْوَة", "شُكْرًا إِلَى الدَّعْوَة", "شُكْرًا مَعَ الدَّعْوَة"], "عَلَى after شُكْرًا."),
        M("Which means “with pleasure”?", "بِكُلِّ سُرُور", ["لِلْأَسَف", "تَفَضَّل", "مَعَ السَّلَامَة"], "سُرُور = pleasure."),
        M("Which means “I invite you (man) to dinner”?", "أَدْعُوكَ إِلَى الْعَشَاء", ["أَدْعُوكِ إِلَى الْعَشَاء", "أَدْعُو إِلَى الْعَشَاء", "تَدْعُوكَ إِلَى الْعَشَاء"], "أَدْعُو + ـكَ."),
        M("You cannot come. Which is a polite reply (man speaking)?", "شُكْرًا، وَلَكِنْ أَنَا مَشْغُول الْيَوْم", ["بِكُلِّ سُرُور", "تَفَضَّل", "أَهْلًا وَسَهْلًا"], "Thank, then give a reason."),
        M("What is a ضَيْف?", "a guest", ["a host", "a cook", "a neighbour"], "ضَيْف = guest."),
        F("___ بِكِ فِي بَيْتِي.", "أَهْلًا", ["شُكْرًا", "لِلْأَسَف", "تَفَضَّل"], "A welcome.", tr="Welcome to my home. (to a woman)"),
        F("شُكْرًا عَلَى ___.", "الدَّعْوَة", ["الضَّيْف", "الْبَاب", "الْمَدِينَة"], "What you are thanking for.", tr="Thank you for the invitation."),
    ],
    verify=vw("تَفَضَّل", "تَفَضَّلِي", "تَفَضَّلُوا", "أَهْلًا", "بِكَ", "بِكِ", "بِكُم", "ضَيْف", "دَعْوَة", "عَشَاء", "غَدَاء",
              "سُرُور", "لِلْأَسَف", "مَشْغُولَة", "أَدْعُو"),
)

# ---------------------------------------------------------------------------- 66
L66 = lesson(
    "The house and its rooms",
    "بَيْت · شَقَّة · غُرْفَة · مَطْبَخ · حَمَّام",
    requires=["بيت", "غرفة", "باب", "شقة", "طابق", "نافذة"],
    cards=[
        card("Rooms",
             "غُرْفَة النَّوْم is “the room of sleeping”, the bedroom: another two-noun phrase like عَاصِمَة مِصْر.",
             tables=[table(["English", "Arabic"],
                           [["house", "بَيْت"], ["apartment", "شَقَّة"], ["room", "غُرْفَة"], ["the bedroom", "غُرْفَة النَّوْم"],
                            ["salon (living room)", "صَالُون"], ["the dining room", "غُرْفَة الطَّعَام"], ["kitchen", "مَطْبَخ"],
                            ["bathroom", "حَمَّام"], ["balcony", "شُرْفَة"], ["garden", "حَدِيقَة"]],
                           say=[1], tlit=[1])]),
        card("Parts of the house",
             "Notice which are masculine and which are feminine: the adjective will have to match.",
             tables=[table(["English", "Arabic"],
                           [["door", "بَاب"], ["window", "نَافِذَة"], ["wall", "جِدَار"], ["floor, storey", "طَابِق"],
                            ["roof", "سَطْح"], ["stairs", "سُلَّم"], ["key", "مِفْتَاح"]],
                           say=[1], tlit=[1])],
             examples=[
                 ex("فِي الشَّقَّة غُرْفَة نَوْم وَمَطْبَخ وَحَمَّام.", "In the apartment there is a bedroom, a kitchen and a bathroom."),
                 ex("الْمَطْبَخ بِجَانِب الصَّالُون.", "The kitchen is next to the living room."),
                 ex("الْبَاب كَبِير وَالنَّافِذَة صَغِيرَة.", "The door is big and the window is small."),
                 ex("بَيْتِي قَدِيم، لَكِنَّ الْحَدِيقَة جَمِيلَة.", "My house is old, but the garden is beautiful."),
             ]),
    ],
    exercises=[
        M("Which word means “kitchen”?", "مَطْبَخ", ["حَمَّام", "صَالُون", "شُرْفَة"], "مَطْبَخ = kitchen."),
        M("Which word means “bathroom”?", "حَمَّام", ["مَطْبَخ", "غُرْفَة", "بَاب"], "حَمَّام = bathroom."),
        M("Which word means “window”?", "نَافِذَة", ["بَاب", "جِدَار", "سُلَّم"], "نَافِذَة = window."),
        M("Which word means “door”?", "بَاب", ["نَافِذَة", "سَطْح", "طَابِق"], "بَاب = door."),
        M("Which means “the bedroom”?", "غُرْفَة النَّوْم", ["غُرْفَة الطَّعَام", "صَالُون", "شُرْفَة"], "غُرْفَة النَّوْم = room of sleeping."),
        M("Which means “apartment”?", "شَقَّة", ["بَيْت", "غُرْفَة", "طَابِق"], "شَقَّة = apartment."),
        M("Which is feminine?", "نَافِذَة", ["بَاب", "مَطْبَخ", "حَمَّام"], "It ends in ة."),
        M("Which means “The kitchen is next to the living room”?", "الْمَطْبَخ بِجَانِب الصَّالُون", ["الْمَطْبَخ فَوْق الصَّالُون", "الصَّالُون بِجَانِب الْحَمَّام", "الْمَطْبَخ تَحْت الصَّالُون"], "بِجَانِب = next to."),
        F("الْبَاب كَبِير وَالنَّافِذَة ___.", "صَغِيرَة", ["صَغِير", "صِغَار", "الصَّغِير"], "نَافِذَة is feminine.", tr="The door is big and the window is small."),
        F("فِي الشَّقَّة غُرْفَة ___ وَمَطْبَخ.", "نَوْم", ["بَيْت", "بَاب", "طَابِق"], "A bedroom is a room of sleeping.", tr="In the apartment there is a bedroom and a kitchen."),
    ],
    verify=vw("بَيْت", "شَقَّة", "غُرْفَة", "النَّوْم", "صَالُون", "الطَّعَام", "مَطْبَخ", "حَمَّام", "شُرْفَة", "بَاب", "نَافِذَة",
              "جِدَار", "طَابِق", "سَطْح", "سُلَّم", "مِفْتَاح"),
)

# ---------------------------------------------------------------------------- 67
L67 = lesson(
    "Furniture",
    "طَاوِلَة · كُرْسِيّ · سَرِير · خِزَانَة",
    requires=["مكتب", "كرسي", "سرير", "طاولة", "غرفة"],
    cards=[
        card("Things in a room",
             "Most of these end in ة and are feminine, but not all. Check the gender before you describe them.",
             tables=[table(["English", "Arabic"],
                           [["table", "طَاوِلَة"], ["chair", "كُرْسِيّ"], ["bed", "سَرِير"], ["sofa", "أَرِيكَة"],
                            ["desk", "مَكْتَب"], ["cupboard, wardrobe", "خِزَانَة"], ["lamp", "مِصْبَاح"],
                            ["carpet", "سَجَّادَة"], ["mirror", "مِرْآة"], ["curtain", "سِتَارَة"],
                            ["refrigerator", "ثَلَّاجَة"], ["television", "تِلْفَاز"]],
                           say=[1], tlit=[1])],
             examples=[
                 ex("الطَّاوِلَة كَبِيرَة وَالْكُرْسِيّ صَغِير.", "The table is big and the chair is small."),
                 ex("السَّرِير جَدِيد وَالْخِزَانَة قَدِيمَة.", "The bed is new and the wardrobe is old."),
                 ex("فِي الصَّالُون أَرِيكَة وَطَاوِلَة وَتِلْفَاز.", "In the living room there is a sofa, a table and a television."),
                 ex("الثَّلَّاجَة فِي الْمَطْبَخ.", "The refrigerator is in the kitchen."),
             ]),
    ],
    exercises=[
        M("Which word means “table”?", "طَاوِلَة", ["كُرْسِيّ", "سَرِير", "خِزَانَة"], "طَاوِلَة = table."),
        M("Which word means “chair”?", "كُرْسِيّ", ["طَاوِلَة", "مَكْتَب", "مِرْآة"], "كُرْسِيّ = chair."),
        M("Which word means “bed”?", "سَرِير", ["كُرْسِيّ", "أَرِيكَة", "خِزَانَة"], "سَرِير = bed."),
        M("Which word means “mirror”?", "مِرْآة", ["مِصْبَاح", "سِتَارَة", "سَجَّادَة"], "مِرْآة = mirror."),
        M("Which word means “refrigerator”?", "ثَلَّاجَة", ["تِلْفَاز", "خِزَانَة", "مَطْبَخ"], "ثَلَّاجَة = refrigerator."),
        M("Which word means “lamp”?", "مِصْبَاح", ["سِتَارَة", "مِرْآة", "تِلْفَاز"], "مِصْبَاح = lamp."),
        M("Which means “The table is big”?", "الطَّاوِلَة كَبِيرَة", ["الطَّاوِلَة كَبِير", "طَاوِلَة الْكَبِيرَة", "الطَّاوِلَة الْكَبِير"], "طَاوِلَة is feminine."),
        M("Which means “The bed is new”?", "السَّرِير جَدِيد", ["السَّرِير جَدِيدَة", "السَّرِير الْجَدِيدَة", "سَرِير الْجَدِيد"], "سَرِير is masculine."),
        F("الْخِزَانَة ___.", "قَدِيمَة", ["قَدِيم", "قُدَمَاء", "الْقَدِيم"], "خِزَانَة is feminine.", tr="The wardrobe is old."),
        F("فِي الصَّالُون ___ وَطَاوِلَة.", "أَرِيكَة", ["جَبَل", "بَحْر", "نَهْر"], "Furniture for a living room.", tr="In the living room there is a sofa and a table."),
    ],
    verify=vw("طَاوِلَة", "كُرْسِيّ", "سَرِير", "أَرِيكَة", "مَكْتَب", "خِزَانَة", "مِصْبَاح", "سَجَّادَة", "مِرْآة", "سِتَارَة",
              "ثَلَّاجَة", "تِلْفَاز"),
)

# ---------------------------------------------------------------------------- 68
L68 = lesson(
    "My room",
    "فِي غُرْفَتِي سَرِير وَمَكْتَب",
    requires=["غرفة", "مكتب", "سرير", "باب", "نافذة", "بيت"],
    cards=[
        card("Describing a room",
             "Combine what you know: the position words, the furniture, and the pattern “in the room there is…”. "
             "When the thing you name is new in the sentence, it has no ال.",
             examples=[
                 ex("فِي غُرْفَتِي سَرِير وَمَكْتَب وَخِزَانَة.", "In my room there is a bed, a desk and a wardrobe."),
                 ex("السَّرِير بِجَانِب النَّافِذَة.", "The bed is next to the window."),
                 ex("الْمِصْبَاح فَوْق الْمَكْتَب.", "The lamp is above the desk."),
                 ex("الْكِتَاب عَلَى الْمَكْتَب وَالْقَلَم تَحْت الْكُرْسِيّ.", "The book is on the desk and the pen is under the chair."),
                 ex("الْمِرْآة عَلَى الْجِدَار.", "The mirror is on the wall."),
                 ex("أَيْنَ الْمِفْتَاح؟ هُوَ عَلَى الطَّاوِلَة.", "Where is the key? It is on the table."),
             ]),
    ],
    exercises=[
        M("«فِي غُرْفَتِي سَرِير وَمَكْتَب وَخِزَانَة.» What is in the room?", "A bed, a desk and a wardrobe", ["A sofa and a table", "A bed and a television", "A desk and a refrigerator"], "سَرِير وَمَكْتَب وَخِزَانَة."),
        M("«السَّرِير بِجَانِب النَّافِذَة.» Where is the bed?", "Next to the window", ["Under the window", "Behind the door", "Above the desk"], "بِجَانِب = next to."),
        M("«الْمِصْبَاح فَوْق الْمَكْتَب.» Where is the lamp?", "Above the desk", ["Under the desk", "Next to the bed", "On the wall"], "فَوْق = above."),
        M("«الْقَلَم تَحْت الْكُرْسِيّ.» Where is the pen?", "Under the chair", ["On the chair", "Behind the chair", "Next to the chair"], "تَحْت = under."),
        M("Which means “The mirror is on the wall”?", "الْمِرْآة عَلَى الْجِدَار", ["الْمِرْآة تَحْت الْجِدَار", "الْجِدَار عَلَى الْمِرْآة", "الْمِرْآة بِجَانِب النَّافِذَة"], "عَلَى = on."),
        M("Which means “Where is the key?”", "أَيْنَ الْمِفْتَاح؟", ["مَتَى الْمِفْتَاح؟", "كَيْفَ الْمِفْتَاح؟", "مَنْ الْمِفْتَاح؟"], "أَيْنَ = where."),
        M("Which means “In my room there is a bed”?", "فِي غُرْفَتِي سَرِير", ["غُرْفَتِي فِي سَرِير", "السَّرِير فِي غُرْفَتِي", "فِي سَرِير غُرْفَتِي"], "Place first, then a noun without ال."),
        F("الْكِتَاب ___ الْمَكْتَب.", "عَلَى", ["تَحْت", "مِنْ", "عَنْ"], "On top of.", tr="The book is on the desk."),
        F("السَّرِير ___ النَّافِذَة.", "بِجَانِب", ["فَوْق", "إِلَى", "مَعَ"], "Side by side.", tr="The bed is next to the window."),
    ],
    verify=vw("غُرْفَتِي", "مِفْتَاح", "الْمِفْتَاح", "الْجِدَار", "الْمِصْبَاح", "الْقَلَم"),
)

# ---------------------------------------------------------------------------- 69
L69 = lesson(
    "Exactly two: the dual",
    "كِتَابَان · غُرْفَتَان",
    requires=["كتاب", "بيت", "غرفة", "سيارة", "ولد"],
    cards=[
        card("A special form for two",
             "Arabic has three numbers: singular, dual (exactly two) and plural. The dual is formed by adding ـَان to the "
             "singular. You do not need the word for “two”; the ending already says it. After a preposition, or "
             "when the dual is an object, ـَان changes to ـَيْن.",
             tables=[table(["English", "Singular", "Two (subject)", "Two (after a preposition)"],
                           [["book", "كِتَاب", "كِتَابَان", "كِتَابَيْن"], ["house", "بَيْت", "بَيْتَان", "بَيْتَيْن"],
                            ["boy", "وَلَد", "وَلَدَان", "وَلَدَيْن"], ["bathroom", "حَمَّام", "حَمَّامَان", "حَمَّامَيْن"]],
                           say=[1, 2, 3], tlit=[2], gloss=False)]),
        card("Feminine nouns change ة to ت",
             "A noun that ends in ة changes it to ت before the dual ending. That is the same change you saw before an "
             "attached pronoun (مَدْرَسَتِي).",
             tables=[table(["English", "Singular", "Two (subject)", "Two (after a preposition)"],
                           [["room", "غُرْفَة", "غُرْفَتَان", "غُرْفَتَيْن"], ["car", "سَيَّارَة", "سَيَّارَتَان", "سَيَّارَتَيْن"],
                            ["hour", "سَاعَة", "سَاعَتَان", "سَاعَتَيْن"], ["apartment", "شَقَّة", "شَقَّتَان", "شَقَّتَيْن"]],
                           say=[1, 2, 3], tlit=[2], gloss=False)],
             examples=[
                 ex("فِي الْبَيْت حَمَّامَان.", "There are two bathrooms in the house."),
                 ex("فِي الشَّقَّة غُرْفَتَان.", "There are two rooms in the apartment."),
                 ex("أَنْظُر إِلَى بَيْتَيْن.", "I am looking at two houses."),
                 ex("هُوَ مَعَ وَلَدَيْن.", "He is with two boys."),
             ]),
    ],
    exercises=[
        M("Which means “two books” (subject)?", "كِتَابَان", ["كِتَابَيْن", "كُتُب", "كِتَاب"], "Add ـَان."),
        M("Which means “two rooms” (subject)?", "غُرْفَتَان", ["غُرْفَاتَان", "غُرَف", "غُرْفَة"], "ة becomes ت, then ـَان."),
        M("Which means “two cars” (subject)?", "سَيَّارَتَان", ["سَيَّارَات", "سَيَّارَانَة", "سَيَّارَتُون"], "Dual of a feminine noun."),
        M("Which means “two houses” (subject)?", "بَيْتَان", ["بُيُوت", "بَيْتَات", "بَيْتُون"], "Add ـَان."),
        M("Which means “with two boys”?", "مَعَ وَلَدَيْن", ["مَعَ وَلَدَان", "مَعَ أَوْلَاد", "مَعَ وَلَدَات"], "After a preposition: ـَيْن."),
        M("Which means “I am looking at two houses”?", "أَنْظُر إِلَى بَيْتَيْن", ["أَنْظُر إِلَى بَيْتَان", "أَنْظُر إِلَى بُيُوت", "أَنْظُر إِلَى بَيْت"], "After إِلَى: ـَيْن."),
        M("Do you need to say اِثْنَان (two) with a dual noun?", "No: the ending already means two", ["Yes, always", "Only in the plural", "Only with feminine nouns"], "The dual ending is enough."),
        F("فِي الْبَيْت ___.", "حَمَّامَان", ["حَمَّام", "حَمَّامَات", "حَمَّامُون"], "Two bathrooms.", tr="There are two bathrooms in the house."),
        F("فِي الشَّقَّة ___.", "غُرْفَتَان", ["غُرْفَة", "غُرْفَاتَان", "غُرَف"], "Two rooms.", tr="There are two rooms in the apartment."),
    ],
    verify=(vd("كِتَاب", "كِتَابَان", "كِتَابَيْن") + vd("بَيْت", "بَيْتَان", "بَيْتَيْن") + vd("وَلَد", "وَلَدَان", "وَلَدَيْن")
            + vd("حَمَّام", "حَمَّامَان", "حَمَّامَيْن") + vd("غُرْفَة", "غُرْفَتَان", "غُرْفَتَيْن")
            + vd("سَيَّارَة", "سَيَّارَتَان", "سَيَّارَتَيْن") + vd("سَاعَة", "سَاعَتَان", "سَاعَتَيْن")
            + vd("شَقَّة", "شَقَّتَان", "شَقَّتَيْن")),
)

# ---------------------------------------------------------------------------- 70
L70 = lesson(
    "The dual with adjectives and verbs",
    "الْكِتَابَان جَدِيدَان · هُمَا يَكْتُبَان",
    requires=["كتاب", "غرفة", "طالب", "جديد", "كبير"],
    cards=[
        card("Adjectives agree in the dual",
             "An adjective that describes a dual noun is also dual. Masculine adjectives add ـَان, feminine adjectives "
             "change ة to ت and add ـَان.",
             tables=[table(["English", "Arabic"],
                           [["two new books", "كِتَابَان جَدِيدَان"], ["two big rooms", "غُرْفَتَان كَبِيرَتَان"],
                            ["two tall boys", "وَلَدَان طَوِيلَان"], ["two small cars", "سَيَّارَتَان صَغِيرَتَان"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("الْكِتَابَان جَدِيدَان.", "The two books are new."),
                 ex("الْغُرْفَتَان كَبِيرَتَان.", "The two rooms are big."),
             ]),
        card("They two, you two",
             "The pronouns for two people are أَنْتُمَا (you two) and هُمَا (they two, for men or women). A verb that "
             "follows its subject takes the dual ending ـَان, with يَـ for two males and تَـ for two females.",
             examples=[
                 ex("هُمَا طَالِبَان.", "They (two men) are students."),
                 ex("هُمَا طَالِبَتَان.", "They (two women) are students."),
                 ex("الطَّالِبَان يَدْرُسَان فِي الْمَكْتَبَة.", "The two students study in the library.", "يَدْرُسَان"),
                 ex("الْبِنْتَان تَلْعَبَان فِي الْحَدِيقَة.", "The two girls play in the garden.", "تَلْعَبَان"),
                 ex("يَلْعَب الْوَلَدَان فِي الشَّارِع.", "The two boys play in the street. (verb first stays singular)"),
             ]),
    ],
    exercises=[
        M("Which means “two new books”?", "كِتَابَان جَدِيدَان", ["كِتَابَان جَدِيدَتَان", "كِتَابَان جَدِيد", "كُتُب جَدِيدَة"], "Masculine dual noun and adjective."),
        M("Which means “two big rooms”?", "غُرْفَتَان كَبِيرَتَان", ["غُرْفَتَان كَبِيرَان", "غُرْفَتَان كَبِيرَة", "غُرَف كَبِيرَتَان"], "Feminine dual noun and adjective."),
        M("Which means “They (two women) are students”?", "هُمَا طَالِبَتَان", ["هُمَا طَالِبَان", "هُنَّ طَالِبَات", "هُمَا طَالِبَة"], "Feminine dual."),
        M("Which means “you two”?", "أَنْتُمَا", ["أَنْتُم", "هُمَا", "أَنْتِ"], "أَنْتُمَا = you two."),
        M("Which means “the two students study” (a verb after the subject)?", "الطَّالِبَان يَدْرُسَان", ["الطَّالِبَان يَدْرُسُون", "الطَّالِبَان يَدْرُس", "الطَّالِبَان تَدْرُسَان"], "A masculine dual verb: يَـ + ـَان.", lemma=None),
        M("Which means “The two girls play” (verb after the subject)?", "الْبِنْتَان تَلْعَبَان", ["الْبِنْتَان يَلْعَبَان", "الْبِنْتَان تَلْعَبُون", "الْبِنْتَان تَلْعَب"], "A feminine dual verb: تَـ + ـَان."),
        M("When the verb comes first, the verb is…", "singular: يَلْعَب الْوَلَدَان", ["dual: يَلْعَبَان الْوَلَدَان", "plural: يَلْعَبُون الْوَلَدَان", "feminine: تَلْعَبَان الْوَلَدَان"], "A verb before its subject stays singular."),
        F("الْغُرْفَتَان ___.", "كَبِيرَتَان", ["كَبِيرَان", "كَبِيرَة", "كَبِيرَات"], "Feminine dual.", tr="The two rooms are big."),
        F("الْكِتَابَان ___.", "جَدِيدَان", ["جَدِيدَتَان", "جَدِيد", "جُدُد"], "Masculine dual.", tr="The two books are new."),
    ],
    verify=(vd("جَدِيد", "جَدِيدَان", "جَدِيدَيْن") + vd("كَبِيرَة", "كَبِيرَتَان", "كَبِيرَتَيْن") + vd("طَوِيل", "طَوِيلَان", "طَوِيلَيْن")
            + vd("صَغِيرَة", "صَغِيرَتَان", "صَغِيرَتَيْن") + vd("طَالِب", "طَالِبَان", "طَالِبَيْن") + vd("طَالِبَة", "طَالِبَتَان", "طَالِبَتَيْن")
            + vd("بِنْت", "بِنْتَان", "بِنْتَيْن") + vd("وَلَد", "وَلَدَان", "وَلَدَيْن")
            + vv("درس", "pres", huma_m="يَدْرُسَان") + vv("لعب", "pres", huma_f="تَلْعَبَان", huma_m="يَلْعَبَان")
            + vw("أَنْتُمَا", "هُمَا")),
)

# ---------------------------------------------------------------------------- 71
L71 = lesson(
    "One and two",
    "وَاحِد · وَاحِدَة · اِثْنَان · اِثْنَتَان",
    requires=["واحد", "غرفة", "بيت", "يوم", "كتاب"],
    cards=[
        card("One: it follows the noun",
             "“One” is an adjective: it follows the noun and agrees with its gender. A masculine noun takes وَاحِد and "
             "a feminine noun takes وَاحِدَة.",
             tables=[table(["English", "Arabic"],
                           [["one book", "كِتَاب وَاحِد"], ["one house", "بَيْت وَاحِد"], ["one day", "يَوْم وَاحِد"],
                            ["one room", "غُرْفَة وَاحِدَة"], ["one car", "سَيَّارَة وَاحِدَة"], ["one hour", "سَاعَة وَاحِدَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Two: the dual, plus an optional اِثْنَان",
             "For two, you normally use the dual alone. If you want to stress “two”, add اِثْنَان (for a masculine noun) "
             "or اِثْنَتَان (for a feminine noun) after it. When you count out loud without a noun, you say "
             "وَاحِد, اِثْنَان.",
             tables=[table(["English", "Arabic"],
                           [["two books", "كِتَابَان"], ["two books (stressed)", "كِتَابَان اِثْنَان"],
                            ["two rooms", "غُرْفَتَان"], ["two rooms (stressed)", "غُرْفَتَان اِثْنَتَان"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("فِي الْبَيْت حَمَّام وَاحِد.", "There is one bathroom in the house."),
                 ex("فِي الْبَيْت غُرْفَتَان وَمَطْبَخ وَاحِد.", "There are two rooms and one kitchen in the house."),
                 ex("أَسْكُن فِي شَقَّة وَاحِدَة.", "I live in one apartment."),
             ]),
    ],
    exercises=[
        M("Which means “one book”?", "كِتَاب وَاحِد", ["كِتَاب وَاحِدَة", "وَاحِد كِتَاب", "كِتَابَان"], "كِتَاب is masculine."),
        M("Which means “one room”?", "غُرْفَة وَاحِدَة", ["غُرْفَة وَاحِد", "وَاحِدَة غُرْفَة", "غُرْفَتَان"], "غُرْفَة is feminine."),
        M("Which means “one day”?", "يَوْم وَاحِد", ["يَوْم وَاحِدَة", "يَوْمَان", "أَيَّام"], "يَوْم is masculine."),
        M("Which means “two rooms”?", "غُرْفَتَان", ["غُرْفَة اِثْنَان", "اِثْنَان غُرْفَة", "غُرَف"], "Use the dual."),
        M("Which stresses “two books”?", "كِتَابَان اِثْنَان", ["كِتَابَان اِثْنَتَان", "كِتَابَان وَاحِد", "اِثْنَان كِتَاب"], "Masculine noun, so اِثْنَان."),
        M("Which stresses “two rooms”?", "غُرْفَتَان اِثْنَتَان", ["غُرْفَتَان اِثْنَان", "غُرْفَتَان وَاحِدَة", "اِثْنَتَان غُرْفَة"], "Feminine noun, so اِثْنَتَان."),
        M("Where does وَاحِد go?", "After the noun", ["Before the noun", "At the start of the sentence", "It replaces the noun"], "“One” is an adjective, so it follows."),
        F("فِي الْبَيْت حَمَّام ___.", "وَاحِد", ["وَاحِدَة", "اِثْنَان", "اِثْنَتَان"], "حَمَّام is masculine.", tr="There is one bathroom in the house."),
        F("أَسْكُن فِي شَقَّة ___.", "وَاحِدَة", ["وَاحِد", "اِثْنَتَان", "اِثْنَان"], "شَقَّة is feminine.", tr="I live in one apartment."),
    ],
    verify=vw("وَاحِد", "وَاحِدَة", "اِثْنَان", "اِثْنَتَان", "كِتَابَان", "غُرْفَتَان") + vf("وَاحِد", "وَاحِدَة"),
)

# ---------------------------------------------------------------------------- 72
L72 = lesson(
    "Three to ten: with masculine nouns",
    "ثَلَاثَة كُتُب · خَمْسَة طُلَّاب",
    requires=["كتاب", "بيت", "طالب", "يوم", "عشرة"],
    cards=[
        card("The number looks feminine",
             "From three to ten, the number has the opposite gender to the singular of the thing counted. With a masculine noun, "
             "the number ends in ـَة, which looks feminine. The noun comes after the number, and it is plural. "
             "Digits are shown for reference; they are not read aloud here.",
             tables=[table(["Digit", "Arabic", "English"],
                           [["٣", "ثَلَاثَة كُتُب", "three books"], ["٤", "أَرْبَعَة بُيُوت", "four houses"],
                            ["٥", "خَمْسَة طُلَّاب", "five students"], ["٦", "سِتَّة أَقْلَام", "six pens"],
                            ["٧", "سَبْعَة أَيَّام", "seven days"], ["٨", "ثَمَانِيَة أَوْلَاد", "eight boys"],
                            ["٩", "تِسْعَة شَوَارِع", "nine streets"], ["١٠", "عَشَرَة مَسَاجِد", "ten mosques"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "A plural of things that follows the number is described with a feminine singular adjective, as before. "
             "A sound masculine plural after a number takes the ـِين ending.",
             examples=[
                 ex("عَلَى الطَّاوِلَة ثَلَاثَة كُتُب.", "There are three books on the table."),
                 ex("سَبْعَة أَيَّام فِي الْأُسْبُوع.", "There are seven days in a week."),
                 ex("أَعْمَل خَمْسَة أَيَّام فِي الْأُسْبُوع.", "I work five days a week."),
                 ex("فِي الْمَدْرَسَة خَمْسَة مُدَرِّسِين.", "There are five teachers in the school."),
                 ex("ثَلَاثَة كُتُب جَدِيدَة", "three new books"),
             ]),
    ],
    exercises=[
        M("Which means “three books”? (كِتَاب is masculine)", "ثَلَاثَة كُتُب", ["ثَلَاث كُتُب", "ثَلَاثَة كِتَاب", "ثَلَاث كِتَاب"], "Masculine noun: the number ends in ـَة."),
        M("Which means “five students”? (طَالِب is masculine)", "خَمْسَة طُلَّاب", ["خَمْس طُلَّاب", "خَمْسَة طَالِب", "خَمْس طَالِب"], "Masculine noun: خَمْسَة."),
        M("Which means “seven days”? (يَوْم is masculine)", "سَبْعَة أَيَّام", ["سَبْع أَيَّام", "سَبْعَة يَوْم", "سَبْعَة يَوْمَان"], "Masculine noun: سَبْعَة, plural noun."),
        M("Which means “ten mosques”? (مَسْجِد is masculine)", "عَشَرَة مَسَاجِد", ["عَشْر مَسَاجِد", "عَشَرَة مَسْجِد", "عَشْر مَسْجِد"], "Masculine noun: عَشَرَة."),
        M("After the numbers three to ten, the noun is…", "plural", ["singular", "dual", "it does not matter"], "ثَلَاثَة كُتُب, not ثَلَاثَة كِتَاب."),
        M("Which gender does the number 3–10 have, compared with the noun?", "The opposite", ["The same", "It has none", "Always feminine"], "This is called polarity."),
        M("Which means “three new books”?", "ثَلَاثَة كُتُب جَدِيدَة", ["ثَلَاثَة كُتُب جَدِيد", "ثَلَاثَة كُتُب الْجَدِيدَة", "ثَلَاث كُتُب جَدِيدَة"], "The adjective after a plural of things: feminine singular."),
        F("عَلَى الطَّاوِلَة ___ كُتُب.", "ثَلَاثَة", ["ثَلَاث", "ثَلَاثُون", "وَاحِد"], "كِتَاب is masculine.", tr="There are three books on the table."),
        F("أَعْمَل ___ أَيَّام فِي الْأُسْبُوع.", "خَمْسَة", ["خَمْس", "خَمْسُون", "اِثْنَان"], "يَوْم is masculine.", tr="I work five days a week."),
    ],
    verify=(vn(3, "m", "ثَلَاثَة") + vn(4, "m", "أَرْبَعَة") + vn(5, "m", "خَمْسَة") + vn(6, "m", "سِتَّة") + vn(7, "m", "سَبْعَة")
            + vn(8, "m", "ثَمَانِيَة") + vn(9, "m", "تِسْعَة") + vn(10, "m", "عَشَرَة")
            + vpb("كِتَاب", "كُتُب") + vpb("بَيْت", "بُيُوت") + vpb("قَلَم", "أَقْلَام") + vpb("وَلَد", "أَوْلَاد")
            + vpb("شَارِع", "شَوَارِع") + vpb("مَسْجِد", "مَسَاجِد") + vpb("طَالِب", "طُلَّاب") + vpb("يَوْم", "أَيَّام")
            + vps("مُدَرِّس", "مُدَرِّسِين", "obl")),
)

# ---------------------------------------------------------------------------- 73
L73 = lesson(
    "Three to ten: with feminine nouns",
    "ثَلَاث غُرَف · عَشْر سَنَوَات",
    requires=["غرفة", "سيارة", "مدينة", "ساعة", "سنة", "عشرة"],
    cards=[
        card("The number loses its ة",
             "With a feminine noun, the number is in its short form with no ـَة. The noun is again plural and comes after the "
             "number.",
             tables=[table(["Digit", "Arabic", "English"],
                           [["٣", "ثَلَاث غُرَف", "three rooms"], ["٤", "أَرْبَع سَيَّارَات", "four cars"],
                            ["٥", "خَمْس مُدُن", "five cities"], ["٦", "سِتّ طَالِبَات", "six students (women)"],
                            ["٧", "سَبْع سَاعَات", "seven hours"], ["٨", "ثَمَانِي شُقَق", "eight apartments"],
                            ["٩", "تِسْع مَدَارِس", "nine schools"], ["١٠", "عَشْر سَنَوَات", "ten years"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Compare these with the last lesson: the noun decides which form of the number you need.",
             examples=[
                 ex("فِي الشَّقَّة ثَلَاث غُرَف.", "There are three rooms in the apartment."),
                 ex("أَدْرُس أَرْبَع سَاعَات.", "I study for four hours."),
                 ex("فِي الْمَدِينَة تِسْع مَدَارِس.", "There are nine schools in the city."),
                 ex("أَسْكُن هُنَا مُنْذُ عَشْر سَنَوَات.", "I have lived here for ten years."),
                 ex("ثَلَاث غُرَف كَبِيرَة", "three big rooms"),
             ]),
    ],
    exercises=[
        M("Which means “three rooms”? (غُرْفَة is feminine)", "ثَلَاث غُرَف", ["ثَلَاثَة غُرَف", "ثَلَاث غُرْفَة", "ثَلَاثَة غُرْفَة"], "Feminine noun: the short number, plural noun."),
        M("Which means “four cars”? (سَيَّارَة is feminine)", "أَرْبَع سَيَّارَات", ["أَرْبَعَة سَيَّارَات", "أَرْبَع سَيَّارَة", "أَرْبَعَة سَيَّارَة"], "Feminine noun: أَرْبَع."),
        M("Which means “five cities”? (مَدِينَة is feminine)", "خَمْس مُدُن", ["خَمْسَة مُدُن", "خَمْس مَدِينَة", "خَمْسَة مَدِينَة"], "Feminine noun: خَمْس."),
        M("Which means “seven hours”? (سَاعَة is feminine)", "سَبْع سَاعَات", ["سَبْعَة سَاعَات", "سَبْع سَاعَة", "سَبْعَة سَاعَة"], "Feminine noun: سَبْع."),
        M("Which means “nine schools”? (مَدْرَسَة is feminine)", "تِسْع مَدَارِس", ["تِسْعَة مَدَارِس", "تِسْع مَدْرَسَة", "تِسْعَة مَدْرَسَة"], "Feminine noun: تِسْع."),
        M("Which means “ten years”? (سَنَة is feminine)", "عَشْر سَنَوَات", ["عَشَرَة سَنَوَات", "عَشْر سَنَة", "عَشَرَة سَنَة"], "Feminine noun: عَشْر."),
        M("Which means “three books” (masculine) and which “three rooms” (feminine)?", "ثَلَاثَة كُتُب · ثَلَاث غُرَف", ["ثَلَاث كُتُب · ثَلَاثَة غُرَف", "ثَلَاثَة كُتُب · ثَلَاثَة غُرَف", "ثَلَاث كُتُب · ثَلَاث غُرَف"], "Opposite gender to the noun."),
        F("فِي الشَّقَّة ___ غُرَف.", "ثَلَاث", ["ثَلَاثَة", "ثَلَاثُون", "وَاحِدَة"], "غُرْفَة is feminine.", tr="There are three rooms in the apartment."),
        F("أَدْرُس ___ سَاعَات.", "أَرْبَع", ["أَرْبَعَة", "أَرْبَعُون", "اِثْنَتَان"], "سَاعَة is feminine.", tr="I study for four hours."),
    ],
    verify=(vn(3, "f", "ثَلَاث") + vn(4, "f", "أَرْبَع") + vn(5, "f", "خَمْس") + vn(6, "f", "سِتّ") + vn(7, "f", "سَبْع")
            + vn(8, "f", "ثَمَانِي") + vn(9, "f", "تِسْع") + vn(10, "f", "عَشْر")
            + vn(3, "m", "ثَلَاثَة")
            + vpb("غُرْفَة", "غُرَف") + vpb("شَقَّة", "شُقَق") + vpb("مَدْرَسَة", "مَدَارِس") + vpb("مَدِينَة", "مُدُن")
            + vpb("سَنَة", "سَنَوَات") + vps("سَيَّارَة", "سَيَّارَات") + vps("طَالِبَة", "طَالِبَات") + vps("سَاعَة", "سَاعَات")),
)

# ---------------------------------------------------------------------------- 74
L74 = lesson(
    "How many?",
    "كَمْ غُرْفَة؟ خَمْس غُرَف",
    requires=["كم", "غرفة", "كتاب", "واحد", "عشرة"],
    cards=[
        card("كَمْ + a singular noun",
             "To ask “how many”, use كَمْ followed by a singular noun without ال. For three to ten, the answer is a "
             "number and then a plural noun, with the number in the form that fits the gender of the noun.",
             tables=[table(["Question", "Answer"],
                           [["كَمْ كِتَاب؟", "ثَلَاثَة كُتُب"], ["كَمْ غُرْفَة؟", "ثَلَاث غُرَف"], ["كَمْ يَوْم؟", "خَمْسَة أَيَّام"],
                            ["كَمْ سَاعَة؟", "خَمْس سَاعَات"], ["كَمْ طَالِب؟", "سِتَّة طُلَّاب"], ["كَمْ طَالِبَة؟", "سِتّ طَالِبَات"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Questions and answers",
             "In an answer, the place usually comes first, then the number and the thing counted.",
             examples=[
                 ex("كَمْ غُرْفَة فِي الْبَيْت؟", "How many rooms are in the house?"),
                 ex("فِي الْبَيْت خَمْس غُرَف.", "There are five rooms in the house."),
                 ex("كَمْ كِتَاب عَلَى الطَّاوِلَة؟", "How many books are on the table?"),
                 ex("عَلَى الطَّاوِلَة ثَلَاثَة كُتُب.", "There are three books on the table."),
                 ex("كَمْ يَوْم فِي الْأُسْبُوع؟", "How many days are in a week?"),
                 ex("سَبْعَة أَيَّام.", "Seven days."),
             ]),
    ],
    exercises=[
        M("Which question asks “How many rooms?”", "كَمْ غُرْفَة؟", ["كَمْ غُرَف؟", "كَمْ غُرْفَتَان؟", "أَيْنَ غُرْفَة؟"], "كَمْ + singular noun."),
        M("Which answers “How many books?” with three?", "ثَلَاثَة كُتُب", ["ثَلَاث كُتُب", "ثَلَاثَة كِتَاب", "ثَلَاث كِتَاب"], "كِتَاب is masculine."),
        M("Which answers “How many rooms?” with three?", "ثَلَاث غُرَف", ["ثَلَاثَة غُرَف", "ثَلَاث غُرْفَة", "ثَلَاثَة غُرْفَة"], "غُرْفَة is feminine."),
        M("Which answers “How many days?” with five?", "خَمْسَة أَيَّام", ["خَمْس أَيَّام", "خَمْسَة يَوْم", "خَمْس يَوْم"], "يَوْم is masculine."),
        M("Which answers “How many hours?” with four?", "أَرْبَع سَاعَات", ["أَرْبَعَة سَاعَات", "أَرْبَع سَاعَة", "أَرْبَعَة سَاعَة"], "سَاعَة is feminine."),
        M("Which answers “How many students (women)?” with six?", "سِتّ طَالِبَات", ["سِتَّة طَالِبَات", "سِتّ طَالِبَة", "سِتَّة طَالِبَة"], "طَالِبَة is feminine."),
        M("Which means “There are seven days in a week”?", "سَبْعَة أَيَّام فِي الْأُسْبُوع", ["سَبْع أَيَّام فِي الْأُسْبُوع", "سَبْعَة يَوْم فِي الْأُسْبُوع", "فِي الْأُسْبُوع سَبْعَة يَوْم"], "يَوْم is masculine; the noun after the number is plural."),
        F("كَمْ ___ فِي الْبَيْت؟", "غُرْفَة", ["غُرَف", "غُرْفَتَان", "غُرْفَات"], "Singular noun after كَمْ.", tr="How many rooms are in the house?"),
        F("فِي الْبَيْت خَمْس ___.", "غُرَف", ["غُرْفَة", "غُرْفَتَان", "غُرَفُون"], "Plural noun after the number.", tr="There are five rooms in the house."),
    ],
    verify=(vn(3, "m", "ثَلَاثَة") + vn(3, "f", "ثَلَاث") + vn(5, "m", "خَمْسَة") + vn(5, "f", "خَمْس") + vn(6, "m", "سِتَّة")
            + vn(6, "f", "سِتّ") + vn(4, "f", "أَرْبَع") + vn(7, "m", "سَبْعَة") + vpb("غُرْفَة", "غُرَف") + vpb("يَوْم", "أَيَّام")
            + vpb("كِتَاب", "كُتُب") + vw("كَمْ")),
)

# ---------------------------------------------------------------------------- 75
L75 = lesson(
    "The iḍāfa: the teacher’s house",
    "بَيْت الْمُدَرِّس · مِفْتَاح الْبَيْت",
    requires=["بيت", "باب", "مدرسة", "عاصمة", "مدير", "غرفة"],
    cards=[
        card("Noun + noun",
             "Arabic says “the house of the teacher”, “the key of the house”, by putting two nouns side by side. This "
             "is the iḍāfa. The first noun never takes ال or a possessive ending. The second noun "
             "decides whether the whole phrase is definite.",
             tables=[table(["Arabic", "English"],
                           [["بَيْت مُدَرِّس", "a teacher’s house"], ["بَيْت الْمُدَرِّس", "the teacher’s house"],
                            ["مِفْتَاح الْبَيْت", "the house key"], ["بَاب الْغُرْفَة", "the door of the room"],
                            ["بَاب غُرْفَة النَّوْم", "the bedroom door"], ["مُدِير الْمَدْرَسَة", "the principal of the school"],
                            ["سَيَّارَة أَبِي", "my father’s car"], ["كِتَاب الطَّالِبَة", "the (female) student’s book"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("A chain, and an adjective",
             "A third noun can be added, as in بَاب غُرْفَة النَّوْم. An adjective that comes at the end agrees with the "
             "noun it describes, and it takes ال, because the whole phrase is definite. Compare the two sentences below: "
             "the gender of the adjective shows which noun it belongs to.",
             examples=[
                 ex("غُرْفَة الْمُدِير الْجَدِيدَة", "the director’s new room (the room is new)", "الْجَدِيدَة"),
                 ex("غُرْفَة الْمُدِير الْجَدِيد", "the room of the new director (the director is new)", "الْجَدِيد"),
                 ex("مِفْتَاح الْبَيْت عَلَى الطَّاوِلَة.", "The house key is on the table."),
                 ex("مُدِير الْمَدْرَسَة جَدِيد.", "The principal of the school is new."),
             ]),
    ],
    exercises=[
        M("Which means “the door of the room”?", "بَاب الْغُرْفَة", ["الْبَاب الْغُرْفَة", "غُرْفَة الْبَاب", "الْبَاب غُرْفَة"], "First noun without ال, second with ال."),
        M("Which means “the house key”?", "مِفْتَاح الْبَيْت", ["الْمِفْتَاح الْبَيْت", "بَيْت الْمِفْتَاح", "الْمِفْتَاح بَيْت"], "مِفْتَاح الْبَيْت."),
        M("Which means “the principal of the school”?", "مُدِير الْمَدْرَسَة", ["الْمُدِير الْمَدْرَسَة", "الْمَدْرَسَة مُدِير", "مَدْرَسَة الْمُدِير"], "First noun without ال."),
        M("Which means “the bedroom door”?", "بَاب غُرْفَة النَّوْم", ["الْبَاب غُرْفَة النَّوْم", "بَاب الْغُرْفَة النَّوْم", "غُرْفَة النَّوْم الْبَاب"], "A chain of three nouns; ال only on the last."),
        M("Which means “my father’s car”?", "سَيَّارَة أَبِي", ["السَّيَّارَة أَبِي", "أَبِي سَيَّارَة", "الْأَب سَيَّارَة"], "أَبِي already makes the phrase definite."),
        M("Which noun in an iḍāfa never takes ال?", "The first", ["The second", "Both", "Neither"], "بَيْت الْمُدَرِّس: ال is on the second only."),
        M("Which means “the director’s new room” (the room is new)?", "غُرْفَة الْمُدِير الْجَدِيدَة", ["غُرْفَة الْمُدِير الْجَدِيد", "غُرْفَة الْمُدِير جَدِيدَة", "غُرْفَة الْمُدِير جَدِيد"], "الْجَدِيدَة is feminine like غُرْفَة, with ال."),
        F("___ الْبَيْت عَلَى الطَّاوِلَة.", "مِفْتَاح", ["الْمِفْتَاح", "مَفَاتِيح", "مِفْتَاحَان"], "The first noun has no ال.", tr="The house key is on the table."),
        F("غُرْفَة الْمُدِير ___.", "الْجَدِيدَة", ["الْجَدِيد", "جَدِيدَة", "جَدِيد"], "The room is new: feminine, with ال.", tr="the director’s new room"),
    ],
    verify=vw("الْمُدَرِّس", "الْبَيْت", "الْغُرْفَة", "مُدِير", "الْمُدِير", "الْمَدْرَسَة", "الطَّالِبَة", "الْجَدِيدَة", "الْجَدِيد",
              "مِفْتَاح"),
)

# ---------------------------------------------------------------------------- 76
L76 = lesson(
    "How long? Days, weeks, years",
    "ثَلَاثَة أَيَّام · سَنَتَان · لِمُدَّة",
    requires=["يوم", "أسبوع", "شهر", "سنة", "ساعة", "مدة"],
    cards=[
        card("One, two, three or more",
             "Each unit of time follows the same pattern as everything you have just learned. Notice the gender: يَوْم, "
             "أُسْبُوع and شَهْر are masculine; سَنَة, سَاعَة and دَقِيقَة are feminine.",
             tables=[table(["English", "One", "Two", "Three"],
                           [["day", "يَوْم وَاحِد", "يَوْمَان", "ثَلَاثَة أَيَّام"], ["week", "أُسْبُوع وَاحِد", "أُسْبُوعَان", "ثَلَاثَة أَسَابِيع"],
                            ["month", "شَهْر وَاحِد", "شَهْرَان", "ثَلَاثَة أَشْهُر"], ["year", "سَنَة وَاحِدَة", "سَنَتَان", "ثَلَاث سَنَوَات"],
                            ["hour", "سَاعَة وَاحِدَة", "سَاعَتَان", "ثَلَاث سَاعَات"], ["minute", "دَقِيقَة وَاحِدَة", "دَقِيقَتَان", "ثَلَاث دَقَائِق"]],
                           say=[1, 2, 3], tlit=[3], gloss=False)]),
        card("Words for “for”, “since”, “after”, “before”",
             "لِمُدَّة means “for a period of”, مُنْذُ means “since” or “for (up to now)”, and بَعْد and قَبْل mean "
             "“after” and “before”. After مُنْذُ, بَعْد and قَبْل a dual noun ends in ـَيْن.",
             examples=[
                 ex("أَسْكُن هُنَا مُنْذُ سَنَتَيْن.", "I have lived here for two years.", "مُنْذُ"),
                 ex("سَأَذْهَب إِلَى الْقَاهِرَة لِمُدَّة ثَلَاثَة أَيَّام.", "I will go to Cairo for three days.", "لِمُدَّة"),
                 ex("الرِّحْلَة سَاعَتَان.", "The trip is two hours."),
                 ex("بَعْد أُسْبُوع سَأَذْهَب إِلَى عَمَّان.", "In a week I will go to Amman.", "بَعْد"),
                 ex("الدَّرْس قَبْل الْعَشَاء.", "The lesson is before dinner.", "قَبْل"),
             ]),
    ],
    exercises=[
        M("Which means “three days”?", "ثَلَاثَة أَيَّام", ["ثَلَاث أَيَّام", "ثَلَاثَة يَوْم", "ثَلَاث يَوْم"], "يَوْم is masculine."),
        M("Which means “three years”?", "ثَلَاث سَنَوَات", ["ثَلَاثَة سَنَوَات", "ثَلَاث سَنَة", "ثَلَاثَة سَنَة"], "سَنَة is feminine."),
        M("Which means “two hours”?", "سَاعَتَان", ["سَاعَات", "سَاعَة اِثْنَان", "اِثْنَان سَاعَة"], "The dual."),
        M("Which means “two weeks”?", "أُسْبُوعَان", ["أُسْبُوعَات", "ثَلَاثَة أَسَابِيع", "أُسْبُوع وَاحِد"], "The dual."),
        M("Which means “one year”?", "سَنَة وَاحِدَة", ["سَنَة وَاحِد", "سَنَتَان", "وَاحِدَة سَنَة"], "سَنَة is feminine."),
        M("Which word means “since”?", "مُنْذُ", ["بَعْد", "قَبْل", "لِمُدَّة"], "مُنْذُ = since, for."),
        M("Which means “I have lived here for two years”?", "أَسْكُن هُنَا مُنْذُ سَنَتَيْن", ["أَسْكُن هُنَا لِمُدَّة سَنَة", "سَأَسْكُن هُنَا مُنْذُ سَنَتَان", "أَسْكُن هُنَا بَعْد سَنَتَيْن"], "مُنْذُ + the dual."),
        M("Which means “after a week”?", "بَعْد أُسْبُوع", ["قَبْل أُسْبُوع", "مُنْذُ أُسْبُوع", "لِمُدَّة أُسْبُوع"], "بَعْد = after."),
        F("سَأَذْهَب إِلَى عَمَّان ___ ثَلَاثَة أَيَّام.", "لِمُدَّة", ["مُنْذُ", "قَبْل", "عَنْ"], "For a period.", tr="I will go to Amman for three days."),
        F("الدَّرْس ___ الْعَشَاء.", "قَبْل", ["بَعْد", "مُنْذُ", "تَحْت"], "The lesson comes first.", tr="The lesson is before dinner."),
    ],
    verify=(vd("يَوْم", "يَوْمَان", "يَوْمَيْن") + vd("أُسْبُوع", "أُسْبُوعَان", "أُسْبُوعَيْن") + vd("شَهْر", "شَهْرَان", "شَهْرَيْن")
            + vd("سَنَة", "سَنَتَان", "سَنَتَيْن") + vd("سَاعَة", "سَاعَتَان", "سَاعَتَيْن") + vd("دَقِيقَة", "دَقِيقَتَان", "دَقِيقَتَيْن")
            + vpb("يَوْم", "أَيَّام") + vpb("أُسْبُوع", "أَسَابِيع") + vpb("شَهْر", "أَشْهُر") + vpb("سَنَة", "سَنَوَات")
            + vpb("دَقِيقَة", "دَقَائِق") + vps("سَاعَة", "سَاعَات") + vn(3, "m", "ثَلَاثَة") + vn(3, "f", "ثَلَاث")
            + vw("مُدَّة", "مُنْذُ", "بَعْد", "قَبْل")),
)

# ---------------------------------------------------------------------------- 77
L77 = lesson(
    "First, second, third: floors and ordinals",
    "الطَّابِق الْأَوَّل · الْغُرْفَة الثَّانِيَة",
    requires=["أول", "ثاني", "ثالث", "رابع", "خامس", "طابق"],
    cards=[
        card("Ordinal numbers",
             "“First”, “second” and so on are adjectives. They follow the noun, take ال if the noun does, and agree in "
             "gender. The first is irregular; the others add ة for the feminine as usual.",
             tables=[table(["English", "Masculine", "Feminine"],
                           [["first", "الْأَوَّل", "الْأُولَى"], ["second", "الثَّانِي", "الثَّانِيَة"],
                            ["third", "الثَّالِث", "الثَّالِثَة"], ["fourth", "الرَّابِع", "الرَّابِعَة"],
                            ["fifth", "الْخَامِس", "الْخَامِسَة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Floors",
             "Floors are masculine (الطَّابِق). The ground floor is الطَّابِق الْأَرْضِيّ; أَرْضِيّ is an adjective made from أَرْض, “ground”.",
             examples=[
                 ex("أَسْكُن فِي الطَّابِق الثَّالِث.", "I live on the third floor.", "الثَّالِث"),
                 ex("الْمَطْبَخ فِي الطَّابِق الْأَرْضِيّ.", "The kitchen is on the ground floor."),
                 ex("غُرْفَة النَّوْم فِي الطَّابِق الْأَوَّل.", "The bedroom is on the first floor (one floor above the ground floor).", "الْأَوَّل"),
                 ex("الْغُرْفَة الثَّانِيَة كَبِيرَة.", "The second room is big.", "الثَّانِيَة"),
                 ex("الدَّرْس الْأَوَّل سَهْل وَالدَّرْس الثَّانِي صَعْب.", "The first lesson is easy and the second lesson is hard."),
             ]),
    ],
    exercises=[
        M("Which means “the second floor”?", "الطَّابِق الثَّانِي", ["الطَّابِق الثَّانِيَة", "طَابِق الثَّانِي", "الثَّانِي الطَّابِق"], "طَابِق is masculine."),
        M("Which means “the third room”?", "الْغُرْفَة الثَّالِثَة", ["الْغُرْفَة الثَّالِث", "غُرْفَة الثَّالِثَة", "الثَّالِثَة الْغُرْفَة"], "غُرْفَة is feminine."),
        M("Which means “the first lesson”?", "الدَّرْس الْأَوَّل", ["الدَّرْس الْأُولَى", "دَرْس الْأَوَّل", "الْأَوَّل الدَّرْس"], "دَرْس is masculine."),
        M("Which means “the first room”?", "الْغُرْفَة الْأُولَى", ["الْغُرْفَة الْأَوَّل", "الْغُرْفَة الْأَوَّلَة", "غُرْفَة الْأُولَى"], "The feminine of الْأَوَّل is irregular."),
        M("Which means “the ground floor”?", "الطَّابِق الْأَرْضِيّ", ["الطَّابِق الْأَوَّل", "الْأَرْض الطَّابِق", "الطَّابِق الْخَامِس"], "الْأَرْضِيّ = of the earth."),
        M("Which means “fourth” (masculine)?", "الرَّابِع", ["الثَّالِث", "الْخَامِس", "الثَّانِي"], "الرَّابِع = fourth."),
        M("Which means “fifth” (feminine)?", "الْخَامِسَة", ["الْخَامِس", "الرَّابِعَة", "الْأُولَى"], "الْخَامِسَة = fifth (f)."),
        F("أَسْكُن فِي الطَّابِق ___.", "الثَّالِث", ["الثَّالِثَة", "ثَلَاثَة", "ثَلَاث"], "طَابِق is masculine.", tr="I live on the third floor."),
        F("الْغُرْفَة ___ كَبِيرَة.", "الثَّانِيَة", ["الثَّانِي", "اِثْنَان", "اِثْنَتَان"], "غُرْفَة is feminine.", tr="The second room is big."),
    ],
    verify=(vf("الثَّانِي", "الثَّانِيَة") + vf("الثَّالِث", "الثَّالِثَة") + vf("الرَّابِع", "الرَّابِعَة") + vf("الْخَامِس", "الْخَامِسَة")
            + vw("الْأَوَّل", "الْأُولَى", "الْأَرْضِيّ")),
)

# ---------------------------------------------------------------------------- 78
L78 = lesson(
    "Reading a property ad",
    "شَقَّة لِلْإِيجَار · بَيْت لِلْبَيْع",
    requires=["شقة", "غرفة", "طابق", "بيع", "إيجار"],
    cards=[
        card("Words used in ads",
             "Property ads are short and use much of the vocabulary of this unit.",
             tables=[table(["English", "Arabic"],
                           [["for rent", "لِلْإِيجَار"], ["for sale", "لِلْبَيْع"], ["near", "قَرِيب مِنْ"],
                            ["ground floor", "الطَّابِق الْأَرْضِيّ"], ["new", "جَدِيد"], ["clean", "نَظِيف"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Two ads",
             "Read each line. The word قَرِيب or قَرِيبَة (“near”) agrees with the thing advertised: شَقَّة is "
             "feminine and بَيْت is masculine.",
             examples=[
                 ex("شَقَّة لِلْإِيجَار فِي الطَّابِق الثَّالِث.", "Apartment for rent on the third floor."),
                 ex("ثَلَاث غُرَف وَمَطْبَخ وَحَمَّامَان.", "Three rooms, a kitchen and two bathrooms."),
                 ex("قَرِيبَة مِنَ الْجَامِعَة.", "Near the university."),
                 ex("بَيْت لِلْبَيْع.", "House for sale."),
                 ex("أَرْبَع غُرَف وَحَدِيقَة كَبِيرَة.", "Four rooms and a big garden."),
                 ex("قَرِيب مِنَ السُّوق وَالْمَسْجِد.", "Near the market and the mosque."),
             ]),
    ],
    exercises=[
        M("«شَقَّة لِلْإِيجَار فِي الطَّابِق الثَّالِث.» What is advertised?", "An apartment to rent on the third floor", ["A house for sale", "An apartment for sale on the third floor", "A room to rent on the first floor"], "لِلْإِيجَار = for rent."),
        M("«ثَلَاث غُرَف وَمَطْبَخ وَحَمَّامَان.» How many rooms are there?", "Three rooms", ["Two rooms", "Four rooms", "One room"], "ثَلَاث = three."),
        M("«ثَلَاث غُرَف وَمَطْبَخ وَحَمَّامَان.» How many bathrooms?", "Two", ["One", "Three", "Four"], "حَمَّامَان is the dual."),
        M("«بَيْت لِلْبَيْع. أَرْبَع غُرَف وَحَدِيقَة كَبِيرَة.» What does the house have?", "Four rooms and a big garden", ["Three rooms and a small garden", "A kitchen and a balcony", "Four bathrooms"], "أَرْبَع غُرَف وَحَدِيقَة كَبِيرَة."),
        M("Which word means “for rent”?", "لِلْإِيجَار", ["لِلْبَيْع", "قَرِيب", "جَدِيد"], "لِلْإِيجَار = for rent."),
        M("Which word means “for sale”?", "لِلْبَيْع", ["لِلْإِيجَار", "نَظِيف", "قَرِيب"], "لِلْبَيْع = for sale."),
        M("The ad says «قَرِيبَة مِنَ الْجَامِعَة». What is being advertised?", "A feminine thing, such as an apartment", ["A house", "A hotel", "An office"], "قَرِيبَة is feminine, like شَقَّة."),
        F("شَقَّة ___ فِي الطَّابِق الثَّانِي.", "لِلْإِيجَار", ["لِلْأَسَف", "لِلْجَامِعَة", "لِلْقَاهِرَة"], "An apartment to rent.", tr="Apartment for rent on the second floor."),
        F("بَيْت ___ قَرِيب مِنَ السُّوق.", "لِلْبَيْع", ["لِلْإِيجَار", "لِلْمَدْرَسَة", "لِلنَّوْم"], "A house for sale.", tr="A house for sale near the market."),
    ],
    verify=vw("لِلْإِيجَار", "لِلْبَيْع", "الْأَرْضِيّ", "قَرِيبَة", "حَمَّامَان") + vn(3, "f", "ثَلَاث") + vn(4, "f", "أَرْبَع") + vpb("غُرْفَة", "غُرَف"),
)

# ---------------------------------------------------------------------------- 79
L79 = lesson(
    "Review: a visit to a new home",
    "Welcome, rooms, numbers",
    requires=["دعوة", "غرفة", "طابق", "ثاني", "كم", "بيت"],
    cards=[
        card("Khalid welcomes Sara",
             "Khalid has invited Sara to see his home. Read the conversation, then answer the questions.",
             examples=[
                 ex("تَفَضَّلِي يَا سَارَة. أَهْلًا بِكِ فِي بَيْتِي.", "Khalid: Please come in, Sara. Welcome to my home."),
                 ex("شُكْرًا عَلَى الدَّعْوَة. الْبَيْت جَمِيل!", "Sara: Thank you for the invitation. The house is beautiful!"),
                 ex("هَذَا هُوَ الصَّالُون. فِي الصَّالُون أَرِيكَة وَطَاوِلَتَان وَتِلْفَاز.", "Khalid: This is the living room. In the living room there is a sofa, two tables and a television."),
                 ex("كَمْ غُرْفَة فِي الْبَيْت؟", "Sara: How many rooms are there in the house?"),
                 ex("فِي الْبَيْت أَرْبَع غُرَف وَحَمَّامَان وَمَطْبَخ وَاحِد.", "Khalid: There are four rooms, two bathrooms and one kitchen."),
                 ex("وَأَيْنَ غُرْفَة النَّوْم؟", "Sara: And where is the bedroom?"),
                 ex("فِي الطَّابِق الثَّانِي. أَسْكُن هُنَا مُنْذُ سَنَتَيْن.", "Khalid: On the second floor. I have lived here for two years."),
             ]),
    ],
    exercises=[
        M("Khalid says تَفَضَّلِي to Sara. What does it mean?", "Please come in (to a woman)", ["Goodbye (to a woman)", "Thank you (to a woman)", "I am busy (to a woman)"], "تَفَضَّلِي = please, to a woman."),
        M("What is in the living room?", "A sofa, two tables and a television", ["A bed and a desk", "A sofa and a refrigerator", "Three tables"], "أَرِيكَة وَطَاوِلَتَان وَتِلْفَاز."),
        M("How many rooms are in the house?", "Four", ["Two", "Three", "Five"], "أَرْبَع غُرَف."),
        M("How many bathrooms?", "Two", ["One", "Three", "Four"], "حَمَّامَان is the dual."),
        M("Where is the bedroom?", "On the second floor", ["On the ground floor", "On the third floor", "In the garden"], "فِي الطَّابِق الثَّانِي."),
        M("How long has Khalid lived there?", "Two years", ["Two months", "Two days", "Ten years"], "مُنْذُ سَنَتَيْن."),
        M("Which means “two tables”?", "طَاوِلَتَان", ["طَاوِلَات", "طَاوِلَة", "طَاوِلَتُون"], "The dual of a feminine noun."),
        M("Which means “five rooms”?", "خَمْس غُرَف", ["خَمْسَة غُرَف", "خَمْس غُرْفَة", "خَمْسَة غُرْفَة"], "غُرْفَة is feminine."),
        M("Which means “the bedroom door”?", "بَاب غُرْفَة النَّوْم", ["الْبَاب غُرْفَة النَّوْم", "غُرْفَة النَّوْم الْبَاب", "بَاب الْغُرْفَة النَّوْم"], "Noun + noun + noun."),
        F("كَمْ ___ فِي الْبَيْت؟", "غُرْفَة", ["غُرَف", "غُرْفَتَان", "خَمْس"], "Singular noun after كَمْ.", tr="How many rooms are there in the house?"),
    ],
    verify=vd("طَاوِلَة", "طَاوِلَتَان", "طَاوِلَتَيْن") + vd("سَنَة", "سَنَتَان", "سَنَتَيْن") + vn(5, "f", "خَمْس") + vn(4, "f", "أَرْبَع"),
)

UNIT = unit("البيت والأرقام: the home, the dual and numbers", [L65, L66, L67, L68, L69, L70, L71, L72, L73, L74, L75, L76, L77, L78, L79])
