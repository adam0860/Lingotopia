"""Unit 76: Lesson 25 (Smart Life), Presentation 1: the takeout dialog with its activities, rhetorical questions with 吗, 除了, 先…然后…最后 and 而且 with their activities,
the skill-integration tasks (the videos, the news article about foreigners and Chinese takeout, the Ele.me journal), the using-Chinese tasks and the vocabulary list.
Audio, pictures, videos and websites are not included; numbers the book writes as digits are spelled out; answers that the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l25_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("发现自己", 0, "fa1"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('数都数不', 0, 'shu3'), ('数都数不', 2, 'shu3'), ('便宜得多', 2, 'de5'), ('懒得', 1, 'de5'), ('人为什么', 1, 'wei4'), ('为人们', 0, 'wei4'), ('萨和面', 1, 'he2'), ('队长', 1, 'zhang3'), ('教教妈妈', 0, 'jiao1'), ('教教妈妈', 1, 'jiao1')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 1
P1 = [("女儿", "妈，我饿了，咱们叫外卖吧。", "Daughter: Mom, I’m hungry; let’s order takeout. (translations in this card are mine)"),
      ("妈妈", "叫外卖？外卖能比我做得快吗？", "Mom: Order takeout? Can takeout be faster than my cooking?"),
      ("女儿", "当然能啦。现在用手机叫外卖又快又便宜，还不用洗碗。", "Daughter: Of course it can. Ordering takeout on a phone now is fast and cheap, and you don’t even have to wash dishes."),
      ("妈妈", "可是，他们送的餐既没有营养又没有味道。", "Mom: But the meals they deliver have neither nutrition nor flavor."),
      ("女儿", "妈，你不知道，现在外卖平台上什么饭都可以点，连五星级饭店的餐，都可以点。", "Daughter: Mom, you don’t know: on takeout platforms now you can order any food, even meals from five-star hotels."),
      ("妈妈", "真的吗？除了点餐以外，还能点别的吗？", "Mom: Really? Besides ordering meals, can you order other things too?"),
      ("女儿", "可以，蔬菜、水果、饮料，外卖平台上都可以点。", "Daughter: Yes, vegetables, fruit, drinks — you can order them all on the takeout platform."),
      ("妈妈", "你都是怎么点的呢？教教妈妈吧。", "Mom: How do you order them? Teach Mom."),
      ("女儿", "你看，在手机上下载一个应用软件，比如“美团”或是“饿了么”，就可以点啦。", "Daughter: Look, download an app on your phone, such as Meituan or Ele.me, and then you can order."),
      ("妈妈", "点开这个应用后，我先做什么？", "Mom: After I open this app, what do I do first?"),
      ("女儿", "当然是先选餐馆啦，然后就是点餐，确认信息，最后下单。", "Daughter: Of course first choose a restaurant, then order dishes, confirm the information, and finally place the order."),
      ("妈妈", "点了以后，怎么付款呢？", "Mom: After ordering, how do I pay?"),
      ("女儿", "下单后，直接用微信支付就可以了，而且还有电子发票和账单。", "Daughter: After placing the order, just pay with WeChat Pay, and there are also electronic invoices and bills."),
      ("妈妈", "不过，多长时间能送到呢？", "Mom: But how long will it take to arrive?"),
      ("女儿", "很快。而且有定位服务，可以追踪，你随时可以查看外卖小哥到了哪儿，几分钟能到。", "Daughter: Very fast. And there is a location service so you can track it; at any time you can check where the delivery guy has got to and in how many minutes he will arrive."),
      ("妈妈", "那太好了，咱们就点吧。", "Mom: That’s great, then; let’s order.")]
L1 = lesson(
    "Lesson 25 Presentation 1: ordering takeout with Mom",
    "咱们叫外卖吧 · 外卖平台 · 美团 饿了么 · 先选餐馆 然后点餐 最后下单 · 定位服务",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. How often do you order food delivery or takeout? B. How do you order? C. What apps do you use? D. What do you like about them? (Four pictures are not included.)"),
        card("Presentation 1: 叫外卖", "The book also prints the dialog in traditional characters. The translations are mine.", examples=dlg(P1)),
        card("Activity 1 (Listening)",
             "A. Global Listening: Listen to Presentation 1 once through and answer the questions. 1. What is the relationship between the two speakers? (mother and daughter) 2. What do they want to do? (order takeout) 3. How are they going to do it? (with a phone app) B. Detailed Listening: Listen to Presentation 1 again and answer the questions. 1. What are three benefits of the delivery service that the first speaker mentions? (fast, cheap, no dishes to wash) 2. What is the second speaker’s concern? (the food has no nutrition or flavor) 3. What are four details about what can be ordered with the app? (any meal, even five-star hotel meals; vegetables; fruit; drinks) 4. What instructions does the first speaker give to the second speaker on how to use the platform? (download an app, open it, choose a restaurant, order dishes, confirm the information, place the order) 5. How do the speakers pay for the service? (WeChat Pay) 6. How can the speakers track their order? (the location service: see where the delivery guy is). (Audio, not included; the answers in brackets are mine, from the text.)"),
    ],
    exercises=[
        M("What does the daughter want to do?", "Order takeout", ["Cook dinner", "Go to a restaurant", "Go shopping"], "咱们叫外卖吧."),
        M("What does the mother doubt at first?", "Whether takeout can be faster than her cooking", ["Whether the app is free", "Whether the daughter is hungry", "Whether it is safe"], "外卖能比我做得快吗？"),
        M("Which is NOT a benefit the daughter mentions?", "Free of charge", ["Fast", "Cheap", "No dishes to wash"], "又快又便宜，还不用洗碗."),
        M("What is the mother’s concern about the food?", "No nutrition and no flavor", ["Too spicy", "Too expensive", "Too slow"], "既没有营养又没有味道."),
        M("What can be ordered besides meals?", "Vegetables, fruit and drinks", ["Cars", "Clothes", "Furniture"], "蔬菜、水果、饮料."),
        M("Which app is named?", "Meituan or Ele.me", ["WeChat only", "Maps only", "A bank app"], "“美团”或是“饿了么”."),
        M("What is the first step after opening the app?", "Choose a restaurant", ["Pay", "Confirm the information", "Place the order"], "先选餐馆."),
        M("What is the last step before paying?", "Place the order", ["Choose a restaurant", "Download the app", "Order dishes"], "最后下单."),
        M("How do they pay?", "With WeChat Pay", ["Cash", "Credit card", "A check"], "直接用微信支付."),
        M("What does the location service let you do?", "Track the delivery guy", ["Find the restaurant’s phone", "Pay a tip", "Print the bill"], "可以追踪."),
        F("现在用手机叫外卖又快___便宜，还不用洗碗。", "又", PART, "又…又…."),
        F("当然是先选餐馆啦，然后就是点餐，确认信息，最后___单。", "下", PART, "下单: place an order."),
        F("现在外卖平台上什么饭都可以点，___五星级饭店的餐，都可以点。", "连", PART, "连…都…: even."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2-6
FILL = [("如果你想知道外卖小哥到了哪儿，就打开平台上的定位服务，可以追踪和知道你的外卖什么时候可以到。", "Student A (my key): If you want to know where the delivery guy has got to, open the platform’s location service; you can track it and know when your takeout will arrive."),
        ("在中国留学的时候，我没有时间做饭，所以常常叫外卖。中国的送餐服务特别方便。我在手机上下载了一个应用软件。在这个外卖平台上，你什么都可以点，披萨，意大利面，中餐等等。要想吃更有营养的饭，你也可以找到。", "Student B (my key): When I studied in China I had no time to cook, so I often ordered takeout. China’s meal-delivery service is especially convenient. I downloaded an app on my phone. On this takeout platform you can order anything: pizza, pasta, Chinese food and so on. If you want food with more nutrition, you can find that too."),
        ("这个应用点开后，你可以选你喜欢的餐馆，然后看他们的菜单，所有的信息都对了，就可以确认，然后下单。你的手机上会看到电子发票和账单。", "Student C (my key): After you open this app, you can choose the restaurant you like and look at their menu; when all the information is right you can confirm and then place the order. On your phone you will see the electronic invoice and the bill. (the bank has one word left over: 付款)")]
PAT = [("我今天又累又饿，还没有时间做饭。", "又…又…，还…: I am tired and hungry today, and I don’t have time to cook either. (a sample sentence in the pattern; mine)"),
       ("现在手机上什么都可以买，连水果也可以。", "什么都…，连…也…: These days you can buy anything on a phone, even fruit. (mine)"),
       ("做饭时，先洗菜，然后切菜，最后炒菜。", "先…，然后…，最后…: When cooking, first wash the vegetables, then cut them, and finally stir-fry them. (mine)"),
       ("外卖很方便。而且价格不贵。", "…。而且…: Takeout is very convenient. And the price is not high. (mine)")]
L2 = lesson(
    "Lesson 25 Presentation 1 activities: odd words, sentences and a food-delivery interview",
    "叫外卖 叫车 · 下载 下单 · 点餐 点开 · 外卖小哥 · 应用软件 · 外卖平台 · 菜单 发票 账单",
    requires=[],
    cards=[
        card("Activity 2 (Reading)",
             "Pair up. Check the odd word out in each row and explain your reasoning. 1. 叫外卖 / 叫琳达 / 叫车 / 叫出租. 2. 下载 / 下单 / 下课 / 下雾. 3. 点餐 / 点菜 / 点酒水 / 点开. 4. 营养 / 味道 / 便宜 / 水果. The book gives no key; my answers: 1. 叫琳达 (calling a person by name, not ordering or hailing a service). 2. 下雾 (weather, not something a person does). 3. 点开 (to click open, not ordering food). 4. 水果 (a food item; the others are qualities of food or service)."),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Examine the following words: 外卖小哥, 点开, 确认, 应用, 菜单, 叫外卖, 送餐, 定位, 应用软件, 外卖平台, 付款, 发票, 下单, 营养, 下载, 账单, 追踪, 外卖. B. In groups of three, complete the sentences below using the word bank above (Students A, B and C each have a passage with blanks). C. Check your work with your teammates. D. Order the three segments to form a coherent paragraph, then take turns reading it aloud. My completed passages, and my order of the segments (B, then C, then A):",
             examples=[D(z, e) for z, e in FILL]),
        card("Activity 4 (Listening, Reading and Speaking)",
             "A. Pair up. Partner 1 listens to the first two dialogs, Partner 2 listens to the last two, and they both fill in the EEIs (relationship of speakers, topic, EEIs) from their dialogs in a table of four rows. B. Complete the table with the information you get from your partner, then share your work with the class. C. Read the dialogs, then perform them with your partner. (Audio; the dialogs are on a page that is blank in this edition.)"),
        card("Activity 5 (Reading and Writing)",
             "A. Pair up and study the following patterns. Partner 1 writes a three to four sentence paragraph with the first two patterns while Partner 2 does the same for the last two: 1. 又…又…，还… 2. 什么都…，连…也… 3. 先…，然后…，最后… 4. …。而且… B. Share your work with your partner and make any necessary corrections or improvements. C. Post your paragraphs on a website to share with the class (the website is not used here). One sample sentence for each pattern:",
             examples=[D(z, e) for z, e in PAT]),
        card("Activity 6 (Reading, Writing, Speaking and Listening)",
             "A. In groups of three, read the questions in the table below, then write down any words or sentence patterns you think you may need. B. Interview two classmates from the other groups and fill in the table (学生 1, 学生 2): 外卖的好处是什么？ 外卖可以点什么？ 用什么外卖平台/应用？ 怎么使用外卖平台/应用？ C. Share your interview results with your group. Discuss in Chinese which food delivery apps are the most popular among your classmates. 大家最喜欢用的外卖平台是： (Three pictures are not included.)"),
    ],
    exercises=[
        M("Which is the odd word out: 叫外卖, 叫琳达, 叫车, 叫出租?", "叫琳达", ["叫外卖", "叫车", "叫出租"], "Calling a person by name."),
        M("Which is the odd word out: 下载, 下单, 下课, 下雾?", "下雾", ["下载", "下单", "下课"], "Weather."),
        M("Which is the odd word out: 点餐, 点菜, 点酒水, 点开?", "点开", ["点餐", "点菜", "点酒水"], "Click open."),
        M("Which is the odd word out: 营养, 味道, 便宜, 水果?", "水果", ["营养", "味道", "便宜"], "A food item."),
        M("Who is the delivery person called?", "外卖小哥", ["外卖平台", "应用软件", "菜单"], "外卖小哥."),
        M("Which service shows where the order is?", "定位", ["付款", "发票", "菜单"], "定位服务."),
        M("What do you look at after choosing a restaurant?", "菜单", ["账单", "发票", "定位"], "看他们的菜单."),
        M("What do you see on your phone after paying?", "电子发票和账单", ["地图", "菜单", "新闻"], "电子发票和账单."),
        M("Which segment comes first in my order?", "Student B: why and how to start", ["Student A: tracking", "Student C: ordering", "Any order"], "B → C → A."),
        F("我在手机上下___了一个应用软件。", "载", PART, "下载: download."),
        F("要想吃更有营___的饭，你也可以找到。", "养", PART, "营养: nutrition."),
        F("做饭时，先洗菜，然后切菜，___后炒菜。", "最", PART, "先…然后…最后…."),
    ],
)

# ------------------------------------------------------------------ 3. rhetorical questions with 吗
RQ = [("A", "他又感冒了。", "1. A: He has caught a cold again."), ("B", "他每天穿得都很少，能不感冒吗？", "B: He wears so little every day; how could he not catch cold?"),
      ("A", "今天我可能会迟到。", "2. A: I might be late today."), ("B", "你起得这么晚。能不迟到吗？", "B: You got up so late. How could you not be late?"),
      ("A", "我点了很多菜，都是你爱吃的。", "3. A: I ordered many dishes, all ones you love."), ("B", "晚上吃这么多菜。能不胖吗？", "B: Eating this many dishes at night, how could one not gain weight? (the book’s English says “I”; the Chinese has no subject)"),
      ("A", "你看到我手机了吗？", "4. A: Have you seen my phone?"), ("B", "不是在桌子上吗？", "B: Isn’t it on the table?"),
      ("A", "我们什么时候开会？", "5. A: When do we have the meeting?"), ("B", "不是已经告诉你了吗？", "B: Haven’t I already told you?"),
      ("A", "今天放假了，好开心。", "6. A: It’s a holiday today; I’m so happy."), ("B", "不是明天放假吗？", "B: Isn’t it tomorrow that we go on vacation?")]
RQT = table(["句型", "用法"], [["能……吗？", "Points out unrealistic expectations"], ["不是……吗？", "Gently reminds someone of a fact they seem to have forgotten"]],
            title="Rhetorical Questions with 吗, 能 and 不是", say=[0])
A1 = [("你这个单元的听力不是考得很好吗？", "1. Didn’t you do very well on the listening part of this unit? (the six statements are printed in the book; the rhetorical questions in this card are mine)"),
      ("他们送的外卖能有营养吗？", "2. How could the takeout they deliver be nutritious?"),
      ("蔬菜、水果、饮料，外卖平台上不是都可以点吗？", "3. Aren’t vegetables, fruit and drinks all available on the takeout platform?"),
      ("点开这个应用后，你不是应该先选餐馆吗？", "4. After opening this app, shouldn’t you choose a restaurant first?"),
      ("这是五星级饭店的餐，味道能不好吗？", "5. This is a meal from a five-star hotel; how could it not taste good?"),
      ("我不是已经说了做完作业才可以看电视吗？", "6. Didn’t I already say you may watch TV only after finishing your homework?")]
A2 = [("张华，咱们今晚去电影院看最新的《美国队长》吧？", "A: Zhang Hua, shall we go to the cinema tonight to see the latest “Captain America”? (the film title is as printed in the book)"),
      ("你不是明天有考试吗？今晚能去看电影吗？", "B (mine): Don’t you have an exam tomorrow? How can you go to a movie tonight?"),
      ("妈，你看到我从学校带回来的那本书了吗？", "A: Mom, have you seen the book I brought back from school?"),
      ("不是在你的书桌上吗？", "B (mine): Isn’t it on your desk?"),
      ("李文，昨天晚上跟你们吃完晚饭回宿舍以后不久，我就开始胃疼。", "A: Li Wen, not long after I got back to the dorm from dinner with you last night, my stomach started to hurt."),
      ("你吃了那么多辣的，胃能不疼吗？", "B (mine): You ate so much spicy food; how could your stomach not hurt?")]
L3 = lesson(
    "Lesson 25 Presentation 1 grammar: rhetorical questions with 吗",
    "能不感冒吗 · 能不胖吗 · 不是在桌子上吗 · 不是已经告诉你了吗 · 能……吗 · 不是……吗",
    requires=[],
    cards=[
        card("Rhetorical Questions with 吗",
             "A rhetorical question is a figure of speech in which a question is asked not to get an answer but to make a persuasive point, e.g., the English “how could...?” or “isn’t…?” It is similar in Chinese: 外卖能比我做得快吗？ (How could food delivery possibly be faster than I can cook?) In rhetorical questions, 吗 is often used together with 能 and 不是. As with regular questions, 吗 always comes at the end of a sentence.",
             tables=[RQT], examples=dlg(RQ)),
        card("Activity 1 (Reading and Writing)",
             "A. In groups of three, each student changes two of the following statements into rhetorical questions using 能……吗 or 不是……吗. Add any words you need. 1. 你这个单元的听力考得很好。 2. 他们送的外卖没有营养。 3. 蔬菜、水果、饮料，外卖平台上都可以点。 4. 点开这个应用后，你当然要先选餐馆啦。 5. 这是五星级饭店的餐，所以味道特别好。 6. 我已经说了做完作业才可以看电视。 B. Share your work with your partners. My versions:",
             examples=[D(z, e) for z, e in A1]),
        card("Activity 2 (Reading, Writing, Speaking and Listening)",
             "A. In pairs, complete the following dialogs with rhetorical questions using 能……吗 or 不是……吗. B. Read your completed dialogs to the class. The book prints the three lines of A and leaves B blank; the B lines are mine:",
             examples=[D(z, e) for z, e in A2]),
        card("Activity 3 (Listening, Reading and Speaking)",
             "A. Listen to the dialog and answer the questions. Compare answers with a partner. 1. Who are the two speakers? 2. What does the man try to convince the woman to do? 3. Why does he fail to persuade her? 4. What does he believe? B. Read the script, then perform it with your partner. C. In Chinese, discuss your views of the mother. What else might you tell her if you were the boyfriend? (Audio; the script is not in the book.)"),
    ],
    exercises=[
        M("What is a rhetorical question for?", "To make a point, not to get an answer", ["To ask for directions", "To ask the time", "To order food"], "A figure of speech."),
        M("Which pattern points out an unrealistic expectation?", "能……吗？", ["不是……吗？", "是不是……？", "有没有……？"], "能…吗."),
        M("Which pattern gently reminds someone of a forgotten fact?", "不是……吗？", ["能……吗？", "怎么……？", "什么……？"], "不是…吗."),
        M("What does 他每天穿得都很少，能不感冒吗？ mean?", "How could he not catch cold?", ["He caught a cold", "He wears a lot", "He never gets cold"], "能不…吗: how could he not."),
        M("What does 不是已经告诉你了吗？ mean?", "Haven’t I already told you?", ["I told nobody", "Tell me again", "Who told you?"], "不是…吗."),
        M("What does 你起得这么晚。能不迟到吗？ imply?", "You will certainly be late", ["You will be early", "You got up early", "You are never late"], "能不迟到吗: surely late."),
        M("Where does 吗 always come in a sentence?", "At the end", ["At the start", "After the subject", "Before the verb"], "吗 at the end."),
        M("Which is a rhetorical form of 他们送的外卖没有营养?", "他们送的外卖能有营养吗？", ["他们送外卖吗？", "他们送外卖了吗？", "外卖有营养吗，谢谢？"], "能有…吗."),
        F("你起得这么晚。能不迟到___？", "吗", ["呢", "了", "吧"], "能不…吗."),
        F("不是在桌子上___？", "吗", ["吧", "呢", "了"], "不是…吗."),
    ],
)

# ------------------------------------------------------------------ 4. 除了
CL = [("现在外卖平台上什么饭都可以点，连五星级饭店的餐，你也可以点。", "Assertion: Now on takeout platforms you can order any food, even meals from five-star hotels."),
      ("除了点餐以外，外卖平台上还可以点蔬菜、水果和饮料。", "Additional facts that strengthen the assertion: Besides ordering meals, on takeout platforms you can also order vegetables, fruit and drinks.")]
CL2 = [("下载外卖平台的手机应用以后，你就可以直接在手机上点餐、下单。然后也可以用手机付款。除了这些以外，你也可以用手机追踪外卖小哥的定位，看他们到了哪儿。", "1. After downloading the takeout platform’s app you can order and place the order directly on your phone. Then you can also pay by phone. Besides these, you can also use your phone to track the delivery guy’s location and see where he has got to. (additional information + pause)"),
       ("学习中文有很多不同的方法。有的学生喜欢看中文电影、听中文歌；也有的学生喜欢读中文报纸和杂志。还有的喜欢跟中国人交朋友，练习口语。除了多听、多说、多看（以外），也要多写。比如，要常写中文汉字或是写周记什么的。", "2. There are many different ways to learn Chinese. Some students like to watch Chinese films and listen to Chinese songs; others like to read Chinese newspapers and magazines. Still others like to make Chinese friends and practice speaking. Besides listening, speaking and reading more, you should also write more. For example, often write Chinese characters or a weekly journal. (additional information + pause)"),
       ("“滴滴”除了为人们提供便利的出行服务以外，也为很多人提供了工作机会，增加了他们的收入。一般来说，“滴滴”司机每月的收入能有四千到五千元人民币。", "3. Besides providing people with convenient travel services, Didi has also provided jobs for many people and increased their income. Generally speaking, a Didi driver’s monthly income can reach 4,000 to 5,000 yuan. (additional information; the book writes the numbers in digits)")]
S4 = [("周末的时候，我喜欢呆在宿舍里。有时候我在网上跟一些网友一起打游戏。", "Student 1: At weekends I like to stay in the dorm. Sometimes I play games online with some online friends. (the book’s example)"),
      ("除了打游戏以外，我也会给我的父母打打电话，告诉他们我的学习情况和在这儿的生活。", "Student 2: Besides playing games, I also call my parents and tell them about my studies and life here."),
      ("除了给父母打电话以外，我也看看中文电视节目，因为有的节目非常有意思，而且还可以练习我的中文听力。", "Student 3: Besides calling my parents, I also watch Chinese TV programs, because some are very interesting and I can practice my Chinese listening too.")]
CT = table(["句式", "用法"], [["Assertion + 除了……（以外），……", "additional information"], ["除了……之外，除此之外，除此以外", "the more formal or literary versions"]],
           title="Providing Additional Information with 除了 (the structure and the formal versions)")
L4 = lesson(
    "Lesson 25 Presentation 1 grammar: providing additional information with 除了",
    "除了点餐以外 · 除了这些以外 · 除了多听多说多看以外 · 除了……之外 · 除此之外 · 滴滴",
    requires=[],
    cards=[
        card("话语语法: Providing Additional Information with 除了",
             "除了 can be used to provide more arguments, alternatives, or facts to strengthen an assertion or proposition. It can also provide listeners a pause to digest the information. 除了……（以外） can be used within a paragraph after initial information has been introduced, or to begin a new paragraph containing much more information. Note: The more formal or literary versions of 除了……（以外） are 除了……（之外）, 除此之外 and 除此以外.",
             tables=[CT], examples=[D(z, e) for z, e in CL]),
        card("Examples with 除了", "The brackets of the book’s 除了……（以外） are kept in example 2. The translations are mine.", examples=[D(z, e) for z, e in CL2]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Form groups of three. The first student makes an assertion about a topic of their choosing. The second student adds to the information with 除了……（以外）. The third student adds more information. Keep going for two more rounds. Study the following example before you begin. B. In turn the second and third students will begin the activity with a topic of their choice. (Three pictures are not included.)",
             examples=[D(z, e) for z, e in S4]),
        card("Activity 5 (Reading, Writing, Speaking and Listening)",
             "A. Form groups of three. Write a paragraph 4–6 sentences in length on one of the topics below using 除了……（以外） while your teammates do the same for the other two: 1. 学习中文 2. 锻炼身体 3. 兴趣爱好. B. Read your paragraphs aloud and help each other make any necessary corrections or improvements. C. Upload your paragraphs to a website and share with the class (the website is not used here)."),
    ],
    exercises=[
        M("What can 除了 be used for?", "To add arguments, alternatives or facts", ["To end a sentence", "To ask a question", "To give an order"], "Additional information."),
        M("What does 除了点餐以外，外卖平台上还可以点蔬菜 mean?", "Besides ordering meals, you can order vegetables too", ["You cannot order vegetables", "Only vegetables", "Nothing else"], "除了…以外，还…."),
        M("Which is a more formal version of 除了……以外?", "除了……之外", ["除了……吗", "除了……呢", "除了……了"], "之外."),
        M("Which means “besides this”?", "除此之外", ["因此之外", "除了吗", "不是之外"], "除此之外."),
        M("Which fits “除了打游戏以外，我___会给父母打电话”?", "也", ["不", "没", "别"], "除了…以外，也…."),
        M("What does the example about Didi add to?", "The income of its drivers", ["The price of tickets", "The speed of cars", "The number of apps"], "增加了他们的收入."),
        M("What does 除了多听、多说、多看（以外），也要多写 mean?", "Besides listening, speaking and reading more, write more", ["Do not write", "Only write", "Write less"], "也要多写."),
        M("What is a Didi driver’s monthly income according to the text?", "4,000 to 5,000 yuan", ["400 yuan", "40,000 yuan", "1,000 yuan"], "四千到五千元人民币."),
        F("除了点餐以___，外卖平台上还可以点蔬菜、水果和饮料。", "外", PART, "以外 (the book prints 以外 here; 除了…以外)."),
        F("除了这些以外，你也可以用手机___踪外卖小哥的定位。", "追", PART, "追踪: track."),
    ],
)

# ------------------------------------------------------------------ 5. 先…然后…最后
ST = table(["步骤", "句式"], [["3 steps", "先…然后…最后…"], ["4 steps", "先…再…然后…最后…"], ["4 steps", "第一步…第二步…第三步…最后（一步）…"]],
           title="Simple Instructions Using 先…然后…最后… (first…then…finally…)", say=[1])
SE = [("煮饺子很容易，你先把水烧开，再把饺子放进锅里，然后煮十分钟左右，等饺子都到水面上，最后把饺子捞出来放进盘子里。这样，你的饺子就煮好啦。", "1. Boiling dumplings is easy: first bring the water to a boil, then put the dumplings into the pot, then cook for about ten minutes, and when all the dumplings have come up to the surface, finally scoop them out into a plate. That way your dumplings are done. (the book writes 再把放饺子进锅里; the word order is corrected here)"),
      ("考试的时候，要先把试卷快快地看一遍，再开始做简单的问题，然后做比较难的问题，最后再检查一遍。", "2. In an exam, first read through the paper quickly, then start with the simple questions, then do the harder ones, and finally check it once more."),
      ("给中国打国际长途，你得先拨零，然后再拨中国的国际区号八六，最后是拨打国内的区号和电话号码或是直接拨手机号码。", "3. To make an international call to China, first dial zero, then the country code for China, eighty-six, and finally the domestic area code and phone number or directly the mobile number. (the book writes 0 and 86 in digits, and 播 for 拨, which is corrected)"),
      ("在骑自行车锻炼时，先慢骑几分钟，再快骑几分钟，然后再慢骑，最后再快骑。这样，可以锻炼人的心脏功能。", "4. When exercising on a bicycle, first ride slowly for a few minutes, then fast for a few minutes, then slowly again, and finally fast again. This way you can exercise the function of the heart."),
      ("我们打算先去北京，然后去上海，最后去香港。", "Note, example 1: We plan to go to Beijing first, then Shanghai, and finally Hong Kong. (sequential future actions)"),
      ("早上，我先穿衣，再刷牙，然后洗脸，最后吃早饭。", "Note, example 2: In the morning I first get dressed, then brush my teeth, then wash my face, and finally eat breakfast. (sequential past actions)")]
L5 = lesson(
    "Lesson 25 Presentation 1 grammar: simple instructions with 先…然后…最后",
    "先…然后…最后 · 先…再…然后…最后 · 第一步…第二步… · 煮饺子 · 国际长途 · 骑自行车锻炼",
    requires=[],
    cards=[
        card("段落语法: Giving Simple Instructions Using 先…然后…最后",
             "For simple instructions, 先…然后…最后 are equivalent to the English adverbs “first…then (after that)…finally.” Example: 当然是先选餐馆啦，然后就是点餐，确认信息，最后下单。 (Naturally, first choose a restaurant, then order dishes and confirm your information, and finally submit the order.) 先…然后…最后 is for three-step instructions. If there are four steps, simply add 再 after 先, as in 先…再…然后…最后, that is, “first…then…after that…finally.” Alternatively, you can use ordinal numbers for each step, e.g., 第一步…第二步…第三步…最后（一步）. Note: 先…然后…最后 or 先…再…然后…最后 can also be used to describe sequential past events or future actions.",
             tables=[ST], examples=[D(z, e) for z, e in SE]),
        card("Activity 6 (Listening, Writing and Speaking)",
             "A. In groups of three, watch the following YouTube video (not included). B. Watch the video again and take notes in Chinese on one of the topics in the table below, while your teammates do the same for the other two: How to make the dish; How to get to the coffee shop; How to care for someone when they are sad. C. Read your notes to each other and complete the table."),
        card("Activity 7 (Writing, Speaking and Listening)",
             "A. Pair up. Write an outline of instructions for something you’re good at using 先…然后…最后 or 先…再…然后…最后, etc. in a table (Student A Instructions, Student B Instructions). B. Based on your outline, tell your partner how to do your particular skill, while your partner takes notes. C. Form groups of three with different students. Based on your notes, instruct the other students how to perform the skill you just learned. (Three pictures are not included.)"),
    ],
    exercises=[
        M("What does 先…然后…最后 mean?", "First…then…finally", ["Because…so…", "If…then…", "Not only…but also…"], "Three steps."),
        M("What do you add for four steps?", "再 after 先", ["也 after 然后", "还 before 最后", "又 at the start"], "先…再…然后…最后."),
        M("Which is the alternative to 先…然后…最后?", "第一步…第二步…第三步…最后", ["第一…第二…第三…完", "一步…二步…三步", "先步…后步"], "第一步…第二步…."),
        M("In the dumpling example, when are the dumplings scooped out?", "When they have come up to the surface", ["As soon as they go in", "After one hour", "Before the water boils"], "等饺子都到水面上."),
        M("What does the exam example say to do last?", "Check it again", ["Read the paper", "Do the easy questions", "Do the hard questions"], "最后再检查一遍."),
        M("What do you dial first for an international call to China?", "Zero", ["Eighty-six", "The area code", "The mobile number"], "先拨零."),
        M("Can the pattern describe past events?", "Yes, and future ones too", ["No, only the future", "No, only the present", "Only questions"], "Note."),
        M("What is the correct word order?", "先把水烧开，再把饺子放进锅里", ["先把水烧开，再把放饺子进锅里", "先把水开烧，再把饺子进放锅里", "先水把烧开，把再饺子放进锅里"], "把 + object + verb phrase."),
        F("我们打算先去北京，___后去上海，最后去香港。", "然", PART, "先…然后…最后…."),
        F("考试的时候，要先把试卷快快地看一遍，___开始做简单的问题。", "再", PART, "先…再…."),
    ],
)

# ------------------------------------------------------------------ 6. 而且
ET = table(["结构", "用法"], [["Subject + Predicate 1, + 而且 + Predicate 2", "connects clauses or predicates within a complex sentence"], ["Clause 1, + 而且 + Clause 2", "connects clauses within a complex sentence"], ["Sentence 1 (2, 3…) + 而且 + Sentence 2 (3, 4…)", "connects sentences"]],
           title="Additional or More Important Information with 而且 (and; moreover; furthermore; in addition to)")
ER = [("下单后，直接用微信支付就可以了，而且还有电子发票和账单。", "From the dialog: After placing the order, just pay with WeChat Pay, and there are also electronic invoices and bills."),
      ("用手机叫外卖很快。而且有定位服务，可以追踪，你随时可以查看外卖小哥到了哪儿，几分钟能到。", "From the dialog: Ordering takeout on a phone is fast. And there is a location service so you can track it; at any time you can check where the delivery guy has got to and in how many minutes he will arrive.")]
EX = [("他会讲英语，而且讲得好。", "1. He can speak English, and speaks it well."),
      ("他学习很好，而且对人很热情。", "2. He studies well, and is warm toward people."),
      ("我的作业做完了，而且全部正确。", "3. I have finished my homework, and it is all correct. (the book writes 作業 and 正確 in traditional characters; converted here, with a full stop added)"),
      ("我不知道，而且我也不想知道。", "4. I don’t know, and I don’t want to know either. (full stop added)"),
      ("天黑了，而且又下雨，别出去了。", "5. It’s dark, and it’s raining again; don’t go out. (full stop added)"),
      ("我很少出去旅游，因为我的假期很少，而且我也没有钱。", "6. I seldom go traveling, because I have few holidays, and I have no money either. (full stop added)"),
      ("我觉得学好中文，兴趣最重要。我从小就对中国文化感兴趣，喜欢看中国的功夫片。而且有了兴趣后就不觉得那么难学，还越学越爱学。", "7. I think that to learn Chinese well, interest is the most important thing. Since I was little I have been interested in Chinese culture and liked watching Chinese kung fu films. And once you have interest you don’t find it so hard to learn, and you like learning more and more. (full stop added)"),
      ("为了“活”下去，邮局扩大了自己的业务，开始了各种代理业务。而且邮局还改进了自己的快递业务，使年快递量达到四百亿件。", "8. In order to “survive,” the post office expanded its business and started all kinds of agency businesses. And the post office also improved its express delivery business, so that the annual express volume reached 40 billion items. (the book writes 400 亿 in digits and has an unmatched quotation mark; both fixed)")]
A8 = [("我喜欢住民宿。", "Sample sentence 1 (mine): I like staying in homestays."),
      ("而且民宿比酒店便宜。", "My partner adds with 而且 (mine): And homestays are cheaper than hotels."),
      ("我昨天晚上在宿舍点了外卖。", "Sample sentence 2 (mine): Last night I ordered takeout in the dorm."),
      ("而且外卖一会儿就送到了。", "Added with 而且 (mine): And it was delivered in no time."),
      ("这个应用很好用。", "Sample sentence 3 (mine): This app is easy to use."),
      ("而且还有中文版本。", "Added with 而且 (mine): And there is a Chinese version too.")]
N1 = [("外卖已经成为了人们生活的必需品，现在人们点外卖不仅仅满足于简单的吃饱，更在乎哪家餐馆的饭更健康，更好吃。而且点外卖价格不贵，既便宜又方便。", "Part 1: Takeout has become a necessity of people’s lives. Now when people order takeout they are not satisfied with simply being full; they care more about which restaurant’s food is healthier and tastier. And the price of takeout is not high, both cheap and convenient. (my English; summary in English: takeout is a necessity, people want healthy tasty food, and it is cheap and convenient)"),
      ("现在外卖在中国人的生活中非常流行，你总是可以看到外卖小哥骑着摩托车飞奔在中国的大街上。而且外卖的形式也变得多种多样，人们不仅可以在网上订餐，也可以用手机应用订餐。", "Part 2: Takeout is now very popular in Chinese people’s lives; you can always see delivery guys speeding on motorbikes along China’s streets. And the forms of takeout have become diverse: people can order not only online but also with a phone app. (the book prints 飞奔在在中国的大街上 with a doubled 在; corrected)"),
      ("在大学校园中，很多学生常常叫外卖。张华是大一的女生，她说：“冬天的时候，除了早饭，别的饭都是叫外卖，都不去食堂吃饭了。太懒了。而且如果没课，除了下楼拿外卖，可以一天都在宿舍床上呆着。”", "Part 3: On university campuses many students often order takeout. Zhang Hua is a first-year girl; she says: “In winter, apart from breakfast, I order takeout for every other meal and don’t go to the canteen at all. Too lazy. And if I have no class, apart from going downstairs to pick up the takeout, I can stay on my dorm bed all day.”")]
T9 = [("点外卖价格不贵，既便宜又方便。", "1. …and the price of takeout is not high; it is both cheap and convenient. (translation of the 而且 clause of Part 1; mine)"),
      ("外卖的形式也变得多种多样，人们不仅可以在网上订餐，也可以用手机应用订餐。", "2. …and the forms of takeout have also become diverse; people can order not only online but also with a phone app. (Part 2; mine)"),
      ("如果没课，除了下楼拿外卖，可以一天都在宿舍床上呆着。", "3. …and if there is no class, apart from going downstairs to pick up takeout, I can stay on the dorm bed all day. (Part 3; mine)")]
L6 = lesson(
    "Lesson 25 Presentation 1 grammar: additional or more important information with 而且",
    "而且 · 他会讲英语而且讲得好 · 天黑了而且又下雨 · 邮局的快递业务 · 外卖已经成为了必需品",
    requires=[],
    cards=[
        card("话语语法: Providing Additional or More Important Information with 而且",
             "而且 can be used to provide additional or more important information. It is similar to English “and,” “moreover,” “furthermore,” or “in addition to.” When 而且 occurs in a complex sentence, it normally begins the second clause or predicate to connect the two parts of the sentence. When 而且 functions as a progressive conjunction to connect two sentences, it usually begins the second sentence and means “in addition to.”",
             tables=[ET], examples=[D(z, e) for z, e in ER]),
        card("Examples with 而且", "The book prints these eight examples with a few traditional characters and missing full stops; both are fixed here. The English is mine.", examples=[D(z, e) for z, e in EX]),
        card("Activity 8 (Writing, Speaking and Listening)",
             "A. Pair up. Write three sentences in Chinese characters in the table below (句子 | 而且), then read them to your partner. Your partner will then add more information to the sentence using 而且 while you transcribe what they say. B. Convert your transcriptions into characters, then read your jointly completed sentences to the class. The book’s table is blank; three sample pairs (mine):",
             examples=[D(z, e) for z, e in A8]),
        card("Activity 9 (Reading, Speaking and Listening)",
             "A. Form groups of three. In English, summarize one part of the news report below while your teammates summarize the other two parts. B. Verbally relate your summary to your teammates in Chinese. C. Translate the sentences with 而且: 1. ……，而且点外卖价格不贵，既便宜又方便。 2. ……，而且外卖的形式也变得多种多样，人们不仅可以在网上订餐，也可以用手机应用订餐。 3. ……，而且如果没课，除了下楼拿外卖，可以一天都在宿舍床上呆着。 (Two pictures are not included.) The three parts follow, with my English:",
             examples=[D(z, e) for z, e in N1]),
        card("Activity 9C: my translations", "The three 而且 clauses without the ellipsis, with my English.", examples=[D(z, e) for z, e in T9]),
    ],
    exercises=[
        M("What does 而且 introduce?", "Additional or more important information", ["A contrast", "A reason", "A condition"], "And; moreover; furthermore."),
        M("Where does 而且 usually come in a complex sentence?", "At the start of the second clause or predicate", ["At the end", "Before the subject of the first clause", "Between the verb and object"], "Clause 1, 而且 clause 2."),
        M("When 而且 connects two sentences, where does it go?", "At the start of the second sentence", ["At the end of the first", "In the middle of the first", "Nowhere"], "Sentence 1 + 而且 + Sentence 2."),
        M("What does 他会讲英语，而且讲得好 mean?", "He can speak English, and speaks it well", ["He cannot speak English", "He speaks English badly", "He teaches English"], "而且."),
        M("What does 天黑了，而且又下雨，别出去了 mean?", "It’s dark and raining again; don’t go out", ["It is bright", "Go out now", "It is hot"], "而且又下雨."),
        M("Why does the speaker seldom travel (example 6)?", "Few holidays and no money", ["Too many holidays", "No time to read", "Too much money"], "假期很少，而且我也没有钱."),
        M("What does the post office do in example 8?", "Expands its business and improves express delivery", ["Closes down", "Raises the stamp price", "Stops delivery"], "扩大了自己的业务."),
        M("According to Part 1, what do people care more about now?", "Which restaurant’s food is healthier and tastier", ["Which restaurant is closest", "The color of the bag", "The speed limit"], "更在乎哪家餐馆的饭更健康，更好吃."),
        M("Who rides motorbikes along China’s streets in Part 2?", "The delivery guys", ["The students", "The cooks", "The teachers"], "外卖小哥."),
        M("What does Zhang Hua say about breakfast in winter?", "She is the only meal she does not order", ["She orders it first", "She eats it at a restaurant", "She skips it"], "除了早饭，别的饭都是叫外卖."),
        F("他学习很好，___且对人很热情。", "而", PART, "而且."),
        F("点外卖价格不贵，既便宜___方便。", "又", PART, "既…又…."),
        F("人们不___可以在网上订餐，也可以用手机应用订餐。", "仅", PART, "不仅…也…."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration 1-3
G1 = table(["第一部分（视频前半段）"], [["美团外卖早晨集合"], ["外卖第一单"], ["外卖第二单"], ["别的订单"], ["午饭和聊天，外卖小哥为什么做这个工作"]],
           title="Activity 2, Group 1: first part of the video (the book gives the times 0:00 to 3:30)", say=[0])
G2 = table(["第二部分（视频后半段）"], [["个人体会"], ["下班高峰期送餐的麻烦"], ["意外的惊喜"], ["一天工作总结"]],
           title="Activity 2, Group 2: second part of the video (the book gives the times 3:31 to 9:14)", say=[0])
L7 = lesson(
    "Lesson 25 Presentation 1 skill integration: a dialog and two videos about food delivery",
    "小菜一碟 · 连歪果仁都开始在中国送外卖了 · 美团外卖早晨集合 · 外卖第一单 · 叫外卖的各种人",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Writing, Speaking and Reading)",
             "A. Listen to the dialog once through and answer the questions. 1. How are the two speakers related? 2. What are their dining preferences? 3. What do they decide to do together? 4. From the context, what does 小菜一碟 (xiǎocài yìdié) mean? (In Chinese it is a small side dish of food, used for “a piece of cake”: something very easy; the audio is not included, so this answer is mine.) B. Listen to the conversation again and fill in the table below using Chinese characters: Benefits of Service; What Can Be Ordered; Prices Mentioned; Mobile Apps; Payment; Delivery Time; How to Use Apps. C. Read your information to a partner, make any necessary changes or additions, then read it to the class. D. Read the script your teacher provides, then perform it with your partner. E. Pair up with a new partner and share your recent experiences ordering food delivery. (Two pictures and the audio are not included; the script is not in the book.)",
             examples=[D("这个小菜一碟。", "小菜一碟: a piece of cake, very easy. (sample line; mine)")]),
        card("Skill Integration, Activity 2 (Reading, Listening, Writing and Speaking)",
             "A. Form two groups. Group 1 watches the first part of the following video while Group 2 watches the second. Take notes and fill in your group’s part of the table below. The video title: 连歪果仁都开始在中国送外卖了！ B. Compare information with your teammates in Chinese. C. Pair off with the other group members. Read your information to your partner while they complete the rest of their table. D. In your own Chinese, retell this food delivery story to your partner. E. Watch the entire video again in class or as homework. (The video and two pictures are not included; the book writes 午饭 + 聊天 with a plus sign, which is written 午饭和聊天 here.)",
             tables=[G1, G2], examples=[D("连歪果仁都开始在中国送外卖了！", "Even foreigners have started delivering takeout in China! (the video title; “歪果仁” is slang for “外国人”, foreigners; the English is mine)")]),
        card("Skill Integration, Activity 3 (Reading, Listening, Writing and Speaking)",
             "A. Watch the video, 叫外卖的各种人. Take notes, then fill in the table below: 叫外卖的各种人 | Details (written in English), with eleven numbered rows. B. Compare information with a partner. C. In Chinese, tell the class how many types of people are mentioned in the video, and which type you are most like. (The video is not included; the table is blank in the book.)",
             examples=[D("叫外卖的各种人", "All kinds of people who order takeout (the video title; mine)")]),
    ],
    exercises=[
        M("What does 小菜一碟 mean from the context?", "A piece of cake, very easy", ["A small bowl of soup", "Too expensive", "A new dish"], "A small dish of food, so very easy."),
        M("Which is a title in the first video?", "连歪果仁都开始在中国送外卖了", ["叫外卖的各种人", "怎么点外卖", "外卖平台"], "The first video."),
        M("What does 歪果仁 stand for?", "外国人", ["中国人", "外卖小哥", "留学生"], "Slang for foreigners."),
        M("In which part of the video is 个人体会?", "The second part", ["The first part", "Both", "Neither"], "Group 2."),
        M("In which part is 外卖第一单?", "The first part", ["The second part", "Both", "Neither"], "Group 1."),
        M("Which row belongs to Group 2?", "意外的惊喜", ["外卖第二单", "别的订单", "美团外卖早晨集合"], "Group 2."),
        M("What does Activity 3 ask you to tell the class?", "How many types of people are mentioned and which you are most like", ["The price of takeout", "The name of the app", "The delivery time"], "Activity 3C."),
        M("Which video is about all kinds of customers?", "叫外卖的各种人", ["连歪果仁都开始在中国送外卖了", "美团外卖早晨集合", "一天工作总结"], "Activity 3."),
        F("连歪果仁___开始在中国送外卖了！", "都", PART, "连…都…."),
        F("美团外卖早晨集___", "合", PART, "集合: gather."),
    ],
)

# ------------------------------------------------------------------ 8. skill integration 4-5
TA = [("现在，越来越多的外国人喜欢住在中国，他们爱上中国有千百个理由，而便宜、方便的外卖美食却是吸引他们的一个非常重要的原因。许多在中国的外国人都说，中国的外卖又好吃又便宜，同时还可以保证按时送到，真是让人无法拒绝。", "1. More and more foreigners like living in China, and they have hundreds of reasons for loving China, but cheap and convenient takeout food is a very important reason that attracts them. Many foreigners in China say that China’s takeout is both tasty and cheap and is guaranteed to arrive on time, which really makes it impossible to refuse. (the book’s first paragraph; English mine)"),
      ("最近，有外国网友问：“为什么那么多人喜欢中国？”住在中国的外国人给出了各种答案，比如“出租车特别便宜”、“高速火车可通往任何一个地方”、“很安全，半夜出门都不必担心”、“二十四小时有地方可以吃饭”等等。但是，提到最多的还是方便的外卖平台和服务。", "2. Recently a foreign netizen asked: “Why do so many people like China?” Foreigners living in China gave all kinds of answers, such as “taxis are especially cheap,” “high-speed trains can go to any place,” “it is very safe, and you needn’t worry about going out in the middle of the night,” “there are places to eat twenty-four hours a day,” and so on. But the one mentioned most was the convenient takeout platforms and service. (the book writes 24 in digits)"),
      ("在中国，人们用手机应用软件和手机支付系统可以找到、订到各种美食，而且还总是能在预约时间内送到。这让很多外国人不能相信。", "3. In China, people can use phone apps and mobile payment systems to find and order all kinds of food, and it can always be delivered within the appointed time. This makes many foreigners unable to believe it."),
      ("另外，网络外卖平台上什么餐点都有、什么都不奇怪。有外国人订过云南汽锅鸡，有人订过烤鸭，带面皮、甜面酱，还有人订过麻辣火锅，不含锅。对于卖披萨、面条、水饺什么的，外国朋友说点那些餐太容易，不值得一提。", "4. Besides, online takeout platforms have every kind of dish and nothing is strange. Some foreigners have ordered Yunnan steam-pot chicken, some have ordered roast duck, with pancakes and sweet bean sauce, and some have ordered spicy hot pot, without the pot. As for those selling pizza, noodles, dumplings and so on, foreign friends say that ordering those is too easy to be worth mentioning. (the book puts the brackets around 带面皮、甜面酱 and 不含锅; they are turned into commas)"),
      ("对于在中国读书的众多外国留学生们，他们在宿舍内就可以吃到各省甚至各国的美食。外卖小哥会“用尽一切办法”把美食送到校园里。然后在接到食物的时候，再用手机一扫，钱就支付了。有时候外国留学生发现自己叫外卖还有打折，让他们非常惊讶。", "5. For the many international students studying in China, they can eat the food of every province and even every country in their dorms. Delivery guys will “use every means” to get the food to the campus. Then when you receive the food, you scan with your phone and the money is paid. Sometimes international students find that their takeout even has a discount, which surprises them very much."),
      ("一位美国来的朋友说，他已经在中国住了六年了，中国街头的各种美食多到让人数都数不过来，而价格却要比美国便宜得多。他还说，要是和朋友一起合点三个外卖中国菜，平均只要三到四点五美元，有时甚至只需要两美元。", "6. A friend from America said that he has already lived in China for six years, that the many kinds of food on China’s streets are too many to count, and that the prices are much cheaper than in America. He also said that if you order three Chinese takeout dishes together with friends, it only costs three to four and a half dollars on average, and sometimes as little as two dollars. (the book writes 6, 3, 4.5 and 2 in digits)"),
      ("食物既能够准时送达，又好吃，而且也不像在美国那样需要另外给小费，这真是让在中国的外国人感到开心极了。", "7. The food can be delivered on time and is tasty, and you don’t have to tip separately as in America, which really makes foreigners in China extremely happy. (the book’s last paragraph)")]
AQ4 = [("第一段讲外国人喜欢住在中国，外卖是一个重要的原因。", "1. The first paragraph is about foreigners liking to live in China, with takeout an important reason. (my answer)"),
       ("最后一段讲在中国点外卖准时、好吃，而且不用给小费。", "2. The last paragraph is about takeout in China being on time and tasty, with no tip. (my answer)"),
       ("文章的主要内容是外国人为什么喜欢中国的外卖。", "3. The main content of the article is why foreigners like China’s takeout. (my answer)")]
MI = [("第二段：外国人说喜欢中国的原因，提到最多的是外卖。", "Paragraph 2 (mine): the reasons foreigners give for liking China; the one mentioned most is takeout."),
      ("第三段：手机应用和手机支付让人订到各种美食，还能按时送到。", "Paragraph 3 (mine): phone apps and mobile payment let people order all kinds of food, delivered on time."),
      ("第四段：外卖平台上什么餐点都有，披萨和面条太容易，不值得一提。", "Paragraph 4 (mine): the platforms have every dish; pizza and noodles are too easy to mention."),
      ("第五段：留学生在宿舍就能吃到各地美食，扫一扫就付款，有时还打折。", "Paragraph 5 (mine): students eat food from everywhere in the dorm, pay with a scan, and sometimes get discounts."),
      ("第六段：美国朋友说中国美食多，价格比美国便宜得多。", "Paragraph 6 (mine): the American friend says China has lots of food and prices are much lower than in the US.")]
JR = [("我在上海交通大学读了四年书，就用了三年的“饿了么”。可以说，我的生活不能没有“饿了么”。", "I studied for four years at Shanghai Jiao Tong University and used Ele.me for three. It can be said that my life cannot do without Ele.me."),
      ("那么，对于我和我的同学们来说，“饿了么”是什么呢？答案就是“我们饿了，懒得去食堂吃饭；或者因为玩游戏、考试、睡过头等等各种原因错过了食堂的饭点，不得不叫外卖；或者更直接，不想吃食堂的饭了，就叫外卖。”", "So for me and my classmates, what is Ele.me? The answer is: “We are hungry and too lazy to go to the canteen; or, for all kinds of reasons such as playing games, exams or oversleeping, we missed the canteen’s mealtime and have to order takeout; or, more directly, we don’t want to eat canteen food any more, so we order takeout.”"),
      ("所以，我们用“饿了么”非常简单。一般来说，大家用了几年后，都有自己喜欢的餐厅了，直接点开“饿了么”的应用，选餐厅，下单，关窗口，前后一分钟搞定。对于我们来说，“饿了么”就是一个快速订餐网站，因为我们都是饿了的时候去订餐的，感觉好像已经快饿死了的样子，所以总想以最快的速度完成订餐、下单、付款的操作。然后，第一时间可以拿到饭，赶紧吃了。", "So using Ele.me is very simple for us. Generally, after using it for a few years everyone has favorite restaurants, so they directly open the Ele.me app, choose the restaurant, place the order and close the window, all done in a minute. To us Ele.me is a quick food-ordering website, because we order when we are hungry, feeling as if we are starving, so we always want to complete ordering, placing the order and paying as fast as possible. Then we can get the food right away and eat it quickly."),
      ("我们不饿的时候都去玩别的网站。吃，很吸引我们大学生，但外卖，就显然只有饿了的时候才吸引我们。因此，我们不会花费大量的时间在平台上比较商家的价格和饭菜。但是，有时我们也会关注哪家新店开了，有团购，比如火锅啊，烧烤啊之类的，或者新开的蛋糕店啊，有打折啊等等。", "When we are not hungry we all go and play on other websites. Eating attracts us university students, but takeout obviously attracts us only when we are hungry. So we don’t spend a lot of time on the platform comparing merchants’ prices and dishes. But sometimes we also pay attention to which new shop has opened and has group-buy deals, such as hot pot or barbecue, or a newly opened cake shop with discounts and so on. (the book’s English heading is “journal entry”; the English is mine)")]
TF = [("“饿了么”对作者来说很重要，他四年大学期间都在用。", "1. Ele.me is very important to the author, and he used it for all four years at university. — False (mine): he used it for three of the four years."),
      ("作者和他的同学们觉得用“饿了么”比较麻烦，需要比较很多餐厅。", "2. The author and his classmates find Ele.me troublesome and need to compare many restaurants. — False (mine): it is very simple and takes a minute."),
      ("大部分的时间大家只有饿的时候才用“饿了么”。", "3. Most of the time people use Ele.me only when they are hungry. — True (mine)."),
      ("“饿了么”既可以满足大家吃的需要，也可以满足大家玩的需要。", "4. Ele.me can satisfy people’s needs to eat and also to play. — False (mine): when not hungry they go and play on other websites.")]
AN5 = [("因为我们饿了，懒得去食堂吃饭，或者错过了食堂的饭点，或者不想吃食堂的饭。", "5B-1, reasons for using Ele.me (mine): because we are hungry and too lazy to go to the canteen, or missed its mealtime, or don’t want canteen food."),
       ("因为他们饿的时候想最快地完成订餐、下单、付款，第一时间拿到饭。", "5B-2, why a quick ordering website (mine): because they order when hungry and want to finish ordering, placing the order and paying as fast as possible and get the food right away."),
       ("他们不饿的时候去玩别的网站，只是有时关注新店、团购和打折。", "5B-3, what they do when not hungry (mine): they play on other websites, only sometimes paying attention to new shops, group buys and discounts.")]
L8 = lesson(
    "Lesson 25 Presentation 1 skill integration: foreigners and Chinese takeout; an Ele.me journal",
    "越来越多的外国人喜欢住在中国 · 外卖美食 · 云南汽锅鸡 · 不用给小费 · 上海交通大学 · 饿了么 · 懒得去食堂",
    requires=[],
    cards=[
        card("Skill Integration, Activity 4 (Reading, Speaking, Listening and Writing)",
             "A. Pair up. Read the first paragraph in the news article below while your partner reads the last. Answer your respective questions, share information, then discuss what you think the main content of the article covers: 1. What is the first paragraph about? 2. What is the last paragraph about? 3. What do you think the main content of the article covers? B. Share your conclusions with the class. C. Divide into two groups. Group 1 reads paragraphs two to four while Group 2 reads paragraphs five and six. Write the main idea of each paragraph and its EEIs in tables (Paragraph | Topic and Details), then share your information with your teammates. D. Pair off with the other group, exchange information about your paragraphs in Chinese, then complete your table with your partner’s information. E. Write three new words from the article with their English meanings. (Three pictures are not included.) The seven paragraphs, with my English:",
             examples=[D(z, e) for z, e in TA]),
        card("Activity 4: my answers", "The book leaves the answers and tables blank; these are mine.", examples=[D(z, e) for z, e in AQ4 + MI]),
        card("Skill Integration, Activity 5 (Reading, Writing, Speaking and Listening)",
             "A. Read the entry from a college student’s journal below, then mark the following statements as true or false: 1. “饿了么”对作者来说很重要，他四年大学期间都在用。 2. 作者和他的同学们觉得用“饿了么”比较麻烦，需要比较很多餐厅。 3. 大部分的时间大家只有饿的时候才用“饿了么”。 4. “饿了么”既可以满足大家吃的需要，也可以满足大家玩的需要。 Compare answers with a partner. B. Form groups of three. Write your answer to the first question in the table while your teammates answer the other two: 作者和同学用“饿了么”的原因 / 为什么作者说“饿了么”是个快速订餐网站？ / 不饿的时候，学生们在“饿了么”上做什么？ Read your answer to your teammates, complete the table with their answers, then read all three answers to the class. C. Write down the reasons why you like or dislike ordering delivery in the table (我喜欢点外卖的原因), then read them to your teammates. (Two pictures are not included.)",
             examples=[D(z, e) for z, e in JR]),
        card("Activity 5A: my true or false keys", "The book gives no key; the keys are mine.", examples=[D(z, e) for z, e in TF]),
        card("Activity 5B: my answers", "The book’s table is blank; the answers are mine.", examples=[D(z, e) for z, e in AN5]),
    ],
    exercises=[
        M("What is the main reason foreigners like living in China, in the first paragraph?", "Cheap, convenient takeout food", ["High salaries", "Cold winters", "Cheap rent"], "便宜、方便的外卖美食."),
        M("What is mentioned most in paragraph two?", "The convenient takeout platforms and service", ["Taxis", "High-speed trains", "Safety"], "提到最多的还是方便的外卖平台和服务."),
        M("What did a foreigner order that was without the pot?", "Spicy hot pot", ["Roast duck", "Pizza", "Dumplings"], "麻辣火锅，不含锅."),
        M("How do students pay when they receive the food?", "They scan with their phone", ["With cash", "With a check", "They pay later"], "再用手机一扫，钱就支付了."),
        M("How long has the American friend lived in China?", "Six years", ["Two years", "Three years", "Ten years"], "住了六年了."),
        M("What does the last paragraph say you don’t need in China?", "To tip separately", ["To pay by phone", "To order early", "To wait"], "不需要另外给小费."),
        M("How many years did the author use Ele.me?", "Three", ["Four", "One", "Ten"], "用了三年."),
        M("Is it true that the author used Ele.me for all four years?", "No, he used it for three", ["Yes, all four years", "No, only one year", "Yes, five years"], "Statement 1 is false."),
        M("When do the students use Ele.me?", "Only when they are hungry", ["All day", "Only in exams", "Never"], "只有饿的时候."),
        M("What do they do when they are not hungry?", "Play on other websites", ["Study", "Order dessert", "Cook"], "去玩别的网站."),
        F("中国街头的各种美食多到让人数都___不过来。", "数", PART, "数 here is shǔ."),
        F("我们饿了，___得去食堂吃饭。", "懒", PART, "懒得: too lazy to."),
        F("同时还可以保证按时送到，真是让人无法___绝。", "拒", PART, "无法拒绝: cannot refuse."),
    ],
)

# ------------------------------------------------------------------ 9. using Chinese in context
UC1 = table(["在美国点外卖"], [["在美国怎么点外卖"], ["好用的应用软件和怎么用"], ["外卖平台上好吃的饭菜"], ["在美国点外卖和在中国点外卖的不同"], ["在美国点外卖需要注意的事情"]],
            title="Activity 1B: discuss the answers with your partner (the book’s “&” is written 和)", say=[0])
UC1S = [("在美国点外卖也很方便，你可以在手机上下载一个应用软件，选餐馆，点餐，然后下单。", "Sample (mine): Ordering takeout in the US is also very convenient: download an app on your phone, choose a restaurant, order dishes, then place the order."),
        ("在美国点外卖，除了饭钱以外，还要给外卖小哥小费。", "Sample (mine): When ordering takeout in the US, besides the price of the food, you also have to tip the delivery person."),
        ("在中国，外卖平台上什么饭都可以点，而且价格不贵。", "Sample (mine): In China you can order any food on the takeout platforms, and the prices are not high.")]
UC2S = [("我喜欢叫外卖，因为外卖又快又方便，而且不用洗碗。", "Group 1 sample (mine): I like ordering takeout, because it is fast and convenient and you don’t have to wash dishes."),
        ("我喜欢去餐馆吃饭，因为餐馆的饭菜新鲜，而且可以跟朋友聊天。", "Group 2 sample (mine): I like eating in restaurants, because the food is fresh and you can chat with friends."),
        ("我喜欢在家做饭，因为自己做的饭更有营养，而且不贵。", "Group 3 sample (mine): I like cooking at home, because the food you make yourself has more nutrition, and it is not expensive.")]
RULES = table(["回合", "内容"], [["第一轮", "Each group explains the advantages of their preference."], ["第二轮", "Each group explains the disadvantages of the other preferences."], ["第三轮", "Rebut your rivals’ arguments."]],
              title="Activity 2D: debate rules (the book prints them in English as First Round, Second Round and Third Round; the Chinese round names are mine)", say=[0])
L9 = lesson(
    "Lesson 25 Presentation 1 using Chinese in context: takeout in the US and dining preferences",
    "在美国点外卖 · 好用的应用软件 · 在美国和在中国点外卖的不同 · 叫外卖 在外面吃 在家做饭 · 辩论",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Pair up. You and a friend are hired by an online Chinese forum to explain food delivery service in the U.S., what apps to use, and other things customers should know. You may watch a video on YouTube for reference. B. Discuss the answers of the following questions with your partner in the table below. C. Using your answers, create a PPT presentation together or divvy up the task. D. Present your slides to the class in Chinese before you upload them to the forum. (Three pictures and the video are not used.) Three sample sentences, mine:",
             tables=[UC1], examples=[D(z, e) for z, e in UC1S]),
        card("Using Chinese in Context, Activity 2 (Writing, Speaking and Listening)",
             "A. Fill in the table below on dining habits and preferences. Write in Chinese characters. The rows are Self, Family and Americans; the columns are Who, Dining Habits/Preferences and Reasons. B. Read your information to a partner. C. Form three groups based on your dining preferences, if possible. Prepare for a debate on why your preference is the best by filling out the relevant table below in Chinese. Group 1: Ordering Delivery Service (Advantages; Disadvantages of Dining Out; Disadvantages of Home Cooking). Group 2: Dining Out (Advantages; Disadvantages of Delivery Service; Disadvantages of Home Cooking). Group 3: Home Cooking (Advantages; Disadvantages of Delivery Service; Disadvantages of Dining Out). D. Now debate according to the following rules. E. Your teacher will decide the winner, explain why, and give feedback on your debate performance. (Three pictures are not included.) One sample first-round sentence for each group, mine:",
             tables=[RULES], examples=[D(z, e) for z, e in UC2S]),
    ],
    exercises=[
        M("What are you and a friend hired to do in Activity 1?", "Explain US food delivery to a Chinese forum", ["Open a restaurant", "Teach cooking", "Deliver food"], "Using Chinese in Context, Activity 1."),
        M("What do you create in Activity 1C?", "A PPT presentation", ["A menu", "A poster", "A video"], "Activity 1C."),
        M("Who do you present your slides to?", "The class, before uploading to the forum", ["The restaurant", "A delivery guy", "Nobody"], "Activity 1D."),
        M("What are the three dining preferences in the debate?", "Ordering delivery, dining out and home cooking", ["Breakfast, lunch and dinner", "Chinese, French and Italian", "Cheap, fast and fresh"], "Three groups."),
        M("What happens in the first round?", "Each group explains the advantages of its preference", ["Each group rebuts rivals", "The teacher chooses", "Nobody speaks"], "第一轮."),
        M("What happens in the third round?", "You rebut your rivals’ arguments", ["You list advantages", "You order food", "You choose the winner"], "第三轮."),
        M("Who decides the winner?", "The teacher", ["The students", "The restaurant", "A delivery guy"], "Activity 2E."),
        M("Which sample sentence argues for home cooking?", "我喜欢在家做饭，因为自己做的饭更有营养", ["我喜欢叫外卖，因为又快又方便", "我喜欢去餐馆吃饭，因为可以聊天", "我不喜欢吃饭"], "Group 3."),
        F("在美国点外卖，除了饭钱以外，还要给外卖小哥小___。", "费", PART, "小费: tip."),
        F("我喜欢叫外卖，因为外卖又快又方便，___且不用洗碗。", "而", PART, "而且."),
    ],
)

# ------------------------------------------------------------------ 10. vocabulary
L10 = vocab_lesson("Lesson 25 Presentation 1 vocabulary", "21 words from the book’s Presentation 1 list",
                   "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第二十五课 Presentation 1: 外卖, 吗的反问, 除了, 先…然后…最后, 而且", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
