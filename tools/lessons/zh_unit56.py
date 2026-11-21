"""Unit 56: Lesson 19 (Travel by High-Speed Rail) Presentation 3 and Area Studies from the book's texts: the first-person ride from Shanghai's
point of view, the adverb 最近, the adverb 才, the prepositions 向, 往 and 对, the conjunction 由于, the skill-integration activities
(Amtrak to Washington, every city on the high-speed rail, the Beijing-Shanghai schedules), the using-Chinese activities (face-scan entry, the
last green train 6451) and the Area Studies reading "China's Fast-Growing Transportation System" and the vocabulary list. Audio, pictures and
links are not included; numbers the book writes as digits are spelled out in the Chinese text; answer keys the book does not print are mine and labeled."""
from zh_auto import *
from zh_l19_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("列车长", 2, "zhang3"), ("机长", 1, "zhang3"), ("背着", 0, "bei1"), ("行驶", 0, "xing2"), ("贵不了", 2, "liao3"), ("参军", 0, "can1"), ("没有", 0, "mei2"), ("没问题", 0, "mei2"), ("没那么", 0, "mei2"), ("没什么", 0, "mei2"), ("没想好", 0, "mei2"),
                          ("没买", 0, "mei2"), ("没去", 0, "mei2"), ("没洗", 0, "mei2"), ("没做", 0, "mei2"), ("还没", 1, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("长大", 0, "zhang3"),
                          ("得好好", 0, "dei3"), ("多得", 1, "de5"), ("教练", 0, "jiao4"), ("觉得买", 1, "de5"), ("下得有", 1, "de5")):
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

# ------------------------------------------------------------------ 1. the passage
P3 = "最近我去上海旅游，第一次乘坐了高铁。因为我已经在网上订好了票，所以到了火车站以后，我在取票机上扫了一下我的护照，票就出来了。进了火车站以后，我才发现高铁站简直就像机场候机厅一样，墙上挂着几个很大的显示屏，两边还有不少商店和快餐店。检票上车不久，列车就正点发车了，十二分钟后，速度就达到了每小时三百五十公里。很快，车上的服务员就开始服务了，他们热情地询问旅客们有什么需要。列车行驶了半个小时以后，列车长突然宣布：“由于安全原因，列车现在减速运行，我们向各位旅客表示歉意。”我快快地看了一下显示器，列车正以每小时二百七十五公里的速度运行。中国人真是太“风趣”了！几分钟以后，列车又回到了原速。我坐在舒适的座位上，一边听着音乐，一边看着窗外的农田、城镇和村庄。不知不觉，列车就驶进了中国最大的城市——上海。"
P3_E = "Recently I went to Shanghai on a trip and rode the high-speed rail for the first time. Because I had already booked the ticket online, after arriving at the station I scanned my passport on the ticket machine and the ticket came out. After entering the station I discovered that the high-speed rail station was practically like an airport waiting hall: several very large display screens hung on the walls, and on both sides there were quite a few shops and fast-food restaurants. Soon after I checked my ticket and boarded, the train departed on time, and twelve minutes later its speed reached 350 kilometers an hour. Very soon the attendants on the train began service, warmly asking the passengers what they needed. Half an hour after the train started running, the conductor suddenly announced: “For safety reasons the train is now slowing down; we apologize to all passengers.” I quickly looked at the monitor; the train was running at 275 kilometers an hour. The Chinese are really so “humorous”! A few minutes later the train returned to its original speed. I sat in the comfortable seat listening to music and looking at the farmland, towns and villages outside the window. Before I knew it, the train had pulled into China’s biggest city, Shanghai. (the book also prints it in traditional characters and writes 350 and 275 as digits)"
A1P3 = [("我在取票机上扫了一下我的护照，票就出来了。", "1. How did he get his ticket? He scanned his passport on the ticket machine and the ticket came out. (my answer)"), ("高铁站简直就像机场候机厅一样，墙上挂着几个很大的显示屏，两边还有不少商店和快餐店。", "2. What was the station like? Practically like an airport waiting hall, with big display screens and shops and fast-food restaurants. (mine)"), ("列车长突然宣布：“由于安全原因，列车现在减速运行。”", "3. What happened half an hour after departure? The conductor suddenly announced a slowdown for safety reasons and apologized. (mine)"),
        ("列车正以每小时二百七十五公里的速度运行。", "4. Why “中国人太风趣了”? Because the “slow” speed was still 275 km/h, so “slowing down” was a joke. (mine)"), ("他一边听着音乐，一边看着窗外的农田、城镇和村庄。", "5. What was he doing during the ride? Listening to music and looking at farmland, towns and villages. (mine)")]
