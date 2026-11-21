"""Unit 9: describing places, flying and swimming, telling time
(textbook module 2, lesson 13)."""
from dsl import *

# ---------------------------------------------------------------------------- 58
L58 = lesson(
    "Adjectives in the prepositional: -ом and -ой",
    "В краси'вом го'роде, в но'вой кни'ге",
    requires=["красивый", "новый", "город", "письмо", "машина"],
    cards=[
        card("The adjective changes with its noun",
             "In lesson 16 you learned that a noun takes the prepositional ending after в, на or о. A describing word "
             "in front of that noun changes too, because adjectives always agree with their noun in gender, number "
             "and case. In the singular, a masculine or neuter adjective ends in -ом, and a feminine one ends in -ой. "
             "Masculine and neuter match, just as they matched for nouns.",
             tables=[table(
                 ["Gender", "Nominative", "Prepositional"],
                 [["masculine", "краси'вый го'род", "в краси'в{ом} го'роде"],
                  ["masculine", "но'вый уче'бник", "в но'в{ом} уче'бнике"],
                  ["neuter", "ка'ждое письмо'", "в ка'жд{ом} письме'"],
                  ["feminine", "зелёная маши'на", "в зелён{ой} маши'не"],
                  ["feminine", "но'вая шко'ла", "в но'в{ой} шко'ле"]],
                 note="Both words change, and the adjective ending is the one you hear first. "
                      "This lesson covers the regular hard-stem endings. Soft stems and the spelling rules come next.")]),
        card("Using it",
             "Everything you know about в and на still applies. Only the adjective is new. When the adjective "
             "stands after о, remember to use об before a vowel: об интере'сной кни'ге.",
             examples=[
                 ex("Я живу' в но'вом до'ме.", "I live in a new house.", "в но'вом до'ме"),
                 ex("Она' рабо'тает в краси'вом го'роде.", "She works in a beautiful city.", "в краси'вом го'роде"),
                 ex("Мы говори'м об интере'сной кни'ге.", "We are talking about an interesting book.", "об интере'сной кни'ге"),
                 ex("Кни'га лежи'т на ста'ром столе'.", "The book is lying on the old table.", "на ста'ром столе'"),
                 ex("Мы гуля'ем в краси'вом па'рке.", "We are walking in a beautiful park.", "в краси'вом па'рке"),
             ]),
    ],
    verify=(vf("новый", "новом", "новой") + vf("красивый", "красивом") + vf("старый", "старом", "старой")
            + vf("интересный", "интересной") + vf("зелёный", "зелёной") + vf("каждый", "каждом")
            + vf("город", "городе") + vf("парк", "парке") + vf("письмо", "письме")),
    exercises=[
        fb("Мы живём в ___ до'ме.", ["но'вом", "но'вой", "но'вый", "но'вого"], "но'вом",
           "Masculine prepositional: -ом.", tr="We live in a new house.", lemma="новый"),
        fb("Она' рабо'тает в ___ шко'ле.", ["но'вой", "но'вом", "но'вая", "но'вую"], "но'вой",
           "Feminine prepositional: -ой.", tr="She works in a new school.", lemma="новый"),
        fb("Мы говори'м об ___ кни'ге.", ["интере'сной", "интере'сном", "интере'сная", "интере'сную"], "интере'сной",
           "Feminine prepositional: -ой.", tr="We are talking about an interesting book.", lemma="интересный"),
        fb("Мы гуля'ем в ___ па'рке.", ["краси'вом", "краси'вой", "краси'вый", "краси'вого"], "краси'вом",
           "Masculine prepositional: -ом.", tr="We are walking in a beautiful park.", lemma="красивый"),
        fb("Кни'га лежи'т на ___ столе'.", ["ста'ром", "ста'рой", "ста'рый", "ста'рую"], "ста'ром",
           "Стол is masculine: -ом.", tr="The book is lying on the old table.", lemma="старый"),
        fb("В ___ письме' она' пи'шет о до'ме.", ["ка'ждом", "ка'ждой", "ка'ждое", "ка'ждый"], "ка'ждом",
           "Письмо' is neuter, and neuter takes the masculine ending -ом.", tr="In every letter she writes about the house.", lemma="каждый"),
        mc("Which ending does a feminine adjective take in the prepositional?", ["-ой", "-ом", "-ая", "-ую"], "-ой",
           "В но'вой шко'ле.", order=True),
        mc("Which ending do masculine AND neuter adjectives take in the prepositional?", ["-ом", "-ой", "-ый", "-ое"], "-ом",
           "В но'вом до'ме, в но'вом письме'.", order=True),
        mc("Which phrase means “in a beautiful city”?",
           ["в краси'вом го'роде", "в краси'вый го'род", "в краси'вой го'роде", "в краси'вом го'род"],
           "в краси'вом го'роде", "Noun and adjective are both prepositional, and город is masculine."),
    ],
)

