"""Unit 3: describing, locating, and the first verbs  (textbook lessons 5-6)."""
from dsl import *

# ---------------------------------------------------------------------------- 13
L13 = lesson(
    "Adjectives agree with their noun",
    "Но'вый дом, но'вая кни'га, но'вое окно', но'вые кни'ги",
    requires=["новый", "старый", "красный", "интересный", "какой"],
    cards=[
        card("Gender and number",
             "An adjective describes a noun, and it takes that noun's gender and number. The question words show "
             "the four forms: Како'й? (masculine), Кака'я? (feminine), Како'е? (neuter), Каки'е? (plural). "
             "The ending tells you which noun it belongs to. Later it will also match the noun's case.",
             tables=[table(
                 ["", "Masculine", "Feminine", "Neuter", "Plural"],
                 [["new", "но'в{ый}", "но'в{ая}", "но'в{ое}", "но'в{ые}"],
                  ["old", "ста'р{ый}", "ста'р{ая}", "ста'р{ое}", "ста'р{ые}"],
                  ["red", "кра'сн{ый}", "кра'сн{ая}", "кра'сн{ое}", "кра'сн{ые}"],
                  ["interesting", "интере'сн{ый}", "интере'сн{ая}", "интере'сн{ое}", "интере'сн{ые}"]])]),
        card("Before the noun, or after it",
             "An adjective can stand before its noun (но'вый дом) or describe it afterwards, with no verb in "
             "between (Дом но'вый). Either way it matches the noun.",
             examples=[
                 ex("но'вый дом", "a new house", "но'вый"),
                 ex("но'вая кни'га", "a new book", "но'вая"),
                 ex("но'вое окно'", "a new window", "но'вое"),
                 ex("но'вые кни'ги", "new books", "но'вые"),
                 ex("Дом ста'рый.", "The house is old.", "ста'рый"),
                 ex("Кни'га ста'рая.", "The book is old.", "ста'рая"),
             ]),
    ],
    verify=[("новый", "новая"), ("новый", "новое"), ("новый", "новые"),
            ("старый", "старая"), ("старый", "старое"), ("старый", "старые"),
            ("красный", "красная"), ("красный", "красное"), ("красный", "красные"),
            ("интересный", "интересная"), ("интересный", "интересное"), ("интересный", "интересные")],
    exercises=[
        fb("Э'то ___ дом.", ["но'вый", "но'вая", "но'вое", "но'вые"], "но'вый",
           "Дом is masculine.", tr="This is a new house."),
        fb("Э'то ___ кни'га.", ["но'вая", "но'вый", "но'вое", "но'вые"], "но'вая",
           "Кни'га is feminine.", tr="This is a new book."),
        fb("Э'то ___ окно'.", ["но'вое", "но'вый", "но'вая", "но'вые"], "но'вое",
           "Окно' is neuter.", tr="This is a new window."),
        fb("Э'то ___ кни'ги.", ["но'вые", "но'вый", "но'вая", "но'вое"], "но'вые",
           "Кни'ги is plural.", tr="These are new books."),
        fb("Дом ___.", ["ста'рый", "ста'рая", "ста'рое", "ста'рые"], "ста'рый",
           "Дом is masculine, so the description is too.", tr="The house is old."),
        fb("Маши'на ___.", ["но'вая", "но'вый", "но'вое", "но'вые"], "но'вая",
           "Маши'на (car) is feminine.", tr="The car is new."),
        fb("Письмо' ___.", ["интере'сное", "интере'сный", "интере'сная", "интере'сные"], "интере'сное",
           "Письмо' (letter) is neuter.", tr="The letter is interesting."),
        fb("Журна'лы ___.", ["интере'сные", "интере'сный", "интере'сная", "интере'сное"], "интере'сные",
           "Журна'лы is plural, whatever the gender of журна'л.", tr="The magazines are interesting."),
        mc("Which question word goes with a feminine noun?",
           ["Кака'я?", "Како'й?", "Како'е?", "Каки'е?"], "Кака'я?",
           "Како'й is masculine, кака'я feminine, како'е neuter, каки'е plural."),
        mc("Which adjective goes with ко'мната (room)?",
           ["кра'сная", "кра'сный", "кра'сное", "кра'сные"], "кра'сная",
           "Ко'мната ends in -а: feminine."),
    ],
)

