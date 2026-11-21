"""Unit 1: naming things, asking questions, gender  (textbook lessons 1-2)."""
from dsl import *

# ---------------------------------------------------------------------------- 1
L1 = lesson(
    "Э'то, and the verb that isn't there",
    "Saying what things and people are",
    requires=["это", "я", "ты", "он", "она", "дом", "мама"],
    cards=[
        card("Э'то",
             "Э'то means “this is”, “that is” or “these are”. It never changes: the same word works for a "
             "house, a book or a whole group of people. Put a noun after it and the sentence is finished. "
             "In speech, pause briefly after э'то.",
             examples=[
                 ex("Э'то дом.", "This is a house.", "Э'то"),
                 ex("Э'то ма'ма.", "This is mom.", "Э'то"),
                 ex("Э'то окно'.", "This is a window.", "Э'то"),
                 ex("Э'то кни'ги.", "These are books.", "Э'то"),
             ]),
        card("The verb that isn't there",
             "English needs “am”, “is” or “are” to join a subject to a description. Russian leaves the present "
             "tense of быть (to be) out entirely. You don't say “I am a doctor”; you say, word for word, "
             "“I doctor”. That is not shorthand: it is the correct sentence. Only the past and future use "
             "быть, and the past comes later in this course.\n\n"
             "In writing, two nouns in a row often get a dash (Москва' — столи'ца, “Moscow is the capital”), "
             "but after я, ты, он, она' and the other pronouns there is none.",
             examples=[
                 ex("Я врач.", "I am a doctor.", "Я врач"),
                 ex("Он студе'нт.", "He is a student.", "Он студе'нт"),
                 ex("Она' ма'ма.", "She is a mom.", "Она' ма'ма"),
                 ex("Мы здесь.", "We are here.", "Мы здесь"),
                 ex("Они' там.", "They are there.", "Они' там"),
             ]),
    ],
    exercises=[
        mc("How do you say “This is a house”?",
           ["Э'то дом.", "Э'то есть дом.", "Э'то быть дом.", "Я дом."],
           "Э'то дом.", "Э'то + noun is the whole sentence. There is no linking verb to add."),
        mc("Which sentence means “I am a student”?",
           ["Я студе'нт.", "Я есть студе'нт.", "Я быть студе'нт.", "Студе'нт я быть."],
           "Я студе'нт.", "The present tense of быть is simply absent: я студе'нт is complete."),
        fb("___ кни'га.",
           ["Э'то", "Э'та", "Э'тот", "Быть"], "Э'то",
           "To say “this is…” you use э'то, whatever the noun. Э'та кни'га would only be the phrase “this book”.",
           tr="This is a book."),
        mc("How do you say “We are here”?",
           ["Мы здесь.", "Мы есть здесь.", "Мы быть здесь.", "Мы э'то здесь."],
           "Мы здесь.", "No word for “are”: subject and place are enough."),
        mc("Which word fits every one of these: “This is a window”, “This is a table”, “These are books”?",
           ["э'то", "э'тот", "э'та", "э'ти"], "э'то",
           "Э'то never changes for gender or number. The others are forms that must agree with a noun."),
        mc("In everyday speech, what goes in the blank?  Он ___ студе'нт.",
           ["(nothing)", "есть", "быть", "явля'ется"], "(nothing)",
           "Он студе'нт is already complete. (Явля'ется does mean “is”, but it belongs to formal or scientific "
           "writing, like “Вода' явля'ется жи'дкостью”, not to saying what someone is.)"),
        mc("Which of these is NOT correct Russian?",
           ["Он есть врач.", "Он врач.", "Мы здесь.", "Э'то дом."], "Он есть врач.",
           "Есть is not used to link a subject and a noun in ordinary present-tense sentences."),
    ],
)

