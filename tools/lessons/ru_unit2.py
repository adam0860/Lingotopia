"""Unit 2: more than one: plurals, numbers, family  (textbook lessons 3-4)."""
from dsl import *

# ---------------------------------------------------------------------------- 8
L8 = lesson(
    "Regular plurals",
    "-ы, -и, -а, -я: the ending depends on the last letter",
    requires=["книга", "школа", "окно", "слово", "письмо", "время"],
    cards=[
        card("Making a plural",
             "For most nouns the plural ending depends on the last letter of the dictionary form. Tap a row to "
             "hear the words. The ending being added is highlighted.",
             tables=[table(
                 ["Singular ends in", "Plural ending", "Singular → plural"],
                 [["a consonant", "-ы", "стол → стол{ы'}  ·  журна'л → журна'л{ы}"],
                  ["-а", "-ы", "шко'ла → шко'л{ы}  ·  ко'мната → ко'мнат{ы}"],
                  ["-ь, -й, -я", "-и", "тетра'дь → тетра'д{и}  ·  музе'й → музе'{и}  ·  неде'ля → неде'л{и}"],
                  ["-ия", "-ии", "ста'нция → ста'нци{и}"],
                  ["-о", "-а", "окно' → о'кн{а}  ·  письмо' → пи'сьм{а}"],
                  ["-е", "-я", "мо'ре → мор{я'}"],
                  ["-ие", "-ия", "зда'ние → зда'ни{я}"],
                  ["-мя", "-мена", "и'мя → им{ена'}  ·  вре'мя → врем{ена'}"]])]),
        card("A spelling rule, and a moving stress",
             "After г, к, х, ж, ч, ш, щ Russian never writes ы: it writes и instead. So кни'га becomes кни'ги "
             "(never кни'гы), and нож becomes ножи'.\n\n"
             "Also watch the stress. It often moves when the word becomes plural: стол → столы' (onto the "
             "ending), but окно' → о'кна (back onto the stem). Stress is not written in ordinary Russian "
             "text, so learn it together with the word.",
             tables=[table(
                 ["After…", "Write", "Example"],
                 [["г, к, х", "и, never ы", "кни'га → кни'ги  ·  ру'чка → ру'чки"],
                  ["ж, ч, ш, щ", "и, never ы", "нож → нож{и'}  ·  врач → врач{и'}"]])]),
    ],
    verify=[("стол", "столы"), ("журнал", "журналы"), ("школа", "школы"), ("комната", "комнаты"),
            ("тетрадь", "тетради"), ("музей", "музеи"), ("неделя", "недели"), ("станция", "станции"),
            ("окно", "окна"), ("письмо", "письма"), ("море", "моря"), ("здание", "здания"),
            ("имя", "имена"), ("время", "времена"), ("книга", "книги"), ("ручка", "ручки"),
            ("нож", "ножи"), ("врач", "врачи")],
    exercises=[
        mc("What is the plural of стол?", ["столы", "столи", "стола", "столя"], "столы",
           "A consonant ending takes -ы: стол → столы'.", lemma="стол"),
        mc("What is the plural of кни'га?", ["книги", "книгы", "книга", "книгу"], "книги",
           "Feminine -а normally gives -ы, but after г the spelling rule requires и: кни'ги.", lemma="книга"),
        mc("What is the plural of окно'?", ["окна", "окны", "окни", "окно"], "окна",
           "Neuter -о becomes -а, and the stress moves back: о'кна.", lemma="окно"),
        mc("What is the plural of неде'ля?", ["недели", "недельы", "недела", "неделя"], "недели",
           "Feminine -я becomes -и: неде'ли.", lemma="неделя"),
        mc("What is the plural of музе'й?", ["музеи", "музеы", "музея", "музей"], "музеи",
           "Masculine -й becomes -и: музе'и.", lemma="музей"),
        mc("What is the plural of ру'чка?", ["ручки", "ручкы", "ручка", "ручку"], "ручки",
           "After к, ы is never written: ру'чки.", lemma="ручка"),
        mc("What is the plural of зда'ние?", ["здания", "здании", "здание", "здани"], "здания",
           "Neuter -ие becomes -ия: зда'ния.", lemma="здание"),
        mc("What is the plural of и'мя?", ["имена", "имя", "имени", "имены"], "имена",
           "Neuter nouns in -мя take -мена, with the stress on the end: имена'. Вре'мя → времена' works the same way.",
           lemma="имя"),
        mc("What is the plural of врач?", ["врачи", "врачы", "врача", "врачей"], "врачи",
           "After ч only и is written: врачи'.", lemma="врач"),
        mc("After г, к, х, ж, ч, ш, щ, which plural ending is written?", ["и", "ы", "а", "я"], "и",
           "This is the spelling rule: ы is replaced by и after those seven letters."),
    ],
)

