"""Unit 45: Lesson 16 (Recreational Activities) Presentation 1 from the book's texts: the computer-game dialog, the progressive
正在/在, 从来不/没, 上 after a noun, the skill-integration and using-Chinese activities and the vocabulary list. Audio, pictures,
videos and the websites are not included; the book writes numbers as digits and they are spelled out here; answer keys the book
does not print (and blanks it leaves for the student) are mine and labeled."""
from zh_auto import *
from zh_l16_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("得做", 0, "dei3"), ("得在", 0, "dei3"), ("得小心", 0, "dei3"), ("中病毒", 0, "zhong4"), ("中了病毒", 0, "zhong4"), ("上瘾", 1, "yin3"), ("网瘾", 1, "yin3"), ("没想到", 0, "mei2"), ("没听见", 0, "mei2"),
                          ("一块儿", 1, "kuai4"), ("长大", 0, "zhang3")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0 and zh[j - 1] not in "当草土天各山场内本外基实陆" and (j + 1 >= len(zh) or zh[j + 1] not in "道址方铁图球区点上下面理"):
            f[j] = "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [("珍妮", "你怎么又坐在电脑前了？", "Why are you sitting in front of the computer again?"), ("大卫", "我正在学习中文呢！", "I’m studying Chinese!"), ("珍妮", "学习中文？我看你是在玩游戏吧！", "Studying Chinese? I think you’re playing games!"),
      ("大卫", "学累了，当然要休息休息。你看，这个游戏很好玩。要不要试一试？", "When I’m tired from studying, of course I need a rest. Look, this game is fun. Want to try?"), ("珍妮", "什么游戏？", "What game?"),
      ("大卫", "《我的世界》。这个游戏现在特别流行，可以自己玩，也可以在网上和别人一起玩。", "“Minecraft”. This game is especially popular now; you can play by yourself or play online with others."), ("珍妮", "我从来不玩游戏，只在网上看新闻，查邮件什么的。", "I never play games; I only read news online, check email and so on."),
      ("大卫", "不会吧！网上能做的事可多了。你可以在网上看视频，也可以在脸书上和朋友聊天。", "No way! There’s so much you can do online. You can watch videos online, and chat with friends on Facebook."), ("珍妮", "我看，你是上网瘾了。", "I think you’re addicted to the internet."),
      ("大卫", "还真有点。因特网太好了，需要什么，鼠标一点，东西就到家门口了。", "Kind of. The internet is so great; whatever you need, one click of the mouse and it’s at your door."), ("珍妮", "算了吧，我上次从网上下载了一首歌，没想到电脑马上就死机了。", "Forget it. Last time I downloaded a song online, and unexpectedly the computer crashed right away."),
      ("大卫", "大概是中了病毒。我帮你装一个杀毒软件，你再下载音乐就不会有问题了。", "Probably it caught a virus. I’ll install antivirus software for you, and then there won’t be a problem when you download music again.")]
A1M = [("点", "8 鼠标"), ("下载", "7 音乐, 4 视频, 9 软件, 2 游戏"), ("看", "1 新闻, 4 视频"), ("查", "3 邮件"), ("玩", "2 游戏"), ("上", "5 网瘾"), ("中", "6 病毒"), ("装", "9 软件"), ("听", "7 音乐")]
A4 = [("A：今天晚上来我宿舍玩电子游戏？", "算了吧！我明天还有考试呢！我还是先好好准备考试吧。", "1. A: Come to my dorm tonight to play video games? B: Forget it! I still have an exam tomorrow. I’d better prepare well for the exam first. (key mine)"),
      ("A：我听说下载音乐常会中病毒。", "不会吧！只要装了杀毒软件就没什么问题。", "2. A: I heard downloading music often gets a virus. B: No way! As long as you have antivirus installed, there’s no problem. (key mine)"),
      ("A：现在我白天上网课，下课后我上网和网友玩游戏，看视频。", "我看，你一天都离不开网路。", "3. A: Now I take online classes during the day, and after class I go online to play games with online friends and watch videos. B: I think you can’t leave the internet for a whole day. (key mine)"),
      ("A：你已经一连干了好几天的活了，都没好好休息。你不累吗？", "还真有点。", "4. A: You’ve been working for several days in a row without a good rest. Aren’t you tired? B: Kind of. (key mine)")]
