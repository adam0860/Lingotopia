"""Unit 31: Lesson 11 (Banking) Presentation 1, from the book's texts: opening an account and exchanging money, 怎么, reading decimals, 这么,
the dialogs, the bank web page, the exchange-rate joke and the vocabulary list. Audio, pictures, videos and web searches are not included."""
from zh_auto import *
from zh_l11_vocab import VOC1

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [
    ("大卫", "您好！我想开个账户，怎么办手续？", "Hello! I’d like to open an account. How do I go about it?"),
    ("营业员", "您想开定期的还是活期的？", "Would you like a fixed-term or a current account?"),
    ("大卫", "开活期的吧，可以随时取钱。", "A current account, please; I can withdraw money any time."),
    ("营业员", "那您先要填一下开户申请表。", "Then first you need to fill in the account application form."),
    ("大卫", "这是我的申请表。我要存三千美元，需要兑换成人民币吗？", "Here is my application form. I want to deposit 3,000 US dollars; do I need to exchange it into RMB?"),
    ("营业员", "不需要，您可以直接存美元，取人民币。请您再填一张存款单。", "No need; you can deposit US dollars directly and withdraw RMB. Please fill in a deposit slip too."),
    ("大卫", "填好了。对了，您可以现在就给我换一些人民币吗？", "Done. By the way, can you change some RMB for me right now?"),
    ("营业员", "可以。您要换多少？", "Yes. How much do you want to exchange?"),
    ("大卫", "今天美元对人民币的兑换率是多少？", "What is today’s exchange rate from US dollars to RMB?"),
    ("营业员", "一比六点九。", "One to six point nine."),
    ("大卫", "这么高？那我换三百美元吧。", "That high? Then I’ll exchange 300 dollars."),
    ("营业员", "您想要多大面值的？", "What denominations would you like?"),
    ("大卫", "请给我十张一百元的，二十张五十的，其他的随便。", "Please give me ten hundreds and twenty fifties; the rest, whatever."),
    ("营业员", "这是您的两千零七十块人民币。请点点。", "Here is your 2,070 yuan RMB. Please count it."),
    ("大卫", "谢谢。", "Thank you."),
]
VERBT = [("开", "账户，活期，定期"), ("办", "手续"), ("取", "人民币，美元"), ("填", "申请表，存款单"), ("存", "美元，人民币，定期，活期"), ("换", "人民币，美元"), ("问", "兑换率"), ("点", "人民币")]
RATE = [("美元", "0.0500", "0.0500", "0.2000", "0.3000", "0.5000", "0.7500", "0.7500"), ("英镑", "0.0500", "0.0500", "0.1000", "0.1000", "0.1000", "0.1000", "0.1000"), ("欧元", "0.0001", "0.0005", "0.0100", "0.0100", "0.0100", "0.0100", "0.0100"), ("日元", "0.0001", "0.0005", "0.0100", "0.0100", "0.0100", "0.0100", "0.0100"),
        ("港币", "0.0100", "0.0100", "0.1000", "0.2500", "0.5000", "0.7000", "0.7000"), ("加元", "0.0100", "0.0500", "0.0500", "0.0500", "0.3000", "0.4000", "0.4000"), ("瑞士法郎", "0.0001", "0.0001", "0.0001", "0.0001", "0.0001", "0.0001", "0.0001"), ("澳元", "0.0500", "0.1000", "0.6000", "0.6500", "0.7500", "0.8500", "0.8500"), ("新加坡元", "0.0001", "0.0005", "0.0100", "0.0100", "0.0100", "0.0100", "0.0100")]
