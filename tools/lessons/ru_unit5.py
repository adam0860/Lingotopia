"""Unit 5: the accusative case, days and bigger numbers  (textbook lessons 7-8)."""
from dsl import *

# ---------------------------------------------------------------------------- 27
L27 = lesson(
    "The accusative: the thing you read, write or see",
    "Я чита'ю кни'гу, Я ви'жу шко'лу",
    requires=["журнал", "письмо", "книга", "газета", "вещь"],
    cards=[
        card("The direct object",
             "The direct object is whatever the action lands on: what you read, write, see, know. In Russian it "
             "goes into the accusative case and answers Что? (what?) or Кого'? (whom?). Nothing goes before "
             "it. For things (not people or animals) most nouns do not change at all. Only feminine nouns in "
             "-а and -я change: -а becomes -у and -я becomes -ю.",
             tables=[table(
                 ["Type of noun", "Nominative", "Accusative"],
                 [["masculine thing", "журна'л · слова'рь · музе'й", "журна'л · слова'рь · музе'й"],
                  ["neuter", "письмо' · зда'ние", "письмо' · зда'ние"],
                  ["feminine in -а", "кни'га · шко'ла", "кни'г{у} · шко'л{у}"],
                  ["feminine in -я", "неде'ля · статья'", "неде'л{ю} · стать{ю'}"],
                  ["feminine in -ь", "вещь · дверь", "вещь · дверь"]],
                 note="Plural things don't change either: Я чита'ю журна'лы.")],
             examples=[
                 ex("Я чита'ю журна'л.", "I'm reading a magazine.", "журна'л"),
                 ex("Он пи'шет письмо'.", "He's writing a letter.", "письмо'"),
                 ex("Мы ви'дим шко'лу.", "We see the school.", "шко'лу"),
                 ex("Ты чита'ешь газе'ту?", "Are you reading a newspaper?", "газе'ту"),
                 ex("Я ви'жу дверь.", "I see a door.", "дверь"),
             ]),
        card("A stress shift to watch",
             "In some feminine nouns the stress is on the ending in the nominative and jumps to the stem in the "
             "accusative. These are very common words, so listen for it.",
             tables=[table(
                 ["Nominative", "Accusative"],
                 [["доска'", "до'ску"], ["стена'", "сте'ну"], ["рука'", "ру'ку"],
                  ["гора'", "го'ру"], ["голова'", "го'лову"]],
                 note="board · wall · hand · mountain · head")]),
    ],
    verify=(vf("книга", "книгу") + vf("школа", "школу") + vf("газета", "газету")
            + vf("неделя", "неделю") + vf("статья", "статью") + vf("доска", "доску")
            + vf("стена", "стену") + vf("рука", "руку") + vf("гора", "гору") + vf("голова", "голову")),
    exercises=[
        fb("Я чита'ю ___.", ["кни'гу", "кни'га", "кни'ги", "кни'ге"], "кни'гу",
           "Feminine in -а: -а becomes -у.", tr="I'm reading a book.", lemma="книга"),
        fb("Он пи'шет ___.", ["письмо'", "письма'", "письму'", "письме'"], "письмо'",
           "A neuter thing doesn't change in the accusative.", tr="He's writing a letter."),
        fb("Мы ви'дим ___.", ["шко'лу", "шко'ла", "шко'ле", "шко'лы"], "шко'лу",
           "Feminine in -а: -у.", tr="We see the school.", lemma="школа"),
        fb("Я чита'ю ___.", ["газе'ту", "газе'та", "газе'ты", "газе'те"], "газе'ту",
           "Feminine in -а: -у.", tr="I'm reading a newspaper.", lemma="газета"),
        fb("Мы смо'трим ___.", ["фильм", "фильма", "фильму", "фильме"], "фильм",
           "A masculine thing doesn't change in the accusative.", tr="We're watching a film."),
        fb("Я ви'жу ___.", ["дверь", "дверю", "дверу", "дверы"], "дверь",
           "Feminine nouns in -ь don't change.", tr="I see a door."),
        fb("Я ви'жу ___.", ["сте'ну", "стену'", "стена'", "сте'не"], "сте'ну",
           "Стена' becomes сте'ну: the stress jumps to the stem.", tr="I see the wall.", lemma="стена"),
        mc("Which noun does not change in the accusative?",
           ["журна'л", "кни'га", "шко'ла", "статья'"], "журна'л",
           "Only feminine nouns in -а and -я change."),
        mc("Which ending marks a feminine noun in -я as a direct object?", ["-ю", "-у", "-е", "-и"], "-ю",
           "Неде'ля → неде'лю.", order=True),
        mc("Which sentence is correct?",
           ["Я чита'ю кни'гу.", "Я чита'ю кни'га.", "Я чита'ю кни'ги.", "Я чита'ю кни'ге."], "Я чита'ю кни'гу.",
           "A direct object is accusative: кни'га → кни'гу."),
    ],
)

