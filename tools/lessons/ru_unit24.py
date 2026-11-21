"""Unit 24: verbs of carrying, leading and driving; самый as "very"; the particle же
(textbook module 6, lesson 32)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 225
L225 = lesson(
    "Carry, lead, drive: носи'ть / нести', води'ть / вести', вози'ть / везти'",
    "Ма'ма ведёт ребёнка в шко'лу, а па'па везёт су'мки.",
    requires=["нести", "носить", "вести", "водить", "везти"],
    cards=[
        card("Three more pairs of motion verbs",
             "You already know pairs such as ходи'ть / идти' (on foot) and е'здить / е'хать (by vehicle). Russian has "
             "three more pairs for moving something or someone along with you. Each pair has a habitual or "
             "round-trip verb and a one-way verb, just like ходи'ть / идти'. The big difference: these verbs always "
             "take a direct object, because you carry, lead or drive somebody or something.",
             tables=[table(
                 ["Habitual", "One way, now", "Meaning"],
                 [["носи'ть", "нести'", "carry; wear (in your hands or on you)"],
                  ["води'ть", "вести'", "lead, take (a person or animal walking)"],
                  ["вози'ть", "везти'", "transport, take (by vehicle)"]])],
             examples=[
                 ex("Он несёт су'мку.", "He is carrying a bag.", "несёт"),
                 ex("Ма'ма ведёт ребёнка в шко'лу.", "Mom is taking the child to school.", "ведёт"),
                 ex("Па'па везёт ребёнка в шко'лу на маши'не.", "Dad is driving the child to school.", "везёт"),
             ]),
        card("The present tense of носи'ть, нести'",
             "Носи'ть is a regular second-conjugation verb with a consonant change in the я-form (с → ш). Нести' is "
             "first conjugation and has the stress on the ending in я and они, and on ё in the other forms.",
             tables=[table(
                 ["", "носи'ть", "нести'"],
                 [["я", "но'шу", "несу'"],
                  ["ты", "но'сишь", "несёшь"],
                  ["он / она'", "но'сит", "несёт"],
                  ["мы", "но'сим", "несём"],
                  ["вы", "но'сите", "несёте"],
                  ["они'", "но'сят", "несу'т"]])],
             examples=[
                 ex("Я ка'ждый день но'шу с собо'й кни'гу.", "I carry a book with me every day.", "но'шу"),
                 ex("Куда' ты несёшь э'ти я'щики?", "Where are you taking these boxes?", "несёшь"),
             ]),
        card("The present tense of води'ть, вести', вози'ть, везти'",
             "Води'ть and вози'ть change д → ж and з → ж in the я-form (вожу' for both!). Вести' and везти' are first "
             "conjugation and look like нести'.",
             tables=[
                 table(["", "води'ть", "вести'"],
                       [["я", "вожу'", "веду'"],
                        ["ты", "во'дишь", "ведёшь"],
                        ["он / она'", "во'дит", "ведёт"],
                        ["мы", "во'дим", "ведём"],
                        ["вы", "во'дите", "ведёте"],
                        ["они'", "во'дят", "веду'т"]]),
                 table(["", "вози'ть", "везти'"],
                       [["я", "вожу'", "везу'"],
                        ["ты", "во'зишь", "везёшь"],
                        ["он / она'", "во'зит", "везёт"],
                        ["мы", "во'зим", "везём"],
                        ["вы", "во'зите", "везёте"],
                        ["они'", "во'зят", "везу'т"]]),
             ],
             examples=[
                 ex("Я вожу' сы'на в шко'лу.", "I take my son to school.", "вожу'"),
                 ex("Они' веду'т соба'ку на прогу'лку.", "They are taking the dog for a walk.", "веду'т"),
             ]),
        card("Walking or driving?",
             "Води'ть / вести' mean taking someone along on foot, so the object must be able to walk by itself: a "
             "child, a dog, a guest. You cannot ‘lead’ a table. Носи'ть / нести' and вози'ть / везти' work with any "
             "object, living or not.",
             examples=[
                 ex("Ли'да ведёт соба'ку.", "Lida is walking the dog.", "ведёт соба'ку"),
                 ex("Грузови'к везёт фру'кты.", "A truck is transporting fruit.", "везёт фру'кты"),
             ]),
    ],
    verify=(vf("носить", "ношу", "носишь", "носит", "носим", "носите", "носят")
            + vf("нести", "несу", "несёшь", "несёт", "несём", "несёте", "несут")
            + vf("водить", "вожу", "водишь", "водит", "водим", "водите", "водят")
            + vf("вести", "веду", "ведёшь", "ведёт", "ведём", "ведёте", "ведут")
            + vf("возить", "вожу", "возишь", "возит", "возим", "возите", "возят")
            + vf("везти", "везу", "везёшь", "везёт", "везём", "везёте", "везут")
            + vf("собака", "собаку") + vf("ребёнок", "ребёнка") + vf("сумка", "сумки")),
    exercises=[
        F("Ка'ждый день ма'ма ___ ребёнка в шко'лу пешко'м. (leads)", "во'дит", ["ведёт", "но'сит", "во'зит"], "Every day, on foot, a child: води'ть.", "Every day Mom walks the child to school.", lemma="водить"),
        F("Ка'ждое у'тро па'па ___ ребёнка в шко'лу на маши'не. (drives)", "во'зит", ["во'дит", "но'сит", "везёт"], "Every morning, by car: вози'ть.", "Every morning Dad drives the child to school.", lemma="возить"),
        F("Она' всегда' ___ в су'мке кни'гу. (carries)", "но'сит", ["несёт", "во'дит", "во'зит"], "A habit: носи'ть.", "She always carries a book in her bag.", lemma="носить"),
        F("Сейча'с я ___ су'мку домо'й. (am carrying)", "несу'", ["но'шу", "веду'", "везу'"], "Now, one way, in my hands: нести'.", "I am carrying the bag home now.", lemma="нести"),
        F("Вы ка'ждую суббо'ту ___ дете'й в парк? (take)", "во'дите", ["ведёте", "во'зите", "но'сите"], "Every Saturday: habitual. On foot: води'ть.", "Do you take the children to the park every Saturday?", lemma="водить"),
        F("Смотри', Ли'да ___ соба'ку. (is walking)", "ведёт", ["во'дит", "несёт", "во'зит"], "Right now: вести'.", "Look, Lida is walking the dog.", lemma="вести"),
        F("Грузови'к ___ фру'кты в магази'н. (is driving)", "везёт", ["во'зит", "ведёт", "несёт"], "A truck, one way, now: везти'.", "The truck is taking fruit to the shop.", lemma="везти"),
        mc("Which verb means to transport something by vehicle, as a habit?", ["вози'ть", "води'ть", "носи'ть", "нести'"], "вози'ть", "Вози'ть = habitual driving.", order=True),
        mc("What do all of these verbs need?", ["a direct object", "only a preposition", "an instrumental noun", "nothing at all"], "a direct object", "You carry, lead or drive somebody or something."),
    ],
)

# ---------------------------------------------------------------------------- 226
L226 = lesson(
    "Every day or right now: past and future of carrying and leading",
    "Когда' мы встре'тили сосе'да, он вёл соба'ку.",
    requires=["нести", "носить", "вести", "везти", "водить"],
    cards=[
        card("Habit, round trip, or on the way",
             "The rules are the same as for ходи'ть / идти'. The habitual verb covers a habit and a round trip. The "
             "one-way verb covers a movement in progress, a single trip in one direction.",
             tables=[table(
                 ["Verb", "Use", "Example"],
                 [["носи'ть", "habit; wearing; there and back", "Я ча'сто но'шу кни'ги."],
                  ["нести'", "on the way now", "Я несу' кни'ги домо'й."],
                  ["вози'ть", "habit; there and back", "Он вози'л дете'й на да'чу."],
                  ["везти'", "on the way now", "Он вёз дете'й на да'чу."]])],
             examples=[
                 ex("Вчера' я носи'л су'мку в ремо'нт, и она' уже' до'ма.", "Yesterday I took the bag to be repaired, and it is already back.", "носи'л"),
                 ex("Когда' мы встре'тили сосе'да, он вёл соба'ку.", "When we met our neighbor, he was walking his dog.", "вёл"),
             ]),
        card("Past tense of the one-way verbs",
             "The masculine past of нести' and везти' has no -л: нёс, вёз. Вести' keeps it: вёл. The feminine, neuter "
             "and plural forms are regular, with the stress on the ending: несла', вела', везли'.",
             tables=[table(
                 ["", "нести'", "вести'", "везти'"],
                 [["он", "нёс", "вёл", "вёз"],
                  ["она'", "несла'", "вела'", "везла'"],
                  ["оно'", "несло'", "вело'", "везло'"],
                  ["они'", "несли'", "вели'", "везли'"]])],
             examples=[
                 ex("Она' несла' тяжёлую су'мку.", "She was carrying a heavy bag.", "несла'"),
                 ex("Они' вели' дете'й за ру'ку.", "They were leading the children by the hand.", "вели'"),
             ]),
        card("Past tense of the habitual verbs",
             "Носи'ть, води'ть and вози'ть form the past tense like any regular verb: -л, -ла, -ло, -ли. In the "
             "past they often mean a round trip: ‘took there and came back’.",
             tables=[table(
                 ["", "носи'ть", "води'ть", "вози'ть"],
                 [["он", "носи'л", "води'л", "вози'л"],
                  ["она'", "носи'ла", "води'ла", "вози'ла"],
                  ["они'", "носи'ли", "води'ли", "вози'ли"]])],
             examples=[
                 ex("Ле'том па'па вози'л нас на мо'ре.", "In summer Dad used to take us to the sea.", "вози'л"),
                 ex("Ба'бушка води'ла меня' в теа'тр.", "Grandma used to take me to the theater.", "води'ла"),
             ]),
    ],
    verify=(vf("нести", "нёс", "несла", "несло", "несли") + vf("вести", "вёл", "вела", "вело", "вели")
            + vf("везти", "вёз", "везла", "везло", "везли") + vf("носить", "носил", "носила", "носили")
            + vf("водить", "водил", "водила", "водили") + vf("возить", "возил", "возила", "возили")
            + vf("собака", "собаку") + vf("сумка", "сумку")),
    exercises=[
        F("Она' ___ тяжёлую су'мку. (was carrying)", "несла'", ["нёс", "несло'", "несли'"], "Feminine past of нести': несла'.", "She was carrying a heavy bag.", lemma="нести"),
        F("Он ___ соба'ку по у'лице. (was leading)", "вёл", ["вела'", "вёз", "нёс"], "Masculine past of вести': вёл.", "He was leading the dog down the street.", lemma="вести"),
        F("Грузови'к ___ фру'кты. (was driving)", "вёз", ["вёл", "нёс", "вози'л"], "Masculine past of везти': вёз.", "The truck was transporting fruit.", lemma="везти"),
        F("Они' ___ дете'й за ру'ку. (were leading)", "вели'", ["вела'", "вёл", "води'ли"], "Plural: вели'.", "They were leading the children by the hand.", lemma="вести"),
        F("Ле'том па'па ___ нас на мо'ре. (used to drive)", "вози'л", ["вёз", "нёс", "носи'л"], "A repeated trip each summer: вози'л.", "In summer Dad used to take us to the sea.", lemma="возить"),
        F("Ба'бушка ча'сто ___ меня' в теа'тр. (used to take)", "води'ла", ["вела'", "везла'", "носи'ла"], "Repeated, on foot: води'ла.", "Grandma often took me to the theater.", lemma="водить"),
        F("Вчера' я ___ су'мку в ремо'нт, и она' уже' до'ма. (took there and back)", "носи'л", ["нёс", "несла'", "вёз"], "A completed round trip: носи'л.", "Yesterday I took the bag in for repair and it is already home.", lemma="носить"),
        mc("What is the feminine past of нести'?", ["несла'", "нёсла", "несет", "несена'"], "несла'", "Feminine past: несла'.", order=False),
        mc("In the past, ‘He was driving the children to the dacha (at that moment)’ is:", ["Он вёз дете'й на да'чу.", "Он вози'л дете'й на да'чу.", "Он вёл дете'й на да'чу.", "Он нёс дете'й на да'чу."], "Он вёз дете'й на да'чу.", "A trip in progress, by vehicle: вёз."),
    ],
)

# ---------------------------------------------------------------------------- 227
L227 = lesson(
    "Set off, or for a while: понести', повезти', поводи'ть",
    "Ко'ля сейча'с повёз бра'та на вокза'л.",
    requires=["нести", "вести", "везти", "водить", "машина"],
    cards=[
        card("Unprefixed verbs are all imperfective",
             "Like ходи'ть and идти', every one of these verbs is imperfective. If you need a perfective verb "
             "without a precise direction, add по-.",
             tables=[table(
                 ["Habitual", "→ for a while", "One way", "→ set off"],
                 [["носи'ть", "поноси'ть", "нести'", "понести'"],
                  ["води'ть", "поводи'ть", "вести'", "повести'"],
                  ["вози'ть", "повози'ть", "везти'", "повезти'"]])],
             examples=[
                 ex("Я немно'го поноси'л э'ту ша'пку и снял её.", "I wore this hat for a little while and took it off.", "поноси'л"),
             ]),
        card("По- + habitual verb: for a little while",
             "The perfective of носи'ть, води'ть, вози'ть means doing the action for a short time, usually going "
             "around with someone.",
             examples=[
                 ex("Он поводи'л госте'й по го'роду и показа'л им па'мятники.", "He took the guests around town for a while and showed them the monuments.", "поводи'л"),
                 ex("Па'па повози'л нас по го'роду.", "Dad drove us around the city for a while.", "повози'л"),
             ]),
        card("По- + one-way verb: set off",
             "The perfective of нести', вести', везти' stresses the start of the movement: ‘picked up and set off’. "
             "The past masculine is понёс, повёл, повёз. The future is formed with the personal endings: понесу', "
             "поведу', повезу'.",
             tables=[table(
                 ["", "понести'", "повезти'"],
                 [["я", "понесу'", "повезу'"],
                  ["он (past)", "понёс", "повёз"],
                  ["она' (past)", "понесла'", "повезла'"]])],
             examples=[
                 ex("Ко'ли сейча'с нет до'ма. Он повёз бра'та на вокза'л.", "Kolya is not home now. He has taken his brother to the station.", "повёз"),
                 ex("Я понесу' су'мку.", "I will carry the bag.", "понесу'"),
                 ex("Де'вочка взяла' зо'нтик и понесла' его' ба'бушке.", "The girl took the umbrella and set off to bring it to her grandmother.", "понесла'"),
             ]),
    ],
    verify=(vf("поносить", "поносил") + vf("поводить", "поводил") + vf("повозить", "повозил")
            + vf("понести", "понесу", "понёс", "понесла") + vf("повезти", "повезу", "повёз", "повезла")
            + vf("повести", "поведу", "повёл") + vf("брат", "брата") + vf("вокзал", "вокзал") + vf("девочка", "девочка")),
    exercises=[
        F("Он ___ гостей по городу и показал им памятники. (took around for a while)", "поводи'л", ["повёл", "вёл", "нёс"], "A short round: поводи'ть.", "He took the guests around town for a while.", lemma="поводить"),
        F("Ко'ли нет до'ма. Он ___ бра'та на вокза'л. (has set off with)", "повёз", ["поводи'л", "повози'л", "вёз"], "A start of a trip by vehicle: повёз.", "Kolya has taken his brother to the station.", lemma="повезти"),
        F("Я ___ су'мку, а ты откро'й дверь. (will carry)", "понесу'", ["поношу'", "несу'", "поведу'"], "Perfective future of нести': понесу'.", "I will carry the bag; you open the door.", lemma="понести"),
        F("Па'па ___ нас по го'роду. (drove around for a while)", "повози'л", ["повёз", "вёз", "понёс"], "A short drive around: повози'ть.", "Dad drove us around town for a while.", lemma="повозить"),
        F("Де'вочка взяла' зо'нтик и ___ его' ба'бушке. (set off carrying)", "понесла'", ["понёс", "поноси'ла", "вела'"], "Feminine past: понесла'.", "The girl took the umbrella and set off to bring it to Grandma."),
        mc("Which prefix makes a perfective verb here?", ["по-", "в-", "вы-", "при-"], "по-", "По- gives a perfective with no direction.", order=True),
        mc("‘For a little while’ goes with:", ["the habitual verb + по-", "the one-way verb + по-", "any verb + вы-", "none of them"], "the habitual verb + по-", "Поводи'ть, повози'ть, поноси'ть."),
        mc("‘Set off carrying’ goes with:", ["the one-way verb + по-", "the habitual verb + по-", "any verb + при-", "none of them"], "the one-way verb + по-", "Понести', повести', повезти'."),
    ],
)

# ---------------------------------------------------------------------------- 228
L228 = lesson(
    "Behave, drive a car, wear glasses: set expressions",
    "Де'ти хорошо' себя' веду'т.",
    requires=["вести", "ответственность", "поведение", "дневник", "очки"],
    cards=[
        card("Вести' себя': to behave",
             "Вести' себя' means to behave. It takes an adverb: хорошо', пло'хо, споко'йно.",
             tables=[table(
                 ["Phrase", "English"],
                 [["вести' себя' хорошо'", "to behave well"],
                  ["вести' себя' пло'хо", "to behave badly"],
                  ["вести' себя' споко'йно", "to behave calmly"]])],
             examples=[
                 ex("Де'ти хорошо' себя' веду'т.", "The children are behaving well.", "себя' веду'т"),
                 ex("Почему' ты так пло'хо себя' ведёшь?", "Why are you behaving so badly?", "себя' ведёшь"),
                 ex("Вчера' она' вела' себя' споко'йно.", "Yesterday she behaved calmly.", "вела' себя'"),
             ]),
        card("Other fixed expressions",
             "These verbs appear in many fixed phrases. Learn each one as a unit.",
             tables=[table(
                 ["Phrase", "English"],
                 [["води'ть маши'ну", "to drive a car"],
                  ["носи'ть очки'", "to wear glasses"],
                  ["носи'ть кольцо'", "to wear a ring"],
                  ["вести' дневни'к", "to keep a diary"],
                  ["вести' разгово'р", "to have a conversation"],
                  ["нести' отве'тственность за + acc.", "to be responsible for"],
                  ["нести' цветы'", "to bring flowers"]])],
             examples=[
                 ex("Она' хорошо' во'дит маши'ну.", "She drives well.", "во'дит маши'ну"),
                 ex("Мой де'душка но'сит очки'.", "My grandfather wears glasses.", "но'сит очки'"),
                 ex("Я веду' дневни'к уже' пять лет.", "I have been keeping a diary for five years.", "веду' дневни'к"),
                 ex("Роди'тели несу'т отве'тственность за дете'й.", "Parents are responsible for their children.", "несу'т отве'тственность"),
             ]),
        card("Note: no ‘drive’ verb for the passenger",
             "Води'ть маши'ну is what the driver does. For a passenger the verb is е'хать (or е'здить): Я е'ду на "
             "маши'не. Do not say вожу' when you are only a passenger.",
             examples=[
                 ex("Я не вожу' маши'ну, я е'зжу на авто'бусе.", "I don't drive; I go by bus.", "не вожу' маши'ну"),
             ]),
    ],
    verify=(vf("вести", "ведут", "ведёшь", "вела") + vf("водить", "водит") + vf("носить", "носит")
            + vf("нести", "несут") + vf("дневник", "дневник") + vf("очки", "очки") + vf("машина", "машину")
            + vf("ответственность", "ответственность") + vf("разговор", "разговор") + vf("цветок", "цветы")
            + vf("кольцо", "кольцо") + vf("дедушка", "дедушка") + vf("ехать", "ехать") + vf("ездить", "езжу")
            + vf("автобус", "автобусе")),
    exercises=[
        F("Де'ти хорошо' себя' ___. (behave)", "веду'т", ["во'дят", "несу'т", "ведёт"], "Plural, now: веду'т.", "The children are behaving well.", lemma="вести"),
        F("Почему' ты так пло'хо себя' ___? (behave)", "ведёшь", ["во'дишь", "несёшь", "ведёт"], "Ты: ведёшь.", "Why are you behaving so badly?", lemma="вести"),
        F("Она' хорошо' ___ маши'ну. (drives)", "во'дит", ["ведёт", "везёт", "но'сит"], "To drive a car: води'ть маши'ну.", "She drives well.", lemma="водить"),
        F("Мой де'душка ___ очки'. (wears)", "но'сит", ["несёт", "ведёт", "во'зит"], "To wear glasses: носи'ть очки'.", "My grandfather wears glasses.", lemma="носить"),
        F("Я ___ дневни'к уже' пять лет. (keep)", "веду'", ["во'жу", "несу'", "но'шу"], "Вести' дневни'к.", "I have been keeping a diary for five years.", lemma="вести"),
        F("Роди'тели ___ отве'тственность за дете'й. (bear)", "несу'т", ["веду'т", "но'сят", "во'дят"], "Нести' отве'тственность.", "Parents are responsible for their children.", lemma="нести"),
        F("Я не вожу' маши'ну, я ___ на авто'бусе. (ride)", "е'зжу", ["вожу'", "иду'", "несу'"], "A passenger rides: е'здить.", "I don't drive; I ride the bus.", lemma="ездить"),
        mc("How do you say ‘to behave well’?", ["вести' себя' хорошо'", "носи'ть себя' хорошо'", "води'ть себя' хорошо'", "везти' себя' хорошо'"], "вести' себя' хорошо'", "Вести' себя'.", order=True),
        mc("What does ‘носи'ть очки'’ mean?", ["to wear glasses", "to carry a box", "to drive a car", "to lead a dog"], "to wear glasses", "Носи'ть also means to wear."),
    ],
)

# ---------------------------------------------------------------------------- 229
L229 = lesson(
    "Bags, suitcases, keys: what we carry",
    "Он несёт два пакета и тяжёлый чемода'н.",
    requires=["сумка", "пакет", "чемодан", "ключ", "очки"],
    cards=[
        card("Things we carry",
             "A short vocabulary of everyday objects that go with нести' and носи'ть.",
             tables=[table(
                 ["Word", "English"],
                 [["су'мка", "bag, handbag"],
                  ["паке'т", "plastic bag; package"],
                  ["чемода'н", "suitcase"],
                  ["рюкза'к", "backpack"],
                  ["коро'бка", "box"],
                  ["ключ (gen. ключа')", "key"],
                  ["очки' (pl.)", "glasses"],
                  ["зонт", "umbrella"],
                  ["коля'ска", "stroller"]])],
             examples=[
                 ex("Он несёт два паке'та и тяжёлый чемода'н.", "He is carrying two bags and a heavy suitcase.", "два паке'та"),
                 ex("Я всегда' но'шу ключи' в карма'не.", "I always keep my keys in my pocket.", "ключи'"),
             ]),
        card("Heavy, light, full",
             "To describe what you carry, use these adjectives.",
             tables=[table(
                 ["Word", "English"],
                 [["тяжёлый", "heavy"],
                  ["лёгкий", "light"],
                  ["по'лный", "full"],
                  ["пусто'й", "empty"],
                  ["большо'й", "big"],
                  ["ма'ленький", "small"]])],
             examples=[
                 ex("У меня' лёгкий рюкза'к.", "I have a light backpack.", "лёгкий"),
                 ex("Э'та коро'бка о'чень тяжёлая.", "This box is very heavy.", "тяжёлая"),
             ]),
        card("Counting what you carry",
             "After 2, 3, 4 use the genitive singular: два чемода'на, три су'мки. After 5 and more, use the genitive "
             "plural: пять паке'тов.",
             tables=[table(
                 ["Number", "Example"],
                 [["1", "оди'н чемода'н"],
                  ["2–4", "две су'мки, три паке'та"],
                  ["5+", "пять чемода'нов, шесть су'мок"]])],
             examples=[
                 ex("Она' несёт три су'мки.", "She is carrying three bags.", "три су'мки"),
                 ex("У нас пять чемода'нов.", "We have five suitcases.", "пять чемода'нов"),
             ]),
    ],
    verify=(vf("сумка", "сумка", "сумки") + vf("пакет", "пакета", "пакеты", "пакетов") + vf("чемодан", "чемодан", "чемодана", "чемоданов")
            + vf("ключ", "ключи") + vf("очки", "очки") + vf("рюкзак", "рюкзак") + vf("коробка", "коробка")
            + vf("зонт", "зонт") + vf("тяжёлый", "тяжёлый", "тяжёлая") + vf("лёгкий", "лёгкий")
            + vf("пустой", "пустой") + vf("полный", "полный") + vf("маленький", "маленький")
            + vf("большой", "большой") + vf("нести", "несёт") + vf("носить", "ношу") + vf("карман", "кармане")),
    exercises=[
        F("Он несёт два ___ и тяжёлый чемода'н. (bags)", "паке'та", ["паке'т", "паке'тов", "паке'ту"], "After 2: genitive singular.", "He is carrying two bags and a heavy suitcase.", lemma="пакет"),
        F("Она' несёт три ___. (bags)", "су'мки", ["су'мка", "су'мок", "су'мку"], "After 3: genitive singular.", "She is carrying three bags.", lemma="сумка"),
        F("У нас пять ___. (suitcases)", "чемода'нов", ["чемода'на", "чемода'ны", "чемода'ну"], "After 5: genitive plural.", "We have five suitcases.", lemma="чемодан"),
        F("Я всегда' но'шу ___ в карма'не. (keys)", "ключи'", ["ключа'", "ключу'", "ключе'й"], "Accusative plural of an inanimate noun = nominative.", "I always keep my keys in my pocket.", lemma="ключ"),
        F("Э'та коро'бка о'чень ___. (heavy)", "тяжёлая", ["тяжёлый", "тяжёлое", "тяжёлые"], "Коро'бка is feminine.", "This box is very heavy.", lemma="тяжёлый"),
        F("У меня' ___ рюкза'к. (light)", "лёгкий", ["лёгкая", "лёгкое", "лёгкие"], "Рюкза'к is masculine.", "I have a light backpack.", lemma="лёгкий"),
        mc("Which word means ‘suitcase’?", ["чемода'н", "рюкза'к", "коро'бка", "зонт"], "чемода'н", "Чемода'н = suitcase.", order=True),
        mc("Which phrase is correct?", ["четы'ре коро'бки", "четы'ре коро'бка", "четы'ре коро'бок", "четы'ре коро'бке"], "четы'ре коро'бки", "After 2–4: genitive singular."),
    ],
)

# ---------------------------------------------------------------------------- 230
L230 = lesson(
    "Games and winning: игра', вы'играть, проигра'ть, ве'сти в счёте",
    "На'ша кома'нда вы'играла матч со счётом два—оди'н.",
    requires=["игра", "выиграть", "проиграть", "команда", "матч"],
    cards=[
        card("Playing, winning and losing",
             "Игра' is a game. The verb for taking part is игра'ть. The result of a game is expressed by two perfective "
             "verbs: вы'играть (to win) and проигра'ть (to lose). Both take a direct object: вы'играть матч, "
             "проигра'ть игру'.",
             tables=[table(
                 ["Word", "English"],
                 [["игра'", "game"],
                  ["игра'ть", "to play"],
                  ["вы'играть", "to win"],
                  ["проигра'ть", "to lose"],
                  ["кома'нда", "team"],
                  ["матч", "match"],
                  ["сопе'рник", "opponent, rival"],
                  ["боле'льщик", "fan"],
                  ["чемпио'н", "champion"],
                  ["турни'р", "tournament"],
                  ["счёт", "score"]])],
             examples=[
                 ex("Мы вы'играли матч.", "We won the match.", "вы'играли"),
                 ex("Наш сопе'рник проигра'л.", "Our rival lost.", "проигра'л"),
                 ex("Кто вы'играл?", "Who won?", "вы'играл"),
             ]),
        card("The score: со счётом",
             "To say the score of a game, use со счётом + the numbers. A dash or двоеточие is read as ‘to’: два оди'н "
             "means 2:1.",
             examples=[
                 ex("На'ша кома'нда вы'играла матч со счётом три—оди'н.", "Our team won the match 3–1.", "со счётом три—оди'н"),
                 ex("Како'й счёт?", "What is the score?", "счёт"),
             ]),
        card("Вести' в счёте: to lead",
             "Вести' also means to be ahead in a game. The usual phrase is вести' в счёте.",
             examples=[
                 ex("На'ши веду'т в счёте.", "Our side is leading.", "веду'т в счёте"),
                 ex("Они' вели' в счёте до са'мого конца'.", "They were ahead until the very end.", "вели' в счёте"),
             ]),
        card("Online games",
             "Players and teams can be anywhere; these words are the same for a video game.",
             tables=[table(
                 ["Word", "English"],
                 [["игро'к", "player"],
                  ["экра'н", "screen"],
                  ["у'ровень (m.)", "level"],
                  ["побе'да", "victory"],
                  ["пораже'ние", "defeat"]])],
             examples=[
                 ex("Он игра'ет с дру'гом онла'йн.", "He plays online with a friend.", "игра'ет"),
                 ex("Э'то была' на'ша пе'рвая побе'да.", "That was our first victory.", "побе'да"),
             ]),
    ],
    verify=(vf("игра", "игра", "игру") + vf("играть", "играет") + vf("выиграть", "выиграли", "выиграл", "выиграла")
            + vf("проиграть", "проиграл") + vf("команда", "команда") + vf("матч", "матч")
            + vf("соперник", "соперник") + vf("болельщик", "болельщик") + vf("чемпион", "чемпион")
            + vf("турнир", "турнир") + vf("счёт", "счёт", "счётом") + vf("игрок", "игрок") + vf("экран", "экран")
            + vf("уровень", "уровень") + vf("победа", "победа") + vf("поражение", "поражение")
            + vf("вести", "ведут", "вели")),
    exercises=[
        F("Мы ___ матч. (won)", "вы'играли", ["проигра'ли", "вы'игрывали", "игра'ли"], "Perfective, a single result: вы'играли.", "We won the match.", lemma="выиграть"),
        F("Наш сопе'рник ___. (lost)", "проигра'л", ["вы'играл", "игра'л", "проигра'ть"], "Проигра'л = lost.", "Our rival lost.", lemma="проиграть"),
        F("На'ша кома'нда вы'играла матч ___ счётом три—оди'н. (with)", "со", ["с", "на", "по"], "Со счётом, because счёт begins with a consonant cluster.", "Our team won the match 3–1."),
        F("На'ши ___ в счёте. (are leading)", "веду'т", ["во'дят", "несу'т", "вы'играют"], "Вести' в счёте.", "Our side is leading.", lemma="вести"),
        F("Како'й ___? (score)", "счёт", ["счёта", "счёту", "счёте"], "Nominative, after како'й: Како'й счёт?", "What is the score?", lemma="счёт"),
        F("Э'то была' на'ша пе'рвая ___. (victory)", "побе'да", ["побе'ды", "побе'ду", "побе'де"], "Nominative feminine.", "That was our first victory.", lemma="победа"),
        F("Кто ___? (won)", "вы'играл", ["игра'ет", "проигра'ть", "вы'играть"], "Past, masculine: вы'играл.", "Who won?", lemma="выиграть"),
        mc("Which verb means ‘to lose a game’?", ["проигра'ть", "вы'играть", "игра'ть", "вести'"], "проигра'ть", "Проигра'ть = to lose.", order=True),
        mc("What is a боле'льщик?", ["a fan", "a player", "a referee", "a team"], "a fan", "Боле'льщик = fan."),
    ],
)

# ---------------------------------------------------------------------------- 231
L231 = lesson(
    "Right at the start, in the very center: са'мый as ‘very’",
    "С са'мого утра' идёт дождь.",
    requires=["самый", "начало", "конец", "центр", "берег"],
    cards=[
        card("Two jobs of са'мый",
             "You know са'мый from the superlative: са'мый большо'й го'род = the biggest city. Russian also uses са'мый "
             "to point to the exact extreme of a place or a time. English says ‘very’ or ‘right’: in the very center, "
             "right at the start.",
             examples=[
                 ex("Э'то са'мая интере'сная кни'га.", "This is the most interesting book.", "са'мая интере'сная"),
                 ex("Фонта'н стои'т в са'мом це'нтре пло'щади.", "The fountain stands in the very center of the square.", "в са'мом це'нтре"),
             ]),
        card("Fixed phrases",
             "In this meaning са'мый agrees with the noun in case, number and gender. The noun is usually "
             "a place or a point in time.",
             tables=[table(
                 ["Phrase", "English"],
                 [["с са'мого нача'ла", "right from the start"],
                  ["с са'мого утра'", "since early morning"],
                  ["до са'мого конца'", "right to the end"],
                  ["в са'мом це'нтре", "in the very center"],
                  ["на са'мом берегу'", "right on the shore"],
                  ["на са'мом краю'", "right on the edge"],
                  ["у са'мого мо'ря", "right by the sea"]])],
             examples=[
                 ex("Мы бы'ли там с са'мого нача'ла.", "We were there from the very beginning.", "с са'мого нача'ла"),
                 ex("Дом стои'т на са'мом берегу' реки'.", "The house stands right on the riverbank.", "на са'мом берегу'"),
                 ex("Мы дошли' до са'мого конца' у'лицы.", "We walked right to the end of the street.", "до са'мого конца'"),
             ]),
        card("The endings",
             "Са'мый is a regular hard adjective, so you already know its endings.",
             tables=[table(
                 ["Case", "Masc. / neut.", "Fem."],
                 [["Genitive", "са'мого", "са'мой"],
                  ["Dative", "са'мому", "са'мой"],
                  ["Instrumental", "са'мым", "са'мой"],
                  ["Prepositional", "са'мом", "са'мой"]])],
             examples=[
                 ex("У са'мой две'ри стои'т ма'ленький стол.", "A little table stands right by the door.", "У са'мой две'ри"),
             ]),
    ],
    verify=(vf("самый", "самый", "самая", "самым", "самые", "самых") + vf("начало", "начала", "начале")
            + vf("конец", "конца") + vf("центр", "центре") + vf("берег", "берегу") + vf("край", "краю")
            + vf("утро", "утра") + vf("море", "моря") + vf("площадь", "площади") + vf("улица", "улицы")
            + vf("река", "реки") + vf("дверь", "двери")),
    exercises=[
        F("Ресторан стои'т на ___ берегу' реки'. (right on)", "са'мом", ["са'мый", "са'мого", "са'мым"], "На + prepositional: са'мом.", "The restaurant is right on the riverbank."),
        F("Мы дошли' до ___ конца' у'лицы. (right to)", "са'мого", ["са'мом", "са'мой", "са'мый"], "До + genitive: са'мого.", "We walked right to the end of the street."),
        F("С ___ утра' идёт дождь. (since early)", "са'мого", ["са'мый", "са'мом", "са'мому"], "С + genitive: са'мого.", "It has been raining since early morning."),
        F("Фонта'н стои'т в ___ це'нтре пло'щади. (in the very)", "са'мом", ["са'мого", "са'мый", "са'мым"], "В + prepositional: са'мом.", "The fountain is in the very center of the square."),
        F("Магази'н нахо'дится в ___ конце' коридо'ра. (at the very)", "са'мом", ["са'мого", "са'мый", "са'мой"], "Prepositional: са'мом.", "The shop is at the very end of the corridor."),
        F("У ___ две'ри стои'т ма'ленький стол. (right by)", "са'мой", ["са'мого", "са'мая", "са'мую"], "У + genitive feminine: са'мой.", "A little table stands right by the door."),
        mc("Which sentence uses са'мый as ‘the very’ (not a superlative)?", ["Мы жи'ли на са'мом берегу' мо'ря.", "Э'то са'мый большо'й дом.", "Она' са'мая у'мная.", "Э'то са'мое интере'сное ме'сто."], "Мы жи'ли на са'мом берегу' мо'ря.", "Right on the shore: са'мом берегу'."),
        mc("‘Right from the start’ is:", ["с са'мого нача'ла", "в са'мом нача'ле", "са'мое нача'ло", "до са'мого нача'ла"], "с са'мого нача'ла", "С + genitive: ‘from’.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 232
L232 = lesson(
    "The same one: тот же, то же са'мое, там же",
    "У нас те же проблемы, и я смотрю' то же са'мое.",
    requires=["тот", "такой", "одинаковый", "время", "проблема"],
    cards=[
        card("Тот же",
             "Же after тот means ‘the same’. Тот declines as usual, and же does not change: тот же, та же, то же, "
             "те же. The word са'мый can follow for emphasis: тот же са'мый.",
             tables=[table(
                 ["", "Masc.", "Fem.", "Neut.", "Plural"],
                 [["Nom.", "тот же", "та же", "то же", "те же"],
                  ["Gen.", "того' же", "той же", "того' же", "тех же"],
                  ["Prep.", "том же", "той же", "том же", "тех же"]])],
             examples=[
                 ex("Он живёт в том же до'ме.", "He lives in the same house.", "в том же до'ме"),
                 ex("У нас те же пробле'мы.", "We have the same problems.", "те же"),
                 ex("Э'то та же са'мая кни'га.", "This is the very same book.", "та же са'мая"),
             ]),
        card("Same thing, same time, same place",
             "То же (са'мое) means ‘the same thing’. Же also joins a place or time word to mean ‘the same’: там же, "
             "туда' же, тогда' же. And в то же вре'мя means ‘at the same time’.",
             tables=[table(
                 ["Phrase", "English"],
                 [["то же са'мое", "the same thing"],
                  ["в то же вре'мя", "at the same time"],
                  ["там же", "in the same place"],
                  ["туда' же", "to the same place"],
                  ["тогда' же", "at that same moment"]])],
             examples=[
                 ex("Я хочу' то же са'мое.", "I want the same thing.", "то же са'мое"),
                 ex("Они' пришли' в то же вре'мя.", "They arrived at the same time.", "в то же вре'мя"),
                 ex("Мы встре'тились там же, где и вчера'.", "We met in the same place as yesterday.", "там же"),
             ]),
        card("Такой же ... как",
             "Такой же means ‘just such’, similar rather than identical. The comparison is introduced by как.",
             examples=[
                 ex("У него' така'я же маши'на, как у меня'.", "He has the same kind of car as mine.", "така'я же маши'на"),
                 ex("Они' но'сят одина'ковые ша'пки.", "They wear identical hats.", "одина'ковые"),
             ]),
    ],
    verify=(vf("тот", "того", "том", "той", "тех") + vf("такой", "такая") + vf("одинаковый", "одинаковые")
            + vf("время", "время") + vf("проблема", "проблемы") + vf("дом", "доме") + vf("машина", "машина")
            + vf("шапка", "шапки") + vf("книга", "книга") + vf("хотеть", "хочу") + vf("встретиться", "встретились")),
    exercises=[
        F("Он живёт в ___ же до'ме. (the same)", "том", ["тот", "того'", "той"], "В + prepositional: том.", "He lives in the same house."),
        F("У нас ___ же пробле'мы. (the same)", "те", ["то", "та", "тех"], "Plural nominative: те.", "We have the same problems."),
        F("Я хочу' то же ___. (the very same thing)", "са'мое", ["са'мый", "са'мая", "са'мые"], "То же са'мое.", "I want the very same thing."),
        F("Они' пришли' в ___ же вре'мя. (the same)", "то", ["тот", "та", "те"], "В то же вре'мя.", "They arrived at the same time."),
        F("Мы встре'тились ___ же, где и вчера'. (in the same place)", "там", ["туда'", "тогда'", "тут"], "Там же = in the same place.", "We met in the same place as yesterday."),
        F("У него' ___ же маши'на, как у меня'. (the same kind of)", "така'я", ["тако'й", "тако'е", "таки'е"], "Маши'на is feminine.", "He has the same kind of car as mine."),
        mc("‘At the same time’ is:", ["в то же вре'мя", "в тот же вре'мя", "на то же вре'мя", "в те же вре'мя"], "в то же вре'мя", "Fixed phrase.", order=True),
        mc("Which word means ‘identical’?", ["одина'ковый", "друго'й", "ра'зный", "ра'вный"], "одина'ковый", "Одина'ковый = identical.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 233
L233 = lesson(
    "But I told you! After all, who is it? The particle же",
    "Я же тебе' говори'л!",
    requires=["же", "ведь", "именно", "даже", "знать"],
    cards=[
        card("A particle that adds feeling",
             "Particles are small words that colour a sentence. They are not translated word for word. Же is the "
             "most common. It sits after the word it emphasizes, often right after the verb or the pronoun.",
             examples=[
                 ex("Ты же зна'ешь!", "But you know!", "же"),
                 ex("Я же тебе' говори'л!", "But I told you!", "же"),
             ]),
        card("Emphasis: after all, but",
             "The speaker reminds the listener of something that should be obvious, often with a hint of irritation. "
             "Ведь does almost the same thing and is often interchangeable.",
             tables=[table(
                 ["With же", "With ведь", "Feeling"],
                 [["Ты же зна'ешь.", "Ты ведь зна'ешь.", "after all, you know"],
                  ["Э'то же невозмо'жно!", "Э'то ведь невозмо'жно!", "but this is impossible!"],
                  ["Вы же врач.", "Вы ведь врач.", "but you are a doctor"]])],
             examples=[
                 ex("Вы же врач, вы должны' знать.", "But you're a doctor, you ought to know.", "Вы же врач"),
             ]),
        card("Question words + же",
             "After a question word же adds impatience or surprise: ‘so what exactly...?’",
             tables=[table(
                 ["Question", "Feeling"],
                 [["Кто же э'то?", "So who is it?"],
                  ["Что же ты де'лаешь?", "What on earth are you doing?"],
                  ["Как же так?", "How can that be?"],
                  ["Где же он?", "Where is he, then?"]])],
             examples=[
                 ex("Что же ты де'лаешь?", "What on earth are you doing?", "Что же"),
                 ex("Кто же э'то был?", "So who was it?", "Кто же"),
             ]),
        card("Именно and даже",
             "Two related words that point to one thing out of many: и'менно (exactly, precisely) and да'же (even).",
             examples=[
                 ex("Э'то и'менно то, что мне ну'жно.", "This is exactly what I need.", "и'менно"),
                 ex("Да'же ребёнок э'то зна'ет.", "Even a child knows this.", "Да'же"),
             ]),
    ],
    verify=(vf("знать", "знаешь") + vf("говорить", "говорил") + vf("делать", "делаешь") + vf("врач", "врач")
            + vf("должен", "должны") + vf("ребёнок", "ребёнок") ),
    exercises=[
        F("Ты ___ зна'ешь! (but)", "же", ["ведь", "да'же", "и'менно"], "Же (or ведь) after the pronoun.", "But you know!"),
        F("Что ___ ты де'лаешь? (on earth)", "же", ["да'же", "и'менно", "бы"], "Question word + же.", "What on earth are you doing?"),
        F("___ ребёнок э'то зна'ет. (even)", "Да'же", ["И'менно", "Же", "Ведь"], "Да'же = even.", "Even a child knows this."),
        F("Э'то ___ то, что мне ну'жно. (exactly)", "и'менно", ["да'же", "ведь", "же"], "И'менно = precisely.", "This is exactly what I need."),
        F("Вы ___ врач, вы должны' знать. (after all)", "же", ["да'же", "и'менно", "бы"], "Вы же = but you are...", "But you're a doctor, you ought to know."),
        F("Э'то ___ невозмо'жно! (but)", "же", ["да'же", "и'менно", "ведь"], "Же adds feeling.", "But this is impossible!"),
        mc("Which word is nearly the same as же in ‘Ты же зна'ешь’?", ["ведь", "да'же", "и'менно", "и'ли"], "ведь", "Ты ведь зна'ешь.", order=True),
        mc("What does Что же ты де'лаешь? express?", ["impatience or surprise", "a polite request", "a neutral question", "a wish"], "impatience or surprise", "Question word + же."),
    ],
)

# ---------------------------------------------------------------------------- 234
L234 = lesson(
    "Review: carrying, driving, the very, the same, же",
    "Ма'ма ведёт дете'й в шко'лу, а па'па везёт су'мки.",
    requires=["нести", "носить", "вести", "самый", "же"],
    cards=[
        card("What you now know",
             "Six verbs: носи'ть / нести' (carry; wear), води'ть / вести' (lead on foot), вози'ть / везти' (transport). "
             "They take an object. The habitual verb covers habit and round trip; the one-way verb covers ‘on the "
             "way’. Add по- for a perfective. Са'мый means ‘very’ before a place or time. Тот же = the same. Же adds "
             "emphasis.",
             tables=[table(
                 ["Meaning", "Habitual", "One way"],
                 [["carry / wear", "носи'ть", "нести'"],
                  ["lead on foot", "води'ть", "вести'"],
                  ["drive, transport", "вози'ть", "везти'"]])],
             examples=[
                 ex("Ма'ма ведёт дете'й в шко'лу, а па'па везёт су'мки.", "Mom is taking the children to school, and Dad is driving the bags.", "ведёт"),
             ]),
    ],
    verify=(vf("нести", "несёт", "несла") + vf("вести", "ведёт", "ведут") + vf("водить", "водит")
            + vf("возить", "возит") + vf("носить", "носит") + vf("ребёнок", "ребёнка")),
    exercises=[
        F("Ка'ждый день ма'ма ___ ребёнка в шко'лу. (walks)", "во'дит", ["ведёт", "несёт", "везёт"], "Habit, on foot: води'ть.", "Every day Mom walks the child to school.", lemma="водить"),
        F("Сейча'с она' ___ ребёнка в шко'лу. (is walking)", "ведёт", ["во'дит", "но'сит", "во'зит"], "Right now: вести'.", "She is walking the child to school now.", lemma="вести"),
        F("Вчера' па'па ___ нас на да'чу на маши'не. (was driving)", "вёз", ["вёл", "нёс", "вози'л"], "A trip in progress by car: вёз.", "Yesterday Dad was driving us to the dacha.", lemma="везти"),
        F("Она' ___ очки'. (wears)", "но'сит", ["несёт", "ведёт", "везёт"], "A habit: носи'ть.", "She wears glasses.", lemma="носить"),
        F("Де'ти хорошо' себя' ___. (behave)", "веду'т", ["во'дят", "несу'т", "везу'т"], "Вести' себя'.", "The children behave well.", lemma="вести"),
        F("Мы бы'ли там с ___ нача'ла. (the very)", "са'мого", ["са'мом", "са'мый", "са'мой"], "С + genitive.", "We were there from the very beginning."),
        F("Он живёт в ___ же до'ме. (the same)", "том", ["тот", "того'", "той"], "В + prepositional.", "He lives in the same house."),
        F("Ты ___ зна'ешь! (but)", "же", ["бы", "да'же", "и'менно"], "Particle же.", "But you know!"),
        mc("Which pair means ‘to drive / to transport’?", ["вози'ть / везти'", "води'ть / вести'", "носи'ть / нести'", "е'здить / е'хать"], "вози'ть / везти'", "Вози'ть / везти'.", order=True),
        mc("Which verb takes only animate objects when you walk?", ["води'ть / вести'", "носи'ть / нести'", "вози'ть / везти'", "ходи'ть / идти'"], "води'ть / вести'", "You lead a person or an animal.", order=True),
    ],
)

UNIT = unit("Unit 24: Carrying, leading and driving; самый and же",
            [L225, L226, L227, L228, L229, L230, L231, L232, L233, L234])
