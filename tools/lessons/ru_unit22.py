"""Unit 22: housing, furniture and the instrumental plural (textbook module 5, lesson 29)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 204
L204 = lesson(
    "Living room, bedroom, hallway: parts of a home",
    "Мы у'жинаем в гости'ной, а спим в спа'льне.",
    requires=["кухня", "дверь", "лестница", "пол", "комната"],
    cards=[
        card("Rooms",
             "Here are the rooms of a home. Note that гости'ная, ва'нная and прихо'жая look like feminine adjectives "
             "and decline that way: they are short for “living room”, “bathroom” and “entry room”, with the word "
             "ко'мната understood.",
             tables=[table(
                 ["Room", "English", "In the...?"],
                 [["гости'ная", "living room", "в гости'ной"],
                  ["спа'льня", "bedroom", "в спа'льне"],
                  ["ку'хня", "kitchen", "на ку'хне"],
                  ["ва'нная", "bathroom", "в ва'нной"],
                  ["прихо'жая", "entryway", "в прихо'жей"],
                  ["кабине'т", "study, office", "в кабине'те"],
                  ["коридо'р", "hallway", "в коридо'ре"],
                  ["туале'т", "restroom", "в туале'те"]])],
             examples=[
                 ex("Мы у'жинаем в гости'ной, а спим в спа'льне.", "We have dinner in the living room and sleep in the bedroom.", "в гости'ной"),
                 ex("Мои' ключи' в прихо'жей.", "My keys are in the entryway.", "в прихо'жей"),
                 ex("Ма'ма мно'го вре'мени прово'дит на ку'хне.", "Mom spends a lot of time in the kitchen.", "на ку'хне"),
             ]),
        card("Parts of a house",
             "These words describe the structure. Learn the unusual prepositional forms: на полу' (on the floor) and "
             "на потолке' (on the ceiling).",
             tables=[table(
                 ["Word", "English", "Example"],
                 [["дверь", "door", "Дверь в спа'льню закры'та."],
                  ["ле'стница", "stairs", "Ле'стница ведёт на кры'шу."],
                  ["пол", "floor", "Ковёр лежи'т на полу'."],
                  ["потоло'к", "ceiling", "На потолке' виси'т лю'стра."],
                  ["кры'ша", "roof", "На кры'ше сиди'т пти'ца."],
                  ["душ", "shower", "Я принима'ю душ у'тром."],
                  ["ва'нна", "bathtub", "Он принима'ет ва'нну."]])],
             examples=[
                 ex("Ле'стница ведёт на кры'шу.", "The staircase leads up to the roof.", "на кры'шу"),
                 ex("Ковёр лежи'т на полу'.", "The rug lies on the floor.", "на полу'"),
                 ex("На потолке' виси'т лю'стра.", "A chandelier hangs on the ceiling.", "На потолке'"),
             ]),
    ],
    verify=(vf("кухня", "кухне") + vf("кабинет", "кабинете") + vf("коридор", "коридоре") + vf("туалет", "туалете")
            + vf("спальня", "спальне") + vf("ключ", "ключи") + vf("пол", "полу") + vf("потолок", "потолке")
            + vf("лестница", "лестница") + vf("крыша", "крышу", "крыше") + vf("душ", "душ") + vf("ванна", "ванну")
            + vf("ковёр", "ковёр") + vf("люстра", "люстра") + vf("проводить", "проводит") + vf("принимать", "принимаю", "принимает")),
    exercises=[
        F("Мы у'жинаем в ___. (the living room)", "гости'ной", ["гости'ная", "гости'ную", "гости'ные"], "Declines like an adjective: в гости'ной.", "We have dinner in the living room."),
        F("Он сейча'с в ___. (the bathroom)", "ва'нной", ["ва'нная", "ва'нную", "ва'нные"], "Declines like an adjective: в ва'нной.", "He is in the bathroom now."),
        F("Мои' ключи' в ___. (the entryway)", "прихо'жей", ["прихо'жая", "прихо'жую", "прихо'жие"], "Declines like an adjective: в прихо'жей.", "My keys are in the entryway."),
        F("Ма'ма мно'го вре'мени прово'дит ___. (in the kitchen)", "на ку'хне", ["на ку'хню", "на ку'хня", "на ку'хней"], "Prepositional: на ку'хне.", "Mom spends a lot of time in the kitchen."),
        F("Ле'стница ведёт на ___. (the roof)", "кры'шу", ["кры'ша", "кры'ше", "кры'ши"], "На + accusative for direction.", "The staircase leads to the roof.", lemma="крыша"),
        F("На ___ виси'т лю'стра. (the ceiling)", "потолке'", ["потолка'", "потоло'к", "потолки'"], "Prepositional: на потолке'.", "A chandelier hangs on the ceiling.", lemma="потолок"),
        F("Ковёр лежи'т на ___. (the floor)", "полу'", ["пол", "по'ла", "по'лы"], "Special prepositional: на полу'.", "The rug lies on the floor.", lemma="пол"),
        F("Я принима'ю ___ у'тром. (a shower)", "душ", ["ду'ша", "ду'шу", "ду'ше"], "Принима'ть душ.", "I take a shower in the morning."),
        mc("Ва'нная, гости'ная and прихо'жая decline like...", ["feminine adjectives", "masculine nouns", "neuter nouns", "feminine nouns in -ь"], "feminine adjectives", "They are adjectives used as nouns."),
    ],
)

# ---------------------------------------------------------------------------- 205
L205 = lesson(
    "Sofa, armchair, rug: furniture and interior",
    "Напро'тив дива'на стои'т кре'сло.",
    requires=["кресло", "зеркало", "картина", "мебель", "стол"],
    cards=[
        card("Furniture and interior",
             "Learn the genders: they decide the adjective endings.",
             tables=[table(
                 ["Word", "English"],
                 [["ме'бель (f.)", "furniture"],
                  ["дива'н", "sofa"],
                  ["кре'сло", "armchair"],
                  ["крова'ть (f.)", "bed"],
                  ["шкаф", "wardrobe, cabinet"],
                  ["по'лка", "shelf"],
                  ["пи'сьменный стол", "desk"],
                  ["журна'льный сто'лик", "coffee table"],
                  ["ковёр", "rug, carpet"],
                  ["зе'ркало", "mirror"],
                  ["карти'на", "painting"],
                  ["лю'стра", "chandelier"],
                  ["плита'", "stove"],
                  ["холоди'льник", "refrigerator"]])],
             examples=[
                 ex("Напро'тив дива'на стои'т кре'сло.", "An armchair stands opposite the sofa.", "кре'сло"),
                 ex("Во'зле окна' стои'т пи'сьменный стол.", "A desk stands near the window.", "пи'сьменный стол"),
                 ex("На стене' виси'т кру'глое зе'ркало.", "A round mirror hangs on the wall.", "кру'глое зе'ркало"),
             ]),
        card("Describing a place",
             "These adjectives are useful when you describe a home. The shapes can be nouns or adjectives.",
             tables=[table(
                 ["Adjective", "English"],
                 [["просто'рный", "spacious"],
                  ["ую'тный", "cozy"],
                  ["совреме'нный", "modern"],
                  ["удо'бный", "comfortable, convenient"],
                  ["шу'мный", "noisy"],
                  ["отде'льный", "separate"],
                  ["кру'глый (круг)", "round (circle)"],
                  ["квадра'тный (квадра'т)", "square"],
                  ["треуго'льный (треуго'льник)", "triangular"]])],
             examples=[
                 ex("Мы хоти'м просто'рную кварти'ру.", "We want a spacious apartment.", "просто'рную кварти'ру"),
                 ex("У нас ую'тная гости'ная.", "We have a cozy living room.", "ую'тная"),
                 ex("Окна' выхо'дят на у'лицу.", "The windows face the street.", "выхо'дят на у'лицу"),
             ]),
        card("Where things are: напро'тив, во'зле, среди'",
             "These three prepositions take the genitive: напро'тив (opposite), во'зле (near), среди' (among). "
             "Про'тив + genitive also means “against”.",
             examples=[
                 ex("Во'зле дива'на стои'т ма'ленький сто'лик.", "A small table stands near the sofa.", "Во'зле дива'на"),
                 ex("Ковёр лежи'т среди' ме'бели.", "The rug lies among the furniture.", "среди' ме'бели"),
                 ex("Я про'тив э'того пла'на.", "I am against this plan.", "про'тив э'того пла'на"),
             ]),
    ],
    verify=(vf("мебель", "мебели") + vf("диван", "дивана") + vf("кресло", "кресло") + vf("кровать", "кровать")
            + vf("шкаф", "шкаф") + vf("полка", "полка") + vf("письменный", "письменный") + vf("журнальный", "журнальный")
            + vf("ковёр", "ковёр") + vf("зеркало", "зеркало") + vf("круглый", "круглое") + vf("картина", "картина")
            + vf("просторный", "просторную") + vf("уютный", "уютная") + vf("окно", "окна") + vf("улица", "улицу")
            + vf("маленький", "маленький") + vf("план", "плана")),
    exercises=[
        F("Напро'тив дива'на стои'т ___. (an armchair)", "кре'сло", ["кре'сла", "кре'слу", "кре'слом"], "Nominative: стои'т кре'сло.", "An armchair stands opposite the sofa.", lemma="кресло"),
        F("Во'зле окна' стои'т пи'сьменный ___. (desk)", "стол", ["сто'ла", "столу'", "столе'"], "Nominative: стол.", "A desk stands near the window.", lemma="стол"),
        F("На стене' виси'т ___ зе'ркало. (round)", "кру'глое", ["кру'глый", "кру'глая", "кру'глые"], "Neuter: кру'глое.", "A round mirror hangs on the wall."),
        F("У нас ___ кварти'ра. (spacious)", "просто'рная", ["просто'рный", "просто'рное", "просто'рные"], "Feminine: просто'рная.", "We have a spacious apartment."),
        F("Ковёр лежи'т на ___. (the floor)", "полу'", ["пол", "по'ла", "по'лы"], "На полу'.", "The rug lies on the floor.", lemma="пол"),
        F("Окна' выхо'дят на ___. (the street)", "у'лицу", ["у'лица", "у'лице", "у'лицей"], "Выходи'ть на + accusative.", "The windows face the street.", lemma="улица"),
        F("Мы живём в ___ кварти'ре. (modern)", "совреме'нной", ["совреме'нная", "совреме'нную", "совреме'нные"], "Prepositional feminine.", "We live in a modern apartment."),
        F("Э'то ___ стул. (comfortable)", "удо'бный", ["удо'бная", "удо'бное", "удо'бные"], "Masculine: удо'бный.", "This is a comfortable chair."),
        mc("What does кру'глый mean?", ["round", "square", "triangular", "separate"], "round", "Кру'глый = round.", order=True),
        mc("What is ме'бель?", ["furniture", "mirror", "kitchen", "ceiling"], "furniture", "Ме'бель = furniture."),
    ],
)

# ---------------------------------------------------------------------------- 206
L206 = lesson(
    "Lease, utilities, housewarming: renting and buying a home",
    "Мы подписа'ли догово'р аре'нды на год.",
    requires=["квартира", "аренда", "договор", "стоимость", "жильё"],
    cards=[
        card("The housing market",
             "These nouns come up when you rent, buy or move.",
             tables=[table(
                 ["Word", "English"],
                 [["жильё (sing. only)", "housing"],
                  ["аре'нда", "rent (of an apartment)"],
                  ["догово'р", "agreement, contract"],
                  ["коммуна'льные услу'ги", "utilities"],
                  ["объявле'ние", "announcement, ad"],
                  ["сто'имость (f.)", "cost"],
                  ["при'город", "suburb"],
                  ["окра'ина", "outskirts"],
                  ["уча'сток", "lot, plot of land"],
                  ["отопле'ние", "heating"],
                  ["общежи'тие", "dormitory"],
                  ["новосе'лье", "housewarming"],
                  ["де'тская площа'дка", "playground"]])],
             examples=[
                 ex("Мы подписа'ли догово'р аре'нды на год.", "We signed a lease for a year.", "догово'р аре'нды"),
                 ex("Мы нашли' жильё по объявле'нию.", "We found a place from an ad.", "по объявле'нию"),
                 ex("Во дворе' есть де'тская площа'дка.", "There is a playground in the yard.", "де'тская площа'дка"),
             ]),
        card("Phrases",
             "Useful set expressions for talking about where you live.",
             tables=[table(
                 ["Russian", "English"],
                 [["Окна' выхо'дят на...", "The windows face..."],
                  ["С одно'й стороны'..., с друго'й стороны'...", "On the one hand..., on the other hand..."],
                  ["со вре'менем", "over time"],
                  ["Э'то меня' устра'ивает.", "That suits me."],
                  ["Э'то меня' не устра'ивает.", "That does not suit me."]])],
             examples=[
                 ex("Мы живём на окра'ине го'рода.", "We live on the outskirts of the city.", "на окра'ине"),
                 ex("Со вре'менем мы ку'пим бо'льше ме'бели.", "Over time we will buy more furniture.", "Со вре'менем"),
                 ex("Сто'имость аре'нды о'чень высо'кая.", "The cost of the rent is very high.", "Сто'имость аре'нды"),
             ]),
    ],
    verify=(vf("жильё", "жильё") + vf("аренда", "аренды") + vf("договор", "договор") + vf("объявление", "объявлению")
            + vf("двор", "дворе") + vf("площадка", "площадка") + vf("окраина", "окраине") + vf("стоимость", "стоимость")
            + vf("высокий", "высокая") + vf("время", "временем") + vf("участок", "участок") + vf("отопление", "отопление")
            + vf("новоселье", "новоселье") + vf("пригласить", "пригласили") + vf("платить", "платим")),
    exercises=[
        F("Мы подписа'ли ___ аре'нды. (agreement)", "догово'р", ["догово'ра", "догово'ру", "догово'ре"], "Подписа'ть догово'р.", "We signed the lease.", lemma="договор"),
        F("Мы живём на ___ го'рода. (outskirts)", "окра'ине", ["окра'ину", "окра'ина", "окра'ины"], "На окра'ине.", "We live on the outskirts of the city.", lemma="окраина"),
        F("Во дворе' есть де'тская ___. (playground)", "площа'дка", ["площа'дку", "площа'дке", "площа'дки"], "Есть + nominative.", "There is a playground in the yard.", lemma="площадка"),
        F("Мы нашли' жильё по ___. (an ad)", "объявле'нию", ["объявле'ние", "объявле'ния", "объявле'нием"], "По + dative.", "We found a place from an ad.", lemma="объявление"),
        F("Сто'имость аре'нды о'чень ___. (high)", "высо'кая", ["высо'кий", "высо'кое", "высо'кую"], "Feminine: высо'кая.", "The cost of the rent is very high."),
        F("Мы пригласи'ли друзе'й на ___. (a housewarming)", "новосе'лье", ["новосе'лья", "новосе'лью", "новосе'льем"], "На + accusative = nominative for neuter.", "We invited our friends to the housewarming."),
        F("Со ___ мы ку'пим бо'льше ме'бели. (over time)", "вре'менем", ["вре'мени", "вре'мя", "времена'"], "Со вре'менем = over time.", "Over time we will buy more furniture.", lemma="время"),
        mc("What does отопле'ние mean?", ["heating", "furniture", "outskirts", "lot of land"], "heating", "Отопле'ние = heating.", order=True),
        mc("Which word means “suburb”?", ["при'город", "окра'ина", "уча'сток", "двор"], "при'город", "При'город = suburb."),
    ],
)

# ---------------------------------------------------------------------------- 207
L207 = lesson(
    "Rent, hand over, host, forbid: verbs of the home",
    "Мы сня'ли кварти'ру в при'городе.",
    requires=["снимать", "сдавать", "принимать", "устраивать", "подписать"],
    cards=[
        card("The verbs and their meanings",
             "Many of these verbs have several meanings, so learn them with a typical object.",
             tables=[table(
                 ["Verb", "Meanings"],
                 [["снима'ть / снять", "rent (from someone); take off; film"],
                  ["сдава'ть / сдать", "rent out; take (an exam)"],
                  ["арендова'ть", "rent (formal)"],
                  ["принима'ть / приня'ть", "accept; receive (guests); take (a shower)"],
                  ["устра'ивать / устро'ить", "arrange, host; suit"],
                  ["запреща'ть / запрети'ть", "forbid"],
                  ["ве'рить / пове'рить (+ dat.)", "believe"]])],
             examples=[
                 ex("Мы сня'ли кварти'ру в при'городе.", "We rented an apartment in the suburbs.", "сня'ли"),
                 ex("Ба'бушка сдаёт две ко'мнаты студе'нтам.", "Grandma rents two rooms to students.", "сдаёт"),
                 ex("Э'та кварти'ра меня' устра'ивает.", "This apartment suits me.", "устра'ивает"),
             ]),
        card("Some forms",
             "Арендова'ть and сдава'ть are the new patterns here. The perfective forms of снять, приня'ть and сдать are "
             "worth memorizing.",
             tables=[table(
                 ["Person", "арендова'ть", "сдава'ть"],
                 [["я", "аренду'ю", "сдаю'"],
                  ["ты", "аренду'ешь", "сдаёшь"],
                  ["он, она'", "аренду'ет", "сдаёт"],
                  ["мы", "аренду'ем", "сдаём"],
                  ["вы", "аренду'ете", "сдаёте"],
                  ["они'", "аренду'ют", "сдаю'т"]]),
                 table(
                 ["Person", "снять", "приня'ть", "сдать"],
                 [["я", "сниму'", "приму'", "сдам"],
                  ["ты", "сни'мешь", "при'мешь", "сдашь"],
                  ["он, она'", "сни'мет", "при'мет", "сдаст"],
                  ["мы", "сни'мем", "при'мем", "сдади'м"],
                  ["вы", "сни'мете", "при'мете", "сдади'те"],
                  ["они'", "сни'мут", "при'мут", "сдаду'т"],
                  ["он (past)", "снял", "при'нял", "сдал"],
                  ["она' (past)", "сняла'", "приняла'", "сдала'"]])],
             examples=[
                 ex("Не снима'йте пальто', у нас хо'лодно.", "Don't take off your coat, it is cold here.", "снима'йте"),
                 ex("Мы принима'ем госте'й в суббо'ту.", "We are having guests on Saturday.", "принима'ем"),
                 ex("Он сдал экза'мен и о'чень рад.", "He passed the exam and is very glad.", "сдал"),
             ]),
    ],
    verify=(vf("арендовать", "арендую", "арендуешь", "арендуют") + vf("сдавать", "сдаю", "сдаёшь", "сдаёт", "сдаю")
            + vf("снять", "сниму", "снимешь", "снимет", "снимем", "снимете", "снимут", "снял", "сняла")
            + vf("принять", "приму", "примешь", "примет", "примем", "примете", "примут", "принял", "приняла")
            + vf("сдать", "сдам", "сдашь", "сдаст", "сдадим", "сдадите", "сдадут", "сдал", "сдала")
            + vf("снимать", "снимайте") + vf("принимать", "принимаем") + vf("устраивать", "устраивает")
            + vf("пальто", "пальто") + vf("бабушка", "бабушка")),
    exercises=[
        F("Мы ___ кварти'ру в при'городе. (rented it from a landlord)", "сня'ли", ["сда'ли", "сня'ло", "сда'ло"], "Снять = rent from someone.", "We rented an apartment in the suburbs."),
        F("Ба'бушка ___ две ко'мнаты студе'нтам. (rents out)", "сдаёт", ["снима'ет", "сни'мет", "сдаю'"], "Сдава'ть = rent out.", "Grandma rents out two rooms to students."),
        F("Он ___ экза'мен и о'чень рад. (passed)", "сдал", ["снял", "запрети'л", "арендова'л"], "Сдать экза'мен = pass an exam.", "He passed the exam and is very glad."),
        F("Не ___ пальто', у нас хо'лодно. (take off)", "снима'йте", ["сдава'йте", "принима'йте", "запреща'йте"], "Снима'ть = take off.", "Don't take off your coat, it is cold here."),
        F("Я не ___ э'тому челове'ку. (believe)", "ве'рю", ["ве'рит", "запрещу'", "устра'иваю"], "Ве'рить + dative.", "I do not believe this person."),
        F("Ма'ма ___ сы'ну игра'ть на у'лице. (forbade)", "запрети'ла", ["сняла'", "сдала'", "арендова'ла"], "Запрети'ть = forbid.", "Mom forbade her son to play in the street."),
        F("Э'та кварти'ра меня' ___. (suits)", "устра'ивает", ["снима'ет", "сдаёт", "запреща'ет"], "Устра'ивать = suit.", "This apartment suits me."),
        F("В суббо'ту мы ___ госте'й. (are having)", "принима'ем", ["снима'ем", "сдаём", "ве'рим"], "Принима'ть госте'й.", "On Saturday we are having guests."),
        mc("Which verb means “to rent out”?", ["сдава'ть", "снима'ть", "принима'ть", "запреща'ть"], "сдава'ть", "Сдава'ть = rent out."),
        mc("What case does ве'рить take?", ["dative", "genitive", "accusative", "instrumental"], "dative", "Ве'рить + dative."),
    ],
)

# ---------------------------------------------------------------------------- 208
L208 = lesson(
    "With friends, with children: the instrumental plural of nouns",
    "Я часто встречаюсь с друзья'ми.",
    requires=["ребёнок", "сосед", "друг", "врач", "студент"],
    cards=[
        card("-ами or -ями",
             "In the instrumental plural, nouns take -ами after a hard stem and -ями after a soft stem. The stress "
             "stays where it was in the nominative plural. After к, г, х, ж, ч, ш, щ and ц the ending is -ами "
             "(never -ями).",
             tables=[table(
                 ["Nominative plural", "Instrumental plural", "Type"],
                 [["студе'нты", "студе'нт{ами}", "hard"],
                  ["доктора'", "доктор{а'ми}", "hard"],
                  ["ко'шки", "ко'шк{ами}", "after к"],
                  ["врачи'", "врач{а'ми}", "after ч"],
                  ["у'лицы", "у'лиц{ами}", "after ц"],
                  ["учителя'", "учител{я'ми}", "soft"],
                  ["сосе'ди", "сосе'д{ями}", "soft"],
                  ["ле'кции", "ле'кц{иями}", "-ия"],
                  ["неде'ли", "неде'л{ями}", "soft"]])],
             examples=[
                 ex("Я ча'сто встреча'юсь с друзья'ми.", "I often meet with my friends.", "с друзья'ми"),
                 ex("Мы разгова'риваем с сосе'дями.", "We talk with our neighbors.", "с сосе'дями"),
                 ex("Она' идёт к врача'м.", "She is going to the doctors.", "к врача'м"),
             ]),
        card("Remember these",
             "Four nouns are special: люди, дети and дочери take -ьми and have end stress, and ма'тери becomes матеря'ми.",
             tables=[table(
                 ["Nominative plural", "Instrumental plural"],
                 [["лю'ди", "люд{ьми'}"],
                  ["де'ти", "дет{ьми'}"],
                  ["до'чери", "дочер{ьми'}"],
                  ["ма'тери", "матер{я'ми}"],
                  ["друзья'", "друзья'ми"],
                  ["бра'тья", "бра'тьями"],
                  ["сёстры", "сёстрами"],
                  ["дере'вья", "дере'вьями"],
                  ["де'ньги", "деньга'ми"]])],
             examples=[
                 ex("Он познако'мился с интере'сными людьми'.", "He got to know some interesting people.", "людьми'"),
                 ex("Она' гуля'ет с детьми' в па'рке.", "She walks with the children in the park.", "с детьми'"),
                 ex("Над крова'тями вися'т карти'ны.", "Paintings hang above the beds.", "крова'тями"),
             ]),
    ],
    verify=(vf("студент", "студентами") + vf("доктор", "докторами") + vf("кошка", "кошками") + vf("врач", "врачами")
            + vf("улица", "улицами") + vf("учитель", "учителями") + vf("сосед", "соседями") + vf("лекция", "лекциями")
            + vf("неделя", "неделями") + vf("человек", "людьми") + vf("ребёнок", "детьми") + vf("дочь", "дочерьми")
            + vf("мать", "матерями") + vf("друг", "друзьями") + vf("брат", "братьями") + vf("сестра", "сёстрами")
            + vf("дерево", "деревьями") + vf("деньги", "деньгами") + vf("кровать", "кроватями")
            + vf("картина", "картины") + vf("висеть", "висят") + vf("гулять", "гуляет")),
    exercises=[
        F("Я ча'сто встреча'юсь с ___. (friends)", "друзья'ми", ["друзья'м", "друзе'й", "друзья'х"], "Instrumental plural: друзья'ми.", "I often meet with my friends.", lemma="друг"),
        F("Мы разгова'риваем с ___. (neighbors)", "сосе'дями", ["сосе'дям", "сосе'дей", "сосе'дях"], "Soft stem: -ями.", "We talk with our neighbors.", lemma="сосед"),
        F("Она' гуля'ет с ___ в па'рке. (children)", "детьми'", ["де'тями", "дета'ми", "дете'й"], "Special: детьми'.", "She walks with the children in the park.", lemma="ребёнок"),
        F("Он познако'мился с ___. (people)", "людьми'", ["лю'дями", "люде'й", "лю'дям"], "Special: людьми'.", "He got acquainted with some people.", lemma="человек"),
        F("Ма'ма разгова'ривает с ___. (her daughters)", "дочерьми'", ["дочеря'м", "дочеря'х", "дочере'й"], "Special: дочерьми'.", "Mom is talking with her daughters.", lemma="дочь"),
        F("Мы поговори'ли с ___. (teachers)", "учителя'ми", ["учителя'м", "учителе'й", "учителя'х"], "Soft stem: -ями; stress as in учителя'.", "We talked with the teachers.", lemma="учитель"),
        F("Над ___ вися'т карти'ны. (beds)", "крова'тями", ["крова'ти", "крова'тей", "крова'тях"], "Soft stem: -ями.", "Paintings hang above the beds.", lemma="кровать"),
        F("Под ___ лежи'т снег. (trees)", "дере'вьями", ["дере'вья", "дере'вьев", "дере'вьях"], "Дере'вья → дере'вьями.", "Snow lies under the trees.", lemma="дерево"),
        mc("Which ending do hard-stem nouns take in the instrumental plural?", ["-ами", "-ями", "-ам", "-ах"], "-ами", "-ами.", order=True),
        mc("After к, г, х, ж, ч, ш, щ the ending is...", ["-ами", "-ями", "-ыми", "-ими"], "-ами", "Spelling rule: а, not я."),
    ],
)

# ---------------------------------------------------------------------------- 209
L209 = lesson(
    "With new friends, with all of them: adjectives in the instrumental plural",
    "Мы ча'сто разгова'риваем с на'шими сосе'дями.",
    requires=["новый", "мой", "этот", "весь", "хороший"],
    cards=[
        card("-ыми or -ими",
             "Adjectives, ordinal numbers and adjectival pronouns take -ыми after a hard stem and -ими after a soft "
             "stem or after к, г, х, ж, ч, ш, щ. The stress stays where it was in the nominative plural.",
             tables=[table(
                 ["Nominative plural", "Instrumental plural"],
                 [["но'вые", "но'в{ыми}"],
                  ["интере'сные", "интере'сн{ыми}"],
                  ["больши'е", "больш{и'ми}"],
                  ["ру'сские", "ру'сск{ими}"],
                  ["хоро'шие", "хоро'ш{ими}"],
                  ["дороги'е", "дорог{и'ми}"],
                  ["пе'рвые", "пе'рв{ыми}"]])],
             examples=[
                 ex("Я люблю' знако'миться с интере'сными людьми'.", "I like to get acquainted with interesting people.", "с интере'сными людьми'"),
                 ex("Он интересу'ется дороги'ми маши'нами.", "He is interested in expensive cars.", "дороги'ми маши'нами"),
                 ex("Мы дружи'м с ру'сскими студе'нтами.", "We are friends with Russian students.", "с ру'сскими студе'нтами"),
             ]),
        card("Pronouns",
             "Possessives and demonstratives follow the same pattern. Те and все simply add -ми, and его, её, их never "
             "change.",
             tables=[table(
                 ["Nominative plural", "Instrumental plural"],
                 [["мои'", "мо{и'ми}"],
                  ["на'ши", "на'ш{ими}"],
                  ["э'ти", "э'т{ими}"],
                  ["те", "те'{ми}"],
                  ["все", "все'{ми}"],
                  ["каки'е", "как{и'ми}"],
                  ["таки'е", "так{и'ми}"],
                  ["его', её, их", "его', её, их"]])],
             examples=[
                 ex("Я не интересу'юсь те'ми людьми'.", "I am not interested in those people.", "те'ми людьми'"),
                 ex("Я уже' поговори'л со все'ми.", "I have already spoken with everyone.", "со все'ми"),
                 ex("Она' гуля'ет с его' соба'ками.", "She walks with his dogs.", "с его' соба'ками"),
             ]),
    ],
    verify=(vf("новый", "новыми") + vf("интересный", "интересными") + vf("большой", "большими") + vf("русский", "русскими")
            + vf("хороший", "хорошими") + vf("дорогой", "дорогими") + vf("первый", "первыми") + vf("мой", "моими")
            + vf("наш", "нашими") + vf("этот", "этими") + vf("тот", "теми") + vf("весь", "всеми")
            + vf("какой", "какими") + vf("такой", "такими") + vf("собака", "собаками") + vf("машина", "машинами")),
    exercises=[
        F("Я люблю' знако'миться с ___ людьми'. (interesting)", "интере'сными", ["интере'сных", "интере'сным", "интере'сные"], "Hard stem: -ыми.", "I like to get acquainted with interesting people.", lemma="интересный"),
        F("Он интересу'ется ___ маши'нами. (expensive)", "дороги'ми", ["дороги'х", "дороги'м", "дороги'е"], "After г: -ими.", "He is interested in expensive cars.", lemma="дорогой"),
        F("Я говорю' со ___. (everyone)", "все'ми", ["всех", "всем", "все"], "Все → все'ми.", "I am speaking with everyone.", lemma="весь"),
        F("Я не интересу'юсь ___ людьми'. (those)", "те'ми", ["тех", "тем", "те"], "Те → те'ми.", "I am not interested in those people.", lemma="тот"),
        F("Мы пое'хали с ___ роди'телями. (my)", "мои'ми", ["мои'х", "мои'м", "мои'"], "Мои' → мои'ми.", "We went with my parents.", lemma="мой"),
        F("Она' гуля'ет с ___ соба'ками. (his)", "его'", ["ему'", "него'", "им"], "Его' never changes.", "She walks with his dogs."),
        F("Мы разгова'риваем с ___ студе'нтами. (these)", "э'тими", ["э'тих", "э'тим", "э'ти"], "Э'ти → э'тими.", "We talk with these students.", lemma="этот"),
        F("Мы дружи'м с ___ сосе'дями. (Russian)", "ру'сскими", ["ру'сских", "ру'сским", "ру'сские"], "After к: -ими.", "We are friends with Russian neighbors.", lemma="русский"),
        mc("Which ending do adjectives take after к, г, х, ж, ч, ш, щ in the instrumental plural?", ["-ими", "-ыми", "-ым", "-ом"], "-ими", "Spelling rule: и, not ы.", order=True),
        mc("What is the instrumental plural of все?", ["все'ми", "всех", "всем", "все'м"], "все'ми", "Все → все'ми."),
    ],
)

# ---------------------------------------------------------------------------- 210
L210 = lesson(
    "Interested in chess, proud of the children: using the instrumental plural",
    "Мама гордится свои'ми детьми'.",
    requires=["интересоваться", "заниматься", "общаться", "гордиться", "владеть"],
    cards=[
        card("With, and verbs that take the instrumental",
             "You already know the instrumental of the singular. The plural does the same jobs: with someone (с), "
             "the means or instrument, being or becoming someone, and verbs that require it.",
             tables=[table(
                 ["Verb", "Meaning", "Example"],
                 [["интересова'ться", "be interested in", "Я интересу'юсь ша'хматами."],
                  ["занима'ться", "do, study", "Он занима'ется лошадьми'."],
                  ["горди'ться", "be proud of", "Ма'ма горди'тся свои'ми детьми'."],
                  ["владе'ть", "own, speak (a language)", "Она' владе'ет иностра'нными языка'ми."],
                  ["любова'ться", "admire", "Мы любу'емся карти'нами."],
                  ["знако'миться / познако'миться с", "get acquainted with", "Он познако'мился с людьми'."],
                  ["обща'ться с", "associate with", "Я ча'сто обща'юсь с друзья'ми."]])],
             examples=[
                 ex("Я интересу'юсь ша'хматами.", "I am interested in chess.", "ша'хматами"),
                 ex("Ма'ма горди'тся свои'ми детьми'.", "Mom is proud of her children.", "свои'ми детьми'"),
                 ex("Мы любу'емся карти'нами.", "We admire the paintings.", "карти'нами"),
             ]),
        card("After над, под, перед, за, между",
             "These prepositions take the instrumental when they say where something is. The plural noun ends in "
             "-ами or -ями.",
             examples=[
                 ex("Над крова'тями вися'т карти'ны.", "Paintings hang above the beds.", "Над крова'тями"),
                 ex("Маши'ны стоя'т пе'ред дома'ми.", "Cars stand in front of the houses.", "пе'ред дома'ми"),
                 ex("Ме'жду дома'ми есть пло'щадь.", "There is a square between the buildings.", "Ме'жду дома'ми"),
                 ex("Мы стоя'ли за дере'вьями.", "We stood behind the trees.", "за дере'вьями"),
             ]),
        card("Becoming and working as",
             "After стать, рабо'тать and быть (in the past and future) the profession is in the instrumental.",
             examples=[
                 ex("Они' ста'ли врача'ми.", "They became doctors.", "врача'ми"),
                 ex("Мои' сыновья' рабо'тают инжене'рами.", "My sons work as engineers.", "инжене'рами"),
             ]),
    ],
    verify=(vf("интересоваться", "интересуюсь") + vf("шахматы", "шахматами") + vf("гордиться", "гордится")
            + vf("владеть", "владеет") + vf("языки", "языками") + vf("любоваться", "любуемся") + vf("картина", "картинами")
            + vf("познакомиться", "познакомился") + vf("общаться", "общаюсь") + vf("кровать", "кроватями")
            + vf("дом", "домами") + vf("площадь", "площадь") + vf("дерево", "деревьями") + vf("стать", "стали")
            + vf("врач", "врачами") + vf("инженер", "инженерами") + vf("сын", "сыновья") + vf("лошадь", "лошадьми")
            + vf("заниматься", "занимается")),
    exercises=[
        F("Я интересу'юсь ___. (chess)", "ша'хматами", ["ша'хматы", "ша'хматам", "ша'хмат"], "Интересова'ться + instrumental.", "I am interested in chess."),
        F("Ма'ма горди'тся ___. (her children)", "детьми'", ["дете'й", "де'ти", "де'тям"], "Горди'ться + instrumental.", "Mom is proud of her children.", lemma="ребёнок"),
        F("Мы любу'емся ___. (the paintings)", "карти'нами", ["карти'ны", "карти'н", "карти'нам"], "Любова'ться + instrumental.", "We admire the paintings.", lemma="картина"),
        F("Над ___ вися'т карти'ны. (beds)", "крова'тями", ["крова'ти", "крова'тей", "крова'тях"], "Над + instrumental.", "Paintings hang above the beds.", lemma="кровать"),
        F("Маши'ны стоя'т пе'ред ___. (houses)", "дома'ми", ["дома'", "домо'в", "дома'м"], "Пе'ред + instrumental.", "Cars stand in front of the houses.", lemma="дом"),
        F("Они' стали ___. (doctors)", "врача'ми", ["врачи'", "враче'й", "врача'м"], "Стать + instrumental.", "They became doctors.", lemma="врач"),
        F("Она' владе'ет иностра'нными ___. (languages)", "языка'ми", ["языки'", "языко'в", "языка'м"], "Владе'ть + instrumental.", "She speaks foreign languages.", lemma="язык"),
        F("Мы живём вме'сте с ___. (parents)", "роди'телями", ["роди'тели", "роди'телям", "роди'телей"], "С + instrumental.", "We live together with our parents.", lemma="родитель"),
        mc("Which preposition does NOT take the instrumental?", ["без", "над", "под", "пе'ред"], "без", "Без takes the genitive."),
        mc("What case follows горди'ться?", ["instrumental", "genitive", "dative", "accusative"], "instrumental", "Горди'ться + instrumental."),
    ],
)

# ---------------------------------------------------------------------------- 211
L211 = lesson(
    "They say, they sell, they called: indefinite-personal sentences",
    "Говоря'т, что он ско'ро же'нится.",
    requires=["говорить", "сказать", "рассказывать", "принимать", "квартира"],
    cards=[
        card("No subject, “they” verb",
             "When you do not say who does something, or it does not matter, Russian uses the third person plural of "
             "the verb and no subject. English uses “they”, “people” or the passive.",
             tables=[table(
                 ["Russian", "English"],
                 [["Говоря'т, что он ско'ро же'нится.", "They say he will get married soon."],
                  ["Здесь продаю'т биле'ты.", "Tickets are sold here."],
                  ["Мне позвони'ли из ба'нка.", "Someone called me from the bank."],
                  ["Его' не при'няли в университе'т.", "He was not admitted to the university."],
                  ["В Росси'и пьют мно'го ча'я.", "In Russia people drink a lot of tea."],
                  ["В на'шем до'ме не устра'ивают вечери'нок.", "In our building people do not hold parties."]])],
             examples=[
                 ex("Говоря'т, что за'втра бу'дет дождь.", "They say it will rain tomorrow.", "Говоря'т"),
                 ex("Здесь продаю'т биле'ты.", "Tickets are sold here.", "продаю'т"),
                 ex("Мне позвони'ли из ба'нка.", "Someone called me from the bank.", "позвони'ли"),
             ]),
        card("Tense and negation",
             "In the past tense use the plural form in -ли. With a negative, a direct object goes into the genitive, as "
             "you saw with вечери'нок.",
             examples=[
                 ex("Его' не при'няли в университе'т.", "He was not admitted to the university.", "не при'няли"),
                 ex("В на'шем до'ме не устра'ивают вечери'нок.", "In our building people do not hold parties.", "не устра'ивают вечери'нок"),
                 ex("Здесь не ку'рят.", "People do not smoke here.", "не ку'рят"),
             ]),
    ],
    verify=(vf("говорить", "говорят") + vf("жениться", "женится") + vf("продавать", "продают") + vf("билет", "билеты")
            + vf("позвонить", "позвонили") + vf("банк", "банка") + vf("принять", "приняли") + vf("университет", "университет")
            + vf("пить", "пьют") + vf("чай", "чая") + vf("устраивать", "устраивают") + vf("вечеринка", "вечеринок")
            + vf("курить", "курят") + vf("дождь", "дождь") + vf("готовить", "готовят")),
    exercises=[
        F("___, что он ско'ро же'нится. (They say)", "Говоря'т", ["Говори'т", "Говорю'", "Говори'л"], "3rd person plural.", "They say he is getting married soon."),
        F("В э'том кафе' хорошо' ___. (they cook)", "гото'вят", ["гото'вит", "гото'влю", "гото'вила"], "3rd person plural.", "They cook well in this café."),
        F("Здесь не ___. (people don't smoke)", "ку'рят", ["ку'рит", "курю'", "ку'рила"], "3rd person plural.", "People do not smoke here."),
        F("Его' не ___ в университе'т. (admitted)", "при'няли", ["при'нял", "приняла'", "при'няло"], "Past plural, no subject.", "He was not admitted to the university."),
        F("Мне ___ из ба'нка. (someone called)", "позвони'ли", ["позвони'л", "позвони'ла", "позвони'ло"], "Past plural, no subject.", "Someone called me from the bank."),
        F("Здесь ___ биле'ты. (they sell)", "продаю'т", ["продаёт", "продаю'", "продаём"], "3rd person plural.", "Tickets are sold here."),
        F("В Росси'и ___ мно'го ча'я. (people drink)", "пьют", ["пьёт", "пью", "пьём"], "3rd person plural.", "In Russia people drink a lot of tea."),
        F("В на'шем до'ме не ___ вечери'нок. (hold)", "устра'ивают", ["устра'ивает", "устра'иваю", "устра'иваем"], "3rd person plural.", "In our building people do not hold parties."),
        mc("In an indefinite-personal sentence the verb is in the...", ["3rd person plural", "3rd person singular", "1st person plural", "infinitive"], "3rd person plural", "No subject; the they-form."),
        mc("How do you say “They say it will rain”?", ["Говоря'т, что бу'дет дождь.", "Он говори'т, что бу'дет дождь.", "Говори'ть, что бу'дет дождь.", "Я говорю', что бу'дет дождь."], "Говоря'т, что бу'дет дождь.", "Говоря'т = they say."),
    ],
)

# ---------------------------------------------------------------------------- 212
L212 = lesson(
    "Review: home, the instrumental plural and “they say”",
    "Мы живём в просто'рной кварти'ре с хоро'шими сосе'дями.",
    requires=["дом", "друг", "интересоваться", "говорить", "хороший"],
    cards=[
        card("The instrumental plural in one table",
             "Memorize the five endings. Everything else is a special case.",
             tables=[table(
                 ["Part of speech", "Hard", "Soft or к г х ж ч ш щ"],
                 [["Nouns", "-ами", "-ями (-ами after к г х ж ч ш щ ц)"],
                  ["Adjectives", "-ыми", "-ими"],
                  ["Special nouns", "людьми', детьми', дочерьми', матеря'ми", ""],
                  ["Pronouns", "те'ми, все'ми, его', её, их", "—"]])],
             examples=[
                 ex("Мы живём в просто'рной кварти'ре с хоро'шими сосе'дями.", "We live in a spacious apartment with good neighbors.", "с хоро'шими сосе'дями"),
             ]),
    ],
    verify=(vf("хороший", "хорошими") + vf("сосед", "соседями") + vf("просторный", "просторной") + vf("квартира", "квартире")
            + vf("друг", "друзьями") + vf("интересоваться", "интересуется") + vf("продавать", "продают")),
    exercises=[
        F("Мы живём с хоро'шими ___. (neighbors)", "сосе'дями", ["сосе'дям", "сосе'дей", "сосе'дях"], "Soft stem: -ями.", "We live next to good neighbors.", lemma="сосед"),
        F("Я ча'сто гуля'ю с ___. (friends)", "друзья'ми", ["друзья'м", "друзе'й", "друзья'х"], "Друзья' → друзья'ми.", "I often walk with my friends.", lemma="друг"),
        F("Она' разгова'ривает с ___. (children)", "детьми'", ["де'тями", "дета'ми", "дете'й"], "Special: детьми'.", "She talks with the children.", lemma="ребёнок"),
        F("Мы разгова'риваем со ___. (everyone)", "все'ми", ["всех", "всем", "все"], "Все → все'ми.", "We talk with everyone.", lemma="весь"),
        F("Он интересу'ется ___ маши'нами. (expensive)", "дороги'ми", ["дороги'х", "дороги'м", "дороги'е"], "After г: -ими.", "He is interested in expensive cars.", lemma="дорогой"),
        F("Ковёр лежи'т на ___. (the floor)", "полу'", ["пол", "по'ла", "по'лы"], "На полу'.", "The rug lies on the floor.", lemma="пол"),
        F("Мы подписа'ли ___ аре'нды. (agreement)", "догово'р", ["догово'ра", "догово'ру", "догово'ре"], "Подписа'ть догово'р.", "We signed the lease.", lemma="договор"),
        F("Говоря'т, что здесь ___ биле'ты. (they sell)", "продаю'т", ["продаёт", "продаю'", "продаём"], "3rd person plural.", "They say tickets are sold here."),
        F("Э'та кварти'ра меня' ___. (suits)", "устра'ивает", ["снима'ет", "сдаёт", "запреща'ет"], "Устра'ивать = suit.", "This apartment suits me."),
        F("Ма'ма горди'тся ___. (her daughters)", "дочерьми'", ["дочеря'м", "дочеря'х", "дочере'й"], "Special: дочерьми'.", "Mom is proud of her daughters.", lemma="дочь"),
        mc("Which preposition takes the genitive?", ["напро'тив", "над", "за", "ме'жду"], "напро'тив", "Напро'тив + genitive."),
    ],
)

UNIT = unit("Unit 22: Home, furniture and the instrumental plural",
            [L204, L205, L206, L207, L208, L209, L210, L211, L212])
