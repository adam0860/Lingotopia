"""Unit 19: comparison, the dative plural, нужен and свой (textbook module 5, lesson 26)."""
from dsl import *

# ---------------------------------------------------------------------------- 169
L169 = lesson(
    "More interesting, faster, colder: the comparative in -ее",
    "Э'тот фильм интере'снее, чем тот.",
    requires=["интересный", "красивый", "быстрый", "холодный", "новый"],
    cards=[
        card("Add -ее to the stem",
             "You know лу'чше and бо'льше. Most other comparatives are built the same simple way: take the stem of "
             "the adjective and add -ее. The result never changes for gender, number or case, and it is used with чем "
             "(than).",
             tables=[table(
                 ["Adjective", "Comparative", "Example"],
                 [["интере'сный", "интере'сн{ее}", "Э'тот фильм интере'снее, чем тот."],
                  ["краси'вый", "краси'в{ее}", "Э'та река' краси'вее, чем та."],
                  ["бы'стрый", "быстр{е'е}", "Мой брат бе'гает быстре'е, чем я."],
                  ["холо'дный", "холодн{е'е}", "Сего'дня холодне'е, чем вчера'."],
                  ["но'вый", "нов{е'е}", "Моя' маши'на нове'е, чем твоя'."],
                  ["си'льный", "сильн{е'е}", "Ты сильне'е, чем я."]])],
             examples=[
                 ex("Э'тот фильм интере'сный, но тот был интере'снее.", "This film is interesting, but that one was more interesting.", "интере'снее"),
                 ex("Мой брат бе'гает быстре'е, чем я.", "My brother runs faster than I do.", "быстре'е"),
                 ex("Сего'дня холодне'е, чем вчера'.", "Today is colder than yesterday.", "холодне'е"),
             ]),
        card("Where does the stress go?",
             "The stress often jumps onto the -ее: быстре'е, холодне'е, нове'е. Words with three or more syllables may "
             "keep their stress where it was: краси'вее, прия'тнее. Check each new word.",
             examples=[
                 ex("Э'та река' краси'вее, чем та.", "This river is more beautiful than that one.", "краси'вее"),
                 ex("Ты сильне'е, чем я.", "You are stronger than I am.", "сильне'е"),
             ]),
    ],
    verify=(vf("интересный", "интересный") + vf("красивый", "красивый") + vf("быстрый", "быстрый")
            + vf("холодный", "холодный") + vf("свежий", "свежая") + vf("новый", "новая") + vf("сильный", "сильный")
            + vf("бегать", "бегает") + vf("река", "река") + vf("фильм", "фильм")),
    exercises=[
        fb("Э'тот фильм ___, чем тот. (more interesting)", ["интере'снее", "интере'сный", "интере'сная", "интере'сные"], "интере'снее", "Add -ее to the stem.", tr="This film is more interesting than that one."),
        fb("Мой брат бе'гает ___, чем я. (faster)", ["быстре'е", "бы'стрый", "бы'стро", "бы'страя"], "быстре'е", "Comparative: быстре'е.", tr="My brother runs faster than I do."),
        fb("Сего'дня ___, чем вчера'. (colder)", ["холодне'е", "холо'дный", "холо'дно", "холо'дная"], "холодне'е", "Comparative: холодне'е.", tr="Today is colder than yesterday."),
        fb("Моя' маши'на ___, чем твоя'. (newer)", ["нове'е", "но'вая", "но'вый", "но'вую"], "нове'е", "Comparative: нове'е.", tr="My car is newer than yours."),
        fb("Э'та река' ___, чем та. (more beautiful)", ["краси'вее", "краси'вая", "краси'вую", "краси'вой"], "краси'вее", "Comparative: краси'вее (stress stays).", tr="This river is more beautiful than that one."),
        fb("Ты ___, чем я. (stronger)", ["сильне'е", "си'льный", "си'льная", "си'льные"], "сильне'е", "Comparative: сильне'е.", tr="You are stronger than I am."),
        mc("Which suffix forms the simple comparative?", ["-ее", "-ой", "-ым", "-ому"], "-ее", "Add -ее.", order=True),
        mc("Does интере'снее change for gender or number?", ["no", "yes, like an adjective", "only in the plural", "only for feminine"], "no", "It never changes."),
    ],
)

