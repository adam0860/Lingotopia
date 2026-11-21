"""Unit 32: Lesson 11 (Banking) Presentation 2, from the book's texts: paying bills online, 怎么 for "why", 怎么样 for "how about it",
只要…就…, the bank passages and the HSBC brochure, and the vocabulary list. Audio, pictures and web pages are not included."""
from zh_auto import *
from zh_l11_vocab import VOC2

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

P2 = [
    ("张文", "大卫，我们中午一起去吃中餐，怎么样？", "David, let’s go and eat Chinese food at noon together; how about it?"),
    ("大卫", "今天不行，我得去银行交上网费。", "I can’t today; I have to go to the bank to pay the internet fee."),
    ("张文", "怎么不在网上交？又快又方便。", "Why don’t you pay online? It’s fast and convenient."),
    ("大卫", "我不知道怎么在网上交，听说很麻烦。", "I don’t know how to pay online; I hear it’s very troublesome."),
    ("张文", "不麻烦。只要在银行的网站上注册一下就行了。", "It’s not troublesome. You just register on the bank’s website, and that’s it."),
    ("大卫", "这么简单啊。", "It’s that simple?"),
    ("张文", "对，不过，你得设一个用户名和密码。", "Yes, but you have to set up a username and a password."),
    ("大卫", "除了交费以外，网上银行还有别的服务吗？", "Besides paying fees, does online banking have other services?"),
    ("张文", "有啊。你可以转账，汇款，也可以付信用卡账单。", "Yes. You can transfer funds, remit money, and also pay credit card bills."),
    ("大卫", "网上银行安全吗？", "Is online banking safe?"),
    ("张文", "很安全。和普通银行一样安全。", "Very safe. It’s as safe as an ordinary bank."),
    ("大卫", "行，我下午就在网上银行注册一下。", "Okay, I’ll register for online banking this afternoon."),
    ("张文", "现在可以一起去吃饭了吧？", "Now we can go to eat together, right?"),
    ("大卫", "好，我请你。", "Okay, my treat."),
]
CLOZE = [("听说那个小区的环境又好又安全，你怎么不在那儿买房子呢？", "I hear the environment of that neighborhood is both good and safe; why don’t you buy a house there?"), ("在银行开户，你只要先填一下开户申请表，再存入一些钱就行了。", "To open an account at the bank, you just fill in the application form first and then deposit some money."),
         ("在中国银行存钱，你可以存活期的，也可以存定期的，还可以直接存外币，然后取人民币。非常方便。", "At the Bank of China, you can deposit into a current account, or a fixed-term one, and you can even deposit foreign currency directly and then withdraw RMB. Very convenient."),
         ("网上银行的服务很多，除了交费，转账，汇款的服务以外，还有网上购物和付信用卡账单的服务。", "Online banking has many services: besides paying fees, transferring and remitting money, it also has online shopping and credit card bill payment."), ("这个周末我得去旧金山，所以不能和你一起去看电影了。", "This weekend I have to go to San Francisco, so I can’t go to the movies with you.")]
