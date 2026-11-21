"""Unit 55: Lesson 19 (Travel by High-Speed Rail) Presentation 2 from the book's texts: Anna and David on the high-speed rail, the use of 次,
the adverb 根本, the adverb 一定 and the modal verb 会 for prediction, 等 meaning "when", the skill-integration activities (the Little Slow
Train), the using-Chinese activities (the Mary and Joe survey hints, the young conductor Zhang Mengmeng) and the vocabulary list. Audio,
pictures, links and the student's own writing blanks are not included; numbers the book writes as digits are spelled out in the Chinese text
here; answer keys the book does not print are mine and labeled."""
from zh_auto import *
from zh_l19_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("列车长", 2, "zhang3"), ("贵不了", 2, "liao3"), ("参军", 0, "can1"), ("没有", 0, "mei2"), ("没问题", 0, "mei2"), ("没那么", 0, "mei2"), ("没什么", 0, "mei2"), ("没想好", 0, "mei2"),
                          ("没买", 0, "mei2"), ("没去", 0, "mei2"), ("没洗", 0, "mei2"), ("没做", 0, "mei2"), ("还没", 1, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("长大", 0, "zhang3"),
                          ("得好好", 0, "dei3"), ("多得", 1, "de5"), ("教练", 0, "jiao4"), ("觉得买", 1, "de5"), ("下得有", 1, "de5"), ("觉得坐", 1, "de5"), ("还有朋", 0, "hai2"), ("连长", 1, "zhang3")):
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
P2 = [("安娜", "最近你在中国生活还好吗？上次你说要坐高铁去上海，去了吧？高铁怎么样？", "How have you been living in China lately? Last time you said you would take the high-speed rail to Shanghai; did you go? How was it?"), ("大卫", "去了，非常好。高铁的确特别快。从上海到北京一千四百多公里，只要四个半小时，时速三百五十公里。", "I went, and it was great. The high-speed rail is indeed extremely fast. From Shanghai to Beijing is over 1,400 kilometers and takes only four and a half hours, at 350 kilometers an hour. (the book writes the numbers as digits)"),
      ("安娜", "速度那么快啊！会不会不安全呢？", "It’s that fast! Won’t it be unsafe?"), ("大卫", "非常安全，而且特别平稳。这么说吧，如果不看窗外，你根本感觉不到列车在运行。", "Very safe, and extremely smooth. Put it this way: if you don’t look out the window, you can’t feel the train moving at all."),
      ("安娜", "高铁上的设施一定也很先进吧？", "The facilities on the high-speed rail must be very advanced too?"), ("大卫", "那当然。那当然。车厢里的座位很宽敞，而且可以无线上网。每个座位都有电源插座，可以随时充电。", "Of course, of course. The seats in the carriage are spacious and you can get online wirelessly. Every seat has a power socket, so you can charge at any time."),
      ("安娜", "高铁上的服务怎么样？", "How is the service on the high-speed rail?"), ("大卫", "相当好，可以说是一流的。服务员个个都很热情，有礼貌，服务也十分周到。", "Quite good; you could say first class. The attendants are all warm and polite, and the service is very thoughtful."),
      ("安娜", "车票好买吗？", "Are the tickets easy to buy?"), ("大卫", "好买。你可以在网上或者在手机上预订，当然也可以直接到火车站去买。", "Easy to buy. You can book online or on your phone, and of course you can also go straight to the train station to buy."),
      ("安娜", "票价是不是很贵？", "Are the fares expensive?"), ("大卫", "一般来说，比飞机票便宜多了。", "Generally speaking, much cheaper than plane tickets."),
      ("安娜", "听你这么说，我真想马上去体验一下。", "Hearing you say that, I really want to go and experience it right away."), ("大卫", "等你来中国的时候，我一定陪你去。", "When you come to China, I’ll definitely go with you.")]
L1 = lesson(
    "Lesson 19 Presentation 2: how was the high-speed rail?",
    "时速三百五十公里 · 安全又平稳 · 宽敞的座位 · 网上预订",
    requires=[],
    cards=[
        card("Getting Started",
             "Two photographs of a train and a station (not included). Pair up and discuss: A. How did you feel the last time you travelled by train? B. What is an Amtrak train like? C. Where in America is a high-speed rail being built?"),
        card("Presentation 2: 坐高铁的体验",
             "The book also prints the dialog in traditional characters.",
             examples=dlg(P2)),
    ],
    exercises=[
        M("Where did David ride the high-speed rail?", "From Shanghai to Beijing", ["From Beijing to Tianjin", "From Xi’an to Chengdu", "From Guangzhou to Hong Kong"], "从上海到北京."),
        M("How long does Shanghai to Beijing take?", "Four and a half hours", ["Two hours", "Six hours", "Four hours exactly"], "只要四个半小时."),
        M("What is the speed per hour?", "Three hundred and fifty kilometers", ["Two hundred kilometers", "Five hundred kilometers", "One hundred and fifty kilometers"], "时速三百五十公里."),
        M("How does David describe the ride?", "Very safe and very smooth", ["Noisy and bumpy", "Slow but cheap", "Dangerous but fast"], "非常安全，而且特别平稳."),
        M("What can’t you feel if you don’t look out the window?", "The train moving", ["The temperature", "The time", "The food"], "根本感觉不到列车在运行."),
        M("What does each seat have?", "A power socket", ["A television", "A small table only", "A reading lamp only"], "每个座位都有电源插座."),
        M("How does David rate the service?", "Quite good, first class", ["Bad", "Ordinary", "Slow"], "相当好，可以说是一流的."),
        M("How can you buy a ticket?", "Online, on a phone, or at the station", ["Only at the airport", "Only on the train", "Only by post"], "在网上或者在手机上预订，也可以直接到火车站去买."),
        M("How do fares compare with plane tickets?", "The high-speed rail is much cheaper", ["The same", "Much more expensive", "Free"], "比飞机票便宜多了."),
        M("What will David do when Anna comes to China?", "Go with her to ride the high-speed rail", ["Send her a ticket", "Take her to the airport", "Meet her in Shanghai"], "我一定陪你去."),
        F("每个座位都有电源插___，可以随时充电。", "座", PART, "插座: socket."),
        F("高铁的___确特别快。", "的", PART, "的确: indeed."),
        F("服务员个个都很热___，有礼貌。", "情", PART, "热情: enthusiastic."),
    ],
)

