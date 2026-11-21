"""Unit 26: Lesson 9 (Shopping) Presentation 2, from the book's texts: the farmers' market dialog, weights, measure words for
produce, 就 for "just, only", David's diary, the three paragraphs about markets, passages about two shoppers and the vocabulary list.
The listening activities, the pictures, the apps and web pages, and the fill-in tables are not included; the lessons say so."""
from zh_auto import *
from zh_l9_vocab import VOC2

PART = ["吗", "们", "呢"]
FOOD = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P2 = [
    ("琳达", "大卫，这个摊子的蔬菜和水果真多呀。", "David, this stand has so many vegetables and fruits."),
    ("大卫", "那咱们买点吧。", "Then let’s buy some."),
    ("琳达", "老板，请问苹果多少钱一斤？", "Boss, how much are the apples per jin?"),
    ("摊主", "五块钱一斤。你想买几斤？", "Five yuan a jin. How many jin do you want?"),
    ("琳达", "我要三斤。再买一串香蕉、两斤桔子。", "I want three jin. And also a bunch of bananas and two jin of tangerines."),
    ("摊主", "三斤苹果十五块，一串香蕉十块，两斤桔子八块。", "Three jin of apples is fifteen yuan, a bunch of bananas ten yuan, two jin of tangerines eight yuan."),
    ("大卫", "天气这么热，老板，再给我们称个西瓜吧。", "The weather is so hot, boss; please also weigh a watermelon for us."),
    ("摊主", "西瓜十二斤半，五十块。", "The watermelon is twelve and a half jin, fifty yuan."),
    ("琳达", "有点儿贵，能不能便宜点儿？", "It’s a bit expensive; can you make it a little cheaper?"),
    ("摊主", "那就四十五块吧。我们的蔬菜很新鲜，你们买点儿吧。", "Then make it forty-five yuan. Our vegetables are very fresh; buy some."),
    ("大卫", "好，给我们来两斤西红柿，一把菠菜，一斤青椒和四斤土豆。", "Okay, give us two jin of tomatoes, a bunch of spinach, a jin of green peppers and four jin of potatoes."),
    ("琳达", "一共多少钱？", "How much is it altogether?"),
    ("摊主", "水果七十八块，加上蔬菜，一共一百零二块。你就给我一百吧。", "The fruit is seventy-eight yuan; with the vegetables, one hundred and two altogether. Just give me one hundred."),
    ("琳达", "这是一百块。谢谢！", "Here is one hundred yuan. Thank you!"),
    ("大卫", "对了，琳达，我们再去买点海鲜和牛肉吧。", "Oh, Linda, let’s also go buy some seafood and beef."),
    ("琳达", "好，走吧。", "Okay, let’s go."),
]
LIST = [("苹果", "三斤", "十五块"), ("香蕉", "一串", "十块"), ("桔子", "两斤", "八块"), ("西瓜", "十二斤半 (one)", "四十五块 (after bargaining; first 五十块)"), ("西红柿", "两斤", "(vegetables together)"), ("菠菜", "一把", "(vegetables together)"), ("青椒", "一斤", "(vegetables together)"), ("土豆", "四斤", "(vegetables together)")]
FRUITS = [("西瓜", "watermelon"), ("桔子", "tangerine"), ("苹果", "apple"), ("香蕉", "banana")]
VEGS = [("青椒", "green bell pepper"), ("西红柿", "tomato"), ("菠菜", "spinach"), ("土豆", "potato")]
OTHER = [("新鲜", "fresh"), ("海鲜", "seafood"), ("牛肉", "beef"), ("摊子", "vendor stand"), ("老板", "boss, owner"), ("称", "to weigh")]
L1 = lesson(
    "Lesson 9 Presentation 2: at the farmers’ market (dialog)",
    "苹果多少钱一斤？ · 能不能便宜点儿？ · 一共多少钱？",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. What are your favorite fruits and vegetables? Can you say them in Chinese? B. Have you been to any of the Monterey farmers’ markets? What fruits and vegetables have you bought?"),
        card("Presentation 2: 琳达 and 大卫 at a market stand",
             "The book also prints the dialog in traditional characters (for example 老闆，請問蘋果多少錢一斤？). Note from the book: colloquially, both 要 and 来 often substitute for the verb “to buy” when shopping, or “to order” in restaurants.",
             examples=dlg(P2)),
        card("Activity 1: fruit, vegetables and the other words",
             "A. Write the characters for the fruits and vegetables from the word bank (新鲜, 西瓜, 桔子, 海鲜, 牛肉, 青椒, 苹果, 西红柿, 摊子, 菠菜, 香蕉, 土豆, 老板, 称) under their categories 水果 and 蔬菜. B. Pair up, identify the words that are not fruits or vegetables, and make one sentence per item. The sorting:",
             tables=[wtable(rows_py(FRUITS), title="水果 (fruit)"), wtable(rows_py(VEGS), title="蔬菜 (vegetables)"), wtable(rows_py(OTHER), title="Not fruit or vegetables")]),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Where is this conversation likely to take place? What are the three main activities in the presentation? B. Listen again and write the quantities you hear under pictures of 西瓜, 香蕉, 苹果, 西红柿, 桔子, 菠菜, 海鲜, 土豆 and 青椒 (audio, not included). C. Read Presentation 2 and complete a shopping list (item, amount, price; if no price per unit is given, list the price of the group). D. Compare lists with a partner. From the text: at a market stand; the three activities are asking prices, bargaining and paying. The shopping list (the table is mine):",
             tables=[table(["Item", "Amount", "Price"], LIST, say=[0], title="The customer’s shopping list")]),
    ],
    exercises=[
        M("How much are the apples per jin?", "Five yuan", ["Fifteen yuan", "Eight yuan", "Ten yuan"], "五块钱一斤。"),
        M("How many jin of apples does 琳达 buy?", "Three", ["Two", "Five", "Twelve"], "我要三斤。"),
        M("How much is three jin of apples?", "Fifteen yuan", ["Five yuan", "Ten yuan", "Eight yuan"], "三斤苹果十五块。"),
        M("How much is a bunch of bananas?", "Ten yuan", ["Five yuan", "Eight yuan", "Fifteen yuan"], "一串香蕉十块。"),
        M("How much is two jin of tangerines?", "Eight yuan", ["Ten yuan", "Five yuan", "Twelve yuan"], "两斤桔子八块。"),
        M("How much does the watermelon weigh?", "Twelve and a half jin", ["Two and a half jin", "Twelve jin", "Fifty jin"], "西瓜十二斤半。"),
        M("What is the watermelon’s price after bargaining?", "Forty-five yuan", ["Fifty yuan", "Forty yuan", "Thirty yuan"], "那就四十五块吧。"),
        M("What is the total price of the fruit?", "Seventy-eight yuan", ["Seventy yuan", "One hundred and two yuan", "Fifty yuan"], "水果七十八块。"),
        M("What is the grand total with the vegetables?", "One hundred and two yuan", ["Seventy-eight yuan", "One hundred yuan", "One hundred and twenty yuan"], "一共一百零二块。"),
        M("How much does 琳达 pay?", "One hundred yuan", ["One hundred and two yuan", "Seventy-eight yuan", "Fifty yuan"], "你就给我一百吧。 这是一百块。"),
        M("What do 大卫 and 琳达 plan to buy next?", "Seafood and beef", ["Clothes", "Shoes", "Flowers"], "我们再去买点海鲜和牛肉吧。"),
        M("How does 琳达 ask for a lower price?", "能不能便宜点儿？", ["能不能贵点儿？", "能不能多点儿？", "能不能快点儿？"], "便宜点儿: a little cheaper."),
        M("Which word is a fruit?", "香蕉", ["菠菜", "土豆", "青椒"], "香蕉 is banana."),
        M("Which word is a vegetable?", "菠菜", ["香蕉", "苹果", "桔子"], "菠菜 is spinach."),
        F("老板，请问苹果多少钱一___？", "斤", PART, "斤 is the unit of weight (0.5 kg)."),
        F("再买一___香蕉。", "串", PART, "串 is the measure word for a bunch."),
        mean("摊子", "tan1 zi5", "vendor stand", ["boss", "fresh", "to weigh"]),
        mean("称", "cheng1", "to weigh", ["to buy", "to go", "to pay"]),
    ],
)

