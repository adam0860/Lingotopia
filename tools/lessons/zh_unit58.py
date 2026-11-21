"""Unit 58: Lesson 20 (The Post Office) Presentation 2 from the book's texts: the parcel-to-New-York dialog, the five activities, the post-modifier
cluster in the 比 pattern, 最多/最少, 要看/得看, 不过/但是/可是, the skill-integration activities (postal rates, the missing parcel, the blogger's post),
the using-Chinese activities (ten sentences and the Taiwan envelopes) and the vocabulary list. Audio, pictures, forms and links are not included;
numbers the book writes as digits are spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l20_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P2 = [("陈雪晴", "您好，我有个包裹要寄到纽约。", "Hello, I have a parcel to send to New York."), ("营业员", "你想怎么寄？我们有航空、海运，还有特快专递？", "How do you want to send it? We have air, sea and express delivery."),
      ("陈雪晴", "哪个最快？", "Which is fastest?"), ("营业员", "特快专递最快，最多五个工作日就到，但是价钱贵一些。空运、海运慢一点，但是价钱便宜很多。", "Express is fastest, it arrives in five working days at most, but the price is a bit higher. Air and sea are a little slower, but the price is much cheaper."),
      ("陈雪晴", "那我就寄特快专递吧。", "Then I’ll send it by express."), ("营业员", "包裹里有没有液体和易碎、易燃物品？", "Are there any liquids, or fragile or flammable items in the parcel?"),
      ("陈雪晴", "没有，就是一张贺卡和一条项链。", "No, just a greeting card and a necklace."), ("营业员", "我称一下。没超重，你要不要买保险？", "Let me weigh it. It isn’t overweight. Do you want to buy insurance?"),
      ("陈雪晴", "要，保险费是多少？", "Yes. How much is the insurance?"), ("营业员", "要看你保多少了。", "It depends on how much you insure it for."),
      ("陈雪晴", "这条项链两千五百块。", "This necklace is 2,500 yuan (the book writes it in characters)."), ("营业员", "邮费加上保险费一共三百八十七块五。不过，请你先填一下包裹单和海关申报单。", "The postage plus the insurance comes to 387.5 yuan altogether. But please first fill in the parcel form and the customs declaration form."),
      ("陈雪晴", "（过了一会儿）填完了，您看填得对不对？", "(After a while) I’ve finished. Could you see whether I filled them in correctly? (the book writes [过了一会儿] in brackets)"), ("营业员", "填得都对。", "They’re all correct."),
      ("陈雪晴", "这是四百块。", "Here’s 400 yuan."), ("营业员", "找你十二块五，这是你的收据，上面有二维码，你扫一下就知道包裹到哪儿了。", "Here’s 12.5 yuan change. This is your receipt, it has a QR code on it, and if you scan it you’ll know where the parcel has got to.")]
L1 = lesson(
    "Lesson 20 Presentation 2: mailing a parcel to New York",
    "航空 海运 特快专递 · 液体、易碎、易燃 · 保险 · 包裹单和海关申报单 · 二维码",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Can you name the shipping services in the images (not included) in Chinese? B. Which shipping methods do you prefer? Why? C. Can you recall questions that a postal clerk might ask you in Chinese when mailing a letter or parcel? List at least three questions."),
        card("Presentation 2: 寄包裹到纽约", "The book also prints the dialog in traditional characters, and the numbers in the dialog (two thousand five hundred, three hundred eighty-seven and a half, four hundred, twelve and a half) are written out in characters. The translations are mine.", examples=dlg(P2)),
    ],
    exercises=[
        M("Where does Chen Xueqing want to send the parcel?", "New York", ["Beijing", "Taipei", "Shanghai"], "寄到纽约."),
        M("Which of the three shipping services is fastest?", "特快专递 (express delivery)", ["航空 (air)", "海运 (sea)", "平信 (ordinary mail)"], "特快专递最快."),
        M("How long does express delivery take at most?", "Five working days", ["Five hours", "Five weeks", "Three working days"], "最多五个工作日就到."),
        M("How do air and sea compare with express?", "A little slower but much cheaper", ["Faster and cheaper", "Faster but dearer", "The same"], "空运、海运慢一点，但是价钱便宜很多."),
        M("What is in the parcel?", "A greeting card and a necklace", ["Books and a bottle of wine", "Clothes", "A phone"], "一张贺卡和一条项链."),
        M("What three kinds of goods does the clerk ask about?", "Liquids, fragile items and flammable items", ["Food, books and toys", "Money, jewelry and stamps", "Clothes, shoes and bags"], "液体和易碎、易燃物品."),
        M("How does the clerk answer “保险费是多少？”", "It depends on how much you insure it for", ["Ten percent", "It is free", "Two hundred"], "要看你保多少了."),
        M("How much is the necklace worth (as she says)?", "Two thousand five hundred yuan", ["Two hundred fifty", "Four hundred", "Three hundred eighty-seven"], "这条项链两千五百块."),
        M("What is the total for postage plus insurance?", "387.5 yuan", ["400 yuan", "12.5 yuan", "2,500 yuan"], "邮费加上保险费一共三百八十七块五."),
        M("How much change does she get?", "12.5 yuan", ["387.5 yuan", "400 yuan", "2.5 yuan"], "找你十二块五."),
        M("What can you do with the QR code on the receipt?", "Scan it to find out where the parcel is", ["Pay for insurance", "Open a mailbox", "Print a form"], "你扫一下就知道包裹到哪儿了."),
        F("你想怎么___？我们有航空、海运，还有特快专递。", "寄", PART, "寄: to mail."),
        F("包裹里有没有液体和易碎、易___物品？", "燃", PART, "易燃: flammable."),
        F("请你先填一下包裹___和海关申报单。", "单", PART, "包裹单: parcel form."),
    ],
)

# ------------------------------------------------------------------ 2. activities 1-5
CAT = table(["可邮寄的东西 (mine)", "邮寄需填的表 (mine)", "邮寄的方式 (mine)"],
            [["项链，贺卡，液体，易碎物品，易燃物品", "包裹单，海关申报单", "航空，海运，特快专递，平信，挂号信"]],
            title="Activity 1A: sorting the fifteen words (the book leaves the table blank; 邮费, 保险费 and 邮局 are not items, forms or methods, so I treat them as the distractors)", say=[0, 1, 2])
MT = [("你想怎么寄？", "我想寄特快专递。", "1 + f. How do you want to send it? — I want to send it by express. (key mine)"), ("航空、海运，还有特快专递，哪个最快？", "特快专递最快，但是有点贵。", "2 + a. Air, sea and express: which is fastest? — Express is fastest, but it’s a bit dear."),
      ("包裹里有没有液体和易碎、易燃物品？", "没有，就是一张贺卡和一条项链。", "3 + d. Are there liquids, or fragile or flammable items in the parcel? — No, just a greeting card and a necklace."), ("保险费是多少？", "那要看你保多少了。", "4 + b. How much is the insurance? — That depends on how much you insure for."),
      ("我想寄一个包裹到美国，我可以怎么寄？", "你可以寄航空、海运或是特快专递。", "5 + e. I want to send a parcel to the U.S.: how can I send it? — You can send it by air, sea or express."), ("从这儿寄一个特快专递的包裹到纽约需要几个工作日？", "差不多要五个工作日。", "6 + c. How many working days does an express parcel from here to New York need? — About five working days. (the book writes 5 with a digit)")]
MTD = []
for q, a, e in MT:
    lab, rest = e.split(". ", 1)
    qen, aen = rest.split(" — ", 1)
    MTD += dlg([("甲", q, lab + ". " + qen), ("乙", a, aen)])
PHR = table(["字", "我知道的词 (mine)"], [["寄", "寄信，寄包裹，邮寄，寄件人，寄东西"], ["包", "包裹，包裹单，书包，面包"], ["费", "邮费，保险费，水电费，学费"], ["品", "物品，食品，商品，易碎物品，易燃物品"]],
            title="Activity 5: phrases that contain 寄, 包, 费 and 品 (the book leaves the table blank; these are mine)", say=[1])
L2 = lesson(
    "Lesson 20 Presentation 2 activities: words, matching, the parcel form",
    "Activities 1 to 5 · 可邮寄的东西 邮寄需填的表 邮寄的方式 · 配对 · 包裹单 · 寄 包 费 品",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking)",
             "A. Write the words 航空, 项链, 贺卡, 邮费, 液体, 海运, 易碎物品, 易燃物品, 海关申报单, 特快专递, 包裹单, 保险费, 平信, 挂号信 and 邮局 into the categories 可邮寄的东西 / 邮寄需填的表 / 邮寄的方式; some words are distractors. B. Do you recognize any words you do not know? Write them with their meanings. C. Pair up and check your answers; create three sentences, each using two words from those you filled in, and your partner will translate them. My sorting:",
             tables=[CAT]),
        card("Activity 2 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 2 once and answer: 1. What is the presentation about? 2. What information is being exchanged? B. Detailed listening: listen again and, in Chinese, write the EEIs (essential elements of information) about what the customer has done: what to ship, how to ship, why this method, shipping cost, additional details. C. Pair up: one partner asks who-what-where questions and the other answers using what they hear. (Audio, not included. From the dialog text: she mails a card and a necklace by express because it is fastest; she buys insurance; the cost is 387.5 yuan.)"),
        card("Activity 3 (Reading and Speaking)",
             "A. Match the questions in the left column with the answers in the right column. The book prints the six questions and answers a to f but no key; my pairs:",
             examples=MTD),
        card("Activity 4 (Reading, Listening and Speaking)",
             "A. Familiarize yourself with the contents of the form (the book prints it as a layout, not included here). 请填写包裹单: 包裹号码; 收件人 (姓名, 地址); 寄件人 (姓名, 地址); 重量; 邮费; 保价费 (元); 共计; 包里有什么物品; 寄件人签字; 日期 (年, 月, 日). B. Listen to the dialog between David and a postal clerk and, using what you hear, complete the form. C. Pair up and, in Chinese, check your answers with those of your partner. (Audio, not included; the book prints no script.)"),
        card("Activity 5 (Reading, Speaking and Listening)",
             "A. Pair up and, with your partner, think of all the phrases you know that contain the characters in the table 寄 | 包 | 费 | 品. B. Share your work with the class. My phrases:",
             tables=[PHR]),
    ],
    exercises=[
        M("Which word belongs to 邮寄的方式?", "特快专递", ["包裹单", "项链", "贺卡"], "特快专递 is a mailing method."),
        M("Which word belongs to 邮寄需填的表?", "海关申报单", ["航空", "液体", "海运"], "海关申报单 is a form."),
        M("Which word belongs to 可邮寄的东西?", "贺卡", ["海运", "挂号信", "包裹单"], "贺卡 is an item."),
        M("Which of these is a distractor (not an item, form or method)?", "邮局", ["贺卡", "包裹单", "航空"], "邮局 is a place."),
        M("In the matching, which answer goes with “保险费是多少？”", "那要看你保多少了", ["差不多要五个工作日", "我想寄特快专递", "没有，就是一张贺卡和一条项链"], "4 + b."),
        M("Which answer goes with “你想怎么寄？”", "我想寄特快专递", ["那要看你保多少了", "你可以寄航空、海运或是特快专递", "差不多要五个工作日"], "1 + f."),
        M("Which question goes with “差不多要五个工作日”?", "从这儿寄一个特快专递的包裹到纽约需要几个工作日？", ["保险费是多少？", "你想怎么寄？", "哪个最快？"], "6 + c."),
        M("What does 保价费 on the form refer to?", "The insured-value (insurance) fee", ["The weight", "The postage", "The date"], "保价费: insurance fee."),
        M("Which phrase contains 费?", "邮费", ["贺卡", "包裹", "寄信"], "邮费."),
        M("Which phrase contains 品?", "易碎物品", ["特快专递", "收据", "二维码"], "易碎物品."),
        F("寄件人___字", "签", PART, "签字: sign."),
        F("包___单和海关申报单", "裹", PART, "包裹单."),
    ],
)

# ------------------------------------------------------------------ 3. comparison
CMP = table(["A", "比", "B", "adjective", "post-modifier cluster (degree)"], [["高铁", "比", "特快车", "快", "得多 / 很多 / 多了 / 不少 / 一点(儿) / a specific amount such as 2–3 个钟头"]],
            title="A 比 B + adj. + post-modifier cluster")
CE = [("高铁比特快车快得多。", "The high-speed rail is much faster than the express train."), ("空运、海运慢一点，不过价钱便宜很多。", "Air and sea are a little slower, but the price is much cheaper."),
      ("空运、海运（比特快专递）慢一点，不过价钱（比特快专递）便宜很多。", "Air and sea are a little slower (than express) but much cheaper (than express): the 比 “B” part restored."), ("特快专递比航空包裹更快。", "Express is even faster than an air parcel (更 before the adjective)."), ("特快专递比航空包裹还快。", "Express is still faster than an air parcel (还 before the adjective).")]
CA1 = [("平信比航空信慢一些。可是比航空信便宜一点儿。", "Ordinary mail is a bit slower than airmail. But it is a little cheaper than airmail. (the book’s example)"), ("特快专递比平信快很多，但是也贵很多。", "Express is much faster than ordinary mail, but also much dearer. (the book’s example)"),
       ("高速动车比特快列车快多了，特快列车又比慢车快不少。", "The high-speed train is much faster than the express train, and the express train is quite a bit faster than the slow train. (mine, for Row 2: 慢车, 特快列车, 高速动车)"), ("坐慢车比坐高速动车便宜得多，可是也慢得多。", "Taking the slow train is much cheaper than the high-speed train, but also much slower. (mine)"), ("今天比昨天冷一点儿，也比昨天冷两度。", "Today is a little colder than yesterday, colder by two degrees. (mine; shows a specific amount)")]
L3 = lesson(
    "Lesson 20 Presentation 2 grammar: the post-modifier cluster in the 比 pattern",
    "高铁比特快车快得多 · 很多 多了 不少 一点儿 · 更 还 · 省略 B",
    requires=[],
    cards=[
        card("Post-modifier cluster in 比 pattern",
             "When used for comparison, the degree to modify the bare adjective needs to be placed after the adjective: A 比 B + adj. + post-modifier cluster (to indicate degree). The cluster can be 得多, 很多, 多了, 不少, 一点(儿), or a specific amount such as 2–3 个钟头. Occasionally the 比 “B” portion may be omitted because the context is known, but the sense of comparison is still implied. The adverbs 更 and 还 can be placed before the adjective when making a comparison.",
             tables=[CMP], examples=[D(z, e) for z, e in CE]),
        card("Activity 1 (Speaking)",
             "Pair up. Students take turns using the images in the rows (four rows of three pictures, not included; Row 2 is labeled 慢车, 特快列车, 高速动车) to make comparisons in degrees. Example: Student A: 平信比航空信慢一些。可是比航空信便宜一点儿。 Student B: 特快专递比平信快很多，但是也贵很多。 My comparisons for Row 2 and others:",
             examples=[D(z, e) for z, e in CA1]),
        card("Activity 2 (Listening and Speaking)",
             "A. Listen to a conversation between a foreign student (Jenny) and a teacher (Teacher Wang) and fill in the table with the features/differences of 海运, 航空 and 特快专递, Teacher Wang’s suggestions and Jenny’s final decision. B. Form groups of three; each student reports on one column of the shipping-method table, and students listen and compare their answers. (Audio, not included; the book prints no script.)"),
    ],
    exercises=[
        M("Where does the degree word go in a 比 comparison?", "After the adjective", ["Before 比", "Before the adjective", "At the very end after the noun"], "A 比 B + adj. + post-modifier."),
        M("Which is a correct comparison?", "高铁比特快车快得多。", ["高铁比特快车得多快。", "高铁快得多比特快车。", "比高铁特快车快得多。"], "A 比 B adj. 得多."),
        M("Which cluster means “a little”?", "一点儿", ["得多", "不少", "很多"], "一点儿: a little."),
        M("Which cluster means “a great deal”?", "得多", ["一点儿", "一些", "一点"], "得多: much more."),
        M("Where do 更 and 还 go?", "Before the adjective", ["After the adjective", "After the noun", "Before 比"], "比…更快 / 比…还快."),
        M("What does 特快专递比航空包裹更快 mean?", "Express is even faster than an air parcel", ["Express is slower", "Air is faster", "They are equally fast"], "更: even more."),
        M("In 空运、海运慢一点，不过价钱便宜很多, what is left out?", "比特快专递 (than express)", ["比平信", "比海运", "比价钱"], "The B portion is omitted because the context is known."),
        M("“Ordinary mail is a bit slower than airmail.”", "平信比航空信慢一些。", ["平信比慢航空信一些。", "平信慢一些比航空信。", "航空信比平信慢一些。"], "平信比航空信慢一些."),
        F("特快专递比平信快很___，但是也贵很多。", "多", PART, "快很多: much faster."),
        F("高铁比特快车快得___。", "多", PART, "得多."),
        F("特快专递比航空包裹___快。", "更", PART, "更快: even faster."),
    ],
)

# ------------------------------------------------------------------ 4. 最多 最少
ZE = [("从中国寄快递包裹到纽约最多只要三个工作日。", "From China, sending an express parcel to New York takes only three working days at most. (the book writes 3)"), ("从旧金山坐飞机到台北最少要十三个小时。", "Flying from San Francisco to Taipei takes at least thirteen hours. (the book writes 13)"),
      ("要通过语言能力考试，你最少要认识一千六百个汉字。", "To pass the language proficiency test you need to know at least 1,600 characters. (the book writes “DLPT 考试” and 1600; I wrote the name in characters because these examples are spoken)"), ("明天的生日派对，你最多需要准备十个人的饭菜。", "For tomorrow’s birthday party you need to prepare food for ten people at most. (the book writes 10)")]
ZS = [("我的银行账户最多只有两千块钱。", "My bank account has two thousand yuan at most. (the book’s example, with 2000 spelled out)"), ("我最多只能吃三碗饭。", "I can eat three bowls of rice at most. (the book’s example)"), ("我最少能认得三百个汉字。", "I can recognize at least three hundred characters. (the book’s example, with 300 spelled out)")]
FLY = ("近几年来由于安全的原因，坐飞机越来越花时间。如果是坐国内的航班，人们最少要提前一个小时到机场。到了机场以后，还要办登机手续和通过安检。人多的时候，有时最少要排上一个多小时的队。除了飞行时间，最少还要再加上两三个小时的交通时间和等候时间。所以现在有越来越多的人选择坐高铁，因为高铁站多半在城内，比较方便，而且速度快，从北京到上海最多不到五个小时。另外，列车也很少晚点。因此，可以为旅客省下不少时间。",
       "In recent years, for safety reasons, flying takes more and more time. For a domestic flight people have to arrive at the airport at least an hour ahead. After arriving they still have to check in and go through security. When there are many people, sometimes they have to queue for at least an hour or more. Besides the flying time, at least two or three more hours of transport and waiting time must be added. So now more and more people choose the high-speed rail, because the stations are mostly inside the city, which is more convenient, and it is fast: from Beijing to Shanghai it takes less than five hours at most. In addition, trains are seldom late. Therefore it can save travelers quite a lot of time. (the book prints digits and the typo 等侯; I wrote the numbers in characters and 等候)")
TRV = table(["项目", "坐飞机 (mine)", "坐高铁 (mine)"],
            [["原因/特点", "为了安全，越来越花时间；最少提前一个小时到机场，办登机手续，通过安检；人多时最少排一个多小时的队", "车站多半在城内，比较方便；速度快；很少晚点"],
             ["时间", "飞行时间再加上两三个小时的交通和等候时间", "从北京到上海最多不到五个小时"],
             ["结论", "越来越花时间", "为旅客省下不少时间，所以越来越多的人选择高铁"]],
            title="Activity 4A: notes on the passage (the book leaves the table blank; this is my filling)", say=[1, 2])
L4 = lesson(
    "Lesson 20 Presentation 2 grammar: 最多 and 最少",
    "最多 = at most, 最少 = at least · 坐飞机还是坐高铁 · 两真一假",
    requires=[],
    cards=[
        card("The usage of 最多 and 最少",
             "最多 indicates “maximum” and 最少 indicates “minimum.” These are generally placed after the subject and followed by a verb, number, measure word, or a noun. Sub + 最多 + verb + number + measure + noun. Sub + 最少 + verb + number + measure + noun. The book’s four examples, with the digits spelled out:",
             examples=[D(z, e) for z, e in ZE]),
        card("Activity 3 (Writing and Speaking)",
             "Think about your past experiences. Create three statements about yourself using 最多 and 最少, with two statements that are false and one that is true. See if your classmates can guess which statement about you is true. The book’s examples, followed by the question 哪个不是真的？",
             examples=[D(z, e) for z, e in ZS]),
        card("Activity 4 (Reading and Speaking)",
             "A. Read the following passage and take notes in the table about the aspects of air travel and high-speed rail. B. In Chinese, check your answer with your partner: Student A reports on the first column and Student B on the second. The passage:",
             tables=[TRV], examples=[D(*FLY)]),
    ],
    exercises=[
        M("What does 最多 mean?", "At most (maximum)", ["At least", "Most people", "Mostly"], "最多: maximum."),
        M("What does 最少 mean?", "At least (minimum)", ["At most", "Fewest people", "Rarely"], "最少: minimum."),
        M("Where do 最多 and 最少 usually stand?", "After the subject, before the verb", ["At the end of the sentence", "Before the subject", "After the object"], "Sub + 最多 + verb."),
        M("“From San Francisco to Taipei by air takes at least thirteen hours.”", "从旧金山坐飞机到台北最少要十三个小时。", ["从旧金山坐飞机到台北最多要十三个小时。", "从旧金山到台北最少坐飞机十三。", "最少从旧金山坐飞机到台北十三个小时要。"], "最少: at least."),
        M("“You need to prepare food for ten people at most.”", "你最多需要准备十个人的饭菜。", ["你最少需要准备十个人的饭菜。", "你需要准备最多十个人饭菜的。", "你最多准备需要十个人的饭菜。"], "最多: at most."),
        M("How early must people reach the airport for a domestic flight, according to the passage?", "At least one hour ahead", ["At most one hour ahead", "Three hours ahead", "Ten minutes ahead"], "最少要提前一个小时到机场."),
        M("Why are more people choosing the high-speed rail?", "Stations are in the city, it is fast and seldom late", ["It is cheaper than the bus", "Airports are closed", "Flights are free"], "高铁站多半在城内…速度快…很少晚点."),
        M("How long does Beijing to Shanghai take by high-speed rail at most?", "Less than five hours", ["About ten hours", "Two hours", "A whole day"], "最多不到五个小时."),
        M("What is added to the flying time?", "At least two or three more hours of transport and waiting", ["Nothing", "One day", "Ten minutes"], "最少还要再加上两三个小时."),
        F("我最___能认得三百个汉字。", "少", PART, "最少: at least."),
        F("你最___需要准备十个人的饭菜。", "多", PART, "最多: at most."),
        F("要通过考试，你最少要认___一千六百个汉字。", "识", PART, "认识: know."),
    ],
)

# ------------------------------------------------------------------ 5. 要看
YK = [("保险费是多少？", "A: How much is the insurance?"), ("那得看你保多少了。", "B: That depends on how much you insure it for."),
      ("你明天参不参加聚会？", "A: Are you going to the party tomorrow?"), ("那要看我女朋友了。", "B: That depends on my girlfriend."),
      ("老师，我能不能通过语言能力考试？", "A: Teacher, can I pass the language proficiency test? (the book writes DLPT)"), ("那得看你学习够不够努力了。", "B: That depends on whether you study hard enough.")]
YK2 = [("学不学音乐要看孩子的兴趣。", "4. Whether to learn music depends on the child’s interest."), ("能不能留在美国得看我能不能拿到签证。", "5. Whether I can stay in the U.S. depends on whether I can get a visa.")]
QS = [("我什么时候练习听力最好？", "那得看你什么时候有空了。", "When is the best time for me to practice listening? — That depends on when you are free. (answer mine)"), ("我应该怎么记生词？", "那得看你习惯怎么学了。", "How should I memorize new words? — That depends on how you are used to studying. (mine)"),
      ("我的学习这么紧张，周末我应该出去玩吗？", "那要看你的作业做完了没有。", "My studies are so intense: should I go out and play on the weekend? — That depends on whether you have finished your homework. (mine)"), ("我怎么样才能通过我的单元考试？", "那要看你学习够不够努力了。", "How can I pass my unit test? — That depends on whether you study hard enough. (mine)"),
      ("我应不应该在这里找个女朋友/男朋友？", "这得看你有没有时间了。", "Should I find a girlfriend/boyfriend here? — That depends on whether you have the time. (mine)"), ("周末的时候，在蒙特雷做什么活动最好？", "那要看你喜欢什么了。", "What is the best activity to do on weekends in Monterey? — That depends on what you like. (mine)")]
QD = []
for q, a, e in QS:
    QD += dlg([("甲", q, "Question: " + e.split(" — ")[0]), ("乙", a, "Answer: " + e.split(" — ")[1])])
L5 = lesson(
    "Lesson 20 Presentation 2 grammar: 要看 and 得看 (it depends)",
    "那得看你保多少了 · 那要看我女朋友了 · 要看孩子的兴趣",
    requires=[],
    cards=[
        card("The use of 要看",
             "要看 and 得看 are colloquial expressions, meaning “it depends (on).” They can be followed by a pronoun, a phrase or a sentence. In conversation, 这/那 is often placed before 要看 and 得看 to refer to the unknown outcome or topic previously discussed. In a statement, an unknown outcome can be used as a subject followed by 要看 or 得看 and an unclear situation. Pattern 1: (这/那) + 要看/得看 + unclear situation + 了 (examples 1–3). Pattern 2: unknown outcome + 要看/得看 + unclear situation (examples 4–5). Here 得 in 得看 is read děi.",
             examples=[D(z, e) for z, e in YK + YK2]),
        card("Activity 5 (Reading, Speaking and Listening)",
             "A new student from another class has struggled with life at DLI and in Monterey. Answer his questions by providing suggestions using 要看 or 得看. Pair up: Student A asks the questions and Student B offers suggestions; the students switch roles and take notes. The book lists six questions and two blank lines for your own questions; my suggested answers (the book prints none):",
             examples=QD),
    ],
    exercises=[
        M("What do 要看 and 得看 mean?", "It depends (on)", ["It must be seen", "It is hard to see", "Look at it"], "要看/得看: it depends."),
        M("How is 得看 read?", "děi kàn", ["dé kàn", "de kàn", "dì kàn"], "得 as “must” is děi."),
        M("“保险费是多少？” — which reply is in the book?", "那得看你保多少了。", ["我也不知道。", "三百八十七块五。", "不要保险。"], "那得看你保多少了."),
        M("What does 那要看我女朋友了 mean?", "That depends on my girlfriend", ["I will see my girlfriend", "My girlfriend must look", "I am looking at her"], "要看…了: depends."),
        M("What word is often placed before 要看 in conversation?", "这/那", ["很/都", "不/没", "和/跟"], "(这/那) + 要看/得看."),
        M("“学不学音乐要看孩子的兴趣。” Which pattern is this?", "Unknown outcome as the subject + 要看 + the situation", ["这/那 + 要看 + 了", "Imperative", "A question"], "Pattern 2."),
        M("What does 能不能留在美国得看我能不能拿到签证 mean?", "Whether I can stay depends on whether I get a visa", ["I will get a visa in America", "I can not stay", "I stay and see the visa"], "得看: depends."),
        M("Which sentence is the best reply to “我应该怎么记生词？” (mine)?", "那得看你习惯怎么学了。", ["对，你应该去邮局。", "我不知道你是谁。", "今天不太热。"], "A suggestion with 得看."),
        F("那得___你保多少了。", "看", PART, "得看: depends."),
        F("那___看我女朋友了。", "要", PART, "要看: depends."),
        F("能不能留在美国得看我能不能拿到___证。", "签", PART, "签证: visa."),
    ],
)

# ------------------------------------------------------------------ 6. 不过 但是 可是
BG = table(["不过", "可是", "但是"], [["Softer tone", "Stronger tone, more colloquial", "Strongest tone, more formal"]], title="不过 · 可是 · 但是 (the book’s table)")
BE = [("特快专递最快，但是价钱有点儿贵。", "Express is fastest, but the price is a little high."), ("空运、海运慢一点，不过价钱便宜很多。", "Air and sea are a little slower, but the price is much cheaper."),
      ("我很喜欢学中文，不过汉字很难学。", "I like studying Chinese, but characters are hard to learn."), ("我想去听这场音乐会，可是我买不到票。", "I want to go to this concert, but I can’t get a ticket.")]
EN6 = [("但是加上去机场和安检的时间，和坐高铁差不多。", "a. But adding the time to go to the airport and through security, it is about the same as taking the high-speed rail."), ("可是厨具很全，冰箱、洗碗机都有。", "b. But the kitchen equipment is complete, there is a refrigerator and a dishwasher."),
       ("可是不管输赢，他都很开心。", "c. But whether he wins or loses, he is always happy."), ("不过不用担心，这些东西都可以在滑雪场租到。", "d. But don’t worry, you can rent all of these at the ski resort."),
       ("可是要是你没用过那些器械，很容易受伤。", "e. But if you haven’t used those apparatuses, it is easy to get hurt."), ("可是有各种各样的海洋动物。", "f. But there are all kinds of sea animals."), ("不过你得设一个用户名和密码。", "g. But you have to set up a user name and a password.")]
MY6 = [("从北京到上海坐飞机只要两个小时，但是加上去机场和安检的时间，和坐高铁差不多。", "1 + a. From Beijing to Shanghai it only takes two hours by air, but adding the time to go to the airport and through security, it is about the same as the high-speed rail. (first half mine)"), ("这个公寓不大，可是厨具很全，冰箱、洗碗机都有。", "2 + b. This apartment isn’t big, but the kitchen equipment is complete: there is a refrigerator and a dishwasher. (first half mine)"),
       ("他们的球队常常输球，可是不管输赢，他都很开心。", "3 + c. His team often loses, but whether they win or lose, he is always happy. (first half mine)"), ("去滑雪要带很多东西，不过不用担心，这些东西都可以在滑雪场租到。", "4 + d. You need to take a lot of things skiing, but don’t worry, you can rent all of them at the ski resort. (first half mine)"),
       ("滑雪很好玩，可是要是你没用过那些器械，很容易受伤。", "5 + e. Skiing is fun, but if you haven’t used those apparatuses it is easy to get hurt. (first half mine)"), ("这个水族馆不大，可是有各种各样的海洋动物。", "6 + f. This aquarium isn’t big, but it has all kinds of sea animals. (first half mine)"),
       ("你可以免费用这个网站，不过你得设一个用户名和密码。", "7 + g. You can use this website for free, but you have to set up a user name and a password. (first half mine)")]
L6 = lesson(
    "Lesson 20 Presentation 2 grammar: 不过, 但是 and 可是",
    "三个“但是” · 语气的轻重 · 配对练习",
    requires=[],
    cards=[
        card("The use of 不过、但是 and 可是",
             "不过, 但是 and 可是 are similar in meaning, indicating “but,” “nevertheless,” or “however” and are often used interchangeably. However, 不过 has a softer tone, while 但是 and 可是 express stronger tones, with 但是 being more formal and 可是 more colloquial.",
             tables=[BG], examples=[D(z, e) for z, e in BE]),
        card("Activity 6 (Listening, Reading and Speaking)",
             "A. Listen to the first part of each sentence and match it with the appropriate ending by writing its letter in the parentheses. The book prints the seven endings (a to g) and the first halves are only on the audio (not included), so I wrote one first half for each ending as my own reconstruction. B. Pair up and check your answers by reading them aloud and translating the entire sentence; the book leaves seven lines for the translations. The seven endings as printed:",
             examples=[D(z, e) for z, e in EN6]),
        card("My complete sentences for Activity 6",
             "The book prints no first halves and no key, so the pairs and the translations below are mine.",
             examples=[D(z, e) for z, e in MY6]),
    ],
    exercises=[
        M("Which of 不过, 但是, 可是 has the softest tone?", "不过", ["但是", "可是", "They are all the same"], "不过: softer."),
        M("Which is the most formal?", "但是", ["不过", "可是", "没有"], "但是: strongest, more formal."),
        M("Which is the most colloquial strong “but”?", "可是", ["但是", "不过", "而且"], "可是: stronger, more colloquial."),
        M("“I like studying Chinese, but characters are hard to learn.” Which connector does the book use?", "不过", ["因为", "所以", "而且"], "我很喜欢学中文，不过汉字很难学."),
        M("“I want to go to this concert, but I can’t get a ticket.” Which connector does the book use?", "可是", ["不过", "所以", "还有"], "我想去听这场音乐会，可是我买不到票."),
        M("What does ending d say?", "Don’t worry, everything can be rented at the ski resort", ["Skiing is dangerous", "The ski resort is closed", "You must buy equipment"], "不用担心…可以在滑雪场租到."),
        M("What does ending g say?", "You have to set up a user name and a password", ["The website is free of charge", "You need a phone", "You cannot register"], "你得设一个用户名和密码."),
        M("What does ending f say?", "There are all kinds of sea animals", ["The kitchen is complete", "He is always happy", "It takes five hours"], "有各种各样的海洋动物."),
        F("特快专递最快，___是价钱有点儿贵。", "但", PART, "但是: but (formal)."),
        F("我很喜欢学中文，不___汉字很难学。", "过", PART, "不过: but (soft)."),
        F("我想去听这场音乐会，___是我买不到票。", "可", PART, "可是: but (colloquial)."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
RT = table(["寄到", "平信", "航空信", "挂号信", "回执"],
           [["本市", "¥1.5", "(none printed: one ¥1.5 value is shown for the city)", "+1.50", "+0.30"], ["中国其他省市", "¥1.6", "¥1.8", "+2.00", "+0.50"], ["香港、台湾", "¥2.8", "¥3.5", "+3.00", "+0.50"],
            ["日本、韩国", "¥4.7", "¥6.2", "+6.30", "+0.60"], ["美国", "¥5.4", "¥6.4", "+6.50", "+0.80"], ["加拿大", "¥5.4", "¥6.4", "+6.50", "+0.80"], ["新西兰", "¥4.7", "¥6.2", "+6.30", "+0.80"]],
           title="Activity 3B: the postal rates in yuan (the + rows for 挂号信 and 回执 are added to the postage)")
SI3 = [("刘国华想往上海寄一封航空挂号信。", "1. Liu Guohua wants to mail an airmail registered letter to Shanghai."), ("营业员让刘国华填张回执单。", "2. The clerk asks Liu Guohua to fill in a return-receipt form."), ("刘国华要寄往广州的信没超重。", "3. The letter Liu Guohua wants to send to Guangzhou is not overweight."),
       ("除了寄信，刘国华还买了信封和邮票。", "4. Besides mailing a letter, Liu Guohua also bought envelopes and stamps."), ("刘国华买了十个信封和十张两块钱的邮票。", "5. Liu Guohua bought ten envelopes and ten two-yuan stamps. (the book writes 十 in characters)"), ("邮费加上信封和邮票一共是五十三块整。", "6. The postage plus the envelopes and stamps came to 53 yuan exactly. (the book writes 五十三 in characters)")]
SK3 = [("顾客", "你好，我想寄五封信到美国。", "Hello, I want to send five letters to the U.S. (mine)"), ("营业员", "你要寄平信还是航空信？", "Do you want ordinary mail or airmail? (mine)"), ("顾客", "航空信比平信快多少？", "How much faster is airmail than ordinary mail? (mine)"),
       ("营业员", "航空信快不少，不过也贵一点儿。寄到美国，平信五块四，航空信六块四。", "Airmail is quite a bit faster, but also a little dearer. To the U.S. ordinary mail is 5.4 yuan, airmail 6.4. (mine)"), ("顾客", "那我要航空信。五封一共多少钱？", "Then I’ll take airmail. How much is it for five altogether? (mine)"),
       ("营业员", "一共三十二块。要不要挂号？", "Thirty-two yuan altogether. Do you want it registered? (mine)"), ("顾客", "不用了，谢谢。", "No need, thank you. (mine)")]
ST4 = ("上个星期我到邮局寄了一个特快专递的包裹给我女朋友。邮局的营业员告诉我，特快专递最快，最多只要三个工作日。因为这个礼物有些贵重，我还买了保险，一共花了五十六块钱。今天是我女朋友的生日，我给她打电话，祝她生日快乐，才知道她还没收到我的包裹。打完电话，我马上去邮局。邮局的营业员让我给他看那天的收据，然后问我有没有按照上面的二维码查包裹是不是已经寄到了。我告诉他网上说寄到了，但是我的女朋友没收到。他用电脑又帮我查了一遍，告诉我东西应该已经寄到了，因为包裹一送到寄件地址，邮差就扫码通知邮局了。他让我再问问女友或她的家人，看是不是她的家人已经帮她领了或者邮差留了一张条子通知她去邮局领。",
       "Last week I went to the post office and mailed an express parcel to my girlfriend. The clerk told me express is fastest, only three working days at most. Because the gift is somewhat valuable I also bought insurance; it cost 56 yuan altogether. Today is my girlfriend’s birthday; I phoned her to wish her a happy birthday and only then learned that she had not received my parcel yet. After the call I went straight to the post office. The clerk asked me to show him the receipt from that day and then asked whether I had used the QR code on it to check whether the parcel had arrived. I told him the web said it had arrived but my girlfriend hadn’t received it. He checked again on the computer and told me the item should already have been delivered, because as soon as a parcel reaches the delivery address the postman scans the code and notifies the post office. He told me to ask my girlfriend or her family again, to see whether her family had already collected it for her or the postman had left a note telling her to collect it at the post office. (the book prints 3 and 56 as digits)")
SKIT = [("顾客", "您好，我上个星期寄了一个特快专递，可是我女朋友还没收到。", "Hello, I mailed an express parcel last week but my girlfriend still hasn’t received it. (skit mine)"), ("营业员", "请把那天的收据给我看一下。你按收据上的二维码查过没有？", "Please show me that day’s receipt. Have you checked with the QR code on it? (mine)"),
        ("顾客", "查过了。网上说寄到了，可是我女朋友没收到。", "I have. The web says it arrived, but my girlfriend didn’t receive it. (mine)"), ("营业员", "我用电脑再帮你查一遍。……东西应该已经寄到了，邮差一送到就扫码通知我们了。", "Let me check again on the computer… The item should have arrived; the postman scans the code to notify us as soon as he delivers. (mine)"),
        ("顾客", "那怎么办呢？", "Then what should I do? (mine)"), ("营业员", "你再问问你女朋友或她的家人，看是不是家人已经帮她领了，或者邮差留了一张条子，通知她来邮局领。", "Ask your girlfriend or her family again to see whether the family collected it for her, or whether the postman left a note telling her to collect it at the post office. (mine)"),
        ("顾客", "好，谢谢您。我马上给她打电话。", "OK, thank you. I’ll call her right away. (mine)")]
BL = ("我是小丽，是纽约大学的中国留学生。今天想跟大家说说我去美国邮局的经验。在国内我们都是用网路联系，几乎很少有人去邮局寄信。可是在美国，许多重要的文件还是得靠邮局寄送，所以到邮局寄信也几乎是留学生一定会有的体验。还记得第一次到邮局寄东西，邮局里的牌子上写着各种不同的寄信方式和计费方式，让我非常头疼。在美国，一共有三种寄件方式，如果已经贴了足够的邮费，而且信件或包裹没有超重就可直接放进邮局的投递箱里。很多人网购以后想要退东西，也是直接把包裹放进投递箱里。第二种寄件方式是，如果不知道该用哪种方式邮寄，也不知道是不是贴够了邮票，那就得直接去邮局，排队请邮局的工作人员帮助你，他们会帮你称重，然后告诉你可以怎么寄。第三种是使用邮局门口的自动柜员机，按照显示屏上一步一步去做就可以完成寄送手续。我觉得最简单的办法就是花一点时间问问邮局的营业员。这样，你就能找到比较适合你的邮寄选择。",
      "I am Xiaoli, a Chinese student studying at New York University. Today I’d like to tell everyone about my experience at the American post office. In China we all keep in touch over the internet and almost nobody goes to the post office to send letters. But in America many important documents still have to be sent through the post office, so mailing a letter at the post office is almost an experience every international student will have. I still remember the first time I went to mail something: the signs in the post office listed all kinds of different ways of sending and ways of charging, which gave me a big headache. In America there are three ways of sending. If you have already put on enough postage and the letter or parcel is not overweight, you can put it straight into the post office’s drop box. Many people who want to return something bought online also put the parcel directly into the drop box. The second way is that if you don’t know which method to use, and don’t know whether you have put on enough stamps, then you must go straight to the post office, queue, and ask the staff to help you; they will weigh it for you and tell you how you can send it. The third is to use the self-service machine at the post office door and complete the mailing by following the screen step by step. I think the simplest way is to spend a little time asking the clerk at the post office. That way you will find the mailing choice that suits you best.")
L7 = lesson(
    "Lesson 20 Presentation 2 skill integration: postal rates, a missing parcel, mailing in America",
    "平信 邮政编码 挂号信 回执 · 邮资表 · 特快专递没收到 · 小丽在美国邮局",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "New vocabulary: 平信 (píngxìn; surface/first class mail), 邮政编码 (yóuzhèng biānmǎ; zip code). A. Listen to the following sentences twice and answer: 1. What did the clerk say? 2. What was being explained? 3. What question was asked? 4. What did the man say? 5. What was said about the letter? 6. What did the customer ask for? B. Pair up and, in Chinese, share your answers with your partner. (Audio, not included; the book prints no script.)"),
        card("Activity 2 (Listening, Speaking and Reading)",
             "New vocabulary: 挂号信 (guàhào xìn; registered mail). A. Pair up. Student A listens to Dialog 1 and Student B listens to Dialog 2; each writes a summary and at least four details. B. Students share their information in Chinese and their partner fills in the other column. C. Students read the script and check their answers. (Audio and a script that this text does not print, so nothing to include.)"),
        card("Activity 3 (Listening, Reading and Speaking)",
             "New vocabulary: 回执 (huí zhí; return receipt). A. Listen to the following conversation and mark each statement True or False; explain your choices in Chinese. The audio is not included and the book prints no key, so I give the six statements without an answer key. B. Pair up. You are in Beijing and want to mail several letters to your friends before Christmas. Check the postal rates below and carry out a conversation with a postal clerk; your partner plays the postal clerk. The statements, then the rates, then a sample conversation of mine:",
             tables=[RT], examples=[D(z, e) for z, e in SI3] + dlg(SK3)),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Read the passage about a customer’s experience at the post office and answer: 1. Provide at least two details. 2. What happened to the package? 3. What information was provided by the postal clerk during the customer’s second visit? 4. What was the customer instructed to do? B. Pair up and create a skit of a conversation between the postal clerk and the customer on his second visit (the book leaves lines for A and B, seven each). C. Present your skit to the class. The passage, then my skit:",
             examples=[D(*ST4)] + dlg(SKIT)),
        card("Activity 5 (Reading, Writing and Speaking)",
             "New vocabulary: 头疼 (tóuténg; headache). A. Below is a blogger’s post regarding the U.S. postal service. Read the passage and create a mind map to summarize the post. The book asks “What is his suggestion?” (the blogger is 小丽, so I treat it as “her”). B. Use the mind map to share the information with your partner in Chinese. My mind map in words: the center is “去美国邮局寄东西”; the branches are 1. 直接放进投递箱 (stamps enough, not overweight; also for returns of online purchases), 2. 去邮局排队请营业员帮忙 (they weigh and tell you how to send), 3. 用邮局门口的自动柜员机 (follow the screen); her suggestion is to ask the clerk. The passage:",
             examples=[D(*BL)]),
    ],
    exercises=[
        M("What is a 平信?", "Surface (first-class) mail", ["Registered mail", "Express mail", "A parcel"], "平信: ordinary mail."),
        M("What is a 挂号信?", "Registered mail", ["Airmail", "Ordinary mail", "A postcard"], "挂号信."),
        M("What is 回执?", "A return receipt", ["A stamp", "A zip code", "A parcel form"], "回执."),
        M("What is 邮政编码?", "Zip code", ["Weight", "Price", "Address book"], "邮政编码."),
        M("According to the rate table, how much is ordinary mail to the U.S.?", "5.4 yuan", ["6.4 yuan", "6.5 yuan", "4.7 yuan"], "美国 平信 ¥5.4."),
        M("According to the table, how much is airmail to Japan and Korea?", "6.2 yuan", ["4.7 yuan", "6.3 yuan", "0.6 yuan"], "日本、韩国 航空信 ¥6.2."),
        M("In the express-parcel story, why did the customer buy insurance?", "The gift was somewhat valuable", ["It was required", "The postman asked", "It was cheap"], "因为这个礼物有些贵重."),
        M("How did the customer find out the parcel had not arrived?", "He phoned his girlfriend on her birthday", ["The clerk called", "He read a letter", "The QR code failed"], "给她打电话…才知道她还没收到."),
        M("What did the clerk say about delivery?", "As soon as the postman delivers, he scans the code and notifies the post office", ["The parcel was lost", "The parcel is still in the plane", "The sender must pay again"], "邮差就扫码通知邮局了."),
        M("What was the customer told to do?", "Ask his girlfriend or her family again, and look for the postman’s note", ["Send another parcel", "Pay a fine", "Go to customs"], "他让我再问问女友或她的家人."),
        M("How many ways of sending does Xiaoli list in America?", "Three", ["Two", "Four", "Five"], "一共有三种寄件方式."),
        M("What is her suggestion?", "Spend a little time asking the post-office clerk", ["Use only the drop box", "Never mail anything", "Use express only"], "最简单的办法就是…问问邮局的营业员."),
        F("邮局的牌子上写着各种不同的寄信方式，让我非常头___。", "疼", PART, "头疼: headache."),
        F("他让我再问问女友或她的家人，看是不是她的家人已经帮她___了。", "领", PART, "领: to collect."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
UC = [("你好，我想寄一封信到美国。", "1. Hello, I’d like to mail a letter to the U.S. (my sentence; the book asks for your own)"), ("请问，你们有哪几种邮寄方式？", "2. Excuse me, which mailing methods do you have? (mine)"), ("平信、航空信、挂号信和特快专递有什么不一样？", "3. How do ordinary mail, airmail, registered mail and express differ? (mine)"),
      ("寄一封信到纽约，需要多少邮费？", "4. How much postage is needed to mail a letter to New York? (mine)"), ("我要买五张八毛的邮票和两张两块八的邮票。", "5. I’d like five 80-cent stamps and two 2.8-yuan stamps. (mine; the book writes 80 and 2.8)"),
      ("寄特快专递的包裹比寄普通的包裹贵多少？", "6. How much more does it cost to mail an express parcel than an ordinary one? (mine)"), ("寄特快专递的包裹比寄普通的包裹贵得多。", "7. Mailing an express parcel costs much more than an ordinary one. (mine)"),
      ("空运寄一封信或者一个包裹到美国，大概要几天？", "8. About how many days does it take to send a letter or parcel to the U.S. by air? (mine)"), ("包裹单上的地址可以用英文写吗？", "9. Can the address on the parcel form be written in English? (mine)"),
      ("我的中文写得不太好，请你看看我填得对不对。", "10. My Chinese writing isn’t very good; please look and see whether I filled it in correctly. (mine)")]
ADD = table(["情景", "地址 (the book’s digits)"], [["Scenario 1: your address", "10645 台北市大安區師大路 9 号"], ["Scenario 1: their address", "70101 台南市东区大学路一号"], ["Scenario 2: your address in Taiwan", "10461 台北市中山北路 4 段 1 号"]],
            title="The addresses in Activity 2 (the book’s digits are the postal codes and house numbers; the postal code goes first, then larger to smaller units)")
EA = [("国内邮件直式信封书写方式：第一步，把收信人的姓名写在信封的中间，地址写在信封的右边，邮递区号用阿拉伯数字写在信封右上方的红框格内。", "Instruction A, how to write a vertical envelope for domestic mail. Step 1: write the addressee’s name in the middle of the envelope and the address on the right side, and the postal code in Arabic numerals in the red boxes at the upper right of the envelope."),
      ("第二步，把寄信人地址、姓名写在信封的左下方，邮递区号以阿拉伯数字写在信封左下方红框格内。", "Step 2: write the sender’s address and name at the lower left of the envelope, and the postal code in Arabic numerals in the red boxes at the lower left."), ("第三步，最后把邮票贴在信封左上方。", "Step 3: finally stick the stamp at the upper left of the envelope."),
      ("国外邮件信封书写方式：第一步，把收信人的地址、姓名和邮递区号写在信封中间靠右的地方。", "Instruction B, how to write an envelope for international mail. Step 1: write the addressee’s address, name and postal code in the middle, toward the right, of the envelope."),
      ("第二步，把寄信人地址、姓名和邮递区号写在信封左上方或信封的后面。", "Step 2: write the sender’s address, name and postal code at the upper left or on the back of the envelope."), ("第三步，最后把邮票贴在信封的右上方。", "Step 3: finally stick the stamp at the upper right of the envelope.")]
L8 = lesson(
    "Lesson 20 Presentation 2 using Chinese in context: at the post office and addressing envelopes",
    "十个常用句 · 顾客和营业员 · 台湾的信封 · 台湾和美国的邮局",
    requires=[],
    cards=[
        card("Activity 1 (Speaking and Listening)",
             "A. You are in China and need to mail a package and several letters. Pair up and think of how to say these in Chinese: 1. What would you say to the clerk if you want to mail a letter or package to the U.S.? 2. What would you ask if you wanted to know your mailing options? 3. How do the options differ (first class, air mail, registered mail, express mail)? 4. How much postage is needed to mail a letter to New York? 5. What would you say if you needed to purchase five 80-cent stamps and two 2.8-yuan stamps? 6. How much more does a special express package cost than an ordinary package? 7. Say that mailing a special express package costs much more than an ordinary one. 8. About how long does it take a letter or package to travel to the U.S. by air? 9. Can you write addresses on packages in English? 10. Tell the clerk you can’t write Chinese well and ask him to look and see whether you have correctly filled in the necessary form. My sentences (the book prints none):",
             examples=[D(z, e) for z, e in UC]),
        card("Activity 1B (role play)",
             "Now you are at the post office in China and need to mail these letters and a package; consult with the post office clerk, played by your partner, then switch roles. A customer needs to ask: the mailing options; the price differences of different options; the time that it takes for the letter to reach the recipient; if the letter is overweight; how much postage you need to pay (surface, airmail, registered or express); if the package form is correctly filled; if you can track your package and how to do it. A postal clerk needs to ask or explain: different mailing options; the content of the package; how the customer must fill out various forms; if the customer wants to purchase insurance; if the customer wants a return receipt; if the customer wants additional services; how the customer wants to pay; the tracking information."),
        card("Activity 2 (Reading, Speaking and Listening)",
             "New vocabulary: 邮递区号 (yóu dì qū hào; postal code), a term often used in Taiwan. Below are instructions on how to fill out a formal vertical envelope for domestic mail and a horizontal-style envelope for international mail in Taiwan. A. Pair up. Student A reads Scenario 1 (you are travelling in Taiwan, took photos with some local people in Tainan and want to mail the photos to them) and Instruction A; Student B reads Scenario 2 (you bought souvenirs in Taiwan and want to send them home to your family) and Instruction B; follow the instruction to fill out the envelopes. B. Use the envelope you filled out to teach each other how to do it properly. Note: unlike addresses written in English, a Chinese address puts the postal code first, followed by larger to smaller units (city, road/street/alley, house number). The book prints the instructions mostly in traditional characters (and gives links to animations at the Taiwan post office website); here they are in simplified characters:",
             tables=[ADD], examples=[D(z, e) for z, e in EA]),
        card("Activity 2C and Activity 3",
             "C. The format of mailing a domestic letter in China is different than in the U.S. Listen to a short passage and write an English summary of it. (Audio, not included.) Activity 3 (Reading, Speaking, Listening and Writing): You are in Taiwan for immersion learning and have learned some facts about the postal services in Taiwan; your teachers would like to know about the postal services in the U.S. A. Form groups of three and list the functions of both the U.S. and the Taiwanese postal service (the book points to the Taiwanese Postal Service website and the U.S. postal service’s Chinese website; links are not included). B. Use the Venn diagram (台湾的邮局 | 美国的邮局, not included) to illustrate the similarities and differences. C. Make a presentation to the class in Chinese describing the American and Taiwanese postal services. D. The class takes notes and votes for the best presentation. From this lesson only (mine): both send letters and parcels and sell stamps; the U.S. has the drop box, the clerk and the self-service machine; in Taiwan the postal code goes on the envelope in red boxes and comes first in the address."),
    ],
    exercises=[
        M("Which sentence asks about postage to New York?", "寄一封信到纽约，需要多少邮费？", ["包裹单上的地址可以用英文写吗？", "你想怎么寄？", "我要买五张邮票。"], "邮费 = postage."),
        M("Which sentence asks whether an address can be written in English?", "包裹单上的地址可以用英文写吗？", ["寄一封信到纽约需要多少邮费？", "你们有哪几种邮寄方式？", "请你看看我填得对不对。"], "可以…吗?"),
        M("How do you say “I’d like five 80-cent stamps”?", "我要买五张八毛的邮票。", ["我要买八张五毛的邮票。", "我要寄五封信。", "我要五个邮局。"], "五张八毛的邮票."),
        M("How do you say 2.8 yuan in speech?", "两块八", ["二十八块", "八块二", "两百八十块"], "两块八."),
        M("What is 邮递区号?", "Postal code (the term often used in Taiwan)", ["Phone number", "Street name", "Stamp price"], "邮递区号."),
        M("In a Taiwan address, which comes first?", "The postal code", ["The house number", "The name", "The city only"], "邮递区号先写."),
        M("In Instruction A (domestic, vertical), where does the stamp go?", "At the upper left", ["At the upper right", "At the lower left", "On the back"], "邮票贴在信封左上方."),
        M("In Instruction B (international), where does the stamp go?", "At the upper right", ["At the upper left", "At the lower left", "On the back"], "邮票贴在信封的右上方."),
        M("In Instruction A, where does the sender’s information go?", "At the lower left", ["At the upper right", "In the middle", "At the upper left"], "寄信人地址、姓名写在信封的左下方."),
        M("In Instruction B, where may the sender’s information go?", "At the upper left or on the back", ["In the middle", "At the lower right", "Nowhere"], "信封左上方或信封的后面."),
        F("邮递区号用阿拉伯___字写在信封右上方的红框格内。", "数", PART, "数字: numerals."),
        F("我的中文写得不太好，请你看看我填得___不对。", "对", PART, "对不对."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 20 Presentation 2 vocabulary", "22 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第二十课 Presentation 2: 寄包裹, 比 + 程度, 最多/最少, 要看, 不过/但是/可是", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
