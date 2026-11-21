"""Unit 36: Lesson 13 (At the Airport) Presentation 1 from the book's texts: the check-in dialog, the 的 phrase as a noun, the
preposition 往, the resultative complements 好 and 完, the simple directional verbs, the skill-integration and using-Chinese
activities and the vocabulary list. Audio, pictures, maps and websites are not included; answer keys the book does not print are mine.
Seat letters are written in full-width form (Ａ, Ｅ) so that every spoken line is Chinese only."""
from zh_auto import *
from zh_l13_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1"}
    if "重庆" in zh:
        f["重"] = "chong2"
    if any(k in zh for k in ("得上", "得坐", "得先")):
        f["得"] = "dei3"
    if "还给她的上司" in zh:
        f["还"] = "hai2"
    i = zh.find("行李")
    while i >= 0:
        f[i + 1] = "li5"          # 行李 xíngli, not the surname Lǐ
        i = zh.find("行李", i + 2)
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D   # dlg() builds its lines with zh_auto.D, so it picks up the fixes above


PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the check-in dialog
P1 = [("服务员", "您好！您要办登机手续吗？", "Hello! Do you want to go through check-in?"),
      ("大卫", "登机手续我已经办好了，可是，我想换一下座位。", "I’ve already completed check-in, but I’d like to change my seat."),
      ("服务员", "请先让我看一下您的护照和登机牌。", "Please let me see your passport and boarding pass first."),
      ("大卫", "在这儿，给您。", "Here you are."),
      ("服务员", "您要换什么座位？", "What seat do you want to change to?"),
      ("大卫", "我订的是靠走道的座位，我想换成靠窗户的。", "I booked an aisle seat; I’d like to change to a window seat."),
      ("服务员", "请稍等，让我查一下。十五排Ａ座可以吗？", "Please wait a moment, let me check. Is seat A in row 15 all right?"),
      ("大卫", "可以。", "Yes."),
      ("服务员", "您要托运行李吗？", "Are you checking any luggage?"),
      ("大卫", "这件大的托运，小的我随身带。", "I’ll check this big one and carry the small one on."),
      ("服务员", "请您把行李放这儿称一下。好了。这是您的行李牌。请到那边过安检。", "Please put your luggage here to be weighed. All done. Here is your luggage tag. Please go over there through security."),
      ("大卫", "请问，十九号登机口怎么走？", "Excuse me, how do I get to Gate 19?"),
      ("服务员", "过了安检，往左拐，坐电梯上二楼，出了电梯往前走，右边第三个登机口就是。", "After security, turn left, take the elevator up to the second floor, and after getting out of the elevator walk straight ahead; it’s the third boarding gate on the right."),
      ("大卫", "谢谢！", "Thank you!")]
A2 = ("我已经办好登机手续了。我对服务员说，我想换一下座位。我的座位是靠走道的，我想换成靠窗户的。服务员看了我的护照和登机牌。换完座位以后，我还要托运行李。我有两件行李，大的托运，小的我随身带。服务员把行李牌给我，让我去过安检，他还告诉我怎么去十九号登机口。",
      "I have already completed check-in. I told the agent I’d like to change my seat. My seat is an aisle one and I want to change to a window one. The agent looked at my passport and boarding pass. After changing seats I still have to check my luggage. I have two pieces of luggage; I check the big one and carry the small one on. The agent gave me the luggage tag, told me to go through security, and also told me how to get to Gate 19.")
A2K = [("登机手续", "我已经办好___了"), ("换一下座位", "我想___"), ("靠走道的", "我的座位是___"), ("靠窗户的", "我想换成___"), ("登机牌", "护照和___"), ("托运行李", "我还要___"), ("件", "我有两___行李"), ("托运", "大的___"), ("我随身带", "小的___"), ("行李牌", "服务员把___给我"), ("过安检", "让我去___"), ("十九号登机口", "他还告诉我怎么去___")]
A3 = [("请让我看一下您的机票。", "Can I see your ticket, please?"), ("您带护照了吗？", "Do you have your passport with you?"), ("您要托运几件行李？", "How many pieces of luggage are you checking in?"), ("您有随身带的行李吗？", "Do you have any carry-on bags?"), ("请您把行李放在这儿。", "Would you place your bag on the counter?"),
      ("您想要靠走道的座位还是靠窗户的座位？", "Would you like an aisle or window seat?"), ("靠走道的座位没有了，靠窗户的可以吗？", "We do not have any aisle seats remaining. Is a window seat OK with you?"), ("这是您的登机牌。", "Here is your boarding pass."), ("您在八号登机口上飞机。", "You will board at Gate 8.")]
A5 = [("服务员", "下午好！请问您的飞机到哪里？", "Good afternoon! Where is your flight going?"), ("大卫", "到香港。", "To Hong Kong."), ("服务员", "请让我看一下您的护照。", "Please let me see your passport."), ("大卫", "这是我的护照。", "Here is my passport."),
      ("服务员", "您有需要托运的行李吗？", "Do you have luggage to check?"), ("大卫", "就这一件。", "Just this one piece."), ("服务员", "请把行李箱放在这里称一下。", "Please put the suitcase here to be weighed."), ("大卫", "我在北京转机，我需要在北京取行李吗？", "I’m transferring in Beijing; do I need to pick up my luggage in Beijing?"),
      ("服务员", "不，您只需要在香港取行李。这是您的登机牌。您的座位号是二十六Ｅ。请到十五号登机口上飞机。", "No, you only need to pick up your luggage in Hong Kong. Here is your boarding pass. Your seat number is 26E. Please go to Gate 15 to board.")]
