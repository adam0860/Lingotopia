"""Unit 15: the genitive of adjectives, dates, describing people, clauses
(textbook module 4, lesson 21)."""
from dsl import *

# ---------------------------------------------------------------------------- 121
L121 = lesson(
    "Adjectives in the genitive: нет но́вого, без хоро́шей",
    "В кла'ссе нет но'вого студе'нта.",
    requires=["новый", "синий", "высокий", "хороший", "большой"],
    cards=[
        card("Four endings",
             "A singular adjective in the genitive takes -ого or -его for masculine and neuter nouns, and -ой or "
             "-ей for feminine ones. Use the hard endings (-ого, -ой) after hard stems like но'вый and the soft "
             "ones (-его, -ей) after soft stems like си'ний and тре'тий.",
             tables=[table(
                 ["Masculine", "Genitive (m, n)", "Feminine", "Genitive (f)"],
                 [["но'вый", "но'в{ого}", "но'вая", "но'в{ой}"],
                  ["си'ний", "си'н{его}", "си'няя", "си'н{ей}"],
                  ["ни'зкий", "ни'зк{ого}", "ни'зкая", "ни'зк{ой}"],
                  ["худо'й", "худ{о'го}", "худа'я", "худ{о'й}"],
                  ["второ'й", "втор{о'го}", "втора'я", "втор{о'й}"],
                  ["тре'тий", "тре'ть{его}", "тре'тья", "тре'ть{ей}"]])]),
        card("Spelling and stress",
             "After ж, ш, ч, щ and ц write е instead of an unstressed о: хоро'шего, хоро'шей, свежего. If the "
             "ending is stressed, write о: большо'го, большо'й. After к, г and х the endings stay the same "
             "(ни'зкого), because the spelling rule only changes ы to и.",
             tables=[table(
                 ["Nominative", "Genitive (m, n)", "Genitive (f)"],
                 [["хоро'ший", "хоро'ш{его}", "хоро'ш{ей}"],
                  ["све'жий", "све'ж{его}", "све'ж{ей}"],
                  ["большо'й", "больш{о'го}", "больш{о'й}"],
                  ["рабо'чий", "рабо'ч{его}", "рабо'ч{ей}"]])],
             examples=[
                 ex("В кла'ссе нет но'вого студе'нта.", "The new student is not in the classroom.", "но'вого"),
                 ex("В э'той ко'мнате нет большо'го окна'.", "There is no big window in this room.", "большо'го"),
                 ex("Э'тот мужчи'на сре'днего ро'ста.", "This man is of average height.", "сре'днего ро'ста"),
                 ex("Я не могу' жить без хоро'шей му'зыки.", "I can't live without good music.", "хоро'шей"),
                 ex("У тре'тьего зда'ния поверни'те напра'во.", "Turn right at the third building.", "тре'тьего"),
             ]),
        card("Compare three cases",
             "The masculine and neuter genitive is the same as the accusative of masculine adjectives with "
             "animate nouns. The feminine genitive is the same as the feminine prepositional.",
             tables=[table(
                 ["Genitive (нет …)", "Accusative (вижу …)", "Prepositional (о …)"],
                 [["но'вого студе'нта", "но'вого студе'нта", "но'вом студе'нте"],
                  ["но'вого стола'", "но'вый стол", "но'вом столе'"],
                  ["но'вой де'вушки", "но'вую де'вушку", "но'вой де'вушке"],
                  ["но'вого письма'", "но'вое письмо'", "но'вом письме'"]])]),
    ],
    verify=(vf("новый", "нового", "новой") + vf("синий", "синего", "синей") + vf("низкий", "низкого", "низкой")
            + vf("худой", "худого", "худой") + vf("второй", "второго", "второй") + vf("третий", "третьего", "третьей")
            + vf("хороший", "хорошего", "хорошей") + vf("свежий", "свежего", "свежей")
            + vf("большой", "большого", "большой") + vf("рабочий", "рабочего", "рабочей")
            + vf("средний", "среднего") + vf("рост", "роста") + vf("девушка", "девушки", "девушку", "девушке")
            + vf("письмо", "письма") + vf("стол", "стола")),
    exercises=[
        fb("В кла'ссе нет ___ студе'нта.", ["но'вого", "но'вый", "но'вому", "но'вым"], "но'вого",
           "Masculine genitive: -ого.", tr="The new student is not in the classroom.", lemma="новый"),
        fb("У меня' нет ___ маши'ны.", ["но'вой", "но'вая", "но'вую", "но'вым"], "но'вой",
           "Feminine genitive: -ой.", tr="I don't have a new car.", lemma="новый"),
        fb("В э'той ко'мнате нет ___ окна'.", ["большо'го", "большо'й", "большо'е", "большо'му"], "большо'го",
           "Окно' is neuter: -ого, stressed so written о.", tr="There is no big window in this room.", lemma="большой"),
        fb("Я не могу' жить без ___ му'зыки.", ["хоро'шей", "хоро'шая", "хоро'шую", "хоро'шего"], "хоро'шей",
           "Feminine genitive after ш: -ей.", tr="I can't live without good music.", lemma="хороший"),
        fb("Э'тот мужчи'на ___ ро'ста. (average)", ["сре'днего", "сре'дний", "сре'дней", "сре'днему"], "сре'днего",
           "Masculine soft stem: -его.", tr="This man is of average height.", lemma="средний"),
        fb("У ___ зда'ния поверни'те напра'во. (third)", ["тре'тьего", "тре'тий", "тре'тьей", "тре'тьему"], "тре'тьего",
           "Neuter soft stem: -ьего.", tr="Turn right at the third building.", lemma="третий"),
        fb("Здесь нет ___ молока'. (fresh)", ["све'жего", "све'жее", "све'жей", "све'жему"], "све'жего",
           "Neuter after ж: -его.", tr="There is no fresh milk here.", lemma="свежий"),
        mc("Which form is the feminine genitive?", ["но'вой", "но'вого", "но'вую", "но'вым"], "но'вой",
           "Feminine genitive: -ой."),
        mc("Which ending do you write after ш, ж, ч, щ if it is unstressed?", ["-его / -ей", "-ого / -ой", "-ому / -ым", "-ей / -ем"],
           "-его / -ей", "The 5-letter spelling rule."),
    ],
)

