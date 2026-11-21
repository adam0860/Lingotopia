"""Unit 23: health, the prepositional plural, short adjectives, impersonal verbs, пусть
(textbook module 5, lessons 30-31)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 213
L213 = lesson(
    "My throat hurts: illnesses, symptoms and parts of the body",
    "У меня' боли'т го'рло и высо'кая температу'ра.",
    requires=["боль", "горло", "спина", "зуб", "температура"],
    cards=[
        card("Illnesses and symptoms",
             "The basic vocabulary for saying what is wrong.",
             tables=[table(
                 ["Word", "English"],
                 [["боле'знь (f.)", "illness, disease"],
                  ["заболева'ние", "illness (formal)"],
                  ["боль (f.)", "pain"],
                  ["грипп", "flu"],
                  ["просту'да", "common cold"],
                  ["ка'шель (gen. ка'шля)", "cough"],
                  ["на'сморк", "runny nose"],
                  ["ожо'г", "burn"],
                  ["пищево'е отравле'ние", "food poisoning"],
                  ["температу'ра", "temperature, fever"],
                  ["давле'ние", "blood pressure"]])],
             examples=[
                 ex("У меня' просту'да и на'сморк.", "I have a cold and a runny nose.", "просту'да"),
                 ex("У неё высо'кая температу'ра.", "She has a high fever.", "высо'кая температу'ра"),
                 ex("Э'то лека'рство от ка'шля.", "This is a cough medicine.", "от ка'шля"),
             ]),
        card("Parts of the body",
             "In Russian you say that a part of the body hurts with у + genitive and the verb боле'ть in the third "
             "person. The body part is the subject, so the verb agrees with it: боли'т (singular), боля'т (plural).",
             tables=[table(
                 ["Word", "English"],
                 [["го'рло", "throat"],
                  ["живо'т", "stomach"],
                  ["зуб", "tooth"],
                  ["спина'", "back"],
                  ["се'рдце", "heart"],
                  ["органи'зм", "body (internal)"],
                  ["голова'", "head"]])],
             examples=[
                 ex("У меня' боли'т го'рло.", "My throat hurts.", "боли'т го'рло"),
                 ex("У ребёнка боли'т живо'т.", "The child has a stomachache.", "боли'т живо'т"),
                 ex("У него' боля'т зу'бы.", "His teeth hurt.", "боля'т зу'бы"),
             ]),
        card("Pain in...",
             "The noun боль takes в and the prepositional case: боль в спине', боль в животе', боль в го'рле.",
             examples=[
                 ex("У неё си'льная боль в спине'.", "She has severe back pain.", "боль в спине'"),
                 ex("У меня' боль в го'рле.", "I have a sore throat.", "боль в го'рле"),
             ]),
    ],
    verify=(vf("болезнь", "болезнь") + vf("грипп", "грипп") + vf("простуда", "простуда") + vf("кашель", "кашля")
            + vf("насморк", "насморк") + vf("температура", "температура") + vf("горло", "горло", "горле")
            + vf("живот", "живот", "животе") + vf("зуб", "зубы") + vf("спина", "спине") + vf("сердце", "сердце")
            + vf("болеть", "болит", "болят") + vf("сильный", "сильная") + vf("лекарство", "лекарство")),
    exercises=[
        F("У меня' боли'т ___. (throat)", "го'рло", ["го'рла", "го'рлу", "го'рле"], "Subject: nominative го'рло.", "My throat hurts.", lemma="горло"),
        F("У ребёнка боли'т ___. (stomach)", "живо'т", ["живота'", "животу'", "животе'"], "Subject: nominative живо'т.", "The child has a stomachache.", lemma="живот"),
        F("У него' ___ зу'бы. (hurt)", "боля'т", ["боли'т", "боле'ю", "боле'ть"], "Plural subject: боля'т.", "His teeth hurt."),
        F("У неё высо'кая ___. (fever)", "температу'ра", ["температу'ры", "температу'ру", "температу'ре"], "Nominative.", "She has a high fever.", lemma="температура"),
        F("У меня' си'льная боль в ___. (back)", "спине'", ["спина'", "спину'", "спи'ной"], "В + prepositional.", "I have severe back pain.", lemma="спина"),
        F("Э'то лека'рство ___ ка'шля. (for)", "от", ["из", "к", "у"], "Лека'рство от + genitive.", "This is a cough medicine."),
        F("У меня' просту'да и ___. (runny nose)", "на'сморк", ["на'сморка", "на'сморку", "на'сморке"], "Nominative.", "I have a cold and a runny nose."),
        mc("Which word means “throat”?", ["го'рло", "живо'т", "спина'", "се'рдце"], "го'рло", "Го'рло = throat.", order=True),
        mc("What is the genitive of ка'шель?", ["ка'шля", "ка'шеля", "ка'шлю", "ка'шлем"], "ка'шля", "The e is fleeting: ка'шля."),
    ],
)

# ---------------------------------------------------------------------------- 214
L214 = lesson(
    "At the clinic: appointment, test, prescription",
    "Я записа'лся на приём к врачу'.",
    requires=["врач", "приём", "анализ", "рецепт", "лекарство"],
    cards=[
        card("Words for a visit to the doctor",
             "A clinic visit has its own vocabulary.",
             tables=[table(
                 ["Word", "English"],
                 [["приём", "appointment; reception"],
                  ["ана'лиз", "lab test"],
                  ["реце'пт", "prescription; recipe"],
                  ["лека'рство (от + gen.)", "medicine (for)"],
                  ["спра'вка", "doctor's note"],
                  ["больни'чный лист", "sick leave certificate"],
                  ["о'чередь (f.)", "line, turn"],
                  ["вес", "weight"],
                  ["кровь (f.)", "blood"],
                  ["профила'ктика", "prevention"]])],
             examples=[
                 ex("Я записа'лся на приём к врачу'.", "I made an appointment with the doctor.", "на приём к врачу'"),
                 ex("Врач вы'писал мне реце'пт.", "The doctor wrote me a prescription.", "вы'писал мне реце'пт"),
                 ex("Мне ну'жно сдать ана'лиз кро'ви.", "I need to have a blood test.", "ана'лиз кро'ви"),
             ]),
        card("Verbs at the doctor",
             "These verbs come in aspect pairs.",
             tables=[table(
                 ["Verb", "English"],
                 [["запи'сываться / записа'ться на приём", "to make an appointment"],
                  ["выпи'сывать / вы'писать реце'пт", "to write a prescription"],
                  ["принима'ть / приня'ть лека'рство", "to take medicine"],
                  ["измеря'ть / изме'рить давле'ние", "to measure blood pressure"],
                  ["проходи'ть / пройти' медосмо'тр", "to have a medical check-up"],
                  ["вызыва'ть / вы'звать врача' на дом", "to call a doctor to the house"]])],
             examples=[
                 ex("Медсестра' измеря'ет мне давле'ние.", "The nurse is taking my blood pressure.", "измеря'ет"),
                 ex("Лека'рство принима'ют три ра'за в день.", "You take this medicine three times a day.", "принима'ют"),
             ]),
    ],
    verify=(vf("врач", "врачу") + vf("записаться", "записался") + vf("выписать", "выписал") + vf("рецепт", "рецепт")
            + vf("анализ", "анализ") + vf("кровь", "крови") + vf("справка", "справка") + vf("очередь", "очереди")
            + vf("давление", "давление") + vf("измерять", "измеряет") + vf("принимать", "принимают")
            + vf("день", "день") + vf("медсестра", "медсестра") + vf("человек", "человек") + vf("раз", "раза")),
    exercises=[
        F("Я записа'лся ___ приём к врачу'. (for)", "на", ["в", "к", "у"], "Записа'ться на приём.", "I made an appointment with the doctor."),
        F("Врач вы'писал мне ___. (prescription)", "реце'пт", ["реце'пта", "реце'пту", "реце'пте"], "Accusative = nominative.", "The doctor wrote me a prescription.", lemma="рецепт"),
        F("Мне нужна' ___ из поликли'ники. (a doctor's note)", "спра'вка", ["спра'вки", "спра'вку", "спра'вке"], "Нужна' + nominative.", "I need a note from the clinic.", lemma="справка"),
        F("Медсестра' измеря'ет ___. (blood pressure)", "давле'ние", ["давле'ния", "давле'нию", "давле'нии"], "Accusative = nominative for neuter.", "The nurse is measuring my blood pressure.", lemma="давление"),
        F("Мне ну'жно сдать ана'лиз ___. (blood)", "кро'ви", ["кровь", "кро'вью", "кро'вей"], "Genitive: ана'лиз кро'ви.", "I need to have a blood test.", lemma="кровь"),
        F("Лека'рство надо принима'ть три ра'за в ___. (day)", "день", ["дня", "дню", "дне"], "В день = per day.", "You must take the medicine three times a day."),
        F("В о'череди сидя'т пять ___. (people)", "челове'к", ["люде'й", "челове'ка", "лю'ди"], "After 5: челове'к.", "Five people are sitting in line."),
        mc("Which word means “prescription”?", ["реце'пт", "приём", "спра'вка", "ана'лиз"], "реце'пт", "Реце'пт = prescription.", order=True),
        mc("What do you say to make an appointment?", ["записа'ться на приём", "вы'писать реце'пт", "вы'звать врача'", "изме'рить давле'ние"], "записа'ться на приём", "Записа'ться на приём."),
    ],
)

# ---------------------------------------------------------------------------- 215
L215 = lesson(
    "I got the flu, I feel better: verbs of illness",
    "Как вы себя' чу'вствуете? Спаси'бо, мне уже' лу'чше.",
    requires=["болеть", "чувствовать", "вызвать", "умирать", "жаловаться"],
    cards=[
        card("Being ill",
             "Боле'ть has two meanings. With the instrumental it means to be sick with an illness. With the "
             "body part as the subject it means to hurt.",
             tables=[table(
                 ["Verb", "Meaning", "Example"],
                 [["боле'ть / заболе'ть (+ instr.)", "be sick with / get sick with", "Он заболе'л гри'ппом."],
                  ["боле'ть / заболе'ть (у + gen.)", "hurt / start to hurt", "У неё заболе'ла голова'."],
                  ["выздора'вливать / вы'здороветь", "get better / recover", "Мы вы'здоровели от просту'ды."],
                  ["лечи'ть / вы'лечить (от + gen.)", "treat / cure", "Врач вы'лечил её от просту'ды."],
                  ["лечи'ться", "undergo treatment", "Я лечу'сь у э'того врача'."],
                  ["вызыва'ть / вы'звать", "call", "Мы вы'звали ско'рую по'мощь."],
                  ["ложи'ться / лечь", "lie down", "Он лёг в больни'цу."],
                  ["устава'ть / уста'ть (от + gen.)", "get tired (of)", "Она' уста'ла от шу'ма."],
                  ["отравля'ться / отрави'ться", "get poisoned", "Мы отрави'лись гриба'ми."]])],
             examples=[
                 ex("Он заболе'л гри'ппом.", "He came down with the flu.", "заболе'л гри'ппом"),
                 ex("Мы вы'звали ско'рую по'мощь.", "We called an ambulance.", "вы'звали ско'рую по'мощь"),
                 ex("Она' уста'ла от шу'ма.", "She got tired of the noise.", "уста'ла от шу'ма"),
             ]),
        card("How are you feeling?",
             "Чу'вствовать себя' means to feel. Ask and answer with these phrases.",
             tables=[table(
                 ["Russian", "English"],
                 [["Как вы себя' чу'вствуете?", "How are you feeling?"],
                  ["Нева'жно.", "Not so good."],
                  ["Спаси'бо, ничего'.", "Thank you, okay."],
                  ["Спаси'бо, мне уже' лу'чше.", "Thank you, I'm better already."],
                  ["У него' высо'кая температу'ра.", "He has a high fever."]])],
             examples=[
                 ex("Как вы себя' чу'вствуете?", "How are you feeling?", "чу'вствуете"),
                 ex("Спаси'бо, мне уже' лу'чше.", "Thank you, I'm better already.", "мне уже' лу'чше"),
             ]),
    ],
    verify=(vf("заболеть", "заболел", "заболела") + vf("грипп", "гриппом") + vf("выздороветь", "выздоровели")
            + vf("вылечить", "вылечил") + vf("лечиться", "лечусь") + vf("вызвать", "вызвали") + vf("лечь", "лёг")
            + vf("устать", "устала") + vf("отравиться", "отравились") + vf("шум", "шума") + vf("гриб", "грибами")
            + vf("чувствовать", "чувствуете") + vf("скорая", "скорую") + vf("помощь", "помощь")),
    exercises=[
        F("Он заболе'л ___. (the flu)", "гри'ппом", ["грипп", "гри'ппа", "гри'ппе"], "Заболе'ть + instrumental.", "He came down with the flu."),
        F("Как вы себя' ___? (feel)", "чу'вствуете", ["чу'вствуют", "чу'вствую", "чу'вствуешь"], "Вы → чу'вствуете.", "How are you feeling?"),
        F("Спаси'бо, мне уже' ___. (better)", "лу'чше", ["лу'чший", "ху'же", "пло'хо"], "Мне лу'чше.", "Thank you, I'm better already."),
        F("Врач ___ её от просту'ды. (cured)", "вы'лечил", ["вы'лечила", "вы'лечили", "вы'лечило"], "Masculine singular.", "The doctor cured her of her cold."),
        F("Мы вы'звали ___ по'мощь. (ambulance)", "ско'рую", ["ско'рая", "ско'рой", "ско'рые"], "Accusative feminine.", "We called an ambulance."),
        F("Он лёг ___ больни'цу. (into)", "в", ["на", "к", "у"], "Лечь в больни'цу.", "He was admitted to the hospital."),
        F("Она' уста'ла ___ шу'ма. (of)", "от", ["из", "с", "до"], "Уста'ть от + genitive.", "She got tired of the noise."),
        mc("What does боле'ть mean with a body part as the subject?", ["to hurt", "to cure", "to recover", "to call"], "to hurt", "У меня' боли'т голова'."),
        mc("What case follows заболе'ть when the illness is named?", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "Заболе'ть гри'ппом."),
    ],
)

# ---------------------------------------------------------------------------- 216
L216 = lesson(
    "In restaurants, about friends: the prepositional plural of nouns",
    "Мы ужинаем в рестора'нах и говори'м о друзья'х.",
    requires=["магазин", "город", "школа", "друг", "урок"],
    cards=[
        card("-ах or -ях",
             "The prepositional plural is used after в, на, о (об), при. Nouns take -ах after a hard stem and -ях after a "
             "soft stem, and the stress stays where it was in the nominative plural.",
             tables=[table(
                 ["Nominative plural", "Prepositional plural", "Type"],
                 [["рестора'ны", "рестора'н{ах}", "hard"],
                  ["магази'ны", "магази'н{ах}", "hard"],
                  ["уро'ки", "уро'к{ах}", "hard"],
                  ["города'", "город{а'х}", "hard"],
                  ["больни'цы", "больни'ц{ах}", "after ц"],
                  ["врачи'", "врач{а'х}", "after ч"],
                  ["музе'и", "музе'{ях}", "soft"],
                  ["учителя'", "учител{я'х}", "soft"],
                  ["пробле'мы", "пробле'м{ах}", "hard"]])],
             examples=[
                 ex("Мы у'жинаем в рестора'нах.", "We have dinner in restaurants.", "в рестора'нах"),
                 ex("Мы говори'м о пробле'мах.", "We talk about problems.", "о пробле'мах"),
                 ex("На уро'ках мы ча'сто чита'ем.", "In class we often read.", "На уро'ках"),
             ]),
        card("Special nouns",
             "The same irregular plurals appear here. Watch for матеря'х and деревня'х, whose stress moves to the ending.",
             tables=[table(
                 ["Nominative plural", "Prepositional plural"],
                 [["друзья'", "друзья'х"],
                  ["де'ти", "де'тях"],
                  ["лю'ди", "лю'дях"],
                  ["ма'тери", "матеря'х"],
                  ["до'чери", "дочеря'х"],
                  ["бра'тья", "бра'тьях"],
                  ["сёстры", "сёстрах"],
                  ["дере'вни", "деревня'х"],
                  ["го'сти", "гостя'х"]])],
             examples=[
                 ex("Он ча'сто ду'мает о друзья'х.", "He often thinks about his friends.", "о друзья'х"),
                 ex("Ма'ма ча'сто говори'т о де'тях.", "Mom often talks about the children.", "о де'тях"),
                 ex("Мы бы'ли в гостя'х у друзе'й.", "We were visiting friends.", "в гостя'х"),
             ]),
    ],
    verify=(vf("ресторан", "ресторанах") + vf("магазин", "магазинах") + vf("урок", "уроках") + vf("город", "городах")
            + vf("больница", "больницах") + vf("врач", "врачах") + vf("музей", "музеях") + vf("учитель", "учителях")
            + vf("проблема", "проблемах") + vf("друг", "друзьях") + vf("ребёнок", "детях") + vf("человек", "людях")
            + vf("мать", "матерях") + vf("дочь", "дочерях") + vf("брат", "братьях") + vf("сестра", "сёстрах")
            + vf("деревня", "деревнях") + vf("гость", "гостях") + vf("школа", "школах")),
    exercises=[
        F("Мы у'жинаем в ___. (restaurants)", "рестора'нах", ["рестора'нов", "рестора'нам", "рестора'нами"], "Hard stem: -ах.", "We have dinner in restaurants.", lemma="ресторан"),
        F("Она' чита'ет о ___. (museums)", "музе'ях", ["музе'ев", "музе'ям", "музе'ями"], "Soft stem: -ях.", "She is reading about museums.", lemma="музей"),
        F("Мы говори'м о ___. (problems)", "пробле'мах", ["пробле'м", "пробле'мам", "пробле'мами"], "Hard stem: -ах.", "We talk about problems.", lemma="проблема"),
        F("Он ча'сто ду'мает о ___. (friends)", "друзья'х", ["друзе'й", "друзья'м", "друзья'ми"], "Special: друзья'х.", "He often thinks about his friends.", lemma="друг"),
        F("Ма'ма ча'сто говори'т о ___. (children)", "де'тях", ["дете'й", "де'тям", "детьми'"], "Special: де'тях.", "Mom often talks about the children.", lemma="ребёнок"),
        F("Она' рабо'тает в ___. (hospitals)", "больни'цах", ["больни'ц", "больни'цам", "больни'цами"], "After ц: -ах.", "She works in hospitals.", lemma="больница"),
        F("Мы живём в ___. (villages)", "деревня'х", ["дере'вень", "деревня'м", "деревня'ми"], "Stress moves: деревня'х.", "We live in villages.", lemma="деревня"),
        F("Мы бы'ли в ___ у друзе'й. (visiting)", "гостя'х", ["го'стях", "госте'й", "гостя'м"], "В гостя'х = visiting.", "We were visiting friends.", lemma="гость"),
        mc("Which ending do hard-stem nouns take in the prepositional plural?", ["-ах", "-ях", "-ам", "-ов"], "-ах", "-ах.", order=True),
        mc("Which ending do soft-stem nouns take in the prepositional plural?", ["-ях", "-ах", "-ям", "-ей"], "-ях", "-ях."),
    ],
)

# ---------------------------------------------------------------------------- 217
L217 = lesson(
    "In big cities, about our friends: adjectives in the prepositional plural",
    "Мы ча'сто говори'м о на'ших ста'рых друзья'х.",
    requires=["новый", "хороший", "весь", "этот", "большой"],
    cards=[
        card("-ых or -их",
             "Adjectives, ordinal numbers and adjectival pronouns end in -ых after a hard stem and in -их after a soft "
             "stem or after к, г, х, ж, ч, ш, щ. This is the same ending as the genitive plural, and the same for all "
             "genders.",
             tables=[table(
                 ["Nominative plural", "Prepositional plural"],
                 [["но'вые", "но'в{ых}"],
                  ["интере'сные", "интере'сн{ых}"],
                  ["больши'е", "больш{и'х}"],
                  ["ру'сские", "ру'сск{их}"],
                  ["хоро'шие", "хоро'ш{их}"],
                  ["мои'", "мо{и'х}"],
                  ["на'ши", "на'ш{их}"],
                  ["э'ти", "э'т{их}"],
                  ["те", "те{х}"],
                  ["все", "все{х}"],
                  ["его', её, их", "его', её, их"]])],
             examples=[
                 ex("В больши'х города'х мно'го люде'й.", "There are many people in big cities.", "В больши'х города'х"),
                 ex("Мы говори'м о на'ших друзья'х.", "We are talking about our friends.", "о на'ших друзья'х"),
                 ex("Он ду'мает обо всех пробле'мах.", "He thinks about all the problems.", "обо всех"),
             ]),
        card("Do not change: его, её, их",
             "The possessives его', её and их are indeclinable, so they stay the same in every case.",
             examples=[
                 ex("Мы говори'м об их де'тях.", "We are talking about their children.", "об их де'тях"),
                 ex("Я ду'маю о его' пробле'мах.", "I am thinking about his problems.", "о его' пробле'мах"),
                 ex("Он ча'сто вспомина'ет о тех днях.", "He often remembers those days.", "о тех днях"),
             ]),
    ],
    verify=(vf("новый", "новых") + vf("интересный", "интересных") + vf("большой", "больших") + vf("русский", "русских")
            + vf("хороший", "хороших") + vf("мой", "моих") + vf("наш", "наших") + vf("этот", "этих") + vf("тот", "тех")
            + vf("весь", "всех") + vf("город", "городах") + vf("друг", "друзьях") + vf("ребёнок", "детях")
            + vf("день", "днях") + vf("проблема", "проблемах") + vf("вспоминать", "вспоминает")),
    exercises=[
        F("В ___ города'х мно'го люде'й. (big)", "больши'х", ["больши'е", "больши'м", "больши'ми"], "After ш/щ/ж/ч/к/г/х: -их; here the stem is big-: больши'х.", "There are many people in big cities.", lemma="большой"),
        F("Мы говори'м о ___ друзья'х. (our)", "на'ших", ["на'ши", "на'шим", "на'шими"], "Prepositional plural: на'ших.", "We are talking about our friends.", lemma="наш"),
        F("Он ча'сто вспомина'ет о ___ днях. (those)", "тех", ["те", "тем", "те'ми"], "Те → тех.", "He often remembers those days.", lemma="тот"),
        F("Она' рабо'тает в ___ больни'цах. (Russian)", "ру'сских", ["ру'сские", "ру'сским", "ру'сскими"], "After к: -их.", "She works in Russian hospitals.", lemma="русский"),
        F("Мы говори'м об ___ де'тях. (their)", "их", ["им", "и'ми", "них"], "Их never changes.", "We are talking about their children."),
        F("Он ду'мает обо ___. (all)", "всех", ["все", "всем", "все'ми"], "Все → всех.", "He is thinking about everyone.", lemma="весь"),
        F("Мы живём в ___ райо'нах. (new)", "но'вых", ["но'вые", "но'вым", "но'выми"], "Hard stem: -ых.", "We live in new districts.", lemma="новый"),
        mc("Which ending do adjectives take after ш in the prepositional plural?", ["-их", "-ых", "-ам", "-ими"], "-их", "-их after ш.", order=True),
        mc("What happens to его', её and их in the prepositional plural?", ["nothing", "they take -х", "they take -ми", "they take -м"], "nothing", "Indeclinable."),
    ],
)

# ---------------------------------------------------------------------------- 218
L218 = lesson(
    "She is young and beautiful: short-form adjectives",
    "Э'та же'нщина молода' и краси'ва.",
    requires=["красивый", "молодой", "умный", "богатый", "счастливый"],
    cards=[
        card("How the short form is built",
             "Remove the ending of the full form. The masculine has no ending; the feminine adds -а; the neuter -о; "
             "the plural -ы (or -и after к, г, х, ж, ч, ш, щ).",
             tables=[table(
                 ["Full form", "Masc.", "Fem.", "Neut.", "Plural"],
                 [["краси'вый", "краси'в", "краси'в{а}", "краси'в{о}", "краси'в{ы}"],
                  ["молодо'й", "мо'лод", "молод{а'}", "мо'лодо", "мо'лоды"],
                  ["бога'тый", "бога'т", "бога'т{а}", "бога'т{о}", "бога'т{ы}"],
                  ["счастли'вый", "сча'стлив", "сча'стлив{а}", "сча'стлив{о}", "сча'стлив{ы}"],
                  ["у'мный", "умён", "умн{а'}", "умн{о'}", "умн{ы'}"]])],
             examples=[
                 ex("Э'та же'нщина молода' и краси'ва.", "This woman is young and beautiful.", "молода' и краси'ва"),
                 ex("Э'ти лю'ди бога'ты.", "These people are rich.", "бога'ты"),
                 ex("Мой брат сча'стлив.", "My brother is happy.", "сча'стлив"),
             ]),
        card("They are predicates only",
             "A short adjective is never used in front of a noun. It stays at the end of the clause as part of the "
             "predicate. In the present tense there is no verb «быть», and the adjective agrees with the subject "
             "in gender and number.",
             examples=[
                 ex("Э'то окно' краси'во.", "This window is beautiful.", "краси'во"),
                 ex("Моя' мать о'чень умна'.", "My mother is very clever.", "умна'"),
                 ex("Ты, Ва'ня, прав.", "You are right, Vanya.", "прав"),
                 ex("Мы о'чень ра'ды вас ви'деть.", "We are very glad to see you.", "ра'ды"),
             ]),
    ],
    verify=(vf("красивый", "красив", "красива", "красиво", "красивы") + vf("молодой", "молод", "молода", "молоды")
            + vf("богатый", "богат", "богаты") + vf("счастливый", "счастлив", "счастлива", "счастливы")
            + vf("умный", "умён", "умна", "умно", "умны") + vf("рад", "рад", "рады") + vf("прав", "прав")),
    exercises=[
        F("Анна ___ и краси'ва. (young)", "молода'", ["мо'лод", "мо'лодо", "мо'лоды"], "Feminine: молода'.", "Anna is young and beautiful."),
        F("Э'ти лю'ди ___. (happy)", "сча'стливы", ["сча'стлив", "сча'стлива", "сча'стливо"], "Plural: сча'стливы.", "These people are happy."),
        F("Он о'чень ___. (rich)", "бога'т", ["бога'та", "бога'то", "бога'ты"], "Masculine: no ending.", "He is very rich."),
        F("Мы о'чень ___ вас ви'деть. (glad)", "ра'ды", ["рад", "ра'да", "ра'до"], "Plural: ра'ды.", "We are very glad to see you."),
        F("Ты, Ва'ня, ___! (right)", "прав", ["права'", "пра'во", "пра'вы"], "Masculine: прав.", "You are right, Vanya!"),
        F("Э'то окно' ___. (beautiful)", "краси'во", ["краси'в", "краси'ва", "краси'вы"], "Neuter: краси'во.", "This window is beautiful."),
        F("Моя' мать о'чень ___. (clever)", "умна'", ["умён", "умно'", "умны'"], "Feminine: умна'.", "My mother is very clever."),
        mc("Short-form adjectives are used only as...", ["predicates", "modifiers before nouns", "adverbs", "nouns"], "predicates", "They stand at the end of the clause."),
        mc("What is the masculine short form of краси'вый?", ["краси'в", "краси'ва", "краси'во", "краси'вы"], "краси'в", "Zero ending."),
    ],
)

# ---------------------------------------------------------------------------- 219
L219 = lesson(
    "Busy, sick, too big: fleeting vowels and велик, мал",
    "Я сего'дня за'нят, а ма'ма больна'.",
    requires=["больной", "здоровый", "довольный", "полезный", "вредный"],
    cards=[
        card("A vowel appears in the masculine",
             "When the stem ends in two consonants, the masculine short form has no ending, so a vowel slips in "
             "between them: usually о before к, and е (or ё) before н.",
             tables=[table(
                 ["Full form", "Masculine", "Feminine", "Plural"],
                 [["у'зкий", "у'зок", "узка'", "узки'"],
                  ["коро'ткий", "ко'роток", "коротка'", "коротки'"],
                  ["больно'й", "бо'лен", "больна'", "больны'"],
                  ["дово'льный", "дово'лен", "дово'льна", "дово'льны"],
                  ["поле'зный", "поле'зен", "поле'зна", "поле'зны"],
                  ["вре'дный", "вре'ден", "вредна'", "вре'дны"],
                  ["здоро'вый", "здоро'в", "здоро'ва", "здоро'вы"],
                  ["занято'й", "за'нят", "занята'", "за'няты"],
                  ["гото'вый", "гото'в", "гото'ва", "гото'вы"]])],
             examples=[
                 ex("Я сего'дня за'нят, а ма'ма больна'.", "I am busy today, and Mom is sick.", "за'нят"),
                 ex("Э'то лека'рство поле'зно.", "This medicine is good for you.", "поле'зно"),
                 ex("Кури'ть вре'дно.", "Smoking is bad for you.", "вре'дно"),
             ]),
        card("Too big, too small: вели'к and мал",
             "Большо'й and ма'ленький have no short forms of their own. Instead the short forms of вели'кий and ма'лый "
             "are used, and they mean “too big” and “too small” for a particular person.",
             tables=[table(
                 ["Meaning", "Masc.", "Fem.", "Neut.", "Plural"],
                 [["too big", "вели'к", "велика'", "велико'", "велики'"],
                  ["too small", "мал", "мала'", "мало'", "малы'"]])],
             examples=[
                 ex("Э'ти боти'нки мне велики'.", "These shoes are too big for me.", "велики'"),
                 ex("Э'то пла'тье мне мало'.", "This dress is too small for me.", "мало'"),
                 ex("Э'та ку'ртка тебе' велика'.", "This jacket is too big for you.", "велика'"),
             ]),
    ],
    verify=(vf("узкий", "узок", "узка", "узки") + vf("короткий", "короток", "коротка", "коротки")
            + vf("больной", "болен", "больна", "больны") + vf("довольный", "доволен", "довольна", "довольны")
            + vf("полезный", "полезен", "полезна", "полезны") + vf("вредный", "вреден", "вредна", "вредны")
            + vf("здоровый", "здоров", "здорова", "здоровы") + vf("занятый", "занят", "занята", "заняты")
            + vf("готовый", "готов", "готова", "готовы") + vf("великий", "велик", "велика", "велико", "велики")
            + vf("малый", "мал", "мала", "мало", "малы") + vf("ботинок", "ботинки") + vf("курить", "курить")),
    exercises=[
        F("Сего'дня я о'чень ___. (busy)", "за'нят", ["занята'", "за'нято", "за'няты"], "Masculine: за'нят.", "I am very busy today."),
        F("Ма'ма ___ уже' три дня. (sick)", "больна'", ["бо'лен", "больно'", "больны'"], "Feminine: больна'.", "Mom has been sick for three days."),
        F("Э'то лека'рство ___ для здоро'вья. (good for you)", "поле'зно", ["поле'зен", "поле'зна", "поле'зны"], "Neuter: поле'зно.", "This medicine is good for your health."),
        F("Кури'ть ___. (is harmful)", "вре'дно", ["вре'ден", "вредна'", "вре'дны"], "With an infinitive: neuter.", "Smoking is harmful."),
        F("Э'ти боти'нки мне ___. (too big)", "велики'", ["вели'к", "велика'", "велико'"], "Plural: велики'.", "These shoes are too big for me."),
        F("Э'то пла'тье мне ___. (too small)", "мало'", ["мал", "мала'", "малы'"], "Neuter: мало'.", "This dress is too small for me."),
        F("Э'та ку'ртка тебе' ___. (too big)", "велика'", ["вели'к", "велико'", "велики'"], "Feminine: велика'.", "This jacket is too big for you."),
        F("Ма'ма ___ мои'ми результа'тами. (pleased)", "дово'льна", ["дово'лен", "дово'льно", "дово'льны"], "Feminine: дово'льна.", "Mom is pleased with my results."),
        mc("What is the masculine short form of у'зкий?", ["у'зок", "у'зка", "у'зко", "узки'"], "у'зок", "A vowel is inserted: у'зок.", order=True),
        mc("Which short form means “too big”?", ["вели'к", "мал", "бо'лен", "за'нят"], "вели'к", "Вели'к = too big."),
    ],
)

# ---------------------------------------------------------------------------- 220
L220 = lesson(
    "A beautiful girl, so beautiful today: short or full?",
    "Ты так краси'ва в э'том пла'тье!",
    requires=["известный", "свободный", "готовый", "рад", "здоровый"],
    cards=[
        card("Full form: a lasting quality; short form: a particular case",
             "The full form describes what something is like in general and can stand in front of a noun. The short "
             "form says what a person or thing is like right now, or in a particular situation, and is common after "
             "как, так, слишком and о'чень.",
             tables=[table(
                 ["Full form", "Short form"],
                 [["Э'то краси'вая де'вушка.", "Ты так краси'ва в э'том пла'тье!"],
                  ["Он молодо'й челове'к.", "Он сли'шком мо'лод для э'той рабо'ты."],
                  ["У неё больно'й ребёнок.", "Ребёнок бо'лен, поэ'тому он до'ма."],
                  ["Э'то здоро'вый мужчи'на.", "Сла'ва Бо'гу, он здоро'в!"],
                  ["Э'то поле'зный сове'т.", "Э'тот сове'т поле'зен."]])],
             examples=[
                 ex("Он сли'шком мо'лод для э'той рабо'ты.", "He is too young for this job.", "мо'лод"),
                 ex("Ребёнок бо'лен, поэ'тому он до'ма.", "The child is sick, so he is at home.", "бо'лен"),
                 ex("Вы гото'вы?", "Are you ready?", "гото'вы"),
             ]),
        card("Words that have only a short form",
             "A few adjectives exist only in the short form, such as рад (glad), до'лжен (must) and прав (right). "
             "Not every adjective has a short form: colors and materials do not, and neither do большо'й or ма'ленький.",
             examples=[
                 ex("Я рад вас ви'деть.", "I am glad to see you.", "рад"),
                 ex("Вы совсе'м прав.", "You are absolutely right.", "прав"),
                 ex("Он до'лжен позвони'ть ма'ме.", "He must call his mother.", "до'лжен"),
             ]),
    ],
    verify=(vf("красивый", "красива") + vf("молодой", "молод") + vf("больной", "болен") + vf("здоровый", "здоров")
            + vf("полезный", "полезный", "полезен") + vf("готовый", "готовы") + vf("рад", "рад") + vf("прав", "прав")
            + vf("должен", "должен") + vf("совет", "совет") + vf("платье", "платье")),
    exercises=[
        F("Э'то ___ де'вушка. (beautiful)", "краси'вая", ["краси'ва", "краси'вый", "краси'во"], "Before a noun: full form.", "This is a beautiful girl."),
        F("Ты так ___ в э'том пла'тье! (beautiful)", "краси'ва", ["краси'вая", "краси'вую", "краси'вой"], "After так: short form.", "You look so beautiful in this dress!"),
        F("Он сли'шком ___ для э'той рабо'ты. (young)", "мо'лод", ["молода'", "мо'лодо", "мо'лоды"], "After сли'шком: short masculine.", "He is too young for this job."),
        F("Арту'р — ___ челове'к. (healthy)", "здоро'вый", ["здоро'в", "здоро'ва", "здоро'во"], "Before a noun: full form.", "Artur is a healthy person.", lemma="здоровый"),
        F("Вы ___? (ready)", "гото'вы", ["гото'в", "гото'ва", "гото'во"], "Plural вы: гото'вы.", "Are you ready?"),
        F("Я ___ вас ви'деть. (glad)", "рад", ["ра'да", "ра'ды", "ра'до"], "Masculine: рад.", "I am glad to see you."),
        F("Э'тот сове'т ___. (useful)", "поле'зен", ["поле'зный", "поле'зна", "поле'зны"], "Predicate: short form.", "This advice is useful."),
        mc("Which form can stand in front of a noun?", ["the full form", "the short form", "both", "neither"], "the full form", "Only the full form modifies a noun."),
        mc("Which adjective has only a short form?", ["рад", "краси'вый", "но'вый", "бога'тый"], "рад", "Рад exists only as a short form."),
    ],
)

# ---------------------------------------------------------------------------- 221
L221 = lesson(
    "I feel sick, I have chills: impersonal verbs of the body",
    "Меня' тошни'т, и меня' зноби'т.",
    requires=["голова", "живот", "сердце", "настроение", "чувствовать"],
    cards=[
        card("The person is the object, not the subject",
             "Some verbs describe how the body feels without any subject. The verb is in the third person singular (neuter "
             "in the past tense), and the person who feels it is in the accusative or dative.",
             tables=[table(
                 ["Russian", "English"],
                 [["Меня' зноби'т.", "I have chills."],
                  ["Меня' тошни'т.", "I feel nauseous."],
                  ["Мне не здоро'вится.", "I am not feeling well."],
                  ["Мне хо'чется спать.", "I feel like sleeping."],
                  ["Его' зноби'ло всю ночь.", "He had chills all night."],
                  ["Её тошни'ло.", "She felt nauseous."]])],
             examples=[
                 ex("Меня' тошни'т.", "I feel nauseous.", "Меня' тошни'т"),
                 ex("Мне не здоро'вится.", "I am not feeling well.", "не здоро'вится"),
                 ex("Ма'ше хо'чется спать.", "Masha feels sleepy.", "хо'чется"),
             ]),
        card("Starting suddenly: за-",
             "The prefix за- shows that the feeling has just begun: зазноби'ть, затошни'ть.",
             examples=[
                 ex("Ве'ру затошни'ло в авто'бусе.", "Vera started feeling nauseous on the bus.", "затошни'ло"),
                 ex("Вдруг меня' зазноби'ло.", "Suddenly I started shivering.", "зазноби'ло"),
                 ex("Его' всю ночь зноби'ло.", "He had chills all night.", "зноби'ло"),
             ]),
    ],
    verify=(vf("знобить", "знобит", "знобило") + vf("тошнить", "тошнит", "тошнило") + vf("затошнить", "затошнило")
            + vf("зазнобить", "зазнобило") + vf("здороваться", "здороваться") + vf("хотеться", "хочется")
            + vf("спать", "спать") + vf("автобус", "автобусе") + vf("ночь", "ночь")),
    exercises=[
        F("Меня' ___. (I feel nauseous)", "тошни'т", ["тошни'ло", "тошни'ла", "тошни'л"], "Present, neuter: тошни'т.", "I feel nauseous."),
        F("Вчера' её ___ весь день. (felt nauseous)", "тошни'ло", ["тошни'т", "тошни'ла", "тошни'л"], "Past, neuter: тошни'ло.", "Yesterday she felt nauseous all day."),
        F("Вдруг Ве'ру ___ в авто'бусе. (started feeling nauseous)", "затошни'ло", ["затошни'т", "затошни'ла", "затошни'л"], "За- + neuter past.", "Suddenly Vera felt nauseous on the bus."),
        F("Его' всю ночь ___. (had chills)", "зноби'ло", ["зноби'л", "зноби'ла", "зноби'т"], "Past, neuter.", "He had chills all night."),
        F("Мне ___. (I am not feeling well)", "не здоро'вится", ["не здоро'вишься", "не здоро'вятся", "не здоро'вился"], "Third person singular.", "I am not feeling well."),
        F("Ма'ше ___ спать. (feels like)", "хо'чется", ["хо'чет", "хочу'", "хотя'т"], "Хо'чется + dative.", "Masha feels like sleeping."),
        mc("In «Меня' тошни'т» the person who feels sick is in the...", ["accusative", "nominative", "genitive", "instrumental"], "accusative", "Меня' = accusative."),
        mc("What does the past tense of an impersonal verb end in?", ["-ло", "-л", "-ла", "-ли"], "-ло", "Neuter: тошни'ло.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 222
L222 = lesson(
    "It got dark, it got colder: impersonal verbs of nature and forces",
    "Зимо'й о'чень ра'но темне'ет.",
    requires=["ветер", "дождь", "снег", "вечер", "хватать"],
    cards=[
        card("Nature acts on its own",
             "Weather and the time of day are expressed with impersonal verbs: no subject, a verb in the third person "
             "singular or neuter past.",
             tables=[table(
                 ["Russian", "English"],
                 [["темне'ет, стемне'ло", "it gets dark, it got dark"],
                  ["света'ет", "dawn is breaking"],
                  ["вечере'ет", "evening is coming"],
                  ["холода'ет, похолода'ло", "it is getting colder, it got colder"],
                  ["потемне'ло", "it grew dark"]])],
             examples=[
                 ex("Зимо'й о'чень ра'но темне'ет.", "In winter it gets dark very early.", "темне'ет"),
                 ex("На у'лице похолода'ло.", "It got colder outside.", "похолода'ло"),
                 ex("Вдруг потемне'ло.", "Suddenly it grew dark.", "потемне'ло"),
             ]),
        card("Outside forces",
             "When something is done to a thing by a force that we do not name, Russian also uses an impersonal verb. "
             "The affected thing is in the accusative, and the force is in the instrumental.",
             tables=[table(
                 ["Russian", "English"],
                 [["Подва'л затопи'ло.", "The basement flooded."],
                  ["Доро'гу занесло' сне'гом.", "The road was covered with snow."],
                  ["Окно' откры'ло ве'тром.", "The window was blown open by the wind."]])],
             examples=[
                 ex("Подва'л затопи'ло дождём.", "The basement was flooded by the rain.", "затопи'ло"),
                 ex("Доро'гу занесло' сне'гом.", "The road was buried in snow.", "занесло'"),
             ]),
        card("Not enough: не хвата'ет",
             "Хвата'ть with a negative means “to be short of”: the thing that is lacking is in the genitive, and the person "
             "who lacks it is in the dative.",
             examples=[
                 ex("Мне не хвата'ет вре'мени.", "I do not have enough time.", "не хвата'ет"),
                 ex("Нам не хвата'ет де'нег.", "We do not have enough money.", "не хвата'ет де'нег"),
                 ex("В больни'цах не хвата'ет враче'й.", "There is a shortage of doctors in the hospitals.", "не хвата'ет враче'й"),
             ]),
    ],
    verify=(vf("темнеть", "темнеет") + vf("стемнеть", "стемнело") + vf("холодать", "холодает")
            + vf("похолодать", "похолодало") + vf("потемнеть", "потемнело") + vf("затопить", "затопило")
            + vf("занести", "занесло") + vf("открыть", "открыло") + vf("хватать", "хватает")
            + vf("снег", "снегом") + vf("ветер", "ветром") + vf("дождь", "дождём") + vf("подвал", "подвал")
            + vf("время", "времени") + vf("деньги", "денег") + vf("врач", "врачей") + vf("больница", "больницах")),
    exercises=[
        F("Зимо'й о'чень ра'но ___. (it gets dark)", "темне'ет", ["темне'ют", "темне'ла", "темне'ть"], "Impersonal, present.", "In winter it gets dark very early."),
        F("На у'лице ___. (it got colder)", "похолода'ло", ["похолода'ла", "похолода'л", "похолода'ют"], "Impersonal, neuter past.", "It got colder outside."),
        F("Вдруг ___. (it grew dark)", "потемне'ло", ["потемне'ла", "потемне'л", "потемне'ют"], "Impersonal, neuter past.", "Suddenly it grew dark."),
        F("Подва'л ___ дождём. (flooded)", "затопи'ло", ["затопи'ла", "затопи'л", "затопи'ли"], "Impersonal, neuter past.", "The basement was flooded by the rain."),
        F("Доро'гу ___ сне'гом. (was snowed over)", "занесло'", ["занесла'", "занёс", "занесли'"], "Impersonal, neuter past.", "The road was covered with snow."),
        F("Нам не ___ де'нег. (is enough)", "хвата'ет", ["хвата'ют", "хвата'ть", "хвата'я"], "Third person singular.", "We do not have enough money."),
        F("Мне не хвата'ет ___. (time)", "вре'мени", ["вре'мя", "вре'менем", "времена'"], "Genitive.", "I do not have enough time.", lemma="время"),
        mc("Which verb means “evening is coming”?", ["вечере'ет", "света'ет", "темне'ет", "холода'ет"], "вечере'ет", "Evening: вечере'ет."),
        mc("What case follows не хвата'ет for the thing that is lacking?", ["genitive", "accusative", "dative", "instrumental"], "genitive", "Не хвата'ет + genitive."),
    ],
)

# ---------------------------------------------------------------------------- 223
L223 = lesson(
    "Let him call, may you be happy: the particle пусть",
    "Пусть он мне позвони'т. Пусть все бу'дут здоро'вы!",
    requires=["пусть", "здоровье", "счастливый", "друг", "жизнь"],
    cards=[
        card("Пусть + subject + verb",
             "Пусть is placed at the beginning of the sentence, followed by the subject and a verb in the present or "
             "future tense. It tells a third person to do something, or expresses a wish. The subject is usually "
             "he, she, they or a name.",
             tables=[table(
                 ["Russian", "English"],
                 [["Пусть он мне позвони'т.", "Have him call me."],
                  ["Пусть Ли'за вы'учит э'то пра'вило.", "Have Liza learn this rule."],
                  ["Пусть де'ти поигра'ют во дворе'.", "Let the children play in the yard."],
                  ["Пусть они' так бо'льше не де'лают.", "I don't want them to do that anymore."]])],
             examples=[
                 ex("Пусть он мне позвони'т.", "Have him call me.", "Пусть он мне позвони'т"),
                 ex("Пусть де'ти поигра'ют во дворе'.", "Let the children play in the yard.", "Пусть де'ти"),
             ]),
        card("Wishes and toasts",
             "Пусть also expresses good wishes in toasts, birthday greetings and holiday cards.",
             tables=[table(
                 ["Russian", "English"],
                 [["Пусть все бу'дут здоро'вы!", "May everyone be healthy!"],
                  ["Пусть тебе' повезёт!", "Good luck to you!"],
                  ["Пусть у вас всегда' бу'дет мно'го друзе'й!", "May you always have many friends!"],
                  ["Пусть сбу'дутся все твои' мечты'!", "May all your dreams come true!"]])],
             examples=[
                 ex("Пусть все бу'дут здоро'вы!", "May everyone be healthy!", "Пусть все бу'дут здоро'вы"),
                 ex("Пусть тебе' повезёт!", "Good luck to you!", "Пусть тебе' повезёт"),
                 ex("Пусть у вас всегда' бу'дет мно'го друзе'й!", "May you always have many friends!", "Пусть у вас всегда'"),
             ]),
    ],
    verify=(vf("позвонить", "позвонит") + vf("выучить", "выучит") + vf("поиграть", "поиграют") + vf("двор", "дворе")
            + vf("быть", "будут", "будет") + vf("здоровый", "здоровы") + vf("повезти", "повезёт")
            + vf("сбыться", "сбудутся") + vf("мечта", "мечты") + vf("друг", "друзей") + vf("правило", "правило")),
    exercises=[
        F("Пусть он ___ мне. (call)", "позвони'т", ["позвони'л", "позвони'ть", "позвони'ли"], "Present or future tense.", "Have him call me."),
        F("Пусть де'ти ___ на у'лице. (play)", "поигра'ют", ["поигра'ли", "поигра'ть", "поигра'л"], "Present or future tense.", "Let the children play outside."),
        F("Пусть все ___ здоро'вы! (be)", "бу'дут", ["бу'дет", "бы'ли", "быть"], "Все → бу'дут.", "May everyone be healthy!"),
        F("Пусть ___ повезёт! (you, informal)", "тебе'", ["тебя'", "тобо'й", "ты"], "Dative of ты: тебе'.", "Good luck to you!"),
        F("Пусть у вас ___ бу'дет мно'го друзе'й! (always)", "всегда'", ["никогда'", "ра'но", "далеко'"], "Всегда' = always.", "May you always have many friends!"),
        F("Пусть Ли'за ___ э'то пра'вило. (learn)", "вы'учит", ["вы'учила", "вы'учить", "вы'учи"], "Future tense.", "Have Liza learn this rule."),
        mc("What tense follows пусть?", ["present or future", "past only", "infinitive only", "imperative only"], "present or future", "Пусть + present or future."),
        mc("Which sentence means “May all your dreams come true!”?", ["Пусть сбу'дутся все твои' мечты'!", "Сбу'дутся все твои' мечты'.", "Все твои' мечты' сбыли'сь.", "Пусть все твои' мечты' сбыли'сь."], "Пусть сбу'дутся все твои' мечты'!", "A wish needs пусть."),
    ],
)

# ---------------------------------------------------------------------------- 224
L224 = lesson(
    "Review: the plural cases, short adjectives and health",
    "Мы говори'м о больны'х друзья'х, а врачи' лечат пациентов.",
    requires=["врач", "болеть", "пусть", "больной", "друг"],
    cards=[
        card("The plural, case by case",
             "You now have every plural case. Learn them as a set. Adjectives and pronouns always follow the noun.",
             tables=[table(
                 ["Case", "Nouns", "Adjectives"],
                 [["Nominative", "-ы, -и, -а, -я", "-ые, -ие"],
                  ["Genitive", "-ов, -ев, -ей, no ending, -ий", "-ых, -их"],
                  ["Dative", "-ам, -ям", "-ым, -им"],
                  ["Instrumental", "-ами, -ями", "-ыми, -ими"],
                  ["Prepositional", "-ах, -ях", "-ых, -их"]])],
             examples=[
                 ex("Мы говори'м о но'вых друзья'х.", "We talk about our new friends.", "о но'вых друзья'х"),
             ]),
        card("Health and short adjectives",
             "Remember the key forms: боли'т/боля'т for pain, the instrumental after заболе'ть, and the short forms "
             "бо'лен, больна', больны' for “is sick”.",
             examples=[
                 ex("У меня' боли'т го'рло, и я не здоро'в.", "My throat hurts and I am not well.", "не здоро'в"),
                 ex("Пусть все бу'дут здоро'вы!", "May everyone be healthy!", "бу'дут здоро'вы"),
             ]),
    ],
    verify=(vf("больной", "больны", "больных") + vf("друг", "друзьях") + vf("врач", "врачи") + vf("пациент", "пациентов")
            + vf("лечить", "лечат") + vf("болеть", "болит") + vf("здоровый", "здоров", "здоровы")),
    exercises=[
        F("Мы говори'м о ___ друзья'х. (sick)", "больны'х", ["больны'е", "больны'м", "больны'ми"], "Prepositional plural: -ых.", "We talk about our sick friends.", lemma="больной"),
        F("Врачи' лечат ___. (patients)", "пацие'нтов", ["пацие'нты", "пацие'нтам", "пацие'нтами"], "Accusative of animate = genitive plural.", "The doctors treat patients.", lemma="пациент"),
        F("Она' разгова'ривает с ___ врача'ми. (new)", "но'выми", ["но'вых", "но'вым", "но'вые"], "Instrumental plural.", "She talks with the new doctors.", lemma="новый"),
        F("Он рабо'тает в больши'х ___. (hospitals)", "больни'цах", ["больни'ц", "больни'цам", "больни'цами"], "Prepositional plural.", "He works in big hospitals.", lemma="больница"),
        F("Э'ти боти'нки мне ___. (too big)", "велики'", ["вели'к", "велика'", "велико'"], "Plural: велики'.", "These shoes are too big for me."),
        F("Он сли'шком ___ для э'той рабо'ты. (young)", "мо'лод", ["молода'", "мо'лодо", "мо'лоды"], "Short form after сли'шком.", "He is too young for this job."),
        F("Меня' ___ в авто'бусе. (felt nauseous)", "тошни'ло", ["тошни'т", "тошни'ла", "тошни'л"], "Impersonal past.", "I felt nauseous on the bus."),
        F("Зимо'й ра'но ___. (it gets dark)", "темне'ет", ["темне'ют", "темне'ла", "темне'ть"], "Impersonal.", "In winter it gets dark early."),
        F("Пусть все ___ здоро'вы! (be)", "бу'дут", ["бу'дет", "бы'ли", "быть"], "Пусть + future.", "May everyone be healthy!"),
        F("У него' ___ зу'бы. (hurt)", "боля'т", ["боли'т", "боле'ю", "боле'ть"], "Plural subject.", "His teeth hurt."),
        mc("Which case ending is -ах / -ях for nouns?", ["prepositional plural", "dative plural", "instrumental plural", "genitive plural"], "prepositional plural", "-ах, -ях."),
    ],
)

UNIT = unit("Unit 23: Health, the prepositional plural and short adjectives",
            [L213, L214, L215, L216, L217, L218, L219, L220, L221, L222, L223, L224])
