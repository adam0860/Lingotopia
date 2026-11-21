"""Unit 33: Lesson 11 (Banking) Presentation 3 and Area Studies, from the book's texts: Mobile Pay, 以前, the 把 construction, 什么 (2) and 什么的,
the WeChat Pay blogs, the vocabulary list and "China's Banking System". Audio, pictures, videos and web searches are not included."""
from zh_auto import *
from zh_l11_vocab import VOC3

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the passage
MP = [
    "以前，中国人买东西通常用现金付款。今年我来中国留学，才发现大多数中国人都用移动支付，连小贩都用手机收费。所以，我马上请朋友小刚帮我注册一个电子钱包。",
    "小刚先帮我下载了一个社交软件“微信”，然后，把我的银行账户和电子钱包连在一起。这样，我就可以用手机付款了。买什么东西，用手机扫一下码就行了。而且，除了买东西，还可以用移动支付交水电费，付房租，订机票什么的，真是太方便了。",
    "现在，我已经习惯用手机支付，身上几乎不带现金了。",
]
MP_E = ["In the past, Chinese people usually paid cash when they bought things. This year I came to China to study abroad and only then discovered that most Chinese people use mobile payment; even vendors use their phones to collect fees. So I immediately asked my friend Xiaogang to help me register an e-wallet.",
        "Xiaogang first helped me download a social software called “WeChat”, and then linked my bank account and e-wallet together. This way I can pay with my phone. To buy anything, I just scan a code with my phone. Besides shopping, I can also use mobile payment to pay water and electricity bills, pay rent, book plane tickets and so on; it’s really too convenient.",
        "Now I am already used to paying by phone and hardly carry cash on me anymore."]
STRIPS = [("十年前，中国人买东西常常用现金付款。这次我来中国工作，才发现大多数中国人用手机支付，连小贩都用手机收费。所以，昨天我去银行请营业员帮我注册一个电子钱包。", "Ten years ago, Chinese people often paid cash. This time I came to China to work and discovered that most Chinese people pay by phone; even vendors use their phones to collect fees. So yesterday I went to the bank and asked the clerk to help me register an e-wallet."),
          ("营业员先帮我下载了社交软件“微信”，然后，把我的银行账户和电子钱包连在一起。这样，我就可以用微信支付付款了。买什么东西，用手机扫一下码就行了。而且，除了买东西，还可以用手机支付交水电费，付房租，订机票什么的，真是太方便了。", "The clerk first helped me download the social software “WeChat” and then linked my bank account and e-wallet. This way I can pay with WeChat Pay. To buy anything, I just scan a code with my phone. Besides shopping, I can also use phone payment to pay water and electricity bills, pay rent, book plane tickets and so on; it’s really too convenient."),
          ("现在，我在中国已经两个月了，开始习惯用手机支付，身上几乎不带现金了。", "Now I have been in China for two months already and am getting used to paying by phone; I hardly carry cash on me anymore.")]
L1 = lesson(
    "Lesson 11 Presentation 3: Mobile Pay (passage)",
    "移动支付 · 微信 · 用手机扫一下码就行了 · 身上几乎不带现金了",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. What methods of payment do Americans use? B. What are your preferred methods of payment? C. How do Chinese people make payments?"),
        card("Presentation 3: 移动支付 (Mobile Pay)",
             "The book also prints the passage in traditional characters (for example 移動支付).",
             examples=[D(z, e) for z, e in zip(MP, MP_E)]),
        card("Activities 1 and 2",
             "Activity 1 (Listening). A. Global listening: 1. What is the topic of the presentation? 2. What surprised the narrator? B. Detailed listening: 1. How did the narrator come to start using the service he mentioned? 2. What are three uses for this service? (Audio, not included. From the text: mobile payment; most Chinese people use it, even vendors; a friend helped him register an e-wallet; shopping, paying water and electricity bills, paying rent, booking plane tickets.) Activity 2 (Reading, Writing and Speaking). A. Pair up. For each verb (买, 用, 付, 带, 下载) write three different objects as quickly as you can; the pair that finishes first wins. B. Read your phrases to the class, translating any items your classmates don’t understand."),
        card("Activities 3 to 5",
             "Activity 3 (Listening, Writing and Reading). A. Listen to the passage and complete the flow chart for WeChat Pay registration in pinyin or characters. B. What else is mentioned in the passage? C. Read the script your teacher provides and make changes to the flow chart. (Audio, not included.) Activity 4 (Reading and Speaking): textual reconstruction. A. Read three sentence strips and arrange them into a logically coherent paragraph. B. In groups of three compare your paragraphs in Chinese; when all agree, compare with another group and decide the final arrangement. The correct order (mine, from the content) is Strip 1, then 2, then 3. The three strips:",
             examples=[D(z, e) for z, e in STRIPS]),
        card("Activity 5 (Speaking, Writing and Listening): Mobile Pay Survey",
             "A. Interview three different classmates about their mobile pay services, in Chinese. Fill in the table with their details in pinyin or characters (姓名, 移动支付, 支付的服务, 怎么使用). B. Exchange your interview information with a partner in Chinese."),
    ],
    exercises=[
        M("How did Chinese people usually pay in the past?", "In cash", ["By phone", "By check", "By credit card"], "以前，中国人买东西通常用现金付款。"),
        M("What surprised the narrator?", "Most Chinese people use mobile payment, even vendors", ["Chinese food", "The high prices", "Cash is everywhere"], "连小贩都用手机收费。"),
        M("Who helped the narrator register an e-wallet?", "His friend 小刚", ["A bank clerk", "His teacher", "His mother"], "请朋友小刚帮我注册一个电子钱包。"),
        M("Which social software did 小刚 download?", "微信", ["脸书", "支付宝", "苹果"], "社交软件“微信”."),
        M("What did 小刚 link together?", "The narrator’s bank account and e-wallet", ["Two phones", "Two banks", "A card and a passport"], "把我的银行账户和电子钱包连在一起。"),
        M("How do you pay when you buy something?", "Scan a code with your phone", ["Hand over cash", "Swipe a card", "Sign a receipt"], "用手机扫一下码就行了。"),
        M("Which is NOT mentioned as a use of mobile payment?", "Buying a house", ["Paying water and electricity bills", "Paying rent", "Booking plane tickets"], "水电费，房租，机票."),
        M("What does the narrator hardly carry now?", "Cash", ["A phone", "A passport", "A key"], "身上几乎不带现金了。"),
        M("What does 连小贩都用手机收费 mean?", "Even vendors use phones to collect fees", ["Vendors do not collect fees", "Only vendors use phones", "Phones collect vendors"], "连…都…: even."),
        M("What does 订机票什么的 mean?", "Book plane tickets and so on", ["Book only plane tickets", "Do not book tickets", "Ask what the tickets are"], "什么的: and so on."),
        F("以前，中国人买东西通常用现金___款。", "付", PART, "付款: pay."),
        F("用手机扫一下___就行了。", "码", PART, "扫码: scan the code."),
        F("我马上请朋友小刚帮我注册一个电子___包。", "钱", PART, "电子钱包: e-wallet."),
        F("现在，我已经习惯用手机支付，身___几乎不带现金了。", "上", PART, "身上: on one’s person."),
    ],
)

