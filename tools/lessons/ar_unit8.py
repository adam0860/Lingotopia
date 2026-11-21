"""Unit 8: كَانَ, "used to", and free time (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 107
L107 = lesson(
    "Things I like to do",
    "أُحِبّ أَنْ أَلْعَب · أُحِبّ الْمُوسِيقَى",
    requires=["لعب", "رياضة", "كرة", "موسيقى", "فيلم", "شاهد"],
    cards=[
        card("Free-time activities",
             "Here are seven things people do in their free time, all with the present-tense “I” form. "
             "Most of the verbs take the same أَـ prefix as أَكْتُب and أَدْرُس, though the middle vowel can differ: أَلْعَب, أَسْبَح.",
             tables=[table(["English", "Arabic"],
                           [["I play football", "أَلْعَب كُرَة الْقَدَم"], ["I swim in the sea", "أَسْبَح فِي الْبَحْر"],
                            ["I read a book", "أَقْرَأ كِتَاب"], ["I listen to music", "أَسْمَع الْمُوسِيقَى"],
                            ["I watch a film", "أُشَاهِد فِيلْم"], ["I ride a bicycle", "أَرْكَب الدَّرَّاجَة"],
                            ["I visit my friends", "أَزُور أَصْدِقَائِي"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("I like…",
             "There are two ways to say what you like. After أُحِبّ you can put a noun, or أَنْ and a present verb "
             "(the pattern you know from يَجِب أَنْ). The verb after أَنْ shows who does the action; for “I like to…” it is also the “I” form.",
             examples=[
                 ex("أُحِبّ الْمُوسِيقَى.", "I like music.", "أُحِبّ"),
                 ex("أُحِبّ أَنْ أَلْعَب كُرَة الْقَدَم.", "I like to play football.", "أُحِبّ أَنْ"),
                 ex("أُحِبّ أَنْ أَسْبَح فِي الصَّيْف.", "I like to swim in summer.", "أُحِبّ أَنْ"),
                 ex("هَلْ تُحِبّ السِّينَمَا؟", "Do you like the cinema? (to a man)", "تُحِبّ"),
                 ex("مَاذَا تُحِبّ أَنْ تَفْعَل فِي وَقْت الْفَرَاغ؟", "What do you like to do in your free time? (to a man)", "تُحِبّ أَنْ"),
                 ex("أُحِبّ أَنْ أَقْرَأ وَأَسْمَع الْمُوسِيقَى.", "I like to read and listen to music.", "أُحِبّ أَنْ"),
             ]),
    ],
    exercises=[
        M("What does أَسْبَح mean?", "I swim", ["I read", "I play", "I ride"], "سَبَحَ = to swim."),
        M("What does أَرْكَب الدَّرَّاجَة mean?", "I ride a bicycle", ["I visit my friends", "I watch a film", "I read a book"], "رَكِبَ = to ride."),
        M("Which means “I like music”?", "أُحِبّ الْمُوسِيقَى", ["أُحِبّ أَنْ الْمُوسِيقَى", "أُحِبّ أَنْ أَسْبَح", "هَلْ تُحِبّ الْمُوسِيقَى"], "أُحِبّ + noun."),
        M("Which means “I like to swim”?", "أُحِبّ أَنْ أَسْبَح", ["أُحِبّ أَسْبَح", "أُحِبّ السِّبَاحَة أَنْ", "أُحِبّ أَنْ تَسْبَح"], "أُحِبّ + أَنْ + أَسْبَح."),
        M("Which asks a man “Do you like the cinema?”", "هَلْ تُحِبّ السِّينَمَا؟", ["هَلْ أُحِبّ السِّينَمَا؟", "مَاذَا تُحِبّ السِّينَمَا؟", "هَلْ يُحِبّ السِّينَمَا؟"], "تُحِبّ = you like (to a man)."),
        M("Which means “What do you like to do in your free time?” (to a man)", "مَاذَا تُحِبّ أَنْ تَفْعَل فِي وَقْت الْفَرَاغ؟", ["أَيْنَ تُحِبّ أَنْ تَفْعَل فِي وَقْت الْفَرَاغ؟", "مَنْ تُحِبّ أَنْ تَفْعَل فِي وَقْت الْفَرَاغ؟", "مَاذَا أُحِبّ أَنْ أَفْعَل فِي وَقْت الْفَرَاغ؟"], "مَاذَا = what; تُحِبّ = you like."),
        F("___ كُرَة الْقَدَم.", "أَلْعَب", ["أَسْبَح", "أَزُور", "أَرْكَب"], "You play a ball game.", tr="I play football."),
        F("أُحِبّ أَنْ ___ فِي الْبَحْر.", "أَسْبَح", ["أَقْرَأ", "أَزُور", "أَرْكَب"], "You swim in the sea.", tr="I like to swim in the sea."),
        F("أُحِبّ ___ أَقْرَأ كِتَاب.", "أَنْ", ["هَلْ", "مَنْ", "لَا"], "أُحِبّ أَنْ + verb.", tr="I like to read a book."),
    ],
    verify=(vv("لعب", "pres", ana="أَلْعَب") + vv("سبح", "pres", ana="أَسْبَح") + vv("قرأ", "pres", ana="أَقْرَأ")
            + vv("سمع", "pres", ana="أَسْمَع") + vv("ركب", "pres", ana="أَرْكَب") + vv("فعل", "pres", anta="تَفْعَل")
            + vpb("صَدِيق", "أَصْدِقَاء") + vw("أُشَاهِد", "أَزُور", "أُحِبّ", "تُحِبّ", "السِّينَمَا", "الْفَرَاغ")),
)

# ---------------------------------------------------------------------------- 108
L108 = lesson(
    "Was: كَانَ",
    "كَانَ الْجَوّ جَمِيلًا · كَانَتِ الْمَدِينَة كَبِيرَةً",
    requires=["كان", "جو", "جميل", "مدينة", "كبير", "أمس"],
    cards=[
        card("The verb كَانَ",
             "Until now every sentence about “now” had no verb for “is”. To say “was”, put كَانَ first and then the "
             "subject. كَانَ is a verb, so it agrees with the subject: كَانَ for a masculine subject, كَانَتْ for a "
             "feminine one. The description that follows gets the same ending as after لَيْسَ: ـًا, or ـَةً on a "
             "feminine word. Before ال, كَانَتْ takes a helping kasra: كَانَتِ الْمَدِينَة.",
             tables=[table(["Now", "Was"],
                           [["الْجَوّ جَمِيل", "كَانَ الْجَوّ جَمِيلًا"], ["الْمَدِينَة كَبِيرَة", "كَانَتِ الْمَدِينَة كَبِيرَةً"],
                            ["الْبَيْت قَدِيم", "كَانَ الْبَيْت قَدِيمًا"], ["الشَّارِع طَوِيل", "كَانَ الشَّارِع طَوِيلًا"],
                            ["الْغُرْفَة صَغِيرَة", "كَانَتِ الْغُرْفَة صَغِيرَةً"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Yesterday, last week",
             "Words like أَمْس (yesterday) and الْمَاضِي (last, past) place the sentence in the past.",
             examples=[
                 ex("كَانَ الْجَوّ جَمِيلًا أَمْس.", "The weather was nice yesterday.", "كَانَ"),
                 ex("كَانَتِ الْمَدِينَة كَبِيرَةً وَجَمِيلَةً.", "The city was big and beautiful.", "كَانَتِ"),
                 ex("كَانَ الْأُسْبُوع الْمَاضِي طَوِيلًا.", "Last week was long.", "كَانَ"),
                 ex("كَانَ الشِّتَاء الْمَاضِي بَارِدًا.", "Last winter was cold.", "كَانَ"),
                 ex("كَانَتِ الْمَدْرَسَة قَرِيبَةً مِنَ الْبَيْت.", "The school was close to the house.", "كَانَتِ"),
             ]),
    ],
    exercises=[
        M("Which means “The weather was nice”?", "كَانَ الْجَوّ جَمِيلًا", ["الْجَوّ جَمِيل", "كَانَتِ الْجَوّ جَمِيلًا", "كَانَ الْجَوّ جَمِيلَةً"], "كَانَ + subject + the description."),
        M("Which means “The city was big”?", "كَانَتِ الْمَدِينَة كَبِيرَةً", ["كَانَ الْمَدِينَة كَبِيرًا", "الْمَدِينَة كَبِيرَة", "كَانَتِ الْمَدِينَة كَبِيرُون"], "مَدِينَة is feminine: كَانَتْ."),
        M("Which verb goes with الْبَيْت (masculine)?", "كَانَ", ["كَانَتْ", "كُنْتُ", "كُنَّا"], "A masculine subject takes كَانَ."),
        M("Which verb goes with الْغُرْفَة (feminine)?", "كَانَتْ", ["كَانَ", "كُنْتَ", "كَانُوا"], "A feminine subject takes كَانَتْ."),
        M("What does أَمْس mean?", "yesterday", ["tomorrow", "today", "last year"], "أَمْس = yesterday."),
        M("Which means “Last winter was cold”?", "كَانَ الشِّتَاء الْمَاضِي بَارِدًا", ["كَانَ الشِّتَاء الْقَادِم بَارِدًا", "الشِّتَاء الْمَاضِي بَارِد", "كَانَتِ الشِّتَاء الْمَاضِي بَارِدَةً"], "الْمَاضِي = past, last."),
        F("___ الْبَيْت قَدِيمًا.", "كَانَ", ["كَانَتِ", "كُنْتُ", "كَانُوا"], "A masculine subject.", tr="The house was old."),
        F("كَانَتِ الْمَدْرَسَة ___.", "قَرِيبَةً", ["قَرِيبًا", "قَرِيبُون", "قَرِيبَات"], "Feminine, singular.", tr="The school was near."),
        F("كَانَ الْجَوّ ___ أَمْس.", "جَمِيلًا", ["جَمِيلَةً", "جَمِيلُون", "جَمِيلَات"], "Masculine, singular.", tr="The weather was nice yesterday."),
    ],
    verify=vw("كَانَ", "كَانَتِ", "جَمِيلًا", "كَبِيرَةً", "قَدِيمًا", "طَوِيلًا", "صَغِيرَةً", "بَارِدًا", "قَرِيبَةً", "الْمَاضِي", "الْأُسْبُوع", "أَمْس"),
)

# ---------------------------------------------------------------------------- 109
L109 = lesson(
    "I was, you were: كُنْتُ · كُنْتَ · كُنْتِ",
    "كُنْتُ طَالِبًا · كُنْتِ سَعِيدَةً · كُنَّا فِي الْبَيْت",
    requires=["كان", "طالب", "سعيد", "صغير", "أنا", "هو"],
    cards=[
        card("Was: six persons",
             "The past tense changes at the END of the word. With “I”, “you” and “we” the middle ا of كَانَ falls out "
             "and a ضَمَّة replaces it: كُنْتُ, كُنَّا. With “he” and “she” the ا stays.",
             tables=[table(["Person", "Pronoun", "Was"],
                           [["I", "أَنَا", "كُنْتُ"], ["you (man)", "أَنْتَ", "كُنْتَ"], ["you (woman)", "أَنْتِ", "كُنْتِ"],
                            ["he", "هُوَ", "كَانَ"], ["she", "هِيَ", "كَانَتْ"], ["we", "نَحْنُ", "كُنَّا"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("With a description",
             "The description that follows takes ـًا (or ـَةً) and agrees with the person: a man says طَالِبًا, a woman "
             "says طَالِبَةً.",
             examples=[
                 ex("كُنْتُ طَالِبًا فِي الْقَاهِرَة.", "I was a student in Cairo. (a man speaking)", "كُنْتُ"),
                 ex("كُنْتُ طَالِبَةً فِي جَامِعَة كَبِيرَة.", "I was a student at a big university. (a woman speaking)", "كُنْتُ"),
                 ex("كُنْتَ سَعِيدًا يَا أَحْمَد.", "You were happy, Ahmad. (to a man)", "كُنْتَ"),
                 ex("كُنْتِ مَشْغُولَةً أَمْس يَا سَارَة.", "You were busy yesterday, Sara. (to a woman)", "كُنْتِ"),
                 ex("كَانَ أَخِي صَغِيرًا.", "My brother was little.", "كَانَ"),
                 ex("كُنَّا فِي الْبَيْت.", "We were at home.", "كُنَّا"),
             ]),
    ],
    exercises=[
        M("Which form means “I was”?", "كُنْتُ", ["كُنْتَ", "كَانَ", "كُنَّا"], "كُنْتُ = I was."),
        M("Which form means “you (woman) were”?", "كُنْتِ", ["كُنْتَ", "كُنْتُ", "كَانَتْ"], "The kasra marks a woman."),
        M("Which form means “she was”?", "كَانَتْ", ["كَانَ", "كُنْتِ", "كُنَّا"], "كَانَتْ = she was."),
        M("Which form means “we were”?", "كُنَّا", ["كُنْتُ", "كُنْتَ", "كَانَ"], "كُنَّا = we were."),
        M("A woman says “I was a student”. Which is right?", "كُنْتُ طَالِبَةً", ["كُنْتِ طَالِبَةً", "كُنْتُ طَالِبًا", "كَانَتْ طَالِبَةً"], "كُنْتُ for “I”, and ـَةً for a woman."),
        M("Which means “You (man) were happy”?", "كُنْتَ سَعِيدًا", ["كُنْتِ سَعِيدًا", "كُنْتُ سَعِيدًا", "كَانَ سَعِيدًا"], "كُنْتَ for a man."),
        M("What happens to the middle ا of كَانَ in كُنْتُ?", "it drops out", ["it becomes و", "it is doubled", "it stays"], "كَانَ → كُنْتُ."),
        F("نَحْنُ ___ فِي الْبَيْت.", "كُنَّا", ["كُنْتُ", "كُنْتِ", "كَانَتْ"], "Whole group, “we”.", tr="We were at home."),
        F("أَخِي ___ صَغِيرًا.", "كَانَ", ["كُنْتُ", "كَانَتْ", "كُنَّا"], "My brother = he.", tr="My brother was little."),
    ],
    verify=vw("كُنْتُ", "كُنْتَ", "كُنْتِ", "كَانَ", "كَانَتْ", "كُنَّا", "طَالِبًا", "طَالِبَةً", "سَعِيدًا", "مَشْغُولَةً", "صَغِيرًا"),
)

# ---------------------------------------------------------------------------- 110
L110 = lesson(
    "You all were, they were",
    "كُنْتُمْ · كَانُوا · كُنَّ · كَانَا · كَانَتَا",
    requires=["كان", "طالب", "مدرسة", "حديقة", "سعيد", "طفل"],
    cards=[
        card("Was: the rest of the persons",
             "A group of men ends in ـُوا (with a silent alif), two people end in ـَا (or ـَتَا for women), and a group of "
             "women ends in ـْنَ (كُنْ + نَ → كُنَّ). For “you”, the stem كُنْـ is followed by تُ and the ending of the person: كُنْتُمْ, كُنْتُنَّ.",
             tables=[table(["Person", "Pronoun", "Was"],
                           [["you two", "أَنْتُمَا", "كُنْتُمَا"], ["you (men / mixed)", "أَنْتُمْ", "كُنْتُمْ"],
                            ["you (women)", "أَنْتُنَّ", "كُنْتُنَّ"], ["they two (men)", "هُمَا", "كَانَا"],
                            ["they two (women)", "هُمَا", "كَانَتَا"], ["they (men / mixed)", "هُمْ", "كَانُوا"],
                            ["they (women)", "هُنَّ", "كُنَّ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("In sentences",
             "With a plural description a broken plural takes ـًا (طُلَّابًا), a plural with ـَات keeps its ending, "
             "and سُعَدَاء (happy, plural) takes no extra ending. A verb that comes before its subject stays "
             "singular, as you learned: كَانَ الطُّلَّاب سُعَدَاء.",
             examples=[
                 ex("كُنْتُمْ سُعَدَاء فِي الْمَدْرَسَة.", "You (all) were happy at school.", "كُنْتُمْ"),
                 ex("هُمْ كَانُوا طُلَّابًا فِي الْجَامِعَة.", "They were students at the university.", "كَانُوا"),
                 ex("الْبِنْتَان كَانَتَا فِي الْحَدِيقَة.", "The two girls were in the garden.", "كَانَتَا"),
                 ex("أَنْتُنَّ كُنْتُنَّ فِي الْمَكْتَبَة.", "You (women) were in the library.", "كُنْتُنَّ"),
                 ex("الْمُدَرِّسَات كُنَّ مَشْغُولَات.", "The (women) teachers were busy.", "كُنَّ"),
                 ex("كَانَ الطُّلَّاب سُعَدَاء.", "The students were happy.", "كَانَ"),
             ]),
    ],
    exercises=[
        M("Which form means “they (men) were”?", "كَانُوا", ["كُنْتُمْ", "كُنَّ", "كَانَا"], "ـُوا = a group of men."),
        M("Which form means “they (women) were”?", "كُنَّ", ["كَانُوا", "كُنَّا", "كَانَتَا"], "كُنَّ ends in the feminine plural."),
        M("Which form means “you (men) were”?", "كُنْتُمْ", ["كُنْتُنَّ", "كُنْتُمَا", "كَانُوا"], "كُنْتُمْ."),
        M("Which form means “they two (women) were”?", "كَانَتَا", ["كَانَا", "كَانَتْ", "كُنَّ"], "ـَتَا = two women or things."),
        M("Which form means “they two (men) were”?", "كَانَا", ["كَانَتَا", "كَانُوا", "كَانَ"], "كَانَا = two masculine."),
        M("Which form means “you two were”?", "كُنْتُمَا", ["كُنْتُمْ", "كَانَا", "كُنَّا"], "كُنْتُمَا."),
        M("Which is right? “The students were happy” with the verb first.", "كَانَ الطُّلَّاب سُعَدَاء", ["كَانُوا الطُّلَّاب سُعَدَاء", "كُنْتُمْ الطُّلَّاب سُعَدَاء", "كُنَّ الطُّلَّاب سُعَدَاء"], "A verb before its subject stays singular."),
        F("الْبِنْتَان ___ فِي الْحَدِيقَة.", "كَانَتَا", ["كَانَا", "كَانَتْ", "كَانُوا"], "Two girls.", tr="The two girls were in the garden."),
        F("هُمْ ___ طُلَّابًا.", "كَانُوا", ["كُنْتُمْ", "كُنَّ", "كَانَ"], "They (men).", tr="They were students."),
    ],
    verify=vw("كُنْتُمَا", "كُنْتُمْ", "كُنْتُنَّ", "كَانَا", "كَانَتَا", "كَانُوا", "كُنَّ", "سُعَدَاء", "طُلَّابًا", "مَشْغُولَات", "الْبِنْتَان", "الْمُدَرِّسَات"),
)

# ---------------------------------------------------------------------------- 111
L111 = lesson(
    "Where were you?",
    "أَيْنَ كُنْتَ؟ · كَيْفَ كَانَ الْجَوّ؟",
    requires=["أين", "كيف", "متى", "من", "كان", "أمس"],
    cards=[
        card("Questions with كَانَ",
             "A question word goes first and كَانَ follows it. The answer begins with كَانَ or كُنْتُ and the place "
             "or description comes after.",
             tables=[table(["Question", "Answer"],
                           [["أَيْنَ كُنْتَ أَمْس؟", "كُنْتُ فِي الْبَيْت."], ["كَيْفَ كَانَ الْجَوّ؟", "كَانَ حَارًّا."],
                            ["مَنْ كَانَ مَعَكَ؟", "كَانَ أَخِي مَعِي."], ["مَتَى كَانَتِ الْحَفْلَة؟", "كَانَتْ أَمْس."],
                            ["هَلْ كُنْتَ فِي الْقَاهِرَة؟", "نَعَمْ، كُنْتُ هُنَاك."]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("A short conversation",
             "Two friends talk about yesterday.",
             examples=[
                 ex("أَيْنَ كُنْتَ أَمْس يَا أَحْمَد؟", "Where were you yesterday, Ahmad? (to a man)", "أَيْنَ كُنْتَ"),
                 ex("كُنْتُ فِي الْمَكْتَبَة مَعَ صَدِيقِي.", "I was in the library with my friend.", "كُنْتُ"),
                 ex("وَكَيْفَ كَانَتِ الْمَكْتَبَة؟", "And how was the library?", "كَيْفَ كَانَتِ"),
                 ex("كَانَتْ كَبِيرَةً وَجَمِيلَةً.", "It was big and beautiful.", "كَانَتْ"),
                 ex("وَمَنْ كَانَ مَعَكَ؟", "And who was with you? (to a man)", "مَنْ كَانَ"),
                 ex("كَانَتْ مَعِي سَارَة.", "Sara was with me.", "كَانَتْ"),
             ]),
    ],
    exercises=[
        M("Which asks a man “Where were you?”", "أَيْنَ كُنْتَ؟", ["أَيْنَ كُنْتِ؟", "أَيْنَ كُنْتُ؟", "كَيْفَ كُنْتَ؟"], "كُنْتَ for a man."),
        M("Which asks a woman “Where were you?”", "أَيْنَ كُنْتِ؟", ["أَيْنَ كُنْتَ؟", "أَيْنَ كَانَتْ؟", "مَتَى كُنْتِ؟"], "كُنْتِ for a woman."),
        M("Which asks “How was the weather?”", "كَيْفَ كَانَ الْجَوّ؟", ["أَيْنَ كَانَ الْجَوّ؟", "مَنْ كَانَ الْجَوّ؟", "كَيْفَ كُنْتُ الْجَوّ؟"], "كَيْفَ = how."),
        M("Which asks “When was the party?”", "مَتَى كَانَتِ الْحَفْلَة؟", ["مَتَى كُنَّا الْحَفْلَة؟", "أَيْنَ كَانَتِ الْحَفْلَة؟", "مَنْ كَانَتِ الْحَفْلَة؟"], "مَتَى = when; حَفْلَة is feminine."),
        M("Which asks a man “Who was with you?”", "مَنْ كَانَ مَعَكَ؟", ["مَنْ كَانَ مَعَكِ؟", "أَيْنَ كَانَ مَعَكَ؟", "مَنْ كُنْتَ مَعِي؟"], "مَعَكَ = with you (man)."),
        M("Which answers «أَيْنَ كُنْتَ أَمْس؟»?", "كُنْتُ فِي الْبَيْت", ["كَانَ حَارًّا", "كَانَتْ أَمْس", "كَانَ أَخِي"], "“Where” asks for a place."),
        M("Which answers «كَيْفَ كَانَتِ الْمَكْتَبَة؟»?", "كَانَتْ كَبِيرَةً", ["كَانَتْ أَمْس", "كُنْتُ فِي الْبَيْت", "كَانَ مَعِي أَخِي"], "“How” asks for a description."),
        F("___ كُنْتَ أَمْس؟", "أَيْنَ", ["مَنْ", "كَمْ", "مَاذَا"], "A place.", tr="Where were you yesterday?"),
        F("كَيْفَ ___ الْجَوّ؟", "كَانَ", ["كَانَتْ", "كُنْتُ", "كُنْتِ"], "الْجَوّ is masculine.", tr="How was the weather?"),
    ],
    verify=vw("كُنْتَ", "كُنْتِ", "كُنْتُ", "كَانَ", "كَانَتْ", "كَانَتِ", "مَعَكَ", "مَعِي", "حَارًّا", "الْحَفْلَة", "هُنَاك", "الْمَكْتَبَة"),
)

# ---------------------------------------------------------------------------- 112
L112 = lesson(
    "Used to: كُنْتُ أَلْعَب",
    "كَانَ + a present verb",
    requires=["كان", "لعب", "كل", "يوم", "صغير", "رياضة"],
    cards=[
        card("كَانَ + present verb",
             "Put كَانَ in front of a present verb and the meaning becomes “used to” (or “was …ing”). Both words show "
             "the person: كُنْتُ for “I” and أَلْعَب for “I”. Nothing is dropped from the verb.",
             tables=[table(["Pronoun", "Arabic", "English"],
                           [["أَنَا", "كُنْتُ أَلْعَب", "I used to play"], ["أَنْتَ", "كُنْتَ تَلْعَب", "you (man) used to play"],
                            ["أَنْتِ", "كُنْتِ تَلْعَبِين", "you (woman) used to play"], ["هُوَ", "كَانَ يَلْعَب", "he used to play"],
                            ["هِيَ", "كَانَتْ تَلْعَب", "she used to play"], ["نَحْنُ", "كُنَّا نَلْعَب", "we used to play"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Habits in the past",
             "This is the way to describe what you used to do every day, every summer, or when you were young.",
             examples=[
                 ex("كُنْتُ أَلْعَب كُرَة الْقَدَم كُلّ يَوْم.", "I used to play football every day.", "كُنْتُ أَلْعَب"),
                 ex("كَانَ أَخِي يَسْبَح فِي الْبَحْر.", "My brother used to swim in the sea.", "كَانَ"),
                 ex("كَانَتْ أُمِّي تَطْبُخ الْعَشَاء.", "My mother used to cook dinner.", "كَانَتْ"),
                 ex("هَلْ كُنْتَ تَقْرَأ كَثِيرًا؟", "Did you use to read a lot? (to a man)", "كُنْتَ تَقْرَأ"),
                 ex("كُنْتِ تَذْهَبِين إِلَى الْمَدْرَسَة.", "You used to go to school. (to a woman)", "كُنْتِ تَذْهَبِين"),
                 ex("كُنَّا نَسْكُن فِي بَيْت صَغِير.", "We used to live in a small house.", "كُنَّا نَسْكُن"),
             ]),
    ],
    exercises=[
        M("Which means “I used to play”?", "كُنْتُ أَلْعَب", ["كَانَ يَلْعَب", "كُنَّا نَلْعَب", "كُنْتُ تَلْعَب"], "كُنْتُ + أَلْعَب."),
        M("Which means “he used to swim”?", "كَانَ يَسْبَح", ["كَانَتْ تَسْبَح", "كُنْتُ أَسْبَح", "كَانَ تَسْبَح"], "كَانَ + يَسْبَح."),
        M("Which means “she used to cook”?", "كَانَتْ تَطْبُخ", ["كَانَ تَطْبُخ", "كَانَتْ يَطْبُخ", "كَانَ يَطْبُخ"], "كَانَتْ + تَطْبُخ."),
        M("Which means “we used to live”?", "كُنَّا نَسْكُن", ["كُنْتُ أَسْكُن", "كَانُوا يَسْكُنُون", "كُنَّا أَسْكُن"], "كُنَّا + نَسْكُن."),
        M("Which asks a man “Did you use to read?”", "هَلْ كُنْتَ تَقْرَأ؟", ["هَلْ كُنْتِ تَقْرَئِين؟", "هَلْ كُنْتُ أَقْرَأ؟", "هَلْ كَانَ يَقْرَأ؟"], "كُنْتَ تَقْرَأ for a man."),
        M("A woman says “I used to go to school”. Which is right?", "كُنْتُ أَذْهَب إِلَى الْمَدْرَسَة", ["كُنْتِ تَذْهَبِين إِلَى الْمَدْرَسَة", "كَانَتْ تَذْهَب إِلَى الْمَدْرَسَة", "كُنَّا نَذْهَب إِلَى الْمَدْرَسَة"], "“I” is the same for men and women."),
        F("كُنْتُ ___ كُرَة الْقَدَم.", "أَلْعَب", ["تَلْعَب", "يَلْعَب", "نَلْعَب"], "The verb must also show “I”.", tr="I used to play football."),
        F("___ أُمِّي تَطْبُخ.", "كَانَتْ", ["كَانَ", "كُنْتُ", "كُنَّا"], "My mother = she.", tr="My mother used to cook."),
        F("كُنَّا ___ فِي بَيْت صَغِير.", "نَسْكُن", ["أَسْكُن", "يَسْكُن", "تَسْكُن"], "“We” needs نَـ.", tr="We used to live in a small house."),
    ],
    verify=(vv("لعب", "pres", ana="أَلْعَب", anta="تَلْعَب", anti="تَلْعَبِين", huwa="يَلْعَب", hiya="تَلْعَب", nahnu="نَلْعَب")
            + vv("سبح", "pres", huwa="يَسْبَح") + vv("طبخ", "pres", hiya="تَطْبُخ") + vv("سكن", "pres", nahnu="نَسْكُن")
            + vv("قرأ", "pres", anta="تَقْرَأ") + vv("ذهب", "pres", anti="تَذْهَبِين", ana="أَذْهَب")
            + vw("كَثِيرًا", "الْعَشَاء")),
)

# ---------------------------------------------------------------------------- 113
L113 = lesson(
    "Used to: they, you all, and how often",
    "كَانُوا يَلْعَبُون · دَائِمًا · أَحْيَانًا",
    requires=["كان", "لعب", "كل", "مرة", "يوم", "صديق"],
    cards=[
        card("Plural “used to”",
             "Both words take the ending of the person. The present verb keeps its full ending (ـُون, ـَان, ـْنَ). "
             "The ن is not dropped here, because there is no أَنْ in front of it.",
             tables=[table(["Pronoun", "Arabic", "English"],
                           [["هُمْ", "كَانُوا يَلْعَبُون", "they (men) used to play"], ["هُمَا", "كَانَا يَلْعَبَان", "the two of them (men) used to play"],
                            ["هُمَا", "كَانَتَا تَلْعَبَان", "the two of them (women) used to play"], ["هُنَّ", "كُنَّ يَلْعَبْنَ", "they (women) used to play"],
                            ["أَنْتُمْ", "كُنْتُمْ تَلْعَبُون", "you (men) used to play"], ["أَنْتُنَّ", "كُنْتُنَّ تَلْعَبْنَ", "you (women) used to play"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("How often?",
             "These words say how often a habit happened. They usually sit right after كَانَ or at the end of the "
             "sentence.",
             tables=[table(["Arabic", "English"],
                           [["دَائِمًا", "always"], ["غَالِبًا", "often"], ["عَادَةً", "usually"], ["أَحْيَانًا", "sometimes"],
                            ["كُلّ يَوْم", "every day"], ["كُلّ صَيْف", "every summer"]],
                           say=[0], tlit=[0], gloss=False)],
             examples=[
                 ex("كَانُوا يَلْعَبُون فِي الْحَدِيقَة كُلّ يَوْم.", "They used to play in the park every day.", "كَانُوا يَلْعَبُون"),
                 ex("كُنَّا نَذْهَب إِلَى الشَّاطِئ كُلّ صَيْف.", "We used to go to the beach every summer.", "كُنَّا نَذْهَب"),
                 ex("كُنْتُ دَائِمًا أَسْمَع الْمُوسِيقَى.", "I always used to listen to music.", "دَائِمًا"),
                 ex("كَانَتْ أُخْتِي أَحْيَانًا تَلْعَب مَعَنَا.", "My sister sometimes used to play with us.", "أَحْيَانًا"),
                 ex("كُنَّ يَدْرُسْنَ فِي الْمَكْتَبَة كُلّ يَوْم.", "They (women) used to study in the library every day.", "كُنَّ يَدْرُسْنَ"),
             ]),
    ],
    exercises=[
        M("Which means “they (men) used to play”?", "كَانُوا يَلْعَبُون", ["كُنَّ يَلْعَبْنَ", "كُنْتُمْ تَلْعَبُون", "كَانَ يَلْعَب"], "ـُوا and ـُون for a group of men."),
        M("Which means “they (women) used to play”?", "كُنَّ يَلْعَبْنَ", ["كَانُوا يَلْعَبُون", "كَانَتَا تَلْعَبَان", "كُنْتُنَّ تَلْعَبْنَ"], "كُنَّ and ـْنَ for women."),
        M("Which means “the two girls used to play”?", "كَانَتَا تَلْعَبَان", ["كَانَا يَلْعَبَان", "كَانَتْ تَلْعَب", "كُنَّ يَلْعَبْنَ"], "A dual feminine: كَانَتَا and تَلْعَبَان."),
        M("Which means “you (men) used to play”?", "كُنْتُمْ تَلْعَبُون", ["كُنْتُنَّ تَلْعَبْنَ", "كَانُوا يَلْعَبُون", "كُنَّا نَلْعَب"], "كُنْتُمْ + تَلْعَبُون."),
        M("What does دَائِمًا mean?", "always", ["sometimes", "never", "once"], "دَائِمًا = always."),
        M("What does أَحْيَانًا mean?", "sometimes", ["always", "usually", "yesterday"], "أَحْيَانًا = sometimes."),
        M("Which means “We used to go to the beach every summer”?", "كُنَّا نَذْهَب إِلَى الشَّاطِئ كُلّ صَيْف", ["كُنْتُ أَذْهَب إِلَى الشَّاطِئ كُلّ صَيْف", "كُنَّا نَذْهَب مِنَ الشَّاطِئ كُلّ صَيْف", "كَانُوا يَذْهَبُون إِلَى الشَّاطِئ كُلّ صَيْف"], "كُنَّا نَذْهَب إِلَى."),
        F("كُنَّ ___ فِي الْمَكْتَبَة.", "يَدْرُسْنَ", ["يَدْرُسُون", "يَدْرُسَان", "تَدْرُس"], "Women: ـْنَ.", tr="They (women) used to study in the library."),
        F("كَانُوا ___ كُلّ يَوْم.", "يَلْعَبُون", ["يَلْعَبْنَ", "يَلْعَب", "نَلْعَب"], "Men: ـُون.", tr="They used to play every day."),
    ],
    verify=(vv("لعب", "pres", hum="يَلْعَبُون", huma_m="يَلْعَبَان", huma_f="تَلْعَبَان", hunna="يَلْعَبْنَ", antum="تَلْعَبُون", antunna="تَلْعَبْنَ")
            + vv("درس", "pres", hunna="يَدْرُسْنَ") + vv("ذهب", "pres", nahnu="نَذْهَب") + vv("سمع", "pres", ana="أَسْمَع")
            + vw("دَائِمًا", "غَالِبًا", "عَادَةً", "أَحْيَانًا", "مَعَنَا", "الشَّاطِئ")),
)

# ---------------------------------------------------------------------------- 114
L114 = lesson(
    "When I was little",
    "عِنْدَمَا كُنْتُ صَغِيرًا · فِي طُفُولَتِي",
    requires=["صغير", "طفل", "مدرسة", "صديق", "قبل", "بعد"],
    cards=[
        card("Time words for the past",
             "Use عِنْدَمَا (“when”) with a past clause, and بَعْد and قَبْل for “after” and “before”. To say “… ago”, "
             "put قَبْل in front of the length of time.",
             tables=[table(["Arabic", "English"],
                           [["عِنْدَمَا كُنْتُ صَغِيرًا", "when I was little"], ["فِي طُفُولَتِي", "in my childhood"],
                            ["بَعْد الْمَدْرَسَة", "after school"], ["قَبْل الْمَدْرَسَة", "before school"],
                            ["قَبْل سَنَة", "a year ago"], ["قَبْل سَنَتَيْن", "two years ago"],
                            ["قَبْل خَمْس سَنَوَات", "five years ago"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("A childhood",
             "A few sentences are enough to tell a story: put the time first, then the habit.",
             examples=[
                 ex("عِنْدَمَا كُنْتُ صَغِيرًا، كُنْتُ أَسْكُن فِي قَرْيَة.", "When I was little, I used to live in a village.", "عِنْدَمَا"),
                 ex("كُنْتُ أَلْعَب مَعَ أَصْدِقَائِي فِي الشَّارِع.", "I used to play with my friends in the street.", "كُنْتُ أَلْعَب"),
                 ex("كَانَتْ جَدَّتِي تَطْبُخ لَنَا كُلّ يَوْم.", "My grandmother used to cook for us every day.", "كَانَتْ جَدَّتِي"),
                 ex("بَعْد الْمَدْرَسَة كُنَّا نَذْهَب إِلَى النَّهْر.", "After school we used to go to the river.", "بَعْد"),
                 ex("فِي طُفُولَتِي كُنْتُ أُحِبّ السِّبَاحَة.", "In my childhood I used to like swimming.", "فِي طُفُولَتِي"),
             ]),
    ],
    exercises=[
        M("Which means “When I was little”?", "عِنْدَمَا كُنْتُ صَغِيرًا", ["عِنْدَمَا كَانَ صَغِيرًا", "عِنْدَمَا كُنَّا صَغِيرًا", "عِنْدَمَا كُنْتَ صَغِيرًا"], "كُنْتُ = I was."),
        M("Which means “after school”?", "بَعْد الْمَدْرَسَة", ["قَبْل الْمَدْرَسَة", "فِي الْمَدْرَسَة", "مِنَ الْمَدْرَسَة"], "بَعْد = after."),
        M("What does قَبْل سَنَتَيْن mean?", "two years ago", ["in two years", "after two years", "two years old"], "قَبْل + a length of time = ago."),
        M("What does طُفُولَة mean?", "childhood", ["school", "village", "family"], "فِي طُفُولَتِي = in my childhood."),
        M("Which means “my grandmother used to cook for us”?", "كَانَتْ جَدَّتِي تَطْبُخ لَنَا", ["كَانَ جَدِّي يَطْبُخ لَنَا", "كَانَتْ جَدَّتِي تَطْبُخ لِي", "كُنْتُ أَطْبُخ لَنَا"], "جَدَّة = grandmother; لَنَا = for us."),
        M("Which means “In my childhood I used to like swimming”?", "فِي طُفُولَتِي كُنْتُ أُحِبّ السِّبَاحَة", ["فِي طُفُولَتِي كَانَ يُحِبّ السِّبَاحَة", "فِي مَدْرَسَتِي كُنْتُ أُحِبّ السِّبَاحَة", "فِي طُفُولَتِي كُنْتُ أَسْبَح"], "أُحِبّ = I like."),
        F("___ كُنْتُ صَغِيرًا، كُنْتُ أَلْعَب فِي الْحَدِيقَة.", "عِنْدَمَا", ["هَلْ", "مَاذَا", "لَكِنْ"], "“When”.", tr="When I was little, I used to play in the garden."),
        F("كُنَّا ___ إِلَى النَّهْر بَعْد الْمَدْرَسَة.", "نَذْهَب", ["أَذْهَب", "يَذْهَبُون", "تَذْهَب"], "“We”.", tr="We used to go to the river after school."),
        F("كُنْتُ أَسْكُن فِي قَرْيَة ___.", "صَغِيرَة", ["صَغِير", "صَغِيرُون", "صَغِيرَتَان"], "قَرْيَة is feminine singular.", tr="I used to live in a small village."),
    ],
    verify=(vv("سكن", "pres", ana="أَسْكُن") + vv("لعب", "pres", ana="أَلْعَب") + vv("طبخ", "pres", hiya="تَطْبُخ")
            + vv("ذهب", "pres", nahnu="نَذْهَب") + vpb("صَدِيق", "أَصْدِقَاء")
            + vw("عِنْدَمَا", "طُفُولَتِي", "جَدَّتِي", "السِّبَاحَة", "قَرْيَة", "النَّهْر", "الشَّارِع")),
)

# ---------------------------------------------------------------------------- 115
L115 = lesson(
    "I used to have: كَانَ عِنْدِي",
    "كَانَ عِنْدِي كَلْب · كَانَ هُنَاك مَطْعَم",
    requires=["كان", "عند", "كلب", "بيت", "سيارة", "مطعم"],
    cards=[
        card("I had",
             "To say “I had”, put كَانَ in front of عِنْدِي (or مَعِي). كَانَ agrees with the thing that was had, "
             "because that is the subject: كَانَ for a masculine thing and كَانَتْ for a feminine one.",
             tables=[table(["Now", "Past"],
                           [["عِنْدِي كَلْب", "كَانَ عِنْدِي كَلْب"], ["عِنْدِي سَيَّارَة", "كَانَتْ عِنْدِي سَيَّارَة"],
                            ["عِنْدَنَا بَيْت كَبِير", "كَانَ عِنْدَنَا بَيْت كَبِير"], ["مَعِي هَاتِف", "كَانَ مَعِي هَاتِف"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("There was, there were",
             "كَانَ هُنَاك (or كَانَ فِي … ) means “there was”. The thing that existed comes after it.",
             examples=[
                 ex("كَانَ عِنْدِي كَلْب صَغِير.", "I used to have a small dog.", "كَانَ عِنْدِي"),
                 ex("كَانَتْ عِنْدَنَا دَرَّاجَة قَدِيمَة.", "We had an old bicycle.", "كَانَتْ عِنْدَنَا"),
                 ex("هَلْ كَانَ عِنْدَكَ كَلْب؟", "Did you have a dog? (to a man)", "كَانَ عِنْدَكَ"),
                 ex("كَانَ فِي مَدِينَتِي مَسْرَح كَبِير.", "There was a big theatre in my city.", "كَانَ فِي"),
                 ex("كَانَ هُنَاك مَطْعَم قَدِيم قَرِيب مِنَ الْبَيْت.", "There was an old restaurant close to the house.", "كَانَ هُنَاك"),
                 ex("كَانَتْ هُنَاك حَدِيقَة جَمِيلَة.", "There was a beautiful garden.", "كَانَتْ هُنَاك"),
             ]),
    ],
    exercises=[
        M("Which means “I used to have a dog”?", "كَانَ عِنْدِي كَلْب", ["عِنْدِي كَلْب", "كُنْتُ عِنْدِي كَلْب", "كَانَتْ عِنْدَكَ كَلْب"], "كَانَ + عِنْدِي + noun."),
        M("Which means “I had an old bicycle”?", "كَانَتْ عِنْدِي دَرَّاجَة قَدِيمَة", ["عِنْدِي دَرَّاجَة قَدِيمَة", "كَانَتْ عِنْدَنَا دَرَّاجَتَان قَدِيمَتَان", "كَانَ عِنْدَكَ دَرَّاجَة قَدِيمَة"], "دَرَّاجَة is feminine."),
        M("Which asks a man “Did you have a dog?”", "هَلْ كَانَ عِنْدَكَ كَلْب؟", ["هَلْ كَانَ عِنْدَكِ كَلْب؟", "هَلْ كَانَ عِنْدِي كَلْب؟", "هَلْ كَانَ عِنْدَهُ كَلْب؟"], "عِنْدَكَ = you have (man)."),
        M("Which means “There was a big theatre in my city”?", "كَانَ فِي مَدِينَتِي مَسْرَح كَبِير", ["فِي مَدِينَتِي مَسْرَح كَبِير", "كَانَتْ فِي مَدِينَتِي مَسْرَح كَبِير", "كَانَ مَسْرَح كَبِير هُنَاك أَمْس"], "كَانَ فِي … = there was in …"),
        M("Which means “There was a restaurant”?", "كَانَ هُنَاك مَطْعَم", ["كُنْتُ هُنَاك مَطْعَم", "لَيْسَ هُنَاك مَطْعَم", "هَلْ كَانَ مَطْعَم"], "كَانَ هُنَاك."),
        M("Which means “I had a phone with me”?", "كَانَ مَعِي هَاتِف", ["مَعِي هَاتِف", "كَانَ مَعَكَ هَاتِف", "كُنْتُ مَعِي هَاتِف"], "مَعِي = with me."),
        F("___ عِنْدِي كَلْب صَغِير.", "كَانَ", ["كَانَتْ", "كُنْتُ", "كُنَّا"], "كَلْب is masculine.", tr="I used to have a small dog."),
        F("كَانَ ___ كَلْب. (We used to have a dog.)", "عِنْدَنَا", ["عِنْدِي", "عِنْدَكَ", "عِنْدَهُ"], "نَا = we / us.", tr="We used to have a dog."),
        F("كَانَ ___ مَطْعَم قَدِيم.", "هُنَاك", ["هَلْ", "مَاذَا", "لَكِنْ"], "هُنَاك = there.", tr="There was an old restaurant."),
    ],
    verify=vw("عِنْدِي", "عِنْدَنَا", "عِنْدَكَ", "عِنْدَهُ", "مَعِي", "مَعَكَ", "كَلْب", "دَرَّاجَة", "مَسْرَح", "هُنَاك", "مَدِينَتِي", "قَدِيمَة"),
)

# ---------------------------------------------------------------------------- 116
L116 = lesson(
    "I used to work at…",
    "كُنْتُ أَعْمَل فِي شَرِكَة · كَانَ أَبِي مُدِيرًا",
    requires=["عمل", "شركة", "مهندس", "طبيب", "مدير", "موظف", "مكتب"],
    cards=[
        card("More jobs",
             "These are all regular words: add ة for a woman. You have met others in the first units.",
             tables=[table(["English", "Man", "Woman"],
                           [["employee", "مُوَظَّف", "مُوَظَّفَة"], ["manager", "مُدِير", "مُدِيرَة"],
                            ["nurse", "مُمَرِّض", "مُمَرِّضَة"], ["salesperson", "بَائِع", "بَائِعَة"],
                            ["driver", "سَائِق", "سَائِقَة"], ["journalist", "صَحَفِيّ", "صَحَفِيَّة"],
                            ["designer", "مُصَمِّم", "مُصَمِّمَة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("What I used to do",
             "Use كَانَ + عَمِلَ in the present form for “used to work”, with فِي for the place and لِمُدَّة for how "
             "long. Or use كَانَ with the job itself: كَانَ أَبِي مُدِيرًا.",
             examples=[
                 ex("كُنْتُ أَعْمَل فِي شَرِكَة كَبِيرَة.", "I used to work at a big company.", "كُنْتُ أَعْمَل"),
                 ex("كُنْتُ أَعْمَل مُهَنْدِسًا لِمُدَّة ثَلَاث سَنَوَات.", "I worked as an engineer for three years.", "مُهَنْدِسًا"),
                 ex("كَانَتْ أُخْتِي مُمَرِّضَةً فِي مُسْتَشْفَى.", "My sister was a nurse in a hospital.", "مُمَرِّضَةً"),
                 ex("كَانَ أَبِي مُدِيرًا.", "My father was a manager.", "مُدِيرًا"),
                 ex("أَيْنَ كُنْتَ تَعْمَل؟", "Where did you use to work? (to a man)", "كُنْتَ تَعْمَل"),
                 ex("كُنْتُ أَعْمَل فِي مَكْتَب قَرِيب مِنَ الْبَيْت.", "I used to work in an office near home.", "مَكْتَب"),
             ]),
    ],
    exercises=[
        M("What does مُوَظَّف mean?", "employee", ["manager", "nurse", "driver"], "مُوَظَّف = employee."),
        M("What does مُدِير mean?", "manager", ["employee", "doctor", "teacher"], "مُدِير = manager."),
        M("Which means “I used to work at a company”?", "كُنْتُ أَعْمَل فِي شَرِكَة", ["كُنْتُ أَدْرُس فِي شَرِكَة", "كُنْتُ أَعْمَل مِنْ شَرِكَة", "كُنَّا أَعْمَل فِي شَرِكَة"], "عَمِلَ = to work."),
        M("Which means “My sister was a nurse”?", "كَانَتْ أُخْتِي مُمَرِّضَةً", ["كَانَ أُخْتِي مُمَرِّضَةً", "كَانَتْ أُخْتِي مُمَرِّضًا", "كَانَتْ أُخْتِي مُمَرِّضُون"], "كَانَتْ and ـَةً for a woman."),
        M("Which means “My father was a manager”?", "كَانَ أَبِي مُدِيرًا", ["كَانَتْ أَبِي مُدِيرًا", "كَانَ أَبِي مُدِيرَةً", "كُنْتُ أَبِي مُدِيرًا"], "كَانَ and ـًا for a man."),
        M("Which asks a man “Where did you use to work?”", "أَيْنَ كُنْتَ تَعْمَل؟", ["أَيْنَ كُنْتِ تَعْمَلِين؟", "أَيْنَ كُنْتُ أَعْمَل؟", "مَتَى كُنْتَ تَعْمَل؟"], "كُنْتَ تَعْمَل."),
        M("Which means “for three years”?", "لِمُدَّة ثَلَاث سَنَوَات", ["لِمُدَّة ثَلَاثَة سَنَوَات", "فِي ثَلَاث سَنَوَات", "قَبْل ثَلَاث سَنَوَات"], "لِمُدَّة = for a period of."),
        F("كُنْتُ أَعْمَل ___ شَرِكَة كَبِيرَة.", "فِي", ["مِنْ", "إِلَى", "عَنْ"], "At a company = فِي.", tr="I used to work at a big company."),
        F("كَانَ أَبِي ___.", "مُدِيرًا", ["مُدِيرَةً", "مُدِيرُون", "مُدِيرَات"], "A man, singular.", tr="My father was a manager."),
        F("كَانَتْ أُخْتِي ___.", "مُمَرِّضَةً", ["مُمَرِّضًا", "مُمَرِّضُون", "مُمَرِّضَان"], "A woman, singular.", tr="My sister was a nurse."),
    ],
    verify=(vv("عمل", "pres", ana="أَعْمَل", anta="تَعْمَل", anti="تَعْمَلِين")
            + vf("مُوَظَّف", "مُوَظَّفَة") + vf("مُدِير", "مُدِيرَة") + vf("مُمَرِّض", "مُمَرِّضَة") + vf("بَائِع", "بَائِعَة")
            + vf("سَائِق", "سَائِقَة") + vf("صَحَفِيّ", "صَحَفِيَّة") + vf("مُصَمِّم", "مُصَمِّمَة")
            + vw("شَرِكَة", "مُسْتَشْفَى", "لِمُدَّة", "مَكْتَب", "مُدِيرًا", "مُمَرِّضَةً", "مُهَنْدِسًا")),
)

# ---------------------------------------------------------------------------- 117
L117 = lesson(
    "Job ads",
    "مَطْلُوب مُوَظَّف · خِبْرَة · رَاتِب",
    requires=["وظيفة", "عمل", "شركة", "مكتب", "بريد", "خبرة"],
    cards=[
        card("Words in a job ad",
             "Job ads are short. مَطْلُوب means “wanted”, and the ad lists what the job needs.",
             tables=[table(["Arabic", "English"],
                           [["مَطْلُوب", "wanted"], ["وَظِيفَة", "job, post"], ["عَمَل", "work, a job"], ["خِبْرَة", "experience"],
                            ["رَاتِب", "salary"], ["إِعْلَان", "advertisement"], ["الْبَرِيد الْإِلِكْتْرُونِيّ", "email"]],
                           say=[0], tlit=[0], gloss=False)]),
        card("An ad and a reply",
             "Read the ad first. Then see how a person who used to work somewhere answers it.",
             examples=[
                 ex("مَطْلُوب مُوَظَّف فِي شَرِكَة كَبِيرَة.", "Wanted: an employee at a big company.", "مَطْلُوب"),
                 ex("يَجِب أَنْ تَكُون عِنْدَهُ خِبْرَة سَنَتَيْن.", "He must have two years of experience.", "خِبْرَة"),
                 ex("الرَّاتِب جَيِّد.", "The salary is good.", "الرَّاتِب"),
                 ex("اُكْتُبْ إِلَيْنَا بِالْبَرِيد الْإِلِكْتْرُونِيّ.", "Write to us by email. (to a man)", "بِالْبَرِيد الْإِلِكْتْرُونِيّ"),
                 ex("أَنَا أَبْحَث عَنْ عَمَل.", "I am looking for a job.", "أَبْحَث عَنْ"),
                 ex("كُنْتُ أَعْمَل فِي شَرِكَة لِمُدَّة سَنَتَيْن.", "I worked at a company for two years.", "كُنْتُ أَعْمَل"),
                 ex("عِنْدِي خِبْرَة جَيِّدَة.", "I have good experience.", "خِبْرَة"),
             ]),
    ],
    exercises=[
        M("What does مَطْلُوب mean in an ad?", "wanted", ["sold", "closed", "free"], "مَطْلُوب = wanted."),
        M("What does خِبْرَة mean?", "experience", ["salary", "email", "office"], "خِبْرَة = experience."),
        M("What does رَاتِب mean?", "salary", ["experience", "advertisement", "job"], "رَاتِب = salary."),
        M("Which means “I am looking for a job”?", "أَنَا أَبْحَث عَنْ عَمَل", ["أَنَا أَبْحَث فِي عَمَل", "أَنْتَ تَبْحَث عَنْ عَمَل", "كُنْتُ أَبْحَث مِنْ عَمَل"], "بَحَثَ عَنْ = to look for."),
        M("Which means “Write to us by email” (to a man)?", "اُكْتُبْ إِلَيْنَا بِالْبَرِيد الْإِلِكْتْرُونِيّ", ["اُكْتُبْ إِلَيْكَ بِالْبَرِيد الْإِلِكْتْرُونِيّ", "لَا تَكْتُبْ إِلَيْنَا بِالْبَرِيد", "كَتَبْتُ إِلَيْنَا بِالْبَرِيد"], "إِلَيْنَا = to us."),
        M("Which means “He must have two years of experience”?", "يَجِب أَنْ تَكُون عِنْدَهُ خِبْرَة سَنَتَيْن", ["يَجِب أَنْ تَكُون عِنْدِي خِبْرَة سَنَتَيْن", "كَانَ عِنْدَهُ خِبْرَة سَنَتَيْن", "يَجِب أَنْ تَكْتُب خِبْرَة سَنَتَيْن"], "تَكُون agrees with خِبْرَة (feminine): يَجِب أَنْ تَكُون عِنْدَهُ خِبْرَة."),
        F("___ مُوَظَّف فِي شَرِكَة كَبِيرَة.", "مَطْلُوب", ["مَعَ", "عِنْدَمَا", "أَمْس"], "The ad starts with “wanted”.", tr="Wanted: an employee at a big company."),
        F("أَنَا أَبْحَث ___ عَمَل.", "عَنْ", ["مِنْ", "إِلَى", "فِي"], "بَحَثَ عَنْ.", tr="I am looking for a job."),
        F("عِنْدِي ___ جَيِّدَة.", "خِبْرَة", ["رَاتِب", "بَرِيد", "إِعْلَان"], "You have experience.", tr="I have good experience."),
    ],
    verify=(vv("بحث", "pres", ana="أَبْحَث") + vv("كتب", "imp", anta="اُكْتُبْ") + vv("عمل", "pres", ana="أَعْمَل")
            + vw("مَطْلُوب", "وَظِيفَة", "خِبْرَة", "رَاتِب", "إِعْلَان", "الْبَرِيد", "الْإِلِكْتْرُونِيّ", "يَكُون", "عِنْدَهُ", "إِلَيْنَا", "سَنَتَيْن")),
)

# ---------------------------------------------------------------------------- 118
L118 = lesson(
    "Review: when I was young",
    "كَانَ · كُنْتُ أَلْعَب · كَانَ عِنْدِي",
    requires=["كان", "لعب", "طفل", "صغير", "مدرسة", "عمل"],
    cards=[
        card("Everything about كَانَ",
             "Three patterns: كَانَ + a description (was), كَانَ + a present verb (used to), and كَانَ + عِنْدِي "
             "(had). The verb shows the person in all three.",
             tables=[table(["Person", "Was", "Used to play"],
                           [["I", "كُنْتُ", "كُنْتُ أَلْعَب"], ["you (man)", "كُنْتَ", "كُنْتَ تَلْعَب"], ["you (woman)", "كُنْتِ", "كُنْتِ تَلْعَبِين"],
                            ["he", "كَانَ", "كَانَ يَلْعَب"], ["she", "كَانَتْ", "كَانَتْ تَلْعَب"], ["we", "كُنَّا", "كُنَّا نَلْعَب"],
                            ["they (men)", "كَانُوا", "كَانُوا يَلْعَبُون"], ["they (women)", "كُنَّ", "كُنَّ يَلْعَبْنَ"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("A short story",
             "Read the story of a woman who used to live in a village.",
             examples=[
                 ex("عِنْدَمَا كُنْتُ صَغِيرَةً، كُنَّا نَسْكُن فِي قَرْيَة.", "When I was little, we used to live in a village."),
                 ex("كَانَ عِنْدَنَا بَيْت قَدِيم وَحَدِيقَة كَبِيرَة.", "We had an old house and a big garden."),
                 ex("كَانَ أَبِي يَعْمَل فِي مَكْتَب فِي الْمَدِينَة.", "My father used to work in an office in the city."),
                 ex("وَكُنْتُ أَلْعَب مَعَ أُخْتِي فِي الْحَدِيقَة كُلّ يَوْم.", "And I used to play with my sister in the garden every day."),
                 ex("كَانَتِ الْحَيَاة بَسِيطَةً وَجَمِيلَةً.", "Life was simple and beautiful."),
             ]),
    ],
    exercises=[
        M("Which form means “you (woman) were”?", "كُنْتِ", ["كُنْتَ", "كُنْتُ", "كَانَتْ"], "The kasra marks a woman."),
        M("Which means “they (men) used to play”?", "كَانُوا يَلْعَبُون", ["كُنَّ يَلْعَبْنَ", "كَانَ يَلْعَب", "كُنَّا نَلْعَب"], "ـُوا and ـُون."),
        M("Which means “I used to have a dog”?", "كَانَ عِنْدِي كَلْب", ["كُنْتُ كَلْب", "عِنْدِي كَلْب", "كَانَتْ عِنْدَنَا كَلْب"], "كَانَ + عِنْدِي."),
        M("Which means “Where were you?” (to a woman)", "أَيْنَ كُنْتِ؟", ["أَيْنَ كُنْتَ؟", "أَيْنَ كَانَتْ؟", "كَيْفَ كُنْتِ؟"], "كُنْتِ = you (woman) were."),
        M("Which means “My father used to work in an office”?", "كَانَ أَبِي يَعْمَل فِي مَكْتَب", ["كَانَتْ أَبِي تَعْمَل فِي مَكْتَب", "كُنْتُ أَعْمَل فِي مَكْتَب", "كَانَ أَبِي مُدِيرًا فِي مَكْتَب"], "كَانَ + يَعْمَل."),
        M("A woman says “I was little”. Which is right?", "كُنْتُ صَغِيرَةً", ["كُنْتُ صَغِيرًا", "كُنْتِ صَغِيرَةً", "كَانَتْ صَغِيرَةً"], "Feminine description: ـَةً."),
        M("Which means “Life was beautiful”?", "كَانَتِ الْحَيَاة جَمِيلَةً", ["كَانَ الْحَيَاة جَمِيلًا", "الْحَيَاة جَمِيلَة", "كُنْتُ الْحَيَاة جَمِيلَةً"], "حَيَاة is feminine."),
        F("عِنْدَمَا ___ صَغِيرًا، كُنْتُ أَلْعَب كَثِيرًا.", "كُنْتُ", ["كُنْتِ", "كُنَّا", "كَانَتْ"], "A man speaking, “I”.", tr="When I was little, I played a lot."),
        F("كَانَتْ أُخْتِي ___ فِي الْحَدِيقَة.", "تَلْعَب", ["يَلْعَب", "أَلْعَب", "نَلْعَب"], "She = تَـ.", tr="My sister used to play in the garden."),
        F("___ عِنْدَنَا بَيْت قَدِيم.", "كَانَ", ["كُنْتُ", "كَانَتْ", "كُنَّا"], "بَيْت is masculine.", tr="We had an old house."),
    ],
    verify=(vv("لعب", "pres", anta="تَلْعَب", anti="تَلْعَبِين", huwa="يَلْعَب", hiya="تَلْعَب", nahnu="نَلْعَب", hum="يَلْعَبُون", hunna="يَلْعَبْنَ")
            + vv("سكن", "pres", nahnu="نَسْكُن") + vv("عمل", "pres", huwa="يَعْمَل")
            + vw("الْحَيَاة", "بَسِيطَةً", "جَمِيلَةً", "كَثِيرًا", "صَغِيرَةً")),
)

UNIT = unit("كَانَ: was, used to, and free time",
            [L107, L108, L109, L110, L111, L112, L113, L114, L115, L116, L117, L118])
