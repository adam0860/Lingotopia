"""Unit 104: Lesson 30 (Unit 5 review), Grammar and Usage Review: Activities 1-9 (starting a topic, elaborating, adding information, clarifying, strengthening an argument,
commenting, stating determination, softening one's tone, choosing the right phrase). Audio and pictures are not included; numbers the book writes as digits are spelled
out in Chinese text; answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('增长', 1, 'zhang3'), ('得奖', 0, 'de2')):
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

# ------------------------------------------------------------------ 1. grammar review acts 1-4
S1 = [("说到当地最好的广东菜馆，那就是东海餐馆了。", "Activity 1B, 1 (translations mine; my technique: “说到…” brings up a topic by mentioning it): Speaking of the best Cantonese restaurant in the area, that would be the Donghai Restaurant."),
      ("说起Ｓａｌｉｎａｓ，人们就会想到“美国的菜篮子”。", "2 (technique: “说起…” plus a well-known association): Speaking of Salinas, people think of “America’s salad bowl.” (the book writes Salinas in Latin letters)"),
      ("你们注意到了吗？随着经济的发展，自然环境越来越差了。", "3 (technique: a question that draws attention, “你们注意到了吗？”): Have you noticed? With economic development, the natural environment is getting worse and worse."),
      ("去过美国的人都注意到，那里冬天室内暖气温度太高，", "4 (technique: “…都注意到” appeals to a shared observation): People who have been to the U.S. have all noticed that in winter the indoor heating there is too hot, (the book prints this sentence with a final comma)"),
      ("你发现了吗？肚子饿的时候最好不要去商店买东西。", "5 (technique: a question that draws attention, “你发现了吗？”): Have you found out? When you are hungry it is best not to go shopping."),
      ("以前出门，人们主要是靠自行车和公交车，现在有了很多新的选择，其中最受欢迎的就是“滴滴出行”。", "6 (technique: contrasting past and present, “以前…现在…”): In the past, people going out mainly relied on bicycles and buses; now there are many new choices, the most popular of which is DiDi Chuxing.")]
S2 = [("人们喜欢她的视频，主要是因为画面非常美，而且还可以了解到中国的美食和文化。", "Activity 2A, 1 (translations mine; my technique: give the main reason, then add more with “而且”): People like her videos mainly because the pictures are very beautiful, and also one can learn about Chinese food and culture."),
      ("这一代年轻人比咱们的能力强多了。有的人年纪轻轻就开办了自己的公司，有的人二十多岁就当上了大学教授，还有的人在各种国际比赛中得奖。", "2 (technique: a general statement, then examples with “有的…有的…还有的…”): This generation of young people is much more capable than we are. Some started their own companies at a young age, some became university professors in their twenties, and others won prizes in various international competitions."),
      ("她说话做事的样子很像她的妈妈，特别是有些习惯动作，比如想问题的时候喜欢玩儿笔。", "3 (technique: a general statement, then a specific one with “特别是…比如…”): The way she speaks and acts is very like her mother, especially some habitual movements, for example liking to play with a pen when thinking about a problem.")]
S4 = [("压力大的时候可以做一些有氧运动，比如散步，慢跑，骑自行车，游泳，跳舞什么的。", "Activity 4, 1 (translations mine; my analysis: “比如” gives examples to clarify): When under stress you can do some aerobic exercise, for example walking, jogging, cycling, swimming, dancing and so on."),
      ("有些城市甚至有幼升小的考试，也就是说，从幼儿园毕业上小学也要经过考试。", "2 (“也就是说” restates in other words): Some cities even have an exam for moving from kindergarten to elementary school; that is to say, graduating from kindergarten into elementary school also requires an exam."),
      ("农民工的孩子不能在当地参加中考，就是初中升高中的考试。", "3 (“就是” defines the term): The children of migrant workers cannot take the zhongkao locally, that is, the exam for going from junior high to high school."),
      ("在这个信息发达的世界，出现了越来越多的“阿宅”。“阿宅”主要指的是那些整天呆在家里或宿舍里，除了上网，就是玩电游、看动漫，生活中只有自己，不喜欢跟别人在一起的人。", "4 (“主要指的是” defines the term): In this world of advanced information, more and more “otaku” have appeared. “Otaku” mainly refers to people who stay at home or in a dormitory all day, who apart from going online just play video games and watch anime, have only themselves in their lives and don’t like being with others."),
      ("在北京街头，你会看到一排排的红色自行车，只要用手机扫码就可以使用，在市区很多地方都有停放点，给人们提供了很多方便，这就是人们常说的“共享单车”。", "5 (“这就是人们常说的…” names what has been described): On Beijing’s streets you will see rows and rows of red bicycles that can be used just by scanning a code with a phone, with parking spots in many parts of the city, bringing people much convenience; this is what people often call “shared bikes.”")]
SIGN = table(["Activity", "Task (the answers are audio, blanks or free discussion; the book gives no key)"], [
    ["Activity 1A, 1C", "A. Pair up and discuss the techniques you can use to start a new topic that will get the attention of your audience. C. Pair up. Start a topic in a way that catches your partner’s attention (two blank lines)."],
    ["Activity 2B", "Elaborate on the topics in Activity 1, Parts B and C. You can use the above techniques, and feel free to explore. Share your work with your partner (six blank lines)."],
    ["Activity 3 (Listening and Speaking): How to Add Additional Information to Discourse", "There are two basic kinds of additional information to add to your discourse: coordinative/progressive and contrasting/adversative. Pair up. Listen to the following sentences (eight audio items), find the signal word for the additional information, and discuss with your partner the relationship between the additional information and the previous information. The book gives a table with the columns Signal Word and Purpose of the Additional Information."],
    ["Activity 4 (Reading and Speaking): How to Clarify Your Information", "Pair up. Explain the meanings of the underlined words and determine how the writer clarified the meanings. (The underlining is lost in the text.)"]],
    title="Grammar and Usage Review, Activities 1 to 4: the tasks")
L1 = lesson(
    "Lesson 30 Grammar and Usage Review: starting a topic, elaborating, adding and clarifying",
    "说到 · 说起 · 你们注意到了吗 · 主要是因为 · 有的…有的…还有的… · 比如 · 也就是说 · 主要指的是 · 这就是人们常说的",
    requires=[],
    cards=[
        card("Grammar and Usage Review, Activities 1 to 4", "How to start a topic and gain an audience’s attention; how to elaborate; how to add additional information; how to clarify your information. The tasks, the printed sentences and my notes on the techniques:", tables=[SIGN], examples=[D(z, e) for z, e in S1 + S2 + S4]),
    ],
    exercises=[
        M("Which opening brings up a topic by mentioning it?", "说到当地最好的广东菜馆……", ["再…也…", "为了…好…", "只好…"], "说到….."),
        M("Which opening draws attention with a question?", "你发现了吗？", ["说起", "以前……现在……", "也就是说"], "你发现了吗？"),
        M("Which pattern gives examples in 有的人……，有的人……，还有的人……?", "A list of examples after a general statement", ["A definition", "A question", "A conclusion"], "general statement, then examples."),
        M("What does “也就是说” do?", "Restates in other words", ["Asks a question", "Adds a contrast", "Starts a story"], "也就是说: that is to say."),
        M("What does “就是初中升高中的考试” do?", "Defines the term 中考", ["Gives an example", "Asks a question", "Adds a contrast"], "就是 defines 中考."),
        M("What does “这就是人们常说的‘共享单车’” do?", "Names what has just been described", ["Starts a topic", "Asks a question", "Quotes someone"], "这就是人们常说的…."),
        M("What does “阿宅” mainly refer to?", "People who stay at home and only go online, play games or watch anime", ["Fast runners", "Teachers", "Tourists"], "主要指的是整天呆在家里……的人."),
        F("你们注意到了___？随着经济的发展，自然环境越来越差了。", "吗", ["吧", "了", "的"], "你们注意到了吗？"),
        F("这一代年轻人比咱们的能力强多___。", "了", ["吗", "呢", "的"], "强多了: much stronger."),
        F("在北京街头，你会看到一___一排的红色自行车。", "排", ["个", "群", "堆"], "一排排: rows and rows."),
    ],
)

# ------------------------------------------------------------------ 2. grammar review acts 5-8
MT = table(["Column A (technique)", "Column B (the book’s sentence)", "My key"], [
    ["1. Use a rhetorical question to arouse listener’s thoughts and reflection.", "b. 当农民难道就不需要文化知识了吗？", "1-b"],
    ["2. Use a metaphor to boost the impression.", "e. 圆圆的月亮像镜子似的挂在天上。", "2-e"],
    ["3. Use parallel sentences to make your argument clear and organized, and to strengthen the emotion.", "d. 父亲是一座山，在困难时给我依靠；父亲是一片海，给我最深的爱；父亲是一盏灯，照亮我前方的路。", "3-d"],
    ["4. Use quotations to encourage others to support you.", "a. 就像爱因斯坦说的，“兴趣是最好的老师”，没有兴趣只有压力你是不可能学好的。", "4-a"],
    ["5. Use summarization to bring your narration to a conclusion and state your idea clearly.", "c. 你可以去图书馆查书，也可以上网查资料，还可以问同事，总之你明天一定要把报告交上来。", "5-c"]],
    title="Activity 5A: strengthening an argument (the book gives no key; the matching is mine)")
ST5 = [("当农民难道就不需要文化知识了吗？", "Activity 5A, b (translations mine): Does being a farmer mean you don’t need any education?"), ("圆圆的月亮像镜子似的挂在天上。", "e: The round moon hangs in the sky like a mirror."), ("父亲是一座山，在困难时给我依靠；父亲是一片海，给我最深的爱；父亲是一盏灯，照亮我前方的路。", "d: Father is a mountain, giving me support in hard times; Father is a sea, giving me the deepest love; Father is a lamp, lighting the road ahead of me."), ("就像爱因斯坦说的，“兴趣是最好的老师”，没有兴趣只有压力你是不可能学好的。", "a: As Einstein said, “Interest is the best teacher”; with no interest and only pressure you can’t possibly learn well."), ("你可以去图书馆查书，也可以上网查资料，还可以问同事，总之你明天一定要把报告交上来。", "c: You can go to the library to look up books, you can search for material online, and you can ask colleagues, but in short you must hand in the report tomorrow.")]
SP5 = [("出国旅游难道只是为了购物吗？", "Activity 5B, 1 (my sample; the book gives only the five prompts): Is traveling abroad only for shopping?"), ("外卖小哥像风一样，把热饭送到你的手上。", "2 (metaphor about delivery): The delivery man is like the wind, bringing hot food into your hands."), ("时间是一条河，带走了过去；朋友是一棵树，给我们阴凉；家人是一盏灯，永远为我们亮着。", "3 (parallel sentences): Time is a river that carries the past away; friends are a tree that gives us shade; family is a lamp that is always lit for us."), ("就像孔子说的，“有教无类”。", "4 (a quotation about education): As Confucius said, “In education there are no class distinctions.”"), ("总之，我在这里的学习生活很紧张，但是我每天都学到很多新东西。", "5 (summary about my life at DLI, kept generic): In short, my life of study here is very tense, but every day I learn a lot of new things.")]
SM = [("再苦再累，我也要完成这个任务。", "Activity 7B (my samples; the book gives six blank lines): However hard and tiring, I will complete this task."), ("不管别人怎么说，我都要走自己的路。", "No matter what others say, I will take my own road."), ("我一定要把中文学好。", "I will certainly learn Chinese well."), ("就是下雨他也要去。", "Even if it rains he will go.")]
SOFT = table(["Stern (my versions)", "Soft (my versions)"], [["他说的一点儿道理也没有。", "他说的好像不太有道理。"], ["那部电影一点儿意思也没有。", "那部电影好像不太有意思。"], ["这本书写得太差了。", "这本书写得不是特别好。"], ["你这样做完全不对。", "你这样做好像不太合适。"]], title="Activity 8: stern and soft versions of 他说的没道理 / 那部电影没意思 / 这本书写得不好 / 你这样做不对 (the book gives empty columns)")
TK = table(["Activity", "Task (audio or free production; the book gives no key)"], [["Activity 6 (Listening and Speaking): How to Comment", "A. Pair up. With your partner, listen to the following sentences (six audio items) and discuss how strongly the second speaker agrees with the first (Agree? Disagree?). B. Pair up. Your partner will make a statement and you comment on it. Take turns practicing, each partner makes three statements."], ["Activity 7 (Listening and Speaking): How to State Determination", "A. Listen to the statement and translate what you hear into English (five audio items). Then pair up and compare your work with your partner’s. B. Use 再…，也…，不管…，都…，要…，就…，一定，and 就是 to create sentences that state your determination, or that of people you know (six blank lines)."], ["Activity 8 (Reading and Speaking): How to soften one’s tone", "Rewrite the following sentences to make them sound sterner, and then write them softer: 1. 他说的没道理。 2. 那部电影没意思。 3. 这本书写得不好。 4. 你这样做不对。"]], title="Activities 6 to 8: the tasks")
L2 = lesson(
    "Lesson 30 Grammar and Usage Review: strengthening an argument, commenting, determination and softening",
    "难道…吗 · 像镜子似的 · 父亲是一座山 · 就像爱因斯坦说的 · 总之 · 再…也… · 不管…都… · 一点儿道理也没有 · 好像不太合适",
    requires=[],
    cards=[
        card("Grammar and Usage Review, Activity 5 (Reading and Speaking): How to Strengthen Your Argument", "A. In this unit, you learned several ways to strengthen your arguments and make your statements more impactful. Read the five techniques in Column A and match them with the sentences in Column B. B. Create your own statements and share them with your partner: 1. A rhetorical question about traveling abroad. 2. A metaphor about fast food delivery. 3. Parallel sentences about time, friendship, or family. 4. A quotation about education. 5. Summary about your life at DLI. The matching and my samples:", tables=[MT], examples=[D(z, e) for z, e in ST5 + SP5]),
        card("Grammar and Usage Review, Activities 6 to 8", "How to comment, how to state determination and how to soften one’s tone. The tasks, my samples and my stern and soft versions:", tables=[TK, SOFT], examples=[D(z, e) for z, e in SM]),
    ],
    exercises=[
        M("Which technique is “当农民难道就不需要文化知识了吗？”?", "A rhetorical question", ["A metaphor", "A quotation", "A summary"], "难道……吗."),
        M("Which technique is “圆圆的月亮像镜子似的挂在天上”?", "A metaphor", ["A rhetorical question", "Parallel sentences", "A summary"], "像镜子似的."),
        M("Which technique is “父亲是一座山……父亲是一片海……父亲是一盏灯……”?", "Parallel sentences", ["A metaphor only", "A quotation", "A question"], "parallel sentences."),
        M("Which technique is “就像爱因斯坦说的……”?", "A quotation", ["A summary", "A rhetorical question", "A comparison of price"], "就像…说的."),
        M("Which technique is “总之你明天一定要把报告交上来”?", "A summary", ["A quotation", "A metaphor", "A question"], "总之: in short."),
        M("Which word means “in short”?", "总之", ["比如", "难道", "就是"], "总之."),
        M("How can you make “他说的没道理” softer?", "他说的好像不太有道理", ["他说的一点儿道理也没有", "他说的完全不对", "他没有说话"], "Soft: 好像不太有道理."),
        M("Which sentence states determination?", "再苦再累，我也要完成这个任务", ["我可能去", "他也许来", "这本书不错"], "再…也…."),
        F("圆圆的月亮像镜子___的挂在天上。", "似", ["是", "样", "像"], "似的: like."),
        F("没有兴趣只有压力你是不可能学___的。", "好", ["完", "到", "上"], "学好: learn well."),
        F("___之你明天一定要把报告交上来。", "总", ["大", "一", "所"], "总之: in short."),
    ],
)

# ------------------------------------------------------------------ 3. activity 9
A9T = table(["No.", "Choices", "Sentence (the book’s, with the choice left open)", "Answer (my key)"], [
    ["1", "正是因为，主要是因为", "＿＿农民工的辛苦劳动，才有了中国城市的高速发展。", "正是因为"],
    ["2", "大多，多半儿", "我看他＿＿是不会去了。", "多半儿"],
    ["3", "不管，尽管", "＿＿这次考试很难，但我还是考出了好成绩。", "尽管"],
    ["4", "根据，据", "应该＿＿每个人的能力和特长来安排他们的工作。", "根据"],
    ["5", "认识到，了解到", "记者在采访中＿＿了真实的情况。", "了解到"],
    ["6", "只好，得", "下个星期，我＿＿去上海出差。", "得"],
    ["7", "为了，好", "老师又说了一遍，＿＿让同学们能记下来。", "好"],
    ["8", "用在，放在", "他把时间都＿＿打电子游戏上了。", "用在"],
    ["9", "坚持下去，坚持下来", "不管遇到(encounter)什么困难，都一定要＿＿。", "坚持下去"],
    ["10", "比不上，没有", "猴子(monkey)很聪明，不过＿＿大象(elephant)。但是，大象还＿＿海豚(dolphin)聪明。", "比不上；没有"],
    ["11", "上不起，付不起", "很多孩子考上了大学，但是＿＿学费。", "付不起"],
    ["12", "忙不过去，干不过来", "地里的活儿太多了，他一个人根本＿＿。", "干不过来"],
    ["13", "总的来说，一般来说", "这次考试的结果＿＿还是不错的。", "总的来说"],
    ["14", "跟着，随着", "＿＿经济的发展，人们的收入也不断提高。", "随着"]],
    title="Grammar and Usage Review, Activity 9: complete the sentence using one of the phrases supplied")
A9 = [("正是因为农民工的辛苦劳动，才有了中国城市的高速发展。", "Activity 9, 1 (completed sentences; my key; translations mine): It is precisely because of the migrant workers’ hard labor that Chinese cities have developed so fast."),
      ("我看他多半儿是不会去了。", "2: I think he probably won’t go any more."),
      ("尽管这次考试很难，但我还是考出了好成绩。", "3: Although this exam was very hard, I still got good results."),
      ("应该根据每个人的能力和特长来安排他们的工作。", "4: Work should be assigned according to each person’s ability and special talents."),
      ("记者在采访中了解到了真实的情况。", "5: In the interview the reporter learned the real situation."),
      ("下个星期，我得去上海出差。", "6: Next week I have to go to Shanghai on a business trip."),
      ("老师又说了一遍，好让同学们能记下来。", "7: The teacher said it once more so that the students could write it down."),
      ("他把时间都用在打电子游戏上了。", "8: He has spent all his time playing video games."),
      ("不管遇到什么困难，都一定要坚持下去。", "9: No matter what difficulties you meet, you must keep going."),
      ("猴子很聪明，不过比不上大象。但是，大象还没有海豚聪明。", "10: Monkeys are very clever, but they are no match for elephants. But elephants are still not as clever as dolphins."),
      ("很多孩子考上了大学，但是付不起学费。", "11: Many children get into university but can’t afford the tuition."),
      ("地里的活儿太多了，他一个人根本干不过来。", "12: There is too much work in the fields; he can’t possibly handle it alone."),
      ("这次考试的结果总的来说还是不错的。", "13: On the whole, the result of this exam is still good."),
      ("随着经济的发展，人们的收入也不断提高。", "14: With the development of the economy, people’s incomes also keep rising.")]
L3 = lesson(
    "Lesson 30 Grammar and Usage Review: choosing the right phrase (Activity 9)",
    "正是因为 · 多半儿 · 尽管 · 根据 · 了解到 · 得 · 好 · 用在 · 坚持下去 · 比不上 · 付不起 · 干不过来 · 总的来说 · 随着",
    requires=[],
    cards=[
        card("Grammar and Usage Review, Activity 9 (Reading and Speaking)", "Complete the sentence using one of the phrases supplied. Pair up and compare your work with your partner’s and discuss any inconsistencies. The book gives no key; my choices are below, with the completed sentences.", tables=[A9T], examples=[D(z, e) for z, e in A9]),
    ],
    exercises=[
        F("___农民工的辛苦劳动，才有了中国城市的高速发展。", "正是因为", ["主要是因为", "不管", "尽管"], "正是因为…才…: the pattern with 才."),
        F("我看他___是不会去了。", "多半儿", ["大多", "尽管", "根据"], "多半儿: probably."),
        F("___这次考试很难，但我还是考出了好成绩。", "尽管", ["不管", "根据", "随着"], "尽管…但是…: although…but…."),
        F("应该___每个人的能力和特长来安排他们的工作。", "根据", ["据", "跟着", "随着"], "根据: according to."),
        F("记者在采访中___了真实的情况。", "了解到", ["认识到", "放在", "用在"], "了解到: learn."),
        F("下个星期，我___去上海出差。", "得", ["只好", "好", "用"], "得: have to (a voluntary or reminding decision)."),
        F("老师又说了一遍，___让同学们能记下来。", "好", ["为了", "只好", "得"], "好: so that."),
        F("他把时间都___打电子游戏上了。", "用在", ["放在", "比不上", "付不起"], "用在…上: spend on."),
        F("不管遇到什么困难，都一定要___。", "坚持下去", ["坚持下来", "付不起", "干不过来"], "坚持下去: keep going."),
        F("猴子很聪明，不过___大象。", "比不上", ["没有", "付不起", "忙不过去"], "比不上: is no match for."),
        F("很多孩子考上了大学，但是___学费。", "付不起", ["上不起", "干不过来", "忙不过去"], "付不起学费: can’t afford the tuition."),
        F("地里的活儿太多了，他一个人根本___。", "干不过来", ["忙不过去", "付不起", "比不上"], "干不过来: can’t handle it."),
        F("这次考试的结果___还是不错的。", "总的来说", ["一般来说", "跟着", "多半儿"], "总的来说: on the whole."),
        F("___经济的发展，人们的收入也不断提高。", "随着", ["跟着", "根据", "尽管"], "随着: with."),
    ],
)

UNIT = unit("第三十课 复习课 Unit 5 Review: 语法和用法复习", [L1, L2, L3])
