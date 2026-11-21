"""Unit 16: the dative case (textbook module 4, lesson 22)."""
from dsl import *

# ---------------------------------------------------------------------------- 133
L133 = lesson(
    "To whom? Nouns in the dative",
    "Я пишу' письмо' дру'гу. Я звоню' ма'ме.",
    requires=["друг", "учитель", "подруга", "тётя", "письмо"],
    cards=[
        card("Кому́? The dative endings",
             "The dative case names the person who receives or benefits from an action: the indirect object. The "
             "question is Кому'? (To whom?). Masculine nouns with a hard consonant and neuter nouns in -о take -у. "
             "Masculine nouns in -й or -ь and neuter nouns in -е take -ю. Feminine nouns in -а and -я take -е. "
             "Feminine nouns in -ия and -ь take -и.",
             tables=[table(
                 ["Nominative", "Dative", "Ending"],
                 [["друг", "дру'г{у}", "-у"],
                  ["окно'", "окн{у'}", "-у"],
                  ["геро'й", "геро'{ю}", "-ю"],
                  ["учи'тель", "учи'тел{ю}", "-ю"],
                  ["зда'ние", "зда'ни{ю}", "-ю"],
                  ["подру'га", "подру'г{е}", "-е"],
                  ["тётя", "тёт{е}", "-е"],
                  ["ста'нция", "ста'нци{и}", "-и"],
                  ["вещь", "ве'щ{и}", "-и"]],
                 note="Masculine nouns in -а and -я take -е: па'па → па'пе, дя'дя → дя'де, Ко'ля → Ко'ле.")]),
        card("Special nouns",
             "Some nouns change their stem. Мать and дочь add -ер-: ма'тери, до'чери. The vowel е drops out of "
             "most nouns in -ец and out of день: отцу', дню. Neuter nouns in -мя drop -я and add -ени: и'мени, "
             "вре'мени.",
             tables=[table(
                 ["Nominative", "Dative"],
                 [["мать", "ма'тери"], ["дочь", "до'чери"], ["оте'ц", "отц{у'}"], ["день", "дн{ю}"],
                  ["и'мя", "и'мени"], ["вре'мя", "вре'мени"]])],
             examples=[
                 ex("Кому' ты пи'шешь письмо'? — Я пишу' письмо' дру'гу.", "To whom are you writing the letter? — To a friend.", "дру'гу"),
                 ex("Я даю' кни'гу ма'тери.", "I am giving a book to my mother.", "ма'тери"),
                 ex("Я даю' кни'гу до'чери.", "I am giving a book to my daughter.", "до'чери"),
                 ex("Я даю' кни'гу отцу'.", "I am giving a book to my father.", "отцу'"),
                 ex("Я звоню' тёте.", "I am calling my aunt.", "тёте"),
             ]),
    ],
    verify=(vf("друг", "другу") + vf("окно", "окну") + vf("герой", "герою") + vf("учитель", "учителю")
            + vf("здание", "зданию") + vf("подруга", "подруге") + vf("тётя", "тёте") + vf("станция", "станции")
            + vf("вещь", "вещи") + vf("папа", "папе") + vf("дядя", "дяде") + vf("мать", "матери")
            + vf("дочь", "дочери") + vf("отец", "отцу") + vf("день", "дню") + vf("имя", "имени")
            + vf("время", "времени") + vf("давать", "даю") + vf("звонить", "звоню") + vf("писать", "пишу", "пишешь")),
    exercises=[
        fb("Я пишу' письмо' ___. (a friend)", ["дру'гу", "друг", "дру'га", "дру'гом"], "дру'гу",
           "Indirect object: dative.", tr="I am writing a letter to a friend.", lemma="друг"),
        fb("Я даю' кни'гу ___. (my mother)", ["ма'тери", "мать", "ма'терью", "ма'ть"], "ма'тери",
           "Мать → ма'тери.", tr="I am giving the book to my mother.", lemma="мать"),
        fb("Я даю' кни'гу ___. (my daughter)", ["до'чери", "дочь", "до'черью", "до'чь"], "до'чери",
           "Дочь → до'чери.", tr="I am giving the book to my daughter.", lemma="дочь"),
        fb("Я пишу' письмо' ___. (the teacher)", ["учи'телю", "учи'тель", "учи'теля", "учи'телем"], "учи'телю",
           "Masculine soft: -ю.", tr="I am writing a letter to the teacher.", lemma="учитель"),
        fb("Я звоню' ___. (my aunt)", ["тёте", "тётя", "тёти", "тётю"], "тёте",
           "Feminine in -я: -е.", tr="I am calling my aunt.", lemma="тётя"),
        fb("Я даю' кни'гу ___. (my father)", ["отцу'", "оте'ц", "отца'", "отцо'м"], "отцу'",
           "The е drops out: отцу'.", tr="I am giving the book to my father.", lemma="отец"),
        fb("Я купи'л э'ту игру'шку ___. (my son)", ["сы'ну", "сын", "сы'на", "сы'ном"], "сы'ну",
           "Masculine hard: -у.", tr="I bought this toy for my son.", lemma="сын"),
        mc("Which ending do masculine nouns in -а (па'па) take in the dative?", ["-е", "-у", "-ю", "-и"], "-е",
           "Па'па → па'пе.", order=True),
        mc("What is the dative of и'мя?", ["и'мени", "и'мя", "и'мю", "и'ме"], "и'мени", "Neuter in -мя: -ени."),
        mc("Which question asks “to whom”?", ["Кому'?", "Кого'?", "Кем?", "О ком?"], "Кому'?", "Кому' = dative."),
    ],
)

