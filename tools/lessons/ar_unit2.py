"""Unit 2: greetings, introductions and basic bio-data (textbook Chapter 1; military
ranks and titles left out)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 16
L16 = lesson(
    "Hello and welcome",
    "أَهْلًا · مَرْحَبًا · السَّلَام عَلَيْكُم",
    requires=["مرحبا", "سلام", "صباح", "مساء", "خير"],
    cards=[
        card("Saying hello",
             "أَهْلًا and مَرْحَبًا are the everyday hellos, and either can be answered with the other. A warmer "
             "welcome is أَهْلًا وَسَهْلًا. Among Muslims, and widely across the Arab world, people also greet "
             "with “peace be upon you”, and the reply turns the words around.",
             examples=[
                 ex("أَهْلًا", "Hello; welcome"),
                 ex("مَرْحَبًا", "Hello; welcome"),
                 ex("أَهْلًا وَسَهْلًا", "Welcome (a warm welcome)"),
                 ex("السَّلَام عَلَيْكُم", "Peace be upon you (hello)"),
                 ex("وَعَلَيْكُمُ السَّلَام", "And upon you, peace (the reply)"),
             ]),
        card("Morning and evening",
             "The greetings for the time of day are answered with a play on words: “morning of goodness” is "
             "returned as “morning of light”. The same pattern works in the evening.",
             examples=[
                 ex("صَبَاح الْخَيْر", "Good morning"),
                 ex("صَبَاح النُّور", "Good morning (the reply)"),
                 ex("مَسَاء الْخَيْر", "Good evening"),
                 ex("مَسَاء النُّور", "Good evening (the reply)"),
             ]),
        card("Parting",
             "To say goodbye, wish the other person safety. “See you” literally means “until the meeting”.",
             examples=[
                 ex("مَعَ السَّلَامَة", "Goodbye (go with safety)"),
                 ex("إِلَى اللِّقَاء", "See you; until we meet again"),
             ]),
    ],
    exercises=[
        M("Someone says صَبَاح الْخَيْر. What is the usual reply?", "صَبَاح النُّور", ["مَسَاء الْخَيْر", "مَعَ السَّلَامَة", "شُكْرًا"],
          "Morning of goodness is answered with morning of light."),
        M("Someone says مَسَاء الْخَيْر. What is the usual reply?", "مَسَاء النُّور", ["صَبَاح النُّور", "إِلَى اللِّقَاء", "أَهْلًا وَسَهْلًا"],
          "The evening greeting is answered the same way."),
        M("Someone says السَّلَام عَلَيْكُم. What is the natural reply?", "وَعَلَيْكُمُ السَّلَام", ["مَعَ السَّلَامَة", "صَبَاح الْخَيْر", "مَرْحَبًا فَقَط"],
          "The reply turns the words around: and upon you, peace."),
        M("Which phrase means “Welcome”?", "أَهْلًا وَسَهْلًا", ["مَعَ السَّلَامَة", "إِلَى اللِّقَاء", "مَسَاء الْخَيْر"],
          "أَهْلًا وَسَهْلًا is the warm welcome."),
        M("Which phrase means “Goodbye”?", "مَعَ السَّلَامَة", ["أَهْلًا", "مَسَاء النُّور", "صَبَاح الْخَيْر"],
          "مَعَ السَّلَامَة wishes the other person safety."),
        M("What does إِلَى اللِّقَاء mean?", "See you; until we meet again", ["Welcome", "Thank you", "Good morning"],
          "It is the everyday “see you”."),
        M("It is eight in the evening. Which greeting fits?", "مَسَاء الْخَيْر", ["صَبَاح الْخَيْر", "صَبَاح النُّور", "أَهْلًا وَسَهْلًا فَقَط"],
          "مَسَاء is evening; صَبَاح is morning."),
        F("___ الْخَيْر", "صَبَاح", ["مَسَاء", "مَرْحَبًا", "مَعَ"], "Good morning is صَبَاح الْخَيْر.", tr="Good morning"),
        F("___ السَّلَامَة", "مَعَ", ["أَهْلًا", "مَرْحَبًا", "مَسَاء"], "Goodbye is مَعَ السَّلَامَة.", tr="Goodbye"),
    ],
    verify=vw("مَعَ", "إِلَى"),
)

# ---------------------------------------------------------------------------- 17
L17 = lesson(
    "How are you?",
    "كَيْفَ حَالُك؟",
    requires=["كيف", "حال", "خير", "شكر", "فضل"],
    cards=[
        card("Asking and answering",
             "كَيْفَ الْحَال؟ asks “how are things?”. Drop ال and add the ending for your listener, and you get “how are you?”: "
             "the ending ـكَ is for a man and ـكِ for a woman. Arabic speech tells you who is addressed, so listen "
             "for the last vowel. A short, polite answer is بِخَيْر (well), often followed by thanks to God.",
             tables=[table(["English", "Man · Woman"],
                           [["How are you?", "كَيْفَ حَالُكَ؟ · كَيْفَ حَالُكِ؟"],
                            ["And you?", "وَأَنْتَ؟ · وَأَنْتِ؟"]],
                           say=[1], tlit=[1]),
                     table(["English", "Reply"],
                           [["Well", "بِخَيْر"], ["Fine, praise God", "بِخَيْر، الْحَمْدُ لِلَّه"], ["Thank you", "شُكْرًا"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Please and thank you",
             "Thanks are returned with عَفْوًا, which also means “pardon me”. For “please” when you ask for "
             "something, say مِنْ فَضْلِك (literally “from your favour”). When you offer something, or hold the door "
             "for someone, say تَفَضَّل to a man and تَفَضَّلِي to a woman.",
             tables=[table(["English", "Man · Woman"],
                           [["Please (asking)", "مِنْ فَضْلِكَ · مِنْ فَضْلِكِ"],
                            ["Please; go ahead; here you are", "تَفَضَّلْ · تَفَضَّلِي"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[ex("شُكْرًا جَزِيلًا", "Thank you very much"), ex("عَفْوًا", "You are welcome")]),
        card("A short exchange",
             "Two friends meet in the corridor.",
             examples=[
                 ex("أَهْلًا يَا خَالِد، كَيْفَ حَالُك؟", "Hello, Khalid, how are you?"),
                 ex("بِخَيْر، الْحَمْدُ لِلَّه. وَأَنْتَ؟", "Fine, praise God. And you?"),
                 ex("بِخَيْر، شُكْرًا.", "Fine, thank you."),
             ]),
    ],
    exercises=[
        M("You ask a woman how she is. Which is right?", "كَيْفَ حَالُكِ؟", ["كَيْفَ حَالُكَ؟", "كَيْفَ حَالُهُ؟", "كَيْفَ حَالُ؟"],
          "ـكِ is the feminine “you”."),
        M("You ask a man how he is. Which is right?", "كَيْفَ حَالُكَ؟", ["كَيْفَ حَالُكِ؟", "كَيْفَ حَالُهَا؟", "كَيْفَ حَالِي؟"],
          "ـكَ is the masculine “you”."),
        M("Which reply means “Fine, praise God”?", "بِخَيْر، الْحَمْدُ لِلَّه", ["مَعَ السَّلَامَة", "أَهْلًا وَسَهْلًا", "مِنْ فَضْلِك"],
          "بِخَيْر means well; الْحَمْدُ لِلَّه adds praise to God."),
        M("Which phrase means “Please” when you ask for something?", "مِنْ فَضْلِك", ["عَفْوًا", "تَفَضَّل", "شُكْرًا"],
          "مِنْ فَضْلِك is the polite “please” of a request."),
        M("You hand a woman a cup of tea. What do you say?", "تَفَضَّلِي", ["تَفَضَّلْ", "شُكْرًا", "مِنْ فَضْلِكَ"],
          "تَفَضَّلِي is the feminine form of “here you are”."),
        M("You hand a man a cup of tea. What do you say?", "تَفَضَّلْ", ["تَفَضَّلِي", "مِنْ فَضْلِكِ", "بِخَيْر"],
          "تَفَضَّلْ is the masculine form."),
        M("Someone says شُكْرًا. What do you answer?", "عَفْوًا", ["مَرْحَبًا", "تَفَضَّلِي", "صَبَاح النُّور"],
          "عَفْوًا answers thanks."),
        M("What does شُكْرًا جَزِيلًا mean?", "Thank you very much", ["Thank you for nothing", "Good evening", "Please come in"],
          "جَزِيل adds “great”."),
        F("كَيْفَ ___؟", "الْحَال", ["الْكِتَاب", "الْبَيْت", "الْبَاب"], "كَيْفَ الْحَال؟ asks how things are.", tr="How are things?"),
    ],
    verify=vw("تَفَضَّل", "تَفَضَّلِي"),
)

# ---------------------------------------------------------------------------- 18
L18 = lesson(
    "My name is…",
    "اِسْمِي · أَنَا · مَا اِسْمُك؟",
    requires=["أنا", "ولد", "عمر", "مرحبا"],
    cards=[
        card("Giving your name",
             "There are two easy ways to give your name: say اِسْمِي and the name (“my name, Khalid”), or say "
             "أَنَا and the name. Arabic has no word for “am”, so أَنَا خَالِد means “I am Khalid”. To ask someone "
             "else, say مَا اِسْمُك؟ with the man or woman ending.",
             examples=[
                 ex("اِسْمِي خَالِد.", "My name is Khalid."),
                 ex("أَنَا مَاهِر.", "I am Maher."),
                 ex("مَا اِسْمُكَ؟", "What is your name? (to a man)"),
                 ex("مَا اِسْمُكِ؟", "What is your name? (to a woman)"),
             ]),
        card("Names to know",
             "Common Arabic names are easy to tell apart by gender. Many women’s names end in ة or ى or ا, but "
             "not all do.",
             tables=[table(["Men", "Women"],
                           [["أَحْمَد", "هُدَى"], ["خَالِد", "سَارَة"], ["مَاهِر", "لَيْلَى"], ["عُمَر", "مَرْيَم"],
                            ["يُوسُف", "فَاطِمَة"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Pleased to meet you",
             "Once you know each other’s names, say تَشَرَّفْنَا, “we are honoured”. The usual answer repeats it "
             "or says that the honour is yours.",
             examples=[
                 ex("تَشَرَّفْنَا.", "Pleased to meet you."),
                 ex("أَهْلًا وَسَهْلًا. تَشَرَّفْنَا يَا مَاهِر.", "Welcome. Pleased to meet you, Maher."),
             ]),
    ],
    exercises=[
        M("How do you say “My name is Khalid”?", "اِسْمِي خَالِد", ["اِسْمُكَ خَالِد", "كَيْفَ خَالِد", "مَعَ خَالِد"],
          "اِسْمِي = my name."),
        M("Which means “I am Maher”?", "أَنَا مَاهِر", ["هُوَ مَاهِر", "أَنْتَ مَاهِر", "هِيَ مَاهِر"],
          "أَنَا means I; Arabic needs no word for “am”."),
        M("You ask a woman her name. Which is right?", "مَا اِسْمُكِ؟", ["مَا اِسْمُكَ؟", "مَا اِسْمِي؟", "مَا اِسْمُهُ؟"],
          "ـكِ is the feminine “your”."),
        M("You ask a man his name. Which is right?", "مَا اِسْمُكَ؟", ["مَا اِسْمُكِ؟", "مَا اِسْمُهَا؟", "مَا اِسْمُنَا؟"],
          "ـكَ is the masculine “your”."),
        M("What does تَشَرَّفْنَا mean?", "Pleased to meet you", ["Goodbye", "Thank you", "How are you?"],
          "It literally means “we are honoured”."),
        M("Which of these is a woman’s name?", "هُدَى", ["أَحْمَد", "خَالِد", "مَاهِر"],
          "هُدَى is a woman’s name; the others are men’s."),
        M("What does اِسْمِي mean?", "my name", ["your name", "his name", "her name"], "ـِي attached to a noun means “my”."),
        F("أَنَا ___.", "لَيْلَى", ["لَيْلَة", "اِسْمِي", "تَشَرَّفْنَا"], "A name follows أَنَا.", tr="I am Layla."),
    ],
    verify=vw("أَحْمَد", "خَالِد", "مَاهِر", "هُدَى", "لَيْلَى"),
)

# ---------------------------------------------------------------------------- 19
L19 = lesson(
    "Titles",
    "أُسْتَاذ · دُكْتُور · سَيِّدَة",
    requires=["أستاذ", "دكتور", "سيدة", "عمر"],
    cards=[
        card("Mr, Mrs, Doctor, Professor",
             "Arabic speakers like titles. Use a title and the first name, not the surname: أُسْتَاذ أَحْمَد. "
             "أُسْتَاذ (ustādh) means “Mr” for an educated man and also “teacher” or “professor”, دُكْتُور is "
             "used for medical doctors and anyone with a doctorate, and سَيِّد and سَيِّدَة mean “Mr” and “Mrs”. "
             "The feminine adds ة.",
             tables=[table(["English", "Man", "Woman"],
                           [["Mr; Ms; teacher", "أُسْتَاذ", "أُسْتَاذَة"],
                            ["Doctor", "دُكْتُور", "دُكْتُورَة"],
                            ["Mr; Mrs", "سَيِّد", "سَيِّدَة"],
                            ["Miss", "", "آنِسَة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Calling someone: يَا",
             "To get someone’s attention, put يَا before the name or title: يَا أَحْمَد, يَا أُسْتَاذ. It works like "
             "“hey” or “O” and is not rude.",
             examples=[
                 ex("صَبَاح الْخَيْر يَا أُسْتَاذ أَحْمَد.", "Good morning, Mr Ahmad.", "يَا أُسْتَاذ"),
                 ex("أَهْلًا يَا دُكْتُورَة سَارَة.", "Hello, Dr Sara.", "يَا دُكْتُورَة"),
                 ex("مَسَاء الْخَيْر يَا سَيِّدَة لَيْلَى.", "Good evening, Mrs Layla.", "يَا سَيِّدَة"),
             ]),
        card("Father of, mother of",
             "Adults are often named after their eldest son: أَبُو أَحْمَد is “father of Ahmad” and أُمّ أَحْمَد "
             "“mother of Ahmad”. It is a mark of respect, and people may use it even for someone who has no child "
             "of that name.",
             examples=[ex("أَبُو أَحْمَد", "father of Ahmad"), ex("أُمّ أَحْمَد", "mother of Ahmad")]),
    ],
    exercises=[
        M("Which title would you use for a woman who is a doctor?", "دُكْتُورَة", ["دُكْتُور", "سَيِّد", "آنِسَة"],
          "The feminine adds ة."),
        M("Which means “Miss”?", "آنِسَة", ["سَيِّدَة", "أُسْتَاذ", "دُكْتُور"], "آنِسَة is used for an unmarried young woman."),
        M("How do you greet a male teacher called Ahmad respectfully?", "صَبَاح الْخَيْر يَا أُسْتَاذ أَحْمَد", ["صَبَاح الْخَيْر يَا أَحْمَد دُكْتُورَة", "صَبَاح الْخَيْر يَا سَيِّدَة أَحْمَد", "صَبَاح الْخَيْر أُسْتَاذَة"],
          "Title + first name, with يَا to call him."),
        M("What does يَا do before a name?", "It calls the person, like “hey” or “O”", ["It makes the name plural", "It means “and”", "It makes the name feminine"],
          "يَا is the calling word."),
        M("Which is the title for a woman, “Mrs”?", "سَيِّدَة", ["سَيِّد", "دُكْتُور", "أُسْتَاذ"], "The feminine adds ة."),
        M("What does أَبُو أَحْمَد mean?", "father of Ahmad", ["Ahmad’s son", "Ahmad’s brother", "Mr Ahmad"], "أَبُو means father of."),
        F("أَهْلًا يَا ___ سَارَة.", "دُكْتُورَة", ["دُكْتُور", "سَيِّد", "أَحْمَد"], "Sara is a woman, so the title is feminine.", tr="Hello, Dr Sara."),
        F("مَسَاء الْخَيْر يَا ___ أَحْمَد.", "أُسْتَاذ", ["أُسْتَاذَة", "سَيِّدَة", "آنِسَة"], "Ahmad is a man, so the title is masculine.", tr="Good evening, Mr Ahmad."),
    ],
    verify=vf("أُسْتَاذ", "أُسْتَاذَة") + vf("دُكْتُور", "دُكْتُورَة") + vf("سَيِّد", "سَيِّدَة"),
)

# ---------------------------------------------------------------------------- 20
L20 = lesson(
    "I, you, he, she",
    "أَنَا · أَنْتَ · أَنْتِ · هُوَ · هِيَ",
    requires=["أنا", "أنت", "هو", "هي"],
    cards=[
        card("Five little words",
             "Personal pronouns are some of the most common words in any language. Arabic has a separate “you” "
             "for a man and a woman, and “he” and “she” are used for things too, because every Arabic noun is "
             "masculine or feminine (“it” does not exist).",
             tables=[table(["English", "Arabic"],
                           [["I", "أَنَا"], ["you (to a man)", "أَنْتَ"], ["you (to a woman)", "أَنْتِ"],
                            ["he; it (masculine)", "هُوَ"], ["she; it (feminine)", "هِيَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Who is speaking?",
             "In Arabic a pronoun can be left out of a sentence when the verb already shows who is meant, but "
             "when there is no verb you need it. Notice how it appears at the start of the sentence.",
             examples=[
                 ex("أَنَا طَالِب.", "I am a student (a man speaking).", "أَنَا"),
                 ex("أَنْتِ طَالِبَة.", "You are a student (to a woman).", "أَنْتِ"),
                 ex("هُوَ مُدَرِّس.", "He is a teacher.", "هُوَ"),
                 ex("هِيَ طَبِيبَة.", "She is a doctor.", "هِيَ"),
             ]),
    ],
    exercises=[
        M("Which pronoun means “I”?", "أَنَا", ["أَنْتَ", "هُوَ", "هِيَ"], "أَنَا = I."),
        M("Which pronoun do you use to a woman?", "أَنْتِ", ["أَنْتَ", "هِيَ", "أَنَا"], "أَنْتِ is the feminine “you”; the final kasra marks it."),
        M("Which pronoun do you use to a man?", "أَنْتَ", ["أَنْتِ", "هِيَ", "هُوَ"], "أَنْتَ is the masculine “you”."),
        M("Which pronoun means “she”?", "هِيَ", ["هُوَ", "أَنْتِ", "أَنَا"], "هِيَ = she."),
        M("Which pronoun means “he”?", "هُوَ", ["هِيَ", "أَنْتَ", "أَنَا"], "هُوَ = he."),
        M("A book is on the table. Which pronoun stands for the masculine word كِتَاب?", "هُوَ", ["هِيَ", "أَنَا", "أَنْتَ"],
          "Arabic uses “he” for masculine things."),
        M("A school (مَدْرَسَة, feminine) is big. Which pronoun stands for it?", "هِيَ", ["هُوَ", "أَنْتِ", "أَنْتَ"],
          "مَدْرَسَة is feminine, so it is هِيَ."),
        F("___ طَبِيبَة.", "هِيَ", ["هُوَ", "نَحْنُ", "أَنْتَ"], "طَبِيبَة is feminine: she is a doctor.", tr="She is a doctor."),
        F("___ مُدَرِّس.", "هُوَ", ["هِيَ", "أَنْتِ", "نَحْنُ"], "مُدَرِّس is masculine: he is a teacher.", tr="He is a teacher."),
    ],
    verify=vw("أَنَا", "أَنْتَ", "أَنْتِ", "هُوَ", "هِيَ"),
)

# ---------------------------------------------------------------------------- 21
L21 = lesson(
    "We, you (all), they",
    "نَحْنُ · أَنْتُم · هُم · and the dual",
    requires=["نحن", "هم", "أنت"],
    cards=[
        card("The plural pronouns",
             "The plural pronouns copy the singular ones, with separate forms for men and women. For mixed groups, "
             "Arabic uses the masculine form. In practice the feminine plurals أَنْتُنَّ and هُنَّ are used only "
             "for groups of women.",
             tables=[table(["English", "Arabic"],
                           [["we", "نَحْنُ"], ["you (men or a mixed group)", "أَنْتُم"], ["you (a group of women)", "أَنْتُنَّ"],
                            ["they (men or a mixed group)", "هُم"], ["they (a group of women)", "هُنَّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("The dual: exactly two",
             "Arabic has a number between one and many: the dual, for exactly two. It has its own pronouns for “you two” "
             "and “they two”, the same for men and women.",
             tables=[table(["English", "Arabic"],
                           [["you two", "أَنْتُمَا"], ["they two", "هُمَا"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[ex("نَحْنُ طُلَّاب.", "We are students.", "نَحْنُ"),
                       ex("هُم مُدَرِّسُون.", "They are teachers.", "هُم"),
                       ex("هُمَا طَالِبَتَان.", "They (two women) are students.", "هُمَا")]),
    ],
    exercises=[
        M("Which pronoun means “we”?", "نَحْنُ", ["هُم", "أَنْتُم", "أَنَا"], "نَحْنُ = we."),
        M("Which pronoun means “they” (a mixed group)?", "هُم", ["هُنَّ", "هُمَا", "نَحْنُ"], "هُم is masculine or mixed plural."),
        M("Which means “they” for a group of women?", "هُنَّ", ["هُم", "هُمَا", "أَنْتُنَّ"], "هُنَّ is feminine plural."),
        M("Which means “you” to a group of men?", "أَنْتُم", ["أَنْتُنَّ", "أَنْتُمَا", "هُم"], "أَنْتُم is the masculine plural “you”."),
        M("Which means “you two”?", "أَنْتُمَا", ["أَنْتُم", "هُمَا", "أَنْتُنَّ"], "The dual pronouns end in ـمَا."),
        M("Which means “they two”?", "هُمَا", ["هُم", "هُنَّ", "أَنْتُمَا"], "هُمَا = the two of them."),
        M("A man, a woman and a child are talking about themselves. Which pronoun?", "نَحْنُ", ["هُم", "أَنْتُم", "هُمَا"], "The group includes the speaker: we."),
        M("You talk to three women. Which pronoun is most exact?", "أَنْتُنَّ", ["أَنْتُم", "أَنْتِ", "هُنَّ"], "أَنْتُنَّ = you (feminine plural)."),
        F("___ طُلَّاب.", "نَحْنُ", ["أَنَا", "هِيَ", "أَنْتِ"], "طُلَّاب is plural and the speaker is included: we.", tr="We are students."),
    ],
    verify=vw("نَحْنُ", "أَنْتُم", "أَنْتُنَّ", "هُم", "هُنَّ", "أَنْتُمَا", "هُمَا"),
)

# ---------------------------------------------------------------------------- 22
L22 = lesson(
    "Sentences without “is”",
    "The nominal sentence",
    requires=["طالب", "مدرس", "كتاب", "بيت"],
    cards=[
        card("No verb “to be”",
             "In the present tense Arabic leaves “is, am, are” out. A sentence made of two nouns, or a pronoun and a "
             "noun, is already complete. This is called the nominal sentence and it has two "
             "parts: the subject (what you talk about) and the predicate (what you say about it).",
             tables=[table(["Subject", "Predicate", "Meaning"],
                           [["أَنَا", "طَالِب", "I am a student"],
                            ["هُوَ", "مُدَرِّس", "He is a teacher"],
                            ["هِيَ", "طَبِيبَة", "She is a doctor"],
                            ["نَحْنُ", "طُلَّاب", "We are students"]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("This is…: هَذَا and هَذِهِ",
             "To point at something, use هَذَا for a masculine noun and هَذِهِ for a feminine one. After them you "
             "can put a noun with no article: “this (is) a book”.",
             examples=[
                 ex("هَذَا كِتَاب.", "This is a book.", "هَذَا"),
                 ex("هَذَا بَيْت.", "This is a house.", "هَذَا"),
                 ex("هَذِهِ مَدْرَسَة.", "This is a school.", "هَذِهِ"),
                 ex("هَذِهِ سَيَّارَة.", "This is a car.", "هَذِهِ"),
             ]),
        card("The, and a",
             "With ال the noun becomes definite: “the book”. Arabic has no word for “a”: an indefinite noun is just "
             "the bare noun. A sentence in which the subject is definite and the predicate is not, as in "
             "الْوَلَد طَالِب, means “the boy is a student”.",
             examples=[
                 ex("الْوَلَد طَالِب.", "The boy is a student.", "الْوَلَد"),
                 ex("الْبِنْت طَالِبَة.", "The girl is a student.", "الْبِنْت"),
                 ex("الْبَيْت كَبِير.", "The house is big.", "الْبَيْت"),
             ]),
    ],
    exercises=[
        M("How do you say “I am a student” (a man speaking)?", "أَنَا طَالِب", ["أَنَا يَكُون طَالِب", "أَنَا هُوَ طَالِب", "طَالِب أَنَا هُوَ"],
          "No word for “am” is needed."),
        M("How do you say “She is a doctor”?", "هِيَ طَبِيبَة", ["هُوَ طَبِيب", "هِيَ طَبِيب", "هُوَ طَبِيبَة"],
          "The pronoun is feminine and so is the noun."),
        M("Which means “This is a house”?", "هَذَا بَيْت", ["هَذِهِ بَيْت", "هَذَا الْبَيْت", "بَيْت هَذِهِ"],
          "بَيْت is masculine, so هَذَا."),
        M("Which means “This is a school”?", "هَذِهِ مَدْرَسَة", ["هَذَا مَدْرَسَة", "هَذِهِ الْمَدْرَسَة", "مَدْرَسَة هَذَا"],
          "مَدْرَسَة is feminine, so هَذِهِ."),
        M("Which means “The house is big”?", "الْبَيْت كَبِير", ["بَيْت كَبِير", "كَبِير بَيْت", "هُوَ بَيْت كَبِير"],
          "Definite subject + indefinite predicate."),
        M("What is the Arabic word for “a” in “a book”?", "There is none", ["وَاحِد", "هَذَا", "الْ"],
          "Indefiniteness is shown by leaving off ال."),
        M("What does ال do?", "It makes a noun definite: “the”", ["It makes a noun plural", "It means “is”", "It makes a noun feminine"],
          "ال is the definite article."),
        F("___ مَدْرَسَة.", "هَذِهِ", ["هَذَا", "هُوَ", "أَنَا"], "مَدْرَسَة is feminine.", tr="This is a school."),
        F("___ كِتَاب.", "هَذَا", ["هَذِهِ", "هِيَ", "أَنْتِ"], "كِتَاب is masculine.", tr="This is a book."),
    ],
    verify=vf("طَالِب", "طَالِبَة") + vf("طَبِيب", "طَبِيبَة") + vw("هَذَا", "هَذِهِ"),
)

# ---------------------------------------------------------------------------- 23
L23 = lesson(
    "Jobs",
    "What do you do?",
    requires=["مدرس", "طبيب", "موظف", "مدير", "معلم", "عامل"],
    cards=[
        card("Masculine and feminine",
             "Most job words add ة for a woman, as you saw with طَالِب and طَالِبَة. The word does not otherwise "
             "change, so the feminine is easy to learn.",
             tables=[table(["English", "Man", "Woman"],
                           [["student", "طَالِب", "طَالِبَة"],
                            ["teacher", "مُدَرِّس", "مُدَرِّسَة"],
                            ["doctor", "طَبِيب", "طَبِيبَة"],
                            ["engineer", "مُهَنْدِس", "مُهَنْدِسَة"],
                            ["employee", "مُوَظَّف", "مُوَظَّفَة"],
                            ["manager", "مُدِير", "مُدِيرَة"]],
                           say=[1, 2], tlit=[1, 2])]),
        card("More jobs",
             "These nouns also change for gender with ة.",
             tables=[table(["English", "Man", "Woman"],
                           [["driver", "سَائِق", "سَائِقَة"], ["worker", "عَامِل", "عَامِلَة"],
                            ["journalist", "صَحَفِيّ", "صَحَفِيَّة"], ["seller", "بَائِع", "بَائِعَة"]],
                           say=[1, 2], tlit=[1, 2])]),
        card("What do you do?",
             "Ask مَاذَا تَعْمَل؟ to a man and مَاذَا تَعْمَلِين؟ to a woman, or ask what someone’s job is. The "
             "answer is a nominal sentence.",
             examples=[
                 ex("أَنَا مُهَنْدِس.", "I am an engineer.", "مُهَنْدِس"),
                 ex("هِيَ مُدَرِّسَة.", "She is a teacher.", "مُدَرِّسَة"),
                 ex("هُوَ سَائِق.", "He is a driver.", "سَائِق"),
             ]),
    ],
    exercises=[
        M("What is the feminine of مُهَنْدِس?", "مُهَنْدِسَة", ["مُهَنْدِسُون", "مُهَنْدِسَان", "هِيَ مُهَنْدِس"], "The feminine adds ة."),
        M("What is the feminine of مُدِير?", "مُدِيرَة", ["مُدِيرُون", "مُدِيرَان", "أَمِير"], "Add ة to make a woman manager."),
        M("What is the masculine of طَبِيبَة?", "طَبِيب", ["طَبِيبَان", "طَبَّاب", "طَبَّة"], "Drop the ة."),
        M("Which means “She is an engineer”?", "هِيَ مُهَنْدِسَة", ["هُوَ مُهَنْدِسَة", "هِيَ مُهَنْدِس", "هُوَ مُهَنْدِس"], "Pronoun and noun are both feminine."),
        M("Which means “I am a driver” (a man speaking)?", "أَنَا سَائِق", ["أَنَا سَائِقَة", "أَنْتَ سَائِق", "هِيَ سَائِق"], "A man says the masculine noun."),
        M("A woman says she is a student. Which sentence?", "أَنَا طَالِبَة", ["أَنَا طَالِب", "هُوَ طَالِبَة", "أَنَا طُلَّاب"], "A woman says the feminine noun."),
        M("What does مُوَظَّف mean?", "employee", ["manager", "teacher", "doctor"], "مُوَظَّف is someone who has a job (a post)."),
        F("هِيَ ___.", "مُدَرِّسَة", ["مُدَرِّس", "سَائِق", "طَالِب"], "The subject is feminine, so the predicate is too.", tr="She is a teacher."),
        F("هُوَ ___.", "طَبِيب", ["طَبِيبَة", "مُدَرِّسَة", "مُهَنْدِسَة"], "The subject is masculine.", tr="He is a doctor."),
    ],
    verify=(vf("طَالِب", "طَالِبَة") + vf("مُدَرِّس", "مُدَرِّسَة") + vf("طَبِيب", "طَبِيبَة")
            + vf("مُهَنْدِس", "مُهَنْدِسَة") + vf("مُوَظَّف", "مُوَظَّفَة") + vf("مُدِير", "مُدِيرَة")
            + vf("سَائِق", "سَائِقَة") + vf("عَامِل", "عَامِلَة") + vf("صَحَفِيّ", "صَحَفِيَّة")
            + vf("بَائِع", "بَائِعَة")),
)

# ---------------------------------------------------------------------------- 24
L24 = lesson(
    "Countries and nationalities",
    "مِصْر ← مِصْرِيّ",
    requires=["مصري", "سوري", "عراقي", "سعودي", "أمريكي", "عربي"],
    cards=[
        card("From country to nationality",
             "To say where a person is from, add the ending ـِيّ to the name of the country. The result is an "
             "adjective (called a nisba adjective) and it works like the job words: add ة for a woman. The article ال "
             "is dropped (الْعِرَاق → عِرَاقِيّ) and a few places lose a letter (سُورِيَا → سُورِيّ), but the pattern "
             "is very regular.",
             tables=[table(["Country", "Man", "Woman"],
                           [["مِصْر", "مِصْرِيّ", "مِصْرِيَّة"],
                            ["سُورِيَا", "سُورِيّ", "سُورِيَّة"],
                            ["الْعِرَاق", "عِرَاقِيّ", "عِرَاقِيَّة"],
                            ["الْيَمَن", "يَمَنِيّ", "يَمَنِيَّة"],
                            ["السُّودَان", "سُودَانِيّ", "سُودَانِيَّة"],
                            ["لُبْنَان", "لُبْنَانِيّ", "لُبْنَانِيَّة"]],
                           say=[0, 1, 2], tlit=[1], gloss=False)]),
        card("More nationalities",
             "Some country names have a different shape, but the nationality adjective follows the same ending.",
             tables=[table(["English", "Man", "Woman"],
                           [["American", "أَمْرِيكِيّ", "أَمْرِيكِيَّة"],
                            ["Saudi", "سُعُودِيّ", "سُعُودِيَّة"],
                            ["Moroccan", "مَغْرِبِيّ", "مَغْرِبِيَّة"],
                            ["Jordanian", "أُرْدُنِّيّ", "أُرْدُنِّيَّة"],
                            ["Arab", "عَرَبِيّ", "عَرَبِيَّة"],
                            ["Russian", "رُوسِيّ", "رُوسِيَّة"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("What is the feminine of مِصْرِيّ?", "مِصْرِيَّة", ["مِصْرِيَّات", "مِصْرِيَّان", "مَصْرِيّ"], "Add ة to the nisba adjective."),
        M("What is the masculine of عِرَاقِيَّة?", "عِرَاقِيّ", ["عِرَاقِيُّون", "عِرَاقِيَّان", "عَرَبِيّ"], "Drop the ة."),
        M("A man from Yemen is…", "يَمَنِيّ", ["يَمَنِيَّة", "يَمَنِيُّون", "الْيَمَن"], "Add ـِيّ to the country name."),
        M("A woman from Syria is…", "سُورِيَّة", ["سُورِيّ", "سُورِيَا", "سُورِيُّون"], "The feminine adds ة."),
        M("Which means “American” (a man)?", "أَمْرِيكِيّ", ["أَمْرِيكِيَّة", "أَمْرِيكَا", "عَرَبِيّ"], "أَمْرِيكِيّ is the masculine adjective."),
        M("Which means “Saudi” (a woman)?", "سُعُودِيَّة", ["سُعُودِيّ", "مَغْرِبِيَّة", "سُورِيَّة"], "سُعُودِيَّة is the feminine adjective."),
        F("هُوَ ___.", "مِصْرِيّ", ["مِصْرِيَّة", "مِصْر", "مِصْرِيُّون"], "A man from Egypt.", tr="He is Egyptian."),
        F("هِيَ ___.", "لُبْنَانِيَّة", ["لُبْنَانِيّ", "لُبْنَان", "لُبْنَانِيُّون"], "A woman from Lebanon.", tr="She is Lebanese."),
        F("أَنَا ___ (a man speaking).", "أَمْرِيكِيّ", ["أَمْرِيكِيَّة", "أَمْرِيكَا", "عَرَبِيَّة"], "A man says the masculine adjective.", tr="I am American."),
    ],
    verify=(vf("مِصْرِيّ", "مِصْرِيَّة") + vf("سُورِيّ", "سُورِيَّة") + vf("عِرَاقِيّ", "عِرَاقِيَّة")
            + vf("يَمَنِيّ", "يَمَنِيَّة") + vf("سُودَانِيّ", "سُودَانِيَّة") + vf("لُبْنَانِيّ", "لُبْنَانِيَّة")
            + vf("أَمْرِيكِيّ", "أَمْرِيكِيَّة") + vf("سُعُودِيّ", "سُعُودِيَّة") + vf("مَغْرِبِيّ", "مَغْرِبِيَّة")
            + vf("أُرْدُنِّيّ", "أُرْدُنِّيَّة") + vf("عَرَبِيّ", "عَرَبِيَّة") + vf("رُوسِيّ", "رُوسِيَّة")),
)

# ---------------------------------------------------------------------------- 25
L25 = lesson(
    "Where are you from?",
    "مِنْ أَيْنَ أَنْتَ؟",
    requires=["أين", "من", "بلد", "سعودي", "مصري"],
    cards=[
        card("Asking",
             "مِنْ أَيْنَ is “from where”. Put the pronoun after it, using the form for a man or a woman, and the "
             "answer starts with أَنَا مِنْ and a place, or with أَنَا and your nationality.",
             examples=[
                 ex("مِنْ أَيْنَ أَنْتَ؟", "Where are you from? (to a man)"),
                 ex("مِنْ أَيْنَ أَنْتِ؟", "Where are you from? (to a woman)"),
                 ex("أَنَا مِنْ مِصْر.", "I am from Egypt."),
                 ex("أَنَا مِصْرِيّ.", "I am Egyptian."),
             ]),
        card("A short conversation",
             "Two people meet at a conference.",
             examples=[
                 ex("أَهْلًا وَسَهْلًا. مِنْ أَيْنَ أَنْتِ؟", "Welcome. Where are you from?"),
                 ex("أَنَا مِنْ لُبْنَان. وَأَنْتَ؟", "I am from Lebanon. And you?"),
                 ex("أَنَا مِنَ الْمَغْرِب، لَكِنْ أَسْكُن فِي أَمْرِيكَا.", "I am from Morocco, but I live in America."),
             ]),
    ],
    exercises=[
        M("How do you ask a woman where she is from?", "مِنْ أَيْنَ أَنْتِ؟", ["مِنْ أَيْنَ أَنْتَ؟", "مَا اِسْمُكِ؟", "كَيْفَ حَالُكِ؟"], "أَنْتِ is the feminine “you”."),
        M("What does أَيْنَ mean?", "where", ["who", "how", "when"], "أَيْنَ = where."),
        M("What does مِنْ mean?", "from", ["in", "with", "to"], "مِنْ = from."),
        M("Which means “I am from Egypt”?", "أَنَا مِنْ مِصْر", ["أَنَا مِصْر", "أَنَا فِي مِصْر", "هُوَ مِنْ مِصْر"], "أَنَا مِنْ + place."),
        M("Which means “He is Lebanese”?", "هُوَ لُبْنَانِيّ", ["هُوَ لُبْنَانِيَّة", "هِيَ لُبْنَانِيّ", "هُوَ لُبْنَان"], "A masculine nisba adjective."),
        M("Which means “And you?” to a woman?", "وَأَنْتِ؟", ["وَأَنْتَ؟", "وَأَنَا؟", "وَهُوَ؟"], "و + أَنْتِ."),
        F("مِنْ ___ أَنْتَ؟", "أَيْنَ", ["كَيْفَ", "مَاذَا", "مَتَى"], "مِنْ أَيْنَ = from where.", tr="Where are you from?"),
        F("أَنَا مِنَ ___.", "الْعِرَاق", ["عِرَاقِيَّة", "عِرَاقِيّ", "هِيَ"], "After مِنْ comes a place name.", tr="I am from Iraq."),
    ],
    verify=vw("أَيْنَ", "مِنْ"),
)

# ---------------------------------------------------------------------------- 26
L26 = lesson(
    "My, your, his, her",
    "Pronouns attached to nouns",
    requires=["كتاب", "بيت", "أنا", "هو"],
    cards=[
        card("Endings instead of words",
             "Arabic does not have a separate word for “my” or “her”. It adds a short ending to the noun. You "
             "have already met two of them: اِسْمِي (my name) and اِسْمُكَ (your name).",
             tables=[table(["English", "Ending", "Example", "Meaning"],
                           [["my", "ـِي", "كِتَابِي", "my book"],
                            ["your (man)", "ـكَ", "كِتَابُكَ", "your book"],
                            ["your (woman)", "ـكِ", "كِتَابُكِ", "your book"],
                            ["his", "ـهُ", "كِتَابُهُ", "his book"],
                            ["her", "ـهَا", "كِتَابُهَا", "her book"]],
                           say=[2], tlit=[2], gloss=False)]),
        card("Our, your, their",
             "The plural endings are ـنَا (our), ـكُم (your, a group of men or mixed) and ـهُم (their). Add ـكُنَّ and "
             "ـهُنَّ for groups of women only. The noun itself does not change (except that ة becomes ت, see below), and an attached "
             "pronoun makes it definite, so it takes no ال.",
             tables=[table(["English", "Ending", "Example", "Meaning"],
                           [["our", "ـنَا", "بَيْتُنَا", "our house"],
                            ["your (all)", "ـكُم", "بَيْتُكُم", "your house"],
                            ["their", "ـهُم", "بَيْتُهُم", "their house"]],
                           say=[2], tlit=[2], gloss=False)]),
        card("A feminine noun changes its ة",
             "A word that ends in ة changes it to ت when an ending is added. So مَدْرَسَة (a school) becomes "
             "مَدْرَسَتِي (my school) and مَدْرَسَتُهَا (her school).",
             examples=[ex("مَدْرَسَتِي كَبِيرَة.", "My school is big.", "مَدْرَسَتِي"),
                       ex("بَيْتُنَا جَدِيد.", "Our house is new.", "بَيْتُنَا"),
                       ex("اِسْمُهَا لَيْلَى.", "Her name is Layla.", "اِسْمُهَا")]),
    ],
    exercises=[
        M("How do you say “my book”?", "كِتَابِي", ["كِتَابُكَ", "كِتَابُهُ", "الْكِتَابِي"], "ـِي = my."),
        M("How do you say “his house”?", "بَيْتُهُ", ["بَيْتُهَا", "بَيْتِي", "بَيْتُنَا"], "ـهُ = his."),
        M("How do you say “her house”?", "بَيْتُهَا", ["بَيْتُهُ", "بَيْتُكِ", "بَيْتُهُم"], "ـهَا = her."),
        M("How do you say “our house”?", "بَيْتُنَا", ["بَيْتِي", "بَيْتُكُم", "بَيْتُهُم"], "ـنَا = our."),
        M("How do you say “your book” to a woman?", "كِتَابُكِ", ["كِتَابُكَ", "كِتَابُهَا", "كِتَابِي"], "ـكِ = your (feminine)."),
        M("What happens to ة before an ending?", "It becomes ت", ["It disappears", "It stays ة", "It becomes ه"], "مَدْرَسَة → مَدْرَسَتِي."),
        M("How do you say “my school”?", "مَدْرَسَتِي", ["مَدْرَسَةِي", "مَدْرَسِي", "الْمَدْرَسَتِي"], "ة changes to ت."),
        M("Does a noun with an attached pronoun take ال?", "No: it is already definite", ["Yes, always", "Only if it is feminine", "Only in the plural"], "كِتَابِي = “my book”, not “the my book”."),
        F("اِسْمُ___ لَيْلَى.", "ـهَا", ["ـكَ", "ـنَا", "ـهُم"], "Her name: ـهَا.", tr="Her name is Layla."),
    ],
    verify=vw("كِتَابِي", "كِتَابُكَ", "كِتَابُهُ", "بَيْتُنَا", "مَدْرَسَتِي"),
)

# ---------------------------------------------------------------------------- 27
L27 = lesson(
    "He writes, she writes",
    "The verb comes first",
    requires=["كتب", "درس", "عمل", "ذهب", "سكن"],
    cards=[
        card("Verb–subject sentences",
             "Arabic sentences often begin with the verb, followed by the subject: “studies Ahmad”. “Ahmad "
             "studies” (أَحْمَد يَدْرُس) is also correct. A verb that comes first agrees with its subject in gender, but stays singular even when the "
             "subject is plural. In the present tense, the “he” form of a verb starts with يَـ and the “she” form with "
             "تَـ.",
             tables=[table(["Subject", "English", "Verb"],
                           [["أَحْمَد", "Ahmad", "يَدْرُس"], ["سَارَة", "Sara", "تَدْرُس"]],
                           say=[0, 2], tlit=[2], gloss=False)],
             examples=[
                 ex("يَدْرُس أَحْمَد فِي الْمَدْرَسَة.", "Ahmad studies at school.", "يَدْرُس"),
                 ex("تَدْرُس سَارَة فِي الْجَامِعَة.", "Sara studies at the university.", "تَدْرُس"),
                 ex("يَدْرُس الطُّلَّاب الْعَرَبِيَّة.", "The students study Arabic.", "يَدْرُس"),
             ]),
        card("A few verbs",
             "Four useful verbs, shown for “he” and “she”.",
             tables=[table(["English", "he…", "she…"],
                           [["write", "يَكْتُب", "تَكْتُب"], ["work", "يَعْمَل", "تَعْمَل"],
                            ["go", "يَذْهَب", "تَذْهَب"], ["live (reside)", "يَسْكُن", "تَسْكُن"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
    ],
    exercises=[
        M("Which means “Ahmad works”?", "يَعْمَل أَحْمَد", ["تَعْمَل أَحْمَد", "أَعْمَل أَحْمَد", "نَعْمَل أَحْمَد"], "A masculine subject: يَـ."),
        M("Which means “Sara works”?", "تَعْمَل سَارَة", ["يَعْمَل سَارَة", "أَعْمَل سَارَة", "يَعْمَلُون سَارَة"], "A feminine subject: تَـ."),
        M("The students study (verb first). Which is right?", "يَدْرُس الطُّلَّاب", ["يَدْرُسُون الطُّلَّاب", "أَدْرُس الطُّلَّاب", "نَدْرُس الطُّلَّاب"],
          "A verb before its subject stays singular."),
        M("Which means “She lives in Cairo”?", "تَسْكُن فِي الْقَاهِرَة", ["يَسْكُن فِي الْقَاهِرَة", "أَسْكُن فِي الْقَاهِرَة", "تَسْكُنُون فِي الْقَاهِرَة"], "Feminine, so تَـ."),
        M("Which is the verb “he goes”?", "يَذْهَب", ["تَذْهَب", "أَذْهَب", "نَذْهَب"], "يَـ = he.", lemma="ذهب:pres:huwa"),
        M("Which is the verb “she writes”?", "تَكْتُب", ["يَكْتُب", "أَكْتُب", "نَكْتُب"], "تَـ = she.", lemma="كتب:pres:hiya"),
        F("___ أَحْمَد فِي الْمَدْرَسَة.", "يَدْرُس", ["تَدْرُس", "أَدْرُس", "نَدْرُس"], "Ahmad is masculine.", tr="Ahmad studies at school."),
        F("___ سَارَة الدَّرْس.", "تَكْتُب", ["يَكْتُب", "أَكْتُب", "نَكْتُب"], "Sara is feminine.", tr="Sara writes the lesson."),
    ],
    verify=(vv("درس", "pres", huwa="يَدْرُس", hiya="تَدْرُس") + vv("كتب", "pres", huwa="يَكْتُب", hiya="تَكْتُب")
            + vv("عمل", "pres", huwa="يَعْمَل", hiya="تَعْمَل") + vv("ذهب", "pres", huwa="يَذْهَب", hiya="تَذْهَب")
            + vv("سكن", "pres", huwa="يَسْكُن", hiya="تَسْكُن")),
)

# ---------------------------------------------------------------------------- 28
L28 = lesson(
    "I write, we write",
    "أَ · نَ · تَ · يَ",
    requires=["كتب", "درس", "عمل", "أنا", "نحن"],
    cards=[
        card("A prefix for the subject",
             "In the present tense the person is shown by a prefix added to the same verb stem. The four "
             "prefixes are أَـ (I), نَـ (we), تَـ (you, and she) and يَـ (he). Because the verb itself shows "
             "who is meant, the pronoun is usually dropped: أَكْتُب is already “I write”.",
             tables=[table(["English", "Arabic"],
                           [["I write", "أَكْتُب"], ["we write", "نَكْتُب"], ["you write (man)", "تَكْتُب"], ["he writes", "يَكْتُب"],
                            ["she writes", "تَكْتُب"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("You (woman)",
             "When you speak to a woman, the verb adds the ending ـِين: تَكْتُبِين means “you (to a woman) write”.",
             examples=[ex("أَنْتَ تَكْتُب.", "You write. (to a man)"), ex("أَنْتِ تَكْتُبِين.", "You write. (to a woman)", "تَكْتُبِين")]),
        card("In a sentence",
             "These sentences all use verbs you know. The object follows the verb.",
             examples=[
                 ex("أَدْرُس الْعَرَبِيَّة.", "I study Arabic.", "أَدْرُس"),
                 ex("نَعْمَل فِي الْمَكْتَب.", "We work in the office.", "نَعْمَل"),
                 ex("أَسْكُن فِي بَيْت كَبِير.", "I live in a big house.", "أَسْكُن"),
             ]),
    ],
    exercises=[
        M("Which verb means “I study”?", "أَدْرُس", ["تَدْرُس", "يَدْرُس", "نَدْرُس"], "أَـ = I.", lemma="درس:pres:ana"),
        M("Which verb means “we study”?", "نَدْرُس", ["أَدْرُس", "تَدْرُس", "يَدْرُس"], "نَـ = we.", lemma="درس:pres:nahnu"),
        M("Which verb means “you (woman) write”?", "تَكْتُبِين", ["تَكْتُب", "أَكْتُب", "نَكْتُب"], "The feminine “you” adds ـِين.", lemma="كتب:pres:anti"),
        M("Which verb means “he writes”?", "يَكْتُب", ["تَكْتُب", "أَكْتُب", "نَكْتُب"], "يَـ = he.", lemma="كتب:pres:huwa"),
        M("Which means “I work”?", "أَعْمَل", ["نَعْمَل", "يَعْمَل", "تَعْمَل"], "أَـ = I.", lemma="عمل:pres:ana"),
        M("Which means “We work in the office”?", "نَعْمَل فِي الْمَكْتَب", ["أَعْمَل فِي الْمَكْتَب", "يَعْمَل فِي الْمَكْتَب", "تَعْمَل فِي الْمَكْتَب"], "نَـ = we."),
        M("Why is a pronoun usually not needed with a present-tense verb?", "The prefix already shows the subject", ["Arabic has no pronouns", "The pronoun comes after the verb", "Pronouns are only for questions"], "The prefix and the ending tell you who is meant."),
        F("___ فِي الْمَدْرَسَة.", "أَدْرُس", ["تَدْرُس", "يَدْرُس", "نَدْرُس"], "The speaker is “I”.", tr="I study at school."),
        F("نَحْنُ ___ فِي الْمَكْتَب.", "نَعْمَل", ["أَعْمَل", "يَعْمَل", "تَعْمَل"], "“We” takes نَـ.", tr="We work in the office."),
    ],
    verify=(vv("كتب", "pres", ana="أَكْتُب", nahnu="نَكْتُب", anta="تَكْتُب", anti="تَكْتُبِين", huwa="يَكْتُب", hiya="تَكْتُب")
            + vv("درس", "pres", ana="أَدْرُس", nahnu="نَدْرُس") + vv("عمل", "pres", ana="أَعْمَل", nahnu="نَعْمَل")
            + vv("سكن", "pres", ana="أَسْكُن")),
)

# ---------------------------------------------------------------------------- 29
L29 = lesson(
    "Tomorrow: the future with سَ",
    "سَأَكْتُب · سَنَذْهَب",
    requires=["غد", "كتب", "ذهب", "درس"],
    cards=[
        card("One small prefix",
             "To talk about the future, put سَـ (or سَوْفَ as a separate word) in front of the present-tense verb. "
             "Nothing else changes, which makes this one of the easiest tenses in the language. سَـ is joined to the "
             "verb; سَوْفَ is written separately.",
             tables=[table(["English", "Arabic"],
                           [["I write", "أَكْتُب"], ["I will write", "سَأَكْتُب"],
                            ["we go", "نَذْهَب"], ["we will go", "سَنَذْهَب"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Time words for the future",
             "غَدًا is “tomorrow”, and الْيَوْم is “today”. The next words fill out the future.",
             tables=[table(["English", "Arabic"],
                           [["today", "الْيَوْم"], ["tomorrow", "غَدًا"], ["the day after tomorrow", "بَعْدَ غَد"],
                            ["next week", "الْأُسْبُوع الْقَادِم"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[ex("سَأَذْهَب إِلَى الْمَدْرَسَة غَدًا.", "I will go to school tomorrow.", "سَأَذْهَب"),
                       ex("سَوْفَ نَدْرُس الْعَرَبِيَّة.", "We will study Arabic.", "سَوْفَ"),
                       ex("هَلْ سَتَكْتُب؟", "Will you write?", "سَتَكْتُب")]),
    ],
    exercises=[
        M("Which means “I will write”?", "سَأَكْتُب", ["أَكْتُب", "كَتَبْتُ", "سَيَكْتُب"], "سَـ + أَكْتُب.", lemma="كتب:fut:ana"),
        M("Which means “we will go”?", "سَنَذْهَب", ["نَذْهَب", "سَأَذْهَب", "سَيَذْهَب"], "سَـ + نَذْهَب.", lemma="ذهب:fut:nahnu"),
        M("Which means “he will study”?", "سَيَدْرُس", ["يَدْرُس", "سَتَدْرُس", "سَأَدْرُس"], "سَـ + يَدْرُس.", lemma="درس:fut:huwa"),
        M("Which means “she will work”?", "سَتَعْمَل", ["تَعْمَل", "سَيَعْمَل", "سَأَعْمَل"], "سَـ + تَعْمَل.", lemma="عمل:fut:hiya"),
        M("What does غَدًا mean?", "tomorrow", ["today", "yesterday", "now"], "غَدًا = tomorrow."),
        M("How else can you say “will” in front of a verb?", "سَوْفَ", ["قَدْ", "لَقَد", "كَانَ"], "سَوْفَ is the spaced-out form of سَـ."),
        M("Which means “I will go to school tomorrow”?", "سَأَذْهَب إِلَى الْمَدْرَسَة غَدًا", ["أَذْهَب إِلَى الْمَدْرَسَة أَمْس", "ذَهَبْتُ إِلَى الْمَدْرَسَة غَدًا", "سَيَذْهَب إِلَى الْمَدْرَسَة غَدًا"], "I = أَـ, with سَـ for the future."),
        F("___ نَدْرُس غَدًا.", "سَوْفَ", ["قَدْ", "لَا", "مَا"], "The future particle.", tr="We will study tomorrow."),
    ],
    verify=(vv("كتب", "fut", ana="سَأَكْتُب") + vv("ذهب", "fut", nahnu="سَنَذْهَب") + vv("درس", "fut", huwa="سَيَدْرُس")
            + vv("عمل", "fut", hiya="سَتَعْمَل") + vw("غَدًا")),
)

# ---------------------------------------------------------------------------- 30
L30 = lesson(
    "Filling in a form",
    "الِاسْم · الْعُنْوَان · رَقْم الْهَاتِف",
    requires=["عمر", "عنوان", "هاتف", "وظيفة", "جنسية", "رقم"],
    cards=[
        card("Words on a form",
             "Forms in Arabic use a fixed set of nouns. Learn to read them and you can fill in almost any application.",
             tables=[table(["English", "Arabic"],
                           [["name", "الِاسْم"], ["nationality", "الْجِنْسِيَّة"], ["job", "الْوَظِيفَة"],
                            ["address", "الْعُنْوَان"], ["phone number", "رَقْم الْهَاتِف"],
                            ["date of birth", "تَارِيخ الْمِيلَاد"], ["age", "الْعُمْر"]],
                           say=[1], tlit=[1])]),
        card("A completed form",
             "Each line gives the label, a colon and the answer.",
             examples=[
                 ex("الِاسْم: خَالِد", "Name: Khalid", "الِاسْم"),
                 ex("الْجِنْسِيَّة: سُعُودِيّ", "Nationality: Saudi", "الْجِنْسِيَّة"),
                 ex("الْوَظِيفَة: مُهَنْدِس", "Job: engineer", "الْوَظِيفَة"),
                 ex("الْعُنْوَان: شَارِع الْجَامِعَة", "Address: University Street", "الْعُنْوَان"),
             ]),
        card("Answering out loud",
             "To answer the questions in speech, use the attached endings you learned.",
             examples=[
                 ex("مَا جِنْسِيَّتُك؟", "What is your nationality?"),
                 ex("جِنْسِيَّتِي مِصْرِيَّة.", "My nationality is Egyptian."),
                 ex("مَا وَظِيفَتُك؟", "What is your job?"),
                 ex("وَظِيفَتِي مُدَرِّسَة.", "My job is teacher. (a woman speaking)"),
             ]),
    ],
    exercises=[
        M("Which word on a form means “name”?", "الِاسْم", ["الْعُنْوَان", "الْجِنْسِيَّة", "الْعُمْر"], "الِاسْم = name."),
        M("Which means “address”?", "الْعُنْوَان", ["الِاسْم", "الْوَظِيفَة", "الْعُمْر"], "الْعُنْوَان = address."),
        M("Which means “nationality”?", "الْجِنْسِيَّة", ["الْوَظِيفَة", "الْعُنْوَان", "الِاسْم"], "الْجِنْسِيَّة = nationality."),
        M("Which means “job”?", "الْوَظِيفَة", ["الْجِنْسِيَّة", "الْعُمْر", "الْعُنْوَان"], "الْوَظِيفَة = job."),
        M("What does رَقْم الْهَاتِف ask for?", "a phone number", ["a postcode", "an address", "an age"], "رَقْم = number; هَاتِف = telephone."),
        M("How do you say “my nationality”?", "جِنْسِيَّتِي", ["جِنْسِيَّةِي", "جِنْسِيَّتُك", "جِنْسِيَّتُهَا"], "ة becomes ت before an ending."),
        M("How do you say “What is your job?” to a man?", "مَا وَظِيفَتُكَ؟", ["مَا وَظِيفَتِي؟", "مَا وَظِيفَتُكِ؟", "مَاذَا وَظِيفَة؟"], "ـكَ for a man."),
        F("___ الْهَاتِف", "رَقْم", ["اِسْم", "عُمْر", "بَيْت"], "A phone number is رَقْم الْهَاتِف.", tr="phone number"),
        F("جِنْسِيَّتِي ___.", "مِصْرِيَّة", ["مِصْر", "مِصْرِيَّان", "مِصْرِيُّون"], "In a full sentence the adjective agrees with جِنْسِيَّة, which is feminine.", tr="My nationality is Egyptian."),
    ],
    verify=vw("الْجِنْسِيَّة", "الْعُنْوَان", "الْوَظِيفَة"),
)

# ---------------------------------------------------------------------------- 31
L31 = lesson(
    "Review: meeting someone",
    "Greetings, introductions and a first conversation",
    requires=["مرحبا", "طالب", "عمل", "بلد", "كيف", "أنا"],
    cards=[
        card("A first meeting",
             "Read the conversation, then use it for the exercises. Sara is a student; Maher works at a bank.",
             examples=[
                 ex("السَّلَام عَلَيْكُم. أَنَا مَاهِر.", "Peace be upon you. I am Maher."),
                 ex("وَعَلَيْكُمُ السَّلَام. أَنَا سَارَة. تَشَرَّفْنَا.", "And upon you, peace. I am Sara. Pleased to meet you."),
                 ex("مِنْ أَيْنَ أَنْتِ يَا سَارَة؟", "Where are you from, Sara?"),
                 ex("أَنَا مِنَ الْأُرْدُنّ، لَكِنْ أَدْرُس فِي أَمْرِيكَا.", "I am from Jordan, but I study in America."),
                 ex("وَمَاذَا تَدْرُسِين؟", "And what do you study?"),
                 ex("أَدْرُس الطِّبّ. وَأَنْتَ، مَاذَا تَعْمَل؟", "I study medicine. And you, what do you do?"),
                 ex("أَنَا مُوَظَّف فِي بَنْك.", "I am a bank employee."),
             ]),
    ],
    exercises=[
        M("Maher begins with السَّلَام عَلَيْكُم. What does Sara answer?", "وَعَلَيْكُمُ السَّلَام", ["صَبَاح النُّور", "مَعَ السَّلَامَة", "عَفْوًا"], "The reply to the Islamic greeting."),
        M("How does Sara say she is from Jordan?", "أَنَا مِنَ الْأُرْدُنّ", ["أَنَا فِي الْأُرْدُنّ", "هِيَ مِنَ الْأُرْدُنّ", "أَنْتِ مِنَ الْأُرْدُنّ"], "أَنَا مِنْ + place."),
        M("Maher asks Sara where she is from. Which question is for a woman?", "مِنْ أَيْنَ أَنْتِ؟", ["مِنْ أَيْنَ أَنْتَ؟", "مِنْ أَيْنَ هُوَ؟", "مِنْ أَيْنَ هِيَ؟"], "أَنْتِ is feminine."),
        M("What does Maher do?", "He is a bank employee", ["He is a student", "He is a doctor", "He is a teacher"], "أَنَا مُوَظَّف فِي بَنْك."),
        M("Which sentence means “She is a student”?", "هِيَ طَالِبَة", ["هُوَ طَالِبَة", "هِيَ طَالِب", "أَنَا طَالِبَة"], "Feminine pronoun, feminine noun."),
        M("Which means “My name is Sara”?", "اِسْمِي سَارَة", ["اِسْمُكِ سَارَة", "اِسْمُهَا سَارَة", "اِسْمُنَا سَارَة"], "ـِي = my."),
        M("Which means “We work in the office”?", "نَعْمَل فِي الْمَكْتَب", ["أَعْمَل فِي الْمَكْتَب", "يَعْمَل فِي الْمَكْتَب", "تَعْمَل فِي الْمَكْتَب"], "نَـ = we."),
        M("Which is the feminine of مُدَرِّس?", "مُدَرِّسَة", ["مُدَرِّسُون", "مُدَرِّسَان", "مُدِير"], "Add ة."),
        M("Which means “I will study tomorrow”?", "سَأَدْرُس غَدًا", ["أَدْرُس غَدًا", "سَيَدْرُس غَدًا", "دَرَسْتُ غَدًا"], "سَـ + أَدْرُس."),
        F("___ الْخَيْر", "مَسَاء", ["صَبَاح", "مَعَ", "إِلَى"], "An evening greeting.", tr="Good evening"),
    ],
)

UNIT = unit("التعارف: greetings and introductions", [L16, L17, L18, L19, L20, L21, L22, L23, L24, L25, L26, L27, L28, L29, L30, L31])
