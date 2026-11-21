"""Unit 72: Lesson 24 (Unit 4 review), the skills integration review, part 1, from the book's texts: Jack asks about the high-speed train, Mark sends a
package, Wang Wen sees Dr. Zhang, and three conversations about directions, each with its script. Audio and pictures are not included; numbers the book
writes as digits are spelled out; the tables, answers and true/false keys that the book leaves blank are mine and labeled. The book's 嗯 is left out."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('还是', 0, 'hai2'), ('还得', 0, 'hai2'), ('还可以', 0, 'hai2'), ('还没', 0, 'hai2'), ('还不好', 0, 'hai2'), ('还脸', 0, 'hai2'), ('还算', 0, 'hai2'), ('还需要', 0, 'hai2'), ('还有', 0, 'hai2'), ('得坐坐', 0, 'dei3'), ('得需要', 0, 'de5'), ('还得需要', 1, 'dei3'), ('得两三', 0, 'dei3'), ('还得看', 1, 'dei3'), ('得付', 0, 'dei3'), ('得先坐', 0, 'dei3'), ('得多', 0, 'de5'), ('贵得多', 1, 'de5'), ('快多了', 0, 'kuai4'), ('跳动得', 2, 'de5'), ('得的是', 0, 'de2'), ('得肺炎', 0, 'de2'), ('得到', 0, 'de2'), ('你得先', 1, 'dei3'), ('得多', 0, 'de5'), ('长假', 0, 'chang2'), ('得一', 0, 'de5'), ('得很', 0, 'de5'), ('跳得', 1, 'de5'), ('没量', 1, 'liang2'), ('得多少', 0, 'dei3')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. activity 1: the high-speed train
J1 = [("杰克", "张华，五一长假的时候，我想去上海玩几天。你觉得我是坐飞机呢还是坐高铁？", "Jack: Zhang Hua, during the May Day holiday I want to go to Shanghai for a few days. Do you think I should fly or take the high-speed train?"),
      ("张华", "一般来说，坐飞机快一些。但是加上去机场和安检，时间和坐高铁差不多。另外，高铁站都在市区，车次也多，非常方便。所以很多中国人更喜欢坐高铁。", "Zhang Hua: Generally speaking, flying is a bit faster. But once you add the trip to the airport and the security check, the time is about the same as the high-speed train. Besides, high-speed train stations are all in the city and there are more trains, so it is very convenient. So many Chinese people prefer the high-speed train."),
      ("杰克", "这样啊，那我得坐坐高铁了。对了，从北京坐高铁到上海需要几个小时？", "Jack: I see, then I have to try the high-speed train. By the way, how many hours does it take from Beijing to Shanghai?"),
      ("张华", "从北京到上海最快只要四个半小时，最慢也不超过六个小时。", "Zhang Hua: From Beijing to Shanghai it takes only four and a half hours at the fastest and no more than six hours at the slowest."),
      ("杰克", "那么快啊？坐在车上稳不稳呢？我有点担心安全。", "Jack: That fast? Is it steady sitting on the train? I am a bit worried about safety."),
      ("张华", "中国的高铁非常安全，而且特别平稳。", "Zhang Hua: China’s high-speed trains are very safe, and especially smooth."),
      ("杰克", "高铁上有什么样的座位？", "Jack: What kinds of seats are there on the high-speed train?"),
      ("张华", "有一等座、二等座，还有商务座和特等座。一等座和二等座的座位又分硬座和软座。", "Zhang Hua: There are first class and second class, and also business class and premium class. The first- and second-class seats are further divided into hard seats and soft seats."),
      ("杰克", "那票价贵不贵？", "Jack: Then are the tickets expensive?"),
      ("张华", "一等座、二等座的座位便宜一些，商务座和特等座稍微贵一些。", "Zhang Hua: First- and second-class seats are cheaper; business and premium class are somewhat more expensive."),
      ("杰克", "我该怎么买票呢？去高铁站吗？", "Jack: How should I buy a ticket? Do I go to the station?"),
      ("张华", "不用。现在买票特别容易，你可以在高铁网上订票，或是下载一个订票应用软件，在手机上就可以订。因为你是个老外，订票的时候还得需要你的护照号码。", "Zhang Hua: No need. Buying tickets is especially easy now; you can book on the high-speed rail website, or download a booking app and book on your phone. Because you are a foreigner you will also need your passport number when booking."),
      ("杰克", "高铁上的服务怎么样？", "Jack: How is the service on the train?"),
      ("张华", "高铁上的服务跟飞机上的服务差不多一样，可以说是一流的。服务员特别有礼貌也很热情。另外，他们也有餐车和售货车服务，什么吃的、喝的都有。", "Zhang Hua: The service on the train is about the same as on a plane; you could say it is first-rate. The attendants are especially polite and very friendly. Also there is a dining car and a sales cart, with every kind of food and drink."),
      ("杰克", "他们的设施怎么样？", "Jack: How are the facilities?"),
      ("张华", "高铁上的设施也非常先进。他们不仅有宽敞、舒适的座位，而且还可以无线上网。每节车厢都有热水器，卫生间也非常干净。", "Zhang Hua: The facilities are also very advanced. They have not only spacious, comfortable seats but also wireless internet. Every car has a water heater and the toilets are very clean."),
      ("杰克", "听你这么说，我都等不及要去体验一下了。今天晚上我就买票。", "Jack: Hearing you say that, I can’t wait to try it. I’ll buy my ticket tonight.")]
TB = table(["项目", "内容 (my answers)"], [["飞机和高铁相比", "飞机快一些；加上去机场和安检，时间差不多；高铁站在市区，车次多"], ["北京到上海需要的时间", "最快四个半小时，最慢不超过六个小时"], ["座位", "一等座，二等座，商务座，特等座；一等座二等座分硬座和软座"], ["票价", "一等座二等座便宜一些，商务座特等座稍微贵一些"], ["买票", "高铁网上订票；下载订票应用软件，在手机上订；订票需要护照号码"], ["车上的服务", "跟飞机差不多，一流；服务员有礼貌，热情；有餐车和售货车"], ["车上的设施", "宽敞舒适的座位；无线上网；每节车厢有热水器；卫生间干净"]],
           title="Activity 1B: the table about China’s high-speed trains (the book leaves it blank; the contents are mine, from the script)", say=[0, 1])
L1 = lesson(
    "Lesson 24 Skills Integration Review: Jack asks about the high-speed train",
    "坐飞机还是坐高铁 · 北京到上海 · 座位 票价 · 订票 · 服务 设施",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "A. Listen to the dialog once and answer the questions: 1. What’s the male speaker’s plan? 2. Is he familiar with China? How do you know? 3. What is his concern? 4. What do you think he will do tonight? (audio and four pictures, not included) B. Listen to the dialog again and complete the table with details about high-speed trains in China. Write your answers in Pinyin or Chinese characters. Then share your answers with your partners in groups of three. C. Read the script together and check your answers. D. If anyone in class has travelled by train, they should share their experience with the class.",
             tables=[TB]),
        card("Script: 杰克问高铁", "The book writes the numbers in digits; here they are spelled out. The translations are mine.", examples=dlg(J1)),
    ],
    exercises=[
        M("When does Jack want to go to Shanghai?", "During the May Day holiday", ["During National Day", "In summer", "At New Year"], "五一长假."),
        M("Why do many Chinese prefer the high-speed train?", "Stations are in the city, many trains, convenient", ["It is free", "It is the only way", "It is slower"], "高铁站都在市区，车次也多."),
        M("How long does the trip from Beijing to Shanghai take at the fastest?", "Four and a half hours", ["Two hours", "Six hours", "Ten hours"], "最快只要四个半小时."),
        M("What is Jack worried about?", "Safety", ["Price", "Luggage", "Food"], "我有点担心安全."),
        M("Which seat is NOT mentioned?", "Sleeper seat", ["First class", "Business class", "Premium class"], "一等座，二等座，商务座，特等座."),
        M("Which seats are cheaper?", "First and second class", ["Business and premium", "All the same", "Only premium"], "一等座、二等座便宜一些."),
        M("Why does Jack need his passport number?", "He is a foreigner booking a ticket", ["He is going abroad", "He is paying cash", "He is a student"], "你是个老外，订票的时候还得需要护照号码."),
        M("How is the service on the high-speed train?", "About the same as on a plane, first-rate", ["Much worse than on a plane", "There is none", "Only a sales cart"], "差不多一样，一流."),
        M("Which facility is NOT mentioned?", "A swimming pool", ["Wireless internet", "Water heaters", "Clean toilets"], "无线上网, 热水器, 卫生间."),
        M("When will Jack buy his ticket?", "Tonight", ["Tomorrow", "Next week", "Never"], "今天晚上我就买票."),
        F("那我___坐坐高铁了。", "得", ["的", "地", "了"], "得 (děi): have to."),
        F("订票的时候___得需要你的护照号码。", "还", ["再", "又", "也"], "还得: also have to."),
    ],
)

# ------------------------------------------------------------------ 2. activity 2: the post office
J2 = [("马克", "您好，我有个包裹要寄到洛杉矶给我的父母。", "Mark: Hello, I have a package to send to my parents in Los Angeles."),
      ("营业员", "你想怎么寄？寄普通包裹还是特快专递？", "Clerk: How do you want to send it? A regular package or express mail?"),
      ("马克", "普通包裹和特快专递有什么不同？", "Mark: What is the difference between a regular package and express mail?"),
      ("营业员", "一般来说，特快专递比普通包裹贵得多，不过也快多了。特快专递一个星期就可以寄到，但是普通包裹得两三个星期。", "Clerk: Generally speaking, express mail is much more expensive than a regular package, but also much faster. Express mail can arrive in a week, but a regular package takes two or three weeks."),
      ("马克", "特快专递得多少钱？", "Mark: How much does express mail cost?"),
      ("营业员", "要看你的包裹有多重？另外，还得看你寄什么东西，要不要买保险？", "Clerk: It depends on how heavy your package is. Also it depends on what you send and whether you want insurance."),
      ("马克", "我给我父母买了一些中国的茶叶，一套茶具和两条围巾。", "Mark: I bought my parents some Chinese tea leaves, a tea set and two scarves."),
      ("营业员", "来，先让我称一下你的包裹。看来茶具挺重的，你的包裹有点超重。", "Clerk: Come, let me weigh your package first. It seems the tea set is quite heavy; your package is a bit overweight."),
      ("马克", "特快专递的邮费是多少？", "Mark: How much is the postage for express mail?"),
      ("营业员", "按你包裹的重量，现在邮费是四百二十块。还有，因为茶具是易碎物品，我觉得你最好买个保险。", "Clerk: By the weight of your package, the postage is now 420 yuan. Also, because the tea set is a fragile item, I think you had better buy insurance."),
      ("马克", "保险费是多少？", "Mark: How much is the insurance?"),
      ("营业员", "保险费差不多一百八十六块。", "Clerk: The insurance is about 186 yuan."),
      ("马克", "我还需要买二十张五毛的邮票。一共多少钱？", "Mark: I also need to buy twenty five-mao stamps. How much is it altogether?"),
      ("营业员", "邮费加上保险费一共六百零六块，再加上邮票十块，你得付六百一十六块。现在，请你先填一下包裹单和海关申报单。", "Clerk: Postage plus insurance is 606 yuan altogether, plus 10 yuan for the stamps, so you have to pay 616 yuan. Now, please fill in the package form and the customs declaration form first."),
      ("马克", "好的。对了，我怎么追踪我的包裹寄到哪儿了？", "Mark: OK. By the way, how do I track where my package has got to?"),
      ("营业员", "我们会给你一个代码，你只要用手机扫描一下，就可以看到包裹到什么地方了。", "Clerk: We will give you a code; just scan it with your phone and you can see where the package has got to."),
      ("马克", "这倒是很方便。好了，包裹单填好了。我怎么付费？", "Mark: That is actually very convenient. All right, the package form is filled in. How do I pay?"),
      ("营业员", "你可以付现金，信用卡或是手机支付。手机支付最方便。", "Clerk: You can pay cash, by credit card or by mobile payment. Mobile payment is the most convenient."),
      ("马克", "好的，我用微信支付吧。可以给我一张收据吗？", "Mark: OK, I’ll use WeChat Pay. Can you give me a receipt?"),
      ("营业员", "你不需要打印收据，在微信支付上你会看到一张电子收据，非常方便保存和查看。", "Clerk: You don’t need to print a receipt; in WeChat Pay you will see an electronic receipt, very convenient to save and look up."),
      ("马克", "在中国寄包裹真是太容易了。谢谢你！", "Mark: Sending a package in China is really too easy. Thank you!"),
      ("营业员", "不客气。再见！", "Clerk: You’re welcome. Goodbye!")]
L2 = lesson(
    "Lesson 24 Skills Integration Review: Mark sends a package to Los Angeles",
    "普通包裹 特快专递 · 保险 · 包裹单 海关申报单 · 微信支付 · 电子收据",
    requires=[],
    cards=[
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the dialog once and answer the questions. Share your answers with a partner. 1. Where does the conversation take place? 2. What does the first speaker want to do? 3. What method did the first speaker choose? 4. What’s the first speaker’s impression of the whole process? Why does he think so? B. Listen to the dialog again and choose the best answer for each of the seven multiple-choice questions (they are the exercises below). Then, share your answers with a partner. C. Read the script and compare it with the information you received. (Audio and picture, not included.)"),
        card("Script: 马克在邮局", "The book writes the amounts in digits (420, 186, 20 张 5 毛, 606, 10, 616); here they are spelled out. The translations are mine.", examples=dlg(J2)),
    ],
    exercises=[
        M("1. Which of the following is NOT a difference between express and regular mail?", "Express mail is safer", ["Express mail is faster", "Express mail is more expensive", "Express mail can be delivered within a week"], "Safer is not mentioned."),
        M("2. How is the postage for express mail calculated?", "By the weight, the items and the insurance", ["By the number of items only", "By whom you send it to", "By the city only"], "要看你的包裹有多重，寄什么东西，要不要买保险."),
        M("3. What is NOT in the package?", "Chinese alcohol", ["Tea leaves", "Scarves", "A tea set"], "茶叶, 茶具, 围巾."),
        M("4. Why should Mark buy insurance?", "The package contains fragile items", ["It is too heavy", "It is too expensive", "It is too big"], "茶具是易碎物品."),
        M("5. How much must Mark pay altogether?", "616 yuan", ["186 yuan", "420 yuan", "606 yuan"], "六百一十六块."),
        M("6. What form does Mark need to fill out?", "A customs claim form and a package form", ["A package form and a return slip", "A customs claim form and a return slip", "A package form and a registered mail slip"], "包裹单和海关申报单."),
        M("7. How will Mark pay?", "WeChat Pay", ["Cash", "Credit card", "Alipay"], "我用微信支付吧."),
        M("Where does the conversation take place?", "In a post office", ["In a bank", "In a hotel", "In a school"], "邮局."),
        M("How long does express mail take?", "About a week", ["Two or three weeks", "One day", "Three months"], "一个星期就可以寄到."),
        M("How does Mark track his package?", "Scan a code with his phone", ["Call every day", "Visit the post office", "Ask a friend"], "用手机扫描一下."),
        F("特快专递比普通包裹贵___多。", "得", ["的", "地", "了"], "贵得多: much more expensive."),
        F("你不需要打印收据，在微信支付上你会看到一张电子___据。", "收", ["发", "拿", "买"], "收据: receipt."),
    ],
)

# ------------------------------------------------------------------ 3. activity 3: seeing the doctor
J3 = [("病人", "张大夫吗？您好，我是跟您约好看病的王文。", "Patient: Dr. Zhang? Hello, I am Wang Wen, who made an appointment to see you."),
      ("医生", "好的。请坐，你哪儿不舒服？", "Doctor: Good. Please sit down. What is wrong?"),
      ("病人", "我两天前开始咳嗽，流鼻涕，就去药店买了一些感冒药，吃了两天。但是昨天晚上开始发烧、口干，而且头也有点晕。今天早上感觉特别没有力气。", "Patient: Two days ago I started coughing and had a runny nose, so I went to a pharmacy, bought some cold medicine and took it for two days. But last night I started running a fever, my mouth was dry, and my head was a bit dizzy too. This morning I felt especially weak."),
      ("医生", "你发烧多少度？", "Doctor: How high was your fever?"),
      ("病人", "昨晚三十八度五。今天早上还没量。", "Patient: Thirty-eight point five last night. I haven’t taken it yet this morning."),
      ("医生", "那，现在我先给你量一下体温。三十九度，发高烧。", "Doctor: Then let me take your temperature now. Thirty-nine degrees, a high fever. (the book has 嗯 before the number; it is left out in the Chinese)"),
      ("病人", "怪不得我觉得热，还脸红。", "Patient: No wonder I feel hot and my face is red."),
      ("医生", "让我听听你的心脏、量量血压。", "Doctor: Let me listen to your heart and take your blood pressure."),
      ("病人", "都正常吗？", "Patient: Is it all normal?"),
      ("医生", "心脏跳动得有点快，但还算正常。血压很稳定。让我看一下你的嗓子。", "Doctor: Your heart is beating a bit fast, but it still counts as normal. Your blood pressure is stable. Let me look at your throat."),
      ("病人", "啊……", "Patient: Ahh… (the patient opens his mouth; the book marks this with 张口 in brackets)"),
      ("医生", "你嗓子肿了。现在看来你得的是流感。", "Doctor: Your throat is swollen. From what I can see you have the flu."),
      ("病人", "严重吗？", "Patient: Is it serious?"),
      ("医生", "不算轻。今天先打一针，再开点儿药吃一吃。三天后要是还不好，就再去验血、验尿和透视，希望不要转成肺炎。", "Doctor: It is not light. Today first an injection, then I will prescribe some medicine for you to take. If in three days it is still not better, then go for a blood test, a urine test and an X-ray; I hope it doesn’t turn into pneumonia."),
      ("病人", "我可不想得肺炎。张大夫，你开的药我怎么吃？", "Patient: I definitely don’t want pneumonia. Dr. Zhang, how should I take the medicine you prescribed?"),
      ("医生", "一天三次，一次两片。最好早晚和中午各吃一次。用温开水服用。", "Doctor: Three times a day, two tablets each time. Best once each in the morning, at noon and in the evening. Take it with warm water."),
      ("病人", "我可以去上班吗？", "Patient: Can I go to work?"),
      ("医生", "最好在家休息。多喝热水，少动，不要外出。按时吃药。", "Doctor: It is best to rest at home. Drink more hot water, move less and don’t go out. Take your medicine on time."),
      ("病人", "好的。我去哪儿打针和取药？", "Patient: OK. Where do I go for the injection and to pick up the medicine?"),
      ("医生", "药房，就在一楼大厅的左边。打针在二楼输液室的旁边。", "Doctor: The pharmacy is right on the left of the first-floor hall. The injection is next to the infusion room on the second floor."),
      ("病人", "谢谢您，张大夫。", "Patient: Thank you, Dr. Zhang.")]
TD = table(["项目", "内容 (my answers)"], [["病人的症状", "咳嗽，流鼻涕，发烧，口干，头晕，没有力气"], ["医生做的检查", "量体温（三十九度），听心脏，量血压，看嗓子（肿了）"], ["诊断", "流感"], ["治疗", "打一针；开药，一天三次，一次两片，用温开水服用"], ["以后的检查", "三天后要是还不好，验血、验尿、透视"], ["医生的建议", "最好在家休息，多喝热水，少动，不要外出，按时吃药"]],
           title="Activity 3D: the table of the visit (the book leaves it blank; the contents are mine, from the script)", say=[0, 1])
TFS = [("病人吃了一些自己买的药，感觉好多了。", "1. False: the patient took cold medicine for two days but started running a fever last night. (key mine)"),
       ("病人早上量了体温，是三十八度五。", "2. False: 38.5 was last night; this morning he had not measured yet, and the doctor then found 39. (mine)"),
       ("病人的心脏跳得有点快，但是血压很稳定。", "3. True: the heart beats a bit fast but counts as normal, and the blood pressure is stable. (mine)"),
       ("病人的病三天后会转成肺炎。", "4. False: the doctor only hopes it will not turn into pneumonia. (mine)"),
       ("病人可以在一楼取药，二楼输液室打针。", "5. True: the pharmacy is in the first-floor hall and the injection is beside the second-floor infusion room. (mine)")]
L3 = lesson(
    "Lesson 24 Skills Integration Review: Wang Wen sees Dr. Zhang",
    "咳嗽 流鼻涕 发烧 · 量体温 听心脏 · 流感 肺炎 · 一天三次一次两片 · 药房 输液室",
    requires=[],
    cards=[
        card("Activity 3 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the first part of the dialog and answer the questions: 1. What’s the first speaker asking about? 2. What did the first speaker do before she arrived? 3. According to the second speaker, what did the first speaker need to do? List three details. 4. What is said in the dialog about the doctor? List three details. (audio and pictures, not included) B. Share your answers with your partner. C. Listen to the second part of the dialog and decide whether the following statements are True or False. D. Listen to the conversation again and complete the table with details in Pinyin or Chinese characters. E. Share your answers in groups of three. F. Read the script and check if you have questions. Act out the dialog if time permits.",
             examples=[D(z, e) for z, e in TFS],
             tables=[TD]),
        card("Script: 看病", "The book writes the temperatures as 38 度 5 and 39 度; here they are spelled out. The translations are mine.", examples=dlg(J3)),
    ],
    exercises=[
        M("What did the patient do first when the cough started?", "Bought cold medicine", ["Went to the hospital", "Stayed in bed", "Called the doctor"], "去药店买了一些感冒药."),
        M("What was last night’s temperature?", "38.5", ["39", "37", "40"], "昨晚三十八度五."),
        M("What was the temperature at the doctor’s?", "39", ["38.5", "37.5", "36"], "三十九度."),
        M("What did the doctor find about the heart?", "A bit fast but still normal", ["Very slow", "Very weak", "Irregular"], "有点快，但还算正常."),
        M("What did the doctor see in the throat?", "It was swollen", ["It was pale", "It was normal", "There was a cut"], "你嗓子肿了."),
        M("What is the diagnosis?", "The flu", ["A cold", "Pneumonia", "Food poisoning"], "你得的是流感."),
        M("What will the doctor do today?", "Give an injection and prescribe medicine", ["Send him home", "Operate", "Take blood"], "今天先打一针，再开点儿药."),
        M("What tests are for after three days if he is not better?", "Blood, urine and X-ray", ["Only blood", "None", "A heart scan"], "验血、验尿和透视."),
        M("How should he take the medicine?", "Three times a day, two tablets each time", ["Once a day", "Four tablets at night", "Only when sick"], "一天三次，一次两片."),
        M("Can he go to work?", "No, it’s best to rest at home", ["Yes, as usual", "Only half a day", "Only by bus"], "最好在家休息."),
        M("Where is the pharmacy?", "On the left of the first-floor hall", ["Second floor", "Behind the hospital", "Next to the infusion room"], "就在一楼大厅的左边."),
        F("我两天前开始咳嗽，流鼻___，就去药店买了一些感冒药。", "涕", ["水", "子", "泪"], "流鼻涕: runny nose."),
        F("三天后要是还不好，就再去验血、验尿和透___。", "视", ["看", "观", "查"], "透视: X-ray."),
    ],
)

# ------------------------------------------------------------------ 4. activity 4: asking directions
W1 = [("小文", "张华，有空儿到我家来玩玩。", "Xiao Wen: Zhang Hua, come over to my place when you have time."),
      ("张华", "好的，小文。你家住哪儿？", "Zhang Hua: OK, Xiao Wen. Where do you live?"),
      ("小文", "我家在中山路五零九号。", "Xiao Wen: My home is at 509 Zhongshan Road. (the book writes 509)"),
      ("张华", "去你家需要坐公共汽车吗？", "Zhang Hua: Do I need to take a bus to your home?"),
      ("小文", "不用。我家离学校很近，走十几分钟就到了。", "Xiao Wen: No. My home is very near the school; a walk of ten-odd minutes gets you there."),
      ("张华", "那到你家怎么走？", "Zhang Hua: Then how do I get to your home?"),
      ("小文", "出了学校大门往东走，过两个十字路口，在第三个十字路口那儿往北拐，路口有一个邮局。我家就在邮局的对面。", "Xiao Wen: Leave the school gate and walk east, pass two intersections, and at the third intersection turn north; there is a post office at the corner. My home is right across from the post office."),
      ("张华", "好，谢谢。我有空儿一定去你家坐坐。", "Zhang Hua: Good, thanks. When I have time I will certainly come to your place.")]
W2 = [("琳达", "请问，从这儿去建国饭店怎么走？", "Linda: Excuse me, how do I get to the Jianguo Hotel from here?"),
      ("行人", "你得先坐地铁，然后再转公共汽车。", "Passer-by: You have to take the subway first and then transfer to a bus."),
      ("琳达", "那我在哪儿坐地铁呢？", "Linda: Then where do I take the subway?"),
      ("行人", "这儿离地铁二号线安定门站很近。你沿着这条马路往前走，过了立交桥就可以看到地铁站口了。", "Passer-by: Line 2’s Andingmen station is very near here. Walk forward along this road, and after you pass the overpass you can see the subway entrance."),
      ("琳达", "我应该坐去哪个方向的地铁？到哪一站下车呢？", "Linda: Which direction should I take, and at which stop do I get off?"),
      ("行人", "你坐去东直门方向的地铁，到建国门站下车。", "Passer-by: Take the subway toward Dongzhimen and get off at Jianguomen station."),
      ("琳达", "出了地铁以后，要坐几路公车？", "Linda: After leaving the subway, which bus do I take?"),
      ("行人", "从地铁东北口出来，在公车站台坐二零一路车，三站路就到了。", "Passer-by: Come out of the subway’s northeast exit and take bus 201 at the bus stop; three stops and you are there.")]
W3 = [("李明", "陈老师，这个周末我打算请几个朋友来聚聚，你也来热闹热闹吧？", "Li Ming: Teacher Chen, this weekend I plan to invite a few friends over for a get-together. Will you come and join the fun?"),
      ("陈老师", "好啊，这个周末我正好没什么事。你家在哪个小区，我开车怎么去那儿？", "Teacher Chen: Sure, this weekend I happen to have nothing on. Which residential community do you live in, and how do I drive there?"),
      ("李明", "我家住在半月花园，很好找。从你家出来，上四号环城高速路。沿着高速路，开十五分钟。", "Li Ming: I live in Half Moon Garden; it is easy to find. Leaving your home, get on the Fourth Ring Expressway. Drive along the expressway for fifteen minutes."),
      ("陈老师", "在哪儿下高速呢？", "Teacher Chen: Where do I leave the expressway?"),
      ("李明", "在三十二号出口下高速。然后，沿着右手边的第一个车道一直开到底，你就会看到一家大华超市。我们小区就在超市的旁边。", "Li Ming: Leave at Exit 32. Then drive along the first lane on the right-hand side all the way to the end and you will see a Dahua supermarket. Our community is right next to the supermarket."),
      ("陈老师", "听上去不太远。到时候你把地址也发给我，如果我忘了怎么走，还可以用一下手机地图和导航。", "Teacher Chen: It sounds not too far. When the time comes send me the address too; if I forget the way I can also use the phone map and navigation."),
      ("李明", "没问题，我一会儿就发给你。", "Li Ming: No problem, I will send it to you in a moment.")]
TW = table(["问路", "目的地 (my answers)", "怎么走 (my answers)"], [["问路一", "小文家，中山路五零九号", "出了学校大门往东走，过两个十字路口，在第三个十字路口往北拐，邮局对面"], ["问路二", "建国饭店", "走到安定门站坐地铁二号线去东直门方向，在建国门站下车，从东北口出来坐二零一路车，三站"], ["问路三", "半月花园", "上四号环城高速路，开十五分钟，在三十二号出口下，沿右手边第一个车道开到底，大华超市旁边"]],
           title="Activity 4A: the table of destinations and directions (the book leaves it blank; the contents are mine, from the scripts)", say=[0, 1, 2])
L4 = lesson(
    "Lesson 24 Skills Integration Review: three conversations about directions",
    "中山路五零九号 · 建国饭店 · 地铁二号线 · 二零一路 · 半月花园 · 三十二号出口",
    requires=[],
    cards=[
        card("Activity 4 (Listening, Writing, Reading, Speaking)",
             "A. Work in groups of three and listen to three dialogs about directions. Each student listens to one dialog and writes the destination and directions in the space provided (问路 1, 问路 2, 问路 3). B. When you are done, exchange information with your partners. Your partners can draw a map according to your directions. C. Together, read the scripts and check your information. (Audio and three pictures, not included.)",
             tables=[TW]),
        card("Script 问路 1", "The book writes 509; here it is spelled out. The translations are mine.", examples=dlg(W1)),
        card("Script 问路 2", "The book writes line 2 and bus 201; here they are spelled out. The translations are mine.", examples=dlg(W2)),
        card("Script 问路 3", "The book writes the Fourth Ring road, 15 minutes and Exit 32; here they are spelled out. The translations are mine.", examples=dlg(W3)),
    ],
    exercises=[
        M("Where does Xiao Wen live?", "509 Zhongshan Road", ["12 Dahua Street", "3 Jianguo Road", "40 Andingmen Road"], "中山路五零九号."),
        M("How does Zhang Hua get to Xiao Wen’s?", "Walk east, pass two intersections, turn north at the third", ["Take bus 201", "Drive on the expressway", "Take the subway"], "往东走，过两个十字路口，第三个往北拐."),
        M("What is across from Xiao Wen’s home?", "A post office", ["A bank", "A school", "A park"], "我家就在邮局的对面."),
        M("What does Linda want to find?", "Jianguo Hotel", ["Dongzhimen station", "A supermarket", "The airport"], "建国饭店."),
        M("Which subway line is mentioned?", "Line 2", ["Line 1", "Line 3", "Line 5"], "地铁二号线."),
        M("At which station does Linda get off?", "Jianguomen", ["Andingmen", "Dongzhimen", "Zhongshan Park"], "建国门站下车."),
        M("Which bus does she take after the subway?", "No. 201", ["No. 12", "No. 65", "No. 32"], "二零一路车."),
        M("What is Li Ming planning for the weekend?", "A get-together with friends", ["A trip", "An exam", "A move"], "请几个朋友来聚聚."),
        M("How long does Teacher Chen drive on the expressway?", "Fifteen minutes", ["Five minutes", "One hour", "Two hours"], "开十五分钟."),
        M("At which exit does he leave the expressway?", "Exit 32", ["Exit 47", "Exit 15", "Exit 4"], "三十二号出口."),
        M("What is next to Li Ming’s community?", "A Dahua supermarket", ["A post office", "A subway station", "A hospital"], "就在超市的旁边."),
        F("出了学校大门往东走，过两个十字路口，在第三个十字路口那儿往北___。", "拐", ["看", "买", "吃"], "往北拐: turn north."),
        F("你沿着这条马路往前走，过了立交桥就可以看到地铁站口___。", "了", ["吗", "呢", "吧"], "过了…就…了."),
    ],
)

UNIT = unit("第二十四课 Unit 4 review: skills integration review, part 1", [L1, L2, L3, L4])