# ---------------------------------------------------------------------------- 134
L134 = lesson(
    "Giving, telling, writing: verbs with the dative",
    "Дай мне ру'ку! Скажи' дире'ктору, что я опозда'ю.",
    requires=["давать", "дарить", "сказать", "рассказывать", "подарок"],
    cards=[
        card("Verbs of giving and telling",
             "Many verbs of giving, telling and writing take the person in the dative and the thing in the "
             "accusative. Learn them as pairs of imperfective and perfective.",
             tables=[table(
                 ["Imperfective", "Perfective", "Meaning"],
                 [["дава'ть", "дать", "to give"],
                  ["дари'ть", "подари'ть", "to give as a gift"],
                  ["говори'ть", "сказа'ть", "to say, to tell"],
                  ["расска'зывать", "рассказа'ть", "to tell about"],
                  ["писа'ть", "написа'ть", "to write"],
                  ["чита'ть", "прочита'ть", "to read to someone"]])]),
        card("Forms of дать",
             "Дава'ть is regular (даю', даёшь …), but дать is irregular.",
             tables=[table(
                 ["", "дава'ть", "дать"],
                 [["я", "даю'", "дам"], ["ты", "даёшь", "дашь"], ["он, она'", "даёт", "даст"],
                  ["мы", "даём", "дади'м"], ["вы", "даёте", "дади'те"], ["они'", "даю'т", "даду'т"]],
                 note="Past of дать: дал, дала', да'ло, да'ли.")],
             examples=[
                 ex("Дай мне ру'ку!", "Give me your hand!", "Дай мне"),
                 ex("Ско'ро я подарю' жене' но'вую маши'ну.", "Soon I will give my wife a new car as a gift.", "жене'"),
                 ex("Мать чита'ет до'чери ска'зку.", "The mother is reading a fairy tale to her daughter.", "до'чери"),
                 ex("Скажи' дире'ктору, что я немно'го опозда'ю.", "Tell the director that I will be a little late.", "дире'ктору"),
                 ex("Расскажи' Анто'ну о твое'й пое'здке в Москву'.", "Tell Anton about your trip to Moscow.", "Анто'ну"),
             ]),
        card("Nouns that take the dative",
             "Some nouns also take an indirect object in the dative: ответ дире'ктору (a reply to the director), "
             "письмо' ма'тери (a letter to my mother), пода'рок сы'ну (a gift for my son), посы'лка вну'ку (a parcel "
             "for my grandson), по'мощь подру'ге (help for a friend) and сове'т дру'гу (advice for a friend).",
             tables=[table(
                 ["Noun", "With the dative"],
                 [["отве'т", "отве'т дире'ктору"], ["письмо'", "письмо' ма'тери"], ["пода'рок", "пода'рок сы'ну"],
                  ["посы'лка", "посы'лка вну'ку"], ["по'мощь", "по'мощь подру'ге"], ["сове'т", "сове'т дру'гу"]])]),
    ],
    verify=(vf("давать", "даю", "даёшь", "даёт", "даём", "даёте", "дают") + vf("дать", "дам", "дашь", "даст", "дадим", "дадите", "дадут", "дай")
            + vf("подарить", "подарю") + vf("жена", "жене") + vf("дочь", "дочери") + vf("директор", "директору")
            + vf("сын", "сыну") + vf("внук", "внуку") + vf("подруга", "подруге") + vf("друг", "другу")
            + vf("мать", "матери") + vf("опоздать", "опоздаю") + vf("поездка", "поездке") + vf("читать", "читает")
            + vf("сказка", "сказку")),
    exercises=[
        fb("Я даю' кни'гу ___. (my friend)", ["дру'гу", "друг", "дру'га", "дру'гом"], "дру'гу",
           "Indirect object: dative.", tr="I'm giving the book to my friend.", lemma="друг"),
        fb("Мать чита'ет ___ ска'зку. (her daughter)", ["до'чери", "дочь", "до'черью", "доче'рь"], "до'чери",
           "Indirect object: dative.", tr="The mother is reading a fairy tale to her daughter.", lemma="дочь"),
        fb("Скажи' ___, что я опозда'ю. (the director)", ["дире'ктору", "дире'ктор", "дире'ктора", "дире'ктором"], "дире'ктору",
           "Indirect object: dative.", tr="Tell the director that I will be late.", lemma="директор"),
        fb("Я подарю' ___ но'вую маши'ну. (my wife)", ["жене'", "жена'", "жены'", "жену'"], "жене'",
           "Feminine in -а: -е.", tr="I will give my wife a new car.", lemma="жена"),
        fb("Расскажи' ___ о пое'здке. (Anton)", ["Анто'ну", "Анто'н", "Анто'на", "Анто'ном"], "Анто'ну",
           "Indirect object: dative.", tr="Tell Anton about the trip."),
        fb("___ мне ру'ку!", ["Дай", "Дал", "Даю'", "Дам"], "Дай", "The command: дай.", tr="Give me your hand!"),
        fb("За'втра я ___ тебе' кни'гу. (will give)", ["дам", "даю'", "дал", "даст"], "дам", "Я takes дам.", tr="Tomorrow I will give you the book."),
        mc("Which verb means “to give as a gift”?", ["дари'ть", "дава'ть", "дать", "говори'ть"], "дари'ть", "Дари'ть."),
        mc("Which is the perfective of говори'ть?", ["сказа'ть", "рассказа'ть", "заказа'ть", "показа'ть"], "сказа'ть", "Говори'ть / сказа'ть."),
        mc("Which question matches Я дал кни'гу бра'ту?",
           ["Кому' ты дал кни'гу?", "Кого' ты дал кни'гу?", "Чей ты дал кни'гу?", "Что ты дал кни'гу?"],
           "Кому' ты дал кни'гу?", "Кому' = to whom?"),
    ],
)

