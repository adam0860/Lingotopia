"""Unit 11: reflexive verbs, the genitive case, and bigger numbers
(textbook module 3, lesson 16)."""
from dsl import *

# ---------------------------------------------------------------------------- 75
L75 = lesson(
    "Verbs with -ся: washing and dressing",
    "Я умыва'юсь, он одева'ется",
    requires=["мальчик", "девочка", "мужчина", "женщина", "ребёнок"],
    cards=[
        card("The little word -ся",
             "Many Russian verbs end in -ся, or in -сь after a vowel. It is a leftover of себя' (oneself). When "
             "the action is done to the person who does it, the verb takes this ending: I wash myself becomes "
             "Я умыва'юсь. A verb without -ся needs someone else to act on, and that someone is the direct "
             "object, in the accusative. Verbs of grooming are the clearest case.",
             tables=[table(
                 ["Verb", "Acts on someone else", "Acts on oneself"],
                 [["умыва'ть", "Я умыва'ю ребёнка.", "Я умыва'юсь."],
                  ["одева'ть", "Он одева'ет сы'на.", "Он одева'ется."],
                  ["причёсывать", "Она' причёсывает дочь.", "Она' причёсывается."],
                  ["брить", "Он бре'ет отца'.", "Он бре'ется."]])]),
        card("Same endings, plus -ся",
             "A verb with -ся is conjugated like the verb without it. Just add -ся after a consonant or й, and "
             "-сь after a vowel. The ты-form ends in -шься and the он-form in -тся, and -тся is pronounced "
             "as if it were -ца, which you will quickly get used to. English often drops “himself” "
             "(“he is shaving”), but Russian never can: Он бре'ется, never just Он бре'ет.",
             tables=[table(
                 ["Person", "умыва'ться", "одева'ться"],
                 [["я", "умыва'ю{сь}", "одева'ю{сь}"],
                  ["ты", "умыва'ешь{ся}", "одева'ешь{ся}"],
                  ["он · она' · оно'", "умыва'ет{ся}", "одева'ет{ся}"],
                  ["мы", "умыва'ем{ся}", "одева'ем{ся}"],
                  ["вы", "умыва'ете{сь}", "одева'ете{сь}"],
                  ["они'", "умыва'ют{ся}", "одева'ют{ся}"]],
                 note="Past: умыва'лся, умыва'лась, умыва'лось, умыва'лись.")],
             examples=[
                 ex("Де'вочка умыва'ется.", "The girl is washing her face.", "умыва'ется"),
                 ex("Ма'льчик одева'ется.", "The boy is getting dressed.", "одева'ется"),
                 ex("Мужчи'на бре'ется.", "The man is shaving.", "бре'ется"),
                 ex("Же'нщина причёсывается.", "The woman is combing her hair.", "причёсывается"),
                 ex("Я умыва'ю ребёнка.", "I am washing the child's face.", "умыва'ю"),
             ]),
    ],
    verify=(vf("умываться", "умываюсь", "умываешься", "умывается", "умываемся", "умываетесь", "умываются", "умывался", "умывалась")
            + vf("одеваться", "одеваюсь", "одеваешься", "одевается", "одеваемся", "одеваетесь", "одеваются")
            + vf("умывать", "умываю") + vf("одевать", "одевает") + vf("причёсывать", "причёсывает")
            + vf("причёсываться", "причёсывается") + vf("брить", "бреет") + vf("бриться", "бреется")
            + vf("ребёнок", "ребёнка")),
    exercises=[
        fb("Я ___ у'тром.", ["умыва'юсь", "умыва'ю", "умыва'ется", "умыва'емся"], "умыва'юсь",
           "The action is done to oneself: -сь after a vowel.", tr="I wash my face in the morning.", lemma="умываться"),
        fb("Ма'льчик ___.", ["одева'ется", "одева'ет", "одева'ются", "одева'ешься"], "одева'ется",
           "He dresses himself: одева'ется.", tr="The boy is getting dressed.", lemma="одеваться"),
        fb("Мужчи'на ___.", ["бре'ется", "бре'ет", "бре'ются", "бре'юсь"], "бре'ется",
           "Russian never drops -ся here.", tr="The man is shaving.", lemma="бриться"),
        fb("Мы ___ ра'но.", ["одева'емся", "одева'ем", "одева'ется", "одева'ются"], "одева'емся",
           "Мы takes -емся.", tr="We get dressed early.", lemma="одеваться"),
        fb("Она' ___ дочь.", ["причёсывает", "причёсывается", "причёсываюсь", "причёсываются"], "причёсывает",
           "There is an object (дочь), so no -ся.", tr="She is combing her daughter's hair.", lemma="причёсывать"),
        fb("Я умыва'ю ___.", ["ребёнка", "ребёнок", "ребёнке", "ребёнку"], "ребёнка",
           "A direct object that is a person: accusative.", tr="I am washing the child's face.", lemma="ребёнок"),
        fb("Ты ___ ра'но?", ["умыва'ешься", "умыва'ется", "умыва'юсь", "умыва'етесь"], "умыва'ешься",
           "Ты takes -ешься.", tr="Do you wash up early?", lemma="умываться"),
        mc("Which ending do you add to a verb that ends in a vowel?", ["-сь", "-ся", "-ться", "-за"], "-сь",
           "Я умыва'юсь (after the vowel ю).", order=True),
        mc("Which sentence means “He is shaving”?", ["Он бре'ется.", "Он бре'ет.", "Он бре'юсь.", "Они' бре'ется."],
           "Он бре'ется.", "Never drop -ся."),
        mc("Which pronoun does -ся come from?", ["себя'", "свой", "сам", "ся"], "себя'",
           "Oneself.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 76
L76 = lesson(
    "Things that start, open and end by themselves",
    "Уро'к начина'ется, магази'н открыва'ется",
    requires=["начинаться", "заканчиваться", "открываться", "называться", "урок"],
    cards=[
        card("From object to subject",
             "Most -ся verbs are not about washing yourself at all. Adding -ся to a verb that needs an object "
             "makes it a verb that does not. The thing that was the object becomes the subject: the teacher "
             "starts the lesson, and the lesson starts. The meaning of the verb hardly changes. The new verb "
             "can never take a direct object, so no accusative follows it.",
             tables=[table(
                 ["Verb", "Someone does it", "It happens by itself"],
                 [["начина'ть", "Учи'тель начина'ет уро'к.", "Уро'к начина'ется."],
                  ["зака'нчивать", "Дире'ктор зака'нчивает встре'чу.", "Встре'ча зака'нчивается."],
                  ["открыва'ть", "Продаве'ц открыва'ет магази'н.", "Магази'н открыва'ется."],
                  ["закрыва'ть", "Он закрыва'ет две'ри.", "Две'ри закрыва'ются."]])]),
        card("Called, and the past tense",
             "Называ'ться is also a -ся verb. It is how you ask and say what something is called: Как "
             "называ'ется э'тот фильм? — Он называ'ется «Весна'». For more than one thing use называ'ются. "
             "In the past tense -ся stays at the end: the verb agrees with its subject, and then -ся or -сь "
             "follows.",
             tables=[table(
                 ["Subject", "начина'ться", "зако'нчиться (once)"],
                 [["masculine", "начина'л{ся}", "зако'нчил{ся}"],
                  ["feminine", "начина'л{ась}", "зако'нчил{ась}"],
                  ["neuter", "начина'л{ось}", "зако'нчил{ось}"],
                  ["plural", "начина'л{ись}", "зако'нчил{ись}"]])],
             examples=[
                 ex("Уро'к начина'ется в де'вять часо'в.", "The lesson starts at nine o'clock.", "начина'ется"),
                 ex("Магази'н открыва'ется в во'семь часо'в утра'.", "The store opens at eight in the morning.", "открыва'ется"),
                 ex("Осторо'жно! Две'ри закрыва'ются.", "Careful! The doors are closing.", "закрыва'ются"),
                 ex("Встре'ча зако'нчилась в семь часо'в ве'чера.", "The meeting ended at seven in the evening.", "зако'нчилась"),
                 ex("Как называ'ется э'тот фильм?", "What is this film called?", "называ'ется"),
             ]),
    ],
    verify=(vf("начинаться", "начинается", "начинается", "начинался", "начиналась", "начиналось", "начинались")
            + vf("закончиться", "закончился", "закончилась", "закончилось", "закончились")
            + vf("заканчиваться", "заканчивается") + vf("открываться", "открывается")
            + vf("закрываться", "закрываются") + vf("называться", "называется", "называются")
            + vf("начинать", "начинает") + vf("заканчивать", "заканчивает") + vf("открывать", "открывает")
            + vf("закрывать", "закрывает")),
    exercises=[
        fb("Уро'к ___ в де'вять часо'в.", ["начина'ется", "начина'ет", "начина'ются", "начина'ю"], "начина'ется",
           "The lesson is the subject, and it starts by itself.", tr="The lesson starts at nine o'clock.", lemma="начинаться"),
        fb("Учи'тель ___ уро'к.", ["начина'ет", "начина'ется", "начина'ются", "начина'ете"], "начина'ет",
           "There is an object (уро'к), so no -ся.", tr="The teacher starts the lesson.", lemma="начинать"),
        fb("Магази'н ___ в во'семь часо'в утра'.", ["открыва'ется", "открыва'ет", "открыва'ются", "открыва'ешь"], "открыва'ется",
           "The store is the subject: -ется.", tr="The store opens at eight in the morning.", lemma="открываться"),
        fb("Продаве'ц ___ магази'н.", ["открыва'ет", "открыва'ется", "открыва'ются", "открыва'емся"], "открыва'ет",
           "There is an object, so no -ся.", tr="The salesperson opens the store.", lemma="открывать"),
        fb("Осторо'жно! Две'ри ___.", ["закрыва'ются", "закрыва'ется", "закрыва'ет", "закрыва'ем"], "закрыва'ются",
           "Две'ри is plural: -ются.", tr="Careful! The doors are closing.", lemma="закрываться"),
        fb("Встре'ча ___ в семь часо'в ве'чера.", ["зако'нчилась", "зако'нчил", "зако'нчились", "зако'нчилось"], "зако'нчилась",
           "Встре'ча is feminine: -лась.", tr="The meeting ended at seven in the evening.", lemma="закончиться"),
        fb("Как ___ э'тот фильм?", ["называ'ется", "называ'ются", "называ'ться", "называ'юсь"], "называ'ется",
           "Singular subject: называ'ется.", tr="What is this film called?", lemma="называться"),
        fb("Как ___ э'ти кни'ги?", ["называ'ются", "называ'ется", "называ'ться", "называ'юсь"], "называ'ются",
           "Plural subject: называ'ются.", tr="What are these books called?", lemma="называться"),
        mc("Which sentence means “The lesson is starting”?",
           ["Уро'к начина'ется.", "Уро'к начина'ешься.", "Уро'к начина'юсь.", "Уро'к начина'емся."],
           "Уро'к начина'ется.", "Third person with -ся."),
        mc("Can a verb with -ся take a direct object?", ["No", "Yes, always", "Only in the past", "Only with people"], "No",
           "A -ся verb is intransitive.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 77
L77 = lesson(
    "To study and to learn: учи'ться",
    "Я учу'сь, мы у'чимся, ребёнок у'чится ходи'ть",
    requires=["учиться", "учить", "научить", "школа", "институт"],
    cards=[
        card("Учи'ть and учи'ться",
             "Учи'ть takes an object. It means to learn something by heart (Он у'чит слова') or to teach "
             "someone (Мать у'чит ребёнка ходи'ть). Учи'ться has -ся and no object: it means to study or to "
             "learn. It is a second-family verb with a consonant change in the я-form: учу'сь, у'чишься, "
             "у'чится. The perfective is научи'ться, which adds на-, and means to learn how to do something "
             "once and for all.",
             tables=[table(
                 ["Person", "учи'ться", "научи'ться (future)"],
                 [["я", "уч{у'сь}", "науч{у'сь}"],
                  ["ты", "у'ч{ишься}", "нау'ч{ишься}"],
                  ["он · она' · оно'", "у'ч{ится}", "нау'ч{ится}"],
                  ["мы", "у'ч{имся}", "нау'ч{имся}"],
                  ["вы", "у'ч{итесь}", "нау'ч{итесь}"],
                  ["они'", "у'ч{атся}", "нау'ч{атся}"]],
                 note="Past: учи'лся, учи'лась, учи'лось, учи'лись. Future: бу'ду учи'ться. Command: Учи'сь! Учи'тесь!")]),
        card("Three ways to use it",
             "To say where you study, use в and the prepositional: Она' у'чится в шко'ле. To say how well, add "
             "an adverb: Она' у'чится хорошо'. To say what you are learning to do, add an infinitive: Ребёнок "
             "у'чится ходи'ть. Compare Мать у'чит ребёнка ходи'ть, where somebody teaches.",
             examples=[
                 ex("Я учу'сь в институ'те.", "I study at the institute.", "учу'сь"),
                 ex("Ма'ша у'чится в шко'ле.", "Masha goes to school.", "у'чится"),
                 ex("Она' у'чится хорошо'.", "She is a good student.", "у'чится"),
                 ex("Ребёнок у'чится ходи'ть.", "The child is learning to walk.", "у'чится"),
                 ex("Мать у'чит ребёнка ходи'ть.", "The mother is teaching the child to walk.", "у'чит"),
                 ex("За'втра я научу'сь пла'вать.", "Tomorrow I will learn to swim.", "научу'сь"),
             ]),
    ],
    verify=(vf("учиться", "учусь", "учишься", "учится", "учимся", "учитесь", "учатся", "учился", "училась", "учились", "учись")
            + vf("научиться", "научусь", "научишься", "научится", "научимся", "научитесь", "научатся")
            + vf("учить", "учит")),
    exercises=[
        fb("Я ___ в институ'те.", ["учу'сь", "учу'", "у'чишься", "у'чатся"], "учу'сь",
           "Study at a school: учи'ться, я-form учу'сь.", tr="I study at the institute.", lemma="учиться"),
        fb("Ты хорошо' ___.", ["у'чишься", "учу'сь", "у'чится", "у'чимся"], "у'чишься",
           "Ты takes -ишься.", tr="You study well.", lemma="учиться"),
        fb("Мы ___ в шко'ле.", ["у'чимся", "учу'сь", "у'чится", "у'читесь"], "у'чимся",
           "Мы takes -имся.", tr="We study at school.", lemma="учиться"),
        fb("Ребёнок ___ ходи'ть.", ["у'чится", "у'чит", "у'чатся", "у'чишься"], "у'чится",
           "He is learning (himself): -ся.", tr="The child is learning to walk.", lemma="учиться"),
        fb("Мать ___ ребёнка ходи'ть.", ["у'чит", "у'чится", "у'чатся", "у'читесь"], "у'чит",
           "She teaches somebody else: no -ся.", tr="The mother is teaching the child to walk.", lemma="учить"),
        fb("Вчера' она' ___ в шко'ле.", ["учи'лась", "учи'лся", "учи'лись", "учи'лось"], "учи'лась",
           "Feminine past: учи'лась.", tr="Yesterday she was at school.", lemma="учиться"),
        fb("За'втра я ___ пла'вать.", ["научу'сь", "научи'лся", "научу'", "нау'чится"], "научу'сь",
           "Learn how to, once and for all: the perfective.", tr="Tomorrow I will learn to swim.", lemma="научиться"),
        mc("Which verb means “to study at a school or college”?", ["учи'ться", "учи'ть", "научи'ть", "уче'бник"], "учи'ться",
           "Учи'ться, with -ся.", order=True),
        mc("Which sentence means “The child is learning to walk”?",
           ["Ребёнок у'чится ходи'ть.", "Ребёнок у'чит ходи'ть.", "Ребёнок у'чишься ходи'ть.", "Ребёнок у'чатся ходи'ть."],
           "Ребёнок у'чится ходи'ть.", "Он-form of учи'ться."),
    ],
)

# ---------------------------------------------------------------------------- 78
L78 = lesson(
    "Whose? The owner in the genitive",
    "Маши'на бра'та, кни'ги студе'нта",
    requires=["брат", "друг", "студент", "учитель", "директор"],
    cards=[
        card("The new case: the genitive",
             "The genitive is the most used case in Russian. It answers Кого'? and Чего'?, and one of its jobs "
             "is to show who owns something. English adds 's (Anton's bicycle) or uses “of”. Russian puts the "
             "thing first and the owner second, and puts the owner in the genitive: велосипе'д Анто'на. A "
             "masculine noun gets -а, or -я if it ends in -й or -ь.",
             tables=[table(
                 ["Nominative", "Genitive", "Ending"],
                 [["студе'нт", "студе'нт{а}", "-а"],
                  ["брат", "бра'т{а}", "-а"],
                  ["друг", "дру'г{а}", "-а"],
                  ["Анто'н", "Анто'н{а}", "-а"],
                  ["музе'й", "музе'{я}", "-я"],
                  ["учи'тель", "учи'тел{я}", "-я"],
                  ["Серге'й", "Серге'{я}", "-я"]],
                 note="Remember the consonant: no ending in the nominative of a hard masculine noun, so the genitive just adds -а.")]),
        card("The owner never changes its case",
             "No matter what case the thing owned is in, its owner stays in the genitive. In the first "
             "example the thing is the subject, in the second it is the object, and in the third it follows на.",
             tables=[table(
                 ["The thing is …", "Example"],
                 [["nominative", "Вот маши'на бра'та."],
                  ["accusative", "Я ви'жу маши'ну бра'та."],
                  ["prepositional", "Мы е'дем на маши'не бра'та."]])],
             examples=[
                 ex("Чей э'то велосипе'д? — Э'то велосипе'д Анто'на.", "Whose bicycle is this? — It's Anton's bicycle.", "Анто'на"),
                 ex("Чьи э'то кни'ги? — Э'то кни'ги преподава'теля.", "Whose books are these? — They are the teacher's books.", "преподава'теля"),
                 ex("Серге'й — дире'ктор музе'я.", "Sergei is the director of the museum.", "музе'я"),
                 ex("Я ви'жу дом дру'га.", "I see my friend's house.", "дру'га"),
             ]),
    ],
    verify=(vf("студент", "студента") + vf("брат", "брата") + vf("друг", "друга") + vf("музей", "музея")
            + vf("учитель", "учителя") + vf("преподаватель", "преподавателя") + vf("директор", "директора")
            + vf("велосипед", "велосипеда")),
    exercises=[
        fb("Чей э'то велосипе'д? — Э'то велосипе'д ___.", ["Анто'на", "Анто'н", "Анто'ну", "Анто'не"], "Анто'на",
           "The owner goes in the genitive: -а.", tr="Whose bicycle is this? — It's Anton's."),
        fb("Э'то кни'ги ___.", ["студе'нта", "студе'нт", "студе'нту", "студе'нте"], "студе'нта",
           "Genitive of a masculine noun: -а.", tr="These are the student's books.", lemma="студент"),
        fb("Вот маши'на ___.", ["бра'та", "брат", "бра'ту", "бра'те"], "бра'та",
           "Owner: genitive.", tr="Here is my brother's car.", lemma="брат"),
        fb("Я ви'жу дом ___.", ["дру'га", "друг", "дру'гу", "дру'ге"], "дру'га",
           "The owner stays genitive even after я ви'жу.", tr="I see my friend's house.", lemma="друг"),
        fb("Э'то кни'га ___.", ["учи'теля", "учи'тель", "учи'телю", "учи'теле"], "учи'теля",
           "Soft masculine: -я.", tr="This is the teacher's book.", lemma="учитель"),
        fb("Серге'й — дире'ктор ___.", ["музе'я", "музе'й", "музе'ю", "музе'е"], "музе'я",
           "Музе'й ends in -й, so the genitive ends in -я.", tr="Sergei is the director of the museum.", lemma="музей"),
        fb("Мы е'дем на маши'не ___.", ["бра'та", "бра'ту", "брат", "бра'те"], "бра'та",
           "The owner stays genitive after на + prepositional.", tr="We are going in my brother's car.", lemma="брат"),
        mc("In Russian, which comes first?", ["the thing owned, then the owner", "the owner, then the thing owned", "either order", "neither"],
           "the thing owned, then the owner", "Маши'на бра'та.", order=True),
        mc("Which case is the owner in?", ["genitive", "accusative", "prepositional", "nominative"], "genitive",
           "Бра'та, студе'нта.", order=True),
        mc("Which phrase means “the teacher's car”?",
           ["маши'на учи'теля", "учи'теля маши'на", "маши'на учи'тель", "маши'ны учи'теля"],
           "маши'на учи'теля", "Thing first, owner second."),
        mc("What happens to бра'та in Я ви'жу маши'ну бра'та?",
           ["It stays genitive", "It becomes accusative", "It becomes prepositional", "It disappears"],
           "It stays genitive", "Only the thing owned changes case."),
    ],
)

# ---------------------------------------------------------------------------- 79
L79 = lesson(
    "The genitive of feminine and neuter nouns",
    "Ко'мнаты, дере'вни, окна', мо'ря",
    requires=["комната", "деревня", "окно", "море", "здание"],
    cards=[
        card("Feminine: -ы or -и",
             "Feminine nouns drop their ending and add -ы (hard) or -и (soft). Nouns in -а become -ы. Nouns in "
             "-я, -ь and -ия become -и. Those in -ия end in two letters и: аудито'рия → аудито'рии.",
             tables=[table(
                 ["Nominative", "Genitive", "Ending"],
                 [["ко'мната", "ко'мнат{ы}", "-ы"],
                  ["шко'ла", "шко'л{ы}", "-ы"],
                  ["сестра'", "сестр{ы'}", "-ы"],
                  ["дере'вня", "дере'вн{и}", "-и"],
                  ["тетра'дь", "тетра'д{и}", "-и"],
                  ["аудито'рия", "аудито'ри{и}", "-и"]])]),
        card("Neuter: -а or -я",
             "Neuter nouns work like masculine ones. Nouns in -о become -а, and those in -е and -ие become -я. "
             "Note the stress, which often moves to the end: окно' → окна'. Then you can use the genitive to "
             "describe a noun as well as to show who owns it: магази'н о'буви (a shoe store), дире'ктор "
             "шко'лы (the school principal).",
             tables=[table(
                 ["Nominative", "Genitive", "Ending"],
                 [["окно'", "окн{а'}", "-а"],
                  ["письмо'", "письм{а'}", "-а"],
                  ["мо'ре", "мо'р{я}", "-я"],
                  ["зда'ние", "зда'ни{я}", "-я"]])],
             examples=[
                 ex("Вот окно' ко'мнаты.", "Here is the window of the room.", "ко'мнаты"),
                 ex("Э'то кни'га сестры'.", "This is my sister's book.", "сестры'"),
                 ex("Э'то шко'ла дере'вни.", "This is the village school.", "дере'вни"),
                 ex("Он рабо'тает в магази'не о'буви.", "He works in a shoe store.", "о'буви"),
                 ex("На стене' портре'т де'вушки.", "On the wall there is a portrait of a young woman.", "де'вушки"),
             ]),
    ],
    verify=(vf("комната", "комнаты") + vf("школа", "школы") + vf("сестра", "сестры") + vf("деревня", "деревни")
            + vf("тетрадь", "тетради") + vf("аудитория", "аудитории") + vf("окно", "окна") + vf("письмо", "письма")
            + vf("море", "моря") + vf("здание", "здания") + vf("обувь", "обуви") + vf("девушка", "девушки")),
    exercises=[
        fb("Вот окно' ___.", ["ко'мнаты", "ко'мната", "ко'мнату", "ко'мнате"], "ко'мнаты",
           "Hard feminine: -ы.", tr="Here is the window of the room.", lemma="комната"),
        fb("Э'то кни'га ___.", ["сестры'", "сестра'", "сестру'", "сестре'"], "сестры'",
           "Hard feminine: -ы.", tr="This is my sister's book.", lemma="сестра"),
        fb("Э'то шко'ла ___.", ["дере'вни", "дере'вня", "дере'вне", "дере'вню"], "дере'вни",
           "Soft feminine: -и.", tr="This is the village school.", lemma="деревня"),
        fb("Вот окно' ___.", ["зда'ния", "зда'ние", "зда'нии", "зда'нию"], "зда'ния",
           "Neuter in -ие: -ия.", tr="Here is the window of the building.", lemma="здание"),
        fb("Он рабо'тает в магази'не ___.", ["о'буви", "о'бувь", "о'бува", "о'бувы"], "о'буви",
           "Feminine in -ь: -и.", tr="He works in a shoe store.", lemma="обувь"),
        fb("Э'то дире'ктор ___.", ["шко'лы", "шко'ла", "шко'лу", "шко'ле"], "шко'лы",
           "Hard feminine: -ы.", tr="This is the school principal.", lemma="школа"),
        fb("Э'то бе'рег ___.", ["мо'ря", "мо'ре", "мо'рю", "мо'ри"], "мо'ря",
           "Neuter in -е: -я.", tr="This is the seashore.", lemma="море"),
        fb("На стене' портре'т ___.", ["де'вушки", "де'вушка", "де'вушку", "де'вушке"], "де'вушки",
           "Genitive of a feminine noun.", tr="On the wall there is a portrait of a young woman.", lemma="девушка"),
        mc("What is the genitive ending of hard feminine nouns like ко'мната?", ["-ы", "-и", "-а", "-у"], "-ы",
           "Ко'мнаты.", order=True),
        mc("What is the genitive ending of feminine nouns in -ь and -ия?", ["-и", "-ы", "-я", "-ю"], "-и",
           "Тетра'ди, аудито'рии.", order=True),
        mc("What is the genitive of окно'?", ["окна'", "окны'", "окни'", "окну'"], "окна'",
           "Neuter in -о: -а, and the stress moves."),
    ],
)

# ---------------------------------------------------------------------------- 80
L80 = lesson(
    "Genitive: spelling and special nouns",
    "Кни'ги, отца', дня, ма'тери, и'мени",
    requires=["отец", "день", "мать", "дочь", "имя"],
    cards=[
        card("The seven-letter rule",
             "After г, к, х, ж, ч, ш and щ you never write ы or я: only и and а. This is the rule from lesson "
             "25. In the genitive it affects feminine nouns: since -ы would follow a к or г, the ending is -и. "
             "Masculine nouns in these letters are not affected, since they already take -а: каранда'ш → "
             "карандаша', ключ → ключа'.",
             tables=[table(
                 ["Nominative", "Genitive"],
                 [["кни'га", "кни'г{и}"],
                  ["студе'нтка", "студе'нтк{и}"],
                  ["подру'га", "подру'г{и}"],
                  ["Ма'ша", "Ма'ш{и}"],
                  ["каранда'ш", "карандаш{а'}"],
                  ["ключ", "ключ{а'}"]])]),
        card("Nouns that change shape",
             "Some common words change inside. Nouns ending in -ец lose the е: оте'ц → отца', америка'нец → "
             "америка'нца. День loses its е too: день → дня. Мать and дочь add -ер-: ма'тери, до'чери. Neuter "
             "nouns in -мя add -ен-: и'мя → и'мени, вре'мя → вре'мени. Learn these as a set, since they will "
             "come back in other cases.",
             tables=[table(
                 ["Nominative", "Genitive"],
                 [["оте'ц", "отц{а'}"],
                  ["америка'нец", "америка'нц{а}"],
                  ["день", "д{ня}"],
                  ["мать", "ма'т{ери}"],
                  ["дочь", "до'ч{ери}"],
                  ["и'мя", "и'м{ени}"],
                  ["вре'мя", "вре'м{ени}"]])],
             examples=[
                 ex("Э'то кни'га студе'нтки.", "This is the student's book.", "студе'нтки"),
                 ex("Э'то маши'на отца'.", "This is my father's car.", "отца'"),
                 ex("Вот маши'на ма'тери.", "Here is my mother's car.", "ма'тери"),
                 ex("И'мя до'чери — А'нна.", "My daughter's name is Anna.", "до'чери"),
                 ex("Э'то коне'ц дня.", "This is the end of the day.", "дня"),
             ]),
    ],
    verify=(vf("книга", "книги") + vf("подруга", "подруги")
            + vf("карандаш", "карандаша") + vf("ключ", "ключа") + vf("отец", "отца") + vf("американец", "американца")
            + vf("день", "дня") + vf("мать", "матери") + vf("дочь", "дочери") + vf("имя", "имени")
            + vf("время", "времени") + vf("конец", "конца")),
    exercises=[
        fb("Э'то кни'га ___.", ["студе'нтки", "студе'нтка", "студе'нткы", "студе'нтку"], "студе'нтки",
           "After к the ending is -и, never -ы.", tr="This is the student's book."),
        fb("Вот кни'га ___.", ["подру'ги", "подру'га", "подру'гы", "подру'гу"], "подру'ги",
           "After г the ending is -и.", tr="Here is my friend's book.", lemma="подруга"),
        fb("Э'то маши'на ___.", ["отца'", "оте'ц", "отцу'", "отце'"], "отца'",
           "The е drops out of оте'ц.", tr="This is my father's car.", lemma="отец"),
        fb("Я ви'жу дом ___.", ["америка'нца", "америка'нец", "америка'нцу", "америка'нце"], "америка'нца",
           "The е drops out of -ец.", tr="I see the American's house.", lemma="американец"),
        fb("Э'то коне'ц ___.", ["дня", "день", "дню", "дне"], "дня",
           "День loses its е.", tr="This is the end of the day.", lemma="день"),
        fb("Вот маши'на ___.", ["ма'тери", "мать", "ма'тер", "ма'терь"], "ма'тери",
           "Мать adds -ер-.", tr="Here is my mother's car.", lemma="мать"),
        fb("И'мя ___ — А'нна.", ["до'чери", "дочь", "до'чер", "до'чере"], "до'чери",
           "Дочь adds -ер-.", tr="My daughter's name is Anna.", lemma="дочь"),
        mc("What is the genitive of и'мя?", ["и'мени", "и'ма", "и'мя", "и'меню"], "и'мени",
           "Neuter nouns in -мя add -ен-."),
        mc("After which letters do you never write ы or я?", ["к г х ж ч ш щ", "б в д з", "а о у э", "п т ф с"], "к г х ж ч ш щ",
           "The seven-letter rule.", order=True),
        mc("What happens to the е in оте'ц when you add an ending?", ["It drops out", "It becomes ё", "It stays", "It becomes и"],
           "It drops out", "Оте'ц → отца'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 81
L81 = lesson(
    "Before, after, from: до, по'сле, из",
    "До ве'чера, по'сле уро'ка, из шко'лы",
    requires=["до", "после", "из", "вечер", "урок"],
    cards=[
        card("Three prepositions, one case",
             "До (before, until), по'сле (after) and из (from, out of) are always followed by the genitive. "
             "Из is also the preposition for where you come from: Я из Росси'и. It is the opposite of в. If you "
             "go в шко'лу you come back из шко'лы.",
             tables=[table(
                 ["Preposition", "Meaning", "Example"],
                 [["до", "before, until", "до обе'да · до ве'чера"],
                  ["по'сле", "after", "по'сле за'втрака · по'сле суббо'ты"],
                  ["из", "from, out of", "из шко'лы · из Москвы' · из Росси'и"]])],
             examples=[
                 ex("Я де'лал дома'шнюю рабо'ту до ве'чера.", "I did my homework until the evening.", "до ве'чера"),
                 ex("По'сле суббо'ты идёт воскресе'нье.", "After Saturday comes Sunday.", "По'сле суббо'ты"),
                 ex("По'сле уро'ка мы идём домо'й.", "After the lesson we go home.", "По'сле уро'ка"),
                 ex("Мой муж из Теха'са.", "My husband is from Texas.", "из Теха'са"),
                 ex("Я из Герма'нии, а моя' жена' из Росси'и.", "I'm from Germany, and my wife is from Russia.", "из Герма'нии"),
             ]),
    ],
    verify=(vf("вечер", "вечера") + vf("урок", "урока") + vf("суббота", "субботы") + vf("школа", "школы")
            + vf("завтрак", "завтрака") + vf("обед", "обеда") + vf("Москва", "Москвы") + vf("Россия", "России")
            + vf("Германия", "Германии")),
    exercises=[
        fb("Он рабо'тал до ___.", ["ве'чера", "ве'чер", "ве'черу", "ве'чере"], "ве'чера",
           "До + genitive.", tr="He worked until the evening.", lemma="вечер"),
        fb("По'сле ___ мы идём домо'й.", ["уро'ка", "уро'к", "уро'ку", "уро'ке"], "уро'ка",
           "По'сле + genitive.", tr="After the lesson we go home.", lemma="урок"),
        fb("Моя' жена' из ___.", ["Росси'и", "Росси'я", "Росси'ю", "Росси'е"], "Росси'и",
           "Из + genitive; -ия → -ии.", tr="My wife is from Russia.", lemma="россия"),
        fb("Мы идём из ___.", ["шко'лы", "шко'ла", "шко'лу", "шко'ле"], "шко'лы",
           "Из + genitive.", tr="We are coming from school.", lemma="школа"),
        fb("По'сле ___ идёт воскресе'нье.", ["суббо'ты", "суббо'та", "суббо'ту", "суббо'те"], "суббо'ты",
           "По'сле + genitive.", tr="Sunday comes after Saturday.", lemma="суббота"),
        fb("Мой друг из ___.", ["Москвы'", "Москва'", "Москву'", "Москве'"], "Москвы'",
           "Из + genitive.", tr="My friend is from Moscow.", lemma="москва"),
        fb("До ___ я чита'ю.", ["за'втрака", "за'втрак", "за'втраку", "за'втраке"], "за'втрака",
           "До + genitive.", tr="Before breakfast I read.", lemma="завтрак"),
        mc("Which case follows до, по'сле and из?", ["genitive", "accusative", "prepositional", "nominative"], "genitive",
           "All three take the genitive.", order=True),
        mc("Which preposition is the opposite of в?", ["из", "до", "по'сле", "у"], "из",
           "В шко'лу — из шко'лы.", order=True),
        mc("Which phrase means “after the lesson”?",
           ["по'сле уро'ка", "по'сле уро'к", "по'сле уро'ке", "по'сле уро'ку"], "по'сле уро'ка",
           "По'сле + genitive."),
    ],
)

# ---------------------------------------------------------------------------- 82
L82 = lesson(
    "Thirty to a thousand",
    "Три'дцать, со'рок, пятьдеся'т … сто, две'сти, ты'сяча",
    requires=["тысяча", "рубль", "час", "день", "год"],
    cards=[
        card("The tens and the hundred",
             "From 50 to 80 the tens are built as “five tens”, “six tens” and so on, and each has a soft sign "
             "in the middle: пятьдеся'т, шестьдеся'т, се'мьдесят, во'семьдесят. The numbers 40, 90 and 100 are "
             "separate words that have to be learned: со'рок, девяно'сто, сто. Thirty is three + дцать. To "
             "build a number such as 35 or 47, say the tens first and the units second.",
             tables=[table(
                 ["Number", "Cardinal", "Ordinal"],
                 [["30", "три'дцать", "тридца'тый"],
                  ["40", "со'рок", "сороково'й"],
                  ["50", "пятьдеся'т", "пятидеся'тый"],
                  ["60", "шестьдеся'т", "шестидеся'тый"],
                  ["70", "се'мьдесят", "семидеся'тый"],
                  ["80", "во'семьдесят", "восьмидеся'тый"],
                  ["90", "девяно'сто", "девяно'стый"],
                  ["100", "сто", "со'тый"],
                  ["1000", "ты'сяча", "ты'сячный"]],
                 note="In a compound ordinal only the last word is an ordinal: шестьдеся'т восьмо'й (68th).")]),
        card("Hundreds and building bigger numbers",
             "The hundreds from 200 to 400 are two and three words glued together: две'сти, три'ста, "
             "четы'реста. Put the larger part first: два'дцать оди'н, со'рок пять, сто три'дцать. The "
             "time-telling rules from lesson 62 still decide the form of мину'та and час: со'рок одна' "
             "мину'та, пятьдеся'т пять мину'т.",
             tables=[table(
                 ["Number", "Word"],
                 [["100", "сто"],
                  ["200", "две'сти"],
                  ["300", "три'ста"],
                  ["400", "четы'реста"],
                  ["1000", "ты'сяча"]])],
             examples=[
                 ex("Сейча'с пятьдеся'т пять мину'т.", "It is fifty-five minutes now.", "пятьдеся'т пять"),
                 ex("Э'то восьмидеся'тая доро'га.", "This is the eightieth road.", "восьмидеся'тая"),
                 ex("Мы бы'ли там со'рок мину'т.", "We were there for forty minutes.", "со'рок"),
                 ex("Э'то наш ты'сячный покупа'тель!", "This is our thousandth customer!", "ты'сячный"),
             ]),
    ],
    verify=(vf("тридцать", "тридцать") + vf("сорок", "сорок") + vf("пятьдесят", "пятьдесят")
            + vf("шестьдесят", "шестьдесят") + vf("семьдесят", "семьдесят") + vf("восемьдесят", "восемьдесят")
            + vf("девяносто", "девяносто") + vf("сто", "сто") + vf("двести", "двести") + vf("триста", "триста")
            + vf("четыреста", "четыреста") + vf("тысяча", "тысяча") + vf("тридцатый", "тридцатый")
            + vf("сороковой", "сороковой") + vf("пятидесятый", "пятидесятый") + vf("шестидесятый", "шестидесятый")
            + vf("семидесятый", "семидесятый") + vf("восьмидесятый", "восьмидесятый")
            + vf("девяностый", "девяностый") + vf("сотый", "сотый") + vf("тысячный", "тысячный")),
    exercises=[
        fb("Два'дцать и де'сять — э'то ___.", ["три'дцать", "со'рок", "пятьдеся'т", "два'дцать"], "три'дцать",
           "20 + 10 = 30.", tr="Twenty and ten is thirty."),
        fb("Три'дцать и три'дцать — э'то ___.", ["шестьдеся'т", "пятьдеся'т", "се'мьдесят", "со'рок"], "шестьдеся'т",
           "30 + 30 = 60.", tr="Thirty and thirty is sixty."),
        fb("Со'рок и со'рок — э'то ___.", ["во'семьдесят", "се'мьдесят", "девяно'сто", "шестьдеся'т"], "во'семьдесят",
           "40 + 40 = 80.", tr="Forty and forty is eighty."),
        fb("Пятьдеся'т и пятьдеся'т — э'то ___.", ["сто", "девяно'сто", "две'сти", "ты'сяча"], "сто",
           "50 + 50 = 100.", tr="Fifty and fifty is a hundred."),
        fb("Сто и сто — э'то ___.", ["две'сти", "три'ста", "сто", "четы'реста"], "две'сти",
           "100 + 100 = 200.", tr="A hundred and a hundred is two hundred."),
        fb("Э'то ___ страни'ца. (80th)", ["восьмидеся'тая", "восьмидеся'тый", "восьмидеся'тое", "во'семьдесят"], "восьмидеся'тая",
           "Страни'ца is feminine.", tr="This is the eightieth page."),
        fb("Э'то ___ уро'к. (40th)", ["сороково'й", "со'рок", "сороково'я", "сороково'е"], "сороково'й",
           "Уро'к is masculine.", tr="This is the fortieth lesson."),
        mc("Which number is 90?", ["девяно'сто", "девятна'дцать", "девяно'ста", "во'семьдесят"], "девяно'сто",
           "Девяно'сто."),
        mc("Which number is 40?", ["со'рок", "четы'ресто", "четы'рдесят", "сороково'й"], "со'рок",
           "Со'рок is a separate word."),
        mc("How do you say 21?", ["два'дцать оди'н", "оди'н два'дцать", "два'дцать и оди'н", "оди'н и два'дцать"], "два'дцать оди'н",
           "Tens first, then units.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 83
L83 = lesson(
    "Review: reflexive verbs, the genitive and numbers",
    "Putting lessons 75 to 82 together",
    requires=["учиться", "брат", "мать", "до", "тысяча"],
    cards=[
        card("What you can do now",
             "You can use -ся and -сь, tell a verb that acts on its subject from one that acts on someone "
             "else, conjugate учи'ться, mark an owner with the genitive, form the genitive of masculine, "
             "feminine and neuter nouns (including the special ones), use до, по'сле and из, and count in "
             "tens up to a thousand.",
             tables=[table(
                 ["Topic", "Remember"],
                 [["Reflexive", "-ся after a consonant, -сь after a vowel"],
                  ["Genitive, masculine", "студе'нта · музе'я"],
                  ["Genitive, feminine", "ко'мнаты · дере'вни · тетра'ди"],
                  ["Genitive, neuter", "окна' · мо'ря · зда'ния"],
                  ["Special", "отца' · дня · ма'тери · и'мени"],
                  ["Prepositions", "до, по'сле, из + genitive"]])],
             examples=[
                 ex("По'сле уро'ка ма'льчик одева'ется и идёт в магази'н.", "After the lesson the boy gets dressed and goes to the store.", "одева'ется"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("Мы ___ в институ'те.", ["у'чимся", "учу'сь", "у'чится", "у'чатся"], "у'чимся",
           "Мы takes -имся.", tr="We study at the institute.", lemma="учиться"),
        fb("Магази'н ___ в де'вять часо'в.", ["открыва'ется", "открыва'ет", "открыва'ются", "открыва'ешь"], "открыва'ется",
           "The store is the subject: -ется.", tr="The store opens at nine.", lemma="открываться"),
        fb("Де'вочка ___.", ["умыва'ется", "умыва'ет", "умыва'ются", "умыва'юсь"], "умыва'ется",
           "She washes herself: -ется.", tr="The girl is washing her face.", lemma="умываться"),
        fb("Э'то маши'на ___.", ["бра'та", "брат", "бра'ту", "бра'те"], "бра'та",
           "Owner: genitive.", tr="This is my brother's car.", lemma="брат"),
        fb("Э'то кни'га ___.", ["сестры'", "сестра'", "сестру'", "сестре'"], "сестры'",
           "Feminine: -ы.", tr="This is my sister's book.", lemma="сестра"),
        fb("Вот окно' ___.", ["ко'мнаты", "ко'мната", "ко'мнату", "ко'мнате"], "ко'мнаты",
           "Feminine: -ы.", tr="Here is the window of the room.", lemma="комната"),
        fb("Вот маши'на ___.", ["ма'тери", "мать", "ма'тер", "ма'терь"], "ма'тери",
           "Мать adds -ер-.", tr="Here is my mother's car.", lemma="мать"),
        fb("Мой друг из ___.", ["Москвы'", "Москва'", "Москву'", "Москве'"], "Москвы'",
           "Из + genitive.", tr="My friend is from Moscow.", lemma="москва"),
        fb("По'сле ___ мы идём домо'й.", ["уро'ка", "уро'к", "уро'ку", "уро'ке"], "уро'ка",
           "По'сле + genitive.", tr="After the lesson we go home.", lemma="урок"),
        fb("Пятьдеся'т и пятьдеся'т — э'то ___.", ["сто", "девяно'сто", "две'сти", "ты'сяча"], "сто",
           "50 + 50 = 100.", tr="Fifty and fifty is a hundred."),
        mc("Which sentence means “He is shaving”?", ["Он бре'ется.", "Он бре'ет.", "Он бре'юсь.", "Они' бре'ется."], "Он бре'ется.",
           "Never drop -ся."),
        mc("What is the genitive of оте'ц?", ["отца'", "оте'ца", "отцу'", "оте'ц"], "отца'",
           "The е drops out."),
    ],
)

UNIT = unit("Unit 11: Reflexive verbs, the genitive and numbers",
            [L75, L76, L77, L78, L79, L80, L81, L82, L83])
