"""Unit 25: Lesson 9 (Shopping) Presentation 1, from the book's texts: buying clothes, the Chinese money units, 有(一)点儿 + adjective,
adjective + 了(一)点儿, adjective + (一)点儿, the passages, advertisements, colors, a mother's letter and the vocabulary list.
The listening and video activities, the pictures and the fill-in tables are not included; the lessons say so."""
from zh_auto import *
from zh_l9_vocab import VOC1

PART = ["吗", "们", "呢"]
FOOD = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [
    ("凯丽", "大卫，我觉得这件衣服样式不错。你说呢？", "David, I think this piece of clothing has a nice style. What do you say?"),
    ("大卫", "是不错。你穿一定很好看。", "It is nice. You would certainly look good in it."),
    ("凯丽", "那我去试试。服务员，请问试衣间在哪儿？", "Then I’ll go try it on. Excuse me, where is the fitting room?"),
    ("服务员", "就在收银台后边。", "Right behind the cash register."),
    ("凯丽", "大卫，你看怎么样？", "David, how does it look?"),
    ("大卫", "不错！不过，好像有点儿大。", "Nice! But it seems a little big."),
    ("凯丽", "服务员，这件衣服大了一点儿。有没有小一号的？", "Excuse me, this piece is a little too big. Do you have one a size smaller?"),
    ("服务员", "这种颜色的没有了，可是我们有粉色和蓝色的。今天都降价，全部打八折。", "We’re out of this color, but we have pink and blue. Everything is on sale today, all at 20% off."),
    ("凯丽", "那，请给我拿一件粉色的试试。", "Then please bring me a pink one to try."),
    ("服务员", "好，您稍等。", "Okay, one moment please."),
    ("凯丽", "这件很合适，就买这件吧！", "This one fits very well; let’s buy this one!"),
    ("大卫", "多少钱？", "How much is it?"),
    ("服务员", "原价三百六十块，打八折以后是二百八十八。你们怎么付费？", "The original price is 360 yuan; after 20% off it is 288. How are you paying?"),
    ("大卫", "可以手机扫码吗？", "Can we scan a code with a cell phone?"),
    ("服务员", "可以。", "Yes."),
]
MATCH1 = [("甲", "这种颜色的没有了，可是有粉色和蓝色的。", "We’re out of this color, but we have pink and blue."), ("乙", "就在收银台那儿。", "Right there at the cash register."), ("丙", "原价三百六十块，打八折以后是二百八十八。", "The original price is 360 yuan; after 20% off it is 288."),
          ("丁", "不错！不过，好像有点儿大。", "Nice! But it seems a little big."), ("戊", "用手机扫码。", "Scan a code with the cell phone.")]
L1 = lesson(
    "Lesson 9 Presentation 1: shopping for clothes (dialog)",
    "这件衣服样式不错 · 试衣间在哪儿？ · 大了一点儿 · 打八折 · 手机扫码",
    requires=[],
    cards=[
        card("Lesson 9 Shopping: objectives",
             "第九课 买东西. Upon completion of this lesson you will be able to obtain and provide information about shopping: asking and giving opinions, asking to exchange one item for another, asking for the unit and total price, negotiating a price and asking for the payment method; and narrate a past shopping experience. To do this you must master: the new words and phrases of the Core Vocabulary; the basic monetary units; the basic units of weight; 有一点儿 + adjective; adjective + 一点儿; adjective 了 + 一点儿; measure words for clothing, daily necessities and produce; basic color names; 快 + verb + 了; 就 (just, only); the 连…也/都… pattern; and the pivotal construction 请. Area Studies: Shopping in China."),
        card("Getting Started",
             "Pair up and discuss. A. When was the last time you shopped for clothes? Where did you go? What did you buy? B. What are some questions you might ask the store clerk? Can you ask them in Chinese?"),
        card("Presentation 1: 凯丽 and 大卫 in a clothing store",
             "The book also prints the dialog in traditional characters (for example 服務員，請問試衣間在哪兒？).",
             examples=dlg(P1)),
        card("Activity 2 (Listening): global and detailed listening",
             "A. Who are the three speakers and what is their relationship? What information is being exchanged? B. What were the two issues the shopper encounters? How were they resolved? Why did they mention a cell phone? (The recording is not included. From the text: Kelly, David and a shop assistant; Kelly and David are friends or a couple shopping together, and the third is the clerk; they exchange opinions on style and fit, then the size, color and price. The two issues: the item was a little big and the color was out of stock; the clerk offered pink and blue and Kelly took a pink one. The cell phone: they will pay by scanning a code. This key is mine.)"),
        card("Activity 3 (Listening, Reading and Speaking): match the questions with the answers",
             "Listen to the key questions from the presentation (audio, not included) and match them with their answers; then Student A reads the answers aloud while Student B recalls the questions. The five answers (a to e, shown here as 甲 to 戊):",
             examples=[D(f"{a}．{z}", e) for a, z, e in MATCH1]),
    ],
    exercises=[
        M("What does 凯丽 think of the piece of clothing at first?", "Its style is nice", ["It is too expensive", "It is the wrong color", "It is too small"], "我觉得这件衣服样式不错。"),
        M("Where is the fitting room?", "Right behind the cash register", ["Next to the door", "Upstairs", "Behind the fitting room"], "就在收银台后边。"),
        M("What is wrong with the first piece when she tries it on?", "It seems a little big", ["It is too small", "It is torn", "It is too expensive"], "好像有点儿大。"),
        M("What does 凯丽 ask for?", "One size smaller", ["One size larger", "A cheaper one", "A different shop"], "有没有小一号的？"),
        M("What colors does the clerk offer instead?", "Pink and blue", ["Red and green", "Black and white", "Yellow and brown"], "我们有粉色和蓝色的。"),
        M("What discount is on today?", "Everything is 20% off (打八折)", ["Everything is 80% off", "Buy one, get one free", "No discount"], "全部打八折: pay 80 percent."),
        M("Which color does 凯丽 try?", "Pink", ["Blue", "The original color", "Black"], "请给我拿一件粉色的试试。"),
        M("What is the original price?", "360 yuan", ["288 yuan", "80 yuan", "630 yuan"], "原价三百六十块。"),
        M("What is the price after the discount?", "288 yuan", ["360 yuan", "280 yuan", "300 yuan"], "打八折以后是二百八十八。"),
        M("How do they pay?", "They scan a code with a cell phone", ["With cash", "With a check", "They don’t pay"], "可以手机扫码吗？ 可以。"),
        F("服务员，这件衣服大了一点儿。有没有小一___的？", "号", PART, "号 means size."),
        F("今天都降价，全部打八___。", "折", PART, "打八折: eight-tenths of the price."),
        F("请问，试衣间在___儿？", "哪", ["这", "那", "几"], "在哪儿: where."),
        mean("试衣间", "shi4 yi1 jian1", "fitting room", ["cash register", "shop assistant", "original price"]),
        mean("原价", "yuan2 jia4", "original price", ["fitting room", "discount", "size"]),
    ],
)

