"""Unit 57: Lesson 20 (The Post Office) Presentation 1 from the book's texts: the post-or-express dialog, the time-order modifiers, 亲自, 恐怕/大概/也许,
the 不仅...而且 construction, the skill-integration activities (Jenny's email and two postal workers), the using-Chinese activities (the 黑猫宅急便 table
and the express-service FAQ) and the vocabulary list. Audio, pictures, forms and links are not included; numbers the book writes as digits are
spelled out in the Chinese text; answer keys the book does not print are mine and labeled."""
from zh_auto import *
from zh_l20_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3")):
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

# ------------------------------------------------------------------ 1. the dialog
P1 = [("陈雪晴", "大年，下个月五号是我奶奶的生日。她住在纽约，我想给她寄一张生日卡和一个小礼物。你觉得怎么寄好呢？", "Danian, the fifth of next month is my grandmother’s birthday. She lives in New York and I want to send her a birthday card and a small gift. How do you think I should send them?"), ("李大年", "去邮局或是找快递公司都可以。", "You can go to the post office or use an express delivery company."),
      ("陈雪晴", "哪个比较好呢？", "Which is better?"), ("李大年", "那得看了。快递公司可以上门服务。邮局呢？你得亲自去，但是寄贵重物品更保险一些。", "That depends. Express companies can serve you at your door. The post office? You have to go in person, but for valuable items it’s safer."),
      ("陈雪晴", "我的好多同事都喜欢用快递公司寄包裹，那现在去邮局的人恐怕不太多了吧？", "Many of my colleagues like to use express companies to send parcels, so I’m afraid not many people go to the post office now?"), ("李大年", "是比以前少了。但是邮局不仅能寄信、寄包裹，还卖信封和邮票，而且……", "There are fewer than before. But the post office can not only send letters and parcels, it also sells envelopes and stamps, and moreover…"),
      ("陈雪晴", "而且？你是说，他们还有别的业务？", "And moreover? You mean they have other businesses too?"), ("李大年", "对。除了原有的业务外，他们还增加了代理保险，代收水电费，代售交通卡等业务。", "Yes. Besides the original business, they have also added acting as an insurance agent, collecting water and electricity bills, selling transit cards and so on."),
      ("陈雪晴", "看来邮局还是很重要的。", "It seems the post office is still very important."), ("李大年", "当然，特别是在一些快递服务不太发达的地方，老百姓就只能靠邮局了。", "Of course, especially in places where express service is not well developed, ordinary people can only rely on the post office."),
      ("陈雪晴", "我还没去过中国的邮局呢，那今天下午我就去邮局给我奶奶寄东西。", "I haven’t been to a Chinese post office yet, so this afternoon I’ll go to the post office and send things to my grandmother."), ("李大年", "我们公司后面就有一个邮局。六点关门，现在都快五点半了。你赶快去吧！", "There is a post office right behind our company. It closes at six, and it’s almost 5:30 now. Hurry up and go! (the book writes 5 点半 with a digit)"), ("陈雪晴", "我马上去！", "I’ll go right away!")]
L1 = lesson(
    "Lesson 20 Presentation 1: should I send it by post or by express?",
    "奶奶的生日卡 · 邮局还是快递公司 · 亲自去 · 增加的新业务",
    requires=[],
    cards=[
        card("Learning objectives (Lesson 20, The Post Office, 在邮局)",
             "Unit 4 continues with Survival Skills and Social Factors. In this lesson you will obtain and provide information about mailing letters and parcels at the post office or with shipping services, describe the key services of the post office, carry out the mailing of letters or parcels or other procedures at the post office, and narrate a personal experience of mailing items by various means. To do so you must master the core vocabulary and patterns, the special modifiers for time order (表示时间先后的特别修饰语), the usage of 亲自, 恐怕, the 不仅…而且 construction, the post-modifier cluster in the 比 pattern, 最多/最少, 要看, the differences among 不过, 但是 and 可是, the connector 另外, the causative verb 使, the usage of 所有的 and the usage of 被 in neutral context. The Area Studies topic is the post office in China."),
        card("Getting Started",
             "A photograph of a post office (not included). Pair up and discuss: A. What services are provided by the post office in the U.S.? Do you know how to say them in Chinese? B. When was the last time you visited a post office? What did you do there? C. Have you ever used other shipping carriers? Why did you choose their services? If not, why?"),
        card("Presentation 1: 寄生日卡和礼物", "The book also prints the dialog in traditional characters.", examples=dlg(P1)),
    ],
    exercises=[
        M("Whose birthday is next month on the fifth?", "Chen Xueqing’s grandmother’s", ["Li Danian’s mother’s", "Chen Xueqing’s own", "A colleague’s"], "下个月五号是我奶奶的生日."),
        M("Where does her grandmother live?", "New York", ["Beijing", "Shanghai", "Taipei"], "她住在纽约."),
        M("What does she want to send?", "A birthday card and a small gift", ["A parcel of books", "Money", "Flowers"], "一张生日卡和一个小礼物."),
        M("What does Danian say about express companies?", "They can serve you at your door", ["They are cheaper", "They are slower", "They only send letters"], "快递公司可以上门服务."),
        M("What does Danian say about the post office?", "You have to go in person, but valuables are safer", ["It delivers to the door", "It is always faster", "It is closed"], "你得亲自去，但是寄贵重物品更保险一些."),
        M("What does Xueqing say her colleagues like?", "Using express companies to send parcels", ["Writing letters", "Using the post office", "Flying"], "我的好多同事都喜欢用快递公司寄包裹."),
        M("Which new services has the post office added?", "Insurance agency, bill collection and transit-card sales", ["Banking only", "Phone repairs", "Hotel booking"], "代理保险，代收水电费，代售交通卡."),
        M("Where does Danian say people rely on the post office?", "Where express service is not well developed", ["In big cities", "At airports", "Abroad"], "快递服务不太发达的地方."),
        M("When does the post office close?", "At six", ["At five", "At seven", "At noon"], "六点关门."),
        M("What time is it in the dialog?", "Almost half past five", ["Almost six", "Almost noon", "Almost midnight"], "现在都快五点半了."),
        F("邮局不仅能寄信、寄包裹，还卖信封和___票。", "邮", PART, "邮票: stamp."),
        F("你得亲___去，但是寄贵重物品更保险一些。", "自", PART, "亲自: in person."),
        F("除了原有的业务外，他们还增___了代理保险等业务。", "加", PART, "增加: add."),
    ],
)

