"""Unit 28: Lesson 10 (Housing and Rentals) Presentation 1, from the book's texts: the phone call to rent an apartment, the modal verb 要,
the adverb 多, (不但)...而且..., the Monterey apartment passage, the rental ads and the vocabulary list.
Audio, pictures and videos are not included; the lessons say so."""
from zh_auto import *
from zh_l10_vocab import VOC1

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [
    ("大卫", "你好！是士林公寓吗？", "Hello! Is this Shilin Apartments?"),
    ("张经理", "是。您好，您要租房吗？", "Yes. Hello, do you want to rent a place?"),
    ("大卫", "对，我想租一套两室一厅的公寓。你们有没有？", "Yes, I’d like to rent a two-bedroom, one-living-room apartment. Do you have one?"),
    ("张经理", "有，您想马上租吗？", "Yes. Do you want to rent right away?"),
    ("大卫", "想。房租每月多少钱？都包什么？", "Yes. How much is the rent per month? What does it include?"),
    ("张经理", "房租每月三千元，包水费和网费，不包电费。", "The rent is 3,000 yuan a month, including water and internet fees, not electricity."),
    ("大卫", "客厅有多大？带不带家具？", "How big is the living room? Does it come with furniture?"),
    ("张经理", "客厅很大，差不多三十平米。带家具，而且都是新的。", "The living room is big, about 30 square meters. It comes with furniture, and it’s all new."),
    ("大卫", "租房以前，需要付押金吗？", "Before renting, do I need to pay a deposit?"),
    ("张经理", "要付一个月的押金。", "You need to pay a month’s deposit."),
    ("大卫", "你们有没有停车位？", "Do you have parking spaces?"),
    ("张经理", "有，每个公寓都有一个停车位。", "Yes, every apartment has one parking space."),
    ("大卫", "我可以先看一下房吗？", "May I look at the place first?"),
    ("张经理", "当然可以。明天早上十点，行吗？", "Of course. Tomorrow morning at ten, okay?"),
    ("大卫", "行。明天见。", "Okay. See you tomorrow."),
]
Q2 = [("租房还是买房？", "Rent or buy?"), ("几室几厅？", "How many bedrooms and living rooms?"), ("月租多少钱？能便宜吗？", "How much is the monthly rent? Can it be cheaper?"), ("包什么费，不包什么费？", "Which fees are included, which are not?"),
      ("带不带家具？", "Does it come with furniture?"), ("客厅有多大？", "How big is the living room?"), ("有没有停车位？多少钱？", "Is there a parking space? How much?"), ("需要付多少押金？", "How much deposit must be paid?")]