# ---------------------------------------------------------------------------- 170
L170 = lesson(
    "Closer, higher, cheaper: irregular comparatives",
    "Мой друг живёт бли'же к институ'ту, чем я.",
    requires=["близкий", "далёкий", "высокий", "дорогой", "лёгкий"],
    cards=[
        card("Learn these by heart",
             "Some very common comparatives are not made with -ее. The final consonant of the stem changes and the "
             "ending is -е (or -ше). Here are the first ones, about size, distance and price.",
             tables=[table(
                 ["Adjective or adverb", "Comparative", "Meaning"],
                 [["бли'зкий", "бли'же", "closer"],
                  ["далёкий", "да'льше", "farther"],
                  ["высо'кий", "вы'ше", "higher, taller"],
                  ["ни'зкий", "ни'же", "lower, shorter"],
                  ["глубо'кий", "глу'бже", "deeper"],
                  ["широ'кий", "ши'ре", "wider"],
                  ["у'зкий", "уже'", "narrower"],
                  ["дорого'й", "доро'же", "more expensive"],
                  ["дешёвый", "деше'вле", "cheaper"],
                  ["бога'тый", "богаче'", "richer"]])],
             examples=[
                 ex("Мой друг живёт бли'же к институ'ту, чем я.", "My friend lives closer to the institute than I do.", "бли'же"),
                 ex("Та ку'ртка дешёвая, но э'та ещё деше'вле.", "That jacket is cheap, but this one is even cheaper.", "деше'вле"),
                 ex("Э'та река' глу'бже, чем та.", "This river is deeper than that one.", "глу'бже"),
             ]),
        card("More irregular comparatives",
             "These are about time, frequency and everyday qualities.",
             tables=[table(
                 ["Adjective or adverb", "Comparative", "Meaning"],
                 [["лёгкий", "ле'гче", "easier, lighter"],
                  ["жа'ркий", "жа'рче", "hotter"],
                  ["коро'ткий", "коро'че", "shorter"],
                  ["ча'стый", "ча'ще", "more often"],
                  ["ре'дкий", "ре'же", "less often"],
                  ["чи'стый", "чи'ще", "cleaner"],
                  ["ти'хий", "ти'ше", "quieter"],
                  ["просто'й", "про'ще", "simpler"],
                  ["ра'но", "ра'ньше", "earlier"],
                  ["по'здно", "по'зже", "later"]])],
             examples=[
                 ex("Англи'йский язы'к ле'гче, чем ру'сский.", "English is easier than Russian.", "ле'гче"),
                 ex("Он прихо'дит по'зже, чем я.", "He comes later than I do.", "по'зже"),
                 ex("Я встаю' ра'ньше, чем ты.", "I get up earlier than you do.", "ра'ньше"),
             ]),
    ],
    verify=(vf("близкий", "близкий") + vf("далёкий", "далёкий") + vf("высокий", "высокий") + vf("дешёвый", "дешёвый")
            + vf("лёгкий", "лёгкий") + vf("жаркий", "жаркий") + vf("короткий", "короткий") + vf("чистый", "чистый")
            + vf("тихий", "тихий") + vf("простой", "простой") + vf("приходить", "приходит") + vf("вставать", "встаю")
            + vf("институт", "институту")),
    exercises=[
        fb("Мой друг живёт ___ к институ'ту, чем я. (closer)", ["бли'же", "бли'зкий", "бли'зко", "бли'зкая"], "бли'же", "Irregular: бли'зкий → бли'же.", tr="My friend lives closer to the institute than I do."),
        fb("Та ку'ртка дешёвая, но э'та ещё ___. (cheaper)", ["деше'вле", "дешёвый", "дёшево", "дешёвая"], "деше'вле", "Irregular: дешёвый → деше'вле.", tr="That jacket is cheap, but this one is even cheaper."),
        fb("Англи'йский язы'к ___, чем ру'сский. (easier)", ["ле'гче", "лёгкий", "легко'", "лёгкая"], "ле'гче", "Irregular: лёгкий → ле'гче.", tr="English is easier than Russian."),
        fb("Моя' шко'ла ___ от до'ма, чем твоя'. (farther)", ["да'льше", "далёкий", "далеко'", "далёкая"], "да'льше", "Irregular: далёкий → да'льше.", tr="My school is farther from home than yours."),
        fb("Я встаю' ___, чем ты. (earlier)", ["ра'ньше", "ра'но", "ра'нний", "по'зже"], "ра'ньше", "Ра'ньше = earlier.", tr="I get up earlier than you do."),
        fb("Он прихо'дит ___, чем я. (later)", ["по'зже", "ра'ньше", "по'здно", "по'здний"], "по'зже", "По'зже = later.", tr="He comes later than I do."),
        fb("Э'та ко'мната ___, чем моя'. (cleaner)", ["чи'ще", "чи'стый", "чи'сто", "чи'стая"], "чи'ще", "Irregular: чи'стый → чи'ще.", tr="This room is cleaner than mine."),
        fb("Мой стол ___, чем твой. (higher)", ["вы'ше", "высо'кий", "высоко'", "высо'кая"], "вы'ше", "Irregular: высо'кий → вы'ше.", tr="My desk is higher than yours."),
        mc("Which is the comparative of дорого'й?", ["доро'же", "доро'гой", "до'рого", "доро'га"], "доро'же", "Дорого'й → доро'же."),
        mc("Which is the comparative of ча'сто?", ["ча'ще", "ре'же", "ча'стый", "ча'сто"], "ча'ще", "Ча'сто → ча'ще (more often)."),
    ],
)

# ---------------------------------------------------------------------------- 171
L171 = lesson(
    "Than: чем or the genitive",
    "Я ни'же, чем он. Я ни'же тебя'.",
    requires=["брат", "молодой", "старый", "высокий", "любить"],
    cards=[
        card("Two ways to say “than”",
             "After a comparative you can use чем and put the second thing in the same case as the first, or, if the "
             "first thing is in the nominative, you can drop чем and put the second thing in the genitive.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["comparative + чем + same case", "Я ни'же, чем он."],
                  ["comparative + genitive", "Я ни'же тебя'."],
                  ["comparative + genitive", "Мой брат ста'рше меня'."],
                  ["comparative + genitive", "Ты моло'же нас."]])],
             examples=[
                 ex("Мой брат ста'рше меня'.", "My brother is older than me.", "меня'"),
                 ex("Ты моло'же нас.", "You are younger than us.", "нас"),
                 ex("Анто'н моло'же Ни'ны.", "Anton is younger than Nina.", "Ни'ны"),
             ]),
        card("When чем is required",
             "You may use the genitive only when the first thing is a subject in the nominative. If the first thing is "
             "an object, keep чем: Ты лю'бишь меня' ме'ньше, чем его'. Here меня' is the accusative, so what follows "
             "чем must be accusative too (его').",
             examples=[
                 ex("Ты лю'бишь меня' ме'ньше, чем его'.", "You love me less than him.", "чем его'"),
                 ex("Я ни'же, чем он.", "I am shorter than he is.", "чем он"),
             ]),
    ],
    verify=(vf("я", "меня") + vf("ты", "тебя") + vf("мы", "нас") + vf("он", "его") + vf("брат", "брат")
            + vf("любить", "любишь")),
    exercises=[
        fb("Мой брат ста'рше ___. (than me)", ["меня'", "я", "мне", "мной"], "меня'", "After a comparative: genitive.", tr="My brother is older than me.", lemma="я"),
        fb("Ты моло'же ___. (than us)", ["нас", "мы", "нам", "на'ми"], "нас", "Genitive of мы: нас.", tr="You are younger than us.", lemma="мы"),
        fb("Я ни'же, ___ он. (than)", ["чем", "что", "как", "и"], "чем", "Чем = than.", tr="I am shorter than he is."),
        fb("Ты лю'бишь меня' ме'ньше, чем ___. (him)", ["его'", "он", "ему'", "им"], "его'", "After чем: accusative, like меня'.", tr="You love me less than him.", lemma="он"),
        fb("Мой дом бли'же, ___ твой. (than)", ["чем", "что", "как", "когда'"], "чем", "Чем = than.", tr="My house is closer than yours."),
        fb("Анто'н моло'же ___. (than Nina)", ["Ни'ны", "Ни'на", "Ни'ну", "Ни'не"], "Ни'ны", "Genitive: Ни'ны.", tr="Anton is younger than Nina."),
        mc("When can you replace чем with the genitive?", ["When the first thing is in the nominative", "When the first thing is in the accusative", "Only with pronouns", "Never"], "When the first thing is in the nominative", "Only after a nominative subject."),
        mc("Which is correct?", ["Я мла'дше тебя'.", "Я мла'дше ты.", "Я мла'дше тебе'.", "Я мла'дше тобо'й."], "Я мла'дше тебя'.", "Genitive of ты: тебя'."),
    ],
)