# ------------------------------------------------------------------ 2. 以前
YQ = [("以前，中国人没有移动支付，他们都用现金购物。", "In the past Chinese people had no mobile payment; they all shopped with cash."), ("以前她是服务员，现在她是老板。", "She used to be a waitress; now she is the boss."), ("我以前不认识他。", "I didn’t know him before."), ("晚上十点以前要做完作业。", "Homework has to be finished before ten at night."),
      ("上大学以前，你来过上海吗？", "Before you went to college, had you been to Shanghai?"), ("用网上银行以前，我都得去银行交电话费。", "Before using online banking, I always had to go to the bank to pay my phone bill.")]
YQ_PAT = [("以前，中国人买东西通常用现金付款。", "In the past, Chinese people usually paid for things in cash.")]
L2 = lesson(
    "Lesson 11 Presentation 3 grammar: the time word 以前",
    "以前，中国人用现金 · 我以前不认识他 · 十点以前 · 睡觉以前",
    requires=[],
    cards=[
        card("The time word 以前",
             "The adverb 以前 can be used to mean “previously” or “in the past”. As in English, 以前 can begin a sentence when it is used as a general time reference. It can also be placed right after the subject. It may also follow a time word or an action to indicate “before” that particular reference point in time, as in 十点以前 or 睡觉以前. Patterns: General time reference: 以前 + Sentence; Subject + 以前 + Verb + Object. Specific time or action: Time + 以前, …; Verb Phrase + 以前, ….",
             examples=[D(z, e) for z, e in YQ_PAT] + [D(z, e, fixes={"得": "dei3"} if "得" in z else None) for z, e in YQ]),
        card("Activities 1 to 3",
             "Activity 1 (Speaking and Listening). Form groups of three. Using the two sentence patterns 以前… or 现在… and …以前，…, take turns describing six images (not included). Activity 2 (Listening). Listen to the dialog and answer: 1. What did the woman ask about Lao Chen’s wife? 2. How has the woman changed? 3. What does Lao Chen suggest she should do? 4. Was the woman happy in the end? Why didn’t she mention the problem sooner? (Audio, not included.) Activity 3 (Speaking and Listening). A. Using 以前, interview a classmate about their life before DLI and now, and take notes in a table (Name, Life Before DLI, Life Now). B. Based on your notes, report your interview results to the class in Chinese."),
    ],
    exercises=[
        M("What does 以前 mean at the start of a sentence?", "Previously; in the past", ["Next year", "Right now", "Always"], "General time reference."),
        M("What does 以前她是服务员，现在她是老板 mean?", "She used to be a waitress; now she is the boss", ["She is a waitress and a boss", "She will be the boss", "She is not the boss"], "以前…现在…"),
        M("What does 我以前不认识他 mean?", "I didn’t know him before", ["I don’t know him now", "I will know him", "I knew him before"], "Subject + 以前 + verb."),
        M("What does 十点以前 mean?", "Before ten o’clock", ["After ten o’clock", "At ten o’clock", "Ten times"], "Time + 以前."),
        M("What does 睡觉以前 mean?", "Before going to bed", ["After going to bed", "While sleeping", "Instead of sleeping"], "Verb phrase + 以前."),
        M("What does 上大学以前，你来过上海吗？ ask?", "Before you went to college, had you been to Shanghai?", ["Have you been to college in Shanghai?", "When did you go to college?", "Where is your college?"], "Verb phrase + 以前."),
        M("What does 用网上银行以前，我都得去银行交电话费 mean?", "Before using online banking, I had to go to the bank to pay my phone bill", ["I use online banking to pay my phone bill", "I never pay phone bills", "I go to the bank after online banking"], "以前: before."),
        M("Where can 以前 (general time) be placed?", "At the start, or right after the subject", ["Only at the end", "Only before the verb", "Only after the object"], "以前 + sentence; subject + 以前 + verb."),
        F("___前，中国人没有移动支付，他们都用现金购物。", "以", PART, "以前: in the past."),
        F("晚上十点以___要做完作业。", "前", PART, "十点以前: before ten."),
        F("我以前不___识他。", "认", PART, "不认识: don’t know."),
    ],
)