# ------------------------------------------------------------------ 2. activities 1, 4, 5
CLASS = [("颜色", "蓝色 · 粉色"), ("挑选标准 (selection criteria)", "颜色 · 样式 · 合适"), ("店里的地方 (places in the store)", "收银台 · 试衣间"), ("人 (people)", "客人 · 服务员"), ("价钱和付款 (prices and payments)", "原价 · 降价 · 打折 · 付费")]
CLOZE9 = [("买完东西得去___付钱。", "收银台"), ("这个周末这个商店的衣服都___。", "降价"), ("买衣服的时候，我一定要___穿才知道合适不合适。", "试"), ("这件衣服不太___，有一点儿小。", "合适"),
          ("现在去很多商店买东西可以用手机___。", "扫码"), ("这个商店的衣服___、颜色都很多，所以我常来这里买。", "样式"), ("我想买这件蓝___的衣服，不过他们没有我要的中号。", "色")]
DLG5 = [("售货员", "您好！您想买什么？", "Hello! What would you like to buy?"), ("顾客", "我想买件衬衫。", "I would like to buy a shirt."), ("售货员", "您想要什么颜色的？", "What color would you like?"), ("顾客", "蓝颜色的。", "A blue one."),
        ("售货员", "您穿多大号的？这件中号的，您试试。", "What size do you wear? Try this medium one."), ("顾客", "好像小了点儿。给我拿件儿大号的试试吧。", "It seems a little small. Please bring me a large one to try."),
        ("售货员", "对不起，蓝色大号的没有了。黑色的可以吗？", "Sorry, we have no large in blue. Is black all right?"), ("顾客", "黑色的也可以。", "Black is fine too."), ("售货员", "好，您稍等。这件您试试。", "Okay, one moment. Try this one."),
        ("顾客", "好。", "Okay."), ("售货员", "怎么样？合适吗？", "How is it? Does it fit?"), ("顾客", "挺合适的。我就买这件。多少钱？", "It fits very well. I’ll buy this one. How much is it?"), ("售货员", "一百二十块。", "One hundred and twenty yuan.")]
L2 = lesson(
    "Lesson 9 Presentation 1 activities: shopping words and a clothing dialog",
    "收银台 · 降价 · 样式 · 衬衫 · 西装 · 给我拿件大号的",
    requires=[],
    cards=[
        card("Activity 1A: sort the words",
             "Use the words 收银台, 客人, 降价, 原价, 合适, 服务员, 颜色, 样式, 付费, 打折, 蓝色, 粉色 and 试衣间 to fill in categories related to shopping (the book’s chart has: Color, Clothes Selection Criteria, Places in Store, Prices and Payments). One way to sort them (the key is mine):",
             tables=[table(["Category", "Words"], CLASS, title="买东西")]),
        card("Activity 1B: complete the sentences",
             "Complete the sentences using the word bank 收银台, 降价, 原价, 合适, 颜色, 样式, 扫码, 衣服, 试 (there are more words than you need), check with a partner, then translate the sentences orally. The seven sentences with my key:",
             tables=[table(["Sentence", "Answer"], CLOZE9, title="Fill in the blanks")]),
        card("Activity 4 (Listening and Speaking): two shoppers",
             "New words: 衬衫 chènshān, shirt (the book prints 衬杉) and 西装 xīzhuāng, suit. A. Listen to two dialogs twice and complete a table with each shopper’s purchase: item purchased, color, size, price (audio, not included). B. Pair up: Student A relays Dialog 1 and Student B Dialog 2 in Chinese.",
             tables=[wtable([("衬衫", "chen4 shan1", "shirt"), ("西装", "xi1 zhuang1", "suit")], title="New words")]),
        card("Activity 5 (Reading, Writing and Speaking): fill in the clerk’s lines",
             "A. The book gives only the customer’s lines (我想买件衬衫。 蓝颜色的。 好像小了点儿。给我拿件儿大号的试试吧。 黑色的也可以。 好。 挺合适的。我就买这件。多少钱?) and asks you to fill in the clerk’s questions and replies. B. Role-play your dialog with a partner. One possible complete dialog (the clerk’s lines are mine):",
             examples=dlg(DLG5)),
    ],
    exercises=[
        M("Which word names the place where you pay?", "收银台", ["试衣间", "服务员", "样式"], "买完东西得去收银台付钱。"),
        M("Which word means “to reduce prices”?", "降价", ["打折", "付费", "试试"], "这个周末这个商店的衣服都降价。"),
        M("Which verb fits: 买衣服的时候，我一定要___穿才知道合适不合适?", "试", ["付", "扫", "降"], "试穿: try on."),
        M("Which word means “style”?", "样式", ["颜色", "原价", "号"], "样式 and 颜色 are selection criteria."),
        M("What do many shops now allow you to do with your phone?", "Scan a code to pay (扫码)", ["Try on clothes", "Choose a color", "Change a size"], "现在去很多商店买东西可以用手机扫码。"),
        M("In the clerk dialog, what does the customer want to buy?", "A shirt (衬衫)", ["A suit", "A coat", "A pair of shoes"], "我想买件衬衫。"),
        M("Why does the customer ask for a larger size?", "The first shirt seems a little small", ["It is too big", "It is the wrong color", "It is too expensive"], "好像小了点儿。"),
        M("What color does the customer finally accept?", "Black", ["Blue", "Pink", "Red"], "黑色的也可以。"),
        M("What does 衬衫 mean?", "shirt", ["suit", "shoes", "coat"], "衬衫 chènshān."),
        F("给我拿件儿大___的试试吧。", "号", PART, "大号: a large size."),
        F("买完东西得去___付钱。", "收银台", ["作业", "操场", "预习"], "收银台 is where you pay."),
        mean("西装", "xi1 zhuang1", "suit", ["shirt", "shoes", "coat"]),
        mean("付费", "fu4 fei4", "pay fees", ["scan a code", "try on", "reduce prices"]),
    ],
)