# ------------------------------------------------------------------ 2. weights and measure words
WEIGHT = [("钱", "qian2", "5 g = 0.176 oz"), ("两", "liang3", "10 钱 = 50 g = 1.7637 oz"), ("斤", "jin1", "10 两 = 500 g = 1.1023 lb")]
MW = [("斤", "Number + 斤 + Noun", "sold by weight", "一斤橘子 · 一斤苹果"), ("把", "Number + 把 + Noun", "sold by the bundle", "一把菠菜 · 一把鲜花"), ("个", "Number + 个 + Noun", "sold individually", "一个西瓜 · 一个土豆"), ("串", "Number + 串 + Noun", "sold in bunches or clusters", "一串香蕉 · 一串葡萄")]
MWEX = [("两斤西红柿", "two jin of tomatoes"), ("一个西瓜", "a watermelon"), ("三把菠菜", "three bunches of spinach"), ("一串香蕉", "a bunch of bananas")]
MW2 = [("李平喜欢每天吃午饭的时候，吃一个苹果。", "Li Ping likes to eat an apple every day at lunch."), ("珍尼买的西红柿是十块钱三斤半。", "The tomatoes Jenny bought are ten yuan for three and a half jin."), ("我想去菜摊买两把菠菜。", "I want to go to the vegetable stand and buy two bunches of spinach."),
       ("请给我称四斤桔子。", "Please weigh four jin of tangerines for me."), ("这种黄香蕉，给我来两串。", "This kind of yellow banana, give me two bunches."), ("老张，帮我挑一个大点儿的西瓜。", "Old Zhang, help me pick a bigger watermelon.")]
