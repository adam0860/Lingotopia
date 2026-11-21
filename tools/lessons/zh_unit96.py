"""Unit 96: Lesson 29 (Education in China), Presentation 2, first half: Getting Started, the passage on valuing education, Activities 1-5 and the Grammar and Usage section
(再…也… and 不管…都…, 好 indicating purpose, 在…的同时, 用在…上).
Audio and pictures are not included; the traditional-character copy of the passage is not repeated; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('舍不得', 0, 'she3'), ('长大', 0, 'zhang3'), ('睡不好觉', 3, 'jiao4')):
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
NOUN = ["前途", "目标", "材料"]

# ------------------------------------------------------------------ 1. presentation 2 and activities 1-3
P2 = [("重视教育是中国人的传统。两千多年前，孔子就说过，人人都应该受教育，社会的发展和教育分不开。现在的中国人特别重视孩子的教育，因为他们相信，有了好的教育，孩子才能有更好的前途。", "Valuing education is a tradition of the Chinese people. More than two thousand years ago Confucius already said that everyone should receive an education and that the development of society cannot be separated from education. Today’s Chinese people especially value their children’s education, because they believe that only with a good education can children have a better future. (Presentation 2; translations mine; the traditional-character copy is not repeated)"),
      ("为了让孩子从小就受到很好的教育，孩子两三岁时，家长就会把他们送到早教班。到了孩子上学的年龄，一些家庭还会买很贵的学区房，好让孩子上更好的学校。上学以后，家长们还会送孩子上补习班和兴趣班，来提高他们的学习和各方面的能力。", "To give children a very good education from an early age, when children are two or three years old, parents send them to early-education classes. When the children reach school age, some families also buy very expensive homes in a good school district so that the children can go to better schools. After they start school, parents also send them to tutoring classes and interest classes to improve their studies and abilities in all respects."),
      ("中国家长在孩子的教育上花的钱是最多的。父母们舍不得给自己花钱，但只要对孩子的教育有好处，再多的钱他们也愿意花，每个家庭百分之三十的钱都会用在孩子身上。", "Chinese parents spend the most money on their children’s education. Parents are reluctant to spend money on themselves, but as long as it benefits their children’s education, they are willing to spend however much money it takes; thirty percent of each family’s money is spent on the children. (the book writes 30% in digits)"),
      ("家长们重视教育是对的，但是，有的时候会使孩子感觉压力太大。有的孩子睡觉时间不够，有的失去学习兴趣，还有的跟父母的关系变得紧张起来。所以，家长们在重视教育的同时，也要关心孩子的身心健康。", "It is right for parents to value education, but sometimes it makes children feel too much pressure. Some children don’t get enough sleep, some lose interest in learning, and some become tense in their relationship with their parents. So while valuing education, parents should also care about their children’s physical and mental health.")]
GS = ("Pair up. Discuss the following questions with your partner. A. What is your impression of education in China? B. Do you think children’s education is the responsibility of schools, or the family? C. What role does family play in the education of their children? D. What aspect of your early education do you think was the most successful and which was most in need of improvement? E. Do you think education has a significant impact on a person’s development? Provide an example. (The pictures, of a statue of Confucius at a middle school and of middle school students, are not included; the book gives no answers.)")
A1 = [("这篇文章的主要意思是：中国的家长很重视孩子的教育，花很多钱，但也要关心孩子的身心健康。", "Activity 1A-1 (my answer): The main idea is that Chinese parents value their children’s education and spend a lot of money, but should also care about their physical and mental health."),
      ("小话题有：重视教育的传统，家长为孩子做的事，花的钱，教育太重视的坏处和建议。", "1A-2 (my answer): The subtopics: the tradition of valuing education, what parents do for their children, the money spent, and the negative effects of overvaluing education with a suggestion."),
      ("孔子说过，人人都应该受教育，社会的发展和教育分不开。", "1B-1 (my answer): Confucius said everyone should receive an education and that society’s development cannot be separated from education."),
      ("因为他们相信，有了好的教育，孩子才能有更好的前途。", "1B-2 (my answer): Because they believe that only with a good education can children have a better future."),
      ("把孩子送到早教班，买学区房，送孩子上补习班和兴趣班。", "1B-3 (my answer): They send them to early-education classes, buy school-district homes, and send them to tutoring and interest classes."),
      ("每个家庭百分之三十的钱都会用在孩子身上。", "1B-4 (my answer): Thirty percent of each family’s money is spent on the children."),
      ("孩子感觉压力太大，睡觉时间不够，失去学习兴趣，跟父母的关系变得紧张。", "1B-5 (my answer): Children feel too much pressure, don’t sleep enough, lose interest in learning and become tense with their parents."),
      ("家长们在重视教育的同时，也要关心孩子的身心健康。", "1B-6 (my answer): While valuing education, parents should also care about their children’s physical and mental health.")]
A2T = table(["Category", "Items (my sort; the book gives sixteen items and empty categories)"], [["Reason", "相信，传统，孩子的前途，国家的发展"], ["What Parents Do for Children", "早教班，兴趣班，补习班，买学区房，提高孩子的能力"], ["Attitude Toward Money", "舍不得给自己花钱，再多的钱也愿意为孩子花"], ["Negative Effects and Suggestions", "失去学习兴趣，和父母关系紧张，感觉压力大，关心身心健康"]], title="Activity 2: sorting the items into the categories (重视教育的中国人 is the heading of the exercise; the items: 相信 早教班 传统 兴趣班 补习班 失去学习兴趣 关心身心健康 舍不得给自己花钱 孩子的前途 国家的发展 买学区房 提高孩子的能力 和父母关系紧张 感觉压力大 再多的钱也愿意为孩子花)")
L1 = lesson(
    "Lesson 29 Presentation 2: valuing education is a Chinese tradition",
    "重视教育 · 孔子 · 早教班 · 学区房 · 补习班 · 舍不得给自己花钱 · 压力太大 · 身心健康",
    requires=[],
    cards=[
        card("Presentation 2: Getting Started", GS),
        card("Presentation 2: valuing education", "A passage on the tradition of valuing education and its cost.", examples=[D(z, e) for z, e in P2]),
        card("Presentation 2 Activities, Activities 1 to 3",
             "Activity 1 (Listening): A. Global Listening: Listen to Presentation 2 once and answer the questions. 1. What’s the main idea of the passage? 2. What are the subtopics of this main idea? B. Detailed Listening: Listen to Presentation 2 again and answer the questions. 1. What did Confucius say about education? 2. Why do parents value their children’s education? 3. What did the parents do to provide good education for their children? 4. What statistic is provided on how much Chinese parents spend on their children’s education? 5. What are some of the negative effects of placing excessive value on a child’s education? 6. What is suggested to balance out any negative effects? Activity 2 (Reading): Sort the following words into the correct categories. Activity 3 (Listening): A. Listen to the passage about Confucius and answer the questions. Pair up and discuss your answers with your partner. 1. According to this passage, what is profound about Confucius? 2. What did you hear about the conversation between Confucius and his students? 3. Why did Confucius value the education of ordinary people? (Activity 3 is audio, so I give no key.) My answers and sort:",
             tables=[A2T], examples=[D(z, e) for z, e in A1]),
    ],
    exercises=[
        M("When did Confucius say everyone should receive an education?", "More than two thousand years ago", ["Last year", "Two hundred years ago", "Ten years ago"], "两千多年前，孔子就说过."),
        M("Why do Chinese people value their children’s education so much?", "They believe a good education gives a better future", ["It is required by law", "It is free", "It is easy"], "有了好的教育，孩子才能有更好的前途."),
        M("At what age might parents send children to early-education classes?", "Two or three", ["Ten", "Fifteen", "Twenty"], "孩子两三岁时."),
        M("Why do some families buy expensive school-district homes?", "So the children can go to better schools", ["To rent them out", "To avoid taxes", "To have a garden"], "好让孩子上更好的学校."),
        M("What share of each family’s money goes to children, according to the passage?", "Thirty percent", ["Three percent", "Three hundred percent", "Nothing"], "每个家庭百分之三十的钱都会用在孩子身上."),
        M("What are parents unwilling to do?", "Spend money on themselves", ["Spend money on children", "Work", "Cook"], "父母们舍不得给自己花钱."),
        M("Which is a negative effect named in the passage?", "Children lose interest in learning", ["Children read too much", "Children grow too fast", "Children sleep too long"], "有的失去学习兴趣."),
        M("What should parents do while valuing education?", "Also care about children’s physical and mental health", ["Stop valuing education", "Spend more money", "Send children abroad"], "也要关心孩子的身心健康."),
        F("现在的中国人特别重视孩子的教___。", "育", ["书", "学", "师"], "教育: education."),
        F("中国家长在孩子的教育上花的钱是最___的。", "多", ["少", "大", "高"], "最多: the most."),
        F("有的孩子睡___时间不够。", "觉", ["看", "想", "说"], "睡觉: sleep."),
    ],
)

# ------------------------------------------------------------------ 2. activities 4-5 and 再...也...
C4Q = "一个普通的中国家庭会把多少钱花在孩子的教育上呢？"
C4 = [(C4Q, "Activity 4 (sight translation; translations mine): How much money does an ordinary Chinese family spend on their children’s education?"),
      ("从孩子出生到大学毕业，一般来说，一个孩子的教育费是五十到一百三十万人民币。如果送孩子出国留学，那这个数字最少也会达到两百万人民币。准备这么多钱，对每个普通家庭来说，都是很大的压力。平均来说，父母会把百分之十五的钱花在孩子现在的教育上，还会把百分之十八的钱存起来，为孩子以后的教育做准备。这些钱都是直接用在孩子的教育上的，另外，还有一些钱也是为了孩子的教育花的，比如买学区房就是很多家庭的选择。", "From a child’s birth to university graduation, generally speaking, a child’s education costs between 500,000 and 1,300,000 yuan. If the child is sent abroad to study, this figure will reach at least 2,000,000 yuan. Preparing this much money is a great pressure for every ordinary family. On average, parents spend 15 percent of their money on the child’s present education and save 18 percent for the child’s future education. This money is spent directly on the child’s education; in addition, some other money is also spent for the child’s education, for example buying a school-district home is the choice of many families. (the book writes 50, 130, 200, 15% and 18% in digits)")]
C5 = [("在中国，上了小学三年级以后，就有百分之七十以上的学生感觉到学习压力太大。学生的作业太多，考试太多。很多孩子除了在学校的八个小时以外，还要上补习班、兴趣班，连周末也没有时间休息。而且，每个学生都有升学考试的压力，不光上中学要考试，上大学要考试，甚至上小学也要考试。", "Activity 5: In China, after the third year of elementary school more than 70 percent of students feel too much pressure in their studies. Students have too much homework and too many exams. Many children, besides the eight hours at school, also attend tutoring classes and interest classes and have no time to rest even on weekends. Moreover, every student faces the pressure of entrance exams: not only is there an exam for middle school and for university, there is even an exam for elementary school. (translations mine; the book writes 70% in digits)"),
      ("因为压力太大，有的孩子不愿意做作业，不愿意去上学；有的孩子害怕考试，考试前吃不下饭，睡不好觉，甚至每次到考试前就生病；还有的孩子跟父母的关系紧张，不愿意回家，也不愿意和父母说学校的事。", "Because of the great pressure, some children are unwilling to do homework or go to school; some children are afraid of exams, can’t eat before exams, can’t sleep well and even get sick every time exams approach; and some children are tense with their parents, unwilling to go home and unwilling to tell their parents about school."),
      ("家长们对孩子的要求都很高，觉得这样对孩子有好处。但真正为孩子好，就应该给他们一个轻松快乐的家庭环境，这样才能让他们的身心健康发展。", "Parents all have high demands on their children and feel that this is good for them. But to really do good for children, one should give them a relaxed and happy family environment, so that their bodies and minds can develop healthily.")]
C5A = [("作业太多，考试太多，课外还要上补习班、兴趣班，每个学生都有升学考试的压力。", "Activity 5-1 (my answer): What reasons are given for student stress? Too much homework and too many exams, tutoring and interest classes outside school, and the pressure of entrance exams for every student."),
       ("不愿意做作业，不愿意去上学；害怕考试，吃不下饭，睡不好觉，生病；和父母关系紧张。", "5-2 (my answer): What are the symptoms? Unwillingness to do homework or go to school; fear of exams, loss of appetite, poor sleep, illness; tense relations with parents."),
      ("应该给孩子一个轻松快乐的家庭环境，让他们的身心健康发展。", "5-3 (my answer): What should parents do? Give their children a relaxed and happy family environment so their bodies and minds develop healthily.")]
ZA = [("天气再不好，我也要去跑步。", "再…也… (usually used hypothetically, indicating determination: “even if” or “no matter how”; Subj. 1 + 再 + extreme situation, subj. 2 + 也 + what will happen), 1: However bad the weather is, I will go running. (translations mine)"), ("父母再辛苦，也要让孩子过上好的生活。", "2: However hard it is for the parents, they want their children to have a good life."), ("为了孩子的教育，再多的钱他们也愿意花。", "3: For their children’s education they are willing to spend however much money it takes."), ("你再哭我也不会让你去。", "4: However much you cry, I won’t let you go.")]
ZB = [("有了百度地图，不管上哪儿你都不会迷路。", "再…也… vs. 不管…都… (不管 is usually followed with a question word, noun phrases for choices, or affirmative-negative phrases), 1: With Baidu Maps, wherever you go you won’t get lost."), ("不管多辛苦，父母都会想办法送孩子出国。", "2: However hard it is, parents will find a way to send their children abroad."), ("不管是补习班还是兴趣班，学费都很贵。", "3: Whether tutoring classes or interest classes, the tuition is very expensive."), ("不管喜不喜欢，你都得去上课。", "4: Whether you like it or not, you have to go to class."),
      ("再辛苦，父母也会送孩子出国。", "Example 2 is interchangeable with 再…也…: 不管多辛苦，父母都会想办法送孩子出国 = 再辛苦，父母也会送孩子出国。"), ("再不喜欢，你也得去上课。", "Example 4 can be modified as 再…也…, but the meaning differs slightly: 不管喜不喜欢，你都得去上课 means “Whether you like it or not, you have to go to class”; 再不喜欢，你也得去上课 means “No matter how much you dislike it, you have to go to class.”")]
Z1 = [("再忙，我也要回家看父母。", "Activity 1A, 1 (my 再…也 version; the book asks to translate and change the sentences): However busy I am, I will go home to see my parents."), ("再累，他也要自己照顾小孩。", "2: However tired he is, he will look after the child himself."), ("孩子再不听话，你也不应该打他们。", "3: However disobedient the children are, you should not hit them."),
      ("你给我再多的钱，我也不会接受这个工作。", "4: However much money you give me, I won’t accept this job."), ("再苦也不能苦孩子，再穷也不能穷教育。", "5: However hard it is, one must not make children suffer; however poor one is, one must not skimp on education.")]
Z2 = [("中文再难，我也要学好。", "Activity 1B, 1 (my completion): However hard Chinese is, I will learn it well."), ("衣服再贵，她也要买。", "2: However expensive the clothes are, she will buy them."), ("你再说什么，我也不会改变主意。", "3: Whatever else you say, I won’t change my mind."), ("花再多的钱，他们也愿意。", "4: However much money it costs, they are willing."),
      ("时间再晚，我也要把作业做完。", "5: However late it is, I will finish my homework."), ("他说得再好听，我也不会相信。", "6: However nicely he talks, I won’t believe it.")]
L2 = lesson(
    "Lesson 29 Presentation 2 activities and grammar: what a family spends, student stress, and 再…也…",
    "教育费 · 学习压力 · 轻松快乐的家庭环境 · 再…也… · 不管…都… · 再多的钱也愿意花",
    requires=[],
    cards=[
        card("Activity 4 (Reading) and Activity 5 (Reading)",
             "Activity 4: Pair up. Take turns completing a sight translation (reading the passage silently and translating it aloud into English) of the passage, sentence by sentence. Activity 5: Pair up. Read the passage and discuss the following questions. 1. What reasons are given in the passage for student stress? 2. What are the symptoms of the stress? 3. What should parents do for their children? The passages and my answers:",
             examples=[D(z, e) for z, e in C4] + [D(z, e) for z, e in C5 + C5A]),
        card("再…也…, and 再…也… vs. 不管…都…",
             "The structure 再…也… is usually used in a sentence hypothetically, indicating determination, meaning “even if” or “no matter how (much).” When subject 1 and subject 2 are the same, one can be omitted. In the 不管…都… structure, 不管 is usually followed with a question word, noun phrases for choices, or affirmative-negative phrases. Activity 1: A. Pair up. Verbally translate the following sentences into English, then change each into the 再…也 structure without changing its meaning: 1. 不管多忙，我都要回家看父母。 2. 不管多累，他都要自己照顾小孩。 3. 不管孩子听不听话，你都不应该打他们。 4. 不管你给我多少钱，我都不会接受这个工作。 5. 不管多么苦，都不能苦孩子；不管多么穷，都不能穷教育。 B. Complete the sentences using 再…也… (the beginnings: 1. 中文再难, 2. 衣服再贵, 3. 你再说什么, 4. 花再多的钱, 5. …，我也要把作业做完。 6. …，我也不会相信。) C. Have you ever decided to do something despite unfavorable conditions? Share your experiences with your class. The examples and my versions:",
             examples=[D(z, e) for z, e in ZA + ZB + Z1 + Z2]),
    ],
    exercises=[
        M("What does 再…也… indicate?", "Determination, “even if” or “no matter how”", ["A past event", "A request", "A question"], "indicating determination."),
        M("What does 天气再不好，我也要去跑步 mean?", "However bad the weather, I’ll go running", ["The weather is good", "I never run", "I ran yesterday"], "天气再不好，我也要去跑步."),
        M("What does 不管…都… usually follow with?", "A question word, noun phrases for choices, or affirmative-negative phrases", ["Only numbers", "Only names", "Only verbs of motion"], "不管 is usually followed with a question word …."),
        M("Which sentence is interchangeable with 不管多辛苦，父母都会想办法送孩子出国?", "再辛苦，父母也会送孩子出国", ["父母不辛苦", "不管喜不喜欢", "再不喜欢"], "Example 2 is interchangeable."),
        M("How does 再不喜欢，你也得去上课 differ from 不管喜不喜欢，你都得去上课?", "“No matter how much you dislike it” rather than “whether you like it or not”", ["It is a question", "It means you can stay home", "There is no difference at all"], "the meanings differ slightly."),
        M("According to Activity 5, what share of students feel too much pressure after third grade?", "More than 70 percent", ["About 7 percent", "About half", "Nobody"], "百分之七十以上."),
        M("What do some children do before exams, according to the passage?", "Can’t eat or sleep well, even get sick", ["Play games", "Travel", "Sing"], "考试前吃不下饭，睡不好觉."),
        M("How much does a child’s education cost at least if sent abroad?", "About two million yuan", ["Two thousand yuan", "Twenty yuan", "Two hundred yuan"], "最少也会达到两百万人民币."),
        F("天气再不好，我___要去跑步。", "也", ["都", "就", "还"], "再…也…."),
        F("不___多辛苦，父母都会想办法送孩子出国。", "管", ["怕", "是", "说"], "不管…都…."),
        F("为了孩子的教育，再多的钱他们也愿___花。", "意", ["想", "要", "看"], "愿意: be willing."),
    ],
)

# ------------------------------------------------------------------ 3. 好 purpose and 在...的同时
HE = [("一些家庭还会买很贵的学区房，好让孩子上更好的学校。", "好 indicating purpose (“in order to” or “for the sake of”; Action, 好 + Purpose), 1: Some families also buy very expensive school-district homes so that their children can go to better schools. (translations mine)"), ("她睡前常喝一杯牛奶，好入睡。", "2: She often drinks a glass of milk before bed to fall asleep."), ("老师，请说慢点儿，我们好做笔记。", "3: Teacher, please speak a bit slower so that we can take notes."), ("请把车停到里面，好让别人走路。", "4: Please park the car inside so that others can walk."),
      ("为了让大家听清楚，老师又讲了一遍。", "为了 is also used for expressing purpose (为了 + verb phrase): To let everyone hear clearly, the teacher explained once more."), ("为了孩子的前途，他每天努力工作。", "(为了 + noun phrase): For his child’s future, he works hard every day.")]
HT = table(["", "Pattern"], [["为了", "为了 + Purpose (noun phr./verb phr.), Subj. + action"], ["好", "Action, 好 + Purpose (verb phr.)"]], title="为了 and 好 compared")
H2 = [("为了家人，他每天努力工作。", "Activity 2B, the book’s example (translations mine): For his family, he works hard every day."), ("他每天努力工作，好让家人有更好的生活。", "→ He works hard every day so that his family can have a better life."),
      ("他离开老家到大城市工作，好挣钱。", "2B-1 (my 好 version): He left his hometown to work in a big city in order to earn money."), ("爸爸每天辛辛苦苦地工作，好让家人过上好生活。", "2B-2: Dad works hard every day so that the family can live well."), ("他们在这个学区租了很贵的房子，好让孩子能上更好的学校。", "2B-3: They rented an expensive home in this school district so that the child can go to a better school."),
      ("爸爸把房子卖了，好给奶奶治病。", "2B-4: Dad sold the house so as to pay for Grandma’s treatment."), ("他每天都坚持锻炼，好让身体更健康。", "2B-5: He keeps exercising every day so as to be healthier.")]
TS = [("我们在重视教育的同时，也要关心孩子的身心健康。", "在…的同时 (the formal use of 同时, often reminding or urging, so the second clause often contains a modal like 要, 应该, 不能; (Subj.) + 在…的同时, (Subj.) + 也 + verb phrase), 1: While valuing education, we should also care about children’s physical and mental health. (translations mine)"), ("在发展经济的同时，我们也应该注意保护环境。", "2: While developing the economy, we should also pay attention to protecting the environment."), ("在努力工作的同时，也不能忘了锻炼身体。", "3: While working hard, one also must not forget to exercise.")]
T3A = [("为自己考虑，同时也应该为别人想想。", "Activity 3A, 1 (my casual 同时 version): Think of yourself, and at the same time also think of others."), ("学好汉语，同时也要了解中国的文化。", "2: Learn Chinese well, and at the same time also understand Chinese culture."), ("发展经济，同时我们也应该注意保护环境。", "3: Develop the economy, and at the same time we should also pay attention to protecting the environment.")]
T3B = [("在高科技给人们带来很多方便的同时，也带来一些不好的影响。", "Activity 3B, 1 (my formal version): While high tech brings people much convenience, it also brings some bad influences."), ("父母们在培养自己孩子的同时，也在为国家培养人才。", "2: While parents bring up their own children, they are also cultivating talent for the country."), ("我们在注重孩子学习的同时，也要注意培养他们独立生活的能力。", "3: While we attach importance to children’s studies, we should also pay attention to cultivating their ability to live independently.")]
T3C = [("在工作的同时，也不能忘了家人。", "Activity 3C, 1 工作和家人 (my sentence): While working, one must not forget one’s family."), ("在赚钱的同时，也要注意健康。", "2 钱和健康: While making money, one should also pay attention to health."), ("在关心孩子快乐的同时，也要想想他们的前途。", "3 孩子的快乐和前途: While caring about children’s happiness, one should also think about their future."), ("在爱孩子的同时，也要尊重孩子。", "4 爱孩子和尊重孩子: While loving children, one should also respect them. (items 5 to 7 of the book’s list are blanks for the learner)")]
L3 = lesson(
    "Lesson 29 Presentation 2 grammar: 好 indicating purpose and 在…的同时",
    "好让孩子上更好的学校 · 好入睡 · 我们好做笔记 · 为了 vs 好 · 在重视教育的同时 · 在发展经济的同时",
    requires=[],
    cards=[
        card("好 indicating purpose",
             "好 can mean “in order to” or “for the sake of,” and expresses a purpose (Action, 好 + Purpose). 为了 is also used for expressing purpose. Activity 2: A. Listen to the sentences and translate them into English (five audio items, which are not included). B. Change the following 为了 sentences into “好 + purpose” sentences. Make any necessary changes: 1. 为了挣钱，他离开老家到大城市工作。 2. 为了家人的生活，爸爸每天辛辛苦苦地工作。 3. 为了孩子能上更好的学校，他们在这个学区租了很贵的房子。 4. 为了给奶奶治病，爸爸把房子卖了。 5. 为了让身体更健康，他每天都坚持锻炼。 C. Pair up. Talk with your partner about your own experience of effort you made for a specific reason, using the “好 + purpose” structure. The examples and my versions:",
             tables=[HT], examples=[D(z, e) for z, e in HE + H2]),
        card("在…的同时",
             "在…的同时 is the formal use of 同时, and often has the meaning of reminding or urging, so the second clause often contains a modal auxiliary, like 要, 应该, 不能, etc. Activity 3: A. Verbally change the following formal 在…同时 sentences into casual 同时 sentences: 1. 在为自己考虑的同时，也应该为别人想想。 2. 在学好汉语的同时，也要了解中国的文化。 3. 在发展经济的同时，我们也应该注意保护环境。 B. Rewrite the following casual 同时 sentences into formal 在…同时 sentences: 1. 高科技给人们带来很多方便，同时也带来一些不好的影响。 2. 父母们在培养自己孩子，同时也在为国家培养人才。 3. 我们要注重孩子学习，同时也要注意培养他们独立生活的能力。 C. Pair up. Think about the relation between two issues in the following list and state your opinion using the “在…同时” structure: 1. 工作和家人 2. 钱和健康 3. 孩子的快乐和前途 4. 爱孩子和尊重孩子 5. 爱好和＿＿ 6. 完成自己的工作和＿＿ 7. ＿＿和＿＿. The examples and my versions:",
             examples=[D(z, e) for z, e in TS + T3A + T3B + T3C]),
    ],
    exercises=[
        M("What does 好 express in 买学区房，好让孩子上更好的学校?", "Purpose, “in order to”", ["A reason in the past", "A condition", "A comparison"], "好 can mean in order to or for the sake of."),
        M("What does 老师，请说慢点儿，我们好做笔记 mean?", "Speak slower so that we can take notes", ["We took notes yesterday", "We don’t want notes", "Please speak faster"], "我们好做笔记."),
        M("Which structure is used with a noun phrase for purpose?", "为了", ["好", "同时", "也"], "为了 + noun phrase."),
        M("Which can be followed only by a verb phrase for purpose?", "好", ["为了", "因为", "虽然"], "Action, 好 + Purpose (verb phr.)."),
        M("What is 在…的同时 compared with 同时?", "The formal use", ["The casual use", "A question form", "A past form"], "the formal use of 同时."),
        M("What kind of verb often appears in the second clause of 在…的同时?", "A modal like 要, 应该 or 不能", ["A past verb", "A color word", "A name"], "the second clause often contains a modal auxiliary."),
        M("What does 在发展经济的同时，我们也应该注意保护环境 mean?", "While developing the economy we should also protect the environment", ["We should stop the economy", "The environment is ruined", "We should travel"], "在发展经济的同时."),
        F("她睡前常喝一杯牛奶，好入___。", "睡", ["吃", "看", "走"], "入睡: fall asleep."),
        F("我们在重视教育的同___，也要关心孩子的身心健康。", "时", ["天", "月", "年"], "同时: at the same time."),
        F("为了孩子的前途，他每天努力工___。", "作", ["学", "习", "话"], "工作: work."),
    ],
)

# ------------------------------------------------------------------ 4. 用在...上
YE = [("每个家庭百分之三十的钱都会用在孩子身上。", "用在…上 (Spend … on a certain person/thing/aspect/area; (把) + Obj. 1 + 用在/花在 + Obj. 2/Action 上; when Object 2 is a living entity it usually appears in the form of 身上), 1: Thirty percent of each family’s money is spent on the children. (translations mine)"), ("年轻人要把时间多用在学习和工作上。", "2: Young people should spend more of their time on study and work."), ("人们常常把钱花在并不需要的东西上。", "3: People often spend money on things they don’t need."),
      ("您把钱都用在给我买书上，而不愿把钱用在您自己买衣服上。", "4: You spend all your money on buying me books and are unwilling to spend money on buying clothes for yourself."), ("我把一半的钱都花在他们身上了。", "5: I have spent half of my money on them.")]
Y4 = [("我不是什么天才，我只是把别人喝咖啡的时间都用在工作上了。", "Activity 4B, 1 (translations mine): I’m no genius; I just spent all the time other people spend drinking coffee on work."), ("我们不应该让学生把全部时间都用在学习上，而要给学生留下许多自由的时间，他才能顺利地学习。", "2: We should not make students spend all their time on studying, but leave them a lot of free time, so that they can study smoothly."),
      ("花在教育上的钱一定不会白花。", "3: Money spent on education is certainly not wasted."), ("把时间用在阅读上吧，这样你就可以轻松地得到别的人很辛苦才能得到的东西。", "4: Spend your time on reading; that way you can easily get what other people have to work very hard to get."),
      ("中国父母最可爱也是最可怜的地方，就是他们把所有的心血都花在子女身上。", "5: What is most lovable and also most pitiable about Chinese parents is that they pour all their heart’s blood into their children."), ("好钢用在刀刃上。", "6: Good steel is used on the blade’s edge (spend your best resources where they matter most).")]
L4 = lesson(
    "Lesson 29 Presentation 2 grammar: 用在…上 (spend … on …)",
    "用在孩子身上 · 花在教育上 · 把时间用在阅读上 · 好钢用在刀刃上",
    requires=[],
    cards=[
        card("用在…上 (Spend… on certain person/thing/aspect/area)",
             "The structure is (把) + Obj. 1 + 用在/花在 + Obj. 2/Action 上. When Object 2 in the structure is a living entity, it usually appears in the form of 身上. Activity 4: A. Listen to the following sentences and translate them into English (five audio items, which are not included). Pair up and compare your work with that of your partner. B. Read the following sentences and translate them into English. Guess the meaning of any unknown words. C. Pair up. Describe how you and your roommate, or you and your family members, spend your time and money. The examples and my translations:",
             examples=[D(z, e) for z, e in YE + Y4]),
    ],
    exercises=[
        M("What does 用在…上 mean?", "Spend … on a certain person, thing or aspect", ["Use … instead of …", "Wait for …", "Run to …"], "Spend … on."),
        M("What form does Object 2 take when it is a living entity?", "…身上", ["…上面", "…里面", "…后面"], "it usually appears in the form of 身上."),
        M("What does 每个家庭百分之三十的钱都会用在孩子身上 mean?", "Thirty percent of each family’s money is spent on the children", ["Children spend thirty percent", "Families have thirty children", "Thirty families spend money"], "用在孩子身上."),
        M("What does 花在教育上的钱一定不会白花 mean?", "Money spent on education is certainly not wasted", ["Education is free", "Money is wasted on education", "Education is cheap"], "花在教育上的钱一定不会白花."),
        M("What does 好钢用在刀刃上 suggest?", "Spend your best resources where they matter most", ["Steel is expensive", "Knives are dangerous", "Never use steel"], "好钢用在刀刃上."),
        M("Which sentence uses 用在…上?", "把时间用在阅读上吧", ["我喜欢阅读", "他在看书", "时间过得很快"], "把时间用在阅读上吧."),
        F("年轻人要把时间多用在学习和工作___。", "上", ["下", "里", "外"], "用在…上."),
        F("我把一半的钱都花在他们身___了。", "上", ["下", "里", "外"], "身上."),
        F("我只是把别人喝咖啡的时间都用在工作上___。", "了", PART, "了: completed."),
    ],
)

UNIT = unit("第二十九课 中国的教育 Presentation 2: 重视教育的传统, 再…也…, 好, 在…的同时, 用在…上", [L1, L2, L3, L4])