MATCH = [("我得交手机费和上网费", "d 网上交费"), ("我有五千美元要给我父母", "a 转账汇款"), ("我下个月到美国学习", "f 全球服务"), ("我不知道我的活期账户有多少钱", "b 电子现金账户"), ("我在购物网站上买东西", "c 电子支付"), ("我想要新的信用卡", "e 信用卡")]
L1 = lesson(
    "Lesson 11 Presentation 2: paying bills online (dialog)",
    "怎么不在网上交？ · 只要注册一下就行了 · 设一个用户名和密码",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. Do you bank online? What do you like most and least about it? B. What kind of online services do American banks provide? C. What services do you use regularly?"),
        card("Presentation 2: 张文 and 大卫 talk about online banking",
             "The book also prints the dialog in traditional characters (for example 只要在銀行的網站上註冊一下就行了).",
             examples=dlg(P2)),
        card("Activity 1 (Listening)",
             "A. Global listening: 1. What is this presentation about? 2. What is the relationship between the two speakers? B. Detailed listening: 1. What does Zhang Jun advise David to do and why? 2. According to Zhang Jun’s instructions, what does David need to do? 3. What are three or more related services discussed? 4. What is David’s main concern? 5. Who do you think will pay for lunch and why? (audio, not included; the book’s question names 张军 though the dialog has 张文). From the text: he advises paying online because it is fast and convenient; David has to register on the bank’s website and set a username and password; related services are transfers, remittances and credit card bills; his concern is that it may be troublesome and unsafe; David will pay for lunch (我请你)."),
        card("Activity 2 (Reading, Writing and Speaking): choose the patterns",
             "A. Pair up. Complete the five sentences with the patterns 得 + V, 怎么不…, 只要…就…, 又…又…, 可以…还可以… and 除了…还…. B. Read your sentences to the class, explain your grammar choices, then translate them. The book gives no key; the completed sentences are mine:",
             examples=[D(z, e, fixes={"得": "dei3"}) for z, e in CLOZE]),
        card("Activity 3 (Reading and Speaking): banking needs and online services",
             "Match your banking needs on the left with the relevant online banking services on the right (a 转账汇款, b 电子现金账户, c 电子支付, d 网上交费, e 信用卡, f 全球服务). Compare answers with a partner and explain your choices in Chinese. The book prints 5000 as digits. The matching is mine (item 4, checking a balance, is the closest fit to the e-cash account):",
             tables=[table(["你的需要", "网上银行服务"], MATCH, say=[0], title="Needs and services")]),
        card("Activities 4 and 5",
             "Activity 4 (Listening, Reading and Speaking). A. Listen to the voicemail and answer: 1. Who is the caller? 2. Why is she calling? 3. What instructions does the caller leave? 4. What advice do they give at the end? Check your answers with a partner. B. Read the script your teacher provides, then tell your partner in Chinese what you would do after listening to the voicemail (audio, not included). Activity 5 (Speaking and Writing). A. Interview two classmates about the types of online banking services they use and their reasons for using them; write the information in a table (Classmate, Bank, Online Services, Reason to Use) in pinyin. B. Exchange your classmate’s information with a partner in Chinese. C. In Chinese, ask your partner what online banking services they have yet to use, then ask the classmates who have used these services how to use them."),
    ],
    exercises=[
        M("What does 张文 suggest at the start?", "Having Chinese food together at noon", ["Going to the bank", "Going to a movie", "Studying together"], "我们中午一起去吃中餐，怎么样？"),
        M("Why can’t 大卫 go?", "He has to go to the bank to pay his internet fee", ["He has a class", "He has no money", "He is sick"], "我得去银行交上网费。"),
        M("What does 张文 say about paying online?", "It is fast and convenient", ["It is expensive", "It is unsafe", "It is slow"], "又快又方便。"),
        M("What is David’s worry about paying online?", "He has heard it is troublesome", ["It is too expensive", "He has no phone", "He has no bank card"], "听说很麻烦。"),
        M("What does he need to do to register?", "Register on the bank’s website", ["Go to the bank in person", "Call the bank", "Write a letter"], "只要在银行的网站上注册一下就行了。"),
        M("What does he need to set up?", "A username and a password", ["A bank card", "A phone number", "An address"], "设一个用户名和密码。"),
        M("Which services does online banking offer besides paying fees?", "Transfers, remittances and credit card bills", ["Only shopping", "Only loans", "Only ATMs"], "转账，汇款，也可以付信用卡账单。"),
        M("How safe is online banking, according to 张文?", "As safe as an ordinary bank", ["Less safe", "Not safe at all", "Safer than any bank"], "和普通银行一样安全。"),
        M("When will 大卫 register?", "This afternoon", ["Tomorrow", "Right now", "Next week"], "我下午就在网上银行注册一下。"),
        M("Who will pay for lunch?", "大卫", ["张文", "Each pays his own", "The bank"], "好，我请你。"),
        M("What does 怎么不在网上交？ mean?", "Why don’t you pay online?", ["How do you pay online?", "Where do you pay online?", "Who pays online?"], "怎么不…: why don’t you."),
        M("What does 转账 mean?", "Transfer funds", ["Remit money", "Open an account", "Fill in a form"], "转账."),
        F("我不知道怎么在网上___，听说很麻烦。", "交", PART, "交: pay."),
        F("只要在银行的网站上注册一下___行了。", "就", PART, "只要…就…"),
        F("网上银行还有别的服___吗？", "务", PART, "服务: service."),
        F("你得设一个用户名和___码。", "密", PART, "密码: password."),
    ],
)

