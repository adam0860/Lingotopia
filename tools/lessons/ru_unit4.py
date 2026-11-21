"""Unit 4: more verbs  (textbook lesson 7, verbs and commands)."""
from dsl import *

# ---------------------------------------------------------------------------- 21
L21 = lesson(
    "Verbs in -ать: one pattern, many verbs",
    "Чита'ю, де'лаю, зна'ю, понима'ю",
    requires=["читать", "делать", "знать", "понимать", "думать"],
    cards=[
        card("Drop -ть, add the ending",
             "You already conjugated жить and рабо'тать. Most verbs ending in -ать work the same way. Take off -ть "
             "to get the stem, then add the ending that matches the subject: -ю, -ешь, -ет, -ем, -ете, -ют. For "
             "these verbs the stress never moves, so it is the same syllable in every form. Tap a row to hear it.",
             tables=[table(
                 ["", "чита'ть", "де'лать", "знать", "понима'ть"],
                 [["я", "чита'{ю}", "де'ла{ю}", "зна'{ю}", "понима'{ю}"],
                  ["ты", "чита'{ешь}", "де'ла{ешь}", "зна'{ешь}", "понима'{ешь}"],
                  ["он · она' · оно'", "чита'{ет}", "де'ла{ет}", "зна'{ет}", "понима'{ет}"],
                  ["мы", "чита'{ем}", "де'ла{ем}", "зна'{ем}", "понима'{ем}"],
                  ["вы", "чита'{ете}", "де'ла{ете}", "зна'{ете}", "понима'{ете}"],
                  ["они'", "чита'{ют}", "де'ла{ют}", "зна'{ют}", "понима'{ют}"]],
                 note="to read · to do, to make · to know · to understand")]),
        card("No “do” in Russian",
             "English needs a helper verb for questions and negatives (Do you know? I don't know). Russian does not: "
             "the verb alone is enough, and a question is just the same sentence said with a rising voice. "
             "Де'лать is only for really doing or making something, so Что ты де'лаешь? means “What are you doing?”, "
             "never the helper “do”.",
             examples=[
                 ex("Ты зна'ешь?", "Do you know?", "зна'ешь"),
                 ex("Я не зна'ю.", "I don't know.", "не зна'ю"),
                 ex("Что ты де'лаешь?", "What are you doing?", "де'лаешь"),
                 ex("Они' мно'го чита'ют.", "They read a lot.", "чита'ют"),
                 ex("Вы понима'ете?", "Do you understand?", "понима'ете"),
                 ex("Я ду'маю, что э'то хорошо'.", "I think this is good.", "ду'маю"),
             ]),
    ],
    verify=(vf("читать", "читаю", "читаешь", "читает", "читаем", "читаете", "читают")
            + vf("делать", "делаю", "делаешь", "делает", "делаем", "делаете", "делают")
            + vf("знать", "знаю", "знаешь", "знает", "знаем", "знаете", "знают")
            + vf("понимать", "понимаю", "понимаешь", "понимает", "понимаем", "понимаете", "понимают")),
    exercises=[
        fb("Я ___, что ты до'ма.", ["зна'ю", "зна'ешь", "зна'ет", "зна'ем"], "зна'ю",
           "Я takes -ю.", tr="I know that you are at home.", lemma="знать"),
        fb("Ты хорошо' ___?", ["понима'ешь", "понима'ю", "понима'ет", "понима'ем"], "понима'ешь",
           "Ты takes -ешь.", tr="Do you understand well?", lemma="понимать"),
        fb("Что он ___?", ["де'лает", "де'лаю", "де'лаешь", "де'лаем"], "де'лает",
           "Он takes -ет.", tr="What is he doing?", lemma="делать"),
        fb("Мы мно'го ___.", ["чита'ем", "чита'ю", "чита'ют", "чита'ете"], "чита'ем",
           "Мы takes -ем.", tr="We read a lot.", lemma="читать"),
        fb("Вы ___ э'то?", ["зна'ете", "зна'ем", "зна'ешь", "зна'ют"], "зна'ете",
           "Вы takes -ете.", tr="Do you know this?", lemma="знать"),
        fb("Что ты ___?", ["ду'маешь", "ду'маю", "ду'мает", "ду'мают"], "ду'маешь",
           "Ты takes -ешь.", tr="What do you think?", lemma="думать"),
        mc("Which ending does ты take with these verbs?", ["-ешь", "-ет", "-ем", "-ют"], "-ешь",
           "Ты → -ешь: чита'ешь, зна'ешь, де'лаешь.", order=True),
        mc("How do you say “I don't understand”?",
           ["Я не понима'ю.", "Я нет понима'ю.", "Я понима'ю не.", "Не я понима'ю."], "Я не понима'ю.",
           "Не goes right before the verb."),
        mc("Which form means “they know”?", ["зна'ют", "зна'ет", "зна'ем", "зна'ете"], "зна'ют",
           "Они' takes -ют.", lemma="знать"),
        mc("How do you ask “What do you do?” (to one friend)?",
           ["Что ты де'лаешь?", "Что ты де'лать?", "Что де'лаешь ты не?", "Что ты де'лаю?"],
           "Что ты де'лаешь?", "No helper verb: just Что + ты + the ты-form."),
    ],
)