L1 = lesson(
    "Lesson 16 Presentation 1: playing games online",
    "你怎么又坐在电脑前了？ · 我正在学习中文呢 · 不会吧 · 算了吧",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: a laptop and a smartphone (not included). Pair up and discuss: A. List activities you can do online; together write a list of five examples. B. What are your favorite things to do online? Why? C. In your opinion, what are the advantages and disadvantages of using computers or the internet?"),
        card("Presentation 1: 在电脑前",
             "The book also prints the dialog in traditional characters. Note: colloquial expressions: 不会吧 (no way; how could that be?); 还真有点 (kind of) indicating agreement; 我看 (I think…; in my opinion…); 算了吧 (forget it).",
             examples=dlg(P1)),
        card("Activity 1 (Reading, Speaking and Listening)",
             "A. Collocation practice: match the verbs with their most likely objects by writing the object numbers. More than one object may match a verb. Verbs: 点, 下载, 看, 查, 玩, 上, 中, 装, 听. Objects: 1. 新闻 2. 游戏 3. 邮件 4. 视频 5. 网瘾 6. 病毒 7. 音乐 8. 鼠标 9. 软件. The book leaves the key out; my matches (mine): " + "; ".join(a + " → " + b for a, b in A1M) + ". B. Read the presentation again and create a concept map of computer technology terms, organized as you like or using the categories 网路, 电脑软件/硬件, 活动, 问题. C. The following words and phrases are internet-related vocabulary from previous units: 用户名，密码，网站，网费，网上银行，网上转账，微信支付，扫码. Add them to your concept map and work with a partner to write three sentences in Chinese using the terms that are the most difficult for you."),
        card("Activities 2 and 3",
             "Activity 2 (Listening, Speaking). A. Global listening: What is the most likely relationship between the two speakers? Did they have similar online experiences? What did you hear that led to your answer? B. Detailed listening: listen again and list the activities the speakers enjoy online and the issues they encountered (columns 大卫 and 马克). C. Pair up; in Chinese, Student A reports David’s experiences and Student B reports Mark’s. D. With your partner, read Presentation 1 aloud. (Audio, not included.) Activity 3 (Listening and Speaking). A. Listen to the sentences that describe the internet habits of Linda’s family and fill in the table (爸爸, 妈妈, 哥哥, 姐姐, 弟弟, 我). B. Pair up; Student A reports on one half of the family’s internet habits and Student B the other half. C. Survey your classmates on their internet activities and find classmates who match: 1. who spends most of their time online on the weekend; 2. who plays Chinese computer games; 3. who shops online at least five times per month; 4. who has a Facebook account; 5. who makes friends via the internet; 6. who knows how to download a video; 7. whose computer has been infected by a virus. D. The entire class shares what they learned through the survey. (Audio, not included.)"),
        card("Activity 4 (Reading and Speaking)",
             "A. Read the conversation below and decide what would be the most appropriate response from those listed in the box: 我看 / 算了吧 / 还真有点 / 不会吧！ B. Compare your answers with a partner and discuss strategies that helped you answer correctly. The book leaves the key out; my completed exchanges (mine):",
             examples=[D(a + "乙：" + b, e) for a, b, e in [(x[0].replace("A：", "甲："), x[1], x[2]) for x in A4]]),
    ],
    exercises=[
        M("What is David doing at the computer?", "Studying Chinese (and playing a game)", ["Cooking", "Sleeping", "Writing a letter"], "我正在学习中文呢；这个游戏很好玩。"),
        M("What game does David recommend?", "Minecraft (我的世界)", ["Chess", "Football", "Solitaire"], "《我的世界》."),
        M("What does Jenny do online?", "Reads news and checks email", ["Plays games", "Chats on Facebook", "Watches videos"], "只在网上看新闻，查邮件什么的。"),
        M("What does 我从来不玩游戏 mean?", "I never play games", ["I sometimes play games", "I will play games", "I have played games"], "从来不: never."),
        M("What does 不会吧！ mean?", "No way! How could that be?", ["Yes, of course", "Let’s go", "Thank you"], "不会吧."),
        M("What does 还真有点 mean?", "Kind of (agreeing)", ["Not at all", "Never", "Really far"], "还真有点."),
        M("What does 算了吧 mean?", "Forget it", ["Come on", "Let’s count", "Calculate it"], "算了吧."),
        M("What happened to Jenny’s computer?", "It crashed after she downloaded a song", ["It caught fire", "It was stolen", "It was sold"], "没想到电脑马上就死机了。"),
        M("What does David offer to install?", "Antivirus software", ["A game", "A browser", "A printer"], "我帮你装一个杀毒软件。"),
        M("What does 网瘾 mean?", "Internet addiction", ["Internet cafe", "Internet speed", "Internet fee"], "网瘾."),
        M("Which verb goes with 病毒?", "中", ["听", "点", "查"], "中病毒: catch a virus."),
        M("Which verb goes with 鼠标?", "点", ["下载", "看", "玩"], "点鼠标: click the mouse."),
        mean("电脑", "dian4 nao3", "computer", ["television", "telephone", "camera"]),
        F("学累了，当然要休___休息。", "息", PART, "休息休息."),
    ],
)