# ------------------------------------------------------------------ 2. activities 1-4
A2 = [("从北京到青岛，坐高铁只要三个小时。", "1. From Beijing to Qingdao it takes only three hours by high-speed rail. (从…到…，只要; sample sentence, mine)"), ("如果不看窗外，你根本感觉不到列车在运行。", "2. If you don’t look out the window, you can’t feel the train moving at all. (如果，根本; mine)"), ("听你这么一说，我也想去体验一下高铁。", "3. Hearing you say that, I want to go and try the high-speed rail too. (听你这么一说; mine)"), ("我一定要去体验一下中国的高铁。", "4. I’ll definitely go and experience China’s high-speed rail. (一定，体验; mine)"), ("高铁上的服务很周到，设施也是一流的。", "5. The service on the high-speed rail is thoughtful and the facilities are first class. (周到，一流; mine)")]
TAB19 = table(["高铁运行", "车厢内部", "服务", "订票"],
              [["特别快，时速三百五十公里，非常安全，特别平稳", "座位很宽敞，可以无线上网，每个座位都有电源插座，可以随时充电", "相当好，一流，热情，有礼貌，十分周到", "在网上或者在手机上预订，直接到火车站去买，比飞机票便宜多了"]],
              title="Activity 2 A: expressions from Presentation 2 (the book leaves the table blank; this fill is mine)", say=[0, 1, 2, 3])
TF19B = [("这是妈妈和女儿的对话，她们还谈到女儿的爸爸和姐姐。", "1. This is a conversation between a mother and a daughter; they also talk about the daughter’s father and sister."), ("妈妈一直觉得坐高铁很安全，所以没担心。", "2. The mother has always felt the high-speed rail is very safe, so she didn’t worry."), ("现在坐高铁的人非常多，有时不是每个人都有座位。", "3. Many people ride the high-speed rail now, and sometimes not everyone has a seat."), ("路上妈妈一直在用手机和她先生还有朋友们聊天。", "4. On the way the mother kept chatting on her phone with her husband and friends."),
         ("他们一家人可能会坐高铁去新疆旅游。", "5. Their family might take the high-speed rail to Xinjiang for a trip."), ("等爸爸和妈妈下车后，会有汽车在车站的南门接他们。", "6. After Dad and Mom get off the train, a car will pick them up at the station’s south gate.")]
CLZ = "上次放假的时候，我坐高铁从北京去了青岛。以前我没坐过，所以这是我第一次坐高铁。从北京到青岛差不多七百公里，只要三个小时。还没坐高铁的时候，我想列车运行速度那么快，坐在上面可能会觉得不太平稳。可是，真的坐上去以后，列车运行得非常平稳，如果不是服务员告诉我，我根本感觉不到列车是在以每小时二百多公里的速度运行。我坐的是二等座，有无线上网，座位旁边还有电源插座，可以随时给手机充电。高铁上的服务员都很客气，他们的服务也很周到。"
CLZ_E = "Last time I had a holiday, I took the high-speed rail from Beijing to Qingdao. I had never ridden before, so this was my first time. From Beijing to Qingdao is about 700 kilometers and takes only three hours. Before I rode it, I thought the train ran so fast that sitting on it I might find it not very smooth. But when I really got on, the train ran very smoothly; if the attendant hadn’t told me, I wouldn’t have felt at all that the train was running at over 200 kilometers an hour. I rode second class; there was wireless internet and a power socket by the seat, so I could charge my phone at any time. The attendants on the high-speed rail were all very polite, and their service was also very thoughtful. (the book gives the six blanks as choices; my key is 1 b 上次, 2 a 第一次, 3 a 可能, 4 c 根本, 5 a 随时, 6 c 周到; the book writes 700 and 3 as digits)"
L2 = lesson(
    "Lesson 19 Presentation 2 activities: the experience of the high-speed rail",
    "Activities 1 to 4 · 先进 设施 周到 一流 · 第一次坐高铁",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 2 and choose the correct answers: 1. What did David say about the high-speed rail in China? (They are the fastest in the world. / They are fast, steady and safe. / They are accessible anywhere in China.) 2. What would most likely happen in the future? (David will pick up Anna at a train station in China. / David will take Anna to China and visit places by train. / They will ride high-speed trains together in China.) B. Detailed listening: 1. How did Anna know that David was going to take the high-speed rail? 2. Was the train running smoothly? How do you know? 3. What features are available for each passenger? 4. How does one go about booking a ticket? (Audio, not included. My answers from the dialog: A1 fast, steady and safe; A2 they will ride high-speed trains together in China, since David says he will go with Anna when she comes; B1 David told her last time he would go; B2 yes, he could not feel the train moving; B3 a power socket and wireless internet; B4 online, on the phone, or at the station.)"),
        card("Activity 2 (Writing, Speaking and Writing)",
             "A. Pair up and take turns writing the expressions you’ve just learned in the table (高铁运行, 车厢内部, 服务, 订票). B. With your partner, write sentences using the expressions in parentheses: 1. (从…到…，只要) 2. (如果，根本) 3. (听你这么一说) 4. (一定，体验) 5. (周到，一流). The book leaves both parts to the student; my fills:",
             tables=[TAB19], examples=[D(z, e) for z, e in A2]),
        card("Activity 3 (Listening, Speaking and Reading)",
             "A. Listen to the dialog and mark each of the following statements as True or False; B. pair up, discuss your answers and go over the script. The audio is not included and the book prints neither the script nor a key, so I do not give a key; the six statements are:",
             examples=[D(z, e) for z, e in TF19B]),
        card("Activity 4 (Reading and Speaking)",
             "A. Choose the correct answers in the table for each blank in the passage, then summarize the passage in three sentences. B. Go over your work in pairs; then take turns translating the sentences into English. The choices are: 1. a 下次 b 上次 c 每次; 2. a 第一次 b 前次 c 二次; 3. a 可能 b 不一定 c 不喜欢; 4. a 甚至 b 有点儿 c 根本; 5. a 随时 b 马上 c 过一会儿; 6. a 方便 b 礼貌 c 周到. The passage with my key filled in (the book gives no key):",
             examples=[D(CLZ, CLZ_E), D("上次放假，我第一次坐高铁从北京去青岛。高铁非常平稳，我根本感觉不到列车在运行。座位旁边有电源插座和无线上网，服务员也很周到。", "My three-sentence summary: Last holiday I rode the high-speed rail from Beijing to Qingdao for the first time. It was so smooth that I couldn’t feel the train moving. By the seat there were a power socket and wireless internet, and the attendants were thoughtful too. (mine)")]),
    ],
    exercises=[
        M("In the Activity 4 passage, which choice fills “___放假的时候，我坐高铁从北京去了青岛”?", "上次", ["下次", "每次", "前次"], "上次: last time."),
        M("Which choice fills “所以这是我___坐高铁”?", "第一次", ["前次", "二次", "每次"], "第一次: the first time."),
        M("Which choice fills “我___感觉不到列车是在以每小时二百多公里的速度运行”?", "根本", ["甚至", "有点儿", "已经"], "根本: at all."),
        M("Which choice fills “可以___给手机充电”?", "随时", ["马上", "过一会儿", "从来不"], "随时: at any time."),
        M("Which choice fills “他们的服务也很___”?", "周到", ["方便", "礼貌", "危险"], "周到: thoughtful."),
        M("How far is Beijing to Qingdao in the passage?", "About 700 kilometers", ["About 70 kilometers", "About 7,000 kilometers", "About 1,700 kilometers"], "差不多七百公里."),
        M("Which seat class did the writer ride?", "Second class", ["First class", "Business class", "Hard sleeper"], "我坐的是二等座."),
        M("What can the writer do by the seat?", "Charge a phone", ["Cook", "Sleep on a bed", "Watch a film on a big screen"], "座位旁边还有电源插座."),
        F("如果不是服务员告诉我，我根___感觉不到列车是在运行。", "本", PART, "根本: at all."),
        F("列车运行得非常平___。", "稳", PART, "平稳: smooth."),
    ],
)