# ---------------------------------------------------------------------------- 14
L14 = lesson(
    "Adjective endings: soft stems, spelling, stress",
    "Си'ний, ру'сский, хоро'ший, большо'й",
    requires=["большой", "маленький", "русский", "хороший", "синий", "молодой", "какой"],
    cards=[
        card("Three groups change the ending",
             "Most adjectives are like но'вый. Three groups differ. A soft stem (си'ний, blue) takes -ий, -яя, "
             "-ее, -ие. After г, к, х the masculine is -ий, not -ый, and the plural -ие: this is the spelling "
             "rule you met with plurals. After ж, ш, ч, щ the same happens, and an unstressed neuter ending "
             "is -ее, not -ое. Tap a row to hear it.",
             tables=[table(
                 ["Type", "Masculine", "Feminine", "Neuter", "Plural"],
                 [["hard stem", "но'в{ый}", "но'в{ая}", "но'в{ое}", "но'в{ые}"],
                  ["soft stem", "си'н{ий}", "си'н{яя}", "си'н{ее}", "си'н{ие}"],
                  ["after г, к, х", "ру'сск{ий}", "ру'сск{ая}", "ру'сск{ое}", "ру'сск{ие}"],
                  ["after ж, ш, ч, щ", "хоро'ш{ий}", "хоро'ш{ая}", "хоро'ш{ее}", "хоро'ш{ие}"]])]),
        card("When the ending is stressed",
             "If the stress falls on the ending, the masculine ends in -о'й instead of -ый or -ий, and the other "
             "forms are -а'я, -о'е, -ы'е. After к and ш the plural is still -и'е, by the spelling rule. The "
             "words большо'й, како'й and молодо'й are all in this group.",
             tables=[table(
                 ["Masculine", "Feminine", "Neuter", "Plural"],
                 [["молод{о'й}", "молод{а'я}", "молод{о'е}", "молод{ы'е}"],
                  ["больш{о'й}", "больш{а'я}", "больш{о'е}", "больш{и'е}"],
                  ["как{о'й}", "как{а'я}", "как{о'е}", "как{и'е}"]])]),
    ],
    verify=[("синий", "синяя"), ("синий", "синее"), ("синий", "синие"),
            ("русский", "русская"), ("русский", "русское"), ("русский", "русские"),
            ("хороший", "хорошая"), ("хороший", "хорошее"), ("хороший", "хорошие"),
            ("молодой", "молодая"), ("молодой", "молодое"), ("молодой", "молодые"),
            ("большой", "большая"), ("большой", "большое"), ("большой", "большие"),
            ("какой", "какая"), ("какой", "какое"), ("какой", "какие"),
            ("маленький", "маленькая"), ("маленький", "маленькое"), ("маленький", "маленькие")],
    exercises=[
        fb("Э'то ___ дом.", ["большо'й", "больша'я", "большо'е", "больши'е"], "большо'й",
           "Дом is masculine, and the stress is on the ending: большо'й.", tr="This is a big house."),
        fb("Э'то ___ шко'ла.", ["больша'я", "большо'й", "большо'е", "больши'е"], "больша'я",
           "Шко'ла is feminine: больша'я.", tr="This is a big school."),
        fb("Э'то ___ окно'.", ["ма'ленькое", "ма'ленький", "ма'ленькая", "ма'ленькие"], "ма'ленькое",
           "Окно' is neuter. After к the ending is still -ое when unstressed.", tr="This is a small window."),
        fb("Э'то ___ де'ти.", ["ма'ленькие", "ма'ленький", "ма'ленькая", "ма'ленькое"], "ма'ленькие",
           "Plural, after к: -ие.", tr="These are small children."),
        fb("Э'то ___ кни'га.", ["ру'сская", "ру'сский", "ру'сское", "ру'сские"], "ру'сская",
           "Кни'га is feminine.", tr="This is a Russian book."),
        fb("Э'то ___ окно'.", ["хоро'шее", "хоро'шая", "хоро'ший", "хоро'шие"], "хоро'шее",
           "After ш an unstressed neuter ending is -ее.", tr="This is a good window."),
        fb("Э'то ___ мо'ре.", ["си'нее", "си'ний", "си'няя", "си'ние"], "си'нее",
           "Мо'ре is neuter, and a soft stem gives -ее.", tr="This is a blue sea."),
        fb("Э'то ___ челове'к.", ["молодо'й", "молода'я", "молодо'е", "молоды'е"], "молодо'й",
           "Челове'к is masculine, and the ending is stressed: молодо'й.", tr="This is a young man."),
        mc("Why is it хоро'шее and not хоро'шое?",
           ["After ж, ш, ч, щ an unstressed neuter ending is -ее", "Because хоро'ший is a plural form",
            "Because the stress is on the ending", "It is an exception with no rule"],
           "After ж, ш, ч, щ an unstressed neuter ending is -ее",
           "It is a spelling rule. When the ending is stressed it stays -ое, as in большо'е."),
        mc("Which masculine ending shows that the stress is on the ending?",
           ["-о'й", "-ый", "-ий", "-ая"], "-о'й",
           "Большо'й, како'й, молодо'й: stressed -о'й."),
    ],
)

