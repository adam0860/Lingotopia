"""Unit 28: weather and natural disasters; collective numerals and adverbs;
telling time to the minute (textbook module 7, lesson 37)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 273
L273 = lesson(
    "Weather warnings: ли'вень, снегопа'д, мете'ль, гололёд, урага'н",
    "Ожида'ется си'льный ли'вень и поры'вистый ве'тер.",
    requires=["погода", "дождь", "снег", "ветер", "прогноз"],
    cards=[
        card("Words for bad weather",
             "Forecasts and news reports use a special set of nouns for dangerous weather.",
             tables=[table(
                 ["Word", "English"],
                 [["ли'вень (m.)", "downpour, heavy rain"],
                  ["снегопа'д", "snowfall"],
                  ["мете'ль (f.)", "snowstorm, blizzard"],
                  ["гололёд", "ice on roads and surfaces"],
                  ["гололе'дица", "slippery roads (icy conditions)"],
                  ["урага'н", "hurricane, gale"],
                  ["гроза'", "thunderstorm"],
                  ["непого'да", "bad weather"],
                  ["цикло'н / антицикло'н", "low-pressure / high-pressure system"],
                  ["сино'птик", "weather forecaster"]])],
             examples=[
                 ex("Сино'птики предупрежда'ют о си'льном ли'вне.", "Forecasters are warning about heavy rain.", "о си'льном ли'вне"),
                 ex("Накану'не в го'роде был снегопа'д.", "There was a snowfall in the city the day before.", "снегопа'д"),
                 ex("Из-за гололёда на доро'гах мно'го ава'рий.", "Because of the ice there are many accidents on the roads.", "Из-за гололёда"),
             ]),
        card("Ожида'ется and возмо'жен",
             "Forecasts say what is expected. The verb ожида'ться (to be expected) and the short adjective возмо'жен (is "
             "possible) agree with the thing that is expected, in number and gender.",
             tables=[table(
                 ["Phrase", "English"],
                 [["Ожида'ется снегопа'д.", "A snowfall is expected."],
                  ["Ожида'ются си'льные дожди'.", "Heavy rains are expected."],
                  ["Возмо'жен гололёд.", "Ice is possible."],
                  ["Возмо'жны гро'зы.", "Thunderstorms are possible."]])],
             examples=[
                 ex("Ожида'ются си'льные дожди'.", "Heavy rains are expected.", "Ожида'ются"),
                 ex("Возмо'жны гро'зы.", "Thunderstorms are possible.", "Возмо'жны"),
             ]),
        card("Предупрежда'ть о чём?",
             "To warn someone about something: предупрежда'ть / предупреди'ть кого' о чём. The warning itself is "
             "предупрежде'ние.",
             tables=[table(
                 ["Who is warned", "About what"],
                 [["жи'телей (Acc.)", "о мете'ли (Prep.)"],
                  ["нас (Acc.)", "о гололёде (Prep.)"],
                  ["води'телей (Acc.)", "об урага'не (Prep.)"]])],
             examples=[
                 ex("Нас предупреди'ли о гололёде.", "We were warned about the ice.", "предупреди'ли о гололёде"),
                 ex("Предупрежде'ние о непого'де де'йствует кру'глые су'тки.", "The bad-weather warning is in force around the clock.", "Предупрежде'ние"),
             ]),
    ],
    verify=(vf("ливень", "ливень", "ливне", "ливни") + vf("снегопад", "снегопад") + vf("метель", "метель")
            + vf("гололёд", "гололёд", "гололёда") + vf("гололедица", "гололедица") + vf("ураган", "ураган", "урагане")
            + vf("гроза", "грозы") + vf("непогода", "непогоде") + vf("циклон", "циклон") + vf("антициклон", "антициклон")
            + vf("ожидаться", "ожидается", "ожидаются") + vf("возможный", "возможен", "возможны")
            + vf("предупреждать", "предупреждают") + vf("предупредить", "предупредили") + vf("предупреждение", "предупреждение")
            + vf("ветер", "ветре") + vf("авария", "аварий") + vf("накануне", "накануне") + vf("дождь", "дожди")
            + vf("водитель", "водителей") + vf("действовать", "действует")),
    exercises=[
        F("Ожида'ется си'льный ___. (downpour)", "ли'вень", ["ли'вня", "ли'вне", "ли'вни"], "Singular subject: nominative.", "A heavy downpour is expected.", lemma="ливень"),
        F("Ожида'ются си'льные ___. (downpours)", "ли'вни", ["ли'вень", "ли'вня", "ли'вне"], "Plural subject: nominative plural.", "Heavy downpours are expected.", lemma="ливень"),
        F("Из-за ___ на доро'гах мно'го ава'рий. (ice)", "гололёда", ["гололёд", "гололёду", "гололёдом"], "Из-за + genitive.", "Because of the ice there are many accidents on the roads.", lemma="гололёд"),
        F("Сино'птики предупреди'ли нас о си'льном ___. (wind)", "ве'тре", ["ве'тер", "ве'тра", "ве'тром"], "О + prepositional.", "Forecasters warned us about the strong wind.", lemma="ветер"),
        F("Накану'не в го'роде был си'льный ___. (snowfall)", "снегопа'д", ["снегопа'да", "снегопа'ду", "снегопа'де"], "Nominative after был.", "The day before there was heavy snowfall in the city.", lemma="снегопад"),
        F("___ си'льные дожди'. (are expected)", "Ожида'ются", ["Ожида'ется", "Ожида'л", "Ожида'ть"], "Plural subject, plural verb.", "Heavy rains are expected."),
        F("___ гро'зы. (possible)", "Возмо'жны", ["Возмо'жен", "Возмо'жна", "Возмо'жно"], "Plural subject.", "Thunderstorms are possible."),
        mc("What does гололёд mean?", ["ice on roads and surfaces", "heavy rain", "snowfall", "a thunderstorm"], "ice on roads and surfaces", "Гололёд = ice."),
        mc("Which word means a low-pressure system?", ["цикло'н", "антицикло'н", "мете'ль", "ли'вень"], "цикло'н", "Цикло'н = low pressure, антицикло'н = high pressure.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 274
L274 = lesson(
    "Water, earth and snow: наводне'ние, па'водок, о'ползень, сель, лави'на",
    "Из-за ли'вней в реке' поднялся' у'ровень воды'.",
    requires=["вода", "река", "гора", "землетрясение", "опасность"],
    cards=[
        card("Natural disasters",
             "A стихи'я is a force of nature. These are the names of the most common ones.",
             tables=[table(
                 ["Word", "English"],
                 [["наводне'ние", "flood"],
                  ["па'водок", "rising water from snowmelt or rain (a minor flood)"],
                  ["о'ползень (m.)", "landslide"],
                  ["сель (m.)", "mudflow"],
                  ["лави'на", "avalanche"],
                  ["землетрясе'ние", "earthquake"],
                  ["толчо'к", "tremor, jolt"],
                  ["стихи'я", "force of nature"]])],
             examples=[
                 ex("В райо'не реки' ожида'ется па'водок.", "A flood is expected in the area of the river.", "па'водок"),
                 ex("Сель перекры'л доро'гу.", "A mudflow blocked the road.", "Сель"),
                 ex("Землетрясе'ние почу'вствовали жи'тели трёх городо'в.", "The inhabitants of three cities felt the earthquake.", "Землетрясе'ние"),
             ]),
        card("Verbs of water and earth",
             "Reports use a few typical verbs.",
             tables=[table(
                 ["Verb", "English"],
                 [["поднима'ться / подня'ться", "to rise"],
                  ["обру'шиваться / обру'шиться", "to strike, hit (a place); to collapse"],
                  ["затопля'ть / затопи'ть", "to flood (a place)"],
                  ["сходи'ть / сойти'", "to come down (an avalanche, mudflow)"],
                  ["бушева'ть", "to rage"]])],
             examples=[
                 ex("У'ровень воды' в реке' поднима'ется.", "The water level in the river is rising.", "поднима'ется"),
                 ex("Затопи'ло не'сколько у'лиц.", "Several streets were flooded.", "Затопи'ло"),
                 ex("В гора'х сошла' лави'на.", "An avalanche came down in the mountains.", "сошла' лави'на"),
             ]),
        card("A line from a news report",
             "Some set phrases appear in almost every report.",
             tables=[table(
                 ["Phrase", "English"],
                 [["режи'м ЧС", "state of emergency"],
                  ["сход лави'ны", "an avalanche coming down"],
                  ["у'ровень воды'", "water level"],
                  ["си'льный толчо'к", "a strong tremor"]])],
             examples=[
                 ex("На побере'жье обру'шился урага'н.", "A hurricane struck the coast.", "обру'шился"),
             ]),
    ],
    verify=(vf("наводнение", "наводнение") + vf("паводок", "паводок") + vf("оползень", "оползень") + vf("сель", "сель")
            + vf("лавина", "лавина") + vf("землетрясение", "землетрясение") + vf("толчок", "толчок") + vf("стихия", "стихия")
            + vf("подниматься", "поднимается") + vf("затопить", "затопило") + vf("обрушиться", "обрушился")
            + vf("уровень", "уровень") + vf("побережье", "побережье") + vf("перекрыть", "перекрыл") + vf("дорога", "дорогу")
            + vf("почувствовать", "почувствовали") + vf("город", "городов") + vf("река", "реки", "реке")
            + vf("вода", "воды") + vf("сойти", "сошла") + vf("район", "районе") + vf("бушевать", "бушевать")
            + vf("улица", "улиц")),
    exercises=[
        F("В горах сошла' ___. (avalanche)", "лави'на", ["лави'ну", "лави'ны", "лави'не"], "Feminine subject; сошла' agrees.", "An avalanche came down in the mountains.", lemma="лавина"),
        F("У'ровень воды' в реке' ___. (is rising)", "поднима'ется", ["поднима'ются", "поднима'ться", "поднима'ют"], "Singular subject: у'ровень.", "The water level in the river is rising."),
        F("Землетрясе'ние почу'вствовали жи'тели трёх ___. (cities)", "городо'в", ["города'", "го'роды", "города'м"], "Три + genitive, but трёх: genitive plural.", "The inhabitants of three cities felt the earthquake.", lemma="город"),
        F("На побере'жье обру'шился ___. (hurricane)", "урага'н", ["урага'на", "урага'ну", "урага'ном"], "Masculine subject.", "A hurricane struck the coast."),
        F("Сель перекры'л ___. (the road)", "доро'гу", ["доро'га", "доро'ги", "доро'ге"], "Accusative object.", "A mudflow blocked the road.", lemma="дорога"),
        F("В райо'не реки' ожида'ется ___. (a flood)", "па'водок", ["па'водка", "па'воду", "па'водке"], "Ожида'ется + nominative.", "A flood is expected in the area of the river.", lemma="паводок"),
        mc("Which word means ‘landslide’?", ["о'ползень", "сель", "лави'на", "па'водок"], "о'ползень", "О'ползень = landslide.", order=True),
        mc("What is сель?", ["a mudflow", "an earthquake", "a hurricane", "a forecaster"], "a mudflow", "Сель = mudflow.", order=True),
        mc("Which word means a smaller shock after an earthquake?", ["толчо'к", "наводне'ние", "мете'ль", "стихи'я"], "толчо'к", "Толчо'к = tremor.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 275
L275 = lesson(
    "Fire and rescue: пожа'р, туши'ть, спаса'тель, эвакуа'ция",
    "Спаса'тели потуши'ли пожа'р и эвакуи'ровали жи'телей.",
    requires=["пожар", "огонь", "спасти", "помощь", "опасность"],
    cards=[
        card("Fire and rescue words",
             "A basic vocabulary for reports about fires and rescue work.",
             tables=[table(
                 ["Word", "English"],
                 [["пожа'р", "fire"],
                  ["ого'нь (m.)", "fire, flame"],
                  ["пла'мя (n.)", "flame, blaze"],
                  ["дым", "smoke"],
                  ["спаса'тель (m.)", "rescuer"],
                  ["вертолёт", "helicopter"],
                  ["эвакуа'ция", "evacuation"],
                  ["МЧС", "Ministry of Emergency Situations (emergency services)"]])],
             examples=[
                 ex("Из-за ды'ма в до'ме бы'ло тру'дно дыша'ть.", "Because of the smoke it was hard to breathe in the house.", "Из-за ды'ма"),
                 ex("Дом горе'л всю ночь.", "The house burned all night.", "горе'л"),
             ]),
        card("Verbs",
             "The actions of the fire service and rescuers.",
             tables=[table(
                 ["Verb", "English"],
                 [["туши'ть / потуши'ть", "to extinguish"],
                  ["спаса'ть / спасти'", "to rescue, to save"],
                  ["эвакуи'ровать", "to evacuate (both aspects)"],
                  ["распространя'ться / распространи'ться", "to spread"],
                  ["ликвиди'ровать", "to eliminate, to deal with"],
                  ["горе'ть / сгоре'ть", "to burn / to burn down"]])],
             examples=[
                 ex("Спаса'тели потуши'ли пожа'р за три часа'.", "The rescuers put out the fire in three hours.", "потуши'ли"),
                 ex("Ого'нь распространи'лся на сосе'дний дом.", "The fire spread to the neighboring house.", "распространи'лся"),
                 ex("Спаса'тели эвакуи'ровали жи'телей до'ма.", "The rescuers evacuated the residents of the building.", "эвакуи'ровали"),
             ]),
        card("They: the impersonal plural",
             "News reports often leave out who is doing the work and use the plural ‘they’ in the past tense. You know this from the "
             "indefinite-personal sentences.",
             examples=[
                 ex("Пожа'р туши'ли почти' шесть часо'в.", "They were putting out the fire for almost six hours.", "туши'ли"),
                 ex("Люде'й спасли' с кры'ши на вертолёте.", "People were rescued from the roof by helicopter.", "спасли'"),
             ]),
    ],
    verify=(vf("пожар", "пожар") + vf("огонь", "огонь") + vf("пламя", "пламя") + vf("дым", "дыма") + vf("спасатель", "спасатели")
            + vf("вертолёт", "вертолёте") + vf("эвакуация", "эвакуация") + vf("гореть", "горел")
            + vf("потушить", "потушили") + vf("спасти", "спасли") + vf("эвакуировать", "эвакуировали")
            + vf("распространиться", "распространился") + vf("ликвидировать", "ликвидировать")
            + vf("дышать", "дышать") + vf("житель", "жителей") + vf("крыша", "крыши") + vf("соседний", "соседний")
            + vf("тушить", "тушили")),
    exercises=[
        F("Спаса'тели ___ пожа'р за три часа'. (put out)", "потуши'ли", ["туши'ли", "туши'ть", "потуши'ть"], "A result in a fixed time: perfective.", "The rescuers put out the fire in three hours."),
        F("Ого'нь распространи'лся на сосе'дний ___. (house)", "дом", ["до'ма", "до'му", "до'ме"], "На + accusative (= nominative).", "The fire spread to the neighboring house.", lemma="дом"),
        F("Из-за ___ в до'ме бы'ло тру'дно дыша'ть. (smoke)", "ды'ма", ["дым", "ды'му", "ды'мом"], "Из-за + genitive.", "Because of the smoke it was hard to breathe in the house.", lemma="дым"),
        F("Спаса'тели эвакуи'ровали ___ до'ма. (the residents)", "жи'телей", ["жи'тели", "жи'телям", "жи'телями"], "Animate accusative plural = genitive.", "The rescuers evacuated the residents of the building.", lemma="житель"),
        F("Люде'й спасли' с кры'ши на ___. (helicopter)", "вертолёте", ["вертолёт", "вертолёта", "вертолёту"], "На + prepositional (means of transport).", "People were rescued from the roof by helicopter.", lemma="вертолёт"),
        F("Дом ___ всю ночь. (was burning)", "горе'л", ["горе'ла", "горе'ло", "горе'ли"], "Masculine singular past.", "The house burned all night."),
        mc("What does эвакуа'ция mean?", ["evacuation", "aftermath", "fire", "rescue worker"], "evacuation", "Эвакуа'ция.", order=True),
        mc("Which noun is neuter?", ["пла'мя", "дым", "пожа'р", "вертолёт"], "пла'мя", "Пла'мя is one of the few neuter nouns in -мя.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 276
L276 = lesson(
    "Damage and aftermath: после'дствия, уще'рб, разруше'ния, убы'тки",
    "Уще'рб от наводне'ния соста'вил не'сколько миллио'нов рубле'й.",
    requires=["последствие", "ущерб", "разрушить", "восстановить", "население"],
    cards=[
        card("Nouns for damage",
             "Most of these appear in the plural in reports.",
             tables=[table(
                 ["Word", "English"],
                 [["после'дствия (pl.)", "consequences, aftermath"],
                  ["уще'рб", "damage, harm"],
                  ["разруше'ния (pl.)", "destruction"],
                  ["поврежде'ния (pl.)", "damage (physical)"],
                  ["убы'тки (pl.)", "losses (economic)"],
                  ["масшта'б", "scale, extent"],
                  ["кров", "shelter (roof over one's head)"]])],
             examples=[
                 ex("Масшта'б разруше'ний о'чень большо'й.", "The scale of the destruction is very large.", "Масшта'б"),
                 ex("Лю'ди оста'лись без кро'ва.", "People were left homeless.", "без кро'ва"),
             ]),
        card("Verbs",
             "What the damage amounts to, and what is done about it.",
             tables=[table(
                 ["Verb", "English"],
                 [["составля'ть / соста'вить", "to amount to"],
                  ["восстана'вливать / восстанови'ть", "to restore, rebuild"],
                  ["ликвиди'ровать", "to clean up (e.g. consequences)"],
                  ["разруша'ть / разру'шить", "to destroy"],
                  ["оста'ться без + Gen.", "to be left without"]])],
             examples=[
                 ex("Уще'рб соста'вил не'сколько миллио'нов рубле'й.", "The damage amounted to several million rubles.", "соста'вил"),
                 ex("Ликвиди'ровать после'дствия урага'на бу'дут не'сколько неде'ль.", "It will take several weeks to clean up after the hurricane.", "Ликвиди'ровать"),
             ]),
        card("According to preliminary data",
             "Reports start with sources and estimates: по + Dative plural.",
             tables=[table(
                 ["Phrase", "English"],
                 [["по предвари'тельным да'нным", "according to preliminary data"],
                  ["по предвари'тельным оце'нкам", "according to preliminary estimates"],
                  ["по сообще'нию МЧС", "according to the report of the emergency services"]])],
             examples=[
                 ex("По предвари'тельным оце'нкам, уще'рб — о'коло двух миллио'нов рубле'й.", "According to preliminary estimates, the damage is about two million rubles.", "По предвари'тельным оце'нкам"),
             ]),
    ],
    verify=(vf("последствие", "последствия") + vf("ущерб", "ущерб") + vf("разрушение", "разрушений", "разрушения")
            + vf("повреждение", "повреждения") + vf("убыток", "убытки") + vf("масштаб", "масштаб") + vf("кров", "крова")
            + vf("составить", "составил") + vf("восстановить", "восстановить") + vf("ликвидировать", "ликвидировать")
            + vf("разрушить", "разрушить") + vf("оценка", "оценкам") + vf("данные", "данным")
            + vf("несколько", "несколько") + vf("миллион", "миллионов") + vf("рубль", "рублей")
            + vf("обещать", "обещали") + vf("остаться", "остались")),
    exercises=[
        F("Масшта'б ___ о'чень большо'й. (of destruction)", "разруше'ний", ["разруше'ния", "разруше'нию", "разруше'нием"], "Genitive plural after масшта'б.", "The scale of the destruction is very large.", lemma="разрушение"),
        F("Лю'ди оста'лись без ___. (shelter)", "кро'ва", ["кров", "кро'ву", "кро'вом"], "Без + genitive.", "People were left homeless.", lemma="кров"),
        F("Уще'рб ___ не'сколько миллио'нов рубле'й. (amounted to)", "соста'вил", ["соста'вила", "соста'вило", "соста'вили"], "Masculine subject.", "The damage amounted to several million rubles."),
        F("Спаса'тели бу'дут ___ после'дствия урага'на. (clean up)", "ликвиди'ровать", ["ликвиди'ровал", "ликвиди'руют", "ликвиди'ровали"], "After бу'дут: infinitive.", "The rescuers will clean up after the hurricane."),
        F("Власти обеща'ли ___ разру'шенные дома'. (rebuild)", "восстанови'ть", ["восстанови'ли", "восстанови'л", "восстанови'ла"], "After обеща'ли: infinitive.", "The authorities promised to rebuild the destroyed houses."),
        F("По предвари'тельным ___ уще'рб — о'коло двух миллио'нов. (estimates)", "оце'нкам", ["оце'нки", "оце'нок", "оце'нками"], "По + dative plural.", "According to preliminary estimates the damage is about two million.", lemma="оценка"),
        mc("Which noun is usually plural in reports: ‘consequences’?", ["после'дствия", "уще'рб", "масшта'б", "кров"], "после'дствия", "После'дствия.", order=True),
        mc("‘Оста'ться без кро'ва’ means:", ["to be left homeless", "to be left hungry", "to be left alone", "to stay at home"], "to be left homeless", "Кров = shelter.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 277
L277 = lesson(
    "In the news: накану'не, спустя', кру'глые су'тки, приходи'лось",
    "Спустя' неде'лю в го'роде всё ещё нет электри'чества.",
    requires=["население", "область", "сообщение", "сообщить", "оказаться"],
    cards=[
        card("Time words in reports",
             "A few time expressions that appear again and again.",
             tables=[table(
                 ["Word", "English"],
                 [["накану'не", "the day before"],
                  ["накану'не + Gen.", "on the eve of"],
                  ["спустя' + Acc.", "after, later"],
                  ["кру'глые су'тки", "around the clock"],
                  ["в тече'ние + Gen.", "during, for a period of"]])],
             examples=[
                 ex("Накану'не в о'бласти объяви'ли режи'м ЧС.", "The day before, a state of emergency was declared in the region.", "Накану'не"),
                 ex("Спустя' два часа' пожа'р потуши'ли.", "Two hours later the fire was put out.", "Спустя' два часа'"),
                 ex("Спаса'тели рабо'тают кру'глые су'тки.", "The rescuers work around the clock.", "кру'глые су'тки"),
             ]),
        card("Verbs that report events",
             "Verbs for what happened to people.",
             tables=[table(
                 ["Verb", "English"],
                 [["приходи'ться / прийти'сь + inf.", "to have to (impersonal; the person is in the dative)"],
                  ["оказа'ться", "to find oneself, to turn out"],
                  ["остава'ться / оста'ться", "to remain"],
                  ["сообща'ть / сообщи'ть", "to report"],
                  ["объявля'ть / объяви'ть", "to declare, announce"]])],
             examples=[
                 ex("Жи'телям пришло'сь поки'нуть дома'.", "The residents had to leave their homes.", "пришло'сь"),
                 ex("Мно'гие оказа'лись без электри'чества.", "Many found themselves without electricity.", "оказа'лись"),
                 ex("Река' остаётся высо'кой.", "The river remains high.", "остаётся"),
             ]),
        card("Reporting the source",
             "Reports often name the source in an introductory phrase.",
             tables=[table(
                 ["Phrase", "English"],
                 [["Как сообща'ют в МЧС, …", "As the emergency services report, …"],
                  ["По сообще'нию МЧС, …", "According to a report by the emergency services, …"]])],
             examples=[
                 ex("Как сообща'ют в МЧС, пострада'вших нет.", "As the emergency services report, there are no casualties.", "Как сообща'ют"),
             ]),
    ],
    verify=(vf("накануне", "накануне") + vf("спустя", "спустя") + vf("круглый", "круглые") + vf("сутки", "сутки")
            + vf("приходиться", "приходилось") + vf("прийтись", "пришлось") + vf("оказаться", "оказались")
            + vf("оставаться", "остаётся") + vf("сообщать", "сообщают") + vf("сообщить", "сообщить")
            + vf("объявить", "объявили") + vf("покинуть", "покинуть") + vf("электричество", "электричества")
            + vf("высокий", "высокой") + vf("область", "области") + vf("потушить", "потушили")
            + vf("работать", "работают")),
    exercises=[
        F("___ урага'на в го'роде объяви'ли режи'м ЧС. (the day before)", "Накану'не", ["Спустя'", "Через", "Пото'м"], "Накану'не + genitive: on the eve of.", "On the eve of the hurricane a state of emergency was declared in the city."),
        F("Спустя' ___ часа' пожа'р потуши'ли. (two)", "два", ["двух", "двум", "двумя'"], "Спустя' + accusative.", "Two hours later the fire was put out."),
        F("Жи'телям ___ поки'нуть дома'. (had to)", "пришло'сь", ["пришла'", "пришёл", "пришли'"], "Impersonal: neuter singular.", "The residents had to leave their homes."),
        F("Спаса'тели рабо'тают ___ су'тки. (around the clock)", "кру'глые", ["кру'глый", "кру'глых", "кру'глая"], "Plural noun: су'тки.", "The rescuers work around the clock.", lemma="круглый"),
        F("Мно'гие жи'тели ___ без электри'чества. (found themselves)", "оказа'лись", ["оказа'ться", "оказа'лся", "оказа'лась"], "Plural past.", "Many residents found themselves without electricity."),
        F("Как ___ в МЧС, пострада'вших нет. (report)", "сообща'ют", ["сообща'ть", "сообща'ла", "сообща'ем"], "Third person plural.", "As the emergency services report, there are no casualties."),
        F("Река' ещё ___ высо'кой. (remains)", "остаётся", ["остаю'тся", "остава'ться", "оста'лся"], "Singular subject, present tense.", "The river is still high."),
        mc("What does ‘спустя' неде'лю’ mean?", ["a week later", "a week earlier", "for a week", "every week"], "a week later", "Спустя' = after.", order=True),
        mc("‘Приходи'лось’ expresses:", ["necessity (had to)", "permission", "wish", "ability"], "necessity (had to)", "Impersonal verb of necessity.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 278
L278 = lesson(
    "Collective numerals: дво'е, тро'е, че'тверо, пя'теро",
    "Дво'е пострада'ли, а че'тверо оста'лись без кро'ва.",
    requires=["житель", "человек", "пострадать", "погибнуть", "спасти"],
    cards=[
        card("The collective numerals",
             "Besides the ordinary numerals, Russian has a set of collective numerals, mostly used in news about groups of "
             "people. Above ten they do not exist, and from six upward they are rare.",
             tables=[table(
                 ["Number", "Word"],
                 [["2", "дво'е"],
                  ["3", "тро'е"],
                  ["4", "че'тверо"],
                  ["5", "пя'теро"],
                  ["6", "ше'стеро"],
                  ["7", "се'меро"],
                  ["8", "во'сьмеро"],
                  ["9", "де'вятеро"],
                  ["10", "де'сятеро"]])],
             examples=[
                 ex("На вечери'нке нас бы'ло всего' че'тверо.", "There were only four of us at the party.", "че'тверо"),
                 ex("Тро'е тури'стов пропа'ли в гора'х.", "Three tourists went missing in the mountains.", "Тро'е тури'стов"),
             ]),
        card("Case endings",
             "The endings are always stressed. Дво'е and тро'е decline like soft adjectives, че'тверо and higher like hard ones. "
             "In the accusative, animate objects use the genitive.",
             tables=[table(
                 ["Case", "2, 3", "4"],
                 [["Nom.", "дво'е, тро'е", "че'тверо"],
                  ["Gen. / Acc.", "двои'х, трои'х", "четверы'х"],
                  ["Dat.", "двои'м, трои'м", "четверы'м"],
                  ["Instr.", "двои'ми, трои'ми", "четверы'ми"],
                  ["Prep.", "(о) двои'х, трои'х", "(о) четверы'х"]])],
             examples=[
                 ex("Спаса'тели нашли' всех четверы'х.", "The rescuers found all four.", "всех четверы'х"),
                 ex("О двои'х ничего' не изве'стно.", "Nothing is known about the two.", "О двои'х"),
             ]),
        card("In news reports",
             "A collective numeral is often used without a noun, in the sense ‘people’. The verb is plural.",
             tables=[table(
                 ["With a noun", "Without a noun"],
                 [["Дво'е тури'стов поги'бли.", "Дво'е поги'бли."],
                  ["Че'тверо жи'телей пострада'ли.", "Че'тверо пострада'ли."]])],
             examples=[
                 ex("Дво'е поги'бли и че'тверо пострада'ли.", "Two died and four were injured.", "Дво'е поги'бли и че'тверо пострада'ли"),
             ]),
    ],
    verify=(vf("двое", "двое", "двоих", "двоим") + vf("трое", "трое", "троих", "троим") + vf("четверо", "четверо", "четверых", "четверым", "четверыми")
            + vf("пятеро", "пятеро") + vf("шестеро", "шестеро") + vf("семеро", "семеро") + vf("восьмеро", "восьмеро")
            + vf("девятеро", "девятеро") + vf("десятеро", "десятеро") + vf("турист", "туристов") + vf("вечеринка", "вечеринке")
            + vf("пропасть", "пропали") + vf("гора", "горах") + vf("погибнуть", "погибли") + vf("пострадать", "пострадали")
            + vf("спасатель", "спасатели") + vf("найти", "нашли") + vf("известно", "известно") + vf("ребёнок", "детей")),
    exercises=[
        F("Нас бы'ло ___. (four)", "че'тверо", ["четы'ре", "четы'рёх", "четвёртый"], "Group of people: collective numeral.", "There were four of us."),
        F("Дво'е пострада'ли, а че'тверо ___ без кро'ва. (were left)", "оста'лись", ["оста'лся", "оста'лась", "оста'вшись"], "Plural verb with a collective numeral.", "Two were injured and four were left homeless."),
        F("В гора'х пропа'ли тро'е ___. (tourists)", "тури'стов", ["тури'ста", "тури'сты", "тури'стам"], "Collective numeral + genitive plural.", "Three tourists went missing in the mountains.", lemma="турист"),
        F("Спаса'тели нашли' всех ___. (four)", "четверы'х", ["че'тверо", "четверы'м", "четверы'ми"], "Animate accusative = genitive.", "The rescuers found all four."),
        F("О ___ ничего' не изве'стно. (two)", "двои'х", ["дво'е", "двои'м", "двои'ми"], "О + prepositional.", "Nothing is known about the two."),
        F("У них тро'е ___. (children)", "дете'й", ["де'ти", "де'тям", "детьми'"], "Genitive plural.", "They have three children."),
        mc("Which noun phrase is correct?", ["че'тверо дете'й", "четы'ре дете'й", "че'тверо ребёнка", "че'тверо де'вочек"], "че'тверо дете'й", "Collective numeral + genitive plural; not for girls only.", order=True),
        mc("Collective numerals above ten:", ["do not exist", "are the same as ordinary numerals", "are rare but exist", "are used for women"], "do not exist", "The list ends at де'сятеро.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 279
L279 = lesson(
    "дво'е часо'в or два часа'? When to use collective numerals",
    "Ва'ня купи'л дво'е часо'в: одни' себе', одни' бра'ту.",
    requires=["мужчина", "женщина", "ребёнок", "час", "друг"],
    cards=[
        card("When the collective numeral is used",
             "Where both a collective and an ordinary numeral are possible, the collective one is preferred in these cases.",
             tables=[table(
                 ["Situation", "Example"],
                 [["plural-only nouns", "дво'е часо'в, тро'е су'ток, че'тверо кани'кул"],
                  ["masculine nouns in -а / -я", "дво'е мужчи'н"],
                  ["children and groups of people", "тро'е дете'й"],
                  ["news-report style", "дво'е пострада'вших"]])],
             examples=[
                 ex("Ва'ня купи'л дво'е часо'в: одни' себе', одни' бра'ту.", "Vanya bought two watches: one for himself, one for his brother.", "дво'е часо'в"),
                 ex("В па'рке сиде'ли дво'е мужчи'н.", "Two men were sitting in the park.", "дво'е мужчи'н"),
                 ex("У них тро'е дете'й.", "They have three children.", "тро'е дете'й"),
             ]),
        card("Ordinary or collective?",
             "Compare the meanings. Часы' (watch) is a plural-only noun, so it needs the collective numeral; часы' as ‘hours’ "
             "is the ordinary noun час.",
             tables=[table(
                 ["Phrase", "Meaning"],
                 [["дво'е часо'в", "two watches or clocks"],
                  ["два часа'", "two hours"],
                  ["тро'е су'ток", "three days and nights"],
                  ["три сестры'", "three sisters (women: ordinary numeral)"]])],
             examples=[
                 ex("Мы жда'ли тро'е су'ток.", "We waited for three days and nights.", "тро'е су'ток"),
                 ex("У меня' три сестры'.", "I have three sisters.", "три сестры'"),
             ]),
        card("Not for women",
             "The collective numeral is for males, or for mixed groups. For women only, use the ordinary numeral. "
             "A mixed group can use the collective numeral without a noun.",
             examples=[
                 ex("Нас бы'ло тро'е: сестра', брат и я.", "There were three of us: my sister, my brother and I.", "тро'е"),
                 ex("Нам нужны' че'тверо кани'кул в год.", "We need four vacations a year.", "че'тверо кани'кул"),
             ]),
    ],
    verify=(vf("часы", "часов") + vf("час", "часа") + vf("мужчина", "мужчин") + vf("ребёнок", "детей")
            + vf("сутки", "суток") + vf("каникулы", "каникул") + vf("сестра", "сестры", "сестёр") + vf("парк", "парке")
            + vf("сидеть", "сидели") + vf("ждать", "ждали") + vf("купить", "купил") + vf("брат", "брату")
            + vf("нужный", "нужны") + vf("пострадавший", "пострадавших")),
    exercises=[
        F("Ва'ня купи'л дво'е ___. (watches)", "часо'в", ["часа'", "часы'", "часа'м"], "Plural-only noun: genitive plural.", "Vanya bought two watches.", lemma="час"),
        F("У них тро'е ___. (children)", "дете'й", ["де'ти", "де'тям", "детьми'"], "Genitive plural.", "They have three children."),
        F("В ко'мнате сиде'ли дво'е ___. (men)", "мужчи'н", ["мужчи'ны", "мужчи'на", "мужчи'нам"], "Genitive plural.", "Two men were sitting in the room.", lemma="мужчина"),
        F("Мы жда'ли тро'е ___. (days and nights)", "су'ток", ["су'тки", "су'ткам", "су'тками"], "Genitive plural.", "We waited for three days and nights.", lemma="сутки"),
        F("У меня' три ___. (sisters)", "сестры'", ["сестёр", "сестре'", "сестра'м"], "Women: ordinary numeral three + genitive singular.", "I have three sisters.", lemma="сестра"),
        F("Нам нужны' че'тверо ___ в год. (vacations)", "кани'кул", ["кани'кулы", "кани'кулам", "кани'кулах"], "Genitive plural.", "We need four vacations a year.", lemma="каникулы"),
        mc("Which means ‘two watches’?", ["дво'е часо'в", "два часа'", "две часа'", "дво'е часа'"], "дво'е часо'в", "Часы' (watches) needs a collective numeral.", order=True),
        mc("Which noun cannot take a collective numeral?", ["сёстры", "мужчи'ны", "де'ти", "часы'"], "сёстры", "Not used for women only.", order=True),
    ],
)


# ---------------------------------------------------------------------------- 280
L280 = lesson(
    "Together as a group: вдвоём, втроём, вчетвером, впятером",
    "Мы пое'хали в го'ры вчетверо'м.",
    requires=["вместе", "друг", "семья", "поездка", "путешествие"],
    cards=[
        card("Collective adverbs",
             "To say that an action is done by a small group together, put в in front of the collective numeral and use "
             "the ending -ом (-ём for 2 and 3). These adverbs do not change.",
             tables=[table(
                 ["Number", "Adverb", "English"],
                 [["2", "вдвоём", "the two of us/you/them, together"],
                  ["3", "втроём", "as a group of three"],
                  ["4", "вчетверо'м", "as a group of four"],
                  ["5", "впятеро'м", "as a group of five"]])],
             examples=[
                 ex("Мы с дру'гом путеше'ствовали вдвоём.", "My friend and I traveled as a pair.", "вдвоём"),
                 ex("Пое'здки вдвоём веселе'е.", "Trips for two are more fun.", "вдвоём"),
                 ex("Мы пое'хали в го'ры вчетверо'м.", "The four of us went to the mountains.", "вчетверо'м"),
             ]),
        card("Using them with verbs",
             "The adverb tells you how many people act together. It often replaces вме'сте in a sentence about a small group.",
             tables=[table(
                 ["Phrase", "English"],
                 [["прийти' втроём", "to come as a group of three"],
                  ["жить вчетверо'м", "to live, the four of us"],
                  ["оста'ться вдвоём", "to be left alone together, the two of us"],
                  ["обе'дать вдвоём", "to have lunch, the two of us"]])],
             examples=[
                 ex("Мы жи'ли впятеро'м в одно'й ко'мнате.", "The five of us lived in one room.", "впятеро'м"),
                 ex("В го'сти они' пришли' втроём.", "The three of them came to visit.", "втроём"),
             ]),
        card("Fitting in",
             "Collective adverbs are common when you speak about whether a group fits, travels or sits together.",
             examples=[
                 ex("Впятеро'м мы не помести'мся в маши'не.", "The five of us won't fit in the car.", "Впятеро'м"),
                 ex("Вчетверо'м мы сиде'ли за одни'м сто'ликом.", "The four of us sat at one table.", "Вчетверо'м"),
             ]),
    ],
    verify=(vf("друг", "другом") + vf("путешествовать", "путешествовали") + vf("поездка", "поездки") + vf("весёлый", "веселее")
            + vf("гора", "горы") + vf("жить", "жили") + vf("комната", "комнате") + vf("гость", "гости")
            + vf("прийти", "пришли") + vf("поместиться", "поместимся") + vf("машина", "машине") + vf("сидеть", "сидели")
            + vf("столик", "столиком")),
    exercises=[
        F("Мы с дру'гом путеше'ствовали ___. (as a pair)", "вдвоём", ["дво'е", "двои'х", "два"], "в + collective numeral + -ём.", "My friend and I traveled together."),
        F("Нас бы'ло тро'е, и мы пошли' в кино' ___. (as a group of three)", "втроём", ["тро'е", "трои'м", "три"], "Adverb for a group of three.", "There were three of us and we went to the cinema together."),
        F("В маши'не мы помести'мся то'лько ___. (the four of us)", "вчетверо'м", ["че'тверо", "четверы'х", "четы'ре"], "в + четверо + -ом.", "We will only fit in the car as four."),
        F("Мы жи'ли ___ в одно'й ко'мнате. (the five of us)", "впятеро'м", ["пя'теро", "пятеры'х", "пять"], "в + пятеро + -ом.", "The five of us lived in one room."),
        mc("What does вчетверо'м mean?", ["as a group of four", "four times", "fourth", "four at a time"], "as a group of four", "Collective adverb for four.", order=True),
        mc("Which adverb means ‘as a group of three’?", ["втроём", "вдвоём", "вчетверо'м", "вме'сте"], "втроём", "Втроём.", order=True),
        mc("Collective adverbs are formed from:", ["в + collective numeral + -ом / -ём", "в + ordinary numeral", "по + dative", "с + instrumental"], "в + collective numeral + -ом / -ём", "A small set of fixed adverbs.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 281
L281 = lesson(
    "Telling time (1): пять мину'т седьмо'го, полови'на пе'рвого",
    "Сейча'с пять мину'т седьмо'го.",
    requires=["час", "минута", "время", "половина", "утро"],
    cards=[
        card("Digital time",
             "In everyday speech you will often hear the digital style. Say the hour and then the minutes, one after another.",
             tables=[table(
                 ["Time", "Russian"],
                 [["8:25", "во'семь два'дцать пять"],
                  ["4:50", "четы'ре пятьдеся'т"],
                  ["10:15", "де'сять пятна'дцать"]])],
             examples=[
                 ex("Сейча'с во'семь два'дцать пять.", "It is eight twenty-five now.", "во'семь два'дцать пять"),
             ]),
        card("Russian-style time: minutes of the next hour",
             "The day starts at midnight, so 12:05 a.m. is five minutes into the first hour. Russians say ‘five minutes of the "
             "first’: the number of minutes, then the hour that has begun, as an ordinal in the genitive. This is used for 1–29 minutes.",
             tables=[table(
                 ["Time", "Russian"],
                 [["12:05", "пять мину'т пе'рвого"],
                  ["1:01", "одна' мину'та второ'го"],
                  ["3:10", "де'сять мину'т четвёртого"],
                  ["7:15", "пятна'дцать мину'т восьмо'го"],
                  ["11:29", "два'дцать де'вять мину'т двена'дцатого"]])],
             examples=[
                 ex("Сейча'с де'сять мину'т четвёртого.", "It is ten past three.", "де'сять мину'т четвёртого"),
                 ex("Сейча'с пятна'дцать мину'т восьмо'го.", "It is a quarter past seven.", "пятна'дцать мину'т восьмо'го"),
             ]),
        card("Half past",
             "For 30 minutes say полови'на + the next hour in the genitive. In speech полови'на is often shortened to пол-: "
             "полседьмо'го.",
             tables=[table(
                 ["Time", "Long form", "Short form"],
                 [["12:30", "полови'на пе'рвого", "полпе'рвого"],
                  ["6:30", "полови'на седьмо'го", "полседьмо'го"],
                  ["9:30", "полови'на деся'того", "полдеся'того"]])],
             examples=[
                 ex("Сейча'с полови'на седьмо'го.", "It is half past six.", "полови'на седьмо'го"),
                 ex("Сейча'с че'тверть восьмо'го.", "It is a quarter past seven.", "че'тверть восьмо'го"),
             ]),
    ],
    verify=(vf("восемь", "восемь") + vf("двадцать", "двадцать") + vf("пятьдесят", "пятьдесят") + vf("десять", "десять")
            + vf("пятнадцать", "пятнадцать") + vf("минута", "минута", "минут") + vf("первый", "первого") + vf("второй", "второго")
            + vf("четвёртый", "четвёртого") + vf("восьмой", "восьмого") + vf("двенадцатый", "двенадцатого")
            + vf("седьмой", "седьмого") + vf("десятый", "десятого") + vf("половина", "половина") + vf("четверть", "четверть")
            + vf("девять", "девять") + vf("пятнадцать", "пятнадцать")),
    exercises=[
        F("3:10 — де'сять мину'т ___. (fourth hour)", "четвёртого", ["четвёртый", "четвёртому", "четы'ре"], "Genitive ordinal.", "It is ten past three."),
        F("7:15 — пятна'дцать мину'т ___.", "восьмо'го", ["восьмо'й", "восьмо'му", "во'семь"], "Genitive ordinal.", "It is a quarter past seven."),
        F("6:30 — ___ седьмо'го. (half)", "полови'на", ["полови'ну", "полови'ны", "полови'не"], "Nominative: полови'на седьмо'го.", "It is half past six.", lemma="половина"),
        F("12:05 — пять мину'т ___.", "пе'рвого", ["пе'рвый", "пе'рвому", "оди'н"], "Genitive ordinal.", "It is five past twelve."),
        F("1:01 — одна' ___ второ'го. (minute)", "мину'та", ["мину'ту", "мину'ты", "мину'те"], "Одна' + nominative singular.", "It is one minute past one.", lemma="минута"),
        F("11:29 — два'дцать де'вять ___ двена'дцатого. (minutes)", "мину'т", ["мину'ты", "мину'та", "мину'там"], "Genitive plural after 9.", "It is twenty-nine minutes past eleven.", lemma="минута"),
        mc("What time is ‘пять мину'т седьмо'го’?", ["6:05", "7:05", "5:07", "6:50"], "6:05", "The sixth hour has ended; five minutes of the seventh.", order=True),
        mc("What time is ‘полови'на пе'рвого’?", ["12:30", "1:30", "0:50", "12:50"], "12:30", "Half of the first hour.", order=True),
        mc("‘Полдеся'того’ is the same as:", ["полови'на деся'того", "де'сять часо'в", "де'сять мину'т", "че'тверть деся'того"], "полови'на деся'того", "The short пол- form.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 282
L282 = lesson(
    "Telling time (2): без двадцати' три, без че'тверти во'семь",
    "Сейча'с без десяти' во'семь.",
    requires=["час", "минута", "время", "половина", "утро"],
    cards=[
        card("After half past: ‘without’",
             "From 31 to 59 minutes Russians look ahead and say how many minutes are missing: без + genitive of the number + the "
             "next hour as an ordinary number. The word мину'та is usually left out, except for amounts under five.",
             tables=[table(
                 ["Time", "Russian"],
                 [["2:40", "без двадцати' три"],
                  ["3:50", "без десяти' четы'ре"],
                  ["7:35", "без двадцати' пяти' во'семь"],
                  ["11:31", "без двадцати' девяти' двена'дцать"],
                  ["1:59", "без одно'й мину'ты два"],
                  ["9:58", "без двух мину'т де'сять"]])],
             examples=[
                 ex("Сейча'с без десяти' во'семь.", "It is ten to eight.", "без десяти' во'семь"),
                 ex("Сейча'с без двадцати' пяти' во'семь.", "It is twenty-five to eight.", "без двадцати' пяти' во'семь"),
             ]),
        card("A quarter and one o'clock",
             "Че'тверть (a quarter) is used as in English. One o'clock is simply час.",
             tables=[table(
                 ["Time", "Russian"],
                 [["7:15", "че'тверть восьмо'го"],
                  ["7:45", "без че'тверти во'семь"],
                  ["12:40", "без двадцати' час"]])],
             examples=[
                 ex("Сейча'с без че'тверти шесть.", "It is a quarter to six.", "без че'тверти шесть"),
                 ex("Сейча'с без двадцати' час.", "It is twenty to one.", "без двадцати' час"),
             ]),
        card("The 24-hour clock",
             "Timetables, television guides and announcements use the 24-hour clock. The hour and the minutes are read as "
             "ordinary numbers.",
             tables=[table(
                 ["Time", "Russian"],
                 [["08:00", "во'семь ноль-ноль"],
                  ["14:30", "четы'рнадцать три'дцать"],
                  ["21:55", "два'дцать оди'н пятьдеся'т пять"]])],
             examples=[
                 ex("По расписа'нию по'езд отправля'ется в четы'рнадцать три'дцать.", "According to the timetable the train leaves at fourteen thirty.", "четы'рнадцать три'дцать"),
             ]),
    ],
    verify=(vf("двадцать", "двадцати") + vf("десять", "десяти") + vf("пять", "пяти") + vf("девять", "девяти")
            + vf("четверть", "четверти") + vf("минута", "минуты", "минут") + vf("один", "одной") + vf("два", "двух")
            + vf("час", "час") + vf("одиннадцать", "одиннадцать") + vf("четырнадцать", "четырнадцать")
            + vf("тридцать", "тридцать") + vf("расписание", "расписанию") + vf("поезд", "поезд")
            + vf("отправляться", "отправляется") + vf("пятьдесят", "пятьдесят")),
    exercises=[
        F("2:40 — без ___ три. (twenty)", "двадцати'", ["два'дцать", "двадцатью'", "двадцато'й"], "Без + genitive.", "It is twenty to three.", lemma="двадцать"),
        F("7:45 — без ___ во'семь. (a quarter)", "че'тверти", ["че'тверть", "че'твертью", "че'твертям"], "Без + genitive.", "It is a quarter to eight.", lemma="четверть"),
        F("3:50 — без ___ четы'ре. (ten)", "десяти'", ["де'сять", "десятью'", "десято'й"], "Без + genitive.", "It is ten to four.", lemma="десять"),
        F("1:59 — без одно'й ___ два. (minute)", "мину'ты", ["мину'та", "мину'ту", "мину'т"], "Без одно'й + genitive singular.", "It is one minute to two.", lemma="минута"),
        F("9:58 — без двух ___ де'сять. (minutes)", "мину'т", ["мину'ты", "мину'та", "мину'ту"], "Без двух + genitive plural.", "It is two minutes to ten.", lemma="минута"),
        F("12:40 — без двадцати' ___. (one o'clock)", "час", ["часа'", "часо'в", "одного'"], "One o'clock is just час.", "It is twenty to one."),
        F("14:30 — четы'рнадцать ___. (thirty)", "три'дцать", ["тридцати'", "тридцатью'", "тридцато'й"], "24-hour clock: ordinary cardinal numbers.", "It is fourteen thirty."),
        mc("What time is ‘без десяти' оди'ннадцать’?", ["10:50", "11:10", "10:10", "11:50"], "10:50", "Ten minutes before eleven.", order=True),
        mc("7:35 is:", ["без двадцати' пяти' во'семь", "двадцать пять мину'т восьмо'го", "без пяти' во'семь", "полови'на восьмо'го"], "без двадцати' пяти' во'семь", "Twenty-five minutes missing before eight.", order=True),
        mc("From 31 to 59 minutes you count towards:", ["the next hour", "the previous hour", "the half hour", "midnight"], "the next hour", "Без + minutes + next hour.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 283
L283 = lesson(
    "At what time? Кото'рый час? В кото'ром часу'? Во ско'лько?",
    "— Во ско'лько нача'ло? — В полови'не седьмо'го.",
    requires=["час", "минута", "время", "половина", "утро"],
    cards=[
        card("Two different questions",
             "To ask what the time is now, use Кото'рый час? or Ско'лько вре'мени?. To ask when something happens, use В кото'ром "
             "часу'? or Во ско'лько?.",
             tables=[table(
                 ["Question", "Meaning"],
                 [["Кото'рый час?", "What time is it?"],
                  ["Ско'лько вре'мени?", "What time is it? (colloquial)"],
                  ["В кото'ром часу'?", "At what time?"],
                  ["Во ско'лько?", "At what time? (colloquial)"]])],
             examples=[
                 ex("Кото'рый сейча'с час?", "What time is it now?", "Кото'рый сейча'с час"),
                 ex("Во ско'лько начина'ется фильм?", "At what time does the film start?", "Во ско'лько"),
             ]),
        card("The preposition в",
             "For ‘at’ with the time: after 1–29 minutes, use в + accusative. For half past use в + prepositional. For the "
             "‘without’ forms use no preposition at all. The short пол- forms never change.",
             tables=[table(
                 ["Time", "At that time"],
                 [["7:05", "в пять мину'т восьмо'го"],
                  ["8:15", "в пятна'дцать мину'т девя'того"],
                  ["9:30", "в полови'не деся'того / в полдеся'того"],
                  ["7:35", "без двадцати' пяти' во'семь"],
                  ["8:45", "без пятна'дцати де'вять"]])],
             examples=[
                 ex("Мы пришли' домо'й в пять мину'т восьмо'го.", "We came home at five past seven.", "в пять мину'т восьмо'го"),
                 ex("Фильм начина'ется в полови'не седьмо'го.", "The film starts at half past six.", "в полови'не седьмо'го"),
                 ex("Авто'бус прихо'дит без пяти' де'сять.", "The bus arrives at five to ten.", "без пяти' де'сять"),
             ]),
        card("Putting it together",
             "A short conversation using both questions.",
             examples=[
                 ex("— Во ско'лько вы пришли' домо'й? — Без двадцати' пяти' де'вять.", "— What time did you get home? — At twenty-five to nine.", "Без двадцати' пяти' де'вять"),
                 ex("— Кото'рый час? — Полови'на деся'того.", "— What time is it? — Half past nine.", "Полови'на деся'того"),
             ]),
    ],
    verify=(vf("который", "который") + vf("сколько", "сколько") + vf("время", "времени") + vf("час", "часу") + vf("минута", "минут")
            + vf("восьмой", "восьмого") + vf("девятый", "девятого") + vf("десятый", "десятого") + vf("половина", "половине")
            + vf("фильм", "фильм") + vf("начинаться", "начинается") + vf("прийти", "пришли") + vf("домой", "домой")
            + vf("автобус", "автобус") + vf("приходить", "приходит") + vf("шестой", "седьмого".replace("седьмого", "шестого"))),
    exercises=[
        F("— ___ вы пришли' домо'й? — Без двадцати' пяти' де'вять. (At what time)", "Во ско'лько", ["Ско'лько", "Кото'рый", "Како'й"], "At what time? Во ско'лько?", "— What time did you get home? — At twenty-five to nine."),
        F("Фильм начина'ется ___ полови'не седьмо'го. (at)", "в", ["на", "к", "у"], "В + prepositional.", "The film starts at half past six."),
        F("Мы пришли' домо'й ___ пять мину'т восьмо'го. (at)", "в", ["на", "к", "без"], "В + accusative.", "We came home at five past seven."),
        F("По'езд отправля'ется ___ че'тверти шесть. (at a quarter to)", "без", ["в", "на", "по"], "No preposition: без itself.", "The train leaves at a quarter to six."),
        F("Фильм начина'ется в ___ восьмо'го. (half past)", "полови'не", ["полови'на", "полови'ну", "полови'ны"], "В + prepositional.", "The film starts at half past seven.", lemma="половина"),
        F("Мы встре'тились в ___. (at half past nine, short form)", "полдеся'того", ["полови'ну", "деся'тый", "де'сять"], "The short form does not change.", "We met at half past nine."),
        mc("Which question means ‘What time is it?’", ["Кото'рый час?", "В кото'ром часу'?", "Во ско'лько?", "Ско'лько часо'в?"], "Кото'рый час?", "Time now.", order=True),
        mc("How do you say ‘at 7:35’?", ["без двадцати' пяти' во'семь", "в без двадцати' пяти' во'семь", "в двадцать пять мину'т восьмо'го", "в полови'не восьмо'го"], "без двадцати' пяти' во'семь", "No в with без.", order=True),
        mc("How do you say ‘at 9:30’?", ["в полови'не деся'того", "в полови'ну деся'того", "в полови'на деся'того", "без полови'ны деся'того"], "в полови'не деся'того", "В + prepositional.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 284
L284 = lesson(
    "Word-building: -рух-, -выс-, под-, воз-/вос-, вз-/вс-",
    "Высота' зда'ния превыша'ет де'сять этаже'й.",
    requires=["высокий", "нарушение", "этаж", "возраст", "взрыв"],
    cards=[
        card("The roots -рух- and -выс-",
             "Roots carry meaning across many words. -Рух- is about collapse and destruction; -выс- is about height.",
             tables=[table(
                 ["Word", "English"],
                 [["ру'хнуть", "to collapse"],
                  ["разруша'ть / разру'шить", "to destroy"],
                  ["обру'шиваться / обру'шиться", "to strike; to collapse"],
                  ["наруше'ние", "violation, disruption"],
                  ["высота'", "height"],
                  ["превыша'ть / превы'сить", "to exceed"],
                  ["повыша'ть / повы'сить", "to raise, increase"],
                  ["повыше'ние", "increase, rise"]])],
             examples=[
                 ex("Высота' зда'ния превыша'ет де'сять этаже'й.", "The height of the building exceeds ten floors.", "превыша'ет"),
                 ex("Цены' повы'сились в сентябре'.", "Prices rose in September.", "повы'сились"),
             ]),
        card("The prefix под-",
             "Под- means ‘under’ or ‘from below’ in many words. It can also mean ‘secretly’ or ‘in addition’.",
             tables=[table(
                 ["Word", "English"],
                 [["поднима'ть / подня'ть", "to raise, lift"],
                  ["подде'ржка", "support"],
                  ["подста'вка", "a stand, a support"],
                  ["подслу'шивать", "to eavesdrop"],
                  ["подсма'тривать", "to peek, spy"],
                  ["подкупи'ть", "to bribe"],
                  ["подде'лать", "to forge"],
                  ["подрабо'тка", "extra work, a side job"]])],
             examples=[
                 ex("Он нашёл подрабо'тку на выходны'х.", "He found a side job for the weekends.", "подрабо'тку"),
                 ex("Не подслу'шивай чужи'е разгово'ры.", "Don't eavesdrop on other people's conversations.", "подслу'шивай"),
             ]),
        card("воз- / вос-, вз- / вс-",
             "Воз-/вос- often means ‘again’ or an abstract ‘up’. Вз-/вс- means ‘up’ in a physical sense.",
             tables=[table(
                 ["Word", "English"],
                 [["восстанови'ть", "to restore"],
                  ["возобнови'ть", "to resume"],
                  ["воспи'тывать", "to bring up (a child)"],
                  ["во'зраст", "age"],
                  ["взрыв", "explosion"],
                  ["взлёт", "takeoff"],
                  ["взро'слый", "adult"],
                  ["вспо'мнить", "to recall"]])],
             examples=[
                 ex("Магази'н возобнови'л рабо'ту по воскресе'ньям.", "The shop has resumed work on Sundays.", "возобнови'л"),
                 ex("Взро'слые и де'ти пришли' на пра'здник.", "Adults and children came to the party.", "Взро'слые"),
             ]),
    ],
    verify=(vf("рухнуть", "рухнуть") + vf("разрушать", "разрушать") + vf("разрушить", "разрушить") + vf("обрушиваться", "обрушиваться")
            + vf("нарушение", "нарушение") + vf("высота", "высота") + vf("превышать", "превышает") + vf("превысить", "превысила")
            + vf("повышать", "повышать") + vf("повышение", "повышение")
            + vf("поднимать", "поднимать") + vf("поддержка", "поддержка") + vf("подставка", "подставка")
            + vf("подслушивать", "подслушивай") + vf("подсматривать", "подсматривать") + vf("подкупить", "подкупить")
            + vf("подделать", "подделать") + vf("восстановить", "восстановить")
            + vf("возобновить", "возобновил") + vf("воспитывать", "воспитывать") + vf("возраст", "возраст")
            + vf("взрыв", "взрыв") + vf("взлёт", "взлёт") + vf("взрослый", "взрослые") + vf("вспомнить", "вспомнить")
            + vf("этаж", "этажей") + vf("здание", "здания") + vf("цена", "цены") + vf("сентябрь", "сентябре")
            + vf("магазин", "магазин") + vf("воскресенье", "воскресеньям") + vf("праздник", "праздник")
            + vf("найти", "нашёл") + vf("выходной", "выходных") + vf("разговор", "разговоры")
            + vf("чужой", "чужие")),
    exercises=[
        F("Магази'н ___ рабо'ту по воскресе'ньям. (resumed)", "возобнови'л", ["возобнови'ла", "возобнови'ло", "возобнови'ли"], "Masculine subject.", "The shop resumed work on Sundays."),
        F("Це'ны ___ в сентябре'. (rose)", "повы'сились", ["повы'силась", "повы'сился", "повы'силось"], "Plural subject.", "Prices rose in September."),
        F("Он ___ пра'вила. (violated)", "нару'шил", ["нару'шила", "нару'шило", "нару'шили"], "Masculine singular.", "He violated the rules.", lemma="нарушить"),
        F("Мы ___ ребёнка в большо'й семье'. (brought up)", "воспита'ли", ["воспита'л", "воспита'ла", "воспита'ть"], "Plural past.", "We brought up a child in a large family."),
        F("Высота' зда'ния ___ де'сять этаже'й. (exceeds)", "превыша'ет", ["превыша'ют", "превы'сил", "превыша'ть"], "Singular subject, present tense.", "The height of the building exceeds ten floors."),
        mc("What does ру'хнуть mean?", ["to collapse", "to run", "to rise", "to repair"], "to collapse", "Root -рух-.", order=True),
        mc("What does высота' mean?", ["height", "speed", "weight", "width"], "height", "Root -выс-.", order=True),
        mc("Which word means ‘adult’?", ["взро'слый", "во'зраст", "взлёт", "воспи'тание"], "взро'слый", "Взро'слый.", order=True),
        mc("What does подслу'шивать mean?", ["to eavesdrop", "to look up", "to support", "to forge"], "to eavesdrop", "Под- can mean ‘secretly’.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 285
L285 = lesson(
    "Review: weather, disasters, collective numerals, telling time",
    "Накану'не в полови'не седьмо'го в го'роде начался' ли'вень.",
    requires=["погода", "пожар", "спасти", "час", "минута"],
    cards=[
        card("Collective numerals and adverbs",
             "Collective numerals stand for groups of people or plural-only nouns and take the genitive plural. The adverbs "
             "вдвоём, втроём, вчетверо'м say that the group acts together.",
             tables=[table(
                 ["Use", "Example"],
                 [["with a noun", "тро'е тури'стов"],
                  ["without a noun", "Дво'е поги'бли."],
                  ["adverb", "Мы пошли' втроём."],
                  ["women only", "три сестры'"]])],
             examples=[
                 ex("Че'тверо тури'стов нашли'сь жи'вы.", "Four tourists were found alive.", "Че'тверо тури'стов"),
             ]),
        card("Telling time",
             "Minutes 1–29: minutes + the next hour in the genitive. Half: полови'на + hour. Minutes 31–59: без + minutes + "
             "the next hour. For ‘at’: в for the first two kinds, no preposition for без.",
             tables=[table(
                 ["Time", "Russian"],
                 [["5:10", "де'сять мину'т шесто'го"],
                  ["5:30", "полови'на шесто'го"],
                  ["5:50", "без десяти' шесть"],
                  ["at 5:10", "в де'сять мину'т шесто'го"],
                  ["at 5:50", "без десяти' шесть"]])],
             examples=[
                 ex("Накану'не в полови'не седьмо'го в го'роде начался' ли'вень.", "The day before, at half past six, a downpour began in the city.", "в полови'не седьмо'го"),
             ]),
    ],
    verify=(vf("турист", "туристов") + vf("живой", "живы") + vf("десять", "десять", "десяти")
            + vf("шестой", "шестого") + vf("шесть", "шесть") + vf("половина", "половина", "половине") + vf("седьмой", "седьмого")
            + vf("начаться", "начался") + vf("ливень", "ливень") + vf("сестра", "сестры")),
    exercises=[
        F("Дво'е ___ пострада'ли в пожа'ре. (residents)", "жи'телей", ["жи'тели", "жи'телям", "жи'телями"], "Collective numeral + genitive plural.", "Two residents were hurt in the fire.", lemma="житель"),
        F("Мы пошли' на конце'рт ___. (the three of us)", "втроём", ["тро'е", "трои'х", "три"], "Collective adverb.", "The three of us went to the concert."),
        F("5:10 — де'сять мину'т ___.", "шесто'го", ["шесто'й", "шесто'му", "шесть"], "Genitive ordinal.", "It is ten past five."),
        F("5:50 — без ___ шесть. (ten)", "десяти'", ["де'сять", "десятью'", "десято'й"], "Без + genitive.", "It is ten to six.", lemma="десять"),
        F("Фильм начина'ется в ___ шесто'го. (half)", "полови'не", ["полови'на", "полови'ну", "полови'ны"], "В + prepositional.", "The film starts at half past five.", lemma="половина"),
        F("Спаса'тели рабо'тают ___ су'тки. (around the clock)", "кру'глые", ["кру'глый", "кру'глых", "кру'глая"], "Plural noun су'тки.", "The rescuers work around the clock.", lemma="круглый"),
        F("Урага'н ___ на побере'жье. (struck)", "обру'шился", ["обру'шилась", "обру'шилось", "обру'шились"], "Masculine.", "The hurricane struck the coast."),
        mc("What time is ‘без двадцати' пяти' де'вять’?", ["8:35", "8:25", "9:25", "9:35"], "8:35", "Twenty-five minutes missing before nine.", order=True),
        mc("How do you say ‘at half past eight’?", ["в полови'не девя'того", "в полови'ну девя'того", "без полови'ны девя'того", "в де'вять мину'т"], "в полови'не девя'того", "Half of the ninth hour: в + prepositional.", order=True),
        mc("Which means ‘as a group of four’?", ["вчетверо'м", "че'тверо", "четве'ртый", "вчетверо"], "вчетверо'м", "Collective adverb.", order=True),
    ],
)

UNIT = unit("Unit 28: Weather, disasters, collective numerals and telling time",
            [L273, L274, L275, L276, L277, L278, L279, L280, L281, L282, L283, L284, L285])
