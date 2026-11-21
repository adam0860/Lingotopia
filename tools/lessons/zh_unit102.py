"""Unit 102: Lesson 30 (Unit 5 review), Vocabulary Review: Activities 1-6 (character tables and words, odd one out, four passages with word banks,
the key sentences and the six scripts, the board game note). Audio and pictures (the board game board) are not included; numbers the book writes as digits
are spelled out in Chinese text; answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段里")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]

# ------------------------------------------------------------------ 1. activity 1-2
TA = table(["1", "2", "3", "4", "5"], [["营", "压", "爱", "餐", "势"], ["熟", "顾", "困", "直", "好"], ["优", "前", "力", "养", "成"], ["照", "点", "播", "难", "途"], ["丰", "选", "富", "手", "绩"]], title="Activity 1A, Student A: characters to combine into words")
TB = table(["1", "2", "3", "4", "5"], [["解", "收", "网", "业", "决"], ["待", "赚", "享", "钱", "宿"], ["担", "分", "毕", "入", "标"], ["寄", "心", "红", "目", "遇"], ["另", "热", "创", "门", "外"]], title="Activity 1A, Student B: characters to combine into words")
TW = table(["Table", "Some words that can be made from the characters (my list; the book gives no key)"], [["Student A", "压力，爱好，照顾，困难，直播，丰富，选手，成绩，前途，优势，养成，营养，点餐"], ["Student B", "解决，收入，毕业，目标，待遇，赚钱，分享，担心，寄宿，创业，热门，另外，网红"]], title="Words from the two tables")
GR = table(["", "Instruction"], [["Activity 1B", "Pair up. Review the meanings of each set of phrases in both tables, then pick four words from the other table to create sentences. Your partner will translate the sentences."], ["Activity 1C 汉字接龙", "Working as a class, the first student will say a phrase and the second student will come up with another phrase that starts with the same pinyin of the last character of the previous phrase; the tone can be different. For example: Student 1: 可怜 (lián), Student 2: 练习 (liàn), Student 3: 习惯 (guàn), Student 4: 管理 (guǎn)… Optional: when a student runs out of words they are withdrawn from the game and the remaining students continue to compete until there is a single winner."]], title="Activity 1: the other steps")
OD = table(["Set", "Four words", "The one not related to the others (my key)"], [["1", "比赛 冠军 选手 帮手", "帮手"], ["2", "直播 打赏 网红 扫货", "扫货"], ["3", "人才 条件 等候 优势", "等候"], ["4", "房主 短租 宾馆 醉酒", "醉酒"], ["5", "抽烟 喝酒 逃学 跳舞", "跳舞"], ["6", "沟通 交流 了解 坚持", "坚持"], ["7", "客气 尊重 关心 差评", "差评"]], title="Activity 2B: select the phrase that is not related to the others")
A2 = table(["", "Instruction"], [["Activity 2A", "Form groups of three. Your teacher shows one character at a time from the table (重, 学, 心, 网). Each group will think of as many vocabulary words or phrases that contain that character as possible. Your teacher will set a time limit to complete the activity. The team that compiles the most words wins."], ["Activity 2C", "Using the phrases in Step B, select four phrases and explain the meaning of each without giving away the exact word. Your partners will guess which phrase you are describing. Take turns until each group member has had a turn."]], title="Activity 2: the other steps")
EX2 = ("旅行的时候住的地方，价钱通常比较贵", "Activity 2C, the book’s example (answer: 宾馆): The place where you stay when traveling, and the price is usually rather high.")
L1 = lesson(
    "Lesson 30 Vocabulary Review: combining characters and odd one out",
    "营养 · 压力 · 解决 · 创业 · 汉字接龙 · 重 学 心 网 · 比赛 冠军 选手 帮手 · 住宿",
    requires=[],
    cards=[
        card("Vocabulary Review, Activity 1 (Reading, Speaking, and Listening)", "A. Pair up. Each student draws from one table and combines characters to form as many words as possible. To make this activity more interesting, the teacher imposes a time limit for students. The two tables, the other steps and my list of words:", tables=[TA, TB, GR, TW]),
        card("Vocabulary Review, Activity 2 (Reading, Speaking, and Listening)", "A. Form groups of three. Your teacher shows one character at a time from the table: 重 学 心 网. B. Read each set of four words and select the phrase that is not related to the others. C. Using the phrases in Step B, select four phrases and explain the meaning of each without giving away the exact word. The sets with my key and the book’s example:", tables=[A2, OD], examples=[D(*EX2)]),
    ],
    exercises=[
        M("Which does not belong: 比赛, 冠军, 选手, 帮手?", "帮手", ["比赛", "冠军", "选手"], "比赛，冠军，选手 are about a contest; 帮手 means helper."),
        M("Which does not belong: 直播, 打赏, 网红, 扫货?", "扫货", ["直播", "打赏", "网红"], "直播，打赏，网红 are about live streaming; 扫货 is a shopping spree."),
        M("Which does not belong: 人才, 条件, 等候, 优势?", "等候", ["人才", "条件", "优势"], "等候 means waiting."),
        M("Which does not belong: 房主, 短租, 宾馆, 醉酒?", "醉酒", ["房主", "短租", "宾馆"], "醉酒 means drunk; the others are about lodging."),
        M("Which does not belong: 抽烟, 喝酒, 逃学, 跳舞?", "跳舞", ["抽烟", "喝酒", "逃学"], "The other three are bad habits."),
        M("Which does not belong: 沟通, 交流, 了解, 坚持?", "坚持", ["沟通", "交流", "了解"], "坚持 means persist; the others are about communication and understanding."),
        M("Which does not belong: 客气, 尊重, 关心, 差评?", "差评", ["客气", "尊重", "关心"], "差评 is a bad review."),
        F("旅行的时候住的地方，价钱通常比较贵：___。", "宾馆", ["民宿", "房主", "短租"], "宾馆: guest house."),
        F("用 压 和 力 组成的词是：___。", "压力", ["力压", "压迫", "用力"], "压力: pressure."),
        F("用 解 和 决 组成的词是：___。", "解决", ["决解", "解释", "决心"], "解决: solve."),
    ],
)

# ------------------------------------------------------------------ 2. activity 3
W1 = table(["Passage", "Word bank (the book’s)", "Blanks in order (my key; the book gives none)"], [["1", "确认 追踪 下单 发票 智能 便利", "下单，确认，发票，追踪，智能，便利"], ["2", "适应 辛苦 陪读 照顾 优势 理想", "优势，理想，适应，辛苦，陪读，照顾"], ["3", "学区 重视 补习 培养 特长 将来", "将来，重视，学区，补习，培养，特长"], ["4", "创业 先进 独生子女 发达 目标 满足", "独生子女，发达，目标，先进，满足，创业"]], title="Activity 3A: complete the sentences as you read")
PS = [("利用网路平台订餐很容易，你得先下单，然后确认你的信息，付款后，他们还会给你发送电子发票。餐点送到前你还可以定位追踪，这样的智能科技给我们的生活带来了很大的便利。", "Passage 1 (completed; my key): Ordering meals through an online platform is easy: you first place the order and then confirm your information, and after you pay they also send you an electronic invoice. Before the food arrives you can also locate and track it; such smart technology has brought great convenience to our lives. (the book writes 网路 as printed)"),
      ("为了让自己更有优势，以后能找到理想的工作，很多人选择出国留学。但是由于在国外念书还得适应国外的生活，所以比较辛苦，特别是年纪小的留学生，所以有些父母会跟着孩子到国外去陪读，照顾他们。", "Passage 2: To have more of an advantage and later find an ideal job, many people choose to study abroad. But since studying abroad also means adapting to life abroad, it is rather hard, especially for young students, so some parents follow their children abroad to accompany their studies and look after them."),
      ("中国的父母相信，孩子有好的教育才会有好的将来，因此很重视孩子的学习成绩，除了想办法让孩子去好的学区读书，下课后送孩子补习以外，为了培养孩子的特长，还送孩子去上各种兴趣班，所以在中国父母和孩子的压力都很大。", "Passage 3: Chinese parents believe that children will have a good future only with a good education, so they value children’s grades; besides finding ways to get their children into a good school district and sending them to tutoring after class, to cultivate their children’s special talents they also send them to all kinds of interest classes, so in China both parents and children are under great pressure."),
      ("九零后、零零后出生的孩子多半是独生子女，这一代人由于学习条件比较好，而且从小生活在信息发达的世界，所以能力强，目标高，在想法上也比较先进，他们不满足于传统的工作，觉得要做就要做最好的，所以很多人自己创业，当上了老板。", "Passage 4: Most children born in the 1990s and 2000s are only children. Because their learning conditions are rather good and they grew up in a world of advanced information, this generation is capable, has high goals and is also rather progressive in its thinking; they are not content with traditional jobs, feeling that if they do something they should do it best, so many start their own businesses and become bosses. (the book writes 90 后 and 00 后 with digits)")]
TR = [("网红是现在很热门的新职业。他们在网上直播，和粉丝互动，粉丝会打赏他们，他们还可以带货，所以很多人靠这个赚钱。", "Activity 3E (my sample paragraph; the book gives only the word list 带货 互动 赚钱 电竞 反应 网红 打赏 职业比赛): Internet celebrity is a very popular new profession today. They live-stream online and interact with fans, the fans tip them, and they can also sell goods, so many people make money this way.")]
L2 = lesson(
    "Lesson 30 Vocabulary Review: four passages with word banks",
    "确认 追踪 下单 发票 智能 便利 · 适应 陪读 · 学区 补习 特长 · 创业 先进 独生子女 · 热门新职业",
    requires=[],
    cards=[
        card("Vocabulary Review, Activity 3 (Reading, Speaking, Listening, and Writing)",
             "A. Pair up. Student A reads Passage 1 and Passage 2. Student B reads Passage 3 and Passage 4. Complete the sentences as you read. B. Student A partners work as a group together and check their answers, and Student B partners work as a group together and check their answers. C. Students return to their original group and read their two passages without showing them to their partners. Their partners take notes and interpret what they hear. D. Students read the passages they have not read and check their answers. E. Select at least five words from the following list and write a short paragraph about a trendy new profession. 热门新职业: 带货 | 互动 | 赚钱 | 电竞 | 反应 | 网红 | 打赏 | 职业比赛. The word banks and my completed passages:",
             tables=[W1], examples=[D(z, e) for z, e in PS + TR]),
    ],
    exercises=[
        F("利用网路平台订餐很容易，你得先___，然后确认你的信息。", "下单", ["付款", "收货", "送餐"], "下单: place an order."),
        F("餐点送到前你还可以定位___。", "追踪", ["确认", "发送", "安装"], "追踪: track."),
        F("这样的智能科技给我们的生活带来了很大的___。", "便利", ["发票", "优势", "目标"], "便利: convenience."),
        F("为了让自己更有___，以后能找到理想的工作，很多人选择出国留学。", "优势", ["发票", "便利", "特长"], "优势: advantage."),
        F("有些父母会跟着孩子到国外去___，照顾他们。", "陪读", ["补习", "创业", "追踪"], "陪读: accompany a child’s studies."),
        F("中国的父母相信，孩子有好的教育才会有好的___。", "将来", ["特长", "学区", "发票"], "将来: future."),
        F("为了培养孩子的___，还送孩子去上各种兴趣班。", "特长", ["学区", "将来", "优势"], "特长: special talent."),
        F("这一代人从小生活在信息___的世界。", "发达", ["先进", "创业", "满足"], "发达: developed."),
        F("他们不___于传统的工作，所以很多人自己创业。", "满足", ["适应", "重视", "培养"], "满足: be content with."),
        M("Which word means “only child”?", "独生子女", ["多半", "先进", "目标"], "独生子女: only child."),
    ],
)

# ------------------------------------------------------------------ 3. activity 4 key sentences
KS = [("快递员的生活就跟打仗似的，每天要送好几百单，连喝水的时间都没有。", "Activity 4E, 1 (key sentences from the presentations; translations mine): A courier’s life is just like fighting a battle; he has to deliver several hundred orders a day, with not even time to drink water."),
      ("“滴滴出行”可以根据乘客需要，提供特别的服务，他们甚至还有代驾服务呢！", "2: DiDi Chuxing can provide special services according to passengers’ needs; they even have a designated-driver service!"),
      ("只要动动手指，滑动一下页面，看看照片和用户评价，很快就可以选择到满意的民宿。", "3: Just move your fingers, swipe the page, and look at the photos and user reviews, and you can quickly choose a homestay you are satisfied with."),
      ("最近有六百年历史的故宫也在网上直播，让更多的年轻人了解古代文物，爱上传统文化。", "4: Recently the Forbidden City, with six hundred years of history, has also been live-streamed online, letting more young people learn about ancient cultural relics and fall in love with traditional culture."),
      ("随着电竞职业的出现，人们认识到电子游戏是一种很好的智力活动，还能训练合作和反应力。", "5: With the appearance of the e-sports profession, people have come to see that video games are a good mental activity that can also train cooperation and reaction."),
      ("你有没有注意到九零后零零后的年轻人排队时不大会加塞儿，坐公交时还主动给老人让座？", "6: Have you noticed that young people born in the 1990s and 2000s don’t often cut in line when queuing and even actively give up their seats to old people on the bus? (the book writes 90 后 00 后 with digits)"),
      ("培养兴趣对孩子的发展很有好处，而且有了特长，在升学考试的时候还可以加分。", "7: Cultivating interests is very good for a child’s development, and with a special talent one can also gain extra points in entrance exams."),
      ("很多父母觉得国内的学习环境比不上国外，所以只要付得起学费、生活费都会把孩子送出国留学。", "8: Many parents feel that the learning environment at home is no match for that abroad, so as long as they can afford the tuition and living costs they will send their child abroad to study.")]
L3 = lesson(
    "Lesson 30 Vocabulary Review: key sentences from the presentations",
    "跟打仗似的 · 代驾服务 · 动动手指 · 故宫直播 · 电竞 · 加塞儿 · 加分 · 比不上国外 · 付得起学费",
    requires=[],
    cards=[
        card("Vocabulary Review, Activity 4 (Listening, Speaking, and Reading)",
             "A. Listen to the questions and answer them using your knowledge and what you learned from the presentations (six audio questions, so no key). B. Pair up. Students exchange information in Chinese. C. Listen to the following key sentences from presentations and translate them (eight audio items). D. Pair up. Students take turns saying the sentences in Chinese using their translations from Step C. E. Read the scripts aloud with your partner to confirm your answers. The scripts:",
             examples=[D(z, e) for z, e in KS]),
    ],
    exercises=[
        M("What is a courier’s life compared to?", "Fighting a battle", ["A holiday", "A dance", "A picnic"], "就跟打仗似的."),
        M("What can DiDi Chuxing even provide, per the sentence?", "A designated-driver service", ["A cooking service", "A hotel", "A school"], "还有代驾服务呢."),
        M("How can you choose a homestay quickly?", "Look at photos and user reviews with a few finger taps", ["Call each owner", "Visit each place", "Ask neighbors"], "动动手指，滑动一下页面，看看照片和用户评价."),
        M("What has been live-streamed online lately?", "The Forbidden City", ["The Great Wall", "A concert", "A match"], "故宫也在网上直播."),
        M("What can electronic games train, per the sentence?", "Cooperation and reaction", ["Only eyesight", "Cooking", "Singing"], "还能训练合作和反应力."),
        M("What do young people born in the 1990s and 2000s not often do?", "Cut in line", ["Queue", "Take the bus", "Give up seats"], "排队时不大会加塞儿."),
        M("What is an advantage of having a special talent?", "Extra points in entrance exams", ["No exams", "Free food", "Longer holidays"], "在升学考试的时候还可以加分."),
        M("Why do many parents send children abroad, per the sentence?", "They feel the learning environment at home is no match", ["It is cheaper", "They want a holiday", "It is a law"], "国内的学习环境比不上国外."),
        F("快递员的生活就跟打___似的。", "仗", ["球", "架", "牌"], "打仗: fight a battle."),
        F("培养兴趣对孩子的发展很有好___。", "处", ["事", "人", "点"], "好处: benefit."),
    ],
)

# ------------------------------------------------------------------ 4. activity 5 scripts, activity 6
SC = [("很多留学生觉得国内的工资待遇比不上国外，所以选择在国外生活下去，但是随着国内经济发展越来越快，也有很多优秀的人才学到国外的经验后回国创业。", "Activity 5B, 1 (scripts; translations mine): Many international students feel that domestic pay and treatment are no match for those abroad, so they choose to keep living abroad, but as the domestic economy develops faster and faster, many outstanding talents also return home to start businesses after learning from foreign experience."),
      ("由于带着宠物出门很麻烦，有越来越多主人选择出游时把宠物寄养在宠物旅馆。这些旅馆除了照顾宠物的吃住以外，也可以帮你安排带宠物散步、帮宠物洗澡等服务，非常方便。", "2: Because going out with a pet is troublesome, more and more owners choose to board their pets at pet hotels when traveling. Besides looking after the pets’ food and lodging, these hotels can also arrange services such as walking the pet and bathing it, which is very convenient."),
      ("到博物馆参观，为了节省排队的时间，很多人会先在网上订票。到了博物馆，为了更了解每件展品，有些人还会请人专门介绍，几个小时下来，大家都觉得学到很多东西。", "3: When visiting a museum, to save time queuing many people book tickets online first. At the museum, to understand each exhibit better, some people also ask someone to give a special introduction, and after several hours everyone feels they have learned a lot."),
      ("对多半的美国父母来说，虽然学习成绩很重要，但是培养孩子独立生活、解决问题的能力更重要，所以常常会让孩子在下课后或是放暑假的时候到外面去打工。", "4: For most American parents, although grades are important, cultivating a child’s ability to live independently and solve problems is more important, so they often let their children go out to work after class or during summer vacation."),
      ("为了保护环境，现在有越来越多的人选择骑自行车上班或上课。很多城市也提供共享单车，让人们可以用手机或是信用卡轻松租到，因此骑自行车在城里游览也成了年轻游客的新选择。", "5: To protect the environment, more and more people now choose to bike to work or class. Many cities also provide shared bikes that people can easily rent with a phone or a credit card, so touring the city by bike has also become a new choice for young tourists."),
      ("对中国父母来说，买房子除了看房子的条件，交通、环境以外，房子的地点是不是在好的学区内也很重要。所以学区越好的房子也越贵，但是为了孩子，很多家长觉得花这笔钱值得！", "6: For Chinese parents, besides the condition of the house, traffic and environment, whether the house’s location is in a good school district is also very important. So the better the school district, the more expensive the house, but for their children many parents feel this money is well spent!")]
L4 = lesson(
    "Lesson 30 Vocabulary Review: dialogs, six short passages and the board game",
    "留学生创业 · 宠物旅馆 · 博物馆订票 · 美国父母 · 共享单车 · 学区房 · 值得",
    requires=[],
    cards=[
        card("Vocabulary Review, Activity 5 (Listening, Speaking, and Reading)",
             "A. Listen to the dialogs and answer the questions. Dialog 1: 1. What did the first speaker propose? 2. What was the second speaker’s opinion about the first speaker’s proposal? Dialog 2: 1. What was the first speaker’s comment? 2. How did the second speaker feel about the first speaker’s comment? Dialog 3: 1. What did the parents decide to do? 2. What was the daughter’s opinion? Dialog 4: 1. What problem did the first speaker encounter? 2. What did the second speaker say about the situation? Dialog 5: 1. What did the first speaker think of the second speaker’s job? 2. What was the second speaker’s reply? Dialog 6: 1. What is “Chibo”? 2. What was the second speaker’s comment about it? (The dialogs are audio, so I give no key.) B. Listen to the short passages, paying attention to the connection between each unit of meaning to understand the entire picture, and then translate them (six audio items). Read the scripts aloud to confirm your answers. The scripts:",
             examples=[D(z, e) for z, e in SC]),
        card("Vocabulary Review, Activity 6 (Reading, Speaking, and Listening): the board game", "Form groups of three. Each member will roll the die and move their marker the number of spaces shown on the die and answer the question in that space. Answer in complete sentences. Some spaces may require you to say more than one sentence. If your marker falls on a purple space, you can pick any topic to speak about. If your marker falls on an orange space, your partner chooses a question for you. (The board with its questions is a picture and is not included.)"),
    ],
    exercises=[
        M("Why do many international students stay abroad, per script 1?", "They feel domestic pay and treatment are no match for abroad", ["They like winter", "They have no passports", "They hate home"], "国内的工资待遇比不上国外."),
        M("What do outstanding talents do as the domestic economy grows, per script 1?", "Return to start businesses after learning foreign experience", ["Stop working", "Move to villages", "Become tourists"], "学到国外的经验后回国创业."),
        M("Why do more owners board pets at pet hotels?", "Going out with pets is troublesome", ["Pets dislike travel", "Hotels are free", "Pets are sick"], "带着宠物出门很麻烦."),
        M("Why do many people book museum tickets online first?", "To save time queuing", ["It is free", "To win prizes", "It is required by law"], "为了节省排队的时间."),
        M("What do most American parents think more important than grades, per script 4?", "Cultivating independent living and problem-solving ability", ["Money", "Sports", "Travel"], "培养孩子独立生活、解决问题的能力更重要."),
        M("Why do more people bike to work or class, per script 5?", "To protect the environment", ["To save money only", "To lose weight", "Because of traffic fines"], "为了保护环境."),
        M("What is also important when Chinese parents buy a home, per script 6?", "Whether it is in a good school district", ["How tall the building is", "The color of the door", "The floor number"], "房子的地点是不是在好的学区内也很重要."),
        F("为了节省排队的时间，很多人会先在网上订___。", "票", ["饭", "书", "房"], "订票: book tickets."),
        F("学区越好的房子也越贵，但是为了孩子，很多家长觉得花这笔钱值___！", "得", ["不", "到", "了"], "值得: worth it."),
        F("很多城市也提供共享单___，让人们可以用手机轻松租到。", "车", ["子", "位", "站"], "单车: bicycle."),
    ],
)

UNIT = unit("第三十课 复习课 Unit 5 Review: 词汇复习", [L1, L2, L3, L4])