L1 = lesson(
    "Lesson 13 Presentation 1: check-in at the airport",
    "第十三课 人在机场 · 我想换一下座位 · 大的托运，小的我随身带 · 十九号登机口怎么走？",
    requires=[],
    cards=[
        card("第十三课 人在机场: Lesson 13 At the Airport, learning objectives",
             "Upon completion of this lesson you will be able to check in at the airport, process customs entry, go through a security check, and give simple directions. To do this you must master new words and phrases for these functions, formulaic expressions for functioning at the airport, and the grammar: the 的 phrase as a noun, the directional 往, the resultative complements 好 and 完, the simple directional verbs, the measure word for verbs 次, the 到 + place + verb construction, simple directional verbs used to indicate the direction of an action, 因此 (therefore) versus 所以, …的样子, 原来 (as it turned out), and the conditional 要是…就…."),
        card("Getting Started",
             "Pair up and discuss: A. When was the last time you took a flight? B. What identification did you need to board? C. How many pieces of luggage did you have? D. What kind of seat do you prefer on the airplane? E. List the stages of a plane journey from check-in to arrival."),
        card("Presentation 1: at the check-in desk",
             "David talks to the check-in agent (the book also prints the dialog in traditional characters). The seat letter is written in full-width form here so that the Chinese is spoken without Latin letters.",
             examples=dlg(P1)),
        card("Activities 1 and 2",
             "Activity 1 (Listening). A. Global listening: where did the conversation take place, and what tasks did the passenger accomplish? B. Detailed listening: 1. What documents was the passenger asked for? 2. What accommodation did he request, and was it satisfied? 3. How many pieces of check-in and carry-on luggage did he have? 4. What was his next stop? 5. What was his last question at the counter? (Audio, not included. From the dialog: passport and boarding pass; he asked for a window seat instead of an aisle seat and got seat A in row 15; one big piece to check and a small one to carry on; security; how to get to Gate 19.) Activity 2 (Reading and Writing). A. Using the presentation, fill in the blanks in the paragraph with pinyin or characters (the book’s blanks are empty; the completed paragraph below is mine). B. Pair up, read your passage to your partner and discuss your work.",
             examples=[D(*A2)],
             tables=[table(["Blank", "Fits into"], [(a, b) for a, b in A2K], title="The words for the blanks", say=[0])]),
        card("Activity 3 (Speaking): at the check-in desk",
             "Below are requests, instructions or questions a passenger may hear at the check-in desk. Pair up: one student plays the check-in agent, the other the passenger; switch roles after the first round. The book gives them in English in four groups: 1. First the agent asks for your ticket and ID. 2. Then the agent takes your luggage. 3. They might ask your seat preference. 4. The clerk tells you your gate number and boarding time. A Chinese version of each (mine):",
             examples=[D(z, e) for z, e in A3]),
        card("Activities 4 and 5",
             "Activity 4 (Listening). Listen to the passage and answer: 1. What kind of seat does the passenger prefer? 2. How many pieces of luggage will he check in, and which bags can he carry on the plane? (Audio, not included.) Activity 5 (Reading). Read the conversation between David and the check-in agent and answer the questions. New word: 转机 (zhuǎnjī): transfer. 1. What is David’s destination? 2. How many pieces of luggage did he check in? 3. Where should he claim his checked-in luggage? 4. Why is his flight stopping at Beijing? (Mine: Hong Kong; one; in Hong Kong; because he is transferring there.) The seat is written in the book as 26E.",
             examples=[D(f"{s}：{z}", e) for s, z, e in A5]),
    ],
    exercises=[
        M("What does the passenger want to change?", "His seat", ["His flight", "His passport", "His luggage tag"], "我想换一下座位。"),
        M("What seat did David book originally?", "An aisle seat", ["A window seat", "A middle seat", "A first-class seat"], "我订的是靠走道的座位。"),
        M("What seat does he want?", "A window seat", ["An aisle seat", "A seat in the back", "A seat by the door"], "我想换成靠窗户的。"),
        M("Which seat does the agent offer?", "Seat A in row 15", ["Seat 15 in row A", "Row 19", "Gate 15"], "十五排Ａ座."),
        M("What does the agent ask to see first?", "His passport and boarding pass", ["His ticket and visa", "His luggage tag", "His credit card"], "请先让我看一下您的护照和登机牌。"),
        M("What does David check and what does he carry on?", "Checks the big one, carries the small one", ["Checks both", "Carries both", "Checks the small one, carries the big one"], "这件大的托运，小的我随身带。"),
        M("What does 随身带 mean?", "To carry with you (on board)", ["To send ahead", "To lose", "To buy"], "随身带: carry on."),
        M("What does the agent give him after weighing his luggage?", "A luggage tag", ["A boarding pass", "A passport", "A ticket"], "这是您的行李牌。"),
        M("Where does the agent send David next?", "Through security", ["To the gate directly", "To the customs desk", "To the elevator"], "请到那边过安检。"),
        M("Where is Gate 19, according to the agent?", "Third gate on the right after getting out of the elevator on the second floor", ["First gate on the left", "On the first floor next to security", "Behind the check-in desk"], "出了电梯往前走，右边第三个登机口就是。"),
        M("In Activity 5, where is David’s flight going?", "Hong Kong", ["Beijing", "Shanghai", "Macau"], "到香港。"),
        M("Where does David need to pick up his luggage in Activity 5?", "In Hong Kong", ["In Beijing", "At Gate 15", "He needn’t"], "您只需要在香港取行李。"),
        M("What does 转机 mean?", "Transfer (change planes)", ["Delay", "Cancel", "Board"], "转机: transfer."),
        M("Which means “How many pieces of luggage are you checking in?”", "您要托运几件行李？", ["您有随身带的行李吗？", "请您把行李放在这儿。", "这是您的登机牌。"], "托运几件行李."),
        F("请先让我看一下您的护照和登机___。", "牌", PART, "登机牌: boarding pass."),
        F("请稍等，让我___一下。", "查", PART, "查一下: check."),
        F("我想换___靠窗户的。", "成", PART, "换成: change into."),
        F("请到那边过安___。", "检", PART, "安检: security check."),
    ],
)