# ---------------------------------------------------------------------------- 135
L135 = lesson(
    "Helping, calling, advising, disturbing",
    "Помоги' бра'ту. Не меша'й сестре'.",
    requires=["помогать", "помочь", "звонить", "советовать", "мешать"],
    cards=[
        card("More verbs with the dative",
             "These verbs also take the dative, even though in English you often say “help someone” or “call "
             "someone” with no preposition.",
             tables=[table(
                 ["Imperfective", "Perfective", "Meaning"],
                 [["звони'ть", "позвони'ть", "to call"],
                  ["помога'ть", "помо'чь", "to help"],
                  ["сове'товать", "посове'товать", "to advise"],
                  ["меша'ть", "помеша'ть", "to disturb"],
                  ["разреша'ть", "разреши'ть", "to allow"],
                  ["объясня'ть", "объясни'ть", "to explain"],
                  ["пока'зывать", "показа'ть", "to show"]])]),
        card("The forms of помо́чь",
             "Помо'чь is an irregular perfective: помогу', помо'жешь …; past помо'г, помогла', помогли'.",
             tables=[table(
                 ["", "помо́чь"],
                 [["я", "помогу'"], ["ты", "помо'жешь"], ["он, она'", "помо'жет"],
                  ["мы", "помо'жем"], ["вы", "помо'жете"], ["они'", "помо'гут"]])],
             examples=[
                 ex("Ка'ждую сре'ду я звоню' ма'ме.", "Every Wednesday I call my mom.", "ма'ме"),
                 ex("Не меша'й бра'ту де'лать уро'ки!", "Don't disturb your brother when he's doing homework!", "бра'ту"),
                 ex("Он помо'жет нам найти' рабо'ту в Москве'.", "He will help us find a job in Moscow.", "помо'жет нам"),
                 ex("Я посове'товал дру'гу бо'льше отдыха'ть.", "I advised my friend to rest more.", "дру'гу"),
                 ex("Учи'тель объясни'л студе'нту, как писа'ть письмо'.", "The teacher explained to the student how to write a letter.", "студе'нту"),
                 ex("Покажи' отцу', где лежи'т ключ.", "Show your father where the key is.", "отцу'"),
             ]),
    ],
    verify=(vf("звонить", "звоню") + vf("позвонить", "позвоню") + vf("помогать", "помогаю") + vf("помочь", "помогу", "помочь", "поможешь", "поможет", "поможем", "поможете", "помогут", "помог", "помогла", "помогли")
            + vf("советовать", "советую") + vf("посоветовать", "посоветовал") + vf("мешать", "мешай")
            + vf("объяснить", "объяснил") + vf("показать", "покажи") + vf("мама", "маме") + vf("брат", "брату")
            + vf("студент", "студенту") + vf("отец", "отцу")),
    exercises=[
        fb("Учи'тель объясни'л ___ э'то. (the student)", ["студе'нту", "студе'нт", "студе'нта", "студе'нтом"], "студе'нту",
           "Indirect object: dative.", tr="The teacher explained it to the student.", lemma="студент"),
        fb("Покажи' ___, где лежи'т ключ. (your father)", ["отцу'", "оте'ц", "отца'", "отцо'м"], "отцу'",
           "Indirect object: dative.", tr="Show your father where the key is.", lemma="отец"),
        fb("Я позвоню' ___ за'втра. (Mom)", ["ма'ме", "ма'ма", "ма'мы", "ма'му"], "ма'ме",
           "Звони'ть takes the dative.", tr="I will call Mom tomorrow.", lemma="мама"),
        fb("Не меша'й ___ де'лать уро'ки! (your brother)", ["бра'ту", "брат", "бра'та", "бра'том"], "бра'ту",
           "Меша'ть takes the dative.", tr="Don't disturb your brother when he's doing homework!", lemma="брат"),
        fb("Он ___ нам найти' рабо'ту. (will help)", ["помо'жет", "помогу'", "помо'г", "помо'гут"], "помо'жет",
           "Он takes помо'жет.", tr="He will help us find a job.", lemma="помочь"),
        fb("Я ___ тебе'. (will help)", ["помогу'", "помо'жет", "помо'жем", "помо'г"], "помогу'",
           "Я takes помогу'.", tr="I will help you.", lemma="помочь"),
        mc("In which case is the person after помога'ть?", ["dative", "accusative", "genitive", "nominative"], "dative",
           "Помога'ть + dative.", order=True),
        mc("Which verb means “to disturb”?", ["меша'ть", "помога'ть", "звони'ть", "объясня'ть"], "меша'ть", "Меша'ть."),
        mc("Which verb means “to explain”?", ["объясня'ть", "меша'ть", "звони'ть", "сове'товать"], "объясня'ть", "Объясня'ть."),
    ],
)

# ---------------------------------------------------------------------------- 136
L136 = lesson(
    "Adjectives and pronouns in the dative",
    "Моему' хоро'шему дру'гу, на'шей тёте",
    requires=["новый", "хороший", "мой", "этот", "первый"],
    cards=[
        card("Adjective endings",
             "Masculine and neuter adjectives take -ому (hard) or -ему (soft); feminine adjectives take -ой (hard) "
             "or -ей (soft). After ж, ч, ш, щ, ц write е in place of an unstressed о.",
             tables=[table(
                 ["Masculine, neuter", "Dative", "Feminine", "Dative"],
                 [["но'вый", "но'в{ому}", "но'вая", "но'в{ой}"],
                  ["си'ний", "си'н{ему}", "си'няя", "си'н{ей}"],
                  ["ру'сский", "ру'сск{ому}", "ру'сская", "ру'сск{ой}"],
                  ["большо'й", "больш{о'му}", "больша'я", "больш{о'й}"],
                  ["хоро'ший", "хоро'ш{ему}", "хоро'шая", "хоро'ш{ей}"],
                  ["дома'шний", "дома'шн{ему}", "дома'шняя", "дома'шн{ей}"]])]),
        card("Pronouns and ordinals",
             "Question words, possessives, э'тот and тот, and ordinal numbers follow the same pattern.",
             tables=[table(
                 ["Nominative", "Masculine, neuter", "Feminine"],
                 [["како'й", "како'му", "како'й"],
                  ["чей", "чьему'", "чьей"],
                  ["э'тот", "э'тому", "э'той"],
                  ["тот", "тому'", "той"],
                  ["мой", "моему'", "мое'й"],
                  ["твой", "твоему'", "твое'й"],
                  ["наш", "на'шему", "на'шей"],
                  ["ваш", "ва'шему", "ва'шей"],
                  ["пе'рвый", "пе'рвому", "пе'рвой"],
                  ["тре'тий", "тре'тьему", "тре'тьей"]])],
             examples=[
                 ex("Я пишу' письмо' моему' хоро'шему дру'гу.", "I am writing a letter to my good friend.", "моему' хоро'шему"),
                 ex("Я купи'л э'ту игру'шку твоему' сы'ну.", "I bought this toy for your son.", "твоему'"),
                 ex("Здесь нра'вится жить на'шей тёте.", "Our aunt likes living here.", "на'шей"),
                 ex("Кому' принадлежи'т э'тот рюкза'к? — Тому' но'вому студе'нту.", "Whom does this backpack belong to? — That new student.", "Тому' но'вому"),
             ]),
    ],
    verify=(vf("новый", "новому", "новой") + vf("синий", "синему", "синей") + vf("русский", "русскому", "русской")
            + vf("большой", "большому", "большой") + vf("хороший", "хорошему", "хорошей")
            + vf("домашний", "домашнему", "домашней") + vf("какой", "какому", "какой") + vf("чей", "чьему", "чьей")
            + vf("этот", "этому", "этой") + vf("тот", "тому", "той") + vf("мой", "моему", "моей")
            + vf("твой", "твоему", "твоей") + vf("наш", "нашему", "нашей") + vf("ваш", "вашему", "вашей")
            + vf("первый", "первому", "первой") + vf("третий", "третьему", "третьей")
            + vf("принадлежать", "принадлежит") + vf("рюкзак", "рюкзак")),
    exercises=[
        fb("Я пишу' письмо' ___ дру'гу. (my)", ["моему'", "мой", "моего'", "мои'м"], "моему'",
           "Masculine dative: моему'.", tr="I am writing a letter to my friend.", lemma="мой"),
        fb("Я позвоню' ___ ма'ме. (our)", ["на'шей", "на'ша", "на'шу", "на'шего"], "на'шей",
           "Feminine dative: на'шей.", tr="I will call our mom.", lemma="наш"),
        fb("Я дал кни'гу ___ студе'нту. (new)", ["но'вому", "но'вый", "но'вого", "но'вым"], "но'вому",
           "Masculine dative: -ому.", tr="I gave the book to the new student.", lemma="новый"),
        fb("Я дал кни'гу ___ подру'ге. (good)", ["хоро'шей", "хоро'шая", "хоро'шую", "хоро'шему"], "хоро'шей",
           "Feminine dative after ш: -ей.", tr="I gave the book to a good friend.", lemma="хороший"),
        fb("Я скажу' э'то ___ учи'телю. (this)", ["э'тому", "э'тот", "э'того", "э'тим"], "э'тому",
           "Masculine dative: э'тому.", tr="I will tell this teacher.", lemma="этот"),
        fb("Я купи'л пода'рок ___ сестре'. (first)", ["пе'рвой", "пе'рвая", "пе'рвую", "пе'рвому"], "пе'рвой",
           "Feminine dative.", tr="I bought a gift for the first sister.", lemma="первый"),
        mc("Which ending do feminine hard adjectives take in the dative?", ["-ой", "-ому", "-ей", "-ым"], "-ой", "Но'вой.", order=True),
        mc("Which form is the masculine dative of мой?", ["моему'", "моего'", "мое'й", "мои'м"], "моему'", "Моему'."),
    ],
)