# ---------------------------------------------------------------------------- 2
L2 = lesson(
    "Asking and answering",
    "Кто? Что? Где? and yes/no questions",
    requires=["кто", "что", "где", "да", "нет", "дом"],
    cards=[
        card("Кто? Что? Где?",
             "Кто (who) asks about people. Что (what) asks about things. Где (where) asks about place. These are "
             "information questions: they start with a question word, and the voice falls at the end, just "
             "as in a statement. Tap a row to hear it.",
             tables=[table(
                 ["Word", "Asks about", "Example", "Meaning"],
                 [["Кто?", "people", "Кто э'то? — Э'то ма'ма.", "Who is this? — This is mom."],
                  ["Что?", "things", "Что э'то? — Э'то кни'га.", "What is this? — This is a book."],
                  ["Где?", "place", "Где дом? — Дом там.", "Where is the house? — The house is there."]])]),
        card("Yes/no questions",
             "A yes/no question has no question word. It uses the same words as the statement, and only the "
             "voice changes: it rises sharply on the word being asked about. In writing, the question mark is "
             "the only sign. Tap the speaker on each pair and listen for the rise.",
             examples=[
                 ex("Э'то дом.", "This is a house. (statement)"),
                 ex("Э'то дом?", "Is this a house? (question)"),
                 ex("Он студе'нт?", "Is he a student?"),
                 ex("Ма'ма здесь?", "Is mom here?"),
             ]),
        card("Short answers",
             "In real conversation people give only the new information. Да and нет can stand alone, or you add "
             "the one word that matters. Don't answer an information question with да or нет: it isn't a "
             "yes/no question.",
             tables=[table(
                 ["Question", "Complete answer", "Short answer"],
                 [["Кто э'то?", "Э'то А'нна.", "А'нна."],
                  ["Ма'ма здесь?", "Да, ма'ма здесь.", "Да, здесь."],
                  ["Он студе'нт?", "Нет, он не студе'нт.", "Нет."]])]),
    ],
    exercises=[
        fb("___ э'то? — Э'то ма'ма.", ["Кто", "Что", "Где", "Как"], "Кто",
           "The answer is a person, so the question is кто."),
        fb("___ э'то? — Э'то кни'га.", ["Кто", "Что", "Где", "Когда'"], "Что",
           "The answer is a thing, so the question is что."),
        fb("___ дом? — Дом там.", ["Кто", "Что", "Где", "Почему'"], "Где",
           "The answer gives a place, so the question is где."),
        mc("Which question can be answered with да or нет?",
           ["Э'то дом?", "Кто э'то?", "Что э'то?", "Где дом?"], "Э'то дом?",
           "Only the question without a question word is a yes/no question."),
        mc("How does a yes/no question differ from the matching statement in speech?",
           ["The voice rises on the word asked about", "A helper word is added", "The word order is reversed",
            "The verb быть appears"],
           "The voice rises on the word asked about",
           "Russian adds nothing. Intonation does the work, which is why listening matters."),
        mc("— Ма'ма здесь?  Pick the natural short answer.",
           ["Да, здесь.", "Да, я здесь.", "Кто, здесь.", "Да, э'то."], "Да, здесь.",
           "Short answers repeat only the new information. “Да, я здесь” would mean “I am here”."),
        mc("— Кто э'то?  Pick the natural short answer.",
           ["А'нна.", "Да, А'нна.", "Нет, А'нна.", "Где А'нна."], "А'нна.",
           "An information question is answered with the information, not with да or нет."),
        fb("— Что э'то? — ___ ру'чка.", ["Э'то", "Кто", "Где", "Нет"], "Э'то",
           "Э'то + noun states what something is."),
    ],
)