# ------------------------------------------------------------------ 3. the 把 construction
BA0 = [("王小英把那些书拿去了。", "Wang Xiaoying took those books (away). (what she did to them)"), ("王小英拿去了那些书。", "Wang Xiaoying took those books. (a plain report)")]
BAX = [("我把自行车修好了。", "I fixed the bike. (resultative complement)"), ("他把你的字典给小陈了。", "He gave your dictionary to Xiao Chen. (indirect object)"), ("老王把房子卖了。", "Lao Wang sold the house. (perfective)"), ("我得把这一课复习复习。", "I have to review this lesson. (reduplicated verb)")]
BAE = [("王大年把我的书拿去了。", "Wang Danian took my book."), ("我把那个书包送给我弟弟了。", "I gave that school bag to my younger brother."), ("她把一本词典拿来了。", "She brought a dictionary."), ("请把那件衣服拿给我看看。", "Please bring that piece of clothing to me to take a look."), ("她把作业做完了。", "She finished the homework."),
       ("小刚把我的银行账户和电子钱包连在一起。", "Xiaogang linked my bank account and e-wallet together."), ("我没把礼物给他。", "I didn’t give him the gift."), ("你不把饭吃了，不能走。", "If you don’t eat up your meal, you can’t leave.")]
BA4 = [("甲：先生，请问您要买什么？", "Sir, what would you like to buy?"), ("乙：请把那个书包拿给我看看。", "Please bring that school bag to me to take a look."), ("甲：小黄，我的笔记本还在你那儿吗？", "Xiao Huang, is my notebook still with you?"), ("乙：我把你的笔记本给李红了。", "I gave your notebook to Li Hong."),
       ("甲：这是二百五十块。", "Here is 250 yuan."), ("乙：找您十四块，请您把钱拿好。", "Here is 14 yuan in change; please hold on to your money."), ("乙：当然，你得把作业交给老师。", "Of course, you have to hand in the homework to the teacher. (my line for exchange 4)")]
T1 = [("我把一个书包送给弟弟了。", "I gave a school bag to my younger brother."), ("弟弟把那本书拿走了。", "My brother took that book away."), ("老王把他的公寓卖了。", "Lao Wang sold his apartment."), ("大年把作业做完了。", "Danian finished the homework."), ("他把自行车修好了。", "He fixed the bike."), ("上课的时候，不要把手机打开。", "Don’t turn on your phone during class.")]
T2 = [("她把一本字典拿来了。", "She brought a dictionary."), ("我把一个礼物送给妈妈了。", "I gave a gift to my mother."), ("明天我得把语法复习复习。", "Tomorrow I have to review the grammar."), ("老师把作业发给我们。", "The teacher hands out the homework to us."), ("服务员，请把那个书包拿给我看看。", "Waiter, please bring me that school bag to look at."), ("小文，请把你的电话号码告诉我。", "Xiao Wen, please tell me your phone number.")]
L3 = lesson(
    "Lesson 11 Presentation 3 grammar: the 把 construction",
    "我把自行车修好了 · 请把那件衣服拿给我看看 · 我没把礼物给他",
    requires=[],
    cards=[
        card("The 把 construction",
             "The 把 construction is used to express how a direct object is disposed of, dealt with, manipulated or affected by the subject. For this reason, the verb is usually active and transitive. Compare: 王小英把那些书拿去了 tells what Wang Xiaoying did to those books (she took them, as opposed to loaning them to a friend); 王小英拿去了那些书 is simply a report of what happened (she took those books, as opposed to doing something else).",
             examples=[D(z, e) for z, e in BA0]),
        card("The verb needs an extra element",
             "The verb in a 把 construction must be followed by an extra element to complete the “disposal”: a resultative complement, an indirect object, the perfective 了, or a reduplicated verb. The object in a 把 construction often refers to something or someone known to both speakers. This can be explicitly marked with pronouns like 这, 那, 你的, etc., or inferred from context. The 把 construction places the direct object before the verbal complex (verb + other elements) and after the subject. To negate it, place the negative marker 不 or 没 before 把. Affirmative: Subject + 把 + Direct Object + Verb + Other Elements (complements, particles, reduplicated verbs, etc.). Negative: Subject + 不/没 + 把 + Direct Object + Verb + Other Elements.",
             examples=[D(z, e, fixes={"得": "dei3"} if "得" in z else None) for z, e in BAX] + [D(z, e) for z, e in BAE]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "Pair up. Complete the following exchanges with 把, then perform them for the class: 1. A: 先生，请问您要买什么？ B: ___ (拿给我看看). 2. A: 小黄，我的笔记本还在你那儿吗？ B: ___ (给李红了). 3. A: 这是二百五十块。 B: 找您十四块 ___ (拿好). 4. A: 这是二百五十块。 B: 当然，你得 ___ (交给老师). (Exchange 4 repeats exchange 3’s first line in the book, so my fourth is a free one.) My completed exchanges:",
             examples=[D(z, e, fixes={"得": "dei3"} if "得" in z else None) for z, e in BA4]),
        card("Activity 5: Game On! (SMART Board activity)",
             "Divide into teams of three. Each team member rewrites two sentences using the 把 construction. The team that finishes first reads their sentences to the class first, followed by the slower team. The team with the most correct sentences wins; if the teams tie, the faster team wins. Team 1’s sentences were 我送给弟弟一个书包, 弟弟拿走了那本书, 老王卖了他的公寓, 大年做完了作业 (the book prints 做好完了), 他修好了自行车, 上课的时候不要打开手机. My rewrites of Team 1:",
             examples=[D(z, e) for z, e in T1]),
        card("Team 2 and Activity 6",
             "Team 2’s sentences were 她拿来一本字典, 我送给妈妈一个礼物, 明天我得复习语法, 老师给我们发作业, 服务员我看看那个书包, 小文请告诉我你的电话号码. My rewrites of Team 2:",
             examples=[D(z, e, fixes={"得": "dei3"} if "得" in z else None) for z, e in T2]),
        card("Activity 6 (Speaking and Listening)",
             "Use the 把 construction to ask a partner to do something for you in the classroom (pictures of a door, a window and a book are not included); your partner responds with the appropriate action."),
    ],
    exercises=[
        M("What does the 把 construction express?", "How a direct object is dealt with by the subject", ["A question", "A comparison", "A time"], "Disposal."),
        M("Where is the direct object placed in a 把 sentence?", "After 把, before the verb", ["After the verb", "At the start", "At the end"], "Subject + 把 + object + verb."),
        M("Which element is required after the verb?", "An extra element, such as a complement or 了", ["Nothing", "A question word", "A time word"], "Complement, indirect object, 了, reduplication."),
        M("How is a 把 sentence negated?", "不 or 没 before 把", ["不 after the verb", "没 after the object", "别 at the end"], "我没把礼物给他。"),
        M("What does 我把自行车修好了 mean?", "I fixed the bike", ["I bought a bike", "I rode the bike", "The bike is mine"], "Resultative complement."),
        M("What does 他把你的字典给小陈了 mean?", "He gave your dictionary to Xiao Chen", ["He lost your dictionary", "He bought a dictionary", "Xiao Chen gave him a dictionary"], "把…给…了."),
        M("What does 我得把这一课复习复习 mean?", "I have to review this lesson", ["I reviewed this lesson", "I will not review", "This lesson is easy"], "Reduplicated verb."),
        M("What does 请把那件衣服拿给我看看 mean?", "Please bring that piece of clothing to me to look at", ["Please wear that clothing", "Please buy that clothing", "Please wash that clothing"], "请把…拿给我看看."),
        M("What does 你不把饭吃了，不能走 mean?", "If you don’t eat up your meal, you can’t leave", ["You may leave after the meal", "Don’t eat", "Eat later"], "把饭吃了."),
        M("Which sentence is correct?", "她把作业做完了。", ["她做完把作业了。", "她把做完作业了。", "把她作业做完了。"], "把 + object + verb + complement."),
        M("Which sentence is a correct negative?", "我没把礼物给他。", ["我把没礼物给他。", "我把礼物没给他。", "没我把礼物给他。"], "没 before 把."),
        F("我___自行车修好了。", "把", PART, "把 + object."),
        F("请把那件衣服拿___我看看。", "给", PART, "拿给我看看."),
        F("我___把礼物给他。", "没", PART, "没 before 把."),
        F("她把作业做___了。", "完", PART, "做完: finish."),
    ],
)

