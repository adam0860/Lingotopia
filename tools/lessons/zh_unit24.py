"""Unit 24: Lesson 8 (Chinese Food and Restaurants) Presentation 3 and Area Studies, from the book's texts: Cooking Day,
就 against 才, 了 for a new event and in sequential actions, 一边…一边…, 会, the pivotal construction, the passages about
dumplings and regional tastes, the Area Studies reading "Food in Chinese Culture" and the vocabulary list.
The listening activities, the pictures and the fill-in tables are not included; the lessons say so."""
from zh_auto import *
from zh_l8_vocab import VOC3

PART = ["吗", "们", "呢"]
FOOD = ["作业", "操场", "预习"]
JIAO = {"教": "jiao1"}

# ------------------------------------------------------------------ 1. Cooking Day
COOK = [("今天是我们班的做饭日。一大早，我们就到了学校的厨房。我们先分成了几个小组，每组有一个老师教我们做中国菜。", "Today is our class’s Cooking Day. Very early in the morning we already arrived at the school kitchen. We first divided into several groups, and in each group a teacher taught us to cook Chinese dishes."),
        ("我们的老师来自中国各地，都很会做菜。陈老师是四川人，她教我们做了一个麻婆豆腐，又香又辣。吴老师在北京长大，最会包饺子，他包的饺子又好看，又好吃。", "Our teachers come from all over China and are all good at cooking. Teacher Chen is from Sichuan; she taught us to make a mapo tofu, both fragrant and spicy. Teacher Wu grew up in Beijing and is best at wrapping dumplings; the dumplings he wraps are both good-looking and delicious."),
        ("张老师是上海人，他教我们做了一个红烧肉，颜色好，味道甜。因为我和大卫都吃素，陆老师教我们做了一个素菜，又清淡又可口。", "Teacher Zhang is from Shanghai; he taught us to make a soy-braised pork, with nice color and a sweet taste. Because David and I are both vegetarians, Teacher Lu taught us to make a vegetable dish, both mild and tasty."),
        ("大家一边做饭，一边说中文。吃了饭以后，我们还看了一个中文电影。我们过了一个愉快的做饭日。", "Everyone spoke Chinese while cooking. After eating we also watched a Chinese movie. We had a happy Cooking Day.")]
TEACH = [("陈老师", "四川人", "麻婆豆腐", "又香又辣"), ("吴老师", "在北京长大", "饺子", "又好看，又好吃"), ("张老师", "上海人", "红烧肉", "颜色好，味道甜"), ("陆老师", "(not stated)", "素菜", "又清淡又可口")]
ODD = [("甜 · 说 · 包 · 做", "甜", "The other three are verbs; 甜 is an adjective."), ("四川 · 各地 · 上海 · 北京", "各地", "The others are place names; 各地 means “various places”."),
       ("做菜 · 颜色好 · 包饺子 · 看电影", "颜色好", "The others are activities; 颜色好 describes a dish."), ("清淡 · 可口 · 辣 · 味道", "味道", "The others describe how food tastes; 味道 is the noun “taste”."),
       ("麻婆豆腐 · 红烧肉 · 饺子 · 厨房", "厨房", "The others are dishes; 厨房 is the kitchen.")]
L1 = lesson(
    "Presentation 3: Cooking Day (passage)",
    "做饭日 · 又香又辣 · 红烧肉 · 一边做饭，一边说中文",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. Do you know your Chinese teachers’ hometowns? B. Do you know what the regional cuisine is like there?"),
        card("Presentation 3: 做饭日 (Cooking Day)",
             "The book also prints this passage in traditional characters (for example 今天是我們班的做飯日).",
             examples=[D(z, e, fixes=JIAO) for z, e in COOK]),
        card("Activity 1 (Listening and Writing)",
             "A. Listen to Presentation 3 once and answer: in sequential order, what are the three main tasks during Cooking Day? B. Listen again and complete the table in Chinese: teacher, hometown or home province, dish made, description of the dish. (The recording is not included. From the text, the three tasks are: arrive at the school kitchen and divide into groups; cook with a teacher in each group; eat and watch a Chinese movie. The table, my summary:)",
             tables=[table(["Teacher", "Hometown", "Dish made", "Description"], TEACH, say=[0, 2], title="Cooking Day table")]),
        card("Activity 2 (Reading and Speaking): which word does not belong?",
             "For each group of words, select the word that does not belong in the same category as the others, and discuss your choices with a partner in Chinese. The five groups, with my answers:",
             tables=[table(["Group", "Odd one out", "Why"], ODD, say=[1], title="Odd one out")]),
    ],
    exercises=[
        M("What is happening at school today?", "Cooking Day for the class", ["A school trip", "A test", "A sports day"], "今天是我们班的做饭日。"),
        M("Where does the class go early in the morning?", "The school kitchen", ["The library", "The playground", "A restaurant"], "一大早，我们就到了学校的厨房。"),
        M("How is the class organized?", "Into small groups, each with a teacher", ["Everyone together with one teacher", "Each student alone", "By nationality"], "我们先分成了几个小组，每组有一个老师。"),
        M("Where is Teacher Chen from, and what did she teach?", "Sichuan; mapo tofu", ["Beijing; dumplings", "Shanghai; soy-braised pork", "Taiwan; a vegetable dish"], "陈老师是四川人，她教我们做了一个麻婆豆腐。"),
        M("What is mapo tofu like?", "Both fragrant and spicy", ["Sweet", "Mild and tasty", "Good-looking and delicious"], "又香又辣。"),
        M("Who grew up in Beijing and is best at wrapping dumplings?", "Teacher Wu", ["Teacher Chen", "Teacher Zhang", "Teacher Lu"], "吴老师在北京长大，最会包饺子。"),
        M("Where is Teacher Zhang from, and what is his dish like?", "Shanghai; nice color and a sweet taste", ["Sichuan; spicy", "Beijing; both good-looking and delicious", "Taiwan; mild"], "红烧肉，颜色好，味道甜。"),
        M("Why did Teacher Lu teach a vegetable dish?", "Because the speaker and David are vegetarians", ["Because it is easy", "Because meat was too expensive", "Because it is a school rule"], "因为我和大卫都吃素，陆老师教我们做了一个素菜。"),
        M("What did the class do while cooking?", "Spoke Chinese", ["Watched TV", "Sang songs", "Listened to music"], "大家一边做饭，一边说中文。"),
        M("What did they do after eating?", "Watched a Chinese movie", ["Washed the dishes", "Took a test", "Went swimming"], "吃了饭以后，我们还看了一个中文电影。"),
        M("In the odd-one-out group 甜 · 说 · 包 · 做, which word does not belong?", "甜", ["说", "包", "做"], "说, 包 and 做 are verbs; 甜 is an adjective."),
        M("In the group 麻婆豆腐 · 红烧肉 · 饺子 · 厨房, which word does not belong?", "厨房", ["麻婆豆腐", "红烧肉", "饺子"], "The other three are dishes."),
        F("我们先___成了几个小组。", "分", PART, "分成: divide into."),
        F("陈老师教我们做了一个麻婆豆腐，又香___辣。", "又", PART, "又…又… joins both qualities."),
        mean("做饭日", "zuo4 fan4 ri4", "Cooking Day", ["Birthday", "Sports Day", "Test day"]),
    ],
)

# ------------------------------------------------------------------ 2. the birthday passage, mapo tofu, dishes
BDAY = ("今天是我的生日，一大早我就起床了。今天天气很好。早饭以后，我和几个同学先去海边玩儿了两个小时，然后，我们一起到城里的一家中国餐馆吃午饭。我们一边吃饭一边聊天。午饭以后，我们还去看了一个新电影。我过了一个很有意思的生日。",
        "Today is my birthday; very early in the morning I got up. The weather is very good today. After breakfast, a few classmates and I first went to the beach and played for two hours, then we went together to a Chinese restaurant in town for lunch. We chatted while we ate. After lunch we also went to see a new movie. I had a very interesting birthday.")