# ---------------------------------------------------------------------------- 3
L3 = lesson(
    "И or А? And word order",
    "Joining, contrasting, and putting new information last",
    requires=["и", "а", "но", "здесь", "там", "тоже"],
    cards=[
        card("И and А",
             "Both can be translated as “and”, but Russian chooses by meaning. И joins things that go together "
             "or adds one to another. А sets two things against each other, or picks the conversation back up "
             "(“and you?”). In the pattern “not X, but Y” you need а.",
             tables=[table(
                 ["Word", "Idea", "Example", "Meaning"],
                 [["и", "adding, joining", "Э'то ма'ма и па'па.", "This is mom and dad."],
                  ["а", "contrast", "Он до'ма, а она' там.", "He is at home, and she is there."],
                  ["а", "not X, but Y", "Э'то не стол, а стул.", "This is not a table but a chair."],
                  ["а", "and you?", "Я здесь. А ты?", "I'm here. And you?"]])],
             examples=[]),
        card("Commas, and where the news goes",
             "Always put a comma before а. Put one before и only when it joins two full clauses (Он здесь, и она' "
             "здесь), not when it joins two words (ма'ма и па'па).\n\n"
             "Russian word order is flexible, and the position carries meaning: new or emphasised "
             "information usually comes last. So the same two words can answer different questions.",
             tables=[table(
                 ["Question", "Answer", "What is new"],
                 [["Что здесь?", "Здесь стол.", "стол (a table)"],
                  ["Где стол?", "Стол здесь.", "здесь (here)"]],
                 note="The words are the same; the order shows what the speaker is telling you.")]),
    ],
    exercises=[
        fb("Э'то ма'ма ___ па'па.", ["и", "а", "но", "не"], "и",
           "Mom and dad belong together: и joins them."),
        fb("Э'то не стол, ___ стул.", ["а", "и", "но", "нет"], "а",
           "In “not X but Y”, Russian uses а."),
        fb("Я здесь. ___ ты?", ["А", "И", "Но", "Да"], "А",
           "А picks the conversation back up: “And you?”", tr="I'm here. And you?"),
        fb("А'нна ___ Бори'с здесь.", ["и", "а", "но", "нет"], "и",
           "Anna and Boris are being added together, so и."),
        mc("Which sentence is punctuated correctly?",
           ["Э'то стол, а э'то стул.", "Э'то стол а э'то стул.", "Э'то стол, и э'то, стул.",
            "Э'то, стол, а э'то стул."],
           "Э'то стол, а э'то стул.", "A comma always comes before а."),
        mc("Which is punctuated correctly?",
           ["А'нна и Бори'с здесь.", "А'нна, и Бори'с здесь.", "А'нна и, Бори'с здесь.",
            "А'нна, и, Бори'с здесь."],
           "А'нна и Бори'с здесь.", "No comma when и joins two words."),
        mc("— Что здесь?   Which answer puts the new information last?",
           ["Здесь кни'га.", "Кни'га здесь."], "Здесь кни'га.",
           "The question asks what is here, so the thing, кни'га, is the news and comes last."),
        mc("— Где кни'га?   Which answer puts the new information last?",
           ["Кни'га здесь.", "Здесь кни'га."], "Кни'га здесь.",
           "The question asks where, so the place, здесь, is the news and comes last."),
    ],
)