# ------------------------------------------------------------------ 2. 的 phrase as a noun
DE5 = [("去北京的请去二十六号登机口，去南京的请去十二号登机口。", "Those going to Beijing please go to Gate 26; those going to Nanjing please go to Gate 12."), ("去北京的人请去二十六号登机口，去南京的人请去十二号登机口。", "(the same with 人 written out)"),
       ("这两个座位，靠窗户的是我的，靠走道的是你的。", "Of these two seats, the window one is mine and the aisle one is yours."), ("这两个座位，靠窗户的座位是我的座位，靠走道的座位是你的座位。", "(the same with 座位 written out)"),
       ("这两件行李，大的托运，小的我随身带。", "Of these two pieces of luggage, the big one I check and the small one I carry on."), ("这两个行李，大的行李托运，小的行李我随身带。", "(the same with 行李 written out; the book writes 个 here)"),
       ("说到饺子啊，老张包的比老陈包的好吃。", "Speaking of dumplings, the ones Lao Zhang makes taste better than the ones Lao Chen makes."), ("说到饺子啊，老张包的饺子比老陈包的饺子好吃。", "(the same with 饺子 written out)"),
       ("美国军人生活不错，住的、吃的、用的都是国家给的。是吗？", "American service members live well; what they live in, eat and use are all given by the country. Is that so?"), ("美国军人生活不错，住的地方、吃的东西、用的东西都是国家给的。是吗？", "(the same with the nouns written out)")]
DE_A1 = [("我朋友说，他要换二百美元人民币，要十张一百块的，六张五十块的。", "My friend says he wants to change 200 dollars into RMB, in ten 100-yuan notes and six 50-yuan notes."), ("我朋友问，你们的公寓，两个卧室的多少钱，一个卧室的多少钱？", "My friend asks, of your apartments, how much is the two-bedroom one and how much is the one-bedroom one?"),
         ("我朋友问，这些水果，好看一点儿的新鲜还是不好看的新鲜？", "My friend asks, of these fruits, are the better-looking ones fresher or the not-so-good-looking ones?"), ("我朋友说，他的茶，要冷的，不要热的。", "My friend says, for his tea, he wants the cold one, not the hot one.")]
L2 = lesson(
    "Lesson 13 Presentation 1 grammar: X 的 as a noun",
    "靠窗户的 · 大的托运，小的我随身带 · 去北京的 · 住的、吃的、用的",
    requires=[],
    cards=[
        card("X 的 as a noun",
             "David said: 1. 我订的是靠走道的座位，我想换成靠窗户的。 2. 这件大的托运，小的我随身带。 In example 1, David meant he wants a 靠窗户的座位 but left out the word 座位. In example 2 he meant to check the 大的行李 and carry on the 小的行李, leaving out 行李. In Chinese, when an object (a person or thing) is known to both speaker and listener in a context, its modifier + 的 (the 的 phrase) can be used to represent the object. The modifier can be a noun, pronoun, adjective, verb or a subject + predicate phrase. Patterns: N/NP/ProN + 的 = N/NP/ProN + 的 + Object; ADJ/ADJP + 的 = ADJ + 的 + Object; V/VP + 的 = V/VP + 的 + Object; SP + 的 = SP + 的 + Object. The function of 的 phrases as nouns is to refer to and differentiate things. The book gives each example followed by its fuller equivalent:",
             examples=[D(z, e) for z, e in DE5]),
        card("Activities 1 and 2",
             "Activity 1 (Writing and Speaking). You accompany your friend to do chores and paraphrase his expressions with 的 phrases when you think he is too wordy. Take turns playing 你的朋友 and 你. 1. At the bank: 我要换二百美元人民币。请给我十张一百元的人民币，六张五十元的人民币。 2. Renting: 你们两个卧室的公寓多少钱？一个卧室的公寓多少钱？ 3. Buying fruit: 好看一点儿的水果新鲜还是不好看的水果新鲜？ 4. At the restaurant: 我要喝冷的茶，不要热的茶。 The book starts each of your answers (我朋友说/问，…) and leaves them to you; my completions:",
             examples=[D(z, e) for z, e in DE_A1]),
        card("Activity 2 (Listening and Speaking)",
             "Pair up. Each person uses 的 phrases to describe a person or an object and the other guesses what it is. The book’s example describes a smartboard:",
             examples=[D("在教室前边的，我们每天上课都看的，很大的，关上时是黑的。", "The thing at the front of the classroom, that we look at in every class, that is very big and is black when it’s turned off. (a smartboard)")]),
    ],
    exercises=[
        M("What does 靠窗户的 stand for in 我想换成靠窗户的?", "靠窗户的座位", ["靠窗户的行李", "靠窗户的护照", "靠窗户的人"], "座位 is left out."),
        M("What does 大的 stand for in 这件大的托运?", "大的行李", ["大的座位", "大的护照", "大的飞机"], "行李 is left out."),
        M("When can a 的 phrase stand for a noun?", "When the noun is known to both speaker and listener", ["Only when the noun is a person", "Only in questions", "Only with adjectives"], "Known object."),
        M("Which cannot be the modifier before 的 in such a phrase?", "A measure word alone", ["A noun", "An adjective", "A verb phrase"], "Noun, pronoun, adjective, verb or subject + predicate."),
        M("What does 去北京的 mean in 去北京的请去二十六号登机口?", "Those going to Beijing", ["Beijing’s gate", "Going to the gate", "The people at the gate"], "去北京的人."),
        M("What does 老张包的 mean?", "The ones Lao Zhang makes (wraps)", ["Lao Zhang’s package", "Lao Zhang is wrapping", "Lao Zhang was wrapped"], "包的饺子."),
        M("What does 住的、吃的、用的 refer to?", "What one lives in, eats and uses", ["Who lives here", "When to eat", "Where to go"], "Verb + 的 as a noun."),
        M("What is the function of 的 phrases as nouns?", "To refer to and differentiate things", ["To ask questions", "To negate verbs", "To show time"], "Refer and differentiate."),
        F("这两个座位，靠窗户的是我___，靠走道的是你的。", "的", PART, "我的: mine."),
        F("我朋友说，他的茶，要冷的，不___热的。", "要", PART, "不要热的: not the hot one."),
        F("说到饺子啊，老张包的比老陈包的好___。", "吃", PART, "好吃: tasty."),
    ],
)

