"""Unit 7: habits, walking, having and liking  (textbook module 2, lesson 11)."""
from dsl import *

# ---------------------------------------------------------------------------- 42
L42 = lesson(
    "How often? Always, sometimes, every day",
    "Всегда', иногда', ка'ждый день",
    requires=["каждый", "обычно", "иногда", "всегда", "часто"],
    cards=[
        card("Words for how often",
             "Russian puts these small adverbs right before the verb, and they never change. Remember "
             "that никогда' (never) needs не before the verb as well: Я никогда' не рабо'таю там.",
             tables=[table(
                 ["Always → never", "Meaning", "Example"],
                 [["всегда'", "always", "Он всегда' до'ма ве'чером."],
                  ["обы'чно", "usually", "Мы обы'чно чита'ем."],
                  ["ча'сто", "often", "Я ча'сто гуля'ю в па'рке."],
                  ["иногда'", "sometimes", "Иногда' она' пи'шет письмо'."],
                  ["ре'дко", "seldom", "Они' ре'дко ви'дят друзе'й."],
                  ["никогда' не", "never", "Я никогда' не курю'."]])]),
        card("Every day, every Saturday",
             "To say “every” plus a time word, use ка'ждый, which agrees with the time word, and put both in the "
             "accusative. Masculine and neuter time words do not change; feminine ones end in -ую and -у or -ю. "
             "You already know the accusative, so there is nothing new to learn.",
             tables=[table(
                 ["Time word", "Every …"],
                 [["день", "ка'ждый день"],
                  ["ве'чер", "ка'ждый ве'чер"],
                  ["у'тро", "ка'ждое у'тро"],
                  ["неде'ля", "ка'ждую неде'лю"],
                  ["суббо'та", "ка'ждую суббо'ту"],
                  ["воскресе'нье", "ка'ждое воскресе'нье"]])],
             examples=[
                 ex("Ка'ждую суббо'ту я пишу' письмо'.", "Every Saturday I write a letter.", "Ка'ждую суббо'ту"),
                 ex("Ка'ждый день он чита'ет газе'ту.", "Every day he reads the newspaper.", "Ка'ждый день"),
                 ex("Ка'ждое у'тро мы гуля'ем в па'рке.", "Every morning we walk in the park.", "Ка'ждое у'тро"),
             ]),
    ],
    verify=vf("каждый", "каждую", "каждое") + vf("неделя", "неделю") + vf("суббота", "субботу"),
    exercises=[
        fb("Она' ___ чита'ет: ка'ждый день и ка'ждый ве'чер.", ["всегда'", "никогда'", "ре'дко", "иногда'"], "всегда'",
           "Every day and every evening means always.", tr="She always reads: every day and every evening."),
        fb("Ка'ждую ___ я до'ма.", ["суббо'ту", "суббо'та", "суббо'ты", "суббо'те"], "суббо'ту",
           "A feminine time word after ка'ждую is accusative: -а becomes -у.", tr="Every Saturday I'm at home.", lemma="суббота"),
        fb("Ка'ждый ___ мы чита'ем.", ["день", "дня", "дню", "дне"], "день",
           "A masculine time word does not change in the accusative.", tr="Every day we read."),
        fb("Ка'ждое ___ он гуля'ет в па'рке.", ["у'тро", "у'тра", "у'тру", "у'тром"], "у'тро",
           "A neuter word does not change in the accusative.", tr="Every morning he walks in the park."),
        fb("Ка'ждую ___ мы пи'шем письмо'.", ["неде'лю", "неде'ля", "неде'ли", "неде'ле"], "неде'лю",
           "Feminine in -я: -я becomes -ю.", tr="Every week we write a letter.", lemma="неделя"),
        fb("Я никогда' ___ курю'.", ["не", "нет", "ни", "и"], "не",
           "Никогда' always comes with не before the verb.", tr="I never smoke."),
        mc("Which word means “sometimes”?", ["иногда'", "всегда'", "ре'дко", "никогда'"], "иногда'",
           "Иногда' = sometimes."),
        mc("Which adverb is the most frequent?", ["всегда'", "иногда'", "ре'дко", "ча'сто"], "всегда'",
           "Всегда' means every time."),
        mc("How do you say “every Sunday”?",
           ["ка'ждое воскресе'нье", "ка'ждая воскресе'нье", "ка'ждый воскресе'нье", "ка'ждую воскресе'нье"],
           "ка'ждое воскресе'нье", "Воскресе'нье is neuter, so ка'ждое, and neuter nouns don't change in the accusative."),
        mc("How do you say “every Friday”?",
           ["ка'ждую пя'тницу", "ка'ждая пя'тница", "ка'ждый пя'тницу", "ка'ждую пя'тница"],
           "ка'ждую пя'тницу", "Feminine: ка'ждую and -у."),
    ],
)