# ------------------------------------------------------------------ 2. progressive
ZZ = [("我正在吃饭(呢)。", "I am eating."), ("我正吃饭呢。", "I am eating."), ("我在吃饭(呢)。", "I am eating."), ("我吃饭呢。", "I am eating."), ("我正在学习英文呢！", "I am studying English!"), ("妈妈正在打电话吗？", "Is Mom making a phone call?"), ("老师没有在上课。", "The teacher is not teaching.")]
ZZ2 = [("昨天我给你打电话的时候，你在做什么？", "(past) What were you doing when I called you yesterday?"), ("你现在在做什么呢？", "(present) What are you doing now?"), ("明天早上这个时候你会做什么呢？", "(future) What will you be doing at this time tomorrow morning?"), ("你打电话给我的时候，我正做着饭呢。", "When you called me, I was cooking."), ("你等一会儿再走，外边正下着雨呢。", "Wait a while before you leave; it’s raining outside.")]
ZA2 = [("大年", "喂，林文？你在做什么呢？", "Hello, Lin Wen? What are you doing?"), ("林文", "在看电视呢。", "Watching TV."), ("大年", "半个小时以前，你在做什么？我去你们家，你们家没人。", "What were you doing half an hour ago? I went to your home and nobody was there."), ("林文", "我正在家里睡觉。没听见你来。", "I was sleeping at home. I didn’t hear you come."),
       ("大年", "现在我到你那儿去一趟，有一点儿事要跟你说。", "I’ll come over to your place now; there’s something I need to tell you."), ("林文", "来吧！我等着你。", "Come on! I’ll be waiting for you.")]
ZB = [("我去他宿舍的时候，他正在玩电脑游戏。", "1. When I went to his dorm, he was playing computer games. (mine)"), ("老师进教室的时候，同学们正在聊天。", "2. When the teacher entered the classroom, the students were chatting. (mine)"), ("我刚才给我女朋友打电话，她正在上课。", "3. I just called my girlfriend; she was in class. (mine)"),
      ("我昨天下课回家的时候，妈妈正在做饭。", "4. When I got home after class yesterday, Mom was cooking. (mine)"), ("明天中午的这个时候，我正在上课呢。", "5. At this time tomorrow noon, I’ll be in class. (mine)")]