# ---------------------------------------------------------------------------- 15
L15 = lesson(
    "Ordinal numbers",
    "Пе'рвый, второ'й, тре'тий…",
    requires=["первый", "второй", "третий", "четвёртый", "пятый", "урок"],
    cards=[
        card("First, second, third",
             "Ordinal numbers are adjectives: they agree with their noun in gender and number, and later in "
             "case. Most behave like но'вый. Второ'й has a stressed ending. Тре'тий is a soft adjective with its "
             "own forms.",
             tables=[table(
                 ["", "Masculine", "Feminine", "Neuter", "Plural"],
                 [["1st", "пе'рв{ый}", "пе'рв{ая}", "пе'рв{ое}", "пе'рв{ые}"],
                  ["2nd", "втор{о'й}", "втор{а'я}", "втор{о'е}", "втор{ы'е}"],
                  ["3rd", "тре'т{ий}", "тре'т{ья}", "тре'т{ье}", "тре'т{ьи}"]])],
             examples=[
                 ex("пе'рвый уро'к", "the first lesson", "пе'рвый"),
                 ex("втора'я кни'га", "the second book", "втора'я"),
                 ex("тре'тье сло'во", "the third word", "тре'тье"),
                 ex("пе'рвые уро'ки", "the first lessons", "пе'рвые"),
             ]),
        card("Fourth to tenth",
             "From four on, the ordinals are formed from the number. Four of them end in a stressed -о'й "
             "(второ'й, шесто'й, седьмо'й, восьмо'й) and take -а'я, -о'е, -ы'е. The others behave like но'вый.",
             tables=[table(
                 ["Number", "Masculine", "Feminine"],
                 [["4th", "четвёртый", "четвёртая"],
                  ["5th", "пя'тый", "пя'тая"],
                  ["6th", "шест{о'й}", "шест{а'я}"],
                  ["7th", "седьм{о'й}", "седьм{а'я}"],
                  ["8th", "восьм{о'й}", "восьм{а'я}"],
                  ["9th", "девя'тый", "девя'тая"],
                  ["10th", "деся'тый", "деся'тая"]])]),
    ],
    verify=[("первый", "первая"), ("первый", "первое"), ("первый", "первые"),
            ("второй", "вторая"), ("второй", "второе"), ("второй", "вторые"),
            ("третий", "третья"), ("третий", "третье"), ("третий", "третьи"),
            ("шестой", "шестая"), ("седьмой", "седьмая"), ("восьмой", "восьмая"),
            ("десятый", "десятая"), ("девятый", "девятая"), ("пятый", "пятая"),
            ("четвёртый", "четвёртая")],
    exercises=[
        fb("Э'то ___ уро'к.", ["пе'рвый", "пе'рвая", "пе'рвое", "пе'рвые"], "пе'рвый",
           "Уро'к is masculine.", tr="This is the first lesson."),
        fb("Э'то ___ кни'га.", ["втора'я", "второ'й", "второ'е", "вторы'е"], "втора'я",
           "Кни'га is feminine, and the stress is on the ending.", tr="This is the second book."),
        fb("Э'то ___ сло'во.", ["тре'тье", "тре'тий", "тре'тья", "тре'тьи"], "тре'тье",
           "Сло'во is neuter, and тре'тий has the soft forms тре'тья, тре'тье, тре'тьи.", tr="This is the third word."),
        fb("Э'то ___ уро'ки.", ["пе'рвые", "пе'рвый", "пе'рвая", "пе'рвое"], "пе'рвые",
           "Plural.", tr="These are the first lessons."),
        fb("Э'то ___ ко'мната.", ["шеста'я", "шесто'й", "шесто'е", "шесты'е"], "шеста'я",
           "Ко'мната is feminine: шеста'я.", tr="This is the sixth room."),
        mc("Which one is “fifth”?", ["пя'тый", "шесто'й", "четвёртый", "деся'тый"], "пя'тый",
           "Пять → пя'тый."),
        mc("Which one is “tenth”?", ["деся'тый", "девя'тый", "пя'тый", "восьмо'й"], "деся'тый",
           "Де'сять → деся'тый."),
        mc("Which one is “seventh”?", ["седьмо'й", "шесто'й", "восьмо'й", "девя'тый"], "седьмо'й",
           "Семь → седьмо'й."),
        mc("What is the feminine form of тре'тий?", ["тре'тья", "тре'тая", "тре'тяя", "тре'тие"], "тре'тья",
           "Тре'тий is a soft adjective with its own forms: тре'тья, тре'тье, тре'тьи."),
    ],
)

