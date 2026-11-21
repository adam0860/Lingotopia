"""Unit 27: Lesson 9 (Shopping) Presentation 3 and Area Studies, from the book's texts: shopping online, measure words for daily
necessities and clothes, 快...了, 连...都/也, the pivotal 请, the receipt, the department store reading, the Sunday passage,
the vocabulary list and "China's Booming Consumer Economy". Audio, pictures, videos and web pages are not included."""
from zh_auto import *
from zh_l9_vocab import VOC3

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the passage
PASS = [
    ("快开学了，大卫正准备去商场买文具和衣服，张文来了。", "School is about to start, and David was getting ready to go to the mall to buy stationery and clothes when Zhang Wen came."),
    ("他问大卫，为什么不上网买呢？", "He asked David why he didn’t buy online."),
    ("大卫告诉张文，他还没有中国的信用卡，不能在网上买东西。", "David told Zhang Wen that he did not have a Chinese credit card yet and could not buy things online."),
    ("张文马上说，“没问题，我可以先用信用卡帮你付账，然后，你给我现金就行了。”", "Zhang Wen immediately said, “No problem, I can first pay for you with my credit card, and then you just give me cash.”"),
    ("网上的文具种类真多，大卫买了一个名牌书包，还买了一些笔记本和圆珠笔。", "There are really many kinds of stationery online; David bought a name-brand school bag and also some notebooks and ballpoint pens."),
    ("买完文具以后，他又开始选购衣服，正好网上促销，很多东西都打折。", "After buying the stationery he started selecting clothes; by chance there was an online promotion and many things were discounted."),
    ("西装打九折，衬衫打八折，皮鞋和领带也都打折。", "Suits were ten percent off, shirts twenty percent off, and leather shoes and ties were also discounted."),
    ("最后，大卫买了一套蓝色西装、两条领带、六双袜子和一双黑皮鞋，连牙刷、毛巾都在网上买了，一共花了两千多块。", "In the end David bought a blue suit, two ties, six pairs of socks and a pair of black leather shoes; he even bought a toothbrush and towels online, spending over two thousand yuan altogether."),
    ("他觉得在网上买东西真是又便宜，又方便。", "He felt that buying things online is really both cheap and convenient."),
    ("他对张文说，“谢谢你，今天晚上我请你吃大餐。”", "He said to Zhang Wen, “Thank you; tonight I’ll treat you to a big meal.”"),
]
CLOZE = [("开学", "文具, 信用卡, 网上"), ]
ITEMS3 = [("书包", "school bag", "文具"), ("笔记本", "notebook", "文具"), ("圆珠笔", "ballpoint pen", "文具"), ("西装", "suit", "服装"), ("领带", "tie", "服装"), ("袜子", "socks", "服装"), ("皮鞋", "leather shoes", "服装"), ("牙刷", "toothbrush", "日用品"), ("毛巾", "towel", "日用品")]
FILLED = [("大卫想上网买一些开学用的东西，可是他没有中国的信用卡。", "David wanted to go online and buy some things for the start of school, but he has no Chinese credit card."),
          ("所以他请张文帮他在网上买。", "So he asked Zhang Wen to help him buy online."),
          ("他先买了一个书包，还有一些文具，有圆珠笔和笔记本。", "He first bought a school bag and some stationery, including ballpoint pens and notebooks."),
          ("因为正好有促销，所以他又选购了领带、西装、皮鞋和袜子。", "Because there happened to be a promotion, he also selected and bought ties, suits, leather shoes and socks."),
          ("最后他也买了一些日用品，像是牙刷和毛巾。", "Finally he also bought some daily necessities, such as a toothbrush and towels."),
          ("他觉得在网上买东西又便宜又方便。", "He feels that buying things online is both cheap and convenient.")]
L1 = lesson(
    "Lesson 9 Presentation 3: shopping online (passage)",
    "快开学了 · 上网买 · 信用卡 · 促销 · 打折 · 又便宜又方便",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. Do you prefer shopping at stores or online? What items do you usually buy online and why? B. List the things you bought in the last month, and their quantities; write as many items as you can in Chinese."),
        card("Presentation 3: 大卫 buys things online",
             "The book also prints the passage in traditional characters (for example 快開學了，大衛正準備去商場買文具和衣服).",
             examples=[D(z, e) for z, e in PASS]),
        card("Activity 2 (Listening, Writing and Reading)",
             "A. Global listening: listen to Presentation 3 once and answer: 1. What is the presentation about? 2. What are David and Zhang Wen’s relationship and how do you know? 3. What does David say about his new experience? B. Detailed listening: listen again and write the items David purchased under 文具 (stationery), 服装 (clothing) and 日用品 (daily necessities) (audio, not included). C. Read Presentation 3 aloud to check your answers. From the text, the sorting (mine):",
             tables=[table(["Item", "English", "Category"], ITEMS3, say=[0, 2], title="What David bought")]),
        card("Activity 3: complete the passage",
             "A. Complete the passage with words from the word bank; there are more words than you will need: 信用卡, 选购, 圆珠笔, 牙刷, 促销, 便宜, 上网, 网上, 开学, 现金 (the unused ones are 现金 and 上网). B. Check your answers with a partner and share your strategies. The completed passage (the key is mine):",
             examples=[D(z, e) for z, e in FILLED]),
        card("Activity 4 (Listening and Speaking)",
             "A. Listen to two dialogs and write what each customer bought and their total expenditure (item, quantity, total amount) (audio, not included). B. Check your answers with a partner. Then use 先, 然后 and 最 to report on Dialog 1, while your partner reports on Dialog 2."),
    ],
    exercises=[
        M("Why does 大卫 not buy online by himself?", "He has no Chinese credit card yet", ["The website is closed", "He has no time", "He has no phone"], "他还没有中国的信用卡，不能在网上买东西。"),
        M("How does 张文 help?", "He pays with his credit card first", ["He gives David his school bag", "He goes to the mall", "He lends David a phone"], "我可以先用信用卡帮你付账。"),
        M("How will 大卫 repay 张文?", "With cash", ["With a gift", "With a credit card", "He will not repay"], "你给我现金就行了。"),
        M("What did 大卫 buy first?", "A name-brand school bag", ["A suit", "A tie", "Socks"], "大卫买了一个名牌书包。"),
        M("Why was the clothing cheap?", "There was an online promotion", ["It was used", "It was a gift", "It was old"], "正好网上促销，很多东西都打折。"),
        M("How much off were the suits?", "Ten percent", ["Twenty percent", "Fifty percent", "Thirty percent"], "西装打九折。"),
        M("How much off were the shirts?", "Twenty percent", ["Ten percent", "Fifty percent", "Thirty percent"], "衬衫打八折。"),
        M("What colour were the shoes?", "Black", ["Blue", "Red", "White"], "一双黑皮鞋。"),
        M("How many pairs of socks did he buy?", "Six", ["Two", "One", "Nine"], "六双袜子。"),
        M("How much did 大卫 spend altogether?", "More than two thousand yuan", ["Two hundred yuan", "One thousand yuan", "Fifty yuan"], "一共花了两千多块。"),
        M("How does 大卫 thank 张文?", "He will treat him to a big meal", ["He gives him a bag", "He pays his rent", "He says nothing"], "今天晚上我请你吃大餐。"),
        M("Which is a daily necessity in this lesson?", "牙刷", ["西装", "圆珠笔", "书包"], "牙刷 and 毛巾 are daily necessities."),
        M("Which is stationery?", "圆珠笔", ["领带", "毛巾", "袜子"], "圆珠笔 and 笔记本 are stationery."),
        F("快___了，大卫正准备去商场买文具和衣服。", "开学", NOUN, "快开学了: school is about to start."),
        F("大卫没有中国的___，所以请张文帮他付账。", "信用卡", NOUN, "信用卡: credit card."),
        F("网上正好有___，很多东西都打折。", "促销", NOUN, "促销: a sales promotion."),
        F("他觉得在网上买东西又便宜又___。", "方便", PART, "又便宜又方便: cheap and convenient."),
    ],
)

