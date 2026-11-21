"""Unit 98: Lesson 29 (Education in China), Presentation 3, first half: Getting Started, the passage on 留守儿童 and 流动儿童, Activities 1-4 and the Grammar and Usage section
(只好, 只好 vs. 得, Verb + 不起, 比不上, 比不上 vs. 没有).
Audio and pictures are not included; the traditional-character copy of the passage is not repeated; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('挣的钱', 0, 'zheng4'), ('挣了钱', 0, 'zheng4'), ('挣学费', 0, 'zheng4'), ('上不了', 2, 'liao3'), ('还得到地里', 1, 'dei3'), ('还给弟弟', 0, 'hai2'), ('重庆', 0, 'chong2')):
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

# ------------------------------------------------------------------ 1. presentation 3 text and activities 1-3
GS3 = ("Pair up. Discuss the following questions with your partner. A. Is there any difference between rural and urban education in the United States? B. In the United States, does the quality of teaching vary greatly from school to school? What determines the difference? C. In the United States, what are the rules that determine which students can attend school? D. Have you ever faced any difficulties that affected your ability to study? Name one. (The four pictures are not included; the book gives no answers.)")
P3 = [("在中国，很多农村人到大城市去打工。他们工作很辛苦，挣的钱也不多，很难让全家人一起在城里生活，只好把孩子留在农村。这些孩子就成了“留守儿童”。现在中国有几千万留守儿童，他们的父母都在城市打工，常常一年才能见一次面。因为父母不在身边，这些孩子在学习和生活上都有很多困难。有些小孩得自己做饭，到地里干活，有的还要照顾弟弟妹妹，很少有时间学习，而且学习上有了困难也没有人帮助。", "In China, many rural people go to big cities to work. They work very hard and don’t earn much; it is very hard for the whole family to live together in the city, so they have no choice but to leave their children in the countryside. These children have become “left-behind children.” Now China has tens of millions of left-behind children; their parents all work in cities and often can meet only once a year. Because their parents are not at their side, these children have many difficulties in study and life. Some children have to cook for themselves and work in the fields, some also have to look after younger brothers and sisters, have little time to study, and when they have difficulty in their studies, nobody helps them. (translations mine; the traditional-character copy is not repeated)"),
      ("也有的农村孩子跟着父母一起来到城市，成为“流动儿童”。因为他们不是那些城市的居民，所以上不了那里的学校。虽然有的学校可以让他们上学，可是学费很贵，他们上不起。有些人开办了学校，专门收“流动儿童”。这些学校学费不太贵，不过教学质量不太好，有的还比不上农村的学校。", "Some rural children also follow their parents to the city and become “migrant children.” Because they are not residents of those cities, they cannot attend school there. Although some schools let them attend, the tuition is very expensive and they cannot afford it. Some people have set up schools that specially admit “migrant children.” These schools’ tuition is not too expensive, but the quality of teaching is not very good, and some are even no match for rural schools."),
      ("在中国，“留守儿童”和“流动儿童”的教育是一个很大的问题，现在大家正在想办法解决。", "In China, the education of “left-behind children” and “migrant children” is a very big problem, and everyone is now trying to find ways to solve it.")]
A1 = [("留守儿童和流动儿童。", "Activity 1A-1 (my answers; the book gives none): The left-behind children and the migrant children."),
      ("他们都是农村人到大城市打工带来的孩子，在教育上都有困难。", "1A-2: Both come from rural families whose parents go to big cities to work, and both have difficulties with education."),
      ("农村人到大城市去打工，工作辛苦，挣钱不多，很难让全家人一起在城里生活，只好把孩子留在农村，这些孩子就成了留守儿童。", "1B-1: Rural people go to big cities to work; the work is hard and the pay low, it is hard for the whole family to live in the city, so they leave their children in the countryside and the children become left-behind children."),
      ("因为他们工作很辛苦，挣的钱也不多，很难让全家人一起在城里生活。", "1B-2: Because they work very hard, don’t earn much, and it is hard for the whole family to live in the city together."),
      ("有些小孩得自己做饭，到地里干活，有的还要照顾弟弟妹妹，很少有时间学习，学习上有了困难也没有人帮助。", "1B-3: Some have to cook for themselves, work in the fields, or look after younger siblings; they have little time to study and nobody helps with difficulties."),
      ("有的农村孩子跟着父母一起来到城市，成为流动儿童。", "1B-4: Some rural children come to the city with their parents and become migrant children."),
      ("他们不是城市的居民，上不了那里的学校；有的学校学费很贵，他们上不起；专门收他们的学校教学质量不太好。", "1B-5: They are not city residents and can’t attend schools there; some schools’ tuition is too expensive; and the schools that specially take them have poor teaching quality.")]
A2T = table(["Aspect", "My notes for retelling (the book gives an empty three-column table)"], [["The Emerging of 留守儿童", "农村人去大城市打工，挣钱不多，没办法一起生活，只好把孩子留在农村"], ["Difficulties Facing 留守儿童", "自己做饭，到地里干活，照顾弟弟妹妹，很少有时间学习，学习上没人帮助"], ["Difficulties Facing 流动儿童", "上不了城市的学校，学费很贵上不起，专门收他们的学校教学质量不太好"]], title="Activity 2: Retelling the presentation from three aspects")
JR = ("我六岁多的时候，爸爸妈妈就出去打工了，那时候，弟弟才三岁。我们跟爷爷奶奶生活在一起。爸爸妈妈每年春节的时候会回来看我们，给我们买好多好吃的东西、好看的衣服，还给弟弟买玩具。我喜欢这些东西，但是我更希望全家人在一起。爷爷奶奶身体都不太好，但是他们还得到地里去干活。有几个月奶奶病了，我放学以后就做饭，弟弟去帮爷爷干活。我们的学校离家很远，要走一个小时。我每天带弟弟一起去上学。弟弟不会做的作业，我就帮他，但是我不会做的作业，就没有人帮我了。我有困难的时候就会更想爸爸妈妈，他们如果在家就好了。但是，学校里有好多同学都和我们一样，爸爸妈妈都在外面打工，还有的学生自己也出去打工了。我想好好上学，以后挣了钱给爸爸妈妈，他们就不用到那么远的地方去工作了。",
      "Activity 3C, a journal entry of a migrant worker’s daughter: When I was a little over six, my parents went out to work; my little brother was only three then. We live with our grandparents. Every Spring Festival my parents come back to see us, buying us lots of good things to eat and nice clothes, and toys for my brother. I like these things, but I would rather have the whole family together. My grandparents are both in poor health, but they still have to go work in the fields. For several months Grandma was ill; after school I cooked, and my brother went to help Grandpa. Our school is far from home, a one-hour walk. Every day I take my brother to school. If my brother can’t do his homework I help him, but when I can’t do mine, nobody helps me. When I have difficulties I miss my parents even more; if only they were home. But many classmates at school are like us, with both parents working outside, and some students go out to work themselves. I want to study hard and, when I earn money later, give it to my parents so they won’t need to work so far away. (translation mine; the book writes six and three in Chinese)")
JA = [("爸爸妈妈每年春节回来看他们，给他们买好吃的东西、好看的衣服，还给弟弟买玩具。她喜欢这些东西，但是更希望全家人在一起。", "Activity 3C-1 (my answer): Her parents come back every Spring Festival and buy tasty food, nice clothes and toys for her brother; she likes them but would rather have the whole family together."),
      ("奶奶病的时候她放学以后做饭，每天带弟弟一起去上学，还帮弟弟做作业。", "3C-2: When Grandma was ill she cooked after school; every day she takes her brother to school and helps him with his homework."),
      ("学校离家很远，要走一个小时；她不会做的作业没有人帮她；有困难的时候她更想爸爸妈妈。", "3C-3: The school is far, a one-hour walk; nobody helps with homework she can’t do; with difficulties she misses her parents more."),
      ("学校里有好多同学都和他们一样，爸爸妈妈都在外面打工，还有的学生自己也出去打工了。", "3C-4: Many classmates are the same, with both parents working outside, and some students even go out to work themselves."),
      ("她希望好好上学，以后挣了钱给爸爸妈妈，让他们不用到那么远的地方去工作。", "3C-5: She wishes to study hard and later earn money to give her parents, so they don’t have to work so far away.")]
L1 = lesson(
    "Lesson 29 Presentation 3: left-behind children and migrant children",
    "留守儿童 · 流动儿童 · 打工 · 农村 · 照顾弟弟妹妹 · 上不起 · 比不上农村的学校 · 想办法解决",
    requires=[],
    cards=[
        card("Presentation 3: Getting Started", GS3),
        card("Presentation 3: 留守儿童 and 流动儿童", "A passage about the education of the children of rural migrant workers.", examples=[D(z, e) for z, e in P3]),
        card("Presentation 3 Activities, Activities 1 to 3",
             "Activity 1 (Listening): A. Global Listening: Listen to Presentation 3 once and answer the questions. 1. Who are the two groups of children mentioned in the article? 2. What do these two groups of children have in common? B. Detailed Listening: Listen to Presentation 3 again and answer the questions. 1. How did the “left behind children” come about? 2. Why can’t most migrant workers bring their children to live with them in the city? 3. What difficulties are faced by these children? Provide examples. 4. How did migrant children emerge? 5. What difficulties do the migrant children have with school? Activity 2 (Speaking and Listening): Form groups of three. Each member retells the presentation from one of the following three aspects. Activity 3 (Listening, Reading, and Speaking): A. Listen to a migrant worker’s monolog and answer the questions: 1. What do you know about the family of this migrant worker? 2. What are the reasons that he leaves his kids at home? Name three. 3. What was said about the schools in the city for the migrant workers’ children? 4. How does he save money? 5. What goal does he hope to achieve? (audio, so I give no key) B. Pair up. Discuss your answers with your partner. C. Read a journal entry of a migrant worker’s daughter and answer the questions: 1. Describe the scene when her parents come back to visit. How does the girl feel about it? 2. What are the girl’s responsibilities when the parents are away from home? 3. What difficulties does she have to deal with? 4. What does she say about the children’s life in that area? 5. What does she wish for in the future? D. Pair up. Discuss your answers with your partner. The journal entry and my answers:",
             tables=[A2T], examples=[D(z, e) for z, e in A1] + [D(*JR)] + [D(z, e) for z, e in JA]),
    ],
    exercises=[
        M("Why do rural parents leave their children in the countryside?", "It is hard for the whole family to live in the city", ["The city has no work", "The children want to farm", "Schools are free in the countryside"], "很难让全家人一起在城里生活，只好把孩子留在农村."),
        M("What are these children called?", "Left-behind children (留守儿童)", ["Migrant children", "City children", "Boarding children"], "这些孩子就成了留守儿童."),
        M("How often can left-behind children often see their parents?", "About once a year", ["Every day", "Every week", "Every month"], "常常一年才能见一次面."),
        M("What do some left-behind children have to do?", "Cook for themselves and work in the fields", ["Go to boarding school", "Take care of pets", "Drive trucks"], "有些小孩得自己做饭，到地里干活."),
        M("What are “migrant children” (流动儿童)?", "Rural children who follow parents to the city", ["Children who move between schools", "Children of teachers", "City children who move to villages"], "跟着父母一起来到城市."),
        M("Why can migrant children often not go to city schools?", "They are not residents of those cities", ["They are too young", "They dislike study", "The schools are too far"], "他们不是那些城市的居民，所以上不了那里的学校."),
        M("What is said about the schools that specially admit migrant children?", "Tuition is not too high but teaching quality is poor", ["Tuition is very high", "Teaching quality is the best", "They are free"], "学费不太贵，不过教学质量不太好."),
        M("What does the girl in the journal entry wish for?", "To study hard, earn money, and spare her parents far-away work", ["To become a doctor abroad", "To stop school", "To leave the village alone"], "以后挣了钱给爸爸妈妈，他们就不用到那么远的地方去工作了."),
        F("很难让全家人一起在城里生___，只好把孩子留在农村。", "活", ["命", "产", "存"], "生活: live."),
        F("这些孩子就成了“留守儿___”。", "童", ["子", "女", "孩"], "儿童: children."),
        F("有些小孩得自己做___，到地里干活。", "饭", ["菜", "衣", "家"], "做饭: cook."),
    ],
)

# ------------------------------------------------------------------ 2. activity 4 and 只好
A4T = table(["Group", "Sentence with the blank", "Answer (my key; the book gives none)"], [
    ["打工，干活儿，工作", "为了增加收入，很多农民到大城市＿＿。", "打工"],
    ["打工，干活儿，工作", "妈妈＿＿很快，一会儿就把家里收拾得干干净净。", "干活儿"],
    ["留在，留守，留下，留学", "这次旅行给我＿＿了美好的回忆。", "留下"],
    ["留在，留守，留下，留学", "很多人毕业以后＿＿国外生活工作。", "留在"],
    ["专门，专家，专线，专递", "这个菜是＿＿为你做的，快尝尝吧！", "专门"],
    ["专门，专家，专线，专递", "有一条地铁＿＿直接从市中心开到机场。", "专线"],
    ["开办，创办，补办", "我的护照丢了，我得去＿＿一个。", "补办"],
    ["开办，创办，补办", "我们学校＿＿了一个家长学习班，让父母更好地关心孩子的身心健康。", "开办"],
    ["帮，帮助，帮忙，帮手", "朋友就是在你困难的时候＿＿你的人。", "帮助"],
    ["帮，帮助，帮忙，帮手", "你可以＿＿我买一杯咖啡吗。", "帮"],
    ["帮，帮助，帮忙，帮手", "上次他＿＿了我一个大＿＿。（choose the one in VO pattern）", "帮、忙"]],
    title="Activity 4 (Reading): complete the sentences with the words from each group")
A4D = [("为了增加收入，很多农民到大城市打工。", "Activity 4, 1 (completed sentences; translations mine): To increase their income, many farmers go to big cities to work."), ("妈妈干活儿很快，一会儿就把家里收拾得干干净净。", "Mom works fast; in a little while she has the house spotlessly tidy."),
       ("这次旅行给我留下了美好的回忆。", "2: This trip left me with beautiful memories."), ("很多人毕业以后留在国外生活工作。", "Many people stay abroad to live and work after graduating."),
       ("这个菜是专门为你做的，快尝尝吧！", "3: This dish was made specially for you; try it quickly!"), ("有一条地铁专线直接从市中心开到机场。", "There is a dedicated subway line running directly from downtown to the airport."),
       ("我的护照丢了，我得去补办一个。", "4: My passport is lost; I have to go get a replacement."), ("我们学校开办了一个家长学习班，让父母更好地关心孩子的身心健康。", "Our school has started a parents’ study class so parents can better care about their children’s physical and mental health."),
       ("朋友就是在你困难的时候帮助你的人。", "5: A friend is someone who helps you when you are in difficulty."), ("你可以帮我买一杯咖啡吗？", "Can you buy a cup of coffee for me?"), ("上次他帮了我一个大忙。", "Last time he did me a big favor.")]
ZH1 = [("家里没有饭了，我只好吃了点儿零食。", "只好 (Unfavorable condition, (Subj.) + 只好 + verb phrase; “no other choice but,” “be resigned to do something”), 1: There was no food at home, so I had no choice but to eat some snacks. (translations mine)"), ("高铁票卖完了，我只好坐普通火车。", "2: The high-speed rail tickets were sold out, so I had to take a regular train."), ("我的车坏了，只好走回家。", "3: My car broke down, so I had to walk home."), ("看比赛的人太多了，我找不到座位，只好站着看。", "4: There were too many people watching the match; I couldn’t find a seat, so I had to watch standing.")]
ZH2 = [("没有医保卡也可以，但你得付现金。", "只好 vs. 得 (只好 expresses a passive decision and has to be used with a condition; 得 usually indicates a voluntary decision or is reminding/urging others to do something and can be used independently without pre-conditions), 1: It’s fine without a medical insurance card, but you have to pay cash."), ("因为没有医保卡，我只好付现金看医生。", "2: Because I had no medical insurance card, I had to pay cash to see the doctor."), ("有些小孩得自己做饭。", "3: Some children have to cook for themselves."), ("爸爸妈妈都在外打工，爷爷奶奶又病了，孩子只好自己做饭。", "4: Both parents work away, and the grandparents are also ill, so the child has no choice but to cook for himself.")]
Z1A = [("我的右手受伤了，只好用左手写字。", "Activity 1A, 1 (my completions): My right hand was hurt, so I had to write with my left hand."), ("专家门诊的号已经挂完了，只好看普通门诊。", "2: The specialist clinic appointments were all booked, so I had to go to the regular clinic."), ("我跟他约好三点见面，可是他三点半还没有来，只好给他打电话。", "3: I arranged to meet him at three, but he hadn’t come by half past, so I had to call him."), ("老张病了，没有办法继续工作，只好请假回家休息。", "4: Lao Zhang was ill and couldn’t continue working, so he had to take leave and rest at home."),
       ("我的护照丢了，只好去办一个新的。", "5: My passport was lost, so I had to go get a new one."), ("出了门才想起来没带手机，只好回家去拿。", "6: Only after going out did I remember I hadn’t brought my phone, so I had to go home to get it."), ("我们想去海边跑步，可是风太大了，只好在家里看电视。", "7: We wanted to run at the seaside, but the wind was too strong, so we had to watch TV at home."), ("最近工作太多了，上班的时候根本做不完，只好带回家做。", "8: Recently there is too much work; I can’t finish it at all during work hours, so I have to take it home.")]
Z1B = [("我没有带书，只好看同学的书。", "Activity 1B, 1 (my answers): I didn’t bring my book, so I had to read my classmate’s."), ("我的车在路上坏了，只好打电话叫拖车。", "2: My car broke down on the road, so I had to call a tow truck."), ("我没带钱包，只好用手机付钱。", "3: I didn’t bring my wallet, so I had to pay with my phone."), ("我只好自己打工挣学费。", "4: I would have no choice but to work myself to earn tuition."), ("我只好戴上耳机睡觉。", "5: I had to put on earphones to sleep. (the book writes 12 点 in digits)")]
Z1C = ("在中国，很多农村人到大城市去打工。他们工作很辛苦，挣的钱也不多，很难让全家人一起在城里生活，只好把孩子留在农村。", "Activity 1C, the book’s sample mini paragraph (precondition + difficulties + 只好 + unwanted decision): In China, many rural people go to big cities to work. They work very hard and don’t earn much; it is very hard for the whole family to live together in the city, so they have no choice but to leave their children in the countryside.")
L2 = lesson(
    "Lesson 29 Presentation 3 activity 4 and grammar: 只好 and 只好 vs. 得",
    "打工 · 干活儿 · 留下 · 专门 · 专线 · 补办 · 开办 · 帮了我一个大忙 · 只好 + verb phrase · 只好 vs. 得",
    requires=[],
    cards=[
        card("Activity 4 (Reading): word choice", "Complete the sentences with the words from each group. My key and the completed sentences:", tables=[A4T], examples=[D(z, e) for z, e in A4D]),
        card("The 只好 + Verb Phrase structure, and 只好 vs. 得",
             "In this structure, 只好 means “no other choice but,” or “be resigned to do something.” Unfavorable condition, (Subj.) + 只好 + verb phrase. 只好 expresses a passive decision and has to be used with a condition. 得 usually indicates a voluntary decision or is reminding/urging others to do something. 得 can be used independently without pre-conditions. Activity 1: A. Complete the sentences with the 只好 + verb phrase structure (the beginnings: 1. 我的右手受伤了， 2. 专家门诊的号已经挂完了， 3. 我跟他约好三点见面，可是他三点半还没有来， 4. 老张病了，没有办法继续工作， 5. 我的护照丢了， 6. 出了门才想起来没带手机， 7. 我们想去海边跑步，可是风太大了， 8. 最近工作太多了，上班的时候根本做不完，). B. Answer the questions using 只好: 1. 上课的时候你没有带书，怎么办？ 2. 你的车在路上坏了，怎么办？ 3. 请朋友吃饭，吃完才发现自己没带钱包，怎么办？ 4. 你的父母没有钱为你付大学的学费，怎么办？ 5. 已经晚上十二点了，旁边住的人还在聚会，唱歌，怎么办？ C. Pair up. Talk with your partner about times you had to make choices you were reluctant to make but were resigned to. Follow the structure of the sample mini paragraph. The examples and my answers:",
             examples=[D(z, e) for z, e in ZH1 + ZH2 + Z1A + Z1B] + [D(*Z1C)]),
    ],
    exercises=[
        M("What does 只好 mean?", "No other choice but; be resigned to doing something", ["Only good", "Happily", "Perhaps"], "only choice, resigned."),
        M("What does 只好 need in the sentence?", "An unfavorable condition", ["A question", "A number", "A date"], "has to be used with a condition."),
        M("Which usually indicates a voluntary decision or urging?", "得", ["只好", "不起", "比不上"], "得 usually indicates a voluntary decision or is reminding/urging."),
        M("What does 高铁票卖完了，我只好坐普通火车 mean?", "The tickets were sold out, so I had to take a regular train", ["I love regular trains", "The trains are free", "I missed the train"], "只好坐普通火车."),
        M("What does 没有医保卡也可以，但你得付现金 mean?", "It’s fine without the card, but you have to pay cash", ["Cash is not accepted", "You can’t pay", "The card is free"], "你得付现金."),
        M("Which sentence is complete with a condition?", "我的车坏了，只好走回家", ["我只好走回家", "只好我走", "我要走回家了"], "condition + 只好."),
        M("Which word fits “上次他___了我一个大忙”?", "帮", ["专", "留", "开"], "帮了我一个大忙."),
        M("Which means “start (a school)”?", "开办", ["补办", "专线", "留下"], "开办了学校."),
        F("看比赛的人太多了，我找不到座位，只好站___看。", "着", ["了", "过", "的"], "站着看: watch standing."),
        F("我的护照丢了，我得去补___一个。", "办", ["做", "买", "拿"], "补办: replace."),
        F("这个菜是专___为你做的，快尝尝吧！", "门", ["线", "家", "业"], "专门: specially."),
    ],
)

# ------------------------------------------------------------------ 3. 不起
BQT = table(["", "Pattern"], [["Affirmative Form", "Verb + 不起 (+ Obj.)"], ["Negative Form", "Verb + 得起 (+ Obj.)"], ["Affirmative-Negative Form", "Verb + 不 + Verb + 得起 (+ Obj.) or Verb + 得起 + Verb + 不起 (+ Obj.) (as printed)"]], title="Verb + 不起: patterns")
BQ = [("那件衣服是你两个月的工资，你买得起吗？", "Verb + 不起 (commonly used to express affordability, e.g. 买不起 can’t afford to buy, 吃不起 can’t afford to eat), 1: That piece of clothing is two months of your salary; can you afford to buy it? (translations mine)"), ("这家旅馆太贵了，我们住不起。", "2: This hotel is too expensive; we can’t afford to stay."), ("一张票两千块钱，你看不看得起这么贵的演出？", "3: A ticket is two thousand yuan; can you afford to see such an expensive show?"), ("大学的学费那么贵，你付得起付不起？", "4: University tuition is so expensive; can you afford to pay it or not?")]
BQ2 = [("许多美国人买不起健康保险。", "Activity 2B, 1 (translations mine): Many Americans can’t afford health insurance."), ("我家有四只狗，我已经快养不起他们了。", "2: My family has four dogs, and I almost can’t afford to keep them any more."), ("一般的大学生租不起这么贵的房子。", "3: An ordinary university student can’t afford to rent such an expensive home."), ("对那些买不起书又爱看书的人来说，图书馆是一个好地方。", "4: For those who can’t afford books but love to read, the library is a good place."),
       ("我买不起苹果八代，只买得起八袋苹果。", "5: I can’t afford an Apple 8 (a pun on 八代 and 八袋); I can only afford eight bags of apples. (the book writes 8代 and 8袋 with digits)"),
       ("他家很穷，买不起新衣服，吃不起肉，住不起大房子。", "Activity 2C (my sample about a poor person; the book gives none): His family is very poor; they can’t afford new clothes, can’t afford meat, and can’t afford a big house.")]
L3 = lesson(
    "Lesson 29 Presentation 3 grammar: Verb + 不起 (can’t afford)",
    "买不起 · 吃不起 · 住不起 · 上不起 · 买得起 · 付得起付不起 · 养不起",
    requires=[],
    cards=[
        card("Verb + 不起",
             "Verb + 不起 is commonly used to express affordability. For example, 买不起 (can’t afford to buy), or 吃不起 (can’t afford to eat). Activity 2: A. Listen to the sentences and translate what you hear into English (six audio items, so no key). B. Translate the sentences into English. C. Pair up. Imagine a poor person and take turns discussing the person’s life, using the Verb + 不起 phrase. Compare your work with that of another pair. The patterns, examples and my translations:",
             tables=[BQT], examples=[D(z, e) for z, e in BQ + BQ2]),
    ],
    exercises=[
        M("What does 买不起 mean?", "Can’t afford to buy", ["Don’t want to buy", "Bought already", "Can buy anything"], "买不起 (can’t afford to buy)."),
        M("What does 吃不起 mean?", "Can’t afford to eat", ["Can’t eat fast", "Don’t like eating", "Eat too much"], "吃不起 (can’t afford to eat)."),
        M("What is the negative form of Verb + 不起?", "Verb + 得起", ["Verb + 了", "Verb + 过", "Verb + 着"], "Negative Form: Verb + 得起 (as the book labels the contrasting form)."),
        M("What does 这家旅馆太贵了，我们住不起 mean?", "This hotel is too expensive; we can’t afford it", ["We love this hotel", "This hotel is closed", "This hotel is far"], "我们住不起."),
        M("What does 你付得起付不起？ ask?", "Can you afford to pay or not?", ["Did you pay?", "Will you pay later?", "Who pays?"], "你付得起付不起？"),
        M("What does 许多美国人买不起健康保险 mean?", "Many Americans can’t afford health insurance", ["Many Americans sell insurance", "Insurance is free", "Americans buy too much"], "买不起健康保险."),
        M("What do those who can’t afford books but love reading need, per the sentence?", "A library", ["A bookstore", "A bank", "A garden"], "图书馆是一个好地方."),
        F("这家旅馆太贵了，我们住___起。", "不", ["没", "别", "未"], "住不起."),
        F("那件衣服是你两个月的工资，你买___起吗？", "得", ["不", "到", "完"], "买得起."),
        F("一般的大学生租不起这么贵的___子。", "房", ["车", "家", "门"], "房子: house."),
    ],
)

# ------------------------------------------------------------------ 4. 比不上
BBT = table(["", "Pattern"], [["Affirmative", "A 比得上 B"], ["Negative", "A 比不上 B"]], title="比不上 and 比得上")
BS = table(["", "Pattern"], [["没有", "A 没有 B + adjective"], ["比不上", "A 比不上 B"]], title="比不上 vs. 没有: structure")
BU1 = [("这些学校学费不太贵，不过教学质量不太好，有的还比不上农村的学校。", "比不上 (a fixed expression for comparison; an ability or condition that cannot be compared with, no match for something/someone else; A 比得上 B / A 比不上 B), from Presentation 3: These schools’ tuition is not too expensive, but the teaching quality is not very good, and some are even no match for rural schools. (translations mine)"),
       ("没有什么药比得上锻炼。", "1: No medicine can match exercise."), ("你们的演出简直比得上专业的摇滚乐队了。", "2: Your performance can simply rival a professional rock band."), ("重庆的气候比不上蒙特雷。", "3: Chongqing’s climate is no match for Monterey’s.")]
BU2 = [("公交车没有地铁方便。", "比不上 vs. 没有, A. Structure, 1: The bus is not as convenient as the subway."), ("你们公司没有我们公司大。", "2: Your company is not as big as ours."), ("公交车的速度比不上地铁。", "3: The speed of the bus is no match for the subway."), ("你们公司比不上我们公司。", "4: Your company is no match for our company."),
       ("我的能力比不上你。", "B. Meaning (比不上 indicates the inferior of ability or condition, while 没有 can convey inferiority or simply a neutral comparison), 1: My ability is no match for yours."), ("爸爸做的菜没有妈妈做的好吃。", "2: The food Dad makes is not as tasty as what Mom makes."), ("爸爸做的菜比不上妈妈做的。", "= Dad’s cooking is no match for Mom’s."), ("蒙特雷的夏天没有重庆那么热。", "3: Monterey’s summer is not as hot as Chongqing’s.")]
BU3 = [("我有很多地方比不上他们，还需要好好学习和提高。", "Activity 3B, 1 (translations mine): There are many respects in which I am no match for them, and I still need to study hard and improve."), ("老王比不上他的朋友们那么有钱，但他的快乐没人能比得上。", "2: Lao Wang is not as rich as his friends, but nobody can match his happiness."), ("看到别人的好处容易，看到自己的好处难，所以人们常常觉得自己比不上别人。", "3: It is easy to see others’ strengths and hard to see one’s own, so people often feel they are no match for others."), ("没有一个朋友能比得上健康，没有一个敌人能比得上疾病。", "4: No friend can match health, and no enemy can match illness."),
       ("你唱歌没有他唱得好。", "Activity 3C, 1 (my 没有 versions; the book gives none): You don’t sing as well as he does."), ("我的中文水平没有他的高。", "2: My Chinese level is not as high as his."), ("这所学校的教学质量没有城里的学校好。", "3: This school’s teaching quality is not as good as the schools in the city."), ("香港在这方面的发展很慢，甚至没有一些西部城市发展得快。", "4: Hong Kong’s development in this respect is slow, even not as fast as some western cities."),
       ("妈妈以前的生活条件比不上你们的。", "Activity 3D, 1 (my 比不上 versions, where applicable): Mom’s past living conditions were no match for yours."), ("重庆的气候比不上蒙特雷。", "3: Chongqing’s climate is no match for Monterey’s."), ("小文的考试成绩比不上马克的。", "5: Xiaowen’s exam scores are no match for Mark’s."),
       ("超级英雄的力气比得上一百头大象，跑得比得上飞机。", "Activity 3E (my sample for the superhero; the book gives none): The superhero’s strength can match a hundred elephants, and he runs as fast as an airplane.")]
L4 = lesson(
    "Lesson 29 Presentation 3 grammar: 比不上 and 比不上 vs. 没有",
    "比得上 · 比不上 · 没有 + adjective · 能力比不上你 · 比不上农村的学校 · 重庆的气候比不上蒙特雷",
    requires=[],
    cards=[
        card("比不上 and 比不上 vs. 没有",
             "比不上 is a fixed expression to make a comparison. It means an ability or condition that cannot be compared with, or is no match for something/someone else. 比不上 indicates inferiority of ability or condition, while 没有 can convey inferiority or simply a neutral comparison. Activity 3: A. Listen to the sentences and translate what you hear into English (four audio items, so no key). B. Translate the sentences into English. C. Change the following 比不上 comparison into 没有 comparison sentences: 1. 你唱歌比不上他。 2. 我的中文水平比不上他。 3. 这所学校的教学质量比不上城里的学校。 4. 香港在这方面的发展很慢，甚至比不上一些西部城市。 D. Change the following 没有 comparisons into 比不上 comparisons, if applicable: 1. 妈妈以前的生活条件没有你们的好。 2. 学拼音没有学汉字那么难。 3. 重庆的气候没有蒙特雷这么好。 4. 小米手机没有苹果手机贵。 5. 小文的考试成绩没有马克高。 (My judgment: 1, 3 and 5 can change; 2 and 4 are neutral comparisons, so they stay with 没有.) E. In groups of three, imagine a superhero and describe him or her with 比得上. Share your work with the other group and compare the two figures with 比不上. The patterns, examples and my versions:",
             tables=[BBT, BS], examples=[D(z, e) for z, e in BU1 + BU2 + BU3]),
    ],
    exercises=[
        M("What does 比不上 mean?", "Is no match for", ["Is better than", "Is the same as", "Is far from"], "an ability or condition that cannot be compared with."),
        M("What is the affirmative of 比不上?", "比得上", ["比得到", "比不得", "比不到"], "A 比得上 B."),
        M("What does 没有什么药比得上锻炼 mean?", "No medicine can match exercise", ["Exercise is medicine", "Medicine is better", "I have no medicine"], "没有什么药比得上锻炼."),
        M("Which comparison can convey a neutral comparison, not just inferiority?", "没有", ["比不上", "比得上", "不如"], "没有 can convey inferiority or simply a neutral comparison."),
        M("What does 我的能力比不上你 mean?", "My ability is no match for yours", ["My ability is better than yours", "I have no ability", "You have no ability"], "我的能力比不上你."),
        M("Which is equivalent to 爸爸做的菜没有妈妈做的好吃?", "爸爸做的菜比不上妈妈做的", ["爸爸做的菜比得上妈妈做的", "爸爸做的菜比妈妈做的好吃", "爸爸不做菜"], "= 爸爸做的菜比不上妈妈做的."),
        M("What does 公交车没有地铁方便 mean?", "The bus is not as convenient as the subway", ["The bus is more convenient", "There is no subway", "There is no bus"], "A 没有 B + adjective."),
        F("没有一个朋友能比得___健康。", "上", ["下", "到", "来"], "比得上."),
        F("你们的演出简直比得上专业的摇滚乐___了。", "队", ["团", "班", "组"], "乐队: band."),
        F("这些学校教学质量不太好，有的还比不上农村的学___。", "校", ["习", "生", "堂"], "学校: school."),
    ],
)

UNIT = unit("第二十九课 中国的教育 Presentation 3: 留守儿童, 只好, 不起, 比不上", [L1, L2, L3, L4])