L1 = lesson(
    "Lesson 10 Presentation 1: renting an apartment on the phone (dialog)",
    "是士林公寓吗？ · 房租每月多少钱？ · 客厅有多大？ · 要付一个月的押金",
    requires=[],
    cards=[
        card("Lesson 10 objectives: 第十课 租房和住房 (Housing and Rentals)",
             "By the end of the lesson you will be able to seek rental information, tour an apartment or house, and describe an apartment or house and its furnishings. To do that you must master the core vocabulary and grammar patterns: the modal verb 要; questions with the adverb 多 (有多大？); the (不但)…, 而且… construction; attributives; the 小是小了点, 可是… construction; existential sentences with 有; the question word 什么时候; the conditional construction 如果…, 就…; the position words 左边, 右边, 旁边, 中间, 前面, 对面, 里面; and the aspect marker 着. Area Studies: living environment and housing conditions in China."),
        card("Getting Started",
             "Pair up and discuss. A. Are you living on post or renting an apartment? B. If you have friends who rent, where did they find their rental information? C. If you would like to rent an apartment, what sort of accommodations would you seek?"),
        card("Presentation 1: 大卫 calls 士林公寓",
             "The book also prints the dialog in traditional characters (for example 是。您好，您要租房嗎？). The book writes the rent as 3,000 and the area as 30, and the time as 10 o’clock; they are spelled out here.",
             examples=dlg(P1)),
        card("Activity 1 (Listening and Speaking)",
             "A. Listen to Presentation 1 and answer: 1. What is going on in this conversation? 2. What is the relationship between the two speakers? B. Listen again and answer: 1. Why does the first speaker call? 2. How much is the rent? Does it include utilities? 3. How big is the living room? 4. What needs to be paid first and how much? 5. What does the first speaker request at the end? C. In Chinese, compare answers with a partner, then share them with the class. D. Share your rental experiences with your partner in Chinese. From the text: a tenant calls the apartment manager; he calls to rent a two-bedroom, one-living-room apartment; the rent is 3,000 yuan a month, with water and internet included and electricity not; the living room is about 30 square meters; a month’s deposit; he asks to see the apartment first."),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Listen to two dialogs and answer the questions below for each (audio, not included). B. Share your answers with a partner. C. Perform both dialogs with your partner, switching roles after each. The questions for Dialog 1 are the first four; for Dialog 2 the last four:",
             examples=[D(z, e) for z, e in Q2]),
    ],
    exercises=[
        M("What kind of apartment does 大卫 want?", "Two bedrooms and one living room", ["One room", "Three bedrooms", "A house"], "两室一厅."),
        M("How much is the monthly rent?", "3,000 yuan", ["300 yuan", "30 yuan", "13,000 yuan"], "房租每月三千元。"),
        M("Which fees are included?", "Water and internet", ["Electricity and water", "Electricity only", "Nothing"], "包水费和网费，不包电费。"),
        M("Which fee is not included?", "Electricity", ["Water", "Internet", "Parking"], "不包电费。"),
        M("About how big is the living room?", "30 square meters", ["3 square meters", "300 square meters", "13 square meters"], "差不多三十平米。"),
        M("Does the apartment come with furniture?", "Yes, and it is all new", ["Yes, but it is old", "No", "Only a bed"], "带家具，而且都是新的。"),
        M("How much deposit must be paid?", "One month’s", ["Two months’", "None", "Half a month’s"], "要付一个月的押金。"),
        M("How many parking spaces does each apartment have?", "One", ["Two", "None", "Three"], "每个公寓都有一个停车位。"),
        M("When will 大卫 look at the apartment?", "Tomorrow at ten in the morning", ["Right now", "Tomorrow at ten in the evening", "Next week"], "明天早上十点。"),
        M("What does 租房 mean?", "To rent housing", ["To buy a house", "To sell a house", "To clean a house"], "租房 is a verb-object phrase."),
        M("What does 您要租房吗？ ask?", "Do you want to rent a place?", ["Do you want to buy a place?", "Do you have a place?", "Where do you live?"], "要: want to."),
        M("Which question asks about the size of the living room?", "客厅有多大？", ["客厅有多少？", "客厅在哪儿？", "客厅贵不贵？"], "多大: how big."),
        F("房租每月多少钱？都___什么？", "包", PART, "包: include."),
        F("客厅很大，差不多三十___米。", "平", PART, "平米: square meter."),
        F("我想租一套两___一厅的公寓。", "室", PART, "两室一厅: two rooms and a living room."),
        F("租房以前，需要付___金吗？", "押", PART, "押金: deposit."),
    ],
)

