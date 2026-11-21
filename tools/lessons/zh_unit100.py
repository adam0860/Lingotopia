"""Unit 100: Lesson 29 (Education in China), Presentation 3, Using Chinese in Context Activities 2-6 (a young teacher's question and three answers, a city school teacher, the Shanghai zhongkao story).
Audio, video and pictures are not included; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('校长', 1, 'zhang3'), ('不好教', 2, 'jiao1'), ('好好教', 2, 'jiao1'), ('教书', 0, 'jiao1'), ('来教几个月', 1, 'jiao1')):
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

# ------------------------------------------------------------------ 1. using chinese act 2
QT = ("我当老师已经几年了，最近我想去一所流动儿童学校教书，我一直都很想帮助那些孩子。但是我也知道这样的学校工资都比较低。我也到了结婚的年龄，应该存一点钱了。你们觉得我应该去吗？",
      "Activity 2A: I have been a teacher for several years. Recently I want to go teach at a migrant children’s school; I have always very much wanted to help those children. But I also know that the pay at such schools is quite low. I have also reached marrying age and should save a little money. Do you think I should go? (translation mine)")
R1 = ("我就是从流动儿童学校毕业的。说真的，学校的条件太差了，学生对学习的要求也不高。但是那里的校长和老师都很好，我自己到现在都很感谢我的语文老师，是她给我的生活打开了一个窗口。我们班有很多同学的家庭环境都很差，但我觉得你应该去完成自己的理想。而且，有很多孩子需要像你这样有爱心的老师。",
      "Activity 2B, 1: I graduated from a migrant children’s school myself. Honestly, the school’s conditions were very poor, and the students’ demands on their studies were not high either. But the principal and teachers there were all very good; I still thank my Chinese teacher to this day, for it was she who opened a window onto life for me. Many of my classmates had very poor family backgrounds, but I think you should go and fulfil your own ideal. Besides, many children need a teacher with a loving heart like you. (translation mine)")
R2 = ("我就在这样一所学校当校工。有人愿意为农民工的孩子做点儿事我很高兴，但是我想告诉你，这里的厕所很脏，教师宿舍非常小，只有十平米左右。班主任的工资每个月只有四千多元，一般老师就更低了。相比起来，一般学校的老师平均每年有十万元的工资。这样的待遇根本不可能留住好老师，很多老师来教几个月就走了。所以你要好好想一想再做决定。",
      "2: I work as a school custodian at such a school. I’m glad someone is willing to do something for migrant workers’ children, but I want to tell you that the toilets here are very dirty, the teachers’ dormitories are very small, only about ten square meters. A homeroom teacher’s pay is only a little over 4,000 yuan a month, and ordinary teachers earn even less. By comparison, teachers at ordinary schools average 100,000 yuan a year. Such treatment simply cannot keep good teachers; many teachers leave after teaching a few months. So think it over carefully before deciding. (the book writes 4000 and 10 万 in digits; translation mine)")
R3 = ("农民工辛辛苦苦地工作，就是想要孩子以后能过得比自己好。我看到一所学校的大门上写着“让打工者的孩子不再打工”，可是农民工子弟学校的教学质量这么差，他们的孩子怎么可能有好的前途？那些孩子学习都不太努力，反正中学一毕业就要跟父母一样去打工。那些孩子不好教，而且老师的工资也确实不高，所以只能是尊重你自己的选择。但说真的，我真的希望有人能好好教那些孩子，给他们希望。",
      "3: Migrant workers work hard precisely because they want their children to live better than themselves. I saw on the gate of a school the words “Let the children of workers no longer be workers,” but the teaching quality at migrant workers’ children’s schools is so poor; how could their children have a good future? Those children don’t study very hard anyway, since as soon as middle school ends they will go to work like their parents. Those children are not easy to teach, and teachers’ pay really is not high, so I can only respect your own choice. But honestly, I really hope someone will teach those children well and give them hope. (translation mine)")
RA = [("支持：他可以帮助很需要老师的孩子，完成自己的理想。反对：工资太低，条件很差，他也应该存钱结婚。", "Activity 2A (my notes; the book leaves lines for Are you for or against and Your reasons): For: he can help children who greatly need teachers and fulfil his own ideal. Against: the pay is too low, conditions are poor, and he should also save money for marriage."),
      ("第一个人最支持，第三个人比较犹豫，第二个人最不支持。", "Activity 2C-1 (my order of strength of support, strongest first; the book gives none): the first writer supports most, the third is hesitant, and the second supports least.")]
L4 = lesson(
    "Lesson 29 Presentation 3 using Chinese in context: should a young teacher go to a migrant children’s school?",
    "流动儿童学校 · 工资比较低 · 校工 · 十平米 · 待遇 · 留住好老师 · 让打工者的孩子不再打工",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 2 (Reading, Listening, and Speaking)",
             "A. Read the question a young teacher posted online. In groups of three, discuss how you would answer his question. List the reasons you support or oppose his idea using your understanding of the migrant children’s school. Are you for or against his idea? Your reasons: B. Each member offers answers and lists the reasons why they are for or against his proposal. (The three answers follow; the book gives For/Against Reasons tables for each.) C. Tell your partners about your passage. As a group you will: 1. List the three answers in order of how strongly they support his idea. 2. What are the main reasons for supporting his idea? 3. What are the main reasons for arguing against his idea? 4. Why do you support or argue against his idea? (The three small photos are not included.) The question, the three answers and my notes:",
             examples=[D(*QT), D(*R1), D(*R2), D(*R3)] + [D(z, e) for z, e in RA]),
    ],
    exercises=[
        M("What does the young teacher want to do?", "Teach at a migrant children’s school", ["Study abroad", "Quit teaching", "Open a company"], "我想去一所流动儿童学校教书."),
        M("What worry does he have?", "The pay is low and he should save money", ["He dislikes children", "He can’t drive", "The school is new"], "这样的学校工资都比较低……应该存一点钱了."),
        M("What does the first writer advise?", "Go and fulfil his ideal", ["Never go", "Wait for ten years", "Teach math only"], "你应该去完成自己的理想."),
        M("What does the school custodian describe?", "Dirty toilets and tiny dormitories", ["Great facilities", "A rich school", "A large library"], "厕所很脏，教师宿舍非常小."),
        M("What do homeroom teachers earn there per month?", "A little over four thousand yuan", ["Over forty thousand yuan", "Over four hundred yuan", "Nothing"], "只有四千多元."),
        M("What does the custodian say ordinary school teachers average a year?", "A hundred thousand yuan", ["Ten thousand yuan", "A million yuan", "Nothing"], "平均每年有十万元的工资."),
        M("What did the third writer see on a school gate?", "“Let the children of workers no longer be workers”", ["“Welcome to our school”", "“No entry”", "“Learning is joy”"], "让打工者的孩子不再打工."),
        M("What does the third writer finally say?", "Respect your own choice, but I hope someone teaches those children well", ["Never go", "Go at once", "Marry first"], "只能是尊重你自己的选择……希望有人能好好教那些孩子."),
        F("我就是从流动儿童学校毕___的。", "业", ["学", "习", "校"], "毕业: graduate."),
        F("这样的待遇根本不可能留___好老师。", "住", ["下", "着", "有"], "留住: retain."),
        F("但是我也知道这样的学校工___都比较低。", "资", ["作", "钱", "人"], "工资: salary."),
    ],
)

# ------------------------------------------------------------------ 2. using chinese acts 3-6
CT = ("我们学校以前全是城里的学生，后来到这里打工的人越来越多，我们就开始收一些农民工的孩子。一是想帮助这些孩子，二是可以增加学校的收入。但是问题来了，那些从农村来的学生，他们的学习比城市学生要差得多。如果一个班的农村学生超过百分之三十，老师上课就很困难了，一个班的教学质量都会下降。有些城市家长对学校很不满意，就会让自己孩子转到别的学校去。所以，城市学生渐渐离开，现在，我们学校全是农民工的孩子了。",
      "Activity 3B, “Words of a city school teacher”: Our school used to be all city students; later more and more people came here to work, and we started to admit some migrant workers’ children. One reason was to help these children; another was to increase the school’s income. But then problems came: the students from the countryside are much weaker in their studies than the city students. If more than 30 percent of a class are rural students, teaching becomes very difficult, and the teaching quality of the whole class goes down. Some city parents are very dissatisfied with the school and move their children to other schools. So the city students gradually left, and now our school is all migrant workers’ children. (the book writes 30% in digits; translation mine)")
SH = ("在所有的大城市中，上海是对农民工比较友好的，住在市区的农民工子女大多可以进入公办学校。但是，当一所公办学校开始接受农民工子女的时候，原有的城市学生常常会离开这所学校，最后，这些学校有百分之八十到九十的学生都是农民工子女。在沪城中学，每个年级有五个班，其中一个班全部是农民工子女。在初中一二年级的时候，这个班的平均成绩一直是全年级的第二三名，也就是说，这些流动儿童的学习成绩超过了一半或一半以上的城市学生。但是到了初中三年级，这个班的平均成绩变成了全年级的最后一名。主要的原因是，农民工子女不能在上海参加中考，就是初中升高中的考试。到了初中的最后一年，他们只好回到农村老家上学。如果继续留在上海，初中毕业以后只能上职业中学。而且，职业中学虽然有很多专业，但只有三个专业让农民工子女选择：厨师、酒店服务、技工。也就是说，从职业中学毕业以后，这些孩子只能跟父母一样，在饭店、旅馆、工厂做一些低收入的工作。看不到希望的学生们也就失去了学习的兴趣和动力。",
      "Activity 4D (adapted from a news article; the source site is left out): Among all the big cities, Shanghai is relatively friendly to migrant workers, and migrant workers’ children living in the urban area can mostly enter public schools. But when a public school starts to admit migrant children, the original city students often leave, and in the end these schools have 80 to 90 percent migrant children. At Hucheng Middle School each grade has five classes, one of which is entirely migrant children. In the first and second years of junior high, this class’s average score was always second or third in the grade; that is, these migrant children’s grades surpassed half or more than half of the city students. But in the third year of junior high, the class’s average score became last in the grade. The main reason is that migrant children cannot take the zhongkao, the high-school entrance exam, in Shanghai. In the last year of junior high they have no choice but to go back to their rural hometowns to study. If they stay in Shanghai, after junior high they can only go to vocational schools. Moreover, although vocational schools have many majors, only three are open to migrant children: cook, hotel service, and skilled worker. That is, after graduating from vocational school these children can only, like their parents, do low-income jobs in restaurants, hotels and factories. Students who can’t see hope also lose their interest and drive in studying. (the book writes 80-90% in digits; translation mine)")
CTA = [("城市学生离开农民工子女多的学校，老师上课困难，学校的教学质量下降。", "Activity 3 (my notes for the benefits and drawbacks; the book gives empty lines): Drawback: when migrant children are many, city students leave, teaching becomes difficult and quality goes down."),
       ("农民工子女不能在上海参加中考，最后一年只好回农村老家上学；留下来只能上职业中学，选择很少，没有希望，失去了学习的兴趣和动力。", "Activity 4D (my answer for the reason; the book gives none): Migrant children cannot take the zhongkao in Shanghai, so in the last year they must return to their rural hometowns; if they stay they can only go to vocational schools with few choices, which leaves them hopeless and without interest or drive.")]
UC = table(["Activity", "Task (the answers to these are audio, video or discussion; the book gives no key)"], [
    ["Activity 3 (Speaking, Listening, and Reading)", "A. Do you think it’s better to have the children of migrant workers and children from the city attend the same schools, or should they be separated? In groups of three, discuss the possible benefits and drawbacks. B. Read the following passage and add the information to your notes above."],
    ["Activity 4 (Reading and Speaking)", "A. In groups of three, discuss, in Chinese, the possible reasons for the low performance of the students in 农民工子弟学校. B. Each member listens to one of the three online chats about this problem and writes the main ideas that they hear (audio). C. Tell your partners about what you hear. Discuss what you agree with and do not agree with. D. Read the following passage to learn additional reasons for the low performance of the migrant students and discuss the reasons why the city has a restrictive policy towards them."],
    ["Activity 5 (Speaking)", "Pair up and discuss the following questions with your partner. 1. What difficulties do children experience if they don’t live with any parents? 2. Share your opinions of these situations with the class."],
    ["Activity 6 (Speaking)", "A. Watch a video about 留守儿童 and think about the following questions. 1. What were peasants’ lives like in China before modern times? 2. How did they change later? 3. How did the 留守儿童 emerge? 4. What is life currently like for Tang Yuwen? 5. What did he do when his parents came back? 6. What’s his biggest wish now? 7. What does he want to do when he grows up? B. In groups of three, share what you think about 留守儿童’s situation and the impact their situation will have on their growth. (The video is not included.)"]],
    title="Using Chinese in Context, Activities 3 to 6")
L5 = lesson(
    "Lesson 29 Presentation 3 using Chinese in context: city schools and migrant children, and the Shanghai zhongkao",
    "农民工子弟学校 · 城市学生渐渐离开 · 上海 · 公办学校 · 中考 · 职业中学 · 失去学习的兴趣和动力",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activities 3 to 6", "The tasks of Activities 3 to 6 and the two reading passages with my notes:", tables=[UC], examples=[D(*CT), D(*SH)] + [D(z, e) for z, e in CTA]),
    ],
    exercises=[
        M("Why did the city school start to admit migrant workers’ children?", "To help them and to increase the school’s income", ["Because they were rich", "Because the city had no students", "Because of a law about uniforms"], "一是想帮助这些孩子，二是可以增加学校的收入."),
        M("What happens when more than thirty percent of a class are rural students, per the teacher?", "Teaching becomes difficult and quality falls", ["Everyone improves", "The class gets a new teacher", "Nothing"], "老师上课就很困难了，一个班的教学质量都会下降."),
        M("What did some city parents do?", "Moved their children to other schools", ["Taught the class", "Gave money", "Moved to the countryside"], "让自己孩子转到别的学校去."),
        M("Which city is called relatively friendly to migrant workers?", "Shanghai", ["Beijing", "Chongqing", "Shenzhen"], "上海是对农民工比较友好的."),
        M("What share of students in such schools can become migrant children, per the passage?", "80 to 90 percent", ["8 to 9 percent", "Half", "None"], "百分之八十到九十."),
        M("What happened to the migrant class’s average rank by the third year of junior high?", "It fell to last place in the grade", ["It rose to first", "It stayed second", "It vanished"], "变成了全年级的最后一名."),
        M("Why can migrant children not stay on in Shanghai for high school?", "They cannot take the zhongkao in Shanghai", ["They are too tall", "They dislike Shanghai", "Schools are closed"], "农民工子女不能在上海参加中考."),
        M("What choices of major do migrant children have at the vocational school?", "Cook, hotel service, skilled worker", ["Doctor, lawyer, teacher", "Pilot, actor, singer", "Any major"], "厨师、酒店服务、技工."),
        F("但是问题来了，那些从农村来的学生，他们的学习比城市学生要差得___。", "多", ["少", "大", "好"], "差得多: much worse."),
        F("上海是对农民工比较友___的。", "好", ["善", "爱", "对"], "友好: friendly."),
        F("看不到希望的学生们也就失去了学习的兴趣和动___。", "力", ["作", "量", "机"], "动力: drive."),
    ],
)

UNIT = unit("第二十九课 中国的教育 Presentation 3: 语境中的汉语 (2)", [L4, L5])