BDAY_T = [("一大早", "起床"), ("早饭以后", "和几个同学先去海边玩儿了两个小时"), ("然后", "一起到城里的一家中国餐馆吃午饭（一边吃饭一边聊天）"), ("午饭以后", "还去看了一个新电影")]
MENU9 = [("糖醋鱼", "sweet and sour fish"), ("西红柿炒鸡蛋", "tomato and scrambled eggs"), ("酸辣汤", "hot and sour soup"), ("红烧肉", "soy-braised pork"), ("饺子", "dumplings"), ("麻婆豆腐", "mapo tofu"), ("北京烤鸭", "Beijing roast duck"), ("素三鲜", "stir-fried three vegetable delicacies"), ("啤酒", "beer")]
REG5 = [("四川", "麻婆豆腐 又香又辣"), ("北京", "饺子，烤鸭"), ("上海", "红烧肉 颜色好，味道甜"), ("广东", "清淡，海鲜")]
L2 = lesson(
    "Presentation 3 activities: a birthday, and choosing from the menu",
    "今天是我的生日 · 先…然后 · 我们一边吃饭一边聊天 · 麻婆豆腐",
    requires=[],
    cards=[
        card("Activity 3 (Reading and Speaking): a birthday passage",
             "A. Read the passage, highlight the activities and the time phrases associated with them. B. Think about what you did last Saturday and complete a table with the columns Time and Activity. C. Pair up and, referring to the table, tell your partner what you did using time phrases, past tense particles, 先…然后 and 以后.",
             examples=[D(*BDAY)]),
        card("The activities and their time phrases",
             "From the passage, the time phrase and its activity:",
             tables=[table(["Time phrase", "Activity"], BDAY_T, say=[0, 1], title="一个很有意思的生日")]),
        card("Activities 4 and 5",
             "Activity 4: A. A group of people are sharing a dish of 麻婆豆腐; listen to the fourteen audios and decide whether each person likes or dislikes it (audio, not included). B. Pair up. Each of you selects a few items from the menu below and tells your partner what you have decided to order; your partner explains why they like or dislike those items; then share your comments with the class. Activity 5: listen to a dialog and complete a table of places and the special features of their dishes; then discuss the regional dishes with a partner and add new information (audio, not included).",
             tables=[wtable(rows_py(MENU9), title="The menu")]),
    ],
    exercises=[
        M("In the passage, when did the speaker get up?", "Very early in the morning", ["At noon", "After lunch", "In the evening"], "一大早我就起床了。"),
        M("What did the speaker do after breakfast?", "Went to the beach for two hours with classmates", ["Took a test", "Cooked lunch", "Saw a movie"], "早饭以后，我和几个同学先去海边玩儿了两个小时。"),
        M("Where did they have lunch?", "A Chinese restaurant in town", ["At home", "At the school kitchen", "On the beach"], "到城里的一家中国餐馆吃午饭。"),
        M("What did they do while eating?", "Chatted", ["Watched TV", "Did homework", "Sang"], "我们一边吃饭一边聊天。"),
        M("What did they do after lunch?", "Saw a new movie", ["Went swimming", "Cooked dinner", "Studied"], "午饭以后，我们还去看了一个新电影。"),
        M("What kind of birthday did the speaker have?", "A very interesting one", ["A boring one", "A tiring one", "A lonely one"], "我过了一个很有意思的生日。"),
        M("Which phrase marks “after lunch”?", "午饭以后", ["早饭以后", "一大早", "然后"], "午饭以后 = after lunch."),
        M("What does 先去海边玩儿了两个小时，然后…… show?", "The order of two activities: first … then …", ["Two things at once", "A wish", "A question"], "先…然后… marks sequence."),
        F("早饭以后，我和几个同学___去海边玩儿了两个小时。", "先", PART, "先…，然后… marks the order."),
        F("我们一___吃饭一边聊天。", "边", PART, "一边…一边… marks simultaneous actions."),
        F("今天天气___好。", "很", PART, "很 + adjective."),
        mean("麻婆豆腐", "ma2 po2 dou4 fu5", "mapo tofu (stir-fried tofu in hot sauce)", ["Beijing roast duck", "sweet and sour fish", "soy-braised pork"]),
        mean("素三鲜", "su4 san1 xian1", "stir-fried three vegetable delicacies", ["beer", "dumplings", "sweet and sour fish"]),
    ],
)

# ------------------------------------------------------------------ 3. 就 against 才
JIU = [("下个星期就是他的生日了。", "His birthday is next week."), ("他的老家就在这儿。", "His hometown is right here.")]
JIU2 = [("一大早，我们就到了学校的厨房。", "Very early in the morning we already arrived at the school kitchen."), ("他每天早上四点半就起床。", "He gets up at half past four every morning already."), ("他每天晚上九点半就睡觉。", "He goes to bed at half past nine every night already.")]
CMP = [("一大早，我们就到了学校的厨房。", "十点多，他们才到了学校的厨房。", "We were already at the school kitchen very early; they didn’t get there until after ten."), ("他早上四点半就起床。", "他早上八点才起床。", "He gets up at 4:30 already; he doesn’t get up until eight."),
       ("十一点我们就吃午饭。", "下午两点他们才吃午饭。", "We eat lunch as early as eleven; they don’t eat lunch until two in the afternoon."), ("我老家四月就很热。", "他老家八月才热。", "My hometown is already hot in April; his is not hot until August.")]
JIUCAI = [("我一分钟就吃了五个饺子。", "I ate five dumplings in just one minute."), ("你一分钟才吃了五个饺子？我一分钟就吃了十个！", "You only ate five dumplings in a minute? I ate ten in a minute!")]
L3 = lesson(
    "Presentation 3 grammar: 就 for “earlier than expected”",
    "一大早我们就到了 · 早上四点半就起床 · 就 against 才",
    requires=[],
    cards=[
        card("Adverb 就 (2)",
             "In previous lessons we learned that the adverb 就 is used before a verb to enhance the tone of emphasis. In this lesson 就 indicates that an action happened early: 一大早，我们就到了学校的厨房 (Very early in the morning, we already arrived at the school kitchen). Pattern: 就 + V/VP.",
             examples=[D(z, e) for z, e in JIU] + [D(z, e) for z, e in JIU2]),
        card("就 against 才",
             "While the adverb 才 (see Presentation 2) indicates that something happened later than expected, 就 indicates that something happened earlier than expected. Compare the four pairs:",
             examples=[D(a, e) for a, b, e in CMP] + [D(b, e) for a, b, e in CMP]),
        card("Opinion: the same fact with 才 or 就",
             "The use of 才 or 就 contains the speaker’s opinion. Therefore, for the same situation, speaker A may use 才 and speaker B 就:",
             examples=[D("甲：" + JIUCAI[0][0], JIUCAI[0][1]), D("乙：" + JIUCAI[1][0], JIUCAI[1][1])]),
        card("Activity 1 (Writing and Speaking)",
             "A. Write three things you consider you do earlier than others in daily life (with 就) and three you do later (with 才). Examples: 我每天早上五点半就锻炼。 / 我每天下午四点才锻炼。 B. Pair up and take turns sharing; your partner responds by comparing his or her situation with yours: 我也每天早上五点半就锻炼。 or 你五点半才锻炼？我四点半就锻炼。 or 你早上五点半就锻炼？我下午四点才锻炼。"),
    ],
    exercises=[
        M("What does 就 show in 一大早，我们就到了学校的厨房?", "It happened early, earlier than expected", ["It happened late", "It will happen", "It never happened"], "就 + verb: already."),
        M("What does 才 show?", "It happened later than expected", ["It happened earlier than expected", "It is a question", "It is a command"], "才: not until."),
        M("Which sentence says he gets up early?", "他早上四点半就起床。", ["他早上八点才起床。", "他不起床。", "他早上起床吗？"], "四点半就: as early as 4:30."),
        M("Which sentence says he gets up late?", "他早上八点才起床。", ["他早上四点半就起床。", "他早上就起床。", "他起床了。"], "八点才: not until eight."),
        M("Which sentence says it is already hot in April?", "我老家四月就很热。", ["他老家八月才热。", "我老家四月不热。", "我老家很冷。"], "四月就很热."),
        M("In 你一分钟才吃了五个饺子？我一分钟就吃了十个！, who thinks five is a small number?", "The speaker who says 才", ["The speaker who says 就", "Both speakers", "Neither speaker"], "才 expresses “only”; 就 expresses “as many as”."),
        M("In the same exchange, who thinks ten is a lot, and the speaker’s own pace fast?", "The speaker who says 就", ["The speaker who says 才", "Both", "Neither"], "我一分钟就吃了十个！"),
        M("Where does 就 go?", "Before the verb or verb phrase", ["At the end", "After the object", "Before the subject"], "就 + V/VP."),
        M("Which means “We eat lunch as early as eleven”?", "十一点我们就吃午饭。", ["十一点我们才吃午饭。", "我们吃午饭十一点就。", "就我们十一点吃午饭。"], "十一点 + 就 + verb."),
        F("他每天晚上九点半___睡觉。", "就", ["再", "给", "放"], "九点半就睡觉: early."),
        F("十点多，他们___到了学校的厨房。", "才", ["再", "吗", "们"], "才: later than expected."),
        F("下个星期___是他的生日了。", "就", ["再", "吗", "们"], "就 enhances emphasis: next week IS his birthday."),
        mean("一大早", "yi1 da4 zao3", "early morning; at dawn", ["afternoon", "evening", "midnight"]),
    ],
)

