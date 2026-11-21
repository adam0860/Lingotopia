"""Unit 12: aspect in more detail, and shopping for food
(textbook module 3, lesson 17)."""
from dsl import *

# ---------------------------------------------------------------------------- 84
L84 = lesson(
    "What did you do? Did you finish?",
    "Что ты де'лал? Ты уже' написа'л?",
    requires=["писать", "написать", "читать", "прочитать", "письмо"],
    cards=[
        card("The question picks the aspect",
             "You can usually tell which aspect to use from the question. If you ask what someone did, how long "
             "it took or whether they spent time on it, you only want to know about the activity, so the "
             "imperfective is used and the result does not matter. If you ask whether something is finished, "
             "when it will be finished, or want to see the result, the perfective is used.",
             tables=[table(
                 ["Question", "Aspect", "Answer"],
                 [["Что ты де'лал вчера' ве'чером?", "imperfective", "Я писа'л пи'сьма."],
                  ["Как до'лго ты писа'л?", "imperfective", "Весь ве'чер."],
                  ["Ты уже' написа'л письмо'?", "perfective", "Да, написа'л."],
                  ["Когда' ты уже' напи'шешь письмо'?", "perfective", "За'втра."]])]),
        card("Two ways to say the same day",
             "The choice depends on what you want to stress. Compare the sentences below. In the first, the speaker "
             "lists what was accomplished. In the second, the speaker lists what was done, and we do not know "
             "whether anything was finished. A short answer to a question about the activity repeats the "
             "imperfective, and the answer to a question about completion uses the perfective.",
             examples=[
                 ex("Сего'дня я сде'лала дома'шнюю рабо'ту, пригото'вила у'жин и убрала' ко'мнату.",
                    "Today I did my homework, cooked dinner and cleaned my room. (all done)", "сде'лала"),
                 ex("Сего'дня я де'лала дома'шнюю рабо'ту, гото'вила у'жин и убира'ла ко'мнату.",
                    "Today I was doing homework, cooking dinner and cleaning my room. (the activities)", "де'лала"),
                 ex("— Ты чита'л э'ту кни'гу? — Да, чита'л.", "— Did you read this book? — Yes, I did.", "чита'л"),
                 ex("— Ты её прочита'л? — Нет, пока' не прочита'л.", "— Did you finish it? — No, not yet.", "прочита'л"),
             ]),
    ],
    verify=(vf("писать", "писал") + vf("написать", "написал", "напишешь") + vf("читать", "читал")
            + vf("прочитать", "прочитал") + vf("делать", "делала", "делал") + vf("сделать", "сделала")
            + vf("готовить", "готовила") + vf("приготовить", "приготовила") + vf("убирать", "убирала")
            + vf("убрать", "убрала")),
    exercises=[
        fb("Что ты ___ вчера' ве'чером?", ["де'лал", "сде'лал"], "де'лал",
           "Asking what the activity was: imperfective.", tr="What did you do yesterday evening?"),
        fb("Как до'лго ты ___ письмо'?", ["писа'л", "написа'л"], "писа'л",
           "Как до'лго asks about duration: imperfective.", tr="How long did you write the letter?"),
        fb("Ты уже' ___ письмо'?", ["написа'л", "писа'л"], "написа'л",
           "Уже' asks about completion: perfective.", tr="Have you already written the letter?"),
        fb("Когда' ты уже' ___ письмо'?", ["напи'шешь", "бу'дешь писа'ть"], "напи'шешь",
           "Asking when it will be done: perfective.", tr="When will you finally write the letter?"),
        fb("— Ты её прочита'л? — Нет, пока' не ___.", ["прочита'л", "чита'л"], "прочита'л",
           "Not finished yet: perfective.", tr="— Did you finish it? — No, not yet."),
        fb("Вчера' я весь ве'чер ___ пи'сьма.", ["писа'л", "написа'л"], "писа'л",
           "Весь ве'чер shows duration: imperfective.", tr="Yesterday I wrote letters all evening."),
        fb("Сего'дня я ___ дома'шнюю рабо'ту, пригото'вила у'жин и убрала' ко'мнату.", ["сде'лала", "де'лала"], "сде'лала",
           "A list of accomplished results: perfective.", tr="Today I did my homework, cooked dinner and cleaned my room."),
        mc("Which question asks whether it is finished?",
           ["Ты уже' написа'л письмо'?", "Что ты де'лал вчера'?", "Как до'лго ты писа'л?", "Что ты писа'л?"],
           "Ты уже' написа'л письмо'?", "Уже' + perfective asks about completion."),
        mc("Which aspect follows Как до'лго …?", ["imperfective", "perfective", "both", "neither"], "imperfective",
           "Duration goes with the imperfective.", order=True),
        mc("Which sentence only says she did these activities, without saying they are finished?",
           ["Сего'дня я де'лала дома'шнюю рабо'ту.", "Сего'дня я сде'лала дома'шнюю рабо'ту.",
            "Сего'дня я сде'лаю дома'шнюю рабо'ту.", "Сего'дня я бу'ду де'лать дома'шнюю рабо'ту."],
           "Сего'дня я де'лала дома'шнюю рабо'ту.", "The imperfective names the activity."),
    ],
)