# ---------------------------------------------------------------------------- 137
L137 = lesson(
    "Pronouns in the dative: мне, тебе́, ему́",
    "Я скажу' ему'. Я иду' к нему'.",
    requires=["я", "ты", "он", "мы", "они"],
    cards=[
        card("The dative of the personal pronouns",
             "You already know мне from мне нра'вится. The full set: мне, тебе', ему', ей, нам, вам, им. After a "
             "preposition the third-person forms get н-: к нему', к ней, к ним. Compare Я скажу' ему' (I will tell "
             "him) and Я иду' к нему' (I am going to see him).",
             tables=[table(
                 ["Nominative", "Dative", "Example"],
                 [["я", "мне", "Он звони'т мне."],
                  ["ты", "тебе'", "Я позвоню' тебе'."],
                  ["он, оно'", "(н)ему'", "Я скажу' ему'."],
                  ["она'", "(н)ей", "Я скажу' ей."],
                  ["мы", "нам", "Он помо'жет нам."],
                  ["вы", "вам", "Я напишу' вам."],
                  ["они'", "(н)им", "Я скажу' им."]])],
             examples=[
                 ex("Я иду' к нему'.", "I am going to his place.", "к нему'"),
                 ex("Я иду' к ней.", "I am going to her place.", "к ней"),
                 ex("Я иду' к ним.", "I am going to their place.", "к ним"),
                 ex("Дай мне, пожа'луйста, ру'чку.", "Give me a pen, please.", "мне"),
                 ex("Мы помо'жем вам.", "We will help you.", "вам"),
             ]),
    ],
    verify=(vf("я", "мне") + vf("ты", "тебе") + vf("он", "ему", "нему") + vf("она", "ей", "ней") + vf("оно", "ему")
            + vf("мы", "нам") + vf("вы", "вам") + vf("они", "им", "ним") + vf("позвонить", "позвоню")
            + vf("помочь", "поможем") + vf("ручка", "ручку")),
    exercises=[
        fb("Он звони'т ___. (me)", ["мне", "я", "меня'", "мной"], "мне", "Звони'ть takes the dative.", tr="He calls me.", lemma="я"),
        fb("Я позвоню' ___. (you, informal)", ["тебе'", "ты", "тебя'", "тобо'й"], "тебе'", "Dative of ты: тебе'.", tr="I will call you.", lemma="ты"),
        fb("Я скажу' ___. (him)", ["ему'", "он", "его'", "им"], "ему'", "Dative of он: ему'.", tr="I will tell him.", lemma="он"),
        fb("Я скажу' ___. (her)", ["ей", "она'", "её", "ней"], "ей", "Dative of она': ей.", tr="I will tell her.", lemma="она"),
        fb("Я иду' к ___. (him)", ["нему'", "ему'", "его'", "ним"], "нему'", "After к: н- is added.", tr="I am going to his place.", lemma="он"),
        fb("Он помо'жет ___. (us)", ["нам", "мы", "нас", "на'ми"], "нам", "Dative of мы: нам.", tr="He will help us.", lemma="мы"),
        fb("Я иду' к ___. (them)", ["ним", "им", "их", "ни'ми"], "ним", "After к: ним.", tr="I am going to their place.", lemma="они"),
        mc("Which pronoun is “to you” (formal or plural)?", ["вам", "вас", "ва'ми", "ваш"], "вам", "Dative of вы: вам."),
        mc("Which sentence means “I am going to her place”?",
           ["Я иду' к ней.", "Я иду' к ей.", "Я иду' к её.", "Я иду' к она'."], "Я иду' к ней.", "After a preposition: ней."),
    ],
)

