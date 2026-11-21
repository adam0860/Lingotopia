"""Unit 40: Lesson 14 (Leisure Travel) Presentation 2 from the book's texts: the Xi'an trip dialog, 什么 + 吗, the rhetorical
question with 什么, the exclamatory 多/多么…啊, 还是 for preference, the skill-integration tour brochures, the using-Chinese
activities and the vocabulary list. Audio, pictures and websites are not included; the book writes numbers as digits and they
are spelled out here so that every spoken line is Chinese; answer keys the book does not print are mine."""
from zh_auto import *
from zh_l14_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("长大", 0, "zhang3"), ("称为", 1, "wei2"), ("半只", 1, "zhi1"), ("朝阳", 0, "chao2"), ("种有", 0, "zhong4"),
                          ("起价为", 2, "wei2"), ("统一为", 2, "wei2"), ("成为", 1, "wei2"), ("作为", 1, "wei2"), ("睡什么觉", 3, "jiao4"), ("睡觉", 1, "jiao4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for k in ("得做", "得需", "得带", "得花", "得坐", "得先", "得去", "得买", "得复习"):
        j = zh.find(k)
        while j >= 0:
            f[j] = "dei3"
            j = zh.find(k, j + 1)
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P2 = [("大卫", "暑假快到了，你有什么打算吗？", "Summer vacation is coming; do you have any plans?"),
      ("马克", "有啊。我打算和几个朋友一起开车去西安看看。", "Yes. I plan to drive to Xi’an with a few friends to have a look."),
      ("大卫", "为什么去那儿呢？", "Why go there?"),
      ("马克", "西安是中国有名的古都，到处都是名胜古迹。", "Xi’an is a famous ancient capital of China; there are scenic spots and historical sites everywhere."),
      ("大卫", "比如说……", "For example…"),
      ("马克", "比如兵马俑，大雁塔什么的，都非常值得一看。", "For example the Terracotta Army, the Big Wild Goose Pagoda and so on; all are well worth seeing."),
      ("大卫", "从北京开车到西安，大概需要多长时间？", "Driving from Beijing to Xi’an, about how long does it take?"),
      ("马克", "十二三个小时吧。", "Twelve or thirteen hours, I’d say."),
      ("大卫", "你怎么不参加旅行团呢？", "Why not join a tour group?"),
      ("马克", "参加旅行团有什么没意思啊。大家都去一样的地方，照一样的照片。", "What’s the fun in joining a tour group? Everyone goes to the same places and takes the same photos. (The traditional-character version prints 有什么意思啊, “what’s the fun”.)"),
      ("大卫", "那，你觉得怎么去好？", "Then, how do you think is best to go?"),
      ("马克", "自己去。你可以选喜欢的路线，还可以住民宿，和当地人聊天，多自由呀。", "Go on your own. You can choose the route you like, stay in a home stay and chat with locals; how free that is!"),
      ("大卫", "可是，自己做旅行计划太麻烦了。像我这样的懒人还是参加旅行团比较方便！", "But making your own travel plans is too troublesome. For a lazy person like me, joining a tour group is more convenient!"),
      ("马克", "那倒也是。导游帮你订旅馆、买门票，你什么事都不用做，只要跟着导游走就行了。", "That’s true. The guide books hotels and buys tickets for you; you don’t need to do anything, just follow the guide."),
      ("大卫", "我就是这么想的。", "That’s just what I was thinking.")]
L1 = lesson(
    "Lesson 14 Presentation 2: a trip to Xi’an",
    "你怎么不参加旅行团呢？ · 自己去，多自由呀 · 那倒也是",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. What famous historical sites have you visited? Where are they? B. When you travel, do you prefer traveling alone or in a group? Why? C. What is your next travel plan? Share your destination, tentative time, mode of transportation, etc."),
        card("Presentation 2: 去西安",
             "The book also prints the dialog in traditional characters. Notes: 像. 像 is used to compare a specific characteristic between two things or people. It means “just like.” 倒. 倒 is used to concede a point or admit you were wrong. 那倒也是 means “I guess so; I hadn’t thought of it like that before.”",
             examples=dlg(P2)),
        card("Activities 1 and 2",
             "Activity 1 (Listening and Speaking). A. Global listening: 1. What would be an appropriate title for this presentation? 2. What does each speaker prefer? B. Detail listening: 1. What is the second speaker’s plan? Why does the speaker plan to do that? 2. What is the first speaker’s suggestion? Does the second speaker like the idea? Why? 3. List three advantages of the second speaker’s preferences. 4. What are the advantages of the first speaker’s preferences? (Audio, not included. From the text: Mark plans to drive to Xi’an because it is an ancient capital full of sights; Mark prefers traveling on his own for freedom, routes and local contact; David prefers a tour group because it is convenient.) Activity 2 (Reading, Writing, Speaking and Listening). A. Before traveling you need a travel plan. Consider all the aspects and write the details in the diagram in Chinese characters: 旅行计划 with 目的地, 交通, 住宿, 时间, 旅行方式, 活动. B. Share your diagram with a classmate. C. Your teacher will check the characters. (The book leaves the diagram blank.)"),
    ],
    exercises=[
        M("What does Mark plan to do this summer?", "Drive to Xi’an with a few friends", ["Fly to Shanghai", "Join a tour group", "Stay in Beijing"], "开车去西安看看。"),
        M("Why does Mark want to go to Xi’an?", "It’s a famous ancient capital full of historical sites", ["It is near", "It is cheap", "He has family there"], "西安是中国有名的古都。"),
        M("Which sights does Mark name?", "The Terracotta Army and the Big Wild Goose Pagoda", ["The Great Wall", "The Forbidden City", "The West Lake"], "兵马俑，大雁塔。"),
        M("How long does the drive from Beijing take?", "About twelve or thirteen hours", ["About two hours", "About a week", "About thirty hours"], "十二三个小时。"),
        M("Why doesn’t Mark want a tour group?", "Everyone goes to the same places and takes the same photos", ["It is too expensive", "It is dangerous", "He is allergic to crowds"], "大家都去一样的地方，照一样的照片。"),
        M("What can you do traveling independently, according to Mark?", "Choose your route, stay in a home stay, chat with locals", ["Get free tickets", "Avoid all costs", "Skip the sights"], "选喜欢的路线，住民宿，和当地人聊天。"),
        M("Why does David prefer a tour group?", "He is lazy and it is convenient", ["It is cheaper", "He knows the guide", "He dislikes Xi’an"], "像我这样的懒人还是参加旅行团比较方便！"),
        M("What does a guide do, according to Mark?", "Books hotels and buys tickets; you just follow", ["Pays for the trip", "Drives the car", "Takes photos for you"], "导游帮你订旅馆、买门票。"),
        M("What does 那倒也是 mean?", "That’s true; I hadn’t thought of it that way", ["That is not true", "That is also dumb", "Let’s go also"], "倒 concedes a point."),
        M("What does 像 mean in 像我这样的懒人?", "Like; such as", ["Photo", "Elephant", "Resemble in face"], "像: just like."),
        mean("导游", "dao3 you2", "tour guide", ["tourist", "driver", "waiter"]),
        F("西安是中国有名的古___。", "都", PART, "古都: ancient capital."),
    ],
)

