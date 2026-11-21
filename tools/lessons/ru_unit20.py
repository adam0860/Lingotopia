"""Unit 20: the genitive plural (textbook module 5, lesson 27)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 180
L180 = lesson(
    "Many students, few lessons: the genitive plural in -ов",
    "В на'шем институ'те мно'го студе'нтов.",
    requires=["много", "студент", "стол", "дом", "мало"],
    cards=[
        card("Hard consonant: add -ов",
             "You know the genitive singular (нет кни'ги). Now the genitive plural. Most masculine nouns that end in a "
             "hard consonant simply add -ов. If the plural is stressed on the ending (столы', дома', города'), "
             "the genitive plural is stressed on -ов too.",
             tables=[table(
                 ["Singular", "Genitive plural", "Ending"],
                 [["студе'нт", "студе'нт{ов}", "-ов"],
                  ["стол", "стол{о'в}", "-ов"],
                  ["дом", "дом{о'в}", "-ов"],
                  ["го'род", "город{о'в}", "-ов"],
                  ["уро'к", "уро'к{ов}", "-ов"],
                  ["журна'л", "журна'л{ов}", "-ов"],
                  ["магази'н", "магази'н{ов}", "-ов"],
                  ["теа'тр", "теа'тр{ов}", "-ов"]])],
             examples=[
                 ex("В на'шем институ'те мно'го студе'нтов.", "There are many students at our institute.", "студе'нтов"),
                 ex("В э'том го'роде ма'ло теа'тров.", "There are few theaters in this city.", "теа'тров"),
                 ex("В ко'мнате нет столо'в.", "There are no tables in the room.", "столо'в"),
             ]),
        card("How many? Many, few, several",
             "Words of quantity are followed by the genitive plural when you can count the things. This is the most "
             "common use of the case, so learn these words well.",
             tables=[table(
                 ["Word", "Meaning", "Example"],
                 [["ско'лько", "how many", "Ско'лько студе'нтов в гру'ппе?"],
                  ["мно'го", "many", "У нас мно'го уро'ков."],
                  ["ма'ло", "few", "В го'роде ма'ло магази'нов."],
                  ["не'сколько", "several", "Там не'сколько теа'тров."],
                  ["сто'лько", "so many", "Почему' сто'лько журна'лов?"],
                  ["большинство'", "most", "Большинство' студе'нтов живёт здесь."]])],
             examples=[
                 ex("Ско'лько студе'нтов в гру'ппе?", "How many students are in the group?", "студе'нтов"),
                 ex("У нас мно'го уро'ков.", "We have many lessons.", "уро'ков"),
                 ex("Большинство' студе'нтов живёт здесь.", "Most of the students live here.", "студе'нтов"),
             ]),
        card("Also: “of”, and nothing at all",
             "The genitive plural also means “of” (the house of the students) and appears after нет (there are no).",
             examples=[
                 ex("Э'то дом студе'нтов.", "This is the students' house.", "студе'нтов"),
                 ex("В гости'нице нет телефо'нов.", "There are no telephones in the hotel.", "телефо'нов"),
             ]),
    ],
    verify=(vf("студент", "студентов") + vf("стол", "столов") + vf("дом", "домов") + vf("город", "городов")
            + vf("урок", "уроков") + vf("журнал", "журналов") + vf("магазин", "магазинов") + vf("театр", "театров")
            + vf("телефон", "телефонов")),
    exercises=[
        F("У нас мно'го ___ в институ'те. (students)", "студе'нтов", ["студе'нты", "студе'нтам", "студе'нта"], "Мно'го + genitive plural: -ов.", "We have many students at the institute.", lemma="студент"),
        F("В ко'мнате не'сколько ___. (tables)", "столо'в", ["столы'", "стола'", "столу'"], "Hard consonant: -ов, stressed like столы'.", "There are several tables in the room.", lemma="стол"),
        F("Ско'лько ___ в э'том го'роде? (theaters)", "теа'тров", ["теа'тры", "теа'тра", "теа'тру"], "Ско'лько + genitive plural.", "How many theaters are in this city?", lemma="театр"),
        F("В э'том райо'не ма'ло ___. (stores)", "магази'нов", ["магази'ны", "магази'на", "магази'ну"], "Ма'ло + genitive plural.", "There are few stores in this district.", lemma="магазин"),
        F("Мы ви'дели мно'го ___. (houses)", "домо'в", ["дома'", "до'му", "до'мом"], "Дом → домо'в, with the stress on the ending.", "We saw many houses.", lemma="дом"),
        F("У нас сего'дня ма'ло ___. (lessons)", "уро'ков", ["уро'ки", "уро'ка", "уро'ку"], "Hard consonant: -ов.", "We have few lessons today.", lemma="урок"),
        F("В гости'нице нет ___. (telephones)", "телефо'нов", ["телефо'ны", "телефо'на", "телефо'ну"], "Нет + genitive; plural: -ов.", "There are no telephones in the hotel.", lemma="телефон"),
        mc("What ending do most masculine nouns in a hard consonant take in the genitive plural?", ["-ов", "-ей", "-ий", "-ам"], "-ов", "Add -ов.", order=True),
        mc("After мно'го, ма'ло and не'сколько with things you can count, the noun is in the...", ["genitive plural", "nominative plural", "dative plural", "genitive singular"], "genitive plural", "Quantity words take the genitive plural."),
    ],
)

# ---------------------------------------------------------------------------- 181
L181 = lesson(
    "Museums, teachers, doctors: -ев and -ей",
    "В э'том го'роде мно'го музе'ев и учителе'й.",
    requires=["музей", "день", "врач", "словарь", "нож"],
    cards=[
        card("Nouns in -й: -ев",
             "A masculine noun that ends in -й loses the -й and takes -ев (or -ёв when the ending is stressed).",
             tables=[table(
                 ["Singular", "Genitive plural", "Ending"],
                 [["музе'й", "музе'{ев}", "-ев"],
                  ["геро'й", "геро'{ев}", "-ев"],
                  ["слу'чай", "слу'ча{ев}", "-ев"],
                  ["трамва'й", "трамва'{ев}", "-ев"]])],
             examples=[
                 ex("В Москве' мно'го музе'ев.", "There are many museums in Moscow.", "музе'ев"),
                 ex("В э'той кни'ге ма'ло геро'ев.", "There are few heroes in this book.", "геро'ев"),
             ]),
        card("Soft sign, ж, ч, ш, щ: -ей",
             "A masculine noun that ends in -ь takes -ей, and so does a masculine noun ending in ж, ч, ш or щ. "
             "Often the stress falls on the ending: учителе'й, ноже'й, враче'й.",
             tables=[table(
                 ["Singular", "Genitive plural", "Ending"],
                 [["преподава'тель", "преподава'тел{ей}", "-ей"],
                  ["учи'тель", "учител{е'й}", "-ей"],
                  ["слова'рь", "словар{е'й}", "-ей"],
                  ["автомоби'ль", "автомоби'л{ей}", "-ей"],
                  ["гость", "гост{е'й}", "-ей"],
                  ["рубль", "рубл{е'й}", "-ей"],
                  ["нож", "нож{е'й}", "-ей"],
                  ["врач", "врач{е'й}", "-ей"],
                  ["ключ", "ключ{е'й}", "-ей"],
                  ["эта'ж", "этаж{е'й}", "-ей"],
                  ["каранда'ш", "карандаш{е'й}", "-ей"]])],
             examples=[
                 ex("Ско'лько учителе'й в ва'шей шко'ле?", "How many teachers are in your school?", "учителе'й"),
                 ex("В больни'це мно'го враче'й.", "There are many doctors at the hospital.", "враче'й"),
                 ex("У меня' нет ключе'й.", "I have no keys.", "ключе'й"),
             ]),
        card("Nouns in -ец",
             "A masculine noun in -ец loses the e and takes -цев when the stress stays on the stem, but -цов when the "
             "ending is stressed.",
             tables=[table(
                 ["Singular", "Genitive plural", "Rule"],
                 [["америка'нец", "америка'н{цев}", "stem stress: -цев"],
                  ["япо'нец", "япо'н{цев}", "stem stress: -цев"],
                  ["па'лец", "па'л{ьцев}", "stem stress: -цев"],
                  ["оте'ц", "от{цо'в}", "end stress: -цов"],
                  ["продаве'ц", "продав{цо'в}", "end stress: -цов"],
                  ["коне'ц", "кон{цо'в}", "end stress: -цов"]])],
             examples=[
                 ex("В гости'нице мно'го америка'нцев.", "There are many Americans at the hotel.", "америка'нцев"),
                 ex("В магази'не три продавца'.", "There are three salesmen in the store.", "продавца'"),
             ]),
    ],
    verify=(vf("музей", "музеев") + vf("герой", "героев") + vf("случай", "случаев") + vf("трамвай", "трамваев")
            + vf("преподаватель", "преподавателей") + vf("учитель", "учителей") + vf("словарь", "словарей")
            + vf("автомобиль", "автомобилей") + vf("гость", "гостей") + vf("рубль", "рублей") + vf("нож", "ножей")
            + vf("врач", "врачей") + vf("ключ", "ключей") + vf("этаж", "этажей") + vf("карандаш", "карандашей")
            + vf("американец", "американцев") + vf("японец", "японцев") + vf("палец", "пальцев")
            + vf("отец", "отцов") + vf("продавец", "продавцов", "продавца") + vf("конец", "концов")),
    exercises=[
        F("В го'роде мно'го ___. (museums)", "музе'ев", ["музе'ов", "музе'й", "музе'ям"], "-й → -ев.", "There are many museums in the city.", lemma="музей"),
        F("У него' нет ___. (dictionaries)", "словаре'й", ["слова'рь", "словаря'м", "слова'ря"], "-ь → -ей, stressed.", "He has no dictionaries.", lemma="словарь"),
        F("Ско'лько ___ в ва'шей гру'ппе? (teachers)", "учителе'й", ["учи'тель", "учителя'м", "учителя'"], "-ь → -ей.", "How many teachers are in your group?", lemma="учитель"),
        F("В больни'це мно'го ___. (doctors)", "враче'й", ["врачи'", "врачу'", "враче'м"], "Ending in ч: -ей.", "There are many doctors at the hospital.", lemma="врач"),
        F("На столе' нет ___. (knives)", "ноже'й", ["ножи'", "ножу'", "ноже'м"], "Ending in ж: -ей.", "There are no knives on the table.", lemma="нож"),
        F("На стоя'нке мно'го ___. (cars)", "автомоби'лей", ["автомоби'ли", "автомоби'ль", "автомоби'лю"], "-ь → -ей.", "There are many cars in the parking lot.", lemma="автомобиль"),
        F("В гости'нице мно'го ___. (Americans)", "америка'нцев", ["америка'нцы", "америка'нца", "америка'нцам"], "-ец with stem stress: -цев.", "There are many Americans at the hotel.", lemma="американец"),
        F("У нас ма'ло ___. (guests)", "госте'й", ["го'сти", "го'стя", "гостю'"], "-ь → -ей, stressed.", "We have few guests.", lemma="гость"),
        mc("What is the genitive plural ending of a masculine noun in -й, like музе'й?", ["-ев", "-ей", "-ов", "-ий"], "-ев", "-й → -ев.", order=True),
        mc("What ending do masculine nouns in -ь, ж, ч, ш and щ take?", ["-ей", "-ев", "-ов", "-ий"], "-ей", "-ей after -ь and ж ч ш щ."),
    ],
)

# ---------------------------------------------------------------------------- 182
L182 = lesson(
    "Books, rooms, words: the zero ending",
    "В э'той ко'мнате мно'го книг.",
    requires=["книга", "комната", "слово", "место", "неделя"],
    cards=[
        card("Drop the last vowel",
             "Feminine nouns in -а and neuter nouns in -о simply lose their ending in the genitive plural. There is "
             "nothing to add: кни'га → книг. This works when the stem ends in a single consonant.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["кни'га", "книг"],
                  ["ко'мната", "ко'мнат"],
                  ["шко'ла", "школ"],
                  ["маши'на", "маши'н"],
                  ["газе'та", "газе'т"],
                  ["ка'рта", "карт"],
                  ["сло'во", "слов"],
                  ["ме'сто", "мест"],
                  ["де'ло", "дел"],
                  ["лицо'", "лиц"]])],
             examples=[
                 ex("В э'той ко'мнате мно'го книг.", "There are many books in this room.", "книг"),
                 ex("Ско'лько слов ты зна'ешь?", "How many words do you know?", "слов"),
                 ex("В авто'бусе нет мест.", "There are no seats on the bus.", "мест"),
             ]),
        card("The stress often moves back",
             "Many nouns that are stressed on the ending in the singular are stressed on the stem in the genitive "
             "plural. Learn the common ones.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["страна'", "стран"],
                  ["рука'", "рук"],
                  ["нога'", "ног"],
                  ["река'", "рек"],
                  ["гора'", "гор"],
                  ["стена'", "стен"],
                  ["цена'", "цен"],
                  ["голова'", "голо'в"],
                  ["война'", "войн"]])],
             examples=[
                 ex("В Евро'пе мно'го стран.", "There are many countries in Europe.", "стран"),
                 ex("В Росси'и мно'го рек.", "There are many rivers in Russia.", "рек"),
             ]),
        card("Feminine nouns in -я",
             "After a single consonant, many nouns in -я replace it with -ь: неде'ля → неде'ль.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["неде'ля", "неде'ль"],
                  ["ба'ня", "бань"],
                  ["ня'ня", "нянь"]])],
             examples=[
                 ex("Я не был дома' не'сколько неде'ль.", "I was not at home for several weeks.", "неде'ль"),
             ]),
    ],
    verify=(vf("книга", "книг") + vf("комната", "комнат") + vf("школа", "школ") + vf("машина", "машин")
            + vf("газета", "газет") + vf("карта", "карт") + vf("слово", "слов") + vf("место", "мест")
            + vf("дело", "дел") + vf("лицо", "лиц") + vf("страна", "стран") + vf("рука", "рук") + vf("нога", "ног")
            + vf("река", "рек") + vf("гора", "гор") + vf("стена", "стен") + vf("цена", "цен")
            + vf("голова", "голов") + vf("война", "войн") + vf("неделя", "недель") + vf("баня", "бань")
            + vf("няня", "нянь")),
    exercises=[
        F("У меня' мно'го ___. (books)", "книг", ["кни'ги", "кни'гам", "кни'гой"], "Drop -а: книг.", "I have many books.", lemma="книга"),
        F("В на'шем до'ме мно'го ___. (rooms)", "ко'мнат", ["ко'мнаты", "ко'мнате", "ко'мнату"], "Drop -а: ко'мнат.", "There are many rooms in our house.", lemma="комната"),
        F("В Евро'пе мно'го ___. (countries)", "стран", ["стра'ны", "стране'", "страну'"], "Страна' → стран.", "There are many countries in Europe.", lemma="страна"),
        F("Ско'лько ___ в ва'шем го'роде? (schools)", "школ", ["шко'лы", "шко'ле", "шко'лу"], "Drop -а: школ.", "How many schools are in your city?", lemma="школа"),
        F("Мы жи'ли там не'сколько ___. (weeks)", "неде'ль", ["неде'ли", "неде'лю", "неде'ле"], "-я → -ь: неде'ль.", "We lived there for several weeks.", lemma="неделя"),
        F("В э'том те'ксте мно'го ___. (words)", "слов", ["сло'ва", "сло'ву", "слова'"], "Drop -о: слов.", "There are many words in this text.", lemma="слово"),
        F("В гараже' нет ___. (cars)", "маши'н", ["маши'ны", "маши'не", "маши'ну"], "Drop -а: маши'н.", "There are no cars in the garage.", lemma="машина"),
        F("В авто'бусе нет свобо'дных ___. (seats)", "мест", ["ме'ста", "ме'сто", "места'"], "Drop -о: мест.", "There are no free seats on the bus.", lemma="место"),
        mc("What happens to кни'га in the genitive plural?", ["the -а is dropped", "-ов is added", "-ей is added", "nothing changes"], "the -а is dropped", "Zero ending."),
        mc("How do you say “many hands”?", ["мно'го рук", "мно'го ру'ки", "мно'го руко'в", "мно'го рука'м"], "мно'го рук", "Рука' → рук."),
    ],
)

# ---------------------------------------------------------------------------- 183
L183 = lesson(
    "Female students, plates, windows: the fleeting vowel",
    "На столе' нет таре'лок.",
    requires=["окно", "сестра", "песня", "кухня", "девушка"],
    cards=[
        card("Two consonants need a vowel",
             "When the stem ends in two consonants (as in студе'нт-к-а), the zero ending would leave them piled up at "
             "the end of the word. So Russian inserts a vowel between them: usually -о-, but -е- after ж, ч, ш, щ and "
             "after й.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["студе'нтка", "студе'нт{о}к"],
                  ["таре'лка", "таре'л{о}к"],
                  ["су'мка", "су'м{о}к"],
                  ["ма'рка", "ма'р{о}к"],
                  ["ло'жка", "ло'ж{е}к"],
                  ["ру'чка", "ру'ч{е}к"],
                  ["ча'шка", "ча'ш{е}к"],
                  ["де'вушка", "де'вуш{е}к"],
                  ["копе'йка", "копе'{е}к"]])],
             examples=[
                 ex("В на'шей гру'ппе мно'го студе'нток.", "There are many female students in our group.", "студе'нток"),
                 ex("На столе' нет таре'лок.", "There are no plates on the table.", "таре'лок"),
                 ex("У меня' нет ру'чек.", "I have no pens.", "ру'чек"),
             ]),
        card("Words in -ня",
             "Words in -ня do not follow one pattern, so learn them as they come. Some take -е- and no soft sign, and "
             "some take a vowel and a soft sign.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["пе'сня", "пе'с{е}н"],
                  ["ба'шня", "ба'ш{е}н"],
                  ["ку'хня", "ку'х{о}нь"],
                  ["дере'вня", "дерев{е'}нь"]])],
             examples=[
                 ex("Ско'лько пе'сен ты зна'ешь?", "How many songs do you know?", "пе'сен"),
                 ex("В э'том до'ме нет ку'хонь.", "There are no kitchens in this house.", "ку'хонь"),
             ]),
        card("Neuter nouns and “sisters”",
             "Neuter nouns in -о can need a fleeting vowel too, and the stress may move to the first syllable. "
             "Сестра' becomes сестёр.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["окно'", "о'к{о}н"],
                  ["письмо'", "пи'с{е}м"],
                  ["кре'сло", "кре'с{е}л"],
                  ["число'", "чи'с{е}л"],
                  ["сестра'", "сест{ё}р"]])],
             examples=[
                 ex("В э'той ко'мнате мно'го о'кон.", "There are many windows in this room.", "о'кон"),
                 ex("У неё нет ни бра'тьев, ни сестёр.", "She has neither brothers nor sisters.", "сестёр"),
             ]),
    ],
    verify=(vf("студентка", "студенток") + vf("тарелка", "тарелок") + vf("сумка", "сумок") + vf("марка", "марок")
            + vf("ложка", "ложек") + vf("ручка", "ручек") + vf("чашка", "чашек") + vf("девушка", "девушек")
            + vf("копейка", "копеек") + vf("песня", "песен") + vf("башня", "башен") + vf("кухня", "кухонь")
            + vf("деревня", "деревень") + vf("окно", "окон") + vf("письмо", "писем") + vf("кресло", "кресел")
            + vf("число", "чисел") + vf("сестра", "сестёр")),
    exercises=[
        F("В на'шей гру'ппе мно'го ___. (female students)", "студе'нток", ["студе'нтк", "студе'нтки", "студе'нткам"], "Insert -о-: студе'нток.", "There are many female students in our group.", lemma="студентка"),
        F("На столе' нет ___. (plates)", "таре'лок", ["таре'лк", "таре'лки", "таре'лкам"], "Insert -о-: таре'лок.", "There are no plates on the table.", lemma="тарелка"),
        F("В э'той ко'мнате мно'го ___. (windows)", "о'кон", ["окн", "о'кна", "о'кнам"], "Окно' → о'кон.", "There are many windows in this room.", lemma="окно"),
        F("У нас нет ___. (spoons)", "ло'жек", ["ло'жк", "ло'жки", "ло'жкам"], "After ж insert -е-: ло'жек.", "We have no spoons.", lemma="ложка"),
        F("Ско'лько ___ ты зна'ешь? (songs)", "пе'сен", ["пе'сни", "пе'сню", "пе'снь"], "Пе'сня → пе'сен.", "How many songs do you know?", lemma="песня"),
        F("В э'том до'ме нет ___. (kitchens)", "ку'хонь", ["ку'хни", "ку'хню", "ку'хня"], "Ку'хня → ку'хонь.", "There are no kitchens in this house.", lemma="кухня"),
        F("Мы купи'ли не'сколько ___. (cups)", "ча'шек", ["ча'шк", "ча'шки", "ча'шку"], "After ш insert -е-: ча'шек.", "We bought several cups.", lemma="чашка"),
        F("Ско'лько ___ в э'той гру'ппе? (girls)", "де'вушек", ["де'вушки", "де'вушку", "де'вушкам"], "After ш insert -е-: де'вушек.", "How many girls are in this group?", lemma="девушка"),
        mc("Why is the form студе'нток and not студе'нтк?", ["two consonants need a vowel between them", "it is an exception", "the stress moves", "the noun is masculine"], "two consonants need a vowel between them", "A fleeting vowel is inserted."),
        mc("Which vowel is inserted in ру'чка → ру'чек?", ["е", "о", "и", "а"], "е", "After ч we insert -е-."),
    ],
)

# ---------------------------------------------------------------------------- 184
L184 = lesson(
    "Squares, nights, lectures: -ей and -ий",
    "В э'том го'роде мно'го площаде'й.",
    requires=["площадь", "ночь", "дверь", "лекция", "здание"],
    cards=[
        card("Feminine -ь and neuter -е: -ей",
             "Feminine nouns in a soft sign and neuter nouns in -е take -ей. The stress is often on the ending.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["пло'щадь", "площад{е'й}"],
                  ["ночь", "ноч{е'й}"],
                  ["дверь", "двер{е'й}"],
                  ["вещь", "вещ{е'й}"],
                  ["тетра'дь", "тетра'д{ей}"],
                  ["о'бласть", "област{е'й}"],
                  ["мо'ре", "мор{е'й}"],
                  ["по'ле", "пол{е'й}"]])],
             examples=[
                 ex("В Москве' мно'го площаде'й.", "There are many squares in Moscow.", "площаде'й"),
                 ex("Мы не спа'ли не'сколько ноче'й.", "We did not sleep for several nights.", "ноче'й"),
                 ex("В Росси'и мно'го море'й.", "There are many seas in Russia.", "море'й"),
             ]),
        card("Nouns in -ия and -ие: -ий",
             "Nouns in -ия and -ие end in -ий in the genitive plural, the -ия or -ие is simply replaced by -ий.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["ле'кция", "ле'кц{ий}"],
                  ["фами'лия", "фами'л{ий}"],
                  ["фотогра'фия", "фотогра'ф{ий}"],
                  ["ста'нция", "ста'нц{ий}"],
                  ["зда'ние", "зда'н{ий}"],
                  ["заня'тие", "заня'т{ий}"],
                  ["упражне'ние", "упражне'н{ий}"],
                  ["зна'ние", "зна'н{ий}"]])],
             examples=[
                 ex("В институ'те мно'го ле'кций.", "There are many lectures at the institute.", "ле'кций"),
                 ex("В э'том го'роде мно'го зда'ний.", "There are many buildings in this city.", "зда'ний"),
                 ex("У нас сего'дня ма'ло заня'тий.", "We have few classes today.", "заня'тий"),
             ]),
    ],
    verify=(vf("площадь", "площадей") + vf("ночь", "ночей") + vf("дверь", "дверей") + vf("вещь", "вещей")
            + vf("тетрадь", "тетрадей") + vf("область", "областей") + vf("море", "морей") + vf("поле", "полей")
            + vf("лекция", "лекций") + vf("фамилия", "фамилий") + vf("фотография", "фотографий")
            + vf("станция", "станций") + vf("здание", "зданий") + vf("занятие", "занятий")
            + vf("упражнение", "упражнений") + vf("знание", "знаний")),
    exercises=[
        F("В на'шем го'роде мно'го ___. (squares)", "площаде'й", ["пло'щади", "пло'щадь", "площадя'м"], "-ь → -ей, stressed.", "There are many squares in our city.", lemma="площадь"),
        F("Ско'лько ___ в э'той ко'мнате? (doors)", "двере'й", ["две'ри", "дверя'м", "дверь"], "-ь → -ей, stressed.", "How many doors are in this room?", lemma="дверь"),
        F("Мы не спа'ли не'сколько ___. (nights)", "ноче'й", ["но'чи", "ночь", "ноча'м"], "-ь → -ей, stressed.", "We did not sleep for several nights.", lemma="ночь"),
        F("В институ'те мно'го ___. (lectures)", "ле'кций", ["ле'кции", "ле'кцией", "ле'кцию"], "-ия → -ий.", "There are many lectures at the institute.", lemma="лекция"),
        F("Ско'лько ___ в ва'шем го'роде? (buildings)", "зда'ний", ["зда'ния", "зда'нию", "зда'нием"], "-ие → -ий.", "How many buildings are in your city?", lemma="здание"),
        F("У нас сего'дня ма'ло ___. (classes)", "заня'тий", ["заня'тия", "заня'тие", "заня'тиям"], "-ие → -ий.", "We have few classes today.", lemma="занятие"),
        F("В Росси'и мно'го ___. (seas)", "море'й", ["мо'ря", "мо'ре", "моря'"], "Neuter -е → -ей.", "There are many seas in Russia.", lemma="море"),
        F("В э'том райо'не нет ___. (stations)", "ста'нций", ["ста'нции", "ста'нцию", "ста'нцией"], "-ия → -ий.", "There are no stations in this district.", lemma="станция"),
        mc("What is the genitive plural ending of nouns in -ия and -ие?", ["-ий", "-ей", "-ов", "-ев"], "-ий", "-ия, -ие → -ий.", order=True),
        mc("What is the genitive plural ending of feminine nouns in a soft sign?", ["-ей", "-ий", "-ов", "no ending"], "-ей", "Soft sign → -ей."),
    ],
)

# ---------------------------------------------------------------------------- 185
L185 = lesson(
    "Friends, children, people, years: irregular genitive plurals",
    "У неё мно'го друзе'й и пять лет опы'та.",
    requires=["друг", "человек", "ребёнок", "год", "раз"],
    cards=[
        card("Family and friends",
             "These very common words are irregular. Learn them as they are.",
             tables=[table(
                 ["Singular", "Genitive plural"],
                 [["друг", "друз{е'й}"],
                  ["брат", "бра'тьев"],
                  ["сын", "сынов{е'й}"],
                  ["мать", "матер{е'й}"],
                  ["дочь", "дочер{е'й}"],
                  ["сестра'", "сестёр"],
                  ["сосе'д", "сосе'дей"],
                  ["муж", "муж{е'й}"],
                  ["ребёнок", "дет{е'й}"],
                  ["челове'к", "люд{е'й}"]])],
             examples=[
                 ex("У меня' мно'го друзе'й.", "I have many friends.", "друзе'й"),
                 ex("У неё нет ни бра'тьев, ни сестёр.", "She has neither brothers nor sisters.", "сестёр"),
                 ex("В па'рке мно'го дете'й.", "There are many children in the park.", "дете'й"),
             ]),
        card("Years, times, days, names",
             "After the numbers 5 and above, and after мно'го, ско'лько and не'сколько, use лет for years, раз for times "
             "and челове'к for a count of people. For people in general (not counting) use люде'й.",
             tables=[table(
                 ["Word", "Genitive plural", "Use"],
                 [["год", "лет", "пять лет, мно'го лет"],
                  ["раз", "раз", "пять раз, мно'го раз"],
                  ["день", "дней", "пять дней"],
                  ["челове'к", "челове'к", "пять челове'к"],
                  ["и'мя", "имён", "мно'го имён"],
                  ["вре'мя", "времён", "времён го'да"]])],
             examples=[
                 ex("Я живу' здесь пять лет.", "I have lived here for five years.", "лет"),
                 ex("Я был там мно'го раз.", "I was there many times.", "раз"),
                 ex("На ле'кции бы'ло пять челове'к.", "There were five people at the lecture.", "челове'к"),
                 ex("Там бы'ло мно'го люде'й.", "There were many people there.", "люде'й"),
             ]),
        card("Plural-only nouns and more",
             "Nouns that exist only in the plural often have no ending at all, or a special one.",
             tables=[table(
                 ["Nominative", "Genitive plural"],
                 [["де'ньги", "де'нег"],
                  ["брю'ки", "брюк"],
                  ["очки'", "очко'в"],
                  ["боти'нки", "боти'нок"],
                  ["кани'кулы", "кани'кул"],
                  ["часы'", "часо'в"],
                  ["су'тки", "су'ток"],
                  ["о'блако", "облако'в"],
                  ["пла'тье", "пла'тьев"],
                  ["англича'нин", "англича'н"]])],
             examples=[
                 ex("У меня' нет де'нег.", "I have no money.", "де'нег"),
                 ex("Мы жда'ли дво'е су'ток.", "We waited two days.", "су'ток"),
             ]),
    ],
    verify=(vf("друг", "друзей") + vf("брат", "братьев") + vf("сын", "сыновей") + vf("мать", "матерей")
            + vf("дочь", "дочерей") + vf("сестра", "сестёр") + vf("сосед", "соседей") + vf("муж", "мужей")
            + vf("ребёнок", "детей") + vf("человек", "людей", "человек") + vf("год", "лет")
            + vf("раз", "раз") + vf("день", "дней") + vf("имя", "имён") + vf("время", "времён")
            + vf("деньги", "денег") + vf("брюки", "брюк") + vf("очки", "очков") + vf("ботинок", "ботинок")
            + vf("каникулы", "каникул") + vf("часы", "часов") + vf("сутки", "суток") + vf("облако", "облаков")
            + vf("платье", "платьев") + vf("англичанин", "англичан")),
    exercises=[
        F("У меня' мно'го ___. (friends)", "друзе'й", ["друзья'", "дру'га", "дру'гу"], "Друг → друзе'й.", "I have many friends.", lemma="друг"),
        F("У неё нет ни бра'тьев, ни ___. (sisters)", "сестёр", ["сестры'", "сестра'м", "сестре'"], "Сестра' → сестёр.", "She has neither brothers nor sisters.", lemma="сестра"),
        F("В па'рке мно'го ___. (children)", "дете'й", ["де'ти", "де'тям", "ребёнка"], "Ребёнок → дете'й.", "There are many children in the park.", lemma="ребёнок"),
        F("Там бы'ло пять ___. (people)", "челове'к", ["люде'й", "лю'ди", "челове'ка"], "After 5 and more: челове'к.", "There were five people there."),
        F("Мно'го ___ пришло' на конце'рт. (people)", "люде'й", ["лю'ди", "лю'дям", "людьми'"], "People in general: люде'й.", "Many people came to the concert."),
        F("Я живу' здесь пять ___. (years)", "лет", ["годо'в", "го'да", "го'ды"], "After 5 and more: лет.", "I have lived here for five years."),
        F("Я был там мно'го ___. (times)", "раз", ["разо'в", "ра'за", "ра'зы"], "Раз stays раз.", "I have been there many times."),
        F("У меня' нет ___. (money)", "де'нег", ["де'ньги", "де'ньгам", "де'ньгами"], "Де'ньги → де'нег.", "I have no money.", lemma="деньги"),
        F("Ско'лько ___ ты зна'ешь? (names)", "имён", ["имена'", "и'мени", "и'мя"], "И'мя → имён.", "How many names do you know?", lemma="имя"),
        mc("How do you say “five years”?", ["пять лет", "пять го'дов", "пять го'да", "пять го'ды"], "пять лет", "After 5+: лет."),
    ],
)

# ---------------------------------------------------------------------------- 186
L186 = lesson(
    "Of new friends, of all those: adjectives in the genitive plural",
    "У меня' нет ру'сских друзе'й.",
    requires=["новый", "русский", "мой", "этот", "весь"],
    cards=[
        card("-ых or -их",
             "Adjectives take -ых after a hard stem and -их after к, г, х, ж, ч, ш, щ and after a soft stem. The same "
             "ending serves all three genders, so you only need to learn one form for the plural.",
             tables=[table(
                 ["Nominative plural", "Genitive plural"],
                 [["но'вые", "но'в{ых}"],
                  ["больши'е", "больш{и'х}"],
                  ["ру'сские", "ру'сск{их}"],
                  ["хоро'шие", "хоро'ш{их}"],
                  ["после'дние", "после'дн{их}"],
                  ["больны'е", "больн{ы'х}"]])],
             examples=[
                 ex("У меня' нет ру'сских друзе'й.", "I have no Russian friends.", "ру'сских"),
                 ex("Он зна'ет мно'го но'вых слов.", "He knows many new words.", "но'вых"),
                 ex("Ско'лько у вас хоро'ших друзе'й?", "How many good friends do you have?", "хоро'ших"),
             ]),
        card("Pronouns and “all”",
             "Possessives, demonstratives and “all” follow the same pattern: -их with soft or ш/щ stems, and the "
             "special forms мои'х, твои'х, свои'х, всех, тех.",
             tables=[table(
                 ["Nominative plural", "Genitive plural"],
                 [["мои'", "мо{и'х}"],
                  ["твои'", "тво{и'х}"],
                  ["на'ши", "на'ш{их}"],
                  ["ва'ши", "ва'ш{их}"],
                  ["э'ти", "э'т{их}"],
                  ["те", "т{ех}"],
                  ["все", "вс{ех}"],
                  ["каки'е", "как{и'х}"]])],
             examples=[
                 ex("Э'то фотогра'фии мои'х роди'телей.", "These are photographs of my parents.", "мои'х"),
                 ex("В магази'не нет тех книг.", "There are none of those books in the store.", "тех"),
                 ex("Мы получи'ли письма' от всех на'ших друзе'й.", "We received letters from all our friends.", "всех"),
             ]),
    ],
    verify=(vf("новый", "новых") + vf("большой", "больших") + vf("русский", "русских") + vf("хороший", "хороших")
            + vf("последний", "последних") + vf("больной", "больных") + vf("мой", "моих") + vf("твой", "твоих")
            + vf("наш", "наших") + vf("ваш", "ваших") + vf("этот", "этих") + vf("тот", "тех") + vf("весь", "всех")
            + vf("какой", "каких") + vf("друг", "друзей") + vf("родитель", "родителей") + vf("слово", "слов")),
    exercises=[
        F("У меня' нет ___ друзе'й. (Russian)", "ру'сских", ["ру'сские", "ру'сским", "ру'сскими"], "After к: -их.", "I have no Russian friends.", lemma="русский"),
        F("Мы зна'ем мно'го ___ слов. (new)", "но'вых", ["но'вые", "но'вым", "но'выми"], "Hard stem: -ых.", "We know many new words.", lemma="новый"),
        F("Э'то фотогра'фии ___ роди'телей. (my)", "мои'х", ["мои'м", "мои'", "мои'ми"], "Мой → мои'х.", "These are photographs of my parents.", lemma="мой"),
        F("В магази'не нет ___ книг. (those)", "тех", ["те", "тем", "те'ми"], "Тот → тех.", "There are none of those books in the store.", lemma="тот"),
        F("Ско'лько ___ городо'в ты ви'дел? (big)", "больши'х", ["больши'е", "больши'м", "больши'ми"], "Big: больши'х.", "How many big cities have you seen?", lemma="большой"),
        F("У нас ма'ло ___ маши'н. (good)", "хоро'ших", ["хоро'шие", "хоро'шим", "хоро'шими"], "After ш: -их.", "We have few good cars.", lemma="хороший"),
        F("У нас нет ___ книг. (these)", "э'тих", ["э'ти", "э'тим", "э'тими"], "Э'тот → э'тих.", "We have none of these books.", lemma="этот"),
        mc("Which ending do adjectives take in the genitive plural after к, г, х, ж, ч, ш, щ?", ["-их", "-ых", "-ым", "-ой"], "-их", "-их after those letters.", order=True),
        mc("What is the genitive plural of мои'?", ["мои'х", "мои'м", "моего'", "мои'ми"], "мои'х", "Мои' → мои'х."),
    ],
)

# ---------------------------------------------------------------------------- 187
L187 = lesson(
    "Two new books, five new books: numbers with adjectives",
    "У нас два но'вых преподава'теля.",
    requires=["интересный", "новый", "большой", "друг", "книга"],
    cards=[
        card("2, 3, 4 and 5 and more",
             "After 2, 3 and 4 the noun is in the genitive singular. The adjective before it is in the genitive plural "
             "for masculine and neuter nouns, but in the nominative plural for feminine nouns. After 5 and more, "
             "both the noun and the adjective are in the genitive plural.",
             tables=[table(
                 ["Gender", "2, 3, 4", "5 and more"],
                 [["Masculine", "два но'в{ых} стола'", "пять но'в{ых} столо'в"],
                  ["Feminine", "две но'в{ые} кни'ги", "пять но'в{ых} книг"],
                  ["Neuter", "три больш{и'х} окна'", "пять больш{и'х} о'кон"]])],
             examples=[
                 ex("У нас два но'вых преподава'теля.", "We have two new teachers.", "два но'вых преподава'теля"),
                 ex("Я купи'л две интере'сные кни'ги.", "I bought two interesting books.", "две интере'сные кни'ги"),
                 ex("В ко'мнате три больши'х окна'.", "There are three big windows in the room.", "три больши'х окна'"),
                 ex("В ко'мнате пять больши'х о'кон.", "There are five big windows in the room.", "пять больши'х о'кон"),
             ]),
        card("Longer numbers",
             "Only the last word of the number matters: 22, 23 and 24 work like 2, 3 and 4, and 25 works like 5.",
             examples=[
                 ex("В институ'те два'дцать два но'вых преподава'теля.", "There are twenty-two new teachers at the institute.", "два'дцать два но'вых преподава'теля"),
                 ex("В институ'те два'дцать пять но'вых преподава'телей.", "There are twenty-five new teachers at the institute.", "два'дцать пять но'вых преподава'телей"),
             ]),
    ],
    verify=(vf("новый", "новых", "новые") + vf("большой", "больших") + vf("интересный", "интересные", "интересных")
            + vf("преподаватель", "преподавателя", "преподавателей") + vf("стол", "стола", "столов")
            + vf("книга", "книги", "книг") + vf("окно", "окна", "окон") + vf("друг", "друга", "друзей")),
    exercises=[
        F("У меня' два ___ бра'та. (older)", "ста'рших", ["ста'рший", "ста'ршая", "ста'ршее"], "Masculine after 2: genitive plural adjective.", "I have two older brothers."),
        F("Мы ви'дели три ___ окна'. (big)", "больши'х", ["большо'е", "большо'й", "большу'ю"], "Neuter after 3: genitive plural adjective.", "We saw three big windows.", lemma="большой"),
        F("У неё две ___ сестры'. (younger)", "мла'дшие", ["мла'дшая", "мла'дшей", "мла'дшую"], "Feminine after 2: nominative plural adjective.", "She has two younger sisters."),
        F("Я купи'л две ___ кни'ги. (interesting)", "интере'сные", ["интере'сный", "интере'сной", "интере'сную"], "Feminine after 2: nominative plural adjective.", "I bought two interesting books.", lemma="интересный"),
        F("У нас пять ___ студе'нтов. (new)", "но'вых", ["но'вые", "но'вый", "но'вого"], "After 5: genitive plural.", "We have five new students.", lemma="новый"),
        F("Мы купи'ли пять ___ книг. (interesting)", "интере'сных", ["интере'сные", "интере'сная", "интере'сной"], "After 5: genitive plural.", "We bought five interesting books.", lemma="интересный"),
        F("В ко'мнате шесть ___ о'кон. (big)", "больши'х", ["больши'е", "большо'е", "большо'й"], "After 6: genitive plural.", "There are six big windows in the room.", lemma="большой"),
        mc("After 2, 3 and 4, a feminine adjective stands in the...", ["nominative plural", "genitive plural", "genitive singular", "dative plural"], "nominative plural", "Feminine: две но'вые кни'ги."),
        mc("After 5 and more, adjective and noun are both in the...", ["genitive plural", "nominative plural", "genitive singular", "accusative singular"], "genitive plural", "5+ → genitive plural."),
    ],
)

# ---------------------------------------------------------------------------- 188
L188 = lesson(
    "A lot of water, a little time: countable and uncountable",
    "У меня' ма'ло вре'мени и мно'го рабо'ты.",
    requires=["вода", "время", "работа", "молоко", "хлеб"],
    cards=[
        card("Things you can count, things you cannot",
             "After мно'го, ма'ло, ско'лько and сто'лько use the genitive plural for things you can count, but the "
             "genitive singular for things you cannot count: water, milk, time, work. Не'сколько always counts things, "
             "so for uncountable things use немно'го (a little).",
             tables=[table(
                 ["Countable: genitive plural", "Uncountable: genitive singular"],
                 [["мно'го книг", "мно'го воды'"],
                  ["ма'ло студе'нтов", "ма'ло вре'мени"],
                  ["сто'лько пробле'м", "сто'лько рабо'ты"],
                  ["ско'лько друзе'й", "ско'лько молока'"]])],
             examples=[
                 ex("У меня' ма'ло вре'мени и мно'го рабо'ты.", "I have little time and a lot of work.", "вре'мени"),
                 ex("В ча'шке ма'ло воды'.", "There is little water in the cup.", "воды'"),
                 ex("Мне ну'жно немно'го хле'ба.", "I need a little bread.", "хле'ба"),
             ]),
        card("More uncountable words",
             "Words for liquids, foods, materials, feelings and abstract ideas are usually uncountable.",
             tables=[table(
                 ["Nominative", "Genitive singular"],
                 [["вода'", "воды'"],
                  ["молоко'", "молока'"],
                  ["хлеб", "хле'ба"],
                  ["вре'мя", "вре'мени"],
                  ["рабо'та", "рабо'ты"],
                  ["снег", "сне'га"],
                  ["информа'ция", "информа'ции"]])],
             examples=[
                 ex("В холоди'льнике ма'ло молока'.", "There is little milk in the refrigerator.", "молока'"),
                 ex("За'втра бу'дет мно'го сне'га.", "Tomorrow there will be a lot of snow.", "сне'га"),
             ]),
        card("Most of...",
             "Большинство' (most) is followed by the genitive plural. The verb is usually singular.",
             examples=[
                 ex("Большинство' студе'нтов живёт в Москве'.", "Most of the students live in Moscow.", "Большинство' студе'нтов"),
             ]),
    ],
    verify=(vf("вода", "воды") + vf("молоко", "молока") + vf("хлеб", "хлеба") + vf("время", "времени")
            + vf("работа", "работы") + vf("снег", "снега") + vf("информация", "информации")
            + vf("проблема", "проблем") + vf("холодильник", "холодильнике")),
    exercises=[
        F("В ча'шке ма'ло ___. (water)", "воды'", ["вода'", "воду'", "водо'й"], "Uncountable: genitive singular.", "There is little water in the cup.", lemma="вода"),
        F("Мне ну'жно немно'го ___. (bread)", "хле'ба", ["хлеб", "хле'бов", "хле'бу"], "Uncountable: genitive singular.", "I need a little bread.", lemma="хлеб"),
        F("У меня' сего'дня мно'го ___. (work)", "рабо'ты", ["рабо'та", "рабо'той", "рабо'ту"], "Uncountable: genitive singular.", "I have a lot of work today.", lemma="работа"),
        F("Ско'лько у вас ___? (time)", "вре'мени", ["вре'мя", "времена'", "вре'менем"], "Uncountable: genitive singular.", "How much time do you have?", lemma="время"),
        F("В холоди'льнике ма'ло ___. (milk)", "молока'", ["молоко'", "молоко'м", "моло'ку"], "Uncountable: genitive singular.", "There is little milk in the refrigerator.", lemma="молоко"),
        F("У меня' ма'ло ___. (friends)", "друзе'й", ["друга'", "друзья'", "дру'гу"], "Countable: genitive plural.", "I have few friends.", lemma="друг"),
        F("Большинство' ___ живёт в Москве'. (students)", "студе'нтов", ["студе'нты", "студе'нтам", "студе'нта"], "Большинство' + genitive plural.", "Most of the students live in Moscow.", lemma="студент"),
        mc("Which noun is countable?", ["кни'га", "вода'", "молоко'", "вре'мя"], "кни'га", "You can count books."),
        mc("What do you use after мно'го with an uncountable noun?", ["genitive singular", "genitive plural", "nominative plural", "dative singular"], "genitive singular", "Мно'го воды'."),
    ],
)

# ---------------------------------------------------------------------------- 189
L189 = lesson(
    "Two of them, three children: двое, трое, четверо",
    "У них дво'е дете'й.",
    requires=["ребёнок", "друг", "человек", "сосед", "сутки"],
    cards=[
        card("Collective numerals",
             "For groups of male persons and for children there is a second set of numerals. They are followed by the "
             "genitive plural. They are not used for women, so say две сестры', not дво'е сестёр.",
             tables=[table(
                 ["Numeral", "Example"],
                 [["дво'е", "дво'е студе'нтов"],
                  ["тро'е", "тро'е дете'й"],
                  ["че'тверо", "че'тверо друзе'й"],
                  ["пя'теро", "пя'теро сосе'дей"],
                  ["ше'стеро", "ше'стеро ма'льчиков"],
                  ["се'меро", "се'меро дете'й"]])],
             examples=[
                 ex("У них дво'е дете'й.", "They have two children.", "дво'е дете'й"),
                 ex("У нас че'тверо сосе'дей.", "We have four neighbors.", "че'тверо сосе'дей"),
                 ex("Нас бы'ло тро'е.", "There were three of us.", "тро'е"),
             ]),
        card("Plural-only nouns",
             "The same numerals are used with nouns that exist only in the plural, such as су'тки (a day and night), "
             "но'жницы (scissors) and часы' (watch).",
             examples=[
                 ex("Мы жда'ли дво'е су'ток.", "We waited for two days.", "дво'е су'ток"),
                 ex("Мне нужны' тро'е но'жниц.", "I need three pairs of scissors.", "тро'е но'жниц"),
             ]),
    ],
    verify=(vf("ребёнок", "детей") + vf("друг", "друзей") + vf("сосед", "соседей") + vf("мальчик", "мальчиков")
            + vf("сутки", "суток") + vf("ножницы", "ножниц")),
    exercises=[
        F("У них ___ дете'й. (three)", "тро'е", ["три", "тре'тий", "тре'тье"], "Children: collective numeral.", "They have three children."),
        F("Нас бы'ло ___. (two)", "дво'е", ["два", "две", "второ'е"], "Two people: дво'е.", "There were two of us."),
        F("У нас ___ сосе'дей. (four)", "че'тверо", ["четы'ре", "четвёртый", "четвёртое"], "Persons: collective numeral.", "We have four neighbors."),
        F("У неё ___ сестры'. (two)", "две", ["дво'е", "два", "второ'й"], "Women: normal numeral две.", "She has two sisters."),
        F("Мы жда'ли ___ су'ток. (two)", "дво'е", ["два", "две", "второ'е"], "Plural-only noun: collective numeral.", "We waited for two days."),
        F("В кла'ссе пя'теро ___. (boys)", "ма'льчиков", ["ма'льчики", "ма'льчика", "ма'льчикам"], "Collective numeral + genitive plural.", "There are five boys in the class.", lemma="мальчик"),
        mc("Which is correct?", ["две сестры'", "дво'е сестёр", "два сестры'", "дво'е сестры'"], "две сестры'", "Collective numerals are not used for women."),
        mc("What case follows the collective numerals?", ["genitive plural", "nominative plural", "genitive singular", "dative plural"], "genitive plural", "Дво'е дете'й."),
    ],
)

# ---------------------------------------------------------------------------- 190
L190 = lesson(
    "Without friends, after classes: prepositions with the genitive plural",
    "По'сле заня'тий мы идём домо'й.",
    requires=["без", "после", "около", "для", "от"],
    cards=[
        card("Prepositions that take the genitive",
             "Every preposition that takes the genitive singular takes the genitive plural too. Here are the common ones.",
             tables=[table(
                 ["Preposition", "Meaning", "Example"],
                 [["без", "without", "Он пришёл без друзе'й."],
                  ["от", "from", "Я получи'л письмо' от роди'телей."],
                  ["до", "before, until", "Мы пришли' до заня'тий."],
                  ["по'сле", "after", "По'сле уро'ков мы идём домо'й."],
                  ["у", "at (someone's)", "У мои'х друзе'й больша'я кварти'ра."],
                  ["из", "out of", "Оди'н из студе'нтов опозда'л."],
                  ["с", "from (off)", "Мы верну'лись с заня'тий."],
                  ["из-за", "because of", "Из-за пробле'м мы не пое'хали."],
                  ["для", "for", "Э'то пода'рки для дете'й."]])],
             examples=[
                 ex("Он пришёл без друзе'й.", "He came without his friends.", "без друзе'й"),
                 ex("По'сле уро'ков мы идём домо'й.", "After lessons we go home.", "По'сле уро'ков"),
                 ex("Э'то пода'рки для дете'й.", "These are gifts for the children.", "для дете'й"),
             ]),
        card("“Of” and “one of”",
             "A noun in the genitive plural after another noun means “of”. After оди'н, ка'ждый and не'которые "
             "use из with the genitive plural.",
             examples=[
                 ex("Э'то дом мои'х роди'телей.", "This is my parents' house.", "мои'х роди'телей"),
                 ex("Оди'н из мои'х друзе'й живёт в Ки'еве.", "One of my friends lives in Kyiv.", "из мои'х друзе'й"),
                 ex("Ка'ждый из студе'нтов получи'л кни'гу.", "Each of the students received a book.", "из студе'нтов"),
             ]),
    ],
    verify=(vf("друг", "друзей") + vf("родитель", "родителей") + vf("занятие", "занятий") + vf("урок", "уроков")
            + vf("студент", "студентов") + vf("проблема", "проблем") + vf("ребёнок", "детей") + vf("мой", "моих")
            + vf("получить", "получил") + vf("опоздать", "опоздал") + vf("подарок", "подарки")),
    exercises=[
        F("Он пришёл на вечери'нку без ___. (friends)", "друзе'й", ["друзья'", "дру'га", "дру'гу"], "Без + genitive plural.", "He came to the party without his friends.", lemma="друг"),
        F("Я получи'л письмо' от ___. (parents)", "роди'телей", ["роди'тели", "роди'телям", "роди'теля"], "От + genitive plural.", "I received a letter from my parents.", lemma="родитель"),
        F("Мы пришли' до ___. (classes)", "заня'тий", ["заня'тия", "заня'тиям", "заня'тие"], "До + genitive plural.", "We arrived before the classes.", lemma="занятие"),
        F("По'сле ___ мы идём домо'й. (lessons)", "уро'ков", ["уро'ки", "уро'кам", "уро'ка"], "По'сле + genitive plural.", "After the lessons we go home.", lemma="урок"),
        F("Оди'н из мои'х ___ живёт в Ки'еве. (friends)", "друзе'й", ["друзья'", "друзья'м", "дру'га"], "Из + genitive plural.", "One of my friends lives in Kyiv.", lemma="друг"),
        F("У мои'х ___ больша'я кварти'ра. (parents)", "роди'телей", ["роди'тели", "роди'телям", "роди'теля"], "У + genitive plural.", "My parents have a big apartment.", lemma="родитель"),
        F("Из-за ___ мы не пое'хали. (problems)", "пробле'м", ["пробле'мы", "пробле'ме", "пробле'му"], "Из-за + genitive plural.", "Because of problems we did not go.", lemma="проблема"),
        F("Э'то пода'рки для ___. (children)", "дете'й", ["де'ти", "де'тям", "ребёнка"], "Для + genitive plural.", "These are gifts for the children.", lemma="ребёнок"),
        mc("What case do без, от, до, по'сле, из and для take?", ["genitive", "dative", "instrumental", "accusative"], "genitive", "All take the genitive."),
    ],
)

# ---------------------------------------------------------------------------- 191
L191 = lesson(
    "I know the students: the accusative plural of animate nouns",
    "Я зна'ю э'тих студе'нтов.",
    requires=["студент", "родитель", "друг", "сосед", "журнал"],
    cards=[
        card("Animate = genitive, inanimate = nominative",
             "In the accusative plural, nouns for people and animals look like the genitive plural. Nouns for things "
             "look like the nominative plural. Adjectives and pronouns follow the noun.",
             tables=[table(
                 ["Plural subject", "Direct object", "Kind"],
                 [["студе'нты", "студе'нтов", "animate"],
                  ["но'вые друзья'", "но'вых друзе'й", "animate"],
                  ["мои' роди'тели", "мои'х роди'телей", "animate"],
                  ["на'ши сосе'ди", "на'ших сосе'дей", "animate"],
                  ["журна'лы", "журна'лы", "inanimate"],
                  ["но'вые кни'ги", "но'вые кни'ги", "inanimate"],
                  ["больши'е о'кна", "больши'е о'кна", "inanimate"]])],
             examples=[
                 ex("Я зна'ю э'тих студе'нтов.", "I know these students.", "э'тих студе'нтов"),
                 ex("Мы ви'дели мои'х роди'телей.", "We saw my parents.", "мои'х роди'телей"),
                 ex("Я чита'ю но'вые журна'лы.", "I am reading new magazines.", "но'вые журна'лы"),
             ]),
        card("More examples",
             "Remember this for all the verbs that take a direct object: знать, ви'деть, люби'ть, ждать, звать.",
             examples=[
                 ex("Она' лю'бит свои'х дете'й.", "She loves her children.", "свои'х дете'й"),
                 ex("Вы ви'дели на'ших сосе'дей?", "Did you see our neighbors?", "на'ших сосе'дей"),
                 ex("Мы ждём э'тих госте'й.", "We are waiting for these guests.", "э'тих госте'й"),
             ]),
    ],
    verify=(vf("студент", "студентов") + vf("родитель", "родителей") + vf("ребёнок", "детей")
            + vf("журнал", "журналы") + vf("друг", "друзей") + vf("сосед", "соседей") + vf("окно", "окна")
            + vf("гость", "гостей") + vf("свой", "своих") + vf("этот", "этих")),
    exercises=[
        F("Я зна'ю э'тих ___. (students)", "студе'нтов", ["студе'нты", "студе'нтам", "студе'нта"], "Animate: accusative = genitive plural.", "I know these students.", lemma="студент"),
        F("Мы ви'дели мои'х ___ в па'рке. (parents)", "роди'телей", ["роди'тели", "роди'телям", "роди'теля"], "Animate: accusative = genitive plural.", "We saw my parents in the park.", lemma="родитель"),
        F("Она' лю'бит свои'х ___. (children)", "дете'й", ["де'ти", "де'тям", "ребёнка"], "Animate: accusative = genitive plural.", "She loves her children.", lemma="ребёнок"),
        F("Я чита'ю но'вые ___. (magazines)", "журна'лы", ["журна'лов", "журна'лам", "журна'ла"], "Inanimate: accusative = nominative plural.", "I am reading new magazines.", lemma="журнал"),
        F("Мы ждём на'ших ___. (friends)", "друзе'й", ["друзья'", "друзья'м", "дру'га"], "Animate: accusative = genitive plural.", "We are waiting for our friends.", lemma="друг"),
        F("Вы ви'дели э'ти ___? (windows)", "о'кна", ["о'кон", "окно'", "о'кнам"], "Inanimate: accusative = nominative plural.", "Did you see these windows?", lemma="окно"),
        F("Он зна'ет всех ___. (neighbors)", "сосе'дей", ["сосе'ди", "сосе'дям", "сосе'д"], "Animate: accusative = genitive plural.", "He knows all the neighbors.", lemma="сосед"),
        mc("The accusative plural of animate nouns is identical to the...", ["genitive plural", "nominative plural", "dative plural", "genitive singular"], "genitive plural", "Animate: genitive plural."),
        mc("The accusative plural of inanimate nouns is identical to the...", ["nominative plural", "genitive plural", "dative plural", "instrumental plural"], "nominative plural", "Inanimate: nominative plural."),
    ],
)

# ---------------------------------------------------------------------------- 192
L192 = lesson(
    "Review: the genitive plural",
    "У нас мно'го книг, друзе'й и зда'ний.",
    requires=["книга", "окно", "год", "друг", "комната"],
    cards=[
        card("All the endings in one table",
             "Look at the last letter of the singular and choose the ending.",
             tables=[table(
                 ["Singular ends in", "Genitive plural", "Example"],
                 [["hard consonant", "-ов", "студе'нтов, столо'в"],
                  ["-й", "-ев", "музе'ев"],
                  ["-ь, ж ч ш щ", "-ей", "учителе'й, ноже'й"],
                  ["-ец", "-цев / -цов", "америка'нцев, отцо'в"],
                  ["-а, -о", "no ending", "книг, слов, стран"],
                  ["-ка, -ня, -о after two consonants", "fleeting vowel", "студе'нток, пе'сен, о'кон"],
                  ["-ь (feminine), -е", "-ей", "ноче'й, море'й"],
                  ["-ия, -ие", "-ий", "ле'кций, зда'ний"],
                  ["adjectives", "-ых / -их", "но'вых, ру'сских"]])],
             examples=[
                 ex("У нас мно'го книг, друзе'й и зда'ний.", "We have many books, friends and buildings.", "друзе'й"),
             ]),
        card("The irregular words",
             "Learn these by heart: друзе'й, бра'тьев, сынове'й, матере'й, дочере'й, сестёр, дете'й, люде'й, челове'к, "
             "лет, раз, дней, имён, де'нег.",
             examples=[
                 ex("Я жил там пять лет и ви'дел мно'го люде'й.", "I lived there for five years and saw many people.", "люде'й"),
             ]),
    ],
    verify=(vf("книга", "книг") + vf("окно", "окон") + vf("год", "лет") + vf("друг", "друзей")
            + vf("комната", "комнат") + vf("здание", "зданий") + vf("человек", "людей")
            + vf("сын", "сыновей") + vf("музей", "музеев") + vf("учитель", "учителей") + vf("песня", "песен")),
    exercises=[
        F("В институ'те мно'го ___. (students)", "студе'нтов", ["студе'нты", "студе'нтам", "студе'нта"], "Hard consonant: -ов.", "There are many students at the institute.", lemma="студент"),
        F("Ско'лько ___ в ва'шем до'ме? (rooms)", "ко'мнат", ["ко'мнаты", "ко'мнате", "ко'мнату"], "Drop -а.", "How many rooms are in your house?", lemma="комната"),
        F("В э'той ко'мнате три больши'х ___. (windows)", "окна'", ["о'кон", "о'кна", "окно'"], "After 3: genitive singular.", "There are three big windows in this room.", lemma="окно"),
        F("Я живу' здесь пять ___. (years)", "лет", ["годо'в", "го'да", "го'ды"], "After 5: лет.", "I have lived here for five years."),
        F("У меня' мно'го ру'сских ___. (friends)", "друзе'й", ["друзья'", "друзья'м", "дру'га"], "Друг → друзе'й.", "I have many Russian friends.", lemma="друг"),
        F("В Москве' мно'го ___. (museums)", "музе'ев", ["музе'ов", "музе'и", "музе'ям"], "-й → -ев.", "There are many museums in Moscow.", lemma="музей"),
        F("В гру'ппе мно'го ___. (female students)", "студе'нток", ["студе'нтки", "студе'нтк", "студе'нткам"], "Fleeting vowel.", "There are many female students in the group.", lemma="студентка"),
        F("В на'шем го'роде мно'го ___. (buildings)", "зда'ний", ["зда'ния", "зда'нию", "зда'нием"], "-ие → -ий.", "There are many buildings in our city.", lemma="здание"),
        F("Мы ви'дели мои'х ___. (parents)", "роди'телей", ["роди'тели", "роди'телям", "роди'теля"], "Animate accusative = genitive plural.", "We saw my parents.", lemma="родитель"),
        F("У неё ___ дете'й. (three)", "тро'е", ["три", "тре'тий", "тре'тье"], "Children: collective numeral.", "She has three children."),
        mc("What is the genitive plural of сестра'?", ["сестёр", "сестро'в", "сестре'й", "сестра'м"], "сестёр", "Irregular."),
    ],
)

UNIT = unit("Unit 20: Many, few, five: the genitive plural",
            [L180, L181, L182, L183, L184, L185, L186, L187, L188, L189, L190, L191, L192])
