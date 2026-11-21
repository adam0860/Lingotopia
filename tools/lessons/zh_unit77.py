"""Unit 77: Lesson 25 (Smart Life), Presentation 2: the homestay and short-term rental passage with its activities, the superlatives 特别 and 最, complex instructions with 接下来,
另外 and 还有, the skill-integration tasks (the Shanghai short-term rental blog post and the travel article about homestays in America), the using-Chinese tasks and the vocabulary list.
Audio, pictures and websites are not included; numbers the book writes as digits are spelled out; answers that the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l25_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("铺好瑜伽垫", 0, "pu1"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('不得不', 1, 'de2'), ('记得', 1, 'de5'), ('随着手机', 1, 'zhe5'), ('暖和自', 1, 'he2'), ('教了', 0, 'jiao1'), ('还教了', 0, 'hai2'), ('好学生', 0, 'hao3')):
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

# ------------------------------------------------------------------ 1. presentation 2
P2 = [("随着手机支付和短租平台的出现，民宿和短租房渐渐成了新的旅行住宿方式，特别受到年轻人的欢迎。", "Paragraph 1: With the appearance of mobile payment and short-term rental platforms, homestays and short-term rentals have gradually become a new way to lodge when traveling, and are especially welcomed by young people. (translations in this card are mine)"),
      ("很多年轻人都在手机上安装了民宿、短租平台的应用软件。旅行前，只要动动手指，滑动一下页面，看看照片和用户评价，很快就可以选择到满意的民宿。接下来，就是确认住宿时间和个人信息，然后用手机付款，基本上就是“一键完成”。", "Paragraph 2: Many young people have installed homestay and short-term rental platform apps on their phones. Before traveling, they only need to move their fingers, swipe the page, and look at the photos and user reviews, and they can soon choose a homestay they are satisfied with. Next comes confirming the dates and personal information and then paying by phone; basically it is “done with one key.”"),
      ("民宿和短租屋的价格比较便宜，是年轻人喜欢住的主要原因。另外，和一般的宾馆相比，民宿和短租房更有特色，有家的感觉，可以自己买菜做饭，也可以跟房主聊天。还有，民宿和短租屋的房客来自不同的国家、不同的地区，可以结交到很多新朋友，了解不同的文化和习俗。", "Paragraph 3: The comparatively low price of homestays and short-term rental houses is the main reason young people like to stay in them. In addition, compared with ordinary guesthouses, homestays and short-term rentals have more character and a feeling of home; you can buy groceries and cook yourself, and you can also chat with the host. Also, the guests in homestays and short-term rentals come from different countries and different regions, so you can make many new friends and learn about different cultures and customs."),
      ("旅行中大家每天可以发送照片，分享自己的经历，或是在平台上给房主打分。这样的旅行更有特点，会留下更多、更美好的回忆。", "Paragraph 4: During the trip everyone can send photos every day, share their experiences, or rate the host on the platform. This kind of trip has more distinctive features and will leave more and more beautiful memories.")]
KEY1 = [("手机支付和短租平台的出现", "A1B1 (mine): the appearance of mobile payment and short-term rental platforms"),
        ("先安装应用，滑动页面看照片和评价，选择满意的民宿，然后确认时间和个人信息，最后用手机付款。", "A1B2 (mine): install the app, swipe the pages to look at photos and reviews, choose a satisfying homestay, confirm the dates and personal information, and finally pay by phone."),
        ("价格便宜，更有特色，房客来自不同的地方。", "A1B3 (mine): the price is low, it has more character, and the guests come from different places."),
        ("发送照片，分享经历，给房主打分，留下更美好的回忆。", "A1B4 (mine): sending photos, sharing experiences and rating the host leave more beautiful memories.")]
WORDS = table(["房主", "短租房"], [["房东", "房间"], ["房客", "房子"], ["房型", "房价"], ["房租", "客房"], ["书房", "厨房"]],
              title="Activity 2: words containing 房 (my list; the book’s two columns, 房主 and 短租房, are blank)", say=[0, 1])
S3 = [("随着中国高铁的出现，人们出行越来越方便了。", "1. With the appearance of China’s high-speed rail, getting around has become more and more convenient. (the book gives only 随着中国高铁的出现，; my completion)"),
      ("这家民宿的早餐特别受到游客的欢迎。", "2. The breakfast at this homestay is especially welcomed by tourists. (the book gives only 特别受到游客的欢迎; my completion)"),
      ("住民宿可以自己做饭，还可以跟房主聊天。这样的住宿方式更方便，更舒服。", "3. In a homestay you can cook for yourself and chat with the host. This kind of lodging is more convenient and more comfortable. (my completion before the book’s second sentence)"),
      ("只要在手机上输入旅行的地方和时间，你很快就可以找到一家民宿。", "4. As long as you enter the place and dates of your trip on your phone, you can find a homestay very quickly. (my completion of the book’s 只要……，你很快就可以找到一家民宿)"),
      ("你得先在短租平台上找好想要租的民宿。接下来，就是确认住宿时间和个人信息。", "5. You have to find the homestay you want to rent on a short-term rental platform first. Next comes confirming the dates and personal information. (my completion of the book’s 先在短租平台上找好想要租的民宿。接下来，就是……)"),
      ("价格便宜是我选择这家民宿的主要原因。", "6. The low price is the main reason I chose this homestay. (my completion of the book’s ……是我选择这家民宿的主要原因)")]
L1 = lesson(
    "Lesson 25 Presentation 2: homestays and short-term rentals",
    "民宿和短租房 · 动动手指 滑动页面 · 一键完成 · 价格比较便宜 · 房主 房客 · 分享经历 给房主打分",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. Where do you like to stay when you travel and why? B. How do you book your stay? C. What apps do you use to book accommodations and why? (Four pictures are not included.)"),
        card("Presentation 2: 民宿和短租房", "The book also prints the passage in traditional characters. The translations are mine.", examples=[D(z, e) for z, e in P2]),
        card("Activity 1 (Listening)",
             "A. Global Listening: Listen to Presentation 2 once through and answer the questions. 1. What is the latest trend mentioned here? 2. What are the three things about this trend that the passage discusses? B. Detailed Listening: Listen to Presentation 2 a second time and answer the questions. 1. What makes this new trend possible? 2. In detail, what are the steps young people take to use the apps mentioned here? 3. What are three reasons for their popularity among young people? 4. Why do these apps make traveling more memorable? (Audio, not included; my answers from the text:)",
             examples=[D(z, e) for z, e in KEY1]),
        card("Activity 2 (Reading and Writing)",
             "A. Fill in the boxes on the left with words containing 房, while a partner fills in the boxes on the right. Use a dictionary if you need to. B. Share your words with your partner and fill in the remaining boxes. C. Post your work on a website to share with the class (the website is not used here).",
             tables=[WORDS]),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Complete the first three sentences with your own words, while a partner completes the last three. The book prints: 1. 随着中国高铁的出现， 2. 特别受到游客的欢迎。 3. ……。这样的住宿方式更方便，更舒服。 4. 只要……，你很快就可以找到一家民宿。 5. 先在短租平台上找好想要租的民宿。接下来，就是…… 6. ……是我选择这家民宿的主要原因。 B. Read your sentences to your partner. My completions:",
             examples=[D(z, e) for z, e in S3]),
    ],
    exercises=[
        M("What is the new way of lodging in Presentation 2?", "Homestays and short-term rentals", ["Five-star hotels", "Camping", "Youth hostels only"], "民宿和短租房."),
        M("Who especially welcomes them?", "Young people", ["Old people", "Hotel owners", "Children"], "特别受到年轻人的欢迎."),
        M("What makes the new trend possible?", "Mobile payment and short-term rental platforms", ["Cheap flights", "High-speed rail", "Takeout"], "手机支付和短租平台."),
        M("What does “一键完成” mean?", "Done with one key", ["Locked with a key", "A new password", "A free room"], "一键: one key."),
        M("What is the main reason young people like to stay in them?", "The comparatively cheap price", ["The free breakfast", "The big pool", "The tour guides"], "价格比较便宜."),
        M("What can you do in a homestay, unlike an ordinary guesthouse?", "Buy groceries, cook and chat with the host", ["Order room service", "Use a gym", "Park for free"], "自己买菜做饭，也可以跟房主聊天."),
        M("Who are the guests in these places?", "People from different countries and regions", ["Only locals", "Only students", "Only families"], "来自不同的国家、不同的地区."),
        M("What can travelers do on the platform at the end of the trip?", "Rate the host", ["Cook for the host", "Buy tickets", "Change rooms"], "给房主打分."),
        M("Which word means “homeowner”?", "房主", ["房客", "房型", "房价"], "房主."),
        M("Which word means “tenant”?", "房客", ["房主", "房东", "房租"], "房客."),
        F("旅行前，只要动动手___，滑动一下页面，就可以选择到满意的民宿。", "指", PART, "手指: finger."),
        F("___着手机支付和短租平台的出现，民宿渐渐成了新的住宿方式。", "随", PART, "随着: along with."),
        F("这样的旅行更有特点，会留下更多、更美好的___忆。", "回", PART, "回忆: memories."),
    ],
)

# ------------------------------------------------------------------ 2. activities 4-6
SUM4 = [("民宿价格便宜，是我们选择短租的主要原因。另外，住在民宿里可以自己做饭，也可以跟房主聊天。还有，除了认识房主以外，还可以认识来自不同地方的房客。", "Sample summary (mine, using 是…的主要原因, 另外, 还有 and 除了): The low price of homestays is the main reason we choose short-term rentals. In addition, you can cook for yourself in a homestay and chat with the host. Also, besides getting to know the host, you can meet guests from different places.")]
FILL5 = [("在手机上完成“爱彼迎”的民宿预订和旅游短租很简单。你需要先在手机上下载一个“爱彼迎”的应用，再打开应用的页面，输入要旅行的目的地，就可以看到很多民宿的照片。然后看看其他房客的评价，基本上可以决定选哪一家民宿。接下来，就是确定住几天，你可以查看可订日历。输入个人信息，最后选择手机付款就可以了。", "Completed passage (my key: 先, 再, 然后, 接下来, 最后): Completing a homestay booking and a short-term rental on Airbnb on your phone is very simple. First you need to download an Airbnb app on your phone, then open the app’s page and enter the destination, and you can see photos of many homestays. Then look at other guests’ reviews, and you can basically decide which homestay to choose. Next comes deciding how many days you will stay; you can check the available-dates calendar. Enter your personal information, and finally choose to pay by phone. (the book writes “爱比迎” in this passage and “爱彼迎” elsewhere; the usual name 爱彼迎 is used)")]
FLOW = [("下载应用，再打开页面，输入目的地，然后看照片和评价，接下来确定住几天，输入个人信息，最后用手机付款。", "Flowchart 1 (mine): download the app → open the page → enter the destination → look at photos and reviews → decide the number of days → enter personal information → pay by phone."),
        ("安装应用，滑动页面看照片和评价，选择满意的民宿，接下来确认时间和个人信息，然后用手机付款，一键完成。", "Flowchart 2 (mine, for the second paragraph of Presentation 2): install the app → swipe the pages to see photos and reviews → choose a satisfying homestay → confirm time and personal information → pay by phone → done with one key.")]
Q6 = [("我们班有多少同学使用过民宿和短租房应用或平台？", "1. How many students in our class have used homestay and short-term rental apps or platforms?"),
      ("同学们常使用的民宿和短租平台应用有哪些？", "2. Which homestay and short-term rental platform apps do the students often use?"),
      ("同学们选择民宿和短租平台应用的原因有哪些？", "3. What are the reasons the students choose homestay and short-term rental platform apps?")]
L2 = lesson(
    "Lesson 25 Presentation 2 activities: reasons, a booking passage and an interview",
    "是…的主要原因 · 先 再 然后 接下来 最后 · 爱彼迎 · 民宿和短租平台应用 · 流程图",
    requires=[],
    cards=[
        card("Activity 4 (Listening, Writing and Speaking)",
             "A. Listen to three speakers discuss why they like Bed & Breakfasts and other short-term rentals, then complete the table below in Chinese: Speaker 1, 2, 3 | Reasons. (The three pictures and the audio are not included, and the speakers’ script is not in the book.) B. Form groups of three. Read your answers to each other, then take turns reading the script aloud so that each member reads one of the speaker’s parts. C. Summarize why the speakers choose Airbnb and other short-term rentals. Write five to six sentences that use 是…的主要原因, 另外, 还有 and 除了. Then read your summary to your teammates, get their feedback, and make any necessary corrections or improvements. A sample summary (mine):",
             examples=[D(z, e) for z, e in SUM4]),
        card("Activity 5 (Reading, Writing, Speaking and Listening)",
             "A. Read the following passage and fill in the blanks with the correct words from the word pool: 接下来, 然后, 先, 最后, 再. B. Compare answers with a partner. C. Create a flowchart of the above passage in Chinese characters, while a partner does the same for the second paragraph of Presentation 2. Make sure your flowchart has clear steps. D. Show your chart to your partner and explain each step in Chinese. The book gives no key; the completed passage and the two flowcharts are mine:",
             examples=[D(z, e) for z, e in FILL5 + FLOW]),
        card("Activity 6 (Reading, Speaking, Listening and Writing)",
             "A. Form groups of three. Interview two classmates in Chinese about their use of Airbnb and other short-term rental apps. Take notes in the table below: 同学 (1) and 同学 (2), with the rows 民宿/短租平台应用名称, 使用的原因, 怎么使用该应用, 使用应用做了什么. B. Exchange survey information with your teammates, then work together to answer the following questions in Chinese characters. (Two pictures are not included.)",
             examples=[D(z, e) for z, e in Q6]),
    ],
    exercises=[
        M("Which word fits “你需要___在手机上下载一个应用”?", "先", ["再", "最后", "接下来"], "先 begins the sequence."),
        M("Which word fits “___打开应用的页面，输入要旅行的目的地”?", "再", ["先", "最后", "然后"], "先…再…."),
        M("Which word fits “___，就是确定住几天”?", "接下来", ["最后", "先", "再"], "接下来，就是…."),
        M("Which word fits “输入个人信息，___选择手机付款”?", "最后", ["先", "再", "接下来"], "最后: finally."),
        M("What can you see after entering the destination?", "Photos of many homestays", ["The bill", "The weather", "The host"], "可以看到很多民宿的照片."),
        M("What can you check when deciding how many days to stay?", "The available-dates calendar", ["The menu", "The map", "The invoice"], "可订日历."),
        M("What are the sentence patterns to use in Activity 4C?", "是…的主要原因, 另外, 还有, 除了", ["能…吗, 不是…吗", "先…然后…最后", "又…又…"], "Activity 4C."),
        M("Who do you interview in Activity 6?", "Two classmates", ["The teacher", "A host", "A hotel manager"], "同学 (1) and 同学 (2)."),
        F("你需要先在手机上下___一个应用。", "载", PART, "下载: download."),
        F("输入个人信息，最___选择手机付款就可以了。", "后", PART, "最后: finally."),
    ],
)

# ------------------------------------------------------------------ 3. 特别 and 最
SUP = table(["结构", "用法"], [["aspect in common + 最重要的是… / 特别是… + 人/事 + elaboration", "singles out the most important aspect or the extreme example, then elaborates"], ["aspect in common + 人/事 + 最受欢迎的是… / 特别受欢迎的是… + elaboration", "singles out the most popular thing or person, then elaborates"]],
            title="Superlatives 特别 and 最")
SE1 = [("随着手机支付和短租平台的出现，民宿和短租房渐渐成了新的旅行住宿方式，特别受到年轻人的欢迎。", "1. With the appearance of mobile payment and short-term rental platforms, homestays and short-term rentals have gradually become a new way to lodge when traveling, especially welcomed by young people."),
       ("以前在中国，大家出行主要靠公交车和出租车。现在有了更方便的选择，最受欢迎的就是“滴滴出行”。", "2. In the past in China, everyone traveled mainly by bus and taxi. Now there are more convenient choices, and the most popular is “Didi Chuxing.” (the book marks this as from Presentation 3)")]
SE2 = [("夏季的东北，农家菜特别受欢迎，地道东北味，外地吃不到。最受欢迎的一道菜就是“三烀一蒸”。这道菜少油，少盐，是非常健康的菜。", "1. In summer in the Northeast, farmhouse dishes are especially popular, with an authentic Northeastern taste you can’t get elsewhere. The most popular dish is “three stews and one steam.” This dish has little oil and little salt and is a very healthy dish."),
       ("最新的小米手机有很多新的功能。最受欢迎的功能就是拍完文字照片以后，能够智能去阴影，很多上网课的大学生都爱用这个新功能。", "2. The newest Xiaomi phone has many new functions. The most popular function is that after you photograph text it can intelligently remove shadows, and many university students who take online classes love to use this new function."),
       ("对于人生，什么是重要的呢？好像有很多，比如：亲情啊，爱情啊，金钱啊或者什么东西。但是，最重要的就是人生自己，无论怎样的变化，一直拥有的就是你自己。", "3. As for life, what is important? There seem to be many things, for example: family love, romantic love, money or some such thing. But the most important is life itself; however things change, what you always have is yourself. (the book prints 人生自己 as it stands)"),
       ("春暖花开，“五一”小长假马上就要到了，喜欢旅游的朋友们要开始计划出国游了。那么到国外旅游最重要的是什么呢？出门在外最重要的是出游安全。外国游客，特别是老人、妇女较容易成为小偷的目标。大家最好结伴出游，相互照看。", "4. Spring is warm and flowers are blooming, the short May Day holiday is about to arrive, and friends who like to travel are starting to plan trips abroad. So what matters most when traveling abroad? What matters most away from home is safety while traveling. Foreign tourists, especially the elderly and women, more easily become the targets of thieves. It is best to travel in groups and look after one another. (the book prints 最要的是什么, a missing 重; written 最重要的是什么 here)"),
       ("我喜欢吃水果，草莓啊，橘子啊，苹果啊什么的，特别是热带水果。每到夏天我都特别开心，因为又可以吃到美味的热带水果啦。", "5. I like eating fruit, strawberries, oranges, apples and so on, especially tropical fruit. Every summer I am especially happy, because I can eat delicious tropical fruit again."),
       ("这次在美国旅行，吃到了很多好吃的美国饭菜！特别是第一顿饭只有五十五美金，量适中，但是味道超好！", "6. On this trip in America I ate a lot of delicious American food! Especially the first meal cost only fifty-five dollars, with a moderate portion, but the flavor was super good! (the book writes 55 in digits)")]
A1 = [("我们班同学学习都很努力，特别是班长，他除了有很多社会工作，还有一个五岁的儿子，可是每次功课都做得很好。有一次……", "A. The example: The students in our class all study very hard, especially the class monitor: besides having a lot of social work, he has a five-year-old son, but he does his homework well every time. Once… (the book labels the parts: aspect of a class, single out, elaboration; it writes 5 in digits)")]
A1B = [("城乡教育不公平一直是中国社会的一个大问题，特别是农民工子女，因为没有户口，他们不能在当地上小学，上中学，更别说参加高考了。为了让子女上学，不得不把自己大部分的工资用来请老师。", "B. The passage: Unequal education between city and countryside has always been a big problem in Chinese society, especially the children of migrant workers, who, because they have no household registration, cannot attend primary or middle school locally, let alone take the college entrance exam. To let their children go to school, parents have no choice but to spend most of their wages on hiring teachers."),
       ("这里谈的是城乡教育不公平，涉及的是城市和农村的孩子。", "1. (my answer) The broad topic is unequal education between city and countryside, concerning city and rural children."),
       ("谈的是孩子上学的机会。", "2. (my answer) The aspect discussed is children’s chances of going to school."),
       ("被特别指出来的是农民工子女。", "3. (my answer) The one singled out is the children of migrant workers."),
       ("作者说他们没有户口，不能在当地上学，父母不得不把大部分的工资用来请老师。", "4. (my answer) The author says they have no household registration and cannot attend school locally, so their parents have to spend most of their wages on hiring teachers.")]
A3S = [("在美国年轻人中，最受欢迎的是手机游戏。特别是在周末，很多人一玩就是几个小时。", "Sample for American youth (mine): Among young Americans, the most popular thing is mobile games. Especially at weekends, many people play for hours at a stretch."),
       ("在中国年轻人中，最受欢迎的是网上购物。特别是在“双十一”，很多人半夜还在买东西。", "Sample for Chinese youth (mine): Among young Chinese, the most popular thing is online shopping. Especially on Singles’ Day, many people are still shopping in the middle of the night.")]
L3 = lesson(
    "Lesson 25 Presentation 2 grammar: the superlatives 特别 and 最",
    "特别受到年轻人的欢迎 · 最受欢迎的是 · 最重要的是 · 特别是 · 三烀一蒸 · 农民工子女",
    requires=[],
    cards=[
        card("话语语法: The Superlatives 特别 and 最",
             "A. 特别 and 最 are similar to the English “especially” and “the most.” They single out something as the most extreme or quintessential example of its kind. B. These two superlatives often come at the end of a sentence, followed by elaboration, or begin a new sentence that elaborates the preceding one. Commonly used phrases are “最重要的是…,” “特别是…,” “最受欢迎的是…” and “特别受欢迎的是…”.",
             tables=[SUP], examples=[D(z, e) for z, e in SE1]),
        card("Examples with 特别 and 最", "The book’s digits are spelled out and one missing character is fixed (see example 4). The English is mine.", examples=[D(z, e) for z, e in SE2]),
        card("Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. Study the following example of 特别, then discuss it with a partner. B. Read the following passage with your partner and answer the questions in Chinese: 1. What is the broad category of people discussed here? 2. Which particular aspect of them is being discussed? 3. Who is singled out as an extreme example? 4. What does the author say to elaborate their point? C. Read your answers to the class. The book gives no key; the answers are mine.",
             examples=[D(z, e) for z, e in A1 + A1B]),
        card("Activity 2 (Speaking and Listening)",
             "A. In groups of three, choose two pictures each to talk about. Using your imagination, try to point out the most important or special information using 最重要的是…/特别是… or 最受欢迎的是…/特别受欢迎的是…. B. Pair up with a student from another group to relate your group’s information to them. (Six pictures are not included.)"),
        card("Activity 3 (Writing and Speaking)",
             "A. Write a short paragraph (five or six sentences) about popular trends among American youth, while a partner does the same for Chinese youth. Use 最重要的是… / 特别是… or 最受欢迎的是… / 特别受欢迎的是… and add as much elaborative information as you can. B. Read your paragraph to your partner, critique each other’s work, and make any necessary corrections or improvements. C. Divide the class into an American group and a Chinese group. In a table (Popular Trends in the U.S. | Popular Trends in China), compile your information to report on your respective popular trends. D. Report your findings to the class in Chinese. (Three pictures are not included.) Two sample sentences, mine:",
             examples=[D(z, e) for z, e in A3S]),
    ],
    exercises=[
        M("What do 特别 and 最 single out?", "The most extreme or quintessential example", ["A question", "A negative", "A past event"], "Superlatives."),
        M("What does 最受欢迎的是… mean?", "The most popular is…", ["The least popular is…", "Nobody likes…", "It is popular because…"], "最受欢迎."),
        M("What does 特别是… mean?", "Especially…", ["Not especially…", "Only…", "Because…"], "特别是."),
        M("Which is the commonly used phrase for “what matters most”?", "最重要的是…", ["最受欢迎的是…", "特别是…", "特别受欢迎的是…"], "最重要的是."),
        M("What is the most popular dish in the Northeast example?", "三烀一蒸", ["麻婆豆腐", "北京烤鸭", "饺子"], "最受欢迎的一道菜就是“三烀一蒸”."),
        M("What is the most popular function of the new Xiaomi phone?", "Removing shadows from photographed text", ["Voice calls", "Games", "Maps"], "智能去阴影."),
        M("Who are singled out as easy targets for thieves?", "Foreign tourists, especially the elderly and women", ["Locals", "Children only", "Drivers"], "特别是老人、妇女."),
        M("Who is singled out in the education passage?", "The children of migrant workers", ["City students", "Teachers", "University students"], "特别是农民工子女."),
        M("What is the aspect of children discussed in the education passage?", "Their chances of going to school", ["Their food", "Their sports", "Their toys"], "不能在当地上小学，上中学."),
        F("我喜欢吃水果，___别是热带水果。", "特", PART, "特别是: especially."),
        F("最受欢迎的一道菜就是“三烀一___”。", "蒸", PART, "三烀一蒸."),
        F("这次在美国旅行，吃到了很多好吃的美国饭___！", "菜", PART, "饭菜: food."),
    ],
)

# ------------------------------------------------------------------ 4. 接下来
SEQ = table(["句式", "意思"], [["先…然后…最后", "first…then…last"], ["先…再…然后…最后", "first…then…then…last"], ["首先…接下来…然后…最后", "first…next…then…last"], ["首先…然后…接下来…最后", "first…then…next…last"], ["首先…其次…然后…最后", "first…then/second…then…last"], ["首先…其次…然后…接着…最后", "first…then/second…then…next…last"]],
            title="Complex Sequential Patterns", say=[0])
SQ0 = [("旅行前，只要动动手指，滑动一下页面，看看照片和用户评价，很快就可以选择到满意的民宿。接下来，就是确认住宿时间和个人信息，然后用手机付款，基本上就是“一键完成”。", "Examine: Before traveling, you only need to move your fingers, swipe the page and look at the photos and user reviews, and you can soon choose a satisfying homestay. Next comes confirming the dates and personal information and then paying by phone; basically it is “done with one key.”")]
SQ1 = [("学习习惯非常重要，首先要做好预习，然后专心听讲，接下来认真完成作业，最后做好复习工作。", "1. Study habits are very important: first prepare well, then listen attentively, next do your homework carefully, and finally do the review well. (the book prints 接下来/接着, either word)"),
       ("洗衣服的方法是：首先将洗衣液倒入适量的水中，接下来让衣服在水中泡上十分钟，然后用手洗或机洗，最后晾干。", "2. The way to wash clothes: first pour the detergent into a suitable amount of water, next let the clothes soak in the water for ten minutes, then wash by hand or machine, and finally hang them to dry. (the book prints 接下来/接着 and 10 in digits)"),
       ("首先我们要努力学习，其次要热爱劳动，然后坚持锻炼身体，最后才能成为一个全面发展的好学生。", "3. First we must study hard, second love labor, then keep exercising, and only finally can we become a good all-round student."),
       ("在学习中，首先要对学习充满热情，其次是要有好的学习态度，然后在学习中学会思考，最后要找到适合自己的学习方法。", "4. In studying, first you must be full of enthusiasm for it, second have a good attitude, then learn to think while studying, and finally find the study method that suits you."),
       ("我们要做一个有用的人，首先是要对自己有用，自己的事情能够自己解决，接下来是对家人有用，能够帮助家庭和家人，然后是对身边的人有用，最后是对整个社会有用。", "5. We should be useful people: first useful to ourselves, able to solve our own affairs; next useful to our family, able to help the household and relatives; then useful to the people around us; and finally useful to the whole society.")]
SQ2 = [("小明先放好自行车，接着走进教室。然后放好书包，最后等老师来上课。", "Note, example 1: Xiao Ming first parked his bicycle, then walked into the classroom, then put down his schoolbag, and finally waited for the teacher to come to class."),
       ("天气突然变了，先是刮起大风，接着乌云密布，然后响起阵阵雷声，最后大雨倾盆而下。", "Note, example 2: The weather suddenly changed: first a strong wind arose, then dark clouds gathered, then peals of thunder sounded, and finally the rain poured down."),
       ("早晨起床，首先刷牙，接着洗脸，然后吃早餐，最后出门上学。", "Note, example 3: In the morning after getting up, first brush your teeth, then wash your face, then eat breakfast, and finally go out to school.")]
A4 = [("昨天下课以后，我首先去食堂吃了午饭，接下来去图书馆做作业，然后回宿舍洗澡，最后跟朋友打了一个小时的游戏。", "After class yesterday (mine): After class yesterday I first went to the canteen for lunch, next went to the library to do homework, then went back to the dorm to shower, and finally played games with a friend for an hour."),
      ("今天早上起床以后，我首先刷牙洗脸，然后吃早饭，接下来看了一会儿手机，最后去上课。", "After getting up this morning (mine): After getting up this morning I first brushed my teeth and washed my face, then ate breakfast, next looked at my phone for a while, and finally went to class.")]
A5 = [("怎么练习瑜伽：首先找一个安静的地方，铺好瑜伽垫，然后慢慢做热身动作，接下来练习几个简单的动作，最后躺下来休息。", "Topic 1, 怎么练习瑜伽 (mine): How to practice yoga: first find a quiet place and lay out the yoga mat, then slowly do warm-up moves, next practice a few simple poses, and finally lie down and rest."),
      ("怎么学习滑雪：首先要穿好雪鞋，戴好帽子和手套，然后学习怎么站稳，接下来学习怎么转弯，最后学习怎么停下来。", "Topic 2, 怎么学习滑雪 (mine): How to learn skiing: first put on your ski boots and wear a hat and gloves, then learn how to stand steadily, next learn how to turn, and finally learn how to stop."),
      ("怎么练习举重：首先要做热身，然后选一个轻一点的重量，接下来慢慢举起来，最后放下来休息一会儿。", "Topic 3, 怎么练习举重 (mine): How to practice weightlifting: first warm up, then choose a lighter weight, next slowly lift it, and finally put it down and rest for a while.")]
L4 = lesson(
    "Lesson 25 Presentation 2 grammar: complex instructions with 接下来",
    "接下来 · 首先…接下来…然后…最后 · 首先…其次…然后…最后 · 洗衣服的方法 · 先是刮起大风 · 怎么练习瑜伽",
    requires=[],
    cards=[
        card("Complex Instructions with 接下来",
             "接下来 is similar to the English “(and) next” in a series of actions. At the beginning of a sentence, it resembles the English “moving right along” to indicate you are “moving on” from one topic to the next. Earlier in the course, you learned to give simple instructions using 先…然后…最后 or 先…再…然后…最后. The more formal version of this is 首先…接下来…然后…最后 (first…next…then…last) or 首先…然后…接下来…最后 (first…then…next…last).",
             tables=[SEQ], examples=[D(z, e) for z, e in SQ0]),
        card("Examples of the complex patterns", "The book gives 接下来/接着 in examples 1 and 2; 接下来 is written here, and 接着 works in the same place. The English is mine.", examples=[D(z, e) for z, e in SQ1]),
        card("Note: past and future events",
             "Besides their use in instructions, these patterns can also be used for sequential past or future events or actions.",
             examples=[D(z, e) for z, e in SQ2]),
        card("Activity 4 (Reading, Writing, Speaking and Listening)",
             "A. Using 首先…接下来…然后…最后 or one of its variants, write down what you did after class yesterday and after getting up this morning (昨天下课以后，… / 今天早上起床以后，…). B. Read your narration to a partner, then tell the class what your partner did in Chinese. My two sample narrations:",
             examples=[D(z, e) for z, e in A4]),
        card("Activity 5 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three and divide up the topics below: Topic 1: 怎么练习瑜伽; Topic 2: 怎么学习滑雪; Topic 3: 怎么练习举重. Using 首先…接下来…然后…最后, 首先…然后…接下来…最后 or another variant, write the instructions for your topic in Chinese characters in the table provided. B. Read your instructions to your teammates, then take notes while they read theirs. C. Report one of your teammate’s instructions to the class in Chinese so that all three sets are covered. (Three pictures are not included.) The book’s table is blank; my sample instructions:",
             examples=[D(z, e) for z, e in A5]),
    ],
    exercises=[
        M("What is 接下来 like in English?", "“(And) next” in a series of actions", ["“Because”", "“Although”", "“Unless”"], "接下来."),
        M("What does 接下来 at the start of a sentence signal?", "Moving on to the next topic", ["A reason", "A contrast", "A question"], "Moving right along."),
        M("Which is the formal version of 先…然后…最后?", "首先…接下来…然后…最后", ["先后…接下来…完", "一…二…三", "首先…最后"], "首先…接下来…."),
        M("What does 首先…其次…然后…最后 mean?", "First…then/second…then…last", ["First…last", "Not only…but also", "If…then"], "其次: second."),
        M("Which word can replace 接下来 in 首先…接下来…然后…最后?", "接着", ["因为", "可是", "虽然"], "接下来/接着."),
        M("In the washing example, how long do the clothes soak?", "Ten minutes", ["One hour", "Five minutes", "A day"], "泡上十分钟."),
        M("Can the patterns describe past events too?", "Yes, and future ones too", ["No, only instructions", "No, only the present", "No"], "Note."),
        M("Which sequence describes the storm?", "Wind, dark clouds, thunder, heavy rain", ["Rain, wind, sun", "Thunder, wind, snow", "Sun, clouds, rain"], "先是刮起大风，接着乌云密布…."),
        F("洗衣服的方法是：首先将洗衣液倒入适量的水中，接下___让衣服在水中泡上十分钟。", "来", PART, "接下来."),
        F("首先我们要努力学习，___次要热爱劳动，然后坚持锻炼身体。", "其", PART, "首先…其次…."),
    ],
)

# ------------------------------------------------------------------ 5. 另外 and 还有
AF = table(["结构", "用法"], [["另外: information + 另外, …. (还/也… )", "adds new information as an afterthought; may be followed by 还 or 也"], ["还有: …., 还有, + additional information", "adds new information; can follow a comma"], ["还有, + additional information", "begins a new sentence"]],
           title="另外 and 还有")
AFE = [("另外，和一般的宾馆相比，民宿和短租房更有特色，有家的感觉，可以自己买菜做饭，也可以跟房主聊天。", "1. In addition, compared with ordinary guesthouses, homestays and short-term rentals have more character and a feeling of home; you can buy groceries and cook yourself, and you can also chat with the host."),
       ("还有，民宿和短租屋的房客来自不同的国家、不同的地区，可以结交到很多新朋友，了解不同的文化和习俗。", "2. Also, the guests in homestays and short-term rentals come from different countries and different regions, so you can make many new friends and learn about different cultures and customs.")]
AFX = [("这个航班经常晚点。另外，他们的飞机餐也很难吃。", "1. This flight is often late. In addition, their in-flight meals are hard to eat too."),
       ("我没时间参加这个活动。另外，我也不太感兴趣。", "2. I don’t have time to attend this event. Besides, I’m not very interested either."),
       ("幼儿园提供午餐。另外，每天下午还有点心和水果。", "3. The kindergarten provides lunch. In addition, there are snacks and fruit every afternoon."),
       ("你需要吃药。还有，要多休息。", "4. You need to take medicine. Also, you need to rest more."),
       ("我要大杯，不要冰，还有，少放糖。", "5. I want a large, no ice, and also, less sugar."),
       ("不要一边吃饭，一边说话。还有，别吃那么快。", "6. Don’t talk while eating. And don’t eat so fast."),
       ("酒店谁来订？还有，机票买了吗？", "7. Who will book the hotel? Also, have the plane tickets been bought? (the book prints these examples with spaces before the punctuation; removed)")]
A6 = [("先生，这里不能吸烟。另外，也不要在这里打电话。", "1. Sir, you can’t smoke here. In addition, please don’t make phone calls here either. (my completion)"),
      ("下班以后早点回来。还有，别忘了买菜。", "2. Come back early after work. Also, don’t forget to buy groceries. (my completion)"),
      ("考试的时候不要说话。另外，也不能看手机。", "3. Don’t talk during the exam. In addition, you can’t look at your phone either. (my completion)"),
      ("他们不想要孩子。另外，他们也不想买房子。", "4. They don’t want children. Besides, they don’t want to buy a house either. (my completion)"),
      ("希望你不要再迟到了。还有，上课要认真听讲。", "5. I hope you won’t be late again. Also, listen carefully in class. (my completion)"),
      ("课堂上要注意听老师讲课。另外，也要认真做笔记。", "6. Pay attention to the teacher’s lecture in class. In addition, take notes carefully too. (my completion)")]
A8S = [("使用智能手机有很多好处。除了可以打电话以外，还可以上网、拍照和导航。另外，用手机付款也特别方便。还有，手机里有很多应用软件，可以学习外语。", "Smartphones (mine): Using a smartphone has many benefits. Besides making phone calls, you can also go online, take photos and navigate. In addition, paying by phone is especially convenient. Also, a phone has many apps and you can study a foreign language."),
       ("参军入伍有很多好处。除了可以锻炼身体以外，还可以学到很多技术。另外，当兵的人可以得到学习的机会。还有，军人受到大家的尊重。", "Joining the army (mine): Joining the army has many benefits. Besides keeping your body in shape, you can also learn many skills. In addition, soldiers can get chances to study. Also, soldiers are respected by everyone."),
       ("住在蒙特雷有很多好处。除了风景美以外，天气也很好。另外，这里有很多好吃的海鲜。还有，去海边很方便。", "Living in Monterey (mine): Living in Monterey has many benefits. Besides the beautiful scenery, the weather is good too. In addition, there is lots of delicious seafood here. Also, it is easy to get to the seaside.")]
L5 = lesson(
    "Lesson 25 Presentation 2 grammar: 另外 and 还有 for additional information as an afterthought",
    "另外 · 还有 · 航班经常晚点 另外 飞机餐也很难吃 · 你需要吃药 还有 要多休息 · 使用智能手机的好处",
    requires=[],
    cards=[
        card("话语语法: 另外 and 还有 for Providing Additional Information as an Afterthought",
             "另外 is similar to the English “in addition” or “besides,” while 还有 is closer to “also...” or “as well as....” Both introduce new information as an afterthought. As a conjunction, 另外 can link two sentences and is often followed by 还 or 也. 还有 can be used before the new clause or sentence. 还有 can also be used with a comma, similar to how you can say “in addition...” in English.",
             tables=[AF], examples=[D(z, e) for z, e in AFE]),
        card("Examples with 另外 and 还有", "The English is mine.", examples=[D(z, e) for z, e in AFX]),
        card("Activity 6 (Reading, Writing, Speaking and Listening)",
             "A. Pair up. Complete three of the following sentences with 另外 or 还有, while a partner does the other three: 1. 先生，这里不能吸烟。 2. 下班以后早点回来。 3. 考试的时候不要说话。 4. 他们不想要孩子。 5. 希望你不要再迟到了。 6. 课堂上要注意听老师讲课。 B. Read your sentences to your partner while they transcribe them, then convert your transcriptions to Chinese characters. My completions:",
             examples=[D(z, e) for z, e in A6]),
        card("Activity 7 (Listening, Writing, Speaking and Reading)",
             "A. Listen to the following three speakers, then fill in the table in Chinese with the particular benefits each one mentions (Speakers 1, 2, 3 | Benefits Mentioned). B. Compare information with a partner, then report your answers to the class in Chinese. C. Read the script and check your answers against it. (Audio; the script is not in the book.)"),
        card("Activity 8 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three and divide up the topics below: 使用智能手机的好处; 参军入伍的好处; 住在蒙特雷的好处. Using 另外, 还有 and/or 除了, write a four to six sentence summary of the benefits of your particular topic. B. Read your summary to your partners. My samples:",
             examples=[D(z, e) for z, e in A8S]),
    ],
    exercises=[
        M("What is 另外 like in English?", "“In addition” or “besides”", ["“Because”", "“However”", "“Unless”"], "另外."),
        M("What is 还有 closer to?", "“Also…” or “as well as…”", ["“But…”", "“So…”", "“If…”"], "还有."),
        M("What kind of information do both introduce?", "New information as an afterthought", ["A reason", "A condition", "A contrast"], "Afterthought."),
        M("What often follows 另外?", "还 or 也", ["不 or 没", "吗 or 呢", "了 or 过"], "另外…还/也…."),
        M("Which sentence is correct?", "你需要吃药。还有，要多休息。", ["你需要吃药。吗，要多休息。", "你需要吃药。因为，要多休息。", "你需要吃药，但是，还有。"], "还有，…."),
        M("What does 我要大杯，不要冰，还有，少放糖 mean?", "I want a large, no ice, and less sugar", ["I want ice", "I want more sugar", "I want a small"], "还有，少放糖."),
        M("What is added after 这个航班经常晚点?", "Their in-flight meals are hard to eat", ["The seats are big", "The price is low", "The pilot is new"], "飞机餐也很难吃."),
        M("What does 酒店谁来订？还有，机票买了吗？ ask?", "Who books the hotel, and whether the tickets are bought", ["Who flies the plane", "Who pays the bill", "Where the airport is"], "还有，…吗？"),
        F("这个航班经常晚点。___外，他们的飞机餐也很难吃。", "另", PART, "另外."),
        F("你需要吃药。___有，要多休息。", "还", PART, "还有."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration 1-3
SK3 = table(["补充词汇", "English"], [["奇妙", "fantastic, wonderful"], ["风味", "distinctive flavor"], ["细心", "careful, attentive"], ["温馨", "warm and comfortable"], ["好奇心", "curiosity"]],
            title="Activity 3A: supplementary vocabulary (the book prints pinyin and English)", say=[0])
B1 = [("记得看到过这样一句话：现在大家的旅行就像快餐，钱都花在当地和自己熟悉的东西上，但是，如果旅行更像是当地风味的豪华自助餐呢？你会更喜欢吗？", "1) I remember seeing a saying like this: these days everyone’s travel is like fast food, with the money all spent on local things and things you are familiar with; but what if travel were more like a luxury buffet of local flavors? Would you like it more?"),
      ("这一次因为出差，我和同事两个人需要在上海住三天。来之前，我们已经在木鸟短租上订了一间民宿。通过跟房东的线上交谈，我们觉得房东是一个非常细心的人。当他了解到我们是两个女生，而且是晚上十一点才到车站，就告诉我们，他会去车站接我们。然后，又把房间的密码发给了我。我们到车站的时候，接到一个司机打来的电话，他告诉我们因为房东先生工作太忙，不能亲自来接站，所以特地叫了专车来接我们。", "2) This time, because of a business trip, my colleague and I needed to stay in Shanghai for three days. Before coming, we had already booked a homestay on Mumian Short-term Rentals. From our online chat with the landlord we felt that he was a very attentive person. When he learned that we were two girls and would not reach the station until eleven at night, he told us that he would pick us up at the station. Then he sent me the room’s password. When we reached the station we got a call from a driver, who told us that because the landlord was too busy at work to come and meet us in person, he had specially called a car to pick us up."),
      ("到了目的地，房间的锁是密码锁，而且密码已经发到我的手机上，所以进入房间超级容易。房间里比我们原来想象的要好得多，因为在短租平台上看到的图片，房间是冷色的，但是到了晚上开灯之后才发现原来房间是如此温馨。橘色的灯光，让整个房间温暖、舒适。那天晚上，还没见到面的房东竟然帮我们叫了外卖！而且是一家高档餐厅的外卖！这让我对房东充满了好奇心。", "3) On arrival, the room had a combination lock and the password had already been sent to my phone, so getting in was super easy. The room was much better than we had imagined, because in the pictures on the short-term rental platform the room had cool colors, but after turning on the lights in the evening we found that the room was in fact this warm and cozy. The orange light made the whole room warm and comfortable. That night the landlord, whom we had not yet met, even ordered takeout for us! And it was takeout from a high-end restaurant! This filled me with curiosity about the landlord. (source note: adapted from a post on the Jianshu website; the English is mine)")]
B2 = [("白天忙工作，晚上回到家，可以做做饭，看看书，听听音乐，和同事一起到楼下散步，找些当地的小吃。房间里边有很多关于美食的书，我想房东一定很爱美食吧。说来奇怪，这谜一样的房东在我们入住这三天的时间里，完全没有露面，但是细心的安排让我们却非常感动。", "1) Busy with work in the daytime, in the evening we could come home and cook, read, listen to music, and take a walk downstairs with my colleague to find some local snacks. The room had many books about food, and I thought the landlord must love food. Strangely, this mysterious landlord did not show his face at all during our three days of staying, but his attentive arrangements moved us a lot."),
      ("退房当天，我给房东发了短信，告诉他我们下午就要走了，谢谢他的照顾。房间也简单收拾好了。没想到房东马上回了我的短信：中午见，等我吃饭。见到房东才知道，原来他是餐厅的大厨，平时工作忙，住在单位的宿舍里，这间房子就空了出来。那天的外卖也是他特别为我们做的，今天中午是请假回来，想给我们两个做一顿午餐，表示欢迎。房东先生还教了我一道他的拿手菜，真地感谢。", "2) On the day of checking out, I sent the landlord a text message to tell him that we were leaving in the afternoon and to thank him for looking after us. The room was also tidied up simply. Unexpectedly the landlord replied to my message right away: see you at noon, wait for me to eat. Only when we met him did we learn that he is a chef at a restaurant; he is usually busy with work and lives in his workplace’s dormitory, so this house was left empty. The takeout that day had also been made by him specially for us, and today he had taken leave and come back at noon to make lunch for the two of us as a welcome. Mr. Landlord also taught me one of his signature dishes; I am truly grateful. (the book prints 真地感谢 as it stands)"),
      ("我和同事都被这位房东迷住了，跟他聊天，就像一家人一样，很是温暖和自在。这次奇妙的短租经历，让我从此爱上了民宿。", "3) My colleague and I were both charmed by this landlord; chatting with him was like being one family, very warm and at ease. This wonderful short-term rental experience made me love homestays from then on. (source note: edited from a post on the Jianshu website)")]
TB = [("第一部分第一段：旅行像快餐，如果像当地风味的豪华自助餐，你会更喜欢吗？", "Part 1, paragraph 1 (my notes): travel is like fast food; would you like it more if it were like a luxury buffet of local flavors?"),
      ("第一部分第二段：因为出差，两个女生在上海住三天，房东很细心，叫了专车来接站。", "Part 1, paragraph 2 (my notes): on a business trip two women stay in Shanghai for three days; the landlord is attentive and has a car sent to meet them."),
      ("第一部分第三段：密码锁很方便，房间温馨，房东还帮她们叫了高档餐厅的外卖。", "Part 1, paragraph 3 (my notes): the combination lock is convenient, the room is cozy, and the landlord even orders takeout from a high-end restaurant for them."),
      ("第二部分第一段：白天工作，晚上做饭、散步，房东一直没有露面，但是安排细心。", "Part 2, paragraph 1 (my notes): work by day, cooking and walking at night; the landlord never shows up, but arranges everything attentively."),
      ("第二部分第二段：退房那天房东请假回来，他是大厨，做了午餐，还教了一道拿手菜。", "Part 2, paragraph 2 (my notes): on checkout day the landlord comes back on leave; he is a chef, makes lunch and teaches a signature dish."),
      ("第二部分第三段：像一家人一样，作者从此爱上了民宿。", "Part 2, paragraph 3 (my notes): like one family; the author has loved homestays ever since.")]
TC = [("地点是上海，住了三天，原因是出差，在木鸟短租上订的民宿。", "3C (mine): Where, duration, reason and booking method: Shanghai, three days, a business trip, booked on Mumian Short-term Rentals."),
      ("房东是餐厅的大厨，很细心，住在单位的宿舍里。", "3C (mine): The owner: a chef at a restaurant, attentive, who lives in his workplace’s dormitory."),
      ("她们做饭、看书、听音乐、散步，印象是温馨、奇妙，爱上了民宿。", "3C (mine): Activities and impressions: they cooked, read, listened to music and took walks; the impression was warm and wonderful, and she fell in love with homestays.")]
L6 = lesson(
    "Lesson 25 Presentation 2 skill integration: stories, an interview and a blog post",
    "一次奇妙的短租经历 · 细心的房东 · 密码锁 · 高档餐厅的外卖 · 大厨 · 拿手菜 · 爱上了民宿",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Speaking and Reading)",
             "A. Listen to the three stories and write a summary of each one (Story 1, Story 2, Story 3). B. Form groups of three and divide up the stories. Fill in the EEIs of your particular story in the table (EEIs 1, 2, 3). C. Tell your teammates about your story in Chinese while they jot down the EEIs. D. Read the script and check your information against it. E. Report your stories to the class in Chinese. (Three pictures and the audio are not included; the script is not in the book.)"),
        card("Skill Integration, Activity 2 (Listening, Speaking and Reading)",
             "A. Listen to the conversation once through and answer the questions. 1. Who are the speakers? 2. What is the topic of conversation? 3. What four or five aspects of this topic do they discuss? B. Listen to the conversation again and fill in the table with the necessary information: Guest Information (Interviewees); When Airbnb Hosted; Property Information; Reason for Hosting; Room Prices; How to Start Hosting; Related Fees; Summary of Hosting Experience. C. Compare information with a partner in Chinese. D. Read the script, check your information against it, then perform the dialog with your partner. E. In Chinese, tell your partner about any experiences you, your family or friends have had with Airbnb or other short-term rentals. (Two pictures and the audio are not included; the script is not in the book.)"),
        card("Skill Integration, Activity 3 (Reading, Speaking and Listening)",
             "A. Study the following new words with a partner and practice using them in a few sentences. B. Form two groups of three. Read the first part of the blog post, while the other group reads the second part. Fill in the table (Paragraph | Main Idea & EEIs) for your respective part, then compare work with your teammates. The post is titled 一次奇妙的短租经历, A Wonderful Short-Term Rental Experience, in two parts. (Pictures are not included.)",
             tables=[SK3]),
        card("一次奇妙的短租经历 (一)", "The first part, with my English.", examples=[D(z, e) for z, e in B1]),
        card("一次奇妙的短租经历 (二)", "The second part, with my English.", examples=[D(z, e) for z, e in B2]),
        card("Activity 3: my notes and table",
             "C. Pair up with a student from the other group, exchange information in Chinese, then fill in the table (Information | Short-Term Rental Experience: Where; Duration; Reason; Booking Method; Rental Information; Owner Information; Activities During Stay; Impressions). D. In Chinese, tell your partner about a short-term rental experience you, your family or friends have had. The book’s tables are blank; these notes are mine.",
             examples=[D(z, e) for z, e in TB + TC]),
    ],
    exercises=[
        M("Why did the two women stay in Shanghai?", "A business trip", ["A holiday", "A wedding", "A study tour"], "因为出差."),
        M("How long did they stay?", "Three days", ["One day", "A week", "A month"], "住三天."),
        M("Where did they book the homestay?", "On a short-term rental platform", ["At a hotel desk", "By phone only", "At the station"], "在木鸟短租上订了一间民宿."),
        M("What made them feel the landlord was attentive?", "He said he would pick them up and sent the room password", ["He gave them money", "He was at the door", "He sent flowers"], "非常细心."),
        M("How did they get into the room?", "With a password lock", ["With a key from the host", "The door was open", "With a card"], "密码锁."),
        M("What did the landlord order for them that night?", "Takeout from a high-end restaurant", ["Flowers", "A taxi", "Breakfast"], "高档餐厅的外卖."),
        M("What does the landlord actually do?", "He is a chef at a restaurant", ["He is a teacher", "He is a driver", "He is a doctor"], "餐厅的大厨."),
        M("Why was the house empty?", "He lives in his workplace dormitory", ["He moved abroad", "It was new", "He was ill"], "住在单位的宿舍里."),
        M("What did he teach her?", "One of his signature dishes", ["A song", "A language", "A game"], "一道他的拿手菜."),
        M("What did the experience make the author do?", "Love homestays", ["Hate homestays", "Open a restaurant", "Move to Shanghai"], "让我从此爱上了民宿."),
        M("What does 奇妙 mean?", "Fantastic, wonderful", ["Careful", "Warm", "Curious"], "奇妙."),
        F("这让我对房东充满了好___心。", "奇", PART, "好奇心: curiosity."),
        F("橘色的灯光，让整个房间温暖、舒___。", "适", PART, "舒适: comfortable."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration 4
SL1 = ("在美国住民宿，首先你需要用“爱彼迎”这个网站，这是个专门预定民宿的网站，有中文网页，而且世界各地的民宿都有。旅行前，你可以先下载手机应用或在它的网站上注册成为会员，并确认邮箱和电话，然后就可以按自己的旅行地点和时间选择想要住宿的房子了。接下来，就是输入自己的个人信息，选择付款方式，我用的是支付宝。最后，提交你的订单就可以了。整个过程，基本上不超过二十分钟，而且是“一键完成”。",
       "Slip 1: To stay in a homestay in America, first you need to use the “Airbnb” website, a website specializing in booking homestays, with Chinese web pages, and with homestays all over the world. Before traveling you can first download the phone app or register as a member on its website and confirm your email and phone, and then you can choose the place you want to stay by your travel location and dates. Next is entering your personal information and choosing the payment method; I used Alipay. Finally, submit your order. The whole process basically takes no more than twenty minutes and is “done with one key.”")
SL2 = ("“爱彼迎”上面的民宿很多，你得小心的选择，这样才能找到满意的民宿。通常来说，房子的地理位置是我选择民宿的首要原因。预定以前，我在平台上看网友的评价或是跟房主了解附近是否安全，有没有方便的交通和超市，或是免费停车的地方。另外，再看看房型是否合适。这次我们是一家三口，所以选择了比较大的独立房间。接下来，就是比较价格。通常地理位置好的民宿，价格都会高一些，但是更方便。我们这次选择的房间基本上都是在六十到八十美金一晚上的。还有，一定要仔细阅读游客给房主的打分和评价。只有大多数方面房客给打满五分的才可以是真正好的民宿。",
       "Slip 2: There are many homestays on Airbnb; you have to choose carefully so you can find a homestay you are satisfied with. Generally speaking, the location of the house is my first reason for choosing a homestay. Before booking I look at netizens’ reviews on the platform or ask the host whether the neighborhood is safe, whether there is convenient transportation and a supermarket, or a place for free parking. In addition, look again at whether the room type is suitable. This time we were a family of three, so we chose a fairly large private room. Next comes comparing prices. Usually homestays in good locations cost a bit more, but are more convenient. The rooms we chose this time were basically all sixty to eighty dollars a night. Also, you must read carefully the ratings and reviews that tourists give the host. Only one that most guests have given a full five points in most respects can be a truly good homestay. (the book writes 60, 80 and 5 in digits)")
SL3 = ("旅行中住宿的费用是非常大的一笔钱。这次去美国旅行，我们尝试了住美国的民宿，中部、东海岸、西海岸，前后住了七个美国民宿。和以前住过的各种酒店、家庭旅馆和青年旅社相比，我们发现这是特别省钱的一种住宿方式，而且还可以近距离地跟当地人接触，了解美国文化和习俗，特别有趣。",
       "Slip 3: The cost of lodging on a trip is a very large sum of money. On this trip to America we tried staying in American homestays, in the Midwest, the East Coast and the West Coast, and altogether stayed in seven American homestays. Compared with the various hotels, family inns and youth hostels we have stayed in before, we found this a particularly money-saving way of lodging, and we could also be close to local people and learn about American culture and customs, which was especially interesting. (the book writes 7 in digits)")
SL4 = ("总之，在外国住民宿是非常难得的一种体会。希望大家都去体验一下，我相信一定会给你留下更多、更美好的回忆。",
       "Slip 4: In short, staying in a homestay abroad is a very rare kind of experience. I hope everyone will go and try it; I believe it will certainly leave you with more and more beautiful memories.")
SUMM = [("在美国住民宿又省钱又有趣，要先在网站上注册，选房子，输入信息，付款，选地理位置好的房子，看评价，比较价格，值得一试。", "Summary (mine): Staying in a homestay in America is both cheap and interesting: register on the website, choose a house, enter your information and pay; choose a house in a good location, read reviews and compare prices; it is worth a try."),
        ("在美国住民宿", "Title (mine): Staying in a homestay in America")]
L7 = lesson(
    "Lesson 25 Presentation 2 skill integration: a travel article about homestays in America",
    "在美国住民宿 · 爱彼迎 · 注册成为会员 · 一键完成 · 地理位置 · 省钱的住宿方式 · 留下美好的回忆",
    requires=[],
    cards=[
        card("Skill Integration, Activity 4 (Reading, Speaking, Listening and Writing)",
             "A. Form groups of three. Your teacher will give each of you one or two paragraphs from a travel article. Read your paragraphs and write a summary based on the main idea and EEIs. B. Share your summary with your teammates in Chinese. C. Reconstruct the article by putting the strips in their correct order. Share your arrangement with the class. D. Read the article together, then give it an appropriate title in Chinese. The four slips follow; the book’s own full text of the article (page 60) puts them in the order Slip 3, Slip 1, Slip 2, Slip 4. (Two pictures are not included.)",
             examples=[D(*SL1), D(*SL2), D(*SL3), D(*SL4)]),
        card("Activity 4: my summary and title", "The book leaves the summary and the title blank; mine are below. The correct order from the book’s full text is 3, 1, 2, 4.", examples=[D(z, e) for z, e in SUMM]),
    ],
    exercises=[
        M("What website does the author use to book homestays?", "Airbnb (爱彼迎)", ["Meituan", "Didi", "WeChat"], "“爱彼迎”."),
        M("How does the author pay?", "With Alipay", ["With cash", "With a check", "With WeChat Pay"], "我用的是支付宝."),
        M("How long does the whole booking take, at most?", "Twenty minutes", ["Two hours", "One day", "Two minutes"], "不超过二十分钟."),
        M("What is the author’s first reason for choosing a homestay?", "The location of the house", ["The color of the walls", "The price of breakfast", "The host’s age"], "地理位置是首要原因."),
        M("What size room did the family of three choose?", "A fairly large private room", ["A shared dorm", "A tent", "A small closet"], "比较大的独立房间."),
        M("What were the nightly prices?", "Sixty to eighty dollars", ["Six to eight dollars", "Six hundred dollars", "Free"], "六十到八十美金一晚上."),
        M("How many American homestays did they stay in?", "Seven", ["Two", "Five", "Seventeen"], "前后住了七个."),
        M("What do they say about homestays compared with hotels?", "They save a lot of money", ["They are much more expensive", "They are noisy", "They are unsafe"], "特别省钱."),
        M("What is the correct order of the slips?", "3, 1, 2, 4", ["1, 2, 3, 4", "4, 3, 2, 1", "2, 3, 1, 4"], "The book’s full text."),
        F("总之，在外国住民宿是非常难得的一种___会。", "体", PART, "体会: experience."),
        F("整个过程，基本上不超过二十分钟，而且是“一键___成”。", "完", PART, "一键完成."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese
UT1 = table(["爱彼迎", "Details and Information"], [["爱彼迎有什么服务", "(blank in the book)"], ["怎么使用爱彼迎", "(blank in the book)"], ["爱彼迎的特点和优势", "(blank in the book)"], ["其它", "(blank in the book)"]],
            title="Activity 1A: the table to fill in", say=[0])
UT2 = table(["第一组：民宿、短租好"], [["原因一"], ["原因二"], ["原因三"]], title="Activity 2B: Group 1 reasons (the book’s rows are numbered 1, 2, 3)", say=[0])
UT3 = table(["第二组：宾馆、酒店好"], [["原因一"], ["原因二"], ["原因三"]], title="Activity 2B: Group 2 reasons (the book’s rows are numbered 1, 2, 3)", say=[0])
UT4 = table(["中国游客", "Opinions/Advice"], [["中国人喜爱住民宿、短租的原因", "(blank in the book)"], ["中国人喜欢用的短租平台，应用和支付方式", "(blank in the book)"], ["中国人的旅行习惯和喜好", "(blank in the book)"], ["房间、厨房、客厅等处准备些什么", "(blank in the book)"], ["房间布置", "(blank in the book)"], ["食物选择", "(blank in the book)"], ["文化不同的地方", "(blank in the book)"]],
            title="Activity 3B: the table to fill in", say=[0])
UCS = [("大家好！今天我们来介绍爱彼迎。在这个平台上，你可以在手机上订世界各地的民宿，而且价格比宾馆便宜。", "Livestream sample (mine): Hello everyone! Today we introduce Airbnb. On this platform you can book homestays all over the world on your phone, and the prices are cheaper than guesthouses."),
       ("使用爱彼迎很简单，首先下载应用，然后选地方，接下来确认时间，最后用手机付款。", "Livestream sample (mine): Using Airbnb is simple: first download the app, then choose a place, next confirm the dates, and finally pay by phone."),
       ("住民宿是很好的选择，因为价格便宜，还可以跟房主聊天。", "Debate sample, Group 1 (mine): Staying in a homestay is a good choice, because the price is cheap and you can chat with the host."),
       ("住宾馆更好，因为宾馆更干净，而且有人打扫房间。", "Debate sample, Group 2 (mine): A guesthouse is better, because it is cleaner and someone cleans the room."),
       ("中国游客喜欢有网络的房间，最重要的是要有热水和干净的卫生间。", "Advice sample (mine): Chinese tourists like rooms with internet; the most important thing is to have hot water and a clean bathroom."),
       ("厨房里最好准备一些锅和碗，因为很多中国人喜欢自己做饭。", "Advice sample (mine): It is best to prepare some pots and bowls in the kitchen, because many Chinese people like to cook for themselves.")]
L8 = lesson(
    "Lesson 25 Presentation 2 using Chinese in context: Airbnb, a debate and hosting advice",
    "爱彼迎推广大使 · 民宿、短租好还是宾馆、酒店好 · 当好民宿主的建议 · 微信直播",
    requires=[],
    cards=[
        card("爱彼迎推广大使 (Using Chinese in Context, Activity 1)",
             "A. Pair up. You and an expat colleague are hired by Airbnb China (爱彼迎) to market their services to Chinese travelers planning to visit the U.S. Visit the Chinese Airbnb website. Take notes on its platform and services in the table provided and search for any relevant information you may need. B. You plan to livestream on WeChat and other platforms to introduce Airbnb services and their advantages, the platform and its app, and how to book accommodations via smartphone apps. Decide who will say what during the livestream and practice your presentation together. C. Livestream to your Chinese audience (your classmates), who will ask you questions about Airbnb. D. When all pairs have finished, vote as a class for the best livestream performance. (Three pictures and the website are not used.)",
             tables=[UT1], examples=[D(z, e) for z, e in UCS[:2]]),
        card("民宿、短租好还是宾馆、酒店好 (Using Chinese in Context, Activity 2)",
             "A. Divide the class into two groups to debate which accommodations are better: Airbnb or short-term rentals, and hotels. As long as the two groups are fairly even in number, divide up according to your preference when traveling. B. Write down the reasons for your preference in Chinese characters in the appropriate table. C. In Chinese, discuss why you think your opponents’ choice is bad. List your reasons or arguments in the tables 宾馆、酒店不好 (Group 1) and 民宿、短租不好 (Group 2). D. Debate when you are ready. Use such patterns as 是…的主要原因, 另外, 还有 and 特别是 as much as possible. E. Your teacher will chair the debate and critique your performance afterwards. (Three pictures are not included.)",
             tables=[UT2, UT3], examples=[D(z, e) for z, e in UCS[2:4]]),
        card("当好民宿主的建议 (Using Chinese in Context, Activity 3)",
             "A. Pair up. A friend who owns a house in Monterey wants to start an Airbnb or other short-term rental service. They ask for your advice on attracting Chinese tourists. In Chinese, ask your teacher and classmates for their opinion, covering at least the following points: reasons Chinese tourists like Airbnb or short-term rentals; what tools, platforms and payment methods they use; their travel habits and preferences; how the homeowner should prepare their rooms, kitchen, living room, etc.; advice on room decoration, food choices and cultural considerations. B. Based on their opinions and advice, fill in the table below. C. Use the information you have gathered to list your advice (当一个好民宿主的建议). D. Read your suggestions to your teacher and classmates and solicit their comments. (Three pictures are not included.)",
             tables=[UT4], examples=[D(z, e) for z, e in UCS[4:]]),
    ],
    exercises=[
        M("Who hires you in Activity 1?", "Airbnb China (爱彼迎)", ["A hotel", "Didi", "Meituan"], "爱彼迎推广大使."),
        M("Where do you livestream in Activity 1?", "On WeChat and other platforms", ["On the radio", "In a newspaper", "In a hotel lobby"], "Activity 1B."),
        M("What do the two debate groups argue about?", "Airbnb/short-term rentals or hotels", ["Takeout or cooking", "Trains or planes", "Summer or winter"], "民宿、短租好还是宾馆、酒店好."),
        M("Which patterns should you use in the debate?", "是…的主要原因, 另外, 还有, 特别是", ["能…吗, 不是…吗", "先…然后…最后", "又…又…"], "Activity 2D."),
        M("Who chairs the debate?", "The teacher", ["A student", "A host", "The winner"], "Activity 2E."),
        M("Where is your friend’s house?", "Monterey", ["Shanghai", "Beijing", "Chengdu"], "A friend who owns a house in Monterey."),
        M("Whose opinions do you ask for in Activity 3?", "Your teacher’s and classmates’", ["Your parents’", "A tourist’s", "A cook’s"], "Activity 3A."),
        M("Which is NOT a point to cover in Activity 3A?", "How to cook Chinese dumplings", ["Reasons Chinese tourists like Airbnb", "Payment methods they use", "Room decoration"], "The listed points."),
        F("你是爱彼迎推广___使。", "大", PART, "推广大使: promotion ambassador."),
        F("当一个好民宿主的___议。", "建", PART, "建议: suggestions."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 25 Presentation 2 vocabulary", "37 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book capitalizes the English “Area”; it is written lower case here.", VOC2)

UNIT = unit("第二十五课 Presentation 2: 民宿和短租, 特别和最, 接下来, 另外和还有", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