# ------------------------------------------------------------------ 2. activities 3 to 5
Q3 = [("周末快到了，你有什么打算？", "d", "我计划开车去旧金山。", "What are your plans? / I plan to drive to San Francisco."), ("北京有什么名胜古迹？", "a", "天安门，故宫，长城什么的。", "What historic sites does Beijing have? / Tiananmen, the Forbidden City, the Great Wall and so on."),
      ("从南京坐高铁到上海大概需要多长时间？", "b", "只要一个小时。", "How long does it take by high-speed rail from Nanjing to Shanghai? / Only an hour."), ("你怎么不参加旅行团？", "e", "那么多人去同样的地方，没意思。", "Why not join a tour group? / So many people go to the same place; it’s boring."),
      ("你觉得怎么住好？", "c", "民宿呀，可以和当地人聊天。", "What kind of lodging is best? / A home stay, you can chat with locals.")]
LD = [("林东", "大卫，还有两个星期暑假就到了，你有什么打算吗？", "David, summer vacation is only two weeks away; do you have any plans?"), ("大卫", "有啊。我跟几个美国来的朋友打算一起坐高铁去郑州玩玩。", "Yes. A few friends from America and I plan to take the high-speed train to Zhengzhou."),
      ("林东", "你们为什么想要去那儿呢？", "Why do you want to go there?"), ("大卫", "我们都喜欢中国的功夫电影，想到少林寺去看看。", "We all like Chinese kung fu movies and want to see the Shaolin Temple."),
      ("林东", "好主意。郑州跟西安一样，也是有名的古都。你们还可以去看看别的名胜古迹。", "Good idea. Zhengzhou, like Xi’an, is also a famous ancient capital. You can also see other sights."), ("大卫", "比如说……", "For example…"),
      ("林东", "比如说，龙门石窟、云台山什么的，都非常值得一看。", "For example the Longmen Grottoes, Yuntai Mountain and so on are all well worth a look."), ("大卫", "从北京坐高铁到郑州，大概需要多长时间？", "How long does it take by high-speed train from Beijing to Zhengzhou?"),
      ("林东", "最快的大概两个半小时就到了。", "The fastest takes about two and a half hours."), ("大卫", "那么快啊，太好了。对了，我怎么订旅馆最好？", "That fast? Great. By the way, what’s the best way to book a hotel?"),
      ("林东", "你要自己订旅馆啊？多麻烦啊！怎么不参加旅行团呢？导游可以帮你们订旅馆、买门票，你自己呢什么事都不用做，只要跟着导游走就好了。", "You want to book hotels yourself? How troublesome! Why not join a tour group? The guide can book hotels and buy tickets for you; you don’t have to do anything, just follow the guide."),
      ("大卫", "参加旅行团有什么意思啊，大家去的地方一样，连照的照片都一样。而且那是年纪大的人喜欢的。", "What’s the fun in a tour group? Everyone goes to the same places, even the photos are the same. Besides, that’s what older people like."),
      ("林东", "那，你觉得怎么旅游最好呢？", "Then how do you think is the best way to travel?"),
      ("大卫", "自己去，我和我的朋友们都特别喜欢自由行。不仅可以选自己喜欢的路线，还可以住民宿，和当地人聊天、吃当地的饭，多有意思啊。", "Go on my own; my friends and I all especially like independent travel. Not only can we choose our own route, we can also stay in a home stay, chat with locals and eat local food. How interesting!"),
      ("林东", "可是，自己做旅行计划，订旅馆，买火车票，这也太麻烦了，不适合我这样的懒人。我还是喜欢旅行团。", "But making your own travel plans, booking hotels, buying train tickets, is too troublesome and doesn’t suit a lazy person like me. I still prefer tour groups."),
      ("大卫", "那倒也是。你是挺懒的！哈哈，我开玩笑呢。", "That’s true. You are quite lazy! Ha ha, I’m joking.")]