# ---------------------------------------------------------------------------- 172
L172 = lesson(
    "More, most, very: бо́лее, са́мый, -ейший",
    "Э'то са'мый краси'вый го'род.",
    requires=["самый", "город", "река", "озеро", "гора"],
    cards=[
        card("A second way to compare: бо'лее and ме'нее",
             "Besides the -ее form, Russian has a compound comparative: бо'лее (more) or ме'нее (less) + the "
             "full adjective. Бо'лее and ме'нее never change, but the adjective agrees with its noun in the "
             "usual way. It is mostly used before a noun.",
             tables=[table(
                 ["Simple (predicate)", "Compound (before a noun)"],
                 [["краси'вее", "бо'лее краси'вый го'род"],
                  ["интере'снее", "бо'лее интере'сная кни'га"],
                  ["краси'вее", "ме'нее краси'вое о'зеро"]])],
             examples=[
                 ex("Э'то бо'лее краси'вый го'род.", "This is a more beautiful city.", "бо'лее краси'вый"),
                 ex("Я не зна'ю бо'лее краси'вого го'рода.", "I don't know a more beautiful city.", "бо'лее краси'вого"),
             ]),
        card("The superlative: са'мый and всех",
             "Са'мый + adjective means the most. Both words agree with the noun. As a predicate you can use the "
             "simple comparative plus всех (than all). For adverbs use всего': лу'чше всего' (best of all).",
             tables=[table(
                 ["Gender", "Compound", "Simple"],
                 [["Masculine", "са'мый краси'вый го'род", "Э'тот го'род краси'вее всех."],
                  ["Feminine", "са'мая краси'вая река'", "Э'та река' краси'вее всех."],
                  ["Neuter", "са'мое краси'вое о'зеро", "Э'то о'зеро краси'вее всех."],
                  ["Plural", "са'мые краси'вые го'ры", "Э'ти го'ры краси'вее всех."]])],
             examples=[
                 ex("Ви'ктор бе'гает быстре'е всех.", "Viktor runs faster than anyone.", "быстре'е всех"),
                 ex("Я люблю' танцева'ть, но лу'чше всего' я танцу'ю та'нго.", "I love dancing, but best of all I dance the tango.", "лу'чше всего'"),
             ]),
        card("Very: -ейший, лу'чший, ху'дший",
             "Adding -ейш- (or -айш- after г, к, х, which become ж, ч, ш) says that something has a quality to a very high "
             "degree. It is not compared with anything. Лу'чший and ху'дший mean best and worst; са'мый can be added "
             "for emphasis.",
             tables=[table(
                 ["Adjective", "With -ейший", "Meaning"],
                 [["интере'сный", "интере'снейший", "very interesting"],
                  ["тру'дный", "трудне'йший", "very hard"],
                  ["стро'гий", "строжа'йший", "very strict"],
                  ["высо'кий", "высоча'йший", "very high"],
                  ["ти'хий", "тиша'йший", "very quiet"]])],
             examples=[
                 ex("Э'то интере'снейшая кни'га. Почита'й её.", "This is a very interesting book. Read it.", "интере'снейшая"),
                 ex("Андре'й — мой са'мый лу'чший друг.", "Andrei is my best friend.", "лу'чший"),
             ]),
    ],
    verify=(vf("красивый", "красивый", "красивого") + vf("самый", "самый", "самая", "самое", "самые")
            + vf("танцевать", "танцую") + vf("лучший", "лучший") + vf("трудный", "трудный") + vf("строгий", "строгий")
            + vf("высокий", "высокий") + vf("тихий", "тихий") + vf("друг", "друг") + vf("озеро", "озеро")
            + vf("гора", "горы") + vf("почитать", "почитай") + vf("тот", "тот")),
    exercises=[
        fb("Э'то ___ краси'вый го'род. (the most)", ["са'мый", "са'мая", "са'мое", "са'мые"], "са'мый", "Agrees with the masculine го'род.", tr="This is the most beautiful city."),
        fb("Э'то са'мая ___ река'. (beautiful)", ["краси'вая", "краси'вый", "краси'вое", "краси'вые"], "краси'вая", "Agrees with the feminine река'.", tr="This is the most beautiful river."),
        fb("Э'то ___ интере'сный фильм. (more)", ["бо'лее", "са'мый", "бо'льше", "ме'ньше"], "бо'лее", "Бо'лее + adjective = more.", tr="This is a more interesting film."),
        fb("Ви'ктор бе'гает быстре'е ___. (than anyone)", ["всех", "все", "всем", "всего'"], "всех", "Simple superlative: comparative + всех.", tr="Viktor runs faster than anyone."),
        fb("Я люблю' танцева'ть, но лу'чше ___ я танцу'ю та'нго.", ["всего'", "всех", "все", "всем"], "всего'", "Adverb superlative: лу'чше всего'.", tr="I love dancing, but best of all I dance the tango."),
        fb("Андре'й — мой са'мый ___ друг. (best)", ["лу'чший", "лу'чше", "лу'чшая", "лу'чшие"], "лу'чший", "Лу'чший = best.", tr="Andrei is my best friend."),
        fb("Э'то ___ уро'к в уче'бнике. (a very hard)", ["трудне'йший", "трудне'йшая", "трудне'йшее", "трудне'йшие"], "трудне'йший", "Agrees with the masculine уро'к.", tr="This is a very hard lesson in the textbook."),
        mc("What does са'мый do?", ["Forms the superlative and agrees with the noun", "Forms the comparative", "Is always followed by всех", "Never changes"], "Forms the superlative and agrees with the noun", "Са'мый agrees with its noun."),
        mc("Which means “She is the most beautiful”?", ["Она' краси'вее всех.", "Она' краси'вая всех.", "Она' са'мое краси'вее.", "Она' краси'вее всего'."], "Она' краси'вее всех.", "Comparative + всех."),
    ],
)