# ---------------------------------------------------------------------------- 22
L22 = lesson(
    "Verbs that change their stem",
    "Пишу', пи'шешь: learn these one by one",
    requires=["писать", "ждать", "жить", "письмо", "друг"],
    cards=[
        card("Same endings, different stem",
             "A few verbs do not keep their infinitive stem. Писа'ть (to write) loses its -а- and its с becomes ш: "
             "пиш-. Ждать (to wait) loses its -а-: жд-. The endings are the ones you know. When the ending carries "
             "the stress, -е- is written as -ё- (ждёшь, like живёшь). Whatever changes shows up in every form, so "
             "learn the я-form together with the infinitive.",
             tables=[table(
                 ["", "писа'ть", "ждать", "жить"],
                 [["я", "пиш{у'}", "ж{ду}", "жив{у'}"],
                  ["ты", "пи'ш{ешь}", "жд{ёшь}", "жив{ёшь}"],
                  ["он · она' · оно'", "пи'ш{ет}", "жд{ёт}", "жив{ёт}"],
                  ["мы", "пи'ш{ем}", "жд{ём}", "жив{ём}"],
                  ["вы", "пи'ш{ете}", "жд{ёте}", "жив{ёте}"],
                  ["они'", "пи'ш{ут}", "ж{дут}", "жив{у'т}"]],
                 note="to write · to wait · to live. Note -у and -ут after a consonant (not -ю and -ют).")]),
        card("Where the stress goes",
             "Писа'ть keeps its stress on the stem in every form except я, where it jumps to the ending: пишу'. "
             "Ждать and жить have the stress on the ending throughout. Both patterns are common, so listen "
             "for the stress each time you tap a form.",
             examples=[
                 ex("Я пишу' письмо'.", "I'm writing a letter.", "пишу'"),
                 ex("Ты пи'шешь ча'сто?", "Do you write often?", "пи'шешь"),
                 ex("Мы ждём до'ма.", "We're waiting at home.", "ждём"),
                 ex("Они' ждут здесь.", "They're waiting here.", "ждут"),
             ]),
    ],
    verify=(vf("писать", "пишу", "пишешь", "пишет", "пишем", "пишете", "пишут")
            + vf("ждать", "жду", "ждёшь", "ждёт", "ждём", "ждёте", "ждут")),
    exercises=[
        fb("Я ___ письмо'.", ["пишу'", "пи'шешь", "пи'шет", "пи'шут"], "пишу'",
           "The я-form is пишу'.", tr="I'm writing a letter.", lemma="писать"),
        fb("Ты ___ письмо'?", ["пи'шешь", "пишу'", "пи'шет", "пи'шем"], "пи'шешь",
           "Ты takes -ешь, and the stress stays on the stem.", tr="Are you writing a letter?", lemma="писать"),
        fb("Мы ___ диало'г.", ["пи'шем", "пи'шет", "пишу'", "пи'шут"], "пи'шем",
           "Мы takes -ем.", tr="We're writing a dialogue.", lemma="писать"),
        fb("Они' ___ ча'сто.", ["пи'шут", "пи'шет", "пишу'", "пи'шете"], "пи'шут",
           "Они' takes -ут: the stem ends in a consonant.", tr="They write often.", lemma="писать"),
        fb("Мы ___ здесь.", ["ждём", "жду", "ждёт", "ждёшь"], "ждём",
           "Мы takes -ём here, because the ending is stressed.", tr="We're waiting here.", lemma="ждать"),
        fb("Я ___ тебя' до'ма.", ["жду", "ждёшь", "ждёт", "ждут"], "жду",
           "The я-form of ждать is жду.", tr="I'm waiting for you at home.", lemma="ждать"),
        fb("Они' ___ здесь.", ["живу'т", "живёт", "живёшь", "живу'"], "живу'т",
           "Они' takes -ут for жить.", tr="They live here.", lemma="жить"),
        mc("What happens to the stem of писа'ть in the present tense?",
           ["Part of it drops out and the consonant changes",
            "Nothing: it is regular", "Only the я-form changes", "The ending -ть is kept"],
           "Part of it drops out and the consonant changes",
           "Пиш- replaces писа-, and the change appears in every form.", order=True),
        mc("Which sentence is correct?",
           ["Мы ждём.", "Мы жду.", "Мы ждёт.", "Мы ждёшь."], "Мы ждём.", "Мы takes -ём."),
    ],
)

