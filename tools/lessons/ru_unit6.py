"""Unit 6: past tense, going places, and everyday sentences  (textbook lessons 8-9, review)."""
from dsl import *

# ---------------------------------------------------------------------------- 34
L34 = lesson(
    "The past tense of verbs",
    "Чита'л, чита'ла, чита'ло, чита'ли",
    requires=["вчера", "читать", "писать", "говорить", "видеть"],
    cards=[
        card("Drop -ть, add -л",
             "To make the past tense, take the infinitive, drop -ть, and add -л plus an ending for the gender "
             "or number of the subject: nothing for masculine, -а for feminine, -о for neuter, -и for plural. "
             "You have already seen this pattern in был, была', бы'ло, бы'ли. Tap a row to hear it.",
             tables=[table(
                 ["", "он", "она'", "оно'", "они' · мы · вы"],
                 [["чита'ть", "чита'{л}", "чита'{ла}", "чита'{ло}", "чита'{ли}"],
                  ["писа'ть", "писа'{л}", "писа'{ла}", "писа'{ло}", "писа'{ли}"],
                  ["говори'ть", "говори'{л}", "говори'{ла}", "говори'{ло}", "говори'{ли}"],
                  ["ви'деть", "ви'де{л}", "ви'де{ла}", "ви'де{ло}", "ви'де{ли}"],
                  ["жить", "жи{л}", "жил{а'}", "жи'{ло}", "жи'{ли}"]],
                 note="In the past the verb shows only gender and number, never the person.")]),
        card("Gender and number only",
             "In the present tense the verb shows the person (я чита'ю, ты чита'ешь). In the past it shows only "
             "gender and number, exactly like быть. So я, ты and он, all masculine, use the same form. A woman "
             "says я чита'ла, and вы always takes the plural, even for one polite person. Irregular present "
             "stems do not matter: писа'ть gives писа'л, not пиша'л.",
             examples=[
                 ex("Вчера' я чита'л журна'л.", "Yesterday I read a magazine. (a man speaking)", "чита'л"),
                 ex("Вчера' я чита'ла журна'л.", "Yesterday I read a magazine. (a woman speaking)", "чита'ла"),
                 ex("Она' писа'ла письмо'.", "She was writing a letter.", "писа'ла"),
                 ex("Мы ви'дели э'тот фильм.", "We saw this film.", "ви'дели"),
                 ex("Вы говори'ли по-ру'сски?", "Did you speak Russian? (polite)", "говори'ли"),
             ]),
    ],
    verify=(vf("читать", "читал", "читала", "читало", "читали")
            + vf("писать", "писал", "писала", "писало", "писали")
            + vf("говорить", "говорил", "говорила", "говорило", "говорили")
            + vf("видеть", "видел", "видела", "видело", "видели")
            + vf("жить", "жил", "жила", "жило", "жили")),
    exercises=[
        fb("Вчера' я ___ кни'гу.", ["чита'л", "чита'ла", "чита'ло", "чита'ли"], "чита'л",
           "A man speaking: masculine.", tr="Yesterday I read a book. (a man speaking)", lemma="читать"),
        fb("Вчера' она' ___ письмо'.", ["писа'ла", "писа'л", "писа'ло", "писа'ли"], "писа'ла",
           "Она' is feminine.", tr="Yesterday she wrote a letter.", lemma="писать"),
        fb("Вчера' мы ___ фильм.", ["ви'дели", "ви'дел", "ви'дела", "ви'дело"], "ви'дели",
           "Мы is plural.", tr="Yesterday we saw a film.", lemma="видеть"),
        fb("Вчера' я ___ письмо'.", ["писа'ла", "писа'л", "писа'ло", "писа'ли"], "писа'ла",
           "A woman speaking: feminine.", tr="Yesterday I wrote a letter. (a woman speaking)", lemma="писать"),
        fb("Вы вчера' ___ по-ру'сски?", ["говори'ли", "говори'л", "говори'ла", "говори'ло"], "говори'ли",
           "Вы always takes the plural.", tr="Did you speak Russian yesterday? (one person, polite)", lemma="говорить"),
        fb("Де'ти слу'шали ___.", ["му'зыку", "му'зыка", "му'зыки", "му'зыке"], "му'зыку",
           "A direct object: feminine in -а takes -у.", tr="The children listened to music."),
        fb("Они' до'лго ___ здесь.", ["жи'ли", "жил", "жила'", "жи'ло"], "жи'ли",
           "Они' is plural.", tr="They lived here for a long time.", lemma="жить"),
        mc("What do you drop from an infinitive to make the past tense?", ["-ть", "the first letter", "-ешь", "nothing"],
           "-ть", "Чита'ть → чита'-, then add -л and the ending.", order=True),
        mc("A woman says “I was reading a book.” Which is correct?",
           ["Я чита'ла кни'гу.", "Я чита'л кни'гу.", "Я чита'ло кни'гу.", "Я чита'ли кни'гу."],
           "Я чита'ла кни'гу.", "The verb follows the speaker's gender."),
        mc("In the past tense, what does the verb agree with?",
           ["Gender and number", "Person", "Nothing", "The object"], "Gender and number",
           "That is why я, ты and он all take the same masculine form.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 35
L35 = lesson(
    "Two aspects: the process and the result",
    "Писа'л / написа'л, покупа'л / купи'л",
    requires=["купить", "написать", "сделать", "делать", "писать"],
    cards=[
        card("Most verbs come in pairs",
             "Most Russian verbs have two partners, called aspects. The imperfective names the activity: it "
             "stresses the process, the duration or the repetition. The perfective names one finished action "
             "and its result. Almost every verb you have learned so far is imperfective. The perfective partner "
             "is usually the same verb with a prefix (писа'ть → написа'ть), though some pairs are different words "
             "(покупа'ть → купи'ть). Learn them as pairs.",
             tables=[table(
                 ["Imperfective (activity)", "Perfective (result)", "Meaning"],
                 [["покупа'ть", "купи'ть", "to buy"],
                  ["чита'ть", "прочита'ть", "to read"],
                  ["писа'ть", "написа'ть", "to write"],
                  ["де'лать", "сде'лать", "to do, to make"],
                  ["продава'ть", "прода'ть", "to sell"]])]),
        card("Which one do I need?",
             "In the past tense, ask yourself: am I describing the activity, or telling that it got done? Words "
             "like весь ве'чер (all evening), до'лго (for a long time), ча'сто (often) and ка'ждый день (every day) "
             "point to the imperfective. Words like наконе'ц (finally) and уже' (already), or a single "
             "result you can show, point to the perfective. The perfective has no ordinary present tense, so for "
             "what is happening now you always use the imperfective.",
             examples=[
                 ex("Вчера' я весь ве'чер чита'л кни'гу.", "Yesterday I read a book all evening. (process)", "чита'л"),
                 ex("Вчера' я прочита'л э'ту кни'гу.", "Yesterday I read this book through. (finished)", "прочита'л"),
                 ex("Он до'лго писа'л письмо'.", "He wrote a letter for a long time. (process)", "писа'л"),
                 ex("Наконе'ц он написа'л письмо'!", "He finally wrote the letter! (result)", "написа'л"),
                 ex("Вот моя' но'вая маши'на. Я купи'л её вчера'.", "Here is my new car. I bought it yesterday.", "купи'л"),
             ]),
    ],
    verify=vf("купить", "купил") + vf("прочитать", "прочитал") + vf("написать", "написал")
           + vf("сделать", "сделал") + vf("продать", "продал"),
    exercises=[
        fb("Вчера' я весь ве'чер ___ письмо'.", ["писа'л", "написа'л"], "писа'л",
           "Весь ве'чер shows duration: imperfective.", tr="Yesterday I wrote a letter all evening."),
        fb("Наконе'ц я ___ письмо'!", ["написа'л", "писа'л"], "написа'л",
           "Наконе'ц points to a finished result: perfective.", tr="I finally wrote the letter!"),
        fb("Вот моя' но'вая маши'на! Я ___ её вчера'.", ["купи'л", "покупа'л"], "купи'л",
           "One completed purchase with a result you can show.", tr="Here is my new car! I bought it yesterday."),
        fb("Она' ча'сто ___ кни'ги.", ["чита'ла", "прочита'ла"], "чита'ла",
           "Ча'сто shows repetition: imperfective.", tr="She often read books."),
        fb("Он уже' ___ уро'к.", ["сде'лал", "де'лал"], "сде'лал",
           "Уже' says it is already done: perfective.", tr="He has already done the lesson."),
        fb("Что ты ___ вчера' ве'чером?", ["де'лал", "сде'лал"], "де'лал",
           "Asking about the activity itself: imperfective.", tr="What were you doing yesterday evening?"),
        mc("Which aspect tells of a finished result?", ["perfective", "imperfective", "both", "neither"], "perfective",
           "The perfective names a completed action.", order=True),
        mc("Which verb is the perfective partner of покупа'ть?",
           ["купи'ть", "продава'ть", "смотре'ть", "писа'ть"], "купи'ть", "Покупа'ть / купи'ть: to buy."),
        mc("Which sentence says you finished the book?",
           ["Я прочита'л кни'гу.", "Я чита'л кни'гу.", "Я чита'ю кни'гу.", "Я не чита'л кни'гу."],
           "Я прочита'л кни'гу.", "The perfective with a prefix names the result."),
        mc("Which aspect do you use for what is happening right now?",
           ["imperfective", "perfective", "either one", "neither"], "imperfective",
           "The perfective has no ordinary present tense.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 36
L36 = lesson(
    "Where at? Where to?",
    "Где? в шко'ле — Куда'? в шко'лу",
    requires=["школа", "магазин", "библиотека", "почта", "куда"],
    cards=[
        card("Two questions, two cases",
             "English says “where” for both rest and movement, and then adds a preposition. Russian has two "
             "question words and the case does the work. Где? (where at?) takes в or на with the prepositional case: "
             "the place where something is. Куда'? (where to?) takes в or на with the accusative: the place "
             "someone is heading for. Which preposition each noun takes (в or на) is the same for both questions.",
             tables=[table(
                 ["Place", "Где? (at)", "Куда'? (to)"],
                 [["шко'ла", "в шко'л{е}", "в шко'л{у}"],
                  ["магази'н", "в магази'н{е}", "в магази'н"],
                  ["библиоте'ка", "в библиоте'к{е}", "в библиоте'к{у}"],
                  ["по'чта", "на по'чт{е}", "на по'чт{у}"],
                  ["стадио'н", "на стадио'н{е}", "на стадио'н"],
                  ["уро'к", "на уро'к{е}", "на уро'к"],
                  ["кафе' · кино'", "в кафе' · в кино'", "в кафе' · в кино'"]],
                 note="Nouns that never change (кафе', кино') look the same both ways: only the question tells you.")],
             examples=[
                 ex("Где ты? — Я в шко'ле.", "Where are you? — I'm at school.", "в шко'ле"),
                 ex("Куда' ты идёшь? — Я иду' в шко'лу.", "Where are you going? — I'm going to school.", "в шко'лу"),
                 ex("Ма'ма на по'чте.", "Mom is at the post office.", "на по'чте"),
                 ex("Ма'ма идёт на по'чту.", "Mom is going to the post office.", "на по'чту"),
             ]),
        card("Here, there, home",
             "A few small words also come in two forms, one for each question. Learn them as pairs.",
             tables=[table(
                 ["Где? (at)", "Куда'? (to)"],
                 [["здесь · тут (here)", "сюда' (here, to this place)"],
                  ["там (there)", "туда' (there, to that place)"],
                  ["до'ма (at home)", "домо'й (home, homeward)"]])],
             examples=[
                 ex("Я до'ма.", "I'm at home.", "до'ма"),
                 ex("Я иду' домо'й.", "I'm going home.", "домо'й"),
             ]),
    ],
    verify=(vf("школа", "школе", "школу") + vf("библиотека", "библиотеке", "библиотеку")
            + vf("почта", "почте", "почту") + vf("магазин", "магазине") + vf("стадион", "стадионе")
            + vf("урок", "уроке")),
    exercises=[
        fb("Где ты? — Я ___.", ["в шко'ле", "в шко'лу", "на шко'ле", "в шко'ла"], "в шко'ле",
           "Где? needs the prepositional.", tr="Where are you? — I'm at school."),
        fb("Куда' ты идёшь? — Я иду' ___.", ["в шко'лу", "в шко'ле", "на шко'лу", "в шко'ла"], "в шко'лу",
           "Куда'? needs the accusative: шко'ла → шко'лу.", tr="Where are you going? — I'm going to school."),
        fb("Где ма'ма? — Она' ___.", ["на по'чте", "на по'чту", "в по'чте", "на по'чта"], "на по'чте",
           "По'чта takes на; where at → prepositional.", tr="Where is mom? — She's at the post office."),
        fb("Куда' он идёт? — Он идёт ___.", ["на по'чту", "на по'чте", "в по'чту", "на по'чта"], "на по'чту",
           "Where to → accusative: по'чта → по'чту.", tr="Where is he going? — He's going to the post office."),
        fb("Где они'? — Они' ___.", ["на стадио'не", "на стадио'н", "в стадио'не", "на стадио'ну"], "на стадио'не",
           "Стадио'н takes на; where at → prepositional.", tr="Where are they? — They're at the stadium."),
        fb("Куда' вы идёте? — Мы идём ___.", ["на уро'к", "на уро'ке", "в уро'к", "на уро'ку"], "на уро'к",
           "A masculine thing doesn't change in the accusative.", tr="Where are you going? — We're going to a lesson."),
        fb("Куда' ты идёшь? — Я иду' ___.", ["домо'й", "до'ма", "в до'ме", "домо'м"], "домо'й",
           "Домо'й is the “going home” word. До'ма means “at home”.", tr="Where are you going? — I'm going home."),
        mc("Which question word asks about location?", ["Где?", "Куда'?", "Когда'?", "Что?"], "Где?",
           "Где? = where at? Куда'? = where to?", order=True),
        mc("Which case answers Куда'??", ["accusative", "prepositional", "nominative", "genitive"], "accusative",
           "Motion toward a place takes the accusative.", order=True),
        mc("Which sentence says you are going to the library?",
           ["Я иду' в библиоте'ку.", "Я иду' в библиоте'ке.", "Я иду' на библиоте'ку.", "Я иду' в библиоте'ка."],
           "Я иду' в библиоте'ку.", "Куда'? → в + accusative."),
    ],
)

# ---------------------------------------------------------------------------- 37
L37 = lesson(
    "Going on foot: идти'",
    "Иду', идёшь, идёт",
    requires=["идти", "куда", "туда", "сюда", "домой"],
    cards=[
        card("Идти' in the present and past",
             "Идти' means to go on foot, in one direction. It is irregular but follows the first-conjugation "
             "pattern in the present. The past tense is also irregular: шёл, шла, шло, шли.",
             tables=[table(
                 ["Person", "Present", "Past"],
                 [["я", "ид{у'}", "я шёл · шла"],
                  ["ты", "ид{ёшь}", "ты шёл · шла"],
                  ["он · она' · оно'", "ид{ёт}", "шёл · шла · шло"],
                  ["мы", "ид{ём}", "мы шли"],
                  ["вы", "ид{ёте}", "вы шли"],
                  ["они'", "ид{у'т}", "они' шли"]],
                 note="Command: иди'! (to a friend), иди'те! (polite or to a group).")]),
        card("Where to?",
             "Say where you are going with в or на and the accusative, or with a little word like домо'й, "
             "туда' or сюда'. People also use идти' for events in town: you go to a concert or to the movies. "
             "The verb has other, figurative uses too.",
             examples=[
                 ex("Я иду' в магази'н.", "I'm going to the store.", "иду'"),
                 ex("Куда' вы идёте? — Мы идём домо'й.", "Where are you going? — We're going home.", "идёте"),
                 ex("Они' иду'т на конце'рт.", "They're going to a concert.", "иду'т"),
                 ex("Иди' сюда'!", "Come here!", "Иди'"),
                 ex("В кино' идёт но'вый фильм.", "A new film is on at the cinema.", "идёт"),
                 ex("Идёт снег.", "It's snowing.", "Идёт"),
             ]),
    ],
    verify=vf("идти", "иду", "идёшь", "идёт", "идём", "идёте", "идут", "иди", "идите", "шёл", "шла", "шло", "шли"),
    exercises=[
        fb("Я ___ в магази'н.", ["иду'", "идёшь", "идёт", "идём"], "иду'",
           "Я takes иду'.", tr="I'm going to the store.", lemma="идти"),
        fb("Куда' ты ___?", ["идёшь", "иду'", "идёт", "идут"], "идёшь",
           "Ты takes идёшь.", tr="Where are you going?", lemma="идти"),
        fb("Ма'ма ___ на по'чту.", ["идёт", "идёшь", "иду'", "идём"], "идёт",
           "Она' and a singular noun take идёт.", tr="Mom is going to the post office.", lemma="идти"),
        fb("Мы ___ домо'й.", ["идём", "идёт", "идёте", "идут"], "идём",
           "Мы takes идём.", tr="We're going home.", lemma="идти"),
        fb("Они' ___ на конце'рт.", ["идут", "идёт", "идёте", "идём"], "идут",
           "Они' takes идут.", tr="They're going to a concert.", lemma="идти"),
        fb("Вчера' она' ___ домо'й.", ["шла", "шёл", "шло", "шли"], "шла",
           "Past: она' → шла.", tr="Yesterday she went home.", lemma="идти"),
        fb("___ сюда', пожа'луйста! (to a friend)", ["Иди'", "Иди'те", "Идёт", "Идти'"], "Иди'",
           "The command to a friend is иди'.", tr="Come here, please!", lemma="идти"),
        mc("Which preposition and case answer Куда' ты идёшь? — … магази'н?",
           ["в + accusative", "в + prepositional", "на + prepositional", "у + nominative"], "в + accusative",
           "Where to → accusative.", order=True),
        mc("What does идёт mean in В кино' идёт фильм?",
           ["is playing", "is walking", "is going home", "is sitting"], "is playing",
           "Идти' also means “to be on”, for films, lessons and snow.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 38
L38 = lesson(
    "How you do it: adverbs in -о",
    "Хорошо', пло'хо, бы'стро, по-ру'сски",
    requires=["быстро", "медленно", "хороший", "плохой", "красивый"],
    cards=[
        card("From adjective to adverb",
             "An adverb says how, where or when something is done. Many adverbs are made from an adjective by "
             "swapping its ending for -о. An adverb never changes. Compare Он хоро'ший студе'нт (adjective, "
             "agrees with студе'нт) with Он хорошо' говори'т (adverb, describes говори'т). A few change a "
             "little on the way: плохо'й → пло'хо, лёгкий → легко'.",
             tables=[table(
                 ["Adjective", "Adverb", "Meaning"],
                 [["краси'вый", "краси'в{о}", "beautifully"],
                  ["интере'сный", "интере'сн{о}", "interestingly"],
                  ["хоро'ший", "хорош{о'}", "well"],
                  ["плохо'й", "пло'х{о}", "badly"],
                  ["бы'стрый", "бы'стр{о}", "quickly"],
                  ["ме'дленный", "ме'дленн{о}", "slowly"],
                  ["лёгкий", "легк{о'}", "easily"],
                  ["тру'дный", "тру'дн{о}", "with difficulty"]])],
             examples=[
                 ex("Он хорошо' говори'т по-ру'сски.", "He speaks Russian well.", "хорошо'"),
                 ex("Она' бы'стро чита'ет.", "She reads quickly.", "бы'стро"),
                 ex("Я пло'хо пишу' по-англи'йски.", "I write English badly.", "пло'хо"),
             ]),
        card("In Russian, and how much",
             "To say that you do something in a language, use по- plus the adverb: по-ру'сски, по-англи'йски. Four "
             "little words tell how much or how often you do an action: мно'го (a lot), немно'го (a little), "
             "ма'ло (little, not enough) and то'лько (only). For now, use them with verbs.",
             examples=[
                 ex("Вы говори'те по-ру'сски?", "Do you speak Russian?", "по-ру'сски"),
                 ex("Да, немно'го.", "Yes, a little.", "немно'го"),
                 ex("Он мно'го рабо'тает.", "He works a lot.", "мно'го"),
                 ex("Она' ма'ло говори'т.", "She doesn't talk much.", "ма'ло"),
                 ex("Мы то'лько чита'ем.", "We only read.", "то'лько"),
             ]),
    ],
    verify=vf("хороший", "хорошо") + vf("плохой", "плохо") + vf("быстрый", "быстро"),
    exercises=[
        fb("Он ___ говори'т по-ру'сски.", ["хорошо'", "хоро'ший", "хоро'шая", "хоро'шие"], "хорошо'",
           "An adverb describes the verb, and never changes.", tr="He speaks Russian well."),
        fb("Э'то ___ студе'нт.", ["хоро'ший", "хорошо'", "хоро'шая", "хоро'шие"], "хоро'ший",
           "A noun needs an adjective that agrees with it.", tr="This is a good student."),
        fb("Она' ___ чита'ет.", ["бы'стро", "бы'страя", "бы'стрый", "бы'стрые"], "бы'стро",
           "Describing the verb: adverb.", tr="She reads quickly."),
        fb("Мы говори'м ___.", ["по-ру'сски", "ру'сский", "по ру'сски", "ру'сски"], "по-ру'сски",
           "Languages use по-…-ски.", tr="We speak Russian."),
        fb("Она' ___ рабо'тает: весь день и весь ве'чер.", ["мно'го", "ма'ло", "немно'го", "то'лько"], "мно'го",
           "All day and all evening is a lot.", tr="She works a lot: all day and all evening."),
        fb("Я ___ понима'ю по-испа'нски: я зна'ю то'лько «приве'т».", ["ма'ло", "мно'го", "о'чень", "бы'стро"], "ма'ло",
           "Knowing a single word is not enough.", tr="I understand little Spanish: I only know “hi”."),
        mc("Which word never changes?", ["хорошо'", "хоро'ший", "хоро'шая", "хоро'шие"], "хорошо'",
           "An adverb has one form."),
        mc("What is the adverb from плохо'й?", ["пло'хо", "плохо'", "пло'хой", "плохи'й"], "пло'хо",
           "Note the stress: it moves to the first syllable."),
        mc("How do you say “I speak English a little”?",
           ["Я немно'го говорю' по-англи'йски.", "Я немно'го говорю' англи'йский.", "Я говорю' немно'го по англи'йски.",
            "Я говорю' по-англи'йски немно'гий."],
           "Я немно'го говорю' по-англи'йски.", "Use по-…-ски for the language, and немно'го for “a little”."),
    ],
)

# ---------------------------------------------------------------------------- 39
L39 = lesson(
    "Sentences with no subject: мо'жно, нельзя'",
    "Здесь мо'жно чита'ть. Здесь краси'во.",
    requires=["можно", "нельзя", "курить", "читать", "библиотека"],
    cards=[
        card("Allowed and not allowed",
             "Мо'жно means “it is allowed, one may” and нельзя' means “it is not allowed, one may not”. Neither has "
             "a subject, and the verb that follows is an infinitive. Such sentences are called impersonal. "
             "On their own they make a short answer: Мо'жно? — Нельзя'!",
             tables=[table(
                 ["Word", "Meaning", "Example"],
                 [["{мо'жно}", "it is allowed", "В библиоте'ке мо'жно чита'ть."],
                  ["{нельзя'}", "it is not allowed", "Здесь нельзя' кури'ть."]])],
             examples=[
                 ex("Мо'жно зада'ть вопро'с?", "May I ask a question?", "Мо'жно"),
                 ex("— Здесь мо'жно кури'ть? — Нет, нельзя'.", "— May one smoke here? — No, one may not.", "нельзя'"),
             ]),
        card("It is easy, it was hard",
             "The same idea works with the adverbs you just learned. Russian says Чита'ть легко' (literally “to "
             "read easy”) where English says “It is easy to read”. There is no it and no verb. In the past you "
             "add бы'ло, the neuter form of быть, which is why it stays the same whatever the infinitive is.",
             tables=[table(
                 ["Now", "Then"],
                 [["Здесь краси'во.", "Здесь {бы'ло} краси'во."],
                  ["Учи'ть слова' тру'дно.", "Учи'ть слова' {бы'ло} тру'дно."],
                  ["Чита'ть легко'.", "Чита'ть {бы'ло} легко'."]])]),
    ],
    verify=vf("быть", "было"),
    exercises=[
        fb("В библиоте'ке ___ говори'ть гро'мко.", ["нельзя'", "мо'жно", "бы'ло", "нет"], "нельзя'",
           "In a library you shouldn't talk loudly.", tr="In the library one may not talk loudly."),
        fb("___ зада'ть вопро'с?", ["Мо'жно", "Нельзя'", "Бы'ло", "Мой"], "Мо'жно",
           "That's the polite way to ask for permission.", tr="May I ask a question?"),
        fb("Здесь ___ кури'ть: э'то шко'ла.", ["нельзя'", "мо'жно", "бы'ло", "легко'"], "нельзя'",
           "It's not allowed at a school.", tr="You can't smoke here: this is a school."),
        fb("Чита'ть по-ру'сски ___.", ["интере'сно", "интере'сный", "интере'сная", "интере'сные"], "интере'сно",
           "An impersonal sentence uses the adverb.", tr="Reading in Russian is interesting."),
        fb("Вчера' ___ интере'сно.", ["бы'ло", "был", "была'", "бы'ли"], "бы'ло",
           "Impersonal sentences use the neuter бы'ло.", tr="Yesterday it was interesting."),
        fb("Здесь ___.", ["краси'во", "краси'вый", "краси'вая", "краси'вое"], "краси'во",
           "The adverb, with no noun to agree with.", tr="It's beautiful here."),
        fb("Учи'ть слова' ___ тру'дно.", ["бы'ло", "был", "была'", "бы'ли"], "бы'ло",
           "The past of an impersonal sentence is always бы'ло.", tr="It was hard to learn words."),
        mc("What follows мо'жно or нельзя'?", ["An infinitive", "A ты-form", "A past-tense form", "An adjective"], "An infinitive",
           "Мо'жно чита'ть, нельзя' кури'ть.", order=True),
        mc("How do you say “Smoking is not allowed here”?",
           ["Здесь нельзя' кури'ть.", "Здесь не мо'жно кури'ть.", "Здесь нет кури'ть.", "Здесь кури'ть не бы'ло."],
           "Здесь нельзя' кури'ть.", "Нельзя' is the word for “not allowed”."),
    ],
)

# ---------------------------------------------------------------------------- 40
L40 = lesson(
    "Nationalities",
    "Америка'нец, америка'нка, америка'нцы",
    requires=["американец", "немец", "француз", "англичанин", "русский"],
    cards=[
        card("A noun for a man, one for a woman",
             "Nationalities are nouns, and there is one form for a man, one for a woman, and a plural. They are "
             "written with a small letter. The masculine plural is used for a group of men or a mixed group. "
             "Watch the spelling: -ец loses its -е- in the plural (не'мец → не'мцы), and -ин drops in англича'не. "
             "The exception is ру'сский, which is an adjective used as a noun and agrees like one.",
             tables=[table(
                 ["Man", "Woman", "Plural"],
                 [["америка'нец", "америка'нка", "америка'нцы"],
                  ["не'мец", "не'мка", "не'мцы"],
                  ["францу'з", "францу'женка", "францу'зы"],
                  ["англича'нин", "англича'нка", "англича'не"],
                  ["испа'нец", "испа'нка", "испа'нцы"],
                  ["ру'сский", "ру'сская", "ру'сские"]])],
             examples=[
                 ex("Он америка'нец, а она' — англича'нка.", "He is American and she is English.", "америка'нец"),
                 ex("Мои' колле'ги — не'мцы.", "My colleagues are German.", "не'мцы"),
                 ex("Я зна'ю америка'нца и францу'женку.", "I know an American and a French woman.", "америка'нца"),
                 ex("Все ру'сские зна'ют э'ту пе'сню.", "All Russians know this song.", "ру'сские"),
             ]),
    ],
    verify=(vf("американец", "американка", "американцы") + vf("немец", "немка", "немцы")
            + vf("француз", "француженка", "французы") + vf("англичанин", "англичанка", "англичане")
            + vf("испанец", "испанка", "испанцы")),
    exercises=[
        fb("Он — ___.", ["америка'нец", "америка'нка", "америка'нцы", "америка'нский"], "америка'нец",
           "A man: америка'нец.", tr="He is American."),
        fb("Она' — ___.", ["не'мка", "не'мец", "не'мцы", "не'мцев"], "не'мка",
           "A woman: не'мка.", tr="She is German."),
        fb("Они' — ___.", ["францу'зы", "францу'з", "францу'женка", "францу'зов"], "францу'зы",
           "A group: францу'зы.", tr="They are French."),
        fb("Ма'ма — ___.", ["францу'женка", "францу'з", "францу'зы", "францу'женец"], "францу'женка",
           "A woman: францу'женка.", tr="My mom is French."),
        fb("Мы зна'ем америка'нца и ___.", ["америка'нку", "америка'нка", "америка'нцы", "америка'нец"], "америка'нку",
           "Direct object, feminine in -а: -у.", tr="We know an American man and an American woman."),
        mc("How do you say “She is German”?",
           ["Она' — не'мка.", "Она' — не'мец.", "Она' — не'мцы.", "Она' — не'мский."], "Она' — не'мка.",
           "A woman: не'мка."),
        mc("Are nationalities capitalised in Russian?",
           ["No, they are lower case", "Yes, always", "Only for women", "Only in the plural"], "No, they are lower case",
           "Unlike English, Russian writes them with a small letter.", order=True),
        mc("Which word is an adjective in form?", ["ру'сский", "америка'нец", "не'мка", "англича'нин"], "ру'сский",
           "It agrees with the noun it replaces: ру'сская, ру'сские."),
        mc("A mixed group of men and women: which plural?",
           ["америка'нцы", "америка'нки", "америка'нец", "америка'нка"], "америка'нцы",
           "The masculine plural also covers mixed groups."),
    ],
)

# ---------------------------------------------------------------------------- 41
L41 = lesson(
    "Review: verbs, cases and sentences",
    "Putting lessons 21 to 40 together",
    requires=["идти", "читать", "писать", "видеть", "говорить"],
    threshold=0.5,
    cards=[
        card("What do I need?",
             "When you build a sentence, ask yourself a few questions and let the answers choose the form. "
             "This is a map of what you have learned since lesson 21.",
             tables=[table(
                 ["Ask yourself", "Use", "Example"],
                 [["Who does what, now?", "verb endings: -ю, -ешь … or -ю, -ишь …", "Я чита'ю. Ты говори'шь."],
                  ["What was done?", "-л, -ла, -ло, -ли", "Она' писа'ла письмо'."],
                  ["Process or result?", "imperfective or perfective", "писа'л / написа'л"],
                  ["What or whom?", "accusative", "кни'гу, студе'нта, меня'"],
                  ["Where at?", "в, на + prepositional", "в шко'ле, на по'чте"],
                  ["Where to?", "в, на + accusative", "в шко'лу, на по'чту"],
                  ["When (day)?", "в + accusative", "в пя'тницу, во вто'рник"],
                  ["Is it allowed?", "мо'жно, нельзя' + infinitive", "Здесь нельзя' кури'ть."]])]),
    ],
    verify=[],
    exercises=[
        fb("Вчера' она' ___ письмо'.", ["писа'ла", "писа'л", "писа'ло", "писа'ли"], "писа'ла",
           "Past tense, feminine.", tr="Yesterday she wrote a letter."),
        fb("Ты ви'дишь Анну? — Да, я ви'жу ___.", ["её", "она'", "ей", "неё"], "её",
           "Direct object: accusative, with no preposition so no н.", tr="Do you see Anna? — Yes, I see her."),
        fb("Я зна'ю ___ студе'нтку.", ["но'вую", "но'вая", "но'вого", "но'вый"], "но'вую",
           "Feminine object: -ую.", tr="I know the new student."),
        fb("Мы идём ___.", ["на по'чту", "на по'чте", "в по'чту", "на по'чта"], "на по'чту",
           "Where to → accusative.", tr="We're going to the post office."),
        fb("___ пя'тницу я до'ма.", ["В", "Во", "На", "У"], "В",
           "Days take в plus the accusative.", tr="On Friday I'm at home."),
        fb("Ты ___ по-ру'сски?", ["говори'шь", "говорю'", "говори'т", "говоря'т"], "говори'шь",
           "Second family: ты takes -ишь.", tr="Do you speak Russian?"),
        fb("___ мне! (to a friend)", ["Пиши'", "Пиши'те", "Пишу'", "Пи'шет"], "Пиши'",
           "A command to ты from the consonant stem пиш-.", tr="Write to me!"),
        fb("Здесь ___ кури'ть: э'то библиоте'ка.", ["нельзя'", "мо'жно", "легко'", "бы'ло"], "нельзя'",
           "Not allowed in a library.", tr="You can't smoke here: this is a library."),
        fb("Наконе'ц я ___ э'ту кни'гу!", ["прочита'л", "чита'л", "чита'ю", "чита'ла"], "прочита'л",
           "Наконе'ц points to a finished result: perfective.", tr="I've finally read this book!"),
        mc("Which sentence is correct?",
           ["Я смотрю' на неё.", "Я смотрю' на её.", "Я смотрю' на она'.", "Я смотрю' на ей."], "Я смотрю' на неё.",
           "After a preposition, её becomes неё."),
        mc("How do you say “She is American”?",
           ["Она' — америка'нка.", "Она' — америка'нец.", "Она' — америка'нцы.", "Она' — америка'нский."],
           "Она' — америка'нка.", "A woman: америка'нка."),
        mc("Which question asks for the destination?", ["Куда'?", "Где?", "Когда'?", "Почему'?"], "Куда'?",
           "Куда'? takes the accusative.", order=True),
    ],
)

UNIT = unit("Unit 6: Past tense, places and everyday sentences", [L34, L35, L36, L37, L38, L39, L40, L41])