# ------------------------------------------------------------------ 3. money
MONEY = [("两块", "¥2.00"), ("三块五毛", "¥3.50"), ("六块八毛", "¥6.80"), ("九块二", "¥9.20 (二, or 两毛)"), ("七十九块四毛二", "¥79.42"), ("一块二毛四", "¥1.24"), ("八毛", "¥0.80"), ("七毛八", "¥0.78"), ("九百零五块", "¥905"), ("十九块零八分", "¥19.08"), ("十块零三分", "¥10.03")]
BUD = [("一件军服一百六十九块九毛九", "A uniform for ¥169.99"), ("饭馆的饭钱五十六块零四分", "¥56.04 for restaurant meals"), ("女朋友的衣服八百六十八块二", "¥868.2 for my girlfriend’s clothes"), ("啤酒钱二十五块", "¥25 for beer"),
       ("手机费九十六块零七分", "¥96.07 phone bill"), ("电脑七百二十九块八毛三", "¥729.83 computer"), ("日用品四十五块三", "¥45.3 daily necessities at the military store"), ("电影六十五块三", "¥65.3 movie")]
L3 = lesson(
    "Lesson 9 Presentation 1 grammar: the basic Chinese money units",
    "块（元）· 毛（角）· 分 · 九百零五 · 十九块零八",
    requires=[],
    cards=[
        card("Basic Chinese monetary units",
             "The basic units are 块/元, 毛/角 and 分. Grammatically, 块/元, 毛/角 and 分 are measure words as well as nouns. 元 and 角 are formal versions usually found only in written Chinese. When one or more units or digits are skipped, 零 must be inserted to fill the gap, as in the last three examples. 钱 (money) may be added at the end: 两块钱. In spoken Chinese the last unit is often dropped (九块二 for 9.20; 七十九块四毛二).",
             tables=[wtable(rows_py([(a, b) for a, b in MONEY]), title="Amounts and their values")]),
        card("Activities 1 and 2",
             "Activity 1: match the coins with the bills of equal value (four pictures, not included). Activity 2: roommates 小王 and 小李 discuss their monthly budgets. A. Student A plays 小王 and gives details of what he spent, for example 一件军服 169.99 块钱/元, while Student B (小李) writes the items and prices in a table; B. switch roles and repeat with the second set. The two sets of items, read out in Chinese:",
             examples=[D(z, e) for z, e in BUD]),
    ],
    exercises=[
        M("What are the three basic Chinese money units in speech?", "块, 毛, 分", ["元, 角, 块", "斤, 两, 毛", "块, 件, 个"], "块/元, 毛/角 and 分."),
        M("Which units are the formal, written forms?", "元 and 角", ["块 and 毛", "分 and 块", "元 and 毛"], "元 and 角 are formal versions."),
        M("How do you say ¥3.50?", "三块五毛", ["三毛五块", "三块五分", "五块三毛"], "三块 + 五毛."),
        M("How do you say ¥0.80?", "八毛", ["八分", "八块", "零八块"], "0.80 is 八毛."),
        M("How do you say ¥905?", "九百零五块", ["九百五块", "九零五块", "九十五块"], "零 fills the missing tens place."),
        M("How do you say ¥19.08?", "十九块零八分", ["十九块八分", "十九块八毛", "一百九块八"], "零 fills the missing 毛 place."),
        M("How do you say ¥10.03?", "十块零三分", ["十块三分", "十块三毛", "一百零三块"], "零 fills the missing 毛 place."),
        M("What is 七十九块四毛二?", "¥79.42", ["¥7.942", "¥79.24", "¥794.2"], "79 yuan, 4 mao, 2 fen."),
        M("Why is 零 inserted in 十九块零八分?", "A unit (毛) is skipped", ["Because 八 is bad luck", "To make it formal", "To show a question"], "When one or more units or digits are skipped, 零 must fill the gap."),
        M("What are 块 and 毛 grammatically?", "Measure words as well as nouns", ["Verbs", "Adjectives", "Particles"], "Grammatically, 块, 毛 and 分 are measure words as well as nouns."),
        F("九百___五块", "零", ["再", "给", "放"], "零 fills the gap in 905."),
        F("八___ (¥0.80)", "毛", PART, "毛 is the second unit."),
        mean("块", "kuai4", "yuan (spoken unit of money)", ["pair", "plate", "piece of clothing"]),
    ],
)

# ------------------------------------------------------------------ 4. 有(一)点儿 + adjective
YOU = [("上个周末有一点儿忙。", "Last weekend was a bit busy."), ("这件衣服有一点儿贵。", "This piece of clothing is a bit expensive."), ("今天有一点儿热。", "Today is a bit hot."), ("纽约的冬天有一点儿冷。", "Winter in New York is a bit cold."),
       ("这道菜有一点儿辣。", "This dish is a bit spicy."), ("今天我有一点儿不高兴。", "Today I am a bit unhappy.")]
YOU_AB = [("甲", "国防语言学院的学习怎么样？", "How is the study at DLI?"), ("乙", "有一点忙，有一点快。", "A bit busy, a bit fast.")]
Q7 = [("你最近忙不忙？", "Are you busy lately?"), ("今天热不热？", "Is it hot today?"), ("跟昨天比，今天热不热？", "Compared with yesterday, is it hot today?"), ("你的手机贵不贵？", "Is your cell phone expensive?"), ("今天你喝咖啡了吗？", "Did you drink coffee today?"),
      ("甲班和乙班，哪个教室大？哪个教室好？", "Between Class A and Class B, which classroom is bigger? Which is better?"), ("我们班大卫和琳达，谁的年纪大？", "In our class, who is older, David or Linda?")]