# ------------------------------------------------------------------ 2. activities 1-4
CLS = table(["原有的服务 (mine)", "新增的服务 (mine)"],
            [["邮票，信封，信，包裹，邮费，邮箱，邮政编码，收件人，寄件人", "保险，水电费，交通卡"]],
            title="Activity 1: sorting the post-office words (the book leaves the table blank; 邮局, 快递公司 and 邮递员/邮差 are places and people rather than services, so I leave them out)", say=[0, 1])
TF20 = [("陈雪晴最后打算去邮局寄一个包裹。", "1. In the end Chen Xueqing plans to go to the post office to send a parcel. — True (she says she will go this afternoon; key mine)"), ("李大年觉得用快递公司寄包裹比邮局便宜得多。", "2. Li Danian thinks sending a parcel by an express company is much cheaper than the post office. — False (he never mentions price)"), ("李大年觉得寄贵重的东西快递公司比邮局保险。", "3. Li Danian thinks an express company is safer than the post office for valuables. — False (he says the post office is safer)"),
        ("快递公司在中国的一些不发达的地方不提供服务。", "4. Express companies do not provide service in some undeveloped places in China. — True in spirit (he says express service is not well developed there, so people rely on the post office; mine)"), ("中国的邮局只能寄信、寄包裹、买邮票什么的，没有其他的服务。", "5. China’s post offices can only send letters and parcels and sell stamps, with no other services. — False (they added insurance, bill collection and transit cards)")]
MT20 = [("陈雪晴的奶奶要过生日了，所以她想给奶奶寄一个礼物。", "1 + e. Chen Xueqing’s grandmother’s birthday is coming, so she wants to send her grandmother a gift. (key mine)"), ("在中国寄东西可以用快递公司，也可以用邮局。", "2 + a. In China you can send things by an express company or by the post office. (mine)"), ("快递公司可以上门服务，比邮局方便得多。", "3 + d. Express companies can serve you at your door, which is much more convenient than the post office. (mine)"),
        ("邮局不仅卖信封、邮票，而且还可以代收费用和代售交通卡。", "4 + c. The post office not only sells envelopes and stamps but can also collect fees and sell transit cards as an agent. (mine)"), ("对于不发达地区的老百姓来说，邮局还是很重要的。", "5 + b. For the people in underdeveloped areas the post office is still very important. (mine)")]
L2 = lesson(
    "Lesson 20 Presentation 1 activities: services of the post office and express companies",
    "Activities 1 to 4 · 原有的服务 新增的服务 · 判断对错 · 配对",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking and Listening)",
             "A. Below is post-office vocabulary: 邮局, 邮票, 邮箱, 水电费, 邮政编码, 交通卡, 信封, 信, 包裹, 保险, 收件人, 寄件人, 邮费, 快递公司, 邮递员/邮差. Identify the words that belong to the traditional post office services and to the newly added services and write them in the categories, adding the appropriate verbs for each phrase (e.g. 寄信, 买邮票, 代收水电费). B. Pair up and check your answers. C. Each partner selects three words that are in neither category and figures out their meaning. D. Use the vocabulary to create three sentences; your partner translates them. My sorting:",
             tables=[CLS]),
        card("Activity 2 (Listening, Speaking and Reading)",
             "A. Global listening: 1. What is the topic of this conversation? 2. What is the view of the second speaker regarding the post office? How do you know? B. Detailed listening: 1. What are the advantages of using the post office and other parcel services? 2. What services are provided by the post office? List at least four. C. Pair up and share your answers in Chinese. D. Four sentences: listen, transcribe a segment, then listen to the entire sentence and translate it. (Audio, not included. From the text: the topic is how to send a card and a gift to a grandmother; the second speaker thinks the post office is still very important.)"),
        card("Activity 3 (Reading and Speaking)",
             "A. Read Presentation 1 and mark the five statements True or False; for false statements give your reason and correct them. B. Match the first half of the sentence in Column A with the second half in Column B. The book prints no key; my answers:",
             examples=[D(z, e) for z, e in TF20 + MT20]),
        card("Activity 4 (Listening and Speaking)",
             "A. Listen to a dialog between a local citizen and a foreign traveler in Taipei and answer: 1. Why is the female speaker going to the post office? 2. What differences between the post office and other express couriers are noted? 3. Why is the bank mentioned in the conversation? 4. Why did the female speaker purchase insurance? 5. What conclusion does Mark arrive at? B. Pair up and take turns asking and answering questions in Chinese to check your answers. (Audio, not included; the book prints no script.)"),
    ],
    exercises=[
        M("In the matching, which line completes “快递公司可以上门服务，”?", "比邮局方便得多", ["所以她想给奶奶寄一个礼物", "邮局还是很重要的", "也可以用邮局"], "3 + d."),
        M("Which line completes “邮局不仅卖信封、邮票，”?", "而且还可以代收费用和代售交通卡", ["比邮局方便得多", "也可以用邮局", "所以她想给奶奶寄一个礼物"], "4 + c."),
        M("Which statement is true?", "邮局增加了代理保险等业务", ["邮局只能寄信", "邮局比快递公司便宜得多", "快递公司比邮局更保险"], "增加了代理保险."),
        M("Which service is a newly added one?", "代收水电费", ["寄信", "卖邮票", "卖信封"], "新增的服务."),
        M("Which is a traditional service?", "卖邮票", ["代理保险", "代售交通卡", "代收水电费"], "原有的服务."),
        M("What does 上门 mean in 上门服务?", "Come to your door", ["Close the door", "Open the door", "Wait at the door"], "上门: deliver at the door."),
        M("Why do people in undeveloped areas rely on the post office?", "Express service is not well developed there", ["The post office is free", "They have no addresses", "They love stamps"], "快递服务不太发达."),
        M("Who is 收件人?", "The person receiving the item", ["The postman", "The sender", "The clerk"], "收件人: addressee."),
        F("邮局还是很重___的。", "要", PART, "重要: important."),
        F("对于不发达地区的老百___来说，邮局还是很重要的。", "姓", PART, "老百姓: common people."),
    ],
)

