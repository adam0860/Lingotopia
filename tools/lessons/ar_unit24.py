"""Unit 24 (chapter 22): hotels, complaints and apologies, imperatives of derived verbs, historic sites, transport, borders and adverbs of time."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 374
L374 = lesson(
    "Checking in at the hotel",
    "لَدَيَّ حَجْز لِسَالِم · وَقِّعْ هُنَا مِنْ فَضْلِكَ",
    requires=["فندق", "حجز", "غرفة", "جواز", "مفتاح", "طابق", "مصعد", "توقيع"],
    cards=[
        card("At the reception desk",
             "The place where guests arrive is مَكْتَب الِاسْتِقْبَال, and the clerk is مُوَظَّف الِاسْتِقْبَال. A room for one person is غُرْفَة مُفْرَدَة and a room for two is غُرْفَة مُزْدَوِجَة. "
             "To sign, the clerk says وَقِّعْ (a command from Measure II). The sentences below are an invented conversation.",
             tables=[table(["English", "Arabic"],
                           [["reception desk", "مَكْتَب الِاسْتِقْبَال"], ["single room", "غُرْفَة مُفْرَدَة"], ["double room", "غُرْفَة مُزْدَوِجَة"], ["key", "مِفْتَاح"], ["floor", "طَابِق"], ["elevator", "مِصْعَد"], ["signature", "تَوْقِيع"], ["for (a person)", "لِ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A conversation (invented)",
             "A guest arrives in the evening.",
             examples=[
                 ex("مَسَاء الْخَيْر، لَدَيَّ حَجْز لِسَالِم.", "Good evening, I have a booking for Salem.", "لَدَيَّ"),
                 ex("أَهْلًا وَسَهْلًا، جَوَاز سَفَرِكَ مِنْ فَضْلِكَ.", "Welcome, your passport, please.", "جَوَاز سَفَرِكَ"),
                 ex("غُرْفَتَان مُزْدَوِجَتَان لِمُدَّة أُسْبُوع.", "Two double rooms for a week.", "مُزْدَوِجَتَان"),
                 ex("وَقِّعْ هُنَا مِنْ فَضْلِكَ.", "Sign here, please.", "وَقِّعْ"),
                 ex("هَذَا مِفْتَاحُكَ، وَغُرْفَتُكَ فِي الطَّابِق السَّابِع.", "This is your key, and your room is on the seventh floor.", "الطَّابِق السَّابِع"),
                 ex("الْمِصْعَد عَلَى الْيَمِين.", "The elevator is on the right.", "الْمِصْعَد"),
             ]),
    ],
    exercises=[
        M("What is مَكْتَب الِاسْتِقْبَال?", "the reception desk", ["the dining room", "the elevator", "the key"], "اِسْتِقْبَال = receiving guests."),
        M("What is a غُرْفَة مُزْدَوِجَة?", "a double room", ["a single room", "a kitchen", "a lobby"], "مُزْدَوِجَة = double."),
        M("What does لَدَيَّ حَجْز لِسَالِم mean?", "I have a booking for Salem", ["Salem has no booking", "I cancelled Salem’s booking", "Salem works here"], "لَدَيَّ = I have; لِ = for."),
        M("What does وَقِّعْ هُنَا mean?", "Sign here", ["Wait here", "Sit here", "Pay here"], "وَقِّعْ = sign! (command)."),
        M("Which floor is the room on?", "the seventh", ["the first", "the third", "the tenth"], "الطَّابِق السَّابِع."),
        M("Where is the elevator?", "on the right", ["on the left", "behind the desk", "upstairs"], "عَلَى الْيَمِين."),
        F("لَدَيَّ ___ لِسَالِم.", "حَجْز", ["خَصْم", "جَوَاز"], "A booking for a person.", tr="I have a booking for Salem."),
        F("___ هُنَا مِنْ فَضْلِكَ.", "وَقِّعْ", ["وَقَّعَ", "يُوَقِّع"], "A command to one man, Measure II: وَقِّعْ.", tr="Sign here, please.", lemma="وقع#2:imp:anta"),
        F("غُرْفَتَان ___ لِمُدَّة أُسْبُوع.", "مُزْدَوِجَتَان", ["مُزْدَوِجَة", "مُزْدَوِجُون"], "A dual feminine noun needs a dual adjective.", tr="Two double rooms for a week."),
    ],
    verify=vv("وقع#2", "imp", anta="وَقِّعْ"),
)

# ---------------------------------------------------------------------------- 375
L375 = lesson(
    "A problem with the reservation",
    "لَا أَجِد حَجْزَكَ · هَلْ عِنْدَكَ رَقْم تَأْكِيد؟",
    requires=["حجز", "رقم", "تأكيد", "غرفة", "فندق", "مدير", "خطأ"],
    cards=[
        card("When the booking is not found",
             "Sometimes the clerk cannot find a booking. The clerk may ask for the confirmation number, رَقْم تَأْكِيد الْحَجْز, and may offer another room. The verb وَجَدَ gives لَا أَجِد, “I do not find”. "
             "A polite apology is أَعْتَذِر عَنْ هَذَا الْخَطَأ, “I apologise for this mistake”. These are invented lines.",
             examples=[
                 ex("آسِف، لَا أَجِد حَجْزَكَ فِي الْقَائِمَة.", "Sorry, I do not find your booking on the list.", "لَا أَجِد"),
                 ex("هَلْ عِنْدَكَ رَقْم تَأْكِيد الْحَجْز؟", "Do you have the booking confirmation number?", "رَقْم تَأْكِيد الْحَجْز"),
                 ex("الْفُنْدُق مُمْتَلِئ الْيَوْم، لَكِنْ هُنَاكَ غُرْفَة شَاغِرَة وَاحِدَة.", "The hotel is full today, but there is one vacant room.", "شَاغِرَة"),
                 ex("هَلْ يُمْكِنُكَ أَنْ تَنْتَظِر قَلِيلًا؟", "Can you wait a little?", "تَنْتَظِر"),
                 ex("سَأَتَّصِل بِالْمُدِير.", "I will call the manager.", "سَأَتَّصِل"),
                 ex("أَعْتَذِر عَنْ هَذَا الْخَطَأ.", "I apologise for this mistake.", "أَعْتَذِر"),
             ]),
    ],
    exercises=[
        M("What does لَا أَجِد حَجْزَكَ mean?", "I do not find your booking", ["I cancelled your booking", "I made your booking", "Your booking is free"], "أَجِد = I find."),
        M("What is رَقْم تَأْكِيد الْحَجْز?", "the booking confirmation number", ["the room number", "the phone number", "the price"], "تَأْكِيد = confirmation."),
        M("What does مُمْتَلِئ mean in الْفُنْدُق مُمْتَلِئ?", "full", ["empty", "old", "new"], "مُمْتَلِئ = full."),
        M("What does غُرْفَة شَاغِرَة mean?", "a vacant room", ["a dirty room", "a double room", "a small room"], "شَاغِر = vacant."),
        M("What does هَلْ يُمْكِنُكَ أَنْ تَنْتَظِر قَلِيلًا؟ ask?", "Can you wait a little?", ["Can you pay now?", "Can you sign?", "Can you leave?"], "تَنْتَظِر = you wait."),
        M("What does أَعْتَذِر عَنْ هَذَا الْخَطَأ mean?", "I apologise for this mistake", ["I thank you for this gift", "I forgot this number", "I want this room"], "اِعْتَذَرَ = to apologise."),
        F("آسِف، لَا ___ حَجْزَكَ فِي الْقَائِمَة.", "أَجِد", ["وَجَدْتُ", "يَجِد"], "“I find”: أَجِد.", tr="Sorry, I do not find your booking on the list.", lemma="وجد:pres:ana"),
        F("هَلْ عِنْدَكَ رَقْم ___ الْحَجْز؟", "تَأْكِيد", ["تَوْقِيع", "تَذْكِرَة"], "The confirmation number.", tr="Do you have the booking confirmation number?"),
        F("___ بِالْمُدِير.", "سَأَتَّصِل", ["اِتَّصَلْتُ", "يَتَّصِل"], "Future, I: سَأَتَّصِل.", tr="I will call the manager."),
    ],
    verify=(vv("وجد", "pres", ana="أَجِد")),
)

# ---------------------------------------------------------------------------- 376
L376 = lesson(
    "The hotel room",
    "فِي الْغُرْفَة سَرِيرَان وَتِلْفَاز وَمُكَيِّف",
    requires=["غرفة", "سرير", "تلفزيون", "حمام", "ماء", "ساخن", "غطاء", "إفطار"],
    cards=[
        card("What is in the room?",
             "Hotel rooms usually have a bed (سَرِير), a television (تِلْفَاز), an air conditioner (مُكَيِّف) and a bathroom (حَمَّام). Smaller things are a pillow (وِسَادَة), a blanket (غِطَاء) and a towel (مِنْشَفَة). "
             "The dual is used for two beds: سَرِيرَان.",
             tables=[table(["English", "Arabic"],
                           [["bed", "سَرِير"], ["two beds", "سَرِيرَان"], ["television", "تِلْفَاز"], ["air conditioner", "مُكَيِّف"], ["bathroom", "حَمَّام"], ["pillow", "وِسَادَة"], ["blanket", "غِطَاء"], ["towel", "مِنْشَفَة"], ["breakfast", "إِفْطَار"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Asking about the room (invented)",
             "A guest asks the clerk.",
             examples=[
                 ex("فِي الْغُرْفَة سَرِيرَان وَتِلْفَاز وَمُكَيِّف.", "In the room there are two beds, a television and an air conditioner.", "سَرِيرَان"),
                 ex("الْحَمَّام فِيهِ مَاء سَاخِن.", "The bathroom has hot water.", "مَاء سَاخِن"),
                 ex("أُرِيد وِسَادَة وَغِطَاء آخَر.", "I want a pillow and another blanket.", "وِسَادَة"),
                 ex("أَحْتَاج إِلَى مِنْشَفَة.", "I need a towel.", "مِنْشَفَة"),
                 ex("الْإِفْطَار مِنَ السَّاعَة السَّابِعَة إِلَى الْعَاشِرَة.", "Breakfast is from seven to ten.", "الْإِفْطَار"),
                 ex("أَيْنَ الْمَطْعَم؟", "Where is the restaurant?", "الْمَطْعَم"),
             ]),
    ],
    exercises=[
        M("What is سَرِيرَان?", "two beds", ["one bed", "three beds", "a big bed"], "The dual ending ـَان."),
        M("What is a مُكَيِّف?", "an air conditioner", ["a television", "a towel", "a key"], "مُكَيِّف = air conditioner."),
        M("What does أُرِيد وِسَادَة mean?", "I want a pillow", ["I want a towel", "I want a bed", "I want a key"], "وِسَادَة = pillow."),
        M("What does الْحَمَّام فِيهِ مَاء سَاخِن mean?", "The bathroom has hot water", ["The bathroom is cold", "The bathroom is closed", "The bathroom is far"], "سَاخِن = hot."),
        M("What does أَحْتَاج إِلَى مِنْشَفَة mean?", "I need a towel", ["I sell a towel", "I lost a towel", "I like a towel"], "أَحْتَاج إِلَى = I need."),
        M("When is breakfast?", "from seven to ten", ["from ten to one", "from one to four", "at night"], "مِنَ السَّاعَة السَّابِعَة إِلَى الْعَاشِرَة."),
        F("فِي الْغُرْفَة ___ وَتِلْفَاز.", "سَرِيرَان", ["سَرِير", "أَسِرَّة"], "Two beds: the dual.", tr="In the room there are two beds and a television."),
        F("أَحْتَاج ___ مِنْشَفَة.", "إِلَى", ["فِي", "عَنْ"], "“need” takes إِلَى.", tr="I need a towel."),
        F("الْإِفْطَار ___ السَّاعَة السَّابِعَة.", "مِنَ", ["فِي", "بَعْد"], "“from”.", tr="Breakfast is from seven o’clock."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 377
L377 = lesson(
    "Complaining about the room",
    "الْمُكَيِّف لَا يَعْمَل · الْغُرْفَة غَيْر نَظِيفَة",
    requires=["غرفة", "نظيف", "بارد", "ضجيج", "مشكلة", "حمام", "ساخن", "إصلاح"],
    cards=[
        card("Saying what is wrong",
             "To say that something does not work, use لَا يَعْمَل (for a masculine thing) or لَا تَعْمَل (for a feminine thing). “Not clean” is غَيْر نَظِيف. "
             "Politely ask for a solution: هَلْ يُمْكِن إِصْلَاح …؟, “Can … be repaired?”, or أُرِيد غُرْفَة أُخْرَى, “I want another room”.",
             examples=[
                 ex("الْمُكَيِّف لَا يَعْمَل.", "The air conditioner does not work.", "لَا يَعْمَل"),
                 ex("الْغُرْفَة بَارِدَة جِدًّا.", "The room is very cold.", "بَارِدَة"),
                 ex("لَا يُوجَد مَاء سَاخِن فِي الْحَمَّام.", "There is no hot water in the bathroom.", "لَا يُوجَد"),
                 ex("الْغُرْفَة غَيْر نَظِيفَة.", "The room is not clean.", "غَيْر نَظِيفَة"),
                 ex("هُنَاكَ ضَجِيج فِي الْمَمَرّ.", "There is noise in the corridor.", "ضَجِيج"),
                 ex("هَلْ يُمْكِن إِصْلَاح الْمُكَيِّف؟", "Can the air conditioner be repaired?", "إِصْلَاح"),
                 ex("أُرِيد غُرْفَة أُخْرَى مِنْ فَضْلِكَ.", "I want another room, please.", "غُرْفَة أُخْرَى"),
             ]),
    ],
    exercises=[
        M("What does الْمُكَيِّف لَا يَعْمَل mean?", "The air conditioner does not work", ["The air conditioner is new", "The air conditioner is cold", "The air conditioner is expensive"], "لَا يَعْمَل = does not work."),
        M("What does غَيْر نَظِيفَة mean?", "not clean", ["very clean", "big", "cold"], "غَيْر = not."),
        M("What does لَا يُوجَد مَاء سَاخِن mean?", "There is no hot water", ["There is hot water", "The water is cold", "I want hot water"], "لَا يُوجَد = there is not."),
        M("What does هُنَاكَ ضَجِيج mean?", "There is noise", ["There is a window", "There is a key", "There is a bed"], "ضَجِيج = noise."),
        M("What does هَلْ يُمْكِن إِصْلَاح الْمُكَيِّف؟ ask?", "Can the air conditioner be repaired?", ["Is the air conditioner new?", "Where is the air conditioner?", "Who broke the air conditioner?"], "إِصْلَاح = repair."),
        M("Which is correct for the television, which is masculine (تِلْفَاز)?", "لَا يَعْمَل", ["لَا تَعْمَل", "both are fine", "neither is fine"], "A masculine thing takes يَـ."),
        F("الْمُكَيِّف ___ يَعْمَل.", "لَا", ["لَنْ", "هَلْ"], "“does not”.", tr="The air conditioner does not work."),
        F("الْغُرْفَة ___ نَظِيفَة.", "غَيْر", ["لَيْسَ", "مِثْل"], "“not clean”: غَيْر نَظِيفَة.", tr="The room is not clean."),
        F("أُرِيد غُرْفَة ___ مِنْ فَضْلِكَ.", "أُخْرَى", ["آخَر", "أُخْرَيَات"], "Feminine: أُخْرَى.", tr="I want another room, please."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 378
L378 = lesson(
    "Apologising and accepting an apology",
    "أَعْتَذِر عَنِ الْإِزْعَاج · لَا بَأْس",
    requires=["أسف", "مشكلة", "شكر", "مدير", "فندق", "قبل", "خطأ"],
    cards=[
        card("Ways to say sorry",
             "The simplest apology is آسِف (a man) or آسِفَة (a woman). More formally say أَعْتَذِر عَنْ …, “I apologise for …”. To accept an apology say لَا بَأْس or لَا مُشْكِلَة, “no problem”, or أَقْبَل اِعْتِذَارَكَ, “I accept your apology”. "
             "A polite answer to a request is بِكُلّ سُرُور, “with pleasure”.",
             tables=[table(["Situation", "Arabic", "English"],
                           [["sorry (m.)", "آسِف", "I am sorry"], ["sorry (f.)", "آسِفَة", "I am sorry"], ["formal apology", "أَعْتَذِر عَنِ الْإِزْعَاج", "I apologise for the inconvenience"], ["accepting", "لَا بَأْس", "no harm done"], ["accepting", "أَقْبَل اِعْتِذَارَكَ", "I accept your apology"], ["agreeing to help", "بِكُلّ سُرُور", "with pleasure"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("At the desk (invented)",
             "A manager talks to a guest.",
             examples=[
                 ex("أَعْتَذِر عَنِ الْإِزْعَاج.", "I apologise for the inconvenience.", "أَعْتَذِر"),
                 ex("لَا بَأْس، لَا مُشْكِلَة.", "It’s all right, no problem.", "لَا بَأْس"),
                 ex("أَقْبَل اِعْتِذَارَكَ، شُكْرًا.", "I accept your apology, thank you.", "أَقْبَل"),
                 ex("هَلْ يُمْكِنُكَ تَغْيِير الْغُرْفَة؟ بِكُلّ سُرُور.", "Can you change the room? With pleasure.", "بِكُلّ سُرُور"),
                 ex("آسِفَة، تَأَخَّرْتُ عَنِ الْمَوْعِد.", "Sorry, I was late for the appointment (a woman speaking).", "آسِفَة"),
                 ex("أَرْجُو أَنْ تَقْبَلَ اِعْتِذَارِي.", "I hope you will accept my apology.", "اِعْتِذَارِي"),
             ]),
    ],
    exercises=[
        M("What does أَعْتَذِر mean?", "I apologise", ["I thank", "I arrive", "I count"], "اِعْتَذَرَ = to apologise."),
        M("What does لَا بَأْس mean?", "no harm done", ["never again", "not today", "I do not know"], "لَا بَأْس = it’s all right."),
        M("What does بِكُلّ سُرُور mean?", "with pleasure", ["with sorrow", "with no money", "with a key"], "سُرُور = pleasure."),
        M("Who says آسِفَة?", "a woman", ["a man", "two men", "a child only"], "The ـَة ending is feminine."),
        M("What does أَقْبَل اِعْتِذَارَكَ mean?", "I accept your apology", ["I refuse your apology", "I forgot your apology", "I read your apology"], "قَبِلَ = to accept."),
        M("Which phrase is formal?", "أَعْتَذِر عَنِ الْإِزْعَاج", ["آسِف", "لَا بَأْس", "تَفَضَّلْ"], "أَعْتَذِر عَنْ … is the formal way."),
        F("___ عَنِ الْإِزْعَاج.", "أَعْتَذِر", ["اِعْتَذَرَ", "يَعْتَذِر"], "“I apologise”: أَعْتَذِر.", tr="I apologise for the inconvenience."),
        F("لَا ___.", "بَأْس", ["مَال", "فَرْد"], "A fixed phrase.", tr="It’s all right."),
        F("أَقْبَل ___ شُكْرًا.", "اِعْتِذَارَكَ", ["اِعْتِذَارِي", "اِعْتَذَرْتُ"], "“your apology” (to a man): اِعْتِذَارَكَ.", tr="I accept your apology, thank you."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 379
L379 = lesson(
    "Suggesting, agreeing, disagreeing",
    "أَقْتَرِح أَنْ نَذْهَب · أَنَا مُوَافِق · لَا أُوَافِق",
    requires=["رأي", "موافق", "فكرة", "أول", "وقت", "جميل", "جيد"],
    cards=[
        card("Giving your view",
             "To make a suggestion say أَقْتَرِح أَنْ …, “I suggest that …”. To agree say أَنَا مُوَافِق; to disagree say لَا أُوَافِق or أَنَا غَيْر مُوَافِق. "
             "Give your view with فِي رَأْيِي, “in my opinion”, and speak with confidence with أَنَا وَاثِق مِنْ ذَلِكَ, “I am sure of that”. In a group, say نُوَافِق or لَا نُوَافِق.",
             tables=[table(["English", "Arabic"],
                           [["I suggest", "أَقْتَرِح"], ["I agree", "أَنَا مُوَافِق"], ["I do not agree", "لَا أُوَافِق"], ["in my opinion", "فِي رَأْيِي"], ["I am sure of that", "أَنَا وَاثِق مِنْ ذَلِكَ"], ["a good idea", "فِكْرَة جَيِّدَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A talk between friends (invented)",
             "Friends plan a day.",
             examples=[
                 ex("أَقْتَرِح أَنْ نَذْهَب إِلَى الْمَتْحَف أَوَّلًا.", "I suggest that we go to the museum first.", "أَقْتَرِح"),
                 ex("أَنَا مُوَافِق، هَذِهِ فِكْرَة جَيِّدَة.", "I agree, this is a good idea.", "مُوَافِق"),
                 ex("لَا أُوَافِق، الْوَقْت قَصِير.", "I do not agree, the time is short.", "لَا أُوَافِق"),
                 ex("فِي رَأْيِي، الْفُنْدُق الْجَدِيد أَفْضَل.", "In my opinion, the new hotel is better.", "فِي رَأْيِي"),
                 ex("أَنَا وَاثِق مِنْ ذَلِكَ.", "I am sure of that.", "وَاثِق"),
                 ex("هَلْ تُوَافِقُون؟ نَعَمْ، نُوَافِق.", "Do you agree? Yes, we agree.", "نُوَافِق"),
             ]),
    ],
    exercises=[
        M("What does أَقْتَرِح أَنْ نَذْهَب mean?", "I suggest that we go", ["I refuse to go", "I went yesterday", "I will not go"], "اِقْتَرَحَ = to suggest."),
        M("What does أَنَا مُوَافِق mean?", "I agree", ["I disagree", "I am late", "I am sorry"], "مُوَافِق = in agreement."),
        M("What does لَا أُوَافِق mean?", "I do not agree", ["I agree", "I do not know", "I will come"], "لَا + present = do not."),
        M("What does فِي رَأْيِي mean?", "in my opinion", ["in my house", "in my room", "in my car"], "رَأْيِي = my opinion."),
        M("What does أَنَا وَاثِق مِنْ ذَلِكَ mean?", "I am sure of that", ["I am afraid of that", "I forgot that", "I want that"], "وَاثِق = confident."),
        M("Who says هَلْ تُوَافِقُون؟", "someone speaking to a group", ["someone speaking to one man", "someone speaking to one woman", "someone speaking alone"], "تُوَافِقُون = you (plural)."),
        F("___ أَنْ نَذْهَب إِلَى الْمَتْحَف.", "أَقْتَرِح", ["اِقْتَرَحَ", "يَقْتَرِح"], "“I suggest”: أَقْتَرِح.", tr="I suggest that we go to the museum."),
        F("___ رَأْيِي، الْفُنْدُق الْجَدِيد أَفْضَل.", "فِي", ["مِنْ", "عَنْ"], "“in my opinion”: فِي رَأْيِي.", tr="In my opinion, the new hotel is better."),
        F("لَا ___، الْوَقْت قَصِير.", "أُوَافِق", ["وَافَقْتُ", "يُوَافِق"], "“I do not agree”: لَا أُوَافِق.", tr="I do not agree, the time is short.", lemma="وفق#3:pres:ana"),
    ],
    verify=vv("وفق#3", "pres", ana="أُوَافِق", nahnu="نُوَافِق"),
)


# ---------------------------------------------------------------------------- 380
L380 = lesson(
    "Commands from Measures II and III",
    "وَقِّعْ · قَدِّمْ · سَاعِدْ · رَاجِعْ",
    requires=["وقع", "قدم", "ساعد", "راجع", "سافر", "شاهد", "جواز", "مدير"],
    cards=[
        card("Take off the prefix",
             "To make a command from Measures II and III, start from the present tense. Drop the prefix يُـ, then put a sukūn on the last letter. "
             "So يُوَقِّعُ becomes وَقِّعْ, “sign!”, and يُسَاعِدُ becomes سَاعِدْ, “help!”. For a woman add ـِي, for a group add ـُوا. No helping alif is needed, because the verb already starts with a vowel.",
             tables=[table(["Measure", "Present", "Command (to a man)", "English"],
                           [["II", "يُوَقِّع", "وَقِّعْ", "sign"], ["II", "يُقَدِّم", "قَدِّمْ", "present, hand over"], ["II", "يُسَجِّل", "سَجِّلْ", "register"], ["II", "يُرَتِّب", "رَتِّبْ", "arrange"],
                            ["III", "يُسَاعِد", "سَاعِدْ", "help"], ["III", "يُرَاجِع", "رَاجِعْ", "review, check"], ["III", "يُسَافِر", "سَافِرْ", "travel"], ["III", "يُشَاهِد", "شَاهِدْ", "watch"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("To a woman and to a group (invented)",
             "Commands to a man, to a woman and to a group.",
             examples=[
                 ex("قَدِّمْ جَوَازَكَ لِلْمُوَظَّف.", "Hand your passport to the clerk.", "قَدِّمْ"),
                 ex("سَجِّلِي الْحَجْز يَا سَلْمَى.", "Register the booking, Salma.", "سَجِّلِي"),
                 ex("رَاجِعُوا الْحِسَاب قَبْلَ الْمُغَادَرَة.", "Check the bill before leaving.", "رَاجِعُوا"),
                 ex("سَاعِدُوا الضُّيُوف مِنْ فَضْلِكُمْ.", "Help the guests, please (to a group).", "سَاعِدُوا"),
                 ex("سَافِرْ بِالْقِطَار يَا سَالِم.", "Travel by train, Salem.", "سَافِرْ"),
                 ex("شَاهِدِي الْمَدِينَة مِنَ النَّافِذَة.", "Watch the city from the window (to a woman).", "شَاهِدِي"),
             ]),
    ],
    exercises=[
        M("What does وَقِّعْ mean?", "sign!", ["wait!", "write!", "pay!"], "A command from Measure II."),
        M("Which is the command from يُسَاعِد?", "سَاعِدْ", ["أَسَاعِد", "مُسَاعِد", "سَاعَدَ"], "Drop يُـ and add a sukūn."),
        M("How do you tell a woman to register the booking?", "سَجِّلِي الْحَجْز", ["سَجِّلِ الْحَجْز", "سَجِّلُوا الْحَجْز", "سَجَّلَتِ الْحَجْز"], "ـِي marks a woman."),
        M("What does رَاجِعُوا الْحِسَاب mean?", "Check the bill (to a group)", ["Pay the bill (to one man)", "I checked the bill", "The bill is long"], "ـُوا marks a group."),
        M("Which Measure is سَافِرْ?", "III", ["II", "IV", "V"], "سَافَرَ has a long vowel after the first root letter."),
        M("What do you say to a man?", "قَدِّمْ جَوَازَكَ", ["قَدِّمِي جَوَازَكِ", "قَدِّمُوا جَوَازَكُمْ", "قَدَّمَ جَوَازَهُ"], "A bare command with ـَكَ."),
        F("___ الْحَجْز يَا سَلْمَى.", "سَجِّلِي", ["سَجِّلْ", "سَجِّلُوا"], "A woman is addressed, so ـِي.", tr="Register the booking, Salma.", lemma="سجل#2:imp:anti"),
        F("___ الضُّيُوف مِنْ فَضْلِكُمْ.", "سَاعِدُوا", ["سَاعِدْ", "سَاعِدِي"], "A group is addressed, so ـُوا.", tr="Help the guests, please.", lemma="سعد#3:imp:antum"),
        F("___ جَوَازَكَ لِلْمُوَظَّف.", "قَدِّمْ", ["قَدَّمَ", "يُقَدِّم"], "A command to one man.", tr="Hand your passport to the clerk.", lemma="قدم#2:imp:anta"),
        F("___ الْمَدِينَة مِنَ النَّافِذَة.", "شَاهِدِي", ["شَاهِدْ", "شَاهِدُوا"], "A woman is addressed.", tr="Watch the city from the window (to a woman).", lemma="شهد#3:imp:anti"),
    ],
    verify=(vv("وقع#2", "imp", anta="وَقِّعْ", anti="وَقِّعِي", antum="وَقِّعُوا") + vv("سعد#3", "imp", anta="سَاعِدْ", antum="سَاعِدُوا") + vv("سجل#2", "imp", anti="سَجِّلِي")
            + vv("قدم#2", "imp", anta="قَدِّمْ") + vv("رجع#3", "imp", antum="رَاجِعُوا") + vv("سفر#3", "imp", anta="سَافِرْ") + vv("شهد#3", "imp", anti="شَاهِدِي")),
)

# ---------------------------------------------------------------------------- 381
L381 = lesson(
    "Commands from Measures IV, V and VI",
    "أَرْسِلْ · تَكَلَّمْ · تَقَابَلْ",
    requires=["أرسل", "أخبر", "أحضر", "أدخل", "أخرج", "تكلم", "تعلم", "تذكر", "رسالة", "موعد"],
    cards=[
        card("Measure IV keeps its hamza",
             "In Measure IV the present is يُرْسِلُ. For the command the prefix goes, but the verb starts again with أَ (a hamza with a fatḥa), and the second letter has a kasra: أَرْسِلْ, “send!”. "
             "This hamza is always pronounced, so it never loses its sound inside a sentence.",
             tables=[table(["Present", "Command", "English"],
                           [["يُرْسِل", "أَرْسِلْ", "send"], ["يُخْبِر", "أَخْبِرْ", "inform, tell"], ["يُحْضِر", "أَحْضِرْ", "bring"], ["يُدْخِل", "أَدْخِلْ", "put in, let in"], ["يُخْرِج", "أَخْرِجْ", "take out"], ["يُكْمِل", "أَكْمِلْ", "finish, continue"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Measures V and VI keep their ت",
             "In Measures V and VI the present is يَتَكَلَّمُ and يَتَقَابَلُ. For the command, drop only the يَـ and keep the تَـ: تَكَلَّمْ, “speak!”, and تَقَابَلْ, “meet!”. "
             "The command from these two measures looks like the past tense of the same verb without its ending; the vowels of the last letters tell them apart.",
             tables=[table(["Measure", "Command", "English"],
                           [["V", "تَكَلَّمْ", "speak"], ["V", "تَعَلَّمْ", "learn"], ["V", "تَذَكَّرْ", "remember"], ["V", "تَحَرَّكْ", "move"], ["VI", "تَقَابَلْ", "meet"], ["VI", "تَسَاعَدْ", "help each other"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences (invented)",
             "Short orders and requests.",
             examples=[
                 ex("أَرْسِلْ هَذِهِ الرِّسَالَة الْيَوْم.", "Send this letter today.", "أَرْسِلْ"),
                 ex("أَخْبِرِ الْمُدِير عَنِ الْمَوْعِد.", "Tell the manager about the appointment.", "أَخْبِرِ"),
                 ex("أَحْضِرُوا جَوَازَاتِكُمْ إِلَى الْمَكْتَب.", "Bring your passports to the office.", "أَحْضِرُوا"),
                 ex("تَكَلَّمْ مَعَ الْمُدِير.", "Speak with the manager.", "تَكَلَّمْ"),
                 ex("تَذَكَّرِي مَوْعِدَكِ يَا هِنْد.", "Remember your appointment, Hind.", "تَذَكَّرِي"),
                 ex("تَقَابَلُوا فِي الْفُنْدُق السَّاعَة الْعَاشِرَة.", "Meet at the hotel at ten o’clock.", "تَقَابَلُوا"),
             ]),
    ],
    exercises=[
        M("What is the command from يُرْسِل?", "أَرْسِلْ", ["يُرْسِلْ", "رَاسِلْ", "تَرْسِلْ"], "Measure IV starts the command with أَ."),
        M("What does أَحْضِرُوا جَوَازَاتِكُمْ mean?", "Bring your passports (to a group)", ["Bring your passport (to one man)", "I brought the passports", "The passports are here"], "ـُوا marks a group."),
        M("What is the command from يَتَكَلَّم?", "تَكَلَّمْ", ["يَكَلَّمْ", "كَلِّمْ", "أَتَكَلَّمْ"], "Drop يَـ and keep تَـ."),
        M("What does أَخْبِرْ mean?", "tell, inform", ["ask", "leave", "take"], "Measure IV of خَبَر."),
        M("Which command is from Measure VI?", "تَقَابَلْ", ["أَرْسِلْ", "وَقِّعْ", "تَكَلَّمْ"], "Measure VI has the prefix تَ and a long vowel after the first root letter."),
        M("What does تَذَكَّرِي mean?", "Remember! (to a woman)", ["Forget! (to a woman)", "I remember", "He remembers"], "ـِي marks a woman."),
        F("___ هَذِهِ الرِّسَالَة الْيَوْم.", "أَرْسِلْ", ["رَسِّلْ", "يُرْسِل"], "A command from Measure IV.", tr="Send this letter today.", lemma="رسل#4:imp:anta"),
        F("___ مَعَ الْمُدِير.", "تَكَلَّمْ", ["كَلِّمْ", "يَتَكَلَّم"], "A command from Measure V.", tr="Speak with the manager.", lemma="كلم#5:imp:anta"),
        F("___ فِي الْفُنْدُق السَّاعَة الْعَاشِرَة.", "تَقَابَلُوا", ["تَقَابَلْ", "تَقَابَلِي"], "A group is addressed.", tr="Meet at the hotel at ten o’clock.", lemma="قبل#6:imp:antum"),
        F("___ مَوْعِدَكِ يَا هِنْد.", "تَذَكَّرِي", ["تَذَكَّرْ", "تَذَكَّرُوا"], "A woman is addressed.", tr="Remember your appointment, Hind.", lemma="ذكر#5:imp:anti"),
    ],
    verify=(vv("رسل#4", "imp", anta="أَرْسِلْ", antum="أَرْسِلُوا") + vv("خبر#4", "imp", anta="أَخْبِرْ") + vv("حضر#4", "imp", antum="أَحْضِرُوا") + vv("كلم#5", "imp", anta="تَكَلَّمْ")
            + vv("ذكر#5", "imp", anti="تَذَكَّرِي") + vv("قبل#6", "imp", anta="تَقَابَلْ", antum="تَقَابَلُوا") + vv("علم#5", "imp", anta="تَعَلَّمْ") + vv("حرك#5", "imp", anta="تَحَرَّكْ")),
)

# ---------------------------------------------------------------------------- 382
L382 = lesson(
    "Commands from Measures VII, VIII and X",
    "اِنْتَظِرْ · اِسْتَمِعْ · اِسْتَخْدِمْ",
    requires=["جمع", "نقل", "عمل", "قبل", "مدير", "مصعد", "موعد", "مكتب"],
    cards=[
        card("The helping alif returns",
             "Measures VII, VIII and X begin with a helping alif (hamzat wasl) in the past tense. The present has no such alif: يَنْتَظِرُ, يَسْتَخْدِمُ. "
             "For the command, drop the prefix يَـ, and a helping alif with a kasra is added: اِنْتَظِرْ, “wait!”, اِسْتَخْدِمْ, “use!”. The alif is pronounced only at the start of a sentence. After another word it is silent: ثُمَّ اِنْتَظِرْ is said thumma ntaẓir.",
             tables=[table(["Measure", "Command", "English"],
                           [["VII", "اِنْطَلِقْ", "set off"], ["VII", "اِنْصَرِفْ", "leave, go away"], ["VIII", "اِنْتَظِرْ", "wait"], ["VIII", "اِسْتَمِعْ", "listen"], ["VIII", "اِقْتَرِحْ", "suggest"],
                            ["VIII", "اِجْتَمِعْ", "meet, gather"], ["VIII", "اِنْتَقِلْ", "move (to)"], ["X", "اِسْتَخْدِمْ", "use"], ["X", "اِسْتَقْبِلْ", "receive, welcome"], ["X", "اِسْتَعْمِلْ", "use"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Before the article (invented)",
             "A command that ends in a consonant takes a helping kasra before الـ: اِسْتَخْدِمِ الْمِصْعَد.",
             examples=[
                 ex("اِنْتَظِرْ فِي الْمَكْتَب مِنْ فَضْلِكَ.", "Wait in the office, please.", "اِنْتَظِرْ"),
                 ex("اِسْتَمِعْ إِلَى الْمُدِير.", "Listen to the manager.", "اِسْتَمِعْ"),
                 ex("اِسْتَخْدِمِ الْمِصْعَد.", "Use the elevator.", "اِسْتَخْدِمِ"),
                 ex("اِقْتَرِحْ مَوْعِدًا آخَر.", "Suggest another time.", "اِقْتَرِحْ"),
                 ex("اِسْتَقْبِلُوا الضُّيُوف عِنْدَ الْبَاب.", "Welcome the guests at the door.", "اِسْتَقْبِلُوا"),
                 ex("اِنْتَقِلِي إِلَى غُرْفَة أُخْرَى.", "Move to another room (to a woman).", "اِنْتَقِلِي"),
             ]),
    ],
    exercises=[
        M("What does اِنْتَظِرْ mean?", "wait!", ["listen!", "leave!", "use!"], "From يَنْتَظِر, Measure VIII."),
        M("Which command is from Measure X?", "اِسْتَخْدِمْ", ["اِنْتَظِرْ", "اِجْتَمِعْ", "اِنْطَلِقْ"], "اِسْتَخْدِمْ adds the prefix اِسْتَ to the root خ-د-م."),
        M("What does اِسْتَمِعْ إِلَى الْمُدِير mean?", "Listen to the manager", ["Speak to the manager", "Wait for the manager", "Call the manager"], "اِسْتَمَعَ إِلَى = to listen to."),
        M("What is the helping vowel in اِسْتَخْدِمِ الْمِصْعَد?", "a kasra before الـ", ["a fatḥa before الـ", "a dammah before الـ", "no vowel"], "A final sukūn before الـ takes a helping kasra."),
        M("How do you say “Welcome the guests” to a group?", "اِسْتَقْبِلُوا الضُّيُوف", ["اِسْتَقْبِلِ الضُّيُوف", "اِسْتَقْبِلِي الضُّيُوف", "يَسْتَقْبِلُون الضُّيُوف"], "ـُوا marks a group."),
        M("Is the alif of اِنْتَظِرْ pronounced after ثُمَّ?", "no, it is silent", ["yes, always", "only for women", "only in questions"], "A helping alif is silent after another word."),
        F("___ فِي الْمَكْتَب مِنْ فَضْلِكَ.", "اِنْتَظِرْ", ["اِنْتَظَرَ", "يَنْتَظِر"], "A command from Measure VIII.", tr="Wait in the office, please.", lemma="نظر#8:imp:anta"),
        F("اِسْتَخْدِمِ ___.", "الْمِصْعَد", ["مِصْعَد", "الْمِصْعَدِ"], "The article is needed after a command meaning “use the …”.", tr="Use the elevator."),
        F("___ الضُّيُوف عِنْدَ الْبَاب.", "اِسْتَقْبِلُوا", ["اِسْتَقْبِلْ", "اِسْتَقْبِلِي"], "A group is addressed.", tr="Welcome the guests at the door.", lemma="قبل#10:imp:antum"),
        F("___ إِلَى غُرْفَة أُخْرَى.", "اِنْتَقِلِي", ["اِنْتَقِلْ", "اِنْتَقِلُوا"], "A woman is addressed.", tr="Move to another room (to a woman).", lemma="نقل#8:imp:anti"),
    ],
    verify=(vv("نظر#8", "imp", anta="اِنْتَظِرْ", anti="اِنْتَظِرِي") + vv("سمع#8", "imp", anta="اِسْتَمِعْ") + vv("خدم#10", "imp", anta="اِسْتَخْدِمْ") + vv("قرح#8", "imp", anta="اِقْتَرِحْ")
            + vv("قبل#10", "imp", antum="اِسْتَقْبِلُوا") + vv("نقل#8", "imp", anti="اِنْتَقِلِي") + vv("طلق#7", "imp", anta="اِنْطَلِقْ") + vv("صرف#7", "imp", anta="اِنْصَرِفْ")
            + vv("جمع#8", "imp", anta="اِجْتَمِعْ") + vv("عمل#10", "imp", anta="اِسْتَعْمِلْ")),
)

# ---------------------------------------------------------------------------- 383
L383 = lesson(
    "Pairs, women and ‘do not’",
    "أَرْسِلَا · أَرْسِلْنَ · لَا تُرْسِلْ",
    requires=["أرسل", "رسالة", "فاتورة", "حقيبة", "باب", "مدير", "ساعد", "قدم"],
    cards=[
        card("One verb, five commands",
             "Every command has five forms. Here is أَرْسِلْ in all of them. The pair ends in ـَا, and a group of women ends in ـْنَ.",
             tables=[table(["To", "Command", "English"],
                           [["one man", "أَرْسِلْ", "send"], ["one woman", "أَرْسِلِي", "send"], ["two people", "أَرْسِلَا", "send"], ["a group of men", "أَرْسِلُوا", "send"], ["a group of women", "أَرْسِلْنَ", "send"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Objects and ‘do not’",
             "A pronoun can be attached to the end of a command: سَاعِدْنِي, “help me”; أَرْسِلْهَا, “send it (f.)”; قَدِّمْهُ, “present it”. "
             "To forbid, put لَا before a short present form, which looks like the command with a prefix: لَا تُرْسِلْ, “do not send”; لَا تُوَقِّعْ, “do not sign”.",
             examples=[
                 ex("أَرْسِلَا الْحَقَائِب إِلَى الْغُرْفَة.", "Send the bags to the room (to two people).", "أَرْسِلَا"),
                 ex("أَرْسِلْنَ الرِّسَالَة يَا بَنَات.", "Send the letter, girls.", "أَرْسِلْنَ"),
                 ex("سَاعِدْنِي مِنْ فَضْلِكَ.", "Help me, please.", "سَاعِدْنِي"),
                 ex("الْفَاتُورَة جَاهِزَة، أَرْسِلْهَا إِلَى الْمُدِير.", "The bill is ready, send it to the manager.", "أَرْسِلْهَا"),
                 ex("لَا تُرْسِلْ هَذِهِ الرِّسَالَة.", "Do not send this letter.", "لَا تُرْسِلْ"),
                 ex("لَا تُوَقِّعْ هُنَا.", "Do not sign here.", "لَا تُوَقِّعْ"),
             ]),
    ],
    exercises=[
        M("Who is addressed in أَرْسِلَا?", "two people", ["one man", "one woman", "a group of women"], "ـَا marks the dual."),
        M("Who is addressed in أَرْسِلْنَ?", "a group of women", ["a group of men", "two men", "one woman"], "ـْنَ marks feminine plural."),
        M("What does سَاعِدْنِي mean?", "help me", ["help him", "he helped", "I help"], "ـنِي = me."),
        M("What does أَرْسِلْهَا mean?", "send it (f.)", ["send him", "she sent", "do not send"], "ـهَا = her, it (f.)."),
        M("What does لَا تُوَقِّعْ هُنَا mean?", "Do not sign here", ["Sign here", "I did not sign", "He will sign"], "لَا + short present = do not."),
        M("How do you tell a man, “Do not send”?", "لَا تُرْسِلْ", ["لَا أَرْسِلْ", "لَا يُرْسِلْ", "مَا تُرْسِلُ"], "لَا + تُرْسِلْ."),
        F("___ الْحَقَائِب إِلَى الْغُرْفَة.", "أَرْسِلَا", ["أَرْسِلْ", "أَرْسِلْنَ"], "Two people are addressed.", tr="Send the bags to the room.", lemma="رسل#4:imp:antuma"),
        F("___ الرِّسَالَة يَا بَنَات.", "أَرْسِلْنَ", ["أَرْسِلُوا", "أَرْسِلِي"], "Girls are addressed.", tr="Send the letter, girls.", lemma="رسل#4:imp:antunna"),
        F("الْفَاتُورَة جَاهِزَة، ___ إِلَى الْمُدِير.", "أَرْسِلْهَا", ["أَرْسِلْنِي", "أَرْسِلْهُ"], "The bill (فَاتُورَة) is feminine: ـهَا.", tr="The bill is ready, send it to the manager."),
        F("لَا ___ هَذِهِ الرِّسَالَة.", "تُرْسِلْ", ["أَرْسِلْ", "تُرْسِلُ"], "After لَا, a short present form.", tr="Do not send this letter."),
    ],
    verify=(vv("رسل#4", "imp", anta="أَرْسِلْ", anti="أَرْسِلِي", antuma="أَرْسِلَا", antum="أَرْسِلُوا", antunna="أَرْسِلْنَ") + vv("رسل#4", "neg", anta="لَا تُرْسِلْ") + vv("وقع#2", "neg", anta="لَا تُوَقِّعْ")),
)

# ---------------------------------------------------------------------------- 384
L384 = lesson(
    "Checking out",
    "أُرِيد الْمُغَادَرَة غَدًا · أَرْسِلِ الْفَاتُورَة",
    requires=["فاتورة", "حقيبة", "بطاقة", "سيارة", "لحظة", "مغادرة", "غرفة", "مفتاح", "شكر", "مدير"],
    cards=[
        card("At the desk (invented)",
             "A guest leaves the hotel in the morning. Notice the commands.",
             tables=[table(["English", "Arabic"],
                           [["check-out", "الْمُغَادَرَة"], ["the bill", "الْفَاتُورَة"], ["credit card", "بِطَاقَة الِائْتِمَان"], ["a taxi", "سَيَّارَة أُجْرَة"], ["one moment", "لَحْظَة"], ["luggage", "الْحَقَائِب"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("صَبَاح الْخَيْر، أُرِيد الْمُغَادَرَة.", "Good morning, I want to check out.", "الْمُغَادَرَة"),
                 ex("اِنْتَظِرْ لَحْظَة، أُحْضِر لَكَ الْفَاتُورَة.", "Wait a moment, I will bring you the bill.", "اِنْتَظِرْ"),
                 ex("رَاجِعِ الْفَاتُورَة ثُمَّ وَقِّعْ هُنَا.", "Check the bill, then sign here.", "رَاجِعِ"),
                 ex("سَأَدْفَع بِبِطَاقَة الِائْتِمَان.", "I will pay by credit card.", "سَأَدْفَع"),
                 ex("أَحْضِرُوا حَقَائِبِي مِنَ الْغُرْفَة.", "Bring my bags from the room (to the staff).", "أَحْضِرُوا"),
                 ex("اُطْلُبْ لِي سَيَّارَة أُجْرَة مِنْ فَضْلِكَ.", "Order me a taxi, please.", "اُطْلُبْ"),
             ]),
        card("A thank-you note (invented)",
             "Before leaving, a guest writes to the manager. Letters begin with the address and end with thanks.",
             examples=[
                 ex("إِلَى مُدِير الْفُنْدُق، تَحِيَّة طَيِّبَة.", "To the hotel manager, kind greetings.", "تَحِيَّة طَيِّبَة"),
                 ex("أَشْكُرُكَ عَلَى إِقَامَة جَمِيلَة.", "I thank you for a lovely stay.", "أَشْكُرُكَ"),
                 ex("أَرْجُو أَنْ تُرْسِلَ الْفَاتُورَة إِلَى عُنْوَانِي.", "Please send the bill to my address.", "أَنْ تُرْسِلَ"),
                 ex("مَعَ أَطْيَب التَّمَنِّيَات.", "With best wishes.", "التَّمَنِّيَات"),
             ]),
    ],
    exercises=[
        M("What does أُرِيد الْمُغَادَرَة mean?", "I want to check out", ["I want a room", "I want a key", "I want a taxi"], "مُغَادَرَة = leaving."),
        M("What does اِنْتَظِرْ لَحْظَة mean?", "Wait a moment", ["Come back tomorrow", "Pay now", "Sign here"], "لَحْظَة = a moment."),
        M("What does رَاجِعِ الْفَاتُورَة mean?", "Check the bill", ["Pay the bill", "Tear the bill", "Send the bill"], "رَاجِعْ = check!, with a helping kasra before الـ."),
        M("What does سَأَدْفَع بِبِطَاقَة الِائْتِمَان mean?", "I will pay by credit card", ["I paid in cash", "I lost my card", "I want a card"], "سَـ = will."),
        M("Who is addressed in أَحْضِرُوا حَقَائِبِي?", "a group", ["one man", "one woman", "two women"], "ـُوا marks a group."),
        M("What does مَعَ أَطْيَب التَّمَنِّيَات mean?", "with best wishes", ["with kind greetings", "with many thanks", "with apologies"], "A closing wish in a letter."),
        F("اِنْتَظِرْ ___، أُحْضِر لَكَ الْفَاتُورَة.", "لَحْظَة", ["سَنَة", "غُرْفَة"], "“a moment”.", tr="Wait a moment, I will bring you the bill."),
        F("أَحْضِرُوا ___ مِنَ الْغُرْفَة.", "حَقَائِبِي", ["مِفْتَاحِي", "فَاتُورَتِي"], "Luggage is brought from a room.", tr="Bring my bags from the room."),
        F("اُطْلُبْ لِي ___ أُجْرَة مِنْ فَضْلِكَ.", "سَيَّارَة", ["حَقِيبَة", "بِطَاقَة"], "A taxi is سَيَّارَة أُجْرَة.", tr="Order me a taxi, please."),
        F("أَرْجُو أَنْ ___ الْفَاتُورَة إِلَى عُنْوَانِي.", "تُرْسِلَ", ["تُرْسِلُ", "أَرْسِلْ"], "After أَنْ, the subjunctive: ـَ.", tr="Please send the bill to my address."),
    ],
    verify=(vv("رسل#4", "sub", anta="تُرْسِلَ") + vv("حضر#4", "imp", antum="أَحْضِرُوا") + vv("طلب", "imp", anta="اُطْلُبْ") + vv("دفع", "pres", ana="أَدْفَع")),
)


# ---------------------------------------------------------------------------- 385
L385 = lesson(
    "Historic sites and monuments",
    "قَلْعَة · مَعْبَد · قَصْر · جِسْر · سُور",
    requires=["موقع", "أثري", "قلعة", "معبد", "قصر", "جسر", "سور", "بوابة", "متحف", "كنيسة", "مسجد", "دليل", "تذكرة"],
    cards=[
        card("Words for old places",
             "A place where ancient remains lie is a مَوْقِع أَثَرِيّ, “archaeological site”. Around it you may find a castle, a temple, a palace, a bridge, a wall or a gate. "
             "A guide who explains the place is a دَلِيل, and you need a تَذْكِرَة to enter.",
             tables=[table(["English", "Arabic"],
                           [["archaeological site", "مَوْقِع أَثَرِيّ"], ["castle", "قَلْعَة"], ["temple", "مَعْبَد"], ["palace", "قَصْر"], ["bridge", "جِسْر"], ["wall", "سُور"], ["gate", "بَوَّابَة"],
                            ["museum", "مَتْحَف"], ["church", "كَنِيسَة"], ["mosque", "مَسْجِد"], ["guide", "دَلِيل"], ["ticket", "تَذْكِرَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A visit (invented)",
             "A tourist talks to the guide at the entrance.",
             examples=[
                 ex("أُرِيد زِيَارَة الْمَوْقِع الْأَثَرِيّ.", "I want to visit the archaeological site.", "الْمَوْقِع الْأَثَرِيّ"),
                 ex("هَذِهِ الْقَلْعَة قَدِيمَة جِدًّا.", "This castle is very old.", "قَدِيمَة"),
                 ex("لَهَا سُور كَبِير وَبَوَّابَتَان.", "It has a big wall and two gates.", "بَوَّابَتَان"),
                 ex("الدَّلِيل يَتَكَلَّم الْعَرَبِيَّة وَالْإِنْجِلِيزِيَّة.", "The guide speaks Arabic and English.", "الدَّلِيل"),
                 ex("كَمْ سِعْر التَّذْكِرَة؟", "How much is the ticket?", "سِعْر"),
                 ex("الْمَتْحَف مَفْتُوح مِنَ الْعَاشِرَة.", "The museum is open from ten o’clock.", "مَفْتُوح"),
             ]),
    ],
    exercises=[
        M("What is a قَلْعَة?", "a castle", ["a bridge", "a ticket", "a church"], "قَلْعَة = castle, fort."),
        M("What is a سُور?", "a wall", ["a gate", "a palace", "a guide"], "سُور = (city) wall."),
        M("What is a جِسْر?", "a bridge", ["a road", "a mountain", "a mosque"], "جِسْر = bridge."),
        M("What does مَوْقِع أَثَرِيّ mean?", "archaeological site", ["hotel room", "railway station", "customs office"], "أَثَر = remains, trace."),
        M("Who explains the place to visitors?", "الدَّلِيل", ["الْمَتْحَف", "الْجِسْر", "التَّذْكِرَة"], "دَلِيل = guide."),
        M("What does لَهَا سُور كَبِير وَبَوَّابَتَان mean?", "It has a big wall and two gates", ["It has a small wall and one gate", "It is near a big wall", "She has two big bags"], "لَهَا = it has (f.); بَوَّابَتَان = two gates."),
        M("Why is it قَدِيمَة in هَذِهِ الْقَلْعَة قَدِيمَة?", "قَلْعَة is feminine", ["it is a plural", "it is a verb", "it is a question"], "A feminine noun takes a feminine adjective."),
        F("أُرِيد زِيَارَة الْمَوْقِع ___.", "الْأَثَرِيّ", ["الْأَثَرِيَّة", "أَثَرِيّ"], "The noun مَوْقِع is masculine and definite.", tr="I want to visit the archaeological site."),
        F("لَهَا سُور كَبِير وَ___.", "بَوَّابَتَان", ["بَوَّابَة", "بَوَّابُون"], "“two gates”: the dual ـَان.", tr="It has a big wall and two gates."),
        F("كَمْ سِعْر ___؟", "التَّذْكِرَة", ["الْجِسْر", "السُّور"], "You buy a ticket.", tr="How much is the ticket?"),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 386
L386 = lesson(
    "Petra and an old city",
    "تَقَع فِي الْجَنُوب · بُنِيَتْ مُنْذُ زَمَن بَعِيد",
    requires=["مدينة", "جبل", "قبر", "قديم", "طريق", "ضيق", "جنوب", "زائر", "بعيد"],
    cards=[
        card("Where it is and how old it is",
             "To say where a place is, use the verb تَقَع, “is situated”, or تُوجَد, “is found”. To say that a city was built long ago, use the passive بُنِيَتْ, “was built”. "
             "These short texts are invented and simple. Petra is an ancient city in the south of Jordan, with tombs cut into the mountains. Jerusalem has an old city with walls and gates.",
             examples=[
                 ex("تَقَع الْبَتْرَاء فِي جَنُوب الْأُرْدُنّ.", "Petra is situated in the south of Jordan.", "تَقَع"),
                 ex("هِيَ مَدِينَة قَدِيمَة بُنِيَتْ مُنْذُ زَمَن بَعِيد.", "It is an ancient city built a long time ago.", "بُنِيَتْ"),
                 ex("فِي الْجَبَل قُبُور كَثِيرَة.", "In the mountain there are many tombs.", "قُبُور"),
                 ex("يَدْخُل الزُّوَّار مِنْ طَرِيق ضَيِّق بَيْنَ جَبَلَيْن.", "Visitors enter by a narrow road between two mountains.", "جَبَلَيْن"),
                 ex("فِي الْقُدْس مَدِينَة قَدِيمَة لَهَا أَسْوَار وَأَبْوَاب كَثِيرَة.", "In Jerusalem there is an old city with many walls and gates.", "أَسْوَار"),
                 ex("تُوجَد فِيهَا مَسَاجِد وَكَنَائِس وَأَسْوَاق.", "In it there are mosques, churches and markets.", "تُوجَد"),
             ]),
    ],
    exercises=[
        M("What does تَقَع فِي الْجَنُوب mean?", "is situated in the south", ["is far away", "is very old", "is closed"], "تَقَع = is situated."),
        M("What does بُنِيَتْ mean?", "was built", ["was lost", "was closed", "was sold"], "A passive past verb."),
        M("Why is it بُنِيَتْ and not بُنِيَ?", "مَدِينَة is feminine", ["the city is large", "it is a question", "it is a command"], "A feminine subject → ـَتْ."),
        M("What does زَمَن بَعِيد mean?", "a long time ago", ["tomorrow", "this year", "next week"], "بَعِيد = far, distant."),
        M("Who enters by a narrow road?", "الزُّوَّار", ["الْجِبَال", "الْقُبُور", "الْأَسْوَار"], "يَدْخُل الزُّوَّار."),
        M("What does تُوجَد فِيهَا مَسَاجِد mean?", "In it there are mosques", ["It has no mosques", "She visits mosques", "Mosques are closed"], "تُوجَد = there is/are."),
        M("What are أَسْوَار?", "walls", ["gates", "bridges", "tombs"], "The plural of سُور."),
        F("___ الْبَتْرَاء فِي جَنُوب الْأُرْدُنّ.", "تَقَع", ["يَقَع", "وَقَعَ"], "الْبَتْرَاء is feminine: تَـ.", tr="Petra is situated in the south of Jordan.", lemma="وقع:pres:hiya"),
        F("مَدِينَة قَدِيمَة ___ مُنْذُ زَمَن بَعِيد.", "بُنِيَتْ", ["بَنَتْ", "بُنِيَ"], "A passive feminine verb.", tr="An ancient city built a long time ago."),
        F("فِي الْجَبَل ___ كَثِيرَة.", "قُبُور", ["قَبْر", "قَبْرَان"], "Many tombs: the plural.", tr="In the mountain there are many tombs."),
    ],
    verify=(vv("وقع", "pres", hiya="تَقَع")),
)

# ---------------------------------------------------------------------------- 387
L387 = lesson(
    "Hiring a car with a driver",
    "كَمِ الْأُجْرَة؟ · تَوَقَّفْ هُنَا",
    requires=["سيارة", "حافلة", "سائق", "أجرة", "محطة", "موقف", "طريق", "طويل", "نصف", "كبير"],
    cards=[
        card("Talking to the driver",
             "When you hire a car or a van, you ask about the price (الْأُجْرَة) and then tell the driver what to do with commands. "
             "Two verbs are useful: تَوَقَّفْ, “stop!” (Measure V), and اِنْتَظِرْنَا, “wait for us!” (Measure VIII). The ‘do not’ form is لَا تُسْرِعْ, “do not hurry”.",
             examples=[
                 ex("نُرِيد سَيَّارَة كَبِيرَة لِسِتَّة أَشْخَاص.", "We want a big car for six people.", "لِسِتَّة أَشْخَاص"),
                 ex("كَمِ الْأُجْرَة إِلَى الْحُدُود؟", "How much is the fare to the border?", "الْأُجْرَة"),
                 ex("الطَّرِيق طَوِيل، اِذْهَبْ بِسُرْعَة مُعْتَدِلَة.", "The road is long, go at a moderate speed.", "اِذْهَبْ"),
                 ex("تَوَقَّفْ هُنَا مِنْ فَضْلِكَ.", "Stop here, please.", "تَوَقَّفْ"),
                 ex("اِنْتَظِرْنَا نِصْف سَاعَة.", "Wait for us half an hour.", "اِنْتَظِرْنَا"),
                 ex("لَا تُسْرِعْ يَا سَائِق.", "Do not hurry, driver.", "لَا تُسْرِعْ"),
             ]),
    ],
    exercises=[
        M("What does كَمِ الْأُجْرَة؟ mean?", "How much is the fare?", ["Where is the station?", "When does it leave?", "Who is the driver?"], "أُجْرَة = fare, fee."),
        M("What does تَوَقَّفْ هُنَا mean?", "Stop here", ["Come here", "Wait there", "Go away"], "تَوَقَّفَ = to stop (Measure V)."),
        M("What does اِنْتَظِرْنَا mean?", "wait for us", ["wait for him", "they waited", "I am waiting"], "ـنَا = us."),
        M("What does لَا تُسْرِعْ mean?", "do not hurry", ["hurry!", "he hurried", "I will hurry"], "لَا + short present = do not."),
        M("What does نِصْف سَاعَة mean?", "half an hour", ["one hour", "two hours", "a quarter of an hour"], "نِصْف = half."),
        M("Who is the سَائِق?", "the driver", ["the guide", "the clerk", "the guest"], "سَائِق = driver."),
        F("نُرِيد ___ كَبِيرَة لِسِتَّة أَشْخَاص.", "سَيَّارَة", ["سُور", "تَذْكِرَة"], "A car for six people.", tr="We want a big car for six people."),
        F("___ هُنَا مِنْ فَضْلِكَ.", "تَوَقَّفْ", ["تَوَقَّفَ", "يَتَوَقَّف"], "A command to one man.", tr="Stop here, please."),
        F("___ نِصْف سَاعَة.", "اِنْتَظِرْنَا", ["اِنْتَظِرْنِي", "اِنْتَظِرْهُ"], "“wait for us”: ـنَا.", tr="Wait for us half an hour."),
        F("لَا ___ يَا سَائِق.", "تُسْرِعْ", ["تُسْرِعُ", "أَسْرِعْ"], "After لَا, the short present.", tr="Do not hurry, driver."),
    ],
    verify=(vv("وقف#5", "imp", anta="تَوَقَّفْ") + vv("نظر#8", "imp", anta="اِنْتَظِرْ") + vv("سرع#4", "neg", anta="لَا تُسْرِعْ") + vv("ذهب", "imp", anta="اِذْهَبْ")),
)

# ---------------------------------------------------------------------------- 388
L388 = lesson(
    "At passport control",
    "جَوَاز سَفَرِكَ · مَا غَرَض الزِّيَارَة؟",
    requires=["جواز", "غرض", "سياحة", "ختم", "طابور", "صالح", "شهر", "بقي", "موظف"],
    cards=[
        card("The officer’s questions",
             "At the border an officer asks for your passport, جَوَاز السَّفَر, and checks the visa, التَّأْشِيرَة. The usual questions are about the purpose of the visit, غَرَض الزِّيَارَة, and how long you will stay. "
             "The officer stamps the passport with the verb خَتَمَ. This conversation is invented.",
             tables=[table(["English", "Arabic"],
                           [["passport", "جَوَاز سَفَر"], ["visa", "تَأْشِيرَة"], ["purpose", "غَرَض"], ["tourism", "سِيَاحَة"], ["queue", "طَابُور"], ["valid", "صَالِح"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("جَوَاز سَفَرِكَ مِنْ فَضْلِكَ.", "Your passport, please.", "جَوَاز سَفَرِكَ"),
                 ex("مَا غَرَض الزِّيَارَة؟", "What is the purpose of the visit?", "غَرَض"),
                 ex("أَنَا سَائِح، جِئْتُ لِلسِّيَاحَة.", "I am a tourist, I came for tourism.", "جِئْتُ"),
                 ex("كَمْ يَوْمًا سَتَبْقَى هُنَا؟", "How many days will you stay here?", "سَتَبْقَى"),
                 ex("سَأَبْقَى ثَلَاثَة أَيَّام.", "I will stay three days.", "سَأَبْقَى"),
                 ex("التَّأْشِيرَة صَالِحَة لِشَهْر.", "The visa is valid for a month.", "صَالِحَة"),
                 ex("خَتَمَ الْمُوَظَّف الْجَوَاز.", "The officer stamped the passport.", "خَتَمَ"),
             ]),
    ],
    exercises=[
        M("What does جَوَاز سَفَرِكَ mean?", "your passport", ["your ticket", "your visa", "your bag"], "جَوَاز سَفَر = passport."),
        M("What does مَا غَرَض الزِّيَارَة؟ mean?", "What is the purpose of the visit?", ["How long is the visit?", "Where is the hotel?", "Who is your guide?"], "غَرَض = purpose."),
        M("Which answer fits ‘What is the purpose?’", "السِّيَاحَة", ["ثَلَاثَة أَيَّام", "فِي الْفُنْدُق", "جَوَازِي"], "The purpose is tourism."),
        M("What does كَمْ يَوْمًا سَتَبْقَى؟ ask?", "how long you will stay", ["how old you are", "where you live", "how much you pay"], "كَمْ يَوْمًا = how many days."),
        M("What does خَتَمَ الْجَوَاز mean?", "stamped the passport", ["lost the passport", "opened the passport", "read the passport"], "خَتَمَ = to stamp, to seal."),
        M("What does التَّأْشِيرَة صَالِحَة لِشَهْر mean?", "The visa is valid for a month", ["The visa is lost", "The visa costs a month", "The visa is for a week"], "صَالِح = valid."),
        F("جَوَاز ___ مِنْ فَضْلِكَ.", "سَفَرِكَ", ["سَفَرِهِ", "سَفَرِي"], "To a man: your passport.", tr="Your passport, please."),
        F("سَأَبْقَى ثَلَاثَة ___.", "أَيَّام", ["يَوْم", "سَنَة"], "Three days: the plural after ثَلَاثَة.", tr="I will stay three days."),
        F("___ الْمُوَظَّف الْجَوَاز.", "خَتَمَ", ["خَتَمْتُ", "يَخْتِم"], "A past verb for the officer.", tr="The officer stamped the passport.", lemma="ختم:past:huwa"),
        F("التَّأْشِيرَة ___ لِشَهْر.", "صَالِحَة", ["صَالِح", "صَالِحُون"], "التَّأْشِيرَة is feminine.", tr="The visa is valid for a month."),
    ],
    verify=(vv("ختم", "past", huwa="خَتَمَ") + vv("بقي", "fut", huwa="سَيَبْقَى", ana="سَأَبْقَى")),
)

# ---------------------------------------------------------------------------- 389
L389 = lesson(
    "At customs",
    "اِفْتَحْ حَقِيبَتَكَ · هَلْ مَعَكَ شَيْء لِلتَّصْرِيح؟",
    requires=["جمرك", "تفتيش", "تصريح", "هدية", "ممنوع", "حقيبة", "فتح", "ضريبة"],
    cards=[
        card("The customs officer",
             "After passport control, the customs officer, مُوَظَّف الْجُمْرُك, may inspect your bags. He may ask whether you have anything to declare (شَيْء لِلتَّصْرِيح). "
             "A forbidden item is مَمْنُوع, and a tax or fee is ضَرِيبَة. Notice the commands. This conversation is invented.",
             examples=[
                 ex("اِفْتَحْ حَقِيبَتَكَ مِنْ فَضْلِكَ.", "Open your bag, please.", "اِفْتَحْ"),
                 ex("هَلْ مَعَكَ شَيْء لِلتَّصْرِيح؟", "Do you have anything to declare?", "لِلتَّصْرِيح"),
                 ex("لَا، مَعِي هَدَايَا فَقَط.", "No, I only have gifts.", "هَدَايَا"),
                 ex("فَتَّشَ مُوَظَّف الْجُمْرُك الْحَقِيبَة.", "The customs officer searched the bag.", "فَتَّشَ"),
                 ex("هَذَا مَمْنُوع، لَا تَأْخُذْهُ مَعَكَ.", "This is forbidden, do not take it with you.", "مَمْنُوع"),
                 ex("عَلَيْكَ أَنْ تَدْفَعَ ضَرِيبَة.", "You must pay a tax.", "ضَرِيبَة"),
             ]),
    ],
    exercises=[
        M("What does اِفْتَحْ حَقِيبَتَكَ mean?", "Open your bag", ["Close your bag", "Carry your bag", "Lose your bag"], "اِفْتَحْ = open! (to one man)."),
        M("What does لِلتَّصْرِيح mean here?", "to declare", ["to forbid", "to hire", "to sign"], "تَصْرِيح = declaration."),
        M("What does مَمْنُوع mean?", "forbidden", ["free", "heavy", "delicious"], "مَمْنُوع = not allowed."),
        M("What does فَتَّشَ الْحَقِيبَة mean?", "searched the bag", ["bought the bag", "carried the bag", "forgot the bag"], "فَتَّشَ = to search (Measure II)."),
        M("What does لَا تَأْخُذْهُ مَعَكَ mean?", "do not take it with you", ["take it with you", "he took it", "I will take it"], "لَا + short present."),
        M("What does عَلَيْكَ أَنْ تَدْفَعَ mean?", "you must pay", ["you may pay", "you paid", "you will not pay"], "عَلَيْكَ أَنْ = you must."),
        F("___ حَقِيبَتَكَ مِنْ فَضْلِكَ.", "اِفْتَحْ", ["فَتَحَ", "يَفْتَح"], "A command to one man.", tr="Open your bag, please.", lemma="فتح:imp:anta"),
        F("لَا، مَعِي ___ فَقَط.", "هَدَايَا", ["حُدُود", "مَدِينَة"], "Gifts, not a border.", tr="No, I only have gifts."),
        F("___ مُوَظَّف الْجُمْرُك الْحَقِيبَة.", "فَتَّشَ", ["فَتَشَ", "يُفَتِّش"], "Measure II past: فَتَّشَ.", tr="The customs officer searched the bag.", lemma="فتش#2:past:huwa"),
        F("عَلَيْكَ أَنْ ___ ضَرِيبَة.", "تَدْفَعَ", ["تَدْفَعُ", "دَفَعَ"], "After أَنْ, the subjunctive: ـَ.", tr="You must pay a tax."),
    ],
    verify=(vv("فتح", "imp", anta="اِفْتَحْ") + vv("فتش#2", "past", huwa="فَتَّشَ") + vv("دفع", "sub", anta="تَدْفَعَ")),
)

# ---------------------------------------------------------------------------- 390
L390 = lesson(
    "Crossing the border",
    "بَعْدَ سَاعَتَيْن · اُعْبُرُوا · لَا تَنْسَ",
    requires=["طابور", "حافلة", "نزل", "عبر", "جواز", "بعد", "أمام", "طويل", "نسي"],
    cards=[
        card("Waiting and crossing",
             "At the border, buses stop and passengers queue. The guide gives orders: اِنْزِلُوا مِنَ الْحَافِلَة, “get off the bus”, اُعْبُرُوا الْحُدُود, “cross the border”. "
             "To warn someone, use لَا تَنْسَ, “do not forget”. The sentences are invented.",
             examples=[
                 ex("نَصِل إِلَى الْحُدُود بَعْدَ سَاعَتَيْن.", "We shall arrive at the border in two hours.", "بَعْدَ سَاعَتَيْن"),
                 ex("أَمَامَنَا طَابُور طَوِيل.", "In front of us is a long queue.", "أَمَامَنَا"),
                 ex("اِنْزِلُوا مِنَ الْحَافِلَة مِنْ فَضْلِكُمْ.", "Please get off the bus.", "اِنْزِلُوا"),
                 ex("اُعْبُرُوا الْحُدُود سَيْرًا عَلَى الْأَقْدَام.", "Cross the border on foot.", "اُعْبُرُوا"),
                 ex("لَا تَنْسَ جَوَازَكَ.", "Do not forget your passport.", "لَا تَنْسَ"),
                 ex("بَعْدَ الْعُبُور نَرْكَب حَافِلَة أُخْرَى.", "After the crossing we ride another bus.", "الْعُبُور"),
             ]),
    ],
    exercises=[
        M("What does بَعْدَ سَاعَتَيْن mean?", "after two hours", ["for two hours", "before two hours", "two hours ago"], "سَاعَتَيْن = two hours (dual)."),
        M("What does اِنْزِلُوا مِنَ الْحَافِلَة mean?", "Get off the bus", ["Get on the bus", "Wait in the bus", "Drive the bus"], "نَزَلَ مِنْ = to get off."),
        M("What does اُعْبُرُوا الْحُدُود mean?", "Cross the border", ["Close the border", "Open the border", "Reach the border"], "عَبَرَ = to cross."),
        M("What does لَا تَنْسَ جَوَازَكَ mean?", "Do not forget your passport", ["Show your passport", "I lost my passport", "Sign your passport"], "نَسِيَ = to forget."),
        M("What does أَمَامَنَا mean?", "in front of us", ["behind us", "with us", "after us"], "أَمَامَ + ـنَا."),
        M("Who is addressed in اِنْزِلُوا?", "a group", ["one man", "one woman", "two people"], "ـُوا marks a group."),
        F("نَصِل إِلَى الْحُدُود ___ سَاعَتَيْن.", "بَعْدَ", ["قَبْلَ", "عِنْدَ"], "“in two hours” is بَعْدَ.", tr="We shall arrive at the border in two hours."),
        F("___ مِنَ الْحَافِلَة مِنْ فَضْلِكُمْ.", "اِنْزِلُوا", ["اِنْزِلْ", "اِنْزِلِي"], "A group is addressed.", tr="Please get off the bus.", lemma="نزل:imp:antum"),
        F("لَا ___ جَوَازَكَ.", "تَنْسَ", ["تَنْسَى", "نَسِيَ"], "After لَا, the short present: تَنْسَ.", tr="Do not forget your passport."),
        F("اُعْبُرُوا الْحُدُود سَيْرًا عَلَى ___.", "الْأَقْدَام", ["الْحَافِلَة", "الطَّرِيق"], "“on foot”.", tr="Cross the border on foot."),
    ],
    verify=(vv("نزل", "imp", antum="اِنْزِلُوا") + vv("نسي", "neg", anta="لَا تَنْسَ") + vv("عبر", "imp", antum="اُعْبُرُوا")),
)


# ---------------------------------------------------------------------------- 391
L391 = lesson(
    "Adverbs of time",
    "صَبَاحًا · مَسَاءً · دَائِمًا · أَحْيَانًا · غَدًا",
    requires=["صباح", "مساء", "ليل", "نهار", "غد", "مبكر", "متأخر", "عادة", "فجأة", "نام"],
    cards=[
        card("When? The accusative ending",
             "An adverb of time answers the question “When?”. Most of these adverbs are in the accusative case, so they end in tanwīn with fatḥa: ـًا, written with an alif. "
             "After tā’ marbūṭa the tanwīn sits on the tā’: عَادَةً. After hamza it is written ـءً: مَسَاءً. Adverbs of time are usually free to move: at the start or the end of the sentence.",
             tables=[table(["English", "Arabic"],
                           [["in the morning", "صَبَاحًا"], ["in the evening", "مَسَاءً"], ["at night", "لَيْلًا"], ["by day", "نَهَارًا"], ["tomorrow", "غَدًا"], ["always", "دَائِمًا"], ["sometimes", "أَحْيَانًا"],
                            ["never (after a negative)", "أَبَدًا"], ["soon", "قَرِيبًا"], ["early", "مُبَكِّرًا"], ["late", "مُتَأَخِّرًا"], ["usually", "عَادَةً"], ["suddenly", "فَجْأَةً"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences (invented)",
             "Daily life of a traveller.",
             examples=[
                 ex("أَصِل إِلَى الْمَكْتَب مُبَكِّرًا.", "I arrive at the office early.", "مُبَكِّرًا"),
                 ex("نَشْرَب الْقَهْوَة صَبَاحًا.", "We drink coffee in the morning.", "صَبَاحًا"),
                 ex("أَذْهَب إِلَى السُّوق مَسَاءً.", "I go to the market in the evening.", "مَسَاءً"),
                 ex("هُوَ يَنَام مُتَأَخِّرًا دَائِمًا.", "He always sleeps late.", "دَائِمًا"),
                 ex("أَحْيَانًا نَزُور الْمَتْحَف.", "Sometimes we visit the museum.", "أَحْيَانًا"),
                 ex("سَنَصِل غَدًا.", "We shall arrive tomorrow.", "غَدًا"),
                 ex("عَادَةً أَسْكُن فِي فُنْدُق صَغِير.", "Usually I stay in a small hotel.", "عَادَةً"),
             ]),
    ],
    exercises=[
        M("What does صَبَاحًا mean?", "in the morning", ["in the evening", "at night", "tomorrow"], "صَبَاح = morning."),
        M("What does مَسَاءً mean?", "in the evening", ["in the morning", "early", "always"], "مَسَاء = evening."),
        M("What does غَدًا mean?", "tomorrow", ["yesterday", "today", "soon"], "غَدًا = tomorrow."),
        M("What does أَحْيَانًا mean?", "sometimes", ["always", "never", "suddenly"], "أَحْيَانًا = sometimes."),
        M("What does دَائِمًا mean?", "always", ["sometimes", "late", "tomorrow"], "دَائِمًا = always."),
        M("Which ending marks an adverb of time?", "tanwīn with fatḥa (ـًا)", ["ـُون", "ـِي", "ـَتْ"], "Adverbs of time are in the accusative."),
        M("How is the tanwīn written after tā’ marbūṭa?", "on the tā’: عَادَةً", ["with an extra alif: عَادَةًا", "it is dropped", "on the dāl"], "ـةً has no alif."),
        F("أَصِل إِلَى الْمَكْتَب ___.", "مُبَكِّرًا", ["مُبَكِّر", "مُبَكِّرَة"], "An adverb of time: ـًا.", tr="I arrive at the office early."),
        F("سَنَصِل ___.", "غَدًا", ["أَمْس", "قَبْل"], "The verb is in the future.", tr="We shall arrive tomorrow."),
        F("أَذْهَب إِلَى السُّوق ___.", "مَسَاءً", ["مَسَاء", "مَسَاءَة"], "“in the evening”.", tr="I go to the market in the evening."),
        F("___ نَزُور الْمَتْحَف.", "أَحْيَانًا", ["أَحْيَان", "حِين"], "“sometimes”.", tr="Sometimes we visit the museum."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 392
L392 = lesson(
    "Time phrases in the accusative",
    "يَوْمَ الْجُمُعَةِ · كُلَّ يَوْمٍ · طَوَالَ اللَّيْلِ",
    requires=["يوم", "أسبوع", "ليلة", "ظهر", "بعد", "عمل", "مشغول", "سكن"],
    cards=[
        card("Nouns used as adverbs",
             "Besides the one-word adverbs, some nouns answer “When?” in the accusative case and need no preposition: يَوْمَ الْجُمُعَةِ, “on Friday”, كُلَّ يَوْمٍ, “every day”, الْيَوْمَ, “today”. "
             "This lesson shows the case endings in full on the time phrases, so that you can see the fatḥa (ـَ) on the first word (a noun or كُلّ). In everyday speech they are dropped.",
             tables=[table(["English", "Arabic"],
                           [["on Friday", "يَوْمَ الْجُمُعَةِ"], ["every day", "كُلَّ يَوْمٍ"], ["today", "الْيَوْمَ"], ["tonight", "اللَّيْلَةَ"], ["this week", "هَذَا الْأُسْبُوعَ"], ["all night long", "طَوَالَ اللَّيْلِ"], ["in the afternoon", "بَعْدَ الظُّهْرِ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences (invented)",
             "Plans for the week.",
             examples=[
                 ex("نَزُور الْمَتْحَف يَوْمَ الْجُمُعَةِ.", "We visit the museum on Friday.", "يَوْمَ الْجُمُعَةِ"),
                 ex("أَعْمَل كُلَّ يَوْمٍ.", "I work every day.", "كُلَّ يَوْمٍ"),
                 ex("الْيَوْمَ نَسْكُن فِي الْفُنْدُق.", "Today we stay in the hotel.", "الْيَوْمَ"),
                 ex("اللَّيْلَةَ نَذْهَب إِلَى مَطْعَم.", "Tonight we go to a restaurant.", "اللَّيْلَةَ"),
                 ex("هَذَا الْأُسْبُوعَ أَنَا مَشْغُول.", "This week I am busy.", "هَذَا الْأُسْبُوعَ"),
                 ex("سَافَرْنَا طَوَالَ اللَّيْلِ.", "We travelled all night long.", "طَوَالَ اللَّيْلِ"),
             ]),
    ],
    exercises=[
        M("What does يَوْمَ الْجُمُعَةِ mean?", "on Friday", ["every Friday", "last Friday", "after Friday"], "يَوْمَ + day = on that day."),
        M("What does كُلَّ يَوْمٍ mean?", "every day", ["all day long", "one day", "yesterday"], "كُلّ + noun = every."),
        M("What does اللَّيْلَةَ mean?", "tonight", ["yesterday", "this morning", "next week"], "لَيْلَة = a night."),
        M("What does طَوَالَ اللَّيْلِ mean?", "all night long", ["every night", "at noon", "in the evening"], "طَوَالَ = throughout."),
        M("What case is the first word of these time phrases in (يَوْمَ، كُلَّ، طَوَالَ)?", "accusative", ["nominative", "genitive", "none"], "Time adverbs take the accusative: fatḥa."),
        M("What does هَذَا الْأُسْبُوعَ أَنَا مَشْغُول mean?", "This week I am busy", ["Last week I was busy", "I am busy every week", "Next week I am free"], "هَذَا الْأُسْبُوعَ = this week."),
        F("نَزُور الْمَتْحَف ___ الْجُمُعَةِ.", "يَوْمَ", ["يَوْمُ", "يَوْمِ"], "In the accusative: يَوْمَ.", tr="We visit the museum on Friday."),
        F("أَعْمَل ___ يَوْمٍ.", "كُلَّ", ["كُلُّ", "كُلِّ"], "“every” as an adverb: كُلَّ.", tr="I work every day."),
        F("___ نَسْكُن فِي الْفُنْدُق.", "الْيَوْمَ", ["الْيَوْمُ", "الْيَوْمِ"], "The accusative: ـَ.", tr="Today we stay in the hotel."),
        F("سَافَرْنَا ___ اللَّيْلِ.", "طَوَالَ", ["طَوَالُ", "طَوَالِ"], "“throughout”, in the accusative.", tr="We travelled all night long."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 393
L393 = lesson(
    "Putting a day in order",
    "أَوَّلًا · ثُمَّ · بَعْدَ ذَلِكَ · أَخِيرًا",
    requires=["أول", "ثم", "بعد", "قبل", "ذلك", "بداية", "نهاية", "مطعم", "غداء"],
    cards=[
        card("Linking words for time",
             "Adverbs of time also organise a story. Start with أَوَّلًا, “first”; continue with ثُمَّ, “then”, and بَعْدَ ذَلِكَ, “after that”; finish with أَخِيرًا, “finally”. "
             "Use فِي الْبِدَايَة, “at the beginning”, and فِي النِّهَايَة, “at the end”. The little story is invented.",
             tables=[table(["English", "Arabic"],
                           [["first", "أَوَّلًا"], ["second", "ثَانِيًا"], ["then", "ثُمَّ"], ["after that", "بَعْدَ ذَلِكَ"], ["before that", "قَبْلَ ذَلِكَ"], ["finally", "أَخِيرًا"], ["at the beginning", "فِي الْبِدَايَة"], ["at the end", "فِي النِّهَايَة"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أَوَّلًا نَصِل إِلَى الْفُنْدُق.", "First we arrive at the hotel.", "أَوَّلًا"),
                 ex("ثُمَّ نَذْهَب إِلَى الْمَتْحَف.", "Then we go to the museum.", "ثُمَّ"),
                 ex("بَعْدَ ذَلِكَ نَتَغَدَّى فِي مَطْعَم.", "After that we have lunch in a restaurant.", "بَعْدَ ذَلِكَ"),
                 ex("قَبْلَ ذَلِكَ نَشْتَرِي تَذَاكِر.", "Before that we buy tickets.", "قَبْلَ ذَلِكَ"),
                 ex("أَخِيرًا نَرْجِع إِلَى الْغُرْفَة.", "Finally we return to the room.", "أَخِيرًا"),
                 ex("فِي النِّهَايَة أَنَا مُتْعَب.", "In the end I am tired.", "فِي النِّهَايَة"),
             ]),
    ],
    exercises=[
        M("What does أَوَّلًا mean?", "first", ["finally", "then", "never"], "أَوَّل = first."),
        M("What does أَخِيرًا mean?", "finally", ["first", "suddenly", "usually"], "آخِر / أَخِير = last."),
        M("What does ثُمَّ mean?", "then", ["before", "but", "because"], "ثُمَّ links events in order."),
        M("What does بَعْدَ ذَلِكَ mean?", "after that", ["before that", "like that", "at that time"], "بَعْد = after."),
        M("What does قَبْلَ ذَلِكَ mean?", "before that", ["after that", "during that", "instead of that"], "قَبْل = before."),
        M("What does فِي الْبِدَايَة mean?", "at the beginning", ["at the end", "in the middle", "all day"], "بِدَايَة = beginning."),
        F("___ نَصِل إِلَى الْفُنْدُق.", "أَوَّلًا", ["أَخِيرًا", "أَبَدًا"], "The first step of the day.", tr="First we arrive at the hotel."),
        F("___ نَذْهَب إِلَى الْمَتْحَف.", "ثُمَّ", ["لَكِنْ", "لِأَنَّ"], "“then”.", tr="Then we go to the museum."),
        F("___ نَرْجِع إِلَى الْغُرْفَة.", "أَخِيرًا", ["أَوَّلًا", "قَبْلَ"], "The last step.", tr="Finally we return to the room."),
        F("بَعْدَ ___ نَتَغَدَّى فِي مَطْعَم.", "ذَلِكَ", ["ذَلِكِ", "هَذِهِ"], "“after that”.", tr="After that we have lunch in a restaurant."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 394
L394 = lesson(
    "Review: hotel, commands, border and time",
    "مُرَاجَعَة الْوَحْدَة",
    requires=["فندق", "حجز", "جواز", "وقع", "قدم", "رسالة", "صباح", "غد"],
    cards=[
        card("Commands from every measure",
             "A summary of the commands from this unit. In Measures II and III the prefix goes; in IV the أَ stays; in V and VI the تَـ stays; in VII, VIII and X a helping alif with kasra is added. Commands to a woman end in ـِي and to a group in ـُوا.",
             tables=[table(["Measure", "To a man", "To a woman", "To a group"],
                           [["II", "وَقِّعْ", "وَقِّعِي", "وَقِّعُوا"], ["III", "سَاعِدْ", "سَاعِدِي", "سَاعِدُوا"], ["IV", "أَرْسِلْ", "أَرْسِلِي", "أَرْسِلُوا"], ["V", "تَكَلَّمْ", "تَكَلَّمِي", "تَكَلَّمُوا"],
                            ["VI", "تَقَابَلْ", "تَقَابَلِي", "تَقَابَلُوا"], ["VIII", "اِنْتَظِرْ", "اِنْتَظِرِي", "اِنْتَظِرُوا"], ["X", "اِسْتَخْدِمْ", "اِسْتَخْدِمِي", "اِسْتَخْدِمُوا"]],
                           say=[1, 2, 3], tlit=[1, 2, 3], gloss=False)]),
    ],
    exercises=[
        M("Which command is from Measure IV?", "أَرْسِلْ", ["وَقِّعْ", "تَكَلَّمْ", "اِنْتَظِرْ"], "Measure IV keeps أَ."),
        M("Which command is from Measure V?", "تَكَلَّمْ", ["سَاعِدْ", "أَرْسِلْ", "اِسْتَخْدِمْ"], "Measure V keeps تَـ."),
        M("Which command is to a woman?", "اِنْتَظِرِي", ["اِنْتَظِرْ", "اِنْتَظِرُوا", "اِنْتَظَرَ"], "ـِي marks a woman."),
        M("What does لَا تُوَقِّعْ هُنَا mean?", "Do not sign here", ["Sign here", "He signed here", "I will sign here"], "لَا + short present."),
        M("What does خَتَمَ الْمُوَظَّف الْجَوَاز mean?", "The officer stamped the passport", ["The officer lost the passport", "The officer read a book", "The officer opened the door"], "خَتَمَ = stamped."),
        M("What does هَلْ مَعَكَ شَيْء لِلتَّصْرِيح؟ ask?", "whether you have anything to declare", ["whether you have a ticket", "whether you are tired", "whether the room is ready"], "At customs."),
        F("___ جَوَازَكَ لِلْمُوَظَّف.", "قَدِّمْ", ["قَدَّمَ", "يُقَدِّم"], "A command to one man (Measure II).", tr="Hand your passport to the clerk.", lemma="قدم#2:imp:anta"),
        F("___ الضُّيُوف عِنْدَ الْبَاب.", "اِسْتَقْبِلُوا", ["اِسْتَقْبِلْ", "اِسْتَقْبِلِي"], "A group is addressed.", tr="Welcome the guests at the door.", lemma="قبل#10:imp:antum"),
        F("لَا ___ جَوَازَكَ.", "تَنْسَ", ["تَنْسَى", "نَسِيَ"], "After لَا, the short present.", tr="Do not forget your passport."),
        F("سَنَصِل ___.", "غَدًا", ["أَمْس", "قَبْل"], "The future needs a future time.", tr="We shall arrive tomorrow."),
        F("أَصِل إِلَى الْمَكْتَب ___.", "مُبَكِّرًا", ["مُبَكِّر", "مُبَكِّرَة"], "An adverb of time: ـًا.", tr="I arrive at the office early."),
        F("___ فِي الْبَتْرَاء مَعَابِد وَقُبُور.", "تُوجَد", ["وَجَدَ", "وَجَدْتُ"], "A passive verb meaning “there are”; the other options mean “he found” and “I found”.", tr="In Petra there are temples and tombs."),
    ],
    verify=(),
)


UNIT = unit("الْفُنْدُق وَالْحُدُود: hotels, imperatives of derived verbs, historic sites and adverbs of time", [L374, L375, L376, L377, L378, L379, L380, L381, L382, L383, L384, L385, L386, L387, L388, L389, L390, L391, L392, L393, L394])