# ------------------------------------------------------------------ 2. measure words
MW3 = [("本", "Number + 本 + Noun", "books, magazines, etc.", "一本书/笔记本/字典"),
       ("把", "Number + 把 + Noun", "items with handles or that can otherwise be carried by hand", "一把牙刷"),
       ("筒", "Number + 筒 + Noun", "items that come in tubes", "一筒牙膏"),
       ("条", "Number + 条 + Noun", "long or dangly objects", "一条裤子/毛巾/领带"),
       ("套", "Number + 套 + Noun", "set", "一套西装"),
       ("件", "Number + 件 + Noun", "piece (of clothing)", "一件衣服/军服"),
       ("双", "Number + 双 + Noun", "pair", "一双筷子/鞋/袜子"),
       ("支", "Number + 支 + Noun", "long, thin, inflexible objects", "一支圆珠笔/铅笔")]
MWEX3 = [("一套西装", "a suit"), ("两筒牙膏", "two tubes of toothpaste"), ("三双男式皮鞋", "three pairs of men’s leather shoes"), ("四条领带", "four ties")]
KEYA = [("一把牙刷", "toothbrush"), ("两条毛巾", "towels"), ("三支铅笔", "pencils"), ("四块肥皂", "bars of soap"), ("一个杯子", "cup"), ("一筒牙膏", "toothpaste")]
KEYB = [("一双皮鞋", "leather shoes"), ("五条领带", "ties"), ("一个书包", "school bag"), ("一套西装", "suit"), ("两条裤子", "pants"), ("六本笔记本", "notebooks")]
KEYC = [("一套西装", "suit"), ("三筒牙膏", "toothpaste"), ("五本笔记本", "notebooks"), ("七双运动鞋", "sneakers"), ("九条裤子", "pants"), ("两把牙刷", "toothbrushes"), ("四支铅笔", "pencils"), ("六支圆珠笔", "ballpoint pens"), ("八件恤衫", "T-shirts"), ("十条领带", "ties")]
STORY = [("甲：上个周末我去军人商店想买一双运动鞋。", "Last weekend I went to the military store to buy a pair of sneakers."), ("乙：不过到了商店，服务员告诉我他们没有我喜欢的颜色。", "But when I got to the store, the clerk told me they didn’t have the color I like."), ("丙：所以我没买到运动鞋，可是我买了几只圆珠笔和一本笔记本。", "So I didn’t get the sneakers, but I bought a few ballpoint pens and a notebook.")]
L2 = lesson(
    "Lesson 9 Presentation 3 grammar: measure words for daily necessities and clothing",
    "一套西装 · 两筒牙膏 · 三双皮鞋 · 四条领带 · 本 把 筒 条 套 件 双 支",
    requires=[],
    cards=[
        card("Measure words for daily necessities, clothing and accessories",
             "When specifying the number of items, a measure word comes between the number and the noun: Number + Measure Word + Noun.",
             examples=[D(z, e) for z, e in MWEX3],
             tables=[table(["Measure word", "Pattern", "Used for", "Examples"], MW3, say=[0], title="本 把 筒 条 套 件 双 支")]),
        card("Activity 1 (Presentation 3 Activities): fill in the measure words",
             "A. For each item on the two shopping lists, fill in the blank with a measure word from the word bank (把, 双, 条, 支, 块, 套, 筒, 双). B. Check your answers with a partner. Can you generalize the rules for these measure words? The book gives no key and 杯子 is not covered by the bank, so the key is mine (杯子 takes 个).",
             tables=[table(["Customer A", "English"], KEYA, say=[0], title="Customer A"), table(["Customer B", "English"], KEYB, say=[0], title="Customer B")]),
        card("Grammar and Usage, Activity 1: fill in the appropriate measure words",
             "A. Fill in the appropriate measure words for the ten items from the bank 本, 把, 筒, 支, 双, 件, 条, 套 (key mine). B. 故事接龙: go around the class, each student saying one sentence with vocabulary from the word bank to build a story about shopping. Bank: 信用卡, 现金, 书包, 笔记本, 圆珠笔, 西装, 衬衫, 领带, 皮鞋, 毛巾, 袜子, 牙刷, 促销/打折, 便宜, 方便, 付账, 觉得, 上网/网上, 先, 然后, 连, 最后, 快, 了. The book’s example (A, B, C are 甲, 乙, 丙):",
             tables=[table(["Phrase", "English"], KEYC, say=[0], title="The ten items")],
             examples=[D(z, e) for z, e in STORY]),
    ],
    exercises=[
        M("Which measure word goes with 西装?", "套", ["本", "把", "筒"], "一套西装: a set."),
        M("Which measure word goes with 牙膏?", "筒", ["把", "支", "双"], "一筒牙膏: items in tubes."),
        M("Which measure word goes with 笔记本?", "本", ["条", "把", "筒"], "一本笔记本."),
        M("Which measure word goes with 皮鞋?", "双", ["件", "本", "筒"], "一双皮鞋: pair."),
        M("Which measure word goes with 领带?", "条", ["套", "双", "本"], "一条领带: long dangly objects."),
        M("Which measure word goes with 牙刷?", "把", ["筒", "双", "套"], "一把牙刷: has a handle."),
        M("Which measure word goes with 铅笔?", "支", ["套", "条", "筒"], "一支铅笔: long, thin, inflexible."),
        M("Which measure word goes with 衣服?", "件", ["双", "支", "筒"], "一件衣服: piece of clothing."),
        M("Which measure word goes with 袜子?", "双", ["本", "套", "筒"], "一双袜子: pair."),
        M("Which measure word goes with 毛巾?", "条", ["筒", "本", "套"], "一条毛巾."),
        M("Which is correct: “two tubes of toothpaste”?", "两筒牙膏", ["两条牙膏", "两套牙膏", "两本牙膏"], "牙膏 comes in tubes."),
        M("Which is correct: “three pairs of men’s leather shoes”?", "三双男式皮鞋", ["三条男式皮鞋", "三本男式皮鞋", "三筒男式皮鞋"], "皮鞋: 双."),
        F("一___西装", "套", ["本", "把", "筒"], "西装 is a set."),
        F("四___领带", "条", ["本", "套", "筒"], "领带 is long and dangly."),
        F("两___牙刷", "把", ["筒", "双", "套"], "牙刷 has a handle."),
        F("六___圆珠笔", "支", ["套", "条", "筒"], "圆珠笔 is a long thin pen."),
    ],
)

