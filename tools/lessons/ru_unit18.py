"""Unit 18: instrumental continued, reciprocal verbs, last names and prefixed motion verbs
(textbook module 4, lesson 24)."""
from dsl import *

# ---------------------------------------------------------------------------- 155
L155 = lesson(
    "Mom and I: мы с мамой",
    "Мы с ма'мой живём в Москве'. Оле'г с О'лей рабо'тают вме'сте.",
    requires=["мы", "вы", "они", "мама", "друг"],
    cards=[
        card("С + instrumental can mean “and”",
             "Russians often say “I and my mother” as “we with my mother”. The pronoun мы, вы or они' comes first, "
             "then с + instrumental, and the verb is plural. Use мы for “someone and I”, вы for “someone and you” "
             "and они' for “someone and he or she”.",
             tables=[table(
                 ["English", "Russian"],
                 [["you and I", "мы с тобо'й"],
                  ["Oleg and I", "мы с Оле'гом"],
                  ["Mom and I", "мы с ма'мой"],
                  ["Oleg and you", "вы с Оле'гом"],
                  ["Mom and you", "вы с ма'мой"],
                  ["Oleg and he or she", "они' с Оле'гом"],
                  ["Mom and he or she", "они' с ма'мой"]])],
             examples=[
                 ex("Мы с ма'мой о'чень тебя' лю'бим.", "Mom and I love you very much.", "Мы с ма'мой"),
                 ex("Оле'г с О'лей рабо'тают на одно'м заво'де.", "Oleg and Olya work at the same factory.", "Оле'г с О'лей"),
                 ex("Мы с тобо'й так похо'жи.", "You and I are so alike.", "Мы с тобо'й"),
                 ex("Куда' вы с ней ходи'ли?", "Where did you and she go?", "вы с ней"),
             ]),
    ],
    verify=(vf("мама", "мамой") + vf("работать", "работают") + vf("жить", "живём", "живёте") + vf("любить", "любим")
            + vf("похожий", "похожи") + vf("ходить", "ходили") + vf("завод", "заводе") + vf("друг", "другом")),
    exercises=[
        fb("___ с тобо'й так похо'жи. (You and I)", ["Мы", "Я", "Вы", "Они'"], "Мы", "“You and I” is мы с тобо'й.", tr="You and I are so alike."),
        fb("Мы с ___ идём в парк. (Oleg)", ["Оле'гом", "Оле'г", "Оле'га", "Оле'гу"], "Оле'гом", "С + instrumental.", tr="Oleg and I are going to the park."),
        fb("___ с ма'мой живём в Москве'. (Mom and I)", ["Мы", "Я", "Вы", "Они'"], "Мы", "The verb is first person plural: живём.", tr="Mom and I live in Moscow."),
        fb("___ с Оле'гом живёте в Москве'. (Oleg and you)", ["Вы", "Мы", "Они'", "Я"], "Вы", "The verb is живёте: вы.", tr="Oleg and you live in Moscow."),
        fb("___ с ма'мой рабо'тают на заво'де. (She and mom)", ["Они'", "Мы", "Вы", "Я"], "Они'", "The verb is рабо'тают: они'.", tr="She and mom work at a factory."),
        fb("Оле'г с О'лей ___ на одно'м заво'де. (work)", ["рабо'тают", "рабо'тает", "рабо'таем", "рабо'таешь"], "рабо'тают", "Two people: plural verb.", tr="Oleg and Olya work at the same factory.", lemma="работать"),
        mc("What does мы с Оле'гом mean?", ["Oleg and I", "Oleg and you", "Oleg and he or she", "I with Oleg's friend"], "Oleg and I", "Мы + с = “and I”."),
        mc("Which means “Oleg and you”?", ["вы с Оле'гом", "мы с Оле'гом", "они' с Оле'гом", "ты с Оле'гом"], "вы с Оле'гом", "Вы с + instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 156
L156 = lesson(
    "Above, in front of, between: над, пе́ред, ме́жду, ря́дом с",
    "Ла'мпа виси'т над столо'м. Шкаф стои'т ме'жду столо'м и окно'м.",
    requires=["стол", "окно", "картина", "стена", "стул"],
    cards=[
        card("Four prepositions of place",
             "Над (above), пе'ред (in front of, before), ме'жду (between) and ря'дом с (next to) always take the "
             "instrumental. They answer the question Где?",
             tables=[table(
                 ["Preposition", "Meaning", "Example"],
                 [["над", "above", "Ла'мпа виси'т над столо'м."],
                  ["пе'ред", "in front of", "Я стою' пе'ред ка'ртой."],
                  ["ме'жду", "between", "Шкаф стои'т ме'жду столо'м и окно'м."],
                  ["ря'дом с", "next to", "Ка'рта виси'т ря'дом с окно'м."]])],
             examples=[
                 ex("Где виси'т ла'мпа? — Ла'мпа виси'т над столо'м.", "Where does the lamp hang? — Over the table.", "над столо'м"),
                 ex("Где ты стои'шь? — Я стою' пе'ред карти'ной.", "Where are you standing? — In front of the picture.", "пе'ред карти'ной"),
                 ex("Стул стои'т ме'жду столо'м и стено'й.", "The chair is between the table and the wall.", "ме'жду столо'м и стено'й"),
                 ex("Ла'мпа стои'т ря'дом со сту'лом.", "The lamp is next to the chair.", "ря'дом со сту'лом"),
             ]),
        card("With мной",
             "Над and пе'ред add an -о before мной and are said together with it: надо мной, передо мной. "
             "Compare Вы бы'ли передо мной (You were in front of me) and Переста'ньте смея'ться надо мной! (Stop "
             "laughing at me!).",
             examples=[
                 ex("Вы бы'ли передо мной.", "You were in front of me.", "передо мной"),
                 ex("Переста'ньте смея'ться надо мной!", "Stop laughing at me!", "надо мной"),
             ]),
    ],
    verify=(vf("стол", "столом") + vf("окно", "окном") + vf("картина", "картиной") + vf("стена", "стеной")
            + vf("стул", "стулом") + vf("висеть", "висит") + vf("стоять", "стою", "стоишь", "стоит")
            + vf("лампа", "лампа") + vf("шкаф", "шкаф") + vf("перестать", "перестаньте") + vf("смеяться", "смеяться")),
    exercises=[
        fb("Ла'мпа виси'т ___ столо'м. (above)", ["над", "под", "в", "на"], "над", "Над + instrumental.", tr="The lamp hangs above the table."),
        fb("Я стою' ___ карти'ной. (in front of)", ["пе'ред", "над", "у", "из"], "пе'ред", "Пе'ред + instrumental.", tr="I am standing in front of the picture."),
        fb("Шкаф стои'т ме'жду столо'м и ___. (the window)", ["окно'м", "окно'", "окна'", "окну'"], "окно'м", "Ме'жду + instrumental.", tr="The cupboard is between the table and the window.", lemma="окно"),
        fb("Ла'мпа стои'т ря'дом со ___. (the chair)", ["сту'лом", "стул", "сту'ла", "сту'лу"], "сту'лом", "Ря'дом с + instrumental.", tr="The lamp is next to the chair.", lemma="стул"),
        fb("Он стои'т пе'ред ___. (the picture)", ["карти'ной", "карти'на", "карти'ну", "карти'не"], "карти'ной", "Пе'ред + instrumental.", tr="He is standing in front of the picture.", lemma="картина"),
        fb("Переста'ньте смея'ться ___ мной! (at)", ["надо", "над", "на", "за"], "надо", "Before мной: надо.", tr="Stop laughing at me!"),
        mc("Which case follows пе'ред, над, ме'жду and ря'дом с?", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "Always the instrumental.", order=True),
        mc("Which means “above me”?", ["надо мной", "над мной", "над меня'", "надо меня'"], "надо мной", "Надо + мной."),
    ],
)

# ---------------------------------------------------------------------------- 157
L157 = lesson(
    "Behind and under: Где? or Куда́?",
    "Рюкза'к лежи'т под столо'м. Положи' рюкза'к под стол.",
    requires=["шкаф", "кот", "кровать", "стол", "сумка"],
    cards=[
        card("Same preposition, different case",
             "Unlike the other prepositions, за (behind, at) and под (under) take two cases. For where something is, use "
             "the instrumental. When something moves there (Куда'?), use the accusative.",
             tables=[table(
                 ["Где? (instrumental)", "Куда'? (accusative)"],
                 [["Рюкза'к лежи'т под столо'м.", "Положи' рюкза'к под стол."],
                  ["Карти'на стои'т за шка'фом.", "Поста'вь карти'ну за шкаф."],
                  ["Мы сиди'м за столо'м.", "Сади'тесь за стол."],
                  ["Кот спит под крова'тью.", "Кот убежа'л под крова'ть."]])],
             examples=[
                 ex("Положи' су'мку под стол.", "Put the bag under the table.", "под стол"),
                 ex("Су'мка лежи'т под столо'м.", "The bag is under the table.", "под столо'м"),
                 ex("Мы сиди'м за столо'м и у'жинаем.", "We sit at the table and have dinner.", "за столо'м"),
             ]),
    ],
    verify=(vf("стол", "стол", "столом") + vf("шкаф", "шкафом") + vf("кровать", "кровать", "кроватью") + vf("кот", "кот")
            + vf("сумка", "сумку") + vf("положить", "положи") + vf("поставить", "поставь") + vf("садиться", "садитесь")
            + vf("убежать", "убежал") + vf("ужинать", "ужинаем") + vf("сидеть", "сидим") + vf("спать", "спит")),
    exercises=[
        fb("Рюкза'к лежи'т ___ столо'м. (under)", ["под", "за", "над", "на"], "под", "Under: под.", tr="The backpack is under the table."),
        fb("Рюкза'к лежи'т под ___.", ["столо'м", "стол", "стола'", "столу'"], "столо'м", "Where? → instrumental.", tr="The backpack is under the table.", lemma="стол"),
        fb("Положи' рюкза'к под ___.", ["стол", "столо'м", "стола'", "столу'"], "стол", "Куда'? → accusative.", tr="Put the backpack under the table.", lemma="стол"),
        fb("Мы сиди'м за ___. (the table)", ["столо'м", "стол", "стола'", "столу'"], "столо'м", "Where? → instrumental.", tr="We are sitting at the table.", lemma="стол"),
        fb("Сади'тесь за ___. (the table)", ["стол", "столо'м", "стола'", "столу'"], "стол", "Куда'? → accusative.", tr="Sit down at the table.", lemma="стол"),
        fb("Карти'на стои'т за ___. (the cupboard)", ["шка'фом", "шкаф", "шка'фа", "шка'фу"], "шка'фом", "Where? → instrumental.", tr="The picture is standing behind the cupboard.", lemma="шкаф"),
        fb("Кот спит под ___. (the bed)", ["крова'тью", "крова'ть", "крова'ти"], "крова'тью", "Where? → instrumental.", tr="The cat sleeps under the bed.", lemma="кровать"),
        fb("Кот убежа'л под ___. (the bed)", ["крова'ть", "крова'тью", "крова'ти"], "крова'ть", "Куда'? → accusative.", tr="The cat ran under the bed.", lemma="кровать"),
        mc("Which means “Put the bag under the table”?",
           ["Положи' су'мку под стол.", "Положи' су'мку под столо'м.", "Положи' су'мку над столо'м.", "Положи' су'мку за столо'м."],
           "Положи' су'мку под стол.", "Motion: accusative."),
    ],
)

# ---------------------------------------------------------------------------- 158
L158 = lesson(
    "Put, stand and hang: класть, ставить, вешать",
    "Я кладу' кни'гу на стол. Кни'га лежи'т на столе'.",
    requires=["поставить", "положить", "повесить", "лежать", "стоять"],
    cards=[
        card("Where? and Куда́?",
             "Russian uses different verbs for being somewhere and for putting something there. Лежа'ть, стоя'ть and "
             "висе'ть say where it is. Класть / положи'ть (lay flat), ста'вить / поста'вить (stand upright) and "
             "ве'шать / пове'сить (hang) move it there. They take an accusative object, and the place is Куда'? (accusative) "
             "after на, в, за, под.",
             tables=[table(
                 ["Position (Где?)", "Placing (Куда'?)", "Perfective"],
                 [["лежа'ть", "класть", "положи'ть"],
                  ["стоя'ть", "ста'вить", "поста'вить"],
                  ["висе'ть", "ве'шать", "пове'сить"]])],
             examples=[
                 ex("Я кладу' кни'гу на стол. Кни'га лежи'т на столе'.", "I put the book on the table. The book lies on the table.", "кладу'"),
                 ex("Он ста'вит ла'мпу на стол. Ла'мпа стои'т на столе'.", "He puts the lamp on the table. The lamp stands on the table.", "ста'вит"),
                 ex("Мы ве'шаем карти'ну на сте'ну. Карти'на виси'т на стене'.", "We hang the picture on the wall. The picture hangs on the wall.", "ве'шаем"),
             ]),
        card("Forms to remember",
             "Класть: кладу', кладёшь, кладёт. Ста'вить: ста'влю, ста'вишь. Ве'шать: ве'шаю, ве'шаешь. The "
             "perfective forms are положу', поста'влю and пове'шу. Stand, lie and hang up in the past use the "
             "regular imperfective: стоя'л, лежа'л, висе'л.",
             examples=[
                 ex("Куда' ты положи'л мою' кни'гу?", "Where did you put my book?", "положи'л"),
                 ex("Поста'вь су'мку на стул.", "Put the bag on the chair.", "Поста'вь"),
                 ex("За'втра мы пове'сим карти'ну.", "Tomorrow we will hang the picture.", "пове'сим"),
             ]),
    ],
    verify=(vf("лежать", "лежит", "лежал") + vf("стоять", "стоит", "стоял") + vf("висеть", "висит", "висел")
            + vf("положить", "положил", "положу") + vf("поставить", "поставлю", "поставь") + vf("повесить", "повешу", "повесим")
            + vf("класть", "кладу", "кладёшь", "кладёт") + vf("ставить", "ставит", "ставлю") + vf("вешать", "вешаю", "вешаем")
            + vf("картина", "картину") + vf("стена", "стену", "стене") + vf("стол", "столе") + vf("лампа", "лампу")
            + vf("сумка", "сумку") + vf("стул", "стул")),
    exercises=[
        fb("Кни'га ___ на столе'.", ["лежи'т", "кладёт", "ве'шает", "ста'вят"], "лежи'т", "Position: лежа'ть.", tr="The book is lying on the table.", lemma="лежать"),
        fb("Я ___ ла'мпу на стол. (put, stand)", ["ста'влю", "стою'", "лежу'", "ве'шу"], "ста'влю", "Placing upright: ста'вить.", tr="I am putting the lamp on the table.", lemma="ставить"),
        fb("Мы ___ карти'ну на сте'ну. (hang up)", ["ве'шаем", "виси'м", "лежи'м", "стои'м"], "ве'шаем", "Placing: ве'шать.", tr="We are hanging the picture on the wall.", lemma="вешать"),
        fb("Карти'на ___ на стене'.", ["виси'т", "ве'шает", "кладёт", "ста'вит"], "виси'т", "Position: висе'ть.", tr="The picture is hanging on the wall.", lemma="висеть"),
        fb("Куда' ты ___ мою' кни'гу? (put, past)", ["положи'л", "лежа'л", "стоя'л", "висе'л"], "положи'л", "Placing, perfective: положи'л.", tr="Where did you put my book?", lemma="положить"),
        fb("Он ___ су'мку на стул. (puts)", ["кладёт", "лежи'т", "виси'т", "стои'т"], "кладёт", "Placing flat: класть.", tr="He puts the bag on the chair."),
        mc("Which verb means “to stand something upright”?", ["ста'вить", "стоя'ть", "лежа'ть", "висе'ть"], "ста'вить", "Placing: ста'вить."),
        mc("Which case does the object of класть, ставить, вешать take?", ["accusative", "instrumental", "genitive", "dative"], "accusative", "Accusative.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 159
L159 = lesson(
    "Meeting and hugging: reciprocal -ся verbs",
    "Мы встреча'емся в кафе'. Они' познако'мились в Москве'.",
    requires=["встречаться", "познакомиться", "видеть", "кафе", "каждый"],
    cards=[
        card("-ся can mean “each other”",
             "Some reflexive verbs describe an action two or more people do to each other. English adds “each other” "
             "or “together”.",
             tables=[table(
                 ["Verb", "Meaning"],
                 [["встреча'ться", "to meet; to date"],
                  ["знако'миться / познако'миться", "to get to know each other"],
                  ["ви'деться / уви'деться", "to see each other"],
                  ["целова'ться", "to kiss"],
                  ["обнима'ться", "to hug"],
                  ["перепи'сываться", "to write each other"]])],
             examples=[
                 ex("Они' познако'мились в Москве'.", "They met in Moscow.", "познако'мились"),
                 ex("Подру'ги обнима'ются.", "The girlfriends hug.", "обнима'ются"),
                 ex("Мы перепи'сываемся по интерне'ту.", "We write to each other online.", "перепи'сываемся"),
                 ex("Я не зна'ю, когда' мы уви'димся.", "I don't know when we will see each other.", "уви'димся"),
             ]),
        card("Naming the partner with с",
             "To stress who the second person is, keep the same verb and add с + instrumental. With a singular "
             "subject the verb is singular: Он познако'мился с Ви'кой.",
             examples=[
                 ex("Он познако'мился с Ви'кой в Москве'.", "He met Vika in Moscow.", "с Ви'кой"),
                 ex("Я встреча'юсь с Са'шей ка'ждый день.", "I meet Sasha every day.", "с Са'шей"),
                 ex("Ко'ля встреча'ется со Све'той.", "Kolya is dating Sveta.", "со Све'той"),
                 ex("Я не зна'ю, когда' я уви'жусь с тобо'й.", "I don't know when I will see you.", "с тобо'й"),
             ]),
    ],
    verify=(vf("встречаться", "встречаемся", "встречаюсь", "встречается") + vf("познакомиться", "познакомились", "познакомился")
            + vf("обниматься", "обнимаются") + vf("переписываться", "переписываемся") + vf("увидеться", "увидимся", "увижусь")
            + vf("подруга", "подруги") + vf("интернет", "интернету") + vf("знать", "знаю")),
    exercises=[
        fb("Мы с Са'шей ка'ждый день ___ в кафе'. (meet)", ["встреча'емся", "встреча'юсь", "встреча'ется", "встреча'ются"], "встреча'емся", "Мы → -емся.", tr="Sasha and I meet in a café every day.", lemma="встречаться"),
        fb("Они' ___ в Москве'. (met for the first time)", ["познако'мились", "познако'мился", "познако'милась", "познако'милось"], "познако'мились", "Plural past: -лись.", tr="They met in Moscow.", lemma="познакомиться"),
        fb("Подру'ги ___. (hug)", ["обнима'ются", "обнима'ется", "обнима'ешься", "обнима'емся"], "обнима'ются", "Plural: -ются.", tr="The girlfriends hug."),
        fb("Мы ___ по интерне'ту. (write to each other)", ["перепи'сываемся", "перепи'сываюсь", "перепи'сываетесь", "перепи'сываются"], "перепи'сываемся", "Мы → -емся.", tr="We write to each other online."),
        fb("Я встреча'юсь с ___. (Sasha)", ["Са'шей", "Са'ша", "Са'шу", "Са'ше"], "Са'шей", "С + instrumental.", tr="I am seeing Sasha."),
        fb("Ко'ля встреча'ется ___ Све'той. (with)", ["со", "с", "к", "у"], "со", "С becomes со before св-.", tr="Kolya is dating Sveta."),
        fb("Я не зна'ю, когда' мы ___. (will see each other)", ["уви'димся", "уви'жусь", "уви'дится", "уви'дитесь"], "уви'димся", "Мы → -имся.", tr="I don't know when we will see each other."),
        mc("Why are verbs like встреча'ться reflexive?", ["Both people take part in the action", "The action is done to oneself", "Because it is in the past", "Because it takes the dative"], "Both people take part in the action", "Reciprocal meaning."),
        mc("Which means “They met each other in Moscow”?",
           ["Они' познако'мились в Москве'.", "Они' познако'мили в Москве'.", "Они' познако'мится в Москве'.", "Он познако'мился в Москве'."],
           "Они' познако'мились в Москве'.", "Plural past reflexive."),
    ],
)

# ---------------------------------------------------------------------------- 160
L160 = lesson(
    "Friends and arguments: дружить, спорить, друг друга",
    "Они' дру'жат пять лет. Они' помога'ют друг дру'гу.",
    requires=["любить", "помогать", "писать", "знать", "говорить"],
    cards=[
        card("Other verbs with с",
             "Not every reciprocal verb ends in -ся. Дружи'ть с, разгова'ривать с and спо'рить с (о + prepositional "
             "for the topic) all take с + instrumental.",
             examples=[
                 ex("Они' дру'жат уже' пять лет.", "They have been friends for five years.", "дру'жат"),
                 ex("Бори'с дру'жит с Ле'ной.", "Boris is friends with Lena.", "с Ле'ной"),
                 ex("Мы уже' два дня не разгова'риваем.", "We haven't talked for two days.", "не разгова'риваем"),
                 ex("Мы с му'жем никогда' не спо'рим о поли'тике.", "My husband and I never argue about politics.", "не спо'рим"),
             ]),
        card("друг друга",
             "With many verbs “each other” is друг дру'га. Only the second word changes, according to the case the "
             "verb or preposition needs. Put the preposition between the two words: друг с дру'гом.",
             tables=[table(
                 ["Case", "Form", "Example"],
                 [["Accusative", "друг дру'га", "Мы давно' лю'бим друг дру'га."],
                  ["Dative", "друг дру'гу", "Они' всегда' помога'ют друг дру'гу."],
                  ["Instrumental", "друг с дру'гом", "Они' разгова'ривают друг с дру'гом."],
                  ["Prepositional", "друг о дру'ге", "Они' ду'мают друг о дру'ге."]])]),
    ],
    verify=(vf("дружить", "дружат", "дружит") + vf("разговаривать", "разговариваем", "разговаривают") + vf("спорить", "спорим")
            + vf("знать", "знают") + vf("любить", "любим") + vf("помогать", "помогают") + vf("писать", "пишут")
            + vf("думать", "думают") + vf("друг", "друга", "другу", "другом", "друге") + vf("муж", "мужем")
            + vf("политика", "политике")),
    exercises=[
        fb("Бори'с дру'жит ___ Ле'ной. (with)", ["с", "со", "к", "у"], "с", "Дружи'ть с + instrumental.", tr="Boris is friends with Lena."),
        fb("Мы с му'жем никогда' не ___ о поли'тике. (argue)", ["спо'рим", "спо'ришь", "спо'рит", "спо'рят"], "спо'рим", "Мы → -им.", tr="My husband and I never argue about politics.", lemma="спорить"),
        fb("Они' зна'ют друг ___ уже' пять лет. (each other)", ["дру'га", "дру'гу", "дру'гом", "дру'ге"], "дру'га", "Знать takes the accusative.", tr="They have known each other for five years.", lemma="друг"),
        fb("Брат и сестра' всегда' помога'ют друг ___.", ["дру'гу", "дру'га", "дру'гом", "дру'ге"], "дру'гу", "Помога'ть takes the dative.", tr="The brother and sister always help each other.", lemma="друг"),
        fb("Они' разгова'ривают друг ___ дру'гом.", ["с", "о", "к", "на"], "с", "Друг с дру'гом.", tr="They talk to each other."),
        fb("Мы давно' лю'бим друг ___.", ["дру'га", "дру'гу", "дру'гом", "дру'ге"], "дру'га", "Люби'ть takes the accusative.", tr="We have loved each other for a long time.", lemma="друг"),
        fb("Они' ду'мают друг ___ дру'ге.", ["о", "с", "к", "на"], "о", "Друг о дру'ге.", tr="They think about each other."),
        mc("Which phrase means “each other” as a direct object?", ["друг дру'га", "друг дру'гу", "друг с дру'гом", "друг о дру'ге"], "друг дру'га", "Accusative: друг дру'га."),
        mc("Which means “They help each other”?",
           ["Они' помога'ют друг дру'гу.", "Они' помога'ют друг дру'га.", "Они' помога'ются.", "Они' помога'ют друг с дру'гом."],
           "Они' помога'ют друг дру'гу.", "Помога'ть + dative."),
    ],
)

# ---------------------------------------------------------------------------- 161
L161 = lesson(
    "Declining last names: Петро́в, Толсто́й, Смит",
    "Я говорю' с Петро'вым. Я чита'ю кни'гу Толсто'го.",
    requires=["фамилия", "имя", "писатель", "книга", "поэт"],
    cards=[
        card("Men's Russian surnames",
             "Surnames in -ов, -ев and -ин decline like nouns, except that the instrumental is -ым. Surnames in -ой "
             "and -ий decline like adjectives in every case.",
             tables=[table(
                 ["Case", "Петро'в", "Толсто'й", "Маяко'вский"],
                 [["Nominative", "Петро'в", "Толсто'й", "Маяко'вский"],
                  ["Genitive, accusative", "Петро'в{а}", "Толсто'{го}", "Маяко'вск{ого}"],
                  ["Dative", "Петро'в{у}", "Толсто'{му}", "Маяко'вск{ому}"],
                  ["Instrumental", "Петро'в{ым}", "Толст{ы'м}", "Маяко'вск{им}"],
                  ["Prepositional", "Петро'в{е}", "Толсто'{м}", "Маяко'вск{ом}"]])],
             examples=[
                 ex("Я чита'ю кни'гу Толсто'го.", "I am reading Tolstoy's book.", "Толсто'го"),
                 ex("Мы говори'м о Маяко'вском.", "We are talking about Mayakovsky.", "о Маяко'вском"),
                 ex("Я разгова'риваю с Петро'вым.", "I am talking with Petrov.", "с Петро'вым"),
             ]),
        card("Women's and foreign surnames",
             "Russian women's surnames decline like feminine adjectives, but those in -ова, -ева and -ина have the "
             "accusative -у (Петро'ву), not -ую. Foreign men's surnames ending in a consonant decline like nouns "
             "(Смит, Сми'та), but foreign women's surnames do not change at all.",
             tables=[table(
                 ["Case", "Петро'ва", "Толста'я", "Смит (m)"],
                 [["Nominative", "Петро'ва", "Толста'я", "Смит"],
                  ["Accusative", "Петро'в{у}", "Толст{у'ю}", "Сми'т{а}"],
                  ["Genitive", "Петро'в{ой}", "Толст{о'й}", "Сми'т{а}"],
                  ["Instrumental", "Петро'в{ой}", "Толст{о'й}", "Сми'т{ом}"]])],
             examples=[
                 ex("Я зна'ю Петро'ву.", "I know Ms. Petrova.", "Петро'ву"),
                 ex("Э'то кни'га Сми'та.", "This is Smith's book.", "Сми'та"),
                 ex("Я зна'ю Э'мму Гилл.", "I know Emma Gill.", "Гилл"),
             ]),
    ],
    verify=(vf("фамилия", "фамилия") + vf("имя", "имя") + vf("писатель", "писатель") + vf("книга", "книгу")
            + vf("поэт", "поэт") + vf("разговаривать", "разговариваю") + vf("говорить", "говорим") + vf("читать", "читаю")
            + vf("знать", "знаю")),
    exercises=[
        fb("Я разгова'риваю с ___. (Mr Petrov)", ["Петро'вым", "Петро'в", "Петро'ва", "Петро'ву"], "Петро'вым", "Men's -ов surnames: instrumental -ым.", tr="I am talking with Mr Petrov."),
        fb("Я разгова'риваю с ___. (Ms Petrova)", ["Петро'вой", "Петро'ва", "Петро'ву", "Петро'вым"], "Петро'вой", "Women's surnames: -ой.", tr="I am talking with Ms Petrova."),
        fb("Мы чита'ем кни'гу ___. (Tolstoy)", ["Толсто'го", "Толсто'й", "Толсто'му", "Толсты'м"], "Толсто'го", "Adjective type, genitive: -ого.", tr="We are reading Tolstoy's book."),
        fb("Мы говори'м о ___. (Mayakovsky)", ["Маяко'вском", "Маяко'вского", "Маяко'вскому", "Маяко'вским"], "Маяко'вском", "О + prepositional.", tr="We are talking about Mayakovsky."),
        fb("Я зна'ю ___. (Ms Petrova)", ["Петро'ву", "Петро'ва", "Петро'вой", "Петро'вым"], "Петро'ву", "Accusative of -ова: -у.", tr="I know Ms Petrova."),
        fb("Э'то кни'га ___. (Smith)", ["Сми'та", "Смит", "Сми'ту", "Сми'том"], "Сми'та", "Foreign men's surnames decline like nouns.", tr="This is Smith's book."),
        fb("Я зна'ю Э'мму ___. (Gill)", ["Гилл", "Гилла", "Гиллу", "Гиллом"], "Гилл", "Foreign women's surnames do not change.", tr="I know Emma Gill."),
        mc("How does a man's surname in -ов decline in the instrumental?", ["like an adjective: -ым", "like a noun: -ом", "it does not change", "-ой"], "like an adjective: -ым", "Петро'вым."),
        mc("Which surname does not change?", ["Э'мма Гилл", "Ива'н Смит", "Алексе'й Петро'в", "Лев Толсто'й"], "Э'мма Гилл", "Foreign women's surnames are not declined."),
    ],
)

# ---------------------------------------------------------------------------- 162
L162 = lesson(
    "Going in, out, to, away: в-, вы-, при-, у-",
    "Он вошёл в класс. Она' вы'шла из ко'мнаты. Они' прие'хали.",
    requires=["входить", "выходить", "приходить", "уходить", "прийти"],
    cards=[
        card("Prefixes change the meaning",
             "Add a prefix to a verb of motion and it stops being unidirectional or multidirectional and becomes an "
             "ordinary imperfective or perfective verb. From -ходи'ть you get an imperfective and from -йти' the "
             "perfective. The prefix в- (in) is the opposite of вы- (out), and при- (arrive) is the opposite of у- (leave).",
             tables=[table(
                 ["Prefix", "Imperfective", "Perfective"],
                 [["в- (in)", "входи'ть", "войти'"],
                  ["вы- (out)", "выходи'ть", "вы'йти"],
                  ["при- (arrive)", "приходи'ть", "прийти'"],
                  ["у- (leave)", "уходи'ть", "уйти'"]])],
             examples=[
                 ex("В класс не входи'ть! Там идёт экза'мен.", "Don't enter the room! There is an exam.", "входи'ть"),
                 ex("Вчера' к нам пришли' го'сти.", "Guests came to see us yesterday.", "пришли'"),
                 ex("Он уже' ушёл домо'й.", "He has already gone home.", "ушёл"),
             ]),
        card("Other verbs of motion",
             "Ездить becomes -езжа'ть / -е'хать, бе'гать becomes -бега'ть / -бежа'ть, лета'ть becomes -лета'ть / "
             "-лете'ть and пла'вать becomes -плыва'ть / -плыть. After в- the hard sign appears before е: въезжа'ть, "
             "въе'хать.",
             tables=[table(
                 ["Prefix", "Imperfective", "Perfective"],
                 [["в-", "въезжа'ть", "въе'хать"],
                  ["вы-", "выезжа'ть", "вы'ехать"],
                  ["при-", "приезжа'ть", "прие'хать"],
                  ["у-", "уезжа'ть", "уе'хать"]],
                 title="by vehicle")]),
        card("Running, flying, swimming",
             "The same pattern works for running (-бега'ть, -бежа'ть), flying (-лета'ть, -лете'ть) and swimming "
             "(-плыва'ть, -плыть). Note that in perfective forms with вы- the stress moves onto the prefix: вы'бежать, "
             "вы'лететь, вы'плыть.",
             tables=[table(
                 ["Prefix", "Run", "Fly", "Swim"],
                 [["в-", "вбежа'ть", "влете'ть", "вплыть"],
                  ["вы-", "вы'бежать", "вы'лететь", "вы'плыть"],
                  ["при-", "прибежа'ть", "прилете'ть", "приплы'ть"],
                  ["у-", "убежа'ть", "улете'ть", "уплы'ть"]])]),
    ],
    verify=(vf("входить", "входить") + vf("войти", "вошёл") + vf("выходить", "выходить") + vf("выйти", "выйти", "вышла")
            + vf("приходить", "приходить") + vf("прийти", "прийти", "пришли") + vf("уходить", "уходить")
            + vf("уйти", "уйти", "ушёл") + vf("въезжать", "въезжать") + vf("въехать", "въехать")
            + vf("выезжать", "выезжать") + vf("выехать", "выехать") + vf("приезжать", "приезжать")
            + vf("приехать", "приехать", "приехали") + vf("уезжать", "уезжать") + vf("уехать", "уехать", "уедут")
            + vf("вбежать", "вбежать") + vf("влететь", "влететь")
            + vf("выбежать", "выбежать") + vf("вылететь", "вылететь") + vf("выплыть", "выплыть")
            + vf("прибежать", "прибежать") + vf("прилететь", "прилететь") + vf("приплыть", "приплыть")
            + vf("убежать", "убежать") + vf("улететь", "улететь", "улетели") + vf("уплыть", "уплыть")
            + vf("экзамен", "экзамен") + vf("гость", "гости") + vf("класс", "класс")),
    exercises=[
        fb("Он ___ в класс и сел. (walked in)", ["вошёл", "вы'шел", "ушёл", "вы'ехал"], "вошёл", "В- = into.", tr="He walked into the classroom and sat down.", lemma="войти"),
        fb("Она' ___ из ко'мнаты. (walked out)", ["вы'шла", "вошла'", "пришла'", "вы'ехала"], "вы'шла", "Вы- = out of.", tr="She walked out of the room.", lemma="выйти"),
        fb("Вчера' к нам ___ го'сти. (arrived on foot)", ["пришли'", "ушли'", "вошли'", "вы'шли"], "пришли'", "При- = arrive.", tr="Guests came to see us yesterday.", lemma="прийти"),
        fb("За'втра они' ___ домо'й. (will leave by car)", ["уе'дут", "прие'дут", "вы'едут", "въе'дут"], "уе'дут", "У- = leave.", tr="Tomorrow they will drive off home.", lemma="уехать"),
        fb("Пти'цы ___ на юг. (flew away)", ["улете'ли", "прилете'ли", "влете'ли", "вы'летели"], "улете'ли", "У- = away.", tr="The birds flew south.", lemma="улететь"),
        fb("Я ___ из до'ма в 7 часо'в. (every day, leave)", ["выхожу'", "вы'йду", "вы'шел", "вы'шла"], "выхожу'", "Imperfective, present.", tr="I leave the house at 7 o'clock.", lemma="выходить"),
        mc("Which prefix means “out of”?", ["вы-", "в-", "при-", "у-"], "вы-", "Вы- = out of.", order=True),
        mc("Which verb is perfective?", ["войти'", "входи'ть", "выходи'ть", "приходи'ть"], "войти'", "Войти' is perfective."),
        mc("What happens to в- before -езжа'ть and -е'хать?", ["a hard sign is added: въезжа'ть", "it becomes во-", "it becomes вы-", "nothing changes"], "a hard sign is added: въезжа'ть", "Въе'хать."),
    ],
)

# ---------------------------------------------------------------------------- 163
L163 = lesson(
    "Where to, where from: prepositions with prefixed motion verbs",
    "Он вошёл в ко'мнату. Она' прие'хала к дру'гу.",
    requires=["войти", "выйти", "приехать", "уехать", "театр"],
    cards=[
        card("Prefix and preposition",
             "Each prefix pairs with certain prepositions. Войти' and вы'йти have one each. При- and у- mean going "
             "to or away from a place, so they use the same prepositions as ordinary motion: в / на + accusative, "
             "к + dative for destinations and из / с / от + genitive for starting points.",
             tables=[table(
                 ["Prefix", "Preposition", "Example"],
                 [["в-", "в + Acc.", "войти' в ко'мнату"],
                  ["вы-", "из + Gen.", "вы'йти из кла'сса"],
                  ["вы- (out into)", "на / в + Acc.", "вы'бежать на у'лицу"],
                  ["при-", "в / на + Acc., к + Dat.", "прийти' в теа'тр, прие'хать к дру'гу"],
                  ["при- (from)", "из / с / от + Gen.", "прийти' из теа'тра, прие'хать от дру'га"],
                  ["у-", "в / на + Acc., к + Dat.", "уйти' в теа'тр, уе'хать к дру'гу"],
                  ["у- (from)", "из / с / от + Gen.", "уйти' из теа'тра, улете'ть с конфере'нции"]])],
             examples=[
                 ex("Он вошёл в ко'мнату.", "He walked into the room.", "в ко'мнату"),
                 ex("Она' вы'шла из кла'сса.", "She walked out of the classroom.", "из кла'сса"),
                 ex("Мы прие'хали к дру'гу.", "We arrived at a friend's.", "к дру'гу"),
                 ex("Мы прие'хали от дру'га.", "We came back from a friend's.", "от дру'га"),
             ]),
        card("Opposites and stepping out",
             "Войти' is the opposite of вы'йти, and прийти' is the opposite of уйти'. Вы'йти also means to step out for "
             "a short time: Где дире'ктор? — Он вы'шел. Подожди'те немно'го.",
             examples=[
                 ex("Где дире'ктор? — Он вы'шел. Подожди'те немно'го.", "Where is the director? — He stepped out. Wait a bit.", "вы'шел"),
                 ex("Мы прилете'ли с конфере'нции.", "We flew in from a conference.", "с конфере'нции"),
             ]),
    ],
    verify=(vf("войти", "вошёл") + vf("выйти", "вышла", "вышел") + vf("приехать", "приехали") + vf("уехать", "уехали")
            + vf("театр", "театра", "театр") + vf("класс", "класса") + vf("друг", "друга", "другу") + vf("комната", "комнату")
            + vf("прилететь", "прилетели") + vf("подождать", "подождите") + vf("директор", "директор")),
    exercises=[
        fb("Он вошёл ___ ко'мнату.", ["в", "из", "к", "от"], "в", "В- goes with в + accusative.", tr="He walked into the room."),
        fb("Она' вы'шла ___ кла'сса.", ["из", "в", "к", "на"], "из", "Вы- goes with из + genitive.", tr="She walked out of the classroom."),
        fb("Мы прие'хали ___ дру'гу. (to a friend's)", ["к", "в", "из", "от"], "к", "To a person: к + dative.", tr="We arrived at a friend's."),
        fb("Мы прие'хали ___ дру'га. (from a friend's)", ["от", "к", "в", "на"], "от", "From a person: от + genitive.", tr="We came from a friend's."),
        fb("Она' прилете'ла ___ конфере'нции. (from)", ["с", "на", "в", "к"], "с", "From an event: с + genitive.", tr="She flew in from the conference."),
        fb("Он вы'бежал ___ у'лицу. (out into)", ["на", "из", "к", "от"], "на", "Out into: на + accusative.", tr="He ran out into the street."),
        fb("Он ___ из теа'тра в 10 часо'в. (left)", ["ушёл", "вошёл", "влете'л", "въе'хал"], "ушёл", "Из + genitive with у-.", tr="He left the theater at 10."),
        mc("Which is the opposite of войти'?", ["вы'йти", "прийти'", "уйти'", "прие'хать"], "вы'йти", "В- ↔ вы-."),
        mc("Which preposition means “from a person's place”?", ["от", "к", "из", "на"], "от", "От + genitive."),
    ],
)

# ---------------------------------------------------------------------------- 164
L164 = lesson(
    "Aspect with prefixed motion verbs",
    "Обы'чно я выхожу' в 7, но вчера' вы'шел в 9.",
    requires=["приходить", "уйти", "гость", "вчера", "дверь"],
    cards=[
        card("Which aspect?",
             "Prefixed verbs of motion follow the same aspect rules as other verbs. The perfective exists only in the "
             "past and the future. The imperfective works in all three tenses and shows habit, repetition or process. "
             "The perfective shows a single completed action or an intention to complete it.",
             tables=[table(
                 ["Meaning", "Example"],
                 [["habit (imperfective)", "Обы'чно я выхожу' из до'ма в 7 утра'."],
                  ["one time (perfective)", "Вчера' я вы'шел из до'ма в 9. За'втра я вы'йду в 9."],
                  ["process (imperfective)", "Когда' я выходи'л из до'ма, зазвони'л телефо'н."],
                  ["result (perfective)", "Он уже' ушёл домо'й."]])],
             examples=[
                 ex("В про'шлом году' я ка'ждый день выходи'л из до'ма в 8 часо'в.", "Last year I left the house at 8 every day.", "выходи'л"),
                 ex("Ско'ро пти'цы улетя'т на юг.", "Soon the birds will fly south.", "улетя'т"),
             ]),
        card("“Visited” and “has been”",
             "In the past tense the imperfective can also report that an action happened and is over: the person "
             "came and left. The perfective says that they arrived and are still there.",
             tables=[table(
                 ["Imperfective (visited, gone)", "Perfective (arrived, still here)"],
                 [["Вчера' к нам приходи'ли го'сти.", "Вчера' к нам пришли' го'сти."],
                  ["Сего'дня ко мне никто' не приходи'л.", "К нам пришёл друг."]])],
             examples=[
                 ex("Вчера' к нам приходи'ли го'сти.", "Guests visited us yesterday.", "приходи'ли"),
                 ex("Дверь откры'та. В э'ту ко'мнату кто-то входи'л.", "The door is open. Someone has been in this room.", "входи'л"),
             ]),
    ],
    verify=(vf("выходить", "выхожу", "выходил") + vf("выйти", "вышел", "выйду") + vf("приходить", "приходили", "приходил")
            + vf("прийти", "пришли", "пришёл") + vf("уйти", "ушёл") + vf("улететь", "улетят") + vf("гость", "гости")
            + vf("войти", "вошёл") + vf("входить", "входил") + vf("дверь", "дверь") + vf("открытый", "открыта")
           ),
    exercises=[
        fb("Обы'чно я ___ из до'ма в 7 часо'в. (leave, habit)", ["выхожу'", "вы'йду", "вы'шел", "вы'шла"], "выхожу'", "Habit: imperfective.", tr="I usually leave the house at 7.", lemma="выходить"),
        fb("Вчера' я ___ из до'ма в 9 часо'в. (left, once)", ["вы'шел", "выхожу'", "вы'йду", "выхо'дишь"], "вы'шел", "One time: perfective.", tr="Yesterday I left the house at 9.", lemma="выйти"),
        fb("За'втра я то'же ___ в 9. (will leave)", ["вы'йду", "вы'шел", "вы'шла", "вы'шли"], "вы'йду", "Future, one time: perfective.", tr="Tomorrow I will also leave at 9.", lemma="выйти"),
        fb("Он уже' ___ домо'й. (has left)", ["ушёл", "ушла'", "ухожу'", "уйдёт"], "ушёл", "Result: perfective.", tr="He has already gone home.", lemma="уйти"),
        fb("Ско'ро пти'цы ___ на юг. (will fly away)", ["улетя'т", "улета'ли", "улете'ли", "улета'л"], "улетя'т", "Future, completion: perfective.", tr="Soon the birds will fly south.", lemma="улететь"),
        mc("What does Вчера' к нам приходи'ли го'сти mean?",
           ["Guests visited us (and have gone)", "Guests are here now", "Guests will come", "Guests never came"],
           "Guests visited us (and have gone)", "Imperfective past: the visit is over."),
        mc("Which aspect can be used in the present tense?", ["imperfective", "perfective", "both", "neither"], "imperfective", "Only the imperfective has a present tense.", order=True),
        mc("Which means “Yesterday guests came (and left)”?",
           ["Вчера' к нам приходи'ли го'сти.", "Вчера' к нам придут го'сти.", "Вчера' к нам ухо'дят го'сти.", "Вчера' к нам прихо'дят го'сти."],
           "Вчера' к нам приходи'ли го'сти.", "Past imperfective."),
    ],
)

# ---------------------------------------------------------------------------- 165
L165 = lesson(
    "Guests and holidays: гость, праздник, С днём рождения!",
    "Поздравля'ю тебя' с днём рожде'ния! Жела'ю тебе' здоро'вья!",
    requires=["гость", "хозяин", "праздник", "приглашать", "здоровье"],
    cards=[
        card("Having people over",
             "Go to someone's house в го'сти (as a guest). The person who invites you is the хозя'ин (host, owner) "
             "or хозя'йка. Приглаша'ть / пригласи'ть means to invite, and отмеча'ть means to celebrate a holiday.",
             tables=[table(
                 ["Russian", "English"],
                 [["гость, гостья", "guest (m, f)"],
                  ["хозя'ин, хозя'йка", "host, hostess"],
                  ["в го'сти", "(to go) as a guest"],
                  ["пра'здник", "holiday"],
                  ["приглаша'ть / пригласи'ть", "to invite"],
                  ["отмеча'ть", "to celebrate"]])],
             examples=[
                 ex("Приходи'те к нам в го'сти!", "Come and visit us!", "в го'сти"),
                 ex("Хозя'ин пригласи'л Ни'ну за стол.", "The host invited Nina to the table.", "пригласи'л"),
                 ex("Мы отмеча'ем пра'здник в суббо'ту.", "We are celebrating the holiday on Saturday.", "отмеча'ем"),
             ]),
        card("Congratulations, wishes and toasts",
             "Поздравля'ть с + instrumental names the occasion. Жела'ть takes the dative of the person and the "
             "genitive of what you wish. The toast За + accusative names the person or thing you drink to.",
             tables=[table(
                 ["Russian", "English"],
                 [["С днём рожде'ния!", "Happy birthday!"],
                  ["С Но'вым го'дом!", "Happy New Year!"],
                  ["С пра'здником!", "Happy holiday!"],
                  ["Жела'ю тебе' здоро'вья!", "I wish you health!"],
                  ["За ва'ше здоро'вье!", "To your health!"],
                  ["Прия'тного аппети'та!", "Bon appétit!"]])],
             examples=[
                 ex("Поздравля'ю тебя' с днём рожде'ния!", "I congratulate you on your birthday!", "с днём рожде'ния"),
                 ex("Жела'ю тебе' здоро'вья и сча'стья!", "I wish you health and happiness!", "здоро'вья"),
             ]),
    ],
    verify=(vf("гость", "гости") + vf("хозяин", "хозяин") + vf("праздник", "праздник") + vf("приглашать", "приглашаю")
            + vf("пригласить", "пригласил") + vf("отмечать", "отмечаем") + vf("поздравлять", "поздравляю")
            + vf("желать", "желаю") + vf("здоровье", "здоровья", "здоровье") + vf("день", "днём") + vf("новый", "новым")
            + vf("год", "годом") + vf("приходить", "приходите")),
    exercises=[
        fb("Поздравля'ю тебя' ___ днём рожде'ния! (on)", ["с", "на", "за", "о"], "с", "Поздравля'ть с + instrumental.", tr="Happy birthday to you!"),
        fb("Жела'ю тебе' ___. (health)", ["здоро'вья", "здоро'вье", "здоро'вьем", "здоро'вью"], "здоро'вья", "Жела'ть + dative + genitive.", tr="I wish you health.", lemma="здоровье"),
        fb("Приходи'те к нам в ___! (as guests)", ["го'сти", "гость", "го'стя", "го'стем"], "го'сти", "Fixed phrase: в го'сти.", tr="Come visit us!", lemma="гость"),
        fb("Вчера' к нам пришли' ___. (guests)", ["го'сти", "гость", "го'стя", "го'стем"], "го'сти", "Plural nominative: го'сти.", tr="Guests came to see us yesterday.", lemma="гость"),
        fb("Хозя'ин пригласи'л Ни'ну за ___. (the table)", ["стол", "столо'м", "стола'", "столу'"], "стол", "Куда'? → за + accusative.", tr="The host invited Nina to the table."),
        fb("С ___ го'дом! (New)", ["Но'вым", "Но'вый", "Но'вого", "Но'вому"], "Но'вым", "С + instrumental.", tr="Happy New Year!", lemma="новый"),
        fb("За ва'ше ___! (health, toast)", ["здоро'вье", "здоро'вья", "здоро'вьем", "здоро'вью"], "здоро'вье", "За + accusative.", tr="To your health!", lemma="здоровье"),
        fb("Мы отмеча'ем ___ в суббо'ту. (the holiday)", ["пра'здник", "пра'здника", "пра'здником", "пра'зднику"], "пра'здник", "Accusative = nominative.", tr="We celebrate the holiday on Saturday.", lemma="праздник"),
        mc("Which means “Happy birthday!”?", ["С днём рожде'ния!", "На день рожде'ния!", "К дню рожде'ния!", "Дня рожде'ния!"], "С днём рожде'ния!", "С + instrumental."),
        mc("Which means “Bon appétit!”?", ["Прия'тного аппети'та!", "За ва'ше здоро'вье!", "С пра'здником!", "До свида'ния!"], "Прия'тного аппети'та!", "Прия'тного аппети'та!"),
    ],
)

# ---------------------------------------------------------------------------- 166
L166 = lesson(
    "Setting the table: таре́лка, ви́лка, блины́",
    "Ма'ма накрыва'ет на стол. Положи' ви'лку ря'дом с таре'лкой.",
    requires=["тарелка", "ложка", "посуда", "пирог", "ужин"],
    cards=[
        card("On the table",
             "To set the table is накрыва'ть на стол (accusative!). Here are the things you put on it.",
             tables=[table(
                 ["Russian", "English"],
                 [["таре'лка", "plate"],
                  ["ло'жка", "spoon"],
                  ["ви'лка", "fork"],
                  ["нож", "knife"],
                  ["салфе'тка", "napkin"],
                  ["посу'да", "dishes, tableware"]])],
             examples=[
                 ex("Ма'ма накрыва'ет на стол.", "Mom is setting the table.", "накрыва'ет на стол"),
                 ex("Положи' ви'лку ря'дом с таре'лкой.", "Put the fork next to the plate.", "с таре'лкой"),
                 ex("На столе' стоя'т таре'лки и ло'жки.", "Plates and spoons are on the table.", "стоя'т"),
             ]),
        card("Food and treats",
             "These words are useful for any Russian meal. Note that пиро'жное and моро'женое decline like "
             "adjectives, and пече'нье and колбаса' follow the patterns you know.",
             tables=[table(
                 ["Russian", "English"],
                 [["блины'", "blini, thin pancakes"],
                  ["пиро'г", "pie"],
                  ["пирожо'к", "small filled bun"],
                  ["пиро'жное", "pastry, cake"],
                  ["пече'нье", "cookies"],
                  ["моро'женое", "ice cream"],
                  ["колбаса'", "sausage"],
                  ["капу'ста", "cabbage"],
                  ["заку'ска", "appetizer"]])],
             examples=[
                 ex("Мы пьём чай с пече'ньем.", "We drink tea with cookies.", "с пече'ньем"),
                 ex("Э'то пиро'г с капу'стой.", "This is a cabbage pie.", "с капу'стой"),
                 ex("На десе'рт мы ели моро'женое.", "We had ice cream for dessert.", "моро'женое"),
             ]),
    ],
    verify=(vf("тарелка", "тарелкой") + vf("ложка", "ложкой") + vf("вилка", "вилкой", "вилку") + vf("нож", "ножи")
            + vf("салфетка", "салфетку") + vf("посуда", "посуда") + vf("накрывать", "накрывает") + vf("блин", "блины")
            + vf("пирог", "пирог", "пирогом") + vf("пирожное", "пирожное")
            + vf("печенье", "печеньем") + vf("мороженое", "мороженое") + vf("колбаса", "колбасой")
            + vf("капуста", "капустой") + vf("закуска", "закуска") + vf("ужин", "ужин") + vf("стол", "стол", "столе")
            + vf("стоять", "стоят")),
    exercises=[
        fb("Ма'ма накрыва'ет на ___. (the table)", ["стол", "столо'м", "столе'", "стола'"], "стол", "Накрыва'ть на стол: accusative.", tr="Mom is setting the table.", lemma="стол"),
        fb("Положи' ви'лку ря'дом с ___. (the plate)", ["таре'лкой", "таре'лка", "таре'лку", "таре'лке"], "таре'лкой", "Ря'дом с + instrumental.", tr="Put the fork next to the plate.", lemma="тарелка"),
        fb("Я ем сала'т ___. (with a fork)", ["ви'лкой", "ви'лка", "ви'лку", "ви'лке"], "ви'лкой", "Tool: instrumental.", tr="I eat salad with a fork.", lemma="вилка"),
        fb("На десе'рт мы ели ___. (ice cream)", ["моро'женое", "моро'женого", "моро'женым", "моро'женому"], "моро'женое", "Accusative = nominative for neuter.", tr="For dessert we had ice cream.", lemma="мороженое"),
        fb("Э'то ___ с капу'стой. (pie)", ["пиро'г", "пиро'га", "пиро'гу", "пиро'гом"], "пиро'г", "Nominative.", tr="This is a cabbage pie.", lemma="пирог"),
        fb("Мы пьём чай с ___. (cookies)", ["пече'ньем", "пече'нье", "пече'нья", "пече'нью"], "пече'ньем", "С + instrumental: -ьем.", tr="We drink tea with cookies.", lemma="печенье"),
        mc("Which word means “napkin”?", ["салфе'тка", "посу'да", "ло'жка", "заку'ска"], "салфе'тка", "Салфе'тка."),
        mc("Which word means “dishes, tableware”?", ["посу'да", "заку'ска", "пече'нье", "колбаса'"], "посу'да", "Посу'да."),
    ],
)

# ---------------------------------------------------------------------------- 167
L167 = lesson(
    "Relative clauses in every case: с которым, о которой",
    "Э'то де'вушка, о кото'рой я говорю'.",
    requires=["который", "человек", "друг", "книга", "город"],
    cards=[
        card("Gender from the noun, case from the clause",
             "Кото'рый (which, who, that) agrees in gender and number with the noun it refers to, but its case "
             "depends on its job in its own clause, including after a preposition.",
             tables=[table(
                 ["Case", "Masculine, neuter", "Feminine"],
                 [["Nominative", "кото'рый", "кото'рая"],
                  ["Genitive", "кото'рого", "кото'рой"],
                  ["Dative", "кото'рому", "кото'рой"],
                  ["Accusative", "кото'рый / кото'рого", "кото'рую"],
                  ["Instrumental", "кото'рым", "кото'рой"],
                  ["Prepositional", "кото'ром", "кото'рой"]])],
             examples=[
                 ex("Э'то ма'льчик, с кото'рым я дружу'.", "This is the boy I am friends with.", "с кото'рым"),
                 ex("Э'то де'вушка, о кото'рой я говорю'.", "This is the girl I am talking about.", "о кото'рой"),
                 ex("Вот дом, в кото'ром я живу'.", "Here is the house I live in.", "в кото'ром"),
                 ex("Э'то учи'тель, кото'рому я помога'ю.", "This is the teacher I help.", "кото'рому"),
                 ex("Вот кни'га, кото'рую я купи'л вчера'.", "Here is the book that I bought yesterday.", "кото'рую"),
             ]),
    ],
    verify=(vf("который", "которым", "которой", "котором", "которому", "которую", "которого") + vf("дружить", "дружу")
            + vf("говорить", "говорю") + vf("жить", "живу") + vf("помогать", "помогаю") + vf("купить", "купил")
            + vf("мальчик", "мальчик")),
    exercises=[
        fb("Э'то ма'льчик, с ___ я дружу'. (whom)", ["кото'рым", "кото'рый", "кото'рого", "кото'рому"], "кото'рым", "С + instrumental, masculine.", tr="This is the boy I am friends with.", lemma="который"),
        fb("Э'то де'вушка, о ___ я говорю'.", ["кото'рой", "кото'рая", "кото'рую", "кото'рым"], "кото'рой", "О + prepositional, feminine.", tr="This is the girl I am talking about.", lemma="который"),
        fb("Вот дом, в ___ я живу'.", ["кото'ром", "кото'рый", "кото'рого", "кото'рым"], "кото'ром", "В + prepositional, masculine.", tr="Here is the house I live in.", lemma="который"),
        fb("Э'то учи'тель, ___ я помога'ю. (to whom)", ["кото'рому", "кото'рый", "кото'рого", "кото'рым"], "кото'рому", "Помога'ть takes the dative.", tr="This is the teacher I help.", lemma="который"),
        fb("Вот кни'га, ___ я купи'л вчера'. (that)", ["кото'рую", "кото'рая", "кото'рой", "кото'рые"], "кото'рую", "Accusative feminine.", tr="Here is the book that I bought yesterday.", lemma="который"),
        fb("Вот ру'чка, ___ я пишу'. (with which)", ["кото'рой", "кото'рая", "кото'рую", "кото'рым"], "кото'рой", "Instrumental feminine.", tr="Here is the pen I write with.", lemma="который"),
        mc("What decides the gender of кото'рый?", ["The noun it refers to", "The verb that follows", "The preposition", "The tense"], "The noun it refers to", "Gender from the noun it replaces."),
        mc("What decides the case of кото'рый?", ["Its role in its own clause", "The noun it refers to", "The previous sentence", "The number"], "Its role in its own clause", "Case from the clause."),
    ],
)

# ---------------------------------------------------------------------------- 168
L168 = lesson(
    "Review: the instrumental, reciprocals and prefixed motion",
    "Мы с ма'мой накрыва'ем на стол. Гости пришли'.",
    requires=["стол", "гость", "друг", "приходить", "праздник"],
    cards=[
        card("Quick map",
             "A review of the main ideas of this unit.",
             tables=[table(
                 ["Topic", "Example"],
                 [["с = and", "Мы с ма'мой лю'бим тебя'."],
                  ["над, пе'ред, ме'жду, ря'дом с", "Ла'мпа виси'т над столо'м."],
                  ["Где? or Куда'?", "под столо'м / под стол"],
                  ["Putting vs being", "класть и лежа'ть"],
                  ["Each other", "встреча'ться, друг дру'га"],
                  ["Prefixed motion", "войти', вы'йти, прийти', уйти'"],
                  ["Relative clause", "Э'то де'вушка, о кото'рой я говорю'."]])]),
    ],
    verify=(vf("мама", "мамой") + vf("стол", "столом") + vf("друг", "друга") + vf("входить", "входить")),
    exercises=[
        fb("___ с ма'мой лю'бим тебя'. (Mom and I)", ["Мы", "Вы", "Они'", "Я"], "Мы", "Мы с + instrumental = “and I”.", tr="Mom and I love you."),
        fb("Ла'мпа виси'т ___ столо'м. (above)", ["над", "под", "за", "на"], "над", "Над + instrumental.", tr="The lamp hangs above the table."),
        fb("Положи' рюкза'к под ___.", ["стол", "столо'м", "стола'", "столу'"], "стол", "Motion: accusative.", tr="Put the backpack under the table.", lemma="стол"),
        fb("Рюкза'к лежи'т под ___.", ["столо'м", "стол", "стола'", "столу'"], "столо'м", "Location: instrumental.", tr="The backpack is under the table.", lemma="стол"),
        fb("Мы с Са'шей ___ ка'ждый день. (meet)", ["встреча'емся", "встреча'юсь", "встреча'ется", "встреча'ются"], "встреча'емся", "Reciprocal -ся.", tr="Sasha and I meet every day."),
        fb("Брат и сестра' помога'ют друг ___.", ["дру'гу", "дру'га", "дру'гом", "дру'ге"], "дру'гу", "Помога'ть + dative.", tr="The brother and sister help each other.", lemma="друг"),
        fb("Мы говори'м о ___. (Mayakovsky)", ["Маяко'вском", "Маяко'вского", "Маяко'вскому", "Маяко'вским"], "Маяко'вском", "О + prepositional.", tr="We are talking about Mayakovsky."),
        fb("Вчера' к нам ___ го'сти. (arrived on foot)", ["пришли'", "ушли'", "вошли'", "вы'шли"], "пришли'", "При- = arrive.", tr="Guests came to see us yesterday."),
        fb("Поздравля'ю тебя' ___ пра'здником! (on)", ["с", "на", "за", "о"], "с", "Поздравля'ть с + instrumental.", tr="Happy holiday to you!"),
        fb("Э'то де'вушка, о ___ я говорю'.", ["кото'рой", "кото'рая", "кото'рую", "кото'рым"], "кото'рой", "О + prepositional, feminine.", tr="This is the girl I am talking about.", lemma="который"),
    ],
)

UNIT = unit("Unit 18: Instrumental continued, reciprocal verbs and prefixed motion",
            [L155, L156, L157, L158, L159, L160, L161, L162, L163, L164, L165, L166, L167, L168])
