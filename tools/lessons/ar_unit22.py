"""Unit 22 (chapter 20): furniture, payment plans, delivery, returns, appliances, moving into an apartment, review of the unit."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 337
L337 = lesson(
    "Furniture and rooms",
    "أَثَاث · كُرْسِيّ · سَرِير · خِزَانَة · غُرْفَة النَّوْم",
    requires=["أثاث", "كرسي", "طاولة", "سرير", "خزانة", "مكتب", "خشب", "غرفة", "نوم", "جلوس"],
    cards=[
        card("Things in a room",
             "The word أَثَاث means “furniture” in general. For one piece, use the specific name. A bedroom is غُرْفَة النَّوْم (“the room of sleep”) and a living room is غُرْفَة الْجُلُوس (“the room of sitting”).",
             tables=[table(["English", "Arabic"],
                           [["furniture", "أَثَاث"], ["chair", "كُرْسِيّ"], ["table", "طَاوِلَة"], ["bed", "سَرِير"], ["wardrobe, cupboard", "خِزَانَة"], ["sofa", "أَرِيكَة"], ["desk", "مَكْتَب"], ["carpet", "سَجَّادَة"], ["wood", "خَشَب"],
                            ["bedroom", "غُرْفَة النَّوْم"], ["living room", "غُرْفَة الْجُلُوس"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What is in the room",
             "Use فِي + the room, then the things that are there.",
             examples=[
                 ex("فِي غُرْفَة النَّوْم سَرِير وَخِزَانَة.", "In the bedroom there is a bed and a wardrobe.", "غُرْفَة النَّوْم"),
                 ex("فِي غُرْفَة الْجُلُوس أَرِيكَة وَطَاوِلَة صَغِيرَة.", "In the living room there is a sofa and a small table.", "غُرْفَة الْجُلُوس"),
                 ex("الْمَكْتَب مِنَ الْخَشَب.", "The desk is made of wood.", "الْخَشَب"),
                 ex("أَجْلِس عَلَى الْكُرْسِيّ.", "I sit on the chair.", "الْكُرْسِيّ"),
                 ex("عَلَى الْأَرْض سَجَّادَة جَمِيلَة.", "On the floor there is a beautiful carpet.", "سَجَّادَة"),
             ]),
    ],
    exercises=[
        M("What does سَرِير mean?", "bed", ["chair", "desk", "carpet"], "سَرِير = bed."),
        M("What does خِزَانَة mean?", "wardrobe, cupboard", ["sofa", "table", "wood"], "خِزَانَة = cupboard."),
        M("Which word means “sofa”?", "أَرِيكَة", ["سَجَّادَة", "مَكْتَب", "كُرْسِيّ"], "أَرِيكَة = sofa."),
        M("What is غُرْفَة النَّوْم?", "the bedroom", ["the kitchen", "the living room", "the bathroom"], "نَوْم = sleep."),
        M("What does الْمَكْتَب مِنَ الْخَشَب mean?", "The desk is made of wood", ["The desk is made of leather", "The desk is in the kitchen", "The desk is cheap"], "خَشَب = wood."),
        M("What does أَثَاث mean?", "furniture", ["clothes", "food", "rooms"], "أَثَاث = furniture."),
        F("فِي غُرْفَة ___ سَرِير وَخِزَانَة.", "النَّوْم", ["الْجُلُوس", "الطَّعَام"], "The room with a bed is the bedroom.", tr="In the bedroom there is a bed and a wardrobe."),
        F("فِي غُرْفَة الْجُلُوس ___ وَطَاوِلَة صَغِيرَة.", "أَرِيكَة", ["سَرِير", "خِزَانَة"], "A living room has a sofa.", tr="In the living room there is a sofa and a small table."),
        F("أَجْلِس عَلَى ___", "الْكُرْسِيّ", ["الْخَشَب", "السِّعْر"], "You sit on a chair.", tr="I sit on the chair."),
    ],
    verify=vw("أَثَاث", "كُرْسِيّ", "الْكُرْسِيّ", "طَاوِلَة", "سَرِير", "خِزَانَة", "أَرِيكَة", "مَكْتَب", "الْمَكْتَب", "سَجَّادَة", "خَشَب", "الْخَشَب", "غُرْفَة", "النَّوْم", "الْجُلُوس", "الطَّعَام", "السِّعْر", "الْأَرْض", "أَجْلِس", "جَمِيلَة"),
)

# ---------------------------------------------------------------------------- 338
L338 = lesson(
    "Describing furniture",
    "مُرِيح · جَدِيد · قَدِيم · عَالِي الْجَوْدَة",
    requires=["مريح", "جديد", "قديم", "حديث", "جودة", "كرسي", "خشب", "كبير", "صغير", "أكثر"],
    cards=[
        card("Quality and comfort",
             "Use مُرِيح for “comfortable” and عَالِي الْجَوْدَة for “of high quality”. For non-human plurals, the adjective is feminine singular. "
             "So كُرْسِيّ مُرِيح is “a comfortable chair”, but كَرَاسِي مُرِيحَة is “comfortable chairs”. To compare, use أَغْلَى مِنْ (“more expensive than”) or أَرْخَص مِنْ (“cheaper than”).",
             tables=[table(["Singular", "Plural"],
                           [["كُرْسِيّ مُرِيح", "كَرَاسِي مُرِيحَة"], ["سَرِير كَبِير", "أَسِرَّة كَبِيرَة"], ["مَكْتَب جَدِيد", "مَكَاتِب جَدِيدَة"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("In a showroom",
             "These are typical phrases.",
             examples=[
                 ex("أُرِيد سَرِير مُرِيح وَكَبِير.", "I want a comfortable, big bed.", "مُرِيح"),
                 ex("عِنْدَنَا كَرَاسِي مُرِيحَة مِنَ الْخَشَب.", "We have comfortable wooden chairs.", "كَرَاسِي مُرِيحَة"),
                 ex("هَذَا الْأَثَاث عَالِي الْجَوْدَة.", "This furniture is of high quality.", "عَالِي الْجَوْدَة"),
                 ex("الْكُرْسِيّ الْجَدِيد أَغْلَى مِنَ الْكُرْسِيّ الْقَدِيم.", "The new chair is more expensive than the old chair.", "أَغْلَى"),
                 ex("الْأَرِيكَة الصَّغِيرَة أَرْخَص مِنَ الْأَرِيكَة الْكَبِيرَة.", "The small sofa is cheaper than the large sofa.", "أَرْخَص"),
             ]),
    ],
    exercises=[
        M("What does مُرِيح mean?", "comfortable", ["expensive", "wooden", "small"], "مُرِيح = comfortable."),
        M("What does عَالِي الْجَوْدَة mean?", "of high quality", ["very cheap", "very small", "free of charge"], "جَوْدَة = quality."),
        M("Which is correct for “comfortable chairs”?", "كَرَاسِي مُرِيحَة", ["كَرَاسِي مُرِيحُون", "كَرَاسِي مُرِيح"], "Things in the plural take a feminine singular adjective."),
        M("What does عِنْدَنَا كَرَاسِي مُرِيحَة مِنَ الْخَشَب mean?", "We have comfortable wooden chairs", ["I sit on a wooden chair", "We sell wood", "Our chairs are old"], "عِنْدَنَا = we have."),
        M("What does الْكُرْسِيّ الْجَدِيد أَغْلَى مِنَ الْكُرْسِيّ الْقَدِيم suggest?", "the new chair costs more", ["the old chair costs more", "they cost the same", "the chair is free"], "أَغْلَى مِنْ = more expensive than."),
        M("Which sofa is cheaper in the lesson?", "the small sofa", ["the large sofa", "the old sofa", "the wooden sofa"], "الصَّغِيرَة أَرْخَص."),
        F("أُرِيد سَرِير ___ وَكَبِير.", "مُرِيح", ["مُرِيحَة", "مُرِيحُون"], "سَرِير is masculine singular.", tr="I want a comfortable, big bed."),
        F("عِنْدَنَا كَرَاسِي ___", "مُرِيحَة", ["مُرِيح", "مُرِيحُونَ"], "Plural things: feminine singular adjective.", tr="We have comfortable chairs."),
        F("هَذَا الْأَثَاث عَالِي ___", "الْجَوْدَة", ["الْخَشَب", "الْغُرْفَة"], "Quality.", tr="This furniture is of high quality."),
    ],
    verify=vw("مُرِيح", "مُرِيحَة", "جَدِيد", "جَدِيدَة", "قَدِيم", "الْقَدِيم", "الْحَدِيث", "عَالِي", "الْجَوْدَة", "كَرَاسِي", "أَسِرَّة", "أَجْهِزَة", "كَبِيرَة", "عِنْدَنَا", "أَغْلَى", "أَرْخَص", "الْأَرِيكَة", "الصَّغِيرَة", "الْكَبِيرَة", "الْخَشَب", "الْغُرْفَة", "مُرِيحُون", "مُرِيحُونَ"),
)

# ---------------------------------------------------------------------------- 339
L339 = lesson(
    "In the furniture showroom",
    "نَحْتَاج إِلَى أَثَاث لِلشَّقَّة",
    requires=["شقة", "غرفة", "أثاث", "ثمن", "كم", "نعم", "كثير"],
    cards=[
        card("A dialogue (invented)",
             "A couple moving into an apartment talk with a salesman. Read the lines in order. The verb نَحْتَاج إِلَى means “we need” and is followed by إِلَى.",
             examples=[
                 ex("مَرْحَبًا، أَيّ خِدْمَة؟", "Welcome, how can I help?", "أَيّ خِدْمَة"),
                 ex("نَحْتَاج إِلَى أَثَاث لِلشَّقَّة.", "We need furniture for the apartment.", "نَحْتَاج إِلَى"),
                 ex("عِنْدَنَا أَصْنَاف كَثِيرَة. هَلْ تُحِبُّونَ الْأَثَاث الْحَدِيث؟", "We have many kinds. Do you like modern furniture?", "تُحِبُّونَ"),
                 ex("نَعَمْ، لَكِنَّنَا لَا نُرِيد أَنْ نَدْفَع كَثِيرًا.", "Yes, but we do not want to pay a lot.", "لَا نُرِيد"),
                 ex("هَذَا السَّرِير رَخِيص وَمُرِيح.", "This bed is cheap and comfortable.", "رَخِيص"),
                 ex("كَمْ ثَمَنُهُ؟", "How much is it?", "كَمْ ثَمَنُهُ"),
             ]),
        card("Useful pieces",
             "Ask for what you need with نَحْتَاج إِلَى or أُرِيد, say what you do not want with لَا نُرِيد, and ask the price with كَمْ.",
             tables=[table(["English", "Arabic"],
                           [["we need", "نَحْتَاج إِلَى"], ["we want", "نُرِيد"], ["we do not want", "لَا نُرِيد"], ["for the apartment", "لِلشَّقَّة"], ["cheap and comfortable", "رَخِيص وَمُرِيح"]],
                           say=[1], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("What does نَحْتَاج إِلَى أَثَاث لِلشَّقَّة mean?", "We need furniture for the apartment", ["We sell furniture in the apartment", "I like the apartment", "The furniture is free"], "نَحْتَاج إِلَى = we need."),
        M("What does هَلْ تُحِبُّونَ الْأَثَاث الْحَدِيث؟ ask?", "Do you like modern furniture?", ["Is the furniture old?", "Where is the furniture?", "How much is the furniture?"], "تُحِبُّونَ = you (pl.) like."),
        M("What does لَا نُرِيد أَنْ نَدْفَع كَثِيرًا mean?", "We do not want to pay a lot", ["We want to pay a lot", "We did not pay yesterday", "We will pay in cash"], "لَا نُرِيد = we do not want."),
        M("What does the salesman say about the bed?", "it is cheap and comfortable", ["it is old and big", "it is red", "it is free"], "رَخِيص وَمُرِيح."),
        M("What does كَمْ ثَمَنُهُ؟ ask?", "How much is it?", ["Where is it?", "Who is it?", "When does it arrive?"], "ثَمَن = price."),
        M("What does أَيّ خِدْمَة؟ mean here?", "How can I help?", ["Which price?", "Which room?", "Any bed?"], "The salesman's opening line."),
        F("___ إِلَى أَثَاث لِلشَّقَّة.", "نَحْتَاج", ["أَحْتَاج", "يَحْتَاجُونَ"], "“We need”: نَحْتَاج.", tr="We need furniture for the apartment."),
        F("لَا ___ أَنْ نَدْفَع كَثِيرًا.", "نُرِيد", ["أُرِيد", "يُرِيدُونَ"], "“We do not want”.", tr="We do not want to pay a lot."),
        F("هَلْ ___ الْأَثَاث الْحَدِيث؟", "تُحِبُّونَ", ["أُحِبّ", "تُحِبِّينَ"], "The salesman speaks to the couple (plural).", tr="Do you (both) like modern furniture?"),
    ],
    verify=vw("أَيّ", "خِدْمَة", "نَحْتَاج", "أَحْتَاج", "يَحْتَاجُونَ", "إِلَى", "أَثَاث", "لِلشَّقَّة", "مَرْحَبًا", "عِنْدَنَا", "أَصْنَاف", "كَثِيرَة", "تُحِبُّونَ", "الْحَدِيث", "لَكِنَّنَا", "نُرِيد", "نَدْفَع", "كَثِيرًا", "رَخِيص", "وَمُرِيح", "السَّرِير", "الشَّقَّة", "يُرِيدُونَ", "تُحِبِّينَ", "أُحِبّ", "أُرِيد", "ثَمَنُهُ"),
)

# ---------------------------------------------------------------------------- 340
L340 = lesson(
    "Payment plans",
    "دُفْعَة أُولَى · أَقْسَاط شَهْرِيَّة · بِدُون فَوَائِد",
    requires=["دفعة", "فائدة", "شيك", "نقد", "بطاقة", "شهر", "سنة", "كل", "أول", "دفع"],
    cards=[
        card("Ways to pay",
             "A store may let you pay all at once or in parts. A part is قِسْط, and the plural is أَقْسَاط. The first payment is الدُّفْعَة الْأُولَى. Interest is فَائِدَة (plural فَوَائِد). A cheque is شِيك. "
             "The sentences below describe an invented store; real stores have their own rules.",
             tables=[table(["English", "Arabic"],
                           [["payment", "دُفْعَة"], ["the first payment", "الدُّفْعَة الْأُولَى"], ["instalment", "قِسْط"], ["instalments", "أَقْسَاط"], ["monthly", "شَهْرِيّ"], ["interest", "فَائِدَة"], ["interest charges", "فَوَائِد"], ["cheque", "شِيك"], ["cash", "نَقْدًا"], ["by card", "بِالْبِطَاقَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Choosing a plan (invented)",
             "A customer asks, and the clerk answers.",
             examples=[
                 ex("هَلْ يُمْكِن أَنْ أَدْفَع عَلَى أَقْسَاط؟", "May I pay in instalments?", "أَقْسَاط"),
                 ex("نَعَمْ، الدُّفْعَة الْأُولَى عِشْرُون بِالْمِئَة.", "Yes, the first payment is twenty per cent.", "الدُّفْعَة الْأُولَى"),
                 ex("وَتَدْفَع قِسْطًا كُلّ شَهْر.", "And you pay an instalment every month.", "كُلّ شَهْر"),
                 ex("هَلْ هُنَاكَ فَوَائِد؟", "Are there any interest charges?", "فَوَائِد"),
                 ex("لَا، بِدُون فَوَائِد.", "No, without interest.", "بِدُون فَوَائِد"),
                 ex("يُمْكِنُكَ أَنْ تَدْفَع نَقْدًا أَوْ بِشِيك.", "You can pay in cash or by cheque.", "بِشِيك"),
             ]),
    ],
    exercises=[
        M("What is a قِسْط?", "an instalment", ["a cheque", "a price", "a shop"], "قِسْط = instalment."),
        M("What does الدُّفْعَة الْأُولَى mean?", "the first payment", ["the last payment", "the monthly payment", "the cheque"], "أُولَى = first (f.)."),
        M("What does بِدُون فَوَائِد mean?", "without interest", ["with a discount", "with a card", "without payment"], "بِدُون = without."),
        M("What does هَلْ يُمْكِن أَنْ أَدْفَع عَلَى أَقْسَاط؟ ask?", "May I pay in instalments?", ["May I return this?", "May I try this on?", "May I pay tomorrow?"], "عَلَى أَقْسَاط = in instalments."),
        M("What does كُلّ شَهْر mean?", "every month", ["every day", "every year", "last month"], "شَهْر = month."),
        M("What is a شِيك?", "a cheque", ["a bill", "a bag", "a bed"], "شِيك = cheque."),
        F("هَلْ يُمْكِن أَنْ أَدْفَع عَلَى ___؟", "أَقْسَاط", ["سَرِير", "خَشَب"], "Pay in instalments.", tr="May I pay in instalments?"),
        F("وَتَدْفَع قِسْطًا ___ شَهْر.", "كُلّ", ["بَعْض", "أَيّ"], "“Every month”.", tr="And you pay an instalment every month."),
        F("لَا، بِدُون ___", "فَوَائِد", ["أَقْسَاط", "كَرَاسِي"], "Without interest.", tr="No, without interest."),
    ],
    verify=vw("دُفْعَة", "الدُّفْعَة", "الْأُولَى", "قِسْط", "قِسْطًا", "أَقْسَاط", "شَهْرِيّ", "فَائِدَة", "فَوَائِد", "شِيك", "بِشِيك", "نَقْدًا", "بِالْبِطَاقَة", "أَدْفَع", "تَدْفَع", "عِشْرُون", "بِالْمِئَة", "كُلّ", "شَهْر", "هُنَاكَ", "يُمْكِنُكَ", "يُمْكِن", "بِدُون", "أَوْ", "سَرِير", "خَشَب", "بَعْض", "كَرَاسِي"),
)

# ---------------------------------------------------------------------------- 341
L341 = lesson(
    "Arranging delivery",
    "يَصِل الْأَثَاث يَوْم الْأَحَد · لَا تَنْسَ الْعُنْوَان",
    requires=["وصل", "توصيل", "مجاني", "عنوان", "أحد", "يوم", "بيت", "أثاث", "جهاز"],
    cards=[
        card("When will it arrive?",
             "Delivery is تَوْصِيل, and free is مَجَّانِيّ. The verb وَصَلَ is an assimilated verb: past وَصَلَ, present يَصِل, imperative صِلْ. "
             "Remember the rule from chapter 16: when the subject is a plural thing, the verb is feminine singular, as in وَصَلَتِ الْأَجْهِزَة, “the appliances arrived”.",
             tables=[table(["Form", "Arabic", "English"],
                           [["past (he)", "وَصَلَ", "he arrived"], ["past (she)", "وَصَلَتْ", "she arrived"], ["present (he)", "يَصِل", "he arrives"], ["present (she)", "تَصِل", "she arrives"], ["future (it, m.)", "سَيَصِل", "it will arrive"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Talking to the store",
             "Notice the negative command لَا تَنْسَ, “do not forget”, from the defective verb نَسِيَ.",
             examples=[
                 ex("هَلِ التَّوْصِيل مَجَّانِيّ؟", "Is delivery free?", "التَّوْصِيل"),
                 ex("نَعَمْ، سَيَصِل الْأَثَاث يَوْم الْأَحَد.", "Yes, the furniture will arrive on Sunday.", "سَيَصِل"),
                 ex("وَصَلَتِ الْأَجْهِزَة الْجَدِيدَة أَمْسِ.", "The new appliances arrived yesterday.", "وَصَلَتِ"),
                 ex("لَا تَنْسَ الْعُنْوَان.", "Do not forget the address.", "لَا تَنْسَ"),
                 ex("سَأَكُون فِي الْبَيْت صَبَاحًا.", "I will be at home in the morning.", "سَأَكُون"),
             ]),
    ],
    exercises=[
        M("What does تَوْصِيل mean?", "delivery", ["payment", "warranty", "price"], "تَوْصِيل = delivery."),
        M("What does مَجَّانِيّ mean?", "free of charge", ["expensive", "monthly", "old"], "مَجَّانِيّ = free."),
        M("What does سَيَصِل الْأَثَاث يَوْم الْأَحَد mean?", "The furniture will arrive on Sunday", ["The furniture arrived on Sunday", "The furniture is free on Sunday", "I want furniture on Sunday"], "سَيَصِل = will arrive."),
        M("What does وَصَلَتِ الْأَجْهِزَة الْجَدِيدَة أَمْسِ mean?", "The new appliances arrived yesterday", ["The new appliances will arrive tomorrow", "The old appliances left", "The appliances are free"], "Past: وَصَلَتِ."),
        M("What does لَا تَنْسَ الْعُنْوَان mean?", "Do not forget the address", ["I forgot the address", "Write the address", "Where is the address?"], "لَا تَنْسَ = do not forget."),
        M("Why is the verb وَصَلَتِ feminine?", "the subject is a plural thing", ["the appliances are female", "the verb is in the future", "the sentence is a question"], "Plural things take feminine singular."),
        F("نَعَمْ، ___ الْأَثَاث يَوْم الْأَحَد.", "سَيَصِل", ["وَصَلَتْ", "صِلْ"], "Future, masculine: سَيَصِل.", tr="Yes, the furniture will arrive on Sunday.", lemma="وصل:fut:huwa"),
        F("___ الْأَجْهِزَة الْجَدِيدَة أَمْسِ.", "وَصَلَتِ", ["وَصَلَ", "وَصَلُوا"], "Plural things: feminine singular verb.", tr="The new appliances arrived yesterday."),
        F("لَا ___ الْعُنْوَان.", "تَنْسَ", ["نَسِيتُ", "نَسِيَ"], "After لَا (command), the shortened form: تَنْسَ.", tr="Do not forget the address."),
    ],
    verify=(vv("وصل", "past", huwa="وَصَلَ", hiya="وَصَلَتْ") + vv("وصل", "pres", huwa="يَصِل", hiya="تَصِل") + vv("وصل", "fut", huwa="سَيَصِل")
            + vw("تَوْصِيل", "التَّوْصِيل", "مَجَّانِيّ", "الْأَثَاث", "الْأَحَد", "الْأَجْهِزَة", "الْجَدِيدَة", "أَمْسِ", "الْعُنْوَان", "سَأَكُون", "صَبَاحًا", "وَصَلَتِ", "وَصَلُوا", "صِلْ", "تَنْسَى", "نَسِيَ", "تَنْسَ")),
)


# ---------------------------------------------------------------------------- 342
L342 = lesson(
    "Returns, receipts and warranties",
    "اِحْتَفِظْ بِالْفَاتُورَة · الْكَفَالَة ثَلَاث سَنَوَات",
    requires=["فاتورة", "كفالة", "ضمان", "عيب", "إصلاح", "خلال", "سنة", "يوم", "شمل", "رد"],
    cards=[
        card("Words of the store's rules",
             "A receipt is فَاتُورَة. A warranty is كَفَالَة; ضَمَان means “guarantee”. A defect is عَيْب, and repair is إِصْلَاح. The verb رَدَّ يَرُدّ means “to return (something)”; its noun رَدّ means “returning”. "
             "Each store has its own rules, and the examples below describe an invented store.",
             tables=[table(["English", "Arabic"],
                           [["receipt, invoice", "فَاتُورَة"], ["warranty", "كَفَالَة"], ["guarantee", "ضَمَان"], ["defect", "عَيْب"], ["repair", "إِصْلَاح"], ["within", "خِلَال"], ["one year", "سَنَة"], ["two years", "سَنَتَيْن"], ["three years", "ثَلَاث سَنَوَات"], ["seven days", "سَبْعَة أَيَّام"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("The rules (invented)",
             "Notice the passive لَا يُقْبَل, “is not accepted”, and the double-letter verb تَرُدَّ, “you return”, after أَنْ.",
             examples=[
                 ex("يُمْكِنُكَ أَنْ تَرُدَّ الْجِهَاز خِلَال سَبْعَة أَيَّام.", "You may return the appliance within seven days.", "تَرُدَّ"),
                 ex("لَا يُقْبَل رَدّ الْجِهَاز بِدُون فَاتُورَة.", "Returning the appliance is not accepted without a receipt.", "لَا يُقْبَل"),
                 ex("اِحْتَفِظْ بِالْفَاتُورَة.", "Keep the receipt.", "اِحْتَفِظْ"),
                 ex("الْكَفَالَة ثَلَاث سَنَوَات.", "The warranty is three years.", "ثَلَاث سَنَوَات"),
                 ex("تَشْمَل الْكَفَالَة الْإِصْلَاح الْمَجَّانِيّ.", "The warranty covers free repair.", "تَشْمَل"),
             ]),
    ],
    exercises=[
        M("What is a فَاتُورَة?", "a receipt", ["a warranty", "a price", "a bed"], "فَاتُورَة = receipt, invoice."),
        M("What does كَفَالَة mean?", "warranty", ["delivery", "discount", "colour"], "كَفَالَة = warranty."),
        M("What does عَيْب mean?", "defect", ["repair", "receipt", "credit"], "عَيْب = defect."),
        M("What does اِحْتَفِظْ بِالْفَاتُورَة mean?", "Keep the receipt", ["Lose the receipt", "Pay the receipt", "Write the receipt"], "اِحْتَفِظْ = keep (command)."),
        M("What does لَا يُقْبَل رَدّ الْجِهَاز بِدُون فَاتُورَة mean?", "Returning the appliance is not accepted without a receipt", ["The appliance is free without a receipt", "The receipt is not accepted", "Receipts are returned"], "لَا يُقْبَل = is not accepted."),
        M("What does الْكَفَالَة ثَلَاث سَنَوَات mean?", "The warranty is three years", ["The warranty is three months", "The warranty is three days", "The warranty is free"], "سَنَوَات = years."),
        F("يُمْكِنُكَ أَنْ ___ الْجِهَاز خِلَال سَبْعَة أَيَّام.", "تَرُدَّ", ["رَدَدْتُ", "رَدّ"], "After أَنْ, a present form with أَنْتَ: تَرُدَّ.", tr="You may return the appliance within seven days.", lemma="ردد:sub:anta"),
        F("لَا ___ رَدّ الْجِهَاز بِدُون فَاتُورَة.", "يُقْبَل", ["مَقْبُول", "قَبِلَ"], "Passive: يُقْبَل.", tr="Returning the appliance is not accepted without a receipt.", lemma="قبل:ppres:huwa"),
        F("تَشْمَل الْكَفَالَة ___ الْمَجَّانِيّ.", "الْإِصْلَاح", ["الْفَاتُورَة", "السَّجَّادَة"], "A warranty can cover repair.", tr="The warranty covers free repair."),
    ],
    verify=(vv("ردد", "sub", anta="تَرُدَّ") + vv("قبل", "ppres", huwa="يُقْبَل") + vv("شمل", "pres", hiya="تَشْمَل")
            + vw("فَاتُورَة", "بِالْفَاتُورَة", "كَفَالَة", "الْكَفَالَة", "ضَمَان", "عَيْب", "إِصْلَاح", "الْإِصْلَاح", "خِلَال", "سَنَة", "سَنَتَيْن", "ثَلَاث", "سَنَوَات", "سَبْعَة", "أَيَّام", "الْجِهَاز", "الْمَجَّانِيّ", "اِحْتَفِظْ", "رَدّ", "يَقْبَل", "قَبِلَ", "رَدَدْتُ", "الْفَاتُورَة", "السَّجَّادَة", "يُمْكِنُكَ", "بِدُون")),
)

# ---------------------------------------------------------------------------- 343
L343 = lesson(
    "Household appliances",
    "ثَلَّاجَة · غَسَّالَة · فُرْن · مُكَيِّف · تِلْفَاز",
    requires=["جهاز", "كهربائي", "ثلاجة", "غسل", "فرن", "هواء", "تلفزيون", "حفظ", "برد", "طعام"],
    cards=[
        card("Appliances",
             "An electrical appliance is جِهَاز كَهْرَبَائِيّ, and the plural is أَجْهِزَة كَهْرَبَائِيَّة. Each appliance does a job, and the jobs are verbs you know.",
             tables=[table(["English", "Arabic", "What it does"],
                           [["refrigerator", "ثَلَّاجَة", "تَحْفَظ الطَّعَام"], ["washing machine", "غَسَّالَة", "تَغْسِل الثِّيَاب"], ["oven", "فُرْن", "يَطْبُخ الطَّعَام"], ["air conditioner", "مُكَيِّف", "يُبَرِّد الْغُرْفَة"], ["television", "تِلْفَاز", "يَعْرِض الْأَخْبَار"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("What each one does",
             "The refrigerator is feminine, so its verb has تَـ. The air conditioner is masculine, so its verb has يَـ.",
             examples=[
                 ex("الثَّلَّاجَة تَحْفَظ الطَّعَام.", "The refrigerator keeps the food.", "تَحْفَظ"),
                 ex("الْغَسَّالَة تَغْسِل الثِّيَاب.", "The washing machine washes the clothes.", "تَغْسِل"),
                 ex("الْمُكَيِّف يُبَرِّد الْغُرْفَة.", "The air conditioner cools the room.", "يُبَرِّد"),
                 ex("الْفُرْن يَطْبُخ الطَّعَام.", "The oven cooks the food.", "يَطْبُخ"),
                 ex("نُرِيد جِهَازًا كَهْرَبَائِيًّا جَدِيدًا.", "We want a new electrical appliance.", "جِهَازًا"),
             ]),
    ],
    exercises=[
        M("What is a ثَلَّاجَة?", "a refrigerator", ["an oven", "a television", "a carpet"], "ثَلَّاجَة = refrigerator."),
        M("What does a غَسَّالَة do?", "washes clothes", ["keeps food cold", "cools the room", "cooks food"], "تَغْسِل الثِّيَاب."),
        M("What does a مُكَيِّف do?", "cools the room", ["washes clothes", "cooks food", "shows the news"], "يُبَرِّد الْغُرْفَة."),
        M("Which word means “oven”?", "فُرْن", ["تِلْفَاز", "سَرِير", "خِزَانَة"], "فُرْن = oven."),
        M("What does جِهَاز كَهْرَبَائِيّ mean?", "an electrical appliance", ["a wooden table", "a school desk", "a coffee cup"], "كَهْرَبَائِيّ = electrical."),
        M("What is the plural of جِهَاز?", "أَجْهِزَة", ["جُهُود", "جَهَازَات"], "Broken plural."),
        F("الثَّلَّاجَة ___ الطَّعَام.", "تَحْفَظ", ["يَحْفَظ", "حَفِظْتُ"], "الثَّلَّاجَة is feminine.", tr="The refrigerator keeps the food.", lemma="حفظ:pres:hiya"),
        F("الْمُكَيِّف ___ الْغُرْفَة.", "يُبَرِّد", ["تُبَرِّد", "بَرَّدَ"], "الْمُكَيِّف is masculine.", tr="The air conditioner cools the room.", lemma="برد#2:pres:huwa"),
        F("الْغَسَّالَة ___ الثِّيَاب.", "تَغْسِل", ["يَغْسِل", "غَسَلْتُ"], "الْغَسَّالَة is feminine.", tr="The washing machine washes the clothes.", lemma="غسل:pres:hiya"),
    ],
    verify=(vv("حفظ", "pres", hiya="تَحْفَظ") + vv("غسل", "pres", hiya="تَغْسِل") + vv("برد#2", "pres", huwa="يُبَرِّد") + vv("طبخ", "pres", huwa="يَطْبُخ") + vpb("جهاز", "أَجْهِزَة")
            + vw("ثَلَّاجَة", "الثَّلَّاجَة", "غَسَّالَة", "الْغَسَّالَة", "فُرْن", "الْفُرْن", "مُكَيِّف", "الْمُكَيِّف", "تِلْفَاز", "جِهَاز", "جِهَازًا", "كَهْرَبَائِيّ", "كَهْرَبَائِيًّا", "كَهْرَبَائِيَّة", "أَجْهِزَة", "الطَّعَام", "الثِّيَاب", "الْغُرْفَة", "الْأَخْبَار", "يَعْرِض", "جَدِيدًا", "يَحْفَظ", "حَفِظْتُ", "تُبَرِّد", "بَرَّدَ", "يَغْسِل", "غَسَلْتُ", "جُهُود", "سَرِير", "خِزَانَة")),
)

# ---------------------------------------------------------------------------- 344
L344 = lesson(
    "Choosing an appliance by its features",
    "سَعَة · صَامِت · كَفَالَة ثَلَاث سَنَوَات",
    requires=["سعة", "طاقة", "صامت", "كفالة", "سنة", "جهاز", "ثلاجة", "غسل", "لون", "كبير"],
    cards=[
        card("Features and warranty",
             "Shoppers compare size (سَعَة, “capacity”), noise (صَامِت, “silent, quiet”) and warranty (كَفَالَة). A warranty is written as كَفَالَة + the length of time in the genitive: كَفَالَة سَنَة, كَفَالَة سَنَتَيْن, كَفَالَة ثَلَاث سَنَوَات. "
             "Imagine a shopper who wants appliances with a warranty of at least three years. These ads are invented.",
             tables=[table(["Appliance", "Feature", "Warranty"],
                           [["ثَلَّاجَة", "سَعَة كَبِيرَة", "كَفَالَة سَنَتَيْن"], ["غَسَّالَة", "صَامِتَة", "كَفَالَة ثَلَاث سَنَوَات"], ["فُرْن", "لَوْن أَبْيَض", "كَفَالَة سَنَة"], ["مُكَيِّف", "يُوَفِّر الطَّاقَة", "كَفَالَة خَمْس سَنَوَات"]],
                           say=[0, 1, 2], tlit=[0, 1, 2], gloss=False)]),
        card("Reading the ads",
             "Read each sentence and decide which appliance matches the shopper's rule.",
             examples=[
                 ex("الثَّلَّاجَة سَعَتُهَا كَبِيرَة وَكَفَالَتُهَا سَنَتَان.", "The refrigerator's capacity is large and its warranty is two years.", "سَعَتُهَا"),
                 ex("الْغَسَّالَة صَامِتَة وَكَفَالَتُهَا ثَلَاث سَنَوَات.", "The washing machine is quiet and its warranty is three years.", "صَامِتَة"),
                 ex("الْفُرْن أَبْيَض وَكَفَالَتُهُ سَنَة.", "The oven is white and its warranty is one year.", "كَفَالَتُهُ"),
                 ex("الْمُكَيِّف يُوَفِّر الطَّاقَة، وَكَفَالَتُهُ خَمْس سَنَوَات.", "The air conditioner saves energy, and its warranty is five years.", "يُوَفِّر"),
                 ex("أُرِيد أَجْهِزَة كَفَالَتُهَا ثَلَاث سَنَوَات عَلَى الْأَقَلّ.", "I want appliances whose warranty is at least three years.", "عَلَى الْأَقَلّ"),
             ]),
    ],
    exercises=[
        M("Which appliances have a warranty of at least three years?", "the washing machine and the air conditioner", ["the refrigerator and the oven", "the oven only", "all four"], "Three or more: غَسَّالَة (3) and مُكَيِّف (5)."),
        M("According to the ads, which appliance is quiet?", "the washing machine", ["the oven", "the refrigerator", "the air conditioner"], "صَامِتَة."),
        M("Which appliance has the shortest warranty?", "the oven", ["the refrigerator", "the washing machine", "the air conditioner"], "كَفَالَة سَنَة = one year."),
        M("What does سَعَة mean?", "capacity", ["noise", "warranty", "colour"], "سَعَة = capacity."),
        M("What does عَلَى الْأَقَلّ mean?", "at least", ["at most", "on the floor", "at no price"], "الْأَقَلّ = the least."),
        M("What does يُوَفِّر الطَّاقَة mean?", "saves energy", ["makes noise", "costs money", "washes clothes"], "وَفَّرَ = save."),
        F("كَفَالَة ثَلَاث ___", "سَنَوَات", ["سَنَة", "سَنَتَان"], "Numbers 3–10 take a plural noun.", tr="a warranty of three years"),
        F("الثَّلَّاجَة سَعَتُهَا ___ وَكَفَالَتُهَا سَنَتَان.", "كَبِيرَة", ["صَامِتَة", "أَبْيَض"], "Capacity is described as large.", tr="The refrigerator's capacity is large and its warranty is two years."),
        F("أُرِيد أَجْهِزَة كَفَالَتُهَا ثَلَاث سَنَوَات عَلَى ___", "الْأَقَلّ", ["الْأَكْثَر", "الْفَاتُورَة"], "At least.", tr="I want appliances whose warranty is at least three years."),
    ],
    verify=(vv("وفر#2", "pres", huwa="يُوَفِّر")
            + vw("سَعَة", "سَعَتُهَا", "صَامِت", "صَامِتَة", "كَفَالَة", "كَفَالَتُهَا", "كَفَالَتُهُ", "سَنَة", "سَنَتَان", "سَنَتَيْن", "ثَلَاث", "خَمْس", "سَنَوَات", "الطَّاقَة", "يُوَفِّر", "الْأَقَلّ", "الْأَكْثَر", "الْفَاتُورَة", "أَبْيَض", "ثَلَّاجَة", "غَسَّالَة", "فُرْن", "مُكَيِّف", "أَجْهِزَة", "لَوْن")),
)

# ---------------------------------------------------------------------------- 345
L345 = lesson(
    "Relative pronouns in store language",
    "الَّذِي · الَّتِي · الَّذِين · اللَّذَان",
    requires=["بائع", "زبون", "جهاز", "ثلاجة", "دفع", "حصل", "خصم", "وصل", "عمل", "هنا"],
    cards=[
        card("Review: who, which, that",
             "A relative pronoun links a clause to a definite noun and agrees with it. For a masculine singular noun: الَّذِي. For a feminine singular noun or a plural thing: الَّتِي. For people in the plural: الَّذِين. "
             "For two masculine persons: اللَّذَان.",
             tables=[table(["Noun", "Pronoun", "Example"],
                           [["masculine singular", "الَّذِي", "الزَّبُون الَّذِي دَفَعَ"], ["feminine singular", "الَّتِي", "الثَّلَّاجَة الَّتِي اِشْتَرَيْتُهَا"], ["plural things", "الَّتِي", "الْأَجْهِزَة الَّتِي وَصَلَتْ"], ["plural persons (men or mixed)", "الَّذِين", "الزَّبَائِن الَّذِين دَفَعُوا"], ["two men", "اللَّذَان", "الْبَائِعَان اللَّذَان يَعْمَلَان هُنَا"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("In store sentences",
             "Find the noun that each pronoun refers to.",
             examples=[
                 ex("الزَّبُون الَّذِي دَفَعَ نَقْدًا حَصَلَ عَلَى خَصْم.", "The customer who paid in cash got a discount.", "الَّذِي"),
                 ex("الثَّلَّاجَة الَّتِي اِشْتَرَيْتُهَا كَبِيرَة.", "The refrigerator that I bought is big.", "الَّتِي"),
                 ex("الْأَجْهِزَة الَّتِي وَصَلَتْ أَمْسِ جَدِيدَة.", "The appliances that arrived yesterday are new.", "الَّتِي"),
                 ex("الزَّبَائِن الَّذِين دَفَعُوا نَقْدًا سَعِيدُون.", "The customers who paid in cash are happy.", "الَّذِين"),
                 ex("الْبَائِعَان اللَّذَان يَعْمَلَان هُنَا مِنْ بَيْرُوت.", "The two sellers who work here are from Beirut.", "اللَّذَان"),
             ]),
    ],
    exercises=[
        M("Which pronoun fits الزَّبُون?", "الَّذِي", ["الَّتِي", "الَّذِين"], "Masculine singular."),
        M("Which pronoun fits الثَّلَّاجَة?", "الَّتِي", ["الَّذِي", "اللَّذَان"], "Feminine singular."),
        M("Which pronoun fits الْأَجْهِزَة (the appliances)?", "الَّتِي", ["الَّذِين", "الَّذِي"], "Plural things take the feminine singular."),
        M("Which pronoun fits الزَّبَائِن (the customers)?", "الَّذِين", ["الَّتِي", "الَّذِي"], "Plural persons."),
        M("What does الزَّبُون الَّذِي دَفَعَ نَقْدًا حَصَلَ عَلَى خَصْم mean?", "The customer who paid in cash got a discount", ["The customer who got a discount paid by card", "The seller gave a gift", "The customer asked for cash"], "الَّذِي refers to الزَّبُون."),
        M("What does الْأَجْهِزَة الَّتِي وَصَلَتْ أَمْسِ جَدِيدَة mean?", "The appliances that arrived yesterday are new", ["The appliances will arrive tomorrow", "The new appliances are cheap", "The appliances left yesterday"], "الَّتِي refers to الْأَجْهِزَة."),
        F("الزَّبُون ___ دَفَعَ نَقْدًا حَصَلَ عَلَى خَصْم.", "الَّذِي", ["الَّتِي", "اللَّذَان"], "الزَّبُون is masculine singular.", tr="The customer who paid in cash got a discount."),
        F("الْأَجْهِزَة ___ وَصَلَتْ أَمْسِ جَدِيدَة.", "الَّتِي", ["الَّذِين", "الَّذِي"], "Plural things.", tr="The appliances that arrived yesterday are new."),
        F("الزَّبَائِن ___ دَفَعُوا نَقْدًا سَعِيدُون.", "الَّذِين", ["الَّذِي", "الَّتِي"], "Plural persons.", tr="The customers who paid in cash are happy."),
    ],
    verify=(vv("حصل", "past", huwa="حَصَلَ") + vv("دفع", "past", huwa="دَفَعَ", hum="دَفَعُوا") + vv("وصل", "past", hiya="وَصَلَتْ")
            + vw("الزَّبُون", "الزَّبَائِن", "الثَّلَّاجَة", "الْأَجْهِزَة", "الْبَائِعَان", "نَقْدًا", "خَصْم", "جَدِيدَة", "كَبِيرَة", "سَعِيدُون", "يَعْمَلَان", "هُنَا", "بَيْرُوت", "أَمْسِ", "الَّتِي", "الَّذِي", "الَّذِين", "اللَّذَان")),
)


# ---------------------------------------------------------------------------- 346
L346 = lesson(
    "The apartment: rooms and floors",
    "شَقَّة · مَطْبَخ · حَمَّام · شُرْفَة · طَابِق · مِصْعَد",
    requires=["شقة", "غرفة", "مطبخ", "حمام", "شرفة", "طابق", "مصعد", "عمارة", "مدخل", "ثالث"],
    cards=[
        card("Parts of an apartment",
             "An apartment is شَقَّة, and the building is عِمَارَة. The floors of a building are طَوَابِق (singular طَابِق). "
             "To say “on the third floor”, use فِي الطَّابِق الثَّالِث, with the ordinal after the noun.",
             tables=[table(["English", "Arabic"],
                           [["apartment", "شَقَّة"], ["building", "عِمَارَة"], ["floor", "طَابِق"], ["elevator", "مِصْعَد"], ["entrance", "مَدْخَل"], ["room", "غُرْفَة"], ["kitchen", "مَطْبَخ"], ["bathroom", "حَمَّام"], ["balcony", "شُرْفَة"], ["window", "نَافِذَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Describing where things are",
             "Combine these words with the place words you know.",
             examples=[
                 ex("الشَّقَّة فِي الطَّابِق الثَّالِث.", "The apartment is on the third floor.", "الطَّابِق الثَّالِث"),
                 ex("فِي الْعِمَارَة مِصْعَد.", "In the building there is an elevator.", "مِصْعَد"),
                 ex("الْمَطْبَخ وَاسِع وَفِيهِ نَافِذَة.", "The kitchen is wide and has a window.", "نَافِذَة"),
                 ex("فِي الشَّقَّة غُرْفَتَان وَحَمَّام.", "In the apartment there are two rooms and a bathroom.", "غُرْفَتَان"),
                 ex("مِنَ الشُّرْفَة مَنْظَر جَمِيل.", "From the balcony there is a beautiful view.", "الشُّرْفَة"),
             ]),
    ],
    exercises=[
        M("What is a شُرْفَة?", "a balcony", ["a kitchen", "a window", "a floor"], "شُرْفَة = balcony."),
        M("What is a مِصْعَد?", "an elevator", ["a stairway", "an entrance", "a key"], "مِصْعَد = elevator."),
        M("What does الشَّقَّة فِي الطَّابِق الثَّالِث mean?", "The apartment is on the third floor", ["The apartment has three rooms", "The apartment is cheap", "The third apartment is empty"], "الثَّالِث = third."),
        M("What does غُرْفَتَان mean?", "two rooms", ["three rooms", "a room", "rooms"], "Dual: ـَتَان."),
        M("What is a عِمَارَة?", "a building", ["an apartment", "a street", "a school"], "عِمَارَة = building."),
        M("What does الْمَطْبَخ وَاسِع وَفِيهِ نَافِذَة mean?", "The kitchen is wide and has a window", ["The kitchen is small", "The window is in the bathroom", "The kitchen has no window"], "فِيهِ = in it."),
        F("فِي الْعِمَارَة ___", "مِصْعَد", ["مَطْبَخ", "سَرِير"], "A building can have an elevator.", tr="In the building there is an elevator."),
        F("الشَّقَّة فِي الطَّابِق ___", "الثَّالِث", ["الثَّالِثَة", "ثَلَاثَة"], "The ordinal agrees with the masculine noun طَابِق.", tr="The apartment is on the third floor."),
        F("فِي الشَّقَّة ___ وَحَمَّام.", "غُرْفَتَان", ["غُرْفَة", "غُرَف"], "“Two rooms”: dual.", tr="In the apartment there are two rooms and a bathroom."),
    ],
    verify=vw("شَقَّة", "الشَّقَّة", "عِمَارَة", "الْعِمَارَة", "طَابِق", "الطَّابِق", "الثَّالِث", "الثَّالِثَة", "ثَلَاثَة", "مِصْعَد", "مَدْخَل", "غُرْفَة", "غُرْفَتَان", "غُرَف", "مَطْبَخ", "الْمَطْبَخ", "حَمَّام", "شُرْفَة", "الشُّرْفَة", "نَافِذَة", "وَاسِع", "مَنْظَر", "جَمِيل", "سَرِير", "فِيهِ"),
)

# ---------------------------------------------------------------------------- 347
L347 = lesson(
    "Renting: contract, owner and key",
    "عَقْد الْإِيجَار · الْمَالِك · الْمِفْتَاح",
    requires=["إيجار", "مالك", "عقد", "مفتاح", "مدة", "شهر", "سنة", "دفع", "حساب", "قبل"],
    cards=[
        card("Renting words",
             "Rent is إِيجَار, and the owner is مَالِك. A contract is عَقْد. The key is مِفْتَاح. A contract is for a period of time: لِمُدَّة سَنَة, “for a period of one year”. "
             "The terms below are examples; every country and every owner has different rules.",
             tables=[table(["English", "Arabic"],
                           [["rent", "إِيجَار"], ["owner", "مَالِك"], ["contract", "عَقْد"], ["rental contract", "عَقْد الْإِيجَار"], ["key", "مِفْتَاح"], ["period, duration", "مُدَّة"], ["for a period of a year", "لِمُدَّة سَنَة"], ["every month", "كُلّ شَهْر"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Examples (invented)",
             "A tenant and an owner talk.",
             examples=[
                 ex("كَمِ الْإِيجَار الشَّهْرِيّ؟", "How much is the monthly rent?", "الْإِيجَار"),
                 ex("عَقْد الْإِيجَار لِمُدَّة سَنَة.", "The rental contract is for one year.", "لِمُدَّة سَنَة"),
                 ex("أَدْفَع الْإِيجَار أَوَّل كُلّ شَهْر.", "I pay the rent at the beginning of every month.", "أَدْفَع"),
                 ex("الْمَالِك يُعْطِينِي الْمِفْتَاح.", "The owner gives me the key.", "الْمَالِك"),
                 ex("اِقْرَأِ الْعَقْد قَبْلَ التَّوْقِيع.", "Read the contract before signing.", "اِقْرَأِ"),
             ]),
    ],
    exercises=[
        M("What is an إِيجَار?", "rent", ["a key", "a contract", "a building"], "إِيجَار = rent."),
        M("Who is the مَالِك?", "the owner", ["the neighbour", "the guest", "the cook"], "مَالِك = owner."),
        M("What is a مِفْتَاح?", "a key", ["a door", "a lock", "a window"], "مِفْتَاح = key."),
        M("What does عَقْد الْإِيجَار لِمُدَّة سَنَة mean?", "The rental contract is for one year", ["The rent is one dinar", "The owner lives for a year", "The contract is for a month"], "مُدَّة = period."),
        M("What does أَدْفَع الْإِيجَار أَوَّل كُلّ شَهْر mean?", "I pay the rent at the beginning of every month", ["I pay the rent at the end of the year", "I paid the rent yesterday", "I do not pay rent"], "أَوَّل كُلّ شَهْر = beginning of each month."),
        M("What does اِقْرَأِ الْعَقْد قَبْلَ التَّوْقِيع mean?", "Read the contract before signing", ["Sign the contract after paying", "Write the contract", "Do not read the contract"], "قَبْلَ = before."),
        F("عَقْد الْإِيجَار ___ مُدَّة سَنَة.", "لِ", ["فِي", "مِنْ"], "The preposition لِـ with مُدَّة: for a period.", tr="The rental contract is for one year."),
        F("أَنَا ___ الْإِيجَار أَوَّل كُلّ شَهْر.", "أَدْفَع", ["تَدْفَع", "دَفَعَ"], "Present, with أَنَا.", tr="I pay the rent at the beginning of every month.", lemma="دفع:pres:ana"),
        F("___ يُعْطِينِي الْمِفْتَاح.", "الْمَالِك", ["الْجِهَاز", "الْإِيجَار"], "The one who gives the key is the owner.", tr="The owner gives me the key."),
    ],
    verify=(vv("دفع", "pres", ana="أَدْفَع") + vv("دفع", "past", huwa="دَفَعَ")
            + vw("إِيجَار", "الْإِيجَار", "مَالِك", "الْمَالِك", "عَقْد", "الْعَقْد", "مِفْتَاح", "الْمِفْتَاح", "مُدَّة", "لِمُدَّة", "سَنَة", "كُلّ", "شَهْر", "الشَّهْر", "الشَّقَّة", "أَوَّل", "يُعْطِينِي", "اِقْرَأِ", "التَّوْقِيع", "الْجِهَاز", "قَبْلَ", "تَدْفَع")),
)

# ---------------------------------------------------------------------------- 348
L348 = lesson(
    "Looking at an apartment",
    "هَلِ الشَّقَّة مَفْرُوشَة؟ · كَمْ غُرْفَة فِيهَا؟",
    requires=["شقة", "غرفة", "مطبخ", "إيجار", "فتح", "نافذة", "باب", "ماء", "ساخن", "كم"],
    cards=[
        card("Questions and commands",
             "When you visit an apartment, ask short questions and give short commands. A furnished apartment is شَقَّة مَفْرُوشَة. "
             "A command to one man drops the present prefix and uses the short (jussive) form; if the stem would start with two consonants, a helping alif is added: اِفْتَحْ, “open!”. Before ال, a final sukūn takes a helping vowel: اِفْتَحِ الْبَاب.",
             tables=[table(["English", "Arabic"],
                           [["furnished", "مَفْرُوشَة"], ["How many rooms are in it?", "كَمْ غُرْفَة فِيهَا؟"], ["Is there hot water?", "هَلْ هُنَاكَ مَاء سَاخِن؟"], ["Open the window.", "اِفْتَحِ النَّافِذَة"], ["Is the rent high?", "هَلِ الْإِيجَار مُرْتَفِع؟"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A visit (invented)",
             "Read what the visitor and the owner say.",
             examples=[
                 ex("هَلِ الشَّقَّة مَفْرُوشَة؟", "Is the apartment furnished?", "مَفْرُوشَة"),
                 ex("نَعَمْ، فِيهَا سَرِير وَخِزَانَة وَطَاوِلَة.", "Yes, it has a bed, a wardrobe and a table.", "فِيهَا"),
                 ex("كَمْ غُرْفَة فِيهَا؟", "How many rooms are in it?", "كَمْ غُرْفَة"),
                 ex("اِفْتَحِ النَّافِذَة مِنْ فَضْلِكَ.", "Open the window, please.", "اِفْتَحِ"),
                 ex("هَلْ هُنَاكَ مَاء سَاخِن فِي الْحَمَّام؟", "Is there hot water in the bathroom?", "مَاء سَاخِن"),
                 ex("الْمَطْبَخ وَاسِع، وَالْإِيجَار مُنَاسِب.", "The kitchen is wide, and the rent is reasonable.", "مُنَاسِب"),
             ]),
    ],
    exercises=[
        M("What does مَفْرُوشَة mean?", "furnished", ["empty", "rented", "expensive"], "مَفْرُوشَة = furnished."),
        M("What does كَمْ غُرْفَة فِيهَا؟ ask?", "How many rooms are in it?", ["Which room is large?", "Where is the room?", "Who has the room?"], "كَمْ = how many."),
        M("What does اِفْتَحِ النَّافِذَة mean?", "Open the window", ["Close the window", "Clean the window", "Buy a window"], "اِفْتَحْ = open!"),
        M("What does هَلْ هُنَاكَ مَاء سَاخِن؟ ask?", "Is there hot water?", ["Is there cold water?", "Is there a kitchen?", "Is there a key?"], "سَاخِن = hot."),
        M("What does الْإِيجَار مُنَاسِب mean?", "The rent is reasonable", ["The rent is very high", "The rent is free", "The rent is paid"], "مُنَاسِب = suitable, reasonable."),
        M("Why does اِفْتَحِ النَّافِذَة have a kasra on ح?", "a helping vowel before ال", ["it is a past tense", "it is a question", "it is a plural"], "Final sukūn + ال takes a helping vowel."),
        F("___ النَّافِذَة مِنْ فَضْلِكَ.", "اِفْتَحِ", ["يَفْتَح", "فَتَحْتُ"], "A command to one man.", tr="Open the window, please."),
        F("هَلْ هُنَاكَ ___ سَاخِن فِي الْحَمَّام؟", "مَاء", ["مَطْبَخ", "مِفْتَاح"], "Hot water.", tr="Is there hot water in the bathroom?"),
        F("كَمْ ___ فِيهَا؟", "غُرْفَة", ["غُرَف", "غُرْفَتَان"], "After كَمْ in a question: singular.", tr="How many rooms are in it?"),
    ],
    verify=(vv("فتح", "imp", anta="اِفْتَحْ")
            + vw("مَفْرُوشَة", "الشَّقَّة", "فِيهَا", "سَرِير", "خِزَانَة", "طَاوِلَة", "غُرْفَة", "غُرَف", "غُرْفَتَان", "اِفْتَحِ", "النَّافِذَة", "فَضْلِكَ", "هُنَاكَ", "مَاء", "سَاخِن", "الْحَمَّام", "الْمَطْبَخ", "وَاسِع", "الْإِيجَار", "مُنَاسِب", "مُرْتَفِع", "الْبَاب", "يَفْتَح", "فَتَحْتُ", "مَطْبَخ", "مِفْتَاح")),
)

# ---------------------------------------------------------------------------- 349
L349 = lesson(
    "Two apartments: comparing",
    "أَكْبَر · أَرْخَص · أَقْرَب · أَجْمَل",
    requires=["شقة", "أكبر", "أرخص", "قريب", "بعيد", "جميل", "إيجار", "غرفة", "منظر", "طابق"],
    cards=[
        card("A real-estate comparison (invented)",
             "An agent describes two apartments. Compare them with the comparative forms you know: أَكْبَر, أَرْخَص, أَقْرَب. The word مِنْ means “than”.",
             tables=[table(["Feature", "Apartment A", "Apartment B"],
                           [["floor", "الطَّابِق الْأَوَّل", "الطَّابِق الْخَامِس"], ["size", "مِسَاحَة صَغِيرَة", "مِسَاحَة كَبِيرَة"], ["rooms", "غُرْفَتَان", "ثَلَاث غُرَف"], ["rent", "أَرْخَص", "أَغْلَى"], ["location", "قَرِيبَة مِنَ السُّوق", "بَعِيدَة عَنِ السُّوق"], ["view", "بِدُون مَنْظَر", "مَنْظَر جَمِيل"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("What the agent says",
             "Read the agent's comparisons.",
             examples=[
                 ex("الشَّقَّة الْأُولَى أَرْخَص مِنَ الشَّقَّة الثَّانِيَة.", "The first apartment is cheaper than the second.", "أَرْخَص"),
                 ex("الشَّقَّة الثَّانِيَة أَكْبَر وَفِيهَا ثَلَاث غُرَف.", "The second apartment is bigger and has three rooms.", "أَكْبَر"),
                 ex("الشَّقَّة الْأُولَى أَقْرَب إِلَى السُّوق.", "The first apartment is closer to the market.", "أَقْرَب"),
                 ex("مَنْظَر الشَّقَّة الثَّانِيَة أَجْمَل.", "The view from the second apartment is more beautiful.", "أَجْمَل"),
                 ex("أَيّ شَقَّة تُفَضِّل؟", "Which apartment do you prefer?", "تُفَضِّل"),
             ]),
    ],
    exercises=[
        M("Which apartment is cheaper?", "the first", ["the second", "both are the same", "neither"], "أَرْخَص."),
        M("Which apartment has three rooms?", "the second", ["the first", "both", "neither"], "ثَلَاث غُرَف."),
        M("Which apartment is closer to the market?", "the first", ["the second", "both", "neither"], "أَقْرَب إِلَى السُّوق."),
        M("Which apartment has the more beautiful view?", "the second", ["the first", "both", "neither"], "مَنْظَر جَمِيل."),
        M("What does أَيّ شَقَّة تُفَضِّل؟ ask?", "Which apartment do you prefer?", ["How much is the apartment?", "Where is the apartment?", "Who owns the apartment?"], "تُفَضِّل = you prefer."),
        M("What does مِنْ mean in أَرْخَص مِنَ الشَّقَّة الثَّانِيَة?", "than", ["from", "with", "in"], "Comparison."),
        F("الشَّقَّة الْأُولَى ___ مِنَ الشَّقَّة الثَّانِيَة.", "أَرْخَص", ["رَخِيص"], "Comparative: أَرْخَص.", tr="The first apartment is cheaper than the second."),
        F("الشَّقَّة الثَّانِيَة ___ وَفِيهَا ثَلَاث غُرَف.", "أَكْبَر", ["كَبِير"], "Comparative: أَكْبَر.", tr="The second apartment is bigger and has three rooms."),
        F("أَيّ شَقَّة ___؟", "تُفَضِّل", ["فَضَّلْتُ", "مُفَضَّل"], "You prefer: تُفَضِّل.", tr="Which apartment do you prefer?", lemma="فضل#2:pres:anta"),
    ],
    verify=(vv("فضل#2", "pres", anta="تُفَضِّل")
            + vw("الشَّقَّة", "الْأُولَى", "الثَّانِيَة", "أَرْخَص", "أَكْبَر", "أَقْرَب", "أَجْمَل", "أَغْلَى", "غُرْفَتَان", "غُرَف", "الطَّابِق", "الْأَوَّل", "الْخَامِس", "قَرِيبَة", "بَعِيدَة", "السُّوق", "مَنْظَر", "جَمِيل", "تُفَضِّل", "رَخِيص", "كَبِير", "فَضَّلْتُ", "مُفَضَّل")),
)

# ---------------------------------------------------------------------------- 350
L350 = lesson(
    "Moving in: where do I put it?",
    "أَيْنَ أَضَع الْأَرِيكَة؟ · ضَعِ الْكُرْسِيّ هُنَا",
    requires=["وضع", "نقل", "أين", "هنا", "هناك", "باب", "نافذة", "جدار", "وسط"],
    cards=[
        card("Assimilated verbs when you move",
             "وَضَعَ يَضَع means “to put”. It is an assimilated verb: the و drops in the present (أَضَع) and in the command (ضَعْ). "
             "Before ال, the command takes a helping vowel: ضَعِ الْكُرْسِيّ. For “do not put”, say لَا تَضَعْ. "
             "The verb نَقَلَ يَنْقُل means “to carry, to move (something)”.",
             tables=[table(["Form", "Arabic", "English"],
                           [["past (I)", "وَضَعْتُ", "I put"], ["present (I)", "أَضَع", "I put"], ["command (m.)", "ضَعْ", "put!"], ["command (f.)", "ضَعِي", "put! (to a woman)"], ["do not put", "لَا تَضَعْ", "do not put!"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Directing the movers",
             "These are typical sentences when furniture is moved.",
             examples=[
                 ex("أَيْنَ أَضَع الْأَرِيكَة؟", "Where do I put the sofa?", "أَضَع"),
                 ex("ضَعِ الْأَرِيكَة بِجَانِب النَّافِذَة.", "Put the sofa next to the window.", "ضَعِ"),
                 ex("ضَعِي الطَّاوِلَة فِي وَسَط الْغُرْفَة.", "Put the table in the middle of the room (to a woman).", "ضَعِي"),
                 ex("لَا تَضَعِ الْخِزَانَة أَمَامَ الْبَاب.", "Do not put the wardrobe in front of the door.", "لَا تَضَعِ"),
                 ex("نَنْقُل الْأَثَاث إِلَى الطَّابِق الثَّالِث.", "We carry the furniture to the third floor.", "نَنْقُل"),
                 ex("وَضَعْتُ الْكُرْسِيّ هُنَا أَمْسِ.", "I put the chair here yesterday.", "وَضَعْتُ"),
             ]),
    ],
    exercises=[
        M("What does ضَعْ mean?", "put!", ["carry!", "open!", "pay!"], "ضَعْ = put (command)."),
        M("What does أَيْنَ أَضَع الْأَرِيكَة؟ ask?", "Where do I put the sofa?", ["Where is the sofa?", "Who put the sofa?", "How much is the sofa?"], "أَضَع = I put."),
        M("What does ضَعِ الْأَرِيكَة بِجَانِب النَّافِذَة mean?", "Put the sofa next to the window", ["Open the window near the sofa", "The sofa is broken", "I sit on the sofa"], "بِجَانِب = next to."),
        M("What does لَا تَضَعِ الْخِزَانَة أَمَامَ الْبَاب mean?", "Do not put the wardrobe in front of the door", ["Put the wardrobe in front of the door", "The wardrobe is in the door", "Open the door"], "لَا تَضَعْ = do not put."),
        M("What does نَنْقُل الْأَثَاث إِلَى الطَّابِق الثَّالِث mean?", "We carry the furniture to the third floor", ["We sell the furniture", "We buy the furniture", "We forget the furniture"], "نَنْقُل = we carry."),
        M("Which is the command to a woman?", "ضَعِي", ["ضَعْ", "تَضَعِينَ"], "Feminine ending ـِي."),
        F("___ الْأَرِيكَة بِجَانِب النَّافِذَة.", "ضَعِ", ["أَضَع", "وَضَعْتُ"], "A command to one man.", tr="Put the sofa next to the window.", lemma="وضع:imp:anta"),
        F("لَا ___ الْخِزَانَة أَمَامَ الْبَاب.", "تَضَعِ", ["ضَعْ", "وَضَعَ"], "Negative command: لَا تَضَعْ.", tr="Do not put the wardrobe in front of the door."),
        F("أَيْنَ ___ الْأَرِيكَة؟", "أَضَع", ["ضَعْ", "وَضَعْتُ"], "Present with أَنَا.", tr="Where do I put the sofa?", lemma="وضع:pres:ana"),
    ],
    verify=(vv("وضع", "past", ana="وَضَعْتُ") + vv("وضع", "pres", ana="أَضَع") + vv("وضع", "imp", anta="ضَعْ", anti="ضَعِي") + vv("وضع", "neg", anta="لَا تَضَعْ") + vv("نقل", "pres", nahnu="نَنْقُل")
            + vw("أَضَع", "ضَعْ", "ضَعِ", "ضَعِي", "تَضَعِ", "تَضَعِينَ", "وَضَعْتُ", "الْأَرِيكَة", "بِجَانِب", "النَّافِذَة", "الطَّاوِلَة", "وَسَط", "الْغُرْفَة", "الْخِزَانَة", "أَمَامَ", "الْبَاب", "نَنْقُل", "الْأَثَاث", "الطَّابِق", "الثَّالِث", "هُنَا", "أَمْسِ", "الْكُرْسِيّ")),
)


# ---------------------------------------------------------------------------- 351
L351 = lesson(
    "Reading a sale flyer",
    "تَبْدَأ التَّخْفِيضَات يَوْم السَّبْت · اِشْتَرِ الْآن",
    requires=["بدأ", "وصل", "خصم", "أسبوع", "فقط", "جهاز", "سعر", "أثاث", "كمية", "جديد"],
    cards=[
        card("Flyer language",
             "A sale flyer uses short sentences and commands. Remember chapter 16: when the subject is a plural thing such as التَّخْفِيضَات (“the sales”) or أَجْهِزَة (“appliances”), a verb that comes first is feminine singular: تَبْدَأ, تَنْتَهِي, تَصِل. "
             "A command with a defective verb loses its final long vowel: اِشْتَرِ (from اِشْتَرَى). A short exclamation uses مَا + أَفْعَلَ + the thing in the accusative: مَا أَرْخَصَ هَذِهِ الْأَسْعَارَ! The flyer below is invented.",
             tables=[table(["Item", "Offer", "Limit"],
                           [["أَثَاث غُرْفَة النَّوْم", "خَصْم عِشْرُون بِالْمِئَة", "لِمُدَّة أُسْبُوع"], ["غَسَّالَات", "تَوْصِيل مَجَّانِيّ", "الْكَمِّيَّة مَحْدُودَة"], ["ثَلَّاجَات", "كَفَالَة ثَلَاث سَنَوَات", "فَقَط هَذَا الشَّهْر"]],
                           say=[0, 1, 2], tlit=[0, 1, 2], gloss=False)]),
        card("Sentences from the flyer",
             "Read the lines in order.",
             examples=[
                 ex("تَبْدَأ التَّخْفِيضَات يَوْم السَّبْت.", "The sales start on Saturday.", "تَبْدَأ"),
                 ex("تَنْتَهِي التَّخْفِيضَات يَوْم الْجُمْعَة.", "The sales end on Friday.", "تَنْتَهِي"),
                 ex("تَصِل أَجْهِزَة جَدِيدَة كُلّ أُسْبُوع.", "New appliances arrive every week.", "تَصِل"),
                 ex("اِشْتَرِ الْآن وَلَا تَنْسَ الْفَاتُورَة.", "Buy now and do not forget the receipt.", "اِشْتَرِ"),
                 ex("الْخَصْم عَلَى الْأَثَاث فَقَط.", "The discount is on furniture only.", "فَقَط"),
                 ex("مَا أَرْخَصَ هَذِهِ الْأَسْعَارَ!", "How cheap these prices are!", "مَا أَرْخَصَ"),
             ]),
    ],
    exercises=[
        M("Why is the verb تَبْدَأ feminine in تَبْدَأ التَّخْفِيضَات?", "the subject is a plural thing", ["the sales are female", "the verb is a command", "it is in the past"], "Plural things take a feminine singular verb."),
        M("What does تَنْتَهِي التَّخْفِيضَات يَوْم الْجُمْعَة mean?", "The sales end on Friday", ["The sales start on Friday", "The sales are free on Friday", "The shop closes on Friday"], "تَنْتَهِي = ends."),
        M("What does اِشْتَرِ الْآن mean?", "Buy now", ["Sell now", "Pay later", "Wait here"], "اِشْتَرِ = buy! (command)."),
        M("What does فَقَط mean?", "only", ["every", "free", "tomorrow"], "فَقَط = only."),
        M("What does الْكَمِّيَّة مَحْدُودَة mean?", "The quantity is limited", ["The quantity is large", "The price is limited", "The delivery is free"], "مَحْدُودَة = limited."),
        M("What does مَا أَرْخَصَ هَذِهِ الْأَسْعَارَ! express?", "How cheap these prices are!", ["What are these prices?", "These prices are higher", "Where are the prices?"], "مَا + أَفْعَلَ."),
        F("___ التَّخْفِيضَات يَوْم السَّبْت.", "تَبْدَأ", ["يَبْدَأ", "يَبْدَأُونَ"], "Plural thing: feminine singular verb.", tr="The sales start on Saturday.", lemma="بدأ:pres:hiya"),
        F("___ أَجْهِزَة جَدِيدَة كُلّ أُسْبُوع.", "تَصِل", ["يَصِل", "يَصِلُونَ"], "Plural things: feminine singular verb.", tr="New appliances arrive every week.", lemma="وصل:pres:hiya"),
        F("اِشْتَرِ الْآن وَلَا ___ الْفَاتُورَة.", "تَنْسَ", ["نَسِيتُ", "نَسِيَ"], "Negative command.", tr="Buy now and do not forget the receipt."),
    ],
    verify=(vv("بدأ", "pres", hiya="تَبْدَأ") + vv("وصل", "pres", hiya="تَصِل")
            + vw("تَبْدَأ", "التَّخْفِيضَات", "تَنْتَهِي", "تَصِل", "اِشْتَرِ", "الْفَاتُورَة", "الْجُمْعَة", "السَّبْت", "أَجْهِزَة", "جَدِيدَة", "كُلّ", "أُسْبُوع", "الْخَصْم", "الْأَثَاث", "فَقَط", "الْكَمِّيَّة", "مَحْدُودَة", "غَسَّالَات", "ثَلَّاجَات", "مَجَّانِيّ", "الشَّهْر", "الْأَسْعَارَ", "هَذِهِ", "أَرْخَصَ", "يَبْدَأ", "يَبْدَأُونَ", "يَصِل", "يَصِلُونَ", "تَنْسَى", "نَسِيَ", "تَنْسَ")),
)

# ---------------------------------------------------------------------------- 352
L352 = lesson(
    "A delivery problem",
    "لَمْ تَصِلِ الْغَسَّالَة · وَجَدْتُ عَيْبًا · سَنَرُدّ لَكَ الْمَبْلَغ",
    requires=["وصل", "وجد", "وعد", "عيب", "مبلغ", "فاتورة", "رد", "أمس", "خلال"],
    cards=[
        card("A conversation (invented)",
             "A customer calls the store about a late delivery and a defect. Notice the assimilated verbs وَصَلَ, وَجَدَ, وَعَدَ; the negative past لَمْ تَصِلْ; and the double-letter verb in سَنَرُدّ, “we will return”.",
             examples=[
                 ex("لَمْ تَصِلِ الْغَسَّالَة أَمْسِ.", "The washing machine did not arrive yesterday.", "لَمْ تَصِلِ"),
                 ex("وَعَدَنِي الْبَائِع بِالتَّوْصِيل أَمْسِ.", "The seller promised me delivery yesterday.", "وَعَدَنِي"),
                 ex("نَعْتَذِر، سَتَصِل الْغَسَّالَة غَدًا صَبَاحًا.", "We apologise; the washing machine will arrive tomorrow morning.", "نَعْتَذِر"),
                 ex("وَجَدْتُ عَيْبًا فِي الثَّلَّاجَة.", "I found a defect in the refrigerator.", "وَجَدْتُ"),
                 ex("أَرْسِلْ لِي الْفَاتُورَة مِنْ فَضْلِكَ.", "Send me the receipt, please.", "أَرْسِلْ"),
                 ex("سَنَرُدّ لَكَ الْمَبْلَغ خِلَال أُسْبُوع.", "We will return the amount to you within a week.", "سَنَرُدّ"),
             ]),
    ],
    exercises=[
        M("What does لَمْ تَصِلِ الْغَسَّالَة أَمْسِ mean?", "The washing machine did not arrive yesterday", ["The washing machine will not arrive", "The washing machine arrived yesterday", "The washing machine is broken"], "لَمْ + present = past negative."),
        M("What does وَعَدَنِي الْبَائِع بِالتَّوْصِيل mean?", "The seller promised me delivery", ["The seller paid me for delivery", "The seller refused delivery", "The seller forgot me"], "وَعَدَ = promised."),
        M("What does نَعْتَذِر mean?", "we apologise", ["we promise", "we arrive", "we pay"], "نَعْتَذِر = we apologise."),
        M("What does وَجَدْتُ عَيْبًا فِي الثَّلَّاجَة mean?", "I found a defect in the refrigerator", ["I lost the refrigerator", "I bought a refrigerator", "I returned the refrigerator"], "وَجَدْتُ = I found."),
        M("What does سَنَرُدّ لَكَ الْمَبْلَغ mean?", "We will return the amount to you", ["We will send you a receipt", "We paid you yesterday", "You will pay the amount"], "سَنَرُدّ = we will return."),
        M("What does أَرْسِلْ لِي الْفَاتُورَة mean?", "Send me the receipt", ["Keep the receipt", "I sent you the receipt", "Write the receipt"], "أَرْسِلْ = send! (to one man); لِي = to me."),
        F("___ تَصِلِ الْغَسَّالَة أَمْسِ.", "لَمْ", ["لَنْ", "لَا"], "Negative past: لَمْ.", tr="The washing machine did not arrive yesterday."),
        F("وَجَدْتُ ___ فِي الثَّلَّاجَة.", "عَيْبًا", ["فَاتُورَة", "كَفَالَة"], "A fault is a defect.", tr="I found a defect in the refrigerator."),
        F("سَنَرُدّ لَكَ ___ خِلَال أُسْبُوع.", "الْمَبْلَغ", ["الْعَيْب", "الْمِفْتَاح"], "The amount of money.", tr="We will return the amount to you within a week."),
    ],
    verify=(vv("وصل", "jus", hiya="تَصِلْ") + vv("وعد", "past", huwa="وَعَدَ") + vv("وجد", "past", ana="وَجَدْتُ") + vv("ردد", "fut", nahnu="سَنَرُدّ") + vv("وصل", "fut", hiya="سَتَصِل")
            + vw("تَصِلِ", "الْغَسَّالَة", "أَمْسِ", "وَعَدَنِي", "الْبَائِع", "بِالتَّوْصِيل", "نَعْتَذِر", "سَتَصِل", "غَدًا", "صَبَاحًا", "وَجَدْتُ", "عَيْبًا", "الثَّلَّاجَة", "أَرْسِلْ", "الْفَاتُورَة", "فَضْلِكَ", "سَنَرُدّ", "الْمَبْلَغ", "خِلَال", "أُسْبُوع", "لَنْ", "لَا", "كَفَالَة", "الْعَيْب", "الْمِفْتَاح")),
)

# ---------------------------------------------------------------------------- 353
L353 = lesson(
    "A story: buying a bedroom set (invented)",
    "ذَهَبَتْ نَادِيَة وَصَدِيقَتُهَا إِلَى مَحَلّ الْأَثَاث",
    requires=["ذهب", "أثاث", "محل", "بائع", "كفالة", "دفع", "جودة", "سنة", "غرفة"],
    cards=[
        card("A short story",
             "This invented story uses everything from the last chapters: a verb before a compound subject, verbs of Measures II, IV, VIII and X, a relative pronoun, a passive, and defective verbs. A bedroom set is طَقْم غُرْفَة النَّوْم. Read it sentence by sentence.",
             examples=[
                 ex("ذَهَبَتْ نَادِيَة وَصَدِيقَتُهَا إِلَى مَحَلّ الْأَثَاث.", "Nadia and her friend went to the furniture shop.", "ذَهَبَتْ"),
                 ex("اِسْتَقْبَلَهُمَا الْبَائِع مَعَ اِبْتِسَامَة.", "The salesman welcomed them with a smile.", "اِسْتَقْبَلَهُمَا"),
                 ex("أَقْنَعَهُمَا الْبَائِع بِطَقْم غُرْفَة النَّوْم الَّذِي كَفَالَتُهُ ثَلَاث سَنَوَات.", "The salesman convinced them to take the bedroom set whose warranty is three years.", "الَّذِي"),
                 ex("اِخْتَارَتْ نَادِيَة الدَّفْع عَلَى أَقْسَاط شَهْرِيَّة.", "Nadia chose to pay in monthly instalments.", "اِخْتَارَتْ"),
                 ex("يُسَلَّم الْأَثَاث بَعْدَ يَوْمَيْن.", "The furniture is delivered after two days.", "يُسَلَّم"),
                 ex("كَانَتْ نَادِيَة سَعِيدَة، وَلَمْ تَنْسَ الْفَاتُورَة.", "Nadia was happy, and she did not forget the receipt.", "لَمْ تَنْسَ"),
             ]),
    ],
    exercises=[
        M("Where did Nadia and her friend go?", "to a furniture shop", ["to a restaurant", "to a school", "to a bank"], "إِلَى مَحَلّ الْأَثَاث."),
        M("Who welcomed them?", "the salesman", ["the owner", "the cook", "the driver"], "اِسْتَقْبَلَهُمَا الْبَائِع."),
        M("How long is the warranty of the bedroom set?", "three years", ["one year", "two years", "five years"], "كَفَالَتُهُ ثَلَاث سَنَوَات."),
        M("How did Nadia choose to pay?", "in monthly instalments", ["in cash", "by cheque", "she did not pay"], "عَلَى أَقْسَاط شَهْرِيَّة."),
        M("Which verb in the story is passive?", "يُسَلَّم", ["ذَهَبَتْ", "اِخْتَارَتْ", "أَقْنَعَ"], "يُسَلَّم = is delivered."),
        M("What does الَّذِي refer to in the third sentence?", "the bedroom set", ["the salesman", "the shop", "Nadia"], "الَّذِي agrees with the first noun, masculine طَقْم."),
        F("___ نَادِيَة وَصَدِيقَتُهَا إِلَى مَحَلّ الْأَثَاث.", "ذَهَبَتْ", ["ذَهَبُوا", "يَذْهَبُونَ"], "A verb before its subject: feminine singular.", tr="Nadia and her friend went to the furniture shop."),
        F("اِخْتَارَتْ نَادِيَة الدَّفْع عَلَى ___ شَهْرِيَّة.", "أَقْسَاط", ["خَشَب", "سَرِير"], "Instalments.", tr="Nadia chose to pay in monthly instalments."),
        F("كَانَتْ نَادِيَة سَعِيدَة، وَلَمْ ___ الْفَاتُورَة.", "تَنْسَ", ["تَنْسَى", "نَسِيَ"], "After لَمْ, the shortened present: تَنْسَ.", tr="Nadia was happy, and she did not forget the receipt."),
    ],
    verify=(vv("ذهب", "past", hiya="ذَهَبَتْ")
            + vw("نَادِيَة", "وَصَدِيقَتُهَا", "الْأَثَاث", "اِسْتَقْبَلَهُمَا", "الْبَائِع", "أَقْنَعَهُمَا", "بِطَقْم", "غُرْفَة", "النَّوْم", "الَّذِي", "كَفَالَتُهُ", "ثَلَاث", "سَنَوَات", "اِخْتَارَتْ", "الدَّفْع", "أَقْسَاط", "شَهْرِيَّة", "يُسَلَّم", "يَوْمَيْن", "سَعِيدَة", "تَنْسَ", "الْفَاتُورَة", "تَنْسَى", "نَسِيَ", "ذَهَبُوا", "يَذْهَبُونَ", "خَشَب", "سَرِير", "أَقْنَعَ")),
)

# ---------------------------------------------------------------------------- 354
L354 = lesson(
    "Review: chapters 16–20",
    "plural things · relative pronouns · passive · defective · double-letter",
    requires=["أثاث", "جهاز", "وصل", "نسي", "وضع", "كفالة", "رد", "سنة", "شقة"],
    cards=[
        card("What the unit taught",
             "Look back over the unit. A verb before a plural thing is feminine singular. A relative pronoun agrees with its noun. The passive changes the vowels: يُقْبَل. "
             "Defective verbs shorten their last vowel after لَا, لَمْ and in commands. Assimilated verbs drop the و in the present and command. Double-letter verbs open the shadda before consonant endings. An exclamation is built as مَا + a word like أَجْمَلَ + the thing in the accusative.",
             tables=[table(["Topic", "Example", "English"],
                           [["plural things", "وَصَلَتِ الْأَجْهِزَة", "The appliances arrived"], ["relative", "الْغَسَّالَة الَّتِي اِشْتَرَيْتُهَا", "the washing machine that I bought"], ["passive", "لَا يُقْبَل الرَّدّ", "returning is not accepted"],
                            ["defective", "لَا تَنْسَ", "do not forget"], ["assimilated", "ضَعِ الْكُرْسِيّ هُنَا", "put the chair here"], ["double-letter", "مَرَرْتُ بِالْمَحَلّ", "I passed by the shop"], ["exclamation", "مَا أَجْمَلَ الشُّرْفَةَ!", "How beautiful the balcony is!"]],
                           say=[1], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("Which verb fits: ___ الْأَجْهِزَة الْجَدِيدَة أَمْسِ?", "وَصَلَتِ", ["وَصَلَ", "وَصَلُوا"], "Plural things: feminine singular."),
        M("Which relative pronoun fits الثَّلَّاجَة?", "الَّتِي", ["الَّذِي", "الَّذِين"], "Feminine singular."),
        M("What does لَا يُقْبَل رَدّ الْجِهَاز mean?", "Returning the appliance is not accepted", ["The appliance is cheap", "The appliance is free", "The appliance is new"], "Passive: يُقْبَل."),
        M("What does ضَعِ الْكُرْسِيّ هُنَا mean?", "Put the chair here", ["Buy the chair", "Sit on the chair", "The chair is here"], "ضَعْ = put."),
        M("What does مَا أَجْمَلَ الشُّرْفَةَ! express?", "How beautiful the balcony is!", ["Where is the balcony?", "The balcony is bigger", "Which balcony?"], "مَا + أَفْعَلَ."),
        M("What is the past of مَرَّ with أَنَا?", "مَرَرْتُ", ["مَرَّتْ", "أَمُرّ"], "Shadda opens before تُ."),
        F("لَا ___ الْفَاتُورَة.", "تَنْسَ", ["نَسِيتُ", "نَسِيَ"], "After لَا (command): shortened.", tr="Do not forget the receipt."),
        F("الْكَفَالَة ثَلَاث ___", "سَنَوَات", ["سَنَة", "سَنَتَان"], "Numbers 3–10 + plural.", tr="The warranty is three years."),
        F("أَنَا ___ الْمَبْلَغ إِلَى الْمَحَلّ.", "رَدَدْتُ", ["رَدَّتْ", "رَدُّوا"], "Past, with “I”: the shadda opens.", tr="I returned the amount to the shop."),
    ],
    verify=(vv("وصل", "past", hiya="وَصَلَتْ") + vv("قبل", "ppres", huwa="يُقْبَل") + vv("وضع", "imp", anta="ضَعْ") + vv("مرر", "past", ana="مَرَرْتُ") + vv("ردد", "past", ana="رَدَدْتُ")
            + vw("وَصَلَتِ", "وَصَلُوا", "الْأَجْهِزَة", "الْجَدِيدَة", "أَمْسِ", "الثَّلَّاجَة", "الَّتِي", "الَّذِي", "الَّذِين", "رَدّ", "الْجِهَاز", "الْكُرْسِيّ", "هُنَا", "الشُّرْفَةَ", "أَجْمَلَ", "الْفَاتُورَة", "تَنْسَى", "نَسِيَ", "تَنْسَ", "الْكَفَالَة", "ثَلَاث", "سَنَوَات", "سَنَة", "سَنَتَان", "الْمَبْلَغ", "الْمَحَلّ", "رَدَّتْ", "رَدُّوا", "الْغَسَّالَة", "الرَّدّ")),
)


UNIT = unit("الْمَتْجَر وَالْبَيْت: stores, furniture, payment and review", [L337, L338, L339, L340, L341, L342, L343, L344, L345, L346, L347, L348, L349, L350, L351, L352, L353, L354])
