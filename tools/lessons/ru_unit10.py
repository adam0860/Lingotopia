"""Unit 10: aspect in the past and future, meals, months and durations
(textbook module 2, lesson 14)."""
from dsl import *

# ---------------------------------------------------------------------------- 66
L66 = lesson(
    "The future tense: two ways to form it",
    "Я бу'ду чита'ть, я прочита'ю",
    requires=["быть", "делать", "сделать", "читать", "прочитать"],
    cards=[
        card("Imperfective future: бу'ду + infinitive",
             "You already know that most verbs come in two aspects. In the past tense both aspects look alike "
             "(де'лал, сде'лал). In the future they are built differently. For the imperfective, take the "
             "future of быть and add the infinitive. The verb быть changes for the person, and the infinitive "
             "stays as it is.",
             tables=[table(
                 ["Person", "быть", "Example"],
                 [["я", "бу'д{у}", "я бу'ду чита'ть"],
                  ["ты", "бу'д{ешь}", "ты бу'дешь рабо'тать"],
                  ["он · она' · оно'", "бу'д{ет}", "она' бу'дет отдыха'ть"],
                  ["мы", "бу'д{ем}", "мы бу'дем де'лать"],
                  ["вы", "бу'д{ете}", "вы бу'дете гото'вить"],
                  ["они'", "бу'д{ут}", "они' бу'дут игра'ть"]])]),
        card("Perfective future: just conjugate it",
             "For the perfective, you do not use бу'ду at all. You conjugate the perfective verb with the "
             "same endings as the imperfective, but the result is future in meaning, since the perfective has no "
             "real present tense. So сде'лаю means “I will do it (and finish it)”. Never say бу'ду сде'лать.",
             tables=[table(
                 ["Person", "де'лать (present)", "сде'лать (future)"],
                 [["я", "де'ла{ю}", "сде'ла{ю}"],
                  ["ты", "де'ла{ешь}", "сде'ла{ешь}"],
                  ["он · она' · оно'", "де'ла{ет}", "сде'ла{ет}"],
                  ["мы", "де'ла{ем}", "сде'ла{ем}"],
                  ["вы", "де'ла{ете}", "сде'ла{ете}"],
                  ["они'", "де'ла{ют}", "сде'ла{ют}"]])],
             examples=[
                 ex("За'втра я бу'ду чита'ть кни'гу.", "Tomorrow I will be reading a book.", "бу'ду чита'ть"),
                 ex("За'втра я прочита'ю э'ту кни'гу.", "Tomorrow I will read this book through.", "прочита'ю"),
                 ex("В суббо'ту я сде'лаю дома'шнюю рабо'ту.", "On Saturday I will do my homework.", "сде'лаю"),
                 ex("В воскресе'нье мы бу'дем отдыха'ть.", "On Sunday we will relax.", "бу'дем отдыха'ть"),
             ]),
    ],
    verify=(vf("быть", "буду", "будешь", "будет", "будем", "будете", "будут")
            + vf("сделать", "сделаю", "сделаешь", "сделает", "сделаем", "сделаете", "сделают")
            + vf("делать", "делаю", "делаешь", "делает", "делаем", "делаете", "делают")
            + vf("прочитать", "прочитаю") + vf("приготовить", "приготовим")),
    exercises=[
        fb("За'втра я ___ чита'ть.", ["бу'ду", "бу'дешь", "бу'дет", "был"], "бу'ду",
           "I will + imperfective infinitive: бу'ду.", tr="Tomorrow I will be reading.", lemma="быть"),
        fb("За'втра мы ___ рабо'тать.", ["бу'дем", "бу'ду", "бу'дете", "бу'дут"], "бу'дем",
           "Мы goes with бу'дем.", tr="Tomorrow we will work.", lemma="быть"),
        fb("В воскресе'нье они' ___ отдыха'ть.", ["бу'дут", "бу'дем", "бу'дет", "бу'дешь"], "бу'дут",
           "Они' goes with бу'дут.", tr="On Sunday they will relax.", lemma="быть"),
        fb("За'втра я ___ дома'шнюю рабо'ту.", ["сде'лаю", "бу'ду сде'лать", "сде'лал", "сде'лаете"], "сде'лаю",
           "Perfective future: conjugate it, no бу'ду.", tr="Tomorrow I will do my homework.", lemma="сделать"),
        fb("В суббо'ту она' ___ э'ту кни'гу.", ["прочита'ет", "прочита'ла", "прочита'ть", "бу'дет прочита'ть"], "прочита'ет",
           "She goes with the ending -ет, and no бу'дет.", tr="On Saturday she will read this book through.", lemma="прочитать"),
        fb("Ве'чером мы ___ у'жин.", ["пригото'вим", "пригото'вили", "пригото'вит", "бу'дем пригото'вить"], "пригото'вим",
           "Мы takes -им in the perfective future.", tr="In the evening we will cook dinner.", lemma="приготовить"),
        mc("Which future is formed with бу'ду + infinitive?", ["imperfective", "perfective", "both", "neither"], "imperfective",
           "The perfective never uses бу'ду.", order=True),
        mc("Which sentence means “I will be doing my homework”?",
           ["Я бу'ду де'лать дома'шнюю рабо'ту.", "Я бу'ду сде'лать дома'шнюю рабо'ту.",
            "Я бу'ду сде'лаю дома'шнюю рабо'ту.", "Я де'лать бу'ду дома'шнюю рабо'ту."],
           "Я бу'ду де'лать дома'шнюю рабо'ту.", "Бу'ду goes with the imperfective infinitive."),
        mc("What does сде'лаю mean?", ["I will do it (and finish it)", "I am doing it", "I did it", "I was doing it"],
           "I will do it (and finish it)", "Perfective forms that look like the present are future.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 67
L67 = lesson(
    "Aspect in the past: process or result?",
    "Я чита'л два часа', я прочита'л кни'гу",
    requires=["делать", "сделать", "читать", "прочитать", "вчера"],
    cards=[
        card("What each aspect says",
             "In the past, the imperfective names the action itself: it was going on (for a while), it was repeated, "
             "or you simply tell what you did. The perfective stresses that one action was completed and that you "
             "have the result. English uses different tenses for these ideas, but Russian only has the two aspects.",
             tables=[table(
                 ["Idea", "Imperfective", "Perfective"],
                 [["In progress", "Он чита'л кни'гу два часа'.", "Он прочита'л кни'гу."],
                  ["Repeated or habit", "Ра'ньше я встава'л в семь.", "Вчера' я встал в оди'ннадцать."],
                  ["Two things at once", "Когда' я де'лал уро'ки, он слу'шал му'зыку.", "—"],
                  ["Things in sequence", "—", "Снача'ла я сде'лал уро'ки, а пото'м отдыха'л."],
                  ["Just naming it", "Что ты де'лал вчера'?", "—"]])]),
        card("Words that give it away",
             "Certain words usually point to one aspect. Duration and repetition words go with the imperfective. "
             "Words that suggest completion, a moment, or a result go with the perfective.",
             tables=[table(
                 ["Imperfective", "Perfective"],
                 [["ка'ждый день · ча'сто · обы'чно", "уже' · наконе'ц"],
                  ["до'лго · два часа' · весь день", "вдруг · сра'зу"],
                  ["ра'ньше · никогда' не", "как то'лько · за час"]])],
             examples=[
                 ex("Вчера' мы де'лали дома'шнюю рабо'ту три часа'.", "Yesterday we did homework for three hours.", "де'лали"),
                 ex("Я уже' сде'лал дома'шнюю рабо'ту.", "I have already finished my homework.", "сде'лал"),
                 ex("Ра'ньше я встава'л в семь часо'в.", "I used to get up at seven.", "встава'л"),
                 ex("Обы'чно я встаю' ра'но, но вчера' я встал в оди'ннадцать.", "I usually get up early, but yesterday I got up at eleven.", "встал"),
                 ex("Наконе'ц я прочита'л э'ту кни'гу!", "At last I have finished reading this book!", "прочита'л"),
             ]),
    ],
    verify=(vf("делать", "делал", "делали") + vf("сделать", "сделал") + vf("вставать", "вставал")
            + vf("встать", "встал") + vf("прочитать", "прочитал") + vf("слушать", "слушал")
            + vf("отдыхать", "отдыхал")),
    exercises=[
        fb("Вчера' они' ___ дома'шнюю рабо'ту два часа'.", ["де'лали", "сде'лали"], "де'лали",
           "Two hours = duration: imperfective.", tr="Yesterday they did homework for two hours."),
        fb("Я уже' ___ дома'шнюю рабо'ту.", ["сде'лал", "де'лал"], "сде'лал",
           "Уже' + a finished result: perfective.", tr="I have already done my homework."),
        fb("Ра'ньше я ___ в семь часо'в.", ["встава'л", "встал"], "встава'л",
           "Ра'ньше = a repeated habit: imperfective.", tr="I used to get up at seven."),
        fb("Обы'чно я встаю' ра'но, но вчера' я ___ в оди'ннадцать.", ["встал", "встава'л"], "встал",
           "A single occasion: perfective.", tr="I usually get up early, but yesterday I got up at eleven."),
        fb("Наконе'ц я ___ э'ту кни'гу!", ["прочита'л", "чита'л"], "прочита'л",
           "Наконе'ц signals completion: perfective.", tr="At last I have read this book!"),
        fb("Когда' я ___ уро'ки, он слу'шал му'зыку.", ["де'лал", "сде'лал"], "де'лал",
           "Two simultaneous actions in progress: imperfective.", tr="While I was doing my lessons, he was listening to music."),
        fb("Я ___ э'ту кни'гу за оди'н час.", ["прочита'л", "чита'л"], "прочита'л",
           "За оди'н час (within an hour) points to a completed action: perfective.", tr="I read this book in one hour."),
        fb("Что ты ___ вчера' ве'чером?", ["де'лал", "сде'лал"], "де'лал",
           "Asking what the activity was: imperfective.", tr="What did you do yesterday evening?"),
        mc("Which word points to the perfective?", ["наконе'ц", "ка'ждый день", "ча'сто", "до'лго"], "наконе'ц",
           "Наконе'ц suggests a completed result."),
        mc("Which word points to the imperfective?", ["ка'ждый день", "наконе'ц", "вдруг", "сра'зу"], "ка'ждый день",
           "Repetition goes with the imperfective."),
        mc("Which sentence means “He read for two hours”?",
           ["Он чита'л два часа'.", "Он прочита'л два часа'.", "Он бу'дет чита'ть два часа'.", "Он чита'ет два часа'."],
           "Он чита'л два часа'.", "Duration in the past: imperfective."),
    ],
)

# ---------------------------------------------------------------------------- 68
L68 = lesson(
    "Aspect in the future: the same two ideas",
    "За'втра я бу'ду гото'вить, в суббо'ту я пригото'влю",
    requires=["готовить", "приготовить", "встать", "сразу", "пока"],
    cards=[
        card("The contrast stays the same",
             "The two aspects do the same jobs in the future as in the past. The imperfective future "
             "(бу'ду + infinitive) is for something in progress, repeated, or simply named. The perfective "
             "future is for one action that you plan to complete, with a result in mind.",
             tables=[table(
                 ["Idea", "Imperfective future", "Perfective future"],
                 [["In progress", "В пять часо'в мы бу'дем гото'вить у'жин.", "—"],
                  ["Plan to finish", "—", "В суббо'ту я сде'лаю дома'шнюю рабо'ту."],
                  ["Habit", "Я бу'ду встава'ть в де'сять часо'в ка'ждый день.", "—"],
                  ["Single occasion", "—", "За'втра я вста'ну в де'вять."],
                  ["Two things at once", "Пока' мы бу'дем гото'вить, мы бу'дем слу'шать му'зыку.", "—"],
                  ["Things in sequence", "—", "Снача'ла мы пригото'вим у'жин, а пото'м сде'лаем уро'ки."]])]),
        card("Words that signal completion",
             "Сра'зу (right away) and как то'лько (as soon as) are followed by the perfective, because they refer "
             "to a finished action. Пока' (while) is followed by the imperfective, because it describes something "
             "that goes on for a while.",
             examples=[
                 ex("Как то'лько я прочита'ю э'ту кни'гу, я напишу' письмо'.", "As soon as I finish this book, I'll write a letter.", "прочита'ю"),
                 ex("Пока' мы бу'дем де'лать уро'ки, мы бу'дем слу'шать му'зыку.", "While we do our lessons, we'll listen to music.", "бу'дем де'лать"),
                 ex("Обы'чно я встаю' в шесть часо'в, но за'втра я вста'ну в де'вять.", "I usually get up at six, but tomorrow I'll get up at nine.", "вста'ну"),
                 ex("В суббо'ту и в воскресе'нье я бу'ду то'лько чита'ть.", "On Saturday and Sunday I'll only read.", "бу'ду то'лько чита'ть"),
             ]),
    ],
    verify=(vf("встать", "встану") + vf("прочитать", "прочитаю") + vf("написать", "напишу")
            + vf("приготовить", "приготовим") + vf("сделать", "сделаю", "сделаем")),
    exercises=[
        fb("За'втра в пять часо'в мы ___ у'жин.", ["бу'дем гото'вить", "пригото'вим"], "бу'дем гото'вить",
           "In progress at a given time: imperfective future.", tr="Tomorrow at five we will be cooking dinner."),
        fb("В суббо'ту я ___ дома'шнюю рабо'ту (and get it done).", ["сде'лаю", "бу'ду де'лать"], "сде'лаю",
           "A plan to finish: perfective future.", tr="On Saturday I will get my homework done."),
        fb("Как то'лько я ___ э'ту кни'гу, я напишу' письмо'.", ["прочита'ю", "бу'ду чита'ть"], "прочита'ю",
           "Как то'лько is followed by a completed action: perfective.", tr="As soon as I finish this book, I'll write a letter."),
        fb("Пока' мы ___ дома'шнюю рабо'ту, мы бу'дем слу'шать му'зыку.", ["бу'дем де'лать", "сде'лаем"], "бу'дем де'лать",
           "Пока' describes a process: imperfective.", tr="While we do our homework, we'll listen to music."),
        fb("Обы'чно я встаю' в шесть, но за'втра я ___ в де'вять.", ["вста'ну", "бу'ду встава'ть"], "вста'ну",
           "One occasion: perfective.", tr="I usually get up at six, but tomorrow I'll get up at nine."),
        fb("В суббо'ту и в воскресе'нье я бу'ду то'лько ___.", ["чита'ть", "прочита'ть"], "чита'ть",
           "Бу'ду takes the imperfective infinitive.", tr="On Saturday and Sunday I'll only read."),
        fb("Когда' я бу'ду жить в дере'вне, я бу'ду ___ ка'ждый день в де'сять.", ["встава'ть", "встать"], "встава'ть",
           "Every day = habit: imperfective.", tr="When I live in the country I'll get up at ten every day."),
        mc("Which aspect usually follows сра'зу and как то'лько?", ["perfective", "imperfective", "both", "neither"], "perfective",
           "They refer to a completed action.", order=True),
        mc("Which form means “I will get up”, a single occasion?", ["я вста'ну", "я бу'ду встать", "я встал", "я встаю'"],
           "я вста'ну", "Perfective future of встать."),
        mc("Which sentence means “Tomorrow I'll cook dinner (and finish)”?",
           ["За'втра я пригото'влю у'жин.", "За'втра я бу'ду гото'вить у'жин.", "За'втра я пригото'вил у'жин.", "За'втра я бу'ду пригото'влю у'жин."],
           "За'втра я пригото'влю у'жин.", "Perfective future for a completed plan."),
    ],
)

# ---------------------------------------------------------------------------- 69
L69 = lesson(
    "Learning aspect pairs: встава'ть / встать, гото'вить / пригото'вить",
    "Я встаю', я вста'ну, я гото'влю, я пригото'влю",
    requires=["вставать", "встать", "готовить", "приготовить", "рано"],
    cards=[
        card("Always learn both",
             "There is no single rule for making the perfective, so look the verb up and learn both forms "
             "together. The most common method is a prefix (по-, при-, про-, на-, с-). Another is changing the "
             "suffix, as in встава'ть → встать. When you conjugate a perfective verb, use the same endings as its "
             "partner, but remember it is future.",
             tables=[table(
                 ["Imperfective", "Perfective", "How the pair works"],
                 [["де'лать", "сде'лать", "prefix с-"],
                  ["чита'ть", "прочита'ть", "prefix про-"],
                  ["писа'ть", "написа'ть", "prefix на-"],
                  ["гото'вить", "пригото'вить", "prefix при-"],
                  ["встава'ть", "встать", "suffix -ва- drops"]])]),
        card("Two patterns to see side by side",
             "Гото'вить → пригото'вить keeps every ending the same, because only the prefix is added. Встава'ть → "
             "встать changes more. The imperfective present is встаю', встаёшь … while the perfective future adds "
             "an н to the stem: вста'ну, вста'нешь …",
             tables=[table(
                 ["Person", "гото'вить (present)", "пригото'вить (future)"],
                 [["я", "гото'в{лю}", "пригото'в{лю}"],
                  ["ты", "гото'в{ишь}", "пригото'в{ишь}"],
                  ["он · она' · оно'", "гото'в{ит}", "пригото'в{ит}"],
                  ["мы", "гото'в{им}", "пригото'в{им}"],
                  ["вы", "гото'в{ите}", "пригото'в{ите}"],
                  ["они'", "гото'в{ят}", "пригото'в{ят}"]]),
             table(
                 ["Person", "встава'ть (present)", "встать (future)"],
                 [["я", "вста{ю'}", "вста'{ну}"],
                  ["ты", "вста{ёшь}", "вста'{нешь}"],
                  ["он · она' · оно'", "вста{ёт}", "вста'{нет}"],
                  ["мы", "вста{ём}", "вста'{нем}"],
                  ["вы", "вста{ёте}", "вста'{нете}"],
                  ["они'", "вста{ю'т}", "вста'{нут}"]])],
             examples=[
                 ex("Я встаю' в семь часо'в.", "I get up at seven.", "встаю'"),
                 ex("За'втра я вста'ну в шесть часо'в.", "Tomorrow I will get up at six.", "вста'ну"),
                 ex("Она' гото'вит у'жин ка'ждый день.", "She cooks dinner every day.", "гото'вит"),
                 ex("За'втра она' пригото'вит вку'сный у'жин.", "Tomorrow she will cook a tasty dinner.", "пригото'вит"),
             ]),
    ],
    verify=(vf("вставать", "встаю", "встаёшь", "встаёт", "встаём", "встаёте", "встают")
            + vf("встать", "встану", "встанешь", "встанет", "встанем", "встанете", "встанут")
            + vf("готовить", "готовлю", "готовишь", "готовит", "готовим", "готовите", "готовят")
            + vf("приготовить", "приготовлю", "приготовишь", "приготовит", "приготовим", "приготовите", "приготовят")),
    exercises=[
        fb("Я ___ ка'ждый день в семь часо'в.", ["встаю'", "вста'ну", "встаёт", "встаёшь"], "встаю'",
           "A daily habit: imperfective встава'ть.", tr="I get up every day at seven.", lemma="вставать"),
        fb("За'втра я ___ в шесть часо'в.", ["вста'ну", "вста'нешь", "встал", "вста'нем"], "вста'ну",
           "Я goes with вста'ну.", tr="Tomorrow I will get up at six.", lemma="встать"),
        fb("Ты ___ ра'но?", ["встаёшь", "встаю'", "встаёт", "встаём"], "встаёшь",
           "Ты goes with -ёшь.", tr="Do you get up early?", lemma="вставать"),
        fb("Она' ___ у'жин ка'ждый день.", ["гото'вит", "гото'влю", "гото'вишь", "гото'вим"], "гото'вит",
           "Она' goes with гото'вит.", tr="She cooks dinner every day.", lemma="готовить"),
        fb("За'втра мы ___ у'жин.", ["пригото'вим", "пригото'вишь", "пригото'вили", "пригото'влю"], "пригото'вим",
           "Мы goes with -им.", tr="Tomorrow we will cook dinner.", lemma="приготовить"),
        fb("Они' ___ ра'но.", ["вста'нут", "вста'ну", "вста'нет", "вста'нем"], "вста'нут",
           "Они' goes with -ут.", tr="They will get up early.", lemma="встать"),
        mc("Which verb is the perfective partner of встава'ть?", ["встать", "вставля'ть", "стоя'ть", "сиде'ть"], "встать",
           "Встава'ть / встать: to get up.", order=True),
        mc("What does the perfective of гото'вить add?", ["the prefix при-", "the prefix по-", "the suffix -ва-", "nothing"],
           "the prefix при-", "Гото'вить / пригото'вить."),
        mc("What is added to the stem of встать in the future?", ["н", "в", "м", "т"], "н",
           "Вста'ну, вста'нешь …", order=True),
        mc("Which pair works with a prefix?",
           ["писа'ть → написа'ть", "покупа'ть → купи'ть", "встава'ть → встать", "говори'ть → сказа'ть"],
           "писа'ть → написа'ть", "На- is the prefix."),
    ],
)

# ---------------------------------------------------------------------------- 70
L70 = lesson(
    "Meals: за'втрак, обе'д, у'жин",
    "Я за'втракаю, мы пообе'дали, на у'жин я ем ка'шу",
    requires=["завтрак", "обед", "ужин", "есть", "пить"],
    cards=[
        card("Three meals, three verbs",
             "Each meal has a noun and a verb that is made from it. All of these verbs are regular -ать "
             "verbs. Their perfective partners add по-: you finish the meal. To say what you eat for a meal use "
             "на plus the accusative: на за'втрак, на обе'д, на у'жин.",
             tables=[table(
                 ["Meal", "Verb (imperfective)", "Verb (perfective)"],
                 [["за'втрак", "за'втракать", "поза'втракать"],
                  ["обе'д", "обе'дать", "пообе'дать"],
                  ["у'жин", "у'жинать", "поу'жинать"]])]),
        card("To eat, to drink",
             "Есть (to eat) and пить (to drink) are irregular, so learn the forms. Есть is the same word you saw "
             "in “there is”, but its meaning here is different and it changes by person. Past: ел, е'ла, е'ли · "
             "пил, пила', пи'ли.",
             tables=[table(
                 ["Person", "есть", "пить"],
                 [["я", "ем", "пь{ю}"],
                  ["ты", "ешь", "пь{ёшь}"],
                  ["он · она' · оно'", "ест", "пь{ёт}"],
                  ["мы", "еди'м", "пь{ём}"],
                  ["вы", "еди'те", "пь{ёте}"],
                  ["они'", "едя'т", "пь{ют}"]])],
             examples=[
                 ex("Что ты ешь на за'втрак?", "What do you eat for breakfast?", "ешь"),
                 ex("На за'втрак я ем ка'шу и пью чай.", "For breakfast I eat porridge and drink tea.", "ем"),
                 ex("Мы обе'даем в час дня.", "We have lunch at one in the afternoon.", "обе'даем"),
                 ex("Вчера' мы поу'жинали до'ма.", "Yesterday we had dinner at home.", "поу'жинали"),
                 ex("Она' ещё не поза'втракала.", "She hasn't had breakfast yet.", "поза'втракала"),
             ]),
    ],
    verify=(vf("есть", "ем", "ешь", "ест", "едим", "едите", "едят", "ел", "ела", "ели")
            + vf("пить", "пью", "пьёшь", "пьёт", "пьём", "пьёте", "пьют", "пил", "пила", "пили")
            + vf("завтракать", "завтракаю", "завтракаешь") + vf("обедать", "обедаем")
            + vf("позавтракать", "позавтракала") + vf("поужинать", "поужинали")),
    exercises=[
        fb("Я ___ ка'шу на за'втрак.", ["ем", "ешь", "ест", "еди'м"], "ем",
           "Я goes with ем.", tr="I eat porridge for breakfast.", lemma="есть"),
        fb("Ты ___ чай?", ["пьёшь", "пью", "пьёт", "пьём"], "пьёшь",
           "Ты goes with пьёшь.", tr="Do you drink tea?", lemma="пить"),
        fb("Мы ___ в час дня.", ["обе'даем", "обе'даю", "обе'дает", "обе'даешь"], "обе'даем",
           "Мы goes with -ем.", tr="We have lunch at one in the afternoon.", lemma="обедать"),
        fb("Вчера' мы ___ до'ма.", ["поу'жинали", "поу'жинаем", "поу'жинать", "поу'жинал"], "поу'жинали",
           "Past, plural: поу'жинали.", tr="Yesterday we had dinner at home.", lemma="поужинать"),
        fb("На ___ я ем бутербро'д.", ["за'втрак", "за'втрака", "за'втраке", "за'втраку"], "за'втрак",
           "For a meal: на + accusative.", tr="For breakfast I eat a sandwich.", lemma="завтрак"),
        fb("Вчера' он ___ чай.", ["пил", "пила'", "пьёт", "пили"], "пил",
           "Masculine past: пил.", tr="Yesterday he drank tea.", lemma="пить"),
        fb("Она' ещё не ___.", ["поза'втракала", "поза'втракал", "поза'втракаю", "поза'втракает"], "поза'втракала",
           "Feminine past of the perfective.", tr="She hasn't had breakfast yet.", lemma="позавтракать"),
        mc("How do you say “for lunch”?", ["на обе'д", "в обе'д", "для обе'де", "о обе'де"], "на обе'д",
           "На + accusative."),
        mc("Which verb is the perfective partner of у'жинать?", ["поу'жинать", "у'жин", "ужина'ть", "у'жинал"], "поу'жинать",
           "The prefix по- makes the perfective."),
        mc("Which verb means “to eat”?", ["есть", "пить", "спать", "ждать"], "есть",
           "Ем, ешь, ест …", order=True),
    ],
)

# ---------------------------------------------------------------------------- 71
L71 = lesson(
    "When and if: когда' and е'сли about the future",
    "Когда' я бу'ду в Москве', е'сли ты прочита'ешь",
    requires=["когда", "если", "быть", "тогда", "время"],
    cards=[
        card("Future inside, future outside",
             "English often uses the present in a clause that starts with “when” or “if” but still talks about "
             "the future (“When I am in Moscow, I will visit museums”). Russian never does this. If the action "
             "has not happened yet, the verb is in the future tense, in the “when” or “if” clause as well. You "
             "can use the imperfective (бу'ду + infinitive, or бу'ду + place) or the perfective (a plan to finish).",
             tables=[table(
                 ["Pattern", "Example"],
                 [["когда' + future", "Когда' я бу'ду в Москве', я бу'ду ходи'ть в музе'и."],
                  ["когда' + perfective", "Когда' я прочита'ю кни'гу, я позвоню'."],
                  ["е'сли + future", "Е'сли ты бу'дешь до'ма, я позвоню'."],
                  ["е'сли … тогда'", "Е'сли ты бу'дешь рабо'тать ве'чером, тогда' я то'же бу'ду."]])],
             examples=[
                 ex("Когда' я бу'ду в Москве', я бу'ду ходи'ть в теа'тры.", "When I am in Moscow, I will go to theaters.", "бу'ду в Москве'"),
                 ex("Е'сли ты бу'дешь до'ма, я позвоню'.", "If you are home, I'll call.", "бу'дешь до'ма"),
                 ex("Когда' мы сде'лаем уро'ки, мы бу'дем отдыха'ть.", "When we finish our lessons, we'll relax.", "сде'лаем"),
                 ex("Е'сли ты вста'нешь ра'но, мы бу'дем за'втракать вме'сте.", "If you get up early, we'll have breakfast together.", "вста'нешь"),
             ]),
    ],
    verify=(vf("быть", "буду", "будешь") + vf("сделать", "сделаем") + vf("встать", "встанешь")
            + vf("позвонить", "позвоню") + vf("работать", "работать")),
    exercises=[
        fb("Когда' я ___ в Москве', я бу'ду ходи'ть в музе'и.", ["бу'ду", "был", "быть", "есть"], "бу'ду",
           "Future action, so future tense even after когда'.", tr="When I am in Moscow, I'll go to museums.", lemma="быть"),
        fb("Е'сли ты ___ до'ма, я позвоню'.", ["бу'дешь", "есть", "был", "быть"], "бу'дешь",
           "Future condition: future tense.", tr="If you are at home, I'll call.", lemma="быть"),
        fb("Когда' мы ___ уро'ки, мы бу'дем отдыха'ть.", ["сде'лаем", "сде'лали", "сде'лал", "сде'лала"], "сде'лаем",
           "A finished action in the future: perfective future.", tr="When we finish our lessons, we'll relax.", lemma="сделать"),
        fb("Е'сли ты ___ ра'но, мы бу'дем за'втракать вме'сте.", ["вста'нешь", "встал", "вста'нут", "вста'ну"], "вста'нешь",
           "Ты goes with вста'нешь.", tr="If you get up early, we'll have breakfast together.", lemma="встать"),
        fb("Когда' я бу'ду в Москве', я ___ ходи'ть в теа'тры.", ["бу'ду", "был", "бу'дем", "бу'дут"], "бу'ду",
           "Я goes with бу'ду.", tr="When I am in Moscow, I will go to theaters.", lemma="быть"),
        mc("Which tense follows когда' when the action is still in the future?", ["future", "present", "past", "imperative"], "future",
           "Russian uses the future in the “when” clause.", order=True),
        mc("Which sentence is correct?",
           ["Е'сли ты бу'дешь до'ма, я позвоню'.", "Е'сли ты есть до'ма, я позвоню'.", "Е'сли ты был до'ма, я позвоню'.", "Е'сли ты бу'ду до'ма, я позвоню'."],
           "Е'сли ты бу'дешь до'ма, я позвоню'.", "Ты goes with бу'дешь."),
        mc("Which word often begins the main clause after е'сли?", ["тогда'", "потому'", "но", "и"], "тогда'",
           "Е'сли … тогда' …"),
        mc("Which sentence means “When I am in Moscow, I will go to museums”?",
           ["Когда' я бу'ду в Москве', я бу'ду ходи'ть в музе'и.", "Когда' я в Москве' был, я бу'ду ходи'ть в музе'и.",
            "Когда' я есть в Москве', я бу'ду ходи'ть в музе'и.", "Когда' я бу'ду в Москве', я ходи'л в музе'и."],
           "Когда' я бу'ду в Москве', я бу'ду ходи'ть в музе'и.", "Future in both clauses."),
    ],
)

# ---------------------------------------------------------------------------- 72
L72 = lesson(
    "In January, this year, this week",
    "В январе', в э'том году', на э'той неде'ле",
    requires=["год", "месяц", "неделя", "январь", "май"],
    cards=[
        card("In a month",
             "To say that something happens in a month, use в and the prepositional of the month. Most months "
             "take -е, and those that end in -ь drop it and replace it with -е. Note the stress: some months are "
             "stressed on the ending (январе'), and some on the stem (в ма'рте).",
             tables=[table(
                 ["Month", "In …", "Month", "In …"],
                 [["янва'рь", "в январ{е'}", "ию'ль", "в ию'л{е}"],
                  ["февра'ль", "в феврал{е'}", "а'вгуст", "в а'вгуст{е}"],
                  ["март", "в ма'рт{е}", "сентя'брь", "в сентябр{е'}"],
                  ["апре'ль", "в апре'л{е}", "октя'брь", "в октябр{е'}"],
                  ["май", "в ма'{е}", "ноя'брь", "в ноябр{е'}"],
                  ["ию'нь", "в ию'н{е}", "дека'брь", "в декабр{е'}"]])]),
        card("This year, this month, this week",
             "With год and ме'сяц use в, with неде'ля use на. The words go in the prepositional, and adjectives "
             "in front of them take the endings you learned. Год is another word with the stressed -у' place "
             "form: в э'том году', but о го'де for “about the year”. Useful modifiers: э'тот, про'шлый (last) and "
             "бу'дущий (next, future).",
             tables=[table(
                 ["Noun", "This", "Last", "Next"],
                 [["год", "в э'том году'", "в про'шлом году'", "в бу'дущем году'"],
                  ["ме'сяц", "в э'том ме'сяце", "в про'шлом ме'сяце", "в бу'дущем ме'сяце"],
                  ["неде'ля", "на э'той неде'ле", "на про'шлой неде'ле", "на бу'дущей неде'ле"]])],
             examples=[
                 ex("Когда' у нас экза'мены? — В феврале'.", "When do we have exams? — In February.", "В феврале'"),
                 ex("В э'том году' мы бу'дем жить в дере'вне.", "This year we will live in the countryside.", "В э'том году'"),
                 ex("На э'той неде'ле я бу'ду до'ма.", "This week I will be at home.", "На э'той неде'ле"),
                 ex("В про'шлом ме'сяце он рабо'тал в А'нглии.", "Last month he worked in England.", "В про'шлом ме'сяце"),
                 ex("Мы бы'ли в Москве' в ма'е.", "We were in Moscow in May.", "в ма'е"),
             ]),
    ],
    verify=(vf("январь", "январе") + vf("февраль", "феврале") + vf("март", "марте") + vf("апрель", "апреле")
            + vf("май", "мае") + vf("июнь", "июне") + vf("июль", "июле") + vf("август", "августе")
            + vf("сентябрь", "сентябре") + vf("октябрь", "октябре") + vf("ноябрь", "ноябре") + vf("декабрь", "декабре")
            + vf("год", "году", "годе") + vf("месяц", "месяце") + vf("неделя", "неделе")
            + vf("этот", "этом", "этой") + vf("прошлый", "прошлом", "прошлой")
            + vf("будущий", "будущем", "будущей")),
    exercises=[
        fb("Мы бы'ли в Москве' в ___.", ["ма'е", "май", "ма'я", "ма'ю"], "ма'е",
           "In a month: в + prepositional.", tr="We were in Moscow in May.", lemma="май"),
        fb("Экза'мены бу'дут в ___.", ["феврале'", "февраль", "февраля'", "февралю'"], "феврале'",
           "Февра'ль → в феврале'.", tr="The exams will be in February.", lemma="февраль"),
        fb("В э'том ___ мы бу'дем жить в дере'вне.", ["году'", "год", "го'да", "го'ды"], "году'",
           "Год has the stressed place form -у'.", tr="This year we will live in the countryside.", lemma="год"),
        fb("На э'той ___ я бу'ду до'ма.", ["неде'ле", "неде'ля", "неде'лю", "неде'ли"], "неде'ле",
           "На + prepositional: неде'ле.", tr="This week I will be at home.", lemma="неделя"),
        fb("В про'шлом ___ он рабо'тал в А'нглии.", ["ме'сяце", "ме'сяц", "ме'сяца", "ме'сяцу"], "ме'сяце",
           "В + prepositional: ме'сяце.", tr="Last month he worked in England.", lemma="месяц"),
        fb("В ___ мы отдыха'ем на мо'ре.", ["ию'ле", "ию'ль", "ию'ля", "ию'лю"], "ию'ле",
           "Ию'ль → в ию'ле.", tr="In July we vacation at the sea.", lemma="июль"),
        fb("Мой экза'мен в ___.", ["октябре'", "октя'брь", "октября'", "октябрю'"], "октябре'",
           "Октя'брь → в октябре'.", tr="My exam is in October.", lemma="октябрь"),
        mc("Which preposition goes with неде'ля in “this week”?", ["на", "в", "о", "к"], "на",
           "На э'той неде'ле.", order=True),
        mc("Which preposition goes with ме'сяц and год?", ["в", "на", "о", "к"], "в",
           "В э'том году', в э'том ме'сяце.", order=True),
        mc("Which phrase means “in September”?", ["в сентябре'", "в сентя'брь", "в сентября'", "на сентябре'"],
           "в сентябре'", "Сентя'брь → в сентябре'."),
        mc("What is special about в году'?", ["It has a stressed -у' ending", "It ends in -ом", "It has no ending", "It ends in -ой"],
           "It has a stressed -у' ending", "Like в лесу', в саду'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 73
L73 = lesson(
    "All day, all week: весь, and “about” a time",
    "Весь день, всю неде'лю, часа' два",
    requires=["весь", "неделя", "год", "месяц", "лето"],
    cards=[
        card("Весь, вся, всё, все",
             "To say that something lasted a whole day, week, month or year, use весь (all, the whole) with "
             "the time word in the accusative. Весь agrees with the noun in gender. Feminine words change to "
             "-у (всю неде'лю), while masculine and neuter words look like the nominative.",
             tables=[table(
                 ["Gender", "Word", "Example"],
                 [["masculine", "весь", "весь день · весь ме'сяц · весь янва'рь"],
                  ["feminine", "всю", "всю неде'лю · всю ночь · всю зи'му"],
                  ["neuter", "всё", "всё ле'то · всё у'тро"],
                  ["plural", "все", "все дни · все выходны'е"]])],
             examples=[
                 ex("Мы жи'ли в дере'вне весь ме'сяц.", "We lived in the countryside for a whole month.", "весь ме'сяц"),
                 ex("Она' рабо'тала там всю неде'лю.", "She worked there all week.", "всю неде'лю"),
                 ex("Они' отдыха'ли всё ле'то.", "They relaxed all summer.", "всё ле'то"),
                 ex("Я бу'ду жить в А'нглии весь год.", "I will live in England for the whole year.", "весь год"),
             ]),
        card("Exactly or about?",
             "To say “about” with a number of units of time, reverse the order: the unit comes first and the number "
             "second. Compare два часа' (exactly two hours) and часа' два (about two hours). The same reversal "
             "works with в, че'рез and за: в во'семь часо'в → часо'в в во'семь, че'рез три часа' → часа' че'рез три.",
             tables=[table(
                 ["Exact", "About"],
                 [["два часа'", "часа' два"],
                  ["три неде'ли", "неде'ли три"],
                  ["в во'семь часо'в", "часо'в в во'семь"],
                  ["че'рез три часа'", "часа' че'рез три"],
                  ["за два часа'", "часа' за два"]])],
             examples=[
                 ex("Он де'лал дома'шнюю рабо'ту два часа'.", "He did the homework for two hours.", "два часа'"),
                 ex("Он де'лал дома'шнюю рабо'ту часа' два.", "He did the homework for about two hours.", "часа' два"),
                 ex("Я бу'ду в институ'те часо'в в во'семь.", "I will be at the institute around eight.", "часо'в в во'семь"),
                 ex("Я чита'ю э'ту кни'гу уже' мину'т два'дцать.", "I have been reading this book for about twenty minutes.", "мину'т два'дцать"),
             ]),
    ],
    verify=(vf("весь", "весь", "всю", "всё", "все") + vf("лето", "лето") + vf("неделя", "неделю")
            + vf("час", "часа", "часов")),
    exercises=[
        fb("Мы жи'ли в дере'вне ___ ме'сяц.", ["весь", "вся", "всё", "все"], "весь",
           "Ме'сяц is masculine: весь.", tr="We lived in the country for a whole month.", lemma="весь"),
        fb("Она' рабо'тала всю ___.", ["неде'лю", "неде'ля", "неде'ли", "неде'ле"], "неде'лю",
           "Feminine accusative: -у.", tr="She worked all week.", lemma="неделя"),
        fb("Они' отдыха'ли ___ ле'то.", ["всё", "весь", "вся", "все"], "всё",
           "Ле'то is neuter: всё.", tr="They relaxed all summer.", lemma="весь"),
        fb("Мы бу'дем до'ма ___ день.", ["весь", "вся", "всё", "все"], "весь",
           "День is masculine: весь.", tr="We will be at home all day.", lemma="весь"),
        fb("Я бу'ду в институ'те ___ в во'семь. (about)", ["часо'в", "часа'", "час", "часы'"], "часо'в",
           "For “about”, put the unit first: часо'в в во'семь.", tr="I'll be at the institute around eight.", lemma="час"),
        fb("Он де'лал дома'шнюю рабо'ту ___ два. (about)", ["часа'", "часо'в", "час", "часы'"], "часа'",
           "Часа' два = about two hours.", tr="He did the homework for about two hours.", lemma="час"),
        mc("Which phrase means “about three weeks”?", ["неде'ли три", "три неде'ли", "три неде'ль", "неде'ль три"], "неде'ли три",
           "Reverse the order: unit first."),
        mc("Which sentence means “exactly two hours”?",
           ["Он чита'л два часа'.", "Он чита'л часа' два.", "Он чита'л два час.", "Он чита'л часы' два."],
           "Он чита'л два часа'.", "Number first = exactly."),
        mc("Which form of весь goes with ночь (feminine, accusative)?", ["всю", "вся", "весь", "всё"], "всю",
           "Всю ночь.", order=True),
        mc("In what case is the time word after весь to show duration?", ["accusative", "prepositional", "nominative", "genitive"],
           "accusative", "Весь день, всю неде'лю.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 74
L74 = lesson(
    "Review: aspects, meals and time expressions",
    "Putting lessons 66 to 73 together",
    requires=["быть", "готовить", "завтрак", "месяц", "весь"],
    cards=[
        card("What you can do now",
             "You can form both futures (бу'ду + infinitive, or the perfective conjugated like a present), "
             "choose between the aspects in the past and the future, use когда' and е'сли with the future, name "
             "meals and talk about eating and drinking, say in which month, year or week something happens, and "
             "express duration with весь and approximate time by reversing number and noun.",
             tables=[table(
                 ["Topic", "Remember"],
                 [["Imperfective future", "я бу'ду де'лать"],
                  ["Perfective future", "я сде'лаю · я вста'ну"],
                  ["Duration, repeated", "imperfective: два часа' · ка'ждый день"],
                  ["Result, one occasion", "perfective: уже' · наконе'ц"],
                  ["Months, years, weeks", "в феврале' · в э'том году' · на э'той неде'ле"],
                  ["Whole period", "весь день · всю неде'лю · всё ле'то"]])],
             examples=[
                 ex("Когда' я прочита'ю э'ту кни'гу, я бу'ду отдыха'ть всю неде'лю.", "When I finish this book I'll relax for the whole week.", "всю неде'лю"),
             ]),
    ],
    verify=[],
    exercises=[
        fb("За'втра мы ___ рабо'тать до шести'.", ["бу'дем", "бу'ду", "бу'дет", "бу'дут"], "бу'дем",
           "Imperfective future of быть for мы.", tr="Tomorrow we will be working until six.", lemma="быть"),
        fb("В суббо'ту я ___ дома'шнюю рабо'ту.", ["сде'лаю", "бу'ду сде'лать", "сде'лал", "сде'лает"], "сде'лаю",
           "Perfective future, first person.", tr="On Saturday I will do my homework.", lemma="сделать"),
        fb("Вчера' мы весь ве'чер ___ уро'ки.", ["де'лали", "сде'лали"], "де'лали",
           "Весь ве'чер = duration: imperfective.", tr="Yesterday we did lessons all evening."),
        fb("Наконе'ц я ___ э'ту кни'гу!", ["прочита'л", "чита'л"], "прочита'л",
           "Наконе'ц: perfective.", tr="At last I have read this book!"),
        fb("Е'сли ты ___ ра'но, мы бу'дем за'втракать вме'сте.", ["вста'нешь", "встал", "встаёшь", "вста'нут"], "вста'нешь",
           "Future condition: future tense.", tr="If you get up early, we'll have breakfast together.", lemma="встать"),
        fb("На ___ я ем ка'шу и пью чай.", ["за'втрак", "за'втрака", "за'втраке", "за'втраку"], "за'втрак",
           "For a meal: на + accusative.", tr="For breakfast I eat porridge and drink tea.", lemma="завтрак"),
        fb("Мы бы'ли в Москве' в ___.", ["апре'ле", "апре'ль", "апре'ля", "апре'лю"], "апре'ле",
           "In a month: prepositional.", tr="We were in Moscow in April.", lemma="апрель"),
        fb("В э'том ___ я бу'ду жить в дере'вне.", ["году'", "год", "го'да", "го'ды"], "году'",
           "Год has the place form -у'.", tr="This year I will live in the countryside.", lemma="год"),
        fb("Она' рабо'тала там ___ неде'лю.", ["всю", "вся", "весь", "всё"], "всю",
           "Feminine accusative: всю.", tr="She worked there all week.", lemma="весь"),
        mc("Which phrase means “about two hours”?", ["часа' два", "два часа'", "два часо'в", "часо'в два"], "часа' два",
           "Reverse the order for “about”."),
        mc("Which aspect follows как то'лько?", ["perfective", "imperfective", "both", "neither"], "perfective",
           "A completed action.", order=True),
        mc("Which sentence is correct?",
           ["Когда' я бу'ду в Москве', я бу'ду ходи'ть в музе'и.", "Когда' я в Москве' был, я бу'ду ходи'ть в музе'и.",
            "Когда' я есть в Москве', я бу'ду ходи'ть в музе'и.", "Когда' я бу'ду в Москве', я бу'ду ходил в музе'и."],
           "Когда' я бу'ду в Москве', я бу'ду ходи'ть в музе'и.", "Future in both clauses."),
    ],
)

UNIT = unit("Unit 10: Aspect, meals and time expressions",
            [L66, L67, L68, L69, L70, L71, L72, L73, L74])