# ---------------------------------------------------------------------------- 59
L59 = lesson(
    "Soft stems and spelling: -ем, -ей and the spelling rules",
    "В си'нем пла'тье, в ру'сском словаре', в хоро'шей кни'ге",
    requires=["синий", "русский", "хороший", "большой", "словарь"],
    cards=[
        card("Soft stems: -ем and -ей",
             "Adjectives that end in -ий, -яя or -ее in the nominative are soft-stem adjectives. In the "
             "prepositional they take -ем for masculine and neuter, and -ей for feminine, instead of -ом and -ой. "
             "Look at the dictionary form to decide which set you need.",
             tables=[table(
                 ["Gender", "Nominative", "Prepositional"],
                 [["masculine", "си'ний уче'бник", "в си'н{ем} уче'бнике"],
                  ["neuter", "си'нее пла'тье", "в си'н{ем} пла'тье"],
                  ["feminine", "си'няя ю'бка", "в си'н{ей} ю'бке"],
                  ["masculine", "после'дний день", "в после'дн{ем} дне"],
                  ["feminine", "после'дняя неде'ля", "в после'дн{ей} неде'ле"]])]),
        card("The spelling rules still apply",
             "The two spelling rules from lesson 25 decide what happens after certain letters. After г, к, х you "
             "always write -ом and -ой, whatever the stress. After ж, ч, ш, щ you write -ем and -ей when the ending "
             "is unstressed, but -ом and -ой when it is stressed. That is why a stressed ending still sounds like "
             "-ой: большо'й, большо'м.",
             tables=[table(
                 ["Adjective", "Masculine / neuter", "Feminine"],
                 [["ру'сский", "в ру'сск{ом} словаре'", "в ру'сск{ой} кни'ге"],
                  ["ма'ленький", "в ма'леньк{ом} до'ме", "в ма'леньк{ой} ко'мнате"],
                  ["хоро'ший", "в хоро'ш{ем} словаре'", "в хоро'ш{ей} кни'ге"],
                  ["большо'й", "в больш{о'м} го'роде", "в больш{о'й} ко'мнате"]],
                 note="Ру'сский and ма'ленький follow the г/к/х rule. Хоро'ший has an unstressed ending, so it keeps "
                      "-ем/-ей. Большо'й has a stressed ending, so it takes -ом/-ой.")],
             examples=[
                 ex("Мы живём в большо'м го'роде.", "We live in a big city.", "в большо'м го'роде"),
                 ex("Э'то сло'во есть в ру'сском словаре'.", "This word is in the Russian dictionary.", "в ру'сском словаре'"),
                 ex("Она' живёт в хоро'шей кварти'ре.", "She lives in a good apartment.", "в хоро'шей кварти'ре"),
                 ex("В си'ней ю'бке она' о'чень краси'вая.", "In a blue skirt she is very beautiful.", "В си'ней ю'бке"),
             ]),
    ],
    verify=(vf("синий", "синем", "синей") + vf("последний", "последнем", "последней")
            + vf("русский", "русском", "русской") + vf("маленький", "маленьком", "маленькой")
            + vf("хороший", "хорошем", "хорошей") + vf("большой", "большом", "большой")
            + vf("словарь", "словаре") + vf("платье", "платье") + vf("юбка", "юбке")),
    exercises=[
        fb("Мы живём в ___ го'роде.", ["большо'м", "бо'льшем", "большо'й", "большо'го"], "большо'м",
           "Stressed ending after щ/ш/ж/ч: -ом.", tr="We live in a big city.", lemma="большой"),
        fb("В ___ словаре' есть э'то сло'во.", ["ру'сском", "ру'сскем", "ру'сской", "ру'сский"], "ру'сском",
           "After к always -ом, never -ем.", tr="This word is in the Russian dictionary.", lemma="русский"),
        fb("Она' живёт в ___ кварти'ре.", ["хоро'шей", "хоро'шой", "хоро'шая", "хоро'шее"], "хоро'шей",
           "After ш with an unstressed ending: -ей.", tr="She lives in a good apartment.", lemma="хороший"),
        fb("В ___ ю'бке она' о'чень краси'вая.", ["си'ней", "си'ной", "си'няя", "си'нюю"], "си'ней",
           "Soft-stem feminine: -ей.", tr="In a blue skirt she is very beautiful.", lemma="синий"),
        fb("Мы живём в ___ до'ме.", ["ма'леньком", "ма'ленькем", "ма'ленький", "ма'леньких"], "ма'леньком",
           "After к: -ом.", tr="We live in a small house.", lemma="маленький"),
        fb("В ___ ко'мнате есть окно'.", ["большо'й", "больше'й", "большо'м", "большо'я"], "большо'й",
           "Stressed ending after щ/ш/ж/ч: -ой.", tr="There is a window in the big room.", lemma="большой"),
        fb("В ___ комнате тепло'.", ["после'дней", "после'дном", "после'дняя", "после'днюю"], "после'дней",
           "Soft-stem feminine: -ей.", tr="It's warm in the last room.", lemma="последний"),
        mc("Which endings do you always write after г, к, х?", ["-ом / -ой", "-ем / -ей", "-ым / -ей", "-ом / -ей"], "-ом / -ой",
           "Never -ем or -ей after г, к, х.", order=True),
        mc("After ж, ч, ш, щ, which endings do you write when the ending is unstressed?",
           ["-ем / -ей", "-ом / -ой", "-ым / -ой", "-ам / -ай"], "-ем / -ей",
           "Хоро'шем, хоро'шей.", order=True),
        mc("Which phrase means “in a good dictionary”?",
           ["в хоро'шем словаре'", "в хоро'шом словаре'", "в хоро'шым словаре'", "в хоро'шего словаре'"],
           "в хоро'шем словаре'", "After ш, an unstressed ending is -ем."),
        mc("Which phrase means “in a Russian book”?",
           ["в ру'сской кни'ге", "в ру'ссей кни'ге", "в ру'сская кни'ге", "в ру'сскую кни'ге"],
           "в ру'сской кни'ге", "After к: -ой."),
    ],
)