# ---------------------------------------------------------------------------- 85
L85 = lesson(
    "Aspect in the infinitive: хочу' есть or хочу' съесть?",
    "Я начина'ю чита'ть, я хочу' прочита'ть",
    requires=["хотеть", "мочь", "начинать", "любить", "уметь"],
    cards=[
        card("Which aspect after a helper verb?",
             "An infinitive takes its aspect from the word in front of it. After verbs of beginning, ending, "
             "learning, liking and knowing how, always use the imperfective: начина'ть, зака'нчивать, учи'ться, "
             "люби'ть, уме'ть. After verbs of wanting, being able and having to do something once, use the "
             "imperfective for the activity in general or the perfective for completing it.",
             tables=[table(
                 ["Imperfective infinitive", "Perfective infinitive"],
                 [["Я начина'ю чита'ть кни'гу.", "Я хочу' прочита'ть э'ту кни'гу."],
                  ["Я зака'нчиваю писа'ть письмо'.", "Я могу' сде'лать э'то сего'дня."],
                  ["Я учу'сь пла'вать.", "Ты до'лжен прочита'ть э'ту кни'гу."],
                  ["Я люблю' игра'ть на гита'ре.", "Мне на'до написа'ть письмо'."],
                  ["Я хочу' есть. (I'm hungry)", "Я хочу' съесть кусо'чек. (a piece)"]],
                 note="До'лжен changes by gender: до'лжен, должна', должно', должны'.")]),
        card("Permitted, forbidden, impossible",
             "With мо'жно and нельзя' the aspect shows what you mean. The imperfective is for a general rule: "
             "В э'той ко'мнате мо'жно открыва'ть о'кна (you may), нельзя' открыва'ть (you may not). The "
             "perfective is for one specific action: Мо'жно откры'ть окно'? (May I open it now?). And Нельзя' "
             "откры'ть окно' says that it cannot be opened, because it is stuck.",
             examples=[
                 ex("В э'той ко'мнате мо'жно открыва'ть о'кна.", "You may open the windows in this room.", "открыва'ть"),
                 ex("В э'той ко'мнате нельзя' открыва'ть о'кна.", "You may not open the windows in this room.", "открыва'ть"),
                 ex("Здесь жа'рко! Мо'жно откры'ть окно'?", "It's hot here! May I open the window?", "откры'ть"),
                 ex("Нельзя' откры'ть окно'. Оно' не открыва'ется.", "The window can't be opened. It's stuck.", "откры'ть"),
             ]),
    ],
    verify=(vf("начинать", "начинаю") + vf("заканчивать", "заканчиваю") + vf("любить", "люблю")
            + vf("уметь", "умею") + vf("съесть", "съесть") + vf("открывать", "открывать")
            + vf("открыть", "открыть") + vf("должен", "должен", "должна", "должно", "должны")),
    exercises=[
        fb("Я начина'ю ___ кни'гу.", ["чита'ть", "прочита'ть"], "чита'ть",
           "After начина'ть: the imperfective infinitive.", tr="I'm starting to read the book."),
        fb("Он зака'нчивает ___ письмо'.", ["писа'ть", "написа'ть"], "писа'ть",
           "After зака'нчивать: the imperfective infinitive.", tr="He is finishing writing the letter."),
        fb("Ребёнок у'чится ___.", ["писа'ть", "написа'ть"], "писа'ть",
           "After учи'ться: the imperfective infinitive.", tr="The child is learning to write."),
        fb("Я люблю' ___ на гита'ре.", ["игра'ть", "сыгра'ть"], "игра'ть",
           "After люби'ть: the imperfective infinitive.", tr="I like to play the guitar."),
        fb("Я голоден. Я хочу' ___.", ["есть", "съесть"], "есть",
           "Wanting to eat in general: imperfective.", tr="I'm hungry. I want to eat."),
        fb("Сего'дня я хочу' ___ дома'шнюю рабо'ту (and get it done).", ["сде'лать", "де'лать"], "сде'лать",
           "Wanting to complete it: perfective.", tr="Today I want to get my homework done."),
        fb("Ты до'лжен ___ э'ту кни'гу. (read it through)", ["прочита'ть", "чита'ть"], "прочита'ть",
           "A task to complete: perfective.", tr="You have to read this book."),
        fb("В э'той ко'мнате нельзя' ___ о'кна.", ["открыва'ть", "откры'ть"], "открыва'ть",
           "A general prohibition: imperfective.", tr="You may not open the windows in this room."),
        fb("Здесь жа'рко! Мо'жно ___ окно'?", ["откры'ть", "открыва'ть"], "откры'ть",
           "One specific action: perfective.", tr="It's hot here! May I open the window?"),
        mc("Which aspect of the infinitive follows начина'ть?", ["imperfective", "perfective", "either", "neither"], "imperfective",
           "Start, finish, learn, like and know how take the imperfective.", order=True),
        mc("Which sentence means “The window can't be opened (it's stuck)”?",
           ["Нельзя' откры'ть окно'.", "Нельзя' открыва'ть окно'.", "Мо'жно откры'ть окно'.", "Мо'жно открыва'ть окно'."],
           "Нельзя' откры'ть окно'.", "Perfective: it cannot be done."),
    ],
)

# ---------------------------------------------------------------------------- 86
L86 = lesson(
    "Commands: every day or just once?",
    "Гуля'йте ка'ждый ве'чер! Погуля'йте вме'сте!",
    requires=["читать", "писать", "гулять", "говорить", "купить"],
    cards=[
        card("Two aspects, two kinds of command",
             "In a command the imperfective means do it regularly, as a habit, or in general. The perfective means "
             "do it once, now, or all the way to the end. Negative commands almost always use the imperfective: "
             "Не покупа'й! Not “Не купи'!”. The endings are the same as in lesson 26: -й or -и for one person "
             "(informal), and -йте or -ите for several people or politeness.",
             tables=[table(
                 ["Verbs", "Imperfective", "Perfective"],
                 [["чита'ть / прочита'ть", "чита'й(те)", "прочита'й(те)"],
                  ["писа'ть / написа'ть", "пиши'(те)", "напиши'(те)"],
                  ["де'лать / сде'лать", "де'лай(те)", "сде'лай(те)"],
                  ["есть / съесть", "ешь(те)", "съешь(те)"],
                  ["гуля'ть / погуля'ть", "гуля'й(те)", "погуля'й(те)"],
                  ["покупа'ть / купи'ть", "покупа'й(те)", "купи'(те)"],
                  ["говори'ть / сказа'ть", "говори'(те)", "скажи'(те)"]])]),
        card("Choosing",
             "Гуля'йте ка'ждый ве'чер! tells people to make a habit of it. Погуля'йте вме'сте! asks them to "
             "go once, right now. Ешь суп! means eat soup as a general habit, while Съешь э'тот суп! means eat "
             "all of this soup. When you want to see the result, use the perfective.",
             examples=[
                 ex("Гуля'йте ка'ждый ве'чер!", "Go for a walk every evening!", "Гуля'йте"),
                 ex("Погуля'йте вме'сте!", "Go for a walk together! (this time)", "Погуля'йте"),
                 ex("Съешь э'тот суп!", "Eat all of this soup!", "Съешь"),
                 ex("Прочита'й э'ту кни'гу до конца'.", "Read this book to the end.", "Прочита'й"),
                 ex("Не покупа'й э'ту маши'ну!", "Don't buy this car!", "Не покупа'й"),
             ]),
    ],
    verify=(vf("читать", "читай", "читайте") + vf("прочитать", "прочитай", "прочитайте")
            + vf("писать", "пиши", "пишите") + vf("написать", "напиши", "напишите")
            + vf("делать", "делай") + vf("сделать", "сделай") + vf("есть", "ешь", "ешьте")
            + vf("съесть", "съешь", "съешьте") + vf("гулять", "гуляй", "гуляйте")
            + vf("погулять", "погуляйте") + vf("покупать", "покупай") + vf("купить", "купи", "купите")
            + vf("говорить", "говори", "говорите") + vf("сказать", "скажи", "скажите")),
    exercises=[
        fb("___ ка'ждый ве'чер!", ["Гуля'йте", "Погуля'йте"], "Гуля'йте",
           "A regular habit: imperfective.", tr="Go for a walk every evening!"),
        fb("___ вме'сте сего'дня!", ["Погуля'йте", "Гуля'йте"], "Погуля'йте",
           "Just once: perfective.", tr="Let's go for a walk together today!"),
        fb("___ э'ту кни'гу до конца'!", ["Прочита'й", "Чита'й"], "Прочита'й",
           "To the end: perfective.", tr="Read this book to the end!"),
        fb("Не ___ э'ту маши'ну!", ["покупа'й", "купи'", "покупа'ю", "купи'л"], "покупа'й",
           "A negative command: imperfective.", tr="Don't buy this car!", lemma="покупать"),
        fb("___ э'тот суп! (all of it)", ["Съешь", "Ешь"], "Съешь",
           "Eat it all: perfective.", tr="Eat all of this soup!"),
        fb("___ ка'ждый день по-ру'сски!", ["Чита'й", "Прочита'й"], "Чита'й",
           "Every day: imperfective.", tr="Read in Russian every day!"),
        fb("Не ___ мне э'то!", ["говори'", "скажи'", "говори'л", "ска'жет"], "говори'",
           "A negative command: imperfective.", tr="Don't tell me that!"),
        fb("___ мне, где вокза'л. (this once)", ["Скажи'", "Говори'"], "Скажи'",
           "A single request: perfective.", tr="Tell me where the station is."),
        mc("Which aspect do negative commands usually take?", ["imperfective", "perfective", "both", "neither"], "imperfective",
           "Не покупа'й, не говори'.", order=True),
        mc("Which command means “Read this book to the end”?",
           ["Прочита'й э'ту кни'гу.", "Чита'й э'ту кни'гу.", "Прочита'ю э'ту кни'гу.", "Прочита'л э'ту кни'гу."],
           "Прочита'й э'ту кни'гу.", "Perfective imperative."),
        mc("Which command means “Go for a walk every evening!”?",
           ["Гуля'йте ка'ждый ве'чер!", "Погуля'йте ка'ждый ве'чер!", "Гуля'ю ка'ждый ве'чер!", "Гуля'ли ка'ждый ве'чер!"],
           "Гуля'йте ка'ждый ве'чер!", "A habit: imperfective."),
    ],
)