# ------------------------------------------------------------------ 3. 次
CI1 = [("我第一次看到他是三年前。", "I first saw him three years ago."), ("我上次去纽约是坐飞机去的。", "Last time I went to New York I went by plane.")]
CI2 = [("我去过两次纽约。", "I’ve been to New York twice."), ("她已经给我打过三次电话了。", "She has already called me three times.")]
CK = [("甲：每次来北京，我都是坐高铁。你呢？乙：我这次是坐高铁来的，上次是坐飞机来的。下次再坐高铁。", "1. A: Every time I come to Beijing I take the high-speed rail. And you? B: This time I came by high-speed rail; last time I came by plane. Next time I’ll take the high-speed rail again. (key mine)"), ("甲：你第一次来蒙特雷是什么时候？乙：是六年前了。这是我第二次来蒙特雷。每次来我都会去渔人码头。", "2. A: When did you first come to Monterey? B: It was six years ago. This is my second time in Monterey. Every time I come I go to Fisherman’s Wharf. (mine)"),
      ("甲：你说昨天要给我打电话，怎么到现在才打过来？乙：昨天下午我给你打了两次，可是没人接啊！", "3. A: You said you’d call me yesterday; why did you only call now? B: Yesterday afternoon I called you twice, but nobody picked up! (mine)"), ("甲：你每年回老家几次？住几天？乙：我每年回老家两次，每次差不多一个星期。第一次是夏天，第二次是冬天。", "4. A: How many times a year do you go back to your hometown? How many days do you stay? B: I go back twice a year, about a week each time. The first time is summer, the second time winter. (mine)"),
      ("甲：上次打电话的时候，你说今年要回来过年。为什么到现在还不回来？乙：妈，最近我太忙了，回不去。下次您过生日，我一定回来。", "5. A: Last time you phoned you said you’d come back for the New Year this year. Why haven’t you come back yet? B: Mom, I’ve been too busy lately and can’t get back. Next time it’s your birthday I’ll definitely come back. (mine)")]
L3 = lesson(
    "Lesson 19 Presentation 2 grammar: more about the use of 次",
    "第一次 · 上次 · 下次 · 每次 · 两次 · specified and unspecified frequency",
    requires=[],
    cards=[
        card("More about the use of 次",
             "As a verbal measure word, 次 is used in two ways. Specified frequency (which time?): it tells us the specified frequency of a particular action and usually follows a specifier such as 第一次, 第三次, 这次, 上次 and 下次. Unspecified frequency (how many times?): it tells us how many times something happens and 次 usually follows a number.",
             examples=[D(z, e) for z, e in CI1 + CI2]),
        card("Grammar Activity 1 (Reading and Speaking)",
             "A. Complete the dialog using the expressions 几次, 这次, 上次, 下次, 每次, 第一次, 第二次 and 两次; some may be used more than once. B. Pair up and share your work; then take turns translating each exchange into English. The book prints the blanks and no key; my completed dialogs:",
             examples=[D(z, e) for z, e in CK]),
    ],
    exercises=[
        M("Which of these is a specifier telling which time?", "第一次", ["三次", "两次", "几次"], "第一次 follows a specifier."),
        M("Which tells how many times?", "两次", ["上次", "下次", "这次"], "Number + 次."),
        M("Which sentence means “I’ve been to New York twice”?", "我去过两次纽约", ["我第二次去纽约", "我下次去纽约", "我上次去纽约"], "Number + 次."),
        M("What does 上次 mean?", "Last time", ["Next time", "Every time", "Each person"], "上次."),
        M("Complete: 我每年回老家两次，___差不多一个星期。", "每次", ["上次", "这次", "几次"], "每次: each time."),
        M("Complete: 你第一次来蒙特雷是什么时候？这是我___来蒙特雷。", "第二次", ["第一次", "下次", "每次"], "第二次: the second time."),
        M("Complete: 昨天下午我给你打了___，可是没人接啊！", "两次", ["上次", "第一次", "下次"], "两次: twice."),
        M("In “___来北京，我都是坐高铁”, which is best?", "每次", ["这次", "下次", "第一次"], "每次…都…."),
        F("她已经给我打过三___电话了。", "次", PART, "三次: three times."),
        F("下___您过生日，我一定回来。", "次", PART, "下次: next time."),
    ],
)