# ---------------------------------------------------------------------------- 9
L9 = lesson(
    "Whose? and plural possessives",
    "Чей, чья, чьё, чьи, and мои', твои', на'ши, ва'ши",
    requires=["чей", "мой", "твой", "наш", "ваш"],
    cards=[
        card("Possessives in the plural",
             "Possessives agree with their noun in gender and in number. In the plural there is one form for all "
             "three genders: мои' books, мои' windows, мои' brothers. The question word Whose? works the same "
             "way, so the form of чей tells you what kind of noun is coming.",
             tables=[table(
                 ["", "Masculine", "Feminine", "Neuter", "Plural"],
                 [["Whose?", "чей", "чья", "чьё", "чьи"],
                  ["my", "мой", "моя'", "моё'", "мо{и'}"],
                  ["your (familiar)", "твой", "твоя'", "твоё'", "тво{и'}"],
                  ["our", "наш", "на'ша", "на'ше", "на'ш{и}"],
                  ["your (polite/plural)", "ваш", "ва'ша", "ва'ше", "ва'ш{и}"]],
                 note="Его' (his), её' (her) and их (their) never change, in the plural either.")],
             examples=[
                 ex("Чей э'то дом? — Э'то мой дом.", "Whose house is this? — It's my house."),
                 ex("Чья э'то газе'та? — Э'то ва'ша газе'та.", "Whose newspaper is this? — It's your newspaper."),
                 ex("Чьё э'то окно'? — Э'то на'ше окно'.", "Whose window is this? — It's our window."),
                 ex("Чьи э'то кни'ги? — Э'то мои' кни'ги.", "Whose books are these? — They're my books."),
             ]),
    ],
    verify=[("мой", "мои"), ("твой", "твои"), ("наш", "наши"), ("ваш", "ваши"),
            ("чей", "чья"), ("чей", "чьё"), ("чей", "чьи")],
    exercises=[
        fb("___ э'то дом?", ["Чей", "Чья", "Чьё", "Чьи"], "Чей",
           "Дом is masculine, so чей.", tr="Whose house is this?"),
        fb("___ э'то кни'га?", ["Чья", "Чей", "Чьё", "Чьи"], "Чья",
           "Кни'га is feminine, so чья.", tr="Whose book is this?"),
        fb("___ э'то окно'?", ["Чьё", "Чей", "Чья", "Чьи"], "Чьё",
           "Окно' is neuter, so чьё.", tr="Whose window is this?"),
        fb("___ э'то де'ти?", ["Чьи", "Чей", "Чья", "Чьё"], "Чьи",
           "Де'ти is plural, so чьи.", tr="Whose children are these?"),
        fb("Э'то ___ кни'ги.", ["мои'", "мой", "моя'", "моё'"], "мои'",
           "Plural noun, so the plural form мои'.", tr="These are my books."),
        fb("Вот ___ очки'.", ["твои'", "твой", "твоя'", "твоё'"], "твои'",
           "Очки' is plural, so твои'.", tr="Here are your glasses. (familiar)"),
        fb("___ роди'тели до'ма?", ["Ва'ши", "Ваш", "Ва'ша", "Ва'ше"], "Ва'ши",
           "Роди'тели is plural, so ва'ши.", tr="Are your (polite) parents at home?"),
        fb("Э'то ___ друзья'.", ["его'", "мои'", "наш", "ва'ши"], "его'",
           "Его' means “his” and never changes: его' друзья'.", tr="These are his friends."),
        mc("How many plural forms does мой have?",
           ["One: мои', for every gender", "Two", "Three", "Four"], "One: мои', for every gender",
           "Gender disappears in the plural.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 10
L10 = lesson(
    "Numbers 0–10",
    "Counting, and the genders of one and two",
    requires=["один", "ноль", "студент", "книга", "окно"],
    cards=[
        card("Zero to ten",
             "These eleven words are the foundation for telling time, giving phone numbers and paying. Tap a "
             "number to hear it.",
             tables=[table(
                 ["Number", "Russian", "Number", "Russian"],
                 [["0", "ноль", "6", "шесть"],
                  ["1", "оди'н", "7", "семь"],
                  ["2", "два", "8", "во'семь"],
                  ["3", "три", "9", "де'вять"],
                  ["4", "четы'ре", "10", "де'сять"],
                  ["5", "пять", "", ""]])]),
        card("One and two have genders",
             "Оди'н, одна', одно' agree with the noun. Two has two forms: два goes with masculine and neuter "
             "nouns, две with feminine ones. The noun after два, три and четы'ре changes its form too. You will "
             "see why later, so for now just choose the right number and copy the pairs.",
             tables=[table(
                 ["", "Masculine", "Feminine", "Neuter"],
                 [["1", "оди'н", "одн{а'}", "одн{о'}"],
                  ["2", "два", "дв{е}", "два"]])],
             examples=[
                 ex("Здесь то'лько оди'н студе'нт.", "There is only one student here.", "оди'н"),
                 ex("Здесь то'лько одна' кни'га.", "There is only one book here.", "одна'"),
                 ex("Здесь то'лько одно' окно'.", "There is only one window here.", "одно'"),
                 ex("Здесь два студе'нта.", "There are two students here.", "два"),
                 ex("Здесь две кни'ги.", "There are two books here.", "две"),
                 ex("Здесь два окна'.", "There are two windows here.", "два"),
             ]),
        card("A number after the noun",
             "When a number comes after the noun as a label (a room number, a page, a bus), it never changes "
             "for gender.",
             examples=[
                 ex("но'мер оди'н", "number one", "оди'н"),
                 ex("но'мер два", "number two", "два"),
                 ex("но'мер три", "number three", "три"),
             ]),
    ],
    verify=[("один", "одна"), ("один", "одно"), ("два", "две")],
    exercises=[
        fb("Здесь то'лько ___ студе'нт.", ["оди'н", "одна'", "одно'", "два"], "оди'н",
           "Студе'нт is masculine.", tr="There is only one student here."),
        fb("Здесь то'лько ___ кни'га.", ["одна'", "оди'н", "одно'", "две"], "одна'",
           "Кни'га is feminine.", tr="There is only one book here."),
        fb("Здесь то'лько ___ окно'.", ["одно'", "оди'н", "одна'", "два"], "одно'",
           "Окно' is neuter.", tr="There is only one window here."),
        fb("Здесь ___ кни'ги.", ["две", "два", "одна'", "три"], "две",
           "Two takes the feminine form with a feminine noun.", tr="There are two books here."),
        fb("Здесь ___ окна'.", ["два", "две", "одно'", "одна'"], "два",
           "Два goes with masculine and neuter nouns.", tr="There are two windows here."),
        mc("Which number is 7?", ["семь", "шесть", "во'семь", "де'вять"], "семь",
           "Семь = 7, шесть = 6, во'семь = 8."),
        mc("Which number is 4?", ["четы'ре", "три", "пять", "шесть"], "четы'ре",
           "Четы'ре = 4."),
        mc("Which of these numbers changes with the gender of the noun?",
           ["оди'н", "пять", "семь", "де'сять"], "оди'н",
           "Of these, only one: оди'н, одна', одно'. (Two also does: два, две.)"),
        mc("How do you say “number two” as a label?",
           ["но'мер два", "но'мер две", "два но'мера"], "но'мер два",
           "After the noun the number doesn't change. Два но'мера would mean “two numbers”."),
    ],
)

# ---------------------------------------------------------------------------- 11
L11 = lesson(
    "Irregular plurals",
    "Words you have to learn as pairs",
    requires=["город", "друг", "ребёнок", "человек", "мать", "брат", "сестра", "отец", "дочь", "сын"],
    cards=[
        card("Plurals in -а or -я, with the stress on the ending",
             "Some masculine nouns take -а (or -я after a soft stem) instead of -ы. The stress lands on that "
             "ending. There is no rule for which nouns do this: learn each one as a pair.",
             tables=[table(
                 ["Singular", "Plural", "Meaning"],
                 [["го'род", "город{а'}", "city"],
                  ["дом", "дом{а'}", "house"],
                  ["но'мер", "номер{а'}", "number"],
                  ["по'езд", "поезд{а'}", "train"],
                  ["па'спорт", "паспорт{а'}", "passport"],
                  ["глаз", "глаз{а'}", "eye"],
                  ["учи'тель", "учител{я'}", "teacher"]])]),
        card("-ья, and plurals that look nothing like the singular",
             "Some nouns take -ья. A few have a completely different plural, and a few change a letter. All of them "
             "have to be memorised.",
             tables=[table(
                 ["Type", "Singular", "Plural"],
                 [["-ья", "брат", "бра'т{ья}"],
                  ["-ья", "друг", "друз{ья'}"],
                  ["-ья", "сын", "сын{овья'}"],
                  ["-ья", "стул", "сту'л{ья}"],
                  ["different word", "мать", "ма'тери"],
                  ["different word", "дочь", "до'чери"],
                  ["different word", "ребёнок", "де'ти"],
                  ["different word", "челове'к", "лю'ди"],
                  ["letter changes", "оте'ц", "отц{ы'}"],
                  ["letter changes", "жена'", "жён{ы}"],
                  ["letter changes", "сестра'", "сёстр{ы}"]],
                 note="Отцы' loses the е of оте'ц. Жёны and сёстры change е to ё.")]),
        card("Plural only",
             "A few nouns exist only in the plural. Things that come as a pair or a set are the usual ones. You "
             "say мои' очки' (my glasses) and never use a singular.",
             tables=[table(
                 ["Plural only", "Meaning"],
                 [["очки'", "glasses"], ["часы'", "watch, clock"], ["де'ньги", "money"],
                  ["брю'ки", "trousers"], ["но'жницы", "scissors"], ["воро'та", "gate"]])],
             examples=[
                 ex("Вот мои' очки'.", "Here are my glasses.", "очки'"),
                 ex("Где твои' часы'?", "Where is your watch?", "часы'"),
             ]),
    ],
    verify=[("город", "города"), ("дом", "дома"), ("номер", "номера"), ("поезд", "поезда"),
            ("паспорт", "паспорта"), ("глаз", "глаза"), ("учитель", "учителя"), ("брат", "братья"),
            ("друг", "друзья"), ("сын", "сыновья"), ("стул", "стулья"), ("мать", "матери"),
            ("дочь", "дочери"), ("отец", "отцы"), ("жена", "жёны"), ("сестра", "сёстры")],
    exercises=[
        mc("What is the plural of го'род?", ["города", "городы", "городи", "городья"], "города",
           "Some masculine nouns take -а with the stress on it: города'.", lemma="город"),
        mc("What is the plural of друг?", ["друзья", "другья", "други", "друга"], "друзья",
           "Друг takes -ья and г changes to з: друзья'.", lemma="друг"),
        mc("What is the plural of ребёнок?", ["дети", "ребёнки", "ребёнка", "ребёнков"], "дети",
           "Ребёнок (child) has a different plural: де'ти."),
        mc("What is the plural of челове'к?", ["люди", "человеки", "человека", "людя"], "люди",
           "Челове'к (person) has a different plural: лю'ди."),
        mc("What is the plural of мать?", ["матери", "матеры", "мати", "матьи"], "матери",
           "Мать → ма'тери. Дочь → до'чери follows the same pattern.", lemma="мать"),
        mc("What is the plural of брат?", ["братья", "браты", "брати", "братя"], "братья",
           "Брат takes -ья: бра'тья.", lemma="брат"),
        mc("What is the plural of сестра'?", ["сёстры", "сестры", "сестра", "сёстри"], "сёстры",
           "The е becomes ё in the plural: сёстры.", lemma="сестра"),
        mc("What is the plural of оте'ц?", ["отцы", "отецы", "отца", "отци"], "отцы",
           "The е is lost: отцы'.", lemma="отец"),
        mc("What is the plural of сын?", ["сыновья", "сынья", "сынов", "сыновь"], "сыновья",
           "Сын takes -овья: сыновья'.", lemma="сын"),
        mc("Which of these nouns has no singular?", ["очки'", "стол", "кни'га", "окно'"], "очки'",
           "Очки' (glasses) exists only in the plural, like часы' and де'ньги."),
    ],
)

# ---------------------------------------------------------------------------- 12
L12 = lesson(
    "Patronymics",
    "Иван Петрович, Мария Павловна: the polite way to address adults",
    requires=["отец", "имя", "сын", "дочь", "семья"],
    cards=[
        card("First name and patronymic",
             "Adults you aren't close to are normally addressed by first name and patronymic (о'тчество): a "
             "middle name made from the father's first name. Никола'й Ива'нович means Nikolai, son of Ivan. "
             "Мари'я Па'вловна is Maria, daughter of Pavel. Use it, with вы, for a teacher, a boss, a colleague "
             "or anyone older. A patronymic has a masculine and a feminine form, so it follows the person's sex.",
             examples=[
                 ex("Здра'вствуйте, Мари'я Па'вловна!", "Hello, Maria Pavlovna!", "Мари'я Па'вловна"),
                 ex("Э'то Никола'й Ива'нович.", "This is Nikolai Ivanovich.", "Никола'й Ива'нович"),
             ]),
        card("Forming the patronymic",
             "Take the father's first name and add a suffix, which depends on how his name ends. Watch the "
             "fleeting vowel: Па'вел loses its е.",
             tables=[table(
                 ["Father's name ends in", "Son", "Daughter", "Example"],
                 [["a consonant", "-ович", "-овна", "Ива'н → Ива'нович / Ива'новна"],
                  ["a consonant (loses е)", "-ович", "-овна", "Па'вел → Па'влович / Па'вловна"],
                  ["-й", "-евич", "-евна", "Никола'й → Никола'евич / Никола'евна"],
                  ["-ий", "-ьевич", "-ьевна", "Васи'лий → Васи'льевич / Васи'льевна"],
                  ["-а, -я", "-ич", "-ична / -инична", "Ники'та → Ники'тич / Ники'тична · Илья' → Ильи'ч / Ильи'нична"]],
                 note="A few names are irregular, for example Дми'трий → Дми'триевич.")]),
    ],
    exercises=[
        fb("А'нна, дочь Ива'на: А'нна ___.", ["Ива'новна", "Ива'нович", "Ива'нова", "Ива'нина"], "Ива'новна",
           "A daughter takes -овна after a name ending in a consonant.", tr="Anna, daughter of Ivan."),
        fb("Бори'с, сын Серге'я: Бори'с ___.", ["Серге'евич", "Серге'йович", "Серге'евна", "Серге'ев"], "Серге'евич",
           "Names in -й take -евич for a son and -евна for a daughter.", tr="Boris, son of Sergei."),
        fb("О'льга, дочь Па'вла: О'льга ___.", ["Па'вловна", "Па'веловна", "Па'вловична"], "Па'вловна",
           "Па'вел loses its е before the suffix: Па'вловна.", tr="Olga, daughter of Pavel."),
        fb("Алексе'й, сын Ники'ты: Алексе'й ___.", ["Ники'тич", "Ники'тович", "Ники'товна", "Ники'тична"], "Ники'тич",
           "Names in -а take -ич for a son and -ична for a daughter.", tr="Alexei, son of Nikita."),
        mc("How do you politely address your teacher Мари'я Па'вловна?",
           ["Мари'я Па'вловна", "Ма'ша", "Мари'я Па'вел", "Па'вловна Мари'я"], "Мари'я Па'вловна",
           "First name, then patronymic, with вы."),
        mc("What is the first name of the father of Никола'й Ива'нович?",
           ["Ива'н", "Никола'й", "Ива'нович", "Ни'кола"], "Ива'н",
           "The patronymic is built from the father's first name."),
        mc("Which of these patronymics belongs to a man?",
           ["Васи'льевич", "Васи'льевна", "Ива'новна", "Ники'тична"], "Васи'льевич",
           "-ич endings (-ович, -евич, -ьевич) are masculine; -на endings are feminine."),
        mc("Whom do you normally address by first name and patronymic?",
           ["An adult you aren't close to, such as a teacher or a colleague", "A close friend",
            "A small child", "Your brother"],
           "An adult you aren't close to, such as a teacher or a colleague",
           "It is respectful and slightly formal. Friends and family use the first name alone."),
    ],
)

UNIT = unit("Unit 2: More than one", [L8, L9, L10, L11, L12])