BUDGET = [("西红柿一斤二块五，我买了两斤半，一共六块二毛五。", "Tomatoes are 2.5 yuan a jin; I bought two and a half jin, 6.25 yuan altogether.")]
CARD = [("西红柿", "按斤称", "一斤半", "¥2.5 / 一斤"), ("菠菜", "两把", "", "¥1.8 / 一把"), ("西瓜", "按斤称", "八斤三两", "¥1.6 / 一斤 (the card prints 一把)"), ("桔子", "按斤称", "四斤八两", "¥2.3 / 一斤"), ("香蕉", "两串", "", "¥3.1 / 一串"), ("苹果", "按斤称", "两斤二两", "¥1.9 / 一斤"), ("鲜花", "三把", "", "¥8 / 一把")]
L2 = lesson(
    "Lesson 9 Presentation 2 grammar: weights and measure words for produce",
    "钱 两 斤 · 一把菠菜 · 一串香蕉 · 一个西瓜 · 按斤称",
    requires=[],
    cards=[
        card("Basic units of weight",
             "The market system: 1 钱 = 5 g (0.176 oz); 1 两 = 10 钱 = 50 g (1.7637 oz); 1 斤 = 10 两 = 500 g (1.1023 lb). So 斤 in the market is half a kilogram.",
             tables=[wtable(WEIGHT, title="Units of weight")]),
        card("Activity 1 (Reading, Speaking and Writing): the farmers’ market",
             "A. Xiao Ming went to the farmers’ market for his grandmother. Since they don’t give receipts, he wrote down what he spent on each item (a table with vegetable or fruit, weight or amount, unit price, price). Read the shopping list, calculate the total he spent, and take turns playing him reporting back to his grandmother in Chinese. The book’s example (the numbers are spelled out here):",
             examples=[D(z, e) for z, e in BUDGET]),
        card("Activity 1B: information gap",
             "Pair up: one of you is a vendor and the other a customer. Look at your role-play card and fill in the missing information on your card. The vendor card (the customer card has the amounts and asks for the prices):",
             tables=[table(["Fruit or vegetable", "By weight or amount", "Amount", "Unit price"], CARD, say=[0], title="Vendor card")]),
        card("Measure words for fruits and vegetables",
             "To specify a certain number of fruits or vegetables, place a measure word between the number and the noun: Number + Measure Word + Noun.",
             examples=[D(z, e) for z, e in MWEX],
             tables=[table(["Measure word", "Pattern", "Used for", "Examples"], MW, say=[0], title="斤 把 个 串")]),
        card("Activity 2 (Reading and Speaking): choose the measure word",
             "A. Choose the correct measure word for each sentence (the book gives two choices each); check your work with a partner. B. Read the completed sentences aloud and translate them. The key (mine, from the choices):",
             examples=[D(z, e) for z, e in MW2]),
    ],
    exercises=[
        M("How many grams is one 斤?", "500", ["50", "5", "1,000"], "1 斤 = 500 g."),
        M("How many 两 make one 斤?", "Ten", ["Five", "Twenty", "One hundred"], "1 斤 = 10 两."),
        M("How many grams is one 两?", "50", ["5", "500", "10"], "1 两 = 50 g."),
        M("Which measure word is for produce sold by weight?", "斤", ["把", "个", "串"], "一斤橘子/苹果."),
        M("Which measure word is for bundles, like spinach?", "把", ["斤", "个", "串"], "一把菠菜."),
        M("Which measure word is for items sold individually, like a watermelon?", "个", ["斤", "把", "串"], "一个西瓜."),
        M("Which measure word is for bunches, like bananas or grapes?", "串", ["个", "把", "斤"], "一串香蕉."),
        M("Which sentence is right: “I bought two bunches of spinach”?", "我买了两把菠菜。", ["我买了两串菠菜。", "我买了两个菠菜。", "我买了两斤菠菜把。"], "菠菜 is sold by the bundle (把)."),
        M("Which sentence is right: “Please weigh four jin of tangerines for me”?", "请给我称四斤桔子。", ["请给我称四个桔子。", "请给我称四把桔子。", "请给我称四串桔子斤。"], "桔子 is sold by weight."),
        M("Which sentence is right: “two bunches of this yellow banana”?", "给我来两串。", ["给我来两把。", "给我来两个。", "给我来两斤把。"], "香蕉: 串."),
        M("Where does the measure word go?", "Between the number and the noun", ["After the noun", "Before the number", "At the end"], "Number + Measure Word + Noun."),
        F("我想去菜摊买两___菠菜。", "把", PART, "菠菜 takes 把."),
        F("请给我称四___桔子。", "斤", PART, "称 goes with weight: 斤."),
        F("李平吃一___苹果。", "个", PART, "苹果 can be 个 when eaten individually."),
        mean("斤", "jin1", "0.5 kg", ["bunch", "bundle", "yuan"]),
    ],
)