# ---------------------------------------------------------------------------- 60
L60 = lesson(
    "My, this, which, first: pronouns and ordinals in the prepositional",
    "О моём бра'те, об э'той кни'ге, на тре'тьем этаже'",
    requires=["мой", "наш", "этот", "какой", "первый", "этаж"],
    cards=[
        card("Same pattern, a few special forms",
             "Possessives, demonstratives, question words and ordinal numbers follow the same rule as adjectives: "
             "one ending for masculine and neuter, another for feminine. The only surprises are that мой, твой and "
             "чей take the stressed ending -ём in the masculine and neuter. Его', её and их never change. Remember "
             "the spelling rule: after ш the ending is -ем/-ей, since it is unstressed.",
             tables=[table(
                 ["Word", "Masculine / neuter", "Feminine"],
                 [["мой · твой", "о мо{ём} · о тво{ём}", "о мо{е'й} · о тво{е'й}"],
                  ["наш · ваш", "о на'ш{ем} · о ва'ш{ем}", "о на'ш{ей} · о ва'ш{ей}"],
                  ["э'тот", "об э'т{ом}", "об э'т{ой}"],
                  ["тот", "о т{ом}", "о т{ой}"],
                  ["како'й", "в как{о'м}", "в как{о'й}"],
                  ["чей", "о чь{ём}", "о чь{ей}"]])]),
        card("Ordinal numbers",
             "Ordinals are adjectives, so they work the same way. They are what you use for floors: на пе'рвом "
             "этаже', на второ'м этаже', на тре'тьем этаже'. Тре'тий is a soft-stem adjective, so it takes -ьем and "
             "-ьей.",
             tables=[table(
                 ["Ordinal", "Masculine / neuter", "Feminine"],
                 [["пе'рвый", "на пе'рв{ом} этаже'", "в пе'рв{ой} кни'ге"],
                  ["второ'й", "на втор{о'м} этаже'", "во втор{о'й} кни'ге"],
                  ["тре'тий", "на тре'ть{ем} этаже'", "в тре'ть{ей} кни'ге"]])],
             examples=[
                 ex("Он ду'мает о твоём бра'те.", "He is thinking about your brother.", "о твоём бра'те"),
                 ex("Мы говори'м о мое'й сестре'.", "We are talking about my sister.", "о мое'й сестре'"),
                 ex("Мы живём в на'шем до'ме на пе'рвом этаже'.", "We live in our house on the first floor.", "на пе'рвом этаже'"),
                 ex("В како'м го'роде ты живёшь?", "In which city do you live?", "В како'м го'роде"),
                 ex("Об э'той кни'ге говоря'т все.", "Everyone is talking about this book.", "Об э'той кни'ге"),
             ]),
    ],
    verify=(vf("мой", "моём", "моей") + vf("твой", "твоём", "твоей") + vf("наш", "нашем", "нашей")
            + vf("ваш", "вашем", "вашей") + vf("этот", "этом", "этой") + vf("тот", "том", "той")
            + vf("какой", "каком", "какой") + vf("чей", "чьём", "чьей") + vf("первый", "первом", "первой")
            + vf("второй", "втором", "второй") + vf("третий", "третьем", "третьей") + vf("этаж", "этаже")),
    exercises=[
        fb("Он живёт в ___ до'ме.", ["на'шем", "на'шей", "наш", "на'шего"], "на'шем",
           "Masculine prepositional of наш: -ем (unstressed, after ш).", tr="He lives in our house.", lemma="наш"),
        fb("Мы говори'м о ___ сестре'.", ["мое'й", "моём", "моя'", "мою'"], "мое'й",
           "Feminine prepositional of мой: -ей.", tr="We are talking about my sister.", lemma="мой"),
        fb("Он ду'мает о ___ бра'те.", ["твоём", "твое'й", "твой", "твоего'"], "твоём",
           "Masculine prepositional of твой: -ём.", tr="He is thinking about your brother.", lemma="твой"),
        fb("В ___ го'роде ты живёшь?", ["како'м", "како'й", "како'е", "како'го"], "како'м",
           "Masculine prepositional of како'й: -ом.", tr="In which city do you live?", lemma="какой"),
        fb("Мы живём на ___ этаже'.", ["тре'тьем", "тре'тьей", "тре'тий", "тре'тье"], "тре'тьем",
           "Этаж is masculine: тре'тьем.", tr="We live on the third floor.", lemma="третий"),
        fb("Об ___ кни'ге говоря'т все.", ["э'той", "э'том", "э'та", "э'ту"], "э'той",
           "Feminine prepositional of э'тот: -ой.", tr="Everyone is talking about this book.", lemma="этот"),
        fb("Он живёт на ___ этаже'.", ["пе'рвом", "пе'рвой", "пе'рвый", "пе'рвое"], "пе'рвом",
           "Masculine prepositional: -ом.", tr="He lives on the first floor.", lemma="первый"),
        mc("Which possessives never change in the prepositional?", ["его', её, их", "мой, твой, наш", "э'тот, тот", "како'й, чей"],
           "его', её, их", "Они' ду'мают о её сестре'.", order=True),
        mc("Which phrase means “about my brother”?",
           ["о моём бра'те", "о мое'й бра'те", "о мой бра'те", "о моего' бра'та"],
           "о моём бра'те", "Masculine мой takes -ём."),
        mc("What is special about мой, твой and чей in the masculine prepositional?",
           ["The ending is -ём", "The ending is -ом", "The ending is -ем", "They do not change"],
           "The ending is -ём", "Моём, твоём, чьём.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 61
L61 = lesson(
    "Flying and swimming: лета'ть, лете'ть, пла'вать, плыть",
    "Лета'ю ча'сто, лечу' сейча'с",
    requires=["летать", "лететь", "плавать", "самолёт", "океан"],
    cards=[
        card("Two more pairs of motion verbs",
             "Flying and swimming work exactly like walking (идти'/ходи'ть) and riding (е'хать/е'здить). The "
             "multidirectional verbs лета'ть and пла'вать describe habits, round trips, general ability, motion "
             "with no fixed direction, and negative commands. The unidirectional verbs лете'ть and плыть describe "
             "one trip in one direction: right now, with a destination, a planned trip, or a step in a sequence. "
             "Плыть is used for swimming, for sailing and for what a ship does.",
             tables=[table(
                 ["Person", "лета'ть (habit)", "лете'ть (one flight)"],
                 [["я", "лета'{ю}", "леч{у'}"],
                  ["ты", "лета'{ешь}", "лет{и'шь}"],
                  ["он · она' · оно'", "лета'{ет}", "лет{и'т}"],
                  ["мы", "лета'{ем}", "лет{и'м}"],
                  ["вы", "лета'{ете}", "лет{и'те}"],
                  ["они'", "лета'{ют}", "лет{я'т}"]],
                 note="Лете'ть belongs to the second family, and the я-form has the т → ч change. "
                      "Past: лета'л, лета'ла · лете'л, лете'ла."),
             table(
                 ["Person", "пла'вать (habit)", "плыть (one trip)"],
                 [["я", "пла'ва{ю}", "плы{ву'}"],
                  ["ты", "пла'ва{ешь}", "плы{вёшь}"],
                  ["он · она' · оно'", "пла'ва{ет}", "плы{вёт}"],
                  ["мы", "пла'ва{ем}", "плы{вём}"],
                  ["вы", "пла'ва{ете}", "плы{вёте}"],
                  ["они'", "пла'ва{ют}", "плы{ву'т}"]],
                 note="Past: пла'вал, пла'вала · плыл, плыла', плы'ли.")]),
        card("Which one?",
             "Use лета'ть and пла'вать for what you do often, for a trip you have already completed and returned "
             "from, for ability (Я не уме'ю пла'вать), and for negative commands (Не пла'вайте здесь!). Use лете'ть "
             "and плыть for now, for a destination, for a planned trip, and for a positive command (Плыви' сюда'!). "
             "Like идти', лете'ть also works figuratively for moving very fast: Вре'мя лети'т!",
             examples=[
                 ex("Я ча'сто лета'ю в Москву'.", "I often fly to Moscow.", "лета'ю"),
                 ex("Сейча'с она' лети'т в Москву'.", "Right now she is flying to Moscow.", "лети'т"),
                 ex("Ка'ждое у'тро он пла'вает в бассе'йне.", "Every morning he swims in the pool.", "пла'вает"),
                 ex("Смотри'! Ло'дка плывёт.", "Look! A boat is sailing by.", "плывёт"),
                 ex("В про'шлом году' мы лета'ли в Евро'пу.", "Last year we went to Europe by plane (and came back).", "лета'ли"),
                 ex("Не пла'вайте здесь! Э'то опа'сно.", "Don't swim here! It's dangerous.", "Не пла'вайте"),
                 ex("Вре'мя лети'т.", "Time flies.", "лети'т"),
             ]),
    ],
    verify=(vf("летать", "летаю", "летаешь", "летает", "летаем", "летаете", "летают", "летал", "летала", "летали")
            + vf("лететь", "лечу", "летишь", "летит", "летим", "летите", "летят", "летел", "летела")
            + vf("плавать", "плаваю", "плаваешь", "плавает", "плаваем", "плаваете", "плавают", "плавал", "плавала", "плавайте")
            + vf("плыть", "плыву", "плывёшь", "плывёт", "плывём", "плывёте", "плывут", "плыл", "плыла", "плыли")),
    exercises=[
        fb("Ка'ждое у'тро он ___ в бассе'йне.", ["пла'вает", "плывёт", "пла'ваю", "плывёшь"], "пла'вает",
           "A daily habit: пла'вать.", tr="Every morning he swims in the pool.", lemma="плавать"),
        fb("Смотри'! Ло'дка ___.", ["плывёт", "пла'вает", "пла'вают", "плыву'"], "плывёт",
           "Happening right now, in one direction: плыть.", tr="Look! A boat is sailing by.", lemma="плыть"),
        fb("Я ча'сто ___ в Москву'.", ["лета'ю", "лечу'", "лети'м", "лета'ть"], "лета'ю",
           "Often = a habit: лета'ть.", tr="I often fly to Moscow.", lemma="летать"),
        fb("Сейча'с мы ___ в Москву' на самолёте.", ["лети'м", "лета'ем", "лета'ю", "лета'ют"], "лети'м",
           "Right now, one direction: лете'ть.", tr="Right now we are flying to Moscow.", lemma="лететь"),
        fb("Вре'мя ___.", ["лети'т", "лета'ет", "лета'ть", "лечу'"], "лети'т",
           "The figurative “time flies” uses лете'ть.", tr="Time flies.", lemma="лететь"),
        fb("В про'шлом году' мы ___ в Евро'пу.", ["лета'ли", "лета'ем", "лета'ю", "лете'ть"], "лета'ли",
           "A round trip in the past: лета'л.", tr="Last year we went to Europe by plane.", lemma="летать"),
        fb("Я не уме'ю ___.", ["пла'вать", "плыть", "плыву'", "пла'ваю"], "пла'вать",
           "Ability in general: пла'вать.", tr="I can't swim."),
        fb("___ здесь! Э'то опа'сно.", ["Не пла'вайте", "Не плыви'те", "Не пла'ваете", "Не плывёте"], "Не пла'вайте",
           "A negative command uses the multidirectional verb.", tr="Don't swim here! It's dangerous."),
        mc("Which pair means “to fly”?", ["лета'ть / лете'ть", "пла'вать / плыть", "ходи'ть / идти'", "е'здить / е'хать"],
           "лета'ть / лете'ть", "Лета'ть (habit) and лете'ть (one trip).", order=True),
        mc("Which sentence means “Tomorrow he is flying to Moscow”?",
           ["За'втра он лети'т в Москву'.", "За'втра он лета'ет в Москву'.", "За'втра он лета'л в Москву'.", "За'втра он лета'ть в Москву'."],
           "За'втра он лети'т в Москву'.", "A planned trip in one direction uses лете'ть."),
    ],
)

# ---------------------------------------------------------------------------- 62
L62 = lesson(
    "What time is it? Hours and minutes",
    "Сейча'с пять часо'в двадцать мину'т",
    requires=["час", "минута", "время", "который", "сейчас"],
    cards=[
        card("Hour: час, часа', часо'в",
             "To ask the time say Кото'рый час? and answer with a number and the word час. The word changes with "
             "the number: оди'н час for 1, then часа' for 2, 3 and 4, then часо'в for 5 and up. (Часа' and "
             "часо'в are the genitive forms, which you will study later. For now just learn the pattern.)",
             tables=[table(
                 ["Number", "Word", "Example"],
                 [["1", "час", "оди'н час"],
                  ["2 · 3 · 4", "час{а'}", "два часа' · три часа' · четы'ре часа'"],
                  ["5 – 12", "час{о'в}", "пять часо'в · во'семь часо'в · двена'дцать часо'в"]])],
             examples=[
                 ex("Кото'рый час? — Сейча'с оди'н час.", "What time is it? — It's one o'clock.", "оди'н час"),
                 ex("Сейча'с два часа'.", "It's two o'clock.", "два часа'"),
                 ex("Сейча'с пять часо'в.", "It's five o'clock.", "пять часо'в"),
             ]),
        card("Minutes: мину'та, мину'ты, мину'т",
             "Minutes work the same way with three forms. One is мину'та (feminine, so одна' мину'та). Two, three "
             "and four use мину'ты (две мину'ты). Five and more use мину'т. With long numbers only the last word "
             "counts, so 21 uses мину'та and 22 uses мину'ты. The teens are the exception: 11 to 19 always take "
             "мину'т, whatever the last digit.",
             tables=[table(
                 ["Number", "Hours", "Minutes"],
                 [["1", "оди'н час", "одна' мину'та"],
                  ["2", "два часа'", "две мину'ты"],
                  ["3 · 4", "три · четы'ре часа'", "три · четы'ре мину'ты"],
                  ["5 – 20", "пять часо'в", "пять мину'т"],
                  ["21", "два'дцать оди'н час", "два'дцать одна' мину'та"],
                  ["22", "два'дцать два часа'", "два'дцать две мину'ты"],
                  ["25", "два'дцать пять часо'в", "два'дцать пять мину'т"]])],
             examples=[
                 ex("Сейча'с шесть часо'в две мину'ты.", "It's two minutes past six.", "две мину'ты"),
                 ex("Сейча'с семь часо'в пятна'дцать мину'т.", "It's seven fifteen.", "пятна'дцать мину'т"),
                 ex("Сейча'с де'вять часо'в два'дцать одна' мину'та.", "It's 9:21.", "одна' мину'та"),
             ]),
    ],
    verify=(vf("час", "часа", "часов", "часы") + vf("минута", "минуты", "минут", "минуту")),
    exercises=[
        fb("Сейча'с два ___.", ["часа'", "час", "часо'в", "часы'"], "часа'",
           "After 2, 3 and 4: часа'.", tr="It's two o'clock.", lemma="час"),
        fb("Сейча'с пять ___.", ["часо'в", "часа'", "час", "часы'"], "часо'в",
           "After 5 and up: часо'в.", tr="It's five o'clock.", lemma="час"),
        fb("Сейча'с оди'н ___.", ["час", "часа'", "часо'в", "часы'"], "час",
           "After 1: час.", tr="It's one o'clock.", lemma="час"),
        fb("Сейча'с три ___.", ["часа'", "часо'в", "час", "часы'"], "часа'",
           "After 3: часа'.", tr="It's three o'clock.", lemma="час"),
        fb("Сейча'с шесть часо'в две ___.", ["мину'ты", "мину'та", "мину'т", "мину'ту"], "мину'ты",
           "After 2, 3 and 4: мину'ты.", tr="It's two minutes past six.", lemma="минута"),
        fb("Сейча'с семь часо'в пять ___.", ["мину'т", "мину'ты", "мину'та", "мину'ту"], "мину'т",
           "After 5 and up: мину'т.", tr="It's five past seven.", lemma="минута"),
        fb("Сейча'с де'вять часо'в два'дцать одна' ___.", ["мину'та", "мину'ты", "мину'т", "мину'ту"], "мину'та",
           "Only the last word counts: одна' → мину'та.", tr="It's 9:21.", lemma="минута"),
        mc("What does Кото'рый час? ask?", ["What time is it?", "At what time?", "What day is it?", "How long?"],
           "What time is it?", "Кото'рый час? asks the time right now.", order=True),
        mc("Which is correct for 21 minutes?",
           ["два'дцать одна' мину'та", "два'дцать одна' мину'ты", "два'дцать одна' мину'т", "два'дцать одну' мину'ту"],
           "два'дцать одна' мину'та", "The last digit is 1: мину'та."),
        mc("Which is correct for 14 minutes?",
           ["четы'рнадцать мину'т", "четы'рнадцать мину'ты", "четы'рнадцать мину'та", "четы'рнадцать мину'ту"],
           "четы'рнадцать мину'т", "The teens always take мину'т."),
    ],
)

# ---------------------------------------------------------------------------- 63
L63 = lesson(
    "At what time? Во ско'лько?",
    "В шесть часо'в утра', в час дня",
    requires=["час", "утро", "вечер", "ночь", "день"],
    cards=[
        card("At a certain time: в + hour",
             "To ask at what time something happens, say Во ско'лько? (informal) or В кото'ром часу'? (formal). "
             "Answer with в and the hour: в два часа', в пять часо'в. For one o'clock say simply в час.",
             examples=[
                 ex("Во ско'лько ты встаёшь? — В семь часо'в.", "What time do you get up? — At seven.", "В семь часо'в"),
                 ex("Наш самолёт в шесть часо'в.", "Our plane is at six o'clock.", "в шесть часо'в"),
                 ex("Мы обе'даем в час.", "We have lunch at one.", "в час"),
             ]),
        card("Morning, day, evening, night",
             "Russian has no a.m. or p.m. Instead you add a word for the part of the day, always in the same "
             "fixed form: утра' (in the morning), дня (in the afternoon), ве'чера (in the evening), но'чи (at "
             "night). Roughly: утра' is up to noon, дня is the afternoon, ве'чера is the evening and но'чи is the "
             "small hours. Without a clock time, use the single words у'тром, днём, ве'чером and но'чью.",
             tables=[table(
                 ["Part of day", "With a clock time", "Without one"],
                 [["morning", "в шесть часо'в утра'", "у'тром"],
                  ["afternoon", "в час дня · в три часа' дня", "днём"],
                  ["evening", "в семь часо'в ве'чера", "ве'чером"],
                  ["night", "в час но'чи · в три часа' но'чи", "но'чью"]])],
             examples=[
                 ex("Я встаю' в шесть часо'в утра'.", "I get up at six in the morning.", "утра'"),
                 ex("Мы обе'даем в час дня.", "We have lunch at one in the afternoon.", "дня"),
                 ex("Фильм в оди'ннадцать часо'в ве'чера.", "The film is at eleven at night.", "ве'чера"),
                 ex("В час но'чи мы бы'ли в аэропорту'.", "At one in the morning we were at the airport.", "но'чи"),
                 ex("У'тром я чита'ю, а ве'чером отдыха'ю.", "In the morning I read, and in the evening I relax.", "У'тром"),
             ]),
    ],
    verify=(vf("утро", "утра", "утром") + vf("день", "дня", "днём") + vf("вечер", "вечера", "вечером")
            + vf("ночь", "ночи", "ночью") + vf("час", "час", "часа", "часов")),
    exercises=[
        fb("Он встаёт в шесть часо'в ___.", ["утра'", "у'тро", "утру'", "утры'"], "утра'",
           "Fixed form for “a.m.”: утра'.", tr="He gets up at six in the morning.", lemma="утро"),
        fb("Мы обе'даем в час ___.", ["дня", "день", "дню", "дни"], "дня",
           "Fixed form for the afternoon: дня.", tr="We have lunch at one in the afternoon.", lemma="день"),
        fb("Фильм в де'вять часо'в ___.", ["ве'чера", "ве'чер", "ве'черу", "ве'чере"], "ве'чера",
           "Fixed form for the evening: ве'чера.", tr="The film is at nine in the evening.", lemma="вечер"),
        fb("Самолёт в три часа' ___.", ["но'чи", "ночь", "но'чу", "ноч"], "но'чи",
           "Fixed form for the small hours: но'чи.", tr="The plane is at three in the night.", lemma="ночь"),
        fb("___ ты встаёшь? — В семь часо'в.", ["Во ско'лько", "Кото'рый час", "Ско'лько часо'в", "Где"], "Во ско'лько",
           "Во ско'лько? asks at what time.", tr="What time do you get up? — At seven."),
        fb("Наш самолёт ___ шесть часо'в.", ["в", "на", "к", "о"], "в",
           "At a clock time: в + hour.", tr="Our plane is at six o'clock."),
        fb("Мы бы'ли в аэропорту' в ___ но'чи.", ["час", "часа'", "часо'в", "часы'"], "час",
           "At one o'clock: в час.", tr="We were at the airport at one at night.", lemma="час"),
        mc("Which phrase means “at 1 p.m.”?", ["в час дня", "в часа' дня", "в часо'в дня", "в часы' дня"],
           "в час дня", "For one o'clock: в час."),
        mc("Which word goes with “at 1 a.m.”, в час ___?", ["но'чи", "утра'", "дня", "ве'чера"], "но'чи",
           "The small hours take но'чи.", order=True),
        mc("Which word means “in the morning” without a clock time?", ["у'тром", "утра'", "у'тро", "утру'"], "у'тром",
           "У'тром, днём, ве'чером, но'чью."),
    ],
)

# ---------------------------------------------------------------------------- 64
L64 = lesson(
    "Playing and tickets: в or на?",
    "Игра'ть в футбо'л, игра'ть на гита'ре, биле'т на конце'рт",
    requires=["играть", "игра", "билет", "футбол", "театр"],
    cards=[
        card("Play a game, play an instrument",
             "With игра'ть the preposition depends on what you play. For sports and games use в plus the "
             "accusative: игра'ть в футбо'л. For musical instruments use на plus the prepositional: игра'ть на "
             "гита'ре. Some instrument names never change, such as пиани'но.",
             tables=[table(
                 ["Games (в + accusative)", "Instruments (на + prepositional)"],
                 [["в футбо'л", "на гита'р{е}"],
                  ["в баскетбо'л", "на скри'пк{е}"],
                  ["в волейбо'л", "на саксофо'н{е}"],
                  ["в те'ннис", "на аккордео'н{е}"],
                  ["в ша'хматы", "на пиани'но"],
                  ["в америка'нский футбо'л", "на роя'л{е}"]])],
             examples=[
                 ex("Мой брат игра'ет в футбо'л.", "My brother plays football.", "в футбо'л"),
                 ex("Моя' сестра' игра'ет на гита'ре.", "My sister plays the guitar.", "на гита'ре"),
                 ex("Мы ча'сто игра'ем в баскетбо'л.", "We often play basketball.", "в баскетбо'л"),
                 ex("Я уме'ю игра'ть на саксофо'не, но не уме'ю игра'ть в америка'нский футбо'л.",
                    "I can play the saxophone, but I can't play American football.", "на саксофо'не"),
             ]),
        card("A ticket to…",
             "Биле'т is followed by в or на and then the accusative. Use в for a ticket to a place, such as a "
             "theater, a museum, a city or a country. Use на for a ticket to an event or a means of transport: a "
             "concert, a game, a lecture, a film, a ballet, a train, a plane.",
             tables=[table(
                 ["Place (в + accusative)", "Event or transport (на + accusative)"],
                 [["биле'т в теа'тр", "биле'т на конце'рт"],
                  ["биле'т в музе'й", "биле'т на футбо'л"],
                  ["биле'т в Москву'", "биле'т на по'езд"],
                  ["биле'ты в кино'", "биле'ты на самолёт"]])],
             examples=[
                 ex("Ты уже' купи'л биле'ты в теа'тр?", "Have you already bought the theater tickets?", "в теа'тр"),
                 ex("Нет, но я купи'л биле'ты в музе'й.", "No, but I bought the museum tickets.", "в музе'й"),
                 ex("Где твой биле'т на по'езд?", "Where is your train ticket?", "на по'езд"),
                 ex("Вот твой биле'т на бале'т, а где мой биле'т на футбо'л?",
                    "Here is your ticket to the ballet, but where is my ticket to the football game?", "на бале'т"),
             ]),
    ],
    verify=(vf("гитара", "гитаре") + vf("скрипка", "скрипке") + vf("саксофон", "саксофоне")
            + vf("аккордеон", "аккордеоне") + vf("рояль", "рояле") + vf("билет", "билет", "билеты")),
    exercises=[
        fb("Мой брат игра'ет ___ футбо'л.", ["в", "на", "о", "к"], "в",
           "Games take в + accusative.", tr="My brother plays football."),
        fb("Моя' сестра' игра'ет ___ гита'ре.", ["на", "в", "с", "у"], "на",
           "Instruments take на + prepositional.", tr="My sister plays the guitar."),
        fb("Мы ча'сто игра'ем в ___.", ["баскетбо'л", "баскетбо'ле", "баскетбо'ла", "баскетбо'лу"], "баскетбо'л",
           "After в for games: accusative, which here looks like the nominative.", tr="We often play basketball.", lemma="баскетбол"),
        fb("Она' хорошо' игра'ет на ___.", ["скри'пке", "скри'пку", "скри'пка", "скри'пки"], "скри'пке",
           "After на for instruments: prepositional.", tr="She plays the violin well.", lemma="скрипка"),
        fb("Он уме'ет игра'ть на ___.", ["саксофо'не", "саксофо'н", "саксофо'на", "саксофо'ну"], "саксофо'не",
           "After на for instruments: prepositional.", tr="He can play the saxophone.", lemma="саксофон"),
        fb("Ты уже' купи'л биле'т ___ теа'тр?", ["в", "на", "о", "у"], "в",
           "A ticket to a place: в.", tr="Have you already bought a ticket to the theater?"),
        fb("Где твой биле'т ___ по'езд?", ["на", "в", "к", "из"], "на",
           "A ticket for transport: на.", tr="Where is your train ticket?"),
        fb("Мы купи'ли биле'ты на ___.", ["конце'рт", "конце'рте", "конце'рта", "конце'рту"], "конце'рт",
           "After на in “ticket to”: accusative.", tr="We bought tickets to the concert.", lemma="концерт"),
        mc("Which preposition goes with a musical instrument?", ["на", "в", "о", "из"], "на",
           "Игра'ть на гита'ре.", order=True),
        mc("Which sentence means “He plays the guitar”?",
           ["Он игра'ет на гита'ре.", "Он игра'ет в гита'ру.", "Он игра'ет на гита'ру.", "Он игра'ет в гита'ре."],
           "Он игра'ет на гита'ре.", "Instrument: на + prepositional."),
        mc("Which phrase means “a ticket to the museum”?",
           ["биле'т в музе'й", "биле'т на музе'й", "биле'т в музе'е", "биле'т на музе'е"],
           "биле'т в музе'й", "A place: в + accusative."),
    ],
)

# ---------------------------------------------------------------------------- 65
L65 = lesson(
    "Review: describing, flying, time and playing",
    "Putting lessons 58 to 64 together",
    requires=["красивый", "большой", "самолёт", "час", "играть"],
    cards=[
        card("What you can do now",
             "You can describe where something is with adjectives in the prepositional (-ом, -ой, -ем, -ей), "
             "decline мой, наш, э'тот, како'й and the ordinals, choose between лета'ть and лете'ть or пла'вать "
             "and плыть, tell the time with час and мину'та, say at what time something happens, and use the "
             "right preposition with игра'ть and биле'т.",
             tables=[table(
                 ["Topic", "Remember"],
                 [["Adjectives", "-ом (m, n) · -ой (f) · -ем / -ей after soft stems and unstressed ш ж ч щ"],
                  ["мой, твой, чей", "моём · мое'й · твоём · чьём"],
                  ["Time", "оди'н час · два часа' · пять часо'в"],
                  ["At what time?", "в шесть часо'в утра' · в час дня"],
                  ["Playing", "игра'ть в футбо'л · игра'ть на гита'ре"]])],
             examples=[
                 ex("Мы живём в большо'м краси'вом до'ме на тре'тьем этаже'.", "We live in a big beautiful house on the third floor.", "в большо'м краси'вом до'ме"),
                 ex("Во ско'лько ты лети'шь? — В шесть часо'в утра'.", "What time are you flying? — At six in the morning.", "В шесть часо'в утра'"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("Мы живём в ___ до'ме.", ["большо'м", "большо'й", "бо'льшем", "большо'го"], "большо'м",
           "Stressed -ом after щ.", tr="We live in a big house.", lemma="большой"),
        fb("Она' рабо'тает в ___ шко'ле.", ["хоро'шей", "хоро'шой", "хоро'шем", "хоро'шая"], "хоро'шей",
           "Feminine, unstressed after ш: -ей.", tr="She works in a good school.", lemma="хороший"),
        fb("Они' говоря'т о ___ сестре'.", ["на'шей", "на'шем", "наша", "нашу"], "на'шей",
           "Feminine prepositional of наш: -ей.", tr="They are talking about our sister.", lemma="наш"),
        fb("Мы живём на ___ этаже'.", ["пе'рвом", "пе'рвой", "пе'рвый", "пе'рвое"], "пе'рвом",
           "Этаж is masculine: -ом.", tr="We live on the first floor.", lemma="первый"),
        fb("Сейча'с четы'ре ___.", ["часа'", "часо'в", "час", "часы'"], "часа'",
           "After 4: часа'.", tr="It's four o'clock.", lemma="час"),
        fb("Сейча'с де'сять часо'в три ___.", ["мину'ты", "мину'т", "мину'та", "мину'ту"], "мину'ты",
           "After 3: мину'ты.", tr="It's three minutes past ten.", lemma="минута"),
        fb("Самолёт в оди'ннадцать часо'в ___.", ["ве'чера", "утра'", "ве'чер", "но'чью"], "ве'чера",
           "Eleven in the evening: ве'чера.", tr="The plane is at eleven in the evening."),
        fb("Сейча'с он ___ в Москву' на самолёте.", ["лети'т", "лета'ет", "лета'ть", "лечу'"], "лети'т",
           "Now, one direction: лете'ть.", tr="Right now he is flying to Moscow.", lemma="лететь"),
        fb("Ка'ждое у'тро она' ___ в бассе'йне.", ["пла'вает", "плывёт", "пла'вают", "плывёшь"], "пла'вает",
           "A habit: пла'вать.", tr="Every morning she swims in the pool.", lemma="плавать"),
        fb("Мой друг игра'ет ___ гита'ре.", ["на", "в", "о", "с"], "на",
           "Instrument: на + prepositional.", tr="My friend plays the guitar."),
        fb("Где биле'ты ___ конце'рт?", ["на", "в", "к", "о"], "на",
           "A ticket to an event: на.", tr="Where are the concert tickets?"),
        mc("Which phrase means “in a new room”?",
           ["в но'вой ко'мнате", "в но'вом ко'мнате", "в но'вая ко'мнату", "в но'вую ко'мнате"],
           "в но'вой ко'мнате", "Feminine prepositional: -ой."),
    ],
)

UNIT = unit("Unit 9: Describing, flying and telling time",
            [L58, L59, L60, L61, L62, L63, L64, L65])
