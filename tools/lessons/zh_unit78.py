"""Unit 78: Lesson 25 (Smart Life), Presentation 3 and Area Studies: the Didi ride-hailing passage with its activities, 根据 and 据, 就是 and 也就是 (说), 来说, the suffix 化,
the skill-integration tasks (the hitch-driver interview, the ride-hailing driver's story, the American businessman's Didi experience), the using-Chinese tasks, the vocabulary list and
the Area Studies reading on tourism and transportation. Audio, pictures and websites are not included; numbers the book writes as digits are spelled out in Chinese text;
answers that the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l25_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('不得不', 1, 'de2'), ('的士', 0, 'di1'), ('张中行', 2, 'xing2'), ('得分', 0, 'de2'), ('聪明了', 2, 'le5')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] == "目的地" or zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 3
P3 = [("以前在中国，大家出行主要靠公交车和出租车。现在有了更方便的选择，最受欢迎的就是“滴滴出行”。“滴滴出行”是一个网约车平台，提供出租车、顺风车、拼车等服务。", "Paragraph 1: In the past in China, everyone traveled mainly by bus and taxi. Now there are more convenient choices, and the most popular is “Didi Chuxing.” Didi Chuxing is a ride-hailing platform that provides taxi, hitchhiking, carpooling and other services. (translations in this card are mine)"),
      ("“滴滴”出现以后，乘客可以用智能手机直接预约叫车，省去了很多等候的时间，因为“滴滴”能够精确定位，准时到达，让你轻松出发。另外，“滴滴”还可以根据乘客需要，提供特别的服务，比如大件行李、宠物或是儿童座椅。他们甚至还有代驾服务，就是代驾司机开着车主的车，把喝过酒或醉酒的车主送回家。", "Paragraph 2: After Didi appeared, passengers can use a smartphone to book a ride directly, saving a lot of waiting time, because Didi can locate accurately and arrive on time, letting you set off with ease. In addition, Didi can also provide special services according to passengers’ needs, such as large pieces of luggage, pets or child seats. They even have a designated-driver service, that is, the designated driver drives the car owner’s car and takes an owner who has been drinking or is drunk home."),
      ("“滴滴”除了为人们提供便利的出行服务以外，也为很多人提供了工作机会，增加了他们的收入。一般来说，“滴滴”司机每月的收入能有四千到五千元人民币。", "Paragraph 3: Besides providing people with convenient travel services, Didi has also provided jobs for many people and increased their income. Generally speaking, a Didi driver’s monthly income can reach four to five thousand yuan. (the book writes 4000 and 5000 in digits)"),
      ("以后的网约车会更加智能化，现在上海已经出现了“滴滴”无人驾驶出租车。新的人工智能会更好地为乘客和司机服务。", "Paragraph 4: In future ride-hailing will become even more intelligent; driverless Didi taxis have already appeared in Shanghai. The new artificial intelligence will serve passengers and drivers even better.")]
KEY3 = [("滴滴出行这个网约车平台，还有以前和现在出行方式的变化", "A1 (mine): the topic is the ride-hailing platform Didi Chuxing; transport has changed from buses and taxis to ride-hailing apps."),
        ("出租车、顺风车、拼车", "B1 (mine): three services: taxis, hitchhiking and carpooling."),
        ("用手机预约，省去等候时间，精确定位，准时到达，轻松出发，还有特别服务", "B2 (mine): benefits: booking by phone, saving waiting time, accurate positioning, punctual arrival, relaxed departure, and special services."),
        ("无人驾驶出租车", "B3 (mine): driverless taxis in Shanghai.")]
WT = table(["词", "我的相关词语"], [["网约车", "出租车、顺风车、拼车"], ["代驾", "代购、代理、代表"], ["宠物", "动物、食物、礼物"], ["喝酒", "啤酒、白酒、酒店"], ["无人车", "无人机、无人驾驶、无人商店"], ["工作机会", "机会、工作、就业机会"]],
           title="Activity 2: three related words for each (my list; the book’s columns hold 车, 代, 物, 酒, 无人 and 机会 and are blank)", say=[0, 1])
MT = table(["提供", "精确", "准时", "轻松", "根据", "增加", "智能"], [["服务", "定位", "到达", "出发", "需要", "收入", "手机"]],
           title="Activity 3: my matching (the book’s Column B is A. 到达, B. 收入, C. 服务, D. 定位, E. 手机, F. 需要, G. 出发)", say=[0, 1, 2, 3, 4, 5, 6])
S4 = [("以前在美国，大家出行主要靠开车；现在，最受欢迎的是网约车；以后，大家也可能会坐无人驾驶的汽车。", "1. In the past in America everyone traveled mainly by driving; now the most popular is ride-hailing; in future people may also ride in driverless cars. (my completion)"),
      ("网约车平台提供出租车、拼车等服务，还有特别服务。乘客可以用手机叫车。", "2. Ride-hailing platforms provide taxi, carpool and other services, and also special services. Passengers can call a car with their phone. (my completion)"),
      ("因为网约车在中国很流行，“滴滴出行”甚至还有代驾服务，就是代驾司机开着车主的车，把喝过酒的车主送回家。", "3. Because ride-hailing is very popular in China, Didi Chuxing even has a designated-driver service, that is, the designated driver drives the owner’s car and takes the owner who has been drinking home. (my completion)"),
      ("美国的两大网约车平台除了提供方便的出行服务以外，也为网约车司机提供了工作机会。一般来说，司机的收入比在餐馆打工多一些。", "4. Besides providing convenient travel services, America’s two big ride-hailing platforms also provide jobs for ride-hailing drivers. Generally speaking, the drivers’ income is a bit more than working in a restaurant. (my completion)")]
L1 = lesson(
    "Lesson 25 Presentation 3: ride-hailing with Didi",
    "以前在中国 出行靠公交车和出租车 · 滴滴出行 · 网约车 顺风车 拼车 · 代驾服务 · 无人驾驶出租车",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. What mobile transportation services, platforms or apps do you use? B. What mobile apps do you use for ridesharing? C. How do you compare ride-hailing apps and services with traditional modes of transportation like taxis or buses? (Four pictures are not included.)"),
        card("Presentation 3: 滴滴出行", "The book also prints the passage in traditional characters. The translations are mine.", examples=[D(z, e) for z, e in P3]),
        card("Activity 1 (Listening)",
             "A. Global Listening: Listen to Presentation 3 once through and answer the questions. 1. What is the main topic of the passage? 2. How have transportation options changed in China in recent years? B. Detailed Listening: Listen to Presentation 3 again and answer the questions. 1. List three services the platform featured in the passage provides. 2. What are four benefits of using this platform? 3. What new service does the platform provide in Shanghai? (Audio, not included; my answers from the text:)",
             examples=[D(z, e) for z, e in KEY3]),
        card("Activity 2 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three. Divide up the columns (1, 2, 3), then complete your two columns with three related words. Use a dictionary if necessary. B. Read your columns to your teammates, then complete the other columns with the words they read out. C. Read your columns to the class.",
             tables=[WT]),
        card("Activity 3 (Reading and Speaking)",
             "Pair up. Match the words in Column A to their appropriate collocations in Column B. Then read your word pairs to the class. The book gives no key; the matches (each from the passage) are mine:",
             tables=[MT]),
        card("Activity 4 (Reading, Writing, Speaking and Listening)",
             "A. Finish two of the following sentences in Chinese characters, while your partner completes the other two: 1. 以前在美国，大家出行主要靠……；现在，最受欢迎的是……；以后，大家也可能会……。 2. 网约车平台提供……服务，还有……特别服务。乘客可以用……叫车。 3. 因为……在中国很流行，“滴滴出行”甚至还有代驾服务，就是……。 4. 美国的两大网约车平台除了……，也为网约车司机……。一般来说，……。 B. Read your sentences to your partner, then complete the other two sentences with your partner’s contribution. My completions:",
             examples=[D(z, e) for z, e in S4]),
    ],
    exercises=[
        M("How did people travel in China in the past, mainly?", "By bus and taxi", ["By bike only", "By plane", "By boat"], "主要靠公交车和出租车."),
        M("What is the most popular new choice?", "Didi Chuxing", ["Meituan", "WeChat", "Airbnb"], "最受欢迎的就是“滴滴出行”."),
        M("Which service does Didi NOT provide in the passage?", "Bus tickets", ["Taxis", "Hitchhiking", "Carpooling"], "出租车、顺风车、拼车."),
        M("What does 代驾 mean?", "A designated driver drives the owner’s car home", ["A driver who teaches", "A car for rent", "A free ride"], "代驾司机开着车主的车."),
        M("What special items can Didi provide for?", "Large luggage, pets and child seats", ["Furniture", "Food", "Flowers"], "大件行李、宠物或是儿童座椅."),
        M("What can a Didi driver earn a month, generally?", "Four to five thousand yuan", ["Four hundred yuan", "Forty thousand yuan", "One thousand yuan"], "四千到五千元人民币."),
        M("What has appeared in Shanghai?", "Driverless Didi taxis", ["Flying taxis", "Free buses", "Electric trains"], "无人驾驶出租车."),
        M("Which collocation is right?", "精确定位", ["精确出发", "精确收入", "精确服务"], "精确定位."),
        M("Which collocation is right?", "准时到达", ["准时需要", "准时手机", "准时增加"], "准时到达."),
        M("Which collocation is right?", "增加收入", ["增加出发", "增加到达", "增加服务"], "增加收入."),
        F("“滴滴”能够精确定位，准___到达，让你轻松出发。", "时", PART, "准时: on time."),
        F("“滴滴”还可以根据乘客需要，提供特别的服___。", "务", PART, "服务: service."),
        F("以后的网约车会更加智能___，现在上海已经出现了无人驾驶出租车。", "化", PART, "智能化: more intelligent."),
    ],
)

# ------------------------------------------------------------------ 2. activities 5-7
C1 = ("张中行：安全平稳，健步如飞。方便，舒适，贴心，周到，春夏秋冬，风雨无阻。等待您的召唤，安步带给您阳光。电话一二三六七八六三九。",
      "Business card 1: Zhang Zhongxing: safe and steady, striding like flying. Convenient, comfortable, considerate, thoughtful, spring, summer, autumn and winter, whatever the wind and rain. Waiting for your call; Anbu brings you sunshine. Phone: 123678639. (the book’s card also has a taxi picture, tildes and dashes; the phone number is spelled digit by digit)")
C2 = ("顺风的士，五星车主。司平安，专职司机，专业操守，安全可靠，接受包车，四平八稳。电话一二三六七四八九三。",
      "Business card 2: Shunfeng Taxi, five-star owner. Si Ping’an, full-time driver, professional conduct, safe and reliable, charters accepted, steady and sure. Phone: 123674893. (the book’s card also has apple and leaf pictures; the phone number is spelled digit by digit)")
CK = [("张中行是出租车司机，有安全平稳、周到的服务，春夏秋冬风雨无阻，电话是一二三六七八六三九。", "Card 1 (my table answers): Who/job/service/contact: Zhang Zhongxing is a taxi driver with safe, steady and thoughtful service in all seasons and weather; phone 123678639."),
      ("司平安是专职司机，专业操守，安全可靠，接受包车，电话是一二三六七四八九三。", "Card 2 (my table answers): Si Ping’an is a full-time driver with professional conduct, safe and reliable, accepting charters; phone 123674893.")]
PP = [("以前美国人出行主要靠自己开车，也坐火车和公共汽车。", "美国人的出行 (以前), my sample: In the past Americans traveled mainly by driving themselves, and also took trains and buses."),
      ("现在大家常常用手机叫网约车，又方便又便宜。", "美国人的出行 (现在), my sample: Now people often call a ride-hailing car with their phone, both convenient and cheap."),
      ("以后可能会有更多的无人驾驶汽车，大家出门不用自己开车了。", "美国人的出行 (以后), my sample: In future there may be more driverless cars, and people won’t need to drive themselves when going out.")]
L2 = lesson(
    "Lesson 25 Presentation 3 activities: a Didi history, two business cards and American transport",
    "滴滴出行以前叫什么 · 名片 · 张中行 · 司平安 · 顺风的士 · 美国人的出行 以前 现在 以后",
    requires=[],
    cards=[
        card("Activity 5 (Listening and Reading)",
             "A. Listen to the passage once through and summarize it. B. Listen again and answer the questions. 1. What was “DiDi Chu Xing” called before? 2. What service did “DiDi” first provide, and what services did it later provide? 3. What three things can users do on their smartphones with the “DiDi” app? 4. What special services does “DiDi” provide? 5. How does the “DiDi” ride-sharing service benefit drivers? C. Share your answers with the class, then read the script. (Audio; neither the audio nor the script is in the book.)"),
        card("Activity 6 (Reading, Writing, Speaking and Listening)",
             "A. Read one of the business cards below while a partner reads the other, then fill in the table (谁; 做什么工作; 有什么服务; 怎么联系; 其它信息). B. Tell your partner in Chinese about the person on your card. Take notes on the person your partner read about. C. Tell the class in Chinese about the person on your partner’s card. The two cards, then my table answers:",
             examples=[D(*C1), D(*C2)] + [D(z, e) for z, e in CK]),
        card("Activity 7 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three. Research past, present or possible future transportation services in America, while your teammates investigate the other two time periods. Write a short paragraph (3–5 Chinese sentences) about your topic, then read it to your partners: 美国人的出行 (以前), (现在), (以后). B. Write a report about the entire topic together, upload it to a website, then read it to the class. (Three pictures and the website are not used.) One sample sentence for each period:",
             examples=[D(z, e) for z, e in PP]),
    ],
    exercises=[
        M("What does business card 1 promise?", "Safe, steady, thoughtful service in all weather", ["Cheap food", "Free tickets", "A hotel room"], "安全平稳，风雨无阻."),
        M("What is Zhang Zhongxing’s job?", "Taxi driver", ["Teacher", "Cook", "Doctor"], "Card 1."),
        M("Which card accepts charters (包车)?", "Card 2", ["Card 1", "Both", "Neither"], "接受包车."),
        M("What does 专职司机 mean?", "A full-time driver", ["A part-time driver", "A driver’s student", "A bus"], "专职: full-time."),
        M("What does 风雨无阻 mean?", "Whatever the wind and rain", ["Wind and rain stop us", "No wind", "Rain only"], "无阻: unhindered."),
        M("Which is the driver’s name on card 2?", "司平安", ["张中行", "彼得", "张华"], "司平安."),
        M("What does Activity 7 ask you to research?", "Past, present and future transportation in America", ["Chinese food", "Hotels", "Money"], "美国人的出行."),
        M("How long should each paragraph in Activity 7 be?", "Three to five sentences", ["One sentence", "Ten sentences", "Two pages"], "3–5 Chinese sentences."),
        F("张中行：安全平稳，___步如飞。", "健", PART, "健步如飞: striding like flying."),
        F("司平安，专职司机，专业操___，安全可靠。", "守", PART, "操守: conduct."),
    ],
)

# ------------------------------------------------------------------ 3. 根据 and 据
GT = table(["结构", "用法"], [["根据 + Noun/Noun Phrase", "two characters or more"], ["据 + Noun/Noun Phrase", "one, two or more characters"], ["据 + Sentence", "据 can be followed by a sentence; 根据 cannot"]],
           title="根据 and 据")
GE0 = [("另外，“滴滴”还可以根据乘客需要，提供特别的服务。", "1. In addition, Didi can also provide special services according to passengers’ needs."),
       ("据说，他明年要到中国去留学。", "2. It is said that he is going to study in China next year."),
       ("你说话要有根据，我什么时候不认真学习了？", "3. You must have a basis when you speak: when did I not study seriously? (根据 as a noun, “basis”)")]
GE = [("根据老师的要求，我们明天要早点到学校。", "1. According to the teacher’s request, we have to get to school a bit earlier tomorrow."),
      ("根据他的能力，她可以当经理。", "2. Based on his ability, she can be a manager. (the book’s pronouns are as printed)"),
      ("根据她的脸色，我就知道她一点都不高兴。", "3. From the look on her face I knew she was not happy at all."),
      ("据说，张华的女朋友很漂亮。", "4. It is said that Zhang Hua’s girlfriend is very pretty."),
      ("据我看，他很聪明，就是不努力。", "5. In my view he is very clever, he just doesn’t work hard."),
      ("据传，她要去北京工作了。", "6. It is rumored that she is going to work in Beijing.")]
GD = table(["据", "根据"], [["据 + single-character words: ✓", "根据 + single-character words: ✗"], ["据 + two or more characters: ✗", "根据 + two or more characters: ✓"], ["据 + 说, 闻, 悉, 传: ✓", "根据 + 报道, 新闻报道, 新华社: ✓"], ["据 + 某人说 / 某人看来: ✓", "根据 + name/pronoun + noun phrase: ✓"], ["据 + sentence: ✓", "根据 + sentence: ✗"], ["Informal: ✓", "Formal, written Chinese (e.g., news): ✓"]],
           title="Differences between 根据 and 据 (summary table; the book’s ✗ symbols are written ✗)")
G1 = table(["中文", "英文 (my definitions)"], [["据说", "it is said that"], ["据称", "it is claimed that; reportedly"], ["据悉", "it is learned that (from sources)"], ["据传", "it is rumored that"], ["据闻", "it is heard that"], ["据报道", "according to reports"], ["据统计", "according to statistics"], ["据估计", "it is estimated that"], ["根据新华社报道", "according to a Xinhua News Agency report"]],
           title="Activity 1: the terms and my English definitions (the book’s table has the Chinese column filled and the English column blank)", say=[0])
G2 = [("据说，她很友好。", "1. (corrected) It is said that she is very friendly. The book’s 根据说 is wrong: 根据 cannot go with 说."),
      ("根据老师的说法，我们班这次考试成绩很好。", "2. (correct) According to the teacher, our class’s exam results this time were very good."),
      ("据我看，他虽然有很多钱，可是不幸福。", "3. (corrected) In my view, although he has a lot of money, he is not happy. The book’s 根据我看 is wrong: 据 is used with 我看."),
      ("据报道，现在学校里每个学生都有一台电脑。", "4. (correct) According to reports, every student in schools now has a computer."),
      ("据传，她准备结婚了。", "5. (corrected) It is rumored that she is getting married. The book’s 根据传 is wrong: 传 goes with 据."),
      ("据统计，百分之八十的学生都觉得早上七点五十五分就上课，太早了。", "6. (correct) According to statistics, eighty percent of the students feel that starting class at 7:55 in the morning is too early. (the book writes 80% and 7:55 in digits)")]
G3 = [("根据天气预报，明天会下大雨，所以学校决定停课一天。", "Formal sample (mine): According to the weather forecast it will rain heavily tomorrow, so the school has decided to cancel classes for one day."),
      ("据说，学校旁边新开了一家餐馆，菜做得特别好吃。", "Informal sample (mine): It is said that a new restaurant has opened next to the school, and the food is especially good.")]
L3 = lesson(
    "Lesson 25 Presentation 3 grammar: the prepositions 根据 and 据",
    "根据乘客需要 · 据说 · 根据老师的要求 · 据我看 · 据传 · 据报道 据统计 据估计 · 根据新华社报道",
    requires=[],
    cards=[
        card("Prepositions 根据 and 据",
             "Both 根据 and 据 are prepositions that mean “according to” or “based on.” 根据 can also be a noun meaning “basis” or “foundation.” As prepositions, 根据 and 据 often precede a noun or noun phrase, but, while 据 can be followed by a sentence, 根据 cannot.",
             tables=[GT], examples=[D(z, e) for z, e in GE0]),
        card("Examples with 根据 and 据", "The English is mine.", examples=[D(z, e) for z, e in GE]),
        card("Differences between 根据 and 据",
             "• 据 can precede words with only one character, while 根据 must precede words with at least two characters. • 据 is often used with the verbs 说, 闻, 悉, 传, while 根据 cannot be. 根据 is commonly used with sets of two-character phrases found in formal and written Chinese, especially in news reports. • 据 is frequently used with word sets like 据报道, 据统计 (statistics) and 据估计 (estimates). • 据 is often used when referring to people, as in 据某人说, 据某人看来 or 据习近平说. However, 根据 can only be used with a personal name or pronoun followed by a noun phrase. • 据 can precede a sentence, while 根据 can only precede a noun or noun phrase.",
             tables=[GD]),
        card("Activity 1 (Reading)",
             "A. Form groups of three. Fill in the table with English definitions of the Chinese terms below. Use a dictionary if necessary. B. Compare definitions with the class.",
             tables=[G1]),
        card("Activity 2 (Reading, Writing, Speaking and Listening)",
             "A. Pair up. Determine whether the following sentences are correct, then rewrite the incorrect sentences in Chinese characters: 1. 根据说，她很友好。 2. 根据老师的说法，我们班这次考试成绩很好。 3. 根据我看，他虽然有很多钱，可是不幸福。 4. 据报道，现在学校里每个学生都有一台电脑。 5. 根据传，她准备结婚了。 6. 据统计，80% 的学生都觉得早上 7:55 就上课，太早了。 B. In Chinese, share your answers with the class and explain your reasoning. The book gives no key; the answers are mine:",
             examples=[D(z, e) for z, e in G2]),
        card("Activity 3 (Writing, Speaking and Listening)",
             "A. Starting with 根据 or 据, write a short report (three or more sentences), in the formal style, on current issues or everyday life, while a partner writes a report in the informal style. B. Read your report to your partner, then work together to improve your reports. C. Read your finished reports to the class. (Three pictures are not included.) One formal and one informal sample sentence, mine:",
             examples=[D(z, e) for z, e in G3]),
    ],
    exercises=[
        M("What do 根据 and 据 mean as prepositions?", "“According to” or “based on”", ["“Because of”", "“In spite of”", "“Instead of”"], "根据/据."),
        M("Which one can be followed by a whole sentence?", "据", ["根据", "Both", "Neither"], "据 + sentence."),
        M("Which one needs at least two characters after it?", "根据", ["据", "Both", "Neither"], "根据 + 2+ characters."),
        M("Which is correct?", "据说，她很友好", ["根据说，她很友好", "据据说，她很友好", "根说，她很友好"], "据说."),
        M("Which is correct?", "据我看，他很聪明", ["根据我看，他很聪明", "根我看，他很聪明", "据据我看，他很聪明"], "据我看."),
        M("Which is correct?", "据传，她准备结婚了", ["根据传，她准备结婚了", "据据传，她准备结婚了", "传据，她准备结婚了"], "据传."),
        M("What does 据报道 mean?", "According to reports", ["According to the weather", "Reports are false", "It is cheap"], "据报道."),
        M("What does 据统计 mean?", "According to statistics", ["According to the teacher", "It is said", "Maybe"], "据统计."),
        M("Which register is 根据 commonly used in?", "Formal, written Chinese, e.g. news", ["Casual talk only", "Poems only", "Children’s songs"], "Formal."),
        M("What does 你说话要有根据 use 根据 as?", "A noun, “basis”", ["A verb", "An adverb", "A measure word"], "根据 as a noun."),
        F("___说，他明年要到中国去留学。", "据", PART, "据说: it is said."),
        F("根___老师的要求，我们明天要早点到学校。", "据", PART, "根据: according to."),
    ],
)

# ------------------------------------------------------------------ 4. 就是/也就是
JT = table(["结构", "用法"], [["Noun, Noun Phrase or Sentence + 就是, + Explanation", "gives clarification, definition or explication"], ["…, 就是/也就是/就是说…", "the common variants; 那就是 and 也就是说 also work"]],
           title="就是/也就是 (说)")
JE0 = [("他们甚至还有代驾服务，就是代驾司机开着车主的车，把喝过酒或醉酒的车主送回家。", "Example: They even have a designated-driver service, that is, the designated driver drives the car owner’s car and takes an owner who has been drinking or is drunk home.")]
JE = [("昨天晚上，我在宿舍里什么都没做，就是在网上看看新闻，打打游戏什么的。", "1. Last night I didn’t do anything in the dorm, just read the news online, played games and so on."),
      ("学好中文没有什么秘密，基本上就是多听多练。", "2. There is no secret to learning Chinese well; basically it is listening and practicing a lot."),
      ("她学习生物学，就是生命科学。", "3. She studies biology, that is, the science of life."),
      ("下次开会是下个星期一，也就是三月一日。", "4. The next meeting is next Monday, that is, March 1st. (the book writes 3 月 1 日 in digits)"),
      ("明天是星期六，也就是说，我们不用去上班。", "5. Tomorrow is Saturday, which means we don’t have to go to work."),
      ("“滴滴出行”，也就是中国的一个网约车平台。", "6. “Didi Chuxing,” that is, a ride-hailing platform in China.")]
J4 = [("她有失眠症，也就是说，她常常夜里睡不着觉。", "1. She has insomnia, that is, she often can’t sleep at night. 失眠症 (my answer): insomnia."),
      ("我们每天的生活都需要有规律，就是说要早睡早起，按时吃饭、工作和锻炼。", "2. Our daily life needs to be regular, that is, going to bed and getting up early and eating, working and exercising on time. 规律 (my answer): regularity, a regular routine."),
      ("今天我们吃饭实行ＡＡ制，就是我们大家每个人平分账单。", "3. Today we are going Dutch, that is, each of us splits the bill equally. ＡＡ制 (my answer): going Dutch, splitting the bill equally. (the book writes AA in Latin letters; written full-width here)"),
      ("他是个素食者，也就是说，他从来不吃肉。", "4. He is a vegetarian, that is, he never eats meat. 素食者 (my answer): vegetarian."),
      ("在中国，“剩女”就是那些到了三十岁以上还没有结婚的女性。", "5. In China “leftover women” are those women who are over thirty and still not married. 剩女 (my answer): “leftover woman,” an unmarried woman over about thirty."),
      ("我哥是一个宅男，就是说他每天呆在家里，除了上网打游戏，或是看书，听音乐，别的时间很少出门。", "6. My brother is a homebody, that is, he stays at home every day and, apart from going online to play games or reading and listening to music, seldom goes out. 宅男 (my answer): a man who stays at home; homebody.")]
NW = [("小鲜肉：网络用语。也就是一些年轻、帅气、有肌肉的男生，他们一般年龄在十二到二十五岁之间，感情经历简单，长得很好看，很帅气。", "1. 小鲜肉: Internet slang. That is, some young, handsome, muscular boys, generally between twelve and twenty-five years old, with simple romantic histories, who are good-looking and handsome. (the book writes 12 and 25 in digits and puts the term in 【】, written here with a colon)"),
      ("数码小偷：就是使用最新科技的小偷。也就是说，这些小偷不用碰到你的钱包，站在十五厘米以外的地方，就可以用新科技偷走你的信用卡或是银行信息，他们被称为“数码小偷”。", "2. 数码小偷: Thieves who use the latest technology. That is, these thieves don’t need to touch your wallet; standing fifteen centimeters away they can steal your credit card or bank information with new technology, and they are called “digital thieves.” (the book writes 15 in digits)"),
      ("脑雾：就是有些事情，你原来很清楚，现在却变得不清楚，一时间你怎么都想不起来，过一段时间后你又会突然想起。", "3. 脑雾: That is, something you used to know clearly has become unclear, and for a while you can’t remember it however you try, but after some time you suddenly remember again."),
      ("吃瓜群众：网络用语，也就是一些网民或是社交媒体的粉丝，网上有新闻或事情发生，他们不太明白，但是却喜欢在旁边观看，或是看别的网友说什么。", "4. 吃瓜群众: Internet slang, that is, some netizens or social-media fans who, when news or something happens online, don’t quite understand it but like to watch from the side or see what other netizens say."),
      ("剁手：就是没有想清楚就在网上购物，不知不觉就花了大量的金钱。买完后一看账单，对自己很生气，要剁自己的手。也就是说，这些人都是特别喜欢网络购物的人。", "5. 剁手: That is, shopping online without thinking clearly and unknowingly spending a large amount of money. After buying, you look at the bill and are so angry with yourself that you want to chop off your own hands. That is, these people are people who especially like online shopping."),
      ("带货：网络新词，就是一些名人或明星们在网上帮助卖商品、卖货。因为粉丝们会对明星们使用的商品或销售的商品更加感兴趣，所以也会跟着买，这种商品也就变得非常流行和受欢迎。", "6. 带货: A new Internet word, that is, some celebrities or stars helping to sell goods online. Because fans become more interested in the goods that stars use or sell, they also follow and buy, and such goods become very popular and welcome.")]
NM = table(["网络新词热词", "Meaning (my answers)"], [["小鲜肉", "young, handsome, muscular guys (“young fresh meat”)"], ["数码小偷", "digital thieves who steal card data by technology from a distance"], ["脑雾", "brain fog: forgetting something you knew and remembering later"], ["吃瓜群众", "melon-eating onlookers: people who watch online drama from the sidelines"], ["剁手", "“chop your hands”: compulsive online shopping you regret afterward"], ["带货", "“bring goods”: celebrities promoting products so fans buy them"]],
          title="Activity 6: the six terms and my English meanings (the book’s Meaning column is blank)", say=[0])
L4 = lesson(
    "Lesson 25 Presentation 3 grammar: 就是 and 也就是 (说) for elaboration and explanation",
    "就是 也就是 那就是 就是说 · 代驾服务 · 失眠症 · 素食者 · 剩女 · 宅男 · 小鲜肉 数码小偷 脑雾 吃瓜群众 剁手 带货",
    requires=[],
    cards=[
        card("话语语法: 就是/也就是 (说) for Elaboration and Explanation",
             "就是, 也就是说, 那就是 and 就是说 mean “that is,” “in other words,” “that is to say,” etc. These are used to provide further clarification, definition, explication, or information. When used for explication or definition, 就是 comes after a noun, noun phrase or sentence, all preceded by a comma.",
             tables=[JT], examples=[D(z, e) for z, e in JE0]),
        card("Examples with 就是 and 也就是 (说)", "The book’s date in example 4 is spelled out. The English is mine.", examples=[D(z, e) for z, e in JE]),
        card("Activity 4 (Reading)",
             "A. Pair up. Read the sentences below, then supply the English meaning of the underlined words by guessing them from context or looking them up: 失眠症, 规律, AA 制, 素食者, 剩女, 宅男. B. Compare work with the class. The book gives no key; my meanings are inside the translations:",
             examples=[D(z, e) for z, e in J4]),
        card("Activity 5 (Listening, Reading, Writing and Speaking)",
             "A. Form groups of three. Listen to the first speaker, while your teammates listen to the other two. Fill in the EEIs in Chinese in the table (Topic | EEIs, rows 1, 2, 3). B. Exchange intel with your teammates in Chinese, then read your group’s EEIs to the class. C. Read the script to check your information. (Audio; the script is not in the book.)"),
        card("网络新词热词 (Activity 6, Reading, Speaking and Listening)",
             "A. Draw a slip from your teacher with a popular Chinese term from the Internet. Read the definition carefully, using a dictionary if necessary. B. Explain your term to your classmates in Chinese using 就是, 也就是, 也就是说, 那就是 or 就是说. Listen to your classmates explain their terms and write their English meanings in the table. C. As a class, compare meanings, then choose the best English version of each term. (Three pictures are not included.) The six slips, with my English:",
             tables=[NM], examples=[D(z, e) for z, e in NW]),
    ],
    exercises=[
        M("What do 就是 and 也就是说 mean in explaining?", "“That is” or “in other words”", ["“Because”", "“Although”", "“Whenever”"], "That is to say."),
        M("Where does 就是 come when explaining?", "After a noun, noun phrase or sentence, preceded by a comma", ["At the start of a text", "Before the subject", "After 吗"], "…, 就是 + explanation."),
        M("What does 下次开会是下个星期一，也就是三月一日 do?", "Explains the date", ["Asks a question", "Gives an order", "Makes a promise"], "也就是."),
        M("What is 失眠症?", "Insomnia", ["A cold", "A headache", "A stomachache"], "睡不着觉."),
        M("What is a 素食者?", "A vegetarian", ["A cook", "A waiter", "A farmer"], "从来不吃肉."),
        M("What is 剩女?", "An unmarried woman over about thirty", ["A rich woman", "A student", "A teacher"], "三十岁以上还没有结婚的女性."),
        M("What is 宅男?", "A man who stays at home a lot", ["A traveling man", "A policeman", "A builder"], "每天呆在家里."),
        M("What is 数码小偷?", "A thief who uses the latest technology", ["A thief of computers", "A police officer", "A shop owner"], "使用最新科技的小偷."),
        M("What is 剁手?", "Shopping online without thinking, then regretting it", ["Cooking", "Cutting vegetables", "Fighting"], "没有想清楚就在网上购物."),
        M("What is 带货?", "Celebrities helping to sell goods online", ["Delivering parcels", "Carrying luggage", "Buying a car"], "名人或明星们在网上帮助卖商品."),
        F("学好中文没有什么秘密，基本上___是多听多练。", "就", PART, "就是: that is."),
        F("明天是星期六，也就是___，我们不用去上班。", "说", PART, "也就是说: that is to say."),
    ],
)

# ------------------------------------------------------------------ 5. 来说
LT = table(["结构", "用法"], [["Qualifier + 来说 + Statement/Comment", "the qualifier indicates the scale, scope or applicability of the statement"]],
           title="来说")
LV = table(["常见说法", "English"], [["一般来说，……", "generally speaking; ordinarily; commonly"], ["总的来说，……", "generally speaking; generally; in general"], ["相对来说，……", "relatively speaking"], ["严格来说，……", "strictly speaking; technically"], ["具体来说，……", "specifically; in detail"], ["对某人来说，……", "from X’s perspective/point of view; as far as X is concerned"]],
           title="Common variants", say=[0])
LE0 = [("一般来说，“滴滴”司机每月的收入能有四千到五千元人民币。", "Example: Generally speaking, a “DiDi” driver’s monthly income can range from 4,000 to 5,000 RMB. (the book writes the figures in digits)")]
LE = [("一般来说，“滴滴”的出租车要比普通的出租车快得多。", "1. Generally speaking, Didi taxis are much faster than ordinary taxis."),
      ("一般来说，大城市有更多工作机会。", "2. Generally speaking, big cities have more job opportunities."),
      ("总的来说，这次的活动很成功。", "3. On the whole, this event was very successful."),
      ("相对来说，我更喜欢学习西班牙文。", "4. Relatively speaking, I prefer studying Spanish."),
      ("严格来说，你的答案不能算对，所以不能得分。", "5. Strictly speaking, your answer can’t count as correct, so you can’t get a point."),
      ("具体来说，住民宿和短租房有三个好处。", "6. Specifically, staying in homestays and short-term rentals has three benefits."),
      ("对你来说，家庭重要还是工作重要？", "7. For you, which is more important, family or work?")]
L7S = [("周末我通常都待在家里当书虫，不太出门。", "1. 一般来说，周末我通常都待在家里当书虫。 Follow-up (mine): …I usually stay at home and read at weekends and don’t go out much."),
       ("第一部分讲网约车的出现，第二部分讲我的经历。", "2. 总的来说，这篇文章分为四个部分。 Follow-up (mine): …the first part is about the appearance of ride-hailing and the second about my experience."),
       ("每次做作业都要花很长时间，不过我很喜欢写汉字。", "3. 对我来说，学习中文有些难，但是也很有意思。 Follow-up (mine): …each time I do homework it takes a long time, but I enjoy writing characters."),
       ("坐高铁不用提前很久到车站，也不会晚点。", "4. 相对来说，坐高铁要比坐飞机更方便。 Follow-up (mine): …with the high-speed train you don’t need to get to the station long beforehand, and it doesn’t run late."),
       ("他们是军人，身体一定要好。", "5. 严格来说，国防语言学院的学生每天都应该锻炼身体。 Follow-up (mine): …they are servicemembers, so their health has to be good."),
       ("第一要早睡，第二要多喝水，第三要多运动。", "6. 具体来说，要想身体健康，你每天得做三件事。 Follow-up (mine): …first sleep early, second drink more water, third exercise more.")]
L8S = [("对我来说，周末最重要的是休息。我喜欢睡到中午，然后去海边走一走。", "对…来说 (mine): For me the most important thing at the weekend is rest. I like to sleep until noon and then go for a walk by the sea."),
       ("一般来说，我每天六点起床。起得早的话，一天都很有精神。", "一般来说 (mine): Generally speaking I get up at six every day. If I get up early I am full of energy all day."),
       ("总的来说，这个学期过得很快。我学到了很多新的词语。", "总的来说 (mine): On the whole this semester went quickly. I learned many new words."),
       ("相对来说，中文的语法比较简单。可是汉字很难写。", "相对来说 (mine): Relatively speaking Chinese grammar is simple. But the characters are hard to write."),
       ("严格来说，这个办法不太对。因为它要花很多钱。", "严格来说 (mine): Strictly speaking, this method is not quite right, because it costs a lot of money."),
       ("具体来说，网约车有三个好处。第一是方便，第二是便宜，第三是安全。", "具体来说 (mine): Specifically, ride-hailing has three benefits. First, convenient; second, cheap; third, safe.")]
L5 = lesson(
    "Lesson 25 Presentation 3 grammar: …来说 for indicating scale or applicability",
    "一般来说 · 总的来说 · 相对来说 · 严格来说 · 具体来说 · 对某人来说 · 当书虫 · 国防语言学院",
    requires=[],
    cards=[
        card("话语语法: ……来说 for Indicating Scale or Applicability",
             "来说 is always preceded by a qualifier, e.g., 一般来说, 总的来说, 相对来说 and 对某人来说. A …来说 phrase precedes a statement or comment to indicate its scale, scope or applicability.",
             tables=[LT, LV], examples=[D(z, e) for z, e in LE0]),
        card("Examples with 来说", "The English is mine.", examples=[D(z, e) for z, e in LE]),
        card("Activity 7 (Reading, Writing, Speaking and Listening)",
             "A. For the first three sentences below, write your own logical follow-up sentence in Chinese characters. A partner will do the same for the remaining three sentences: 1. 一般来说，周末我通常都待在家里当书虫。 2. 总的来说，这篇文章分为四个部分。 3. 对我来说，学习中文有些难，但是也很有意思。 4. 相对来说，坐高铁要比坐飞机更方便。 5. 严格来说，国防语言学院的学生每天都应该锻炼身体。 6. 具体来说，要想身体健康，你每天得做三件事。 B. Read your original and follow-up sentences to your partner. Listen to your partner’s sentences and transcribe their follow-up sentences. Then convert them to Chinese characters. My follow-ups (the book’s “Follow-up:” lines are blank):",
             examples=[D(z, e) for z, e in L7S]),
        card("Activity 8 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three. Divvy up the 来说 phrases below, two per person (对…来说, 一般来说, 总的来说, 相对来说, 严格来说, 具体来说). Write a sentence for each of your two phrases, then add one or two sentences to explain or elaborate on it. B. Read your sentences to your teammates, transcribe their sentences in the appropriate boxes, then convert your transcriptions into Chinese characters. C. Read a teammate’s sentences to the class. My samples, one for each phrase:",
             examples=[D(z, e) for z, e in L8S]),
    ],
    exercises=[
        M("What does 来说 need before it?", "A qualifier", ["A question word", "A number", "A verb only"], "Qualifier + 来说."),
        M("What does 来说 indicate?", "The scale, scope or applicability of a statement", ["A reason", "A time", "A place"], "Scale, scope, applicability."),
        M("What does 一般来说 mean?", "Generally speaking", ["Strictly speaking", "Specifically", "Relatively speaking"], "一般来说."),
        M("What does 总的来说 mean?", "On the whole", ["Specifically", "For you", "Strictly speaking"], "总的来说."),
        M("What does 相对来说 mean?", "Relatively speaking", ["Generally speaking", "Strictly speaking", "In detail"], "相对来说."),
        M("What does 严格来说 mean?", "Strictly speaking", ["Relatively speaking", "In general", "For me"], "严格来说."),
        M("What does 具体来说 mean?", "Specifically; in detail", ["Generally", "Relatively", "As far as you are concerned"], "具体来说."),
        M("What does 对你来说 mean?", "As far as you are concerned", ["As far as I know", "Because of you", "Instead of you"], "对某人来说."),
        M("What is 对你来说，家庭重要还是工作重要？ asking?", "Which is more important to you, family or work", ["Where you work", "How many children you have", "When you finish work"], "对你来说…."),
        F("一般来说，大城市有更多工作机___。", "会", PART, "机会: opportunity."),
        F("___体来说，住民宿和短租房有三个好处。", "具", PART, "具体来说: specifically."),
    ],
)

# ------------------------------------------------------------------ 6. the suffix 化
HT = table(["结构", "用法"], [["Noun + 化 → Verb/Noun", "-ize, -ify, -ization, -ification"], ["Adjective + 化 → Verb/Noun", "-ize, -ify, -ization, -ification"]],
           title="Suffix 化 (-ize, -ify, -ization, -ification)")
HC = table(["名词 + 化", "English", "形容词 + 化", "English"], [["美国化", "Americanize", "美化", "beautify/beautification"], ["本地化", "localize", "绿化", "greenify/greenification"], ["智能化", "intellectualize", "软化", "soften"], ["数字化", "digitalize", "强化", "strengthen"]],
           title="Some common 化 terms currently in use", say=[0, 2])
HE0 = [("以后的网约车会更加智能化，现在上海已经出现了“滴滴”无人驾驶出租车。", "Example: In future ride-hailing will become even more intelligent; driverless Didi taxis have already appeared in Shanghai.")]
HE = [("中国的年轻人已经习惯了智能化的生活。出门在外，时刻得带着智能手机。", "1. Young people in China have become used to an intelligent way of life. Away from home they have to carry a smartphone at all times."),
      ("在美国生活了二十多年以后，他已经美国化了，早上起来要喝咖啡，吃饭要吃西餐。", "2. After living in America for more than twenty years he has already become Americanized: he has to drink coffee when he gets up in the morning and eats Western food."),
      ("中国每年的三月有植树节，希望种下的树越来越多，既可绿化山林，又可美化环境。", "3. China has Arbor Day every March, hoping that more and more trees will be planted, which can both green the mountain forests and beautify the environment."),
      ("很多美国大公司进入中国以后，没有做好本地化的工作，最后只能关门。", "4. After many big American companies entered China they did not do the localization work well and in the end could only close down.")]
H9N = table(["名词", "+化", "English (mine)"],
            [["农业", "农业化", "agriculturalize (rare)"], ["国际", "国际化", "internationalize"], ["欧洲", "欧洲化", "Europeanize"], ["城市", "城市化", "urbanize"], ["职业", "职业化", "professionalize"], ["军事", "军事化", "militarize"], ["西", "西化", "Westernize"], ["老龄", "老龄化", "age (population aging)"], ["全球", "全球化", "globalize"], ["商业", "商业化", "commercialize"], ["市场", "市场化", "marketize"], ["信息", "信息化", "informatize"], ["量", "量化", "quantify"]],
            title="Activity 9, nouns: my classification and 化 forms (the book gives the 20-word bank 简单 农业 国际 欧洲 丑 城市 职业 自动 军事 西 老龄 全球 私有 自由 深 商业 民主 市场 信息 量 and blank tables; the split into nouns and adjectives is mine)", say=[0, 1])
H9A = table(["形容词", "+化", "English (mine)"],
            [["简单", "简单化", "simplify"], ["丑", "丑化", "vilify; make look ugly"], ["自动", "自动化", "automate"], ["私有", "私有化", "privatize"], ["自由", "自由化", "liberalize"], ["深", "深化", "deepen"], ["民主", "民主化", "democratize"]],
            title="Activity 9, adjectives: my classification and 化 forms", say=[0, 1])
H10 = [("全球化给我们的日常生活带来了明显的变化，让个人的生活更加国际化。日常生活中，我们可以去沃尔玛超市，买国外牌子的日用品，也可以去电影院看最新的美国大片，还可以去国外快餐店或是西餐厅，品尝国外的美食。这些都是全球化给我们生活上带来的便利。", "The model passage: Globalization has brought obvious changes to our daily life and made personal life more international. In daily life we can go to Walmart, buy foreign-brand daily goods, go to the cinema to see the latest American blockbusters, and go to foreign fast-food places or Western restaurants to taste foreign food. These are all conveniences that globalization has brought to our life."),
       ("现在很多人习惯了网络化的生活。我们在网上买东西，在网上看病，也在网上学习。城市化和老龄化也给社会带来了很多变化。", "A sample paragraph (mine): Many people are now used to a networked life. We buy things online, see doctors online and study online. Urbanization and population aging have also brought many changes to society.")]
L6 = lesson(
    "Lesson 25 Presentation 3 grammar: the suffix 化",
    "智能化 · 美国化 本地化 数字化 · 美化 绿化 软化 强化 · 全球化 国际化 · 城市化 老龄化",
    requires=[],
    cards=[
        card("The Suffix 化",
             "As in English, a Chinese suffix (后缀 hòuzhuì) attaches to the end of the word it modifies. The suffix 化 is equivalent to the English “-ize,” “-ify,” “-ization” or “-ification.” 化 attaches to a noun or adjective to form a disyllabic or polysyllabic word, although most are disyllabic.",
             tables=[HT, HC], examples=[D(z, e) for z, e in HE0]),
        card("Examples with 化", "The English is mine.", examples=[D(z, e) for z, e in HE]),
        card("Activity 9 (Reading, Writing, Speaking and Listening)",
             "A. Write all the adjectives from the word bank below in their respective column in the table. Your partner will do the same for the nouns. B. Apply the suffix 化 to each word, then fill in the English equivalents. C. Read your answers to your partner so they can complete their table. D. Share your work with the class. The book’s tables are blank; mine are below.",
             tables=[H9A, H9N]),
        card("Activity 10 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three and read the following passage. B. Individually, write a short paragraph, three to five sentences, about a social trend or phenomenon. Use the passage as a model and include as many 化 words as possible. C. Read your paragraphs to each other. Fill in the table with your teammates’ information (Teammate | Social Trend/Phenomenon | EEIs). D. Upload your paragraphs to a website to share them with the class. The model passage, then my sample paragraph:",
             examples=[D(z, e) for z, e in H10]),
    ],
    exercises=[
        M("What is the suffix 化 equivalent to?", "“-ize” or “-ify”", ["“-less”", "“-ness”", "“un-”"], "化."),
        M("What does 化 attach to?", "A noun or adjective", ["A verb only", "A number", "A particle"], "Noun/adjective + 化."),
        M("What does 美国化 mean?", "Americanize", ["Americanism", "American food", "America’s Day"], "美国化."),
        M("What does 绿化 mean?", "Make green; greenify", ["Make red", "Make cold", "Make sweet"], "绿化."),
        M("What does 数字化 mean?", "Digitalize", ["Number the pages", "Count money", "Draw a figure"], "数字化."),
        M("What does 本地化 mean?", "Localize", ["Globalize", "Mobilize", "Privatize"], "本地化."),
        M("Which means “strengthen”?", "强化", ["软化", "美化", "绿化"], "强化."),
        M("Which means “soften”?", "软化", ["强化", "美化", "智能化"], "软化."),
        M("What does 全球化 mean?", "Globalization", ["Urbanization", "Localization", "Modernization"], "全球化."),
        M("What did American companies often fail to do in China, per example 4?", "Localization (本地化)", ["Advertising", "Hiring", "Paying taxes"], "没有做好本地化的工作."),
        F("以后的网约车会更加智能___。", "化", PART, "智能化."),
        F("在美国生活了二十多年以后，他已经美国___了。", "化", PART, "美国化."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration 1-2
ST6 = [("车主是一名专职的“滴滴”司机。", "1. The car owner is a full-time “Didi” driver."),
       ("车主开顺风车主要是为了增加收入。", "2. The car owner drives hitchhiking rides mainly to increase his income."),
       ("车主只有在上下班的时候才会接送乘客。", "3. The car owner picks up passengers only when going to and from work."),
       ("北京的交通很好，开顺风车很方便。", "4. Beijing’s traffic is good, so driving hitchhiking rides is convenient."),
       ("车主送过的一位乘客是他朋友孩子的老师。", "5. A passenger the car owner has driven is the teacher of his friend’s child."),
       ("能够给顾客提供满意的服务就是最好的顺风车车主。", "6. Being able to provide customers with satisfying service makes the best hitchhike car owner.")]
L7 = lesson(
    "Lesson 25 Presentation 3 skill integration: transportation talks and a hitch driver’s interview",
    "交通出行 · 顺风车车主 · 专职的滴滴司机 · 增加收入 · 提供满意的服务",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Writing, Speaking and Reading)",
             "A. Listen to three speakers talk about transportation in China, then answer the following questions: 1. Who are the speakers? 2. What is each speaker’s preferred mode of transportation? B. Listen again and fill in the table (Speaker 1, 2, 3 | Mode of Transportation | Pros & Cons) in Chinese. C. Form groups of three and read your information to your teammates. D. Read the script and check your work against it. E. Discuss in Chinese: your favorite modes of transportation; pros and cons of your preferred modes. F. Report the results of your discussion to the class in Chinese. (Three pictures and the audio are not included; the script is not in the book.)"),
        card("Skill Integration, Activity 2 (Listening, Reading and Speaking)",
             "A. Listen to the radio interview and determine whether the statements that follow are true or false. Compare answers with a partner and explain your reasoning. B. Listen again, take notes, and fill in the table: Identity of driver; How he got started in the business; Pros of being a Hitch driver; How it changed his life; Special experiences; Qualities of a good Hitch driver. C. In groups of three, compare information in Chinese. D. Read the script and check your information. (Two pictures and the audio are not included, and the script is not in the book, so the answers depend on the audio and are not given here.) The six statements:",
             examples=[D(z, e) for z, e in ST6]),
    ],
    exercises=[
        M("Who is the driver in Activity 2 called?", "A hitchhike car owner (顺风车车主)", ["A bus driver", "A train driver", "A pilot"], "顺风车车主."),
        M("What is the topic of Activity 2’s radio interview?", "Being a hitch driver", ["Buying a house", "Cooking", "Studying abroad"], "Statements 1–6."),
        M("What is statement 5 about?", "A passenger who was his friend’s child’s teacher", ["A pet", "A big suitcase", "A fine"], "他朋友孩子的老师."),
        M("What is statement 6 about?", "What makes the best hitch driver", ["How to buy a car", "How to cook", "How to find a job"], "最好的顺风车车主."),
        M("Which table row asks about the benefits?", "Pros of being a Hitch driver", ["Special experiences", "Identity of driver", "Related fees"], "The table."),
        M("What do you do in Activity 1E?", "Discuss favorite modes of transportation and their pros and cons", ["Write an email", "Order food", "Book a room"], "Activity 1E."),
        F("车主是一名专职的“滴滴”___机。", "司", PART, "司机: driver."),
        F("能够给顾客提供满意的服务就是最好的顺风车车___。", "主", PART, "车主: car owner."),
    ],
)

# ------------------------------------------------------------------ 8. skill integration 3
SK3B = table(["生词", "拼音", "English (mine)"], [["技能", "jìnéng", "skill"], ["羡慕", "xiànmù", "envy; admire"], ["稳定", "wěndìng", "stable"], ["便捷", "biànjié", "convenient; quick"], ["移民", "yímín", "immigrant; immigrate"], ["取代", "qǔdài", "replace"]],
             title="Activity 3A: supplementary vocabulary (the book gives the words and pinyin and leaves the English blank; the English is mine)", say=[0])
AR = [("现在是网络化时代，信息交流越来越方便。新型的网约车服务受到越来越多人的欢迎，人们利用互联网和手机就可以轻松预约出租车业务。网约车平台除了提供出租车服务以外，也提供拼车、专车等别的服务。", "1) This is the age of networking, and information exchange is more and more convenient. New-style ride-hailing services are welcomed by more and more people, and people can easily book taxi service with the Internet and a phone. Besides taxi service, ride-hailing platforms also provide carpooling, private cars and other services."),
      ("二零一二年，我从中国来到了美国旧金山。那时我既没钱，英文也不好，根本找不到合适的工作，只能做零工或是帮餐馆送外卖。因为这些工作既不要求语言，也不需要技能。那时的我，交通出行近的地方靠走路，远的靠公交车，从没想过乘坐网约车出行。", "2) In 2012 I came from China to San Francisco in America. I had no money then and my English was not good; I simply couldn’t find a suitable job and could only do odd jobs or deliver takeout for restaurants, because these jobs neither require language nor need skills. In those days, for getting around I relied on walking for near places and the bus for far ones, and I had never thought of taking a ride-hailing car. (the book writes 2012 in digits)"),
      ("直到二零一四年的一天，我的一个好朋友说起他做网约车司机的事，我很好奇。当时，我马上就下载了叫车应用软件，然后当场注册，叫车体验了一下。只有两百米左右的路程，我付了五美元的服务费。我很羡慕这份工作，轻松、自由，还有很高的奖金。", "3) Until one day in 2014, a good friend of mine talked about his work as a ride-hailing driver and I was curious. At that time I immediately downloaded a car-hailing app, registered on the spot and tried calling a car. It was only about two hundred meters, and I paid five dollars in service fees. I envied this job: relaxed, free, and with a high bonus."),
      ("两年以后，我觉得收入不稳定，所以就买了一辆新车，开始当起了网约车司机。那个时候的网约车已经能够提供快速、便捷、低费、优质的出行服务了，越来越多的年轻人开始选择乘坐网约车出行。", "4) Two years later I felt my income was unstable, so I bought a new car and started working as a ride-hailing driver. By then ride-hailing could already provide fast, convenient, low-cost and high-quality travel service, and more and more young people began to choose to ride in ride-hailing cars."),
      ("我觉得刚到美国的新移民特别适合做网约车司机，原因就是不需要英文，入门很容易，操作也简单。你只需要简单的英文交流能力，然后下载一个网约车软件，而且他们有全中文的操作，简单培训一下，就可以接送乘客了。另外，网约车司机的收入也比在餐馆打工多一些。一般来说，每小时至少可以有二十六美元的收入，高于旧金山十五美元的最低小时工资。还有，网约车的工作时间自由，可根据你个人的需要选择工作时间和地点。所以比较轻松，时间也随意。", "5) I think new immigrants who have just arrived in America are especially suited to be ride-hailing drivers, because no English is needed, it is easy to get into and the operation is simple. You only need simple English communication ability, then download a ride-hailing app, and there is an all-Chinese version of the operation; with a little training you can pick up and drop off passengers. In addition, a ride-hailing driver’s income is also a bit more than working in a restaurant. Generally speaking, you can earn at least 26 dollars an hour, above San Francisco’s minimum hourly wage of 15 dollars. Also, the working hours of ride-hailing are free, and you can choose working time and place according to your own needs. So it is fairly relaxed and the time is flexible. (the book writes 26 and 15 in digits)"),
      ("以后的网约车会更加智能化，不知道网约车司机的工作会不会被“无人驾驶”出租车所取代。", "6) In future ride-hailing will become more intelligent, and I don’t know whether the ride-hailing driver’s job will be replaced by “driverless” taxis.")]
AR_N = [("第一段：网约车服务越来越受欢迎，用手机就能预约。", "Paragraph 1 (my notes): ride-hailing is more and more popular and can be booked with a phone."),
        ("第二段：二零一二年作者来到旧金山，没钱，英文不好，只能做零工和送外卖，没有想过坐网约车。", "Paragraph 2 (my notes): the author came to San Francisco in 2012, had no money and little English, and could only do odd jobs and deliveries; he had never thought of ride-hailing."),
        ("第三段：二零一四年朋友做网约车司机，作者好奇，试着叫了一次车，很羡慕这份工作。", "Paragraph 3 (my notes): in 2014 a friend became a driver; the author was curious, tried one ride and envied the job."),
        ("第四段：两年以后收入不稳定，他买了新车，开始当网约车司机。", "Paragraph 4 (my notes): two years later his income was unstable, so he bought a new car and became a driver."),
        ("第五段：新移民适合当网约车司机，因为不需要英文，收入高，时间自由。", "Paragraph 5 (my notes): new immigrants suit the job because no English is needed, the income is higher and the hours are flexible."),
        ("第六段：以后的网约车会更智能，司机的工作可能会被无人驾驶出租车取代。", "Paragraph 6 (my notes): in future ride-hailing will be smarter and drivers’ jobs may be replaced by driverless taxis.")]
TF3 = [("网络和手机让大家可以轻松预约叫车，受到越来越多人的喜爱。", "1. The Internet and phones let everyone easily book a ride, and it is liked by more and more people. — True (mine): paragraph 1."),
       ("作者刚到美国的时候，喜欢在餐馆送外卖。", "2. When the author first arrived in America he liked delivering takeout at restaurants. — False (mine): he could only do it because it needed no language and no skills."),
       ("作者第一次接触网约车，他不喜欢。", "3. The first time the author came into contact with ride-hailing, he didn’t like it. — False (mine): he was curious and envied the job."),
       ("因为网约车已经能够提供很好的服务，所以他开始当网约车司机。", "4. Because ride-hailing could already provide very good service, he began working as a driver. — False (mine): the reason he gives is that his income was unstable."),
       ("新移民非常适合开网约车，因为他们有很多开车的经验。", "5. New immigrants are very suited to driving for ride-hailing because they have a lot of driving experience. — False (mine): the reasons are no English needed, easy entry and simple operation."),
       ("车主很希望网约车越来越智能化。", "6. The car owner very much hopes ride-hailing will become more and more intelligent. — False (mine): he worries that driverless taxis may replace drivers.")]
L8 = lesson(
    "Lesson 25 Presentation 3 skill integration: a ride-hailing driver’s story",
    "网络化时代 · 新移民 · 零工 · 羡慕 · 收入不稳定 · 全中文的操作 · 无人驾驶出租车 取代",
    requires=[],
    cards=[
        card("Skill Integration, Activity 3 (Reading, Speaking and Listening)",
             "A. Guess the meaning of the following words or look them up. Compare work with a partner. B. Form groups of three. Each teammate reads two consecutive paragraphs in the following article. Write the main idea of each paragraph and its EEIs in the table (Teammate 1, 2, 3 | Paragraph 1, 2). C. Verbally convey your information to your teammates in Chinese. Fill in their information to complete the tables. D. As a group, determine whether the following statements are true or false. Consult the article if necessary. (Two pictures are not included.)",
             tables=[SK3B]),
        card("The article", "The six paragraphs, with my English.", examples=[D(z, e) for z, e in AR]),
        card("Activity 3: my notes", "The book’s tables are blank; the notes are mine.", examples=[D(z, e) for z, e in AR_N]),
        card("Activity 3D: true or false", "The statements are the book’s; the answers are mine.", examples=[D(z, e) for z, e in TF3]),
    ],
    exercises=[
        M("When did the author come to San Francisco?", "2012", ["2014", "2016", "2000"], "二零一二年."),
        M("Why could he only do odd jobs and deliveries at first?", "He had no money and his English was not good", ["He was too young", "He didn’t like driving", "He had no phone"], "既没钱，英文也不好."),
        M("What made him curious about ride-hailing?", "A friend’s work as a driver", ["An advertisement", "A film", "A newspaper"], "好朋友说起他做网约车司机的事."),
        M("How much did he pay for the first ride?", "Five dollars", ["Fifty dollars", "Free", "Fifteen dollars"], "付了五美元的服务费."),
        M("Why did he start driving himself?", "His income was unstable", ["He lost his car", "He moved house", "He was bored"], "收入不稳定."),
        M("Why are new immigrants suited to drive, according to him?", "No English needed, easy entry and simple operation", ["They know the city", "They own luxury cars", "They love driving"], "不需要英文，入门很容易，操作也简单."),
        M("What is the hourly income he mentions, at least?", "Twenty-six dollars", ["Six dollars", "Sixty dollars", "Twelve dollars"], "至少可以有二十六美元的收入."),
        M("What is San Francisco’s minimum hourly wage in the article?", "Fifteen dollars", ["Five dollars", "Twenty-five dollars", "Fifty dollars"], "十五美元的最低小时工资."),
        M("What worries him about the future?", "Driverless taxis may replace drivers", ["Gas prices", "Traffic jams", "Parking fines"], "被无人驾驶出租车所取代."),
        M("What does 取代 mean?", "Replace", ["Take a photo", "Take a seat", "Take a break"], "取代."),
        F("我很羡___这份工作，轻松、自由，还有很高的奖金。", "慕", PART, "羡慕: envy."),
        F("我觉得收入不稳___，所以就买了一辆新车。", "定", PART, "稳定: stable."),
    ],
)

# ------------------------------------------------------------------ 9. skill integration 4
BM = [("如果你是已经到过中国的外国人，你一定有过这样的经历：你和一群老外排着长长的队在酒店门口等出租车，而聪明的中国人却一个一个从你身边悠闲地走过，坐上他们用手机应用叫来的网约车。", "1) If you are a foreigner who has already been to China, you must have had this experience: you and a group of foreigners line up in a long queue at the hotel door waiting for a taxi, while clever Chinese people walk past you one by one at leisure and get into the ride-hailing cars they called with their phone apps."),
      ("近日，我这个老外就在中国亲身体验了一下“滴滴出行”的服务。这次去北京参加车展以前，我就提前做好了准备，在手机上下载好了“滴滴”的手机应用英文版，现在在中国甚至就连出租车司机也开始使用“滴滴”的打车应用。如果没有这个应用，我真不知道该怎么办。", "2) Recently I, this foreigner, personally tried the Didi Chuxing service in China. Before going to Beijing for the auto show, I prepared in advance and downloaded the English version of the Didi phone app; now in China even taxi drivers have begun to use Didi’s taxi app. Without this app I really wouldn’t know what to do."),
      ("因为我不会说中文，所以要是需要告诉司机在哪儿接送我，我会感到很紧张。第一次开始叫车以前我很担心，怕司机找不到我。但最后还是很顺利，一辆“滴滴”出租车在不到三分钟的时间就到了我所在的地方。", "3) Because I can’t speak Chinese, if I need to tell the driver where to pick me up and drop me off I feel very nervous. Before calling a car for the first time I was very worried, afraid the driver couldn’t find me. But in the end it went very smoothly, and a Didi taxi arrived where I was in less than three minutes. (the book writes 3 in digits)"),
      ("其实，“滴滴”的应用操作起来很容易。它把所有的信息都翻译成英语，并通过汽车图片、车牌号码和司机的照片帮助乘客找到司机。随着我预约的车越来越近，我开始看到司机发给我的中文消息出现在手机上，我只能猜一猜他想要告诉我什么。不过，因为这个应用非常智能化，可以提供英文的快速回复，也就是说，你可以直接输入英文信息，点击发送时，这些信息和回复就会自动翻译成中文，再发给司机。这样你和司机的沟通就不会有问题了。真是太方便、太聪明了。", "4) In fact, the Didi app is very easy to operate. It translates all the information into English and helps passengers find the driver through the picture of the car, the license plate number and the driver’s photo. As the car I booked came nearer, I began to see the driver’s Chinese messages appear on my phone, and I could only guess what he wanted to tell me. But because the app is so intelligent it can offer quick replies in English; that is, you can type English messages directly, and when you click send these messages and replies are automatically translated into Chinese and sent to the driver. This way there is no problem in communicating with the driver. It is really so convenient and so clever."),
      ("“滴滴”在中国，除了为人们提供了非常便利和省时的出行服务以外，同时也为很多人提供了新的就业机会，增加了很多人的收入，所以他们的服务也受到越来越多人的欢迎。甚至，就连我这样不会说中文的老外也成为了他们的粉丝。", "5) Besides providing people with very convenient, time-saving travel services in China, Didi has also provided new jobs for many people and increased many people’s income, so its service is welcomed by more and more people. Even a foreigner like me who can’t speak Chinese has become one of its fans.")]
MS = table(["Summary", "段落 (my answers)"], [["作者去中国前的准备", "第二段"], ["为什么“滴滴”受到大家的欢迎", "第五段"], ["作者的担心", "第三段"], ["老外们在中国的经历", "第一段"], ["“滴滴”的操作和使用", "第四段"]],
           title="Activity 4B: matching the Chinese summaries to their paragraphs (the book’s Paragraph No. column is blank; the matches are mine)", say=[0, 1])
TR = [("如果你是已经到过中国的外国人，你一定有过这样的经历：你和一群老外排着长长的队在酒店门口等出租车，而聪明的中国人却一个一个从你身边悠闲地走过，坐上他们用手机应用叫来的网约车。", "Translation 1 is paragraph 1 above."),
      ("不过，因为这个应用非常智能化，可以提供英文的快速回复，也就是说，你可以直接输入英文信息，点击发送时，这些信息和回复就会自动翻译成中文，再发给司机。", "Translation 2: But because the app is so intelligent it can offer quick replies in English; that is, you can type English messages directly, and when you click send these messages and replies are automatically translated into Chinese and then sent to the driver. (my translation)"),
      ("“滴滴”在中国，除了为人们提供了非常便利和省时的出行服务以外，同时也为很多人提供了新的就业机会，增加了很多人的收入，所以他们的服务也受到越来越多人的欢迎。甚至，就连我这样不会说中文的老外也成为了他们的粉丝。", "Translation 3 is paragraph 5 above.")]
PRB = [("在中国可能会有的困难：不会说中文，找不到路，不知道怎么叫车，也不知道怎么付款。", "Activity 4A, problems you might encounter in China (my sample): not speaking Chinese, not finding the way, not knowing how to call a car, and not knowing how to pay.")]
L9 = lesson(
    "Lesson 25 Presentation 3 skill integration: an American businessman uses Didi in Beijing",
    "老外在中国 · 滴滴出行的英文版 · 快速回复 自动翻译成中文 · 就连我也成为了他们的粉丝 · 排着长长的队",
    requires=[],
    cards=[
        card("Skill Integration, Activity 4 (Speaking, Writing, Reading and Listening)",
             "A. Pair up. In Chinese, discuss problems you might encounter in China, especially with transportation. Then write them down in Chinese in the table (在中国可能会有的困难). B. Individually, skim the following translation of an American businessman’s experience in China and summarize each paragraph. Then match the Chinese summaries in the chart below to their source paragraph. Compare work with your partner. C. Form groups of three. Student 1 reads paragraphs one and two of the passage, Student 2 reads paragraph three and four, and Student 3 reads paragraph five. Then fill in the EEIs for each paragraph in the table. D. Report your EEIs to your teammates in Chinese, then complete the table with their information. E. Translate the three paragraphs that follow the article. (Two pictures are not included.) A sample for 4A, mine:",
             examples=[D(z, e) for z, e in PRB]),
        card("The businessman’s five paragraphs", "With my English.", examples=[D(z, e) for z, e in BM]),
        card("Activity 4B: my matching and 4E notes", "The book’s chart and the translations are open; the matching and my translation of the second item are below. Items 1 and 3 are the businessman’s first and last paragraphs, translated above.",
             tables=[MS], examples=[D(TR[1][0], TR[1][1])]),
    ],
    exercises=[
        M("What do foreigners and Chinese people do at the hotel door in paragraph 1?", "Foreigners queue for taxis; Chinese ride in cars they called by app", ["Everyone walks", "Everyone waits for buses", "Nobody waits"], "Paragraph 1."),
        M("Where did the author go for the auto show?", "Beijing", ["Shanghai", "Chengdu", "Xi’an"], "去北京参加车展."),
        M("What did he download before going?", "The English version of the Didi app", ["A map", "A language dictionary", "A WeChat bank"], "“滴滴”的手机应用英文版."),
        M("What was he worried about?", "The driver not finding him", ["The price", "The weather", "The food"], "怕司机找不到我."),
        M("How long did the first taxi take to arrive?", "Less than three minutes", ["Half an hour", "One hour", "Ten minutes"], "不到三分钟."),
        M("How does the app help passengers find the driver?", "Car photo, license plate number and driver’s photo", ["A phone call", "A paper map", "A guide"], "汽车图片、车牌号码和司机的照片."),
        M("What happens when you send an English message?", "It is automatically translated into Chinese for the driver", ["It is deleted", "It is sent in English", "It is read aloud"], "自动翻译成中文."),
        M("Which paragraph matches “作者的担心”?", "Paragraph 3", ["Paragraph 1", "Paragraph 2", "Paragraph 5"], "My matching."),
        M("Which paragraph matches “为什么“滴滴”受到大家的欢迎”?", "Paragraph 5", ["Paragraph 1", "Paragraph 3", "Paragraph 4"], "My matching."),
        M("What has the author become by the end?", "A fan of Didi", ["A driver", "A teacher", "A doctor"], "成为了他们的粉丝."),
        F("我这个老外就在中国亲身___验了一下“滴滴出行”的服务。", "体", PART, "体验: experience."),
        F("这些信息和回复就会自动翻___成中文，再发给司机。", "译", PART, "翻译: translate."),
    ],
)

# ------------------------------------------------------------------ 10. using Chinese in context
TP = [("美国有哪些流行的网约车平台和手机应用？", "Talking point 1: Which popular ride-hailing platforms and phone apps are there in America?"),
      ("美国的网约车平台提供哪些服务？有什么特别的服务吗？", "Talking point 2: What services do America’s ride-hailing platforms provide? Are there any special services?"),
      ("美国人为什么喜欢用这些平台和应用？", "Talking point 3: Why do Americans like to use these platforms and apps?"),
      ("推荐一个特别受欢迎的网约车平台和应用，告诉中国听众怎么使用这个平台和应用。", "Talking point 4: Recommend a particularly popular ride-hailing platform and app and tell the Chinese audience how to use it."),
      ("对美国人来说，美国的网约车平台还有什么别的好处？", "Talking point 5: For Americans, what other benefits do America’s ride-hailing platforms have?"),
      ("中国人在使用美国网约车平台和应用时，应该注意些什么？", "Talking point 6: What should Chinese people pay attention to when using American ride-hailing platforms and apps?")]
UCS3 = [("在美国，最受欢迎的网约车平台有两个。你可以在手机上下载应用，输入你要去的地方，就可以叫车了。", "Sample for the radio program (mine): In America there are two very popular ride-hailing platforms. You can download the app on your phone, enter where you want to go, and then call a car."),
        ("网约车平台除了提供出租车服务以外，也提供拼车服务，还有价格比较便宜的选择。", "Sample (mine): Besides taxi service, ride-hailing platforms also provide carpooling and cheaper options."),
        ("网约车的问题是价格有时候很贵，另外，司机也不一定认识路。", "Activity 2, pair 1 sample (mine): The problem with ride-hailing is that the price is sometimes very high; in addition, the driver does not always know the way."),
        ("可以让价格更透明，还可以让乘客给司机打分，这样服务会更好。", "Activity 2, pair 2 sample (mine): Prices could be made more transparent and passengers could rate drivers, so service would be better."),
        ("以后，无人驾驶汽车会越来越多，网约车会更加智能化。", "Activity 2, pair 3 sample (mine): In future there will be more and more driverless cars and ride-hailing will become more intelligent."),
        ("上个周末，我跟朋友去海边玩。因为没有车，所以我们用手机叫了一辆网约车。首先，我下载了应用，然后输入了地方，接下来，司机很快就来了。路上，司机给我们介绍了很多好玩的地方。总的来说，这次的经历很不错。", "Activity 3, a sample story (mine): Last weekend my friend and I went to the seaside. Because we had no car, we called a ride-hailing car with our phone. First I downloaded the app and then entered the place; next, the driver came very quickly. On the way the driver told us about many fun places. All in all, this experience was very good.")]
UT_1 = table(["美国的网约车"], [["美国流行的网约车平台和应用"], ["提供的服务"], ["使用这些产品和服务的原因"], ["怎么使用这些平台和应用"], ["其他好处和优点"], ["中国用户需要注意的事情"]],
             title="Activity 1B: the table to fill in (the book writes the headings in English: Popular U.S. mobile transportation platforms and apps; Services provided; Reasons for using these products and services; How to use these platforms and apps; Other benefits and advantages; Things Chinese users need to pay attention to; the Chinese here is mine)", say=[0])
UT_3 = table(["坐网约车的故事"], [["谁，或者跟谁"], ["什么时候"], ["在哪儿"], ["做什么"], ["为什么"], ["怎么做"], ["坐车的印象"], ["其他信息"]],
             title="Activity 3A: the outline table (the book writes Who (or with whom), When, Where, What, Why, How, Ride Impressions and Additional Information in English; the Chinese is mine)", say=[0])
L10 = lesson(
    "Lesson 25 Presentation 3 using Chinese in context: American ride-hailing and a ride story",
    "美国的网约车 · 上海交通广播电台 · 网约车的现在和未来 · 网约车的问题、解决方案和未来趋向 · 坐网约车的故事",
    requires=[],
    cards=[
        card("美国的网约车 (Using Chinese in Context, Activity 1, Reading, Speaking and Listening)",
             "A. Pair up. A Shanghai radio program invites you and an expat colleague to talk about popular American mobile transportation platforms and apps. Read the following talking points the station has provided to you in advance: 《美国的网约车平台和使用》节目要点 (上海交通广播电台). B. Divide up the talking points and research online for information to help you address them. Fill in the table with your findings. C. Exchange information with your partner. D. Present your talking points to your Chinese officemates (the class) to prepare for the radio program. (Three pictures are not included.) The six talking points:",
             tables=[UT_1], examples=[D(z, e) for z, e in TP + UCS3[:2]]),
        card("网约车的现在和未来 (Using Chinese in Context, Activity 2, Reading, Writing, Speaking and Listening)",
             "A. Divide the class into three pairs to answer the following questions, one question per pair: 1. What problems do mobile transportation platforms and services have? 2. How could we improve mobile transportation services and platforms? 3. What mobile transportation trends do you foresee in the near future (modes, systems, platforms, services, AI, etc.)? B. Conduct research and write down key terms and information in Chinese characters in the table (Pair 1 – Problems with Mobile Transportation Platforms and Services; Pair 2 – How to Improve Mobile Transportation Platforms and Services; Pair 3 – Future Mobile Transportation Modes, Systems, Platforms and Services). C. Using appropriate connectives, write four to six Chinese sentences to answer your question. D. Form groups of three with one member from each pair. Read your answer to your teammates. E. Write a group report on the problems, solutions and future direction of mobile transportation (网约车的问题、解决方案和未来趋向). Read it to the class, then email it to your teacher. (Three pictures are not included.) One sample answer for each pair, mine:",
             examples=[D(z, e) for z, e in UCS3[2:5]]),
        card("坐网约车的故事 (Using Chinese in Context, Activity 3, Reading, Writing, Speaking and Listening)",
             "A. After hearing you on the Shanghai radio program, a local newspaper asks you and your expat colleagues to write a story on your mobile transportation experiences. To organize your own story, fill in the EEIs (who, what, where, when, how and why) in Chinese in the table. B. Write at least 6–8 complete Chinese sentences in the table 坐网约车的经历. Use connective and sequential words as much as possible. Your Chinese colleague (your teacher) will assist you and review your story. C. Form groups of three and read your story to your teammates. D. Each group selects the best story and reads it to the office (the class), who then chooses the final story to submit to the newspaper. A sample story, mine:",
             tables=[UT_3], examples=[D(z, e) for z, e in UCS3[5:]]),
    ],
    exercises=[
        M("Who invites you to talk in Activity 1?", "A Shanghai radio program", ["A TV station in Beijing", "A newspaper", "A school"], "上海交通广播电台."),
        M("What is the radio program called?", "《美国的网约车平台和使用》", ["《中国的高铁》", "《外卖平台》", "《民宿》"], "节目要点."),
        M("What do you research for the program?", "American ride-hailing platforms and apps", ["Chinese food", "Hotels", "Banks"], "Activity 1B."),
        M("How many pairs divide up the questions in Activity 2?", "Three", ["Two", "Four", "Six"], "Three pairs."),
        M("What is Pair 3’s question about?", "Future mobile transportation trends", ["Problems", "Prices", "Drivers’ food"], "Pair 3."),
        M("What is the group report in Activity 2E titled?", "网约车的问题、解决方案和未来趋向", ["滴滴出行", "民宿", "外卖"], "网约车的问题、解决方案和未来趋向."),
        M("What do you write in Activity 3?", "A story about your ride-hailing experience", ["A menu", "A poem", "A letter to the teacher"], "坐网约车的故事."),
        M("How many sentences should the story have, at least?", "Six to eight", ["One", "Two", "Twenty"], "At least 6–8 sentences."),
        M("Who finally chooses the story for the newspaper?", "The class", ["The teacher alone", "The driver", "The newspaper"], "Activity 3D."),
        F("下载应用，输入你要去的地方，就可以___车了。", "叫", PART, "叫车: call a car."),
        F("总的来说，这次的经___很不错。", "历", PART, "经历: experience."),
    ],
)

# ------------------------------------------------------------------ 11. vocabulary
L11 = vocab_lesson("Lesson 25 Presentation 3 vocabulary", "25 words from the book’s Presentation 3 list",
                   "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book lists the suffix as -化 and prints the traditional form and pinyin of 滴滴出行 in one cell; here the suffix is written 化.", VOC3)

# ------------------------------------------------------------------ 12. area studies
L12 = lesson(
    "Lesson 25 Area Studies: Tourism and Transportation in China",
    "旅游业 · 微信支付 · 途家网 · 滴滴出行 · 神州专车 · 首汽约车 · 曹操出行 · 美团打车",
    requires=[],
    cards=[
        card("Tourism and Transportation in China (1)",
             "The tourist industry in China grew rapidly with the advent of economic reform and the opening-up to international trade, commerce, and investment in the 1980s and 1990s. In 2019, the total income from domestic and foreign tourism was $95 billion, 11.05% of GDP. In recent years, mobile transportation apps and online homestay platforms have flourished. Among the hundreds of apps used for daily living and recreational activities, the most popular are WeChat Pay (微信支付 Wēixìn Zhīfù), Tujia (途家网 Tújiāwǎng) and Didi Travel (滴滴出行 Dīdī Chūxíng)."),
        card("(2) WeChat Pay and short-term lodging",
             "WeChat Pay is a digital wallet service with which customers make mobile payments and exchange money between contacts. Although Alibaba retained a 54 % share of the Chinese mobile online payment market compared to WeChat’s 37 %, WeChat overtook Alibaba in 2019 with 800 million active users compared to Alipay’s 520 million. WeChat Pay can also be used for bus or subway rides by scanning the ride code into barcode scanners. Online platforms for short-term lodging also abound. The current estimated market share is 42% for Tujia, 31% for Muniao and 8% for Airbnb. Launched in 2011, Tujia is now the world’s leading short-term rental platform. It offers 400 domestic and 1,037 overseas destinations, and over 10 million online housing units including homestays, houses and apartments. Tujia’s GMV (gross merchandise value) reached $2.5 billion in 2019."),
        card("(3) Online ride-hailing",
             "As of August 2018, over 80 online ride-hailing companies held operating licenses. The major platforms include DiDi Travel (滴滴出行 Dīdī Chūxíng), UCAR Inc. (神州专车 Shénzhōu Zhuānchē), Shouqi Taxi (首汽约车 Shǒuqì Yuēchē), CAOCAO (曹操出行 Cáocāo Chūxíng), Dida Travel (嘀嗒出行 Dídā Chūxíng), Yidao (易到 Yìdào) and Us Regiment Taxi (美团打车 Měituán Dǎchē). Among these, Didi Chuxing occupies more than 90% of market share with the most users. As of June 2019, the number of ride-hailing users in China reached 337 million, an increase of 6.7 million from 2018, accounting for 39.4% of total Internet users. The number of online taxi-hailing or express taxi users in China reached 339 million, an increase of 6.33 million from 2018, constituting 39.7% of all netizens."),
        card("(4) DiDi Travel and the conclusion",
             "DiDi Travel (滴滴出行 Dīdī Chūxíng) is a Chinese transportation company headquartered in Beijing. The company provides app-based transportation services, including taxi-hailing, private car-hailing, social ridesharing and bike-sharing; on-demand delivery services; and automobile services, including sales, leasing, financing, maintenance, fleet operation, electric vehicle charging, and co-development of vehicles with automakers. In 2018, Didi boasted more than 550 million platform users, tens of millions of drivers, and a GMV of $45.11 billion. These burgeoning platforms and app companies contribute significantly to the economy and make travel, lodging and daily life in China far more convenient. (The book’s reference list names three websites; they are left out here. Two pictures are not included.)"),
    ],
    exercises=[
        M("When did the tourist industry in China grow rapidly?", "With economic reform and opening-up in the 1980s and 1990s", ["Only after 2010", "In the 1950s", "During the 1960s"], "1980s and 1990s."),
        M("What was the total income from tourism in 2019?", "$95 billion, 11.05% of GDP", ["$9.5 billion", "$950 billion", "$95 million"], "$95 billion."),
        M("Which three apps are named as the most popular?", "WeChat Pay, Tujia and Didi Travel", ["Alipay, Meituan and Taobao", "Airbnb, Uber and Lyft", "Baidu, Weibo and QQ"], "WeChat Pay, Tujia, Didi."),
        M("How many active users did WeChat Pay have in 2019, versus Alipay?", "800 million versus 520 million", ["520 million versus 800 million", "37 million versus 54 million", "80 million versus 52 million"], "WeChat overtook Alibaba in 2019."),
        M("What can WeChat Pay also be used for?", "Bus or subway rides by scanning the ride code", ["Flights only", "Taxes only", "Tuition only"], "Bus or subway rides."),
        M("What is Tujia’s estimated market share?", "42%", ["31%", "8%", "54%"], "42% for Tujia."),
        M("What is Airbnb’s estimated share of short-term lodging platforms in China?", "8%", ["42%", "31%", "37%"], "8% for Airbnb."),
        M("When was Tujia launched?", "2011", ["2001", "2019", "1999"], "Launched in 2011."),
        M("How many ride-hailing companies held operating licenses as of August 2018?", "Over 80", ["Over 8", "Over 800", "Exactly 2"], "Over 80."),
        M("What share of the market does Didi Chuxing occupy?", "More than 90%", ["About 10%", "About 50%", "About 31%"], "More than 90%."),
        M("How many ride-hailing users were there in China as of June 2019?", "337 million", ["33.7 million", "3.37 billion", "6.7 million"], "337 million."),
        M("Where is DiDi Travel headquartered?", "Beijing", ["Shanghai", "Shenzhen", "Hangzhou"], "Headquartered in Beijing."),
    ],
)

UNIT = unit("第二十五课 Presentation 3: 滴滴出行, 根据和据, 就是和也就是, 来说, 化, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