# ---------------------------------------------------------------------------- 4
L4 = lesson(
    "Gender of nouns",
    "Masculine, feminine, neuter: read it from the ending",
    requires=["книга", "окно", "стол", "день", "ночь", "дом", "имя", "папа"],
    cards=[
        card("Three genders",
             "Every Russian noun is masculine, feminine or neuter, even a table or a window. You can usually tell "
             "from the last letter of the dictionary form. Gender matters because other words (my, new, was) "
             "change to match the noun, as the next lessons show.",
             tables=[table(
                 ["Gender", "Dictionary form ends in", "Examples"],
                 [["Masculine", "a consonant, or -й", "дом (house), стол (table), музе'й (museum)"],
                  ["Feminine", "-а, -я, -ия", "кни'га (book), неде'ля (week), ста'нция (station)"],
                  ["Neuter", "-о, -е, -ие, -мя", "окно' (window), мо'ре (sea), зда'ние (building), и'мя (name)"]],
                 note="Tap a row to hear the words.")]),
        card("Exceptions to learn",
             "Not every noun follows the ending rule. Nouns in a soft sign (-ь) can be masculine or feminine, so "
             "learn each one with its gender; two suffixes help: -тель is almost always masculine and "
             "-ость always feminine. And a few nouns that name men end in -а or -я but are masculine.",
             tables=[table(
                 ["Case", "Gender", "Examples"],
                 [["ends in -ь", "learn each one", "день (m.), ночь (f.), жизнь (f.)"],
                  ["-тель", "masculine", "учи'тель (teacher), писа'тель (writer)"],
                  ["-ость", "feminine", "ра'дость (joy), но'вость (news)"],
                  ["man's name or title in -а / -я", "masculine", "па'па, дя'дя, де'душка, мужчи'на"]])]),
    ],
    exercises=[
        mc("What gender is кни'га?", ["feminine", "masculine", "neuter"], "feminine",
           "It ends in -а, the typical feminine ending.", order=True),
        mc("What gender is окно'?", ["neuter", "masculine", "feminine"], "neuter",
           "Nouns in -о are neuter."),
        mc("What gender is стол?", ["masculine", "feminine", "neuter"], "masculine",
           "A consonant ending means masculine."),
        mc("What gender is и'мя?", ["neuter", "feminine", "masculine"], "neuter",
           "It looks feminine because of -я, but -мя nouns are neuter: и'мя, вре'мя."),
        mc("What gender is па'па?", ["masculine", "feminine", "neuter"], "masculine",
           "It ends in -а but names a man, so it is masculine: мой па'па."),
        mc("What gender is ста'нция?", ["feminine", "masculine", "neuter"], "feminine",
           "-ия is a feminine ending. (Compare -ие, as in зда'ние, which is neuter.)"),
        mc("Which of these nouns is feminine?", ["ночь", "день", "учи'тель", "дя'дя"], "ночь",
           "Ночь is feminine. Soft-sign nouns need to be learned one by one; день and учи'тель are masculine."),
        mc("Which of these nouns is masculine?", ["день", "ночь", "жизнь", "ра'дость"], "день",
           "Of the soft-sign nouns here, only день is masculine."),
    ],
)

# ---------------------------------------------------------------------------- 5
L5 = lesson(
    "He, she, it: pronouns follow gender",
    "Why a table is он and a book is она'",
    requires=["я", "ты", "он", "она", "мы", "вы", "они", "оно"],
    cards=[
        card("The eight personal pronouns",
             "Russian has eight personal pronouns. Ты is for one person you are on familiar terms with: a friend, "
             "a relative, a child. Вы is for several people, and also for one person you address politely, such "
             "as a stranger, a teacher or someone older. Choosing between them is a real social decision.",
             tables=[table(
                 ["Person", "Singular", "Plural"],
                 [["1st", "я (I)", "мы (we)"],
                  ["2nd", "ты (you, familiar)", "вы (you, several or polite)"],
                  ["3rd", "он (he, it) · она' (she, it) · оно' (it)", "они' (they)"]])]),
        card("Он, она', оно' replace nouns",
             "A pronoun matches the gender of the noun it replaces, for things as well as people. A table is он, "
             "a book is она', a window is оно'. English calls all three “it”. Plural nouns, of any gender, "
             "are replaced by они'. In answers the pronoun is often dropped altogether.",
             tables=[table(
                 ["Noun", "Gender", "Pronoun", "English"],
                 [["стол", "masculine", "он", "it"],
                  ["кни'га", "feminine", "она'", "it"],
                  ["окно'", "neuter", "оно'", "it"],
                  ["кни'ги", "plural", "они'", "they"],
                  ["брат", "masculine", "он", "he"]])],
             examples=[
                 ex("Где стол? — Он здесь.", "Where is the table? — It is here.", "Он"),
                 ex("Где кни'га? — Она' там.", "Where is the book? — It is there.", "Она'"),
                 ex("Где окно'? — Оно' здесь.", "Where is the window? — It is here.", "Оно'"),
                 ex("Твой дом здесь? — Да, здесь.", "Is your house here? — Yes, it is.", "Да, здесь"),
             ]),
    ],
    exercises=[
        fb("Где кни'га? — ___ здесь.", ["Она'", "Он", "Оно'", "Они'"], "Она'",
           "Кни'га is feminine, so она'."),
        fb("Где стол? — ___ там.", ["Он", "Она'", "Оно'", "Они'"], "Он",
           "Стол is masculine, so он."),
        fb("Где окно'? — ___ здесь.", ["Оно'", "Он", "Она'", "Они'"], "Оно'",
           "Окно' is neuter, so оно'."),
        fb("Где де'ти? — ___ до'ма.", ["Они'", "Он", "Она'", "Оно'"], "Они'",
           "Any plural noun is replaced by они'.", tr="Where are the children? — They are at home."),
        mc("Which pronoun replaces брат?", ["он", "она'", "оно'", "они'"], "он",
           "Брат is masculine.", order=True),
        mc("Which pronoun replaces письмо' (letter)?", ["оно'", "он", "она'", "они'"], "оно'",
           "Письмо' ends in -о, so it is neuter."),
        mc("You are speaking to your teacher. Which pronoun do you use for “you”?",
           ["вы", "ты", "он", "мы"], "вы",
           "Вы is the polite form for one person you don't know well, or who deserves respect."),
        mc("You are speaking to two friends together. Which do you use?", ["вы", "ты"], "вы",
           "Ты is only for one person. Several people are always вы."),
    ],
)

