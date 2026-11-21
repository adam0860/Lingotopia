"""Unit 94: Lesson 29 (Education in China), the unit overview and learning objectives, Presentation 1 (an interview at the Children's Palace) with Activities 1-3,
and the grammar section on the concessive use of 当然.
Audio and pictures are not included; the traditional-character copy of the presentation is not repeated; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('少年宫', 0, 'shao4'), ('长大', 0, 'zhang3'), ('觉得自己', 1, 'de5')):
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

# ------------------------------------------------------------------ 1. overview, getting started, presentation 1, activities 1-3
OV = table(["Item", "Lesson 29 (as laid out in the unit overview)"],
           [["Lesson topic", "Education in China"],
            ["Task/Function", "Discuss the rapid growth of interest-oriented classes in China. Discuss the value of children’s education in China: its traditions, family investment, and related negative issues. Describe the difficulties regarding the education of children left behind in rural areas, and migrant children."],
            ["Grammar", "New words and phrases in the Core Vocabulary; use 当然 as a concession word; use 吧 to express indefinite tone; use directional complements 下去 and 下来 to express the continuation of an action; complements: verb+得+过来, 上不起, 比不上; the 用在…上 structure; the 在…的同时 structure; use 好 to express purpose; 再…也… for determination; the 只好 + verb phrase structure"],
            ["Area Studies", "China’s Education"]],
           title="Overview: Unit 5 Social Factors, Lesson 29 (the PDF mixes the columns of this table; I have separated them)")
LO = ("1. Upon completion of this lesson, you will be able to talk about: the rapid growth of hobby classes in China; the value of children’s education in China: its traditions, family investment, and related negative issues; the difficulties in education faced by children left behind in rural areas, and the village children who migrate to cities.\n\n"
      "2. To perform the above you must master the following: new words and phrases associated with the above functions; using 当然 as a concession conjunction word; using 吧 to express the indefinite tone; using directional complements 下去 and 下来 to express continuation of an action; complement: Verb + 得 + 过来, 上不起, 比不上; the structure 用在…上; the structure 在…的同时; using 好 to express purpose; structure 再…也… for determination; the 只好 + Verb phrase.")
DL = [("记者", "王主任，谢谢您接受我们的采访。现在到少年宫参加兴趣班的孩子有多少？", "Reporter: Director Wang, thank you for accepting our interview. How many children now come to the Children’s Palace to attend interest classes? (Presentation 1; translations mine; the traditional-character copy is not repeated)"),
      ("王主任", "平时周末有五千多人，暑假要更多一些。", "Director Wang: Usually on weekends there are over five thousand, and in the summer holidays there are more. (the book writes 5000 in digits)"),
      ("记者", "这么多啊？", "Reporter: That many?"),
      ("王主任", "我们这儿还是少的呢，有些大城市的少年宫，每个周末都有三四万孩子。", "Director Wang: Here it’s still few; at some big cities’ children’s palaces there are thirty or forty thousand children every weekend."),
      ("记者", "上兴趣班的孩子怎么这么多呢？", "Reporter: Why are there so many children attending interest classes?"),
      ("王主任", "我想主要是人们都有钱了，另外也希望孩子有更多的兴趣和爱好。", "Director Wang: I think mainly it’s that people all have money now, and they also hope their children have more interests and hobbies."),
      ("记者", "我也觉得，现在的父母不像以前，只关心孩子的学习成绩了。", "Reporter: I feel so too; today’s parents are not like before, caring only about their children’s grades."),
      ("王主任", "是啊。培养兴趣对孩子的发展很有好处。而且有了特长，在升学考试的时候还可以加分。", "Director Wang: Yes. Cultivating interests is very good for a child’s development. Besides, with a special skill, one can also get extra points in the entrance exams."),
      ("记者", "你们都有些什么样的兴趣班呢？", "Reporter: What kinds of interest classes do you have?"),
      ("王主任", "各种各样的班都有，像音乐、舞蹈、画画、武术什么的。", "Director Wang: All kinds of classes, such as music, dance, drawing, martial arts and so on."),
      ("记者", "你们怎么收费？", "Reporter: How do you charge?"),
      ("王主任", "我们收费比外面低得多，上一个班一年三千元左右吧。", "Director Wang: Our fees are much lower than outside; one class costs about three thousand yuan a year."),
      ("记者", "听说有些家长喜欢和别人比，会同时给孩子报好几个班。", "Reporter: I hear some parents like to compare with others and sign their children up for quite a few classes at the same time."),
      ("王主任", "一般也就报两三个吧，当然，也有报四、五个的。", "Director Wang: Generally just two or three, though of course some sign up for four or five."),
      ("记者", "这么多，小孩子能学得过来吗？", "Reporter: So many; can a little child manage to learn them all?"),
      ("王主任", "的确，这样的效果不一定好，还是要尊重孩子自己的兴趣。", "Director Wang: True, the effect of this is not necessarily good; we should still respect the child’s own interest."),
      ("记者", "您说得对。孩子有兴趣才能坚持下去。", "Reporter: You’re right. Only if a child is interested can he keep going.")]
A1O = table(["Topic (a-f)", "Order in the presentation (my key)"], [["e. Number of participants", "1"], ["d. Reasons for the booming business of the Youth Center", "2"], ["a. Types of classes offered at the Youth Center", "3"], ["f. Charges", "4"], ["b. A special type of parent", "5"], ["c. Suggestions for taking classes at the Youth Center", "6"]], title="Activity 1A-2: the correct order e, d, a, f, b, c (my key; the speakers for 1A-1 are a reporter and Director Wang of the Children’s Palace)")
A1B = [("平时周末有五千多人，暑假更多。", "Activity 1B-1 (my answer): On weekends there are over five thousand, and more in the summer."),
       ("人们都有钱了，也希望孩子有更多的兴趣和爱好；培养兴趣对孩子的发展有好处，有了特长，升学考试时还可以加分。", "1B-2 (my answer): People have money and also hope their children have more interests; cultivating interests helps development, and with a special skill one can get extra points in the entrance exams."),
       ("各种各样的班都有：音乐、舞蹈、画画、武术什么的。", "1B-3 (my answer): All kinds: music, dance, drawing, martial arts and so on."), ("收费比外面低得多。", "1B-4 (my answer): The fees are much lower than outside."), ("上一个班一年三千元左右。", "1B-5 (my answer): About three thousand yuan a year for one class."),
       ("喜欢和别人比、同时给孩子报好几个班的家长。", "1B-6 (my answer): Parents who like to compare with others and sign their children up for several classes at once."), ("要尊重孩子自己的兴趣，孩子有兴趣才能坚持下去；一般报两三个班就可以了。", "1B-7 (my answer): Respect the child’s own interest, since only with interest can a child keep going; generally two or three classes are enough.")]
A2T = table(["Category", "Words (my sort; the book gives the sixteen words and leaves the table empty)"], [["少年宫的兴趣班: Types of Classes", "音乐，舞蹈，画画，武术"], ["Reasons for Participation", "培养，发展，好处，加分，特长，升学，希望"], ["Issues Worth Attention", "效果，尊重，坚持，家长，各种各样"]], title="Activity 2: sorting the words into three categories (the words: 音乐 加分 效果 武术 尊重 培养 舞蹈 发展 升学 画画 好处 家长 特长 坚持 各种各样 希望)")
P3Q = [("这里有多少少年宫和兴趣班？", "Activity 3A-1 (audio about a Children’s Palace in rural areas; no key): How many children’s palaces and interest classes are there here? (new word: 乡村, xiāngcūn, rural village)"), ("有什么样的兴趣班？", "3A-2: What kinds of interest classes are there?"), ("有多少学生参加兴趣班？", "3A-3: How many students attend interest classes?"), ("收费怎么样？", "3A-4: How are the fees?"), ("家长怎么看少年宫？", "3A-5: How do parents see the Children’s Palace?"), ("家长们为什么这么看？", "3A-6: Why do parents see it this way?"),
       ("孩子参加了什么兴趣班？", "3B-1 (audio of an interview with a parent; no key): What interest class did the child take part in?"), ("家长帮孩子选兴趣班了吗？为什么？", "3B-2: Did the parent help the child choose the class? Why?"), ("孩子上兴趣班以后跟以前有什么不一样了？", "3B-3: How has the child changed since attending the class?")]
PN = ("我从小就非常喜欢钢琴，但是不知道上哪儿去学，城里的兴趣班收费太贵，我们根本没有钱上那里的班。现在我们这儿也有少年宫了，有了音乐班，还有几十台电钢琴。我第一个就报了名。我学了几个月，现在已经会弹好几首歌了。以前，我们总觉得自己比不上城里的孩子。现在，我们也可以跟城里的学生一样弹钢琴了。我一定会坚持学下去。", "I have loved the piano since I was little, but didn’t know where to go to learn; the city’s interest classes charge too much and we simply had no money to attend classes there. Now we also have a children’s palace here, with a music class and dozens of electric pianos. I was the first to sign up. I have studied for a few months and can now already play quite a few songs. Before, we always felt we couldn’t compare with city children. Now we can also play the piano like city students. I will certainly keep on studying. (Activity 3C; translation mine)")
PNQ = [("她为什么以前没有学钢琴？", "Activity 3C (my three questions for my partner): Why didn’t she learn the piano before?"), ("现在她们那儿有什么？", "What do they have there now?"), ("她学了多长时间，已经会什么了？", "How long has she studied and what can she already do?")]
L1 = lesson(
    "Lesson 29 Education in China: overview, objectives and Presentation 1 (the Children’s Palace)",
    "中国的教育 · 少年宫 · 兴趣班 · 培养兴趣 · 加分 · 收费 · 报好几个班 · 学得过来吗",
    requires=[],
    cards=[
        card("第二十九课 中国的教育: Lesson 29 Education in China", "Learning Objectives (the overview of the unit follows in the table):\n\n" + LO, tables=[OV]),
        card("Presentation 1: Getting Started",
             "Pair up. Discuss the following questions with your partner. A. What hobbies did you have as a child? B. Did you acquire these hobbies on your own or with the help of a friend or adult/teacher? C. How long did you take to learn it? D. How do you benefit from these hobbies? E. What role did your parents play in forming your hobbies? (The pictures, of Beijing’s and Shanghai’s children’s palaces, a dance performance and learning an instrument, are not included; the book gives no answers.)"),
        card("Presentation 1: an interview at the Children’s Palace", "A reporter interviews Director Wang about the many children who attend interest classes.", examples=dlg(DL)),
        card("Presentation 1 Activities, Activity 1 (Listening)",
             "A. Global Listening: Listen to Presentation 1 once and answer the questions. 1. Who are the two speakers in the conversation? 2. What topics about the Youth Center were talked about? Order the following issues by letter, according to their discussion in the presentation: a. Types of classes offered at the Youth Center b. A special type of parent c. Suggestions for taking classes at the Youth Center d. Reasons for the booming business of the Youth Center e. Number of participants f. Charges. B. Detailed Listening: Listen to Presentation 1 again and answer the following questions. 1. How many participants are there at the Youth Centers? 2. Why have Youth Centers become so popular? 3. What kind of classes are offered in this Youth Center? 4. What was said about the cost of classes at the Youth Center? 5. How much does an average family spend at the Youth Center? 6. What type of parent is specifically mentioned? 7. What suggestions are made regarding which classes a child should take at the Youth Center? My key and answers:",
             tables=[A1O], examples=[D(z, e) for z, e in A1B]),
        card("Activity 2 (Reading) and Activity 3 (Listening, Reading, and Speaking)",
             "Activity 2: Sort the following words into three categories. Activity 3: A. Listen to the interview about the Children’s Palace in rural areas and answer the questions below. Then compare your work with that of a classmate. B. Listen to the interview with a parent and answer the questions. Pair up and discuss your answers with your partner. C. Pair up and read the following passage, without checking your dictionary. Using the information in the passage, write three questions to ask your partner, in Chinese. My sort, the questions as printed, the passage and my questions:",
             tables=[A2T], examples=[D(z, e) for z, e in P3Q] + [D(*PN)] + [D(z, e) for z, e in PNQ]),
    ],
    exercises=[
        M("How many children attend on a usual weekend at Director Wang’s children’s palace?", "Over five thousand", ["Over fifty", "Over fifty thousand", "Over five hundred thousand"], "平时周末有五千多人."),
        M("How many children go every weekend to some big cities’ palaces?", "Thirty or forty thousand", ["Three or four hundred", "Three or four", "Three or four million"], "每个周末都有三四万孩子."),
        M("What does the director say is the main reason for so many children?", "People have money now and want children to have more interests", ["Classes are free", "Schools closed", "Parents have no time"], "人们都有钱了，另外也希望孩子有更多的兴趣和爱好."),
        M("How can a special skill help in entrance exams?", "It can earn extra points", ["It removes exams", "It lowers fees", "It gives a gift"], "在升学考试的时候还可以加分."),
        M("How do the Children’s Palace fees compare with outside?", "Much lower", ["Much higher", "The same", "Free"], "我们收费比外面低得多."),
        M("About how much is one class per year?", "Three thousand yuan", ["Thirty yuan", "Three yuan", "Three hundred thousand yuan"], "上一个班一年三千元左右."),
        M("Which parents does the reporter say like to compare with others?", "Those who sign up for several classes at once", ["Those who sign up for none", "Those who teach at home", "Those who live far away"], "会同时给孩子报好几个班."),
        M("What does the director say matters most when choosing classes?", "Respect the child’s own interest", ["Choose the most expensive", "Choose what neighbors choose", "Choose the most classes"], "还是要尊重孩子自己的兴趣."),
        M("Why couldn’t the girl in Activity 3C learn the piano before?", "City classes were too expensive", ["She disliked it", "She had no time", "She was too young"], "城里的兴趣班收费太贵."),
        F("现在的父母不像以前，只关心孩子的学习成___了。", "绩", ["字", "话", "校"], "成绩: grades."),
        F("培养兴趣对孩子的发展很有好___。", "处", ["看", "想", "说"], "好处: benefit."),
        F("孩子有兴趣才能坚持下___。", "去", ["来", "上", "到"], "坚持下去: keep going."),
    ],
)

# ------------------------------------------------------------------ 2. grammar: 当然
DR1 = [("买高铁票很方便，你可以在网上或者在手机上预订，当然也可以直接到火车站去买。", "Post-main clause use (a 当然 clause that offers a secondary choice to soften the tone: main clause + 当然 clause), 1: Buying high-speed rail tickets is very convenient; you can book online or on your phone, and of course you can also go straight to the train station to buy. (translations mine)"),
       ("这代年轻人又有知识又有能力，当然，他们也有一些不足的地方，比如生活能力就不太强。", "2: This generation of young people has both knowledge and ability; of course they also have some shortcomings, for example their ability to take care of themselves is not strong."),
       ("家长们通常会给孩子报两三个兴趣班，当然，也有选七八个的。", "3: Parents usually sign their children up for two or three interest classes, though of course some choose seven or eight.")]
DR2 = [("钱当然很重要，但我觉得，生活中还应该有些别的什么。", "Pre-main clause use (the 当然 clause acknowledges the other’s or a common opinion first, then an adversative conjunction 但是/可是/不过 and the main clause), 1: Money is of course important, but I think life should have something else too."),
       ("重视孩子的教育当然是好的，但家长们也应该重视孩子们的身心健康。", "2: Valuing children’s education is of course good, but parents should also value their children’s physical and mental health.")]
DA1 = [("明天的比赛输赢都没有关系，大家努力就行了。当然，能赢最好。", "Activity 1, 1 (translations mine; note the function of 当然, a post-main clause use): Whether we win or lose tomorrow’s match doesn’t matter; it’s enough for everyone to try hard. Of course, winning would be best."),
       ("成熟的男人喜欢聪明的女人，当然，如果同时长得也漂亮，就更好了。", "2 (post-main): Mature men like clever women; of course, if she is also good-looking at the same time, so much the better."),
       ("我们相信美国会做正确的事，当然，是在她试过别的一切可能以后。", "3 (post-main): We believe America will do the right thing, of course after she has tried every other possibility."),
       ("孩子听话当然是好事，但是你也要看他在听话的同时是不是快乐。", "4 (pre-main): A child being obedient is of course a good thing, but you should also see whether he is happy while being obedient."),
       ("一个人说什么当然重要，但更重要的是他做什么，怎么做。", "5 (pre-main): What a person says is of course important, but more important is what he does and how.")]
DA2 = [("我每天都锻炼身体，当然，有时候太忙了就不去。", "Activity 2, picture 1 Exercise (my sentence, post-main): I exercise every day, though of course when I’m too busy sometimes I don’t go."), ("学中文当然很难，但是我觉得很有意思。", "2 Learning Chinese (my sentence, pre-main): Learning Chinese is of course hard, but I find it very interesting."),
       ("参军很辛苦，当然，也可以学到很多东西。", "3 Join military (my sentence, post-main): Joining the military is hard work, though of course one can also learn a lot."), ("快餐当然方便，但是吃得太多对身体不好。", "4 Order fast food (my sentence, pre-main): Fast food is of course convenient, but eating too much is bad for the body."),
       ("自动驾驶汽车当然很先进，但是我还是有点儿担心。", "5 Self-driving car (my sentence, pre-main): Self-driving cars are of course advanced, but I’m still a bit worried."), ("出国旅游很有意思，当然，也要花很多钱。", "6 Traveling abroad (my sentence, post-main): Traveling abroad is a lot of fun, though of course it also costs a lot of money. (the pictures are not included, so these sentences are only my samples)")]
DA3 = [("要学好中文，背生词很重要。", "Activity 3A, the book’s example. Student A: To learn Chinese well, memorizing new words is very important."), ("背生词当然很重要，但是，不要忘了多读多听真实语料。", "Student B: Memorizing new words is of course very important, but don’t forget to read and listen to a lot of authentic material."),
       ("想减肥就要少吃。", "Activity 3B, the book’s example. Common idea: If you want to lose weight, you must eat less."), ("想减肥就要少吃，当然，锻炼也很重要。", "Response: If you want to lose weight you must eat less; of course, exercise is also important."), ("想减肥就要少吃，当然，吃得太少对身体也不好。", "Or: … of course, eating too little is also bad for the body."),
       ("在中国学中文最好，当然，在别的地方也可以。", "My sample (3A, student A): Studying Chinese in China is best, though of course you can also do it elsewhere.")]
L2 = lesson(
    "Lesson 29 Presentation 1 grammar: the concessive use of 当然",
    "当然 · 后置的当然 · 前置的当然 · 但是/可是/不过 · 当然也可以 · 当然很重要，但是",
    requires=[],
    cards=[
        card("The concessive use of 当然",
             "In conversation or discourse, the “当然 clause” provides a concessional tone to the main opinion of the speaker. There are two types: 1) post-main clause use, and 2) pre-main clause use. Post-main clause use: this type of 当然 clause offers a secondary choice or opinion to the speaker’s main notion to soften the tone (main clause + 当然 clause). Pre-main clause use: in conversation, the pre-main clause 当然 is often used to acknowledge the other speaker’s opinion or a common opinion first, then offer a contradicting opinion of the main speaker, so as to make this opinion less forceful and offer a concessionary tone (当然 clause + adversative conjunction (但是/可是/不过) + main clause).",
             examples=[D(z, e) for z, e in DR1 + DR2]),
        card("Activities 1 to 3",
             "Activity 1 (Reading): Translate the following sentences into English. Note the function of 当然 in each sentence. Activity 2 (Speaking): Create sentences with the concessive 当然, using the pictures for reference (1. Exercise 2. Learning Chinese 3. Join military 4. Order fast food 5. Self-driving car 6. Traveling abroad). Make sure you use both pre-main and post-main clauses in your sentences. Pair up and share your work with your partner. Activity 3 (Speaking): A. Pair up. Student A makes a statement. Student B acknowledges it with 当然, then uses 但是/可是/不过 to add a contradictory idea to it. Then, switch roles. B. Work with your partner to find common ideas, then use 当然 to add secondary thoughts to the ideas. The sentences, my translations and samples:",
             examples=[D(z, e) for z, e in DA1 + DA2 + DA3]),
    ],
    exercises=[
        M("What does a post-main 当然 clause do?", "Offers a secondary choice or opinion to soften the tone", ["Asks a question", "Repeats the main clause", "Ends the sentence with a command"], "offers a secondary choice/opinion to the speaker’s main notion."),
        M("What does a pre-main 当然 clause do?", "Acknowledges an opinion first, then the main speaker contradicts it politely", ["Adds a second reason", "Changes the topic", "Shows anger"], "acknowledge … first, then offer a contradicting opinion."),
        M("Which conjunction can follow a pre-main 当然 clause?", "但是, 可是 or 不过", ["所以", "因为", "如果"], "adversative conjunction."),
        M("In 钱当然很重要，但我觉得，生活中还应该有些别的什么, which type is 当然?", "Pre-main", ["Post-main", "Neither", "A question word"], "钱当然很重要，但…."),
        M("In 能赢最好 after 当然, what is the idea?", "Winning would be best", ["Losing would be best", "There is no match", "Nobody tries"], "当然，能赢最好."),
        M("What does 孩子听话当然是好事，但是… warn about?", "Check that the child is happy while obedient", ["Children must never listen", "Parents must shout", "Children should not study"], "他在听话的同时是不是快乐."),
        F("买高铁票很方便，当___也可以直接到火车站去买。", "然", ["为", "天", "果"], "当然: of course."),
        F("重视孩子的教育当然是好的，___家长们也应该重视孩子们的身心健康。", "但", ["和", "跟", "还"], "但: but."),
        F("背生词当然很重要，但是，不要忘了多读多听真实语___。", "料", ["言", "文", "话"], "语料: corpus."),
    ],
)

UNIT = unit("第二十九课 中国的教育 Presentation 1: 少年宫, 当然", [L1, L2])
