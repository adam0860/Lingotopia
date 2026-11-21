"""Unit 25: prefixed verbs of carrying and leading; чтобы; -то and -нибудь
(textbook module 6, lesson 33)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 235
L235 = lesson(
    "Bring and take away: приноси'ть, приводи'ть, привози'ть and у-",
    "Па'па привёз нам пода'рки из Москвы'.",
    requires=["принести", "привести", "приносить", "приводить", "привезти"],
    cards=[
        card("Prefix + motion verb = one aspect pair",
             "Just as ходи'ть / идти' become приходи'ть / прийти', the verbs of carrying and leading combine with "
             "directional prefixes. The rule is the same as before: prefix + habitual verb gives the imperfective, "
             "prefix + one-way verb gives the perfective. No spelling changes happen; only the stress moves.",
             tables=[table(
                 ["Imperfective", "Perfective", "Meaning"],
                 [["приноси'ть", "принести'", "to bring (carrying)"],
                  ["приводи'ть", "привести'", "to bring (leading a person on foot)"],
                  ["привози'ть", "привезти'", "to bring (by vehicle)"],
                  ["уноси'ть", "унести'", "to carry away"],
                  ["уводи'ть", "увести'", "to lead away"],
                  ["увози'ть", "увезти'", "to take away (by vehicle)"]])],
             examples=[
                 ex("Официа'нт принёс нам суп.", "The waiter brought us soup.", "принёс"),
                 ex("Па'па привёз нам пода'рки из Москвы'.", "Dad brought us presents from Moscow.", "привёз"),
                 ex("Я привёл дру'га на вечери'нку.", "I brought a friend to the party.", "привёл"),
             ]),
        card("Forms",
             "The perfective forms are built on the one-way stem. The я-form of приводи'ть and привози'ть is the "
             "same: привожу'.",
             tables=[table(
                 ["", "принести'", "привести'", "привезти'"],
                 [["я", "принесу'", "приведу'", "привезу'"],
                  ["он", "принёс", "привёл", "привёз"],
                  ["она'", "принесла'", "привела'", "привезла'"],
                  ["они'", "принесли'", "привели'", "привезли'"]])],
             examples=[
                 ex("Принеси' мне воды', пожа'луйста.", "Please bring me some water.", "Принеси'"),
                 ex("Ка'ждое ле'то он приво'зит нам фру'кты.", "Every summer he brings us fruit.", "приво'зит"),
             ]),
        card("Taking away",
             "The prefix у- is the opposite of при-: you carry, lead or drive somebody or something away from the "
             "place. Use из, с or от for ‘from where’ and в, на or к for ‘to where’.",
             examples=[
                 ex("Они' увезли' ме'бель на да'чу.", "They took the furniture away to the dacha.", "увезли'"),
                 ex("Ма'ма увела' ребёнка домо'й.", "Mom took the child home.", "увела'"),
                 ex("Официа'нт унёс таре'лки.", "The waiter took the plates away.", "унёс"),
             ]),
    ],
    verify=(vf("приносить", "приношу", "приносит") + vf("принести", "принесу", "принёс", "принесла", "принесли")
            + vf("приводить", "привожу") + vf("привести", "приведу", "привёл", "привела", "привели")
            + vf("привозить", "привожу", "привозит") + vf("привезти", "привезу", "привёз", "привезла", "привезли")
            + vf("унести", "унёс") + vf("увезти", "увезли") + vf("увести", "увела")
            + vf("подарок", "подарки") + vf("друг", "друга") + vf("вода", "воды") + vf("мебель", "мебель")
            + vf("тарелка", "тарелки") + vf("суп", "суп")),
    exercises=[
        F("Официа'нт ___ нам суп. (brought)", "принёс", ["привёл", "привёз", "унёс"], "A waiter carries a dish: принёс.", "The waiter brought us soup.", lemma="принести"),
        F("Па'па ___ нам пода'рки из Москвы'. (brought, by plane)", "привёз", ["принёс", "привёл", "увёз"], "Gifts from a distant city came by vehicle: привёз.", "Dad brought us presents from Moscow.", lemma="привезти"),
        F("Я ___ дру'га на вечери'нку. (brought, walking with him)", "привёл", ["принёс", "привёз", "увёл"], "A person you walk with: привёл.", "I brought a friend to the party.", lemma="привести"),
        F("Ма'ма ___ ребёнка домо'й. (led away)", "увела'", ["привела'", "унесла'", "увезла'"], "Away + on foot + feminine: увела'.", "Mom took the child home.", lemma="увести"),
        F("Они' ___ ме'бель на да'чу на грузовике'. (took away)", "увезли'", ["унесли'", "увели'", "привезли'"], "Away + by truck: увезли'.", "They took the furniture to the dacha on a truck.", lemma="увезти"),
        F("Принеси' мне ___, пожа'луйста. (some water)", "воды'", ["вода'", "воде'", "водо'й"], "Принести' a part of a substance: genitive.", "Please bring me some water.", lemma="вода"),
        F("Ка'ждое ле'то он ___ нам фру'кты. (brings, by car)", "приво'зит", ["приво'дит", "прино'сит", "привезёт"], "Habit + vehicle: привози'ть.", "Every summer he brings us fruit.", lemma="привозить"),
        mc("Which verb means ‘to bring a person on foot’?", ["привести'", "принести'", "привезти'", "унести'"], "привести'", "Привести' = bring (leading).", order=True),
        mc("What does the prefix у- add?", ["motion away", "motion toward", "motion across", "motion around"], "motion away", "У- = away from the speaker or the place."),
    ],
)

# ---------------------------------------------------------------------------- 236
L236 = lesson(
    "In and out: внести', вы'нести, ввести', вы'вести",
    "Вы'неси му'сор, пожа'луйста.",
    requires=["внести", "вынести", "ввести", "вывести", "выносить"],
    cards=[
        card("В- and вы-",
             "The prefix в- means ‘into’ and вы- means ‘out of’. They combine with the carrying and leading verbs just "
             "like при- and у-. Remember the one special rule: вы- is always stressed in the perfective.",
             tables=[table(
                 ["Imperfective", "Perfective", "Meaning"],
                 [["вноси'ть", "внести'", "to carry in"],
                  ["выноси'ть", "вы'нести", "to carry out"],
                  ["вводи'ть", "ввести'", "to lead in; to introduce"],
                  ["выводи'ть", "вы'вести", "to lead out, to walk (an animal)"],
                  ["ввози'ть", "ввезти'", "to import"],
                  ["вывози'ть", "вы'везти", "to export; to take out (by vehicle)"]])],
             examples=[
                 ex("Внеси' чемода'н в дом.", "Carry the suitcase into the house.", "Внеси'"),
                 ex("Вы'неси му'сор, пожа'луйста.", "Take out the trash, please.", "Вы'неси"),
                 ex("Я вы'веду соба'ку на прогу'лку.", "I will take the dog for a walk.", "вы'веду"),
             ]),
        card("Where is the stress?",
             "Compare the imperfective, with the stress on the ending, and the perfective, with the stress on вы-.",
             tables=[table(
                 ["Imperfective", "Perfective"],
                 [["выноси'ть, выношу', вы'носит", "вы'нести, вы'несу, вы'нес, вы'несла"],
                  ["выводи'ть, вывожу', выво'дит", "вы'вести, вы'веду, вы'вел, вы'вела"]])],
             examples=[
                 ex("Ка'ждый ве'чер он выно'сит му'сор.", "Every evening he takes out the trash.", "выно'сит"),
                 ex("Вчера' мы вы'несли ста'рые кре'сла на у'лицу.", "Yesterday we carried the old armchairs out to the street.", "вы'несли"),
             ]),
        card("Prepositions",
             "To say what you carry in, use в or на + accusative. To say what you carry out of, use из or с + genitive.",
             examples=[
                 ex("Они' внесли' дива'н в кварти'ру.", "They carried the sofa into the apartment.", "внесли' дива'н в кварти'ру"),
                 ex("Он вы'вел ребёнка из ко'мнаты.", "He led the child out of the room.", "из ко'мнаты"),
             ]),
    ],
    verify=(vf("вносить", "вносит") + vf("внести", "внесли") + vf("выносить", "выносит")
            + vf("вынести", "вынеси", "вынесу", "вынес", "вынесла", "вынесли") + vf("вводить", "вводит")
            + vf("ввести", "введу") + vf("вывести", "выведу", "вывел", "вывела") + vf("мусор", "мусор")
            + vf("собака", "собаку") + vf("кресло", "кресла") + vf("квартира", "квартиру") + vf("диван", "диван")
            + vf("комната", "комнаты") + vf("чемодан", "чемодан")),
    exercises=[
        F("___ чемода'н в дом. (carry in!)", "Внеси'", ["Вы'неси", "Принеси'", "Унеси'"], "В- = into: внести'.", "Carry the suitcase into the house.", lemma="внести"),
        F("___ му'сор, пожа'луйста. (take out!)", "Вы'неси", ["Внеси'", "Принеси'", "Вноси'"], "Вы- = out; imperative of the perfective.", "Take out the trash, please.", lemma="вынести"),
        F("Я ___ соба'ку на прогу'лку. (will take out)", "вы'веду", ["введу'", "приведу'", "вы'вожу"], "Perfective future of вы'вести.", "I will take the dog for a walk.", lemma="вывести"),
        F("Они' ___ дива'н в кварти'ру. (carried in)", "внесли'", ["вы'несли", "принесли'", "унесли'"], "В- = into.", "They carried the sofa into the apartment.", lemma="внести"),
        F("Вчера' мы ___ ста'рые кре'сла на у'лицу. (carried out)", "вы'несли", ["внесли'", "принесли'", "унесли'"], "Вы- = out.", "Yesterday we carried the old armchairs out to the street.", lemma="вынести"),
        F("Ка'ждый ве'чер он ___ му'сор. (takes out)", "выно'сит", ["вы'несет", "вно'сит", "выноси'ть"], "Habit: imperfective выноси'ть.", "Every evening he takes out the trash.", lemma="выносить"),
        mc("Where is the stress in the perfective with вы-?", ["on вы-", "on the root", "on the ending", "on the last syllable"], "on вы-", "Вы'нести, вы'вести, вы'нес."),
        mc("Which verb means ‘to carry in’?", ["внести'", "вы'нести", "принести'", "унести'"], "внести'", "Внести' = carry in.", order=True),
        mc("What is the masculine past of вы'нести?", ["вы'нес", "вы'нел", "вы'несла", "вы'несли"], "вы'нес", "Like нести': no -л."),
    ],
)

# ---------------------------------------------------------------------------- 237
L237 = lesson(
    "Across, back, a lift: перевести', отнести', отвезти', подвезти'",
    "Я переведу' ребёнка че'рез доро'гу.",
    requires=["перевести", "отнести", "доставить", "привезти", "привести"],
    cards=[
        card("More prefixes",
             "These prefixes behave as they do with other motion verbs.",
             tables=[table(
                 ["Imperfective", "Perfective", "Meaning"],
                 [["переводи'ть", "перевести'", "to take across (a street)"],
                  ["относи'ть", "отнести'", "to take (to a place, to someone)"],
                  ["отвози'ть", "отвезти'", "to drive someone to a destination"],
                  ["подвози'ть", "подвезти'", "to give a lift"],
                  ["довози'ть", "довезти'", "to take all the way"],
                  ["заводи'ть", "завести'", "to drop off on the way"]])],
             examples=[
                 ex("Я переведу' ребёнка че'рез доро'гу.", "I will take the child across the road.", "переведу'"),
                 ex("Отнеси' э'ту таре'лку на ку'хню.", "Take this plate to the kitchen.", "Отнеси'"),
                 ex("За'втра мне ну'жно отвезти' роди'телей в аэропо'рт.", "Tomorrow I must drive my parents to the airport.", "отвезти'"),
             ]),
        card("От- and за-",
             "От- often means returning something to its place or taking someone to a specific destination. За- means "
             "dropping somebody off on your way: Заведи' сестру' в де'тский сад.",
             examples=[
                 ex("Заведи' сестру' в де'тский сад по доро'ге в шко'лу.", "Drop your sister at kindergarten on the way to school.", "Заведи'"),
                 ex("Вчера' па'па подвёз меня' на рабо'ту.", "Yesterday Dad gave me a lift to work.", "подвёз"),
             ]),
        card("Parents and children",
             "Many situations have a typical verb:",
             tables=[table(
                 ["Situation", "Verb"],
                 [["leading a child across a busy road", "перевести' (че'рез доро'гу)"],
                  ["taking a plate to the kitchen", "отнести'"],
                  ["driving a guest to the airport", "отвезти'"],
                  ["giving a colleague a lift", "подвезти'"],
                  ["bringing a delivery to a client", "доста'вить"]])],
             examples=[
                 ex("Курье'р доста'вил посы'лку в о'фис.", "The courier delivered the package to the office.", "доста'вил"),
             ]),
    ],
    verify=(vf("переводить", "перевожу") + vf("перевести", "переведу") + vf("относить", "отношу")
            + vf("отнести", "отнеси") + vf("отвозить", "отвожу") + vf("отвезти", "отвезти")
            + vf("подвезти", "подвёз") + vf("завести", "заведи") + vf("доставить", "доставил")
            + vf("дорога", "дорогу") + vf("тарелка", "тарелку") + vf("кухня", "кухню") + vf("аэропорт", "аэропорт")
            + vf("сестра", "сестру") + vf("посылка", "посылку") + vf("офис", "офис") + vf("курьер", "курьер")),
    exercises=[
        F("Я ___ ребёнка че'рез доро'гу. (will take across)", "переведу'", ["приведу'", "отведу'", "заведу'"], "Пере- = across.", "I will take the child across the road.", lemma="перевести"),
        F("___ э'ту таре'лку на ку'хню. (take!)", "Отнеси'", ["Принеси'", "Вы'неси", "Внеси'"], "От- = take to its place.", "Take this plate to the kitchen.", lemma="отнести"),
        F("За'втра мне ну'жно ___ роди'телей в аэропо'рт. (to drive)", "отвезти'", ["отвести'", "отнести'", "привезти'"], "От- + везти' = drive to a destination.", "Tomorrow I must drive my parents to the airport.", lemma="отвезти"),
        F("Вчера' па'па ___ меня' на рабо'ту. (gave a lift)", "подвёз", ["привёз", "увёз", "вёз"], "Под- = a lift.", "Yesterday Dad gave me a lift to work.", lemma="подвезти"),
        F("___ сестру' в де'тский сад по доро'ге в шко'лу. (drop off!)", "Заведи'", ["Принеси'", "Вы'неси", "Отнеси'"], "За- = on the way.", "Drop your sister at kindergarten on the way to school.", lemma="завести"),
        F("Курье'р ___ посы'лку в о'фис. (delivered)", "доста'вил", ["подвёз", "отвёл", "принёс"], "Доста'вить = to deliver.", "The courier delivered the package to the office.", lemma="доставить"),
        mc("Which verb fits ‘take a child across the street’?", ["перевести'", "отвезти'", "внести'", "унести'"], "перевести'", "Пере- = across.", order=True),
        mc("‘Give a lift’ is:", ["подвезти'", "довезти'", "привезти'", "отвезти'"], "подвезти'", "Под-: pick up on the way.", order=True),
        mc("What does the prefix от- often show?", ["returning to its place; to a destination", "going in", "going around", "going up"], "returning to its place; to a destination", "Отнести', отвезти'."),
    ],
)

# ---------------------------------------------------------------------------- 238
L238 = lesson(
    "Give an example, spend time, postpone: figurative uses",
    "Мы провели' выходны'е на да'че.",
    requires=["пример", "провести", "перевести", "перенести", "ввести"],
    cards=[
        card("The prefixes take on new meanings",
             "Like перевести' статью' (to translate an article), many prefixed carrying and leading verbs have abstract "
             "meanings. Learn them as fixed phrases.",
             tables=[table(
                 ["Phrase", "English"],
                 [["приводи'ть / привести' приме'р", "to give an example"],
                  ["проводи'ть / провести' вре'мя", "to spend time"],
                  ["проводи'ть / провести' уро'к", "to hold a lesson"],
                  ["переводи'ть / перевести' текст", "to translate a text"],
                  ["переноси'ть / перенести' встре'чу", "to postpone a meeting"],
                  ["вводи'ть / ввести' пра'вило", "to introduce a rule"],
                  ["заводи'ть / завести' соба'ку", "to get a dog"],
                  ["заводи'ть / завести' маши'ну", "to start a car"]])],
             examples=[
                 ex("Приведи' приме'р, пожа'луйста.", "Give an example, please.", "Приведи' приме'р"),
                 ex("Мы провели' выходны'е на да'че.", "We spent the weekend at the dacha.", "провели'"),
             ]),
        card("Postponing and introducing",
             "Перенести' means to move to a different time. The new time follows на + accusative: перенести' встре'чу на "
             "за'втра.",
             examples=[
                 ex("Они' перенесли' встре'чу на за'втра.", "They postponed the meeting until tomorrow.", "перенесли' встре'чу"),
                 ex("В шко'ле ввели' но'вое пра'вило.", "A new rule was introduced at school.", "ввели' но'вое пра'вило"),
             ]),
        card("Pets and cars",
             "Завести' has two everyday meanings. With an animal it means ‘to get one’. With a car or an engine it "
             "means ‘to start’.",
             examples=[
                 ex("Мы завели' соба'ку.", "We got a dog.", "завели' соба'ку"),
                 ex("Я не могу' завести' маши'ну.", "I cannot start the car.", "завести' маши'ну"),
             ]),
    ],
    verify=(vf("приводить", "привожу") + vf("привести", "приведи") + vf("пример", "пример")
            + vf("провести", "провели") + vf("проводить", "провожу") + vf("время", "время")
            + vf("урок", "урок") + vf("перевести", "перевёл") + vf("переводить", "перевожу")
            + vf("текст", "текст") + vf("перенести", "перенесли") + vf("переносить", "переношу")
            + vf("встреча", "встречу") + vf("ввести", "ввели") + vf("правило", "правило")
            + vf("завести", "завели") + vf("собака", "собаку") + vf("машина", "машину") + vf("дача", "даче")
            + vf("выходной", "выходные")),
    exercises=[
        F("___ приме'р, пожа'луйста. (give)", "Приведи'", ["Принеси'", "Вы'веди", "Переведи'"], "Привести' приме'р.", "Give an example, please.", lemma="привести"),
        F("Мы ___ выходны'е на да'че. (spent)", "провели'", ["перенесли'", "привели'", "ввели'"], "Провести' вре'мя.", "We spent the weekend at the dacha.", lemma="провести"),
        F("Они' ___ встре'чу на за'втра. (postponed)", "перенесли'", ["принесли'", "провели'", "ввели'"], "Перенести' встре'чу.", "They postponed the meeting until tomorrow.", lemma="перенести"),
        F("В шко'ле ___ но'вое пра'вило. (introduced)", "ввели'", ["привели'", "перевели'", "завели'"], "Ввести' пра'вило.", "A new rule was introduced at the school.", lemma="ввести"),
        F("Мы ___ соба'ку. (got)", "завели'", ["ввели'", "привели'", "увели'"], "Завести' соба'ку.", "We got a dog.", lemma="завести"),
        F("Он ___ текст с англи'йского на ру'сский. (translated)", "перевёл", ["перенёс", "провёл", "привёл"], "Перевести' текст.", "He translated the text from English into Russian.", lemma="перевести"),
        mc("‘To spend time’ is:", ["провести' вре'мя", "перевести' вре'мя", "ввести' вре'мя", "принести' вре'мя"], "провести' вре'мя", "Про- here: ‘through’.", order=True),
        mc("‘To postpone a meeting’ is:", ["перенести' встре'чу", "привести' встре'чу", "унести' встре'чу", "вынести' встре'чу"], "перенести' встре'чу", "Пере- = to move across to another time.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 239
L239 = lesson(
    "I want you to come: хочу', что'бы ты пришёл",
    "Я хочу', что'бы ты пришёл ко мне.",
    requires=["хотеть", "чтобы", "прийти", "помогать", "позвонить"],
    cards=[
        card("Same subject: infinitive",
             "When the person who wants and the person who acts are the same, Russian uses an infinitive, just like "
             "English: I want to go.",
             examples=[
                 ex("Я хочу' пойти' в кино'.", "I want to go to the cinema.", "хочу' пойти'"),
             ]),
        card("Different subject: что'бы + past tense",
             "When someone wants another person to act, the second verb goes into the past tense after что'бы. "
             "The past tense here does not point to the past. It only shows a wish: the time is decided by the context. "
             "The conjunction что'бы is not translated: ‘I want you to come’.",
             tables=[table(
                 ["Same subject", "Different subject"],
                 [["Я хочу' прийти'.", "Я хочу', что'бы ты пришёл."],
                  ["Мы хоти'м позвони'ть.", "Мы хоти'м, что'бы он позвони'л."],
                  ["Она' хо'чет помо'чь.", "Она' хо'чет, что'бы мы помогли'."]])],
             examples=[
                 ex("Я хочу', что'бы ты пришёл ко мне.", "I want you to come to see me.", "что'бы ты пришёл"),
                 ex("Ма'ма хо'чет, что'бы мы позвони'ли ба'бушке.", "Mom wants us to call Grandma.", "что'бы мы позвони'ли"),
             ]),
        card("The verb agrees with the subject",
             "The past-tense verb after что'бы agrees with its own subject in gender and number.",
             tables=[table(
                 ["Subject", "Example"],
                 [["ты (m.)", "Я хочу', что'бы ты пришёл."],
                  ["ты (f.)", "Я хочу', что'бы ты пришла'."],
                  ["вы", "Я хочу', что'бы вы пришли'."],
                  ["они'", "Я хочу', что'бы они' пришли'."]])],
             examples=[
                 ex("Она' не хо'чет, что'бы мы уходи'ли.", "She does not want us to leave.", "что'бы мы уходи'ли"),
             ]),
    ],
    verify=(vf("хотеть", "хочу", "хочет", "хотим") + vf("прийти", "пришёл", "пришла", "пришли")
            + vf("позвонить", "позвонили", "позвонил") + vf("помочь", "помочь", "помогли")
            + vf("мама", "мама") + vf("бабушка", "бабушке") + vf("кино", "кино") + vf("пойти", "пойти")
            + vf("уходить", "уходили")),
    exercises=[
        F("Я хочу' ___ домо'й. (go, I myself)", "пойти'", ["пошёл", "пошла'", "пойду'"], "Same subject: infinitive.", "I want to go home.", lemma="пойти"),
        F("Я хочу', что'бы ты ___ ко мне. (came, m.)", "пришёл", ["прийти'", "придёшь", "приходи'"], "Different subject: что'бы + past.", "I want you to come to me.", lemma="прийти"),
        F("Ма'ма хо'чет, что'бы мы ___ ба'бушке. (called)", "позвони'ли", ["позвони'ть", "позвоним", "позвони'"], "Plural past.", "Mom wants us to call Grandma.", lemma="позвонить"),
        F("Она' не хо'чет, что'бы мы ___. (left)", "уходи'ли", ["уходи'ть", "уйдём", "уходи'м"], "Different subject: что'бы + past.", "She does not want us to leave.", lemma="уходить"),
        F("Я хочу', что'бы вы ___ мне. (helped)", "помогли'", ["помо'чь", "помо'жете", "помога'ть"], "Plural past: помогли'.", "I want you to help me.", lemma="помочь"),
        F("Ма'ма хо'чет ___ ба'бушке. (to call, she herself)", "позвони'ть", ["позвони'ла", "позвони'ли", "позвони'л"], "Same subject: infinitive.", "Mom wants to call Grandma.", lemma="позвонить"),
        mc("Which form follows что'бы when the subject changes?", ["the past tense", "the infinitive", "the present tense", "the imperative"], "the past tense", "Что'бы + past."),
        mc("Does the past tense after что'бы refer to the past?", ["no, only to the wish", "yes, always", "only in the plural", "only for women"], "no, only to the wish", "The time comes from the context."),
    ],
)

# ---------------------------------------------------------------------------- 240
L240 = lesson(
    "Ask, advise, demand: проси'ть, сове'товать, тре'бовать, приказа'ть",
    "Врач посове'товал, что'бы я отдыха'л.",
    requires=["просить", "советовать", "требовать", "приказать", "предлагать"],
    cards=[
        card("Verbs that go with что'бы",
             "After verbs of asking, advising, demanding and ordering, what you want someone to do can be expressed "
             "with что'бы + past tense. With most of these verbs you can also use an infinitive, as in English.",
             tables=[table(
                 ["Verb", "With an infinitive", "With что'бы"],
                 [["проси'ть", "Я прошу' тебя' позвони'ть.", "Я прошу', что'бы ты позвони'л."],
                  ["сове'товать", "Врач сове'тует мне отдыха'ть.", "Врач сове'тует, что'бы я отдыха'л."],
                  ["приказа'ть", "Он приказа'л нам уйти'.", "Он приказа'л, что'бы мы ушли'."],
                  ["тре'бовать", "—", "Я тре'бую, что'бы вы молча'ли."],
                  ["сказа'ть", "—", "Ма'ма сказа'ла, что'бы мы шли домо'й."]])],
             examples=[
                 ex("Ма'ма попроси'ла меня' купи'ть хлеб.", "Mom asked me to buy bread.", "попроси'ла меня' купи'ть"),
                 ex("Ма'ма попроси'ла, что'бы я купи'л хлеб.", "Mom asked me to buy bread.", "что'бы я купи'л"),
             ]),
        card("Cases after these verbs",
             "Проси'ть takes the accusative of the person: проси'ть кого'. Сове'товать and приказа'ть take the dative: "
             "сове'товать кому', приказа'ть кому'. Тре'бовать takes что'бы or от + genitive.",
             tables=[table(
                 ["Verb", "Person is in..."],
                 [["проси'ть", "accusative (кого')"],
                  ["сове'товать / посове'товать", "dative (кому')"],
                  ["прика'зывать / приказа'ть", "dative (кому')"],
                  ["тре'бовать", "от + genitive"]])],
             examples=[
                 ex("Врач посове'товал мне отдыха'ть.", "The doctor advised me to rest.", "посове'товал мне"),
                 ex("Преподава'тель потре'бовал от студе'нтов тишины'.", "The teacher demanded silence from the students.", "от студе'нтов"),
             ]),
        card("Suggest: предлага'ть",
             "Предлага'ть takes a dative person and an infinitive: Я предлага'ю тебе' пойти'. With что'бы it works "
             "like проси'ть: Я предлага'ю, что'бы мы пошли'.",
             examples=[
                 ex("Я предлага'ю пойти' в парк.", "I suggest going to the park.", "предлага'ю"),
                 ex("Она' предложи'ла, что'бы мы пошли' в кино'.", "She suggested that we go to the cinema.", "что'бы мы пошли'"),
             ]),
    ],
    verify=(vf("просить", "прошу") + vf("попросить", "попросила") + vf("советовать", "советует") + vf("посоветовать", "посоветовал")
            + vf("приказать", "приказал") + vf("требовать", "требую") + vf("сказать", "сказала")
            + vf("предлагать", "предлагаю") + vf("предложить", "предложила") + vf("позвонить", "позвонил")
            + vf("отдыхать", "отдыхал", "отдыхать") + vf("купить", "купил", "купить") + vf("хлеб", "хлеб")
            + vf("уйти", "ушли", "уйти") + vf("молчать", "молчали") + vf("врач", "врач")
            + vf("студент", "студентов") + vf("тишина", "тишины")),
    exercises=[
        F("Ма'ма попроси'ла, что'бы я ___ хлеб. (bought)", "купи'л", ["купи'ть", "куплю'", "покупа'л"], "Что'бы + past.", "Mom asked me to buy bread.", lemma="купить"),
        F("Врач посове'товал, что'бы я ___. (rested)", "отдыха'л", ["отдыха'ть", "отдыха'ю", "отдохну'"], "Что'бы + past.", "The doctor advised me to rest.", lemma="отдыхать"),
        F("Он приказа'л, что'бы мы ___. (left)", "ушли'", ["уйти'", "уйдём", "уходи'ть"], "Plural past: ушли'.", "He ordered us to leave.", lemma="уйти"),
        F("Я тре'бую, что'бы вы ___. (kept quiet)", "молча'ли", ["молча'ть", "молчи'те", "молча'т"], "Что'бы + past plural.", "I demand that you be quiet.", lemma="молчать"),
        F("Врач посове'товал ___ отдыха'ть. (me)", "мне", ["меня'", "мной", "мно'ю"], "Сове'товать кому'.", "The doctor advised me to rest."),
        F("Ма'ма попроси'ла ___ купи'ть хлеб. (me)", "меня'", ["мне", "мной", "мно'ю"], "Проси'ть кого'.", "Mom asked me to buy bread."),
        F("Ма'ма сказа'ла, ___ мы шли домо'й. (so that: a command)", "что'бы", ["что", "е'сли", "и'ли"], "Command: что'бы + past.", "Mom said that we should go home."),
        mc("Which verb takes the dative of the person?", ["сове'товать", "проси'ть", "бить", "ждать"], "сове'товать", "Сове'товать кому'.", order=True),
        mc("Which verb takes the accusative of the person?", ["проси'ть", "сове'товать", "приказа'ть", "помога'ть"], "проси'ть", "Проси'ть кого'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 241
L241 = lesson(
    "In order to: что'бы for purpose",
    "Я иду' в магази'н, что'бы купи'ть хлеб.",
    requires=["чтобы", "цель", "успеть", "купить", "записка"],
    cards=[
        card("Why? In order to...",
             "Что'бы also answers the question Заче'м? (what for?). When the subject of both parts is the same, it is "
             "followed by the infinitive, exactly like English ‘in order to’.",
             tables=[table(
                 ["Question", "Answer"],
                 [["Заче'м ты идёшь в магази'н?", "Что'бы купи'ть хлеб."],
                  ["Заче'м она' у'чит ру'сский?", "Что'бы чита'ть кни'ги."],
                  ["Заче'м вы вста'ли ра'но?", "Что'бы успе'ть на по'езд."]])],
             examples=[
                 ex("Я иду' в магази'н, что'бы купи'ть хлеб.", "I am going to the store to buy bread.", "что'бы купи'ть"),
                 ex("Мы вста'ли ра'но, что'бы успе'ть на по'езд.", "We got up early to catch the train.", "что'бы успе'ть"),
             ]),
        card("A different subject: past tense",
             "When the second part has its own subject, the verb is in the past tense, as after verbs of wanting.",
             examples=[
                 ex("Я оста'влю запи'ску, что'бы он знал.", "I will leave a note so that he knows.", "что'бы он знал"),
                 ex("Говори' гро'мко, что'бы все слы'шали.", "Speak loudly so that everyone can hear.", "что'бы все слы'шали"),
             ]),
        card("Purpose at the start",
             "The что'бы part may come first. In formal Russian you may also hear для того' что'бы, which means the "
             "same.",
             examples=[
                 ex("Что'бы хорошо' говори'ть по-ру'сски, на'до мно'го чита'ть.", "To speak Russian well, you have to read a lot.", "Что'бы хорошо' говори'ть"),
                 ex("Для того' что'бы успе'ть на по'езд, мы взя'ли такси'.", "To catch the train we took a taxi.", "Для того' что'бы"),
             ]),
    ],
    verify=(vf("купить", "купить") + vf("успеть", "успеть") + vf("записка", "записку") + vf("хлеб", "хлеб")
            + vf("магазин", "магазин") + vf("учить", "учит") + vf("читать", "читать") + vf("встать", "встали")
            + vf("рано", "рано") + vf("поезд", "поезд") + vf("знать", "знал") + vf("слышать", "слышали")
            + vf("говорить", "говорить") + vf("такси", "такси") + vf("цель", "цель")),
    exercises=[
        F("Я иду' в магази'н, что'бы ___ хлеб. (buy)", "купи'ть", ["купи'л", "куплю'", "купи'ла"], "Same subject: infinitive.", "I am going to the store to buy bread.", lemma="купить"),
        F("Мы вста'ли ра'но, что'бы ___ на по'езд. (catch)", "успе'ть", ["успе'ли", "успе'л", "успе'ем"], "Same subject: infinitive.", "We got up early to catch the train.", lemma="успеть"),
        F("Я оста'влю запи'ску, что'бы он ___. (would know)", "знал", ["знать", "знает", "знала"], "Different subject: что'бы + past; он is masculine.", "I will leave a note so that he knows.", lemma="знать"),
        F("Говори' гро'мко, что'бы все ___. (could hear)", "слы'шали", ["слы'шать", "слы'шат", "слы'шит"], "Plural past after что'бы.", "Speak loudly so that everyone can hear.", lemma="слышать"),
        F("Мы пошли' в парк, ___ погуля'ть. (to)", "что'бы", ["потому' что", "е'сли", "и'ли"], "Purpose: что'бы.", "We went to the park to take a walk."),
        F("___ хорошо' говори'ть по-ру'сски, на'до мно'го чита'ть. (to)", "Что'бы", ["Е'сли", "Потому' что", "Кото'рый"], "Что'бы at the start of a purpose clause.", "To speak Russian well, you have to read a lot."),
        mc("Which question does что'бы answer?", ["Заче'м?", "Когда'?", "Где?", "Ско'лько?"], "Заче'м?", "Заче'м? = what for?", order=True),
        mc("What follows что'бы when the subject stays the same?", ["an infinitive", "a past tense", "a future tense", "an imperative"], "an infinitive", "Я иду', что'бы купи'ть.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 242
L242 = lesson(
    "Someone, something, somewhere: кто'-то, что'-то, где'-то",
    "Кто'-то звони'л, но я не зна'ю кто.",
    requires=["кто", "что", "где", "куда", "какой"],
    cards=[
        card("The particle -то",
             "Add -то to a question word and you get ‘some...’: someone, something, somewhere. The particle -то is "
             "used when you know that the person, thing or place exists, but you cannot or do not want to say which. "
             "The particle itself never changes.",
             tables=[table(
                 ["Question word", "With -то", "English"],
                 [["кто", "кто'-то", "someone"],
                  ["что", "что'-то", "something"],
                  ["где", "где'-то", "somewhere"],
                  ["куда'", "куда'-то", "(to) somewhere"],
                  ["отку'да", "отку'да-то", "from somewhere"],
                  ["когда'", "когда'-то", "once, at some time"],
                  ["како'й", "како'й-то", "some kind of"],
                  ["почему'", "почему'-то", "for some reason"],
                  ["как", "ка'к-то", "somehow"]])],
             examples=[
                 ex("Кто'-то звони'л, но я не зна'ю кто.", "Someone called, but I don't know who.", "Кто'-то"),
                 ex("Он куда'-то уе'хал.", "He went off somewhere.", "куда'-то"),
                 ex("Почему'-то она' не отвеча'ет.", "For some reason she is not answering.", "Почему'-то"),
             ]),
        card("Something happened, but details are missing",
             "With -то the action or the object is real. You just cannot give more details: perhaps you forgot, perhaps "
             "you do not know, perhaps it does not matter.",
             examples=[
                 ex("Я где'-то ви'дел э'того челове'ка.", "I have seen this person somewhere.", "где'-то"),
                 ex("Когда'-то здесь был парк.", "Once there was a park here.", "Когда'-то"),
                 ex("В ко'мнате что'-то лежи'т.", "Something is lying in the room.", "что'-то"),
             ]),
        card("Spelling",
             "Always use a hyphen: кто-то, где-то, куда-то. Where the question word has a stress, it stays the same: "
             "кто'-то, что'-то, куда'-то. Note that ка'к-то has the stress on the first word.",
             examples=[
                 ex("Како'й-то челове'к ждёт вас.", "Some man is waiting for you.", "Како'й-то"),
             ]),
    ],
    verify=(vf("звонить", "звонил") + vf("уехать", "уехал") + vf("отвечать", "отвечает") + vf("видеть", "видел")
            + vf("человек", "человека") + vf("комната", "комнате") + vf("лежать", "лежит") + vf("ждать", "ждёт")
            + vf("парк", "парк") + vf("знать", "знаю")),
    exercises=[
        F("___ звони'л, но я не зна'ю кто. (someone)", "Кто'-то", ["Кто", "Никто'", "Что'-то"], "Someone real, unknown: кто'-то.", "Someone called, but I don't know who."),
        F("Он ___ уе'хал. (off somewhere)", "куда'-то", ["где'-то", "отку'да-то", "куда'"], "Direction: куда'-то.", "He went off somewhere."),
        F("Я ___ ви'дел э'того челове'ка. (somewhere)", "где'-то", ["куда'-то", "никогда'", "где"], "Place, no direction: где'-то.", "I have seen this person somewhere."),
        F("___ она' не отвеча'ет. (for some reason)", "Почему'-то", ["Почему'", "Заче'м-то", "Ка'к-то"], "Почему'-то = for some reason.", "For some reason she is not answering."),
        F("___ здесь был парк. (once)", "Когда'-то", ["Когда'", "Где'-то", "Куда'-то"], "Когда'-то = once.", "Once there was a park here."),
        F("В ко'мнате ___ лежи'т. (something)", "что'-то", ["что", "кто'-то", "ничего'"], "Something real: что'-то.", "Something is lying in the room."),
        mc("What does -то show?", ["it exists, but details are unknown", "it may not exist", "it does not exist", "it is a question"], "it exists, but details are unknown", "Кто'-то = someone (definite but unknown).", order=True),
        mc("Which spelling is right for ‘to somewhere’?", ["куда'-то", "куда' то", "куда'то", "куда'—то"], "куда'-то", "With a hyphen.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 243
L243 = lesson(
    "Anyone, anything, ever: кто'-нибудь, что'-нибудь, когда'-нибудь",
    "Ты когда'-нибудь был в Росси'и?",
    requires=["кто", "что", "когда", "где", "как"],
    cards=[
        card("The particle -нибудь",
             "Add -нибудь to a question word when you do not know whether the person, thing or event even exists: "
             "anyone, anything, anywhere, ever. It is typical of questions, conditions, requests and the future.",
             tables=[table(
                 ["Question word", "With -нибудь", "English"],
                 [["кто", "кто'-нибудь", "anyone"],
                  ["что", "что'-нибудь", "anything"],
                  ["где", "где'-нибудь", "anywhere"],
                  ["куда'", "куда'-нибудь", "(to) anywhere"],
                  ["когда'", "когда'-нибудь", "ever; some day"],
                  ["как", "ка'к-нибудь", "somehow; sometime"],
                  ["како'й", "како'й-нибудь", "any"]])],
             examples=[
                 ex("Ты когда'-нибудь был в Росси'и?", "Have you ever been to Russia?", "когда'-нибудь"),
                 ex("Кто'-нибудь звони'л?", "Did anyone call?", "Кто'-нибудь"),
             ]),
        card("-то or -нибудь?",
             "-то: it exists, but you cannot say which. -нибудь: perhaps it exists, perhaps not. Compare a question and "
             "its answer.",
             tables=[table(
                 ["Question (-нибудь)", "Answer (-то)"],
                 [["Кто'-нибудь звони'л?", "Да, кто'-то звони'л."],
                  ["Ты куда'-нибудь е'здил?", "Да, я куда'-то е'здил."],
                  ["Ты что'-нибудь купи'л?", "Да, я что'-то купи'л."]])],
             examples=[
                 ex("Е'сли кто'-нибудь придёт, скажи', что меня' нет.", "If anyone comes, say that I am out.", "кто'-нибудь придёт"),
                 ex("Купи' что'-нибудь пое'сть.", "Buy something to eat.", "что'-нибудь"),
                 ex("Позвони' мне ка'к-нибудь.", "Call me sometime.", "ка'к-нибудь"),
             ]),
        card("Where -нибудь appears",
             "Think of -нибудь as ‘any’. It is natural in these places:",
             tables=[table(
                 ["Context", "Example"],
                 [["questions", "Есть здесь кто'-нибудь?"],
                  ["if-clauses", "Е'сли что'-нибудь случи'тся, позвони'."],
                  ["requests", "Принеси' что'-нибудь попи'ть."],
                  ["future", "Я куда'-нибудь пое'ду ле'том."]])],
             examples=[
                 ex("Я куда'-нибудь пое'ду ле'том.", "I will go somewhere in the summer.", "куда'-нибудь"),
             ]),
    ],
    verify=(vf("быть", "был") + vf("звонить", "звонил") + vf("приехать", "приедет") + vf("прийти", "придёт")
            + vf("сказать", "скажи") + vf("купить", "купил") + vf("позвонить", "позвони") + vf("лето", "летом")
            + vf("поехать", "поеду") + vf("ездить", "ездил") + vf("принести", "принеси")
            + vf("случиться", "случится")),
    exercises=[
        F("Ты ___ был в Росси'и? (ever)", "когда'-нибудь", ["никогда'", "всегда'", "сейча'с"], "Questions about experience: когда'-нибудь.", "Have you ever been to Russia?"),
        F("___ звони'л? (did anyone)", "Кто'-нибудь", ["Никто'", "Кого'", "Что"], "Question: кто'-нибудь.", "Did anyone call?"),
        F("Да, ___ звони'л. (someone did)", "кто'-то", ["кто'-нибудь", "никто'", "кто"], "Confirmed, but unknown: кто'-то.", "Yes, someone called."),
        F("Е'сли ___ придёт, скажи', что меня' нет. (anyone)", "кто'-нибудь", ["кто'-то", "никто'", "кого'"], "Conditional: -нибудь.", "If anyone comes, say that I am out."),
        F("Купи' ___ пое'сть. (something)", "что'-нибудь", ["ничего'", "что", "никто'"], "Request: -нибудь.", "Buy something to eat."),
        F("Я ___ пое'ду ле'том. (somewhere)", "куда'-нибудь", ["никуда'", "куда'", "ничего'"], "Future plan: -нибудь.", "I will go somewhere in the summer."),
        mc("In which sentence is -нибудь used correctly?", ["Ты что'-нибудь купи'л?", "Вчера' кто'-нибудь звони'л, но я не зна'ю кто.", "Он куда'-нибудь уе'хал, я знаю.", "Я где'-нибудь уже' был."], "Ты что'-нибудь купи'л?", "-нибудь fits questions."),
        mc("What does когда'-нибудь often mean in questions?", ["ever", "never", "always", "now"], "ever", "Ты когда'-нибудь был...?", order=True),
    ],
)

# ---------------------------------------------------------------------------- 244
L244 = lesson(
    "To someone, with something: the cases of кто'-то and что'-нибудь",
    "Я с кем-то говори'л о чём-то ва'жном.",
    requires=["кто", "что", "чей", "какой", "говорить"],
    cards=[
        card("The question word declines, the particle does not",
             "Put the question word in the case it needs and add the particle at the end. The preposition goes in front "
             "of the whole word.",
             tables=[table(
                 ["Case", "Someone", "Something"],
                 [["Nominative", "кто'-то", "что'-то"],
                  ["Genitive", "кого'-то", "чего'-то"],
                  ["Dative", "кому'-то", "чему'-то"],
                  ["Accusative", "кого'-то", "что'-то"],
                  ["Instrumental", "ке'м-то", "че'м-то"],
                  ["Prepositional", "(о) ко'м-то", "(о) чём-то"]])],
             examples=[
                 ex("Я с ке'м-то говори'л о чём-то ва'жном.", "I was speaking with someone about something important.", "с ке'м-то"),
                 ex("Он кому'-то позвони'л.", "He called someone.", "кому'-то"),
                 ex("У кого'-то есть ру'чка?", "Does anyone have a pen?", "У кого'-то"),
             ]),
        card("The same with -нибудь",
             "The forms of -нибудь are built in exactly the same way.",
             tables=[table(
                 ["Case", "Anyone", "Anything"],
                 [["Genitive", "кого'-нибудь", "чего'-нибудь"],
                  ["Dative", "кому'-нибудь", "чему'-нибудь"],
                  ["Instrumental", "ке'м-нибудь", "че'м-нибудь"],
                  ["Prepositional", "(о) ко'м-нибудь", "(о) чём-нибудь"]])],
             examples=[
                 ex("Ты говори'л об э'том с ке'м-нибудь?", "Did you talk about this with anyone?", "с ке'м-нибудь"),
                 ex("Ты что'-нибудь зна'ешь о нём?", "Do you know anything about him?", "что'-нибудь"),
             ]),
        card("Whose? Which?",
             "Како'й declines like an adjective. The particle again stays unchanged.",
             tables=[table(
                 ["Word", "Genitive"],
                 [["како'й-то", "како'го-то"],
                  ["како'й-нибудь", "како'го-нибудь"]])],
             examples=[
                 ex("Э'то письмо' от како'го-то незнако'мца.", "This letter is from some stranger.", "от како'го-то"),
             ]),
        card("Do not confuse with ни-",
             "Words with ни- mean ‘no one, nothing’ and need не before the verb. Compare:",
             tables=[table(
                 ["With -нибудь (maybe)", "With ни- (none)"],
                 [["Ты ви'дел кого'-нибудь?", "Я никого' не ви'дел."],
                  ["Ты что'-нибудь зна'ешь?", "Я ничего' не зна'ю."]])],
             examples=[
                 ex("Я никому' не звони'л.", "I did not call anyone.", "никому'"),
             ]),
    ],
    verify=(vf("говорить", "говорил") + vf("позвонить", "позвонил") + vf("ручка", "ручка")
            + vf("видеть", "видел") + vf("знать", "знаешь") + vf("письмо", "письмо") + vf("важный", "важном")
            + vf("звонить", "звонил")),
    exercises=[
        F("Я с ___ говори'л о чём-то ва'жном. (someone)", "ке'м-то", ["кто'-то", "кого'-то", "кому'-то"], "С + instrumental.", "I was speaking with someone about something important."),
        F("Он ___ позвони'л. (someone)", "кому'-то", ["кто'-то", "кого'-то", "ке'м-то"], "Позвони'ть кому'.", "He called someone."),
        F("У ___ есть ру'чка? (anyone)", "кого'-нибудь", ["кто'-нибудь", "кому'-нибудь", "ке'м-нибудь"], "У + genitive.", "Does anyone have a pen?"),
        F("Ты говори'л об э'том с ___? (anyone)", "ке'м-нибудь", ["кто'-нибудь", "кого'-нибудь", "кому'-нибудь"], "С + instrumental.", "Did you talk about this with anyone?"),
        F("Я ___ не звони'л. (no one)", "никому'", ["никто'", "никого'", "ни с кем"], "Звони'ть кому': никому'.", "I did not call anyone."),
        F("Я ___ не ви'дел. (no one)", "никого'", ["никто'", "никому'", "ничего'"], "Ви'деть кого': никого'.", "I saw no one."),
        mc("Does the particle -то change with the case?", ["no, only the question word does", "yes, it becomes -ту", "yes, it becomes -ти", "only in the plural"], "no, only the question word does", "Кому'-то, ке'м-то.", order=True),
        mc("Where does the preposition go?", ["before the whole word: с кем-то", "inside the word: ке'м с-то", "after the word: кем-то с", "it is dropped"], "before the whole word: с кем-то", "С ке'м-то.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 245
L245 = lesson(
    "Review: bring, take, want, in order to, someone",
    "Я хочу', что'бы ты кому'-нибудь отвёз э'ти кни'ги.",
    requires=["принести", "хотеть", "чтобы", "кто", "что"],
    cards=[
        card("What you now know",
             "Prefixed carrying and leading verbs make an aspect pair (the perfective uses the one-way stem). Вы- is "
             "stressed in the perfective. Что'бы + past tense joins a wish, a request or a command to a different "
             "subject. Что'бы + infinitive gives a purpose. -То means ‘someone I cannot name’; -нибудь means ‘anyone, "
             "if any’.",
             tables=[table(
                 ["Topic", "Example"],
                 [["bring (carrying)", "Принеси' воды'."],
                  ["wish with another subject", "Я хочу', что'бы ты пришёл."],
                  ["purpose", "Я иду' в магази'н, что'бы купи'ть хлеб."],
                  ["someone (unknown)", "Кто'-то звони'л."],
                  ["anyone (question)", "Кто'-нибудь звони'л?"]])],
             examples=[
                 ex("Я хочу', что'бы ты отвёз э'ти кни'ги кому'-нибудь из друзе'й.", "I want you to take these books to one of your friends.", "что'бы ты отвёз"),
             ]),
    ],
    verify=(vf("принести", "принеси") + vf("хотеть", "хочу") + vf("отвезти", "отвёз") + vf("книга", "книги")
            + vf("друг", "друзей") + vf("прийти", "пришёл")),
    exercises=[
        F("___ воды', пожа'луйста. (bring!)", "Принеси'", ["Вы'неси", "Унеси'", "Привези'"], "Принести' воду.", "Please bring some water.", lemma="принести"),
        F("Я хочу', что'бы ты ___. (come)", "пришёл", ["прийти'", "придёшь", "приходи'ть"], "Different subject: что'бы + past.", "I want you to come.", lemma="прийти"),
        F("Я иду' в магази'н, что'бы ___ хлеб. (buy)", "купи'ть", ["купи'л", "куплю'", "купи'ла"], "Same subject: infinitive.", "I am going to the store to buy bread.", lemma="купить"),
        F("___ звони'л, но я не зна'ю кто. (someone)", "Кто'-то", ["Кто'-нибудь", "Никто'", "Кого'"], "A real call, unknown caller.", "Someone called, but I don't know who."),
        F("Ты ___ был в Росси'и? (ever)", "когда'-нибудь", ["когда'-то", "никогда'", "иногда'"], "Question about experience.", "Have you ever been to Russia?"),
        F("Врач посове'товал, что'бы я ___. (rested)", "отдыха'л", ["отдыха'ть", "отдыха'ю", "отдохну'"], "Что'бы + past.", "The doctor advised me to rest.", lemma="отдыхать"),
        F("Де'ти ___ себя' хорошо'. (behave, plural)", "веду'т", ["ведёт", "несу'т", "во'зят"], "Вести' себя'.", "The children behave well.", lemma="вести"),
        mc("‘To drive someone to a destination’ is:", ["отвезти'", "принести'", "вы'нести", "завести'"], "отвезти'", "От- + везти'.", order=True),
        mc("Which sentence is correct?", ["Я хочу', что'бы она' пришла'.", "Я хочу', что'бы она' придёт.", "Я хочу', что'бы она' прийти'.", "Я хочу', что'бы она' приходит."], "Я хочу', что'бы она' пришла'.", "Что'бы + past tense."),
    ],
)

UNIT = unit("Unit 25: Prefixed carrying verbs, чтобы, -то and -нибудь",
            [L235, L236, L237, L238, L239, L240, L241, L242, L243, L244, L245])