# ------------------------------------------------------------------ 4. 根本
GB = [("我根本就不累。", "1. I’m not tired at all."), ("雨下得根本就不大。", "2. The rain isn’t heavy at all."), ("我根本就不认识他。", "3. I don’t know him at all."), ("这儿离电影院根本就不远。", "4. It’s not far from here to the cinema at all."), ("老刘说要给我打电话，可是根本就没打。", "5. Lao Liu said he’d call me but didn’t call at all.")]
GA2 = [("甲：对不起，开会的事我全忘了。乙：没关系，我根本就没打算去开会。", "1. A: Sorry, I forgot all about the meeting. B: It’s OK; I didn’t plan to go to the meeting at all. (the book leaves B blank; the answers are mine)"), ("甲：小王说你是他的朋友。乙：我根本就不认识他。", "2. A: Xiao Wang says you’re his friend. B: I don’t know him at all. (mine)"), ("甲：听说你最近根本就不锻炼身体。乙：不对，昨天我还去操场跑步了呢。", "3. A: I hear you haven’t been exercising at all lately. B: Not true, I even went running on the sports field yesterday. (the book prints B; A is mine)"),
       ("甲：医生要你在家休息，你上午为什么去商店买东西？乙：我根本就没觉得自己有病啊。", "4. A: The doctor told you to rest at home; why did you go to the shop to buy things this morning? B: I didn’t feel sick at all. (mine)"), ("甲：他英文说得根本就不好。乙：他不是去过加拿大吗？我还以为他说英文说得很好呢。", "5. A: His English is not good at all. B: Hasn’t he been to Canada? I thought he spoke English very well. (the book prints B; A is mine)"),
       ("甲：昨天晚上你为什么那么晚才睡觉？是不是又玩儿游戏了？乙：我根本就没玩儿游戏，我在做作业。", "6. A: Why did you go to bed so late last night? Did you play games again? B: I didn’t play games at all; I was doing homework. (mine)")]
GA3 = [("姐姐：你又吃了我的巧克力！男孩：我根本就没吃你的巧克力。", "1. Sister: You ate my chocolate again! Boy: I didn’t eat your chocolate at all. (sample scenario, mine)"), ("姐姐：你把我的手机弄坏了！男孩：我根本就没动你的手机。", "2. Sister: You broke my phone! Boy: I didn’t touch your phone at all. (mine)"), ("姐姐：昨天晚上你很晚才睡觉，还玩儿游戏了。男孩：我根本就没玩儿游戏，我九点就睡了。", "3. Sister: You went to bed late last night and played games. Boy: I didn’t play games at all; I was asleep at nine. (mine)"), ("姐姐：你又忘了做作业！男孩：我根本就没忘，早就做完了。", "4. Sister: You forgot to do your homework again! Boy: I didn’t forget at all; I finished long ago. (mine)")]
L4 = lesson(
    "Lesson 19 Presentation 2 grammar: the adverb 根本",
    "根本就不 · 根本就没 · not at all",
    requires=[],
    cards=[
        card("The adverb 根本",
             "The adverb 根本 means “at all” and is usually used to emphasize negation; thus it is very similar to the expression “一点儿也不”. 根本 often appears before a verb or as an adjective in a negative sentence and is usually followed by 就. Examples:",
             examples=[D(z, e) for z, e in GB]),
        card("Grammar Activity 2 (Writing, Speaking and Reading)",
             "A. Complete the following sentences using 根本 (the book leaves the answers blank, then prints possible answers that are not in the text I have; my fills below). B. Pair up and check your work; take turns translating the exchanges into English.",
             examples=[D(z, e) for z, e in GA2]),
        card("Grammar Activity 3 (Writing and Speaking)",
             "A. A little boy has a big sister who continually criticizes him for things she thinks he has done. In Chinese, list four scenarios in which the sister criticizes her brother for doing things but he categorically denies doing them (姐姐 / 男孩). B. Pair up and share your work; choose two of your partner’s scenarios and share them with the class. (A cartoon picture, not included.) My sample scenarios:",
             examples=[D(z, e) for z, e in GA3]),
    ],
    exercises=[
        M("What does 根本 mean?", "At all (with a negative)", ["Very much", "Sometimes", "Already"], "根本: at all."),
        M("Which expression is it similar to?", "一点儿也不", ["非常", "已经", "又"], "根本就不 ≈ 一点儿也不."),
        M("What usually follows 根本?", "就", ["了", "吗", "呢"], "根本就不/没."),
        M("What does “我根本就不认识他” mean?", "I don’t know him at all", ["I know him well", "I met him yesterday", "He doesn’t know me"], "根本就不认识."),
        M("What does “雨下得根本就不大” mean?", "The rain isn’t heavy at all", ["The rain is very heavy", "It rained all day", "It will rain tomorrow"], "根本就不大."),
        M("What does “老刘根本就没打” mean?", "Lao Liu didn’t call at all", ["Lao Liu called twice", "Lao Liu will call", "Lao Liu hit me"], "根本就没打."),
        M("How does the boy deny, in the book’s scenarios?", "With 根本就没…", ["With 早就…", "With 反正…", "With 一定…"], "根本就没…"),
        M("Is “我根本就很累” correct?", "No; 根本 goes with a negative", ["Yes", "Only in questions", "Only in the past"], "根本 emphasizes negation."),
        F("这儿离电影院根___就不远。", "本", PART, "根本: at all."),
        F("我根本就不认___他。", "识", PART, "认识: know."),
    ],
)

# ------------------------------------------------------------------ 5. 一定 and 会
YD1 = [("明天一定很冷。", "Tomorrow it will definitely be cold."), ("明天会很冷。", "Tomorrow it will be cold."), ("明天一定下雨。", "It will definitely rain tomorrow. (the speaker is certain)"), ("明天会下雨。", "It will rain tomorrow. (the speaker thinks it very likely)"), ("明天可能会下雨。", "It might rain tomorrow."), ("明天大概会下雨。", "It will probably rain tomorrow."), ("明天一定会下雨。", "It will surely rain tomorrow. (very certain of the likelihood)")]
YD4 = [("夏威夷的风景太漂亮了！没人不喜欢。到了那里你一定会不想回来了。", "1. Hawaii’s scenery is so beautiful! Nobody doesn’t like it. When you get there you will surely not want to come back. (changed 可能 to 一定会; mine)"), ("今天下午一直在下雨，明天可能还会下雨。", "2. It has been raining all afternoon; tomorrow it might still rain. (changed 一定 to 可能…会; mine)"), ("如果早饭吃得很少，中午你可能会非常饿。", "3. If you eat very little for breakfast, at noon you might be very hungry. (changed 一定会 to 可能会; mine)"),
       ("他学中文歌，看中文电影。我想他一定喜欢学中文。", "4. He learns Chinese songs and watches Chinese movies. I think he surely likes learning Chinese. (changed 可能 to 一定; mine)"), ("如果你中文说得很好，你的听力可能会更好。", "5. If you speak Chinese very well, your listening might be even better. (changed 一定 to 可能会; mine)")]