L4 = lesson(
    "Lesson 9 Presentation 1 grammar: 有(一)点儿 + adjective",
    "有一点儿贵 · 有点儿热 · 今天我有一点儿不高兴",
    requires=[],
    cards=[
        card("The 有(一)点儿 + Adjective pattern",
             "The pattern “有一点儿 + adjective” describes something dissatisfying, uncomfortable or contrary to one’s wishes. In essence it means “a bit too much” of a certain quality. Hence you will not hear *有点高兴, *有点舒服 or *有点好玩儿, because “happy”, “comfortable” and “fun” are adjectives with positive connotations. It is correct, however, to say 今天我有一点儿不高兴/不舒服. Patterns: Subject + 有一点(儿) + Adjective; Subject + 有点(儿) + Adjective (spoken Chinese). Also: the shortened answer must keep 有 (*一点忙，一点快 is wrong).",
             examples=[D(z, e) for z, e in YOU] + [D(f"{s}：{z}", e) for s, z, e in YOU_AB]),
        card("Activity 3 (Reading and Speaking)",
             "Ask a partner the following questions while they answer with 有一点儿 or 一点儿.",
             examples=[D(z, e) for z, e in Q7]),
    ],
    exercises=[
        M("What does 有一点儿 + adjective express?", "Dissatisfaction: “a bit too …”", ["A pleasant quality", "A question", "A past action"], "有一点儿贵: a bit too expensive."),
        M("What does 这件衣服有一点儿贵 mean?", "This piece of clothing is a bit too expensive", ["This piece of clothing is cheap", "This piece of clothing is very good", "I have one expensive piece of clothing"], "有一点儿 + undesirable quality."),
        M("Which sentence is correct?", "今天我有一点儿不高兴。", ["今天我有一点儿高兴。", "今天我一点儿高兴。", "今天有一点儿我高兴。"], "Positive adjectives like 高兴 do not take 有一点儿; 不高兴 does."),
        M("Why can’t you say 有点好玩儿?", "好玩儿 is a positive adjective", ["好玩儿 is a noun", "有点 is only for nouns", "好玩儿 is too long"], "“Happy”, “comfortable” and “fun” have positive connotations."),
        M("Which is the correct answer to 国防语言学院的学习怎么样？", "有一点忙，有一点快。", ["一点忙，一点快。", "有忙，有快。", "忙一点，快一点。"], "有 must stay: *一点忙 is wrong."),
        M("Which means “Winter in New York is a bit cold”?", "纽约的冬天有一点儿冷。", ["纽约的冬天冷一点儿。", "纽约的冬天一点儿冷。", "纽约有冬天冷一点儿。"], "有一点儿 comes before the adjective."),
        M("Where does 有一点儿 go?", "Before the adjective", ["After the adjective", "At the end of the sentence", "Before the subject"], "Subject + 有一点儿 + Adjective."),
        M("Which colloquial form is correct?", "Subject + 有点(儿) + Adjective", ["Subject + 一点 + 有 + Adjective", "Subject + Adjective + 有点", "有点 + Subject + Adjective"], "有点 in spoken Chinese."),
        F("这道菜有一点儿___。", "辣", PART, "辣 (spicy) is an adjective that can follow 有一点儿."),
        F("上个周末___一点儿忙。", "有", ["再", "才", "给"], "有一点儿 + adjective."),
        F("今天我有一点儿不___。", "高兴", ["吗", "们", "呢"], "不高兴 is acceptable after 有一点儿."),
        mean("有点儿", "you3 dian3r5", "a little bit (too much)", ["a little (as a request)", "size", "style"]),
    ],
)

# ------------------------------------------------------------------ 5. adjective + 了 + (一)点儿
ADJLE = [("这条裤子小了一点儿，有大一号的吗？", "These trousers are a little too small; do you have a size bigger?"), ("这道菜咸了点，能换一盘清淡一点的吗？", "This dish is a little too salty; can I change it for a milder one?"),
         ("现在做作业晚了一点吧？五分钟后你就得交了。", "Isn’t it a bit late to do homework now? In five minutes you have to hand it in."), ("蒙特雷的夏天冷了一点，所以不能去游泳。", "Summer in Monterey is a bit too cold, so you can’t go swimming."),
         ("这个学校贵了一点，但是老师都很不错。", "This school is a little expensive, but the teachers are all very good.")]
L5 = lesson(
    "Lesson 9 Presentation 1 grammar: adjective + 了 + (一)点儿",
    "小了一点儿 · 咸了点 · 贵了一点 · 不能说“紧张了一点”",
    requires=[],
    cards=[
        card("The Adjective + 了 + (一)点儿 pattern",
             "“Adjective 了 + 一点儿” is similar to “有一点(儿) + adjective” in expressing “a little bit too much”. However, only “有一点(儿) + adjective” can take adjectives or emotive verbs such as 紧张, 不高兴 and 难过 (nánguò, sad). You can say 有一点紧张, 有点不高兴 or 有一点难过, but it is incorrect to say *紧张了一点, *不高兴了一点 or *难过了一点. Pattern: Adjective + 了(一)点儿.",
             examples=[D(z, e) for z, e in ADJLE], ),
    ],
    exercises=[
        M("What does 这条裤子小了一点儿 mean?", "These trousers are a little too small", ["These trousers are very small", "These trousers are just right", "I have small trousers"], "Adjective 了 + 一点儿: a little too …"),
        M("Which sentence is correct?", "这道菜咸了点。", ["这道菜有咸点。", "这道菜了咸点。", "这道菜点咸了。"], "咸了点: a little too salty."),
        M("Which is NOT correct?", "紧张了一点", ["有一点紧张", "有点不高兴", "有一点难过"], "Only 有一点 can take emotive adjectives like 紧张."),
        M("What does 蒙特雷的夏天冷了一点 mean?", "Summer in Monterey is a bit too cold", ["Summer in Monterey is very hot", "Summer in Monterey is cold", "Monterey has no summer"], "冷了一点: a bit too cold."),
        M("What does 这个学校贵了一点，但是老师都很不错 mean?", "The school is a little expensive, but the teachers are very good", ["The school is cheap and the teachers are bad", "The school is very good", "The teachers are expensive"], "贵了一点 + 但是…"),
        M("What does 现在做作业晚了一点吧？ suggest?", "It may be a bit late to do homework now", ["It is the right time", "It is too early", "Nobody does homework"], "晚了一点: a bit too late."),
        M("Where does 了 go in this pattern?", "Right after the adjective", ["Before the adjective", "At the end of the sentence", "After 一点"], "Adjective + 了 + (一)点儿."),
        F("这件衣服大___一点儿，有没有小一号的？", "了", PART, "Adjective + 了 + 一点儿."),
        F("这道菜咸了___，能换一盘清淡一点的吗？", "点", ["再", "才", "给"], "咸了点: a little too salty."),
        mean("清淡", "qing1 dan4", "mild (of flavor)", ["salty", "spicy", "sweet"]),
    ],
)

# ------------------------------------------------------------------ 6. adjective + (一)点儿
ADJYD = [("请你快一点儿！", "Please hurry up a little!"), ("老板，能不能便宜一点儿？", "Boss, can you make it a little cheaper?"), ("这件黑皮鞋比那双白皮鞋质量好一点。", "These black leather shoes are a little better in quality than those white ones."),
         ("蒙特雷的冬天比纽约暖和一点儿。", "Winter in Monterey is a little warmer than in New York."), ("明天人一定很多，请你早一点来。", "There will be a lot of people tomorrow; please come a little earlier."), ("这件衣服有大一点吗？", "Do you have this piece in a slightly bigger size?"), ("这件衣服大了一号，有没有小一号的？", "This piece is one size too big; do you have one size smaller?")]