# ------------------------------------------------------------------ 4. 了 for a new event
LE = [("昨天，我和朋友们看了一个中国电影。", "Yesterday I and my friends saw a Chinese movie."), ("今天早上，北京下了一场大雪。", "This morning it snowed heavily in Beijing."), ("周末，我买了两本中文书。", "On the weekend I bought two Chinese books."),
      ("昨天，我值班，没有去上课。", "Yesterday I was on duty and did not go to class."), ("你昨天锻炼没锻炼？", "Did you exercise yesterday?")]
LE_REP = [("去年，我每个月都看一个中国电影。", "Last year I saw a Chinese movie every month."), ("明年，我每个月都要看一个中国电影。", "Next year I will see a Chinese movie every month.")]
MONO = [("我们去了一家餐馆。", "We went to a restaurant."), ("服务员给了我们菜单，问我们想喝点儿什么。", "The waiter gave us the menu and asked what we wanted to drink."), ("我要了一瓶啤酒，小文要了一杯橙汁。", "I ordered a bottle of beer and Xiaowen ordered a glass of orange juice."),
        ("服务员说北京烤鸭最有特色，我们就点了半只烤鸭、一个糖醋鱼和一个西红柿炒鸡蛋。", "The waiter said the Beijing roast duck was the most distinctive, so we ordered half a duck, a sweet and sour fish and a tomato and scrambled eggs."),
        ("我们还要了两碗米饭和一盘饺子，还请服务员拿了两双筷子。", "We also ordered two bowls of rice and a plate of dumplings, and asked the waiter to bring two pairs of chopsticks."), ("五分钟以后，菜来了，我们谢了服务员。", "Five minutes later the dishes came and we thanked the waiter.")]
L4 = lesson(
    "Presentation 3 grammar: 了 for reporting a new event",
    "我们做了一个麻婆豆腐 · 没有… · 看没看 · 去年每个月都看一个",
    requires=[],
    cards=[
        card("了 for reporting a new event",
             "了 can be used to report a new event: 我们做了一个麻婆豆腐 (We made a mapo tofu). When 了 is used to report a new event, it occurs between the verb and the object. The negative and interrogative forms use 没(有) without 了. Positive: Subject + Verb + 了 + (Num. + M) + Object. Negative: Subject + 没(有) + Verb + Object. Interrogative: Subject + Verb + 没(有) + Verb + Object?",
             examples=[D("我们做了一个麻婆豆腐。", "We made a mapo tofu.")] + [D(z, e) for z, e in LE]),
        card("The negative never takes 了",
             "The book marks 昨天，我值班，没有去上课了 as wrong (with 没有 do not add 了); the correct sentence is 昨天，我值班，没有去上课。"),
        card("Repeated actions do not take 了",
             "This use of 了 can’t refer to repeated actions, even if the actions happened in the past. In Chinese, a simple verb is used to state repeated actions, whether they are in the past, present or future. So 去年，我每个月都看了一个中国电影 is not the way to say it; use:",
             examples=[D(z, e) for z, e in LE_REP]),
        card("Activities 2 and 3: narrate it",
             "Activity 2: turn the ordering dialog of Presentation 1 into a monolog using as many 了 as possible to report new events; write an outline first, then narrate it to a partner. One possible monolog (mine):",
             examples=[D(z, e) for z, e in MONO]),
        card("Activity 3 (Writing and Speaking)",
             "Narrate your last experience at a restaurant. A. List five actions you did, in order, using 了 as many times as possible. B. Arrange the actions into a monolog with necessary time nouns and cohesive devices such as 去年, 上个月, 先…然后 and 还; write an outline in your notebook. C. Pair up and speak your monolog to your partner."),
    ],
    exercises=[
        M("Where does 了 go when reporting a new event?", "Between the verb and the object", ["At the end of the sentence only", "Before the verb", "Before the subject"], "Subject + Verb + 了 + Object."),
        M("What does 周末，我买了两本中文书 mean?", "On the weekend I bought two Chinese books", ["I will buy two Chinese books", "I buy Chinese books every weekend", "I have no Chinese books"], "买了: a completed new event."),
        M("How do you say “I did not go to class yesterday”?", "昨天，我没有去上课。", ["昨天，我没有去上课了。", "昨天，我不了去上课。", "昨天，我去了没上课。"], "Negative: 没(有) without 了."),
        M("How do you ask “Did you exercise yesterday?” in the verb-not-verb form?", "你昨天锻炼没锻炼？", ["你昨天锻炼了没有了？", "你昨天没锻炼了锻炼？", "你昨天锻炼不锻炼了？"], "Verb + 没(有) + verb."),
        M("Which form is used for repeated actions in the past?", "A simple verb: 去年，我每个月都看一个中国电影", ["Verb + 了: 去年，我每个月都看了一个中国电影", "没 + 了", "再 + 了"], "了 can’t refer to repeated actions."),
        M("Which sentence reports a one-time past event?", "昨天，我和朋友们看了一个中国电影。", ["明年，我每个月都要看一个中国电影。", "去年，我每个月都看一个中国电影。", "我很喜欢看中国电影。"], "了 + one-time event."),
        M("What does 今天早上，北京下了一场大雪 mean?", "This morning it snowed heavily in Beijing", ["It will snow in Beijing", "It snows in Beijing every morning", "Beijing has no snow"], "下了一场大雪: it snowed a big snow."),
        M("Which sentence is wrong?", "昨天，我值班，没有去上课了。", ["昨天，我值班，没有去上课。", "昨天，我看了一个电影。", "你昨天锻炼没锻炼？"], "没有 and 了 do not go together."),
        F("昨天，我和朋友们看___一个中国电影。", "了", PART, "Verb + 了 + number + measure word + object."),
        F("你昨天锻炼___锻炼？", "没", ["再", "吗", "们"], "A 没-verb question reports a past event."),
        F("昨天，我值班，___有去上课。", "没", ["再", "才", "们"], "没有 negates a past event."),
        mean("了", "le5", "(particle reporting a completed new event)", ["(a question particle)", "(a plural suffix)", "(a measure word)"]),
    ],
)