# ------------------------------------------------------------------ 2. modal verb 要
YAO1 = [("我要租一套公寓。", "I want to rent an apartment."), ("我现在有点儿累，不想写作业。", "I’m a little tired now and don’t want to do homework."), ("我要去海边散步，你要不要和我一起去？", "I want to go to the beach for a stroll. Do you want to go with me?")]
YAO2 = [("我要买一条领带。", "I want to buy a tie."), ("我想买一条领带。", "I would like to buy a tie."), ("我要去看电影。", "I want to go see a movie."), ("我想去看电影。", "I’d like to go see a movie.")]
YAO3 = [("甲：租房以前，要付押金吗？", "Before renting, do I need to pay a deposit?"), ("乙：你不用付押金，只付一个月的房费就可以了。", "You don’t need to pay a deposit; you can just pay a month’s rent."), ("甲：今天我们要锻炼身体吗？", "Do we need to work out today?"), ("乙：不用，今天你们很忙，明天再锻炼吧。", "No, you’re very busy today; you can work out tomorrow.")]
YAO4 = [("租房以前，需要付押金吗？", "Before renting, do I need to pay a deposit?"), ("租房以前，要付押金吗？", "Before renting, do I need to pay a deposit?"), ("我不需要租公寓，我可以住在学校宿舍。", "I don’t need to rent an apartment; I can live in the school dormitory."), ("我不用租公寓，我可以住在学校宿舍。", "I don’t need to rent an apartment; I can live in the school dormitory.")]
ACT1 = [("我要去农贸市场买水果，你要不要也去买一些？", "I want to go to the farmers’ market to buy fruit; do you want to go and buy some too?"), ("我不想去，我家里还有很多水果。", "I don’t want to; I still have a lot of fruit at home.")]
ACT1E = ["Do you want to rent or buy a place?", "What kind of apartment would you like to rent?", "Do you want to go to the movies with me tonight?", "Would you like to teach English in China?", "Do you know, before renting, is a deposit needed?", "Do we have to go to the library to do homework every day?"]
ACT1Q = ["你要租房还是买房？", "你想租什么样的公寓？", "今天晚上，你要不要和我一起去看电影？", "你想在中国教英文吗？", "你知道，租房以前，需要付押金吗？", "我们每天要去图书馆做作业吗？"]
L2 = lesson(
    "Lesson 10 Presentation 1 grammar: the modal verb 要 (want, need)",
    "我要租公寓 · 不想 · 要不要 · 要 vs 想 · 不用 · 需要",
    requires=[],
    cards=[
        card("Activity 3 (Reading, Writing, Speaking and Listening) and Activity 4",
             "Activity 3. A. Pair up and write five sentences using the words from the picture of a house (套, 停车位, 公寓, 多大, 租, 租房, 房租, 押金, 而且, 包, 带, 看房, 付, 想, 要, 有, 水费, 网费, 电费, 每月, 客厅, 家具, 新的, 以前, 一室一厅). Use each word at least once and add any others you need, paying close attention to sentence structure and grammar. B. Take turns reading your sentences to the class. C. Your teacher and classmates point out errors and give feedback. Activity 4 (Speaking): pair up and call a rental agency to ask about housing in your area (rent, security deposit, utilities, facilities, furniture and so on); your partner plays the agent. Use the words and patterns of this lesson."),
        card("The modal verb 要 for desire or intention",
             "The modal 要 + Verb expresses the desire or intention to do something. The negative form is 不想 + Verb, although some speakers in southern China use 不要 + Verb. The affirmative-negative question form is 要不要 + Verb. Patterns: 要 + Verb; 不想 (不要) + Verb; 要不要 + Verb?",
             examples=[D(z, e) for z, e in YAO1]),
        card("要 and 想",
             "Both 要 and 想 can express desire or intention, although 要 is stronger in tone. 想 is often used as a modal verb to mean “would like to” or “feel like doing”. Pattern: 要/想 + Verb.",
             examples=[D(z, e) for z, e in YAO2]),
        card("要 for need, and 需要",
             "要 can also convey the need to do something. In that case the negation is 不用. Pattern: 要 + Verb; 不用 + Verb. When 要 expresses “need to”, 需要 can replace it without a significant change in meaning: 需要(要) + Verb; 不需要(不用) + Verb.",
             examples=[D(z, e) for z, e in YAO3] + [D(z, e) for z, e in YAO4]),
        card("Activities 1 and 2 (Reading and Speaking)",
             "Activity 1. In pairs, take turns asking and answering. The example: A asks about the farmers’ market, B answers. Then ask and answer the six questions: 你要租房还是买房？ 你想租什么样的公寓？ 今天晚上，你要不要和我一起去看电影？ 你想在中国教英文吗？ 你知道，租房以前，需要付押金吗？ 我们每天要去图书馆做作业吗？ Activity 2 (Speaking): you and your partner will begin sharing an apartment next week; discuss what you need to buy for it, using 要, 想 and 需要.",
             examples=[D(z, e) for z, e in ACT1] + [D(q, e) for q, e in zip(ACT1Q, ACT1E)]),
    ],
    exercises=[
        M("What does 我要租一套公寓 mean?", "I want to rent an apartment", ["I rented an apartment", "I have an apartment", "I need an apartment’s key"], "要 + verb: want to."),
        M("What is the negative of 要 for desire?", "不想", ["不用", "没有", "别"], "不想 + verb (some southern speakers say 不要)."),
        M("What is the affirmative-negative question form of 要?", "要不要 + verb", ["要吗不 + verb", "不要要 + verb", "要要 + verb"], "要不要 + verb?"),
        M("Which is stronger in tone: 要 or 想?", "要", ["想", "They are equal", "不想"], "要 is stronger."),
        M("What does 想 mean as a modal verb?", "Would like to; feel like doing", ["Must", "Have to", "Can"], "想 + verb."),
        M("What is the negation of 要 meaning “need to”?", "不用", ["不想", "不能", "没有"], "要 + verb → 不用 + verb."),
        M("Which can replace 要 meaning “need to”?", "需要", ["想要", "不要", "很要"], "需要(要) + verb."),
        M("What does 你不用付押金 mean?", "You don’t need to pay a deposit", ["You can’t pay a deposit", "You must pay a deposit", "You paid a deposit"], "不用: don’t need to."),
        M("What does 我不需要租公寓 mean?", "I don’t need to rent an apartment", ["I don’t want an apartment", "I can’t rent an apartment", "I rented an apartment"], "不需要: don’t need."),
        M("Which sentence asks “Do you want to go with me?”", "你要不要和我一起去？", ["你要不用和我一起去？", "你不想要和我一起去？", "你去要不要？"], "要不要 + verb."),
        F("我现在有点儿累，___想写作业。", "不", ["吗", "们", "呢"], "不想 + verb: don’t want to."),
        F("租房以前，___要付押金吗？", "需", PART, "需要: need to."),
        F("今天你们很忙，明天再锻炼吧。——___，今天你们很忙。", "不用", ["没有", "不是", "不会"], "不用: no need."),
        F("我要去看电影，你要___要和我一起去？", "不", ["吗", "们", "呢"], "要不要: do you want to."),
    ],
)

