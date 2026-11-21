"""Unit 8: getting around town  (textbook module 2, lesson 12)."""
from dsl import *

# ---------------------------------------------------------------------------- 50
L50 = lesson(
    "Going by vehicle: е'хать and е'здить",
    "Еду' сейча'с, е'зжу ка'ждый день",
    requires=["ехать", "ездить", "машина", "автобус", "рынок"],
    cards=[
        card("The vehicle twins of идти' and ходи'ть",
             "When you travel by car, bus, train or any vehicle, Russian uses е'хать (one trip in one direction, "
             "right now, with a destination, or a planned trip) and е'здить (habits, round trips, general "
             "ability, liking, negative commands). They work exactly like идти' and ходи'ть. To stress that you "
             "go on foot, add пешко'м: Я хожу' на рабо'ту пешко'м.",
             tables=[table(
                 ["Person", "е'хать", "е'здить"],
                 [["я", "е'д{у}", "е'зж{у}"],
                  ["ты", "е'д{ешь}", "е'зд{ишь}"],
                  ["он · она' · оно'", "е'д{ет}", "е'зд{ит}"],
                  ["мы", "е'д{ем}", "е'зд{им}"],
                  ["вы", "е'д{ете}", "е'зд{ите}"],
                  ["они'", "е'д{ут}", "е'зд{ят}"]],
                 note="Past: е'хал, е'хала, е'хали · е'здил, е'здила, е'здили. Е'здить has the д → ж change in the я-form.")]),
        card("Which one?",
             "Same logic as for walking. Сейча'с, куда'?, за'втра (a planned trip) point to е'хать; ка'ждый день, "
             "ча'сто, люблю' point to е'здить. In the past е'здил means a round trip, so Вчера' я е'здил на ры'нок "
             "means I went there and came back. For a positive command to go by vehicle use поезжа'й(те); for "
             "a negative one, не е'зди(те).",
             examples=[
                 ex("Сейча'с я е'ду домо'й.", "Right now I'm driving home.", "е'ду"),
                 ex("Ка'ждую суббо'ту я е'зжу на ры'нок.", "Every Saturday I go to the market.", "е'зжу"),
                 ex("За'втра мы е'дем в аэропо'рт.", "Tomorrow we are going to the airport.", "е'дем"),
                 ex("Вчера' он е'здил на ры'нок.", "Yesterday he went to the market (and came back).", "е'здил"),
                 ex("Поезжа'й на метро'!", "Go by subway!", "Поезжа'й"),
             ]),
    ],
    verify=(vf("ехать", "еду", "едешь", "едет", "едем", "едете", "едут", "ехал", "ехала", "ехали")
            + vf("ездить", "езжу", "ездишь", "ездит", "ездим", "ездите", "ездят", "ездил", "ездила", "ездили")
            + vf("поехать", "поезжай", "поезжайте")),
    exercises=[
        fb("Ка'ждую суббо'ту я ___ на ры'нок на авто'бусе.", ["е'зжу", "е'ду", "иду'", "хожу'"], "е'зжу",
           "A weekly habit by bus: е'здить.", tr="Every Saturday I go to the market by bus.", lemma="ездить"),
        fb("Сейча'с мы ___ в аэропо'рт на такси'.", ["е'дем", "е'здим", "идём", "хо'дим"], "е'дем",
           "Right now, one direction, by vehicle: е'хать.", tr="Right now we're going to the airport by taxi.", lemma="ехать"),
        fb("Я не люблю' ___ на маши'не.", ["е'здить", "е'здим", "е'ду", "е'зжу"], "е'здить",
           "A general liking: е'здить.", tr="I don't like driving."),
        fb("За'втра они' ___ в Москву'.", ["е'дут", "е'здят", "е'дет", "е'дем"], "е'дут",
           "A planned trip: е'хать.", tr="Tomorrow they are going to Moscow.", lemma="ехать"),
        fb("___ на метро'!", ["Поезжа'й", "Е'зди", "Е'зжу", "Е'ду"], "Поезжа'й",
           "A positive command to go by vehicle: поезжа'й.", tr="Go by subway!"),
        fb("В институ'т я хожу' ___.", ["пешко'м", "на маши'не", "на авто'бусе", "в маши'не"], "пешко'м",
           "Пешко'м adds “on foot”.", tr="I go to the institute on foot."),
        mc("Which sentence means “Yesterday he went to the market (and came back)”?",
           ["Вчера' он е'здил на ры'нок.", "Вчера' он е'хал на ры'нок.", "Вчера' он е'дет на ры'нок.", "Вчера' он е'зжу на ры'нок."],
           "Вчера' он е'здил на ры'нок.", "Past е'здил = a completed round trip."),
        mc("Which verb fits “Every day I go to work by car”?",
           ["е'здить", "е'хать", "идти'", "ходи'ть"], "е'здить", "A daily habit by vehicle.", order=True),
        mc("What do you add to ходи'ть/идти' to stress that you go on foot?",
           ["пешко'м", "на маши'не", "домо'й", "вме'сте"], "пешко'м", "Пешко'м = on foot."),
    ],
)