# ------------------------------------------------------------------ 3. 快...了
KUAI = [("快上课了！", "Class is about to start!"), ("快下雨了！", "It’s about to rain!"), ("快到下课的时间了。", "It’s almost time for class to end."), ("快到集合的时间了。", "It’s almost time to assemble."), ("父亲节快到了。", "Father’s Day is almost here."), ("春节快到了。", "The Spring Festival is almost here.")]
KUAI2 = [("快四点钟了，我弟弟快来了。", "It’s almost four o’clock; my younger brother will be here soon.")]
SIM = [("快开学了", "School is about to start"), ("快要开学了", "School is about to start"), ("就要开学了", "School is about to start"), ("要开学了！", "School is about to start!"), ("就开学了！", "School starts soon!")]
DLG3 = [("你的生日快到了！", "Your birthday is almost here!"), ("你想要什么生日礼物？", "What birthday present do you want?")]
TF = [("他们在说周末的打算。", "They are talking about their weekend plans."), ("大年打算和王丽去吃晚饭。", "Da Nian plans to go to dinner with Wang Li."), ("大年打算周末去买衣服，花很多钱。", "Da Nian plans to buy clothes at the weekend and spend a lot of money."), ("大年没有钱，所以只能在宿舍上网。", "Da Nian has no money, so he can only go online in the dorm.")]
L3 = lesson(
    "Lesson 9 Presentation 3 grammar: the 快…了 construction",
    "快上课了 · 快下雨了 · 春节快到了 · 快要…了 · 就要…了 · 还没…(呢)",
    requires=[],
    cards=[
        card("The 快…了 construction",
             "The 快…了 construction indicates an action is about to take place or that it is almost a certain time. Its negative form is 还没…(呢), meaning an action has yet to take place. No specific time words or phrases may be used to modify the construction. Incorrect: 我弟弟四点钟快来了. Correct: 快四点钟了，我弟弟快来了. Patterns: 快 + Verb Phrase + 了; 快(到) Noun / Noun Phrase 了; Noun / Noun Phrase 快到了. There are a few other constructions similar to 快…了, such as 快要…了, 就要…了, 要…了 and 就…了.",
             examples=[D(z, e) for z, e in KUAI2] + [D(z, e) for z, e in KUAI] + [D(z, e) for z, e in SIM]),
        card("Activity 2 (Speaking and Listening)",
             "Pair up with a partner. Pick one of the images in the book (a birthday, a holiday, and so on; the pictures are not included) and make a sentence about it with the 快…了 pattern. Your partner creates a follow-up sentence or question. Read the example for the first image, then make up your own exchange for the same image, and switch until you have talked about all the images. The book’s example, Student A then Student B:",
             examples=[D(z, e) for z, e in DLG3]),
        card("Activity 3 (Listening, Reading and Speaking)",
             "A. Listen to the dialog and mark the four statements true or false (the dialog is audio, so no key is given here). B. Check your answers with a partner and take turns telling each other the correct versions of each false statement. C. Transcribe and translate three sentences from the dialog into pinyin and English (audio, not included). The statements:",
             examples=[D(z, e) for z, e in TF]),
    ],
    exercises=[
        M("What does the 快…了 construction express?", "An action about to take place, or almost a certain time", ["An action that already happened", "An action that always happens", "A wish"], "快…了: about to / almost."),
        M("What is the negative form of 快…了?", "还没…(呢)", ["不…了", "没有…了", "别…了"], "还没…(呢): has yet to take place."),
        M("What does 快下雨了 mean?", "It’s about to rain", ["It rained yesterday", "It never rains", "I like rain"], "快下雨了！"),
        M("What does 春节快到了 mean?", "The Spring Festival is almost here", ["The Spring Festival is over", "I like the Spring Festival", "Spring is far away"], "快到了: almost here."),
        M("Which sentence is correct?", "快四点钟了，我弟弟快来了。", ["我弟弟四点钟快来了。", "四点钟我弟弟快来了。", "我弟弟快四点钟来了。"], "No specific time word may modify 快…了."),
        M("What does 父亲节快到了 mean?", "Father’s Day is almost here", ["Father’s Day was yesterday", "I’m a father", "Father’s Day is not a holiday"], "父亲节快到了。"),
        M("Which is not similar to 快…了?", "我们昨天去商场了", ["快要开学了", "就要开学了", "要开学了"], "The others mean about to begin."),
        M("What does 快上课了 mean?", "Class is about to start", ["Class is over", "Class is boring", "I skipped class"], "快上课了！"),
        F("___上课了！", "快", PART, "快 + verb phrase + 了."),
        F("春节快到___！", "了", PART, "Noun + 快到了."),
        F("快四点钟了，我弟弟快来___。", "了", PART, "快…了 needs 了."),
        F("快开学了，大卫正准备去商场买___和衣服。", "文具", NOUN, "文具: stationery."),
    ],
)