# ------------------------------------------------------------------ 5. 一边…一边…
YIBIAN = [("大家一边做饭，一边说中文。", "Everyone spoke Chinese while cooking."), ("他一边吃饭，一边看电视。", "He watches TV while eating."), ("他们一边散步，一边聊天。", "They chat while taking a walk."), ("我们边走边聊吧。", "Let’s chat while we walk.")]
YIBIAN_SAY = [("他们一边喝茶，一边看书。", "They read while drinking tea."), ("她一边走路，一边打电话。", "She talks on the phone while walking."), ("孩子们一边包饺子，一边唱歌。", "The children sing while wrapping dumplings."), ("我喜欢一边听音乐，一边做作业。", "I like to do homework while listening to music."),
              ("请不要一边上课，一边玩儿手机。", "Please don’t play with your phone while in class.")]
L5 = lesson(
    "Presentation 3 grammar: 一边…一边… for two simultaneous actions",
    "一边做饭，一边说中文 · 边走边聊",
    requires=[],
    cards=[
        card("The 一边…一边… construction",
             "The 一边…一边… construction expresses two actions occurring at the same time. Pattern: Subject + 一边 + Verb + (Object), 一边 + Verb + (Object). 一边 can be shortened to 边 for a more colloquial feeling, especially when the verb is monosyllabic.",
             examples=[D(z, e) for z, e in YIBIAN]),
        card("Activity 4 (Speaking and Writing)",
             "A. Pair up. Choose three of nine pictures (not included) and describe them to the class using 一边…一边…. B. Use 一边…一边… to complete: 1. 我喜欢… 2. (a classmate) 常常… 3. 请不要… Some of mine (the key is mine):",
             examples=[D(z, e) for z, e in YIBIAN_SAY]),
    ],
    exercises=[
        M("What does 一边…一边… express?", "Two actions at the same time", ["Two actions one after another", "A choice between two actions", "A negative command"], "他一边吃饭，一边看电视."),
        M("What does 他们一边散步，一边聊天 mean?", "They chat while taking a walk", ["They take a walk, then chat", "They neither walk nor chat", "They talk about walking"], "一边 + verb, 一边 + verb."),
        M("What is the colloquial short form of 一边?", "边", ["再", "就", "才"], "我们边走边聊吧."),
        M("When is the short form 边 most natural?", "When the verb is monosyllabic", ["When the verb has three syllables", "In writing only", "In questions only"], "边走边聊: 走 and 聊 are one syllable each."),
        M("What does 我们边走边聊吧 mean?", "Let’s chat while we walk", ["Let’s walk then chat", "We chatted yesterday", "Don’t walk"], "边走边聊."),
        M("Which sentence is right for “He watches TV while eating”?", "他一边吃饭，一边看电视。", ["他一边吃饭，然后看电视。", "他吃饭一边看电视一边。", "他一边一边吃饭看电视。"], "一边 before each verb."),
        M("Which sentence is right for “Everyone spoke Chinese while cooking”?", "大家一边做饭，一边说中文。", ["大家做饭，一边说中文一边。", "大家先做饭，然后说中文。", "大家一边做饭说中文。"], "两个一边."),
        F("他们一___散步，一边聊天。", "边", PART, "一边…一边…"),
        F("大家一边做饭，一___说中文。", "边", PART, "The second 一边."),
        F("我们___走边聊吧。", "边", ["再", "才", "们"], "边…边… in short form."),
        mean("一边", "yi4 bian1", "at the same time (in 一边…一边…)", ["again", "already", "later"]),
    ],
)

# ------------------------------------------------------------------ 6. 会
HUI = [("我会说中文。", "I can speak Chinese."), ("你会不会写汉字？", "Can you write Chinese characters?"), ("大卫不会游泳。", "David can’t swim."), ("你们都会包饺子吗？", "Can you all wrap dumplings?"), ("我妈妈很会做饭，可是她不太会做中国饭。", "My mother is very good at cooking, but she isn’t very good at cooking Chinese food.")]
ABIL = [("做饭", "cook"), ("包饺子", "wrap dumplings"), ("写汉字", "write Chinese characters"), ("说中文", "speak Chinese"), ("说法文", "speak French"), ("说西班牙文", "speak Spanish"), ("做红烧肉", "make soy-braised pork"), ("游泳", "swim"), ("做中国饭", "cook Chinese food"), ("用筷子", "use chopsticks"), ("用中文点菜", "order food in Chinese")]
REPORT = [("我们都很会说中文。", "We can all speak Chinese very well."), ("我会包饺子，可是他不会包饺子。", "I can wrap dumplings, but he can’t."), ("我会游泳，他也会游泳。", "I can swim and he can swim too."), ("我们都不太会做红烧肉。", "None of us is very good at making soy-braised pork.")]
L6 = lesson(
    "Presentation 3 grammar: the modal verb 会",
    "我会说中文 · 你会不会写汉字？ · 很会做饭 · 不太会",
    requires=[],
    cards=[
        card("Modal verb 会",
             "The modal verb 会 indicates an ability that has been learned, that is, one knows how to do something. Pattern: Subject + 会 + Verb + Object.",
             examples=[D(z, e) for z, e in HUI]),
        card("Activity 5 (Reading and Speaking): can you …?",
             "A. With a partner, take turns asking if he or she knows how to perform the activities below; keep going until you have used up all the items (the last item in the book is a smiley picture). New word: 用 yòng, to use. B. Report your findings to the class using patterns such as 我们都(很/不太/不)会…, 我会, 可是他不会…, 我会，他也会.",
             tables=[wtable(rows_py(ABIL), title="Can you …?")],
             examples=[D(z, e) for z, e in REPORT]),
    ],
    exercises=[
        M("What does 会 indicate?", "A learned ability: knowing how to do something", ["A future plan", "A permission", "A past event"], "我会说中文."),
        M("What does 大卫不会游泳 mean?", "David can’t swim", ["David doesn’t like to swim", "David swam yesterday", "David will swim"], "不会 + verb: can’t (not learned)."),
        M("How do you ask “Can you write Chinese characters?” in the verb-not-verb form?", "你会不会写汉字？", ["你会写汉字不会？", "你不会会写汉字？", "你写会不会汉字？"], "会不会 + verb."),
        M("What does 我妈妈很会做饭 mean?", "My mother is very good at cooking", ["My mother will cook", "My mother cooked", "My mother dislikes cooking"], "很会: skilled at."),
        M("What does 不太会 mean in 她不太会做中国饭?", "isn’t very good at", ["is very good at", "will never", "refuses to"], "不太会: not very able."),
        M("Which sentence says “I can use chopsticks”?", "我会用筷子。", ["我要用筷子。", "我想用筷子吗。", "我了用筷子。"], "会 + verb + object."),
        M("How do you say “Can you order food in Chinese?”", "你会用中文点菜吗？", ["你会点菜用中文吗？", "你用会中文点菜吗？", "你中文会用点菜吗？"], "用中文 comes before 点菜."),
        M("Which sentence reports that both of you can do it?", "我会，他也会。", ["我会，可是他不会。", "我不会，他也不会。", "我们都不会。"], "也: also."),
        F("我___说中文。", "会", ["再", "才", "们"], "会 + verb: can."),
        F("大卫不___游泳。", "会", ["再", "才", "们"], "不会 + verb."),
        F("你们都会包饺子___？", "吗", ["们", "呢", "不会"], "会 + verb + object + 吗."),
        mean("会", "hui4", "can; be able to (a learned ability)", ["divide", "wrap", "arrive"]),
    ],
)

# ------------------------------------------------------------------ 7. 了 in sequential actions
SEQL = [("上周六，买了东西，我和朋友看了一个中国电影。", "Last Saturday, after buying things, my friend and I saw a Chinese movie. (past action)"), ("吃了午饭以后，我要去图书馆预习功课。", "After eating lunch, I am going to the library to preview the lessons. (future action)"),
        ("张老师做了麻婆豆腐，还做了一个糖醋鱼。", "Teacher Zhang made mapo tofu, and also made a sweet and sour fish. (past action)"), ("明天晚上，预习了功课，我要去值班。", "Tomorrow evening, after previewing the lessons, I am going on duty. (future action)")]
