"""Unit 33: real and unreal conditions; direct and indirect speech; the particle ли;
final reviews (textbook module 7, lessons 40-41)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 328
L328 = lesson(
    "Real conditions: Е'сли опозда'ет, она' позвони'т",
    "Е'сли за'втра пойдёт дождь, мы не пое'дем.",
    requires=["если", "позвонить", "дождь", "обязательно", "билет"],
    cards=[
        card("Condition and result",
             "A conditional sentence has a condition (е'сли …) and a result (то …). The word то is optional, and the two parts can swap places. If the result comes first, то is dropped.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["Е'сли X, (то) Y", "Е'сли О'ля опозда'ет, она' позвони'т."],
                  ["Y, е'сли X", "Она' позвони'т, е'сли опозда'ет."]])],
             examples=[
                 ex("Е'сли О'ля опозда'ет, она' обяза'тельно позвони'т.", "If Olya is late, she will definitely call.", "Е'сли О'ля опозда'ет"),
                 ex("Пикни'к отме'нят, е'сли пойдёт дождь.", "The picnic will be cancelled if it rains.", "е'сли пойдёт дождь"),
             ]),
        card("Future in both parts",
             "English uses the present in the condition (‘if it rains’). Russian uses the future in both parts, because the action has not happened yet.",
             tables=[table(
                 ["English", "Russian"],
                 [["If you send the parcel today, it will arrive.", "Е'сли ты отпра'вишь посы'лку сего'дня, её доста'вят."],
                  ["If I have time, I will call.", "Е'сли у меня' бу'дет вре'мя, я позвоню'."]])],
             examples=[
                 ex("Е'сли у меня' бу'дет вре'мя, я позвоню'.", "If I have time, I'll call.", "бу'дет вре'мя"),
             ]),
        card("One time or many times",
             "Choose the aspect as you would in any future sentence. A single event takes the perfective future; a repeated one takes бу'ду + infinitive.",
             tables=[table(
                 ["Meaning", "Sentence"],
                 [["single", "Е'сли ты придёшь, я бу'ду рад."],
                  ["repeated", "Е'сли у меня' бу'дут де'ньги, я бу'ду ча'сто путеше'ствовать."]])],
             examples=[
                 ex("Е'сли у нас бу'дут биле'ты, мы пое'дем.", "If we have tickets, we'll go.", "бу'дут биле'ты"),
             ]),
    ],
    verify=(vf("опоздать", "опоздает") + vf("позвонить", "позвонит", "позвоню") + vf("отправить", "отправишь") + vf("доставить", "доставят")
            + vf("прийти", "придёшь") + vf("поехать", "поедем") + vf("пойти", "пойдёт") + vf("отменить", "отменят") + vf("посылка", "посылку")),
    exercises=[
        F("Е'сли за'втра ___ дождь, пикни'к отме'нят. (rains)", "пойдёт", ["шло", "шёл", "шла"], "Future in the condition part.", "If it rains tomorrow, the picnic will be cancelled.", lemma="пойти"),
        F("Е'сли О'ля ___, она' позвони'т. (is late)", "опозда'ет", ["опозда'ла", "опа'здывала", "опозда'ть"], "Future perfective in the condition.", "If Olya is late, she'll call.", lemma="опоздать"),
        F("Е'сли ты ___ посы'лку сего'дня, её доста'вят в пя'тницу. (send)", "отпра'вишь", ["отпра'вил", "отправля'л", "отпра'вить"], "Future perfective.", "If you send the parcel today, it will be delivered on Friday.", lemma="отправить"),
        F("Е'сли за'втра у меня' ___ вре'мя, я позвоню'. (there is)", "бу'дет", ["бу'дут", "бы'ло", "был"], "Future of быть.", "If I have time tomorrow, I'll call.", lemma="быть"),
        F("Е'сли ты придёшь, я ___ рад. (will be)", "бу'ду", ["был", "бы", "быть"], "Future in the result.", "If you come, I'll be glad.", lemma="быть"),
        F("Я позвоню', ___ у меня' бу'дет вре'мя. (if)", "е'сли", ["е'сли бы", "ли", "что'бы"], "Real condition: е'сли.", "I'll call if I have time."),
        mc("Which sentence has the result first?", ["Мы пое'дем, е'сли бу'дут биле'ты.", "Е'сли бу'дут биле'ты, мы пое'дем.", "Е'сли бу'дут биле'ты, то мы пое'дем.", "Е'сли бы бы'ли биле'ты, мы пое'хали бы."], "Мы пое'дем, е'сли бу'дут биле'ты.", "Result, then condition (no то).", order=True),
        mc("What tense is used after е'сли in a real future condition?", ["future", "past", "present only", "infinitive"], "future", "Both parts use the future.", order=True),
        mc("Is то required in ‘Е'сли опозда'ет, то позвони'т’?", ["no, it is optional", "yes, always", "only in questions", "only with бы"], "no, it is optional", "То can be dropped.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 329
L329 = lesson(
    "Unreal conditions: Е'сли бы я знал, я бы сказал",
    "Е'сли бы я знал отве'т, я бы тебе' сказа'л.",
    requires=["если", "бы", "знать", "ответ", "сказать", "помочь", "хотеть"],
    cards=[
        card("бы in both parts",
             "An unreal condition describes something that is not or was not true. Add бы to both parts, and put the verb in the past tense.",
             tables=[table(
                 ["Part", "Form"],
                 [["condition", "е'сли бы + past tense"],
                  ["result", "past tense + бы (or бы + past tense)"]])],
             examples=[
                 ex("Е'сли бы я знал отве'т, я бы тебе' сказа'л.", "If I knew the answer, I would tell you. / If I had known, I would have told you.", "Е'сли бы я знал"),
             ]),
        card("Tense comes from the context",
             "Past-tense forms with бы do not tell you when. The context decides: now, in the past, or in the future.",
             tables=[table(
                 ["Sentence", "Possible meanings"],
                 [["Е'сли бы у меня' бы'ли де'ньги, я бы купи'л маши'ну.", "If I had money (now), I would buy a car. / If I had had money, I would have bought one."],
                  ["Е'сли бы вчера' бы'ло тепле'е, мы бы пошли' на пляж.", "If it had been warmer yesterday, we would have gone to the beach."]])],
             examples=[
                 ex("Е'сли бы вчера' бы'ло тепле'е, мы бы пошли' на пляж.", "If it had been warmer yesterday, we would have gone to the beach.", "Е'сли бы вчера' бы'ло тепле'е"),
             ]),
        card("Я бы хоте'л(а)",
             "The phrase я бы хоте'л(а) + infinitive is a polite way to say ‘I would like to …’.",
             tables=[table(
                 ["Speaker", "Phrase"],
                 [["man", "Я бы хоте'л поговори'ть с дире'ктором."],
                  ["woman", "Я бы хоте'ла поговори'ть с дире'ктором."]])],
             examples=[
                 ex("Я бы хоте'ла заказа'ть сто'лик.", "I would like to reserve a table.", "Я бы хоте'ла"),
             ]),
    ],
    verify=(vf("знать", "знал") + vf("сказать", "сказал") + vf("купить", "купил") + vf("хотеть", "хотела", "хотел") + vf("пойти", "пошли")
            + vf("помочь", "помогла") + vf("директор", "директором")),
    exercises=[
        F("Е'сли ___ я знал отве'т, я сказа'л бы. (would)", "бы", ["что'бы", "ли", "же"], "Бы after е'сли.", "If I knew the answer, I would say it."),
        F("Е'сли бы я ___ отве'т, я бы тебе' сказа'л. (knew)", "знал", ["зна'ю", "бу'ду знать", "узна'ю"], "Past tense with бы.", "If I knew the answer, I would tell you.", lemma="знать"),
        F("Е'сли бы у меня' бы'ли де'ньги, я ___ бы маши'ну. (would buy)", "купи'л", ["куплю'", "покупа'ю", "купи'ть"], "Past tense with бы.", "If I had money, I would buy a car.", lemma="купить"),
        F("Е'сли бы вчера' бы'ло тепле'е, мы ___ бы на пляж. (would have gone)", "пошли'", ["пойдём", "идём", "идти'"], "Past tense with бы.", "If it had been warmer yesterday, we would have gone to the beach.", lemma="пойти"),
        F("Я ___ хоте'ла заказа'ть сто'лик. (would)", "бы", ["бу'ду", "ли", "же"], "Polite: я бы хоте'ла.", "I would like to reserve a table."),
        F("Е'сли бы Ма'ша ___ нас, мы бы ей помогли'. (had asked)", "попроси'ла", ["попро'сит", "про'сит", "попроси'ть"], "Past + бы.", "If Masha had asked us, we would have helped her.", lemma="попросить"),
        mc("Which sentence is unreal?", ["Е'сли бы я знал, я бы сказа'л.", "Е'сли я узна'ю, я скажу'.", "Е'сли ты придёшь, я бу'ду рад.", "Когда' я узна'ю, я скажу'."], "Е'сли бы я знал, я бы сказа'л.", "Бы in both parts.", order=True),
        mc("Which means ‘I would like to …’ (said by a woman)?", ["Я бы хоте'ла …", "Я бу'ду хоте'ть …", "Я хоте'ла …", "Я хочу' бы …"], "Я бы хоте'ла …", "Past tense with бы.", order=True),
        mc("After бы the verb is always in:", ["the past tense", "the future tense", "the infinitive", "the present tense"], "the past tense", "бы + past.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 330
L330 = lesson(
    "Where does бы go? Also short б and repeated ‘would’",
    "Е'сли б не ты, я не успе'л бы.",
    requires=["если", "бы", "экзамен", "рейс", "успеть"],
    cards=[
        card("Position of бы",
             "In the condition, бы must stand right after е'сли. In the result part it is free: it can come before the verb, after the verb, or after the subject.",
             tables=[table(
                 ["Order", "Example"],
                 [["бы before the verb", "Е'сли бы Ва'ня вы'учил слова', он бы сдал экза'мен."],
                  ["бы after the verb", "Е'сли бы Ва'ня вы'учил слова', он сдал бы экза'мен."]])],
             examples=[
                 ex("Е'сли бы Ва'ня вы'учил слова', он сдал бы экза'мен.", "If Vanya had learned the words, he would have passed the exam.", "он сдал бы"),
             ]),
        card("Short б",
             "In informal speech, and sometimes in writing, бы is shortened to б. It attaches to the previous word.",
             tables=[table(
                 ["Full", "Short"],
                 [["Е'сли бы не ты …", "Е'сли б не ты …"],
                  ["Я бы пошёл.", "Я б пошёл."],
                  ["Ты бы позвони'л.", "Ты б позвони'л."]])],
             examples=[
                 ex("Е'сли б не ты, я не успе'л бы.", "If it weren't for you, I wouldn't have made it.", "Е'сли б не ты"),
             ]),
        card("Repeated ‘would’ is not unreal",
             "English ‘would’ can mean a past habit. In Russian this is just the past imperfective, with no бы.",
             tables=[table(
                 ["English", "Russian"],
                 [["When I was little, we would go to the beach on weekends.", "Когда' я был ма'леньким, мы е'здили на пляж по выходны'м."],
                  ["If I were little, I would go.", "Е'сли бы я был ма'леньким, я бы пошёл."]])],
             examples=[
                 ex("Когда' я был ма'леньким, мы е'здили на пляж.", "When I was little, we would go to the beach.", "е'здили"),
             ]),
    ],
    verify=(vf("выучить", "выучил") + vf("сдать", "сдал") + vf("успеть", "успел") + vf("ездить", "ездили") + vf("пойти", "пошёл")
            + vf("позвонить", "позвонил") + vf("маленький", "маленьким")),
    exercises=[
        F("Е'сли бы Ва'ня вы'учил слова', он ___ бы экза'мен. (would have passed)", "сдал", ["сдаст", "сдава'л", "сдать"], "Past + бы.", "If Vanya had learned the words, he would have passed the exam.", lemma="сдать"),
        F("Е'сли ___ не ты, я бы опозда'л. (short form)", "б", ["бы", "ли", "же"], "Short бы.", "If it weren't for you, I would have been late."),
        F("Ты ___ позвони'л ей. (would/should)", "бы", ["ли", "бу'дет", "же"], "Past + бы.", "You should call her."),
        F("Когда' я был ма'леньким, мы ___ на пляж по выходны'м. (would go)", "е'здили", ["е'здили бы", "пое'хали бы", "пое'дем"], "Past habit: imperfective, no бы.", "When I was little, we would go to the beach on weekends.", lemma="ездить"),
        F("Е'сли бы я ___ раньше, я бы успе'л. (had left)", "вы'шел", ["вы'йду", "выхожу'", "выходи'ть"], "Past + бы.", "If I had left earlier, I would have made it.", lemma="выйти"),
        mc("Where must бы stand in the condition clause?", ["right after е'сли", "at the end", "before the subject", "it is optional"], "right after е'сли", "Е'сли бы.", order=True),
        mc("Which version is NOT correct?", ["Он сдал бы бы экза'мен.", "Он бы сдал экза'мен.", "Он сдал бы экза'мен.", "Он экза'мен сдал бы."], "Он сдал бы бы экза'мен.", "Only one бы in the result.", order=True),
        mc("‘Е'сли б не ты’ is:", ["informal for ‘е'сли бы не ты’", "a question", "a real condition", "a command"], "informal for ‘е'сли бы не ты’", "Б = бы.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 331
L331 = lesson(
    "If it weren't for: Е'сли бы не спаса'тели, мы поги'бли бы",
    "Е'сли бы не ве'тер, день был бы идеа'льным.",
    requires=["если", "бы", "спасатель", "ветер", "идеальный", "погибнуть"],
    cards=[
        card("Е'сли бы не + noun",
             "When the condition is just ‘не + noun’ with no verb, it means ‘if it weren't / hadn't been for …’.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["Е'сли бы не + nominative", "Е'сли бы не спаса'тели, мы поги'бли бы."],
                  ["", "Е'сли бы не ве'тер, день был бы идеа'льным."]])],
             examples=[
                 ex("Е'сли бы не спаса'тели, мы поги'бли бы.", "If it hadn't been for the rescuers, we would have died.", "Е'сли бы не спаса'тели"),
                 ex("Е'сли бы не ве'тер, день был бы идеа'льным.", "If it weren't for the wind, it would be an ideal day.", "Е'сли бы не ве'тер"),
             ]),
        card("The noun stays in the nominative",
             "Unlike English ‘but for’, Russian does not change the noun's case after не.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Е'сли бы не ты, я бы не успе'л.", "If it weren't for you, I wouldn't have made it."],
                  ["Е'сли бы не дождь, мы бы гуля'ли.", "If it weren't for the rain, we would be walking."]])],
             examples=[
                 ex("Е'сли бы не дождь, мы бы гуля'ли.", "If it weren't for the rain, we would be walking.", "Е'сли бы не дождь"),
             ]),
        card("Advice with бы",
             "Бы + past can also give advice or express a wish. Often used with на твоём ме'сте: ‘if I were you’.",
             tables=[table(
                 ["Phrase", "English"],
                 [["На твоём ме'сте я бы позвони'л.", "In your place I would call."],
                  ["Тебе' бы отдохну'ть.", "You should rest (I wish you would)."]])],
             examples=[
                 ex("На твоём ме'сте я бы позвони'л.", "In your place I would call.", "На твоём ме'сте"),
             ]),
    ],
    verify=(vf("спасатель", "спасатели") + vf("погибнуть", "погибли") + vf("ветер", "ветер") + vf("идеальный", "идеальным")
            + vf("успеть", "успел") + vf("гулять", "гуляли") + vf("позвонить", "позвонил") + vf("отдохнуть", "отдохнуть")),
    exercises=[
        F("Е'сли бы не ___, мы бы погибли. (the rescuers)", "спаса'тели", ["спаса'телей", "спаса'телям", "спаса'телями"], "Nominative after не.", "If it hadn't been for the rescuers, we would have died.", lemma="спасатель"),
        F("Е'сли бы не ___, я бы не успе'л. (you)", "ты", ["тебя'", "тебе'", "тобой"], "Nominative after не.", "If it weren't for you, I wouldn't have made it."),
        F("Е'сли бы не ___, день был бы идеа'льным. (the wind)", "ве'тер", ["ве'тра", "ве'тру", "ве'тром"], "Nominative after не.", "If it weren't for the wind, the day would be ideal.", lemma="ветер"),
        F("Е'сли бы не дождь, мы бы ___. (would be walking)", "гуля'ли", ["гуля'ем", "погуля'ем", "гуля'ть"], "Past + бы.", "If it weren't for the rain, we would be walking.", lemma="гулять"),
        F("На твоём ме'сте я ___ позвони'л. (would)", "бы", ["ли", "же", "бу'ду"], "Past + бы.", "In your place I would call."),
        mc("Which means ‘If it weren't for you’?", ["Е'сли бы не ты", "Е'сли не ты", "Е'сли бы нет тебя'", "Е'сли бы не тебя'"], "Е'сли бы не ты", "Nominative after не.", order=True),
        mc("What case follows ‘Е'сли бы не’?", ["nominative", "genitive", "dative", "accusative"], "nominative", "The noun is the ‘cause’ and stays in the nominative.", order=True),
        mc("‘На твоём ме'сте я бы позвони'л’ means:", ["In your place I would call.", "I called you.", "I will call you.", "You must call."], "In your place I would call.", "Advice with бы.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 332
L332 = lesson(
    "Real or unreal? Е'сли придёт … / Е'сли бы пришёл …",
    "Е'сли он придёт, я бу'ду рад. Е'сли бы он пришёл, я был бы рад.",
    requires=["если", "бы", "болеть", "заболеть", "работа", "дорогой", "билет"],
    cards=[
        card("Two kinds of condition",
             "A real condition is open: it might happen. An unreal condition is contrary to fact, or very unlikely. Russian marks the difference with бы.",
             tables=[table(
                 ["Real (no бы)", "Unreal (бы)"],
                 [["Е'сли он придёт, я бу'ду рад.", "Е'сли бы он пришёл, я был бы рад."],
                  ["Е'сли за'втра бу'дет тепло', мы пойдём гуля'ть.", "Е'сли бы сего'дня бы'ло тепло', мы пошли' бы гуля'ть."],
                  ["Е'сли ты заболе'ешь, оста'нешься до'ма.", "Е'сли бы ты заболе'л, ты оста'лся бы до'ма."]])],
             examples=[
                 ex("Е'сли он придёт, я бу'ду рад.", "If he comes (and he may), I'll be glad.", "Е'сли он придёт"),
                 ex("Е'сли бы он пришёл, я был бы рад.", "If he had come (he didn't), I would have been glad.", "Е'сли бы он пришёл"),
             ]),
        card("How to decide",
             "Ask: is the situation still possible? If yes, use a real condition. If it is false, or has already turned out differently, use бы.",
             tables=[table(
                 ["Situation", "Choice"],
                 [["Tomorrow, maybe it will rain.", "real: Е'сли за'втра пойдёт дождь …"],
                  ["It is not raining now, but I imagine it.", "unreal: Е'сли бы шёл дождь …"],
                  ["Yesterday I was ill and didn't go.", "unreal: Е'сли бы я не боле'л, я пошёл бы."]])],
             examples=[
                 ex("Е'сли бы Ди'ма не боле'л, он пошёл бы на рабо'ту.", "If Dima weren't ill, he would go to work.", "Е'сли бы Ди'ма не боле'л"),
             ]),
        card("Reasons that explain what did not happen",
             "A good way to practise: take a sentence ‘I didn't X because Y’ and flip it to ‘If not Y, I would X’.",
             tables=[table(
                 ["Fact", "Unreal condition"],
                 [["Я не купи'л телефо'н, потому' что он до'рог.", "Е'сли бы телефо'н не был до'рог, я купи'л бы его'."],
                  ["Мы не пошли' в кино', потому' что не бы'ло биле'тов.", "Е'сли бы бы'ли биле'ты, мы пошли' бы в кино'."]])],
             examples=[
                 ex("Е'сли бы бы'ли биле'ты, мы пошли' бы в кино'.", "If there had been tickets, we would have gone to the movies.", "Е'сли бы бы'ли биле'ты"),
             ]),
    ],
    verify=(vf("прийти", "придёт", "пришёл") + vf("заболеть", "заболеешь", "заболел") + vf("болеть", "болел") + vf("остаться", "останешься", "остался")
            + vf("купить", "купил") + vf("пойти", "пойдём", "пошли") + vf("дорогой", "дорог")),
    exercises=[
        F("Е'сли он ___, я бу'ду рад. (comes — possible)", "придёт", ["пришёл", "пришёл бы", "приходи'л"], "Real: future, no бы.", "If he comes, I'll be glad.", lemma="прийти"),
        F("Е'сли бы он ___, я был бы рад. (had come — he didn't)", "пришёл", ["придёт", "прихо'дит", "прийти'"], "Unreal: past + бы.", "If he had come, I would have been glad.", lemma="прийти"),
        F("Е'сли за'втра бу'дет тепло', мы ___ гуля'ть. (will go)", "пойдём", ["пошли' бы", "ходи'ли", "идти'"], "Real: future in the result.", "If it is warm tomorrow, we'll go for a walk.", lemma="пойти"),
        F("Е'сли бы сего'дня бы'ло тепло', мы ___ бы гуля'ть. (would go)", "пошли'", ["пойдём", "идём", "идти'"], "Unreal: past + бы.", "If it were warm today, we would go for a walk.", lemma="пойти"),
        F("Е'сли бы Ди'ма не ___, он пошёл бы на рабо'ту. (were ill)", "боле'л", ["бу'дет боле'ть", "боле'ет", "заболе'ет"], "Unreal.", "If Dima weren't ill, he would go to work.", lemma="болеть"),
        mc("‘Tomorrow it may rain’ calls for:", ["a real condition", "an unreal condition", "a question with ли", "a command"], "a real condition", "Still possible.", order=True),
        mc("‘I would go if I had a ticket (but I don't)’ calls for:", ["an unreal condition", "a real condition", "indirect speech", "a participle"], "an unreal condition", "Contrary to fact.", order=True),
        mc("Choose the unreal sentence.", ["Е'сли бы бы'ли биле'ты, мы пошли' бы в кино'.", "Е'сли бу'дут биле'ты, мы пойдём в кино'.", "Е'сли есть биле'ты, мы идём.", "Когда' бу'дут биле'ты, мы пойдём."], "Е'сли бы бы'ли биле'ты, мы пошли' бы в кино'.", "Бы in both parts.", order=True),
        mc("Choose the real sentence.", ["Е'сли ты заболе'ешь, оста'нешься до'ма.", "Е'сли бы ты заболе'л, ты оста'лся бы до'ма.", "Е'сли б ты заболе'л, ты оста'лся б до'ма.", "Е'сли ты бы заболе'л, ты оста'лся бы до'ма."], "Е'сли ты заболе'ешь, оста'нешься до'ма.", "No бы.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 333
L333 = lesson(
    "Direct and indirect speech: Ле'на сказа'ла, что она' бу'дет до'ма",
    "Ле'на сказа'ла, что она' бу'дет до'ма че'рез час.",
    requires=["сказать", "что", "думать", "знать", "заказать", "обед", "родитель", "работа"],
    cards=[
        card("Quoting and reporting",
             "Direct speech uses quotation marks and a dash before the speaker. Indirect (reported) speech uses что. Pronouns shift to fit the speaker.",
             tables=[table(
                 ["Direct", "Indirect"],
                 [["«Сего'дня мой день рожде'ния», — сказа'ла А'ня.", "А'ня сказа'ла, что сего'дня её день рожде'ния."],
                  ["Ле'на сказа'ла: «Я бу'ду до'ма че'рез час».", "Ле'на сказа'ла, что она' бу'дет до'ма че'рез час."]])],
             examples=[
                 ex("А'ня сказа'ла, что сего'дня её день рожде'ния.", "Anya said that today was her birthday.", "сказа'ла, что"),
             ]),
        card("The tense stays the same",
             "Unlike English, Russian does not shift the tense back. It reports the tense of the original statement.",
             tables=[table(
                 ["Original", "Indirect speech"],
                 [["Ле'на: «Я бу'ду до'ма».", "Ле'на сказа'ла, что бу'дет до'ма. (will be)"],
                  ["Вади'м: «Я не зна'ю, что заказа'ть».", "Вади'м сказа'л, что не зна'ет, что заказа'ть. (didn't know)"],
                  ["Ди'ма: «Мои' роди'тели на рабо'те».", "Ди'ма ду'мал, что его' роди'тели на рабо'те. (were at work)"]])],
             examples=[
                 ex("Вади'м сказа'л, что не зна'ет, что заказа'ть.", "Vadim said he didn't know what to order.", "не зна'ет"),
             ]),
        card("A tense can change the meaning",
             "Because the tense follows the original statement, a past tense in the clause means ‘used to’.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Я не знал, что Ма'ша живёт ря'дом.", "I didn't know Masha lived next door."],
                  ["Я не знал, что Ма'ша жила' ря'дом.", "I didn't know Masha used to live next door."]])],
             examples=[
                 ex("Я не знал, что Ма'ша живёт ря'дом.", "I didn't know that Masha lived next door.", "живёт"),
             ]),
    ],
    verify=(vf("сказать", "сказала", "сказал") + vf("думать", "думал") + vf("знать", "знает", "знал") + vf("заказать", "заказать")
            + vf("жить", "живёт", "жила") + vf("родитель", "родители") + vf("быть", "будет")),
    exercises=[
        F("А'ня сказа'ла, ___ сего'дня её день рожде'ния. (that)", "что", ["чтобы", "е'сли", "ли"], "Reported statement: что.", "Anya said that today was her birthday."),
        F("Ле'на сказа'ла, что она' ___ до'ма че'рез час. (will be)", "бу'дет", ["была'", "быть", "бы'ло"], "Same tense as the original: future.", "Lena said she would be home in an hour.", lemma="быть"),
        F("Вади'м сказа'л, что не ___, что заказа'ть. (knows)", "зна'ет", ["знал", "узна'ет", "бу'дет знать"], "Same tense as the original: present.", "Vadim said he didn't know what to order.", lemma="знать"),
        F("Ди'ма ду'мал, что роди'тели ещё ___. (are sleeping)", "спят", ["спа'ли", "бу'дут спать", "спать"], "Same tense as the original thought: present.", "Dima thought his parents were still asleep.", lemma="спать"),
        F("Я не знал, что Ма'ша ___ ря'дом. (lives)", "живёт", ["жила'", "жил", "бу'дет жить"], "Present: she was living there.", "I didn't know that Masha lived next door.", lemma="жить"),
        F("Я не знал, что Ма'ша ___ ря'дом. (used to live)", "жила'", ["живёт", "жил", "бу'дет жить"], "Past: ‘used to’.", "I didn't know that Masha used to live next door.", lemma="жить"),
        mc("In ‘Ле'на сказа'ла, что бу'дет до'ма’ the verb бу'дет is future because:", ["Lena's original statement was future", "Russian never uses the past after что", "English requires it", "the main verb is perfective"], "Lena's original statement was future", "Same tense as the original.", order=True),
        mc("Which connector introduces reported statements?", ["что", "ли", "бы", "е'сли"], "что", "Сказа'ть, что.", order=True),
        mc("Which sentence means ‘Anya said she was tired’?", ["А'ня сказа'ла, что она' уста'ла.", "А'ня сказа'ла, что бу'дет уставать.", "А'ня сказа'ла, что устанет.", "А'ня сказа'ла, ли она' уста'ла."], "А'ня сказа'ла, что она' уста'ла.", "Past statement.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 334
L334 = lesson(
    "Indirect questions with question words: Са'ша спроси'л, где они'",
    "Я не зна'ю, почему' она' перее'хала в Москву'.",
    requires=["спросить", "где", "когда", "почему", "куда", "откуда", "зачем", "узнать"],
    cards=[
        card("Same word, no inversion",
             "To report a question with a question word, keep that word and move on. The tense is still that of the original question.",
             tables=[table(
                 ["Direct question", "Indirect question"],
                 [["Где они'?", "Са'ша спроси'л меня', где они'."],
                  ["Почему' она' перее'хала в Москву'?", "Я не зна'ю, почему' она' перее'хала в Москву'."],
                  ["Когда' он придёт домо'й?", "Я спроси'л, когда' он придёт домо'й."]])],
             examples=[
                 ex("Са'ша спроси'л меня', где они'.", "Sasha asked me where they were.", "где они'"),
                 ex("Я спроси'л, когда' он придёт домо'й.", "I asked when he would be home.", "когда' он придёт"),
             ]),
        card("Question words you can report",
             "Any question word can start the indirect clause. Put a comma before it.",
             tables=[table(
                 ["Word", "English"],
                 [["где / куда' / отку'да", "where / where to / where from"],
                  ["когда'", "when"],
                  ["почему' / заче'м", "why / what for"],
                  ["как", "how"],
                  ["ско'лько", "how many / how much"],
                  ["кто / что", "who / what"]])],
             examples=[
                 ex("Он спроси'л, куда' мы идём.", "He asked where we were going.", "куда' мы идём"),
             ]),
        card("With an infinitive",
             "If the subject of the question is the speaker, Russian often uses an infinitive: ‘I don't know what to order’.",
             tables=[table(
                 ["Sentence", "English"],
                 [["Я не зна'ю, что заказа'ть.", "I don't know what to order."],
                  ["Мы не зна'ем, куда' идти'.", "We don't know where to go."]])],
             examples=[
                 ex("Мы не зна'ем, куда' идти'.", "We don't know where to go.", "куда' идти'"),
             ]),
    ],
    verify=(vf("спросить", "спросил") + vf("прийти", "придёт") + vf("переехать", "переехала") + vf("идти", "идём", "идти")
            + vf("заказать", "заказать") + vf("знать", "знаю", "знаем")),
    exercises=[
        F("Са'ша спроси'л меня', ___ они'. (where)", "где", ["куда'", "когда'", "зачем"], "Они' — where are they?", "Sasha asked me where they were.", lemma=None),
        F("Я спроси'л, ___ он придёт домо'й. (when)", "когда'", ["где", "куда'", "кто"], "Придёт: when.", "I asked when he would be home.", lemma=None),
        F("Он спроси'л, ___ мы идём. (where to)", "куда'", ["где", "отку'да", "почему'"], "Идём: куда'?", "He asked where we were going.", lemma=None),
        F("Я не зна'ю, ___ она' перее'хала в Москву'. (why)", "почему'", ["когда'", "где", "кто"], "Why.", "I don't know why she moved to Moscow.", lemma=None),
        F("Мы не зна'ем, куда' ___. (to go)", "идти'", ["идём", "шли", "пошли'"], "Infinitive after the question word.", "We don't know where to go.", lemma="идти"),
        F("Я не зна'ю, что ___. (to order)", "заказа'ть", ["заказа'л", "закажу'", "заказа'ла"], "Infinitive after the question word.", "I don't know what to order.", lemma="заказать"),
        mc("The tense of an indirect question follows:", ["the original question", "the main verb", "English rules", "the question word"], "the original question", "Same tense as the original.", order=True),
        mc("Which sentence reports ‘Когда' ты придёшь?’?", ["Он спроси'л, когда' я приду'.", "Он спроси'л, приду' ли я.", "Он спроси'л, когда' я пришёл бы.", "Он спроси'л, е'сли я приду'."], "Он спроси'л, когда' я приду'.", "Question word stays.", order=True),
        mc("Is a comma needed before the question word in the indirect clause?", ["yes", "no", "only with ли", "only in questions"], "yes", "Russian marks every subordinate clause.", order=True),
    ],
)
# ---------------------------------------------------------------------------- 335
L335 = lesson(
    "Yes/no indirect questions: Са'ша спроси'л, здесь ли они'",
    "Я не зна'ю, есть ли у И'горя маши'на.",
    requires=["ли", "спросить", "узнать", "помнить", "забыть", "уверенный", "решить"],
    cards=[
        card("Use ли, not е'сли",
             "A yes/no question, reported, uses the particle ли. Put the focus word first, then ли, then the rest. Never use е'сли here: it only introduces a condition.",
             tables=[table(
                 ["Direct question", "Indirect question"],
                 [["Они' здесь?", "Са'ша меня' спроси'л, здесь ли они'."],
                  ["Она' перее'хала в Москву'?", "Я не был уве'рен, перее'хала ли она' в Москву'."],
                  ["Он ско'ро придёт домо'й?", "Я не мог вспо'мнить, ско'ро ли он придёт домо'й."]])],
             examples=[
                 ex("Са'ша меня' спроси'л, здесь ли они'.", "Sasha asked me if they were here.", "здесь ли они'"),
                 ex("Я не мог вспо'мнить, ско'ро ли он придёт домо'й.", "I couldn't remember if he would be home soon.", "ско'ро ли он"),
             ]),
        card("The focus decides the word order",
             "Ли goes right after the word you want to question. It is never stressed, and it is pronounced together with the word before it. Different focus words mean different questions.",
             tables=[table(
                 ["Sentence", "What is being asked"],
                 [["Са'ша спроси'л, здесь ли они'.", "Are they here (rather than elsewhere)?"],
                  ["Са'ша спроси'л, они' ли здесь.", "Is it them who are here (and not someone else)?"]])],
             examples=[
                 ex("Са'ша спроси'л, они' ли здесь.", "Sasha asked whether it was they who were here.", "они' ли здесь"),
             ]),
        card("Four small rules",
             "Keep these in mind.",
             tables=[table(
                 ["Rule", "Example"],
                 [["есть is often the focus word", "Я не зна'ю, есть ли у И'горя маши'на."],
                  ["do not add «и'ли нет»", "Ди'ма не по'мнил, закры'л ли он дверь."],
                  ["‘whether’ test", "If you can say ‘whether’, use ли."],
                  ["comma before the clause", "Не зна'ю, придёт ли он."]])],
             examples=[
                 ex("Я не зна'ю, есть ли у И'горя маши'на.", "I don't know whether Igor has a car.", "есть ли"),
             ]),
    ],
    verify=(vf("спросить", "спросил") + vf("вспомнить", "вспомнить") + vf("помнить", "помнил") + vf("закрыть", "закрыл") + vf("дверь", "дверь")
            + vf("переехать", "переехала") + vf("прийти", "придёт") + vf("машина", "машина")),
    exercises=[
        F("Са'ша спроси'л, ___ они'. (whether they are here)", "здесь ли", ["е'сли здесь", "ли здесь", "здесь е'сли"], "Focus word + ли.", "Sasha asked whether they were here.", lemma=None),
        F("Я не знал, ___ она' в Москву'. (whether she had moved)", "перее'хала ли", ["е'сли перее'хала", "ли перее'хала", "перее'хала бы"], "Focus word + ли.", "I didn't know whether she had moved to Moscow.", lemma=None),
        F("Я не зна'ю, ___ у И'горя маши'на. (whether he has)", "есть ли", ["е'сли есть", "ли есть", "есть бы"], "Есть + ли.", "I don't know whether Igor has a car.", lemma=None),
        F("Ди'ма не по'мнил, закры'л ___ он дверь. (whether)", "ли", ["е'сли", "бы", "же"], "Ли after the focus word закры'л.", "Dima didn't remember whether he had closed the door.", lemma=None),
        F("Ма'ма спроси'ла, пришли' ___ мы домо'й. (whether)", "ли", ["е'сли", "бы", "же"], "Ли after the verb.", "Mom asked whether we had come home.", lemma=None),
        mc("Which sentence is correct?", ["Я не зна'ю, придёт ли он.", "Я не зна'ю, е'сли он придёт.", "Я не зна'ю, придёт ли он и'ли нет.", "Я не зна'ю, ли придёт он."], "Я не зна'ю, придёт ли он.", "Ли follows придёт; no «и'ли нет».", order=True),
        mc("Is ли stressed?", ["no, it joins the word before it", "yes, always", "only in questions", "only in writing"], "no, it joins the word before it", "Enclitic.", order=True),
        mc("‘Они' ли здесь?’ asks:", ["whether it is they who are here", "whether they are here", "why they are here", "when they came"], "whether it is they who are here", "Focus on они'.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 336
L336 = lesson(
    "ли or е'сли? Condition vs. question; ли in direct questions",
    "Мы ещё не реши'ли, пойдём ли мы на вечери'нку.",
    requires=["если", "ли", "бы", "решить", "позвонить", "рейс", "отменить"],
    cards=[
        card("Two uses of «if»",
             "English ‘if’ covers two ideas. Condition: if X happens, Y will happen — use е'сли. Question: ‘whether’ — use ли.",
             tables=[table(
                 ["Meaning", "Russian"],
                 [["We would buy flowers if we were going to Lena's party.", "Мы купи'ли бы цветы', е'сли бы шли на вечери'нку к Ле'не."],
                  ["We hadn't decided if we were going to Lena's party.", "Мы ещё не реши'ли, пойдём ли мы на вечери'нку к Ле'не."]])],
             examples=[
                 ex("Мы ещё не реши'ли, пойдём ли мы на вечери'нку.", "We hadn't yet decided whether we were going to the party.", "пойдём ли мы"),
             ]),
        card("Another pair",
             "Tanya's flight shows both uses side by side.",
             tables=[table(
                 ["Meaning", "Russian"],
                 [["Tanya called the airport to check if her flight had been cancelled.", "Таня позвони'ла в аэропо'рт, что'бы узна'ть, отмени'ли ли её рейс."],
                  ["Tanya would've called us if her flight had been cancelled.", "Таня позвони'ла бы нам, е'сли бы её рейс отмени'ли."]])],
             examples=[
                 ex("Таня позвони'ла бы нам, е'сли бы её рейс отмени'ли.", "Tanya would have called us if her flight had been cancelled.", "е'сли бы"),
             ]),
        card("Direct questions with ли",
             "Ли can also appear in direct questions to give weight to the word before it. This is common in newspaper headlines.",
             tables=[table(
                 ["Headline", "English"],
                 [["Мо'жно ли победи'ть ста'рость?", "Can old age be defeated?"],
                  ["Поле'зно ли вегетариа'нство?", "Is vegetarianism healthy?"],
                  ["Бу'дут ли меня'ться це'ны?", "Will prices change?"]])],
             examples=[
                 ex("Мо'жно ли победи'ть ста'рость?", "Can old age be defeated?", "Мо'жно ли"),
             ]),
    ],
    verify=(vf("решить", "решили") + vf("пойти", "пойдём") + vf("купить", "купили") + vf("идти", "шли") + vf("позвонить", "позвонила")
            + vf("узнать", "узнать") + vf("отменить", "отменили") + vf("победить", "победить") + vf("меняться", "меняться")),
    exercises=[
        F("Мы ещё не реши'ли, пойдём ___ мы на вечери'нку. (whether)", "ли", ["е'сли", "бы", "же"], "A question: ли.", "We haven't yet decided whether we're going to the party.", lemma=None),
        F("Мы купи'ли бы цветы', ___ бы шли на вечери'нку. (if)", "е'сли", ["ли", "что", "что'бы"], "A condition: е'сли бы.", "We would buy flowers if we were going to the party.", lemma=None),
        F("Таня позвони'ла, что'бы узна'ть, отмени'ли ___ рейс. (whether)", "ли", ["е'сли", "бы", "же"], "A question: ли.", "Tanya called to find out whether the flight had been cancelled.", lemma=None),
        F("Таня позвони'ла бы нам, ___ бы рейс отмени'ли. (if)", "е'сли", ["ли", "что", "тоже"], "A condition.", "Tanya would have called us if the flight had been cancelled.", lemma=None),
        F("Мо'жно ___ победи'ть ста'рость? (direct question)", "ли", ["е'сли", "бы", "же"], "Ли gives weight to мо'жно.", "Can old age be defeated?", lemma=None),
        mc("Which test tells you to use ли?", ["‘whether’ fits in place of ‘if’", "‘when’ fits", "the sentence is in the past", "there is a question mark"], "‘whether’ fits in place of ‘if’", "Ли = whether.", order=True),
        mc("Which sentence is a condition?", ["Я позвоню', е'сли бу'дет вре'мя.", "Я не зна'ю, бу'дет ли вре'мя.", "Он спроси'л, есть ли вре'мя.", "Мы не реши'ли, пойдём ли мы."], "Я позвоню', е'сли бу'дет вре'мя.", "Condition → е'сли.", order=True),
        mc("Which sentence is an indirect question?", ["Мы не реши'ли, пойдём ли мы.", "Мы пойдём, е'сли бу'дет вре'мя.", "Е'сли бы мы шли, мы купи'ли бы цветы'.", "Е'сли мы пойдём, позвони'м."], "Мы не реши'ли, пойдём ли мы.", "Ли → question.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 337
L337 = lesson(
    "Final review A: collective numerals, time and verbal adverbs",
    "Тро'е су'ток шёл снег, и мы верну'лись домо'й вдвоём.",
    requires=["сутки", "половина", "четверть", "ночь", "утро", "вечер", "зима"],
    cards=[
        card("Collective numerals",
             "Use дво'е, тро'е, че'тверо for people (especially male or mixed groups), with pronouns (их бы'ло тро'е), and with plural-only nouns like су'тки.",
             tables=[table(
                 ["Case", "Example"],
                 [["with су'тки", "Тро'е су'ток шёл снег."],
                  ["with pronoun", "Их бы'ло че'тверо."],
                  ["with children", "У неё пя'теро дете'й."],
                  ["together", "вдвоём, втроём, вчетверо'м"]])],
             examples=[
                 ex("Тро'е су'ток шёл снег.", "It snowed for three days and nights.", "Тро'е су'ток"),
             ]),
        card("Telling time",
             "Полови'на + next hour (genitive) gives half past. Без че'тверти + hour gives a quarter to.",
             tables=[table(
                 ["Time", "Russian"],
                 [["7:30", "полови'на восьмо'го"],
                  ["6:45", "без че'тверти семь"],
                  ["8:15", "че'тверть девя'того"]])],
             examples=[
                 ex("Сейча'с полови'на восьмо'го.", "It is half past seven.", "полови'на восьмо'го"),
             ]),
        card("Verbal adverbs",
             "An imperfective adverb shows an action at the same time as the main verb. A perfective adverb shows one that came first.",
             tables=[table(
                 ["Type", "Example"],
                 [["simultaneous", "Идя' домо'й, он слу'шал му'зыку."],
                  ["earlier", "Сде'лав уро'ки, он пошёл гуля'ть."],
                  ["negative", "Он ушёл, не сказа'в ни сло'ва."]])],
             examples=[
                 ex("Идя' домо'й, он слу'шал му'зыку.", "Walking home, he listened to music.", "Идя'"),
                 ex("Сде'лав уро'ки, он пошёл гуля'ть.", "Having done his homework, he went out.", "Сде'лав"),
             ]),
    ],
    verify=(vf("сутки", "суток") + vf("половина", "половина") + vf("четверть", "четверти") + vf("делать", "делая") + vf("сделать", "сделав")
            + vf("слушать", "слушал") + vf("сказать", "сказав") + vf("идти", "идя") + vf("пойти", "пошёл")),
    exercises=[
        F("___ су'ток шёл снег. (three — collective form)", "Тро'е", ["Три", "Трёх", "Трои'х"], "Plural-only noun: collective numeral.", "It snowed for three days and nights."),
        F("Их бы'ло ___. (four people)", "че'тверо", ["четы'ре", "четырёх", "четвёртый"], "With a pronoun: collective.", "There were four of them.", lemma="четверо"),
        F("У неё ___ дете'й. (five — collective form)", "пя'теро", ["пять", "пяти'", "пя'тый"], "Collective numerals can count children.", "She has five children.", lemma="пятеро"),
        F("Мы пришли' ___. (the two of us)", "вдвоём", ["двое", "два", "втроём"], "Together as a group.", "We came the two of us."),
        F("Сейча'с полови'на ___. (7:30)", "восьмо'го", ["восьмо'й", "восемь", "восьмо'му"], "Half of the eighth hour.", "It is half past seven."),
        F("___ уро'ки, он пошёл гуля'ть. (having done)", "Сде'лав", ["Де'лая", "Сде'лать", "Дела'л"], "Earlier action: perfective adverb.", "Having done his homework, he went out."),
        F("___ домо'й, он слу'шал му'зыку. (walking)", "Идя'", ["Придя'", "Шёл", "Идти'"], "Simultaneous action: imperfective adverb.", "Walking home, he listened to music."),
        mc("‘Без че'тверти семь’ is:", ["6:45", "7:15", "7:30", "6:15"], "6:45", "A quarter to seven.", order=True),
        mc("Which action came first in ‘Сде'лав уро'ки, он пошёл гуля'ть’?", ["doing homework", "going out", "both at once", "neither"], "doing homework", "Perfective adverb.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 338
L338 = lesson(
    "Final review B: -ся or not, negation and то/тот",
    "Нам не'куда идти', и мы никуда' не идём.",
    requires=["снизить", "повысить", "менять", "меняться", "нечего", "никто"],
    cards=[
        card("Choosing a verb form",
             "If the verb has a direct object, use the form without -ся. If the subject is what changes, add -ся. Ask yourself: what is the subject?",
             tables=[table(
                 ["With an object", "Without an object"],
                 [["Компа'ния меня'ет фо'рму.", "Фо'рма меня'ется."],
                  ["Вла'сти сни'зят нало'г.", "Нало'г сни'зится."],
                  ["Предприя'тия увольня'ют люде'й.", "Спрос снижа'ется."]])],
             examples=[
                 ex("Спрос снижа'ется.", "Demand is falling.", "снижа'ется"),
             ]),
        card("Negation",
             "The ни- pattern describes what happens. The не'- pattern says there is nothing to do it with.",
             tables=[table(
                 ["ни- + не", "не'- + infinitive"],
                 [["Я ничего' не де'лаю.", "Мне не'чего де'лать."],
                  ["Он ни с кем не говори'т.", "Ему' не' с кем говори'ть."],
                  ["Они' никуда' не иду'т.", "Им не'куда идти'."]])],
             examples=[
                 ex("Ему' не' с кем говори'ть.", "He has no one to talk to.", "не' с кем"),
             ]),
        card("то and тот",
             "Pick the case that the first verb or preposition requires, and use то as a buffer. For people use тот, кто.",
             tables=[table(
                 ["Pattern", "Example"],
                 [["то after a verb", "Мы ве'рим тому', что они' сказа'ли."],
                  ["то after a preposition", "из-за того', что"],
                  ["people", "Те, кто нару'шил зако'н, отвеча'ют."]])],
             examples=[
                 ex("Те, кто нару'шил зако'н, отвеча'ют.", "Those who broke the law are held responsible.", "Те, кто"),
             ]),
    ],
    verify=(vf("менять", "меняет") + vf("меняться", "меняется") + vf("снизить", "снизят") + vf("снизиться", "снизится") + vf("снижаться", "снижается")
            + vf("увольнять", "увольняют") + vf("верить", "верим") + vf("нарушить", "нарушил") + vf("отвечать", "отвечают")),
    exercises=[
        F("Стоимость доставки может ___ на пять проце'нтов. (go down)", "сни'зиться", ["сни'зить", "снижа'ть", "сни'зила"], "No object: -ся.", "The cost of delivery may go down by five percent.", lemma="снизиться"),
        F("МЧС ___ фо'рму для сотру'дников. (is changing)", "меня'ет", ["меня'ется", "меня'ются", "меня'ть"], "Direct object фо'рму.", "The ministry is changing the uniform for staff.", lemma="менять"),
        F("Спрос на вино' ___. (is falling)", "снижа'ется", ["снижа'ет", "снижа'ют", "снижа'ть"], "No object.", "Demand for wine is falling.", lemma="снижаться"),
        F("Предприя'тия ___ бо'льше люде'й, чем нанима'ют. (fire)", "увольня'ют", ["увольня'ются", "увольня'ет", "увольня'ть"], "Direct object люде'й.", "Companies are firing more people than they are hiring.", lemma="увольнять"),
        F("Я ничего' не де'лаю: мне ___ де'лать. (nothing to)", "не'чего", ["ничего'", "не'кого", "не'кому"], "Positive infinitive: не'-.", "I'm doing nothing: I have nothing to do.", lemma=None),
        F("Он ни с ___ не говори'т. (anyone)", "кем", ["кого'", "ком", "кому'"], "С + instrumental.", "He doesn't talk to anyone.", lemma="кто"),
        F("Мы ве'рим ___, что они' сказа'ли. (what)", "тому'", ["то", "того'", "том"], "Ве'рить + dative.", "We believe what they said."),
        F("Из-за ___, что шёл дождь, мы не пошли' гуля'ть. (the fact)", "того'", ["то", "тому'", "том"], "Из-за + genitive.", "Because it was raining, we didn't go for a walk."),
        mc("Choose the correct sentence.", ["Нам не'куда идти'.", "Нам никуда' идти'.", "Мы не'куда не идём.", "Нам не'куда не идти'."], "Нам не'куда идти'.", "Dative + не'- + infinitive.", order=True),
        mc("‘Те, кто нару'шил зако'н’ — Те is:", ["plural", "singular masculine", "singular feminine", "neuter"], "plural", "Те = those.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 339
L339 = lesson(
    "Final review C: conditions and reported speech",
    "Е'сли бы я знал, я бы сказа'л. Я спроси'л, зна'ет ли она'.",
    requires=["если", "бы", "ли", "сказать", "спросить", "знать"],
    cards=[
        card("Map of the lesson",
             "Choose the pattern by the idea you want to express.",
             tables=[table(
                 ["Idea", "Pattern"],
                 [["possible condition", "Е'сли придёшь, позвони'."],
                  ["contrary to fact", "Е'сли бы знал, сказа'л бы."],
                  ["if it weren't for", "Е'сли бы не ты …"],
                  ["reported statement", "Он сказа'л, что …"],
                  ["reported question", "Он спроси'л, где … / придёт ли …"]])],
             examples=[
                 ex("Он спроси'л, зна'ет ли она'.", "He asked whether she knew.", "зна'ет ли она'"),
             ]),
    ],
    verify=(vf("сказать", "сказал") + vf("спросить", "спросил") + vf("знать", "знает") + vf("прийти", "придёшь") + vf("позвонить", "позвони")),
    exercises=[
        F("Е'сли ты ___ за'втра, мы пойдём в кино'. (come)", "придёшь", ["пришёл", "пришёл бы", "прихо'дишь"], "Real: future.", "If you come tomorrow, we'll go to the movies.", lemma="прийти"),
        F("Е'сли бы ты ___ вчера', мы пошли' бы в кино'. (had come)", "пришёл", ["придёшь", "прихо'дишь", "прийти'"], "Unreal: past + бы.", "If you had come yesterday, we would have gone to the movies.", lemma="прийти"),
        F("Е'сли бы не ___, я бы опозда'л. (you)", "ты", ["тебя'", "тебе'", "тобо'й"], "Nominative after не.", "If it weren't for you, I would have been late."),
        F("Он сказа'л, ___ придёт в пять. (that)", "что", ["ли", "е'сли", "бы"], "Reported statement.", "He said that he would come at five."),
        F("Он спроси'л, живу' ___ я в Москве'. (whether)", "ли", ["е'сли", "бы", "что"], "Yes/no question: ли.", "He asked whether I live in Moscow."),
        F("Он спроси'л, где я ___. (live)", "живу'", ["жил", "жить", "бу'ду жить"], "Same tense as the original question.", "He asked where I live.", lemma="жить"),
        F("Я бы ___ поговори'ть с дире'ктором. (would like, man)", "хоте'л", ["хоте'ла", "хочу'", "захоте'ть"], "Masculine past after бы.", "I would like to talk to the director.", lemma="хотеть"),
        mc("Which sentence is a reported yes/no question?", ["Он спроси'л, придёт ли она'.", "Он сказа'л, что она' придёт.", "Он знает, е'сли она' придёт.", "Он спроси'л, е'сли она' придёт."], "Он спроси'л, придёт ли она'.", "Ли.", order=True),
        mc("Which sentence is unreal?", ["Е'сли бы я знал, я бы сказа'л.", "Е'сли я узнаю', я скажу'.", "Когда' я узнаю', я скажу'.", "Я узнаю', придёт ли он."], "Е'сли бы я знал, я бы сказа'л.", "Бы in both parts.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 340
L340 = lesson(
    "Course finale: reading the news",
    "Мно'гие понима'ют новости на ру'сском. Вы тоже!",
    requires=["если", "ли", "бы", "правительство", "суд", "зарплата", "образование", "пожар"],
    cards=[
        card("You can read the news",
             "In this course you learned the grammar and vocabulary behind a typical news report: weather and disasters, crime and the courts, education and work. Here is one last mix.",
             tables=[table(
                 ["Topic", "Typical phrase"],
                 [["disaster", "Пожа'р потуши'ли за три часа'."],
                  ["crime", "Суд приговори'л его' к двум года'м."],
                  ["education", "Ско'лько выпускнико'в поступи'ло в университе'ты?"],
                  ["work", "Зарпла'та повы'силась на пять проце'нтов."],
                  ["conditions", "Е'сли бы не спаса'тели …"]])],
             examples=[
                 ex("Суд приговори'л его' к двум года'м.", "The court sentenced him to two years.", "приговори'л"),
             ]),
    ],
    verify=(vf("приговорить", "приговорил") + vf("потушить", "потушили") + vf("повыситься", "повысилась") + vf("поступить", "поступило")),
    exercises=[
        F("Спаса'тели ___ пожа'р за три часа'. (put out)", "потуши'ли", ["потуши'лись", "потуши'л", "потуши'ть"], "Plural subject; object пожа'р.", "The rescuers put out the fire in three hours.", lemma="потушить"),
        F("Суд приговори'л его' ___ двум года'м. (to)", "к", ["на", "в", "за"], "Приговори'ть к + dative.", "The court sentenced him to two years."),
        F("Зарпла'та ___ на пять проце'нтов. (rose)", "повы'силась", ["повы'сила", "повы'сили", "повы'сить"], "Feminine, no object: -ся.", "The salary rose by five percent.", lemma="повыситься"),
        F("Не'которые выпускники' ___ в университе'т. (got in)", "поступи'ли", ["поступа'ли", "поступи'ться", "поступа'ть"], "Result: perfective.", "Some graduates got into university.", lemma="поступить"),
        F("Е'сли ___ не спаса'тели, мы поги'бли бы. (it weren't for)", "бы", ["ли", "же", "бу'дет"], "Е'сли бы не + nominative.", "If it weren't for the rescuers, we would have died."),
        F("Он спроси'л, нашли' ___ свиде'теля. (whether)", "ли", ["е'сли", "бы", "что"], "Indirect yes/no question.", "He asked whether they had found the witness."),
        F("Нам не'куда ___ по'сле шко'лы. (to go)", "идти'", ["идём", "шли", "пошли'"], "Positive negative with infinitive.", "We have nowhere to go after school.", lemma="идти"),
        F("За после'дние дво'е су'ток ___ мно'го сне'га. (fell)", "вы'пало", ["вы'пал", "вы'пала", "вы'пали"], "Neuter: мно'го сне'га.", "A lot of snow fell over the last two days."),
        mc("Which sentence uses a verbal adverb?", ["Перее'хав в Москву', она' нашла' рабо'ту.", "Она' перее'хала в Москву'.", "Она' нашла' рабо'ту.", "Она' перее'хала и нашла' рабо'ту."], "Перее'хав в Москву', она' нашла' рабо'ту.", "Перее'хав = having moved.", order=True),
        mc("Which is a passive-like -ся sentence?", ["Рейс отменя'ется.", "Авиакомпа'ния отменя'ет рейс.", "Она' умыва'ется.", "Они' встреча'ются."], "Рейс отменя'ется.", "Рейс is the receiver.", order=True),
    ],
)

UNIT = unit("Unit 33: Conditions, reported speech and final review",
            [L328, L329, L330, L331, L332, L333, L334, L335, L336, L337, L338, L339, L340])
