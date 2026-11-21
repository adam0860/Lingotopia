"""Unit 13: absence, numbers 2-4, aspect with time expressions, clothes
(textbook module 3, lesson 18)."""
from dsl import *

# ---------------------------------------------------------------------------- 95
L95 = lesson(
    "There isn't any: нет and the genitive",
    "В па'рке нет туале'та. У меня' нет бра'та.",
    requires=["нет", "кот", "машина", "брат", "сестра"],
    cards=[
        card("Есть or нет",
             "To say that something exists, use есть and the nominative: Здесь есть магази'н. To say that it does "
             "not exist, use нет and put the missing thing in the genitive: Здесь нет магази'на. So нет is not only "
             "“no”: it also means “there isn't”, and the genitive tells you what is missing.",
             tables=[table(
                 ["There is", "There isn't"],
                 [["Здесь есть магази'н.", "Здесь нет магази'н{а}."],
                  ["Здесь есть шко'ла.", "Здесь нет шко'л{ы}."],
                  ["Здесь есть окно'.", "Здесь нет окн{а'}."],
                  ["В па'рке есть туале'т.", "В па'рке нет туале'т{а}."],
                  ["В кла'ссе есть слова'рь.", "В кла'ссе нет словар{я'}."],
                  ["В го'роде есть мост.", "В го'роде нет мост{а'}."]],
                 note="Some words never change: кафе', метро', такси'. Здесь есть кафе'. Здесь нет кафе'.")]),
        card("У меня' нет …",
             "To say what you do not have, use у + the owner in the genitive, then нет + the missing thing in the "
             "genitive. Both the owner and the thing are in the genitive: У ма'мы нет маши'ны.",
             tables=[table(
                 ["I have", "I don't have"],
                 [["У меня' есть брат.", "У меня' нет бра'т{а}."],
                  ["У ма'мы есть маши'на.", "У ма'мы нет маши'н{ы}."],
                  ["У дру'га есть кот.", "У дру'га нет кот{а'}."],
                  ["У сестры' есть ко'шка.", "У сестры' нет ко'шк{и}."]])],
             examples=[
                 ex("У меня' нет вре'мени.", "I have no time.", "нет вре'мени"),
                 ex("У нас нет учи'теля.", "We don't have a teacher.", "нет учи'теля"),
                 ex("Здесь нет кафе'.", "There is no café here.", "нет кафе'"),
                 ex("В э'том го'роде нет мо'ря.", "There is no sea in this city.", "нет мо'ря"),
             ]),
    ],
    verify=(vf("кот", "кота") + vf("брат", "брата") + vf("машина", "машины") + vf("сестра", "сестры")
            + vf("туалет", "туалета") + vf("мост", "моста") + vf("словарь", "словаря") + vf("время", "времени")
            + vf("магазин", "магазина") + vf("школа", "школы") + vf("окно", "окна") + vf("мама", "мамы")
            + vf("учитель", "учителя") + vf("море", "моря") + vf("друг", "друга") + vf("кошка", "кошки")),
    exercises=[
        fb("В па'рке нет ___.", ["туале'та", "туале'т", "туале'ту", "туале'том"], "туале'та",
           "After нет: the genitive.", tr="There is no bathroom in the park.", lemma="туалет"),
        fb("У меня' нет ___.", ["бра'та", "брат", "бра'ту", "бра'том"], "бра'та",
           "After нет: the genitive.", tr="I don't have a brother.", lemma="брат"),
        fb("У ма'мы нет ___.", ["маши'ны", "маши'на", "маши'ну", "маши'не"], "маши'ны",
           "Feminine nouns in -а take -ы in the genitive.", tr="Mom doesn't have a car.", lemma="машина"),
        fb("В э'том го'роде нет ___.", ["мо'ря", "мо'ре", "мо'рю", "мо'рем"], "мо'ря",
           "Neuter nouns in -е take -я.", tr="There is no sea in this city.", lemma="море"),
        fb("У дру'га нет ___.", ["словаря'", "слова'рь", "словарю'", "словаре'"], "словаря'",
           "Masculine soft nouns take -я.", tr="My friend doesn't have a dictionary.", lemma="словарь"),
        fb("У нас нет ___. (time)", ["вре'мени", "вре'мя", "вре'менем", "времена'"], "вре'мени",
           "Вре'мя is one of the special nouns: вре'мени.", tr="We have no time.", lemma="время"),
        mc("Which case follows нет?", ["genitive", "nominative", "accusative", "prepositional"], "genitive",
           "Нет is followed by the genitive.", order=True),
        mc("Which word never changes in the genitive?", ["кафе'", "окно'", "шко'ла", "парк"], "кафе'",
           "Кафе', метро' and такси' are indeclinable."),
        mc("How do you say “We have no teacher”?",
           ["У нас нет учи'теля.", "У нас нет учи'тель.", "У нас нет учи'телем.", "У нас нет учи'телю."],
           "У нас нет учи'теля.", "Genitive of учи'тель: учи'теля."),
        mc("Which sentence says there is no cat here?",
           ["Здесь нет кота'.", "Здесь нет кот.", "Здесь есть кота'.", "Здесь нет коту'."],
           "Здесь нет кота'.", "Нет + genitive."),
    ],
)

