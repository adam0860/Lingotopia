"""Unit 29: crime and justice vocabulary; verbal adverbs; case conflicts and the
buffer word то (textbook module 7, lesson 38)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 286
L286 = lesson(
    "Crimes and criminals: преступле'ние, вор, моше'нник, граби'тель",
    "Вор укра'л су'мку, а моше'нник — де'ньги.",
    requires=["преступление", "преступник", "вор", "убийство", "кража"],
    cards=[
        card("People and crimes",
             "Words for those who commit crimes and for the crimes themselves.",
             tables=[table(
                 ["Word", "English"],
                 [["преступле'ние", "crime, offense"],
                  ["престу'пник", "criminal"],
                  ["престу'пность (f.)", "crime (as a social problem)"],
                  ["вор", "thief"],
                  ["граби'тель (m.)", "robber"],
                  ["моше'нник", "swindler, con artist"],
                  ["уби'йца", "murderer"],
                  ["злоумы'шленник", "culprit, offender"],
                  ["соуча'стник", "accomplice"],
                  ["кра'жа", "theft"],
                  ["ограбле'ние", "robbery, burglary"],
                  ["уби'йство", "murder"]])],
             examples=[
                 ex("Вор укра'л су'мку, а моше'нник — де'ньги.", "The thief stole a bag, and the swindler stole money.", "Вор"),
                 ex("Моше'нник обману'л пенсионе'ра.", "A swindler deceived a pensioner.", "Моше'нник"),
                 ex("Поли'ция и'щет престу'пников.", "The police are looking for the criminals.", "престу'пников"),
             ]),
        card("Verbs and their nouns",
             "Many crime nouns are connected to verbs you can recognize.",
             tables=[table(
                 ["Verb", "Noun", "English"],
                 [["красть / укра'сть", "кра'жа", "to steal / theft"],
                  ["гра'бить / огра'бить", "ограбле'ние", "to rob / robbery"],
                  ["похища'ть / похи'тить", "похище'ние", "to abduct / abduction"],
                  ["соверша'ть / соверши'ть", "—", "to commit (a crime)"]])],
             examples=[
                 ex("У него' укра'ли телефо'н.", "His phone was stolen.", "укра'ли"),
                 ex("Банк огра'били но'чью.", "The bank was robbed at night.", "огра'били"),
             ]),
        card("Forms to know",
             "Вор and the nouns in -ец, -ель and -ник have a few irregular forms.",
             tables=[table(
                 ["Singular", "Plural"],
                 [["вор", "во'ры, воро'в, вора'м"],
                  ["граби'тель", "граби'тели, граби'телей"],
                  ["уби'йца (m. or f.)", "уби'йцы, уби'йц"]])],
             examples=[
                 ex("В магази'не бы'ли дво'е воро'в.", "There were two thieves in the shop.", "дво'е воро'в"),
             ]),
    ],
    verify=(vf("преступление", "преступление") + vf("преступник", "преступников") + vf("преступность", "преступность")
            + vf("вор", "воров") + vf("грабитель", "грабитель") + vf("мошенник", "мошенник") + vf("убийца", "убийца")
            + vf("злоумышленник", "злоумышленник") + vf("соучастник", "соучастник") + vf("кража", "кража")
            + vf("ограбление", "ограбление") + vf("убийство", "убийство") + vf("красть", "красть")
            + vf("украсть", "украл", "украли") + vf("грабить", "грабить") + vf("ограбить", "ограбили")
            + vf("похищать", "похищать") + vf("похитить", "похитить") + vf("похищение", "похищение")
            + vf("сумка", "сумку") + vf("обмануть", "обманул") + vf("пенсионер", "пенсионера") + vf("искать", "ищет")
            + vf("банк", "банк") + vf("телефон", "телефон") + vf("совершать", "совершать") + vf("совершить", "совершить")),
    exercises=[
        F("Вор укра'л мою' ___. (bag)", "су'мку", ["су'мка", "су'мки", "су'мке"], "Accusative object.", "The thief stole my bag.", lemma="сумка"),
        F("Моше'нник обману'л ___. (a pensioner)", "пенсионе'ра", ["пенсионе'р", "пенсионе'ру", "пенсионе'ром"], "Animate accusative = genitive.", "The swindler deceived a pensioner.", lemma="пенсионер"),
        F("Поли'ция и'щет ___. (the criminals)", "престу'пников", ["престу'пники", "престу'пникам", "престу'пниками"], "Animate accusative plural = genitive.", "The police are looking for the criminals.", lemma="преступник"),
        F("В магази'не бы'ли дво'е ___. (thieves)", "воро'в", ["во'ры", "вора'м", "вора'ми"], "Collective numeral + genitive plural.", "There were two thieves in the shop."),
        F("У него' ___ телефо'н. (stole, 'they')", "укра'ли", ["укра'л", "укра'сть", "кра'дут"], "Indefinite-personal plural past.", "His phone was stolen."),
        mc("Who takes money by deceiving people?", ["моше'нник", "граби'тель", "уби'йца", "свиде'тель"], "моше'нник", "Моше'нник = swindler.", order=True),
        mc("What is кра'жа?", ["theft", "robbery", "murder", "fraud"], "theft", "Кра'жа ← красть.", order=True),
        mc("Which word means ‘accomplice’?", ["соуча'стник", "злоумы'шленник", "свиде'тель", "судья'"], "соуча'стник", "Соуча'стник.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 287
L287 = lesson(
    "Police and investigation: поли'ция, сле'дователь, о'быск, свиде'тель",
    "Сле'дователь допроси'л свиде'теля.",
    requires=["полиция", "следователь", "расследование", "свидетель", "обыск"],
    cards=[
        card("Who and what",
             "The people and procedures of an investigation.",
             tables=[table(
                 ["Word", "English"],
                 [["поли'ция", "police"],
                  ["полице'йский", "police officer"],
                  ["сле'дователь (m.)", "investigator"],
                  ["рассле'дование", "investigation"],
                  ["прокурату'ра", "public prosecutor's office"],
                  ["уголо'вный ро'зыск", "criminal investigation department"],
                  ["свиде'тель / очеви'дец", "witness / eyewitness"],
                  ["подозрева'емый", "suspect"],
                  ["заде'ржанный", "detainee"],
                  ["доказа'тельство, ули'ка", "proof, evidence; clue"],
                  ["о'быск", "search (of a person or premises)"],
                  ["ро'зыск", "wanted search, manhunt"],
                  ["ли'чность (f.)", "identity"]])],
             examples=[
                 ex("Полице'йские провели' о'быск в кварти'ре.", "The police carried out a search in the apartment.", "о'быск"),
                 ex("Очеви'дцы рассказа'ли о происше'ствии.", "The eyewitnesses told about the incident.", "Очеви'дцы"),
             ]),
        card("Verbs",
             "Typical verbs in a police report.",
             tables=[table(
                 ["Verb", "English"],
                 [["задержа'ть / заде'рживать", "to detain"],
                  ["аресто'вывать / арестова'ть", "to arrest"],
                  ["допра'шивать / допроси'ть", "to interrogate, question"],
                  ["обнару'живать / обнару'жить", "to discover, find"],
                  ["устана'вливать / установи'ть ли'чность", "to establish the identity"],
                  ["объяви'ть в ро'зыск", "to put on the wanted list"],
                  ["возбуди'ть уголо'вное де'ло", "to open a criminal case"],
                  ["раскры'ть преступле'ние", "to solve a crime"]])],
             examples=[
                 ex("Сле'дователь допроси'л свиде'теля.", "The investigator questioned the witness.", "допроси'л"),
                 ex("Подозрева'емого задержа'ли вчера'.", "The suspect was detained yesterday.", "задержа'ли"),
             ]),
        card("A short report",
             "Typical sentences in a news item about a theft.",
             examples=[
                 ex("Поли'ция установи'ла ли'чность вора'.", "The police established the thief's identity.", "установи'ла ли'чность"),
                 ex("Его' объяви'ли в ро'зыск.", "He was put on the wanted list.", "в ро'зыск"),
                 ex("Сле'дователь возбуди'л уголо'вное де'ло.", "The investigator opened a criminal case.", "уголо'вное де'ло"),
             ]),
    ],
    verify=(vf("полиция", "полиция") + vf("полицейский", "полицейские") + vf("следователь", "следователь") + vf("расследование", "расследование")
            + vf("прокуратура", "прокуратура") + vf("свидетель", "свидетеля") + vf("очевидец", "очевидцы")
            + vf("подозреваемый", "подозреваемого") + vf("доказательство", "доказательство") + vf("улика", "улика")
            + vf("обыск", "обыск") + vf("розыск", "розыск") + vf("личность", "личность")
            + vf("задержать", "задержали") + vf("арестовать", "арестовать") + vf("допросить", "допросил")
            + vf("обнаружить", "обнаружить") + vf("установить", "установила") + vf("объявить", "объявили")
            + vf("возбудить", "возбудил") + vf("раскрыть", "раскрыть") + vf("уголовный", "уголовное")
            + vf("квартира", "квартире") + vf("происшествие", "происшествии") + vf("рассказать", "рассказали")),
    exercises=[
        F("Полице'йские провели' ___ в кварти'ре. (a search)", "о'быск", ["о'быска", "о'быску", "о'быске"], "Accusative = nominative.", "The police carried out a search in the apartment.", lemma="обыск"),
        F("Сле'дователь допроси'л ___. (the witness)", "свиде'теля", ["свиде'тель", "свиде'телю", "свиде'телем"], "Animate accusative = genitive.", "The investigator questioned the witness.", lemma="свидетель"),
        F("Подозрева'емого ___ вчера'. (was detained)", "задержа'ли", ["задержа'ть", "задержа'л", "задержа'ла"], "Indefinite-personal plural past.", "The suspect was detained yesterday."),
        F("Поли'ция ___ ли'чность вора'. (established)", "установи'ла", ["установи'л", "установи'ло", "установи'ли"], "Поли'ция is feminine singular.", "The police established the thief's identity."),
        F("Его' объяви'ли в ___. (the wanted list)", "ро'зыск", ["ро'зыска", "ро'зыску", "ро'зыске"], "В + accusative.", "He was put on the wanted list.", lemma="розыск"),
        F("Сле'дователь возбуди'л уголо'вное ___. (case)", "де'ло", ["де'ла", "де'лу", "де'ле"], "Accusative = nominative.", "The investigator opened a criminal case."),
        mc("Who saw the crime happen?", ["очеви'дец", "сле'дователь", "судья'", "адвока'т"], "очеви'дец", "Очеви'дец = eyewitness.", order=True),
        mc("What does ро'зыск mean?", ["a search for a wanted person", "a verdict", "a punishment", "a witness"], "a search for a wanted person", "Ро'зыск.", order=True),
        mc("What does обнару'жить mean?", ["to discover", "to arrest", "to steal", "to sentence"], "to discover", "Обнару'жить.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 288
L288 = lesson(
    "In court: суд, судья', адвока'т, пригово'р, срок, штраф",
    "Суд вы'нес пригово'р: три го'да лише'ния свобо'ды.",
    requires=["суд", "судья", "адвокат", "приговор", "срок"],
    cards=[
        card("Court and verdict",
             "Суд has end stress in every case: суда', суду', судо'м. Судья' can be a man or a woman.",
             tables=[table(
                 ["Word", "English"],
                 [["суд", "court"],
                  ["судья' (m. or f.)", "judge"],
                  ["адвока'т", "lawyer, attorney"],
                  ["обвине'ние", "charge, accusation"],
                  ["обвиня'емый / подсуди'мый", "the accused, the defendant"],
                  ["вина'", "guilt"],
                  ["пригово'р", "verdict, sentence"],
                  ["срок", "term (of a sentence)"]])],
             examples=[
                 ex("Суд вы'нес пригово'р.", "The court passed sentence.", "вы'нес пригово'р"),
                 ex("Адвока'т защища'ет подсуди'мого.", "The lawyer defends the defendant.", "подсуди'мого"),
                 ex("Подсуди'мый призна'л свою' вину'.", "The defendant admitted his guilt.", "призна'л свою' вину'"),
             ]),
        card("Punishments",
             "Words for what a court can decide.",
             tables=[table(
                 ["Word", "English"],
                 [["штраф", "fine"],
                  ["усло'вный срок", "suspended sentence, probation"],
                  ["лише'ние свобо'ды", "imprisonment (lit., deprivation of freedom)"],
                  ["тюре'мное заключе'ние", "prison sentence"],
                  ["тюрьма'", "prison"],
                  ["за решёткой", "behind bars"]])],
             examples=[
                 ex("Суд назна'чил ему' штраф.", "The court imposed a fine on him.", "штраф"),
                 ex("Престу'пника посади'ли в тюрьму'.", "The criminal was put in prison.", "в тюрьму'"),
                 ex("Он получи'л усло'вный срок.", "He received a suspended sentence.", "усло'вный срок"),
             ]),
        card("Useful set phrases",
             "A few collocations you will often meet.",
             tables=[table(
                 ["Phrase", "English"],
                 [["вы'нести пригово'р (+ Dat.)", "to pass sentence on"],
                  ["призна'ть вину'", "to admit guilt"],
                  ["назна'чить штраф", "to impose a fine"],
                  ["посади'ть в тюрьму'", "to send to prison"]])],
             examples=[
                 ex("Суд вы'нес ему' пригово'р.", "The court passed sentence on him.", "ему'"),
             ]),
    ],
    verify=(vf("суд", "суд", "суда") + vf("судья", "судья") + vf("адвокат", "адвокат") + vf("обвинение", "обвинение")
            + vf("подсудимый", "подсудимого") + vf("вина", "вину") + vf("приговор", "приговор") + vf("срок", "срок")
            + vf("штраф", "штраф") + vf("условный", "условный") + vf("лишение", "лишения") + vf("свобода", "свободы")
            + vf("заключение", "заключение") + vf("тюрьма", "тюрьму") + vf("решётка", "решёткой")
            + vf("вынести", "вынес") + vf("признать", "признал") + vf("назначить", "назначил") + vf("посадить", "посадили")
            + vf("защищать", "защищает") + vf("получить", "получил") + vf("год", "года")),
    exercises=[
        F("Суд назна'чил ему' ___. (a fine)", "штраф", ["штра'фа", "штра'фу", "штра'фом"], "Accusative = nominative.", "The court imposed a fine on him.", lemma="штраф"),
        F("Суд вы'нес ___. (sentence)", "пригово'р", ["пригово'ра", "пригово'ру", "пригово'ре"], "Accusative = nominative.", "The court passed sentence.", lemma="приговор"),
        F("Престу'пника посади'ли в ___. (prison)", "тюрьму'", ["тюрьма'", "тюрьмы'", "тюрьме'"], "В + accusative: where to?", "The criminal was put in prison.", lemma="тюрьма"),
        F("Подсуди'мый призна'л свою' ___. (guilt)", "вину'", ["вина'", "вины'", "вине'"], "Accusative feminine.", "The defendant admitted his guilt.", lemma="вина"),
        F("Адвока'т защища'ет ___. (the defendant)", "подсуди'мого", ["подсуди'мый", "подсуди'мому", "подсуди'мым"], "Animate accusative = genitive.", "The lawyer defends the defendant."),
        F("Он получи'л усло'вный ___. (suspended sentence)", "срок", ["сро'ка", "сро'ку", "сро'ке"], "Accusative = nominative.", "He received a suspended sentence."),
        mc("Which punishment is a money penalty?", ["штраф", "тюрьма'", "пригово'р", "вина'"], "штраф", "Штраф = fine.", order=True),
        mc("What is ‘лише'ние свобо'ды’?", ["imprisonment", "a fine", "an acquittal", "a witness"], "imprisonment", "Deprivation of freedom.", order=True),
        mc("Судья' can be:", ["masculine or feminine", "only masculine", "only feminine", "plural only"], "masculine or feminine", "Судья' is like an ordinary -я noun but names a person of either sex.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 289
L289 = lesson(
    "Accuse, suspect, sentence: обвиня'ть в, подозрева'ть в, приговори'ть к",
    "Его' обвиня'ют в кра'же, но он не признаёт вину'.",
    requires=["обвинить", "подозревать", "доказать", "нарушить", "украсть"],
    cards=[
        card("Verbs with prepositions",
             "Verbs of crime and justice have fixed patterns. Learn the preposition and the case together.",
             tables=[table(
                 ["Verb", "Pattern", "Example"],
                 [["обвиня'ть кого' в чём", "в + Prep.", "обвиня'ть в кра'же"],
                  ["подозрева'ть кого' в чём", "в + Prep.", "подозрева'ть в уби'йстве"],
                  ["приговори'ть кого' к чему'", "к + Dat.", "приговори'ть к штра'фу"],
                  ["лиша'ть / лиши'ть кого' чего'", "Gen.", "лиши'ть свобо'ды"],
                  ["наруша'ть / нару'шить что", "Acc.", "нару'шить зако'н"],
                  ["доказа'ть что", "Acc.", "доказа'ть вину'"]])],
             examples=[
                 ex("Его' обвиня'ют в кра'же.", "He is accused of theft.", "в кра'же"),
                 ex("Мужчи'ну подозрева'ют в уби'йстве.", "The man is suspected of murder.", "в уби'йстве"),
                 ex("Суд приговори'л его' к штра'фу.", "The court sentenced him to a fine.", "к штра'фу"),
             ]),
        card("Nouns and adjectives with the same pattern",
             "The nouns and adjectives from these verbs keep the preposition.",
             tables=[table(
                 ["Word", "Pattern"],
                 [["обвине'ние в чём", "в + Prep."],
                  ["подозре'ние в чём", "в + Prep."],
                  ["вино'вный в чём", "в + Prep."],
                  ["прича'стный к чему'", "к + Dat."]])],
             examples=[
                 ex("Ему' предъяви'ли обвине'ние в кра'же.", "He was charged with theft.", "обвине'ние в кра'же"),
                 ex("Суд приговори'л вора' к трём года'м заключе'ния.", "The court sentenced the thief to three years of imprisonment.", "к трём года'м"),
             ]),
        card("Aspect pairs",
             "Most of the verbs come in pairs.",
             tables=[table(
                 ["Imperfective", "Perfective"],
                 [["обвиня'ть", "обвини'ть"],
                  ["дока'зывать", "доказа'ть"],
                  ["красть", "укра'сть"],
                  ["наруша'ть", "нару'шить"]])],
             examples=[
                 ex("Он нару'шил зако'н.", "He broke the law.", "нару'шил"),
             ]),
    ],
    verify=(vf("обвинять", "обвиняют") + vf("обвинить", "обвинить") + vf("подозревать", "подозревают") + vf("приговорить", "приговорил")
            + vf("лишать", "лишать") + vf("лишить", "лишить") + vf("нарушать", "нарушать") + vf("нарушить", "нарушил")
            + vf("доказать", "доказать") + vf("кража", "краже") + vf("убийство", "убийстве") + vf("штраф", "штрафу")
            + vf("свобода", "свободы") + vf("закон", "закон") + vf("вина", "вину") + vf("признавать", "признаёт")
            + vf("обвинение", "обвинение") + vf("подозрение", "подозрение") + vf("предъявить", "предъявили")
            + vf("год", "годам") + vf("мужчина", "мужчину") + vf("вор", "вора") + vf("заключение", "заключения")),
    exercises=[
        F("Его' обвиня'ют ___ кра'же. (of)", "в", ["на", "за", "к"], "Обвиня'ть в + prepositional.", "He is accused of theft."),
        F("Мужчи'ну подозрева'ют ___ уби'йстве. (of)", "в", ["о", "на", "за"], "Подозрева'ть в + prepositional.", "The man is suspected of murder."),
        F("Суд приговори'л его' ___ штра'фу. (to)", "к", ["в", "на", "за"], "Приговори'ть к + dative.", "The court sentenced him to a fine."),
        F("Его' обвиня'ют в ___. (a theft)", "кра'же", ["кра'жа", "кра'жу", "кра'жей"], "В + prepositional.", "He is accused of theft.", lemma="кража"),
        F("Суд приговори'л вора' к трём ___ заключе'ния. (years)", "года'м", ["го'да", "годо'в", "года'ми"], "К + dative plural.", "The court sentenced the thief to three years of imprisonment.", lemma="год"),
        F("Престу'пник ___ вину'. (admitted)", "призна'л", ["призна'ла", "призна'ло", "призна'ли"], "Masculine past.", "The criminal admitted his guilt."),
        F("Он нару'шил ___. (the law)", "зако'н", ["зако'на", "зако'ну", "зако'ном"], "Accusative = nominative.", "He broke the law.", lemma="закон"),
        mc("Which preposition goes with подозрева'ть?", ["в", "к", "о", "на"], "в", "Подозрева'ть в чём.", order=True),
        mc("‘Лиши'ть свобо'ды’ takes the:", ["genitive", "dative", "accusative", "prepositional"], "genitive", "Лиши'ть + genitive.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 290
L290 = lesson(
    "Verbal adverbs: чита'я and прочита'в",
    "Он за'втракает, проверя'я по'чту.",
    requires=["читать", "прочитать", "проверить", "делать", "сделать"],
    cards=[
        card("What is a verbal adverb?",
             "A verbal adverb (дееприча'стие) is a verb form that works as an adverb. It has no tense, gender or case: it only "
             "adds a second action to the main verb. It comes in two kinds.",
             tables=[table(
                 ["Kind", "Meaning", "English"],
                 [["imperfective", "at the same time as the main action", "while doing, doing"],
                  ["perfective", "before the main action", "having done"]])],
             examples=[
                 ex("Он за'втракает, проверя'я по'чту.", "He eats breakfast while checking his mail.", "проверя'я"),
                 ex("Прове'рив по'чту, он идёт за'втракать.", "Having checked his mail, he goes to have breakfast.", "Прове'рив"),
             ]),
        card("The same person does both actions",
             "The verbal adverb always belongs to the subject of the main verb. The tense is set only by the main verb.",
             tables=[table(
                 ["Sentence", "Who does both?"],
                 [["Идя' домо'й, я встре'тил дру'га.", "я"],
                  ["Прочита'в письмо', она' позвони'ла домо'й.", "она'"],
                  ["Он слу'шает му'зыку, гото'вя у'жин.", "он"]])],
             examples=[
                 ex("Идя' домо'й, я встре'тил дру'га.", "While walking home, I met a friend.", "Идя'"),
                 ex("Прочита'в письмо', она' позвони'ла домо'й.", "Having read the letter, she phoned home.", "Прочита'в"),
             ]),
        card("Mostly written Russian",
             "Verbal adverbs are typical of written and formal Russian. In speech you use a clause with пока' or по'сле того' как.",
             tables=[table(
                 ["Written", "Spoken"],
                 [["Чита'я кни'гу, он пил чай.", "Пока' он чита'л кни'гу, он пил чай."],
                  ["Прочита'в кни'гу, он лёг спать.", "По'сле того' как он прочита'л кни'гу, он лёг спать."]])],
             examples=[
                 ex("Чита'я кни'гу, он пил чай.", "While reading the book he drank tea.", "Чита'я"),
             ]),
    ],
    verify=(vf("читать", "читая") + vf("прочитать", "прочитав") + vf("проверять", "проверяя") + vf("проверить", "проверив")
            + vf("делать", "делая") + vf("сделать", "сделав") + vf("слушать", "слушая") + vf("послушать", "послушав")
            + vf("посмотреть", "смотря") + vf("идти", "идя") + vf("готовить", "готовя") + vf("завтракать", "завтракает")
            + vf("письмо", "письмо") + vf("почта", "почту") + vf("встретить", "встретил") + vf("позвонить", "позвонила")
            + vf("пить", "пил")),
    exercises=[
        F("Он пьёт чай, ___ но'вости. (while reading)", "чита'я", ["прочита'в", "чита'л", "чита'ть"], "Simultaneous: imperfective verbal adverb.", "He drinks tea while reading the news."),
        F("___ письмо', она' позвони'ла домо'й. (having read)", "Прочита'в", ["Чита'я", "Прочита'л", "Прочита'ть"], "Sequential: perfective verbal adverb.", "Having read the letter, she phoned home."),
        F("Он идёт по у'лице, ___ му'зыку. (listening)", "слу'шая", ["послу'шав", "слу'шать", "слу'шал"], "Simultaneous.", "He walks along the street listening to music."),
        F("___ дома'шнюю рабо'ту, Ди'ма пошёл в кино'. (having done)", "Сде'лав", ["Де'лая", "Сде'лал", "Сде'лать"], "Sequential.", "Having done his homework, Dima went to the cinema."),
        F("Она' у'жинает, ___ телеви'зор. (watching)", "смотря'", ["посмотре'в", "смо'трит", "смотре'ла"], "Simultaneous.", "She eats supper while watching television."),
        mc("Which verbal adverb shows an action before the main action?", ["прочита'в", "чита'я", "чита'л", "чита'ющий"], "прочита'в", "Perfective.", order=True),
        mc("Verbal adverbs have:", ["no tense, gender or case", "gender and case", "tense and case", "gender and tense"], "no tense, gender or case", "They are unchanging.", order=True),
        mc("Who performs both actions in a sentence with a verbal adverb?", ["the same person", "two different people", "the subject and the object", "nobody"], "the same person", "They share the subject.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 291
L291 = lesson(
    "Imperfective verbal adverbs: чита'я, говоря', слу'жа, сидя'",
    "Мы пьём чай, разгова'ривая.",
    requires=["читать", "слушать", "смотреть", "идти", "работа"],
    cards=[
        card("The rule",
             "Take the они' form, drop the last two letters (-ут, -ют, -ат, -ят) and add -я. After ж, ч, ш and щ write -а instead.",
             tables=[table(
                 ["Infinitive", "Они' form", "Verbal adverb"],
                 [["чита'ть", "чита'ют", "чита'я"],
                  ["слу'шать", "слу'шают", "слу'шая"],
                  ["рабо'тать", "рабо'тают", "рабо'тая"],
                  ["идти'", "иду'т", "идя'"],
                  ["говори'ть", "говоря'т", "говоря'"],
                  ["смотре'ть", "смо'трят", "смотря'"],
                  ["служи'ть", "слу'жат", "служа'"]])],
             examples=[
                 ex("Идя' домо'й, я встре'тил дру'га.", "While walking home I met a friend.", "Идя'"),
                 ex("Рабо'тая в рестора'не, она' про'бовала мно'го блюд.", "While working in a restaurant she tried many dishes.", "Рабо'тая"),
             ]),
        card("Stress and special cases",
             "In a few verbs the stress is different from the они' form. Verbs in -ся end in -ясь. Verbs in -давать, -знавать, -ставать keep -ва-.",
             tables=[table(
                 ["Verb", "Verbal adverb"],
                 [["сиде'ть (сидя'т)", "си'дя"],
                  ["лежа'ть (лежа'т)", "лёжа"],
                  ["занима'ться", "занима'ясь"],
                  ["встава'ть", "встава'я"],
                  ["продава'ть", "продава'я"],
                  ["быть", "бу'дучи"]])],
             examples=[
                 ex("Лёжа на дива'не, он чита'л кни'гу.", "Lying on the sofa, he read a book.", "Лёжа"),
                 ex("Бу'дучи вегетариа'нцем, Ле'на не ест мя'со.", "Being a vegetarian, Lena does not eat meat.", "Бу'дучи"),
             ]),
        card("No imperfective verbal adverb",
             "Some common verbs do not form an imperfective verbal adverb at all: есть, пить, е'хать, спать, хоте'ть, ждать, "
             "мочь, писа'ть. Use a clause with пока' instead.",
             examples=[
                 ex("Пока' он пил чай, он чита'л газе'ту.", "While he drank tea he read the newspaper.", "Пока' он пил"),
             ]),
    ],
    verify=(vf("читать", "читая") + vf("слушать", "слушая") + vf("работать", "работая") + vf("идти", "идя") + vf("говорить", "говоря")
            + vf("посмотреть", "смотря") + vf("служить", "служа") + vf("сидеть", "сидя") + vf("лежать", "лёжа")
            + vf("заниматься", "занимаясь") + vf("вставать", "вставая") + vf("продавать", "продавая") + vf("быть", "будучи")
            + vf("разговаривать", "разговаривая") + vf("улыбаться", "улыбаясь") + vf("встретить", "встретил")
            + vf("пробовать", "пробовала") + vf("диван", "диване") + vf("вегетарианец", "вегетарианцем")
            + vf("есть", "ест") + vf("пить", "пил") + vf("газета", "газету") + vf("мясо", "мясо")),
    exercises=[
        F("___ по у'лице, он слу'шал му'зыку. (walking)", "Идя'", ["Иду'т", "Шёл", "Идти'"], "From иду'т: drop -ут, add -я.", "Walking along the street, he listened to music."),
        F("Она' отвеча'ет, ___. (smiling)", "улыба'ясь", ["улыба'я", "улыба'лась", "улыбну'ться"], "-ся verbs: -ясь.", "She answers, smiling."),
        F("___ в рестора'не, Та'ня про'бовала мно'го блюд. (working)", "Рабо'тая", ["Порабо'тав", "Рабо'тает", "Рабо'тать"], "Simultaneous.", "While working in a restaurant, Tanya tried many dishes."),
        F("___ на дива'не, он чита'л кни'гу. (lying)", "Лёжа", ["Лежа'", "Лежи'", "Лежа'ть"], "The adverb of лежа'ть is лёжа.", "Lying on the sofa, he read a book."),
        F("Мы пьём чай, ___. (chatting)", "разгова'ривая", ["разгова'ривают", "разгова'ривать", "разгова'ривал"], "Simultaneous adverb.", "We drink tea, chatting."),
        F("___ вегетариа'нцем, Ле'на не ест мя'со. (being)", "Бу'дучи", ["Бу'дет", "Бу'дь", "Быть"], "The adverb of быть is бу'дучи.", "Being a vegetarian, Lena does not eat meat."),
        mc("Form the verbal adverb from говоря'т:", ["говоря'", "говоря'в", "говори'вши", "говоря'ся"], "говоря'", "Drop -т, change to -я.", order=True),
        mc("Which verb has no imperfective verbal adverb?", ["пить", "чита'ть", "говори'ть", "идти'"], "пить", "Пить does not form one.", order=True),
        mc("The verbal adverb from занима'ться ends in:", ["-ясь", "-ся", "-ав", "-вши"], "-ясь", "-ся verbs.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 292
L292 = lesson(
    "Perfective verbal adverbs: прочита'в, получи'в, придя'",
    "Прочита'в письмо', он позвони'л домо'й.",
    requires=["прочитать", "купить", "прийти", "сделать", "послушать"],
    cards=[
        card("The rule: -л → -в",
             "Take the masculine past tense and replace the final -л with -в.",
             tables=[table(
                 ["Verb", "Masc. past", "Verbal adverb"],
                 [["прочита'ть", "прочита'л", "прочита'в"],
                  ["получи'ть", "получи'л", "получи'в"],
                  ["уви'деть", "уви'дел", "уви'дев"],
                  ["сде'лать", "сде'лал", "сде'лав"],
                  ["написа'ть", "написа'л", "написа'в"]])],
             examples=[
                 ex("Прочита'в письмо', он позвони'л домо'й.", "Having read the letter, he phoned home.", "Прочита'в"),
                 ex("Сде'лав дома'шнюю рабо'ту, Ди'ма пошёл в кино'.", "Having done his homework, Dima went to the cinema.", "Сде'лав"),
             ]),
        card("When the masculine past does not end in -л",
             "Add -ши. Verbs with -ся always take -вшись.",
             tables=[table(
                 ["Verb", "Masc. past", "Verbal adverb"],
                 [["спасти'", "спас", "спа'сши"],
                  ["вы'расти", "вы'рос", "вы'росши"],
                  ["научи'ться", "научи'лся", "научи'вшись"],
                  ["познако'миться", "познако'мился", "познако'мившись"]])],
             examples=[
                 ex("Вы'росши в дере'вне, наш сосе'д не лю'бит жить в большо'м го'роде.", "Having grown up in the country, our neighbor doesn't like living in a big city.", "Вы'росши"),
                 ex("Познако'мившись с Ле'ной, он позвони'л ей на сле'дующий день.", "Having met Lena, he called her the next day.", "Познако'мившись"),
             ]),
        card("Motion verbs: like the imperfective rule",
             "Verbs in -йти, -вести, -везти, -нести form the perfective adverb the way the imperfective is formed: the они' form minus "
             "the ending plus -я. So one letter can be the only difference between the two aspects.",
             tables=[table(
                 ["Verb", "Verbal adverb", "Meaning"],
                 [["прийти'", "придя'", "having come"],
                  ["вы'йти", "вы'йдя", "having gone out"],
                  ["привезти'", "привезя'", "having brought (by vehicle)"],
                  ["переводи'ть", "переводя'", "while translating"],
                  ["перевести'", "переведя'", "having translated"]])],
             examples=[
                 ex("Придя' домо'й, он включи'л телеви'зор.", "Having come home, he turned on the TV.", "Придя'"),
                 ex("Вы'йдя из до'ма, он закры'л дверь.", "Having gone out of the house, he closed the door.", "Вы'йдя"),
             ]),
    ],
    verify=(vf("прочитать", "прочитав") + vf("получить", "получив") + vf("увидеть", "увидев") + vf("сделать", "сделав")
            + vf("написать", "написав") + vf("спасти", "спасши") + vf("вырасти", "выросши") + vf("научиться", "научившись")
            + vf("познакомиться", "познакомившись") + vf("прийти", "придя") + vf("выйти", "выйдя") + vf("привезти", "привезя")
            + vf("переводить", "переводя") + vf("перевести", "переведя") + vf("купить", "купив") + vf("послушать", "послушав")
            + vf("письмо", "письмо") + vf("позвонить", "позвонил") + vf("деревня", "деревне") + vf("сосед", "сосед")
            + vf("включить", "включил") + vf("телевизор", "телевизор") + vf("закрыть", "закрыл") + vf("дверь", "дверь")
            + vf("следующий", "следующий") + vf("день", "день")),
    exercises=[
        F("___ письмо', он позвони'л домо'й. (having read)", "Прочита'в", ["Чита'я", "Прочита'л", "Прочита'ть"], "Perfective: -л → -в.", "Having read the letter, he phoned home."),
        F("___ биле'ты, мы пошли' в аэропо'рт. (having bought)", "Купи'в", ["Покупа'я", "Купи'л", "Купи'ть"], "Perfective: -л → -в.", "Having bought the tickets, we went to the airport."),
        F("___ домо'й, он включи'л телеви'зор. (having come)", "Придя'", ["Прийти'", "Пришёл", "Приходи'ть"], "Прийти': they-form стем + -я.", "Having come home, he turned on the TV."),
        F("___ пла'вать, он с удово'льствием хо'дит в бассе'йн. (having learned)", "Научи'вшись", ["Научи'в", "Научи'лся", "Научи'ться"], "-ся verbs: -вшись.", "Having learned to swim, he goes to the pool with pleasure."),
        F("Вы'йдя из до'ма, он закры'л ___. (the door)", "дверь", ["две'ри", "две'рью"], "Accusative = nominative.", "Having left the house, he closed the door."),
        F("___ в дере'вне, наш сосе'д не лю'бит жить в большо'м го'роде. (having grown up)", "Вы'росши", ["Вы'росший", "Вы'росла", "Выраста'я"], "Perfective adverb from вы'рос: add -ши.", "Having grown up in the country, our neighbor doesn't like living in a big city."),
        mc("Perfective verbal adverb of сде'лал:", ["сде'лав", "сде'лая", "сде'лавший", "сде'лаемый"], "сде'лав", "-л → -в.", order=True),
        mc("The perfective adverb of прийти' is:", ["придя'", "прише'в", "приходя'", "придё"], "придя'", "Like the imperfective rule.", order=True),
        mc("-ся verbs form perfective verbal adverbs ending in:", ["-вшись", "-ясь", "-ся", "-в"], "-вшись", "Always -вшись.", order=True),
    ],
)


# ---------------------------------------------------------------------------- 293
L293 = lesson(
    "Without doing: не ду'мая, не сказа'в; adverb or participle?",
    "Он ушёл, не сказа'в ни сло'ва.",
    requires=["думать", "слово", "последствие", "потерять", "рассказать"],
    cards=[
        card("Не + verbal adverb = ‘without’",
             "A verbal adverb with не often means ‘without doing’. It can be imperfective or perfective.",
             tables=[table(
                 ["Phrase", "English"],
                 [["не ду'мая о после'дствиях", "without thinking about the consequences"],
                  ["не сказа'в ни сло'ва", "without saying a word"],
                  ["не теря'я ни мину'ты", "without losing a minute"],
                  ["не сдава'ясь", "without giving up"]])],
             examples=[
                 ex("Он ушёл, не сказа'в ни сло'ва.", "He left without saying a word.", "не сказа'в"),
                 ex("Не ду'мая о после'дствиях, он вы'шел на у'лицу без пальто'.", "Without thinking about the consequences, he went outside without a coat.", "Не ду'мая"),
                 ex("Она' рабо'тает, не теря'я ни мину'ты.", "She works without losing a minute.", "не теря'я"),
             ]),
        card("Verbal adverb or participle?",
             "A verbal adverb has no endings and belongs to the subject. A participle agrees with a noun. Compare:",
             tables=[table(
                 ["Sentence", "What it is"],
                 [["Вы'росши в дере'вне, наш сосе'д не лю'бит го'род.", "verbal adverb: the neighbor, having grown up in the country, …"],
                  ["Наш сосе'д, вы'росший в дере'вне, не лю'бит го'род.", "participle: our neighbor, who grew up in the country, …"]])],
             examples=[
                 ex("Вы'росши в дере'вне, наш сосе'д не лю'бит го'род.", "Having grown up in the country, our neighbor does not like cities.", "Вы'росши"),
                 ex("Наш сосе'д, вы'росший в дере'вне, не лю'бит го'род.", "Our neighbor, who grew up in the country, does not like cities.", "вы'росший"),
             ]),
        card("Commas",
             "A phrase with a verbal adverb is separated by commas from the rest of the sentence.",
             examples=[
                 ex("Придя' домо'й, он лёг спать.", "Having come home, he went to bed.", "Придя' домо'й"),
                 ex("Он рассказа'л об э'том, не поду'мав о после'дствиях.", "He told about it without thinking of the consequences.", "не поду'мав"),
             ]),
    ],
    verify=(vf("думать", "думая") + vf("сказать", "сказав") + vf("терять", "теряя") + vf("сдаваться", "сдаваясь") + vf("потерять", "потеряв")
            + vf("слово", "слова") + vf("последствие", "последствиях") + vf("минута", "минуты") + vf("уйти", "ушёл")
            + vf("выйти", "вышел") + vf("пальто", "пальто") + vf("улица", "улицу") + vf("работать", "работает")
            + vf("вырасти", "выросши") + vf("деревня", "деревне") + vf("сосед", "сосед") + vf("любить", "любит")
            + vf("город", "город") + vf("прийти", "придя") + vf("рассказать", "рассказал") + vf("подумать", "подумав")),
    exercises=[
        F("Он ушёл, ___ ни сло'ва. (without saying)", "не сказа'в", ["не сказа'л", "сказа'в", "не сказа'вший"], "Не + perfective verbal adverb.", "He left without saying a word."),
        F("___ о после'дствиях, он вы'шел на у'лицу. (without thinking)", "Не ду'мая", ["Не ду'маю", "Не ду'мавший", "Не ду'мать"], "Не + imperfective verbal adverb.", "Without thinking about the consequences, he went outside."),
        F("Она' рабо'тает, не ___ ни мину'ты. (losing)", "теря'я", ["теря'л", "теря'ть", "теря'ют"], "Verbal adverb: drop -т and add -я.", "She works without losing a minute."),
        F("Наш сосе'д, ___ в дере'вне, не лю'бит го'род. (who grew up)", "вы'росший", ["вы'росши", "вы'росла", "вы'рос"], "Participle: agrees with the noun.", "Our neighbor, who grew up in the country, does not like cities."),
        F("___ в дере'вне, наш сосе'д не лю'бит го'род. (having grown up)", "Вы'росши", ["Вы'росший", "Вы'росла", "Вы'рос"], "Verbal adverb: no endings.", "Having grown up in the country, our neighbor does not like cities."),
        mc("Не + verbal adverb usually means:", ["without doing something", "never doing", "if not doing", "in order not to"], "without doing something", "Without + -ing.", order=True),
        mc("A participle differs from a verbal adverb because it:", ["agrees with a noun", "has no endings", "is always perfective", "never has cases"], "agrees with a noun", "Participles decline.", order=True),
        mc("A phrase with a verbal adverb is set off by:", ["commas", "dashes", "colons", "quotation marks"], "commas", "Commas.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 294
L294 = lesson(
    "Verbal adverb or clause? в то вре'мя как, по'сле того' как, как то'лько",
    "Придя' домо'й, он лёг спать = Когда' он пришёл домо'й, он лёг спать.",
    requires=["после", "пока", "сразу", "время", "работа"],
    cards=[
        card("Imperfective: while",
             "Replace an imperfective verbal adverb with в то вре'мя как, пока' or когда'. Add the subject and put the verb in the "
             "same tense as the main verb.",
             tables=[table(
                 ["Verbal adverb", "Clause"],
                 [["Рабо'тая над перево'дом, Ма'ша слу'шала му'зыку.", "В то вре'мя как Ма'ша рабо'тала над перево'дом, она' слу'шала му'зыку."],
                  ["Идя' домо'й, я встре'тил дру'га.", "Когда' я шёл домо'й, я встре'тил дру'га."]])],
             examples=[
                 ex("Рабо'тая над перево'дом, Ма'ша слу'шала му'зыку.", "While working on a translation, Masha listened to music.", "Рабо'тая"),
             ]),
        card("Perfective: after",
             "Replace a perfective verbal adverb with по'сле того' как, когда' or как то'лько.",
             tables=[table(
                 ["Verbal adverb", "Clause"],
                 [["Услы'шав шаги', соба'ка сра'зу подбежа'ла.", "Как то'лько соба'ка услы'шала шаги', она' сра'зу подбежа'ла."],
                  ["Проведя' два го'да в Герма'нии, Бо'ря стал хорошо' говори'ть по-неме'цки.", "По'сле того' как Бо'ря провёл два го'да в Герма'нии, он стал хорошо' говори'ть по-неме'цки."]])],
             examples=[
                 ex("Услы'шав шаги', соба'ка сра'зу подбежа'ла.", "Hearing steps, the dog ran up at once.", "Услы'шав"),
             ]),
        card("Steps for rewriting",
             "1. Find the verbal adverb. 2. Decide: same time (imperfective) or earlier (perfective). 3. Choose the conjunction. "
             "4. Turn the adverb into a finite verb that agrees with the subject. 5. Put it in the same tense as the main verb.",
             tables=[table(
                 ["Type", "Conjunction"],
                 [["imperfective", "в то вре'мя как, пока', когда'"],
                  ["perfective", "по'сле того' как, как то'лько, когда'"]])],
             examples=[
                 ex("Сде'лав рабо'ту, он пошёл домо'й.", "Having finished the work, he went home.", "Сде'лав"),
                 ex("По'сле того' как он сде'лал рабо'ту, он пошёл домо'й.", "After he finished the work, he went home.", "По'сле того' как он сде'лал"),
             ]),
    ],
    verify=(vf("работать", "работая", "работала") + vf("слушать", "слушала") + vf("идти", "шёл") + vf("встретить", "встретил")
            + vf("услышать", "услышав", "услышала") + vf("подбежать", "подбежала") + vf("провести", "проведя", "провёл")
            + vf("говорить", "говорить") + vf("шаг", "шаги") + vf("перевод", "переводом") + vf("сделать", "сделав", "сделал")
            + vf("пойти", "пошёл") + vf("лечь", "лёг") + vf("прийти", "пришёл") + vf("год", "года") + vf("собака", "собака")),
    exercises=[
        F("Рабо'тая над перево'дом = ___ она' рабо'тала над перево'дом. (while)", "В то вре'мя как", ["По'сле того' как", "Как то'лько", "Хотя'"], "Simultaneous action.", "While she was working on a translation."),
        F("___ он прочита'л письмо', он позвони'л домо'й. (after)", "По'сле того' как", ["В то вре'мя как", "Пока'", "Хотя'"], "Earlier action: по'сле того' как.", "After he read the letter, he phoned home."),
        F("___ соба'ка услы'шала шаги', она' сра'зу подбежа'ла. (as soon as)", "Как то'лько", ["В то вре'мя как", "Пока'", "Хотя'"], "Earlier action followed immediately.", "As soon as the dog heard steps, it ran up at once."),
        F("Идя' домо'й = ___ я шёл домо'й, я встре'тил дру'га. (when)", "Когда'", ["Пото'м", "Хотя'", "Что'бы"], "When I was walking.", "While I was walking home, I met a friend."),
        F("Проведя' два го'да в Герма'нии = По'сле того' как он ___ два го'да в Герма'нии. (spent)", "провёл", ["проводи'л", "проведёт", "проведя'"], "Earlier action: perfective past.", "After he spent two years in Germany."),
        mc("Which conjunction replaces an imperfective verbal adverb?", ["в то вре'мя как", "по'сле того' как", "как то'лько", "потому' что"], "в то вре'мя как", "Simultaneous.", order=True),
        mc("Which replaces a perfective verbal adverb?", ["по'сле того' как", "в то вре'мя как", "пока'", "хотя'"], "по'сле того' как", "Sequential.", order=True),
        mc("When you rewrite an adverb as a clause you must add:", ["a subject", "a participle", "an infinitive", "a question word"], "a subject", "The clause needs its own subject and finite verb.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 295
L295 = lesson(
    "Case conflicts: Мы ве'рим тому', что они' сказа'ли",
    "Мы ве'рим тому', что они' сказа'ли.",
    requires=["верить", "думать", "слышать", "помнить", "рассказать"],
    cards=[
        card("Two verbs, two cases",
             "Sometimes one verb takes the dative and the other the accusative, and the same word ‘what’ has to join them. "
             "Russian solves this with a buffer word то (the neuter of тот). It takes the case of the first verb.",
             tables=[table(
                 ["First verb", "Case", "Sentence"],
                 [["знать", "accusative", "Мы зна'ем, что они' сказа'ли."],
                  ["слы'шать", "accusative", "Мы не слы'шали, что они' сказа'ли."],
                  ["ве'рить", "dative", "Мы ве'рим тому', что они' сказа'ли."],
                  ["ду'мать о", "prepositional", "Мы ду'мали о том, что они' сказа'ли."]])],
             examples=[
                 ex("Мы ве'рим тому', что они' сказа'ли.", "We believe what they said.", "тому', что"),
                 ex("Мы ду'мали о том, что они' сказа'ли.", "We thought about what they said.", "о том, что"),
             ]),
        card("Forms of то",
             "The buffer word to use depends on the case the first verb needs.",
             tables=[table(
                 ["Case", "Form", "Example"],
                 [["Nom. / Acc.", "то", "Он де'лает то, что лю'бит."],
                  ["Gen.", "того'", "Мы бои'мся того', что он ска'жет."],
                  ["Dat.", "тому'", "Мы ве'рим тому', что она' сказа'ла."],
                  ["Instr.", "тем", "Он занима'ется тем, что лю'бит."],
                  ["Prep.", "(о) том", "Мы говори'м о том, что случи'лось."]])],
             examples=[
                 ex("Он занима'ется тем, что лю'бит.", "He does what he loves.", "тем, что"),
                 ex("Мы говори'м о том, что случи'лось.", "We are talking about what happened.", "о том, что"),
             ]),
        card("Nouns, accusative and exceptions",
             "When a noun joins the clauses, use кото'рый instead of то. If the first verb takes the accusative, то is "
             "usually left out. But if the first verb needs any other case, то is needed even when there is no real conflict.",
             tables=[table(
                 ["Case", "Example"],
                 [["noun + кото'рый", "Мы ве'рим лю'дям, кото'рые э'то сказа'ли."],
                  ["accusative: то left out", "Мы зна'ем, что они' сказа'ли."],
                  ["other case: то needed", "Подро'стки не ве'рят тому', чему' роди'тели их у'чат."]])],
             examples=[
                 ex("Мы ве'рим лю'дям, кото'рые э'то сказа'ли.", "We believe the people who said it.", "кото'рые"),
                 ex("Подро'стки не ве'рят тому', чему' роди'тели стара'ются их учи'ть.", "Teenagers do not believe what their parents try to teach them.", "тому', чему'"),
             ]),
    ],
    verify=(vf("знать", "знаем") + vf("слышать", "слышали") + vf("верить", "верим", "верят") + vf("думать", "думали")
            + vf("сказать", "сказали", "скажет") + vf("говорить", "говорим") + vf("случиться", "случилось")
            + vf("заниматься", "занимается") + vf("любить", "любит") + vf("бояться", "боимся") + vf("делать", "делает")
            + vf("человек", "людям") + vf("который", "которые") + vf("подросток", "подростки") + vf("родитель", "родители")
            + vf("учить", "учат", "учить") + vf("стараться", "стараются") + vf("тот", "того", "тому", "том", "тем")),
    exercises=[
        F("Мы ве'рим ___, что они' сказа'ли.", "тому'", ["то", "того'", "том"], "Ве'рить takes the dative: тому'.", "We believe what they said."),
        F("Мы ду'мали о ___, что они' сказа'ли.", "том", ["то", "тому'", "тем"], "О + prepositional: о том.", "We thought about what they said."),
        F("Он занима'ется ___, что лю'бит.", "тем", ["то", "тому'", "том"], "Занима'ться takes the instrumental: тем.", "He does what he loves."),
        F("Мы зна'ем, ___ они' сказа'ли.", "что", ["чему'", "о чём", "чем"], "Both verbs take the accusative: no buffer.", "We know what they said."),
        F("Подро'стки не ве'рят ___, чему' роди'тели стара'ются их учи'ть.", "тому'", ["то", "того'", "тем"], "Ве'рить takes the dative.", "Teenagers do not believe what their parents try to teach them."),
        F("Мы ве'рим лю'дям, ___ э'то сказа'ли. (who)", "кото'рые", ["что", "то", "чему'"], "A noun links the clauses: кото'рый.", "We believe the people who said it."),
        mc("Why is то needed in ‘Мы ве'рим тому', что они' сказа'ли’?", ["the two verbs need different cases", "because of the past tense", "because of the plural", "because it is a question"], "the two verbs need different cases", "Ве'рить + dative, сказа'ть + accusative.", order=True),
        mc("What case is тому'?", ["dative", "genitive", "accusative", "instrumental"], "dative", "Тому' = dative of то.", order=True),
        mc("If the first verb takes the accusative, то is:", ["usually left out", "always required", "always genitive", "always plural"], "usually left out", "Мы зна'ем, что …", order=True),
    ],
)

# ---------------------------------------------------------------------------- 296
L296 = lesson(
    "то after prepositions: из-за того', что; по'сле того' как; о том, как",
    "Ава'рия произошла' из-за того', что води'тель не уви'дел знак.",
    requires=["зависеть", "причина", "благодаря", "перед", "вернуться"],
    cards=[
        card("Conjunctions made of preposition + то",
             "Many conjunctions are formed from a preposition, a form of то and что or как. The preposition decides the form of то.",
             tables=[table(
                 ["Conjunction", "English"],
                 [["из-за того', что", "because of the fact that"],
                  ["благодаря' тому', что", "thanks to the fact that"],
                  ["несмотря' на то, что", "despite the fact that"],
                  ["по'сле того' как", "after"],
                  ["до того' как", "before"],
                  ["пе'ред тем как", "just before"],
                  ["в то вре'мя как", "while"]])],
             examples=[
                 ex("Ава'рия произошла' из-за того', что води'тель не уви'дел знак.", "The accident happened because the driver did not see the sign.", "из-за того', что"),
                 ex("По'сле того' как Ле'на око'нчила рабо'ту, она' пошла' спать.", "After Lena finished her work, she went to bed.", "По'сле того' как"),
                 ex("Мы верну'лись домо'й как раз пе'ред тем как пошёл дождь.", "We got home just before it started to rain.", "пе'ред тем как"),
             ]),
        card("Verb + preposition + то",
             "After a verb with a preposition, то often introduces an indirect question.",
             tables=[table(
                 ["Verb + preposition", "Example"],
                 [["зави'сеть от", "Цена' зави'сит от того', куда' вы лети'те."],
                  ["ду'мать о", "Мы ду'мали о том, почему' мы проигра'ли."],
                  ["говори'ть о", "Они' говори'ли о том, где жить."]])],
             examples=[
                 ex("Цена' биле'тов зави'сит от того', куда' вы лети'те.", "The price of the tickets depends on where you are flying.", "от того'"),
             ]),
        card("Noun + preposition + то",
             "Nouns and short adjectives also use то.",
             tables=[table(
                 ["Phrase", "English"],
                 [["статья' о том, как …", "an article about how …"],
                  ["вопро'с о том, почему' …", "a question about why …"],
                  ["Пробле'ма в том, что …", "The problem is that …"]])],
             examples=[
                 ex("Вот статья' о том, как стать миллионе'ром.", "Here is an article about how to become a millionaire.", "о том, как"),
                 ex("Пробле'ма в том, что вре'мени ма'ло.", "The problem is that there is little time.", "в том, что"),
                 ex("Он смог прийти', несмотря' на то, что бо'лен.", "He managed to come in spite of being ill.", "на то, что"),
             ]),
    ],
    verify=(vf("авария", "авария") + vf("водитель", "водитель") + vf("увидеть", "увидел") + vf("знак", "знак")
            + vf("благодаря", "благодаря") + vf("закончить", "закончить") + vf("окончить", "окончила")
            + vf("вернуться", "вернулись") + vf("дождь", "дождь") + vf("зависеть", "зависит") + vf("билет", "билетов")
            + vf("лететь", "летите") + vf("проиграть", "проиграли") + vf("жить", "жить") + vf("статья", "статья")
            + vf("стать", "стать") + vf("миллионер", "миллионером") + vf("проблема", "проблема") + vf("время", "времени")
            + vf("прийти", "прийти") + vf("мочь", "смог")),
    exercises=[
        F("Ава'рия произошла' из-за ___, что води'тель не уви'дел знак.", "того'", ["то", "тому'", "том"], "Из-за + genitive.", "The accident happened because the driver did not see the sign."),
        F("Цена' биле'тов зави'сит ___ того', куда' вы лети'те.", "от", ["о", "на", "за"], "Зави'сеть от + genitive.", "The price of the tickets depends on where you are flying."),
        F("___ того' как Ле'на око'нчила рабо'ту, она' пошла' спать. (After)", "По'сле", ["Пе'ред", "До", "Из-за"], "After: по'сле того' как.", "After Lena finished work, she went to bed."),
        F("Мы верну'лись домо'й как раз ___ тем как пошёл дождь. (just before)", "пе'ред", ["по'сле", "из-за", "благодаря'"], "Just before: пе'ред тем как.", "We got home just before it started to rain."),
        F("Пробле'ма ___ том, что вре'мени ма'ло. (is in)", "в", ["на", "о", "к"], "Пробле'ма в том, что …", "The problem is that there is little time."),
        F("Вот статья' ___ том, как стать миллионе'ром. (about)", "о", ["об", "в", "на"], "О + prepositional: о том.", "Here is an article about how to become a millionaire."),
        F("Он смог прийти', несмотря' ___ то, что бо'лен. (despite)", "на", ["от", "в", "за"], "Несмотря' на то, что …", "He managed to come in spite of being ill."),
        mc("‘Благодаря' тому', что’ means:", ["thanks to the fact that", "despite the fact that", "before", "while"], "thanks to the fact that", "Благодаря' + dative.", order=True),
        mc("‘Пе'ред тем как’ expresses:", ["just before", "just after", "because", "although"], "just before", "Пе'ред + instrumental.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 297
L297 = lesson(
    "дово'лен тем, что; тот, кто; те, кто",
    "Тот, кто придёт пе'рвым, полу'чит приз.",
    requires=["довольный", "опасный", "правда", "ответить", "интерес"],
    cards=[
        card("Short adjectives with то",
             "Short-form adjectives govern a case, so they also need то before что or an indirect question.",
             tables=[table(
                 ["Adjective", "Case", "With то"],
                 [["дово'лен / недово'лен", "чем (instr.)", "недово'лен тем, ско'лько ему' пла'тят"],
                  ["рад", "чему' (dat.)", "рад тому', что вы пришли'"],
                  ["уве'рен", "в чём (prep.)", "уве'рен в том, что он прав"],
                  ["согла'сен", "с чем (instr.)", "согла'сен с тем, что вы сказа'ли"],
                  ["опа'сен", "чем (instr.)", "опа'сен тем, что мало' освеще'ния"]])],
             examples=[
                 ex("И'горь недово'лен тем, ско'лько ему' пла'тят.", "Igor is dissatisfied with how much he is paid.", "тем, ско'лько"),
                 ex("Э'та доро'га опа'сна тем, что на ней мало' освеще'ния.", "This road is dangerous because there is little lighting on it.", "тем, что"),
                 ex("Я рад тому', что вы пришли'.", "I am glad that you came.", "тому', что"),
             ]),
        card("Тот, кто and те, кто",
             "To speak about people in general, use тот with кто (singular) or те with кто (plural). Each part takes its own case.",
             tables=[table(
                 ["Form", "Example"],
                 [["тот, кто", "Тот, кто придёт пе'рвым, полу'чит приз."],
                  ["те, кто", "Те, у кого' есть соба'ка, ча'сто гуля'ют."],
                  ["тому', кого'", "Всегда' говори'те пра'вду тому', кого' вы лю'бите."],
                  ["у тех, кто", "У тех, кто говори'т на иностра'нном языке', лу'чше па'мять."]])],
             examples=[
                 ex("Тот, кто придёт пе'рвым, полу'чит приз.", "The one who comes first will get a prize.", "Тот, кто"),
                 ex("Те, у кого' есть соба'ка, ча'сто гуля'ют.", "Those who have a dog walk often.", "Те, у кого'"),
             ]),
        card("Agreement",
             "After те the main verb is plural. After кто the verb in the second clause is usually singular, but the plural is "
             "also heard.",
             examples=[
                 ex("Всегда' говори'те пра'вду тому', кого' вы лю'бите.", "Always tell the truth to the one you love.", "тому', кого'"),
             ]),
    ],
    verify=(vf("довольный", "доволен") + vf("рад", "рад") + vf("уверенный", "уверен") + vf("согласный", "согласен")
            + vf("опасный", "опасна") + vf("платить", "платят") + vf("прийти", "придёт", "пришли") + vf("получить", "получит")
            + vf("приз", "приз") + vf("собака", "собака") + vf("гулять", "гуляют") + vf("правда", "правду")
            + vf("любить", "любите") + vf("говорить", "говорите", "говорит") + vf("язык", "языке") + vf("память", "память")
            + vf("освещение", "освещения") + vf("иностранный", "иностранном") + vf("дорога", "дорога")),
    exercises=[
        F("И'горь недово'лен ___, ско'лько ему' пла'тят.", "тем", ["то", "тому'", "том"], "Дово'лен + instrumental.", "Igor is dissatisfied with how much he is paid."),
        F("Я рад ___, что вы пришли'.", "тому'", ["то", "том", "тем"], "Рад + dative.", "I am glad that you came."),
        F("Я уве'рен в ___, что он прав.", "том", ["то", "тому'", "тем"], "В + prepositional.", "I am sure that he is right."),
        F("___, кто придёт пе'рвым, полу'чит приз. (The one)", "Тот", ["Те", "Того'", "Тому'"], "Singular: тот, кто.", "The one who comes first will get a prize."),
        F("Всегда' говори'те пра'вду ___, кого' вы лю'бите. (to the one)", "тому'", ["тот", "того'", "том"], "Dative after говори'те.", "Always tell the truth to the one you love."),
        F("___, у кого' есть соба'ка, ча'сто гуля'ют. (Those)", "Те", ["Тот", "Тех", "Тем"], "Plural, nominative; the verb is plural.", "Those who have a dog walk often."),
        F("Э'та доро'га опа'сна ___, что на ней мало' освеще'ния.", "тем", ["то", "тому'", "том"], "Опа'сен + instrumental.", "This road is dangerous because there is little lighting on it."),
        mc("‘Те, кто’ means:", ["those who", "the one who", "everything that", "who is that"], "those who", "Plural.", order=True),
        mc("‘Дово'лен тем’: тем is in the:", ["instrumental", "dative", "genitive", "prepositional"], "instrumental", "Дово'лен чем?", order=True),
    ],
)

# ---------------------------------------------------------------------------- 298
L298 = lesson(
    "Word-building: -вин-, -след-, под-",
    "Суд призна'л подсуди'мого вино'вным.",
    requires=["вина", "виноватый", "следить", "след", "наследство"],
    cards=[
        card("The root -вин-",
             "-Вин- is about guilt and blame.",
             tables=[table(
                 ["Word", "English"],
                 [["вина'", "guilt, fault"],
                  ["винова'т", "guilty, to blame"],
                  ["вино'вный", "guilty (in a legal sense)"],
                  ["вино'вник", "culprit"],
                  ["неви'нный / невино'вный", "innocent"],
                  ["обвине'ние", "accusation, charge"],
                  ["обвиня'ть / обвини'ть", "to accuse"]])],
             examples=[
                 ex("Кто винова'т?", "Who is to blame?", "винова'т"),
                 ex("Суд призна'л подсуди'мого вино'вным.", "The court found the defendant guilty.", "вино'вным"),
             ]),
        card("The root -след-",
             "-След- is about a trace and following.",
             tables=[table(
                 ["Word", "English"],
                 [["след", "trace, footprint"],
                  ["сле'довать", "to follow"],
                  ["следи'ть за + Instr.", "to watch, to keep an eye on"],
                  ["сле'дователь", "investigator"],
                  ["сле'дствие", "investigation"],
                  ["рассле'дование", "investigation"],
                  ["пресле'довать", "to pursue"],
                  ["насле'дство", "inheritance"]])],
             examples=[
                 ex("Мать следи'т за детьми'.", "The mother is watching the children.", "следи'т за детьми'"),
                 ex("Поли'ция вы'шла на след престу'пника.", "The police got onto the criminal's trail.", "вы'шла на след"),
                 ex("Он получи'л насле'дство от де'душки.", "He received an inheritance from his grandfather.", "насле'дство"),
             ]),
        card("The prefix под- in legal words",
             "Под- can mean ‘under’: a person under someone's protection or authority.",
             tables=[table(
                 ["Word", "English"],
                 [["подсуди'мый", "defendant (the one ‘under the court’)"],
                  ["подзащи'тный", "a lawyer's client (the one ‘under protection’)"],
                  ["подозре'ние", "suspicion"]])],
             examples=[
                 ex("Мой подзащи'тный не признаёт вину'.", "My client does not admit guilt.", "подзащи'тный"),
             ]),
    ],
    verify=(vf("вина", "вина") + vf("виноватый", "виноват") + vf("виновный", "виновным") + vf("виновник", "виновник")
            + vf("невинный", "невинный") + vf("обвинение", "обвинение") + vf("обвинять", "обвинять") + vf("обвинить", "обвинить")
            + vf("след", "след") + vf("следовать", "следовать") + vf("следить", "следит") + vf("следователь", "следователь")
            + vf("следствие", "следствие") + vf("расследование", "расследование") + vf("преследовать", "преследовать")
            + vf("наследство", "наследство") + vf("подсудимый", "подсудимого") + vf("подзащитный", "подзащитный")
            + vf("подозрение", "подозрение") + vf("мать", "мать") + vf("ребёнок", "детьми") + vf("дедушка", "дедушки")
            + vf("признавать", "признаёт") + vf("суд", "суд") + vf("полиция", "полиция") + vf("преступник", "преступника")),
    exercises=[
        F("Кто ___ в э'том? (to blame)", "винова'т", ["вино'вный", "вино'вник", "вина'"], "Short form: винова'т.", "Who is to blame for this?"),
        F("Сле'дователь ведёт ___. (investigation)", "рассле'дование", ["рассле'дования", "рассле'дованию", "рассле'дованием"], "Accusative = nominative.", "The investigator is conducting an investigation.", lemma="расследование"),
        F("Мать следи'т ___ детьми'. (watches)", "за", ["на", "по", "о"], "Следи'ть за + instrumental.", "The mother is watching the children."),
        F("Поли'ция вы'шла на ___ престу'пника. (trail)", "след", ["сле'да", "сле'ду", "сле'де"], "Вы'йти на след: accusative.", "The police got onto the criminal's trail.", lemma="след"),
        F("Он получи'л ___ от де'душки. (inheritance)", "насле'дство", ["насле'дства", "насле'дству", "насле'дстве"], "Accusative = nominative.", "He received an inheritance from his grandfather.", lemma="наследство"),
        mc("What does неви'нный mean?", ["innocent", "guilty", "suspicious", "punished"], "innocent", "Не- + вин-.", order=True),
        mc("What does пресле'довать mean?", ["to pursue", "to follow rules", "to inherit", "to acquit"], "to pursue", "Root -след-.", order=True),
        mc("Who is a подсуди'мый?", ["the defendant", "the judge", "the witness", "the lawyer"], "the defendant", "The person ‘under the court’.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 299
L299 = lesson(
    "Review: crime, verbal adverbs and case conflicts",
    "Прочита'в пригово'р, он не ве'рил тому', что слы'шит.",
    requires=["закон", "суд", "читать", "сделать", "верить"],
    cards=[
        card("Verbal adverbs: a reminder",
             "Imperfective (at the same time): они' form minus the ending + -я (чита'ют → чита'я). Perfective (before): masculine past "
             "−л + в (прочита'л → прочита'в); -ся verbs: -вшись; -йти, -вести, -везти, -нести: they-form + -я (придя'). Не + adverb = ‘without’.",
             tables=[table(
                 ["Aspect", "Example"],
                 [["imperfective", "Идя' домо'й, я слу'шал му'зыку."],
                  ["perfective", "Придя' домо'й, я включи'л телеви'зор."],
                  ["не + adverb", "Он ушёл, не сказа'в ни сло'ва."]])],
             examples=[
                 ex("Прочита'в пригово'р, он не ве'рил тому', что слы'шит.", "Having read the verdict, he did not believe what he was hearing.", "Прочита'в"),
             ]),
        card("The buffer word то",
             "Use то in the case required by the first verb, adjective, noun or preposition. Use тот, кто and те, кто for people.",
             tables=[table(
                 ["Case", "Example"],
                 [["dative", "Мы ве'рим тому', что они' сказа'ли."],
                  ["prepositional", "Мы говори'м о том, что случи'лось."],
                  ["genitive", "из-за того', что"],
                  ["people", "Те, кто нару'шил зако'н, отвеча'ют пе'ред судо'м."]])],
             examples=[
                 ex("Те, кто нару'шил зако'н, отвеча'ют пе'ред судо'м.", "Those who broke the law answer before the court.", "Те, кто"),
             ]),
    ],
    verify=(vf("читать", "читая") + vf("прочитать", "прочитав") + vf("верить", "верил", "верим") + vf("слышать", "слышит")
            + vf("приговор", "приговор") + vf("закон", "закон") + vf("суд", "судом") + vf("нарушить", "нарушил")
            + vf("отвечать", "отвечают") + vf("слушать", "слушал") + vf("включить", "включил") + vf("сказать", "сказав", "сказали")
            + vf("говорить", "говорим") + vf("случиться", "случилось")),
    exercises=[
        F("___ пригово'р, он не ве'рил тому', что слы'шит. (having read)", "Прочита'в", ["Чита'я", "Прочита'л", "Прочита'ть"], "Earlier action: perfective adverb.", "Having read the verdict, he did not believe what he was hearing."),
        F("Он не ве'рил ___, что слы'шит. (what)", "тому'", ["то", "того'", "том"], "Ве'рить + dative.", "He did not believe what he heard."),
        F("___ домо'й, я слу'шал му'зыку. (walking)", "Идя'", ["Придя'", "Шёл", "Идти'"], "Simultaneous adverb.", "Walking home, I listened to music."),
        F("Он ушёл, не ___ ни сло'ва. (saying)", "сказа'в", ["сказа'л", "говоря'т", "скажи'"], "Не + perfective adverb.", "He left without saying a word."),
        F("Ава'рия произошла' из-за ___, что дождь шёл це'лый день. (the fact)", "того'", ["то", "тому'", "том"], "Из-за + genitive.", "The accident happened because it rained all day."),
        F("___, кто нару'шил зако'н, отвеча'ют пе'ред судо'м. (Those)", "Те", ["Тот", "Тех", "Тем"], "Plural: отвеча'ют.", "Those who broke the law answer before the court."),
        F("Он обвиня'ет её ___ кра'же. (of)", "в", ["на", "за", "к"], "Обвиня'ть в + prepositional.", "He accuses her of theft."),
        mc("Which means ‘without thinking’?", ["не ду'мая", "ду'мая", "поду'мав", "не ду'мать"], "не ду'мая", "Не + imperfective adverb.", order=True),
        mc("Which word is the buffer in ‘Мы говори'м ___ том, что случи'лось’?", ["о", "в", "на", "с"], "о", "Говори'ть о + prepositional.", order=True),
    ],
)

UNIT = unit("Unit 29: Crime and justice, verbal adverbs and case conflicts",
            [L286, L287, L288, L289, L290, L291, L292, L293, L294, L295, L296, L297, L298, L299])
