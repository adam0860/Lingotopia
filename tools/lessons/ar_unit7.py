"""Unit 7: review of the whole course (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 101
L101 = lesson(
    "Review: meeting someone",
    "اِسْمِي سَارَة · أَنَا مِنْ مِصْر · هُوَ مُدَرِّس",
    requires=["من", "طالب", "مدرس", "أنا", "هو", "هي"],
    cards=[
        card("Two people meet",
             "A first conversation uses almost everything from the first two units: greetings, the pronouns, "
             "a noun sentence with no “is”, and مِنْ for where you come from.",
             examples=[
                 ex("السَّلَام عَلَيْكُم.", "Peace be upon you."),
                 ex("وَعَلَيْكُمُ السَّلَام.", "And upon you, peace."),
                 ex("اِسْمِي سَارَة. مَا اِسْمُكَ؟", "My name is Sara. What is your name? (to a man)"),
                 ex("اِسْمِي أَحْمَد. أَنَا مُدَرِّس.", "My name is Ahmad. I am a teacher."),
                 ex("مِنْ أَيْنَ أَنْتِ يَا سَارَة؟", "Where are you from, Sara? (to a woman)"),
                 ex("أَنَا مِنْ مِصْر. هِيَ طَالِبَة وَهُوَ مُدَرِّس.", "I am from Egypt. She is a student and he is a teacher."),
             ]),
    ],
    exercises=[
        M("Which means “My name is Sara”?", "اِسْمِي سَارَة", ["اِسْمُكَ سَارَة", "اِسْمُهَا سَارَة", "أَنَا اِسْمِي"], "ـِي = my."),
        M("Which means “What is your name?” to a man?", "مَا اِسْمُكَ؟", ["مَا اِسْمُكِ؟", "مَنْ اِسْمُكَ؟", "أَيْنَ اِسْمُكَ؟"], "ـكَ for a man."),
        M("Which asks a woman where she is from?", "مِنْ أَيْنَ أَنْتِ؟", ["مِنْ أَيْنَ أَنْتَ؟", "أَيْنَ أَنْتِ مِنْ؟", "مِنْ مَنْ أَنْتِ؟"], "أَنْتِ = you (woman)."),
        M("Which means “She is a student”?", "هِيَ طَالِبَة", ["هُوَ طَالِبَة", "هِيَ طَالِب", "أَنَا طَالِبَة"], "هِيَ + طَالِبَة."),
        M("Which means “He is a teacher”?", "هُوَ مُدَرِّس", ["هِيَ مُدَرِّس", "هُوَ مُدَرِّسَة", "هُوَ هُنَا"], "هُوَ + مُدَرِّس."),
        M("What do you answer to «السَّلَام عَلَيْكُم»?", "وَعَلَيْكُمُ السَّلَام", ["مَعَ السَّلَامَة", "أَهْلًا بِكَ", "شُكْرًا"], "The reply reverses the order."),
        M("Which means “I am from Egypt”?", "أَنَا مِنْ مِصْر", ["أَنَا فِي مِصْر", "أَنَا إِلَى مِصْر", "هُوَ مِنْ مِصْر"], "مِنْ = from."),
        F("___ اِسْمُكَ؟", "مَا", ["هَلْ", "مَنْ", "أَيْنَ"], "What is your name?", tr="What is your name?"),
        F("أَنَا ___ مِصْر.", "مِنْ", ["فِي", "إِلَى", "عَلَى"], "From.", tr="I am from Egypt."),
    ],
    verify=vw("السَّلَام", "عَلَيْكُم", "وَعَلَيْكُم", "اِسْمِي", "اِسْمُكَ", "سَارَة", "أَحْمَد", "مُدَرِّس", "طَالِبَة", "مِصْر", "أَنْتِ"),
)

# ---------------------------------------------------------------------------- 102
L102 = lesson(
    "Review: asking and saying no",
    "هَلْ · مَنْ · مَاذَا · أَيْنَ · لَا · لَيْسَ",
    requires=["هل", "من", "ما", "أين", "لا", "ليس"],
    cards=[
        card("Choosing the right word",
             "Question words go first. هَلْ asks yes or no. لَا negates a present-tense verb, and لَيْسَ negates a "
             "noun sentence.",
             tables=[table(["Word", "Use", "Example"],
                           [["هَلْ", "yes/no question", "هَلْ أَنْتَ طَالِب؟"], ["مَنْ", "who", "مَنْ هَذَا؟"],
                            ["مَا / مَاذَا", "what", "مَاذَا تَدْرُس؟"], ["أَيْنَ", "where", "أَيْنَ الْمَدْرَسَة؟"],
                            ["لَا", "does not (with a verb)", "لَا أَدْرُس الْيَوْم"], ["لَيْسَ", "is not (with a noun)", "هُوَ لَيْسَ طَالِبًا"]],
                           say=[0, 2], tlit=[2], gloss=False)]),
        card("Question and answer",
             "A negative answer picks لَا or لَيْسَ depending on what comes after it.",
             examples=[
                 ex("هَلْ أَنْتَ طَالِب؟", "Are you a student? (to a man)"),
                 ex("لَا، أَنَا لَسْتُ طَالِبًا. أَنَا مُدَرِّس.", "No, I am not a student. I am a teacher."),
                 ex("مَاذَا تَدْرُس؟", "What do you study? (to a man)"),
                 ex("أَدْرُس الْعَرَبِيَّة وَلَا أَدْرُس الْفَرَنْسِيَّة.", "I study Arabic and I do not study French."),
                 ex("أَيْنَ الْمَدْرَسَة؟", "Where is the school?"),
                 ex("الْمَدْرَسَة لَيْسَتْ هُنَا.", "The school is not here."),
             ]),
    ],
    exercises=[
        M("Which word starts a yes/no question?", "هَلْ", ["مَنْ", "لَيْسَ", "لَا"], "هَلْ."),
        M("Which question word means “where”?", "أَيْنَ", ["مَنْ", "كَمْ", "مَاذَا"], "أَيْنَ = where."),
        M("Which question word asks about a person?", "مَنْ", ["أَيْنَ", "مَاذَا", "كَمْ"], "مَنْ = who."),
        M("Which negates «أَدْرُس الْيَوْم»?", "لَا أَدْرُس الْيَوْم", ["لَيْسَ أَدْرُس الْيَوْم", "مَنْ أَدْرُس الْيَوْم", "هَلْ أَدْرُس الْيَوْم"], "A verb takes لَا."),
        M("Which negates «الْمَدْرَسَة هُنَا»?", "الْمَدْرَسَة لَيْسَتْ هُنَا", ["الْمَدْرَسَة لَا هُنَا", "الْمَدْرَسَة لَيْسَ هُنَا", "لَا الْمَدْرَسَة هُنَا"], "مَدْرَسَة is feminine: لَيْسَتْ."),
        M("Which means “I am not a student”?", "أَنَا لَسْتُ طَالِبًا", ["أَنَا لَا طَالِب", "أَنَا لَيْسَ طَالِب", "أَنَا لَسْتَ طَالِبًا"], "لَسْتُ = I am not."),
        M("Which means “What do you study?”", "مَاذَا تَدْرُس؟", ["مَنْ تَدْرُس؟", "أَيْنَ تَدْرُس؟", "هَلْ تَدْرُس؟"], "مَاذَا = what."),
        F("___ أَنْتَ طَالِب؟", "هَلْ", ["مَاذَا", "أَيْنَ", "لَيْسَ"], "Yes/no question.", tr="Are you a student?"),
        F("أَنَا ___ أَدْرُس الْيَوْم.", "لَا", ["لَيْسَ", "هَلْ", "مَنْ"], "Negating a verb.", tr="I do not study today."),
    ],
    verify=(vv("درس", "pres", ana="أَدْرُس", anta="تَدْرُس") + vw("لَسْتُ", "لَيْسَتْ", "هُنَا", "الْعَرَبِيَّة", "الْفَرَنْسِيَّة", "مَاذَا")),
)

# ---------------------------------------------------------------------------- 103
L103 = lesson(
    "Review: places and weather",
    "فِي الشِّتَاء الْجَوّ بَارِد · أَذْهَب إِلَى السُّوق",
    requires=["شتاء", "صيف", "جو", "سوق", "مدينة", "ذهب"],
    cards=[
        card("Describing a day",
             "Weather sentences are noun sentences, and travel sentences use a present verb with إِلَى.",
             examples=[
                 ex("فِي الشِّتَاء الْجَوّ بَارِد.", "In winter the weather is cold."),
                 ex("فِي الصَّيْف الْجَوّ حَارّ.", "In summer the weather is hot."),
                 ex("أُحِبّ الرَّبِيع لِأَنَّ الْجَوّ جَمِيل.", "I like spring because the weather is nice."),
                 ex("أَذْهَب إِلَى السُّوق كُلّ يَوْم.", "I go to the market every day."),
                 ex("الْمَدِينَة كَبِيرَة، وَالْجَبَل بَعِيد.", "The city is big, and the mountain is far."),
             ]),
    ],
    exercises=[
        M("Which means “In winter the weather is cold”?", "فِي الشِّتَاء الْجَوّ بَارِد", ["فِي الصَّيْف الْجَوّ بَارِد", "فِي الشِّتَاء الْجَوّ حَارّ", "فِي الشِّتَاء الْجَوّ بَارِدَة"], "شِتَاء = winter."),
        M("Which means “In summer the weather is hot”?", "فِي الصَّيْف الْجَوّ حَارّ", ["فِي الشِّتَاء الْجَوّ حَارّ", "فِي الصَّيْف الْجَوّ بَارِد", "فِي الرَّبِيع الْجَوّ حَارّ"], "صَيْف = summer."),
        M("Which means “I go to the market every day”?", "أَذْهَب إِلَى السُّوق كُلّ يَوْم", ["أَذْهَب مِنَ السُّوق كُلّ يَوْم", "تَذْهَب إِلَى السُّوق كُلّ يَوْم", "أَذْهَب إِلَى السُّوق كُلّ شَهْر"], "إِلَى = to."),
        M("Which means “The mountain is far”?", "الْجَبَل بَعِيد", ["الْجَبَل قَرِيب", "الْجَبَل بَعِيدَة", "الْمَدِينَة بَعِيد"], "بَعِيد = far."),
        M("Which means “The city is big”?", "الْمَدِينَة كَبِيرَة", ["الْمَدِينَة كَبِير", "الْمَدِينَة صَغِيرَة", "الْمَدِينَة الْكَبِيرَة"], "مَدِينَة is feminine."),
        M("Why does the adjective in «الْجَوّ بَارِد» have no ة?", "الْجَوّ is masculine", ["it is plural", "it is a verb", "it is definite"], "Agreement in gender."),
        F("فِي الصَّيْف الْجَوّ ___ .", "حَارّ", ["بَارِد", "حَارَّة", "بَعِيد"], "Summer.", tr="In summer the weather is hot."),
        F("أَذْهَب ___ السُّوق.", "إِلَى", ["مِنْ", "عَنْ", "مَعَ"], "To.", tr="I go to the market."),
    ],
    verify=(vv("ذهب", "pres", ana="أَذْهَب") + vw("الشِّتَاء", "الصَّيْف", "الرَّبِيع", "جَمِيل", "حَارّ", "بَعِيد", "لِأَنَّ", "كُلّ")),
)

# ---------------------------------------------------------------------------- 104
L104 = lesson(
    "Review: plurals, agreement and the family",
    "طُلَّاب · طَالِبَات · كِتَاب كَبِير · أَبِي وَأُمِّي",
    requires=["طالب", "كتاب", "أب", "أم", "كبير", "معلم"],
    cards=[
        card("Number and gender",
             "A noun can be singular, dual or plural. An adjective after a noun matches its gender and its "
             "definiteness (a plural of things takes a feminine singular adjective). A sound plural adds an ending; a broken plural changes the inside of the word.",
             tables=[table(["English", "Singular", "Plural"],
                           [["student (m)", "طَالِب", "طُلَّاب"], ["student (f)", "طَالِبَة", "طَالِبَات"],
                            ["teacher (m)", "مُدَرِّس", "مُدَرِّسُون"], ["book", "كِتَاب", "كُتُب"],
                            ["room", "غُرْفَة", "غُرَف"]],
                           say=[1, 2], tlit=[1, 2])]),
        card("Family and agreement",
             "Add ـِي to say “my”: أَبِي, أُمِّي. The adjective follows the noun and matches it.",
             examples=[
                 ex("أَبِي مُدَرِّس وَأُمِّي طَالِبَة.", "My father is a teacher and my mother is a student."),
                 ex("عِنْدِي كِتَاب كَبِير.", "I have a big book."),
                 ex("عِنْدَهَا كُتُب كَبِيرَة.", "She has big books."),
                 ex("هَذَا هُوَ الْبَيْت الْكَبِير.", "This is the big house."),
                 ex("الطَّالِبَان فِي الْمَدْرَسَة.", "The two (male) students are at school."),
             ]),
    ],
    exercises=[
        M("What is the plural of كِتَاب?", "كُتُب", ["كِتَابَات", "كِتَابُون", "كُتُبَان"], "Broken plural."),
        M("What is the plural of طَالِبَة?", "طَالِبَات", ["طُلَّاب", "طَالِبُون", "طَالِبَتَان"], "Sound feminine plural."),
        M("Which means “two students (m)”?", "طَالِبَان", ["طُلَّاب", "طَالِبَات", "طَالِبَتَان"], "Dual."),
        M("Which means “my father”?", "أَبِي", ["أَبُوكَ", "أَبُوهَا", "أَبُونَا"], "ـِي = my."),
        M("Which means “I have a big book”?", "عِنْدِي كِتَاب كَبِير", ["عِنْدِي كِتَاب كَبِيرَة", "عِنْدِي كُتُب كَبِير", "عِنْدَهَا كِتَاب كَبِير"], "كِتَاب is masculine."),
        M("Which means “She has big books”?", "عِنْدَهَا كُتُب كَبِيرَة", ["عِنْدَهَا كُتُب كَبِير", "عِنْدَهُ كُتُب كَبِيرَة", "عِنْدَهَا كِتَاب كَبِير"], "A plural of a thing agrees as feminine singular."),
        M("Which means “the big house”?", "الْبَيْت الْكَبِير", ["الْبَيْت كَبِير", "بَيْت الْكَبِير", "الْبَيْت كَبِيرَة"], "Both words take ال."),
        F("أَبِي مُدَرِّس وَ___ طَالِبَة.", "أُمِّي", ["أَخِي", "أَبِي", "أُخْتُهُ"], "My mother.", tr="My father is a teacher and my mother is a student."),
        F("عِنْدَهَا ___ كَبِيرَة.", "كُتُب", ["كِتَاب", "كُتُبَان", "طَالِب"], "Plural noun.", tr="She has big books."),
    ],
    verify=(vps("مُدَرِّس", "مُدَرِّسُون") + vps("طَالِبَة", "طَالِبَات") + vpb("كِتَاب", "كُتُب") + vpb("طَالِب", "طُلَّاب") + vpb("غُرْفَة", "غُرَف")
            + vd("طَالِب", "طَالِبَان", "طَالِبَيْن") + vf("كَبِير", "كَبِيرَة") + vw("أَبِي", "أُمِّي", "أَخِي", "الطَّالِبَان", "الْكَبِير")),
)

# ---------------------------------------------------------------------------- 105
L105 = lesson(
    "Review: numbers, the iḍāfa and the house",
    "ثَلَاث غُرَف · بَاب الْبَيْت · كَمْ غُرْفَة؟",
    requires=["بيت", "غرفة", "باب", "كم", "عشرة", "واحد"],
    cards=[
        card("Counting and joining nouns",
             "Numbers 3 to 10 take the form with the opposite gender from the noun, and the noun after them is plural. "
             "Two nouns side by side, the first with no ال, can make an iḍāfa; the second may have ال.",
             examples=[
                 ex("فِي الْبَيْت ثَلَاث غُرَف.", "There are three rooms in the house."),
                 ex("عِنْدِي خَمْسَة كُتُب.", "I have five books."),
                 ex("بَاب الْبَيْت كَبِير.", "The door of the house is big."),
                 ex("مِفْتَاح الْغُرْفَة عَلَى الطَّاوِلَة.", "The key of the room is on the table."),
                 ex("كَمْ غُرْفَة عِنْدَكُم؟", "How many rooms do you have?"),
                 ex("عِنْدَنَا غُرْفَتَان وَمَطْبَخ.", "We have two rooms and a kitchen."),
             ]),
    ],
    exercises=[
        M("Which means “three rooms”?", "ثَلَاث غُرَف", ["ثَلَاثَة غُرَف", "ثَلَاث غُرْفَة", "ثَلَاثَة غُرْفَة"], "غُرْفَة is feminine, so the number has no ة."),
        M("Which means “five books”?", "خَمْسَة كُتُب", ["خَمْس كُتُب", "خَمْسَة كِتَاب", "خَمْس كِتَاب"], "كِتَاب is masculine, so the number ends in ة."),
        M("Which means “two rooms”?", "غُرْفَتَان", ["غُرَف", "ثَلَاث غُرَف", "غُرْفَة"], "Dual."),
        M("Which means “the door of the house”?", "بَاب الْبَيْت", ["الْبَاب الْبَيْت", "بَاب بَيْت الْ", "بَيْت الْبَاب"], "The first noun has no ال."),
        M("Which question asks “How many rooms?”", "كَمْ غُرْفَة؟", ["كَمْ غُرَف؟", "أَيْنَ غُرْفَة؟", "هَلْ غُرْفَة؟"], "كَمْ + singular."),
        M("Which means “The key of the room is on the table”?", "مِفْتَاح الْغُرْفَة عَلَى الطَّاوِلَة", ["الْمِفْتَاح الْغُرْفَة عَلَى الطَّاوِلَة", "مِفْتَاح الْغُرْفَة فِي الطَّاوِلَة", "الْغُرْفَة مِفْتَاح عَلَى الطَّاوِلَة"], "iḍāfa + عَلَى."),
        F("فِي الْبَيْت ___ غُرَف.", "ثَلَاث", ["ثَلَاثَة", "ثَلَاثُون", "ثَلَاثَة عَشَر"], "Feminine noun, so no ة.", tr="There are three rooms in the house."),
        F("بَاب ___ كَبِير.", "الْبَيْت", ["بَيْت", "الْبَيْتَان", "بَيْتِي الْ"], "Second noun of the iḍāfa.", tr="The door of the house is big."),
    ],
    verify=(vn(3, "f", "ثَلَاث") + vn(5, "m", "خَمْسَة") + vd("غُرْفَة", "غُرْفَتَان", "غُرْفَتَيْن") + vpb("غُرْفَة", "غُرَف") + vpb("كِتَاب", "كُتُب")
            + vw("مِفْتَاح", "مَطْبَخ", "الطَّاوِلَة")),
)

# ---------------------------------------------------------------------------- 106
L106 = lesson(
    "A day with Sara",
    "تَسْكُن سَارَة فِي الْقَاهِرَة · هِيَ طَالِبَة",
    requires=["سكن", "درس", "مدرسة", "بيت", "يوم", "عمل"],
    cards=[
        card("A short text",
             "Read the whole text first, then answer the questions at the end.",
             examples=[
                 ex("اِسْمِي سَارَة. أَنَا طَالِبَة وَأَسْكُن فِي الْقَاهِرَة.", "My name is Sara. I am a student and I live in Cairo."),
                 ex("عِنْدِي أَخ وَأُخْت. أَبِي مُدَرِّس وَأُمِّي تَعْمَل فِي مَطْعَم.", "I have a brother and a sister. My father is a teacher and my mother works in a restaurant."),
                 ex("فِي الصَّبَاح أَشْرَب الشَّايْ وَآكُل الْخُبْز وَالْجُبْن.", "In the morning I drink tea and eat bread and cheese."),
                 ex("ثُمَّ أَذْهَب إِلَى الْمَدْرَسَة.", "Then I go to school."),
                 ex("بَعْد الْمَدْرَسَة يَجِب أَنْ أَكْتُب الْوَاجِب.", "After school I must write my homework."),
                 ex("فِي الْمَسَاء نَأْكُل الْعَشَاء فِي الْبَيْت، وَأَغْسِل الصُّحُون.", "In the evening we eat dinner at home, and I wash the dishes."),
             ]),
    ],
    exercises=[
        M("«أَنَا طَالِبَة وَأَسْكُن فِي الْقَاهِرَة». Where does Sara live?", "in Cairo", ["in Amman", "at school", "in a restaurant"], "أَسْكُن فِي = I live in."),
        M("«أَبِي مُدَرِّس وَأُمِّي تَعْمَل فِي مَطْعَم». What does her mother do?", "works in a restaurant", ["is a teacher", "is a student", "cooks at home"], "تَعْمَل فِي."),
        M("«أَشْرَب الشَّايْ وَآكُل الْخُبْز وَالْجُبْن». What does she have for breakfast?", "tea, bread and cheese", ["coffee and eggs", "juice and fish", "milk and rice"], "الشَّايْ، الْخُبْز، الْجُبْن."),
        M("«ثُمَّ أَذْهَب إِلَى الْمَدْرَسَة». What does she do next?", "goes to school", ["washes the dishes", "writes a letter", "goes to the market"], "إِلَى الْمَدْرَسَة."),
        M("«يَجِب أَنْ أَكْتُب الْوَاجِب». What must she do after school?", "write her homework", ["cook dinner", "wash the dishes", "open the window"], "يَجِب أَنْ = I must."),
        M("«نَأْكُل الْعَشَاء فِي الْبَيْت». Who eats dinner?", "Sara and her family", ["only Sara", "only her mother", "her teacher"], "نَـ = we."),
        M("Which of these does Sara NOT say?", "I have two brothers", ["I live in Cairo", "I am a student", "I wash the dishes"], "She has one brother and one sister."),
        F("فِي الصَّبَاح أَشْرَب ___ .", "الشَّايْ", ["الْعَشَاء", "الْمَدْرَسَة", "الْوَاجِب"], "A drink.", tr="In the morning I drink tea."),
        F("بَعْد الْمَدْرَسَة يَجِب أَنْ ___ الْوَاجِب.", "أَكْتُب", ["يَكْتُب", "كَتَبَ", "اُكْتُبْ"], "I write.", tr="After school I must write my homework."),
    ],
    verify=(vv("سكن", "pres", ana="أَسْكُن", hiya="تَسْكُن") + vv("ذهب", "pres", ana="أَذْهَب") + vv("كتب", "pres", ana="أَكْتُب")
            + vv("غسل", "pres", ana="أَغْسِل") + vv("شرب", "pres", ana="أَشْرَب") + vw("الْقَاهِرَة", "ثُمَّ", "الْمَسَاء", "تَعْمَل", "مَطْعَم")),
)

UNIT = unit("المراجعة: review of the whole course", [L101, L102, L103, L104, L105, L106])