# ---------------------------------------------------------------------------- 51
L51 = lesson(
    "By bus, on the bus: на and в with transport",
    "На авто'бусе, в авто'бусе",
    requires=["автобус", "машина", "поезд", "метро", "самолёт"],
    cards=[
        card("How you travel vs where you are",
             "To say how you travel use на plus the prepositional case: е'хать на авто'бусе, на по'езде, "
             "на маши'не. To say where you are, inside the vehicle, use в plus the prepositional: в авто'бусе, "
             "в по'езде. Two nouns never change: метро' and такси'. Because they do not decline, only на or в "
             "(and the context) shows the difference.",
             tables=[table(
                 ["Vehicle", "By …  (на)", "Inside …  (в)"],
                 [["авто'бус", "на авто'бус{е}", "в авто'бус{е}"],
                  ["маши'на", "на маши'н{е}", "в маши'н{е}"],
                  ["по'езд", "на по'езд{е}", "в по'езд{е}"],
                  ["самолёт", "на самолёт{е}", "в самолёт{е}"],
                  ["велосипе'д", "на велосипе'д{е}", "—"],
                  ["метро' · такси'", "на метро' · на такси'", "в метро' · в такси'"]])],
             examples=[
                 ex("Я е'зжу туда' на авто'бусе.", "I go there by bus.", "на авто'бусе"),
                 ex("В авто'бусе я чита'ю газе'ту.", "On the bus I read the paper.", "В авто'бусе"),
                 ex("Мы е'дем на по'езде.", "We are traveling by train.", "на по'езде"),
                 ex("В по'езде нельзя' кури'ть.", "You may not smoke on a train.", "В по'езде"),
             ]),
    ],
    verify=(vf("автобус", "автобусе") + vf("машина", "машине") + vf("поезд", "поезде")
            + vf("самолёт", "самолёте") + vf("велосипед", "велосипеде")),
    exercises=[
        fb("Я е'зжу на рабо'ту ___.", ["на авто'бусе", "в авто'бусе", "на авто'бус", "авто'бусе"], "на авто'бусе",
           "By bus = на + prepositional.", tr="I go to work by bus."),
        fb("___ я чита'ю газе'ту.", ["В авто'бусе", "На авто'бусе", "В авто'бус", "На авто'бус"], "В авто'бусе",
           "Inside the bus = в + prepositional.", tr="On the bus I read the paper."),
        fb("Мы е'дем домо'й ___.", ["на по'езде", "в по'езде", "на по'езд", "по'езде"], "на по'езде",
           "By train = на по'езде.", tr="We're going home by train."),
        fb("В ___ нельзя' кури'ть.", ["по'езде", "по'езд", "по'езда", "по'езду"], "по'езде",
           "Prepositional after в.", tr="You can't smoke on a train."),
        fb("Мы е'дем в аэропо'рт ___.", ["на такси'", "в такси'", "на таксе'", "на такси'е"], "на такси'",
           "Такси' never changes.", tr="We're going to the airport by taxi."),
        fb("Я люблю' е'здить ___.", ["на велосипе'де", "в велосипе'де", "на велосипе'д", "велосипе'де"], "на велосипе'де",
           "By bicycle = на + prepositional.", tr="I like to ride a bicycle."),
        mc("Which preposition means “by” a vehicle?", ["на", "в", "к", "из"], "на",
           "Е'хать на + prepositional.", order=True),
        mc("Which phrase means “inside the bus”?",
           ["в авто'бусе", "на авто'бусе", "в авто'бус", "на авто'бус"], "в авто'бусе", "Location inside: в + prepositional."),
        mc("What is special about метро' and такси'?",
           ["They never change", "They are feminine", "They are plural", "They are masculine"], "They never change",
           "Indeclinable nouns look the same in every case.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 52
L52 = lesson(
    "In the forest, on the bridge: the second prepositional",
    "В лесу', на мосту', в саду'",
    requires=["лес", "сад", "мост", "угол", "берег"],
    cards=[
        card("Place: stressed -у'",
             "A small group of masculine nouns, mostly one-syllable, has two prepositional forms. To say where "
             "something is after в or на, they take a stressed -у' (or -ю'): в лесу', в саду', на мосту'. To say "
             "what you are talking about after о, they use the ordinary -е: о ле'се, о са'де, о мосте'. Learn "
             "them as pairs, because the stress changes too.",
             tables=[table(
                 ["Nominative", "Где? (place)", "О чём? (about)"],
                 [["лес", "в лес{у'}", "о ле'с{е}"],
                  ["сад", "в сад{у'}", "о са'д{е}"],
                  ["мост", "на мост{у'}", "о мост{е'}"],
                  ["у'гол", "на угл{у'} · в угл{у'}", "об угл{е'}"],
                  ["пол", "на пол{у'}", "о по'л{е}"],
                  ["шкаф", "в шкаф{у'}", "о шка'ф{е}"],
                  ["порт", "в порт{у'}", "о по'рт{е}"],
                  ["аэропо'рт", "в аэропорт{у'}", "об аэропо'рт{е}"],
                  ["бе'рег", "на берег{у'}", "о бе'рег{е}"]])],
             examples=[
                 ex("Мой дя'дя рабо'тает в саду'.", "My uncle works in the garden.", "в саду'"),
                 ex("Он ча'сто говори'т о са'де.", "He often talks about the garden.", "о са'де"),
                 ex("Маши'на стои'т на мосту'.", "The car is standing on the bridge.", "на мосту'"),
                 ex("Все мои' ве'щи в шкафу'.", "All my things are in the wardrobe.", "в шкафу'"),
             ]),
    ],
    verify=(vf("лес", "лесу", "лесе") + vf("сад", "саду", "саде") + vf("мост", "мосту", "мосте")
            + vf("угол", "углу", "угле") + vf("пол", "полу", "поле") + vf("шкаф", "шкафу", "шкафе")
            + vf("порт", "порту", "порте") + vf("аэропорт", "аэропорту", "аэропорте") + vf("берег", "берегу", "береге")),
    exercises=[
        fb("Мы гуля'ем в ___.", ["лесу'", "ле'се", "лес", "леса'"], "лесу'",
           "Place after в: stressed -у'.", tr="We're walking in the forest.", lemma="лес"),
        fb("Он говори'т о ___.", ["ле'се", "лесу'", "лес", "леса'"], "ле'се",
           "After о the regular -е.", tr="He's talking about the forest.", lemma="лес"),
        fb("Мой дя'дя рабо'тает в ___.", ["саду'", "са'де", "сад", "сада'"], "саду'",
           "Place: -у'.", tr="My uncle works in the garden.", lemma="сад"),
        fb("Я ви'жу маши'ну на ___.", ["мосту'", "мосте'", "мост", "моста'"], "мосту'",
           "Place: -у'.", tr="I see a car on the bridge.", lemma="мост"),
        fb("Кни'га на ___.", ["полу'", "по'ле", "пол", "пола'"], "полу'",
           "Place: -у'.", tr="The book is on the floor.", lemma="пол"),
        fb("Все мои' ве'щи в ___.", ["шкафу'", "шка'фе", "шкаф", "шкафа'"], "шкафу'",
           "Place: -у'.", tr="All my things are in the wardrobe.", lemma="шкаф"),
        fb("Он ждёт на ___.", ["углу'", "угле'", "у'гол", "угла'"], "углу'",
           "Place: the о drops out too: у'гол → углу'.", tr="He's waiting on the corner.", lemma="угол"),
        mc("Which ending marks the “place” form of лес?", ["stressed -у", "-е", "-ом", "-а"], "stressed -у",
           "В лесу', на мосту'.", order=True),
        mc("Which form is used for “about the forest”?",
           ["о ле'се", "о лесу'", "о леса'", "о лес"], "о ле'се", "After о use the regular -е."),
    ],
)

# ---------------------------------------------------------------------------- 53
L53 = lesson(
    "About me, about him: pronouns in the prepositional",
    "Обо мне', о нём, о ней",
    requires=["тебе", "нём", "ней", "них", "нас"],
    cards=[
        card("Seven forms",
             "Personal pronouns have a prepositional case, used after о, в, на and other prepositions that take it. "
             "The forms for он, она' and они' always start with н because a preposition always stands in front of "
             "them. With мне, о becomes обо and в becomes во.",
             tables=[table(
                 ["Nominative", "Prepositional", "Example"],
                 [["я", "мне", "Он ду'мает о'бо мне."],
                  ["ты", "тебе'", "Я ду'маю о тебе'."],
                  ["он · оно'", "нём", "Мы говори'м о нём."],
                  ["она'", "ней", "Он ду'мает о ней."],
                  ["мы", "нас", "Они' говоря'т о нас."],
                  ["вы", "вас", "Мы ду'маем о вас."],
                  ["они'", "них", "Ты ду'маешь о них?"]])],
             examples=[
                 ex("Что ты во мне ви'дишь?", "What do you see in me?", "во мне"),
                 ex("Я ду'маю о тебе'.", "I'm thinking about you.", "о тебе'"),
                 ex("Мы говори'м о нём.", "We're talking about him.", "о нём"),
             ]),
    ],
    verify=[("я", "мне"), ("ты", "тебе"), ("он", "нём"), ("она", "ней"), ("мы", "нас"), ("вы", "вас"), ("они", "них")],
    exercises=[
        fb("Я ду'маю о ___. (him)", ["нём", "его'", "ему'", "он"], "нём",
           "Prepositional of он: нём.", tr="I'm thinking about him."),
        fb("Мы говори'м о ___. (her)", ["ней", "её", "ей", "она'"], "ней",
           "Prepositional of она': ней.", tr="We're talking about her."),
        fb("Они' говоря'т о ___. (us)", ["нас", "нам", "мы", "на'ми"], "нас",
           "Prepositional of мы: нас.", tr="They're talking about us."),
        fb("Он ду'мает ___ мне.", ["обо", "о", "об", "на"], "обо",
           "With мне, о becomes обо.", tr="He's thinking about me."),
        fb("Что ты ___ мне ви'дишь?", ["во", "в", "на", "о"], "во",
           "With мне, в becomes во.", tr="What do you see in me?"),
        fb("Мы расска'зываем о ___. (them)", ["них", "их", "им", "они'"], "них",
           "Prepositional of они': них.", tr="We're telling about them."),
        fb("Я ду'маю о ___. (you, ты)", ["тебе'", "тебя'", "ты", "тобо'й"], "тебе'",
           "Prepositional of ты: тебе'.", tr="I'm thinking about you."),
        mc("Which phrase means “about me”?", ["обо мне", "о меня'", "о я", "о мной"], "обо мне",
           "Prepositional of я: мне, with обо."),
        mc("Why is it о нём and not о него'?",
           ["The prepositional of он is нём", "Because it is accusative", "Because нём is plural", "It's an exception"],
           "The prepositional of он is нём", "Он → нём, она' → ней, они' → них.", order=True),
        mc("Which pronoun has ней in the prepositional?", ["она'", "он", "они'", "мы"], "она'",
           "Она' → ней.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 54
L54 = lesson(
    "Nobody, nothing, never: ни- words",
    "Никто', ничего', никогда', нигде', никуда'",
    requires=["никто", "никогда", "никуда", "нигде", "ничто"],
    cards=[
        card("Add ни- to a question word",
             "Negative pronouns and adverbs are made by putting ни- in front of a question word. The key rule: "
             "the verb must still carry не. Russian does not mind a double (or triple) negative; it requires it. "
             "Ничто' (nothing) is only used as a subject; the usual form after a negated verb is ничего'.",
             tables=[table(
                 ["Question", "Negative", "Meaning"],
                 [["кто?", "{ни}кто'", "no one"],
                  ["кого'?", "{ни}кого'", "(not) anyone"],
                  ["что?", "{ни}чего'", "(not) anything"],
                  ["когда'?", "{ни}когда'", "never"],
                  ["где?", "{ни}где'", "nowhere"],
                  ["куда'?", "{ни}куда'", "(not) anywhere (motion)"]])]),
        card("In sentences",
             "Put не right before the verb, and the ни- word wherever it fits. Remember: нигде' is for where "
             "something is, никуда' is for where someone goes. The particle не can also negate a single word "
             "other than the verb: Я рабо'таю не здесь, а там.",
             examples=[
                 ex("Он никогда' не рабо'тает.", "He never works.", "никогда' не"),
                 ex("Я ничего' не зна'ю.", "I don't know anything.", "ничего' не"),
                 ex("Они' никуда' не иду'т.", "They aren't going anywhere.", "никуда' не"),
                 ex("Я никого' не ви'дел.", "I didn't see anyone.", "никого' не"),
                 ex("Никто' не зна'ет.", "No one knows.", "Никто' не"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("Я ___ не зна'ю.", ["ничего'", "что", "чего'", "ничто'"], "ничего'",
           "After a negated verb: ничего'.", tr="I don't know anything."),
        fb("Он ___ не рабо'тает.", ["никогда'", "когда'", "нигде'", "никуда'"], "никогда'",
           "Never = никогда'.", tr="He never works."),
        fb("Мы ___ не идём.", ["никуда'", "нигде'", "никогда'", "никто'"], "никуда'",
           "Going nowhere: никуда'.", tr="We're not going anywhere."),
        fb("Мой друг ___ не рабо'тает.", ["нигде'", "никуда'", "никогда'", "никто'"], "нигде'",
           "Not working anywhere (location): нигде'.", tr="My friend doesn't work anywhere."),
        fb("Я ___ здесь не зна'ю.", ["никого'", "никто'", "ничего'", "никуда'"], "никого'",
           "Not anyone, as an object: никого'.", tr="I don't know anyone here."),
        fb("___ не зна'ет э'того.", ["Никто'", "Никого'", "Ничего'", "Никогда'"], "Никто'",
           "No one, as a subject: никто'.", tr="No one knows this."),
        mc("What must a sentence with никогда' also have?",
           ["не before the verb", "нет", "ни", "nothing else"], "не before the verb",
           "Russian uses a double negative.", order=True),
        mc("Which means “nowhere” (location)?", ["нигде'", "никуда'", "никогда'", "никто'"], "нигде'",
           "Где? → нигде'."),
        mc("How do you say “I didn't see anyone”?",
           ["Я никого' не ви'дел.", "Я никого' ви'дел.", "Я никто' не ви'дел.", "Я не ви'дел никто'."],
           "Я никого' не ви'дел.", "Object form никого', plus не."),
    ],
)

# ---------------------------------------------------------------------------- 55
L55 = lesson(
    "Can and want: мочь and хоте'ть",
    "Могу', хочу'",
    requires=["мочь", "хотеть", "можно", "нельзя", "купить"],
    cards=[
        card("Two irregular verbs",
             "Мочь (can, to be able to) and хоте'ть (to want) are irregular, and both are followed by an "
             "infinitive. Мочь has a changing stem (мог-/мож-). Хоте'ть is a mix: its singular forms follow the "
             "first family and its plural forms the second.",
             tables=[table(
                 ["Person", "мочь", "хоте'ть"],
                 [["я", "мог{у'}", "хоч{у'}"],
                  ["ты", "мо'ж{ешь}", "хо'ч{ешь}"],
                  ["он · она' · оно'", "мо'ж{ет}", "хо'ч{ет}"],
                  ["мы", "мо'ж{ем}", "хот{и'м}"],
                  ["вы", "мо'ж{ете}", "хот{и'те}"],
                  ["они'", "мо'г{ут}", "хот{я'т}"]],
                 note="Past: мог, могла', могло', могли' · хоте'л, хоте'ла, хоте'ло, хоте'ли.")],
             examples=[
                 ex("Я могу' чита'ть по-ру'сски.", "I can read Russian.", "могу'"),
                 ex("Ты мо'жешь говори'ть ме'дленно?", "Can you speak slowly?", "мо'жешь"),
                 ex("Он хо'чет купи'ть маши'ну, но не мо'жет.", "He wants to buy a car, but he can't.", "хо'чет"),
                 ex("Мы хоти'м идти' домо'й.", "We want to go home.", "хоти'м"),
             ]),
        card("Can vs. may",
             "You already know мо'жно (it is allowed) and нельзя' (it is not allowed). They describe permission "
             "with no subject. Мочь with a person says that someone is able, or has the opportunity, to do "
             "something: Здесь мо'жно кури'ть (it is allowed), but Я не могу' кури'ть (I can't, perhaps because "
             "I'm ill).",
             tables=[table(
                 ["Impersonal", "Personal"],
                 [["Здесь мо'жно чита'ть.", "Я могу' чита'ть."],
                  ["Здесь нельзя' кури'ть.", "Я не могу' кури'ть."]])]),
    ],
    verify=(vf("мочь", "могу", "можешь", "может", "можем", "можете", "могут", "мог", "могла", "могло", "могли")
            + vf("хотеть", "хочу", "хочешь", "хочет", "хотим", "хотите", "хотят", "хотел", "хотела", "хотели")),
    exercises=[
        fb("Я ___ чита'ть по-ру'сски.", ["могу'", "мо'жешь", "мо'жет", "мо'гут"], "могу'",
           "Я → могу'.", tr="I can read Russian.", lemma="мочь"),
        fb("Ты ___ говори'ть ме'дленно?", ["мо'жешь", "могу'", "мо'жет", "мо'жем"], "мо'жешь",
           "Ты → мо'жешь.", tr="Can you speak slowly?", lemma="мочь"),
        fb("Мы ___ купи'ть э'ту маши'ну.", ["хоти'м", "хо'чем", "хо'чет", "хочу'"], "хоти'м",
           "Plural forms of хоте'ть follow the second family: хоти'м.", tr="We want to buy this car.", lemma="хотеть"),
        fb("Они' ___ идти' домо'й.", ["хотя'т", "хо'тят", "хо'чут", "хочу'"], "хотя'т",
           "Они' → хотя'т.", tr="They want to go home.", lemma="хотеть"),
        fb("Вчера' она' не ___ говори'ть.", ["могла'", "мог", "могло'", "могли'"], "могла'",
           "Past feminine: могла'.", tr="Yesterday she couldn't talk.", lemma="мочь"),
        fb("Он ___ купи'ть маши'ну, но не мо'жет.", ["хо'чет", "хоти'т", "хотя'т", "хочу'"], "хо'чет",
           "Singular он → хо'чет.", tr="He wants to buy a car, but he can't.", lemma="хотеть"),
        mc("What follows мочь and хоте'ть?", ["an infinitive", "a past form", "an accusative pronoun only", "nothing"], "an infinitive",
           "Могу' чита'ть, хочу' идти'.", order=True),
        mc("Which form means “we can”?", ["мо'жем", "мо'жете", "могу'", "мо'гут"], "мо'жем", "Мы → мо'жем."),
        mc("What is the difference between мо'жно and я могу'?",
           ["Мо'жно says it is allowed; я могу' says I am able", "They are identical", "Мо'жно is past", "Я могу' has no subject"],
           "Мо'жно says it is allowed; я могу' says I am able", "Impersonal permission vs personal ability.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 56
L56 = lesson(
    "Asking the way",
    "Извини'те, как попа'сть на вокза'л?",
    requires=["прямо", "далеко", "рядом", "площадь", "улица"],
    cards=[
        card("Useful questions",
             "Start with Извини'те (excuse me). Then ask where something is, or how to get there. Нахо'дится "
             "(is located) agrees with what you ask about: нахо'дится for one thing, нахо'дятся for several. "
             "Как попа'сть в … / на … ? takes the accusative, so use the same в or на that the place takes.",
             tables=[table(
                 ["Question", "Meaning"],
                 [["Где нахо'дится музе'й?", "Where is the museum located?"],
                  ["Где нахо'дятся остано'вки?", "Where are the bus stops?"],
                  ["Как попа'сть в музе'й?", "How do I get to the museum?"],
                  ["Как попа'сть на вокза'л?", "How do I get to the station?"]])]),
        card("Answers",
             "Directions use commands (иди'те, поезжа'йте) and a few small words: пря'мо (straight on), "
             "напра'во (to the right), нале'во (to the left), далеко' (far), недалеко' (not far), ря'дом (nearby). "
             "A distance can be one block: оди'н кварта'л.",
             examples=[
                 ex("Иди'те пря'мо, пото'м нале'во.", "Go straight, then left.", "пря'мо"),
                 ex("Вокза'л недалеко'.", "The station isn't far.", "недалеко'"),
                 ex("Пло'щадь далеко'?", "Is the square far?", "далеко'"),
                 ex("Иди'те оди'н кварта'л пря'мо.", "Go one block straight ahead.", "оди'н кварта'л"),
                 ex("Метро' ря'дом.", "The subway is nearby.", "ря'дом"),
             ]),
    ],
    verify=vf("находиться", "находится", "находятся"),
    exercises=[
        fb("Как попа'сть ___ музе'й?", ["в", "на", "к", "у"], "в",
           "Музе'й takes в; Как попа'сть + accusative.", tr="How do I get to the museum?"),
        fb("Как попа'сть ___ вокза'л?", ["на", "в", "к", "у"], "на",
           "Вокза'л takes на.", tr="How do I get to the station?"),
        fb("Иди'те ___, пото'м нале'во.", ["пря'мо", "далеко'", "ря'дом", "до'ма"], "пря'мо",
           "Пря'мо = straight ahead.", tr="Go straight, then left."),
        fb("Извини'те, где ___ вокза'л?", ["нахо'дится", "нахо'дятся", "нахо'дит", "нахожу'сь"], "нахо'дится",
           "Вокза'л is singular.", tr="Excuse me, where is the station located?", lemma="находиться"),
        fb("Где ___ остано'вки?", ["нахо'дятся", "нахо'дится", "нахо'дит", "нахо'дят"], "нахо'дятся",
           "Plural subject.", tr="Where are the stops located?", lemma="находиться"),
        mc("Which word means “to the left”?", ["нале'во", "напра'во", "пря'мо", "ря'дом"], "нале'во",
           "Нале'во = left, напра'во = right."),
        mc("Which word means “straight ahead”?", ["пря'мо", "нале'во", "напра'во", "далеко'"], "пря'мо", "Пря'мо."),
        mc("What case follows Как попа'сть в …?", ["accusative", "prepositional", "nominative", "genitive"], "accusative",
           "Where to? → accusative.", order=True),
        mc("How do you ask “Where is the museum located?”",
           ["Где нахо'дится музе'й?", "Куда' нахо'дится музе'й?", "Где нахо'дятся музе'й?", "Как нахо'дится музе'й?"],
           "Где нахо'дится музе'й?", "Где нахо'дится + a singular subject."),
    ],
)

# ---------------------------------------------------------------------------- 57
L57 = lesson(
    "Review: walking, riding, having, liking",
    "Putting lessons 42 to 56 together",
    requires=["ходить", "ехать", "мочь", "хотеть", "нравиться"],
    threshold=0.5,
    cards=[
        card("What do I need?",
             "A map of what you have learned since lesson 42. Use it to choose a form before you speak.",
             tables=[table(
                 ["Ask yourself", "Use", "Example"],
                 [["How often?", "всегда', иногда', ка'ждый день", "Ка'ждую суббо'ту я до'ма."],
                  ["On foot or by vehicle? One trip or habit?", "идти'/ходи'ть · е'хать/е'здить", "Сейча'с я иду'. Ка'ждый день я е'зжу."],
                  ["Talking about …", "о (об) + prepositional", "Мы говори'м о нём. Об отце'."],
                  ["Does it exist? Do I have it?", "есть · у меня' есть", "В го'роде есть мост. У нас есть дом."],
                  ["Do I like it?", "мне нра'вится / нра'вятся", "Мне нра'вятся э'ти фи'льмы."],
                  ["By what? Where inside?", "на / в + prepositional", "на авто'бусе · в по'езде"],
                  ["Nothing, nobody, never", "ни- word + не", "Я ничего' не зна'ю."],
                  ["Can, want", "мочь, хоте'ть + infinitive", "Я могу' и хочу' идти'."]])]),
    ],
    verify=[],
    exercises=[
        fb("Ка'ждый день я ___ в институ'т пешко'м.", ["хожу'", "иду'", "е'ду", "е'зжу"], "хожу'",
           "Every day, on foot: ходи'ть.", tr="Every day I walk to the institute."),
        fb("Сейча'с мы ___ домо'й на авто'бусе.", ["е'дем", "е'здим", "идём", "хо'дим"], "е'дем",
           "Right now, by vehicle: е'хать.", tr="Right now we're going home by bus."),
        fb("Она' ду'мает ___ тебе'.", ["о", "об", "на", "в"], "о",
           "Тебе' starts with a consonant: о.", tr="She's thinking about you."),
        fb("У ___ есть брат. (she)", ["неё", "её", "она'", "ей"], "неё",
           "After у: неё.", tr="She has a brother."),
        fb("Мне ___ э'ти кни'ги.", ["нра'вятся", "нра'вится", "нра'вишься", "нра'вимся"], "нра'вятся",
           "Plural things: нра'вятся.", tr="I like these books."),
        fb("Мы о'бе ___ в Москве'. (two women)", ["живём", "живёт", "живёшь", "живу'т"], "живём",
           "Мы takes живём.", tr="We both live in Moscow."),
        fb("Мы ___ ехать на метро'.", ["хоти'м", "хо'чет", "хочу'", "хотя'т"], "хоти'м",
           "Мы → хоти'м.", tr="We want to go by subway."),
        fb("Он никогда' ___ рабо'тает в воскресе'нье.", ["не", "нет", "ни", "и"], "не",
           "Никогда' needs не.", tr="He never works on Sunday."),
        fb("Мой дя'дя рабо'тает в ___.", ["саду'", "са'де", "сад", "сада'"], "саду'",
           "Place: stressed -у'.", tr="My uncle works in the garden."),
        mc("Which is correct?", ["Я говорю' о нём.", "Я говорю' о него'.", "Я говорю' о он.", "Я говорю' о ему'."],
           "Я говорю' о нём.", "Prepositional of он: нём."),
        mc("Which sentence is right?", ["Это така'я краси'вая маши'на!", "Это так краси'вая маши'на!", "Это тако'й краси'вая маши'на!", "Это таки'е краси'вая маши'на!"],
           "Это така'я краси'вая маши'на!", "Тако'й agrees with the noun."),
        mc("Which means “How do I get to the station?”",
           ["Как попа'сть на вокза'л?", "Как попа'сть в вокза'л?", "Где попа'сть вокза'л?", "Куда' нахо'дится вокза'л?"],
           "Как попа'сть на вокза'л?", "Вокза'л takes на, with the accusative."),
    ],
)

UNIT = unit("Unit 8: Getting around town", [L50, L51, L52, L53, L54, L55, L56, L57])
