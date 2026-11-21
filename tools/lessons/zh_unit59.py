"""Unit 59: Lesson 20 (The Post Office) Presentation 3 and Area Studies from the book's texts: the passage on the post office then and now, the five
activities, the causative 使, the neutral 被, 另外/还有/而且, 所有的, the skill-integration activities (the survey, the U.S. and Taiwan post offices), the
using-Chinese activities (drop boxes, the i邮箱 service), the vocabulary list and the Area Studies reading. Audio, pictures, videos and links are not
included; numbers the book writes as digits are spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l20_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 3
PA = ("说起几十年前的中国邮政，四、五十岁的人都会记起那些虽然不大，但是非常繁忙的邮局。那时候，人们每隔几天就要去一趟邮局。买邮票，寄信，寄包裹要去邮局，打长途，发电报，也得去邮局，订报纸、杂志，给爷爷奶奶汇钱，还要去邮局，邮局和人们的日常生活简直是分不开。",
      "Speaking of the Chinese post of several decades ago, people in their forties and fifties will all remember those post offices that were not big but were very busy. In those days people had to go to the post office every few days. To buy stamps, send letters and send parcels you went to the post office; to make long-distance calls and send telegrams you also had to go to the post office; to subscribe to newspapers and magazines and to remit money to Grandpa and Grandma you still had to go to the post office. The post office and people’s daily life were simply inseparable. (translation mine)")
PB = ("可是，电子邮件的发明，却使邮局一下子减少了百分之八十以上的邮件业务。手机、微信的出现更使邮局失去了几乎所有的电讯业务。另外，快递公司的出现也使邮局的快件业务少了一大半。邮局在人们生活中不那么重要了，去邮局的人也越来越少。",
      "But the invention of e-mail suddenly cut the post office’s mail business by more than 80 percent (the book writes 80%). The appearance of mobile phones and WeChat made the post office lose almost all of its telecommunications business. In addition, the appearance of express companies also cut the post office’s express business by more than half. The post office was no longer so important in people’s lives, and fewer and fewer people went to it. (mine)")
PC = ("为了“活”下去，邮局扩大了自己的业务，开始了各种代理业务。代理保险，代售手机卡，代发工资，代收水电费，再次把人们的生活和邮局联系在一起，邮局又慢慢忙起来。邮局还改进了自己的快递业务，使年快递量达到四百亿件。现在，邮局不但活了下来，而且发展得越来越好，被人们叫做快递中的“国家队”，生活中的“万能手”。",
      "In order to “live” on, the post office expanded its business and started all kinds of agency business. Acting as an insurance agent, selling SIM cards, paying wages on behalf of companies and collecting water and electricity bills tied people’s lives and the post office together again, and the post office gradually became busy again. It also improved its express business so that the yearly express volume reached 40 billion items (the book writes 400 亿). Now the post office has not only survived but is developing better and better, and people call it the “national team” of express delivery and the “all-rounder” of daily life. (mine)")
L1 = lesson(
    "Lesson 20 Presentation 3: the post office then and now",
    "几十年前的邮局 · 电子邮件和微信 · 代理业务 · 国家队 万能手",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Can you name several traditional services offered by the U.S. post office? B. Do you know any additional services provided by the post office? C. What factors have impacted the post office’s operation in the U.S.? (Four small pictures, not included.)"),
        card("Presentation 3: 中国邮政的过去和现在",
             "The passage is in three paragraphs; the book also prints it in traditional characters. The percentage and the volume (80%, 400 亿) are written in characters here. The translations are mine.",
             examples=[D(*PA), D(*PB), D(*PC)]),
    ],
    exercises=[
        M("How did people in their forties and fifties remember the post offices of decades ago?", "Not big, but very busy", ["Big and empty", "Small and quiet", "New and modern"], "虽然不大，但是非常繁忙."),
        M("How often did people go to the post office back then?", "Every few days", ["Every day twice", "Once a year", "Never"], "每隔几天就要去一趟邮局."),
        M("Which of these did people do at the post office in those days?", "Subscribe to newspapers and magazines", ["Buy plane tickets", "Rent apartments", "Take exams"], "订报纸、杂志."),
        M("What cut the post office’s mail business by more than 80 percent?", "The invention of e-mail", ["Express companies", "Mobile phones", "The weather"], "电子邮件的发明."),
        M("What made the post office lose almost all its telecommunications business?", "Mobile phones and WeChat", ["E-mail", "The telegram", "Insurance"], "手机、微信的出现."),
        M("What cut the post office’s express business by more than half?", "The appearance of express companies", ["Telegrams", "Stamps", "The new year"], "快递公司的出现."),
        M("What did the post office do “in order to live”?", "Expanded its business with agency services", ["Closed half its offices", "Raised the prices", "Stopped sending letters"], "开始了各种代理业务."),
        M("Which of these is one of the agency businesses?", "代收水电费", ["代卖汽车", "代写作业", "代做饭"], "代收水电费."),
        M("How large did the yearly express volume become?", "Forty billion items", ["Four million", "Four hundred", "Forty thousand"], "年快递量达到四百亿件."),
        M("What do people now call the post office?", "The “national team” of express delivery and the “all-rounder” of daily life", ["The old shop", "The telegram office", "The slowest courier"], "快递中的“国家队”，生活中的“万能手”."),
        F("邮局和人们的日常生___简直是分不开。", "活", PART, "生活: life."),
        F("电子邮件的发___，却使邮局一下子减少了邮件业务。", "明", PART, "发明: invention."),
        F("邮局还改进了自己的快___业务。", "递", PART, "快递: express."),
    ],
)

# ------------------------------------------------------------------ 2. activities 1-5
KS = [("说起几十年前的中国邮政，四、五十岁的人都会记起那些虽然不大，但是非常繁忙的邮局。", "Paragraph C’s key sentence (first)"), ("可是，电子邮件的发明，却使邮局一下子减少了百分之八十以上的邮件业务。", "Paragraph A’s key sentence (first)"), ("为了“活”下去，邮局扩大了自己的业务，开始了各种代理业务。", "Paragraph B’s key sentence (first)")]
TL = table(["阶段 (mine)", "邮局的变化 (mine)"],
           [["几十年前", "邮局不大，但是非常繁忙，人们每隔几天就要去一趟"], ["电子邮件出现以后", "邮件业务一下子减少了百分之八十以上"], ["手机、微信出现以后", "几乎失去了所有的电讯业务"], ["快递公司出现以后", "快件业务少了一大半，去邮局的人越来越少"],
            ["邮局扩大业务以后", "代理保险、代售手机卡、代发工资、代收水电费，邮局又慢慢忙起来；快递改进了，年快递量达到四百亿件"], ["现在", "邮局活了下来，发展得越来越好，被叫做“国家队”和“万能手”"]],
           title="Activity 2B: the timeline of the post office (the book leaves the timeline blank; this is my filling)", say=[0, 1])
LS = [("说起几十年前的中国邮政，四、五十岁的人都会记起那些虽然不大，但是非常繁忙的邮局。", "1. Subject: 四、五十岁的人; verb phrase: 会记起; object: 那些…邮局. Speaking of the Chinese post of several decades ago, people in their forties and fifties will all remember those post offices that were not big but were very busy. (analysis and translation mine)"),
      ("电子邮件的发明，使邮局一下子减少了百分之八十以上的邮件业务。", "2. Subject: 电子邮件的发明; verb: 使 (the object 邮局 is also the subject of 减少了); object: 业务 (减少了…业务). The invention of e-mail suddenly cut the post office’s mail business by more than 80 percent. (mine)"),
      ("邮局还改进了自己的快递业务，使年快递量达到四百亿件。", "3. Subject: 邮局; verb: 改进了; object: 自己的快递业务; 使… makes the yearly express volume reach 40 billion items. The post office also improved its own express business, so that the yearly express volume reached 40 billion items. (mine)"),
      ("代理保险，代售手机卡，代发工资，代收水电费，再次把人们的生活和邮局联系在一起。", "4. Subject: the four agency services; 把 phrase: 把人们的生活和邮局; verb: 联系在一起. Acting as insurance agent, selling SIM cards, paying wages for others and collecting water and electricity bills tied people’s lives and the post office together again. (mine)"),
      ("邮局不但活了下来，而且发展得越来越好，被人们叫做快递中的“国家队”，生活中的“万能手”。", "5. Subject: 邮局; verbs: 活了下来, 发展, 被…叫做; object (of the passive): 国家队, 万能手. The post office has not only survived but is developing better and better, and people call it the “national team” of express delivery and the “all-rounder” of daily life. (mine)")]
TW1 = ("中华邮政的业务分为邮务和银行两大业务。邮政业务包括邮件寄送与快递，银行业务包括存款、提款、汇款，各种保险、房屋贷款。其他服务还包括集邮、代售商品等。中华邮政在全国各地共有邮局一千三百二十二处，如果把邮局当作是一般银行的分行，邮局是营业点最多的银行。",
       "Chunghwa Post’s business is divided into two big businesses, postal and banking. Postal business includes mail delivery and express, banking business includes deposits, withdrawals, remittances, all kinds of insurance and housing loans. Other services also include stamp collecting and selling goods as an agent. Chunghwa Post has 1,322 post offices across the country (the book writes 1322); if you regard post offices as branches of an ordinary bank, the post office is the bank with the most business locations. (the book prints it in traditional characters; translation mine)")
TW2 = ("近几年来，虽然电话、网际网络等电子通信方式的发达，以及其它快递公司的加入，使得中华邮政的邮务业务大量减少，但因邮局的快递与包裹服务等定价还是比其它快递公司便宜，因此，中华邮政的快递和包裹业务还是发展得相当快。另外，中华邮政的银行业务以及保险业务也已经远远超过邮局的邮政业务，成为邮局最挣钱的业务。邮局的存款金额更是全台湾银行中的第一位。",
       "In recent years, although electronic means of communication such as the telephone and the internet have developed, and other express companies have joined in, so that Chunghwa Post’s postal business has greatly decreased, the prices of the post office’s express and parcel services are still cheaper than those of the other express companies, so Chunghwa Post’s express and parcel business is still developing quite fast. In addition, Chunghwa Post’s banking and insurance businesses have already far surpassed its postal business and become the post office’s most profitable business. The post office’s deposit total is even number one among all banks in Taiwan. (the book prints it mostly in traditional characters; translation mine)")
DIFF = table(["相同的地方 (mine)", "不同的地方 (mine)"],
             [["邮局都有快递和包裹业务；电子通信和快递公司的出现都使邮政业务减少", "中华邮政分为邮务和银行两大业务，银行和保险是最挣钱的业务，存款是台湾第一；大陆的邮局靠代理业务和改进快递“活”了下来，年快递量达到四百亿件"]],
             title="Activity 5A: similarities and differences between the passage and Presentation 3 (the book leaves the table blank; this is my filling)", say=[0, 1])
OD = [("增加、发展、扩大、失去", "失去", "the others mean “grow/expand/increase”; 失去 is to lose"), ("但是、而且、不过、却", "而且", "the others all mean “but”; 而且 means “moreover”"), ("另外、加上、不过、还有", "不过", "the others all add information; 不过 means “but”"),
      ("发明、产生、出现、万能", "万能", "the others mean something comes into being; 万能 is “all-powerful”"), ("失去、增加、减少、降低", "增加", "the others mean to lose or decrease; 增加 is to increase")]
L2 = lesson(
    "Lesson 20 Presentation 3 activities: order, timeline, long sentences, odd one out, Taiwan",
    "Activities 1 to 5 · 段落顺序 · 邮局的变化 · 长句分析 · 找不同类的词 · 中华邮政",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking)",
             "A. Without reading the presentation, put Paragraphs A, B and C (printed in scrambled order) in a logical order and give the rationale. B. Read the presentation aloud to your partner to check your answer. C. Highlight the key sentence in each paragraph; did you notice where it stands? My order (the book prints no key): C, A, B. C describes the past (几十年前), A begins with 可是 and turns to what changed, and B begins with 为了“活”下去 and tells how the post office survived. The key sentence stands at the beginning of each paragraph:",
             examples=[D(z, e) for z, e in KS]),
        card("Activity 2 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 3 once and write a summary. B. Detailed listening: listen again and take notes on the changes to the post office on the timeline. C. Pair up and, in Chinese, share your answers; each partner reports one block of information and the students take turns reporting the entire story. D. Scan through the presentation again and identify the words and phrases that indicate the different stages of postal services (e.g. 几十年前, 那时候, 可是, 另外, 为了, 再次, 又, 现在). (Audio, not included; my timeline from the text:)",
             tables=[TL]),
        card("Activity 3 Long Sentence Analysis (Reading)",
             "A. In the sentences below, highlight the subject, verb/verb phrase and object in each sentence, then translate each sentence. B. Pair up and check your answers. The book prints the five sentences and leaves blanks; my analysis and translations:",
             examples=[D(z, e) for z, e in LS]),
        card("Activity 4 (Reading)",
             "Select the word that does not belong in the group: 1. 增加 | 发展 | 扩大 | 失去. 2. 但是 | 而且 | 不过 | 却. 3. 另外 | 加上 | 不过 | 还有. 4. 发明 | 产生 | 出现 | 万能. 5. 失去 | 增加 | 减少 | 降低. My answers (the book prints no key): 1. 失去 (the others mean grow, expand or increase); 2. 而且 (the others all mean “but”); 3. 不过 (the others add information); 4. 万能 (the others mean something comes into being); 5. 增加 (the others mean to lose or decrease)."),
        card("Activity 5 (Reading and Speaking)",
             "A. Compare the following passage (about Chunghwa Post in Taiwan, from zh.wikipedia.org) with the Presentation and write down any similarities or differences in the table. B. Can you guess the meaning of the new, underlined words 貸款, 集郵, 分行, 掙錢? My guesses: 贷款 a loan, 集邮 stamp collecting, 分行 a branch (of a bank), 挣钱 to earn money. The book prints the passage in traditional characters (simplified here):",
             tables=[DIFF], examples=[D(*TW1), D(*TW2)]),
    ],
    exercises=[
        M("In my order of the three paragraphs, which comes first?", "Paragraph C (decades ago)", ["Paragraph A", "Paragraph B", "They can come in any order"], "C, A, B."),
        M("Which paragraph begins with 可是?", "Paragraph A", ["Paragraph B", "Paragraph C", "None of them"], "可是，电子邮件的发明…"),
        M("Where does the key sentence usually stand in these paragraphs?", "At the beginning", ["At the end", "In the middle", "There is none"], "Each paragraph starts with its key sentence."),
        M("Which word does not belong: 增加, 发展, 扩大, 失去?", "失去", ["增加", "发展", "扩大"], "失去: to lose."),
        M("Which word does not belong: 但是, 而且, 不过, 却?", "而且", ["但是", "不过", "却"], "而且: moreover."),
        M("Which word does not belong: 另外, 加上, 不过, 还有?", "不过", ["另外", "加上", "还有"], "不过: but."),
        M("Which word does not belong: 发明, 产生, 出现, 万能?", "万能", ["发明", "产生", "出现"], "万能: all-powerful."),
        M("Which word does not belong: 失去, 增加, 减少, 降低?", "增加", ["失去", "减少", "降低"], "增加: increase."),
        M("What two big businesses does Chunghwa Post have?", "Postal business and banking", ["Express and parcels only", "Insurance and travel", "Newspapers and telegrams"], "邮务和银行两大业务."),
        M("What is the post office’s most profitable business in Taiwan?", "Banking and insurance", ["Letters", "Parcels", "Stamps"], "最挣钱的业务."),
        M("How does the passage describe the post office’s deposits?", "Number one among all banks in Taiwan", ["The lowest", "Equal to the other banks", "Unknown"], "全台湾银行中的第一位."),
        F("邮局是营业点最多的银___。", "行", PART, "银行: bank."),
        F("邮局的存款金___更是全台湾银行中的第一位。", "额", PART, "金额: amount."),
    ],
)

# ------------------------------------------------------------------ 3. 使 and 让
SH = table(["A", "使", "B"], [["Cause / condition", "使", "Result / effect (adjective or verb phrase)"]], title="The causative verb 使: A 使 B (adj. or verb phrase)")
SE = [("电子邮件的出现使邮局的邮政业务减少了一大半。", "(formal) The appearance of e-mail cut the post office’s postal business by more than half."), ("电子邮件的出现让邮局的邮政业务减少了一大半。", "(less formal) The same sentence with 让."),
      ("电子邮件的出现使邮局的邮政业务减少了一大半。", "(state) The result of 使 is a state: the postal business decreased."), ("邮政业务的减少让邮局开始增加许多代理业务。", "(action) The decrease of the postal business made the post office begin adding many agency businesses (an action, so 让)."),
      ("老师让同学明天带作业本来。", "(give orders) The teacher tells the students to bring their workbooks tomorrow. (the book prints 作业书, which I read as 作业本)"), ("妈妈让我做完作业看三十分钟电视。", "(give permission) Mom lets me watch thirty minutes of TV after I finish my homework. (the book writes 30)"),
      ("他让我午休的时候帮他买一杯咖啡。", "(make a request) He asked me to buy him a cup of coffee at the lunch break.")]
SA1 = [("来国防语言学院使我每天都得学很多汉字。", "Coming to the Defense Language Institute makes me have to learn many characters every day. (Student A, mine)"), ("去不同地方旅行使我认识了很多新朋友。", "Traveling to different places made me meet many new friends. (A, mine)"), ("玩电子游戏使我的眼睛很累。", "Playing video games makes my eyes very tired. (A, mine)"), ("手机的出现使人们的生活方便多了。", "The appearance of mobile phones made people’s lives much more convenient. (A, mine)"),
       ("参军使我更有责任感。", "Joining the army gives me a stronger sense of responsibility. (Student B, mine)"), ("上语法课使我更了解汉语的句子。", "Going to grammar class helps me understand Chinese sentences better. (B, mine)"), ("锻炼身体使我睡得更好。", "Exercising makes me sleep better. (B, mine)"), ("网路的发明使世界变小了。", "The invention of the internet made the world smaller. (B, mine)")]
SA2 = [("高铁的出现不仅使两地的距离变短了，而且也使人们的生活更加便利。", "1. 使 / 让 (both possible; the results are states): The appearance of the high-speed rail not only made the distance between two places shorter, but also made people’s lives more convenient. (key mine)"), ("我太太让我回家以前到超市去买些蔬菜水果。", "2. 让 only (a request): My wife asked me to go to the supermarket to buy some vegetables and fruit before coming home. (mine)"),
       ("航空公司不让旅客带液体或是易燃品上飞机。", "3. 让 only (permission): Airlines do not let passengers take liquids or flammable goods onto the plane. (mine; the book prints 或事, which I read as 或是)"), ("快递公司的出现使邮局的邮政业务减少了一大部分。", "4. 使 / 让 (both possible; the result is a state): The appearance of express companies cut a large part of the post office’s postal business. (mine)"),
       ("班长让我通知大家下午三点半到操场集合。", "5. 让 only (an order): The class monitor told me to notify everyone to gather at the playground at half past three in the afternoon. (mine; the book writes 三点半 in characters)")]
L3 = lesson(
    "Lesson 20 Presentation 3 grammar: the causative verb 使 (and 让)",
    "电子邮件的出现使邮局…减少了 · 使 比 让 正式 · 让 = 命令 允许 请求",
    requires=[],
    cards=[
        card("The Causative Verb 使",
             "The causative verb 使 is used to express the idea that A (the cause or condition) makes B change to a specific state or take an action (i.e., a result or effect): A 使 B (adjective or verb phrase). Although 使 and 让 can be translated as “make/cause” in English and are sometimes used interchangeably, they differ in their usage due to their meaning. 1. 使 tends to be used more in formal/written situations while 让 is used in a more colloquial style. 2. When 使 is used in a sentence, the result can be a state; when 让 is used the result can be either a state or an action. 3. 让 can also mean giving permission, making a request, or giving orders; in this situation only 让 is allowed.",
             tables=[SH], examples=[D(z, e) for z, e in SE]),
        card("Activity 1 (Reading and Speaking)",
             "Pair up. Each partner uses the topics in one of the columns to create a sentence using 使; the partner translates the sentence. For example: 学中文 → Student A: 学中文使我对中国文化感兴趣。 Student B: Learning Chinese makes me interested in Chinese culture. Student A’s topics: 来国防语言学院, 去不同地方旅行, 玩电子游戏, 手机的出现. Student B’s topics: 参军 (参加陆军/空军/海军), 上语法课/听力课/说话课, 锻炼身体, 网路的发明. My sentences:",
             examples=[D(z, e) for z, e in SA1]),
        card("Activity 2 (Reading)",
             "A. Complete the sentences with either 让 or 使, or both, and provide your rationale. B. Check your answers with your partner. The book prints the five sentences with blanks and no key; my answers:",
             examples=[D(z, e) for z, e in SA2]),
    ],
    exercises=[
        M("Which of 使 and 让 is more formal or written?", "使", ["让", "They are equally colloquial", "Neither"], "使 tends to be formal/written."),
        M("When can the result of 使 be an action?", "Not as a rule: 使 usually has a state as its result", ["Always", "Only in questions", "Only with 不"], "使: state; 让: state or action."),
        M("Which one can express giving permission?", "让 only", ["使 only", "Both", "Neither"], "Only 让 can give permission."),
        M("Which sentence is a request?", "他让我午休的时候帮他买一杯咖啡。", ["电子邮件的出现使邮局业务减少了。", "高铁使两地的距离变短了。", "班长使我很高兴。"], "让 = make a request."),
        M("Which sentence uses 让 to give an order?", "老师让同学明天带作业本来。", ["妈妈让我做完作业看三十分钟电视。", "他让我午休的时候帮他买一杯咖啡。", "电子邮件使邮局的业务减少了。"], "老师让同学…带作业本来."),
        M("Which sentence uses 让 to give permission?", "妈妈让我做完作业看三十分钟电视。", ["老师让同学明天带作业本来。", "邮政业务的减少让邮局开始增加许多代理业务。", "快递公司使邮局业务减少了。"], "妈妈让我…看电视."),
        M("Which blank takes only 让?", "我太太___我回家以前到超市去买些蔬菜水果", ["快递公司的出现___邮局的业务减少了", "高铁的出现不仅___两地的距离变短了", "电子邮件的出现___邮局的业务减少了"], "A request: only 让."),
        M("What does 邮政业务的减少让邮局开始增加许多代理业务 show?", "让 can be followed by an action", ["使 must be used", "The result is a state", "Nothing special"], "让 + action."),
        F("电子邮件的出现___邮局的邮政业务减少了一大半。", "使", PART, "使: made (formal)."),
        F("妈妈___我做完作业看三十分钟电视。", "让", PART, "让: let (permission)."),
        F("班长让我通知大家下午三点半到操___集合。", "场", PART, "操场: playground."),
    ],
)

# ------------------------------------------------------------------ 4. 被
BEI = table(["A (recipient)", "被", "B (doer)", "Verb (+ complement)"], [["邮局", "被", "人们", "叫做快递中的“国家队”"]], title="The passive voice with 被: A 被 B + verb (+ complement)")
BE1 = [("他被人打了。", "He was hit by someone. (the book’s adverse example)"), ("我们公司的申请表都被找工作的人拿完了。", "All of our company’s application forms were taken by job seekers. (the book’s adverse example)")]
BE2 = [("邮局被人们叫做快递中的“国家队”，生活中的“万能手”。", "1. The post office is called by people the “national team” of express delivery and the “all-rounder” of daily life."), ("他被选为我们的班长。", "2. He was elected our class monitor."), ("我们被分成两个小组。", "3. We were divided into two groups."), ("重庆又被叫做、称为中国的雾都。", "4. Chongqing is also called China’s “city of fog” (the book writes 叫做/称为 with a slash)."),
       ("这本书很受欢迎，被翻译成许多国的语言。", "5. This book is very popular and has been translated into the languages of many countries."), ("因为她的外语能力好，她常被派往许多城市出差。", "6. Because her foreign-language ability is good, she is often sent to many cities on business trips."), ("他高考考得很不错，所以被北京大学录取了。", "7. He did quite well in the college entrance exam, so he was admitted to Peking University.")]
RO = [("纽约被许多人叫做大苹果。", "1. New York is called the Big Apple by many people. (my order)"), ("芝加哥被当地人称为风城。", "2. Chicago is called the “Windy City” by the locals. (mine; the book prints 凤城, which I read as 风城)"), ("他被这所学校请去当语文老师。", "3. He was invited by this school to be a Chinese teacher. (mine)"),
      ("所有的家事都被我妈妈包了。", "4. All the housework has been taken over by my mother. (mine)"), ("每天早上六点他就被妈妈叫起来学习了。", "5. Every morning at six he is woken up by his mother to study. (mine; the book writes 6)"), ("包裹被邮局退回来了。", "6. The parcel was returned by the post office. (mine)")]
L4 = lesson(
    "Lesson 20 Presentation 3 grammar: the passive 被 in a neutral context",
    "被叫做 被称为 被选为 被分成 · 被翻译成 被派往 被录取 · 句子重组",
    requires=[],
    cards=[
        card("The Passive Voice of 被 in a Neutral Context",
             "被 is used to express the passive voice in a sentence. In a passive-voice sentence the object of an action becomes the subject of the sentence, and the doer of the action, which would have been the subject of the normal (active-voice) sentence, becomes secondary and may or may not be mentioned: A (recipient) 被 (B, doer) verb (+ complement). The 被 structure is often used to express an adverse or unfortunate situation, or to express the disposition of the object in the same way the 把 construction does; in this lesson we focus on 被 in a neutral context. There it often accompanies 为 or 做, as in 被称为, 被选为, 被叫做. Other neutral contexts are shown in examples 5 to 7. The book’s adverse examples first:",
             tables=[BEI], examples=[D(z, e) for z, e in BE1 + BE2]),
        card("Activity 3 (Reading and Speaking)",
             "Reorder the following phrases into a grammatically correct and logical sentence and then translate them. 1. 叫做 | 纽约 | 被 大苹果 | 许多人. 2. 当地人 称为 芝加哥 被 凤城. 3. 被 他 当 这所学校 请去 语文老师. 4. 我妈妈 包 家事 了 所有的 都 被. 5. 妈妈 叫起来 每天早上 6 点 他 就 被 学习 了. 6. 包裹 退回来 邮局 被 了. The book leaves the translation lines blank; my sentences and translations:",
             examples=[D(z, e) for z, e in RO]),
    ],
    exercises=[
        M("In a 被 sentence, what becomes the subject?", "The recipient of the action", ["The doer of the action", "The verb", "The time"], "The object of the action becomes the subject."),
        M("Where does the doer go in 被 sentences?", "After 被, before the verb (and it may be omitted)", ["Before the subject", "At the end", "It must be omitted"], "A 被 B verb."),
        M("Which words often go with 被 in a neutral context?", "为 and 做 (被称为, 被叫做)", ["了 and 过", "不 and 没", "吗 and 呢"], "被称为, 被选为, 被叫做."),
        M("“He was elected our class monitor.”", "他被选为我们的班长。", ["他选为被我们的班长。", "被他选为我们班长的。", "我们的班长选他被为。"], "被选为."),
        M("“We were divided into two groups.”", "我们被分成两个小组。", ["我们分被成两个小组。", "被我们分成两个小组。", "两个小组我们被分了成。"], "被分成."),
        M("Which is the correct order?", "纽约被许多人叫做大苹果。", ["被纽约许多人叫做大苹果。", "纽约叫做许多人被大苹果。", "许多人纽约被叫做大苹果。"], "New York is called the Big Apple by many people."),
        M("Which is the correct order?", "包裹被邮局退回来了。", ["包裹邮局被退回来了。", "被包裹邮局退回来了。", "邮局包裹被退回来了。"], "包裹被邮局退回来了."),
        M("Which sentence is an adverse (unfortunate) 被 example from the book?", "他被人打了。", ["他被选为我们的班长。", "我们被分成两个小组。", "重庆又被叫做中国的雾都。"], "他被人打了."),
        M("What does 他被北京大学录取了 mean?", "He was admitted to Peking University", ["He admitted Peking University", "He lost his job", "He taught at Peking University"], "录取: admit."),
        F("他___选为我们的班长。", "被", PART, "被选为: elected as."),
        F("邮局被人们叫___快递中的“国家队”。", "做", PART, "被叫做."),
        F("他高考考得很不错，所以被北京大学___取了。", "录", PART, "录取: admit."),
    ],
)

# ------------------------------------------------------------------ 5. 另外
LW = table(["词", "语气", "意思"], [["另外", "Softer tone, “by the way”", "By the way"], ["还有", "Stronger tone, more colloquial", "In addition to"], ["而且", "Stronger tone, more formal", "Furthermore"]], title="另外, 还有 and 而且 (the book’s table)")
LE = [("特快专递最快，另外，价钱也不贵。", "Express is fastest. By the way, the price isn’t high either. (pattern: sentence, 另外, sentence; mine)"), ("他会说中文，另外，他还会说日文。", "He can speak Chinese; in addition he can also speak Japanese. (另外 followed by 还; mine)"), ("邮局可以寄信，另外，也可以代收水电费。", "The post office can send letters, and in addition can collect utility bills. (另外 followed by 也; mine)")]
HOB = ("我喜欢跑步。原因有三个：第一，跑步对身体好。第二，跑步不用花很多钱，也不用找人一起去。另外，跑步以后我觉得很轻松，晚上睡得也好。而且在公园里跑步还可以认识很多新朋友。还有，每天早上跑步使我一天都很有精神。",
       "I like running. There are three reasons: first, running is good for the body. Second, running doesn’t cost much, and you don’t need to find someone to go with. In addition, after running I feel relaxed and I sleep well at night. Moreover, running in the park I can meet many new friends. Also, running every morning keeps me energetic all day. (my sample paragraph; the book leaves the space for your own hobby, reasons 1 to 3 and a short paragraph using 另外, 而且 or 还有)")
L5 = lesson(
    "Lesson 20 Presentation 3 grammar: 另外, 还有 and 而且",
    "另外 = by the way · 还有 = in addition to · 而且 = furthermore",
    requires=[],
    cards=[
        card("The Usage of 另外",
             "As a conjunction, 另外 can link two sentences, indicating “in addition to” or “besides.” It is often followed by 还 or 也: Sentence, 另外, Sentence. 另外, 而且 and 还有 share similar meanings and are often used interchangeably. However, compared to 而且 and 还有, 另外 has a softer tone and a meaning similar to the English “by the way,” so it is usually followed by a less important point that the speaker wants to mention. 还有 is stronger in tone, similar to “in addition to” and more colloquial, while 而且 also has a stronger tone, tends to be more formal and expresses “furthermore.”",
             tables=[LW], examples=[D(z, e) for z, e in LE]),
        card("Activity 4 (Writing)",
             "A. Think of your favorite hobby and write several reasons why you enjoy it (我喜欢(hobby)。原因：1. 2. 3.). B. Use the key elements from your list to write a short paragraph about your hobby using 另外, 而且 or 还有. My sample paragraph:",
             examples=[D(*HOB)]),
    ],
    exercises=[
        M("Which of 另外, 还有, 而且 has the softest tone?", "另外", ["还有", "而且", "They are the same"], "另外: softer, “by the way”."),
        M("Which is the most formal?", "而且", ["另外", "还有", "没有"], "而且: more formal, “furthermore”."),
        M("Which is the most colloquial?", "还有", ["另外", "而且", "但是"], "还有: more colloquial."),
        M("What usually follows 另外?", "A less important point the speaker wants to mention", ["The main point", "A question", "A command"], "另外: “by the way”."),
        M("What often follows 另外 in the same clause?", "还 or 也", ["不 or 没", "吗 or 呢", "了 or 过"], "另外，还… / 另外，也…"),
        M("Which pattern is correct?", "Sentence, 另外, sentence", ["另外 + noun only", "另外 at the end of a sentence", "Sentence 另外 另外"], "Sentence, 另外, Sentence."),
        M("Which sentence uses 另外 well?", "特快专递最快，另外，价钱也不贵。", ["特快专递另外最快价钱。", "另外特快专递而且。", "特快专递最快另外另外。"], "Sentence, 另外, sentence."),
        M("Which connector means “furthermore”?", "而且", ["另外", "还有", "不过"], "而且: furthermore."),
        F("邮局可以寄信，___外，也可以代收水电费。", "另", PART, "另外: in addition."),
        F("在公园里跑步还可以认识很多新朋友，___且还很便宜。", "而", PART, "而且: furthermore."),
        F("跑步对身体好。还___，跑步不用花很多钱。", "有", PART, "还有: also."),
    ],
)

# ------------------------------------------------------------------ 6. 所有的
SY = [("手机、微信的出现使邮局失去了所有的电讯业务。", "1. The appearance of mobile phones and WeChat made the post office lose all of its telecommunications business."), ("我们班所有的同学都是军人。", "2. All the students in our class are servicemen."), ("我把所有的时间都花在学习中文上。", "3. I spend all my time on studying Chinese."), ("他把他所有的钱都拿去买房子了。", "4. He took all his money and bought a house.")]
SY2 = [("梅西百货大楼所有的商品都打八折。", "1. All the goods in Macy’s department store are 20 percent off. (所有的 and 都 together)"), ("梅西百货大楼商品都打八折。", "2. The goods in Macy’s department store are all 20 percent off. (都 only)")]
A5 = [("大家都出去！", "Set 1, sentence 1: Everyone out! — correct (key mine)"), ("她的皮包里什么都没有。", "Set 2, sentence 1: There is nothing at all in her handbag. — correct (mine)"), ("音乐厅里所有的人都站了起来。", "Set 3, sentence 1: All the people in the concert hall stood up. — correct (mine)"), ("音乐厅里的人都站了起来。", "Set 3, sentence 2: The people in the concert hall all stood up. — also correct (mine)")]
A6 = [("今天所有的高铁票都卖完了。", "1. All of today’s high-speed rail tickets are sold out. (the book’s example, with 所有的)"), ("今天的高铁票都卖完了。", "2. Today’s high-speed rail tickets are all sold out. (the book’s example, with 都)"),
      ("机场里所有的人都在排队。", "3. All the people in the airport are queueing. (my sentence with 所有的; the book’s pictures are not included)"), ("机场里的人全都在排队。", "4. The people in the airport are all queueing. (mine, with 全都)"), ("这个商店所有的衣服都很便宜。", "5. All the clothes in this shop are cheap. (mine, with 所有的)"), ("这个商店的衣服全都很便宜。", "6. The clothes in this shop are all cheap. (mine, with 全都)")]
L6 = lesson(
    "Lesson 20 Presentation 3 grammar: 所有的 and 都",
    "所有的 + noun · 所有的和都一起用 · 什么都没有 · 全都",
    requires=[],
    cards=[
        card("The Use of 所有的",
             "所有的 serves as an adjective and is usually followed by a noun. It means “all,” or “all of …”: 所有的 + noun. 所有的 vs 都: 所有的 is an adjective, generally followed by a noun, while 都 is an adverb, usually placed after a subject and followed by a verb. 所有的 and 都 often appear together in one sentence to express the meaning “all.”",
             examples=[D(z, e) for z, e in SY + SY2]),
        card("Activity 5 (Reading)",
             "Choose the correct sentence and check your answer with a classmate. Set 1: 1. 大家都出去！ 2. 什么都出去！ 3. 所有的都出去。 Set 2: 1. 她的皮包里什么都没有。 2. 她的皮包里都没有。 3. 她的皮包里所有的都没。 Set 3: 1. 音乐厅里所有的人都站了起来。 2. 音乐厅里的人都站了起来。 3. 音乐厅里的人什么都站了起来。 The book prints no key; my choices are Set 1: 1; Set 2: 1; Set 3: 1 and 2 (2 is also correct but without the stress of 所有的), and 3 is wrong:",
             examples=[D(z, e) for z, e in A5]),
        card("Activity 6 (Speaking)",
             "Use the following pictures (five scenes, not included) to create two sentences using 所有的 and 全都. The example is at the high-speed rail station: 1. 今天所有的高铁票都卖完了。 2. 今天的高铁票都卖完了。 The book gives two blank lines for each picture; my sentences:",
             examples=[D(z, e) for z, e in A6]),
    ],
    exercises=[
        M("What kind of word is 所有的?", "An adjective, usually followed by a noun", ["An adverb", "A verb", "A measure word"], "所有的 + noun."),
        M("What kind of word is 都?", "An adverb, after the subject and before the verb", ["An adjective before a noun", "A noun", "A particle at the end"], "都 is an adverb."),
        M("Which sentence is correct?", "我把所有的时间都花在学习中文上。", ["我把所有的都时间花在学习中文上。", "我把所有时间花都在学习中文上。", "我所有的把时间都花在学习中文上。"], "所有的 + noun + 都 + verb."),
        M("How do you say “Everyone out!”?", "大家都出去！", ["什么都出去！", "大家什么出去！", "所有大家出去！"], "大家都出去."),
        M("How do you say “There is nothing at all in her handbag”?", "她的皮包里什么都没有。", ["她的皮包里都没有。", "她的皮包里所有的都没。", "她的皮包什么都有没有。"], "什么都没有."),
        M("Which sentence is correct?", "音乐厅里所有的人都站了起来。", ["音乐厅里的人什么都站了起来。", "音乐厅里所有的人什么站了起来。", "所有的音乐厅都人站了起来。"], "所有的人都…"),
        M("What does 梅西百货大楼所有的商品都打八折 mean?", "All the goods are 20 percent off", ["Everything is 80 percent off", "Nothing is on sale", "Only some goods are on sale"], "打八折: 20 percent off."),
        M("What did he do with all his money?", "他把他所有的钱都拿去买房子了。", ["他把钱放在银行里。", "他把钱给了朋友。", "他把钱丢了。"], "买房子."),
        F("手机、微信的出现使邮局失去了___有的电讯业务。", "所", PART, "所有的: all."),
        F("我们班所有的同学___是军人。", "都", PART, "都: all."),
        F("今天的高铁票全___卖完了。", "都", PART, "全都: all."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
SQ = [("你上次寄包裹是什么时候？你去哪儿寄？怎么寄？", "1. When was the last time you mailed a parcel? Where did you go to mail it? How?"), ("你平常寄信、寄贺卡吗？你什么时候会寄？", "2. Do you usually mail letters or greeting cards? When do you mail them?"), ("如果你不寄信，你常用什么方式和家人朋友联系？", "3. If you don’t mail letters, what way do you often use to keep in touch with family and friends?"),
      ("你用过邮局或银行的什么代理业务？", "4. What agency services of the post office or a bank have you used?"), ("你最常用美国邮局的哪个服务？为什么？", "5. Which U.S. Postal Service service do you use most often? Why?"), ("你租过美国邮局的信箱或用他们办过护照吗？你觉得怎么样？", "6. Have you rented a P.O. box at a U.S. post office or applied for a passport through them? What did you think?"),
      ("你网购以后退过东西吗？你怎么把东西寄回去？", "7. Have you returned something after buying online? How did you send it back?"), ("网路的发明使你增加了什么？减少了什么？失去了什么？", "8. What has the invention of the internet added for you? What has it reduced? What has it made you lose?")]
BG3 = ("我来美国以后才知道美国的邮局和台湾的邮局不太一样。第一，他们的颜色不同。美国邮局的颜色是蓝色，台湾的是绿色。第二，他们的服务也有些不一样。美国的邮局一般只办邮局的普通业务，不像台湾的邮局还有银行和许多其它的代理业务。所以美国人去邮局多半是为了寄信、寄包裹、买邮票、买信封什么的。另外，美国邮局还有一个特别的服务，那就是留交邮件的服务。要是你常出差或旅行，你可以在旅行或出差前，到邮局的网站填一张表，告诉邮局你什么时候不在家，这样邮局可以帮你保留信件。等你回到家，他们还会把信都送还给你。当然，你也可以亲自去邮局领取。最后，美国邮局还有一个台湾邮局没有的服务，那就是美国邮局可以代办护照。只要你先填好护照申请表，准备好照片和申请费，你就可以跟邮局预约一个时间到邮局去申请护照，非常方便。",
       "After I came to America I learned that American post offices and Taiwanese post offices are not quite the same. First, their colors are different: the American post office is blue, Taiwan’s is green. Second, their services are also somewhat different. American post offices generally handle only ordinary post-office business, not like Taiwan’s post office, which also has banking and many other agency services. So Americans mostly go to the post office to send letters, send parcels, buy stamps, buy envelopes and so on. In addition, the American post office has a special service, which is the hold-mail service. If you often go on business trips or travel, before you travel you can fill in a form on the post office’s website to tell the post office when you will not be at home, and then the post office can hold your mail for you. When you get home they will also send all the mail back to you. Of course you can also go to the post office in person and pick it up. Last, the American post office has a service the Taiwanese post office does not have: it can handle passports for you. As long as you first fill in the passport application form and prepare the photo and the application fee, you can make an appointment with the post office for a time to go there and apply for a passport, which is very convenient. (the book prints it in a mix of traditional and simplified characters; translation mine)")
CP = table(["项目", "美国的邮局 (mine)", "台湾的邮局 (mine)"],
           [["颜色", "蓝色", "绿色"], ["一般的服务", "一般只办邮局的普通业务：寄信、寄包裹、买邮票、买信封", "除了邮局业务以外，还有银行和许多其它的代理业务"], ["特别的服务", "留交邮件（出差或旅行时让邮局保留信件，回家后再送还）；代办护照（填好申请表，准备好照片和申请费，预约一个时间）", "没有代办护照的服务"]],
           title="Activity 3A: the post office in the U.S. and in Taiwan (the book leaves the table blank; this is my filling)", say=[1, 2])
L7 = lesson(
    "Lesson 20 Presentation 3 skill integration: your mailing habits, the U.S. and Taiwan post offices",
    "寄包裹的习惯 · 邮递员 · 美国的邮局和台湾的邮局 · 留交邮件 代办护照",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading and Speaking)",
             "A. Take a few minutes to study the following questions. Then use them to acquire information from your classmates and fill in the table. B. The class shares their findings in Chinese. The eight questions (the table is not included; the translations are mine):",
             examples=[D(z, e) for z, e in SQ]),
        card("Activity 2 (Listening and Speaking)",
             "New vocabulary: 邮递员 (yóudìyuán; postman or letter carrier). Listen to the conversation between Mark, a foreign student, and his Chinese friend Da Nian and answer: 1. What is the topic of the conversation? 2. What does the first speaker intend to do? Be specific. 3. What instructions are provided by the second speaker? 4. What alternative method is provided? (Audio, not included; the book prints no script.)"),
        card("Activity 3 (Reading, Speaking and Writing)",
             "A. Read the passage from a Chinese immigrant’s blog, take notes on the differences between the postal service in the U.S. and Taiwan, and fill in the table. B. Pair up and share your answers in Chinese with your partner. The passage, then my notes:",
             tables=[CP], examples=[D(*BG3)]),
        card("Activity 4 (Listening, Speaking and Writing)",
             "A. Listen to the passage about a past mailing service. Extract the EEIs and fill in the table: What business is reported? In what context was this business established? How was the business conducted? What impact did this business have? What ultimately happened to the business? Why? Then pair up and, in Chinese, share your answers. B. Conduct online research and, in Chinese, create a poster to introduce this business; post your work on Linoit. C. Each pair of students uses the poster to give an oral report about the service to the class in Chinese. (Audio, online research and posters are not included; the book does not name the service.)"),
    ],
    exercises=[
        M("What is a 邮递员?", "A postman or letter carrier", ["A postal clerk", "A postmaster", "A customs officer"], "邮递员."),
        M("What color is the American post office, according to the blogger?", "Blue", ["Green", "Red", "White"], "美国邮局的颜色是蓝色."),
        M("What color is Taiwan’s?", "Green", ["Blue", "Red", "Yellow"], "台湾的是绿色."),
        M("What do American post offices generally handle?", "Only ordinary post-office business", ["Banking and insurance", "Passports only", "Bills and tax"], "一般只办邮局的普通业务."),
        M("What do Americans mostly go to the post office for?", "Sending letters and parcels, buying stamps and envelopes", ["Opening bank accounts", "Paying water bills", "Buying insurance"], "寄信、寄包裹、买邮票、买信封."),
        M("What is the special 留交邮件 service?", "The post office holds your mail while you are away", ["The post office reads your mail", "The post office prints your mail", "The post office returns your mail"], "保留信件."),
        M("How do you start the hold-mail service?", "Fill in a form on the post office’s website", ["Phone your neighbor", "Go to a bank", "Write a letter to the president"], "到邮局的网站填一张表."),
        M("What service does the American post office have that Taiwan’s does not?", "Handling passport applications", ["Banking", "Express delivery", "Selling stamps"], "美国邮局可以代办护照."),
        M("What do you need for a passport application?", "The filled-in form, a photo and the application fee", ["Only a letter", "A parcel", "A bank account"], "护照申请表、照片和申请费."),
        M("Which question asks what the internet has made you lose?", "网路的发明使你增加了什么？减少了什么？失去了什么？", ["你上次寄包裹是什么时候？", "你平常寄信、寄贺卡吗？", "你网购以后退过东西吗？"], "Question 8."),
        F("要是你常出差或旅行，你可以到邮局的网站填一张___。", "表", PART, "表: form."),
        F("美国邮局可以代___护照。", "办", PART, "代办: handle on behalf."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
YT = ("你知道吗？到邮局寄信、寄包裹，不用赶在上班时间去。下班以后，还是可以寄东西。为了让老百姓的生活更方便，每个邮局外面都设有邮筒。台湾的邮筒分为红色和绿色的。寄一般的邮件得把信放进绿色的邮筒。绿色的邮筒分为左右两边。一边是寄到本市的信件，另一边是寄到别的县市的信件。如果你的信是快件或是要寄到国外的，那你就得把信放进红色的邮筒。不管你放的是哪个邮筒，寄之前，别忘了填好寄件人和收件人的姓名和地址。当然，最重要的是要贴上足够的邮票。这样邮局才不会把你的信退回来。如果你寄的是包裹，邮局外的邮筒放不进去，这也不要紧。虽然邮局通常营业到下午五点，但是有些邮局提供夜间的服务，最晚开到晚上九点。你只要上邮局的网站查一下就能找到这些信息。另外，多半的邮局星期六还上半天班，这下子，你就不用担心找不到时间去邮局了。",
      "Did you know? To mail letters or parcels at the post office you don’t have to rush there during working hours. After work you can still mail things. To make the people’s lives more convenient every post office has drop boxes outside. Taiwan’s drop boxes are divided into red and green ones. To send ordinary mail you must put the letter into the green box. The green box is divided into a left and a right side: one side is for letters to the same city, the other for letters to other counties and cities. If your letter is express mail or is going abroad, then you must put it into the red box. Whichever box you use, before mailing don’t forget to fill in the names and addresses of the sender and the recipient. Of course the most important thing is to put on enough stamps; only then will the post office not send your letter back. If you are mailing a parcel and the box outside the post office is too small for it, that’s also fine. Although post offices are usually open until five in the afternoon (the book writes 5 点), some offer night service and stay open until nine at night at the latest (9 点). You only need to check the post office’s website to find this information. In addition, most post offices work half a day on Saturday, so you don’t need to worry about not finding time to go to the post office. (the book has a full stop after “国外的”, which I changed to a comma; translation mine)")
IB = ("爱邮箱是一种新型的取、寄邮件体验，提供全年无休、自助领取、交寄包裹及退货的服务。您可上网在各地的邮局或车站找到爱邮箱。你不仅可以在爱邮箱寄信、寄包裹，也可用爱邮箱的地址，让收件人直接到爱邮箱领包裹，或是你也可以在网路购物后，请网购公司把你的商品直接寄送到爱邮箱，你再按领件时间到特定的爱邮箱取件就可以了。",
      "i-Mailbox (the book writes “i 邮箱”; since the examples are spoken I wrote the letter’s name, 爱, and use a comma for the slash in 取/寄) is a new kind of pick-up/mailing experience, offering year-round, self-service pickup, parcel posting and return services. You can find i-Mailboxes online at post offices and stations in various places. You can not only send letters and parcels at an i-Mailbox, but also use an i-Mailbox’s address and let the recipient pick up the parcel directly at the i-Mailbox; or after shopping online you can ask the online store to send your goods straight to an i-Mailbox and then pick them up there at the specified time. (translation mine; the book prints it in traditional characters)")
L8 = lesson(
    "Lesson 20 Presentation 3 using Chinese in context: drop boxes, i邮箱 and mailing services in Taiwan",
    "邮筒 红色和绿色 · 夜间的服务 · 爱邮箱 · 平信 限时邮件 挂号邮件",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking)",
             "New vocabulary: 邮筒 (yóutǒng; post office drop box). Sometimes this can also be called 邮箱 (yóuxiāng), but 邮箱 can also refer to the P.O. box or a mailbox in front of a house. A. Read the passage and answer: 1. Who is the intended audience? 2. What message does the passage try to convey? 3. What solutions are provided? List two. 4. Why are different colors mentioned? B. Pair up and, in Chinese, check your answers. My answers (the book prints none): 1. People who want to mail something but cannot go during working hours. 2. You don’t have to rush to the post office in working hours; you can mail things after work. 3. Drop boxes outside every post office; night service until nine; Saturday half-day. 4. The green box is for ordinary mail (left side for the same city, right side for other cities); the red box is for express mail and mail going abroad. The passage:",
             examples=[D(*YT)]),
        card("Activity 2 (Reading, Listening and Writing)",
             "In order to compete with the other express services, the post office in Taiwan has offered the i 邮箱 service. A. Read the short introduction below about this service and summarize the service it provides. My summary: it is a self-service pick-up and mailing point at post offices and stations, open all year without a break, where you can send letters and parcels, return goods, and have parcels (including online purchases) delivered to it and collect them at the specified time. B. Now use the link (a YouTuber’s video, 1:52–3:49, or a second video) to watch a video about using this service and, in Chinese, write instructions with bullet points for other internet users; post them on Linoit. (Videos and Linoit are not included.) The introduction:",
             examples=[D(*IB)]),
        card("Activity 3 (Listening and Speaking)",
             "A. Use the video link (0:39–3:54) to listen to a YouTuber talking about different mailing services in Taiwan and take notes. B. Match each mailing service in the left column (平信, 限时邮件, 挂号邮件, 限时挂号邮件, 挂号附回执, 限时挂号附回执) with its written description in the right column; some descriptions may have more than one answer. The descriptions: 1. 通常两个工作日寄到。 2. 收件人得签名两次，一张收据给邮局，一张收据寄回给寄件人。 3. 普通邮件，最慢也最便宜，需要三个工作日寄到。 4. 假日也会送。 5. 一天/24 小时寄到。 6. 得亲自去邮局寄。 7. 最贵，最快，最保险。 8. 可以放进信箱寄。 C. Pair up and check your answers in Chinese. (The video is not included and the book prints no key, so I give no key; 3 and 8 fit 平信 and 7 fits 限时挂号附回执 best on their face.)"),
        card("Activity 4 (Speaking, Listening and Writing)",
             "Scenario: as internet and e-mail use gain in popularity and more advanced communication technology emerges, fewer and fewer people use postal services in the U.S. As a result the U.S. postal service has gone through unprecedented challenges to survive. A. Form groups of three. Using what you have learned from this lesson and your opinion as a customer, discuss and identify the weaknesses and strengths of the U.S. postal service (strengths | weaknesses table) and share them in your group. B. With your group members, create a list of suggestions or recommendations helping the post office improve its services. C. Each group posts its work on Linoit and gives an oral report to the class. D. The class votes for the best suggestion list. (Discussion and posting are not included.)"),
    ],
    exercises=[
        M("What is a 邮筒?", "A post-office drop box", ["A P.O. box number", "A parcel form", "A stamp"], "邮筒: drop box."),
        M("Why are drop boxes useful?", "You can mail things after work hours", ["They are free", "They are bigger than the office", "They sell stamps"], "下班以后，还是可以寄东西."),
        M("What color is the box for ordinary mail in Taiwan?", "Green", ["Red", "Blue", "Yellow"], "寄一般的邮件得把信放进绿色的邮筒."),
        M("What does the left or right side of the green box tell you?", "Same city or other counties and cities", ["Parcels or letters", "Day or night", "Domestic or foreign"], "一边是寄到本市的信件，另一边是…别的县市."),
        M("Which letters go into the red box?", "Express mail and mail going abroad", ["Ordinary mail", "Parcels", "Postcards only"], "快件或是要寄到国外的."),
        M("What is the most important thing before mailing?", "Put on enough stamps", ["Sign your name", "Fold the letter", "Phone the post office"], "最重要的是要贴上足够的邮票."),
        M("When do some post offices close at the latest (night service)?", "At nine in the evening", ["At midnight", "At six", "At eleven"], "最晚开到晚上九点."),
        M("What do most post offices do on Saturday?", "Work half a day", ["Close all day", "Work all night", "Do banking only"], "星期六还上半天班."),
        M("What does the i邮箱 service offer?", "Self-service pickup, parcel posting and returns all year round", ["Only stamps", "Only banking", "Weekly service"], "全年无休、自助领取、交寄包裹及退货."),
        M("Why did Taiwan’s post office introduce it?", "To compete with other express services", ["To close offices", "To sell phones", "To print stamps"], "为了和其他快递服务竞争."),
        F("每个邮局外面都设有邮___。", "筒", PART, "邮筒: drop box."),
        F("这样邮局才不会把你的信退___来。", "回", PART, "退回来: send back."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 20 Presentation 3 vocabulary", "37 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 10. area studies
L10 = lesson(
    "Lesson 20 Area Studies: Postal Service in China",
    "1998年的改革 · 八万二千多个邮局 · E-post · EMS · 二十一世纪的邮政",
    requires=[],
    cards=[
        card("Postal Service in China (1)",
             "In 1998 China reformed its postal and telecommunications systems and established an independent postal service. The new postal service conforms to the global trend of postal service functions, and has become one of the most important carriers of information, commodities, and financial instruments in China. China Post has accelerated the development of postal services, improved service quality and made postal service more available all over the country. According to statistics from the State Post Bureau, the number of post offices is more than 82,000, with almost 60,000 located in rural areas. This greatly helps the country’s postal service."),
        card("Postal Service in China (2)",
             "Instead of traditional businesses such as post-delivery, philately, magazine and newspaper subscription services, China Post, the sole agency in charge of China’s nationwide post services, is relying more and more on postal savings deposits boxes for profit, and is now focusing on the development of E-post (electronic postal service), which includes online remittance, online shopping, online stamp collecting, online newspaper subscription and door-to-door parcel delivery. Post offices, with their eye-catching green emblems, are usually found on main streets, at railway stations, at airports and scenic spots. They are open daily from 09:00–17:00. Domestic mail is very fast and the cost is low, normally 0.8 yuan for local delivery, 1.2 yuan for inter-city mail, 2.50 yuan for Hong Kong and 5.50 yuan for foreign countries."),
        card("Postal Service in China (3)",
             "China’s postal service also offers Express Mail Service (EMS). After China joined the World Trade Organization (WTO) in 2001, fierce market competition emerged, with the arrival of many foreign companies. Several international express mail services, such as DHL, UPS, TNT and FedEx, have offices in major Chinese cities. China Post has established direct postal service policies with 220 countries and regions worldwide. China’s universal postal service is a government owed enterprise and has its own provision. Its provision, to some extent, has led the enterprise to become not only unprofitable but also suffer a deficit. To overcome this situation, China also initiated market-oriented services and is striving to actively compete, expand their market share and increase their postal income to meet social demands. In the 21st century, China’s postal service will be completely modernized. It will utilize the latest mechanization, automation and computerization, achieving rapid delivery, automated sorting, computerized operation, information-based management and other diversified services. The new system will play an important role in global postal affairs."),
    ],
    exercises=[
        M("What happened in 1998?", "China reformed its postal and telecommunications systems and set up an independent postal service", ["China joined the WTO", "The first post office opened", "EMS was banned"], "In 1998 China reformed…"),
        M("How many post offices are there, according to the State Post Bureau?", "More than 82,000", ["About 8,200", "About 820,000", "Exactly 60,000"], "more than 82,000."),
        M("How many of them are in rural areas?", "Almost 60,000", ["About 6,000", "About 82,000", "None"], "almost 60,000 located in rural areas."),
        M("What is China Post relying on more and more for profit?", "Postal savings deposits", ["Stamp sales", "Telegrams", "Newspapers"], "postal savings deposits."),
        M("What does E-post include?", "Online remittance, shopping, stamp collecting, newspaper subscription and door-to-door parcel delivery", ["Only e-mail", "Only telegrams", "Only phone cards"], "E-post list."),
        M("What do post office emblems look like?", "Eye-catching and green", ["Red", "Blue", "Yellow"], "eye-catching green emblems."),
        M("What are the daily opening hours?", "09:00–17:00", ["06:00–12:00", "10:00–22:00", "24 hours"], "09:00–17:00."),
        M("Normal postage for local delivery?", "0.8 yuan", ["1.2 yuan", "2.50 yuan", "5.50 yuan"], "0.8 yuan for local delivery."),
        M("Normal postage for Hong Kong?", "2.50 yuan", ["0.8 yuan", "1.2 yuan", "5.50 yuan"], "2.50 yuan for Hong Kong."),
        M("What happened in 2001?", "China joined the WTO and fierce market competition emerged", ["EMS started", "DHL left China", "The post office closed"], "After China joined the World Trade Organization in 2001…"),
        M("With how many countries and regions has China Post set up direct postal policies?", "220", ["22", "2,200", "120"], "220 countries and regions."),
        M("What is the outlook for the 21st century?", "A completely modernized postal service", ["Fewer offices", "No more parcels", "Only paper mail"], "completely modernized."),
    ],
)

UNIT = unit("第二十课 Presentation 3: 邮局的过去和现在, 使/让, 被, 另外, 所有的", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