# ---------------------------------------------------------------------------- 28
L28 = lesson(
    "The accusative with people and animals",
    "Я ви'жу студе'нта, Я зна'ю учи'теля",
    requires=["студент", "учитель", "отец", "мать", "девушка"],
    cards=[
        card("Masculine people and animals take an ending",
             "For a masculine noun that is a person or an animal, the accusative is not the same as the "
             "nominative. After a hard consonant add -а. If the noun ends in -ь or -й, replace that letter with "
             "-я. Nouns in -ец lose their -е-, as in the plural: оте'ц becomes отца'.",
             tables=[table(
                 ["Nominative", "Accusative", "Rule"],
                 [["студе'нт", "студе'нт{а}", "hard consonant: add -а"],
                  ["капита'н", "капита'н{а}", "hard consonant: add -а"],
                  ["учи'тель", "учи'тел{я}", "-ь becomes -я"],
                  ["Никола'й", "Никола'{я}", "-й becomes -я"],
                  ["оте'ц", "отц{а'}", "the -е- drops out"]])],
             examples=[
                 ex("Я ви'жу студе'нта.", "I see the student.", "студе'нта"),
                 ex("Он зна'ет учи'теля.", "He knows the teacher.", "учи'теля"),
                 ex("Ты зна'ешь Никола'я?", "Do you know Nikolai?", "Никола'я"),
                 ex("Мы ви'дим отца'.", "We see [my] father.", "отца'"),
             ]),
        card("Women, and men whose names end in -а or -я",
             "Women are easy: whether a feminine noun is a person or a thing makes no difference. Девушка becomes "
             "де'вушку, Та'ня becomes Та'ню, and мать stays мать. Men with nouns in -а or -я, such as па'па and "
             "дя'дя, decline like feminine nouns, so they take -у and -ю.",
             tables=[table(
                 ["Nominative", "Accusative"],
                 [["де'вушка", "де'вуш{ку}"], ["Та'ня", "Та'н{ю}"], ["мать", "мать"],
                  ["па'па", "па'п{у}"], ["дя'дя", "дя'д{ю}"]])]),
    ],
    verify=(vf("студент", "студента") + vf("капитан", "капитана") + vf("учитель", "учителя")
            + vf("отец", "отца") + vf("девушка", "девушку") + vf("папа", "папу") + vf("дядя", "дядю")),
    exercises=[
        fb("Я ви'жу ___.", ["студе'нта", "студе'нт", "студе'нту", "студе'нты"], "студе'нта",
           "A masculine person adds -а.", tr="I see the student.", lemma="студент"),
        fb("Мы зна'ем ___.", ["учи'теля", "учи'тель", "учи'телю", "учи'теле"], "учи'теля",
           "-ь becomes -я.", tr="We know the teacher.", lemma="учитель"),
        fb("Ты ви'дишь ___?", ["отца'", "оте'ц", "отцу'", "оте'ца"], "отца'",
           "In оте'ц the -е- drops out.", tr="Do you see [my] father?", lemma="отец"),
        fb("Мы зна'ем ___.", ["Никола'я", "Никола'й", "Никола'ю", "Никола'е"], "Никола'я",
           "-й becomes -я.", tr="We know Nikolai."),
        fb("Я ви'жу ___.", ["па'пу", "па'па", "па'пе", "па'пы"], "па'пу",
           "Па'па ends in -а, so it takes -у like a feminine noun.", tr="I see dad.", lemma="папа"),
        fb("Он зна'ет ___.", ["Та'ню", "Та'ня", "Та'не", "Та'ни"], "Та'ню",
           "-я becomes -ю.", tr="He knows Tanya."),
        fb("Мы ви'дим ___.", ["дя'дю", "дя'дя", "дя'де", "дя'ди"], "дя'дю",
           "Дя'дя ends in -я, so -ю.", tr="We see [our] uncle.", lemma="дядя"),
        fb("Ты зна'ешь э'ту ___?", ["де'вушку", "де'вушка", "де'вушки", "де'вушке"], "де'вушку",
           "A woman takes -у like any feminine noun in -а.", tr="Do you know this girl?", lemma="девушка"),
        mc("Which noun changes in the accusative?", ["студе'нт", "журна'л", "письмо'", "окно'"], "студе'нт",
           "A masculine person takes an ending; masculine things don't."),
        mc("Which sentence is correct?",
           ["Я ви'жу учи'теля.", "Я ви'жу учи'тель.", "Я ви'жу учи'телю.", "Я ви'жу учи'телем."],
           "Я ви'жу учи'теля.", "-ь becomes -я."),
    ],
)