# ------------------------------------------------------------------ 3. time words
TW = table(["大前年", "前年", "去年", "今年", "明年", "后年", "大后年"], [["the year before the year before last", "the year before last", "last year (exception)", "this year", "next year", "the year after next", "three years from now"]], title="Set one for 年: 大前--前--去--今--明--后--大后")
TW2 = table(["大前天", "前天", "昨天", "今天", "明天", "后天", "大后天"], [["three days ago", "the day before yesterday", "yesterday (exception)", "today", "tomorrow", "the day after tomorrow", "three days from now"]], title="Set one for 天: 大前--前--昨--今--明--后--大后")
TW3 = table(["上上(个)星期", "上(个)星期", "这(个)星期", "下(个)星期", "下下(个)星期"], [["the week before last", "last week", "this week", "next week", "the week after next"]], title="Set two for 星期: 上上(个)--上(个)--这(个)--下(个)--下下(个)")
TW4 = table(["上上(个)月", "上(个)月", "这(个)月", "下(个)月", "下下(个)月"], [["the month before last", "last month", "this month", "next month", "the month after next"]], title="Set two for 月")
TWE = [("下个月五号是我奶奶的生日。", "1. The fifth of next month is my grandmother’s birthday."), ("上个星期我坐高铁去上海。", "2. Last week I took the high-speed rail to Shanghai."), ("明年他的孩子就要上大学了！", "3. Next year his child will go to college!"), ("前天他去邮局开了个邮箱。", "4. The day before yesterday he went to the post office and opened a P.O. box.")]
TWA1 = [("他下个月要去中国出差。", "1. He will go to China for a business trip next month. (translation mine)"), ("前年他住在台湾。", "2. He lived in Taiwan the year before last. (mine)"), ("我三天前见到了我的老同学。", "3. I met my old classmate three days ago. (mine)"), ("我后年要搬到德克萨斯去。", "4. I will move to Texas the year after next. (mine)"), ("我订好了下下个星期的高铁票。", "5. I booked the high-speed rail ticket for the week after next. (mine)")]
L3 = lesson(
    "Lesson 20 Presentation 1 grammar: modifiers for earlier and later times",
    "大前年 前年 去年 今年 明年 后年 · 上(个)星期 下(个)月 · 天和年不能用个",
    requires=[],
    cards=[
        card("表示时间先后的特别修饰语",
             "Students may occasionally say 一个天, 下个年 or 后个月, which are wrong in Chinese. The most obvious reason is the difference in how Chinese and English indicate previous and future days, weeks, months and years. Unlike English, Chinese uses two sets of modifiers. Set one, 大前--前--去/昨--今--明--后--大后, covers 天 and 年. Note 1: 天 and 年 use the same set of modifiers except for the previous day (昨天) and the previous year (去年). Note 2: 天 and 年 cannot take 个 as a measure word. Set two, 上上(个)--上(个)--这(个)--下(个)--下下(个), covers 星期 and 月. Note 3: 个 is optional in the table below; however, when a number is used before 月, adding or omitting 个 creates a difference in meaning: 一个月 means “a month”, whereas 一月 means “January”.",
             tables=[TW, TW2, TW3, TW4], examples=[D(z, e) for z, e in TWE]),
        card("Grammar Activities 1 and 2",
             "Activity 1 (Reading and Writing): translate the sentences into Chinese: 1. He will go to China for a business trip next month. 2. He lived in Taiwan the year before last. 3. I met my old classmate three days ago. 4. I will move to Texas the year after next. 5. I booked the high-speed rail ticket for the week after next. My translations (the book prints no key):",
             examples=[D(z, e) for z, e in TWA1]),
        card("Grammar Activity 2 (Speaking and Listening)",
             "Pair up. Each partner uses a timeline (Student A’s and Student B’s, printed as blank diagrams) to indicate special events they did, are doing or will do at certain times. Describe the timeline to your partner using the two sets of modifiers without showing it; the partner listens and recreates the timeline with the specific events. (A diagram, not included.)"),
    ],
    exercises=[
        M("What is 前年?", "The year before last", ["Last year", "Next year", "This year"], "前年."),
        M("What is 后天?", "The day after tomorrow", ["The day before yesterday", "Tomorrow", "Yesterday"], "后天."),
        M("What is 去年?", "Last year", ["The year before last", "Next year", "This year"], "去年 (the exception)."),
        M("What is 昨天?", "Yesterday", ["The day before yesterday", "Today", "Tomorrow"], "昨天 (the exception)."),
        M("Which is wrong?", "一个天", ["三天", "昨天", "后天"], "天 and 年 cannot take 个."),
        M("What is 下下个星期?", "The week after next", ["Next week", "Last week", "This week"], "下下(个)星期."),
        M("What is the difference between 一个月 and 一月?", "A month versus January", ["January versus a month", "No difference", "A week versus a year"], "一个月 / 一月."),
        M("Which sentence means “the fifth of next month”?", "下个月五号", ["下月个五号", "个下月五号", "月下五号个"], "下个月五号."),
        F("明___他的孩子就要上大学了！", "年", PART, "明年: next year."),
        F("前___他去邮局开了个邮箱。", "天", PART, "前天: the day before yesterday."),
    ],
)

# ------------------------------------------------------------------ 4. 亲自
QZ = [("你得亲自去办理护照。", "1. You have to go in person to get your passport."), ("要想知道一个地方好不好，最好亲自去那儿住几个月。", "2. If you want to know whether a place is good, it’s best to go and live there yourself for a few months."), ("你得自己去办理护照。", "3. You have to go and get your passport yourself. (自己 may also mean “alone”, so it is ambiguous)"), ("你得一个人去办理护照。", "4. You have to go and get your passport alone. (一个人 avoids the ambiguity)"), ("校长亲自打电话祝贺那个学生。", "5. The principal personally phoned to congratulate that student. (implies the principal does not usually need to)")]
QZ3 = [("太太：这个长周末你陪我去韩国旅行吧。先生：这个周末恐怕不行。下个星期一上海有一个很重要的会，我得亲自去参加。", "Wife: Come with me to Korea this long weekend. Husband: I’m afraid I can’t this weekend. There is a very important meeting in Shanghai next Monday, and I have to attend in person. (亲自; key mine)"), ("太太：哎呀，我已经买好飞机票了。先生：那你自己去吧。", "Wife: Oh dear, I’ve already bought the plane ticket. Husband: Then go by yourself. (自己)"),
       ("太太：一个人去没意思，而且要是我想照相都找不到人帮我照。先生：你跟你的朋友去怎么样？", "Wife: Going alone is no fun, and if I want a photo I can’t find anyone to take it. Husband: How about going with your friends? (一个人)"), ("太太：我的朋友也要跟自己的先生去旅行呢！先生：我听说韩国没有什么好玩的，你还是别去了！等以后我有空了，咱们一起去法国旅行。", "Wife: My friends are also going on trips with their own husbands! Husband: I hear there’s nothing fun in Korea; you’d better not go! When I have time later, let’s go to France together. (自己)"),
       ("太太：你又没有亲自去过，怎么知道韩国不好玩？我看你就是不想陪我去！先生：好，好，我陪你去。不过到了韩国，你自己去逛街买东西，我得在旅馆里准备下个星期的会。", "Wife: You haven’t even been there yourself; how do you know Korea isn’t fun? I think you just don’t want to go with me! Husband: OK, OK, I’ll go with you. But when we get to Korea you go shopping by yourself; I have to prepare for next week’s meeting in the hotel. (亲自; 自己)")]