# ---------------------------------------------------------------------------- 16
L16 = lesson(
    "Where? The prepositional case",
    "В журна'ле, на окне', в тетра'ди: the ending that says “where”",
    requires=["школа", "комната", "работа", "город", "банк", "музей", "здание"],
    cards=[
        card("Saying where something is",
             "To say where something is, Russian uses the prepositional case. It answers Где? and always follows "
             "a preposition. For now, that means в (in) or на (on, at). The noun changes its ending: most take -е, "
             "and nouns in -ь, -ий, -ия, -ие take -и. Tap a row to hear it.",
             tables=[table(
                 ["Gender", "Nominative (Что?)", "Prepositional (Где?)", "Ending"],
                 [["masculine", "журна'л", "в журна'л{е}", "-е"],
                  ["masculine -ь", "слова'рь", "в словар{е'}", "-е"],
                  ["masculine -й", "музе'й", "в музе'{е}", "-е"],
                  ["masculine -ий", "планета'рий", "в планета'ри{и}", "-и"],
                  ["feminine -а", "газе'та", "в газе'т{е}", "-е"],
                  ["feminine -я", "земля'", "на земл{е'}", "-е"],
                  ["feminine -ь", "тетра'дь", "в тетра'д{и}", "-и"],
                  ["feminine -ия", "а'рмия", "в а'рми{и}", "-и"],
                  ["neuter -о", "окно'", "на окн{е'}", "-е"],
                  ["neuter -е", "мо'ре", "на мо'р{е}", "-е"],
                  ["neuter -ие", "зда'ние", "в зда'ни{и}", "-и"]])]),
        card("Where, not where to",
             "This case answers Где? (where is it?), not Куда'? (where is it going?). The stress often moves onto "
             "the ending (слова'рь → в словаре', окно' → на окне'). The prepositional is used only after a "
             "preposition, which is why it carries that name.",
             examples=[
                 ex("Ма'ма в шко'ле.", "Mom is at school.", "в шко'ле"),
                 ex("Де'ти в ко'мнате.", "The children are in the room.", "в ко'мнате"),
                 ex("Па'па на рабо'те.", "Dad is at work.", "на рабо'те"),
                 ex("Они' в го'роде.", "They are in town.", "в го'роде"),
             ]),
    ],
    verify=[("журнал", "журнале"), ("словарь", "словаре"), ("музей", "музее"),
            ("планетарий", "планетарии"), ("газета", "газете"), ("земля", "земле"),
            ("тетрадь", "тетради"), ("армия", "армии"), ("окно", "окне"), ("море", "море"),
            ("здание", "здании"), ("школа", "школе"), ("комната", "комнате"), ("работа", "работе"),
            ("город", "городе"), ("банк", "банке")],
    exercises=[
        fb("Ма'ма в ___.", ["шко'ле", "шко'ла", "шко'лу", "шко'лы"], "шко'ле",
           "Feminine -а takes -е in the prepositional.", tr="Mom is at school."),
        fb("Де'ти в ___.", ["ко'мнате", "ко'мната", "ко'мнату", "ко'мнаты"], "ко'мнате",
           "Feminine -а takes -е.", tr="The children are in the room."),
        fb("Па'па на ___.", ["рабо'те", "рабо'та", "рабо'ту", "рабо'ты"], "рабо'те",
           "Feminine -а takes -е.", tr="Dad is at work."),
        fb("Мы в ___.", ["го'роде", "го'род", "го'рода", "го'роду"], "го'роде",
           "A masculine noun ending in a consonant takes -е.", tr="We are in town."),
        fb("Па'па в ___.", ["ба'нке", "банк", "ба'нка", "ба'нку"], "ба'нке",
           "A masculine noun ending in a consonant takes -е.", tr="Dad is at the bank."),
        fb("Они' в ___.", ["музе'е", "музе'й", "музе'я", "музе'ю"], "музе'е",
           "Masculine -й is replaced by -е: музе'е.", tr="They are in the museum."),
        fb("Ру'чка в ___.", ["тетра'ди", "тетра'дь", "тетра'де", "тетра'дью"], "тетра'ди",
           "Feminine nouns in -ь take -и.", tr="The pen is in the notebook."),
        fb("Мы в ___.", ["зда'нии", "зда'ние", "зда'ния", "зда'нье"], "зда'нии",
           "Nouns in -ие take -ии.", tr="We are in the building."),
        fb("Они' на ___.", ["мо'ре", "мо'ря", "мо'ру", "мо'ри"], "мо'ре",
           "Neuter -е stays -е, so here the prepositional looks like the nominative.", tr="They are at the sea."),
        mc("Which question does the prepositional case answer here?",
           ["Где?", "Куда'?", "Кто?", "Чей?"], "Где?",
           "It states location. Where something is going uses a different case, which comes later."),
    ],
)