TB5 = [("谁", "大卫和几个美国朋友"), ("时间", "暑假，还有两个星期"), ("目的地", "郑州：少林寺、龙门石窟、云台山"), ("交通", "高铁，北京到郑州最快两个半小时"), ("活动", "看功夫电影里的少林寺，游览名胜古迹"), ("住宿", "住民宿，自己订"), ("旅行方式", "自由行"), ("订票", "自己订")]
L2 = lesson(
    "Lesson 14 Presentation 2 activities: matching and the Zhengzhou conversation",
    "高铁去郑州 · 少林寺 · 龙门石窟 · 跟团游还是自由行",
    requires=[],
    cards=[
        card("Activity 3 (Reading and Speaking)",
             "Match each question with its most likely answer. The questions: 1. 周末快到了，你有什么打算？ 2. 北京有什么名胜古迹？ 3. 从南京坐高铁到上海大概需要多长时间？ 4. 你怎么不参加旅行团？ 5. 你觉得怎么住好？ The answers: a. 天安门，故宫，长城什么的。 b. 只要一个小时。 c. 民宿呀，可以和当地人聊天。 d. 我计划开车去旧金山。 e. 那么多人去同样的地方，没意思。 My matching (mine): 1-d, 2-a, 3-b, 4-e, 5-c."),
        card("Activity 4 (Listening and Speaking)",
             "A. Listen to the dialog once and choose the best answer: 1. What is the relationship between the two speakers? (Student and teacher / Two teachers / Father and son / Two students) 2. What is the topic of this dialog? (Travel plans during Spring Festival / Transportation in Taiwan and China / Scenery on the outskirts of Taipei / Services provided by a travel agency) B. Listen again and decide whether each statement is true or false; in groups of three discuss your answers: 1. The second speaker plans to travel to Taipei, Taizhong and Taidong. 2. The second speaker plans to go to Chinatown in San Francisco and dine with their parents. 3. The second speaker is going on a long-distance bus ride and a high-speed train ride. 4. The second speaker has booked their flight tickets and train tickets. 5. The first speaker’s family plans to travel together next summer. 6. The first speaker gave the second speaker a website address. (Audio, not included, so no key.)"),
        card("Activity 5 (Reading, Speaking and Listening): Students 1, 2 and 3",
             "A. Work in groups of three. Each student reads one part of a conversation between two friends (Student 1: the first seven lines up to 云台山; Student 2: from 从北京坐高铁到郑州 to the “年纪大的人喜欢的” line; Student 3: from 那，你觉得怎么旅游最好呢？ to the end) and summarizes it in their own words. B. Share your summary with your group. C. Complete the table with the information from each other. D. Pair up with a new partner and read the complete conversation aloud; compare the preferences of the two speakers. The complete conversation:",
             examples=dlg(LD)),
        card("Activity 5 table (旅行计划)",
             "The book’s table has the rows 谁, 时间, 目的地, 交通, 活动, 住宿, 旅行方式 and 订票 for you to fill in. My completed table from the conversation (mine):",
             tables=[table(["项目", "内容"], [(a, b) for a, b in TB5], title="旅行计划 (mine)", say=[0, 1])]),
    ],
    exercises=[
        M("Match: 北京有什么名胜古迹？", "天安门，故宫，长城什么的。", ["只要一个小时。", "民宿呀。", "我计划开车去旧金山。"], "2→a."),
        M("Match: 你怎么不参加旅行团？", "那么多人去同样的地方，没意思。", ["只要一个小时。", "天安门，故宫，长城什么的。", "民宿呀。"], "4→e."),
        M("Match: 你觉得怎么住好？", "民宿呀，可以和当地人聊天。", ["我计划开车去旧金山。", "只要一个小时。", "那么多人去同样的地方。"], "5→c."),
        M("Where do David and his friends plan to go?", "Zhengzhou", ["Xi’an", "Shanghai", "Guilin"], "去郑州玩玩。"),
        M("Why do they want to go to Zhengzhou?", "They like kung fu movies and want to see the Shaolin Temple", ["They have relatives there", "It is by the sea", "They want to shop"], "喜欢中国的功夫电影，想到少林寺去看看。"),
        M("How long does the fastest train from Beijing to Zhengzhou take?", "About two and a half hours", ["About twelve hours", "About one hour", "About a day"], "最快的大概两个半小时。"),
        M("What does Lin Dong think of independent travel?", "Too troublesome; he prefers a tour group", ["He loves it", "He has never heard of it", "It is too expensive"], "我还是喜欢旅行团。"),
        M("What does David think of tour groups?", "Boring, the photos are all the same, and for older people", ["Great and cheap", "The only safe way", "Only for students"], "参加旅行团有什么意思啊。"),
        M("What does 自由行 mean?", "Independent travel", ["Free tickets", "Tour group", "Business trip"], "自由行."),
        M("What is Lin Dong accused of?", "Being quite lazy (jokingly)", ["Being late", "Being rude", "Being rich"], "你是挺懒的！我开玩笑呢。"),
        F("我跟几个美国来的朋友打算一起坐高___去郑州玩玩。", "铁", PART, "高铁: high-speed rail."),
        F("郑州跟西安一样，也是有名的古___。", "都", PART, "古都."),
    ],
)

# ------------------------------------------------------------------ 3. 什么 + 吗
SM = [("你有什么打算吗？", "Do you have any plan? (softer; vs. 你有打算吗？)"), ("你有打算吗？", "Do you have a plan? (plain yes/no question)"), ("您买什么吗？", "Are you buying anything? (vs. 您买什么？ What are you buying?)"), ("您买什么？", "What are you buying?"), ("你有什么想法吗？", "Do you have any ideas? (softer; vs. 你有什么想法？ What are your ideas?)"), ("你有什么想法？", "What are your ideas?")]
SM1 = [("暑假快到了，你有什么打算吗？", "Summer vacation is around the corner. Do you have a plan or not? (the speaker does not know if “you” have a plan)"), ("暑假快到了，你有什么打算？", "Summer vacation is around the corner. What’s your plan? (the speaker is certain “you” have a plan but wants to know what kind)"), ("暑假快到了，你有打算吗？", "Summer vacation is around the corner; do you have a plan? (plain)"), ("暑假快到了，你有什么打算吗？", "(the same, with 什么 + 吗: softer and more polite)")]
SMX = [("你想吃什么吗？", "(mine) Is there anything you’d like to eat? (soft offer)"), ("你想吃什么？", "(mine) What do you want to eat?"), ("你最近有什么事吗？", "(mine) Is something going on with you lately?"), ("你最近有什么事？", "(mine) What is going on with you lately?")]
L3 = lesson(
    "Lesson 14 Presentation 2 grammar: 什么 + 吗",
    "你有什么打算吗？ · 您买什么吗？ · 什么 + 吗 softens the question",
    requires=[],
    cards=[
        card("什么 + 吗",
             "In Chinese, when a question word 什么 is used in a sentence together with 吗, the sentence is not asking for the information that the question word indicates any more, but rather the information that the main verb indicates. In practice, “什么 + 吗” softens the tone of asking. Compare 暑假快到了，你有打算吗？ and 暑假快到了，你有什么打算吗？ The second one sounds softer in tone and more polite.",
             examples=[D(z, e) for z, e in SM1]),
        card("Examples",
             "Examples with and without 什么: 1. 你有什么打算吗？ vs. 你有打算吗？ 2. 您买什么吗？ vs. 您买什么？ 3. 你有什么想法吗？ vs. 你有什么想法？",
             examples=[D(z, e) for z, e in SM]),
        card("Activities 1 and 2",
             "Activity 1 (Writing, Speaking and Listening). A. Work in groups of three. Each student writes two sentences in Chinese: one a regular 什么 question and the other a 什么 + 吗 question; think about the meaning of your sentences. B. Share your sentences with your two partners and compare their meanings. My samples:",
             examples=[D(z, e) for z, e in SMX]),
        card("Activity 2 (Listening and Speaking)",
             "A. Listen to the three sentences and write the English translation of each in the table; share your answers with a classmate. B. Work in pairs and take turns answering the questions you just heard in Chinese. C. Read the scripts if needed. (Audio, not included.)"),
    ],
    exercises=[
        M("What does 什么 + 吗 do?", "Asks about the verb’s information and softens the tone", ["Asks about the object", "Makes a command", "Makes a negative"], "什么 + 吗 softens."),
        M("Which is the softer, more polite version?", "你有什么打算吗？", ["你有打算吗？", "你有什么打算？", "你打算什么？"], "Softer."),
        M("What does 你有什么打算？ expect?", "A description of the plan (the speaker is sure there is one)", ["A yes or no", "A refusal", "Silence"], "Information question."),
        M("What does 你有什么打算吗？ ask?", "Whether you have a plan at all", ["What your plan is", "When you plan", "Where you plan"], "Verb information."),
        M("What does 您买什么吗？ ask?", "Are you buying anything?", ["What are you buying?", "Why are you buying?", "Who is buying?"], "什么 + 吗."),
        M("What does 你有什么想法吗？ ask?", "Do you have any ideas?", ["What is your idea?", "Where is your idea?", "Who has ideas?"], "什么 + 吗."),
        M("What does 什么 stop meaning in 什么 + 吗?", "“What” as a request for specific information", ["“Not”", "“Many”", "“Yes”"], "No longer asking for the thing."),
        F("暑假快到了，你有什么打算___？", "吗", ["们", "呢", "呀"], "什么 + 吗."),
        F("你有什么想法___？", "吗", ["们", "了", "过"], "什么 + 吗."),
    ],
)