# ---------------------------------------------------------------------------- 87
L87 = lesson(
    "Making the perfective: prefixes",
    "Чита'ть → прочита'ть, писа'ть → написа'ть",
    requires=["видеть", "слышать", "писать", "читать", "готовить"],
    cards=[
        card("Seven common prefixes",
             "The simplest way to make a perfective verb is to add a prefix. The prefix does not change the "
             "meaning, only the aspect. Seven prefixes do most of the work. The stress stays on the same "
             "syllable as in the imperfective, except with вы-, which always carries the stress.",
             tables=[table(
                 ["Prefix", "Imperfective", "Perfective"],
                 [["про-", "чита'ть", "прочита'ть"],
                  ["на-", "писа'ть", "написа'ть"],
                  ["с-", "есть", "съесть"],
                  ["у-", "ви'деть", "уви'деть"],
                  ["при-", "гото'вить", "пригото'вить"],
                  ["по-", "за'втракать", "поза'втракать"],
                  ["вы-", "учи'ть", "вы'учить"]],
                 note="Also: слы'шать → услы'шать, пить → вы'пить, де'лать → сде'лать. Съесть has a hard sign, because the prefix с- ends in a consonant and е follows.")]),
        card("Learn to memorize, teach to teach",
             "Учи'ть has two perfectives. Вы'учить means to learn by heart, to memorize: Он вы'учил слова'. "
             "Научи'ть means to teach someone how to do something: Мать научи'ла ребёнка ходи'ть. Remember the "
             "pairs, since you cannot always guess the prefix from the verb.",
             examples=[
                 ex("Вдруг я уви'дел его' в па'рке.", "Suddenly I saw him in the park.", "уви'дел"),
                 ex("Вдруг мы услы'шали го'лос.", "Suddenly we heard a voice.", "услы'шали"),
                 ex("Он вы'учил но'вые слова'.", "He learned the new words by heart.", "вы'учил"),
                 ex("Она' вы'пила ча'шку ко'фе.", "She drank a cup of coffee.", "вы'пила"),
                 ex("Он съел весь суп.", "He ate all the soup.", "съел"),
             ]),
    ],
    verify=(vf("прочитать", "прочитал") + vf("написать", "написал") + vf("съесть", "съел", "съела")
            + vf("увидеть", "увидел") + vf("услышать", "услышали") + vf("приготовить", "приготовил")
            + vf("позавтракать", "позавтракал") + vf("выучить", "выучил") + vf("выпить", "выпила")),
    exercises=[
        fb("Вчера' я ___ но'вые слова'. (learned by heart)", ["вы'учил", "учи'л", "научи'л", "учи'лся"], "вы'учил",
           "To memorize: вы'учить.", tr="Yesterday I learned the new words by heart."),
        fb("Он ___ весь суп.", ["съел", "ел", "съесть", "съест"], "съел",
           "Perfective past of есть: съел.", tr="He ate all the soup."),
        fb("Она' ___ ча'шку ко'фе.", ["вы'пила", "пила'", "вы'пить", "пи'ла"], "вы'пила",
           "Perfective of пить: вы'пить.", tr="She drank a cup of coffee."),
        fb("Вдруг я ___ его' в па'рке.", ["уви'дел", "ви'дел"], "уви'дел",
           "Suddenly = a moment: perfective.", tr="Suddenly I saw him in the park."),
        fb("Вдруг мы ___ го'лос.", ["услы'шали", "слы'шали"], "услы'шали",
           "Suddenly = a moment: perfective.", tr="Suddenly we heard a voice."),
        mc("What is the perfective of чита'ть?", ["прочита'ть", "написа'ть", "сде'лать", "уви'деть"], "прочита'ть",
           "Про- + чита'ть."),
        mc("What is the perfective of писа'ть?", ["написа'ть", "прочита'ть", "сде'лать", "съесть"], "написа'ть",
           "На- + писа'ть."),
        mc("What is the perfective of ви'деть?", ["уви'деть", "прови'деть", "нави'деть", "свидеть"], "уви'деть",
           "У- + ви'деть."),
        mc("Where does the stress fall in вы'учить?", ["always on вы-", "on the last syllable", "same as учи'ть", "on -чить"],
           "always on вы-", "Вы- always carries the stress."),
        mc("Which prefix makes пригото'вить?", ["при-", "по-", "на-", "с-"], "при-",
           "При- + гото'вить.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 88
L88 = lesson(
    "Making the perfective: suffixes and different verbs",
    "Открыва'ть → откры'ть, встава'ть → встать, говори'ть → сказа'ть",
    requires=["открыть", "закрыть", "продать", "спросить", "ответить"],
    cards=[
        card("Dropping or changing the suffix",
             "Many pairs do not use a prefix at all. Some drop the suffix -ва-: открыва'ть → откры'ть, "
             "закрыва'ть → закры'ть, продава'ть → прода'ть, встава'ть → встать. In others the ending "
             "changes: -ать or -ять becomes -ить or -нуть, as in изуча'ть → изучи'ть, отвеча'ть → "
             "отве'тить, отдыха'ть → отдохну'ть. Спра'шивать changes to спроси'ть.",
             tables=[table(
                 ["Imperfective", "Perfective", "What changes"],
                 [["открыва'ть", "откры'ть", "-ва- drops"],
                  ["закрыва'ть", "закры'ть", "-ва- drops"],
                  ["продава'ть", "прода'ть", "-ва- drops"],
                  ["спра'шивать", "спроси'ть", "ending changes"],
                  ["изуча'ть", "изучи'ть", "-ать → -ить"],
                  ["отвеча'ть", "отве'тить", "-ать → -ить"],
                  ["отдыха'ть", "отдохну'ть", "-ать → -нуть"]])]),
        card("Pairs you just have to learn",
             "A few verbs use two completely different words for the two aspects. The most common are "
             "говори'ть / сказа'ть (to say) and покупа'ть / купи'ть (to buy). Always learn a verb together with its "
             "partner. Here are their past forms in use:",
             examples=[
                 ex("Наконе'ц он откры'л окно'.", "At last he opened the window.", "откры'л"),
                 ex("Вдруг дверь закры'лась.", "Suddenly the door closed.", "закры'лась"),
                 ex("Вчера' я прода'л маши'ну.", "Yesterday I sold my car.", "прода'л"),
                 ex("Он спроси'л меня', где вокза'л.", "He asked me where the station was.", "спроси'л"),
                 ex("Она' сра'зу отве'тила на мой вопро'с.", "She answered my question right away.", "отве'тила"),
                 ex("Я купи'л биле'ты и сказа'л об э'том дру'гу.", "I bought the tickets and told my friend.", "купи'л"),
             ]),
    ],
    verify=(vf("открыть", "открыл") + vf("закрыть", "закрыл") + vf("продать", "продал")
            + vf("спросить", "спросил") + vf("ответить", "ответила") + vf("купить", "купил")
            + vf("сказать", "сказал") + vf("изучить", "изучил") + vf("отдохнуть", "отдохнул")
            + vf("встать", "встать")),
    exercises=[
        fb("Наконе'ц он ___ окно'.", ["откры'л", "открыва'л"], "откры'л",
           "Наконе'ц: perfective.", tr="At last he opened the window."),
        fb("Вдруг дверь ___.", ["закры'лась", "закрыва'лась"], "закры'лась",
           "Вдруг: perfective.", tr="Suddenly the door closed."),
        fb("Вчера' я ___ маши'ну. (sold it)", ["прода'л", "продава'л"], "прода'л",
           "A single completed sale: perfective.", tr="Yesterday I sold my car."),
        fb("Он ___ меня', где вокза'л.", ["спроси'л", "спра'шивал"], "спроси'л",
           "One question, one answer: perfective.", tr="He asked me where the station was."),
        fb("Она' сра'зу ___ на мой вопро'с.", ["отве'тила", "отвеча'ла"], "отве'тила",
           "Сра'зу: perfective.", tr="She answered my question right away."),
        mc("What is the perfective of покупа'ть?", ["купи'ть", "продава'ть", "смотре'ть", "писа'ть"], "купи'ть",
           "A different stem."),
        mc("What is the perfective of говори'ть (to say)?", ["сказа'ть", "поговори'ть", "прогово'рить", "сговори'ть"], "сказа'ть",
           "A different word."),
        mc("What is the perfective of встава'ть?", ["встать", "вста'вить", "встава'л", "встав"], "встать",
           "Drop -ва-."),
        mc("Which pair drops the suffix -ва-?", ["закрыва'ть → закры'ть", "писа'ть → написа'ть", "говори'ть → сказа'ть", "отдыха'ть → отдохну'ть"],
           "закрыва'ть → закры'ть", "Закрыва'ть → закры'ть."),
    ],
)

# ---------------------------------------------------------------------------- 89
L89 = lesson(
    "Say, tell, order: сказа'ть, рассказа'ть, заказа'ть",
    "Скажу', расскажу', закажу'",
    requires=["говорить", "сказать", "рассказывать", "рассказать", "спросить"],
    cards=[
        card("Говори'ть and сказа'ть",
             "Говори'ть is a regular second-family verb. Its perfective сказа'ть is a first-family verb with "
             "a consonant change (з → ж) throughout the future: скажу', ска'жешь, ска'жет. Two other very "
             "common pairs follow the same pattern: зака'зывать / заказа'ть (to order) and расска'зывать / "
             "рассказа'ть (to tell, to narrate). The commands are скажи'(те), закажи'(те), расскажи'(те).",
             tables=[table(
                 ["Person", "говори'ть (present)", "сказа'ть (future)"],
                 [["я", "говор{ю'}", "скаж{у'}"],
                  ["ты", "говор{и'шь}", "ска'ж{ешь}"],
                  ["он · она' · оно'", "говор{и'т}", "ска'ж{ет}"],
                  ["мы", "говор{и'м}", "ска'ж{ем}"],
                  ["вы", "говор{и'те}", "ска'ж{ете}"],
                  ["они'", "говор{я'т}", "ска'ж{ут}"]],
                 note="Past: сказа'л, сказа'ла, сказа'ли.")]),
        card("Ordering and telling",
             "Заказа'ть and рассказа'ть have the same pattern in the future, where з changes to ж. Their "
             "imperfective partners are regular -ывать verbs: зака'зываю, зака'зываешь and расска'зываю.",
             tables=[table(
                 ["Person", "заказа'ть", "рассказа'ть"],
                 [["я", "закаж{у'}", "расскаж{у'}"],
                  ["ты", "зака'ж{ешь}", "расска'ж{ешь}"],
                  ["он · она' · оно'", "зака'ж{ет}", "расска'ж{ет}"],
                  ["мы", "зака'ж{ем}", "расска'ж{ем}"],
                  ["вы", "зака'ж{ете}", "расска'ж{ете}"],
                  ["они'", "зака'ж{ут}", "расска'ж{ут}"]])],
             examples=[
                 ex("Я хочу' знать, что ты ска'жешь.", "I want to know what you will say.", "ска'жешь"),
                 ex("Продавщи'ца сказа'ла, что все о'вощи све'жие.", "The saleswoman said that all the vegetables are fresh.", "сказа'ла"),
                 ex("Мы зака'жем суп и сок.", "We will order soup and juice.", "зака'жем"),
                 ex("Расскажи' мне о го'роде.", "Tell me about the city.", "Расскажи'"),
             ]),
    ],
    verify=(vf("говорить", "говорю", "говоришь", "говорит", "говорим", "говорите", "говорят")
            + vf("сказать", "скажу", "скажешь", "скажет", "скажем", "скажете", "скажут", "сказал", "сказала", "скажи")
            + vf("заказать", "закажу", "закажешь", "закажет", "закажем", "закажете", "закажут", "закажи")
            + vf("рассказать", "расскажу", "расскажешь", "расскажет", "расскажем", "расскажете", "расскажут", "расскажи")
            + vf("заказывать", "заказываю") + vf("рассказывать", "рассказываю")),
    exercises=[
        fb("Я хочу' знать, что ты ___.", ["ска'жешь", "скажу'", "ска'жет", "сказа'л"], "ска'жешь",
           "Ты takes -ешь.", tr="I want to know what you will say.", lemma="сказать"),
        fb("Продавщи'ца ___, что все о'вощи све'жие.", ["сказа'ла", "сказа'л", "ска'жут", "скажу'"], "сказа'ла",
           "Feminine past: сказа'ла.", tr="The saleswoman said that all the vegetables are fresh.", lemma="сказать"),
        fb("Мы ___ суп и сок.", ["зака'жем", "закажу'", "зака'жет", "зака'жут"], "зака'жем",
           "Мы takes -ем.", tr="We will order soup and juice.", lemma="заказать"),
        fb("Я ___ ры'бу.", ["закажу'", "зака'жешь", "зака'жет", "зака'жем"], "закажу'",
           "Я takes -у', with з → ж.", tr="I will order fish.", lemma="заказать"),
        fb("___ мне о го'роде.", ["Расскажи'", "Расскажу'", "Расска'жет", "Расска'зывать"], "Расскажи'",
           "A command: расскажи'.", tr="Tell me about the city."),
        fb("Мы ча'сто ___ по-ру'сски.", ["говори'м", "ска'жем", "говорю'", "ска'жут"], "говори'м",
           "Often = a habit: imperfective, мы-form.", tr="We often speak Russian.", lemma="говорить"),
        mc("What is the perfective of зака'зывать?", ["заказа'ть", "зака'зать", "заказа'л", "заказ"], "заказа'ть",
           "Зака'зывать / заказа'ть."),
        mc("What is the informal command from сказа'ть?", ["скажи'", "скажу'", "ска'жет", "ска'зывай"], "скажи'",
           "Скажи'(те)!"),
        mc("What does ска'жут mean?", ["they will say", "they said", "they are saying", "say!"], "they will say",
           "Они' takes -ут."),
    ],
)

# ---------------------------------------------------------------------------- 90
L90 = lesson(
    "A glass of water, a piece of bread",
    "Стака'н воды', кусо'к хле'ба, литр молока'",
    requires=["хлеб", "молоко", "стакан", "кусок", "килограмм"],
    cards=[
        card("Amounts take the genitive",
             "After a word for a part or an amount, the thing measured goes in the genitive: кусо'к хле'ба "
             "(a piece of bread), стака'н воды' (a glass of water), литр молока' (a liter of milk). This is the "
             "genitive you already know, used for “of”.",
             tables=[table(
                 ["Measure", "Example"],
                 [["кусо'к", "кусо'к хле'ба · кусо'к сы'ра"],
                  ["стака'н", "стака'н воды' · стака'н со'ка"],
                  ["ча'шка", "ча'шка ча'я · ча'шка ко'фе"],
                  ["буты'лка", "буты'лка вина' · буты'лка пи'ва"],
                  ["па'чка", "па'чка ча'я · па'чка са'хара"],
                  ["литр", "литр молока' · литр воды'"],
                  ["килогра'мм", "килогра'мм карто'шки · килогра'мм мя'са"],
                  ["полови'на", "полови'на пи'ццы · полови'на хле'ба"]],
                 note="Ко'фе never changes, so it looks the same in every case.")]),
        card("Parts and fractions",
             "Fractions are also followed by the genitive: полови'на (a half), треть (a third), че'тверть (a "
             "quarter). Where the whole is a single word, the half can be joined to it with пол-: полчаса' "
             "(half an hour).",
             examples=[
                 ex("Дай мне стака'н воды'.", "Give me a glass of water.", "воды'"),
                 ex("Купи' литр молока'.", "Buy a liter of milk.", "молока'"),
                 ex("Я хочу' кусо'к хле'ба.", "I want a piece of bread.", "хле'ба"),
                 ex("Она' вы'пила буты'лку вина'.", "She drank a bottle of wine.", "вина'"),
                 ex("Я съел полови'ну пи'ццы.", "I ate half of the pizza.", "пи'ццы"),
             ]),
    ],
    verify=(vf("хлеб", "хлеба") + vf("сыр", "сыра") + vf("вода", "воды") + vf("сок", "сока") + vf("чай", "чая")
            + vf("вино", "вина") + vf("пиво", "пива") + vf("сахар", "сахара") + vf("молоко", "молока")
            + vf("картошка", "картошки") + vf("мясо", "мяса") + vf("пицца", "пиццы")),
    exercises=[
        fb("Дай мне стака'н ___.", ["воды'", "вода'", "воду'", "воде'"], "воды'",
           "After a measure: genitive.", tr="Give me a glass of water.", lemma="вода"),
        fb("Купи' литр ___.", ["молока'", "молоко'", "молоку'", "молоке'"], "молока'",
           "After a measure: genitive.", tr="Buy a liter of milk.", lemma="молоко"),
        fb("Я хочу' кусо'к ___.", ["хле'ба", "хлеб", "хле'бу", "хле'бе"], "хле'ба",
           "After a measure: genitive.", tr="I want a piece of bread.", lemma="хлеб"),
        fb("Вот па'чка ___.", ["ча'я", "чай", "ча'ем", "ча'е"], "ча'я",
           "After a measure: genitive.", tr="Here is a pack of tea.", lemma="чай"),
        fb("Она' вы'пила буты'лку ___.", ["вина'", "вино'", "вину'", "вине'"], "вина'",
           "After a measure: genitive.", tr="She drank a bottle of wine.", lemma="вино"),
        fb("Я съел полови'ну ___.", ["пи'ццы", "пи'цца", "пи'ццу", "пи'цце"], "пи'ццы",
           "After полови'на: genitive.", tr="I ate half of the pizza.", lemma="пицца"),
        fb("Купи' килогра'мм ___.", ["карто'шки", "карто'шка", "карто'шку", "карто'шке"], "карто'шки",
           "After a measure: genitive.", tr="Buy a kilo of potatoes.", lemma="картошка"),
        mc("Which case follows a measure word like стака'н or кусо'к?", ["genitive", "accusative", "prepositional", "nominative"], "genitive",
           "Стака'н воды'.", order=True),
        mc("Which phrase means “a glass of water”?",
           ["стака'н воды'", "стака'н вода'", "стака'н воду'", "стака'н воде'"], "стака'н воды'",
           "Genitive after стака'н."),
        mc("What is the genitive of молоко'?", ["молока'", "молоко'", "молоку'", "молоке'"], "молока'",
           "Neuter in -о: -а."),
    ],
)

# ---------------------------------------------------------------------------- 91
L91 = lesson(
    "Some tea, some cheese: the genitive for “some”",
    "Купи' сы'ра, хочу' ча'я, дай воды'",
    requires=["купить", "хотеть", "сыр", "чай", "сок"],
    cards=[
        card("Not all, just some",
             "The genitive can also mean “some” or “any”, when the amount is not stated and you do not "
             "mean a specific, known thing. This is common with commands and wishes: Купи' сы'ра (buy some "
             "cheese), Хочу' ча'я (I want some tea), Дай воды' (give me some water). The same word in the "
             "accusative points to something definite: Купи' э'тот сыр.",
             tables=[table(
                 ["Word", "Genitive: “some”", "Informal alternative"],
                 [["сыр", "сы'р{а}", "сы'р{у}"],
                  ["чай", "ча'{я}", "ча'{ю}"],
                  ["сок", "со'к{а}", "со'к{у}"],
                  ["са'хар", "са'хар{а}", "са'хар{у}"],
                  ["хлеб", "хле'б{а}", "—"],
                  ["вода'", "вод{ы'}", "—"]])]),
        card("Informal -у and -ю",
             "Some masculine nouns, especially food and drinks, have a second, informal “some” ending: -у or -ю "
             "instead of -а or -я. You can use either in speech, but only the -а/-я form is possible in writing "
             "for every noun. Feminine and neuter nouns have no such alternative.",
             examples=[
                 ex("Купи' сы'ра.", "Buy some cheese.", "сы'ра"),
                 ex("Хочу' ча'я.", "I want some tea.", "ча'я"),
                 ex("Хочу' ча'ю.", "I want some tea. (informal)", "ча'ю"),
                 ex("Дай мне со'ку.", "Give me some juice. (informal)", "со'ку"),
                 ex("Дай воды'.", "Give me some water.", "воды'"),
             ]),
    ],
    verify=(vf("сыр", "сыра") + vf("чай", "чая") + vf("сок", "сока") + vf("сахар", "сахара") + vf("хлеб", "хлеба")
            + vf("вода", "воды")),
    exercises=[
        fb("Купи' ___. (some cheese)", ["сы'ра", "сы'ре", "сы'ром", "сы'ры"], "сы'ра",
           "“Some” takes the genitive.", tr="Buy some cheese.", lemma="сыр"),
        fb("Дай ___. (some water)", ["воды'", "воде'", "водо'й", "вод"], "воды'",
           "“Some” takes the genitive.", tr="Give me some water."),
        fb("Купи' ___ на у'жин. (some bread)", ["хле'ба", "хле'бе", "хле'бом", "хле'бы"], "хле'ба",
           "“Some” takes the genitive.", tr="Buy some bread for dinner.", lemma="хлеб"),
        fb("Хочу' ___. (some tea, informal)", ["ча'ю", "ча'е", "ча'ем", "чаи'"], "ча'ю",
           "The informal “some” ending is -ю.", tr="I want some tea.", lemma="чай"),
        fb("Дай мне ___. (some juice, informal)", ["со'ку", "со'ке", "со'ком", "со'ки"], "со'ку",
           "The informal “some” ending is -у.", tr="Give me some juice.", lemma="сок"),
        mc("Which phrase means “half of the pizza”?",
           ["полови'на пи'ццы", "полови'на пи'цца", "полови'на пи'ццу", "полови'на пи'цце"], "полови'на пи'ццы",
           "Fractions take the genitive."),
        mc("Which form is the informal “some cheese”?", ["сы'ру", "сы'ра", "сыр", "сы'ре"], "сы'ру",
           "Some masculine nouns take -у."),
        mc("Which case can express “some” or “any”?", ["genitive", "prepositional", "nominative", "accusative"], "genitive",
           "Купи' сы'ра.", order=True),
        mc("Which of these has no informal -у alternative?", ["вода'", "сыр", "чай", "сок"], "вода'",
           "Only certain masculine nouns have it."),
    ],
)

# ---------------------------------------------------------------------------- 92
L92 = lesson(
    "At the checkout: rubles and kopecks",
    "Бу'дьте добры', ско'лько с меня'? С вас пять рубле'й",
    requires=["рубль", "копейка", "цена", "стоить", "платить"],
    cards=[
        card("Polite phrases",
             "In a store, Бу'дьте добры', … (Would you be so kind …) opens a polite request. Ско'лько с меня'? "
             "asks how much you owe, and the answer begins С вас … (from you …). Благодарю' (вас) is a formal "
             "thank-you. Ско'лько сто'ит …? asks the price of one thing, and to pay for something use "
             "плати'ть за plus the accusative.",
             examples=[
                 ex("— Бу'дьте добры', скажи'те, ско'лько с меня'? — С вас сто рубле'й.", "— Excuse me, how much do I owe? — A hundred rubles.", "С вас"),
                 ex("Благодарю' вас!", "Thank you!", "Благодарю'"),
                 ex("Ско'лько сто'ит э'тот сыр?", "How much does this cheese cost?", "сто'ит"),
                 ex("Я плачу' за обе'д.", "I'm paying for the lunch.", "за обе'д"),
             ]),
        card("Rubles and kopecks follow the pattern of hours",
             "Рубль and копе'йка use the same three forms as час and мину'та: one form after 1, another "
             "after 2, 3 and 4, and another from 5 up. The last digit decides, except for the teens, which "
             "always take the plural form. Also learn the new hundreds from 200 to 400: две'сти, три'ста, "
             "четы'реста.",
             tables=[table(
                 ["Number", "рубль", "копе'йка"],
                 [["1 · 21", "рубль", "копе'йка"],
                  ["2 · 3 · 4", "рубл{я'}", "копе'йк{и}"],
                  ["5 – 20", "рубл{е'й}", "копе'{ек}"],
                  ["22 · 23 · 24", "рубл{я'}", "копе'йк{и}"],
                  ["25 – 30", "рубл{е'й}", "копе'{ек}"]])],
             examples=[
                 ex("С вас четы'реста четы'ре рубля' со'рок пять копе'ек.", "That's 404 rubles and 45 kopecks.", "четы'ре рубля'"),
                 ex("Два биле'та сто'ят четы'реста рубле'й.", "Two tickets cost 400 rubles.", "сто'ят"),
             ]),
    ],
    verify=(vf("рубль", "рубль", "рубля", "рублей") + vf("копейка", "копейка", "копейки", "копеек")
            + vf("стоить", "стоит", "стоят") + vf("платить", "плачу") + vf("добрый", "добры")
            + vf("благодарить", "благодарю") + vf("двести", "двести") + vf("триста", "триста")
            + vf("четыреста", "четыреста")),
    exercises=[
        fb("С вас два ___.", ["рубля'", "рубль", "рубле'й", "рубли'"], "рубля'",
           "After 2, 3, 4: рубля'.", tr="That's two rubles.", lemma="рубль"),
        fb("С вас пять ___.", ["рубле'й", "рубля'", "рубль", "рубли'"], "рубле'й",
           "After 5 and up: рубле'й.", tr="That's five rubles.", lemma="рубль"),
        fb("С вас оди'н ___.", ["рубль", "рубля'", "рубле'й", "рубли'"], "рубль",
           "After 1: рубль.", tr="That's one ruble.", lemma="рубль"),
        fb("Три ___.", ["копе'йки", "копе'йка", "копе'ек", "копе'йку"], "копе'йки",
           "After 2, 3, 4: копе'йки.", tr="Three kopecks.", lemma="копейка"),
        fb("Пять ___.", ["копе'ек", "копе'йки", "копе'йка", "копе'йку"], "копе'ек",
           "After 5 and up: копе'ек.", tr="Five kopecks.", lemma="копейка"),
        fb("Два биле'та ___ четы'реста рубле'й.", ["сто'ят", "сто'ит", "сто'ишь", "сто'им"], "сто'ят",
           "Plural subject (два биле'та): сто'ят.", tr="Two tickets cost 400 rubles.", lemma="стоить"),
        fb("Я плачу' ___ обе'д.", ["за", "на", "в", "к"], "за",
           "To pay for: плати'ть за + accusative.", tr="I'm paying for lunch."),
        mc("How do you ask “How much do I owe?”", ["Ско'лько с меня'?", "Ско'лько у меня'?", "Ско'лько для меня'?", "Ско'лько на меня'?"],
           "Ско'лько с меня'?", "A fixed phrase."),
        mc("Which is correct for 22 rubles?",
           ["два'дцать два рубля'", "два'дцать два рубль", "два'дцать два рубле'й", "два'дцать два рубли'"],
           "два'дцать два рубля'", "The last digit is 2."),
        mc("Which is correct for 15 kopecks?",
           ["пятна'дцать копе'ек", "пятна'дцать копе'йки", "пятна'дцать копе'йка", "пятна'дцать копе'йку"],
           "пятна'дцать копе'ек", "The teens always take the plural form."),
    ],
)

# ---------------------------------------------------------------------------- 93
L93 = lesson(
    "Tasty, fresh, too hot: describing food",
    "Вку'сный суп, све'жая ры'ба, сли'шком горя'чий",
    requires=["вкусный", "свежий", "горячий", "сладкий", "острый"],
    cards=[
        card("Describing food",
             "Food words are ordinary adjectives, so they agree with the noun in gender and number. The "
             "adjectives with a hard stem follow the pattern you know (вку'сный, вку'сная, вку'сное, "
             "вку'сные). Those that end in -ий after ч or ж (горя'чий) or have a soft stem (све'жий) follow "
             "the soft pattern, with a spelling twist after ж/ч. Use сли'шком for “too” and да'же for “even”.",
             tables=[table(
                 ["Masculine", "Feminine", "Neuter", "Plural"],
                 [["вку'сн{ый} суп", "вку'сн{ая} ры'ба", "вку'сн{ое} мя'со", "вку'сн{ые} о'вощи"],
                  ["све'ж{ий} хлеб", "све'ж{ая} ры'ба", "све'ж{ее} молоко'", "све'ж{ие} о'вощи"],
                  ["горя'ч{ий} чай", "горя'ч{ая} ка'ша", "горя'ч{ее} блю'до", "горя'ч{ие} напи'тки"],
                  ["сла'дк{ий} чай", "сла'дк{ая} ка'ша", "сла'дк{ое} вино'", "сла'дк{ие} напи'тки"],
                  ["о'стр{ый} сыр", "о'стр{ая} колбаса'", "о'стр{ое} блю'до", "о'стр{ые} о'вощи"]])]),
        card("Courses, “too”, “even”, “ago”",
             "A meal has courses: пе'рвое (the first course, usually soup), второ'е or горя'чее (the main "
             "course), and десе'рт. Пе'рвое and второ'е are neuter adjectives used as nouns. The word "
             "сли'шком (too) goes in front of the adjective, and да'же (even) stands in front of the word it "
             "stresses. To say how long ago something was, put тому' наза'д after the time: год тому' наза'д.",
             examples=[
                 ex("Э'тот суп сли'шком горя'чий.", "This soup is too hot.", "сли'шком горя'чий"),
                 ex("Мя'со вку'сное, но сли'шком солёное.", "The meat is tasty, but too salty.", "вку'сное"),
                 ex("Он съел да'же суп.", "He even ate the soup.", "да'же"),
                 ex("Что на пе'рвое? — Суп.", "What's for the first course? — Soup.", "пе'рвое"),
                 ex("Год тому' наза'д мы жи'ли в А'нглии.", "A year ago we lived in England.", "тому' наза'д"),
             ]),
    ],
    verify=(vf("вкусный", "вкусный", "вкусная", "вкусное", "вкусные") + vf("свежий", "свежий", "свежая", "свежее", "свежие")
            + vf("горячий", "горячий", "горячая", "горячее", "горячие") + vf("сладкий", "сладкий", "сладкая", "сладкое", "сладкие")
            + vf("острый", "острый", "острая", "острое", "острые") + vf("солёный", "солёное")
            + vf("колбаса", "колбаса") + vf("напиток", "напитки") + vf("блюдо", "блюдо")),
    exercises=[
        fb("Э'то ___ суп.", ["вку'сный", "вку'сная", "вку'сное", "вку'сные"], "вку'сный",
           "Суп is masculine.", tr="This is a tasty soup.", lemma="вкусный"),
        fb("Э'то ___ ры'ба.", ["све'жая", "све'жий", "све'жее", "све'жие"], "све'жая",
           "Ры'ба is feminine.", tr="This is fresh fish.", lemma="свежий"),
        fb("Э'то ___ молоко'.", ["све'жее", "све'жий", "све'жая", "све'жие"], "све'жее",
           "Молоко' is neuter.", tr="This is fresh milk.", lemma="свежий"),
        fb("Э'то ___ о'вощи.", ["све'жие", "све'жий", "све'жая", "све'жее"], "све'жие",
           "О'вощи is plural.", tr="These are fresh vegetables.", lemma="свежий"),
        fb("Э'тот суп ___ горя'чий.", ["сли'шком", "да'же", "ско'ро", "наконе'ц"], "сли'шком",
           "Сли'шком = too.", tr="This soup is too hot."),
        fb("Он съел ___ суп.", ["да'же", "сли'шком", "ско'ро", "наконе'ц"], "да'же",
           "Да'же = even.", tr="He even ate the soup."),
        fb("Год ___ мы жи'ли в А'нглии.", ["тому' наза'д", "до", "по'сле", "из"], "тому' наза'д",
           "“Ago” follows the time.", tr="A year ago we lived in England."),
        mc("What is пе'рвое in a meal?", ["the first course", "the main course", "dessert", "a drink"], "the first course",
           "Usually soup.", order=True),
        mc("Which phrase means “too hot”?",
           ["сли'шком горя'чий", "да'же горя'чий", "ско'ро горя'чий", "тепе'рь горя'чий"], "сли'шком горя'чий",
           "Сли'шком goes in front of the adjective."),
        mc("Which phrase means “tasty meat”?",
           ["вку'сное мя'со", "вку'сный мя'со", "вку'сная мя'со", "вку'сные мя'со"], "вку'сное мя'со",
           "Мя'со is neuter."),
    ],
)

# ---------------------------------------------------------------------------- 94
L94 = lesson(
    "Review: aspect, amounts and prices",
    "Putting lessons 84 to 93 together",
    requires=["написать", "хлеб", "рубль", "вкусный", "сказать"],
    cards=[
        card("What you can do now",
             "You can choose the aspect from the question, for an infinitive and for a command, make "
             "perfectives with prefixes and suffixes, conjugate сказа'ть, заказа'ть and рассказа'ть, name "
             "amounts with the genitive (стака'н воды'), say “some” with the genitive (купи' сы'ра), pay in "
             "rubles and kopecks, and describe food.",
             tables=[table(
                 ["Topic", "Remember"],
                 [["Is it finished?", "Ты уже' написа'л? (perfective)"],
                  ["What did you do?", "Что ты де'лал? (imperfective)"],
                  ["After начина'ть, люби'ть, учи'ться", "imperfective infinitive"],
                  ["Negative commands", "imperfective: не покупа'й"],
                  ["Amounts", "стака'н воды' · кусо'к хле'ба"],
                  ["Prices", "оди'н рубль · два рубля' · пять рубле'й"]])],
             examples=[
                 ex("Бу'дьте добры', литр молока' и кусо'к сы'ра.", "Excuse me, a liter of milk and a piece of cheese.", "литр молока'"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("Ты уже' ___ письмо'?", ["написа'л", "писа'л"], "написа'л",
           "Уже' asks about completion: perfective.", tr="Have you written the letter yet?"),
        fb("Что ты ___ вчера' ве'чером?", ["де'лал", "сде'лал"], "де'лал",
           "Asking what the activity was: imperfective.", tr="What did you do yesterday evening?"),
        fb("Он начина'ет ___ кни'гу.", ["чита'ть", "прочита'ть"], "чита'ть",
           "After начина'ть: imperfective.", tr="He is starting to read the book."),
        fb("Не ___ э'ту маши'ну!", ["покупа'й", "купи'", "покупа'ю", "купи'л"], "покупа'й",
           "Negative command: imperfective.", tr="Don't buy this car!", lemma="покупать"),
        fb("Вчера' я ___ но'вые слова'. (learned by heart)", ["вы'учил", "учи'л", "научи'л", "учи'лся"], "вы'учил",
           "Вы'учить = to memorize.", tr="Yesterday I learned the new words by heart."),
        fb("Мы ___ суп и сок.", ["зака'жем", "закажу'", "зака'жет", "зака'жут"], "зака'жем",
           "Мы takes -ем.", tr="We will order soup and juice.", lemma="заказать"),
        fb("Дай мне стака'н ___.", ["воды'", "вода'", "воду'", "воде'"], "воды'",
           "After a measure: genitive.", tr="Give me a glass of water.", lemma="вода"),
        fb("Купи' ___. (some cheese)", ["сы'ра", "сы'ре", "сы'ром", "сы'ры"], "сы'ра",
           "“Some” takes the genitive.", tr="Buy some cheese.", lemma="сыр"),
        fb("С вас пять ___.", ["рубле'й", "рубля'", "рубль", "рубли'"], "рубле'й",
           "After 5: рубле'й.", tr="That's five rubles.", lemma="рубль"),
        fb("Э'то ___ ры'ба.", ["све'жая", "све'жий", "све'жее", "све'жие"], "све'жая",
           "Ры'ба is feminine.", tr="This is fresh fish.", lemma="свежий"),
        mc("Which aspect do negative commands usually take?", ["imperfective", "perfective", "both", "neither"], "imperfective",
           "Не покупа'й.", order=True),
        mc("What is the perfective of открыва'ть?", ["откры'ть", "открыв", "открыва'ться", "откры'л"], "откры'ть",
           "Drop -ва-."),
    ],
)

UNIT = unit("Unit 12: Aspect in detail, shopping and food",
            [L84, L85, L86, L87, L88, L89, L90, L91, L92, L93, L94])
