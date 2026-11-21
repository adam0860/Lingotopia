"""Unit 21: prefixed verbs of motion II and driving (textbook module 5, lesson 28)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 193
L193 = lesson(
    "Walk in, walk by, walk across: prefix + motion verb",
    "Он ка'ждый день захо'дит в магази'н.",
    requires=["идти", "ехать", "ходить", "пройти", "зайти"],
    cards=[
        card("What a prefix does to aspect",
             "A plain verb of motion is always imperfective, with a multidirectional and a unidirectional form. Add a "
             "prefix and that pair disappears: the verb is now imperfective or perfective. A prefix on a "
             "multidirectional verb gives the imperfective, and a prefix on a unidirectional verb gives the "
             "perfective.",
             tables=[table(
                 ["Motion", "Imperfective (prefix + multi)", "Perfective (prefix + uni)"],
                 [["walk", "заходи'ть", "зайти'"],
                  ["walk", "подходи'ть", "подойти'"],
                  ["walk", "переходи'ть", "перейти'"],
                  ["walk", "проходи'ть", "пройти'"],
                  ["travel", "заезжа'ть", "зае'хать"],
                  ["travel", "подъезжа'ть", "подъе'хать"],
                  ["travel", "переезжа'ть", "перее'хать"],
                  ["travel", "проезжа'ть", "прое'хать"],
                  ["swim", "переплыва'ть", "переплы'ть"],
                  ["fly", "пролета'ть", "пролете'ть"],
                  ["run", "сбега'ть", "сбежа'ть"],
                  ["run", "подбега'ть", "подбежа'ть"]])],
             examples=[
                 ex("Он ка'ждый день захо'дит в магази'н.", "He stops in at the store every day.", "захо'дит"),
                 ex("Вчера' он зашёл в магази'н и купи'л хлеб.", "Yesterday he stopped in at the store and bought bread.", "зашёл"),
             ]),
        card("The stems change a little",
             "The prefix attaches to the stem, which is not always the same as the infinitive. Идти' becomes -йти' "
             "(зайти'), е'здить becomes -езжа'ть (заезжа'ть), пла'вать becomes -плыва'ть (переплыва'ть), and бе'гать "
             "becomes -бега'ть, with the stress shifting to the ending.",
             tables=[table(
                 ["Plain verb", "Stem with a prefix", "Example"],
                 [["идти'", "-йти'", "зайти', пройти'"],
                  ["е'здить", "-езжа'ть", "заезжа'ть, проезжа'ть"],
                  ["пла'вать", "-плыва'ть", "переплыва'ть"],
                  ["бе'гать", "-бега'ть", "сбега'ть, подбега'ть"]])],
             examples=[
                 ex("Мы ка'ждое у'тро прохо'дим ми'мо шко'лы.", "Every morning we walk past the school.", "прохо'дим"),
                 ex("Вдруг ми'мо нас прое'хал авто'бус.", "Suddenly a bus drove past us.", "прое'хал"),
             ]),
    ],
    verify=(vf("заходить", "заходит") + vf("зайти", "зашёл") + vf("проходить", "проходим") + vf("проехать", "проехал")
            + vf("переплыть", "переплыл") + vf("купить", "купил") + vf("хлеб", "хлеб")
            + vf("подойти", "подошёл") + vf("перейти", "перешёл")),
    exercises=[
        F("Ка'ждый день он ___ в магази'н. (stops in)", "захо'дит", ["зашёл", "зайдёт", "зайти'"], "Every day: imperfective заходи'ть.", "Every day he stops in at the store."),
        F("Он ___ в магази'н и купи'л хлеб. (stopped in)", "зашёл", ["заходи'л", "захо'дит", "зайти'"], "One completed action: perfective зашёл.", "He stopped in at the store and bought bread."),
        F("Ка'ждое у'тро мы ___ ми'мо шко'лы. (walk past)", "прохо'дим", ["прошли'", "пройдём", "пройти'"], "Repeated: imperfective проходи'ть.", "Every morning we walk past the school."),
        F("Вдруг ми'мо нас ___ авто'бус. (drove past)", "прое'хал", ["проезжа'л", "проезжа'ет", "прое'дет"], "Sudden single event: perfective прое'хал.", "Suddenly a bus drove past us."),
        F("Он ___ ре'ку за пять мину'т. (swam across it)", "переплы'л", ["переплыва'л", "переплыва'ет", "переплы'ть"], "Done once, in five minutes: perfective.", "He swam across the river in five minutes."),
        mc("Which of these is imperfective?", ["переходи'ть", "перейти'", "пройти'", "зайти'"], "переходи'ть", "Prefix + ходи'ть = imperfective.", order=True),
        mc("A prefix added to a unidirectional verb (идти', е'хать) makes the verb...", ["perfective", "imperfective", "multidirectional", "unidirectional"], "perfective", "Prefix + unidirectional = perfective."),
        mc("What is the perfective partner of проезжа'ть?", ["прое'хать", "проходи'ть", "пройти'", "проезжа'л"], "прое'хать", "-езжа'ть ↔ -е'хать."),
    ],
)

# ---------------------------------------------------------------------------- 194
L194 = lesson(
    "Come up to, move away from: под- and от-",
    "Же'нщина подошла' к окну'.",
    requires=["подойти", "уйти", "ехать", "окно", "дорога"],
    cards=[
        card("под- means “up to”",
             "Under the prefix под- the motion ends next to something: you come up to a person or a thing. The "
             "preposition is к with the dative. You can also leave out the thing and just say подойти'.",
             tables=[table(
                 ["Verb (perfective)", "Meaning", "Example"],
                 [["подойти'", "walk up to", "Же'нщина подошла' к окну'."],
                  ["подъе'хать", "drive up to", "Такси' подъе'хало к гости'нице."],
                  ["подбежа'ть", "run up to", "Де'вочка подбежа'ла к ма'ме."],
                  ["подплы'ть", "swim up to", "Ло'дка подплыла' к бе'регу."],
                  ["подлете'ть", "fly up to", "Пти'ца подлете'ла к окну'."]])],
             examples=[
                 ex("Же'нщина подошла' к окну' и откры'ла его'.", "The woman walked up to the window and opened it.", "подошла' к окну'"),
                 ex("Такси' подъе'хало к гости'нице.", "The taxi pulled up to the hotel.", "подъе'хало к гости'нице"),
                 ex("Де'вочка подбежа'ла к ма'ме.", "The girl ran up to her mother.", "подбежа'ла к ма'ме"),
             ]),
        card("от- means “away from”",
             "The prefix от- is the opposite: you move away from something. The preposition is от with the genitive. "
             "It also describes the departure of buses and trains (but not planes).",
             tables=[table(
                 ["Verb (perfective)", "Meaning", "Example"],
                 [["отойти'", "step away from", "Отойди' от доро'ги!"],
                  ["отъе'хать", "drive away from", "Маши'на отъе'хала от до'ма."],
                  ["отбежа'ть", "run away from", "Ма'льчик отбежа'л от ма'тери."],
                  ["отплы'ть", "swim away from", "Ло'дка отплыла' от бе'рега."],
                  ["отходи'ть", "(trains) depart", "Наш по'езд отхо'дит в де'вять."]])],
             examples=[
                 ex("Отойди' от доро'ги!", "Get away from the road!", "Отойди' от доро'ги"),
                 ex("Маши'на отъе'хала от до'ма.", "The car drove away from the house.", "отъе'хала от до'ма"),
                 ex("Наш по'езд отхо'дит в де'вять.", "Our train leaves at nine.", "отхо'дит"),
             ]),
    ],
    verify=(vf("подойти", "подошла", "подошёл") + vf("подъехать", "подъехало") + vf("подбежать", "подбежала")
            + vf("подплыть", "подплыла") + vf("подлететь", "подлетела") + vf("отойти", "отойди")
            + vf("отъехать", "отъехала") + vf("отбежать", "отбежал") + vf("отплыть", "отплыла")
            + vf("отходить", "отходит") + vf("открыть", "открыла") + vf("окно", "окну") + vf("дорога", "дороги")),
    exercises=[
        F("Же'нщина подошла' ___ окну'. (to)", "к", ["от", "из", "у"], "Под- + к + dative.", "The woman walked up to the window."),
        F("Отойди' ___ доро'ги! (away from)", "от", ["к", "в", "на"], "От- + от + genitive.", "Get away from the road!"),
        F("Такси' ___ к гости'нице. (pulled up)", "подъе'хало", ["отъе'хало", "прое'хало", "съе'хало"], "Под- = up to.", "The taxi pulled up to the hotel."),
        F("Маши'на ___ от до'ма. (drove away)", "отъе'хала", ["подъе'хала", "зае'хала", "дое'хала"], "От- = away from.", "The car drove away from the house."),
        F("Де'вочка ___ к ма'ме и обняла' её. (ran up)", "подбежа'ла", ["отбежа'ла", "сбежа'ла", "убежа'ла"], "Под- = up to.", "The girl ran up to her mother and hugged her."),
        F("По'езд ___ в де'вять часо'в. (leaves)", "отхо'дит", ["подхо'дит", "перехо'дит", "захо'дит"], "От- also describes departure.", "The train leaves at nine o'clock."),
        F("Ло'дка ___ к бе'регу. (swam up to)", "подплыла'", ["отплыла'", "переплыла'", "заплыла'"], "Под- + к.", "The boat came up to the shore."),
        mc("Which prefix means “up to, approaching”?", ["под-", "от-", "с-", "до-"], "под-", "под- = approach.", order=True),
        mc("Which preposition follows от-verbs such as отойти'?", ["от + genitive", "к + dative", "в + accusative", "с + instrumental"], "от + genitive", "Away from: от + genitive."),
    ],
)

# ---------------------------------------------------------------------------- 195
L195 = lesson(
    "Up the mountain, down the stairs: вз- and с-",
    "Тури'сты взошли' на верши'ну горы'.",
    requires=["гора", "лестница", "выйти", "лететь", "берег"],
    cards=[
        card("вз- (вс-): up",
             "The prefix вз- means motion up, onto something high, or off the ground. It is spelled вс- before "
             "voiceless consonants. The preposition is на or в with the accusative.",
             tables=[table(
                 ["Verb (perfective)", "Meaning", "Example"],
                 [["взойти'", "climb up, rise", "Тури'сты взошли' на верши'ну горы'."],
                  ["взбежа'ть", "run up", "Ма'льчик взбежа'л на второ'й эта'ж."],
                  ["взлете'ть", "take off", "Самолёт взлете'л в во'семь часо'в."],
                  ["взойти'", "(sun) come up", "Со'лнце уже' взошло'."]])],
             examples=[
                 ex("Тури'сты взошли' на верши'ну горы'.", "The tourists climbed to the top of the mountain.", "взошли' на верши'ну"),
                 ex("Самолёт взлете'л в во'семь часо'в.", "The plane took off at eight o'clock.", "взлете'л"),
                 ex("Со'лнце уже' взошло'.", "The sun has already risen.", "взошло'"),
             ]),
        card("с-: down, off",
             "The prefix с- is the opposite: motion down, or off something. The preposition is с with the genitive.",
             tables=[table(
                 ["Up (вз-)", "Down (с-)", "Example"],
                 [["взойти'", "сойти'", "Он сошёл с по'езда."],
                  ["взбежа'ть", "сбежа'ть", "Де'ти сбежа'ли с горы'."],
                  ["взлете'ть", "слете'ть", "Пти'ца слете'ла с ве'тки."],
                  ["взъе'хать", "съе'хать", "Мы съе'хали с шоссе'."]])],
             examples=[
                 ex("Де'ти сбежа'ли с горы'.", "The children ran down from the hill.", "сбежа'ли с горы'"),
                 ex("Пти'ца слете'ла с ве'тки.", "The bird flew off the branch.", "слете'ла с ве'тки"),
                 ex("Мы съе'хали с шоссе' и пое'хали в дере'вню.", "We turned off the highway and drove to the village.", "съе'хали с шоссе'"),
             ]),
    ],
    verify=(vf("взойти", "взошли", "взошло") + vf("взбежать", "взбежал") + vf("взлететь", "взлетел")
            + vf("сойти", "сошёл") + vf("сбежать", "сбежали") + vf("слететь", "слетела") + vf("съехать", "съехали")
            + vf("взъехать", "взъехать") + vf("гора", "горы") + vf("шоссе", "шоссе")),
    exercises=[
        F("Тури'сты ___ на верши'ну горы'. (climbed up)", "взошли'", ["сошли'", "дошли'", "вошли'"], "Вз- = up.", "The tourists climbed to the top of the mountain."),
        F("Де'ти ___ с горы'. (ran down)", "сбежа'ли", ["взбежа'ли", "подбежа'ли", "забежа'ли"], "С- = down.", "The children ran down from the hill."),
        F("Пти'ца ___ с ве'тки. (flew off)", "слете'ла", ["взлете'ла", "залете'ла", "пролете'ла"], "С- = off.", "The bird flew off the branch."),
        F("Самолёт ___ в во'семь часо'в. (took off)", "взлете'л", ["слете'л", "перелете'л", "залете'л"], "Вз- = up, off the ground.", "The plane took off at eight o'clock."),
        F("Мы ___ с шоссе' и пое'хали в дере'вню. (turned off)", "съе'хали", ["въе'хали", "подъе'хали", "отъе'хали"], "С- + с + genitive.", "We turned off the highway and drove to the village."),
        F("Со'лнце уже' ___. (has risen)", "взошло'", ["сошло'", "зашло'", "дошло'"], "Вз- = up.", "The sun has already risen."),
        F("Он ___ с по'езда на ста'нции. (got off)", "сошёл", ["взошёл", "дошёл", "перешёл"], "С- = off.", "He got off the train at the station."),
        mc("Which prefix means “down from, off”?", ["с-", "вз-", "под-", "до-"], "с-", "с- = down, off.", order=True),
        mc("What is the opposite of взбежа'ть?", ["сбежа'ть", "подбежа'ть", "забежа'ть", "добежа'ть"], "сбежа'ть", "Up ↔ down."),
    ],
)

# ---------------------------------------------------------------------------- 196
L196 = lesson(
    "Get as far as, get across: до- and пере-",
    "Мы дошли' до моста' за де'сять мину'т.",
    requires=["дойти", "перейти", "река", "мост", "улица"],
    cards=[
        card("до-: as far as",
             "The prefix до- means reaching a certain point. The preposition is до with the genitive. Often you add за "
             "and a time to say how long it took.",
             tables=[table(
                 ["Verb (perfective)", "Meaning", "Example"],
                 [["дойти'", "walk as far as", "Мы дошли' до моста' за де'сять мину'т."],
                  ["дое'хать", "drive as far as", "Она' дое'хала до вокза'ла за час."],
                  ["добежа'ть", "run as far as", "Ты добежи'шь до того' де'рева?"],
                  ["доплы'ть", "swim as far as", "Он доплы'л до острова'."],
                  ["долете'ть", "fly as far as", "Мы долете'ли до Москвы' за три часа'."]])],
             examples=[
                 ex("Мы дошли' до моста' за де'сять мину'т.", "We walked to the bridge in ten minutes.", "дошли' до моста'"),
                 ex("Она' дое'хала до вокза'ла за час.", "She got to the station in an hour.", "дое'хала до вокза'ла"),
             ]),
        card("пере-: across, over",
             "The prefix пере- means motion across or over something. The thing crossed is in the accusative, "
             "with or without че'рез.",
             tables=[table(
                 ["Verb (perfective)", "Meaning", "Example"],
                 [["перейти'", "cross on foot", "Пешехо'д перешёл (че'рез) доро'гу."],
                  ["перее'хать", "drive across", "Мы перее'хали мост."],
                  ["переплы'ть", "swim across", "Он переплы'л ре'ку."],
                  ["перелете'ть", "fly over", "Мяч перелете'л че'рез забо'р."]])],
             examples=[
                 ex("Пешехо'д перешёл доро'гу на зелёный свет.", "The pedestrian crossed the road on the green light.", "перешёл доро'гу"),
                 ex("Мы перее'хали мост и пое'хали да'льше.", "We drove across the bridge and drove on.", "перее'хали мост"),
                 ex("Мяч перелете'л че'рез забо'р.", "The ball flew over the fence.", "перелете'л че'рез забо'р"),
             ]),
    ],
    verify=(vf("дойти", "дошли") + vf("доехать", "доехала") + vf("добежать", "добежишь") + vf("доплыть", "доплыл")
            + vf("долететь", "долетели") + vf("перейти", "перешёл") + vf("переехать", "переехали")
            + vf("переплыть", "переплыл") + vf("перелететь", "перелетел") + vf("мост", "моста", "мост")
            + vf("вокзал", "вокзала") + vf("остров", "острова") + vf("забор", "забор")),
    exercises=[
        F("Мы ___ до моста' за де'сять мину'т. (walked as far as)", "дошли'", ["перешли'", "взошли'", "отошли'"], "До- = as far as.", "We walked to the bridge in ten minutes."),
        F("Она' ___ до вокза'ла за час. (drove as far as)", "дое'хала", ["перее'хала", "отъе'хала", "подъе'хала"], "До- = as far as.", "She got to the station in an hour."),
        F("Пешехо'д ___ доро'гу на зелёный свет. (crossed)", "перешёл", ["дошёл", "отошёл", "зашёл"], "Пере- = across.", "The pedestrian crossed the road on the green light."),
        F("Мы ___ мост и пое'хали да'льше. (drove across)", "перее'хали", ["дое'хали", "отъе'хали", "съе'хали"], "Пере- = across.", "We drove across the bridge and drove on."),
        F("Он ___ ре'ку на ло'дке. (crossed)", "переплы'л", ["доплы'л", "заплы'л", "отплы'л"], "Пере- = across.", "He crossed the river by boat."),
        F("Мяч ___ че'рез забо'р. (flew over)", "перелете'л", ["долете'л", "слете'л", "залете'л"], "Пере- = over.", "The ball flew over the fence."),
        F("Мы дошли' ___ па'рка. (as far as)", "до", ["к", "от", "из"], "До- + до + genitive.", "We walked as far as the park."),
        mc("Which prefix means “across, over”?", ["пере-", "до-", "от-", "вз-"], "пере-", "пере- = across.", order=True),
        mc("Which prefix means “reaching a point”?", ["до-", "пере-", "с-", "под-"], "до-", "до- + до."),
    ],
)

# ---------------------------------------------------------------------------- 197
L197 = lesson(
    "Walk past, miss the stop: про-",
    "Авто'бус прое'хал ми'мо остано'вки.",
    requires=["пройти", "мимо", "через", "остановка", "площадь"],
    cards=[
        card("про-: past or through",
             "The prefix про- covers three ideas: moving past something, moving through or across something, and "
             "covering a distance. Pass-by verbs take ми'мо with the genitive, and crossing verbs take че'рез with the "
             "accusative.",
             tables=[table(
                 ["Meaning", "Preposition", "Example"],
                 [["past", "ми'мо + genitive", "Она' пробежа'ла ми'мо меня'."],
                  ["through, across", "че'рез + accusative", "Мы прошли' че'рез парк."],
                  ["between", "ме'жду + instrumental", "Он прошёл ме'жду стола'ми."],
                  ["distance", "accusative", "За день мы прошли' два'дцать киломе'тров."]])],
             examples=[
                 ex("Она' пробежа'ла ми'мо меня' и не поздоро'валась.", "She ran past me and did not say hello.", "пробежа'ла ми'мо меня'"),
                 ex("Мы прошли' че'рез парк.", "We walked through the park.", "прошли' че'рез парк"),
                 ex("За день мы прошли' два'дцать киломе'тров.", "In one day we covered twenty kilometers.", "прошли' два'дцать киломе'тров"),
             ]),
        card("Missing your stop",
             "When you go past a place where you meant to stop, you also use про-: прое'хать, пройти'. The place is in the "
             "accusative, with no preposition.",
             examples=[
                 ex("Я заду'мался и прое'хал свою' остано'вку.", "I got lost in thought and missed my stop.", "прое'хал свою' остано'вку"),
                 ex("Авто'бус прое'хал ми'мо остано'вки.", "The bus drove past the stop.", "прое'хал ми'мо остано'вки"),
                 ex("Маши'ны прое'хали че'рез пло'щадь.", "The cars drove across the square.", "прое'хали че'рез пло'щадь"),
             ]),
    ],
    verify=(vf("проехать", "проехал", "проехали") + vf("пройти", "прошли", "прошёл") + vf("пробежать", "пробежала")
            + vf("поздороваться", "поздоровалась") + vf("задуматься", "задумался") + vf("остановка", "остановку", "остановки")
            + vf("площадь", "площадь") + vf("парк", "парк") + vf("стол", "столами") + vf("километр", "километров")),
    exercises=[
        F("Авто'бус ___ ми'мо остано'вки. (drove past)", "прое'хал", ["подъе'хал", "отъе'хал", "дое'хал"], "Про- = past.", "The bus drove past the stop."),
        F("Мы ___ через парк. (walked through)", "прошли'", ["подошли'", "взошли'", "сошли'"], "Про- = through.", "We walked through the park."),
        F("Я заду'мался и ___ свою' остано'вку. (missed)", "прое'хал", ["дое'хал", "перее'хал", "отъе'хал"], "Про- = go past a stop.", "I got lost in thought and missed my stop."),
        F("За день мы ___ два'дцать киломе'тров. (covered)", "прошли'", ["дошли'", "подошли'", "перешли'"], "Про- + distance in the accusative.", "In one day we covered twenty kilometers."),
        F("Она' ___ ми'мо меня' и не поздоро'валась. (ran past)", "пробежа'ла", ["добежа'ла", "сбежа'ла", "подбежа'ла"], "Про- = past.", "She ran past me and did not say hello."),
        F("Мы прошли' ми'мо ___. (the school)", "шко'лы", ["шко'ле", "шко'лу", "шко'лой"], "Ми'мо + genitive.", "We walked past the school.", lemma="школа"),
        F("Маши'ны прое'хали ___ пло'щадь. (across)", "че'рез", ["ми'мо", "до", "от"], "Че'рез + accusative.", "The cars drove across the square."),
        mc("Which preposition goes with про- when you pass by something?", ["ми'мо + genitive", "к + dative", "от + genitive", "до + genitive"], "ми'мо + genitive", "Ми'мо = past."),
        mc("«Я прое'хал свою' остано'вку» means...", ["I missed my stop", "I reached my stop", "I got off at my stop", "I left my stop"], "I missed my stop", "Про- = went past it."),
    ],
)

# ---------------------------------------------------------------------------- 198
L198 = lesson(
    "Drop in, go behind, go around: за- and о(б)-",
    "По доро'ге домо'й я зайду' в апте'ку.",
    requires=["зайти", "вокруг", "магазин", "лес", "дерево"],
    cards=[
        card("за-: behind, in, by",
             "The prefix за- has several uses. All of them are about moving off the main path for a moment.",
             tables=[table(
                 ["Meaning", "Preposition", "Example"],
                 [["go behind", "за + accusative", "Соба'ка забежа'ла за дом."],
                  ["go in", "в, на + accusative", "Зайди' в дом, на у'лице хо'лодно."],
                  ["stop by someone's place", "к + dative", "Я зайду' к тебе' по'сле рабо'ты."],
                  ["stop on the way", "в, на + accusative", "По доро'ге домо'й я зайду' в апте'ку."],
                  ["go too far", "далеко'", "Он зашёл сли'шком далеко' в лес."]])],
             examples=[
                 ex("Соба'ка забежа'ла за дом.", "The dog ran behind the house.", "забежа'ла за дом"),
                 ex("Я зайду' к тебе' по'сле рабо'ты.", "I will drop in on you after work.", "зайду' к тебе'"),
                 ex("По доро'ге домо'й я зайду' в апте'ку.", "On the way home I will stop at the pharmacy.", "зайду' в апте'ку"),
             ]),
        card("о- / об-: around",
             "The prefix о- (об- before a vowel) means motion around something. It takes вокру'г with the genitive, or "
             "just the accusative. It also means going around an obstacle, and covering a whole area.",
             tables=[table(
                 ["Meaning", "Example"],
                 [["around", "Мы обошли' вокру'г о'зера."],
                  ["around an obstacle", "Води'тель объе'хал я'му."],
                  ["all over a place", "Мы обошли' весь го'род."]])],
             examples=[
                 ex("Мы обошли' вокру'г о'зера.", "We walked around the lake.", "обошли' вокру'г о'зера"),
                 ex("Води'тель объе'хал я'му.", "The driver drove around the pothole.", "объе'хал я'му"),
                 ex("Мы обошли' весь го'род.", "We walked all over the city.", "обошли' весь го'род"),
             ]),
    ],
    verify=(vf("зайти", "зайду", "зашёл") + vf("забежать", "забежала") + vf("обойти", "обошли")
            + vf("объехать", "объехал") + vf("собака", "собака") + vf("аптека", "аптеку") + vf("озеро", "озера")
            + vf("яма", "яму") + vf("город", "город") + vf("лес", "лес")),
    exercises=[
        F("По доро'ге домо'й я ___ в апте'ку. (will stop in)", "зайду'", ["отойду'", "сойду'", "взойду'"], "За- = stop in on the way.", "On the way home I will stop at the pharmacy."),
        F("Соба'ка ___ за дом. (ran behind)", "забежа'ла", ["добежа'ла", "сбежа'ла", "отбежа'ла"], "За- = behind.", "The dog ran behind the house."),
        F("Мы ___ вокру'г о'зера. (walked around)", "обошли'", ["дошли'", "перешли'", "взошли'"], "О(б)- = around.", "We walked around the lake."),
        F("Води'тель ___ я'му. (drove around)", "объе'хал", ["зае'хал", "отъе'хал", "съе'хал"], "Об- = around an obstacle.", "The driver drove around the pothole."),
        F("Он ___ сли'шком далеко' в лес. (went)", "зашёл", ["взошёл", "сошёл", "перешёл"], "За- = too far in.", "He went too far into the forest."),
        F("Я ___ к тебе' по'сле рабо'ты. (will drop in)", "зайду'", ["обойду'", "взойду'", "доплыву'"], "За- + к + dative.", "I will drop in on you after work."),
        F("Мы ___ весь го'род. (walked all over)", "обошли'", ["сошли'", "зашли'", "ушли'"], "Об- = all over.", "We walked all over the city."),
        mc("Which prefix means “around”?", ["о- / об-", "за-", "до-", "пере-"], "о- / об-", "о(б)- = around.", order=True),
        mc("«Я зайду' к тебе'» means...", ["I will drop in on you", "I will walk past you", "I will go away from you", "I will cross to you"], "I will drop in on you", "За- + к = visit briefly."),
    ],
)

# ---------------------------------------------------------------------------- 199
L199 = lesson(
    "Gather and disperse; walk around a while: с-…ся, раз-…ся, по-, за-",
    "Все ро'дственники съе'хались на пра'здник.",
    requires=["разойтись", "собраться", "ехать", "ходить", "дом"],
    cards=[
        card("Coming together, going apart",
             "With the particle -ся, the prefix с- means “gather from many places to one” and раз- (разъ- before "
             "я, е, ю, ё) means “scatter from one place to many”. The gathering place takes в, на or к, and the "
             "dispersal takes по with the dative.",
             tables=[table(
                 ["Gather (с-…ся)", "Disperse (раз-…ся)", "Example"],
                 [["съе'хаться", "разъе'хаться", "Госте'й съе'халось мно'го."],
                  ["сойти'сь", "разойти'сь", "По'сле конце'рта все разошли'сь по дома'м."],
                  ["сбежа'ться", "разбежа'ться", "Де'ти разбежа'лись по двору'."]])],
             examples=[
                 ex("На юбиле'й съе'хались все ро'дственники.", "All the relatives came together for the anniversary.", "съе'хались"),
                 ex("По'сле конце'рта все разошли'сь по дома'м.", "After the concert everyone went home.", "разошли'сь по дома'м"),
             ]),
        card("A prefix that does not show direction",
             "Sometimes a prefix with a multidirectional verb only tells you about time or about a round trip. "
             "По- means “for a while”, за- means “to begin”, and с- means “go there and come back”.",
             tables=[table(
                 ["Prefix + verb", "Meaning", "Example"],
                 [["по- + бе'гать", "run around for a while", "Ребёнок побе'гал и усну'л."],
                  ["за- + ходи'ть", "begin to pace", "Он встал и заходи'л по ко'мнате."],
                  ["с- + ходи'ть", "go there and back", "Я схожу' в магази'н и бы'стро верну'сь."],
                  ["с- + е'здить", "go there and back by vehicle", "Съе'зди, пожа'луйста, в апте'ку."]])],
             examples=[
                 ex("Ребёнок побе'гал и усну'л.", "The child ran around for a while and fell asleep.", "побе'гал"),
                 ex("Я схожу' в магази'н и бы'стро верну'сь.", "I will pop out to the store and be right back.", "схожу'"),
             ]),
    ],
    verify=(vf("съехаться", "съехались", "съехалось") + vf("разойтись", "разошлись") + vf("разбежаться", "разбежались")
            + vf("побегать", "побегал") + vf("заходить", "заходил") + vf("сходить", "схожу") + vf("уснуть", "уснул") + vf("вернуться", "вернусь")
            + vf("съездить", "съезди") + vf("юбилей", "юбилей") + vf("родственник", "ро'дственники")),
    exercises=[
        F("Все ро'дственники ___ на пра'здник. (gathered)", "съе'хались", ["разъе'хались", "подъе'хали", "отъе'хали"], "С-…ся = gather.", "All the relatives came together for the holiday."),
        F("По'сле лекции студе'нты ___ по дома'м. (dispersed)", "разошли'сь", ["сошли'сь", "дошли'сь", "зашли'сь"], "Раз-…ся = disperse.", "After the lecture the students went home."),
        F("Я ___ в магази'н и бы'стро верну'сь. (will go there and back)", "схожу'", ["перейду'", "дойду'", "отойду'"], "С- + multidirectional = round trip.", "I will pop out to the store and be right back."),
        F("Ребёнок ___ по ко'мнате и успоко'ился. (ran around a while)", "побе'гал", ["забе'гал", "сбе'гал", "отбе'гал"], "По- = for a while.", "The child ran around the room for a while and calmed down."),
        F("Он встал и ___ по ко'мнате. (began to pace)", "заходи'л", ["походи'л", "сходи'л", "дошёл"], "За- = begin.", "He got up and began to pace around the room."),
        F("Де'ти ___ по двору'. (scattered)", "разбежа'лись", ["сбежа'лись", "добежа'лись", "перебежа'лись"], "Раз-…ся = scatter.", "The children scattered over the yard."),
        mc("What does съе'хаться mean?", ["to gather from many places", "to scatter", "to drive across", "to drive away"], "to gather from many places", "С-…ся = gather."),
        mc("What does the prefix по- add to бе'гать?", ["for a while", "to begin", "there and back", "across"], "for a while", "Побе'гать = run around a while."),
    ],
)

# ---------------------------------------------------------------------------- 200
L200 = lesson(
    "Move house, pass an exam, time flies: figurative prefixes",
    "Мы перее'хали в друго'й го'род.",
    requires=["перейти", "переходить", "проходить", "дойти", "уйти"],
    cards=[
        card("The same prefixes, new meanings",
             "Once you know what each prefix does, many figurative uses are easy to guess. Here are the most common "
             "ones.",
             tables=[table(
                 ["Verb", "Meaning", "Example"],
                 [["перее'хать", "move to a new home", "Мы перее'хали в друго'й го'род."],
                  ["перейти'", "switch to something else", "Я перешёл на другу'ю рабо'ту."],
                  ["пройти'", "pass (an exam)", "Он прошёл экза'мен."],
                  ["проходи'ть", "take place", "Конце'рт прохо'дит в суббо'ту."],
                  ["пролете'ть", "(time) fly by", "Ле'то пролете'ло бы'стро."],
                  ["подходи'ть", "suit, fit", "Э'то пла'тье тебе' подхо'дит."],
                  ["подойти' к", "approach (a problem)", "Он подошёл к вопро'су серьёзно."]])],
             examples=[
                 ex("Мы перее'хали в друго'й го'род.", "We moved to another city.", "перее'хали"),
                 ex("Ле'то пролете'ло бы'стро.", "The summer flew by.", "пролете'ло"),
                 ex("Э'то пла'тье тебе' подхо'дит.", "This dress suits you.", "подхо'дит"),
             ]),
        card("More expressions",
             "Some verbs of motion have become set phrases. Learn them whole.",
             tables=[table(
                 ["Verb", "Meaning", "Example"],
                 [["отойти' от", "move away from (a topic, a habit)", "Он давно' отошёл от спо'рта."],
                  ["разойти'сь", "break up; (opinions) differ", "Мы с ним разошли'сь."],
                  ["сойти' с ума'", "go crazy", "Я схожу' с ума' от э'того шу'ма."],
                  ["сбежа'ть", "run away", "Соба'ка сбежа'ла из до'ма."]])],
             examples=[
                 ex("Он давно' отошёл от спо'рта.", "He gave up sports long ago.", "отошёл от спо'рта"),
                 ex("Я схожу' с ума' от э'того шу'ма.", "This noise is driving me crazy.", "схожу' с ума'"),
                 ex("Соба'ка сбежа'ла из до'ма.", "The dog ran away from home.", "сбежа'ла"),
             ]),
    ],
    verify=(vf("переехать", "переехали") + vf("перейти", "перешёл") + vf("пройти", "прошёл") + vf("проходить", "проходит")
            + vf("пролететь", "пролетело") + vf("подходить", "подходит") + vf("подойти", "подошёл") + vf("отойти", "отошёл")
            + vf("разойтись", "разошлись") + vf("сходить", "схожу") + vf("сбежать", "сбежала") + vf("экзамен", "экзамен")
            + vf("шум", "шума") + vf("спорт", "спорта") + vf("лето", "лето") + vf("платье", "платье")),
    exercises=[
        F("Мы ___ в друго'й го'род. (moved)", "перее'хали", ["отъе'хали", "съе'хали", "подъе'хали"], "Пере- = change of home.", "We moved to another city."),
        F("Ле'то ___ о'чень бы'стро. (flew by)", "пролете'ло", ["взлете'ло", "слете'ло", "перелете'ло"], "Про- = time passes.", "The summer flew by very quickly."),
        F("Э'то пла'тье тебе' ___. (suits)", "подхо'дит", ["отхо'дит", "прохо'дит", "захо'дит"], "Подходи'ть = suit.", "This dress suits you."),
        F("Он ___ экза'мен и о'чень рад. (passed)", "прошёл", ["перешёл", "дошёл", "зашёл"], "Пройти' экза'мен.", "He passed the exam and is very glad."),
        F("Конце'рт ___ в суббо'ту. (takes place)", "прохо'дит", ["подхо'дит", "отхо'дит", "захо'дит"], "Проходи'ть = take place.", "The concert takes place on Saturday."),
        F("Соба'ка ___ из до'ма. (ran away)", "сбежа'ла", ["взбежа'ла", "подбежа'ла", "пробежа'ла"], "Сбежа'ть = run away.", "The dog ran away from home."),
        F("Я ___ с ума' от э'того шу'ма! (am going crazy)", "схожу'", ["подхожу'", "отхожу'", "прохожу'"], "Сойти' с ума'.", "This noise is driving me crazy!"),
        mc("What does «Он отошёл от спо'рта» mean?", ["He gave up sports", "He walked to the stadium", "He crossed the stadium", "He won at sports"], "He gave up sports", "Отойти' от = move away from."),
        mc("What does «Мы с ним разошли'сь» mean?", ["We broke up", "We met", "We went together", "We crossed paths"], "We broke up", "Раз-…ся = part."),
    ],
)

# ---------------------------------------------------------------------------- 201
L201 = lesson(
    "At the wheel: cars, roads and rentals",
    "Я получи'л права' и купи'л маши'ну в автосало'не.",
    requires=["машина", "дорога", "шоссе", "поездка", "руль"],
    cards=[
        card("Cars and places",
             "Here are the nouns you need to talk about cars and roads.",
             tables=[table(
                 ["Russian", "English"],
                 [["легково'й автомоби'ль", "passenger car, sedan"],
                  ["внедоро'жник", "off-road vehicle"],
                  ["кроссо'вер", "SUV"],
                  ["автосало'н", "car dealership"],
                  ["автомастерска'я", "car repair shop"],
                  ["автозапра'вка, АЗС", "gas station"],
                  ["бензи'н", "gasoline"],
                  ["права'", "driver's license"],
                  ["страхо'вка", "insurance"],
                  ["аре'нда, прока'т", "rental"]])],
             examples=[
                 ex("Я получи'л права' и купи'л маши'ну в автосало'не.", "I got my driver's license and bought a car at a dealership.", "права'"),
                 ex("Мы взя'ли маши'ну напрока'т на неде'лю.", "We rented a car for a week.", "напрока'т"),
             ]),
        card("On the road",
             "These words describe the road itself.",
             tables=[table(
                 ["Russian", "English"],
                 [["руль", "steering wheel"],
                  ["светофо'р", "traffic light"],
                  ["перекрёсток", "intersection"],
                  ["шоссе' (indeclinable)", "highway"],
                  ["про'бка", "traffic jam"],
                  ["час пик", "rush hour"],
                  ["движе'ние", "traffic, movement"],
                  ["пое'здка", "trip"]])],
             examples=[
                 ex("На светофо'ре гори'т кра'сный свет.", "The light is red at the traffic light.", "светофо'ре"),
                 ex("В час пик на шоссе' всегда' про'бки.", "At rush hour there are always traffic jams on the highway.", "про'бки"),
             ]),
        card("Verbs for drivers",
             "Most of these come in aspect pairs. They are listed imperfective / perfective.",
             tables=[table(
                 ["Russian", "English"],
                 [["води'ть маши'ну", "to drive a car"],
                  ["сади'ться / сесть за руль", "to get behind the wheel"],
                  ["заправля'ться / запра'виться", "to get gas"],
                  ["лома'ться / слома'ться", "to break down"],
                  ["повора'чивать / поверну'ть", "to turn"],
                  ["остана'вливаться / останови'ться", "to stop"],
                  ["проверя'ть / прове'рить", "to check"],
                  ["ремонти'ровать / отремонти'ровать", "to repair"],
                  ["опа'здывать / опозда'ть", "to be late"]])],
             examples=[
                 ex("Моя' маши'на слома'лась, и я позвони'л в автомастерску'ю.", "My car broke down and I called a repair shop.", "слома'лась"),
                 ex("Нам ну'жно запра'виться: в ба'ке нет бензи'на.", "We need to get gas: there is none in the tank.", "запра'виться"),
             ]),
    ],
    verify=(vf("руль", "руль") + vf("бензин", "бензина") + vf("страховка", "страховка") + vf("сломаться", "сломалась")
            + vf("позвонить", "позвонил") + vf("светофор", "светофоре") + vf("пробка", "пробки") + vf("шоссе", "шоссе")
            + vf("сесть", "сесть") + vf("садиться", "садиться") + vf("останавливаться", "останавливаться")
            + vf("проверять", "проверять") + vf("опаздывать", "опаздывать")),
    exercises=[
        F("Я получи'л ___ и купи'л маши'ну. (driver's license)", "права'", ["про'бку", "бензи'н", "светофо'р"], "Права' = driver's license.", "I got my driver's license and bought a car."),
        F("В час пик на шоссе' всегда' ___. (traffic jams)", "про'бки", ["права'", "перекрёстки", "руль"], "Про'бка = traffic jam.", "At rush hour there are always traffic jams on the highway."),
        F("Нам ну'жно запра'виться: в ба'ке нет ___. (gasoline)", "бензи'на", ["бензи'ну", "бензи'ном", "бензи'н"], "Нет + genitive.", "We need to get gas: there is none in the tank.", lemma="бензин"),
        F("Мы взя'ли маши'ну ___. (to rent)", "напрока'т", ["перекрёсток", "светофо'р", "страхо'вка"], "Взять напрока'т.", "We rented a car."),
        F("На ___ гори'т кра'сный свет. (traffic light)", "светофо'ре", ["руле'", "страхо'вке", "права'х"], "Светофо'р = traffic light.", "The light is red at the traffic light.", lemma="светофор"),
        F("Моя' маши'на ___. (broke down)", "слома'лась", ["заправи'лась", "опозда'ла", "ремонти'ровала"], "Слома'ться = break down.", "My car broke down."),
        F("Я сел за ___ и пое'хал. (the wheel)", "руль", ["права'", "светофо'р", "бензи'н"], "Сесть за руль.", "I got behind the wheel and drove off."),
        mc("What does шоссе' mean?", ["highway", "intersection", "traffic jam", "gas station"], "highway", "Шоссе' = highway."),
        mc("Where do you get gas?", ["на автозапра'вке", "в автосало'не", "на перекрёстке", "на светофо'ре"], "на автозапра'вке", "Автозапра'вка = gas station."),
    ],
)

# ---------------------------------------------------------------------------- 202
L202 = lesson(
    "A crash on the highway: accidents and traffic rules",
    "На шоссе' произошла' ава'рия.",
    requires=["авария", "скорость", "правило", "полиция", "случиться"],
    cards=[
        card("Accidents",
             "Here is the vocabulary for talking about a traffic accident and its consequences.",
             tables=[table(
                 ["Russian", "English"],
                 [["ава'рия", "accident, crash"],
                  ["ДТП (доро'жно-тра'нспортное происше'ствие)", "traffic accident"],
                  ["несча'стный слу'чай", "accident"],
                  ["столкнове'ние", "collision"],
                  ["лобово'е столкнове'ние", "head-on collision"],
                  ["пешехо'д", "pedestrian"],
                  ["пешехо'дный перехо'д", "pedestrian crossing"],
                  ["тра'вма", "injury"],
                  ["ско'рая по'мощь", "ambulance"]])],
             examples=[
                 ex("На шоссе' произошла' ава'рия.", "An accident happened on the highway.", "произошла' ава'рия"),
                 ex("Ско'рая по'мощь прие'хала че'рез пять мину'т.", "The ambulance arrived in five minutes.", "Ско'рая по'мощь"),
                 ex("Два пешехо'да получи'ли тра'вмы.", "Two pedestrians were injured.", "получи'ли тра'вмы"),
             ]),
        card("Rules and violations",
             "These words describe what drivers do wrong, and what happens next.",
             tables=[table(
                 ["Russian", "English"],
                 [["пра'вила доро'жного движе'ния (ПДД)", "traffic rules"],
                  ["наруше'ние", "violation"],
                  ["ско'рость", "speed"],
                  ["полоса'", "lane"],
                  ["встре'чная полоса'", "oncoming traffic lane"],
                  ["взя'тка", "bribe"],
                  ["вреза'ться / вре'заться (в + acc.)", "to crash into"],
                  ["случа'ться / случи'ться", "to happen"],
                  ["спра'виться (с + instr.)", "to cope with"]])],
             examples=[
                 ex("Води'тель не спра'вился с управле'нием и вре'зался в забо'р.", "The driver lost control and crashed into a fence.", "не спра'вился с управле'нием"),
                 ex("Он нару'шил пра'вила доро'жного движе'ния.", "He broke the traffic rules.", "нару'шил пра'вила"),
                 ex("Води'тель вы'ехал на встре'чную полосу'.", "The driver pulled into the oncoming lane.", "встре'чную полосу'"),
             ]),
    ],
    verify=(vf("авария", "авария") + vf("пешеход", "пешехода") + vf("травма", "травмы") + vf("забор", "забор")
            + vf("справиться", "справился") + vf("врезаться", "врезался") + vf("нарушить", "нарушил")
            + vf("выехать", "выехал") + vf("полоса", "полосу") + vf("правило", "правила") + vf("скорость", "скорость")
            + vf("получить", "получили") + vf("произойти", "произошла") + vf("приехать", "приехала")),
    exercises=[
        F("На шоссе' произошла' ___. (accident)", "ава'рия", ["ава'рию", "ава'рии", "ава'рией"], "Nominative: произошла' ава'рия.", "An accident happened on the highway."),
        F("Води'тель не спра'вился с ___. (control)", "управле'нием", ["управле'ние", "управле'нию", "управле'нии"], "Спра'виться с + instrumental.", "The driver lost control."),
        F("Маши'на вре'залась в ___. (fence)", "забо'р", ["забо'ра", "забо'ре", "забо'ром"], "Вре'заться в + accusative.", "The car crashed into a fence."),
        F("Пешехо'ды перехо'дят доро'гу по ___ перехо'ду. (pedestrian)", "пешехо'дному", ["пешехо'дный", "пешехо'дного", "пешехо'дным"], "По + dative.", "Pedestrians cross the road at the pedestrian crossing."),
        F("Два пешехо'да получи'ли ___. (injuries)", "тра'вмы", ["тра'вмам", "тра'вмами", "тра'вме"], "Plural: тра'вмы.", "Two pedestrians were injured."),
        F("Води'тель вы'ехал на ___ полосу'. (oncoming)", "встре'чную", ["встре'чная", "встре'чной", "встре'чное"], "Accusative feminine.", "The driver pulled into the oncoming lane."),
        F("Он превы'сил ___. (the speed limit)", "ско'рость", ["ско'рости", "ско'ростью", "ско'ростей"], "Accusative: ско'рость.", "He exceeded the speed."),
        mc("What does ДТП stand for?", ["traffic accident", "driver's license", "traffic light", "car rental"], "traffic accident", "Доро'жно-тра'нспортное происше'ствие."),
        mc("What case follows спра'виться с?", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "Спра'виться с + instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 203
L203 = lesson(
    "Review: prefixed motion verbs and driving",
    "Мы прошли' ми'мо ава'рии и дошли' до остано'вки.",
    requires=["идти", "пройти", "дорога", "авария", "машина"],
    cards=[
        card("Prefix meanings at a glance",
             "Choose the prefix for the direction of the motion, then the preposition that goes with it.",
             tables=[table(
                 ["Prefix", "Meaning", "Preposition"],
                 [["под-", "up to", "к + dative"],
                  ["от-", "away from", "от + genitive"],
                  ["вз-", "up, onto", "на, в + accusative"],
                  ["с-", "down, off", "с + genitive"],
                  ["до-", "as far as", "до + genitive"],
                  ["пере-", "across", "через, accusative"],
                  ["про-", "past, through", "ми'мо, че'рез"],
                  ["за-", "behind, in, drop by", "за, в, к"],
                  ["о(б)-", "around", "вокру'г"],
                  ["с-…ся / раз-…ся", "gather / disperse", "на, к / по"]])],
             examples=[
                 ex("Мы прошли' ми'мо ава'рии и дошли' до остано'вки.", "We walked past the accident and got to the stop.", "прошли' ми'мо ава'рии"),
             ]),
    ],
    verify=(vf("пройти", "прошли") + vf("дойти", "дошли") + vf("авария", "аварии") + vf("остановка", "остановки")
            + vf("подъехать", "подъехала") + vf("перейти", "перешёл") + vf("слететь", "слетела")),
    exercises=[
        F("Мы прошли' ми'мо ___. (the accident)", "ава'рии", ["ава'рия", "ава'рию", "ава'рией"], "Ми'мо + genitive.", "We walked past the accident.", lemma="авария"),
        F("Такси' ___ к вокза'лу. (pulled up)", "подъе'хало", ["отъе'хало", "перее'хало", "съе'хало"], "Под- + к.", "The taxi pulled up to the station."),
        F("Пешехо'д ___ доро'гу на зелёный свет. (crossed)", "перешёл", ["подошёл", "отошёл", "взошёл"], "Пере- + accusative.", "The pedestrian crossed the road on the green light."),
        F("Мы ___ до остано'вки за пять мину'т. (got to)", "дошли'", ["перешли'", "сошли'", "взошли'"], "До- + до.", "We got to the stop in five minutes."),
        F("Пти'ца ___ с ве'тки. (flew off)", "слете'ла", ["взлете'ла", "залете'ла", "долете'ла"], "С- = off.", "The bird flew off the branch."),
        F("Я схожу' в магази'н и ___. (come back)", "верну'сь", ["вернётся", "возвраща'юсь", "верну'ться"], "Return: верну'сь.", "I will go to the store and come back."),
        F("Гости ___ на пра'здник со всей страны'. (gathered)", "съе'хались", ["разъе'хались", "отъе'хали", "объе'хали"], "С-…ся = gather.", "Guests gathered for the holiday from all over the country."),
        F("Води'тель не спра'вился с ___. (control)", "управле'нием", ["управле'ние", "управле'нию", "управле'нии"], "Спра'виться с + instrumental.", "The driver lost control."),
        F("В час пик на шоссе' мно'го ___. (traffic jams)", "про'бок", ["про'бки", "про'бка", "про'бкам"], "Мно'го + genitive plural: про'бок.", "There are many traffic jams on the highway at rush hour."),
        F("Он давно' ___ от спо'рта. (gave up)", "отошёл", ["подошёл", "дошёл", "перешёл"], "Отойти' от = move away from.", "He gave up sports a long time ago."),
        mc("Which verb means “drive across”?", ["перее'хать", "подъе'хать", "отъе'хать", "дое'хать"], "перее'хать", "Пере- = across."),
    ],
)

UNIT = unit("Unit 21: Prefixed verbs of motion and driving",
            [L193, L194, L195, L196, L197, L198, L199, L200, L201, L202, L203])