# ---------------------------------------------------------------------------- 96
L96 = lesson(
    "There was no, there will be no: не́ было, не бу́дет",
    "Вчера' не́ было дождя'. За'втра не бу'дет конце'рта.",
    requires=["быть", "дождь", "концерт", "вчера", "завтра"],
    cards=[
        card("The past: не́ было",
             "In the past, есть becomes был, была', бы'ло or бы'ли and agrees with what existed. When something did "
             "not exist, Russian uses one fixed form, не́ было, with the stress on не. It never changes for gender or "
             "number, and the missing thing goes in the genitive.",
             tables=[table(
                 ["There was", "There was not"],
                 [["Здесь был телефо'н.", "Здесь не́ было телефо'н{а}."],
                  ["В кла'ссе была' ка'рта.", "В кла'ссе не́ было ка'рт{ы}."],
                  ["На столе' бы'ло вино'.", "На столе' не́ было вин{а'}."],
                  ["Вчера' был дождь.", "Вчера' не́ было дожд{я'}."],
                  ["Вчера' был уро'к.", "Вчера' не́ было уро'к{а}."]])]),
        card("The future: не бу́дет",
             "In the future, бу'дет (or бу'дут) agrees with what will exist. When something will not exist, use one "
             "fixed form, не бу'дет, and the genitive.",
             tables=[table(
                 ["There will be", "There will not be"],
                 [["За'втра бу'дет дождь.", "За'втра не бу'дет дожд{я'}."],
                  ["Здесь бу'дет кинотеа'тр.", "Здесь не бу'дет кинотеа'тр{а}."],
                  ["Послеза'втра бу'дет конце'рт.", "Послеза'втра не бу'дет конце'рт{а}."],
                  ["В кла'ссе бу'дет ка'рта.", "В кла'ссе не бу'дет ка'рт{ы}."]])],
             examples=[
                 ex("У меня' никогда' не́ было ко'шки.", "I have never had a cat.", "не́ было"),
                 ex("У меня' никогда' не бу'дет ко'шки.", "I will never have a cat.", "не бу'дет"),
                 ex("Анто'на сего'дня нет.", "Anton isn't here today.", "Анто'на"),
                 ex("Анто'на вчера' не́ было.", "Anton wasn't here yesterday.", "не́ было"),
                 ex("Анто'на за'втра не бу'дет.", "Anton won't be here tomorrow.", "не бу'дет"),
             ]),
    ],
    verify=(vf("дождь", "дождя") + vf("урок", "урока") + vf("телефон", "телефона") + vf("карта", "карты")
            + vf("вино", "вина") + vf("кинотеатр", "кинотеатра") + vf("концерт", "концерта")
            + vf("кошка", "кошки") + vf("быть", "был", "была", "было", "были", "будет", "будут")),
    exercises=[
        fb("Вчера' не́ было ___.", ["дождя'", "дождь", "дождём", "дожде'"], "дождя'",
           "After не́ было: the genitive.", tr="There was no rain yesterday.", lemma="дождь"),
        fb("За'втра не бу'дет ___.", ["уро'ка", "уро'к", "уро'ку", "уро'ком"], "уро'ка",
           "After не бу'дет: the genitive.", tr="There will be no lesson tomorrow.", lemma="урок"),
        fb("В э'той ко'мнате был стол, но не́ было ___. (a telephone)", ["телефо'на", "телефо'н", "телефо'ну", "телефо'ном"],
           "телефо'на", "After не́ было: the genitive.", tr="In this room there was a table, but there was no telephone.",
           lemma="телефон"),
        fb("В кла'ссе не́ было ___.", ["ка'рты", "ка'рта", "ка'рту", "ка'рте"], "ка'рты",
           "Feminine nouns in -а take -ы.", tr="There was no map in the classroom.", lemma="карта"),
        fb("На столе' не́ было ___.", ["вина'", "вино'", "вину'", "вине'"], "вина'",
           "Neuter nouns in -о take -а, and the stress moves.", tr="There was no wine on the table.", lemma="вино"),
        fb("Анто'на вчера' ___ до'ма.", ["не́ было", "нет", "не бу'дет", "не́ были"], "не́ было",
           "Past tense: не́ было, which never changes.", tr="Anton wasn't at home yesterday."),
        mc("Which sentence is correct?",
           ["Вчера' не́ было дождя'.", "Вчера' не была дождя'.", "Вчера' не́ были дождя'.", "Вчера' не́ был дождя'."],
           "Вчера' не́ было дождя'.", "Не́ было stays neuter singular."),
        mc("Which form never changes in the negative past?", ["не́ было", "не́ был", "не́ была", "не́ были"], "не́ было",
           "Always neuter singular.", order=True),
        mc("How do you say “There will be no concert tomorrow”?",
           ["За'втра не бу'дет конце'рта.", "За'втра не бу'дет конце'рт.", "За'втра нет конце'рта.", "За'втра не бу'ду конце'рта."],
           "За'втра не бу'дет конце'рта.", "Не бу'дет + genitive."),
    ],
)

# ---------------------------------------------------------------------------- 97
L97 = lesson(
    "Without me, near him: pronouns in the genitive",
    "У меня' нет, у него' нет, без неё",
    requires=["я", "тебя", "его", "её", "нас"],
    cards=[
        card("The genitive of pronouns",
             "The genitive of the personal pronouns is the same as the accusative that you learned in lesson 29: "
             "меня', тебя', его', её, нас, вас, их. Use them after нет, у, без, до, из and every other preposition "
             "that takes the genitive.",
             tables=[table(
                 ["Nominative", "Genitive", "Example"],
                 [["я", "меня'", "У меня' нет вре'мени."],
                  ["ты", "тебя'", "У тебя' нет вре'мени."],
                  ["он, оно'", "(н)его'", "У него' нет вре'мени."],
                  ["она'", "(н)её", "У неё нет вре'мени."],
                  ["мы", "нас", "У нас нет вре'мени."],
                  ["вы", "вас", "У вас нет вре'мени."],
                  ["они'", "(н)их", "У них нет вре'мени."]])]),
        card("Add н after a preposition",
             "After a preposition, его', её and их become него', неё and них. This applies only to the personal "
             "pronouns (him, her, them). The possessives его' (his), её (her) and их (their) never get н: У его' "
             "отца' есть маши'на. Compare the two rows below.",
             tables=[table(
                 ["Personal (him, her, them)", "Possessive (his, her, their)"],
                 [["У него' есть маши'на.", "У его' отца' есть маши'на."],
                  ["У неё есть маши'на.", "У её отца' есть маши'на."],
                  ["У них есть маши'на.", "У их отца' есть маши'на."]],
                 note="He has a car. / His father has a car. The same applies to her and them.")],
             examples=[
                 ex("Я не могу' жить без неё.", "I can't live without her.", "без неё"),
                 ex("Я иду' без него'.", "I am going without him.", "без него'"),
                 ex("До них здесь бы'ли мы.", "We were here before them.", "До них"),
                 ex("Меня' нет до'ма.", "I'm not at home.", "Меня' нет"),
                 ex("Тебя' вчера' не́ было на уро'ке.", "You weren't in class yesterday.", "Тебя'"),
             ]),
    ],
    verify=(vf("я", "меня") + vf("ты", "тебя") + vf("он", "его", "него") + vf("она", "её", "неё")
            + vf("мы", "нас") + vf("вы", "вас") + vf("они", "их", "них") + vf("оно", "его", "него")),
    exercises=[
        fb("У ___ есть маши'на. (him)", ["него'", "его'", "ему'", "ним"], "него'",
           "After у: н- is added.", tr="He has a car.", lemma="он"),
        fb("У ___ нет вре'мени. (me)", ["меня'", "я", "мне", "мной"], "меня'",
           "Genitive of я: меня'.", tr="I have no time.", lemma="я"),
        fb("Мы идём без ___. (her)", ["неё", "её", "ей", "ней"], "неё",
           "After a preposition: неё.", tr="We are going without her.", lemma="она"),
        fb("У ___ нет вре'мени. (us)", ["нас", "на'ши", "нам", "нами"], "нас",
           "Genitive of мы: нас.", tr="We have no time.", lemma="мы"),
        fb("Э'то маши'на ___ отца'. (his)", ["его'", "него'", "ему'", "ним"], "его'",
           "Possessive его' never gets н.", tr="This is his father's car."),
        fb("У ___ есть кот. (them)", ["них", "их", "им", "ими"], "них",
           "After у: них.", tr="They have a cat.", lemma="они"),
        fb("Тебя' вчера' не́ ___ на уро'ке.", ["было", "был", "была'", "были"], "было",
           "Не́ было never changes.", tr="You weren't in class yesterday."),
        mc("Which sentence is correct?",
           ["У неё нет вре'мени.", "У её нет вре'мени.", "У она' нет вре'мени.", "У ней нет вре'мени."],
           "У неё нет вре'мени.", "After a preposition: неё."),
        mc("When do его', её and их get н-?",
           ["after a preposition, as pronouns", "always", "never", "only before nouns"],
           "after a preposition, as pronouns", "Personal pronouns only."),
        mc("Which sentence means “I'm not at home”?",
           ["Меня' нет до'ма.", "Я нет до'ма.", "Мне нет до'ма.", "Меня' не до'ма."],
           "Меня' нет до'ма.", "Genitive of the person + нет."),
    ],
)