# ---------------------------------------------------------------------------- 43
L43 = lesson(
    "Two verbs for walking: идти' and ходи'ть",
    "Иду' сейча'с, хожу' ка'ждый день",
    requires=["ходить", "идти", "парк", "магазин", "кино"],
    cards=[
        card("One way now, or back and forth",
             "Russian has two verbs for going on foot. Идти' is for one trip in one direction: you are on your way "
             "somewhere right now, or you have a destination in mind. Ходи'ть is for everything else: habits "
             "and repeated trips, going and coming back, general ability, and walking around with no particular "
             "direction. Words like ка'ждый день, обы'чно and ча'сто point to ходи'ть. Words like сейча'с and the "
             "question Куда'? point to идти'.",
             tables=[table(
                 ["", "Идти'", "Ходи'ть"],
                 [["Direction", "one way, to a destination", "back and forth, or in general"],
                  ["Clue words", "сейча'с, вот, куда'?", "ка'ждый день, ча'сто, обы'чно"],
                  ["Example", "Я иду' в магази'н.", "Я хожу' в магази'н ка'ждый день."]])]),
        card("Ходи'ть: forms and the past",
             "Ходи'ть is a second-family verb with the я-form change you met in lesson 24 (д becomes ж). In the "
             "past, ходи'л в парк means “went to the park (and came back)”, so it can replace был: "
             "Вчера' я ходи'л в парк = Вчера' я был в па'рке. For commands, ходи'ть is the usual verb for a "
             "negative command (Не ходи'!), and идти' for a positive one (Иди'!).",
             tables=[table(
                 ["Person", "Present", "Past"],
                 [["я", "хож{у'}", "я ходи'л · ходи'ла"],
                  ["ты", "хо'д{ишь}", "ты ходи'л · ходи'ла"],
                  ["он · она' · оно'", "хо'д{ит}", "ходи'л · ходи'ла · ходи'ло"],
                  ["мы", "хо'д{им}", "мы ходи'ли"],
                  ["вы", "хо'д{ите}", "вы ходи'ли"],
                  ["они'", "хо'д{ят}", "они' ходи'ли"]])],
             examples=[
                 ex("Ка'ждый день мы хо'дим в парк.", "Every day we go to the park.", "хо'дим"),
                 ex("Куда' ты идёшь?", "Where are you going (now)?", "идёшь"),
                 ex("Не ходи' сего'дня в магази'н.", "Don't go to the store today.", "Не ходи'"),
                 ex("Иди' домо'й!", "Go home!", "Иди'"),
                 ex("Идёт дождь.", "It's raining. (always идти')", "Идёт"),
             ]),
    ],
    verify=vf("ходить", "хожу", "ходишь", "ходит", "ходим", "ходите", "ходят", "ходил", "ходила", "ходили", "ходи"),
    exercises=[
        fb("Ка'ждый день я ___ в парк.", ["хожу'", "иду'", "хо'дит", "идёт"], "хожу'",
           "Every day = a habit, so ходи'ть.", tr="Every day I go to the park.", lemma="ходить"),
        fb("Сейча'с я ___ в магази'н.", ["иду'", "хожу'", "ходи'л", "шёл"], "иду'",
           "Сейча'с = right now, one direction: идти'.", tr="Right now I'm going to the store."),
        fb("Мы ча'сто ___ в кино'.", ["хо'дим", "идём", "идёте", "хо'дишь"], "хо'дим",
           "Ча'сто = repeated trips: ходи'ть.", tr="We often go to the movies.", lemma="ходить"),
        fb("Куда' ты ___ сейча'с?", ["идёшь", "хо'дишь", "ходи'л", "шёл"], "идёшь",
           "Right now, to a destination: идти'.", tr="Where are you going right now?"),
        fb("Я люблю' ___ бы'стро.", ["ходи'ть", "идёт", "иду'", "хожу'"], "ходи'ть",
           "A general activity (no particular trip): ходи'ть. After люблю' use the infinitive.", tr="I like to walk fast."),
        fb("Не ___ сего'дня в магази'н!", ["ходи'", "иди'", "иду'", "хожу'"], "ходи'",
           "A negative command normally uses ходи'ть.", tr="Don't go to the store today!"),
        fb("___ домо'й!", ["Иди'", "Ходи'", "Хожу'", "Ходи'ть"], "Иди'",
           "A positive command normally uses идти'.", tr="Go home!"),
        mc("Which sentence means “Yesterday I went to the institute (and came back)”?",
           ["Вчера' я ходи'л в институ'т.", "Вчера' я шёл в институ'т.", "Вчера' я иду' в институ'т.", "Вчера' я хожу' в институ'т."],
           "Вчера' я ходи'л в институ'т.", "Past ходи'л = a completed round trip, like был."),
        mc("Which verb is always used for “It's raining”?", ["идти'", "ходи'ть", "е'хать", "бежа'ть"], "идти'",
           "Идёт дождь, идёт снег, идёт уро'к: always идти'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 44
L44 = lesson(
    "Talking about: о and об",
    "Я ду'маю о рабо'те, Мы говори'м об учи'теле",
    requires=["думать", "рассказывать", "разговаривать", "семья", "работа"],
    cards=[
        card("О + the prepositional case",
             "The preposition о (about, of) always takes the prepositional case. It comes after verbs of "
             "thinking and talking: ду'мать, говори'ть, расска'зывать (to tell), разгова'ривать (to chat), "
             "чита'ть (to read about). The questions are О чём? (about what?) and О ком? (about whom?). "
             "Remember that the prepositional ends in -е for most nouns.",
             tables=[table(
                 ["Nominative", "О + prepositional"],
                 [["рабо'та", "о рабо'т{е}"],
                  ["семья'", "о семь{е'}"],
                  ["брат", "о бра'т{е}"],
                  ["шко'ла", "о шко'л{е}"],
                  ["мать", "о ма'тер{и}"]])],
             examples=[
                 ex("О чём вы ду'маете? — Я ду'маю о рабо'те.", "What are you thinking about? — I'm thinking about work.", "о рабо'те"),
                 ex("Он расска'зывает о семье'.", "He tells about his family.", "о семье'"),
             ]),
        card("Before a vowel, об",
             "When the next word starts with а, и, о, у or э, о becomes об, to keep the vowels apart. You say "
             "об учи'теле, об отце', об э'той кни'ге, об а'вгусте. Before consonants it stays о: о ком, о бра'те. "
             "Never use об before a consonant.",
             examples=[
                 ex("О ком вы говори'те? — Мы говори'м об учи'теле.", "Whom are you talking about? — We're talking about the teacher.", "об учи'теле"),
                 ex("Я чита'ю об э'той кни'ге.", "I'm reading about this book.", "об э'той"),
                 ex("Они' разгова'ривают об отце'.", "They're chatting about [their] father.", "об отце'"),
             ]),
    ],
    verify=vf("работа", "работе") + vf("семья", "семье") + vf("брат", "брате") + vf("школа", "школе")
           + vf("мать", "матери") + vf("учитель", "учителе") + vf("отец", "отце"),
    exercises=[
        fb("Я ду'маю о ___.", ["рабо'те", "рабо'та", "рабо'ту", "рабо'ты"], "рабо'те",
           "After о the noun is prepositional: -а becomes -е.", tr="I'm thinking about work.", lemma="работа"),
        fb("Мы говори'м о ___.", ["бра'те", "брат", "бра'та", "бра'ту"], "бра'те",
           "Prepositional: брат → бра'те.", tr="We're talking about [my] brother.", lemma="брат"),
        fb("Она' расска'зывает о ___.", ["семье'", "семья'", "семью'", "семьи'"], "семье'",
           "Prepositional: семья' → семье'.", tr="She tells about her family.", lemma="семья"),
        fb("Он говори'т ___ учи'теле.", ["об", "о", "на", "в"], "об",
           "Учи'теле starts with у, so о becomes об.", tr="He's talking about the teacher."),
        fb("Они' говоря'т ___ отце'.", ["об", "о", "на", "в"], "об",
           "Отце' starts with о, so об.", tr="They're talking about [their] father."),
        fb("Мы чита'ем ___ э'той кни'ге.", ["об", "о", "на", "в"], "об",
           "Э'той starts with э, so об.", tr="We're reading about this book."),
        fb("О ___ вы ду'маете?", ["чём", "что", "чего'", "чем"], "чём",
           "О чём? = about what?", tr="What are you thinking about?"),
        fb("___ ком вы говори'те?", ["О", "Об", "На", "К"], "О",
           "Ком starts with к, a consonant: о.", tr="Whom are you talking about?"),
        mc("Which case follows о in the meaning “about”?", ["prepositional", "accusative", "nominative", "none"], "prepositional",
           "О always takes the prepositional.", order=True),
        mc("When does о become об?", ["Before а, и, о, у, э", "Before every noun", "Before б", "Never"], "Before а, и, о, у, э",
           "To avoid two vowels in a row.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 45
L45 = lesson(
    "There is, there are: е'сть",
    "В го'роде есть река'",
    requires=["есть", "город", "улица", "телефон", "гостиница"],
    cards=[
        card("Saying something exists",
             "To say that something exists or is available somewhere, put the place first, then есть, then the "
             "thing. Есть never changes (it stands for both is and are), and the thing that follows is in the "
             "nominative, singular or plural. The sentence works like a map: place, then what is in it.",
             tables=[table(
                 ["Place", "", "Thing"],
                 [["В го'роде", "{есть}", "река'."],
                  ["На на'шей у'лице", "{есть}", "гости'ница."],
                  ["В ко'мнате", "{есть}", "стол и стул."],
                  ["Здесь", "{есть}", "телефо'н."]])],
             examples=[
                 ex("Здесь есть телефо'н?", "Is there a telephone here?", "есть"),
                 ex("Да, есть.", "Yes, there is.", "есть"),
                 ex("На у'лице есть больши'е магази'ны.", "There are big stores on the street.", "есть"),
             ]),
        card("Есть or где?",
             "Use есть to introduce something that may or may not be there: В го'роде есть мост. Use Где? and вот "
             "when you already know the thing and are asking about its location: Где мой телефо'н? — Вот он. "
             "For the past tense you use был, была', бы'ло, бы'ли instead of есть, as in lesson 19.",
             examples=[
                 ex("Где мой телефо'н? — Вот он.", "Where is my phone? — Here it is.", "Вот"),
                 ex("В го'роде был мост.", "There was a bridge in the city.", "был"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("В го'роде ___ рынок.", ["есть", "нет", "ты", "мы"], "есть",
           "Place + есть + thing.", tr="There is a market in the city."),
        fb("На у'лице ___ гости'ница.", ["есть", "нет", "он", "вы"], "есть",
           "Есть introduces what exists there.", tr="There's a hotel on the street."),
        fb("В ко'мнате есть стол и ___.", ["стул", "сту'ла", "сту'лу", "сту'ле"], "стул",
           "The thing after есть is nominative.", tr="There's a table and a chair in the room."),
        fb("На у'лице есть больши'е ___.", ["магази'ны", "магази'нов", "магази'нам", "магази'нах"], "магази'ны",
           "Nominative plural.", tr="There are big stores on the street."),
        fb("Где мой телефо'н? — ___ он!", ["Вот", "Есть", "Нет", "Тут есть"], "Вот",
           "To point at something you already know about, use вот.", tr="Where's my phone? — Here it is!"),
        mc("Which sentence means “There is a bridge in our city”?",
           ["В на'шем го'роде есть мост.", "На'ш город есть мост.", "Мост на'ш город есть.", "В на'шем го'роде мост нет."],
           "В на'шем го'роде есть мост.", "Place first, then есть, then the thing."),
        mc("How do you answer “Is there a hotel here?” briefly and positively?",
           ["Да, есть.", "Да, я.", "Да, бы'ло.", "Да, гости'ница."], "Да, есть.", "Repeat есть."),
        mc("In what case is the noun after есть?", ["nominative", "accusative", "prepositional", "dative"], "nominative",
           "В ко'мнате есть стол: стол is nominative.", order=True),
        mc("How do you say “There was a bridge in the city”?",
           ["В го'роде был мост.", "В го'роде есть мост.", "В го'роде была мост.", "В го'роде бы'ло мост."],
           "В го'роде был мост.", "In the past, быть agrees with the thing: мост is masculine."),
    ],
)

# ---------------------------------------------------------------------------- 46
L46 = lesson(
    "I have: у меня' есть",
    "У меня' есть брат, у неё есть маши'на",
    requires=["брат", "сестра", "семья", "машина", "дом"],
    cards=[
        card("“At me there is”",
             "Russian has no verb “to have” for owning things. It says “at me there is”: у меня' есть. The person "
             "goes after у in a special form, and the thing you have is in the nominative. These forms look "
             "like the accusative pronouns you know, and the same rule adds a н when a preposition comes "
             "before его', её or их.",
             tables=[table(
                 ["Who", "At …", "Example"],
                 [["я", "у меня'", "У меня' есть брат."],
                  ["ты", "у тебя'", "У тебя' есть маши'на?"],
                  ["он · оно'", "у {н}его'", "У него' есть дом."],
                  ["она'", "у {н}её", "У неё есть сестра'."],
                  ["мы", "у нас", "У нас есть семья'."],
                  ["вы", "у вас", "У вас есть де'ти?"],
                  ["они'", "у {н}их", "У них есть соба'ка."]])]),
        card("When есть is left out",
             "Use есть when the point is that you have something at all. If the sentence mostly describes the "
             "thing (a new car, a big family), есть is dropped and the description comes first: У него' "
             "но'вая маши'на. У нас больша'я семья'. In the past, use был, была', бы'ло, бы'ли, which agree "
             "with the thing you had.",
             examples=[
                 ex("У меня' есть маши'на.", "I have a car. (the fact of having one)", "есть"),
                 ex("У меня' но'вая маши'на.", "I have a new car. (describing it)", "но'вая"),
                 ex("У неё больша'я семья'.", "She has a big family.", "больша'я"),
                 ex("У нас была' маши'на.", "We had a car.", "была'"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("У ___ есть брат.", ["меня'", "я", "мне", "мной"], "меня'",
           "At me: у меня'.", tr="I have a brother."),
        fb("У ___ есть маши'на?", ["тебя'", "ты", "тебе'", "тобо'й"], "тебя'",
           "At you: у тебя'.", tr="Do you have a car?"),
        fb("У ___ есть сестра'.", ["него'", "его'", "он", "ему'"], "него'",
           "After the preposition у, его' becomes него'.", tr="He has a sister."),
        fb("У ___ есть семья'.", ["неё", "её", "она'", "ей"], "неё",
           "After у, её becomes неё.", tr="She has a family."),
        fb("У ___ есть дом.", ["нас", "мы", "нам", "на'ми"], "нас",
           "At us: у нас.", tr="We have a house."),
        fb("У ___ есть де'ти.", ["них", "их", "они'", "им"], "них",
           "After у, их becomes них.", tr="They have children."),
        fb("У меня' больша'я ___.", ["семья'", "семью'", "семьи'", "семье'"], "семья'",
           "The thing you have stays nominative.", tr="I have a big family.", lemma="семья"),
        fb("У нас ___ маши'на.", ["была'", "был", "бы'ло", "бы'ли"], "была'",
           "Маши'на is feminine.", tr="We had a car."),
        mc("Why is there no есть in “У него' но'вая маши'на”?",
           ["The sentence describes the car, not the fact of having one", "It is a mistake", "Because it is past tense", "Because но'вая is feminine"],
           "The sentence describes the car, not the fact of having one", "You can drop есть when the focus is a description.", order=True),
        mc("How do you ask a polite “Do you have a family?”",
           ["У вас есть семья'?", "У вы есть семья'?", "Вы есть семья'?", "У вам есть семья'?"],
           "У вас есть семья'?", "At you (polite): у вас."),
    ],
)

# ---------------------------------------------------------------------------- 47
L47 = lesson(
    "Liking things: мне нра'вится",
    "Мне нра'вится го'род, мне нра'вятся фи'льмы",
    requires=["нравиться", "любить", "город", "фильм", "платье"],
    cards=[
        card("The thing pleases you",
             "Russian does not say “I like the city”. It says “the city is pleasing to me”: Мне нра'вится го'род. The "
             "person is in a special form (мне, тебе', ему', ей, нам, вам, им), the thing liked is the subject, "
             "and the verb agrees with it: нра'вится for one thing or an activity, нра'вятся for several. After "
             "нра'вится you can also use an infinitive.",
             tables=[table(
                 ["Who", "To …", "Example"],
                 [["я", "{мне}", "Мне нра'вится э'тот го'род."],
                  ["ты", "{тебе'}", "Тебе' нра'вятся э'ти фи'льмы?"],
                  ["он", "{ему'}", "Ему' нра'вится гуля'ть."],
                  ["она'", "{ей}", "Ей нра'вится ва'ше пла'тье."],
                  ["мы", "{нам}", "Нам нра'вятся э'ти кни'ги."],
                  ["вы", "{вам}", "Вам нра'вится здесь?"],
                  ["они'", "{им}", "Им не нра'вится рабо'та."]])]),
        card("Нра'виться or люби'ть?",
             "Нра'виться is a lighter feeling: a preference, a taste, a first impression, or a compliment. Люби'ть is "
             "for deep, lasting feelings: family, your country, a long-time favourite. To compliment someone's "
             "dress say Мне нра'вится ва'ше пла'тье!, not Я люблю' ва'ше пла'тье. When you see a film for the first "
             "time and enjoy it, you say Мне понра'вился э'тот фильм, using the past tense and the "
             "perfective verb понра'виться.",
             examples=[
                 ex("Я люблю' мою' семью'.", "I love my family.", "люблю'"),
                 ex("Мне нра'вится э'тот фильм.", "I like this film.", "нра'вится"),
                 ex("Мне о'чень понра'вился э'тот фильм.", "I really liked this film.", "понра'вился"),
             ]),
    ],
    verify=vf("нравиться", "нравится", "нравятся") + vf("понравиться", "понравился"),
    exercises=[
        fb("___ нра'вится э'тот го'род.", ["Мне", "Я", "Меня'", "Мной"], "Мне",
           "The person who likes is in the form мне.", tr="I like this city."),
        fb("Ей ___ э'та кни'га.", ["нра'вится", "нра'вятся", "нра'вишься", "нра'влюсь"], "нра'вится",
           "One thing: нра'вится.", tr="She likes this book."),
        fb("Нам ___ но'вые фи'льмы.", ["нра'вятся", "нра'вится", "нра'вишься", "нра'вимся"], "нра'вятся",
           "Plural things: нра'вятся.", tr="We like new films."),
        fb("Мне нра'вится ___ в па'рке.", ["гуля'ть", "гуля'ю", "гуля'л", "гуля'ет"], "гуля'ть",
           "After нра'вится an infinitive.", tr="I like walking in the park."),
        fb("___ нра'вится э'тот фильм? (ты)", ["Тебе'", "Ты", "Тебя'", "Тобо'й"], "Тебе'",
           "To you: тебе'.", tr="Do you like this film?"),
        fb("Им ___ э'тот го'род.", ["нра'вится", "нра'вятся", "нра'вишься", "нра'вимся"], "нра'вится",
           "Го'род is one thing.", tr="They like this city."),
        mc("Which sentence means “I like these books”?",
           ["Мне нра'вятся э'ти кни'ги.", "Мне нра'вится э'ти кни'ги.", "Я нра'вятся э'ти кни'ги.", "Меня' нра'вятся э'ти кни'ги."],
           "Мне нра'вятся э'ти кни'ги.", "Plural subject: нра'вятся."),
        mc("What is the grammatical subject in “Мне нра'вится го'род”?", ["го'род", "мне", "нра'вится", "no subject"], "го'род",
           "The thing liked is the subject; it is in the nominative.", order=True),
        mc("Which sentence is the natural compliment about a dress?",
           ["Мне нра'вится ва'ше пла'тье!", "Я люблю' ва'ше пла'тье!", "Я нра'влюсь ва'ше пла'тье!", "Вам нра'вится я!"],
           "Мне нра'вится ва'ше пла'тье!", "Use нра'виться for taste and compliments."),
        mc("Which sentence expresses a deep, long-held feeling?",
           ["Я люблю' мою' семью'.", "Мне нра'вится моя' семья'.", "Мне понра'вилась моя' семья'.", "Я нра'влюсь моей семье'."],
           "Я люблю' мою' семью'.", "Deep, lasting feeling: люби'ть."),
    ],
)

# ---------------------------------------------------------------------------- 48
L48 = lesson(
    "Both of us: о'ба, о'бе; и … и …, ни … ни …",
    "Мы о'ба студе'нты, они' о'бе врачи'",
    requires=["вместе", "друг", "сестра", "брат", "врач"],
    cards=[
        card("О'ба or о'бе",
             "О'ба and о'бе mean “both”. They have two forms: о'бе for two women (or two feminine nouns) and о'ба "
             "for everything else: two men, or a man and a woman together. In the plural pronouns they follow "
             "the pronoun.",
             tables=[table(
                 ["Who", "Two women", "Anything else"],
                 [["мы", "мы {о'бе}", "мы {о'ба}"],
                  ["вы", "вы {о'бе}", "вы {о'ба}"],
                  ["они'", "они' {о'бе}", "они' {о'ба}"]],
                 note="“Anything else” = two men, or a man and a woman.")],
             examples=[
                 ex("Я студе'нт, и мой друг студе'нт. Мы о'ба студе'нты.", "I'm a student and my friend is a student. We are both students.", "о'ба"),
                 ex("Ма'ма и сестра' — врачи'. Они' о'бе врачи'.", "Mom and my sister are doctors. They are both doctors.", "о'бе"),
                 ex("Муж и жена' до'ма. Они' о'ба до'ма.", "The husband and wife are at home. They are both at home.", "о'ба"),
             ]),
        card("Both … and, neither … nor",
             "To translate “both A and B”, do not use о'ба: say и … и …. “Neither A nor B” is ни … ни …, and the "
             "verb must still be negated with не.",
             examples=[
                 ex("И мой брат, и его' друг — студе'нты.", "Both my brother and his friend are students.", "И мой брат, и"),
                 ex("Ни она', ни её сестра' не иду'т в кино'.", "Neither she nor her sister is going to the movies.", "Ни она', ни"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("Мой брат и я — студе'нты. Мы ___ студе'нты.", ["о'ба", "о'бе", "ни", "и"], "о'ба",
           "Two men: о'ба.", tr="My brother and I are students. We are both students."),
        fb("Ма'ма и сестра' — врачи'. Они' ___ врачи'.", ["о'бе", "о'ба", "ни", "и"], "о'бе",
           "Two women: о'бе.", tr="Mom and my sister are doctors. They are both doctors."),
        fb("Па'па и ма'ма до'ма. Они' ___ до'ма.", ["о'ба", "о'бе", "ни", "и"], "о'ба",
           "A man and a woman: о'ба.", tr="Dad and mom are at home. They are both at home."),
        fb("Вы ___ мои' подру'ги. (to two women)", ["о'бе", "о'ба", "ни", "и"], "о'бе",
           "Two women: о'бе.", tr="You are both my friends."),
        fb("___ мой брат, и его' друг — студе'нты.", ["И", "Ни", "О'ба", "О'бе"], "И",
           "Both … and is и … и …, not о'ба.", tr="Both my brother and his friend are students."),
        fb("Ни она', ни её сестра' ___ иду'т в кино'.", ["не", "нет", "ни", "и"], "не",
           "After ни … ни … the verb takes не.", tr="Neither she nor her sister is going to the movies."),
        mc("Which word do you use for two women?", ["о'бе", "о'ба", "и", "ни"], "о'бе",
           "О'бе is the feminine form.", order=True),
        mc("What happens to the verb after ни … ни …?",
           ["It must be negated with не", "Nothing", "It becomes past", "It is dropped"], "It must be negated with не",
           "Russian uses a double negative.", order=True),
        mc("A man and his wife are doctors. “They are both doctors.” Which is right?",
           ["Они' о'ба врачи'.", "Они' о'бе врачи'.", "Они' и врачи'.", "Они' ни врачи'."],
           "Они' о'ба врачи'.", "A mixed pair takes о'ба."),
    ],
)

# ---------------------------------------------------------------------------- 49
L49 = lesson(
    "Such and so: тако'й and так",
    "Тако'й интере'сный фильм! Он так бы'стро чита'ет.",
    requires=["такой", "так", "красивый", "интересный", "плохой"],
    cards=[
        card("Two words, two jobs",
             "Both words mean “so” or “such”, but they attach to different things. Тако'й is an adjective: it goes "
             "with a noun, or with an adjective that describes one, and it agrees with the noun in gender, "
             "number and case (тако'й, така'я, тако'е, таки'е). Так is an adverb: it goes with a verb or another "
             "adverb and never changes.",
             tables=[table(
                 ["", "Goes with", "Example"],
                 [["{тако'й · така'я · тако'е · таки'е}", "a noun, or adjective + noun", "Э'то така'я интере'сная кни'га."],
                  ["{так}", "a verb or an adverb", "Он так бы'стро чита'ет."]])],
             examples=[
                 ex("Ва'ша маши'на така'я краси'вая!", "Your car is so beautiful!", "така'я"),
                 ex("У меня' уже' есть така'я кни'га.", "I already have such a book.", "така'я"),
                 ex("Здесь так краси'во.", "It's so beautiful here.", "так"),
                 ex("Он так пло'хо говори'т по-англи'йски.", "He speaks English so badly.", "так"),
             ]),
    ],
    verify=vf("такой", "такая", "такое", "такие"),
    exercises=[
        fb("Э'то ___ интере'сная кни'га.", ["така'я", "так", "тако'й", "таки'е"], "така'я",
           "Кни'га is feminine: така'я.", tr="This is such an interesting book."),
        fb("Он ___ бы'стро чита'ет.", ["так", "тако'й", "така'я", "тако'е"], "так",
           "Describing a verb: так.", tr="He reads so fast."),
        fb("Здесь ___ краси'во.", ["так", "тако'й", "така'я", "тако'е"], "так",
           "Краси'во is an adverb, so так.", tr="It's so beautiful here."),
        fb("Э'то ___ большо'й дом!", ["тако'й", "так", "така'я", "тако'е"], "тако'й",
           "Дом is masculine.", tr="This is such a big house!"),
        fb("У меня' уже' есть ___ маши'на.", ["така'я", "так", "тако'й", "таки'е"], "така'я",
           "Маши'на is feminine.", tr="I already have such a car."),
        fb("Ва'ши кни'ги ___ интере'сные!", ["таки'е", "так", "тако'й", "така'я"], "таки'е",
           "Plural: таки'е.", tr="Your books are so interesting!"),
        mc("Which word modifies a verb or an adverb?", ["так", "тако'й", "така'я", "таки'е"], "так",
           "Так never changes.", order=True),
        mc("Which sentence is correct?",
           ["Она' так хорошо' говори'т.", "Она' тако'й хорошо' говори'т.", "Она' така'я хорошо' говори'т.", "Она' таки'е хорошо' говори'т."],
           "Она' так хорошо' говори'т.", "Хорошо' is an adverb: так."),
        mc("What does тако'й agree with?",
           ["The noun it goes with", "The verb", "Nothing", "The subject always"], "The noun it goes with",
           "Gender, number and case of the noun.", order=True),
    ],
)

UNIT = unit("Unit 7: Habits, walking, having and liking", [L42, L43, L44, L45, L46, L47, L48, L49])