L1 = lesson(
    "Lesson 11 Presentation 1: opening an account and changing money (dialog)",
    "我想开个账户 · 活期还是定期 · 兑换率是多少 · 请点点",
    requires=[],
    cards=[
        card("Lesson 11 objectives: 第十一课 银行 (Banking)",
             "By the end of the lesson you will be able to open an account and deposit money at a Chinese bank, exchange currency, discuss online banking registration and services, and explain how to use Mobile Pay in China. To do that you must master the core vocabulary and patterns, the interrogative 怎么 (1) and (2), how to read decimals, 这么, the interrogative 怎么样 (2), the construction 只要…就…, 以前 as a general time reference, 什么 (2) and the 把 construction. Area Studies: China’s banking system."),
        card("Getting Started",
             "Pair up and discuss. A. What did you do at the bank the last time you went there? B. Do you know how to open a bank account and deposit money in the U.S.? C. Do you know how to exchange USD for foreign currency?"),
        card("Presentation 1: 大卫 at the bank",
             "The book also prints the dialog in traditional characters (for example 您想開定期的還是活期的？). The book writes the amounts as 3,000 and 2,070; they are spelled out here.",
             examples=dlg(P1)),
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 1 once and answer: 1. Where does this conversation take place? 2. What does the customer want to do? B. Detailed listening: listen again and answer: 1. What are two instructions the clerk provides? 2. In what denominations does the customer want his money? (audio, not included.) From the text: at a bank; he wants to open an account; the clerk tells him to fill in the application form and a deposit slip; he wants ten 100-yuan notes and twenty 50-yuan notes."),
        card("Activity 2 (Reading, Writing and Speaking): the verb table",
             "Pair up. In the verb table, fill in appropriate objects chosen from the word bank (账户, 手续, 活期, 定期, 申请表, 人民币, 美元, 存款单, 兑换率) to complement the verbs 开, 办, 取, 填, 存, 换, 问 and 点. Read your answers to the class. The book gives no key; mine:",
             tables=[table(["Verb", "Object(s)"], VERBT, say=[0, 1], title="Verbs and their objects")]),
        card("Activity 3 (Reading and Speaking): the interest-rate table",
             "A. You want to open a savings account with USD at the Bank of China in Beijing. Compare the interest rates in the Foreign Currency Savings Interest Rate Table (外汇存款利率表, dated 2019-09-13), then write your preferred deposit option(s) in a table (preferred deposit type, currency, deposit amount). B. Discuss your choice with a partner in Chinese. The rates, as printed (the columns are 活期, then 定期: 7天通知, 一个月, 三个月, 六个月, 一年, 二年):",
             tables=[table(["货币", "活期", "7天通知", "一个月", "三个月", "六个月", "一年", "二年"], RATE, say=[0], title="外汇存款利率表")]),
        card("Activities 4 and 5",
             "Activity 4 (Listening, Reading and Speaking). A. Listen to a dialog and answer: 1. What does the customer want to do? 2. What does he need to do first? 3. How much money does he withdraw? 4. What denomination of bills does he want? 5. What should he do before leaving? Compare answers with a partner. B. Read the script your teacher provides and perform the dialog with your partner, switching roles (audio, not included). Activity 5 (Speaking, Writing and Reading): exchanging currency. A. Pair up. Look up today’s exchange rates, then take turns playing clerk and customer for three exchanges: USD 4,000 to RMB, USD 6,000 to RMB and RMB 12,000 to USD. B. With your partner, write a set of instructions in Chinese to help your classmates open a bank account and exchange currency at a Chinese bank (the title is 怎么在中国银行开账户), post them on Linoit.com and compare them with the other instructions posted there."),
    ],
    exercises=[
        M("Where does this conversation take place?", "At a bank", ["At a post office", "At a shop", "At a school"], "开个账户，办手续."),
        M("Which type of account does 大卫 choose?", "A current account (活期)", ["A fixed-term account (定期)", "A credit card", "A loan"], "开活期的吧。"),
        M("Why does he choose it?", "He can withdraw money any time", ["It pays more interest", "It needs no form", "It is free"], "可以随时取钱。"),
        M("What does the clerk ask him to fill in first?", "The account application form", ["A loan form", "A tax form", "A visa form"], "先要填一下开户申请表。"),
        M("How much does he deposit?", "3,000 US dollars", ["300 US dollars", "30,000 US dollars", "3,000 RMB"], "我要存三千美元。"),
        M("Does he need to exchange the dollars into RMB first?", "No, he can deposit dollars and withdraw RMB", ["Yes, he must", "Yes, at another bank", "No, he cannot withdraw RMB"], "您可以直接存美元，取人民币。"),
        M("What is the exchange rate?", "1 to 6.9", ["1 to 69", "1 to 0.69", "1 to 7.9"], "一比六点九。"),
        M("How much does he exchange?", "300 US dollars", ["3,000 US dollars", "30 US dollars", "600 US dollars"], "我换三百美元吧。"),
        M("What denominations does he want?", "Ten 100s and twenty 50s, the rest whatever", ["All 100s", "All 50s", "Only coins"], "十张一百元的，二十张五十的，其他的随便。"),
        M("How much RMB does he get?", "2,070 yuan", ["207 yuan", "20,700 yuan", "3,000 yuan"], "两千零七十块人民币。"),
        M("What does the clerk ask him to do at the end?", "Count the money", ["Sign the form", "Show his ID", "Pay a fee"], "请点点。"),
        M("What does 兑换 mean?", "To exchange; convert", ["To deposit", "To withdraw", "To count"], "兑换成人民币."),
        M("What does 随便 mean?", "Casual(ly); as you please", ["Anytime", "Directly", "Quickly"], "其他的随便."),
        F("我想开个账户，怎么___手续？", "办", PART, "办手续: go through the formalities."),
        F("您想开定期的还是___期的？", "活", PART, "活期: current."),
        F("请您再填一张存___单。", "款", PART, "存款单: deposit slip."),
        F("今天美元对人民币的兑换___是多少？", "率", PART, "兑换率: exchange rate."),
    ],
)