# ---------------------------------------------------------------------------- 6
L6 = lesson(
    "Possessives and gender",
    "Мой, моя', моё': match the thing owned, not the owner",
    requires=["мой", "твой", "наш", "ваш", "его", "её"],
    cards=[
        card("My, your, our",
             "The possessives мой, твой, наш and ваш change form to agree in gender with the thing owned. "
             "It is the noun that decides, never the owner: a woman says мой брат (masculine) and моя' "
             "сестра' (feminine) exactly as a man does. Tap a row to hear all three forms.",
             tables=[table(
                 ["", "Masculine", "Feminine", "Neuter"],
                 [["my", "мо{й}", "мо{я'}", "мо{ё'}"],
                  ["your (familiar)", "тво{й}", "тво{я'}", "тво{ё'}"],
                  ["our", "наш", "на'ш{а}", "на'ш{е}"],
                  ["your (polite/plural)", "ваш", "ва'ш{а}", "ва'ш{е}"]])],
             examples=[
                 ex("Э'то мой дом.", "This is my house.", "мой дом"),
                 ex("Э'то моя' кни'га.", "This is my book.", "моя' кни'га"),
                 ex("Э'то моё' окно'.", "This is my window.", "моё' окно'"),
                 ex("Э'то ва'ша сестра'.", "This is your sister.", "ва'ша сестра'"),
             ]),
        card("Three things to watch",
             "1. Masculine nouns that end in -а or -я take masculine forms: мой па'па, мой дя'дя.\n\n"
             "2. The neuter ends in -ё or -е: моё' окно', на'ше и'мя.\n\n"
             "3. Его' (his), её' (her) and их (their) never change, whatever they describe: его' дом, "
             "его' кни'га, её' окно', их де'ти.",
             examples=[
                 ex("Мой па'па до'ма.", "My dad is at home.", "Мой па'па"),
                 ex("Э'то его' кни'га.", "This is his book.", "его' кни'га"),
                 ex("Э'то её' брат.", "This is her brother.", "её' брат"),
             ]),
    ],
    verify=[("мой", "моя"), ("мой", "моё"), ("твой", "твоя"), ("твой", "твоё"),
            ("наш", "наша"), ("наш", "наше"), ("ваш", "ваша"), ("ваш", "ваше")],
    exercises=[
        fb("Э'то ___ сестра'.", ["моя'", "мой", "моё'"], "моя'",
           "Сестра' is feminine, so моя'.", tr="This is my sister."),
        fb("Э'то ___ окно'.", ["моё'", "мой", "моя'"], "моё'",
           "Окно' is neuter, so моё'.", tr="This is my window."),
        fb("___ па'па до'ма.", ["Мой", "Моя'", "Моё'"], "Мой",
           "Па'па names a man, so it is masculine despite its ending: мой па'па.", tr="My dad is at home."),
        fb("Где ___ кни'га?", ["ва'ша", "ваш", "ва'ше"], "ва'ша",
           "Кни'га is feminine, so ва'ша.", tr="Where is your (polite) book?"),
        fb("Э'то ___ дом.", ["наш", "на'ша", "на'ше"], "наш",
           "Дом is masculine, so наш.", tr="This is our house."),
        fb("Э'то ___ брат.", ["её'", "моя'", "мой", "ваш"], "её'",
           "Её' means “her”. It is the only form here that expresses the owner.", tr="This is her brother."),
        mc("Which possessive never changes its form?", ["его'", "мой", "твой", "наш"], "его'",
           "Его', её' and их stay the same for every noun."),
        mc("A woman introduces her brother. Which sentence is right?",
           ["Э'то мой брат.", "Э'то моя' брат.", "Э'то моё' брат.", "Э'то мой сестра'."],
           "Э'то мой брат.", "The owner's gender never matters: брат is masculine, so мой."),
        mc("Which of these nouns takes мой, even though it ends in -а?",
           ["па'па", "кни'га", "шко'ла", "ко'мната"], "па'па",
           "Па'па is a man, so masculine."),
    ],
)