# ---------------------------------------------------------------------------- 138
L138 = lesson(
    "It's hot for me: feelings and wishes in the dative",
    "Мне жа'рко. Де'вочке хо'лодно. Мне ка'жется, что …",
    requires=["нравиться", "казаться", "хотеться", "надо", "погода"],
    cards=[
        card("Impersonal sentences",
             "Russian often describes a feeling, impression or need with no real subject. The person goes in the "
             "dative and the word describing the feeling stands alone. Нра'виться, каза'ться (to seem), хоте'ться "
             "(to feel like) and на'до / ну'жно (need to) all work this way. In the past add бы'ло and in the future "
             "add бу'дет.",
             tables=[table(
                 ["Russian", "English"],
                 [["Мне жа'рко.", "I am hot."],
                  ["Де'вочке хо'лодно.", "The girl is cold."],
                  ["Сы'ну хо'чется игра'ть во дворе'.", "The son feels like playing in the yard."],
                  ["Ве'ре ка'жется, что за'втра бу'дет дождь.", "It seems to Vera that it will rain tomorrow."],
                  ["Анто'ну нра'вится игра'ть в волейбо'л.", "Anton likes playing volleyball."],
                  ["Мне ну'жно научи'ться петь.", "I need to learn to sing."]])]),
        card("Past and future",
             "The same sentences in the past use бы'ло and in the future бу'дет: Вчера' мне бы'ло жа'рко. За'втра "
             "тебе' бу'дет хо'лодно. The verbs каза'ться and хоте'ться take -ся forms: ка'жется, хо'чется.",
             examples=[
                 ex("Мне жа'рко.", "I'm hot.", "Мне жа'рко"),
                 ex("Вчера' мне бы'ло жа'рко.", "Yesterday I was hot.", "бы'ло"),
                 ex("За'втра тебе' бу'дет хо'лодно.", "Tomorrow you will be cold.", "бу'дет"),
                 ex("Ему' ка'жется, что пого'да за'втра бу'дет плоха'я.", "It seems to him that the weather tomorrow will be bad.", "Ему' ка'жется"),
                 ex("Ей хо'чется спать.", "She feels like sleeping.", "хо'чется"),
             ]),
    ],
    verify=(vf("казаться", "кажется") + vf("хотеться", "хочется") + vf("нравиться", "нравится")
            + vf("девочка", "девочке") + vf("сын", "сыну") + vf("двор", "дворе") + vf("плохой", "плохая")
            + vf("научиться", "научиться") + vf("петь", "петь") + vf("волейбол", "волейбол")),
    exercises=[
        fb("___ жа'рко. (I)", ["Мне", "Я", "Меня'", "Мной"], "Мне", "The person goes in the dative.", tr="I am hot."),
        fb("Де'вочке ___. (cold)", ["хо'лодно", "холодна'я", "холо'дный", "холо'дные"], "хо'лодно",
           "An impersonal feeling: хо'лодно.", tr="The girl is cold."),
        fb("Ве'ре ___, что за'втра бу'дет дождь. (it seems)", ["ка'жется", "кажу'сь", "ка'жутся", "каза'лся"], "ка'жется",
           "Impersonal: ка'жется.", tr="It seems to Vera that it will rain tomorrow.", lemma="казаться"),
        fb("Сы'ну ___ игра'ть во дворе'. (feels like)", ["хо'чется", "хочу'", "хо'чет", "хотя'т"], "хо'чется",
           "Impersonal: хо'чется.", tr="The son feels like playing in the yard.", lemma="хотеться"),
        fb("Вчера' мне ___ жа'рко.", ["бы'ло", "бу'дет", "был", "есть"], "бы'ло", "Past: бы'ло.", tr="Yesterday I was hot."),
        fb("За'втра тебе' ___ хо'лодно.", ["бу'дет", "бы'ло", "бу'дут", "был"], "бу'дет", "Future: бу'дет.", tr="Tomorrow you will be cold."),
        fb("___ ка'жется, что пого'да плоха'я. (him)", ["Ему'", "Он", "Его'", "Им"], "Ему'", "Dative: ему'.", tr="It seems to him that the weather is bad."),
        mc("In which case is the person in Мне жа'рко?", ["dative", "nominative", "genitive", "accusative"], "dative", "Dative.", order=True),
        mc("Which means “She feels like sleeping”?",
           ["Ей хо'чется спать.", "Она' хо'чется спать.", "Её хо'чется спать.", "Ей хо'чешь спать."], "Ей хо'чется спать.",
           "Dative + хо'чется."),
    ],
)