# ------------------------------------------------------------------ 4. rhetorical question
RQ = [("参加旅行团有什么意思啊？大家都去一样的地方，照一样的照片。", "What is the fun in joining a tour? Everyone goes to the same place and takes the same pictures. (There is no fun in joining a tour.)"), ("今天是星期五，去什么体育馆呀？", "Today is Friday; why would we go to the gym? (We should not have to go to the gym on Friday.)")]
RQ2 = [("你开什么玩笑啊？你打了我，还要我跟你说“对不起”？", "What kind of joke is this? You hit me, and you still want me to say “sorry” to you?"), ("你没钱，请我吃什么饭啊？", "You have no money; what are you inviting me to dinner for?"), ("还看什么电影啊？要考试了，得复习功课。", "Why watch a movie? There’s an exam coming; we have to review."), ("今天是星期五，去什么体育馆呀？", "It’s Friday, why go to the gym?"), ("如果你都不可以说自己想说的话，还有什么自由呢？", "If you can’t even say what you want to say, what freedom is there?")]
W3 = [("睡觉", "还睡什么觉啊？天都亮了，快起床！", "Why still sleep? It’s already light; get up!"), ("去图书馆", "去什么图书馆啊？图书馆今天不开门。", "Why go to the library? It isn’t open today."), ("学中文", "学什么中文啊？这么难，我不学了！", "Why study Chinese? It’s so hard, I quit!"), ("聊天", "聊什么天啊？明天就考试了。", "Why chat? The exam is tomorrow."), ("兑换人民币", "兑换什么人民币啊？这儿可以用手机付钱。", "Why exchange RMB? You can pay with a phone here."),
      ("上网", "上什么网啊？网络坏了。", "Why go online? The network is down."), ("买新皮鞋", "买什么新皮鞋啊？你有那么多双。", "Why buy new leather shoes? You have so many pairs."), ("付现金", "付什么现金啊？可以刷卡。", "Why pay cash? You can use a card."), ("做饭", "做什么饭啊？我们去饭馆吃吧。", "Why cook? Let’s eat out."), ("坐公共汽车", "坐什么公共汽车啊？这么堵，走路更快。", "Why take the bus? With this jam, walking is faster.")]
ARG = [("丈夫", "你买什么买啊？家里的衣服已经够多了！", "What are you buying for? We already have enough clothes at home!"), ("妻子", "你说什么呢？这件衣服才打五折！", "What are you saying? This piece is only half price!"), ("丈夫", "打五折也是钱啊，还买什么买呢？", "Half price is still money. Why buy it?"), ("妻子", "好了好了，我不买了。你生什么气啊！", "OK OK, I won’t buy it. What are you getting angry for!")]
L4 = lesson(
    "Lesson 14 Presentation 2 grammar: the rhetorical question with 什么",
    "有什么意思啊？ · 去什么体育馆呀？ · 还有什么自由呢？",
    requires=[],
    cards=[
        card("The Rhetorical Question with 什么 (+ Object) + 啊/呢/呀?",
             "A rhetorical question is asked without expecting a direct answer—when the speaker already has an opinion on the topic and doesn’t expect an answer. In Chinese, adding 啊 after 什么 (noun) can change a question sentence into a rhetorical question. This usage is usually followed or preceded by a clause that states the reasons. These kinds of rhetorical questions are more likely to occur between friends, or two people who are familiar with each other. Pattern: Verb + 什么 (+ Object) + 啊/呢/呀？",
             examples=[D(z, e) for z, e in RQ]),
        card("Examples",
             "Examples 1 to 5:",
             examples=[D(z, e) for z, e in RQ2]),
        card("Activity 3 (Reading and Speaking)",
             "Work in pairs. Take turns picking one Chinese word from the list (睡觉, 去图书馆, 学中文, 聊天, 兑换人民币, 上网, 买新皮鞋, 付现金, 做饭, 坐公共汽车) and using it to create a rhetorical question with 什么. Share your questions with the class. My sample for each word (mine):",
             examples=[D(z, e) for _, z, e in W3]),
        card("Activity 4 (Speaking, Writing and Listening): Good and Bad Arguments",
             "A. Work in pairs. Choose one of the scenarios (an argument between husband and wife; an argument between two friends; a disagreement between a customer and a salesperson; a disagreement between two colleagues) and write a dialog expressing an argument between two people, using rhetorical questions with 什么 in as many different ways as you can. B. Share your work with the class by acting out your dialog. My sample, husband and wife (mine):",
             examples=dlg(ARG)),
    ],
    exercises=[
        M("What is a rhetorical question?", "A question asked without expecting an answer", ["A question asking for time", "A polite request", "A yes/no question"], "Rhetorical."),
        M("What does 参加旅行团有什么意思啊？ really mean?", "There is no fun in joining a tour", ["Joining a tour is very fun", "Where is the tour?", "What is the tour?"], "No fun."),
        M("What does 去什么体育馆呀？ imply?", "We shouldn’t go to the gym", ["Which gym should we go to?", "The gym is closed", "I love the gym"], "Rhetorical."),
        M("What does 你开什么玩笑啊？ imply?", "You can’t be serious", ["Tell me a joke", "I like jokes", "Joke again"], "Rhetorical."),
        M("What does 你没钱，请我吃什么饭啊？ imply?", "You shouldn’t treat me when you have no money", ["What food do you offer?", "Let’s eat", "Where shall we eat?"], "Rhetorical."),
        M("What does 还看什么电影啊？要考试了 imply?", "Don’t watch a movie; there is an exam coming", ["Which movie shall we watch?", "Let’s watch a movie", "The exam is over"], "Rhetorical."),
        M("What does 还有什么自由呢？ imply?", "There is no freedom left", ["What freedom shall we have?", "We have much freedom", "Where is freedom?"], "Rhetorical."),
        M("Between whom is this usage typical?", "Friends or people who know each other well", ["Strangers", "Teacher to student only", "Bosses to employees only"], "Familiar speakers."),
        F("你没钱，请我吃什么饭___？", "啊", ["们", "吗", "过"], "什么…啊."),
        F("还看什么电影啊？要考试了，得复习功___。", "课", PART, "功课: schoolwork."),
    ],
)