L5 = lesson(
    "Lesson 19 Presentation 2 grammar: the adverb 一定 and the modal verb 会 for prediction",
    "一定 · 会 · 可能会 · 一定会 · how certain the speaker is",
    requires=[],
    cards=[
        card("The adverb 一定 and the modal verb 会 expressing prediction",
             "Both 一定 and 会 can be used for prediction, for example 明天一定很冷 and 明天会很冷. 一定 indicates something the speaker thinks will definitely happen: 明天一定下雨 says the speaker is certain it will rain tomorrow. 会 indicates the likelihood that something will happen: 明天会下雨 says the speaker thinks it very likely that it will rain tomorrow. One can use 可能, 大概 and other words before 会 to stress likelihood, such as 明天可能会下雨 and 明天大概会下雨. 一定会 indicates the speaker is very certain of the likelihood: 明天一定会下雨 says the speaker is certain it is very likely that it will rain tomorrow.",
             examples=[D(z, e) for z, e in YD1]),
        card("Grammar Activity 4 (Reading, Writing and Speaking)",
             "A. 一定 and 会 indicate how certain a speaker thinks that something is true or something will happen. Read the five sentences that use 一定 or 会; with a classmate, revise each sentence to change the speaker’s tone, then take turns translating your revisions into English. The book’s five originals: 1. 夏威夷的风景太漂亮了！没人不喜欢。到了那里你可能就不想回来了。 2. 今天下午一直在下雨，明天一定还要下雨。 3. 如果早饭吃得很少，中午你一定会非常饿。 4. 他学中文歌，看中文电影。我想他可能喜欢学中文。 5. 如果你中文说得很好，你的听力一定更好。 B. Pair up and share your work; then go over the suggested revisions. The book’s suggested revisions are not in the text, so these are mine:",
             examples=[D(z, e) for z, e in YD4]),
        card("Grammar Activity 5 (Listening, Speaking and Reading)",
             "A. Listen to the dialog and answer the questions: 1. What is the relationship between the two speakers? 2. What event is being planned and who will organize it? 3. Was the female speaker sure that the male speaker travelled by air? Why? 4. Will the party start on time? Why or why not? 5. What is said about Er Ge (二哥)? 6. Where will the male speaker buy the cake? Why? B. Pair up and share your answers; then go over the script and refine your work. (Audio, not included; the book prints no script.)"),
    ],
    exercises=[
        M("Which indicates what the speaker thinks will definitely happen?", "一定", ["会", "可能", "大概"], "一定: definitely."),
        M("Which indicates the likelihood that something will happen?", "会", ["一定", "一定会", "必须"], "会: likelihood."),
        M("What does “明天一定下雨” say?", "The speaker is certain it will rain tomorrow", ["It may rain tomorrow", "It rained yesterday", "It won’t rain tomorrow"], "一定."),
        M("What does “明天会下雨” say?", "The speaker thinks it very likely it will rain", ["The speaker is sure it will rain", "It never rains", "It rained today"], "会."),
        M("Which words can be put before 会 to stress likelihood?", "可能 and 大概", ["已经 and 刚", "不 and 没", "很 and 太"], "可能会; 大概会."),
        M("Which is the most certain?", "明天一定会下雨", ["明天可能会下雨", "明天大概会下雨", "明天会下雨"], "一定会."),
        M("How would you soften “明天一定还要下雨”?", "明天可能还会下雨", ["明天一定还会下雨", "明天不会下雨", "明天已经下雨"], "可能…会."),
        M("What does “明天大概会下雨” mean?", "It will probably rain tomorrow", ["It will certainly rain", "It won’t rain", "It rained yesterday"], "大概会."),
        F("如果早饭吃得很少，中午你一定___非常饿。", "会", PART, "一定会: surely will."),
        F("我想他可___喜欢学中文。", "能", PART, "可能: maybe."),
    ],
)

