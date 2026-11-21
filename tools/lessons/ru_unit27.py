"""Unit 27: travel and food; short and long past passive participles, headlines;
numbers 1-30 in every case (textbook module 6, lesson 35)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 259
L259 = lesson(
    "Planning a trip: пое'здка, маршру'т, куро'рт, за грани'цу",
    "Мы плани'руем пое'здку на мо'ре.",
    requires=["поездка", "путешествие", "маршрут", "турист", "страна"],
    cards=[
        card("Travel words",
             "A basic vocabulary for planning a trip.",
             tables=[table(
                 ["Word", "English"],
                 [["пое'здка", "trip"],
                  ["путеше'ствие", "journey, travel"],
                  ["путеше'ственник", "traveler"],
                  ["тури'ст", "tourist"],
                  ["маршру'т", "route, itinerary"],
                  ["куро'рт", "resort"],
                  ["экску'рсия", "excursion"],
                  ["достопримеча'тельность (f.)", "sight, attraction"],
                  ["ви'за", "visa"],
                  ["страна'", "country"]])],
             examples=[
                 ex("Мы плани'руем пое'здку на мо'ре.", "We are planning a trip to the sea.", "пое'здку"),
                 ex("Како'й у вас маршру'т?", "What is your route?", "маршру'т"),
                 ex("Тури'сты осма'тривают достопримеча'тельности го'рода.", "The tourists are looking at the sights of the city.", "достопримеча'тельности"),
             ]),
        card("Verbs for travelling",
             "Many travel verbs are ones you already know.",
             tables=[table(
                 ["Verb", "English"],
                 [["путеше'ствовать", "to travel"],
                  ["отдыха'ть на куро'рте", "to relax at a resort"],
                  ["плани'ровать / заплани'ровать", "to plan"],
                  ["посеща'ть / посети'ть", "to visit (a place)"],
                  ["осма'тривать / осмотре'ть", "to look around, to see the sights"]])],
             examples=[
                 ex("Ле'том мы отдыха'ем на куро'рте.", "In summer we relax at a resort.", "на куро'рте"),
                 ex("Я люблю' путеше'ствовать по стране'.", "I like traveling around the country.", "путеше'ствовать"),
             ]),
        card("Abroad: за грани'цу, за грани'цей",
             "The word грани'ца also means ‘border’. ‘Abroad’ uses за + the word грани'ца in two cases: за грани'цу "
             "(where to?), за грани'цей (where?) and из-за грани'цы (where from?).",
             tables=[table(
                 ["Question", "Phrase"],
                 [["Куда'?", "за грани'цу"],
                  ["Где?", "за грани'цей"],
                  ["Отку'да?", "из-за грани'цы"]])],
             examples=[
                 ex("Они' е'дут за грани'цу.", "They are going abroad.", "за грани'цу"),
                 ex("Мой брат живёт за грани'цей.", "My brother lives abroad.", "за грани'цей"),
             ]),
    ],
    verify=(vf("поездка", "поездку") + vf("путешествие", "путешествие") + vf("путешественник", "путешественник")
            + vf("турист", "туристы") + vf("маршрут", "маршрут") + vf("курорт", "курорте")
            + vf("экскурсия", "экскурсия") + vf("достопримечательность", "достопримечательности")
            + vf("виза", "виза") + vf("страна", "стране") + vf("путешествовать", "путешествовать")
            + vf("отдыхать", "отдыхаем") + vf("осматривать", "осматривают") + vf("город", "города")
            + vf("планировать", "планируем") + vf("граница", "границу", "границей", "границы")
            + vf("брат", "брат") + vf("жить", "живёт") + vf("море", "море")),
    exercises=[
        F("Мы плани'руем ___ на мо'ре. (a trip)", "пое'здку", ["пое'здка", "пое'здки", "пое'здке"], "Accusative after плани'ровать.", "We are planning a trip to the sea.", lemma="поездка"),
        F("Тури'сты осма'тривают ___ го'рода. (the sights)", "достопримеча'тельности", ["достопримеча'тельность", "достопримеча'тельностью", "достопримеча'тельностей"], "Accusative plural of a feminine noun.", "The tourists are looking at the sights of the city.", lemma="достопримечательность"),
        F("Ле'том мы отдыха'ем на ___. (resort)", "куро'рте", ["куро'рт", "куро'рта", "куро'рту"], "Where? на + prepositional.", "In summer we relax at a resort.", lemma="курорт"),
        F("Они' е'дут ___ грани'цу. (abroad)", "за", ["из-за", "на", "в"], "Куда'? за грани'цу.", "They are going abroad."),
        F("Мой брат живёт за ___. (abroad)", "грани'цей", ["грани'цу", "грани'цы", "грани'це"], "Где? за грани'цей.", "My brother lives abroad.", lemma="граница"),
        F("Я люблю' ___ по стране'. (to travel)", "путеше'ствовать", ["путеше'ствие", "путеше'ственник", "путеше'ствует"], "After люблю': infinitive.", "I like traveling around the country.", lemma="путешествовать"),
        mc("Which word means ‘route, itinerary’?", ["маршру'т", "куро'рт", "экску'рсия", "ви'за"], "маршру'т", "Маршру'т = route.", order=True),
        mc("‘From abroad’ is:", ["из-за грани'цы", "за грани'цей", "за грани'цу", "на грани'цу"], "из-за грани'цы", "Where from? из-за грани'цы.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 260
L260 = lesson(
    "At the airport: рейс, биле'т, бага'ж, па'спорт, заде'ржка",
    "Наш рейс задержа'ли на два часа'.",
    requires=["билет", "самолёт", "пассажир", "аэропорт", "паспорт"],
    cards=[
        card("Words for flying",
             "A basic vocabulary for travelling by air.",
             tables=[table(
                 ["Word", "English"],
                 [["аэропо'рт", "airport"],
                  ["самолёт", "airplane"],
                  ["рейс", "flight"],
                  ["биле'т", "ticket"],
                  ["пассажи'р", "passenger"],
                  ["па'спорт", "passport"],
                  ["бага'ж", "luggage"],
                  ["регистра'ция", "check-in"],
                  ["поса'дка", "boarding"],
                  ["заде'ржка", "delay"],
                  ["переса'дка", "transfer, connection"]])],
             examples=[
                 ex("Покажи'те, пожа'луйста, биле'т и па'спорт.", "Please show your ticket and passport.", "биле'т и па'спорт"),
                 ex("Регистра'ция на рейс начина'ется в шесть часо'в.", "Check-in for the flight begins at six o'clock.", "Регистра'ция"),
             ]),
        card("Flight verbs",
             "Several verbs are used in the plural for ‘they’ (an impersonal ‘they’) when the subject is airline staff.",
             tables=[table(
                 ["Phrase", "English"],
                 [["лете'ть / полете'ть", "to fly"],
                  ["регистри'роваться / зарегистри'роваться", "to check in"],
                  ["опа'здывать / опозда'ть на рейс", "to be late for a flight"],
                  ["успева'ть / успе'ть на рейс", "to make it in time"],
                  ["задержа'ть / отмени'ть рейс", "to delay / cancel a flight"]])],
             examples=[
                 ex("Наш рейс задержа'ли на два часа'.", "Our flight was delayed by two hours.", "задержа'ли"),
                 ex("Рейс отмени'ли из-за тума'на.", "The flight was cancelled because of fog.", "отмени'ли"),
                 ex("Мы чуть не опозда'ли на рейс, но успе'ли.", "We almost missed the flight but made it.", "успе'ли"),
             ]),
        card("Customs and baggage",
             "At the border you pass through па'спортный контро'ль and тамо'жня (customs). You collect your luggage at "
             "the baggage claim: получи'ть бага'ж.",
             examples=[
                 ex("Мы получи'ли бага'ж и прошли' тамо'жню.", "We collected our luggage and went through customs.", "прошли' тамо'жню"),
             ]),
    ],
    verify=(vf("аэропорт", "аэропорт") + vf("самолёт", "самолёт") + vf("рейс", "рейс") + vf("билет", "билет")
            + vf("пассажир", "пассажир") + vf("паспорт", "паспорт") + vf("багаж", "багаж")
            + vf("задержка", "задержка") + vf("лететь", "лететь") + vf("опоздать", "опоздали")
            + vf("успеть", "успели") + vf("задержать", "задержали") + vf("отменить", "отменили")
            + vf("получить", "получили") + vf("пройти", "прошли") + vf("таможня", "таможню")
            + vf("туман", "тумана") + vf("час", "часа")),
    exercises=[
        F("Покажи'те, пожа'луйста, ___ и па'спорт. (ticket)", "биле'т", ["биле'та", "биле'ту", "биле'те"], "Accusative = nominative for inanimate.", "Please show your ticket and passport.", lemma="билет"),
        F("Наш ___ задержа'ли на два часа'. (flight)", "рейс", ["рейса", "рейсу", "рейсе"], "Accusative = nominative.", "Our flight was delayed by two hours.", lemma="рейс"),
        F("Рейс ___ из-за тума'на. (was cancelled)", "отмени'ли", ["отмени'ть", "отменя'ет", "отменя'л"], "Impersonal ‘they’: plural past.", "The flight was cancelled because of fog."),
        F("Мы чуть не ___ на рейс, но успе'ли. (nearly missed)", "опозда'ли", ["опозда'ть", "опа'здывают", "опозда'ю"], "Past plural.", "We almost missed the flight but made it."),
        F("Мы получи'ли ___ и прошли' тамо'жню. (the luggage)", "бага'ж", ["бага'жа", "бага'жу", "бага'же"], "Accusative = nominative.", "We collected our luggage and went through customs.", lemma="багаж"),
        F("Регистра'ция ___ рейс начина'ется в шесть часо'в. (for)", "на", ["в", "к", "у"], "Регистра'ция на рейс.", "Check-in for the flight begins at six."),
        mc("Which word means ‘boarding’?", ["поса'дка", "регистра'ция", "заде'ржка", "переса'дка"], "поса'дка", "Поса'дка = boarding.", order=True),
        mc("Which word means ‘passenger’?", ["пассажи'р", "тури'ст", "путеше'ственник", "курье'р"], "пассажи'р", "Пассажи'р.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 261
L261 = lesson(
    "At the hotel: гости'ница, но'мер, эта'ж, заброни'ровать",
    "Я хочу' заброни'ровать но'мер на три но'чи.",
    requires=["гостиница", "отель", "номер", "этаж", "завтрак"],
    cards=[
        card("Hotel words",
             "A basic vocabulary for booking and staying.",
             tables=[table(
                 ["Word", "English"],
                 [["гости'ница", "hotel"],
                  ["оте'ль (m.)", "hotel"],
                  ["но'мер", "room (in a hotel); number"],
                  ["эта'ж", "floor"],
                  ["за'втрак", "breakfast"],
                  ["ключ", "key"],
                  ["администра'тор", "receptionist, manager"],
                  ["одноме'стный / двухме'стный но'мер", "single / double room"],
                  ["вид на мо'ре", "sea view"]])],
             examples=[
                 ex("Я хочу' заброни'ровать но'мер на три но'чи.", "I want to book a room for three nights.", "заброни'ровать но'мер"),
                 ex("Наш но'мер на пя'том этаже'.", "Our room is on the fifth floor.", "на пя'том этаже'"),
                 ex("За'втрак вхо'дит в це'ну.", "Breakfast is included in the price.", "вхо'дит в це'ну"),
             ]),
        card("Booking and staying",
             "Useful verbs and phrases.",
             tables=[table(
                 ["Phrase", "English"],
                 [["брони'ровать / заброни'ровать", "to book"],
                  ["остана'вливаться / останови'ться в гости'нице", "to stay at a hotel"],
                  ["выезжа'ть / вы'ехать из но'мера", "to check out"],
                  ["Свобо'дные номера' есть?", "Are there any rooms available?"],
                  ["На ско'лько дней?", "For how many days?"]])],
             examples=[
                 ex("Мы останови'лись в небольшо'й гости'нице у мо'ря.", "We stayed at a small hotel by the sea.", "останови'лись"),
                 ex("Ско'лько сто'ит но'мер на одного'?", "How much is a single room?", "но'мер на одного'"),
             ]),
        card("Asking at reception",
             "A few short phrases for the front desk.",
             examples=[
                 ex("Подскажи'те, пожа'луйста, где ле'стница?", "Could you tell me where the stairs are?", "Подскажи'те"),
                 ex("В како'м часу' за'втрак?", "At what time is breakfast?", "за'втрак"),
             ]),
    ],
    verify=(vf("гостиница", "гостиница", "гостинице") + vf("отель", "отель") + vf("номер", "номер", "номера")
            + vf("этаж", "этаже") + vf("завтрак", "завтрак") + vf("ключ", "ключ") + vf("администратор", "администратор")
            + vf("бронировать", "бронировать") + vf("забронировать", "забронировать") + vf("останавливаться", "останавливаться")
            + vf("остановиться", "остановились") + vf("входить", "входит") + vf("цена", "цену")
            + vf("море", "моря") + vf("стоить", "стоит") + vf("пятый", "пятом") + vf("ночь", "ночи")
            + vf("лестница", "лестница") + vf("подсказать", "подскажите")),
    exercises=[
        F("Я хочу' заброни'ровать ___ на три но'чи. (a room)", "но'мер", ["но'мера", "но'меру", "но'мере"], "Accusative = nominative.", "I want to book a room for three nights.", lemma="номер"),
        F("Наш но'мер на пя'том ___. (floor)", "этаже'", ["эта'ж", "этажа'", "этажу'"], "Where? на + prepositional.", "Our room is on the fifth floor.", lemma="этаж"),
        F("___ вхо'дит в це'ну. (breakfast)", "За'втрак", ["За'втрака", "За'втраку", "За'втраке"], "Nominative subject.", "Breakfast is included in the price.", lemma="завтрак"),
        F("Мы останови'лись ___ небольшо'й гости'нице. (in)", "в", ["на", "к", "о"], "Остановиться в гостинице.", "We stayed at a small hotel."),
        F("Ско'лько сто'ит но'мер на ___? (one person)", "одного'", ["оди'н", "одна'", "одно'м"], "На + accusative, masculine animate: одного'.", "How much is a single room?"),
        F("Свобо'дные номера' ___? (are there)", "есть", ["быть", "был", "бу'дет"], "Есть = there is/are.", "Are there any rooms available?"),
        mc("Which word means ‘floor (of a building)’?", ["эта'ж", "но'мер", "ключ", "за'втрак"], "эта'ж", "Эта'ж.", order=True),
        mc("‘To stay at a hotel’ is:", ["останови'ться в гости'нице", "заброни'ровать гости'ницу", "вы'ехать из гости'ницы", "войти' в гости'ницу"], "останови'ться в гости'нице", "Останови'ться.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 262
L262 = lesson(
    "Meat, rice, soup: food and dishes",
    "Что вы предпочита'ете: говя'дину, свини'ну и'ли ку'рицу?",
    requires=["мясо", "курица", "кухня", "блюдо", "рис"],
    cards=[
        card("Meat and main dishes",
             "Words for the main part of a meal.",
             tables=[table(
                 ["Word", "English"],
                 [["мя'со", "meat"],
                  ["говя'дина", "beef"],
                  ["свини'на", "pork"],
                  ["бара'нина", "lamb, mutton"],
                  ["ку'рица", "chicken"],
                  ["ры'ба", "fish"],
                  ["рис", "rice"],
                  ["карто'шка", "potatoes"],
                  ["о'вощи (pl.)", "vegetables"],
                  ["суп", "soup"],
                  ["борщ", "borscht"],
                  ["блю'до", "dish"],
                  ["ку'хня", "cuisine; kitchen"]])],
             examples=[
                 ex("Я не ем мя'со.", "I do not eat meat.", "мя'со"),
                 ex("На обе'д был рис с ку'рицей.", "Lunch was rice with chicken.", "рис с ку'рицей"),
                 ex("Что вы предпочита'ете: говя'дину, свини'ну и'ли ку'рицу?", "What do you prefer: beef, pork or chicken?", "говя'дину"),
             ]),
        card("How it is cooked",
             "The adjectives for cooked food are past passive participles. You can learn them as ordinary adjectives.",
             tables=[table(
                 ["Adjective", "English"],
                 [["жа'реный", "fried, roasted"],
                  ["варёный", "boiled"],
                  ["печёный", "baked"],
                  ["копчёный", "smoked"],
                  ["све'жий", "fresh"],
                  ["о'стрый", "spicy"]])],
             examples=[
                 ex("Жа'реная ку'рица с ри'сом — моё люби'мое блю'до.", "Fried chicken with rice is my favorite dish.", "Жа'реная"),
                 ex("Дай мне варёную карто'шку.", "Give me some boiled potatoes.", "варёную"),
             ]),
        card("Cuisine",
             "Ку'хня means the cooking of a country. It also means ‘kitchen’.",
             examples=[
                 ex("Мне нра'вится ру'сская ку'хня.", "I like Russian cuisine.", "ку'хня"),
                 ex("В э'том рестора'не гото'вят блю'да грузи'нской ку'хни.", "This restaurant cooks Georgian dishes.", "ку'хни"),
             ]),
    ],
    verify=(vf("мясо", "мясо") + vf("говядина", "говядину") + vf("свинина", "свинину") + vf("баранина", "баранина")
            + vf("курица", "курицу", "курицей") + vf("рыба", "рыба") + vf("рис", "рис", "рисом") + vf("картошка", "картошка")
            + vf("овощ", "овощи") + vf("суп", "суп") + vf("борщ", "борщ") + vf("блюдо", "блюдо", "блюда")
            + vf("кухня", "кухня", "кухни") + vf("жареный", "жареный", "жареная") + vf("варёный", "варёный", "варёную")
            + vf("печёный", "печёный") + vf("копчёный", "копчёный") + vf("свежий", "свежий") + vf("острый", "острый")
            + vf("есть", "ем") + vf("предпочитать", "предпочитаете") + vf("обед", "обед")),
    exercises=[
        F("Я не ем ___. (meat)", "мя'со", ["мя'са", "мя'су", "мя'се"], "После не ем: accusative (or genitive); here: neuter accusative.", "I do not eat meat.", lemma="мясо"),
        F("На обе'д был рис с ___. (chicken, instr.)", "ку'рицей", ["ку'рица", "ку'рицу", "ку'рицы"], "С + instrumental.", "Lunch was rice with chicken.", lemma="курица"),
        F("Жа'реная ___ с ри'сом — моё люби'мое блю'до. (chicken)", "ку'рица", ["ку'рицу", "ку'рицей", "ку'рицы"], "Nominative subject.", "Fried chicken with rice is my favorite dish.", lemma="курица"),
        F("Дай мне ___ карто'шку. (boiled)", "варёную", ["варёный", "варёная", "варёное"], "Accusative feminine: -ую.", "Give me some boiled potatoes."),
        F("Мне нра'вится ру'сская ___. (cuisine)", "ку'хня", ["ку'хню", "ку'хни", "ку'хне"], "Нра'виться + nominative subject.", "I like Russian cuisine.", lemma="кухня"),
        F("Что вы предпочита'ете: ___, свини'ну и'ли ку'рицу? (beef)", "говя'дину", ["говя'дина", "говя'дины", "говя'дине"], "Accusative.", "What do you prefer: beef, pork or chicken?", lemma="говядина"),
        mc("Which word means ‘lamb’?", ["бара'нина", "свини'на", "говя'дина", "ку'рица"], "бара'нина", "Бара'нина = lamb.", order=True),
        mc("What does варёный mean?", ["boiled", "fried", "baked", "smoked"], "boiled", "Варёный = boiled."),
    ],
)

# ---------------------------------------------------------------------------- 263
L263 = lesson(
    "In a restaurant: меню', официа'нт, счёт, чаевы'е",
    "Принеси'те, пожа'луйста, счёт.",
    requires=["ресторан", "меню", "заказать", "счёт", "обслуживание"],
    cards=[
        card("Words at the table",
             "A basic vocabulary for eating out.",
             tables=[table(
                 ["Word", "English"],
                 [["рестора'н", "restaurant"],
                  ["кафе'", "café"],
                  ["сто'лик", "small table, reservation"],
                  ["меню'", "menu"],
                  ["официа'нт", "waiter"],
                  ["заказа'ть", "to order"],
                  ["счёт", "bill"],
                  ["чаевы'е (pl.)", "tip"],
                  ["обслу'живание", "service"]])],
             examples=[
                 ex("Мы заказа'ли сто'лик на четырёх.", "We reserved a table for four.", "сто'лик"),
                 ex("Принеси'те, пожа'луйста, счёт.", "Please bring the bill.", "счёт"),
                 ex("Обслу'живание здесь о'чень хоро'шее.", "The service here is very good.", "Обслу'живание"),
             ]),
        card("Ordering",
             "Polite ways to order and to pay.",
             tables=[table(
                 ["Phrase", "English"],
                 [["Мне, пожа'луйста, суп.", "I'll have soup, please."],
                  ["Мы бы хоте'ли заказа'ть.", "We would like to order."],
                  ["Прия'тного аппети'та!", "Enjoy your meal!"],
                  ["Мо'жно счёт?", "Can I have the bill?"],
                  ["Оста'вить чаевы'е", "to leave a tip"]])],
             examples=[
                 ex("Мы бы хоте'ли заказа'ть суп и сала'т.", "We would like to order soup and a salad.", "заказа'ть"),
                 ex("Официа'нту ну'жно оста'вить чаевы'е.", "You should leave the waiter a tip.", "чаевы'е"),
             ]),
        card("Good and bad service",
             "Opinions about a restaurant:",
             tables=[table(
                 ["Phrase", "English"],
                 [["Всё бы'ло вку'сно.", "Everything was tasty."],
                  ["Обслу'живание бы'ло ме'дленное.", "The service was slow."],
                  ["Бы'строе обслу'живание", "fast service"]])],
             examples=[
                 ex("Всё бы'ло вку'сно, а обслу'живание бы'строе.", "Everything was tasty, and the service was fast.", "вку'сно"),
             ]),
    ],
    verify=(vf("ресторан", "ресторане") + vf("столик", "столик") + vf("меню", "меню") + vf("официант", "официанту")
            + vf("заказать", "заказали", "заказать") + vf("счёт", "счёт") + vf("чаевые", "чаевые")
            + vf("обслуживание", "обслуживание") + vf("принести", "принесите") + vf("суп", "суп")
            + vf("салат", "салат") + vf("оставить", "оставить") + vf("быстрый", "быстрое") + vf("медленный", "медленное")
            + vf("вкусно", "вкусно") + vf("хотеть", "хотели")),
    exercises=[
        F("Принеси'те, пожа'луйста, ___. (the bill)", "счёт", ["счёта", "счёту", "счёте"], "Accusative = nominative.", "Please bring the bill.", lemma="счёт"),
        F("Мы ___ сто'лик на четырёх. (reserved)", "заказа'ли", ["заказа'ть", "зака'зывают", "заказа'л"], "Past plural.", "We reserved a table for four."),
        F("Официа'нту ну'жно оста'вить ___. (a tip)", "чаевы'е", ["чаевы'х", "чаевы'м", "чаевы'ми"], "Plural-only noun in the accusative.", "You should leave the waiter a tip.", lemma="чаевые"),
        F("___ здесь о'чень хоро'шее. (service)", "Обслу'живание", ["Обслу'живания", "Обслу'живанию", "Обслу'живании"], "Nominative subject.", "The service here is very good.", lemma="обслуживание"),
        F("Мы бы хоте'ли ___ суп и сала'т. (order)", "заказа'ть", ["заказа'ли", "зака'зывают", "заказа'л"], "After хоте'ли: infinitive.", "We would like to order soup and a salad."),
        F("Мне, пожа'луйста, ___. (soup)", "суп", ["супа", "супу", "супе"], "Accusative = nominative.", "I'll have soup, please.", lemma="суп"),
        mc("Which word means ‘waiter’?", ["официа'нт", "курье'р", "тури'ст", "администра'тор"], "официа'нт", "Официа'нт = waiter.", order=True),
        mc("What do you say before eating?", ["Прия'тного аппети'та!", "До свидания!", "Спаси'бо за обе'д.", "Как дела'?"], "Прия'тного аппети'та!", "A wish before the meal."),
    ],
)

# ---------------------------------------------------------------------------- 264
L264 = lesson(
    "Short past passive: закры'то, сде'лано, переведён",
    "Магази'н закры'т. Дверь закры'та. Окно' закры'то.",
    requires=["закрыть", "открыть", "сделать", "решить", "забыть"],
    cards=[
        card("Making the short form",
             "A past passive participle also has a short form, used in the nominative only and always connected to "
             "the verb быть. To make it, drop the long ending. For -тый participles, drop -ый. For -нный, drop the "
             "ending and one н. For -ённый, drop the ending and one н; the stress moves to the last syllable.",
             tables=[table(
                 ["Long form", "Masc.", "Fem.", "Neut.", "Plural"],
                 [["закры'тый", "закры'т", "закры'та", "закры'то", "закры'ты"],
                  ["откры'тый", "откры'т", "откры'та", "откры'то", "откры'ты"],
                  ["сде'ланный", "сде'лан", "сде'лана", "сде'лано", "сде'ланы"],
                  ["переведённый", "переведён", "переведена'", "переведено'", "переведены'"]])],
             examples=[
                 ex("Магази'н закры'т. Дверь закры'та. Окно' закры'то.", "The shop is closed. The door is closed. The window is closed.", "закры'т"),
                 ex("Вопро'с уже' решён.", "The question has already been settled.", "решён"),
             ]),
        card("They agree with the noun",
             "The short form agrees with its noun in gender and number. It has no cases: it is always the predicate (‘the door is closed’), "
             "never a description (‘the closed door’).",
             tables=[table(
                 ["Noun", "Short form"],
                 [["магази'н", "закры'т"],
                  ["дверь", "закры'та"],
                  ["окно'", "закры'то"],
                  ["две'ри", "закры'ты"]])],
             examples=[
                 ex("Музе'й откры'т с десяти' до шести'.", "The museum is open from ten till six.", "откры'т"),
                 ex("Всё сде'лано.", "Everything is done.", "сде'лано"),
             ]),
        card("Past and future",
             "Present tense uses no verb: Дверь закры'та. Past tense adds была': Дверь была' закры'та. Future adds бу'дет: "
             "Дверь бу'дет закры'та.",
             tables=[table(
                 ["Tense", "Example"],
                 [["present", "Дверь закры'та."],
                  ["past", "Дверь была' закры'та."],
                  ["future", "Дверь бу'дет закры'та."]])],
             examples=[
                 ex("Дверь была' закры'та, когда' мы пришли'.", "The door was closed when we arrived.", "была' закры'та"),
                 ex("Вопро'с бу'дет решён за'втра.", "The question will be settled tomorrow.", "бу'дет решён"),
             ]),
    ],
    verify=(vf("закрытый", "закрыт", "закрыта", "закрыто", "закрыты") + vf("открытый", "открыт", "открыта", "открыто", "открыты")
            + vf("решённый", "решён") + vf("вопрос", "вопрос") + vf("магазин", "магазин") + vf("дверь", "дверь")
            + vf("окно", "окно") + vf("музей", "музей") + vf("всё", "всё") + vf("быть", "была", "будет")
            + vf("прийти", "пришли") + vf("завтра", "завтра")),
    exercises=[
        F("Магази'н ___. (closed, masc.)", "закры'т", ["закры'та", "закры'то", "закры'ты"], "Masculine: no ending.", "The shop is closed.", lemma="закрытый"),
        F("Дверь ___. (closed, fem.)", "закры'та", ["закры'т", "закры'то", "закры'ты"], "Feminine: -а.", "The door is closed.", lemma="закрытый"),
        F("Окно' ___. (closed, neut.)", "закры'то", ["закры'т", "закры'та", "закры'ты"], "Neuter: -о.", "The window is closed.", lemma="закрытый"),
        F("Музе'й ___ с десяти' до шести'. (open)", "откры'т", ["откры'та", "откры'то", "откры'ты"], "Masculine: музей.", "The museum is open from ten till six.", lemma="открытый"),
        F("Вопро'с уже' ___. (settled)", "решён", ["решена'", "решено'", "решены'"], "Masculine -ённый → -ён.", "The question has already been settled."),
        F("Дверь ___ закры'та, когда' мы пришли'. (was)", "была'", ["был", "бы'ло", "бу'дет"], "Past, feminine.", "The door was closed when we arrived."),
        F("Вопро'с ___ решён за'втра. (will be)", "бу'дет", ["была'", "был", "есть"], "Future.", "The question will be settled tomorrow."),
        mc("Which form is the short form of сде'ланный (neuter)?", ["сде'лано", "сде'лана", "сде'лан", "сде'ланное"], "сде'лано", "Neuter: -о.", order=True),
        mc("Which case does a short participle use?", ["only the nominative", "all cases", "only the genitive", "only the accusative"], "only the nominative", "It is only a predicate.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 265
L265 = lesson(
    "Long or short? Describes the noun, or states the result",
    "Посы'лка, отпра'вленная вчера', пришла' сего'дня. Посы'лка была' отпра'влена вчера'.",
    requires=["отправить", "получить", "купить", "доставить", "создать"],
    cards=[
        card("Two jobs, two forms",
             "A long form describes the noun and can replace кото'рый + a verb. A short form states that something has "
             "been done and is always linked with быть. The short form with its noun is a full sentence; the long form "
             "is not.",
             tables=[table(
                 ["Form", "Role", "Example"],
                 [["long", "explains the noun (= кото'рый + verb)", "Посы'лка, отпра'вленная вчера', пришла'."],
                  ["short", "states what was done", "Посы'лка была' отпра'влена вчера'."]])],
             examples=[
                 ex("Посы'лка, отпра'вленная вчера', пришла' сего'дня.", "The parcel sent yesterday arrived today.", "отпра'вленная"),
                 ex("Посы'лка была' отпра'влена вчера'.", "The parcel was sent yesterday.", "отпра'влена"),
             ]),
        card("A quick test",
             "Try to replace the participle with кото'рый + a verb. If it works, use the long form. If the participle "
             "is the main information and the sentence would not be complete without it, use the short form.",
             tables=[table(
                 ["Sentence", "Test", "Form"],
                 [["Письмо', получе'нное вчера', у меня'.", "= письмо', кото'рое я получи'л вчера'", "long"],
                  ["Письмо' получено' вчера'.", "the whole sentence says it was received", "short"]])],
             examples=[
                 ex("Дом, со'зданный архите'ктором, стои'т у мо'ря.", "The house created by the architect stands by the sea.", "со'зданный"),
                 ex("Дом со'здан архите'ктором.", "The house was created by an architect.", "со'здан"),
             ]),
        card("English translations",
             "The short form is often translated by ‘has been’ or ‘was’. The long form is translated by ‘that’, ‘which’ or "
             "an English participle phrase.",
             examples=[
                 ex("Биле'ты уже' ку'плены.", "The tickets have already been bought.", "ку'плены"),
                 ex("Биле'ты, ку'пленные вчера', лежа'т на столе'.", "The tickets bought yesterday are lying on the table.", "ку'пленные"),
             ]),
    ],
    verify=(vf("отправить", "отправил") + vf("посылка", "посылка") + vf("доставить", "доставил")
            + vf("получить", "получил") + vf("купить", "купил") + vf("создать", "создал")
            + vf("архитектор", "архитектором") + vf("дом", "дом") + vf("море", "моря") + vf("билет", "билеты")
            + vf("лежать", "лежат") + vf("стол", "столе") + vf("сегодня", "сегодня") + vf("вчера", "вчера")),
    exercises=[
        F("Посы'лка, ___ вчера', пришла' сего'дня. (sent)", "отпра'вленная", ["отпра'влена", "отпра'вили", "отпра'вить"], "Describes the noun: long form.", "The parcel sent yesterday arrived today."),
        F("Посы'лка была' ___ вчера'. (sent)", "отпра'влена", ["отпра'вленная", "отпра'вленную", "отпра'вленной"], "States the action: short form.", "The parcel was sent yesterday."),
        F("Биле'ты уже' ___. (bought)", "ку'плены", ["ку'пленные", "ку'пленных", "ку'пленными"], "Short form after the noun.", "The tickets have already been bought."),
        F("Биле'ты, ___ вчера', лежа'т на столе'. (bought)", "ку'пленные", ["ку'плены", "ку'плен", "ку'плено"], "A phrase describing the tickets: long form.", "The tickets bought yesterday are lying on the table."),
        F("Дом ___ архите'ктором. (was created)", "со'здан", ["со'зданный", "со'зданная", "со'зданное"], "Predicate, masculine.", "The house was created by an architect."),
        F("Дом, ___ архите'ктором, стои'т у мо'ря. (created)", "со'зданный", ["со'здан", "со'здана", "со'здано"], "Describes the house.", "The house created by the architect stands by the sea."),
        mc("A long participle can replace:", ["кото'рый + a verb", "быть + an adjective", "a noun", "an infinitive"], "кото'рый + a verb", "Explanatory.", order=True),
        mc("A short participle is always linked with:", ["быть", "кото'рый", "что'бы", "ли"], "быть", "Present is understood; past uses была', future бу'дет.", order=True),
    ],
)


# ---------------------------------------------------------------------------- 266
L266 = lesson(
    "Headlines: Закры'т аэропо'рт, Постро'ена шко'ла",
    "Закры'т аэропо'рт из-за снегопа'да.",
    requires=["объявить", "установить", "принять", "найти", "построить"],
    cards=[
        card("Short participles without быть",
             "News headlines use short past participles and drop the verb быть. The participle usually comes first and "
             "agrees in gender and number with the noun that follows. It has the sense ‘has been done’.",
             tables=[table(
                 ["Headline", "English"],
                 [["Закры'т аэропо'рт из-за снегопа'да", "The airport is closed because of snowfall"],
                  ["Откры'т но'вый маршру'т до куро'рта", "A new route to the resort has been opened"],
                  ["Постро'ена но'вая шко'ла", "A new school has been built"],
                  ["При'нято реше'ние откры'ть музе'й", "A decision to open a museum has been taken"],
                  ["Устано'влен но'вый реко'рд", "A new record has been set"],
                  ["Объя'влен ко'нкурс", "A competition has been announced"]])],
             examples=[
                 ex("Закры'т аэропо'рт из-за снегопа'да.", "The airport is closed because of snowfall.", "Закры'т"),
                 ex("Постро'ена но'вая шко'ла.", "A new school has been built.", "Постро'ена"),
                 ex("При'нято реше'ние откры'ть музе'й.", "A decision to open a museum has been taken.", "При'нято"),
             ]),
        card("Which ending?",
             "Choose the ending to match the noun, as in a normal short participle. Masculine: no ending. Feminine: -а. "
             "Neuter: -о. Plural: -ы.",
             tables=[table(
                 ["Noun", "Headline"],
                 [["аэропо'рт (m.)", "Закры'т аэропо'рт"],
                  ["шко'ла (f.)", "Постро'ена шко'ла"],
                  ["реше'ние (n.)", "При'нято реше'ние"],
                  ["магази'ны (pl.)", "Откры'ты магази'ны"]])],
             examples=[
                 ex("Откры'ты но'вые магази'ны.", "New shops have opened.", "Откры'ты"),
                 ex("На'йден тури'ст, кото'рый пропа'л в гора'х.", "The tourist who went missing in the mountains has been found.", "На'йден"),
             ]),
        card("Same thing, different style",
             "In normal speech you would write the sentence with the verb: Аэропо'рт закры'т. A headline is a compressed "
             "form of this: the participle is moved forward and the noun follows.",
             examples=[
                 ex("Аэропо'рт закры'т.", "The airport is closed.", "закры'т"),
                 ex("Объя'влен ко'нкурс на лу'чшую фотогра'фию.", "A competition for the best photograph has been announced.", "Объя'влен"),
             ]),
    ],
    verify=(vf("аэропорт", "аэропорт") + vf("снегопад", "снегопада") + vf("маршрут", "маршрут") + vf("курорт", "курорта")
            + vf("школа", "школа") + vf("решение", "решение") + vf("музей", "музей") + vf("рекорд", "рекорд")
            + vf("конкурс", "конкурс") + vf("магазин", "магазины") + vf("турист", "турист") + vf("пропасть", "пропал")
            + vf("гора", "горах") + vf("лучший", "лучшую") + vf("фотография", "фотографию")),
    exercises=[
        F("___ аэропо'рт из-за снегопа'да. (closed)", "Закры'т", ["Закры'та", "Закры'то", "Закры'ты"], "Аэропо'рт is masculine.", "The airport is closed because of snowfall."),
        F("___ но'вая шко'ла. (built)", "Постро'ена", ["Постро'ен", "Постро'ено", "Постро'ены"], "Шко'ла is feminine.", "A new school has been built."),
        F("___ реше'ние откры'ть музе'й. (taken)", "При'нято", ["При'нят", "При'нята", "При'няты"], "Реше'ние is neuter.", "A decision to open a museum has been taken."),
        F("___ но'вые магази'ны. (opened)", "Откры'ты", ["Откры'т", "Откры'та", "Откры'то"], "Plural: -ы.", "New shops have opened."),
        F("___ но'вый реко'рд. (set)", "Устано'влен", ["Устано'влена", "Устано'влено", "Устано'влены"], "Реко'рд is masculine.", "A new record has been set."),
        F("Объя'влен ___. (a competition)", "ко'нкурс", ["ко'нкурса", "ко'нкурсу", "ко'нкурсе"], "The noun is the subject, so nominative.", "A competition has been announced.", lemma="конкурс"),
        mc("How do headlines usually express ‘has been closed’?", ["a short participle without быть", "a long participle with был", "an infinitive", "кото'рый + a verb"], "a short participle without быть", "Short participle, быть dropped.", order=True),
        mc("Why is найден masculine in ‘На'йден тури'ст’?", ["because тури'ст is masculine", "because it is past tense", "because headlines are always masculine", "because it ends in -ен"], "because тури'ст is masculine", "Agrees with the noun.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 267
L267 = lesson(
    "Number + adjective + noun: оди'н но'вый дом, два но'вых до'ма, пять но'вых домо'в",
    "Мы ви'дели два больши'х па'рка.",
    requires=["число", "количество", "новый", "большой", "старый"],
    cards=[
        card("Three groups, three patterns",
             "The noun follows the usual rule: 1 takes the nominative singular, 2–4 take the genitive singular, 5+ "
             "take the genitive plural. The adjective follows the noun.",
             tables=[table(
                 ["Number", "Adjective + noun", "Example"],
                 [["1", "agrees with the noun", "оди'н но'вый дом"],
                  ["2, 3, 4", "gen. pl. adjective + gen. sg. noun", "два но'вых {до'ма}"],
                  ["5 and more", "gen. pl. adjective + gen. pl. noun", "пять но'вых {домо'в}"]])],
             examples=[
                 ex("У нас оди'н большо'й стол.", "We have one big table.", "оди'н большо'й стол"),
                 ex("Мы ви'дели два больши'х па'рка.", "We saw two big parks.", "больши'х па'рка"),
                 ex("На столе' лежа'т пять ста'рых книг.", "Five old books are lying on the table.", "пять ста'рых книг"),
             ]),
        card("Feminine nouns and 2–4",
             "With feminine nouns the adjective may be in the nominative plural or in the genitive plural. The genitive "
             "plural is always safe. With masculine and neuter nouns use the genitive plural only.",
             tables=[table(
                 ["Gender", "Allowed", "Not allowed"],
                 [["masculine", "три но'вых до'ма", "три но'вые до'ма"],
                  ["neuter", "четы'ре но'вых окна'", "четы'ре но'вые окна'"],
                  ["feminine", "три но'вых / но'вые маши'ны", "—"]])],
             examples=[
                 ex("Я купи'л четы'ре но'вых окна'.", "I bought four new windows.", "четы'ре но'вых окна'"),
                 ex("На у'лице стоя'т три но'вые маши'ны.", "Three new cars are standing in the street.", "три но'вые маши'ны"),
             ]),
        card("The last digit decides, and о'ба / о'бе",
             "With large numbers the last word decides the pattern. О'ба (both) and о'бе (both, f.) follow the 2–4 pattern.",
             tables=[table(
                 ["Number", "Phrase"],
                 [["два'дцать оди'н", "италья'нский рестора'н"],
                  ["два'дцать четы'ре", "италья'нских рестора'на"],
                  ["два'дцать во'семь", "италья'нских рестора'нов"]])],
             examples=[
                 ex("О'ба мои'х бра'та у'чатся в институ'те.", "Both my brothers study at an institute.", "О'ба мои'х бра'та"),
                 ex("О'бе на'ши до'чери рабо'тают в больни'це.", "Both our daughters work at a hospital.", "О'бе на'ши до'чери"),
             ]),
    ],
    verify=(vf("дом", "дом", "дома", "домов") + vf("новый", "новых", "новые") + vf("большой", "большой", "больших")
            + vf("старый", "старых") + vf("парк", "парка") + vf("книга", "книг") + vf("окно", "окна")
            + vf("машина", "машины") + vf("итальянский", "итальянский", "итальянских") + vf("ресторан", "ресторан", "ресторана", "ресторанов")
            + vf("двадцать", "двадцать") + vf("брат", "брата") + vf("дочь", "дочери") + vf("институт", "институте")
            + vf("больница", "больнице") + vf("работать", "работают") + vf("видеть", "видели")
            + vf("лежать", "лежат") + vf("стоять", "стоят")),
    exercises=[
        F("У нас оди'н ___ стол. (big)", "большо'й", ["больши'х", "больша'я", "большо'го"], "1 → agrees with the noun.", "We have one big table."),
        F("Мы ви'дели два ___ па'рка. (big)", "больши'х", ["большо'й", "больши'е", "большо'го"], "2–4 + masculine noun: genitive plural.", "We saw two big parks."),
        F("Я купи'л четы'ре ___ окна'. (new)", "но'вых", ["но'вые", "но'вый", "но'вого"], "Neuter: genitive plural only.", "I bought four new windows."),
        F("На столе' лежа'т пять ___ книг. (old)", "ста'рых", ["ста'рые", "ста'рая", "ста'рой"], "5+: genitive plural.", "Five old books are lying on the table."),
        F("В Москве' есть два'дцать оди'н ___ рестора'н. (Italian)", "италья'нский", ["италья'нских", "италья'нские", "италья'нского"], "21 → ends in 1: nominative singular.", "There are 21 Italian restaurants in Moscow."),
        F("В Москве' есть два'дцать четы'ре италья'нских ___. (restaurants)", "рестора'на", ["рестора'нов", "рестора'ны", "рестора'н"], "24 → ends in 4: genitive singular.", "There are 24 Italian restaurants in Moscow.", lemma="ресторан"),
        F("В Москве' есть два'дцать во'семь италья'нских ___. (restaurants)", "рестора'нов", ["рестора'на", "рестора'ны", "рестора'н"], "28 → ends in 8: genitive plural.", "There are 28 Italian restaurants in Moscow.", lemma="ресторан"),
        F("О'ба мои'х ___ у'чатся в институ'те. (brothers)", "бра'та", ["бра'тья", "бра'тьев", "бра'ту"], "О'ба follows 2–4: genitive singular.", "Both my brothers study at an institute.", lemma="брат"),
        mc("Which phrase is correct?", ["три но'вых до'ма", "три но'вые до'ма", "три но'вый до'ма", "три но'вого до'ма"], "три но'вых до'ма", "Masculine: genitive plural adjective.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 268
L268 = lesson(
    "Declension of оди'н: одного', одному', одни'м, об одно'м",
    "Мы чита'ли об одно'м изве'стном писа'теле.",
    requires=["число", "количество", "новый", "большой", "старый"],
    cards=[
        card("Оди'н is an adjective",
             "The number 1 agrees with its noun in gender, number and case. Its endings are those of э'тот.",
             tables=[table(
                 ["Case", "Masc.", "Fem.", "Neut.", "Plural"],
                 [["Nom.", "оди'н", "одн{а'}", "одн{о'}", "одн{и'}"],
                  ["Gen.", "одн{ого'}", "одн{о'й}", "одн{ого'}", "одн{и'х}"],
                  ["Dat.", "одн{ому'}", "одн{о'й}", "одн{ому'}", "одн{и'м}"],
                  ["Acc.", "оди'н / одн{ого'}", "одн{у'}", "одн{о'}", "одн{и'} / одн{и'х}"],
                  ["Instr.", "одн{и'м}", "одн{о'й}", "одн{и'м}", "одн{и'ми}"],
                  ["Prep.", "(об) одн{о'м}", "(об) одн{о'й}", "(об) одн{о'м}", "(об) одн{и'х}"]])],
             examples=[
                 ex("Мы чита'ли об одно'м изве'стном писа'теле.", "We read about a famous writer.", "об одно'м"),
                 ex("Он купи'л одну' кни'гу.", "He bought one book.", "одну'"),
                 ex("Она' живёт в одно'й небольшо'й дере'вне.", "She lives in a small village.", "в одно'й"),
             ]),
        card("Accusative: animate or inanimate",
             "In the accusative, masculine singular and the plural look like the nominative for inanimate nouns and like "
             "the genitive for animate nouns.",
             tables=[table(
                 ["Noun", "Accusative"],
                 [["стол (inanimate)", "Я ви'жу оди'н стол."],
                  ["врач (animate)", "Я зна'ю одного' врача'."]])],
             examples=[
                 ex("Я зна'ю то'лько одного' врача'.", "I know only one doctor.", "одного'"),
                 ex("Я иду' к одному' ста'рому дру'гу.", "I am going to see an old friend.", "к одному'"),
             ]),
        card("Plural одни'",
             "The plural одни' is used with nouns that only exist in the plural. It can often be translated as ‘one pair of’.",
             examples=[
                 ex("У него' одни' си'ние брю'ки.", "He has one pair of blue trousers.", "одни'"),
                 ex("Он пое'хал в о'тпуск с одни'м ста'рым дру'гом.", "He went on holiday with one old friend.", "с одни'м"),
             ]),
    ],
    verify=(vf("писатель", "писателе") + vf("известный", "известном") + vf("книга", "книгу") + vf("деревня", "деревне")
            + vf("небольшой", "небольшой") + vf("врач", "врача") + vf("друг", "другу", "другом") + vf("старый", "старому", "старым")
            + vf("брюки", "брюки") + vf("синий", "синие") + vf("знать", "знаю") + vf("читать", "читали")
            + vf("купить", "купил") + vf("жить", "живёт") + vf("видеть", "вижу") + vf("стол", "стол")),
    exercises=[
        F("Мы чита'ли об ___ изве'стном писа'теле. (one)", "одно'м", ["одного'", "одному'", "одни'м"], "Prepositional masculine.", "We read about a famous writer."),
        F("Я зна'ю то'лько ___ врача'. (one)", "одного'", ["оди'н", "одному'", "одно'м"], "Animate accusative = genitive.", "I know only one doctor."),
        F("Он купи'л ___ кни'гу. (one)", "одну'", ["одна'", "одно'й", "одно'"], "Feminine accusative.", "He bought one book."),
        F("У него' ___ си'ние брю'ки. (one pair)", "одни'", ["оди'н", "одна'", "одно'"], "Plural-only noun.", "He has one pair of blue trousers."),
        F("Она' живёт в ___ небольшо'й дере'вне. (one)", "одно'й", ["одна'", "одну'", "одно'м"], "Prepositional feminine.", "She lives in a small village."),
        F("Я иду' к ___ ста'рому дру'гу. (one)", "одному'", ["одного'", "одни'м", "одно'й"], "К + dative.", "I am going to see an old friend."),
        F("Он пое'хал в о'тпуск с ___ ста'рым дру'гом. (one)", "одни'м", ["одного'", "одно'м", "одному'"], "С + instrumental.", "He went on holiday with one old friend."),
        mc("Which noun takes одни'?", ["часы'", "стол", "окно'", "кни'га"], "часы'", "Часы' (watch/clock) is plural-only.", order=True),
        mc("What is the accusative of оди'н with a person (врач)?", ["одного'", "оди'н", "одному'", "одна'"], "одного'", "Animate: genitive form.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 269
L269 = lesson(
    "Declension of 2, 3, 4 and о'ба / о'бе",
    "Преподава'тели разреши'ли трём студе'нтам пойти' на конце'рт.",
    requires=["число", "количество", "новый", "большой", "старый"],
    cards=[
        card("Two, three, four",
             "These numbers change by case. The two-form два / две is only for the nominative.",
             tables=[table(
                 ["Case", "2", "3", "4"],
                 [["Nom.", "два / две", "три", "четы'ре"],
                  ["Gen.", "двух", "трёх", "четырёх"],
                  ["Dat.", "двум", "трём", "четырём"],
                  ["Acc.", "= Nom. or Gen.", "= Nom. or Gen.", "= Nom. or Gen."],
                  ["Instr.", "двумя'", "тремя'", "четырьмя'"],
                  ["Prep.", "(о) двух", "(о) трёх", "(о) четырёх"]])],
             examples=[
                 ex("Они' дово'льны двумя' маши'нами.", "They are satisfied with the two cars.", "двумя'"),
                 ex("Мы говори'ли о четырёх студе'нтах.", "We talked about four students.", "о четырёх"),
             ]),
        card("О'ба and о'бе",
             "‘Both’ has two forms. The stress is on the first syllable in the nominative and on the middle -о- (in о'ба) or "
             "-е- (in о'бе) in the other cases.",
             tables=[table(
                 ["Case", "Masc. / neut.", "Fem."],
                 [["Nom.", "о'ба", "о'бе"],
                  ["Gen.", "обо'их", "обе'их"],
                  ["Dat.", "обо'им", "обе'им"],
                  ["Acc.", "= Nom. or Gen.", "= Nom. or Gen."],
                  ["Instr.", "обо'ими", "обе'ими"],
                  ["Prep.", "(об) обо'их", "(об) обе'их"]])],
             examples=[
                 ex("Ле'на звони'т обо'им сыновья'м и обе'им дочеря'м ка'ждую неде'лю.", "Lena calls both sons and both daughters every week.", "обо'им сыновья'м и обе'им дочеря'м"),
                 ex("Я люблю' обе'их дочере'й.", "I love both daughters.", "обе'их"),
             ]),
        card("The basic-form rule",
             "The rule ‘2–4 + genitive singular’ only works when the number is in its basic (counting) form: the "
             "nominative, or the accusative of an inanimate noun. In any other case the noun takes the same case as the number. "
             "With animate nouns the accusative of 2–4 is the genitive.",
             tables=[table(
                 ["Sentence", "Number", "Noun"],
                 [["Три студе'нта сда'ли экза'мен.", "nominative", "gen. sg."],
                  ["Я купи'л три биле'та.", "inanimate acc.", "gen. sg."],
                  ["Я зна'ю трёх студе'нтов.", "animate acc. = gen.", "animate acc. (= gen.)"],
                  ["Я помога'ю трём студе'нтам.", "dative", "dative pl."]])],
             examples=[
                 ex("Три студе'нта сда'ли экза'мен.", "Three students passed the exam.", "Три студе'нта"),
                 ex("Преподава'тели разреши'ли трём студе'нтам пойти' на конце'рт.", "The teachers allowed three students to go to the concert.", "трём студе'нтам"),
                 ex("Я зна'ю двух преподава'телей и трёх студе'нток.", "I know two teachers and three students.", "двух преподава'телей"),
             ]),
    ],
    verify=(vf("два", "двух", "двум", "двумя") + vf("три", "трёх", "трём", "тремя")
            + vf("четыре", "четырёх", "четырём", "четырьмя") + vf("оба", "обоих", "обоим", "обоими")
            + vf("студент", "студента", "студентов", "студентам", "студентах")
            + vf("преподаватель", "преподавателей") + vf("разрешить", "разрешили") + vf("пойти", "пойти")
            + vf("концерт", "концерт") + vf("сдать", "сдали") + vf("экзамен", "экзамен") + vf("машина", "машинами")
            + vf("довольный", "довольны") + vf("сын", "сыновьям") + vf("дочь", "дочерям", "дочерей")
            + vf("звонить", "звонит") + vf("каждый", "каждую") + vf("неделя", "неделю") + vf("знать", "знаю")
            + vf("говорить", "говорили") + vf("любить", "люблю") + vf("билет", "билета") + vf("помогать", "помогаю")),
    exercises=[
        F("___ студе'нта сда'ли экза'мен. (three)", "Три", ["Трёх", "Трём", "Тремя'"], "Nominative: три + gen. sg.", "Three students passed the exam."),
        F("Преподава'тели разреши'ли ___ студе'нтам пойти' на конце'рт. (three)", "трём", ["три", "трёх", "тремя'"], "Разреши'ть + dative.", "The teachers allowed three students to go to the concert."),
        F("Я зна'ю ___ студе'нток. (three)", "трёх", ["три", "трём", "тремя'"], "Animate accusative = genitive.", "I know three students."),
        F("Он купи'л ___ биле'та. (two)", "два", ["двух", "двум", "двумя'"], "Inanimate accusative = nominative.", "He bought two tickets."),
        F("Они' дово'льны ___ маши'нами. (two)", "двумя'", ["два", "двух", "двум"], "Instrumental.", "They are satisfied with two cars."),
        F("Ле'на звони'т ___ сыновья'м. (both)", "обо'им", ["о'ба", "обо'их", "обе'им"], "Dative masculine.", "Lena calls both sons."),
        F("Я люблю' ___ дочере'й. (both)", "обе'их", ["о'бе", "обо'их", "обе'им"], "Animate accusative = genitive; feminine.", "I love both daughters."),
        F("Мы говори'ли о ___ студе'нтах. (four)", "четырёх", ["четы'ре", "четырём", "четырьмя'"], "O + prepositional.", "We talked about four students."),
        mc("An animate accusative of два, три, четы'ре looks like the:", ["genitive", "dative", "instrumental", "nominative"], "genitive", "Same as the genitive.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 270
L270 = lesson(
    "Declension of 5–20 and 30: like дверь",
    "Мы познако'мились с пятна'дцатью но'выми студе'нтами.",
    requires=["число", "количество", "тысяча", "считать", "второй"],
    cards=[
        card("Only three forms",
             "Numerals from 5 to 20 and 30 end in -ь and decline like дверь. The accusative is the same as the nominative, "
             "so animate and inanimate nouns behave alike.",
             tables=[table(
                 ["Case", "пять", "во'семь", "два'дцать", "пятна'дцать"],
                 [["Nom. / Acc.", "пять", "во'семь", "два'дцать", "пятна'дцать"],
                  ["Gen. / Dat. / Prep.", "пят{и'}", "восьм{и'}", "двадцат{и'}", "пятна'дцат{и}"],
                  ["Instr.", "пят{ью'}", "восем{ью'}", "двадцат{ью'}", "пятна'дцат{ью}"]])],
             examples=[
                 ex("Он позвони'л пяти' друзья'м.", "He called five friends.", "пяти' друзья'м"),
                 ex("Я хочу' поговори'ть с пятью' друзья'ми.", "I want to talk to five friends.", "с пятью' друзья'ми"),
             ]),
        card("Stress",
             "In the short numerals the stress moves to the end of the word when the number is not in its basic form. "
             "In 11–19 the stress does not move.",
             tables=[table(
                 ["Basic form", "Other cases"],
                 [["пять", "пяти' / пятью'"],
                  ["шесть", "шести'"],
                  ["во'семь", "восьми' / восемью'"],
                  ["де'сять", "десяти'"],
                  ["два'дцать", "двадцати' / двадцатью'"],
                  ["пятна'дцать", "пятна'дцати / пятна'дцатью"]])],
             examples=[
                 ex("Э'та кни'га о восьми' ста'рых города'х.", "This book is about eight old cities.", "о восьми' ста'рых города'х"),
                 ex("Он прочита'л статью' о двадцати' интере'сных музе'ях.", "He read an article about twenty interesting museums.", "о двадцати'"),
             ]),
        card("Not the basic form: no special rule",
             "As with 2–4, the noun and the adjective copy the case of the number. There is no genitive plural unless the "
             "number is nominative or accusative.",
             tables=[table(
                 ["Number is...", "Noun is..."],
                 [["nominative: пять студе'нтов", "genitive plural"],
                  ["accusative: ви'жу пять студе'нтов", "genitive plural"],
                  ["dative: пяти' студе'нтам", "dative plural"],
                  ["instrumental: с пятью' студе'нтами", "instrumental plural"]])],
             examples=[
                 ex("Мы познако'мились с пятна'дцатью но'выми студе'нтами.", "We met fifteen new students.", "с пятна'дцатью но'выми студе'нтами"),
                 ex("Ма'ша купи'ла пять карандаше'й и де'сять ру'чек.", "Masha bought five pencils and ten pens.", "пять карандаше'й и де'сять ру'чек"),
             ]),
    ],
    verify=(vf("пять", "пять", "пяти", "пятью") + vf("восемь", "восемь", "восьми", "восемью")
            + vf("двадцать", "двадцать", "двадцати", "двадцатью") + vf("пятнадцать", "пятнадцать", "пятнадцати", "пятнадцатью")
            + vf("шесть", "шести") + vf("десять", "десять", "десяти") + vf("друг", "друзьям", "друзьями")
            + vf("позвонить", "позвонил") + vf("поговорить", "поговорить") + vf("хотеть", "хочу")
            + vf("старый", "старых") + vf("город", "городах") + vf("музей", "музеях") + vf("статья", "статью")
            + vf("прочитать", "прочитал") + vf("интересный", "интересных") + vf("познакомиться", "познакомились")
            + vf("новый", "новыми") + vf("студент", "студентами", "студентов") + vf("карандаш", "карандашей")
            + vf("ручка", "ручек") + vf("купить", "купила")),
    exercises=[
        F("Он позвони'л пяти' ___. (friends)", "друзья'м", ["друзе'й", "друзья'", "друзья'ми"], "Number in the dative: noun in the dative plural.", "He called five friends."),
        F("Мы говори'ли о ___ ста'рых города'х. (eight)", "восьми'", ["во'семь", "восемью'", "восьмо'й"], "O + prepositional.", "We talked about eight old cities."),
        F("Мы познако'мились с ___ но'выми студе'нтами. (fifteen)", "пятна'дцатью", ["пятна'дцать", "пятна'дцати", "пятна'дцатой"], "С + instrumental.", "We met fifteen new students."),
        F("Я хочу' поговори'ть с ___ друзья'ми. (five)", "пятью'", ["пять", "пяти'", "пя'тым"], "С + instrumental.", "I want to talk to five friends."),
        F("Ма'ша купи'ла пять карандаше'й и ___ ру'чек. (ten)", "де'сять", ["десяти'", "десятью'", "деся'тый"], "Accusative = nominative; noun in genitive plural.", "Masha bought five pencils and ten pens."),
        F("Он прочита'л статью' о ___ интере'сных музе'ях. (twenty)", "двадцати'", ["два'дцать", "двадцатью'", "двадцато'й"], "O + prepositional.", "He read an article about twenty interesting museums."),
        mc("Which form is the genitive of шесть?", ["шести'", "шесть", "шестью'", "шесто'й"], "шести'", "Shifted stress, ending -и.", order=True),
        mc("In which numbers does the stress not move?", ["11–19", "5–10", "20 and 30", "all of them"], "11–19", "In 11–19 the stress stays fixed.", order=True),
        mc("How many different forms does пять have?", ["three, like дверь", "six", "two", "one"], "three, like дверь", "Nom./acc., gen./dat./prep. and instr.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 271
L271 = lesson(
    "Numbers above 20: every part declines",
    "Ма'ша побыва'ла в двадцати' восьми' национа'льных па'рках.",
    requires=["число", "количество", "тысяча", "считать", "старый"],
    cards=[
        card("Every part has its own case",
             "In a number such as 25 or 36 each word takes the case ending. The last word decides whether the noun is "
             "singular or plural.",
             tables=[table(
                 ["Case", "21", "22", "25"],
                 [["Nom.", "два'дцать оди'н", "два'дцать два", "два'дцать пять"],
                  ["Gen.", "двадцати' одного'", "двадцати' двух", "двадцати' пяти'"],
                  ["Dat.", "двадцати' одному'", "двадцати' двум", "двадцати' пяти'"],
                  ["Instr.", "двадцатью' одни'м", "двадцатью' двумя'", "двадцатью' пятью'"],
                  ["Prep.", "(о) двадцати' одно'м", "(о) двадцати' двух", "(о) двадцати' пяти'"]])],
             examples=[
                 ex("Ма'ша побыва'ла в двадцати' восьми' национа'льных па'рках.", "Masha visited twenty-eight national parks.", "двадцати' восьми'"),
                 ex("Я говори'л с двадцатью' пятью' студе'нтами.", "I talked to twenty-five students.", "двадцатью' пятью'"),
             ]),
        card("The last digit",
             "The nominative and inanimate accusative follow the last digit: 21 → nominative singular, 22–24 → genitive "
             "singular, 25–30 → genitive plural.",
             tables=[table(
                 ["Number", "Noun"],
                 [["два'дцать оди'н национа'льный парк", "nominative singular"],
                  ["два'дцать два национа'льных па'рка", "genitive singular"],
                  ["два'дцать во'семь национа'льных па'рков", "genitive plural"]])],
             examples=[
                 ex("В на'шем шта'те есть два'дцать оди'н национа'льный парк.", "In our state there are 21 national parks.", "два'дцать оди'н национа'льный парк"),
                 ex("В сосе'днем шта'те есть два'дцать два национа'льных па'рка.", "In the next state there are 22 national parks.", "два'дцать два национа'льных па'рка"),
             ]),
        card("Animate nouns: only for simple 2–4 and 1",
             "The animate-accusative rule is used for simple 2, 3 and 4. It does not apply to 22, 23 or 24. It does "
             "apply to 21, because one is an adjective.",
             tables=[table(
                 ["Number", "Accusative"],
                 [["3", "Мы ви'дели трёх актёров."],
                  ["23", "Мы ви'дели два'дцать три актёра."],
                  ["21", "Мы ви'дели два'дцать одного' актёра."]])],
             examples=[
                 ex("Мы ви'дели два'дцать три актёра.", "We saw twenty-three actors.", "два'дцать три актёра"),
                 ex("Мы ви'дели два'дцать одного' актёра.", "We saw twenty-one actors.", "два'дцать одного' актёра"),
             ]),
    ],
    verify=(vf("двадцать", "двадцать", "двадцати", "двадцатью") + vf("один", "один", "одного", "одному", "одном")
            + vf("два", "два", "двух", "двум", "двумя") + vf("пять", "пять", "пяти", "пятью")
            + vf("восемь", "восемь", "восьми") + vf("три", "три", "трёх") + vf("парк", "парк", "парка", "парков", "парках")
            + vf("национальный", "национальный", "национальных") + vf("побывать", "побывала") + vf("студент", "студентами")
            + vf("штат", "штате") + vf("соседний", "соседнем") + vf("видеть", "видели") + vf("актёр", "актёров", "актёра")
            + vf("говорить", "говорил")),
    exercises=[
        F("В шта'те есть два'дцать оди'н национа'льный ___. (park)", "парк", ["па'рка", "па'рки", "па'рков"], "21: nominative singular.", "There are 21 national parks in the state."),
        F("В шта'те есть два'дцать два национа'льных ___. (parks)", "па'рка", ["парк", "па'рки", "па'рков"], "22: genitive singular.", "There are 22 national parks in the state."),
        F("В стране' есть два'дцать во'семь национа'льных ___. (parks)", "па'рков", ["парк", "па'рка", "па'рки"], "28: genitive plural.", "There are 28 national parks in the country."),
        F("Я чита'л статью' о двадцати' ___ национа'льном па'рке. (one)", "одно'м", ["оди'н", "одного'", "одну'"], "Prepositional masculine.", "I read an article about twenty-one national parks."),
        F("Та'ня чита'ла о двадцати' ___ национа'льных па'рках. (two)", "двух", ["два", "двум", "двумя'"], "Prepositional.", "Tanya read about twenty-two national parks."),
        F("Мы ви'дели два'дцать три ___. (actors)", "актёра", ["актёров", "актёры", "актёру"], "Not a simple 3: no animate rule; genitive singular.", "We saw twenty-three actors."),
        F("Мы ви'дели два'дцать ___ актёра. (one, animate)", "одного'", ["оди'н", "одному'", "одну'"], "Animate accusative of one.", "We saw twenty-one actors."),
        F("Я говори'л с двадцатью' ___ студе'нтами. (five)", "пятью'", ["пять", "пяти'", "пя'тым"], "Each part is instrumental.", "I talked to twenty-five students."),
        mc("What decides the number of the noun after 22, 33, 54?", ["the last digit", "the first digit", "the whole number", "the verb"], "the last digit", "Last digit: 2–4 → genitive singular.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 272
L272 = lesson(
    "Review: travel, short participles, numbers",
    "В гости'нице бы'ло пять свобо'дных номеро'в.",
    requires=["число", "количество", "тысяча", "считать", "большой"],
    cards=[
        card("Numbers and nouns",
             "Remember the three patterns: оди'н + nominative; два, три, четы'ре + genitive singular; пять and more + "
             "genitive plural. If the number is not in its basic form, the noun takes the case of the number.",
             tables=[table(
                 ["Phrase", "Pattern"],
                 [["оди'н но'вый но'мер", "1 + nominative"],
                  ["два но'вых но'мера", "2–4 + gen. sg."],
                  ["пять но'вых номеро'в", "5+ + gen. pl."],
                  ["о пяти' но'вых номера'х", "other case → same case"]])],
             examples=[
                 ex("В гости'нице бы'ло пять свобо'дных номеро'в.", "There were five free rooms in the hotel.", "пять свобо'дных номеро'в"),
             ]),
        card("Headlines and short participles",
             "A short participle agrees in gender and number with its noun: закры'т, закры'та, закры'то, закры'ты. In "
             "headlines the verb быть is dropped.",
             examples=[
                 ex("Откры'та но'вая гости'ница.", "A new hotel has opened.", "Откры'та"),
                 ex("Все биле'ты уже' ку'плены.", "All the tickets have already been bought.", "ку'плены"),
             ]),
    ],
    verify=(vf("гостиница", "гостинице", "гостиница") + vf("свободный", "свободных", "свободная") + vf("номер", "номеров", "номера", "номерах")
            + vf("билет", "билеты") + vf("новый", "новых")),
    exercises=[
        F("Три тури'ста ___ в гости'нице. (stayed)", "останови'лись", ["останови'лся", "останови'ться", "останови'ла"], "Plural past.", "Three tourists stayed at the hotel."),
        F("Мы заброни'ровали но'мер на ___ ноче'й. (five)", "пять", ["пяти'", "пятью'", "пя'тый"], "Basic form after на.", "We booked a room for five nights."),
        F("Все биле'ты уже' ___. (bought)", "ку'плены", ["ку'плен", "ку'плена", "ку'плено"], "Plural short form.", "All the tickets have already been bought."),
        F("Она' позвони'ла двум ___. (friends, f.)", "подру'гам", ["подру'г", "подру'ги", "подру'гами"], "Dative plural after the dative number.", "She called two friends."),
        F("У нас два ___ окна'. (big)", "больши'х", ["больши'е", "большо'е", "большо'й"], "Neuter: genitive plural.", "We have two big windows."),
        F("Мы говори'ли о четырёх ___. (restaurants)", "рестора'нах", ["рестора'на", "рестора'нов", "рестора'ны"], "Prepositional plural.", "We talked about four restaurants."),
        F("В меню' пять ___ блюд. (tasty)", "вку'сных", ["вку'сные", "вку'сный", "вку'сного"], "5+: genitive plural.", "There are five tasty dishes on the menu."),
        F("Мы ви'дели двух ___ тури'стов. (Russian)", "ру'сских", ["ру'сские", "ру'сский", "ру'сского"], "Animate accusative = genitive plural.", "We saw two Russian tourists."),
        mc("Which headline means ‘A new hotel has opened’?", ["Откры'та но'вая гости'ница", "Откры'то но'вая гости'ница", "Откры'т но'вая гости'ница", "Откры'ты но'вая гости'ница"], "Откры'та но'вая гости'ница", "Гости'ница is feminine.", order=True),
        mc("What happens to a noun after трём?", ["it goes into the dative plural", "it stays in the genitive singular", "it goes into the genitive plural", "it goes into the nominative"], "it goes into the dative plural", "Not the basic form: the noun copies the case.", order=True),
    ],
)

UNIT = unit("Unit 27: Travel, food, short participles and numbers",
            [L259, L260, L261, L262, L263, L264, L265, L266, L267, L268, L269, L270, L271, L272])
