"""Unit 95: Lesson 29 (Education in China), Presentation 1, second half: the grammar sections on 过来, 下来 vs. 下去 and 吧, the skill-integration tasks (interest classes),
the using-Chinese tasks (a news report, statistics, a father who borrowed money for piano lessons) and the vocabulary list.
Audio, pictures and charts are not included; answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l29_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('少年宫', 0, 'shao4'), ('长大', 0, 'zhang3'), ('觉得自己', 1, 'de5'), ('女孩还报', 1, 'hai2'), ('男孩还报', 1, 'hai2'), ('成长', 1, 'zhang3')):
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

# ------------------------------------------------------------------ 1. 过来
GT = table(["Usage", "Meaning of 过来 as a resultative complement"], [["1", "Movement in a direction (literal meaning)"], ["2", "Change of state (figurative meaning, usually indicating a return to an original, normal, and typically improved state)"], ["3", "Degree of feasibility (figurative meaning, with sufficiency of time, ability to manage something, usually used in negative or interrogative sentences)"]], title="过来 as resultative complements: when used as a resultative complement, 过来 has three meanings")
GE = [("她向我走过来。", "Usage 1: She walks toward me. (translations mine)"), ("你得把这个坏习惯改过来。", "Usage 2: You have to correct this bad habit."), ("这么多兴趣班，孩子学得过来吗？", "Usage 3: So many interest classes; can the child manage to learn them all?")]
G4 = [("我接到一个从美国打过来的电话。", "Activity 4, 1 (translations mine): I received a phone call made from America."), ("工作这么多，一个人根本忙不过来。", "2: There is so much work that one person simply can’t manage it all."), ("等他明白过来，已经太晚了。", "3: By the time he realized (came to understand), it was already too late."), ("我的手很冷，半天也暖和不过来。", "4: My hands are very cold and haven’t warmed up for ages."), ("事情不多，我一个人也忙得过来。", "5: There isn’t much to do; I can manage it alone.")]
G5 = [("天上的星星，多得数不过来。", "Activity 5, 1 (my completion; the images are not included): The stars in the sky are too many to count."), ("你买这么多书，看得过来吗？", "2 (my completion): You bought so many books; can you manage to read them?"), ("以后的知识越来越多，我们学不过来。", "3 (my completion): The knowledge of the future will grow and grow and we won’t be able to learn it all."), ("他说了半天，我还没明白过来。", "4 (my completion): He talked for ages and I still haven’t understood."), ("这么多孩子，老师一个人照顾不过来。", "5 (my completion): So many children; one teacher can’t take care of them all.")]
# ------------------------------------------------------------------ 2. 下来 / 下去
XE = [("大卫很喜欢汉语，他还想继续学下去。", "下来 vs. 下去, 1: David likes Chinese very much and wants to keep studying it. (translations mine)"), ("为了“活”下去，邮局扩大了自己的业务。", "2: In order to “survive,” the post office expanded its business."), ("现在，邮局不但活了下来，而且发展得越来越好。", "3: Now the post office has not only survived but is developing better and better."), ("她终于坚持下来了。", "4: She finally stuck it out."), ("经过医生们的努力，孩子活下来了。", "5: Thanks to the doctors’ efforts, the child survived.")]
XP = table(["", "Potential complement form of 下去 (“able to go on” / “can’t go on”; 了 is often used at the end of the negative sentence)"], [["Affirmative", "Verb + 得 + 下去"], ["Negative", "Verb + 不 + 下去 (+ 了)"]], title="Potential complement form of 下去")
XD = [("A", "这本书这么难，你看得下去吗？", "1. A: This book is so hard; can you keep reading it? (translations mine)"), ("B", "看得下去！", "B: I can!")]
XS = [("这个电影真没意思，我看不下去了。", "2. This movie is really boring; I can’t go on watching it."), ("这儿太冷了，我住不下去了。", "3. It is too cold here; I can’t go on living here."), ("我跟他过不下去了，我要离婚！", "4. I can’t go on living with him; I want a divorce!"),
      ("我不能再这样胖下去了，我要减肥！", "Note: “Adjective + 下去” indicates a state that has existed and will continue to develop, usually with a negative connotation. For example: I can’t keep getting fatter like this; I’m going to lose weight!"), ("现在才六月，天气还会热下去。", "It is only June now, and the weather will keep getting hotter.")]
X6 = [("你再喝下去就醉了。", "Activity 6A, 1 (translations mine): If you keep drinking you will get drunk."), ("再这样干下去，你会生病的。", "2: If you keep working like this, you will get sick."), ("他看了我一眼，又接着说了下去。", "3: He glanced at me and then went on talking."), ("你不能这样生活下去了。", "4: You can’t go on living like this."), ("我们谈不下去了。", "5: We can’t go on talking."), ("坚持下去，很快就要到了。", "6: Keep going; we’ll be there soon.")]
X6B = [("这里的房租便宜，交通又方便，我打算住下去。", "Activity 6B, 1 (my completion): The rent here is cheap and the transportation is convenient; I plan to go on living here."), ("这件事很有意思，我想继续做下去。", "2 (my completion): This matter is very interesting; I want to keep doing it."), ("为了孩子们，我一定要坚持下去。", "3 (my completion): For the sake of the children, I will certainly keep going."),
       ("没有他们的帮助，我们的公司就办不下去了。", "4 (my completion): Without their help our company couldn’t go on."), ("这本书对你会很有帮助的，你一定要看下去。", "5 (my completion): This book will be very helpful to you; you must keep reading."), ("这本书没意思，我看不下去了。", "6 (my completion): This book is boring; I can’t go on reading it.")]
# ------------------------------------------------------------------ 3. 吧
BE = [("A", "你们怎么收费？", "1. A: How do you charge? (the particle 吧 expresses an indefinite tone, to convey real uncertainty or to soften a comment; translations mine)"), ("B", "我们收费比外面低得多，上一个班一年三千元左右吧。", "B: Our fees are much lower than outside, about three thousand yuan a year for one class, I’d say."),
      ("A", "听说有些家长喜欢和别人比，会同时给孩子报好几个班。", "2. A: I hear some parents like to compare with others and sign their children up for quite a few classes at the same time."), ("B", "一般也就两三个吧。", "B: Generally just two or three, I’d say."),
      ("A", "他这次考得怎么样？", "3. A: How did he do on the exam this time?"), ("B", "还可以吧。", "B: Not bad, I guess."),
      ("A", "那个送快递的晚了五分钟，我要给他差评！", "4. A: That delivery man was five minutes late; I’m going to give him a bad review!"), ("B", "这样做不太好吧。", "B: Doing that isn’t quite right, is it?"),
      ("A", "这个题是这样做吗？", "5. A: Is this problem done this way?"), ("B", "应该是吧。", "B: It should be, I think.")]
B7 = [("这样做不太好吧。", "Activity 7, 1 (my sample reply; liquor at a party with guests under 21): That isn’t quite right, is it?"), ("大概五百公里吧。", "2 (my sample; how far from Monterey to Los Angeles): About five hundred kilometers, I’d say."), ("不太多，够用吧。", "3 (my sample; how much is your pay): Not much; enough to get by, I guess."),
      ("还可以吧。", "4 (my sample; are you stressed from your studies): It’s okay, I guess."), ("我想想，大概两三站吧。", "5 (my sample; how many bus stops from school to the shopping center): Let me think, perhaps two or three stops.")]
BU = [("我们走吧！", "Different uses of 吧, 1. Making suggestions (吧 makes a suggestion more tentative and polite): Let’s go! (translations mine)"), ("今天天气不太好，我们还是明天去吧。", "2. 还是…吧 indicates a selected choice or a preference: The weather isn’t good today; we had better go tomorrow."),
      ("A", "这件太贵了！", "3. To concede a point (to accept or agree with something you’re not particularly happy about). A: This one is too expensive!"), ("B", "好吧，那就别买了。", "B: All right then, let’s not buy it."),
      ("我们收费比外面低得多，上一个班一年三千元左右吧。", "4. To form an indefinite tone: Our fees are much lower than outside, about three thousand yuan a year for one class, I’d say."),
      ("你的中文说得非常好，一定有很多学习体会吧？", "5. To seek confirmation of assumed information or thoughts: Your Chinese is excellent; you must have a lot of learning experience, right?"),
      ("A", "今天美元对人民币的兑换率是一比六点九。", "6. To respond with a decision after giving thought to the other speaker’s question, request or proposal. A: Today’s exchange rate of the U.S. dollar to the renminbi is one to six point nine."), ("B", "那我换三百美元吧。", "B: Then I’ll change three hundred dollars.")]
B9 = [("我们的蔬菜很新鲜，你买一点吧。", "Activity 9, 1 (suggestion; my completion): Our vegetables are very fresh; why not buy some? (translations mine)"),
      ("A", "我每天早上五点起床。", "2 (confirm an assumption; my completion). A: I get up at five o’clock every morning."), ("B", "你一定很早睡觉吧？", "B: You must go to bed very early, right?"),
      ("A", "聚会什么时候开始？", "3 (estimation; my completion). A: When does the party start?"), ("B", "大概七点吧。", "B: Around seven, I’d say."),
      ("A", "你要存定期还是活期？", "4 (come to a decision; my completion). A: Do you want a fixed deposit or a current one?"), ("B", "那我存活期吧。", "B: Then I’ll take a current one."),
      ("A", "我在准备考试呢。", "5 (preference; my completion). A: I’m preparing for an exam."), ("B", "那你还是明天再来吧。", "B: Then you had better come tomorrow."),
      ("A", "我太累了，不想做饭。", "6 (concession; my completion). A: I’m too tired and don’t want to cook."), ("B", "好吧，那我们出去吃吧。", "B: All right, then let’s eat out.")]

def _mix(items):
    out = []
    for it in items:
        out.append(it)
    return out

L1 = lesson(
    "Lesson 29 Presentation 1 grammar: 过来 as a resultative complement",
    "走过来 · 改过来 · 学得过来 · 忙不过来 · 明白过来 · 暖和不过来",
    requires=[],
    cards=[
        card("过来 as resultative complements",
             "When used as a resultative complement, 过来 has three meanings: (1) movement in a direction, (2) change of state, and (3) degree of feasibility. Activity 4 (Reading): Translate the following sentences into English. Activity 5 (Reading and Speaking): Use the images to complete the sentences. Share your work with the class. The five beginnings are: 1. 天上的星星 2. 你买这么多书, 3. 以后的知识越来越多, 4. 他说了半天, 5. 这么多孩子, The examples, my translations and my completions:",
             tables=[GT], examples=[D(z, e) for z, e in GE + G4 + G5]),
    ],
    exercises=[
        M("What does 过来 mean in 她向我走过来?", "Movement in a direction", ["Change of state", "Feasibility", "Past tense"], "Usage 1."),
        M("What does 过来 mean in 你得把这个坏习惯改过来?", "Change of state, a return to a normal state", ["Movement toward me", "Feasibility", "A question"], "Usage 2."),
        M("What does 学得过来 express?", "Being able to manage to learn", ["Having learned", "Not wanting to learn", "Learning in the past"], "Usage 3."),
        M("What does 一个人根本忙不过来 mean?", "One person simply can’t handle it all", ["One person is not busy", "One person came over", "Everyone is busy"], "忙不过来."),
        M("What does 等他明白过来 mean?", "By the time he came to understand", ["After he leaves", "Before he arrives", "If he sleeps"], "明白过来: change of state."),
        M("In which sentence types is usage 3 usually used?", "Negative or interrogative", ["Only commands", "Only past tense", "Only exclamations"], "usually used in negative or interrogative sentences."),
        F("事情不多，我一个人也忙得___来。", "过", ["回", "进", "出"], "忙得过来: can manage."),
        F("我接到一个从美国打___来的电话。", "过", ["回", "进", "出"], "打过来: call from."),
        F("这么多兴趣班，孩子学得过___吗？", "来", ["去", "上", "下"], "学得过来吗?"),
    ],
)

L2 = lesson(
    "Lesson 29 Presentation 1 grammar: 下来 vs. 下去, and the potential complement 得下去 / 不下去",
    "坚持下来 · 坚持下去 · 活下来 · 学下去 · 看得下去 · 住不下去了 · 胖下去",
    requires=[],
    cards=[
        card("下来 vs. 下去",
             "When 下来 and 下去 are used as directional complements, they can indicate the continuation of an action. “Verb + 下来” means an action was started in the past and continues until the present; it was not easy, but it was completed. “Verb + 下去” means an action has begun and will continue. The verbs commonly used include 坚持, 活, 保存, 学, 跑, etc., usually preceded by a modal auxiliary verb like 要, 想, 能, 一定, 应该, or an adverb that indicates time, like 再, 又, 接着, 继续, etc. Potential complement form of 下去: it means “able to go on” / “can’t go on” (doing something). Affirmative: Verb + 得 + 下去; negative: Verb + 不 + 下去 (+ 了). 了 is often used at the end of the negative sentence.",
             tables=[XP], examples=[D(z, e) for z, e in XE] + dlg(XD) + [D(z, e) for z, e in XS]),
        card("Activity 6 (Reading, Writing, and Speaking)",
             "A. Translate the following sentences into English. B. Complete the sentences using 下去 (the beginnings are 1. 这里的房租便宜，交通又方便， 2. 这件事很有意思， 3. 为了孩子们， 4. 没有他们的帮助， 5. 这本书对你会很有帮助的， 6. 这本书没意思，). C. Pair up. Tell your partner something you have been doing persistently and something you plan to keep on doing. The sentences, with my translations and my completions:",
             examples=[D(z, e) for z, e in X6 + X6B]),
    ],
    exercises=[
        M("What does “Verb + 下来” mean?", "Started in the past and continues until now, completed with difficulty", ["Will start tomorrow", "Never started", "Ended long ago"], "an action was started in the past and continues until the present."),
        M("What does “Verb + 下去” mean?", "An action has begun and will continue", ["An action ended", "An action never began", "An action is a question"], "an action has begun and will continue."),
        M("What does 孩子活下来了 mean?", "The child survived", ["The child lived there", "The child left", "The child was born"], "孩子活下来了."),
        M("What does 看不下去了 mean?", "I can’t go on watching", ["I can’t see", "I don’t look down", "I watched yesterday"], "我看不下去了."),
        M("What is the affirmative potential form?", "Verb + 得 + 下去", ["Verb + 不 + 下去", "Verb + 了", "Verb + 过"], "Verb + 得 + 下去."),
        M("What is often added to the end of the negative sentence?", "了", ["吗", "呢", "啊"], "了 is often used at the end of the negative sentence."),
        M("What does “Adjective + 下去” indicate?", "A state that has existed and will continue, usually negative", ["A change to the opposite", "A question", "A past event"], "usually with a negative connotation."),
        F("为了孩子们，我一定要坚持___去。", "下", ["过", "回", "出"], "坚持下去: keep going."),
        F("这本书这么难，你看得下___吗？", "去", ["来", "上", "到"], "看得下去吗?"),
        F("现在，邮局不但活了下来，而___发展得越来越好。", "且", ["是", "也", "还"], "不但…而且…."),
    ],
)

L3 = lesson(
    "Lesson 29 Presentation 1 grammar: 吧 to express an indefinite tone, and the different uses of 吧",
    "左右吧 · 还可以吧 · 不太好吧 · 我们走吧 · 还是…吧 · 好吧 · 一定…吧？ · 那我…吧",
    requires=[],
    cards=[
        card("吧 to express an indefinite tone",
             "The particle 吧 can be used to express an indefinite tone, either to convey a real sense of uncertainty or to soften a comment to make it more polite, gentle, and less forceful. Activity 7 (Speaking): What would you say in the following situations? Share your work with a classmate. 1. Your friend suggests a party with liquor, although there are attendees under 21. 2. Your friend asks how far it is from Monterey to Los Angeles. 3. Your friend asks how much your pay is. 4. Your friend asks if you are stressed from your studies. 5. Your friend asks how many bus stops there are from DLI to Del Monte Shopping Center. The examples and my sample replies:",
             examples=dlg(BE) + [D(z, e) for z, e in B7]),
        card("Different uses of 吧",
             "1. Making suggestions. 2. 还是…吧 indicates a selected choice or a preference. 3. To concede a point. 4. To form an indefinite tone. 5. To seek confirmation of assumed information or thoughts. 6. To respond with a decision after giving thought to the other speaker’s question, request, or proposal. Activity 8 (Listening and Speaking): Listen to a short dialog and explain the function of 吧 in each sentence (six audio items, which are not included, so I give no key). Activity 9 (Reading and Speaking): Complete the sentences using the tone in parentheses. Share your work with your partner. The examples and my completions:",
             examples=[D(*BU[0]), D(*BU[1])] + dlg(BU[2:4]) + [D(*BU[4]), D(*BU[5])] + dlg(BU[6:8]) + dlg(B9[1:3]) + [D(*B9[0])] + dlg(B9[3:])),
    ],
    exercises=[
        M("What does 吧 do in 上一个班一年三千元左右吧?", "Gives an indefinite, softened estimate", ["Asks a question", "Gives an order", "Shows anger"], "to form an indefinite tone."),
        M("What does 还是明天去吧 express?", "A preference or selected choice", ["A refusal", "A past event", "A surprise"], "还是…吧."),
        M("What does 好吧，那就别买了 express?", "Conceding a point", ["Joy", "A suggestion to buy", "A threat"], "To concede a point."),
        M("What does 你一定有很多学习体会吧？ do?", "Seeks confirmation of an assumption", ["Gives a command", "Makes a suggestion", "Refuses"], "To seek confirmation."),
        M("What does 那我换三百美元吧 express?", "A decision after thought", ["A doubt", "A question", "A refusal"], "To respond with a decision."),
        M("What does 我们走吧！ express?", "A tentative, polite suggestion", ["A threat", "A question about time", "A refusal"], "Making suggestions."),
        F("A: 那个送快递的晚了五分钟，我要给他差评！ B: 这样做不太好___。", "吧", PART, "吧: softened disagreement."),
        F("A: 他这次考得怎么样？ B: 还可以___。", "吧", PART, "还可以吧."),
        F("A: 这个题是这样做吗？ B: 应该是___。", "吧", PART, "应该是吧."),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
IN1 = table(["Part", "Group listening (audio; the passage’s title is printed in the book)"], [["Part 1 / Part 2 / Part 3", "给孩子报兴趣班时要注意哪些问题"]], title="Skill Integration, Activity 1: Divide the class into three groups; each listens to part of the passage (Parts 1, 2 and 3 are audio and are not included)")
IQ = [("给孩子报兴趣班时要注意哪几点？", "Activity 1C, 1 (questions as printed; no key, since they depend on audio): What points should one pay attention to when signing a child up for interest classes?"), ("为什么应该让孩子上兴趣班？", "2: Why should children attend interest classes?"), ("有什么样的办法来帮助孩子选兴趣班？", "3: What methods are there to help a child choose interest classes?"), ("孩子在上兴趣班时会有什么问题？", "4: What problems might children have while attending interest classes?"), ("孩子不想学的时候家长应该怎么办？", "5: What should parents do when the child doesn’t want to study?"), ("作者举了什么样的例子？这个例子的目的是什么？", "6: What kind of example did the author give? What is the purpose of this example?")]
M2A = ("我以前也不想给孩子报那么多兴趣班，只要她健康快乐就行了。但是看看周围同事们的孩子，从小就上各种兴趣班，我就开始担心自己的孩子了，怕她只知道玩儿，别的什么也不会。所以在我女儿两岁半的时候，我给她报了英语班，后来又报了钢琴班和舞蹈班。所有的兴趣班都是我们家长选的，这么小的孩子也不知道喜欢什么不喜欢什么。兴趣爱好都是要培养的，她学着学着就会感兴趣了。", "I used not to want to sign my child up for so many interest classes either; it was enough for her to be healthy and happy. But looking at my colleagues’ children, who attended all kinds of interest classes from an early age, I began to worry about my own child, afraid she would only know how to play and nothing else. So when my daughter was two and a half I signed her up for an English class, and later for piano and dance classes. All the interest classes were chosen by us parents; such a small child doesn’t know what she likes or dislikes. Interests and hobbies have to be cultivated; as she keeps studying she will become interested. (Activity 2A, an interview; translation mine)")
M2C = ("小孩子放暑假在家里，除了写作业就是上网玩儿游戏。给他们报兴趣班，可以丰富生活。两个孩子都报了音乐班，另外，男孩报了武术，女孩报了舞蹈。他们都很喜欢来这里上课。有时候还会去参加一些演出活动，对小孩子的成长很有好处，增加了他们的学习兴趣，认识了很多新朋友。我们也不会给孩子什么压力，每天练习半个小时左右，作业少的时候就多练一点。", "When children are at home on summer vacation, besides doing homework they just play games online. Signing them up for interest classes can enrich their lives. Both children signed up for a music class, and in addition the boy signed up for martial arts and the girl for dance. They both like coming here to class. Sometimes they also take part in some performances, which is very good for little children’s growth, increases their interest in learning and lets them meet many new friends. We also don’t put any pressure on the children; they practice about half an hour a day, and more when there is less homework. (Activity 2C; translation mine)")
M2Q = [("我觉得她这样做有她的道理，但是应该多听听孩子自己的想法。", "Activity 2A (a sample of what I think of the mother’s decision, my own view; the activity asks for the learner’s opinion): I think she has her reasons, but should listen more to the child’s own ideas."),
       ("两个孩子都报了音乐班，男孩还报了武术，女孩还报了舞蹈。", "Activity 2C-1 (my answer): Both children take music; the boy also takes martial arts and the girl dance."), ("可以丰富生活，对小孩子的成长很有好处，增加他们的学习兴趣，认识很多新朋友。", "2C-2 (my answer): It enriches their lives, is good for their growth, increases their interest in learning and lets them meet new friends."),
       ("他们都很喜欢，因为他们很喜欢来这里上课，家长也不给他们什么压力。", "2C-3 (my answer): Yes, they like it, because they like coming to class here and the parents put no pressure on them.")]
M2B = table(["Activity", "Audio tasks (no key, since they depend on the recording)"], [["2B", "Listen to a father speaking about his son’s hobby classes: 1. How many classes did his son take? 2. How much money did he spend on the classes? 3. What is his attitude toward the cost of his son’s education?"], ["2D", "Listen to a student speaking about her hobby classes. Take notes and share your notes with your partner. Find the differences in your notes and listen to the dialog again to address any inconsistencies."], ["2E", "In groups of three, rank the parents in the above passages (including the parents of the student in Passage 4) according to your degree of approval of their attitude toward their children’s interest in their hobby classes. Tell your partners the reasons for your ranking."]], title="Activity 2: the audio and discussion tasks")
L4 = lesson(
    "Lesson 29 Presentation 1 skill integration: what to watch for when signing children up for interest classes",
    "给孩子报兴趣班 · 两岁半 · 各种兴趣班 · 暑假 · 丰富生活 · 演出 · 压力 · 练习半个小时",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Reading, Listening, and Speaking)",
             "A. Divide the class into three groups, 1, 2, and 3. Each group listens to part of the passage. Discuss what you hear within the group and make sure each member understands their part thoroughly. Discuss any unknown words and take brief notes on your passage. B. Regroup so that you join a new group. Tell your partners about the part you listened to and take notes on their parts. C. Answer the following questions and compare your work with that of your new partners. The title, and the questions as printed:",
             tables=[IN1], examples=[D(z, e) for z, e in IQ]),
        card("Skill Integration, Activity 2 (Reading, Speaking, and Listening)",
             "A. Pair up and read the following interview. Tell your partner what you think of the mother’s decision. B. Listen to a father speaking about his son’s hobby classes and answer the questions. C. Read about a mother’s thoughts on her children’s hobby classes and discuss the following questions with your partner: 1. What kinds of classes do her children take? 2. According to the mother, what is the benefit of taking hobby classes? 3. Do you think the children like the hobby classes? Why? D. Listen to a student speaking about her hobby classes. E. In groups of three, rank the parents. The two passages, my answers and the audio tasks:",
             tables=[M2B], examples=[D(*M2A), D(*M2C)] + [D(z, e) for z, e in M2Q]),
    ],
    exercises=[
        M("Why did the mother first sign her daughter up for classes?", "She worried her child would only know how to play", ["She was told to by law", "She wanted money", "She had nothing to do"], "怕她只知道玩儿，别的什么也不会."),
        M("How old was her daughter at the first class?", "Two and a half", ["Ten", "Half a year", "Twelve"], "两岁半."),
        M("Who chose all the classes?", "The parents", ["The teacher", "The child", "The neighbors"], "所有的兴趣班都是我们家长选的."),
        M("What does the first mother say about interests?", "They have to be cultivated", ["They come naturally", "They are useless", "They cost nothing"], "兴趣爱好都是要培养的."),
        M("What do the children in Passage C do at home during the summer besides homework?", "Play games online", ["Study abroad", "Work", "Travel"], "除了写作业就是上网玩儿游戏."),
        M("Which classes did both children in Passage C sign up for?", "Music", ["Martial arts only", "Dance only", "English"], "两个孩子都报了音乐班."),
        M("How long do the children practice each day?", "About half an hour", ["Five hours", "Ten minutes", "All day"], "每天练习半个小时左右."),
        M("What does the mother in Passage C avoid giving her children?", "Pressure", ["Presents", "Pocket money", "Food"], "我们也不会给孩子什么压力."),
        F("她学着学着就会感兴___了。", "趣", ["字", "话", "书"], "感兴趣: become interested."),
        F("给他们报兴趣班，可以丰___生活。", "富", ["有", "多", "好"], "丰富: enrich."),
        F("每天练习半个小时左___，作业少的时候就多练一点。", "右", ["左", "上", "下"], "左右: about."),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese
UCN = table(["Activity", "Tasks without key (they depend on screenshots, recordings or a chart that are not included)"], [["Activity 1", "A. In groups of three, study the screenshots of a TV news report about what happened at 北京市少年宫. Within your group, guess the content of the news report and share it with the class. B. (Listen to the news report and write the EEIs.) C. Compare the EEIs from your team’s work in part A with those of the other group. The group with the most correct information wins."], ["Activity 2", "In groups of three, study the statistics below (a chart titled 你为什么让孩子上兴趣班?). Discuss things that are not clear and share the two points that are most interesting to you with your group."]], title="Using Chinese in Context, Activities 1 and 2")
UP = ("在参访中，我们见到一位父亲，他去年花在孩子兴趣班上的钱有很大一部分是借来的。这位父亲说，孩子喜欢弹钢琴，跟着当地一位非常有名的钢琴大师学习，学费很高。但是这位父亲觉得，衣食住行都可以省，孩子教育不能省，他说：“很多东西比钱更重要，要学就学最好的。”", "During our visit we met a father, a large part of the money he spent last year on his child’s interest classes was borrowed. This father said his child likes playing the piano and studies with a very famous local piano master, and the tuition is very high. But this father feels that food, clothing, housing and transport can all be economized on, whereas a child’s education cannot be; he said, “Many things are more important than money; if you study, study with the best.” (Activity 3A; the book numbers and underlines three expressions: 1) 借来的, 2) 大师, 3) 衣食住行; translation mine)")
UW = table(["Underlined expression", "Meaning (mine)"], [["1) 借来的", "borrowed"], ["2) 大师", "master (of an art)"], ["3) 衣食住行", "clothing, food, housing and transport; the basic necessities of daily life"]], title="Activity 3A: the three underlined expressions", say=[0])
UA = [("他的态度是：衣食住行都可以省，孩子教育不能省。我同意他，因为教育对孩子的将来很重要；可是，借钱让孩子学钢琴，家里压力也不小。", "Activity 3B (a sample of my own view; the activity asks the learner to agree or disagree): His attitude is that food, clothing, housing and transport can be economized on but a child’s education cannot. I agree, because education is important for a child’s future; but borrowing money for piano lessons also puts great pressure on the family.")]
U4 = table(["Activity 4", "Prompts (my own paragraph is not given, since it is about the learner)"], [["A. Write a short paragraph about your hobbies", "What hobbies did you have as a child? Did you develop these hobbies on your own, or with the help of a teacher? How did you benefit from these hobbies? What were your parents’ attitudes toward your hobbies? In retrospect, what would you say to yourself as a child back then?"], ["B. In groups of three, each partner tells their stories. Evaluate them within the group.", "Who was the most persistent in pursuit of their hobbies? Whose parents were the most supportive? Who spent the most money on their hobbies? Who practiced the hardest on their hobbies?"]], title="Using Chinese in Context, Activity 4 (Writing, Listening and Speaking)")
L5 = lesson(
    "Lesson 29 Presentation 1 using Chinese in context: a news report, statistics, and a father who borrowed money for piano lessons",
    "北京市少年宫 · 你为什么让孩子上兴趣班 · 借钱 · 钢琴大师 · 衣食住行 · 教育不能省",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activities 1 and 2", "Activity 1 (Listening, Writing, and Speaking) and Activity 2 (Reading, Writing, and Speaking). The screenshots, the news report and the chart are not included.", tables=[UCN]),
        card("Using Chinese in Context, Activity 3 (Reading and Speaking)",
             "A. Pair up and read the following passage. Discuss the meanings of the underlined words with your partner. B. Form groups of three. Discuss the attitude of the man’s parents toward the education of his child. Do you agree or disagree with him? What is your reasoning? The passage, the three expressions and a sample view:",
             tables=[UW, U4], examples=[D(*UP)] + [D(z, e) for z, e in UA]),
    ],
    exercises=[
        M("How was a large part of the father’s spending on classes paid?", "With borrowed money", ["With a gift", "With a prize", "With savings only"], "有很大一部分是借来的."),
        M("What does the father’s child like to play?", "The piano", ["The violin", "Football", "Chess"], "孩子喜欢弹钢琴."),
        M("Who does the child study with?", "A very famous local piano master", ["A cousin", "A neighbor", "A student"], "跟着当地一位非常有名的钢琴大师学习."),
        M("What does the father say can be economized on?", "Food, clothing, housing and transport", ["Education", "Piano lessons", "Books"], "衣食住行都可以省."),
        M("What can’t be economized on, in his view?", "A child’s education", ["Food", "Travel", "Clothes"], "孩子教育不能省."),
        M("What does he say about learning?", "If you study, study with the best", ["Study as little as possible", "Study alone", "Study only when rich"], "要学就学最好的."),
        F("这位父亲觉得，衣食住行都可以___，孩子教育不能省。", "省", ["看", "想", "说"], "省: economize."),
        F("跟着当地一位非常有名的钢琴大___学习。", "师", ["家", "生", "人"], "大师: master."),
    ],
)

L6 = vocab_lesson("Lesson 29 Presentation 1 vocabulary", "16 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The entry 升学 is printed with a stray number from the page layout; I leave it out.", VOC1)

UNIT = unit("第二十九课 中国的教育 Presentation 1: 过来, 下来 下去, 吧, 兴趣班, 词汇", [L1, L2, L3, L4, L5, L6])