# ---------------------------------------------------------------------------- 122
L122 = lesson(
    "My, this, which: other words in the genitive",
    "Нет моего' ключа'. Чьей ку'ртки нет?",
    requires=["мой", "наш", "этот", "какой", "чей"],
    cards=[
        card("Possessives and question words",
             "Possessive pronouns (мой, твой, наш, ваш), question words (како'й, кото'рый, чей) and the words "
             "э'тот, тот, тако'й, друго'й and оди'н take the same endings as adjectives. Его', её and их never "
             "change.",
             tables=[table(
                 ["Nominative", "Masculine, neuter", "Feminine"],
                 [["мой / моя' / моё'", "моего'", "мое'й"],
                  ["твой / твоя' / твоё'", "твоего'", "твое'й"],
                  ["наш / на'ша / на'ше", "на'шего", "на'шей"],
                  ["ваш / ва'ша / ва'ше", "ва'шего", "ва'шей"],
                  ["како'й / кака'я", "како'го", "како'й"],
                  ["кото'рый / кото'рая", "кото'рого", "кото'рой"],
                  ["чей / чья", "чьего'", "чьей"]])]),
        card("This, that, such, another, one",
             "These words follow the same pattern. Remember that оди'н becomes одного' and одно'й.",
             tables=[table(
                 ["Nominative", "Masculine, neuter", "Feminine"],
                 [["э'тот / э'та / э'то", "э'того", "э'той"],
                  ["тот / та / то", "того'", "той"],
                  ["тако'й / така'я", "тако'го", "тако'й"],
                  ["друго'й / друга'я", "друго'го", "друго'й"],
                  ["оди'н / одна'", "одного'", "одно'й"]])],
             examples=[
                 ex("Сын э'того врача' - мой друг.", "This doctor's son is my friend.", "э'того врача'"),
                 ex("И'мя той де'вушки - Ве'ра.", "That girl's name is Vera.", "той"),
                 ex("Ключ ва'шей сестры' лежи'т на столе'.", "Your sister's key is lying on the table.", "ва'шей"),
                 ex("О'коло како'го до'ма остано'вка авто'буса?", "Near which building is the bus stop?", "како'го"),
                 ex("Чьей ку'ртки здесь нет?", "Whose jacket isn't here?", "Чьей"),
                 ex("У меня' никогда' не бу'дет друго'го тако'го дру'га.", "I will never have another friend like that.", "друго'го тако'го"),
             ]),
    ],
    verify=(vf("мой", "моего", "моей") + vf("твой", "твоего", "твоей") + vf("наш", "нашего", "нашей")
            + vf("ваш", "вашего", "вашей") + vf("какой", "какого", "какой") + vf("который", "которого", "которой")
            + vf("чей", "чьего", "чьей") + vf("этот", "этого", "этой") + vf("тот", "того", "той")
            + vf("такой", "такого", "такой") + vf("другой", "другого", "другой") + vf("один", "одного", "одной")
            + vf("врач", "врача") + vf("остановка", "остановка")),
    exercises=[
        fb("Здесь нет ___ ключа'. (my)", ["моего'", "мой", "мое'й", "моему'"], "моего'",
           "Masculine genitive: моего'.", tr="My key isn't here.", lemma="мой"),
        fb("Здесь нет ___ су'мки. (your)", ["твое'й", "твоего'", "твоя'", "твою'"], "твое'й",
           "Feminine genitive: твое'й.", tr="Your bag isn't here.", lemma="твой"),
        fb("Э'то кни'га ___ сестры'. (our)", ["на'шей", "на'шего", "на'ша", "на'шу"], "на'шей",
           "Feminine genitive: на'шей.", tr="This is our sister's book.", lemma="наш"),
        fb("Здесь нет ___ ма'льчика. (that)", ["того'", "тот", "той", "та"], "того'",
           "Masculine genitive: того'.", tr="That boy isn't here.", lemma="тот"),
        fb("Здесь нет ___ де'вушки. (that)", ["той", "того'", "та", "ту"], "той",
           "Feminine genitive: той.", tr="That girl isn't here.", lemma="тот"),
        fb("___ ку'ртки здесь нет? (whose)", ["Чьей", "Чья", "Чьего'", "Чью"], "Чьей",
           "Feminine genitive: чьей.", tr="Whose jacket isn't here?", lemma="чей"),
        fb("О'коло ___ до'ма остано'вка? (which)", ["како'го", "како'й", "како'е", "каки'х"], "како'го",
           "Masculine genitive: како'го.", tr="Near which building is the bus stop?", lemma="какой"),
        fb("У ___ студе'нта нет словаря'. (one)", ["одного'", "оди'н", "одно'й", "одному'"], "одного'",
           "Masculine genitive: одного'.", tr="One student has no dictionary.", lemma="один"),
        mc("Which form is “of this” (feminine)?", ["э'той", "э'того", "э'та", "э'ту"], "э'той", "Э'той."),
        mc("Which words never change?", ["его', её, их", "мой, твой, наш", "како'й, чей", "тот, та, то"], "его', её, их",
           "The possessives for “his, her, their” are fixed."),
    ],
)

