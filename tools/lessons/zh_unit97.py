"""Unit 97: Lesson 29 (Education in China), Presentation 2, second half: Skill Integration (education and development, Hong Kong cram schools, education software,
sending a child abroad), Using Chinese in Context (the candy experiment, the PISA story, the study-stress checklist and suggestions, study tours) and the 16-word vocabulary.
Audio, video, pictures, the statistics image and the ranking chart are not included; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('又得上班', 1, 'dei3'), ('长见识', 0, 'zhang3'), ('总是觉得', 2, 'jue2'), ('中都是', 1, 'dou1')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]

# ------------------------------------------------------------------ 1. skill integration, activities 1-2
SI_T = table(["", "Educational spending per student (2018)", "Public expenditure as a share of GDP (2018)"], [["美国", "$13,600", "5.0%"], ["中国", "¥ 36,300", "4.11%"]], title="Activity 1A: the table (as printed; the two spending figures are in different currencies)")
SI_W = table(["Word", "Meaning (my glosses; the book leaves the meanings blank for the learner)"], [["占", "make up, account for"], ["水平", "level, standard"], ["付出", "pay, put in (effort or money)"], ["素质", "quality (of people)"], ["劳动力", "labor force, workforce"]], title="Word Meanings")
SI_P = ("大家都知道，最近几十年中国的发展很快。专家说，中国的发展和中国人的传统分不开。中国人的传统中有非常重要的一点，就是重视教育和学习。中国家庭为中国教育的发展付出了很多。全世界平均来说，国家花在教育上的钱占ＧＤＰ的百分之四点九，有的国家占到了百分之六以上，而中国只有百分之四点一，远远低于世界平均水平。中国学生的教育费大部分是每个家庭自己付的。正是因为有了每一个家庭的付出，才能让更多的孩子受到更好的教育，大大提高了人口素质，为国家的发展准备了高质量的劳动力。",
        "Activity 1B: Everyone knows that China has developed very fast in recent decades. Experts say that 1) [China’s development cannot be separated from the Chinese people’s traditions. One very important point in the Chinese tradition is the value placed on education and learning.] 2) [Chinese families have paid a great deal for the development of China’s education.] Worldwide, on average, the money a country spends on education makes up 4.9 percent of GDP, and some countries reach more than 6 percent, while China has only 4.1 percent, far below the world average. Most of Chinese students’ education costs are paid by each family itself. 3) [It is precisely because of each family’s contribution that more children could receive a better education, which greatly raised the quality of the population and prepared a high-quality labor force for the country’s development.] (the book marks sentences 1 to 3 in brackets for translation, writes GDP as Latin letters and the percentages in digits; the translation is mine)")
SI_A = [("国家的发展和教育分不开：中国的发展很快，是因为中国人重视教育，每个家庭为孩子的教育付出了很多。", "Activity 1A-1 / 1C (my answer): A country’s development cannot be separated from education: China developed fast because the Chinese value education and every family pays a great deal for it."),
        ("美国的公共教育支出占国内生产总值的百分之五，中国是百分之四点一一，所以中国国家花的钱比较少，家庭花的钱比较多。", "1A-2 / 1C (my answer): U.S. public expenditure is 5.0 percent of GDP and China’s is 4.11 percent, so the Chinese state spends less and families spend more."),
        ("中国的发展和中国人的传统分不开。", "Translations, 1 (my version of the book’s sentence 1; the book leaves translations blank): China’s development cannot be separated from the Chinese people’s traditions."),
        ("中国家庭为中国教育的发展付出了很多。", "2: Chinese families have paid a great deal for the development of China’s education."),
        ("正是因为有了每一个家庭的付出，才能让更多的孩子受到更好的教育。", "3 (first half): It is precisely because of every family’s contribution that more children can receive a better education.")]
L1 = lesson(
    "Lesson 29 Presentation 2 skill integration: education and a country’s development",
    "国家的发展和教育 · 占ＧＤＰ · 付出 · 水平 · 素质 · 劳动力",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Reading and Speaking)",
             "A. Pair up. In Chinese or English, discuss the following questions with your partner. 1. How is a country’s development related to education? 2. What can you tell from the information in the table below? B. Read the passage. Guess the meaning of the underlined words in context and translate the sentences in brackets. Compare your translations with your partner’s. C. How does the passage answer the two questions in Step A? (The underlining is lost in the text; the five words are listed in the table.)",
             tables=[SI_T, SI_W], examples=[D(SI_P[0], SI_P[1])] + [D(z, e) for z, e in SI_A]),
        card("Skill Integration, Activity 2 (Reading and Speaking)",
             "In groups of three, study the statistics below (a statistics image, which is not included). Discuss things that are not clear and share the two points that are most interesting to you with your group. The book has lines for “Unclear points” and “Interesting points”; it gives no key."),
    ],
    exercises=[
        M("What does the passage say about China’s development and tradition?", "They cannot be separated", ["They are unrelated", "Tradition stopped it", "It is slow"], "中国的发展和中国人的传统分不开."),
        M("What is an important point in the Chinese tradition?", "Valuing education and learning", ["Saving money", "Playing games", "Moving house"], "重视教育和学习."),
        M("What share of GDP does China spend on education, per the passage?", "4.1 percent", ["14 percent", "41 percent", "0.41 percent"], "中国只有百分之四点一."),
        M("What share is the world average, per the passage?", "4.9 percent", ["49 percent", "9 percent", "0.9 percent"], "占ＧＤＰ的百分之四点九."),
        M("Who pays most of Chinese students’ education costs?", "Each family itself", ["The state", "The school", "Companies"], "每个家庭自己付的."),
        M("What did families’ contributions help the country do?", "Raise population quality and prepare a high-quality labor force", ["Lower prices", "Close schools", "Avoid exams"], "提高了人口素质，准备了高质量的劳动力."),
        M("What does 水平 mean?", "Level", ["Water", "Flat roof", "Number"], "水平: level, standard."),
        M("What does 劳动力 mean?", "Labor force", ["Strength of will", "Teacher", "Machine"], "劳动力: labor force."),
        F("中国家庭为中国教育的发展付___了很多。", "出", ["进", "来", "去"], "付出: pay, contribute."),
        F("远远低于世界平均水___。", "平", ["高", "地", "面"], "水平: level."),
        F("大大提高了人口素___。", "质", ["数", "量", "好"], "素质: quality."),
    ],
)

# ------------------------------------------------------------------ 2. activity 3 and 4
HK = ("在香港，只有百分之十八的高中学生毕业以后能上大学。所以，学生们从小就要为大学考试而努力。从小学开始就有很多孩子参加补习班，到了高中，超过四分之三的香港学生都会参加补习班。有不少人说，大多数香港学生并不需要上补习班，但是补习班的广告让人们觉得，不上补习班就考不上大学。一些补习班的老师在Ｆａｃｅｂｏｏｋ上有大量的粉丝，有的明星补习老师年收入达到一千万港元，约一百三十万美元。",
      "Activity 3B: In Hong Kong, only 18 percent of high school students can go to university after graduating. So students work hard for the university exam from childhood. Many children attend tutoring classes beginning in elementary school, and by high school more than three quarters of Hong Kong students attend them. Quite a few people say that most Hong Kong students do not actually need tutoring classes, but the ads for tutoring classes make people feel that without them one cannot pass the university exam. Some tutoring teachers have a great many fans on Facebook, and some star tutors earn up to 10 million Hong Kong dollars a year, about 1.3 million U.S. dollars. (the book writes 18%, 3/4, Facebook, 1000万 and 130万 in digits and Latin letters; the photo is not included; translation mine)")
SW = [("跟兴趣班和补习班比起来，教育类软件可以说是“非常便宜”，但是它种类丰富，满足了很多家长的需要。", "Activity 3C: Compared with hobby classes and tutoring classes, educational software can be called “very cheap,” but it comes in rich variety and meets the needs of many parents. (translations mine)"),
      ("张云有两个女儿。大女儿十岁，上小学四年级；小女儿七岁，读一年级。除了上学和体育运动这样的兴趣班，别的课几乎都是在教育软件上完成的。", "Zhang Yun has two daughters. The elder is 10 and in fourth grade; the younger is 7 and in first grade. Apart from school and hobby classes such as sports, almost all other classes are completed on educational software. (the book writes 10 and 7 in digits)"),
      ("两年前，张云在给孩子选择课程时，发现许多喜欢的课在当地都很难找到，所以，她就转向了种类丰富的教育应用软件。张云给孩子们选择的课程一般每个三百到四百元，两个孩子可以一起使用。", "Two years ago, when choosing courses for her children, Zhang Yun found that many of the classes she liked were hard to find locally, so she turned to educational apps with a rich variety. The courses she chooses for the children generally cost 300 to 400 yuan each, and the two children can use them together. (the book writes 300 and 400 in digits)")]
SWA = [("教育软件。", "Activity 3C-1 (my answer): Educational software (online courses and apps)."),
       ("因为教育软件比兴趣班和补习班便宜得多，种类丰富，满足很多家长的需要，而且当地很难找到喜欢的课。", "3C-2 (my answer): Because educational software is much cheaper than hobby and tutoring classes, has rich variety, meets many parents’ needs, and the classes they like are hard to find locally.")]
HKA = [("因为补习班的广告让人们觉得，不上补习班就考不上大学。", "Activity 3B-1 (my answer): Because the ads for tutoring classes make people feel that without them they cannot pass the university exam; star tutors also earn a great deal, and only a small share of students can enter university.")]
ZL1 = ("跟兴趣班和补习班比，送孩子出国简直可以说是“天价”。在深圳工作的一位老师张林说，去年，她把十岁的女儿送到国外上学，所有费用加在一起，大概三百多万人民币。每天下班后，张林都会同女儿视频聊天，问问她生活上是不是适应，学习上需要什么帮助。不过，她还是不太放心，她说，“我很想去国外陪读，但是又得上班赚钱。”",
       "Activity 3D, Paragraph 1: Compared with hobby classes and tutoring classes, sending a child abroad can simply be called a “sky-high price.” Zhang Lin, a teacher who works in Shenzhen, says that last year she sent her ten-year-old daughter to study abroad, and all the costs added together were about three million-plus yuan. Every day after work Zhang Lin video-chats with her daughter, asking whether she is adapting in daily life and what help she needs in her studies. But she is still a bit worried; she says, “I very much want to go abroad to accompany her studies, but I also have to go to work to earn money.” (the book writes 十岁 as printed; translation mine)")
ZL2 = ("有朋友问她，为什么要让自己这么辛苦？让女儿在国内读书不好吗？但张林说，“花这么多钱，我的压力当然也很大，但我觉得国外的教育可能更适合她。孩子在国内学习压力太大，而且，为了让孩子能考上好学校，家长们花在补习班上的钱甚至比送孩子出国更多。除了花钱，父母们还要花时间陪孩子学习，接送孩子上学放学。跟他们比，我更轻松一些。”",
       "Paragraph 2: A friend asked her, why make yourself so tired? Wouldn’t it be good to let your daughter study in China? But Zhang Lin says, “Spending this much money, of course my pressure is also great, but I feel that education abroad may suit her better. The pressure of studying in China is too great for children, and moreover, to get their children into good schools, parents spend even more on tutoring classes than on sending their children abroad. Besides spending money, parents also have to spend time accompanying children’s studies and taking them to and from school. Compared with them, I am a little more relaxed.”")
ZLA = [("她花了三百多万人民币，把十岁的女儿送到国外上学，所有的费用加在一起。", "Activity 3D-1 (my answer): She spent over three million yuan to send her ten-year-old daughter abroad, all costs added together."),
       ("每天下班后，她都同女儿视频聊天。", "3D-2: Every day after work she video-chats with her daughter."),
       ("她很想去国外陪女儿读书，但是又得上班赚钱。", "3D-3: She would like to go abroad to accompany her daughter’s studies, but also has to work to earn money."),
       ("孩子在国内学习压力太大，家长花在补习班上的钱甚至比送孩子出国更多，而且国外的教育可能更适合她。", "3D-4: The pressure in China is too great for children, parents spend even more on tutoring than on going abroad, and she thinks foreign education may suit her daughter better.")]
L2 = lesson(
    "Lesson 29 Presentation 2 skill integration: cram schools in Hong Kong, education software, and sending a child abroad",
    "香港补习班 · 教育类软件 · 张云的两个女儿 · 张林送女儿出国 · 天价 · 陪读",
    requires=[],
    cards=[
        card("Skill Integration, Activity 3 (Reading, Listening, and Speaking): A and B",
             "A. Listen to the passage and answer the questions. 1. What was said in the passage about changes made by the parents? 2. When did they make this change, and why? 3. How do parents feel about the cost? (Audio, so I give no key.) B. Read the passage and answer the question. 1. According to the passage, why is 补习班 prosperous in Hong Kong? (The photo is not included.)",
             examples=[D(*HK)] + [D(z, e) for z, e in HKA]),
        card("Activity 3 C and D",
             "C. Read the passage and answer the questions. 1. What are some alternate choices parents can make for their children’s education, other than hobby classes and “cram” schools? 2. Why would parents make this choice? D. Pair up. Each partner reads one paragraph of the passage. Tell your partner the information in your part, and then answer the questions together. 1. How much money did this mother spend, and how was it spent? 2. How does the mother keep in contact with her child? 3. What is her dilemma? 4. What caused her decision?",
             examples=[D(z, e) for z, e in SW + SWA] + [D(*ZL1), D(*ZL2)] + [D(z, e) for z, e in ZLA]),
        card("Skill Integration, Activity 4 (Listening, Speaking, and Reading)",
             "Listen to the passage and answer the following questions. Discuss your work with your partner. 1. What is the main idea of the passage? 2. How did the author explain their point of view? 3. What are common misconceptions among parents? (Audio, so I give no key.)"),
    ],
    exercises=[
        M("What share of Hong Kong high-school students can go to university?", "18 percent", ["81 percent", "8 percent", "180 percent"], "只有百分之十八."),
        M("What share of Hong Kong high schoolers attend tutoring classes, per the passage?", "More than three quarters", ["About a tenth", "Nobody", "Half of one class"], "超过四分之三."),
        M("What do tutoring ads make people feel?", "That without tutoring they cannot pass the university exam", ["That exams are easy", "That school is free", "That tutoring is bad"], "不上补习班就考不上大学."),
        M("How does the passage describe educational software compared with hobby classes?", "Very cheap", ["Very rare", "Very slow", "Very hard"], "可以说是“非常便宜”."),
        M("Why did Zhang Yun turn to educational apps?", "Many classes she liked were hard to find locally", ["Apps are free", "Her daughters dislike school", "She dislikes sports"], "许多喜欢的课在当地都很难找到."),
        M("What did Zhang Lin pay roughly to send her daughter abroad?", "More than three million yuan", ["Three hundred yuan", "Thirty yuan", "Three thousand dollars"], "大概三百多万人民币."),
        M("How does Zhang Lin keep in touch with her daughter?", "Daily video chat after work", ["Weekly letters", "Visits every month", "Telegrams"], "每天下班后同女儿视频聊天."),
        M("What is Zhang Lin’s dilemma?", "She wants to accompany her daughter abroad but has to work", ["She can’t cook", "She dislikes the country", "She can’t find a school"], "很想去国外陪读，但是又得上班赚钱."),
        F("在香港，只有百分之十八的高中学生毕业以后能上___学。", "大", ["中", "小", "老"], "上大学."),
        F("跟兴趣班和补习班比，送孩子出国简直可以说是“天___”。", "价", ["上", "高", "大"], "天价: sky-high price."),
        F("我很想去国外陪读，但是又得上___赚钱。", "班", ["课", "学", "房"], "上班: go to work."),
    ],
)

# ------------------------------------------------------------------ 3. using chinese act 1, 2
MS = ("十几年后，人们发现，当年面对糖等候时间长，最长的三分之一的孩子，在学习上超过等候时间短，最短的三分之一的孩子，他们的大学入学考试分数比等候时间最短的三分之一的孩子高出了二百一十分，满分一千六百分。这些等待时间长的小孩，不仅后来学习成绩更好，而且在生活的各个方面也都更有优势，他们比较少做不成熟的事；工作更努力；而且在三十岁左右的时候，他们的身体也比那些等候时间短的孩子们更健康。这大概就是大部分中国父母的想法：为了以后更好的生活，现在吃苦和努力都是应该的，他们不仅这样要求自己，也这样要求孩子。",
      "Activity 1C: More than ten years later, people found that the children who had waited longest for the candy (the longest third) did better in their studies than the children who waited the shortest time (the shortest third): their university entrance exam scores were 210 points higher (out of 1600) than those of the shortest-waiting third. These long-waiting children not only later had better grades but were also better off in many other aspects of life: they did fewer immature things, worked harder, and at around the age of 30 were also healthier than the children who waited a short time. This is probably the thought of most Chinese parents: for a better life later, suffering and working hard now is only right; they make this demand not only of themselves but also of their children. (the book writes 1/3, 210, 1600 and 30 in digits and puts the fractions in brackets; the book’s sentence “面对糖等候时间长” is kept as printed; translation mine)")
PISAT = table(["", "Information (English in the book; the 2018 ranking chart is not included)"], [["PISA", "A worldwide study intended to evaluate educational systems by measuring 15-year-old school pupils’ scholastic performance on mathematics, science, and reading. The test measures problem solving and cognition skills."], ["PISA 2018", "Included data for around 600,000 participating students in 79 countries and economies."]], title="Activity 2A (Reading, Listening, and Speaking)")
GLT = table(["Word", "Pinyin", "English (the book’s brackets in the story)"], [["赶上", "gǎnshàng", "catch up with"], ["科学", "kēxué", "science"]], title="Glosses in the story, moved here from the spoken text")
STY = ("我从小就害怕考试，十六岁到中国上海留学的时候，我才知道中国的考试比美国多得多。一年以后我回到美国，所有的老师都问我：中国的高中跟美国的高中有什么不一样？我们怎么才能赶上中国的高中？他们的担心是有道理的。在二零一零年的ＰＩＳＡ考试中，中国上海的学生在数学、阅读和科学三个考试中都是第一，而美国平均排在全世界的第二十三、二十四名。从那以后我更害怕考试了，连我的父母都开始给我压力，说我应该像中国学生那样努力学习。但是上大学以后，这样的担心就减少了。大学三年级我是在中国北京的一所大学读的。虽然我没有参加过中国的高考，但是我发现学习对我来说并不是很难，我也没有觉得我的中国同学比我聪明很多，而且上课和写作业都是用我的第三语言——中文。如果考试没有那么重要，可能我从小就不应该那么害怕它？",
       "Activity 2C: I have been afraid of exams since childhood. When I went to study in Shanghai, China, at sixteen, I learned that China has far more exams than the U.S. A year later I returned to the U.S., and all the teachers asked me: How are Chinese high schools different from American ones? How can we catch up with China’s high schools? Their worry was justified. In the 2010 PISA test, students from Shanghai were first in all three tests, mathematics, reading and science, while the U.S. ranked on average 23rd and 24th in the world. After that I was even more afraid of exams; even my parents began to put pressure on me, saying I should study as hard as Chinese students. But after I went to university, such worries decreased. In my third year I studied at a university in Beijing, China. Although I had never taken the Chinese gaokao, I found that studying was not very hard for me, nor did I feel that my Chinese classmates were much smarter than I, and classes and homework were all in my third language, Chinese. If exams are not that important, perhaps I should not have been so afraid of them from childhood? (adapted from a newspaper article; the source site is left out; the book writes 16, 2010 and 23, 24 in digits and gives the glosses in brackets; translation mine)")
ORG = ("不过，我一到了大学，这些担心就减少了。我大三时在清华读了一学期的进修课。我当时的同学确实很聪明和友好，求知欲也很强。但不管我有没有参加过高考，我跟他们一起学习从来没有觉得吃力，同时也没有觉得同学比我聪明得多，而上课和写作业时用的都是我的第三语言——中文。我在清华上的课大多都是历史系的课，而我很快发现我可以利用我在美国做独立历史研究的经验来对我们班的讨论作出贡献。",
       "Activity 2D, part of the original article: But as soon as I got to university, these worries decreased. In my third year I took a one-semester advanced course at Tsinghua. My classmates at the time were indeed very smart and friendly, with a strong thirst for knowledge. But whether or not I had taken the gaokao, I never felt it was a strain to study with them, and I did not feel my classmates were much smarter than I, while classes and homework were in my third language, Chinese. Most of the classes I took at Tsinghua were history-department classes, and I quickly found that I could use my experience of independent historical research in the U.S. to contribute to our class discussions. (translation mine; the book asks the learner to use machine translation on the reason part)")
ORGA = [("他在清华上的课大多是历史系的课，他可以利用自己在美国做独立历史研究的经验来对班上的讨论作出贡献，所以他不觉得吃力。", "Activity 2D, Reason (my answer): Most of his classes at Tsinghua were history classes, and he could use his experience of independent historical research in the U.S. to contribute to class discussions, so he did not find it a strain."),
        ("考试多的压力不一定让人学得更好，他的聪明和努力不比中国同学差。", "2C (my own possible discussion point; the book gives no answer): The pressure of many exams does not necessarily make people learn better; his intelligence and effort were not inferior to his Chinese classmates’.")]
L3 = lesson(
    "Lesson 29 Presentation 2 using Chinese in context: the candy experiment and a PISA story",
    "糖的实验 · 等候时间 · 吃苦和努力 · 上海留学 · ＰＩＳＡ考试 · 清华 · 第三语言",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Listening, Reading, and Speaking)",
             "A. In groups of three, watch the video and, in Chinese, describe what happened. B. In groups of three, listen to the social-science research experiment conducted in 1972 and discuss the question at the end. (The video and audio are not included; no key.) C. Read the findings of the experiment and compare it with your discussion.",
             examples=[D(*MS)]),
        card("Activity 2 (Reading, Listening, and Speaking)",
             "A. In groups of three, read the following information and discuss the 2018 test results with your partners (the book tells you to open a link for the ranking results, which is not included). B. Share your group’s thoughts with the class. C. Read a story about the pressure a U.S. student experienced when taking the PISA test. What information in his story is most interesting to you? Share it with your group, then discuss the possible reason for his ability to study well at the Chinese university that is revealed at the end of the story. D. Below is part of the original article. Find the reason for his ability to study well at the Chinese university in this paragraph. Use Google Translate to translate that particular part.",
             tables=[PISAT, GLT], examples=[D(*STY), D(*ORG)] + [D(z, e) for z, e in ORGA]),
    ],
    exercises=[
        M("What did people find years after the candy experiment?", "Children who waited longer did better in their studies", ["Children who waited longer did worse", "No difference", "All were sick"], "等候时间长的孩子，在学习上超过等候时间短的孩子."),
        M("How many points higher were the long-waiting children’s exam scores?", "210", ["21", "2100", "12"], "高出了二百一十分."),
        M("What was the full score of the exam mentioned?", "1600", ["160", "600", "16"], "满分一千六百分."),
        M("About how old were the children when the health comparison was made?", "Around thirty", ["Around ten", "Around sixty", "Around fifteen"], "三十岁左右."),
        M("What do most Chinese parents think, according to the passage?", "Hardship and hard work now is right, for a better life later", ["Children should play more", "Money is unimportant", "Exams are useless"], "现在吃苦和努力都是应该的."),
        M("How old was the U.S. student when he went to study in Shanghai?", "Sixteen", ["Six", "Twenty-six", "Sixty"], "十六岁到中国上海留学."),
        M("In which test were Shanghai students first in all three subjects?", "The 2010 PISA test", ["The 2018 gaokao", "A 1972 test", "A local quiz"], "在二零一零年的ＰＩＳＡ考试中."),
        M("Why did the American student not find studying at Tsinghua hard?", "He could use his experience of independent history research", ["He skipped classes", "He knew nobody", "He studied in English"], "可以利用我在美国做独立历史研究的经验."),
        F("这些等待时间长的小孩，不仅后来学习成绩更好，而且在生活的各个方面也都更有优___。", "势", ["点", "事", "示"], "优势: advantage."),
        F("我从小就害怕考试，十六岁到中国上海留___的时候。", "学", ["书", "习", "校"], "留学: study abroad."),
        F("我没有觉得我的中国同学比我聪明很___。", "多", ["少", "大", "好"], "聪明很多: much smarter."),
    ],
)

# ------------------------------------------------------------------ 4. using chinese act 3, 4
CK = ["上次考试考得不好", "学习上有困难的时候，我不知道该怎么办", "老师讲的我听不懂", "上课有的东西没听懂，但是我不想问老师", "上课的时候没有办法好好听课，总是想到别的东西", "我觉得老师不太关心学生", "我不知道自己能不能学好", "我觉得作业太多了", "有时候很难完成作业", "学习上的竞争太厉害了", "需要太多时间学习，没有时间锻炼和玩儿", "体重减少或增加了", "总是觉得累，睡觉时间变长或变短了", "学习和考试给我很大的压力", "我没有朋友", "我觉得没有人关心我", "以前喜欢做的事现在没有兴趣了"]
CKE = ["Activity 3A, “你有学习压力吗？” Check the items that apply to you; 1. I did poorly on the last exam. (the book gives no key; translations mine)", "2. When I have difficulty in my studies, I don’t know what to do.", "3. I can’t understand what the teacher says.", "4. In class there are things I didn’t understand, but I don’t want to ask the teacher.", "5. In class I can’t listen properly; I’m always thinking of other things.", "6. I feel the teacher doesn’t care much about students.", "7. I don’t know whether I can learn well.", "8. I feel there is too much homework.", "9. Sometimes it is hard to finish homework.", "10. The competition in studies is too fierce.", "11. I need too much time to study and have no time to exercise and play. (玩儿 as printed)", "12. My weight has decreased or increased. (the book writes 减少/增加 with a slash)", "13. I always feel tired; my sleep time has become longer or shorter. (the book writes 变长/变短 with a slash)", "14. Studies and exams give me great pressure.", "15. I have no friends.", "16. I feel nobody cares about me.", "17. I am no longer interested in things I used to like doing."]
SUG = [("学习压力大怎么办呢？试试这些办法吧！", "Activity 3D: What to do about heavy study stress? Try these methods! (translations mine)"),
       ("首先要理解，生活中每个人都有压力，不要害怕压力。", "1. First understand that everyone in life has pressure; don’t be afraid of pressure."),
       ("制定一个学习计划，每天坚持完成当天的计划。", "2. Make a study plan and keep finishing that day’s plan every day."),
       ("不懂的问题及时问老师或同学。", "3. Ask the teacher or classmates promptly about questions you don’t understand."),
       ("体育锻炼。体育运动是减压的好办法。在周末你还可以跟朋友一起爬山、打球等。", "4. Physical exercise. Sports are a good way to reduce stress. On weekends you can also go hiking or play ball with friends."),
       ("把压力写下来。写出来以后你可能会发现，这些压力没有你想的那么严重。", "5. Write the stress down. After writing it out you may find that the stress is not as serious as you thought."),
       ("一定要有足够的睡觉时间。睡觉前把所有的电子产品都关上。", "6. Be sure to have enough sleeping time. Turn off all electronic products before sleep."),
       ("吃好饭。有的人觉得学习辛苦，应该多吃大鱼大肉。还有的人觉得学习紧张的时候吃点儿零食会开心起来。但这些想法都不对，应该多吃一些新鲜的蔬菜和水果。", "7. Eat well. Some people think study is hard and one should eat lots of fish and meat. Others think that when study is tense eating some snacks will cheer them up. But these ideas are all wrong; one should eat more fresh vegetables and fruit. (the book’s items 7 and 8 split this sentence after 学习紧张的时候, which looks like a layout slip, so I join them here and the following items are numbered 8 and 9 in my reading)"),
       ("闻香气。很多人闻到香气会觉得轻松快乐。", "8 (the book’s 9). Smell fragrances. Many people feel relaxed and happy when they smell a fragrance."),
       ("根据自己的爱好做一些活动，当你学习累了，可以出去打球，跑步，散步，也可以阅读，听歌，跳舞。", "9 (the book’s 10). Do some activities according to your hobbies; when you are tired from studying you can go out to play ball, run, or take a walk, or you can read, listen to songs, or dance.")]
SUGM = ("我觉得体育锻炼对我最有用，学习累了的时候我会出去跑步，也会跟朋友一起打球。", "Activity 3C (my possible answer; the book gives none): I find exercise most useful; when I am tired from studying I go running and also play ball with friends.")
YX = ("“游学”就是离开自己生活的地方，到另一个全新的环境学习和旅游，体验当地生活。近些年来，越来越多的中国家庭有能力而且愿意为孩子的教育花更多的钱，游学也成了孩子培养计划中的一个。这几年参加游学的学生不断增加，他们主要是去一些英语国家，比如英国、美国、加拿大、澳大利亚等。一位家庭月收入约三万的家长说，自己为了让孩子去英国游学一个月，花了十万。可看到孩子回来后长见识了，更自信了，认识了很多朋友，所以想有机会让孩子再去一次。",
      "Activity 4A: “Study tour” means leaving the place where you live and going to a completely new environment to study and travel, experiencing local life. In recent years more and more Chinese families have the ability and the willingness to spend more money on their children’s education, and study tours have become one part of children’s development plans. In the past few years the number of students on study tours has kept increasing; they mainly go to English-speaking countries such as the U.K., the U.S., Canada and Australia. A parent whose family’s monthly income is about 30,000 said that to send her child on a one-month study tour in the U.K. she spent 100,000. But seeing the child return having broadened their horizons, more self-confident and having made many friends, she wants to give the child another chance. (the book writes 30,000 as 三万 and 100,000 as 十万 in Chinese already; the photo is not included; translation mine)")
YXA = [("第一部分：什么是游学。第二部分：越来越多的家庭愿意花钱让孩子游学，学生主要去英语国家。第三部分：一位家长的例子。", "Activity 4A, Sections (my division; the book gives lines for learners): One: what a study tour is. Two: more and more families are willing to spend money on study tours, mostly to English-speaking countries. Three: one parent’s example."),
       ("游学的好处有：长见识，更自信，认识很多朋友，提高外语水平，体验当地生活。", "Activity 4C (my list of benefits; the book leaves the list to the learners, and 4D is audio, so there is no key for that): Broader horizons, more self-confidence, making many friends, improving foreign-language level, experiencing local life.")]
L4 = lesson(
    "Lesson 29 Presentation 2 using Chinese in context: study stress and study tours",
    "你有学习压力吗 · 压力大怎么办 · 体育锻炼 · 足够的睡觉时间 · 游学 · 长见识 · 更自信",
    requires=[],
    cards=[
        card("Activity 3 (Reading and Speaking): the stress checklist",
             "A. Check the items that apply to you to see if you experience stress from your studies. B. Do you experience other symptoms of stress? Share your information with your partner and add it to the above list (the book gives five blank lines). C. What are useful ways for you to reduce stress while studying? Share your thoughts with the class. D. Read the following suggestions for reducing study stress. Find any that may be useful to you. (The three small pictures are not included.)",
             examples=[D(z, e) for z, e in zip(CK, CKE)] + [D(z, e) for z, e in SUG] + [D(*SUGM)]),
        card("Activity 4 (Reading, Listening and Speaking): study tours",
             "A. Read the passage about a “study tour.” Divide the passage into a few sections and summarize the main idea of each section. Compare your work with a classmate’s. B. Do you have any study tour experiences? If yes, your partners will write some questions to ask you about your experience. C. What are the benefits of study tours? Discuss with your partners and list them below. D. Listen to a list of benefits of study tours and take notes. Note the items not included in your list. (The book gives lines for the summary, sections and notes.)",
             examples=[D(*YX)] + [D(z, e) for z, e in YXA]),
    ],
    exercises=[
        M("What does the first stress-reduction suggestion say?", "Everyone has pressure; don’t be afraid of it", ["Avoid all pressure", "Only students have pressure", "Pressure is good for sleep"], "生活中每个人都有压力，不要害怕压力."),
        M("What should you make to reduce study stress?", "A study plan", ["A new school", "A budget", "A trip"], "制定一个学习计划."),
        M("What does the passage say about sports?", "They are a good way to reduce stress", ["They cause stress", "They waste time", "They are only for weekends"], "体育运动是减压的好办法."),
        M("What should you do before sleep?", "Turn off all electronic products", ["Eat a snack", "Do homework", "Run"], "睡觉前把所有的电子产品都关上."),
        M("What does the passage advise about eating?", "Eat more fresh vegetables and fruit", ["Eat lots of fish and meat", "Eat more snacks", "Skip meals"], "应该多吃一些新鲜的蔬菜和水果."),
        M("What is a “study tour” (游学)?", "Leaving home to study and travel in a completely new environment", ["Studying at home online", "A school exam", "A school uniform"], "离开自己生活的地方，到另一个全新的环境学习和旅游."),
        M("Where do students on study tours mainly go?", "English-speaking countries", ["Only Asian countries", "Only Africa", "Only nearby towns"], "主要是去一些英语国家."),
        M("How much did the parent in the passage spend on the one-month tour?", "A hundred thousand", ["A thousand", "A hundred", "Ten"], "花了十万."),
        F("体育运动是减压的好办___。", "法", ["子", "式", "事"], "办法: method."),
        F("很多人闻到香气会觉得轻松快___。", "乐", ["了", "活", "平"], "快乐: happy."),
        F("可看到孩子回来后长见识了，更自___了。", "信", ["己", "由", "古"], "自信: self-confident."),
    ],
)

# ------------------------------------------------------------------ 5. vocabulary
L5 = vocab_lesson("Lesson 29 Presentation 2 vocabulary", "16 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第二十九课 中国的教育 Presentation 2: 综合技能, 语境中的汉语, 词汇", [L1, L2, L3, L4, L5])