# ------------------------------------------------------------------ 3. 就 for only/just
JIU1 = [("就四十块吧！", "Just forty yuan!"), ("我就一个哥哥。", "I have only one older brother."), ("他在美国就一个亲人。", "He has only one relative in America."), ("你们家就一个孩子吗？", "Does your family have only one child?")]
JIU2 = [("就给我一百吧！", "Just give me one hundred!"), ("你就点了两个菜吗？", "Did you order only two dishes?"), ("我早饭就喝了一杯咖啡。", "For breakfast I only drank a cup of coffee."), ("在这儿我就认识她。", "Here I only know her.")]
JIU_T = [("这个摊子就卖水果。", "This stand only sells fruit."), ("今天晚上我们就一个作业。", "We only have one homework assignment for tonight."), ("他就吃鸡肉。", "He only eats chicken."), ("我就有二十块。", "I only have twenty dollars."),
         ("她就认识一百个汉字。", "She only knows 100 Chinese characters."), ("她女儿就在一个地方工作。", "Her daughter only works at one place."), ("就给我五十块吧。", "Just give me fifty.")]
L3 = lesson(
    "Lesson 9 Presentation 2 grammar: 就 for “just” or “only”",
    "我就一个哥哥 · 就给我一百吧 · 我早饭就喝了一杯咖啡",
    requires=[],
    cards=[
        card("就 for “just” or “only”",
             "In Lesson 4 you used 就 to mean “indeed” or “exactly”. In this lesson 就 can also mean “only” or “just”. Type 1: Subject + 就 + Number + Measure Word + Noun. Type 2: Subject + 就 + Verb Phrase.",
             examples=[D(z, e) for z, e in JIU1] + [D(z, e) for z, e in JIU2]),
        card("Activity 3 (Speaking and Writing)",
             "A. Work with a partner to translate into Chinese: 1. This stand only sells fruit. 2. We only have one homework assignment for tonight. 3. He only eats chicken. 4. I only have $20. 5. She only knows 100 Chinese characters. 6. Her daughter only works at one place. 7. Just give me $50. One possible translation of each (mine):",
             examples=[D(z, e) for z, e in JIU_T]),
        card("Activity 3B and Activity 4",
             "3B. Use 就 to write two true and one false statement about yourself; 3C read them to your partner and have them guess the false one. Activity 4: divide into shopkeepers and shoppers. Shopkeepers decide which eight items to sell (shirts, suits, shoes, computers, cell phones, fruits and vegetables), draw each on a card and write the price underneath; each has ¥150 for change and may sell each item once. Shoppers make a shopping list of six items (color, size, style, type, quantity, amount to spend) and have ¥600 each. B. Begin shopping, and bargain! Keep each card you buy. C. When time is up, shopkeepers win by most items sold and most profit; shoppers by most items bought and least spent."),
    ],
    exercises=[
        M("What does 就 mean in 我就一个哥哥?", "only, just", ["already", "exactly", "then"], "就 + number + measure word + noun: only."),
        M("What does 你们家就一个孩子吗？ ask?", "Does your family have only one child?", ["Do you have a child?", "Are you an only child?", "Where is your child?"], "就一个孩子: only one child."),
        M("What does 就给我一百吧 mean?", "Just give me one hundred", ["Give me one hundred, then", "I will give you one hundred", "One hundred is too much"], "就 + verb phrase: just."),
        M("What does 我早饭就喝了一杯咖啡 mean?", "For breakfast I only drank a cup of coffee", ["I drank coffee at breakfast already", "I never drink coffee", "I drank a cup of coffee, then breakfast"], "就 + verb phrase: only."),
        M("What does 在这儿我就认识她 mean?", "Here I only know her", ["Here I know her already", "I know her here", "She knows me"], "就认识她: only know her."),
        M("Which is Type 1?", "我就一个哥哥。", ["我早饭就喝了一杯咖啡。", "你就点了两个菜吗？", "在这儿我就认识她。"], "Subject + 就 + number + measure word + noun."),
        M("Which is Type 2?", "你就点了两个菜吗？", ["我就一个哥哥。", "他在美国就一个亲人。", "就四十块吧！"], "Subject + 就 + verb phrase."),
        M("How do you say “I only have twenty dollars”?", "我就有二十块。", ["我二十块就有。", "就我有二十块吗。", "我有就二十块。"], "就 before the verb."),
        M("How do you say “Just give me fifty”?", "就给我五十块吧。", ["给我就五十块吧。", "给就我五十块吧。", "五十块就吧给我。"], "就 before 给."),
        F("我___一个哥哥。", "就", PART, "就 + number: only."),
        F("他在美国就一个___。", "亲人", ["作业", "操场", "预习"], "就一个亲人: only one relative."),
        mean("就", "jiu4", "just; only (emphasis)", ["pair", "arrive", "wait"]),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
DIARY = [
    "今天一下课，我就和马林去逛农贸市场。农贸市场在蒙特雷山下，从国防语言学院到农贸市场走二十分钟就到了。",
    "农贸市场什么东西都有，不但有卖蔬菜、水果的，而且还有卖衣服、鲜花、小吃的。那儿的水果和蔬菜都很新鲜，种类又多，不过那儿的价格比别的地方贵一点。",
    "那天我买了五个西红柿、一把菠菜、两斤苹果和一串香蕉。马林很喜欢中国小吃，他买了几个包子和一杯奶茶。摊主听说他是学生，还给他打了九折。",
    "买完东西以后，我们就高高兴兴地回学校了。",
]
PARA = [
    ("Paragraph 1 (supermarkets)", "后来有了超市，人们开始去超市买生鲜蔬果。因为超市常常打折，有些蔬菜、水果的价格有时会比外面菜市场便宜。在超市买东西不但可以用现金，还可以刷卡，非常方便。"),
    ("Paragraph 2 (online)", "最近几年，有越来越多的人喜欢上网买菜。他们可以在网上挑想买的蔬菜水果，用手机付费，然后东西就会送到家，不出门就可以吃到各种新鲜的水果、蔬菜，真是太方便了。"),
    ("Paragraph 3 (traditional markets)", "中国人以前都爱去菜市场买东西，因为菜市场的东西又新鲜又便宜。除了卖蔬菜、水果，他们也卖海鲜和肉类。有些菜市场还卖衣服和鞋子等。"),
]
L4 = lesson(
    "Lesson 9 Presentation 2 skill integration: 找, 花, David’s diary and the market article",
    "农贸市场 · 种类 价格 奶茶 摊主 · 菜市场 超市 上网买菜",
    requires=[],
    cards=[
        card("Activity 1: new words, a dialog and a radio ad",
             "New words: 找 (zhǎo) find; look for; give change. 花 (huā) flower. Activity 1: listen to a dialog and take notes, write three questions about it for a partner, then role-play the script (audio, not included). Activity 2: listen to a radio advertisement, extract the elements of essential information, write a summary and three specific details, report them to a partner in Chinese, write a script for a Chinese ad for the shop together and post it on Linoit, and vote for the best ad as a class (audio, not included).",
             tables=[wtable([("找", "zhao3", "find; look for; give change"), ("花", "hua1", "flower")], title="New words")]),
        card("Activity 3: David’s diary entry about the farmers’ market (农贸市场)",
             "A. In pairs, take turns reading and translating each sentence. B. Together, write three significant facts about the farmers’ market, with details. C. Guess the meaning of 种类, 价格, 奶茶 and 摊主 from context and share your strategies. D. Listen to a monolog about two other students’ trip and number nine pictures in the order they visited the stands (audio and pictures, not included). E. Share the itinerary with your partner in Chinese.",
             examples=[D(s, e) for s, e in zip(DIARY, [
                 "Right after class today I went with Ma Lin to browse the farmers’ market. The market is at the foot of Monterey’s hills, and from the Defense Language Institute it takes twenty minutes on foot.",
                 "The market has everything: not only vegetables and fruit but also clothes, flowers and snacks. The fruit and vegetables are fresh and there are many kinds, but the prices there are a bit higher than elsewhere.",
                 "That day I bought five tomatoes, a bunch of spinach, two jin of apples and a bunch of bananas. Ma Lin likes Chinese snacks; he bought a few baozi and a cup of milk tea. The vendor heard he was a student and gave him ten percent off.",
                 "After we finished shopping, we happily went back to the school."])]),
        card("Activity 4: the newspaper article, paragraphs in the wrong order",
             "The paragraphs of an online article have been posted in the wrong order. A. In groups of three, read one paragraph each and take notes. B. Report on your paragraph in Chinese, listen to the other two and fill in the table. C. Put the three paragraphs in the correct order. D. Guess what the underlined 超市 and 上网 mean from context. The correct order (mine, from the content): 3, then 1, then 2: traditional markets, then supermarkets, then buying online.",
             examples=[D(z, e) for (t, z), e in zip(PARA, [
                 "Later there were supermarkets, and people began to buy fresh produce there. Supermarkets often have sales, so some vegetables and fruit are sometimes cheaper than at the outside markets. In a supermarket you can pay with cash or by card, which is very convenient.",
                 "In recent years more and more people like to buy groceries online. They can pick the vegetables and fruit they want online and pay by phone, and the things are delivered home; without going out you can eat all kinds of fresh fruit and vegetables, which is really convenient.",
                 "Chinese people used to love going to the vegetable market, because the things there were fresh and cheap. Besides vegetables and fruit, they also sell seafood and meat. Some markets even sell clothes and shoes."])]),
    ],
    exercises=[
        M("Where is the farmers’ market in David’s diary?", "At the foot of the Monterey hills", ["Next to the school", "In the city center", "By the sea"], "农贸市场在蒙特雷山下。"),
        M("How long does it take to walk from the school to the market?", "Twenty minutes", ["Two minutes", "Two hours", "Ten minutes"], "走二十分钟就到了。"),
        M("Besides vegetables and fruit, what do they sell at the market?", "Clothes, flowers and snacks", ["Computers", "Cars", "Furniture"], "还有卖衣服、鲜花、小吃的。"),
        M("What does David say about the prices there?", "A bit higher than elsewhere", ["Much cheaper", "The same", "Not marked"], "那儿的价格比别的地方贵一点。"),
        M("What did David buy?", "Five tomatoes, a bunch of spinach, two jin of apples and a bunch of bananas", ["Five apples and two tomatoes", "Two jin of bananas", "Only spinach"], "五个西红柿、一把菠菜、两斤苹果和一串香蕉。"),
        M("What did 马林 buy?", "A few baozi and a cup of milk tea", ["Five tomatoes", "A watermelon", "Flowers"], "他买了几个包子和一杯奶茶。"),
        M("Why did the vendor give 马林 a discount?", "He heard he was a student", ["He bought a lot", "He is a friend", "It was closing time"], "摊主听说他是学生，还给他打了九折。"),
        M("What does 打九折 mean?", "Take ten percent off", ["Give nine yuan", "Pay nine times", "Ninety percent more"], "九折: nine-tenths of the price."),
        M("Which paragraph of the article is first?", "Traditional markets", ["Supermarkets", "Online grocery buying", "Credit cards"], "中国人以前都爱去菜市场买东西。"),
        M("In the article, what is a supermarket advantage?", "Sales, and you can pay by card", ["Always cheaper", "You can bargain", "Delivery to your home"], "超市常常打折 and 可以刷卡。"),
        M("In the article, how do people who buy groceries online pay?", "By phone", ["Only cash", "By check", "With coupons"], "用手机付费。"),
        M("What does 找 mean at a stand?", "To give change", ["To pay", "To weigh", "To bargain"], "找 also means find; look for; give change."),
        F("今天一下课，我___和马林去逛农贸市场。", "就", PART, "一…就…: as soon as."),
        F("摊主听说他是学生，还给他打了九___。", "折", PART, "打九折: ten percent off."),
        mean("种类", "zhong3 lei4", "kind, type", ["price", "vendor", "milk tea"], ),
        mean("价格", "jia4 ge2", "price", ["kind, type", "vendor", "snack"]),
        mean("奶茶", "nai3 cha2", "milk tea", ["price", "vendor", "kind, type"]),
        mean("摊主", "tan1 zhu3", "stand owner", ["price", "milk tea", "student"]),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context
P_1 = "王美美在电脑公司工作，她平时工作很忙，没有时间去菜市场买菜，所以只能下班以后去附近的超市买，虽然超市的价钱比其他市场贵一点儿，可是东西很多，还能买到国外来的东西。超市也常会打折，所以有些蔬菜、水果的价格有时会比外面菜市场便宜。超市快关门以前，很多吃的东西都会有特价，非常便宜，所以不做饭也没问题。"
P_2 = "李妈妈是个家庭妇女，她喜欢天天去菜市场买菜。每天一起床，她就会先想想那天要做的菜，然后去菜市场。她喜欢先逛逛不同的摊子，问一下价钱，然后在最便宜、最新鲜的摊子上买。有时她买了很多东西，也会请摊主给她打折。回家以前，她还会逛逛卖衣服和鞋子的摊子，再买一些小吃。她觉得去一个地方什么东西都能买到，真的太方便了！"
L5 = lesson(
    "Lesson 9 Presentation 2 using Chinese in context: apps, a party and two shoppers",
    "77生鲜 · 王美美 · 李妈妈 · 超市和菜市场 · 台北的传统市场",
    requires=[],
    cards=[
        card("Activity 1: the app 77生鲜",
             "A. The page shows a popular app called 77生鲜 (a picture, not included). Answer with a partner: 1. What is this app used for? 2. What can you buy with this app? 3. What kind of services does it offer? How do you know? 4. What do you think 今日特价 means? 5. Based on the words you know, what do you think 首次购买生鲜免费送绿色土鸡蛋一盒 means? B. Share the strategies you used in Chinese. From the words: 今日特价 is today’s special price; the long line says that for a first purchase of fresh food you get a free box of green free-range eggs.",
             examples=[D("今日特价", "today’s special price"), D("首次购买生鲜免费送绿色土鸡蛋一盒", "For a first purchase of fresh food, get a free box of green free-range eggs")]),
        card("Activity 2: a farewell party in Taiwan",
             "After immersion in Taiwan, you and your classmates decide to cook some Chinese dishes for a farewell party to thank your teachers. You have a budget of NT$5000 (= $150.00) for the ingredients. A. In groups of three, discuss in Chinese what dishes you want to make, write a shopping list for the local market in Chinese and post it on Linoit. B. One group plays the vendors (meat, vegetable and fruit stands) and the other the shoppers; then switch. Shoppers must: ask the unit price of each item; specify the quantity; ask the vendor to weigh some items; ask the vendor to select particular items; negotiate for the best prices; ask for payment options; buy everything on the list within the budget."),
        card("Activity 3: Passage 1 and Passage 2",
             "A. Read Passage 1 while a partner reads Passage 2 and take notes. B. Report on your passage in Chinese while your partner fills in the key information. C. Discuss the questions: for each, what did you find out about her, and what shopping decisions does she make and why?",
             examples=[D(P_1, "Wang Meimei works at a computer company. She is usually busy and has no time to go to the vegetable market, so she can only shop at the nearby supermarket after work. Although supermarket prices are a bit higher than other markets, there are lots of things and you can even buy things from abroad. Supermarkets often have sales, so some vegetables and fruit are sometimes cheaper than at the outside market. Shortly before the supermarket closes, lots of food has special prices and is very cheap, so not cooking is no problem."),
                       D(P_2, "Mrs. Li is a housewife and likes to go to the vegetable market every day. As soon as she gets up she thinks about the dishes to make that day, then goes to the market. She likes to browse different stands first, ask the price, and then buy at the cheapest, freshest stand. Sometimes when she buys a lot she asks the vendor for a discount. Before going home she also browses the stands selling clothes and shoes and buys some snacks. She feels that being able to buy everything in one place is really convenient!")]),
        card("Activity 4 and Activity 5",
             "Activity 4. A. Listen to a dialog and answer in Chinese: 1. What is the first speaker’s assumption in the first sentence? 2. What does the second speaker say about the apple he bought? 3. What are three things he says about the farmers’ market? 4. What did the first speaker say he would do? (audio, not included). B. In groups of three, one group lists the advantages and disadvantages of shopping at a supermarket, the other those of a farmers’ market. C. Present your list and take notes on the other group’s; each group discusses the disadvantages of the other’s venue and presents a rebuttal in Chinese. D. Both groups write their lists in Chinese and post them on Linoit. Activity 5: during immersion you research traditional Chinese markets in Taipei. A. Browse two websites, 南門市場 (nanmenmarket.org) and 士東市場 (shi-dong.com), and discuss their key features in Chinese (the websites are not included). B. Discuss similarities and differences between traditional markets in Taipei and farmers’ markets in the U.S. C. Decide which market is better (location, prices, quality, variety) and research it. D. Create a PPT presentation on traditional markets in Taipei, with tips for shopping there, and present it to the class in Chinese."),
    ],
    exercises=[
        M("What does 今日特价 mean?", "Today’s special price", ["Today’s weather", "Today’s news", "Today’s class"], "特价: special price."),
        M("What is the free gift for a first purchase on the app?", "A box of green free-range eggs", ["A bunch of bananas", "A bag of rice", "A watermelon"], "免费送绿色土鸡蛋一盒。"),
        M("Where does 王美美 work?", "At a computer company", ["At a supermarket", "At a school", "At a restaurant"], "王美美在电脑公司工作。"),
        M("Why does 王美美 shop at the supermarket?", "She is busy and has no time for the vegetable market", ["It is cheaper", "It is closer to her school", "Her mother tells her to"], "她平时工作很忙，没有时间去菜市场买菜。"),
        M("When can she get very cheap food at the supermarket?", "Shortly before closing", ["On the weekend", "In the morning", "When she pays by card"], "超市快关门以前……特价。"),
        M("What can she buy at the supermarket that is not at the market?", "Things from abroad", ["Clothes", "Fresh flowers", "Snacks"], "还能买到国外来的东西。"),
        M("What is 李妈妈’s job?", "Housewife", ["Cook", "Teacher", "Shop owner"], "李妈妈是个家庭妇女。"),
        M("What does 李妈妈 do first when she gets up?", "Thinks about the dishes for the day", ["Goes to the supermarket", "Calls the vendor", "Buys snacks"], "她就会先想想那天要做的菜。"),
        M("Where does 李妈妈 buy her vegetables?", "At the cheapest, freshest stand", ["At the first stand", "At the supermarket", "Online"], "在最便宜、最新鲜的摊子上买。"),
        M("What does 李妈妈 do when she buys a lot?", "Asks the vendor for a discount", ["Pays by card", "Asks for a gift", "Goes elsewhere"], "也会请摊主给她打折。"),
        M("What does 李妈妈 like about the market?", "She can buy everything in one place", ["It is near her home", "It has a delivery service", "It is open at night"], "去一个地方什么东西都能买到。"),
        M("Which of the two shoppers goes to the market every day?", "李妈妈", ["王美美", "Both", "Neither"], "她喜欢天天去菜市场买菜。"),
        F("她喜欢先逛逛不同的摊子，问一下价钱，然后在最___、最新鲜的摊子上买。", "便宜", ["作业", "操场", "预习"], "最便宜: cheapest."),
        F("超市也常会打___，所以有些蔬菜、水果的价格比菜市场便宜。", "折", PART, "打折: give a discount."),
    ],
)

UNIT = unit("第九课 买东西 Presentation 2: at the market", [L1, L2, L3, L4, L5,
    vocab_lesson("Lesson 9 Presentation 2 vocabulary", "21 words: 一共 串 便宜 土豆 摊子 斤 新鲜 桔子 水果 海鲜 牛肉 称 老板 苹果 菠菜 蔬菜 西瓜 贵 走 零 青椒", "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)])
