"""Unit 99: Lesson 29 (Education in China), Presentation 3, second part: Skill Integration (left-behind children and statistics, a father's dilemma, a free summer class, a futsal team)
and Using Chinese in Context Activity 1 (农民工).
Audio, video and pictures are not included; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('长大', 0, 'zhang3'), ('村长', 1, 'zhang3'), ('挣不了钱', 0, 'zheng4'), ('挣不了钱', 2, 'liao3'), ('带不了孩子', 2, 'liao3'), ('评为', 1, 'wei2'), ('重庆', 0, 'chong2')):
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

# ------------------------------------------------------------------ 1. skill integration act 1-2
ST = table(["Year", "Statistics (my table from the printed passage, Activity 1C; the book’s table for the audio passage is blank, and the 2010 figures are in the audio, so not included)"], [["二零一八年", "农村留守儿童九百多万；百分之三十的留守儿童一年只能见到父母一到两次；百分之十五的留守儿童一年也见不到父母一次；近百分之九十的留守儿童和爷爷奶奶生活在一起"], ["二零一零年", "(audio only; no key)"]], title="Activity 1A: a table of the statistics")
QB = [("什么是农村留守儿童？", "Activity 1B, 1 (translations mine): What are rural left-behind children?"), ("留守儿童可能面对哪些困难？", "2: What difficulties might left-behind children face?"),
      ("农村留守儿童就是父母去城市打工，自己留在农村的孩子。", "1B-1 (my answer; the book gives none): Rural left-behind children are children whose parents go to work in the city and who stay in the countryside."),
      ("他们可能要自己做饭、干活儿，学习上没有人帮助，安全和身心健康也有问题。", "1B-2 (my answer): They may have to cook and work by themselves, have no help with study, and have safety and physical and mental health problems.")]
LS = ("二零一八年，中国农村留守儿童有九百多万。百分之三十的留守儿童一年只能见到父母一到两次，百分之十五的留守儿童甚至一年也见不到父母一次。由于父母长期不在身边，留守儿童要面对安全、身心健康、教育、甚至是基本生活的难题。近百分之九十的留守儿童和爷爷奶奶生活在一起，爷爷奶奶们年龄比较大，有些身体也不太好。孩子们不仅要照顾自己，有时还要照顾比自己还小的弟弟妹妹们。很多爷爷奶奶也没有读过什么书，大部分连小学都没有读完。而随着孩子一天天长大，在学习和生活上的困难越来越多，爷爷奶奶很难给他们需要的帮助。有些留守儿童甚至根本没有人照顾，他们的安全、教育和身心健康都是急需解决的问题。",
      "Activity 1C: In 2018 China had more than 9 million rural left-behind children. 30 percent of them can see their parents only one or two times a year, and 15 percent cannot even see their parents once a year. Because their parents are away for a long time, left-behind children face difficulties of safety, physical and mental health, education, and even basic living. Nearly 90 percent live with their grandparents, who are relatively old, and some are not in good health. The children not only have to look after themselves, but sometimes also after younger brothers and sisters. Many grandparents have not read much either, and most did not even finish primary school. As the children grow up day by day, their difficulties in study and life increase, and it is hard for the grandparents to give them the help they need. Some left-behind children even have nobody at all to look after them, and their safety, education and physical and mental health are problems in urgent need of solving. (the book writes 2018, 900, 30%, 15% and 90% in digits; translation mine)")
LSA = [("安全，身心健康，教育，基本生活。", "Activity 1C, difficulties (my answer): 1. Safety. 2. Physical and mental health. 3. Education and basic living."),
       ("爷爷奶奶年龄比较大，身体也不太好，没有读过什么书，很难给孩子需要的帮助。", "(my note) The grandparents are old, in poor health and little educated, so it is hard for them to give the children the help they need.")]
L1 = lesson(
    "Lesson 29 Presentation 3 skill integration: left-behind children and statistics",
    "农村留守儿童 · 九百多万 · 见不到父母 · 爷爷奶奶 · 身心健康 · 急需解决的问题",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Reading, Listening, and Speaking)",
             "A. Listen to the following passage and make a table of the statistics (audio). Pair up and compare your work with your partner’s. B. Discuss the following questions with your partner. C. Read the passage and answer the questions: What are the difficulties faced by 留守儿童 in the passage? Compare your answer with your discussion results from Part B, question 2 above. The table, the questions, the passage and my answers:",
             tables=[ST], examples=[D(z, e) for z, e in QB] + [D(*LS)] + [D(z, e) for z, e in LSA]),
        card("Skill Integration, Activity 2 (Listening and Speaking)",
             "Listen to the following passage and complete the tasks. Pair up and compare your answers with those of your partner. 1. Transcribe any unknown words you hear and check their meanings with your dictionary. 2. What kind of present did Li Zhifa receive? Who gave him this gift? 3. Describe Li Zhifa’s family situation. 4. What does Li Zhifa wish for? 5. What do you think the mother says in the phone call? (Audio, so I give no key.)"),
    ],
    exercises=[
        M("How many rural left-behind children were there in China in 2018?", "More than nine million", ["More than ninety", "About nine thousand", "Over nine billion"], "九百多万."),
        M("What share of them see their parents only one or two times a year?", "Thirty percent", ["Three percent", "Ninety percent", "Fifteen percent"], "百分之三十."),
        M("What share cannot see their parents even once a year?", "Fifteen percent", ["Fifty percent", "One percent", "Thirty percent"], "百分之十五."),
        M("Who do nearly ninety percent of left-behind children live with?", "Their grandparents", ["Their teachers", "Their neighbors", "Their uncles"], "和爷爷奶奶生活在一起."),
        M("Which is NOT listed as a difficulty?", "Too much free time", ["Safety", "Education", "Basic living"], "安全、身心健康、教育、基本生活."),
        M("What did many grandparents not do?", "Finish primary school", ["Work", "Cook", "Walk"], "大部分连小学都没有读完."),
        M("What do some left-behind children not even have?", "Anybody to look after them", ["A school", "A home", "A toy"], "根本没有人照顾."),
        F("留守儿童要面对安全、身心健___、教育、甚至是基本生活的难题。", "康", ["身", "心", "体"], "健康: health."),
        F("爷爷奶奶很难给他们需要的帮___。", "助", ["忙", "手", "做"], "帮助: help."),
        F("他们的安全、教育和身心健康都是急需解___的问题。", "决", ["开", "释", "答"], "解决: solve."),
    ],
)

# ------------------------------------------------------------------ 2. skill integration act 3-4
LZ = ("李正华和太太在重庆市打工好几年了，他们在农村老家有一个上五年级的儿子，儿子从小就跟着爷爷奶奶长大。李正华对记者说：“让儿子在家里我们不放心，让他到城里来我们又没有时间照顾他。”他说，儿子读书的学校离家只有二十分钟，上一二年级的时候，儿子每天一放学就回家，可到四年级的时候，每天放学好几个小时以后才回家。原来，儿子每天放学后都到同学家里去玩儿电脑游戏。儿子说：“回家以后没什么好玩的，跟爷爷奶奶也没什么话说，只能跟同学玩儿。”李正华说：“我们也没有办法，带孩子就挣不了钱，挣钱就带不了孩子。”学校的老师也对记者说，学校一般下午两三点就放学了，大部分孩子都不回家，聚在一起玩游戏。",
      "Activity 3: Li Zhenghua and his wife have worked in Chongqing for several years. In their rural hometown they have a fifth-grade son, who has grown up with his grandparents since childhood. Li Zhenghua told a reporter: “Leaving our son at home we don’t feel at ease; bringing him to the city we have no time to look after him.” He said the school where his son studies is only twenty minutes from home. In first and second grade the son came home as soon as school was out, but by fourth grade he came home several hours after school. It turned out that every day after school the son went to a classmate’s home to play computer games. The son said: “After I get home there is nothing fun, and I have nothing to say to my grandparents, so I can only play with classmates.” Li Zhenghua said: “We have no way out either: if we take care of the child, we can’t earn money; if we earn money, we can’t take care of the child.” The school’s teacher also told the reporter that school generally lets out at two or three in the afternoon and most children don’t go home but gather to play games. (translation mine)")
LZA = [("可以请学校的老师在放学以后组织一些活动，让孩子有事做；也可以让爷爷奶奶多跟孩子聊天，或者让孩子到爸爸妈妈打工的城市上学。", "Activity 3, possible solutions (my sample; the book gives no key): The school’s teachers could organize activities after school so children have something to do; the grandparents could talk with the child more, or the child could go to school in the city where the parents work.")]
SV = ("金花村位于重庆山区，这里有很多留守儿童。每次到暑假的时候，孩子们的生活都很没有意思，爷爷奶奶没有办法在学习上帮助他们，更不能带他们去游玩。几年前，重庆大学的几个学生在这里开办了一个免费的留守儿童兴趣班。到现在，重庆大学已经有二百名学生参加了这个活动，附近的二十三个村子都有了免费的暑假兴趣班。孩子们不仅暑假生活更丰富，而且学习上也有了进步。村里有一个叫李晴的孩子，他的爸爸妈妈都在很远的城市打工。六年前他开始参加村里的暑假兴趣班，从那时候起，他就喜欢上了英语，觉得学好英语就可以了解外面的世界。今年高考，李晴考上了四川外语学院。村长说，因为这些大学生，村里很多孩子都有了上大学的愿望。",
      "Activity 4B: Jinhua Village is in the mountain area of Chongqing, and there are many left-behind children here. Every summer vacation the children’s life is very boring; the grandparents have no way to help them with study, much less take them out to play. A few years ago, several students of Chongqing University set up a free interest class for left-behind children here. By now 200 Chongqing University students have taken part in this activity, and 23 nearby villages have free summer interest classes. The children not only have a richer summer vacation but also progress in their studies. A child in the village called Li Qing has parents who both work in a far-away city. Six years ago he began to attend the village summer interest class, and since then he has come to like English, feeling that learning English well lets one understand the outside world. This year in the gaokao Li Qing was admitted to Sichuan International Studies University. The village head says that because of these university students many children in the village now have the wish to go to university. (the book writes 200 and 23 in digits; translation mine)")
SVA = [("没有意思。", "Activity 4B-1 (my answers; the book gives none): “没有意思” (boring)."),
       ("爷爷奶奶没有办法在学习上帮助他们，更不能带他们去游玩。", "4B-2: The grandparents have no way to help them with study, and can’t take them out to play."),
       ("他们开办了一个免费的留守儿童兴趣班。", "4B-3: They set up a free interest class for left-behind children."),
       ("重庆大学已经有二百名学生参加了这个活动，附近的二十三个村子都有了免费的暑假兴趣班。", "4B-4: 200 Chongqing University students have taken part, and 23 nearby villages have free summer interest classes."),
       ("孩子们不仅暑假生活更丰富，而且学习上也有了进步。", "4B-5 Direct narration: The children not only have a richer summer vacation but also progress in their studies."),
       ("李晴参加了兴趣班以后，喜欢上了英语，考上了四川外语学院。", "4B-5 Example: After joining the interest class Li Qing came to like English and was admitted to Sichuan International Studies University."),
       ("村长说，因为这些大学生，村里很多孩子都有了上大学的愿望。", "4B-5 Quotation: The village head says that because of these university students, many village children now wish to go to university.")]
L2 = lesson(
    "Lesson 29 Presentation 3 skill integration: a father’s dilemma and a free summer class",
    "李正华 · 不放心 · 玩电脑游戏 · 挣钱就带不了孩子 · 金花村 · 暑假兴趣班 · 村长",
    requires=[],
    cards=[
        card("Skill Integration, Activity 3 (Reading and Speaking)",
             "Pair up. Read the passage and check your understanding with your partner, then discuss possible solutions for the problem described. The passage and my sample:",
             examples=[D(*LZ)] + [D(z, e) for z, e in LZA]),
        card("Skill Integration, Activity 4 (Speaking, Listening and Reading)",
             "A. In groups of three, discuss the following questions. 1. How do the 留守儿童 spend their summer vacation? 2. What can the college students do for the 留守儿童 during their summer vacation? B. Read the passage about the summer vacation of 留守儿童 and answer the questions. Compare your answer with your partner and discuss the differences, if any. 1. What specific word in the passage describes the summer vacation of 留守儿童? 2. What caused the problem? 3. What did the college students do for the children? 4. What is the current situation? 5. Describe three ways the author illustrates how the college students bring benefit to the 留守儿童 (Direct narration / Example / Quotation). The passage and my answers:",
             examples=[D(*SV)] + [D(z, e) for z, e in SVA]),
    ],
    exercises=[
        M("Why do Li Zhenghua and his wife not want to bring their son to the city?", "They have no time to look after him", ["The city has no school", "He doesn’t want to come", "It is too cold"], "让他到城里来我们又没有时间照顾他."),
        M("What did the son do after school by fourth grade?", "Played computer games at classmates’ homes", ["Studied at the library", "Helped his grandfather", "Practiced football"], "放学后都到同学家里去玩儿电脑游戏."),
        M("Why did the son say he could only play with classmates?", "Nothing fun at home and nothing to say to grandparents", ["He had no grandparents", "He liked the school bus", "He was afraid of dogs"], "回家以后没什么好玩的，跟爷爷奶奶也没什么话说."),
        M("What does Li Zhenghua say about taking care of the child and earning money?", "He can’t do both", ["He can do both", "He does neither", "Money is not needed"], "带孩子就挣不了钱，挣钱就带不了孩子."),
        M("What did Chongqing University students set up in Jinhua Village?", "A free interest class for left-behind children", ["A university branch", "A hospital", "A factory"], "开办了一个免费的留守儿童兴趣班."),
        M("What did Li Qing come to like because of the class?", "English", ["Math", "Football", "Painting"], "喜欢上了英语."),
        M("Where was Li Qing admitted?", "Sichuan International Studies University", ["Peking University", "Chongqing University", "A local school"], "考上了四川外语学院."),
        F("金花村位于重庆山___，这里有很多留守儿童。", "区", ["里", "上", "下"], "山区: mountain area."),
        F("几年前，重庆大学的几个学生在这里开___了一个免费的留守儿童兴趣班。", "办", ["做", "始", "放"], "开办: set up."),
        F("村里很多孩子都有了上大学的愿___。", "望", ["意", "想", "心"], "愿望: wish."),
    ],
)

# ------------------------------------------------------------------ 3. act 5 futsal and using chinese act 1
FT = ("这是一所普通的农村小学，但是有一个很特别的足球队。球队的十三个队员都是留守儿童，教练是不太懂足球的数学老师。但是，他们赢过很多专业球队，两次在全国比赛得到第二名。专家们都说，这些孩子能赢，主要是因为太能吃苦，太能跑了。因为有足球特长，这些孩子有了一个新的机会：到城里的中学读书。最让人高兴的是，球队的两名队员——国林和云丰被评为全国最优秀小球员，城里一所有名的中学请他们免费上学。",
      "Activity 5A: This is an ordinary rural elementary school, but it has a very special futsal team. The team’s thirteen players are all left-behind children, and the coach is a math teacher who doesn’t know much about soccer. But they have beaten many professional teams and twice won second place in national competitions. The experts all say that these children can win mainly because they can endure hardship so well and can run so much. Because of their soccer talent, these children have a new opportunity: to study at a middle school in the city. Most gratifying of all, two players of the team, Guolin and Yunfeng, were named the best young players in the country, and a famous city middle school invited them to study for free. (the book writes 13 in digits and joins the dash as “--”; translation mine)")
FTA = [("球队的十三个队员都是留守儿童，教练是不太懂足球的数学老师。", "Activity 5A-1 (my answers; the book gives none): The team’s thirteen players are all left-behind children, and the coach is a math teacher who doesn’t know much about soccer."),
       ("他们赢过很多专业球队，两次在全国比赛得到第二名，因为他们太能吃苦，太能跑了。", "5A-2: They beat many professional teams and twice won second place in national matches, because they can endure hardship and run a lot."),
       ("因为国林和云丰被评为全国最优秀小球员。", "5A-3: Because Guolin and Yunfeng were named the best young players in the country."),
       ("城里一所有名的中学请他们免费上学。", "5A-4: A famous city middle school invited them to study for free."),
       ("十年以后，他们可能成了专业的足球运动员，也可能上了大学。", "5C (my imagining; the book gives none): In ten years they might be professional football players, or might have gone to university.")]
NM = ("农民工就是那些从农村到城市打工的人，他们大多数是从中国的中部和西部贫穷的地区到东部经济发达的地区工作。到二零一八年，中国的农民工超过二点八亿。农民工的教育水平比较低，干的都是城里人不愿意做的最苦最累的活儿。他们是城市中工作条件最差，收入最低的人。他们很难和家人生活在一起，也不能照顾留在农村的老人和孩子。有的农民工把孩子带到城市，但是，这些孩子都面对在城里上学难，上学贵的困难。",
      "Using Chinese in Context, Activity 1B: Migrant workers (农民工) are people who go from the countryside to cities to work. Most of them go from the poor central and western regions of China to work in the economically developed eastern regions. By 2018 China’s migrant workers numbered more than 280 million. Their education level is relatively low, and the work they do is the hardest and most tiring work city people don’t want to do. They are the people with the worst working conditions and lowest incomes in the city. It is hard for them to live with their families, and they cannot look after the old people and children left in the countryside. Some migrant workers bring their children to the city, but these children all face the difficulties of schooling in the city being hard and expensive. (the book writes 2018 and 2.8 in digits; translation mine)")
L3 = lesson(
    "Lesson 29 Presentation 3: a futsal team of left-behind children, and who 农民工 are",
    "足球队 · 数学老师当教练 · 太能吃苦 · 最优秀小球员 · 农民工 · 中部和西部 · 最苦最累的活儿",
    requires=[],
    cards=[
        card("Skill Integration, Activity 5 (Reading, Listening and Speaking)",
             "A. Read the story about a futsal team and answer the questions. 1. Why is this futsal team special? 2. What did they achieve, and why? 3. Why were the two boys outstanding? 4. What opportunity was offered to them? B. Pair up. Each partner listens to one part of the story and tells their partner about it (Part 1 and Part 2 are audio, so no key). C. Imagine the two boys’ life in 10 years. Share your thoughts with the class. The story and my answers:",
             examples=[D(*FT)] + [D(z, e) for z, e in FTA]),
        card("Using Chinese in Context, Activity 1 (Speaking and Reading)",
             "A. Pair up. Using what you learned thus far, discuss with your partner who 农民工 are. What are the difficulties they face? List them below (the book gives two empty lines: 什么是农民工, 他们有哪些困难). B. Read the short passage and determine what is missing in your discussion. What is missing? (The book gives no key.)",
             examples=[D(*NM)]),
    ],
    exercises=[
        M("What is special about the futsal team?", "All thirteen players are left-behind children", ["It is from a big city", "It has foreign players", "It has no coach"], "球队的十三个队员都是留守儿童."),
        M("Who is the coach?", "A math teacher who doesn’t know much about soccer", ["A famous player", "A foreign coach", "A doctor"], "教练是不太懂足球的数学老师."),
        M("What did the team achieve?", "Twice won second place nationally", ["Won the world cup", "Never lost", "Won last place"], "两次在全国比赛得到第二名."),
        M("Why can these children win, according to experts?", "They can endure hardship and run a lot", ["They are very tall", "They have fancy shoes", "They practice indoors"], "太能吃苦，太能跑了."),
        M("What opportunity did the two boys get?", "A free place at a famous city middle school", ["A trip abroad", "A job", "A new house"], "城里一所有名的中学请他们免费上学."),
        M("Who are 农民工?", "People who go from the countryside to cities to work", ["City teachers", "Foreign workers", "Farmers who stay home"], "从农村到城市打工的人."),
        M("Where do most 农民工 come from?", "The poor central and western regions", ["Eastern cities", "Overseas", "Northern forests"], "从中国的中部和西部贫穷的地区."),
        M("What do their children face?", "Hard, expensive schooling in the city", ["No school at all anywhere", "Free schools", "Easy exams"], "上学难，上学贵."),
        F("球队的两名队员被评为全国最优___小球员。", "秀", ["良", "好", "高"], "优秀: outstanding."),
        F("农民工的教育水___比较低。", "平", ["高", "面", "地"], "水平: level."),
        F("他们是城市中工作条件最差，收___最低的人。", "入", ["出", "进", "来"], "收入: income."),
    ],
)

UNIT = unit("第二十九课 中国的教育 Presentation 3: 综合技能, 语境中的汉语 (1)", [L1, L2, L3])