SEQL_REP = [("每天，下了课，我们都得去操场跑步。", "Every day, after class, we have to go run on the drill field. (repeated action)", {"得": "dei3"}), ("每个周日，吃了早饭，我都去海边跑步。", "Every Sunday, after eating breakfast, I go running at the beach. (repeated action)", None)]
VPAIRS = [("做作业，预习功课", "做了作业以后，我又预习了明天的功课。", "After doing my homework, I also previewed tomorrow’s lessons."), ("吃早饭，上课", "等你吃了早饭，我们一起去上课吧。", "When you have eaten breakfast, let’s go to class together."),
          ("做汤，做糖醋鱼", "我做了汤，还做了一个糖醋鱼。", "I made soup, and also made a sweet and sour fish."), ("锻炼，去电影院", "锻炼了以后，我们去电影院看电影吧。", "After working out, let’s go to the cinema to see a movie."),
          ("预习课文，去饭馆", "预习了课文，我们就去饭馆吃饭。", "Once we have previewed the text, we’ll go to a restaurant to eat."), ("喝汤，吃饭", "喝了汤以后，我们再吃饭。", "After drinking the soup, we’ll eat."),
          ("值班，睡觉", "值了班，我就去睡觉了。", "After going on duty, I went to sleep."), ("集合，上课", "集合了以后，我们去上课。", "After forming up, we go to class.")]
L7 = lesson(
    "Presentation 3 grammar: 了 in sequential actions",
    "吃了饭以后，我们还看了一个中文电影 · 下了课，我们都得去操场跑步",
    requires=[],
    cards=[
        card("了 in sequential actions",
             "了 can be used in sequential actions to indicate that two actions take place one after another: 吃了饭以后，我们还看了一个中文电影 (We saw a Chinese movie after dinner). 了 in a sequence of actions is placed after the first verb. It can refer to a past action, a future action or repeated actions. Past: Subj. + V1 + 了 + Obj., V2 + 了 + (Num. + M) Obj.; or V1 + 了 + Obj., Subj. + V2 + 了 + (Num. + M) Obj. Future or repeated: Subj. + V1 + 了 + Obj., V2 + Obj.; or V1 + 了 + Obj., Subj. + V2 + Obj.",
             examples=[D("吃了饭以后，我们还看了一个中文电影。", "We saw a Chinese movie after dinner.")] + [D(z, e) for z, e in SEQL] + [D(z, e, fixes=f) for z, e, f in SEQL_REP]),
        card("Activity 6 (Reading and Speaking): sequences with 了",
             "Pair up. Using the sequential action 了, take turns making sentences with the verbal phrase pairs listed below, and orally translate your partner’s sentences into English. The book’s two examples: 做作业，预习功课 → 做了作业以后，我又预习了明天的功课。 吃早饭，上课 → 等你吃了早饭，我们一起去上课吧。 The eight pairs of the activity, with sentences of my own:",
             examples=[D(b, e) for a, b, e in VPAIRS]),
        card("Activity 7 (Listening and Writing)",
             "Listen to four dialogs and write the activities you hear in sequential order using Chinese characters (audio, not included)."),
    ],
    exercises=[
        M("Where is 了 placed in a sequence of actions?", "After the first verb", ["After the last verb only", "At the end of the sentence", "Before the subject"], "V1 + 了 + Obj., V2…"),
        M("What does the 了 after the first verb show?", "The first action is completed before the second", ["The actions are simultaneous", "The actions are negative", "A question"], "Sequence: after V1, then V2."),
        M("Can the sequential 了 refer to a future action?", "Yes: 吃了午饭以后，我要去图书馆预习功课", ["No, only the past", "Only in questions", "Only with 没"], "Past, future or repeated."),
        M("Can the sequential 了 refer to repeated actions?", "Yes: 每天，下了课，我们都得去操场跑步", ["No", "Only with 才", "Only in the past"], "Repeated actions are allowed."),
        M("What does 每个周日，吃了早饭，我都去海边跑步 mean?", "Every Sunday after breakfast I go running at the beach", ["Last Sunday I ran", "I will run next Sunday only", "I never run"], "都 shows repetition."),
        M("What does 明天晚上，预习了功课，我要去值班 mean?", "Tomorrow evening, after previewing the lessons, I will go on duty", ["Yesterday I went on duty", "I never preview", "Tomorrow I preview only"], "A future sequence."),
        M("What does 张老师做了麻婆豆腐，还做了一个糖醋鱼 mean?", "Teacher Zhang made mapo tofu and also a sweet and sour fish", ["Teacher Zhang ate mapo tofu", "Teacher Zhang will make fish", "Teacher Zhang can’t cook"], "Two past actions."),
        M("Which is right for “After class, we have to go to the drill field”?", "下了课，我们都得去操场。", ["下课了，我们都得去操场。", "下课，了我们都得去操场。", "我们都得去操场下了课。"], "V1 + 了 + Obj., Subj. + V2…"),
        F("吃___午饭以后，我要去图书馆。", "了", PART, "了 comes after the first verb."),
        F("上周六，买___东西，我和朋友看了一个中国电影。", "了", PART, "了 after 买."),
        F("下了课，我们都___去操场跑步。", "得", ["了", "吗", "们"], "得 (děi) means must here."),
        mean("集合", "ji2 he2", "have formation; muster", ["wrap", "divide", "wait a moment"]),
    ],
)

# ------------------------------------------------------------------ 8. the pivotal construction
PIV = [("林老师教我们包饺子。", "Teacher Lin teaches us to wrap dumplings."), ("昨天，老师教我们唱了一个中国歌。", "Yesterday the teacher taught us to sing a Chinese song."), ("他请我吃饭。", "He invites me to dinner."), ("妈妈叫我回家。", "Mom tells me to come home.")]
PIV8 = [("我爸爸教我游泳。", "My dad taught me how to swim."), ("陆老师教我们做了一个素菜。", "Teacher Lu taught us to make a vegetable dish."), ("我的好朋友请我去他家。", "My good friend invited me to his home.")]
L8 = lesson(
    "Presentation 3 grammar: the pivotal construction",
    "林老师教我们包饺子 · 他请我吃饭 · 妈妈叫我回家",
    requires=[],
    cards=[
        card("The pivotal construction",
             "In a pivotal sentence there are two predicates (verbs). The object of the first verb is also the subject of the second verb. Pattern: Subject + Verb 1 + Subject/Object + Verb 2 + Object 2.",
             examples=[D(z, e, fixes=JIAO) for z, e in PIV]),
        card("Activity 8 (Reading and Writing): translate",
             "Translate the three sentences into English. The key (mine):",
             examples=[D(z, e, fixes=JIAO) for z, e in PIV8]),
    ],
    exercises=[
        M("How many predicates (verbs) does a pivotal sentence have?", "Two", ["One", "Three", "None"], "Verb 1 and Verb 2."),
        M("What is special about the object of the first verb?", "It is also the subject of the second verb", ["It is omitted", "It comes after the second verb", "It is always 你"], "Subject + V1 + Subject/Object + V2 + Object 2."),
        M("In 林老师教我们包饺子, which word is the pivot?", "我们", ["林老师", "饺子", "包"], "我们 is the object of 教 and the subject of 包."),
        M("In 他请我吃饭, which word is the pivot?", "我", ["他", "吃", "饭"], "我 is the object of 请 and the subject of 吃."),
        M("In 妈妈叫我回家, who comes home?", "我 (I)", ["妈妈", "他", "老师"], "我 is the subject of 回家."),
        M("What does 他请我吃饭 mean?", "He invites me to dinner", ["He asks me to cook", "I invite him to dinner", "He eats my dinner"], "请 = invite."),
        M("What does 妈妈叫我回家 mean?", "Mom tells me to come home", ["Mom goes home", "I tell mom to come home", "Mom calls me at home"], "叫 here means to tell, to ask."),
        M("What does 我的好朋友请我去他家 mean?", "My good friend invited me to his home", ["I invited my friend to my home", "My friend is at home", "I went home"], "请我去他家."),
        F("林老师___我们包饺子。", "教", ["再", "才", "放"], "教 + people + verb: teach someone to do."),
        F("他请我___饭。", "吃", ["拿", "放", "查"], "请我吃饭: invite me to eat."),
        F("妈妈叫我回___。", "家", ["作业", "操场", "预习"], "回家: go home."),
        mean("请", "qing3", "to invite; please", ["to wrap", "to divide", "to sit"]),
    ],
)