# ------------------------------------------------------------------ 4. 连...都/也
LIAN = [("这个汉字太难，连我的中文老师都不认识。", "This character is so hard that even my Chinese teacher doesn’t know it."), ("我周末出去玩，连一毛钱都没花。", "I went out to have fun at the weekend and didn’t even spend one mao."), ("这个问题太简单，连三岁小孩都知道。", "This question is so simple that even a three-year-old knows it."), ("这个问题太容易，连三岁小孩都知道。", "This question is so easy that even a three-year-old knows it."), ("她喜欢吃辣，连她的汤都是辣的。", "She likes spicy food; even her soup is spicy.")]
LIAN_DO = [("她很有钱，连飞机都买得起。", "She is rich; she can even afford a plane."), ("大卫什么肉都吃，连蛇肉都吃。", "David eats any kind of meat; he even eats snake."), ("中国人常用手机扫码付费，连买菜都用手机。", "Chinese people often pay by scanning a code on a phone; they even pay for vegetables with their phone."),
           ("他的中文很好，连中国人都听不出来他是美国人。", "His Chinese is very good; even Chinese people can’t tell he is American."), ("我女朋友很喜欢上网买东西，连牙刷都在网上买。", "My girlfriend loves shopping online; she even buys toothbrushes online."), ("我的同学很能睡，连上课都睡。", "My classmate can really sleep; he even sleeps in class.")]
L4 = lesson(
    "Lesson 9 Presentation 3 grammar: the 连…都/也… pattern",
    "连我的老师都不认识 · 连一毛钱都没花 · 连三岁小孩都知道",
    requires=[],
    cards=[
        card("The 连…都/也… pattern",
             "Similar to the English “even”, 连…都/也… emphasizes surprise at something. “Even” in Chinese, however, necessitates both parts of the pattern, for example “I work out every day, even when it rains”: 我每天锻炼，连下雨天都/也去. In Chinese, 都 and 也 are interchangeable in this pattern, although 都 is more common. Patterns: Statement, 连 + Object + 都/也 + Verb; Statement, 连 + Object + 都/也 + 不/没 + Verb. The book’s fifth example is 她的英文很不好，连 hello 这个字都不会说 (Her English is very bad; she can’t even say the word “hello”).",
             examples=[D(z, e) for z, e in LIAN]),
        card("Activity 4 (Reading, Writing, Speaking, Transcribing, Translating)",
             "A. Complete the sentences below with 连…都/也…: 1. 她很有钱, 2. 大卫什么肉都吃, 3. 中国人常用手机扫码付费, 4. 他的中文很好, 5. 我女朋友很喜欢上网买东西, 6. 我的同学很能睡. One possible completion each (mine):",
             examples=[D(z, e) for z, e in LIAN_DO]),
        card("Activity 4B: your own statement",
             "In the first row of the table, write a statement in pinyin about yourself using the 连…都/也… pattern. When your teacher calls on you, read your statement to the class. Your classmates transcribe and translate what you said in the space provided. When everyone has finished, the class decides in Chinese which statement is the most creative or surprising and explains why. (The table has columns Who/Name, Statement/Transcription and Translation, with rows for Myself and S1 to S5.)"),
    ],
    exercises=[
        M("What does 连…都/也… express?", "“Even”: surprise at something", ["“Because”", "“If”", "“Only”"], "Similar to “even”."),
        M("Which words are interchangeable in this pattern?", "都 and 也", ["都 and 就", "也 and 才", "都 and 不"], "都 is more common."),
        M("What does 连一毛钱都没花 mean?", "Didn’t even spend one mao", ["Spent one mao", "Spent a lot", "Will spend one mao"], "连…都没…: not even."),
        M("What does 连三岁小孩都知道 mean?", "Even a three-year-old knows", ["A three-year-old knows nothing", "Only a three-year-old knows", "Three children know"], "连 + noun + 都 + verb."),
        M("What does 她喜欢吃辣，连她的汤都是辣的 mean?", "She likes spicy food; even her soup is spicy", ["Her soup is not spicy", "She dislikes spicy food", "She only eats soup"], "连她的汤都是辣的."),
        M("Which is correct: “Even my teacher doesn’t know it”?", "连我的老师都不认识。", ["我的老师连都不认识。", "连我的老师不认识。", "都连我的老师不认识。"], "连 + object + 都 + 不 + verb."),
        M("Which is correct: “I didn’t even spend one mao”?", "我连一毛钱都没花。", ["我连一毛钱没花都。", "我一毛钱连都没花。", "连我一毛钱花都没。"], "连 + 一毛钱 + 都 + 没 + 花."),
        M("Both parts of the pattern are needed, so which sentence is incomplete?", "连我的老师不认识。", ["连我的老师都不认识。", "连我的老师也不认识。", "连老师都不认识。"], "连 needs 都 or 也."),
        F("这个汉字太难，连我的中文老师___不认识。", "都", PART, "连…都不…"),
        F("我周末出去玩，连一毛钱都___花。", "没", ["吗", "们", "呢"], "没 for a past negative."),
        F("这个问题太简单，___三岁小孩都知道。", "连", PART, "连…都…"),
        F("她喜欢吃辣，连她的汤___是辣的。", "都", PART, "连…都…"),
    ],
)