PAT6 = [("有点儿贵", "贵了点儿", "便宜点（吧）"), ("有点儿不高兴", "没有这种说法", "高兴点儿（吧）")]
ITEMS_A = [("这件衬衫", "贵", "便宜"), ("这套西装", "大", "小"), ("这个教室", "小", "大"), ("这杯茶", "酸", "甜"), ("这个桔子", "凉", "热")]
ITEMS_B = [("这道麻婆豆腐", "贵", "便宜"), ("今晚的作业", "多", "少"), ("这家饭店", "淡", "辣"), ("这杯咖啡", "酸", "甜"), ("这个苹果", "冷", "热")]
L6 = lesson(
    "Lesson 9 Presentation 1 grammar: adjective + (一)点儿 for requests",
    "便宜一点儿 · 快一点儿 · 小一号 · 有点儿贵 / 贵了点儿 / 便宜点",
    requires=[],
    cards=[
        card("The Adjective + (一)点儿 pattern",
             "“Adjective + (一)点儿” is very different from “有(一)点儿 + adjective” in both form and meaning. In form, 有一点儿 precedes the adjective, while (一)点儿 follows it. In meaning, “有一点 + adjective” has an undesirable or negative connotation, while “adjective + 一点” connotes desirability. The latter is most often used in making requests. Pattern: Adjective + 一点(儿).",
             examples=[D(z, e) for z, e in ADJYD[:5]]),
        card("When you know the exact size: 一号",
             "When you know the exact size or amount you need, instead of 一点儿 use “Adjective + 了 + exact amount” to express dissatisfaction and “Adjective + exact amount” to express your preference.",
             examples=[D(z, e) for z, e in ADJYD[5:]]),
        card("Three patterns compared",
             "To describe something undesirable use 有(一)点(儿) + adjective or adjective + 了(一)点(儿); to make a request use adjective + (一)点(儿). The adjective 贵 (expensive) goes with all three; an emotive word like 不高兴 cannot take 了点, so it has an X in the middle:",
             tables=[table(["有(一)点(儿) + Adj", "Adj 了(一)点(儿)", "Adj (一)点(儿) request"], PAT6, say=[0, 1, 2], title="Describing and requesting")]),
        card("Activity 4 (Reading and Speaking): dissatisfaction, then a request",
             "A. Student A uses “有一点儿 + adjective” to express dissatisfaction with each item below (the book has 这条衬衫; 这件衬衫 is the usual measure word); Student B repeats it and uses “adjective + 一点儿” to request their preference. Example: 这件衣服有一点儿贵。 → 这件衣服有一点贵，有没有便宜一点儿的？ B. Student B uses “adjective 了 + 一点儿”, e.g. 这件衣服贵了一点儿。 → 这件衣服贵了一点儿，有没有便宜一点儿的？ Sentences made from the two lists (mine):",
             examples=[D(f"{a}有一点儿{b}，有没有{c}一点儿的？", f"{a} is a bit too {b}; do you have one that is a little {c}?") for a, b, c in ITEMS_A[:3]] +
                      [D(f"{a}{b}了一点儿，有没有{c}一点儿的？", f"{a} is a little too {b}; do you have one that is a little {c}?") for a, b, c in ITEMS_B[:3]]),
    ],
    exercises=[
        M("What is the difference in form between 有一点儿 + adjective and adjective + 一点儿?", "有一点儿 comes before the adjective; 一点儿 comes after it", ["They are the same", "有一点儿 comes at the end", "一点儿 comes before the subject"], "有一点儿贵 against 便宜一点儿."),
        M("What does adjective + 一点儿 usually express?", "A request or a wish", ["Dissatisfaction", "A past event", "A question about price"], "便宜一点儿: a bit cheaper, please."),
        M("How do you ask the boss for a lower price?", "老板，能不能便宜一点儿？", ["老板，能不能有一点儿便宜？", "老板，能不能一点儿便宜？", "老板，便宜有点儿吗？"], "Adjective + 一点儿 for a request."),
        M("What does 请你快一点儿 mean?", "Please hurry up a little", ["You are too fast", "I am a bit slow", "Please wait"], "快一点儿: a bit faster."),
        M("Which sentence compares two things gently?", "蒙特雷的冬天比纽约暖和一点儿。", ["蒙特雷的冬天有一点儿暖和。", "蒙特雷的冬天暖和了一点儿。", "蒙特雷的冬天一点儿暖和。"], "比 + noun + adjective + 一点儿."),
        M("What is the pattern for a known size?", "这件衣服大了一号，有没有小一号的？", ["这件衣服有一点儿大号。", "这件衣服大一点儿号。", "这件衣服了大一号。"], "Adjective 了 + exact amount, then adjective + exact amount."),
        M("Which request goes with “happy” (高兴)?", "高兴点儿（吧）", ["有点儿高兴", "高兴了点儿", "点儿高兴"], "Only the request form works with 高兴."),
        M("Which one is wrong?", "高兴了点儿", ["有点儿不高兴", "高兴点儿（吧）", "便宜点（吧）"], "Emotive words cannot take 了点儿."),
        M("Student A says 这件衣服有一点儿贵. What would student B say?", "这件衣服有一点贵，有没有便宜一点儿的？", ["这件衣服有一点贵，有没有一点儿便宜的？", "这件衣服贵，便宜有没有的？", "这件衣服有没有贵一点儿的？"], "Repeat, then ask for a cheaper one."),
        F("明天人一定很多，请你早一点___。", "来", ["再", "才", "给"], "早一点来: come a little earlier."),
        F("这件衣服有大一___吗？", "点", PART, "大一点: a slightly bigger one."),
        F("这件衣服大了一号，有没有小一___的？", "号", PART, "小一号: one size smaller."),
        mean("便宜", "pian2 yi5", "cheap", ["expensive", "mild", "salty"]),
    ],
)

# ------------------------------------------------------------------ 7. activities 5-7
TFS = [("客人买了黑西装，因为比蓝的便宜。", "The customer bought the black suit because it was cheaper than the blue one."), ("客人最后买了中号的黑西装。", "In the end the customer bought a medium black suit."), ("客人穿大号的西装，有点儿大。", "The customer tried the large suit and it was a little big."), ("客人一共花了七百七十块钱。", "The customer spent 770 yuan in all.")]
LETTER = [("王英：", "Wang Ying:", None), ("你好！你在上海已经住了半年多了，习惯了吧？我想请你帮我在上海买两双三十六号的皮鞋，价钱贵一点儿不要紧，可是质量一定要好。", "Hello! You’ve been living in Shanghai for more than half a year already; have you gotten used to it? I’d like to ask you to buy two pairs of size 36 leather shoes for me in Shanghai; it doesn’t matter if the price is a bit higher, but the quality must be good."),
          ("上个月我在上海蓝天鞋店看到一双黑皮鞋，我很喜欢，可是觉得有一点儿贵，所以没买。我回北京以后，去了很多鞋店都没有看到我喜欢的鞋。", "Last month at the Lantian shoe store in Shanghai I saw a pair of black leather shoes that I liked very much, but I thought they were a bit expensive, so I didn’t buy them. After I came back to Beijing, I went to many shoe stores and did not see any shoes I liked."),
          ("北京的皮鞋比上海的皮鞋便宜一点儿，可是上海皮鞋的质量比北京皮鞋的质量好一点儿。麻烦你了，谢谢！好，不多写了。祝安好！", "Beijing leather shoes are a little cheaper than Shanghai leather shoes, but the quality of Shanghai shoes is a little better than that of Beijing shoes. Sorry to trouble you, thank you! Okay, I won’t write more. Wishing you well!"),
          ("李丽", "Li Li", None), ("六月十八日", "June 18", None)]