# ---------------------------------------------------------------------------- 98
L98 = lesson(
    "Two, three, four: the genitive after small numbers",
    "Два стола', две кни'ги, три окна', четы'ре ко'мнаты",
    requires=["студент", "книга", "окно", "час", "год"],
    cards=[
        card("A noun after 2, 3 and 4",
             "After два (две), три and четы'ре, the noun takes the genitive singular. Два is for masculine and "
             "neuter nouns, две is for feminine ones. The stress moves in the same way as in the genitive: "
             "стол → стола'. After пять and larger numbers the noun takes a different form that you will learn "
             "later (you have already seen it in пять рубле'й).",
             tables=[table(
                 ["Number", "Masculine", "Feminine", "Neuter"],
                 [["1", "оди'н стол", "одна' кни'га", "одно' окно'"],
                  ["2", "два стол{а'}", "дв{е} кни'г{и}", "два окн{а'}"],
                  ["3", "три стол{а'}", "три кни'г{и}", "три окн{а'}"],
                  ["4", "четы'ре стол{а'}", "четы'ре кни'г{и}", "четы'ре окн{а'}"]])]),
        card("22, 33, 104 and the rest",
             "Look only at the last word of the number. If it is два (две), три or четы'ре, use the genitive "
             "singular: два'дцать два стола'. If it is оди'н, use the nominative: два'дцать оди'н стол. The "
             "numbers 12, 13 and 14 are the exception: they end in -надцать, so they follow the later rule. "
             "This works for time words too: два часа', три дня, четы'ре го'да.",
             tables=[table(
                 ["Number", "Last word", "Example"],
                 [["21", "оди'н", "два'дцать оди'н стол"],
                  ["22", "два", "два'дцать два стол{а'}"],
                  ["33", "три", "три'дцать три окн{а'}"],
                  ["104", "четы'ре", "сто четы'ре кни'г{и}"]])],
             examples=[
                 ex("У меня' два бра'та.", "I have two brothers.", "два бра'та"),
                 ex("У неё две сестры'.", "She has two sisters.", "две сестры'"),
                 ex("В кла'ссе три окна'.", "There are three windows in the classroom.", "три окна'"),
                 ex("Мы там бы'ли два часа'.", "We were there for two hours.", "два часа'"),
                 ex("Я живу' здесь два го'да.", "I have lived here for two years.", "два го'да"),
                 ex("Он рабо'тает три дня.", "He works for three days.", "три дня"),
             ]),
    ],
    verify=(vf("стол", "стола") + vf("книга", "книги") + vf("окно", "окна") + vf("брат", "брата")
            + vf("сестра", "сестры") + vf("комната", "комнаты") + vf("час", "часа") + vf("год", "года")
            + vf("день", "дня") + vf("два", "два", "две") + vf("четыре", "четыре")),
    exercises=[
        fb("Вот два ___.", ["стола'", "стол", "столы'", "столо'в"], "стола'",
           "After два: the genitive singular.", tr="Here are two tables.", lemma="стол"),
        fb("У меня' две ___.", ["сестры'", "сестра'", "сестру'", "сестре'"], "сестры'",
           "After две: the genitive singular.", tr="I have two sisters.", lemma="сестра"),
        fb("В кла'ссе три ___.", ["окна'", "окно'", "окну'", "окне'"], "окна'",
           "After три: the genitive singular.", tr="There are three windows in the classroom.", lemma="окно"),
        fb("Здесь четы'ре ___.", ["ко'мнаты", "ко'мната", "ко'мнату", "ко'мнате"], "ко'мнаты",
           "After четы'ре: the genitive singular.", tr="There are four rooms here.", lemma="комната"),
        fb("Я живу' здесь два ___.", ["го'да", "год", "го'ду", "годо'м"], "го'да",
           "After два: го'да.", tr="I have lived here for two years.", lemma="год"),
        fb("Мы там бы'ли три ___.", ["часа'", "час", "часы'", "часо'в"], "часа'",
           "After три: часа'.", tr="We were there for three hours.", lemma="час"),
        fb("У меня' ___ кни'ги.", ["две", "два", "оди'н", "одна'"], "две",
           "Кни'ги is feminine, so две.", tr="I have two books."),
        fb("Здесь два'дцать два ___.", ["стола'", "стол", "столы'", "столо'в"], "стола'",
           "The last word is два: genitive singular.", tr="There are twenty-two tables here.", lemma="стол"),
        mc("Which number takes a noun in the genitive singular?", ["34", "15", "20", "11"], "34",
           "It ends in 4. Fifteen, twenty and eleven do not.", order=True),
        mc("How do you say “three books”?",
           ["три кни'ги", "три кни'га", "три кни'гу", "три кни'ге"], "три кни'ги", "Три + genitive singular."),
    ],
)

# ---------------------------------------------------------------------------- 99
L99 = lesson(
    "For how long? In how long?",
    "Я чита'л три часа'. Я прочита'л за три часа'.",
    requires=["читать", "прочитать", "делать", "сделать", "час"],
    cards=[
        card("For how long? The imperfective",
             "A time word in the accusative with no preposition says how long an action lasted, and the verb is "
             "imperfective: Я чита'л э'ту кни'гу три часа'. The questions are Как до'лго …? and Ско'лько "
             "вре'мени …?",
             tables=[table(
                 ["Question", "Answer (imperfective)"],
                 [["Как до'лго ты чита'л?", "Я чита'л три часа'."],
                  ["Ско'лько вре'мени ты де'лал уро'ки?", "Я де'лал уро'ки час."],
                  ["Как до'лго она' жила' там?", "Она' жила' там год."],
                  ["Как до'лго вы бу'дете там?", "Мы бу'дем там неде'лю."]])]),
        card("In how long? The perfective with за",
             "To say how much time it took to finish, use the perfective and за + the accusative: Я прочита'л э'ту "
             "кни'гу за три часа'. The question is За ско'лько вре'мени …?",
             tables=[table(
                 ["Question", "Answer (perfective)"],
                 [["За ско'лько вре'мени ты прочита'л кни'гу?", "Я прочита'л её за три часа'."],
                  ["За ско'лько вре'мени ты сде'лаешь э'то?", "Я сде'лаю э'то за час."],
                  ["За ско'лько вре'мени она' написа'ла письмо'?", "За пять мину'т."]])],
             examples=[
                 ex("Я чита'л э'ту кни'гу три часа'.", "I read (was reading) this book for three hours.", "три часа'"),
                 ex("Я прочита'л э'ту кни'гу за три часа'.", "I finished this book in three hours.", "за три часа'"),
                 ex("Э'та дома'шняя рабо'та больша'я. Я бу'ду де'лать её три часа'.",
                    "This homework is big. I will be doing it for three hours.", "бу'ду де'лать"),
                 ex("Э'та дома'шняя рабо'та небольша'я. Я сде'лаю её за час.",
                    "This homework is not big. I will do it in an hour.", "сде'лаю"),
                 ex("Мы жи'ли там год.", "We lived there for a year.", "год"),
             ]),
    ],
    verify=(vf("читать", "читал") + vf("прочитать", "прочитал") + vf("делать", "делал")
            + vf("сделать", "сделаю", "сделаешь") + vf("написать", "написала")),
    exercises=[
        fb("Я ___ э'ту кни'гу три часа'.", ["чита'л", "прочита'л"], "чита'л",
           "A duration: imperfective.", tr="I read this book for three hours."),
        fb("Я ___ э'ту кни'гу за три часа'.", ["прочита'л", "чита'л"], "прочита'л",
           "За + time: perfective.", tr="I finished this book in three hours."),
        fb("Как до'лго ты ___ уро'ки?", ["де'лал", "сде'лал"], "де'лал",
           "Как до'лго: imperfective.", tr="How long did you do your homework?"),
        fb("За ско'лько вре'мени ты ___ э'то?", ["сде'лаешь", "бу'дешь де'лать"], "сде'лаешь",
           "За ско'лько вре'мени: perfective.", tr="How long will it take you to do this?"),
        fb("Мы жи'ли там ___.", ["год", "за год", "че'рез год", "в год"], "год",
           "A duration needs no preposition.", tr="We lived there for a year."),
        fb("Она' написа'ла письмо' ___ пять мину'т.", ["за", "в", "о", "из"], "за",
           "Completion in a time: за.", tr="She wrote the letter in five minutes."),
        mc("Which question asks for the duration?",
           ["Как до'лго ты чита'л?", "За ско'лько вре'мени ты прочита'л?", "Что ты чита'л?", "Ты уже' прочита'л?"],
           "Как до'лго ты чита'л?", "Как до'лго = for how long."),
        mc("Which aspect goes with за + a time?", ["perfective", "imperfective", "either", "neither"], "perfective",
           "You say how long it took to finish.", order=True),
        mc("Which means “I read it in two hours (and finished)”?",
           ["Я прочита'л э'то за два часа'.", "Я чита'л э'то два часа'.", "Я прочита'л э'то два часа'.", "Я чита'л э'то за два часа'."],
           "Я прочита'л э'то за два часа'.", "Perfective + за."),
    ],
)