# ------------------------------------------------------------------ 9. skill integration
TF = [("我是韩国人,在中国上学。", "I am Korean and I go to school in China."), ("朋友的爸爸妈妈一起做菜。", "My friend’s father and mother cook together."), ("朋友的妈妈也会做菜。", "My friend’s mother can cook too."),
      ("我不好意思，因为我不会做菜。", "I feel embarrassed because I can’t cook."), ("今天很有意思，因为我吃了很好吃的中国菜。", "Today was interesting because I ate delicious Chinese food.")]
DUMP = ("我的老家在北京。中国北方人都很喜欢吃饺子。可是来美国以后，我就很少吃饺子了。上个周末，我请了几个同学一起包饺子。我们都不太会做饺子皮，所以饺子皮是买的。我们先做饺子馅儿，有肉馅儿，也有素菜鸡蛋馅儿。做完馅儿我们就开始包饺子。大家一边包一边笑，因为有的饺子真的太难看了！可是，味道还是挺不错的。我们每人吃了二十多个！大家都说，以后还要一起包饺子。不过，下次一定要自己做饺子皮。",
        "My hometown is in Beijing. Northern Chinese all like to eat dumplings very much. But since coming to America I rarely eat dumplings. Last weekend I invited a few classmates to wrap dumplings together. None of us is very good at making dumpling wrappers, so the wrappers were bought. We first made the filling, with meat filling and also vegetable and egg filling. After making the filling we began to wrap the dumplings. Everyone laughed while wrapping, because some of the dumplings really looked too ugly! But the taste was still quite good. We each ate more than twenty! Everyone said that in the future we will wrap dumplings together again. But next time we must make the wrappers ourselves.")
TASTE = ("每个地方的饭菜都有自己的特色。有人说，中国菜是南甜、北咸、东辣、西酸。意思是说南方人喜欢吃甜的，北方人喜欢吃咸的，东部的人爱吃辣的，西部的人爱吃酸的。不过，真正喜欢吃辣的人是在湖南、湖北、四川这些地方。喜欢吃辣和气候有关。这些地方一年四季很少有太阳，阴天多，雾也多。吃辣椒出汗，对身体很有好处。东北一些地区的人也喜欢吃辣，这是因为那里气候寒冷，吃完辣椒就暖和了。",
         "The food of every place has its own character. Some say that Chinese food is “south sweet, north salty, east spicy, west sour”. This means that southerners like sweet food, northerners like salty food, people in the east love spicy food, and people in the west love sour food. But the people who truly like spicy food are in places like Hunan, Hubei and Sichuan. Liking spicy food is related to the climate. In these places there is little sun all year round, with many overcast days and a lot of fog. Eating chili peppers makes you sweat, which is very good for the body. People in some parts of the northeast also like spicy food, because the climate there is cold, and after eating chili peppers you feel warm.")
KEYW = [("南甜、北咸、东辣、西酸", "south sweet, north salty, east spicy, west sour"), ("湖南、湖北、四川", "Hunan, Hubei, Sichuan"), ("气候", "climate"), ("吃辣椒出汗", "eating chili peppers makes you sweat"), ("东北，气候寒冷，暖和", "the northeast: cold climate, warm up")]
L9 = lesson(
    "Presentation 3 skill integration: true or false, dumplings and regional tastes",
    "我不好意思 · 饺子馅儿 · 一边包一边笑 · 南甜、北咸、东辣、西酸",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing and Reading): true or false",
             "A. Listen to the passage once, then write what you remember in pinyin or characters. B. Listen again and refine your notes. C. Decide whether the five statements are true or false based on the passage (the recording is not included, so the key cannot be given here). D. Discuss your answers with the class, then listen again to confirm or correct your understanding. The five statements:",
             examples=[D(z, e) for z, e in TF]),
        card("Activity 2 (Listening, Writing and Speaking)",
             "A. Listen to a dialog and complete a table: the people mentioned and their relationships, and what you learned about them (audio, not included). B. Pair up and ask each other questions in Chinese about the dialog to verify your notes."),
        card("Activity 3 (Reading and Speaking): making dumplings",
             "A. Read the passage and highlight the words you don’t know; try to work out their meaning from context. B. In groups of three, check your understanding of the words you highlighted. C. Identify the pictures (six, not included) that apply to the passage and discuss your choices with the group in Chinese.",
             examples=[D(*DUMP)]),
        card("Activity 4 (Reading, Writing and Speaking): regional tastes",
             "A. Read the passage and highlight the words you don’t know. B. In groups of three, check the terms you highlighted. C. Copy the keywords from the passage in the space provided and discuss your choice of key words with the group in Chinese. My choice of keywords:",
             examples=[D(*TASTE)] + [D(z, e) for z, e in KEYW]),
    ],
    exercises=[
        M("Dumplings passage: where is the speaker’s hometown?", "Beijing", ["Shanghai", "Sichuan", "Hunan"], "我的老家在北京。"),
        M("Dumplings passage: who likes dumplings very much?", "Northern Chinese", ["Southern Chinese", "Americans", "Only teachers"], "中国北方人都很喜欢吃饺子。"),
        M("Dumplings passage: why were the dumpling wrappers bought?", "They were not very good at making wrappers", ["Wrappers are free", "The shop was next door", "They had no flour"], "我们都不太会做饺子皮，所以饺子皮是买的。"),
        M("Dumplings passage: what fillings did they make?", "Meat filling and vegetable and egg filling", ["Only meat", "Only fish", "Only vegetables"], "有肉馅儿，也有素菜鸡蛋馅儿。"),
        M("Dumplings passage: why did everyone laugh while wrapping?", "Some of the dumplings looked really ugly", ["The movie was funny", "A teacher told a joke", "They were embarrassed"], "有的饺子真的太难看了！"),
        M("Dumplings passage: how did the dumplings taste?", "Still quite good", ["Terrible", "Too salty", "Too sweet"], "味道还是挺不错的。"),
        M("Dumplings passage: how many did each person eat?", "More than twenty", ["About five", "Exactly ten", "None"], "我们每人吃了二十多个！"),
        M("Dumplings passage: what is the plan for next time?", "Make the wrappers themselves", ["Buy more wrappers", "Order in a restaurant", "Never wrap again"], "下次一定要自己做饺子皮。"),
        M("Regional tastes: what does 南甜、北咸、东辣、西酸 say?", "South sweet, north salty, east spicy, west sour", ["South sour, north spicy", "All places are spicy", "Every place is sweet"], "A saying about regional tastes."),
        M("Which places really love spicy food?", "Hunan, Hubei and Sichuan", ["Beijing and Tianjin", "Shanghai and Hangzhou", "Guangdong and Fujian"], "湖南、湖北、四川这些地方。"),
        M("Why do people there eat spicy food?", "Liking spicy food is related to the climate: little sun, much fog, and chili makes you sweat", ["It is cheap", "It is a tradition of the army", "It is a religion"], "喜欢吃辣和气候有关。"),
        M("Why do some people in the northeast eat spicy food?", "The climate is cold, and chili peppers warm you up", ["It is hot there", "They have no other food", "It is a festival"], "吃完辣椒就暖和了。"),
        M("In the T/F statement 我不好意思，因为我不会做菜, what is the reason for embarrassment?", "The speaker can’t cook", ["The speaker is late", "The speaker is a guest", "The speaker is Korean"], "不会做菜."),
        F("做___馅儿，我们就开始包饺子。", "完", PART, "做完馅儿: finish making the filling."),
        F("大家一边包一___笑。", "边", PART, "一边…一边…"),
    ],
)

