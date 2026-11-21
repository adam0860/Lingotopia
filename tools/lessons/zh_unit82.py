"""Unit 82: Lesson 27 (New Careers), Presentation 1: the dialog about a security guard who becomes a courier with its activities, the rhetorical question 难道…吗,
the modal particle 的, 跟…似的, 正是因为, the skill-integration tasks (couriers in China, Song Xuewen, Dou Liguo), the using-Chinese tasks (international shipping, a courier company, a job posting)
and the vocabulary list. Audio, pictures, videos and websites are not included; numbers the book writes as digits are spelled out in Chinese text;
the e-mail address and telephone number in the advertisements are left out; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l27_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('还得再跑', 1, 'dei3'), ('还得再送', 1, 'dei3'), ('得到零差评', 0, 'de2'), ('行业', 0, 'hang2'), ('完成了无人', 2, 'le5'), ('成长为', 1, 'zhang3'), ('孩子，还给', 3, 'hai2')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 1 + activities 1-2
P1 = [("老李", "小张，好久没看到咱们小区保安小宋了。他去哪儿了？", "Lao Li: Xiao Zhang, I haven’t seen Xiao Song, our compound’s security guard, for a long time. Where has he gone? (translations in this card are mine)"),
      ("小张", "老李，难道你不知道他换工作了吗？他去做快递员了。", "Xiao Zhang: Lao Li, don’t you know he changed jobs? He has become a courier."),
      ("老李", "真的吗？当快递员可比保安辛苦多了，起早贪黑的。", "Lao Li: Really? Being a courier is much harder than being a guard, working from dawn to night."),
      ("小张", "可不是嘛。风里来雨里去，每天在路上要跑十多个小时。", "Xiao Zhang: You said it. Braving wind and rain, he runs more than ten hours on the road every day."),
      ("老李", "确实是，而且越到节假日他们就越忙。", "Lao Li: Indeed, and the closer to holidays the busier they get."),
      ("小张", "特别在“双十一”的时候，快递员的生活就跟打仗似的，每天要送好几百单，连喝水的时间都没有。", "Xiao Zhang: Especially at “Double Eleven”, a courier’s life is just like a battle; they have to deliver several hundred orders a day with not even time to drink water."),
      ("老李", "正是因为“快递小哥”的辛苦，我们的生活才变得方便多了。", "Lao Li: It is precisely because of the “courier guys’” hard work that our lives have become so much more convenient."),
      ("小张", "那当然。前两天，我要寄个包裹，一打电话，快递员就上门来收件，第二天包裹就寄到了，你说快不快。", "Xiao Zhang: Of course. A couple of days ago I wanted to send a parcel; as soon as I phoned, the courier came to the door to collect it, and the next day the parcel had arrived. Isn’t that fast?"),
      ("老李", "快递既快捷又便利，而且什么东西都可以送。", "Lao Li: Express delivery is both fast and convenient, and anything can be sent."),
      ("小张", "是啊。我太太常常在网上买菜买水果，每次下好单后，东西很快就送来了。", "Xiao Zhang: Yes. My wife often buys vegetables and fruit online, and every time after she places the order the things arrive very soon."),
      ("老李", "“快递小哥”真是我们生活的好帮手啊，可是有的人对快递员很不客气。", "Lao Li: The “courier guys” really are good helpers in our lives, but some people are very impolite to couriers."),
      ("小张", "对啊，我也听说有人因为送货晚了一会儿，就给快递员差评，而且还说一些难听的话。", "Xiao Zhang: Right, I have also heard that some people, because a delivery was a little late, give the courier a bad review and even say some unpleasant things."),
      ("老李", "这些人太不尊重“快递小哥”的劳动了。", "Lao Li: These people don’t respect the “courier guys’” labor at all."),
      ("小张", "下次看到小宋，我们要多鼓励他，希望他成为一个优秀的“快递小哥”。", "Xiao Zhang: Next time we see Xiao Song, let’s encourage him more and hope he becomes an excellent “courier guy”.")]
A1 = [("他们可能是邻居，住在同一个小区，老李问小张小区保安小宋去哪儿了。", "Activity 1A-1 (my answer): They are probably neighbors living in the same compound; Lao Li asks Xiao Zhang where the compound’s guard Xiao Song has gone."),
      ("他们在谈小宋换工作做快递员，快递员的辛苦，快递的方便，还有有的人对快递员不客气。", "1A-2 (my answer): They talk about Xiao Song changing jobs to become a courier, the hard work of couriers, the convenience of express delivery, and how some people are impolite to couriers."),
      ("小宋以前是小区的保安，现在是快递员。", "1B-1 (my answer): Xiao Song used to be the compound’s guard and is now a courier."),
      ("他起早贪黑，风里来雨里去，每天在路上跑十多个小时；越到节假日越忙，“双十一”每天要送好几百单。", "1B-2 (my answer, three details): He works from dawn to night, braving wind and rain, over ten hours on the road a day; the closer to holidays the busier, and at “Double Eleven” he delivers several hundred orders a day."),
      ("打个电话快递员就上门收件，第二天就寄到；什么东西都可以送，在网上买菜买水果很快就送来。", "1B-3 (my answer, two details): Phone and the courier comes to the door to collect, and it arrives the next day; anything can be sent, and vegetables and fruit bought online arrive soon."),
      ("因为送货晚了一会儿。", "1B-4 (my answer): Because a delivery was a little late."),
      ("他们会多鼓励他，希望他成为一个优秀的“快递小哥”。", "1B-5 (my answer): They would encourage him more and hope he becomes an excellent “courier guy”.")]
Q2 = [("王红的弟弟在哪儿工作？他的公司怎么样？", "Activity 2A-1: Where does Wang Hong’s younger brother work? How is his company?"), ("王红的弟弟每天都做什么？", "2A-2: What does Wang Hong’s younger brother do every day?"),
      ("在中国，对快递员来说，什么时候最忙？", "2A-3: In China, when is the busiest time for couriers?"), ("为什么说快递员让我们的生活变得更方便了？举个例子。", "2A-4: Why do we say couriers have made our lives more convenient? Give an example."),
      ("快递员小宋给老李送来他在网上买的健身器。", "2D-1 (true or false): Courier Xiao Song delivers to Lao Li the exercise machine he bought online."), ("小宋工作非常认真，到现在一个差评也没有。", "2D-2: Xiao Song works very conscientiously and so far has not had a single bad review."),
      ("小宋不管是收货还是送货都很认真。", "2D-3: Whether collecting or delivering, Xiao Song is very conscientious."), ("很多人不尊重快递员，常常给他们差评。", "2D-4: Many people don’t respect couriers and often give them bad reviews."),
      ("老李的女儿收到包裹后，老李忘了给小宋好评。", "2D-5: After Lao Li’s daughter received the parcel, Lao Li forgot to give Xiao Song a good review.")]
L1 = lesson(
    "Lesson 27 Presentation 1: a security guard becomes a courier",
    "快递员 · 保安小宋 · 起早贪黑 · 风里来雨里去 · 双十一 · 差评 · 快递小哥",
    requires=[],
    cards=[
        card("Learning objectives of Lesson 27 (New Careers, 新职业)",
             "Upon completion of this lesson, you should be able to: discuss a career as a courier in China, including one’s life and work; discuss the popularity of internet influencers in China, and their impact; discuss China’s e-sports industry and professional e-sports players. To perform the above you must master the new words and phrases in the Core Vocabulary section and these patterns: the rhetorical question 难道……吗; the modal particle 的 (表示附加原因，补充说明); the pattern 跟……似的; the usage of 正是因为……; the pattern 把……叫做……; the discourse function 前解释和后解释; 说到/想到/提到……; the function of 主要是因为……; the usage of 随着……; 认识到/了解到/打听到; the structure 当(职业)需要……(表示条件); the structure 有了……后，……."),
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. Are there any couriers in the U.S.? Can you name the courier companies? B. What are the work schedules for couriers in the U.S.? C. How often do you use courier services? How do you like the service? (One picture is not included.)"),
        card("Presentation 1: 快递小哥", "The dialog; the book also prints it in traditional characters.", examples=dlg(P1)),
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Global Listening: listen to Presentation 1 once through and answer the questions. 1. What is the relationship between Xiao Zhang and Lao Li? How do you know? 2. What are they talking about? B. Detailed Listening: listen again and answer: 1. Who is Xiao Song? What is his current occupation? 2. Provide three details about his job. 3. Provide two details about the convenience of courier services. 4. Why do some people give their couriers bad ratings? 5. What would Xiao Zhang and Lao Li say to Xiao Song if they saw him? C. Pair up and discuss the answers with your partner and share your answers with the class. (Audio; my answers from the text:)",
             examples=[D(z, e) for z, e in A1]),
        card("Activity 2 (Listening, Writing and Speaking)",
             "A. Listen to the first dialog and answer the questions below. B. Pair up and discuss the answers with your partner. C. Conduct a similar conversation with your partner. Talk about being a courier in the U.S. D. Listen to the second dialog and mark the statements as either True or False. E. Pair up and discuss your answers with your partner. Justify your decisions. F. Conduct a similar conversation with your partner. Talk about your own experiences using a courier service. (Both dialogs are audio and not in the book, so there is no key; the questions and statements are the book’s.)",
             examples=[D(z, e) for z, e in Q2]),
    ],
    exercises=[
        M("Who is Xiao Song?", "The compound’s former security guard, now a courier", ["A teacher", "A doctor", "A taxi driver"], "他换工作了…去做快递员了."),
        M("How long does a courier run on the road each day?", "More than ten hours", ["About two hours", "Exactly eight hours", "Less than an hour"], "每天在路上要跑十多个小时."),
        M("When are couriers even busier?", "On holidays", ["On Mondays", "In the middle of the night", "Never"], "越到节假日他们就越忙."),
        M("What is a courier’s life like at Double Eleven?", "Like a battle", ["Like a holiday", "Like a party", "Like a classroom"], "就跟打仗似的."),
        M("How many orders may a courier deliver a day then?", "Several hundred", ["Five", "Twenty", "Two"], "每天要送好几百单."),
        M("What does the convenience of express delivery include?", "It is fast and convenient and anything can be sent", ["It is cheap and slow", "It is free", "It only sends letters"], "既快捷又便利，而且什么东西都可以送."),
        M("Why do some people give couriers bad reviews?", "A delivery was a little late", ["The courier was rich", "The courier was too fast", "The parcel was free"], "因为送货晚了一会儿."),
        M("What do Xiao Zhang and Lao Li want to do next time they see Xiao Song?", "Encourage him", ["Complain to him", "Pay him", "Ignore him"], "我们要多鼓励他."),
        M("What does 可不是嘛 express?", "Agreement", ["Disagreement", "A question", "A refusal"], "可不是嘛."),
        F("当快递员可比保安辛___多了，起早贪黑的。", "苦", PART, "辛苦: hard."),
        F("这些人太不尊___“快递小哥”的劳动了。", "重", PART, "尊重: respect."),
    ],
)

# ------------------------------------------------------------------ 2. activities 3-5
WB = table(["Word", "My related words", "Part of speech and meaning (mine)"],
           [["保安", "保护, 安全, 安静", "example from the book: n., security guard"], ["快递", "快乐, 快速, 传递", "n./v., express delivery"], ["送单", "送货, 送礼, 简单", "v.o., deliver an order"], ["收件", "收到, 收入, 邮件", "v.o., collect a parcel"], ["难听", "困难, 难过, 听力", "adj., unpleasant to hear"], ["帮手", "帮助, 帮忙, 手机", "n., helper"], ["客气", "客人, 顾客, 天气", "adj., polite"]],
           title="Activity 3A: words sharing a character with the given words (the book’s blanks; my words)", say=[0, 1])
CZ = ("十一月十一日是快递行业最忙的一天，因为在双十一这天很多人在网上购物。为了能按时把货送给顾客，快递员常常要起早贪黑，早上五点就开始工作，晚上九点才能回家。这一天的生活就跟打仗似的，连吃饭，喝水的时间都没有。虽然他们这天非常忙，在路上要跑十多个小时，风里来雨里去，但是看到顾客收到在网上买的东西后，笑得很开心的样子，快递员们就不觉得辛苦了。正是因为有了“快递小哥”的服务，中国的快递既快捷又便利，有时候顾客早上在网上下单，下午快递员就把货送到了。快递使我们的生活变得越来越方便。",
      "November 11th is the busiest day of the courier industry, because on this day many people shop online. To deliver goods to customers on time, couriers often have to work from dawn to night, starting work at five in the morning and getting home only at nine at night. Life on this day is just like a battle, with not even time to eat and drink. Although they are very busy that day, running more than ten hours on the road, braving wind and rain, when they see customers happy to receive what they bought online, the couriers don’t feel tired any more. It is precisely because of the “courier guys’” service that China’s express delivery is both fast and convenient; sometimes a customer places an order online in the morning and the courier has delivered the goods by the afternoon. Express delivery makes our lives more and more convenient. (my key: 双十一, 起早贪黑, 打仗, 跑, 风里来雨里去, 辛苦, 快捷, 便利, 下单; the book writes 11 月 11 日 in digits)")
US5 = [("在美国，快递员也很忙，特别是圣诞节前。", "Activity 5 (my sample sentences about U.S. couriers): In America couriers are also very busy, especially before Christmas."), ("难道美国的快递员不辛苦吗？", "Isn’t the work of U.S. couriers hard?"), ("有的人对快递员不客气，还说一些难听的话，这是不尊重他们的劳动。", "Some people are impolite to couriers and say unpleasant things, which does not respect their labor."), ("我们应该多鼓励他们，不要给差评。", "We should encourage them more and not give bad reviews.")]
L2 = lesson(
    "Lesson 27 Presentation 1 activities: word building, the busiest day and talking about couriers",
    "快递 送单 收件 难听 帮手 客气 · 起早贪黑 下单 风里来雨里去 打仗 双十一 · 尊重 劳动 鼓励 差评",
    requires=[],
    cards=[
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up and think of three words that each contain at least one character similar to the characters in the provided words (example: 保安 → 保护, 安全, 安静; then 快递, 送单, 收件, 难听, 帮手, 客气). B. With your partner, discuss the parts of speech of the words you wrote, and translate them into English. My words:",
             tables=[WB]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Pair up. Read the passage and complete the sentences with the words and expressions below: 起早贪黑, 下单, 风里来雨里去, 跑, 便利, 打仗, 双十一, 辛苦, 快捷. B. With your partner, discuss your answers and explain the strategies you used in making your choices. C. Talk about the couriers on the busiest shopping day in the U.S. with your partner. The completed passage (my key):",
             examples=[D(*CZ)]),
        card("Activity 5 (Writing and Speaking)",
             "A. Pair up and use the following words and expressions to talk about couriers in the U.S. with your partner: 难道…吗, 跟打仗似的, 难听, 尊重, 劳动, 鼓励, 差评. Write your notes in the space provided. B. Share your discussion with the class. My sample:",
             examples=[D(z, e) for z, e in US5]),
    ],
    exercises=[
        M("Which word fits “十一月十一日是___”?", "双十一", ["节假日", "劳动节", "春节"], "双十一: Double Eleven."),
        M("Which expression means working from dawn to night?", "起早贪黑", ["风里来雨里去", "跟打仗似的", "多半儿"], "起早贪黑."),
        M("Which expression means braving the weather?", "风里来雨里去", ["起早贪黑", "好几百单", "上门收件"], "风里来雨里去."),
        M("What does 下单 mean?", "Place an order", ["Deliver an order", "Cancel a parcel", "Send a letter"], "下单."),
        M("Which pair means “fast and convenient”?", "快捷, 便利", ["辛苦, 打仗", "尊重, 劳动", "难听, 客气"], "既快捷又便利."),
        M("Which word fits “看到顾客高兴，快递员就不觉得___了”?", "辛苦", ["快捷", "便利", "双十一"], "不觉得辛苦了."),
        M("Which word shares the character 安 with 保安?", "安全", ["快递", "收件", "客气"], "保安 → 安全."),
        M("Which word shares the character 客 with 客气?", "顾客", ["保护", "快速", "收到"], "客气 → 顾客."),
        F("快递员常常要起___贪黑。", "早", PART, "起早贪黑."),
        F("在路上要___十多个小时。", "跑", PART, "跑: run."),
    ],
)

# ------------------------------------------------------------------ 3. 难道…吗
ND0 = table(["结构", "用法"], [["难道 + rhetorical question", "难道 strengthens the tone of a rhetorical question and can be placed before or after the subject"], ["难道 + general question = rhetorical question", "吗 can be omitted"]], title="The Rhetorical Question 难道……吗")
NDE = [("你不知道他换工作了吗？", "1. (a regular rhetorical question) Don’t you know he changed jobs?"), ("难道你不知道他换工作了吗？", "2. (a rhetorical question with stronger tone) Don’t you know he changed jobs? (stronger)"),
       ("你喜欢她吗？", "1. (general question) Do you like her?"), ("难道你喜欢她？", "2. (rhetorical question; 吗 can be omitted) Could it be that you like her?")]
ND1 = [("难道大卫写完作业了吗？", "1. (my key) Could David have finished his homework?"), ("难道快递员送错包裹了吗？", "2. (my key) Could the courier have delivered the wrong parcel?"), ("难道琳达的爸爸是军人吗？", "3. (my key) Could Linda’s father be a soldier?"),
       ("难道快递员可以来顾客家里收件吗？", "4. (my key) Could couriers really come to a customer’s home to collect parcels?"), ("难道当快递员比当保安辛苦吗？", "5. (my key) Could being a courier really be harder than being a guard?")]
ND2 = [("甲：你会说中文吗？", "1. A: Do you speak Chinese?"), ("乙：对不起，我不会说。", "B: Sorry, I don’t."), ("甲：难道你是美国人吗？", "A (my completion of the blank): Could you be an American?"), ("乙：不是，我是韩国人。", "B: No, I am Korean."),
       ("安娜：比尔，这个字是什么意思？", "2. Anna: Bill, what does this character mean?"), ("比尔：安娜，这不是“祝”字吗？我们昨天才学的，难道你忘了吗？", "Bill: Anna, isn’t this the character 祝? We only learned it yesterday; could you have forgotten? (my completion)"), ("安娜：现在想起来了。昨天我们还一起庆祝你的生日呢。", "Anna: I remember now. Yesterday we even celebrated your birthday together."),
       ("珍妮：李军，你有多久没回中国了？", "3. Jenny: Li Jun, how long has it been since you went back to China?"), ("李军：差不多三年没回去了。", "Li Jun: Almost three years."), ("珍妮：这么久啊。难道你不想家吗？", "Jenny: That long! Could you not be homesick? (my completion)"), ("李军：想啊，可是我工作太忙，走不开啊。", "Li Jun: I am, but I’m too busy with work to get away."),
       ("王红：小丽，都已经十二点多了，你怎么还不去食堂吃午饭呢？难道你不饿吗？", "4. Wang Hong: Xiao Li, it is already past twelve; why haven’t you gone to the cafeteria for lunch? Could you not be hungry? (my completion)"), ("小丽：王红，你先去吃吧。我得把这个邮件写完发出去再去。", "Xiao Li: Wang Hong, you go first. I have to finish writing this email and send it before I go."),
       ("张英：大卫，我做了这么多菜，可是你吃得很少，难道不好吃吗？", "5. Zhang Ying: David, I made so many dishes, but you eat very little; could it be that it doesn’t taste good? (my completion)"), ("大卫：张英，你的手艺很好，菜很好吃，不过，我这几天胃有点儿不舒服。", "David: Zhang Ying, your cooking is very good and the food is tasty, but my stomach has been a little upset these days."),
       ("周阳：彼得，你在中国呆了一个月，难道没学会用筷子吗？", "6. Zhou Yang: Peter, you stayed in China for a month; could you not have learned to use chopsticks? (my completion)"), ("彼得：在中国时，我常常用筷子吃饭，可是回到美国后，我就不习惯用了。", "Peter: In China I often ate with chopsticks, but after returning to America I got out of the habit.")]
ND3 = [("甲：这篇课文昨天学过了，难道你看不懂吗？", "Example: A: We studied this text yesterday; could it be you can’t understand it?"), ("乙：昨天我生病了，没来上课，所以我看不懂。", "B: Yesterday I was ill and missed class, so I can’t understand it."),
       ("甲：难道快递员会送错包裹吗？", "1. A (my completion): Could the courier deliver the wrong parcel?"), ("乙：快递员不会送错包裹的，你再等等吧。", "B: The courier won’t deliver the wrong parcel; wait a bit longer."),
       ("甲：难道你忘了我的生日吗？", "2. A (my completion): Could you have forgotten my birthday?"), ("乙：对不起，我最近工作太忙，没有想起来你的生日。", "B: Sorry, I have been too busy with work recently and didn’t remember your birthday."),
       ("甲：已经这么晚了，难道你明天不用上班吗？", "3. A (my completion): It is already so late; don’t you have to work tomorrow?"), ("乙：今天我晚一点回家，明天公司放假，不用上班。", "B: Today I’ll get home a little later; the company has a holiday tomorrow and there is no work."),
       ("甲：“双十一”网上有很多优惠，难道你不想买吗？", "4. A (my completion): There are many discounts online at “Double Eleven”; don’t you want to buy?"), ("乙：“双十一”网上有优惠也不行，我妈不让我买。", "B: Even with online discounts at “Double Eleven” it’s no good; my mom won’t let me buy."),
       ("甲：今天晚上咱们出去放松一下吧。你想去哪儿玩啊？", "5. A: Let’s go out and relax tonight. Where do you want to go?"), ("乙：难道你不累吗？", "B (my completion): Aren’t you tired?")]
L3 = lesson(
    "Lesson 27 Presentation 1 grammar: the rhetorical question 难道…吗",
    "难道你不知道他换工作了吗 · 难道你喜欢她 · 难道你忘了吗 · 难道你不想家吗 · 难道你不累吗",
    requires=[],
    cards=[
        card("The Rhetorical Question 难道……吗",
             "难道 can be used in a rhetorical question to strengthen the tone. It can be placed before the subject or after the subject. 难道 can be used to turn a general, “yes/no” question into a rhetorical question; 吗 can be omitted. Pattern: 难道 + rhetorical question; 难道 + general question = rhetorical question.",
             tables=[ND0], examples=[D(z, e) for z, e in NDE]),
        card("Activity 1 (Reading, Writing and Speaking)",
             "A. Pair up and rewrite these general questions as rhetorical questions, using 难道: 1. 大卫写完作业了吗？ 2. 快递员送错包裹了吗？ 3. 琳达的爸爸是军人吗？ 4. 快递员可以来顾客家里收件吗？ 5. 当快递员比当保安辛苦吗？ B. With your partner, read the rhetorical questions in Step A and translate them into English. Together, discuss how the meaning changes when these sentences are cast as rhetorical questions. My key (the question turns from a plain request for information into a doubting or surprised remark):",
             examples=[D(z, e) for z, e in ND1]),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the following dialogs. Write the rhetorical questions using 难道 in the spaces provided. B. Pair up and discuss the meanings of the rhetorical questions with 难道 in these audios and translate them into English. The six dialogs as printed, with my completions of the blanks:",
             examples=dlg([(l[:-1] if False else l[0].split("：")[0], l[0].split("：", 1)[1], l[1]) for l in ND2])),
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up and complete the dialogs with rhetorical questions using 难道. B. With your partner, discuss how you were able to complete this task. Practice the dialogs with your partner. The example, then my completions:",
             examples=dlg([(l[0].split("：")[0], l[0].split("：", 1)[1], l[1]) for l in ND3])),
    ],
    exercises=[
        M("What does 难道 do in a question?", "It strengthens the tone, making it rhetorical", ["It makes it polite", "It makes it a command", "It makes it past tense"], "难道 strengthens the tone."),
        M("Where can 难道 be placed?", "Before or after the subject", ["Only at the end", "Only before 吗", "After the object"], "Before or after the subject."),
        M("Can 吗 be omitted after 难道?", "Yes", ["No, never", "Only in writing", "Only with names"], "吗 can be omitted."),
        M("Which is the rhetorical version of 你喜欢她吗?", "难道你喜欢她？", ["你难喜欢她吗", "难你道喜欢她吗", "你喜欢难道她吗"], "难道 + general question."),
        M("What does 难道你不知道他换工作了吗 express?", "Surprise that you don’t know", ["A polite request", "Thanks", "A promise"], "Stronger rhetorical tone."),
        M("Which fits the blank: “你会说中文吗？ … 不是，我是韩国人。”?", "难道你是美国人吗", ["难道你是老师", "你是难道军人", "你难道说中文"], "My completion."),
        M("Which fits the blank after “差不多三年没回去了。这么久啊。”?", "难道你不想家吗", ["难道你很高兴吗", "难道你是老师吗", "难道你没有工作吗"], "My completion."),
        M("Which fits “这篇课文昨天学过了，___”?", "难道你看不懂吗", ["难道你很高兴", "难道你会飞", "难道你昨天来了"], "The book’s example."),
        F("___道你不知道他换工作了吗？", "难", PART, "难道: could it be that."),
        F("难道快递员送错包裹了___？", "吗", ["呢", "吧", "啊"], "吗 can end the question."),
    ],
)

# ------------------------------------------------------------------ 4. modal 的 + 跟…似的
MD0 = table(["结构", "用法"], [["Statement, ……的", "the particle 的 is most often a structural particle, but it can also be used as a modal particle after a statement that provides an added explanation of what the speaker is saying"]], title="The Modal Particle 的 (表示附加原因，解释说明)")
MDE = [("当快递员可比保安辛苦多了，起早贪黑的。", "1. Being a courier is much harder than being a guard, working from dawn to night."), ("我们得天天去操场集合，挺辛苦的。", "2. We have to gather on the sports ground every day; it’s quite tiring.")]
MD4 = [("快递员每天在路上要跑十多个小时，风里来雨里去的。", "1. (my key) Couriers run more than ten hours on the road every day, braving wind and rain."), ("现在寄包裹，快递员可以到你家里收件，挺方便的。", "2. (my key) Now to send a parcel the courier can come to your home to collect it; it’s quite convenient."),
       ("“快递小哥”每天要很早起来送货，晚上很晚才回家，起早贪黑的。", "3. (my key) “Courier guys” get up very early every day to deliver and get home very late, working from dawn to night."), ("节假日时，快递员每天要送好几百单，挺辛苦的。", "4. (my key) On holidays couriers deliver several hundred orders a day; it’s quite hard."),
       ("有些人给快递员差评，还说一些难听的话，挺不客气的。", "5. (my key) Some people give couriers bad reviews and say unpleasant things; that’s quite impolite."), ("以前我每天都去市场买菜，很麻烦的。现在我只在网上买。", "6. (my key) I used to go to the market to buy vegetables every day, which was a lot of trouble. Now I only buy online. (unused words in the box: 便利, 快捷, 容易)")]
SS0 = table(["结构", "用法"], [["跟 + Noun/Pronoun/Verb/Sentence + 似的", "expresses that something is similar to something else, very much the same as 像……一样; often used in metaphors or similes"], ["好像 + Noun/Pronoun/Verb/Sentence + 似的", "好像……似的 can replace 跟……似的 to express “it seems (as though)”"]], title="The Pattern 跟……似的")
SSE = [("他俩好得跟亲兄弟似的。", "1. The two of them are as close as brothers."), ("你跟我似的，不爱自己做饭，喜欢叫外卖。", "2. You are like me: you don’t like cooking yourself and like ordering takeout."), ("在“双十一”的时候，快递员的生活就跟打仗似的，每天要送好几百单。", "3. At “Double Eleven” a courier’s life is just like a battle, with several hundred orders to deliver a day."), ("小宋做快递员跟他在小区做保安似的一样辛苦。", "4. Xiao Song is as hard-worked as a courier as he was as a guard in the compound."),
       ("他们兄弟俩长得好像一个人似的。", "好像 1. The two brothers look as if they were one person."), ("我姐姐好像我似的，就喜欢吃苹果。", "2. My older sister is like me; she just likes eating apples."), ("刚才我看到她拿着一个行李出去了，好像去旅游似的。", "3. Just now I saw her go out carrying a piece of luggage, as if going traveling."), ("你怎么好像一个人过日子似的，家里什么家具都没有。", "4. How come you live as if you were living alone, with no furniture at all at home?")]
SS5 = [("他唱歌跟哭似的，一点也不好听。", "Activity 5, 1 (my key): He sings as if crying; it doesn’t sound good at all."), ("他走路好像喝醉了似的。", "2: He walks as if he were drunk."), ("她的脸红得跟苹果似的。", "3: Her face is as red as an apple."), ("今天的天气热得跟夏天似的。", "4: Today’s weather is as hot as summer."), ("这个短租屋干净得跟旅馆似的。", "5: This short-term rental is as clean as a hotel."), ("这里的建筑好像西式建筑似的。", "6: The buildings here look like Western-style buildings.")]
SS6 = [("美国的快递员好像也起早贪黑似的，圣诞节前特别忙。", "Activity 6 (my samples about U.S. couriers): U.S. couriers also seem to work from dawn to night, and are especially busy before Christmas."), ("我的快递员对我跟朋友似的，每次都笑着打招呼。", "My courier treats me like a friend and greets me with a smile every time."), ("下雪的时候，快递员送货跟打仗似的。", "When it snows, delivering is like a battle for couriers.")]
L4 = lesson(
    "Lesson 27 Presentation 1 grammar: the modal particle 的 and the pattern 跟…似的",
    "起早贪黑的 · 挺辛苦的 · 好得跟亲兄弟似的 · 跟打仗似的 · 好像…似的 · 红得跟苹果似的",
    requires=[],
    cards=[
        card("The Modal Particle 的 (表示附加原因，解释说明)",
             "The particle 的 is most often a structural particle, but it can also be used as a modal particle after a statement that provides an added explanation of what the speaker is saying. Pattern: Statement, …….的",
             tables=[MD0], examples=[D(z, e) for z, e in MDE]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Pair up and complete the sentences with the modal particle 的 (words in the box: 起早贪黑, 风里来雨里去, 便利, 辛苦, 快捷, 麻烦, 方便, 容易, 客气). B. With your partner, read the sentences aloud and translate them into English. My key:",
             examples=[D(z, e) for z, e in MD4]),
        card("The Pattern 跟……似的",
             "跟……似的 expresses that something is similar to something else, very much the same as 像……一样. This pattern is often used in metaphors or similes. Pattern: 跟 + Noun/Pronoun/Verb/Sentence + 似的. 好像……似的 can replace 跟……似的 to express “it seems (as though)”: 好像 + Noun/Pronoun/Verb/Sentence + 似的.",
             tables=[SS0], examples=[D(z, e) for z, e in SSE]),
        card("Activity 5 (Reading, Writing and Speaking)",
             "A. Pair up and write sentences using each word pair with the pattern 跟/好像……似的: 1. 唱歌，哭 2. 走路，醉 3. 脸，苹果 4. 天气，夏天 5. 短租屋，旅馆 6. 建筑，西式. B. Pair up; Student A reads sentences 1, 3 and 5 while Student B translates them into English. Then Student B reads sentences 2, 4 and 6 and Student A translates them into English. My key:",
             examples=[D(z, e) for z, e in SS5]),
        card("Activity 6 (Writing and Speaking)",
             "A. Pair up and create five sentences about courier service in the U.S. using the pattern 跟/好像……似的. B. Share your sentences with the class. My samples:",
             examples=[D(z, e) for z, e in SS6]),
    ],
    exercises=[
        M("What does the modal particle 的 at the end of 起早贪黑的 do?", "It adds an explanation to what was said", ["It marks the past", "It marks a question", "It marks a command"], "Modal particle."),
        M("Which sentence ends with the modal 的?", "我们得天天去操场集合，挺辛苦的", ["我的书很多", "他是我的朋友", "这是老师的"], "Modal 的."),
        M("What does 跟……似的 mean?", "Just like; similar to", ["Different from", "Before", "Because of"], "像……一样."),
        M("What can replace 跟……似的 to mean “it seems as though”?", "好像……似的", ["因为……所以", "不但……而且", "一边……一边"], "好像…似的."),
        M("What does 他俩好得跟亲兄弟似的 mean?", "The two are as close as brothers", ["The two are strangers", "The two are brothers", "The two argue"], "Simile."),
        M("What does 快递员的生活就跟打仗似的 compare a courier’s life to?", "A battle", ["A holiday", "A picnic", "A school"], "打仗."),
        M("Which fits “她的脸红得___苹果似的”?", "跟", ["比", "把", "被"], "跟…似的."),
        M("Which fits “她走路好像___了似的”?", "喝醉", ["写完", "吃饱", "学会"], "My key."),
        F("现在寄包裹，快递员可以到你家里收件，挺方便___。", "的", PART, "Modal 的."),
        F("他俩好得跟亲兄弟___的。", "似", PART, "跟…似的."),
    ],
)

# ------------------------------------------------------------------ 5. 正是因为
ZY0 = table(["结构", "用法"], [["正是因为……，……", "因为 can introduce clauses of cause and reason, and can also be a two-word preposition meaning “because of”; 正是 emphasizes 因为 to express “just because (of)”"], ["正是因为……，……才……", "才 can be used in the main clause to emphasize a result"]], title="正是因为……")
ZYE = [("正是因为快递既快捷又便利，我们都喜欢用快递。", "1. It is precisely because express delivery is both fast and convenient that we all like to use it."), ("正是因为中国的经济发展了，中国人的生活越来越好。", "2. It is precisely because China’s economy has developed that Chinese people’s lives are getting better and better."),
       ("正是因为“快递小哥”的辛苦，我们的生活才变得方便多了。", "With 才: It is precisely because of the “courier guys’” hard work that our lives have become so much more convenient."), ("正是因为外语很有用，你才更应该努力学习。", "With 才: It is precisely because foreign languages are very useful that you should study even harder.")]
ZY8 = [("正是因为手机叫外卖又方便又快，很多人才喜欢用手机订餐。", "Activity 8, 1 (my paragraph on 手机叫外卖): It is precisely because ordering takeout by phone is both convenient and fast that many people like to order meals by phone."), ("正是因为网约车可以在手机上叫车，也不用现金，人们才越来越常坐网约车。", "2 (网约车): It is precisely because ride-hailing lets you call a car on your phone, without cash, that people take them more and more often."),
       ("正是因为醉酒开车很危险，人们才找代驾送自己回家。", "3 (醉酒代驾): It is precisely because drunk driving is very dangerous that people find a designated driver to take them home."), ("正是因为民宿比旅馆便宜，又有家的感觉，才有越来越多的人喜欢住民宿。", "4 (民宿和短租屋): It is precisely because homestays are cheaper than hotels and feel like home that more and more people like to stay in them."),
       ("正是因为中国人越来越有钱，才有越来越多的人出国旅游、自驾游、扫货。", "5 (中国人出国旅游，自驾游，扫货): It is precisely because Chinese people are getting richer and richer that more and more of them travel abroad, take self-drive tours and go on shopping sprees.")]
L5 = lesson(
    "Lesson 27 Presentation 1 grammar: 正是因为 for “just because”",
    "正是因为…才… · 正是因为快递既快捷又便利 · 正是因为外语很有用 · 手机叫外卖 网约车 醉酒代驾 民宿",
    requires=[],
    cards=[
        card("正是因为……",
             "因为 can act as a subordinating conjunction to introduce clauses of cause and reason. 因为 also can act as a two-word preposition meaning “because of”. 正是 is used to emphasize 因为 to express “just because (of)”. Pattern: 正是因为……，…….  才 can be used in the main clause to emphasize a result.",
             tables=[ZY0], examples=[D(z, e) for z, e in ZYE]),
        card("Activity 7 (Listening, Writing and Speaking)",
             "A. Listen to the sentences with 正是因为 (six items) and translate them into English. B. Pair up and check your translation with your partner. Then repeat the sentences in Chinese with your partner. (Audio; the sentences are not in the book.)"),
        card("Activity 8 (Listening, Writing and Speaking)",
             "A. Pair up and talk about the cause and effect of the following topics using 正是因为: 1. 手机叫外卖 2. 网约车 3. 醉酒代驾 4. 民宿和短租屋 5. 中国人出国旅游，自驾游，扫货. Write a short paragraph for each topic. B. Share your paragraphs with the class. My samples:",
             examples=[D(z, e) for z, e in ZY8]),
    ],
    exercises=[
        M("What does 正是因为 mean?", "Just because; precisely because", ["Although", "If", "Besides"], "正是 emphasizes 因为."),
        M("What can 才 do in the main clause?", "Emphasize the result", ["Make a question", "Make it negative", "Mark the past"], "才 emphasizes a result."),
        M("Which sentence is correct?", "正是因为外语很有用，你才更应该努力学习", ["正是外语很有用因为，你才更应该努力学习", "因为正是外语很有用，你更应该努力学习", "你才更应该努力学习，正是因为外语很有用才"], "Pattern."),
        M("Which fits “正是因为快递既快捷又便利，我们都___用快递”?", "喜欢", ["讨厌", "忘记", "害怕"], "Example 1."),
        M("What is the cause in “正是因为中国的经济发展了，中国人的生活越来越好”?", "China’s economy has developed", ["People’s lives got better", "People got older", "The weather improved"], "Example 2."),
        M("What is the result in “正是因为‘快递小哥’的辛苦，我们的生活才变得方便多了”?", "Our lives have become much more convenient", ["Couriers are tired", "Couriers quit", "Parcels are free"], "The result."),
        M("Which fits “正是因为醉酒开车很危险，人们___找代驾”?", "才", ["吗", "过", "着"], "才: emphasizes the result."),
        F("正是因为外语很有用，你才更应___努力学习。", "该", PART, "应该: should."),
        F("正是因为民宿比旅馆便宜，___有越来越多的人喜欢住民宿。", "才", ["吗", "呢", "吧"], "才: emphasizes the result."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
SKQ = [("为什么说中国的快递发展很快？举二个例子。", "Activity 1C, Segment 1: Why do we say China’s express delivery has developed fast? Give two examples."), ("大部分快递员的年龄有多大？", "Segment 2, 1: How old are most couriers?"), ("快递员都是高中毕业吗？猜一猜“大专”是什么教育水平？", "2: Did all couriers graduate from high school? Guess what educational level 大专 is."), ("快递员每月工资怎么样？最多能赚多少钱？", "3: How is a courier’s monthly pay? What is the most one can earn?"), ("为什么说“快递小哥”已经成为我们生活中不可缺少的一部分？", "Segment 3: Why do we say “courier guys” have become an indispensable part of our lives?"),
       ("美国有哪些快速公司？美国快递员多不多？", "Activity 1E (questions to talk about a U.S. courier company): What courier companies are there in the U.S.? Are there many U.S. couriers?"), ("美国快递员的年龄一般有多大？", "How old are U.S. couriers usually?"), ("美国有没有大学毕业生去当快递员？", "Do any university graduates in the U.S. become couriers?"), ("美国快递员的工资怎么样？", "How is the pay of U.S. couriers?")]
VT = table(["词", "拼音", "Meaning (mine)"], [["奖章", "jiǎngzhāng", "medal"], ["内蒙古", "nèiménggǔ", "Inner Mongolia"], ["运营", "yùnyíng", "operations"], ["稳定", "wěndìng", "stable"], ["头脑", "tóunǎo", "brains, mind"], ["效率", "xiàolǜ", "efficiency"], ["无人机", "wú rén jī", "drone"]], title="Activity 2A: the glossed words and the four phrases to guess", say=[0])
SX = ("从一名普通的快递员，成长为全国五一劳动奖章获得者，需要多久？宋学文的答案是六年。作为一名快递小哥，从二零一一年到二零一七年，他送了二十二万个包裹，走了三十多万公里，得到零差评，成为了第一个获得全国“五一”劳动奖章的快递员。宋学文十六岁时从老家内蒙古来到北京。他只有一个愿望就是想找一个稳定的工作，多赚一些钱。刚开始他当保安，后来做了快递员。很多人认为送快递很容易，只需要有体力，不需要有头脑，可宋学文不这样认为。以前，他每次送货时，收货人有时不在家，他还得再跑一趟，把货当面交给他们。有的人一次买好几件商品，他送完一单还得再送一单。有的办公室下班时间也不一样，送货的要求也不一样。为了提高效率，他在笔记本上记下每个顾客的上班、下班时间和送货的要求，然后建立了一个送货工作法，帮助他按时把货送到。他还把这个工作法告诉给别的快递员，向他们介绍自己的经验，这大大地提高了他们送货的效率。去年，宋学文用四个月的时间，完成了无人机运营培训，以后，他可以用无人机把更多的包裹快速地送到顾客手里。",
      "“Courier Guy” wins the national May Day Labor Medal. How long does it take to grow from an ordinary courier into a winner of the national May Day Labor Medal? Song Xuewen’s answer is six years. As a courier, from 2011 to 2017 he delivered 220,000 parcels and traveled over 300,000 kilometers, got zero bad reviews, and became the first courier to win the national “May Day” Labor Medal. Song Xuewen came to Beijing at sixteen from his hometown of Inner Mongolia. He had only one wish: to find a stable job and earn a bit more money. At first he was a security guard and later became a courier. Many people think delivering is easy, that it takes only physical strength and no brains, but Song Xuewen doesn’t think so. Before, whenever he delivered, the recipient was sometimes not at home and he had to make another trip to hand over the goods in person. Some people buy several items at a time, and after delivering one order he had to deliver another. Some offices have different closing times and different delivery requirements. To raise efficiency, he wrote down in a notebook each customer’s work hours and delivery requirements, and then set up a delivery method that helped him deliver on time. He also told this method to other couriers and shared his experience, which greatly raised their delivery efficiency. Last year Song Xuewen spent four months completing drone operations training, and in future he can use drones to quickly deliver more parcels to customers’ hands. (source note: adapted from an article by 任敏 in the Beijing Daily of May 4, 2019; the book writes the years and figures in digits)")
SXK = [("五一劳动奖章是中国颁发给优秀劳动者的奖章，通常在五月一日劳动节前后发。", "Activity 2B-1 (my answer; the book asks you to look it up online): The May Day Labor Medal is a medal China gives to outstanding workers, usually around Labor Day on May 1."),
       ("因为他六年送了二十二万个包裹，走了三十多万公里，得到零差评，还把自己的工作法告诉别的快递员。", "2B-2 (my answer): Because in six years he delivered 220,000 parcels, traveled over 300,000 kilometers, got zero bad reviews and shared his working method with other couriers."),
       ("因为很多人觉得送快递只需要有体力，不需要有头脑。", "2B-3 (my answer): Because many people think delivering takes only physical strength and no brains."),
       ("他在笔记本上记下每个顾客的上班、下班时间和送货的要求，建立了一个送货工作法，还把它告诉别的快递员。", "2B-4 (my answer): He wrote down each customer’s work hours and delivery requirements in a notebook, set up a delivery method and shared it with other couriers."),
       ("他用四个月的时间完成了无人机运营培训。", "2B-5 (my answer): He spent four months completing drone operations training.")]
DA = ("为了能够快速地把货送给顾客，窦立国根据自己的经验，画了一个便捷的北京地图。根据这个地图送快递，可以节省一个半小时，比那些地图软件还好用。由于他工作好，能力强，很快成为了分公司的经理。在他的管理下，分公司的快递业务是全公司第一名。他用五年的时间就挣到了二百万元。赚到钱后，他在老家买了一个大房子，还买了宝马和奔驰车。", "Passage A: To deliver goods to customers quickly, Dou Liguo drew a convenient map of Beijing based on his own experience. Delivering by this map saves an hour and a half, and is better than those map apps. Because he worked well and was capable, he soon became the manager of a branch company. Under his management the branch’s express business ranked first in the whole company. In five years he earned two million yuan. After making money he bought a big house in his hometown and also bought a BMW and a Mercedes. (the book writes 200 万 in digits)")
DB = ("近几年，窦立国一直收集衣物和图书，然后送给农村的孩子，还给他们建了很多图书馆，让他们有机会读书。他希望这些孩子也能和他一样通过读书了解外面的世界，最后改变自己的命运。", "Passage B: In recent years Dou Liguo has been collecting clothes and books, giving them to rural children, and has also built many libraries for them so that they have the chance to read. He hopes these children can also, like him, learn about the outside world through reading and finally change their own fate.")
DC = ("窦立国在北京第一份工作是酒店保安，一个月六百元。干了几个月后，在经理的鼓励下，他在厨房学习做菜的手艺，当了酒店的厨师。厨师干了三年后，窦立国去了一家快递公司。为了让生意好起来，他印了一万张名片，天天在小区里发。有的人拿到了他的名片，就给他打电话，让他帮忙寄快递。几个月后，生意越来越好。", "Passage C: Dou Liguo’s first job in Beijing was as a hotel security guard at 600 yuan a month. After a few months, encouraged by the manager, he learned cooking in the kitchen and became the hotel’s cook. After three years as a cook, Dou Liguo went to a courier company. To get business going he printed ten thousand business cards and handed them out in residential compounds every day. Some people who got his card phoned him to help send parcels. A few months later business was better and better. (the book writes 600 in digits)")
DD = ("二零一四年九月十九日是窦立国最开心的日子。这一天，阿里巴巴在纽约证交所上市，窦立国是八个敲钟人之一，还和马云一起照了相。一个骑着小车在北京城到处送货的“快递小哥”，为什么会被阿里巴巴请来敲钟？", "Passage D: September 19, 2014 was Dou Liguo’s happiest day. That day Alibaba listed on the New York Stock Exchange, and Dou Liguo was one of the eight bell-ringers and also had his picture taken with Jack Ma. Why would a “courier guy” riding a little cart delivering all over Beijing be invited by Alibaba to ring the bell? (the book writes the date in digits; 马云 is the founder of Alibaba)")
DS = [("窦立国在北京第一份工作是酒店保安，后来学做菜当了厨师，三年后去快递公司，印名片发给小区的人，生意越来越好。", "Activity 3C, my summary of the Group 1 passages (C and D): Dou Liguo’s first job in Beijing was as a hotel guard; he later learned cooking and became a cook, and three years later went to a courier company, printed cards to give to people in the compounds, and business got better and better."),
      ("他画了一个便捷的北京地图，很快成为经理，五年挣了二百万元；近几年他把衣物和图书送给农村孩子，还建图书馆。", "My summary of the Group 2 passages (A and B): He drew a convenient map of Beijing, soon became a manager and earned two million yuan in five years; in recent years he has given clothes and books to rural children and built libraries.")]
VQ = [("窦立国在北京打工时有什么梦想？", "Activity 4A-1 (video questions): What dream did Dou Liguo have when he worked in Beijing?"), ("他帮助一个客人以后，他的经理问他有什么愿望时，他是怎么回答的？", "2: After he helped a guest, how did he answer when his manager asked what wish he had?"), ("不做厨师以后，他做了哪些工作？", "3: After he stopped being a cook, what jobs did he do?"), ("是什么让他决定去做快递？", "4: What made him decide to become a courier?"), ("做快递的第一单他赚了多少钱？", "5: How much did he earn from his first courier order?"), ("后来，他加入了什么组织？他做了什么事？", "6: Later, what organization did he join, and what did he do?")]
L6 = lesson(
    "Lesson 27 Presentation 1 skill integration: couriers in China, a medal winner and Dou Liguo",
    "快递的发展 · 大专 · 宋学文 · 五一劳动奖章 · 无人机 · 窦立国 · 中国最励志的快递小哥",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the recording and write the main idea expressed. B. Pair up and discuss how you understood the main idea from the vocabulary and contextual clues. C. Listen to the recording again in segments and answer the questions. D. With your partner, discuss your answers and explain how you understood the questions. E. With your partner, talk about a U.S. courier company using the questions below. (The recording is not in the book, so there is no key; the questions are the book’s.)",
             examples=[D(z, e) for z, e in SKQ]),
        card("Skill Integration, Activity 2 (Reading, Writing and Speaking)",
             "A. Pair up and read an article about Song Xuewen and discuss the meaning of the phrases that follow (1. 稳定的工作 2. 有头脑 3. 提高效率 4. 无人机) using the context and your knowledge of the vocabulary. B. With your partner, read the article again and answer the questions. C. Share your answers with the class. Explain what strategies you used to comprehend the content. D. Talk about the following topics with your partner: What kind of medals are given to hard-working couriers in the U.S.? Must a courier in the U.S. hand the goods to the recipient in person; if the recipient is not at home, what does the courier do? Do U.S. courier companies use drones, and if so what for? The article, the glossed words and my answers:",
             tables=[VT], examples=[D(*SX)] + [D(z, e) for z, e in SXK]),
        card("Skill Integration, Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up, read the passages, and arrange them in a logical order. B. With your partner, discuss the order of the passages and explain what strategies you used for your ordering. C. In two groups of two, read the passages again and summarize each one. D. Re-group into three pairs by pairing up students from Group A with students from Group B. Summarize the passages you read for your new partner. The four passages are printed under the title 中国最励志的“快递小哥”; in the book they are out of order. My correct order: 1. Passage D (the happiest day), 2. Passage C (his first jobs and the courier company), 3. Passage A (the map and his success), 4. Passage B (recent charity). The passages in my order, then my summaries:",
             examples=[D(*DD), D(*DC), D(*DA), D(*DB)] + [D(z, e) for z, e in DS]),
        card("Skill Integration, Activity 4 (Listening, Reading, Writing and Speaking)",
             "A. Watch a video segment about Dou Liguo and answer the questions. B. Pair up and discuss your answers with your partner. Share your discussion with the class. (The video is not included, so there is no key; the questions are the book’s.)",
             examples=[D(z, e) for z, e in VQ]),
    ],
    exercises=[
        M("Who won the national May Day Labor Medal as a courier?", "Song Xuewen", ["Dou Liguo", "Xiao Zhang", "Lao Li"], "宋学文."),
        M("How long did it take him to grow from an ordinary courier into a medal winner?", "Six years", ["One year", "Twenty years", "Three months"], "宋学文的答案是六年."),
        M("What was his only wish when he came to Beijing at sixteen?", "To find a stable job and earn more money", ["To become famous", "To study abroad", "To open a company"], "找一个稳定的工作，多赚一些钱."),
        M("What do many people think about delivering?", "It takes only strength, not brains", ["It is dangerous", "It pays a lot", "It is boring"], "只需要有体力，不需要有头脑."),
        M("How did he raise efficiency?", "He noted customers’ hours and requirements and built a delivery method", ["He bought a bigger truck", "He worked at night only", "He hired helpers"], "建立了一个送货工作法."),
        M("What training did he complete last year?", "Drone operations", ["Cooking", "Driving", "English"], "无人机运营培训."),
        M("What was Dou Liguo’s first job in Beijing?", "A hotel security guard", ["A courier", "A teacher", "A cook"], "酒店保安."),
        M("How many business cards did he print?", "Ten thousand", ["One hundred", "One thousand", "A million"], "印了一万张名片."),
        M("What happened on September 19, 2014?", "Alibaba listed in New York and Dou Liguo rang the bell", ["He won a medal", "He opened a library", "He became a manager"], "八个敲钟人之一."),
        M("What does Dou Liguo do for rural children?", "Gives them clothes and books and builds libraries", ["Teaches them cooking", "Gives them phones", "Takes them to Beijing"], "收集衣物和图书…建了很多图书馆."),
        F("他在笔记本上记下每个顾客的上班、下班时间和送货的要___。", "求", PART, "要求: requirements."),
        F("为了让生意好起来，他印了一万张名___。", "片", PART, "名片: business card."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese
USPS = table(["Service", "Delivery time", "Details"], [["USPS 美国邮局: Global Express Mail", "1–3 个工作日", "可以查看, 有退款保证, 包括 $100 保险, 邮费 $67.80 以上"], ["Priority Mail Express International", "3–5 个工作日", "可以查看, 有退款保证, 包括 $100 文件/$200 货物的保险, 邮费 $44.00 以上"], ["Priority Mail International", "6–10 个工作日", "没有退款保证, 邮费 $25.85 以上"]], title="USPS 美国邮局 (the book notes: the prices are for this lesson only and may not be the actual prices)")
UPSF = table(["Service", "Delivery time", "Details"], [["UPS 联合包裹服务: UPS Worldwide Saver", "2–5 个工作日", "$50 左右/1 公斤"], ["UPS Worldwide Expedited", "3–5 个工作日", "$45 左右/1 公斤"], ["(both)", "", "按重量收费, 加上其他的费用"], ["FedEx 联邦快递: International Next Flight", "the fastest", "$160 左右"], ["International First (早上送达) and International Priority", "1–3 个工作日 (by destination)", "$150 左右"], ["International Economy", "5 个工作日内", "$120 左右"], ["International Mail Service", "(not stated)", "最便宜; 如果包裹不大也比较轻, 例如衣服、光盘等, 可以使用这个服务, $100 左右"]], title="UPS and FedEx")
SPQ = table(["Item", "Shentong Delivery 申通快递, 中美专线 (门到门的服务)"], [["业务介绍", "申通国际中美专线是专门服务于中国到美国的包裹，可邮寄各种物品"], ["业务特色", "快捷，方便，中国至美国门到门一站式服务，保证安全"], ["价格优惠", "首重 120 元/0.5KG（续重 50 元/0.5KG）"], ["服务保障", "全程跟踪，丢失赔偿"], ["服务范围", "服务美国所有的州（不包括小岛屿和阿拉斯加地区）"], ["到达时间", "平均 6–7 个工作日"], ["联系咨询", "(an e-mail address is printed in the book; left out)"]], title="Activity 2A: the courier advertisement")
SPK = [("门到门的服务是快递员从你家门口取件，直接送到收件人的家门口。", "Activity 2A-1 (my answer): Door-to-door service means the courier collects from your door and delivers right to the recipient’s door."), ("首重一百二十元每半公斤，续重五十元每半公斤。", "2A-2 (my answer): The first 0.5 kg costs 120 yuan and each further 0.5 kg costs 50 yuan."), ("安全，他们保证安全，全程跟踪，丢失赔偿。", "2A-3 (my answer): Yes; they guarantee safety, track the whole way and compensate for loss."),
       ("不完全包括，不包括小岛屿和阿拉斯加地区。", "2A-4 (my answer): Not entirely; small islands and the Alaska region are not included."), ("平均六到七个工作日。", "2A-5 (my answer): On average six to seven working days.")]
SPQ2 = [("寄到芝加哥要多长时间？多少钱？", "Activity 2B (my questions for the call): How long does it take to Chicago, and how much?"), ("包裹有没有重量和大小的限制？", "Are there weight and size limits for the parcel?"), ("包裹丢了怎么赔偿？", "How is a lost parcel compensated?"), ("能不能上门取件？", "Can you collect it from my door?")]
JB = table(["Item", "招聘快递员, 5000–8000 元/月"], [["工资", "工资高，多劳多得，没有最高限制"], ["福利", "加班补助，包吃、包住、电话费补助，餐费补助"], ["工作地点", "北京市朝阳区西坝河东里 97 号楼"], ["送货地点", "北京市朝阳区"], ["有意者请电", "(a telephone number is printed in the book; left out)"], ["工作要求", "1. 送件、取件 2. 准时送达物品 3. 整理、上交业务单据和资料 4. 客户维护，客户咨询的处理和意见的反馈"], ["招聘条件", "1. 初中、高中或大学毕业 2. 工作认真，有很强的责任心 3. 能吃苦，人品好 4. 身体健康，没有不良习惯"]], title="Activity 3A: the job posting")
JK = [("每月大约能赚五千到八千元。", "Activity 3A-1 (my answer): About 5,000 to 8,000 yuan a month."), ("福利有加班补助，包吃、包住，还有电话费补助和餐费补助。", "3A-2 (my answer): Benefits include overtime allowance, free meals and housing, and phone and meal allowances."),
      ("要送件、取件，准时送达物品，整理、上交业务单据和资料，还要维护客户，处理客户的咨询和反馈意见。", "3A-3 (my answer): Collect and deliver items, deliver on time, organize and hand in documents, maintain customers and handle their inquiries and feedback."), ("初中、高中或大学毕业，工作认真，有很强的责任心，能吃苦，人品好，身体健康，没有不良习惯的人。", "3A-4 (my answer): People who have graduated from junior high, high school or university, work conscientiously, have a strong sense of responsibility, can bear hardship, have good character, are healthy and have no bad habits.")]
EM = [("王老师，您好。我们小组推荐联邦快递的国际经济服务，五个工作日内就能送到，一百二十美元左右，不太贵，也比较快。谢谢您！", "Activity 1E (my sample recommendation email; the book’s header lines TO, CC and Subject are blank): Hello, Professor Wang. Our group recommends FedEx’s International Economy service: it arrives within five working days for about $120, not too expensive and fairly fast. Thank you!")]
L7 = lesson(
    "Lesson 27 Presentation 1 using Chinese in context: shipping abroad, a courier company and a job posting",
    "美国邮局 联合包裹服务 联邦快递 · 申通快递 门到门 首重 续重 · 招聘快递员 福利 工作要求 招聘条件",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Listening, Reading, Writing and Speaking)",
             "Scenario: You just received an email from a teacher who taught you Chinese during your studies at Beijing University. Your teacher needs your suggestions on using courier services in the United States. You will discuss this with your classmates and make suggestions for your teacher. A. Listen to the email from Mark’s teacher Professor Wang in Beijing and summarize the information he wants from Mark. B. Pair up and see if you and your partner arrived at the same conclusion. C. Divide into two groups. Read the information about international shipping services from USPS, UPS and FedEx and compare their delivery fees, speeds, times, insurance, etc. Decide which service your group would recommend for Professor Wang’s daughter. D. After discussing the choices, each group take turns presenting their decision and explains why they think it is the best choice. E. After completing your presentation, decide which group’s decision is preferred and write an email to Professor Wang with your recommendation. (The email is audio and not in the book.) The three services and my sample recommendation:",
             tables=[USPS, UPSF], examples=[D(*EM[0])]),
        card("Using Chinese in Context, Activity 2 (Reading, Writing and Speaking)",
             "Scenario: You have been studying Chinese at Fudan University in Shanghai for several months. Christmas is approaching and you’d like to mail Christmas gifts to your family in the U.S. You just found a courier company on the Internet and need information about parcel delivery fees, arrival times, insurance, etc. A. Pair up and read about the Chinese courier company Shentong Delivery. Get to know the details of their services by answering the questions: 1. 这家快递公司有中国到美国门到门服务，这是什么意思？ 2. 寄包裹的价格是多少？ 3. 用这家快递公司寄包裹安全吗？ 4. 他们的快递服务包括美国所有的地方吗？ 5. 包裹通常多长时间能到？ B. With your partner, discuss the details of the courier service and list all the questions you will ask when you call the courier company for further information. C. Role-play: You plan to mail a parcel of Christmas gifts to your parents in Chicago, but you want to know how much it will cost and how long it will take to arrive via courier service from Shanghai to Chicago. Call the company; your partner plays the customer service agent. Then switch roles and repeat. The advertisement, my answers and my questions:",
             tables=[SPQ], examples=[D(z, e) for z, e in SPK + SPQ2]),
        card("Using Chinese in Context, Activity 3 (Reading, Writing and Speaking)",
             "Scenario: You are currently studying Chinese in Beijing University and sharing an apartment with a Chinese student. Your roommate would like to work as a courier after graduating from community college. You saw an online posting for hiring couriers and encourage your roommate to call the company to inquire about the position. A. Read the job posting and familiarize yourself with the details by answering the questions: 1. 招聘的快递员大约每月能赚多少钱？ 2. 这个工作的福利怎么样？ 3. 对这个快递员的工作要求是什么？ 4. 什么样的人适合做这个快递工作？ B. Pair up and check your answers and list all the questions that you will ask when you call the courier company. C. Role-play: One partner calls the courier company to inquire about the position; the other plays the company manager. Switch roles and repeat. The posting and my answers:",
             tables=[JB], examples=[D(z, e) for z, e in JK]),
    ],
    exercises=[
        M("Which USPS service is the fastest in the book’s list?", "Global Express Mail", ["Priority Mail International", "International Mail Service", "UPS Worldwide Saver"], "1–3 working days."),
        M("Which FedEx service is the cheapest?", "International Mail Service", ["International Next Flight", "International First", "International Economy"], "最便宜."),
        M("What does 门到门 mean?", "Door to door", ["Gate to gate", "Door only", "Roof to roof"], "门到门."),
        M("What is Shentong’s price for the first 0.5 kg?", "120 yuan", ["50 yuan", "12 yuan", "500 yuan"], "首重 120 元."),
        M("How long does a Shentong parcel take on average?", "6 to 7 working days", ["1 day", "3 days", "20 days"], "平均 6–7 个工作日."),
        M("What does Shentong not cover?", "Small islands and the Alaska region", ["Chicago", "New York", "Texas"], "不包括小岛屿和阿拉斯加地区."),
        M("What is the salary of the posted courier job?", "5,000–8,000 yuan a month", ["500 yuan a month", "80,000 yuan a month", "Unpaid"], "5000–8000 元/月."),
        M("Which benefit does the posting mention?", "Free meals and housing", ["A car", "A house", "Free flights"], "包吃、包住."),
        M("Which is a requirement for the applicant?", "A strong sense of responsibility", ["A college degree only", "Age over fifty", "Living abroad"], "有很强的责任心."),
        M("Which is NOT a job duty in the posting?", "Cooking meals for customers", ["Delivering items", "Collecting items", "Handling customer inquiries"], "工作要求."),
        F("申通国际中美专线是专门服务于中国到美国的包___。", "裹", PART, "包裹: parcel."),
        F("工作认真，有很强的责___心。", "任", PART, "责任心: sense of responsibility."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 27 Presentation 1 vocabulary", "19 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. Several cells are broken by page layout in the PDF; the entries 双十一, 起早贪黑 and 风里来雨里去 are written out in full.", VOC1)

UNIT = unit("第二十七课 Presentation 1: 快递小哥, 难道, 的, 跟…似的, 正是因为", [L1, L2, L3, L4, L5, L6, L7, L8])