# ------------------------------------------------------------------ 4. 什么 (2), 什么的
SM = [("买什么东西，用手机扫一下码就行了。", "When you buy something, you can just use your cellphone to scan the code."), ("我们什么果汁都喝。", "We drink any kind of fruit juice.")]
SM2 = [("妈妈做什么菜都好吃。", "Whatever dish Mom makes is delicious."), ("网上银行什么服务都有。", "Online banking has every kind of service."), ("她男朋友什么运动都喜欢。", "Her boyfriend likes every kind of sport."), ("在中国，你买什么东西都可以用移动支付。", "In China, you can use mobile payment to buy anything."), ("今天我不舒服，什么东西都没吃。", "I’m not feeling well today and haven’t eaten anything."), ("你在家里怎么什么事都不做？", "Why don’t you do anything at all at home?")]
SDE = [("除了买东西，还可以用移动支付交水电费，付房租，订机票什么的。", "Besides shopping, you can also use mobile payment to pay water and electricity bills, pay the rent, book plane tickets, and so on."), ("我奶奶不吃肉，只吃蔬菜、豆腐、水果什么的。", "My grandmother doesn’t eat meat; she only eats vegetables, tofu, fruit and so on."), ("在中国银行换外汇很容易，你可以兑换美元、欧元、澳元、英镑什么的。", "It’s easy to change foreign currency at the Bank of China; you can exchange US dollars, euros, Australian dollars, pounds and so on."),
       ("网上银行又快又方便，你可以转账、汇款、付账单什么的。", "Online banking is fast and convenient; you can transfer, remit, pay bills and so on."), ("跑步、游泳、爬山什么的，这些运动他都喜欢。", "Running, swimming, hiking and so on: he likes all these sports.")]
