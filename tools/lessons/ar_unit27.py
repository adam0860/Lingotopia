"""Unit 27 (chapter 25): accidents, injuries, feelings, illness, the doctor and the pharmacy, a party, and a final review."""
from dsl_ar import *

# ---------------------------------------------------------------------------- 435
L435 = lesson(
    "A road accident",
    "وَقَعَ حَادِث سَيْر · تَصَادَمَتِ السَّيَّارَتَان",
    requires=["حادث", "سير", "سرعة", "إشارة", "شاحنة", "سيارة", "طريق", "وقع", "توقف"],
    cards=[
        card("What happened on the road",
             "A traffic accident is حَادِث سَيْر. You say it happened with وَقَعَ, “occurred”. Cars collide: اِصْطَدَمَتْ بِـ, “crashed into”, or تَصَادَمَتَا, “collided with each other” (Measure VI). "
             "When the verb comes first it stays singular: تَصَادَمَتِ السَّيَّارَتَان. When the pair comes first, the verb agrees with the dual: السَّيَّارَتَان تَصَادَمَتَا. The journal lines are invented.",
             tables=[table(["English", "Arabic"],
                           [["traffic accident", "حَادِث سَيْر"], ["speed", "سُرْعَة"], ["traffic light", "إِشَارَة الْمُرُور"], ["lorry", "شَاحِنَة"], ["fast driver", "مُسْرِع"], ["it happened", "وَقَعَ"], ["crashed into", "اِصْطَدَمَ بِ"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("وَقَعَ حَادِث سَيْر عَلَى الطَّرِيق السَّرِيع.", "A traffic accident happened on the highway.", "وَقَعَ"),
                 ex("اِصْطَدَمَتْ سَيَّارَتُنَا بِشَاحِنَة.", "Our car crashed into a lorry.", "اِصْطَدَمَتْ"),
                 ex("كَانَ السَّائِق مُسْرِعًا.", "The driver was speeding.", "مُسْرِعًا"),
                 ex("لَمْ يَتَوَقَّفْ عِنْدَ الْإِشَارَة الْحَمْرَاء.", "He did not stop at the red light.", "الْإِشَارَة الْحَمْرَاء"),
                 ex("تَصَادَمَتِ السَّيَّارَتَان عِنْدَ الْإِشَارَة.", "The two cars collided at the light.", "تَصَادَمَتِ"),
                 ex("السَّيَّارَتَان تَصَادَمَتَا بِقُوَّة.", "The two cars collided hard.", "تَصَادَمَتَا"),
             ]),
    ],
    exercises=[
        M("What is حَادِث سَيْر?", "a traffic accident", ["a train timetable", "a road map", "a driving licence"], "حَادِث = accident; سَيْر = traffic."),
        M("What does اِصْطَدَمَتْ سَيَّارَتُنَا بِشَاحِنَة mean?", "Our car crashed into a lorry", ["Our car overtook a lorry", "Our lorry hit a car", "We rented a lorry"], "اِصْطَدَمَ بِـ = to crash into."),
        M("What does مُسْرِع mean?", "speeding, fast", ["slow", "tired", "careful"], "أَسْرَعَ = to hurry, to speed."),
        M("What does تَصَادَمَتَا mean?", "the two (f.) collided with each other", ["the two (f.) were repaired", "the two (f.) were stolen", "she collided"], "Measure VI, dual feminine."),
        M("Why is it تَصَادَمَتِ السَّيَّارَتَان, with a singular verb?", "the verb comes first", ["the cars are masculine", "there are three cars", "it is a command"], "A verb before its subject stays singular."),
        M("What does لَمْ يَتَوَقَّفْ mean?", "he did not stop", ["he will not stop", "he stopped", "stop!"], "لَمْ + jussive."),
        F("وَقَعَ ___ سَيْر عَلَى الطَّرِيق السَّرِيع.", "حَادِث", ["حَقِيبَة", "فَرَامِل"], "A traffic accident.", tr="A traffic accident happened on the highway."),
        F("___ سَيَّارَتُنَا بِشَاحِنَة.", "اِصْطَدَمَتْ", ["اِصْطَدَمَ", "اِصْطَدَمُوا"], "سَيَّارَة is feminine.", tr="Our car crashed into a lorry."),
        F("كَانَ السَّائِق ___.", "مُسْرِعًا", ["مُسْرِعُونَ", "مُسْرِعَة"], "After كَانَ the predicate is accusative.", tr="The driver was speeding."),
        F("السَّيَّارَتَان ___ بِقُوَّة.", "تَصَادَمَتَا", ["تَصَادَمَتْ", "تَصَادَمُوا"], "The pair comes first: a dual verb.", tr="The two cars collided hard.", lemma="صدم#6:past:huma_f"),
    ],
    verify=vv("صدم#6", "past", huma_f="تَصَادَمَتَا", hiya="تَصَادَمَتْ"),
)

# ---------------------------------------------------------------------------- 436
L436 = lesson(
    "Injured and damaged",
    "جُرِحَ ثَلَاثَة أَشْخَاص · تَضَرَّرَتِ السَّيَّارَة",
    requires=["جرح", "جريح", "إصابة", "خطير", "خفيف", "إسعاف", "مستشفى", "سيارة"],
    cards=[
        card("People and cars after the crash",
             "People are injured: the passive جُرِحَ, “was wounded”, أُصِيبَ, “was hurt”. An injury is إِصَابَة, and the injured are الْجَرْحَى. An injury can be بَسِيطَة, “slight”, or خَطِيرَة, “serious”. "
             "Cars are damaged: تَضَرَّرَتِ السَّيَّارَة (Measure V). An ambulance is سَيَّارَة إِسْعَاف. The lines are invented.",
             tables=[table(["English", "Arabic"],
                           [["was wounded", "جُرِحَ"], ["was hurt", "أُصِيبَ"], ["the injured", "الْجَرْحَى"], ["injury", "إِصَابَة"], ["slight", "بَسِيطَة"], ["serious", "خَطِيرَة"], ["was damaged (f.)", "تَضَرَّرَتْ"], ["ambulance", "سَيَّارَة إِسْعَاف"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("جُرِحَ ثَلَاثَة أَشْخَاص فِي الْحَادِث.", "Three people were wounded in the accident.", "جُرِحَ"),
                 ex("كَانَتِ الْإِصَابَات بَسِيطَة.", "The injuries were slight.", "بَسِيطَة"),
                 ex("لَمْ يُجْرَحْ أَحَد.", "No one was wounded.", "لَمْ يُجْرَحْ"),
                 ex("تَضَرَّرَتِ السَّيَّارَة كَثِيرًا.", "The car was badly damaged.", "تَضَرَّرَتِ"),
                 ex("وَصَلَتْ سَيَّارَة الْإِسْعَاف بَعْدَ عَشْر دَقَائِق.", "The ambulance arrived after ten minutes.", "الْإِسْعَاف"),
                 ex("نُقِلَ الْجَرْحَى إِلَى الْمُسْتَشْفَى.", "The injured were taken to the hospital.", "نُقِلَ"),
             ]),
    ],
    exercises=[
        M("What does جُرِحَ ثَلَاثَة أَشْخَاص mean?", "Three people were wounded", ["Three people helped", "Three people left", "Three people paid"], "A passive verb."),
        M("What are الْجَرْحَى?", "the injured", ["the doctors", "the drivers", "the visitors"], "جَرِيح = injured; plural جَرْحَى."),
        M("What does إِصَابَة بَسِيطَة mean?", "a slight injury", ["a serious injury", "a new car", "a long road"], "بَسِيط = simple, slight."),
        M("What does لَمْ يُجْرَحْ أَحَد mean?", "no one was wounded", ["someone was wounded", "everyone was wounded", "the doctor was wounded"], "لَمْ + passive jussive."),
        M("What does تَضَرَّرَتِ السَّيَّارَة mean?", "the car was damaged", ["the car was sold", "the car was rented", "the car was washed"], "ضَرَر = damage."),
        M("What does نُقِلَ الْجَرْحَى إِلَى الْمُسْتَشْفَى mean?", "The injured were taken to the hospital", ["The injured left the hospital", "The hospital is closed", "The doctor was injured"], "نُقِلَ = was transported."),
        F("جُرِحَ ثَلَاثَة ___ فِي الْحَادِث.", "أَشْخَاص", ["شَخْص", "شَخْصَان"], "After ثَلَاثَة, a plural.", tr="Three people were wounded in the accident."),
        F("كَانَتِ الْإِصَابَات ___.", "بَسِيطَة", ["بَسِيط", "بَسِيطُون"], "Plural of things: feminine singular.", tr="The injuries were slight."),
        F("___ السَّيَّارَة كَثِيرًا.", "تَضَرَّرَتِ", ["تَضَرَّرَ", "يَتَضَرَّر"], "A feminine past verb.", tr="The car was badly damaged.", lemma="ضرر#5:past:hiya"),
        F("وَصَلَتْ سَيَّارَة ___ بَعْدَ عَشْر دَقَائِق.", "الْإِسْعَاف", ["الْفَرَامِل", "الْوَقُود"], "The ambulance arrives.", tr="The ambulance arrived after ten minutes."),
    ],
    verify=(vv("ضرر#5", "past", hiya="تَضَرَّرَتْ")),
)

# ---------------------------------------------------------------------------- 437
L437 = lesson(
    "The news report",
    "أَعْلَنَتِ الشُّرْطَة · يُقَال إِنَّ · مَا زَالَ التَّحْقِيق",
    requires=["شرطة", "أعلن", "حادث", "تحقيق", "مستمر", "مسؤولية", "سائق", "مستشفى"],
    cards=[
        card("How a report sounds",
             "News reports use set phrases. أَعْلَنَتِ الشُّرْطَة أَنَّ …, “the police announced that …”; يُقَال إِنَّ …, “it is said that …”; مَا زَالَ التَّحْقِيق مُسْتَمِرًّا, “the investigation is still going on”. "
             "The word مَسْؤُولِيَّة means “responsibility”. The two reports below are invented, and they name no real event.",
             examples=[
                 ex("أَعْلَنَتِ الشُّرْطَة أَنَّ حَادِثًا وَقَعَ صَبَاحَ الْيَوْم.", "The police announced that an accident happened this morning.", "أَعْلَنَتِ"),
                 ex("تَصَادَمَتْ سَيَّارَة وَشَاحِنَة عِنْدَ الْإِشَارَة.", "A car and a lorry collided at the light.", "تَصَادَمَتْ"),
                 ex("نُقِلَ الْجَرْحَى إِلَى الْمُسْتَشْفَى.", "The injured were taken to the hospital.", "نُقِلَ"),
                 ex("يُقَال إِنَّ سَائِق الشَّاحِنَة كَانَ مُسْرِعًا.", "It is said that the lorry driver was speeding.", "يُقَال إِنَّ"),
                 ex("لَمْ تُحَدِّدِ الشُّرْطَة الْمَسْؤُولِيَّة بَعْدُ.", "The police have not yet determined who is responsible.", "الْمَسْؤُولِيَّة"),
                 ex("مَا زَالَ التَّحْقِيق مُسْتَمِرًّا.", "The investigation is still continuing.", "مَا زَالَ"),
             ]),
    ],
    exercises=[
        M("What does أَعْلَنَتِ الشُّرْطَة mean?", "The police announced", ["The police asked", "The police left", "The police arrived"], "أَعْلَنَ = to announce."),
        M("What does يُقَال إِنَّ mean?", "it is said that", ["it is known that", "we hope that", "I forgot that"], "A reporting phrase."),
        M("What does مَا زَالَ التَّحْقِيق مُسْتَمِرًّا mean?", "The investigation is still going on", ["The investigation has ended", "The investigation is cancelled", "The investigation has not begun"], "مَا زَالَ = still."),
        M("What is مَسْؤُولِيَّة?", "responsibility", ["accident", "speed", "injury"], "Who is responsible."),
        M("Why أَعْلَنَتِ with a final تِ?", "الشُّرْطَة is feminine", ["it is a command", "it is plural", "it is a question"], "A feminine subject."),
        M("What does لَمْ تُحَدِّدِ الشُّرْطَة الْمَسْؤُولِيَّة بَعْدُ mean?", "The police have not yet determined the responsibility", ["The police have blamed the driver", "The police denied the accident", "The police closed the road"], "لَمْ … بَعْدُ = not yet."),
        F("___ الشُّرْطَة أَنَّ حَادِثًا وَقَعَ.", "أَعْلَنَتِ", ["أَعْلَنَ", "تُعْلِن"], "A feminine past verb.", tr="The police announced that an accident happened."),
        F("___ إِنَّ سَائِق الشَّاحِنَة كَانَ مُسْرِعًا.", "يُقَال", ["قُلْتُ", "قَالَ"], "“it is said that”.", tr="It is said that the lorry driver was speeding."),
        F("مَا زَالَ التَّحْقِيق ___.", "مُسْتَمِرًّا", ["مُسْتَمِرٌّ", "مُسْتَمِرُّونَ"], "After مَا زَالَ the predicate is accusative.", tr="The investigation is still continuing."),
        F("لَمْ تُحَدِّدِ الشُّرْطَة الْمَسْؤُولِيَّة ___.", "بَعْدُ", ["قَبْلُ", "أَمْس"], "“not yet”.", tr="The police have not yet determined the responsibility."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 438
L438 = lesson(
    "Telling mishaps in order: وَ، فَ، ثُمَّ، أَوْ",
    "نَزَلَ السَّائِق ثُمَّ نَظَرَ إِلَى الْإِطَار",
    requires=["نزل", "نظر", "شرطة", "شركة", "طريق", "سائق", "إطار"],
    cards=[
        card("Four small words",
             "Four short conjunctions organise a story. وَ simply joins, “and”. فَ joins with a quick result, “and so, and then at once”. ثُمَّ joins with a pause, “then, after that”. أَوْ gives a choice, “or”. "
             "فَ and وَ are written joined to the next word; ثُمَّ and أَوْ are separate words. Before الـ, أَوْ becomes أَوِ. The sentences are invented.",
             tables=[table(["Word", "Meaning"],
                           [["وَ", "and"], ["فَ", "and so, at once"], ["ثُمَّ", "then, after a pause"], ["أَوْ", "or"]],
                           say=[0], tlit=[0], gloss=False)],
             examples=[
                 ex("أَوْقَفَ السَّائِق السَّيَّارَة فَنَزَلَ.", "The driver stopped the car and (at once) got out.", "فَنَزَلَ"),
                 ex("نَزَلَ السَّائِق ثُمَّ نَظَرَ إِلَى الْإِطَار.", "The driver got out, then looked at the tyre.", "ثُمَّ"),
                 ex("وَصَلَتِ الشُّرْطَة فَكَتَبَتْ تَقْرِيرًا.", "The police arrived and wrote a report.", "فَكَتَبَتْ"),
                 ex("اِتَّصَلَ بِالشُّرْطَة ثُمَّ بِالشَّرِكَة.", "He called the police, then the company.", "ثُمَّ بِالشَّرِكَة"),
                 ex("أَيَّ طَرِيق نَأْخُذ: الْقَدِيم أَوِ الْجَدِيد؟", "Which road shall we take: the old or the new?", "أَوِ"),
                 ex("سَأَنْتَظِر فِي السَّيَّارَة أَوْ فِي الْمَقْهَى.", "I will wait in the car or in the café.", "أَوْ"),
             ]),
    ],
    exercises=[
        M("Which word means ‘or’?", "أَوْ", ["ثُمَّ", "فَ", "وَ"], "A choice."),
        M("Which word means ‘then, after a pause’?", "ثُمَّ", ["فَ", "أَوْ", "وَ"], "A pause between events."),
        M("What does فَـ add in أَوْقَفَ السَّيَّارَة فَنَزَلَ?", "a quick result", ["a choice", "a reason", "a condition"], "‘and at once’."),
        M("Why أَوِ الْجَدِيد?", "a helping kasra before الـ", ["a new word", "a plural ending", "a mistake"], "A final sukūn before الـ takes a helping vowel."),
        M("Which word is written joined to the next word?", "فَ", ["ثُمَّ", "أَوْ", "بَلْ"], "فَ and وَ are prefixes."),
        M("What does اِتَّصَلَ بِالشُّرْطَة ثُمَّ بِالشَّرِكَة mean?", "He called the police, then the company", ["He called the company, then the police", "He called both together", "He did not call anyone"], "ثُمَّ = then."),
        F("أَوْقَفَ السَّائِق السَّيَّارَة ___ نَزَلَ.", "فَ", ["أَوْ", "ثُمَّ"], "At once.", tr="The driver stopped the car and got out at once."),
        F("نَزَلَ السَّائِق ___ نَظَرَ إِلَى الْإِطَار.", "ثُمَّ", ["أَوْ", "لَكِنَّ"], "After a pause.", tr="The driver got out, then looked at the tyre."),
        F("سَأَنْتَظِر فِي السَّيَّارَة ___ فِي الْمَقْهَى.", "أَوْ", ["ثُمَّ", "فَ"], "A choice.", tr="I will wait in the car or in the café."),
        F("أَيَّ طَرِيق نَأْخُذ: الْقَدِيم ___ الْجَدِيد؟", "أَوِ", ["أَوْ", "ثُمَّ"], "Before الـ: أَوِ.", tr="Which road shall we take: the old or the new?"),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 439
L439 = lesson(
    "Comparing: faster, safer, lighter",
    "أَسْرَع مِنْ · أَخْطَر مِنْ · أَقَلّ",
    requires=["سريع", "بطيء", "خطير", "خفيف", "أقل", "أكثر", "طريق", "سيارة"],
    cards=[
        card("The أَفْعَل comparative",
             "You know the comparative pattern أَفْعَل, “more …”: أَسْرَع, “faster”, أَبْطَأ, “slower”, أَخْطَر, “more dangerous”, أَخَفّ, “lighter”, أَسْلَم, “safer”. "
             "The thing compared follows مِنْ, “than”. A comparative does not change for gender or number. The sentences are invented.",
             tables=[table(["English", "Positive", "Comparative"],
                           [["fast", "سَرِيع", "أَسْرَع"], ["slow", "بَطِيء", "أَبْطَأ"], ["dangerous", "خَطِير", "أَخْطَر"], ["light", "خَفِيف", "أَخَفّ"], ["safe", "سَلِيم", "أَسْلَم"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("السَّيَّارَة أَسْرَع مِنَ الشَّاحِنَة.", "The car is faster than the lorry.", "أَسْرَع مِنَ"),
                 ex("الطَّرِيق الْقَدِيم أَخْطَر مِنَ الطَّرِيق الْجَدِيد.", "The old road is more dangerous than the new road.", "أَخْطَر"),
                 ex("الْقِيَادَة الْبَطِيئَة أَسْلَم.", "Slow driving is safer.", "أَسْلَم"),
                 ex("كَانَتْ إِصَابَتُهُ أَخَفّ مِنْ إِصَابَتِي.", "His injury was lighter than mine.", "أَخَفّ"),
                 ex("هَذَا الْحَادِث أَقَلّ خَطَرًا مِنَ الْأَوَّل.", "This accident is less dangerous than the first.", "أَقَلّ خَطَرًا"),
             ]),
    ],
    exercises=[
        M("What does أَسْرَع مِنْ mean?", "faster than", ["as fast as", "slower than", "the fastest"], "أَفْعَل + مِنْ."),
        M("What is the comparative of بَطِيء?", "أَبْطَأ", ["أَبْطَاء", "بَطِيئَة", "بَطَأ"], "The comparative of بَطِيء."),
        M("What does أَخْطَر مِنَ الطَّرِيق الْجَدِيد mean?", "more dangerous than the new road", ["safer than the new road", "as long as the new road", "newer than the road"], "خَطِير = dangerous."),
        M("Does a comparative change for a feminine noun?", "no", ["yes, it adds ـَة", "yes, it adds ـُون", "yes, it is dual"], "أَفْعَل stays the same."),
        M("What does الْقِيَادَة الْبَطِيئَة أَسْلَم mean?", "slow driving is safer", ["fast driving is safer", "slow driving is cheaper", "driving is dangerous"], "أَسْلَم = safer."),
        M("What does أَقَلّ خَطَرًا mean?", "less dangerous", ["more dangerous", "as dangerous", "very dangerous"], "أَقَلّ = less."),
        F("السَّيَّارَة ___ مِنَ الشَّاحِنَة.", "أَسْرَع", ["سَرِيع", "السَّرِيع"], "The comparative.", tr="The car is faster than the lorry."),
        F("الطَّرِيق الْقَدِيم أَخْطَر ___ الطَّرِيق الْجَدِيد.", "مِنَ", ["عَنْ", "إِلَى"], "“than”.", tr="The old road is more dangerous than the new road."),
        F("كَانَتْ إِصَابَتُهُ ___ مِنْ إِصَابَتِي.", "أَخَفّ", ["خَفِيفَة", "أَخَفُّون"], "The comparative.", tr="His injury was lighter than mine."),
        F("الْقِيَادَة الْبَطِيئَة ___.", "أَسْلَم", ["سَلِيم", "سَلِيمَة"], "The comparative.", tr="Slow driving is safer."),
    ],
    verify=(),
)


# ---------------------------------------------------------------------------- 440
L440 = lesson(
    "How do you feel? Adjectives",
    "سَعِيد · حَزِين · غَاضِب · خَائِف · قَلِق · مُتْعَب · مُرْتَاح",
    requires=["سعيد", "حزين", "غاضب", "خائف", "قلق", "متعب", "مرتاح", "شعور"],
    cards=[
        card("Feelings are adjectives",
             "To say how you feel, use a noun phrase with no verb: أَنَا سَعِيد, “I am happy”. The adjective agrees with the person: add ـَة for a woman and ـُون for a group of men, ـَات for a group of women. "
             "To ask, use كَيْفَ تَشْعُر؟, “How do you feel?” (to a woman كَيْفَ تَشْعُرِين؟). Another way to say it: أَشْعُر بِـ + a noun, “I feel …”, as in أَشْعُر بِالتَّعَب, “I feel tired”. The sentences are invented.",
             tables=[table(["English", "Man", "Woman"],
                           [["happy", "سَعِيد", "سَعِيدَة"], ["sad", "حَزِين", "حَزِينَة"], ["angry", "غَاضِب", "غَاضِبَة"], ["afraid", "خَائِف", "خَائِفَة"],
                            ["worried", "قَلِق", "قَلِقَة"], ["tired", "مُتْعَب", "مُتْعَبَة"], ["comfortable", "مُرْتَاح", "مُرْتَاحَة"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("أَنَا سَعِيد الْيَوْم.", "I am happy today.", "سَعِيد"),
                 ex("هِيَ حَزِينَة لِأَنَّ أُخْتَهَا سَافَرَتْ.", "She is sad because her sister travelled.", "حَزِينَة"),
                 ex("لِمَاذَا أَنْتَ غَاضِب؟", "Why are you angry?", "غَاضِب"),
                 ex("هُمْ خَائِفُون مِنَ الْكَلْب.", "They are afraid of the dog.", "خَائِفُون"),
                 ex("كَيْفَ تَشْعُرِين الْآن؟", "How do you (f.) feel now?", "تَشْعُرِين"),
                 ex("أَشْعُر بِالتَّعَب.", "I feel tired.", "أَشْعُر بِالتَّعَب"),
                 ex("نَحْنُ مُرْتَاحُون فِي الْفُنْدُق.", "We are comfortable in the hotel.", "مُرْتَاحُون"),
             ]),
    ],
    exercises=[
        M("What does أَنَا سَعِيد الْيَوْم mean?", "I am happy today", ["I was happy yesterday", "I will be happy", "I am tired today"], "A noun phrase with no verb."),
        M("How does a woman say “I am sad”?", "أَنَا حَزِينَة", ["أَنَا حَزِين", "أَنَا حَزِينُون", "أَنَا حَزِينَات"], "Add ـَة for a woman."),
        M("What does خَائِف mean?", "afraid", ["angry", "tired", "happy"], "خَوْف = fear."),
        M("What does كَيْفَ تَشْعُرِين؟ ask?", "How do you (f.) feel?", ["Where do you live?", "What do you want?", "Who are you?"], "تَشْعُرِين is addressed to a woman."),
        M("What does أَشْعُر بِالتَّعَب mean?", "I feel tired", ["I feel hungry", "I feel happy", "I feel at home"], "تَعَب = tiredness."),
        M("What is the plural, for a group of men, of قَلِق?", "قَلِقُون", ["قَلِقَة", "قَلِقَات", "قَلِقَان"], "Sound masculine plural: ـُون."),
        F("هِيَ ___ لِأَنَّ أُخْتَهَا سَافَرَتْ.", "حَزِينَة", ["حَزِين", "حَزِينُون"], "A feminine subject.", tr="She is sad because her sister travelled."),
        F("لِمَاذَا أَنْتَ ___؟", "غَاضِب", ["غَاضِبَة", "غَاضِبُون"], "Said to a man.", tr="Why are you angry?"),
        F("هُمْ ___ مِنَ الْكَلْب.", "خَائِفُون", ["خَائِف", "خَائِفَة"], "A group of men.", tr="They are afraid of the dog."),
        F("نَحْنُ ___ فِي الْفُنْدُق.", "مُرْتَاحُون", ["مُرْتَاح", "مُرْتَاحَة"], "We (men or mixed).", tr="We are comfortable in the hotel."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 441
L441 = lesson(
    "Feelings as verbs",
    "فَرِحَ بِـ · حَزِنَ عَلَى · غَضِبَ مِنْ · خَافَ مِنْ · قَلِقَ عَلَى",
    requires=["فرح", "حزن", "غضب", "خاف", "قلق", "تعب", "خبر", "خوف"],
    cards=[
        card("Verbs of feeling and their prepositions",
             "Many feelings have a verb with a fixed preposition. فَرِحَ بِـ, “was glad about”. حَزِنَ عَلَى, “grieved for”. غَضِبَ مِنْ, “got angry at”. خَافَ مِنْ, “was afraid of”. قَلِقَ عَلَى, “worried about”. "
             "تَعِبَ, “got tired”, takes no preposition. The verb خَافَ is hollow, so “I was afraid” is خِفْتُ with a short vowel. To calm someone, use a negative command: لَا تَقْلَقْ, “don't worry”, لَا تَحْزَنْ, “don't be sad”, لَا تَخَفْ, “don't be afraid”. The sentences are invented.",
             tables=[table(["English", "Past (he)", "Present (he)"],
                           [["was glad", "فَرِحَ", "يَفْرَح"], ["grieved", "حَزِنَ", "يَحْزَن"], ["got angry", "غَضِبَ", "يَغْضَب"], ["worried", "قَلِقَ", "يَقْلَق"], ["got tired", "تَعِبَ", "يَتْعَب"], ["was afraid", "خَافَ", "يَخَاف"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("فَرِحْتُ بِالْخَبَر.", "I was glad about the news.", "فَرِحْتُ بِ"),
                 ex("حَزِنَتْ عَلَى جَدَّتِهَا.", "She grieved for her grandmother.", "حَزِنَتْ عَلَى"),
                 ex("غَضِبَ الْمُدِير مِنَ التَّأْخِير.", "The manager got angry at the delay.", "غَضِبَ الْمُدِير مِنَ"),
                 ex("خِفْتُ مِنَ السُّرْعَة.", "I was afraid of the speed.", "خِفْتُ"),
                 ex("قَلِقَتْ أُمِّي عَلَيَّ.", "My mother worried about me.", "قَلِقَتْ"),
                 ex("لَا تَقْلَقْ، كُلّ شَيْء بِخَيْر.", "Don't worry, everything is fine.", "لَا تَقْلَقْ"),
                 ex("لَا تَخَفْ.", "Don't be afraid.", "لَا تَخَفْ"),
             ]),
    ],
    exercises=[
        M("What does فَرِحْتُ بِالْخَبَر mean?", "I was glad about the news", ["I was angry about the news", "I heard the news", "I read the news"], "فَرِحَ بِـ = to be glad about."),
        M("Which preposition goes with حَزِنَ?", "عَلَى", ["بِ", "إِلَى", "فِي"], "حَزِنَ عَلَى = to grieve for."),
        M("What does غَضِبَ مِنَ التَّأْخِير mean?", "he got angry at the delay", ["he was glad about the delay", "he caused the delay", "he waited for the delay"], "غَضِبَ مِنْ = to get angry at."),
        M("How do you say “I was afraid”?", "خِفْتُ", ["خَافْتُ", "خَفْتُ", "يَخَاف"], "A hollow verb takes a short vowel before the ending."),
        M("What does لَا تَقْلَقْ mean?", "don't worry", ["worry", "I worry", "he worried"], "A negative command."),
        M("What does قَلِقَتْ أُمِّي عَلَيَّ mean?", "my mother worried about me", ["my mother called me", "my mother stayed with me", "my mother waited for me"], "قَلِقَ عَلَى = to worry about."),
        F("___ بِالْخَبَر.", "فَرِحْتُ", ["فَرِحَتْ", "فَرِحُوا"], "“I”.", tr="I was glad about the news.", lemma="فرح:past:ana"),
        F("حَزِنَتْ ___ جَدَّتِهَا.", "عَلَى", ["بِ", "إِلَى"], "The preposition for حَزِنَ.", tr="She grieved for her grandmother."),
        F("غَضِبَ الْمُدِير ___ التَّأْخِير.", "مِنَ", ["بِ", "إِلَى"], "The preposition for غَضِبَ.", tr="The manager got angry at the delay."),
        F("لَا ___، كُلّ شَيْء بِخَيْر.", "تَقْلَقْ", ["تَقْلَقُ", "قَلِقْتَ"], "Jussive after لَا.", tr="Don't worry, everything is fine."),
    ],
    verify=vv("فرح", "past", ana="فَرِحْتُ", huwa="فَرِحَ", hiya="فَرِحَتْ") + vv("خوف", "past", ana="خِفْتُ", huwa="خَافَ") + vv("قلق", "pres", huwa="يَقْلَق") + vv("حزن", "past", hiya="حَزِنَتْ") + vv("غضب", "past", huwa="غَضِبَ"),
)

# ---------------------------------------------------------------------------- 442
L442 = lesson(
    "Parts of the body",
    "رَأْس · عَيْن · أُذُن · أَنْف · فَم · يَد · رِجْل · ظَهْر · بَطْن",
    requires=["رأس", "عين", "أذن", "أنف", "فم", "يد", "رجل", "ظهر", "بطن", "صدر", "قلب", "حلق", "إنسان"],
    cards=[
        card("The body",
             "Learn the body parts with a pronoun ending: رَأْسِي, “my head”, يَدُكَ, “your hand”. Many paired parts are feminine: عَيْن, أُذُن, يَد, رِجْل. A pair is dual: عَيْنَان, “two eyes”, أُذُنَان, “two ears”, يَدَان, “two hands”, رِجْلَان, “two legs”. "
             "As the object of a verb, or after a preposition, the dual ends in ـَيْن: اِفْتَحْ عَيْنَيْكَ, “open your eyes”. The word سِنّ, “tooth”, has the plural أَسْنَان, “teeth”. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["head", "رَأْس"], ["eye", "عَيْن"], ["ear", "أُذُن"], ["nose", "أَنْف"], ["mouth", "فَم"], ["throat", "حَلْق"], ["hand", "يَد"], ["leg", "رِجْل"],
                            ["back", "ظَهْر"], ["stomach", "بَطْن"], ["chest", "صَدْر"], ["heart", "قَلْب"], ["teeth", "أَسْنَان"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("لِلْإِنْسَان عَيْنَان وَأُذُنَان وَيَدَان وَرِجْلَان.", "A person has two eyes, two ears, two hands and two legs.", "عَيْنَان"),
                 ex("اِفْتَحْ فَمَكَ مِنْ فَضْلِك.", "Open your mouth, please.", "فَمَكَ"),
                 ex("ضَعْ يَدَكَ عَلَى صَدْرِكَ.", "Put your hand on your chest.", "يَدَكَ"),
                 ex("اِغْسِلْ يَدَيْكَ قَبْلَ الْأَكْل.", "Wash your hands before eating.", "يَدَيْكَ"),
                 ex("أَنْفُهُ كَبِير.", "His nose is big.", "أَنْفُهُ"),
                 ex("أُنَظِّفُ أَسْنَانِي بَعْدَ الْأَكْل.", "I brush my teeth after eating.", "أَسْنَانِي"),
             ]),
    ],
    exercises=[
        M("What is عَيْن?", "an eye", ["an ear", "a nose", "a mouth"], "عَيْن, dual عَيْنَان."),
        M("What does ظَهْر mean?", "back", ["chest", "stomach", "head"], "Do not confuse it with the noon prayer time."),
        M("What are أَسْنَان?", "teeth", ["hands", "ears", "legs"], "The plural of سِنّ."),
        M("What is the dual of أُذُن (as a subject)?", "أُذُنَان", ["أُذُنُون", "أُذُنَات", "آذَان"], "Dual: ـَان."),
        M("What does اِفْتَحْ فَمَكَ mean?", "open your mouth", ["close your eyes", "wash your hands", "turn your head"], "فَم = mouth."),
        M("Why is it اِغْسِلْ يَدَيْكَ, with ـَيْ?", "the dual as the object of a verb ends in ـَيْن", ["it is a plural", "it is a question", "it is feminine"], "The dual in the accusative: ـَيْن."),
        F("لِلْإِنْسَان ___ وَأُذُنَان.", "عَيْنَان", ["عَيْن", "أَنْف"], "Two eyes.", tr="A person has two eyes and two ears."),
        F("ضَعْ يَدَكَ عَلَى ___.", "صَدْرِكَ", ["ظَهْرِكَ", "فَمِكَ"], "The chest.", tr="Put your hand on your chest."),
        F("اِفْتَحْ ___ مِنْ فَضْلِك.", "فَمَكَ", ["قَلْبَكَ", "ظَهْرَكَ"], "Open the mouth.", tr="Open your mouth, please."),
        F("أُنَظِّفُ ___ بَعْدَ الْأَكْل.", "أَسْنَانِي", ["أَنْفِي", "رِجْلِي"], "Brushing teeth.", tr="I brush my teeth after eating."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 443
L443 = lesson(
    "Aches and symptoms",
    "عِنْدِي صُدَاع · عِنْدَهُ حُمَّى · أَلَم فِي ظَهْرِي",
    requires=["صداع", "حمى", "دوار", "ألم", "مريض", "شديد", "منذ"],
    cards=[
        card("Saying what is wrong",
             "Arabic says “I have” with عِنْدِي: عِنْدِي صُدَاع, “I have a headache”. The symptoms: صُدَاع, “headache”, حُمَّى, “fever”, سُعَال, “cough”, زُكَام, “a cold”, إِسْهَال, “diarrhoea”, دُوَار, “dizziness”. "
             "For a pain in a place: عِنْدِي أَلَم فِي + the part, “I have a pain in …”. “Since” is مُنْذُ + a time: مُنْذُ يَوْمَيْن, “for two days”. To deny: لَيْسَ عِنْدِي حُمَّى, “I have no fever”. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["headache", "صُدَاع"], ["fever", "حُمَّى"], ["cough", "سُعَال"], ["a cold", "زُكَام"], ["diarrhoea", "إِسْهَال"], ["dizziness", "دُوَار"], ["pain", "أَلَم"], ["sick", "مَرِيض"], ["severe", "شَدِيد"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("عِنْدِي صُدَاع شَدِيد.", "I have a severe headache.", "صُدَاع شَدِيد"),
                 ex("عِنْدَهُ حُمَّى وَسُعَال.", "He has a fever and a cough.", "عِنْدَهُ"),
                 ex("عِنْدِي أَلَم فِي ظَهْرِي.", "I have a pain in my back.", "أَلَم فِي ظَهْرِي"),
                 ex("أَنَا مَرِيض مُنْذُ يَوْمَيْن.", "I have been ill for two days.", "مُنْذُ يَوْمَيْن"),
                 ex("لَيْسَ عِنْدِي حُمَّى.", "I have no fever.", "لَيْسَ عِنْدِي"),
                 ex("هَلْ عِنْدَكِ دُوَار؟", "Do you (f.) have dizziness?", "عِنْدَكِ"),
             ]),
    ],
    exercises=[
        M("What does عِنْدِي صُدَاع mean?", "I have a headache", ["I have a fever", "I have a cough", "I have a cold"], "عِنْدِي = I have."),
        M("What is حُمَّى?", "a fever", ["a cough", "a cold", "a pain"], "Often with a cough."),
        M("What does عِنْدَهُ حُمَّى وَسُعَال mean?", "he has a fever and a cough", ["she has a cold", "he has a headache", "I have a fever"], "عِنْدَهُ = he has."),
        M("What does مُنْذُ يَوْمَيْن mean?", "for two days", ["in two days", "two days ago", "every two days"], "مُنْذُ = since, for."),
        M("How do you say “I have no fever”?", "لَيْسَ عِنْدِي حُمَّى", ["عِنْدِي حُمَّى", "لَا عِنْدِي حُمَّى", "لَمْ عِنْدِي حُمَّى"], "لَيْسَ + عِنْدِي."),
        M("What does عِنْدِي أَلَم فِي ظَهْرِي mean?", "I have a pain in my back", ["I have a pain in my head", "I have a cough", "I was in the back"], "أَلَم = pain."),
        F("___ صُدَاع شَدِيد.", "عِنْدِي", ["أَنَا", "مَعِي"], "“I have”.", tr="I have a severe headache."),
        F("عِنْدَهُ ___ وَسُعَال.", "حُمَّى", ["صُدَاع", "دُوَار"], "A fever.", tr="He has a fever and a cough."),
        F("أَنَا مَرِيض ___ يَوْمَيْن.", "مُنْذُ", ["بَعْدَ", "قَبْلَ"], "“For”.", tr="I have been ill for two days."),
        F("___ عِنْدِي حُمَّى.", "لَيْسَ", ["لَا", "لَمْ"], "Negating “have”.", tr="I have no fever."),
        F("هَلْ ___ دُوَار؟", "عِنْدَكِ", ["عِنْدَكَ", "عِنْدِي"], "To a woman.", tr="Do you (f.) have dizziness?"),
    ],
    verify=(),
)


# ---------------------------------------------------------------------------- 444
L444 = lesson(
    "Asking about someone's health",
    "كَيْفَ صِحَّتُكَ؟ · مَا بِكَ؟ · لَسْتُ بِخَيْر",
    requires=["صحة", "مريض", "تحسن", "فرح", "تعب", "طبيب", "راحة"],
    cards=[
        card("How is your health?",
             "To ask about health: كَيْفَ صِحَّتُكَ؟, “How is your health?”, or هَلْ أَنْتَ بِخَيْر؟, “Are you well?” A usual answer is الْحَمْدُ لِلَّه, أَنَا بِخَيْر, “Thank God, I'm fine”. "
             "If someone looks unwell, ask مَا بِكَ؟, “What is wrong with you?” (to a woman مَا بِكِ؟). To say you are not well: لَسْتُ بِخَيْر, with بِ before the noun. To say you are better: أَنَا أَفْضَل الْيَوْم. "
             "Health that improves is تَحَسَّنَتْ صِحَّتُهُ, “his health improved” (Measure V). The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["How is your health?", "كَيْفَ صِحَّتُكَ؟"], ["Are you well?", "هَلْ أَنْتَ بِخَيْر؟"], ["Thank God, I'm fine.", "الْحَمْدُ لِلَّه، أَنَا بِخَيْر."], ["What is wrong with you?", "مَا بِكَ؟"],
                            ["I am not well.", "لَسْتُ بِخَيْر."], ["I am better today.", "أَنَا أَفْضَل الْيَوْم."]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("كَيْفَ صِحَّتُكَ يَا أَخِي؟", "How is your health, brother?", "صِحَّتُكَ"),
                 ex("هَلْ أَنْتِ بِخَيْر؟", "Are you (f.) well?", "بِخَيْر"),
                 ex("مَا بِكِ؟ تَبْدِينَ حَزِينَة.", "What is wrong with you (f.)? You look sad.", "مَا بِكِ"),
                 ex("لَسْتُ بِخَيْر الْيَوْم.", "I am not well today.", "لَسْتُ بِخَيْر"),
                 ex("الْحَمْدُ لِلَّه، أَنَا أَفْضَل الْيَوْم.", "Thank God, I am better today.", "أَفْضَل"),
                 ex("تَحَسَّنَتْ صِحَّتُهُ كَثِيرًا.", "His health improved a lot.", "تَحَسَّنَتْ"),
             ]),
    ],
    exercises=[
        M("What does كَيْفَ صِحَّتُكَ؟ ask?", "How is your health?", ["Where is your house?", "What is your job?", "When did you arrive?"], "صِحَّة = health."),
        M("How do you reply that you are fine?", "الْحَمْدُ لِلَّه، أَنَا بِخَيْر", ["لَسْتُ بِخَيْر", "مَا بِكَ؟", "كَيْفَ صِحَّتُكَ؟"], "بِخَيْر = well."),
        M("What does مَا بِكِ؟ ask?", "What is wrong with you (f.)?", ["Who are you (f.)?", "Where are you (f.) going?", "What do you (f.) want?"], "The final ـِ marks a woman."),
        M("What does لَسْتُ بِخَيْر mean?", "I am not well", ["I am very well", "I will not come", "I did not say"], "لَسْتُ + بِ."),
        M("What does أَنَا أَفْضَل الْيَوْم mean?", "I am better today", ["I am worse today", "I am busy today", "I am free today"], "أَفْضَل = better."),
        M("What does تَحَسَّنَتْ صِحَّتُهُ mean?", "his health improved", ["his health worsened", "his doctor arrived", "he is on holiday"], "تَحَسَّنَ = to improve."),
        F("كَيْفَ ___ يَا أَخِي؟", "صِحَّتُكَ", ["صِحَّتُكِ", "مَرِيضُكَ"], "Said to a man.", tr="How is your health, brother?"),
        F("هَلْ أَنْتِ ___؟", "بِخَيْر", ["خَيْر", "خَيْرَة"], "With بِ.", tr="Are you (f.) well?"),
        F("لَسْتُ ___ خَيْر الْيَوْم.", "بِ", ["فِي", "مِنْ"], "After لَيْسَ.", tr="I am not well today."),
        F("___ صِحَّتُهُ كَثِيرًا.", "تَحَسَّنَتْ", ["تَحَسَّنَ", "تَحَسَّنْتُ"], "صِحَّة is feminine.", tr="His health improved a lot.", lemma="حسن#5:past:hiya"),
    ],
    verify=vv("حسن#5", "past", hiya="تَحَسَّنَتْ", huwa="تَحَسَّنَ", ana="تَحَسَّنْتُ"),
)

# ---------------------------------------------------------------------------- 445
L445 = lesson(
    "At the doctor's",
    "مَوْعِد عِنْدَ الطَّبِيب · ضَغْط الدَّم · تَحْلِيل الدَّم",
    requires=["طبيب", "موعد", "عيادة", "فحص", "ضغط", "دم", "حرارة", "تحليل", "تأمين"],
    cards=[
        card("A visit to the clinic",
             "You book an appointment: أُرِيد مَوْعِدًا عِنْدَ الطَّبِيب. In the clinic the doctor checks you: يَفْحَص الطَّبِيب الْمَرِيض. Common checks: ضَغْط الدَّم, “blood pressure”, دَرَجَة الْحَرَارَة, “temperature”, تَحْلِيل الدَّم, “a blood test”. "
             "The cost of treatment may be covered by تَأْمِين صِحِّي, “health insurance”. A clinic is عِيَادَة. The dialogue is invented.",
             tables=[table(["English", "Arabic"],
                           [["appointment", "مَوْعِد"], ["clinic", "عِيَادَة"], ["check-up", "فَحْص"], ["blood pressure", "ضَغْط الدَّم"], ["temperature", "دَرَجَة الْحَرَارَة"], ["blood test", "تَحْلِيل الدَّم"], ["health insurance", "تَأْمِين صِحِّي"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُرِيد مَوْعِدًا عِنْدَ الطَّبِيب.", "I want an appointment with the doctor.", "مَوْعِدًا"),
                 ex("مَوْعِدُكَ غَدًا فِي الْعَاشِرَة.", "Your appointment is tomorrow at ten.", "مَوْعِدُكَ"),
                 ex("يَفْحَص الطَّبِيب الْمَرِيض.", "The doctor examines the patient.", "يَفْحَص"),
                 ex("ضَغْط الدَّم عِنْدَكَ طَبِيعِيّ.", "Your blood pressure is normal.", "ضَغْط الدَّم"),
                 ex("دَرَجَة حَرَارَتِكَ مُرْتَفِعَة قَلِيلًا.", "Your temperature is a little high.", "مُرْتَفِعَة"),
                 ex("نَحْتَاج إِلَى تَحْلِيل الدَّم.", "We need a blood test.", "تَحْلِيل الدَّم"),
                 ex("هَلْ عِنْدَكَ تَأْمِين صِحِّي؟", "Do you have health insurance?", "تَأْمِين صِحِّي"),
             ]),
    ],
    exercises=[
        M("What does مَوْعِد mean?", "appointment", ["medicine", "clinic", "insurance"], "مَوْعِد = an appointed time."),
        M("What does أُرِيد مَوْعِدًا عِنْدَ الطَّبِيب mean?", "I want an appointment with the doctor", ["I want medicine from the doctor", "I want to be a doctor", "I want a new clinic"], "عِنْدَ = at, with."),
        M("What does يَفْحَص الطَّبِيب الْمَرِيض mean?", "the doctor examines the patient", ["the doctor visits the patient", "the doctor calls the patient", "the patient pays the doctor"], "فَحَصَ = to examine."),
        M("What is ضَغْط الدَّم?", "blood pressure", ["a blood test", "a fever", "a pain"], "ضَغْط = pressure; دَم = blood."),
        M("What does دَرَجَة الْحَرَارَة mean?", "temperature", ["pressure", "a prescription", "a weight"], "دَرَجَة = degree."),
        M("What is تَأْمِين صِحِّي?", "health insurance", ["a health check", "a clinic", "a medicine"], "تَأْمِين = insurance."),
        F("أُرِيد ___ عِنْدَ الطَّبِيب.", "مَوْعِدًا", ["مَوْعِد", "مَوْعِدُون"], "Accusative object.", tr="I want an appointment with the doctor."),
        F("يَفْحَص ___ الْمَرِيض.", "الطَّبِيب", ["الدَّوَاء", "الْمَوْعِد"], "The doctor examines.", tr="The doctor examines the patient."),
        F("نَحْتَاج إِلَى ___ الدَّم.", "تَحْلِيل", ["ضَغْط", "مَوْعِد"], "A blood test.", tr="We need a blood test."),
        F("دَرَجَة حَرَارَتِكَ ___ قَلِيلًا.", "مُرْتَفِعَة", ["مُرْتَفِع", "مُرْتَفِعُون"], "دَرَجَة is feminine.", tr="Your temperature is a little high."),
    ],
    verify=(),
)

# ---------------------------------------------------------------------------- 446
L446 = lesson(
    "The doctor's advice",
    "اِشْرَبْ مَاءً · نَمْ · لَا تَأْكُلْ · يَجِب أَنْ",
    requires=["شرب", "نوم", "ماء", "راحة", "نصيحة", "طبيب"],
    cards=[
        card("Commands and “you must”",
             "Doctors speak in commands. To a man: اِشْرَبْ مَاءً كَثِيرًا, “drink a lot of water”, نَمْ مُبَكِّرًا, “sleep early”. To several people: اِشْرَبُوا. To forbid: لَا تَشْرَبْ, and before الـ the final sukūn takes a helping kasra: لَا تَشْرَبِ الْقَهْوَة. "
             "Another way is يَجِب أَنْ + subjunctive, “you must …”: يَجِب أَنْ تَنَامَ، “you must sleep”, or عَلَيْكَ أَنْ تَسْتَرِيحَ, “you should rest”. The sentences are invented.",
             tables=[table(["English", "To a man", "Not to a man"],
                           [["drink", "اِشْرَبْ", "لَا تَشْرَبْ"], ["sleep", "نَمْ", "لَا تَنَمْ"], ["eat", "كُلْ", "لَا تَأْكُلْ"], ["go", "اِذْهَبْ", "لَا تَذْهَبْ"], ["work", "اِعْمَلْ", "لَا تَعْمَلْ"]],
                           say=[1, 2], tlit=[1, 2], gloss=False)],
             examples=[
                 ex("اِشْرَبْ مَاءً كَثِيرًا.", "Drink a lot of water.", "اِشْرَبْ"),
                 ex("نَمْ مُبَكِّرًا.", "Sleep early.", "نَمْ"),
                 ex("لَا تَشْرَبِ الْقَهْوَة.", "Don't drink coffee.", "لَا تَشْرَبِ"),
                 ex("اِشْرَبُوا الْمَاء.", "Drink the water (all of you).", "اِشْرَبُوا"),
                 ex("يَجِب أَنْ تَنَامَ ثَمَانِي سَاعَات.", "You must sleep eight hours.", "أَنْ تَنَامَ"),
                 ex("عَلَيْكَ أَنْ تَسْتَرِيحَ فِي الْبَيْت.", "You should rest at home.", "عَلَيْكَ أَنْ"),
                 ex("لَا تَذْهَبْ إِلَى الْعَمَل غَدًا.", "Don't go to work tomorrow.", "لَا تَذْهَبْ"),
             ]),
    ],
    exercises=[
        M("What does اِشْرَبْ مَاءً كَثِيرًا mean?", "drink a lot of water", ["pour a lot of water", "buy water", "don't drink water"], "A command."),
        M("What does لَا تَشْرَبِ الْقَهْوَة mean?", "don't drink coffee", ["drink coffee", "I drank coffee", "he drinks coffee"], "لَا + jussive forbids."),
        M("Why the kasra in لَا تَشْرَبِ الْقَهْوَة?", "a helping vowel before الـ", ["a plural ending", "a question", "a feminine ending"], "A final sukūn before الـ takes a kasra."),
        M("How do you tell several people to drink?", "اِشْرَبُوا", ["اِشْرَبْ", "تَشْرَبُ", "شَرِبْتُ"], "The group imperative ends in ـُوا."),
        M("What does يَجِب أَنْ تَنَامَ mean?", "you must sleep", ["you slept", "you want to sleep", "he sleeps"], "يَجِب أَنْ = must."),
        M("What does عَلَيْكَ أَنْ تَسْتَرِيحَ mean?", "you should rest", ["you rested", "you are tired", "I rest"], "عَلَى + pronoun + أَنْ = should."),
        F("___ مَاءً كَثِيرًا.", "اِشْرَبْ", ["تَشْرَبُ", "شَرِبْتَ"], "A command.", tr="Drink a lot of water.", lemma="شرب:imp:anta"),
        F("لَا ___ الْقَهْوَة.", "تَشْرَبِ", ["تَشْرَبُ", "اِشْرَبْ"], "After لَا, jussive with a helping vowel.", tr="Don't drink coffee."),
        F("يَجِب أَنْ ___ ثَمَانِي سَاعَات.", "تَنَامَ", ["تَنَامُ", "نَامَ"], "After أَنْ, the subjunctive.", tr="You must sleep eight hours."),
        F("___ أَنْ تَسْتَرِيحَ فِي الْبَيْت.", "عَلَيْكَ", ["عِنْدَكَ", "مَعَكَ"], "“You should”.", tr="You should rest at home."),
    ],
    verify=vv("شرب", "imp", anta="اِشْرَبْ", antum="اِشْرَبُوا") + vv("شرب", "neg", anta="لَا تَشْرَبْ") + vv("ذهب", "neg", anta="لَا تَذْهَبْ") + vv("عمل", "imp", anta="اِعْمَلْ") + vv("نوم", "sub", anta="تَنَامَ") + vv("نوم", "imp", anta="نَمْ"),
)

# ---------------------------------------------------------------------------- 447
L447 = lesson(
    "At the hospital",
    "غُرْفَة · سَرِير · عَمَلِيَّة · الطَّوَارِئ",
    requires=["مستشفى", "غرفة", "سرير", "عملية", "ممرض", "طبيب", "مريض", "خرج", "دخل"],
    cards=[
        card("Inside the hospital",
             "A patient enters the hospital: دَخَلَ الْمُسْتَشْفَى. He leaves it: خَرَجَ مِنَ الْمُسْتَشْفَى. In an emergency you go to الطَّوَارِئ, “the emergency department”, and call the ambulance: اِتَّصِلْ بِالْإِسْعَاف. "
             "Rooms and beds: غُرْفَة, سَرِير. A nurse is مُمَرِّض (m.) or مُمَرِّضَة (f.). An operation is عَمَلِيَّة. The future uses سَـ: سَيَبْقَى ثَلَاثَة أَيَّام, “he will stay three days”. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["hospital", "مُسْتَشْفَى"], ["emergency department", "الطَّوَارِئ"], ["room", "غُرْفَة"], ["bed", "سَرِير"], ["nurse (f.)", "مُمَرِّضَة"], ["operation", "عَمَلِيَّة"], ["he entered", "دَخَلَ"], ["he left", "خَرَجَ"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("دَخَلَ الْمَرِيض الْمُسْتَشْفَى مَسَاءَ أَمْسِ.", "The patient entered the hospital yesterday evening.", "دَخَلَ"),
                 ex("اِتَّصِلْ بِالْإِسْعَاف فَوْرًا.", "Call the ambulance at once.", "اِتَّصِلْ"),
                 ex("غُرْفَتُهُ فِي الطَّابِق الثَّانِي.", "His room is on the second floor.", "غُرْفَتُهُ"),
                 ex("سَيَبْقَى فِي الْمُسْتَشْفَى ثَلَاثَة أَيَّام.", "He will stay in the hospital for three days.", "سَيَبْقَى"),
                 ex("سَتَكُون الْعَمَلِيَّة غَدًا صَبَاحًا.", "The operation will be tomorrow morning.", "الْعَمَلِيَّة"),
                 ex("مَتَى يَخْرُج مِنَ الْمُسْتَشْفَى؟", "When will he leave the hospital?", "يَخْرُج"),
             ]),
    ],
    exercises=[
        M("What does دَخَلَ الْمَرِيض الْمُسْتَشْفَى mean?", "the patient entered the hospital", ["the patient left the hospital", "the doctor entered", "the patient called"], "دَخَلَ = entered."),
        M("What does اِتَّصِلْ بِالْإِسْعَاف فَوْرًا mean?", "call the ambulance at once", ["wait for the ambulance", "drive to the hospital slowly", "the ambulance arrived"], "فَوْرًا = at once."),
        M("What is مُمَرِّضَة?", "a nurse (f.)", ["a doctor (f.)", "a patient (f.)", "a teacher (f.)"], "Ends in ـَة, so a woman."),
        M("What does سَيَبْقَى ثَلَاثَة أَيَّام mean?", "he will stay three days", ["he stayed three days", "he stays every three days", "he left after three days"], "سَـ marks the future."),
        M("What is عَمَلِيَّة here?", "an operation", ["a trip", "a meeting", "a payment"], "A medical operation."),
        M("What does مَتَى يَخْرُج؟ ask?", "when will he leave?", ["where will he go?", "who will leave?", "why did he enter?"], "خَرَجَ = left."),
        F("___ الْمَرِيض الْمُسْتَشْفَى مَسَاءَ أَمْسِ.", "دَخَلَ", ["خَرَجَ", "يَدْخُل"], "He entered.", tr="The patient entered the hospital yesterday evening.", lemma="دخل:past:huwa"),
        F("غُرْفَتُهُ فِي ___ الثَّانِي.", "الطَّابِق", ["السَّرِير", "الطَّوَارِئ"], "The floor.", tr="His room is on the second floor."),
        F("___ فِي الْمُسْتَشْفَى ثَلَاثَة أَيَّام.", "سَيَبْقَى", ["بَقِيَ", "يَبْقَى"], "Future with سَـ.", tr="He will stay in the hospital for three days."),
        F("مَتَى ___ مِنَ الْمُسْتَشْفَى؟", "يَخْرُج", ["خَرَجْتُ", "اُخْرُجْ"], "A present verb.", tr="When will he leave the hospital?"),
    ],
    verify=vv("دخل", "past", huwa="دَخَلَ") + vv("خرج", "pres", huwa="يَخْرُج"),
)

# ---------------------------------------------------------------------------- 448
L448 = lesson(
    "At the pharmacy",
    "صَيْدَلِيَّة · دَوَاء · وَصْفَة · كَمْ مَرَّة؟",
    requires=["دواء", "قرص", "شراب", "صداع", "مرة", "يوم", "قبل", "بعد", "وجبة"],
    cards=[
        card("Buying medicine",
             "The pharmacy is صَيْدَلِيَّة and the pharmacist is صَيْدَلِيّ. You ask for medicine: أُرِيد دَوَاءً لِلصُّدَاع, “I want medicine for a headache”. Forms of medicine: قُرْص, “tablet”, شَرَاب, “syrup”. "
             "The pharmacist asks about the prescription: هَلْ مَعَكَ وَصْفَة طِبِّيَّة؟ and tells you how often: ثَلَاث مَرَّات فِي الْيَوْم, “three times a day”, بَعْدَ الْأَكْل, “after eating”, قَبْلَ النَّوْم, “before sleep”. The dialogue is invented.",
             tables=[table(["English", "Arabic"],
                           [["pharmacy", "صَيْدَلِيَّة"], ["medicine", "دَوَاء"], ["tablet", "قُرْص"], ["syrup", "شَرَاب"], ["prescription", "وَصْفَة طِبِّيَّة"], ["three times a day", "ثَلَاث مَرَّات فِي الْيَوْم"], ["after the meal", "بَعْدَ الْوَجْبَة"], ["before sleep", "قَبْلَ النَّوْم"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أُرِيد دَوَاءً لِلصُّدَاع.", "I want medicine for a headache.", "دَوَاءً"),
                 ex("هَلْ مَعَكَ وَصْفَة طِبِّيَّة؟", "Do you have a prescription?", "وَصْفَة طِبِّيَّة"),
                 ex("خُذْ قُرْصًا وَاحِدًا بَعْدَ الْأَكْل.", "Take one tablet after eating.", "قُرْصًا وَاحِدًا"),
                 ex("كَمْ مَرَّة فِي الْيَوْم؟", "How many times a day?", "كَمْ مَرَّة"),
                 ex("ثَلَاث مَرَّات فِي الْيَوْم.", "Three times a day.", "ثَلَاث مَرَّات"),
                 ex("هَذَا الشَّرَاب لِلسُّعَال.", "This syrup is for a cough.", "لِلسُّعَال"),
                 ex("اِشْرَبْهُ قَبْلَ النَّوْم.", "Drink it before sleep.", "اِشْرَبْهُ"),
             ]),
    ],
    exercises=[
        M("What is a قُرْص?", "a tablet", ["a syrup", "a prescription", "a bed"], "قُرْص = tablet."),
        M("What does أُرِيد دَوَاءً لِلصُّدَاع mean?", "I want medicine for a headache", ["I want a doctor for a headache", "I have no headache", "I gave medicine"], "لِـ = for."),
        M("What does هَلْ مَعَكَ وَصْفَة؟ ask?", "Do you have a prescription?", ["Do you have insurance?", "Do you have a bed?", "Do you have a headache?"], "مَعَكَ = with you."),
        M("What does ثَلَاث مَرَّات فِي الْيَوْم mean?", "three times a day", ["three days a week", "in three days", "for three hours"], "مَرَّة = a time."),
        M("What does بَعْدَ الْأَكْل mean?", "after eating", ["before eating", "while eating", "instead of eating"], "بَعْدَ = after."),
        M("What does قَبْلَ النَّوْم mean?", "before sleep", ["after sleep", "during the day", "after work"], "قَبْلَ = before."),
        F("أُرِيد ___ لِلصُّدَاع.", "دَوَاءً", ["دَوَاء", "صَيْدَلِيّ"], "Accusative object.", tr="I want medicine for a headache."),
        F("هَلْ مَعَكَ ___ طِبِّيَّة؟", "وَصْفَة", ["وَصْفَات", "قُرْص"], "A prescription.", tr="Do you have a prescription?"),
        F("كَمْ ___ فِي الْيَوْم؟", "مَرَّة", ["مَرَّات", "يَوْم"], "After كَمْ: singular.", tr="How many times a day?"),
        F("اِشْرَبْهُ ___ النَّوْم.", "قَبْلَ", ["بَعْدَ", "مِنْ"], "Before sleep.", tr="Drink it before sleep."),
    ],
    verify=vv("شرب", "imp", anta="اِشْرَبْ"),
)

# ---------------------------------------------------------------------------- 449
L449 = lesson(
    "Reading a medicine label",
    "الْجُرْعَة · تَحْذِير · الْآثَار الْجَانِبِيَّة · يُحْفَظ",
    requires=["جرعة", "تحذير", "ممنوع", "حامل", "وجبة", "تاريخ", "دواء", "يوم"],
    cards=[
        card("Label language",
             "A label speaks in the passive and in short phrases. الْجُرْعَة, “the dose”: قُرْص وَاحِد مَرَّتَيْن فِي الْيَوْم. يُؤْخَذ بَعْدَ الْأَكْل, “is taken after eating”. "
             "A warning: تَحْذِير. Something forbidden: مَمْنُوع, and “for … it is not allowed”: لَا يُسْتَخْدَم لِلْأَطْفَال. Storage: يُحْفَظ بَعِيدًا عَنِ الْأَطْفَال, “is kept away from children”. "
             "Dates: تَارِيخ الِانْتِهَاء, “expiry date”. The passive present has the prefix يُـ and a fatḥa on the second root letter: يُؤْخَذ, يُحْفَظ. The labels are invented.",
             tables=[table(["English", "Arabic"],
                           [["the dose", "الْجُرْعَة"], ["warning", "تَحْذِير"], ["forbidden", "مَمْنُوع"], ["expiry date", "تَارِيخ الِانْتِهَاء"], ["is taken", "يُؤْخَذ"], ["is kept", "يُحْفَظ"], ["is not used", "لَا يُسْتَخْدَم"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("الْجُرْعَة: قُرْص وَاحِد مَرَّتَيْن فِي الْيَوْم.", "Dose: one tablet twice a day.", "الْجُرْعَة"),
                 ex("يُؤْخَذ بَعْدَ الْأَكْل.", "Take after eating (lit. is taken after eating).", "يُؤْخَذ"),
                 ex("تَحْذِير: لَا يُسْتَخْدَم لِلْأَطْفَال.", "Warning: not to be used for children.", "لَا يُسْتَخْدَم"),
                 ex("يُحْفَظ بَعِيدًا عَنِ الْأَطْفَال.", "Keep away from children.", "يُحْفَظ"),
                 ex("تَارِيخ الِانْتِهَاء مَكْتُوب هُنَا.", "The expiry date is written here.", "تَارِيخ الِانْتِهَاء"),
                 ex("مَمْنُوع لِلْحَامِل.", "Not allowed for a pregnant woman.", "مَمْنُوع"),
             ]),
    ],
    exercises=[
        M("What is الْجُرْعَة?", "the dose", ["the warning", "the date", "the price"], "جُرْعَة = dose."),
        M("What does يُؤْخَذ بَعْدَ الْأَكْل mean?", "is taken after eating", ["is bought after eating", "is given before eating", "is eaten"], "A passive verb."),
        M("What does تَحْذِير mean?", "warning", ["price", "dose", "invitation"], "حَذَّرَ = to warn."),
        M("What does مَمْنُوع لِلْحَامِل mean?", "not allowed for a pregnant woman", ["good for a pregnant woman", "taken by a doctor", "sold in a pharmacy"], "مَمْنُوع = forbidden."),
        M("What does يُحْفَظ بَعِيدًا عَنِ الْأَطْفَال mean?", "is kept away from children", ["is given to children", "is sold to children", "is taken with children"], "حَفِظَ = to keep."),
        M("What is تَارِيخ الِانْتِهَاء?", "the expiry date", ["the starting date", "the birth date", "the price list"], "اِنْتِهَاء = ending."),
        F("___: قُرْص وَاحِد مَرَّتَيْن فِي الْيَوْم.", "الْجُرْعَة", ["التَّحْذِير", "الشَّرَاب"], "The dose.", tr="Dose: one tablet twice a day."),
        F("___ بَعْدَ الْأَكْل.", "يُؤْخَذ", ["يَأْخُذ", "أَخَذَ"], "The passive.", tr="Take after eating."),
        F("يُحْفَظ ___ عَنِ الْأَطْفَال.", "بَعِيدًا", ["قَرِيبًا", "بَعِيد"], "Away from.", tr="Keep away from children."),
        F("تَحْذِير: ___ يُسْتَخْدَم لِلْأَطْفَال.", "لَا", ["لَمْ", "لَنْ"], "A present negative.", tr="Warning: not to be used for children."),
    ],
    verify=(),
)


# ---------------------------------------------------------------------------- 450
L450 = lesson(
    "Get well soon: visiting a patient",
    "سَلَامَتُكَ · شَافَاكَ اللَّه · زُرْنَا صَدِيقَنَا",
    requires=["سلامة", "شفاء", "زيارة", "زهور", "هدية", "صديق", "مستشفى", "زار", "حضر"],
    cards=[
        card("Wishing someone well",
             "To a sick person people say سَلَامَتُكَ, “your safety”, meaning “get well”, and شَافَاكَ اللَّه, “may God heal you”. A longer wish: أَتَمَنَّى لَكَ الشِّفَاء الْعَاجِل, “I wish you a quick recovery”. "
             "When you visit, you say زُرْتُكَ لِأَطْمَئِنَّ عَلَيْكَ, or simply جِئْتُ لِزِيَارَتِكَ, “I came to visit you”. You may bring flowers, زُهُور, or a gift, هَدِيَّة: أَحْضَرْنَا لَهُ زُهُورًا. "
             "These phrases are common and polite; wording varies from place to place. The sentences are invented.",
             tables=[table(["English", "Arabic"],
                           [["get well (lit. your safety)", "سَلَامَتُكَ"], ["may God heal you", "شَافَاكَ اللَّه"], ["a quick recovery", "الشِّفَاء الْعَاجِل"], ["visit", "زِيَارَة"], ["flowers", "زُهُور"], ["a gift", "هَدِيَّة"], ["I visited", "زُرْتُ"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("سَلَامَتُكَ يَا صَدِيقِي!", "Get well, my friend!", "سَلَامَتُكَ"),
                 ex("شَافَاكَ اللَّه وَعَافَاكَ.", "May God heal you and keep you well.", "شَافَاكَ"),
                 ex("أَتَمَنَّى لَكَ الشِّفَاء الْعَاجِل.", "I wish you a quick recovery.", "الشِّفَاء الْعَاجِل"),
                 ex("زُرْنَا صَدِيقَنَا فِي الْمُسْتَشْفَى.", "We visited our friend in the hospital.", "زُرْنَا"),
                 ex("أَحْضَرْنَا لَهُ زُهُورًا وَهَدِيَّة.", "We brought him flowers and a gift.", "أَحْضَرْنَا"),
                 ex("سَأَزُورُهُ غَدًا مَرَّة أُخْرَى.", "I will visit him again tomorrow.", "سَأَزُورُهُ"),
             ]),
    ],
    exercises=[
        M("What does سَلَامَتُكَ say to a sick person?", "get well", ["welcome", "goodbye", "congratulations"], "A short wish for health."),
        M("What does شَافَاكَ اللَّه mean?", "may God heal you", ["may God forgive you", "may God guide us", "God is great"], "شِفَاء = healing."),
        M("What does الشِّفَاء الْعَاجِل mean?", "a quick recovery", ["a long illness", "a new doctor", "a small gift"], "عَاجِل = quick."),
        M("What does زُرْنَا صَدِيقَنَا mean?", "we visited our friend", ["we called our friend", "our friend visited us", "we helped our friend"], "زَارَ = to visit."),
        M("What are زُهُور?", "flowers", ["gifts", "tablets", "rooms"], "A plural."),
        M("What does سَأَزُورُهُ غَدًا mean?", "I will visit him tomorrow", ["I visited him yesterday", "he will visit me", "I visit him daily"], "سَـ = future."),
        F("___ يَا صَدِيقِي!", "سَلَامَتُكَ", ["سَلَامَتُكِ", "شَفَاءَتُكَ"], "Said to a man.", tr="Get well, my friend!"),
        F("أَتَمَنَّى لَكَ ___ الْعَاجِل.", "الشِّفَاء", ["الْمَوْعِد", "الْحُمَّى"], "Recovery.", tr="I wish you a quick recovery."),
        F("___ صَدِيقَنَا فِي الْمُسْتَشْفَى.", "زُرْنَا", ["زَارَ", "زُرْتُ"], "“We”.", tr="We visited our friend in the hospital.", lemma="زور:past:nahnu"),
        F("أَحْضَرْنَا لَهُ ___ وَهَدِيَّة.", "زُهُورًا", ["دَوَاءً", "مَرِيضًا"], "Flowers.", tr="We brought him flowers and a gift."),
    ],
    verify=vv("زور", "past", ana="زُرْتُ", nahnu="زُرْنَا") + vv("حضر#4", "past", nahnu="أَحْضَرْنَا"),
)

# ---------------------------------------------------------------------------- 451
L451 = lesson(
    "A surprise party",
    "أَدْعُوكَ إِلَى حَفْلَة · لَا تَقُلْ لِأَحَد · عِيد مِيلَاد سَعِيد",
    requires=["دعوة", "حفلة", "مفاجأة", "عيد", "ميلاد", "هدية", "حضر", "مبروك"],
    cards=[
        card("Inviting friends",
             "An invitation is دَعْوَة and to invite is دَعَا, with إِلَى for the event: أَدْعُوكَ إِلَى حَفْلَة. A surprise is مُفَاجَأَة. A birthday is عِيد مِيلَاد, and the greeting is عِيد مِيلَاد سَعِيد. "
             "To keep it secret: لَا تَقُلْ لِأَحَد, “don't tell anyone” (hollow verb: لَا تَقُلْ). To say you will attend: سَأَحْضُر. Congratulations is مَبْرُوك. The messages are invented.",
             tables=[table(["English", "Arabic"],
                           [["invitation", "دَعْوَة"], ["party", "حَفْلَة"], ["surprise", "مُفَاجَأَة"], ["birthday", "عِيد مِيلَاد"], ["happy birthday", "عِيد مِيلَاد سَعِيد"], ["congratulations", "مَبْرُوك"], ["don't tell anyone", "لَا تَقُلْ لِأَحَد"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أَدْعُوكَ إِلَى حَفْلَة مُفَاجَأَة.", "I invite you to a surprise party.", "أَدْعُوكَ"),
                 ex("سَتَكُون الْحَفْلَة يَوْمَ الْجُمُعَة مَسَاءً.", "The party will be on Friday evening.", "سَتَكُون"),
                 ex("لَا تَقُلْ لِأَحَد، فَهِيَ مُفَاجَأَة.", "Don't tell anyone, it's a surprise.", "لَا تَقُلْ"),
                 ex("سَأَحْضُر وَسَأُحْضِر هَدِيَّة.", "I will come and I will bring a gift.", "سَأَحْضُر"),
                 ex("عِيد مِيلَاد سَعِيد يَا أُخْتِي!", "Happy birthday, sister!", "عِيد مِيلَاد سَعِيد"),
                 ex("مَبْرُوك! كَمْ عُمْرُكِ الْآن؟", "Congratulations! How old are you now?", "مَبْرُوك"),
             ]),
    ],
    exercises=[
        M("What does أَدْعُوكَ إِلَى حَفْلَة mean?", "I invite you to a party", ["I thank you for the party", "I saw you at the party", "I miss the party"], "دَعَا إِلَى = to invite to."),
        M("What is مُفَاجَأَة?", "a surprise", ["a gift", "a secret", "a guest"], "A surprise party is حَفْلَة مُفَاجَأَة."),
        M("What does لَا تَقُلْ لِأَحَد mean?", "don't tell anyone", ["tell everyone", "I told someone", "he didn't say"], "لَا + jussive of قَالَ."),
        M("What does سَأَحْضُر mean?", "I will attend", ["I attended", "he attends", "attend!"], "سَـ = future."),
        M("What is the birthday greeting?", "عِيد مِيلَاد سَعِيد", ["سَلَامَتُكَ", "شَافَاكَ اللَّه", "مَعَ السَّلَامَة"], "عِيد مِيلَاد = birthday."),
        M("When do you say مَبْرُوك?", "to congratulate", ["to apologise", "to say goodbye", "to ask the way"], "A congratulation."),
        F("أَدْعُوكَ ___ حَفْلَة مُفَاجَأَة.", "إِلَى", ["مِنْ", "عَنْ"], "Invite to.", tr="I invite you to a surprise party."),
        F("لَا ___ لِأَحَد، فَهِيَ مُفَاجَأَة.", "تَقُلْ", ["تَقُولُ", "قُلْتَ"], "A negative command.", tr="Don't tell anyone, it's a surprise."),
        F("___ أَحْضُر وَسَأُحْضِر هَدِيَّة.", "سَ", ["لَنْ", "لَمْ"], "Future.", tr="I will come and I will bring a gift."),
        F("___ مِيلَاد سَعِيد يَا أُخْتِي!", "عِيد", ["حَفْلَة", "دَعْوَة"], "Happy birthday.", tr="Happy birthday, sister!"),
    ],
    verify=vv("قول", "neg", anta="لَا تَقُلْ") + vv("حضر", "pres", ana="أَحْضُر") + vv("حضر#4", "pres", ana="أُحْضِر"),
)

# ---------------------------------------------------------------------------- 452
L452 = lesson(
    "Politely saying no",
    "شُكْرًا عَلَى الدَّعْوَة · لَكِنْ لَا أَسْتَطِيع · أَنَا آسِف",
    requires=["شكر", "دعوة", "آسف", "مشغول", "مسافر", "لكن"],
    cards=[
        card("A reason and a feeling",
             "A polite refusal has three parts. First, thanks: شُكْرًا عَلَى الدَّعْوَة. Then regret: أَنَا آسِف, “I am sorry”. Then the reason, joined with لِأَنَّ, “because”, or وَلِذَلِكَ, “and therefore”. "
             "You can add a wish: أَتَمَنَّى لَكُمْ وَقْتًا جَمِيلًا, “I wish you a lovely time”. For “I can't”, use لَا أَسْتَطِيع, followed by the noun الْحُضُور, “attending”, or أَنْ + subjunctive. The messages are invented.",
             tables=[table(["English", "Arabic"],
                           [["thank you for the invitation", "شُكْرًا عَلَى الدَّعْوَة"], ["I am sorry", "أَنَا آسِف"], ["I can't attend", "لَا أَسْتَطِيع الْحُضُور"], ["because I am busy", "لِأَنَّنِي مَشْغُول"], ["therefore", "وَلِذَلِكَ"], ["a lovely time", "وَقْتًا جَمِيلًا"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("شُكْرًا عَلَى الدَّعْوَة.", "Thank you for the invitation.", "شُكْرًا"),
                 ex("أَنَا آسِف، لَا أَسْتَطِيع الْحُضُور.", "I am sorry, I can't attend.", "لَا أَسْتَطِيع الْحُضُور"),
                 ex("لِأَنَّنِي مُسَافِر غَدًا.", "Because I am travelling tomorrow.", "لِأَنَّنِي"),
                 ex("أَنَا مَشْغُول، وَلِذَلِكَ لَنْ أَحْضُرَ.", "I am busy, therefore I will not come.", "وَلِذَلِكَ"),
                 ex("أَتَمَنَّى لَكُمْ وَقْتًا جَمِيلًا.", "I wish you a lovely time.", "وَقْتًا جَمِيلًا"),
                 ex("سَأَزُورُكُمْ فِي الْأُسْبُوع الْقَادِم.", "I will visit you next week.", "سَأَزُورُكُمْ"),
             ]),
    ],
    exercises=[
        M("What does شُكْرًا عَلَى الدَّعْوَة mean?", "thank you for the invitation", ["I accept the invitation", "sorry for the delay", "welcome to the party"], "عَلَى = for (thanks)."),
        M("What does لَا أَسْتَطِيع الْحُضُور mean?", "I can't attend", ["I can attend", "I did not attend", "he can't attend"], "اِسْتَطَاعَ = to be able."),
        M("What does لِأَنَّنِي مُسَافِر mean?", "because I am travelling", ["although I travelled", "if I travel", "when I return"], "لِأَنَّ = because."),
        M("What does وَلِذَلِكَ mean?", "and therefore", ["and before", "and also", "but"], "A result connector."),
        M("Which part gives the reason?", "لِأَنَّنِي مَشْغُول", ["شُكْرًا", "أَنَا آسِف", "مَعَ السَّلَامَة"], "لِأَنَّ introduces a reason."),
        M("What does أَتَمَنَّى لَكُمْ وَقْتًا جَمِيلًا mean?", "I wish you a lovely time", ["I thank you for the time", "I have no time", "I will come in time"], "تَمَنَّى = to wish."),
        F("___ عَلَى الدَّعْوَة.", "شُكْرًا", ["مَبْرُوك", "آسِف"], "Thanks.", tr="Thank you for the invitation."),
        F("أَنَا آسِف، لَا ___ الْحُضُور.", "أَسْتَطِيع", ["أَسْتَطِيعُون", "اِسْتَطَعْتُ"], "“I can't”.", tr="I am sorry, I can't attend."),
        F("___ مُسَافِر غَدًا.", "لِأَنَّنِي", ["لَكِنَّ", "ثُمَّ"], "Because I.", tr="Because I am travelling tomorrow."),
        F("أَنَا مَشْغُول، ___ لَنْ أَحْضُرَ.", "وَلِذَلِكَ", ["لِأَنَّ", "أَوْ"], "Therefore.", tr="I am busy, therefore I will not come."),
    ],
    verify=vv("حضر", "sub", ana="أَحْضُرَ") + vv("زور", "fut", ana="سَأَزُورُ"),
)

# ---------------------------------------------------------------------------- 453
L453 = lesson(
    "Remembering the journey",
    "أَوَّلًا · ثُمَّ · بَعْدَ ذَلِكَ · تَذَكَّرْتُ · رَجَعْنَا",
    requires=["رحلة", "ذكرى", "سافر", "وصل", "تعلم", "رجع", "جميل", "أول", "ثم", "بعد"],
    cards=[
        card("Telling a story in order",
             "To tell a trip in order, link past verbs with أَوَّلًا, “first”, ثُمَّ, “then”, بَعْدَ ذَلِكَ, “after that”, and وَأَخِيرًا, “and finally”. The verbs are past: سَافَرْنَا, وَصَلْنَا, تَعَلَّمْنَا, رَجَعْنَا. "
             "To say what you remember: تَذَكَّرْتُ, “I remembered”, or ذِكْرَى جَمِيلَة, “a lovely memory”. Superlatives use أَجْمَل, “the most beautiful”, in an idāfa: أَجْمَل ذِكْرَى, “the loveliest memory”. The story is invented.",
             tables=[table(["English", "Arabic"],
                           [["first", "أَوَّلًا"], ["then", "ثُمَّ"], ["after that", "بَعْدَ ذَلِكَ"], ["finally", "وَأَخِيرًا"], ["we travelled", "سَافَرْنَا"], ["we arrived", "وَصَلْنَا"], ["we learned", "تَعَلَّمْنَا"], ["we returned", "رَجَعْنَا"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("أَوَّلًا سَافَرْنَا إِلَى مَدِينَة جَمِيلَة.", "First we travelled to a lovely city.", "أَوَّلًا"),
                 ex("ثُمَّ وَصَلْنَا إِلَى الْفُنْدُق.", "Then we arrived at the hotel.", "ثُمَّ"),
                 ex("بَعْدَ ذَلِكَ تَعَلَّمْنَا كَلِمَات جَدِيدَة.", "After that we learned new words.", "بَعْدَ ذَلِكَ"),
                 ex("وَأَخِيرًا رَجَعْنَا إِلَى بُيُوتِنَا.", "And finally we returned to our homes.", "وَأَخِيرًا"),
                 ex("تَذَكَّرْتُ أَصْدِقَائِي هُنَاك.", "I remembered my friends there.", "تَذَكَّرْتُ"),
                 ex("كَانَتْ أَجْمَل ذِكْرَى فِي حَيَاتِي.", "It was the loveliest memory of my life.", "أَجْمَل ذِكْرَى"),
             ]),
    ],
    exercises=[
        M("What does أَوَّلًا mean?", "first", ["finally", "then", "never"], "The start of the sequence."),
        M("What does بَعْدَ ذَلِكَ mean?", "after that", ["before that", "like that", "except that"], "بَعْدَ = after."),
        M("What does وَأَخِيرًا mean?", "and finally", ["and first", "and then", "and always"], "أَخِير = last."),
        M("What does تَعَلَّمْنَا كَلِمَات جَدِيدَة mean?", "we learned new words", ["we wrote new words", "we forgot the words", "we taught the words"], "تَعَلَّمَ = to learn."),
        M("What does أَجْمَل ذِكْرَى mean?", "the loveliest memory", ["a sad memory", "a long memory", "no memory"], "أَجْمَل + noun = the most beautiful."),
        M("What does تَذَكَّرْتُ mean?", "I remembered", ["I forgot", "I travelled", "I wrote"], "ذِكْرَى = memory."),
        F("___ سَافَرْنَا إِلَى مَدِينَة جَمِيلَة.", "أَوَّلًا", ["أَخِيرًا", "مَبْرُوك"], "The first step.", tr="First we travelled to a lovely city."),
        F("ثُمَّ ___ إِلَى الْفُنْدُق.", "وَصَلْنَا", ["وَصَلْتُ", "وَصَلُوا"], "“We”.", tr="Then we arrived at the hotel.", lemma="وصل:past:nahnu"),
        F("بَعْدَ ذَلِكَ ___ كَلِمَات جَدِيدَة.", "تَعَلَّمْنَا", ["تَعَلَّمُوا", "يَتَعَلَّم"], "“We learned”.", tr="After that we learned new words.", lemma="علم#5:past:nahnu"),
        F("وَأَخِيرًا ___ إِلَى بُيُوتِنَا.", "رَجَعْنَا", ["رَجَعْتُ", "رَجَعَتْ"], "“We returned”.", tr="And finally we returned to our homes.", lemma="رجع:past:nahnu"),
        F("كَانَتْ ___ ذِكْرَى فِي حَيَاتِي.", "أَجْمَل", ["جَمِيل", "جَمِيلَة"], "Superlative.", tr="It was the loveliest memory of my life."),
    ],
    verify=vv("سفر#3", "past", nahnu="سَافَرْنَا") + vv("وصل", "past", nahnu="وَصَلْنَا") + vv("علم#5", "past", nahnu="تَعَلَّمْنَا") + vv("رجع", "past", nahnu="رَجَعْنَا") + vv("ذكر#5", "past", ana="تَذَكَّرْتُ"),
)

# ---------------------------------------------------------------------------- 454
L454 = lesson(
    "Course review: the verb, the negatives, the sentence",
    "ماضٍ · مُضَارِع · أَمْر · لَمْ · لَنْ · لَا · لَيْسَ",
    requires=["سافر", "كتب", "ذهب", "تعلم", "نوم", "شرب", "عمل", "رجع"],
    cards=[
        card("What you can now do",
             "You now have the main tools of Modern Standard Arabic. Past: كَتَبْتُ, “I wrote”. Present: أَكْتُب, “I write”. Future: سَأَكْتُب, “I will write”. Command: اُكْتُبْ, “write!”. "
             "Four negatives: لَا + present (لَا أَكْتُب), لَمْ + jussive (لَمْ أَكْتُبْ, “I did not write”), لَنْ + subjunctive (لَنْ أَكْتُبَ, “I will not write”), لَيْسَ + noun or adjective (لَيْسَ كَبِيرًا). "
             "Add feelings, health, directions, travel and the news, and you can tell your own story. These last exercises mix all of it.",
             tables=[table(["English", "Arabic"],
                           [["I wrote", "كَتَبْتُ"], ["I write", "أَكْتُب"], ["I will write", "سَأَكْتُب"], ["write!", "اُكْتُبْ"], ["I did not write", "لَمْ أَكْتُبْ"], ["I will not write", "لَنْ أَكْتُبَ"], ["I do not write", "لَا أَكْتُب"]],
                           say=[1], tlit=[1], gloss=False)],
             examples=[
                 ex("كَتَبْتُ رِسَالَة إِلَى صَدِيقِي.", "I wrote a letter to my friend.", "كَتَبْتُ"),
                 ex("لَمْ أَكْتُبْ لَهُ أَمْسِ.", "I did not write to him yesterday.", "لَمْ أَكْتُبْ"),
                 ex("لَنْ أَنْسَى هَذِهِ الرِّحْلَة.", "I will not forget this trip.", "لَنْ أَنْسَى"),
                 ex("لَيْسَ الطَّرِيق طَوِيلًا.", "The road is not long.", "لَيْسَ"),
                 ex("اِشْرَبْ مَاءً وَنَمْ مُبَكِّرًا.", "Drink water and sleep early.", "نَمْ"),
                 ex("إِذَا تَعِبْتَ فَنَمْ قَلِيلًا.", "If you get tired, sleep a little.", "إِذَا تَعِبْتَ"),
             ]),
    ],
    exercises=[
        M("Which means “I did not write”?", "لَمْ أَكْتُبْ", ["لَنْ أَكْتُبَ", "لَا أَكْتُب", "كَتَبْتُ"], "لَمْ + jussive."),
        M("Which means “I will not write”?", "لَنْ أَكْتُبَ", ["لَمْ أَكْتُبْ", "لَا أَكْتُب", "سَأَكْتُب"], "لَنْ + subjunctive."),
        M("Which negative goes with a noun or adjective predicate?", "لَيْسَ", ["لَمْ", "لَنْ", "لَا"], "لَيْسَ الطَّرِيق طَوِيلًا."),
        M("What does إِذَا تَعِبْتَ فَنَمْ قَلِيلًا mean?", "if you get tired, sleep a little", ["when I sleep, I get tired", "you slept, so you got tired", "do not sleep"], "إِذَا + past = if; فَـ before the command."),
        M("What does سَأَكْتُب mean?", "I will write", ["I wrote", "I write", "write!"], "سَـ = future."),
        M("Which is the command “drink”?", "اِشْرَبْ", ["شَرِبْتَ", "تَشْرَب", "لَا تَشْرَبْ"], "The imperative."),
        F("___ أَكْتُبْ لَهُ أَمْسِ.", "لَمْ", ["لَنْ", "لَيْسَ"], "A past meaning.", tr="I did not write to him yesterday."),
        F("___ أَنْسَى هَذِهِ الرِّحْلَة.", "لَنْ", ["لَمْ", "لَيْسَ"], "A future meaning.", tr="I will not forget this trip."),
        F("___ الطَّرِيق طَوِيلًا.", "لَيْسَ", ["لَمْ", "لَنْ"], "A noun sentence.", tr="The road is not long."),
        F("اِشْرَبْ مَاءً ___ مُبَكِّرًا.", "وَنَمْ", ["وَنَامَ", "وَتَنَامُ"], "A second command.", tr="Drink water and sleep early."),
    ],
    verify=vv("كتب", "past", ana="كَتَبْتُ") + vv("كتب", "pres", ana="أَكْتُب") + vv("كتب", "fut", ana="سَأَكْتُب") + vv("كتب", "imp", anta="اُكْتُبْ") + vv("كتب", "jus", ana="أَكْتُبْ") + vv("كتب", "sub", ana="أَكْتُبَ") + vv("نوم", "imp", anta="نَمْ"),
)


UNIT = unit("الْعَوْدَة إِلَى الْكُوَيْت: accidents, health, feelings and review", [L435, L436, L437, L438, L439, L440, L441, L442, L443, L444, L445, L446, L447, L448, L449, L450, L451, L452, L453, L454])