# ------------------------------------------------------------------ 3. the adverb 多 and (不但)...而且...
DUO = [("你公寓的客厅有多大？", "How large is the living room in your apartment?"), ("你公寓的客厅多大？", "How large is the living room in your apartment?"), ("你儿子现在有多高？", "How tall is your son now?"), ("你儿子现在多高？", "How tall is your son now?"), ("今天的天气有多热？", "How hot is the weather today?"), ("今天的天气多热？", "How hot is the weather today?")]
DUOQ = [("马克有一米八十二。", "珍尼 sample: Mark is 1.82 m tall.", "马克有多高？"), ]
DUO_K = [("珍妮的卧室有三十平米。", "珍妮的卧室有多大？", "Jenny’s bedroom is 30 square meters: How big is Jenny’s bedroom? (the book’s example)"), ("马克有一米八二。", "马克有多高？", "Mark is 1.82 m: How tall is Mark?"), ("张老师的女儿今年三岁。", "张老师的女儿今年多大？", "Teacher Zhang’s daughter is three this year: How old is she?"), ("这种水果四十块一斤。", "这种水果多少钱一斤？", "This fruit is 40 yuan a jin: How much a jin?"), ("今天的气温是一百零三华氏度。", "今天的气温有多高？", "Today it is 103 °F: How high is today’s temperature?"), ("昨天晚上的气温有零下二十摄氏度。", "昨天晚上的气温有多低？", "Last night it was minus 20 °C: How low was last night’s temperature?"), ("琳达每天都是十二点才睡觉。", "琳达每天都是几点才睡觉？", "Linda only goes to bed at twelve every day: What time does she go to bed?")]
BD1 = [("上海不但有很多好吃的饭馆，而且还有很多好玩的地方。", "Shanghai not only has many restaurants with good food, but also has many fun places."), ("这件衬衫不但颜色好，而且也很便宜。", "This shirt not only has a nice color, it is also very cheap.")]
BD2 = [("你租的公寓带家具，而且都是新的。", "The apartment you have rented comes furnished, and (moreover) it’s all new."), ("这道菜很好吃，而且很好看。", "This dish is really tasty; (furthermore) it looks very nice, as well.")]
BD3 = [("甲：这个公寓不但颜色好，", "This apartment not only has a nice color,"), ("乙：而且样式很特别。", "but also has a very special style.")]
BDQ = [("这个饺子不但好吃，而且很便宜。", "These dumplings are not only tasty, but also cheap."), ("这个图书馆不但很大，而且很安静。", "This library is not only big, but also quiet."), ("这套西装不但样式好，而且很便宜。", "This suit not only has a nice style, but is also cheap."), ("这个西瓜不但很大，而且很甜。", "This watermelon is not only big, but also sweet."), ("这个客厅不但很大，而且很干净。", "This living room is not only big, but also clean."), ("这些海鲜不但很新鲜，而且很便宜。", "This seafood is not only fresh, but also cheap.")]
L3 = lesson(
    "Lesson 10 Presentation 1 grammar: 有多大？ and (不但)…，而且…",
    "客厅有多大？ · 你儿子多高？ · 不但…，而且… · 带家具，而且都是新的",
    requires=[],
    cards=[
        card("The adverb 多",
             "The adverb 多 is usually placed before monosyllabic (single-syllable) adjectives to inquire about degree or extent. 有 can precede 多 to indicate an estimation. Pattern: (有)多 + Adjective?",
             examples=[D(z, e) for z, e in DUO]),
        card("Activity 3 (Reading and Writing)",
             "Work in pairs. Using the (有)多 + Adjective pattern, write the questions you need to ask to get the measurements underlined in the following sentences. The book’s example: 珍妮的卧室有三十平米 → 珍妮的卧室有多大？ The sentences are 1. 马克有一米八二 2. 张老师的女儿今年三岁 3. 这种水果四十块一斤 4. 今天的气温是一百零三华氏度 5. 昨天晚上的气温有零下二十摄氏度 6. 琳达每天都是十二点才睡觉. The book gives no key; the questions below are mine:",
             tables=[table(["Sentence", "Question", "English"], [(a, b, c) for a, b, c in DUO_K], say=[0, 1], title="The sentences and their questions")]),
        card("The construction (不但)…，而且…",
             "Similar to the English construction “not only…, but also…”, 不但…，而且… joins two phrases or clauses to emphasize their correlation. Used alone, 而且 can function as a conjunction to convey “moreover” or “furthermore”.",
             examples=[D(z, e) for z, e in BD1] + [D(z, e) for z, e in BD2]),
        card("Activities 4 and 5",
             "Activity 4 (Listening): listen to five statements and answer: 1. What is said about the apartment rent? 2. How is the clothing described? 3. How is the parents’ house described? 4. Describe the oranges sold in this store. 5. How is the weather described? (audio, not included). Activity 5 (Speaking and Writing): with a partner, use 不但…，而且… to describe pictures (the pictures are not included). Student A starts each sentence with 不但 and Student B finishes it with 而且. The book’s example for the apartment picture, and then one possible sentence each for 饺子, 图书馆, 西装, 西瓜, 客厅 and 海鲜 (mine):",
             examples=[D(z, e) for z, e in BD3] + [D(z, e) for z, e in BDQ]),
    ],
    exercises=[
        M("Where is 多 placed in 客厅有多大？", "Before a single-syllable adjective", ["After the noun", "Before the subject", "At the end"], "(有)多 + adjective."),
        M("What does 你儿子现在多高？ ask?", "How tall is your son now?", ["How old is your son?", "Where is your son?", "Is your son tall?"], "多高: how tall."),
        M("What does 今天的天气有多热？ ask?", "How hot is the weather today?", ["Is it hot today?", "What is today’s date?", "Will it rain?"], "有多热: how hot."),
        M("What does 有 add in (有)多 + adjective?", "An estimation", ["A negative", "A past tense", "A command"], "有 can precede 多 to indicate an estimation."),
        M("Which question asks for someone’s age?", "他今年多大？", ["他今年多高？", "他今年多重？", "他今年多远？"], "多大 can ask age."),
        M("What does 不但…，而且… mean?", "Not only…, but also…", ["Because…, so…", "If…, then…", "Although…, but…"], "不但…，而且…"),
        M("What does 而且 mean when used alone?", "Moreover; furthermore", ["Therefore", "However", "Whether"], "…，而且…"),
        M("What does 带家具，而且都是新的 mean?", "It comes furnished, and moreover it’s all new", ["It has no furniture", "It is old but cheap", "It is furnished but small"], "而且: moreover."),
        M("Which sentence is a correct 不但…，而且… sentence?", "这件衬衫不但颜色好，而且也很便宜。", ["这件衬衫不但颜色好，但是很便宜。", "这件衬衫因为颜色好，而且很便宜。", "这件衬衫如果颜色好，而且很便宜。"], "不但…，而且…"),
        F("你公寓的客厅有___大？", "多", PART, "有多大: how big."),
        F("这道菜很好吃，___很好看。", "而且", ["所以", "但是", "可是"], "而且: furthermore."),
        F("这个公寓不但颜色好，___样式很特别。", "而且", ["所以", "但是", "可是"], "不但…，而且…"),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
PASS_A = "我刚来蒙特雷的第一个月是住在我的老同学家里。他比我早来蒙特雷两年，所以我请他帮我看看有没有合适的公寓出租。蒙特雷的房租很贵，他找了很长时间都没有找到合适的公寓。最后在网上看到了一个两室一厅的小公寓，每个月的房租只要一千八，包上网费，不包水电，而且交通很方便，开二十分钟的车就可以到学校了。他马上给出租公寓的王经理打电话问了一下。王经理说这个公寓是新公寓，去年建的，环境很美，客厅很大，还带一些家具，有一个停车位。租房以前，要付一个月的房租和一个月的押金。我觉得这个公寓很合适，明天要去看一下。"
PASS_E = "I stayed at an old classmate’s home during my first month in Monterey. He came to Monterey two years before me, so I asked him to help me see if there was a suitable apartment for rent. Rents in Monterey are expensive, and he looked for a long time without finding a suitable apartment. Finally he saw a small two-bedroom, one-living-room apartment online; the monthly rent is only 1,800, including internet but not water and electricity, and the transportation is very convenient: it’s a twenty-minute drive to school. He immediately phoned Manager Wang, who rents out the apartment. Manager Wang said it is a new apartment, built last year, with a beautiful environment and a big living room, some furniture, and one parking space. Before renting, you must pay a month’s rent and a month’s deposit. I think this apartment is very suitable and plan to go and see it tomorrow."
AD3 = "本套房位于中山大学旁，海鲜酒家后的阳光小区一楼。套房为三房两厅一厨两卫，房间配有全套家具：沙发，餐桌，大床；还提供：厨房用具，冰箱，热水器，洗衣机等生活必需品，套房还有电视，且每个房间都配有空调。您只需拎包即可入住。租金实惠，欢迎来电咨询。联系人：李先生"
AD3E = "This suite is next to Sun Yat-sen University, on the first floor of the Sunshine residential community behind the Seafood Restaurant. The suite has three bedrooms, two living rooms, one kitchen and two bathrooms, with a full set of furniture in the rooms: sofa, dining table, big bed. Also provided: kitchen utensils, refrigerator, water heater, washing machine and other daily necessities. The suite also has Wi-Fi and TV, and every room has air conditioning. You only need to bring your bags and move in. The rent is reasonable; calls for inquiries are welcome. Contact: Mr. Li (the phone number is in the book)."
L4 = lesson(
    "Lesson 10 Presentation 1 skill integration: the Monterey apartment, ads and moving in",
    "老同学帮我找公寓 · 钥匙 搬家 · 公寓出租 · 独立屋出租 · 拎包入住",
    requires=[],
    cards=[
        card("Activity 1: a monolog and the passage",
             "A. Listen to the monolog and summarize it, including at least three EEIs (essential elements of information) (audio, not included). B. Read the passage and answer: 1. Why is the speaker’s former classmate having a hard time finding an apartment? 2. According to the speaker, what advantages does the apartment have? 3. According to the manager, what advantages does the apartment have? 4. What does the speaker need to pay before renting? C. Compare answers with a partner. D. In Chinese, discuss where you would most like to live in Monterey, and report your choice and reasoning to the class. (The book prints the rent as 一千八.)",
             examples=[D(PASS_A, PASS_E)]),
        card("Activity 2: a video clip",
             "New words (生词): 钥匙 key; 搬家 move (residence); 赶鸭子上架 push someone beyond their ability (idiom). A. Watch a video clip and summarize it, taking notes on what you understand. B. Watch it again and answer: 1. Why does the speaker say “Today is a very important day”? 2. Does he need to buy any furniture? How do you know? 3. What else does he need to do after he moves in? C. Compare answers with a partner. D. In Chinese, pair up and share your experiences of finding or moving into an apartment or house, on campus or on post. (The video is not included.)",
             tables=[wtable([("钥匙", "yao4 shi5", "key"), ("搬家", "ban1 jia1", "move (residence)"), ("赶鸭子上架", "gan3 ya1 zi5 shang4 jia4", "push someone beyond their ability (idiom)")], title="生词")]),
        card("Activity 3: two rental advertisements",
             "A. Divide into two groups. Group A reads Advertisement 1 and Group B reads Advertisement 2. Guess the meaning of unknown words from the context, then translate the ads into English. The ads (as printed; the prices are in dollars): Advertisement 1, 公寓出租: 三藩市日落区有房出租，一室一浴一车库，月租 $2,300，包水费和垃圾，按金 $3,000，清洁金 $150，请电 415-233-6888. Advertisement 2, 独立屋出租: 日落区楼下两房出租，环境优美，交通便利，全新厨房，设备齐全，停车方便，$3,245/月，请电 415-845-2268. My translation of Ad 1: apartment for rent in San Francisco’s Sunset District, one bedroom, one bath, a garage; monthly rent $2,300, water and garbage included; deposit $3,000, cleaning fee $150. Ad 2: house for rent, two rooms downstairs in the Sunset District, beautiful environment, convenient transportation, brand-new kitchen, fully equipped, easy parking, $3,245 a month. B. Pair up with a student from the other group and paraphrase the information of your ad in standard conversational Chinese; the other student writes down the essential information, asking questions when necessary; then switch. Check your notes by reading each other’s ads."),
        card("Activity 4: an apartment ad",
             "A. Read the ad and answer: 1. Where exactly is the apartment located? 2. What type of rooms does it have and how many? 3. What furniture, amenities or utilities are provided? 4. How does a prospective renter inquire about this apartment? B. Compare answers with a partner. C. Write at least three words you didn’t understand in the ad and see if your partner can figure out the meaning from context. D. You want to rent the apartment: call the contact person (your partner) to find out the monthly rent, security deposit, utilities, WiFi, parking facilities, etc.; switch roles and repeat. The ad (the book also prints the phone number 13519855673):",
             examples=[D(AD3, AD3E)]),
    ],
    exercises=[
        M("Where did the speaker stay in his first month in Monterey?", "At an old classmate’s home", ["In a hotel", "In a dormitory", "On post"], "住在我的老同学家里。"),
        M("Why couldn’t the classmate find an apartment?", "Rents in Monterey are expensive", ["He was too busy", "There are no apartments", "He did not like apartments"], "蒙特雷的房租很贵。"),
        M("How much is the monthly rent of the apartment in the passage?", "1,800", ["800", "18,000", "180"], "每个月的房租只要一千八。"),
        M("What does the rent include?", "Internet", ["Water and electricity", "Furniture only", "Nothing"], "包上网费，不包水电。"),
        M("How far is the apartment from school?", "A twenty-minute drive", ["A twenty-minute walk", "A two-hour drive", "Next door"], "开二十分钟的车就可以到学校了。"),
        M("Who is the manager?", "王经理", ["张经理", "李先生", "马林"], "出租公寓的王经理."),
        M("When was the apartment built?", "Last year", ["Ten years ago", "This year", "Two years ago"], "去年建的。"),
        M("What must be paid before renting?", "A month’s rent and a month’s deposit", ["Only the rent", "A year’s rent", "Nothing"], "要付一个月的房租和一个月的押金。"),
        M("What does 搬家 mean?", "Move (residence)", ["Clean the house", "Buy a house", "Rent a car"], "搬家."),
        M("What does 钥匙 mean?", "Key", ["Door", "Window", "Lock only"], "钥匙."),
        M("In the last ad, where is the suite?", "On the first floor next to Sun Yat-sen University", ["On the top floor", "In a villa", "Downtown"], "位于中山大学旁……一楼。"),
        M("How many bedrooms does the suite have?", "Three", ["Two", "One", "Four"], "三房两厅一厨两卫。"),
        M("What does 您只需拎包即可入住 mean?", "You only need to bring your bags and move in", ["You must buy furniture", "Bags are provided", "Move in next year"], "拎包即可入住."),
        mean("出租", "chu1 zu1", "rent out, for rent", ["rent (housing)", "deposit", "furniture"]),
        mean("环境", "huan2 jing4", "environment", ["deposit", "key", "furniture"]),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context
QS = [("公寓在哪里？", "Where is the apartment?"), ("什么样的公寓？", "What kind of apartment?"), ("月租是多少？", "How much is the monthly rent?"), ("客厅有多大？", "How big is the living room?"), ("公寓都包什么？", "What does the apartment include?"), ("公寓带什么家具？", "What furniture does the apartment come with?"), ("每个房间有什么？", "What is in each room?"), ("有没有停车位？", "Is there a parking space?"), ("要不要付押金？", "Do you need to pay a deposit?")]
L5 = lesson(
    "Lesson 10 Presentation 1 using Chinese in context",
    "单间出租 · 有房出租 · 找室友 · 打电话问房租",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking)",
             "A. Pair up. Your teacher, played by your partner, rents an apartment in Monterey. You would also like to move off post. Ask for information about the rental (location, monthly rent, utilities, living conditions, etc.) and take notes in a worksheet. B. Report the information you gathered to the class. The questions to ask:",
             examples=[D(z, e) for z, e in QS]),
        card("Activity 2 (Reading and Speaking): two ads",
             "Form two groups of three. One student plays a prospective renter inquiring about two apartment ads, while the other two play the contact people, Mr. Zhang or Ms. Wang. A. The contact people first read their ads; the renter calls each one and writes down the essential details. B. The renter decides which apartment to rent and reports the choice and reasoning to the class in Chinese. The ads (as printed; the book gives the phone numbers 831-339-7156 and 831-467-5890): 单间出租: 木地板，双人床，宽带，衣柜，电脑桌，沙发，热水器，包水电，网络，900 元/月，女士，学生，上班族优先，联系人：张先生. 有房出租: 一室一厅，近市中心，超市，医院，交通便利，不带家具，包水电，不包网络，电视，1200 元/月，联系人：王小姐. Notes (mine): the first is a single room with wooden floor, double bed, broadband, wardrobe, computer desk, sofa, water heater, water and electricity included, 900 yuan a month, women, students and office workers preferred; the second is a one-bedroom, one-living-room apartment near the city center, supermarket and hospital, convenient transportation, unfurnished, water and electricity included, internet not included, TV, 1,200 yuan a month."),
        card("Activity 3 (Writing and Speaking)",
             "A. Form two groups of three. You need a fourth roommate to share your apartment in Taipei. Write an ad in Chinese to post online, including the location, amount of security deposit, monthly rent, utilities, amenities (TV, WiFi, etc.), furnishings, parking, contact information and what sort of tenant you are seeking. B. Pair up with a student from the other group. Call the contact person to inquire about the apartment they are advertising, while the contact person asks for details about you. Conclude by deciding whether this is a mutually agreeable arrangement; switch roles and repeat."),
    ],
    exercises=[
        M("Which question asks where the apartment is?", "公寓在哪里？", ["公寓有多大？", "公寓贵不贵？", "公寓是谁的？"], "在哪里: where."),
        M("Which question asks what furniture comes with it?", "公寓带什么家具？", ["公寓包什么？", "公寓在哪里？", "公寓多大？"], "带什么家具."),
        M("Which question asks about the deposit?", "要不要付押金？", ["要不要看房？", "要不要停车？", "要不要搬家？"], "押金: deposit."),
        M("What does 单间出租 mean?", "A single room for rent", ["A whole house for sale", "A shop for rent", "A garage for rent"], "单间: a single room."),
        M("In the second ad, is the apartment furnished?", "No", ["Yes", "Only the kitchen", "Only the bed"], "不带家具。"),
        M("What does 包水电 mean?", "Water and electricity are included", ["Water and electricity are extra", "Only water", "No utilities"], "包水电."),
        M("What does 近市中心 mean?", "Near the city center", ["Far from the city center", "In the village", "By the sea"], "近: near."),
        M("In the first ad, who gets priority?", "Women, students and office workers", ["Men only", "Families", "Foreigners only"], "女士，学生，上班族优先."),
        F("请问，公寓___什么家具？", "带", PART, "带: come with."),
        F("这个公寓交通便利，___市中心很近。", "离", ["吗", "们", "呢"], "离…很近: close to."),
    ],
)

UNIT = unit("第十课 租房和住房 Presentation 1: renting an apartment", [L1, L2, L3, L4, L5,
    vocab_lesson("Lesson 10 Presentation 1 vocabulary", "Words from the book’s Presentation 1 list", "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)])