L2 = lesson(
    "Lesson 16 Presentation 1 grammar: the progressive aspect 正在/在",
    "我正在学习呢 · 正在 + Predicate + 呢 · 没有在… · 正做着饭呢",
    requires=[],
    cards=[
        card("The progressive aspect 正在/在",
             "In this presentation, David says 我正在学习呢 to indicate he is studying. Therefore 正在 V(P) 呢 is a pattern that indicates an action (VP) is going on. This pattern has three alternative forms, with no difference in meaning. Statement: 正在 + Predicate + (呢); 正 + Predicate + 呢; 在 + Predicate + (呢); Predicate + 呢. Question: (正)在 + Predicate + 吗？ Negation: 没有(+ 在) + Predicate.",
             examples=[D(z, e) for z, e in ZZ]),
        card("Past, present and future",
             "An action in the progressive aspect may take place at the present time, in the past or the future. 着 used in the continuation of an action sometimes accompanies 正 or 呢.",
             examples=[D(z, e) for z, e in ZZ2]),
        card("Activity 1 (Speaking, Listening and Reading)",
             "A. Pair up. Student A chooses one word from the table (散步, 聊天, 看电影, 上网, 游泳, 照相, 骑自行车 for A; 买东西, 滑雪, 踢球, 吃零食, 喝茶, 打乒乓球, 排队 for B) and acts it out. Student B observes and forms a yes/no question using (正)在 while guessing; Student A answers with the negation or affirmative form. For example: B: 你正在锻炼吗？ A: 我没有在锻炼。 B: 你正在跳舞吗？ A: 对。 B. Each partner takes turns completing the sentences below; the other partner translates the entire sentence into English: 1. 我去他宿舍的时候，____。 2. 老师进教室的时候，____。 3. 我刚才给我女朋友打电话，____。 4. 我昨天下课回家的时候，____。 5. 明天中午的这个时候，____。 My completions (mine):",
             examples=[D("你正在锻炼吗？", "Are you exercising?"), D("我没有在锻炼。", "I’m not exercising."), D("你正在跳舞吗？", "Are you dancing?"), D("对。", "Yes.")] + [D(z, e) for z, e in ZB]),
        card("Activity 2 (Reading, Listening and Speaking)",
             "A. Pair up and read the conversation between two friends, using a timeline to record 林文’s actions (mine: now he is watching TV; half an hour ago he was sleeping at home). Compare your answer with your partner in Chinese using the progressive pattern. B. Listen to a dialog between two friends and mark the statements True or False: 1. Da Li asked Li Dong to help him with his homework. 2. Li Dong is doing his homework and would like to help Da Li later. 3. Da Li’s roommate cannot help him because he is taking a test. 4. The other students in Da Li’s dorm building have all left. 5. Li Dong agrees to go and help Da Li immediately. (Audio, not included.) C. Pair up, compare your answers and explain them in Chinese.",
             examples=dlg(ZA2)),
    ],
    exercises=[
        M("What does 正在 + Predicate + 呢 indicate?", "An action in progress", ["A finished action", "A past habit", "A wish"], "Progressive."),
        M("What does 我吃饭呢 mean?", "I am eating", ["I want to eat", "I ate", "I never eat"], "Predicate + 呢."),
        M("How do you negate the progressive?", "没有(+ 在) + Predicate", ["不 + 在", "别 + 在", "没 + 呢"], "没有（+在）+ Predicate."),
        M("What does 老师没有在上课 mean?", "The teacher is not teaching", ["The teacher didn’t come", "The teacher left", "The teacher is late"], "没有在."),
        M("What does 你现在在做什么呢？ ask?", "What are you doing now?", ["What did you do?", "What will you do?", "Where are you?"], "Present progressive."),
        M("Which sentence is about the future?", "明天早上这个时候你会做什么呢？", ["你现在在做什么呢？", "昨天我给你打电话的时候，你在做什么？", "我正在吃饭"], "会 + future."),
        M("What does 外边正下着雨呢 mean?", "It is raining outside", ["It rained yesterday", "It will rain", "It never rains"], "正下着雨呢."),
        M("What was Lin Wen doing half an hour earlier?", "Sleeping at home", ["Watching TV", "Eating", "Studying"], "我正在家里睡觉."),
        F("我___在学习英文呢！", "正", PART, "正在."),
        F("妈妈正在打电话___？", "吗", ["们", "着", "过"], "Question: (正)在 + Predicate + 吗？"),
    ],
)