# ------------------------------------------------------------------ 3. 往
WANG1 = [("你下车以后往南走，十分钟就到了。", "After you get off the bus walk south; you’ll be there in ten minutes."), ("往前走两百米就是图书馆。", "Walk forward two hundred meters and there is the library."), ("过了红绿灯往左拐。", "After the traffic light turn left."), ("你往上看。", "Look up.")]
WANG2 = [("二百五十七次航班飞往纽约。", "Flight 257 flies to New York."), ("开往南方的火车有很多。", "There are many trains heading south."), ("请把这件行李运往重庆。", "Please ship this piece of luggage to Chongqing."), ("他们把这些书寄往中国。", "They mailed these books to China. (寄往: mail to)"), ("前往洛杉矶的乘客请到六号登机口。", "Passengers going to Los Angeles please go to Gate 6. (前往: go to)")]
DIRS = [("往上", "up"), ("往下", "down"), ("往前", "forward"), ("往后", "backward"), ("往左", "to the left"), ("往右", "to the right"), ("往南", "south"), ("往北", "north"), ("往东", "east"), ("往西", "west")]
MAP = [("往西走。", "Walk west."), ("在第一个红绿灯往左拐。", "Turn left at the first traffic light."), ("一直往前走。", "Keep going straight ahead."), ("在第二个红绿灯往右拐。", "At the second intersection, turn right."), ("我家就在你的右手边。", "My house is on your right.")]
L3 = lesson(
    "Lesson 13 Presentation 1 grammar: the preposition 往",
    "往左拐 · 往前走 · 往南走 · 飞往纽约 · 前往洛杉矶",
    requires=[],
    cards=[
        card("Preposition 往",
             "The basic meaning of 往 is “moving toward” or “in the direction of”. 往 takes a directional or a place noun to form a “往 phrase”, which precedes a verb: 往 + Direction + Verb. In written language, 往 can also be used after a few monosyllabic verbs (飞, 开, 发, 送, 寄, 运) as a directional complement meaning “to go in the direction of”: Verb + 往 + Direction/Location. (The book prints the numbers as digits: 200 米, 257 次航班.)",
             tables=[wtable(rows_py(DIRS), title="往 + direction")],
             examples=[D(z, e) for z, e in WANG1] + [D(z, e) for z, e in WANG2]),
        card("Activities 3 and 4",
             "Activity 3 (Listening). Listen to the airport announcements and answer: Announcement 1 and 2: who is addressed and what should they do? (Audio, not included.) Activity 4 (Speaking and Listening). Pair up. Your friend is walking to your house and becomes lost. Give the directions below in Chinese while your partner draws a map from them; compare your map with other pairs. The book gives the five steps in both English and Chinese:",
             examples=[D(z, e) for z, e in MAP]),
    ],
    exercises=[
        M("What does 往 mean in 往左拐?", "Toward; in the direction of", ["From", "Behind", "Because of"], "往 + direction + verb."),
        M("What does 往前走两百米就是图书馆 mean?", "Go forward 200 meters and you reach the library", ["The library is 200 meters behind", "Walk to the library and then forward", "The library is closed"], "往前走."),
        M("Where does a 往 phrase go in a sentence?", "Before the verb", ["After the verb always", "At the end", "Before the subject"], "往 + direction + verb."),
        M("What does 二百五十七次航班飞往纽约 mean?", "Flight 257 flies to New York", ["Flight 257 comes from New York", "257 people fly to New York", "Flight 257 is delayed"], "飞往: fly to."),
        M("What does 开往南方的火车 mean?", "Trains heading south", ["Trains from the south", "Slow trains", "Trains that stop in the south"], "开往: head toward."),
        M("What does 前往洛杉矶的乘客 mean?", "Passengers going to Los Angeles", ["Passengers from Los Angeles", "Los Angeles’ airline", "Passengers who are late"], "前往: go to."),
        M("What does 往东 mean?", "To the east", ["To the west", "To the north", "To the south"], "东: east."),
        M("Which means “turn right at the second traffic light”?", "在第二个红绿灯往右拐。", ["在第一个红绿灯往左拐。", "一直往前走。", "往西走。"], "往右拐."),
        M("What does 我家就在你的右手边 mean?", "My house is right on your right", ["My house is behind you", "My house is on your left", "I am at your house"], "右手边: right-hand side."),
        mean("往", "wang3", "to, towards", ["to pass", "to turn", "to change"]),
        mean("拐", "guai3", "to turn", ["to pass", "to change", "to go out"]),
        F("过了红绿灯往左___。", "拐", PART, "往左拐: turn left."),
        F("一直___前走。", "往", PART, "一直往前走: keep going straight."),
    ],
)

# ------------------------------------------------------------------ 4. resultative complements 好 and 完
HW = [("我做完作业了。", "I’ve finished my homework."), ("我吃好饭了。", "I’ve finished eating."), ("我还没有锻炼完。", "I haven’t finished working out yet."), ("你买完东西了吗？", "Have you finished buying things?"), ("你做完功课了没有？", "Have you finished your homework?"), ("饭菜已经做好了。", "The meal is already prepared."), ("信用卡已经办好了。", "The credit card has already been taken care of.")]
HW6 = [("甲：准备好了吗？准备好了我们就开始。", "Are you ready? Once you’re ready we’ll start."), ("乙：准备好了。", "Ready."), ("甲：你锻炼完了吗？锻炼完了我们一起去吃饭。", "Have you finished working out? When you’re done we’ll go eat together."), ("乙：还有几分钟就锻炼完了。", "In a few minutes I’ll be done."),
       ("甲：饮料喝完了吗？喝完了我再买。", "Have you finished the drinks? When they’re finished I’ll buy more."), ("乙：还没喝完呢，不用再买了。", "I haven’t finished yet, no need to buy more."), ("甲：我的手机修好了吗？", "Has my phone been fixed?"), ("乙：修好了。现在可以用了。", "It’s fixed. You can use it now.")]