# ------------------------------------------------------------------ 2. 怎么 (2), 怎么样 (2)
WHY = [("甲：陆老师今天怎么没来？", "Why didn’t Teacher Lu come today?"), ("乙：她去日本了。", "She went to Japan."), ("我们去旧金山那天，你怎么不多买几本中文书？", "The day we went to San Francisco, why didn’t you buy a few more Chinese books?"), ("明天要考试，你怎么还不看书？", "There is an exam tomorrow; why aren’t you studying yet?"), ("怎么今天早上空军没集合？", "Why didn’t the Air Force assemble this morning?"), ("怎么你又回答错了？", "How come you answered wrong again?"), ("怎么你不给你的父母打电话？", "Why don’t you call your parents?")]
STRESS = [("他怎么去中国？", "With 怎么 stressed: how is he going to China (by what means of transportation)?"), ("他怎么去中国？", "With 去中国 stressed: why is he going to China (why China specifically, or what compels him to go)?")]
CARDS = [("上个周末，我买了一双五百美元的皮鞋。", "Last weekend I bought a pair of leather shoes for 500 dollars."), ("昨天我在银行申请了一个活期账户。", "Yesterday I applied for a current account at the bank."), ("下个星期，我要签一个合同，租一个新的公寓。", "Next week I’ll sign a contract and rent a new apartment.")]
HOWABOUT = [("大卫，我们中午一起去吃中餐，怎么样？", "David, let’s go eat Chinese food at noon together; how about it?"), ("今天晚上咱们一起去看电影，怎么样？", "Let’s go see a movie together tonight; how about it?"), ("下课以后，去体育馆锻炼身体，怎么样？", "After class, how about going to the gym to work out?"), ("今天我不能给你打电话，明天怎么样？", "I can’t call you today; how about tomorrow?"), ("先生，你想吃什么？烤鸭怎么样？", "Sir, what would you like to eat? How about roast duck?"), ("这个周末是我的生日，大家到我家来玩玩，一起吃吃饭，怎么样？", "This weekend is my birthday; how about everyone coming to my place to hang out and have a meal together?")]
D3 = [("甲：昨天你没来上课，怎么也没打电话？", "You didn’t come to class yesterday; why didn’t you call either?"), ("甲：请问，在美国银行开账户怎么办手续？", "Excuse me, how do I go through the procedures to open an account at a US bank?"), ("甲：你老家冬天的天气怎么样？", "What is the winter weather like in your hometown?"), ("甲：今天晚上咱们一起去看电影怎么样？", "How about going to see a movie together tonight?")]
L2 = lesson(
    "Lesson 11 Presentation 2 grammar: 怎么 meaning “why”, and 怎么样 for “how about it?”",
    "怎么没来？ · 怎么不…？ · 怎么今天… · 一起去吃饭，怎么样？ · 烤鸭怎么样？",
    requires=[],
    cards=[
        card("The interrogative 怎么 (2): “why”, “how come”",
             "怎么 may be used to ask “why” or “how come”, as in 怎么不在网上交？ (Why don’t you pay online?). It can occur before or after the subject: Subject + 怎么 + Verb Phrase; 怎么 + Subject + Verb Phrase.",
             examples=[D(z, e) for z, e in WHY]),
        card("Stress changes the meaning",
             "The question 他怎么去中国？ can mean two different things, depending on where in the sentence the stress falls. When 怎么 is stressed, it means “how is he going to China?”, that is, by what means of transportation. When 去中国 is stressed, it means “why is he going to China?”, that is, why China specifically (and not someplace else), or what compels him to go there.",
             examples=[D(z, e) for z, e in STRESS]),
        card("Activities 1 and 2",
             "Activity 1 (Reading and Speaking). Form groups of three. Each student is assigned one index card by the teacher (A, B or C), reads the statement aloud, and the partners ask questions with 怎么 meaning “why” or “how come”. The book prints 500 as digits. The cards:",
             examples=[D(z, e) for z, e in CARDS]),
        card("Activity 2 (Listening, Writing and Speaking)",
             "A. Listen to a dialog. As you hear four sentences, pay attention to where the stress falls in each, write the stressed words in a table, then translate the sentences and check with a partner. B. Take turns asking your partner questions about the sentence content by stressing different words. (Audio, not included.)"),
        card("The interrogative 怎么样 (2)",
             "怎么样 can be used to ask for consent or an opinion in an open-ended way, similar to the English “How about it?” or “What do you think?” This use of 怎么样 most often appears after a noun or at the end of a sentence: Sentence + 怎么样？; Noun + 怎么样？",
             examples=[D(z, e) for z, e in HOWABOUT]),
        card("Activities 3 and 4",
             "Activity 3 (Reading, Writing, Speaking and Listening). Pair up. One student completes the questions with 怎么 or 怎么样 and the other answers them. The book gives no key; my completions of the four dialogs’ first lines:",
             examples=[D(z, e) for z, e in D3]),
        card("Activity 4 (Reading and Speaking)",
             "A. Pair up. Using 怎么样, take turns making proposals about each of the pictures (a birthday party 生日聚会, renting a house 租房子, applying for a new credit card 申请新的信用卡, a trip to San Francisco 旧金山旅行); your partner responds accordingly. B. Then use 怎么 to ask each other questions about these pictures. (The pictures are not included.)"),
    ],
    exercises=[
        M("What does 怎么 mean in 陆老师今天怎么没来？", "Why", ["How", "When", "Where"], "怎么 + negative: why didn’t."),
        M("What does 陆老师今天怎么没来？ ask?", "Why didn’t Teacher Lu come today?", ["How did Teacher Lu come?", "When did Teacher Lu come?", "Who didn’t come?"], "怎么没来."),
        M("What does 明天要考试，你怎么还不看书？ ask?", "Why aren’t you studying yet for tomorrow’s exam?", ["How do you study?", "When is the exam?", "Where do you study?"], "怎么还不…"),
        M("What does 怎么你又回答错了？ express?", "Why/how come you answered wrong again?", ["How do you answer?", "A request", "A statement of pride"], "怎么 + subject + verb phrase."),
        M("Where can 怎么 (why) occur?", "Before or after the subject", ["Only after the verb", "Only at the end", "Only before the subject"], "Subject + 怎么 + VP / 怎么 + subject + VP."),
        M("What does stressed 怎么 in 他怎么去中国？ mean?", "How is he going to China?", ["Why is he going to China?", "When is he going to China?", "Who is going to China?"], "By what means."),
        M("What does stressed 去中国 in 他怎么去中国？ mean?", "Why is he going to China?", ["How is he going to China?", "Where is China?", "When is he going?"], "Why China specifically."),
        M("What does 怎么样 ask for in 我们一起去吃饭，怎么样？", "Consent or an opinion: how about it?", ["The time", "The reason", "The way to do it"], "怎么样: How about it?"),
        M("Where does 怎么样 most often appear?", "After a noun or at the end of a sentence", ["At the start only", "Before the verb", "After the subject only"], "Sentence/noun + 怎么样？"),
        M("What does 烤鸭怎么样？ mean?", "How about roast duck?", ["How do you cook roast duck?", "Why roast duck?", "Where is the roast duck?"], "Noun + 怎么样？"),
        M("What does 今天我不能给你打电话，明天怎么样？ mean?", "I can’t call you today; how about tomorrow?", ["Why can’t you call?", "How do you call tomorrow?", "What did you do tomorrow?"], "明天怎么样？"),
        F("陆老师今天___么没来？", "怎", PART, "怎么没来: why didn’t come."),
        F("今天晚上咱们一起去看电影，___么样？", "怎", PART, "怎么样: how about it?"),
        F("明天要考试，你怎么___不看书？", "还", PART, "还不: still not."),
    ],
)