# ------------------------------------------------------------------ 3. 从来不/没
CL = [("她从来不喝酒。", "She never drinks alcohol."), ("他的女朋友从来不给他打电话。", "His girlfriend never calls him."), ("我从来不十二点以后睡觉。", "I never go to bed after twelve."), ("我从不一边吃饭一边玩手机。", "I never play with my phone while eating.")]
CL2 = [("我从来没有去过中国。", "I have never been to China."), ("我从来没有想过这个问题。", "I have never thought about this question."), ("我从来没有听说过这个地方。", "I have never heard of this place."), ("我从来没有学过这个生词。", "I have never learned this new word."), ("我从来没有出国旅游过。", "I have never traveled abroad.")]
CL3 = [("我从来不吃早饭。", "I never eat breakfast. (mine)"), ("我从来没有坐过飞机。", "I have never flown on a plane. (mine)"), ("我从来不在网上买东西。", "I never shop online. (mine)")]
L3 = lesson(
    "Lesson 16 Presentation 1 grammar: 从来不/没",
    "她从来不喝酒 · 我从来没有去过中国 · 从不",
    requires=[],
    cards=[
        card("从来不",
             "Although 从来 can work in the positive meaning “always,” it is usually used in negation. When used as 从来不, you are saying that you never do something (e.g., as a habit or as a rule). 从来不 may be shortened to 从不 in casual speech. Subject + 从(来)不 + Verb Phrase.",
             examples=[D(z, e) for z, e in CL]),
        card("从来没(有)…过",
             "When used as 从来没 or 没有 (and 过 after the verb), you are saying that you have never done something (i.e., it is not a part of your life experience). Subject + 从(来)没有 + Verb + 过.",
             examples=[D(z, e) for z, e in CL2]),
        card("Activity 3 (Writing, Speaking and Listening)",
             "Write three statements about something you have never done or never do, using 从来不/从来没; one of the statements must be false and the other two must be true. Read them aloud to the class and have your classmates guess which are true. My statements (mine):",
             examples=[D(z, e) for z, e in CL3]),
    ],
    exercises=[
        M("What does 从来不 say?", "You never do something (a habit)", ["You have never done something once", "You always do it", "You may do it"], "从来不: never (habit)."),
        M("What does 从来没有…过 say?", "You have never experienced something", ["You never do it as a habit", "You always do it", "You will do it"], "Life experience."),
        M("How is 从来不 shortened in casual speech?", "从不", ["不从", "没从", "从没不"], "从不."),
        M("What does 她从来不喝酒 mean?", "She never drinks alcohol", ["She drinks a lot", "She has never drunk it", "She will drink"], "从来不."),
        M("What does 我从来没有去过中国 mean?", "I have never been to China", ["I never go to China", "I am in China", "I will go to China"], "从来没有…过."),
        M("What does 他的女朋友从来不给他打电话 mean?", "His girlfriend never calls him", ["His girlfriend calls often", "His girlfriend is away", "He never calls her"], "从来不."),
        M("What does 我从不一边吃饭一边玩手机 mean?", "I never play on my phone while eating", ["I always play on my phone", "I eat while sleeping", "I have no phone"], "从不."),
        F("我从来没有听说___这个地方。", "过", PART, "从来没有 + Verb + 过."),
        F("她从来___喝酒。", "不", PART, "从来不."),
    ],
)