ESSAY = ("每天都忙的你，是不是只知道“做”，只想“做完”，却没有想过“做”的结果？“做完”和“做好”只有一个字不同，但意思却很不一样。后面一个不但做完了工作，而且有一个好的结果。可是，大多数人只知道自己做了很多，不知道自己做得怎么样，也不在乎自己做得怎么样。一个字的不同，后面是不一样的人生。")
ESSAY_E = ("You who are busy every day, do you only know how to “do”, only want to “finish”, without ever thinking about the result of the “doing”? “做完” and “做好” differ by only one character, but their meanings are very different. The latter not only finishes the work but also has a good result. Yet most people only know that they have done a lot; they don’t know how well they did and don’t care how well they did. One character’s difference; behind it lies a different life.")
L4 = lesson(
    "Lesson 13 Presentation 1 grammar: resultative complements 好 and 完",
    "办好了 · 做完作业了 · 准备好了吗？ · “做完”和“做好”",
    requires=[],
    cards=[
        card("Resultative Complement and 好、完",
             "A complement is a grammatical unit in Chinese. It appears after the main verb to enhance its meaning. Resultative complements indicate the resultative aspect of an action. We learned the resultative complement 完 in Lesson 9, as in 买完文具以后, 他又开始选购衣服. 完 indicates finishing an action, while 好 indicates the completion of an action and/or achieving the desired results. When 好 indicates only the completion of an action, it is interchangeable with 完. In the presentation David says 手续我已经办好了 (or 我已经办好手续了): “I have already completed the boarding procedures.” Patterns: Object + Subject + Verb + Resultative Complement + 了. Subject + Verb + Resultative Complement + Object + 了. Question: Subject + Verb + Resultative Complement + Object + 了 + 吗/没有？ Negative: Subject + 没有 + Verb + Resultative Complement + Object.",
             examples=[D(z, e) for z, e in HW]),
        card("Activities 5 and 6",
             "Activity 5 (Listening and Writing). Listen to the dialog between Xiaoming and his mother and answer: 1. When did the conversation most likely take place? 2. When does Xiaoming plan to do his homework? 3. Why does the mother ask 你吃好了吗？ 4. What will Xiaoming probably do when his homework is finished? (Audio, not included.) Activity 6 (Reading, Writing and Speaking). A. Complete the sentences with the correct resultative complement, 完 or 好. B. Share your work with a classmate and discuss any differences. The blanks are empty in the book; the completed exchanges are mine:",
             examples=[D(z, e) for z, e in HW6]),
        card("Activity 7 (Reading and Speaking)",
             "“做完”和“做好”—两种不同的人生: read and discuss the short text below.",
             examples=[D(ESSAY, ESSAY_E)]),
    ],
    exercises=[
        M("What does 完 indicate?", "Finishing an action", ["Beginning an action", "Repeating an action", "Stopping a plan"], "完: finish."),
        M("What does 好 indicate?", "Completing an action and/or achieving the desired result", ["A bad result", "A habit", "A question"], "好: completion and desired result."),
        M("What does 我已经办好手续了 mean?", "I have already completed the procedures", ["I will do the procedures", "I can’t do the procedures", "I forgot the procedures"], "办好: completed."),
        M("Which is the negative of 我做完作业了?", "我没有做完作业。", ["我不做完作业。", "我做不完作业了。", "我没做作业完。"], "没有 + verb + complement."),
        M("Which is the correct question?", "你买完东西了吗？", ["你买东西完了吗？", "你完买东西了吗？", "你买了完东西吗？"], "Subject + verb + complement + object + 了 + 吗."),
        M("What does 饭菜已经做好了 mean?", "The meal is already prepared", ["The meal was bad", "The meal is gone", "No meal was made"], "做好: ready."),
        M("What does 我还没有锻炼完 mean?", "I haven’t finished working out yet", ["I will never work out", "I worked out too much", "I like working out"], "没有…完: not finished."),
        M("Which fits: 我的手机修___了吗？ (is my phone fixed?)", "好", ["完", "到", "成"], "修好: fixed, so it works."),
        M("In the essay, what is the difference between 做完 and 做好?", "做好 also has a good result", ["做完 is better", "They are identical", "做好 means not finished"], "后面一个不但做完了工作，而且有一个好的结果。"),
        F("你做___功课了没有？", "完", PART, "做完功课: finished the homework."),
        F("饭菜已经做___了。", "好", PART, "做好: prepared."),
        F("我还没有锻炼___。", "完", PART, "锻炼完: finish exercising."),
    ],
)

# ------------------------------------------------------------------ 5. simple directional verbs
SDV = [("我上楼拿东西。", "I’m going upstairs to get something."), ("往前走，过了汽车站就是商店。", "Go straight; after you pass the bus station, there is the store."), ("刚进教室就上课了。", "Class began just as I entered the classroom."), ("下了楼就是机场服务台。", "Once you go downstairs, there is the airport service desk."),
       ("你每天几点回家。", "What time do you go home every day?"), ("周六来我家吃饭。", "Come to my house to eat on Saturday."), ("我们七点去学校。", "We go to school at seven.")]
