"""Unit 14: where from, near, seasons, setting off, position verbs
(textbook module 3, lesson 19)."""
from dsl import *

# ---------------------------------------------------------------------------- 108
L108 = lesson(
    "Where from? из and с",
    "Я иду' из шко'лы. Она' идёт с рабо'ты.",
    requires=["из", "откуда", "город", "работа", "школа"],
    cards=[
        card("из: the opposite of в",
             "To say where you are coming from, use из or с with the genitive. The question is Отку'да? Use из for "
             "everything you say в about: countries, cities, buildings and enclosed spaces. If you say в for “to” "
             "and “in”, say из for “from”.",
             tables=[table(
                 ["Where to?", "Where?", "Where from?"],
                 [["Мы идём в клуб.", "Мы бы'ли в клу'бе.", "Мы идём из клу'б{а}."],
                  ["Они' е'дут в Москву'.", "Они' бы'ли в Москве'.", "Они' е'дут из Москв{ы'}."],
                  ["Я иду' в шко'лу.", "Я был в шко'ле.", "Я иду' из шко'л{ы}."],
                  ["Я е'ду в командиро'вку.", "Я был в командиро'вке.", "Я е'ду из командиро'вк{и}."]])]),
        card("с: the opposite of на",
             "Use с for everything you say на about: open spaces, events, compass points, and words like по'чта, "
             "вокза'л and заво'д. If you say на for “to” and “on”, say с for “from”.",
             tables=[table(
                 ["Where to?", "Where?", "Where from?"],
                 [["Я иду' на рабо'ту.", "Я был на рабо'те.", "Я иду' с рабо'т{ы}."],
                  ["Она' е'дет на по'чту.", "Она' была' на по'чте.", "Она' е'дет с по'чт{ы}."],
                  ["Мы е'дем на конфере'нцию.", "Мы бы'ли на конфере'нции.", "Мы е'дем с конфере'нци{и}."],
                  ["Он идёт на конце'рт.", "Он был на конце'рте.", "Он идёт с конце'рт{а}."]])],
             examples=[
                 ex("Отку'да ты идёшь? — Я иду' из шко'лы.", "Where are you coming from? — I'm coming from school.", "из шко'лы"),
                 ex("Мы идём с конце'рта.", "We are coming from a concert.", "с конце'рта"),
                 ex("Он е'дет с вокза'ла.", "He is coming from the station.", "с вокза'ла"),
                 ex("Я иду' с уро'ка.", "I am coming from class.", "с уро'ка"),
             ]),
        card("From here, from there",
             "Three questions have their own words for “from”: отку'да (from where), отсю'да (from here) and "
             "отту'да (from there).",
             tables=[table(
                 ["Where to?", "Where?", "Where from?"],
                 [["куда'", "где", "отку'да"],
                  ["сюда'", "здесь", "отсю'да"],
                  ["туда'", "там", "отту'да"]])],
             examples=[
                 ex("Отсю'да до вокза'ла далеко'.", "It is far from here to the station.", "Отсю'да"),
                 ex("Отту'да я пошёл домо'й.", "From there I went home.", "Отту'да"),
             ]),
    ],
    verify=(vf("клуб", "клуба") + vf("школа", "школы") + vf("работа", "работы") + vf("почта", "почты")
            + vf("конференция", "конференции") + vf("концерт", "концерта") + vf("вокзал", "вокзала")
            + vf("урок", "урока") + vf("командировка", "командировки")),
    exercises=[
        fb("Мы идём ___ клу'ба.", ["из", "с", "от", "у"], "из", "В клуб → из клу'ба.", tr="We are coming from the club."),
        fb("Я иду' ___ рабо'ты.", ["с", "из", "от", "у"], "с", "На рабо'ту → с рабо'ты.", tr="I'm coming from work."),
        fb("Она' е'дет ___ Москвы'.", ["из", "с", "от", "у"], "из", "В Москву' → из Москвы'.", tr="She is coming from Moscow."),
        fb("Они' е'дут ___ вокза'ла.", ["с", "из", "от", "у"], "с", "На вокза'л → с вокза'ла.", tr="They are coming from the station."),
        fb("Мы идём с ___. (concert)", ["конце'рта", "конце'рт", "конце'рту", "конце'рте"], "конце'рта",
           "After с: the genitive.", tr="We are coming from the concert.", lemma="концерт"),
        fb("Он идёт из ___. (school)", ["шко'лы", "шко'ла", "шко'лу", "шко'ле"], "шко'лы",
           "After из: the genitive.", tr="He is coming from school.", lemma="школа"),
        fb("Я е'ду с ___. (post office)", ["по'чты", "по'чта", "по'чту", "по'чте"], "по'чты",
           "After с: the genitive.", tr="I'm coming from the post office.", lemma="почта"),
        fb("___ ты идёшь? — Из шко'лы.", ["Отку'да", "Куда'", "Где", "Отсю'да"], "Отку'да",
           "Отку'да = from where?", tr="Where are you coming from? — From school."),
        mc("If you say в for “to”, which preposition do you use for “from”?", ["из", "с", "от", "у"], "из",
           "В ↔ из.", order=True),
        mc("Which phrase goes with на рабо'ту?", ["с рабо'ты", "из рабо'ты", "от рабо'ты", "у рабо'ты"], "с рабо'ты",
           "На ↔ с."),
    ],
)