# ---------------------------------------------------------------------------- 173
L173 = lesson(
    "Much faster, a bit slower, the sooner the better",
    "Чем ра'ньше, тем лу'чше! Как мо'жно скоре'е!",
    requires=["быстрый", "смелый", "скорее", "ранний", "год"],
    cards=[
        card("Making a comparison stronger or weaker",
             "Put гора'здо or намно'го (much) or ещё (even) before the comparative to strengthen it. Add the prefix по- to the "
             "comparative to say “a bit”: побыстре'е (a bit faster), посмеле'е (a bit braver).",
             tables=[table(
                 ["Pattern", "Example"],
                 [["гора'здо + comparative", "Э'та кни'га гора'здо интере'снее, чем та."],
                  ["намно'го + comparative", "Моя' но'вая маши'на е'здит намно'го быстре'е."],
                  ["ещё + comparative", "Я сме'лый, но он ещё смеле'е!"],
                  ["по- + comparative", "Бу'дь посмеле'е и отвеча'й!"]])],
             examples=[
                 ex("Э'та кни'га гора'здо интере'снее, чем та.", "This book is much more interesting than that one.", "гора'здо интере'снее"),
                 ex("Я сме'лый, но он ещё смеле'е!", "I am brave, but he is even braver!", "ещё смеле'е"),
                 ex("Говори' поме'дленнее, пожа'луйста.", "Speak a bit more slowly, please.", "поме'дленнее"),
             ]),
        card("Set patterns",
             "Learn these ready-made ways to compare: чем … тем … (the … the …), всё + comparative и … (more and "
             "more) and как мо'жно + comparative (as … as possible). To say by how much two people differ in age, use на: "
             "ста'рше на три го'да.",
             tables=[table(
                 ["Russian", "English"],
                 [["Чем ра'ньше, тем лу'чше.", "The sooner the better."],
                  ["всё вы'ше и вы'ше", "higher and higher"],
                  ["Как мо'жно скоре'е!", "As soon as possible!"],
                  ["Он ста'рше меня' на три го'да.", "He is three years older than me."],
                  ["Она' моло'же му'жа на пять лет.", "She is five years younger than her husband."]])]),
    ],
    verify=(vf("муж", "мужа") + vf("я", "меня") + vf("год", "года")
            + vf("говорить", "говори")),
    exercises=[
        fb("Э'та кни'га ___ интере'снее, чем та. (much)", ["гора'здо", "о'чень", "ма'ло", "са'мо"], "гора'здо", "Гора'здо goes with a comparative.", tr="This book is much more interesting than that one."),
        fb("Я сме'лый, но он ___ смеле'е! (even)", ["ещё", "уже'", "то'же", "тогда'"], "ещё", "Ещё + comparative = even.", tr="I am brave, but he is even braver!"),
        fb("Чем ра'ньше, ___ лу'чше.", ["тем", "чем", "что", "как"], "тем", "Чем …, тем ….", tr="The sooner the better."),
        fb("Как мо'жно ___!", ["скоре'е", "ско'ро", "ско'рый", "ско'рая"], "скоре'е", "Как мо'жно + comparative.", tr="As soon as possible!"),
        fb("Он ста'рше меня' ___ три го'да. (by)", ["на", "в", "за", "по"], "на", "Difference in age: на.", tr="He is three years older than me."),
        fb("Она' моло'же му'жа ___ пять лет.", ["на", "в", "за", "по"], "на", "Difference in age: на.", tr="She is five years younger than her husband."),
        fb("Он ста'рше меня' на два ___. (years)", ["го'да", "год", "лет", "го'ды"], "го'да", "After 2: го'да.", tr="He is two years older than me.", lemma="год"),
        fb("Всё ___ и вы'ше. (higher and higher)", ["вы'ше", "высо'кий", "высоко'", "выса'"], "вы'ше", "Всё + comparative и ….", tr="Higher and higher."),
        mc("What does the prefix по- add to a comparative?", ["a little, a bit", "very", "much", "less"], "a little, a bit", "Побыстре'е = a bit faster."),
        mc("Which is “much better”?", ["намно'го лу'чше", "о'чень лу'чше", "ма'ло лу'чше", "совсе'м лу'чше"], "намно'го лу'чше", "Намно'го + comparative."),
    ],
)

