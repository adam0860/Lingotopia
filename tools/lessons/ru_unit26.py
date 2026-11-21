"""Unit 26: mail, internet and social networks; recognising participles
(textbook module 6, lesson 34)."""
from dsl import *


def F(prompt, ans, wrong, why, tr, lemma=None):
    return fb(prompt, [ans] + list(wrong), ans, why, tr=tr, lemma=lemma)


# ---------------------------------------------------------------------------- 246
L246 = lesson(
    "At the post office: письмо', откры'тка, посы'лка, ма'рка",
    "Мне ну'жно отпра'вить посы'лку в Каза'нь.",
    requires=["почта", "письмо", "марка", "адрес", "индекс"],
    cards=[
        card("What you send and receive",
             "A basic vocabulary for the post office.",
             tables=[table(
                 ["Word", "English"],
                 [["по'чта", "mail; post office"],
                  ["письмо'", "letter"],
                  ["откры'тка", "postcard"],
                  ["посы'лка", "parcel"],
                  ["конве'рт", "envelope"],
                  ["ма'рка", "stamp"],
                  ["а'дрес (pl. адреса')", "address"],
                  ["и'ндекс", "postal code"],
                  ["почто'вый я'щик", "mailbox"],
                  ["почтальо'н", "mail carrier"]])],
             examples=[
                 ex("Мне ну'жно отпра'вить посы'лку в Каза'нь.", "I need to send a parcel to Kazan.", "отпра'вить посы'лку"),
                 ex("Я купи'л ма'рки и конве'рты.", "I bought stamps and envelopes.", "ма'рки и конве'рты"),
                 ex("Како'й у вас и'ндекс?", "What is your postal code?", "и'ндекс"),
             ]),
        card("Writing an address",
             "Russian addresses go from the specific to the general in the order: country, postal code, city, street, "
             "building, apartment, name. On a letter you also see the words получа'тель (addressee) and "
             "отправи'тель (sender).",
             tables=[table(
                 ["Word", "English"],
                 [["получа'тель", "addressee"],
                  ["отправи'тель", "sender"],
                  ["у'лица", "street"],
                  ["дом", "building"],
                  ["кварти'ра", "apartment"]])],
             examples=[
                 ex("Напиши' а'дрес на конве'рте.", "Write the address on the envelope.", "а'дрес на конве'рте"),
                 ex("В почто'вом я'щике лежи'т письмо'.", "A letter is lying in the mailbox.", "В почто'вом я'щике"),
             ]),
        card("At the counter",
             "Useful phrases for sending something.",
             tables=[table(
                 ["Phrase", "English"],
                 [["Ско'лько сто'ит отпра'вить?", "How much does it cost to send?"],
                  ["Когда' придёт посы'лка?", "When will the parcel arrive?"],
                  ["Мне ну'жно посла'ть письмо'.", "I need to send a letter."],
                  ["Отпра'вьте сро'чно.", "Send it urgently."]])],
             examples=[
                 ex("Ско'лько сто'ит отпра'вить письмо' в Москву'?", "How much does it cost to send a letter to Moscow?", "Ско'лько сто'ит"),
             ]),
    ],
    verify=(vf("почта", "почта") + vf("письмо", "письмо") + vf("марка", "марки") + vf("адрес", "адрес", "адреса")
            + vf("индекс", "индекс") + vf("конверт", "конверты", "конверте") + vf("посылка", "посылку")
            + vf("отправить", "отправить") + vf("ящик", "ящике") + vf("улица", "улица") + vf("дом", "дом")
            + vf("квартира", "квартира") + vf("лежать", "лежит") + vf("стоить", "стоит") + vf("прийти", "придёт")
            + vf("послать", "послать")),
    exercises=[
        F("Мне ну'жно отпра'вить ___ в Каза'нь. (a parcel)", "посы'лку", ["посы'лка", "посы'лки", "посы'лке"], "Accusative after отпра'вить.", "I need to send a parcel to Kazan.", lemma="посылка"),
        F("Я купи'л ___ и конве'рты. (stamps)", "ма'рки", ["ма'рка", "ма'рку", "ма'рок"], "Accusative plural, inanimate.", "I bought stamps and envelopes.", lemma="марка"),
        F("Како'й у вас ___? (postal code)", "и'ндекс", ["и'ндекса", "и'ндексу", "и'ндексе"], "Nominative.", "What is your postal code?", lemma="индекс"),
        F("Напиши' а'дрес на ___. (the envelope)", "конве'рте", ["конве'рт", "конве'рта", "конве'ртом"], "На + prepositional: where?", "Write the address on the envelope.", lemma="конверт"),
        F("В почто'вом ___ лежи'т письмо'. (mailbox)", "я'щике", ["я'щик", "я'щика", "я'щиком"], "В + prepositional: where?", "A letter is lying in the mailbox.", lemma="ящик"),
        F("Ско'лько ___ отпра'вить письмо'? (does it cost)", "сто'ит", ["стоя'т", "сто'ить", "стоя'л"], "Third person singular.", "How much does it cost to send a letter?", lemma="стоить"),
        mc("Which word means ‘postcard’?", ["откры'тка", "конве'рт", "посы'лка", "ма'рка"], "откры'тка", "Откры'тка = postcard.", order=True),
        mc("Who sends the parcel?", ["отправи'тель", "получа'тель", "почтальо'н", "курье'р"], "отправи'тель", "Отправи'тель = sender.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 247
L247 = lesson(
    "Sending and delivery: отпра'вить, получи'ть, доста'вить",
    "Посы'лку доста'вят за три дня.",
    requires=["отправить", "получить", "доставка", "срочно", "сообщение"],
    cards=[
        card("Verbs of the post",
             "Each of these verbs comes in an aspect pair. Use the imperfective for a process or habit and the "
             "perfective for a single completed action.",
             tables=[table(
                 ["Imperfective", "Perfective", "Meaning"],
                 [["отправля'ть", "отпра'вить", "to send"],
                  ["получа'ть", "получи'ть", "to receive"],
                  ["доставля'ть", "доста'вить", "to deliver"],
                  ["присыла'ть", "присла'ть", "to send (to me)"],
                  ["пересыла'ть", "пересла'ть", "to forward"]])],
             examples=[
                 ex("Я вчера' отпра'вил посы'лку.", "I sent a parcel yesterday.", "отпра'вил"),
                 ex("Мы получи'ли письмо' от ба'бушки.", "We received a letter from Grandma.", "получи'ли"),
                 ex("Курье'р доставля'ет посы'лки.", "The courier delivers parcels.", "доставля'ет"),
             ]),
        card("Delivery times and messages",
             "A few words you will see on tracking pages and in notifications.",
             tables=[table(
                 ["Word", "English"],
                 [["доста'вка", "delivery"],
                  ["сро'чно", "urgently"],
                  ["бы'стро", "quickly"],
                  ["сообще'ние", "message"],
                  ["отсле'живать", "to track"],
                  ["в пути'", "on the way"]])],
             examples=[
                 ex("Доста'вка занима'ет три дня.", "Delivery takes three days.", "Доста'вка"),
                 ex("Посы'лка уже' в пути'.", "The parcel is already on its way.", "в пути'"),
                 ex("Я получи'л сообще'ние от ба'нка.", "I got a message from the bank.", "сообще'ние"),
             ]),
        card("Присла'ть, посла'ть, отпра'вить",
             "Посла'ть and отпра'вить are close in meaning. Присла'ть means that the thing is sent to the speaker or "
             "to the person you are talking about: Пришли' мне фо'то.",
             examples=[
                 ex("Пришли' мне фо'то, пожа'луйста.", "Send me the photo, please.", "Пришли'"),
                 ex("Когда' ты отпра'вишь письмо'?", "When will you send the letter?", "отпра'вишь"),
             ]),
    ],
    verify=(vf("отправить", "отправил", "отправишь") + vf("получить", "получили", "получил") + vf("доставлять", "доставляет")
            + vf("доставить", "доставят") + vf("присылать", "присылать") + vf("прислать", "прислать")
            + vf("доставка", "доставка") + vf("срочно", "срочно") + vf("быстро", "быстро") + vf("сообщение", "сообщение")
            + vf("посылка", "посылки", "посылка") + vf("курьер", "курьер") + vf("фото", "фото")
            + vf("бабушка", "бабушки") + vf("банк", "банка")),
    exercises=[
        F("Я вчера' ___ посы'лку. (sent)", "отпра'вил", ["отправля'л", "отпра'вит", "отпра'вить"], "One completed action: perfective.", "I sent a parcel yesterday.", lemma="отправить"),
        F("Мы ___ письмо' от ба'бушки. (received)", "получи'ли", ["получа'ем", "получи'ть", "получи'т"], "Past tense, plural.", "We received a letter from Grandma.", lemma="получить"),
        F("Курье'р ___ посы'лки. (delivers)", "доставля'ет", ["доста'вит", "доста'вил", "доста'вить"], "A habit: imperfective.", "The courier delivers parcels.", lemma="доставлять"),
        F("___ занима'ет три дня. (delivery)", "Доста'вка", ["Доста'вки", "Доста'вку", "Доста'вке"], "Nominative subject.", "Delivery takes three days.", lemma="доставка"),
        F("Отпра'вьте ___. (urgently)", "сро'чно", ["сро'чный", "сро'чная", "сро'чное"], "An adverb: сро'чно.", "Send it urgently.", lemma="срочно"),
        F("Я получи'л ___ от ба'нка. (a message)", "сообще'ние", ["сообще'ния", "сообще'нию", "сообще'нии"], "Accusative = nominative for neuter.", "I got a message from the bank.", lemma="сообщение"),
        mc("‘To receive’ (once) is:", ["получи'ть", "получа'ть", "отпра'вить", "доста'вить"], "получи'ть", "Perfective получи'ть.", order=True),
        mc("What does ‘в пути'’ mean?", ["on the way", "at home", "in the mailbox", "returned"], "on the way", "В пути' = on the way."),
    ],
)

# ---------------------------------------------------------------------------- 248
L248 = lesson(
    "Internet and computer: сайт, ссы'лка, файл, паро'ль",
    "Введи' паро'ль и откро'й сайт.",
    requires=["интернет", "сайт", "ссылка", "файл", "пароль"],
    cards=[
        card("Words for the web",
             "The core vocabulary of the internet.",
             tables=[table(
                 ["Word", "English"],
                 [["интерне'т", "internet"],
                  ["сайт", "website"],
                  ["страни'ца", "page"],
                  ["ссы'лка", "link"],
                  ["файл", "file"],
                  ["паро'ль (m.)", "password"],
                  ["компью'тер", "computer"],
                  ["приложе'ние", "app"],
                  ["экра'н", "screen"],
                  ["по'льзователь", "user"]])],
             examples=[
                 ex("Э'тот сайт о'чень популя'рный.", "This website is very popular.", "сайт"),
                 ex("Нажми' на ссы'лку.", "Click on the link.", "ссы'лку"),
                 ex("Я забы'л паро'ль.", "I forgot my password.", "паро'ль"),
             ]),
        card("What you do online",
             "These verbs often come in aspect pairs.",
             tables=[table(
                 ["Verb", "English"],
                 [["заходи'ть / зайти' на сайт", "to visit a website"],
                  ["открыва'ть / откры'ть страни'цу", "to open a page"],
                  ["ска'чивать / скача'ть файл", "to download a file"],
                  ["вводи'ть / ввести' паро'ль", "to enter a password"],
                  ["включа'ть / включи'ть компью'тер", "to turn on a computer"],
                  ["выключа'ть / вы'ключить", "to turn off"]])],
             examples=[
                 ex("Введи' паро'ль и откро'й сайт.", "Enter the password and open the site.", "Введи'"),
                 ex("Я скача'л э'тот файл вчера'.", "I downloaded this file yesterday.", "скача'л"),
                 ex("Он зашёл на сайт ба'нка.", "He went onto the bank's website.", "зашёл на сайт"),
             ]),
        card("Typical sentences",
             "On a website you meet short instructions. Notice the imperative.",
             tables=[table(
                 ["Instruction", "English"],
                 [["Введи'те а'дрес.", "Enter your address."],
                  ["Нажми'те на ссы'лку.", "Click on the link."],
                  ["Сохрани'те файл.", "Save the file."],
                  ["Зарегистри'руйтесь.", "Register."]])],
             examples=[
                 ex("Сохрани'те файл на компью'тере.", "Save the file on your computer.", "Сохрани'те"),
             ]),
    ],
    verify=(vf("интернет", "интернет") + vf("сайт", "сайт") + vf("страница", "страница", "страницу") + vf("ссылка", "ссылку")
            + vf("файл", "файл") + vf("пароль", "пароль") + vf("компьютер", "компьютер", "компьютере")
            + vf("приложение", "приложение") + vf("экран", "экран") + vf("пользователь", "пользователь")
            + vf("забыть", "забыл") + vf("зайти", "зашёл") + vf("открыть", "открой") + vf("ввести", "введи")
            + vf("скачать", "скачал") + vf("популярный", "популярный") + vf("банк", "банка")),
    exercises=[
        F("Э'тот ___ о'чень популя'рный. (website)", "сайт", ["сайта", "сайту", "сайте"], "Nominative subject.", "This website is very popular.", lemma="сайт"),
        F("Нажми' на ___. (the link)", "ссы'лку", ["ссы'лка", "ссы'лки", "ссы'лке"], "На + accusative: нажа'ть на что.", "Click on the link.", lemma="ссылка"),
        F("Я забы'л ___. (the password)", "паро'ль", ["паро'ля", "паро'лю", "паро'ле"], "Accusative = nominative for inanimate masculine.", "I forgot my password.", lemma="пароль"),
        F("___ паро'ль и откро'й сайт. (enter!)", "Введи'", ["Войди'", "Выведи'", "Приведи'"], "Ввести' паро'ль.", "Enter the password and open the site.", lemma="ввести"),
        F("Я ___ э'тот файл вчера'. (downloaded)", "скача'л", ["скачиваю", "скача'ть", "скача'ет"], "Past perfective.", "I downloaded this file yesterday.", lemma="скачать"),
        F("Он ___ на сайт ба'нка. (went onto)", "зашёл", ["вошёл", "вышел", "ушёл"], "Зайти' на сайт: visit a website.", "He went onto the bank's website.", lemma="зайти"),
        mc("Which word means ‘link’?", ["ссы'лка", "страни'ца", "файл", "сайт"], "ссы'лка", "Ссы'лка = link.", order=True),
        mc("What do you do with a password?", ["ввести' его'", "скача'ть его'", "включи'ть его'", "послать его' по по'чте"], "ввести' его'", "Ввести' паро'ль."),
    ],
)

# ---------------------------------------------------------------------------- 249
L249 = lesson(
    "Social networks and phones: про'филь, коммента'рий, фо'то",
    "Я вы'ложил фо'то и получи'л мно'го коммента'риев.",
    requires=["сеть", "пользователь", "комментарий", "профиль", "блог"],
    cards=[
        card("Social networks",
             "The word for ‘social network’ is социа'льная сеть (often shortened to соцсе'ть).",
             tables=[table(
                 ["Word", "English"],
                 [["социа'льная сеть", "social network"],
                  ["про'филь (m.)", "profile"],
                  ["коммента'рий", "comment"],
                  ["блог", "blog"],
                  ["фо'то", "photo"],
                  ["ви'део", "video"],
                  ["по'льзователь", "user"],
                  ["страни'ца", "page"]])],
             examples=[
                 ex("У меня' страни'ца в социа'льной се'ти.", "I have a page in a social network.", "в социа'льной се'ти"),
                 ex("Э'тот блог чита'ют ты'сячи люде'й.", "Thousands of people read this blog.", "блог"),
             ]),
        card("What you do there",
             "Common verbs and phrases for posting and reading.",
             tables=[table(
                 ["Phrase", "English"],
                 [["вы'ложить фо'то", "to post a photo"],
                  ["написа'ть коммента'рий", "to write a comment"],
                  ["подписа'ться на + acc.", "to follow, subscribe to"],
                  ["поста'вить лайк", "to like"],
                  ["отве'тить на сообще'ние", "to reply to a message"]])],
             examples=[
                 ex("Я вы'ложил фо'то и получи'л мно'го коммента'риев.", "I posted a photo and got many comments.", "коммента'риев"),
                 ex("Она' подписа'лась на мой блог.", "She subscribed to my blog.", "подписа'лась на мой блог"),
             ]),
        card("The phone",
             "Words you need for a mobile phone.",
             tables=[table(
                 ["Word", "English"],
                 [["телефо'н", "phone"],
                  ["смартфо'н", "smartphone"],
                  ["звоно'к", "call; ring"],
                  ["ка'мера", "camera"],
                  ["сни'мок", "snapshot"],
                  ["фотографи'ровать", "to photograph"]])],
             examples=[
                 ex("Мне позвони'ли с незнако'мого но'мера.", "I got a call from an unknown number.", "позвони'ли"),
                 ex("Э'ту фотогра'фию я сде'лал на телефо'н.", "I took this photo with my phone.", "на телефо'н"),
             ]),
    ],
    verify=(vf("сеть", "сети") + vf("профиль", "профиль") + vf("комментарий", "комментарий", "комментариев")
            + vf("блог", "блог") + vf("фото", "фото") + vf("видео", "видео") + vf("пользователь", "пользователь")
            + vf("страница", "страница") + vf("телефон", "телефон") + vf("смартфон", "смартфон")
            + vf("камера", "камера") + vf("снимок", "снимок") + vf("звонок", "звонок")
            + vf("выложить", "выложил") + vf("получить", "получил") + vf("подписаться", "подписалась")
            + vf("позвонить", "позвонили") + vf("незнакомый", "незнакомого") + vf("номер", "номера")
            + vf("сделать", "сделал") + vf("фотография", "фотографию")),
    exercises=[
        F("У меня' страни'ца в социа'льной ___. (network)", "се'ти", ["сеть", "сетью", "сетей"], "В + prepositional: се'ти.", "I have a page in a social network.", lemma="сеть"),
        F("Я вы'ложил фо'то и получи'л мно'го ___. (comments)", "коммента'риев", ["комментарии", "коммента'рий", "комментарию"], "Мно'го + genitive plural.", "I posted a photo and got many comments.", lemma="комментарий"),
        F("Она' подписа'лась ___ мой блог. (to)", "на", ["в", "к", "о"], "Подписа'ться на + accusative.", "She subscribed to my blog."),
        F("Э'тот ___ чита'ют ты'сячи люде'й. (blog)", "блог", ["блога", "блогу", "блоге"], "Accusative = nominative for inanimate.", "Thousands of people read this blog.", lemma="блог"),
        F("Мне позвони'ли с незнако'мого ___. (number)", "но'мера", ["но'мер", "но'меру", "но'мере"], "С + genitive.", "I got a call from an unknown number.", lemma="номер"),
        F("Э'ту фотогра'фию я сде'лал на ___. (phone)", "телефо'н", ["телефо'на", "телефо'ну", "телефо'не"], "На + accusative: what did I take it on?", "I took this photo with my phone.", lemma="телефон"),
        mc("Which word means ‘a user’?", ["по'льзователь", "блог", "про'филь", "коммента'рий"], "по'льзователь", "По'льзователь = user.", order=True),
        mc("‘To subscribe to a blog’ is:", ["подписа'ться на блог", "подписа'ть блог", "подписа'ться блог", "подписа'ться с блогом"], "подписа'ться на блог", "Подписа'ться на + accusative."),
    ],
)

# ---------------------------------------------------------------------------- 250
L250 = lesson(
    "Adjectives made from verbs: what is a participle?",
    "Э'то мой люби'мый писа'тель.",
    requires=["любимый", "бывший", "открыть", "закрыть", "писатель"],
    cards=[
        card("You already know some",
             "Look at these words you have met: люби'мый (favorite), бы'вший (former), закры'тый (closed), "
             "за'нятый (busy). They look like adjectives, because they have adjective endings. But each one is built "
             "from a verb: люби'мый from люби'ть, бы'вший from быть, закры'тый from закры'ть. Such a word is a participle "
             "(прича'стие in Russian; the root is the same as in часть, ‘part’, because it takes part in both a verb "
             "and an adjective).",
             tables=[table(
                 ["Participle", "From the verb", "Meaning"],
                 [["люби'мый", "люби'ть", "loved, favorite"],
                  ["бы'вший", "быть", "former"],
                  ["закры'тый", "закры'ть", "closed"],
                  ["откры'тый", "откры'ть", "open"],
                  ["за'нятый", "заня'ть", "busy; taken"],
                  ["чита'ющий", "чита'ть", "reading"]])],
             examples=[
                 ex("Э'то мой люби'мый писа'тель.", "This is my favorite writer.", "люби'мый"),
                 ex("Бы'вший президе'нт живёт в Москве'.", "The former president lives in Moscow.", "Бы'вший"),
                 ex("Дверь закры'та, а окно' откры'то.", "The door is closed, but the window is open.", "закры'та"),
             ]),
        card("Two things a participle shows",
             "A participle says what the action is, and it also tells you two more things. Is the action happening now "
             "(present) or was it earlier (past)? Is the noun doing the action (active) or is something being done to "
             "the noun (passive)? English has participles too: ‘the stolen money’ is past passive, ‘a fire-breathing "
             "dragon’ is present active.",
             tables=[table(
                 ["English", "Tense", "Voice"],
                 [["the stolen money", "past", "passive"],
                  ["a sleeping child", "present", "active"],
                  ["a closed door", "past", "passive"],
                  ["the winning team", "present", "active"]])],
             examples=[
                 ex("Спя'щий ребёнок не слы'шит шум.", "The sleeping child does not hear the noise.", "Спя'щий"),
             ]),
        card("Where do you meet them?",
             "Participles are common in news, books, signs and official language, and less common in everyday "
             "speech. In this unit you will learn to recognise them; you do not need to build them yet.",
             examples=[
                 ex("Вот письмо', напи'санное вчера'.", "Here is a letter written yesterday.", "напи'санное"),
             ]),
    ],
    verify=(vf("любить", "любимый") + vf("быть", "бывший") + vf("закрытый", "закрытый") + vf("открытый", "открытый")
            + vf("занять", "занятый") + vf("читать", "читающий") + vf("писатель", "писатель")
            + vf("президент", "президент") + vf("спать", "спящий") + vf("ребёнок", "ребёнок")
            + vf("письмо", "письмо") + vf("окно", "окно") + vf("дверь", "дверь") + vf("Москва", "Москве")),
    exercises=[
        mc("Which verb does люби'мый come from?", ["люби'ть", "быть", "жить", "писа'ть"], "люби'ть", "Люби'мый = loved.", order=True),
        mc("Which verb does бы'вший come from?", ["быть", "бить", "брать", "есть"], "быть", "Бы'вший = one who used to be."),
        F("Э'то мой ___ писа'тель. (favorite)", "люби'мый", ["любо'вь", "люблю'", "люби'ть"], "A participle agreeing with писа'тель.", "This is my favorite writer."),
        F("___ президе'нт живёт в Москве'. (former)", "Бы'вший", ["Бу'дущий", "Сле'дующий", "Настоя'щий"], "Бы'вший = former.", "The former president lives in Moscow."),
        F("___ ребёнок не слы'шит шум. (sleeping)", "Спя'щий", ["Спать", "Спит", "Спал"], "A participle agrees with ребёнок.", "The sleeping child does not hear the noise."),
        F("Э'то ___ письмо'. (written)", "напи'санное", ["напи'санный", "напи'санная", "напи'санные"], "Neuter: письмо'.", "This is a written letter."),
        mc("What is a participle?", ["an adjective formed from a verb", "a verb formed from a noun", "a short form of a noun", "a preposition"], "an adjective formed from a verb", "It shows an action and a tense."),
        mc("Which word is a participle?", ["люби'мый", "ма'ленький", "но'вый", "хоро'ший"], "люби'мый", "Люби'мый is formed from люби'ть.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 251
L251 = lesson(
    "Four types: present or past, active or passive",
    "Чита'ющий, чита'емый, чита'вший, прочи'танный.",
    requires=["читать", "писать", "любить", "закрыть", "бывший"],
    cards=[
        card("Two questions, four types",
             "Ask two questions about any participle. When did the action happen: now (present) or earlier (past)? "
             "Who does the action: the noun itself (active) or somebody else (passive)? The answers give four types.",
             tables=[table(
                 ["", "Active (the noun acts)", "Passive (the noun is acted on)"],
                 [["Present", "чита'ющий", "чита'емый"],
                  ["Past", "чита'вший, прочита'вший", "прочи'танный"]])],
             examples=[
                 ex("Студе'нт, чита'ющий кни'гу, сиди'т у окна'.", "The student who is reading a book is sitting by the window.", "чита'ющий"),
                 ex("Кни'га, прочи'танная студе'нтом, лежи'т на столе'.", "The book read by the student is lying on the table.", "прочи'танная"),
             ]),
        card("How to recognise them",
             "Look at the suffix just before the ending:",
             tables=[table(
                 ["Suffix", "Type", "Example"],
                 [["-ущ- / -ющ- / -ащ- / -ящ-", "present active", "чита'ющий, говоря'щий"],
                  ["-вш- / -ш-", "past active", "чита'вший, уше'дший"],
                  ["-ем- / -им-", "present passive", "чита'емый, люби'мый"],
                  ["-нн- / -енн- / -т-", "past passive", "прочи'танный, закры'тый"]])],
             examples=[
                 ex("Бы'вший президе'нт живёт в Москве'.", "The former president lives in Moscow.", "Бы'вший"),
             ]),
        card("English translations",
             "Literal translations show the type well.",
             tables=[table(
                 ["Participle", "Type", "Rough English"],
                 [["чита'ющий", "present active", "that is reading"],
                  ["чита'емый", "present passive", "that is being read"],
                  ["чита'вший", "past active", "that was reading"],
                  ["прочита'вший", "past active", "that had read"],
                  ["прочи'танный", "past passive", "that has been read"]])],
             examples=[
                 ex("Э'то мой люби'мый писа'тель.", "This is my favorite writer.", "люби'мый"),
             ]),
    ],
    verify=(vf("читать", "читающий", "читаемый", "читавший") + vf("прочитать", "прочитанный")
            + vf("любить", "любимый") + vf("уйти", "ушедший") + vf("говорить", "говорящий") + vf("закрытый", "закрытый")
            + vf("быть", "бывший") + vf("студент", "студент", "студентом") + vf("книга", "книгу", "книга")
            + vf("сидеть", "сидит") + vf("лежать", "лежит") + vf("стол", "столе")),
    exercises=[
        mc("What type is чита'ющий?", ["present active", "present passive", "past active", "past passive"], "present active", "-ющ- = present active.", order=True),
        mc("What type is чита'емый?", ["present passive", "present active", "past active", "past passive"], "present passive", "-ем- = present passive.", order=True),
        mc("What type is чита'вший?", ["past active", "present active", "present passive", "past passive"], "past active", "-вш- = past active.", order=True),
        mc("What type is прочи'танный?", ["past passive", "past active", "present active", "present passive"], "past passive", "-нн- = past passive.", order=True),
        mc("Which suffix signals an active participle?", ["-щ- or -ш-", "-м- or -нн-", "-ть", "-л-"], "-щ- or -ш-", "Active: щ / ш.", order=True),
        mc("Which suffix signals a passive participle?", ["-м-, -нн- or -т-", "-щ- or -ш-", "-ся", "-л-"], "-м-, -нн- or -т-", "Passive: м / нн / т.", order=True),
        mc("‘A book that has been read’ is:", ["прочи'танная кни'га", "чита'ющая кни'га", "чита'вшая кни'га", "чита'емая кни'га"], "прочи'танная кни'га", "The book is acted on, and the action is finished: past passive.", order=True),
        mc("‘A student who is reading’ is:", ["чита'ющий студе'нт", "чита'емый студе'нт", "прочи'танный студе'нт", "чита'вшая студе'нт"], "чита'ющий студе'нт", "The student acts, now: present active.", order=True),
        mc("What does бы'вший describe?", ["a past active participle", "a present passive participle", "a noun", "a verb"], "a past active participle", "Бы'вший = former (one who was)."),
    ],
)

# ---------------------------------------------------------------------------- 252
L252 = lesson(
    "Present active: чита'ющий, пи'шущий, говоря'щий",
    "Студе'нты, изуча'ющие ру'сский, живу'т в общежи'тии.",
    requires=["читать", "писать", "говорить", "жить", "спать"],
    cards=[
        card("From the они'-form",
             "A present active participle describes a noun that is doing the action right now. Take the они'-form of the "
             "verb, drop -т, and add -щий. First conjugation gives -ущий / -ющий; second conjugation gives -ащий / -ящий. "
             "The stress usually stays where it is in the они'-form.",
             tables=[table(
                 ["Verb", "они'-form", "Participle", "Meaning"],
                 [["чита'ть", "чита'ют", "чита'ющий", "reading"],
                  ["писа'ть", "пи'шут", "пи'шущий", "writing"],
                  ["жить", "живу'т", "живу'щий", "living"],
                  ["говори'ть", "говоря'т", "говоря'щий", "speaking"],
                  ["спать", "спят", "спя'щий", "sleeping"],
                  ["рабо'тать", "рабо'тают", "рабо'тающий", "working"]])],
             examples=[
                 ex("Де'вочка, чита'ющая кни'гу, — моя' сестра'.", "The girl reading a book is my sister.", "чита'ющая"),
                 ex("Лю'ди, живу'щие в э'том до'ме, о'чень до'брые.", "The people who live in this building are very kind.", "живу'щие"),
             ]),
        card("Reflexive verbs keep -ся",
             "A reflexive verb keeps -ся at the end of the participle, even after a vowel: занима'ющийся, "
             "ча'сто встреча'ющийся. The ending is always -ся here, never -сь.",
             tables=[table(
                 ["Verb", "Participle"],
                 [["занима'ться", "занима'ющийся"],
                  ["учи'ться", "уча'щийся"],
                  ["встреча'ться", "встреча'ющийся"]])],
             examples=[
                 ex("Ребёнок, занима'ющийся спо'ртом, ре'дко боле'ет.", "A child who does sports rarely gets sick.", "занима'ющийся"),
             ]),
        card("In a sentence",
             "A present active participle can replace кото'рый + a present-tense verb. The two sentences below mean "
             "the same.",
             tables=[table(
                 ["With кото'рый", "With a participle"],
                 [["Студе'нт, кото'рый чита'ет кни'гу, сиди'т у окна'.", "Студе'нт, чита'ющий кни'гу, сиди'т у окна'."],
                  ["Лю'ди, кото'рые живу'т здесь, до'брые.", "Лю'ди, живу'щие здесь, до'брые."]])],
             examples=[
                 ex("Вот челове'к, рабо'тающий в на'шем ба'нке.", "Here is a person who works in our bank.", "рабо'тающий"),
             ]),
    ],
    verify=(vf("читать", "читающий", "читают") + vf("писать", "пишущий", "пишут") + vf("жить", "живущий", "живут")
            + vf("говорить", "говорящий", "говорят") + vf("спать", "спящий", "спят") + vf("работать", "работающий", "работают")
            + vf("заниматься", "занимающийся") + vf("встречаться", "встречающийся")
            + vf("девочка", "девочка") + vf("сестра", "сестра") + vf("добрый", "добрые") + vf("банк", "банке")
            + vf("спорт", "спортом") + vf("болеть", "болеет") + vf("человек", "человек")),
    exercises=[
        mc("What is the participle of они' чита'ют?", ["чита'ющий", "чита'емый", "чита'вший", "прочи'танный"], "чита'ющий", "Drop -т, add -щий: чита'ющий.", order=True),
        mc("What is the participle of они' пи'шут?", ["пи'шущий", "пи'шет", "писа'вший", "напи'санный"], "пи'шущий", "They write → пи'шущий.", order=True),
        mc("What is the participle of они' говоря'т?", ["говоря'щий", "говоря'вший", "говори'мый", "говори'ть"], "говоря'щий", "Second conjugation: -ящий.", order=True),
        mc("What is the participle of они' живу'т?", ["живу'щий", "жи'вший", "жи'вущий", "живу'мый"], "живу'щий", "First conjugation: -ущий.", order=True),
        F("Лю'ди, ___ в э'том до'ме, о'чень до'брые. (living)", "живу'щие", ["жи'вшие", "живу'т", "жить"], "A present participle in the plural.", "The people who live in this building are very kind."),
        F("Ребёнок, ___ спо'ртом, ре'дко боле'ет. (doing)", "занима'ющийся", ["занима'вшийся", "занима'ться", "занима'ется"], "Reflexive: -ся stays.", "A child who does sports rarely gets sick.", lemma="заниматься"),
        F("Вот челове'к, ___ в на'шем ба'нке. (working)", "рабо'тающий", ["рабо'тающая", "рабо'тающие", "рабо'тать"], "Masculine singular: челове'к.", "Here is a person who works in our bank.", lemma="работать"),
        mc("Participles can often replace:", ["кото'рый + a present verb", "потому' что", "е'сли", "что'бы"], "кото'рый + a present verb", "Студе'нт, чита'ющий = студе'нт, кото'рый чита'ет."),
    ],
)

# ---------------------------------------------------------------------------- 253
L253 = lesson(
    "Past active: чита'вший, прочита'вший, уше'дший",
    "Студе'нт, прочита'вший кни'гу, отве'тил на вопро'с.",
    requires=["читать", "прочитать", "получить", "купить", "отправить"],
    cards=[
        card("From the past tense",
             "A past active participle describes a noun that did the action earlier. Take the masculine past tense, drop "
             "-л and add -вший. If the masculine past does not end in -л, add -ший: ушёл → уше'дший. The stress stays "
             "close to the stress of the infinitive; Wiktionary shows the exact form.",
             tables=[table(
                 ["Verb", "Past (m.)", "Participle", "Meaning"],
                 [["чита'ть", "чита'л", "чита'вший", "who was reading"],
                  ["прочита'ть", "прочита'л", "прочита'вший", "who had read"],
                  ["написа'ть", "написа'л", "написа'вший", "who had written"],
                  ["получи'ть", "получи'л", "получи'вший", "who had received"],
                  ["купи'ть", "купи'л", "купи'вший", "who had bought"],
                  ["уйти'", "ушёл", "уше'дший", "who had left"],
                  ["прийти'", "пришёл", "прише'дший", "who had come"]])],
             examples=[
                 ex("Студе'нт, прочита'вший кни'гу, отве'тил на вопро'с.", "The student who had read the book answered the question.", "прочита'вший"),
                 ex("Лю'ди, прише'дшие на конце'рт, жда'ли на у'лице.", "The people who had come to the concert were waiting on the street.", "прише'дшие"),
             ]),
        card("Imperfective or perfective",
             "Past active participles can be made from both aspects. From an imperfective verb the participle shows an "
             "action in progress or a repeated one in the past: чита'вший = who was reading. From a perfective verb it "
             "shows a finished action: прочита'вший = who had read.",
             tables=[table(
                 ["Imperfective", "Perfective"],
                 [["чита'вший (was reading)", "прочита'вший (had read)"],
                  ["отправля'вший (was sending)", "отпра'вивший (had sent)"],
                  ["получа'вший (was receiving)", "получи'вший (had received)"]])],
             examples=[
                 ex("Челове'к, отпра'вивший посы'лку, ушёл.", "The man who had sent the parcel left.", "отпра'вивший"),
             ]),
        card("In a sentence",
             "A past active participle can replace кото'рый + a past-tense verb.",
             tables=[table(
                 ["With кото'рый", "With a participle"],
                 [["Же'нщина, кото'рая купи'ла биле'т, ушла'.", "Же'нщина, купи'вшая биле'т, ушла'."]])],
             examples=[
                 ex("Ма'льчик, уста'вший по'сле дня, лёг спать.", "The boy, tired after the day, went to bed.", "уста'вший"),
             ]),
    ],
    verify=(vf("читать", "читавший") + vf("прочитать", "прочитавший") + vf("написать", "написавший")
            + vf("получить", "получивший") + vf("купить", "купивший") + vf("уйти", "ушедший")
            + vf("прийти", "пришедший") + vf("отправить", "отправивший") + vf("устать", "уставший")
            + vf("студент", "студент") + vf("книга", "книгу") + vf("вопрос", "вопрос") + vf("концерт", "концерт")
            + vf("улица", "улице") + vf("мальчик", "мальчик") + vf("женщина", "женщина") + vf("билет", "билет")
            + vf("посылка", "посылку") + vf("человек", "человек")),
    exercises=[
        mc("What is the participle of чита'л (past)?", ["чита'вший", "чита'ющий", "чита'емый", "прочи'танный"], "чита'вший", "Drop -л, add -вший.", order=True),
        mc("What is the participle of ушёл?", ["уше'дший", "уше'вший", "уходя'щий", "уйдённый"], "уше'дший", "No -л in the past: add -ший.", order=True),
        mc("‘The man who had bought a ticket’ is:", ["челове'к, купи'вший биле'т", "челове'к, покупа'ющий биле'т", "челове'к, ку'пленный биле'т", "челове'к, купи'мый биле'т"], "челове'к, купи'вший биле'т", "Past active.", order=True),
        F("Студе'нт, ___ кни'гу, отве'тил на вопро'с. (who had read)", "прочита'вший", ["чита'ющий", "прочи'танный", "чита'емый"], "Past active, perfective.", "The student who had read the book answered the question.", lemma="прочитать"),
        F("Челове'к, ___ посы'лку, ушёл. (who had sent)", "отпра'вивший", ["отпра'вленный", "отправля'ющий", "отпра'вить"], "Past active, perfective.", "The man who had sent the parcel left.", lemma="отправить"),
        F("Лю'ди, ___ на конце'рт, жда'ли на у'лице. (who had come)", "прише'дшие", ["прише'л", "приходя'щие", "прихо'дят"], "Past active plural.", "The people who had come to the concert were waiting on the street."),
        F("Ма'льчик, ___ по'сле дня, лёг спать. (tired)", "уста'вший", ["уста'нет", "уста'ть", "устаю'щий"], "Past active of уста'ть.", "The boy, tired after the day, went to bed.", lemma="устать"),
        mc("What is the participle from the perfective получи'л?", ["получи'вший", "получа'вший", "полу'ченный", "получа'емый"], "получи'вший", "Past active from the perfective.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 254
L254 = lesson(
    "Present passive: чита'емый, люби'мый, изуча'емый",
    "Вот кни'га, люби'мая детьми'.",
    requires=["читать", "любить", "видеть", "продавать", "изучать"],
    cards=[
        card("From the мы-form",
             "A present passive participle describes a noun that is being acted on right now. Take the мы-form of the "
             "verb and add -ый. First conjugation gives -емый; second conjugation gives -имый. Only imperfective verbs "
             "that take an object have this participle.",
             tables=[table(
                 ["Verb", "мы-form", "Participle", "Meaning"],
                 [["чита'ть", "чита'ем", "чита'емый", "that is being read"],
                  ["изуча'ть", "изуча'ем", "изуча'емый", "that is being studied"],
                  ["люби'ть", "лю'бим", "люби'мый", "loved"],
                  ["ви'деть", "ви'дим", "ви'димый", "visible"],
                  ["продава'ть", "продаём", "продава'емый", "that is being sold"],
                  ["уважа'ть", "уважа'ем", "уважа'емый", "respected"]])],
             examples=[
                 ex("Э'то изуча'емый в шко'ле язы'к.", "This is a language studied at school.", "изуча'емый"),
                 ex("Уважа'емые студе'нты! Уро'к начина'ется.", "Dear students! The lesson is beginning.", "Уважа'емые"),
             ]),
        card("The agent",
             "If you say who does the action, put them in the instrumental case. The participle is passive, so the "
             "doer goes in the instrumental: чита'емая детьми' кни'га = a book read by children.",
             examples=[
                 ex("Э'то кни'га, люби'мая детьми'.", "This is a book loved by children.", "люби'мая детьми'"),
                 ex("Вот това'ры, продава'емые в на'шем магази'не.", "Here are the goods sold in our shop.", "продава'емые"),
             ]),
        card("A few have become ordinary adjectives",
             "Some present passive participles are now just adjectives. Люби'мый (favorite), ви'димый (visible), "
             "уважа'емый (respected, dear) are everyday words. Elsewhere this participle is mostly found in writing.",
             examples=[
                 ex("Э'то мой люби'мый го'род.", "This is my favorite city.", "люби'мый"),
             ]),
    ],
    verify=(vf("читать", "читаем", "читаемый") + vf("изучать", "изучаем", "изучаемый") + vf("любить", "любим", "любимый")
            + vf("видеть", "видим", "видимый") + vf("продавать", "продаём", "продаваемый") + vf("уважать", "уважаем", "уважаемый")
            + vf("язык", "язык") + vf("школа", "школе") + vf("товар", "товары")
            + vf("магазин", "магазине") + vf("город", "город")),
    exercises=[
        mc("What is the present passive participle of чита'ть?", ["чита'емый", "чита'ющий", "чита'вший", "прочи'танный"], "чита'емый", "мы чита'ем → чита'емый.", order=True),
        mc("What is the present passive participle of люби'ть?", ["люби'мый", "любя'щий", "люби'вший", "лю'бленный"], "люби'мый", "мы лю'бим → люби'мый.", order=True),
        mc("Which verb has the present passive participle ви'димый?", ["ви'деть", "знать", "хоте'ть", "быть"], "ви'деть", "ви'дим → ви'димый.", order=True),
        F("Э'то изуча'емый в шко'ле ___. (language)", "язы'к", ["язы'ка", "языку'", "языке'"], "Nominative, after the participle.", "This is a language studied at school.", lemma="язык"),
        F("Э'то кни'га, люби'мая ___. (by children)", "детьми'", ["де'ти", "дете'й", "де'тям"], "The doer is in the instrumental.", "This is a book loved by children."),
        F("Вот това'ры, ___ в на'шем магази'не. (sold)", "продава'емые", ["продаю'щие", "прода'вшие", "про'данные"], "Present passive: продава'емые.", "Here are the goods sold in our shop."),
        F("Э'то мой ___ го'род. (favorite)", "люби'мый", ["любя'щий", "люби'вший", "лю'бить"], "A present passive participle used as an adjective.", "This is my favorite city.", lemma="любить"),
        mc("Which verbs have present passive participles?", ["imperfective verbs with an object", "perfective verbs only", "only verbs of motion", "all verbs"], "imperfective verbs with an object", "A thing must be acted on, and it must be happening."),
    ],
)

# ---------------------------------------------------------------------------- 255
L255 = lesson(
    "Past passive: прочи'танный, закры'тый, переведённый",
    "Письмо', напи'санное вчера', уже' на по'чте.",
    requires=["написать", "открыть", "закрыть", "сделать", "забыть"],
    cards=[
        card("From the infinitive of a perfective verb",
             "The past passive participle describes a noun that something has been done to. It is usually made from "
             "perfective verbs. The three suffixes are -нн-, -енн- and -т-.",
             tables=[table(
                 ["Verb", "Participle", "Meaning"],
                 [["прочита'ть", "прочи'танный", "read"],
                  ["написа'ть", "напи'санный", "written"],
                  ["сде'лать", "сде'ланный", "made, done"],
                  ["отпра'вить", "отпра'вленный", "sent"],
                  ["получи'ть", "полу'ченный", "received"],
                  ["доста'вить", "доста'вленный", "delivered"],
                  ["купи'ть", "ку'пленный", "bought"],
                  ["перевести'", "переведённый", "translated"],
                  ["закры'ть", "закры'тый", "closed"],
                  ["откры'ть", "откры'тый", "opened"],
                  ["забы'ть", "забы'тый", "forgotten"],
                  ["взять", "взя'тый", "taken"]])],
             examples=[
                 ex("Письмо', напи'санное вчера', уже' на по'чте.", "The letter written yesterday is already at the post office.", "напи'санное"),
                 ex("Покупа'тели нашли' ку'пленный вчера' зонт.", "The shoppers found the umbrella that had been bought yesterday.", "ку'пленный"),
             ]),
        card("Which suffix?",
             "Roughly: verbs in -ать, -ять, -еть add -нный (написанный). Verbs in -ить change the consonant and add "
             "-енный (полученный, купленный). A few short verbs add -тый (закрытый, забытый, взятый).",
             tables=[table(
                 ["Infinitive ends in", "Suffix", "Example"],
                 [["-ать / -ять", "-нный", "прочи'танный"],
                  ["-ить / -еть", "-енный / -ённый", "полу'ченный, переведённый"],
                  ["-уть / -ыть / one syllable", "-тый", "закры'тый, взя'тый"]])],
             examples=[
                 ex("Откры'тая дверь ведёт в сад.", "The open door leads into the garden.", "Откры'тая"),
             ]),
        card("The agent",
             "The doer, if mentioned, goes in the instrumental case.",
             examples=[
                 ex("Э'то письмо', напи'санное мое'й ба'бушкой.", "This is a letter written by my grandmother.", "ба'бушкой"),
                 ex("Вот забы'тый ке'м-то зонт.", "Here is an umbrella forgotten by someone.", "забы'тый"),
             ]),
    ],
    verify=(vf("прочитать", "прочитанный") + vf("написать", "написанный") + vf("сделать", "сделанный")
            + vf("отправить", "отправленный") + vf("получить", "полученный") + vf("доставить", "доставленный")
            + vf("купить", "купленный") + vf("закрытый", "закрытый") + vf("открытый", "открытый") + vf("забыть", "забытый")
            + vf("взять", "взятый") + vf("письмо", "письмо") + vf("дверь", "дверь") + vf("сад", "сад")
            + vf("бабушка", "бабушкой") + vf("зонт", "зонт")),
    exercises=[
        mc("What is the past passive participle of написа'ть?", ["напи'санный", "написа'вший", "пи'шущий", "пи'сьменный"], "напи'санный", "Написа'ть → напи'санный.", order=True),
        mc("What is the past passive participle of закры'ть?", ["закры'тый", "закрыва'ющий", "закры'вший", "закры'ванный"], "закры'тый", "Short verbs add -тый.", order=True),
        mc("What is the past passive participle of купи'ть?", ["ку'пленный", "купи'вший", "покупа'емый", "ку'пенный"], "ку'пленный", "Купи'ть → ку'пленный.", order=True),
        F("Письмо', ___ вчера', уже' на по'чте. (written)", "напи'санное", ["написа'вшее", "пи'шущее", "напи'санный"], "Neuter past passive: письмо'.", "The letter written yesterday is already at the post office."),
        F("___ дверь ведёт в сад. (open)", "Откры'тая", ["Откры'тый", "Откры'тое", "Откры'тые"], "Дверь is feminine.", "The open door leads into the garden.", lemma="открытый"),
        F("Э'то письмо', напи'санное мое'й ___. (by my grandmother)", "ба'бушкой", ["ба'бушка", "ба'бушки", "ба'бушку"], "The doer is in the instrumental.", "This is a letter written by my grandmother."),
        F("Вот ___ ке'м-то зонт. (forgotten)", "забы'тый", ["забы'вший", "забыва'ющий", "забыва'емый"], "Past passive: something was forgotten.", "Here is an umbrella forgotten by someone.", lemma="забыть"),
        mc("Which suffix does a past passive participle usually have?", ["-нн-, -енн- or -т-", "-щ- or -ш-", "-ем- or -им-", "-л-"], "-нн-, -енн- or -т-", "Past passive: н, нн, т.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 256
L256 = lesson(
    "A participle agrees with its noun: in every case",
    "Я ви'жу де'вочку, чита'ющую кни'гу.",
    requires=["девочка", "письмо", "слово", "окно", "студент"],
    cards=[
        card("Like any adjective",
             "A participle has adjective endings, so it agrees with its noun in gender, number and case. The verb part "
             "of the participle stays the same. Compare the endings of чита'ющий with хоро'ший:",
             tables=[table(
                 ["Case", "Masc.", "Fem.", "Neut.", "Plural"],
                 [["Nom.", "чита'ющий", "чита'ющая", "чита'ющее", "чита'ющие"],
                  ["Gen.", "чита'ющего", "чита'ющей", "чита'ющего", "чита'ющих"],
                  ["Dat.", "чита'ющему", "чита'ющей", "чита'ющему", "чита'ющим"],
                  ["Instr.", "чита'ющим", "чита'ющей", "чита'ющим", "чита'ющими"],
                  ["Prep.", "чита'ющем", "чита'ющей", "чита'ющем", "чита'ющих"]])],
             examples=[
                 ex("Я ви'жу де'вочку, чита'ющую кни'гу.", "I see a girl reading a book.", "чита'ющую"),
                 ex("Мы говори'м о де'вочке, чита'ющей кни'гу.", "We are talking about the girl who is reading a book.", "чита'ющей"),
             ]),
        card("The object keeps its own case",
             "The words that depend on the verb part keep the case the verb needs. Чита'ть takes the accusative, so "
             "кни'гу stays in the accusative however the participle changes.",
             examples=[
                 ex("Он помога'ет ма'льчику, чита'ющему вслух.", "He is helping the boy who is reading aloud.", "чита'ющему"),
                 ex("Мы дово'льны студе'нтами, изуча'ющими ру'сский.", "We are pleased with the students who are studying Russian.", "изуча'ющими"),
             ]),
        card("Passive and past participles",
             "Passive and past participles agree in the same way. Their endings are the ordinary adjective endings.",
             tables=[table(
                 ["Case", "Fem. singular", "Plural"],
                 [["Nom.", "напи'санная", "напи'санные"],
                  ["Gen.", "напи'санной", "напи'санных"],
                  ["Acc.", "напи'санную", "напи'санные"],
                  ["Instr.", "напи'санной", "напи'санными"]])],
             examples=[
                 ex("Я чита'ю статью', напи'санную мои'м дру'гом.", "I am reading an article written by my friend.", "напи'санную"),
             ]),
    ],
    verify=(vf("читать", "читать") + vf("девочка", "девочку", "девочке") + vf("мальчик", "мальчику")
            + vf("студент", "студентами") + vf("книга", "книгу") + vf("помогать", "помогает")
            + vf("довольный", "довольны") + vf("изучать", "изучающими" if False else "изучать")
            + vf("статья", "статью") + vf("друг", "другом") + vf("вслух", "вслух")),
    exercises=[
        F("Я ви'жу де'вочку, ___ кни'гу. (reading, fem. acc.)", "чита'ющую", ["чита'ющая", "чита'ющей", "чита'ющий"], "Accusative feminine: -ую.", "I see a girl reading a book."),
        F("Мы говори'м о де'вочке, ___ кни'гу. (reading, fem. prep.)", "чита'ющей", ["чита'ющую", "чита'ющая", "чита'ющим"], "Prepositional feminine: -ей.", "We are talking about the girl who is reading a book."),
        F("Он помога'ет ма'льчику, ___ вслух. (reading, masc. dat.)", "чита'ющему", ["чита'ющего", "чита'ющим", "чита'ющем"], "Dative masculine: -ему.", "He is helping the boy who is reading aloud."),
        F("Мы дово'льны студе'нтами, ___ ру'сский. (studying, plural instr.)", "изуча'ющими", ["изуча'ющих", "изуча'ющим", "изуча'ющие"], "Instrumental plural: -ими.", "We are pleased with the students who are studying Russian."),
        F("Я чита'ю статью', ___ мои'м дру'гом. (written, fem. acc.)", "напи'санную", ["напи'санная", "напи'санной", "напи'санный"], "Accusative feminine: -ую.", "I am reading an article written by my friend."),
        F("Кни'га оста'лась у студе'нта, ___ её вчера'. (who had read, masc. gen.)", "прочита'вшего", ["прочита'вший", "прочита'вшему", "прочита'вшим"], "Genitive masculine: -его (after ш: -его).", "The book stayed with the student who had read it yesterday."),
        mc("What does a participle agree with?", ["the noun it describes", "the subject of the sentence always", "the verb of the main clause", "nothing"], "the noun it describes", "Gender, number, case."),
        mc("Which case does the object keep after чита'ющий?", ["accusative", "genitive", "dative", "nominative"], "accusative", "Чита'ть + accusative.", order=True),
    ],
)

# ---------------------------------------------------------------------------- 257
L257 = lesson(
    "Word order: noun + participle, or participle + noun",
    "Письмо', напи'санное вчера', лежи'т на столе'.",
    requires=["письмо", "стол", "девочка", "окно", "дверь"],
    cards=[
        card("Construction 1: noun, then participle",
             "The participle follows the noun and is set off by commas, together with the words that depend on it. This "
             "is the easiest order to read, because the noun comes first.",
             tables=[table(
                 ["Noun", "Participle phrase"],
                 [["Письмо',", "напи'санное вчера',"],
                  ["Студе'нт,", "чита'ющий газе'ту,"],
                  ["Де'вочка,", "стоя'щая у окна',"]])],
             examples=[
                 ex("Письмо', напи'санное вчера', лежи'т на столе'.", "The letter written yesterday is lying on the table.", "напи'санное вчера'"),
                 ex("Де'вочка, стоя'щая у окна', — моя' сестра'.", "The girl standing by the window is my sister.", "стоя'щая у окна'"),
             ]),
        card("Construction 2: participle first, noun last",
             "The participle can also stand before the noun, like an ordinary adjective. But its dependent words come "
             "with it, so the participle and its noun may be separated by a whole phrase. There is no comma before the "
             "participle.",
             tables=[table(
                 ["Construction 1", "Construction 2"],
                 [["Письмо', напи'санное вчера', лежи'т на столе'.", "Напи'санное вчера' письмо' лежи'т на столе'."],
                  ["Студе'нт, чита'ющий газе'ту, молчи'т.", "Чита'ющий газе'ту студе'нт молчи'т."]])],
             examples=[
                 ex("Стоя'щая у окна' де'вочка улыбну'лась.", "The girl standing by the window smiled.", "Стоя'щая у окна' де'вочка"),
             ]),
        card("How to untangle it",
             "If you meet a participle without a comma before it, note its gender, number and case. Then read on until "
             "you find a noun with the same features. Everything between them belongs to the participle.",
             tables=[table(
                 ["Sentence", "Participle", "Its noun"],
                 [["Откры'тая учи'телем дверь ведёт в сад.", "откры'тая", "дверь (fem. nom.)"],
                  ["Я чита'ю письмо', напи'санное бра'том.", "напи'санное", "письмо' (neut.)"]])],
             examples=[
                 ex("Я чита'ю письмо', напи'санное бра'том.", "I am reading a letter written by my brother.", "напи'санное бра'том"),
             ]),
    ],
    verify=(vf("письмо", "письмо") + vf("стол", "столе") + vf("девочка", "девочка") + vf("окно", "окна")
            + vf("студент", "студент") + vf("газета", "газету") + vf("сестра", "сестра") + vf("брат", "братом")
            + vf("улыбнуться", "улыбнулась") + vf("учитель", "учителем") + vf("дверь", "дверь") + vf("сад", "сад")
            + vf("молчать", "молчит") + vf("лежать", "лежит") + vf("читать", "читаю") + vf("вести", "ведёт")),
    exercises=[
        mc("In ‘Письмо', напи'санное вчера', лежи'т на столе'.’ the participle refers to:", ["письмо'", "вчера'", "стол", "лежи'т"], "письмо'", "Construction 1: noun, participle.", order=True),
        mc("In ‘Стоя'щая у окна' де'вочка улыбну'лась.’ the participle refers to:", ["де'вочка", "окно'", "улыбну'лась", "у"], "де'вочка", "Construction 2: the noun comes last.", order=True),
        mc("In ‘Я чита'ю письмо', напи'санное бра'том.’ the doer is:", ["бра'том", "я", "письмо'", "чита'ю"], "бра'том", "Instrumental: the doer of a passive participle.", order=True),
        F("Студе'нт, ___ газе'ту, молчи'т. (reading)", "чита'ющий", ["чита'ющая", "чита'ющее", "чита'ющие"], "Construction 1, masculine.", "The student reading a newspaper is silent."),
        F("___ учи'телем дверь ведёт в сад. (opened)", "Откры'тая", ["Откры'тый", "Откры'тое", "Откры'тые"], "Construction 2; agrees with дверь.", "The door opened by the teacher leads into the garden."),
        F("Де'вочка, ___ у окна', — моя' сестра'. (standing)", "стоя'щая", ["стоя'щий", "стоя'щее", "стоя'щие"], "Construction 1, feminine.", "The girl standing by the window is my sister."),
        mc("Is there a comma before the participle in Construction 2?", ["no", "yes", "only before names", "only at the end"], "no", "No comma before the participle in front of the noun.", order=True),
        mc("What do you do with an unfamiliar participle in front of a noun?", ["find the noun with the same gender, number and case", "ignore it", "translate it as a verb in the future", "turn it into an infinitive"], "find the noun with the same gender, number and case", "Gender, number and case point to the noun."),
    ],
)

# ---------------------------------------------------------------------------- 258
L258 = lesson(
    "Review: post, internet, social networks and participles",
    "Письмо', напи'санное мое'й сестро'й, пришло' по по'чте.",
    requires=["письмо", "интернет", "сеть", "читать", "открыть"],
    cards=[
        card("What you know",
             "Post, internet and social-network vocabulary. A participle is an adjective formed from a verb; it agrees "
             "with its noun and has four types:",
             tables=[table(
                 ["", "Active", "Passive"],
                 [["Present", "чита'ющий", "чита'емый"],
                  ["Past", "чита'вший, прочита'вший", "прочи'танный"]])],
             examples=[
                 ex("Письмо', напи'санное мое'й сестро'й, пришло' по по'чте.", "The letter written by my sister came by mail.", "напи'санное мое'й сестро'й"),
                 ex("Сайт, посеща'емый ты'сячами люде'й, рабо'тает бы'стро.", "The website visited by thousands of people works fast.", "посеща'емый"),
             ]),
    ],
    verify=(vf("письмо", "письмо") + vf("сестра", "сестрой") + vf("почта", "почте") + vf("сайт", "сайт")
            + vf("посещать", "посещаемый") + vf("тысяча", "тысячами") + vf("работать", "работает")
            + vf("быстро", "быстро")),
    exercises=[
        F("Мне ну'жно ___ посы'лку. (send)", "отпра'вить", ["получи'ть", "скача'ть", "забы'ть"], "Отпра'вить посы'лку.", "I need to send a parcel.", lemma="отправить"),
        F("Введи' ___ и откро'й сайт. (password)", "паро'ль", ["ссы'лку", "файл", "страни'цу"], "Ввести' паро'ль.", "Enter the password and open the site."),
        F("Она' подписа'лась ___ мой блог. (to)", "на", ["в", "к", "о"], "Подписа'ться на + accusative.", "She subscribed to my blog."),
        mc("What type is чита'ющий?", ["present active", "present passive", "past active", "past passive"], "present active", "-ющ-.", order=True),
        mc("What type is прочи'танный?", ["past passive", "past active", "present active", "present passive"], "past passive", "-нн-.", order=True),
        mc("Which participle fits ‘a letter that was written’?", ["напи'санное письмо'", "пи'шущее письмо'", "написа'вшее письмо'", "пи'шемое письмо'"], "напи'санное письмо'", "Past passive, neuter.", order=True),
        F("Де'вочка, ___ кни'гу, — моя' сестра'. (reading)", "чита'ющая", ["чита'ющий", "чита'ющее", "чита'ющие"], "Feminine singular.", "The girl reading a book is my sister."),
        F("Вот письмо', ___ вчера'. (written)", "напи'санное", ["напи'санная", "напи'санный", "напи'санные"], "Neuter: письмо'.", "Here is a letter written yesterday."),
        mc("Does a participle agree with its noun?", ["yes, in gender, number and case", "no", "only in number", "only in gender"], "yes, in gender, number and case", "Like any adjective."),
    ],
)

UNIT = unit("Unit 26: Post, internet and social networks; participles",
            [L246, L247, L248, L249, L250, L251, L252, L253, L254, L255, L256, L257, L258])