L1 = lesson(
    "Lesson 19 Presentation 3: my first high-speed ride to Shanghai",
    "取票机上扫护照 · 高铁站像候机厅 · 列车减速 · 不知不觉到了上海",
    requires=[],
    cards=[
        card("Getting Started",
             "A photograph of a station waiting area (not included). Pair up and discuss: A. What does the waiting area look like in an airport or a train station in America? B. What do the attendants do before an airplane or train departs? C. When do the captain or train conductors make announcements to passengers?"),
        card("Presentation 3: 第一次乘坐高铁", "The book also prints the passage in traditional characters.", examples=[D(P3, P3_E)]),
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 3 and choose the correct answer: The train ride did not go as smoothly as the speaker had expected. / The train ride went smoothly until the scary accident. / The train ride was satisfactory as far as the speaker was concerned. (Audio, not included; from the text the third is right.) B. Detailed listening: 1. How did the speaker get his ticket at the train station? 2. What was the train station like? 3. What happened 30 minutes after the train departed? 4. Why did the speaker say “中国人太风趣了”? 5. What was the speaker doing during the ride? My answers, each with the line from the passage:",
             examples=[D(z, e) for z, e in A1P3]),
    ],
    exercises=[
        M("Where did the writer travel?", "Shanghai", ["Beijing", "Xi’an", "Guangzhou"], "我去上海旅游."),
        M("How did he get his ticket?", "He scanned his passport on a ticket machine", ["He bought it from a person", "A friend gave it", "He printed it at home"], "在取票机上扫了一下我的护照."),
        M("What was the station like?", "Like an airport waiting hall", ["Small and empty", "Dark and old", "Like a market"], "简直就像机场候机厅一样."),
        M("What hung on the walls?", "Several large display screens", ["Posters", "Paintings", "Clocks only"], "墙上挂着几个很大的显示屏."),
        M("How soon did the train reach 350 km per hour?", "In twelve minutes", ["In two minutes", "In an hour", "In half a day"], "十二分钟后."),
        M("What did the attendants do?", "Warmly asked what passengers needed", ["Sold tickets", "Checked passports", "Played music"], "热情地询问旅客们有什么需要."),
        M("What did the conductor announce?", "The train was slowing down for safety reasons", ["The train was late", "The train would stop", "Lunch was ready"], "由于安全原因，列车现在减速运行."),
        M("What speed did the monitor show during the slowdown?", "275 kilometers an hour", ["50 kilometers an hour", "100 kilometers an hour", "350 kilometers an hour"], "每小时二百七十五公里."),
        M("What did he do during the ride?", "Listened to music and watched the scenery", ["Slept", "Worked", "Read the newspaper"], "一边听着音乐，一边看着窗外."),
        F("我在取票___上扫了一下我的护照，票就出来了。", "机", PART, "取票机: ticket machine."),
        F("列车长突然宣___：“由于安全原因，列车现在减速运行。”", "布", PART, "宣布: announce."),
        F("我才发现高铁站___直就像机场候机厅一样。", "简", PART, "简直: practically."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2-4
AR = [("下了车以后我才发现上海高铁站简直就像浦东机场的候机厅一样。", "1. After getting off I discovered that Shanghai’s high-speed rail station was practically like the waiting hall of Pudong Airport. (key mine)"), ("十二分钟后，显示屏显示列车时速达到了每小时三百五十公里。", "2. Twelve minutes later the display screen showed that the train speed reached 350 kilometers an hour. (mine)"), ("服务员热情地询问旅客们要不要订餐。", "3. The attendant warmly asked the passengers whether they wanted to order a meal. (mine)"),
      ("机长突然宣布飞机要减速飞行，并向旅客们表示歉意。", "4. The captain suddenly announced that the plane would slow down, and apologized to the passengers. (mine)"), ("最近几个月她经常坐高铁去北京，每次都是不知不觉地就到了。", "5. In the last few months she often goes to Beijing by high-speed rail, and every time she arrives before she knows it. (mine)"), ("我在飞机场的取票机上扫了一下我的身份证，机票就出来了。", "6. I scanned my ID card on the ticket machine at the airport and the ticket came out. (mine)")]
EX4 = [("甲：我想坐高铁去杭州，你知道怎么买票吗？乙：你可以在网上订票，然后到火车站的取票机上取票。", "1. A: I want to take the high-speed rail to Hangzhou; do you know how to buy a ticket? B: You can book online and then pick the ticket up at the ticket machine at the station. (the book leaves A’s and B’s blanks; my fills)"), ("甲：请问，进车站以后在哪里能看到列车的到达时间？乙：墙上挂着几个很大的显示屏，你可以在那儿看。", "2. A: Excuse me, where can I see the train arrival times after entering the station? B: There are several big display screens on the wall; you can look there."),
       ("甲：我已经在网上订好票了，请问怎么取票？乙：在取票机上扫一下护照，车票就出来了。", "3. A: I’ve already booked online; how do I pick up the ticket? B: Scan your passport on the ticket machine and the ticket comes out."), ("甲：各位旅客，由于安全原因，列车现在减速运行，我们向各位旅客表示歉意。乙：服务员，请问列车还能正点到达北京吗？", "4. A: Dear passengers, for safety reasons the train is now slowing down; we apologize. B: Attendant, can the train still arrive in Beijing on time?"),
       ("甲：请问您要喝点儿什么？乙：我要一瓶可乐。谢谢！", "5. A: What would you like to drink? B: I’d like a bottle of cola. Thanks!"), ("甲：这个高铁站简直就像机场候机厅一样。乙：高铁站就是这样啊。", "6. A: This high-speed rail station is practically like an airport waiting hall. B: High-speed rail stations are just like this."),
       ("甲：请问这趟高铁的时速是多少？乙：每小时三百公里。", "7. A: How fast is this high-speed train per hour? B: 300 kilometers an hour."), ("甲：我想知道怎么换票，您能告诉我吗？乙：你可以找列车长询问一下。", "8. A: I want to know how to change a ticket; can you tell me? B: You can ask the conductor.")]
TAB3 = table(["关于", "中文词语 (mine)"],
             [["订票、取票", "在网上订票，取票机，扫一下护照，票就出来了"], ["高铁站", "候机厅，显示屏，商店，快餐店"], ["列车运行", "正点发车，达到每小时三百五十公里，减速运行，回到原速"], ["服务", "热情地询问，有什么需要，表示歉意"], ["体验", "舒适的座位，听着音乐，看着窗外，不知不觉"]],
             title="Activity 2 A: expressions from Presentation 3 (the book leaves the table blank; this fill is mine)", say=[0, 1])
L2 = lesson(
    "Lesson 19 Presentation 3 activities: arranging sentences and completing exchanges",
    "Activities 2 to 4 · 简直就像 · 询问 · 表示歉意 · 取票",
    requires=[],
    cards=[
        card("Activity 2 (Writing, Reading and Speaking)",
             "A. Pair up and fill in the table with the expressions you’ve just learned (订票、取票, 高铁站, 列车运行, 服务, 体验). B. Rearrange the expressions and write logical, correct sentences. The six sets: 1. 简直就像 / 我才发现 / 一样 / 浦东机场的 / 上海高铁站 / 下了车以后 / 候机厅 2. 达到了 / 显示屏显示 / 每小时 / 350 公里 / 十二分钟后 / 列车时速 3. 询问 / 热情地 / 订餐 / 服务员 / 要不要 / 旅客们 4. 向旅客们 / 飞机要 / 表示歉意 / 减速飞行 / 机长 / 并 / 突然宣布 5. 坐高铁去北京 / 每次都是 / 就到了 / 不知不觉地 / 最近几个月 / 她经常 6. 取票机上 / 飞机场的 / 我的身份证 / 扫了一下 / 我在 / 机票就出来了. C. Pair up, share your work and go over the suggested answers; translate the sentences into English. The book’s suggested answers are not in the text, so my answers:",
             tables=[TAB3], examples=[D(z, e) for z, e in AR]),
        card("Activity 3 (Listening, Writing, Speaking and Reading)",
             "A. Listen to the six statements and write down the main idea of each statement in English. B. Pair up and check your answers against the script your teacher provided; take turns translating the sentences into English. (Audio and the teacher’s script, not included.)"),
        card("Activity 4 (Writing and Speaking)",
             "A. Complete the eight exchanges (for example: A: 我想坐高铁去杭州，你知道怎么买票吗？ B: ___。 / A: ___？ B: 在取票机上扫一下护照，车票就出来了。 / A: 各位旅客，___。 B: 服务员，请问列车还能正点到达北京吗？ / A: ___？ B: 每小时三百公里。 / A: ___ B: 你可以找列车长询问一下。). B. Share your work in pairs and refine your sentences with your partner’s feedback; take turns translating the exchanges into English and back into Chinese. My completed exchanges:",
             examples=[D(z, e) for z, e in EX4]),
    ],
    exercises=[
        M("Which sentence is arranged correctly?", "服务员热情地询问旅客们要不要订餐", ["热情地服务员询问旅客们订餐要不要", "服务员询问热情地订餐旅客们要不要", "旅客们热情地服务员询问要不要订餐"], "Key 3."),
        M("Which sentence is arranged correctly?", "机长突然宣布飞机要减速飞行，并向旅客们表示歉意", ["机长并突然宣布向旅客们飞机要减速飞行表示歉意", "飞机要机长突然宣布向旅客们表示歉意减速飞行", "表示歉意机长突然宣布并飞机要减速飞行"], "Key 4."),
        M("What does 简直就像 mean?", "Practically like", ["Not at all like", "Never like", "Almost nothing"], "简直: practically."),
        M("What does 不知不觉 mean?", "Before one knows it", ["Knowing everything", "Not knowing anything", "Suddenly knowing"], "不知不觉: unconsciously."),
        M("Which sentence says the ticket came out?", "我在取票机上扫了一下我的身份证，机票就出来了", ["我在机票上扫了一下取票机", "取票机在我的身份证上出来了", "机票扫了一下我的取票机"], "Key 6."),
        M("What does the attendant ask in key 3?", "Whether passengers want to order a meal", ["How old they are", "Where they are going", "Whether they have passports"], "询问旅客们要不要订餐."),
        M("In exchange 4, who apologizes?", "The announcer to all the passengers", ["The passengers", "The attendant to the captain", "Nobody"], "我们向各位旅客表示歉意."),
        M("In exchange 7, how fast is the train?", "300 kilometers an hour", ["30 kilometers an hour", "350 kilometers an hour", "3,000 kilometers an hour"], "每小时三百公里."),
        F("机长突然宣布飞机要减速飞行，并向旅客们表示歉___。", "意", PART, "歉意: apology."),
        F("服务员热情地询___旅客们要不要订餐。", "问", PART, "询问: inquire."),
    ],
)

# ------------------------------------------------------------------ 3. 最近
ZJ = table(["Chinese", "English"],
           [["最近几天", "in/over the last few days; in recent days"], ["最近几个星期", "in/over the last few weeks; in recent weeks"], ["最近几个月", "in/over the last few months; in recent months"], ["最近几年", "in/over the last few years; in recent years"], ["最近三天", "in/over the last 3 days"], ["最近两个星期", "in/over the last 2 weeks"], ["最近四个月", "in/over the last 4 months"], ["最近五年", "in/over the last 5 years"]],
           title="The adverb 最近 with time words (the first four are general, the last four specific; the book prints “last few weeks” for the months and years rows, which is corrected here)")
ZJ2 = [("甲：小李去过苏州吗？乙：他上大学的时候去过，最近几年没去。", "1. A: Has Xiao Li been to Suzhou? B: He went when he was in college, but hasn’t been in recent years. (key mine)"), ("甲：琳达的作业多不多？乙：马上就要考试了，所以最近几天作业很多。", "2. A: Does Linda have a lot of homework? B: The exam is coming soon, so she has had a lot of homework these last few days. (mine)"),
       ("甲：小王那里最近的天气怎么样？乙：他们那里最近几天一直在下雨，明天可能要下大雨。", "3. A: How has the weather been at Xiao Wang’s place lately? B: It has been raining all along these last few days there, and tomorrow it might rain heavily. (mine)"), ("甲：今天小张过生日，他女朋友怎么没来？乙：她最近两个月都在北京学习，下个星期就会回来。", "4. A: Today is Xiao Zhang’s birthday; why didn’t his girlfriend come? B: She has been studying in Beijing for the last two months and will come back next week. (mine)"),
       ("甲：为什么大力很长时间没去操场锻炼身体了？乙：他最近一个月都去体育馆游泳，所以就没去操场。", "5. A: Why hasn’t Dali been to the sports field to exercise for a long time? B: He has been going to the gym to swim the last month, so he hasn’t gone to the field. (mine)")]
L3 = lesson(
    "Lesson 19 Presentation 3 grammar: the adverb 最近",
    "最近几天 · 最近几个月 · 最近三天 · 最近五年",
    requires=[],
    cards=[
        card("Use of the adverb 最近",
             "The adverb 最近 can form expressions with certain time words to indicate recent days, weeks, months, years and so on. Compare Chinese and English; in the table the first four are the general expressions and the last four the specific ones.",
             tables=[ZJ]),
        card("Grammar Activities 1 and 2",
             "Activity 1 (Listening, Writing, Speaking and Reading): A. Listen to the sentences and answer in Chinese: 1. 说话人经常回中国吗？ 2. 说话人最近给家里打电话了吗？为什么？ 3. 现在蔬菜为什么特别贵？ 4. 说话人问的问题是什么？ 5. 说话人还经常去滑雪吗？为什么？ 6. 羊羊为什么还没回家？ B. Pair up, share your work and go over the text. (Audio, not included; the book prints no script.) Activity 2 (Reading, Writing and Speaking): A. Read the exchanges and complete the sentences using one instance of 最近 in each; B. pair up, share your work and go over the suggested text. The blanks were lost in the printed text, so the completed exchanges are my reconstruction:",
             examples=[D(z, e) for z, e in ZJ2]),
    ],
    exercises=[
        M("What does 最近几天 mean?", "In the last few days", ["In a few years", "Tomorrow", "Last year"], "最近几天."),
        M("What does 最近五年 mean?", "In the last 5 years", ["In 5 days", "Every 5 years", "Next 5 years"], "最近 + number + time word."),
        M("Which means “in recent months”?", "最近几个月", ["最近三天", "最近五年", "最近几天"], "最近几个月."),
        M("Which is specific?", "最近四个月", ["最近几天", "最近几个星期", "最近几年"], "Number + time word is specific."),
        M("Complete: 琳达的作业多不多？马上就要考试了，所以___作业很多。", "最近几天", ["昨天", "去年", "三年前"], "最近几天."),
        M("Complete: 他___都去体育馆游泳，所以就没去操场。", "最近一个月", ["去年夏天", "明年", "三年前"], "最近一个月."),
        M("What does “她最近两个月都在北京学习” mean?", "She has been studying in Beijing for the last two months", ["She will study two months", "She studied two years ago", "She doesn’t study"], "最近两个月."),
        M("What does “最近几个星期” mean?", "In the last few weeks", ["In a few days", "Next weeks", "Two weeks ago"], "最近几个星期."),
        F("最近几___，蔬菜特别贵。", "天", PART, "最近几天: lately."),
        F("他最近___个月都在北京学习。", "两", PART, "最近两个月."),
    ],
)

# ------------------------------------------------------------------ 4. 才
CA = [("每天我们都等爸爸妈妈回家后才吃晚饭。", "1. Every day we wait until Mom and Dad come home before eating dinner."), ("你们散步以后才吃晚饭，还是吃了晚饭以后才散步？", "2. Do you eat dinner after you take a walk, or do you walk after you have eaten dinner?"), ("见到他以后我才知道他中文说得那么好。", "3. Only after meeting him did I know he speaks Chinese so well."), ("看了今天的新闻我才知道我们老家也有高铁站了。", "4. Only after reading today’s news did I know our hometown has a high-speed rail station too."), ("你每天都是锻炼完身体以后才做作业吗？", "5. Do you do your homework only after you finish exercising every day?")]
CA3 = [("我订好了高铁票以后才打电话告诉我父母，说我明天回家。", "1. Only after I booked the high-speed rail ticket did I phone my parents to tell them I’d be home tomorrow. (key mine)"), ("你是来到蒙特雷以后才发现蒙特雷的海边非常漂亮的吗？", "2. Was it only after you came to Monterey that you discovered the seaside is so beautiful? (mine)"), ("我订好了机票以后才看到另一个网站卖的机票更便宜。", "3. Only after I booked the plane ticket did I see that another website sold cheaper tickets. (mine)"),
       ("到了中国以后我才发现大家买东西都用手机付钱。", "4. Only after arriving in China did I discover that everyone pays with their phone when shopping. (mine)"), ("你们是在旧金山玩儿了半天以后才开车回家的吗？", "5. Did you drive home only after playing half a day in San Francisco? (mine)"), ("我们去商店买了东西以后才去老李家参加老朋友聚会。", "6. Only after we bought things at the store did we go to Lao Li’s home for the old friends’ party. (mine)")]
CA5 = [("我走到学校的时候，天才黑。", "1. By the time I walked to school it was only just getting dark. (sample, mine)"), ("学了三年中文以后，他才能看中文报纸。", "2. Only after three years of Chinese could he read a Chinese newspaper. (mine)"), ("听你这么一说，我才知道高铁那么快。", "3. Only after hearing you say that did I know the high-speed rail is that fast. (mine)"), ("我体验了一下高铁，才知道自己那么喜欢它。", "4. Only after trying the high-speed rail did I know how much I like it. (mine)"), ("坐了一次高铁，我才知道服务那么周到。", "5. Only after riding the high-speed rail once did I know the service is so thoughtful. (mine)")]
L4 = lesson(
    "Lesson 19 Presentation 3 grammar: the adverb 才",
    "…以后才… · not until · rewriting with 才",
    requires=[],
    cards=[
        card("The adverb 才",
             "The adverb 才 can be used to indicate “not until”. In addition to indicating that something does not happen until a certain time, such as 我八点才回到家, 才 can also be used to indicate that something does not happen until another event occurs. For instance, 他们有了第一个孩子以后才搬家, “They didn’t move until they had their first child”. 才 is often used in complex sentences. Like many Chinese complex sentences, if the subject is the same it usually appears just once. For instance, instead of 我做完作业以后我才睡觉, we usually say 做完作业以后我才睡觉, or 我做完作业以后才睡觉. Examples:",
             examples=[D(z, e) for z, e in CA]),
        card("Grammar Activity 3 (Reading, Writing and Speaking)",
             "A. Rewrite the six sentences using 才 (originals: 1. 我订好了高铁票以后，打电话告诉我父母，说我明天回家。 2. 你是来到蒙特雷以后，发现蒙特雷的海边非常漂亮的吗？ 3. 我订好了机票以后，看到另一个网站卖的机票更便宜。 4. 到了中国以后，我发现大家买东西都用手机付钱。 5. 你们是在旧金山玩儿了半天，然后开车回家的吗？ 6. 我们去商店买了东西，然后去老李家参加老朋友聚会。) B. Pair up, share your work and check the suggested answers. The book’s suggested answers are not in the text, so these are mine:",
             examples=[D(z, e) for z, e in CA3]),
        card("Grammar Activities 4 and 5",
             "Activity 4 (Listening, Speaking and Reading): A. Listen and transcribe eight statements in English; B. pair up, share your work and go over the script and the suggested English translations. (Audio, not included.) Activity 5 (Speaking and Writing): in pairs, write sentences using the expressions provided and use 才 in each: 1. 走到学校，天黑 2. 学三年中文，看中文报纸 3. 听你这么一说，高铁那么快 4. 体验一下…，喜欢 5. 坐一次…，服务那么周到. The book leaves the sentences to the student; my samples:",
             examples=[D(z, e) for z, e in CA5]),
    ],
    exercises=[
        M("What does 才 indicate here?", "Not until", ["Already", "Always", "Never"], "才: not until."),
        M("What does “我八点才回到家” mean?", "I didn’t get home until eight", ["I got home at eight already", "I will go home at eight", "I never go home"], "才."),
        M("What does “他们有了第一个孩子以后才搬家” mean?", "They didn’t move until they had their first child", ["They moved before their first child", "They have no children", "They never move"], "才 after an event."),
        M("Where does 才 go in 我做完作业以后才睡觉?", "Before the verb after the first clause", ["At the end", "Before the subject", "After 吗"], "…以后才…."),
        M("Rewrite “到了中国以后，我发现…” with 才.", "到了中国以后我才发现…", ["到了中国以后我发现才…", "到了中国才以后我发现…", "才到了中国以后我发现…"], "Key 4."),
        M("What does “看了今天的新闻我才知道我们老家也有高铁站了” mean?", "Only after reading today’s news did I know", ["I read the news before", "I never read news", "I wrote the news"], "…才知道."),
        M("Complete: 每天我们都等爸爸妈妈回家后___吃晚饭。", "才", ["就", "又", "再也"], "才."),
        M("Which question asks about the order of walking and dinner?", "你们散步以后才吃晚饭，还是吃了晚饭以后才散步？", ["你们几点吃晚饭？", "你们在哪儿散步？", "你们吃什么晚饭？"], "Example 2."),
        F("见到他以后我___知道他中文说得那么好。", "才", PART, "才: only then."),
        F("你每天都是锻炼完身体以后才做作___吗？", "业", PART, "作业: homework."),
    ],
)

# ------------------------------------------------------------------ 5. 向 往 对
XD1 = [("他向我们走来。", "He walks toward us."), ("他往我们这儿走来。", "He walks toward us."), ("他对我们很好。", "He is nice toward us.")]
XD2 = [("向北走 = 往北走", "Walk north (向 more formal, 往 colloquial)."), ("向前看 = 往前看", "Look ahead."), ("向学校走去 = 往学校走去", "Walk toward the school.")]
XD3 = [("我们向各位旅客表示歉意。", "1. We apologize to all passengers. (向 can take a person as its object; 往 cannot)")]
XD4 = [("他俩面对面聊天。", "They chat face to face."), ("向日葵向着太阳开。", "Sunflowers (Xiàngrìkuí) bloom facing the sun."), ("我们教室的窗户对着操场。", "The windows of our classroom face the sports field."), ("两架飞机，一架向东飞，一架向西飞。", "Two planes, one flying east, one flying west (向)."), ("两架飞机，一架往东飞，一架往西飞。", "Two planes, one flying east, one flying west (往).")]
XD5 = [("我对他说：“谢谢啦！”", "I said to him, “Thanks!”"), ("他对中国高铁很感兴趣。", "He is very interested in China’s high-speed rail."), ("我们对各位旅客表示歉意。", "We apologize to all passengers (对).")]
XD6 = [("飞往北京，开往北京，通往北京，送往，寄往，运往", "Words with 往 often used in announcements and news reports: fly to Beijing, bound for Beijing, lead to Beijing, send to, mail to, transport to.")]
XA6 = [("去北京的火车是往南开还是往北开？", "1. Does the train to Beijing go south or north? (往 or 向; key mine)"), ("离开前，他对连长说：“谢谢连长！”还向连长敬了一个礼。", "2. Before leaving, he said to the company commander, “Thank you, sir!” and also saluted him. (对, 向)"), ("妈妈对我说：“你的学习成绩是不错，但还可以更好。”", "3. Mom said to me, “Your grades are good, but they can be even better.” (对)"), ("搬家以后，琳达对我们说，向南的房子真好，从早到晚都有太阳。", "4. After moving, Linda told us that a south-facing house is really nice, with sun from morning till night. (对, 向)"),
       ("张老师对我说：“你的作业有几个错儿，中午我给你讲讲。”", "5. Teacher Zhang said to me, “There are a few mistakes in your homework; at noon I’ll go over them with you.” (对)"), ("大卫和同学们边说话边往操场走去。", "6. David and his classmates walked toward the sports field as they talked. (往 or 向)"), ("一看到妈妈，那个小女孩儿就飞快地向妈妈跑过去。", "7. As soon as she saw her mother, the little girl ran quickly toward her. (向, since 往 can’t take a person)")]
XA7 = [("医生对我说，糖吃得太多对身体不好。", "1. The doctor said to me, “Eating too much sugar is bad for your health.” (key mine: e)"), ("早上起床以后，她向山下的操场走去。", "2. After getting up in the morning she walked toward the sports field at the foot of the hill. (d)"), ("每次考完试，妈妈总对我说，不够好，你应该考一百分。", "3. Every time after an exam Mom always says to me, “Not good enough; you should get 100.” (a)"), ("今天王老师对我们说，下星期二是我们班的做饭日。", "4. Today Teacher Wang told us that next Tuesday is our class’s cooking day. (h)"),
       ("不下雨了，太阳也出来了，琳达对我说，现在咱们可以出去走走了吧？", "5. The rain stopped and the sun came out; Linda said to me, “Now we can go out for a walk, can’t we?” (f)"), ("从这儿向前走五十米，向左拐，再走五分钟就是邮局。", "6. From here go forward fifty meters, turn left, and walk five more minutes and you’re at the post office. (g)"), ("老师向他笑笑，然后回答了他的问题。", "7. The teacher smiled at him and then answered his question. (b)"), ("服务员对我说，往前走，过两个车厢，就是餐车。", "8. The attendant told me, “Go forward, pass two carriages, and it’s the dining car.” (c)")]
L5 = lesson(
    "Lesson 19 Presentation 3 grammar: the prepositions 向, 往 and 对",
    "向 往 对 · toward · 对 introduces the object of an action",
    requires=[],
    cards=[
        card("The prepositions 向, 往 and 对",
             "向, 往 and 对 can all be translated as “toward” in English. For example:", examples=[D(z, e) for z, e in XD1]),
        card("Overlap and differences",
             "向, 往 and 对 may overlap in meaning or usage, but they are different as well. Etymology: 向 originally meant a window, then to face, then toward; 往 originally meant to go, then toward, then to; 对 originally meant to face, then to respond, then toward, then to. Overlap: both 向 and 往 can indicate moving toward a certain direction or object; 向 is more formal and 往 is colloquial. Differences: 1. 向 can take a person as its object; 往 cannot (the book marks 我们往各位旅客表示歉意 with an asterisk as wrong). 2. 向 and 对 are also used as verbs to describe a static state; 往 is only for moving actions. 3. 对 is used to introduce the object of an action instead of direction. 4. 往 words used in announcements and news reports.",
             examples=[D(z, e) for z, e in XD2 + XD3 + XD4 + XD5 + XD6]),
        card("Grammar Activity 6 (Reading, Writing and Speaking)",
             "A. Complete the sentences using 向, 往 or 对 (敬礼, jìnglǐ, salute). The book leaves the blanks to the student and prints no key; my completed sentences:",
             examples=[D(z, e) for z, e in XA6]),
        card("Grammar Activity 7 (Reading and Speaking)",
             "A. Match the elements in Column A with those in Column B by writing the letter in the middle column. B. Pair up, share your work and discuss why you made your choices; translate each sentence into English and back into Chinese. The book prints no key; my matched sentences:",
             examples=[D(z, e) for z, e in XA7]),
    ],
    exercises=[
        M("Which preposition can take a person as its object, “We apologize to all passengers”?", "向", ["往", "Neither", "Both equally"], "向 can take a person; 往 cannot."),
        M("Which is only for moving actions?", "往", ["向", "对", "Both 向 and 对"], "往 is only for moving."),
        M("Which introduces the object of an action rather than direction?", "对", ["向", "往", "Neither"], "对."),
        M("Which is the more formal of 向 and 往?", "向", ["往", "Both", "Neither"], "向 more formal."),
        M("Complete: 我们教室的窗户___着操场。", "对", ["往", "到", "把"], "对着: facing."),
        M("Complete: 他___中国高铁很感兴趣。", "对", ["往", "向", "给"], "对…感兴趣."),
        M("Complete: 一看到妈妈，那个小女孩儿就飞快地___妈妈跑过去。", "向", ["往", "对", "给"], "向 + person."),
        M("Which -往 word means “bound for”?", "开往", ["对往", "往开", "向往往"], "开往 (北京)."),
        M("What does “向日葵向着太阳开” describe?", "A static state of facing", ["Moving to the sun", "Planting seeds", "A sunny day"], "向 as a verb of a static state."),
        M("Which line matches “医生对我说，”?", "糖吃得太多对身体不好", ["向左拐，再走五分钟就是邮局", "往前走，过两个车厢，就是餐车", "然后回答了他的问题"], "Key 1 + e."),
        F("大卫和同学们边说话边___操场走去。", "往", PART, "往操场走去."),
        F("妈妈___我说：“你的学习成绩是不错，但还可以更好。”", "对", PART, "对我说."),
    ],
)

# ------------------------------------------------------------------ 6. 由于 + skill integration 1
YY = [("由于安全原因，列车现在减速运行。", "For safety reasons the train is now slowing down. (formal)"), ("因为安全原因，列车现在减速运行。", "Because of safety reasons the train is now slowing down. (less formal)"), ("因为雨太大，她不想出去跑步了。", "Because the rain is too heavy she doesn’t want to go out running."), ("由于雨太大，她不想出去跑步了。", "Because the rain is too heavy she doesn’t want to go out running. (rarely said)"),
      ("她不想去跑步了，因为雨太大了。", "She doesn’t want to go running anymore, because the rain is too heavy."), ("你得走路回去了，因为太晚了，没车了。", "You have to walk back, because it’s too late and there are no more buses."),
      ("由于高铁给人们出行提供了方便，因此中国最近十几年出现了旅游热。", "Because high-speed rail has made traveling convenient for people, a tourism boom has appeared in China in the last dozen or so years."), ("由于列车突然减速让乘客不适，因而列车长需要表示歉意。", "Because the train’s sudden slowdown made passengers uncomfortable, the conductor needs to apologize.")]
YYM = [("在语言节宣布：由于演员身体不适，因此他们需要休息。", "Pair 1 first part (the book’s example): At the Language Day announcement: “Because the actors feel unwell, therefore they need rest.” (class guess 1)"), ("由于演员身体不适，因而大家看不到演出了。", "Class guess 2: because the actors are unwell, everyone cannot see the show."), ("由于演员身体不适，因而学校请来了中医师。", "Pair 1 second part: because the actors are unwell, the school invited a traditional Chinese medicine doctor.")]
YYM2 = [("在学校宣布：由于明天有大雪，因此学校明天放假一天。", "Scenario: school announcement. Cause: because there will be heavy snow tomorrow; outcome: therefore school will be closed for a day tomorrow. (my sample announcement)")]
L6 = lesson(
    "Lesson 19 Presentation 3 grammar: the conjunction 由于, and Skill Integration (Amtrak to Washington)",
    "由于 … 因此/因而 · formal announcements · 乘火车去华盛顿",
    requires=[],
    cards=[
        card("Conjunction 由于",
             "In this presentation the train conductor announced: 列车长突然宣布：“由于安全原因，列车现在减速运行，……” Here 由于 is a conjunction similar to 因为, introducing a reason and meaning “because”. Compare with 因为: 1. 由于 is more formal and not usually used in casual conversation. 2. Because of its formality it cannot be used in the later part of a complex sentence like 因为: the book marks 她不想去跑步了，由于雨太大了 and 你得走路回去了，由于太晚了，没车了 with asterisks as wrong. 3. 因为 goes with 所以; 由于 goes with 因此 or 因而. Examples:",
             examples=[D(z, e) for z, e in YY]),
        card("Grammar Activity 8 (Writing and Speaking)",
             "A. Pair up with a partner. Together think of a social event or scenario and come up with a formal announcement with 由于; write it in the table (Scenario; Announcement: Cause (由于), Outcome). B. Each pair shares the first part of their announcement in class and asks the class to guess the second part; after the class makes two guesses the pair shares the second part. (A picture, not included.) The book’s example, and my sample announcement:",
             examples=[D(z, e) for z, e in YYM + YYM2]),
        card("Skill Integration Activity 1 (Writing, Listening, Speaking and Reading)",
             "A. Song Laoshi wants to travel to Washington D.C., and you suggest that she take Amtrak; she has never taken a train in America. Think about what you would tell her to do; you may want to go to Amtrak’s Chinese website for the information (link not included). In Chinese, write your discussion points. B. Listen to the dialog and take notes (check your dictionary for 汽油 and 了解 first: mine, gasoline and to understand); pair up and discuss what information in the audio could benefit Song Laoshi on her trip, in the table 坐火车: 时间, 钱, 看什么, 设施; 火车上的服务和设施: 用餐, 卧铺. C. Go over the script and refine your notes; then write an email to Song Laoshi explaining what her trip will be like and how she should prepare (TO, CC, Subject). (Audio, not included; the book prints no script.)"),
    ],
    exercises=[
        M("What does 由于 mean?", "Because; due to", ["Although", "If", "Unless"], "由于: because (formal)."),
        M("Which is more formal?", "由于", ["因为", "Both equally", "Neither"], "由于 is more formal."),
        M("Which can be used in the later part of a complex sentence?", "因为", ["由于", "Both", "Neither"], "She doesn’t want to go running, 因为雨太大了."),
        M("Which goes with 由于?", "因此 or 因而", ["所以 only", "但是", "如果"], "由于…因此/因而."),
        M("Which goes with 因为?", "所以", ["因此", "因而", "但是"], "因为…所以."),
        M("Complete: ___安全原因，列车现在减速运行。", "由于", ["虽然", "如果", "只要"], "由于 in announcements."),
        M("Which sentence is wrong?", "你得走路回去了，由于太晚了，没车了", ["由于安全原因，列车现在减速运行", "因为雨太大，她不想出去跑步了", "她不想去跑步了，因为雨太大了"], "由于 can’t go in the later part."),
        M("Which fits “由于高铁给人们出行提供了方便，___中国最近十几年出现了旅游热”?", "因此", ["所以", "但是", "也许"], "由于…因此."),
        F("由于列车突然减速让乘客不适，因___列车长需要表示歉意。", "而", PART, "因而: therefore."),
        F("由于高铁给人们出行提供了方便，因___中国最近十几年出现了旅游热。", "此", PART, "因此: therefore."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration 2-3
NEWS = ["二零一八年福建省省内较大的城市都通了高铁，福建成为中国第一个市市通高铁的省。然后，山东、河南等七个省也在二零二零年实现了市市通高铁。", "山东省有一亿多人口，省内的十七个较大的城市已经全部通了高铁，以前坐火车从省内一个城市到另一个城市，最远的需要十多个小时，现在坐高铁不超过三个小时就到了。比如，青岛在山东的东部，是山东第二大城市。现在，从青岛坐高铁去山东东部的城市，一个小时以内就能到，去省内离青岛最远的城市，最多两个小时就能到达。",
        "现在高铁站提供的各种服务也越来越多。比如，在一些高铁站，旅客可以吃，住，购物，玩儿，也可以订旅游景点的门票，以及各地的酒店。"]
NEWS_E = ["1. In 2018 all the larger cities within Fujian Province had high-speed rail, and Fujian became China’s first province with high-speed rail in every city. Then Shandong, Henan and seven other provinces also achieved this in 2020. (underlined sentence 1; the book writes the years and 7 as digits)",
          "2. Shandong Province has over 100 million people, and its 17 larger cities all have high-speed rail now. Before, going by train from one city to another within the province took more than ten hours at the farthest; now by high-speed rail it takes no more than three hours. For example, Qingdao is in eastern Shandong and is the province’s second-largest city. Now, from Qingdao you can reach cities in eastern Shandong in under an hour, and the farthest city in the province from Qingdao in two hours at most. (sentences 2 and 3 are underlined; the book writes 17 as digits)",
          "3. The services provided by high-speed rail stations are also increasing. For example, at some stations passengers can eat, stay, shop and play, and can also book tickets to tourist attractions and hotels in various places. (underlined sentence 4)"]
TFN = [("如果你住在福建省一个比较大的城市，你可以坐高铁去别的地方。", "1. If you live in a fairly large city in Fujian Province, you can take the high-speed rail to other places. — True (key mine)"), ("现在中国有八个省已经做到了省内市市通高铁。", "2. Now eight provinces in China have achieved high-speed rail in every city within the province. — True (Fujian plus seven more)"), ("在山东省，从一个重要城市去另一个重要城市，坐高铁最多需要两个小时。", "3. In Shandong Province, going from one important city to another by high-speed rail takes two hours at most. — False (the report says not more than three hours)"),
       ("坐高铁从青岛到上海三个小时就能到达。", "4. From Qingdao to Shanghai takes three hours by high-speed rail. — False (the report does not say this)"), ("一些高铁站内有旅馆，在高铁站旅客也可以订其他地方的酒店。", "5. Some high-speed rail stations have hotels, and at the station passengers can also book hotels elsewhere. — True")]
SCH = table(["车次", "始发站", "始发时间", "到达站", "到达时间", "二等座", "一等座", "商务座"],
            [["G131", "北京", "6:36", "上海", "12:40", "￥553 有票", "￥933 有票", "￥1748 还有12张"], ["G5", "北京", "7:00", "上海", "11:40", "￥558 有票", "￥939 有票", "￥1762 还有9张"], ["G143", "北京", "7:20", "上海", "13:08", "￥553 有票", "￥933 还有7张", "￥1748 无票"], ["G107", "北京", "7:50", "上海", "13:12", "￥553 有票", "￥933 无票", "￥1748 还有17张"],
             ["G9", "北京", "12:00", "上海", "16:36", "￥553 有票", "￥933 无票", "￥1748 还有8张"], ["G129", "北京", "12:10", "上海", "18:07", "￥558 有票", "￥939 还有6张", "￥1762 无票"], ["G131", "北京", "12:20", "上海", "18:16", "￥553 有票", "￥933 有票", "￥1748 还有12张"], ["G133", "北京", "12:50", "上海", "18:40", "￥553 有票", "￥933 有票", "￥1748 还有10张"]],
            title="Skill Integration Activity 3: the two sets of train schedules from Beijing to Shanghai (the book’s tables, as printed; 6:36 to 12:40 is the morning set and 12:00 to 12:50 the early-afternoon set)")
HINTS = table(["成为", "省内", "通", "实现", "随着"], [["Hint: 换成, 分成, 变化, 变成 (become)", "Hint: 内 is the opposite of 外 (within the province)", "Hint: 交通; 101 号高速公路通旧金山 (lead to, open to traffic)", "实 means “reality”, 现 “materialize” (achieve; e.g. 她实现了去北京上大学的计划)", "Hints: 随时, 随身带, 随便 (along with)"]],
              title="Skill Integration Activity 2 A: guess the meanings (the book’s hints; the meanings in the brackets are mine)")
RPT2 = [("记者", "请问现在中国有几个省实现了省内市市通高铁？", "How many provinces in China have achieved high-speed rail in every city?"), ("官员", "福建在二零一八年第一个实现了，然后山东、河南等七个省也在二零二零年实现了。", "Fujian was the first, in 2018, and then Shandong, Henan and seven other provinces did it in 2020. (sample dialog, mine)"), ("记者", "在山东坐高铁很方便吗？", "Is it convenient to take the high-speed rail in Shandong?"), ("官员", "很方便。从青岛去东部的城市，一个小时以内就能到。", "Very. From Qingdao you can reach the eastern cities in under an hour."),
        ("记者", "高铁站还提供什么服务？", "What other services do the stations provide?"), ("官员", "旅客可以吃，住，购物，玩儿，也可以订旅游景点的门票和各地的酒店。", "Passengers can eat, stay, shop and play, and can also book tickets for tourist attractions and hotels everywhere.")]
L7 = lesson(
    "Lesson 19 Presentation 3 skill integration: every city on the high-speed rail, and the Beijing–Shanghai schedules",
    "市市通高铁 · 福建 山东 · 车次时刻表 · 记者与官员",
    requires=[],
    cards=[
        card("Skill Integration Activity 2 (Reading, Speaking and Writing): 市市通高铁",
             "A. Pair up and guess what the following expressions mean: 成为, 省内, 通, 实现, 随着. B. Read the news report, then mark the statements as True or False. C. Discuss your answers with your partner and translate the underlined sentences into English. D. With your partner create a dialog between a reporter and a transportation department official in China, using the information in the report; act it out for the class. The report (the book writes the years and numbers as digits):",
             tables=[HINTS], examples=[D(z, e) for z, e in zip(NEWS, NEWS_E)]),
        card("The statements and my key", "The five statements are the book’s; the keys are mine.", examples=[D(z, e) for z, e in TFN]),
        card("A dialog between a reporter and an official (my sample for Step D)", "The book leaves the five turns blank.", examples=dlg(RPT2)),
        card("Skill Integration Activity 3 (Reading, Speaking and Writing): choosing a train",
             "A. You and a colleague are going from Beijing to Shanghai tomorrow on a business trip. Examine the two train schedules (one train leaves early in the morning and the other in the early afternoon) and decide which train you’d like to take. B. Pair up and share the details of your train schedule with your partner, who is your traveling companion; try to convince them to accept your choice by considering the time, price, seats, weather, nature of your business and so on. C. Share your final choice with the class and explain why. (A picture, not included.) The schedules (as printed; 有票 = tickets available, 无票 = sold out, 还有 N 张 = N tickets left):",
             tables=[SCH]),
    ],
    exercises=[
        M("Which province was the first to have high-speed rail in every city?", "Fujian", ["Shandong", "Henan", "Sichuan"], "福建成为中国第一个市市通高铁的省."),
        M("In which year did Fujian achieve it?", "2018", ["2020", "2008", "2015"], "二零一八年."),
        M("How many provinces were counted by 2020?", "Eight", ["Two", "Seventeen", "Thirty-one"], "福建 + 七个省."),
        M("How many people does Shandong have?", "Over 100 million", ["Over 10 million", "Over 1 million", "Over 1 billion"], "一亿多人口."),
        M("How long did the farthest trip between two cities in Shandong once take by ordinary train?", "More than ten hours", ["About one hour", "Three hours", "Half an hour"], "十多个小时."),
        M("What is Qingdao to Shandong?", "The second-largest city", ["The capital", "The smallest city", "A village"], "是山东第二大城市."),
        M("What can passengers do at some stations?", "Eat, stay, shop, play and book tickets and hotels", ["Only wait", "Only buy tickets", "Only eat"], "旅客可以吃，住，购物，玩儿."),
        M("On the schedule, which train from Beijing leaves at 7:00?", "G5", ["G131", "G9", "G107"], "G5 北京 7:00."),
        M("Which morning train is quickest (my own subtraction)?", "G5, 7:00 to 11:40", ["G131, 6:36 to 12:40", "G143, 7:20 to 13:08", "G107, 7:50 to 13:12"], "11:40 − 7:00 = 4:40."),
        M("On the schedule, which business-class seats are sold out on G143?", "无票", ["还有7张", "有票", "还有9张"], "G143 商务座 ￥1748 无票."),
        F("福建成为中国第一个市市___高铁的省。", "通", PART, "市市通高铁."),
        F("旅客也可以订旅游景点的门票，以及各地的酒___。", "店", PART, "酒店: hotel."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
CTX3 = [("在中国坐高铁怎么订票、取票？", "1. How do you book and pick up tickets for the high-speed rail in China?"), ("中国一些大城市的高铁站是什么样子？", "2. What do the high-speed rail stations in some big Chinese cities look like?"), ("如果列车途中减速，列车长会说什么？", "3. If the train slows down on the way, what will the conductor say?"), ("坐在高铁上感觉怎么样？", "4. How does it feel to ride on the high-speed rail?")]
FACE = table(["表达", "意思 (mine; the book asks you to match each with a picture)"],
             [["刷脸进站", "enter the station by face scan"], ["对准镜头", "face the camera / line up with the lens"], ["比对", "to compare (match) the face with the record"], ["输入", "to enter (type in) information"], ["临时身份证", "temporary ID card"]],
             title="Using Chinese in Context Activity 2 A: the expressions (the pictures are not included)", say=[0])
TRAV = [("你（中文）", "我的这位同事说，你不需要车票，可以直接刷脸进站。", "Sample interpretation into Chinese (mine): my colleague says you don’t need a ticket and can enter the station by face scan."), ("你同事", "对，你只要站在机器前面，对准镜头，机器比对以后，你就可以进站了。", "The colleague (sample, mine): yes, just stand in front of the machine and face the camera, and once it matches your face you can enter."),
        ("你（中文）", "她说她没有中国的身份证，只带了护照。", "Interpretation (mine): she says she has no Chinese ID and only brought her passport."), ("你同事", "没关系，她可以把护照放在机器上扫一下，输入号码，也可以去人工窗口办一张临时身份证。", "The colleague (sample, mine): no problem, she can scan her passport on the machine and enter the number, or go to the staffed window for a temporary ID.")]
GREEN1 = "六四五一次列车停驶。二零一九年一月五日，最后一班六四五一次列车从北京站开出。因为列车是绿色的，人们把它叫做绿皮火车。这班绿皮火车运行了几十年，是从北京去天津最便宜的一趟火车，一张票只有六块多钱。绿皮火车一方面便宜，另一方面也提供了一个体验老日子的机会，所以平时虽然坐不满，但也总是有人坐。今天，列车上坐得满满的，很多人是铁路爱好者。他们不停地拍照片，还有人留下了眼泪。据说，六四五一次列车最早是给上下班的铁路职工坐的，用的是最简易的车厢，铁路职工乘坐不需要买票。后来老百姓也可以坐了，由于票价便宜，坐的老百姓越来越多。但现在的生活和以前不一样了，出行的时候，大家不是开车就是坐高铁或快车，所以绿皮火车就不太需要了。"
GREEN1_E = "Reporter A: Train 6451 stops running. On January 5, 2019, the last Train 6451 left Beijing Station. Because the train is green, people call it the “green-skin train”. This green train ran for decades and was the cheapest train from Beijing to Tianjin, a ticket costing only a little over six yuan. The green train was on one hand cheap, and on the other it offered a chance to experience the old days, so although usually not full, there were always people on it. Today the train was packed, and many were railway enthusiasts. They took photos non-stop, and some even shed tears. It is said that Train 6451 was originally for railway staff commuting to and from work, used the simplest carriages, and railway staff did not need tickets. Later ordinary people could ride, and because the fare was cheap, more and more ordinary people rode it. But life now is different from before; when going out people either drive or take the high-speed rail or a fast train, so the green train was no longer much needed. (the book writes the numbers as digits and counts 288 characters)"
GREEN2 = "六四五一次列车今天“退休”。今天，走进最后一班六四五一次的绿皮车厢的，是背着大包小包、抱着孩子的乘客，还有喜欢绿皮车慢时光的车迷们。十八时零一分，六四五一次从北京站慢慢开动，坐在绿皮车内望着窗外，只见路上车水马龙，而车厢内却有一份宁静。列车员告诉记者，六四五一次列车的乘客主要往返于北京和廊坊之间。特别是到了每周五，经常找不到座位。有的人在北京工作、廊坊买房，工作日住在北京，周末回廊坊休假。从北京站到廊坊北七十四公里，行驶一小时十三分钟，四元的票价可以说性价比非常高，为百姓出行提供了方便。但是，这趟车的茶炉、暖气都是靠烧煤的，对环境很不好，而且它车速慢。地铁开通以后，人们都更喜欢坐地铁。所以这趟绿皮车就从今天起停驶了。"
GREEN2_E = "Reporter B: Train 6451 “retires” today. Today those who walked into the carriages of the last Train 6451 were passengers carrying big and small bags and holding children, and also train fans who love the slow time of the green train. At 18:01 Train 6451 pulled slowly out of Beijing Station; sitting inside looking out the window you saw only a stream of cars and horses on the road, while inside the carriage there was a calm. The train attendant told reporters that the passengers of Train 6451 mainly travel back and forth between Beijing and Langfang, especially on Fridays when seats are often hard to find. Some people work in Beijing and buy a home in Langfang, living in Beijing on workdays and returning to Langfang for the weekend. From Beijing Station to Langfang North is 74 kilometers, taking 1 hour 13 minutes, and a 4-yuan fare can be called very good value, providing convenience for ordinary people. But the tea boiler and the heating on this train both ran on burning coal, which is bad for the environment, and it is slow. After the subway opened people liked the subway better, so this green train stopped running from today. (the book writes the numbers as digits, glosses 廊坊 as Lángfāng and 煤 as méi, coal, and counts 290 characters)"
GREENT = table(["", "记者A", "记者B"],
               [["什么事情", "六四五一次绿皮火车停驶", "六四五一次列车“退休”"], ["今天的情况", "最后一班，坐得满满的，很多人是铁路爱好者，不停地拍照片，有人流泪", "最后一班，乘客背着大包小包、抱着孩子，还有车迷，十八时零一分开出"], ["过去的情况", "最早是给铁路职工上下班坐的，后来老百姓也能坐，票价只有六块多钱", "主要往返于北京和廊坊之间，周五常常找不到座位，四元的票价性价比很高"], ["为什么会有今天事情", "现在大家不是开车就是坐高铁或快车，不太需要绿皮火车了", "烧煤对环境不好，车速慢，地铁开通后人们更喜欢坐地铁"]],
               title="Using Chinese in Context Activity 3 B: the table the two reporters complete (blank in the book; my fill)", say=[0, 1, 2])
L8 = lesson(
    "Lesson 19 Presentation 3 using Chinese in context: face-scan entry and the last green train",
    "刷脸进站 · 两方口译 · 六四五一次绿皮火车停驶",
    requires=[],
    cards=[
        card("Using Chinese in Context Activity 1 (Reading and Speaking)",
             "Pair up and take turns answering the questions. Provide as many details as possible using two or three sentences. When you have finished, switch roles and repeat. (A photograph, not included.)",
             examples=[D(z, e) for z, e in CTX3]),
        card("Using Chinese in Context Activity 2 (Reading, Listening, Writing and Speaking)",
             "A. You and one of your Chinese colleagues have just arrived at the train station to take a high-speed train from Shanghai to Beijing. Your colleague tells you that you don’t need tickets to check in. Read the following expressions and guess what each means by matching it with one of the five images (not included). B. An elderly woman comes to your colleague and asks for help; listen and write your notes in the table 关于 / 怎么做 (怎么进站; 没带身份证怎么办). (Audio, not included.) C. Two-way interpretation: a foreign tourist who speaks only English asks your colleague, who speaks only Chinese, for help, and you are the interpreter. Discuss with your partner how your colleague would answer her questions and how you would interpret. The book prints only the traveler’s English lines: 1. “I booked my ticket online. Do you know how to check in?” 2. “But I don’t have a Chinese ID, and I only have my passport with me.” 3. “Thank you! This is my first time taking a high-speed train. At such a high speed, I wonder if the train can run very smoothly.” 4. “How about their services. Will I have access to the internet?” 5. “That’s good to hear. How about food? What drinks do they have?” My sample interpretation for the first two:",
             tables=[FACE], examples=dlg(TRAV)),
        card("Using Chinese in Context Activity 3 (Reading, Speaking, Listening and Writing)",
             "You are a reporter writing a special report for the International Journal of Culture and Society about the people and the development of the transportation system in Beijing. You learn about an event for an old-fashioned green train, and you and a colleague each do the following. A. Reporter A reads piece A and Reporter B reads piece B and each takes notes. B. After both reporters are done reading, share what you read with each other and complete the table (什么事情, 今天的情况, 过去的情况, 为什么会有今天事情). C. Together write a brief report based on the information in B. D. Report orally to the class. The two pieces (the book’s counts: 288 and 290 characters) and my filled table:",
             examples=[D(GREEN1, GREEN1_E), D(GREEN2, GREEN2_E)], tables=[GREENT]),
    ],
    exercises=[
        M("What does 刷脸进站 mean?", "Entering the station by face scan", ["Washing your face", "Buying a ticket", "Showing a passport only"], "刷脸进站."),
        M("What is a 临时身份证?", "A temporary ID card", ["A train ticket", "A passport", "A bank card"], "临时身份证."),
        M("Why is the green train called 绿皮火车?", "Because the train is green", ["Because it is cheap", "Because it carries vegetables", "Because it is new"], "因为列车是绿色的."),
        M("When did the last Train 6451 leave Beijing Station?", "January 5, 2019", ["January 5, 2009", "October 12, 2003", "May 1, 2021"], "二零一九年一月五日."),
        M("How much did a ticket cost, according to Reporter A?", "A little over six yuan", ["Sixty yuan", "Six hundred yuan", "It was free"], "一张票只有六块多钱."),
        M("Who rode the train at first?", "Railway staff commuting to work", ["Tourists", "Soldiers", "Students"], "最早是给上下班的铁路职工坐的."),
        M("Between which two places do most passengers travel, according to Reporter B?", "Beijing and Langfang", ["Beijing and Shanghai", "Tianjin and Hebei", "Langfang and Xi’an"], "往返于北京和廊坊之间."),
        M("How long does the trip from Beijing Station to Langfang North take?", "One hour thirteen minutes", ["Thirteen hours", "Seventy-four minutes only", "Four hours"], "行驶一小时十三分钟."),
        M("Why did the train stop running according to Reporter B?", "Burning coal is bad for the environment and it is slow; the subway opened", ["It was too new", "It had no passengers", "A strike"], "烧煤，车速慢，地铁开通."),
        M("Why is the green train no longer much needed, according to Reporter A?", "People now drive or take the high-speed rail or fast trains", ["Nobody likes green", "It is too fast", "It is too expensive"], "大家不是开车就是坐高铁或快车."),
        F("这班绿皮火车是从北京去天津最便___的一趟火车。", "宜", PART, "便宜: cheap."),
        F("坐在绿皮车内望着窗外，只见路上车水马___。", "龙", PART, "车水马龙: heavy traffic."),
    ],
)

# ------------------------------------------------------------------ 9. Area Studies + vocabulary
AS1 = ["China’s transport infrastructure has been in the process of massive upgrades for the past few decades. For example, the annual transport volume of cargo has increased from 130.6 billion tons in 2000 to 543.4 billion tons in 2019. Rail plays a very important role in China’s transportation system. As of 2020, China’s railway mileage reached 141,400 kilometers, 36,000 kilometers of which are high-speed railways, the most in the world.",
       "By 2035, according to plan, the national railway network will have an operating mileage of over 200,000 kilometers, including about 70,000 kilometers of high-speed rail. Cities with populations over 200,000 (336 cities) will be accessible by railways, and cities with populations over 500,000 (322 cities) will be accessible by high-speed rail.",
       "Over the past 10 years, the annual growth rate of air travel has reached 14%. In 2019, China’s airlines transported 660 million passengers, a year-on-year increase of 7.9%, and cargo and mail transport volume was 7.5 million tons, a year-on-year increase of 1.9%. At the end of 2019, China’s airlines have 5,155 domestic and international routes, the fleet size has reached 3,818 vehicles and the number of airports has reached 238. The newly built Beijing Daxing International Airport will soon become the world’s busiest airport.",
       "China’s waterways account for 1.56% of passenger transport volume, and 13.8% of China’s freight transport volume. There are 2007 coastal ports with berths of 10,000 tons and above. China’s merchant fleet ranks first in the world. Since 2005 China’s merchant shipbuilding capacity has been the largest in the world. In 2019, China’s shipbuilding industry completed 36.72 million deadweight tons, and export ships accounted for 92.1% of the total.",
       "On December 21, 1984, China’s first expressway broke ground; the Shanghai-Jiading Expressway was 20.5 kilometers long. On September 1, 1990, Shenyang-Dalian Expressway was completed. With a length of 375 kilometers, it was the longest expressway in the country at the time. In 2017, the Beijing-Xinjiang Expressway was connected, cutting across the Gobi Desert with a total mileage of 2,768 kilometers; it is the longest highway in the world. In 2019, the total mileage of China’s highways was 4,846,500 kilometers. The national expressway network, the largest in the world, now consists of 7 capital radiation lines, 9 north-south vertical lines and 18 east-west horizontal lines."]
L9 = lesson(
    "Lesson 19 Area Studies: China’s fast-growing transportation system",
    "铁路 · 航空 · 水运 · 高速公路",
    requires=[],
    cards=[
        card("Area Studies: China’s Fast-Growing Transportation System",
             "The book’s English reading, in five paragraphs (with pictures of a high-speed train, Beijing Daxing International Airport and a highway, not included). Its references are wikipedia.org, finance.ifeng.com, china.chinadaily.com.cn and sourcedb.igsnrr.cas.cn.\n\n" + "\n\n".join(AS1)),
    ],
    exercises=[
        M("How many kilometers of railway did China have as of 2020?", "141,400", ["14,140", "36,000", "200,000"], "China’s railway mileage reached 141,400 kilometers."),
        M("How many kilometers of that are high-speed rail?", "36,000", ["70,000", "141,400", "3,600"], "36,000 kilometers of which are high-speed."),
        M("What is the plan for high-speed rail by 2035?", "About 70,000 kilometers", ["About 7,000 kilometers", "About 200,000 kilometers", "About 36,000 kilometers"], "about 70,000 kilometers of high-speed rail."),
        M("Which cities will be accessible by high-speed rail by 2035?", "Those with populations over 500,000", ["Those over 200,000", "Those over 50,000", "Only capitals"], "over 500,000 (322 cities)."),
        M("How many passengers did China’s airlines carry in 2019?", "660 million", ["66 million", "6.6 billion", "7.5 million"], "660 million passengers."),
        M("How many airports did China have at the end of 2019?", "238", ["38", "2,380", "3,818"], "number of airports reached 238."),
        M("Which airport will soon be the world’s busiest?", "Beijing Daxing International Airport", ["Pudong", "Hong Kong", "Guangzhou"], "newly built Beijing Daxing International Airport."),
        M("What share of China’s freight is carried on waterways?", "13.8%", ["1.56%", "92.1%", "7.9%"], "13.8% of freight transport volume."),
        M("Which is the longest highway in the world, according to the text?", "The Beijing-Xinjiang Expressway", ["The Shanghai-Jiading Expressway", "The Shenyang-Dalian Expressway", "The Lhasa Expressway"], "2,768 kilometers."),
        M("When did China’s first expressway break ground?", "December 21, 1984", ["September 1, 1990", "2017", "2005"], "Shanghai-Jiading Expressway."),
        M("How long was the Shanghai-Jiading Expressway?", "20.5 kilometers", ["375 kilometers", "2,768 kilometers", "4,846,500 kilometers"], "20.5 kilometers long."),
    ],
)
L10 = vocab_lesson("Lesson 19 Presentation 3 vocabulary", "36 words from the book’s Presentation 3 list",
                   "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

UNIT = unit("第十九课 Presentation 3: 乘坐高铁, 最近, 才, 向/往/对, 由于, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
