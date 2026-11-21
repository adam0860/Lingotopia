"""Unit 70: Lesson 24 (Unit 4 review), the presentation activities review from the book's texts: translating fifteen sentences with key expressions,
the three passages (the train manager's announcement, Lao Lin the postman, the postcard kiosk), matching twelve sentences and ordering the
San Diego paragraphs. Audio and pictures are not included; numbers the book writes as digits are spelled out; the Chinese sentences for the
translation activity, the answer keys and the summaries are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('列车长', 2, 'zhang3'), ('还是', 0, 'hai2'), ('还有', 0, 'hai2'), ('还寄', 0, 'hai2'), ('还办', 0, 'hai2'), ('还说', 0, 'hai2'), ('还恶', 0, 'hai2'), ('还是这么', 0, 'hai2'), ('发得', 1, 'de5'), ('说得', 1, 'de5'), ('开得', 1, 'de5'), ('唱得', 1, 'de5'), ('得对', 0, 'de5'), ('得不好', 0, 'de5'), ('得越来', 0, 'de5'), ('疼得', 1, 'de5'), ('得好极', 0, 'de5'), ('得很厉害', 0, 'de5'), ('得到', 0, 'de2'), ('得很好', 0, 'de5'), ('长假', 0, 'chang2'), ('长时间', 0, 'chang2'), ('长途', 0, 'chang2'), ('最长', 1, 'chang2'), ('得流感', 0, 'de2'), ('爱得', 1, 'de5'), ('得了流', 0, 'de2'), ('国都有', 1, 'dou1'), ('上了无', 1, 'le5'), ('诊为', 1, 'wei2')):
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

# ------------------------------------------------------------------ 1. activity 1, items 1-8
P1 = [("儿子，国庆长假快到了，你陪我和你妈回老家住几天，怎么样？", "1A. Son, National Day holiday is coming. How about you accompany me and your mom back to our hometown for a few days? (国庆长假，陪)"),
      ("我早就订好高铁票了。反正我们每年国庆都回去看奶奶。", "1B. I booked high-speed train tickets a long time ago. We go and see grandma every National Day anyway. (早就，反正)"),
      ("高铁开得这么平稳，如果列车长不告诉我们，我们根本不知道现在的时速是三百五十公里。", "2. The high-speed train was traveling so steadily that I’d have had no idea it was going 350 km an hour if the conductor hadn’t told us. (平稳，如果，根本)"),
      ("列车减速运行了五分钟，列车长才通知我们。她还说，列车一定会准时到达上海。", "3. The train conductor only informed us of the slowdown after the train had been running at a reduced speed for five minutes. She also said that the train would arrive in Shanghai on time for sure. (减速，才，一定)"),
      ("她不但给我寄了生日贺卡，而且还寄了一份礼物，都是用特快专递寄的。", "4. Not only did she send me a birthday card, but also a present. And she sent them by express mail. (不但…而且…)"),
      ("多长时间能寄到，要看你怎么寄。如果寄特快专递，最多三天就能寄到，不过那样寄很贵。", "5. How long it will take to arrive depends on how you are going to send it. It will take three days, at most, by express mail, but it would be expensive to send it that way. (寄到，要看，最多，那样寄，不过)"),
      ("邮局每天办理很多信件和包裹业务，另外还办理交费等业务，所以被很多人称为“万能手”。", "6. The post office handles a lot of mail and packages every day. Besides this they also handle utility payments and other business. Therefore, they are called a “Jack of all trades” by many people. (办理，另外，被)"),
      ("吃了药以后，如果发烧还是这么厉害，请再来。下次挂普通门诊就行了，别忘了带病历卡。", "7. After taking the medicine, please come back if your fever is still as bad as it is now. Just register for the regular outpatient clinic next time, and don’t forget to bring your registration card. (这么厉害，下次，普通门诊，别) (病历卡 for “registration card” is mine)"),
      ("你发烧发得很厉害，看起来是得了流感。你先吃点儿药，多喝水，好好休息。", "8. Your fever is bad, and it looks like you’ve got the flu. Take some medicine first. You need to drink a lot of water and get plenty of rest. (发烧发得…，看起来，先，多，好好)")]
L1 = lesson(
    "Lesson 24 Presentation Activities Review: translating sentences, part 1",
    "国庆长假 · 高铁平稳 · 减速 · 贺卡 · 特快专递 · 万能手 · 发烧发得很厉害",
    requires=[],
    cards=[
        card("Activity 1 (Speaking, Writing, and Reading), items 1 to 8",
             "A. Pair up. Take turns translating the sentences to your partner in Chinese. Some key expressions have been provided. B. Go over the suggested answer provided by the teacher and refine your sentences. The book prints the English sentences and key expressions only; the Chinese sentences below are mine, built from the key expressions, with numbers spelled out in characters.",
             examples=[D(z, e) for z, e in P1]),
    ],
    exercises=[
        M("Which expression means “anyway”?", "反正", ["早就", "根本", "一定"], "反正: anyway."),
        M("Which expression means “a long time ago, already”?", "早就", ["反正", "才", "别"], "早就."),
        M("Which expression means “not at all (with a negative)”?", "根本", ["一定", "最多", "先"], "根本不知道: no idea at all."),
        M("Which word marks that something happened later than expected?", "才", ["就", "也", "都"], "五分钟以后才通知."),
        M("Which word means “at most”?", "最多", ["最少", "一定", "反正"], "最多三天."),
        M("Which word marks the agent in “被很多人称为”?", "被", ["把", "给", "对"], "被: passive."),
        M("Which expression means “it looks like”?", "看起来", ["听起来", "起来", "看看"], "看起来是得了流感."),
        M("Which means “don’t”?", "别", ["不", "没", "不要 (mild)"], "别忘了: don’t forget."),
        M("What does 寄特快专递，最多三天就能寄到 mean?", "By express mail it takes three days at most", ["It takes three weeks", "It is free", "It never arrives"], "最多三天."),
        M("What do many people call the post office?", "万能手", ["快递员", "代理人", "老爷爷"], "被…称为“万能手”."),
        F("国庆长假快到了，你___我和你妈回老家住几天，怎么样？", "陪", PART, "陪: accompany."),
        F("她___但给我寄了生日贺卡，而且还寄了一份礼物。", "不", PART, "不但…而且…."),
    ],
)

# ------------------------------------------------------------------ 2. activity 1, items 9-15
P2 = [("半夜她发起烧来，肚子也疼，还恶心。我赶紧开车把她送到了医院急诊室。", "9. She started to have a fever in the middle of the night, and she also felt stomach pain and nausea. I quickly drove her to the hospital for emergency treatment. (V+起+O+来，把，送到)"),
      ("请问，我迷路了，您能告诉我到火车站怎么走吗？", "10A. Excuse me, I cannot find my way. Can you tell me how to get to the railway station? (迷路，到…怎么走)"),
      ("您从这儿坐往北开的地铁，坐三站下车，然后往东走。过了两个十字路口，往左拐就到了。", "10B. Take the north-bound subway from here, get off at the third stop, then go east. Turn left after passing two intersections, and you will be there. (往，过，拐)"),
      ("我再说一遍：出了富兰克林门，沿着街往下坡走，过了第三个红绿灯往左拐，一直走到头就到了。我说得对吗？", "11. Let me repeat. Go downhill along the street after you go out the Franklin Gate, make a left turn at the third traffic light, then go to the end of the street and I’ll be there. Did I say it right? (沿着，一直，过，拐，头 (end)，说得)"),
      ("旧金山国际机场位于旧金山的南边，是美国西部第二大机场，仅次于洛杉矶国际机场。", "12. San Francisco International Airport is located on the south side of San Francisco. It is the second largest airport in the western United States, second only to Los Angeles International Airport. (位于，仅次于)"),
      ("要提高汉语听力，你需要多听真实的语言材料。一开始有些材料你可能听不懂，但是慢慢地，听着听着你就听懂了。", "13. To improve your Chinese listening comprehension you need to listen to a lot of authentic material. You may have difficulty understanding some material in the beginning, but slowly, as you keep listening, you will understand it. (听力，慢慢地，听着听着就)"),
      ("虽然四川菜对我来说很辣，但是吃着吃着就习惯了。我已经学着做过好几次四川菜了。", "14. Although Sichuan dishes were very spicy to me, I became used to it as I kept eating them. I have tried making Sichuan dishes several times. (虽然…但是…，吃着吃着就，学着)"),
      ("她不但喜欢说中文，而且喜欢唱中文歌。她的中文歌唱得好极了！", "15. Not only does she like to speak Chinese, but she also likes to sing Chinese songs. She sings Chinese songs amazingly well! (不但…而且…，极了)")]
L2 = lesson(
    "Lesson 24 Presentation Activities Review: translating sentences, part 2",
    "发起烧来 · 迷路 · 沿着 一直 过 拐 · 位于 仅次于 · 听着听着就 · 吃着吃着就 · 好极了",
    requires=[],
    cards=[
        card("Activity 1 (continued), items 9 to 15",
             "The book prints the English sentences and key expressions only; the Chinese sentences below are mine, built from the key expressions.",
             examples=[D(z, e) for z, e in P2]),
    ],
    exercises=[
        M("Which pattern means “start to have a fever”?", "发起烧来", ["发烧起", "起发烧", "烧发起来"], "V + 起 + O + 来."),
        M("Which means “to get lost”?", "迷路", ["拐弯", "过桥", "走路"], "迷路."),
        M("Which means “turn (left or right)”?", "拐", ["过", "沿着", "到"], "往左拐."),
        M("Which means “keep going straight”?", "一直", ["仅次于", "位于", "最多"], "一直走."),
        M("Which expression means “located at”?", "位于", ["仅次于", "沿着", "迷路"], "位于旧金山的南边."),
        M("Which expression means “second only to”?", "仅次于", ["位于", "最多", "根本"], "仅次于洛杉矶国际机场."),
        M("What does 听着听着你就听懂了 mean?", "As you keep listening you will come to understand", ["You never understand", "You stop listening", "You listen once"], "V着V着就…."),
        M("What does 吃着吃着就习惯了 mean?", "I got used to it as I kept eating", ["I stopped eating", "I ate too fast", "I never ate it"], "V着V着就…."),
        M("What does 她的中文歌唱得好极了 mean?", "She sings Chinese songs extremely well", ["She cannot sing", "She sings slowly", "She sings little"], "好极了."),
        M("Which means “end of the street”?", "街的头", ["街的头 (wrong)", "街的尾巴", "街的脚"], "走到头: walk to the end."),
        F("半夜她发起烧___，肚子也疼。", "来", PART, "发起烧来."),
        F("你听我说得对不对？我说___对吗？", "得", PART, "说得对吗."),
    ],
)

# ------------------------------------------------------------------ 3. activity 2
T2 = table(["词", "Meaning (mine)"], [["南北方向", "north-south direction"], ["邮局的变化", "changes in the post office"], ["售货亭", "kiosk, sales booth"], ["明信片", "postcard"], ["邮筒", "mailbox, post box"], ["收件人", "addressee, recipient"]],
           title="Activity 2A: guess the meaning of the following expressions (meanings mine)", say=[0])
S1 = ("各位旅客，您好！我是本次列车的列车长马小明。欢迎您乘坐Ｇ八十从广州开往北京的高速列车。北京和广州之间的高铁是目前中国线路最长，也是经过的省最多的南北方向的高速铁路。京广铁路全线是二零一二年十二月建成通车的。",
      "Script Passage 1, paragraph 1: Dear passengers, hello! I am Ma Xiaoming, the train manager of this train. Welcome aboard the G80 high-speed train from Guangzhou to Beijing. The high-speed railway between Beijing and Guangzhou is currently the longest line in China and also the north-south high-speed railway that passes through the most provinces. The whole Beijing–Guangzhou railway was completed and opened to traffic in December 2012. (the book writes G80 and the date in digits; translation mine)")
S1B = ("我们的列车今天早上七点离开广州，将在今天下午五点零一分到达北京。沿途一共运行两千三百公里，平均每小时车速是二百八十七公里。",
       "Paragraph 2: Our train left Guangzhou at seven this morning and will arrive in Beijing at 5:01 this afternoon. Along the way it runs a total of 2,300 kilometers, with an average speed of 287 kilometers per hour. (mine)")
S1C = ("各位旅客，本次列车提供免费无线上网服务。如果您需要用餐，餐车就在第五号车厢。另外，每节车厢有热水器，您可以用热水泡茶或咖啡。服务员也给您准备好了各种饮料和零食，每隔半小时售货车会到每个车厢，欢迎旅客们购买。",
       "Paragraph 3: Dear passengers, this train offers free wireless internet. If you need a meal, the dining car is in car number five. In addition, each car has a water heater, and you can use the hot water to make tea or coffee. The attendants have also prepared all kinds of drinks and snacks for you, and every half hour the sales cart will come to each car; passengers are welcome to buy. (mine)")
S2 = ("我姓林，你就叫我老林吧。我十七岁起就在邮局工作，每天骑着自行车出去送信送包裹。那时的邮局只寄信、寄包裹、打长途电话。今年我五十七岁了，过去的这三十年，我们的邮局变化太大了。现在寄信的人少多了，更没人来邮局打长途电话了，但寄的包裹越来越多。现在我们邮局除了办理一般的包裹业务以外，还办理国内和国外的特快专递。现在邮局的业务都离不开电脑和网络。过去要知道一个包裹在什么地方，需要花一个星期，打很多电话才能找到。现在客人自己上网随时就能查到。以前我们骑自行车送邮件，现在呢，都是用汽车，有些地方甚至用上了无人飞机。",
      "Script Passage 2, paragraph 1: My surname is Lin; just call me Lao Lin. I have worked in the post office since I was seventeen, going out every day by bicycle to deliver letters and packages. The post office then only sent letters and packages and made long-distance calls. This year I am fifty-seven, and in the past thirty years our post office has changed enormously. Now far fewer people send letters, and even fewer come to the post office to make long-distance calls, but more and more packages are sent. Now besides handling ordinary package business our post office also handles domestic and international express mail. Now the post office’s business cannot do without computers and the internet. In the past, to know where a package was, you needed to spend a week and make many phone calls before finding it. Now customers can check it online themselves at any time. Before, we delivered mail by bicycle; now it is all by car, and in some places we even use drones. (the book writes 17; translation mine)")
S2B = ("邮局现在不仅寄送信件和包裹，还代收各种费用，并且办理银行业务。我儿子今年二十五岁，也在邮局工作。不过，他不办理信件或包裹业务，而是在邮局大厅为顾客提供银行服务。",
       "Paragraph 2: Now the post office not only sends letters and packages but also collects all kinds of fees on behalf of others and handles banking business. My son is twenty-five this year and also works in the post office. However, he does not handle letters or packages; instead he provides banking services for customers in the post office hall. (mine)")
S3 = ("二十一岁的小杨住在山东省济南市，那是一个风景不错的城市。到济南旅游的游客不仅多，而且喜欢买一些当地的纪念品。今年四月，小杨在一条游客特别多的大街上，租下了一个售货亭。她的售货亭不卖日用品，也不卖书和报纸杂志，只卖明信片。她卖的明信片上都有一张济南的风景照片。为了方便游客，她在售货亭旁边放了一个邮筒。客人买了明信片以后，先填上收件人名字和地址，再贴上邮票，然后把它放进邮筒。到了下午四点，小杨就会把游客放在邮筒里的明信片取出来，然后亲自到邮局把它们寄走。几天以后，收件人就能收到一张来自济南的漂亮的明信片。小杨的售货亭已经开了三个多月了，每天都有很多人来买明信片。小杨说，这个售货亭能给游客带来不同的体验，这是最让她高兴的事。",
      "Script Passage 3: Xiao Yang, twenty-one, lives in Jinan, Shandong Province, a city with fine scenery. The tourists who travel to Jinan are not only many but also like to buy local souvenirs. This April Xiao Yang rented a kiosk on a street with an especially large number of tourists. Her kiosk does not sell daily necessities, nor books, newspapers and magazines; it sells only postcards. Every postcard she sells has a photo of Jinan scenery. To make things convenient for tourists she put a mailbox beside the kiosk. After customers buy a postcard they first fill in the addressee’s name and address, then put on a stamp, and then drop it into the mailbox. At four in the afternoon Xiao Yang takes the postcards out of the mailbox and then goes to the post office herself to send them off. A few days later the addressee will receive a beautiful postcard from Jinan. Xiao Yang’s kiosk has been open for more than three months and many people come to buy postcards every day. Xiao Yang says this kiosk can give tourists a different experience, and that is the thing that makes her happiest. (mine)")
L3 = lesson(
    "Lesson 24 Presentation Activities Review: the train manager, Lao Lin and the postcard kiosk",
    "南北方向 · 邮局的变化 · 售货亭 · 明信片 · 邮筒 · 收件人 · 三篇听力文本",
    requires=[],
    cards=[
        card("Activity 2 (Listening, Writing, Speaking, and Reading)",
             "A. Guess the meaning of the following expressions. B. Listen to the three passages and match them with the pictures below (audio and three pictures, not included). C. Form groups of three. Each partner listens to one dialog, prepares a summary and completes the table (大意: 第一篇, 第二篇, 第三篇). D. Share your work in group and take notes in the above table of the other two passages. Ask each of your partners at least three questions. E. Read the scripts below and check your summary and notes.",
             tables=[T2]),
        card("Script Passage 1: the train manager’s announcement", "The book writes G80 and the digits as numerals; here they are spelled out and the letter is full-width. The translations are mine.", examples=[D(*S1), D(*S1B), D(*S1C)]),
        card("Script Passage 2: Lao Lin, a postman", "Numbers are spelled out. The translations are mine.", examples=[D(*S2), D(*S2B)]),
        card("Script Passage 3: Xiao Yang’s postcard kiosk", "Numbers are spelled out. The translation is mine.", examples=[D(*S3)]),
    ],
    exercises=[
        M("Who is making the announcement in Passage 1?", "The train manager, Ma Xiaoming", ["A ticket seller", "A passenger", "A driver"], "我是本次列车的列车长马小明."),
        M("Where is the train going?", "From Guangzhou to Beijing", ["From Beijing to Shanghai", "From Xi’an to Beijing", "From Chengdu to Lhasa"], "从广州开往北京."),
        M("When was the whole Beijing–Guangzhou line completed?", "December 2012", ["December 2008", "May 2010", "June 2015"], "二零一二年十二月."),
        M("When does the train arrive in Beijing?", "5:01 in the afternoon", ["7:00 in the morning", "9:15", "noon"], "下午五点零一分."),
        M("Where is the dining car?", "Car number five", ["Car number one", "Car number eight", "At the station"], "餐车就在第五号车厢."),
        M("How often does the sales cart come to each car?", "Every half hour", ["Every hour", "Every ten minutes", "Never"], "每隔半小时."),
        M("Since when has Lao Lin worked at the post office?", "Since he was seventeen", ["Since last year", "Since forty", "Since twenty-five"], "十七岁起."),
        M("How old is Lao Lin now?", "Fifty-seven", ["Seventeen", "Twenty-five", "Seventy"], "五十七岁."),
        M("What does Lao Lin’s son do at the post office?", "Provides banking services in the hall", ["Delivers letters by bicycle", "Flies drones", "Sorts packages"], "在邮局大厅为顾客提供银行服务."),
        M("What does Xiao Yang sell in her kiosk?", "Only postcards", ["Newspapers", "Daily necessities", "Stamps only"], "只卖明信片."),
        M("When does she take the postcards out of the mailbox?", "At four in the afternoon", ["At noon", "At night", "At seven"], "到了下午四点."),
        M("What makes Xiao Yang happiest?", "Giving tourists a different experience", ["Making money", "Opening a second kiosk", "Winning a prize"], "给游客带来不同的体验."),
        F("她的售货亭不卖日用品，也不卖书，只___明信片。", "卖", PART, "只卖明信片."),
        F("客人买了明信片以后，先填上___件人名字和地址。", "收", PART, "收件人: addressee."),
    ],
)

# ------------------------------------------------------------------ 4. activities 3 and 4
MT = [("我父亲发烧，还拉肚子，请问他应该挂哪个科？", "1 → C. My father has a fever and diarrhea; which department should he register for? (key mine)"),
      ("先生，能不能麻烦您一下，您知道去天安门怎么走吗？", "2 → I. Sir, could I trouble you for a moment; do you know how to get to Tiananmen? (mine)"),
      ("这个药怎么吃啊？我还真不知道。你没问医生吗？", "3 → D. How do you take this medicine? I really don’t know. Didn’t you ask the doctor? (mine)"),
      ("出了学校大门，一直往南开，到第三个红绿灯往右拐，再开两分钟就是高速公路。", "4 → J. Leaving the school gate, drive straight south, turn right at the third traffic light, and after two more minutes of driving you are at the expressway. (mine)"),
      ("上海浦东机场是中国的第二大机场，仅次于北京的首都机场。", "5 → G. Shanghai Pudong Airport is China’s second largest airport, second only to Beijing Capital Airport. (mine)"),
      ("我发烧两天了，头疼得也很厉害。你一定是得了流感。现在得流感的人很多。", "6 → A. I have had a fever for two days and my head hurts badly too. You must have the flu; many people have the flu now. (mine)"),
      ("是不是在候机楼一楼提取行李？是二楼。一楼是国际出发大厅。", "7 → L. Do you pick up luggage on the first floor of the terminal? It is the second floor; the first floor is the international departure hall. (mine)"),
      ("一开始说得不好没关系，只要多说多听，慢慢地就会说得越来越好。", "8 → K. It does not matter if you speak poorly at first; as long as you speak and listen more, you will gradually speak better and better. (mine)"),
      ("从这儿上公共汽车，坐三站下车，往前走一会儿，你就会看见美国大使馆了。", "9 → F. Get on the bus here, ride three stops, get off, walk forward for a while and you will see the U.S. embassy. (mine)"),
      ("昨晚我有点儿累了，做作业的时候做着做着睡着了。", "10 → H. Last night I was a bit tired and fell asleep while doing homework. (mine)"),
      ("今天早上他肚子疼得越来越厉害，我马上开车把他送到急诊室，医生确诊为阑尾炎。", "11 → E. This morning his stomach hurt more and more; I immediately drove him to the emergency room and the doctor confirmed appendicitis. (the book’s English gloss “appendicitis” is dropped from the Chinese; key mine)"),
      ("深圳是个现代化大都市，那里不但有很多高楼，而且也有很多漂亮的公园。", "12 → B. Shenzhen is a modern metropolis; it has not only many tall buildings but also many beautiful parks. (mine)")]
AA = ("现在有十几万华人住在圣地亚哥。随着经济的发展和人口的增加，越来越多的华人来到圣地亚哥投资或者工作。来这儿的华人喜欢住在校区好的地段，目的是让他们的孩子得到很好的教育。",
      "Paragraph A: Now more than a hundred thousand Chinese people live in San Diego. With the development of the economy and the increase in population, more and more Chinese come to San Diego to invest or work. The Chinese who come here like to live in areas with good school districts, with the aim of letting their children get a good education. (mine)")
AB = ("圣地亚哥位于美国西海岸南边，是一座非常美丽的现代化都市。它是加州第二大城市，也是美国的第八大城市。这里不仅旅游业十分发达，而且制药和高科技等产业在美国都有重要的位置。",
      "Paragraph B: San Diego is located in the south of the American West Coast and is a very beautiful modern city. It is the second largest city in California and the eighth largest in the United States. Here not only is tourism very developed but industries such as pharmaceuticals and high technology also hold important positions in the United States. (mine)")
AC = ("如果您想来圣地亚哥居住，请一定和我们联系，我们一定会帮您买到您喜欢的房子。如果您不想买房，我们也有各种出租房由您选择。",
      "Paragraph C: If you would like to live in San Diego, please be sure to contact us; we will certainly help you buy a house you like. If you don’t want to buy, we also have all kinds of rental homes for you to choose from. (mine)")
L4 = lesson(
    "Lesson 24 Presentation Activities Review: matching sentences and ordering paragraphs",
    "挂哪个科 · 去天安门怎么走 · 仅次于首都机场 · 做着做着睡着了 · 圣地亚哥",
    requires=[],
    cards=[
        card("Activity 3 (Reading and Speaking)",
             "A. Match the terms in Column A with the terms in Column B by writing the correct letter in the left column. B. Pair up and check your work. Take turns translating the sentences into English. Column A: 1. 我父亲发烧，还拉肚子， 2. 先生，能不能麻烦您一下， 3. 这个药怎么吃啊？ 4. 出了学校大门，一直往南开，到第三个红绿灯往右拐， 5. 上海浦东机场是中国的第二大机场， 6. 我发烧两天了，头疼得也很厉害。 7. 是不是在候机楼一楼提取行李？ 8. 一开始说得不好没关系， 9. 从这儿上公共汽车，坐三站下车， 10. 昨晚我有点儿累了，做作业的时候 11. 今天早上他肚子疼得越来越厉害， 12. 深圳是个现代化大都市，那里不但有很多高楼， Column B: A. 你一定是得了流感。现在得流感的人很多。 B. 而且也有很多漂亮的公园。 C. 请问他应该挂哪个科？ D. 我还真不知道。你没问医生吗？ E. 我马上开车把他送到急诊室，医生确诊为阑尾炎。 F. 往前走一会儿，你就会看见美国大使馆了。 G. 仅次于北京的首都机场。 H. 做着做着睡着了。 I. 您知道去天安门怎么走吗？ J. 再开两分钟就是高速公路。 K. 只要多说多听，慢慢地就会说得越来越好。 L. 是二楼。一楼是国际出发大厅。 The book gives no key; my matching, joined into sentences:",
             examples=[D(z, e) for z, e in MT]),
        card("Activity 4 (Reading and Speaking)",
             "A. Read the following paragraphs and arrange them together in a logical, numerical order. B. Pair up, share your work, and explain your reasoning. Speak in Chinese. C. Write a summary of the passage in English and share it with the class. The book prints the paragraphs in the order A, B, C, with no key. My order: B (where San Diego is and what it is like), then A (the Chinese who live there), then C (the housing offer). My summary: San Diego, in the south of the American West Coast, is a beautiful modern city and California’s second largest; tourism, pharmaceuticals and high technology are strong. More than a hundred thousand Chinese now live there, choosing areas with good schools for their children. The writer, a real-estate agent, invites readers to contact them to buy or rent a home. (The picture is not included.)",
             examples=[D(*AA), D(*AB), D(*AC)]),
    ],
    exercises=[
        M("Which ending goes with 我父亲发烧，还拉肚子，?", "请问他应该挂哪个科？", ["仅次于北京的首都机场。", "做着做着睡着了。", "是二楼。"], "1 → C."),
        M("Which ending goes with 先生，能不能麻烦您一下，?", "您知道去天安门怎么走吗？", ["而且也有很多漂亮的公园。", "再开两分钟就是高速公路。", "做着做着睡着了。"], "2 → I."),
        M("Which ending goes with 上海浦东机场是中国的第二大机场，?", "仅次于北京的首都机场。", ["是二楼。", "往前走一会儿。", "请问他挂哪个科？"], "5 → G."),
        M("Which ending goes with 昨晚我有点儿累了，做作业的时候?", "做着做着睡着了。", ["再开两分钟。", "你没问医生吗？", "仅次于首都机场。"], "10 → H."),
        M("Which ending goes with 一开始说得不好没关系，?", "只要多说多听，慢慢地就会说得越来越好。", ["我马上开车把他送到急诊室。", "是二楼。", "再开两分钟就是高速公路。"], "8 → K."),
        M("Which ending goes with 深圳是个现代化大都市，那里不但有很多高楼，?", "而且也有很多漂亮的公园。", ["仅次于北京。", "我还真不知道。", "做着做着睡着了。"], "12 → B."),
        M("What did the doctor confirm in item 11?", "Appendicitis", ["The flu", "A cold", "Pneumonia"], "确诊为阑尾炎."),
        M("In the San Diego passage, which paragraph comes first?", "B (the location and the city)", ["A", "C", "Any order"], "B → A → C."),
        M("According to the passage, why do Chinese live in areas with good school districts?", "To give their children a good education", ["To save money", "To be near the sea", "To find jobs"], "目的是让他们的孩子得到很好的教育."),
        M("What is San Diego’s rank among California’s cities?", "Second largest", ["Largest", "Eighth", "Smallest"], "加州第二大城市."),
        F("圣地亚哥___于美国西海岸南边。", "位", PART, "位于: be located at."),
        F("现在有十几万华人___在圣地亚哥。", "住", PART, "住在."),
    ],
)

UNIT = unit("第二十四课 Unit 4 review: presentation activities review", [L1, L2, L3, L4])