L7 = lesson(
    "Lesson 9 Presentation 1 activities: a suit, class feedback and Lili’s letter",
    "客人买了黑西装 · 作业有点儿多，可以少一点吗？ · 王英：你好！",
    requires=[],
    cards=[
        card("Activity 5 (Listening and Speaking): a customer and a clerk",
             "A. Listen to a dialog between a customer and a clerk, take notes and summarize (audio, not included). B. Listen again and decide whether each statement is true or false; say the correct answers for the false statements aloud. (The key needs the recording.) The four statements:",
             examples=[D(z, e) for z, e in TFS]),
        card("Activity 6 (Writing and Speaking): feedback to your team leader",
             "You have been at DLI for over a month. To improve learning and teaching, your team leader asks for your opinions of your classes, homework, pace of work, learning environment, etc. A. Write a short list of your dissatisfactions using 有一点 + adjective or adjective 了 + 一点儿 to soften your tone, and follow each with a constructive suggestion using adjective + 一点儿. Example: 我觉得每天晚上的作业有点儿多，作业可以少一点吗？ B. Share your list with the class in Chinese. C. As a class, select the top three suggestions for the team leader.",
             examples=[D("我觉得每天晚上的作业有点儿多，作业可以少一点吗？", "I think the homework every night is a bit much; could there be a little less homework?")]),
        card("Activity 7 (Reading and Speaking): Lili’s letter to a Chinese friend",
             "A. Read the letter and fill the blanks with 贵了一点, 贵一点儿, 有一点儿不好, 便宜一点儿, 好一点儿 and 有一点儿贵 (the book leaves four blanks; the letter below is completed with my key). B. Read the underlined sentences to a partner and translate them together.",
             examples=[D(*x[:2]) for x in LETTER]),
    ],
    exercises=[
        M("In the letter, what does Li Li ask Wang Ying to do?", "Buy two pairs of size 36 leather shoes in Shanghai", ["Send her to Beijing", "Sell her shoes", "Visit her"], "请你帮我在上海买两双三十六号的皮鞋。"),
        M("What matters most to Li Li about the shoes?", "The quality; a higher price is acceptable", ["The price must be very low", "The color only", "The brand only"], "价钱贵一点儿不要紧，可是质量一定要好。"),
        M("Why didn’t Li Li buy the black shoes in Shanghai?", "She thought they were a bit expensive", ["They were too small", "The shop was closed", "She didn’t like black"], "觉得有一点儿贵，所以没买。"),
        M("How do Beijing shoes compare with Shanghai shoes?", "Beijing shoes are a little cheaper; Shanghai shoes are a little better in quality", ["Beijing shoes are better and cheaper", "Shanghai shoes are cheaper", "They are the same"], "北京的…便宜一点儿；上海…质量好一点儿."),
        M("How long has Wang Ying lived in Shanghai?", "More than half a year", ["Two weeks", "Ten years", "Just arrived"], "你在上海已经住了半年多了。"),
        M("In Activity 6, how does the example soften a complaint?", "我觉得…有点儿多 (a bit much), then a request: 可以少一点吗？", ["It shouts at the leader", "It says nothing", "It asks a question about price"], "有点儿 + adjective, then adjective + 一点."),
        M("When is the date of the letter?", "June 18", ["January 1", "December 25", "March 3"], "六月十八日."),
        F("价钱___一点儿不要紧，可是质量一定要好。", "贵", ["再", "才", "们"], "价钱贵一点儿不要紧: a slightly higher price doesn’t matter."),
        F("北京的皮鞋比上海的皮鞋便宜一点儿，可是质量好___点儿。", "一", ["再", "才", "们"], "好一点儿: a little better."),
        mean("质量", "zhi4 liang4", "quality", ["price", "size", "color"]),
    ],
)

# ------------------------------------------------------------------ 8. skill integration
RED = ("这位客人想买一件红颜色的衬衫。服务员给他中号的，可是那件衬衫有点大，他请服务员给他小一号的。不过那件衬衫没有他要的颜色，只有蓝色的。他还是试了一下。他觉得挺合适的就买了那件。因为他没有这么多现金，最后他用手机扫码付费，一共付了七十六块五。",
       "This customer wanted to buy a red shirt. The clerk gave him a medium, but that shirt was a little big, so he asked the clerk for one a size smaller. But that shirt did not come in the color he wanted, only in blue. He tried it on anyway. He felt it fit very well, so he bought it. Because he did not have that much cash, in the end he paid by scanning a code with his cell phone, 76.5 yuan in all.")
NEWV = [("价钱", "jia4 qian2", "price"), ("刷卡", "shua1 ka3", "to swipe a card"), ("收银员", "shou1 yin2 yuan2", "cashier")]
SIZES = [("美国", "6 · 7 · 8 · 9 · 10 · 11 · 12"), ("中国", "38 · 39.5 · 41 · 42 · 43 · 44.5 · 46")]
SHOEQ = [("您穿多大号的？", "b", "在美国我穿十号的鞋。", "What size do you wear? — In America I wear a size 10 shoe."), ("请问，美国十号的鞋在中国是多大号？", "c", "美国十号的鞋在中国是四十三号。", "Excuse me, what is a US size 10 in China? — A US size 10 is a size 43 in China."),
         ("除了这种黑色的以外，还有别的颜色没有？", "d", "还有咖啡色的和蓝色的。", "Besides this black, are there other colors? — There are also coffee-colored and blue ones."), ("这双四十四号半的怎么样？", "a", "这双正合适，就买这双吧！", "How about this pair in size 44.5? — This pair fits just right; let’s buy this pair!")]