SDV_T1 = [("进教室", "enter the classroom"), ("出学校", "leave the school"), ("上楼", "go upstairs"), ("下车", "get off the car"), ("回家", "go home"), ("过桥", "cross the bridge"), ("起床", "get up")]
DIR8 = ("从图书馆这里去红花饭店，得先下山。你在前面这条路往右拐，然后往前走，出了富兰克林大门，往山下走。过两个红绿灯，在第三个红绿灯往左拐，这时候你在太平街上。往前走，过一个红绿灯，在第二个红绿灯往右拐，然后再往左拐，红花饭店就在你的右边。你得上二楼，才可以进饭店。吃完饭以后回学校，你得上山，有点儿累哦。")
DIR8_E = ("To get to the Benihana restaurant from the library here, you first have to go down the hill. Turn right on the road in front, then go straight, go out through the Franklin gate and head down the hill. Pass two traffic lights and turn left at the third traffic light; at this point you are on Taiping Street. Go straight, pass one traffic light, turn right at the second traffic light and then left, and the restaurant is on your right. You have to go up to the second floor to be able to enter the restaurant. After the meal, to return to school you have to go up the hill, which is a bit tiring!")
DIR9 = ("进了机场大厅，坐电梯上三楼，出了电梯往左拐，过三个登机口，就是中国民航服务台，服务台在你的左手边。")
DIR9_E = "After you enter the airport hall, take the elevator up to the third floor, turn left after getting out of the elevator, pass three boarding gates, and there is the airline service desk; it’s on your left-hand side."
L5 = lesson(
    "Lesson 13 Presentation 1 grammar: simple directional verbs",
    "进 出 上 下 回 过 起 · 来 去 · 出了电梯往前走 · 过了安检往左拐",
    requires=[],
    cards=[
        card("Simple Directional Verbs",
             "The check-in agent tells David: 过了安检，往左拐，坐电梯上二楼，出了电梯往前走，右边第三个登机口就是. In this instruction 过 (“to pass through”), 上 (“to go up”) and 出 (“to go out”) are “simple directional verbs”. Like other transitive verbs they can take objects, but they also indicate directions of movement. There are two types. Type 1: 进, 出, 上, 下, 回, 过, 起; the directions are in reference to locations. Type 2: 来 and 去; the directions are in reference to the speaker: 来 (similar to “come”) means the action is toward the speaker, 去 (similar to “go”) that it is away from the speaker.",
             tables=[wtable(rows_py(SDV_T1), title="Type 1 verbs with an object")],
             examples=[D(z, e) for z, e in SDV]),
        card("Activities 8 and 9",
             "Activity 8 (Reading and Writing). You tell a Chinese friend how to get from the library to the Benihana restaurant. Choose from 进, 出, 上, 下, 回, 过 to complete the directions, using the map as reference (the map is not included; the blanks are empty in the book, so the completed directions are mine, and the book’s gate name Franklin is written 富兰克林).",
             examples=[D(DIR8, DIR8_E)]),
        card("Activity 9 (Speaking)",
             "A. Pair up. Decide on a starting point and a destination at an airport you have been to, then give your partner simple directions using at least three of 进, 出, 上, 下, 回, 过; exchange roles and repeat. Example: starting point 机场大厅; destination 中国民航 (mínháng, airline) 服务台. B. Pair up. Decide on a place in DLI as the destination and ask your partner to give simple directions using at least three of the directional verbs. The book’s example:",
             examples=[D(DIR9, DIR9_E)]),
    ],
    exercises=[
        M("What do the simple directional verbs of Type 1 refer to?", "Locations", ["The speaker", "The time", "The weather"], "进、出、上、下、回、过、起: in reference to locations."),
        M("What do 来 and 去 refer to?", "The speaker’s position", ["A place name", "A time", "A person’s age"], "来 toward, 去 away from the speaker."),
        M("What does 过桥 mean?", "Cross the bridge", ["Build a bridge", "Go under the bridge", "Buy a bridge"], "过: pass through."),
        M("What does 起床 mean?", "Get up", ["Make the bed", "Lie in bed", "Buy a bed"], "起床."),
        M("What does 下了楼就是机场服务台 mean?", "Once you go downstairs, there is the airport service desk", ["The service desk is upstairs", "You can’t go downstairs", "The desk is on the roof"], "下楼: go downstairs."),
        M("What does 刚进教室就上课了 mean?", "Class began just as I entered the classroom", ["I left the classroom", "Class was cancelled", "I was late for lunch"], "进教室: enter the classroom."),
        M("Which means “Come to my house to eat on Saturday”?", "周六来我家吃饭。", ["周六去我家吃饭。", "周六回我家吃饭。", "周六出我家吃饭。"], "来: toward the speaker."),
        M("In 出了电梯往前走, what does 出 mean?", "Go out of", ["Go up", "Go down", "Return to"], "出了电梯: after getting out of the elevator."),
        M("Which completes: 吃完饭以后___学校? (return to school)", "回", ["进", "出", "起"], "回学校: return to school."),
        F("你得上二楼，才可以___饭店。", "进", PART, "进饭店: enter the restaurant."),
        F("过两个红绿灯，在第三个红绿灯往左___。", "拐", PART, "往左拐: turn left."),
        F("我上___拿东西。", "楼", PART, "上楼: go upstairs."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
BOSS = [("王先生是一家电脑公司的经理，常常需要到别的城市出差。有一次，他要去上海出差。因为太忙，所以他让新来公司的小李去买票。王先生很胖，他告诉小李说：“你帮我订两张北京到上海的往返票。要明天一早出发，后天下午五点以后回来的。”",
         "Mr. Wang is a manager at a computer company and often has to go to other cities on business trips. Once, he had to go to Shanghai on business. Because he was too busy, he had Xiao Li, who had just joined the company, buy the ticket. Mr. Wang is fat. He told Xiao Li: “Book me two round-trip tickets from Beijing to Shanghai. They should leave early tomorrow morning and return after five o’clock the day after tomorrow.”"),
        ("小李很快就在网上订好了票，他高兴地对王经理说：“经理，票已经订好了！明天早上八点十分出发，后天下午五点一刻回来。而且今天运气不错，买到的两张票都是靠窗户的！”",
         "Xiao Li quickly booked the tickets online and said happily to Manager Wang: “Manager, the tickets are booked! You leave tomorrow morning at 8:10 and return the day after tomorrow at 5:15 in the afternoon. And today we’re lucky; both tickets I bought are window seats!”")]
TF13 = [("还有两个飞往香港的航班，旅客可以坐上午的，也可以坐下午的。", "There are two more flights to Hong Kong; the passenger can take the morning one or the afternoon one."), ("旅客更喜欢靠窗户的座位。", "The passenger prefers a window seat."), ("旅客不需要托运行李，因为他只有随身带的行李。", "The passenger doesn’t need to check luggage because he only has carry-on luggage."), ("服务员给了旅客登机牌和行李牌。", "The agent gave the passenger a boarding pass and a luggage tag.")]
CHEN = ("陈丽在中国银行工作。因为工作需要，她常常得坐飞机去香港，澳门和新加坡。她都是在网上订机票，然后在网上办理登机手续。这样，到机场以后，就只需要托运行李。每次她带的行李都不多，一个大一点的箱子托运，里面放衣服什么的，小的她就随身带上飞机。她每次都把护照放在随身带的行李箱里。除了护照以外，她还喜欢随身带一本书和一些小吃。她喜欢看飞机外的风景，所以每次都订靠窗户的座位。有时，她也看看书，或是跟旁边的人聊聊天。")
CHEN_E = ("Chen Li works at the Bank of China. Because of her work she often has to fly to Hong Kong, Macau and Singapore. She always books air tickets online and then checks in online. This way, after arriving at the airport she only needs to check her luggage. Each time she doesn’t bring much luggage: a somewhat bigger suitcase to check, with clothes and so on inside, and the small one she carries on the plane. She always puts her passport in the carry-on bag. Besides her passport she also likes to carry a book and some snacks. She likes to look at the scenery outside the plane, so she books a window seat every time. Sometimes she also reads a book or chats with the person beside her.")
CHEN_Q = [("陈丽在哪儿工作？", "Where does Chen Li work?"), ("她为什么常常坐飞机？", "Why does she often fly?"), ("她怎么订机票和办理登机手续？", "How does she book tickets and check in?"), ("她为什么每次都订靠窗户的座位？", "Why does she book a window seat every time?")]
L6 = lesson(
    "Lesson 13 Presentation 1: skill integration",
    "王先生订票 · 陈丽的旅行 · 机场对话",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking, Writing and Listening): Mr. Wang’s tickets",
             "A. Pair up. Read one paragraph of the story while your partner reads the other. Report what you read to your partner, note the EEIs of your partner’s report, transcribe the critical words and check your dictionary for any words you do not know. B. Discuss with your partner and write your answers: 1. Will the manager be satisfied with Xiao Li’s effort? Why? 2. Why did Xiao Li make the mistake? My reading of the joke (the book gives no answers): Mr. Wang is fat and asked for two tickets, so he needs two seats next to each other; two window seats cannot be side by side, so he will not be satisfied, and the new employee did not understand why his boss wanted two tickets.",
             examples=[D(z, e) for z, e in BOSS]),
        card("Activity 2 (Listening, Speaking and Reading)",
             "Pair up. Listen to the two dialogs at the airport check-in desk and answer the questions. Dialog 1: 1. What method did the passenger use to check in? 2. What did the passenger say about his boarding pass? 3. What did the passenger ask of the airline agent? 4. What was said about his luggage? Dialog 2: 1. Where does the passenger want to go? 2. Provide details about the flight. 3. Provide details about the passenger’s luggage. 4. What is his next stop? 5. What directions was he given? B. Using what you heard, mark the statements below true or false; discuss in groups of three, then with the class. (Audio, so no key is given.)",
             examples=[D(z, e) for z, e in TF13]),
        card("Activity 3 (Reading and Speaking)",
             "Pair up and read the passage. Each student then creates three questions in Chinese to ask their partner. The book leaves the questions empty; mine:",
             examples=[D(CHEN, CHEN_E)] + [D(z, e) for z, e in CHEN_Q]),
        card("Activity 4 (Listening and Speaking)",
             "Listen to two dialogs. Transcribe the critical unknown words and look them up in your dictionary; discuss the problems and solutions with a partner. (Audio, not included.)"),
    ],
    exercises=[
        M("What is Mr. Wang’s job?", "Manager at a computer company", ["Airline agent", "Bank clerk", "Teacher"], "王先生是一家电脑公司的经理。"),
        M("Why did he ask Xiao Li to buy the tickets?", "He was too busy", ["He was ill", "He didn’t know how", "He was on vacation"], "因为太忙，所以他让新来公司的小李去买票。"),
        M("What kind of tickets did Mr. Wang ask for?", "Two round-trip tickets from Beijing to Shanghai", ["One one-way ticket", "Two tickets to Beijing", "A hotel booking"], "两张北京到上海的往返票。"),
        M("When did the tickets leave?", "Tomorrow morning at 8:10", ["Tomorrow night", "The day after tomorrow", "At 5:15"], "明天早上八点十分出发。"),
        M("What did Xiao Li say about the seats?", "Both were window seats", ["Both were aisle seats", "They were side by side", "They were first class"], "买到的两张票都是靠窗户的！"),
        M("What does 往返票 mean?", "Round-trip ticket", ["One-way ticket", "Boarding pass", "Luggage tag"], "往返: go and return."),
        M("Where does Chen Li work?", "At the Bank of China", ["At an airline", "At a school", "At the airport"], "陈丽在中国银行工作。"),
        M("Where does Chen Li often fly?", "Hong Kong, Macau and Singapore", ["Beijing, Shanghai and Xi’an", "New York and Chicago", "Tokyo and Seoul"], "香港，澳门和新加坡。"),
        M("How does Chen Li check in?", "Online", ["At the counter", "By phone", "At the gate"], "在网上办理登机手续。"),
        M("Why does she book a window seat?", "She likes to look at the scenery outside", ["She dislikes people", "It is cheaper", "It is nearer the exit"], "她喜欢看飞机外的风景。"),
        M("Where does she put her passport?", "In her carry-on bag", ["In her checked suitcase", "In her pocket", "At home"], "把护照放在随身带的行李箱里。"),
        F("她都是在网上订机___。", "票", PART, "订机票: book a flight ticket."),
        F("她常常得___飞机去香港。", "坐", PART, "坐飞机: take a plane."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context
FL = [("芝加哥—北京", "国航", "2970", "5010", "2.15-2.21"), ("洛杉矶—上海", "美联航", "4350", "8200", "3.15-6.15"), ("旧金山—北京", "国航", "3100", "4260", "4.22-4.30"), ("旧金山—广州", "美西北", "3300", "3610", "5.12-5.16"), ("纽约—北京", "美西北", "-", "4540", "5.15-5.20"), ("纽约—西安", "国航", "3950", "5860", "9.2-10.2")]
L7 = lesson(
    "Lesson 13 Presentation 1: using Chinese in context",
    "航线 · 机票信息 · 单程 往返 · 北京大兴国际机场 · 携程网",
    requires=[],
    cards=[
        card("Activities 1 and 2",
             "Activity 1 (Reading and Speaking). Pair up and share your experience of the last time you traveled by air; include 出发时间和城市, 到达时间和城市, 转机, 行李, etc. Activity 2 (Reading and Speaking). Below is flight information from a travel information website in China (prices in yuan; valid dates as printed). Choose one of the American cities as your hometown and use it to find out how to travel to Beijing: what flight would you take and why? In groups of three share your choices and reasons.",
             tables=[table(["航线", "航空公司", "单程", "往返", "有效日期"], FL, title="Flight information")]),
        card("Activity 3 (Reading and Speaking)",
             "A. Listen to five recordings and write the kind of seat the speakers request and why (Comment 1 to Comment 5: preferred seat; reason). B. In groups of three, list all five comments in your desired order for a window seat, compare and discuss any differences. (Audio, not included.)"),
        card("Activity 4 (Reading and Speaking): the e-ticket",
             "Pair up. In Chinese, answer the questions orally using the information on the e-ticket: 1. Is the ticket round trip or one-way? 2. What is the cost? 3. What are the departure city and the destination? 4. What is the flight number? 5. Which airline? 6. What is the flight schedule? The e-ticket (机票信息) reads as in the table, and my answers are in the second table.",
             tables=[table(["Item", "Information"], [("出发日期", "02-26"), ("出发地", "北京大兴国际机场"), ("航班号", "CS254"), ("起飞时间", "08:30"), ("目的地", "上海虹桥国际机场"), ("机型", "波音 787"), ("到达时间", "09:45"), ("航空公司", "中国东方航空集团公司"), ("回程备注", "单程"), ("原价", "¥1050"), ("销售价", "¥890"), ("出票条件", "限散客"), ("出票方式", "提前三天")], title="机票信息"),
                     table(["Question", "Answer (mine)"], [("1. Round trip or one-way?", "One-way (单程)"), ("2. Cost", "890 yuan (original price 1,050)"), ("3. Cities", "From Beijing Daxing International Airport to Shanghai Hongqiao International Airport"), ("4. Flight number", "CS254"), ("5. Airline", "China Eastern Airlines"), ("6. Schedule", "February 26, departs 8:30, arrives 9:45")], title="Answers")]),
        card("Activities 5 to 7",
             "Activity 5 (Reading and Speaking). Pair up. Choose one location from the list without revealing it; give your partner directions using the map and location key (you are both at 进口处) and your partner tries to determine the destination. The list: 1. 中餐厅 2. 十号登机口 3. 商场 4. 行李提取处 5. 二十号登机口 6. 卫生间. Useful phrases: 向（右）拐, 往（前）走, 坐电梯（上去）, 出了电梯, 往（左）拐, 在右手边. (The map is a picture, not included.) Activity 6 (Reading and Listening). Listen to the airport announcements (1 to 4) and mark each True or False using the departure information shown. (Audio, not included.) Activity 7 (Reading, Speaking and Listening). A. Create two groups of three; one group travels to 北京, the other to 广州. Decide on a time for your trip, then each group member searches one of the websites 携程网, MoMondo or Expedia and chooses where to buy the ticket. Fill in the table (出发城市 旧金山; 到达城市; 航空公司; 机票价格; 起飞日期和时间; 到达日期和时间; 转机; 回美国日期和时间) and report to your group. B. Compare the information, decide which ticket to book and report your group’s decision to the class."),
    ],
    exercises=[
        M("What does 单程 mean?", "One-way", ["Round trip", "Direct flight", "Business class"], "单程: one-way."),
        M("What does 往返 mean in a fare table?", "Round trip", ["One-way", "Transfer", "Delay"], "往返: round trip."),
        M("Which airline flies 芝加哥—北京 in the table?", "国航", ["美联航", "美西北", "东方航空"], "国航 (Air China)."),
        M("What is the one-way price for 旧金山—北京?", "3100", ["4260", "3300", "2970"], "单程 column."),
        M("Which route has no one-way fare?", "纽约—北京", ["旧金山—广州", "洛杉矶—上海", "芝加哥—北京"], "单程 is “-”."),
        M("What is the flight number on the e-ticket?", "CS254", ["CS524", "CS452", "CS245"], "航班号 CS254."),
        M("What is the sales price of the e-ticket?", "890 yuan", ["1,050 yuan", "1,890 yuan", "8,900 yuan"], "销售价 ¥890."),
        M("When does the flight take off and land?", "8:30 and 9:45", ["9:45 and 8:30", "8:30 and 8:45", "8:00 and 10:30"], "起飞 08:30, 到达 09:45."),
        M("Which airport is the destination?", "上海虹桥国际机场", ["北京大兴国际机场", "广州白云国际机场", "香港国际机场"], "目的地."),
        M("Is the e-ticket round trip?", "No, it is one-way", ["Yes, it is round trip", "It is a transfer flight", "It has no return"], "回程备注: 单程."),
        mean("单程", "dan1 cheng2", "one-way trip", ["round trip", "boarding gate", "luggage tag"]),
        F("请问，十九号登机___怎么走？", "口", PART, "登机口: boarding gate."),
    ],
)

L8 = vocab_lesson("Lesson 13 Presentation 1 vocabulary", "17 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十三课 人在机场 Presentation 1: check-in, 的 phrases, 往, 好/完, directional verbs", [L1, L2, L3, L4, L5, L6, L7, L8])