# ------------------------------------------------------------------ 10. using Chinese in context
CQ = [("这个菜叫什么名字？", "What is this dish called?"), ("你是在哪儿吃的？", "Where did you eat it?"), ("你是什么时候吃的？", "When did you eat it?"), ("这个菜的味道怎么样？", "How does this dish taste?"), ("你喜欢吗？为什么？", "Do you like it? Why?"), ("你知道这是中国哪个地方的特色菜吗？", "Do you know which place in China this specialty is from?")]
SAT = ("上周六，我九点才起床。起床以后，我先吃了早饭，然后开始做作业。做完作业，我去体育馆锻炼了一个小时。晚上，我和朋友们一起去看了一场电影。晚上十点我们才回学校。",
       "Last Saturday I did not get up until nine. After getting up, I first ate breakfast, and then started doing homework. After finishing my homework, I went to the gym and worked out for an hour. In the evening, my friends and I went to see a movie together. We didn’t return to school until ten at night.")
LABELS = [("最忙的一天", "zui4 mang2 de5 yi4 tian1", "the busiest day"), ("最有意思的一天", "zui4 you3 yi4 si5 de5 yi4 tian1", "the most interesting day"), ("最无聊的一天", "zui4 wu2 liao2 de5 yi4 tian1", "the most boring day"),
          ("最懒的一天", "zui4 lan3 de5 yi4 tian1", "the laziest day"), ("最轻松的一天", "zui4 qing1 song1 de5 yi4 tian1", "the most relaxing day"), ("最努力学习的一天", "zui4 nu3 li4 xue2 xi2 de5 yi4 tian1", "the day of the hardest study")]
L10 = lesson(
    "Presentation 3: using Chinese in context (a dish, interviews, a Saturday)",
    "这个菜叫什么名字？ · 做完作业 · 最有意思的一天 · 最懒的一天",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): a Chinese dish you have had",
             "A. Recall a Chinese dish or food you have had, then answer the six questions (check a dictionary if necessary). B. In groups of three, introduce this dish or food to your partners and explain any new words you use.",
             examples=[D(z, e) for z, e in CQ]),
        card("Activities 2 and 3: interview the instructors; plan a potluck",
             "Activity 2: interview some Chinese instructors about their hometown cuisine, the types of dishes they like to cook, and the dishes they would recommend from their favorite restaurant. A. As a class, generate six interview questions and write them in Chinese. B. Interview the instructors and take notes. C. Report your results to the class while the others take notes; your teacher will then ask the class questions about the interview. Activity 3: plan a Chinese potluck for the class from the interview results. A. Divide into two groups: Plan A, based on the dishes the instructors like to cook; Plan B, based on the dishes they recommended from their favorite restaurants. Each group presents its plan. B. Vote for the best plan."),
        card("Activity 4 (Reading, Writing and Speaking): last Saturday",
             "A. Write a short paragraph about what you did last Saturday using 先…然后, …以后 and V + 完. The book’s example:",
             examples=[D(*SAT)]),
        card("Activity 4, parts B to D: choose the label",
             "B. Tell the class what you did on Saturday, without looking at your paragraph unless you forget something. C. After listening to all your classmates’ reports, decide which of six labels best fits which report: the busiest day, the most interesting day, the most boring day, the laziest day, the most relaxing day, the day of the hardest study. D. Share your top picks with the class and explain them. New words: 有意思 interesting, 无聊 boring, 懒 lazy, 轻松 relaxing.",
             tables=[wtable(LABELS, title="The six labels")]),
    ],
    exercises=[
        M("In the example paragraph, when did the writer get up?", "At nine, which is late", ["At six, which is early", "At noon", "At five"], "我九点才起床。"),
        M("What did the writer do first after getting up?", "Ate breakfast", ["Did homework", "Went to the gym", "Saw a movie"], "起床以后，我先吃了早饭。"),
        M("What did the writer do after finishing homework?", "Worked out at the gym for an hour", ["Saw a movie", "Ate breakfast", "Went to sleep"], "做完作业，我去体育馆锻炼了一个小时。"),
        M("What did the writer do in the evening?", "Saw a movie with friends", ["Studied", "Cooked", "Went on duty"], "晚上，我和朋友们一起去看了一场电影。"),
        M("When did they return to school?", "Not until ten at night", ["At eight", "At noon", "At midnight"], "晚上十点我们才回学校。"),
        M("What does V + 完 show, as in 做完作业?", "The action is finished", ["The action is about to start", "The action is repeated", "The action is forbidden"], "完: finish, complete."),
        M("Which question asks for the name of a dish?", "这个菜叫什么名字？", ["你是在哪儿吃的？", "你喜欢吗？", "你是什么时候吃的？"], "叫什么名字: what is it called?"),
        M("Which question asks where you ate it?", "你是在哪儿吃的？", ["你是什么时候吃的？", "这个菜的味道怎么样？", "你喜欢吗？"], "在哪儿: where."),
        M("Which question asks how a dish tastes?", "这个菜的味道怎么样？", ["这个菜叫什么名字？", "你知道这是哪里的特色菜吗？", "你喜欢吗？"], "味道: taste."),
        M("Which label means “the laziest day”?", "最懒的一天", ["最忙的一天", "最无聊的一天", "最轻松的一天"], "懒 means lazy."),
        M("Which label means “the most boring day”?", "最无聊的一天", ["最懒的一天", "最忙的一天", "最有意思的一天"], "无聊 means boring."),
        M("Which label means “the most interesting day”?", "最有意思的一天", ["最无聊的一天", "最懒的一天", "最轻松的一天"], "有意思 means interesting."),
        F("做___作业，我去体育馆锻炼了一个小时。", "完", PART, "做完: finish doing."),
        F("上周六，我九点___起床。", "才", ["再", "给", "放"], "九点才: not until nine."),
        mean("轻松", "qing1 song1", "relaxing; relaxed", ["lazy", "boring", "busy"]),
    ],
)

# ------------------------------------------------------------------ 11. Area Studies
AS1 = ("Although written records only date back to 1250 BCE, China is popularly said to have “5,000 years of civilization.” Regardless, its venerable culinary tradition has always been an integral part of Chinese culture.\n\n"
       "In Chinese cuisine, food preparation is complex. Food is divided into fan (饭 fàn) and cai (菜 cài), fan being grains such as rice, and cai being vegetables and meat. Both ingredients are necessary for a balanced meal. To prepare cai, a cook must cut up and mix different ingredients to enhance their flavors and increase variety. Pork, for example, can be diced, shredded, or ground and combined with various other meats.\n\n"
       "Chinese cuisine can be basically divided into Southern and Northern styles. Southern cuisine emphasizes freshness and tenderness, while Northern dishes tend to be richer in oil and reliant on vinegar and garlic. The four oldest types of Chinese food are Sichuanese, Cantonese, Northern, and Huaiyang. Eventually, eight types of Chinese cuisine evolved, each of which has its own distinct history and characteristics. Many Chinese dishes are named after historical figures, such as 东坡肉 (dōngpōròu, steamed pork shoulder), the favorite dish of Song dynasty poet 苏东坡; 贵妃鸡 (guìfēijī, Imperial Concubine Chicken), named after the Tang dynasty courtesan, 杨贵妃; and the spicy 左宗棠鸡 (zuǒzōngtángjī, General Zuo’s Chicken), named for the Qing dynasty Hunanese general, 左宗棠.")