L4 = lesson(
    "Lesson 11 Presentation 3 grammar: 什么 (2) meaning “any”, and 什么的",
    "什么东西都… · 什么服务都有 · 什么都没吃 · 订机票什么的",
    requires=[],
    cards=[
        card("什么 (2): “any”, “every”",
             "什么 usually means “what”, as in 这是什么? or 你喝什么? Coming before a noun, however, it can also mean “something”, “anything” or “everything”, and is often used together with 都 or 也. Affirmative: 什么 + Noun + 都 + Verb. Negative: 什么 + Noun + 都/也 + 不 + Verb; 什么 + Noun + 都/也 + 没(有) + Verb.",
             examples=[D(z, e) for z, e in SM] + [D(z, e) for z, e in SM2]),
        card("什么的: “and so on”",
             "什么 and 的 can be combined to form 什么的, meaning “and so on” or “etcetera”. As in English, it is used to end a list of similar items. Nouns, noun phrases and verb phrases can all be followed by 什么的. Patterns: Noun 1 + Noun 2 + (Noun 3…) + 什么的; Verb Phrase 1 + Verb Phrase 2 + (Verb Phrase 3…) + 什么的.",
             examples=[D(z, e) for z, e in SDE]),
        card("Activities 7 and 8",
             "Activity 7 (Listening and Speaking). A. Pair up. Each partner listens to two of four passages and fills in the information about the places or people mentioned. B. In Chinese, exchange information with your partner to complete the table. C. Report your information to the class in Chinese. (Audio, not included.) Activity 8 (Writing, Speaking, Listening and Reading). Form groups of three. You are tasked to write a DLI brochure for Chinese visitors. A. Each group member chooses two topics from the list (国防语言学院: 学生宿舍, 食堂, 体育馆, 图书馆, 老师, 学生) and, using 什么…都… and 什么的, writes a short paragraph of six to eight sentences about them, then reads it to the group. B. As a group, organize all the sentences and paragraphs on paper or in a PowerPoint document to make your brochure. C. Present your group brochure to the class."),
    ],
    exercises=[
        M("What does 什么 mean before a noun with 都?", "Any; every", ["What", "Why", "When"], "什么 + noun + 都."),
        M("What does 我们什么果汁都喝 mean?", "We drink any kind of fruit juice", ["We don’t drink juice", "What juice do we drink?", "We drink one juice"], "什么 + noun + 都."),
        M("What does 妈妈做什么菜都好吃 mean?", "Whatever dish Mom makes is delicious", ["Mom makes no dishes", "Which dish is delicious?", "Mom only makes one dish"], "什么菜都好吃."),
        M("What does 今天我不舒服，什么东西都没吃 mean?", "I’m unwell and haven’t eaten anything today", ["I ate everything", "What did I eat?", "I ate one thing"], "什么 + noun + 都 + 没."),
        M("What does 网上银行什么服务都有 mean?", "Online banking has every kind of service", ["Online banking has no services", "Which services are there?", "Only one service"], "什么服务都有."),
        M("What does 什么的 mean at the end of a list?", "And so on", ["What for?", "What is it?", "Or not"], "订机票什么的."),
        M("Which can be followed by 什么的?", "Nouns, noun phrases and verb phrases", ["Only nouns", "Only verbs", "Only numbers"], "All three."),
        M("What does 跑步、游泳、爬山什么的，这些运动他都喜欢 mean?", "Running, swimming, hiking and so on: he likes all of these", ["He dislikes them", "He likes only running", "What sports does he like?"], "什么的."),
        F("买___么东西，用手机扫一下码就行了。", "什", PART, "什么东西: anything."),
        F("她男朋友什么运动___喜欢。", "都", PART, "什么 + noun + 都."),
        F("你可以转账、汇款、付账单什么___。", "的", PART, "什么的."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
TF = [("杰克的新手机很便宜，而且很好看。", "Jack’s new phone is cheap and good-looking."), ("现在中国人最喜欢用的社交软件是脸书。", "The social software Chinese people like to use most now is Facebook."), ("杰克还不知道怎么用移动支付。", "Jack doesn’t yet know how to use mobile payment."), ("杰克觉得他有信用卡，所以不需要电子钱包。", "Jack thinks that since he has a credit card he doesn’t need an e-wallet."), ("有电子钱包就可以用手机支付了。", "With an e-wallet you can pay by phone.")]
A2K = [("我先帮你下载微信，帮你注册电子钱包，然后你把银行卡连在一起。", "First I’ll help you download WeChat and register an e-wallet, then you link your bank card to it."), ("你今天回去以后，就打开微信，然后点击钱包，将你的银行卡绑定。这样，你就可以用微信支付了。", "When you get back today, open WeChat, then tap Wallet and bind your bank card. This way you can use WeChat Pay.")]
B1 = "上次在北京吃早点，因为十块钱纸币难倒了老板，六块钱的早点只付了五块，有点儿《百万英镑》那种“有钱人”的感觉。这次再去，发现拿着手机等着付款的人很多。过去还有老年人拿现金支付。现在老年人都是手机支付了，连街头小商小贩都是手机收费。大多数外国朋友到中国以前都没有微信钱包。没有微信钱包在中国当然什么都干不了。那么怎么办呢？这非常简单。你先在手机上“下载”微信，然后请中国朋友给你发一个几块钱人民币的红包。你点开红包的时候，微信就会给你开通微信钱包。有了微信钱包，你还需要把微信钱包和你的银行卡连在一起，就是中国人说的“绑定”。如果你有中国的银行卡，可以先打开微信，然后点击钱包，选和银行卡绑定，输入银行卡号、姓名、身份证号码和手机号进行绑定，就这么简单。但是，你的手机号最好是中国国内的手机号。微信支付注册完成以后，你什么都可以扫码支付，吃早点、购物、打车、订餐什么的。"
B1E = "Last time I had breakfast in Beijing, a 10-yuan note stumped the owner and I paid only 5 yuan for a 6-yuan breakfast, which felt a bit like being the “rich man” in “The Million Pound Note”. This time I went again and found that many people were waiting with phones in hand to pay. In the past some elderly people still paid with cash; now the elderly all pay by phone, and even street vendors collect fees by phone. Most foreign friends have no WeChat wallet before they come to China, and without one you of course can’t do anything in China. So what to do? It’s very simple. First download WeChat on your phone, then ask a Chinese friend to send you a red packet of a few yuan. When you tap open the red packet, WeChat will activate a WeChat wallet for you. With the wallet, you also need to link it to your bank card, what Chinese people call “binding”. If you have a Chinese bank card, first open WeChat, tap Wallet, choose to bind a bank card, and enter the card number, name, ID number and phone number; it’s that simple. But your phone number had better be a Chinese domestic one. After registering WeChat Pay, you can scan to pay for everything: breakfast, shopping, taxis, ordering meals and so on."
B2 = "听说现在微信支付可以绑定国外信用卡了，也就是说你可以把你的美国信用卡和微信钱包连在一起。操作非常简单。当然，你需要先用手机下载微信。在微信上，点击钱包，然后点击银行卡。国外手机直接输入信用卡卡号和个人信息就可以。电话号码就是你国外的手机号。然后设定微信支付密码就可以了。当收到红包，接受一下就把钱放入钱包了。支付的时候，在微信中扫描一下商家的二维码，支付就完成了！在微信中，还有一个“收钱”功能。选择“收钱”，就会看到一个二维码，付钱的人扫描一下钱就进来了。选择“支付”，同样出现二维码，对方扫描一下钱就走了。在中国要看清楚二维码，比如共享自行车，车上有二维码，一扫就打开了。但是，现在有人把自己的二维码放在自行车上，你一扫，钱就给他了！在中国你不仅可以用微信支付订机票，付手机费、水电费、付房租、订餐、订酒店，而且还可以用微信支付买房、卖房什么的。"
B2E = "I hear that WeChat Pay can now bind foreign credit cards, which means you can link your American credit card to your WeChat wallet. The operation is very simple. Of course you first need to download WeChat on your phone. In WeChat tap Wallet, then tap Bank Cards. With a foreign phone, just enter the credit card number and personal information; the phone number is your foreign mobile number. Then set a WeChat Pay password. When you receive a red packet, accept it and the money goes into your wallet. To pay, scan the merchant’s QR code in WeChat and the payment is done! WeChat also has a “Collect money” function: choose it and you will see a QR code, and when the payer scans it the money comes in. Choose “Pay” and a QR code also appears; when the other side scans it, the money goes away. In China you must look carefully at QR codes: for example, shared bikes have a QR code on them that opens with one scan; but now some people stick their own QR code on bikes, and when you scan it, your money goes to them! In China you can use WeChat Pay not only to book plane tickets and pay phone bills, water and electricity bills, rent, order food and book hotels, but also to buy and sell houses and so on."
CHAIN = [("文文：见面啊？我也想啊，可是我现在还在德国留学呢。听说现在国内有一个关于支付的说法是不是真的啊？就是这个：支付鄙视链", "Wenwen: Meet up? I’d like to, but I’m still studying in Germany. I hear there is a saying about payment in China now; is it true? It’s this one: the payment “contempt chain”.")]
L5 = lesson(
    "Lesson 11 Presentation 3 skill integration: WeChat Pay, two blogs and the payment “contempt chain”",
    "绑定 · 红包 · 二维码 · 外国人在中国 · 支付鄙视链",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading and Speaking)",
             "A. Listen to the dialog and mark the statements true or false (audio, so no key is given here). Check your answers with a partner and explain your reasoning in Chinese. B. Listen again and answer: 1. What does the first speaker want to know? 2. What conveniences does the second speaker mention? 3. What does the second speaker consider unusual? 4. What is the societal phenomenon mentioned at the end of the dialog? The statements:",
             examples=[D(z, e) for z, e in TF]),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the dialog and select the correct images: 1. Where does this conversation take place (a farmers’ market, a bank or a restaurant)? 2. What options does the first speaker have (WeChat Pay, PayPal, Alipay, Apple Pay)? B. Listen again and complete the sentences with the information the second speaker relates, then translate: 1. 我先 ___ 帮你 ___，帮你 ___，然后你 ___。 2. 你今天回去以后，就 ___，然后 ___，将你的 ___。这样，你就可以 ___ 了。 C. Check your work with a partner. D. Read the script and perform the dialog. E. In Chinese, discuss what you might experience in China based on this conversation. The blanks cannot be recovered without the audio; my completion of both sentences:",
             examples=[D(z, e) for z, e in A2K]),
        card("Activity 3 (Reading, Writing, Speaking and Listening): two blog posts",
             "A. Pair up. Read the first blog post while your partner reads the second. Write a summary of your post in Chinese, then read it to your partner. B. Compare the blog posts by filling in a table (Topic, Help Provided, Instructions, New Trends, Uses for New Tools). C. Report your findings to the class in Chinese, including what most surprised you about WeChat Pay. Blog 1 is by 董倩, 外国人在中国 (the first post is dated 20 January 2020); the book prints the figures as digits.",
             examples=[D(B1, B1E)]),
        card("Blog 2",
             "Blog 2 is by 黄翔, 外国人在中国 (dated 18 February 2020):",
             examples=[D(B2, B2E)]),
        card("Optional Activity 4 (Reading, Speaking and Listening)",
             "A. Pair up and read the following WeChat message. In Chinese, discuss which payment method is likely to be used the most, and the least, by Chinese people in the future. B. Tell the class in Chinese where you are presently on that chain, based on the payment method you are currently most comfortable using. The “payment contempt chain” (支付鄙视链), from lowest to highest: 现金支付 < 银行卡支付 < 信用卡支付 < 手机微信支付/支付宝扫码支付 < 用除了支付宝以外的应用扫码支付 < 指纹支付 < 刷脸支付 (cash, bank card, credit card, WeChat Pay or Alipay scan, scanning with an app other than Alipay, fingerprint, face payment).",
             examples=[D(z, e) for z, e in CHAIN]),
    ],
    exercises=[
        M("What is 红包 used for in Blog 1?", "A friend sends a few yuan to activate your WeChat wallet", ["To pay for breakfast", "To buy a house", "To pay the bank"], "请中国朋友给你发一个几块钱人民币的红包。"),
        M("What does “绑定” mean in the blog?", "To link a WeChat wallet to a bank card", ["To buy a phone", "To close an account", "To scan a code"], "把微信钱包和银行卡连在一起，就是“绑定”。"),
        M("What does Blog 1 say is best about the phone number?", "It should be a Chinese domestic number", ["It should be a foreign number", "It should be a landline", "Any number will do"], "你的手机号最好是中国国内的手机号。"),
        M("What can you pay with WeChat Pay after registering, per Blog 1?", "Breakfast, shopping, taxis and meals", ["Only breakfast", "Only taxis", "Nothing"], "吃早点、购物、打车、订餐什么的."),
        M("What new feature does Blog 2 mention?", "WeChat Pay can bind foreign credit cards", ["WeChat Pay is free", "WeChat Pay needs a Chinese ID", "WeChat Pay has no password"], "微信支付可以绑定国外信用卡了。"),
        M("What does the “收钱” function show?", "A QR code the payer scans", ["A password", "A bill", "A map"], "就会看到一个二维码."),
        M("What warning does Blog 2 give?", "Some people stick their own QR codes on shared bikes", ["Bikes are unsafe", "Phones can’t scan codes", "Cash is required"], "有人把自己的二维码放在自行车上."),
        M("What does Blog 2 say you can also do with WeChat Pay?", "Buy and sell houses", ["Climb a mountain", "Study abroad", "Open a school"], "买房、卖房什么的."),
        M("Which payment method is at the top of the “contempt chain”?", "刷脸支付", ["现金支付", "信用卡支付", "指纹支付"], "…＜ 指纹支付 ＜ 刷脸支付."),
        M("Which payment method is at the bottom of the chain?", "现金支付", ["刷脸支付", "银行卡支付", "指纹支付"], "现金支付 is first (lowest)."),
        mean("红包", "hong2 bao1", "red packet (gift money)", ["cash", "credit card", "bank"]),
        mean("二维码", "er4 wei2 ma3", "QR code", ["password", "bank card", "passbook"]),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese in context
CASH = [("上午", "", "", ""), ("中午", "", "", ""), ("下午", "", "", ""), ("晚上", "", "", "")]
L6 = lesson(
    "Lesson 11 Presentation 3 using Chinese in context: the cashless life, WeChat Pay in the U.S.",
    "体验中国无现金生活 · 在北京无现金生活的一天 · 在美国怎么用微信",
    requires=[],
    cards=[
        card("Activity 1 (Writing, Reading, Listening and Speaking): 体验中国无现金生活",
             "Experience the cashless life in China. Pair up. You and a classmate have been studying at Beijing Normal University for a semester; some American friends are coming to visit and you want to show them how to use WeChat Pay. A. Go online to find out how Americans use WeChat Pay on U.S. cellphones; before writing instructions for your friends, first write a Chinese version so your teacher can check the accuracy. B. You come across a video featuring an Australian expat and his American friend using WeChat Pay in Hangzhou, 两老外在杭州体验无现金生存 结果爽呆了! Watch the video and take notes in a table (在哪儿, 活动, 用微信支付做什么). C. Plan a WeChat Pay itinerary for your friends using the table 在北京无现金生活的一天 (时间: 上午, 中午, 下午, 晚上; 去哪儿; 活动; 用微信支付做什么). D. Read your instructions and itinerary to the class in Chinese. (The video is not included.)",
             examples=[D("两老外在杭州体验无现金生存，结果爽呆了！", "Two foreigners experience cashless living in Hangzhou, and are blown away!"), D("在北京无现金生活的一天", "A cashless day in Beijing")]),
        card("Activity 2 (Reading, Writing, Speaking and Listening)",
             "Pair up. Your homestay family in Hangzhou is planning their first trip to the U.S. They want to know how and where they can use WeChat Pay there. A. Research Chinese tourist websites on the use of WeChat Pay in the U.S.; write down keywords and other essential information, then share it with your Chinese friend (your partner). B. Based on your research, write a list of instructions for using WeChat Pay in the U.S. (在美国怎么用微信; 在哪儿可以用微信). C. List the family’s options when they cannot use WeChat Pay (在美国可以用的支付; 怎么做) and explain how to use these other payment methods. D. Post your two sets of instructions on Linoit.com, then read your instructions to the class.",
             examples=[D("在美国怎么用微信", "How to use WeChat in the U.S."), D("在哪儿可以用微信", "Where you can use WeChat")]),
    ],
    exercises=[
        M("Where have you been studying in Activity 1?", "Beijing Normal University", ["Fudan University", "Qinghua University", "Taiwan Normal University"], "Beijing Normal University for a semester."),
        M("Who is coming to visit?", "American friends", ["A Chinese teacher", "A homestay family", "A bank manager"], "Some American friends are coming to visit."),
        M("What does 无现金 mean?", "Cashless", ["Very cheap", "Cash only", "Free"], "无现金生活: cashless life."),
        M("Where does the homestay family live?", "Hangzhou", ["Beijing", "Shanghai", "Taipei"], "Your homestay family in Hangzhou."),
        M("Where is the family planning to go?", "The U.S.", ["Japan", "Germany", "Australia"], "First trip to the U.S."),
        mean("无现金", "wu2 xian4 jin1", "cashless", ["very cheap", "cash only", "free"]),
    ],
)

L7 = vocab_lesson("Lesson 11 Presentation 3 vocabulary", "20 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 8. Area Studies
BANKS = [("中国银行", "Bank of China (BoC)"), ("中国工商银行", "Industrial and Commercial Bank of China (ICBC)"), ("中国建设银行", "China Construction Bank (CCB)"), ("交通银行", "Bank of Communications (BoCom)"), ("中国农业银行", "Agricultural Bank of China (ABC)"), ("中国人民银行", "People’s Bank of China (PBoC), the central bank")]
OLD = [("票号", "piaohao: a traditional financial institution"), ("钱庄", "qianzhuang: a traditional financial institution"), ("中国通商银行", "Imperial Bank of China"), ("大清户部银行", "Great Qing Bank of the Board of Revenue"), ("大清银行", "Great Qing Government Bank"), ("辛亥革命", "the Xinhai Revolution"), ("京汉铁路", "Beijing-Hankou Railway"), ("盛宣怀", "Sheng Xuanhuai")]
L8 = lesson(
    "Lesson 11 Area Studies: China’s banking system",
    "票号 钱庄 · 中国人民银行 · 四大银行 · 中国银行 中国工商银行 中国建设银行",
    requires=[],
    cards=[
        card("China’s banking system (1): the history",
             "China has a long history of banking. As early as the Song Dynasty (960-1279), Chinese financial institutions conducted all major banking functions, including deposits, loans, issuance of notes, currency exchange, and long-distance remittance. In 1024, the first paper currency was issued by the state in Sichuan. The two major types of indigenous financial institutions, piàohào (票号) and qiánzhuāng (钱庄), cooperated more than competed in financial markets. In 1897, China’s first modern public bank, the Imperial Bank of China (中国通商银行), opened for business, while financier Sheng Xuanhuai (盛宣怀) founded the first private bank. In 1905, China’s first central bank was established as the Great Qing Bank of the Board of Revenue (大清户部银行); it was renamed the Great Qing Government Bank (大清银行) three years later. Following the Xinhai Revolution (辛亥革命) in 1911, the Daqing Bank was finally renamed the Bank of China (中国银行). Another government bank, the Bank of Communications (交通银行), was set up in 1908 by the Ministry of Posts and Communications to raise money to buy the Beijing-Hankou Railway (京汉铁路) from Belgian contractors.",
             tables=[wtable(rows_py(OLD), title="Names in the history")]),
        card("The People’s Republic and the big five",
             "With the founding of the People’s Republic of China in 1949, the People’s Bank of China (PBoC 中国人民银行) was established as the central bank. PBoC issues currency, monitors the money supply, regulates China’s financial institutions, and formulates monetary policy for the State Council. In the early 1980s, the government opened up the banking system and allowed five state-owned specialized banks to accept deposits and conduct business: 1) the Bank of China (BoC 中国银行); 2) the Industrial & Commercial Bank of China (ICBC 中国工商银行); 3) the China Construction Bank (CCB 中国建设银行); 4) the Bank of Communications (BoCom 交通银行); and 5) the Agricultural Bank of China (ABC 中国农业银行). (The book’s photographs are not included.)",
             tables=[wtable(rows_py(BANKS), title="The central bank and the five state-owned banks")]),
        card("Roles and today’s banking sector",
             "The Bank of China manages foreign exchange transactions and reserves. The China Construction Bank lends state budget funds for capital construction projects. The Industrial and Commercial Bank of China raises both domestic and international funds to bolster the economy, manage credit, and promote industrial production and commercial circulation. And the Agricultural Bank of China lends to and invests deposits from the agricultural sector. Today, China’s banking sector is the largest in the world by assets, which totaled U.S. $40.1 trillion in the first quarter of 2019. As of April 2020, four Chinese banks topped the list of world banks ranked by total assets. According to Zhihu (知乎), there were 4,597 banks and financial institutions across the nation in 2020. Together, they play a vital role in the Chinese economy. China’s financial reform and development in the last 40 years has enabled both financial stability and tremendous economic growth. In recent years, however, the financial system has suffered declines in efficiency along with a rise in financial risk. Still dominated by state banks and pervasive government intervention, China increasingly needs to build a more open, market-oriented system to meet new economic needs and challenges at home and abroad."),
    ],
    exercises=[
        M("When did Chinese financial institutions already conduct all major banking functions?", "As early as the Song Dynasty", ["In the Qing Dynasty only", "After 1949", "In the 1980s"], "Song Dynasty (960-1279)."),
        M("When and where was the first paper currency issued by the state?", "1024, in Sichuan", ["1897, in Shanghai", "1949, in Beijing", "1905, in Tianjin"], "In 1024... in Sichuan."),
        M("Which are the two indigenous financial institution types?", "票号 and 钱庄", ["中国银行 and 交通银行", "微信 and 支付宝", "票号 and 邮局"], "票号 and 钱庄."),
        M("What was China’s first modern public bank?", "中国通商银行", ["中国银行", "交通银行", "中国人民银行"], "Imperial Bank of China, 1897."),
        M("What was the Daqing Bank finally renamed after 1911?", "中国银行", ["中国人民银行", "交通银行", "中国农业银行"], "Bank of China."),
        M("Which bank was set up in 1908 to buy the Beijing-Hankou Railway?", "交通银行", ["中国银行", "中国工商银行", "中国农业银行"], "Bank of Communications."),
        M("What is China’s central bank?", "中国人民银行", ["中国银行", "中国工商银行", "中国建设银行"], "PBoC, founded 1949."),
        M("What does PBoC do?", "Issues currency, monitors the money supply, regulates institutions and formulates monetary policy", ["Lends only to farmers", "Manages only foreign exchange", "Sells insurance"], "Central bank functions."),
        M("Which bank manages foreign exchange transactions and reserves?", "中国银行", ["中国农业银行", "中国建设银行", "交通银行"], "Bank of China."),
        M("Which bank lends to and invests deposits from the agricultural sector?", "中国农业银行", ["中国银行", "中国建设银行", "中国工商银行"], "Agricultural Bank of China."),
        M("What does the China Construction Bank lend?", "State budget funds for capital construction projects", ["Only to farmers", "Foreign currency", "Personal loans only"], "Capital construction."),
        M("How large was China’s banking sector in the first quarter of 2019?", "The largest in the world, U.S. $40.1 trillion in assets", ["Second after the US, $4.1 trillion", "Smallest in Asia", "$401 billion"], "Largest in the world by assets."),
        mean("中国人民银行", "zhong1 guo2 ren2 min2 yin2 hang2", "People’s Bank of China (central bank)", ["Bank of China", "Agricultural Bank of China", "Bank of Communications"]),
        mean("交通银行", "jiao1 tong1 yin2 hang2", "Bank of Communications", ["Bank of China", "People’s Bank of China", "China Construction Bank"]),
        mean("中国农业银行", "zhong1 guo2 nong2 ye4 yin2 hang2", "Agricultural Bank of China", ["Bank of China", "People’s Bank of China", "China Construction Bank"]),
    ],
)

UNIT = unit("第十一课 银行 Presentation 3: Mobile Pay, and Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8])