# ---------------------------------------------------------------------------- 123
L123 = lesson(
    "What is the date?",
    "Како'е сего'дня число'? — Сего'дня тре'тье ию'ня.",
    requires=["число", "январь", "май", "июнь", "ноябрь"],
    cards=[
        card("The months in the genitive",
             "When a month follows the date, it goes in the genitive: тре'тье ию'ня (the third of June). Masculine "
             "months take -а or, after ь and й, -я.",
             tables=[table(
                 ["Month", "Genitive"],
                 [["янва'рь", "январ{я'}"], ["февра'ль", "феврал{я'}"], ["март", "ма'рт{а}"],
                  ["апре'ль", "апре'л{я}"], ["май", "ма'{я}"], ["ию'нь", "ию'н{я}"],
                  ["ию'ль", "ию'л{я}"], ["а'вгуст", "а'вгуст{а}"], ["сентя'брь", "сентябр{я'}"],
                  ["октя'брь", "октябр{я'}"], ["ноя'брь", "ноябр{я'}"], ["дека'брь", "декабр{я'}"]])]),
        card("Asking and answering",
             "The question is Како'е сего'дня число'? The answer is an ordinal number in the neuter nominative "
             "(because число' is neuter), then the month in the genitive. In the future бу'дет can be left out, but "
             "in the past бы'ло cannot.",
             tables=[table(
                 ["Question", "Answer"],
                 [["Како'е сего'дня число'?", "Сего'дня тре'тье ию'ня."],
                  ["Како'е вчера' бы'ло число'?", "Вчера' бы'ло девятна'дцатое января'."],
                  ["Како'е за'втра (бу'дет) число'?", "За'втра (бу'дет) два'дцать шесто'е ноября'."]])],
             examples=[
                 ex("Сего'дня пя'тое ма'я.", "Today is the fifth of May.", "пя'тое ма'я"),
                 ex("Вчера' бы'ло пе'рвое ма'рта.", "Yesterday was the first of March.", "бы'ло"),
                 ex("За'втра два'дцать пя'тое декабря'.", "Tomorrow is the twenty-fifth of December.", "декабря'"),
             ]),
    ],
    verify=(vf("январь", "января") + vf("февраль", "февраля") + vf("март", "марта") + vf("апрель", "апреля")
            + vf("май", "мая") + vf("июнь", "июня") + vf("июль", "июля") + vf("август", "августа")
            + vf("сентябрь", "сентября") + vf("октябрь", "октября") + vf("ноябрь", "ноября")
            + vf("декабрь", "декабря") + vf("третий", "третье") + vf("девятнадцатый", "девятнадцатое")
            + vf("шестой", "шестое") + vf("пятый", "пятое") + vf("первый", "первое")),
    exercises=[
        fb("Сего'дня тре'тье ___.", ["ию'ня", "ию'нь", "ию'не", "ию'ню"], "ию'ня",
           "The month after the date: genitive.", tr="Today is the third of June.", lemma="июнь"),
        fb("Вчера' бы'ло девятна'дцатое ___.", ["января'", "янва'рь", "январе'", "январю'"], "января'",
           "Genitive: января'.", tr="Yesterday was the nineteenth of January.", lemma="январь"),
        fb("За'втра два'дцать шесто'е ___.", ["ноября'", "ноя'брь", "ноябре'", "ноябрю'"], "ноября'",
           "Genitive: ноября'.", tr="Tomorrow is the twenty-sixth of November.", lemma="ноябрь"),
        fb("Сего'дня пя'тое ___.", ["ма'я", "май", "ма'е", "ма'ю"], "ма'я",
           "Genitive of май: ма'я.", tr="Today is the fifth of May.", lemma="май"),
        fb("Како'е сего'дня ___?", ["число'", "числа'", "числу'", "числе'"], "число'",
           "The question asks about число'.", tr="What is today's date?", lemma="число"),
        fb("Сего'дня ___ ма'рта. (the first)", ["пе'рвое", "пе'рвый", "пе'рвая", "пе'рвого"], "пе'рвое",
           "Neuter, like число'.", tr="Today is the first of March."),
        mc("Which question asks for the date?",
           ["Како'е сего'дня число'?", "Кото'рый час?", "Како'й сего'дня день?", "Ско'лько сего'дня?"],
           "Како'е сего'дня число'?", "Число' = date."),
        mc("Which sentence is correct?",
           ["Вчера' бы'ло пя'тое ма'я.", "Вчера' пя'тое ма'я.", "Вчера' бу'дет пя'тое ма'я.", "Вчера' пя'тый ма'я."],
           "Вчера' бы'ло пя'тое ма'я.", "In the past бы'ло cannot be left out."),
        mc("What is ию'ль in the genitive?", ["ию'ля", "ию'ль", "ию'лю", "ию'ле"], "ию'ля", "-ь becomes -я."),
    ],
)