# ------------------------------------------------------------------ 5. pivotal 请
QING = [("我请你吃饭。", "I invite you to a meal."), ("他请我去看电影。", "He invites me to see a movie."), ("他请我们去他家喝咖啡。", "He invites us to his house for coffee."), ("请你帮他买一杯饮料。", "Please help him buy a drink."), ("请你给我他的手机号码。", "Please give me his cell phone number.")]
NOTE = ["王英：", "明天是我的生日，我想请一些朋友到我们家来吃晚饭，请你告诉小力和大年。我做晚饭，请你们不要买别的东西。好，明天下午见！", "李华", "七月八日"]
L5 = lesson(
    "Lesson 9 Presentation 3 grammar: the pivotal construction 请",
    "我请你吃饭 · 请你帮他买一杯饮料 · 请你给我两条黄毛巾",
    requires=[],
    cards=[
        card("The pivotal construction 请",
             "There are two predicates (verbs) in a pivotal sentence. The object of the first predicate is also the subject of the second. There are a limited number of verbs in Chinese that appear in a pivotal construction. 请 is often used for invitations or polite requests, and in imperative sentences to express a request. For example, in 请您给我两条黄毛巾 there is no subject before the first verb, 请. Instead, 您 is both the object of 请 and the subject of the second verb, 给. Pattern: Subject + Verb 1 + {Subject/Object} + Verb 2 + Object.",
             examples=[D(z, e) for z, e in QING] + [D("请您给我两条黄毛巾。", "Please give me two yellow towels.")]),
        card("Activity 5 (Listening, Speaking and Writing)",
             "A. Listen to a phone conversation and answer: 1. Why did Wang Ying call her teacher, Mr. Li? 2. What is Mr. Li going to do this afternoon? 3. What are they going to do tomorrow? B. Check your answers with a partner in Chinese. C. Listen again and write the sentences that use the pivotal 请 (audio, not included). D. Using the pivotal construction 请, come up with three activities to invite three classmates to do this weekend; they can accept or give a reason for declining. Fill in the table (Who, Activity, Yes/No and why)."),
        card("Activity 6 (Reading and Speaking): the note",
             "A. Read the note Li Hua left for Wang Ying, then summarize it in English in the space provided. B. Share your summary with your partner in Chinese. The book prints the date as 7月8日. A summary (mine): it is Li Hua’s birthday tomorrow and she would like to invite friends for dinner at their home; she asks Wang Ying to tell 小力 and 大年; she will cook and asks them not to buy anything else; see you tomorrow afternoon.",
             examples=[D("王英：", "To Wang Ying:"), D(NOTE[1], "Tomorrow is my birthday. I’d like to invite some friends to our home for dinner; please tell Xiao Li and Da Nian. I’ll make dinner, so please don’t buy anything else. Okay, see you tomorrow afternoon!"), D("李华", "Li Hua"), D("七月八日", "July 8")]),
    ],
    exercises=[
        M("What is a pivotal sentence?", "One where the object of the first verb is the subject of the second", ["One with no verb", "One with three objects", "One with only a subject"], "Two predicates sharing a middle noun."),
        M("In 我请你吃饭, who eats?", "你", ["我", "他", "Nobody"], "你 is the object of 请 and the subject of 吃."),
        M("What does 他请我去看电影 mean?", "He invites me to see a movie", ["I invite him to see a movie", "He sees a movie", "I ask him the time"], "他请我去看电影."),
        M("What does 请你帮他买一杯饮料 mean?", "Please help him buy a drink", ["Please drink for him", "I helped him buy a drink", "He asked me for a drink"], "请你帮他…"),
        M("What does 请你给我他的手机号码 mean?", "Please give me his cell phone number", ["Please call him", "Please give him my number", "Please text me"], "请你给我…"),
        M("In 请您给我两条黄毛巾, what is 您?", "The object of 请 and the subject of 给", ["Only the subject of 请", "Only the object of 给", "A measure word"], "Pivot."),
        M("What is Li Hua’s note about?", "An invitation to dinner for her birthday", ["A shopping list", "A class cancellation", "A farewell"], "明天是我的生日，我想请一些朋友到我们家来吃晚饭。"),
        M("What does Li Hua ask them not to do?", "Buy anything else", ["Come early", "Cook", "Call her"], "请你们不要买别的东西。"),
        M("Who is to be told about the dinner?", "小力 and 大年", ["王英 only", "The teacher", "Nobody"], "请你告诉小力和大年。"),
        M("When will they meet?", "Tomorrow afternoon", ["Tonight", "Next week", "This morning"], "明天下午见！"),
        F("我___你吃饭。", "请", PART, "请: invite."),
        F("他请我们去他家___咖啡。", "喝", ["看", "买", "做"], "喝咖啡: drink coffee."),
        F("请你___他买一杯饮料。", "帮", ["看", "吃", "做"], "帮他买: help him buy."),
        F("我做晚饭，请你们不要买别___东西。", "的", PART, "别的东西: anything else."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
REC = [("0026", "书包", "¥12.00", "1", "¥12.00"), ("0052", "圆珠笔", "¥2.50", "2", "¥5.00"), ("0073", "铅笔", "¥6.80", "1", "¥6.80"), ("0084", "笔记本", "¥1.30", "3", "¥3.90")]
SUN = "昨天是星期天，上午王小军和他的朋友先一起到中山公园去。那儿的风景很美，他们在那儿散了一会儿步，然后到书店去买了几本打折的书。买完书，他们又坐车到王府井百货大楼去买东西了。王小军的学校快开学了，所以他在文具部买了几枝红圆珠笔和一个绿色的笔记本。王小军还在鞋帽部买了一双黑色的皮鞋，又便宜又好看。王小军的朋友，有的买了夹克和领带，有的买了衬衫和裤子。王小军想买一套运动衣，可是没有合适的颜色。中午王小军和朋友们一起到王府井烤鸭店去吃北京烤鸭。下午他们在电影院看了一个电影就坐公共汽车回学校了。他们过了愉快的一天。"
AD = "华星皮鞋二百八十块一双；儿童服装一百块起。休闲运动鞋打九折；男式西裤五百五十块；新式西装七折；女士夹克三折到五折；领带全部打八折。"
SUNTAB = [("上午", "中山公园 · 书店 · 王府井百货大楼", "散步，买打折的书，买文具、黑皮鞋"), ("中午", "王府井烤鸭店", "吃北京烤鸭"), ("下午", "电影院", "看电影，然后坐公共汽车回学校")]
L6 = lesson(
    "Lesson 9 Presentation 3 skill integration: the receipt, the ad and 王小军’s Sunday",
    "新华文具店收据 · 新天地百货大楼 · 王府井 · 先…然后…",
    requires=[],
    cards=[
        card("Activity 1: the receipt",
             "A. Read the receipt, then write four questions about it in Chinese. Ask a partner your questions and check their answers against the receipt. B. Using the information on the receipt, make a few purchases in Chinese while your partner plays the store clerk; switch roles and repeat. 新华文具店收据 (Xinhua stationery store receipt): total ¥27.70, cash ¥30.00, change ¥2.30; address 西长安街 21 号; cashier no. 00432; time 2001/11/25 16:08.",
             tables=[table(["商品代码", "品名", "单价", "数量", "价钱"], REC, say=[1], title="新华文具店收据")]),
        card("Activity 2 (Listening, Speaking, Reading and Writing)",
             "A. Listen to a dialog and answer: 1. What are three things Xiao Ming did yesterday? 2. What are two things Da Hua did yesterday? B. Share your answers in Chinese. C. Role-play the script. D. Guess the meaning of 书店, 字典, 文具店 and 铅笔 from context. E. Listen to a second dialog and answer: 1. What comment does the first speaker make? 2. Does the second speaker agree? Why or why not? F. In Chinese, list the items mentioned and their prices. G. Role-play the dialog. H. Guess the meaning of 夹克 and 皮包 from context (audio, not included).",
             tables=[wtable([("书店", "shu1 dian4", "bookstore"), ("字典", "zi4 dian3", "dictionary"), ("文具店", "wen2 ju4 dian4", "stationery store"), ("铅笔", "qian1 bi3", "pencil"), ("夹克", "jia2 ke4", "jacket"), ("皮包", "pi2 bao1", "leather bag")], title="Words to guess")]),
        card("Activity 3: the department store advertisement",
             "A. Read the advertisement of 新天地百货大楼 (Xin Tiandi Department Store) and write the amount each sale item is discounted under its picture (pictures not included). The book prints the prices in digits (¥280 a pair, ¥100 and up, ¥550, 7折, 3-5折, 80%); they are spelled out here. B. Pair up: listen to Passage 1 while your partner listens to Passage 2 (张英 and 李国华), and fill in your column (when, activities, additional information) (audio, not included). C. Get together with the students who heard your passage and compare in Chinese. D. Pair back up and fill in the other column as you relate your information.",
             examples=[D(AD, "Huaxing leather shoes 280 yuan a pair; children’s clothing from 100 yuan. Casual sneakers 10% off; men’s dress pants 550 yuan; new-style suits 30% off; women’s jackets 50% to 70% off; all ties 20% off.")]),
        card("Activity 4: 王小军’s Sunday",
             "A. Read the passage, then fill in the table in Chinese (星期天, 去哪儿, 做什么 for 上午, 中午, 下午). B. Listen to four statements and decide true or false (audio, not included). C. Write correct versions of the false statements. D. Following a similar format (timeline, locations, activities, additional information), tell your partner what you did last Saturday or Sunday. The table below is my filling-in:",
             examples=[D(SUN, "Yesterday was Sunday. In the morning Wang Xiaojun and his friends first went to Zhongshan Park together. The scenery there is beautiful; they took a stroll for a while, then went to the bookstore and bought a few discounted books. After buying the books, they took a bus to the Wangfujing department store to shop. Wang Xiaojun’s school is about to start, so he bought a few red ballpoint pens and a green notebook in the stationery section. He also bought a pair of black leather shoes in the shoe and hat section, cheap and good-looking. Of his friends, some bought jackets and ties, some shirts and pants. Wang Xiaojun wanted a sports outfit but there was no suitable color. At noon he and his friends went to the Wangfujing roast duck restaurant for Beijing roast duck. In the afternoon they watched a movie at the cinema and then took the bus back to school. They had a happy day.")],
             tables=[table(["星期天", "去哪儿？", "做什么？"], SUNTAB, say=[0], title="王小军的星期天")]),
    ],
    exercises=[
        M("What is the total on the receipt?", "¥27.70", ["¥30.00", "¥2.30", "¥12.00"], "共计: ¥27.70."),
        M("How much change does the customer get?", "¥2.30", ["¥27.70", "¥30.00", "¥5.00"], "找零: ¥2.30."),
        M("How much is one ballpoint pen on the receipt?", "¥2.50", ["¥5.00", "¥6.80", "¥1.30"], "单价 ¥2.50, quantity 2."),
        M("How many notebooks were bought?", "3", ["1", "2", "5"], "数量 3."),
        M("Which item costs ¥6.80?", "铅笔", ["书包", "笔记本", "圆珠笔"], "铅笔 ¥6.80."),
        M("How much off are the ties in the ad?", "Twenty percent", ["Ten percent", "Thirty percent", "Fifty percent"], "领带全部打八折。"),
        M("How much off are the new-style suits?", "Thirty percent", ["Seventy percent", "Ten percent", "Twenty percent"], "新式西装七折: 70% of the price."),
        M("How much off are the casual sneakers?", "Ten percent", ["Twenty percent", "Fifty percent", "Thirty percent"], "休闲运动鞋打九折。"),
        M("Where did 王小军 go first?", "Zhongshan Park", ["The bookstore", "The roast duck restaurant", "The cinema"], "先一起到中山公园去。"),
        M("What did 王小军 buy at the stationery section?", "A few red ballpoint pens and a green notebook", ["Black shoes", "A jacket", "A suit"], "几枝红圆珠笔和一个绿色的笔记本。"),
        M("What did 王小军 want but could not buy?", "A sports outfit in a suitable color", ["Black shoes", "A tie", "A jacket"], "没有合适的颜色。"),
        M("What did they eat at noon?", "Beijing roast duck", ["Dumplings", "Noodles", "Hot pot"], "吃北京烤鸭。"),
        M("How did they get back to school?", "By bus", ["By taxi", "On foot", "By bike"], "坐公共汽车回学校。"),
        mean("书店", "shu1 dian4", "bookstore", ["dictionary", "pencil", "jacket"]),
        mean("夹克", "jia2 ke4", "jacket", ["bookstore", "leather bag", "pencil"]),
        mean("字典", "zi4 dian3", "dictionary", ["bookstore", "jacket", "leather bag"]),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context
FLOOR = [("美食广场", "8F food court"), ("儿童及婴儿孕妇装", "7F children’s, infants’ and maternity wear"), ("床具家电文具", "6F bedding, appliances, stationery"), ("男式服饰男式鞋包", "5F men’s apparel, men’s shoes and bags"), ("流行女装内睡衣配饰", "4F fashionable women’s wear, underwear and sleepwear, accessories")]
STORES = [("爱买", "FE Amart (fe-amart.com.tw)"), ("大润发", "RT-Mart (news.rt-mart.com.tw)"), ("好市多", "Costco (www.costco.com.tw)"), ("家乐福", "Carrefour (www.carrefour.com.tw)")]
L7 = lesson(
    "Lesson 9 Presentation 3 using Chinese in context",
    "楼层指南 · 杀价 · 重要 · 台北的商店",
    requires=[],
    cards=[
        card("Activity 1: a VOA report (video)",
             "You are a journalist at the Xinhua News Agency (新华社) Washington DC (华盛顿特区) bureau; your bureau chief asks you to write a report on a VOA (美国之音) news item titled 《奥巴马总统逛商店为妻女买衣服》 (VOA, 0:05 to 0:40). A. Watch the video and take notes on the key details. B. Discuss with your American colleague (a partner): 1. Where was President Obama and what was he doing? 2. What did he do for his two daughters? 3. What was his original plan for his wife, and what does he end up doing? C. Write your report in Chinese. (The video is not included.)",
             examples=[D("奥巴马总统逛商店为妻女买衣服", "President Obama goes shopping for clothes for his wife and daughters")]),
        card("Activity 2: the floor directory (楼层指南) of the Xin Guang department store",
             "A. Pair up and read the floor directory; discuss what is sold on each floor, based on the vocabulary and characters you have learned. B. Listen to a conversation about David’s shopping trip to Xin Guang, arrange the departments he visited in order, and fill in the information about his purchases (audio, not included). C. Based on the table, recount David’s shopping trip using such transitional patterns as 先…然后…最后 and 因为…所以….",
             tables=[wtable(rows_py(FLOOR), title="楼层指南")]),
        card("Activity 3: question strips",
             "A. Form groups of three. With the question strips face down, take turns picking a strip from the stack and translating the question into Chinese to ask the group. B. Each group shares some highlights about each other with the class in Chinese. The strips: Do you like shopping? Why or why not? · Do you bargain (杀价 shā jià) when you shop? If so, when and where? · Do you check out ads before shopping? Do you prefer to shop during sales? Why or why not? · How much money do you usually spend a day, week and month? · Do you buy things you don’t need? If so, what? · Do you prefer to shop online or at stores? · Where do you prefer to buy your fruits and vegetables and why? · How much do you usually spend on presents? · What is more important (重要 zhòngyào) to you: price, quality or style? · Do you try on clothes before buying them? How do you like your clothes to fit and why? · Do you like to shop at small or large venues? · Do you prefer to wear the latest fashions? Why or why not? · What would you like to buy but can’t afford? · What is your favorite store and why?"),
        card("Activity 4: stores in Taipei",
             "Pair up. You are now studying in Taipei and you need to buy some stationery, daily necessities and clothes. Check the online ads of several local stores and select the two stores with the most variety and best prices (the web pages are not included). A. In Chinese, decide what you will buy and write a list of which items you will buy at which store (a table with Store and Items to Buy). B. Based on your research and list, create a PPT shopping guide and present it to the class in Chinese.",
             tables=[wtable(rows_py(STORES), title="Four stores in Taiwan")]),
    ],
    exercises=[
        M("What does 楼层指南 mean?", "Floor directory", ["Shopping list", "Receipt", "Price tag"], "楼层 floors, 指南 guide."),
        M("What is sold on the 8th floor of Xin Guang?", "A food court", ["Shoes", "Stationery", "Bedding"], "8F 美食广场."),
        M("Which floor has men’s apparel and men’s shoes and bags?", "5F", ["7F", "4F", "8F"], "5F 男式服饰/男式鞋包."),
        M("Which floor has children’s and infants’ wear?", "7F", ["5F", "4F", "6F"], "7F 儿童及婴儿/孕妇装."),
        M("Which floor sells stationery?", "6F", ["8F", "7F", "5F"], "6F 床具/家电/文具."),
        M("What does 杀价 mean?", "To bargain", ["To pay", "To weigh", "To count"], "Do you bargain (杀价)?"),
        M("What does 重要 mean?", "Important", ["Heavy", "Cheap", "Fresh"], "What is more important (重要)?"),
        M("Which is the Chinese name of Costco in Taiwan?", "好市多", ["家乐福", "大润发", "爱买"], "好市多: www.costco.com.tw."),
        M("Which is the Chinese name of Carrefour in Taiwan?", "家乐福", ["好市多", "大润发", "爱买"], "家乐福: www.carrefour.com.tw."),
        mean("楼层指南", "lou2 ceng2 zhi3 nan2", "floor directory", ["receipt", "price tag", "shopping list"]),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 9 Presentation 3 vocabulary", "34 words: 上网 书包 付账 促销 信用卡 准备 名牌 商场 圆珠笔 大餐 套 帮 开学 快 文具 方便 最后 条 正好 毛巾 牙刷 现金 皮鞋 种类 笔记本 网上 网 花 衬衫 袜子 西装 选购 领带 黑",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 9. Area Studies
EC = [("天猫商城", "Tmall Mall"), ("淘宝", "Taobao"), ("京东商城", "Jingdong Mall"), ("拼多多", "Pinduoduo"), ("苏宁易购", "Suning Tesco")]
PAY = [("贝宝", "PayPal"), ("支付宝", "Alipay"), ("财付通", "Tenpay")]
EXP = [("顺丰速运", "SF Express"), ("邮政", "Postal EMS"), ("圆通速递", "YTO Express")]
L9 = lesson(
    "Lesson 9 Area Studies: China’s booming consumer economy",
    "天猫商城 淘宝 京东商城 拼多多 · 支付宝 · 顺丰速运",
    requires=[],
    cards=[
        card("China’s booming consumer economy (1)",
             "Since the late 1970s, China has transitioned from a closed, centrally planned economy to a market-based global giant. Reform began with the phaseout of collectivized agriculture and soon extended to price liberalization, fiscal decentralization, increased state-owned enterprise (SOE) autonomy, private sector growth, stock market development, modern banking practices, and opening up to foreign trade and investment. From 1978 to 2019, China has seen an average GDP growth rate of 9.3% annually. In 2019, its GDP was $27,307 trillion (as printed in the book), second only to the US; its per capita income was $19,504 in Purchasing Power Parity (PPP); and it became the world’s leading exporter, with exports valued at $2.5 billion (as printed in the book), the US coming in a distant second at only $1.6 billion. China’s robust economy and rising standard of living are promoting an ardent consumer lifestyle. According to the McKinsey China Report, the scale of China’s e-commerce ranks first in the world, reaching $1.5 trillion in 2019. (The book’s photographs, from People.com.cn, are not included.)"),
        card("E-commerce and online payment",
             "Today, the top five e-commerce retailers in China are Tmall Mall (天猫商城 tiānmāo shāngchéng), Taobao (淘宝 táobǎo), Jingdong Mall (京东商城 Jīngdōng shāngchéng), Pinduoduo (拼多多 pīn duōduō) and Suning Tesco (苏宁易购 Sūníng Yìgòu), which supply almost everything Chinese consumers need. Due to the prosperous e-commerce market, online payment and express delivery systems are also flourishing. The top three online pay apps are PayPal (贝宝 bèibǎo), Alipay (支付宝 zhīfùbǎo) and Tenpay (财付通 cáifùtōng). Almost everyone now pays for their purchases by phone; even in remote rural areas, cash is rarely used anymore.",
             tables=[wtable(rows_py(EC), title="Top five e-commerce retailers"), wtable(rows_py(PAY), title="Top three online pay apps")]),
        card("Express delivery",
             "Among the burgeoning express delivery services, the top three are SF Express (顺丰速运 shùnfēng sùyùn), Postal EMS (邮政 EMS yóuzhèng EMS) and YTO Express (圆通速递 yuántōng sùdì). SF Express has more than 15,000 vehicles and 13,000 service centers across the country. The company earned a revenue of $8.6 billion in 2016 and began trading publicly in January 2017. Wang Wei, Chairman of SF Express, has become one of the richest men in China, with a net worth of $21.4 billion. Nonetheless, it is not the entrepreneurs or CEOs that bring the nearly 100 million packages to Chinese doorsteps. Enabling these soaring revenues is the labor of over two million scooter couriers who make deliveries 24 hours a day; these workers delivered a total of 60 billion parcels in 2019, according to data from the State Post Bureau (SPB). China’s delivery services now boast 20,000 enterprises and over three million employees. SPB data shows that over 30,000 delivery outlets now cover 96% of townships in China. In short, China’s consumer market and service industries are surging in the wake of its ongoing economic expansion.",
             tables=[wtable(rows_py(EXP), title="Top three express delivery services")]),
    ],
    exercises=[
        M("What was China’s average annual GDP growth rate from 1978 to 2019?", "9.3%", ["3.3%", "19.3%", "0.9%"], "Average GDP growth rate of 9.3% annually."),
        M("According to the McKinsey China Report, where does China’s e-commerce rank?", "First in the world", ["Second in the world", "Tenth", "Last"], "The scale of China’s e-commerce ranks first in the world."),
        M("How large was China’s e-commerce in 2019?", "$1.5 trillion", ["$1.5 million", "$15 billion", "$27 billion"], "Reaching $1.5 trillion in 2019."),
        M("Which is one of the top five e-commerce retailers?", "淘宝", ["贝宝", "财付通", "顺丰速运"], "淘宝 (Taobao)."),
        M("Which is an online pay app?", "支付宝", ["天猫商城", "拼多多", "圆通速递"], "支付宝 (Alipay)."),
        M("Which is an express delivery service?", "顺丰速运", ["支付宝", "淘宝", "财付通"], "顺丰速运 (SF Express)."),
        M("How do almost everyone in China pay now?", "By phone", ["In cash", "By check", "By credit card only"], "Even in remote rural areas, cash is rarely used anymore."),
        M("How many parcels did couriers deliver in 2019?", "60 billion", ["60 million", "6 billion", "100 million"], "A total of 60 billion parcels in 2019."),
        M("What share of townships do the delivery outlets cover?", "96%", ["69%", "16%", "50%"], "Over 30,000 delivery outlets cover 96% of townships."),
        M("Who does the book say actually brings the packages to doorsteps?", "Over two million scooter couriers", ["The CEOs", "The entrepreneurs", "The post office only"], "The labor of over two million scooter couriers."),
        mean("天猫商城", "tian1 mao1 shang1 cheng2", "Tmall Mall", ["Alipay", "SF Express", "Pinduoduo"]),
        mean("支付宝", "zhi1 fu4 bao3", "Alipay", ["Tmall Mall", "SF Express", "Taobao"]),
        mean("顺丰速运", "shun4 feng1 su4 yun4", "SF Express", ["Alipay", "Taobao", "Tenpay"]),
    ],
)

UNIT = unit("第九课 买东西 Presentation 3: shopping online, and Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