L8 = lesson(
    "Lesson 9 Presentation 1 skill integration: a red shirt, shoe sizes, a coat",
    "红颜色的衬衫 · 手机扫码付费 · 美国十号的鞋在中国是多大号？",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): the passage",
             "A. Read the passage and answer in Chinese: 1. What did the customer want to buy? 2. What did he end up buying, and why? 3. What is his method of payment and how much does he pay? B. Check your answers with a partner in Chinese. C. In pairs, write your own clerk and customer dialog based on the passage and act it out; switch roles and repeat.",
             examples=[D(*RED)]),
        card("Activity 2 (Listening, Writing, Speaking and Reading)",
             "A. Listen to a dialog and jot down the EEIs (Elements of Essential Information) (audio, not included). B. Write four questions to ask a partner about the dialog, then take turns asking them. C. Read the script your teacher provides aloud and check your partner’s answers. D. Guess the meaning of these new words (answers: price, swipe a card, cashier):",
             tables=[wtable(NEWV, title="New vocabulary")]),
        card("Activity 3 (Listening, Speaking and Reading): a shoe size chart",
             "New word: 咖啡色 kāfēisè, coffee-colored; beige. A. Listen to a dialog and consult the size chart (men’s shoe sizes) to select the most appropriate size for the customer. B. Listen again and answer in Chinese: What does the customer want to buy? What colors does it come in? Which color does he choose? What size does he first tell the clerk he wears? What is his actual size? C. In pairs, take turns asking questions about the dialog. D. Match the questions and answers (the four pairs below, matching a to d as the book prints them; the key is mine).",
             tables=[table(["", "Men’s shoe sizes"], SIZES, title="男式鞋号 (US and China)")],
             examples=[D(q, qe.split(" — ")[0]) for q, k, a, qe in SHOEQ] + [D(a, qe.split(" — ")[1]) for q, k, a, qe in SHOEQ]),
        card("Activity 4 (Listening, Writing and Speaking): Xiao Li’s coat",
             "New word: 大衣 dàyī, coat. A. Listen to a dialog twice and, below three pictures, write the key Chinese words you think are most essential to understanding the dialog (audio, not included). B. Using your key words, retell Xiao Li’s shopping experience to a partner. C. Check your key words with your partner to see if you got them all."),
    ],
    exercises=[
        M("What did the customer want to buy?", "A red shirt", ["A blue shirt", "A pink shirt", "A black coat"], "这位客人想买一件红颜色的衬衫。"),
        M("What size did the clerk first give him?", "Medium", ["Small", "Large", "Extra large"], "服务员给他中号的。"),
        M("Why did he ask for a different size?", "The medium was a little big", ["It was too small", "It was torn", "It was too expensive"], "那件衬衫有点大，他请服务员给他小一号的。"),
        M("What did he end up buying?", "A blue shirt in the smaller size, because it fit well", ["A red shirt", "A pink shirt", "Nothing"], "只有蓝色的…他觉得挺合适的就买了那件。"),
        M("How did he pay, and why?", "By phone code, because he didn’t have enough cash", ["With cash", "With a card, because it was cheaper", "He did not pay"], "因为他没有这么多现金，最后他用手机扫码付费。"),
        M("How much did he pay?", "76.5 yuan", ["765 yuan", "76 fen", "7.65 yuan"], "一共付了七十六块五。"),
        M("In China, what size is a US size 10 shoe, according to the chart?", "43", ["42", "44.5", "41"], "美国十号的鞋在中国是四十三号。"),
        M("What is a US size 7 in China, according to the chart?", "39.5", ["38", "41", "42"], "The chart: 7 → 39.5."),
        M("What does 咖啡色 mean?", "coffee-colored; beige", ["blue", "pink", "black"], "咖啡色 kāfēisè."),
        M("What does 收银员 mean?", "cashier", ["customer", "shop owner", "waiter"], "收银 = collect money; 员 = person."),
        M("What does 大衣 mean?", "coat", ["shirt", "suit", "shoes"], "大衣 dàyī."),
        F("您穿多大___的？", "号", PART, "大号: size."),
        F("这双正___，就买这双吧！", "合适", ["作业", "操场", "预习"], "正合适: fits just right."),
        mean("价钱", "jia4 qian2", "price", ["quality", "size", "color"]),
    ],
)

# ------------------------------------------------------------------ 9. using Chinese in context
ADS = [("红色广告 (red ad)", "换季大拍卖 · 秋装上市 · 夏装七折", "Season-change sale · autumn clothes now in · summer clothes 30% off"), ("蓝色广告 (blue ad)", "全场 · 买一双 · 第二双半价 · 买一千送二百", "Everything · buy one pair, the second pair half price · spend 1,000, get 200 back"),
       ("黄色广告 (yellow ad)", "大降价 · 一件九折 · 两件八点五折 · 三件八折 · 来就送小礼物", "Big price cuts · one piece 10% off · two pieces 15% off · three pieces 20% off · a small gift just for coming")]
CATS = [("尺码 (size)", "这件衬衫你们有没有大号的？"), ("颜色 (color)", "这件衬衫有什么颜色？"), ("我喜欢的样式 (style)", "你们有什么样式的？"), ("我看起来怎么样？ (how do I look?)", "这件有一点儿太小？"), ("价钱对不对？ (is it the right price?)", "这件多少钱？"), ("现金还是刷卡？ (cash or charge?)", "一共多少钱？")]
COLORS = [("红色", "hong2 se4", "red"), ("绿色", "lv4 se4", "green"), ("棕色", "zong1 se4", "brown"), ("橙色", "cheng2 se4", "orange (or 橘子色)"), ("灰色", "hui1 se4", "gray"), ("咖啡色", "ka1 fei1 se4", "coffee color"),
          ("黄色", "huang2 se4", "yellow"), ("紫色", "zi3 se4", "purple"), ("白色", "bai2 se4", "white"), ("黑色", "hei1 se4", "black"), ("蓝色", "lan2 se4", "blue"), ("粉色", "fen3 se4", "pink"), ("浅蓝色", "qian3 lan2 se4", "light blue (浅 = light)"), ("深蓝色", "shen1 lan2 se4", "dark blue (深 = dark)")]
MOM = [("小明：", "Xiaoming:"), ("你的生日快到了。我不知道你想要什么礼物。我知道你们每天都要锻炼身体，所以给你买了一件锻炼的时候可以穿的衣服。", "Your birthday is coming soon. I don’t know what gift you want. I know you all have to exercise every day, so I bought you a piece of clothing you can wear when you exercise."),
       ("你以前穿中号的，可是妈妈有一年没见到你了，不知道你的衣服大小是不是还和以前一样。要是大小不合适，你可以拿收据去店里换。", "You used to wear a medium, but Mom hasn’t seen you for a year and doesn’t know if your clothing size is still the same as before. If the size isn’t right, you can take the receipt to the store and exchange it."),
       ("你可以去那里试穿，换你喜欢的。妈妈很想你。常给妈妈打电话。", "You can go there to try it on and exchange it for what you like. Mom misses you very much. Call Mom often."), ("祝好！", "Best wishes!"), ("妈妈", "Mom")]