# ---------------------------------------------------------------------------- 174
L174 = lesson(
    "To the students, to the parents: nouns in the dative plural",
    "Я звоню' роди'телям. Учи'тель помога'ет студе'нтам.",
    requires=["родитель", "студент", "врач", "ребёнок", "человек"],
    cards=[
        card("-ам or -ям",
             "The dative plural is the easiest plural form: add -ам after a hard stem and -ям after a soft one. It is "
             "built from the nominative plural, so the stress is the same as there, and the spelling rule applies: "
             "after ж, ч, ш and щ write а, not я.",
             tables=[table(
                 ["Nominative singular", "Dative plural", "Ending"],
                 [["студе'нт", "студе'нт{ам}", "-ам"],
                  ["инжене'р", "инжене'р{ам}", "-ам"],
                  ["врач", "врач{а'м}", "-ам"],
                  ["ма'ма", "ма'м{ам}", "-ам"],
                  ["озеро", "озёр{ам}", "-ам"],
                  ["Андре'й", "Андре{я'м}", "-ям"],
                  ["преподава'тель", "преподава'тел{ям}", "-ям"],
                  ["тётя", "тёт{ям}", "-ям"],
                  ["мо'ре", "мор{я'м}", "-ям"],
                  ["пло'щадь", "площад{я'м}", "-ям"]])],
             examples=[
                 ex("Учи'тель помога'ет студе'нтам.", "The teacher helps the students.", "студе'нтам"),
                 ex("Я звоню' роди'телям.", "I call my parents.", "роди'телям"),
                 ex("Врач помога'ет больны'м.", "The doctor helps the sick.", "больны'м"),
             ]),
        card("Words to remember",
             "Plural words that are not regular in the nominative plural give an irregular dative plural. Learn these.",
             tables=[table(
                 ["Nominative plural", "Dative plural"],
                 [["друзья'", "друзья'м"],
                  ["бра'тья", "бра'тьям"],
                  ["де'ти", "де'тям"],
                  ["лю'ди", "лю'дям"],
                  ["ма'тери", "матеря'м"],
                  ["до'чери", "дочеря'м"],
                  ["роди'тели", "роди'телям"]])],
             examples=[
                 ex("Мы пи'шем пи'сьма друзья'м.", "We write letters to our friends.", "друзья'м"),
                 ex("Он пока'зывает фотогра'фии де'тям.", "He shows photos to the children.", "де'тям"),
                 ex("Мы говори'м э'то лю'дям.", "We say this to people.", "лю'дям"),
             ]),
    ],
    verify=(vf("студент", "студентам") + vf("инженер", "инженерам") + vf("врач", "врачам") + vf("мама", "мамам")
            + vf("озеро", "озёрам") + vf("Андрей", "Андреям") + vf("преподаватель", "преподавателям")
            + vf("тётя", "тётям") + vf("море", "морям") + vf("площадь", "площадям") + vf("друг", "друзьям")
            + vf("брат", "братьям") + vf("ребёнок", "детям") + vf("человек", "людям") + vf("мать", "матерям")
            + vf("дочь", "дочерям") + vf("родитель", "родителям") + vf("помогать", "помогает")
            + vf("звонить", "звоню") + vf("показывать", "показывает") + vf("фотография", "фотографии")
            + vf("больной", "больным")),
    exercises=[
        fb("Я звоню' ___. (my parents)", ["роди'телям", "роди'тели", "роди'телю", "роди'теля"], "роди'телям", "Soft stem: -ям.", tr="I call my parents.", lemma="родитель"),
        fb("Учи'тель помога'ет ___. (students)", ["студе'нтам", "студе'нты", "студе'нта", "студе'нту"], "студе'нтам", "Hard stem: -ам.", tr="The teacher helps the students.", lemma="студент"),
        fb("Мы пи'шем пи'сьма ___. (friends)", ["друзья'м", "друзья'", "дру'гу", "друзе'й"], "друзья'м", "Irregular plural друзья' → друзья'м.", tr="We write letters to our friends.", lemma="друг"),
        fb("Врач помога'ет ___. (children)", ["де'тям", "де'ти", "ребёнку", "дете'й"], "де'тям", "Де'ти → де'тям.", tr="The doctor helps the children.", lemma="ребёнок"),
        fb("Мы говори'м э'то ___. (people)", ["лю'дям", "лю'ди", "челове'ку", "челове'ка"], "лю'дям", "Лю'ди → лю'дям.", tr="We tell this to people.", lemma="человек"),
        fb("Мы показываем вокза'л ___. (guests)", ["гостя'м", "го'сти", "го'стя", "гостю'"], "гостя'м", "Soft stem: -ям.", tr="We show the station to the guests.", lemma="гость"),
        fb("Мы звони'м ___. (aunts)", ["тётям", "тёти", "тётя", "тётей"], "тётям", "Soft stem: -ям.", tr="We call our aunts.", lemma="тётя"),
        mc("Which ending do hard-stem nouns take in the dative plural?", ["-ам", "-ям", "-ом", "-ем"], "-ам", "Hard: -ам.", order=True),
        mc("What is the dative plural of дя'дя?", ["дя'дям", "дя'дам", "дя'де", "дя'дю"], "дя'дям", "Soft: -ям."),
    ],
)