AS2 = ("Chinese food involves stir-frying, deep-frying, steaming, stewing or roasting. Stir-frying is the most common and entails quick cooking over high heat with a small amount of oil. With this method, meat stays juicy and vegetables remain crisp. Chinese people are very conscious of what they eat and enjoy nutritious food from the vegetable, herb and fungi kingdoms; in fact, many foods are specifically prepared for disease prevention and cure. As both science and art, Chinese cuisine also prescribes how different foods should be cooked and prepared for optimal health.")
AS3 = ("Alcohol, of course, is also a part of traditional Chinese culture. It plays an important role in birthday parties for adults, wedding feasts, business banquets, and even ceremonial offerings at ancestral gravesites. Naturally, it is also part of daily life. In restaurants or bars, for example, people play drinking games, like the “finger guessing game” (划拳 or 猜拳). A little like “paper, scissors, rock,” two players each throw out a Chinese hand sign for a number from zero to ten while one of them calls a number out loud. If the combined sign numbers add up to the “caller’s” number, he wins and the loser has to drink. There are many other drinking games that involve telling jokes, riddles, or playing on Chinese customs or poetry.\n\n"
       "Alcohol also features prominently in Chinese art and literature. In general, Chinese people consider moderate drinking healthy and now imbibe a wide variety of liquor, wine and beer. The most famous Chinese liquors are Maotai, Fenjiu, and Wuliangye. The foremost three wines are Great Wall Wine, Dynasty Wine and Changyu Wine. The top three beers are China Resources Beer, Tsingtao and AB InBev.")
AS4 = ("China has cultivated tea for over three thousand years. It is an integral part of Chinese culture and cuisine. Legend has it that tea was introduced to China by the mythical emperor and herbalist Shénnóng 神农 in 2737 BC. There are five major types: green tea, Oolong tea, jasmine tea, black tea and compressed tea. These teas are classified according to the different ways they are processed. For example, green tea is not fermented to preserve the original color, fragrance and flavor of the leaves. The three finest teas in China are considered to be West Lake Longjing, Dahongpao and Tieguanyin.\n\n"
       "Tea is the most important daily beverage in China, valued for both its health properties and its salient role in social customs and ceremony. Chinese people believe that tea cools and relaxes by dispelling heat from the body, so teahouses abound in cities, towns and villages, where locals often meet to chat over a cup of tea. An ancient Chinese proverb says, “Better to go without salt for three days than without tea for a single day.”\n\n"
       "Chinese tea has been internationally renowned for centuries. The world’s largest tea producer, China exported $2 billion worth of tea in 2019, 31.8% of the global market share.")
NAMES = [("东坡肉", "steamed pork shoulder (Dongpo pork)"), ("贵妃鸡", "Imperial Concubine Chicken"), ("左宗棠鸡", "General Zuo’s Chicken"), ("划拳", "the finger guessing game"), ("猜拳", "the finger guessing game (another name)"),
         ("茅台酒", "Maotai liquor"), ("汾酒", "Fenjiu liquor"), ("五粮液", "Wuliangye liquor"), ("长城葡萄酒", "Great Wall Wine"), ("王朝葡萄酒", "Dynasty Wine"), ("张裕葡萄酒", "Changyu Wine"),
         ("华润雪花", "China Resources Beer"), ("青岛啤酒", "Tsingtao beer"), ("百威英博", "AB InBev"), ("神农", "Shennong, the mythical emperor and herbalist"), ("西湖龙井", "West Lake Longjing tea"), ("大红袍", "Dahongpao tea"), ("铁观音", "Tieguanyin tea")]
L11 = lesson(
    "Area Studies: Food in Chinese Culture",
    "饭 and 菜 · eight cuisines · stir-frying · alcohol · tea",
    requires=[],
    cards=[card("Food in Chinese Culture (1): fan and cai, and the regional styles", AS1),
           card("Food in Chinese Culture (2): cooking methods", AS2),
           card("Alcohol", AS3, tables=[wtable(rows_py(NAMES[:14]), title="Names in the reading (1)")]),
           card("Tea", AS4 + "\n\nThe book’s photos (ZQ, Wikimedia, Freepik) are not included.", tables=[wtable(rows_py(NAMES[14:]), title="Names in the reading (2)")])],
    exercises=[
        M("What are the two parts of a Chinese meal?", "Fan (grains such as rice) and cai (vegetables and meat)", ["Soup and dessert", "Meat and fish", "Tea and alcohol"], "Both are necessary for a balanced meal."),
        M("What does 饭 refer to in this reading?", "Grains such as rice", ["Vegetables and meat", "Soup", "Tea"], "fan being grains such as rice."),
        M("How do Southern and Northern cuisines differ?", "Southern emphasizes freshness and tenderness; Northern is richer in oil and relies on vinegar and garlic", ["Southern is spicier", "Northern uses no oil", "There is no difference"], "Southern cuisine emphasizes freshness and tenderness."),
        M("How many types of Chinese cuisine eventually evolved?", "Eight", ["Four", "Six", "Ten"], "The four oldest types, then eight in all."),
        M("Which are the four oldest types?", "Sichuanese, Cantonese, Northern and Huaiyang", ["Hunan, Hubei, Fujian and Zhejiang", "Beijing, Shanghai, Tianjin and Chongqing", "Sweet, salty, spicy and sour"], "The four oldest types of Chinese food."),
        M("After whom is 贵妃鸡 named?", "The Tang dynasty courtesan 杨贵妃", ["The poet 苏东坡", "The general 左宗棠", "The emperor 神农"], "named after the Tang dynasty courtesan."),
        M("What is 东坡肉 and whose favorite was it?", "Steamed pork shoulder, the favorite of the Song poet 苏东坡", ["Roast duck, the favorite of an emperor", "Spicy chicken, the favorite of a general", "Fried rice, the favorite of a monk"], "东坡肉 (dōngpōròu)."),
        M("Which is the most common cooking method?", "Stir-frying", ["Deep-frying", "Steaming", "Roasting"], "Stir-frying is the most common."),
        M("What does stir-frying do for meat and vegetables?", "Meat stays juicy and vegetables remain crisp", ["Meat becomes dry", "Vegetables become soft", "Both are boiled"], "Quick cooking over high heat with a small amount of oil."),
        M("In the finger guessing game, who drinks?", "The loser", ["The winner", "Both players", "The caller always"], "The loser has to drink."),
        M("Which are the three most famous Chinese liquors?", "Maotai, Fenjiu and Wuliangye", ["Great Wall, Dynasty and Changyu", "Tsingtao, China Resources and AB InBev", "Longjing, Dahongpao and Tieguanyin"], "茅台酒, 汾酒, 五粮液."),
        M("Which is the first of the top three beers?", "China Resources Beer (华润雪花)", ["Tsingtao (青岛啤酒)", "AB InBev (百威英博)", "Great Wall"], "华润雪花, 青岛啤酒, 百威英博."),
        M("How long has China cultivated tea, and who introduced it, by legend?", "Over three thousand years; the mythical emperor Shennong in 2737 BC", ["One hundred years; a Tang poet", "Five hundred years; a general", "Over ten thousand years; a monk"], "Legend has it that tea was introduced by 神农 in 2737 BC."),
        M("How many major types of tea are there?", "Five: green, Oolong, jasmine, black and compressed", ["Three", "Eight", "Two"], "There are five major types."),
        M("Which are considered the three finest teas?", "West Lake Longjing, Dahongpao and Tieguanyin", ["Maotai, Fenjiu and Wuliangye", "Green, black and jasmine", "Oolong, compressed and white"], "西湖龙井, 大红袍, 铁观音."),
        M("What does the ancient proverb say about tea?", "Better to go without salt for three days than without tea for a single day", ["Tea is better than wine", "Tea cools the head", "Never drink tea at night"], "The proverb is quoted at the end of the second tea paragraph."),
        M("How much tea did China export in 2019?", "$2 billion worth, 31.8% of the global market", ["$20 billion, 80%", "$200 million, 5%", "$2 billion, 3%"], "The world’s largest tea producer."),
    ],
)

# ------------------------------------------------------------------ 12. vocabulary
L12 = vocab_lesson("Presentation 3 vocabulary (23 words)", "做饭 · 做菜 · 愉快 · 味道 · 素菜 · 麻婆豆腐 · 会 · 吃素 · 包",
                   "Vocabulary list (Presentation 3)",
                   "The book’s 23 words, with the traditional form where it differs.", VOC3)

UNIT = unit("第八课 中国食品与餐馆 Presentation 3: Cooking Day, 就 and 才, 了, 一边…一边…, 会, and Food in Chinese Culture", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