# ---------------------------------------------------------------------------- 7
L7 = lesson(
    "Не or нет?",
    "Negating a word, and saying no",
    requires=["не", "нет", "да"],
    cards=[
        card("Не negates a word",
             "Не is the negative particle. Put it directly before the word it negates. English needs helpers "
             "such as “do not”; Russian just adds не. For now it goes before nouns, adjectives and "
             "place words; verbs come later in the course.",
             examples=[
                 ex("Э'то не мой дом.", "This is not my house.", "не мой"),
                 ex("Он не студе'нт.", "He is not a student.", "не студе'нт"),
                 ex("Она' не здесь.", "She is not here.", "не здесь"),
             ]),
        card("Нет means “no”",
             "Нет is the word for “no”. It answers a yes/no question, as the opposite of да, and a comma "
             "follows it. Notice that Russian uses both: нет answers the question, and не negates the statement.",
             tables=[table(
                 ["Word", "Job", "Example"],
                 [["не", "negates the word after it", "Он не врач."],
                  ["нет", "answers “no”", "— Он врач? — Нет, он не врач."]])]),
    ],
    exercises=[
        fb("Э'то ___ мой дом.", ["не", "нет", "ни", "нельзя'"], "не",
           "Не negates the word after it: “not my house”.", tr="This is not my house."),
        fb("— Ты студе'нт? — ___, я не студе'нт.", ["Нет", "Не", "Да", "Ни"], "Нет",
           "To answer “no” you say нет, followed by a comma.", tr="— Are you a student? — No, I'm not a student."),
        fb("Он ___ до'ма.", ["не", "нет", "ни", "да"], "не",
           "Не goes before the word it negates.", tr="He is not at home."),
        mc("How do you say “She is not a doctor”?",
           ["Она' не врач.", "Она' нет врач.", "Она' врач не.", "Она' не есть врач."],
           "Она' не врач.", "Не comes right before врач."),
        mc("— Ма'ма здесь?  How do you say “No, she isn't”?",
           ["Нет, она' не здесь.", "Нет она' не здесь.", "Не, она' нет здесь.", "Нет, она' нет здесь."],
           "Нет, она' не здесь.", "Нет answers the question (with a comma after it), and не negates здесь."),
        mc("Which word do you use on its own to answer “no”?", ["нет", "не", "ни", "нельзя'"], "нет",
           "Не can't stand alone; it always negates a word that follows."),
        mc("Which sentence is correct?",
           ["Э'то не ма'ма, а сестра'.", "Э'то нет ма'ма, а сестра'.", "Э'то не ма'ма, и сестра'.",
            "Э'то не ма'ма сестра'."],
           "Э'то не ма'ма, а сестра'.", "“Not X but Y” is не … а …, with a comma before а."),
        mc("In “Нет, он не врач”, which word negates врач?", ["не", "нет", "он", "врач"], "не",
           "Нет answers the question; не negates the word врач."),
    ],
)

UNIT = unit("Unit 1: Naming, asking and gender", [L1, L2, L3, L4, L5, L6, L7])