# ---------------------------------------------------------------------------- 100
L100 = lesson(
    "Didn't try, or didn't manage?",
    "Я не учи'л. Я не вы'учил.",
    requires=["учить", "делать", "сделать", "писать", "написать"],
    cards=[
        card("Negation and aspect",
             "With не, the imperfective says that the action did not happen at all: no time was spent on it, no "
             "attempt was made. The perfective says that the action was not completed: you may have tried, but "
             "there is no result to show. So Я не учи'л э'тот диало'г means “I didn't study this dialog at all”, "
             "while Я не вы'учил э'тот диало'г means “I can't recite it, because I didn't learn it”.",
             tables=[table(
                 ["Sentence", "Aspect", "What it means"],
                 [["Я не учи'л э'тот диало'г.", "imperfective", "I didn't study it."],
                  ["Я не вы'учил э'тот диало'г.", "perfective", "I didn't learn it."],
                  ["Я не писа'л письмо'.", "imperfective", "I didn't write at all."],
                  ["Я не написа'л письмо'.", "perfective", "I haven't got it written."]])]),
        card("Negation in the future",
             "The same contrast works in the future. Я не бу'ду де'лать э'ту рабо'ту! says that you will not even "
             "start. Я не сде'лаю э'ту рабо'ту says that you believe you will not manage to finish it. In both "
             "sentences the reason can be the same: the job is too big (сли'шком большо'й).",
             examples=[
                 ex("Я не бу'ду де'лать э'ту рабо'ту! Она' сли'шком больша'я.",
                    "I will not do this work! It is too big.", "не бу'ду де'лать"),
                 ex("Я не сде'лаю э'ту рабо'ту. Она' сли'шком больша'я.",
                    "I won't manage to do this work. It is too big.", "не сде'лаю"),
                 ex("Вчера' я не чита'л, а смотре'л фильм.", "Yesterday I didn't read; I watched a film.", "не чита'л"),
                 ex("Я весь ве'чер учи'л э'то сло'во, но не вы'учил его'.",
                    "I studied this word all evening, but I didn't learn it.", "не вы'учил"),
                 ex("Я не прочита'л э'ту кни'гу.", "I haven't read this book through.", "не прочита'л"),
             ]),
    ],
    verify=(vf("учить", "учил") + vf("выучить", "выучил") + vf("писать", "писал") + vf("написать", "написал")
            + vf("сделать", "сделаю") + vf("читать", "читал")
            + vf("прочитать", "прочитал")),
    exercises=[
        fb("Вчера' я не ___, а смотре'л фильм. (didn't read at all)", ["чита'л", "прочита'л"], "чита'л",
           "No attempt at reading was made: imperfective.", tr="Yesterday I didn't read; I watched a film."),
        fb("Я весь ве'чер учи'л э'то сло'во, но не ___ его'.", ["вы'учил", "учи'л"], "вы'учил",
           "Tried, but no result: perfective.", tr="I studied this word all evening, but I didn't learn it."),
        fb("Я пыта'лся, но не ___ э'ту рабо'ту.", ["сде'лал", "де'лал"], "сде'лал",
           "Tried, but did not finish: perfective.", tr="I tried, but I didn't manage to do this work."),
        fb("Я не ___ э'ту кни'гу до конца'. (didn't finish it)", ["прочита'л", "чита'л"], "прочита'л",
           "Not completed: perfective.", tr="I haven't read this book to the end."),
        fb("Э'та рабо'та сли'шком больша'я. Я не ___ её! (I won't even start)", ["бу'ду де'лать", "сде'лаю"], "бу'ду де'лать",
           "The refusal to even begin: не бу'ду + imperfective.", tr="This work is too big. I'm not going to do it!"),
        mc("Which sentence says the letter is still not finished?",
           ["Я не написа'л письмо'.", "Я не писа'л письмо'.", "Я не пишу' письмо'.", "Я пишу' письмо'."],
           "Я не написа'л письмо'.", "Не + perfective: no completed result."),
        mc("Which sentence says that no writing took place at all?",
           ["Я не писа'л письмо'.", "Я не написа'л письмо'.", "Я написа'л письмо'.", "Я пишу' письмо'."],
           "Я не писа'л письмо'.", "Не + imperfective: the action did not happen."),
        mc("Which aspect do you use for “I tried but didn't manage”?", ["perfective", "imperfective", "either", "neither"],
           "perfective", "No result: не + perfective.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 101
L101 = lesson(
    "Suddenly! At once! Begin, continue, finish",
    "Он вдруг уви'дел кота'. Мы на'чали смотре'ть фильм.",
    requires=["вдруг", "сразу", "начинать", "продолжать", "закончить"],
    cards=[
        card("A quick, single action",
             "Words such as сра'зу (at once), как то'лько (as soon as) and вдруг (suddenly) show an action that "
             "happens in a moment. The verb is perfective.",
             tables=[table(
                 ["Word", "Meaning", "Example"],
                 [["сра'зу", "at once", "Я сра'зу купи'л су'мку."],
                  ["как то'лько", "as soon as", "Как то'лько я уви'дел су'мку, я купи'л её."],
                  ["вдруг", "suddenly", "Он вдруг услы'шал му'зыку."]])],
             examples=[
                 ex("Как то'лько я уви'дела э'ту су'мку, я сра'зу купи'ла её.",
                    "As soon as I saw this bag, I bought it right away.", "сра'зу купи'ла"),
                 ex("И'горь чита'л газе'ту, когда' вдруг услы'шал му'зыку.",
                    "Igor was reading the paper when he suddenly heard music.", "вдруг услы'шал"),
                 ex("Я откры'л дверь и вдруг уви'дел кота'.", "I opened the door and suddenly saw a cat.", "вдруг уви'дел"),
             ]),
        card("Begin, continue, finish",
             "The verbs начина'ть / нача'ть, продолжа'ть and зака'нчивать / зако'нчить are followed only by an "
             "imperfective infinitive, whatever the aspect of the first verb. Мой брат на'чал изуча'ть "
             "францу'зский (perfective нача'ть, imperfective infinitive). When the first verb is imperfective, "
             "it can also mean that you tried several times: Я мно'го раз начина'л изуча'ть францу'зский.",
             tables=[table(
                 ["Verb", "Example"],
                 [["начина'ть / нача'ть", "Мой брат на'чал изуча'ть францу'зский язы'к."],
                  ["продолжа'ть", "Ве'ра продолжа'ет игра'ть на саксофо'не."],
                  ["зака'нчивать / зако'нчить", "Мы зако'нчили обе'дать."]])],
             examples=[
                 ex("Мы зако'нчили обе'дать и на'чали смотре'ть фильм.",
                    "We finished lunch and began watching a film.", "на'чали смотре'ть"),
                 ex("Я мно'го раз начина'л изуча'ть францу'зский.",
                    "I started studying French many times. (I tried many times.)", "начина'л изуча'ть"),
             ]),
    ],
    verify=(vf("купить", "купил", "купила") + vf("увидеть", "увидел", "увидела") + vf("услышать", "услышал")
            + vf("открыть", "открыл") + vf("начать", "начал", "начали") + vf("закончить", "закончили")
            + vf("продолжать", "продолжает") + vf("изучать", "изучать") + vf("обедать", "обедать")),
    exercises=[
        fb("Как то'лько я уви'дел су'мку, я сра'зу ___ её.", ["купи'л", "покупа'л"], "купи'л",
           "A single, instant action: perfective.", tr="As soon as I saw the bag, I bought it right away."),
        fb("Он чита'л газе'ту, когда' вдруг ___ му'зыку.", ["услы'шал", "слы'шал"], "услы'шал",
           "Вдруг: perfective.", tr="He was reading the paper when he suddenly heard music."),
        fb("Я откры'л дверь и вдруг ___ кота'.", ["уви'дел", "ви'дел"], "уви'дел",
           "Вдруг: perfective.", tr="I opened the door and suddenly saw a cat."),
        fb("Мы зако'нчили ___ и на'чали смотре'ть фильм.", ["обе'дать", "пообе'дать"], "обе'дать",
           "After зако'нчить: the imperfective infinitive.", tr="We finished lunch and began watching a film."),
        fb("Ве'ра продолжа'ет ___ на саксофо'не.", ["игра'ть", "сыгра'ть"], "игра'ть",
           "After продолжа'ть: the imperfective infinitive.", tr="Vera keeps playing the saxophone."),
        fb("Мой брат на'чал ___ францу'зский язы'к.", ["изуча'ть", "изучи'ть"], "изуча'ть",
           "After нача'ть: the imperfective infinitive.", tr="My brother began studying French."),
        mc("Which word signals a sudden, single action?", ["вдруг", "ча'сто", "всегда'", "ка'ждый день"], "вдруг",
           "Вдруг = suddenly."),
        mc("Which infinitive follows продолжа'ть?", ["imperfective", "perfective", "either", "neither"], "imperfective",
           "Begin, continue and finish take the imperfective.", order=True),
        mc("Which sentence is correct?",
           ["Он на'чал чита'ть кни'гу.", "Он на'чал прочита'ть кни'гу.", "Он продолжа'ет прочита'ть кни'гу.", "Он зако'нчил прочита'ть кни'гу."],
           "Он на'чал чита'ть кни'гу.", "After на'чал: an imperfective infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 102
L102 = lesson(
    "Let's! Дава́й and дава́йте",
    "Дава'йте говори'ть по-ру'сски! Дава'й напи'шем!",
    requires=["говорить", "писать", "написать", "смотреть", "посмотреть"],
    cards=[
        card("Let's do it regularly",
             "Дава'й (to one friend) or Дава'йте (to several people, or politely) + a verb makes a suggestion. To "
             "suggest doing something regularly, from now on, use the imperfective infinitive. You can add "
             "бу'дем before it. To say “Let's not …”, put не before the imperfective infinitive.",
             tables=[table(
                 ["Suggestion", "Meaning"],
                 [["Дава'йте говори'ть по-ру'сски!", "Let's speak Russian (from now on)."],
                  ["Дава'йте бу'дем говори'ть по-ру'сски!", "The same, with бу'дем."],
                  ["Дава'йте не говори'ть по-англи'йски!", "Let's not speak English."],
                  ["Дава'й не бу'дем писа'ть расска'з!", "Let's not write a story."]])]),
        card("Let's do it once",
             "To suggest doing something once, from start to finish, use дава'й(те) and the perfective “we” form. "
             "It is the same as the future tense: напи'шем, посмо'трим, ку'пим.",
             tables=[table(
                 ["Dictionary form", "Let's …"],
                 [["написа'ть", "Дава'й напи'шем!"],
                  ["посмотре'ть", "Дава'й посмо'трим!"],
                  ["купи'ть", "Дава'й ку'пим!"],
                  ["сде'лать", "Дава'й сде'лаем!"],
                  ["прочита'ть", "Дава'й прочита'ем!"],
                  ["пойти'", "Дава'й пойдём!"]])],
             examples=[
                 ex("Дава'йте говори'ть в кла'ссе то'лько по-ру'сски!", "Let's speak only Russian in the classroom!", "говори'ть"),
                 ex("Дава'йте напи'шем расска'з по-ру'сски!", "Let's write a story in Russian!", "напи'шем"),
                 ex("Дава'й не бу'дем говори'ть по-англи'йски!", "Let's not speak English!", "не бу'дем говори'ть"),
                 ex("Дава'й посмо'трим э'тот фильм!", "Let's watch this film!", "посмо'трим"),
             ]),
    ],
    verify=(vf("написать", "напишем") + vf("посмотреть", "посмотрим") + vf("купить", "купим")
            + vf("сделать", "сделаем") + vf("прочитать", "прочитаем") + vf("пойти", "пойдём")
            + vf("говорить", "говорить") + vf("давать", "давай", "давайте")),
    exercises=[
        fb("Дава'йте ___ в кла'ссе то'лько по-ру'сски! (from now on)", ["говори'ть", "сказа'ть"], "говори'ть",
           "A regular habit: the imperfective infinitive.", tr="Let's speak only Russian in the classroom!"),
        fb("Дава'йте ___ расска'з! (once)", ["напи'шем", "писа'ть"], "напи'шем",
           "Once, to the end: the perfective we-form.", tr="Let's write a story!"),
        fb("Дава'й не ___ по-англи'йски!", ["говори'ть", "сказа'ть"], "говори'ть",
           "A negative suggestion: the imperfective infinitive.", tr="Let's not speak English!"),
        fb("Дава'й ___ э'тот фильм сего'дня!", ["посмо'трим", "смотре'ть"], "посмо'трим",
           "Once: the perfective we-form.", tr="Let's watch this film today!"),
        fb("Дава'й ___ но'вую маши'ну!", ["ку'пим", "покупа'ть"], "ку'пим",
           "Once: the perfective we-form.", tr="Let's buy a new car!"),
        fb("Дава'й ___ э'ту рабо'ту сейча'с. (finish it)", ["сде'лаем", "де'лать"], "сде'лаем",
           "To a result: the perfective we-form.", tr="Let's do this work now."),
        mc("What is the form for a suggestion to do something once?",
           ["perfective we-form", "imperfective infinitive", "past tense", "imperative"], "perfective we-form",
           "Дава'й напи'шем.", order=True),
        mc("How do you say “Let's not speak English”?",
           ["Дава'й не говори'ть по-англи'йски!", "Дава'й не скажем по-англи'йски!", "Дава'й не говорю' по-англи'йски!", "Дава'й не говори'л по-англи'йски!"],
           "Дава'й не говори'ть по-англи'йски!", "Negative: не + imperfective."),
        mc("Which form do you use to suggest something to several people?", ["Дава'йте", "Дава'й", "Дам", "Дава'ть"], "Дава'йте",
           "-те = several people or politely."),
    ],
)

# ---------------------------------------------------------------------------- 103
L103 = lesson(
    "Clothes: что ты но́сишь?",
    "Ку'ртка, пла'тье, ша'пка, пальто'",
    requires=["носить", "куртка", "сумка", "платье", "одежда"],
    cards=[
        card("To wear: носи'ть",
             "Носи'ть means to wear (and also to carry). The я form has the stress on the end, then it moves back: "
             "ношу', но'сишь, но'сит. The adjectives мужско'й (men's), же'нский (women's) and де'тский "
             "(children's) agree with the noun.",
             tables=[table(
                 ["Who", "носи'ть"],
                 [["я", "ношу'"], ["ты", "но'сишь"], ["он, она'", "но'сит"],
                  ["мы", "но'сим"], ["вы", "но'сите"], ["они'", "но'сят"]]),
                 table(
                 ["Masculine", "Feminine", "Neuter"],
                 [["мужско'й костю'м", "мужска'я ку'ртка", "мужско'е пальто'"],
                  ["же'нский костю'м", "же'нская су'мка", "же'нское пла'тье"],
                  ["де'тский костю'м", "де'тская ша'пка", "де'тское пальто'"]])]),
        card("Clothes and things you carry",
             "Пальто' never changes. Перча'тки and носки' are usually used in the plural. In the genitive you "
             "can say, for example, В карма'не нет телефо'на.",
             tables=[table(
                 ["Russian", "English"],
                 [["пальто'", "coat"], ["ку'ртка", "jacket"], ["шу'ба", "fur coat"], ["дублёнка", "sheepskin coat"],
                  ["ша'пка", "hat"], ["шарф", "scarf"], ["перча'тки", "gloves"], ["носки'", "socks"],
                  ["пла'тье", "dress"], ["руба'шка", "shirt"], ["су'мка", "bag"], ["карма'н", "pocket"],
                  ["о'бувь", "footwear"], ["оде'жда", "clothing"]])],
             examples=[
                 ex("Сего'дня хо'лодно, и я но'шу ша'пку и шарф.", "It's cold today, and I'm wearing a hat and a scarf.", "но'шу"),
                 ex("Мой брат но'сит мужску'ю ку'ртку.", "My brother wears a men's jacket.", "мужску'ю"),
                 ex("Она' но'сит дублёнку.", "She wears a sheepskin coat.", "но'сит"),
                 ex("В карма'не нет телефо'на.", "There is no phone in the pocket.", "нет телефо'на"),
                 ex("Э'то де'тская ша'пка.", "This is a child's hat.", "де'тская"),
             ]),
    ],
    verify=(vf("носить", "ношу", "носишь", "носит", "носим", "носите", "носят")
            + vf("мужской", "мужской", "мужская", "мужское", "мужскую") + vf("женский", "женский", "женская", "женское")
            + vf("детский", "детский", "детская", "детское") + vf("костюм", "костюм") + vf("куртка", "куртка")
            + vf("сумка", "сумка") + vf("пальто", "пальто") + vf("платье", "платье") + vf("шапка", "шапка")
            + vf("шарф", "шарф") + vf("перчатка", "перчатки") + vf("носок", "носки") + vf("рубашка", "рубашка")
            + vf("обувь", "обувь") + vf("одежда", "одежда") + vf("шуба", "шуба") + vf("дублёнка", "дублёнка")
            + vf("карман", "кармане") + vf("телефон", "телефона")),
    exercises=[
        fb("Он ___ ку'ртку.", ["но'сит", "носи'т", "ношу'", "но'сят"], "но'сит",
           "Он takes но'сит.", tr="He wears a jacket.", lemma="носить"),
        fb("Я ___ ша'пку.", ["ношу'", "но'сишь", "но'сит", "но'сим"], "ношу'",
           "Я takes ношу'.", tr="I wear a hat.", lemma="носить"),
        fb("Э'то ___ пла'тье. (women's)", ["же'нское", "же'нский", "же'нская", "же'нские"], "же'нское",
           "Пла'тье is neuter.", tr="This is a women's dress.", lemma="женский"),
        fb("Э'то ___ ша'пка. (children's)", ["де'тская", "де'тский", "де'тское", "де'тские"], "де'тская",
           "Ша'пка is feminine.", tr="This is a child's hat.", lemma="детский"),
        fb("Э'то ___ костю'м. (men's)", ["мужско'й", "мужска'я", "мужско'е", "мужски'е"], "мужско'й",
           "Костю'м is masculine.", tr="This is a men's suit.", lemma="мужской"),
        fb("В карма'не нет ___.", ["телефо'на", "телефо'н", "телефо'ну", "телефо'ном"], "телефо'на",
           "After нет: the genitive.", tr="There is no phone in the pocket.", lemma="телефон"),
        mc("What is пальто'?", ["a coat", "a hat", "a bag", "a pocket"], "a coat", "Пальто' = coat."),
        mc("Which word means “gloves”?", ["перча'тки", "носки'", "шарф", "карма'н"], "перча'тки", "Перча'тки = gloves."),
        mc("Which word never changes?", ["пальто'", "ку'ртка", "ша'пка", "су'мка"], "пальто'",
           "Пальто' is indeclinable."),
        mc("Which phrase means “a women's bag”?",
           ["же'нская су'мка", "же'нский су'мка", "же'нское су'мка", "же'нские су'мка"], "же'нская су'мка",
           "Су'мка is feminine."),
    ],
)

# ---------------------------------------------------------------------------- 104
L104 = lesson(
    "Show, sell, find, understand",
    "Покажи' мне. Я нашёл. Я поня'л.",
    requires=["показывать", "продавать", "находить", "найти", "понимать"],
    cards=[
        card("Four pairs with unusual perfectives",
             "Four common verbs form their perfective in an unusual way. Learn the pairs: пока'зывать / показа'ть "
             "(to show), продава'ть / прода'ть (to sell), находи'ть / найти' (to find), понима'ть / поня'ть "
             "(to understand). Their perfective future forms follow.",
             tables=[table(
                 ["", "показа'ть", "прода'ть", "найти'", "поня'ть"],
                 [["я", "покажу'", "прода'м", "найду'", "пойму'"],
                  ["ты", "пока'жешь", "прода'шь", "найдёшь", "поймёшь"],
                  ["он, она'", "пока'жет", "прода'ст", "найдёт", "поймёт"],
                  ["мы", "пока'жем", "продади'м", "найдём", "поймём"],
                  ["вы", "пока'жете", "продади'те", "найдёте", "поймёте"],
                  ["они'", "пока'жут", "продаду'т", "найду'т", "пойму'т"]])]),
        card("The past of найти' and поня'ть",
             "Найти' has an irregular masculine past: нашёл, нашла', нашли'. Поня'ть is regular, but the stress "
             "moves: по'нял, поняла', по'няли.",
             tables=[table(
                 ["", "найти'", "поня'ть"],
                 [["он", "нашёл", "по'нял"], ["она'", "нашла'", "поняла'"],
                  ["оно'", "нашло'", "по'няло"], ["они'", "нашли'", "по'няли"]])],
             examples=[
                 ex("Покажи' мне, пожа'луйста, э'ту су'мку.", "Show me this bag, please.", "Покажи'"),
                 ex("Он нашёл но'вую рабо'ту.", "He found a new job.", "нашёл"),
                 ex("Я про'дал свою' ста'рую маши'ну.", "I sold my old car.", "про'дал"),
                 ex("Ты меня' понима'ешь?", "Do you understand me?", "понима'ешь"),
                 ex("Здесь продаю'т о'бувь.", "Shoes are sold here.", "продаю'т"),
             ]),
    ],
    verify=(vf("показать", "покажу", "покажешь", "покажет", "покажем", "покажете", "покажут", "покажи")
            + vf("продать", "продам", "продашь", "продаст", "продадим", "продадите", "продадут", "продал")
            + vf("найти", "найду", "найдёшь", "найдёт", "найдём", "найдёте", "найдут", "нашёл", "нашла", "нашло", "нашли")
            + vf("понять", "пойму", "поймёшь", "поймёт", "поймём", "поймёте", "поймут", "понял", "поняла", "поняло", "поняли")
            + vf("продавать", "продают") + vf("понимать", "понимаешь") + vf("обувь", "обувь")),
    exercises=[
        fb("За'втра я ___ тебе' э'ту су'мку.", ["покажу'", "пока'зываю", "пока'жет", "показа'л"], "покажу'",
           "Я takes -у: покажу'.", tr="Tomorrow I will show you this bag.", lemma="показать"),
        fb("Он ___ но'вую рабо'ту. (past)", ["нашёл", "нашла'", "нашли'", "найдёт"], "нашёл",
           "Masculine past of найти'.", tr="He found a new job.", lemma="найти"),
        fb("Она' ___ мою' су'мку. (past)", ["нашла'", "нашёл", "нашли'", "найдёт"], "нашла'",
           "Feminine past of найти'.", tr="She found my bag.", lemma="найти"),
        fb("Я не ___ э'то сло'во. (past)", ["по'нял", "поняла'", "по'няли", "поймёт"], "по'нял",
           "Masculine past of поня'ть.", tr="I didn't understand this word.", lemma="понять"),
        fb("Мы ___ э'ту маши'ну за'втра.", ["продади'м", "прода'м", "продаду'т", "прода'ст"], "продади'м",
           "Мы takes -им: продади'м.", tr="We will sell this car tomorrow.", lemma="продать"),
        fb("Вы ___ э'то письмо'? (will find)", ["найдёте", "найдёшь", "найду'", "найду'т"], "найдёте",
           "Вы takes -ёте.", tr="Will you find this letter?", lemma="найти"),
        fb("Они' ___ мне доро'гу. (will show)", ["пока'жут", "покажу'", "пока'жешь", "пока'жем"], "пока'жут",
           "Они' takes -ут.", tr="They will show me the way.", lemma="показать"),
        mc("Which is the perfective of находи'ть?", ["найти'", "находи'ть", "нашёл", "найду'т"], "найти'",
           "Находи'ть / найти'."),
        mc("What is the perfective of понима'ть?", ["поня'ть", "понима'ться", "понима'л", "поню'"], "поня'ть",
           "Понима'ть / поня'ть."),
    ],
)

# ---------------------------------------------------------------------------- 105
L105 = lesson(
    "Better, worse, more, less",
    "Э'та ку'ртка лу'чше, чем та.",
    requires=["хороший", "плохой", "большой", "маленький", "намного"],
    cards=[
        card("Four words that do not change",
             "Four useful comparative words never change for gender or number: лу'чше (better), ху'же (worse), "
             "бо'льше (bigger, more) and ме'ньше (smaller, less, fewer). To compare, put чем (than) before the "
             "second thing, which stays in the nominative. Намно'го means “much”: намно'го лу'чше.",
             tables=[table(
                 ["Word", "Meaning", "Example"],
                 [["лу'чше", "better", "Э'та ку'ртка лу'чше, чем та."],
                  ["ху'же", "worse", "Моя' су'мка ху'же, чем твоя'."],
                  ["бо'льше", "bigger, more", "Москва' бо'льше, чем наш го'род."],
                  ["ме'ньше", "smaller, less", "Э'та ко'мната ме'ньше, чем моя'."]])],
             examples=[
                 ex("Э'то пла'тье намно'го лу'чше.", "This dress is much better.", "намно'го лу'чше"),
                 ex("Э'ти ку'ртки лу'чше, чем те.", "These jackets are better than those.", "лу'чше, чем"),
                 ex("У неё бо'льше вре'мени, чем у меня'.", "She has more time than I do.", "бо'льше вре'мени"),
                 ex("Э'та су'мка намно'го ху'же.", "This bag is much worse.", "намно'го ху'же"),
             ]),
    ],
    verify=vf("время", "времени"),
    exercises=[
        fb("Э'та ку'ртка ___, чем та. (better)", ["лу'чше", "ху'же", "бо'льше", "ме'ньше"], "лу'чше",
           "Лу'чше = better.", tr="This jacket is better than that one."),
        fb("Моя' су'мка ___, чем твоя'. (worse)", ["ху'же", "лу'чше", "бо'льше", "ме'ньше"], "ху'же",
           "Ху'же = worse.", tr="My bag is worse than yours."),
        fb("Москва' ___, чем наш го'род. (bigger)", ["бо'льше", "ме'ньше", "лу'чше", "ху'же"], "бо'льше",
           "Бо'льше = bigger.", tr="Moscow is bigger than our city."),
        fb("Э'та ко'мната ___, чем моя'. (smaller)", ["ме'ньше", "бо'льше", "лу'чше", "ху'же"], "ме'ньше",
           "Ме'ньше = smaller.", tr="This room is smaller than mine."),
        fb("Э'то пла'тье ___ лу'чше. (much)", ["намно'го", "о'чень", "ма'ло", "совсе'м"], "намно'го",
           "Намно'го goes before a comparative.", tr="This dress is much better."),
        fb("У неё бо'льше вре'мени, ___ у меня'.", ["чем", "что", "как", "и"], "чем",
           "Чем = than.", tr="She has more time than I do."),
        mc("Which word means “worse”?", ["ху'же", "лу'чше", "бо'льше", "ме'ньше"], "ху'же", "Ху'же."),
        mc("Which sentence is correct?",
           ["Э'та ку'ртка лу'чше, чем та.", "Э'та ку'ртка лу'чше, что та.", "Э'та ку'ртка лу'чше, как та.", "Э'та ку'ртка лу'чше та."],
           "Э'та ку'ртка лу'чше, чем та.", "Чем = than."),
        mc("Do лу'чше and бо'льше change for gender?", ["no", "yes, like adjectives", "only in the plural", "only for feminine"], "no",
           "They never change.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 106
L106 = lesson(
    "Five hundred to nine hundred",
    "Пятьсо'т, шестьсо'т, семьсо'т, восемьсо'т, девятьсо'т",
    requires=["рубль", "цена", "стоить", "тысяча", "куртка"],
    cards=[
        card("Hundreds from 500",
             "From 500 the hundreds are written as one word: пять + сот, шесть + сот and so on. The stress is on "
             "the last syllable (пятьсо'т). Together with 200, 300 and 400 you now have every hundred: сто, две'сти, "
             "три'ста, четы'реста, пятьсо'т, шестьсо'т, семьсо'т, восемьсо'т, девятьсо'т.",
             tables=[table(
                 ["Number", "Word"],
                 [["500", "пятьсо'т"], ["600", "шестьсо'т"], ["700", "семьсо'т"], ["800", "восемьсо'т"],
                  ["900", "девятьсо'т"]])]),
        card("Prices",
             "Combine them with the numbers you know: пятьсо'т два'дцать пять is 525. In a price the word рубле'й "
             "follows (you learned it in lesson 92).",
             examples=[
                 ex("Ско'лько сто'ит э'та ку'ртка?", "How much does this jacket cost?", "сто'ит"),
                 ex("Она' сто'ит пятьсо'т рубле'й.", "It costs five hundred rubles.", "пятьсо'т рубле'й"),
                 ex("Э'та су'мка сто'ит семьсо'т рубле'й.", "This bag costs seven hundred rubles.", "семьсо'т"),
                 ex("Ша'пка сто'ит шестьсо'т два'дцать пять рубле'й.", "The hat costs 625 rubles.", "шестьсо'т"),
                 ex("Ку'ртка сто'ит девятьсо'т рубле'й.", "The jacket costs 900 rubles.", "девятьсо'т"),
             ]),
    ],
    verify=(vf("пятьсот", "пятьсот") + vf("шестьсот", "шестьсот") + vf("семьсот", "семьсот")
            + vf("восемьсот", "восемьсот") + vf("девятьсот", "девятьсот") + vf("стоить", "стоит")
            + vf("рубль", "рублей")),
    exercises=[
        fb("500 = ___", ["пятьсо'т", "шестьсо'т", "семьсо'т", "пятьдеся'т"], "пятьсо'т", "5 × 100.", tr="500"),
        fb("700 = ___", ["семьсо'т", "се'мьдесят", "шестьсо'т", "восемьсо'т"], "семьсо'т", "7 × 100.", tr="700"),
        fb("900 = ___", ["девятьсо'т", "девяно'сто", "восемьсо'т", "девятна'дцать"], "девятьсо'т", "9 × 100.", tr="900"),
        fb("Три'ста плюс три'ста — э'то ___.", ["шестьсо'т", "пятьсо'т", "семьсо'т", "две'сти"], "шестьсо'т",
           "300 + 300 = 600.", tr="Three hundred plus three hundred is six hundred."),
        fb("Две'сти плюс пятьсо'т — э'то ___.", ["семьсо'т", "шестьсо'т", "восемьсо'т", "пятьсо'т"], "семьсо'т",
           "200 + 500 = 700.", tr="Two hundred plus five hundred is seven hundred."),
        fb("Ку'ртка сто'ит ___ рубле'й. (800)", ["восемьсо'т", "восемьдесят", "восемна'дцать", "восьмо'й"], "восемьсо'т",
           "800.", tr="The jacket costs 800 rubles."),
        mc("Which number is 600?", ["шестьсо'т", "шестьдеся'т", "шестна'дцать", "шесто'й"], "шестьсо'т", "Шесть + сот."),
        mc("Where is the stress in пятьсо'т, шестьсо'т, семьсо'т?",
           ["on the last syllable", "on the first syllable", "on the middle syllable", "there is none"],
           "on the last syllable", "The ending -сот is stressed.", order=True),
        mc("How do you say 525?",
           ["пятьсо'т два'дцать пять", "пятьдеся'т пять сто", "сто пять два'дцать", "пять сто два'дцать пять"],
           "пятьсо'т два'дцать пять", "Hundreds first, then tens, then units."),
    ],
)

# ---------------------------------------------------------------------------- 107
L107 = lesson(
    "Review: absence, numbers and aspect",
    "Putting lessons 95 to 106 together",
    requires=["нет", "дождь", "куртка", "хороший", "рубль"],
    cards=[
        card("What you can do now",
             "You can say what is missing (нет, не́ было, не бу'дет + genitive), use the genitive of pronouns "
             "(у него', без неё), use the genitive singular after два, три and четы'ре, choose the aspect with "
             "time expressions, negation, sudden actions and suggestions, talk about clothes, compare with "
             "лу'чше, ху'же, бо'льше and ме'ньше, and say hundreds up to 900.",
             tables=[table(
                 ["Topic", "Remember"],
                 [["Missing now", "У меня' нет бра'та."],
                  ["Missing before and later", "не́ было дождя' · не бу'дет конце'рта"],
                  ["After 2, 3, 4", "два стола' · две кни'ги · три окна'"],
                  ["For how long, in how long", "чита'л три часа' · прочита'л за три часа'"],
                  ["Didn't try, didn't manage", "не учи'л · не вы'учил"],
                  ["Let's", "Дава'й говори'ть · Дава'й напи'шем"],
                  ["Compare", "лу'чше, чем … · бо'льше, чем …"]])]),
    ],
    verify=[],
    exercises=[
        fb("У меня' нет ___.", ["бра'та", "брат", "бра'ту", "бра'том"], "бра'та",
           "After нет: the genitive.", tr="I don't have a brother.", lemma="брат"),
        fb("Вчера' не́ было ___.", ["дождя'", "дождь", "дождём", "дожде'"], "дождя'",
           "After не́ было: the genitive.", tr="There was no rain yesterday.", lemma="дождь"),
        fb("У ___ нет вре'мени. (him)", ["него'", "его'", "ему'", "ним"], "него'",
           "After у: него'.", tr="He has no time.", lemma="он"),
        fb("У меня' три ___.", ["сестры'", "сестра'", "сестру'", "сестре'"], "сестры'",
           "After три: the genitive singular.", tr="I have three sisters.", lemma="сестра"),
        fb("Я прочита'л кни'гу ___ два часа'.", ["за", "в", "о", "из"], "за",
           "Completion in a time: за + perfective.", tr="I finished the book in two hours."),
        fb("Дава'й ___ расска'з! (once)", ["напи'шем", "писа'ть", "пишу'", "писа'л"], "напи'шем",
           "Once: the perfective we-form.", tr="Let's write a story!"),
        fb("Э'та ку'ртка ___, чем та. (better)", ["лу'чше", "ху'же", "бо'льше", "ме'ньше"], "лу'чше",
           "Лу'чше = better.", tr="This jacket is better than that one."),
        fb("Ку'ртка сто'ит ___ рубле'й. (500)", ["пятьсо'т", "пятьдеся'т", "шестьсо'т", "пять"], "пятьсо'т",
           "500.", tr="The jacket costs 500 rubles."),
        fb("Как то'лько он уви'дел су'мку, он сра'зу ___ её.", ["купи'л", "покупа'л"], "купи'л",
           "A quick action: perfective.", tr="As soon as he saw the bag, he bought it right away."),
        mc("What case follows нет?", ["genitive", "nominative", "accusative", "prepositional"], "genitive",
           "Нет + genitive.", order=True),
        mc("Which sentence is correct?",
           ["Вчера' не́ было дождя'.", "Вчера' не была дождя'.", "Вчера' не́ были дождя'.", "Вчера' не́ был дождя'."],
           "Вчера' не́ было дождя'.", "Не́ было never changes."),
        mc("How do you say “four windows”?", ["четы'ре окна'", "четы'ре окно'", "четы'ре о'кон", "четы'ре окну'"],
           "четы'ре окна'", "Четы'ре + genitive singular."),
    ],
)

UNIT = unit("Unit 13: Absence, small numbers, clothes and comparing",
            [L95, L96, L97, L98, L99, L100, L101, L102, L103, L104, L105, L106, L107])