QZ4 = [("你自己一个人的时候喜欢做什么？", "1. What do you like to do when you are by yourself?"), ("你做什么事的时候，不喜欢自己一个人？", "2. What do you not like to do by yourself?"), ("在美国哪些事得自己亲自去办？", "3. In the U.S., which things do you have to go and do in person?"), ("别人亲自为你做了一件什么事，让你很吃惊或是很感动？", "4. What did someone do for you in person that surprised or moved you? (the book glosses 吃惊 as chījīng, surprised, and 感动 as gǎndòng, moved)")]
L4 = lesson(
    "Lesson 20 Presentation 1 grammar: 亲自, 自己 and 一个人",
    "亲自 = in person · 自己 or 一个人 = by oneself",
    requires=[],
    cards=[
        card("The use of 亲自",
             "亲自 is used to indicate “do something in person”. In this instance 亲自 and 自己 can be used interchangeably, but 你得自己去办理护照 is ambiguous, since it can also mean “you have to go by yourself (no one will accompany you)”. 你得一个人去办理护照 avoids the ambiguity. 亲自 is also used to indicate that someone does something in person although they do not need to: 校长亲自打电话祝贺那个学生 implies that a principal usually does not or need not call a student in person to congratulate him. Examples:",
             examples=[D(z, e) for z, e in QZ]),
        card("Grammar Activity 3 (Reading and Speaking)",
             "A. Read the dialogue and complete the sentences using 自己, 一个人 or 亲自. B. Pair up and check your answers. The book leaves the blanks to the student and prints no key; my completed dialogue:",
             examples=[D(z, e) for z, e in QZ3]),
        card("Grammar Activity 4 (Reading, Speaking and Listening)",
             "A. Pair up and familiarize yourselves with the following questions; walk around and interview your classmates. B. The whole class shares their findings in Chinese.",
             examples=[D(z, e) for z, e in QZ4]),
    ],
    exercises=[
        M("What does 亲自 mean?", "In person", ["Alone", "Quickly", "Together"], "亲自: personally."),
        M("Which phrase avoids the ambiguity of “by yourself, alone”?", "一个人", ["亲自", "自己", "大家"], "一个人."),
        M("Which sentence implies the principal didn’t need to call?", "校长亲自打电话祝贺那个学生", ["校长打电话", "校长自己的学生", "学生亲自祝贺校长"], "亲自 for something one need not do."),
        M("Complete: 下个星期一上海有一个很重要的会，我得___去参加。", "亲自", ["一个人", "自己人", "大家"], "亲自."),
        M("Complete: 你又没有___去过，怎么知道韩国不好玩？", "亲自", ["一起", "一个", "自由"], "亲自."),
        M("Complete: ___去没意思，而且要是我想照相都找不到人帮我照。", "一个人", ["亲自", "大家", "全家"], "一个人: alone."),
        M("What does the wife say about her friends?", "They are going on trips with their own husbands", ["They live in Korea", "They don’t travel", "They are busy"], "我的朋友也要跟自己的先生去旅行."),
        M("What will the husband do in the Korean hotel?", "Prepare for next week’s meeting", ["Go shopping", "Sleep", "Phone his boss"], "我得在旅馆里准备下个星期的会."),
        F("要想知道一个地方好不好，最好亲___去那儿住几个月。", "自", PART, "亲自."),
        F("你得___己去办理护照。", "自", PART, "自己."),
    ],
)

# ------------------------------------------------------------------ 5. 恐怕 大概 也许
KP = [("现在去邮局的人恐怕不太多了吧？", "1. I’m afraid not many people go to the post office now, do they?"), ("他坐五点发车的高铁，大概晚上八点才会到。", "2. He is taking the five o’clock high-speed train and will probably not arrive until eight in the evening. (the book writes 5 as a digit)"), ("明天我有期中考试，恐怕去不了明天的聚会。", "3. I have a midterm exam tomorrow, so I’m afraid I can’t go to tomorrow’s party."), ("他明天也许来，也许不来。", "4. He may come tomorrow or he may not.")]
KP5 = [("水族馆离渔人码头不太远，走路大概只要十到十五分钟。", "1. The aquarium is not far from Fisherman’s Wharf; walking probably takes only 10 to 15 minutes. (key mine; the book writes 10-15 as digits)"), ("天这么黑，恐怕快要下雨了。", "2. The sky is so dark; I’m afraid it’s about to rain. (恐怕 or 也许)"), ("这个周末要是天气好，也许我会去海边烤肉踢球好好放松一下。", "3. If the weather is good this weekend, maybe I’ll go to the beach to barbecue and play ball and relax. (也许)"),
       ("这个单元我没有花太多时间准备生词，这次的单元考试恐怕会考不好。", "4. I didn’t spend much time preparing the vocabulary for this unit, so I’m afraid I’ll do badly on this unit test. (恐怕)"), ("我已经等了二十分钟的公共汽车了。我想我也许错过了这班车。", "5. I have already waited twenty minutes for the bus. I think maybe I missed it. (也许 or 恐怕; the book writes 20 as a digit)"), ("这个月等我发工资，也许请你去吃中国饭。", "6. When I get paid this month, maybe I’ll treat you to Chinese food. (也许)")]