# ------------------------------------------------------------------ 5. 多 exclamatory
DUO = [("自己去，你可以选自己喜欢的路线，还可以住民宿，和当地人聊天，多自由呀！", "Go on your own: you can choose the route you like, stay in a home stay and chat with locals; how free that is!"), ("今天的天气多美啊！", "How beautiful the weather is today!"), ("姐姐新买的衣服多么漂亮啊！", "How pretty the clothes my sister just bought are!"), ("做饭日那天，大家多么高兴啊！", "How happy everyone was on cooking day!"),
       ("那位老大爷七十多岁了，身体多好呀！", "That old gentleman is over seventy; how good his health is!"), ("我多么喜欢学习中文啊！", "How much I like studying Chinese!"), ("先生告诉太太说，“我多爱你啊！”", "The husband told his wife, “How much I love you!”"), ("我多想旅行全世界，到每个国家看看啊。", "How I’d love to travel the whole world and visit every country!")]
DUO5 = [("这些菜多新鲜啊！", "(Card A: 新鲜) How fresh these dishes are!"), ("这个地方多么安全啊！", "(安全) How safe this place is!"), ("他学习多努力啊！", "(努力) How hard he studies!"), ("我今天多忙啊！", "(忙) How busy I am today!"), ("今天天气多热啊！", "(热) How hot it is today!"),
        ("这张沙发多舒服啊！", "(Card B: 舒服) How comfortable this sofa is!"), ("这个汤多清淡啊！", "(清淡) How light this soup is!"), ("这里的东西多便宜啊！", "(便宜) How cheap things are here!"), ("下班的时候路上多堵啊！", "(堵) How jammed the road is at rush hour!"), ("这个西瓜多甜啊！", "(甜) How sweet this watermelon is!"),
        ("自己订旅馆多麻烦啊！", "(Card C: 麻烦) How troublesome it is to book hotels yourself!"), ("夏天的天气多么闷热啊！", "(闷热) How muggy the summer weather is!"), ("这个菜多可口啊！", "(可口) How tasty this dish is!"), ("这个汤多咸啊！", "(咸) How salty this soup is!"), ("北京的房子多贵啊！", "(贵) How expensive houses in Beijing are!")]
DUO6 = [("我们的班多么团结啊！", "(mine) How united our class is!"), ("我们的同学多么友好啊！", "(mine) How friendly our classmates are!"), ("我们的学校多漂亮啊！", "(mine) How beautiful our school is!"), ("我多喜欢我们的老师啊！", "(mine) How much I like our teachers!")]
L5 = lesson(
    "Lesson 14 Presentation 2 grammar: the exclamatory sentence with 多",
    "多自由呀！ · 今天的天气多美啊！ · 我多想旅行全世界啊",
    requires=[],
    cards=[
        card("Exclamatory Sentence with 多",
             "In Chinese, the exclamatory pattern 多/多么…啊/呀！ may be used to express a strong emotional response to a situation or experience. In this pattern, an adjective describing the speaker’s strong feeling or a verb expressing a strong emotion is placed after 多/多么. Adjective: (Something) + 多/多么 + adjective + 啊/呀！ Verb: Subject + 多/多么 + Verb + Object + 啊/呀！ The book’s examples 1 to 7 follow the sentence from the dialog.",
             examples=[D(z, e) for z, e in DUO]),
        card("Activity 5 (Reading, Listening and Speaking)",
             "Work in groups of three. Each group member picks one index card (A: 新鲜, 安全, 努力, 忙, 热. B: 舒服, 清淡, 便宜, 堵, 甜. C: 麻烦, 闷热, 可口, 咸, 贵), studies it, and takes turns selecting one word from the card for a group member to make an exclamatory sentence with 多/多么…啊/呀！ Keep going until all the words are used. My sentences for all fifteen words:",
             examples=[D(z, e) for z, e in DUO5]),
        card("Activity 6 (Writing and Speaking)",
             "Divide into pairs. Create exclamatory sentences complimenting your class, your classmates and DLI (the Defense Language Institute), using 多/多么 + adj. + 啊/呀！ or 多/多么 + VO + 啊/呀. A. Each pair chooses a topic and writes several sentences. B. Exchange your work with other pairs and tell them how you feel about your class, classmates and DLI. My samples:",
             examples=[D(z, e) for z, e in DUO6]),
    ],
    exercises=[
        M("What does the pattern 多/多么…啊 express?", "A strong emotion: “how…!”", ["A question", "A negation", "A request"], "Exclamation."),
        M("What comes right after 多/多么?", "An adjective or a verb of strong feeling", ["A noun", "A number", "A question word"], "多 + adj./verb."),
        M("What does 今天的天气多美啊！ mean?", "How beautiful the weather is today!", ["Is the weather beautiful?", "The weather is bad", "I like the weather forecast"], "多美."),
        M("What does 那位老大爷七十多岁了，身体多好呀！ mean?", "That old man is over seventy; how healthy he is!", ["He is seventy and ill", "He is a doctor", "He is very young"], "多好."),
        M("What does 我多想旅行全世界啊 express?", "How much I want to travel the whole world!", ["I traveled the world", "I hate traveling", "I will travel next week"], "多想."),
        M("What does 先生告诉太太说，“我多爱你啊！” mean?", "“How much I love you!”", ["“I don’t love you”", "“Do you love me?”", "“Where are you?”"], "多爱."),
        M("What can come after the adjective or verb phrase?", "啊 or 呀", ["吗", "了", "过"], "多…啊/呀."),
        F("自己去，多自由___！", "呀", ["吗", "们", "过"], "多…呀."),
        F("今天的天气___美啊！", "多", PART, "多 + adj."),
        F("姐姐新买的衣服多么漂___啊！", "亮", PART, "漂亮: pretty."),
    ],
)