# ---------------------------------------------------------------------------- 17
L17 = lesson(
    "В or на?",
    "Which preposition goes with which place",
    requires=["школа", "комната", "улица", "почта", "вокзал", "кухня", "двор"],
    cards=[
        card("The general idea",
             "В (in) goes with enclosed spaces that have clear borders: rooms, buildings, towns, countries. На "
             "(on, at) goes with surfaces, open areas and events. Both take the prepositional case when they "
             "answer Где? Tap a row to hear it.",
             tables=[table(
                 ["в: enclosed space", "на: surface, open area, event"],
                 [["в до'ме", "на столе'"],
                  ["в шко'ле", "на стене'"],
                  ["в ко'мнате", "на у'лице"],
                  ["в ба'нке", "на уро'ке"],
                  ["в го'роде", "на конце'рте"],
                  ["в больни'це", "на стадио'не"],
                  ["в теа'тре", "на ка'рте"]])]),
        card("Pairs to memorise",
             "Some places do not follow the logic, and you just have to learn the pair. These are common ones "
             "that take на.",
             tables=[table(
                 ["Say", "Meaning"],
                 [["на по'чте", "at the post office"],
                  ["на рабо'те", "at work"],
                  ["на вокза'ле", "at the station"],
                  ["на ку'хне", "in the kitchen"],
                  ["на у'лице", "outside, on the street"],
                  ["на уро'ке", "in class, at a lesson"]],
                 note="Before some consonant clusters в becomes во: во дворе' (in the yard).")]),
    ],
    verify=[("дом", "доме"), ("школа", "школе"), ("комната", "комнате"), ("банк", "банке"),
            ("город", "городе"), ("больница", "больнице"), ("театр", "театре"), ("стол", "столе"),
            ("стена", "стене"), ("улица", "улице"), ("урок", "уроке"), ("концерт", "концерте"),
            ("стадион", "стадионе"), ("карта", "карте"), ("почта", "почте"), ("работа", "работе"),
            ("вокзал", "вокзале"), ("кухня", "кухне"), ("двор", "дворе")],
    exercises=[
        fb("Мы ___ шко'ле.", ["в", "на", "о", "к"], "в", "A school is an enclosed space: в.", tr="We are at school."),
        fb("Кни'га ___ столе'.", ["на", "в", "о", "к"], "на", "A table is a surface: на.", tr="The book is on the table."),
        fb("Ма'ма ___ ку'хне.", ["на", "в", "о", "к"], "на",
           "Ку'хня is one of the pairs to learn: на ку'хне.", tr="Mom is in the kitchen."),
        fb("Па'па ___ рабо'те.", ["на", "в", "о", "к"], "на", "На рабо'те is a fixed pair.", tr="Dad is at work."),
        fb("Де'ти ___ у'лице.", ["на", "в", "о", "к"], "на", "Open space: на у'лице.", tr="The children are outside."),
        fb("Он ___ ба'нке.", ["в", "на", "о", "к"], "в", "A bank is a building: в.", tr="He is at the bank."),
        fb("Мы ___ уро'ке.", ["на", "в", "о", "к"], "на", "Events and activities take на.", tr="We are in class."),
        fb("Она' ___ больни'це.", ["в", "на", "о", "к"], "в", "A hospital is a building: в.", tr="She is in the hospital."),
        fb("Я ___ по'чте.", ["на", "в", "о", "к"], "на", "На по'чте is a fixed pair.", tr="I am at the post office."),
        fb("Они' ___ дворе'.", ["во", "в", "на", "со"], "во",
           "Before some consonant clusters, в becomes во: во дворе' (in the yard). На дворе' also exists, but it "
           "is an idiom meaning “outdoors”, as in на дворе' хо'лодно.", tr="They are in the yard."),
    ],
)

