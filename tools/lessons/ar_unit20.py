"""Unit 20 (chapter 18): defective verbs, Measures VIII and X, customs, holidays, dress, peoples and weddings."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 294
L294 = lesson(
    "Defective verbs: three families",
    "مَشَى ← يَمْشِي · دَعَا ← يَدْعُو · نَسِيَ ← يَنْسَى",
    requires=["مشى", "بنى", "دعا", "نسي", "بقي", "لقي", "سعى", "رمى", "جرى", "فعل"],
    cards=[
        card("A weak letter at the end",
             "Verbs whose last root letter is weak (و or ي) are called defective. In the past they end in ـَى, ـَا or ـِيَ: مَشَى, دَعَا, نَسِيَ. A few family 3 verbs, such as سَعَى, end in ـَى in the past, like family 1, so always learn a verb together with its present form. "
             "To find the present, you need to know the family. There are three main families, and you learn each verb with its present form.",
             tables=[table(["Family", "Past (he)", "Present (he)", "English"],
                           [["1", "مَشَى", "يَمْشِي", "walks"], ["1", "بَنَى", "يَبْنِي", "builds"], ["1", "رَمَى", "يَرْمِي", "throws"],
                            ["2", "دَعَا", "يَدْعُو", "calls, invites"], ["2", "شَكَا", "يَشْكُو", "complains"],
                            ["3", "نَسِيَ", "يَنْسَى", "forgets"], ["3", "بَقِيَ", "يَبْقَى", "stays"], ["3", "لَقِيَ", "يَلْقَى", "meets"], ["3", "سَعَى", "يَسْعَى", "strives"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("Reading the family from the present",
             "Family 1 ends in ـِي in the present, family 2 in ـُو, family 3 in ـَى. The vowel before the last letter matches: kasra, ḍamma, fatḥa.",
             examples=[
                 ex("يَمْشِي أَخِي إِلَى الْمَدْرَسَة.", "My brother walks to school.", "يَمْشِي"),
                 ex("بَنَى جَدِّي بَيْتًا كَبِيرًا.", "My grandfather built a big house.", "بَنَى"),
                 ex("يَدْعُو صَدِيقِي أَهْلَهُ إِلَى الْحَفْلَة.", "My friend invites his family to the party.", "يَدْعُو"),
                 ex("نَسِيَ الرَّاكِب حَقِيبَتَهُ.", "The passenger forgot his bag.", "نَسِيَ"),
                 ex("يَبْقَى الْوَلَد فِي الْبَيْت.", "The boy stays at home.", "يَبْقَى"),
                 ex("لَقِيَ الْمُهَنْدِس صَدِيقًا قَدِيمًا.", "The engineer met an old friend.", "لَقِيَ"),
             ]),
    ],
    exercises=[
        M("Which is the present of مَشَى?", "يَمْشِي", ["مَشِيَ"], "Family 1: ـِي."),
        M("Which is the present of دَعَا?", "يَدْعُو", ["دَعِيَ"], "Family 2: ـُو."),
        M("Which is the present of نَسِيَ?", "يَنْسَى", ["نَسَا"], "Family 3: ـَى."),
        M("Which is the present of بَنَى?", "يَبْنِي", ["بَنِيَ"], "Same family as مَشَى."),
        M("What does بَنَى جَدِّي بَيْتًا كَبِيرًا mean?", "My grandfather built a big house", ["My grandfather sold a big house", "My grandfather forgot a big house", "My grandfather walked to a big house"], "بَنَى = built."),
        M("What does يَبْقَى الْوَلَد فِي الْبَيْت mean?", "The boy stays at home", ["The boy leaves home", "The boy forgets the house", "The boy builds a house"], "يَبْقَى = stays."),
        F("___ أَخِي إِلَى الْمَدْرَسَة.", "يَمْشِي", ["مَشَتْ"], "Present, family 1.", tr="My brother walks to school.", lemma="مشي:pres:huwa"),
        F("___ صَدِيقِي أَهْلَهُ إِلَى الْحَفْلَة.", "يَدْعُو", ["دَعَا"], "Present, family 2.", tr="My friend invites his family to the party.", lemma="دعو:pres:huwa"),
        F("___ الْوَلَد فِي الْبَيْت.", "يَبْقَى", ["بَقِيَ"], "Present, family 3.", tr="The boy stays at home.", lemma="بقي:pres:huwa"),
    ],
    verify=(vv("مشي", "past", huwa="مَشَى") + vv("مشي", "pres", huwa="يَمْشِي") + vv("بني", "past", huwa="بَنَى") + vv("بني", "pres", huwa="يَبْنِي")
            + vv("رمي", "past", huwa="رَمَى") + vv("رمي", "pres", huwa="يَرْمِي") + vv("دعو", "past", huwa="دَعَا") + vv("دعو", "pres", huwa="يَدْعُو")
            + vv("شكو", "past", huwa="شَكَا") + vv("شكو", "pres", huwa="يَشْكُو") + vv("نسي", "past", huwa="نَسِيَ") + vv("نسي", "pres", huwa="يَنْسَى")
            + vv("بقي", "past", huwa="بَقِيَ") + vv("بقي", "pres", huwa="يَبْقَى") + vv("لقي", "past", huwa="لَقِيَ") + vv("لقي", "pres", huwa="يَلْقَى")
            + vv("سعي", "past", huwa="سَعَى") + vv("سعي", "pres", huwa="يَسْعَى")
            + vw("أَهْلَهُ", "الْحَفْلَة", "حَقِيبَتَهُ", "قَدِيمًا", "بَيْتًا", "كَبِيرًا", "الْوَلَد", "الْمَدْرَسَة", "صَدِيقًا")),
)

# ---------------------------------------------------------------------------- 295
L295 = lesson(
    "The past of مَشَى: every person",
    "مَشَى · مَشَتْ · مَشَيْتُ · مَشَوْا",
    requires=["مشى", "محطة", "مدرسة", "بيت", "صباح", "أنا", "هو", "هي", "نحن", "هم"],
    cards=[
        card("What happens to the last letter",
             "In مَشَى the last letter is a long ā written ى. Before the endings it changes: it disappears before تْ (مَشَتْ), becomes ي before an ending that starts with a consonant (مَشَيْتُ), and becomes و before the plural ـوا (مَشَوْا). "
             "The two-person forms keep the ي: مَشَيَا.",
             tables=[table(["Pronoun", "Past of مَشَى", "English"],
                           [["هُوَ", "مَشَى", "he walked"], ["هِيَ", "مَشَتْ", "she walked"], ["هُمَا", "مَشَيَا", "they two (m.) walked"], ["هُمْ", "مَشَوْا", "they walked"], ["هُنَّ", "مَشَيْنَ", "they (f.) walked"],
                            ["أَنَا", "مَشَيْتُ", "I walked"], ["أَنْتَ", "مَشَيْتَ", "you walked (m.)"], ["أَنْتِ", "مَشَيْتِ", "you walked (f.)"], ["نَحْنُ", "مَشَيْنَا", "we walked"], ["أَنْتُمْ", "مَشَيْتُمْ", "you walked (pl.)"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "The same changes happen with every verb of family 1, such as بَنَى and رَمَى.",
             examples=[
                 ex("مَشَيْتُ إِلَى الْمَحَطَّة فِي الصَّبَاح.", "I walked to the station in the morning.", "مَشَيْتُ"),
                 ex("مَشَتِ الْبِنْت إِلَى الْمَدْرَسَة.", "The girl walked to school.", "مَشَتِ"),
                 ex("مَشَوْا إِلَى الْبَيْت مَعًا.", "They walked home together.", "مَشَوْا"),
                 ex("مَشَيْنَا فِي الْحَدِيقَة سَاعَة.", "We walked in the park for an hour.", "مَشَيْنَا"),
                 ex("بَنَيْتُ بَيْتًا صَغِيرًا.", "I built a small house.", "بَنَيْتُ"),
                 ex("بَنَوْا مَسْجِدًا جَدِيدًا.", "They built a new mosque.", "بَنَوْا"),
             ]),
    ],
    exercises=[
        M("Which means “I walked”?", "مَشَيْتُ", ["مَشَى", "مَشَتْ", "مَشَوْا"], "The ى becomes ي before تُ."),
        M("Which means “she walked”?", "مَشَتْ", ["مَشَى", "مَشَيْتِ", "مَشَيْنَ"], "The ى disappears before تْ."),
        M("Which means “they walked” (men)?", "مَشَوْا", ["مَشَيْنَ", "مَشَى", "مَشَيَا"], "The ى becomes و."),
        M("Which means “we walked”?", "مَشَيْنَا", ["مَشَيْتُ", "مَشَوْا", "مَشَتْ"], "ـنَا = we."),
        M("Which means “I built”?", "بَنَيْتُ", ["بَنَى", "بَنَوْا", "بَنَتْ"], "Same changes as مَشَى."),
        M("What does مَشَوْا إِلَى الْبَيْت مَعًا mean?", "They walked home together", ["They built a house together", "He walked home alone", "We will walk home"], "مَشَوْا = they walked."),
        F("أَنَا ___ إِلَى الْمَحَطَّة فِي الصَّبَاح.", "مَشَيْتُ", ["مَشَى", "مَشَتْ", "مَشَوْا"], "I walked.", tr="I walked to the station in the morning.", lemma="مشي:past:ana"),
        F("هُمْ ___ إِلَى الْبَيْت مَعًا.", "مَشَوْا", ["مَشَيْنَ", "مَشَيَا", "مَشَتْ"], "They (men) walked.", tr="They walked home together.", lemma="مشي:past:hum"),
        F("نَحْنُ ___ فِي الْحَدِيقَة سَاعَة.", "مَشَيْنَا", ["مَشَيْتُ", "مَشَوْا", "مَشَى"], "We walked.", tr="We walked in the park for an hour.", lemma="مشي:past:nahnu"),
    ],
    verify=(vv("مشي", "past", huwa="مَشَى", hiya="مَشَتْ", huma_m="مَشَيَا", huma_f="مَشَتَا", hum="مَشَوْا", hunna="مَشَيْنَ", ana="مَشَيْتُ", anta="مَشَيْتَ", anti="مَشَيْتِ", nahnu="مَشَيْنَا", antum="مَشَيْتُمْ")
            + vv("بني", "past", ana="بَنَيْتُ", hum="بَنَوْا")
            + vw("الْمَحَطَّة", "الْبِنْت", "الْحَدِيقَة", "مَعًا", "مَشَتِ", "بَيْتًا", "صَغِيرًا", "مَسْجِدًا", "جَدِيدًا")),
)

# ---------------------------------------------------------------------------- 296
L296 = lesson(
    "The past of دَعَا and نَسِيَ",
    "دَعَوْتُ · دَعَوْا · نَسِيتُ · نَسُوا",
    requires=["دعا", "نسي", "ضيف", "حفلة", "أنا", "هو", "هم"],
    cards=[
        card("Two more patterns",
             "Family 2 (دَعَا) keeps a و where family 1 had ي: دَعَوْتُ, دَعَوْا. Family 3 verbs like نَسِيَ end in ـِيَ, and the ي stays long before the endings: نَسِيتُ (a few, like سَعَى, behave like family 1 in the past). "
             "Only the plural he-form is special: نَسُوا, with a ḍamma.",
             tables=[table(["Pronoun", "دَعَا (invite)", "نَسِيَ (forget)"],
                           [["هُوَ", "دَعَا", "نَسِيَ"], ["هِيَ", "دَعَتْ", "نَسِيَتْ"], ["هُمْ", "دَعَوْا", "نَسُوا"], ["هُنَّ", "دَعَوْنَ", "نَسِينَ"], ["أَنَا", "دَعَوْتُ", "نَسِيتُ"], ["أَنْتَ", "دَعَوْتَ", "نَسِيتَ"],
                            ["أَنْتِ", "دَعَوْتِ", "نَسِيتِ"], ["نَحْنُ", "دَعَوْنَا", "نَسِينَا"], ["أَنْتُمْ", "دَعَوْتُمْ", "نَسِيتُمْ"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "Notice that the doer of دَعَا can be followed by a pronoun ending: دَعَانِي means “he invited me”.",
             examples=[
                 ex("دَعَوْتُ أَصْدِقَائِي إِلَى الْحَفْلَة.", "I invited my friends to the party.", "دَعَوْتُ"),
                 ex("دَعَتْنِي صَدِيقَتِي إِلَى بَيْتِهَا.", "My friend invited me to her home.", "دَعَتْنِي"),
                 ex("دَعَوْنَا الضُّيُوف إِلَى الْعَشَاء.", "We invited the guests to dinner.", "دَعَوْنَا"),
                 ex("نَسِيتُ اِسْمَهُ.", "I forgot his name.", "نَسِيتُ"),
                 ex("نَسُوا الْمَوْعِد.", "They forgot the appointment.", "نَسُوا"),
                 ex("نَسِينَا الْحَقَائِب فِي بَيْتِي.", "We forgot the bags at my house.", "نَسِينَا"),
             ]),
    ],
    exercises=[
        M("Which means “I invited”?", "دَعَوْتُ", ["دَعَا", "دَعَوْا"], "Family 2 keeps the و."),
        M("Which means “they invited” (men)?", "دَعَوْا", ["دَعَتْ", "دَعَوْتُ"], "ـَوْا."),
        M("Which means “I forgot”?", "نَسِيتُ", ["نَسِيَ", "نَسُوا", "نَسِيَتْ"], "ـتُ = I."),
        M("Which means “they forgot” (men)?", "نَسُوا", ["نَسِيَ", "نَسِينَ", "نَسِيتُمْ"], "A ḍamma before the ـوا."),
        M("What does دَعَتْنِي صَدِيقَتِي إِلَى بَيْتِهَا mean?", "My friend invited me to her home", ["I invited my friend to her home", "My friend forgot me", "My friend built a home"], "دَعَتْنِي = she invited me."),
        M("What does نَسِينَا الْحَقَائِب فِي بَيْتِي mean?", "We forgot the bags at my house", ["We carried the bags to the car", "We invited the bags", "I forgot the car"], "نَسِينَا = we forgot."),
        F("___ أَصْدِقَائِي إِلَى الْحَفْلَة.", "دَعَوْتُ", ["دَعَا", "دَعَتْ", "دَعَوْا"], "I invited.", tr="I invited my friends to the party.", lemma="دعو:past:ana"),
        F("___ اِسْمَهُ.", "نَسِيتُ", ["نَسِيَ", "نَسُوا", "نَسِينَا"], "I forgot.", tr="I forgot his name.", lemma="نسي:past:ana"),
        F("هُمْ ___ الْمَوْعِد.", "نَسُوا", ["نَسِيَ", "نَسِيتُ", "نَسِينَ"], "They (men) forgot.", tr="They forgot the appointment.", lemma="نسي:past:hum"),
    ],
    verify=(vv("دعو", "past", huwa="دَعَا", hiya="دَعَتْ", hum="دَعَوْا", hunna="دَعَوْنَ", ana="دَعَوْتُ", anta="دَعَوْتَ", anti="دَعَوْتِ", nahnu="دَعَوْنَا", antum="دَعَوْتُمْ")
            + vv("نسي", "past", huwa="نَسِيَ", hiya="نَسِيَتْ", hum="نَسُوا", hunna="نَسِينَ", ana="نَسِيتُ", anta="نَسِيتَ", anti="نَسِيتِ", nahnu="نَسِينَا", antum="نَسِيتُمْ")
            + vw("دَعَانِي", "دَعَتْنِي", "أَصْدِقَائِي", "صَدِيقَتِي", "بَيْتِهَا", "الضُّيُوف", "الْعَشَاء", "اِسْمَهُ", "الْمَوْعِد", "السَّيَّارَة", "الْحَقَائِب")),
)

# ---------------------------------------------------------------------------- 297
L297 = lesson(
    "The present of يَمْشِي: every person",
    "أَمْشِي · تَمْشِين · تَمْشُون · يَمْشُون",
    requires=["مشى", "بنى", "رمى", "مدرسة", "أنا", "أنت", "هو", "هي", "نحن", "هم"],
    cards=[
        card("Prefixes as usual, endings with a twist",
             "The prefixes are the usual أَ تَ يَ نَ. The last letter ي stays in the singular forms: أَمْشِي, تَمْشِي, يَمْشِي. For they-men and you-men the ي turns into the plural ـُون: يَمْشُون. "
             "For you-woman and the two feminine plurals the ending is ـِين: تَمْشِين. Notice that أَنْتِ and أَنْتُنَّ have the same form.",
             tables=[table(["Pronoun", "Present of مَشَى", "English"],
                           [["أَنَا", "أَمْشِي", "I walk"], ["أَنْتَ", "تَمْشِي", "you walk (m.)"], ["أَنْتِ", "تَمْشِين", "you walk (f.)"], ["هُوَ", "يَمْشِي", "he walks"], ["هِيَ", "تَمْشِي", "she walks"], ["أَنْتُنَّ", "تَمْشِين", "you walk (f. pl.)"],
                            ["نَحْنُ", "نَمْشِي", "we walk"], ["هُمَا", "يَمْشِيَان", "they two (m.) walk"], ["أَنْتُمْ", "تَمْشُون", "you walk (pl.)"], ["هُمْ", "يَمْشُون", "they walk"], ["هُنَّ", "يَمْشِين", "they (f.) walk"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Family 1 verbs such as يَبْنِي and يَرْمِي follow exactly the same pattern.",
             examples=[
                 ex("أَمْشِي إِلَى الْعَمَل كُلّ يَوْم.", "I walk to work every day.", "أَمْشِي"),
                 ex("هَلْ تَمْشِين إِلَى الْمَدْرَسَة؟", "Do you walk to school? (to a woman)", "تَمْشِين"),
                 ex("نَمْشِي فِي الْمَسَاء بَعْد الْعَشَاء.", "We walk in the evening after dinner.", "نَمْشِي"),
                 ex("يَمْشُون إِلَى الْمَسْجِد مَعًا.", "They walk to the mosque together.", "يَمْشُون"),
                 ex("يَبْنِي الْعُمَّال بَيْتًا جَدِيدًا.", "The workers are building a new house.", "يَبْنِي"),
                 ex("يَرْمِي الْوَلَد الْكُرَة.", "The boy throws the ball.", "يَرْمِي"),
             ]),
    ],
    exercises=[
        M("Which means “I walk”?", "أَمْشِي", ["تَمْشِي", "يَمْشِي", "نَمْشِي"], "أَ = I."),
        M("Which means “you walk” (to a woman)?", "تَمْشِين", ["تَمْشِي", "تَمْشُون", "أَمْشِي"], "ـِين = to a woman."),
        M("Which means “they walk” (men)?", "يَمْشُون", ["يَمْشِين", "يَمْشِي", "تَمْشِين"], "ـُون = men."),
        M("Which means “we walk”?", "نَمْشِي", ["أَمْشِي", "تَمْشُون", "يَمْشِي"], "نـ = we."),
        M("What does هَلْ تَمْشِين إِلَى الْمَدْرَسَة؟ ask?", "Do you (a woman) walk to school?", ["Do they walk to school?", "Did she walk to school?", "Will you walk to school?"], "تَمْشِين = you (f.) walk."),
        M("Which two pronouns share the form تَمْشِين?", "أَنْتِ and أَنْتُنَّ", ["أَنَا and نَحْنُ", "هُوَ and هُمْ", "أَنْتَ and أَنْتُمْ"], "Both end in ـِين."),
        F("أَنَا ___ إِلَى الْعَمَل كُلّ يَوْم.", "أَمْشِي", ["تَمْشِي", "يَمْشِي", "نَمْشِي"], "I walk.", tr="I walk to work every day.", lemma="مشي:pres:ana"),
        F("هُمْ ___ إِلَى الْمَسْجِد مَعًا.", "يَمْشُون", ["يَمْشِين", "يَمْشِي", "تَمْشِي"], "They (men) walk.", tr="They walk to the mosque together.", lemma="مشي:pres:hum"),
        F("نَحْنُ ___ فِي الْمَسَاء بَعْد الْعَشَاء.", "نَمْشِي", ["أَمْشِي", "يَمْشُون", "تَمْشِين"], "We walk.", tr="We walk in the evening after dinner.", lemma="مشي:pres:nahnu"),
    ],
    verify=(vv("مشي", "pres", ana="أَمْشِي", anta="تَمْشِي", anti="تَمْشِين", huwa="يَمْشِي", hiya="تَمْشِي", nahnu="نَمْشِي", huma_m="يَمْشِيَان", antum="تَمْشُون", hum="يَمْشُون", hunna="يَمْشِين", antunna="تَمْشِين")
            + vv("بني", "pres", huwa="يَبْنِي") + vv("رمي", "pres", huwa="يَرْمِي")
            + vw("الْعَمَل", "الْعَشَاء", "الْمَسَاء", "الْعُمَّال", "الْكُرَة", "الْوَلَد", "الْمَسْجِد", "جَدِيدًا", "مَعًا", "أَنْتُنَّ")),
)

# ---------------------------------------------------------------------------- 298
L298 = lesson(
    "The present of يَدْعُو and يَنْسَى",
    "أَدْعُو · تَدْعِين · يَنْسَوْن · يَنْسَيْن",
    requires=["دعا", "نسي", "ضيف", "أهل", "أنا", "أنت", "هو", "هم", "هن"],
    cards=[
        card("Families 2 and 3 side by side",
             "Family 2 (يَدْعُو) keeps ـُو in most forms and changes to ـِين for you-woman. Family 3 (يَنْسَى) has ـَى in most singular forms, ـَوْن for men in the plural, and ـَيْن for you-woman and the feminine plurals. Remember too: لَنْ + present means “will not”. "
             "A real quirk of family 2: they-men and they-women look identical, يَدْعُون.",
             tables=[table(["Pronoun", "يَدْعُو (invite)", "يَنْسَى (forget)"],
                           [["أَنَا", "أَدْعُو", "أَنْسَى"], ["أَنْتَ", "تَدْعُو", "تَنْسَى"], ["أَنْتِ", "تَدْعِين", "تَنْسَيْن"], ["هُوَ", "يَدْعُو", "يَنْسَى"], ["هِيَ", "تَدْعُو", "تَنْسَى"],
                            ["نَحْنُ", "نَدْعُو", "نَنْسَى"], ["أَنْتُمْ", "تَدْعُون", "تَنْسَوْن"], ["هُمْ", "يَدْعُون", "يَنْسَوْن"], ["هُنَّ", "يَدْعُون", "يَنْسَيْن"]],
                           say=[0, 1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "Context tells you who is meant when a form is shared.",
             examples=[
                 ex("أَدْعُو أَصْدِقَائِي إِلَى الْعَشَاء.", "I invite my friends to dinner.", "أَدْعُو"),
                 ex("هَلْ تَدْعِين أُمَّكِ إِلَى الْحَفْلَة؟", "Do you invite your mother to the party? (to a woman)", "تَدْعِين"),
                 ex("يَدْعُون الضُّيُوف إِلَى الْبَيْت.", "They invite the guests to the house.", "يَدْعُون"),
                 ex("أَنْسَى اِسْمَ الْفُنْدُق دَائِمًا.", "I always forget the name of the hotel.", "أَنْسَى"),
                 ex("تَنْسَى الطَّالِبَة كِتَابَهَا أَحْيَانًا.", "The student sometimes forgets her book.", "تَنْسَى"),
                 ex("لَا يَنْسَوْن مَوْعِدَ الْحَفْلَة.", "They do not forget the time of the party.", "يَنْسَوْن"),
             ]),
    ],
    exercises=[
        M("Which means “I invite”?", "أَدْعُو", ["تَدْعُو", "يَدْعُو", "أَدْعَى"], "أَ = I."),
        M("Which means “you invite” (to a woman)?", "تَدْعِين", ["تَدْعُو", "تَدْعُون", "تَدْعَيْن"], "ـِين."),
        M("Which means “I forget”?", "أَنْسَى", ["نَسِيتُ"], "Family 3: ـَى."),
        M("Which means “they forget” (men)?", "يَنْسَوْن", ["يَنْسَيْن", "يَنْسَى", "تَنْسَى"], "ـَوْن."),
        M("Which form is shared by “they (m.) invite” and “they (f.) invite”?", "يَدْعُون", ["يَدْعُو", "تَدْعُو"], "Family 2 quirk."),
        M("What does تَنْسَى الطَّالِبَة كِتَابَهَا أَحْيَانًا mean?", "The student sometimes forgets her book", ["The student always remembers her book", "The student invited her book", "The students forgot a book"], "أَحْيَانًا = sometimes."),
        F("أَنَا ___ أَصْدِقَائِي إِلَى الْعَشَاء.", "أَدْعُو", ["تَدْعُو", "نَدْعُو", "يَدْعُون"], "I invite.", tr="I invite my friends to dinner.", lemma="دعو:pres:ana"),
        F("أَنْتِ ___ أُمَّكِ إِلَى الْحَفْلَة؟", "تَدْعِين", ["تَدْعُو", "يَدْعُون", "أَدْعُو"], "To a woman.", tr="Do you invite your mother to the party? (to a woman)", lemma="دعو:pres:anti"),
        F("هُمْ لَا ___ مَوْعِدَ الْحَفْلَة.", "يَنْسَوْن", ["يَنْسَى", "تَنْسَى", "أَنْسَى"], "They (men).", tr="They do not forget the time of the party.", lemma="نسي:pres:hum"),
    ],
    verify=(vv("دعو", "pres", ana="أَدْعُو", anta="تَدْعُو", anti="تَدْعِين", huwa="يَدْعُو", hiya="تَدْعُو", nahnu="نَدْعُو", antum="تَدْعُون", hum="يَدْعُون", hunna="يَدْعُون")
            + vv("نسي", "pres", ana="أَنْسَى", anta="تَنْسَى", anti="تَنْسَيْن", huwa="يَنْسَى", hiya="تَنْسَى", nahnu="نَنْسَى", antum="تَنْسَوْن", hum="يَنْسَوْن", hunna="يَنْسَيْن")
            + vw("أَصْدِقَائِي", "أُمَّكِ", "الْفُنْدُق", "دَائِمًا", "كِتَابَهَا", "أَحْيَانًا", "مَوْعِدَ", "الضُّيُوف")),
)

# ---------------------------------------------------------------------------- 299
L299 = lesson(
    "Defective verbs: future, negation, commands",
    "لَا تَنْسَ! · اِمْشِ · اُدْعُ · لَمْ يَمْشِ",
    requires=["مشى", "دعا", "نسي", "ضيف", "حفلة", "لم", "لن"],
    cards=[
        card("The weak ending shortens",
             "For the future, add سَـ to the present: سَأَمْشِي. After لَمْ, and in the command, the long final vowel drops: لَمْ يَمْشِ (he did not walk), لَمْ يَدْعُ (he did not invite), لَمْ يَنْسَ (he did not forget). "
             "The command is the short form without the prefix: اِمْشِ (walk!), اُدْعُ (invite!), اِنْسَ (forget!). For a woman and a group, the long vowel returns: اِمْشِي, اِمْشُوا (family 3 verbs end in ـَيْ and ـَوْا).",
             tables=[table(["Meaning", "مَشَى", "دَعَا", "نَسِيَ"],
                           [["he will", "سَيَمْشِي", "سَيَدْعُو", "سَيَنْسَى"], ["he did not", "لَمْ يَمْشِ", "لَمْ يَدْعُ", "لَمْ يَنْسَ"],
                            ["to a man", "اِمْشِ", "اُدْعُ", "اِنْسَ"], ["to a woman", "اِمْشِي", "اُدْعِي", "اِنْسَيْ"], ["to a group", "اِمْشُوا", "اُدْعُوا", "اِنْسَوْا"],
                            ["do not (to a man)", "لَا تَمْشِ", "لَا تَدْعُ", "لَا تَنْسَ"]],
                           say=[1, 2, 3], tlit=[1, 2, 3], gloss=False)]),
        card("Everyday phrases",
             "لَا تَنْسَ is the verb you will hear most: “don’t forget!”.",
             examples=[
                 ex("سَأَمْشِي إِلَى الْمَدْرَسَة غَدًا.", "I will walk to school tomorrow.", "سَأَمْشِي"),
                 ex("لَمْ يَدْعُ أَخِي الضُّيُوف.", "My brother did not invite the guests.", "لَمْ يَدْعُ"),
                 ex("لَا تَنْسَ مَوْعِدَ الْحَفْلَة!", "Do not forget the time of the party! (to a man)", "لَا تَنْسَ"),
                 ex("لَا تَنْسَيْ جَوَازَ سَفَرِكِ!", "Do not forget your passport! (to a woman)", "لَا تَنْسَيْ"),
                 ex("اُدْعُ صَدِيقَكَ إِلَى الْبَيْت.", "Invite your friend to the house. (to a man)", "اُدْعُ"),
                 ex("اِمْشُوا بِسُرْعَة!", "Walk quickly! (to a group)", "اِمْشُوا"),
             ]),
    ],
    exercises=[
        M("What does لَا تَنْسَ mean?", "Do not forget (to a man)", ["He did not forget", "I forget", "Forget it (to a group)"], "لَا + short form = do not."),
        M("Which is the command “walk!” to a man?", "اِمْشِ", ["اِمْشِي", "اِمْشُوا", "يَمْشِي"], "No ending."),
        M("Which is “do not forget” to a woman?", "لَا تَنْسَيْ", ["لَا تَنْسَ", "لَا تَنْسَوْا", "لَمْ يَنْسَ"], "ـَيْ = to a woman."),
        M("Which is “he did not invite”?", "لَمْ يَدْعُ", ["لَمْ يَدْعُو", "لَنْ يَدْعُو", "لَا يَدْعُ"], "After لَمْ the و drops."),
        M("Which is “invite!” to a group?", "اُدْعُوا", ["اُدْعُ", "اُدْعِي", "يَدْعُون"], "ـُوا = group."),
        M("What does سَأَمْشِي إِلَى الْمَدْرَسَة غَدًا mean?", "I will walk to school tomorrow", ["I walked to school yesterday", "I do not walk to school", "Walk to school tomorrow"], "سَـ = will."),
        F("لَا ___ مَوْعِدَ الْحَفْلَة!", "تَنْسَ", ["تَنْسَى", "تَنْسَيْ", "تَنْسَوْا"], "A man: the long vowel drops.", tr="Do not forget the time of the party! (to a man)", lemma="نسي:jus:anta"),
        F("___ صَدِيقَكَ إِلَى الْبَيْت.", "اُدْعُ", ["اُدْعُوا", "اُدْعِي", "أَدْعُو"], "A command to a man.", tr="Invite your friend to the house. (to a man)", lemma="دعو:imp:anta"),
        F("___ بِسُرْعَة!", "اِمْشُوا", ["اِمْشِ", "اِمْشِي", "أَمْشِي"], "A group.", tr="Walk quickly! (to a group)", lemma="مشي:imp:antum"),
    ],
    verify=(vv("مشي", "fut", huwa="سَيَمْشِي", ana="سَأَمْشِي") + vv("دعو", "fut", huwa="سَيَدْعُو") + vv("نسي", "fut", huwa="سَيَنْسَى")
            + vv("مشي", "jus", huwa="يَمْشِ") + vv("دعو", "jus", huwa="يَدْعُ") + vv("نسي", "jus", huwa="يَنْسَ", anta="تَنْسَ", anti="تَنْسَيْ")
            + vv("مشي", "imp", anta="اِمْشِ", anti="اِمْشِي", antum="اِمْشُوا") + vv("دعو", "imp", anta="اُدْعُ", anti="اُدْعِي", antum="اُدْعُوا") + vv("نسي", "imp", anta="اِنْسَ", anti="اِنْسَيْ", antum="اِنْسَوْا")
            + vv("مشي", "neg", anta="لَا تَمْشِ") + vv("دعو", "neg", anta="لَا تَدْعُ") + vv("نسي", "neg", anta="لَا تَنْسَ", anti="لَا تَنْسَيْ")
            + vw("بِسُرْعَة", "الضُّيُوف", "جَوَازَ", "سَفَرِكِ", "صَدِيقَكَ", "تَنْسَيْ", "تَنْسَوْا", "يَدْعُو", "يَدْعُون")),
)

# ---------------------------------------------------------------------------- 300
L300 = lesson(
    "A story with defective verbs: an invitation",
    "دَعَانِي صَدِيقِي إِلَى حَفْلَة",
    requires=["دعا", "نسي", "مشى", "بقي", "لقي", "حفلة", "صديق", "هدية", "بيت", "ضيف"],
    cards=[
        card("Pronoun endings on defective verbs",
             "A verb can take an object pronoun directly: دَعَانِي (he invited me), دَعَاهُ (he invited him), دَعَاهَا (he invited her). The ending of the verb stays as it was: دَعَا + نِي. "
             "For a verb in the تْ form the pattern is دَعَتْنِي (she invited me).",
             tables=[table(["English", "Arabic"],
                           [["he invited me", "دَعَانِي"], ["he invited him", "دَعَاهُ"], ["he invited her", "دَعَاهَا"], ["she invited me", "دَعَتْنِي"], ["he met me", "لَقِيَنِي"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("An invitation (an invented practice text)",
             "A person tells what happened. Read it through once, then answer the questions.",
             examples=[
                 ex("دَعَانِي صَدِيقِي أَحْمَد إِلَى حَفْلَة فِي بَيْتِهِ.", "My friend Ahmad invited me to a party at his house.", "دَعَانِي"),
                 ex("مَشَيْتُ إِلَى بَيْتِهِ مَعَ أَخِي.", "I walked to his house with my brother.", "مَشَيْتُ"),
                 ex("لَقِيَنَا أَحْمَد عِنْدَ الْبَاب.", "Ahmad met us at the door.", "لَقِيَنَا"),
                 ex("نَسِيتُ الْهَدِيَّة فِي بَيْتِي!", "I forgot the gift at my house!", "نَسِيتُ"),
                 ex("رَجَعْتُ وَأَخَذْتُهَا، ثُمَّ بَقِينَا فِي الْحَفْلَة حَتَّى الْمَسَاء.", "I went back and took it, and then we stayed at the party until evening.", "بَقِينَا"),
                 ex("لَنْ أَنْسَى هَذِهِ الْحَفْلَة.", "I will not forget this party.", "لَنْ أَنْسَى"),
             ]),
    ],
    exercises=[
        M("Who invited the speaker?", "a friend called Ahmad", ["a brother", "a teacher", "a neighbour"], "دَعَانِي صَدِيقِي أَحْمَد."),
        M("How did they get to the house?", "they walked", ["by car", "by bus", "by plane"], "مَشَيْتُ إِلَى بَيْتِهِ."),
        M("What did the speaker forget?", "the gift", ["the passport", "the invitation", "the brother"], "نَسِيتُ الْهَدِيَّة فِي بَيْتِي."),
        M("How long did they stay?", "until the evening", ["a minute", "until morning", "a year"], "حَتَّى الْمَسَاء."),
        M("What does دَعَانِي mean?", "he invited me", ["I invited him", "he forgot me", "he met me"], "نِي = me."),
        M("What does لَنْ أَنْسَى mean?", "I will not forget", ["I did not forget", "I forget", "do not forget"], "لَنْ = will not."),
        F("___ صَدِيقِي أَحْمَد إِلَى حَفْلَة.", "دَعَانِي", ["دَعَوْتُهُ", "دَعَتْنِي", "دَعَوْنَا"], "He invited me.", tr="My friend Ahmad invited me to a party."),
        F("___ الْهَدِيَّة فِي بَيْتِي!", "نَسِيتُ", ["نَسِيَ", "نَسُوا", "أَنْسَى"], "I forgot.", tr="I forgot the gift at my house!", lemma="نسي:past:ana"),
        F("___ أَنْسَى هَذِهِ الْحَفْلَة.", "لَنْ", ["لَمْ", "إِنْ", "أَنْ"], "Will not.", tr="I will not forget this party."),
    ],
    verify=(vv("لقي", "past", huwa="لَقِيَ") + vv("بقي", "past", nahnu="بَقِينَا") + vv("مشي", "past", ana="مَشَيْتُ") + vv("نسي", "sub", ana="أَنْسَى")
            + vw("دَعَانِي", "دَعَاهُ", "دَعَاهَا", "دَعَتْنِي", "لَقِيَنِي", "لَقِيَنَا", "بَيْتِهِ", "رَجَعْتُ", "أَخَذْتُهَا", "الْهَدِيَّة", "حَتَّى", "الْمَسَاء", "أَحْمَد", "دَعَوْتُهُ", "دَعَوْنَا", "قَدْ")),
)


# ---------------------------------------------------------------------------- 301
L301 = lesson(
    "Measure VIII: اِفْتَعَلَ",
    "جَمَعَ ← اِجْتَمَعَ · نَظَرَ ← اِنْتَظَرَ · سَمِعَ ← اِسْتَمَعَ",
    requires=["جمع", "نظر", "سمع", "رفع", "شغل", "مدير", "موظف", "حافلة"],
    cards=[
        card("A ت tucked in after the first letter",
             "Measure VIII has the pattern اِفْتَعَلَ: an alif with kasra, then the first root letter with sukūn, then a ت with fatḥa, then the other two root letters with fatḥa. "
             "Its meaning often shows that the action involves the doer himself, or happens between people: جَمَعَ (he gathered something) → اِجْتَمَعَ (he met, came together).",
             tables=[table(["Measure I", "Measure VIII", "English"],
                           [["جَمَعَ", "اِجْتَمَعَ", "gathered → met, got together"], ["نَظَرَ", "اِنْتَظَرَ", "looked → waited"], ["سَمِعَ", "اِسْتَمَعَ", "heard → listened"],
                            ["رَفَعَ", "اِرْتَفَعَ", "raised → rose"], ["شَغَلَ", "اِشْتَغَلَ", "occupied → worked, was busy"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Look out for اِسْتَمَعَ: it begins with اِسْتَ like Measure X, but the س is the first root letter, so it is Measure VIII. These sentences are invented.",
             examples=[
                 ex("اِجْتَمَعَ الْمُدِير مَعَ الْمُوَظَّفِين.", "The director met with the employees.", "اِجْتَمَعَ"),
                 ex("اِنْتَظَرْتُ الْحَافِلَة سَاعَة.", "I waited for the bus for an hour.", "اِنْتَظَرْتُ"),
                 ex("اِسْتَمَعْنَا إِلَى الْأَخْبَار.", "We listened to the news.", "اِسْتَمَعْنَا"),
                 ex("اِرْتَفَعَ السِّعْر فِي الْمَطَار.", "The price at the airport rose.", "اِرْتَفَعَ"),
                 ex("اِشْتَغَلَ أَبِي فِي مَصْنَع.", "My father worked in a factory.", "اِشْتَغَلَ"),
                 ex("اِجْتَمَعَتِ الْعَائِلَة فِي الْبَيْت.", "The family got together at home.", "اِجْتَمَعَتِ"),
             ]),
    ],
    exercises=[
        M("Which is the Measure VIII verb from جَمَعَ?", "اِجْتَمَعَ", ["جَمَّعَ", "تَجَمَّعَ", "جُمِعَ"], "ت after the first letter."),
        M("What does اِنْتَظَرَ mean?", "he waited", ["he looked", "he heard", "he worked"], "Measure VIII of نَظَرَ."),
        M("What does اِسْتَمَعَ mean?", "he listened", ["he heard", "he used", "he asked"], "Measure VIII of سَمِعَ."),
        M("What does اِرْتَفَعَ السِّعْر mean?", "The price rose", ["The price fell", "The price was fixed", "The price was asked"], "اِرْتَفَعَ = rose."),
        M("Which letter is inserted after the first root letter in Measure VIII?", "ت", ["ن", "س", "ا"], "اِفْتَعَلَ."),
        M("Why is اِسْتَمَعَ Measure VIII, not X?", "the س is the first root letter", ["it has two س", "it is a command", "it is passive"], "Its first root letter is س, from سَمِعَ."),
        F("___ الْمُدِير مَعَ الْمُوَظَّفِين.", "اِجْتَمَعَ", ["جَمَعَ", "يَجْمَع", "اِجْتَمِعْ"], "Met: Measure VIII.", tr="The director met with the employees.", lemma="جمع#8:past:huwa"),
        F("___ الْحَافِلَة سَاعَة.", "اِنْتَظَرْتُ", ["نَظَرْتُ", "اِنْتَظَرَ", "أَنْتَظِر"], "I waited: Measure VIII, past, I.", tr="I waited for the bus for an hour.", lemma="نظر#8:past:ana"),
        F("___ أَبِي فِي مَصْنَع.", "اِشْتَغَلَ", ["شَغَلَ", "يَشْتَغِل", "اِشْتَغِلْ"], "Worked: Measure VIII.", tr="My father worked in a factory.", lemma="شغل#8:past:huwa"),
    ],
    verify=(vv("جمع#8", "past", huwa="اِجْتَمَعَ", hiya="اِجْتَمَعَتْ") + vv("نظر#8", "past", huwa="اِنْتَظَرَ", ana="اِنْتَظَرْتُ") + vv("سمع#8", "past", huwa="اِسْتَمَعَ", nahnu="اِسْتَمَعْنَا")
            + vv("رفع#8", "past", huwa="اِرْتَفَعَ") + vv("شغل#8", "past", huwa="اِشْتَغَلَ")
            + vw("جَمَعَ", "نَظَرَ", "سَمِعَ", "رَفَعَ", "شَغَلَ", "اِشْتَغَلَ", "الْمُوَظَّفِين", "الْحَافِلَة", "الْأَخْبَار", "السِّعْر", "مَصْنَع", "اِجْتَمَعَتِ", "الْعَائِلَة", "جَمَّعَ", "تَجَمَّعَ", "جُمِعَ", "يَجْمَع", "اِجْتَمِعْ", "أَنْتَظِر", "يَشْتَغِل", "اِشْتَغِلْ")),
)

# ---------------------------------------------------------------------------- 302
L302 = lesson(
    "Measure VIII: present and commands",
    "أَنْتَظِر · تَنْتَظِرِين · اِنْتَظِرْ · لَا تَنْتَظِرْ",
    requires=["جمع", "نظر", "سمع", "قرب", "شغل", "صديق", "مطار", "ساعة"],
    cards=[
        card("Prefix + the Measure VIII stem",
             "The present is the prefix, the first root letter with sukūn, ت with fatḥa, the second root letter with a kasra, and then the last root letter: يَنْتَظِر, يَجْتَمِع, يَسْتَمِع. "
             "The same endings are added as for every present verb. The command drops the prefix and puts اِ in front: اِنْتَظِرْ (wait!).",
             tables=[table(["Pronoun", "Present of اِنْتَظَرَ", "English"],
                           [["أَنَا", "أَنْتَظِر", "I wait"], ["أَنْتَ", "تَنْتَظِر", "you wait (m.)"], ["أَنْتِ", "تَنْتَظِرِين", "you wait (f.)"], ["هُوَ", "يَنْتَظِر", "he waits"], ["هِيَ", "تَنْتَظِر", "she waits"],
                            ["نَحْنُ", "نَنْتَظِر", "we wait"], ["أَنْتُمْ", "تَنْتَظِرُون", "you wait (pl.)"], ["هُمْ", "يَنْتَظِرُون", "they wait"]],
                           say=[0, 1], tlit=[1], gloss=False),
                    table(["Command", "Arabic"],
                          [["to a man", "اِنْتَظِرْ"], ["to a woman", "اِنْتَظِرِي"], ["to a group", "اِنْتَظِرُوا"], ["do not wait (to a man)", "لَا تَنْتَظِرْ"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Other Measure VIII verbs follow the same plan.",
             examples=[
                 ex("أَنْتَظِر صَدِيقِي فِي الْمَطَار.", "I am waiting for my friend at the airport.", "أَنْتَظِر"),
                 ex("هَلْ تَنْتَظِرِين الْحَافِلَة؟", "Are you waiting for the bus? (to a woman)", "تَنْتَظِرِين"),
                 ex("يَجْتَمِع الْمُوَظَّفُون كُلّ أُسْبُوع.", "The employees meet every week.", "يَجْتَمِع"),
                 ex("نَسْتَمِع إِلَى الْأَخْبَار فِي الصَّبَاح.", "We listen to the news in the morning.", "نَسْتَمِع"),
                 ex("اِنْتَظِرْ قَلِيلًا مِنْ فَضْلِك!", "Wait a little, please! (to a man)", "اِنْتَظِرْ"),
                 ex("لَا تَنْتَظِرُوا طَوِيلًا.", "Do not wait long. (to a group)", "لَا تَنْتَظِرُوا"),
             ]),
    ],
    exercises=[
        M("Which means “I wait”?", "أَنْتَظِر", ["تَنْتَظِر", "يَنْتَظِر", "نَنْتَظِر"], "أَ = I."),
        M("Which means “you wait” (to a woman)?", "تَنْتَظِرِين", ["تَنْتَظِرُون", "تَنْتَظِر", "أَنْتَظِر"], "ـِين."),
        M("Which means “they wait” (men)?", "يَنْتَظِرُون", ["يَنْتَظِر", "تَنْتَظِرِين", "نَنْتَظِر"], "ـُون."),
        M("Which is the command “wait!” to a man?", "اِنْتَظِرْ", ["يَنْتَظِر", "اِنْتَظَرَ", "اِنْتَظِرُوا"], "اِ + stem."),
        M("What does لَا تَنْتَظِرُوا طَوِيلًا mean?", "Do not wait long (to a group)", ["We waited long", "Wait long (to a group)", "He does not wait"], "لَا + short present + ـُوا."),
        M("What does نَسْتَمِع إِلَى الْأَخْبَار mean?", "We listen to the news", ["We read the news", "We wrote the news", "We hear nothing"], "نَسْتَمِع = we listen."),
        F("أَنَا ___ صَدِيقِي فِي الْمَطَار.", "أَنْتَظِر", ["تَنْتَظِر", "يَنْتَظِر", "نَنْتَظِر"], "I wait.", tr="I am waiting for my friend at the airport.", lemma="نظر#8:pres:ana"),
        F("___ قَلِيلًا مِنْ فَضْلِك!", "اِنْتَظِرْ", ["اِنْتَظِرُوا", "اِنْتَظِرِي", "تَنْتَظِر"], "A command to a man.", tr="Wait a little, please! (to a man)", lemma="نظر#8:imp:anta"),
        F("الْمُوَظَّفُون ___ كُلّ أُسْبُوع.", "يَجْتَمِعُون", ["يَجْتَمِع", "تَجْتَمِع", "أَجْتَمِع"], "Plural men.", tr="The employees meet every week.", lemma="جمع#8:pres:hum"),
    ],
    verify=(vv("نظر#8", "pres", ana="أَنْتَظِر", anta="تَنْتَظِر", anti="تَنْتَظِرِين", huwa="يَنْتَظِر", hiya="تَنْتَظِر", nahnu="نَنْتَظِر", antum="تَنْتَظِرُون", hum="يَنْتَظِرُون")
            + vv("نظر#8", "imp", anta="اِنْتَظِرْ", anti="اِنْتَظِرِي", antum="اِنْتَظِرُوا") + vv("نظر#8", "neg", anta="لَا تَنْتَظِرْ", antum="لَا تَنْتَظِرُوا")
            + vv("جمع#8", "pres", huwa="يَجْتَمِع", hum="يَجْتَمِعُون") + vv("سمع#8", "pres", nahnu="نَسْتَمِع")
            + vw("الْمُوَظَّفُون", "الْمَطَار", "صَدِيقِي", "أُسْبُوع", "طَوِيلًا", "قَلِيلًا", "الْحَافِلَة", "تَجْتَمِع", "أَجْتَمِع", "اِنْتَظِرُوا", "اِنْتَظِرِي", "اِنْتَظَرَ")),
)

# ---------------------------------------------------------------------------- 303
L303 = lesson(
    "Measure X: اِسْتَفْعَلَ",
    "خَدَمَ ← اِسْتَخْدَمَ · قَبِلَ ← اِسْتَقْبَلَ · عَمِلَ ← اِسْتَعْمَلَ",
    requires=["خدم", "قبل", "عمل", "خرج", "رجع", "فندق", "سائح", "هاتف", "هاتف"],
    cards=[
        card("Adding اِسْتَ",
             "Measure X has the pattern اِسْتَفْعَلَ: put اِسْتَ in front of the three root letters: the first root letter has sukūn, and the second and third have fatḥa. "
             "It often means to ask for, to seek or to put something to use: خَدَمَ (he served) → اِسْتَخْدَمَ (he put to service, used).",
             tables=[table(["Measure I", "Measure X", "English"],
                           [["خَدَمَ", "اِسْتَخْدَمَ", "served → used"], ["قَبِلَ", "اِسْتَقْبَلَ", "accepted → received, welcomed"], ["عَمِلَ", "اِسْتَعْمَلَ", "worked → used, employed"],
                            ["خَرَجَ", "اِسْتَخْرَجَ", "went out → extracted"], ["رَجَعَ", "اِسْتَرْجَعَ", "returned → got back"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Examples",
             "Some very common verbs are Measure X with a weak middle letter, such as اِسْتَطَاعَ (he was able). You will meet them as phrases first. These sentences are invented.",
             examples=[
                 ex("اِسْتَخْدَمْتُ الْهَاتِف فِي الْمَطَار.", "I used the phone at the airport.", "اِسْتَخْدَمْتُ"),
                 ex("اِسْتَقْبَلَ الْفُنْدُق السُّيَّاح.", "The hotel welcomed the tourists.", "اِسْتَقْبَلَ"),
                 ex("اِسْتَعْمَلَ الْمُوَظَّف جِهَازًا جَدِيدًا.", "The employee used a new device.", "اِسْتَعْمَلَ"),
                 ex("اِسْتَقْبَلَتْنَا الْمُدِيرَة بِالْقَهْوَة.", "The manager welcomed us with coffee.", "اِسْتَقْبَلَتْنَا"),
                 ex("اِسْتَرْجَعْتُ حَقِيبَتِي بَعْد سَاعَة.", "I got my bag back after an hour.", "اِسْتَرْجَعْتُ"),
                 ex("اِسْتَطَاعَ الرَّاكِب أَنْ يَصِل فِي الْوَقْت.", "The passenger was able to arrive on time.", "اِسْتَطَاعَ"),
             ]),
    ],
    exercises=[
        M("Which is the Measure X verb from خَدَمَ?", "اِسْتَخْدَمَ", ["خَدَّمَ", "اِخْتَدَمَ", "تَخَدَّمَ"], "اِسْتَ + root."),
        M("What does اِسْتَقْبَلَ mean?", "he welcomed, received", ["he refused a gift", "he asked for money", "he stood up"], "اِسْتَقْبَلَ = to receive a guest."),
        M("What does اِسْتَعْمَلَ mean?", "he used", ["he worked", "he forgot", "he asked"], "Measure X of عَمِلَ."),
        M("What does اِسْتَرْجَعْتُ حَقِيبَتِي mean?", "I got my bag back", ["I lost my bag", "I bought a bag", "I carried a bag"], "اِسْتَرْجَعَ = to get back."),
        M("What does Measure X often mean?", "to ask for, seek or put to use", ["to do something together", "to become passive", "to look at"], "Seeking/using."),
        M("What is the pattern of Measure X?", "اِسْتَفْعَلَ", ["اِفْتَعَلَ", "اِنْفَعَلَ", "فَعَّلَ"], "اِسْتَ + root."),
        F("___ الْفُنْدُق السُّيَّاح.", "اِسْتَقْبَلَ", ["قَبِلَ", "يَقْبَل", "اِقْتَبَلَ"], "Welcomed: Measure X.", tr="The hotel welcomed the tourists.", lemma="قبل#10:past:huwa"),
        F("___ الْهَاتِف فِي الْمَطَار.", "اِسْتَخْدَمْتُ", ["خَدَمْتُ", "اِسْتَخْدَمَ", "أَسْتَخْدِم"], "I used: Measure X, past, I.", tr="I used the phone at the airport.", lemma="خدم#10:past:ana"),
        F("___ الْمُوَظَّف جِهَازًا جَدِيدًا.", "اِسْتَعْمَلَ", ["عَمِلَ", "يَعْمَل", "اِعْتَمَلَ"], "Used: Measure X.", tr="The employee used a new device.", lemma="عمل#10:past:huwa"),
    ],
    verify=(vv("خدم#10", "past", huwa="اِسْتَخْدَمَ", ana="اِسْتَخْدَمْتُ") + vv("قبل#10", "past", huwa="اِسْتَقْبَلَ", hiya="اِسْتَقْبَلَتْ") + vv("عمل#10", "past", huwa="اِسْتَعْمَلَ")
            + vv("خرج#10", "past", huwa="اِسْتَخْرَجَ") + vv("رجع#10", "past", ana="اِسْتَرْجَعْتُ")
            + vw("خَدَمَ", "قَبِلَ", "عَمِلَ", "خَرَجَ", "رَجَعَ", "اِسْتَطَاعَ", "السُّيَّاح", "الْفُنْدُق", "جِهَازًا", "الْمُدِيرَة", "بِالْقَهْوَة", "حَقِيبَتِي", "خَدَّمَ", "تَخَدَّمَ", "يَقْبَل", "يَعْمَل", "أَسْتَخْدِم", "فَعَّلَ", "اِفْتَعَلَ", "اِنْفَعَلَ")),
)

# ---------------------------------------------------------------------------- 304
L304 = lesson(
    "Measure X: present and commands",
    "أَسْتَخْدِم · تَسْتَقْبِلِين · اِسْتَخْدِمْ",
    requires=["خدم", "قبل", "عمل", "خرج", "هاتف", "فندق", "سائح", "كمبيوتر", "طاولة"],
    cards=[
        card("Same plan as Measure VIII",
             "The present is the prefix with fatḥa, then سْتَ, the three root letters, and a kasra before the last one: يَسْتَخْدِم, يَسْتَقْبِل, يَسْتَعْمِل. "
             "The command drops the prefix and puts اِ in front: اِسْتَخْدِمْ (use!).",
             tables=[table(["Pronoun", "Present of اِسْتَخْدَمَ", "English"],
                           [["أَنَا", "أَسْتَخْدِم", "I use"], ["أَنْتَ", "تَسْتَخْدِم", "you use (m.)"], ["أَنْتِ", "تَسْتَخْدِمِين", "you use (f.)"], ["هُوَ", "يَسْتَخْدِم", "he uses"], ["هِيَ", "تَسْتَخْدِم", "she uses"],
                            ["نَحْنُ", "نَسْتَخْدِم", "we use"], ["أَنْتُمْ", "تَسْتَخْدِمُون", "you use (pl.)"], ["هُمْ", "يَسْتَخْدِمُون", "they use"]],
                           say=[0, 1], tlit=[1], gloss=False),
                    table(["Command", "Arabic"],
                          [["to a man", "اِسْتَخْدِمْ"], ["to a woman", "اِسْتَخْدِمِي"], ["to a group", "اِسْتَخْدِمُوا"], ["do not use (to a man)", "لَا تَسْتَخْدِمْ"]],
                          say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "These sentences use the present of Measure X.",
             examples=[
                 ex("أَسْتَخْدِم الْحَاسُوب كُلّ يَوْم.", "I use the computer every day.", "أَسْتَخْدِم"),
                 ex("تَسْتَقْبِل الْفَنَادِق السُّيَّاح فِي الصَّيْف.", "Hotels welcome tourists in the summer.", "تَسْتَقْبِل"),
                 ex("يَسْتَعْمِل أَخِي هَاتِفِي أَحْيَانًا.", "My brother sometimes uses my phone.", "يَسْتَعْمِل"),
                 ex("هَلْ تَسْتَخْدِمِين الْحَافِلَة؟", "Do you use the bus? (to a woman)", "تَسْتَخْدِمِين"),
                 ex("اِسْتَخْدِمْ هَذِهِ الْبِطَاقَة هُنَا.", "Use this card here. (to a man)", "اِسْتَخْدِمْ"),
                 ex("لَا تَسْتَخْدِمُوا الْهَاتِف فِي الطَّائِرَة.", "Do not use the phone on the plane. (to a group)", "لَا تَسْتَخْدِمُوا"),
             ]),
    ],
    exercises=[
        M("Which means “I use”?", "أَسْتَخْدِم", ["تَسْتَخْدِم", "يَسْتَخْدِم", "نَسْتَخْدِم"], "أَ = I."),
        M("Which means “they use” (men)?", "يَسْتَخْدِمُون", ["تَسْتَخْدِمِين", "يَسْتَخْدِم", "نَسْتَخْدِم"], "ـُون."),
        M("Which is the command “use!” to a man?", "اِسْتَخْدِمْ", ["يَسْتَخْدِم", "اِسْتَخْدَمَ", "اِسْتَخْدِمِي"], "اِ + stem."),
        M("What does لَا تَسْتَخْدِمُوا الْهَاتِف فِي الطَّائِرَة mean?", "Do not use the phone on the plane (to a group)", ["We used the phone", "Use the phone on the plane", "He does not use the phone"], "لَا + short present."),
        M("What does تَسْتَقْبِل الْفَنَادِق السُّيَّاح mean?", "Hotels welcome tourists", ["Tourists build hotels", "The hotel left the tourist", "A tourist is a hotel"], "تَسْتَقْبِل = welcomes."),
        M("Why is it تَسْتَقْبِل الْفَنَادِق, not يَسْتَقْبِل؟", "a plural of things takes the feminine singular", ["the hotels are women", "it is a command", "it is passive"], "A plural of things (الْفَنَادِق) takes the feminine singular verb."),
        F("أَنَا ___ الْحَاسُوب كُلّ يَوْم.", "أَسْتَخْدِم", ["تَسْتَخْدِم", "يَسْتَخْدِم", "نَسْتَخْدِم"], "I use.", tr="I use the computer every day.", lemma="خدم#10:pres:ana"),
        F("___ الْفَنَادِق السُّيَّاح فِي الصَّيْف.", "تَسْتَقْبِل", ["يَسْتَقْبِل", "أَسْتَقْبِل", "نَسْتَقْبِل"], "Things in the plural: feminine singular.", tr="Hotels welcome tourists in the summer.", lemma="قبل#10:pres:hiya"),
        F("___ هَذِهِ الْبِطَاقَة هُنَا.", "اِسْتَخْدِمْ", ["اِسْتَخْدِمُوا", "اِسْتَخْدِمِي", "تَسْتَخْدِم"], "A command to a man.", tr="Use this card here. (to a man)", lemma="خدم#10:imp:anta"),
    ],
    verify=(vv("خدم#10", "pres", ana="أَسْتَخْدِم", anta="تَسْتَخْدِم", anti="تَسْتَخْدِمِين", huwa="يَسْتَخْدِم", hiya="تَسْتَخْدِم", nahnu="نَسْتَخْدِم", antum="تَسْتَخْدِمُون", hum="يَسْتَخْدِمُون")
            + vv("خدم#10", "imp", anta="اِسْتَخْدِمْ", anti="اِسْتَخْدِمِي", antum="اِسْتَخْدِمُوا") + vv("خدم#10", "neg", anta="لَا تَسْتَخْدِمْ", antum="لَا تَسْتَخْدِمُوا")
            + vv("قبل#10", "pres", hiya="تَسْتَقْبِل", huwa="يَسْتَقْبِل") + vv("عمل#10", "pres", huwa="يَسْتَعْمِل")
            + vw("الْحَاسُوب", "الْفَنَادِق", "السُّيَّاح", "الصَّيْف", "هَاتِفِي", "أَحْيَانًا", "الْحَافِلَة", "الْبِطَاقَة", "الْهَاتِف", "اِسْتَخْدِمِي", "اِسْتَخْدِمُوا")),
)

# ---------------------------------------------------------------------------- 305
L305 = lesson(
    "Verbal nouns of Measure VIII: اِفْتِعَال",
    "اِجْتِمَاع · اِنْتِظَار · اِحْتِفَال · اِرْتِفَاع",
    requires=["جمع", "نظر", "رفع", "قرب", "سمع", "صالة", "سعر", "حفل", "عيد"],
    cards=[
        card("The pattern",
             "The verbal noun of Measure VIII is اِفْتِعَال: kasra under the ت, then a long ā before the last root letter. اِجْتَمَعَ gives اِجْتِمَاع (meeting), اِنْتَظَرَ gives اِنْتِظَار (waiting).",
             tables=[table(["Verb", "Verbal noun", "English"],
                           [["اِجْتَمَعَ", "اِجْتِمَاع", "a meeting"], ["اِنْتَظَرَ", "اِنْتِظَار", "waiting"], ["اِحْتَفَلَ", "اِحْتِفَال", "a celebration"], ["اِرْتَفَعَ", "اِرْتِفَاع", "a rise, height"],
                            ["اِسْتَمَعَ", "اِسْتِمَاع", "listening"], ["اِقْتَرَبَ", "اِقْتِرَاب", "approaching"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("In use",
             "The nouns are everyday words: you will see صَالَة اِنْتِظَار (waiting room), اِجْتِمَاع (meeting) and اِرْتِفَاع الْأَسْعَار (the rise in prices).",
             examples=[
                 ex("الْمُدِير فِي اِجْتِمَاع الْآن.", "The director is in a meeting now.", "اِجْتِمَاع"),
                 ex("نَجْلِس فِي صَالَة الِانْتِظَار.", "We sit in the waiting room.", "الِانْتِظَار"),
                 ex("اِرْتِفَاع الْأَسْعَار مُشْكِلَة كَبِيرَة.", "The rise in prices is a big problem.", "اِرْتِفَاع"),
                 ex("الِاسْتِمَاع إِلَى الْأَخْبَار مُفِيد.", "Listening to the news is useful.", "الِاسْتِمَاع"),
                 ex("الِاحْتِفَال بِالْعِيد فِي الْمَدِينَة كَبِير.", "The Eid celebration in the city is big.", "الِاحْتِفَال"),
                 ex("مَعَ اِقْتِرَاب الشِّتَاء يَنْزِل الْمَطَر.", "As winter approaches, the rain falls.", "اِقْتِرَاب"),
             ]),
    ],
    exercises=[
        M("Which is the verbal noun of اِجْتَمَعَ?", "اِجْتِمَاع", ["جَمْع", "مُجْتَمِع", "يَجْتَمِع"], "اِفْتِعَال."),
        M("Which is the verbal noun of اِنْتَظَرَ?", "اِنْتِظَار", ["نَظَر", "مُنْتَظِر", "اِنْتَظِرْ"], "اِفْتِعَال."),
        M("What is صَالَة اِنْتِظَار?", "a waiting room", ["a meeting room", "a dining room", "a gate"], "اِنْتِظَار = waiting."),
        M("What does اِرْتِفَاع الْأَسْعَار mean?", "the rise in prices", ["the fall in prices", "the price of heights", "high markets"], "اِرْتِفَاع = rise."),
        M("What does اِحْتِفَال mean?", "a celebration", ["a meeting", "an arrival", "a delay"], "Noun of اِحْتَفَلَ."),
        M("Which pattern is the verbal noun of Measure VIII?", "اِفْتِعَال", ["اِسْتِفْعَال", "اِنْفِعَال", "تَفْعِيل"], "VIII → اِفْتِعَال."),
        F("الْمُدِير فِي ___ الْآن.", "اِجْتِمَاع", ["اِجْتَمَعَ", "يَجْتَمِع", "اِجْتَمِعْ"], "A noun after فِي.", tr="The director is in a meeting now."),
        F("___ الْأَسْعَار مُشْكِلَة كَبِيرَة.", "اِرْتِفَاع", ["اِرْتَفَعَ", "يَرْتَفِع", "مُرْتَفِع"], "A noun as subject.", tr="The rise in prices is a big problem."),
        F("نَجْلِس فِي صَالَة ___.", "الِانْتِظَار", ["الْحَقِيبَة", "الْجَوَاز", "الِارْتِفَاع"], "A waiting room.", tr="We sit in the waiting room."),
    ],
    verify=(vv("جلس", "pres", nahnu="نَجْلِس")
            + vw("اِجْتِمَاع", "اِنْتِظَار", "اِحْتِفَال", "اِرْتِفَاع", "اِسْتِمَاع", "اِقْتِرَاب", "اِحْتَفَلَ", "اِقْتَرَبَ", "الِانْتِظَار", "مُشْكِلَة", "مُفِيد", "الْعِيد", "الشِّتَاء", "يَنْزِل", "الْمَطَر", "مُجْتَمِع", "مُنْتَظِر", "اِجْتَمَعَ", "اِنْتَظَرَ", "اِنْتَظِرْ", "جَمْع", "نَظَر", "مُرْتَفِع", "يَرْتَفِع", "اِرْتَفَعَ", "اِجْتَمِعْ", "الِاجْتِمَاع", "الِاحْتِفَال", "الِاسْتِمَاع")),
)

# ---------------------------------------------------------------------------- 306
L306 = lesson(
    "Verbal nouns of Measure X: اِسْتِفْعَال",
    "اِسْتِخْدَام · اِسْتِقْبَال · اِسْتِعْمَال",
    requires=["خدم", "قبل", "عمل", "فندق", "هاتف", "طريقة", "مكتب", "مدير", "طائرة"],
    cards=[
        card("The pattern",
             "The verbal noun of Measure X is اِسْتِفْعَال: kasra under the ت and a long ā before the last root letter. اِسْتَخْدَمَ gives اِسْتِخْدَام (use), اِسْتَقْبَلَ gives اِسْتِقْبَال (reception, welcome).",
             tables=[table(["Verb", "Verbal noun", "English"],
                           [["اِسْتَخْدَمَ", "اِسْتِخْدَام", "use"], ["اِسْتَقْبَلَ", "اِسْتِقْبَال", "reception, welcome"], ["اِسْتَعْمَلَ", "اِسْتِعْمَال", "use, usage"], ["اِسْتَرْجَعَ", "اِسْتِرْجَاع", "getting back, retrieval"]],
                           say=[0, 1], tlit=[1], gloss=False)]),
        card("Signs and phrases",
             "These nouns appear on signs: مَكْتَب الِاسْتِقْبَال (reception desk), طَرِيقَة الِاسْتِعْمَال (directions for use), اِسْتِخْدَام الْهَاتِف مَمْنُوع (use of the phone is forbidden).",
             examples=[
                 ex("مَكْتَب الِاسْتِقْبَال فِي الطَّابِق الْأَوَّل.", "The reception desk is on the first floor.", "الِاسْتِقْبَال"),
                 ex("طَرِيقَة الِاسْتِعْمَال مَكْتُوبَة عَلَى الْعُلْبَة.", "The directions for use are written on the box.", "الِاسْتِعْمَال"),
                 ex("اِسْتِخْدَام الْهَاتِف مَمْنُوع فِي الطَّائِرَة.", "Using the phone is forbidden on the plane.", "اِسْتِخْدَام"),
                 ex("اِسْتِقْبَال الْفُنْدُق كَانَ جَمِيلًا.", "The hotel’s welcome was lovely.", "اِسْتِقْبَال"),
                 ex("اِسْتِرْجَاع الْمَال يَأْخُذ أُسْبُوعًا.", "Getting the money back takes a week.", "اِسْتِرْجَاع"),
                 ex("بَعْد اِسْتِخْدَام الْبِطَاقَة نَحْتَفِظ بِالْفَاتُورَة.", "After using the card we keep the receipt.", "اِسْتِخْدَام"),
             ]),
    ],
    exercises=[
        M("Which is the verbal noun of اِسْتَخْدَمَ?", "اِسْتِخْدَام", ["خِدْمَة", "مُسْتَخْدِم", "يَسْتَخْدِم"], "اِسْتِفْعَال."),
        M("What is مَكْتَب الِاسْتِقْبَال?", "the reception desk", ["the manager’s office", "the exit", "the bank"], "اِسْتِقْبَال = reception."),
        M("What is طَرِيقَة الِاسْتِعْمَال?", "directions for use", ["a way to travel", "a payment method", "a kind of work"], "اِسْتِعْمَال = use."),
        M("What does اِسْتِخْدَام الْهَاتِف مَمْنُوع mean?", "Using the phone is forbidden", ["The phone is free", "The phone is broken", "The phone is expensive"], "مَمْنُوع = forbidden."),
        M("Which pattern is the verbal noun of Measure X?", "اِسْتِفْعَال", ["اِفْتِعَال", "اِنْفِعَال", "مُفَاعَلَة"], "X → اِسْتِفْعَال."),
        M("What does اِسْتِرْجَاع الْمَال يَأْخُذ أُسْبُوعًا mean?", "Getting the money back takes a week", ["The money is a week old", "He keeps the money for a week", "A week is not enough money"], "يَأْخُذ = takes."),
        F("___ الْهَاتِف مَمْنُوع فِي الطَّائِرَة.", "اِسْتِخْدَام", ["اِسْتَخْدَمَ", "يَسْتَخْدِم", "اِسْتَخْدِمْ"], "A noun as subject.", tr="Using the phone is forbidden on the plane."),
        F("مَكْتَب ___ فِي الطَّابِق الْأَوَّل.", "الِاسْتِقْبَال", ["الِاسْتِعْمَال", "الِارْتِفَاع", "الِانْتِظَار"], "A reception desk.", tr="The reception desk is on the first floor."),
        F("طَرِيقَة ___ مَكْتُوبَة عَلَى الْعُلْبَة.", "الِاسْتِعْمَال", ["الِارْتِفَاع", "الِانْتِظَار", "الِاحْتِفَال"], "Directions for use.", tr="The directions for use are written on the box."),
    ],
    verify=(vv("حفظ#8", "pres", nahnu="نَحْتَفِظ") + vw("اِسْتِخْدَام", "اِسْتِقْبَال", "اِسْتِعْمَال", "اِسْتِرْجَاع", "الِاسْتِقْبَال", "الِاسْتِعْمَال", "الِاسْتِرْجَاع", "الِاجْتِمَاع", "الِانْتِظَار", "الِاحْتِفَال", "مُسْتَخْدِم", "خِدْمَة", "طَرِيقَة", "الطَّابِق", "الْأَوَّل", "مَكْتُوبَة", "الْعُلْبَة", "الْمَال", "أُسْبُوعًا", "يَأْخُذ", "الْوَصْل", "جَمِيلًا", "اِنْفِعَال")),
)

# ---------------------------------------------------------------------------- 307
L307 = lesson(
    "A map of Measures I to X",
    "كَتَبَ · عَلَّمَ · شَاهَدَ · أَغْلَقَ · تَعَلَّمَ · تَبَادَلَ · اِنْطَلَقَ · اِنْتَظَرَ · اِسْتَخْدَمَ",
    requires=["كتب", "علم", "شاهد", "غلق", "تعلم", "تبادل", "طلق", "نظر", "خدم"],
    cards=[
        card("Nine patterns on one page",
             "Most verbs from three-letter roots are built on one of these patterns, so recognising the measure tells you a lot about a new word. Measure IX is rare: it describes colours and defects, and you can leave it for later. "
             "Here are the measures you now know, each with its past, its present and its verbal noun.",
             tables=[table(["Measure", "Past", "Present", "Verbal noun"],
                           [["I", "كَتَبَ", "يَكْتُب", "كِتَابَة"], ["II", "عَلَّمَ", "يُعَلِّم", "تَعْلِيم"], ["III", "شَاهَدَ", "يُشَاهِد", "مُشَاهَدَة"], ["IV", "أَغْلَقَ", "يُغْلِق", "إِغْلَاق"],
                            ["V", "تَعَلَّمَ", "يَتَعَلَّم", "تَعَلُّم"], ["VI", "تَبَادَلَ", "يَتَبَادَل", "تَبَادُل"], ["VII", "اِنْطَلَقَ", "يَنْطَلِق", "اِنْطِلَاق"], ["VIII", "اِنْتَظَرَ", "يَنْتَظِر", "اِنْتِظَار"],
                            ["X", "اِسْتَخْدَمَ", "يَسْتَخْدِم", "اِسْتِخْدَام"]],
                           say=[1, 2, 3], tlit=[1, 2, 3], gloss=False)]),
        card("Clues in the first letters",
             "Learn to look at the start of a past verb. A doubled middle letter (عَلَّمَ) means II. An ā after the first letter (شَاهَدَ) means III. أَ at the start usually means IV (unless the أ is a root letter, as in أَكَلَ). تَ at the start usually means V or VI. "
             "اِنْ often means VII, but check the root: in اِنْتَظَرَ (root ن ظ ر) the ن is a root letter and the ت shows Measure VIII. اِ + a ت after the first root letter means VIII, and اِسْتَ means X.",
             examples=[
                 ex("عَلَّمَ الْمُدَرِّس الطُّلَّاب.", "The teacher taught the students.", "عَلَّمَ"),
                 ex("شَاهَدْنَا الْأَخْبَار.", "We watched the news.", "شَاهَدْنَا"),
                 ex("أَغْلَقَ الْمُوَظَّف الْبَاب.", "The employee closed the door.", "أَغْلَقَ"),
                 ex("تَعَلَّمْتُ الْعَرَبِيَّة.", "I learned Arabic.", "تَعَلَّمْتُ"),
                 ex("اِنْتَظَرَ الرَّاكِب الطَّائِرَة.", "The passenger waited for the plane.", "اِنْتَظَرَ"),
                 ex("اِسْتَخْدَمَتِ الشَّرِكَة طَائِرَات جَدِيدَة.", "The company used new planes.", "اِسْتَخْدَمَتِ"),
             ]),
    ],
    exercises=[
        M("Which measure is عَلَّمَ?", "II", ["I", "III", "IV"], "A doubled middle letter."),
        M("Which measure is شَاهَدَ?", "III", ["II", "IV", "V"], "An ā after the first letter."),
        M("Which measure is أَغْلَقَ?", "IV", ["II", "VII", "X"], "أَ at the start."),
        M("Which measure is اِنْطَلَقَ?", "VII", ["VIII", "X", "V"], "اِنْ at the start."),
        M("Which measure is اِنْتَظَرَ?", "VIII", ["VII", "X", "III"], "ت after the first root letter."),
        M("Which measure is اِسْتَخْدَمَ?", "X", ["VIII", "VII", "IV"], "اِسْتَ at the start."),
        F("___ الْمُدَرِّس الطُّلَّاب.", "عَلَّمَ", ["تَعَلَّمَ", "شَاهَدَ", "اِنْتَظَرَ"], "Taught: Measure II.", tr="The teacher taught the students."),
        F("___ الرَّاكِب الطَّائِرَة.", "اِنْتَظَرَ", ["اِنْطَلَقَ", "أَغْلَقَ", "اِسْتَخْدَمَ"], "Waited: Measure VIII.", tr="The passenger waited for the plane."),
        F("___ الْهَاتِف فِي الْقَاعَة مَمْنُوع.", "اِسْتِخْدَام", ["اِنْطِلَاق", "تَعْلِيم", "اِنْكِسَار"], "The verbal noun of اِسْتَخْدَمَ (Measure X) is اِسْتِخْدَام.", tr="Using the phone in the hall is forbidden."),
    ],
    verify=(vv("علم#2", "past", huwa="عَلَّمَ") + vv("شهد#3", "past", huwa="شَاهَدَ", nahnu="شَاهَدْنَا") + vv("غلق#4", "past", huwa="أَغْلَقَ") + vv("علم#5", "past", huwa="تَعَلَّمَ", ana="تَعَلَّمْتُ")
            + vv("بدل#6", "past", huwa="تَبَادَلَ") + vv("طلق#7", "past", huwa="اِنْطَلَقَ") + vv("نظر#8", "past", huwa="اِنْتَظَرَ") + vv("خدم#10", "past", huwa="اِسْتَخْدَمَ", hiya="اِسْتَخْدَمَتْ")
            + vw("كِتَابَة", "تَعْلِيم", "مُشَاهَدَة", "إِغْلَاق", "تَعَلُّم", "تَبَادُل", "اِنْطِلَاق", "الْمُدَرِّس", "الطُّلَّاب", "الْأَخْبَار", "الْمُوَظَّف", "الْعَرَبِيَّة", "الرَّاكِب", "اِسْتَخْدَمَتِ", "الشَّرِكَة", "طَائِرَات", "جَدِيدَة", "اِنْتِظَار")),
)


# ---------------------------------------------------------------------------- 308
L308 = lesson(
    "Hospitality and visiting",
    "يَسْتَقْبِل صَاحِب الْبَيْت الضُّيُوف · تُقَدَّم الْقَهْوَة",
    requires=["ضيف", "ضيافة", "قهوة", "شاي", "زيارة", "صاحب", "بيت", "شكر", "بقي", "زار"],
    cards=[
        card("Words for visits",
             "A guest is ضَيْف (plural ضُيُوف) and hospitality is ضِيَافَة. The person who owns the house is صَاحِب الْبَيْت. "
             "Customs differ from country to country and from family to family, so the sentences below describe what happens in many homes, not in all of them.",
             tables=[table(["English", "Arabic"],
                           [["guest", "ضَيْف"], ["guests", "ضُيُوف"], ["hospitality", "ضِيَافَة"], ["the owner of the house", "صَاحِب الْبَيْت"], ["visit", "زِيَارَة"], ["relatives", "أَقَارِب"],
                            ["coffee", "قَهْوَة"], ["juice", "عَصِير"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In many homes",
             "Notice the verbs from this chapter: the X verb يَسْتَقْبِل, the passive تُقَدَّم, the defective يَبْقَى, and the hollow يَزُور.",
             examples=[
                 ex("فِي كَثِير مِنَ الْبُيُوت يَسْتَقْبِل صَاحِب الْبَيْت الضُّيُوف عِنْدَ الْبَاب.", "In many homes the owner of the house welcomes the guests at the door.", "يَسْتَقْبِل"),
                 ex("تُقَدَّم الْقَهْوَة أَوِ الْعَصِير لِلضَّيْف.", "Coffee or juice is served to the guest.", "تُقَدَّم"),
                 ex("يَزُور النَّاس أَقَارِبَهُمْ فِي الْأَعْيَاد.", "People visit their relatives at the holidays.", "يَزُور"),
                 ex("يَبْقَى الضُّيُوف سَاعَة أَوْ سَاعَتَيْن.", "The guests stay an hour or two.", "يَبْقَى"),
                 ex("لَا يَنْسَى الضَّيْف أَنْ يَشْكُر صَاحِب الْبَيْت.", "The guest does not forget to thank the owner of the house.", "لَا يَنْسَى"),
                 ex("يَدْعُو صَاحِب الْبَيْت الضَّيْف إِلَى الْعَشَاء.", "The owner of the house invites the guest to dinner.", "يَدْعُو"),
             ]),
    ],
    exercises=[
        M("Which word means “guest”?", "ضَيْف", ["صَاحِب", "قَرِيب", "جَار"], "ضَيْف = guest."),
        M("Who is صَاحِب الْبَيْت?", "the owner of the house", ["the guest", "the neighbour", "the cook"], "صَاحِب = owner."),
        M("What does ضِيَافَة mean?", "hospitality", ["tradition", "holiday", "greeting"], "Same root as ضَيْف."),
        M("What does تُقَدَّم الْقَهْوَة لِلضَّيْف mean?", "Coffee is served to the guest", ["The guest makes coffee", "The guest drinks tea", "The owner forgets the coffee"], "Passive: تُقَدَّم."),
        M("What does لَا يَنْسَى الضَّيْف أَنْ يَشْكُر صَاحِب الْبَيْت mean?", "The guest does not forget to thank the owner", ["The guest forgets the owner", "The owner thanks the guest", "The guest invites the owner"], "لَا يَنْسَى = does not forget."),
        M("Why does the lesson say “in many homes”?", "customs differ between families and countries", ["every home is the same", "it is a law", "only guests do this"], "Customs vary."),
        F("___ صَاحِب الْبَيْت الضُّيُوف عِنْدَ الْبَاب.", "يَسْتَقْبِل", ["يَسْتَقْبَل", "اِسْتَقْبِلْ", "يَقْبَل"], "Present, Measure X.", tr="The owner of the house welcomes the guests at the door.", lemma="قبل#10:pres:huwa"),
        F("___ الضُّيُوف سَاعَة أَوْ سَاعَتَيْن.", "يَبْقَى", ["يَبْقِي", "بَقِيَ", "نَبْقَى"], "Defective verb, present, he-form.", tr="The guests stay an hour or two.", lemma="بقي:pres:huwa"),
        F("يَزُور النَّاس ___ فِي الْأَعْيَاد.", "أَقَارِبَهُمْ", ["أَقَارِبَهَا", "أَقَارِبَكَ", "أَقَارِبِي"], "Their relatives.", tr="People visit their relatives at the holidays."),
    ],
    verify=(vv("قبل#10", "pres", huwa="يَسْتَقْبِل") + vv("بقي", "pres", huwa="يَبْقَى") + vv("نسي", "pres", huwa="يَنْسَى") + vv("دعو", "pres", huwa="يَدْعُو") + vv("زور", "pres", huwa="يَزُور") + vv("شكر", "pres", huwa="يَشْكُر")
            + vw("ضَيْف", "الضَّيْف", "ضُيُوف", "الضُّيُوف", "ضِيَافَة", "صَاحِب", "زِيَارَة", "أَقَارِب", "أَقَارِبَهُمْ", "قَهْوَة", "الْقَهْوَة", "عَصِير", "الْعَصِير", "تُقَدَّم", "الْبُيُوت", "الْأَعْيَاد", "سَاعَتَيْن", "الْعَشَاء", "جَار", "قَرِيب", "يَسْتَقْبَل", "اِسْتَقْبِلْ", "يَقْبَل", "يَبْقِي", "أَقَارِبَهَا", "أَقَارِبَكَ", "أَقَارِبِي", "أَوِ")),
)

# ---------------------------------------------------------------------------- 309
L309 = lesson(
    "Holidays and greetings",
    "رَمَضَان · عِيد الْفِطْر · عِيد الْأَضْحَى · كُلّ عَام وَأَنْتُمْ بِخَيْر",
    requires=["عيد", "فطر", "أضحى", "صوم", "ميلاد", "شهر", "هدية", "مبارك", "سنة", "مسلم", "مسيحي"],
    cards=[
        card("The main holidays",
             "Muslim holidays follow the Hijri lunar calendar, so their dates move about ten or eleven days earlier each year in the Gregorian calendar. "
             "رَمَضَان is the month of fasting; عِيد الْفِطْر is the festival that follows it; عِيد الْأَضْحَى is the other major Muslim festival. "
             "Christians celebrate عِيد الْمِيلَاد (Christmas) and عِيد الْفِصْح (Easter). Many countries also have a national day.",
             tables=[table(["English", "Arabic"],
                           [["Ramadan", "رَمَضَان"], ["the festival after Ramadan", "عِيد الْفِطْر"], ["the festival of sacrifice", "عِيد الْأَضْحَى"], ["Christmas", "عِيد الْمِيلَاد"], ["Easter", "عِيد الْفِصْح"],
                            ["New Year", "رَأْس السَّنَة"], ["national day", "الْعِيد الْوَطَنِيّ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("What people do and say",
             "The verb يَحْتَفِل (celebrates) is Measure VIII and يَصُوم (fasts) is a hollow verb. A common greeting for any festival is «كُلّ عَام وَأَنْتُمْ بِخَيْر», literally “every year and you are well”.",
             examples=[
                 ex("يَصُوم كَثِير مِنَ الْمُسْلِمِين فِي شَهْر رَمَضَان.", "Many Muslims fast in the month of Ramadan.", "يَصُوم"),
                 ex("يَحْتَفِل النَّاس بِعِيد الْفِطْر بَعْد رَمَضَان.", "People celebrate the festival of Eid al-Fitr after Ramadan.", "يَحْتَفِل"),
                 ex("يَحْصُل بَعْض الْأَطْفَال عَلَى هَدَايَا فِي الْعِيد.", "Some children get gifts at the festival.", "هَدَايَا"),
                 ex("يَحْتَفِل الْمَسِيحِيُّون بِعِيد الْمِيلَاد.", "Christians celebrate Christmas.", "الْمَسِيحِيُّون"),
                 ex("نَقُول فِي الْعِيد: «عِيد مُبَارَك!»", "At the festival we say: “Blessed festival!”", "مُبَارَك"),
                 ex("تَتَغَيَّر تَوَارِيخ الْأَعْيَاد الْإِسْلَامِيَّة كُلّ سَنَة.", "The dates of the Islamic festivals change every year.", "تَتَغَيَّر"),
             ]),
    ],
    exercises=[
        M("Which is the month of fasting?", "رَمَضَان", ["شَوَّال", "الْمِيلَاد", "الْفِصْح"], "رَمَضَان."),
        M("Which festival follows Ramadan?", "عِيد الْفِطْر", ["عِيد الْمِيلَاد", "رَأْس السَّنَة", "الْعِيد الْوَطَنِيّ"], "عِيد الْفِطْر."),
        M("What does عِيد الْمِيلَاد mean?", "Christmas", ["Easter", "New Year", "National Day"], "مِيلَاد = birth."),
        M("What does كُلّ عَام وَأَنْتُمْ بِخَيْر express?", "a festival greeting", ["a question about health", "a request for money", "an apology"], "A wish for the whole year."),
        M("Why do the dates of Muslim festivals move through the year?", "the Hijri calendar is lunar", ["they are decided each week", "they follow the school year", "they follow the harvest"], "A lunar year is about eleven days shorter than a solar year."),
        M("What does يَحْتَفِل النَّاس بِعِيد الْفِطْر mean?", "People celebrate Eid al-Fitr", ["People forget Eid al-Fitr", "People wait for Eid al-Fitr", "People travel at Eid al-Fitr"], "يَحْتَفِل = celebrates."),
        F("___ كَثِير مِنَ الْمُسْلِمِين فِي شَهْر رَمَضَان.", "يَصُوم", ["يَصِيم", "صَامَ", "يَصُومُون"], "A masculine plural people subject takes a singular verb before it.", tr="Many Muslims fast in the month of Ramadan.", lemma="صوم:pres:huwa"),
        F("___ النَّاس بِعِيد الْفِطْر بَعْد رَمَضَان.", "يَحْتَفِل", ["يَحْتَفِلُون", "اِحْتَفَلَ", "تَحْتَفِل"], "A singular verb before a plural of people.", tr="People celebrate the festival of Eid al-Fitr after Ramadan.", lemma="حفل#8:pres:huwa"),
        F("نَقُول فِي الْعِيد: «___ مُبَارَك!»", "عِيد", ["قَمِيص", "جَوَاز", "خُبْز"], "The greeting is عِيد مُبَارَك.", tr="At the festival we say: “Blessed festival!”"),
    ],
    verify=(vv("صوم", "pres", huwa="يَصُوم", hum="يَصُومُون") + vv("صوم", "past", huwa="صَامَ") + vv("حفل#8", "pres", huwa="يَحْتَفِل", hum="يَحْتَفِلُون") + vv("حفل#8", "past", huwa="اِحْتَفَلَ")
            + vw("رَمَضَان", "عِيد", "الْفِطْر", "الْأَضْحَى", "الْمِيلَاد", "الْفِصْح", "رَأْس", "السَّنَة", "الْوَطَنِيّ", "الْمُسْلِمُون", "الْمَسِيحِيُّون", "الْأَطْفَال", "هَدَايَا", "مُبَارَك", "تَتَغَيَّر", "تَوَارِيخ", "الْأَعْيَاد", "الْإِسْلَامِيَّة", "شَوَّال", "يَصُومُون", "تَحْتَفِل", "يَحْتَفِلُون", "عَام", "بِخَيْر", "يَأْخُذ")),
)

# ---------------------------------------------------------------------------- 310
L310 = lesson(
    "Traditional dress",
    "ثَوْب · عَبَاءَة · كُوفِيَّة · جَلَّابِيَّة",
    requires=["ثوب", "لباس", "تقليدي", "حجاب", "أبيض", "أسود", "نساء", "لبس", "خفيف", "مناسبة", "زي"],
    cards=[
        card("Names of clothes",
             "Traditional dress differs a great deal from one country to another, and many people today wear modern clothes every day and traditional dress on special occasions. "
             "Here are a few well-known pieces. The verb لَبِسَ (he wore) and the Measure VIII verb اِرْتَدَى (he put on) both mean “wear”.",
             tables=[table(["English", "Arabic"],
                           [["traditional dress", "لِبَاس تَقْلِيدِيّ"], ["a long robe (thawb)", "ثَوْب"], ["a long cloak (abaya)", "عَبَاءَة"], ["a headscarf", "حِجَاب"], ["a checked head cloth (kufiyya)", "كُوفِيَّة"],
                            ["a hooded robe (djellaba)", "جَلَّابِيَّة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Who wears what, and where",
             "These are broad descriptions. Use بَعْض (some) and كَثِير مِنَ (many of) to avoid saying that everybody does the same.",
             examples=[
                 ex("يَلْبَس كَثِير مِنَ الرِّجَال فِي الْخَلِيج ثَوْبًا أَبْيَض.", "Many men in the Gulf wear a white thawb.", "يَلْبَس"),
                 ex("تَلْبَس بَعْض النِّسَاء عَبَاءَة سَوْدَاء.", "Some women wear a black abaya.", "تَلْبَس"),
                 ex("فِي الْمَغْرِب يَلْبَس كَثِير مِنَ النَّاس جَلَّابِيَّة.", "In Morocco many people wear a djellaba.", "جَلَّابِيَّة"),
                 ex("يَرْتَدِي بَعْض الرِّجَال كُوفِيَّة عَلَى رَأْسِهِمْ.", "Some men wear a kufiyya on their heads.", "يَرْتَدِي"),
                 ex("تَخْتَلِف الْمَلَابِس التَّقْلِيدِيَّة مِنْ بَلَد إِلَى بَلَد.", "Traditional clothes differ from one country to another.", "تَخْتَلِف"),
                 ex("فِي الصَّيْف يَلْبَس النَّاس مَلَابِس خَفِيفَة.", "In summer people wear light clothes.", "خَفِيفَة"),
             ]),
    ],
    exercises=[
        M("What is a ثَوْب?", "a long robe", ["a hat", "a pair of shoes", "a belt"], "ثَوْب = robe."),
        M("What is a جَلَّابِيَّة?", "a hooded robe", ["a headscarf", "a coat of metal", "a pair of trousers"], "جَلَّابِيَّة = djellaba."),
        M("What does يَلْبَس mean?", "he wears", ["he buys", "he sells", "he washes"], "لَبِسَ = to wear."),
        M("What does تَخْتَلِف الْمَلَابِس مِنْ بَلَد إِلَى بَلَد mean?", "Clothes differ from one country to another", ["Clothes are the same everywhere", "Clothes are expensive in one country", "A country has clothes"], "تَخْتَلِف = differs."),
        M("Why does the lesson use بَعْض and كَثِير مِنَ?", "to avoid saying that everyone does the same", ["to count people exactly", "because they are plural nouns", "to ask a question"], "Descriptions are general."),
        M("What does فِي الصَّيْف يَلْبَس النَّاس مَلَابِس خَفِيفَة mean?", "In summer people wear light clothes", ["In winter people wear robes", "In summer people sell clothes", "The summer is light"], "خَفِيفَة = light."),
        F("يَلْبَس كَثِير مِنَ الرِّجَال فِي الْخَلِيج ___ أَبْيَض.", "ثَوْبًا", ["عَبَاءَة", "فُسْتَانًا", "جَلَّابِيَّة"], "The translation says thawb; a dress is not worn by men, and عَبَاءَة is feminine, so أَبْيَض would not agree.", tr="Many men in the Gulf wear a white thawb."),
        F("___ بَعْض النِّسَاء عَبَاءَة سَوْدَاء.", "تَلْبَس", ["يَلْبَس", "أَلْبَس", "نَلْبَس"], "Feminine subject (بَعْض النِّسَاء).", tr="Some women wear a black abaya.", lemma="لبس:pres:hiya"),
        F("تَخْتَلِف الْمَلَابِس ___ مِنْ بَلَد إِلَى بَلَد.", "التَّقْلِيدِيَّة", ["التَّقْلِيدِيّ", "التَّقْلِيدِيُّون", "التَّقْلِيدِيَّتَان"], "Plural things → feminine singular adjective.", tr="Traditional clothes differ from one country to another."),
    ],
    verify=(vv("لبس", "pres", huwa="يَلْبَس", hiya="تَلْبَس") + vv("لبس", "past", huwa="لَبِسَ") + vv("خلف#8", "pres", hiya="تَخْتَلِف")
            + vw("ثَوْب", "ثَوْبًا", "عَبَاءَة", "حِجَاب", "فُسْتَانًا", "كُوفِيَّة", "جَلَّابِيَّة", "لِبَاس", "تَقْلِيدِيّ", "الرِّجَال", "الْخَلِيج", "أَبْيَض", "سَوْدَاء", "النِّسَاء", "الْمَغْرِب", "يَرْتَدِي", "اِرْتَدَى", "رَأْسِهِمْ", "الْمَلَابِس", "التَّقْلِيدِيَّة", "بَلَد", "خَفِيفَة", "التَّقْلِيدِيّ", "التَّقْلِيدِيُّون", "التَّقْلِيدِيَّتَان", "أَلْبَس", "نَلْبَس")),
)

# ---------------------------------------------------------------------------- 311
L311 = lesson(
    "Peoples and religions of the Arab world",
    "مُعْظَم السُّكَّان عَرَب، وَهُنَاك أَيْضًا أَمَازِيغ وَأَكْرَاد",
    requires=["عرب", "كردي", "مسلم", "مسيحي", "طائفة", "أقلية", "دين", "لغة", "معظم", "شمال"],
    cards=[
        card("Many communities",
             "The Arab world is home to people of many backgrounds. In most countries the majority are Arabs who speak Arabic, and there are also communities such as الْأَمَازِيغ (the Amazigh, in North Africa) and الْأَكْرَاد (the Kurds). "
             "Most people are Muslim, and there are also Christians and other communities. These are broad facts; every country has its own mix.",
             tables=[table(["English", "Arabic"],
                           [["the Arabs", "الْعَرَب"], ["the Amazigh", "الْأَمَازِيغ"], ["the Kurds", "الْأَكْرَاد"], ["Muslims", "الْمُسْلِمُون"], ["Christians", "الْمَسِيحِيُّون"],
                            ["the majority", "الْأَكْثَرِيَّة"], ["a minority", "أَقَلِّيَّة"], ["a community", "طَائِفَة"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Describing a population",
             "Use relative clauses, as in chapter 17, to say who speaks what. Notice the returning pronoun in اللُّغَة الَّتِي يَتَكَلَّم بِهَا.",
             examples=[
                 ex("فِي مُعْظَم الْبِلَاد الْعَرَبِيَّة الْعَرَب هُمُ الْأَكْثَرِيَّة.", "In most Arab countries the Arabs are the majority.", "الْأَكْثَرِيَّة"),
                 ex("يَعِيش الْأَمَازِيغ فِي شَمَال أَفْرِيقِيَا.", "The Amazigh live in North Africa.", "الْأَمَازِيغ"),
                 ex("يَعِيش الْأَكْرَاد فِي الْعِرَاق وَسُورِيَا وَتُرْكِيَا وَإِيرَان.", "The Kurds live in Iraq, Syria, Turkey and Iran.", "الْأَكْرَاد"),
                 ex("مُعْظَم السُّكَّان مُسْلِمُون، وَيُوجَد أَيْضًا مَسِيحِيُّون.", "Most of the people are Muslims, and there are also Christians.", "يُوجَد"),
                 ex("الْعَرَبِيَّة هِيَ اللُّغَة الَّتِي يَتَكَلَّم بِهَا مُعْظَم النَّاس فِي الْبِلَاد الْعَرَبِيَّة.", "Arabic is the language that most people in the Arab countries speak.", "بِهَا"),
                 ex("تَحْتَفِظ جَمَاعَات كَثِيرَة بِلُغَتِهَا.", "Many groups keep their language.", "تَحْتَفِظ"),
             ]),
    ],
    exercises=[
        M("Who are الْأَمَازِيغ?", "the Amazigh of North Africa", ["the people of the Gulf", "the Kurds of Iraq", "the travellers of Asia"], "الْأَمَازِيغ."),
        M("Who are الْأَكْرَاد?", "the Kurds", ["the Arabs", "the Christians", "the Amazigh"], "الْأَكْرَاد."),
        M("What does أَقَلِّيَّة mean?", "a minority", ["the majority", "a country", "a religion"], "أَقَلّ = less."),
        M("What does مُعْظَم mean?", "most", ["some", "none", "all"], "مُعْظَم النَّاس = most people."),
        M("What does تَحْتَفِظ جَمَاعَات كَثِيرَة بِلُغَتِهَا mean?", "Many groups keep their language", ["Many groups forget their language", "Many groups celebrate a language", "One group has a language"], "تَحْتَفِظ بِـ = keeps."),
        M("In اللُّغَة الَّتِي يَتَكَلَّم بِهَا, what is the job of بِهَا؟", "the returning pronoun بِهَا points back to اللُّغَة", ["بِهَا is the subject", "it makes the verb passive", "it shows the past"], "A feminine returning pronoun."),
        F("يَعِيش ___ فِي شَمَال أَفْرِيقِيَا.", "الْأَمَازِيغ", ["الْأَكْرَاد", "الْهُنُود", "السُّيَّاح"], "The Amazigh live in North Africa.", tr="The Amazigh live in North Africa."),
        F("الْعَرَبِيَّة هِيَ اللُّغَة ___ يَتَكَلَّم بِهَا مُعْظَم النَّاس فِي الْبِلَاد الْعَرَبِيَّة.", "الَّتِي", ["الَّذِي", "الَّذِين", "اللَّاتِي"], "اللُّغَة is feminine singular.", tr="Arabic is the language that most people in the Arab countries speak."),
        F("مُعْظَم السُّكَّان ___، وَيُوجَد أَيْضًا مَسِيحِيُّون.", "مُسْلِمُون", ["مُسْلِمَة", "مُسْلِم", "مُسْلِمَات"], "Plural men and women together.", tr="Most of the people are Muslims, and there are also Christians."),
    ],
    verify=(vv("عيش", "pres", huwa="يَعِيش") + vv("حفظ#8", "pres", hiya="تَحْتَفِظ")
            + vw("الْعَرَب", "الْأَمَازِيغ", "الْأَكْرَاد", "الْمُسْلِمُون", "مُسْلِمُون", "الْمَسِيحِيُّون", "مَسِيحِيُّون", "الْأَكْثَرِيَّة", "أَقَلِّيَّة", "طَائِفَة", "مُعْظَم", "السُّكَّان", "أَيْضًا", "الْعِرَاق", "سُورِيَا", "تُرْكِيَا", "إِيرَان", "جَمَاعَة", "بِلُغَتِهَا", "وَعَادَاتِهَا", "يَتَكَلَّمُ", "بِهَا", "السُّيَّاح", "مُسْلِمَة", "مُسْلِم", "مُسْلِمَات", "أَقَلّ")),
)

# ---------------------------------------------------------------------------- 312
L312 = lesson(
    "Weddings",
    "دَعَانِي صَدِيقِي إِلَى زِفَافِهِ · مَبْرُوك!",
    requires=["زفاف", "عروس", "عريس", "زواج", "حفلة", "دعوة", "هدية", "حضر", "مبروك", "أهل"],
    cards=[
        card("Wedding words",
             "A wedding is زِفَاف or عُرْس or زَوَاج. The bride is عَرُوس and the groom is عَرِيس. The congratulation is مَبْرُوك. "
             "Wedding customs vary widely: some weddings are a single evening and others last several days, so these sentences stay general.",
             tables=[table(["English", "Arabic"],
                           [["wedding", "زِفَاف"], ["wedding party", "حَفْلَة الزِّفَاف"], ["bride", "عَرُوس"], ["groom", "عَرِيس"], ["invitation", "دَعْوَة"], ["gift", "هَدِيَّة"], ["Congratulations!", "مَبْرُوك"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Going to a wedding",
             "The verbs you know from this chapter fit this topic: دَعَا (invite), حَضَرَ (attend), اِحْتَفَلَ (celebrate). These sentences are invented.",
             examples=[
                 ex("دَعَانِي صَدِيقِي إِلَى زِفَافِهِ.", "My friend invited me to his wedding.", "دَعَانِي"),
                 ex("يَحْضُر الْأَهْل وَالْأَصْدِقَاء حَفْلَة الزِّفَاف.", "The family and friends attend the wedding party.", "يَحْضُر"),
                 ex("تَلْبَس الْعَرُوس فُسْتَانًا جَمِيلًا.", "The bride wears a beautiful dress.", "الْعَرُوس"),
                 ex("يُقَدِّم الضُّيُوف هَدَايَا لِلْعَرُوس وَالْعَرِيس.", "The guests give gifts to the bride and groom.", "هَدَايَا"),
                 ex("فِي بَعْض الْبِلَاد تَبْقَى الْحَفْلَة عِدَّة أَيَّام.", "In some countries the party lasts several days.", "تَبْقَى"),
                 ex("نَقُول لِلْعَرِيس وَالْعَرُوس: «مَبْرُوك!»", "We say to the groom and the bride: “Congratulations!”", "مَبْرُوك"),
             ]),
    ],
    exercises=[
        M("Who is the عَرُوس?", "the bride", ["the groom", "the guest", "the host"], "عَرُوس = bride."),
        M("Who is the عَرِيس?", "the groom", ["the bride", "the cook", "the friend"], "عَرِيس = groom."),
        M("What do you say to a couple?", "مَبْرُوك", ["شُكْرًا", "عَفْوًا", "مَعَ السَّلَامَة"], "مَبْرُوك = congratulations."),
        M("What does دَعَانِي صَدِيقِي إِلَى زِفَافِهِ mean?", "My friend invited me to his wedding", ["I invited my friend to his wedding", "My friend forgot his wedding", "My friend attended my wedding"], "دَعَانِي = he invited me."),
        M("What does تَبْقَى الْحَفْلَة عِدَّة أَيَّام mean?", "The party lasts several days", ["The party is on Tuesday", "The party is tomorrow", "The party ended early"], "عِدَّة أَيَّام = several days."),
        M("Why does the lesson stay general?", "wedding customs differ a lot", ["weddings are rare", "weddings are illegal", "only one custom exists"], "Customs vary."),
        F("___ صَدِيقِي إِلَى زِفَافِهِ.", "دَعَانِي", ["دَعَوْتُهُ", "دَعَتْنِي", "يَدْعُونِي"], "He invited me.", tr="My friend invited me to his wedding."),
        F("___ الْأَهْل وَالْأَصْدِقَاء حَفْلَة الزِّفَاف.", "يَحْضُر", ["تَحْضُر", "أَحْضُر", "نَحْضُر"], "Masculine subject (people), verb first.", tr="The family and friends attend the wedding party.", lemma="حضر:pres:huwa"),
        F("نَقُول لِلْعَرِيس وَالْعَرُوس: «___!»", "مَبْرُوك", ["مَرْحَبًا", "تَفَضَّلْ", "عَفْوًا"], "Congratulations.", tr="We say to the groom and the bride: “Congratulations!”"),
    ],
    verify=(vv("حضر", "pres", huwa="يَحْضُر") + vv("لبس", "pres", hiya="تَلْبَس") + vv("بقي", "pres", hiya="تَبْقَى")
            + vw("زِفَاف", "زِفَافِهِ", "الزِّفَاف", "عُرْس", "زَوَاج", "عَرُوس", "الْعَرُوس", "عَرِيس", "الْعَرِيس", "دَعْوَة", "هَدِيَّة", "هَدَايَا", "مَبْرُوك", "حَفْلَة", "الْحَفْلَة", "الْأَهْل", "الْأَصْدِقَاء", "جَمِيلًا", "عِدَّة", "أَيَّام", "دَعَانِي", "دَعَوْتُهُ", "دَعَتْنِي", "يَدْعُونِي", "حَضَرَ", "تَحْضُر", "أَحْضُر", "نَحْضُر", "مَرْحَبًا", "عَفْوًا", "مَعَ", "السَّلَامَة", "تَفَضَّلْ")),
)

# ---------------------------------------------------------------------------- 313
L313 = lesson(
    "Cards and emails",
    "عَزِيزِي خَالِد · مَعَ أَطْيَب التَّمَنِّيَات",
    requires=["تحية", "عزيز", "تهنئة", "هدية", "رسالة", "بريد", "إلكتروني", "شكر", "زفاف", "مبروك"],
    cards=[
        card("Opening and closing",
             "A friendly email or card has a greeting at the top, the message, and a closing. For a man write عَزِيزِي; for a woman, عَزِيزَتِي. Common closings are مَعَ تَحِيَّاتِي (with my greetings) and مَعَ أَطْيَب التَّمَنِّيَات (with best wishes).",
             tables=[table(["Part", "Arabic"],
                           [["Dear (man)", "عَزِيزِي"], ["Dear (woman)", "عَزِيزَتِي"], ["Peace be upon you", "السَّلَام عَلَيْكَ"], ["Warmest congratulations", "أَطْيَب التَّهَانِي"], ["With my greetings", "مَعَ تَحِيَّاتِي"],
                            ["With best wishes", "مَعَ أَطْيَب التَّمَنِّيَات"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("An invented email",
             "A friend answers a wedding invitation. The people and the message are made up.",
             examples=[
                 ex("عَزِيزِي خَالِد، السَّلَام عَلَيْكَ.", "Dear Khalid, peace be upon you.", "عَزِيزِي"),
                 ex("شُكْرًا لِدَعْوَتِكَ إِلَى حَفْلَة الزِّفَاف.", "Thank you for your invitation to the wedding party.", "شُكْرًا"),
                 ex("سَأَحْضُر مَعَ أَخِي إِنْ شَاءَ اللَّه.", "I will attend with my brother, God willing.", "سَأَحْضُر"),
                 ex("مَبْرُوك! أَطْيَب التَّهَانِي لَكَ وَلِلْعَرُوس.", "Congratulations! Warmest congratulations to you and to the bride.", "أَطْيَب التَّهَانِي"),
                 ex("وَسَأُرْسِل لَكُمَا هَدِيَّة صَغِيرَة.", "And I will send you both a small gift.", "هَدِيَّة"),
                 ex("مَعَ أَطْيَب التَّمَنِّيَات، يُوسُف.", "With best wishes, Yusuf.", "مَعَ أَطْيَب التَّمَنِّيَات"),
             ]),
    ],
    exercises=[
        M("How do you open an email to a man called Khalid?", "عَزِيزِي خَالِد", ["عَزِيزَتِي خَالِد", "مَعَ تَحِيَّاتِي خَالِد", "مَبْرُوك خَالِد"], "عَزِيزِي = my dear (m.)."),
        M("How do you open a card to a woman?", "عَزِيزَتِي", ["عَزِيزِي", "عَزِيزُهُ", "مَعَ تَحِيَّاتِي"], "عَزِيزَتِي = my dear (f.)."),
        M("What does مَعَ أَطْيَب التَّمَنِّيَات mean?", "with best wishes", ["with best thanks", "with my apologies", "with many questions"], "تَمَنِّيَات = wishes."),
        M("What does أَطْيَب التَّهَانِي express?", "warmest congratulations", ["best regards", "good night", "many thanks"], "تَهَانِي = congratulations."),
        M("What does سَأَحْضُر مَعَ أَخِي mean?", "I will attend with my brother", ["I attended with my brother", "My brother will attend", "I did not see my brother"], "سَـ = will."),
        M("Where does the closing go?", "at the end", ["at the top", "after the date only", "in the subject line"], "Closings end the message."),
        F("___ خَالِد، السَّلَام عَلَيْكَ.", "عَزِيزِي", ["عَزِيزَتِي", "عَزِيزَيْنِ", "عَزِيزُونَ"], "Khalid is a man.", tr="Dear Khalid, peace be upon you."),
        F("مَبْرُوك! أَطْيَب ___ لَكَ وَلِلْعَرُوس.", "التَّهَانِي", ["الْأَسْمَاء", "التَّحِيَّات", "الْأَيَّام"], "The translation says congratulations, so the word is التَّهَانِي.", tr="Congratulations! Warmest congratulations to you and to the bride."),
        F("___ أَطْيَب التَّمَنِّيَات، يُوسُف.", "مَعَ", ["بَعْد", "قَبْل", "عَنْ"], "The usual closing starts with مَعَ.", tr="With best wishes, Yusuf."),
    ],
    verify=(vv("حضر", "pres", ana="أَحْضُر")
            + vw("عَزِيزِي", "عَزِيزَتِي", "السَّلَام", "عَلَيْكَ", "لِدَعْوَتِكَ", "الزِّفَاف", "حَفْلَة", "سَأَحْضُر", "اللَّه", "أَطْيَب", "التَّهَانِي", "وَلِلْعَرُوس", "وَسَأُرْسِل", "لَكُمَا", "هَدِيَّة", "تَحِيَّاتِي", "التَّمَنِّيَات", "يُوسُف", "خَالِد", "التَّحِيَّات", "الْأَسْمَاء", "عَزِيزَيْنِ", "عَزِيزُونَ")),
)

# ---------------------------------------------------------------------------- 314
L314 = lesson(
    "Giving a short talk: Lebanon",
    "سَأَتَحَدَّث الْيَوْم عَنْ لُبْنَان · شُكْرًا عَلَى اِسْتِمَاعِكُمْ",
    requires=["تحدث", "عاصمة", "لغة", "رسمي", "مسلم", "مسيحي", "ثم", "عن"],
    cards=[
        card("The shape of a talk",
             "A short talk has an opening (سَأَتَحَدَّث عَنْ…, “I will talk about…”), points in order (أَوَّلًا, ثَانِيًا, ثَالِثًا, or ثُمَّ), and a closing (شُكْرًا عَلَى اِسْتِمَاعِكُمْ, “thank you for listening”). "
             "Use the structures of the chapter: يَقَع for place, relative clauses for details.",
             tables=[table(["Part", "Arabic"],
                           [["opening", "سَأَتَحَدَّث الْيَوْم عَنْ"], ["first point", "أَوَّلًا"], ["second point", "ثَانِيًا"], ["third point", "ثَالِثًا"], ["closing", "شُكْرًا عَلَى اِسْتِمَاعِكُمْ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A talk about Lebanon (basic facts)",
             "These facts are standard reference facts, kept simple.",
             examples=[
                 ex("سَأَتَحَدَّث الْيَوْم عَنْ لُبْنَان.", "Today I will talk about Lebanon.", "سَأَتَحَدَّث"),
                 ex("أَوَّلًا، لُبْنَان دَوْلَة عَرَبِيَّة صَغِيرَة تَقَع عَلَى الْبَحْر الْمُتَوَسِّط.", "First, Lebanon is a small Arab country that lies on the Mediterranean Sea.", "تَقَع"),
                 ex("عَاصِمَة لُبْنَان هِيَ بَيْرُوت.", "The capital of Lebanon is Beirut.", "بَيْرُوت"),
                 ex("ثَانِيًا، يَعِيش فِي لُبْنَان مُسْلِمُون وَمَسِيحِيُّون.", "Second, Muslims and Christians live in Lebanon.", "يَعِيش"),
                 ex("ثَالِثًا، اللُّغَة الرَّسْمِيَّة هِيَ الْعَرَبِيَّة.", "Third, the official language is Arabic.", "الرَّسْمِيَّة"),
                 ex("شُكْرًا عَلَى اِسْتِمَاعِكُمْ.", "Thank you for listening.", "اِسْتِمَاعِكُمْ"),
             ]),
    ],
    exercises=[
        M("How does the talk begin?", "سَأَتَحَدَّث الْيَوْم عَنْ لُبْنَان", ["شُكْرًا عَلَى اِسْتِمَاعِكُمْ", "أَوَّلًا وَأَخِيرًا", "مَعَ تَحِيَّاتِي"], "Opening: I will talk about…"),
        M("What is the capital of Lebanon?", "Beirut", ["Cairo", "Amman", "Rabat"], "بَيْرُوت."),
        M("What is the official language of Lebanon?", "Arabic", ["French only", "Persian", "Armenian"], "الْعَرَبِيَّة."),
        M("Which sea does Lebanon lie on?", "the Mediterranean", ["the Red Sea", "the Arabian Gulf", "the Black Sea"], "الْبَحْر الْمُتَوَسِّط."),
        M("What does شُكْرًا عَلَى اِسْتِمَاعِكُمْ mean?", "Thank you for listening", ["Thank you for your gift", "Thank you for waiting", "Thank you for coming"], "اِسْتِمَاع = listening."),
        M("What is the order of the points?", "أَوَّلًا، ثَانِيًا، ثَالِثًا", ["ثَالِثًا، أَوَّلًا، ثَانِيًا", "ثَانِيًا، ثَالِثًا، أَوَّلًا", "أَوَّلًا، ثَالِثًا، ثَانِيًا"], "First, second, third."),
        F("___ الْيَوْم عَنْ لُبْنَان.", "سَأَتَحَدَّث", ["تَحَدَّثْتُ", "أَتَحَدَّث", "تَحَدَّثَ"], "I will talk.", tr="Today I will talk about Lebanon."),
        F("لُبْنَان دَوْلَة عَرَبِيَّة صَغِيرَة ___ عَلَى الْبَحْر الْمُتَوَسِّط.", "تَقَع", ["يَقَع", "تَجِد", "وَقَفَ"], "Feminine (دَوْلَة).", tr="Lebanon is a small Arab country that lies on the Mediterranean Sea.", lemma="وقع:pres:hiya"),
        F("ثَالِثًا، اللُّغَة ___ هِيَ الْعَرَبِيَّة.", "الرَّسْمِيَّة", ["الرَّسْمِيّ", "الرَّسْمِيُّون", "الرَّسْمِيَّتَان"], "Feminine singular, like اللُّغَة.", tr="Third, the official language is Arabic."),
    ],
    verify=(vv("وقع", "pres", hiya="تَقَع") + vv("عيش", "pres", huwa="يَعِيش")
            + vw("سَأَتَحَدَّث", "تَحَدَّثْتُ", "أَتَحَدَّث", "تَحَدَّثَ", "لُبْنَان", "أَوَّلًا", "ثَانِيًا", "ثَالِثًا", "اِسْتِمَاعِكُمْ", "بَيْرُوت", "الرَّسْمِيَّة", "الرَّسْمِيّ", "الرَّسْمِيُّون", "الرَّسْمِيَّتَان", "عَاصِمَة", "تَجِد", "وَقَفَ", "الْمُتَوَسِّط")),
)

# ---------------------------------------------------------------------------- 315
L315 = lesson(
    "Review: customs, verbs and nouns",
    "يَدْعُو · يَنْسَى · يَحْتَفِل · يَسْتَخْدِم",
    requires=["دعا", "نسي", "مشى", "جمع", "نظر", "خدم", "عيد", "ضيف", "زفاف", "حفلة"],
    cards=[
        card("What to remember",
             "Defective verbs: the present ends in ـِي, ـُو or ـَى (يَمْشِي, يَدْعُو, يَنْسَى), the long vowel drops after لَمْ and in the command (لَا تَنْسَ). "
             "Measure VIII is اِفْتَعَلَ (يَنْتَظِر) with the noun اِفْتِعَال; Measure X is اِسْتَفْعَلَ (يَسْتَخْدِم) with the noun اِسْتِفْعَال.",
             tables=[table(["English", "Arabic"],
                           [["They walk to the party together.", "يَمْشُون إِلَى الْحَفْلَة مَعًا"], ["Do not forget the gift! (to a man)", "لَا تَنْسَ الْهَدِيَّة"], ["The family met at the wedding.", "اِجْتَمَعَتِ الْعَائِلَة فِي الزِّفَاف"],
                            ["Hotels welcome guests.", "تَسْتَقْبِل الْفَنَادِق الضُّيُوف"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("A weekend (an invented practice text)",
             "A short text that mixes the ideas of the chapter.",
             examples=[
                 ex("دَعَانِي صَدِيقِي إِلَى زِفَافِ أُخْتِهِ.", "My friend invited me to his sister’s wedding.", "دَعَانِي"),
                 ex("اِنْتَظَرْتُ أَخِي أَمَامَ الْبَيْت.", "I waited for my brother in front of the house.", "اِنْتَظَرْتُ"),
                 ex("مَشَيْنَا مَعًا إِلَى الْقَاعَة.", "We walked together to the hall.", "مَشَيْنَا"),
                 ex("اِسْتَقْبَلَنَا أَهْل الْعَرُوس بِالْقَهْوَة.", "The bride’s family welcomed us with coffee.", "اِسْتَقْبَلَنَا"),
                 ex("قُلْتُ لِلْعَرِيس: مَبْرُوك! وَلَمْ أَنْسَ الْهَدِيَّة.", "I said to the groom: congratulations! And I did not forget the gift.", "لَمْ أَنْسَ"),
                 ex("اِحْتَفَلَ النَّاس حَتَّى وَقْت مُتَأَخِّر.", "The people celebrated until late.", "اِحْتَفَلَ"),
             ]),
    ],
    exercises=[
        M("Who invited the speaker?", "a friend", ["a brother", "a teacher", "a neighbour"], "دَعَانِي صَدِيقِي."),
        M("Whom did the speaker wait for?", "his brother", ["his friend", "the groom", "the bride"], "اِنْتَظَرْتُ أَخِي."),
        M("How did they go to the hall?", "they walked", ["by car", "by bus", "by plane"], "مَشَيْنَا."),
        M("What did the bride’s family offer?", "coffee", ["tea only", "a gift", "a ticket"], "بِالْقَهْوَة."),
        M("Which is correct for “he did not forget”?", "لَمْ يَنْسَ", ["لَمْ يَنْسَى", "لَنْ يَنْسَ", "لَا يَنْسَ"], "لَمْ + short form."),
        M("Which noun comes from اِسْتَخْدَمَ?", "اِسْتِخْدَام", ["اِفْتِعَال", "اِجْتِمَاع", "اِنْتِظَار"], "X → اِسْتِفْعَال."),
        F("هُمْ ___ إِلَى الْحَفْلَة مَعًا.", "يَمْشُون", ["يَمْشِين", "يَمْشِي", "تَمْشِين"], "They (men) walk.", tr="They walk to the party together.", lemma="مشي:pres:hum"),
        F("لَا ___ الْهَدِيَّة!", "تَنْسَ", ["تَنْسَى", "تَنْسَيْ", "تَنْسَوْا"], "To a man, the long vowel drops.", tr="Do not forget the gift! (to a man)", lemma="نسي:jus:anta"),
        F("___ الْعَائِلَة فِي الزِّفَاف.", "اِجْتَمَعَتِ", ["اِجْتَمَعَ", "جَمَعَتِ", "تَجْتَمِعُ"], "Feminine, past, Measure VIII.", tr="The family met at the wedding."),
    ],
    verify=(vv("مشي", "pres", hum="يَمْشُون") + vv("نسي", "jus", anta="تَنْسَ", ana="أَنْسَ") + vv("جمع#8", "past", hiya="اِجْتَمَعَتْ") + vv("قبل#10", "pres", hiya="تَسْتَقْبِل") + vv("نظر#8", "past", ana="اِنْتَظَرْتُ")
            + vv("مشي", "past", nahnu="مَشَيْنَا") + vv("حفل#8", "past", huwa="اِحْتَفَلَ")
            + vw("دَعَانِي", "زِفَافِ", "أُخْتِهِ", "أَخِي", "الْقَاعَة", "اِسْتَقْبَلَنَا", "الْعَرُوس", "بِالْقَهْوَة", "قُلْتُ", "لِلْعَرِيس", "مَبْرُوك", "الْهَدِيَّة", "مُتَأَخِّر", "اِجْتَمَعَتِ", "جَمَعَتِ", "تَجْتَمِعُ", "الْفَنَادِق", "الضُّيُوف", "اِجْتِمَاع", "اِنْتِظَار", "اِفْتِعَال", "وَقْت")),
)


UNIT = unit("الْعَادَات وَالتَّقَالِيد: customs, defective verbs and Measures VIII and X", [L294, L295, L296, L297, L298, L299, L300, L301, L302, L303, L304, L305, L306, L307, L308, L309, L310, L311, L312, L313, L314, L315])