# ---------------------------------------------------------------------------- 139
L139 = lesson(
    "How old are you? Age with the dative",
    "Ско'лько тебе' лет? — Мне два'дцать оди'н год.",
    requires=["год", "возраст", "брат", "сестра", "бабушка"],
    cards=[
        card("Age: the person goes in the dative",
             "Russian does not say “I am 20”. It says “to me 20 years”, so the person goes in the dative and the "
             "word for year depends on the last number: год after 1 (21, 31 …), го'да after 2–4 (22, 23, 24 …) and лет "
             "after 5–20 and everything that ends in 0 or 5–9. Numbers 11–14 always take лет.",
             tables=[table(
                 ["Number", "Word", "Example"],
                 [["1, 21, 31 …", "год", "Мне 21 год."],
                  ["2–4, 22–24 …", "го'да", "Ей 23 го'да."],
                  ["5–20, 25–30 …", "лет", "Ему' 25 лет."],
                  ["11–14", "лет", "Бра'ту 12 лет."]])],
             examples=[
                 ex("Ско'лько тебе' лет?", "How old are you?", "тебе'"),
                 ex("Мне 21 год.", "I am 21.", "год"),
                 ex("Мое'й сестре' 23 го'да.", "My sister is 23.", "сестре'"),
                 ex("Моему' бра'ту 32 го'да.", "My brother is 32.", "бра'ту"),
                 ex("Ба'бушке 70 лет.", "Grandma is 70.", "лет"),
             ]),
        card("Asking, and past and future",
             "Ask with Ско'лько + dative + лет: Ско'лько ему' лет? In the past add бы'ло and in the future бу'дет, "
             "exactly as in the impersonal sentences you met before. Бы'ло and бу'дет do not change for the number.",
             examples=[
                 ex("Ско'лько ему' лет?", "How old is he?", "ему'"),
                 ex("Мне бы'ло 10 лет.", "I was 10.", "бы'ло"),
                 ex("Че'рез год мне бу'дет 30 лет.", "In a year I will be 30.", "бу'дет"),
                 ex("Ско'лько лет ва'шей ба'бушке?", "How old is your grandmother?", "лет"),
             ]),
    ],
    verify=(vf("год", "года") + vf("брат", "брату") + vf("сестра", "сестре") + vf("бабушка", "бабушке")
            + vf("ты", "тебе") + vf("он", "ему") + vf("ваш", "вашей") + vf("мой", "моей", "моему")),
    exercises=[
        fb("Мне 21 ___.", ["год", "го'да", "лет", "го'ды"], "год", "After 1 (and 21, 31): год.", tr="I am 21.", lemma="год"),
        fb("Ей 23 ___.", ["го'да", "год", "лет", "го'ды"], "го'да", "After 2–4 (and 22–24): го'да.", tr="She is 23.", lemma="год"),
        fb("Ему' 25 ___.", ["лет", "год", "го'да", "го'ды"], "лет", "After 5 and up: лет.", tr="He is 25."),
        fb("Ско'лько ___ лет? (you, informal)", ["тебе'", "ты", "тебя'", "тобо'й"], "тебе'", "The person is in the dative.", tr="How old are you?", lemma="ты"),
        fb("Мое'й ___ 19 лет. (sister)", ["сестре'", "сестра'", "сестру'", "сестры'"], "сестре'", "Feminine dative: сестре'.", tr="My sister is 19.", lemma="сестра"),
        fb("Моему' ___ 32 го'да. (brother)", ["бра'ту", "брат", "бра'та", "бра'том"], "бра'ту", "Masculine dative: бра'ту.", tr="My brother is 32.", lemma="брат"),
        fb("Год наза'д мне ___ 20 лет.", ["бы'ло", "бу'дет", "есть", "была'"], "бы'ло", "Past: бы'ло.", tr="A year ago I was 20."),
        fb("Че'рез год мне ___ 30 лет.", ["бу'дет", "бы'ло", "есть", "была'"], "бу'дет", "Future: бу'дет.", tr="In a year I will be 30."),
        mc("Which word goes with the number 12?", ["лет", "год", "го'да", "го'ды"], "лет", "11–14 always take лет.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 140
L140 = lesson(
    "To a person's place: к + dative",
    "Я иду' к врачу'. Он идёт от бра'та.",
    requires=["идти", "ехать", "врач", "бабушка", "понедельник"],
    cards=[
        card("Places and people",
             "Use в or на for places, but к for the person you are heading to. The three questions use a "
             "different preposition and case set for places and for people. Ко is used before a few words, "
             "especially ко мне, ко всем and ко дню.",
             tables=[table(
                 ["", "Где?", "Куда'?", "Отку'да?"],
                 [["Places", "в / на + Prep.", "в / на + Acc.", "из / с + Gen."],
                  ["People", "у + Gen.", "к + Dat.", "от + Gen."]])],
             examples=[
                 ex("Где Андре'й? — Он у бра'та.", "Where is Andrei? — He is at his brother's.", "у бра'та"),
                 ex("Куда' идёт Андре'й? — Он идёт к бра'ту.", "Where is Andrei going? — To his brother's.", "к бра'ту"),
                 ex("Отку'да идёт Андре'й? — Он идёт от бра'та.", "Where is he coming from? — From his brother's.", "от бра'та"),
             ]),
        card("Other uses of к",
             "К also goes with places you walk toward, and with a deadline it means “by”. Remember ко мне: "
             "Приходи' ко мне! means “Come to my place!”.",
             examples=[
                 ex("Мы идём к реке'.", "We are walking toward the river.", "к реке'"),
                 ex("Студе'нт идёт к доске'.", "The student walks to the board.", "к доске'"),
                 ex("За'втра он е'дет к ба'бушке.", "Tomorrow he is going to his grandmother's.", "к ба'бушке"),
                 ex("Я зако'нчу э'то к понеде'льнику.", "I will finish this by Monday.", "к понеде'льнику"),
                 ex("Приходи' ко мне!", "Come over to my place!", "ко мне"),
             ]),
    ],
    verify=(vf("врач", "врачу") + vf("брат", "брата", "брату") + vf("река", "реке") + vf("доска", "доске")
            + vf("бабушка", "бабушке") + vf("понедельник", "понедельнику") + vf("закончить", "закончу")
            + vf("приходить", "приходи") + vf("идти", "иду", "идёт") + vf("ехать", "едет")),
    exercises=[
        fb("Я иду' ___ врачу'. (to)", ["к", "у", "от", "по"], "к", "Motion toward a person: к + dative.", tr="I am going to the doctor's."),
        fb("Где А'ня? — Она' ___ ба'бушки.", ["у", "к", "от", "в"], "у", "Location at a person's: у + genitive.", tr="Where is Anya? — She is at grandma's."),
        fb("Он идёт ___ бра'та. (from)", ["от", "к", "у", "из"], "от", "Motion away from a person: от + genitive.", tr="He is coming from his brother's."),
        fb("Мы идём к ___. (the river)", ["реке'", "река'", "ре'ку", "реко'й"], "реке'", "К takes the dative.", tr="We are walking toward the river.", lemma="река"),
        fb("Студе'нт идёт к ___. (the board)", ["доске'", "доска'", "доску'", "доско'й"], "доске'", "К takes the dative.", tr="The student walks to the board.", lemma="доска"),
        fb("Приходи' ___ мне! (to)", ["ко", "к", "у", "от"], "ко", "Ко мне: the special form before мне.", tr="Come to my place!"),
        fb("Я зако'нчу э'то ___ понеде'льнику. (by)", ["к", "у", "от", "из"], "к", "К + dative with a deadline means “by”.", tr="I will finish this by Monday."),
        mc("Which sentence means “I am going to the doctor's”?",
           ["Я иду' к врачу'.", "Я иду' у врача'.", "Я иду' от врача'.", "Я иду' в врача'."], "Я иду' к врачу'.",
           "К + dative for heading to a person."),
        mc("Which preposition means “from a person's place”?", ["от", "к", "у", "по"], "от", "От + genitive.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 141
L141 = lesson(
    "Along, around and by: по + dative",
    "Я хожу' по го'роду. Он говори'т по телефо'ну.",
    requires=["город", "дорога", "телефон", "интернет", "почта"],
    cards=[
        card("Moving along or around",
             "По takes the dative. With movement it means along or around: you walk along a corridor, drive "
             "down a road or wander around a city.",
             tables=[table(
                 ["Russian", "English"],
                 [["по коридо'ру", "along the corridor"],
                  ["по го'роду", "around the city"],
                  ["по центра'льной доро'ге", "along the central road"],
                  ["по ко'мнате", "around the room"]])],
             examples=[
                 ex("Я иду' по коридо'ру.", "I am walking along the corridor.", "по коридо'ру"),
                 ex("Они' е'дут по центра'льной доро'ге.", "They are driving along the central road.", "по центра'льной доро'ге"),
                 ex("Мы е'здим по го'роду.", "We drive around town.", "по го'роду"),
                 ex("Он хо'дит по ко'мнате.", "He paces around the room.", "по ко'мнате"),
             ]),
        card("By phone, mail and on TV",
             "По also names the means by which you send or receive something: по телефо'ну, по по'чте, по "
             "ра'дио, по телеви'зору, по интерне'ту. Radio is indeclinable, so it never changes.",
             tables=[table(
                 ["Russian", "English"],
                 [["по телефо'ну", "by / on the phone"],
                  ["по по'чте", "by mail"],
                  ["по ра'дио", "on the radio"],
                  ["по телеви'зору", "on television"],
                  ["по интерне'ту", "on the internet"]])],
             examples=[
                 ex("По телеви'зору показа'ли интере'сный фильм.", "An interesting film was shown on TV.", "По телеви'зору"),
                 ex("По ра'дио переда'ли прогно'з пого'ды.", "The weather forecast was broadcast on the radio.", "По ра'дио"),
                 ex("Я говорю' по телефо'ну.", "I am talking on the phone.", "по телефо'ну"),
             ]),
    ],
    verify=(vf("коридор", "коридору") + vf("город", "городу") + vf("дорога", "дороге") + vf("телефон", "телефону")
            + vf("телевизор", "телевизору") + vf("интернет", "интернету") + vf("почта", "почте")
            + vf("ходить", "хожу", "ходит") + vf("ездить", "ездим") + vf("показать", "показали")
            + vf("передать", "передали") + vf("прогноз", "прогноз")),
    exercises=[
        fb("Я иду' по ___. (the corridor)", ["коридо'ру", "коридо'р", "коридо'ре", "коридо'ром"], "коридо'ру", "По + dative.", tr="I am walking along the corridor.", lemma="коридор"),
        fb("Мы е'здим по ___. (the city)", ["го'роду", "го'род", "го'роде", "го'рода"], "го'роду", "По + dative.", tr="We drive around town.", lemma="город"),
        fb("Они' е'дут по центра'льной ___. (road)", ["доро'ге", "доро'га", "доро'гу", "доро'гой"], "доро'ге", "Feminine dative after по.", tr="They are driving along the central road.", lemma="дорога"),
        fb("Он говори'т по ___. (the phone)", ["телефо'ну", "телефо'н", "телефо'ном", "телефо'не"], "телефо'ну", "По + dative.", tr="He is talking on the phone.", lemma="телефон"),
        fb("По ___ показа'ли фильм. (TV)", ["телеви'зору", "телеви'зор", "телеви'зоре", "телеви'зором"], "телеви'зору", "По + dative.", tr="A film was shown on TV.", lemma="телевизор"),
        fb("Я посмотре'л э'то по ___. (the internet)", ["интерне'ту", "интерне'т", "интерне'те", "интерне'том"], "интерне'ту", "По + dative.", tr="I saw it on the internet.", lemma="интернет"),
        fb("Я отпра'влю пода'рок по ___. (mail)", ["по'чте", "по'чта", "по'чту", "по'чтой"], "по'чте", "По + dative.", tr="I will send the gift by mail.", lemma="почта"),
        mc("Which sentence means “I walk around the city”?",
           ["Я хожу' по го'роду.", "Я хожу' по го'роде.", "Я хожу' по го'рода.", "Я хожу' по го'род."],
           "Я хожу' по го'роду.", "По + dative."),
        mc("Which case does по take in по телефо'ну?", ["dative", "genitive", "accusative", "prepositional"], "dative", "Dative.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 142
L142 = lesson(
    "Character and mood: умный, строгий, смеяться",
    "Он у'мный, но стро'гий. Она' смеётся и поёт.",
    requires=["умный", "глупый", "строгий", "скучный", "смеяться"],
    cards=[
        card("Describing character",
             "These adjectives describe a person's character or how something feels. They agree with the noun "
             "in gender, number and case as always.",
             tables=[table(
                 ["Adjective", "Meaning"],
                 [["у'мный", "clever"],
                  ["глу'пый", "silly, foolish"],
                  ["стро'гий", "strict"],
                  ["гру'бый", "rude"],
                  ["весёлый", "cheerful, fun"],
                  ["ску'чный", "boring"],
                  ["счастли'вый", "happy"],
                  ["просто'й", "simple, ordinary"]])],
             examples=[
                 ex("Наш учи'тель о'чень стро'гий.", "Our teacher is very strict.", "стро'гий"),
                 ex("Он у'мный, но гру'бый.", "He is clever but rude.", "у'мный"),
                 ex("Э'тот фильм ску'чный.", "This film is boring.", "ску'чный"),
                 ex("Моя' сестра' весёлая.", "My sister is cheerful.", "весёлая"),
             ]),
        card("Verbs of feeling and fun",
             "Петь and смея'ться change their stem. Сердиться (to be angry) takes на + accusative, and an "
             "animate masculine noun in the accusative looks like the genitive: серди'ться на сы'на.",
             tables=[table(
                 ["Infinitive", "я", "он, она'"],
                 [["петь", "пою'", "поёт"],
                  ["танцева'ть", "танцу'ю", "танцу'ет"],
                  ["смея'ться", "смею'сь", "смеётся"],
                  ["улыба'ться", "улыба'юсь", "улыба'ется"],
                  ["серди'ться", "сержу'сь", "се'рдится"]])],
             examples=[
                 ex("Ма'ма се'рдится на сы'на.", "Mom is angry at her son.", "на сы'на"),
                 ex("Не серди'сь на меня'!", "Don't be angry with me!", "на меня'"),
                 ex("Кто тако'й Серге'й? — Э'то мой друг.", "Who is Sergei? — He is my friend.", "тако'й"),
                 ex("Кто така'я Ни'на? — Э'то на'ша учи'тельница.", "Who is Nina? — She is our teacher.", "така'я"),
             ]),
    ],
    verify=(vf("умный", "умный") + vf("глупый", "глупый") + vf("строгий", "строгий") + vf("грубый", "грубый")
            + vf("скучный", "скучный") + vf("счастливый", "счастливый") + vf("простой", "простой")
            + vf("петь", "пою", "поёт") + vf("танцевать", "танцую", "танцует") + vf("смеяться", "смеюсь", "смеётся", "смеются")
            + vf("улыбаться", "улыбаюсь", "улыбается") + vf("сердиться", "сержусь", "сердится", "сердись")
            + vf("сын", "сына") + vf("я", "меня") + vf("такой", "такой", "такая")),
    exercises=[
        fb("Наш учи'тель о'чень ___. (strict)", ["стро'гий", "стро'гая", "стро'гое", "стро'гие"], "стро'гий", "Masculine nominative: -ий.", tr="Our teacher is very strict.", lemma="строгий"),
        fb("Э'тот фильм ___. (boring)", ["ску'чный", "ску'чная", "ску'чное", "ску'чные"], "ску'чный", "Agrees with the masculine фильм.", tr="This film is boring.", lemma="скучный"),
        fb("Она' лю'бит ___ и танцева'ть. (to sing)", ["петь", "пою'", "поёт", "пе'сня"], "петь", "Люби'ть takes an infinitive.", tr="She loves to sing and dance.", lemma="петь"),
        fb("Де'ти ___ и игра'ют. (laugh)", ["смею'тся", "смеётся", "смею'сь", "смеёмся"], "смею'тся", "Plural: смею'тся.", tr="The children laugh and play.", lemma="смеяться"),
        fb("Не серди'сь ___ меня'! (at)", ["на", "в", "к", "о"], "на", "Серди'ться на + accusative.", tr="Don't be angry with me!"),
        fb("Ма'ма се'рдится на ___. (son)", ["сы'на", "сын", "сы'ну", "сы'ном"], "сы'на", "Animate masculine accusative = genitive.", tr="Mom is angry at her son.", lemma="сын"),
        fb("Кто ___ Серге'й? — Э'то мой друг.", ["тако'й", "така'я", "таки'е", "како'й"], "тако'й", "Masculine: тако'й.", tr="Who is Sergei? — He is my friend."),
        fb("Кто ___ Ни'на? — Э'то на'ша учи'тельница.", ["така'я", "тако'й", "таки'е", "тако'е"], "така'я", "Feminine: така'я.", tr="Who is Nina? — She is our teacher."),
        mc("Which means “She smiles”?", ["Она' улыба'ется.", "Она' улыба'ться.", "Она' улыбну'ться.", "Она' улыба'лся."], "Она' улыба'ется.", "Third person present."),
    ],
)

# ---------------------------------------------------------------------------- 143
L143 = lesson(
    "Review: the dative case",
    "Я даю' кни'гу сестре'. Я иду' к врачу'.",
    requires=["друг", "телефон", "год", "врач", "петь"],
    cards=[
        card("Where the dative is used",
             "The dative answers Кому'? (to whom?). Besides the indirect object, you meet it in impersonal "
             "feelings, in age, and after к and по.",
             tables=[table(
                 ["Use", "Example"],
                 [["Indirect object", "Я пишу' письмо' дру'гу."],
                  ["Feelings, wishes", "Мне жа'рко."],
                  ["Age", "Ей 23 го'да."],
                  ["к + person or place", "Я иду' к врачу'."],
                  ["по + movement", "Я хожу' по го'роду."],
                  ["по + means", "Я говорю' по телефо'ну."]])]),
        card("Endings at a glance",
             "Remember the pronouns мне, тебе', ему', ей, нам, вам, им, and the н- after a preposition: к нему', к ней, к ним.",
             tables=[table(
                 ["Gender", "Noun", "Adjective"],
                 [["Masculine, neuter", "-у / -ю", "-ому / -ему"],
                  ["Feminine", "-е / -и", "-ой / -ей"]])],
             examples=[
                 ex("Я скажу' э'то моему' дру'гу.", "I will tell this to my friend.", "моему' дру'гу"),
                 ex("Я позвоню' мое'й ма'тери.", "I will call my mother.", "мое'й ма'тери"),
             ]),
    ],
    verify=(vf("друг", "другу") + vf("мать", "матери") + vf("мой", "моему", "моей") + vf("отец", "отцу")
            + vf("твой", "твоему") + vf("город", "городу") + vf("телефон", "телефону")),
    exercises=[
        fb("Я позвоню' ___. (my sister)", ["мое'й сестре'", "моя' сестра'", "мою' сестру'", "мое'й сестры'"], "мое'й сестре'", "Feminine dative.", tr="I will call my sister."),
        fb("Он идёт ___ врачу'. (to)", ["к", "у", "от", "по"], "к", "К + dative.", tr="He is going to the doctor's."),
        fb("Мне 22 ___.", ["го'да", "год", "лет", "го'ды"], "го'да", "22 takes го'да.", tr="I am 22.", lemma="год"),
        fb("Сы'ну ___ игра'ть. (feels like)", ["хо'чется", "хочу'", "хо'чет", "хотя'т"], "хо'чется", "Impersonal: хо'чется.", tr="The son feels like playing."),
        fb("Мы е'здим ___ го'роду.", ["по", "в", "на", "из"], "по", "По + dative.", tr="We drive around town."),
        fb("Я говорю' ___ телефо'ну. (on the)", ["по", "в", "на", "с"], "по", "По + dative.", tr="I am talking on the phone."),
        fb("Я даю' кни'гу ___. (to her)", ["ей", "она'", "её", "ней"], "ей", "Dative: ей.", tr="I am giving her the book.", lemma="она"),
        fb("Покажи' э'то ___ отцу'. (your)", ["твоему'", "твой", "твоего'", "твои'м"], "твоему'", "Masculine dative.", tr="Show this to your father.", lemma="твой"),
        mc("Which case follows по in по го'роду?", ["dative", "genitive", "accusative", "instrumental"], "dative", "Dative.", order=True),
        mc("Which sentence is correct?", ["Я иду' к ма'тери.", "Я иду' у ма'тери.", "Я иду' от ма'тери.", "Я иду' в ма'тери."], "Я иду' к ма'тери.", "К + dative for heading to a person."),
    ],
)

UNIT = unit("Unit 16: The dative case", [L133, L134, L135, L136, L137, L138, L139, L140, L141, L142, L143])