# ---------------------------------------------------------------------------- 18
L18 = lesson(
    "This and that: э'тот, тот, and э'то",
    "Demonstratives agree with the noun; э'то never does",
    requires=["этот", "тот", "большой", "новый", "старый", "маленький"],
    cards=[
        card("Э'тот and тот",
             "Э'тот points at something close, or just mentioned. Тот points at something farther away, or "
             "mentioned earlier. Like adjectives, they agree with the noun in gender and number.",
             tables=[table(
                 ["", "Masculine", "Feminine", "Neuter", "Plural"],
                 [["this / these", "э'тот", "э'та", "э'то", "э'ти"],
                  ["that / those", "тот", "та", "то", "те"]])],
             examples=[
                 ex("Э'тот стол большо'й, а тот ма'ленький.", "This table is big, and that one is small.", "Э'тот"),
                 ex("Э'та кни'га но'вая, а та ста'рая.", "This book is new, and that one is old.", "Э'та"),
                 ex("Э'ти дома' но'вые, а те ста'рые.", "These houses are new, and those are old.", "Э'ти"),
             ]),
        card("Э'то is a different word",
             "Don't confuse the demonstratives with э'то meaning “this is”. That word has one form and never "
             "changes. A demonstrative goes before a noun and agrees with it, so on its own “э'та кни'га” is "
             "only the phrase “this book”, not a sentence. The neuter э'то looks identical to the fixed э'то, so "
             "there context decides.",
             tables=[table(
                 ["Form", "Meaning", "Example"],
                 [["Э'то + noun", "“This is…”; never changes", "Э'то кни'га. = This is a book."],
                  ["Э'та + noun", "“this book”; agrees", "Э'та кни'га но'вая. = This book is new."]])]),
    ],
    verify=[("этот", "эта"), ("этот", "это"), ("этот", "эти"), ("тот", "та"), ("тот", "то"), ("тот", "те")],
    exercises=[
        fb("___ дом ста'рый.", ["Э'тот", "Э'та", "Э'то", "Э'ти"], "Э'тот",
           "Дом is masculine, so э'тот.", tr="This house is old."),
        fb("___ кни'га но'вая.", ["Э'та", "Э'тот", "Э'то", "Э'ти"], "Э'та",
           "Кни'га is feminine, so э'та.", tr="This book is new."),
        fb("Э'тот стол большо'й, а ___ ма'ленький.", ["тот", "та", "то", "те"], "тот",
           "Masculine, and “that one” far away: тот.", tr="This table is big, and that one is small."),
        fb("Э'та кни'га но'вая, а ___ ста'рая.", ["та", "тот", "то", "те"], "та",
           "Feminine: та.", tr="This book is new, and that one is old."),
        fb("Э'ти дома' но'вые, а ___ ста'рые.", ["те", "тот", "та", "то"], "те",
           "Plural: те.", tr="These houses are new, and those are old."),
        mc("Which sentence means “This is a book”?",
           ["Э'то кни'га.", "Э'та кни'га.", "Э'тот кни'га.", "Э'ти кни'га."], "Э'то кни'га.",
           "Э'то + noun is a full sentence. Э'та кни'га is only “this book”."),
        mc("Which sentence means “These children are at home”?",
           ["Э'ти де'ти до'ма.", "Э'то де'ти до'ма.", "Э'та де'ти до'ма.", "Э'тот де'ти до'ма."], "Э'ти де'ти до'ма.",
           "Э'ти agrees with the plural noun and means “these”. Э'то де'ти… would be “these are children…”."),
        mc("Which of these is a fixed word that never changes?",
           ["э'то", "э'тот", "э'та", "э'ти"], "э'то",
           "Э'то (“this is”) has one form. Don't confuse it with the neuter of э'тот, which looks identical."),
        mc("Which word means “that one” (masculine, far away)?",
           ["тот", "та", "то", "те"], "тот", "Тот, та, то, те: that / those."),
    ],
)