# ---------------------------------------------------------------------------- 175
L175 = lesson(
    "To new friends, on Saturdays: adjectives in the dative plural",
    "По суббо'там мы убира'ем ко'мнату.",
    requires=["красивый", "молодой", "этот", "мой", "суббота"],
    cards=[
        card("-ым or -им",
             "In the dative plural adjectives, ordinal numbers and adjectival pronouns take -ым after a hard stem and "
             "-им after a soft stem or after к, г, х, ж, ч, ш, щ. The same endings serve all three genders.",
             tables=[table(
                 ["Nominative plural", "Dative plural"],
                 [["краси'вые", "краси'в{ым}"],
                  ["молоды'е", "молод{ы'м}"],
                  ["си'ние", "си'н{им}"],
                  ["ру'сские", "ру'сск{им}"],
                  ["хоро'шие", "хоро'ш{им}"],
                  ["больши'е", "больш{и'м}"]]),
                  table(
                 ["Nominative plural", "Dative plural"],
                 [["каки'е", "каки'м"],
                  ["чьи", "чьим"],
                  ["э'ти", "э'тим"],
                  ["те", "тем"],
                  ["други'е", "други'м"],
                  ["все", "всем"],
                  ["мои'", "мои'м"],
                  ["на'ши", "на'шим"],
                  ["пе'рвые", "пе'рвым"]],
                 note="Те and все take -ем: тем, всем. Его', её and их do not change.")],
             examples=[
                 ex("Я пишу' письмо' ста'рым друзья'м.", "I write a letter to old friends.", "ста'рым друзья'м"),
                 ex("Мы звони'м на'шим родителям.", "We call our parents.", "на'шим"),
                 ex("Я скажу' э'то всем.", "I will tell this to everyone.", "всем"),
             ]),
        card("Days and times: по + dative plural",
             "По + the dative plural says that something happens regularly on those days or at those times: по "
             "суббо'там (on Saturdays), по у'трам (in the mornings), по вечера'м (in the evenings).",
             tables=[table(
                 ["Russian", "English"],
                 [["по понеде'льникам", "on Mondays"],
                  ["по средам", "on Wednesdays"],
                  ["по суббо'там", "on Saturdays"],
                  ["по выходны'м", "on days off"],
                  ["по у'трам", "in the mornings"],
                  ["по вечера'м", "in the evenings"],
                  ["по ноча'м", "at night, nightly"]])],
             examples=[
                 ex("По суббо'там мы убира'ем ко'мнату.", "On Saturdays we clean our room.", "По суббо'там"),
                 ex("Он у'чится по вечера'м.", "He studies in the evenings.", "по вечера'м"),
                 ex("Ва'жно за'втракать по у'трам.", "It is important to eat breakfast in the morning.", "по у'трам"),
             ]),
    ],
    verify=(vf("красивый", "красивым") + vf("молодой", "молодым") + vf("синий", "синим") + vf("русский", "русским")
            + vf("хороший", "хорошим") + vf("большой", "большим") + vf("какой", "каким") + vf("чей", "чьим")
            + vf("этот", "этим") + vf("тот", "тем") + vf("другой", "другим") + vf("весь", "всем") + vf("мой", "моим")
            + vf("наш", "нашим") + vf("первый", "первым") + vf("старый", "старым") + vf("друг", "друзьям")
            + vf("родитель", "родителям") + vf("понедельник", "понедельникам") + vf("среда", "средам")
            + vf("суббота", "субботам") + vf("выходной", "выходным") + vf("утро", "утрам") + vf("вечер", "вечерам")
            + vf("ночь", "ночам") + vf("убирать", "убираем") + vf("учиться", "учится") + vf("завтракать", "завтракать")),
    exercises=[
        fb("Я пишу' письма ___ друзья'м. (good)", ["хоро'шим", "хоро'шие", "хоро'ших", "хоро'шими"], "хоро'шим", "Dative plural after ш: -им.", tr="I write letters to good friends.", lemma="хороший"),
        fb("Мы помога'ем ___ студе'нтам. (new)", ["но'вым", "но'вые", "но'вых", "но'выми"], "но'вым", "Dative plural, hard stem: -ым.", tr="We help the new students.", lemma="новый"),
        fb("Я звоню' ___ роди'телям. (my)", ["мои'м", "мои'", "мои'х", "мои'ми"], "мои'м", "Dative plural: мои'м.", tr="I call my parents.", lemma="мой"),
        fb("Я скажу' э'то ___ студе'нтам. (all)", ["всем", "все", "всех", "все'ми"], "всем", "Dative plural: всем.", tr="I will tell this to all the students.", lemma="весь"),
        fb("___ суббо'там мы убира'ем ко'мнату. (on)", ["По", "В", "На", "За"], "По", "По + dative plural.", tr="On Saturdays we clean our room."),
        fb("Он у'чится по ___. (evenings)", ["вечера'м", "ве'чер", "вечера'", "вечера'х"], "вечера'м", "По + dative plural.", tr="He studies in the evenings.", lemma="вечер"),
        fb("Я рабо'таю по ___. (nights)", ["ноча'м", "но'чи", "ночь", "ноча'х"], "ноча'м", "По + dative plural.", tr="I work nights.", lemma="ночь"),
        fb("Физподгото'вка у нас по ___. (Wednesdays)", ["среда'м", "среда'", "сре'ду", "среде'"], "среда'м", "По + dative plural.", tr="We have physical training on Wednesdays.", lemma="среда"),
        mc("What does по у'трам mean?", ["in the mornings", "tomorrow morning", "this morning", "every morning at 7"], "in the mornings", "Regular times: по + dative plural."),
        mc("Which ending do hard-stem adjectives take in the dative plural?", ["-ым", "-им", "-ой", "-ому"], "-ым", "Dative plural: -ым.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 176
L176 = lesson(
    "Time to sleep, it's a pity: more impersonal dative sentences",
    "Де'тям пора' спать. Нам о'чень жаль.",
    requires=["пора", "жаль", "нечего", "лекция", "отпуск"],
    cards=[
        card("Dative + a word for a state",
             "You know Мне жа'рко. The same pattern works for many more states: the person is in the dative and "
             "the state is a single word that never changes. Add бы'ло or бу'дет for the past and the future.",
             tables=[table(
                 ["Russian", "English"],
                 [["Ане и Ка'те хо'лодно.", "Anya and Katya are cold."],
                  ["Нам о'чень жаль, что …", "We are very sorry that …"],
                  ["Де'тям пора' спать.", "It is time for the children to sleep."],
                  ["Дире'ктору хо'чется в о'тпуск.", "The director feels like going on vacation."],
                  ["Нам бы'ло интере'сно на ле'кции.", "We found the lecture interesting."],
                  ["Ему' не'чего де'лать.", "He has nothing to do."]])],
             examples=[
                 ex("Де'тям пора' спать.", "It's time for the children to go to bed.", "пора'"),
                 ex("Нам о'чень жаль, что ты уезжа'ешь.", "We are very sorry that you are leaving.", "жаль"),
                 ex("Ему' не'чего де'лать.", "He has nothing to do.", "не'чего"),
                 ex("Нам бы'ло интере'сно на ле'кции.", "We found the lecture interesting.", "бы'ло интере'сно"),
             ]),
        card("No subject at all",
             "Some sentences have no subject whatever: На у'лице темно'. (It is dark outside.) Темне'ет. (It is "
             "getting dark.) Here Russian simply leaves out “it”.",
             examples=[
                 ex("На у'лице темно'.", "It is dark outside.", "темно'"),
                 ex("Темне'ет.", "It is getting dark.", "Темне'ет"),
             ]),
    ],
    verify=(vf("хотеться", "хочется") + vf("уезжать", "уезжаешь") + vf("темнеть", "темнеет") + vf("лекция", "лекции")
            + vf("отпуск", "отпуск") + vf("директор", "директору") + vf("ребёнок", "детям") + vf("спать", "спать")
            + vf("делать", "делать")),
    exercises=[
        fb("Де'тям ___ спать. (it's time)", ["пора'", "нельзя'", "жаль", "не'чего"], "пора'", "Пора' = it's time.", tr="It's time for the children to go to bed."),
        fb("Нам о'чень ___, что ты уезжа'ешь. (sorry)", ["жаль", "пора'", "хо'лодно", "бы'ло"], "жаль", "Жаль = a pity, sorry.", tr="We are very sorry that you are leaving."),
        fb("Ему' ___ де'лать. (has nothing to)", ["не'чего", "ничего'", "ничто'", "никто'"], "не'чего", "Не'чего + infinitive.", tr="He has nothing to do."),
        fb("Нам бы'ло ___ на ле'кции. (interesting)", ["интере'сно", "интере'сный", "интере'сная", "интере'сные"], "интере'сно", "A state word does not change.", tr="We found the lecture interesting."),
        fb("Ане и Ка'те ___. (cold)", ["хо'лодно", "холо'дный", "холодна'", "холодны'"], "хо'лодно", "State word: хо'лодно.", tr="Anya and Katya are cold."),
        fb("На у'лице ___. (it is dark)", ["темно'", "тёмный", "темна'", "тёмная"], "темно'", "No subject: темно'.", tr="It is dark outside."),
        fb("Дире'ктору ___ в о'тпуск. (feels like going)", ["хо'чется", "хо'чет", "хочу'", "хоте'л"], "хо'чется", "Impersonal: хо'чется.", tr="The director feels like going on vacation.", lemma="хотеться"),
        mc("In which case is the person in Де'тям пора' спать?", ["dative", "nominative", "genitive", "accusative"], "dative", "Dative.", order=True),
        mc("Which means “It is getting dark”?", ["Темне'ет.", "Темно'.", "Тёмный.", "Темнота'."], "Темне'ет.", "A verb with no subject."),
    ],
)

# ---------------------------------------------------------------------------- 177
L177 = lesson(
    "I need a dictionary: нужен, нужна, нужно, нужны",
    "Мне ну'жен словарь. Тебе' нужна' маши'на.",
    requires=["надо", "компьютер", "словарь", "машина", "пальто"],
    cards=[
        card("Two ways to say “need”",
             "На'до, ну'жно and необходи'мо (necessary) are followed by an infinitive: Мне на'до идти'. For a thing "
             "you need, use ну'жен, нужна', ну'жно or нужны' (and necessary: необходи'м, необходи'ма, "
             "необходи'мо, необходи'мы). The person who needs it is in the dative, and the word needed is the "
             "subject: it is in the nominative and the adjective agrees with it.",
             tables=[table(
                 ["Thing needed", "Needed", "Necessary"],
                 [["Masculine", "ну'жен", "необходи'м"],
                  ["Feminine", "нужна'", "необходи'ма"],
                  ["Neuter", "ну'жно", "необходи'мо"],
                  ["Plural", "нужны'", "необходи'мы"]])],
             examples=[
                 ex("Мне ну'жен но'вый компью'тер.", "I need a new computer.", "ну'жен"),
                 ex("Тебе' не нужна' маши'на.", "You do not need a car.", "нужна'"),
                 ex("Моему' сы'ну ну'жно пальто'.", "My son needs a coat.", "ну'жно"),
                 ex("Вам нужны' де'ньги?", "Do you need money?", "нужны'"),
                 ex("Вы мне нужны'.", "I need you.", "нужны'"),
             ]),
        card("Past and future",
             "Put the right form of быть after the word. In на'до, ну'жно and необходи'мо sentences use бы'ло or "
             "бу'дет. With ну'жен use был, была', бы'ло, бы'ли or бу'дет, бу'дут to agree with the thing needed. The "
             "need word comes first.",
             examples=[
                 ex("Мне ну'жен был словарь.", "I needed a dictionary.", "ну'жен был"),
                 ex("Им нужна' была' я.", "They needed me.", "нужна' была'"),
                 ex("Нам необходи'мо бу'дет встать ра'но.", "We will have to get up early.", "необходи'мо бу'дет"),
                 ex("Ви'те ну'жно бы'ло позвони'ть А'не.", "Vitya had to call Anya.", "ну'жно бы'ло"),
             ]),
    ],
    verify=(vf("компьютер", "компьютер") + vf("словарь", "словарь") + vf("машина", "машина") + vf("пальто", "пальто")
            + vf("быть", "был", "была", "было", "будет") + vf("встать", "встать") + vf("позвонить", "позвонить")
            + vf("новый", "новый") + vf("мы", "нам") + vf("сын", "сыну") + vf("мой", "моему")),
    exercises=[
        fb("Мне ___ но'вый компью'тер. (need)", ["ну'жен", "нужна'", "ну'жно", "нужны'"], "ну'жен", "Masculine: ну'жен.", tr="I need a new computer."),
        fb("Тебе' не ___ маши'на. (need)", ["нужна'", "ну'жен", "ну'жно", "нужны'"], "нужна'", "Feminine: нужна'.", tr="You do not need a car."),
        fb("Вам ___ де'ньги? (need)", ["нужны'", "ну'жен", "нужна'", "ну'жно"], "нужны'", "Plural: нужны'.", tr="Do you need money?"),
        fb("Моему' сы'ну ___ пальто'. (needs)", ["ну'жно", "ну'жен", "нужна'", "нужны'"], "ну'жно", "Neuter: ну'жно.", tr="My son needs a coat."),
        fb("Вы мне ___. (I need you)", ["нужны'", "ну'жен", "нужна'", "ну'жно"], "нужны'", "Plural вы: нужны'.", tr="I need you."),
        fb("Мне ___ идти'. (I need to go)", ["на'до", "ну'жен", "нужна'", "нужны'"], "на'до", "Before an infinitive: на'до.", tr="I need to go.", lemma="надо"),
        fb("Вчера' мне ___ был словарь. (needed)", ["ну'жен", "ну'жно", "нужна'", "нужны'"], "ну'жен", "Masculine словарь: ну'жен.", tr="Yesterday I needed a dictionary."),
        fb("Им нужна' ___ я. (was)", ["была'", "был", "бы'ло", "бы'ли"], "была'", "Agrees with нужна': была'.", tr="They needed me."),
        mc("Which means “I need a car”?", ["Мне нужна' маши'на.", "Я нужна' маши'на.", "Мне нужну' маши'ну.", "Я ну'жен маши'на."], "Мне нужна' маши'на.", "Dative + нужна' + nominative."),
        mc("What do ну'жен, нужна', ну'жно and нужны' agree with?", ["the thing that is needed", "the person who needs it", "the verb", "the preposition"], "the thing that is needed", "They agree with the subject: the thing needed."),
    ],
)

# ---------------------------------------------------------------------------- 178
L178 = lesson(
    "My own: свой, своя, своё, свои",
    "Он лю'бит своего' бра'та. Она' пи'шет своему' бра'ту.",
    requires=["свой", "брат", "друг", "письмо", "документ"],
    cards=[
        card("One's own",
             "Свой means “one's own” and refers back to the subject of the clause. Use it to make clear that the "
             "thing belongs to the person who does the action. With я, ты, мы and вы, свой is optional, but with он, "
             "она' and они' it prevents confusion: его', её and их mean someone else's.",
             tables=[table(
                 ["Subject", "Own", "Someone else's"],
                 [["я", "мой / свой", "—"],
                  ["ты", "твой / свой", "—"],
                  ["он", "свой", "его'"],
                  ["она'", "свой", "её"],
                  ["мы", "наш / свой", "—"],
                  ["вы", "ваш / свой", "—"],
                  ["они'", "свой", "их"]])],
             examples=[
                 ex("Он о'чень лю'бит своего' бра'та.", "He loves his (own) brother very much.", "своего' бра'та"),
                 ex("Я о'чень люблю' его' бра'та.", "I love his brother very much (not mine).", "его' бра'та"),
                 ex("А'ня пи'шет письмо' своему' бра'ту.", "Anya is writing to her own brother.", "своему' бра'ту"),
                 ex("Он и'щет свои' докуме'нты.", "He is looking for his (own) documents.", "свои' докуме'нты"),
             ]),
        card("Forms and limits",
             "Свой declines like мой and твой. It always refers to the subject of its own clause, so it can't "
             "be used when the owner is in another clause, and it can't describe the subject itself.",
             tables=[table(
                 ["Case", "Masculine, neuter", "Feminine", "Plural"],
                 [["Nominative", "свой, своё", "своя'", "свои'"],
                  ["Genitive", "своего'", "свое'й", "свои'х"],
                  ["Dative", "своему'", "свое'й", "свои'м"],
                  ["Instrumental", "свои'м", "свое'й", "свои'ми"],
                  ["Prepositional", "о своём", "о свое'й", "о свои'х"]])],
             examples=[
                 ex("Кири'лл говори'т, что его' сестра' пое'хала в магази'н.", "Kirill says his sister has gone to the shop.", "его' сестра'"),
                 ex("У меня' тепе'рь есть свой компью'тер.", "I now have my own computer.", "свой компью'тер"),
             ]),
    ],
    verify=(vf("свой", "свой", "своя", "свои", "своего", "своему", "своих", "своим", "своей") + vf("брат", "брата", "брату")
            + vf("документ", "документы") + vf("искать", "ищет") + vf("писать", "пишет") + vf("поехать", "поехала")
            + vf("кирилл", "кирилл")),
    exercises=[
        fb("Он о'чень лю'бит ___ бра'та. (his own)", ["своего'", "его'", "свой", "свои'х"], "своего'", "Свой refers to the subject.", tr="He loves his own brother very much."),
        fb("А'ня пи'шет письмо' ___ бра'ту. (her own)", ["своему'", "её", "свой", "свои'м"], "своему'", "Dative masculine: своему'.", tr="Anya is writing a letter to her own brother."),
        fb("Он и'щет ___ докуме'нты. (his own)", ["свои'", "его'", "своё", "своя'"], "свои'", "Plural: свои'.", tr="He is looking for his own documents."),
        fb("Де'ти зову'т ___ отца'. (their own)", ["своего'", "их", "свой", "свои'"], "своего'", "Accusative animate: своего'.", tr="The children are calling their father."),
        fb("У меня' тепе'рь есть ___ компью'тер. (my own)", ["свой", "своего'", "своя'", "своё"], "свой", "Masculine inanimate: свой.", tr="I now have my own computer."),
        fb("Кири'лл говори'т, что ___ сестра' пое'хала в магази'н. (his)", ["его'", "свой", "своя'", "свои'"], "его'", "Свой can't modify the subject of another clause.", tr="Kirill says his sister went to the shop."),
        mc("Which is true about свой?", ["It refers to the subject of the clause", "It refers to the object", "It is only for я", "It never changes"], "It refers to the subject of the clause", "Свой refers back to the subject."),
        mc("Which sentence says Anya writes to her own brother?",
           ["А'ня пи'шет письмо' своему' бра'ту.", "А'ня пи'шет письмо' свой бра'т.", "А'ня пи'шет письмо' своего' бра'та.", "А'ня пи'шет письмо' свои'м бра'ту."],
           "А'ня пи'шет письмо' своему' бра'ту.", "Dative masculine: своему'."),
    ],
)

# ---------------------------------------------------------------------------- 179
L179 = lesson(
    "Review: comparing, the dative plural, need and own",
    "Э'тот фильм интере'снее, чем тот. Мне ну'жен словарь.",
    requires=["интересный", "брат", "суббота", "свой", "надо"],
    cards=[
        card("Quick map",
             "A review of the main points of this unit.",
             tables=[table(
                 ["Topic", "Example"],
                 [["Comparative", "Э'тот фильм интере'снее, чем тот."],
                  ["Irregular", "бли'зкий — бли'же, дорого'й — доро'же"],
                  ["Than", "Я ни'же тебя'. Я ни'же, чем он."],
                  ["Superlative", "са'мый краси'вый, краси'вее всех"],
                  ["Dative plural", "студе'нтам, но'вым друзья'м"],
                  ["Regular days", "по суббо'там, по у'трам"],
                  ["Need", "Мне ну'жен словарь. Тебе' нужна' маши'на."],
                  ["Own", "Он лю'бит своего' бра'та."]])]),
    ],
    verify=(vf("брат", "брата") + vf("интересный", "интересный")),
    exercises=[
        fb("Э'тот фильм ___, чем тот. (more interesting)", ["интере'снее", "интере'сный", "интере'сная", "интере'сные"], "интере'снее", "Add -ее.", tr="This film is more interesting than that one."),
        fb("Англи'йский язы'к ___, чем ру'сский. (easier)", ["ле'гче", "лёгкий", "легко'", "лёгкая"], "ле'гче", "Irregular: ле'гче.", tr="English is easier than Russian."),
        fb("Мой брат ста'рше ___. (than me)", ["меня'", "я", "мне", "мной"], "меня'", "After a comparative: genitive.", tr="My brother is older than me."),
        fb("Э'то ___ краси'вый го'род. (the most)", ["са'мый", "са'мая", "са'мое", "са'мые"], "са'мый", "Agrees with го'род.", tr="This is the most beautiful city."),
        fb("Я звоню' ___ роди'телям. (my)", ["мои'м", "мои'", "мои'х", "мои'ми"], "мои'м", "Dative plural.", tr="I call my parents.", lemma="мой"),
        fb("___ суббо'там мы убира'ем ко'мнату.", ["По", "В", "На", "За"], "По", "По + dative plural.", tr="On Saturdays we clean our room."),
        fb("Де'тям ___ спать. (it's time)", ["пора'", "нельзя'", "жаль", "не'чего"], "пора'", "Пора' = it's time.", tr="It's time for the children to go to bed."),
        fb("Тебе' не ___ маши'на. (need)", ["нужна'", "ну'жен", "ну'жно", "нужны'"], "нужна'", "Feminine: нужна'.", tr="You do not need a car."),
        fb("Он о'чень лю'бит ___ бра'та. (his own)", ["своего'", "его'", "свой", "свои'х"], "своего'", "Свой refers to the subject.", tr="He loves his own brother very much."),
        mc("Which means “much better”?", ["намно'го лу'чше", "о'чень лу'чше", "ма'ло лу'чше", "совсе'м лу'чше"], "намно'го лу'чше", "Намно'го + comparative."),
    ],
)

UNIT = unit("Unit 19: Comparison, the dative plural, need and own",
            [L169, L170, L171, L172, L173, L174, L175, L176, L177, L178, L179])