# ------------------------------------------------------------------ 4. 上 after noun
SH = [("许多人在网上买机票，订旅馆，方便极了。", "Many people buy plane tickets and book hotels online; it is extremely convenient."), ("在聚会上大家常常一边喝酒，一边聊天。", "At parties everyone often drinks and chats at the same time."), ("她是我们班上最努力的学生。", "She is the hardest-working student in our class."), ("在生活上我们什么都有，所以我们要多帮助别人。", "In life we have everything, so we should help others more.")]
SH4 = [("这个人在电视上/网上玩电脑游戏。", "This person is playing a computer game on TV/online. (the book’s example)"), ("你今天在中文课上讲的语法，我还不太懂。", "I still don’t quite understand the grammar you taught in Chinese class today."), ("你先回家看看你的书，书上有练习。", "First go home and look at your book; there are exercises in the book."), ("要是你看了书还不会，你把语法上的问题写在笔记本上，明天下课以后，我再给你讲。", "If you still can’t do it after reading the book, write the grammar problems in your notebook, and tomorrow after class I’ll explain to you.")]
L4 = lesson(
    "Lesson 16 Presentation 1 grammar: 上 used after a noun",
    "在网上 · 书上 · 学习上 · 在聚会上 · 班上",
    requires=[],
    cards=[
        card("上 used after a noun",
             "When 上 is used after a noun, it indicates range, sphere, limits, or a particular aspect of something, as in 在网上, “online,” 书上, “in the book” and 学习上, “in studies.” (在) + Noun + 上.",
             examples=[D(z, e) for z, e in SH]),
        card("Activity 4 看图说话 (Speaking)",
             "A. Describe each of five pictures using the “N + 上” construction (pictures, not included). Example: 这个人在电视上/网上玩电脑游戏。 B. Pair up. Read the following conversation between a teacher and student with your partner. Take turns writing translations of the underlined sentences (the three sentences are: 1) 你今天在中文课上讲的语法，我还不太懂。 2) 你先回家看看你的书，书上有练习。 3) 要是你看了书还不会，你把语法上的问题写在笔记本上，明天下课以后，我再给你讲。). Speakers: 李大力 and 王老师.",
             examples=[D(z, e) for z, e in SH4]),
    ],
    exercises=[
        M("What does 上 after a noun indicate?", "Range, sphere or aspect (e.g. online, in the book)", ["Direction up", "A past action", "A question"], "Range, sphere, limits."),
        M("What does 在网上 mean?", "Online", ["On the net (a fishing net)", "At home", "In the office"], "在网上."),
        M("What does 书上 mean?", "In the book", ["On the desk", "On the shelf", "In the bag"], "书上."),
        M("What does 学习上 mean?", "In studies", ["In the school", "In the exam", "On the road"], "学习上."),
        M("What does 她是我们班上最努力的学生 mean?", "She is the hardest-working student in our class", ["She is our teacher", "She is absent", "She is lazy"], "班上."),
        M("What does 在聚会上 mean?", "At a party", ["After a party", "Before a party", "Instead of a party"], "在聚会上."),
        M("What does 语法上的问题 mean?", "Problems in grammar", ["A grammar book", "A grammar teacher", "A grammar class"], "语法上的问题."),
        F("许多人在网___买机票，订旅馆，方便极了。", "上", PART, "在网上."),
        F("你先回家看看你的书，书___有练习。", "上", PART, "书上."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
GM = ("要是你要上网玩游戏，你得做一些准备。第一步，你的电脑需要能上网，这样你能在网上找可以下载电脑游戏的网站。第二步是到那个网站去。网站上会有各种各样的游戏，有些是学习的游戏，有些是锻练的游戏。你可以挑选你喜欢的，游戏不一样，价钱也不一样。第三步，你得在这个网站开一个账户，设好用户名和密码。这样你才可以在网上付钱。你用信用卡付完钱后，就可以在网上下载你买的游戏。第四步，下载完游戏，你就可以开始玩了。你可以自己一个人玩或是在网上找网友一块儿玩。最后我想说的是上网下载游戏得小心。最好去你常去的网站，因为下载游戏可能让你的电脑中病毒。")
GM_E = ("If you want to play games online, you have to make some preparations. Step one: your computer needs to be able to get online, so that you can find websites online where you can download computer games. Step two is to go to that website. There will be all kinds of games on the website, some for learning and some for exercise. You can choose the ones you like; games differ, and so do prices. Step three: you have to open an account on this website and set a user name and password. Only then can you pay online. After you pay with a credit card, you can download the game you bought online. Step four: when the download is finished, you can start playing. You can play by yourself, or find online friends to play together. Finally, what I want to say is that downloading games online requires caution. It is best to go to websites you often use, because downloading games may give your computer a virus.")
NB = ("以前中国人家里有电脑的不多，所以网路刚开始流行的时候，很多人喜欢去网吧上网。在网吧你可以上网看新闻或是发电子邮件。后来网吧的服务越来越多，你不但能在网吧上网，还能点东西吃。所以很多地方又把网吧叫做网咖（网路咖啡店）。他们除了咖啡以外，还卖很多吃的和喝的东西，像其它的饮料、小吃、方便面什么的。近几年来，因为有越来越多人家里都装了电脑，也有了手机，他们随时都能上网看新闻，发电子邮件。所以现在很多人去网咖都是为了打电子游戏。他们一打就是几个小时，还有人一连几天都“住”在网咖里。有些网咖还有洗澡的地方，不想吃网咖的东西还可以点外卖，方便、舒服极了！")
NB_E = ("In the past not many Chinese families had a computer at home, so when the internet first became popular, many people liked to go to internet bars to get online. At an internet bar you could go online to read the news or send email. Later the internet bars offered more and more services: you could not only get online but also order things to eat. So in many places internet bars were also called 网咖 (internet cafes). Besides coffee they also sell many things to eat and drink, such as other drinks, snacks, instant noodles and so on. In recent years, because more and more homes have installed computers and people also have mobile phones, they can go online anytime to read the news and send email. So now many people go to internet cafes in order to play video games. They play for hours at a stretch, and some even “live” in the internet cafe for days in a row. Some internet cafes even have places to take a shower, and if you don’t want to eat the cafe’s food you can order takeout; extremely convenient and comfortable!")
L5 = lesson(
    "Lesson 16 Presentation 1: skill integration",
    "你有网瘾吗？ · 怎么在网上玩游戏 · 网吧和网咖",
    requires=[],
    cards=[
        card("Activity 1 你有网瘾吗？ (Listening, Speaking and Writing)",
             "A. You are studying at Beijing University. One day you receive a phone call from a polling company asking you to complete a survey. Listen to the questions (nine) and answer them based on your situation; several answers are chosen from 总是, 常常, 不常, 从不. B. Using the findings of the survey, the whole class discusses key elements of identifying someone with internet addiction and makes a list of the elements. (Audio, not included.)"),
        card("Activity 2 (Reading, Writing and Speaking): how to play an online game",
             "A. David is asking a friend to show him how to play an online computer game. Read the instructions and write the key steps in the boxes (第一步, 第二步, 第三步, 第四步, 最后). B. Pair up and, in Chinese, share your work. C. Think of an online activity you often do (e.g., shopping, downloading e-books, streaming movies or music) and write four steps of simple instructions for your partner. D. In Chinese, share your instructions verbally. My key steps (mine): 第一步 get a computer that can get online; 第二步 go to a game-download website and choose a game; 第三步 open an account, set a user name and password, and pay by credit card; 第四步 download and play, alone or with online friends; 最后 be careful, because downloading may bring a virus.",
             examples=[D(GM, GM_E)]),
        card("Activity 3 (Listening, Speaking and Writing)",
             "New vocabulary: 保龄球 (bǎolíngqiú; bowling). A. Listen to the conversation and answer: 1. What is the relationship between the two speakers? 2. What conclusion does the first speaker come to? B. Listen again and, in the table, list the differences described between Taiwanese young people (台湾年轻人) and Teacher Li (李老师). C. Pair up and, in Chinese, share your answer. D. Work with your partner to think of five questions about your teacher’s internet or recreational activities, select one of your team’s teachers to interview, then write a summary report (我的老师) and post it on MS Teams or Linoit. (Audio, not included.)"),
        card("Activity 4 (Reading and Speaking): the internet bar",
             "A. Read the passage and use the timeline as a template to illustrate the development of an internet cafe in China. B. Pair up and share your answers in Chinese; each student reports one block of information, and you take turns reporting the entire story.",
             examples=[D(NB, NB_E)]),
    ],
    exercises=[
        M("What do you need first to play online games?", "A computer that can get online", ["A credit card", "A username", "A game CD"], "第一步，你的电脑需要能上网。"),
        M("What kinds of games are mentioned?", "Learning games and exercise games", ["Only war games", "Only sports", "Only puzzles"], "有些是学习的游戏，有些是锻练的游戏。"),
        M("What do you set up on the website?", "An account with a user name and password", ["A shop", "A phone number", "A game"], "开一个账户，设好用户名和密码。"),
        M("How do you pay for the game?", "With a credit card, online", ["With cash", "By check", "At a store"], "你用信用卡付完钱后。"),
        M("What is the final advice about downloading games?", "Be careful; use sites you usually visit", ["Never download", "Download at night", "Use any site"], "上网下载游戏得小心。"),
        M("Why did many people use internet bars in the past?", "Few families had computers at home", ["They were free", "They were quiet", "They were new"], "以前中国人家里有电脑的不多。"),
        M("What is a 网咖?", "An internet cafe", ["A bank", "A school", "A phone shop"], "网路咖啡店."),
        M("Why do many people go to internet cafes now?", "To play video games", ["To read news", "To send email", "To shop"], "现在很多人去网咖都是为了打电子游戏。"),
        M("What extra services do some internet cafes have?", "A place to shower, and takeout ordering", ["A swimming pool", "A cinema", "A library"], "有些网咖还有洗澡的地方，可以点外卖。"),
        F("你可以自己一个人玩或是在网上找网友一块儿___。", "玩", PART, "一块儿玩."),
        F("网吧的服务越___越多。", "来", PART, "越来越多."),
    ],
)

# ------------------------------------------------------------------ 6. context
WH = [("张华", "大明，休息的时候你都做些什么？", "Daming, what do you do when you rest?"), ("大明", "我喜欢上网玩游戏。", "I like to play games online."), ("张华", "你在家里打吗？", "Do you play at home?"), ("大明", "家里上网太慢，我喜欢去网咖打。网咖上网快得多。", "Internet at home is too slow; I like to play at the internet cafe. It’s much faster there."),
      ("张华", "在网吧打游戏很贵吧？", "Isn’t playing games at an internet bar expensive?"), ("大明", "不太贵，一个小时大约十块。而且网咖什么游戏都有。想玩什么就玩什么。", "Not very; about ten yuan an hour. And the cafe has every game. You play whatever you want."),
      ("张华", "那网咖还有什么别的服务吗？", "Does the cafe have any other services?"), ("大明", "有啊！有时要是你打累了，想吃东西也没问题。只要鼠标点一下，服务员就会把你点的东西送过来。非常方便。", "Yes! If you get tired from playing and want to eat, no problem. Just click the mouse and the waiter will bring what you ordered. Very convenient."),
      ("张华", "听起来挺不错的！", "Sounds pretty good!"), ("大明", "是啊！我还在网咖认识许多网友。我们常一块上网打游戏！比自己在家玩有意思得多！", "Yes! I also met many online friends at the cafe. We often play online together! It’s much more fun than playing at home alone!"),
      ("张华", "我也想试试！下次你去的时候告诉我，我和你一起去。", "I want to try too! Next time you go, tell me and I’ll go with you."), ("大明", "没问题！", "No problem!")]
L6 = lesson(
    "Lesson 16 Presentation 1: using Chinese in context",
    "网咖的好处 · 订单和寄 · 网咖的比较 · 电子书项目",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "A. Listen to a conversation between two friends and list at least four advantages of using an internet cafe (网咖). B. Pair up and, in Chinese, discuss your answers. C. Number the sentences below in a logical order; the first sentence (张华: 大明，休息的时候你都做些什么？) has been done for you. The book prints the twelve lines out of order; the order below is my key (mine): 1 张华, 2 大明, 3 张华, 4 大明, 5 张华, 6 大明, 7 张华, 8 大明, 9 张华, 10 大明, 11 张华, 12 大明. (Audio, not included.)",
             examples=dlg(WH)),
        card("Activities 2 and 3",
             "Activity 2 (Listening, Speaking and Reading). New vocabulary: 订单 (dìngdān; order), 寄 (jì; mail). A. Listen to two phone conversations between a customer and a shopping website’s representative and fill in the table (reason for the call; what the customer service representatives reply). B. Pair up and, in Chinese, share your answers. C. With your partner, orally create a phone conversation between a customer and an online shopping site’s representative. (Audio, not included.) Activity 3 (Listening, Speaking and Writing). Below the book gives two links (YouTube) to two Americans talking about an internet cafe in the U.S. and China. A. Pair up. Student A watches link 1 (0:14–2:19, a Chinese 网咖) and Student B watches link 2 (1:49–3:10, an American 网咖); take notes on main features (price, service, customers). B. Report to your partner on what you learned from your video; your partner fills the other portion of the table. C. Create PPT slides on the similarities and differences and give an oral report to the entire class. (Videos and websites, not included.)"),
        card("Activity 4 (Speaking, Listening, Writing and Reading): instructional e-book project",
             "Most DLI students currently enrolled are “digital natives.” However, some teachers are not. In order to help teachers narrow the technology gap, your class is creating an instructional e-book that shows teachers how to utilize technology and the internet to make their lives more convenient. A. Work in groups of three. Identify and list three key online activities you think your teachers would benefit from in your instruction. B. Select one activity from your group list. Follow the layout you learned in Activity 2 of the Skill Integration section and write step-by-step instructions in Chinese. C. Peer review: share your instructions with your group member and help each other revise them to ensure the language is clear and easy to follow. D. Publish your group instruction pages on MS Teams Wiki; each group reads the other groups’ work and provides feedback. E. The class combines each group’s final products into one e-book."),
    ],
    exercises=[
        M("What does 大明 like to do when resting?", "Play games online", ["Watch movies", "Read books", "Sleep"], "我喜欢上网玩游戏。"),
        M("Why does Daming go to the internet cafe?", "Home internet is too slow", ["Home has no computer", "It is free", "It is close"], "家里上网太慢。"),
        M("How much does an hour cost?", "About ten yuan", ["About one yuan", "About a hundred yuan", "Free"], "一个小时大约十块。"),
        M("Why is the cafe’s game selection good?", "It has every game", ["It has only new games", "It has few games", "It has only Chinese games"], "网咖什么游戏都有。"),
        M("How do you order food at the cafe?", "Click the mouse and a waiter brings it", ["Go to the counter", "Call by phone", "Bring your own"], "只要鼠标点一下。"),
        M("What else does Daming get at the cafe?", "Many online friends", ["A job", "A degree", "A prize"], "我还在网咖认识许多网友。"),
        M("What does 张华 want to do?", "Go to the cafe with Daming next time", ["Quit games", "Open a cafe", "Study alone"], "我也想试试！"),
        M("What does 订单 mean?", "Order (for goods)", ["Receipt", "Delivery man", "Store"], "订单."),
        M("What does 寄 mean?", "Mail", ["Open", "Pay", "Return"], "寄."),
        F("张华：在网吧打游戏很贵___？", "吧", ["们", "着", "过"], "很贵吧: right?"),
    ],
)
L7 = vocab_lesson("Lesson 16 Presentation 1 vocabulary", "24 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十六课 娱乐活动 Presentation 1: computer games, 正在/在, 从来不/没, 上 after a noun, internet cafes", [L1, L2, L3, L4, L5, L6, L7])