CMP = table(["", "大概", "恐怕", "也许"], [["Meaning", "probably, approximately", "I am afraid…", "perhaps, maybe"], ["Judgment", "objective (based on known information)", "objective (based on known information)", "subjective (a pure guess)"], ["Affirmation", "stronger", "less strong; worry and anxiety", "indefinite (not sure)"], ["What can follow", "a number", "a grim or negative prediction", "a positive or a negative prediction"]],
            title="恐怕, 大概 and 也许 compared (the book’s explanation, put in a table)")
L5 = lesson(
    "Lesson 20 Presentation 1 grammar: 恐怕, 大概 and 也许",
    "I am afraid · probably · perhaps",
    requires=[],
    cards=[
        card("恐怕, 大概 & 也许",
             "The adverb 恐怕 indicates inference and estimation. It is similar to 大概 and 也许 in meaning and is often used to soften the tone of the sentence; there are subtle differences. For inference or estimation, 大概 and 恐怕 require a more objective judgment, using the known information to predict a possible outcome. 大概 expresses stronger affirmation than 恐怕. 恐怕 also carries the meaning of “worry” and “anxiety”, so it usually leads to a more negative prediction. Compared with them, 也许 indicates a more subjective estimation and strongly expresses indefiniteness rather than affirmation; 也许 can be followed by either a positive or a negative prediction.",
             tables=[CMP], examples=[D(z, e) for z, e in KP]),
        card("Grammar Activity 5 (Reading and Speaking)",
             "A. Read and complete the sentences using 大概, 也许 or 恐怕. B. Pair up and check your answers by reading the sentences aloud and translating them. The book prints no key; my completed sentences:",
             examples=[D(z, e) for z, e in KP5]),
        card("Grammar Activity 6 (Listening and Speaking)",
             "Listen to the dialog and answer: 1. What is the male speaker’s plan? 2. What is the concern? 3. What is the alternative plan? 4. What does the female speaker think of his plans? (Audio, not included; the book prints no script.)"),
    ],
    exercises=[
        M("Which of the three is a pure guess?", "也许", ["大概", "恐怕", "Both 大概 and 恐怕"], "也许 is subjective."),
        M("Which usually leads to a negative prediction?", "恐怕", ["大概", "也许", "None"], "恐怕: I am afraid…"),
        M("Which can be followed by a number?", "大概", ["恐怕", "也许", "None"], "大概: approximately."),
        M("What does “他明天也许来，也许不来” mean?", "He may come tomorrow or he may not", ["He will certainly come", "He certainly won’t come", "He came yesterday"], "也许."),
        M("What does “明天我有期中考试，恐怕去不了明天的聚会” mean?", "I’m afraid I can’t go to the party", ["I will go to the party", "I might skip the exam", "The party is cancelled"], "恐怕 + negative."),
        M("What does “他坐五点发车的高铁，大概晚上八点才会到” mean?", "He will probably arrive at eight in the evening", ["He arrived at eight", "He won’t come", "He takes a plane"], "大概."),
        M("Which fits “这次的单元考试___会考不好”?", "恐怕", ["也许是", "大概能", "一定"], "恐怕 for a worry."),
        M("Which fits “走路___只要十到十五分钟”?", "大概", ["恐怕", "可惜", "最好"], "大概 with a number."),
        F("现在去邮局的人___怕不太多了吧？", "恐", PART, "恐怕: I’m afraid."),
        F("他明天也___来，也许不来。", "许", PART, "也许: maybe."),
    ],
)