# ---------------------------------------------------------------------------- 109
L109 = lesson(
    "From a person: от and у",
    "Я была' у врача'. Я иду' от врача'.",
    requires=["у", "от", "врач", "бабушка", "друг"],
    cards=[
        card("At someone's place, from someone's place",
             "With a person, у + the genitive means “at that person's place” (У кого'? At whose place?), and от + "
             "the genitive means “from that person's place” (От кого'? From whom?). It can also mean the person's "
             "office or room: Анто'н сейча'с у врача'.",
             tables=[table(
                 ["At (у кого'?)", "From (от кого'?)"],
                 [["Я была' у врача'.", "Я иду' от врач{а'}."],
                  ["Она' была' у ба'бушки.", "Она' е'дет от ба'бушк{и}."],
                  ["Мы бы'ли у дру'га.", "Мы е'дем от дру'г{а}."],
                  ["Я жил у тёти.", "Я е'ду от тёт{и}."]])]),
        card("Buying and asking: у",
             "The preposition у also works with покупа'ть / купи'ть (to buy from someone) and спра'шивать / "
             "спроси'ть (to ask someone). От also means “from” when something comes from a person, like a letter.",
             examples=[
                 ex("У кого' ты был? — Я был у дру'га.", "At whose place were you? — I was at a friend's.", "У кого'"),
                 ex("Где вы жи'ли ра'ньше? — Я жил у тёти.", "Where did you live before? — I lived at my aunt's.", "у тёти"),
                 ex("Анто'н сейча'с у врача'.", "Anton is at the doctor's right now.", "у врача'"),
                 ex("Я купи'л э'ту маши'ну у дру'га.", "I bought this car from a friend.", "у дру'га"),
                 ex("Спроси' у преподава'теля, что зна'чит э'то сло'во.", "Ask the teacher what this word means.", "у преподава'теля"),
                 ex("Э'то письмо' от бра'та.", "This letter is from my brother.", "от бра'та"),
             ]),
    ],
    verify=(vf("врач", "врача") + vf("бабушка", "бабушки") + vf("друг", "друга") + vf("тётя", "тёти")
            + vf("преподаватель", "преподавателя") + vf("брат", "брата") + vf("значить", "значит")),
    exercises=[
        fb("Я был ___ врача'.", ["у", "от", "из", "с"], "у", "At the doctor's: у.", tr="I was at the doctor's."),
        fb("Я иду' ___ врача'.", ["от", "у", "из", "с"], "от", "From the doctor's: от.", tr="I'm coming from the doctor's."),
        fb("Мы бы'ли у ___. (a friend)", ["дру'га", "друг", "дру'гу", "дру'гом"], "дру'га",
           "After у: the genitive.", tr="We were at a friend's.", lemma="друг"),
        fb("Э'то письмо' ___ бра'та.", ["от", "у", "с", "из"], "от", "From a person: от.", tr="This letter is from my brother."),
        fb("Она' жила' у ___. (aunt)", ["тёти", "тётя", "тётю", "тёте"], "тёти",
           "After у: the genitive.", tr="She lived at her aunt's.", lemma="тётя"),
        fb("Я купи'л э'ту маши'ну ___ дру'га.", ["у", "от", "из", "с"], "у", "Buy from: купи'ть у.", tr="I bought this car from a friend."),
        fb("___ кого' ты идёшь? — От ба'бушки.", ["От", "У", "Из", "С"], "От", "От кого'? = from whom?", tr="Whose place are you coming from? — Grandma's."),
        mc("Which question matches Я был у врача'?",
           ["У кого' ты был?", "Отку'да ты шёл?", "Куда' ты шёл?", "Что ты де'лал?"], "У кого' ты был?", "У кого' = at whose place?"),
        mc("Which preposition means “at someone's place”?", ["у", "от", "из", "с"], "у", "У + genitive.", order=True),
        mc("How do you say “from grandma's”?", ["от ба'бушки", "у ба'бушки", "из ба'бушки", "с ба'бушки"], "от ба'бушки",
           "From a person: от."),
    ],
)