# ------------------------------------------------------------------ 6. 等
DE = [("等我一到家就给你打电话。", "1. As soon as I get home I’ll call you."), ("等(到)作业做完了我就上床睡觉。", "2. When my homework is done I’ll go to bed."), ("等(到)太阳出来了咱们再去散步吧。", "3. Let’s go for a walk once the sun comes out."), ("等(到)秋天到了他儿子就会来看他。", "4. When autumn comes his son will come to see him."), ("等(到)老张来电话的时候，你问问他打算什么时候回中国。", "5. When Lao Zhang calls, ask him when he plans to go back to China.")]
DE6 = [("等我跟你打完电话就去锻炼。", "1. When I finish talking to you on the phone I’ll go work out. (key mine)"), ("等老张他们到了咱们就开始吃饭。", "2. When Lao Zhang and the others arrive we’ll start eating. (mine)"), ("等连长同意了我就买回家的飞机票。", "3. When the company commander agrees I’ll buy the plane ticket home. (mine)"), ("等我值完班再做作业好吗？", "4. May I do my homework after I finish my shift? (mine)"), ("等飞机下了我马上就告诉你。", "5. As soon as the plane lands I’ll tell you right away. (mine)")]
L6 = lesson(
    "Lesson 19 Presentation 2 grammar: 等 expressing “when”",
    "等(到) · 等…就… · 等…再… · ordering the words",
    requires=[],
    cards=[
        card("等 expressing “when”",
             "In addition to expressing “wait”, 等 can also be used to express “when”, especially in daily conversation. 等到 can also be used to express the same idea. Examples:",
             examples=[D(z, e) for z, e in DE]),
        card("Grammar Activity 6 (Reading and Speaking)",
             "A. Order the provided words in the correct sequence to make logical sentences: 1. 去锻炼 电话 / 我 / 打完 / 就 / 跟你 / 等 2. 吃饭 咱们 / 老张他们 / 就 / 等 / 到了 / 开始 3. 飞机票 我就 / 等 / 回家的 / 连长 / 买 / 同意了 4. 好吗 等 / 再 / 我 / 作业 / 值完班 / 做 5. 就 我 / 飞机 / 你 / 告诉 / 等 / 下了 / 马上 B. Pair up and share your work; check against the suggested answer keys; translate each sentence into English and back into Chinese. The book’s keys are not in the text, so these are mine:",
             examples=[D(z, e) for z, e in DE6]),
        card("Grammar Activity 7 (Writing and Speaking)",
             "A. Using 等, write five statements that say Event A will happen after Event B. B. Pair up; Student A reads his or her sentences one by one and Student B translates them verbally into English; repeat and take turns. (A picture of an alarm clock, not included; your own sentences.)"),
    ],
    exercises=[
        M("What does 等 mean in 等我一到家就给你打电话?", "When", ["Wait for", "Equal", "Class"], "等 can mean “when”."),
        M("What can replace 等 with the same meaning?", "等到", ["到等", "等于", "等候"], "等(到)."),
        M("Which sentence means “When my homework is done I’ll go to bed”?", "等作业做完了我就上床睡觉", ["我等作业做完了就睡觉上床", "作业等做完了我就上床睡觉", "上床睡觉等作业做完了我就"], "等 + event B, 就 + event A."),
        M("Which is the correct ordering of 等 飞机 下了 我 马上 就 告诉 你?", "等飞机下了我马上就告诉你", ["我等飞机下了马上就告诉你", "飞机等下了我马上就告诉你", "等我飞机下了马上就告诉你"], "Key 5."),
        M("In 等我值完班再做作业好吗？, what comes first?", "Finishing the shift", ["Doing homework", "Asking permission", "Going home"], "等…再…."),
        M("What does “等(到)秋天到了他儿子就会来看他” mean?", "When autumn comes his son will visit him", ["His son visited in autumn", "He visits his son", "His son hates autumn"], "等(到)…就…."),
        M("Which word often follows the 等-clause?", "就", ["了", "吗", "呢"], "等…就…."),
        M("In 等老张来电话的时候, 等 means?", "When", ["Wait", "Equal", "Rank"], "等 = when."),
        F("等我一到家___给你打电话。", "就", PART, "等…就…."),
        F("等(到)太阳出来了咱们___去散步吧。", "再", PART, "等…再…."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
SLOW = ["在四川省的一个山区，有一条火车线路，火车的行驶速度非常慢。这条线路一共是三百五十三公里，中间有二十六个车站，火车每小时只走四十公里，所以人们叫它“小慢车”。",
        "虽然速度很慢，但是这条火车线路对住在那里的人来说太重要了。一位老人说，她二十五岁结婚后一直住在山里，很长时间，她每次回母亲家要走一天多的山路。后来有了“小慢车”，只要四十多分钟她就可以到家了。",
        "这儿很多人也用“小慢车”运东西。比如去城里卖东西的人，会把一包一包的水果、蔬菜或别的东西放到车上，运到他们要去的地方。", "到了星期五和星期天，很多孩子会坐这趟“校车”回家或上学。在车厢里你会看到孩子们有的在做作业，有的在看书。",
        "为什么大家都喜欢“小慢车”？第一是因为车站多，在附近来往很方便。第二是因为它太便宜了。从一九九五年以来票价没有变过。你要是坐它去近的地方，只需要花两元钱。"]
SLOW_E = ["1. In a mountain area of Sichuan Province there is a railway line on which the trains run very slowly. This line is 353 kilometers in all, with 26 stations in between, and the trains go only 40 kilometers an hour, so people call it the “Little Slow Train”. (the underlined sentence 1; the book writes the numbers as digits)",
          "2. Although it is slow, this railway line is extremely important to the people living there. An old woman said that after she married at 25 she lived in the mountains all along; for a long time each trip back to her mother’s home took more than a day on mountain roads. Later, with the “Little Slow Train”, it takes only a little over 40 minutes to reach home. (the underlined sentence 2 begins at 很长时间)",
          "3. Many people here also use the “Little Slow Train” to carry things. For example, people going to town to sell things put bundles of fruit, vegetables or other things on the train and send them to where they are going. (the underlined sentence 3 begins at 比如)",
          "4. On Fridays and Sundays, many children ride this “school bus” home or to school. In the carriages you will see some children doing homework and some reading. (the underlined sentence 4)",
          "5. Why does everyone like the “Little Slow Train”? First, because there are many stations and getting around nearby is convenient. Second, because it is so cheap. The fare has not changed since 1995. If you take it to a nearby place you only need to spend two yuan. (the underlined sentence 5 is 从1995年以来票价没有变过)"]
RPT = [("记者", "请问这条火车线路有多长？", "How long is this railway line? (sample dialog, mine)"), ("乘客", "一共三百五十三公里，中间有二十六个车站，火车每小时只走四十公里，所以人们叫它“小慢车”。", "353 kilometers in all, with 26 stations between, and the train goes only 40 km an hour, so people call it the “Little Slow Train”."), ("记者", "它对您来说重要吗？", "Is it important to you?"), ("乘客", "太重要了！以前我回母亲家要走一天多的山路，现在只要四十多分钟。", "Very! I used to need more than a day on mountain roads to reach my mother’s; now it only takes a little over 40 minutes."),
       ("记者", "为什么大家都喜欢它？", "Why does everyone like it?"), ("乘客", "第一是因为车站多，来往很方便。第二是因为它很便宜，只需要花两元钱。", "First, there are many stations and getting around is convenient. Second, it is cheap; it only costs two yuan.")]
GUESS = table(["表达", "意思 (my guess for the book’s five expressions)"],
              [["厉害", "impressive; formidable (她说中文说得比很多中国人还好，真厉害！)"], ["说起来容易做起来难", "easier said than done"], ["硬币", "coin (硬 as in 硬卧, 币 as in 人民币)"], ["倒 (dǎo)", "to fall down, to collapse (一场大雨以后，那个老房子倒了。)"], ["级", "level, rank (省一级的地方: a place at the provincial level)"]],
              title="Skill Integration Activity 1 A: guess the meanings (the book prints only the expressions; the meanings are mine)")
AMT = table(["线路", "基本信息 (Basic Info)", "座位、票价、服务"], [["洛杉矶到旧金山", "", ""], ["纽约到华盛顿", "", ""]], title="Skill Integration Activity 3 A: Amtrak routes (blank in the book; collected online by the student)")
L7 = lesson(
    "Lesson 19 Presentation 2 skill integration: the Little Slow Train",
    "小慢车 · 厉害 说起来容易做起来难 硬币 倒 级 · 两条美国铁路线",
    requires=[],
    cards=[
        card("Skill Integration Activity 1 (Listening, Writing, Speaking and Reading)",
             "A. Pair up and guess the meaning of the following expressions: 1. 厉害 (e.g. 她说中文说得比很多中国人还好，真厉害！) 2. 说起来容易做起来难。 3. 硬币 (you’ve learned 硬 in 硬卧, and 币 in 人民币) 4. 倒 (dǎo; e.g. 一场大雨以后，那个老房子倒了。) 5. 级 (e.g. you’ve learned 六年级; what does it mean in 省一级的地方?) B. Listen to the dialog and answer: 1. What is the topic of this dialog? 2. How long is China’s high-speed rail? 3. How common is high-speed rail in China? C. Pair up and share your answers; listen again and list the details in the table (琳达的体验, 另一位外国朋友的体验, 工程师们的努力). D. Write a text message to your Chinese teacher sharing what you’ve learned from the conversation between Linda and Mr. Zhang. E. Go over the script and revise your text message. (Audio, not included; the book prints no script.)",
             tables=[GUESS]),
        card("Skill Integration Activity 2 (Reading, Speaking and Writing): 小慢车",
             "A. Read the passage below; write an English summary and consult your dictionary if necessary. (Photographs of the train, not included; the book underlines five sentences, which are numbered 1) to 5) in the text; the book writes the numbers as digits.) B. Pair up and, in Chinese, ask each other: 1. 这篇文章是关于什么的？ 2. 为什么住在那儿的人叫那样的火车“小慢车”？ 3. “小慢车”对那儿的老百姓为什么非常重要？ 4. 那儿的老百姓为什么喜欢“小慢车”？ C. Take turns translating the underlined sentences into English; your partner translates them back into Chinese without looking at the passage. D. Work with your partner to rewrite the passage as a conversation between a reporter and a local passenger and act it out for the class. The passage:",
             examples=[D(z, e) for z, e in zip(SLOW, SLOW_E)]),
        card("A conversation between a reporter and a passenger (my sample for Step D)",
             "The book leaves the five turns blank; this is my sample.",
             examples=dlg(RPT)),
        card("Skill Integration Activity 3 (Writing and Speaking)",
             "A. Pair up. Each partner goes online and collects information about one of the following Amtrak train routes in the U.S. (distance, speed, major train stations, ticket price, seat options, services and so on) and writes it in the table. B. You play the role of a traveler from China and your partner is your old classmate now living in America; ask your partner questions about the train line and take notes; then switch roles. C. You want to try your partner’s rail line. Leave a voice mail for your brother in China telling him what the route is like and your plans to ride the line next week; share your voice mail with your partner. (A picture, not included; your own information.)",
             tables=[AMT]),
    ],
    exercises=[
        M("Where is the Little Slow Train?", "In a mountain area of Sichuan Province", ["In Beijing", "In Hong Kong", "In Tibet"], "在四川省的一个山区."),
        M("How many kilometers is the line?", "353", ["53", "35", "3,530"], "三百五十三公里."),
        M("How many stations are on the line?", "Twenty-six", ["Sixteen", "Sixty-two", "Thirty-six"], "二十六个车站."),
        M("How fast does the train go?", "40 kilometers an hour", ["140 kilometers an hour", "4 kilometers an hour", "400 kilometers an hour"], "每小时只走四十公里."),
        M("Why do people call it “小慢车”?", "It is very slow", ["It is very small only", "It is the cheapest", "It is the oldest"], "速度非常慢."),
        M("How long did the old woman once need to walk to her mother’s home?", "More than a day", ["Half an hour", "Two hours", "A week"], "要走一天多的山路."),
        M("How long does the train take her now?", "A little over 40 minutes", ["More than a day", "Five minutes", "Three hours"], "只要四十多分钟."),
        M("What do children do on the train on Friday and Sunday?", "Go home or to school; some do homework", ["Sell fruit", "Take photos", "Work"], "坐这趟“校车”回家或上学."),
        M("Since when has the fare not changed?", "Since 1995", ["Since 2005", "Since 1985", "Since last year"], "从一九九五年以来票价没有变过."),
        M("How much does a short trip cost?", "Two yuan", ["Twenty yuan", "Two hundred yuan", "Free"], "只需要花两元钱."),
        M("What does 硬币 mean?", "Coin", ["Hard bed", "Paper money", "Credit card"], "硬 + 币: coin."),
        F("这条线路一共是三百五十三公___，中间有二十六个车站。", "里", PART, "公里: kilometers."),
        F("火车每小时只___四十公里，所以人们叫它“小慢车”。", "走", PART, "走: go."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
CTX2 = [("中国高铁的速度快不快，时速是多少，从北京到另外一个大城市需要多长时间？", "1. Is China’s high-speed rail fast? What is the speed per hour? How long does it take to go from Beijing to another big city?"), ("在中国坐高铁安全吗？你怎么知道的？", "2. Is it safe to take the high-speed rail in China? How do you know?"), ("中国高铁里面的设施和服务怎么样？", "3. What are the facilities and service like inside China’s high-speed rail?"), ("在中国怎么订高铁车票？", "4. How do you book high-speed rail tickets in China?")]
HINT = table(["", "Mary (in Canada)", "Joe (in the U.S.)"],
             [["Personal info", "35 years old; in China for over 10 years; likes Tai chi", "29 years old; in China for over 8 years; likes Chinese medicine; girlfriend is Chinese"], ["How often travel on high-speed rail", "every couple of months; usually takes it when going to places over 200 km away", "weekly, attending meetings and seeing friends"], ["Train stations", "close and convenient; services good; can also buy things there", "new, big, clean and crowded; food quite expensive"], ["On the train", "quiet, clean, good services; internet sometimes not stable; wishes more choices for food", "feels happy and comfortable; often works on his computer; wishes conductors speak some English"]],
             title="Using Chinese in Context Activity 2 C: hints for the interview (the book’s English table; as printed after matching the columns)")
CONDUCT = "十月初国庆节期间，人们不是出去旅游，就是在家休息。但是，今年不到三十岁的张萌萌却更忙了。她是高铁的列车长，放假这几天她每天都要工作十几个小时。张萌萌是四川人，十几年前当上了列车服务员，由于她工作努力，素质优秀，两年前成了一名高铁列车长。国庆节这天，她早上五点就起床了，为上班做准备，六点到了火车站的站台接车。那天她服务了一班又一班列车，最后一班到达重庆的时候，已经是二十三点三十二分了。下车以后，她和车上的工作人员又一起开会，总结一天的工作，看看有没有做得不够好的地方。“虽然工作很累，但我们都觉得很愉快，”张萌萌说。国庆节那几天旅客出行非常多，她和车上的工作人员每天都要工作十个小时以上。她觉得，节日里让每位旅客安全舒适地出行，对她和同事们来说是最重要的事。"
CONDUCT_E = "In early October, during the National Day holiday, people either go out traveling or rest at home. But this year Zhang Mengmeng, who is not yet thirty, was even busier. She is a high-speed rail conductor, and over the holiday days she had to work a dozen or more hours a day. Zhang Mengmeng is from Sichuan; she became a train attendant more than ten years ago, and because she works hard and has excellent qualities she became a high-speed rail conductor two years ago. On National Day she got up at five in the morning to prepare for work, and at six she was at the station platform to meet the train. That day she served one train after another, and when the last one reached Chongqing it was already 23:32. After getting off, she and the staff on the train held a meeting together to sum up the day’s work and see whether anything had not been done well enough. “Although the work is tiring, we all feel very happy,” Zhang Mengmeng said. During those National Day days there were very many travelers, and she and the staff on the train had to work more than ten hours a day. She feels that letting every passenger travel safely and comfortably during the holiday is the most important thing for her and her colleagues. (the book’s title is 十八岁高铁列车长繁忙的假日, “An eighteen-year-old high-speed rail conductor’s busy holiday”; the book writes the times and 10 as digits)"
IQ = [("你多大了？你是哪里人？", "How old are you? Where are you from? (sample interview questions, mine)"), ("你是什么时候当上列车长的？", "When did you become a conductor?"), ("国庆节那天你几点起床？几点下班？", "What time did you get up on National Day? What time did you finish?"), ("你每天工作多长时间？累不累？", "How many hours a day do you work? Are you tired?"), ("你觉得什么事最重要？", "What do you think is most important?")]
L8 = lesson(
    "Lesson 19 Presentation 2 using Chinese in context: surveys and a young conductor",
    "高铁的速度 · Mary 和 Joe 的出行 · 十八岁高铁列车长",
    requires=[],
    cards=[
        card("Using Chinese in Context Activity 1 (Reading and Speaking)",
             "Pair up and take turns telling your partner what you would say in the following situations. Provide as many details as possible using two to four sentences. (A photograph of a high-speed train, not included.)",
             examples=[D(z, e) for z, e in CTX2]),
        card("Using Chinese in Context Activity 2 (Listening, Writing, Reading and Speaking)",
             "You are the manager of an international consulting firm, and China State Railway Co. asks you to conduct a survey with open-ended questions for foreigners about their experiences taking the high-speed rail in China. Soon after you sent out the survey you receive two voice messages, one from Mary in Canada and one from Joe in the U.S. A. Pair up; each partner listens to one of the messages and writes the key information in the table 关于中国高铁 (Mary: 好的地方, 不够好的地方; Joe: 选座位, 不够好的地方). Before listening, find the meanings of these words: 出行, 市区, 舒适, 标识 (mine: to travel out; urban area; comfortable; sign). B. Share your notes with your partner; go over the scripts; then prepare five questions for an in-depth interview. C. Conduct the interview; your partner plays the interviewee, using the hints in the table below. D. Write an email to your customer summarizing the in-depth interview (TO, CC, Subject). (Audio, not included; the book prints no script, only the hints table.)",
             tables=[HINT]),
        card("Using Chinese in Context Activity 3 (Reading, Writing and Speaking)",
             "You write blogs on the tourist industry for a magazine and your job sometimes takes you to China. One day in Beijing you saw a brief news article online, with images; you were quite impressed with the young conductor Zhang Mengmeng. Read the title and examine the images (not included): 十八岁高铁列车长繁忙的假日. A. If you were to interview this person, what questions would you ask? Write five questions and share your work with a classmate. B. You will interview Zhang Mengmeng soon; first read the report below and consult your dictionary for any unknown words. C. Conduct the interview; your partner plays Zhang Mengmeng. D. Write your dialog (记者 / 列车长) and act it out for the class. The report (the book writes the numbers as digits):",
             examples=[D(CONDUCT, CONDUCT_E)] + [D(z, e) for z, e in IQ]),
    ],
    exercises=[
        M("Who is Zhang Mengmeng?", "A high-speed rail conductor", ["A reporter", "A pilot", "A doctor"], "她是高铁的列车长."),
        M("Where is she from?", "Sichuan", ["Beijing", "Shanghai", "Chongqing"], "张萌萌是四川人."),
        M("How long has she been a conductor?", "Two years", ["Ten years", "Half a year", "Twenty years"], "两年前成了一名高铁列车长."),
        M("What time did she get up on National Day?", "Five in the morning", ["Seven in the morning", "Noon", "Midnight"], "早上五点就起床了."),
        M("What time did the last train reach Chongqing?", "23:32", ["06:00", "12:30", "20:00"], "已经是二十三点三十二分了."),
        M("What did she do after getting off?", "Held a meeting with the staff to sum up the day", ["Went on holiday", "Went home immediately", "Wrote a book"], "和车上的工作人员又一起开会."),
        M("What does she think is most important during the holiday?", "Letting every passenger travel safely and comfortably", ["Selling many tickets", "Finishing early", "Taking a holiday"], "让每位旅客安全舒适地出行."),
        M("In Mary’s hints, how often does she take the high-speed rail?", "Every couple of months", ["Weekly", "Every day", "Never"], "Hint table."),
        M("What does Joe wish the conductors could do?", "Speak some English", ["Sing", "Serve more food", "Open windows"], "Hint table."),
        F("她和车上的工作人___又一起开会，总结一天的工作。", "员", PART, "工作人员: staff."),
        F("由于她工作努力，素质优秀，两年前成了一名高铁列车___。", "长", PART, "列车长: conductor."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 19 Presentation 2 vocabulary", "25 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十九课 Presentation 2: 高铁体验, 次, 根本, 一定/会, 等, the Little Slow Train", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