# ------------------------------------------------------------------ 3. 只要...就...
ZY = [("只要你好好学习，就一定能学好中文。", "As long as you study hard, you will certainly learn Chinese well."), ("只要好好学习，你就一定能学好中文。", "As long as you study hard, you will certainly learn Chinese well."), ("你只要好好学习，就一定能学好中文。", "As long as you study hard, you will certainly learn Chinese well."),
      ("只要你有空儿，我就来。", "As long as you have time, I’ll come."), ("你只要有空儿，我就来。", "As long as you have time, I’ll come."), ("只要明天不下雨，我们就去冲浪。", "As long as it doesn’t rain tomorrow, we’ll go surfing."), ("只要您说得慢一点儿，我们就能听懂。", "As long as you speak a little slower, we can understand."),
      ("你只要每天听录音，听力就一定能好起来。", "As long as you listen to recordings every day, your listening will certainly get better."), ("你只要存美元，就可以取人民币。", "As long as you deposit dollars, you can withdraw RMB.")]
ZYK = [("只要有用户名和密码，就可以登录网上银行。", "As long as you have a username and password, you can log in to online banking."), ("只要你中午有空，我们就一起去吃午饭。", "As long as you are free at noon, we’ll go to lunch together."), ("只要你手机可以上网，就可以用苹果地图。", "As long as your phone can go online, you can use Apple Maps."),
       ("只要银行今天开门，我们就去开账户。", "As long as the bank is open today, we’ll go open an account."), ("只要你有账号，就可以直接存美元。", "As long as you have an account number, you can deposit dollars directly."), ("只要你给我打折，我就买这件夹克。", "As long as you give me a discount, I’ll buy this jacket.")]