L9 = lesson(
    "Lesson 9 Presentation 1: using Chinese in context (ads, colors, a mother’s letter)",
    "全场大降价 · 一件九折 · 红色 绿色 棕色 · 你可以拿收据去店里换",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Writing): three advertisements",
             "In groups of three, each student reads one of three advertisements to extract the EEIs (Elements of Essential Information). A. Write two questions about your ad and post them online. B. Read the other two groups’ questions and answer them from the ads. C. Return to your group and review each other’s answers. The three ads (red, blue and yellow):",
             tables=[table(["Ad", "Text", "Meaning"], ADS, title="Advertisements")]),
        card("Activity 2 (Writing, Reading and Speaking): shopping in Beijing",
             "You have finally arrived at your Beijing hotel after a 12-hour flight; your luggage is on a different flight, so you must buy some clothes. A. In groups of three, each student chooses two categories and brainstorms questions or statements a clerk or customer might say. The book’s six categories, each with its example question:",
             tables=[table(["Category", "Example question"], CATS, say=[], title="Six categories")],
             examples=[D(z, z.split(" (")[0]) for z in []]),
        card("Activity 2B and 2C: sizes and colors",
             "B. Refer to the chart of clothing sizes (not included) and highlight the sizes you wear or intend to buy. C. Review some basic colors in Chinese; 浅 qiǎn (light) and 深 shēn (dark) go before a color, as in 浅蓝色 and 深蓝色.",
             tables=[wtable(COLORS, title="Basic colors")]),
        card("Activity 2D: role-play cards",
             "You are at the local department store. Find a partner and act out the customer and the salesperson; switch roles and repeat. Customer: greet the clerk; tell the clerk what items you are looking for; ask about the available colors; ask about the available sizes; ask if you can try the items on; ask the clerk’s opinion on how the items suit or fit you; express some dissatisfaction and request adjustments; ask the prices and if you can get any discounts; decide on your purchases and ask about methods of payment. Salesperson: greet the customer and ask what they are looking for; ask what colors they prefer, tell them they are not available and offer alternatives; ask what sizes they wear, explain that Chinese sizes usually run smaller than Western ones and suggest other sizes; offer other styles that are more expensive but better quality; suggest items to try on; quote the prices and offer discounts, especially for multiple items; offer various payment options."),
        card("Activity 3 (Reading, Speaking and Writing): Xiao Ming’s mother’s letter",
             "Xiao Ming’s mom has sent him a letter along with a birthday gift. A. Read the letter and answer in Chinese: 1. What present did Xiao Ming get? 2. What is his mom’s concern? 3. What does his mom tell him he can do? B. Pair up: Xiao Ming discovers the present does not suit him; play Xiao Ming and exchange it for another style, color or size, while your partner is the sales associate. C. When you return, write an e-mail to your mom (妈妈：您好！… 祝好！ + your name) to thank her and update her on the gift. One sentence of the letter, which names a shopping center, reads in full: 蒙特雷的 Del Monte 购物中心有这家商店 (“This store is at the Del Monte shopping center in Monterey”).",
             examples=[D(*x) for x in MOM]),
        card("Activity 4 (Listening, Speaking and Writing): videos",
             "Divide into two groups; Group A watches Video 1 and Group B Video 2 from the Chinese TV program 爸爸去哪儿 and takes notes (new words: 金色 jīnsè, golden; 借 jiè, borrow); then discuss, exchange stories in pairs, watch both again, and learn how the subtle accent differences led to the children’s errors in the videos. If time permits, write your own dialogs for the two videos. (The videos are not included.)"),
    ],
    exercises=[
        M("What does the red ad say about summer clothes?", "夏装七折 — summer clothes 30% off", ["Summer clothes are free", "Summer clothes are 70% off", "No summer clothes"], "七折 means pay 70 percent."),
        M("What does the blue ad offer on the second pair?", "第二双半价 — half price", ["Free", "Double price", "20% off"], "买一双，第二双半价。"),
        M("What does 买一千送二百 mean?", "Spend 1,000, get 200 back", ["Spend 200, get 1,000", "Buy 1,000 items", "1,200 yuan off"], "送 = give as a gift."),
        M("What does the yellow ad give just for coming?", "A small gift (小礼物)", ["Free food", "Cash", "A coupon for next year"], "来就送小礼物。"),
        M("What does 两件八点五折 mean in the yellow ad?", "Two pieces at 15% off", ["Two pieces at 85% off", "Two for the price of one", "Two pieces at 8.5 yuan"], "八点五折: pay 85 percent."),
        M("What does 红色 mean?", "red", ["green", "brown", "yellow"], "红色 hóngsè."),
        M("What does 绿色 mean?", "green", ["red", "purple", "brown"], "绿色 lǜsè."),
        M("What does 灰色 mean?", "gray", ["white", "black", "orange"], "灰色 huīsè."),
        M("What does 深蓝色 mean?", "dark blue", ["light blue", "pink", "sky"], "深 means dark."),
        M("What does 浅 mean?", "light (of color)", ["dark", "deep", "wide"], "浅蓝色: light blue."),
        M("What did Xiao Ming’s mom buy him?", "Clothing he can wear when he exercises", ["A coat", "A suit", "A pair of shoes"], "给你买了一件锻炼的时候可以穿的衣服。"),
        M("What is his mom’s concern?", "His size might have changed, since she hasn’t seen him for a year", ["The color might be wrong", "He might not like it", "It might be too expensive"], "有一年没见到你了，不知道你的衣服大小是不是还和以前一样。"),
        M("What does she say he can do if the size is wrong?", "Take the receipt to the store and exchange it", ["Throw it away", "Send it back by mail", "Wear it anyway"], "你可以拿收据去店里换。"),
        F("要是大小不合适，你可以拿收据去店里___。", "换", PART, "换 means to exchange."),
        F("买一双，第二双___价。", "半", PART, "半价: half price."),
    ],
)

# ------------------------------------------------------------------ 10. vocabulary
L10 = vocab_lesson("Lesson 9 Presentation 1 vocabulary (24 words)", "原价 · 样式 · 试衣间 · 扫码 · 降价 · 合适 · 打折 · 穿",
                   "Vocabulary list (Lesson 9 Presentation 1)",
                   "The book’s 24 words, with the traditional form where it differs.", VOC1)

UNIT = unit("第九课 买东西 Presentation 1: shopping for clothes", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