# ------------------------------------------------------------------ 2. 怎么 (1)
ZM = [("这个表怎么填？", "How do I fill in this form?"), ("我怎么兑换外币？", "How do I exchange foreign currency?"), ("你常常怎么锻炼身体？", "How do you usually work out?"), ("你怎么学中文？", "How do you study Chinese?"), ("怎么写你的中文名字？", "How do you write your Chinese name?"), ("在中国的银行，怎么开户？", "At a bank in China, how do you open an account?")]
ZM1 = [("请问去农贸市场怎么走？", "Excuse me, how do I get to the farmers’ market?"), ("营业员，请问定期存款怎么存？", "Clerk, how do I make a fixed-term deposit?"), ("王老师，中国的饺子很好吃，请问怎么做？", "Teacher Wang, Chinese dumplings are delicious; how are they made?"), ("这个字我不认识，请问怎么读？", "I don’t know this character; how is it read?"), ("我还没有找到住的地方，请问怎么找房子？", "I haven’t found a place to live yet; how do I look for a house?"), ("这个苹果手机是新的，你知道怎么用吗？", "This Apple phone is new; do you know how to use it?")]
DEC = [("0.1", "零点一"), ("0.02", "零点零二"), ("0.13", "零点一三"), ("0.28", "零点二八"), ("0.305", "零点三零五"), ("1.1", "一点一"), ("1.3", "一点零三"), ("2.24", "二点二四"), ("6.98", "六点九八"), ("12.01", "十二点零一"), ("20.305", "二十点三零五"), ("22.44", "二十二点四四")]
RATES17 = [("英镑", "100", "880.02"), ("美元", "100", "660.99"), ("港币", "100", "84.59"), ("新台币", "100", "22.00"), ("日元", "100", "5.870"), ("加元", "100", "514.96"), ("新西兰元", "100", "462.62")]
RATEK = [("美元", "6.6099", "六点六零九九"), ("日元", "0.0587", "零点零五八七"), ("英镑", "8.8002", "八点八零零二"), ("加元", "5.1496", "五点一四九六"), ("港币", "0.8459", "零点八四五九")]
L2 = lesson(
    "Lesson 11 Presentation 1 grammar: 怎么 (how) and reading decimals",
    "这个表怎么填？ · 怎么办手续 · 零点一 · 一点零三 · 二点二四",
    requires=[],
    cards=[
        card("The interrogative 怎么 (1)",
             "怎么 can be used to ask “how”, as in 我想开个账户，怎么办手续？ (I’d like to open an account. How do I apply?). When 怎么 is used as an interrogative adverb to ask how to carry out a specific action, it occurs between the subject and its predicate: Subject + 怎么 + Verb?",
             examples=[D(z, e) for z, e in ZM]),
        card("Activities 1 and 2",
             "Activity 1 (Reading, Writing and Speaking). Complete the six sentences using 怎么, then pair up and read your partner’s questions aloud: 1. 请问去农贸市场___? 2. 营业员，请问定期存款___? 3. 王老师，中国的饺子很好吃，请问___? 4. 这个字我不认识，请问___? 5. 我还没有找到住的地方，请问___? 6. 这个苹果手机是新的，你知道___? The book gives no key; my completions:",
             examples=[D(z, e) for z, e in ZM1]),
        card("Activity 2 (Writing, Speaking and Listening)",
             "A. You and a partner have just arrived at Qinghua University (清华大学) to begin advanced Chinese studies at the Inter-University Program (IUP, or “Stanford Center”). Write four “how to” questions using 怎么 to ask the University’s International Office. B. Read your list to the class; the class combines the ten best questions into a new list. C. Call the International Office and ask your questions in turn; your teacher plays the representative who answers the phone."),
        card("How to read decimals",
             "Numbers before the decimal point are read the same as integers (whole numbers). Zeros before the decimal point are read 零. Decimal points are read as 点(儿), meaning “point” or “dot”. Numbers after the decimal point are read separately as digits. Patterns: 零 + 点 + Digits; Integer + 点 + Digits.",
             tables=[table(["Number", "Reading"], DEC, say=[1], title="Reading decimals")]),
        card("Activity 3 (Reading and Writing): exchange rates",
             "A. Look up the exchange rates for the currencies in the table dated 2017年12月15日星期五 (人民币兑换率 for 100 units of each foreign currency), then complete the sentences by writing the rates in decimals; for example the rate for euros to renminbi is 1:7.78 (= 100:778.30). B. With your partner, use an online currency converter to write today’s exchange rates in Chinese for 英镑, 美元, 港币, 新台币, 日元, 加元 and 新西兰元 (1 unit each). C. Which is higher, the exchange rate for USD to renminbi in part A, or today’s? What might be the cause? The 2017 table and my readings of the five rates:",
             tables=[table(["外币", "Amount", "人民币兑换率"], RATES17, say=[0], title="2017-12-15"), table(["Currency", "Rate", "Reading"], RATEK, say=[0, 2], title="The five rates, as decimals")]),
        card("Activity 4 (Speaking)",
             "A. You and two partners want to visit Hong Kong, Taiwan or Beijing. Look up the exchange rates in the three places and fill in a table (Destination, Exchange Rate, Estimated Cost of Trip). B. In Chinese, discuss which destination you want to go to and why. C. In Chinese, report to the class or teacher what you have decided, with the reasons, the exchange rate and the estimated cost of a trip."),
    ],
    exercises=[
        M("Where does 怎么 go in a question about how to do something?", "Between the subject and the predicate", ["At the start", "At the end", "After the object"], "Subject + 怎么 + verb."),
        M("What does 这个表怎么填？ ask?", "How do I fill in this form?", ["Where is this form?", "Who fills in the form?", "Why fill in the form?"], "怎么填: how to fill in."),
        M("What does 我怎么兑换外币？ ask?", "How do I exchange foreign currency?", ["Where do I deposit money?", "How much is a dollar?", "When do I exchange?"], "怎么兑换."),
        M("What does 怎么写你的中文名字？ ask?", "How do you write your Chinese name?", ["What is your Chinese name?", "Who wrote your name?", "Why write your name?"], "怎么写."),
        M("How is 0.1 read?", "零点一", ["一点零", "零一点", "点零一"], "零 + 点 + digits."),
        M("How is 0.02 read?", "零点零二", ["零点二", "零二点", "二点零"], "Digits separately."),
        M("How is 1.3 read?", "一点三", ["十三点", "一点十三", "一点零三"], "1.3 = 一点三."),
        M("How is 2.24 read?", "二点二四", ["二点二十四", "二十四点二", "二点二百四"], "Digits after the point are read separately."),
        M("How is 12.01 read?", "十二点零一", ["十二点一", "十二点零十", "一二点零一"], "Integer + 点 + digits."),
        M("How is 20.305 read?", "二十点三零五", ["二十点三百零五", "二点三零五", "二十点三五"], "Digits separately."),
        M("What does 点 mean in decimals?", "Point; dot", ["Zero", "Or", "Ratio"], "Decimal points are read as 点(儿)."),
        F("这个表___么填？", "怎", PART, "怎么填: how to fill in."),
        F("请问去农贸市场怎么___？", "走", PART, "怎么走: how to get there."),
        F("0.1 读作：零___一", "点", PART, "零点一."),
    ],
)