# ---------------------------------------------------------------------------- 29
L29 = lesson(
    "Pronouns in the accusative: me, you, him, her",
    "Меня', тебя', его', её, нас, вас, их",
    requires=["тебя", "его", "её", "нас", "вас"],
    cards=[
        card("Seven new forms",
             "Personal pronouns have their own accusative forms. Learn them as a set: they are used all the time "
             "(Я зна'ю тебя', Он ви'дит нас).",
             tables=[table(
                 ["Nominative", "Accusative", "Example"],
                 [["я", "меня'", "Она' зна'ет меня'."],
                  ["ты", "тебя'", "Я ви'жу тебя'."],
                  ["он · оно'", "его'", "Учи'тель ви'дит его'."],
                  ["она'", "её", "Я зна'ю её."],
                  ["мы", "нас", "Вы слы'шите нас?"],
                  ["вы", "вас", "Я понима'ю вас."],
                  ["они'", "их", "Мы ви'дим их."]])]),
        card("The extra н after a preposition",
             "When его', её or их comes right after a preposition, a н is added at the front: него', неё, них. "
             "Without a preposition there is no н. The same words are also the possessives “his, her, their” "
             "(его' дом, её кни'га, их маши'на), and those never take н.",
             tables=[table(
                 ["Without a preposition", "After a preposition"],
                 [["Я ви'жу его'.", "Я смотрю' на {н}его'."],
                  ["Я ви'жу её.", "Я смотрю' на {н}её."],
                  ["Я ви'жу их.", "Я смотрю' на {н}их."]])],
             examples=[
                 ex("Я живу' в его' до'ме.", "I live in his house. (possessive: no н)", "его'"),
                 ex("Он смо'трит на меня'.", "He is looking at me. (меня' never changes)", "на меня'"),
             ]),
    ],
    verify=[("я", "меня"), ("ты", "тебя"), ("он", "его"), ("она", "её"), ("мы", "нас"), ("вы", "вас"),
            ("они", "их")],
    exercises=[
        fb("Он ви'дит ___.", ["меня'", "я", "мне", "мной"], "меня'",
           "Direct object: accusative of я is меня'.", tr="He sees me."),
        fb("Я ви'жу ___.", ["тебя'", "ты", "тебе'", "тобо'й"], "тебя'",
           "Accusative of ты is тебя'.", tr="I see you."),
        fb("Мы зна'ем ___.", ["её", "она'", "ей", "неё"], "её",
           "No preposition, so no н.", tr="We know her."),
        fb("Я смотрю' на ___.", ["неё", "её", "она'", "ей"], "неё",
           "After the preposition на, её becomes неё.", tr="I'm looking at her."),
        fb("Вы слы'шите ___?", ["нас", "мы", "нам", "на'ми"], "нас",
           "Accusative of мы is нас.", tr="Do you hear us?"),
        fb("Мы ви'дим ___.", ["их", "они'", "им", "и'ми"], "их",
           "Accusative of они' is их.", tr="We see them."),
        fb("Я смотрю' на ___.", ["него'", "его'", "он", "ему'"], "него'",
           "After a preposition его' becomes него'.", tr="I'm looking at him."),
        fb("Я живу' в ___ до'ме.", ["его'", "него'", "он", "ему'"], "его'",
           "Here его' means “his”, a possessive, so no н.", tr="I live in his house."),
        mc("Which word means “you” (one friend) as a direct object?", ["тебя'", "ты", "тебе'", "вас"], "тебя'",
           "Ты → тебя'."),
        mc("Why do we say на неё but Я зна'ю её?",
           ["A preposition adds н- before его', её and их", "На is feminine", "Неё is plural", "It's just an exception"],
           "A preposition adds н- before его', её and их",
           "Without a preposition, no н.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 30
L30 = lesson(
    "Adjectives in the accusative",
    "Но'вую кни'гу, но'вого студе'нта",
    requires=["новый", "русский", "хороший", "большой", "красивый"],
    cards=[
        card("Adjectives follow the noun",
             "The adjective takes the same case as its noun. So when the noun is a direct object, the adjective "
             "must be accusative too. Where the noun does not change (masculine things, neuter, plural things), "
             "the adjective does not change either. A feminine noun takes -ую (hard stem) or -юю (soft stem).",
             tables=[table(
                 ["", "Nominative", "Accusative"],
                 [["masculine thing", "но'вый дом", "Я ви'жу но'вый дом."],
                  ["neuter", "но'вое окно'", "Я ви'жу но'вое окно'."],
                  ["plural things", "но'вые кни'ги", "Я чита'ю но'вые кни'ги."],
                  ["feminine, hard", "но'вая кни'га", "Я чита'ю но'в{ую} кни'гу."],
                  ["feminine, soft", "си'няя руба'шка", "Я ви'жу си'н{юю} руба'шку."]])]),
        card("Masculine people: -ого and -его",
             "With a masculine person or animal both the noun and the adjective change. A hard adjective ends in "
             "-ого, a soft one in -его. Spelling rules still apply: after к, г, х you keep the hard ending "
             "(ру'сского), and after ж, ч, ш, щ an unstressed о turns into е (хоро'шего). A stressed о stays "
             "(большо'го).",
             tables=[table(
                 ["Nominative", "Accusative", "Why"],
                 [["но'вый", "но'в{ого}", "hard stem"],
                  ["большо'й", "больш{о'го}", "stressed о stays"],
                  ["си'ний", "си'н{его}", "soft stem"],
                  ["ру'сский", "ру'сск{ого}", "after к the ending is hard"],
                  ["хоро'ший", "хоро'ш{его}", "five-letter rule: о becomes е after ш"]])],
             examples=[
                 ex("Я зна'ю но'вого студе'нта.", "I know the new student.", "но'вого"),
                 ex("Мы зна'ем хоро'шего учи'теля.", "We know a good teacher.", "хоро'шего"),
                 ex("Он ви'дит большо'го кота'.", "He sees a big cat.", "большо'го"),
                 ex("Ты зна'ешь ру'сского студе'нта?", "Do you know the Russian student?", "ру'сского"),
             ]),
    ],
    verify=(vf("новый", "новую", "нового") + vf("синий", "синюю", "синего") + vf("русский", "русского")
            + vf("хороший", "хорошего") + vf("большой", "большого")),
    exercises=[
        fb("Я чита'ю ___ кни'гу.", ["но'вую", "но'вая", "но'вый", "но'вого"], "но'вую",
           "Feminine object: -ая becomes -ую.", tr="I'm reading a new book.", lemma="новый"),
        fb("Мы ви'дим ___ дом.", ["но'вый", "но'вую", "но'вого", "но'вое"], "но'вый",
           "A masculine thing keeps its nominative form.", tr="We see a new house.", lemma="новый"),
        fb("Я ви'жу ___ окно'.", ["большо'е", "большо'й", "большо'го", "большу'ю"], "большо'е",
           "A neuter keeps its nominative form.", tr="I see a big window."),
        fb("Я зна'ю ___ студе'нта.", ["но'вого", "но'вый", "но'вую", "но'вое"], "но'вого",
           "A masculine person: -ый becomes -ого.", tr="I know the new student.", lemma="новый"),
        fb("Мы зна'ем ___ учи'теля.", ["хоро'шего", "хоро'шого", "хоро'ший", "хоро'шую"], "хоро'шего",
           "After ш an unstressed о is written е.", tr="We know a good teacher.", lemma="хороший"),
        fb("Он зна'ет ___ студе'нта.", ["ру'сского", "ру'сский", "ру'сскую", "ру'ссого"], "ру'сского",
           "After к the ending stays hard: -ого.", tr="He knows the Russian student.", lemma="русский"),
        fb("Я ви'жу ___ кота'.", ["большо'го", "большо'й", "большу'ю", "большо'е"], "большо'го",
           "The о is stressed, so it stays: -ого.", tr="I see a big cat.", lemma="большой"),
        fb("Мы чита'ем ___ журна'лы.", ["интере'сные", "интере'сных", "интере'сный", "интере'сную"], "интере'сные",
           "Plural things keep their nominative form.", tr="We read interesting magazines."),
        mc("Which adjective endings go with a feminine direct object?", ["-ую / -юю", "-ого / -его", "-ый / -ий", "-ая / -яя"],
           "-ую / -юю", "Feminine object: -ая → -ую, -яя → -юю.", order=True),
        mc("Which rule explains хоро'шего (not хоро'шого)?",
           ["After ш an unstressed о is written е", "After ш you write ы", "After г you write я", "It is a soft adjective"],
           "After ш an unstressed о is written е", "The five-letter rule."),
    ],
)

# ---------------------------------------------------------------------------- 31
L31 = lesson(
    "My, this, which: other words that agree",
    "Мою' сестру', э'того бра'та, каку'ю кни'гу?",
    requires=["мой", "наш", "этот", "какой", "первый"],
    cards=[
        card("They decline like adjectives",
             "Many words that go with a noun behave like adjectives: мой, твой, наш, ваш (my, your, our, your), "
             "э'тот and тот (this, that), како'й (which), чей (whose), and the ordinal numbers пе'рвый, "
             "второ'й, тре'тий. In the accusative they follow the same three rules: no change for things, "
             "-ого or -его for masculine people, and a feminine ending for feminine nouns.",
             tables=[table(
                 ["Word", "Masc. thing", "Masc. person", "Feminine"],
                 [["мой", "мой", "мо{его'}", "мо{ю'}"],
                  ["твой", "твой", "тво{его'}", "тво{ю'}"],
                  ["наш", "наш", "на'ш{его}", "на'ш{у}"],
                  ["ваш", "ваш", "ва'ш{его}", "ва'ш{у}"],
                  ["э'тот", "э'тот", "э'т{ого}", "э'т{у}"],
                  ["тот", "тот", "т{ого'}", "т{у}"],
                  ["како'й", "како'й", "как{о'го}", "как{у'ю}"],
                  ["чей", "чей", "чь{его'}", "чь{ю}"],
                  ["пе'рвый", "пе'рвый", "пе'рв{ого}", "пе'рв{ую}"],
                  ["тре'тий", "тре'тий", "тре'ть{его}", "тре'ть{ю}"]],
                 note="Neuter and plural things: no change. Его', её, их never change at all.")]),
        card("In sentences",
             "Your choice depends on the noun that follows: its gender, and whether it is a person. Мой and твой take "
             "the soft endings (моего', мою'). Чей and тре'тий also keep a soft sign in every form except the "
             "masculine thing: чью, чьего', тре'тью, тре'тьего. Наш and ваш follow the spelling rule you met in "
             "lesson 25: на'шего, ва'шего.",
             examples=[
                 ex("Вы зна'ете моего' бра'та?", "Do you know my brother?", "моего'"),
                 ex("Я ви'жу мою' сестру'.", "I see my sister.", "мою'"),
                 ex("Мы зна'ем э'того студе'нта.", "We know this student.", "э'того"),
                 ex("Каку'ю кни'гу ты чита'ешь?", "Which book are you reading?", "Каку'ю"),
                 ex("Я чита'ю пе'рвую страни'цу.", "I'm reading the first page.", "пе'рвую"),
                 ex("Чью маши'ну вы ви'дите?", "Whose car do you see?", "Чью"),
             ]),
    ],
    verify=(vf("мой", "моего", "мою") + vf("твой", "твоего", "твою") + vf("наш", "нашего", "нашу")
            + vf("ваш", "вашего", "вашу") + vf("этот", "этого", "эту") + vf("тот", "того", "ту")
            + vf("какой", "какого", "какую") + vf("чей", "чьего", "чью")
            + vf("первый", "первого", "первую") + vf("третий", "третьего", "третью")),
    exercises=[
        fb("Я ви'жу ___ сестру'.", ["мою'", "моя'", "мой", "моего'"], "мою'",
           "Feminine object: моя' becomes мою'.", tr="I see my sister."),
        fb("Вы зна'ете ___ бра'та?", ["моего'", "мой", "мою'", "моё"], "моего'",
           "Masculine person: мой becomes моего'.", tr="Do you know my brother?"),
        fb("Мы зна'ем ___ студе'нта.", ["э'того", "э'тот", "э'ту", "э'то"], "э'того",
           "Masculine person: э'тот becomes э'того.", tr="We know this student."),
        fb("Я ви'жу ___ де'вушку.", ["э'ту", "э'та", "э'того", "э'то"], "э'ту",
           "Feminine: э'та becomes э'ту.", tr="I see this girl."),
        fb("___ кни'гу ты чита'ешь?", ["Каку'ю", "Кака'я", "Како'й", "Како'го"], "Каку'ю",
           "Feminine object: кака'я becomes каку'ю.", tr="Which book are you reading?"),
        fb("Мы ви'дим ___ ма'му.", ["на'шу", "на'ша", "на'шего", "наш"], "на'шу",
           "Feminine object: на'ша becomes на'шу.", tr="We see our mom."),
        mc("Which form is used with мой and a masculine thing, like дом?",
           ["мой", "моего'", "мою'", "моя'"], "мой", "Masculine things don't change."),
        mc("What is the accusative of тре'тья for a feminine object?",
           ["тре'тью", "тре'тья", "тре'тьего", "тре'тьюю"], "тре'тью", "Third is a soft-stem word, so -ю."),
        mc("Which words never change for case?", ["его', её, их", "мой, твой", "э'тот, тот", "кто, что"],
           "его', её, их", "These possessives are frozen.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 32
L32 = lesson(
    "On Monday, on Tuesday: the days of the week",
    "В понеде'льник, во вто'рник, в сре'ду",
    requires=["понедельник", "вторник", "среда", "четверг", "суббота"],
    cards=[
        card("The week",
             "The days are not capitalised in Russian. To say “on Monday” use в plus the accusative, and the "
             "question is Когда'? (when?). In во вто'рник the preposition becomes во because the next word starts "
             "with two consonants. Masculine and neuter days do not change; the feminine days (среда', пя'тница, "
             "суббо'та) take -у, and сре'ду moves its stress.",
             tables=[table(
                 ["Day", "On this day"],
                 [["понеде'льник", "в понеде'льник"],
                  ["вто'рник", "{во} вто'рник"],
                  ["среда'", "в сре'д{у}"],
                  ["четве'рг", "в четве'рг"],
                  ["пя'тница", "в пя'тниц{у}"],
                  ["суббо'та", "в суббо'т{у}"],
                  ["воскресе'нье", "в воскресе'нье"]])]),
        card("In use",
             "Use the nominative to say what day it is today or tomorrow, and в + accusative for when something "
             "happens. This is the same accusative you have been learning: it just follows в.",
             examples=[
                 ex("Сего'дня понеде'льник.", "Today is Monday.", "понеде'льник"),
                 ex("За'втра вто'рник.", "Tomorrow is Tuesday.", "вто'рник"),
                 ex("В сре'ду я до'ма.", "On Wednesday I'm at home.", "В сре'ду"),
                 ex("Во вто'рник мы рабо'таем.", "On Tuesday we work.", "Во вто'рник"),
                 ex("В суббо'ту мы не рабо'таем.", "On Saturday we don't work.", "В суббо'ту"),
             ]),
    ],
    verify=vf("среда", "среду") + vf("пятница", "пятницу") + vf("суббота", "субботу"),
    exercises=[
        fb("___ понеде'льник я рабо'таю.", ["В", "Во", "На", "У"], "В",
           "Days take в plus the accusative.", tr="On Monday I work."),
        fb("___ вто'рник мы до'ма.", ["Во", "В", "На", "У"], "Во",
           "Before вто'рник the preposition is во.", tr="On Tuesday we're at home."),
        fb("В ___ я до'ма.", ["сре'ду", "среда'", "среды'", "среде'"], "сре'ду",
           "Feminine day: -а becomes -у, and the stress jumps to the stem.", tr="On Wednesday I'm at home.", lemma="среда"),
        fb("В ___ мы смо'трим фильм.", ["пя'тницу", "пя'тница", "пя'тницы", "пя'тнице"], "пя'тницу",
           "Feminine day: -а becomes -у.", tr="On Friday we watch a film.", lemma="пятница"),
        fb("В ___ я не рабо'таю.", ["суббо'ту", "суббо'та", "суббо'ты", "суббо'те"], "суббо'ту",
           "Feminine day: -у.", tr="On Saturday I don't work.", lemma="суббота"),
        fb("Сего'дня ___.", ["четве'рг", "четве'рга", "четве'ргу", "четве'рге"], "четве'рг",
           "To say what day it is, use the nominative.", tr="Today is Thursday."),
        mc("Which question do these phrases answer?", ["Когда'?", "Где?", "Куда'?", "Кто?"], "Когда'?",
           "When? → в + accusative.", order=True),
        mc("Which day takes во, not в?", ["вто'рник", "понеде'льник", "пя'тница", "суббо'та"], "вто'рник",
           "Во before two consonants: во вто'рник."),
        mc("Which sentence is correct?",
           ["В пя'тницу я до'ма.", "В пя'тница я до'ма.", "На пя'тницу я до'ма.", "В пя'тницы я до'ма."],
           "В пя'тницу я до'ма.", "В + the accusative: пя'тница → пя'тницу."),
    ],
)

# ---------------------------------------------------------------------------- 33
L33 = lesson(
    "Eleven to twenty",
    "Оди'ннадцать, двена'дцать … два'дцать",
    requires=["неделя", "год", "час", "день", "месяц"],
    cards=[
        card("The teens",
             "The numbers 11 to 19 are built from the unit plus -на-дцать, which literally means “on ten”. "
             "They all end in a soft sign, and the unit's own soft sign disappears (пять → пятна'дцать). Twenty is "
             "its own word. Ordinals are made by swapping -ь for -ый: двена'дцать → двена'дцатый. "
             "They behave like any adjective, so they agree with their noun.",
             tables=[table(
                 ["", "Cardinal", "Ordinal"],
                 [["11", "оди'н{надцать}", "оди'ннадцатый"],
                  ["12", "две{на'дцать}", "двена'дцатый"],
                  ["13", "три{на'дцать}", "трина'дцатый"],
                  ["14", "четы'р{надцать}", "четы'рнадцатый"],
                  ["15", "пят{на'дцать}", "пятна'дцатый"],
                  ["16", "шест{на'дцать}", "шестна'дцатый"],
                  ["17", "сем{на'дцать}", "семна'дцатый"],
                  ["18", "восем{на'дцать}", "восемна'дцатый"],
                  ["19", "девят{на'дцать}", "девятна'дцатый"],
                  ["20", "два'дцать", "двадца'тый"]])],
             examples=[
                 ex("Сего'дня двена'дцатый день.", "Today is the twelfth day.", "двена'дцатый"),
                 ex("Э'то пятна'дцатая ко'мната.", "This is the fifteenth room.", "пятна'дцатая"),
                 ex("Сего'дня девятна'дцатый день.", "Today is the nineteenth day.", "девятна'дцатый"),
             ]),
    ],
    verify=[("одиннадцать", "одиннадцать"), ("двенадцать", "двенадцать"), ("тринадцать", "тринадцать"),
            ("четырнадцать", "четырнадцать"), ("пятнадцать", "пятнадцать"), ("шестнадцать", "шестнадцать"),
            ("семнадцать", "семнадцать"), ("восемнадцать", "восемнадцать"), ("девятнадцать", "девятнадцать"),
            ("двадцать", "двадцать"), ("двенадцатый", "двенадцатый"), ("двадцатый", "двадцатый")],
    exercises=[
        fb("Пять и де'сять — э'то ___.", ["пятна'дцать", "шестна'дцать", "двена'дцать", "два'дцать"], "пятна'дцать",
           "Пять + на + дцать.", tr="Five and ten is fifteen."),
        fb("Де'вять и де'сять — э'то ___.", ["девятна'дцать", "восемна'дцать", "семна'дцать", "два'дцать"], "девятна'дцать",
           "Девять + на + дцать.", tr="Nine and ten is nineteen."),
        fb("Два и де'сять — э'то ___.", ["двена'дцать", "трина'дцать", "оди'ннадцать", "два'дцать"], "двена'дцать",
           "Две + на'дцать.", tr="Two and ten is twelve."),
        fb("Э'то ___ уро'к. (13th)", ["трина'дцатый", "трина'дцать", "трина'дцатая", "трина'дцатое"], "трина'дцатый",
           "Урок is masculine, so the ordinal takes -ый.", tr="This is the thirteenth lesson."),
        fb("Э'то ___ ко'мната. (20th)", ["двадца'тая", "двадца'тый", "два'дцать", "двадца'тое"], "двадца'тая",
           "Ко'мната is feminine.", tr="This is the twentieth room."),
        mc("Which number is 14?", ["четы'рнадцать", "шестна'дцать", "пятна'дцать", "двена'дцать"], "четы'рнадцать",
           "Четы'ре + на'дцать → четы'рнадцать."),
        mc("What do the numbers 11 to 19 have in common?",
           ["They all end in -надцать", "They all end in -дцать only", "They all begin with два", "They all end in -ый"],
           "They all end in -надцать", "Unit + -надцать.", order=True),
        mc("How do the ordinals from 11 to 20 behave?",
           ["Like adjectives: they agree with the noun", "Like nouns", "They never change", "Like verbs"],
           "Like adjectives: they agree with the noun", "Двена'дцатый, двена'дцатая, двена'дцатое."),
        mc("Which phrase means “the sixteenth room”?",
           ["шестна'дцатая ко'мната", "шестна'дцать ко'мната", "шестна'дцатый ко'мната", "шестна'дцатое ко'мната"],
           "шестна'дцатая ко'мната", "Ко'мната is feminine, so the ordinal ends in -ая."),
    ],
)

UNIT = unit("Unit 5: The accusative, days and numbers", [L27, L28, L29, L30, L31, L32, L33])