# ---------------------------------------------------------------------------- 124
L124 = lesson(
    "On what date? Когда́ ты роди́лся?",
    "Четвёртого ма'я. Я роди'лся тре'тьего а'вгуста.",
    requires=["родиться", "число", "год", "месяц", "май"],
    cards=[
        card("On a date: the ordinal in the genitive",
             "To say that something happens on a date, put the ordinal in the genitive (masculine, like числа') and "
             "the month in the genitive. There is no preposition. The question is Како'го числа'? or Когда'?",
             tables=[table(
                 ["Date", "On the …"],
                 [["пе'рвое", "пе'рв{ого}"],
                  ["второ'е", "втор{о'го}"],
                  ["тре'тье", "тре'ть{его}"],
                  ["четвёртое", "четвёрт{ого}"],
                  ["пя'тое", "пя'т{ого}"],
                  ["деся'тое", "деся'т{ого}"],
                  ["двадца'тое", "двадца'т{ого}"],
                  ["два'дцать пе'рвое", "два'дцать пе'рв{ого}"]])]),
        card("Dates in sentences, and years",
             "Years work the same way: the last word of the ordinal and the word го'да are in the genitive. So "
             "1982 on a birthday is ты'сяча девятьсо'т во'семьдесят второ'го го'да. To say where something happened "
             "you still say в + the prepositional (в 1982 году'), but for a full date use the genitive.",
             examples=[
                 ex("Како'го числа' наш экза'мен? — Четвёртого ма'я.", "On what date is our exam? — On the fourth of May.", "Четвёртого ма'я"),
                 ex("Когда' мы е'дем в Москву'? — Мы е'дем пя'того января'.", "When are we going to Moscow? — On the fifth of January.", "пя'того января'"),
                 ex("Когда' ты роди'лся? — Я роди'лся тре'тьего а'вгуста.", "When were you born? — On the third of August.", "тре'тьего а'вгуста"),
                 ex("Она' родила'сь двадца'того апре'ля ты'сяча девятьсо'т девяно'сто пе'рвого го'да.",
                    "She was born on the twentieth of April, 1991.", "двадца'того апре'ля"),
                 ex("Мой день рожде'ния деся'того октября'.", "My birthday is on the tenth of October.", "деся'того октября'"),
             ]),
    ],
    verify=(vf("первый", "первого") + vf("второй", "второго") + vf("третий", "третьего")
            + vf("четвёртый", "четвёртого") + vf("пятый", "пятого") + vf("десятый", "десятого")
            + vf("двадцатый", "двадцатого") + vf("родиться", "родился", "родилась", "родились")
            + vf("июнь", "июня") + vf("январь", "января") + vf("август", "августа") + vf("апрель", "апреля")
            + vf("октябрь", "октября") + vf("тысяча", "тысяча") + vf("девятьсот", "девятьсот")
            + vf("девяносто", "девяносто") + vf("рождение", "рождения") + vf("год", "года")),
    exercises=[
        fb("Како'го ___ наш экза'мен?", ["числа'", "число'", "числу'", "числе'"], "числа'",
           "Како'го числа' = on what date?", tr="On what date is our exam?", lemma="число"),
        fb("Наш экза'мен четвёртого ___.", ["ма'я", "май", "ма'е", "ма'ю"], "ма'я",
           "The month: genitive.", tr="Our exam is on the fourth of May.", lemma="май"),
        fb("Мы е'дем в Москву' пя'того ___.", ["января'", "янва'рь", "январе'", "январю'"], "января'",
           "The month: genitive.", tr="We are going to Moscow on the fifth of January.", lemma="январь"),
        fb("Я роди'лся тре'тьего ___. (August)", ["а'вгуста", "а'вгуст", "а'вгусте", "а'вгусту"], "а'вгуста",
           "The month: genitive.", tr="I was born on the third of August.", lemma="август"),
        fb("Я родила'сь ___ ма'рта. (the first)", ["пе'рвого", "пе'рвое", "пе'рвый", "пе'рвому"], "пе'рвого",
           "On a date: the ordinal in the genitive.", tr="I was born on the first of March.", lemma="первый"),
        fb("Мы пое'дем деся'того ___. (October)", ["октября'", "октя'брь", "октябре'", "октябрю'"], "октября'",
           "The month: genitive.", tr="We will go on the tenth of October.", lemma="октябрь"),
        fb("Ма'ша ___ деся'того ию'ня. (was born)", ["родила'сь", "роди'лся", "родили'сь", "роди'лось"], "родила'сь",
           "Feminine past: родила'сь.", tr="Masha was born on the tenth of June.", lemma="родиться"),
        mc("Which phrase means “on the ninth of June”?",
           ["девя'того ию'ня", "девя'тое ию'ня", "девя'тый ию'нь", "девя'том ию'не"], "девя'того ию'ня",
           "Genitive + genitive."),
        mc("Is there a preposition before a date?", ["no", "в", "на", "до"], "no",
           "Say Четвёртого ма'я, not в четвёртого ма'я.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 125
L125 = lesson(
    "Tall, short, slim: height and build",
    "Он высо'кого ро'ста. Она' стро'йная.",
    requires=["высокий", "низкий", "средний", "сильный", "слабый"],
    cards=[
        card("How tall? Како́го ро́ста?",
             "To describe someone's height, use рост in the genitive after a genitive adjective: высо'кого ро'ста "
             "(tall), сре'днего ро'ста (average height), ни'зкого ро'ста (short). The question is Како'го он ро'ста? "
             "The adjectives show the endings you have just learned.",
             tables=[table(
                 ["Question", "Answer"],
                 [["Како'го он ро'ста?", "Он высо'кого ро'ста."],
                  ["Како'го она' ро'ста?", "Она' сре'днего ро'ста."],
                  ["Како'го ро'ста ваш брат?", "Он ни'зкого ро'ста."]])]),
        card("Build and appearance",
             "Pairs of opposite adjectives help you describe a person. Use вне'шность (appearance) for the whole "
             "picture and телосложе'ние for build. Ask Как он вы'глядит? (What does he look like?).",
             tables=[table(
                 ["Adjective", "Opposite"],
                 [["высо'кий (tall)", "ни'зкий (short)"],
                  ["си'льный (strong)", "сла'бый (weak)"],
                  ["худо'й (skinny)", "по'лный (heavyset)"],
                  ["широ'кий (wide)", "у'зкий (narrow)"],
                  ["дли'нный (long)", "коро'ткий (short)"]],
                 note="Стро'йный means slim, in a pleasant way.")],
             examples=[
                 ex("Мой брат высо'кого ро'ста и о'чень си'льный.", "My brother is tall and very strong.", "высо'кого ро'ста"),
                 ex("Она' ни'зкого ро'ста, но стро'йная.", "She is short but slim.", "ни'зкого ро'ста"),
                 ex("Кака'я у него' вне'шность?", "What does he look like?", "вне'шность"),
                 ex("Э'тот челове'к сре'днего ро'ста.", "This person is of average height.", "сре'днего ро'ста"),
             ]),
    ],
    verify=(vf("рост", "роста") + vf("высокий", "высокого") + vf("средний", "среднего") + vf("низкий", "низкого")
            + vf("сильный", "сильный") + vf("слабый", "слабый") + vf("худой", "худой") + vf("полный", "полный")
            + vf("широкий", "широкий") + vf("узкий", "узкий") + vf("длинный", "длинный")
            + vf("короткий", "короткий") + vf("стройный", "стройная") + vf("внешность", "внешность")),
    exercises=[
        fb("Он высо'кого ___.", ["ро'ста", "рост", "ро'сту", "ро'сте"], "ро'ста",
           "Height: ро'ста in the genitive.", tr="He is tall.", lemma="рост"),
        fb("Мой брат ___ ро'ста. (tall)", ["высо'кого", "высо'кий", "высо'кой", "высо'кому"], "высо'кого",
           "Genitive: -ого.", tr="My brother is tall.", lemma="высокий"),
        fb("Она' ___ ро'ста. (short)", ["ни'зкого", "ни'зкая", "ни'зкий", "ни'зкой"], "ни'зкого",
           "Genitive of quality: ро'ста needs -ого.", tr="She is short.", lemma="низкий"),
        fb("Как он вы'глядит? — Он сре'днего ___.", ["ро'ста", "рост", "ро'сту", "ро'сте"], "ро'ста",
           "Genitive.", tr="What does he look like? — He is of average height.", lemma="рост"),
        mc("What is the opposite of высо'кий?", ["ни'зкий", "широ'кий", "сла'бый", "дли'нный"], "ни'зкий", "Tall ↔ short."),
        mc("What is the opposite of си'льный?", ["сла'бый", "у'зкий", "ни'зкий", "коро'ткий"], "сла'бый", "Strong ↔ weak."),
        mc("Which word means “heavyset”?", ["по'лный", "стро'йный", "высо'кий", "сла'бый"], "по'лный", "По'лный."),
        mc("Which question asks about height?",
           ["Како'го он ро'ста?", "Какой он ро'сте?", "Что он ро'ста?", "Чей он ро'ст?"], "Како'го он ро'ста?",
           "Како'го ро'ста?"),
    ],
)

# ---------------------------------------------------------------------------- 126
L126 = lesson(
    "Hair, eyes and face",
    "У неё дли'нные све'тлые во'лосы и ка'рие глаза'.",
    requires=["глаз", "борода", "лицо", "красивый", "длинный"],
    cards=[
        card("Describing with у + genitive",
             "To describe someone's features, use у + the person in the genitive (у него', у неё) and the feature "
             "as the subject: У неё дли'нные во'лосы. The word во'лосы (hair) is plural in Russian. Ask Каки'е у "
             "него' во'лосы? (What kind of hair does he have?).",
             tables=[table(
                 ["Hair", "Meaning"],
                 [["тёмные", "dark"], ["све'тлые", "light, fair"], ["ру'сые", "dark blond"],
                  ["ры'жие", "red, ginger"], ["седы'е", "grey"], ["дли'нные", "long"], ["коро'ткие", "short"]])]),
        card("Eyes and face",
             "Ask Како'го цве'та у неё глаза'? (What colour are her eyes?). The answer is a plural adjective. "
             "Other parts of the face: лицо', нос, рот, борода', усы'.",
             tables=[table(
                 ["Colour of eyes", "Meaning"],
                 [["ка'рие", "brown"], ["голубы'е", "light blue"], ["зелёные", "green"], ["се'рые", "grey"]])],
             examples=[
                 ex("У неё дли'нные све'тлые во'лосы.", "She has long fair hair.", "дли'нные све'тлые во'лосы"),
                 ex("У него' тёмные во'лосы и ка'рие глаза'.", "He has dark hair and brown eyes.", "ка'рие глаза'"),
                 ex("Како'го цве'та у неё глаза'? — Голубы'е.", "What colour are her eyes? — Blue.", "Како'го цве'та"),
                 ex("У него' борода' и усы'.", "He has a beard and a moustache.", "борода'"),
                 ex("У ма'ленького ма'льчика кру'глое лицо'.", "The little boy has a round face.", "лицо'"),
             ]),
    ],
    verify=(vf("волосы", "волосы") + vf("тёмный", "тёмные") + vf("светлый", "светлые") + vf("русый", "русые")
            + vf("рыжий", "рыжие") + vf("седой", "седые") + vf("длинный", "длинные") + vf("короткий", "короткие")
            + vf("карий", "карие") + vf("голубой", "голубые") + vf("зелёный", "зелёные") + vf("серый", "серые")
            + vf("цвет", "цвета") + vf("глаз", "глаза") + vf("борода", "борода") + vf("усы", "усы")
            + vf("лицо", "лицо") + vf("круглый", "круглое") + vf("маленький", "маленького")),
    exercises=[
        fb("У неё дли'нные ___ во'лосы. (fair)", ["све'тлые", "све'тлый", "све'тлая", "све'тлое"], "све'тлые",
           "Во'лосы is plural.", tr="She has long fair hair.", lemma="светлый"),
        fb("У него' ___ глаза'. (brown)", ["ка'рие", "ка'рий", "ка'рая", "ка'рое"], "ка'рие",
           "Глаза' is plural.", tr="He has brown eyes.", lemma="карий"),
        fb("Како'го ___ у неё глаза'?", ["цве'та", "цвет", "цве'ту", "цве'те"], "цве'та",
           "Како'го цве'та = what colour?", tr="What colour are her eyes?", lemma="цвет"),
        fb("У него' ___ и усы'. (a beard)", ["борода'", "бороду'", "бороды'", "бороде'"], "борода'",
           "Subject: nominative.", tr="He has a beard and a moustache.", lemma="борода"),
        fb("У ма'льчика кру'глое ___.", ["лицо'", "лица'", "лицу'", "лице'"], "лицо'",
           "Subject: nominative.", tr="The boy has a round face.", lemma="лицо"),
        mc("Which means “grey hair”?", ["седы'е во'лосы", "ры'жие во'лосы", "ка'рие во'лосы", "дли'нные глаза'"], "седы'е во'лосы",
           "Седо'й = grey-haired."),
        mc("Which question asks about eye colour?",
           ["Како'го цве'та у неё глаза'?", "Ско'лько у неё глаз?", "Что у неё глаза'?", "Чей у неё глаза'?"],
           "Како'го цве'та у неё глаза'?", "Како'го цве'та?"),
        mc("Is во'лосы singular or plural?", ["plural", "singular", "both", "neither"], "plural",
           "У него' тёмные во'лосы.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 127
L127 = lesson(
    "The body: head, arm, leg, eye",
    "Две руки', две ноги', два глаза', два у'ха",
    requires=["голова", "рука", "нога", "нос", "рот"],
    cards=[
        card("Parts of the body",
             "Several parts of the body have an irregular plural. Learn them in pairs. Глаз, ухо and плечо are "
             "neuter or masculine in the singular and change completely in the plural.",
             tables=[table(
                 ["Singular", "Plural"],
                 [["голова'", "го'ловы"], ["рука'", "ру'ки"], ["нога'", "но'ги"], ["глаз", "глаза'"],
                  ["у'хо", "у'ши"], ["плечо'", "пле'чи"], ["лицо'", "ли'ца"], ["те'ло", "тела'"],
                  ["нос", "носы'"], ["рот", "рты"]],
                 note="Prepositional: в глазу', на носу', во рту.")]),
        card("Counting body parts",
             "After два, три and четы'ре the noun takes the genitive singular: две руки', две ноги', два глаза', два "
             "уха'. This is the rule from lesson 98.",
             examples=[
                 ex("У челове'ка две руки' и две ноги'.", "A person has two arms and two legs.", "две руки'"),
                 ex("У нас два глаза' и два уха'.", "We have two eyes and two ears.", "два глаза'"),
                 ex("У меня' боли'т голова'.", "I have a headache.", "голова'"),
                 ex("У него' широ'кие пле'чи.", "He has broad shoulders.", "пле'чи"),
                 ex("Что у тебя' на носу'?", "What do you have on your nose?", "на носу'"),
             ]),
    ],
    verify=(vf("голова", "головы", "голова") + vf("рука", "руки") + vf("нога", "ноги") + vf("глаз", "глаза")
            + vf("ухо", "уха", "уши") + vf("плечо", "плечи") + vf("лицо", "лица") + vf("тело", "тела")
            + vf("нос", "носы", "носу") + vf("рот", "рты") + vf("человек", "человека") + vf("болеть", "болит")),
    exercises=[
        fb("У челове'ка две ___.", ["руки'", "рука'", "руку'", "руке'"], "руки'",
           "После две: genitive singular.", tr="A person has two arms.", lemma="рука"),
        fb("У нас два ___.", ["глаза'", "глаз", "глазу'", "глазе'"], "глаза'",
           "После два: genitive singular.", tr="We have two eyes.", lemma="глаз"),
        fb("У него' две ___.", ["ноги'", "нога'", "ногу'", "ноге'"], "ноги'",
           "После две: genitive singular.", tr="He has two legs.", lemma="нога"),
        fb("Что у тебя' на ___? (nose)", ["носу'", "нос", "носа'", "носе'"], "носу'",
           "The prepositional: на носу'.", tr="What do you have on your nose?", lemma="нос"),
        fb("Во ___ у неё конфе'та. (mouth)", ["рту", "рот", "рта", "рте"], "рту",
           "The prepositional: во рту.", tr="She has a candy in her mouth.", lemma="рот"),
        mc("What is the plural of у'хо?", ["у'ши", "у'хи", "уха'", "у'хо"], "у'ши", "У'хо → у'ши."),
        mc("What is the plural of глаз?", ["глаза'", "глазы'", "глази", "глазы"], "глаза'", "Глаз → глаза'."),
        mc("What is the plural of рука'?", ["ру'ки", "руки'", "рука'", "ру'к"], "ру'ки", "Рука' → ру'ки."),
    ],
)

# ---------------------------------------------------------------------------- 128
L128 = lesson(
    "What does she look like? And what is she like?",
    "Как она' вы'глядит? Она' похо'жа на ма'му.",
    requires=["выглядеть", "умный", "добрый", "весёлый", "красивый"],
    cards=[
        card("To look: вы'глядеть, похо́ж на …",
             "Вы'глядеть is an imperfective verb (я вы'гляжу, ты вы'глядишь …). Похо'ж (похо'жа, похо'жи) means "
             "similar; use it with на + the accusative: Она' похо'жа на ма'му.",
             tables=[table(
                 ["Who", "вы'глядеть"],
                 [["я", "вы'гляжу"], ["ты", "вы'глядишь"], ["он, она'", "вы'глядит"],
                  ["мы", "вы'глядим"], ["вы", "вы'глядите"], ["они'", "вы'глядят"]]),
                 table(
                 ["Who", "похо́ж"],
                 [["он", "похо'ж"], ["она'", "похо'жа"], ["они'", "похо'жи"]])],
             examples=[
                 ex("Как она' вы'глядит?", "What does she look like?", "вы'глядит"),
                 ex("Она' вы'глядит о'чень хорошо'.", "She looks very good.", "вы'глядит"),
                 ex("Она' похо'жа на ма'му.", "She looks like her mom.", "похо'жа на"),
                 ex("Он похо'ж на отца'.", "He looks like his father.", "похо'ж на"),
                 ex("Мы с сестро'й о'чень похо'жи.", "My sister and I look very much alike.", "похо'жи"),
             ]),
        card("Character",
             "Use these adjectives to say what someone is like. They agree with the person in gender and number.",
             tables=[table(
                 ["Masculine", "Feminine", "Meaning"],
                 [["у'мный", "у'мная", "smart"], ["глу'пый", "глу'пая", "silly, stupid"],
                  ["до'брый", "до'брая", "kind"], ["весёлый", "весёлая", "cheerful"],
                  ["ску'чный", "ску'чная", "boring"], ["стро'гий", "стро'гая", "strict"],
                  ["гру'бый", "гру'бая", "rude"], ["просто'й", "проста'я", "simple, down-to-earth"],
                  ["симпати'чный", "симпати'чная", "cute"]])]),
    ],
    verify=(vf("вы'глядеть", "вы'гляжу", "вы'глядишь", "вы'глядит", "вы'глядим", "вы'глядите", "вы'глядят")
            + vf("похожий", "похож", "похожа", "похожи") + vf("мама", "маму") + vf("отец", "отца")
            + vf("умный", "умная") + vf("глупый", "глупая") + vf("добрый", "добрая") + vf("весёлый", "весёлая")
            + vf("скучный", "скучная") + vf("строгий", "строгая") + vf("грубый", "грубая")
            + vf("простой", "простая") + vf("симпатичный", "симпатичная")),
    exercises=[
        fb("Она' ___ на ма'му. (looks like)", ["похо'жа", "похо'ж", "похо'жи", "похо'же"], "похо'жа",
           "Feminine: похо'жа.", tr="She looks like her mom."),
        fb("Он похо'ж на ___. (father)", ["отца'", "оте'ц", "отцу'", "отце'"], "отца'",
           "На + accusative; for an animate masculine noun it looks like the genitive.", tr="He looks like his father.", lemma="отец"),
        fb("Мы с сестро'й о'чень ___.", ["похо'жи", "похо'ж", "похо'жа", "похо'же"], "похо'жи",
           "Plural: похо'жи.", tr="My sister and I look very much alike."),
        fb("Как он ___?", ["вы'глядит", "вы'глядишь", "вы'гляжу", "вы'глядят"], "вы'глядит",
           "Он takes -ит.", tr="What does he look like?", lemma="выглядеть"),
        fb("Я сего'дня ___ о'чень хорошо'.", ["вы'гляжу", "вы'глядит", "вы'глядишь", "вы'глядим"], "вы'гляжу",
           "Я takes вы'гляжу.", tr="I look very good today.", lemma="выглядеть"),
        mc("Which adjective means “kind”?", ["до'брый", "гру'бый", "глу'пый", "ску'чный"], "до'брый", "До'брый = kind."),
        mc("Which adjective means “rude”?", ["гру'бый", "до'брый", "весёлый", "у'мный"], "гру'бый", "Гру'бый = rude."),
        mc("Which question asks what someone looks like?",
           ["Как она' вы'глядит?", "Где она' вы'глядит?", "Кто она' вы'глядит?", "Что она' вы'глядит?"], "Как она' вы'глядит?",
           "Как вы'глядит …?"),
    ],
)

# ---------------------------------------------------------------------------- 129
L129 = lesson(
    "When, while, as soon as: which aspect?",
    "Пока' я смотре'ла телеви'зор, он пригото'вил у'жин.",
    requires=["когда", "пока", "смотреть", "приготовить", "начать"],
    cards=[
        card("Three patterns",
             "Clauses with когда' (when), пока' (while) and как то'лько (as soon as) say when the main action "
             "happens. The aspect depends on how the two actions relate. At the same time: both verbs are "
             "imperfective. One action goes on while another happens: imperfective in the когда'/пока' clause, "
             "perfective in the main clause. One action follows another: both are perfective.",
             tables=[table(
                 ["The two actions", "Subordinate clause", "Main clause"],
                 [["at the same time", "imperfective", "imperfective"],
                  ["one happens during the other", "imperfective", "perfective"],
                  ["one after the other", "perfective", "perfective"]])]),
        card("Examples",
             "Compare the three sentences. In the first the two activities run in parallel, in the second the "
             "dinner is cooked while the person watches TV, and in the third the dinner starts only after the film "
             "is over.",
             examples=[
                 ex("Пока' мой брат чита'л, я смотре'ла телеви'зор.",
                    "While my brother was reading, I was watching TV.", "чита'л, я смотре'ла"),
                 ex("Пока' я смотре'ла телеви'зор, он пригото'вил у'жин и убра'л ко'мнату.",
                    "While I was watching TV, he cooked dinner and cleaned the room.", "смотре'ла"),
                 ex("Когда' я посмотре'ла фильм, я начала' гото'вить у'жин.",
                    "When I had watched the film, I started cooking dinner.", "посмотре'ла"),
                 ex("Как то'лько я посмотрю' фильм, я начну' гото'вить у'жин.",
                    "As soon as I have watched the film, I will start cooking dinner.", "посмотрю'"),
                 ex("Пока' я бу'ду смотре'ть телеви'зор, он пригото'вит у'жин.",
                    "While I watch TV, he will cook dinner.", "бу'ду смотре'ть"),
             ]),
    ],
    verify=(vf("смотреть", "смотрела") + vf("посмотреть", "посмотрела", "посмотрю") + vf("читать", "читал")
            + vf("приготовить", "приготовил", "приготовит") + vf("убрать", "убрал")
            + vf("начать", "начала", "начну") + vf("готовить", "готовить") + vf("телевизор", "телевизор")
            + vf("ужин", "ужин")),
    exercises=[
        fb("Пока' мой брат чита'л, я ___ телеви'зор.", ["смотре'ла", "посмотре'ла"], "смотре'ла",
           "Two parallel actions: both imperfective.", tr="While my brother was reading, I was watching TV."),
        fb("Пока' я смотре'ла телеви'зор, он ___ у'жин.", ["пригото'вил", "гото'вил"], "пригото'вил",
           "One action is completed during the other: perfective in the main clause.",
           tr="While I was watching TV, he cooked dinner."),
        fb("Когда' я ___ фильм, я начала' гото'вить у'жин. (finished it)", ["посмотре'ла", "смотре'ла"], "посмотре'ла",
           "One after the other: both perfective.", tr="When I had watched the film, I started cooking dinner."),
        fb("Как то'лько я ___ фильм, я начну' гото'вить у'жин.", ["посмотрю'", "бу'ду смотре'ть"], "посмотрю'",
           "One after the other: perfective.", tr="As soon as I have watched the film, I will start cooking dinner."),
        fb("Пока' я бу'ду смотре'ть телеви'зор, он ___ у'жин и уберёт ко'мнату.", ["пригото'вит", "бу'дет гото'вить"],
           "пригото'вит", "Completed during the other: perfective.", tr="While I watch TV, he will cook dinner and clean the room."),
        mc("Which aspects do two parallel actions take?",
           ["both imperfective", "both perfective", "imperfective, then perfective", "perfective, then imperfective"],
           "both imperfective", "At the same time.", order=True),
        mc("Which aspects do two actions that follow each other take?",
           ["both perfective", "both imperfective", "imperfective, then perfective", "perfective, then imperfective"],
           "both perfective", "One after the other.", order=True),
        mc("Which word means “as soon as”?", ["как то'лько", "пока'", "е'сли", "хотя'"], "как то'лько", "Как то'лько."),
    ],
)

# ---------------------------------------------------------------------------- 130
L130 = lesson(
    "He asked who was at home",
    "Скажи', пожа'луйста, кака'я за'втра бу'дет пого'да.",
    requires=["кто", "что", "какой", "который", "чей"],
    cards=[
        card("A question inside a sentence",
             "A question word can connect two clauses. Put a comma before it, keep the word order of the "
             "question, and use the same tense as in the original question: Кто до'ма? → Он спроси'л, кто "
             "до'ма. Question words that work this way are кто, что, како'й, кото'рый, чей and ско'лько.",
             tables=[table(
                 ["Direct question", "Inside a sentence"],
                 [["Кто до'ма?", "Он спроси'л, кто до'ма."],
                  ["Что ты купи'ла?", "Я хочу' знать, что ты купи'ла."],
                  ["Кака'я за'втра бу'дет пого'да?", "Скажи', пожа'луйста, кака'я за'втра бу'дет пого'да."],
                  ["Кото'рый час?", "Я хочу' знать, кото'рый час."],
                  ["Чьи э'то перча'тки?", "Ты не зна'ешь, чьи э'то перча'тки?"],
                  ["Ско'лько вре'мени вы бу'дете здесь?", "Скажи'те, ско'лько вре'мени вы бу'дете здесь."]])],
             examples=[
                 ex("Я не зна'ю, кто э'то.", "I don't know who this is.", "кто"),
                 ex("Он спроси'л, что мы де'лаем.", "He asked what we were doing.", "что"),
                 ex("Скажи', кото'рый час.", "Tell me what time it is.", "кото'рый"),
             ]),
    ],
    verify=(vf("спросить", "спросил") + vf("купить", "купила") + vf("перчатка", "перчатки")
            + vf("погода", "погода") + vf("знать", "знаешь") + vf("хотеть", "хочу")),
    exercises=[
        fb("Он спроси'л, ___ до'ма. (who)", ["кто", "что", "чей", "ско'лько"], "кто", "Кто asks about a person.",
           tr="He asked who was at home."),
        fb("Я хочу' знать, ___ ты купи'ла. (what)", ["что", "кто", "како'й", "чей"], "что", "Что asks about a thing.",
           tr="I want to know what you bought."),
        fb("Ты не зна'ешь, ___ э'то перча'тки? (whose)", ["чьи", "чей", "чья", "чьё"], "чьи",
           "Перча'тки is plural: чьи.", tr="Do you know whose gloves these are?"),
        fb("Скажи', ___ за'втра бу'дет пого'да. (what kind)", ["кака'я", "како'й", "како'е", "каки'е"], "кака'я",
           "Пого'да is feminine: кака'я.", tr="Tell me what kind of weather it will be tomorrow."),
        fb("Скажи'те, ___ вре'мени вы бу'дете здесь. (how much)", ["ско'лько", "мно'го", "кото'рый", "чей"], "ско'лько",
           "Ско'лько + genitive.", tr="Tell me how long you will be here."),
        fb("Я хочу' знать, ___ час. (what)", ["кото'рый", "кото'рая", "кото'рое", "кото'рые"], "кото'рый",
           "Кото'рый час? — час is masculine.", tr="I want to know what time it is."),
        mc("Where does the comma go?",
           ["Он спроси'л, кто до'ма.", "Он спроси'л кто, до'ма.", "Он, спроси'л кто до'ма.", "Он спроси'л кто до'ма,"],
           "Он спроси'л, кто до'ма.", "A comma goes before the question word."),
        mc("Does the tense change in the indirect question?", ["no, it stays the same", "yes, always the past", "yes, always the future", "it disappears"],
           "no, it stays the same", "The tense of the original question stays.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 131
L131 = lesson(
    "The one who, the thing that: тот, кто and то, что",
    "Я зна'ю того', кто написа'л э'тот расска'з.",
    requires=["тот", "такой", "который", "кто", "что"],
    cards=[
        card("Тот, кто and то, что",
             "To refer to a person or thing in general, use a demonstrative word in the main clause and a question "
             "word in the second clause. If the demonstrative has no noun, use кто for a person and что for a "
             "thing: Я зна'ю того', кто написа'л э'тот расска'з. То, что я купи'ла, не мо'дно.",
             tables=[table(
                 ["Main clause", "Second clause", "Example"],
                 [["тот (that one)", "кто", "Тот, кто написа'л э'тот расска'з, живёт здесь."],
                  ["то (that thing)", "что", "Я ви'дела то, что вы купи'ли."]])]),
        card("With a noun: кото́рый; with тако́й: како́й",
             "If the main clause has a noun, use кото'рый and make it agree with the noun in gender and number. "
             "If it has тако'й, use како'й. The case of each pronoun depends on its own clause.",
             tables=[table(
                 ["Noun", "кото́рый", "Example"],
                 [["пиджа'к (m)", "кото'рый", "тот пиджа'к, кото'рый я купи'л"],
                  ["ю'бка (f)", "кото'рая", "та ю'бка, кото'рая лежи'т здесь"],
                  ["пла'тье (n)", "кото'рое", "то пла'тье, кото'рое я ви'дел"],
                  ["ве'щи (pl)", "кото'рые", "те ве'щи, кото'рые я купи'ла"]])],
             examples=[
                 ex("Я люблю' таки'е кни'ги, каки'е лю'бите вы.", "I like the kind of books you like.", "таки'е кни'ги, каки'е"),
                 ex("Вот тот но'вый рюкза'к, кото'рый я вчера' купи'л.", "Here is the new backpack that I bought yesterday.", "кото'рый"),
                 ex("Он запла'тит сто'лько, ско'лько вы хоти'те.", "He will pay as much as you want.", "сто'лько, ско'лько"),
                 ex("То, что я купи'ла, уже' не мо'дно.", "What I bought is no longer in fashion.", "То, что"),
             ]),
    ],
    verify=(vf("написать", "написал") + vf("купить", "купила", "купил") + vf("видеть", "видела")
            + vf("любить", "любите") + vf("заплатить", "заплатит") + vf("хотеть", "хотите")
            + vf("жить", "живёт") + vf("модный", "модно") + vf("пиджак", "пиджак") + vf("юбка", "юбка")
            + vf("платье", "платье") + vf("вещь", "вещи") + vf("рассказ", "рассказ")),
    exercises=[
        fb("Я зна'ю того', ___ написа'л э'тот расска'з.", ["кто", "что", "кото'рый", "како'й"], "кто",
           "Тот without a noun, a person: кто.", tr="I know the person who wrote this story."),
        fb("Я ви'дела то, ___ вы купи'ли.", ["что", "кто", "кото'рый", "како'й"], "что",
           "То without a noun, a thing: что.", tr="I saw what you bought."),
        fb("Вот тот но'вый рюкза'к, ___ я вчера' купи'л.", ["кото'рый", "что", "кто", "кото'рая"], "кото'рый",
           "A masculine noun: кото'рый.", tr="Here is the new backpack that I bought yesterday."),
        fb("Вот та ю'бка, ___ я вчера' купи'ла.", ["кото'рую", "кото'рая", "кото'рый", "что"], "кото'рую",
           "Feminine, and it is the object of купи'ла: accusative.", tr="Here is the skirt I bought yesterday."),
        fb("Я люблю' таки'е кни'ги, ___ лю'бите вы.", ["каки'е", "кото'рые", "кто", "что"], "каки'е",
           "Таки'е → каки'е.", tr="I like the kind of books you like."),
        fb("Он запла'тит сто'лько, ___ вы хоти'те.", ["ско'лько", "кото'рый", "кто", "како'й"], "ско'лько",
           "Сто'лько → ско'лько.", tr="He will pay as much as you want."),
        mc("Which pronoun follows тот when there is no noun and a person is meant?", ["кто", "что", "кото'рый", "како'й"], "кто",
           "Тот, кто …", order=True),
        mc("Which pronoun follows тако'й?", ["како'й", "кото'рый", "кто", "что"], "како'й", "Тако'й …, како'й …", order=True),
    ],
)

# ---------------------------------------------------------------------------- 132
L132 = lesson(
    "Review: adjectives, dates and descriptions",
    "Putting lessons 121 to 131 together",
    requires=["новый", "число", "высокий", "когда", "который"],
    cards=[
        card("What you can do now",
             "You can use adjectives, possessives and ordinals in the genitive, ask for and give the date and "
             "birthday, describe a person's height, build, hair, eyes and character, name the parts of the body, "
             "choose the aspect after когда', пока' and как то'лько, put a question inside a sentence, and join "
             "clauses with тот, кто, то, что and кото'рый.",
             tables=[table(
                 ["Topic", "Remember"],
                 [["Genitive adjective", "нет но'вого стола' · нет но'вой ку'ртки"],
                  ["Date", "Сего'дня пя'тое ма'я."],
                  ["On a date", "Мы е'дем пя'того января'."],
                  ["Height", "Он высо'кого ро'ста."],
                  ["Hair and eyes", "У неё све'тлые во'лосы и ка'рие глаза'."],
                  ["During", "Пока' я смотре'ла, он пригото'вил …"],
                  ["Inside a sentence", "Скажи', кто до'ма."],
                  ["The one who", "Тот, кто … · то, что …"]])]),
    ],
    verify=[],
    exercises=[
        fb("В кла'ссе нет ___ студе'нта.", ["но'вого", "но'вый", "но'вому", "но'вым"], "но'вого",
           "Masculine genitive: -ого.", tr="The new student is not in the classroom.", lemma="новый"),
        fb("Здесь нет ___ ключа'. (my)", ["моего'", "мой", "мое'й", "моему'"], "моего'",
           "Masculine genitive: моего'.", tr="My key isn't here.", lemma="мой"),
        fb("Сего'дня тре'тье ___.", ["ию'ня", "ию'нь", "ию'не", "ию'ню"], "ию'ня",
           "Genitive of the month.", tr="Today is the third of June.", lemma="июнь"),
        fb("Мы е'дем в Москву' пя'того ___.", ["января'", "янва'рь", "январе'", "январю'"], "января'",
           "On a date: genitive.", tr="We are going to Moscow on the fifth of January.", lemma="январь"),
        fb("Он высо'кого ___.", ["ро'ста", "рост", "ро'сту", "ро'сте"], "ро'ста",
           "Height: genitive.", tr="He is tall.", lemma="рост"),
        fb("У неё ка'рие ___.", ["глаза'", "глаз", "глазу'", "глазе'"], "глаза'",
           "Plural: глаза'.", tr="She has brown eyes.", lemma="глаз"),
        fb("Пока' мой брат чита'л, я ___ телеви'зор.", ["смотре'ла", "посмотре'ла"], "смотре'ла",
           "Parallel actions: imperfective.", tr="While my brother was reading, I was watching TV."),
        fb("Я хочу' знать, ___ ты купи'ла. (what)", ["что", "кто", "како'й", "чей"], "что",
           "Что asks about a thing.", tr="I want to know what you bought."),
        fb("Я зна'ю того', ___ написа'л э'тот расска'з.", ["кто", "что", "кото'рый", "како'й"], "кто",
           "Тот without a noun, a person: кто.", tr="I know the person who wrote this story."),
        mc("Which means “on the ninth of June”?",
           ["девя'того ию'ня", "девя'тое ию'ня", "девя'тый ию'нь", "девя'том ию'не"], "девя'того ию'ня",
           "Ordinal in the genitive, then the month in the genitive."),
        mc("Which genitive ending does a feminine hard adjective take?", ["-ой", "-ого", "-ей", "-ому"], "-ой",
           "Но'вой.", order=True),
    ],
)

UNIT = unit("Unit 15: Genitive adjectives, dates and describing people",
            [L121, L122, L123, L124, L125, L126, L127, L128, L129, L130, L131, L132])