# ---------------------------------------------------------------------------- 19
L19 = lesson(
    "Was and were: the past of быть",
    "Four forms: был, была', бы'ло, бы'ли",
    requires=["быть", "вчера", "дом", "работа", "школа"],
    cards=[
        card("Four forms",
             "In the present tense быть disappears. In the past it comes back, and Russian needs four forms where "
             "English has two (was, were): three for the singular genders and one for the plural. You choose by the "
             "subject. Я and ты take был or была' depending on who is speaking: a woman says я была'. Вы always "
             "takes бы'ли, even for one polite person.",
             tables=[table(
                 ["Subject", "Form", "Example"],
                 [["он · masculine noun", "бы{л}", "Вчера' он был до'ма. = Yesterday he was at home."],
                  ["она' · feminine noun", "был{а'}", "Вчера' она' была' до'ма. = Yesterday she was at home."],
                  ["оно' · neuter noun", "бы'л{о}", "Письмо' бы'ло на столе'. = The letter was on the table."],
                  ["мы, вы, они' · plural noun", "бы'л{и}", "Вчера' мы бы'ли в шко'ле. = Yesterday we were at school."]])]),
        card("Кто, что, and the negative",
             "Кто (who) always takes the masculine singular, even when the answer is a woman. Что (what) always "
             "takes the neuter. When быть is negated, the stress jumps onto не in every form except the feminine.",
             tables=[table(
                 ["Masculine", "Feminine", "Neuter", "Plural"],
                 [["не' был", "не была'", "не' было", "не' были"]])],
             examples=[
                 ex("Кто был до'ма? — До'ма была' моя' сестра'.", "Who was at home? — My sister was at home.", "Кто был"),
                 ex("Что бы'ло на столе'? — На столе' бы'ли де'ньги.", "What was on the table? — There was money on the table.", "Что бы'ло"),
             ]),
    ],
    verify=[("быть", "был"), ("быть", "была"), ("быть", "было"), ("быть", "были")],
    exercises=[
        fb("Вчера' ма'ма ___ до'ма.", ["была'", "был", "бы'ло", "бы'ли"], "была'",
           "Ма'ма is feminine.", tr="Yesterday mom was at home."),
        fb("Вчера' брат ___ на рабо'те.", ["был", "была'", "бы'ло", "бы'ли"], "был",
           "Брат is masculine.", tr="Yesterday my brother was at work."),
        fb("Вчера' де'ти ___ в шко'ле.", ["бы'ли", "был", "была'", "бы'ло"], "бы'ли",
           "Де'ти is plural.", tr="Yesterday the children were at school."),
        fb("Вчера' я ___ до'ма.", ["была'", "был", "бы'ло", "бы'ли"], "была'",
           "The speaker is a woman, so the feminine form.", tr="Yesterday I was at home. (a woman speaking)"),
        fb("Вы ___ вчера' до'ма?", ["бы'ли", "был", "была'", "бы'ло"], "бы'ли",
           "Вы always takes the plural form, even for one polite person.", tr="Were you at home yesterday? (one person, polite)"),
        fb("Что ___ на столе'?", ["бы'ло", "был", "была'", "бы'ли"], "бы'ло",
           "Что takes the neuter.", tr="What was on the table?"),
        fb("Кто ___ здесь?", ["был", "была'", "бы'ло", "бы'ли"], "был",
           "Кто takes the masculine, even if the answer turns out to be a woman.", tr="Who was here?"),
        mc("Which negated form keeps the stress on the verb?",
           ["не была'", "не' был", "не' было", "не' были"], "не была'",
           "Only the feminine keeps the stress on the verb: не была'."),
        mc("How do you say “The letter wasn't there”?",
           ["Письмо' не' было там.", "Письмо' не' была там.", "Письмо' не' был там.", "Письмо' нет было там."],
           "Письмо' не' было там.", "Письмо' is neuter, so бы'ло, with the stress on не."),
        mc("A man says “Вчера' я был на рабо'те.” How does a woman say it?",
           ["Вчера' я была' на рабо'те.", "Вчера' я был на рабо'те.", "Вчера' я бы'ло на рабо'те.",
            "Вчера' я бы'ли на рабо'те."],
           "Вчера' я была' на рабо'те.", "The verb follows the speaker's gender."),
    ],
)

