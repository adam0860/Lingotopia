"""Unit 17: the instrumental case (textbook module 4, lesson 23)."""
from dsl import *

# ---------------------------------------------------------------------------- 144
L144 = lesson(
    "With whom? с + instrumental",
    "Я иду' в парк с дру'гом. Она' гуля'ет с сестро'й.",
    requires=["друг", "сестра", "учитель", "семья", "разговаривать"],
    cards=[
        card("Together with: с + instrumental",
             "The instrumental case answers the questions Кем? and Чем? (with whom? with what?). With the "
             "preposition с it means “together with”. Masculine and neuter nouns take -ом, or -ем after a soft "
             "stem, and feminine nouns take -ой, or -ей after a soft stem. When the ending is stressed, -ем and "
             "-ей are written -ём and -ёй.",
             tables=[table(
                 ["Nominative", "Instrumental", "Ending"],
                 [["друг", "дру'г{ом}", "-ом"],
                  ["окно'", "окн{о'м}", "-ом"],
                  ["учи'тель", "учи'тел{ем}", "-ем"],
                  ["слова'рь", "словар{ём}", "-ём"],
                  ["музе'й", "музе'{ем}", "-ем"],
                  ["сестра'", "сестр{о'й}", "-ой"],
                  ["тётя", "тёт{ей}", "-ей"],
                  ["семья'", "семь{ёй}", "-ёй"]])],
             examples=[
                 ex("Я иду' в парк с дру'гом.", "I am going to the park with a friend.", "с дру'гом"),
                 ex("Она' гуля'ет с сестро'й.", "She is walking with her sister.", "с сестро'й"),
                 ex("Я живу' с семьёй.", "I live with my family.", "с семьёй"),
                 ex("Мы разгова'риваем с учи'телем.", "We are talking with the teacher.", "с учи'телем"),
             ]),
        card("Verbs that go with с",
             "Several verbs of joint action take с + instrumental: знако'миться / познако'миться (to meet for "
             "the first time), встреча'ться (to meet, to date), разгова'ривать and поговори'ть (to talk). The word "
             "с becomes со before some clusters, as in со словарём.",
             examples=[
                 ex("Я познако'мился с Ни'ной в сентябре'.", "I met Nina in September.", "с Ни'ной"),
                 ex("Ко'ля встреча'ется с Ма'шей.", "Kolya is dating Masha.", "с Ма'шей"),
                 ex("Вчера' я разгова'ривал с дире'ктором.", "Yesterday I talked with the director.", "с дире'ктором"),
                 ex("Он идёт в магази'н со словарём.", "He goes to the shop with a dictionary.", "со словарём"),
             ]),
    ],
    verify=(vf("друг", "другом") + vf("окно", "окном") + vf("учитель", "учителем") + vf("словарь", "словарём")
            + vf("музей", "музеем") + vf("сестра", "сестрой") + vf("тётя", "тётей") + vf("семья", "семьёй")
            + vf("разговаривать", "разговариваем", "разговаривал") + vf("познакомиться", "познакомился")
            + vf("встречаться", "встречается") + vf("директор", "директором") + vf("идти", "иду", "идёт")
            + vf("жить", "живу") + vf("гулять", "гуляет")),
    exercises=[
        fb("Я иду' в парк с ___. (a friend)", ["дру'гом", "друг", "дру'га", "дру'гу"], "дру'гом", "Masculine hard stem: -ом.", tr="I am going to the park with a friend.", lemma="друг"),
        fb("Она' гуля'ет с ___. (sister)", ["сестро'й", "сестра'", "сестре'", "сестру'"], "сестро'й", "Feminine hard stem, stressed ending: -о'й.", tr="She is walking with her sister.", lemma="сестра"),
        fb("Мы разгова'риваем с ___. (the teacher)", ["учи'телем", "учи'тель", "учи'теля", "учи'телю"], "учи'телем", "Soft stem: -ем.", tr="We are talking with the teacher.", lemma="учитель"),
        fb("Я живу' с ___. (family)", ["семьёй", "семья'", "семью'", "семье'"], "семьёй", "Stressed soft feminine ending: -ёй.", tr="I live with my family.", lemma="семья"),
        fb("Мы жи'ли с ___. (aunt)", ["тётей", "тётя", "тёте", "тётю"], "тётей", "Soft feminine: -ей.", tr="We lived with an aunt.", lemma="тётя"),
        fb("Он идёт в магази'н со ___. (a dictionary)", ["словарём", "словарь", "словаря'", "словарю'"], "словарём", "Stressed soft masculine ending: -ём.", tr="He goes to the shop with a dictionary.", lemma="словарь"),
        fb("Мы встреча'емся с ___. (Masha)", ["Ма'шей", "Ма'ша", "Ма'шу", "Ма'ше"], "Ма'шей", "Soft feminine: -ей.", tr="We are seeing Masha."),
        mc("Which ending do feminine nouns with a hard stem take in the instrumental?", ["-ой", "-ом", "-ей", "-ем"], "-ой", "Сестро'й, ма'мой.", order=True),
        mc("Which means “with a friend”?", ["с дру'гом", "с друг", "с дру'га", "с дру'гу"], "с дру'гом", "С + instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 145
L145 = lesson(
    "Mother, daughter, father, day: special instrumentals",
    "Я горжу'сь ма'терью. С днём рожде'ния!",
    requires=["мать", "дочь", "отец", "день", "имя"],
    cards=[
        card("Soft-sign nouns and the long stems",
             "Feminine nouns ending in -ь take -ью: но'чью. Мать and дочь add the syllable -ер- in all cases "
             "except the nominative and accusative: ма'терью, до'черью. Words in -ец and день lose the е: отцо'м, "
             "днём. The neuter nouns и'мя and вре'мя add -ен-: и'менем, вре'менем. Masculine nouns in -а or -я, "
             "such as па'па and дя'дя, take the feminine endings.",
             tables=[table(
                 ["Nominative", "Instrumental", "Note"],
                 [["ночь", "но'чь{ю}", "-ью"],
                  ["мать", "ма'тер{ью}", "-ер-"],
                  ["дочь", "до'чер{ью}", "-ер-"],
                  ["оте'ц", "отц{о'м}", "e drops out"],
                  ["день", "дн{ём}", "e drops out"],
                  ["и'мя", "и'мен{ем}", "-ен-"],
                  ["вре'мя", "вре'мен{ем}", "-ен-"],
                  ["па'па", "па'п{ой}", "like feminine"],
                  ["дя'дя", "дя'д{ей}", "like feminine"]])],
             examples=[
                 ex("Я иду' с ма'терью.", "I am going with my mother.", "с ма'терью"),
                 ex("Дочь горди'тся ма'терью.", "The daughter is proud of her mother.", "ма'терью"),
                 ex("Я поговори'л с отцо'м.", "I talked with my father.", "с отцо'м"),
                 ex("С днём рожде'ния!", "Happy birthday!", "С днём"),
                 ex("Я горжу'сь ма'мой и па'пой, тётей и дя'дей!", "I am proud of my mom and dad, my aunt and uncle!", "ма'мой и па'пой"),
             ]),
    ],
    verify=(vf("мать", "матерью") + vf("дочь", "дочерью") + vf("отец", "отцом") + vf("день", "днём")
            + vf("имя", "именем") + vf("время", "временем") + vf("ночь", "ночью") + vf("папа", "папой")
            + vf("дядя", "дядей") + vf("мама", "мамой") + vf("тётя", "тётей") + vf("гордиться", "гордится", "горжусь")
            + vf("поговорить", "поговорил")),
    exercises=[
        fb("Я иду' с ___. (mother)", ["ма'терью", "мать", "ма'тери"], "ма'терью", "Мать gets -ер- and -ью.", tr="I am going with my mother.", lemma="мать"),
        fb("Она' гуля'ет с ___. (daughter)", ["до'черью", "дочь", "до'чери"], "до'черью", "Дочь gets -ер- and -ью.", tr="She is walking with her daughter.", lemma="дочь"),
        fb("Я поговори'л с ___. (father)", ["отцо'м", "оте'ц", "отца'", "отцу'"], "отцо'м", "The е drops out: отцо'м.", tr="I talked with my father.", lemma="отец"),
        fb("С ___ рожде'ния! (the day)", ["днём", "день", "дня", "дню"], "днём", "The е drops out: днём.", tr="Happy birthday!", lemma="день"),
        fb("Я горжу'сь ___ и па'пой. (mom)", ["ма'мой", "ма'ма", "ма'му", "ма'ме"], "ма'мой", "Hard feminine: -ой.", tr="I am proud of my mom and dad.", lemma="мама"),
        fb("Мы говори'ли с ___. (uncle)", ["дя'дей", "дя'дя", "дя'де", "дя'дю"], "дя'дей", "Дя'дя takes the feminine ending -ей.", tr="We talked with my uncle.", lemma="дядя"),
        fb("Он рабо'тает но'чью и ___. (by day)", ["днём", "день", "дня", "дню"], "днём", "Time of day: днём.", tr="He works at night and by day."),
        mc("What is the instrumental of и'мя?", ["и'менем", "и'мя", "и'мени", "и'мей"], "и'менем", "Add -ен- and -ем.", lemma="имя"),
        mc("Which of these nouns loses the vowel е in the instrumental?", ["оте'ц", "мать", "ночь", "папа"], "оте'ц", "Отцо'м."),
    ],
)

# ---------------------------------------------------------------------------- 146
L146 = lesson(
    "Pronouns in the instrumental: со мной, с ним",
    "Пойдём со мной! Я иду' с ни'ми.",
    requires=["я", "ты", "мы", "они", "кто"],
    cards=[
        card("The instrumental of pronouns",
             "The personal pronouns are мной, тобо'й, им, ей, на'ми, ва'ми and и'ми, and the questions are кем? "
             "and чем? After a preposition the third-person forms add н-: с ним, с ней, с ни'ми. С becomes со "
             "before мной: Он лю'бит разгова'ривать со мной.",
             tables=[table(
                 ["Nominative", "Instrumental", "With с"],
                 [["я", "мной", "со мной"],
                  ["ты", "тобо'й", "с тобо'й"],
                  ["он, оно'", "(н)им", "с ним"],
                  ["она'", "(н)ей", "с ней"],
                  ["мы", "на'ми", "с на'ми"],
                  ["вы", "ва'ми", "с ва'ми"],
                  ["они'", "(н)и'ми", "с ни'ми"],
                  ["кто", "кем", "с кем"],
                  ["что", "чем", "с чем"]])],
             examples=[
                 ex("Мне ну'жно поговори'ть с тобо'й.", "I need to talk with you.", "с тобо'й"),
                 ex("Он лю'бит разгова'ривать со мной.", "He likes talking with me.", "со мной"),
                 ex("Я иду' с ним.", "I am going with him.", "с ним"),
                 ex("Я иду' с ни'ми.", "I am going with them.", "с ни'ми"),
                 ex("С кем ты идёшь в кино'?", "Who are you going to the cinema with?", "С кем"),
             ]),
    ],
    verify=(vf("я", "мной") + vf("ты", "тобой") + vf("он", "им", "ним") + vf("она", "ей", "ней")
            + vf("мы", "нами") + vf("вы", "вами") + vf("они", "ими", "ними") + vf("кто", "кем")
            + vf("что", "чем") + vf("разговаривать", "разговаривать") + vf("любить", "любит")
            + vf("кино", "кино")),
    exercises=[
        fb("Он идёт в парк со ___. (me)", ["мной", "я", "меня'", "мне"], "мной", "Instrumental of я: мной.", tr="He is going to the park with me.", lemma="я"),
        fb("Я хочу' поговори'ть с ___. (you, informal)", ["тобо'й", "ты", "тебя'", "тебе'"], "тобо'й", "Instrumental of ты: тобо'й.", tr="I want to talk with you.", lemma="ты"),
        fb("Я иду' с ___. (him)", ["ним", "им", "его'", "нему'"], "ним", "After a preposition: н-.", tr="I am going with him.", lemma="он"),
        fb("Я иду' с ___. (her)", ["ней", "ей", "её", "она'"], "ней", "After a preposition: н-.", tr="I am going with her.", lemma="она"),
        fb("Мы идём с ___. (them)", ["ни'ми", "и'ми", "их", "ним"], "ни'ми", "After a preposition: ни'ми.", tr="We are going with them.", lemma="они"),
        fb("Они' идут с ___. (us)", ["на'ми", "нам", "нас", "мы"], "на'ми", "Instrumental of мы: на'ми.", tr="They are going with us.", lemma="мы"),
        fb("С ___ ты идёшь в кино'? (whom)", ["кем", "кто", "кого'", "кому'"], "кем", "Instrumental of кто: кем.", tr="Who are you going to the cinema with?", lemma="кто"),
        mc("Which means “with me”?", ["со мной", "с мной", "с мне", "с меня'"], "со мной", "Со + мной."),
        mc("Which means “with them”?", ["с ни'ми", "с и'ми", "с их", "с ним"], "с ни'ми", "N- is added after the preposition."),
    ],
)

# ---------------------------------------------------------------------------- 147
L147 = lesson(
    "Adjectives in the instrumental: с но́вым другом",
    "Я говорю' с но'вым студе'нтом.",
    requires=["новый", "хороший", "русский", "большой", "этот"],
    cards=[
        card("Four endings again",
             "Masculine and neuter adjectives take -ым after a hard stem and -им after a soft stem or after к, г, х, "
             "ж, ш, ч, щ. Feminine adjectives take -ой after a hard stem and -ей after a soft stem or after ж, ш, ч, щ "
             "when unstressed.",
             tables=[table(
                 ["Masculine", "Instrumental (m, n)", "Feminine", "Instrumental (f)"],
                 [["но'вый", "но'в{ым}", "но'вая", "но'в{ой}"],
                  ["си'ний", "си'н{им}", "си'няя", "си'н{ей}"],
                  ["ру'сский", "ру'сск{им}", "ру'сская", "ру'сск{ой}"],
                  ["хоро'ший", "хоро'ш{им}", "хоро'шая", "хоро'ш{ей}"],
                  ["большо'й", "больш{и'м}", "больша'я", "больш{о'й}"],
                  ["пе'рвый", "пе'рв{ым}", "пе'рвая", "пе'рв{ой}"],
                  ["тре'тий", "тре'ть{им}", "тре'тья", "тре'ть{ей}"]])]),
        card("Pronouns that behave like adjectives",
             "Question words, demonstratives, possessives, весь and оди'н use the same endings.",
             tables=[table(
                 ["Nominative", "Masculine, neuter", "Feminine"],
                 [["како'й", "каки'м", "како'й"],
                  ["чей", "чьим", "чьей"],
                  ["э'тот", "э'тим", "э'той"],
                  ["тот", "тем", "той"],
                  ["мой", "мои'м", "мое'й"],
                  ["наш", "на'шим", "на'шей"],
                  ["весь", "всем", "всей"],
                  ["оди'н", "одни'м", "одно'й"]])],
             examples=[
                 ex("Я говорю' с но'вым студе'нтом.", "I am talking with the new student.", "с но'вым студе'нтом"),
                 ex("Я живу' с мое'й сестро'й.", "I live with my sister.", "с мое'й сестро'й"),
                 ex("Я интересу'юсь той но'вой кни'гой.", "I am interested in that new book.", "той но'вой кни'гой"),
                 ex("Я горжу'сь ва'шим сы'ном.", "I am proud of your son.", "ва'шим сы'ном"),
                 ex("Я занима'юсь ру'сским языко'м с э'тим преподава'телем.", "I study Russian with this teacher.", "с э'тим преподава'телем"),
             ]),
    ],
    verify=(vf("новый", "новым", "новой") + vf("синий", "синим", "синей") + vf("русский", "русским", "русской")
            + vf("хороший", "хорошим", "хорошей") + vf("большой", "большим", "большой") + vf("первый", "первым", "первой")
            + vf("третий", "третьим", "третьей") + vf("какой", "каким") + vf("чей", "чьим", "чьей")
            + vf("этот", "этим", "этой") + vf("тот", "тем", "той") + vf("мой", "моим", "моей")
            + vf("наш", "нашим", "нашей") + vf("ваш", "вашим") + vf("весь", "всем", "всей")
            + vf("один", "одним", "одной") + vf("студент", "студентом") + vf("язык", "языком")
            + vf("сын", "сыном") + vf("книга", "книгой") + vf("гордиться", "горжусь")),
    exercises=[
        fb("Я говорю' с ___ студе'нтом. (new)", ["но'вым", "но'вый", "но'вого", "но'вому"], "но'вым", "Masculine hard: -ым.", tr="I am talking with the new student.", lemma="новый"),
        fb("Она' идёт с ___ подру'гой. (good)", ["хоро'шей", "хоро'шая", "хоро'шую", "хоро'шим"], "хоро'шей", "Feminine after ш: -ей.", tr="She is walking with a good friend.", lemma="хороший"),
        fb("Он рабо'тает с ___ врачо'м. (this)", ["э'тим", "э'тот", "э'того", "э'тому"], "э'тим", "Masculine: э'тим.", tr="He works with this doctor.", lemma="этот"),
        fb("Я живу' с ___ сестро'й. (my)", ["мое'й", "моя'", "мою'", "мои'м"], "мое'й", "Feminine: мое'й.", tr="I live with my sister.", lemma="мой"),
        fb("Я интересу'юсь ___ кни'гой. (that)", ["той", "та", "ту", "тем"], "той", "Feminine: той.", tr="I am interested in that book.", lemma="тот"),
        fb("Я горжу'сь ___ сы'ном. (your, formal)", ["ва'шим", "ваш", "ва'шего", "ва'шей"], "ва'шим", "Masculine: ва'шим.", tr="I am proud of your son.", lemma="ваш"),
        fb("С ___ студе'нтом вы разгова'ривали? (which)", ["каки'м", "како'й", "како'го", "како'му"], "каки'м", "Masculine: каки'м.", tr="Which student did you talk with?", lemma="какой"),
        mc("Which ending do hard-stem feminine adjectives take in the instrumental?", ["-ой", "-ым", "-ей", "-им"], "-ой", "Но'вой.", order=True),
        mc("Which means “with the Russian teacher” (male)?",
           ["с ру'сским учи'телем", "с ру'сский учи'тель", "с ру'сского учи'теля", "с ру'сскому учи'телю"],
           "с ру'сским учи'телем", "Masculine instrumental: -им, -ем."),
    ],
)

# ---------------------------------------------------------------------------- 148
L148 = lesson(
    "A house with a garden: с for features and manner",
    "Ко'фе с молоко'м. Они' слу'шали с интере'сом.",
    requires=["лицо", "нос", "кофе", "молоко", "сад"],
    cards=[
        card("Describing a thing or a person",
             "С + instrumental also adds a feature: what a thing contains or what a person looks like. Note that "
             "ко'фе never changes. In English the same idea is “with”.",
             examples=[
                 ex("Ко'фе с молоко'м, пожа'луйста.", "Coffee with milk, please.", "с молоко'м"),
                 ex("Э'то дом с са'дом.", "This is a house with a garden.", "с са'дом"),
                 ex("Э'то де'вушка с кру'глым лицо'м.", "This is a girl with a round face.", "с кру'глым лицо'м"),
                 ex("Э'то мужчи'на с больши'м но'сом.", "This is a man with a big nose.", "с больши'м но'сом"),
             ]),
        card("How an action is done",
             "С also tells the feeling or manner in which something is done. English often uses an adverb here.",
             tables=[table(
                 ["Russian", "English"],
                 [["с ра'достью", "happily, with joy"],
                  ["с интере'сом", "with interest"],
                  ["с трудо'м", "with difficulty"],
                  ["с улы'бкой", "with a smile"],
                  ["с любо'вью", "with love"],
                  ["с удово'льствием", "with pleasure"]])],
             examples=[
                 ex("Студе'нты слу'шали с интере'сом.", "The students listened with interest.", "с интере'сом"),
                 ex("Я с трудо'м запомина'ю но'вые слова'.", "I remember new words with difficulty.", "с трудо'м"),
                 ex("Он с ра'достью рассказа'л мне об э'том.", "He happily told me about it.", "с ра'достью"),
                 ex("Она' отве'тила с улы'бкой.", "She answered with a smile.", "с улы'бкой"),
             ]),
    ],
    verify=(vf("молоко", "молоком") + vf("сад", "садом") + vf("лицо", "лицом") + vf("нос", "носом")
            + vf("круглый", "круглым") + vf("большой", "большим") + vf("интерес", "интересом") + vf("труд", "трудом")
            + vf("радость", "радостью") + vf("улыбка", "улыбкой") + vf("любовь", "любовью")
            + vf("удовольствие", "удовольствием") + vf("слушать", "слушали") + vf("запоминать", "запоминаю")
            + vf("рассказать", "рассказал") + vf("ответить", "ответила") + vf("слово", "слова")),
    exercises=[
        fb("Я пью ко'фе с ___. (milk)", ["молоко'м", "молоко'", "молока'", "молоку'"], "молоко'м", "Neuter hard: -ом.", tr="I drink coffee with milk.", lemma="молоко"),
        fb("Э'то дом с ___. (garden)", ["са'дом", "сад", "са'да", "са'ду"], "са'дом", "Masculine hard: -ом.", tr="This is a house with a garden.", lemma="сад"),
        fb("Э'то де'вушка с кру'глым ___. (face)", ["лицо'м", "лицо'", "лица'", "лицу'"], "лицо'м", "Neuter: лицо'м.", tr="This is a girl with a round face.", lemma="лицо"),
        fb("Студе'нты слу'шали с ___. (interest)", ["интере'сом", "интере'с", "интере'са", "интере'су"], "интере'сом", "Manner: с + instrumental.", tr="The students listened with interest.", lemma="интерес"),
        fb("Я с ___ запомина'ю слова'. (difficulty)", ["трудо'м", "труд", "труда'", "труду'"], "трудо'м", "С трудо'м means “with difficulty”.", tr="I remember words with difficulty.", lemma="труд"),
        fb("Он отве'тил с ___. (joy)", ["ра'достью", "ра'дость", "ра'дости"], "ра'достью", "Feminine in -ь: -ью.", tr="He answered with joy.", lemma="радость"),
        fb("Она' посмотре'ла на меня' с ___. (a smile)", ["улы'бкой", "улы'бка", "улы'бку", "улы'бке"], "улы'бкой", "Feminine hard: -ой.", tr="She looked at me with a smile.", lemma="улыбка"),
        mc("Which means “a man with a big nose”?",
           ["мужчи'на с больши'м но'сом", "мужчи'на с большо'й нос", "мужчи'на с большо'го но'са", "мужчи'на с большо'му но'су"],
           "мужчи'на с больши'м но'сом", "Masculine instrumental: -им, -ом."),
        mc("In с интере'сом, which case follows с?", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "With a meaning “with”, с takes the instrumental (with the meaning “from”, the genitive).", order=True),
    ],
)

# ---------------------------------------------------------------------------- 149
L149 = lesson(
    "Who do you work as? быть, работать, стать + instrumental",
    "Она' рабо'тает учи'тельницей. Я хочу' стать врачо'м.",
    requires=["работать", "стать", "врач", "журналист", "инженер"],
    cards=[
        card("A job or role after быть, работать, стать",
             "After быть (past and future), работать (to work as) and стать (to become), the name of a job or "
             "role goes in the instrumental. The questions are Кем? and Каки'м? Кем она' рабо'тает? — Она' "
             "рабо'тает учи'тельницей.",
             tables=[table(
                 ["Nominative", "Instrumental"],
                 [["врач", "врач{ом}"],
                  ["учи'тель", "учи'тел{ем}"],
                  ["журнали'ст", "журнали'ст{ом}"],
                  ["инжене'р", "инжене'р{ом}"],
                  ["учи'тельница", "учи'тельниц{ей}"],
                  ["медсестра'", "медсестр{о'й}"],
                  ["тре'нер", "тре'нер{ом}"],
                  ["балери'на", "балери'н{ой}"]])],
             examples=[
                 ex("Кем она' рабо'тает? — Она' рабо'тает учи'тельницей.", "What does she work as? — As a teacher.", "учи'тельницей"),
                 ex("Мой оте'ц был врачо'м.", "My father was a doctor.", "врачо'м"),
                 ex("Я хочу' быть инжене'ром.", "I want to be an engineer.", "инжене'ром"),
                 ex("Она' хо'чет стать журнали'стом.", "She wants to become a journalist.", "журнали'стом"),
             ]),
        card("But not in the present tense",
             "Russian leaves out “am, is, are”. Without a form of быть the noun stays in the nominative. Compare "
             "Раньше оте'ц был врачо'м and Оте'ц — врач. Or Я хочу' быть космонавтом and Я космона'вт.",
             tables=[table(
                 ["Present, no быть", "Past or future, with быть"],
                 [["Оте'ц — врач.", "Оте'ц был врачо'м."],
                  ["Она' — тре'нер.", "Она' бу'дет тре'нером."],
                  ["Я — журнали'ст.", "Я ста'ну журнали'стом."]])]),
    ],
    verify=(vf("врач", "врачом") + vf("учитель", "учителем") + vf("журналист", "журналистом") + vf("инженер", "инженером")
            + vf("медсестра", "медсестрой") + vf("тренер", "тренером")
            + vf("балерина", "балериной") + vf("космонавт", "космонавтом") + vf("быть", "был", "была", "будет")
            + vf("стать", "стану") + vf("работать", "работает") + vf("хотеть", "хочет", "хочу")),
    exercises=[
        fb("Кем она' рабо'тает? — Она' рабо'тает ___.", ["учи'тельницей", "учи'тельница", "учи'тельницу", "учи'тельнице"], "учи'тельницей", "Работать takes the instrumental.", tr="What does she work as? — As a teacher."),
        fb("Мой оте'ц был ___. (doctor)", ["врачо'м", "врач", "врача'", "врачу'"], "врачо'м", "Past tense of быть: instrumental.", tr="My father was a doctor.", lemma="врач"),
        fb("Мой оте'ц — ___. (doctor)", ["врач", "врачо'м", "врача'", "врачу'"], "врач", "No быть in the present: nominative.", tr="My father is a doctor.", lemma="врач"),
        fb("Я хочу' быть ___. (engineer)", ["инжене'ром", "инжене'р", "инжене'ра", "инжене'ру"], "инжене'ром", "After быть in the infinitive: instrumental.", tr="I want to be an engineer.", lemma="инженер"),
        fb("Она' хо'чет стать ___. (journalist)", ["журнали'стом", "журнали'ст", "журнали'ста", "журнали'сту"], "журнали'стом", "Стать takes the instrumental.", tr="She wants to become a journalist.", lemma="журналист"),
        fb("Ра'ньше она' была' ___. (nurse)", ["медсестро'й", "медсестра'", "медсестру'", "медсестре'"], "медсестро'й", "Past tense of быть: instrumental.", tr="She used to be a nurse.", lemma="медсестра"),
        fb("За'втра он бу'дет ___. (the director)", ["дире'ктором", "дире'ктор", "дире'ктора", "дире'ктору"], "дире'ктором", "Future of быть: instrumental.", tr="Tomorrow he will be the director.", lemma="директор"),
        mc("Why is врач in the nominative in Он — врач?",
           ["The verb быть is left out in the present tense", "Because врач is a short word", "Because он is masculine", "Because it follows a preposition"],
           "The verb быть is left out in the present tense", "No быть, no instrumental."),
        mc("Which means “She was a teacher”?",
           ["Она' была' учи'тельницей.", "Она' была' учи'тельница.", "Она' была' учи'тельницу.", "Она' была' учи'тельнице."],
           "Она' была' учи'тельницей.", "Past tense: instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 150
L150 = lesson(
    "Interests and sports: заниматься, интересоваться",
    "Я занима'юсь футбо'лом. Я интересу'юсь му'зыкой.",
    requires=["заниматься", "интересоваться", "спорт", "музыка", "футбол"],
    cards=[
        card("Verbs that take the instrumental",
             "Some verbs always take the instrumental for the thing you do, enjoy or use. Learn them as a set: "
             "занима'ться (to be busy with, to practise), интересова'ться (to be interested in), горди'ться "
             "(to be proud of) and по'льзоваться (to use).",
             tables=[table(
                 ["Verb", "я", "Example"],
                 [["занима'ться", "занима'юсь", "Я занима'юсь спо'ртом."],
                  ["интересова'ться", "интересу'юсь", "Я интересу'юсь му'зыкой."],
                  ["горди'ться", "горжу'сь", "Я горжу'сь сы'ном."],
                  ["по'льзоваться", "по'льзуюсь", "Я по'льзуюсь словарём."]])],
             examples=[
                 ex("Чем вы занима'етесь в свобо'дное вре'мя?", "What do you do in your free time?", "Чем"),
                 ex("Каки'м ви'дом спо'рта вы занима'етесь? — Я занима'юсь футбо'лом.", "Which sport do you practise? — I play soccer.", "футбо'лом"),
                 ex("Чем вы интересу'етесь? — Я интересу'юсь фотогра'фией.", "What are you interested in? — Photography.", "фотогра'фией"),
             ]),
        card("Sports and hobbies",
             "Compare игра'ть в + accusative with занима'ться + instrumental: игра'ть в футбо'л and занима'ться "
             "футбо'лом mean almost the same. Nouns in -ия take -ией: фотогра'фия, фотогра'фией.",
             tables=[table(
                 ["Nominative", "Instrumental"],
                 [["футбо'л", "футбо'л{ом}"],
                  ["те'ннис", "те'ннис{ом}"],
                  ["спорт", "спорт{ом}"],
                  ["му'зыка", "му'зык{ой}"],
                  ["литерату'ра", "литерату'р{ой}"],
                  ["фотогра'фия", "фотогра'ф{ией}"]])]),
    ],
    verify=(vf("заниматься", "занимаюсь", "занимаетесь") + vf("интересоваться", "интересуюсь", "интересуется", "интересуетесь")
            + vf("гордиться", "горжусь") + vf("пользоваться", "пользуюсь", "пользуется") + vf("футбол", "футболом")
            + vf("теннис", "теннисом") + vf("спорт", "спортом") + vf("музыка", "музыкой") + vf("литература", "литературой")
            + vf("фотография", "фотографией") + vf("словарь", "словарём") + vf("брат", "братом") + vf("сын", "сыном")),
    exercises=[
        fb("Я занима'юсь ___. (soccer)", ["футбо'лом", "футбо'л", "футбо'ла", "футбо'ле"], "футбо'лом", "Занима'ться takes the instrumental.", tr="I play soccer.", lemma="футбол"),
        fb("Он интересу'ется ___. (music)", ["му'зыкой", "му'зыка", "му'зыку", "му'зыке"], "му'зыкой", "Интересова'ться takes the instrumental.", tr="He is interested in music.", lemma="музыка"),
        fb("Мы интересу'емся ___. (photography)", ["фотогра'фией", "фотогра'фия", "фотогра'фию", "фотогра'фии"], "фотогра'фией", "Nouns in -ия take -ией.", tr="We are interested in photography.", lemma="фотография"),
        fb("Чем вы ___ в свобо'дное вре'мя?", ["занима'етесь", "занима'ется", "занима'юсь", "занима'ются"], "занима'етесь", "Вы goes with занима'етесь.", tr="What do you do in your free time?", lemma="заниматься"),
        fb("Она' по'льзуется ___. (a dictionary)", ["словарём", "словарь", "словаря'", "словарю'"], "словарём", "По'льзоваться takes the instrumental.", tr="She uses a dictionary.", lemma="словарь"),
        fb("Я горжу'сь ___. (my brother)", ["бра'том", "брат", "бра'та", "бра'ту"], "бра'том", "Горди'ться takes the instrumental.", tr="I am proud of my brother.", lemma="брат"),
        fb("Мой друг занима'ется ___. (tennis)", ["те'ннисом", "те'ннис", "те'нниса", "те'ннису"], "те'ннисом", "Занима'ться takes the instrumental.", tr="My friend plays tennis.", lemma="теннис"),
        mc("Which case do заниматься and интересоваться take?", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "The instrumental.", order=True),
        mc("Which sentence is right?", ["Я занима'юсь футбо'лом.", "Я занима'юсь футбо'л.", "Я занима'юсь в футбо'л.", "Я занима'юсь футбо'ла."], "Я занима'юсь футбо'лом.", "Занима'ться + instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 151
L151 = lesson(
    "By hand, with a pen: the instrumental of means; times of day",
    "Я пишу' ру'чкой. У'тром я пью ко'фе.",
    requires=["ручка", "нож", "утро", "зима", "лето"],
    cards=[
        card("With what? Чем?",
             "Russian uses no preposition to say what you do something with. The tool simply goes in the "
             "instrumental: Чем ты пи'шешь? — Я пишу' ру'чкой.",
             tables=[table(
                 ["Nominative", "Instrumental", "Phrase"],
                 [["ру'чка", "ру'чк{ой}", "писа'ть ру'чкой"],
                  ["карандаш", "карандаш{о'м}", "писа'ть карандашо'м"],
                  ["ло'жка", "ло'жк{ой}", "есть суп ло'жкой"],
                  ["ви'лка", "ви'лк{ой}", "есть сала'т ви'лкой"],
                  ["нож", "нож{о'м}", "ре'зать хлеб ножо'м"],
                  ["мы'ло", "мы'л{ом}", "мыть ру'ки мы'лом"],
                  ["полоте'нце", "полоте'нц{ем}", "вытира'ть ру'ки полоте'нцем"]])],
             examples=[
                 ex("Обы'чно я пишу' карандашо'м.", "Usually I write with a pencil.", "карандашо'м"),
                 ex("Он ест суп ло'жкой.", "He eats soup with a spoon.", "ло'жкой"),
                 ex("Она' ре'жет хлеб ножо'м.", "She cuts the bread with a knife.", "ножо'м"),
             ]),
        card("Times of day and seasons",
             "The instrumental also answers “when?” for times of day and seasons. Use these as ready-made words.",
             tables=[table(
                 ["Russian", "English"],
                 [["у'тром", "in the morning"],
                  ["днём", "in the daytime"],
                  ["ве'чером", "in the evening"],
                  ["но'чью", "at night"],
                  ["весно'й", "in spring"],
                  ["ле'том", "in summer"],
                  ["о'сенью", "in autumn"],
                  ["зимо'й", "in winter"]])],
             examples=[
                 ex("У'тром я пью ко'фе.", "In the morning I drink coffee.", "У'тром"),
                 ex("Ле'том мы е'здим на мо'ре.", "In summer we go to the seaside.", "Ле'том"),
                 ex("Зимо'й здесь о'чень хо'лодно.", "In winter it is very cold here.", "Зимо'й"),
             ]),
    ],
    verify=(vf("ручка", "ручкой") + vf("карандаш", "карандашом") + vf("ложка", "ложкой") + vf("вилка", "вилкой")
            + vf("нож", "ножом") + vf("мыло", "мылом") + vf("полотенце", "полотенцем") + vf("утро", "утром")
            + vf("день", "днём") + vf("вечер", "вечером") + vf("ночь", "ночью") + vf("весна", "весной")
            + vf("лето", "летом") + vf("осень", "осенью") + vf("зима", "зимой") + vf("писать", "пишешь", "пишу")
            + vf("резать", "режет") + vf("есть", "ест") + vf("пить", "пью") + vf("мыть", "мыть") + vf("вытирать", "вытирать")),
    exercises=[
        fb("Я пишу' ___. (with a pen)", ["ру'чкой", "ру'чка", "ру'чку", "ру'чке"], "ру'чкой", "The tool goes in the instrumental.", tr="I write with a pen.", lemma="ручка"),
        fb("Он ест суп ___. (with a spoon)", ["ло'жкой", "ло'жка", "ло'жку", "ло'жке"], "ло'жкой", "The tool goes in the instrumental.", tr="He eats soup with a spoon.", lemma="ложка"),
        fb("Она' ре'жет хлеб ___. (with a knife)", ["ножо'м", "нож", "но'жа", "ножу'"], "ножо'м", "Stressed ending: -о'м.", tr="She cuts bread with a knife.", lemma="нож"),
        fb("Обы'чно я пишу' ___. (with a pencil)", ["карандашо'м", "карандаш", "карандаша'", "карандашу'"], "карандашо'м", "Stressed ending: -о'м.", tr="Usually I write with a pencil.", lemma="карандаш"),
        fb("___ я пью ко'фе. (in the morning)", ["У'тром", "У'тро", "У'тра", "У'тру"], "У'тром", "Time of day: instrumental.", tr="In the morning I drink coffee.", lemma="утро"),
        fb("___ здесь о'чень хо'лодно. (in winter)", ["Зимо'й", "Зима'", "Зи'му", "Зиме'"], "Зимо'й", "Season: instrumental.", tr="In winter it is very cold here.", lemma="зима"),
        fb("___ мы е'здим на мо'ре. (in summer)", ["Ле'том", "Ле'то", "Ле'та", "Ле'ту"], "Ле'том", "Season: instrumental.", tr="In summer we go to the seaside.", lemma="лето"),
        mc("Which means “at night”?", ["но'чью", "ночь", "но'чи"], "но'чью", "Time of day: instrumental."),
        mc("Which means “in the evening”?", ["ве'чером", "ве'чер", "ве'чера", "ве'черу"], "ве'чером", "Time of day: instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 152
L152 = lesson(
    "Family and wedding: внук, племянник, жениться",
    "Он жени'лся на Ни'не. Она' вы'шла за'муж за Анто'на.",
    requires=["свадьба", "жених", "невеста", "внук", "родственник"],
    cards=[
        card("Relatives",
             "Besides родственник (a relative), you need the words for the next and previous generations.",
             tables=[table(
                 ["Russian", "English"],
                 [["внук, вну'чка", "grandson, granddaughter"],
                  ["племя'нник, племя'нница", "nephew, niece"],
                  ["двою'родный брат", "cousin (male)"],
                  ["двою'родная сестра'", "cousin (female)"],
                  ["ро'дственник, ро'дственница", "relative (m, f)"]])],
             examples=[
                 ex("У меня' есть двою'родный брат.", "I have a cousin.", "двою'родный брат"),
                 ex("Мой племя'нник игра'ет в футбо'л.", "My nephew plays soccer.", "племя'нник"),
             ]),
        card("Weddings: who marries whom",
             "A man uses жени'ться на + prepositional, a woman выхо'дит за'муж за + accusative. To say that someone is "
             "married, use жена'т на + prepositional for a man and за'мужем за + instrumental for a woman. "
             "A couple пожени'лись. The words you need: сва'дьба, жени'х, неве'ста, разво'д.",
             tables=[table(
                 ["Who", "Phrase"],
                 [["Man marries", "Он жени'лся на Ни'не."],
                  ["Woman marries", "Она' вы'шла за'муж за Анто'на."],
                  ["Married man", "Он жена'т на Ни'не."],
                  ["Married woman", "Она' за'мужем за Анто'ном."],
                  ["Couple", "Они' пожени'лись."]])],
             examples=[
                 ex("Ско'ро их сва'дьба.", "Their wedding is soon.", "сва'дьба"),
                 ex("На сва'дьбе жени'х и неве'ста о'чень счастли'вы.", "At the wedding the groom and bride are very happy.", "жени'х и неве'ста"),
             ]),
    ],
    verify=(vf("внук", "внуки") + vf("родственник", "родственник") + vf("жених", "жених") + vf("невеста", "невеста")
            + vf("свадьба", "свадьбе") + vf("развод", "развод") + vf("жениться", "женился") + vf("пожениться", "поженились")
            + vf("выйти", "вышла") + vf("женатый", "женат") + vf("играть", "играет") + vf("счастливый", "счастливы")),
    exercises=[
        fb("Он жени'лся ___ Ни'не. (on)", ["на", "за", "с", "к"], "на", "Жени'ться на + prepositional.", tr="He married Nina."),
        fb("Она' вы'шла за'муж ___ Анто'на. (for)", ["за", "на", "с", "к"], "за", "Выйти за'муж за + accusative.", tr="She married Anton."),
        fb("Она' за'мужем за ___. (Anton)", ["Анто'ном", "Анто'н", "Анто'на", "Анто'ну"], "Анто'ном", "За'мужем за + instrumental.", tr="She is married to Anton."),
        fb("Сын мое'й сестры' — мой ___. (nephew)", ["племя'нник", "внук", "сын", "друг"], "племя'нник", "Nephew: племя'нник.", tr="My sister's son is my nephew."),
        fb("Сын моего' сы'на — мой ___. (grandson)", ["внук", "племя'нник", "дя'дя", "оте'ц"], "внук", "Grandson: внук.", tr="My son's son is my grandson."),
        fb("Мой ___ брат живёт в друго'м го'роде. (cousin)", ["двою'родный", "стро'гий", "ску'чный", "у'мный"], "двою'родный", "Cousin: двою'родный брат.", tr="My cousin lives in another city."),
        fb("На сва'дьбе жени'х и ___. (bride)", ["неве'ста", "неве'сту", "неве'сте", "неве'сты"], "неве'ста", "Nominative: неве'ста.", tr="At the wedding: the groom and the bride.", lemma="невеста"),
        mc("Which word means “divorce”?", ["разво'д", "сва'дьба", "жени'х", "пода'рок"], "разво'д", "Разво'д."),
        mc("Which means “She married Anton”?",
           ["Она' вы'шла за'муж за Анто'на.", "Она' вы'шла за'муж на Анто'не.", "Она' вы'шла за'муж с Анто'ном.", "Она' вы'шла за'муж к Анто'ну."],
           "Она' вы'шла за'муж за Анто'на.", "Выйти за'муж за + accusative."),
    ],
)

# ---------------------------------------------------------------------------- 153
L153 = lesson(
    "Must, can, know how: должен, мочь, уметь",
    "Он до'лжен э'то знать. Я не смогу' вы'играть.",
    requires=["мочь", "уметь", "знать", "работать", "завтра"],
    cards=[
        card("До'лжен has four forms",
             "До'лжен means must or supposed to, and it agrees with the subject like a short adjective. It is "
             "followed by an infinitive, as are мочь, смочь, уме'ть and суме'ть.",
             tables=[table(
                 ["Subject", "Form", "Example"],
                 [["я, ты, он", "до'лжен", "Он до'лжен рабо'тать."],
                  ["я, ты, она'", "должна'", "Она' должна' рабо'тать."],
                  ["оно'", "должно'", "Э'то должно' быть тут."],
                  ["мы, вы, они'", "должны'", "Мы должны' рабо'тать."]])]),
        card("Past and future with быть",
             "Put the form of быть after до'лжен: in the past was or were, in the future the matching form of "
             "бу'ду. Compare Он до'лжен был рабо'тать and За'втра я должна' бу'ду рабо'тать.",
             tables=[table(
                 ["Past", "Future"],
                 [["я до'лжен был, должна' была'", "я до'лжен бу'ду, должна' бу'ду"],
                  ["он до'лжен был", "он до'лжен бу'дет"],
                  ["она' должна' была'", "она' должна' бу'дет"],
                  ["мы должны' бы'ли", "мы должны' бу'дем"]])],
             examples=[
                 ex("Вчера' мы должны' бы'ли рабо'тать.", "Yesterday we had to work.", "должны' бы'ли"),
                 ex("За'втра я должна' бу'ду рабо'тать.", "Tomorrow I will have to work.", "должна' бу'ду"),
             ]),
        card("Can and know how",
             "Мочь means can (circumstances allow it) and уме'ть means can (you have the skill). Смочь and "
             "суме'ть are the perfective forms: they mean to manage to.",
             examples=[
                 ex("Он уме'ет пла'вать.", "He knows how to swim.", "уме'ет"),
                 ex("Он не мо'жет говори'ть гро'мко: у него' боли'т го'рло.", "He cannot speak loudly: his throat hurts.", "не мо'жет"),
                 ex("Я не смогу' вы'играть э'ту па'ртию.", "I will not be able to win this game.", "не смогу'"),
                 ex("Он до'лжен э'то знать.", "He must know this.", "до'лжен"),
             ]),
    ],
    verify=(vf("мочь", "могу", "может", "могут") + vf("смочь", "смогу") + vf("уметь", "умею", "умеет")
            + vf("плавать", "плавать") + vf("выиграть", "выиграть") + vf("быть", "был", "была", "были", "буду", "будет", "будем")
            + vf("знать", "знать") + vf("болеть", "болит") + vf("горло", "горло") + vf("партия", "партию")
            + vf("работать", "работать") + vf("громко", "громко")),
    exercises=[
        fb("Она' ___ рабо'тать сего'дня.", ["должна'", "до'лжен", "должно'", "должны'"], "должна'", "Feminine: должна'.", tr="She must work today."),
        fb("Мы ___ бы'ли рабо'тать вчера'.", ["должны'", "до'лжен", "должна'", "должно'"], "должны'", "Plural: должны'.", tr="We had to work yesterday."),
        fb("Вчера' он до'лжен ___ рабо'тать.", ["был", "бу'дет", "бы'ло", "была'"], "был", "Past, masculine: был.", tr="Yesterday he had to work."),
        fb("За'втра я до'лжен ___ рабо'тать.", ["бу'ду", "бу'дет", "был", "есть"], "бу'ду", "Future, I: бу'ду.", tr="Tomorrow I will have to work."),
        fb("Он не ___ говори'ть гро'мко: у него' боли'т го'рло.", ["мо'жет", "могу'", "мо'гут", "смог"], "мо'жет", "Third person present: мо'жет.", tr="He cannot speak loudly: his throat hurts.", lemma="мочь"),
        fb("Я пло'хо ___ игра'ть в ша'хматы. (know how)", ["уме'ю", "могу'", "до'лжен", "смогу'"], "уме'ю", "Skill: уме'ть.", tr="I don't know how to play chess well.", lemma="уметь"),
        fb("Я не ___ вы'играть э'ту па'ртию. (will be able to)", ["смогу'", "смог", "смогла'", "смо'жешь"], "смогу'", "Future perfective, I: смогу'.", tr="I will not be able to win this game.", lemma="смочь"),
        mc("What form follows до'лжен?", ["an infinitive", "an instrumental noun", "a past tense verb", "a dative noun"], "an infinitive", "До'лжен + infinitive.", order=True),
        mc("Which means “She had to work”?",
           ["Она' должна' была' рабо'тать.", "Она' до'лжен был рабо'тать.", "Она' должна' бу'дет рабо'тать.", "Она' должно' бы'ло рабо'тать."],
           "Она' должна' была' рабо'тать.", "Должна' + была'."),
    ],
)

# ---------------------------------------------------------------------------- 154
L154 = lesson(
    "Review: the instrumental case",
    "Я иду' с дру'гом. Она' рабо'тает врачо'м.",
    requires=["друг", "сестра", "работать", "утро", "ручка"],
    cards=[
        card("Where the instrumental is used",
             "The instrumental answers Кем? and Чем? Remember the main jobs it does.",
             tables=[table(
                 ["Use", "Example"],
                 [["с = together with", "Я иду' с дру'гом."],
                  ["с = feature or manner", "Ко'фе с молоко'м. Она' рабо'тает с интере'сом."],
                  ["Job or role", "Она' рабо'тает врачо'м."],
                  ["Interests", "Я интересу'юсь му'зыкой."],
                  ["Tool", "Я пишу' ру'чкой."],
                  ["Time of day", "У'тром я пью ко'фе."]])]),
        card("Endings at a glance",
             "Nouns, adjectives and pronouns each have a short set of endings.",
             tables=[table(
                 ["Gender", "Noun", "Adjective"],
                 [["Masculine, neuter", "-ом / -ем (-ём)", "-ым / -им"],
                  ["Feminine", "-ой / -ей (-ёй) / -ью", "-ой / -ей"]])],
             examples=[
                 ex("Я говорю' с но'вым дру'гом.", "I am talking with a new friend.", "с но'вым дру'гом"),
                 ex("Я иду' с ней.", "I am going with her.", "с ней"),
             ]),
    ],
    verify=(vf("друг", "другом") + vf("новый", "новым") + vf("врач", "врачом") + vf("музыка", "музыкой")
            + vf("ручка", "ручкой") + vf("утро", "утром") + vf("молоко", "молоком") + vf("работать", "работает")
            + vf("интересоваться", "интересуюсь")),
    exercises=[
        fb("Я иду' в кино' с ___. (my sister)", ["мое'й сестро'й", "моя' сестра'", "мою' сестру'", "мое'й сестре'"], "мое'й сестро'й", "Instrumental feminine.", tr="I am going to the cinema with my sister."),
        fb("Она' рабо'тает ___. (doctor)", ["врачо'м", "врач", "врача'", "врачу'"], "врачо'м", "Работать takes the instrumental.", tr="She works as a doctor.", lemma="врач"),
        fb("Я интересу'юсь ___. (music)", ["му'зыкой", "му'зыка", "му'зыку", "му'зыке"], "му'зыкой", "Интересова'ться takes the instrumental.", tr="I am interested in music.", lemma="музыка"),
        fb("Я пишу' ___. (with a pen)", ["ру'чкой", "ру'чка", "ру'чку", "ру'чке"], "ру'чкой", "Tool: instrumental.", tr="I write with a pen.", lemma="ручка"),
        fb("___ я пью ко'фе. (in the morning)", ["У'тром", "У'тро", "У'тра", "У'тру"], "У'тром", "Time of day: instrumental.", tr="In the morning I drink coffee.", lemma="утро"),
        fb("Он идёт со ___. (me)", ["мной", "я", "меня'", "мне"], "мной", "Instrumental of я.", tr="He is going with me.", lemma="я"),
        fb("Я говорю' с ___ студе'нтом. (this)", ["э'тим", "э'тот", "э'того", "э'тому"], "э'тим", "Masculine instrumental.", tr="I am talking with this student.", lemma="этот"),
        fb("Мой оте'ц — ___. (engineer)", ["инжене'р", "инжене'ром", "инжене'ра", "инжене'ру"], "инжене'р", "No быть in the present: nominative.", tr="My father is an engineer.", lemma="инженер"),
        mc("Which means “coffee with milk”?", ["ко'фе с молоко'м", "ко'фе с молоко'", "ко'фе с молока'", "ко'фе с молоку'"], "ко'фе с молоко'м", "С + instrumental."),
        mc("Which sentence is right?", ["Она' была' врачо'м.", "Она' была' врач.", "Она' была' врача'.", "Она' была' врачу'."], "Она' была' врачо'м.", "After a past form of быть: instrumental."),
    ],
)

UNIT = unit("Unit 17: The instrumental case", [L144, L145, L146, L147, L148, L149, L150, L151, L152, L153, L154])