L3 = lesson(
    "Lesson 11 Presentation 2 grammar: 只要…就… (as long as)",
    "只要注册一下就行了 · 你只要存美元，就可以取人民币 · 只要明天不下雨，我们就去冲浪",
    requires=[],
    cards=[
        card("The construction 只要…就…",
             "The conditional construction 只要…就… is similar to the English “as long as X, (then) Y”: as long as X occurs, Y will follow. 只要在银行的网站上注册一下就行了 (As long as you register on the bank’s website, that’ll do it). The conjunction 只要 in the first clause indicates the condition; the correlative adverb 就 in the second clause indicates the result. The subject of the first clause comes either before or after 只要, while the subject of the second clause always comes before 就. Patterns: 只要 + Condition, 就 + Result. Same subject: 只要 + Subject + VP, 就 + VP; 只要 + VP, Subject + 就 + VP; Subject + 只要 + VP, 就 + VP. Different subjects: 只要 + Subject 1 + VP, Subject 2 + 就 + VP; Subject 1 + 只要 + VP, Subject 2 + 就 + VP.",
             examples=[D(z, e) for z, e in ZY]),
        card("Activity 5 (Reading, Speaking and Listening)",
             "A. Use 只要…就… to connect the conditions on the left with their logical results on the right: 1. 有用户名和密码 2. 你中午有空 3. 你手机可以上网 4. 银行今天开门 5. 你有账号 6. 你给我打折; a. 去开账户 b. 可以直接存美元 c. 买这件夹克 d. 可以登录网上银行 e. 一起去吃午饭 f. 可以用苹果地图. You also need to add the subjects in the second clause. Check your completed sentences with a partner. B. With your partner, take turns reading three of your sentences to the class. My matching:",
             examples=[D(z, e) for z, e in ZYK]),
        card("Activity 6 (Writing, Speaking and Listening)",
             "A. Using 只要…就…, write five things you would do, given all the right conditions. B. In groups of three, read your ideas to your group. C. Vote for the three most interesting ideas and read them to the class."),
    ],
    exercises=[
        M("What does 只要…就… mean?", "As long as X, then Y", ["Not only X, but also Y", "If X, then Y was not possible", "Because X, so Y"], "只要 gives the condition, 就 the result."),
        M("What does 只要 indicate?", "The condition", ["The result", "A contrast", "A reason"], "Conjunction in the first clause."),
        M("What does 就 indicate in this pattern?", "The result", ["The condition", "A contrast", "A question"], "Adverb in the second clause."),
        M("Where can the subject of the first clause go?", "Before or after 只要", ["Only before 只要", "Only after 就", "Only at the end"], "只要你… / 你只要…"),
        M("Where must the subject of the second clause go?", "Before 就", ["After 就", "After 只要", "At the end"], "Always before 就."),
        M("What does 只要明天不下雨，我们就去冲浪 mean?", "As long as it doesn’t rain tomorrow, we’ll go surfing", ["If it rains, we’ll go surfing", "We’ll go surfing tomorrow no matter what", "It never rains here"], "只要…就…"),
        M("What does 你只要存美元，就可以取人民币 mean?", "As long as you deposit dollars, you can withdraw RMB", ["You can only withdraw dollars", "Dollars can’t be deposited", "You need RMB to deposit dollars"], "只要…就…"),
        M("Which sentence is correct?", "只要你有空儿，我就来。", ["只要你有空儿，就我来。", "你有空儿只要，我就来。", "只要就你有空儿，我来。"], "就 follows the subject of the second clause."),
        M("Which is the best match for 只要银行今天开门，…?", "我们就去开账户。", ["我就买这件夹克。", "就可以用苹果地图。", "就可以登录网上银行。"], "Sensible pairing."),
        M("Which is the best match for 只要你给我打折，…?", "我就买这件夹克。", ["我们就去开账户。", "就可以用苹果地图。", "我们一起去吃午饭。"], "Sensible pairing."),
        F("___要你好好学习，就一定能学好中文。", "只", PART, "只要: as long as."),
        F("只要你有空儿，我___来。", "就", PART, "就 introduces the result."),
        F("你只要存美元，就可以___人民币。", "取", PART, "取: withdraw."),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
ADD = [("自动提款机", "zi4 dong4 ti2 kuan3 ji1", "ATM (automatic teller machine)"), ("自助", "zi4 zhu4", "self-service"), ("一次性", "yi2 ci4 xing4", "one-time; disposable")]
PJ = "中国建设银行成立于一九五四年十月一日，也叫做建行。它是中国五大国有商业银行之一。中国建设银行不仅在国内设有一万四千五百家分行，而且在美国、英国、法国、日本、韩国、香港、台湾等七十三个国家和地区设有分行。中国建设银行有多种服务，像存款取款、兑换外币、发行信用卡等。中国银行还设有网上银行。你可以在网上办理定期存款，注册电子钱包，也可以在网上付账单。网上银行可以为你提供一年三百六十五天，一天二十四小时的服务。中国建设银行除了有外币兑换、旅行支票等服务外，还有外语电话银行服务，为国外的客户提供英语、法语、德语、俄语、韩语等多语种服务。"
PJE = "China Construction Bank was founded on 1 October 1954 and is also called 建行. It is one of China’s five big state-owned commercial banks. Besides its 14,500 domestic branches, it has branches in 73 countries and regions including the USA, Britain, France, Japan, Korea, Hong Kong and Taiwan. It has many services, such as deposits and withdrawals, foreign currency exchange and issuing credit cards. (The book says 中国银行 here.) It also has online banking, where you can handle fixed-term deposits, register an e-wallet and pay bills online, 365 days a year, 24 hours a day. Besides foreign currency exchange and traveler’s checks, it also has a foreign-language telephone banking service offering English, French, German, Russian, Korean and other languages to customers abroad."
PG = "中国工商银行，也叫做工行，成立于一九八四年一月一日。中国工商银行在国内有三万多个分支，与国外五十多个国家和地区的四百一十家银行有业务往来。中国工商银行的服务非常多。它的电子银行业务包括：自助银行、电话银行、手机银行和网上银行。网上银行开通的城市有三百多个。客户不出家门就能够安全、方便地使用中国工商银行的网上银行服务。只要有用户名和密码，便能在世界各地进入网络银行。电子钱包和网上支付都很安全。除了开户、查询、转账等服务以外，客户也可以随时随地使用活期和定期存款、支票、信用卡、汇款和交费等网上银行服务。"
PGE = "The Industrial and Commercial Bank of China, also called 工行, was founded on 1 January 1984. It has more than 30,000 domestic branches and business ties with 410 banks in more than 50 countries and regions. Its services are very many. Its electronic banking includes self-service banking, telephone banking, mobile banking and online banking; online banking is available in more than 300 cities. Customers can use its online banking safely and conveniently without leaving home. As long as you have a username and password, you can get into online banking anywhere in the world. The e-wallet and online payment are both very safe. Besides opening accounts, inquiries and transfers, customers can also use current and fixed deposits, checks, credit cards, remittances and bill payment, any time and anywhere."
HS = [("如何注册使用汇丰个人网上银行", "How to register and use HSBC personal online banking"), ("客户朋友们：", "Dear customers:"),
      ("如何使用汇丰个人网银呢？这很简单。网银，就是我们常说的网上银行业务。您只要完成下面的几步，就可以马上开通和使用汇丰个人网上银行了。", "How do you use HSBC personal online banking? It’s very simple. 网银 is what we often call online banking business. As soon as you complete the steps below, you can immediately activate and use HSBC personal online banking."),
      ("一、阅读并接受银行条款", "1. Read and accept the bank’s terms"), ("请在个人网上银行注册页面阅读汇丰个人网上银行和电子账单及电子通知相关的条款，如果您接受这些条款，请点击注册页面上的「确认」。", "On the personal online banking registration page, please read the terms for HSBC personal online banking and e-bills and e-notices; if you accept these terms, please click “Confirm” on the registration page."),
      ("二、确认您的身份", "2. Confirm your identity"), ("只要您有汇丰中国个人银行账户，就可以用借记卡卡号或者您的个人电话号码开通个人网上银行。", "As long as you have an HSBC China personal bank account, you can activate personal online banking with your debit card number or your personal phone number."),
      ("三、设定网上银行账户", "3. Set up your online banking account"), ("您需要设定一个用户名和个人密码，我们将问您一些安全问题，以后在您需要重新设定登录信息时，可以用。", "You need to set a username and a personal password, and we will ask you some security questions, which can be used later when you need to reset your login information."),
      ("四、完成网上银行注册后，怎么登录个人网上银行？", "4. After completing online banking registration, how do you log in to personal online banking?"), ("在您完成个人网上银行注册后，您可以用您的个人网上银行用户名及个人密码登录个人网上银行服务，使用网上银行的服务。为了您的服务安全，我们会在您登录的时候，发给您一个手机短信，告诉您一个安全密码，您需要输入这个安全密码，才能完成登录我们的网上银行。", "After you complete registration, you can log in to the personal online banking service with your username and personal password and use its services. For the safety of your service, when you log in we will send you a text message with a security code; you need to enter this security code to complete logging in to our online banking.")]
L4 = lesson(
    "Lesson 11 Presentation 2 skill integration: bank passages and the HSBC online-banking brochure",
    "自动提款机 自助 一次性 · 中国建设银行 · 中国工商银行 · 如何注册使用个人网上银行",
    requires=[],
    cards=[
        card("Activities 1 and 2",
             "Activity 1 (Listening and Speaking). A. Listen to the dialog and answer: 1. Where does this conversation take place (choose the correct picture)? 2. What does the first speaker want to tell the second? 3. What else does he want to do? 4. What exactly does the second speaker explain to the first? 5. What does the second speaker say about Chinese people compared to Americans? B. In groups of three compare answers. C. In Chinese, tell the others about an online banking service you used recently, and why and how you used it. (Audio, not included.) Activity 2 (Reading, Listening and Speaking). A. Pair up. Based on the characters you already know, fill in the pinyin and English meanings for each word in the supplementary vocabulary table (补充词汇). B. Listen to the passage and mark four statements true or false: 1. This passage is about online bank registration. 2. You must be at least 16 years old to register. 3. Having a username and password is the safest way to use the bank’s services. 4. Services include logging in, checking accounts, paying bills, transferring money and ordering food. C. Listen again and fill in a table with the different ways to register (means of registration and procedure). D. Check your work with a partner, then read the script your teacher provides. E. In Chinese, tell your partner how you prefer to register for an account online and how to do it. (Audio, not included.) The supplementary vocabulary (my readings):",
             tables=[wtable(ADD, title="补充词汇")]),
        card("Activity 3 (Reading and Speaking): two banks",
             "A. These two passages are about different Chinese banks. Read the first while your partner reads the second, then fill in your table (bank name, when established, size/scale, online services, other services); look up any words you don’t know. B. Exchange information with your partner in Chinese, then complete the second table with details from the other bank. C. Discuss in Chinese: 1. Which bank is older? 2. Which bank is larger? 3. What are the differences and similarities in their services? 4. Which one would you bank with and why? The book prints the figures as digits; they are spelled out here. Passage 1, 中国建设银行 (the book says 中国银行 once, where 中国建设银行 is meant):",
             examples=[D(PJ, PJE)]),
        card("Passage 2",
             "中国工商银行:",
             examples=[D(PG, PGE)]),
        card("Activity 4 (Reading, Writing and Speaking): the HSBC brochure",
             "A. Pair up. Translate the title of this HSBC (汇丰银行) brochure, 如何注册使用汇丰个人网上银行. B. Optional: translate the numbered headings, then read the entire brochure. C. Write a summary of the brochure in Chinese, then read it to the class. The brochure (the slogan is 环球金融 地方智慧, “global finance, local knowledge”; the numbered headings are written 一 to 四 here):",
             examples=[D(z, e) for z, e in HS]),
    ],
    exercises=[
        M("What does 自动提款机 mean?", "ATM", ["Credit card", "Bank clerk", "Passbook"], "自动提款机."),
        M("What does 自助 mean?", "Self-service", ["Automatic", "Online", "Free"], "自助银行."),
        M("What does 一次性 mean?", "One-time; disposable", ["Always", "Many times", "Anytime"], "一次性."),
        M("When was 中国建设银行 founded?", "1 October 1954", ["1 January 1984", "1 October 1984", "1 January 1954"], "一九五四年十月一日。"),
        M("How many domestic branches does 中国建设银行 have?", "14,500", ["30,000", "410", "73"], "一万四千五百家分行."),
        M("In how many countries and regions does 建行 have branches?", "73", ["50", "14", "410"], "七十三个国家和地区."),
        M("When was 中国工商银行 founded?", "1 January 1984", ["1 October 1954", "1 January 1954", "1 October 1984"], "一九八四年一月一日。"),
        M("How many domestic branches does 工行 have?", "More than 30,000", ["14,500", "410", "More than 300"], "三万多个分支."),
        M("In how many cities is 工行’s online banking available?", "More than 300", ["More than 30,000", "More than 50", "410"], "三百多个."),
        M("Which bank is older?", "中国建设银行", ["中国工商银行", "They are the same age", "汇丰银行"], "1954 vs 1984."),
        M("Which bank has more domestic branches?", "中国工商银行", ["中国建设银行", "They are equal", "汇丰银行"], "30,000+ vs 14,500."),
        M("What do you need to log in to the HSBC online banking, besides username and password?", "A security code sent by text message", ["A fingerprint", "A paper form", "A bank visit"], "发给您一个手机短信，告诉您一个安全密码."),
        M("What does 条款 mean?", "Terms (of an agreement)", ["Account", "Bill", "Password"], "阅读并接受银行条款."),
        mean("借记卡", "jie4 ji4 ka3", "debit card", ["credit card", "passbook", "check"]),
        mean("身份", "shen1 fen4", "identity", ["bill", "password", "branch"]),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context
L5 = lesson(
    "Lesson 11 Presentation 2 using Chinese in context: a registration flow chart, and questions at Fudan",
    "网上银行注册流程 · 复旦大学 · 网上银行服务",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking)",
             "A. Pair up. While interning at an American bank in San Francisco, you and a colleague are tasked to create a flow chart to help Chinese customers register for online banking. Study the flow chart from a Chinese bank to understand the various steps (the flow chart is not included). B. Go to the website of an American bank and look at its online registration instructions; use them as a guide to create a flow chart in Chinese, draw it on a flip chart and post it on the wall. C. Write a list of your bank’s online services in Chinese. D. Present your work to the class in Chinese and answer any questions."),
        card("Activity 2 (Writing, Reading, Speaking and Listening)",
             "You and your classmates have just begun studies at Fudan University (复旦大学) in Shanghai. You have some questions about using the online banking services in China and try to find answers from each other and one of your professors. A. Each student writes their questions in Chinese and posts them on the wall. B. In groups of three, read each classmate’s questions, discuss answers, then write them down and post them on the wall. C. Each student now reads their questions aloud, and a student from the other group reads their answers to that student. D. Your teacher will also provide their answers. E. As a class, vote for the best answer to each different question."),
    ],
    exercises=[
        M("Who creates the flow chart in Activity 1?", "Two interns at an American bank", ["A Chinese bank manager", "A teacher", "A customer"], "You and a colleague are tasked to create a flow chart."),
        M("Who is the flow chart for?", "Chinese customers registering for online banking", ["American customers", "Bank clerks", "Students"], "To help Chinese customers register."),
        M("Where do you study in Activity 2?", "Fudan University in Shanghai", ["Qinghua University", "Taiwan Normal University", "Nanjing University"], "复旦大学."),
        M("Who answers the questions in Activity 2?", "Classmates and one of the professors", ["Only the bank", "Only the teacher", "Nobody"], "Find answers from each other and one of your professors."),
        mean("复旦大学", "fu4 dan4 da4 xue2", "Fudan University", ["Qinghua University", "Peking University", "Nanjing University"]),
        mean("设", "she4", "set up", ["pay", "register", "exchange"]),
    ],
)

L6 = vocab_lesson("Lesson 11 Presentation 2 vocabulary", "16 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十一课 银行 Presentation 2: online banking", [L1, L2, L3, L4, L5, L6])