# ---------------------------------------------------------------------------- 20
L20 = lesson(
    "The present tense: your first verbs",
    "Жить and рабо'тать: each person has its own ending",
    requires=["жить", "работать", "город", "дом", "школа"],
    cards=[
        card("Infinitive and endings",
             "The dictionary form of a verb is the infinitive, usually ending in -ть: жить (to live), "
             "рабо'тать (to work). In the present tense each person has its own ending, so Russian often needs "
             "no pronoun. Changing the endings like this is called conjugating. These two are called "
             "first-conjugation verbs. Tap a row to hear it.",
             tables=[table(
                 ["Person", "жить", "рабо'тать"],
                 [["я", "жив{у'}", "рабо'та{ю}"],
                  ["ты", "жив{ёшь}", "рабо'та{ешь}"],
                  ["он · она' · оно'", "жив{ёт}", "рабо'та{ет}"],
                  ["мы", "жив{ём}", "рабо'та{ем}"],
                  ["вы", "жив{ёте}", "рабо'та{ете}"],
                  ["они'", "жив{у'т}", "рабо'та{ют}"]],
                 note="The stem of жить changes (жи- becomes жив-), so learn it as it is.")]),
        card("Putting it together",
             "You can now build real sentences: в or на with the prepositional case for the place, and не before "
             "the verb to negate it. There is also only one present tense: Я рабо'таю covers both “I work” and "
             "“I am working”.",
             examples=[
                 ex("Я живу' в до'ме.", "I live in a house.", "живу'"),
                 ex("Ма'ма рабо'тает в шко'ле.", "Mom works at a school.", "рабо'тает"),
                 ex("Где вы живёте?", "Where do you live?", "живёте"),
                 ex("Они' не рабо'тают здесь.", "They don't work here.", "не рабо'тают"),
             ]),
    ],
    verify=[("жить", "живу"), ("жить", "живёшь"), ("жить", "живёт"), ("жить", "живём"),
            ("жить", "живёте"), ("жить", "живут"), ("работать", "работаю"), ("работать", "работаешь"),
            ("работать", "работает"), ("работать", "работаем"), ("работать", "работаете"),
            ("работать", "работают")],
    exercises=[
        fb("Я ___ в шко'ле.", ["рабо'таю", "рабо'таешь", "рабо'тает", "рабо'таем"], "рабо'таю",
           "Я takes -ю.", tr="I work at a school."),
        fb("Ты ___ здесь?", ["живёшь", "живу'", "живёт", "живём"], "живёшь",
           "Ты takes -ёшь.", tr="Do you live here?"),
        fb("Ма'ма ___ в ба'нке.", ["рабо'тает", "рабо'таю", "рабо'таешь", "рабо'тают"], "рабо'тает",
           "Он, она' and a singular noun take -ет.", tr="Mom works at a bank."),
        fb("Мы ___ в до'ме.", ["живём", "живу'", "живёшь", "живу'т"], "живём",
           "Мы takes -ём.", tr="We live in a house."),
        fb("Они' ___ на по'чте.", ["рабо'тают", "рабо'тает", "рабо'таете", "рабо'таем"], "рабо'тают",
           "Они' takes -ют.", tr="They work at the post office."),
        fb("Вы ___ в го'роде?", ["живёте", "живу'", "живёшь", "живу'т"], "живёте",
           "Вы takes -ёте.", tr="Do you live in town? (polite or plural)"),
        mc("How do you say “He doesn't work here”?",
           ["Он не рабо'тает здесь.", "Он нет рабо'тает здесь.", "Он рабо'тает нет здесь.", "Он не есть рабо'тает здесь."],
           "Он не рабо'тает здесь.", "Не goes right before the verb."),
        mc("Which form means “they live”?", ["живу'т", "живёт", "живёте", "живу'"], "живу'т",
           "Они' takes -ут for жить."),
        mc("What does “Я рабо'таю” cover in English?",
           ["Both “I work” and “I am working”", "Only “I work”", "Only “I am working”", "Neither"],
           "Both “I work” and “I am working”",
           "Russian has a single present tense.", order=True),
    ],
)

UNIT = unit("Unit 3: Describing, locating and verbs", [L13, L14, L15, L16, L17, L18, L19, L20])