# ------------------------------------------------------------------ 6. 不仅…而且
BJ = [("邮局不仅能寄信、寄包裹，而且还卖信封和邮票。", "1. The post office can not only send letters and parcels, but also sells envelopes and stamps."), ("高铁不仅速度快，而且坐起来也很舒服。", "2. The high-speed rail is not only fast, but also comfortable to ride."), ("他不仅喜欢吃中国菜，而且也会做几道中国菜。", "3. He not only likes eating Chinese food, but can also cook a few Chinese dishes."), ("小李不只会说流利的中文，他的中文歌也唱得很不错。", "4. Xiao Li can not only speak fluent Chinese; he sings Chinese songs quite well too."), ("不仅中国人用筷子，日本人、韩国人也用筷子。", "5. Not only Chinese use chopsticks; Japanese and Koreans use chopsticks too.")]
BJ7 = [("你常上网做些什么？", "1. What do you often do online?"), ("你周末常去 Del Monte 购物中心做些什么？", "2. What do you often do at the Del Monte shopping center on weekends? (the book prints Del Monte in Latin letters)"), ("蒙特雷的健身中心或国防语言学院的体育馆怎么样？", "3. What are Monterey’s fitness centers or the Defense Language Institute’s gym like?"), ("骑自行车游览蒙特雷怎么样？", "4. How is touring Monterey by bicycle?"), ("你为什么这么喜欢爬山、露营、滑雪或你的爱好？", "5. Why do you like hiking, camping, skiing or your hobby so much?")]
L6 = lesson(
    "Lesson 20 Presentation 1 grammar: 不仅…而且…",
    "不但/不仅/不只 … 而且/还/也 · not only … but also",
    requires=[],
    cards=[
        card("The 不仅…而且 construction",
             "In the previous lesson you learned 不但…而且 to express “not only … but also”. 不但 can be a substitute for 不仅 or 不只, all of which mean “not only” and can be followed by 而且, 还 or 也 to indicate a progressive relationship. Pattern: Subject + 不但/不仅/不只 …, 而且/还/也 …; or 不但/不仅/不只 + Subject 1 + …, 而且 Subject 2 + 还/也. Examples:",
             examples=[D(z, e) for z, e in BJ]),
        card("Grammar Activity 7 (Reading, Listening and Speaking)",
             "Pair up. Student A asks the question and Student B answers it using the 不仅…而且 pattern. Switch roles and repeat. The five questions:",
             examples=[D(z.replace("Del Monte", "德尔蒙特"), e) for z, e in BJ7]),
    ],
    exercises=[
        M("Which words can replace 不仅?", "不但 and 不只", ["因为 and 所以", "虽然 and 但是", "如果 and 就"], "不但/不仅/不只."),
        M("Which words can follow the first clause?", "而且, 还 and 也", ["所以", "但是", "因此"], "而且/还/也."),
        M("What does “高铁不仅速度快，而且坐起来也很舒服” mean?", "The high-speed rail is not only fast but also comfortable", ["It is fast but uncomfortable", "It is slow but comfortable", "It is cheap and slow"], "不仅…而且…."),
        M("What does “小李不只会说流利的中文，他的中文歌也唱得很不错” mean?", "Xiao Li speaks fluent Chinese and also sings Chinese songs well", ["Xiao Li can’t sing", "Xiao Li can’t speak Chinese", "Xiao Li hates songs"], "不只…也…."),
        M("What does “不仅中国人用筷子，日本人、韩国人也用筷子” mean?", "Not only Chinese use chopsticks; Japanese and Koreans do too", ["Only Chinese use chopsticks", "Nobody uses chopsticks", "Only Koreans use them"], "Subject 1 … Subject 2 也…."),
        M("Complete: 邮局不仅能寄信、寄包裹，___还卖信封和邮票。", "而且", ["所以", "但是", "因为"], "不仅…而且…."),
        M("Which is NOT a way to say “not only”?", "既然", ["不但", "不仅", "不只"], "既然 means “since”."),
        M("Which sentence is correct?", "他不仅会说中文，而且会写汉字", ["他不仅会说中文，所以会写汉字", "他会说中文不仅，而且会写汉字", "他不仅会说中文，但是不会写汉字"], "不仅…而且…."),
        F("他不仅喜欢吃中国菜，___且也会做几道中国菜。", "而", PART, "而且: and also."),
        F("小李不___会说流利的中文，他的中文歌也唱得很不错。", "只", PART, "不只: not only."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration 3-4
JENNY = [("你好，", "Hello,"), ("我来台湾师大学习已经两个星期了，开始慢慢习惯这里的生活。我想给你寄一个包裹，可是我学习很忙，一直找不到时间去邮局寄。后来我的朋友告诉我，快递公司比邮局更方便。我只要用手机在网上和快递公司预约付款，他们会亲自上门来取我的包裹，不用贴邮票，不需要填很多表。因为我每天都要上课，没时间在宿舍等他们上门，所以他们让我把包裹拿到宿舍附近的便利商店，他们会去那里取。昨天我已经寄出你的包裹了。你大概一个星期以后会收到，希望你会喜欢。你最近的生活怎么样？有空给我回信。这里的快递服务很方便，要是你还需要什么，就马上告诉我。", "I have been studying at Taiwan Normal University for two weeks and am slowly getting used to life here. I wanted to send you a parcel, but I am so busy with study that I could never find time to go to the post office. Later my friend told me that express companies are more convenient than the post office. I only need to use my phone to make an appointment and pay online with the express company, and they will come to my door in person to collect my parcel; no stamps to stick, not many forms to fill. Because I have class every day and have no time to wait in the dorm for them, they let me take the parcel to a convenience store near the dorm, where they will pick it up. Yesterday I already sent your parcel. You will probably receive it in about a week; I hope you like it. How is your life lately? Write back when you have time. The express service here is very convenient; if you need anything else, tell me right away."),
         ("祝好！你的朋友，珍妮。二零二零年六月五号", "Best wishes! Your friend, Jenny. June 5, 2020. (the book writes the date in digits)")]
PA1 = "我是一个快递投递员，虽然工作时间自由，但是工作真不轻松。我的工作最重要的是用最快的速度把客人的东西安全地送到。平时还好，但是要是外面刮风、下雨就会特别辛苦。另外，过年、过节是我最忙的时候，因为要送的东西特别多，常常得加班。有时自己的东西送完了，还得帮忙别的同事送，真是忙极了！不过，做这个工作也很有意思。我几乎什么东西都送过，像是行李、高尔夫球具、鲜花、水果和各地美食等。这个工作也让我更了解自己住的这个城市。每天出门送东西前，我都会先查一下那一天的路线，以前总会有几条我从来没走过的路。走过几次以后，现在不管去哪儿，我几乎都不用地图了。"
PA1_E = "I am an express delivery worker. Although my working hours are flexible, the work is really not easy. The most important thing in my job is to deliver customers’ things safely at the fastest speed. On ordinary days it’s fine, but when it’s windy or rainy outside it is especially hard. In addition, the New Year and holidays are my busiest time, because there is especially a lot to deliver and I often have to work overtime. Sometimes when I have finished my own deliveries I still have to help colleagues deliver theirs; I am so busy! Still, this job is also interesting. I have delivered almost everything, such as luggage, golf clubs, fresh flowers, fruit and local delicacies. This job has also made me understand the city I live in better. Every day before going out to deliver I check that day’s route first; there were always a few roads I had never walked. After walking them a few times, now wherever I go I hardly need a map. (the underlined sentence about 了解 is 这个工作也让我更了解自己住的这个城市; mine: 了解 means to understand or get to know)"
PA2 = "我是一个邮局的营业员，在邮局已经工作了二十几年了。再过几年就可以退休了。进邮局以前，我以为邮局的工作很简单，就是卖卖邮票、信封、帮客人寄寄信，寄寄包裹什么的。进了邮局才知道邮局的业务比我想的要多得多，不是只有一般的邮政业务。那时候白天要上班，晚上还要去培训，学习其他的业务。通过培训，我学会了怎么帮客人开户、存款、汇款和转账等银行业务。后来做了这些业务，我才知道原来这些银行业务才是邮局业务的主要部分，而且很多人来邮局都是为了办这些事。最近我开始帮客人办保险。我觉得这个工作是这些工作中最难的，因为除了得知道每种保险的不同以外，我还得知道每种保险需要填的表，还要能回答客人的问题。工作了二十几年，还在学习。真是活到老学到老啊！"
PA2_E = "I am a post office clerk and have worked at the post office for more than twenty years. In a few more years I can retire. Before joining the post office I thought the work there was very simple, just selling stamps and envelopes, helping customers mail letters and parcels and so on. After joining I found that the post office’s business was much more than I thought, not only the ordinary postal business. In those days I worked in the daytime and went to training in the evenings to learn other business. Through the training I learned how to help customers open accounts, deposit, remit and transfer money and other banking business. Later, after doing this business, I found that these banking services were in fact the main part of the post office’s business, and many people come to the post office to handle these things. Recently I started helping customers with insurance. I think this job is the hardest of all, because besides having to know the differences between each insurance, I also have to know the forms to fill for each and be able to answer customers’ questions. Twenty-some years of work and still learning. Truly one is never too old to learn! (the last sentence is the proverb 活到老学到老)"
L7 = lesson(
    "Lesson 20 Presentation 1 skill integration: Jenny’s email and two postal workers",
    "台湾的快递 · 快递投递员 · 邮局营业员 · 活到老学到老",
    requires=[],
    cards=[
        card("Skill Integration Activities 1 and 2 (Listening and Speaking)",
             "Activity 1 (Listening, Speaking and Reading): A. Listen and answer six questions: 1. What advice is given? Why? 2. What is said to be safer to do? 3. What is reported about the post office? 4. What suggestion is given? 5. What trend is described? 6. How did Li Guohao find his job? B. Pair up, share your answers in Chinese and read the script aloud. Activity 2 (Listening and Speaking): A. Listen to a conversation between an American student and a post office clerk (new vocabulary: 邮箱, yóuxiāng, P.O. box) and answer: 1. Why is John going to the post office? 2. What is John asked to do by the clerk? 3. What information is John not aware of? (at least two details) 4. What will John do tomorrow? B. Pair up and share your answers in Chinese. (Audio, not included; the book prints no script.)"),
        card("Skill Integration Activity 3 (Reading, Speaking, Listening and Writing): Jenny’s email",
             "A. Read the email sent from your classmate Jenny in Taiwan (TO: XXX (your name); CC; Subject) and answer: 1. Why did Jenny write the letter? 2. What did Jenny say about her school life? 3. What did Jenny learn about the courier service in Taiwan? 4. Where did Jenny mail her item? Why? B. Pair up and take turns retelling the story in Chinese. C. As her friend, write an email back to Jenny (TO: 珍妮; Subject: 你的回信). The email:",
             examples=[D(z, e) for z, e in JENNY]),
        card("Skill Integration Activity 4 (Reading, Speaking and Listening): two passages",
             "A. Pair up; each student reads one of the two passages and answers the questions. B. Each student then orally summarizes the passage they read to their partner; then each reads the other passage, answers the questions and compares answers. Passage 1 questions: 1. Who is the narrator? 2. How does he feel about his job? 3. What is the most important part of his job? 4. List at least three details about his job experience. 5. Based on the context, guess the meaning of 了解 in the underlined sentence. Passage 2 questions: 1. Who is the narrator? 2. How does she feel about her job after working in the post office? 3. What has she found challenging at work? Provide at least three examples. 4. What does the last sentence mean? The two passages:",
             examples=[D(PA1, PA1_E), D(PA2, PA2_E)]),
    ],
    exercises=[
        M("Where is Jenny studying?", "At Taiwan Normal University", ["In Beijing", "In Shanghai", "In Hong Kong"], "我来台湾师大学习已经两个星期了."),
        M("Why couldn’t Jenny go to the post office?", "She was too busy with study", ["It was closed", "It was too far", "She lost the parcel"], "我学习很忙，一直找不到时间去邮局寄."),
        M("What does the express company do?", "They come to the door to collect, with no stamps or many forms", ["They only sell stamps", "They give free gifts", "They open at night"], "他们会亲自上门来取我的包裹，不用贴邮票."),
        M("Where did Jenny take the parcel?", "A convenience store near the dorm", ["The post office", "The airport", "The bank"], "宿舍附近的便利商店."),
        M("How soon will the friend receive it?", "In about a week", ["Tomorrow", "In a month", "In a year"], "你大概一个星期以后会收到."),
        M("What is the delivery worker’s most important task?", "To deliver things safely at the fastest speed", ["To sell stamps", "To wait at home", "To drive a bus"], "用最快的速度把客人的东西安全地送到."),
        M("When is the delivery worker busiest?", "At the New Year and holidays", ["In summer", "On weekends only", "At night"], "过年、过节是我最忙的时候."),
        M("What does 了解 mean in the delivery worker’s passage?", "To understand; to get to know", ["To finish", "To leave", "To clean"], "更了解自己住的这个城市."),
        M("How long has the post office clerk worked there?", "More than twenty years", ["About two years", "Ten years", "Fifty years"], "已经工作了二十几年了."),
        M("What did the clerk learn through training?", "Banking: opening accounts, deposits, remittances and transfers", ["How to deliver", "How to drive", "How to cook"], "开户、存款、汇款和转账."),
        M("What does the clerk find hardest?", "Handling insurance", ["Selling stamps", "Delivering parcels", "Cleaning"], "办保险…最难的."),
        F("我是一个快递投___员，虽然工作时间自由，但是工作真不轻松。", "递", PART, "投递员: delivery worker."),
        F("真是活到老学到___啊！", "老", PART, "活到老学到老."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
CAT = table(["服务", "说明 (the book’s table from the 黑猫宅急便 website; the Latin parts are left out)"],
            [["一般常温宅急便", "一般用品"], ["低温宅急便", "生鲜食品"], ["平价宅急便", "网购、文件、小包"], ["当日宅急便", "需快速送达的商品"], ["行李寄送", "高尔夫球，饭店行李"], ["到付宅急便", "收件人收费"], ["网路宅急便", "网路预约寄件"]],
            title="服务介绍 (Taiwan’s 黑猫宅急便; 宅急便 zháijíbiàn, delivery service: 宅 home, 急 hurry, 便 convenient)", say=[0, 1])
FAQ = [("我要寄快递，怎么寄呢？", "Q1. I want to send an express parcel; how do I send it?"), ("您可以到我们的代收店，像是各地的七一一便利商店，或是我们各地的营业点寄件，您也可以直接打电话到客服专线四一二，八八八八，或网络客服和我们联系。另外，我们也提供网络预约和手机应用程序预约的服务。只要是一个星期内的寄件，服务人员会在您选择的收件日去您家收件。", "A1. You can go to our agent stores, such as 7-11 convenience stores everywhere, or to our business points to send; you can also call the customer service line 412-8888 directly or contact us through online customer service. In addition we offer online and mobile app booking. For any item sent within one week, service staff will come to your home on the pick-up day you choose. (the book prints this in mixed traditional and simplified characters, writes 7-11 and the number in digits, and “app” in Latin letters)"),
       ("我白天都不在家，要怎么样才能收到包裹呢？", "Q2. I’m never home during the day; how can I receive the parcel?"), ("我们的配送最晚到晚上六点，您可以请寄件人在寄件时勾选十四时到十八时的时间，或者您可以请家人或是大楼管理员代收。此外，如果收件地址填写您上班的地方，我们也一样都会帮您配送喔。", "A2. Our delivery runs until six in the evening at the latest; you can ask the sender to tick the 14:00–18:00 slot when sending, or you can have family or the building manager receive it for you. Also, if you put your workplace as the delivery address, we will deliver there just the same."),
       ("我可以寄到邮政信箱吗？", "Q3. Can I send to a P.O. box?"), ("很抱歉，由于包裹寄到邮政信箱后没有人可以签收，所以我们不能提供这个服务。另外，如军营、军校等地址我们也无法托运。", "A3. Sorry, because nobody can sign for a parcel sent to a P.O. box, we cannot provide this service. Also we cannot ship to addresses such as military camps and military schools."),
       ("什么东西你们不能寄送？", "Q4. What can’t you send?"), ("现金、动物、超大件家具、电视、冰箱、自行车、护照等，我们不能帮您运送。", "A4. Cash, animals, oversized furniture, televisions, refrigerators, bicycles, passports and so on we cannot ship for you."),
       ("你们提供先把行李寄到机场，出国时再提领的服务吗？", "Q5. Do you offer a service of sending luggage to the airport first and picking it up when going abroad?"), ("我们现在不提供这样的服务。", "A5. We do not offer such a service now."),
       ("你们的运费可不可以请收件人给付？", "Q6. Can the freight be paid by the recipient?"), ("可以，您的运费可以让收件人付。包裹送到时，我们的工作人员会向收件人收取运费。", "A6. Yes, your freight can be paid by the recipient. When the parcel is delivered, our staff will collect the freight from the recipient.")]
DD = table(["Do (mine)", "Don’t (mine)"], [["可以到代收店、营业点寄件，或打电话、上网、用手机预约；可以让家人或大楼管理员代收；可以让收件人付运费；寄件时选好收件时间", "不要寄到邮政信箱；不要寄现金、动物、超大件家具、电视、冰箱、自行车、护照；不要寄到军营、军校；不能先把行李寄到机场"]],
          title="Using Chinese in Context Activity 2 B: the Do and Don’t list (blank in the book; my fill from the six FAQs)", say=[0, 1])
L8 = lesson(
    "Lesson 20 Presentation 1 using Chinese in context: express services in Taiwan and China",
    "黑猫宅急便 · 常见问题 · 注意事项 · EMS 和顺丰申通",
    requires=[],
    cards=[
        card("Using Chinese in Context Activity 1 (Reading, Speaking and Listening)",
             "New vocabulary: 宅急便 (zháijíbiàn, delivery service; 宅 home, 急 hurry, 便 convenient), a term used often in Taiwan. A. Read the table from the popular express service 黑猫宅急便 website in Taiwan (the web address is not given here) and determine what services the company provides. B. Pair up and discuss your findings; then generate five questions to ask customer service. C. Call the customer service representative and get more details about their service; your partner plays the representative; then switch roles.",
             tables=[CAT]),
        card("Using Chinese in Context Activity 2 (Reading, Speaking and Listening): the FAQ",
             "Read the following FAQ from an express service and help create a Do’s and Don’ts list for customers. A. Form groups of three. Each member picks two of the six FAQs, reads them and takes notes. B. Each member reports what they read, gathers the remaining information from the group and writes up a Do’s and Don’ts list for customers; post your work on Linoit. C. The entire class votes for the best list. The six questions and answers:",
             examples=[D(z, e) for z, e in FAQ], tables=[DD]),
        card("Using Chinese in Context Activities 3 and 4",
             "Activity 3 (Reading, Speaking and Listening): You are studying Chinese at Beijing University and would like to send a Chinese New Year present through EMS to your friend, who now lives in Shanghai. A. At the post office you are asked to fill out an EMS form; figure out what information needs to be provided and fill out the form in Chinese (a photograph of an EMS form, not included). B. Go to a counter in the post office and mail the package to your friend; a classmate plays the postal clerk. Activity 4 (Reading, Speaking and Listening): You are doing an internship at a U.S. company in Shanghai. Your company often needs to mail products domestically and internationally; to reduce costs while still ensuring parcels are delivered as quickly as possible, your manager wants your team to research the two biggest express services in China, 顺丰 and 申通, and compare their rates, services, delivery times and user friendliness. Prepare a PPT report for your manager and give an oral report. A. Form groups of three; use the two companies’ websites (links not included; 顺丰: 我要寄件, 运费时效查询, 快递服务; 申通: 运费查询, 产品服务). B. Discuss your findings and decide what to include in your slides. C. Deliver an oral report using your presentation. D. The entire class votes on which delivery company to recommend."),
    ],
    exercises=[
        M("What does 宅急便 mean?", "Delivery service", ["A hotel", "A fast train", "A taxi"], "宅急便: delivery service."),
        M("Which 宅急便 is for fresh food?", "低温宅急便", ["一般常温宅急便", "平价宅急便", "到付宅急便"], "低温宅急便: 生鲜食品."),
        M("Which is for items that must arrive quickly the same day?", "当日宅急便", ["平价宅急便", "行李寄送", "到付宅急便"], "当日宅急便."),
        M("What is 到付宅急便?", "The recipient pays", ["The sender pays double", "Free delivery", "Delivery at night"], "到付宅急便: 收件人收费."),
        M("What is the latest delivery time in FAQ 2?", "Six in the evening", ["Noon", "Midnight", "Nine in the evening"], "我们的配送最晚到晚上六点."),
        M("Why can’t they send to a P.O. box?", "Nobody can sign for the parcel", ["It is too small", "It costs too much", "It is illegal"], "没有人可以签收."),
        M("Which of these can’t they send?", "Cash", ["Books", "Clothes", "Shoes"], "现金…不能帮您运送."),
        M("Can the recipient pay the freight?", "Yes", ["No", "Only on weekends", "Only abroad"], "可以，您的运费可以让收件人付."),
        M("Can they send luggage to the airport to be picked up when leaving the country?", "No, they do not offer that service", ["Yes, for free", "Yes, for a fee", "Only for soldiers"], "我们现在不提供这样的服务."),
        F("我们的配送最晚到晚___六点。", "上", PART, "晚上: evening."),
        F("您的运费可以让收件人___。", "付", PART, "付: pay."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 20 Presentation 1 vocabulary", "31 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English (保险 appears twice, as insurance and as safe).", VOC1)

UNIT = unit("第二十课 Presentation 1: 在邮局, 时间修饰语, 亲自, 恐怕/大概/也许, 不仅…而且", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
