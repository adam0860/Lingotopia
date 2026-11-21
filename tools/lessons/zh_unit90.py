"""Unit 90: Lesson 28 (China's Youth), Presentation 2, second half: the skill-integration tasks (a survey of the post-'00s, what they are like, young professors),
the using-Chinese tasks (situations, Zak's book about China's youth, Qi Yifei and her mother) and the vocabulary list.
Audio and pictures are not included; numbers the book writes as digits are spelled out in Chinese text; Latin letters in the spoken text are written full-width; web addresses are left out;
answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l28_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('长大', 0, 'zhang3'), ('生长', 1, 'zhang3'), ('增长', 1, 'zhang3'), ('问卷', 1, 'juan4')):
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
NOUN = ["前途", "目标", "材料"]

# ------------------------------------------------------------------ 1. skill integration 1
W1 = [("现在年轻人的环保意识很强。", "Activity 1A, 1. 意识 (consciousness, awareness; the glosses in this list are mine), the book’s example: Young people today have a strong environmental awareness."),
      ("关于环境问题的问卷调查。", "2. 问卷调查 (questionnaire survey): A questionnaire survey about environmental problems."),
      ("这次单元考试的结果你们知道了吗？", "3. 结果 (result): Do you all know the results of this unit exam?"),
      ("以前他们不重视环保，现在重视了。", "4. 重视 (attach importance to): Before, they did not attach importance to environmental protection; now they do."),
      ("认为锻炼身体越多越好是不科学的。", "5. 科学 (scientific): It is unscientific to think that the more you exercise the better."),
      ("他去过很多地方，眼界很开阔。", "6. 眼界开阔 (yǎnjiè kāikuò, broad horizons): He has been to many places and his horizons are very broad."),
      ("环保观念，家庭观念，教育观念。", "7. 观念 (concept, idea): Environmental concepts, family concepts, educational concepts.")]
SK1 = [("记者", "王教授，听说您最近对零零后青少年的环保意识，做了一个问卷调查。", "Reporter: Professor Wang, I hear you recently did a questionnaire survey about the environmental awareness of post-’00s young people. (the Activity 1 script; translations mine; the book writes 00 后 in digits)"),
       ("教授", "对，我们对中国十个省的差不多一万名零零后做了一个问卷调查。", "Professor: Yes, we did a questionnaire survey of nearly ten thousand post-’00s in ten provinces of China."),
       ("记者", "能不能把结果给大家介绍一下？", "Reporter: Could you introduce the results to everyone?"),
       ("教授", "好啊。简单地说，调查结果告诉我们，现在的零零后，百分之七十以上都有很强的环保意识。", "Professor: Sure. Simply put, the survey results tell us that more than seventy percent of today’s post-’00s have a strong environmental awareness."),
       ("记者", "哦，那很高啊。", "Reporter: Oh, that is very high."),
       ("教授", "是的。五年前我们也做过这样的调查，那时青少年的环保意识比现在差很多。", "Professor: Yes. Five years ago we did a similar survey, and at that time young people’s environmental awareness was much worse than now."),
       ("记者", "为什么现在的青少年越来越重视环保了呢？", "Reporter: Why are young people today paying more and more attention to environmental protection?"),
       ("教授", "一个重要原因是他们受的教育多了，看事情更科学了。", "Professor: One important reason is that they are better educated and look at things more scientifically."),
       ("记者", "可能还有一点。年轻人喜欢上网，看得多了，眼界就更开阔，更关心世界上的事，也更关心将来的事。", "Reporter: There may be one more point. Young people like to go online; seeing more, their horizons become broader, and they care more about world affairs and about the future."),
       ("教授", "你说得很对。现在信息发达了，对青少年的观念有很大影响。还有，生活条件越来越好，对人们的观念也有相当大的影响。", "Professor: You are quite right. Information is more developed now and has a great influence on young people’s ideas. Also, living conditions are getting better and better, which also has a considerable influence on people’s ideas."),
       ("记者", "要我看，这一条最重要。每天饭都不够吃，很少有人会想到关心教育和爱护地球。", "Reporter: In my view this one is the most important. When there isn’t enough food every day, few people think of caring about education and cherishing the earth."),
       ("教授", "你说得有道理！", "Professor: What you say makes sense!")]
SK1A = [("这个对话主要谈的是零零后青少年的环保意识的问卷调查，还有他们越来越重视环保的原因。", "Activity 1B-1 (my answer): The dialog is mainly about the questionnaire survey on post-’00s young people’s environmental awareness and the reasons they are paying more and more attention to the environment."),
        ("问卷调查的结果说，现在的零零后，百分之七十以上都有很强的环保意识，比五年前高多了。", "1B-2 (my answer): The survey results say that more than seventy percent of today’s post-’00s have a strong environmental awareness, much higher than five years ago."),
        ("他们受的教育多了，看事情更科学了；上网多了，眼界更开阔；信息发达了；生活条件也越来越好。", "1B-3 (my answer): They are better educated and see things more scientifically; they go online more and have broader horizons; information is more developed; and living conditions keep improving.")]
SK1T = table(["关于", "细节 (my sample, from the script)"], [["问卷调查和结果", "对中国十个省的差不多一万名零零后做的调查；百分之七十以上有很强的环保意识；五年前也做过，那时的环保意识比现在差很多"], ["青少年重视环保的原因 (王教授)", "受的教育多了，看事情更科学；上网多，眼界更开阔，更关心世界和将来；信息发达，对观念有很大影响；生活条件越来越好，对观念也有相当大的影响"]], title="Activity 1C: the details table (the book leaves the cells empty)")
L1 = lesson(
    "Lesson 28 Presentation 2 skill integration: a survey of the post-’00s and their environmental awareness",
    "意识 · 问卷调查 · 结果 · 重视 · 科学 · 眼界开阔 · 观念 · 王教授",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Writing, Speaking, and Reading)",
             "A. Pair up and see if you and your partner can guess what the following expressions mean (the book’s examples follow, with glosses of mine). B. Listen to the dialog and answer the following questions. Share your answers with your partner. 1. 这个对话主要谈的是什么？ 2. 问卷调查的结果说什么了？ 3. 是什么改变了中国年轻一代对环保问题的看法？ C. Listen to the dialog two more times and list as many details as you can in the table below. Share your work with your partner when you’re done. Go through the script and refine your work. D. Tell your partner how young people in the U.S. have changed their attitude about the environment. Include an example. The words, the script, my answers and table:",
             tables=[SK1T], examples=[D(z, e) for z, e in W1] + dlg(SK1) + [D(z, e) for z, e in SK1A]),
    ],
    exercises=[
        M("How many provinces did the professor’s survey cover?", "Ten", ["Two", "Twenty", "Thirty"], "中国十个省."),
        M("About how many post-’00s answered the survey?", "About ten thousand", ["About a hundred", "About a million", "About twenty"], "差不多一万名."),
        M("What share of post-’00s have a strong environmental awareness?", "More than seventy percent", ["Ten percent", "About half", "Nobody"], "百分之七十以上."),
        M("How did young people’s awareness five years ago compare with now?", "It was much worse", ["It was the same", "It was much better", "It was not measured"], "那时青少年的环保意识比现在差很多."),
        M("What is one important reason young people value environmental protection more?", "They are better educated", ["They have less money", "They go out less", "They are older"], "他们受的教育多了."),
        M("What effect does going online have on young people, according to the reporter?", "Broader horizons", ["Shorter horizons", "Less sleep", "Worse grades"], "眼界就更开阔."),
        M("What does the reporter think is the most important reason?", "Better living conditions", ["More homework", "Fewer cars", "Cheaper food only"], "这一条最重要."),
        M("What does 重视 mean?", "Attach importance to", ["Forget about", "Fear", "Sell"], "以前他们不重视环保，现在重视了."),
        F("现在的零零后，百分之七十以上都有很强的环保意___。", "识", ["字", "想", "说"], "意识: awareness."),
        F("看事情更科___了。", "学", ["校", "字", "习"], "科学: scientific."),
        F("每天饭都不够吃，很少有人会想到关心教育和爱___地球。", "护", ["看", "想", "跑"], "爱护: cherish."),
    ],
)

# ------------------------------------------------------------------ 2. skill integration 2-3
P2A = ("零零后有什么特点呢？首先，他们的生长环境不同。不少零零后的父母是在改革开放的环境中长大的，他们的生活条件，比八零后、九零后的父母当时的条件好很多。等到自己有了孩子，他们很多人可以给孩子买电脑，送孩子参加各种补习班，甚至带孩子出国旅游。", "What are the characteristics of the post-’00s? First, their growing-up environment is different. Many post-’00s’ parents grew up in the environment of reform and opening up, and their living conditions were much better than the conditions of the post-’80s’ and post-’90s’ parents back then. When they had children of their own, many of them could buy computers for their children, send them to all kinds of tutoring classes, and even take them abroad on trips. (Skill Integration, Activity 2; underlined sentence 1 is the second; translations mine)")
P2B = ("零零后的第二个特点是比较成熟。虽然他们多数还是学生，但是他们很多人对事情都有自己的看法，有事情喜欢自己作决定。", "The second characteristic of the post-’00s is that they are rather mature. Although most of them are still students, many of them have their own views on things and like to make their own decisions. (underlined sentence 2 is the first)")
P2C = ("零零后的第三个特点是重视学习。他们是在互联网的影响下长大的，很了解世界上发生的事情，对新的事物特别感兴趣。他们愿意在学习中发现，在发现中找到乐趣。", "The third characteristic of the post-’00s is that they value learning. They grew up under the influence of the Internet, know a lot about what happens in the world, and are especially interested in new things. They are willing to discover in learning and to find enjoyment in discovery. (underlined sentence 3 is the first)")
U2 = [("不少零零后的父母是在改革开放的环境中长大的，他们的生活条件，比八零后、九零后的父母当时的条件好很多。", "Activity 2B, underlined sentence 1 (my translation): Many post-’00s’ parents grew up in the environment of reform and opening up, and their living conditions were much better than the conditions of the post-’80s’ and post-’90s’ parents back then."),
      ("虽然他们多数还是学生，但是他们很多人对事情都有自己的看法，有事情喜欢自己作决定。", "Underlined sentence 2 (my translation): Although most of them are still students, many of them have their own views on things and like to make their own decisions."),
      ("他们是在互联网的影响下长大的，很了解世界上发生的事情，对新的事物特别感兴趣。", "Underlined sentence 3 (my translation): They grew up under the influence of the Internet, know a lot about what happens in the world, and are especially interested in new things.")]
QA2 = [("这篇文章主要是讲零零后的三个特点：生长环境不同、比较成熟、重视学习。", "Activity 2C-1 (my answer): The article is mainly about three characteristics of the post-’00s: a different growing-up environment, being rather mature, and valuing learning."),
       ("零零后的父母是在改革开放的环境中长大的，生活条件比八零后、九零后的父母当时好很多，能给孩子买电脑，送孩子参加补习班，甚至带孩子出国旅游。", "2C-2 (my answer): The post-’00s’ parents grew up during reform and opening up, with much better living conditions than the post-’80s’ and post-’90s’ parents had, and could buy computers for their children, send them to tutoring classes and even take them abroad."),
       ("因为他们很多人对事情都有自己的看法，有事情喜欢自己作决定。", "2C-3 (my answer): Because many of them have their own views on things and like to make their own decisions."),
       ("他们是在互联网的影响下长大的，很了解世界上发生的事情，对新的事物特别感兴趣，愿意在学习中发现，在发现中找到乐趣。", "2C-4 (my answer): They grew up under the Internet’s influence, know a lot about the world, are especially interested in new things, and like to discover in learning and find enjoyment in discovery.")]
RD2 = [("记者", "请问，零零后有什么特点？", "Activity 2D (my sample dialog between a reporter and an expert in Chinese education): Reporter: May I ask, what are the post-’00s like?"),
       ("专家", "首先，他们的生长环境不同。不少零零后的父母是在改革开放的环境中长大的，生活条件比八零后、九零后的父母当时好很多。", "Expert: First, their growing-up environment is different. Many of their parents grew up during reform and opening up, with living conditions much better than those of the post-’80s’ and post-’90s’ parents back then."),
       ("记者", "那他们的父母能给孩子什么？", "Reporter: Then what can their parents give them?"),
       ("专家", "很多人可以给孩子买电脑，送孩子参加各种补习班，甚至带孩子出国旅游。", "Expert: Many can buy computers for their children, send them to all kinds of tutoring classes, and even take them abroad."),
       ("记者", "零零后还有什么特点？", "Reporter: What other characteristics do the post-’00s have?"),
       ("专家", "第二个特点是比较成熟。他们很多人对事情都有自己的看法，有事情喜欢自己作决定。", "Expert: The second is that they are rather mature. Many have their own views and like to make their own decisions."),
       ("记者", "在学习方面呢？", "Reporter: And in learning?"),
       ("专家", "他们重视学习。他们是在互联网的影响下长大的，很了解世界上发生的事情，对新的事物特别感兴趣。", "Expert: They value learning. They grew up under the Internet’s influence, know a lot about the world and are especially interested in new things."),
       ("记者", "谢谢您！", "Reporter: Thank you!"),
       ("专家", "不客气。", "Expert: You’re welcome.")]
HJ1 = ("今年二十九岁的胡剑在博士毕业后，成为华东交通大学的教授，他也是华东交大的第一位九零后教授。在接受记者采访时，胡剑说“能够有一点小成果，可能更多还是因为我们比较用功一点或者说勤奋一点，有好几个月都是六点左右去实验室，晚上十二点才回宿舍。”胡剑曾经在世界最有名的科学杂志之一——《Ｓｃｉｅｎｃｅ》杂志上发表过论文。据说，能够在那个杂志上发表论文，是胡剑成为教授的重要原因之一。", "Hu Jian, who is twenty-nine this year, became a professor at East China Jiaotong University after earning his doctorate; he is also the university’s first post-’90s professor. In an interview with a reporter, Hu Jian said, “That I have been able to achieve a small result is probably more because we are a bit more hard-working, or diligent; for several months I went to the lab at around six o’clock and returned to the dormitory only at twelve at night.” Hu Jian once published a paper in Science, one of the most famous science journals in the world. It is said that being able to publish a paper in that journal is one of the important reasons Hu Jian became a professor. (Activity 3, an authentic news report adapted from a news site, whose address is left out; the book writes the numbers in digits and Science in Latin letters; translations mine)")
HJ2 = ("最近，网友不止一次看到九零后担任教授的新闻。比如，几天前，二十八岁的女博士李琳担任了南方医科大学教授；二零一九年七月，同样是二十八岁的万龙成为了哈尔滨工业大学教授；二零一八年十二月，获得博士学位的李姗，进入南京农业大学担任教授，那年她也是二十八岁；二零一八年三月，二十八岁的李东，被湖南大学聘为教授。", "Recently, netizens have more than once seen news of post-’90s people becoming professors. For example, a few days ago, Li Lin, a 28-year-old woman doctor, became a professor at Southern Medical University; in July 2019, Wan Long, also 28, became a professor at Harbin Institute of Technology; in December 2018, Li Shan, who had received her doctorate, entered Nanjing Agricultural University as a professor, and she too was 28 that year; in March 2018, Li Dong, 28, was hired as a professor by Hunan University.")
HJS = [("胡剑二十九岁，博士毕业后成为华东交通大学的教授，是学校的第一位九零后教授。他很用功，在世界最有名的科学杂志之一上发表过论文，这是他成为教授的重要原因之一。最近还有几位二十八岁的九零后也当了教授。", "Activity 3 summary (my sample, in Chinese; the book asks for English): Hu Jian is twenty-nine; after his doctorate he became a professor at East China Jiaotong University, the school’s first post-’90s professor. He is very diligent and published a paper in one of the world’s most famous science journals, which was one of the important reasons he became a professor. Recently several 28-year-old post-’90s people have also become professors.")]
HJQ = [("胡剑是在哪儿当教授的？", "Activity 3B (my sample questions to the journalist): Where did Hu Jian become a professor?"), ("他为什么能这么年轻就当教授？", "Why was he able to become a professor so young?"), ("他每天几点去实验室，几点回宿舍？", "What time did he go to the lab each day, and what time did he return to the dormitory?"), ("他在哪个杂志上发表过论文？", "In which journal did he publish a paper?"), ("别的九零后教授，都是多大年纪当的教授？", "How old were the other post-’90s professors when they became professors?")]
WK3 = table(["词", "Meaning (mine)"], [["勤奋", "diligent"], ["发表", "publish"], ["论文", "paper, thesis"], ["博士", "doctor, Ph.D."], ["学位", "academic degree"], ["被聘为", "be hired as"]], title="Activity 3A: terms to look up first", say=[0])
L2 = lesson(
    "Lesson 28 Presentation 2 skill integration: what the post-’00s are like, and young professors",
    "零零后的特点 · 生长环境 · 成熟 · 重视学习 · 胡剑 · 勤奋 · 发表论文 · 九零后教授",
    requires=[],
    cards=[
        card("Skill Integration, Activity 2 (Reading, Writing, and Speaking)",
             "A. Read the passage below. Consult your dictionary if necessary. B. Take turns translating the underlined sentences into English (the book underlines one sentence in each of the three paragraphs, numbered 1) to 3)). C. Pair up. Ask and answer the questions in Chinese. 1. 这篇文章主要是讲什么的？ 2. 和八零后、九零后的父母比较，零零后的父母有什么特点？ 3. 为什么说零零后比较成熟？ 4. 在学习方面，零零后有什么特点？ D. Turn the passage into a conversation between a reporter and an expert in Chinese education. Act out the dialog for the class. The passage, the underlined sentences, my answers and my sample dialog:",
             examples=[D(*P2A), D(*P2B), D(*P2C)] + [D(z, e) for z, e in U2 + QA2] + dlg(RD2)),
        card("Skill Integration, Activity 3 (Reading, Writing, and Speaking)",
             "A. Read the authentic material below and write an English summary. Then share your summary with a classmate. First consult a dictionary to learn these terms: 勤奋, 发表, 论文, 博士, 学位 and 被聘为. B. You are having a conversation with the journalist who wrote this report. Ask them questions about Hu Jian’s achievements and promotion. Obtain any details about the promotions of others. Your partner will play the role of the journalist. The report, a sample summary and my sample questions:",
             tables=[WK3], examples=[D(*HJ1), D(*HJ2)] + [D(z, e) for z, e in HJS + HJQ]),
    ],
    exercises=[
        M("What is the first characteristic of the post-’00s in the passage?", "Their growing-up environment is different", ["They are lazy", "They dislike school", "They are very tall"], "首先，他们的生长环境不同."),
        M("What can many post-’00s’ parents do for their children?", "Buy computers, send them to classes and take them abroad", ["Nothing", "Send them to work", "Move abroad alone"], "买电脑，送孩子参加各种补习班，甚至带孩子出国旅游."),
        M("What is the second characteristic?", "They are rather mature", ["They are shy", "They are noisy", "They are old"], "比较成熟."),
        M("What is the third characteristic?", "They value learning", ["They avoid learning", "They like sleeping", "They like money only"], "重视学习."),
        M("How old is Hu Jian?", "Twenty-nine", ["Eighteen", "Forty", "Fifty"], "今年二十九岁."),
        M("What was Hu Jian’s university first?", "Its first post-’90s professor", ["Its oldest professor", "Its first student", "Its first library"], "华东交大的第一位九零后教授."),
        M("What time did Hu Jian return to the dormitory some nights?", "Twelve o’clock at night", ["Six in the morning", "Noon", "Four in the afternoon"], "晚上十二点才回宿舍."),
        M("Which journal did Hu Jian publish a paper in?", "One of the world’s most famous science journals", ["A local newspaper", "A cooking magazine", "A sports weekly"], "世界最有名的科学杂志之一."),
        M("How old were the other post-’90s professors mentioned?", "Twenty-eight", ["Fifty", "Eighteen", "Seventy"], "都是二十八岁."),
        F("他们愿意在学习中发___，在发现中找到乐趣。", "现", ["看", "想", "说"], "发现: discover."),
        F("能够有一点小成果，可能更多还是因为我们比较用功一点或者说勤___一点。", "奋", ["快", "学", "忙"], "勤奋: diligent."),
        F("胡剑曾经在世界最有名的科学杂志之一上发___过论文。", "表", ["看", "写", "读"], "发表: publish."),
    ],
)

# ------------------------------------------------------------------ 3. using Chinese 1-2
UC1 = [("关心。调查说，百分之七十以上的零零后环保意识很强。他们觉得，关心世界、爱护地球是自己该做的事。", "Using Chinese in Context, Activity 1, 1 (my answer, two sentences): Yes. Surveys say that more than seventy percent of the post-’00s have a strong environmental awareness. They feel that caring about the world and cherishing the earth is something they should do."),
       ("这可能是因为他们长大的环境不一样。父母那一代生活条件不太好，对外面的事情了解得很少；年轻一代从小就用互联网，知道的事情多，眼界也更开阔，所以想得不一样。", "2 (my answer, three sentences): This may be because the environments they grew up in are different. The parents’ generation did not have very good living conditions and knew little about the outside; the young generation have used the Internet since childhood, know many things and have broader horizons, so they think differently."),
       ("应该对他说，这样做不对，不要把垃圾倒在马路上。如果他不听，可以告诉警察。", "3 (my answer, two sentences): You should tell him that doing this is wrong and that he should not dump garbage on the road. If he does not listen, you can tell the police.")]
ZB = ("《一个美国九零后的观察：中国的年轻人与年轻的中国》", "Using Chinese in Context, Activity 2: the book Zak has published (the book writes 90 后 in digits; the title means “A Post-’90s American’s Observations: China’s Young People and Young China”; translation mine; the book gives the web address of an online bookstore, which I leave out)")
ZW = table(["词", "Meaning (mine)"], [["观察", "observe; observation"], ["接触", "come into contact with"], ["自信", "self-confident"], ["自豪", "proud"], ["举一个例子", "give an example"], ["遇到", "run into, meet"], ["落后", "backward"], ["倍", "times, -fold"], ["旧", "old, worn"], ["决定", "decide"], ["命运", "fate"]], title="Activity 2A: the words to find the meaning of first", say=[0])
ZS1 = [("朋友", "听说您最近写了一本关于中国青年人的书。", "Script 1. Friend: I hear you recently wrote a book about Chinese young people. (translations mine)"),
       ("作者", "对。我自己是美国的九零后，在中国生活了一段时间，我想把自己对中国年轻一代的观察写下来，告诉美国的老百姓。", "Author: Right. I am a post-’90s American; I lived in China for a period and I wanted to write down my observations of China’s young generation and tell ordinary Americans."),
       ("朋友", "中国青年和美国青年一定有很多不同，对吧？", "Friend: Chinese and American young people must differ in many ways, right?"),
       ("作者", "是的。首先，中国年轻人的数量太大了。八零后和九零后，美国有八千万人，中国是美国的五倍，超过四亿。", "Author: Yes. First, the number of Chinese young people is huge. For the post-’80s and post-’90s, the U.S. has eighty million, and China has five times as many, over four hundred million."),
       ("朋友", "四亿？那差不多是美国和加拿大两个国家人口了。", "Friend: Four hundred million? That is about the population of the U.S. and Canada put together."),
       ("作者", "可不。", "Author: Exactly."),
       ("朋友", "还有别的不同吗？", "Friend: Are there other differences?"),
       ("作者", "另一个不同，就是童年的目标不一样。在美国，我们强调全面发展。", "Author: Another difference is that childhood goals are different. In the U.S. we emphasize all-round development."),
       ("朋友", "对，我们不但要学习好，也要参加各种各样的活动。", "Friend: Right, we have to not only study well but also take part in all kinds of activities."),
       ("作者", "当我们在到处玩儿、周末在外过夜、去游泳或打篮球的时候，我们的中国同龄人都在努力地学习。", "Author: When we were playing everywhere, spending weekends away overnight, swimming or playing basketball, our Chinese peers were all studying hard."),
       ("朋友", "中国的孩子学习的压力非常大。", "Friend: Chinese children are under great pressure to study."),
       ("作者", "还有一点，就是现在中国的年轻人，与外面的世界接触越多，反而越自信。", "Author: One more thing: today’s Chinese young people, the more they come into contact with the outside world, are on the contrary more self-confident."),
       ("朋友", "这是为什么？", "Friend: Why is that?"),
       ("作者", "他们见得多了，更知道中国这些年的进步。我在中国遇到的年轻人，很多人都对作为中国人感到自豪。", "Author: They have seen more and know better how China has progressed in these years. Many of the young people I met in China feel proud to be Chinese.")]
ZS2 = [("朋友", "中国的年轻人和他们父母那一代比，有哪些不同呢？", "Script 2. Friend: Compared with their parents’ generation, how do China’s young people differ?"),
       ("作者", "我给你举一个例子。我朋友小飞的父母告诉我，当他们还是孩子的时候，一些邻居们总来他们家，就为了看他们家墙上的几张欧洲的风景照片。", "Author: Let me give you an example. My friend Xiao Fei’s parents told me that when they were children, some neighbors always came to their house just to look at a few photos of European scenery on their wall."),
       ("朋友", "那时中国很落后。听说一般老百姓连去另一个省都很少，更不用说出国了。所以他们觉得西方国家的什么东西都好。", "Friend: China was very backward then. I hear ordinary people rarely even went to another province, let alone abroad. So they felt everything in Western countries was good."),
       ("作者", "到了小飞这一代，从小就学英语，上网，他们是看着美国电影和电视节目长大的，长大以后很多人出国上学或是旅游。", "Author: By Xiao Fei’s generation, they learned English and went online from childhood, grew up watching American movies and TV shows, and when grown many went abroad to study or travel."),
       ("朋友", "他们这一代很了解国外的情况。", "Friend: This generation knows foreign conditions very well."),
       ("作者", "小飞说，从他出生到现在，中国的ＧＤＰ增长了二十七倍。大批年轻人从农村到了城市，从骑自行车到开上了汽车，从住又小又旧的房子搬到漂亮宽敞的高层公寓。", "Author: Xiao Fei says that since he was born, China’s GDP has grown twenty-seven times. Masses of young people have gone from the countryside to the cities, from riding bicycles to driving cars, from living in small old houses to moving into beautiful, spacious high-rise apartments. (the book writes GDP in Latin letters and 27 in digits)"),
       ("朋友", "这个变化是太大了。", "Friend: That is an enormous change."),
       ("作者", "对。现在大多数年轻人不需要想怎么才能有饭吃。他们会问，“我想要一个什么样的自己？一个什么样的家庭？一个什么样的国家？”", "Author: Yes. Most young people now don’t need to think about how to get enough to eat. They ask, “What kind of self do I want? What kind of family? What kind of country?” (the book’s 年轻人人 has a repeated 人; I print 年轻人)"),
       ("朋友", "他们有自己的想法，要决定自己的命运，还有家庭和国家的命运。", "Friend: They have their own ideas and want to decide their own fate, and the fate of their family and country.")]
ZT = table(["关于", "笔记 (my sample, from the scripts)"],
           [["作者和他写的书", "作者是美国的九零后，在中国生活了一段时间，写了一本关于中国青年的书，想告诉美国的老百姓"], ["中国青年和美国青年的不同", "中国年轻人数量太大了（八零后和九零后超过四亿，是美国的五倍）；童年的目标不一样，美国强调全面发展，中国同龄人都在努力地学习；与外面的世界接触越多，反而越自信，对作为中国人感到自豪"], ["中国青年和他们父母一代的不同", "小飞的父母小时候，邻居来看墙上的欧洲风景照片，那时中国很落后；小飞这一代从小学英语、上网，看美国电影和电视节目，很多人出国上学或旅游；经济增长很快，大批年轻人从农村到了城市，开上了汽车，住进漂亮宽敞的高层公寓"], ["多数中国青年关心的事", "不再想怎么才能有饭吃，而是问自己想要什么样的自己、家庭和国家，要决定自己、家庭和国家的命运"]],
           title="Activity 2A: the notes table (Part 1 and Part 2; the book leaves the cells empty)")
ZQ = [("作者为什么写这本书？", "Activity 2B (my five questions): Why did the author write this book?"), ("八零后和九零后，中国有多少人？", "How many post-’80s and post-’90s people does China have?"), ("美国孩子和中国孩子的童年有什么不同？", "How do the childhoods of American and Chinese children differ?"),
      ("为什么中国年轻人越接触外面的世界越自信？", "Why are Chinese young people more self-confident the more they come into contact with the outside world?"), ("小飞的父母小时候，邻居为什么总来他们家？", "Why did the neighbors always come to Xiao Fei’s parents’ house when they were children?")]
L3 = lesson(
    "Lesson 28 Presentation 2 using Chinese in context: situations, and a post-’90s American’s book about China’s young people",
    "中国的年轻人关心环境吗 · 看法不一样 · 垃圾 · 一个美国九零后的观察 · 全面发展 · 自信 自豪 · 小飞",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Reading and Speaking)",
             "Pair up and take turns telling your partner what you would say in the following situations. Provide as many details as possible. When you are done, switch roles and repeat the activity. 1. 有人问，现在中国的年轻人关心环境问题吗？ (two or more sentences) 2. 你发现，中国的年轻一代和他们的父母对很多问题的看法不一样。这是为什么呢？ (three or more sentences) 3. 看见有人把垃圾倒在马路上，应该怎么做？ (two or more sentences) My answers:",
             examples=[D(z, e) for z, e in UC1]),
        card("Using Chinese in Context, Activity 2 (Listening, Writing, Reading, and Speaking)",
             "Your friend’s friend, Zak, has spent a few years in China and he’s just published a book about China’s youth. A. Pair up. Each partner listens to one part of the conversation between Zak and his friend and notes the key information in the table below. First find the meanings of these words. B. Share what you wrote with your partner. Ask your partner at least five questions about what they heard. Use the scripts to refine your work. C. Examine the two images below, taken 40 years apart (the images are not included). How would you describe each? Possible questions to answer: Who could the people be? What are their living conditions like? What educational resources do they have? What will their future provide? D. Tell your partner an imaginary story about one of the pictures. Your partner will tell you a story about the other. The book, the words, the two scripts, my notes and my five questions:",
             tables=[ZW, ZT], examples=[D(*ZB)] + dlg(ZS1) + dlg(ZS2) + [D(z, e) for z, e in ZQ]),
    ],
    exercises=[
        M("Where is Zak from?", "The United States", ["China", "Canada", "Japan"], "我自己是美国的九零后."),
        M("How many post-’80s and post-’90s people does the U.S. have, according to Zak?", "Eighty million", ["Four hundred million", "Eight million", "Eight thousand"], "美国有八千万人."),
        M("How does China’s number compare with that of the U.S.?", "Five times as many", ["The same", "Half as many", "Ten times as many"], "中国是美国的五倍，超过四亿."),
        M("What do American childhoods emphasize, according to Zak?", "All-round development", ["Only studying", "Only sports", "Only travel"], "在美国，我们强调全面发展."),
        M("What do Chinese young people feel the more they contact the outside world?", "More self-confident", ["More afraid", "More tired", "More angry"], "反而越自信."),
        M("Why did neighbors come to Xiao Fei’s parents’ house?", "To look at photos of European scenery", ["To borrow food", "To watch TV", "To learn English"], "就为了看他们家墙上的几张欧洲的风景照片."),
        M("By how many times has China’s GDP grown since Xiao Fei was born?", "Twenty-seven times", ["Two times", "Seven times", "A hundred times"], "中国的ＧＤＰ增长了二十七倍."),
        M("What questions do most young people ask now?", "What kind of self, family and country do I want?", ["How can I get enough to eat?", "Where is the nearest store?", "What is the weather?"], "我想要一个什么样的自己？一个什么样的家庭？一个什么样的国家？"),
        M("What should you do if you see someone dumping garbage on the road (my answer)?", "Tell him it is wrong", ["Ignore it", "Join him", "Take a photo only"], "应该对他说，这样做不对."),
        F("在美国，我们强调全面发___。", "展", ["看", "想", "说"], "发展: development."),
        F("他们见得多了，更知道中国这些年的进___。", "步", ["学", "校", "子"], "进步: progress."),
        F("很多人都对作为中国人感到自___。", "豪", ["己", "信", "家"], "自豪: proud."),
    ],
)

# ------------------------------------------------------------------ 4. using Chinese 3: Qi Yifei
QA = [("她大概在想，爸爸妈妈有没有来送她，他们是不是还在生她的气。", "Activity 3A-1 (my answer, based on the report since the pictures are not included): She is probably wondering whether Mom and Dad have come to see her off and whether they are still angry with her."),
      ("她可能在给妈妈写信，说说她在部队的生活，也想知道妈妈是不是还在生气。", "3A-2 (my answer): She may be writing to her mother, telling her about her life in the army and wanting to know whether her mother is still angry."),
      ("她妈妈来给她发奖，妈妈和女儿都哭了，妈妈最后理解了她，也支持她。", "3A-3 (my answer): Her mother came to present her award, mother and daughter both cried, and in the end her mother understood and supported her.")]
LT = [("菲菲：三个月来，妈妈欠你一封信。总觉得有很多话要说，你刚离家时，那几天晚上妈妈都是一夜无眠。", "Activity 3C, the complete letter (translations mine). Feifei: For three months Mom has owed you a letter. I always felt there was so much to say; when you had just left home, for those few nights Mom did not sleep all night."),
      ("当我看到你们的训练视频的时候，看到那个在燃烧的铁丝网下匍匐前进的女兵，妈妈还是掉眼泪了。后来我才知道，那个女兵就是你啊！我没有想到我的女儿是如此坚强。", "When I saw the video of your training and saw the woman soldier crawling forward under the burning barbed wire, Mom still shed tears. Only later did I learn that the woman soldier was you! I never thought my daughter was so strong."),
      ("几次泪流满面，有心痛，有感动，也有惭愧和理解。你们是“零零后”新生一代，妈妈或许曾经不能理解你，但是妈妈现在坚定地支持你……", "Several times my face was covered with tears: there was heartache, there was being moved, and also shame and understanding. You are the new “post-’00s” generation; Mom perhaps could not understand you before, but Mom now firmly supports you… (the book writes 00 in digits)"),
      ("女儿，妈妈爱你！", "Daughter, Mom loves you!")]
LQ = [("她妈妈看到训练视频里，在燃烧的铁丝网下匍匐前进的女兵，后来才知道那就是自己的女儿，没想到女儿这么坚强，又心痛又感动。", "Activity 3C-1 (my answer): Her mother saw in the training video a woman soldier crawling under burning barbed wire and learned only later that she was her own daughter; she never thought her daughter was so strong, and felt both heartache and being moved."),
      ("妈妈以前不支持女儿参军，也不理解她，现在看到女儿这么坚强，觉得惭愧，也理解了她，坚定地支持她。", "3C-2 (my answer; 惭愧 cánkuì, be ashamed): Her mother had not supported her enlisting and had not understood her; now seeing how strong her daughter is, she feels ashamed, understands her and firmly supports her.")]
R1 = ("二零一八年，祁逸菲以很高的分数考入了清华大学美术学院，是个真正的“学霸”。", "In 2018, Qi Yifei entered the Academy of Arts & Design of Tsinghua University with very high scores; she was a true “top student.” (Activity 3D, the report; translations mine; the book writes 2018 in digits)")
R2 = ("但是，在就要上大二时，她却突然决定要参军。对她的打算，她妈妈不支持。妈妈觉得，她该好好地在清华大学学习，将来要当设计师，为什么要当兵呢？可是祁逸菲说，不是清华的学生要去当兵，而是想当兵的人考上了清华！", "But just as she was about to start her second year, she suddenly decided to join the army. Her mother did not support her plan. Her mother felt she should study well at Tsinghua and in the future become a designer, so why become a soldier? But Qi Yifei said it was not that a Tsinghua student wanted to be a soldier, but that someone who wanted to be a soldier had got into Tsinghua!")
R3 = ("祁逸菲穿上了军装。但一幅漫画作品，却说出了她的心事：在新兵队伍里，有一个女兵在往后看。祁逸菲画的是她自己。没得到父母同意她就参了军，她不停地在送行的家长中找爸爸妈妈的身影，希望在最后一分钟得到他们的支持。", "Qi Yifei put on the uniform. But a cartoon revealed what was on her mind: in the line of new recruits, there is a woman soldier looking back. Qi Yifei drew herself. She had joined the army without her parents’ consent, and kept looking among the parents seeing their children off for the figures of her mom and dad, hoping to get their support in the last minute.")
R4 = ("三个多月的训练过去了，新兵们迎来了训练结业仪式。祁逸菲第一次穿上了洁白的海军军服。就在一天前，她偷偷画了一幅漫画，想跟妈妈说说她在部队的生活，但这封信却并没有寄出去。不过，祁逸菲很想知道，父母是不是还在生她的气。", "More than three months of training passed, and the new recruits welcomed the graduation ceremony of the training. Qi Yifei put on the pure-white navy uniform for the first time. Just a day before, she had secretly drawn a cartoon wanting to tell her mother about her life in the army, but this letter was not sent out. (the book prints 没有 twice here) Still, Qi Yifei very much wanted to know whether her parents were still angry with her.")
R5 = ("因为祁逸菲表现优秀，部队要发奖给她。她走上领奖台，忽然发现，为她发奖的是她妈妈！妈妈和女儿都哭了。几天之后，祁逸菲到了海军陆战队。她还收到了妈妈的一封信。", "Because Qi Yifei performed excellently, the unit wanted to give her an award. She walked onto the podium and suddenly found that the one presenting her award was her mother! Mother and daughter both cried. A few days later Qi Yifei arrived at the Navy Marine Corps. She also received a letter from her mother.")
MI = [("祁逸菲考上清华大学美术学院，却在要上大二时决定参军，妈妈不支持。她在训练中表现优秀，结业仪式上，给她发奖的竟是妈妈，母女都哭了。妈妈后来在信里说，她理解女儿，也坚定地支持她。", "Activity 3D, main idea (my sample, in Chinese; the book asks for English): Qi Yifei got into Tsinghua’s Academy of Arts & Design but decided to join the army just before her second year, and her mother did not support her. She did excellently in training, and at the graduation ceremony the person who presented her award was her mother; both cried. Her mother later wrote in a letter that she understood her daughter and firmly supported her.")]
L4 = lesson(
    "Lesson 28 Presentation 2 using Chinese in context: from top student to marine, Qi Yifei and her mother",
    "祁逸菲 · 女学霸变身海军陆战队队员 · 参军 · 妈妈的信 · 惭愧 · 理解 · 坚定地支持",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 3 (Reading, Writing, and Speaking)",
             "When you were in China visiting your old friend last year, she talked about her old classmate 祁逸菲 (Qí Yìfēi), and mentioned that there is a report about this person entitled “女学霸变身海军陆战队队员.” You became interested and wanted to know more about her. A. The following three images, by 祁逸菲, are about Qí Yìfēi (also concerning her parents). Discuss them and the photo and answer the following questions with a classmate (the pictures are not included). 1. 在第一幅画里，一个刚参军的女孩儿，在队伍里偷偷地向后看。她好像有什么不放心的事。她大概在想什么？ 2. 在第二幅画里，这个女孩儿半夜在写信。她可能在给谁写信？她会说些什么？ 3. 第三幅画和最后的照片告诉你什么？ B. Below is part of a letter from Qí Yìfēi’s mother (it is given as a picture). Read it, then discuss what it is about with your partner. Revise your answers in Part A using what you learned from the letter. C. Below is the complete letter. Read it and answer the questions. 1. 她妈妈为什么掉眼泪？ 2. 她妈妈在信里为什么说，她有惭愧也有理解？ D. Read the report. Share the main idea from it with your friends in English. My answers, the letter, the report and a main idea:",
             examples=[D(z, e) for z, e in QA + LT + LQ] + [D(*R1), D(*R2), D(*R3), D(*R4), D(*R5)] + [D(z, e) for z, e in MI]),
    ],
    exercises=[
        M("Which university did Qi Yifei enter?", "Tsinghua University", ["Peking University", "Fudan University", "Harvard"], "考入了清华大学美术学院."),
        M("When did she decide to join the army?", "Just before her second year", ["Before high school", "After graduating", "In her first week"], "在就要上大二时，她却突然决定要参军."),
        M("What did her mother want her to become?", "A designer", ["A soldier", "A doctor", "A teacher"], "将来要当设计师."),
        M("What did Qi Yifei say about being a soldier and a Tsinghua student?", "A person who wanted to be a soldier got into Tsinghua", ["She hated Tsinghua", "She was forced to join", "She wanted to study abroad"], "是想当兵的人考上了清华."),
        M("What does the cartoon show?", "A woman soldier looking back among the new recruits", ["A student studying", "A mother cooking", "A ship at sea"], "有一个女兵在往后看."),
        M("What was she hoping for among the parents seeing recruits off?", "Her parents’ support", ["A gift", "A photo", "A ride"], "希望在最后一分钟得到他们的支持."),
        M("Who presented her award at the ceremony?", "Her mother", ["Her father", "The president", "Her teacher"], "为她发奖的是她妈妈."),
        M("What did her mother cry about when she saw the training video?", "Her daughter crawling under burning barbed wire", ["A sad movie", "A lost bag", "A bad grade"], "在燃烧的铁丝网下匍匐前进的女兵."),
        M("What does her mother say she now does?", "Firmly supports her", ["Forbids her", "Forgets her", "Fears her"], "妈妈现在坚定地支持你."),
        F("没得到父母同意她就参了___，她不停地在送行的家长中找爸爸妈妈的身影。", "军", ["书", "车", "话"], "参军: join the army."),
        F("三个月来，妈妈欠你一封___。", "信", ["书", "话", "字"], "一封信: a letter."),
        F("你们是“零零后”新生一代，妈妈或许曾经不能理___你。", "解", ["看", "想", "说"], "理解: understand."),
    ],
)

L5 = vocab_lesson("Lesson 28 Presentation 2 vocabulary", "12 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book writes 单车 for “bicycle” in this list although the text uses 共享单车.", VOC2)

UNIT = unit("第二十八课 Presentation 2: 零零后的环保意识, 零零后的特点, 胡剑, 一个美国九零后的观察, 祁逸菲, 词汇", [L1, L2, L3, L4, L5])