# ------------------------------------------------------------------ 3. 这么
ZE1 = [("这么高？那我换三百美元吧。", "That high? Then I’ll exchange USD 300."), ("这个汉字应该这么写。", "This Chinese character should be written like this.")]
ZE2 = [("今天的天气这么冷，我不想出去了。", "The weather is so cold today that I don’t want to go out."), ("“做饭日”做的饭这么多，我们都吃不完。", "So much food was made on “cooking day” that we can’t finish it all."), ("这双皮鞋这么大，我穿不了。", "These shoes are so big that I can’t wear them."), ("这么走，什么时候才可以走到？", "Walking like this, when will we ever get there?"), ("我这么麻烦你，真是非常不好意思。", "I’m troubling you so much; I’m really very sorry.")]
L3 = lesson(
    "Lesson 11 Presentation 1 grammar: 这么 (so; in this way)",
    "这么高？ · 这么写 · 这么冷 · 这么多 · 这么麻烦你",
    requires=[],
    cards=[
        card("这么",
             "这么 is placed before adjectives and verbs to convey the meaning “so…” or “in such a manner”. Patterns: 这么 + Adjective; 这么 + Verb.",
             examples=[D(z, e) for z, e in ZE1] + [D(z, e) for z, e in ZE2]),
        card("Activities 5 and 6",
             "Activity 5 (Listening): listen to the dialog, answer the questions, then compare answers with a partner: 1. Where are the two speakers and what is their relationship? 2. What does the first speaker want to do and why? 3. What is the second speaker’s concern? 4. What are three details about the first speaker? 5. What does the first speaker finally decide to do and why? (audio, not included). Activity 6 (Speaking, Writing and Listening): A. In groups of three, take turns describing one of the pictures using 这么 (pictures, not included). B. As a group, write a short paragraph of six to eight sentences describing your classroom and classmates using 这么, then read it to the class."),
    ],
    exercises=[
        M("Where is 这么 placed?", "Before adjectives and verbs", ["After nouns", "At the end of a sentence", "Before numbers only"], "这么 + adjective / verb."),
        M("What does 这么 convey?", "“So…” or “in such a manner”", ["“If…”", "“Because…”", "“Although…”"], "so / in this way."),
        M("What does 这么高？ express?", "Surprise: that high?", ["A request", "A condition", "A past event"], "这么 + adjective."),
        M("What does 这个汉字应该这么写 mean?", "This character should be written like this", ["This character is hard to write", "I wrote the character", "Do not write it"], "这么 + verb: this way."),
        M("What does 今天的天气这么冷，我不想出去了 mean?", "It’s so cold today that I don’t want to go out", ["It’s cold, so I’ll go out", "It was cold yesterday", "I like cold weather"], "这么冷: so cold."),
        M("What does 这双皮鞋这么大，我穿不了 mean?", "These shoes are so big that I can’t wear them", ["These shoes are too small", "I wear these shoes often", "I want bigger shoes"], "穿不了: can’t wear."),
        M("What does 我这么麻烦你，真是非常不好意思 mean?", "I’m troubling you so much; I’m very sorry", ["You trouble me", "I am not sorry", "I will trouble you later"], "这么麻烦你."),
        M("Which sentence uses 这么 + verb?", "这个字应该这么写。", ["今天这么冷。", "这个苹果这么大。", "他这么高。"], "这么写: write like this."),
        F("___么高？那我换三百美元吧。", "这", PART, "这么高: that high?"),
        F("这个汉字应该这___写。", "么", PART, "这么写."),
        F("今天的天气这么冷，我不想出去___。", "了", PART, "不想…了."),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
TF1 = [("在银行存美元，需要先填表，开个账户。", "To deposit US dollars at a bank, you need to fill in a form first and open an account."), ("活期存款和定期存款没什么不同。", "Current and fixed deposits are not different."), ("活期存款可以随时取钱，比较方便。", "With a current deposit you can withdraw money any time, which is more convenient."), ("小陈开了一个定期存款账户。", "Xiao Chen opened a fixed-term deposit account."),
       ("营业员需要看小陈的学生证。", "The clerk needs to see Xiao Chen’s student ID."), ("小陈第一次开账户就存了五千美元。", "Xiao Chen deposited 5,000 US dollars the first time he opened the account."), ("小陈只能提取人民币。", "Xiao Chen can only withdraw RMB.")]
WEB = "在中国的银行开户，可以有两种选择：活期账户或定期账户。活期存款账户没有存期要求，可以用银行卡或存折在银行的营业厅或自动取款机上随时存款或提取现金。人民币活期存款一元起存，外币活期存款金额为不低于人民币二十元的外汇。定期存款一般来说是不能随时取的，存款时间可以是三个月，也可以是十年以上。定期存款的存款时间越长，利率就越高。定期开户五十元起存。你可以直接把现金存为定期存款，用卡就可以存钱，现在的存款卡叫做“一卡通”。定期存款提取方式有三种：第一种：到期的时候，取出全部的存款，银行给你所有的利息；第二种：到期以前取出全部的存款，银行按取钱那一天的活期存款利率计算利息；第三种：到期以前取一部分的存款，提出来的钱的利息按活期计算，别的还是按定期算。另外，你可以把定期换成活期，也可以把活期换成定期。"
WEBE = "There are two options for opening an account at a bank in China: a current account or a fixed-term account. A current account has no deposit-period requirement; you can deposit or withdraw cash any time with a bank card or passbook at the bank’s hall or at an ATM. A current RMB deposit starts from 1 yuan, and a current foreign-currency deposit must be foreign exchange worth no less than 20 yuan. A fixed-term deposit generally cannot be withdrawn at any time; the term can be 3 months or more than 10 years, and the longer the term, the higher the interest rate. A fixed-term account starts from 50 yuan. You can deposit cash directly as a fixed deposit, and with a card you can deposit money; the current deposit card is called the “One Card”. There are three ways to withdraw a fixed deposit: first, at maturity you take out the whole deposit and the bank gives you all the interest; second, if you take out the whole deposit before maturity, the bank calculates the interest at the current-deposit rate of the day you withdraw; third, if you take out part of the deposit before maturity, the interest on the part withdrawn is calculated at the current rate and the rest still at the fixed rate. You can also change a fixed deposit into a current one, or a current one into a fixed one."
JOKE = "有个美国人到中国旅游，用十万美元兑换到六十八万元人民币。他在中国吃喝玩乐了一年，花了十八万元人民币。一年后，他准备回国，于是到银行兑回美元，此时人民币升值，这位美国人用剩下的五十万元人民币换到了十万美元。来时十万美元，回去还是十万美元，等于没花钱，他高高兴兴地回家了。"
JOKEE = "An American went to China to travel and exchanged 100,000 US dollars for 680,000 yuan. He spent a year eating, drinking and having fun in China, spending 180,000 yuan. A year later he got ready to go home, so he went to the bank to change back to dollars; at that time the RMB had appreciated, and with his remaining 500,000 yuan the American got 100,000 US dollars. He came with 100,000 dollars and went back with 100,000 dollars; it was as if he had spent no money, and he went home very happy."
L4 = lesson(
    "Lesson 11 Presentation 1 skill integration: current vs fixed accounts, and the exchange-rate joke",
    "活期账户 定期账户 · 一卡通 · 网络笑话：该不该把钱换成美元",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "A. Listen to a dialog and decide whether these statements are True or False (the dialog is audio, so no key is given here). B. Compare answers with a partner and explain your reasoning in Chinese. C. Read the script your teacher provides and perform the dialog with your partner. The statements (the book prints 5000 as digits; spelled out here):",
             examples=[D(z, e) for z, e in TF1]),
        card("Activity 2 (Listening, Speaking and Reading)",
             "A. Pair up. Listen to Part 1 of a dialog and answer the questions while your partner listens to Part 2. Student A (Part 1): 1. What does the first speaker want to do? 2. What does the second speaker ask the first speaker for? 3. What does the first speaker decide to do? 4. What does the second speaker recommend? Student B (Part 2): 1. What can the customer expect in a week? 2. What can he do now? 3. How much cash can the customer withdraw today, and what bill denominations does he want? 4. What was yesterday’s exchange rate? B. Exchange the information about your dialog with your partner in Chinese. C. Check your answers against the script your teacher provides, then listen to the entire dialog again. D. In Chinese, summarize what Mark did for your partner. (Audio, not included.)"),
        card("Activity 3 (Reading and Speaking): a Chinese bank web page",
             "A. You need to deposit some money at the bank. Read the web page from a Chinese bank, then fill in the table (type of account, time requirement, minimum deposit, rules for deposit and withdrawal, interest rates). B. Compare your table with your partner’s in Chinese. C. Tell each other in Chinese how you would like to deposit your money and why. The page, with the numbers spelled out, is titled 定期帐户和活期帐户:",
             examples=[D(WEB, WEBE)]),
        card("Activity 4 (Reading): an internet joke",
             "Read the article 网络笑话：该不该把钱换成美元 (Internet joke: should you change your money into US dollars?) and answer: 1. What happened to the American in the article? 2. What made him so happy? 3. What phenomenon allowed this to occur? (The book prints the amounts as digits.) The article (the answers are mine: he came with 100,000 dollars and left with 100,000 dollars while spending 180,000 yuan; he was happy because it was as if he had spent nothing; the RMB appreciated against the dollar):",
             examples=[D(JOKE, JOKEE)]),
    ],
    exercises=[
        M("How many kinds of account can you open at a Chinese bank?", "Two: current and fixed-term", ["Three", "One", "Four"], "活期账户或定期账户."),
        M("Can you withdraw from a current account any time?", "Yes", ["No", "Only on Mondays", "Only after a year"], "随时存款或提取现金。"),
        M("What is the minimum for a current RMB deposit?", "1 yuan", ["20 yuan", "50 yuan", "100 yuan"], "人民币活期存款一元起存。"),
        M("What is the minimum for a fixed-term deposit?", "50 yuan", ["1 yuan", "20 yuan", "5,000 yuan"], "定期开户五十元起存。"),
        M("How long can a fixed term be?", "From 3 months to over 10 years", ["Only one day", "Only one year", "Always ten years"], "三个月，也可以是十年以上."),
        M("What is the rule on interest and the term?", "The longer the term, the higher the interest rate", ["The longer the term, the lower the rate", "The rate never changes", "Only current accounts earn interest"], "存款时间越长，利率就越高。"),
        M("If you withdraw the whole fixed deposit before maturity, what happens?", "The interest is computed at the current-account rate", ["You pay a fine", "You get double interest", "You get no money"], "第二种."),
        M("What is the deposit card called?", "一卡通", ["一卡行", "银联", "存折"], "存款卡叫做“一卡通”."),
        M("How much RMB did the American in the joke get for 100,000 dollars?", "680,000 yuan", ["68,000 yuan", "6,800,000 yuan", "100,000 yuan"], "十万美元兑换到六十八万元人民币。"),
        M("How much did he spend in a year?", "180,000 yuan", ["18,000 yuan", "500,000 yuan", "680,000 yuan"], "花了十八万元人民币。"),
        M("How much RMB did he have left?", "500,000 yuan", ["50,000 yuan", "180,000 yuan", "680,000 yuan"], "用剩下的五十万元人民币."),
        M("Why did he come out even?", "The RMB appreciated against the dollar", ["The RMB fell", "The bank gave him a gift", "He earned money in China"], "此时人民币升值。"),
        mean("利率", "li4 lv4", "interest rate", ["exchange rate", "deposit slip", "account"]),
        mean("升值", "sheng1 zhi2", "to appreciate (in value)", ["to exchange", "to deposit", "to withdraw"]),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context
TAB1 = [("一个月", "$1,000.00", "0.10%", "0.10%"), ("两个月", "$1,000.00", "0.10%", "0.10%"), ("三个月", "$1,000.00", "0.10%", "0.10%"), ("六个月", "$1,000.00", "0.21%", "0.21%"), ("九个月", "$1,000.00", "0.21%", "0.21%"), ("一年", "$1,000.00", "0.37%", "0.38%"), ("十八个月", "$1,000.00", "0.37%", "0.38%"), ("两年", "$1,000.00", "0.62%", "0.63%")]
TAB2 = [("六个月", "$5,000.00", "0.24%", "0.24%"), ("九个月", "$5,000.00", "0.24%", "0.24%"), ("一年", "$5,000.00", "0.40%", "0.41%"), ("十八个月", "$5,000.00", "0.40%", "0.41%"), ("两年", "$5,000.00", "0.68%", "0.69%")]
L5 = lesson(
    "Lesson 11 Presentation 1 using Chinese in context: bank rate charts and a role-play",
    "中国银行美元存款利率表 · 中国工商银行外汇存款利率 · 银行职员和客户",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking and Listening)",
             "A. Pair up. You and a friend have just arrived in China to attend the Hopkins-Nanjing Center. You both need to deposit USD in a Chinese bank and exchange USD for renminbi. Read the chart from the first bank’s website, while your partner reads the second, then share your information in Chinese. The first chart, 中国银行美元存款利率表 (effective from 3 January 2020), gives for each term the minimum balance needed to earn the annual yield, the interest rate % and the annual yield %:",
             tables=[table(["定期存款 (个人和公司)", "最低余额", "利率%", "年收益率%"], TAB1, say=[0], title="定期存款 (individuals and companies)"), table(["大额定期存款 (个人和公司)", "最低余额", "利率%", "年收益率%"], TAB2, say=[0], title="大额定期存款")]),
        card("The second chart and the follow-up",
             "The second chart is 中国工商银行外汇存款利率 (2019-11-03), 中国工商银行外汇存款参考利率, unit annual rate %, with columns 币种, 活期, 7天通知存款, 一个月, 三个月, 六个月, 一年, 二年. The book’s rows (the figures are given as printed, and some of the printed rows are shorter than the columns): 美元 0.0500, 0.2, 0.3, 0.50, 0.8000; 欧元 0.0050, 0.03, 0.05, 0.2, 0.2500; 港币 0.0100, 0.1, 0.25, 0.5, 0.7, 0.75; 日元 0.0001, 0.0005, 0.0100; 英镑 0.0500, 0.1000; 瑞士法郎 0.0001; 新加坡元 0.0001, 0.0005, 0.0100; 加拿大元 0.01, 0.0500, 0.3, 0.4, 0.4; 澳大利亚元 0.2, 0.25, 1.2, 1.300, 1.500. Source: 中国工商银行. 1. Which bank would you prefer to use and how would you like to deposit your money? B. Use online currency converters to find today’s dollar-to-yuan exchange rate, then discuss in Chinese how much you will need to change. C. Report your decisions and reasoning to the class in Chinese."),
        card("Activity 2 (Writing and Speaking): the role-play",
             "Pair up with the same partner. You will now go to the Chinese bank you chose, open an account, deposit your USD, and exchange some of it for renminbi; your partner plays the bank clerk. Study the role-play cards and plan what you will say, writing useful information or questions in pinyin or characters. The clerk: greet the customer, then ask what you can do for them; explain the various types of accounts; specify the interest rates; open an account for them; specify today’s exchange rates; exchange currency for them; ask what denominations of bills they prefer; add any additional information or ask questions that occur to you. The customer: greet the clerk, then ask how to open an account; about the various types of accounts; about interest rates; about withdrawal restrictions; how to exchange USD for renminbi; about today’s exchange rates; any additional questions."),
        card("Optional Activity 3 (Listening, Writing and Speaking)",
             "A. Watch a video on how Chinese people can open a U.S. bank account (外国人如何开银行账户？ How do foreigners open accounts?), then fill in a table in Chinese: ways to open an account, places to open an account, possible IDs, age requirements, actions not permitted. Use Pleco only when you cannot guess the meaning of key words. B. Pair up. Combine and summarize your information to write a brief set of instructions for Chinese people who want to open U.S. bank accounts. C. Read your instructions to the class. (The video is not included.)"),
    ],
    exercises=[
        M("What is 利率?", "Interest rate", ["Exchange rate", "Deposit slip", "Account"], "利率."),
        M("Which term in the first chart has the highest rate (0.62%)?", "两年", ["一个月", "六个月", "一年"], "两年 0.62%."),
        M("What is the minimum balance for the regular fixed deposits?", "$1,000", ["$5,000", "$100", "$50"], "最低余额 $1,000.00."),
        M("What is the minimum balance for the large fixed deposits?", "$5,000", ["$1,000", "$500", "$50,000"], "大额定期存款 $5,000.00."),
        M("What is 大额定期存款?", "Large-amount fixed deposit", ["A current account", "A loan", "A credit card"], "大额: large amount."),
        M("In the role-play, who explains the account types?", "The clerk", ["The customer", "Both", "Nobody"], "The clerk explains."),
        M("In the role-play, who asks about withdrawal restrictions?", "The customer", ["The clerk", "Both", "Nobody"], "The customer asks."),
        mean("银行", "yin2 hang2", "bank", ["school", "hospital", "market"]),
        mean("利息", "li4 xi1", "interest (on money)", ["exchange rate", "account", "denomination"]),
    ],
)

# ------------------------------------------------------------------ 6. vocabulary
L6 = vocab_lesson("Lesson 11 Presentation 1 vocabulary", "23 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十一课 银行 Presentation 1: opening an account and exchanging money", [L1, L2, L3, L4, L5, L6])
