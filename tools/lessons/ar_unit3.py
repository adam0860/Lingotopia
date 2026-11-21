"""Unit 3: questions, directions, places, languages, the present tense, negation, weather
(textbook Chapter 2; all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 32
L32 = lesson(
    "Question words",
    "مَنْ · مَا · أَيْنَ · كَيْفَ · مَتَى · لِمَاذَا · كَمْ",
    requires=["من", "ما", "ماذا", "أين", "كيف", "متى", "لماذا", "كم"],
    cards=[
        card("The question words",
             "Arabic questions begin with the question word. Eight of them cover most of what you will ask. "
             "Two of them mean “what”: مَا goes in front of a noun or a pronoun, and مَاذَا in front of a verb.",
             tables=[table(["English", "Arabic"],
                           [["who?", "مَنْ"], ["what? (before a noun)", "مَا"], ["what? (before a verb)", "مَاذَا"],
                            ["where?", "أَيْنَ"], ["how?", "كَيْفَ"], ["when?", "مَتَى"],
                            ["why?", "لِمَاذَا"], ["how many? how much?", "كَمْ"]],
                           say=[1], tlit=[1])]),
        card("In a sentence",
             "Say the question word, then the rest of the sentence. A noun sentence needs no verb: أَيْنَ الْمَدْرَسَة؟ "
             "is just “where the school?”.",
             examples=[
                 ex("مَنْ هَذَا؟", "Who is this?"),
                 ex("مَا اِسْمُكَ؟", "What is your name?"),
                 ex("مَاذَا تَدْرُس؟", "What do you study?"),
                 ex("أَيْنَ تَسْكُن؟", "Where do you live?"),
                 ex("كَيْفَ الطَّقْس الْيَوْم؟", "How is the weather today?"),
                 ex("مَتَى تَذْهَب إِلَى الْجَامِعَة؟", "When do you go to the university?"),
                 ex("لِمَاذَا تَدْرُس الْعَرَبِيَّة؟", "Why do you study Arabic?"),
                 ex("كَمْ عُمْرُكَ؟", "How old are you? (literally: how much your age)"),
             ]),
        card("مَنْ (who) or مِنْ (from)?",
             "These two small words differ only in their vowel, so the vowel matters. مَنْ asks about a person; "
             "مِنْ means “from”.",
             examples=[ex("مَنْ أَنْتَ؟", "Who are you?", "مَنْ"),
                       ex("مِنْ أَيْنَ أَنْتَ؟", "Where are you from?", "مِنْ")]),
    ],
    exercises=[
        M("Which word means “where”?", "أَيْنَ", ["كَيْفَ", "مَتَى", "مَنْ"], "أَيْنَ = where."),
        M("Which word means “when”?", "مَتَى", ["أَيْنَ", "لِمَاذَا", "كَمْ"], "مَتَى = when."),
        M("Which word means “why”?", "لِمَاذَا", ["مَاذَا", "كَيْفَ", "مَنْ"], "لِمَاذَا = why."),
        M("Which word asks about a person?", "مَنْ", ["مِنْ", "مَا", "أَيْنَ"], "مَنْ = who. مِنْ is “from”."),
        M("Which means “Who is this?”", "مَنْ هَذَا؟", ["مِنْ هَذَا؟", "أَيْنَ هَذَا؟", "كَمْ هَذَا؟"], "مَنْ = who (with fatḥa)."),
        M("Which question asks “How old are you?”", "كَمْ عُمْرُكَ؟", ["أَيْنَ عُمْرُكَ؟", "مَتَى عُمْرُكَ؟", "مَنْ عُمْرُكَ؟"], "كَمْ = how much / how many."),
        M("Which means “Why do you study Arabic?”", "لِمَاذَا تَدْرُس الْعَرَبِيَّة؟", ["أَيْنَ تَدْرُس الْعَرَبِيَّة؟", "مَتَى تَدْرُس الْعَرَبِيَّة؟", "مَنْ تَدْرُس الْعَرَبِيَّة؟"], "لِمَاذَا = why."),
        F("___ اِسْمُكَ؟", "مَا", ["أَيْنَ", "كَمْ", "مَتَى"], "A noun sentence: مَا + noun.", tr="What is your name?"),
        F("___ تَسْكُن؟", "أَيْنَ", ["مَنْ", "كَمْ", "لِمَاذَا"], "The question is about a place.", tr="Where do you live?"),
        F("___ تَكْتُب؟", "مَاذَا", ["مَنْ", "أَيْنَ", "كَيْفَ"], "“What” before a verb: مَاذَا.", tr="What do you write?"),
    ],
    verify=(vw("مَنْ", "أَيْنَ", "كَيْفَ", "مَتَى", "لِمَاذَا", "كَمْ", "مَاذَا")
            + vv("درس", "pres", anta="تَدْرُس") + vv("سكن", "pres", anta="تَسْكُن") + vv("كتب", "pres", anta="تَكْتُب")
            + vv("ذهب", "pres", anta="تَذْهَب")),
)

# ---------------------------------------------------------------------------- 33
L33 = lesson(
    "Yes–no questions: هَلْ",
    "هَلْ أَنْتَ طَالِب؟ نَعَمْ · لَا",
    requires=["هل", "نعم", "لا", "طالب"],
    cards=[
        card("Starting a yes–no question",
             "To ask something that can be answered with yes or no, put هَلْ at the start. The rest of the "
             "sentence does not change. The answers are نَعَمْ (yes) and لَا (no).",
             examples=[
                 ex("هَلْ أَنْتَ طَالِب؟", "Are you a student?", "هَلْ"),
                 ex("نَعَمْ، أَنَا طَالِب.", "Yes, I am a student.", "نَعَمْ"),
                 ex("هَلْ هِيَ مِصْرِيَّة؟", "Is she Egyptian?", "هَلْ"),
                 ex("لَا، هِيَ سُورِيَّة.", "No, she is Syrian.", "لَا"),
             ]),
        card("Questions with a verb",
             "A verb question works the same way. In your answer the verb changes to fit the speaker: if you are "
             "asked تَسْكُن (you live), you answer أَسْكُن (I live).",
             examples=[
                 ex("هَلْ تَسْكُن فِي الْقَاهِرَة؟", "Do you live in Cairo?"),
                 ex("نَعَمْ، أَسْكُن فِي الْقَاهِرَة.", "Yes, I live in Cairo.", "أَسْكُن"),
                 ex("هَلْ تَدْرُس فِي الْجَامِعَة؟", "Do you study at the university?"),
                 ex("لَا، أَعْمَل فِي الْمَكْتَب.", "No, I work in the office.", "أَعْمَل"),
             ]),
    ],
    exercises=[
        M("Which word begins a yes–no question?", "هَلْ", ["مَنْ", "أَيْنَ", "لِمَاذَا"], "هَلْ turns a statement into a yes–no question."),
        M("Which word means “yes”?", "نَعَمْ", ["لَا", "هَلْ", "مَعَ"], "نَعَمْ = yes."),
        M("Which word means “no”?", "لَا", ["نَعَمْ", "هَلْ", "مَنْ"], "لَا = no."),
        M("Which means “Are you a student?” (to a man)", "هَلْ أَنْتَ طَالِب؟", ["هَلْ أَنْتِ طَالِب؟", "هَلْ هُوَ طَالِب؟", "مَنْ أَنْتَ طَالِب؟"], "هَلْ + أَنْتَ (masculine “you”)."),
        M("Someone asks هَلْ هِيَ مِصْرِيَّة؟ and she is Syrian. The answer is…", "لَا، هِيَ سُورِيَّة", ["نَعَمْ، هِيَ سُورِيَّة", "لَا، هُوَ سُورِيّ", "نَعَمْ، هِيَ مِصْرِيَّة"], "No, and then the correct fact."),
        M("You are asked هَلْ تَسْكُن فِي الْقَاهِرَة؟ and you live there. You say…", "نَعَمْ، أَسْكُن فِي الْقَاهِرَة", ["نَعَمْ، تَسْكُن فِي الْقَاهِرَة", "نَعَمْ، يَسْكُن فِي الْقَاهِرَة", "لَا، أَسْكُن فِي الْقَاهِرَة"], "The question’s تَـ (you) becomes أَـ (I) in your answer."),
        M("In an answer, the verb prefix تَـ of the question becomes…", "أَـ", ["نَـ", "يَـ", "تَـ"], "You answer in the first person: أَـ."),
        F("___ أَنْتِ مُدَرِّسَة؟", "هَلْ", ["أَيْنَ", "مَتَى", "كَمْ"], "A yes–no question.", tr="Are you a teacher? (to a woman)"),
        F("هَلْ تَدْرُس الْيَوْم؟ نَعَمْ، ___ الْيَوْم.", "أَدْرُس", ["تَدْرُس", "يَدْرُس", "نَدْرُس"], "You answer for yourself: أَـ.", tr="Do you study today? Yes, I study today.", lemma="درس:pres:ana"),
    ],
    verify=(vw("هَلْ", "نَعَمْ") + vv("سكن", "pres", anta="تَسْكُن", ana="أَسْكُن") + vv("درس", "pres", anta="تَدْرُس", ana="أَدْرُس")
            + vv("عمل", "pres", ana="أَعْمَل")),
)

# ---------------------------------------------------------------------------- 34
L34 = lesson(
    "North, south, east, west",
    "الشَّمَال · الْجَنُوب · الشَّرْق · الْغَرْب",
    requires=["شمال", "جنوب", "غرب", "يمين", "يسار"],
    cards=[
        card("The compass",
             "The four directions are masculine nouns. Place names after them are joined directly, as in جَنُوب مِصْر: the "
             "first noun has no ال, and the second names the place. With فِي the meaning changes from “south of” "
             "to “in the south of”.",
             tables=[table(["English", "Arabic"],
                           [["north", "الشَّمَال"], ["south", "الْجَنُوب"], ["east", "الشَّرْق"], ["west", "الْغَرْب"],
                            ["the middle", "الْوَسَط"], ["the Middle East", "الشَّرْق الْأَوْسَط"]],
                           say=[1], tlit=[1])],
             examples=[
                 ex("مِصْر فِي شَمَال أَفْرِيقِيَا.", "Egypt is in the north of Africa.", "شَمَال"),
                 ex("السُّودَان جَنُوب مِصْر.", "Sudan is south of Egypt.", "جَنُوب"),
                 ex("لُبْنَان غَرْب سُورِيَا.", "Lebanon is west of Syria.", "غَرْب"),
                 ex("الْعِرَاق شَرْق سُورِيَا.", "Iraq is east of Syria.", "شَرْق"),
             ]),
        card("Left and right",
             "عَلَى الْيَمِين is “on the right” and عَلَى الْيَسَار is “on the left”. Read the building names aloud; "
             "you will meet them again soon.",
             tables=[table(["English", "Arabic"],
                           [["the right", "الْيَمِين"], ["the left", "الْيَسَار"], ["on the right", "عَلَى الْيَمِين"],
                            ["on the left", "عَلَى الْيَسَار"]],
                           say=[1], tlit=[1])],
             examples=[
                 ex("الْمَدْرَسَة عَلَى الْيَمِين.", "The school is on the right.", "عَلَى الْيَمِين"),
                 ex("الْبَنْك عَلَى الْيَسَار.", "The bank is on the left.", "عَلَى الْيَسَار"),
             ]),
    ],
    exercises=[
        M("Which word means “north”?", "الشَّمَال", ["الْجَنُوب", "الشَّرْق", "الْغَرْب"], "الشَّمَال = north."),
        M("Which word means “south”?", "الْجَنُوب", ["الشَّمَال", "الشَّرْق", "الْوَسَط"], "الْجَنُوب = south."),
        M("Which word means “west”?", "الْغَرْب", ["الشَّرْق", "الشَّمَال", "الْيَمِين"], "الْغَرْب = west."),
        M("Which word means “east”?", "الشَّرْق", ["الْغَرْب", "الْجَنُوب", "الْيَسَار"], "الشَّرْق = east."),
        M("Which means “on the left”?", "عَلَى الْيَسَار", ["عَلَى الْيَمِين", "عَلَى الْجَنُوب", "فِي الْوَسَط"], "الْيَسَار = the left."),
        M("Which means “on the right”?", "عَلَى الْيَمِين", ["عَلَى الْيَسَار", "عَلَى الْجَنُوب", "فِي الْغَرْب"], "الْيَمِين = the right."),
        M("The opposite of الشَّمَال is…", "الْجَنُوب", ["الْغَرْب", "الْيَمِين", "الْوَسَط"], "North and south are opposites."),
        F("السُّودَان ___ مِصْر.", "جَنُوب", ["شَمَال", "غَرْب", "يَمِين"], "Sudan lies south of Egypt.", tr="Sudan is south of Egypt."),
        F("لُبْنَان ___ سُورِيَا.", "غَرْب", ["شَرْق", "جَنُوب", "يَسَار"], "Lebanon lies west of Syria.", tr="Lebanon is west of Syria."),
    ],
    verify=vw("الشَّمَال", "الْجَنُوب", "الشَّرْق", "الْغَرْب", "الْيَمِين", "الْيَسَار", "الْوَسَط", "الْأَوْسَط"),
)

# ---------------------------------------------------------------------------- 35
L35 = lesson(
    "Mountains, rivers, seas",
    "جَبَل · نَهْر · بَحْر · صَحْرَاء",
    requires=["جبل", "بحر", "نهر", "صحراء", "شاطئ", "جزيرة", "غابة"],
    cards=[
        card("Landscape words",
             "These are the nouns for the shape of the land. Several are feminine, which you can usually see "
             "from the ending ة.",
             tables=[table(["English", "Arabic"],
                           [["mountain", "جَبَل"], ["sea", "بَحْر"], ["river", "نَهْر"], ["desert", "صَحْرَاء"],
                            ["beach", "شَاطِئ"], ["island", "جَزِيرَة"], ["forest", "غَابَة"], ["lake", "بُحَيْرَة"],
                            ["valley", "وَادِي"], ["coast", "سَاحِل"]],
                           say=[1], tlit=[1])]),
        card("Names of places",
             "A name such as “the Red Sea” is a noun followed by an adjective, and both take ال. Plain sentences "
             "about the land use the nouns you have just learned.",
             examples=[
                 ex("النِّيل نَهْر طَوِيل.", "The Nile is a long river."),
                 ex("الْبَحْر الْأَحْمَر بَيْنَ مِصْر وَالسُّعُودِيَّة.", "The Red Sea is between Egypt and Saudi Arabia."),
                 ex("الْبَحْرَيْن جَزِيرَة فِي الْخَلِيج.", "Bahrain is an island (really a group of islands) in the Gulf."),
                 ex("فِي مِصْر صَحْرَاء كَبِيرَة.", "There is a big desert in Egypt."),
                 ex("فِي لُبْنَان جِبَال وَبَحْر.", "In Lebanon there are mountains and a sea."),
             ]),
    ],
    exercises=[
        M("Which word means “mountain”?", "جَبَل", ["بَحْر", "نَهْر", "غَابَة"], "جَبَل = mountain."),
        M("Which word means “sea”?", "بَحْر", ["نَهْر", "جَبَل", "شَاطِئ"], "بَحْر = sea."),
        M("Which word means “river”?", "نَهْر", ["بَحْر", "جَزِيرَة", "وَادِي"], "نَهْر = river."),
        M("Which word means “desert”?", "صَحْرَاء", ["غَابَة", "جَبَل", "سَاحِل"], "صَحْرَاء = desert."),
        M("Which word means “island”?", "جَزِيرَة", ["شَاطِئ", "بُحَيْرَة", "غَابَة"], "جَزِيرَة = island."),
        M("Which word means “forest”?", "غَابَة", ["صَحْرَاء", "جَزِيرَة", "نَهْر"], "غَابَة = forest."),
        M("Which means “the Red Sea”?", "الْبَحْر الْأَحْمَر", ["بَحْر أَحْمَر", "الْأَحْمَر الْبَحْر", "النَّهْر الْأَحْمَر"], "Noun + adjective, both with ال."),
        M("Which means “The Nile is a long river”?", "النِّيل نَهْر طَوِيل", ["النِّيل بَحْر طَوِيل", "النِّيل نَهْر قَصِير", "النَّهْر نِيل طَوِيل"], "النِّيل is the Nile; نَهْر is river."),
        F("الْبَحْرَيْن ___ فِي الْخَلِيج.", "جَزِيرَة", ["صَحْرَاء", "غَابَة", "جَبَل"], "Bahrain lies in the Gulf, surrounded by water.", tr="Bahrain is an island in the Gulf."),
    ],
    verify=vw("جَبَل", "بَحْر", "نَهْر", "صَحْرَاء", "شَاطِئ", "جَزِيرَة", "غَابَة", "بُحَيْرَة", "وَادِي", "سَاحِل", "الْبَحْر الْأَحْمَر")
           + vpb("جَبَل", "جِبَال"),
)

# ---------------------------------------------------------------------------- 36
L36 = lesson(
    "In, on, to, from, with",
    "فِي · عَلَى · إِلَى · مِنْ · عَنْ · مَعَ",
    requires=["في", "على", "إلى", "من", "عن", "مع"],
    cards=[
        card("Six small words",
             "Prepositions come before their noun. Some of them change their last vowel when ال follows: "
             "مِنْ becomes مِنَ الْـ and عَنْ becomes عَنِ الْـ.",
             tables=[table(["English", "Arabic", "Example"],
                           [["in, at", "فِي", "فِي الْبَيْت"], ["on, over", "عَلَى", "عَلَى الْمَكْتَب"],
                            ["to", "إِلَى", "إِلَى الْمَدْرَسَة"], ["from", "مِنْ", "مِنَ الْمَدْرَسَة"],
                            ["about", "عَنْ", "عَنِ الطَّقْس"], ["with", "مَعَ", "مَعَ صَدِيقِي"]],
                           say=[1, 2], tlit=[1], gloss=False)]),
        card("“There is…” without a verb",
             "Arabic does not need a word for “there is”. Put the place first and an indefinite noun after it: “in the house a "
             "book” means “there is a book in the house”. Turn it around, with a definite noun first, and you get "
             "an ordinary sentence: “the book is in the house”.",
             examples=[
                 ex("فِي الْبَيْت كِتَاب.", "There is a book in the house."),
                 ex("الْكِتَاب فِي الْبَيْت.", "The book is in the house."),
                 ex("فِي الْمَدِينَة مَسْجِد كَبِير.", "There is a big mosque in the city."),
                 ex("عَلَى الْمَكْتَب هَاتِف.", "There is a phone on the desk."),
                 ex("فِي الْفُنْدُق مَطْعَم.", "There is a restaurant in the hotel."),
             ]),
        card("Verbs and their prepositions",
             "Some verbs usually take a particular preposition, like English “talk about”.",
             examples=[
                 ex("أَذْهَب إِلَى الْمَدْرَسَة مَعَ صَدِيقِي.", "I go to school with my friend."),
                 ex("أَتَكَلَّم عَنِ الطَّقْس.", "I talk about the weather."),
                 ex("أَنَا مِنَ الْمَغْرِب.", "I am from Morocco."),
             ]),
    ],
    exercises=[
        M("Which word means “in”?", "فِي", ["عَلَى", "إِلَى", "مَعَ"], "فِي means in or at."),
        M("Which word means “on”?", "عَلَى", ["فِي", "عَنْ", "مِنْ"], "عَلَى = on, over."),
        M("Which word means “to”?", "إِلَى", ["مِنْ", "عَنْ", "مَعَ"], "إِلَى = to."),
        M("Which word means “with”?", "مَعَ", ["عَنْ", "إِلَى", "فِي"], "مَعَ = with."),
        M("Which means “There is a book in the house”?", "فِي الْبَيْت كِتَاب", ["الْكِتَاب فِي الْبَيْت", "فِي الْكِتَاب بَيْت", "كِتَاب إِلَى الْبَيْت"], "Place first, indefinite noun after."),
        M("Which means “The book is in the house”?", "الْكِتَاب فِي الْبَيْت", ["فِي الْبَيْت كِتَاب", "الْبَيْت الْكِتَاب فِي", "الْبَيْت فِي الْكِتَاب"], "A definite noun first makes an ordinary sentence."),
        M("What does مِنَ الْمَدْرَسَة mean?", "from the school", ["to the school", "in the school", "with the school"], "مِنْ = from."),
        F("أَذْهَب ___ الْمَدْرَسَة.", "إِلَى", ["مِنْ", "عَنْ", "مَعَ"], "Going to a place: إِلَى.", tr="I go to school."),
        F("أَدْرُس ___ صَدِيقِي.", "مَعَ", ["عَلَى", "إِلَى", "عَنْ"], "“With” a person: مَعَ.", tr="I study with my friend."),
        F("أَنَا ___ مِصْر.", "مِنْ", ["مَعَ", "عَلَى", "عَنْ"], "Where you come from: مِنْ.", tr="I am from Egypt."),
    ],
    verify=vw("فِي", "عَلَى", "إِلَى", "مِنَ", "عَنِ", "مَعَ", "مَسْجِد", "مَطْعَم", "فُنْدُق", "أَتَكَلَّم")
           + vv("ذهب", "pres", ana="أَذْهَب") + vv("درس", "pres", ana="أَدْرُس"),
)

# ---------------------------------------------------------------------------- 37
L37 = lesson(
    "Countries and capitals",
    "عَاصِمَة مِصْر الْقَاهِرَة",
    requires=["عاصمة", "مدينة", "بلد", "دولة", "وطن"],
    cards=[
        card("Capital of…",
             "To say “the capital of Egypt”, put the two nouns side by side: عَاصِمَة مِصْر. The first noun "
             "never takes ال and the second is the owner. This two-noun link is called an iḍāfa, and you will use it "
             "all the time.",
             examples=[
                 ex("عَاصِمَة مِصْر الْقَاهِرَة.", "The capital of Egypt is Cairo.", "عَاصِمَة مِصْر"),
                 ex("مَا عَاصِمَة الْعِرَاق؟", "What is the capital of Iraq?", "عَاصِمَة الْعِرَاق"),
                 ex("بَيْرُوت عَاصِمَة لُبْنَان.", "Beirut is the capital of Lebanon.", "عَاصِمَة لُبْنَان"),
             ]),
        card("Countries and capitals (1)",
             "Say each pair aloud, then cover one column and test yourself.",
             tables=[table(["English", "Country", "Capital"],
                           [["Egypt", "مِصْر", "الْقَاهِرَة"], ["Syria", "سُورِيَا", "دِمَشْق"],
                            ["Iraq", "الْعِرَاق", "بَغْدَاد"], ["Jordan", "الْأُرْدُنّ", "عَمَّان"],
                            ["Lebanon", "لُبْنَان", "بَيْرُوت"], ["Saudi Arabia", "السُّعُودِيَّة", "الرِّيَاض"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Countries and capitals (2)",
             "Tunisia, Algeria and Kuwait share their name with their capital city.",
             tables=[table(["English", "Country", "Capital"],
                           [["Morocco", "الْمَغْرِب", "الرَّبَاط"], ["Yemen", "الْيَمَن", "صَنْعَاء"],
                            ["Sudan", "السُّودَان", "الْخُرْطُوم"], ["Tunisia", "تُونُس", "تُونُس"],
                            ["Algeria", "الْجَزَائِر", "الْجَزَائِر"], ["Libya", "لِيبِيَا", "طَرَابُلُس"],
                            ["Oman", "عُمَان", "مَسْقَط"], ["Qatar", "قَطَر", "الدَّوْحَة"],
                            ["Bahrain", "الْبَحْرَيْن", "الْمَنَامَة"], ["Kuwait", "الْكُوَيْت", "الْكُوَيْت"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
    ],
    exercises=[
        M("What is the capital of Egypt?", "الْقَاهِرَة", ["دِمَشْق", "بَغْدَاد", "عَمَّان"], "عَاصِمَة مِصْر الْقَاهِرَة."),
        M("What is the capital of Syria?", "دِمَشْق", ["بَيْرُوت", "عَمَّان", "الرِّيَاض"], "عَاصِمَة سُورِيَا دِمَشْق."),
        M("What is the capital of Iraq?", "بَغْدَاد", ["دِمَشْق", "الْقَاهِرَة", "الدَّوْحَة"], "عَاصِمَة الْعِرَاق بَغْدَاد."),
        M("What is the capital of Saudi Arabia?", "الرِّيَاض", ["الرَّبَاط", "مَسْقَط", "صَنْعَاء"], "عَاصِمَة السُّعُودِيَّة الرِّيَاض."),
        M("What is the capital of Morocco?", "الرَّبَاط", ["الرِّيَاض", "تُونُس", "الْخُرْطُوم"], "عَاصِمَة الْمَغْرِب الرَّبَاط."),
        M("What is the capital of Qatar?", "الدَّوْحَة", ["الْمَنَامَة", "مَسْقَط", "الْكُوَيْت"], "عَاصِمَة قَطَر الدَّوْحَة."),
        M("Which means “the capital of Lebanon”?", "عَاصِمَة لُبْنَان", ["الْعَاصِمَة لُبْنَان", "عَاصِمَة فِي لُبْنَان", "لُبْنَان عَاصِمَة"], "In an iḍāfa the first noun has no ال."),
        M("Which capital shares its name with its country?", "تُونُس", ["بَغْدَاد", "دِمَشْق", "الرَّبَاط"], "تُونُس is both the country and its capital."),
        F("بَيْرُوت ___ لُبْنَان.", "عَاصِمَة", ["الْعَاصِمَة", "مَدِينَة", "بَلَد"], "The first noun of an iḍāfa has no ال.", tr="Beirut is the capital of Lebanon."),
    ],
    verify=vw("عَاصِمَة", "الْقَاهِرَة", "دِمَشْق", "بَغْدَاد", "عَمَّان", "بَيْرُوت", "الرِّيَاض", "الرَّبَاط", "صَنْعَاء",
              "الْخُرْطُوم", "تُونُس", "الْجَزَائِر", "طَرَابُلُس", "مَسْقَط", "الدَّوْحَة", "الْمَنَامَة", "الْكُوَيْت"),
)

# ---------------------------------------------------------------------------- 38
L38 = lesson(
    "Languages",
    "الْعَرَبِيَّة · الْإِنْجِلِيزِيَّة · الْفَرَنْسِيَّة",
    requires=["لغة", "عربي", "إنجليزي", "فرنسي", "روسي", "صيني", "ألماني", "تركي"],
    cards=[
        card("Naming a language",
             "A language is the feminine nisba adjective (the same ending as مِصْرِيَّة) with ال. The full phrase "
             "is اللُّغَة الْعَرَبِيَّة, “the Arabic language”, and in daily use the first word is simply dropped.",
             tables=[table(["English", "Arabic"],
                           [["language", "لُغَة"], ["Arabic", "الْعَرَبِيَّة"], ["English", "الْإِنْجِلِيزِيَّة"],
                            ["French", "الْفَرَنْسِيَّة"], ["Spanish", "الْإِسْبَانِيَّة"], ["Russian", "الرُّوسِيَّة"],
                            ["Chinese", "الصِّينِيَّة"], ["German", "الْأَلْمَانِيَّة"], ["Turkish", "التُّرْكِيَّة"],
                            ["Persian", "الْفَارِسِيَّة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Speaking, writing, knowing",
             "أَتَكَلَّم means “I speak”. To say “in Arabic”, join بِـ to the language: بِالْعَرَبِيَّة. "
             "Add قَلِيلًا (a little) or جَيِّدًا (well) at the end.",
             examples=[
                 ex("أَتَكَلَّم الْعَرَبِيَّة وَالْإِنْجِلِيزِيَّة.", "I speak Arabic and English.", "أَتَكَلَّم"),
                 ex("هَلْ تَتَكَلَّم الْفَرَنْسِيَّة؟", "Do you speak French?", "تَتَكَلَّم"),
                 ex("نَعَمْ، أَتَكَلَّم الْفَرَنْسِيَّة قَلِيلًا.", "Yes, I speak French a little.", "قَلِيلًا"),
                 ex("أَكْتُب بِالْعَرَبِيَّة.", "I write in Arabic.", "بِالْعَرَبِيَّة"),
                 ex("نَتَكَلَّم الرُّوسِيَّة جَيِّدًا.", "We speak Russian well.", "جَيِّدًا"),
             ]),
    ],
    exercises=[
        M("Which means “Arabic” (the language)?", "الْعَرَبِيَّة", ["الْعَرَبِيّ", "عَرَبِيَّة", "الْعَرَب"], "Feminine nisba with ال."),
        M("Which means “English”?", "الْإِنْجِلِيزِيَّة", ["الْفَرَنْسِيَّة", "الْأَلْمَانِيَّة", "الرُّوسِيَّة"], "الْإِنْجِلِيزِيَّة = English."),
        M("Which means “French”?", "الْفَرَنْسِيَّة", ["الْإِسْبَانِيَّة", "الْإِنْجِلِيزِيَّة", "التُّرْكِيَّة"], "الْفَرَنْسِيَّة = French."),
        M("Which means “Chinese”?", "الصِّينِيَّة", ["الرُّوسِيَّة", "الْفَارِسِيَّة", "الْعَرَبِيَّة"], "الصِّينِيَّة = Chinese."),
        M("Which means “Russian”?", "الرُّوسِيَّة", ["الصِّينِيَّة", "الْأَلْمَانِيَّة", "الْفَرَنْسِيَّة"], "الرُّوسِيَّة = Russian."),
        M("Which means “in Arabic”?", "بِالْعَرَبِيَّة", ["فِي عَرَبِيَّة", "مِنَ الْعَرَبِيَّة", "عَلَى الْعَرَبِيَّة"], "بِـ + الْعَرَبِيَّة."),
        M("Which means “I speak”?", "أَتَكَلَّم", ["تَتَكَلَّم", "نَتَكَلَّم", "يَتَكَلَّم"], "أَـ = I.", lemma=None),
        M("What does قَلِيلًا mean in أَتَكَلَّم الْعَرَبِيَّة قَلِيلًا?", "a little", ["well", "every day", "badly"], "قَلِيلًا = a little."),
        F("هَلْ ___ الْفَرَنْسِيَّة؟", "تَتَكَلَّم", ["أَتَكَلَّم", "نَتَكَلَّم", "يَتَكَلَّم"], "You are asking the listener, تَـ.", tr="Do you speak French?"),
        F("أَكْتُب ___.", "بِالْعَرَبِيَّة", ["فِي عَرَبِيَّة", "عَرَبِيَّة", "مِنَ الْعَرَبِيَّة"], "“In Arabic” is بِالْعَرَبِيَّة.", tr="I write in Arabic."),
    ],
    verify=vw("لُغَة", "الْعَرَبِيَّة", "الْإِنْجِلِيزِيَّة", "الْفَرَنْسِيَّة", "الْإِسْبَانِيَّة", "الرُّوسِيَّة", "الصِّينِيَّة",
              "الْأَلْمَانِيَّة", "التُّرْكِيَّة", "الْفَارِسِيَّة", "أَتَكَلَّم", "تَتَكَلَّم", "نَتَكَلَّم", "قَلِيلًا", "جَيِّدًا"),
)

# ---------------------------------------------------------------------------- 39
L39 = lesson(
    "The present tense: every person",
    "أَكْتُب · تَكْتُبِين · يَكْتُبُون",
    requires=["كتب", "أنا", "أنت", "هو", "هي", "نحن", "هم"],
    cards=[
        card("One verb, thirteen persons",
             "You already know the prefixes أَـ نَـ تَـ يَـ. Many persons also take an ending, shown in the "
             "highlight below. A masculine and a feminine “you” differ, and so do “you” and “they” in the plural. "
             "Here is the verb كَتَبَ, “to write”, in every person.",
             tables=[table(["Person", "Verb", "English"],
                           [["أَنَا", "{أَ}كْتُب", "I write"], ["أَنْتَ", "{تَ}كْتُب", "you write (man)"],
                            ["أَنْتِ", "{تَ}كْتُ{بِين}", "you write (woman)"], ["هُوَ", "{يَ}كْتُب", "he writes"],
                            ["هِيَ", "{تَ}كْتُب", "she writes"]],
                           title="Singular", say=[0, 1], tlit=[1], gloss=False),
                    table(["Person", "Verb", "English"],
                          [["نَحْنُ", "{نَ}كْتُب", "we write"], ["أَنْتُم", "{تَ}كْتُ{بُون}", "you write (men)"],
                           ["أَنْتُنَّ", "{تَ}كْتُ{بْنَ}", "you write (women)"], ["هُم", "{يَ}كْتُ{بُون}", "they write (men)"],
                           ["هُنَّ", "{يَ}كْتُ{بْنَ}", "they write (women)"]],
                          title="Plural", say=[0, 1], tlit=[1], gloss=False)]),
        card("Two people: the dual",
             "Arabic has a special form for exactly two. You will study it in unit 5. For now, notice that it "
             "ends in ـَان and that “you two” and “they two (women)” share the same verb, تَكْتُبَان.",
             tables=[table(["Person", "Verb", "English"],
                           [["أَنْتُمَا", "{تَ}كْتُ{بَان}", "you two write"], ["هُمَا", "{يَ}كْتُ{بَان}", "they two write (men)"],
                            ["هُمَا", "{تَ}كْتُ{بَان}", "they two write (women)"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("A pronoun is optional",
             "Because the prefix and ending already show who is meant, a pronoun is mostly used for emphasis or contrast.",
             examples=[
                 ex("هُم يَكْتُبُون وَنَحْنُ نَدْرُس.", "They write and we study.", "يَكْتُبُون"),
                 ex("أَنْتُم تَكْتُبُون بِالْعَرَبِيَّة.", "You (all) write in Arabic.", "تَكْتُبُون"),
                 ex("هُنَّ يَكْتُبْنَ الدَّرْس.", "They (women) write the lesson.", "يَكْتُبْنَ"),
             ]),
    ],
    exercises=[
        M("Which means “you (woman) write”?", "تَكْتُبِين", ["تَكْتُب", "تَكْتُبُون", "تَكْتُبْنَ"], "A woman is addressed with ـِين.", lemma="كتب:pres:anti"),
        M("Which means “you (men) write”?", "تَكْتُبُون", ["تَكْتُبِين", "تَكْتُبْنَ", "يَكْتُبُون"], "ـُون for a group of men.", lemma="كتب:pres:antum"),
        M("Which means “you (women) write”?", "تَكْتُبْنَ", ["تَكْتُبُون", "تَكْتُبِين", "يَكْتُبْنَ"], "ـْنَ for a group of women.", lemma="كتب:pres:antunna"),
        M("Which means “they (men) write”?", "يَكْتُبُون", ["يَكْتُبْنَ", "تَكْتُبُون", "نَكْتُب"], "يَـ + ـُون.", lemma="كتب:pres:hum"),
        M("Which means “they (women) write”?", "يَكْتُبْنَ", ["يَكْتُبُون", "تَكْتُبْنَ", "تَكْتُبِين"], "يَـ + ـْنَ.", lemma="كتب:pres:hunna"),
        M("Which means “we write”?", "نَكْتُب", ["أَكْتُب", "يَكْتُبُون", "تَكْتُبُون"], "نَـ = we.", lemma="كتب:pres:nahnu"),
        M("Which ending shows a woman being addressed?", "ـِين", ["ـُون", "ـْنَ", "ـَان"], "تَكْتُبِين."),
        M("What is the difference between تَكْتُب and يَكْتُب?", "Only the prefix", ["The ending", "The tense", "Nothing; they are the same"], "تَـ shows you or she; يَـ shows he."),
        F("هُم ___ بِالْعَرَبِيَّة.", "يَكْتُبُون", ["يَكْتُب", "تَكْتُبُون", "أَكْتُب"], "Masculine plural “they”.", tr="They write in Arabic.", lemma="كتب:pres:hum"),
        F("أَنْتِ ___ الدَّرْس.", "تَكْتُبِين", ["تَكْتُب", "يَكْتُب", "تَكْتُبُون"], "A woman: ـِين.", tr="You write the lesson. (to a woman)", lemma="كتب:pres:anti"),
    ],
    verify=(vv("كتب", "pres", ana="أَكْتُب", nahnu="نَكْتُب", anta="تَكْتُب", anti="تَكْتُبِين", antuma="تَكْتُبَان",
               antum="تَكْتُبُون", antunna="تَكْتُبْنَ", huwa="يَكْتُب", hiya="تَكْتُب", huma_m="يَكْتُبَان", huma_f="تَكْتُبَان",
               hum="يَكْتُبُون", hunna="يَكْتُبْنَ") + vv("درس", "pres", nahnu="نَدْرُس")),
)

# ---------------------------------------------------------------------------- 40
L40 = lesson(
    "Which vowel? Verb patterns",
    "يَكْتُب · يَذْهَب · يَجْلِس",
    requires=["كتب", "درس", "ذهب", "جلس", "فتح", "شرب"],
    cards=[
        card("A verb has three letters and a vowel",
             "Most Arabic verbs are built on three root letters. For these verbs the prefix and endings you just learned stay the same, "
             "but the vowel on the middle letter of the present tense depends on the verb, and you "
             "have to learn it with the word. Textbooks and many dictionaries give the “he” form of the past together with "
             "the present-tense vowel, so they show the vowel for you.",
             tables=[table(["English", "he … (past)", "he … (present)"],
                           [["write", "كَتَبَ", "يَكْ{تُ}ب"], ["study", "دَرَسَ", "يَدْ{رُ}س"],
                            ["go out", "خَرَجَ", "يَخْ{رُ}ج"], ["enter", "دَخَلَ", "يَدْ{خُ}ل"],
                            ["look", "نَظَرَ", "يَنْ{ظُ}ر"]],
                           title="Present vowel ـُ (ḍamma)", say=[1, 2], tlit=[2], gloss=False)]),
        card("The other two vowels",
             "The same rule holds for verbs with ـَ and ـِ in the present tense. Say each pair aloud.",
             tables=[table(["English", "he … (past)", "he … (present)"],
                           [["go", "ذَهَبَ", "يَذْ{هَ}ب"], ["open", "فَتَحَ", "يَفْ{تَ}ح"],
                            ["drink", "شَرِبَ", "يَشْ{رَ}ب"], ["work", "عَمِلَ", "يَعْ{مَ}ل"],
                            ["understand", "فَهِمَ", "يَفْ{هَ}م"], ["hear", "سَمِعَ", "يَسْ{مَ}ع"],
                            ["play", "لَعِبَ", "يَلْ{عَ}ب"]],
                           title="Present vowel ـَ (fatḥa)", say=[1, 2], tlit=[2], gloss=False),
                    table(["English", "he … (past)", "he … (present)"],
                          [["sit", "جَلَسَ", "يَجْ{لِ}س"], ["know", "عَرَفَ", "يَعْ{رِ}ف"], ["return", "رَجَعَ", "يَرْ{جِ}ع"]],
                          title="Present vowel ـِ (kasra)", say=[1, 2], tlit=[2], gloss=False)]),
        card("Using them",
             "Once you know the vowel, every person follows the pattern from the last lesson.",
             examples=[
                 ex("أَجْلِس فِي الْمَكْتَب.", "I sit in the office.", "أَجْلِس"),
                 ex("يَفْتَح أَحْمَد الْبَاب.", "Ahmad opens the door.", "يَفْتَح"),
                 ex("نَشْرَب الْمَاء.", "We drink water.", "نَشْرَب"),
                 ex("هَلْ تَعْرِفِين سَارَة؟", "Do you know Sara? (to a woman)", "تَعْرِفِين"),
                 ex("يَخْرُجُون مِنَ الْبَيْت.", "They go out of the house.", "يَخْرُجُون"),
             ]),
    ],
    exercises=[
        M("Which is “I sit”?", "أَجْلِس", ["أَجْلُس", "أَجْلَس", "تَجْلِس"], "جَلَسَ takes ـِ in the present.", lemma="جلس:pres:ana"),
        M("Which is “I open”?", "أَفْتَح", ["أَفْتُح", "أَفْتِح", "نَفْتَح"], "فَتَحَ takes ـَ in the present.", lemma="فتح:pres:ana"),
        M("Which is “she goes out”?", "تَخْرُج", ["تَخْرَج", "تَخْرِج", "يَخْرُج"], "خَرَجَ takes ـُ in the present.", lemma="خرج:pres:hiya"),
        M("Which is “we understand”?", "نَفْهَم", ["نَفْهُم", "نَفْهِم", "أَفْهَم"], "فَهِمَ takes ـَ in the present.", lemma="فهم:pres:nahnu"),
        M("Which is “they (men) drink”?", "يَشْرَبُون", ["يَشْرُبُون", "يَشْرِبُون", "تَشْرَبُون"], "شَرِبَ takes ـَ.", lemma="شرب:pres:hum"),
        M("Which is “you (woman) know”?", "تَعْرِفِين", ["تَعْرَفِين", "تَعْرُفِين", "تَعْرِف"], "عَرَفَ takes ـِ.", lemma="عرف:pres:anti"),
        M("Which is “he enters”?", "يَدْخُل", ["يَدْخَل", "يَدْخِل", "تَدْخُل"], "دَخَلَ takes ـُ.", lemma="دخل:pres:huwa"),
        M("Why must you learn the present vowel with each verb?", "It differs from verb to verb", ["It is always ـُ", "It shows the person", "It shows the tense"], "The prefix shows the person; the middle vowel belongs to the verb."),
        F("___ أَحْمَد الْبَاب.", "يَفْتَح", ["يَفْتُح", "يَفْتِح", "تَفْتَح"], "Masculine subject, verb with ـَ.", tr="Ahmad opens the door.", lemma="فتح:pres:huwa"),
        F("أَنَا ___ فِي الْبَيْت.", "أَجْلِس", ["أَجْلَس", "أَجْلُس", "نَجْلِس"], "First person singular, verb with ـِ.", tr="I sit in the house.", lemma="جلس:pres:ana"),
    ],
    verify=(vv("كتب", "past", huwa="كَتَبَ") + vv("كتب", "pres", huwa="يَكْتُب")
            + vv("درس", "past", huwa="دَرَسَ") + vv("درس", "pres", huwa="يَدْرُس")
            + vv("خرج", "past", huwa="خَرَجَ") + vv("خرج", "pres", huwa="يَخْرُج", hiya="تَخْرُج", hum="يَخْرُجُون")
            + vv("دخل", "past", huwa="دَخَلَ") + vv("دخل", "pres", huwa="يَدْخُل")
            + vv("نظر", "past", huwa="نَظَرَ") + vv("نظر", "pres", huwa="يَنْظُر")
            + vv("ذهب", "past", huwa="ذَهَبَ") + vv("ذهب", "pres", huwa="يَذْهَب")
            + vv("فتح", "past", huwa="فَتَحَ") + vv("فتح", "pres", huwa="يَفْتَح", ana="أَفْتَح")
            + vv("شرب", "past", huwa="شَرِبَ") + vv("شرب", "pres", huwa="يَشْرَب", nahnu="نَشْرَب", hum="يَشْرَبُون")
            + vv("عمل", "past", huwa="عَمِلَ") + vv("عمل", "pres", huwa="يَعْمَل")
            + vv("فهم", "past", huwa="فَهِمَ") + vv("فهم", "pres", huwa="يَفْهَم", nahnu="نَفْهَم")
            + vv("سمع", "past", huwa="سَمِعَ") + vv("سمع", "pres", huwa="يَسْمَع")
            + vv("لعب", "past", huwa="لَعِبَ") + vv("لعب", "pres", huwa="يَلْعَب")
            + vv("جلس", "past", huwa="جَلَسَ") + vv("جلس", "pres", huwa="يَجْلِس", ana="أَجْلِس")
            + vv("عرف", "past", huwa="عَرَفَ") + vv("عرف", "pres", huwa="يَعْرِف", anti="تَعْرِفِين")
            + vv("رجع", "past", huwa="رَجَعَ") + vv("رجع", "pres", huwa="يَرْجِع")),
)

# ---------------------------------------------------------------------------- 41
L41 = lesson(
    "Saying no: لَا + verb",
    "لَا أَعْرِف · لَا أَفْهَم",
    requires=["لا", "عرف", "فهم", "كتب", "درس", "ذهب"],
    cards=[
        card("Negating a present-tense verb",
             "To say that something is not happening, put لَا in front of the present-tense verb. The verb itself "
             "does not change at all: the prefix and endings stay exactly as they were.",
             tables=[table(["English", "Arabic"],
                           [["I don’t write", "لَا أَكْتُب"], ["you don’t write (man)", "لَا تَكْتُب"],
                            ["he doesn’t write", "لَا يَكْتُب"], ["we don’t write", "لَا نَكْتُب"],
                            ["they don’t write (men)", "لَا يَكْتُبُون"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Keep the usual verb-first order. With تَـ, a similar form gives an order, “don’t…!” (some endings change); you "
             "will meet that in unit 6.",
             examples=[
                 ex("لَا أَعْرِف.", "I don’t know.", "لَا"),
                 ex("لَا أَفْهَم.", "I don’t understand.", "لَا"),
                 ex("لَا يَسْكُن أَحْمَد فِي الْقَاهِرَة.", "Ahmad doesn’t live in Cairo.", "لَا"),
                 ex("لَا نَدْرُس الْيَوْم.", "We don’t study today.", "لَا"),
                 ex("لَا تَذْهَب سَارَة إِلَى الْمَكْتَب.", "Sara doesn’t go to the office.", "لَا"),
                 ex("لَا، شُكْرًا.", "No, thank you."),
             ]),
    ],
    exercises=[
        M("Which means “I don’t know”?", "لَا أَعْرِف", ["لَا تَعْرِف", "لَا يَعْرِف", "لَا نَعْرِف"], "لَا + أَعْرِف (I know)."),
        M("Which means “I don’t understand”?", "لَا أَفْهَم", ["لَا نَفْهَم", "لَا تَفْهَم", "لَا يَفْهَم"], "لَا + أَفْهَم."),
        M("Which means “Ahmad doesn’t live in Cairo”?", "لَا يَسْكُن أَحْمَد فِي الْقَاهِرَة", ["لَا تَسْكُن أَحْمَد فِي الْقَاهِرَة", "لَا أَسْكُن أَحْمَد فِي الْقَاهِرَة", "لَا نَسْكُن أَحْمَد فِي الْقَاهِرَة"], "Ahmad is masculine, so يَـ."),
        M("Which means “we don’t study today”?", "لَا نَدْرُس الْيَوْم", ["لَا أَدْرُس الْيَوْم", "لَا يَدْرُس الْيَوْم", "لَا تَدْرُس الْيَوْم"], "نَـ = we."),
        M("Which word negates a present-tense verb?", "لَا", ["لَيْسَ", "هَلْ", "مَنْ"], "لَا goes in front of the verb."),
        M("What happens to the verb after لَا?", "Nothing: it stays the same", ["It loses its prefix", "It turns into the past", "It takes ـُون"], "Only لَا is added."),
        F("لَا ___ الْيَوْم.", "أَدْرُس", ["تَدْرُسِين", "يَدْرُسُون", "نَدْرُس"], "The sentence says “I”.", tr="I don’t study today.", lemma="درس:pres:ana"),
        F("لَا ___ سَارَة إِلَى الْمَكْتَب.", "تَذْهَب", ["يَذْهَب", "أَذْهَب", "نَذْهَب"], "Sara is feminine, so تَـ.", tr="Sara doesn’t go to the office.", lemma="ذهب:pres:hiya"),
        F("هَلْ تَفْهَم؟ لَا، لَا ___.", "أَفْهَم", ["تَفْهَم", "يَفْهَم", "نَفْهَم"], "You answer for yourself: أَـ.", tr="Do you understand? No, I don’t understand.", lemma="فهم:pres:ana"),
    ],
    verify=(vv("عرف", "pres", ana="أَعْرِف", anta="تَعْرِف", huwa="يَعْرِف", nahnu="نَعْرِف")
            + vv("فهم", "pres", ana="أَفْهَم", nahnu="نَفْهَم", anta="تَفْهَم", huwa="يَفْهَم")
            + vv("سكن", "pres", huwa="يَسْكُن", ana="أَسْكُن", hiya="تَسْكُن", nahnu="نَسْكُن")
            + vv("درس", "pres", nahnu="نَدْرُس", ana="أَدْرُس", huwa="يَدْرُس", anta="تَدْرُس")
            + vv("ذهب", "pres", hiya="تَذْهَب", huwa="يَذْهَب", ana="أَذْهَب", nahnu="نَذْهَب")
            + vv("كتب", "pres", ana="أَكْتُب", anta="تَكْتُب", huwa="يَكْتُب", nahnu="نَكْتُب", hum="يَكْتُبُون")),
)

# ---------------------------------------------------------------------------- 42
L42 = lesson(
    "Saying “is not”: لَيْسَ",
    "لَسْتُ · لَيْسَ · لَيْسَتْ",
    requires=["ليس", "لا", "طالب", "كبير", "بارد"],
    cards=[
        card("To be not",
             "Arabic has no word for “is” in the present, so “he is a student” is just هُوَ طَالِب. To negate a "
             "sentence like that, use لَيْسَ. It is a verb that changes for the person, like a past-tense verb.",
             tables=[table(["Person", "Arabic", "English"],
                           [["أَنَا", "لَسْتُ", "I am not"], ["أَنْتَ", "لَسْتَ", "you are not (man)"],
                            ["أَنْتِ", "لَسْتِ", "you are not (woman)"], ["هُوَ", "لَيْسَ", "he is not"],
                            ["هِيَ", "لَيْسَتْ", "she is not"], ["نَحْنُ", "لَسْنَا", "we are not"],
                            ["أَنْتُم", "لَسْتُم", "you are not (men)"], ["هُم", "لَيْسُوا", "they are not (men)"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("The word after لَيْسَ",
             "The noun or adjective that follows لَيْسَ takes a new ending: ـًا, or ـً on a word that ends in "
             "ة. You can see it in the examples. Write it with the ending, even though it is not essential for "
             "understanding.",
             examples=[
                 ex("لَسْتُ طَالِبًا.", "I am not a student. (a man speaking)", "طَالِبًا"),
                 ex("لَسْتِ مُدَرِّسَةً.", "You are not a teacher. (to a woman)", "مُدَرِّسَةً"),
                 ex("هُوَ لَيْسَ مُهَنْدِسًا.", "He is not an engineer.", "لَيْسَ"),
                 ex("هِيَ لَيْسَتْ مِصْرِيَّةً.", "She is not Egyptian.", "لَيْسَتْ"),
                 ex("الطَّقْس لَيْسَ بَارِدًا الْيَوْم.", "The weather is not cold today.", "لَيْسَ"),
                 ex("لَسْنَا طُلَّابًا.", "We are not students.", "لَسْنَا"),
             ]),
        card("لَا or لَيْسَ",
             "Ask what comes next. A verb is negated with لَا; a noun or an adjective is negated with لَيْسَ.",
             tables=[table(["English", "Arabic"],
                           [["I don’t study (verb)", "لَا أَدْرُس"], ["I am not a student (noun)", "لَسْتُ طَالِبًا"],
                            ["he doesn’t work (verb)", "لَا يَعْمَل"], ["he is not busy (adjective)", "لَيْسَ مَشْغُولًا"]],
                           say=[1], tlit=[1], gloss=False)]),
    ],
    exercises=[
        M("Which means “I am not a student” (a man speaking)?", "لَسْتُ طَالِبًا", ["لَيْسَ طَالِبًا", "لَسْنَا طَالِبًا", "لَا طَالِب"], "لَسْتُ is “I am not”."),
        M("Which means “She is not Egyptian”?", "هِيَ لَيْسَتْ مِصْرِيَّةً", ["هِيَ لَيْسَ مِصْرِيَّةً", "هُوَ لَيْسَتْ مِصْرِيَّةً", "هِيَ لَسْتُ مِصْرِيَّةً"], "لَيْسَتْ is the feminine form."),
        M("Which means “We are not students”?", "لَسْنَا طُلَّابًا", ["لَسْتُ طُلَّابًا", "لَيْسُوا طُلَّابًا", "لَيْسَتْ طُلَّابًا"], "لَسْنَا is “we are not”."),
        M("Which means “you (woman) are not”?", "لَسْتِ", ["لَسْتَ", "لَيْسَتْ", "لَسْتُ"], "ـتِ for a woman."),
        M("Which word negates a noun sentence?", "لَيْسَ", ["لَا", "هَلْ", "نَعَمْ"], "لَيْسَ = is not."),
        M("Which negative goes with a verb like يَعْمَل?", "لَا", ["لَيْسَ", "لَسْتُ", "لَيْسَتْ"], "لَا + present verb."),
        M("Which ending appears on a word after لَيْسَ?", "ـًا", ["ـُون", "ـِين", "ـَان"], "The word after لَيْسَ takes ـًا."),
        F("أَنَا ___ مُهَنْدِسًا.", "لَسْتُ", ["لَيْسَ", "لَيْسَتْ", "لَسْنَا"], "أَنَا takes لَسْتُ.", tr="I am not an engineer."),
        F("الطَّقْس ___ بَارِدًا.", "لَيْسَ", ["لَيْسَتْ", "لَسْتُ", "لَسْنَا"], "الطَّقْس is masculine and singular.", tr="The weather is not cold."),
        F("هِيَ ___ طَالِبَةً.", "لَيْسَتْ", ["لَيْسَ", "لَسْتِ", "لَسْتُ"], "A feminine subject takes لَيْسَتْ.", tr="She is not a student."),
    ],
    verify=vw("لَسْتُ", "لَسْتَ", "لَسْتِ", "لَيْسَ", "لَيْسَتْ", "لَسْنَا", "لَسْتُم", "لَيْسُوا", "طَالِبَةً", "مُهَنْدِسًا",
              "مَشْغُولًا", "مُدَرِّسَةً"),
)

# ---------------------------------------------------------------------------- 43
L43 = lesson(
    "The weather",
    "الطَّقْس · حَارّ · بَارِد · مُمْطِر",
    requires=["طقس", "شمس", "مطر", "ثلج", "حار", "بارد", "جو"],
    cards=[
        card("Describing the weather",
             "These adjectives describe the weather. Use them after الطَّقْس or الْجَوّ, both of which mean "
             "“the weather” and are masculine, so the adjectives stay in the masculine form.",
             tables=[table(["English", "Arabic"],
                           [["hot", "حَارّ"], ["cold", "بَارِد"], ["warm", "دَافِئ"], ["mild", "مُعْتَدِل"],
                            ["dry", "جَافّ"], ["humid", "رَطْب"], ["sunny", "مُشْمِس"], ["cloudy", "غَائِم"],
                            ["rainy", "مُمْطِر"], ["stormy, very windy", "عَاصِف"]],
                           say=[1], tlit=[1])]),
        card("Weather nouns",
             "Nouns for the things in the sky.",
             tables=[table(["English", "Arabic"],
                           [["the weather", "الطَّقْس · الْجَوّ"], ["the sun", "الشَّمْس"], ["the rain", "الْمَطَر"],
                            ["the snow", "الثَّلْج"], ["the wind", "الرِّيح"], ["the clouds", "الْغُيُوم"],
                            ["the sky", "السَّمَاء"], ["temperature", "دَرَجَة الْحَرَارَة"]],
                           say=[1], tlit=[1])]),
        card("Talking about it",
             "الْجَوّ is masculine, but السَّمَاء (the sky) is feminine, so its adjective ends in ة: "
             "السَّمَاء غَائِمَة.",
             examples=[
                 ex("الطَّقْس حَارّ الْيَوْم.", "The weather is hot today."),
                 ex("الْجَوّ بَارِد وَالسَّمَاء غَائِمَة.", "The weather is cold and the sky is cloudy.", "غَائِمَة"),
                 ex("كَيْفَ الطَّقْس فِي مِصْر؟", "How is the weather in Egypt?"),
                 ex("حَارّ وَجَافّ.", "Hot and dry."),
                 ex("هَلِ الْجَوّ مُمْطِر؟", "Is it rainy?"),
                 ex("لَا، الْجَوّ مُشْمِس.", "No, it is sunny."),
                 ex("فِي الْجِبَال ثَلْج.", "There is snow in the mountains."),
             ]),
    ],
    exercises=[
        M("Which word means “hot”?", "حَارّ", ["بَارِد", "دَافِئ", "جَافّ"], "حَارّ = hot."),
        M("Which word means “cold”?", "بَارِد", ["حَارّ", "غَائِم", "رَطْب"], "بَارِد = cold."),
        M("Which word means “rainy”?", "مُمْطِر", ["مُشْمِس", "عَاصِف", "جَافّ"], "مُمْطِر comes from مَطَر (rain)."),
        M("Which word means “sunny”?", "مُشْمِس", ["غَائِم", "مُمْطِر", "بَارِد"], "مُشْمِس comes from شَمْس (sun)."),
        M("Which word means “snow”?", "الثَّلْج", ["الْمَطَر", "الشَّمْس", "الرِّيح"], "الثَّلْج = snow."),
        M("Which word means “wind”?", "الرِّيح", ["الْغُيُوم", "السَّمَاء", "الْمَطَر"], "الرِّيح = wind."),
        M("Which is right?", "السَّمَاء غَائِمَة", ["السَّمَاء غَائِم", "الْجَوّ غَائِمَة", "الْجَوّ السَّمَاء"], "السَّمَاء is feminine, الْجَوّ is masculine."),
        M("Which means “How is the weather?”", "كَيْفَ الطَّقْس؟", ["أَيْنَ الطَّقْس؟", "مَتَى الطَّقْس؟", "مَنْ الطَّقْس؟"], "كَيْفَ = how."),
        F("الطَّقْس ___ الْيَوْم.", "حَارّ", ["حَارَّة", "السَّمَاء", "الْمَطَر"], "The weather is masculine.", tr="The weather is hot today."),
        F("فِي الْجِبَال ___.", "ثَلْج", ["شَمْس", "بَحْر", "شَاطِئ"], "Snow falls on mountains.", tr="There is snow in the mountains."),
    ],
    verify=vw("حَارّ", "بَارِد", "دَافِئ", "مُعْتَدِل", "جَافّ", "رَطْب", "مُشْمِس", "غَائِم", "مُمْطِر", "عَاصِف", "الطَّقْس",
              "الْجَوّ", "الشَّمْس", "الْمَطَر", "الثَّلْج", "الرِّيح", "الْغُيُوم", "السَّمَاء", "دَرَجَة", "الْحَرَارَة"),
)

# ---------------------------------------------------------------------------- 44
L44 = lesson(
    "The seasons, and أُحِبّ",
    "الصَّيْف · الشِّتَاء · أُحِبّ",
    requires=["صيف", "شتاء", "خريف", "فصل", "أحب"],
    cards=[
        card("Four seasons",
             "الْفَصْل is “the season”. Use فِي to say “in summer”.",
             tables=[table(["English", "Arabic"],
                           [["season", "فَصْل · فُصُول"], ["spring", "الرَّبِيع"], ["summer", "الصَّيْف"],
                            ["autumn", "الْخَرِيف"], ["winter", "الشِّتَاء"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[ex("فِي الصَّيْف الطَّقْس حَارّ.", "In summer the weather is hot."),
                       ex("فِي الشِّتَاء الْجَوّ بَارِد.", "In winter it is cold.")]),
        card("To like: أُحِبّ",
             "The verb “to like, to love” has prefixes with ḍamma (أُـ تُـ يُـ نُـ) and ends in a doubled letter. "
             "It is different from كَتَبَ in how it looks, but the idea is the same: the prefix tells you who.",
             tables=[table(["English", "Arabic"],
                           [["I like", "أُحِبّ"], ["you like (man)", "تُحِبّ"], ["he likes", "يُحِبّ"],
                            ["she likes", "تُحِبّ"], ["we like", "نُحِبّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Saying what you like",
             "لِأَنَّ means “because”. It is followed by a full sentence.",
             examples=[
                 ex("أُحِبّ الشِّتَاء.", "I like winter.", "أُحِبّ"),
                 ex("هَلْ تُحِبّ الصَّيْف؟", "Do you like summer?", "تُحِبّ"),
                 ex("لَا أُحِبّ الصَّيْف لِأَنَّ الْجَوّ حَارّ جِدًّا.", "I don’t like summer because it is very hot.", "لِأَنَّ"),
                 ex("تُحِبّ سَارَة الرَّبِيع.", "Sara likes spring.", "تُحِبّ"),
                 ex("نُحِبّ الشَّاطِئ فِي الصَّيْف.", "We like the beach in summer.", "نُحِبّ"),
             ]),
    ],
    exercises=[
        M("Which word means “summer”?", "الصَّيْف", ["الشِّتَاء", "الْخَرِيف", "الرَّبِيع"], "الصَّيْف = summer."),
        M("Which word means “winter”?", "الشِّتَاء", ["الصَّيْف", "الرَّبِيع", "الْفَصْل"], "الشِّتَاء = winter."),
        M("Which word means “autumn”?", "الْخَرِيف", ["الرَّبِيع", "الصَّيْف", "الشِّتَاء"], "الْخَرِيف = autumn."),
        M("Which word means “spring”?", "الرَّبِيع", ["الْخَرِيف", "الشِّتَاء", "الْيَوْم"], "الرَّبِيع = spring."),
        M("Which means “I like winter”?", "أُحِبّ الشِّتَاء", ["تُحِبّ الشِّتَاء", "يُحِبّ الشِّتَاء", "نُحِبّ الشِّتَاء"], "أُـ = I."),
        M("Which means “we like the beach”?", "نُحِبّ الشَّاطِئ", ["أُحِبّ الشَّاطِئ", "يُحِبّ الشَّاطِئ", "تُحِبّ الشَّاطِئ"], "نُـ = we."),
        M("What does لِأَنَّ mean?", "because", ["but", "when", "with"], "لِأَنَّ = because."),
        M("Which means “I don’t like summer”?", "لَا أُحِبّ الصَّيْف", ["لَيْسَ أُحِبّ الصَّيْف", "لَا تُحِبّ الصَّيْف", "أُحِبّ لَا الصَّيْف"], "لَا + the present verb."),
        F("___ سَارَة الرَّبِيع.", "تُحِبّ", ["أُحِبّ", "يُحِبّ", "نُحِبّ"], "Sara is feminine: تُـ.", tr="Sara likes spring."),
        F("فِي ___ الْجَوّ بَارِد.", "الشِّتَاء", ["الصَّيْف", "الْغَابَة", "الْجَبَل"], "Winter is the cold season.", tr="In winter the weather is cold."),
    ],
    verify=vw("أُحِبّ", "تُحِبّ", "يُحِبّ", "نُحِبّ", "الرَّبِيع", "الصَّيْف", "الْخَرِيف", "الشِّتَاء", "لِأَنَّ", "جِدًّا", "فُصُول"),
)

# ---------------------------------------------------------------------------- 45
L45 = lesson(
    "Bigger, smaller, colder: أَفْعَل",
    "أَكْبَر مِنْ · أَصْغَر مِنْ",
    requires=["أكبر", "أصغر", "أجمل", "كبير", "صغير", "جميل"],
    cards=[
        card("The comparative shape",
             "To say “bigger”, “colder” and so on, fit the three root letters of the adjective into the pattern "
             "أَ _ْ _َ _. So كَبِير (big, root ك-ب-ر) becomes أَكْبَر (bigger). When it is used with مِنْ (“than”), the word does not change for gender or "
             "number.",
             tables=[table(["English", "Adjective", "Comparative"],
                           [["big", "كَبِير", "أَكْبَر"], ["small", "صَغِير", "أَصْغَر"], ["beautiful", "جَمِيل", "أَجْمَل"],
                            ["long, tall", "طَوِيل", "أَطْوَل"], ["short", "قَصِير", "أَقْصَر"],
                            ["near", "قَرِيب", "أَقْرَب"], ["far", "بَعِيد", "أَبْعَد"], ["cold", "بَارِد", "أَبْرَد"],
                            ["easy", "سَهْل", "أَسْهَل"], ["difficult", "صَعْب", "أَصْعَب"], ["many, much", "كَثِير", "أَكْثَر"]],
                           say=[1, 2], tlit=[2], gloss=False)]),
        card("Comparing with مِنْ",
             "Use مِنْ for “than”: “Cairo bigger than Damascus”. The comparative stays the same for a "
             "feminine subject such as الْقَاهِرَة.",
             examples=[
                 ex("الْقَاهِرَة أَكْبَر مِنْ دِمَشْق.", "Cairo is bigger than Damascus.", "أَكْبَر مِنْ"),
                 ex("النِّيل أَطْوَل مِنَ الْفُرَات.", "The Nile is longer than the Euphrates.", "أَطْوَل مِنَ"),
                 ex("الْعِرَاق أَصْغَر مِنَ السُّعُودِيَّة.", "Iraq is smaller than Saudi Arabia.", "أَصْغَر مِنَ"),
                 ex("الشِّتَاء أَبْرَد مِنَ الْخَرِيف.", "Winter is colder than autumn.", "أَبْرَد مِنَ"),
             ]),
        card("The biggest",
             "To say “the biggest”, put the comparative before a singular noun without ال.",
             examples=[
                 ex("الْقَاهِرَة أَكْبَر مَدِينَة فِي الْوَطَن الْعَرَبِيّ.", "Cairo is the biggest city in the Arab world.", "أَكْبَر مَدِينَة"),
                 ex("النِّيل أَطْوَل نَهْر فِي أَفْرِيقِيَا.", "The Nile is the longest river in Africa.", "أَطْوَل نَهْر"),
             ]),
    ],
    exercises=[
        M("Which means “bigger”?", "أَكْبَر", ["كَبِير", "أَصْغَر", "أَكْثَر"], "كَبِير → أَكْبَر."),
        M("Which means “smaller”?", "أَصْغَر", ["صَغِير", "أَكْبَر", "أَقْصَر"], "صَغِير → أَصْغَر."),
        M("Which means “longer, taller”?", "أَطْوَل", ["أَقْصَر", "طَوِيل", "أَبْعَد"], "طَوِيل → أَطْوَل."),
        M("Which means “colder”?", "أَبْرَد", ["بَارِد", "أَكْثَر", "أَقْرَب"], "بَارِد → أَبْرَد."),
        M("Which means “Cairo is bigger than Damascus”?", "الْقَاهِرَة أَكْبَر مِنْ دِمَشْق", ["دِمَشْق أَكْبَر مِنَ الْقَاهِرَة", "الْقَاهِرَة كَبِير مِنْ دِمَشْق", "الْقَاهِرَة أَكْبَر عَنْ دِمَشْق"], "Comparative + مِنْ."),
        M("Which word means “than” in a comparison?", "مِنْ", ["عَنْ", "مَعَ", "فِي"], "مِنْ = than."),
        M("Does أَكْبَر change for a feminine noun when it is used with مِنْ?", "No", ["Yes, it adds ة", "Yes, it adds ـُون", "Only in the plural"], "With مِنْ, the comparative does not change."),
        M("Which means “The Nile is the longest river in Africa”?", "النِّيل أَطْوَل نَهْر فِي أَفْرِيقِيَا", ["النِّيل طَوِيل نَهْر فِي أَفْرِيقِيَا", "النِّيل أَقْصَر نَهْر فِي أَفْرِيقِيَا", "النَّهْر أَطْوَل نِيل فِي أَفْرِيقِيَا"], "The comparative before a singular noun without ال."),
        F("الْعِرَاق ___ مِنَ السُّعُودِيَّة.", "أَصْغَر", ["أَكْبَر", "أَطْوَل", "أَجْمَل"], "Iraq is smaller.", tr="Iraq is smaller than Saudi Arabia."),
        F("الشِّتَاء ___ مِنَ الْخَرِيف.", "أَبْرَد", ["أَحَرّ", "أَسْهَل", "أَصْغَر"], "Winter is colder.", tr="Winter is colder than autumn."),
    ],
    verify=vw("أَكْبَر", "أَصْغَر", "أَجْمَل", "أَطْوَل", "أَقْصَر", "أَقْرَب", "أَبْعَد", "أَبْرَد", "أَسْهَل", "أَصْعَب", "أَكْثَر",
              "الْفُرَات", "أَفْرِيقِيَا", "الْوَطَن"),
)

# ---------------------------------------------------------------------------- 46
L46 = lesson(
    "Near, far, and how long",
    "قَرِيب مِنْ · بَعِيد عَنْ · نِصْف سَاعَة",
    requires=["بعيد", "قريب", "ساعة", "نصف", "دقيقة", "مطار", "فندق"],
    cards=[
        card("Near and far",
             "Say قَرِيب مِنْ for “near to” and بَعِيد عَنْ for “far from”. The adjective agrees with its noun: "
             "قَرِيبَة and بَعِيدَة for a feminine one.",
             examples=[
                 ex("الْمَطَار بَعِيد عَنِ الْمَدِينَة.", "The airport is far from the city.", "بَعِيد عَنِ"),
                 ex("الْفُنْدُق قَرِيب مِنَ الْمَطَار.", "The hotel is near the airport.", "قَرِيب مِنَ"),
                 ex("مَدْرَسَتِي قَرِيبَة مِنْ بَيْتِي.", "My school is near my house.", "قَرِيبَة مِنْ"),
                 ex("الْجَامِعَة بَعِيدَة عَنْ بَيْتِي.", "The university is far from my house.", "بَعِيدَة عَنْ"),
             ]),
        card("Units of time",
             "To say how long something takes, name the amount of time. “Half” is نِصْف and “a quarter” is رُبْع, "
             "both followed by the unit.",
             tables=[table(["English", "Arabic"],
                           [["minute", "دَقِيقَة"], ["hour", "سَاعَة"], ["half an hour", "نِصْف سَاعَة"],
                            ["a quarter of an hour", "رُبْع سَاعَة"], ["an hour and a half", "سَاعَة وَنِصْف"],
                            ["day", "يَوْم"], ["week", "أُسْبُوع"], ["month", "شَهْر"], ["year", "سَنَة"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("الرِّحْلَة نِصْف سَاعَة.", "The trip is half an hour.", "نِصْف سَاعَة"),
                 ex("كَمْ سَاعَة مِنَ الْقَاهِرَة إِلَى الْإِسْكَنْدَرِيَّة؟", "How many hours is it from Cairo to Alexandria?", "كَمْ سَاعَة"),
             ]),
    ],
    exercises=[
        M("Which means “far from the city”?", "بَعِيد عَنِ الْمَدِينَة", ["قَرِيب مِنَ الْمَدِينَة", "فِي الْمَدِينَة", "إِلَى الْمَدِينَة"], "بَعِيد عَنْ = far from."),
        M("Which means “near the airport”?", "قَرِيب مِنَ الْمَطَار", ["بَعِيد عَنِ الْمَطَار", "فِي الْمَطَار", "مَعَ الْمَطَار"], "قَرِيب مِنْ = near to."),
        M("Which means “half an hour”?", "نِصْف سَاعَة", ["رُبْع سَاعَة", "سَاعَة وَنِصْف", "نِصْف دَقِيقَة"], "نِصْف = half."),
        M("Which means “a quarter of an hour”?", "رُبْع سَاعَة", ["نِصْف سَاعَة", "سَاعَة وَنِصْف", "رُبْع يَوْم"], "رُبْع = a quarter."),
        M("Which means “an hour and a half”?", "سَاعَة وَنِصْف", ["نِصْف سَاعَة", "رُبْع سَاعَة", "دَقِيقَة وَنِصْف"], "سَاعَة + و + نِصْف."),
        M("Which means “The hotel is near the airport”?", "الْفُنْدُق قَرِيب مِنَ الْمَطَار", ["الْفُنْدُق بَعِيد عَنِ الْمَطَار", "الْفُنْدُق فِي الْمَطَار", "الْمَطَار بَعِيد عَنِ الْفُنْدُق"], "قَرِيب مِنَ = near."),
        M("Which means “month”?", "شَهْر", ["سَنَة", "أُسْبُوع", "يَوْم"], "شَهْر = month."),
        F("الْجَامِعَة ___ عَنْ بَيْتِي.", "بَعِيدَة", ["بَعِيد", "قَرِيبَة", "قَرِيب"], "الْجَامِعَة is feminine and the meaning is “far”.", tr="The university is far from my house."),
        F("مَدْرَسَتِي ___ مِنْ بَيْتِي.", "قَرِيبَة", ["قَرِيب", "بَعِيدَة", "بَعِيد"], "مَدْرَسَة is feminine and the meaning is “near”.", tr="My school is near my house."),
        F("الرِّحْلَة نِصْف ___.", "سَاعَة", ["يَوْم", "شَهْر", "سَنَة"], "Half of an hour.", tr="The trip is half an hour."),
    ],
    verify=vw("قَرِيب", "بَعِيد", "قَرِيبَة", "بَعِيدَة", "الْمَطَار", "الْفُنْدُق", "نِصْف", "رُبْع", "دَقِيقَة", "سَاعَة", "يَوْم",
              "أُسْبُوع", "شَهْر", "سَنَة", "الطَّرِيق", "الْإِسْكَنْدَرِيَّة"),
)

# ---------------------------------------------------------------------------- 47
L47 = lesson(
    "A weather report",
    "الطَّقْس فِي الْمُدُن الْعَرَبِيَّة",
    requires=["طقس", "حار", "بارد", "مطر", "درجة", "حرارة"],
    cards=[
        card("A forecast table",
             "A winter forecast for six cities. The temperatures are in degrees Celsius, and the numbers are "
             "written with the Arabic digits from unit 1. The figures are made up for practice.",
             tables=[table(["City", "Weather", "°C", "English"],
                           [["الْقَاهِرَة", "مُشْمِس", "١٩", "Cairo: sunny"], ["بَيْرُوت", "مُمْطِر", "١٤", "Beirut: rainy"],
                            ["عَمَّان", "بَارِد وَمُمْطِر", "٨", "Amman: cold and rainy"], ["الرِّيَاض", "دَافِئ", "٢٤", "Riyadh: warm"],
                            ["بَغْدَاد", "غَائِم", "١٢", "Baghdad: cloudy"], ["الرَّبَاط", "عَاصِف", "١٦", "Rabat: windy"]],
                           say=[0, 1], gloss=False)]),
        card("The same report in sentences",
             "Reports use ordinary sentences. أَعْلَى means “higher” and أَقَلّ means “less, lower”.",
             examples=[
                 ex("الطَّقْس فِي الْقَاهِرَة مُشْمِس.", "The weather in Cairo is sunny."),
                 ex("الْجَوّ فِي عَمَّان بَارِد وَمُمْطِر.", "In Amman it is cold and rainy."),
                 ex("السَّمَاء غَائِمَة فِي بَغْدَاد.", "The sky in Baghdad is cloudy."),
                 ex("دَرَجَة الْحَرَارَة فِي الرِّيَاض أَعْلَى مِنْ عَمَّان.", "The temperature in Riyadh is higher than in Amman.", "أَعْلَى"),
                 ex("دَرَجَة الْحَرَارَة فِي بَغْدَاد أَقَلّ مِنَ الْقَاهِرَة.", "The temperature in Baghdad is lower than in Cairo.", "أَقَلّ"),
             ]),
    ],
    exercises=[
        M("«الْجَوّ فِي عَمَّان بَارِد وَمُمْطِر.» What is the weather in Amman?", "Cold and rainy", ["Hot and dry", "Warm and sunny", "Windy and cloudy"], "بَارِد = cold, مُمْطِر = rainy."),
        M("«الطَّقْس فِي الْقَاهِرَة مُشْمِس.» What is the weather in Cairo?", "Sunny", ["Rainy", "Cloudy", "Windy"], "مُشْمِس = sunny."),
        M("«السَّمَاء غَائِمَة فِي بَغْدَاد.» What is the sky like?", "Cloudy", ["Clear", "Rainy", "Windy"], "غَائِمَة = cloudy."),
        M("الْقَاهِرَة ١٩ · عَمَّان ٨ · الرِّيَاض ٢٤. Which city is the warmest?", "الرِّيَاض", ["الْقَاهِرَة", "عَمَّان", "الرَّبَاط"], "٢٤ is the highest number."),
        M("الْقَاهِرَة ١٩ · عَمَّان ٨ · الرِّيَاض ٢٤. Which city is the coldest?", "عَمَّان", ["الْقَاهِرَة", "الرِّيَاض", "بَيْرُوت"], "٨ is the lowest number."),
        M("What does دَرَجَة الْحَرَارَة mean?", "temperature", ["weather forecast", "hot weather", "cold wind"], "دَرَجَة = degree; حَرَارَة = heat."),
        M("Which means “higher”?", "أَعْلَى", ["أَقَلّ", "أَكْبَر", "أَقْرَب"], "أَعْلَى = higher."),
        F("الْجَوّ فِي الرَّبَاط ___.", "عَاصِف", ["مُشْمِس", "دَافِئ", "جَافّ"], "The report says windy.", tr="The weather in Rabat is windy."),
        F("دَرَجَة الْحَرَارَة فِي الرِّيَاض ___ مِنْ عَمَّان.", "أَعْلَى", ["أَقَلّ", "أَبْعَد", "أَقْصَر"], "٢٤ is more than ٨.", tr="The temperature in Riyadh is higher than in Amman."),
        F("دَرَجَة الْحَرَارَة فِي عَمَّان ___ مِنَ الْقَاهِرَة.", "أَقَلّ", ["أَعْلَى", "أَبْعَد", "أَطْوَل"], "٨ is less than ١٩.", tr="The temperature in Amman is lower than in Cairo."),
    ],
    verify=vw("أَعْلَى", "أَقَلّ", "الْمُدُن", "غَائِمَة", "دَرَجَة", "الْحَرَارَة"),
)

# ---------------------------------------------------------------------------- 48
L48 = lesson(
    "Review: a phone call",
    "Questions, places, languages, weather",
    requires=["هل", "أين", "طقس", "عاصمة", "لغة", "كتب", "ليس", "أكبر"],
    cards=[
        card("Layla in Rabat, Omar in Cairo",
             "Two friends talk on the phone. Read the conversation, then answer the questions.",
             examples=[
                 ex("هَلْ أَنْتَ فِي الْقَاهِرَة يَا عُمَر؟", "Layla: Are you in Cairo, Omar?"),
                 ex("نَعَمْ، أَنَا فِي الْقَاهِرَة. وَأَنْتِ، أَيْنَ أَنْتِ؟", "Omar: Yes, I am in Cairo. And you, where are you?"),
                 ex("أَنَا فِي الرَّبَاط، عَاصِمَة الْمَغْرِب.", "Layla: I am in Rabat, the capital of Morocco."),
                 ex("كَيْفَ الطَّقْس هُنَاك؟", "Omar: How is the weather there?"),
                 ex("الْجَوّ بَارِد وَعَاصِف، لَكِنَّ الْمَدِينَة جَمِيلَة.", "Layla: Cold and windy, but the city is beautiful."),
                 ex("هُنَا الْجَوّ دَافِئ وَمُشْمِس. الْقَاهِرَة أَكْبَر مِنَ الرَّبَاط.", "Omar: Here it is warm and sunny. Cairo is bigger than Rabat."),
                 ex("أَتَكَلَّم الْعَرَبِيَّة وَالْفَرَنْسِيَّة هُنَا.", "Layla: I speak Arabic and French here."),
             ]),
    ],
    exercises=[
        M("Omar answers Layla’s first question with…", "نَعَمْ، أَنَا فِي الْقَاهِرَة", ["لَا، أَنَا فِي الرَّبَاط", "نَعَمْ، هُوَ فِي الْقَاهِرَة", "لَسْتُ فِي الْقَاهِرَة"], "Yes, and the verb-less sentence أَنَا فِي الْقَاهِرَة."),
        M("Which word begins a yes–no question?", "هَلْ", ["كَيْفَ", "مَتَى", "أَيْنَ"], "هَلْ turns a statement into a question."),
        M("How is the weather in Rabat?", "Cold and windy", ["Warm and sunny", "Hot and dry", "Rainy and cloudy"], "بَارِد وَعَاصِف."),
        M("What is the capital of Morocco?", "الرَّبَاط", ["الْقَاهِرَة", "تُونُس", "بَغْدَاد"], "عَاصِمَة الْمَغْرِب الرَّبَاط."),
        M("Which means “Lebanon is west of Syria”?", "لُبْنَان غَرْب سُورِيَا", ["لُبْنَان شَرْق سُورِيَا", "سُورِيَا غَرْب لُبْنَان", "لُبْنَان جَنُوب سُورِيَا"], "غَرْب = west."),
        M("Which means “I speak French a little”?", "أَتَكَلَّم الْفَرَنْسِيَّة قَلِيلًا", ["تَتَكَلَّم الْفَرَنْسِيَّة قَلِيلًا", "أَكْتُب الْفَرَنْسِيَّة قَلِيلًا", "أَتَكَلَّم الْعَرَبِيَّة جَيِّدًا"], "أَتَكَلَّم = I speak."),
        M("Which means “they (women) write”?", "يَكْتُبْنَ", ["يَكْتُبُون", "تَكْتُبْنَ", "تَكْتُبِين"], "يَـ + ـْنَ.", lemma="كتب:pres:hunna"),
        M("Which means “I don’t know”?", "لَا أَعْرِف", ["لَيْسَ أَعْرِف", "لَا نَعْرِف", "لَا يَعْرِف"], "لَا + أَعْرِف."),
        M("Which means “She is not Egyptian”?", "هِيَ لَيْسَتْ مِصْرِيَّةً", ["هِيَ لَا مِصْرِيَّة", "هُوَ لَيْسَ مِصْرِيًّا", "هِيَ لَسْتُ مِصْرِيَّةً"], "لَيْسَتْ + ـَةً."),
        M("Which means “Cairo is bigger than Rabat”?", "الْقَاهِرَة أَكْبَر مِنَ الرَّبَاط", ["الرَّبَاط أَكْبَر مِنَ الْقَاهِرَة", "الْقَاهِرَة كَبِير مِنَ الرَّبَاط", "الْقَاهِرَة أَكْبَر فِي الرَّبَاط"], "أَكْبَر + مِنْ."),
        F("___ الطَّقْس فِي الْقَاهِرَة؟", "كَيْفَ", ["مَنْ", "كَمْ", "هَلْ"], "A question about how things are.", tr="How is the weather in Cairo?"),
        F("أَنَا ___ طَالِبًا.", "لَسْتُ", ["لَا", "لَيْسَتْ", "لَيْسُوا"], "“I am not” = لَسْتُ.", tr="I am not a student."),
    ],
    verify=(vw("أَتَكَلَّم", "الْمَغْرِب", "الرَّبَاط", "هُنَاك", "مِصْرِيًّا", "لَكِنَّ") + vv("كتب", "pres", hunna="يَكْتُبْنَ", hum="يَكْتُبُون")
            + vv("عرف", "pres", ana="أَعْرِف", nahnu="نَعْرِف", huwa="يَعْرِف")),
)

UNIT = unit("الطقس والأماكن: places, weather and the present tense", [L32, L33, L34, L35, L36, L37, L38, L39, L40, L41, L42, L43, L44, L45, L46, L47, L48])