# ------------------------------------------------------------------ 6. 还是
HS = [("像我这样的懒人还是参加旅行团比较方便。", "For a lazy person like me, it is better to join a tour group; it would be more convenient."), ("我们还是明天去吧。", "We’d better go tomorrow."), ("太晚了，我们还是打车吧。", "It’s too late; we’d better take a taxi."), ("她不想说，还是不要问了。", "She doesn’t want to talk; better not ask."),
      ("今天太冷，你还是多穿些衣服吧。", "It’s too cold today; you’d better put on more clothes."), ("还是你来我家吧。我七点钟在家等你。", "You’d better come to my home. I’ll wait for you at home at seven."), ("这双皮鞋太贵了，还是别买了。", "These shoes are too expensive; better not buy them.")]
HP = [("同学", "我今年的作业太多了，睡得很少。", "I have so much homework this year, and I sleep very little."), ("朋友", "你还是少玩儿手机，早点儿睡觉吧。", "You’d better play less on your phone and go to bed earlier. (mine)"), ("同学", "我的中文说得不好，不敢跟中国人说话。", "My Chinese isn’t good and I dare not speak with Chinese people."), ("朋友", "还是多跟他们聊天吧，这样进步最快。", "You’d better chat with them more; that’s the fastest way to improve. (mine)")]
L6 = lesson(
    "Lesson 14 Presentation 2 grammar: expressing preferences with 还是",
    "我们还是明天去吧 · 你还是多穿些衣服吧 · 还是别买了",
    requires=[],
    cards=[
        card("Express Preferences with 还是",
             "In previous lessons, 还是 was used as an alternative question marker indicating a selection between two or more options. When used in a statement, the adverb 还是 may indicate a choice or preference, similar to the English phrase “had better” or “it would be better to”. 还是 usually comes before a verb or subject. 吧 is often placed after this structure as a suggestion. Patterns: Subject + 还是 + Verb + (吧); 还是 + Subject + Verb + (吧).",
             examples=[D(z, e) for z, e in HS]),
        card("Activities 7 and 8",
             "Activity 7 (Listening and Speaking). A. Listen to the three dialogs and write notes in the table (speaker’s preference and reason). B. Exchange findings with your partner and share them with the class. (Audio, not included.) Activity 8 帮帮我 (Writing, Speaking and Listening). You will try to help resolve each other’s problems and concerns by offering suggestions using 还是. A. Pair up. In Chinese, write down problems or concerns from your life (four lines). B. In groups of three, take turns reading your problems aloud; the other students offer suggestions using 还是. C. Share some of your group’s problems with the other groups and try to provide more suggestions. A sample exchange (mine):",
             examples=dlg(HP)),
    ],
    exercises=[
        M("What does 还是 mean in a statement?", "“Had better”; a preference", ["“Or” in a question", "“Although”", "“Never”"], "Preference."),
        M("What word often ends the suggestion?", "吧", ["吗", "了", "过"], "吧."),
        M("What does 我们还是明天去吧 mean?", "We’d better go tomorrow", ["Did we go tomorrow?", "We went yesterday", "We never go"], "还是…吧."),
        M("What does 太晚了，我们还是打车吧 mean?", "It’s too late; we’d better take a taxi", ["We should walk", "We should stay", "We took a taxi"], "还是打车."),
        M("What does 这双皮鞋太贵了，还是别买了 mean?", "These shoes are too expensive; better not buy them", ["Let’s buy two pairs", "They are cheap", "I bought them"], "还是别买."),
        M("What does 今天太冷，你还是多穿些衣服吧 mean?", "It’s cold; you’d better wear more clothes", ["Take off your clothes", "It is hot", "Buy clothes"], "还是多穿."),
        M("Where can 还是 stand?", "Before a verb or before a subject", ["Only at the end", "Only before a number", "After 吗"], "Before a verb or subject."),
        F("太晚了，我们还是打车___。", "吧", ["吗", "们", "了"], "还是…吧."),
        F("她不想说，还是不要问___。", "了", ["吗", "们", "呢"], "还是不要问了."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
PL1 = [("周文的旅行计划", "参观西安的名胜古迹。去上海逛逛商场、买买东西。去哈尔滨玩儿几天，在哈尔滨滑雪。"), ("高军的旅行计划", "和女朋友去广州过春节。和女朋友在北京城里、城外逛逛。去海南岛玩儿一个星期。")]
B1 = ("苏州加乌镇加杭州，四日三晚，跟团游。苏州，乌镇，杭州。行程特色：一，古镇风光，小桥流水。二，最短时间，美景看全。三，入住商务酒店和民宿。四，游览西湖，尝龙井茶。"
      "行程概要。第一天：早晨六点半坐旅游车前往苏州，跟随导游参观苏州市中心和当地有名的园林。晚上看夜景，逛夜市。第二天：坐高铁前往乌镇。坐游船看古镇，和当地人聊天。晚上住民宿。第三天：坐高铁前往杭州，然后坐旅游车跟随导游游览西湖，乘船游西湖，拍照。下午去品尝最有名的龙井茶，购买龙井茶。晚上，在市中心的中国饭馆吃当地特色的饭菜。入住四星商务酒店。第四天：上午自由活动，游市中心，逛街，购物。中午乘高铁离开。"
      "费用：每人九百九十九元，包三晚酒店住宿；专用旅游车；中文导游服务；和景点门票。预订：网上预订或打电话，四零零，八一零，五五二二。中国青年旅行社。")
B1_E = ("Suzhou + Wuzhen + Hangzhou, 4 days 3 nights, group tour. Itinerary features: 1. Ancient-town scenery, small bridges and flowing water. 2. The shortest time to see all the beautiful sights. 3. Stay in business hotels and home stays. 4. Tour West Lake and taste Longjing tea. Outline. Day 1: at 6:30 a.m. take the tour bus to Suzhou; follow the guide to visit downtown Suzhou and the famous local gardens. In the evening see the night view and stroll the night market. Day 2: take the high-speed train to Wuzhen. Take a boat to see the ancient town and chat with locals. Stay in a home stay at night. Day 3: take the high-speed train to Hangzhou, then the tour bus with the guide to tour West Lake, boat on West Lake, take photos. In the afternoon go taste the most famous Longjing tea and buy some. In the evening eat local-specialty dishes at a Chinese restaurant downtown. Stay at a four-star business hotel. Day 4: free activities in the morning, tour downtown, stroll and shop. Leave by high-speed train at noon. Cost: 999 yuan per person, including 3 nights’ hotel, a dedicated tour bus, Chinese-language guide service and admission tickets. Booking: online or by phone 400-810-5522 (the phone number is read out digit by digit). China Youth Travel Service.")
B2 = ("黄山风景区，三日两晚，跟团游。行程特色：一，登黄山，看日出。二，观云海，赏美景。三，住五星酒店。四，经典路线，千人出游。"
      "行程概要。第一天：从上海出发，坐高铁前往黄山景区。跟随导游坐缆车，游黄山，入住黄山大酒店。晚上看夜景，听松涛声。第二天：早五点半起床，准备看有名的黄山日出。看日出、观云海，拍照。中午起，可以步行下山。不想爬山的游客，可以坐缆车或旅游车去不同的景点。晚上住山下酒店，品安徽名菜。第三天：坐旅游车前往附近的小镇宏村，游老街，在村里散步。到处是景，像画一样，看当地人的生活和房子，买特色产品。"
      "费用：每人一千零九十九元，包两晚酒店住宿；两顿早餐，中西餐；专用旅游车；和中英文导游服务；不包景点门票。预订：网上预订或打电话预订，为了您的安全，十八岁以下，六十岁以上游客不可以参加本旅游团。中国天下旅行社。")
B2_E = ("Huangshan Scenic Area, 3 days 2 nights, group tour. Itinerary features: 1. Climb Huangshan and watch the sunrise. 2. See the sea of clouds and enjoy beautiful views. 3. Stay in a five-star hotel. 4. A classic route, a thousand people travel it. Outline. Day 1: depart from Shanghai by high-speed train to the Huangshan scenic area. Follow the guide by cable car, tour Huangshan, check in at Huangshan Grand Hotel. In the evening see the night view and listen to the sound of the pines. Day 2: get up at 5:30 to see the famous Huangshan sunrise. Watch the sunrise and sea of clouds, take photos. From noon you can walk down the mountain. Visitors who don’t want to climb can take the cable car or tour bus to different sights. At night stay at the hotel at the foot of the mountain and taste famous Anhui dishes. Day 3: take the tour bus to the nearby small town Hongcun, tour the old street and stroll in the village. Everywhere is scenery, like a painting; see the locals’ life and houses and buy specialty products. Cost: 1099 yuan per person, including 2 nights’ hotel, 2 breakfasts (Chinese and Western), a dedicated tour bus and Chinese–English guide service; scenic-spot tickets not included. Booking: online or by phone; for your safety, visitors under 18 or over 60 cannot join this tour. China Tianxia Travel Service.")
VIEW = ("爸爸带着小儿子爬到山顶。爸爸说：“快看哪，山下的景色多好啊！”儿子说：“既然下面的景色好，我们为什么要花三个小时爬到上面来呢？”")
VIEW_E = "A father took his young son up to the mountaintop. The father said: “Look, how nice the scenery below the mountain is!” The son said: “Since the scenery below is good, why did we spend three hours climbing up here?” (the book’s title: 景色)"
L7 = lesson(
    "Lesson 14 Presentation 2: skill integration",
    "周文和高军的旅行计划 · 跟团游 · 黄山 · 景色",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "A. Pair up. Listen to the dialog once and list all the places described; discuss the topic of the conversation (photo: DLIFLC). B. Listen again and complete the table (Name of Traveler; Travel Activities; Transportation; Accommodations; Other Information). C. With your partner, arrange the sequence of events according to each speaker’s travel plans by numbering the sentences (below, as printed in the book). D. Take turns retelling each speaker’s plan in your own words, using the structure 先… 然后… 最后… E. Read the script and decide which traveler’s plan you like more, then explain why. (Audio, not included, so no sequence key.)",
             examples=[D(a + "：" + b, "(the book’s sentences, to be numbered)") for a, b in PL1]),
        card("Activity 2 (Listening, Speaking and Reading)",
             "A. Listen to the conversation between two friends and answer: 1. What did the speakers talk about? 2. What did the two speakers agree to do together? Why? 3. How long will it take to get to the speakers’ hometown from where they are now? 4. What is the second speaker’s warning and suggestion to the first speaker? B. Listen again and complete the table (Information: First Speaker, Second Speaker; rows: 目的地, 为什么去那儿, 旅行方式, 为什么这样旅行). C. Pair up and share your answers. D. Read the script with the class. (Audio, not included.)"),
        card("Activity 3 (Reading, Writing, Speaking and Listening): Brochure 1",
             "A. The following travel brochures are from two travel agencies. Work in pairs; each student reads one brochure and writes notes in the table (旅行社; 旅游团: 名字, 目的地; 时间: 天数; 行程: 活动; 费用; 预订). Focus on the tasks and guess the meanings of new words. The book prints numbers as digits and a telephone number; they are spelled out here. The book also shows photographs of Suzhou, Wuzhen and Hangzhou.",
             examples=[D(B1, B1_E)]),
        card("Brochure 2",
             "Photographs of Suzhou and Hangzhou (not included). The book’s Brochure 2:",
             examples=[D(B2, B2_E)]),
        card("Activity 3 B to D and Activity 4",
             "B. When you have completed Step A, share the information with your partner and ask them questions about their brochure. C. Compare the two travel packages and decide which tour you and your partner would like to go on: 我们选择了 ___ 旅行团，因为：1. 2. 3. 4. D. Share your decision with the class and provide your reasons. Activity 4 (Reading and Speaking). Read the dialog and answer the questions: 1. Do you think the child’s question is nonsense? Why? 2. If you were the parent, how would you answer the child’s question? My answers (mine): 1. Not entirely; it is a funny question, but it shows he sees no point in the climb. 2. “Because the view from the top is different, and the climb itself is the fun.”",
             examples=[D(VIEW, VIEW_E)]),
    ],
    exercises=[
        M("Which cities does Brochure 1 visit?", "Suzhou, Wuzhen, Hangzhou", ["Beijing, Xi’an, Luoyang", "Guilin, Lijiang, Kunming", "Huangshan, Hongcun, Shanghai"], "苏州+乌镇+杭州."),
        M("How many days and nights is Brochure 1’s tour?", "Four days, three nights", ["Three days, two nights", "Five days, four nights", "One day"], "四日三晚."),
        M("What is the cost of Brochure 1?", "999 yuan per person", ["1099 yuan", "199 yuan", "9999 yuan"], "每人九百九十九元."),
        M("Which tea can you taste in Brochure 1?", "Longjing tea", ["Pu’er tea", "Jasmine tea", "Oolong tea"], "龙井茶."),
        M("How does Brochure 1 travel from Suzhou to Wuzhen?", "By high-speed train", ["By boat only", "By plane", "On foot"], "坐高铁前往乌镇。"),
        M("Where does Brochure 2 go?", "Huangshan and Hongcun", ["Suzhou and Hangzhou", "The Great Wall", "Xi’an"], "黄山风景区."),
        M("What do visitors see at dawn on Huangshan?", "The sunrise and the sea of clouds", ["A parade", "A market", "The moon only"], "看日出、观云海。"),
        M("What is not included in Brochure 2’s price?", "Scenic-spot admission tickets", ["Hotel", "Breakfast", "The tour bus"], "不包景点门票。"),
        M("Who cannot join Brochure 2’s tour?", "Visitors under 18 or over 60", ["Anyone from abroad", "Students", "Families"], "十八岁以下，六十岁以上游客不可以参加。"),
        M("What does the son ask the father?", "Why spend three hours climbing if the view below is good?", ["Where the toilets are", "When to go home", "Whether he can buy food"], "我们为什么要花三个小时爬到上面来呢？"),
        mean("缆车", "lan3 che1", "cable car", ["taxi", "train", "bicycle"]),
        mean("预订", "yu4 ding4", "to book in advance", ["to cancel", "to pay", "to refund"]),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
FLY = [("美国东部", "the U.S. East"), ("美国西部", "the U.S. West"), ("美国南部", "the U.S. South"), ("美国中西部", "the U.S. Midwest")]
INFO = [("地区和天气", "Region and weather"), ("旅游景点", "Tourist spots"), ("最佳旅游时间", "Best times to visit"), ("活动选择", "Activity options"), ("交通选择", "Transportation options"), ("住宿选择", "Accommodation options"), ("跟团游还是自由行", "Take a tour or travel independently"), ("费用估计", "Estimated costs"), ("怎么预订旅行计划", "How to book the travel program")]
L8 = lesson(
    "Lesson 14 Presentation 2: using Chinese in context",
    "暑假旅行计划 · 美国欢迎你 · 跟团游还是自由行？",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking, Writing and Listening): Summer Vacation Travel Plans",
             "Scenario: you are studying Chinese at Shanghai Fudan University in China. Your summer vacation starts in two weeks and you plan to travel around China with some friends (photographs: the Sichuan giant panda reserve, Guilin, Tibet). Decide on travel plans with your friends and figure out all the details. A. Pair up. Research Chinese travel websites to decide where you would like to go (the book lists three travel websites, not included here). 我们打算去：___。 B. After you decide on your destination, write your plans in Chinese characters in the table 暑假旅行计划 (rows: 时间, 目的地, 交通, 活动, 住宿, 旅行方式, 费用, 订票). C. Post your travel plans online and share them with your classmates, who will comment or ask questions."),
        card("Activity 2 (Reading, Speaking, Writing and Listening): Travel flyer 美国欢迎你",
             "A U.S. travel agency needs your help creating new printed programs for Chinese tourists (photographs: San Francisco’s Golden Gate Bridge, New York). You and your classmates compete to create travel flyers for popular destinations for Chinese tourists in the U.S.; the flyers must be in Chinese and the winner will be hired as a consultant. A. Pair up and choose a destination: 美国东部, 美国西部, 美国南部, 美国中西部; research relevant travel information. B. Collect for your flyer: region and weather, tourist spots, best times to visit, activity options, transportation options, accommodation options, take a tour or travel independently, estimated costs, how to book the travel program. C. Design your flyer on a white board or flip chart and post it. D. Each pair presents its flyer to the agency’s marketing team (the class) and explains why its program is the best choice. E. The winner is announced after a vote.",
             tables=[table(["Region", "Meaning"], [(a, b) for a, b in FLY], title="Choose one", say=[0]), table(["Flyer item", "Meaning"], [(a, b) for a, b in INFO], title="Information to collect (Chinese wording is mine)", say=[0])]),
        card("Activity 3 (Speaking, Writing and Listening): Debate 跟团游还是自由行？",
             "While you are studying at Beijing University, you and your classmates debate the best way to travel: joining a tour group or traveling independently. A. Divide the class into two groups; Group A advocates traveling with a tour and Group B independent travel. B. In your group, prepare for the debate: discuss the advantages of your mode of travel and create in Chinese a list of the benefits (跟团游的好处 / 自由行的好处, four lines), with supporting examples (stories, statistics, etc.). C. Discuss and list the disadvantages of the other group’s mode of travel (的坏处, four lines). D. Your teacher facilitates the debate. (Photographs not included.)"),
    ],
    exercises=[
        M("What is the scenario in Activity 1?", "Planning a summer trip around China with friends", ["Buying a house", "Studying for an exam", "Looking for a job"], "暑假旅行计划."),
        M("What do you write in the plan table?", "Time, destination, transport, activities, lodging, travel mode, cost, booking", ["Only prices", "Only dates", "Only names"], "Table rows."),
        M("What is the task in Activity 2?", "Create Chinese travel flyers for Chinese tourists visiting the U.S.", ["Translate an English flyer", "Sell tickets", "Review a hotel"], "美国欢迎你."),
        M("Which region is NOT in the list?", "美国北部", ["美国东部", "美国西部", "美国中西部"], "East, West, South, Midwest."),
        M("What does 跟团游 mean?", "Group tour", ["Independent travel", "Business trip", "School trip only"], "跟团游."),
        M("What does Group B argue for in the debate?", "Independent travel", ["Group tours", "Staying at home", "Taking a taxi"], "Group B promotes independent travel."),
        F("跟团游还是___由行？", "自", PART, "自由行: independent travel."),
        F("美国___迎你。", "欢", PART, "欢迎: welcome."),
    ],
)
L9 = vocab_lesson("Lesson 14 Presentation 2 vocabulary", "26 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十四课 休闲旅游 Presentation 2: Xi’an trip, 什么 + 吗, rhetorical 什么, 多…啊, 还是, tour brochures", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