# ---------------------------------------------------------------------------- 110
L110 = lesson(
    "Near: о́коло and у",
    "Они' живу'т о'коло больни'цы. Он стои'т у доски'.",
    requires=["около", "стол", "окно", "больница", "собака"],
    cards=[
        card("о́коло: near, by",
             "О'коло means near or by, and it can be used with anything: a thing, a place or a person. The noun "
             "that follows is in the genitive.",
             tables=[table(
                 ["Russian", "English"],
                 [["Они' живу'т о'коло нас.", "They live near us."],
                  ["Они' живу'т о'коло больни'цы.", "They live near the hospital."],
                  ["Соба'ка лежи'т о'коло стола'.", "The dog is lying by the table."],
                  ["В кла'ссе я сижу' о'коло окна'.", "In class I sit by the window."],
                  ["Не стой о'коло меня'!", "Don't stand near me!"]])]),
        card("у also means near, but only for things",
             "У + the genitive also means near, but only with things. With people, у means “at that person's place”. "
             "So Учени'к стои'т у доски' and Учени'к стои'т о'коло доски' mean the same, but Учени'к стои'т "
             "о'коло учи'теля must use о'коло. If two things are of similar size, use о'коло: Письмо' лежи'т "
             "о'коло газе'ты.",
             examples=[
                 ex("Учени'к стои'т у доски'.", "The pupil is standing at the board.", "у доски'"),
                 ex("Учени'к стои'т о'коло доски'.", "The pupil is standing by the board.", "о'коло доски'"),
                 ex("Учени'к стои'т о'коло учи'теля.", "The pupil is standing next to the teacher.", "о'коло учи'теля"),
                 ex("Маши'на стои'т у до'ма.", "The car is standing by the house.", "у до'ма"),
                 ex("Письмо' лежи'т о'коло газе'ты.", "The letter is lying next to the newspaper.", "о'коло газе'ты"),
             ]),
    ],
    verify=(vf("больница", "больницы") + vf("стол", "стола") + vf("окно", "окна") + vf("я", "меня")
            + vf("доска", "доски") + vf("учитель", "учителя") + vf("дом", "дома") + vf("газета", "газеты")
            + vf("ученик", "ученик") + vf("лежать", "лежит") + vf("стоять", "стоит") + vf("сидеть", "сижу")),
    exercises=[
        fb("Они' живу'т о'коло ___. (the hospital)", ["больни'цы", "больни'ца", "больни'цу", "больни'це"], "больни'цы",
           "After о'коло: the genitive.", tr="They live near the hospital.", lemma="больница"),
        fb("Я сижу' о'коло ___. (the window)", ["окна'", "окно'", "окну'", "окне'"], "окна'",
           "After о'коло: the genitive.", tr="I sit by the window.", lemma="окно"),
        fb("Не стой о'коло ___! (me)", ["меня'", "я", "мне", "мной"], "меня'",
           "Genitive of я: меня'.", tr="Don't stand near me!", lemma="я"),
        fb("Учени'к стои'т о'коло ___. (the teacher)", ["учи'теля", "учи'тель", "учи'телю", "учи'телем"], "учи'теля",
           "After о'коло: the genitive.", tr="The pupil is standing next to the teacher.", lemma="учитель"),
        fb("Маши'на стои'т ___ до'ма.", ["у", "от", "из", "с"], "у", "Near a thing: у is possible.", tr="The car is standing by the house."),
        fb("Учени'к стои'т ___ учи'теля. (next to a person)", ["о'коло", "у", "от", "из"], "о'коло",
           "Near a person: only о'коло.", tr="The pupil is standing next to the teacher."),
        mc("Which preposition can be used with a person for “near”?", ["о'коло", "у", "от", "из"], "о'коло",
           "У + a person means “at that person's place”.", order=True),
        mc("What does Он сидит у врача' mean?",
           ["He is at the doctor's.", "He is sitting near the doctor.", "He is from the doctor.", "He is with the doctor."],
           "He is at the doctor's.", "У + a person = at their place."),
        mc("Which case follows о'коло?", ["genitive", "nominative", "accusative", "prepositional"], "genitive",
           "О'коло + genitive.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 111
L111 = lesson(
    "Spring, summer, autumn, winter",
    "Весно'й, ле'том, о'сенью, зимо'й",
    requires=["весна", "лето", "осень", "зима", "год"],
    cards=[
        card("The four seasons",
             "To say “in spring” and so on, use a special form with no preposition: весно'й, ле'том, о'сенью, "
             "зимо'й. Do not say в весну. The question is Како'е сейча'с вре'мя го'да? (What season is it?).",
             tables=[table(
                 ["Season", "In …"],
                 [["весна'", "весн{о'й}"],
                  ["ле'то", "ле'т{ом}"],
                  ["о'сень", "о'сен{ью}"],
                  ["зима'", "зим{о'й}"]])],
             examples=[
                 ex("Весно'й тепло'.", "It is warm in spring.", "Весно'й"),
                 ex("Ле'том я люблю' пла'вать.", "In summer I like to swim.", "Ле'том"),
                 ex("О'сенью идёт дождь.", "It rains in autumn.", "О'сенью"),
                 ex("Зимо'й идёт снег.", "It snows in winter.", "Зимо'й"),
                 ex("Зимо'й хо'лодно, и я но'шу шу'бу.", "In winter it is cold and I wear a fur coat.", "Зимо'й"),
                 ex("Како'е вре'мя го'да ты лю'бишь?", "Which season do you like?", "вре'мя го'да"),
             ]),
    ],
    verify=(vf("весна", "весной") + vf("лето", "летом") + vf("осень", "осенью") + vf("зима", "зимой")
            + vf("плавать", "плавать") + vf("снег", "снег") + vf("шуба", "шубу") + vf("любить", "любишь")
            + vf("год", "года")),
    exercises=[
        fb("___ жа'рко. (In summer)", ["Ле'том", "Ле'то", "Ле'ту", "Ле'те"], "Ле'том", "In summer: ле'том.", tr="It is hot in summer."),
        fb("___ идёт снег. (In winter)", ["Зимо'й", "Зима'", "Зи'му", "Зимы'"], "Зимо'й", "In winter: зимо'й.", tr="It snows in winter."),
        fb("___ идёт дождь. (In autumn)", ["О'сенью", "О'сень", "О'сени", "О'сеню"], "О'сенью", "In autumn: о'сенью.", tr="It rains in autumn."),
        fb("___ тепло'. (In spring)", ["Весно'й", "Весна'", "Весну'", "Весне'"], "Весно'й", "In spring: весно'й.", tr="It is warm in spring."),
        mc("Which word is “spring”?", ["весна'", "зима'", "ле'то", "о'сень"], "весна'", "Весна' = spring."),
        mc("How do you say “in winter”?", ["зимо'й", "зима'", "зи'му", "зиме'"], "зимо'й", "No preposition: зимо'й."),
        mc("What does о'сень mean?", ["autumn", "spring", "summer", "winter"], "autumn", "О'сень = autumn.", order=True),
        mc("Which season is ле'то?", ["summer", "spring", "autumn", "winter"], "summer", "Ле'то = summer.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 112
L112 = lesson(
    "North, south, east, west",
    "На се'вере, на ю'ге, с восто'ка, на за'пад",
    requires=["север", "юг", "восток", "запад", "карта"],
    cards=[
        card("The compass points take на and с",
             "The four points of the compass are се'вер, юг, восто'к and за'пад. They go with на (where, where "
             "to) and с (where from).",
             tables=[table(
                 ["Direction", "Where?", "Where from?"],
                 [["се'вер", "на се'вер{е}", "с се'вер{а}"],
                  ["юг", "на ю'г{е}", "с ю'г{а}"],
                  ["восто'к", "на восто'к{е}", "с восто'к{а}"],
                  ["за'пад", "на за'пад{е}", "с за'пад{а}"]],
                 note="Where to? is на + the nominative form: Мы е'дем на юг.")]),
        card("Between the points",
             "Join two points with a hyphen to name the directions between them. The first part ends in -о.",
             tables=[table(
                 ["Direction", "Russian"],
                 [["northeast", "се'веро-восто'к"], ["northwest", "се'веро-за'пад"],
                  ["southeast", "ю'го-восто'к"], ["southwest", "ю'го-за'пад"]])],
             examples=[
                 ex("Мы е'дем отдыха'ть на юг.", "We are going on vacation to the south.", "на юг"),
                 ex("Мы отдыха'ем на ю'ге.", "We are on vacation in the south.", "на ю'ге"),
                 ex("Мы е'дем с ю'га.", "We are coming from the south.", "с ю'га"),
                 ex("Мой брат живёт на се'вере.", "My brother lives in the north.", "на се'вере"),
                 ex("Э'тот го'род на восто'ке.", "This city is in the east.", "на восто'ке"),
             ]),
    ],
    verify=(vf("север", "севере", "севера") + vf("юг", "юге", "юга") + vf("восток", "востоке", "востока")
            + vf("запад", "западе", "запада") + vf("отдыхать", "отдыхаем") + vf("жить", "живёт")),
    exercises=[
        fb("Мы живём на ___. (north)", ["се'вере", "се'вер", "се'вера", "се'веру"], "се'вере",
           "На + the prepositional.", tr="We live in the north.", lemma="север"),
        fb("Мы е'дем на ___. (to the south)", ["юг", "ю'ге", "ю'га", "ю'гу"], "юг",
           "Where to: на + accusative (юг).", tr="We are going to the south.", lemma="юг"),
        fb("Он е'дет с ___. (from the east)", ["восто'ка", "восто'к", "восто'ке", "восто'ку"], "восто'ка",
           "С + the genitive.", tr="He is coming from the east.", lemma="восток"),
        fb("Они' живу'т на ___. (west)", ["за'паде", "за'пад", "за'пада", "за'паду"], "за'паде",
           "На + the prepositional.", tr="They live in the west.", lemma="запад"),
        mc("What is се'веро-восто'к?", ["northeast", "northwest", "southeast", "southwest"], "northeast",
           "Се'веро = north, восто'к = east.", order=True),
        mc("What is ю'го-за'пад?", ["southwest", "southeast", "northwest", "northeast"], "southwest",
           "Ю'го = south, за'пад = west.", order=True),
        mc("Which preposition goes with the points of the compass?", ["на", "в", "из", "у"], "на",
           "На се'вере, на ю'ге.", order=True),
        mc("How do you say “from the south”?", ["с ю'га", "из ю'га", "от ю'га", "у ю'га"], "с ю'га", "На ↔ с."),
    ],
)

# ---------------------------------------------------------------------------- 113
L113 = lesson(
    "Setting off: пошёл, пое́хал, полечу́",
    "Он пошёл в магази'н. Я пое'ду в Москву'.",
    requires=["пойти", "поехать", "идти", "ехать", "лететь"],
    cards=[
        card("Past: someone set off",
             "Adding по- to идти', е'хать, лете'ть and плыть makes a perfective verb. In the past it says that "
             "someone set off: Он пошёл в магази'н means “He has gone to the store” (he headed there). We do not "
             "know whether he arrived, and that does not matter. Compare Он ходи'л в магази'н, which means that "
             "he went and came back.",
             tables=[table(
                 ["Verb", "он", "она'", "они'"],
                 [["пойти'", "пошёл", "пошла'", "пошли'"],
                  ["пое'хать", "пое'хал", "пое'хала", "пое'хали"],
                  ["полете'ть", "полете'л", "полете'ла", "полете'ли"],
                  ["поплы'ть", "поплы'л", "поплыла'", "поплы'ли"]])]),
        card("Future: I will go",
             "In the future the focus is on the intention. These are perfective, so the forms look like the "
             "present but mean the future. Note the change of consonant in полечу' (т → ч), just like in "
             "лечу'.",
             tables=[table(
                 ["", "пойти'", "пое'хать", "полете'ть", "поплы'ть"],
                 [["я", "пойду'", "пое'ду", "полечу'", "поплыву'"],
                  ["ты", "пойдёшь", "пое'дешь", "полети'шь", "поплывёшь"],
                  ["он, она'", "пойдёт", "пое'дет", "полети'т", "поплывёт"],
                  ["мы", "пойдём", "пое'дем", "полети'м", "поплывём"],
                  ["вы", "пойдёте", "пое'дете", "полети'те", "поплывёте"],
                  ["они'", "пойду'т", "пое'дут", "полетя'т", "поплыву'т"]])],
             examples=[
                 ex("— Где Рома'н? — Он пошёл в магази'н.", "— Where is Roman? — He has gone to the store.", "пошёл"),
                 ex("Кири'лл пое'хал на по'езде в Ки'ев.", "Kirill left for Kiev by train.", "пое'хал"),
                 ex("Я хочу' пойти' на конце'рт. Е'сли я пойду', я наде'ну но'вое пла'тье.",
                    "I want to go to the concert. If I go, I will put on my new dress.", "пойду'"),
                 ex("У меня' ско'ро бу'дет о'тпуск. Я полечу' на Гава'йи.", "My vacation is soon. I will fly to Hawaii.", "полечу'"),
                 ex("Мы поплывём на теплохо'де в круи'з.", "We will go on a cruise by steamship.", "поплывём"),
             ]),
    ],
    verify=(vf("пойти", "пошёл", "пошла", "пошли", "пойду", "пойдёшь", "пойдёт", "пойдём", "пойдёте", "пойдут")
            + vf("поехать", "поехал", "поехала", "поехали", "поеду", "поедешь", "поедет", "поедем", "поедете", "поедут")
            + vf("полететь", "полетел", "полетела", "полетели", "полечу", "полетишь", "полетит", "полетим", "полетите", "полетят")
            + vf("поплыть", "поплыл", "поплыла", "поплыли", "поплыву", "поплывёшь", "поплывёт", "поплывём", "поплывёте", "поплывут")
            + vf("надеть", "надену") + vf("ходить", "ходил")),
    exercises=[
        fb("Он ___ в магази'н. (set off)", ["пошёл", "пошла'", "пошли'", "пойдёт"], "пошёл",
           "Masculine past of пойти'.", tr="He has gone to the store.", lemma="пойти"),
        fb("Она' ___ в Ки'ев на по'езде. (set off)", ["пое'хала", "пое'хал", "пое'хали", "пое'дет"], "пое'хала",
           "Feminine past of пое'хать.", tr="She left for Kiev by train.", lemma="поехать"),
        fb("За'втра я ___ на конце'рт.", ["пойду'", "пошёл", "ходи'л", "пошла'"], "пойду'",
           "Я takes -у: пойду'.", tr="Tomorrow I will go to the concert.", lemma="пойти"),
        fb("Мы ___ в о'тпуск на Гава'йи. (fly)", ["полети'м", "полечу'", "полетя'т", "полети'шь"], "полети'м",
           "Мы takes -им.", tr="We will fly to Hawaii on vacation.", lemma="полететь"),
        fb("Ты ___ с нами? (go by transport)", ["пое'дешь", "пое'ду", "пое'дет", "пое'дут"], "пое'дешь",
           "Ты takes -ешь.", tr="Will you go with us?", lemma="поехать"),
        fb("Они' ___ в круи'з на теплохо'де. (sail)", ["поплыву'т", "поплывёшь", "поплыву'", "поплывём"], "поплыву'т",
           "Они' takes -ут.", tr="They will go on a cruise by steamship.", lemma="поплыть"),
        mc("What does Он пошёл в магази'н mean?",
           ["He has set off for the store.", "He goes to the store every day.", "He has come back from the store.", "He is in the store."],
           "He has set off for the store.", "The emphasis is on the beginning of the motion."),
        mc("What is the perfective of лете'ть?", ["полете'ть", "лета'ть", "лете'л", "лете'ла"], "полете'ть", "По- + лете'ть."),
        mc("Which prefix makes идти' perfective?", ["по-", "на-", "за-", "про-"], "по-", "Пойти'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 114
L114 = lesson(
    "Walk around, drive around: походи́ть, пое́здить",
    "Он немно'го походи'л по па'рку и пошёл домо'й.",
    requires=["ходить", "ездить", "летать", "плавать", "идти"],
    cards=[
        card("A little while: по- with repeating verbs",
             "With ходи'ть, е'здить, лета'ть and пла'вать, the prefix по- makes a perfective verb that means “for "
             "some time”. It describes movement limited in time and is often followed by another action: Рома'н "
             "походи'л полчаса' по пля'жу и пошёл домо'й (he walked around the beach for half an hour, then "
             "left). Compare пошёл, which means “set off”: the stress and the meaning are both different.",
             tables=[table(
                 ["Repeating verb", "For a while", "Meaning"],
                 [["ходи'ть", "походи'ть", "walk around for a while"],
                  ["е'здить", "пое'здить", "drive around for a while"],
                  ["лета'ть", "полета'ть", "fly around for a while"],
                  ["пла'вать", "попла'вать", "swim for a while"]])],
             examples=[
                 ex("Рома'н походи'л полчаса' по пля'жу и пошёл домо'й.",
                    "Roman walked around the beach for half an hour and went home.", "походи'л"),
                 ex("Кири'лл пое'здил по Ки'еву на маши'не.", "Kirill drove around Kiev by car.", "пое'здил"),
                 ex("За'втра у'тром де'ти попла'вают в о'зере и пото'м пойду'т в шко'лу.",
                    "Tomorrow morning the children will swim in the lake for a while and then go to school.", "попла'вают"),
                 ex("Моя' канаре'йка полета'ет и ся'дет на ла'мпу.",
                    "My canary will fly around for a while and then land on the lamp.", "полета'ет"),
             ]),
    ],
    verify=(vf("походить", "походил") + vf("поездить", "поездил") + vf("полетать", "полетает")
            + vf("поплавать", "поплавают", "поплавал") + vf("пойти", "пойдут", "пошёл")
            + vf("сесть", "сядет") + vf("лампа", "лампу")),
    exercises=[
        fb("Он немно'го ___ по па'рку и пошёл домо'й. (walked around)", ["походи'л", "пошёл", "пойдёт", "идёт"], "походи'л",
           "Walking around for a while: походи'ть.", tr="He walked around the park for a bit and went home."),
        fb("Кири'лл два дня ___ по Ки'еву на маши'не. (drove around)", ["пое'здил", "пое'хал", "пое'дет", "е'дет"], "пое'здил",
           "Driving around for a while: пое'здить.", tr="Kirill drove around Kiev for two days."),
        fb("За'втра они' ___ в о'зере. (will swim for a while)", ["попла'вают", "поплывёт", "плыву'т", "попла'ваю"], "попла'вают",
           "Они' takes -ют: попла'вают.", tr="Tomorrow they will swim in the lake for a while.", lemma="поплавать"),
        fb("Моя' канаре'йка ___ и ся'дет на ла'мпу.", ["полета'ет", "полети'т", "полета'ть", "полете'ла"], "полета'ет",
           "Flying around for a while: полета'ть.", tr="My canary will fly around and land on the lamp."),
        mc("What does по- add to ходи'ть, е'здить, лета'ть, пла'вать?",
           ["for a while", "many times", "a long time", "every day"], "for a while", "Limited in time.", order=True),
        mc("Which word means “swam for a while”?", ["попла'вал", "поплы'л", "плыл", "пла'вал"], "попла'вал",
           "По- + пла'вать."),
        mc("Which word means “drove around for a while”?", ["пое'здил", "пое'хал", "е'здил", "е'хал"], "пое'здил",
           "По- + е'здить."),
        mc("Which word means “walked around for a while”?", ["походи'л", "пошёл", "ходи'л", "шёл"], "походи'л",
           "По- + ходи'ть."),
    ],
)

# ---------------------------------------------------------------------------- 115
L115 = lesson(
    "Sitting, standing, lying, hanging",
    "Ка'рта виси'т на стене'. Маши'на стои'т у до'ма.",
    requires=["сидеть", "стоять", "лежать", "висеть", "стол"],
    cards=[
        card("Four verbs for where things are",
             "Russian often says how something is positioned, where English only says “is”. Use сиде'ть (to sit), "
             "стоя'ть (to stand), лежа'ть (to lie) and висе'ть (to hang). They are in the second family: -и- in "
             "the middle, but the я form changes: сижу', стою', лежу', вишу'.",
             tables=[table(
                 ["", "сиде'ть", "стоя'ть", "лежа'ть", "висе'ть"],
                 [["я", "сижу'", "стою'", "лежу'", "вишу'"],
                  ["ты", "сиди'шь", "стои'шь", "лежи'шь", "виси'шь"],
                  ["он, она'", "сиди'т", "стои'т", "лежи'т", "виси'т"],
                  ["мы", "сиди'м", "стои'м", "лежи'м", "виси'м"],
                  ["вы", "сиди'те", "стои'те", "лежи'те", "виси'те"],
                  ["они'", "сидя'т", "стоя'т", "лежа'т", "вися'т"]])],
             examples=[
                 ex("Кни'га лежи'т на столе'.", "The book is lying on the table.", "лежи'т"),
                 ex("Ка'рта виси'т на стене'.", "The map is hanging on the wall.", "виси'т"),
                 ex("Маши'на стои'т у до'ма.", "The car is parked by the house.", "стои'т"),
                 ex("В кла'ссе я сижу' о'коло окна'.", "In class I sit by the window.", "сижу'"),
                 ex("Э'та фотогра'фия год висе'ла на стене'.", "This picture hung on the wall for a year.", "висе'ла"),
             ]),
        card("For a while",
             "With по- these verbs mean “for some time”: посиде'ть, постоя'ть, полежа'ть, повисе'ть. Combine with "
             "дава'йте: Дава'йте посиди'м здесь!",
             tables=[table(
                 ["Imperfective", "For a while"],
                 [["сиде'ть", "посиде'ть"], ["стоя'ть", "постоя'ть"], ["лежа'ть", "полежа'ть"], ["висе'ть", "повисе'ть"]])],
             examples=[
                 ex("Дава'йте посиди'м здесь.", "Let's sit here for a while.", "посиди'м"),
                 ex("Он немно'го полежа'л и встал.", "He lay for a bit and got up.", "полежа'л"),
             ]),
    ],
    verify=(vf("сидеть", "сижу", "сидишь", "сидит", "сидим", "сидите", "сидят")
            + vf("стоять", "стою", "стоишь", "стоит", "стоим", "стоите", "стоят")
            + vf("лежать", "лежу", "лежишь", "лежит", "лежим", "лежите", "лежат")
            + vf("висеть", "вишу", "висишь", "висит", "висим", "висите", "висят", "висела")
            + vf("посидеть", "посидим") + vf("полежать", "полежал") + vf("постоять", "постоять")
            + vf("повисеть", "повисеть") + vf("встать", "встал") + vf("фотография", "фотография")
            + vf("карта", "карта") + vf("стена", "стене") + vf("стол", "столе")),
    exercises=[
        fb("Я ___ о'коло окна'.", ["сижу'", "сиди'шь", "сиди'т", "сидя'т"], "сижу'",
           "Я takes сижу'.", tr="I'm sitting by the window.", lemma="сидеть"),
        fb("Они' ___ у до'ма. (stand)", ["стоя'т", "стои'т", "стою'", "стои'м"], "стоя'т",
           "Они' takes -ят.", tr="They are standing by the house.", lemma="стоять"),
        fb("Ты до'лго ___ в крова'ти? (lie)", ["лежи'шь", "лежу'", "лежа'т", "лежи'м"], "лежи'шь",
           "Ты takes -ишь.", tr="Do you lie in bed for long?", lemma="лежать"),
        fb("Э'та ка'рта ___ здесь год. (hung)", ["висе'ла", "вися'т", "висе'л", "висе'ли"], "висе'ла",
           "Feminine past.", tr="This map hung here for a year.", lemma="висеть"),
        fb("Ка'рта ___ на стене'.", ["виси'т", "лежи'т", "сиди'т", "стоя'т"], "виси'т",
           "Only a hanging thing: висе'ть.", tr="The map is hanging on the wall."),
        fb("Маши'на ___ о'коло до'ма.", ["стои'т", "виси'т", "сиди'т", "лежи'т"], "стои'т",
           "Cars “stand”: стоя'ть.", tr="The car is standing by the house."),
        mc("What does посиде'ть mean?", ["to sit for a while", "to sit down once", "to sit every day", "to stop sitting"],
           "to sit for a while", "По- = for a while."),
        mc("Which is the я form of висе'ть?", ["вишу'", "ви'жу", "виша'", "висю'"], "вишу'",
           "Висе'ть → вишу', not ви'жу (that is ви'деть)."),
        mc("Which verb describes a book on the table?", ["лежа'ть", "висе'ть", "сиде'ть", "стоя'ть"], "лежа'ть",
           "A book lies flat on a table."),
    ],
)

# ---------------------------------------------------------------------------- 116
L116 = lesson(
    "For a week, for a week, in a week",
    "неде'лю · на неде'лю · че'рез неде'лю",
    requires=["неделя", "месяц", "год", "день", "час"],
    cards=[
        card("Three ways to say a time",
             "A time word can answer three questions. With no preposition (accusative), it says how long something "
             "lasted. With на + the accusative, it says how long you intend to stay or be somewhere. With че'рез + "
             "the accusative, it says after how long something will happen.",
             tables=[table(
                 ["Pattern", "Meaning", "Example"],
                 [["accusative", "how long it lasted", "Я неде'лю жил в Москве'."],
                  ["на + accusative", "for how long (planned)", "Я пое'хал в Москву' на неде'лю."],
                  ["че'рез + accusative", "in how long, after", "Я пое'ду в Москву' че'рез неде'лю."]]),
                 table(
                 ["Time word", "How long?", "Planned for", "After"],
                 [["час", "час", "на час", "че'рез час"],
                  ["день", "день", "на день", "че'рез день"],
                  ["неде'ля", "неде'лю", "на неде'лю", "че'рез неде'лю"],
                  ["ме'сяц", "ме'сяц", "на ме'сяц", "че'рез ме'сяц"],
                  ["год", "год", "на год", "че'рез год"]])],
             examples=[
                 ex("Я писа'л э'то письмо' час.", "I was writing this letter for an hour.", "час"),
                 ex("Мы ме'сяц отдыха'ли в дере'вне.", "We vacationed in the village for a month.", "ме'сяц"),
                 ex("Он пошёл туда' на час, а был там це'лый день.", "He went there for an hour, but was there all day.", "на час"),
                 ex("В Москву' я е'здил на два дня.", "I went to Moscow for two days.", "на два дня"),
                 ex("Он пойдёт туда' че'рез час.", "He will go there in an hour.", "че'рез час"),
                 ex("Мы пое'дем в дере'вню че'рез три дня.", "We will go to the village in three days.", "че'рез три дня"),
             ]),
    ],
    verify=(vf("неделя", "неделю") + vf("месяц", "месяц") + vf("год", "год") + vf("день", "день", "дня")
            + vf("час", "час") + vf("деревня", "деревню", "деревне") + vf("отдыхать", "отдыхали")
            + vf("ездить", "ездил") + vf("пойти", "пойдёт") + vf("поехать", "поедем")),
    exercises=[
        fb("Я пое'ду в Москву' ___ неде'лю. (in a week)", ["че'рез", "на", "за", "в"], "че'рез",
           "Че'рез = after.", tr="I will go to Moscow in a week."),
        fb("Я пое'ду в Москву' ___ неде'лю. (for a week)", ["на", "че'рез", "за", "в"], "на",
           "На = for a planned stay.", tr="I will go to Moscow for a week."),
        fb("Мы отдыха'ли в дере'вне ___. (for a month)", ["ме'сяц", "на ме'сяц", "че'рез ме'сяц", "за ме'сяц"], "ме'сяц",
           "How long it lasted: no preposition.", tr="We vacationed in the village for a month."),
        fb("Он пойдёт туда' ___ час. (in an hour)", ["че'рез", "на", "за", "в"], "че'рез",
           "Че'рез = after.", tr="He will go there in an hour."),
        fb("Мы пое'дем в дере'вню че'рез три ___.", ["дня", "день", "дни", "дней"], "дня",
           "After три: genitive singular.", tr="We will go to the village in three days.", lemma="день"),
        fb("В Москву' я е'здил на два ___.", ["дня", "день", "дни", "дней"], "дня",
           "After два: genitive singular.", tr="I went to Moscow for two days.", lemma="день"),
        mc("Which phrase means “for a planned hour”?", ["на час", "час", "че'рез час", "за час"], "на час",
           "На + accusative = a planned time."),
        mc("Which preposition means “in (after) …”?", ["че'рез", "на", "за", "о"], "че'рез",
           "Че'рез + accusative.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 117
L117 = lesson(
    "One and a half: полтора́ and полторы́",
    "Полтора' часа', полторы' неде'ли",
    requires=["час", "месяц", "стакан", "молоко", "кофе"],
    cards=[
        card("Two forms",
             "Полтора' (“one and a half”) goes with masculine and neuter nouns, and полторы' goes with feminine "
             "ones. The noun after it takes the genitive singular, just like after два.",
             tables=[table(
                 ["Gender", "Numeral", "Examples"],
                 [["masculine", "полтора'", "полтора' ме'сяца · полтора' часа'"],
                  ["neuter", "полтора'", "полтора' окна'"],
                  ["feminine", "полторы'", "полторы' неде'ли · полторы' ча'шки ко'фе"]])],
             examples=[
                 ex("Я жил в Москве' полтора' го'да.", "I lived in Moscow for a year and a half.", "полтора' го'да"),
                 ex("Я рабо'тал полтора' часа'.", "I worked for an hour and a half.", "полтора' часа'"),
                 ex("Купи' полтора' ли'тра молока'.", "Buy a liter and a half of milk.", "полтора' ли'тра"),
                 ex("Она' вы'пила полторы' ча'шки ко'фе.", "She drank a cup and a half of coffee.", "полторы' ча'шки"),
                 ex("Мы там бы'ли полторы' неде'ли.", "We were there for a week and a half.", "полторы' неде'ли"),
             ]),
    ],
    verify=(vf("месяц", "месяца") + vf("неделя", "недели") + vf("час", "часа") + vf("год", "года")
            + vf("литр", "литра") + vf("чашка", "чашки") + vf("молоко", "молока") + vf("кофе", "кофе")
            + vf("окно", "окна") + vf("полтора", "полтора")
            + vf("выпить", "выпила") + vf("пить", "пила")),
    exercises=[
        fb("Я жил там ___ го'да. (1½)", ["полтора'", "полторы'", "два", "пять"], "полтора'",
           "Год is masculine.", tr="I lived there for a year and a half."),
        fb("Мы бы'ли там ___ неде'ли. (1½)", ["полторы'", "полтора'", "два", "оди'н"], "полторы'",
           "Неде'ля is feminine.", tr="We were there for a week and a half."),
        fb("Купи' полтора' ___ молока'.", ["ли'тра", "литр", "ли'тры", "ли'тру"], "ли'тра",
           "After полтора': the genitive singular.", tr="Buy a liter and a half of milk.", lemma="литр"),
        fb("Она' вы'пила полторы' ___ ко'фе.", ["ча'шки", "ча'шка", "ча'шку", "ча'ше"], "ча'шки",
           "After полторы': the genitive singular.", tr="She drank a cup and a half of coffee.", lemma="чашка"),
        fb("Я рабо'тал полтора' ___.", ["часа'", "час", "часы'", "часо'в"], "часа'",
           "After полтора': часа'.", tr="I worked for an hour and a half.", lemma="час"),
        mc("Which numeral goes with feminine nouns?", ["полторы'", "полтора'", "одно'", "один"], "полторы'",
           "Полторы' = feminine.", order=True),
        mc("What case does the noun after полтора' take?",
           ["genitive singular", "nominative", "accusative", "genitive plural"], "genitive singular",
           "Like after два.", order=True),
        mc("How do you say “1½ months”?",
           ["полтора' ме'сяца", "полторы' ме'сяца", "полтора' ме'сяц", "полтора' ме'сяцы"], "полтора' ме'сяца",
           "Ме'сяц is masculine."),
    ],
)

# ---------------------------------------------------------------------------- 118
L118 = lesson(
    "I have to: мне на́до, тебе́ ну́жно",
    "Мне на'до рабо'тать. Вчера' мне на'до бы'ло рабо'тать.",
    requires=["надо", "я", "время", "работать", "ехать"],
    cards=[
        card("The person is in the dative",
             "To say that someone must or needs to do something, put that person in the dative and add на'до or "
             "ну'жно with an infinitive. You know the dative pronouns from мне нра'вится: мне, тебе', ему', ей, "
             "нам, вам, им. The word на'до never changes.",
             tables=[table(
                 ["Who", "Dative", "Example"],
                 [["я", "мне", "Мне на'до рабо'тать."],
                  ["ты", "тебе'", "Тебе' ну'жно отдохну'ть."],
                  ["он, оно'", "ему'", "Ему' на'до пойти' домо'й."],
                  ["она'", "ей", "Ей ну'жно написа'ть письмо'."],
                  ["мы", "нам", "Нам на'до е'хать."],
                  ["вы", "вам", "Вам ну'жно купи'ть бума'гу."],
                  ["они'", "им", "Им на'до учи'ться."]])]),
        card("Past, future and “don't have to”",
             "In the past, add бы'ло: Вчера' мне на'до бы'ло рабо'тать. In the future, add бу'дет: За'втра нам "
             "на'до бу'дет е'хать. To say that you do not have to, put не before на'до: Ей не на'до ждать.",
             examples=[
                 ex("Мне на'до рабо'тать.", "I have to work.", "Мне на'до"),
                 ex("Вчера' мне на'до бы'ло рабо'тать.", "Yesterday I had to work.", "на'до бы'ло"),
                 ex("За'втра нам на'до бу'дет е'хать в Москву'.", "Tomorrow we will have to go to Moscow.", "на'до бу'дет"),
                 ex("Тебе' ну'жно отдохну'ть.", "You need to rest.", "Тебе' ну'жно"),
                 ex("Ей не на'до ждать.", "She doesn't have to wait.", "не на'до"),
             ]),
    ],
    verify=(vf("отдохнуть", "отдохнуть") + vf("написать", "написать") + vf("купить", "купить")
            + vf("учиться", "учиться") + vf("пойти", "пойти") + vf("ехать", "ехать")
            + vf("работать", "работать") + vf("бумага", "бумагу")),
    exercises=[
        fb("___ на'до рабо'тать. (I)", ["Мне", "Я", "Меня'", "Мной"], "Мне", "The person goes in the dative.", tr="I have to work."),
        fb("___ ну'жно отдохну'ть. (you, informal)", ["Тебе'", "Ты", "Тебя'", "Тобой"], "Тебе'",
           "The dative of ты: тебе'.", tr="You need to rest."),
        fb("___ на'до пойти' домо'й. (him)", ["Ему'", "Он", "Его'", "Им"], "Ему'",
           "The dative of он: ему'.", tr="He has to go home."),
        fb("___ ну'жно написа'ть письмо'. (her)", ["Ей", "Она'", "Её", "Ней"], "Ей",
           "The dative of она': ей.", tr="She needs to write a letter."),
        fb("___ на'до учи'ться. (them)", ["Им", "Они'", "Их", "Ими"], "Им",
           "The dative of они': им.", tr="They have to study."),
        fb("Вчера' мне на'до ___ рабо'тать.", ["бы'ло", "бу'дет", "был", "есть"], "бы'ло",
           "The past: add бы'ло.", tr="Yesterday I had to work."),
        fb("За'втра нам на'до ___ е'хать в Москву'.", ["бу'дет", "бы'ло", "бу'дут", "был"], "бу'дет",
           "The future: add бу'дет.", tr="Tomorrow we will have to go to Moscow."),
        mc("In which case is the person after на'до?", ["dative", "nominative", "genitive", "accusative"], "dative",
           "Мне на'до.", order=True),
        mc("Which means “She doesn't have to wait”?",
           ["Ей не на'до ждать.", "Она' не на'до ждать.", "Её не на'до ждать.", "Ей нет ждать."],
           "Ей не на'до ждать.", "Не на'до + infinitive."),
    ],
)

# ---------------------------------------------------------------------------- 119
L119 = lesson(
    "You're right! In my opinion …",
    "Ты прав. По-мо'ему, э'то ва'жно.",
    requires=["важный", "прекрасный", "приятный", "ладно", "сначала"],
    cards=[
        card("To be right: прав",
             "To say that someone is right, use the short adjective прав, права' or пра'вы. It has no other forms. "
             "Use прав for a man, права' for a woman and пра'вы for several people. In the past add был, была' or "
             "бы'ли.",
             tables=[table(
                 ["Who", "Form"],
                 [["я, ты, он (man)", "прав"],
                  ["я, ты, она'", "права'"],
                  ["мы, вы, они'", "пра'вы"]])],
             examples=[
                 ex("Ты прав.", "You are right.", "прав"),
                 ex("Ма'ша права'.", "Masha is right.", "права'"),
                 ex("Вы пра'вы!", "You are right!", "пра'вы"),
                 ex("Я был прав.", "I was right.", "был прав"),
             ]),
        card("Opinions and reactions",
             "Some short words help you take part in a conversation: По-мо'ему (in my opinion), Ла'дно (all right), "
             "Снача'ла (at first), and the adjectives ва'жный (important), прекра'сный (wonderful) and прия'тный "
             "(pleasant). Тяжело' means “it is hard”.",
             tables=[table(
                 ["Phrase", "Meaning"],
                 [["По-мо'ему, …", "In my opinion, …"],
                  ["Ла'дно.", "All right. Okay."],
                  ["Снача'ла …, пото'м …", "First …, then …"],
                  ["Э'то ва'жно.", "This is important."],
                  ["Э'то прекра'сно!", "That's wonderful!"],
                  ["Э'то тяжело'.", "That's hard."]])],
             examples=[
                 ex("По-мо'ему, э'то о'чень ва'жно.", "I think this is very important.", "По-мо'ему"),
                 ex("— Дава'й посмо'трим фильм. — Ла'дно.", "— Let's watch a film. — Okay.", "Ла'дно"),
                 ex("Снача'ла он шёл ме'дленно, а пото'м вдруг пошёл о'чень бы'стро.",
                    "At first he walked slowly, but then suddenly he started walking very fast.", "Снача'ла"),
                 ex("Э'то прекра'сный день!", "It is a wonderful day!", "прекра'сный"),
                 ex("Тяжело' учи'ться и рабо'тать.", "It is hard to study and work.", "Тяжело'"),
             ]),
    ],
    verify=(vf("важный", "важно", "важный") + vf("прекрасный", "прекрасно", "прекрасный")
            + vf("тяжело", "тяжело") + vf("медленно", "медленно") + vf("быстро", "быстро")),
    exercises=[
        fb("Ты ___. (right)", ["прав", "права'", "пра'вы", "пра'во"], "прав", "A man: прав.", tr="You are right."),
        fb("Ма'ша ___. (right)", ["права'", "прав", "пра'вы", "пра'во"], "права'", "A woman: права'.", tr="Masha is right."),
        fb("Вы ___! (right)", ["пра'вы", "прав", "права'", "пра'во"], "пра'вы", "Plural: пра'вы.", tr="You are right!"),
        fb("___, э'то о'чень ва'жно. (In my opinion)", ["По-мо'ему", "По-тво'ему", "По-на'шему", "По-ва'шему"], "По-мо'ему",
           "По-мо'ему = in my opinion.", tr="In my opinion, this is very important."),
        fb("— Дава'й посмо'трим фильм. — ___.", ["Ла'дно", "Спаси'бо", "До свида'ния", "Здра'вствуйте"], "Ла'дно",
           "Ла'дно = okay.", tr="— Let's watch a film. — Okay."),
        fb("___ он шёл ме'дленно, а пото'м бы'стро. (At first)", ["Снача'ла", "Сра'зу", "Вдруг", "Всегда'"], "Снача'ла",
           "Снача'ла = at first.", tr="At first he walked slowly, and then fast."),
        mc("What does Э'то тяжело' mean?", ["It is hard.", "It is easy.", "It is cheap.", "It is pleasant."], "It is hard.",
           "Тяжело' = hard."),
        mc("Which form is used for “she is right”?", ["права'", "прав", "пра'вы", "пра'во"], "права'", "A woman: права'."),
        mc("Which word means “wonderful”?", ["прекра'сный", "прия'тный", "ва'жный", "тяжёлый"], "прекра'сный",
           "Прекра'сный."),
    ],
)

# ---------------------------------------------------------------------------- 120
L120 = lesson(
    "Review: from, near, seasons and going",
    "Putting lessons 108 to 119 together",
    requires=["из", "около", "весна", "сидеть", "надо"],
    cards=[
        card("What you can do now",
             "You can say where you are coming from (из, с, от), where someone is (у), what is near (о'коло), "
             "name the seasons and compass points, say that someone set off (пошёл, пое'хал, полечу'), say "
             "that things sit, stand, lie or hang, give a time as how long, for how long or in how long, say "
             "полтора', say that someone must (мне на'до), and say that someone is right (прав).",
             tables=[table(
                 ["Topic", "Remember"],
                 [["From a building or city", "из шко'лы · из Москвы'"],
                  ["From an open place or event", "с рабо'ты · с конце'рта"],
                  ["At or from a person", "у врача' · от врача'"],
                  ["Near", "о'коло окна' · у до'ма"],
                  ["Seasons", "весно'й · ле'том · о'сенью · зимо'й"],
                  ["Set off", "пошёл · пое'хал · полечу'"],
                  ["Position", "сиди'т · стои'т · лежи'т · виси'т"],
                  ["Time", "неде'лю · на неде'лю · че'рез неде'лю"],
                  ["Have to", "Мне на'до + infinitive"]])]),
    ],
    verify=[],
    exercises=[
        fb("Мы идём ___ клу'ба.", ["из", "с", "от", "у"], "из", "В клуб → из клу'ба.", tr="We are coming from the club."),
        fb("Я иду' ___ конце'рта.", ["с", "из", "от", "у"], "с", "На конце'рт → с конце'рта.", tr="I'm coming from the concert."),
        fb("Она' идёт ___ врача'.", ["от", "у", "из", "с"], "от", "From a person: от.", tr="She is coming from the doctor's."),
        fb("Я была' ___ врача'.", ["у", "от", "из", "с"], "у", "At a person's: у.", tr="I was at the doctor's."),
        fb("___ идёт снег. (winter)", ["Зимо'й", "Зима'", "Зи'му", "Зимы'"], "Зимо'й", "In winter: зимо'й.", tr="It snows in winter."),
        fb("Он ___ в магази'н и ещё не вернулся.", ["пошёл", "ходи'л", "идёт", "ходи'ть"], "пошёл",
           "Set off and not yet back: пошёл.", tr="He went to the store and hasn't come back yet."),
        fb("Ка'рта ___ на стене'.", ["виси'т", "лежи'т", "сиди'т", "стоя'т"], "виси'т",
           "A hanging thing: висе'ть.", tr="The map is hanging on the wall."),
        fb("Я пое'ду в Москву' ___ три дня. (for three days)", ["на", "че'рез", "за", "в"], "на",
           "На = a planned stay.", tr="I will go to Moscow for three days."),
        fb("Мне на'до ___ домо'й.", ["пойти'", "пошёл", "пойду'", "иду'"], "пойти'",
           "After на'до: the infinitive.", tr="I have to go home."),
        fb("Ты ___. (right)", ["прав", "права'", "пра'вы", "пра'во"], "прав", "A man: прав.", tr="You are right."),
        mc("Which means “near the window”?", ["о'коло окна'", "у окно'", "о'коло окну'", "от окна'"], "о'коло окна'",
           "О'коло + genitive."),
        mc("How do you say “1½ hours”?",
           ["полтора' часа'", "полторы' часа'", "полтора' час", "полтора' часы'"], "полтора' часа'",
           "Час is masculine: полтора'."),
    ],
)

UNIT = unit("Unit 14: From, near, seasons and going",
            [L108, L109, L110, L111, L112, L113, L114, L115, L116, L117, L118, L119, L120])
