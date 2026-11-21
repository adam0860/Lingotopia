"""Unit 11: free time, preferences, hobbies and sports, Measures III and VI, food from Arab countries (all example sentences are original)."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 157
L157 = lesson(
    "Free time",
    "مَاذَا تَفْعَل فِي وَقْت الْفَرَاغ؟ · أُحِبّ الْقِرَاءَة",
    requires=["وقت", "فراغ", "قراءة", "رسم", "موسيقى", "رحلة", "فيلم", "مشي"],
    cards=[
        card("Hobbies",
             "وَقْت الْفَرَاغ is “free time”. Many hobbies are verbal nouns, and they take ال. You "
             "can ask a man مَاذَا تَفْعَل فِي وَقْت الْفَرَاغ؟ and answer with أُحِبّ and a hobby.",
             tables=[table(["English", "Arabic"],
                           [["reading", "الْقِرَاءَة"], ["swimming", "السِّبَاحَة"], ["drawing", "الرَّسْم"], ["cooking", "الطَّبْخ"],
                            ["walking", "الْمَشْيْ"], ["music", "الْمُوسِيقَى"], ["photography", "التَّصْوِير"],
                            ["trips", "الرِّحْلَات"], ["films", "الْأَفْلَام"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("I like…",
             "After أُحِبّ you can put a noun, or أَنْ and a verb. You can say it about other people too: تُحِبّ (she or "
             "you, to a man), نُحِبّ (we), يُحِبّ (he).",
             examples=[
                 ex("مَاذَا تَفْعَل فِي وَقْت الْفَرَاغ؟", "What do you do in your free time? (to a man)", "وَقْت الْفَرَاغ"),
                 ex("أُحِبّ الْقِرَاءَة وَالْمُوسِيقَى.", "I like reading and music.", "أُحِبّ"),
                 ex("أُحِبّ أَنْ أَرْسُم فِي الْحَدِيقَة.", "I like to draw in the park.", "أُحِبّ أَنْ أَرْسُم"),
                 ex("أُخْتِي تُحِبّ السِّبَاحَة فِي الْبَحْر.", "My sister likes swimming in the sea.", "تُحِبّ"),
                 ex("لَا أُحِبّ الطَّبْخ، لَكِنْ أُحِبّ الْمَشْيْ.", "I do not like cooking, but I like walking.", "لَا أُحِبّ"),
                 ex("نُحِبّ أَنْ نَذْهَب فِي رِحْلَة كُلّ شَهْر.", "We like to go on a trip every month.", "نُحِبّ"),
             ]),
    ],
    exercises=[
        M("What does وَقْت الْفَرَاغ mean?", "free time", ["work time", "lunch time", "bedtime"], "فَرَاغ = emptiness, free."),
        M("What does السِّبَاحَة mean?", "swimming", ["reading", "cooking", "walking"], "سَبَحَ = to swim."),
        M("What does الرَّسْم mean?", "drawing", ["music", "photography", "cooking"], "رَسَمَ = to draw."),
        M("Which means “I like reading”?", "أُحِبّ الْقِرَاءَة", ["أُحِبّ الْمَشْيْ", "لَا أُحِبّ الْقِرَاءَة", "تُحِبّ الْقِرَاءَة"], "أُحِبّ = I like."),
        M("Which means “I do not like cooking”?", "لَا أُحِبّ الطَّبْخ", ["أُحِبّ الطَّبْخ", "لَمْ أُحِبّ الطَّبْخ", "لَنْ أُحِبّ الطَّبْخ"], "لَا + present."),
        M("Which means “My sister likes swimming”?", "أُخْتِي تُحِبّ السِّبَاحَة", ["أُخْتِي يُحِبّ السِّبَاحَة", "أَخِي تُحِبّ السِّبَاحَة", "أُخْتِي أُحِبّ السِّبَاحَة"], "She: تُـ."),
        M("Which means “We like to go on a trip”?", "نُحِبّ أَنْ نَذْهَب فِي رِحْلَة", ["أُحِبّ أَنْ أَذْهَب فِي رِحْلَة", "نُحِبّ أَنْ يَذْهَبُوا فِي رِحْلَة", "نُحِبّ الرِّحْلَة"], "نُحِبّ أَنْ + نَذْهَب."),
        F("مَاذَا تَفْعَل فِي وَقْت ___؟ (to a man)", "الْفَرَاغ", ["الْعَمَل", "الْفَرَاغَة", "فَرَاغ"], "“Free time”.", tr="What do you do in your free time?"),
        F("أُحِبّ أَنْ ___ فِي الْحَدِيقَة.", "أَرْسُم", ["رَسَمْتُ", "الرَّسْم", "يَرْسُم"], "After أَنْ, a present verb.", tr="I like to draw in the park."),
    ],
    verify=vv("رسم", "pres", ana="أَرْسُم") + vv("ذهب", "pres", nahnu="نَذْهَب")
    + vw("وَقْت", "الْفَرَاغ", "الْقِرَاءَة", "السِّبَاحَة", "الرَّسْم", "الطَّبْخ", "الْمَشْيْ", "الْمُوسِيقَى", "التَّصْوِير", "الرِّحْلَات", "الْأَفْلَام", "أُحِبّ", "تُحِبّ", "نُحِبّ",
         "الْحَدِيقَة", "رِحْلَة", "لَكِنْ"),
)

# ---------------------------------------------------------------------------- 158
L158 = lesson(
    "I prefer… : أُفَضِّل",
    "أُفَضِّل الشَّايْ عَلَى الْقَهْوَة · أَفْضَل رِيَاضَة",
    requires=["فضل", "أفضل", "رياضة", "فيلم", "لماذا", "قهوة"],
    cards=[
        card("Preferring one thing to another",
             "فَضَّلَ (to prefer) is a Measure II verb, like دَرَّسَ. Its present is أُفَضِّل. You prefer one thing "
             "to another with عَلَى: أُفَضِّل الشَّايْ عَلَى الْقَهْوَة. To ask a choice, use هَلْ and أَمْ (“or”; formal writing often uses أَ instead of هَلْ): "
             "هَلْ تُفَضِّل السِّينَمَا أَمِ الْمَسْرَح؟",
             tables=[table(["Person", "Arabic"],
                           [["I", "أُفَضِّل"], ["we", "نُفَضِّل"], ["you (to a man)", "تُفَضِّل"], ["you (to a woman)", "تُفَضِّلِين"],
                            ["he", "يُفَضِّل"], ["she", "تُفَضِّل"], ["they (men)", "يُفَضِّلُون"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Better and best",
             "أَفْضَل means “better” (with مِنْ for “than”) or “best”. For “the best + noun”, put أَفْضَل in front of a "
             "singular noun without ال: أَفْضَل رِيَاضَة.",
             examples=[
                 ex("أُفَضِّل الشَّايْ عَلَى الْقَهْوَة.", "I prefer tea to coffee.", "عَلَى"),
                 ex("هَلْ تُفَضِّل السِّينَمَا أَمِ الْمَسْرَح؟", "Do you prefer the cinema or the theatre? (to a man)", "أَمِ"),
                 ex("لِمَاذَا تُفَضِّلِين الْمُوسِيقَى؟", "Why do you prefer music? (to a woman)", "تُفَضِّلِين"),
                 ex("أُفَضِّل الْمَشْيْ عَلَى السِّبَاحَة.", "I prefer walking to swimming.", "أُفَضِّل"),
                 ex("هَذَا الْفِيلْم أَفْضَل مِنَ الْفِيلْم الْآخَر.", "This film is better than the other film.", "أَفْضَل مِنَ"),
                 ex("أَفْضَل رِيَاضَة عِنْدِي هِيَ السِّبَاحَة.", "My favourite sport is swimming.", "أَفْضَل رِيَاضَة"),
             ]),
    ],
    exercises=[
        M("What does أُفَضِّل mean?", "I prefer", ["I like", "I try", "I hate"], "فَضَّلَ = to prefer."),
        M("Which means “I prefer tea to coffee”?", "أُفَضِّل الشَّايْ عَلَى الْقَهْوَة", ["أُفَضِّل الْقَهْوَة عَلَى الشَّايْ", "أُفَضِّل الشَّايْ مِنَ الْقَهْوَة", "أُحِبّ الشَّايْ عَلَى الْقَهْوَة"], "أُفَضِّل X عَلَى Y."),
        M("Which means “or” in a question?", "أَمْ", ["لَكِنْ", "ثُمَّ", "مَعَ"], "هَلْ … أَمْ …"),
        M("Which means “Do you prefer the cinema or the theatre?” (to a man)", "هَلْ تُفَضِّل السِّينَمَا أَمِ الْمَسْرَح؟", ["هَلْ تُفَضِّل السِّينَمَا وَالْمَسْرَح؟", "هَلْ أُفَضِّل السِّينَمَا أَمِ الْمَسْرَح؟", "هَلْ تُفَضِّلِين السِّينَمَا أَمِ الْمَسْرَح؟"], "تُفَضِّل = you (to a man)."),
        M("Which means “Why do you prefer music?” (to a woman)", "لِمَاذَا تُفَضِّلِين الْمُوسِيقَى؟", ["لِمَاذَا تُفَضِّل الْمُوسِيقَى؟", "لِمَاذَا يُفَضِّلُون الْمُوسِيقَى؟", "لِمَاذَا أُفَضِّل الْمُوسِيقَى؟"], "ـِين = you (to a woman)."),
        M("Which means “the best sport”?", "أَفْضَل رِيَاضَة", ["الرِّيَاضَة الْأَفْضَل مِنْ", "رِيَاضَة أَفْضَل مِنْ", "فَضَّلَ رِيَاضَة"], "أَفْضَل + singular noun without ال."),
        M("Which means “This film is better than the other film”?", "هَذَا الْفِيلْم أَفْضَل مِنَ الْفِيلْم الْآخَر", ["هَذَا الْفِيلْم أَفْضَل عَلَى الْفِيلْم الْآخَر", "هَذَا الْفِيلْم يُفَضِّل الْفِيلْم الْآخَر", "هَذَا فِيلْم أَفْضَل"], "أَفْضَل مِنْ = better than."),
        F("أُفَضِّل الْمَشْيْ ___ السِّبَاحَة.", "عَلَى", ["مِنَ", "فِي", "مَعَ"], "Prefer X over Y.", tr="I prefer walking to swimming."),
        F("هَذَا الْفِيلْم أَفْضَل ___ الْفِيلْم الْآخَر.", "مِنَ", ["عَلَى", "فِي", "إِلَى"], "Better than.", tr="This film is better than the other film."),
    ],
    verify=vw("أُفَضِّل", "نُفَضِّل", "تُفَضِّل", "تُفَضِّلِين", "يُفَضِّل", "يُفَضِّلُون", "أَمْ", "أَمِ", "السِّينَمَا", "الْمَسْرَح", "أَفْضَل", "الْفِيلْم", "الْآخَر", "الشَّايْ", "رِيَاضَة",
              "لِمَاذَا"),
)

# ---------------------------------------------------------------------------- 159
L159 = lesson(
    "Sports and the places for them",
    "أَلْعَب كُرَة الْقَدَم · النَّادِي · الْمَلْعَب",
    requires=["كرة", "قدم", "نادي", "ملعب", "مباراة", "فريق", "لعب", "سبح"],
    cards=[
        card("Playing sports",
             "You play a ball sport with لَعِبَ: أَلْعَب كُرَة الْقَدَم (“I play football”, literally “the ball of the "
             "foot”). Swimming uses سَبَحَ: أَسْبَح. A sport takes place at a club (نَادِي), a stadium or field (مَلْعَب) "
             "or a swimming pool (مَسْبَح).",
             tables=[table(["English", "Arabic"],
                           [["football", "كُرَة الْقَدَم"], ["basketball", "كُرَة السَّلَّة"], ["club", "النَّادِي"],
                            ["field, stadium", "الْمَلْعَب"], ["swimming pool", "الْمَسْبَح"], ["match", "الْمُبَارَاة"],
                            ["team", "الْفَرِيق"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Sport sentences use the verbs you know, with times and places.",
             examples=[
                 ex("أَلْعَب كُرَة الْقَدَم فِي النَّادِي.", "I play football at the club.", "أَلْعَب"),
                 ex("نَلْعَب كُرَة السَّلَّة يَوْم الْجُمْعَة.", "We play basketball on Friday.", "كُرَة السَّلَّة"),
                 ex("الْمُبَارَاة فِي السَّاعَة السَّابِعَة مَسَاءً.", "The match is at seven in the evening.", "الْمُبَارَاة"),
                 ex("فَرِيقِي يَلْعَب فِي الْمَلْعَب الْكَبِير.", "My team plays in the big stadium.", "فَرِيقِي"),
                 ex("أَسْبَح فِي الْمَسْبَح كُلّ صَبَاح.", "I swim in the pool every morning.", "أَسْبَح"),
                 ex("هَلْ تَلْعَب كُرَة الْقَدَم يَا أَحْمَد؟", "Do you play football, Ahmad?", "هَلْ تَلْعَب"),
             ]),
    ],
    exercises=[
        M("What does كُرَة الْقَدَم mean?", "football", ["basketball", "swimming", "the stadium"], "“The ball of the foot”."),
        M("What does الْمَلْعَب mean?", "stadium, field", ["club", "team", "match"], "لَعِبَ = to play."),
        M("What does الْمَسْبَح mean?", "swimming pool", ["sea", "club", "match"], "سَبَحَ = to swim."),
        M("Which means “I play football at the club”?", "أَلْعَب كُرَة الْقَدَم فِي النَّادِي", ["أَلْعَب كُرَة السَّلَّة فِي النَّادِي", "أَسْبَح فِي النَّادِي", "نَلْعَب كُرَة الْقَدَم فِي النَّادِي"], "أَلْعَب = I play."),
        M("Which means “We play basketball on Friday”?", "نَلْعَب كُرَة السَّلَّة يَوْم الْجُمْعَة", ["أَلْعَب كُرَة السَّلَّة يَوْم الْجُمْعَة", "نَلْعَب كُرَة الْقَدَم يَوْم الْجُمْعَة", "نَلْعَب كُرَة السَّلَّة يَوْم السَّبْت"], "نَـ = we."),
        M("Which means “I swim in the pool every morning”?", "أَسْبَح فِي الْمَسْبَح كُلّ صَبَاح", ["أَسْبَح فِي الْبَحْر كُلّ صَبَاح", "أَلْعَب فِي الْمَسْبَح كُلّ صَبَاح", "أَسْبَح فِي الْمَسْبَح كُلّ مَسَاء"], "سَبَحَ."),
        M("Which means “The match is at seven in the evening”?", "الْمُبَارَاة فِي السَّاعَة السَّابِعَة مَسَاءً", ["الْمُبَارَاة فِي السَّاعَة السَّابِعَة صَبَاحًا", "الْمُبَارَاة فِي السَّاعَة الثَّامِنَة مَسَاءً", "الْفَرِيق فِي السَّاعَة السَّابِعَة مَسَاءً"], "مَسَاءً = in the evening."),
        F("أَلْعَب ___ الْقَدَم فِي النَّادِي.", "كُرَة", ["كُرِيَة", "لَعِبَ", "فَرِيق"], "كُرَة الْقَدَم.", tr="I play football at the club."),
        F("فَرِيقِي ___ فِي الْمَلْعَب الْكَبِير.", "يَلْعَب", ["أَلْعَب", "تَلْعَبِين", "لَعِبْتُ"], "The team: he.", tr="My team plays in the big stadium."),
    ],
    verify=vv("لعب", "pres", ana="أَلْعَب", nahnu="نَلْعَب", anta="تَلْعَب", huwa="يَلْعَب") + vv("سبح", "pres", ana="أَسْبَح")
    + vw("كُرَة", "الْقَدَم", "السَّلَّة", "النَّادِي", "الْمَلْعَب", "الْمَسْبَح", "الْمُبَارَاة", "الْفَرِيق", "فَرِيقِي", "الْجُمْعَة"),
)

# ---------------------------------------------------------------------------- 160
L160 = lesson(
    "Measure III: فَاعَلَ",
    "سَاعَدَ · شَاهَدَ · سَافَرَ · أُسَاعِد",
    requires=["ساعد", "شاهد", "سافر", "قابل", "شارك", "حاول", "وافق", "رافق"],
    cards=[
        card("A long ā after the first letter",
             "Measure III has a long ā after the first root letter. The past is فَاعَلَ (سَاعَدَ, “he helped”) and the "
             "present is يُفَاعِل (يُسَاعِد). The present prefix has ḍamma, like Measure II, but the long ā comes "
             "before the second letter and there is a kasra before the last letter. Many Measure III verbs mean doing something "
             "with someone else.",
             tables=[table(["Meaning", "Past (he)", "Present (I)"],
                           [["to help", "سَاعَدَ", "أُسَاعِد"], ["to watch", "شَاهَدَ", "أُشَاهِد"], ["to travel", "سَافَرَ", "أُسَافِر"],
                            ["to accompany", "رَافَقَ", "أُرَافِق"], ["to meet", "قَابَلَ", "أُقَابِل"],
                            ["to take part", "شَارَكَ", "أُشَارِك"], ["to try", "حَاوَلَ", "أُحَاوِل"], ["to agree", "وَافَقَ", "أُوَافِق"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "The endings are the ones you know. Compare the present of Measure III with Measure II: يُدَرِّس has a "
             "doubled letter, يُسَاعِد has a long ā.",
             examples=[
                 ex("أُسَاعِد أُمِّي فِي الْبَيْت.", "I help my mother at home.", "أُسَاعِد"),
                 ex("نُشَاهِد فِيلْم جَمِيل فِي السِّينَمَا.", "We watch a nice film at the cinema.", "نُشَاهِد"),
                 ex("سَافَرَ أَبِي إِلَى الْأُرْدُنّ أَمْس.", "My father travelled to Jordan yesterday.", "سَافَرَ"),
                 ex("قَابَلْتُ مُدَرِّسِي فِي الْمَكْتَبَة.", "I met my teacher in the library.", "قَابَلْتُ"),
                 ex("هَلْ تُرَافِق أَخِي إِلَى النَّادِي؟", "Are you going with my brother to the club? (to a man)", "تُرَافِق"),
                 ex("أُخْتِي تُشَارِك فِي الْمُبَارَاة.", "My sister takes part in the match.", "تُشَارِك"),
             ]),
    ],
    exercises=[
        M("What does سَاعَدَ mean?", "he helped", ["he watched", "he travelled", "he tried"], "Measure III."),
        M("What does شَاهَدَ mean?", "he watched", ["he helped", "he met", "he agreed"], "شَاهَدَ = to watch, see."),
        M("What does سَافَرَ mean?", "he travelled", ["he accompanied", "he helped", "he returned"], "سَافَرَ = to travel."),
        M("Which is “I help”?", "أُسَاعِد", ["أَسْعَد", "يُسَاعِد", "سَاعَدْتُ"], "أُ + a long ā + a kasra."),
        M("Which is “we watch”?", "نُشَاهِد", ["أُشَاهِد", "تُشَاهِد", "نَشْهَد"], "نُـ = we."),
        M("Which is “you (to a man) accompany”?", "تُرَافِق", ["أُرَافِق", "يُرَافِق", "رَافَقْتَ"], "تُـ."),
        M("Which means “I met my teacher in the library”?", "قَابَلْتُ مُدَرِّسِي فِي الْمَكْتَبَة", ["أُقَابِل مُدَرِّسِي فِي الْمَكْتَبَة", "قَابَلَ مُدَرِّسِي فِي الْمَكْتَبَة", "قَابَلْنَا مُدَرِّسِي فِي الْمَكْتَبَة"], "ـتُ = I (past)."),
        F("___ أَبِي إِلَى الْأُرْدُنّ أَمْس.", "سَافَرَ", ["أُسَافِر", "يُسَافِر", "سَافَرْتُ"], "A past verb for “he”.", tr="My father travelled to Jordan yesterday."),
        F("أُخْتِي ___ فِي الْمُبَارَاة.", "تُشَارِك", ["أُشَارِك", "يُشَارِك", "شَارَكْتُ"], "“She”: تُـ.", tr="My sister takes part in the match."),
    ],
    verify=vw("سَاعَدَ", "شَاهَدَ", "سَافَرَ", "رَافَقَ", "قَابَلَ", "شَارَكَ", "حَاوَلَ", "وَافَقَ", "أُسَاعِد", "أُشَاهِد", "أُسَافِر", "أُرَافِق", "أُقَابِل", "أُشَارِك", "أُحَاوِل", "أُوَافِق",
              "نُشَاهِد", "تُرَافِق", "تُشَارِك", "قَابَلْتُ", "يُسَاعِد", "سَاعَدْتُ", "رَافَقْتَ", "الْأُرْدُنّ", "الْمُبَارَاة"),
)


# ---------------------------------------------------------------------------- 161
L161 = lesson(
    "Measure III: past and future",
    "شَاهَدْتُ · شَاهَدَتْ · سَنُشَاهِد",
    requires=["شاهد", "ساعد", "مباراة", "فيلم", "نادي", "واجب"],
    cards=[
        card("The past of شَاهَدَ",
             "The past endings are the ones you know from كَتَبَ and دَرَسَ. The long ā stays in every form. In the "
             "future, put سَـ in front of the present: سَأُشَاهِد.",
             tables=[table(["Person", "Past", "Future"],
                           [["I", "شَاهَدْتُ", "سَأُشَاهِد"], ["we", "شَاهَدْنَا", "سَنُشَاهِد"],
                            ["you (to a man)", "شَاهَدْتَ", "سَتُشَاهِد"], ["you (to a woman)", "شَاهَدْتِ", "سَتُشَاهِدِين"],
                            ["he", "شَاهَدَ", "سَيُشَاهِد"], ["she", "شَاهَدَتْ", "سَتُشَاهِد"],
                            ["they (men)", "شَاهَدُوا", "سَيُشَاهِدُون"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("شَاهَدْتُ مُبَارَاة كُرَة الْقَدَم أَمْس.", "I watched the football match yesterday.", "شَاهَدْتُ"),
                 ex("هَلْ شَاهَدْتَ هَذَا الْفِيلْم؟", "Did you watch this film? (to a man)", "شَاهَدْتَ"),
                 ex("شَاهَدَتْ أُخْتِي فِيلْم جَمِيل.", "My sister watched a nice film.", "شَاهَدَتْ"),
                 ex("سَنُشَاهِد الْمُبَارَاة فِي النَّادِي غَدًا.", "We will watch the match at the club tomorrow.", "سَنُشَاهِد"),
                 ex("لَنْ أُشَاهِد التِّلْفَاز اللَّيْلَة.", "I will not watch television tonight.", "لَنْ أُشَاهِد"),
                 ex("سَاعَدَنِي أَخِي فِي الْوَاجِب.", "My brother helped me with the homework.", "سَاعَدَنِي"),
             ]),
    ],
    exercises=[
        M("Which means “I watched”?", "شَاهَدْتُ", ["أُشَاهِد", "شَاهَدَ", "شَاهَدْنَا"], "ـتُ = I (past)."),
        M("Which means “we watched”?", "شَاهَدْنَا", ["شَاهَدْتُ", "نُشَاهِد", "شَاهَدُوا"], "ـنَا = we (past)."),
        M("Which means “she watched”?", "شَاهَدَتْ", ["شَاهَدَ", "شَاهَدْتِ", "تُشَاهِد"], "ـتْ = she (past)."),
        M("Which means “they (men) watched”?", "شَاهَدُوا", ["شَاهَدَ", "شَاهَدْنَا", "يُشَاهِدُون"], "ـُوا = they (past)."),
        M("Which means “We will watch the match tomorrow”?", "سَنُشَاهِد الْمُبَارَاة غَدًا", ["شَاهَدْنَا الْمُبَارَاة غَدًا", "سَأُشَاهِد الْمُبَارَاة غَدًا", "لَنْ نُشَاهِد الْمُبَارَاة غَدًا"], "سَـ + نُشَاهِد."),
        M("Which means “I will not watch television tonight”?", "لَنْ أُشَاهِد التِّلْفَاز اللَّيْلَة", ["لَمْ أُشَاهِد التِّلْفَاز اللَّيْلَة", "سَأُشَاهِد التِّلْفَاز اللَّيْلَة", "لَا أُشَاهِد التِّلْفَاز أَمْس"], "لَنْ for the future."),
        M("Which means “My brother helped me with the homework”?", "سَاعَدَنِي أَخِي فِي الْوَاجِب", ["سَاعَدْتُ أَخِي فِي الْوَاجِب", "يُسَاعِدُنِي أَخِي فِي الْوَاجِب", "سَاعَدَتْنِي أُخْتِي فِي الْوَاجِب"], "ـنِي = me."),
        F("___ هَذَا الْفِيلْم؟ (Did you watch, to a man)", "هَلْ شَاهَدْتَ", ["هَلْ شَاهَدْتِ", "هَلْ شَاهَدْتُ", "هَلْ سَتُشَاهِد"], "A past verb: you (to a man).", tr="Did you watch this film?"),
        F("سَنُشَاهِد الْمُبَارَاة فِي ___ غَدًا.", "النَّادِي", ["نَادِي", "النَّادِيَة", "مُبَارَاة"], "A place with ال.", tr="We will watch the match at the club tomorrow."),
    ],
    verify=vw("شَاهَدْتُ", "شَاهَدْنَا", "شَاهَدْتَ", "شَاهَدْتِ", "شَاهَدَتْ", "شَاهَدُوا", "سَأُشَاهِد", "سَنُشَاهِد", "سَتُشَاهِد", "سَتُشَاهِدِين", "سَيُشَاهِد", "سَيُشَاهِدُون",
              "أُشَاهِد", "التِّلْفَاز", "اللَّيْلَة", "سَاعَدَنِي", "سَاعَدْتُ", "سَاعَدَتْنِي", "يُسَاعِدُنِي", "نُشَاهِد", "يُشَاهِدُون", "الْمُبَارَاة", "النَّادِي"),
)

# ---------------------------------------------------------------------------- 162
L162 = lesson(
    "Trying, taking part, agreeing",
    "حَاوَلَ أَنْ · شَارَكَ فِي · وَافَقَ عَلَى",
    requires=["حاول", "شارك", "وافق", "فكرة", "موعد", "رحلة"],
    cards=[
        card("Measure III verbs and what follows them",
             "Many verbs need a particular word after them. حَاوَلَ is followed by أَنْ and a verb, شَارَكَ by فِي, وَافَقَ by "
             "عَلَى. Learn the verb together with its word.",
             tables=[table(["English", "Arabic"],
                           [["to try to…", "حَاوَلَ أَنْ"], ["to take part in…", "شَارَكَ فِي"], ["to agree to…", "وَافَقَ عَلَى"],
                            ["to help with…", "سَاعَدَ فِي"], ["to meet (someone)", "قَابَلَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "After أَنْ the present verb has the shortened endings you know.",
             examples=[
                 ex("أُحَاوِل أَنْ أَتَكَلَّم الْعَرَبِيَّة كُلّ يَوْم.", "I try to speak Arabic every day.", "أُحَاوِل أَنْ"),
                 ex("حَاوَلَ أَخِي أَنْ يَفْتَح الْبَاب.", "My brother tried to open the door.", "حَاوَلَ أَخِي أَنْ"),
                 ex("شَارَكْتُ فِي الرِّحْلَة.", "I took part in the trip.", "شَارَكْتُ فِي"),
                 ex("أُوَافِق عَلَى هَذِه الْفِكْرَة.", "I agree with this idea.", "أُوَافِق عَلَى"),
                 ex("لَا أُوَافِق عَلَى هَذَا الْمَوْعِد.", "I do not agree to this time.", "لَا أُوَافِق"),
                 ex("سَاعَدَتْنِي أُخْتِي فِي الْوَاجِب.", "My sister helped me with the homework.", "سَاعَدَتْنِي"),
             ]),
    ],
    exercises=[
        M("What does حَاوَلَ أَنْ mean?", "he tried to", ["he agreed to", "he took part in", "he helped"], "حَاوَلَ = to try."),
        M("Which preposition follows شَارَكَ?", "فِي", ["عَلَى", "مِنْ", "إِلَى"], "شَارَكَ فِي."),
        M("Which preposition follows وَافَقَ?", "عَلَى", ["فِي", "مَعَ", "عَنْ"], "وَافَقَ عَلَى."),
        M("Which means “I try to speak Arabic every day”?", "أُحَاوِل أَنْ أَتَكَلَّم الْعَرَبِيَّة كُلّ يَوْم", ["أُحَاوِل أَتَكَلَّم الْعَرَبِيَّة كُلّ يَوْم", "أُحَاوِل أَنْ تَتَكَلَّم الْعَرَبِيَّة كُلّ يَوْم", "حَاوَلْتُ أَنْ أَتَكَلَّم الْعَرَبِيَّة كُلّ يَوْم"], "أُحَاوِل أَنْ + a present verb."),
        M("Which means “I took part in the trip”?", "شَارَكْتُ فِي الرِّحْلَة", ["أُشَارِك فِي الرِّحْلَة", "شَارَكَ فِي الرِّحْلَة", "شَارَكْتُ عَلَى الرِّحْلَة"], "ـتُ = I (past)."),
        M("Which means “I do not agree to this time”?", "لَا أُوَافِق عَلَى هَذَا الْمَوْعِد", ["لَنْ أُوَافِق عَلَى هَذَا الْمَوْعِد", "لَمْ أُوَافِق فِي هَذَا الْمَوْعِد", "أُوَافِق عَلَى هَذَا الْمَوْعِد"], "لَا + present."),
        M("Which means “My brother tried to open the door”?", "حَاوَلَ أَخِي أَنْ يَفْتَح الْبَاب", ["حَاوَلَتْ أُخْتِي أَنْ تَفْتَح الْبَاب", "يُحَاوِل أَخِي أَنْ يَفْتَح الْبَاب", "حَاوَلَ أَخِي أَنْ أَفْتَح الْبَاب"], "He: حَاوَلَ … يَفْتَح."),
        F("أُوَافِق ___ هَذِه الْفِكْرَة.", "عَلَى", ["فِي", "إِلَى", "مِنْ"], "وَافَقَ عَلَى.", tr="I agree with this idea."),
        F("شَارَكْتُ ___ الرِّحْلَة.", "فِي", ["عَلَى", "إِلَى", "عَنْ"], "شَارَكَ فِي.", tr="I took part in the trip."),
    ],
    verify=vv("فتح", "sub", huwa="يَفْتَح") + vv("فتح", "pres", huwa="يَفْتَح")
    + vw("حَاوَلَ", "أُحَاوِل", "شَارَكْتُ", "أُوَافِق", "الْفِكْرَة", "الْمَوْعِد", "سَاعَدَتْنِي", "أُشَارِك", "أَتَكَلَّم", "أَنْ"),
)

# ---------------------------------------------------------------------------- 163
L163 = lesson(
    "Measure VI: تَفَاعَلَ",
    "تَقَابَلَ · نَتَقَابَل · نَتَحَادَث",
    requires=["قابل", "تبادل", "تعاون", "وقت", "نادي", "كتاب"],
    cards=[
        card("Doing it to each other",
             "Put تَـ in front of a Measure III verb and you get Measure VI, written تَفَاعَلَ. It usually means two or "
             "more people do the action to each other: قَابَلَ (to meet someone) gives تَقَابَلَ (to meet each other). "
             "This repeats what happened between Measures II and V: Measure V is II with تَـ, Measure VI is III with تَـ. "
             "The present is يَتَفَاعَل.",
             tables=[table(["Meaning", "Past (he)", "Present (we)"],
                           [["to meet each other", "تَقَابَلَ", "نَتَقَابَل"], ["to talk to each other", "تَحَادَثَ", "نَتَحَادَث"],
                            ["to exchange", "تَبَادَلَ", "نَتَبَادَل"], ["to cooperate", "تَعَاوَنَ", "نَتَعَاوَن"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)]),
        card("In sentences",
             "Because the action goes between people, the subject is often “we” or “they”.",
             examples=[
                 ex("نَتَقَابَل فِي النَّادِي يَوْم الْجُمْعَة.", "We meet at the club on Friday.", "نَتَقَابَل"),
                 ex("تَقَابَلْنَا أَمْس فِي الْحَدِيقَة.", "We met yesterday in the park.", "تَقَابَلْنَا"),
                 ex("نَتَحَادَث كُلّ مَسَاء.", "We talk to each other every evening.", "نَتَحَادَث"),
                 ex("نَتَبَادَل الْكُتُب.", "We exchange books.", "نَتَبَادَل"),
                 ex("يَتَعَاوَن الطُّلَّاب فِي الْوَاجِب.", "The students cooperate on the homework.", "يَتَعَاوَن"),
                 ex("سَنَتَقَابَل بَعْدَ الدَّرْس.", "We will meet after the lesson.", "سَنَتَقَابَل"),
             ]),
    ],
    exercises=[
        M("What does تَقَابَلَ mean?", "to meet each other", ["to watch", "to meet someone", "to help"], "Measure VI is reciprocal."),
        M("What does تَبَادَلَ mean?", "to exchange", ["to travel", "to meet", "to talk"], "تَبَادَلَ = to exchange."),
        M("Which is “we meet each other”?", "نَتَقَابَل", ["نُقَابِل", "يَتَقَابَل", "تَقَابَلَ"], "نَـ + تَـ."),
        M("Which is “we talk to each other”?", "نَتَحَادَث", ["نُحَادِث", "أَتَحَادَث", "تَحَادَثْتُ"], "نَـ + تَحَادَث."),
        M("Which means “We met yesterday in the park”?", "تَقَابَلْنَا أَمْس فِي الْحَدِيقَة", ["نَتَقَابَل أَمْس فِي الْحَدِيقَة", "تَقَابَلْتُ أَمْس فِي الْحَدِيقَة", "سَنَتَقَابَل أَمْس فِي الْحَدِيقَة"], "ـنَا = we (past)."),
        M("Which means “We will meet after the lesson”?", "سَنَتَقَابَل بَعْدَ الدَّرْس", ["تَقَابَلْنَا بَعْدَ الدَّرْس", "لَنْ نَتَقَابَل بَعْدَ الدَّرْس", "سَأَتَقَابَل بَعْدَ الدَّرْس"], "سَـ + نَتَقَابَل."),
        M("Which means “We exchange books”?", "نَتَبَادَل الْكُتُب", ["أَتَبَادَل الْكُتُب", "نَتَبَادَل الْكِتَاب", "يَتَبَادَلُون الْكُتُب"], "نَـ = we."),
        F("___ فِي النَّادِي يَوْم الْجُمْعَة.", "نَتَقَابَل", ["أَتَقَابَل", "نُقَابِل", "تَقَابَلَ"], "We: نَـ.", tr="We meet at the club on Friday."),
        F("يَتَعَاوَن ___ فِي الْوَاجِب.", "الطُّلَّاب", ["الطَّالِبَة", "نَتَعَاوَن", "أَكْتُب"], "The people who cooperate.", tr="The students cooperate on the homework."),
    ],
    verify=vw("تَقَابَلَ", "تَحَادَثَ", "تَبَادَلَ", "تَعَاوَنَ", "نَتَقَابَل", "نَتَحَادَث", "نَتَبَادَل", "نَتَعَاوَن", "تَقَابَلْنَا", "تَقَابَلْتُ", "سَنَتَقَابَل", "يَتَعَاوَن", "أَتَقَابَل",
              "يَتَقَابَل", "أَتَحَادَث", "تَحَادَثْتُ", "أَتَبَادَل", "يَتَبَادَلُون", "الْكُتُب", "الطُّلَّاب", "قَابَلَ", "نُقَابِل", "نُحَادِث"),
)

# ---------------------------------------------------------------------------- 164
L164 = lesson(
    "Let’s meet!",
    "هَلْ تُرِيد أَنْ تُرَافِقَنِي؟ · أَيْنَ نَتَقَابَل؟",
    requires=["موعد", "سينما", "ساعة", "أين", "متى", "فكرة"],
    cards=[
        card("An invitation",
             "To invite someone use هَلْ تُرِيد أَنْ … and a verb. With an ending for “me” the verb gets a ن first: "
             "تُرَافِقَنِي (you accompany me). Then fix the time and the place with مَتَى and أَيْنَ.",
             tables=[table(["Speaker A", "Speaker B"],
                           [["هَلْ تُرِيد أَنْ تُرَافِقَنِي إِلَى السِّينَمَا؟", "نَعَمْ، فِكْرَة جَيِّدَة."],
                            ["مَتَى نَتَقَابَل؟", "فِي السَّاعَة السَّادِسَة."],
                            ["أَيْنَ نَتَقَابَل؟", "أَمَامَ السِّينَمَا."],
                            ["حَسَنًا، إِلَى اللِّقَاء.", "إِلَى اللِّقَاء."]],
                           say=[0, 1], tlit=[0, 1], gloss=False)]),
        card("Saying yes and no",
             "Agree with فِكْرَة جَيِّدَة (“good idea”) or حَسَنًا (“fine”). To refuse politely, say آسِف and give a "
             "reason.",
             examples=[
                 ex("هَلْ تُرِيدِين أَنْ تُرَافِقِينِي إِلَى الْمُبَارَاة؟", "Do you want to come with me to the match? (to a woman)", "تُرَافِقِينِي"),
                 ex("نَعَمْ، فِكْرَة جَيِّدَة. مَتَى نَتَقَابَل؟", "Yes, good idea. When shall we meet?", "فِكْرَة جَيِّدَة"),
                 ex("نَتَقَابَل فِي السَّاعَة الرَّابِعَة وَالنِّصْف أَمَامَ النَّادِي.", "We meet at half past four in front of the club.", "أَمَامَ"),
                 ex("آسِف، عِنْدِي مَوْعِد غَدًا.", "Sorry, I have an appointment tomorrow. (a man speaking)", "آسِف"),
                 ex("لَا أُوَافِق عَلَى هَذَا الْمَكَان.", "This place does not suit me.", "لَا أُوَافِق"),
                 ex("حَسَنًا، إِلَى اللِّقَاء غَدًا.", "Fine, see you tomorrow.", "إِلَى اللِّقَاء"),
             ]),
    ],
    exercises=[
        M("Which invites someone to the cinema?", "هَلْ تُرِيد أَنْ تُرَافِقَنِي إِلَى السِّينَمَا؟", ["هَلْ رَافَقْتَنِي إِلَى السِّينَمَا؟", "لَنْ أُرَافِقَكَ إِلَى السِّينَمَا", "كَمْ ثَمَن السِّينَمَا؟"], "تُرَافِقَنِي = you accompany me."),
        M("What does فِكْرَة جَيِّدَة mean?", "good idea", ["good morning", "bad news", "good night"], "فِكْرَة = idea."),
        M("Which asks “When shall we meet?”", "مَتَى نَتَقَابَل؟", ["أَيْنَ نَتَقَابَل؟", "مَنْ نَتَقَابَل؟", "كَمْ نَتَقَابَل؟"], "مَتَى = when."),
        M("Which asks “Where shall we meet?”", "أَيْنَ نَتَقَابَل؟", ["مَتَى نَتَقَابَل؟", "لِمَاذَا نَتَقَابَل؟", "كَيْفَ نَتَقَابَل؟"], "أَيْنَ = where."),
        M("Which means “in front of the club”?", "أَمَامَ النَّادِي", ["خَلْفَ النَّادِي", "بَيْنَ النَّادِي", "فِي النَّادِي"], "أَمَامَ = in front of."),
        M("Which is a polite refusal?", "آسِف، عِنْدِي مَوْعِد", ["حَسَنًا، فِكْرَة جَيِّدَة", "مَرْحَبًا", "أَهْلًا وَسَهْلًا"], "آسِف = sorry."),
        M("Which means “We meet at half past four”?", "نَتَقَابَل فِي السَّاعَة الرَّابِعَة وَالنِّصْف", ["نَتَقَابَل فِي السَّاعَة الرَّابِعَة إِلَّا رُبْعًا", "نَتَقَابَل فِي السَّاعَة الْخَامِسَة وَالنِّصْف", "تَقَابَلْنَا فِي السَّاعَة الرَّابِعَة وَالنِّصْف"], "وَالنِّصْف = and a half."),
        F("هَلْ تُرِيد أَنْ ___ إِلَى السِّينَمَا؟ (accompany me)", "تُرَافِقَنِي", ["تُرَافِقُونِي", "رَافَقْتَنِي", "أُرَافِقَكَ"], "A present verb with “me”.", tr="Do you want to come with me to the cinema?"),
        F("نَتَقَابَل ___ النَّادِي.", "أَمَامَ", ["خَلْفَ", "مَعَ", "عَلَى"], "In front of.", tr="We meet in front of the club."),
    ],
    verify=vw("تُرِيد", "تُرَافِقَنِي", "تُرِيدِين", "تُرَافِقِينِي", "فِكْرَة", "جَيِّدَة", "أَمَامَ", "آسِف", "حَسَنًا", "اللِّقَاء", "مَوْعِد", "الْمَكَان", "السِّينَمَا", "رَافَقْتَنِي",
              "أُرَافِقَكَ"),
)

# ---------------------------------------------------------------------------- 165
L165 = lesson(
    "Dishes from Arab countries",
    "الْفَلَافِل · الشَّاوِرْمَا · التَّبُّولَة · الْبَقْلَاوَة",
    requires=["لذيذ", "طبق", "خبز", "شاي", "حلو", "جرب"],
    cards=[
        card("Dishes you can find in many places",
             "Falafel is made from chickpeas or beans, shawarma is meat cut from a spit, tabbouleh is a fresh salad of "
             "parsley and wheat, hummus is a chickpea dip and baklava is a very sweet pastry. They are eaten in many Arab "
             "countries, with small differences from place to place.",
             tables=[table(["English", "Arabic"],
                           [["falafel", "الْفَلَافِل"], ["shawarma", "الشَّاوِرْمَا"], ["tabbouleh", "التَّبُّولَة"],
                            ["hummus", "الْحُمُّص"], ["baklava", "الْبَقْلَاوَة"], ["mint", "النَّعْنَاع"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("Talking about food",
             "Use the words you already know for taste and for likes.",
             examples=[
                 ex("الْفَلَافِل لَذِيذَة وَرَخِيصَة.", "Falafel is delicious and cheap.", "لَذِيذَة"),
                 ex("أُحِبّ الْحُمُّص مَعَ الْخُبْز.", "I like hummus with bread.", "الْحُمُّص"),
                 ex("هَلْ جَرَّبْتَ التَّبُّولَة؟", "Have you tried tabbouleh? (to a man)", "جَرَّبْتَ"),
                 ex("الْبَقْلَاوَة حُلْوَة جِدًّا.", "Baklava is very sweet.", "حُلْوَة"),
                 ex("نَشْرَب الشَّايْ بِالنَّعْنَاع بَعْدَ الْغَدَاء.", "We drink tea with mint after lunch.", "بِالنَّعْنَاع"),
                 ex("أُفَضِّل الشَّاوِرْمَا عَلَى الْفَلَافِل.", "I prefer shawarma to falafel.", "أُفَضِّل"),
             ]),
    ],
    exercises=[
        M("Which dish is a sweet pastry?", "الْبَقْلَاوَة", ["الْفَلَافِل", "التَّبُّولَة", "الشَّاوِرْمَا"], "بَقْلَاوَة = baklava."),
        M("Which dish is a fresh salad?", "التَّبُّولَة", ["الْبَقْلَاوَة", "الْحُمُّص", "الشَّاوِرْمَا"], "تَبُّولَة = tabbouleh."),
        M("What does النَّعْنَاع mean?", "mint", ["tea", "bread", "rice"], "نَعْنَاع = mint."),
        M("Which means “Falafel is delicious and cheap”?", "الْفَلَافِل لَذِيذَة وَرَخِيصَة", ["الْفَلَافِل غَالِيَة وَرَخِيصَة", "الْبَقْلَاوَة لَذِيذَة وَرَخِيصَة", "الْفَلَافِل لَذِيذَة وَغَالِيَة"], "لَذِيذ = tasty."),
        M("Which means “I like hummus with bread”?", "أُحِبّ الْحُمُّص مَعَ الْخُبْز", ["أُفَضِّل الْحُمُّص عَلَى الْخُبْز", "لَا أُحِبّ الْحُمُّص مَعَ الْخُبْز", "تُحِبّ الْحُمُّص مَعَ الْخُبْز"], "مَعَ = with."),
        M("Which means “Have you tried tabbouleh?” (to a man)", "هَلْ جَرَّبْتَ التَّبُّولَة؟", ["هَلْ جَرَّبْتِ التَّبُّولَة؟", "هَلْ تُجَرِّب التَّبُّولَة؟", "هَلْ جَرَّبْتُ التَّبُّولَة؟"], "جَرَّبْتَ = you (man) tried."),
        M("Which means “I prefer shawarma to falafel”?", "أُفَضِّل الشَّاوِرْمَا عَلَى الْفَلَافِل", ["أُفَضِّل الْفَلَافِل عَلَى الشَّاوِرْمَا", "أُفَضِّل الشَّاوِرْمَا مِنَ الْفَلَافِل", "أُحِبّ الشَّاوِرْمَا عَلَى الْفَلَافِل"], "أُفَضِّل X عَلَى Y."),
        F("الْبَقْلَاوَة حُلْوَة ___.", "جِدًّا", ["لَذِيذ", "غَدًا", "كَثِيرًا"], "“Very”.", tr="Baklava is very sweet."),
        F("نَشْرَب الشَّايْ ___النَّعْنَاع.", "بِ", ["فِي", "عَلَى", "إِلَى"], "“With”: بِـ.", tr="We drink tea with mint."),
    ],
    verify=vv("شرب", "pres", nahnu="نَشْرَب")
    + vw("الْفَلَافِل", "الشَّاوِرْمَا", "التَّبُّولَة", "الْحُمُّص", "الْبَقْلَاوَة", "النَّعْنَاع", "لَذِيذَة", "رَخِيصَة", "جَرَّبْتَ", "جَرَّبْتِ", "جَرَّبْتُ", "تُجَرِّب", "حُلْوَة", "جِدًّا",
         "الْخُبْز", "الْغَدَاء"),
)

# ---------------------------------------------------------------------------- 166
L166 = lesson(
    "Booking a table and paying",
    "أُرِيد أَنْ أَحْجِز طَاوِلَة · الْحِسَاب مِنْ فَضْلِكَ",
    requires=["حجز", "طاولة", "شخص", "حساب", "قائمة", "مطعم"],
    cards=[
        card("At the restaurant, step by step",
             "Phone the restaurant to book a table. For the number of people use the numbers 3–10 with the plural "
             "أَشْخَاص, and remember that شَخْص is masculine, so the number ends in ـَة (أَرْبَعَة). Then ask for the "
             "menu and, at the end, for the bill.",
             tables=[table(["English", "Arabic"],
                           [["I want to book a table", "أُرِيد أَنْ أَحْجِز طَاوِلَة"], ["for four people", "لِأَرْبَعَة أَشْخَاص"],
                            ["at what time?", "فِي أَيّ سَاعَة؟"], ["the menu", "الْقَائِمَة"], ["The bill, please.", "الْحِسَاب مِنْ فَضْلِكَ"]],
                           say=[1], tlit=[1], gloss=False)]),
        card("In sentences",
             "Notice how the numbers you learned earlier are used for the people and the bill.",
             examples=[
                 ex("أُرِيد أَنْ أَحْجِز طَاوِلَة لِسِتَّة أَشْخَاص.", "I want to book a table for six people.", "لِسِتَّة أَشْخَاص"),
                 ex("فِي أَيّ سَاعَة؟ فِي السَّاعَة الثَّامِنَة مَسَاءً.", "At what time? At eight in the evening.", "فِي أَيّ سَاعَة"),
                 ex("مِنْ فَضْلِكَ، الْقَائِمَة.", "The menu, please. (to a man)", "الْقَائِمَة"),
                 ex("هَلْ تُفَضِّلِين الدَّجَاج أَمِ السَّمَك؟", "Do you prefer chicken or fish? (to a woman)", "أَمِ"),
                 ex("الْحِسَاب مِنْ فَضْلِكَ. كَمِ الْحِسَاب؟", "The bill, please. How much is the bill? (to a man)", "الْحِسَاب"),
                 ex("الْحِسَاب خَمْسَة وَسَبْعُون دِينَارًا.", "The bill is seventy-five dinars.", "خَمْسَة وَسَبْعُون"),
             ]),
    ],
    exercises=[
        M("What does أَحْجِز طَاوِلَة mean?", "I book a table", ["I clean a table", "I buy a table", "I eat at a table"], "حَجَزَ = to book."),
        M("Which means “for four people”?", "لِأَرْبَعَة أَشْخَاص", ["لِأَرْبَع أَشْخَاص", "لِأَرْبَعَة شَخْص", "لِأَرْبَعِين أَشْخَاص"], "4 + plural: أَرْبَعَة (شَخْص is masculine)."),
        M("Which asks “At what time?”", "فِي أَيّ سَاعَة؟", ["كَمِ السَّاعَة؟", "أَيْنَ السَّاعَة؟", "مَنِ السَّاعَة؟"], "فِي أَيّ سَاعَة؟"),
        M("What does الْقَائِمَة mean here?", "the menu", ["the bill", "the table", "the restaurant"], "قَائِمَة = list, menu."),
        M("Which means “The bill, please”?", "الْحِسَاب مِنْ فَضْلِكَ", ["الْقَائِمَة مِنْ فَضْلِكَ", "الطَّاوِلَة مِنْ فَضْلِكَ", "الْخُبْز مِنْ فَضْلِكَ"], "حِسَاب = bill."),
        M("Which means “I want to book a table for six people”?", "أُرِيد أَنْ أَحْجِز طَاوِلَة لِسِتَّة أَشْخَاص", ["أُرِيد أَنْ أَحْجِز طَاوِلَة لِسِتّ أَشْخَاص", "أُرِيد أَنْ أَحْجِز طَاوِلَة لِسِتَّة شَخْص", "أَحْجِز طَاوِلَة لِسِتِّين شَخْص"], "6 + plural."),
        M("Which means “The bill is seventy-five dinars”?", "الْحِسَاب خَمْسَة وَسَبْعُون دِينَارًا", ["الْحِسَاب خَمْس وَسَبْعُون دِينَارًا", "الْحِسَاب خَمْسَة وَخَمْسُون دِينَارًا", "الْحِسَاب سَبْعَة وَخَمْسُون دِينَارًا"], "Unit, وَ, ten; masculine noun: خَمْسَة."),
        F("أُرِيد أَنْ ___ طَاوِلَة.", "أَحْجِز", ["حَجَزْتُ", "يَحْجِز", "حَجْز"], "I want to + a present verb.", tr="I want to book a table."),
        F("___ مِنْ فَضْلِكَ.", "الْحِسَاب", ["الطَّبَق", "غَدًا", "الْجَوّ"], "At the end of the meal.", tr="The bill, please."),
    ],
    verify=vw("أَحْجِز", "طَاوِلَة", "لِأَرْبَعَة", "أَشْخَاص", "أَيّ", "الْقَائِمَة", "الْحِسَاب", "فَضْلِكَ", "لِسِتَّة", "الدَّجَاج", "السَّمَك", "خَمْسَة", "وَسَبْعُون", "دِينَارًا",
              "حَجَزْتُ", "يَحْجِز"),
)


# ---------------------------------------------------------------------------- 167
L167 = lesson(
    "Review: hobbies and preferences",
    "أُحِبّ · أُفَضِّل · أَلْعَب · أَسْبَح",
    requires=["وقت", "فراغ", "قراءة", "فضل", "لعب", "سبح"],
    cards=[
        card("Two friends talk about free time",
             "Rana and Sami compare what they like to do.",
             examples=[
                 ex("مَاذَا تَفْعَل فِي وَقْت الْفَرَاغ يَا سَامِي؟", "What do you do in your free time, Sami?"),
                 ex("أَلْعَب كُرَة الْقَدَم فِي النَّادِي، وَأُحِبّ أَنْ أَسْبَح أَيْضًا.", "I play football at the club, and I also like to swim."),
                 ex("وَأَنَا أُفَضِّل الْقِرَاءَة وَالرَّسْم عَلَى الرِّيَاضَة.", "And I prefer reading and drawing to sport."),
                 ex("هَلْ تُشَاهِدِين الْأَفْلَام؟", "Do you watch films? (to a woman)"),
                 ex("نَعَمْ، شَاهَدْتُ فِيلْم جَمِيل أَمْس.", "Yes, I watched a nice film yesterday."),
                 ex("لَنْ أَلْعَب غَدًا لِأَنَّ عِنْدِي مَوْعِد.", "I will not play tomorrow because I have an appointment."),
             ]),
    ],
    exercises=[
        M("Which means “I like to swim”?", "أُحِبّ أَنْ أَسْبَح", ["أُحِبّ السِّبَاحَة أَنْ", "أُفَضِّل أَنْ أَسْبَح", "سَبَحْتُ"], "أُحِبّ أَنْ + a present verb."),
        M("Which means “I prefer reading to sport”?", "أُفَضِّل الْقِرَاءَة عَلَى الرِّيَاضَة", ["أُحِبّ الْقِرَاءَة عَلَى الرِّيَاضَة", "أُفَضِّل الرِّيَاضَة عَلَى الْقِرَاءَة", "أَفْضَل الْقِرَاءَة مِنَ الرِّيَاضَة"], "أُفَضِّل X عَلَى Y."),
        M("Which asks a woman “Do you watch films?”", "هَلْ تُشَاهِدِين الْأَفْلَام؟", ["هَلْ تُشَاهِد الْأَفْلَام؟", "هَلْ شَاهَدْتُ الْأَفْلَام؟", "هَلْ يُشَاهِدُون الْأَفْلَام؟"], "ـِين = you (to a woman)."),
        M("Which means “I watched a nice film yesterday”?", "شَاهَدْتُ فِيلْم جَمِيل أَمْس", ["أُشَاهِد فِيلْم جَمِيل أَمْس", "سَأُشَاهِد فِيلْم جَمِيل غَدًا", "شَاهَدَ فِيلْم جَمِيل أَمْس"], "Measure III past: شَاهَدْتُ."),
        M("Which means “I will not play tomorrow”?", "لَنْ أَلْعَب غَدًا", ["لَمْ أَلْعَب غَدًا", "لَا أَلْعَب أَمْس", "سَأَلْعَب غَدًا"], "لَنْ + present."),
        M("Which means “I play football at the club”?", "أَلْعَب كُرَة الْقَدَم فِي النَّادِي", ["أَلْعَب كُرَة السَّلَّة فِي النَّادِي", "أَسْبَح فِي النَّادِي", "نَلْعَب كُرَة الْقَدَم فِي النَّادِي"], "لَعِبَ = to play."),
        M("Which sport does Sami play at the club?", "كُرَة الْقَدَم", ["الرَّسْم", "الْقِرَاءَة", "الْمُوسِيقَى"], "He plays football at the club."),
        F("وَأَنَا ___ الْقِرَاءَة وَالرَّسْم عَلَى الرِّيَاضَة.", "أُفَضِّل", ["أَفْضَل", "فَضَّلْتُ", "تُفَضِّل"], "Measure II present, I.", tr="And I prefer reading and drawing to sport."),
        F("لَنْ أَلْعَب غَدًا ___ عِنْدِي مَوْعِد.", "لِأَنَّ", ["مَعَ", "ثُمَّ", "أَمْ"], "“Because”.", tr="I will not play tomorrow because I have an appointment."),
    ],
    verify=vv("لعب", "pres", ana="أَلْعَب") + vv("سبح", "pres", ana="أَسْبَح")
    + vw("سَامِي", "أُحِبّ", "أُفَضِّل", "أَيْضًا", "الْأَفْلَام", "تُشَاهِدِين", "شَاهَدْتُ", "لِأَنَّ", "مَوْعِد", "الرِّيَاضَة", "سَبَحْتُ", "أَفْضَل"),
)

# ---------------------------------------------------------------------------- 168
L168 = lesson(
    "Review: Measures III and VI, and a meal out",
    "شَاهَدْنَا · تَقَابَلْنَا · أَحْجِز · الْحِسَاب",
    requires=["شاهد", "قابل", "حجز", "حساب", "طبق", "لذيذ"],
    cards=[
        card("A Saturday outing",
             "Laila tells her friend about an outing with her family.",
             examples=[
                 ex("تَقَابَلْنَا أَمَامَ الْمَطْعَم فِي السَّاعَة الثَّامِنَة مَسَاءً.", "We met in front of the restaurant at eight in the evening."),
                 ex("حَجَزَ أَبِي طَاوِلَة لِخَمْسَة أَشْخَاص.", "My father booked a table for five people."),
                 ex("سَاعَدْتُ أُمِّي فِي الْمَطْعَم.", "I helped my mother at the restaurant."),
                 ex("نَظَرْنَا فِي الْقَائِمَة وَجَرَّبْنَا الْفَلَافِل وَالتَّبُّولَة.", "We looked at the menu and tried the falafel and the tabbouleh."),
                 ex("كَانَ الطَّعَام لَذِيذًا، لَكِنَّ الْبَقْلَاوَة كَانَتْ حُلْوَةً جِدًّا.", "The food was delicious, but the baklava was very sweet."),
                 ex("دَفَعَ أَبِي الْحِسَاب، ثُمَّ رَجَعْنَا إِلَى الْبَيْت.", "My father paid the bill, then we went home."),
             ]),
    ],
    exercises=[
        M("Which means “We met in front of the restaurant”?", "تَقَابَلْنَا أَمَامَ الْمَطْعَم", ["نَتَقَابَل أَمَامَ الْمَطْعَم", "قَابَلْتُ أَمَامَ الْمَطْعَم", "سَنَتَقَابَل أَمَامَ الْمَطْعَم"], "Measure VI past with ـنَا."),
        M("Which means “My father booked a table”?", "حَجَزَ أَبِي طَاوِلَة", ["أَحْجِز طَاوِلَة", "حَجَزْتُ طَاوِلَة", "يَحْجِز أَبِي طَاوِلَة"], "حَجَزَ = he booked."),
        M("Which means “a table for five people”?", "طَاوِلَة لِخَمْسَة أَشْخَاص", ["طَاوِلَة لِخَمْس أَشْخَاص", "طَاوِلَة لِخَمْسَة شَخْص", "طَاوِلَة لِخَمْسِين أَشْخَاص"], "5 + plural: خَمْسَة."),
        M("Which means “I helped my mother”?", "سَاعَدْتُ أُمِّي", ["أُسَاعِد أُمِّي", "سَاعَدَتْ أُمِّي", "سَاعَدَنِي أُمِّي"], "Measure III past, I."),
        M("Which means “We tried the falafel”?", "جَرَّبْنَا الْفَلَافِل", ["جَرَّبْتُ الْفَلَافِل", "نُجَرِّب الْفَلَافِل", "شَاهَدْنَا الْفَلَافِل"], "جَرَّبَ is Measure II."),
        M("Which means “The baklava was very sweet”?", "كَانَتِ الْبَقْلَاوَة حُلْوَةً جِدًّا", ["كَانَتِ الْبَقْلَاوَة رَخِيصَةً جِدًّا", "تَكُون الْبَقْلَاوَة حُلْوَةً جِدًّا", "لَمْ تَكُنِ الْبَقْلَاوَة حُلْوَةً جِدًّا"], "A feminine noun: كَانَتْ."),
        M("Which means “My father paid the bill”?", "دَفَعَ أَبِي الْحِسَاب", ["أَدْفَع الْحِسَاب", "دَفَعْتُ الْحِسَاب", "يَدْفَع أَبِي الْحِسَاب"], "دَفَعَ = he paid."),
        F("___ أَمَامَ الْمَطْعَم فِي السَّاعَة الثَّامِنَة.", "تَقَابَلْنَا", ["نَتَقَابَل", "قَابَلْنَا", "سَنَتَقَابَل"], "Measure VI, past, we.", tr="We met in front of the restaurant at eight o’clock."),
        F("دَفَعَ أَبِي الْحِسَاب، ثُمَّ ___ إِلَى الْبَيْت.", "رَجَعْنَا", ["نَرْجِع", "رَجَعَ", "أَرْجِع"], "Past, we.", tr="My father paid the bill, then we went home."),
    ],
    verify=(vv("دفع", "past", huwa="دَفَعَ") + vv("رجع", "past", nahnu="رَجَعْنَا") + vv("كتب", "past", huwa="كَتَبَ")
    + vw("تَقَابَلْنَا", "حَجَزَ", "لِخَمْسَة", "أَمَامَ", "سَاعَدْتُ", "شَاهَدْنَا", "جَرَّبْنَا", "جَرَّبْتُ", "لَذِيذًا", "كَانَتِ", "الْبَقْلَاوَة", "الْحِسَاب", "ثُمَّ", "نَتَقَابَل", "سَنَتَقَابَل",
         "قَابَلْتُ", "قَابَلْنَا", "الْمَطْعَم", "الطَّعَام", "لَكِنَّ")),
)

UNIT = unit("وَقْت الْفَرَاغ: hobbies, preferences, Measures III and VI, and eating out",
            [L157, L158, L159, L160, L161, L162, L163, L164, L165, L166, L167, L168])
