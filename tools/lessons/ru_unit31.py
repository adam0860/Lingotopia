"""Unit 31: the many jobs of -ся; the pronoun себя; word-building; employment vocabulary
(textbook module 7, lessons 39-40)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 311
L311 = lesson(
    "What -ся does: умыва'ться, встреча'ться, боя'ться",
    "Мы ча'сто встреча'емся, и она' всегда' улыба'ется.",
    requires=["готовиться", "встречаться", "познакомиться", "бояться", "улыбаться", "надеяться", "нравиться", "находиться"],
    cards=[
        card("Reflexive: the action returns to the subject",
             "The ending -ся is a short form of себя'. In reflexive verbs the doer and the receiver are the same person.",
             tables=[table(
                 ["Without -ся", "With -ся"],
                 [["Ма'ма умыва'ет Са'шу.", "Са'ша умыва'ется сам."],
                  ["Ма'ма одева'ет дочь.", "Дочь одева'ется сама'."],
                  ["Тре'нер гото'вит кома'нду.", "Кома'нда гото'вится к ма'тчу."]])],
             examples=[
                 ex("Малы'ш уже' умыва'ется сам.", "The little boy already washes up by himself.", "умыва'ется"),
                 ex("Она' гото'вится к экза'мену.", "She is preparing for the exam.", "гото'вится"),
             ]),
        card("Reciprocal: each other",
             "In reciprocal verbs the people act on each other. The -ся here could be replaced by друг дру'га.",
             tables=[table(
                 ["Verb", "English"],
                 [["встреча'ться", "to meet (each other); to date"],
                  ["знако'миться / познако'миться", "to get to know each other"],
                  ["перепи'сываться", "to write to each other"],
                  ["ссо'риться", "to quarrel"]])],
             examples=[
                 ex("Мы ча'сто встреча'емся в кафе'.", "We often meet at a café.", "встреча'емся"),
                 ex("Они' познако'мились в университе'те.", "They met at university.", "познако'мились"),
             ]),
        card("Verbs that exist only with -ся",
             "Many common verbs have no form without -ся. You simply learn them as they are.",
             tables=[table(
                 ["Verb", "English"],
                 [["боя'ться", "to be afraid"],
                  ["улыба'ться", "to smile"],
                  ["наде'яться", "to hope"],
                  ["находи'ться", "to be located"],
                  ["нра'виться", "to be liked"],
                  ["смея'ться", "to laugh"],
                  ["стара'ться", "to try hard"]])],
             examples=[
                 ex("Магази'н нахо'дится в це'нтре.", "The shop is located in the center.", "нахо'дится"),
                 ex("Я бою'сь соба'к.", "I am afraid of dogs.", "бою'сь"),
             ]),
    ],
    verify=(vf("умываться", "умывается") + vf("одеваться", "одевается") + vf("готовиться", "готовится") + vf("встречаться", "встречаемся")
            + vf("познакомиться", "познакомились") + vf("переписываться", "переписываться") + vf("ссориться", "ссориться")
            + vf("бояться", "бояться", "боюсь") + vf("улыбаться", "улыбается") + vf("надеяться", "надеяться")
            + vf("находиться", "находится") + vf("нравиться", "нравится") + vf("смеяться", "смеяться") + vf("стараться", "стараться")),
    exercises=[
        F("Малы'ш уже' ___ сам. (washes up)", "умыва'ется", ["умыва'ет", "умыва'ют", "умыва'ться"], "Reflexive: the child washes himself.", "The little boy already washes up by himself.", lemma="умываться"),
        F("Мы ча'сто ___ в кафе'. (meet)", "встреча'емся", ["встреча'ем", "встреча'ете", "встреча'ются"], "Reciprocal: мы … друг дру'га.", "We often meet at a café.", lemma="встречаться"),
        F("Она' ___ к экза'мену. (is preparing)", "гото'вится", ["гото'вит", "гото'вятся", "гото'виться"], "Reflexive: she prepares herself.", "She is preparing for the exam.", lemma="готовиться"),
        F("Я ___ соба'к. (am afraid of)", "бою'сь", ["бои'шься", "бои'тся", "боя'ться"], "Present, first person of боя'ться.", "I am afraid of dogs.", lemma="бояться"),
        F("Она' всегда' ___, когда' ви'дит нас. (smiles)", "улыба'ется", ["улыба'ет", "улыба'ются", "улыба'ться"], "Улыба'ться only exists with -ся.", "She always smiles when she sees us.", lemma="улыбаться"),
        F("Магази'н ___ в це'нтре. (is located)", "нахо'дится", ["нахо'дит", "нахо'дятся", "находи'ть"], "Singular subject.", "The shop is located in the center.", lemma="находиться"),
        F("Они' ___ в университе'те. (got to know each other)", "познако'мились", ["познако'мили", "познако'мился", "познако'мить"], "Plural past, reciprocal.", "They met at university.", lemma="познакомиться"),
        mc("Which verb is reciprocal?", ["встреча'ться", "умыва'ться", "боя'ться", "нра'виться"], "встреча'ться", "Two people meet each other.", order=True),
        mc("The ending -ся originally comes from:", ["себя'", "сам", "со", "сей"], "себя'", "Себя' is the full reflexive pronoun.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 312
L312 = lesson(
    "Things get done: Рейс отменя'ется, це'ны поднима'ются",
    "Авиакомпа'ния отменя'ет рейс. — Рейс отменя'ется.",
    requires=["отменить", "поднимать", "подниматься", "рейс", "цена", "строить", "строиться", "предложение"],
    cards=[
        card("The object becomes the subject",
             "To describe an action without saying who does it, take a transitive verb, make its object the subject, and add -ся. The verb agrees with the new subject.",
             tables=[table(
                 ["Active (doer named)", "-ся (doer not important)"],
                 [["Авиакомпа'ния отменя'ет рейс.", "Рейс отменя'ется."],
                  ["Вла'сти поднима'ют це'ны.", "Це'ны поднима'ются."],
                  ["Компа'ния предлага'ет услу'ги.", "Услу'ги предлага'ются."],
                  ["Рабо'чие стро'ят дом.", "Дом стро'ится."]])],
             examples=[
                 ex("Рейс отменя'ется из-за пого'ды.", "The flight is being cancelled because of the weather.", "отменя'ется"),
                 ex("Це'ны на бензи'н поднима'ются.", "Gas prices are rising.", "поднима'ются"),
             ]),
        card("Naming the doer",
             "If you still want to mention who does it, put the doer in the instrumental case.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Дом стро'ится рабо'чими.", "The house is being built by workers."],
                  ["Рейс отменя'ется авиакомпа'нией.", "The flight is cancelled by the airline."]])],
             examples=[
                 ex("Дом стро'ится рабо'чими.", "The house is being built by workers.", "рабо'чими"),
             ]),
        card("Only imperfective, only with objects",
             "This construction is normally imperfective: it describes a process or a general rule. Verbs that cannot take an object do not add -ся: рейс прилета'ет, пла'мя бушу'ет.",
             tables=[table(
                 ["Verb", "Why no -ся"],
                 [["прилета'ть", "no direct object"],
                  ["бушева'ть", "no direct object"],
                  ["отменя'ть → отменя'ться", "has a direct object, so -ся is possible"]])],
             examples=[
                 ex("Рейс прилета'ет во'время.", "The flight arrives on time.", "прилета'ет"),
             ]),
    ],
    verify=(vf("отменять", "отменяет") + vf("поднимать", "поднимают") + vf("подниматься", "поднимаются") + vf("предлагать", "предлагает")
            + vf("строить", "строят") + vf("строиться", "строится") + vf("прилетать", "прилетает") + vf("бушевать", "бушует")
            + vf("рабочий", "рабочими") + vf("цена", "цены") + vf("рейс", "рейс")),
    exercises=[
        F("Авиакомпа'ния ___ рейс. (cancels)", "отменя'ет", ["отменя'ется", "отменя'ют", "отменя'ть"], "Has a direct object (рейс): no -ся.", "The airline cancels the flight.", lemma="отменять"),
        F("Рейс ___ из-за пого'ды. (is being cancelled)", "отменя'ется", ["отменя'ет", "отменя'ют", "отменя'ть"], "Рейс is the subject: -ся.", "The flight is being cancelled because of the weather."),
        F("Вла'сти ___ це'ны на бензи'н. (are raising)", "поднима'ют", ["поднима'ются", "поднима'ет", "поднима'ться"], "Plural subject, object це'ны.", "The authorities are raising gas prices.", lemma="поднимать"),
        F("Це'ны на бензи'н ___. (are rising)", "поднима'ются", ["поднима'ют", "поднима'ет", "поднима'ться"], "Plural subject, no object: -ся.", "Gas prices are rising.", lemma="подниматься"),
        F("Рабо'чие ___ но'вый дом. (are building)", "стро'ят", ["стро'ится", "стро'ятся", "стро'ить"], "Object: но'вый дом.", "The workers are building a new house.", lemma="строить"),
        F("Но'вый дом ___ рабо'чими. (is being built)", "стро'ится", ["стро'ят", "стро'ятся", "стро'ить"], "Singular subject дом: -ся.", "The new house is being built by workers.", lemma="строиться"),
        F("Э'ти услу'ги ___ по ни'зким це'нам. (are offered)", "предлага'ются", ["предлага'ют", "предлага'ет", "предлага'ть"], "Plural услу'ги is the subject.", "These services are offered at low prices."),
        mc("Which sentence has the doer in the instrumental?", ["Дом стро'ится рабо'чими.", "Рабо'чие стро'ят дом.", "Дом стро'ят.", "Дом был постро'ен."], "Дом стро'ится рабо'чими.", "Doer in the instrumental case.", order=True),
        mc("Which verb does NOT add -ся?", ["прилета'ть", "отменя'ть", "поднима'ть", "стро'ить"], "прилета'ть", "No direct object.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 313
L313 = lesson(
    "With or without -ся: меня'ть / меня'ться, продолжа'ть / продолжа'ться",
    "Компа'ния меня'ет це'ны, и це'ны меня'ются.",
    requires=["менять", "меняться", "продолжать", "продолжаться", "изменить", "измениться", "закончить", "закончиться", "открыть", "открыться"],
    cards=[
        card("A simple test",
             "If there is a direct object in the accusative, use the verb without -ся. If the subject is itself what changes, starts or ends, use -ся.",
             tables=[table(
                 ["With an object", "Without an object"],
                 [["меня'ть", "меня'ться"],
                  ["измени'ть", "измени'ться"],
                  ["продолжа'ть", "продолжа'ться"],
                  ["зако'нчить", "зако'нчиться"],
                  ["откры'ть", "откры'ться"],
                  ["останови'ть", "останови'ться"]])],
             examples=[
                 ex("Компа'ния меня'ет це'ны.", "The company is changing its prices.", "меня'ет"),
                 ex("Це'ны меня'ются.", "Prices are changing.", "меня'ются"),
             ]),
        card("More pairs",
             "These pairs often appear in news and reports.",
             tables=[table(
                 ["Verb + object", "Verb with -ся"],
                 [["повыша'ть / повы'сить", "повыша'ться / повы'ситься"],
                  ["снижа'ть / сни'зить", "снижа'ться / сни'зиться"],
                  ["увели'чивать / увели'чить", "увели'чиваться / увели'читься"],
                  ["сокраща'ть / сократи'ть", "сокраща'ться / сократи'ться"],
                  ["обновля'ть", "обновля'ться"]])],
             examples=[
                 ex("Прави'тельство сни'зило нало'г.", "The government lowered the tax.", "сни'зило"),
                 ex("Нало'г сни'зился.", "The tax went down.", "сни'зился"),
             ]),
        card("People vs. things",
             "-Ся also appears when a person does something to themselves: остановиться (stop), измениться (change). The test is still the same: no direct object.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Води'тель останови'л маши'ну.", "The driver stopped the car."],
                  ["Маши'на останови'лась.", "The car stopped."],
                  ["Он останови'лся у до'ма.", "He stopped by the house."]])],
             examples=[
                 ex("Уро'к зако'нчился в три часа'.", "The lesson ended at three o'clock.", "зако'нчился"),
             ]),
    ],
    verify=(vf("менять", "меняет") + vf("меняться", "меняются") + vf("изменить", "изменил") + vf("измениться", "изменился")
            + vf("продолжать", "продолжать") + vf("продолжаться", "продолжается") + vf("закончить", "закончил") + vf("закончиться", "закончился")
            + vf("открыть", "открыл") + vf("открыться", "открылся") + vf("остановить", "остановил") + vf("остановиться", "остановился")
            + vf("снизить", "снизило") + vf("снизиться", "снизился") + vf("налог", "налог") + vf("правительство", "правительство")),
    exercises=[
        F("Компа'ния ___ це'ны. (changes)", "меня'ет", ["меня'ется", "меня'ются", "меня'ть"], "Object це'ны: no -ся.", "The company changes its prices.", lemma="менять"),
        F("Це'ны ___. (are changing)", "меня'ются", ["меня'ют", "меня'ет", "меня'ть"], "No object: -ся.", "Prices are changing.", lemma="меняться"),
        F("Прави'тельство ___ нало'г. (lowered)", "сни'зило", ["сни'зилось", "сни'зился", "сни'зить"], "Object нало'г; neuter subject.", "The government lowered the tax.", lemma="снизить"),
        F("Нало'г ___. (went down)", "сни'зился", ["сни'зил", "сни'зило", "сни'зить"], "Masculine subject, no object.", "The tax went down.", lemma="снизиться"),
        F("Води'тель ___ маши'ну. (stopped)", "останови'л", ["останови'лся", "останови'лась", "останови'ть"], "Object маши'ну.", "The driver stopped the car.", lemma="остановить"),
        F("Маши'на ___. (stopped)", "останови'лась", ["останови'ла", "останови'лся", "останови'ть"], "Feminine, no object.", "The car stopped.", lemma="остановиться"),
        F("Уро'к ___ в три часа'. (ended)", "зако'нчился", ["зако'нчил", "зако'нчила", "зако'нчить"], "Masculine subject, no object.", "The lesson ended at three o'clock.", lemma="закончиться"),
        F("Учи'тель ___ уро'к в три часа'. (ended)", "зако'нчил", ["зако'нчился", "зако'нчилась", "зако'нчить"], "Object уро'к.", "The teacher finished the lesson at three o'clock.", lemma="закончить"),
        mc("Choose the correct sentence.", ["Бизнес бы'стро развива'ется.", "Бизнес бы'стро развива'ет.", "Бизнес бы'стро развива'ются.", "Бизнес бы'стро развива'ть."], "Бизнес бы'стро развива'ется.", "No object: -ся.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 314
L314 = lesson(
    "Three ways to say it: отменя'ется, отменя'ют, отменён",
    "Рейс отменя'ется. Рейс отменя'ют. Рейс отменён.",
    requires=["отменить", "решить", "решаться", "организовать", "рейс", "проблема"],
    cards=[
        card("Same idea, three tools",
             "When the doer is unknown or unimportant, Russian offers three constructions.",
             tables=[table(
                 ["Construction", "Example", "Feeling"],
                 [["verb + -ся", "Рейс отменя'ется.", "a process, neutral"],
                  ["they-form without они'", "Рейс отменя'ют.", "someone does it, we don't know who"],
                  ["был / бу'дет + short participle", "Рейс был отменён.", "a completed result"]])],
             examples=[
                 ex("Це'ны поднима'ются. — Це'ны поднима'ют.", "Prices are rising. — They are raising the prices.", "поднима'ются"),
             ]),
        card("Past and future",
             "In the past and the future, the third option adds a form of быть.",
             tables=[table(
                 ["Time", "-ся", "Participle"],
                 [["past", "Конце'рт отмени'лся.", "Конце'рт был отменён."],
                  ["future", "Пробле'ма не реши'тся.", "Пробле'ма не бу'дет решена'."]])],
             examples=[
                 ex("Пробле'ма не бу'дет решена'.", "The problem will not be resolved.", "бу'дет решена'"),
                 ex("Конце'рт был отменён.", "The concert was cancelled.", "был отменён"),
             ]),
        card("Choosing",
             "The participle fits official reports and finished results. The they-form is natural in speech. The -ся form describes what is happening to the subject.",
             tables=[table(
                 ["Situation", "Best choice"],
                 [["announcement at the airport", "Рейс отменён."],
                  ["telling a friend", "Рейс отмени'ли."],
                  ["describing a trend", "Це'ны поднима'ются."]])],
             examples=[
                 ex("Рейс отменён.", "The flight is cancelled.", "отменён"),
             ]),
    ],
    verify=(vf("отменить", "отменили") + vf("решиться", "решится") + vf("поднимать", "поднимают") + vf("подниматься", "поднимаются")),
    exercises=[
        F("Рейс ___ из-за снегопа'да. (they-form: cancelled)", "отмени'ли", ["отменён", "отмени'лся", "отмени'ла"], "Plural verb, no они'.", "They cancelled the flight because of the snowfall.", lemma="отменить"),
        F("Рейс ___ из-за снегопа'да. (short participle)", "отменён", ["отмени'ли", "отмени'лся", "отменена'"], "Masculine: рейс.", "The flight has been cancelled because of the snowfall.", lemma=None),
        F("Конце'рт ___ из-за дождя'. (-ся, past)", "отмени'лся", ["отменён", "отмени'ли", "отмени'лась"], "Masculine subject.", "The concert was cancelled because of the rain."),
        F("Пробле'ма не бу'дет ___. (short participle, fem.)", "решена'", ["реши'тся", "реши'т", "решено'"], "Feminine: пробле'ма.", "The problem will not be resolved.", lemma=None),
        F("Пробле'ма не ___. (-ся, future)", "реши'тся", ["решена'", "реши'т", "реши'ла"], "Future of реши'ться.", "The problem will not be resolved."),
        mc("Which sentence has no stated doer and uses the они'-form?", ["Дом стро'ят.", "Дом стро'ится.", "Дом был постро'ен.", "Они' стро'ят дом."], "Дом стро'ят.", "Plural verb without они'.", order=True),
        mc("Which suits an official airport announcement?", ["Рейс отменён.", "Рейс отменя'ют.", "Они' отменя'ют рейс.", "Рейс отмени'лся ра'ньше."], "Рейс отменён.", "Short participle = result.", order=True),
        mc("Convert to the past with a participle: ‘Прое'кт не реши'тся’.", ["Прое'кт не был решён.", "Прое'кт не бу'дет решён.", "Прое'кт не реши'ли.", "Прое'кт не реши'лся."], "Прое'кт не был решён.", "Был + short participle.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 315
L315 = lesson(
    "The pronoun себя': себя', себе', собо'й, о себе'",
    "Он ду'мает то'лько о себе', а она' ре'дко покупа'ет себе' что'-то.",
    requires=["себя", "зеркало", "сам", "видеть", "подарок"],
    cards=[
        card("Forms of себя'",
             "Себя' reflects the subject back: ‘myself, himself, themselves’ and so on. Its forms are those of ты, with с instead of т.",
             tables=[table(
                 ["Case", "ты", "себя'"],
                 [["genitive", "тебя'", "себя'"],
                  ["dative", "тебе'", "себе'"],
                  ["accusative", "тебя'", "себя'"],
                  ["instrumental", "тобо'й", "собо'й"],
                  ["prepositional", "о тебе'", "о себе'"]])],
             examples=[
                 ex("Он ду'мает то'лько о себе'.", "He thinks only of himself.", "о себе'"),
             ]),
        card("No nominative",
             "Себя' always refers back to the subject of the sentence, so it has no nominative form and can never be a subject.",
             tables=[table(
                 ["Subject", "Meaning of себя'"],
                 [["я", "myself"],
                  ["ты", "yourself"],
                  ["он / она'", "himself / herself"],
                  ["мы", "ourselves"],
                  ["они'", "themselves"]])],
             examples=[
                 ex("Ма'ша ре'дко покупа'ет себе' что'-то.", "Masha rarely buys herself anything.", "себе'"),
                 ex("Они' ви'дят себя' в зе'ркале.", "They see themselves in the mirror.", "себя'"),
             ]),
        card("Ме'жду собо'й",
             "With plural subjects ме'жду собо'й means ‘among themselves’, ‘with each other’.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Они' говоря'т ме'жду собо'й по-неме'цки.", "They speak German to each other."],
                  ["Мы дово'льны собо'й.", "We are pleased with ourselves."]])],
             examples=[
                 ex("Они' говоря'т ме'жду собо'й по-неме'цки.", "They speak German to each other.", "ме'жду собо'й"),
             ]),
    ],
    verify=(vf("думать", "думает") + vf("покупать", "покупает") + vf("видеть", "видят") + vf("зеркало", "зеркале")
            + vf("говорить", "говорят") + vf("довольный", "довольны")),
    exercises=[
        F("Он ду'мает то'лько о ___. (himself)", "себе'", ["себя'", "собо'й", "тебе'"], "О + prepositional.", "He thinks only of himself."),
        F("Она' ви'дит ___ в зе'ркале. (herself)", "себя'", ["себе'", "собо'й", "тебя'"], "Accusative object.", "She sees herself in the mirror."),
        F("Он купи'л ___ но'вую маши'ну. (for himself)", "себе'", ["себя'", "собо'й", "тебе'"], "Dative: for whom?", "He bought himself a new car."),
        F("Мы дово'льны ___. (with ourselves)", "собо'й", ["себя'", "себе'", "мной"], "Дово'лен + instrumental.", "We are pleased with ourselves."),
        F("Они' говоря'т ме'жду ___ по-неме'цки. (themselves)", "собо'й", ["себя'", "себе'", "ними"], "Ме'жду + instrumental.", "They speak German to each other."),
        F("Она' не ве'рит в ___. (herself)", "себя'", ["себе'", "собо'й", "тебя'"], "В + accusative.", "She doesn't believe in herself."),
        mc("Себя' has no form in the:", ["nominative", "genitive", "dative", "instrumental"], "nominative", "It can never be a subject.", order=True),
        mc("Which pronoun matches Он ду'мает о ___?", ["себе'", "его'", "нём", "им"], "себе'", "The subject and the one thought about are the same person.", order=True),
        mc("Себя' has the same endings as:", ["ты", "он", "мы", "кто"], "ты", "тебя', тебе', тобо'й, о тебе'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 316
L316 = lesson(
    "To my place, with me, to myself: к себе', у себя', с собо'й, про себя'",
    "Приходи' ко мне — нет, к себе' я не приглашу'.",
    requires=["себя", "приглашать", "брать", "принести", "дверь", "кабинет"],
    cards=[
        card("Home and ownership",
             "Себя' with a preposition often points to ‘my own place’. The subject decides whose.",
             tables=[table(
                 ["Phrase", "English"],
                 [["к себе'", "to one's own place"],
                  ["у себя'", "at one's own place"],
                  ["Он у себя'?", "Is he in (his office)?"],
                  ["Я иду' к себе'.", "I'm going home / to my room."],
                  ["пригласи'ть к себе'", "to invite over"]])],
             examples=[
                 ex("Я приглашу' вас к себе' на вечери'нку.", "I'll invite you to my place for a party.", "к себе'"),
                 ex("Нача'льник у себя' в кабине'те?", "Is the manager in his office?", "у себя'"),
             ]),
        card("With me, to myself",
             "С собо'й is used for what a person takes or carries with them.",
             tables=[table(
                 ["Phrase", "English"],
                 [["брать с собо'й", "to take with you"],
                  ["принести' с собо'й", "to bring along"],
                  ["«Здесь и'ли с собо'й?»", "“For here or to go?”"],
                  ["говори'ть про себя'", "to say to oneself"],
                  ["ме'жду собо'й", "among themselves"]])],
             examples=[
                 ex("Он берёт дете'й с собо'й на рабо'ту.", "He takes his kids to work with him.", "с собо'й"),
                 ex("Цикло'н принесёт с собо'й дождь.", "The cyclone will bring rain with it.", "с собо'й"),
             ]),
        card("Doors: на себя' and от себя'",
             "On doors, на себя' means pull and от себя' means push. The direction is relative to the person acting.",
             tables=[table(
                 ["Sign", "English"],
                 [["на себя'", "pull"],
                  ["от себя'", "push"]])],
             examples=[
                 ex("На две'ри напи'сано: «на себя'».", "On the door it says ‘pull’.", "на себя'"),
             ]),
    ],
    verify=(vf("пригласить", "приглашу") + vf("брать", "берёт") + vf("принести", "принесёт")
            + vf("кабинет", "кабинете") + vf("дверь", "двери") + vf("вечеринка", "вечеринку")),
    exercises=[
        F("Я приглашу' вас ___ на вечери'нку. (to my place)", "к себе'", ["у себя'", "с собо'й", "от себя'"], "Куда'? к + dative.", "I'll invite you to my place for a party.", lemma=None),
        F("Нача'льник ___ в кабине'те? (in his office)", "у себя'", ["к себе'", "с собо'й", "на себя'"], "Где? у + genitive.", "Is the manager in his office?", lemma=None),
        F("Он берёт дете'й ___ на рабо'ту. (along)", "с собо'й", ["у себя'", "к себе'", "про себя'"], "Taking along: с собо'й.", "He takes his children along to work.", lemma=None),
        F("Кафе: «Здесь и'ли ___?» (to go)", "с собо'й", ["от себя'", "к себе'", "на себя'"], "Take away.", "“For here or to go?”", lemma=None),
        F("На две'ри напи'сано: «___». (push)", "от себя'", ["на себя'", "с собо'й", "про себя'"], "Away from yourself.", "The door says ‘push’.", lemma=None),
        F("На две'ри напи'сано: «___». (pull)", "на себя'", ["от себя'", "с собо'й", "у себя'"], "Toward yourself.", "The door says ‘pull’.", lemma=None),
        F("Он сказа'л э'то ___, что'бы никто' не слы'шал. (to himself)", "про себя'", ["к себе'", "у себя'", "с собо'й"], "Silently.", "He said it to himself so that nobody would hear.", lemma=None),
        mc("‘Я иду' к себе'’ means:", ["I'm going home / to my room.", "I'm going with myself.", "I'm going to him.", "I'm going away."], "I'm going home / to my room.", "К себе' = to one's own place.", order=True),
        mc("Which phrase means ‘among themselves’?", ["ме'жду собо'й", "про себя'", "к себе'", "у себя'"], "ме'жду собо'й", "Plural subjects.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 317
L317 = lesson(
    "Verb phrases with себя': чу'вствовать себя', вести' себя', позво'лить себе'",
    "Она' хорошо' себя' чу'вствует и взяла' на себя' отве'тственность.",
    requires=["чувствовать", "вести", "ответственность", "позволить", "представлять", "видеть", "цель", "считать"],
    cards=[
        card("Feeling and behaving",
             "Two phrases you already know take себя' in the accusative.",
             tables=[table(
                 ["Phrase", "English"],
                 [["чу'вствовать себя' хорошо' / пло'хо", "to feel well / badly"],
                  ["вести' себя' хорошо' / пло'хо", "to behave well / badly"],
                  ["Как ты себя' чу'вствуешь?", "How do you feel?"]])],
             examples=[
                 ex("Как ты себя' чу'вствуешь?", "How are you feeling?", "себя' чу'вствуешь"),
                 ex("Де'ти вели' себя' хорошо'.", "The children behaved well.", "вели' себя'"),
             ]),
        card("Taking, allowing, imagining",
             "Other fixed phrases use себя' or себе'.",
             tables=[table(
                 ["Phrase", "English"],
                 [["брать на себя' отве'тственность", "to take responsibility"],
                  ["позво'лить себе' + acc.", "to afford"],
                  ["представля'ть себе'", "to imagine"],
                  ["ста'вить пе'ред собо'й цель", "to set oneself a goal"],
                  ["счита'ть себя' + instr.", "to consider oneself"],
                  ["не похо'ж на себя'", "not look like oneself"]])],
             examples=[
                 ex("Она' взяла' на себя' отве'тственность.", "She took responsibility upon herself.", "на себя'"),
                 ex("Я не могу' позво'лить себе' тако'й тур.", "I can't afford such a tour.", "позво'лить себе'"),
             ]),
        card("Seeing and thinking of oneself",
             "Several verbs of perception and thought take себя' as an object.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Тре'нером я себя' не ви'жу.", "I don't see myself as a coach."],
                  ["Он счита'ет себя' специали'стом.", "He considers himself a specialist."],
                  ["Предста'вь себе' э'то!", "Imagine that!"]])],
             examples=[
                 ex("Он счита'ет себя' специали'стом.", "He considers himself a specialist.", "себя'"),
             ]),
    ],
    verify=(vf("чувствовать", "чувствуешь", "чувствует") + vf("вести", "вели") + vf("брать", "взяла") + vf("позволить", "позволить")
            + vf("представить", "представь") + vf("ставить", "ставить") + vf("считать", "считает") + vf("видеть", "вижу")
            + vf("ответственность", "ответственность") + vf("специалист", "специалистом")),
    exercises=[
        F("Как ты ___ чу'вствуешь? (yourself)", "себя'", ["себе'", "собо'й", "тебя'"], "Чу'вствовать себя'.", "How are you feeling?"),
        F("Де'ти вели' ___ хорошо'. (themselves)", "себя'", ["себе'", "собо'й", "их"], "Вести' себя'.", "The children behaved well."),
        F("Она' взяла' на ___ отве'тственность. (herself)", "себя'", ["себе'", "собо'й", "её"], "Брать на себя'.", "She took responsibility upon herself."),
        F("Я не могу' позво'лить ___ тако'й тур. (myself)", "себе'", ["себя'", "собо'й", "мне"], "Позво'лить себе'.", "I can't afford such a tour."),
        F("Он счита'ет ___ специали'стом. (himself)", "себя'", ["себе'", "собо'й", "его'"], "Счита'ть себя' кем.", "He considers himself a specialist."),
        F("Она' ста'вит пе'ред ___ но'вые це'ли. (herself)", "собо'й", ["себя'", "себе'", "ней"], "Пе'ред + instrumental.", "She sets herself new goals."),
        F("Предста'вь ___ э'ту карти'ну! (to yourself)", "себе'", ["себя'", "собо'й", "тебе'"], "Представля'ть себе'.", "Imagine this picture!"),
        mc("‘Он вёл себя' пло'хо’ means:", ["He behaved badly.", "He felt bad.", "He led a bad life.", "He drove badly."], "He behaved badly.", "Вести' себя'.", order=True),
        mc("Which phrase means ‘to afford’?", ["позво'лить себе'", "взять на себя'", "вести' себя'", "ви'деть себя'"], "позво'лить себе'", "Literally: allow oneself.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 318
L318 = lesson(
    "Word-building: крат / корот, пуск / пуст, прав, ступ",
    "Выпускни'к, упуще'ние, исправля'ть, поступа'ть — одни' и те же ко'рни.",
    requires=["выпуск", "пускать", "управление", "управлять", "поступок", "вступить", "уступить", "короткий"],
    cards=[
        card("КРАТ – КОРОТ: short",
             "Both roots mean ‘short’. Прекраща'ть is to make something stop (cut it short), and сокраща'ть is to shorten.",
             tables=[table(
                 ["Word", "English"],
                 [["коро'ткий", "short"],
                  ["кра'ткий", "brief"],
                  ["сократи'ть", "to shorten, reduce"],
                  ["прекрати'ть", "to stop"],
                  ["укоро'ченный", "shortened"]])],
             examples=[
                 ex("Они' сократи'ли рабо'чий день.", "They shortened the working day.", "сократи'ли"),
                 ex("Да'йте кра'ткий отве'т.", "Give a brief answer.", "кра'ткий"),
             ]),
        card("ПУСК – ПУСТ: let go",
             "The root means ‘let go, release, allow’.",
             tables=[table(
                 ["Word", "English"],
                 [["вы'пуск", "release; issue; graduating class"],
                  ["выпускни'к", "graduate"],
                  ["пуска'ть", "to let in"],
                  ["упусти'ть", "to miss, let slip"],
                  ["упуще'ние", "oversight"],
                  ["допусти'мо", "it is permissible"]])],
             examples=[
                 ex("Он упусти'л возмо'жность.", "He missed the opportunity.", "упусти'л"),
             ]),
        card("ПРАВ and СТУП",
             "Прав means ‘right, direct’. Ступ means ‘step, act’.",
             tables=[table(
                 ["Word", "English"],
                 [["направле'ние", "direction; field (of study)"],
                  ["прави'тельство", "government"],
                  ["управля'ть", "to manage, drive"],
                  ["испра'вить", "to correct"],
                  ["поступи'ть", "to enter, to act"],
                  ["посту'пок", "action, deed"],
                  ["просту'пок", "misdeed"],
                  ["уступи'ть", "to give way"]])],
             examples=[
                 ex("Он испра'вил оши'бку.", "He corrected the mistake.", "испра'вил"),
                 ex("Э'то хоро'ший посту'пок.", "This is a good deed.", "посту'пок"),
                 ex("Она' уступи'ла ме'сто в авто'бусе.", "She gave up her seat on the bus.", "уступи'ла"),
             ]),
    ],
    verify=(vf("короткий", "короткий") + vf("краткий", "краткий") + vf("сократить", "сократили") + vf("прекратить", "прекратить")
            + vf("выпуск", "выпуск") + vf("выпускник", "выпускник") + vf("пускать", "пускать") + vf("упустить", "упустил")
            + vf("упущение", "упущение") + vf("направление", "направление") + vf("правительство", "правительство") + vf("управлять", "управлять")
            + vf("исправить", "исправил") + vf("поступить", "поступить") + vf("поступок", "поступок") + vf("проступок", "проступок")
            + vf("уступить", "уступила") + vf("вступить", "вступить")),
    exercises=[
        F("Они' ___ рабо'чий день. (shortened)", "сократи'ли", ["пуска'ли", "уступи'ли", "исправи'ли"], "The root крат: shorten.", "They shortened the working day.", lemma="сократить"),
        F("Он ___ возмо'жность. (missed)", "упусти'л", ["упусти'ть", "сократи'л", "поступи'л"], "Root пуст: let slip.", "He missed the opportunity.", lemma="упустить"),
        F("Он ___ оши'бку. (corrected)", "испра'вил", ["упусти'л", "уступи'л", "сократи'л"], "Root прав: make right.", "He corrected the mistake.", lemma="исправить"),
        F("Э'то хоро'ший ___. (deed)", "посту'пок", ["вы'пуск", "проступо'к", "направле'ние"], "Root ступ.", "This is a good deed.", lemma="поступок"),
        F("Она' ___ ме'сто в авто'бусе. (gave up)", "уступи'ла", ["упусти'ла", "испра'вила", "сократи'ла"], "Root ступ: give way.", "She gave up her seat on the bus.", lemma="уступить"),
        mc("The root ПУСК/ПУСТ means:", ["let go, release", "right, direct", "step", "short"], "let go, release", "Выпускни'к, пуска'ть.", order=True),
        mc("The root КРАТ/КОРОТ means:", ["short", "step", "right", "let go"], "short", "Кра'ткий, коро'ткий.", order=True),
        mc("Which word means ‘government’ (root прав)?", ["прави'тельство", "посту'пок", "упуще'ние", "вы'пуск"], "прави'тельство", "Root прав.", order=True),
        mc("A просту'пок is:", ["a misdeed", "a step", "an exit", "a release"], "a misdeed", "Про- + ступ: a step over the line.", order=True),
    ],
)
# ---------------------------------------------------------------------------- 319
L319 = lesson(
    "Review: -ся, себя' and word roots",
    "Це'ны поднима'ются, а она' ве'дёт себя' споко'йно.",
    requires=["себя", "встречаться", "отменить", "поступок", "чувствовать", "строить"],
    cards=[
        card("What to remember",
             "The ending -ся can mean reflexive, reciprocal, or passive-like. Use it when there is no direct object. Себя' has no nominative; its forms are себя', себе', собо'й, о себе'.",
             tables=[table(
                 ["Idea", "Example"],
                 [["reflexive", "Малы'ш умыва'ется."],
                  ["reciprocal", "Мы встреча'емся."],
                  ["passive-like", "Рейс отменя'ется."],
                  ["себя' + prep.", "к себе', у себя', с собо'й, про себя'"],
                  ["fixed phrases", "чу'вствовать себя', вести' себя', позво'лить себе'"]])],
             examples=[
                 ex("Це'ны поднима'ются, а она' ве'дёт себя' споко'йно.", "Prices are rising, but she is behaving calmly.", "ве'дёт себя'"),
             ]),
    ],
    verify=(vf("вести", "ведёт") + vf("подниматься", "поднимаются") + vf("спокойный", "спокойно")),
    exercises=[
        F("Рейс ___ из-за снегопа'да. (is being cancelled)", "отменя'ется", ["отменя'ет", "отменя'ют", "отменя'ть"], "Рейс is the subject: -ся.", "The flight is being cancelled because of the snowfall."),
        F("Авиакомпа'ния ___ рейс. (cancels)", "отменя'ет", ["отменя'ется", "отменя'ются", "отменя'ть"], "Direct object: no -ся.", "The airline cancels the flight."),
        F("Мы ча'сто ___ по пя'тницам. (meet)", "встреча'емся", ["встреча'ем", "встреча'ете", "встреча'ются"], "Reciprocal.", "We often meet on Fridays."),
        F("Он ду'мает то'лько о ___. (himself)", "себе'", ["себя'", "собо'й", "тебе'"], "О + prepositional.", "He thinks only of himself."),
        F("Я приглашу' вас ___. (to my place)", "к себе'", ["у себя'", "с собо'й", "на себя'"], "Куда'? К себе'.", "I'll invite you to my place."),
        F("Как ты ___ чу'вствуешь? (yourself)", "себя'", ["себе'", "собо'й", "тебя'"], "Чу'вствовать себя'.", "How do you feel?"),
        F("Уро'к ___ в три часа'. (ended)", "зако'нчился", ["зако'нчил", "зако'нчила", "зако'нчить"], "No object: -ся.", "The lesson ended at three o'clock.", lemma="закончиться"),
        F("Э'то хоро'ший ___. (deed)", "посту'пок", ["вы'пуск", "проступо'к", "направле'ние"], "Root ступ.", "This is a good deed.", lemma="поступок"),
        mc("Which sentence is correct?", ["Дом стро'ится рабо'чими.", "Дом стро'ит рабо'чими.", "Дом стро'ятся рабо'чими.", "Дом стро'ится рабо'чие."], "Дом стро'ится рабо'чими.", "Passive-like -ся, doer in the instrumental.", order=True),
        mc("On a door, ‘от себя'’ means:", ["push", "pull", "open", "locked"], "push", "Away from yourself.", order=True),
    ],
)

UNIT = unit("Unit 31: Reflexive verbs, себя' and word-building",
            [L311, L312, L313, L314, L315, L316, L317, L318, L319])