# ---------------------------------------------------------------------------- 23
L23 = lesson(
    "The second family: говори'ть, учи'ть, смотре'ть",
    "Говорю', говори'шь, говори'т",
    requires=["говорить", "смотреть", "видеть", "слышать", "учить"],
    cards=[
        card("Drop -ть and the vowel before it",
             "Russian has two families of verbs. You have met the first (-ю, -ешь, -ет, -ем, -ете, -ют). The second "
             "family has its own endings: -ю, -ишь, -ит, -им, -ите, -ят. To conjugate one, drop -ть and the vowel "
             "before it (говори'-ть → говор-), then add the ending.",
             tables=[table(
                 ["", "говори'ть", "учи'ть", "смотре'ть"],
                 [["я", "говор{ю'}", "уч{у'}", "смотр{ю'}"],
                  ["ты", "говор{и'шь}", "у'ч{ишь}", "смо'тр{ишь}"],
                  ["он · она' · оно'", "говор{и'т}", "у'ч{ит}", "смо'тр{ит}"],
                  ["мы", "говор{и'м}", "у'ч{им}", "смо'тр{им}"],
                  ["вы", "говор{и'те}", "у'ч{ите}", "смо'тр{ите}"],
                  ["они'", "говор{я'т}", "у'ч{ат}", "смо'тр{ят}"]],
                 note="to speak · to learn, to teach · to watch, to look. Why -у and -ат in учи'ть? See lesson 25.")]),
        card("Which family is a verb in?",
             "Almost every verb in -ить belongs to the second family. A handful of others do too, including "
             "смотре'ть, ви'деть and слы'шать (to hear). Most verbs in -ать and -ять belong to the first. When you "
             "learn a new verb, learn its я-form and ты-form with it, and the family is obvious: -ешь means first, "
             "-ишь means second.",
             tables=[table(
                 ["", "First family", "Second family"],
                 [["ты", "-{ешь}", "-{ишь}"],
                  ["он · она' · оно'", "-{ет}", "-{ит}"],
                  ["мы", "-{ем}", "-{им}"],
                  ["вы", "-{ете}", "-{ите}"],
                  ["они'", "-{ют}", "-{ят}"]])],
             examples=[
                 ex("Мы говори'м по-ру'сски.", "We speak Russian.", "говори'м"),
                 ex("Он хорошо' у'чит слова'.", "He learns words well.", "у'чит"),
                 ex("Вы смо'трите фильм?", "Are you watching a film?", "смо'трите"),
                 ex("Они' хорошо' слы'шат.", "They hear well.", "слы'шат"),
             ]),
    ],
    verify=(vf("говорить", "говорю", "говоришь", "говорит", "говорим", "говорите", "говорят")
            + vf("учить", "учу", "учишь", "учит", "учим", "учите", "учат")
            + vf("смотреть", "смотрю", "смотришь", "смотрит", "смотрим", "смотрите", "смотрят")
            + vf("слышать", "слышат")),
    exercises=[
        fb("Я ___ по-ру'сски.", ["говорю'", "говори'шь", "говори'т", "говоря'т"], "говорю'",
           "Я takes -ю.", tr="I speak Russian.", lemma="говорить"),
        fb("Ты ___ по-англи'йски?", ["говори'шь", "говорю'", "говори'т", "говори'м"], "говори'шь",
           "Second family: ты takes -ишь.", tr="Do you speak English?", lemma="говорить"),
        fb("Она' ___ фильм.", ["смо'трит", "смотрю'", "смо'тришь", "смо'трят"], "смо'трит",
           "Second family: она' takes -ит.", tr="She is watching a film.", lemma="смотреть"),
        fb("Мы ___ но'вые слова'.", ["у'чим", "у'чит", "у'чите", "у'чат"], "у'чим",
           "Second family: мы takes -им.", tr="We are learning new words.", lemma="учить"),
        fb("Вы ___ меня'?", ["слы'шите", "слы'шишь", "слы'шат", "слы'шим"], "слы'шите",
           "Second family: вы takes -ите.", tr="Do you hear me?", lemma="слышать"),
        fb("Они' ___ по-ру'сски.", ["говоря'т", "говоря'", "говори'т", "говорю'т"], "говоря'т",
           "Second family: они' takes -ят.", tr="They speak Russian.", lemma="говорить"),
        mc("Which ending belongs to the second family?", ["-ишь", "-ешь", "-ёшь", "-ют"], "-ишь",
           "Ты takes -ишь in the second family and -ешь in the first.", order=True),
        mc("Which verb belongs to the second family?",
           ["говори'ть", "чита'ть", "де'лать", "писа'ть"], "говори'ть", "Almost all verbs in -ить are second family."),
        mc("What do you drop from смотре'ть before adding an ending?",
           ["-ть and the vowel before it", "only -ть", "only the last letter", "nothing"],
           "-ть and the vowel before it", "Смотре'ть → смотр-.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 24
L24 = lesson(
    "When the я-form changes its consonant",
    "Ви'жу, ви'дишь: only the first person changes",
    requires=["видеть", "любить", "ходить", "сидеть", "платить"],
    cards=[
        card("One form that is different",
             "Many second-family verbs change the last consonant of the stem, but only in the я-form. The other "
             "five forms use the consonant you see in the infinitive. Видеть is the model: д becomes ж in "
             "ви'жу, then it is back to д in ви'дишь, ви'дит, ви'дим, ви'дите, ви'дят.",
             tables=[table(
                 ["", "ви'деть", "люби'ть"],
                 [["я", "ви'{жу}", "люб{лю'}"],
                  ["ты", "ви'дишь", "лю'бишь"],
                  ["он · она' · оно'", "ви'дит", "лю'бит"],
                  ["мы", "ви'дим", "лю'бим"],
                  ["вы", "ви'дите", "лю'бите"],
                  ["они'", "ви'дят", "лю'бят"]],
                 note="to see · to love, to like")]),
        card("Common changes",
             "The change is not random: the same few swaps keep coming back. You have to learn which verbs do it, "
             "but the я-form shows you straight away. Смотре'ть, говори'ть and учи'ть do not change at all, "
             "so compare them with the verbs below.",
             tables=[table(
                 ["Change", "Verb", "я", "ты"],
                 [["д → ж", "ходи'ть (to walk)", "хож{у'}", "хо'дишь"],
                  ["д → ж", "сиде'ть (to sit)", "сиж{у'}", "сиди'шь"],
                  ["б → бл", "люби'ть", "люб{лю'}", "лю'бишь"],
                  ["т → ч", "плати'ть (to pay)", "пла{чу'}", "пла'тишь"]])]),
    ],
    verify=(vf("видеть", "вижу", "видишь", "видит", "видим", "видите", "видят")
            + vf("любить", "люблю", "любишь", "любит", "любим", "любите", "любят")
            + vf("ходить", "хожу", "ходишь") + vf("сидеть", "сижу", "сидишь")
            + vf("платить", "плачу", "платишь")),
    exercises=[
        fb("Я ___ дом.", ["ви'жу", "ви'дишь", "ви'дит", "ви'дят"], "ви'жу",
           "In the я-form д becomes ж.", tr="I see a house.", lemma="видеть"),
        fb("Ты ___ меня'?", ["ви'дишь", "ви'жу", "ви'дит", "ви'дим"], "ви'дишь",
           "Only the я-form changes. Ты has the plain д.", tr="Do you see me?", lemma="видеть"),
        fb("Мы ___ шко'лу.", ["ви'дим", "ви'жем", "ви'дят", "ви'жу"], "ви'дим",
           "Мы has the plain д.", tr="We see the school.", lemma="видеть"),
        fb("Я ___ э'ту кни'гу.", ["люблю'", "лю'бишь", "лю'бит", "лю'бят"], "люблю'",
           "The я-form is люблю' (б becomes бл).", tr="I love this book.", lemma="любить"),
        fb("Они' ___ рок.", ["лю'бят", "лю'бит", "люблю'", "лю'бите"], "лю'бят",
           "Они' takes -ят, with the plain б.", tr="They love rock music.", lemma="любить"),
        fb("Я ча'сто ___ в па'рке.", ["хожу'", "хо'дишь", "хо'дит", "хо'дят"], "хожу'",
           "Ходи'ть: д becomes ж in the я-form.", tr="I often walk in the park.", lemma="ходить"),
        fb("Мы ___ до'ма.", ["сиди'м", "сижу'", "сидя'т", "сидя'"], "сиди'м",
           "Only the я-form changes: мы has the plain д.", tr="We are sitting at home.", lemma="сидеть"),
        mc("In which form does the consonant change?",
           ["я", "ты", "они'", "мы"], "я", "The change affects the я-form only.", order=True),
        mc("What is the я-form of плати'ть?", ["плачу'", "плату'", "плажу'", "пла'тю"], "плачу'",
           "Т → ч.", lemma="платить"),
    ],
)

# ---------------------------------------------------------------------------- 25
L25 = lesson(
    "Two spelling rules",
    "Which letters you may not write after others",
    requires=["писать", "учить", "книга", "русский", "хороший"],
    cards=[
        card("The seven-letter rule",
             "After the seven letters к, г, х, ж, ч, ш, щ, Russian never writes ы, я or ю. It writes и, а, у "
             "instead. That is why the plural of кни'га is кни'ги (never кни'гы), why the они'-form of учи'ть is "
             "у'чат (never у'чят), and why the я-form of писа'ть is пишу' (never пишю'). Whenever a regular "
             "ending would put one of those letters after these consonants, the spelling changes, and the "
             "sound stays the same.",
             tables=[table(
                 ["After к г х ж ч ш щ", "Instead of", "Example"],
                 [["{и}", "ы", "кни'г{и}, ру'чк{и}"],
                  ["{а}", "я", "у'ч{ат}, слы'ш{ат}"],
                  ["{у}", "ю", "пиш{у'}, уч{у'}, леж{у'}"]])]),
        card("The five-letter rule",
             "After ж, ч, ш, щ and ц, an unstressed о is written е. You see it in neuter adjectives and in some "
             "pronouns: хоро'шее (not хоро'шое), на'ше (not на'шо). If the о is stressed, it stays: большо'е.",
             tables=[table(
                 ["Stress", "Neuter ending", "Example"],
                 [["unstressed", "-{ее}", "хоро'ш{ее} ме'сто"],
                  ["unstressed", "-{е}", "на'ш{е} окно'"],
                  ["stressed", "-{о'е}", "больш{о'е} окно'"]],
                 note="The five-letter rule applies after ж ч ш щ ц; the seven-letter rule after к г х ж ч ш щ.")],
             examples=[
                 ex("Э'то хоро'шее вино'.", "This is good wine.", "хоро'шее"),
                 ex("Э'то на'ше окно'.", "This is our window.", "на'ше"),
                 ex("Они' у'чат слова'.", "They are learning words.", "у'чат"),
                 ex("Я пишу' письмо'.", "I'm writing a letter.", "пишу'"),
             ]),
    ],
    verify=(vf("хороший", "хорошее") + vf("наш", "наше") + vf("большой", "большое")
            + vf("книга", "книги") + vf("ручка", "ручки") + vf("учить", "учат")),
    exercises=[
        fb("Вот мои' ___.", ["кни'ги", "кни'гы", "кни'га", "кни'гу"], "кни'ги",
           "After г you write и, never ы.", tr="Here are my books."),
        fb("Вот ва'ши ___.", ["ру'чки", "ру'чкы", "ру'чка", "ру'чку"], "ру'чки",
           "After к you write и, never ы.", tr="Here are your pens."),
        fb("Они' ___ слова'.", ["у'чат", "у'чят", "у'чут", "у'чют"], "у'чат",
           "After ч you write а, never я.", tr="They learn words.", lemma="учить"),
        fb("Я ___ письмо'.", ["пишу'", "пишю'", "пи'шет", "пи'шем"], "пишу'",
           "After ш you write у, never ю.", tr="I'm writing a letter."),
        fb("Э'то хоро'шее ___.", ["вино'", "вина'", "вину'", "вине'"], "вино'",
           "Хоро'шее is neuter, so a neuter noun follows. Note ее after ш.", tr="This is good wine."),
        fb("Э'то ___ окно'.", ["на'ше", "на'шо", "на'ша", "на'ши"], "на'ше",
           "After ш an unstressed о becomes е: на'ше.", tr="This is our window."),
        mc("Which spelling is correct?",
           ["ру'сские кни'ги", "ру'сскые кни'ги", "ру'сские кни'гы", "ру'сскые кни'гы"], "ру'сские кни'ги",
           "After к and г you cannot write ы."),
        mc("Which of these letters does the five-letter rule NOT include?",
           ["к", "ж", "ч", "ц"], "к", "The five letters are ж, ч, ш, щ, ц. К belongs to the seven-letter rule only.", order=True),
        mc("Why is it большо'е окно', not большее?",
           ["The о is stressed, so it stays", "Because окно' is masculine", "Because ш is a soft letter",
            "It is an exception with no reason"],
           "The о is stressed, so it stays", "Only an unstressed о changes to е."),
    ],
)

# ---------------------------------------------------------------------------- 26
L26 = lesson(
    "Commands: Чита'й! Пиши'!",
    "Making the imperative from the они'-form",
    requires=["читать", "писать", "слушать", "отвечать", "спрашивать"],
    cards=[
        card("How to build a command",
             "Take the они'-form of the verb and drop the ending (-ут, -ют, -ат, -ят). If a vowel is left at the "
             "end, add -й (to one friend, ты) or -йте (to someone you address as вы, or to several people). If a "
             "consonant is left, add -и (ты) or -и'те (вы), and the stress goes on the и in all the verbs below. Add "
             "пожа'луйста to be polite.",
             tables=[table(
                 ["Verb", "они'-form", "Stem ends in", "ты", "вы"],
                 [["рабо'тать", "рабо'тают", "vowel", "рабо'та{й}", "рабо'та{йте}"],
                  ["чита'ть", "чита'ют", "vowel", "чита'{й}", "чита'{йте}"],
                  ["писа'ть", "пи'шут", "consonant", "пиш{и'}", "пиш{и'те}"],
                  ["учи'ть", "у'чат", "consonant", "уч{и'}", "уч{и'те}"],
                  ["говори'ть", "говоря'т", "consonant", "говор{и'}", "говор{и'те}"],
                  ["смотре'ть", "смо'трят", "consonant", "смотр{и'}", "смотр{и'те}"]],
                 note="Stress of -и commands lands on the и, as shown.")]),
        card("In use",
             "A command is addressed to someone, so ты or вы is already understood. Use the вы-form with "
             "people you do not know well, a group, or anyone you would address politely. To tell someone not "
             "to do something, put не before the command: Не чита'й!",
             examples=[
                 ex("Чита'й, пожа'луйста!", "Read, please! (to a friend)", "Чита'й"),
                 ex("Пиши' мне!", "Write to me! (to a friend)", "Пиши'"),
                 ex("Слу'шайте меня'!", "Listen to me! (to a group, or politely)", "Слу'шайте"),
                 ex("Отвеча'йте, пожа'луйста.", "Please answer. (polite)", "Отвеча'йте"),
                 ex("Не спра'шивай!", "Don't ask!", "Не спра'шивай"),
             ]),
    ],
    verify=(vf("работать", "работай", "работайте") + vf("читать", "читай", "читайте")
            + vf("писать", "пиши", "пишите") + vf("учить", "учи", "учите")
            + vf("говорить", "говори", "говорите") + vf("смотреть", "смотри", "смотрите")
            + vf("слушать", "слушай", "слушайте") + vf("отвечать", "отвечай", "отвечайте")
            + vf("спрашивать", "спрашивай")),
    exercises=[
        fb("___, пожа'луйста! (to a friend: read)", ["Чита'й", "Чита'йте", "Читаю'", "Чита'ет"], "Чита'й",
           "Они' чита'ют → чита'- + й.", tr="Read, please!", lemma="читать"),
        fb("___ меня'! (to a group: listen)", ["Слу'шайте", "Слу'шай", "Слу'шать", "Слу'шаете"], "Слу'шайте",
           "Слу'шают → слу'шай- + те.", tr="Listen to me!", lemma="слушать"),
        fb("___ мне! (to a friend: write)", ["Пиши'", "Пи'шай", "Пишу'", "Пи'шет"], "Пиши'",
           "Пи'шут → пиш- (a consonant), so add -и, stressed.", tr="Write to me!", lemma="писать"),
        fb("___ мне, пожа'луйста! (polite: write)", ["Пиши'те", "Пиши'", "Пи'шете", "Пи'шайте"], "Пиши'те",
           "A consonant stem plus -ите for вы.", tr="Please write to me.", lemma="писать"),
        fb("___ по-ру'сски! (to a friend: speak)", ["Говори'", "Говори'й", "Говорю'", "Говоря'т"], "Говори'",
           "Говоря'т → говор- (a consonant), so add -и.", tr="Speak Russian!", lemma="говорить"),
        fb("___ на вопро'с! (polite: answer)", ["Отвеча'йте", "Отвеча'й", "Отвечи'те", "Отвеча'ете"], "Отвеча'йте",
           "Отвеча'ют → отвеча- (a vowel) + йте.", tr="Answer the question!", lemma="отвечать"),
        mc("What do you add to a stem that ends in a vowel (to one friend)?",
           ["-й", "-и", "-йте", "-ь"], "-й", "Vowel → -й, consonant → -и.", order=True),
        mc("How do you say “Don't read!” to a friend?",
           ["Не чита'й!", "Нет чита'й!", "Чита'й не!", "Не чита'ешь!"], "Не чита'й!",
           "Не goes before the command."),
        mc("Which command is polite or plural?",
           ["Смотри'те!", "Смотри'!", "Смотрю'!", "Смо'трит!"], "Смотри'те!", "The -те ending marks вы."),
    ],
)

UNIT = unit("Unit 4: More verbs", [L21, L22, L23, L24, L25, L26])
