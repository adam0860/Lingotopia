"""Unit 87: Lesson 28 (China's Youth), Presentation 1, first half: the dialog about the promising young generation with its activities (matching and fill-in),
the discourse grammar 那是, 可不, 说了, the 可……了 construction, the expression 注意到, and adverbs of degree.
Audio and pictures are not included; numbers the book writes as digits are spelled out in Chinese text; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l28_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('失去得到', 2, 'de2'), ('舍得', 0, 'she3'), ('舍得', 1, 'de5'), ('文明了', 2, 'le5')):
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

# ------------------------------------------------------------------ 1. objectives + presentation 1 + activity 1
P1 = [("小张", "老高，刚才电视上的英语演讲比赛，那几个年轻人英语说得太棒了！", "Xiao Zhang: Lao Gao, in the English speech contest on TV just now, those young people spoke English so well! (translations in this card are mine)"),
      ("老高", "对。他们从小就学英语，网上又有那么多的学习材料，当然能学好。", "Lao Gao: Right. They have studied English since childhood and there are so many learning materials online, so of course they can learn it well."),
      ("小张", "现在的学习条件多好，九零后、零零后真是赶上好时候了。", "Xiao Zhang: Learning conditions are so good now; the post-’90s and post-’00s have really caught good times."),
      ("老高", "那是。他们都是独生子女，父母舍得花钱，受教育的机会比咱们年轻的时候多多了。", "Lao Gao: Absolutely. They are all only children, their parents are willing to spend money, and their opportunities for education are far more than when we were young."),
      ("小张", "这代人不但知道得多，能力也比咱们强。", "Xiao Zhang: This generation not only knows a lot, but is also more capable than we are."),
      ("老高", "对，有些人年纪轻轻就有了自己的公司，还有的二十多岁就当上了大学教授。", "Lao Gao: Yes, some have their own companies while still very young, and some became university professors in their twenties."),
      ("小张", "他们不仅能力强，目标也高。有一个稳定的工作，已经不能让他们满足了。", "Xiao Zhang: Not only are they capable, their goals are also high. Having a stable job can no longer satisfy them."),
      ("老高", "可不。我儿子说了，他将来要做阿里巴巴的马云，或脸书的扎克伯格。", "Lao Gao: Exactly. My son said he wants to be the Jack Ma of Alibaba or the Zuckerberg of Facebook in the future."),
      ("小张", "这代人想得比咱们可高多了。你发现没有，他们做事也比较文明。", "Xiao Zhang: This generation thinks much higher than we do. Have you noticed that they also behave in a fairly civilized way?"),
      ("老高", "对。我也注意到，他们排队时不大会加塞儿，坐公交时还主动给老人让座。", "Lao Gao: Yes. I have also noticed that they rarely cut in line when queueing, and on the bus they even offer their seats to old people on their own initiative."),
      ("小张", "当然，他们也有一些不足的地方，比如生活能力就不太强。", "Xiao Zhang: Of course, they also have some shortcomings, for example their ability to take care of themselves isn’t very strong."),
      ("老高", "那是。不足总是有的，不过他们这一代还是大有前途的。", "Lao Gao: Absolutely. There are always shortcomings, but this generation still has a great future.")]
A1 = [("他们在谈这一代充满希望的年轻人。", "Activity 1A-1 (the book gives English choices; my answer): The promising young generation."), ("他们的条件大大改善了，所以知道得更多，能力也更强。", "1A-2 (my answer): They are more knowledgeable and capable due to greatly improved conditions."),
      ("因为他们从小就学英语，网上又有很多学习材料。", "1B-1 (my answer): Because they have studied English since childhood and there are many learning materials online."), ("他们的父母舍得花钱，让他们受教育的机会比以前多多了。", "1B-2 (my answer): Their parents are willing to spend money, so they have far more opportunities for education than before."),
      ("老高的儿子说，他将来要做马云或者扎克伯格；有的人年纪轻轻就有了自己的公司，还有的二十多岁就当上了大学教授。", "1B-3 (my answer): Lao Gao’s son says he wants to be Jack Ma or Zuckerberg; some have their own companies when very young and some become university professors in their twenties."),
      ("他们排队时不大会加塞儿，坐公交时还主动给老人让座。", "1B-4 (my answer): They rarely cut in line and offer their seats to old people on the bus."), ("他们的生活能力不太强。", "1B-5 (my answer): Their ability to take care of themselves is not very strong.")]
L1 = lesson(
    "Lesson 28 Presentation 1: the promising young generation",
    "第二十八课 中国的年轻人 · 独生子女 · 赶上好时候 · 舍得花钱 · 目标高 · 加塞儿 · 让座 · 大有前途",
    requires=[],
    cards=[
        card("Learning objectives of Lesson 28 (China’s Youth, 中国的年轻人)",
             "Upon completion of this lesson, you should be able to: discuss China’s youth including their education, abilities, and ambitions; discuss China’s youth including their values and experiences growing up; discuss China’s youth including their entrepreneurship, such as creativity, goals, and management skills. To perform the above you must master the new words and phrases associated with these functions and the following: discourse grammar (那是, 可不, 说了, 就像……说的, expressions to bring up or elaborate on a topic, inserting a question to draw the listener’s attention, 同时); the 可……了 construction; the expression 注意到; adverbs of degree; 就是 expressing insistence; parallel sentences; 呢 to express contrast; 什么 to soften the tone in a negative sentence; the use of …不…，但是…很… construction; the 要 + verb + 就 + verb …的 construction. The Area Studies topic is the post-’70, post-’80, post-’90 and post-’00 generations and the eras in which they grew up."),
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. What was your life like when you finished high school? B. What are some characteristics of Americans under 30, including education and lifestyle? (Two pictures are not included.)"),
        card("Presentation 1: 年轻的一代", "The dialog; the book also prints it in traditional characters.", examples=dlg(P1)),
        card("Activity 1 (Listening and Speaking)",
             "A. Global Listening: listen to Presentation 1 once and choose the correct answers. 1. What did the speakers talk about? (Their children who have their own business. / Young people who speak excellent English. / The promising young generation.) 2. Which of the following statements is true about many of those born in the 1990s or 2000s in China? (They are well educated, capable, ambitious, and financially successful. / They are more knowledgeable and capable due to greatly improved conditions. / They are as civilized as the prior generation in dealing with other people.) B. Detailed Listening: listen again and answer: 1. Why do some young people in China speak English so well? 2. How do the parents of these young people help them? 3. What example was given about young people’s ambitions? 4. What behaviors did Lao Gao observe about these young people? 5. What shortcomings do these young people have? My answers:",
             examples=[D(z, e) for z, e in A1]),
    ],
    exercises=[
        M("What did the two speakers mainly talk about?", "The promising young generation", ["A cooking show", "A football match", "The weather"], "大有前途."),
        M("Why can the young people speak English so well?", "They learned it from childhood and have many materials online", ["They live abroad", "They never study", "They only watch TV"], "从小就学英语…网上…学习材料."),
        M("Why are these young people called “only children”?", "They have no brothers or sisters", ["They are all orphans", "They are all twins", "They are all older"], "独生子女."),
        M("What are the parents like, according to Lao Gao?", "Willing to spend money on education", ["Unwilling to spend money", "Always away", "Very strict about TV"], "父母舍得花钱."),
        M("Which is an example of young people’s ambition?", "Wanting to be like Jack Ma or Zuckerberg", ["Wanting a stable job only", "Wanting to retire early", "Wanting to travel only"], "要做阿里巴巴的马云，或脸书的扎克伯格."),
        M("What did Lao Gao notice about their behavior?", "They rarely cut in line and give up seats on the bus", ["They cut in line often", "They never take buses", "They shout in public"], "不大会加塞儿…让座."),
        M("What shortcoming did Xiao Zhang mention?", "Their ability to take care of themselves is not strong", ["They don’t like English", "They are lazy at school", "They have no goals"], "生活能力就不太强."),
        M("What does 可不 express here?", "Agreement", ["Refusal", "Surprise", "A question"], "可不: Exactly."),
        M("What does 加塞儿 mean?", "Cut in line", ["Take a seat", "Make a call", "Buy a ticket"], "加塞儿."),
        F("现在的学习条件多好，九零后、零零后真是___上好时候了。", "赶", PART, "赶上: catch."),
        F("他们都是独生子女，父母舍___花钱。", "得", ["了", "过", "着"], "舍得: be willing."),
        F("不足总是有的，不过他们这一代还是大有前___的。", "途", PART, "前途: future."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2-4
T2 = table(["学习和生活环境", "成绩和目标", "行为 (behavior)"], [["从小就学英语; 网上有那么多的学习材料; 学习条件多好; 独生子女; 父母舍得花钱; 受教育的机会多多了", "英语说得太棒了; 知道得多; 能力比咱们强; 年纪轻轻就有了自己的公司; 二十多岁就当上了大学教授; 目标也高; 要做马云或扎克伯格", "做事比较文明; 排队时不大会加塞儿; 坐公交时主动给老人让座"]], title="Activity 2A: expressions from Presentation 1 (my sample; the book leaves the table empty)")
K2 = [("前边那个人，年纪轻轻的，别人排队他却加塞儿，太不文明了！", "Activity 2B-1 (my key: 年纪轻轻, 加塞儿, 文明): That person in front, so young, yet he cuts in while others are queueing; how uncivilized!"),
      ("王教授正在为明天的演讲准备材料。", "2B-3 (my key: 演讲, 材料): Professor Wang is preparing materials for tomorrow’s speech."), ("他们的能力很强，又有一个很大的目标，也注意到了自己的不足，将来一定会成功的。", "2B-4 (my key: 目标, 不足): Their ability is very strong and they have a big goal, and they have also noticed their own shortcomings; they will surely succeed in the future."),
      ("一个稳定的生活是不大会让他满足的。为了理想，他舍得失去得到的一切。", "2B-5 (my key: 满足, 舍得): A stable life would hardly satisfy him. For his ideal, he is willing to lose everything he has gained.")]
K22 = [("A", "他们这一代，多数是独生子女，从小生活条件就很好，真是赶上好时候了。", "2B-2 (my key: 独生子女, 赶上, 可不, 前途) A: Most of this generation are only children and have had very good living conditions since childhood; they really caught good times."), ("B", "可不。他们受教育的机会比我们多多了，将来一定很有前途。", "B: Exactly. Their educational opportunities are far more than ours, and they will surely have a great future.")]
D3 = table(["", "对话 1", "对话 2"], [["大意", "", ""], ["三个细节", "", ""]], title="Activity 3B: the summary table (the dialogs are audio and the three pictures A, B, C are not included; the cells are empty in the book)")
A4 = [("现在的年轻人不但能力强，也很注意文明礼貌。他们排队很少加塞儿。", "Activity 4, 1-d (my key): Young people today are not only capable but also pay attention to civility and manners. They rarely cut in line."), ("我弟弟虽然是个九零后，年纪很轻，可他已经是大学教授了。", "2-e: Although my younger brother is post-’90s and very young, he is already a university professor."),
      ("我们没赶上好时候，所以年轻时目标不高，只要有一个稳定的工作就满足了。", "3-g: We didn’t catch good times, so our goals were not high when we were young; we were satisfied as long as we had a stable job."), ("她的中文怎么说得那么棒？她从小就参加中文学校，也经常上网学中文。", "4-f: How does she speak Chinese so well? She has attended Chinese school since childhood and often studies Chinese online."),
      ("你们的条件比我们年轻时好得太多了，所以你们就应该想得比我们高。", "5-c: Your conditions are far better than ours were when we were young, so you should think higher than we did."), ("他们还年轻，一定会有这样或那样的不足。", "6-a: They are still young and will surely have one shortcoming or another."),
      ("他们都是独生子女的父母，虽然自己的生活条件不一定很好，可是都舍得花钱让孩子受很好的教育。", "7-b: They are all parents of only children; although their own living conditions are not necessarily good, they are all willing to spend money so that their child gets a very good education.")]
L2 = lesson(
    "Lesson 28 Presentation 1 activities 2-4: expressions, fill-in and matching",
    "独生子女 · 年纪轻轻 · 加塞儿 · 赶上 · 舍得 · 满足 · 不足 · 前途 · 演讲 · 材料",
    requires=[],
    cards=[
        card("Activity 2 (Writing, Speaking, and Reading)",
             "A. Pair up and think about the expressions in Presentation 1 that are related to the three areas shown in the table below. Write them in the space provided. B. With your partner, complete the sentences using the words listed below: 独生子女 | 演讲 | 年纪轻轻 | 不足 | 目标 | 材料 | 赶上 | 满足 | 前途 | 加塞儿 | 可不 | 文明 | 舍得. C. Take turns translating the sentences into English. My sample table and key:",
             tables=[T2], examples=[D(z, e) for z, e in K2[:1]] + dlg(K22) + [D(z, e) for z, e in K2[1:]]),
        card("Activity 3 (Listening, Writing, Speaking, and Reading)",
             "A. Listen to two dialogs and match them with the pictures below (A, B and C; three pictures are not included). B. Pair up. Each partner listens to one dialog and writes a summary. Fill in your part of the table below. C. Ask your partner questions about the dialog they hear and fill in the other part of the table. D. Summarize your partner’s dialog. Discuss your summary with your partner. E. Check your summary against the script, then share your summary with the class. (Audio and pictures; the script is not in the book, so there is no key.)",
             tables=[D3]),
        card("Activity 4 (Reading and Speaking)",
             "A. Match the parts in Column A with the parts in Column B by writing the letter in the leftmost column. Share your work with a classmate. B. Pair up and take turns translating the sentences into English. Your partner will translate them back into Chinese without looking at the table. Then go back to the table, check for any errors, and make corrections accordingly. The book’s matching is left blank (and its columns are scrambled in the PDF); the seven completed sentences are my key:",
             examples=[D(z, e) for z, e in A4]),
    ],
    exercises=[
        M("Which word fits “前边那个人，___的，别人排队他却加塞儿”?", "年纪轻轻", ["独生子女", "满足", "演讲"], "年纪轻轻."),
        M("Which word fits “太不___了”, said of someone who cuts in line?", "文明", ["前途", "材料", "目标"], "文明."),
        M("Which word fits “王教授正在为明天的___准备材料”?", "演讲", ["不足", "满足", "舍得"], "演讲."),
        M("Which word fits “他们的能力很强，又有一个很大的___”?", "目标", ["材料", "演讲", "加塞儿"], "目标."),
        M("Which word fits “一个稳定的生活是不大会让他___的”?", "满足", ["赶上", "文明", "演讲"], "满足."),
        M("Which sentence pairs with “她的中文怎么说得那么棒？”?", "她从小就参加中文学校，也经常上网学中文", ["可他已经是大学教授了", "一定会有这样或那样的不足", "也很注意文明礼貌"], "4-f."),
        M("Which sentence pairs with “我弟弟虽然是个九零后，年纪很轻，”?", "可他已经是大学教授了", ["所以你们就应该想得比我们高", "只要有一个稳定的工作就满足了", "也很注意文明礼貌"], "2-e."),
        M("What does 年纪轻轻 describe?", "Being very young", ["Being very old", "Being very tall", "Being very rich"], "年纪轻轻."),
        F("为了理想，他舍___失去得到的一切。", "得", ["了", "过", "着"], "舍得: be willing."),
        F("他们都是独生子女，父母舍得花钱让孩子受很好的教___。", "育", PART, "教育: education."),
    ],
)

# ------------------------------------------------------------------ 3. 那是 and 可不
NS0 = table(["结构", "用法"], [["那是 (colloquial)", "indicates that one agrees with what has been said, similar to “You’re right” or “Absolutely”; often followed by an explanation"]], title="Discourse Grammar: 那是")
NSE = [("A", "在加州现在学中文的人越来越多了。", "1. A: More and more people in California are learning Chinese now."), ("B", "那是，有的地方连小学都有中文课了。", "B: Absolutely; in some places even elementary schools have Chinese classes."),
       ("A", "李琳的女儿真有礼貌。", "2. A: Li Lin’s daughter is really polite."), ("B", "那是，每次看见大人，她老远就问好。", "B: Absolutely; every time she sees an adult she greets them from far away."),
       ("A", "老张唱歌唱得真棒。", "3. A: Lao Zhang sings really well."), ("B", "那是，他一直是合唱队的主要队员。", "B: Absolutely; he has always been a main member of the choir.")]
NS1 = [("A", "这儿的天气真好。", "Activity 1A-1 (my answers to the five exchanges): A: The weather here is really nice."), ("B", "那是，这儿一年四季都不太冷也不太热。", "B: Absolutely; it is neither too cold nor too hot here all year round."),
       ("A", "她的中文字写得真漂亮。", "2. A: Her Chinese characters are written beautifully."), ("B", "那是，她从小就跟奶奶学写毛笔字。", "B: Absolutely; she has learned to write with a brush from her grandmother since childhood."),
       ("A", "你和老马是老朋友了吧？", "3. A: You and Lao Ma are old friends, aren’t you?"), ("B", "那是，我们从小学就是同学。", "B: Absolutely; we have been classmates since elementary school."),
       ("A", "国防语言学院的历史很久了吧？", "4. A: The Defense Language Institute has a long history, doesn’t it?"), ("B", "那是，它是一所很老的学校了。", "B: Absolutely; it is a very old school."),
       ("A", "琳达学中文学得那么好，连她女儿也喜欢学中文。", "5. A: Linda learns Chinese so well that even her daughter likes learning Chinese."), ("B", "那是，她们家里常常说中文。", "B: Absolutely; they often speak Chinese at home.")]
NS2 = [("A", "你的汉堡真好吃！", "Activity 2 (my four exchanges), 1. A: Your burger is really tasty!"), ("B", "那是，这是我自己做的。", "B: Absolutely; I made it myself."),
       ("A", "你们学校的图书馆真大。", "2. A: Your school’s library is really big."), ("B", "那是，有三层楼呢。", "B: Absolutely; it has three floors."),
       ("A", "小王的篮球打得真好。", "3. A: Xiao Wang plays basketball really well."), ("B", "那是，他每天都练习两个小时。", "B: Absolutely; he practices two hours every day."),
       ("A", "这个周末的聚会真有意思。", "4. A: This weekend’s party was really fun."), ("B", "那是，大家都带了好吃的东西来。", "B: Absolutely; everyone brought good food.")]
KB0 = table(["结构", "用法"], [["可不 (colloquial)", "an abbreviation of 可不是吗, used to indicate agreement; English “Absolutely” or “Exactly!”. Like 那是, but 那是 is used in a positive context while 可不 is used in both positive and negative contexts"]], title="Discourse Grammar: 可不")
KBE = [("A", "没想到今天这么冷！", "1. A: I didn’t expect it to be this cold today!"), ("B", "可不，刚才出去散步，差点儿把我冻坏了。", "B: Exactly; I went out for a walk just now and almost froze."),
       ("A", "蒙特雷的风景真漂亮！", "2. A: Monterey’s scenery is really beautiful!"), ("B", "可不，每天都有很多游客来这里玩儿。", "B: Exactly; many tourists come to play here every day."),
       ("A", "大明昨天忙得连午饭也没吃上。", "3. A: Da Ming was so busy yesterday that he didn’t even get lunch."), ("B", "可不，他这几天准备考试，太紧张了。", "B: Exactly; he is preparing for exams these days and is too stressed.")]
KB3 = [("A", "今天下班后开车回家，路上走得慢极了。", "Activity 3A-1 (audio; my answers use the book’s script): A: Driving home after work today, the road was extremely slow."), ("B", "可不，马路上的车太多了，开车还不如骑自行车快。", "B: Exactly; there were too many cars on the road, and driving was not even faster than cycling."),
       ("A", "旧金山的房子怎么那么贵啊？", "2. A: Why are houses in San Francisco so expensive?"), ("B", "可不，我再工作十年，恐怕也买不起一座小房子。", "B: Exactly; even if I work another ten years I probably couldn’t afford a small house."),
       ("A", "今天是个大晴天，太阳特别好。", "3. A: Today is a big sunny day, with especially good sunshine."), ("B", "可不，很多人去公园散步，也有的人在海边晒太阳。", "B: Exactly; many people went for a walk in the park and some sunbathed by the sea."),
       ("A", "王老师在国防语言学院工作了很长时间了吧？", "4. A: Teacher Wang has worked at the Defense Language Institute for a long time, hasn’t she?"), ("B", "可不，她在那儿工作了三十多年了。她来这儿的时候，我还没出生呢。", "B: Exactly; she has worked there for over thirty years. When she came here I wasn’t even born yet.")]
KB4 = [("可不，今天的作业特别多。", "Activity 3C (my situation sentences with the replies): Exactly, there is a lot of homework today. (reply to “今天的作业真多！”)"), ("可不，这个周末我们都没出去玩儿。", "Exactly, none of us went out to play this weekend. (reply to “这个周末天天下雨。”)")]
L3 = lesson(
    "Lesson 28 Presentation 1 grammar: discourse grammar 那是 and 可不",
    "那是 · 可不 · 可不是吗 · 表示同意 · 在加州学中文 · 蒙特雷 · 国防语言学院",
    requires=[],
    cards=[
        card("Discourse Grammar: 那是",
             "In colloquial Chinese, 那是 can be used to indicate that one agrees with what has been said, similar to “You’re right” or “Absolutely” in English. It is often followed by an explanation.",
             tables=[NS0], examples=dlg(NSE)),
        card("Activity 1 (Reading, Writing, and Speaking)",
             "A. Complete the exchanges, beginning with 那是. B. Share your work with a classmate. Take turns translating your exchanges into English. My answers (the book leaves the B lines blank):",
             examples=dlg(NS1)),
        card("Activity 2 (Writing and Speaking)",
             "Create four exchanges, using 那是 wherever appropriate. My four exchanges:",
             examples=dlg(NS2)),
        card("Discourse Grammar: 可不",
             "可不 is an abbreviation of 可不是吗 and is used to indicate agreement in colloquial Chinese. Its English equivalent is “Absolutely” or “Exactly!” 可不 is similar to 那是, but with one difference: 那是 is used in a positive context while 可不 is used in both positive and negative contexts.",
             tables=[KB0], examples=dlg(KBE)),
        card("Activity 3 (Listening, Writing, Speaking, and Reading)",
             "A. Listen to the statements and complete the exchanges using 可不 and the information you hear in each. B. Share your work with a partner. Use the script below to refine your work. C. Write four sentences that describe situations around you. Then pair up, take turns saying a sentence and your partner responds, beginning with 可不. The book prints the script of the four statements (今天下班的时候，马路上的车太多了，开车还不如骑自行车快。旧金山的房子太贵了。我再工作十年，恐怕也买不起一座小房子。今天天气真好，很多人去公园散步，也有的人在海边晒太阳。王老师在国防语言学院工作了三十多年了。她来这儿的时候，我还没出生呢。), so my answers follow it:",
             examples=dlg(KB3) + [D(z, e) for z, e in KB4]),
    ],
    exercises=[
        M("What does 那是 express in conversation?", "Agreement (“Absolutely”)", ["Refusal", "A question", "Thanks"], "那是: agree."),
        M("What usually follows 那是?", "An explanation", ["A question", "A refusal", "A number"], "Often followed by an explanation."),
        M("What is 可不 short for?", "可不是吗", ["可不可以", "可不要", "不可以"], "可不 = 可不是吗."),
        M("What is the difference between 那是 and 可不?", "那是 is for positive contexts; 可不 is for both positive and negative", ["可不 is for positive only", "They are exactly the same", "那是 is for negative only"], "The difference."),
        M("Which reply fits “没想到今天这么冷！”?", "可不，刚才出去散步，差点儿把我冻坏了", ["那是，今天太热了", "不对，我很热", "我不知道"], "可不."),
        M("Which reply fits “老张唱歌唱得真棒。”?", "那是，他一直是合唱队的主要队员", ["可不，他不会唱歌", "我没有时间", "他是医生"], "那是."),
        M("Which fits a negative situation: “今天下班后开车回家，路上走得慢极了。”?", "可不，马路上的车太多了", ["那是，今天天气真好", "那是，路很空", "我喜欢游泳"], "可不: negative context."),
        F("A：蒙特雷的风景真漂亮！B：___，每天都有很多游客来这里玩儿。", "可不", ["不是", "没有", "好的"], "可不."),
        F("A：李琳的女儿真有礼貌。B：那___，每次看见大人，她老远就问好。", "是", PART, "那是."),
    ],
)

# ------------------------------------------------------------------ 4. 说了, 可…了, 注意到
SL0 = table(["结构", "用法"], [["Speaker + 说了，quotation", "in daily conversation, 说了 indicates a quotation, like “… has already said” in English, and it often implies that the quoted words carry weight"]], title="Discourse Grammar: 说了")
SLE = [("班长刚才说了，星期五中午我们要搞聚会，家人和朋友也可以参加。", "1. The class monitor just said that on Friday noon we are going to have a party, and family and friends can also take part."), ("妈妈说了，不做完作业我就不能玩儿游戏。", "2. Mom said I can’t play games if I don’t finish my homework."), ("电视上说了，明天会刮大风，下午有中到大雨。", "3. The TV said there will be strong wind tomorrow and moderate to heavy rain in the afternoon."),
       ("李老师说了，下星期二有单元考试，我们得好好准备。", "4. Teacher Li said there is a unit test next Tuesday and we have to prepare well."), ("医生说了，甜的和咸的东西吃多了对身体都不好。", "5. The doctor said that eating too much sweet and salty food is bad for the body.")]
SLS = [("太太", "女儿刚刚发来短信，说她坐今天夜里从旧金山坐飞机，明天晚上到北京。", "Wife: Our daughter just sent a text saying she is taking a flight from San Francisco tonight and arrives in Beijing tomorrow evening. (the script of Activity 4A; translations mine)"),
       ("先生", "太好了，那她应该能在家过年了。她哪天到青岛？", "Husband: Great, then she should be able to spend the New Year at home. What day does she get to Qingdao?"),
       ("太太", "她可能不过来了，说要去开一个重要的会，三天后就飞回美国。", "Wife: She may not come over; she said she has to go to an important meeting and will fly back to the U.S. three days later."),
       ("先生", "为什么这么急？", "Husband: Why such a hurry?"),
       ("太太", "她说她的公司做的应用软件，马上就要完成了，这段时间非常忙。", "Wife: She said the app her company is making is about to be finished and she is very busy at this time."),
       ("先生", "那，要不要咱们去北京看看她？", "Husband: Then, shall we go to Beijing to see her?"),
       ("太太", "别了。她说她现在连睡觉的时间都没有，哪有时间陪咱们。", "Wife: Don’t. She said she doesn’t even have time to sleep now, so how could she have time for us."),
       ("先生", "好吧，过段时间再说。", "Husband: All right, let’s see after a while."),
       ("太太", "她说等到夏天就有空儿了，一定回来看咱们。", "Wife: She said she will be free by summer and will definitely come back to see us.")]
SLK = [("女儿来短信说了，她坐今天夜里从旧金山的飞机，明天晚上到北京。", "Activity 4A, 1 (my reading of the printed script; the audio may divide the sentences differently): The daughter said in her text that she is flying from San Francisco tonight and arrives in Beijing tomorrow evening."),
       ("她说了，她要去开一个重要的会，三天后就飞回美国。", "2: She said she has to go to an important meeting and will fly back to the U.S. three days later."), ("她还说了，她的公司做的应用软件，马上就要完成了。", "3: She also said the app her company is making is about to be finished."),
       ("女儿说了，她这段时间非常忙，现在连睡觉的时间都没有。", "4: The daughter said she is very busy at this time and doesn’t even have time to sleep."), ("她说了，她哪有时间陪我们。", "5: She said she has no time to keep us company."), ("她又说了，等到夏天就有空儿了，一定回来看我们。", "6: She said again that she will be free by summer and will definitely come back to see us.")]
SL5 = [("妈妈说了，做事情要认真，不能只想着玩儿。", "Activity 5 (my five, 1): Mom said: do things seriously, don’t think only about playing."), ("爷爷说了，早睡早起身体好。", "2: Grandpa said: going to bed early and getting up early is good for your health."), ("老师说了，每天都要复习当天学的东西。", "3: The teacher said you must review what you learned every day."), ("朋友说了，有困难一定告诉他。", "4: My friend said: if I have difficulties I must tell him."), ("爸爸说了，学习外语一定要多说多听。", "5: Dad said: to learn a foreign language you must speak and listen a lot.")]
KL0 = table(["结构", "用法"], [["可 + adjective/verb phrase + 了", "used for emphasis in colloquial Chinese; similar to “very” or “so” in English; the element between 可 and 了 is usually an adjective or verb phrase"]], title="The 可……了 Construction")
KLE = [("昨天我们看的那个电影可好了。", "1. The film we saw yesterday was so good."), ("你妈妈看上去可年轻了。", "2. Your mother looks so young."), ("高铁跑得可快了，从北京到上海不到一天就到了。", "3. High-speed trains run so fast; from Beijing to Shanghai you arrive in less than a day."), ("下完雨以后我出去散了一会儿步，可舒服了。", "4. After the rain I went out for a short walk, and it was so comfortable."), ("她没去过中国，但她可喜欢中国了。", "5. She has never been to China, but she likes China so much.")]
KL6 = [("徐丽的女儿可爱说英语了，见到外国朋友就和人家聊天。", "Activity 6A-1 (my rewrites): Xu Li’s daughter loves speaking English so much; whenever she meets foreign friends she chats with them."), ("从这里去邮局可远了，走路要四十分钟。", "2: It’s so far from here to the post office; it takes forty minutes on foot."), ("我以前的房间可小了，只能放下一张床和一把椅子。", "3: My former room was so small, it could hold only a bed and a chair."),
       ("我们的西瓜可甜了，快买一个尝尝吧。", "4: Our watermelons are so sweet; buy one and try it."), ("那家饭馆的烤鸭做得可好吃了。", "5: That restaurant’s roast duck is so delicious."), ("她一边走路一边看手机，走得可慢了。", "7: She looks at her phone while walking and walks so slowly.")]
KL66 = [("A", "那本书你觉得怎么样？", "6: A: What do you think of that book?"), ("B", "写得可好了，你也借来看看吧。", "B: It’s written so well; borrow it and read it too.")]
ZY0 = table(["表达", "用法"], [["注意到", "“having noticed/observed”; different from 注意, “paying attention to”: 注意天气的变化 means “to pay attention to the change in weather” while 注意到天气的变化 means “to have noticed a change in the weather”"], ["你注意到没有？", "sometimes used as a reminder, such as 你注意到没有？最近你锻炼得越来越少了。"]], title="The Expression 注意到")
ZYE = [("你注意到小张今天的样子了吗？他好像不太舒服。", "1. Have you noticed how Xiao Zhang looks today? He doesn’t seem very well."), ("她注意到，这儿的冬天比她老家冷多了。", "2. She noticed that the winter here is much colder than in her hometown."), ("我注意到新课表已经把说话课改到上午了。", "3. I have noticed that the new schedule has changed the speaking class to the morning."),
       ("注意到了吧？这次说话考试你考得比上次好很多。", "4. Did you notice? You did much better on this speaking test than last time."), ("这个字你写得不对，注意到就好了。下次要写对。", "5. You wrote this character wrong; it’s good that you noticed. Write it correctly next time.")]
ZY7 = [("你注意到他的新车了吗？就停在我们楼的前面。", "Activity 7A-1 (the book’s suggested answer): Have you noticed his new car? It is parked in front of our building."), ("我注意到，越来越多的人开始锻炼身体了。", "7A-2: I have noticed that more and more people have started to exercise."), ("这个词你的发音不对。你注意到了吗？", "7A-3: Your pronunciation of this word is incorrect. Have you noticed that?"),
       ("我们注意到，这儿的人对外地人非常好。", "7A-4: We have noticed that people here are very nice to outsiders."), ("他没注意到这里的房租特别贵。", "7A-5: He did not notice that rent here is especially expensive."), ("我已经注意到我作业里做错的地方了。", "7A-6: I have already noticed the mistakes in my homework.")]
L4 = lesson(
    "Lesson 28 Presentation 1 grammar: 说了, the 可……了 construction and 注意到",
    "说了 · 可……了 · 注意到 · 班长说了 · 妈妈说了 · 可好了 · 注意到没有",
    requires=[],
    cards=[
        card("Discourse Grammar: 说了",
             "In daily conversation, 说了 indicates a quotation, like “… has already said” in English, and it often implies that the quoted words carry weight.",
             tables=[SL0], examples=[D(z, e) for z, e in SLE]),
        card("Activity 4 (Listening, Writing, Speaking, and Reading)",
             "A. Listen to the dialog and complete the sentences you hear (six sentences beginning 女儿来短信说了, 她说了, 她还说了, 女儿说了, 她说了, 她又说了). B. Share your work with a classmate. Then, using the script below, take turns translating the sentences into English. The script, then my completed sentences:",
             examples=dlg(SLS) + [D(z, e) for z, e in SLK]),
        card("Activity 5 (Writing and Speaking)",
             "List five things your family members or people close to you have said that you found helpful. Use 说了 wherever appropriate. My five:",
             examples=[D(z, e) for z, e in SL5]),
        card("The 可……了 Construction",
             "This construction is used for emphasis in colloquial Chinese. It is similar to “very” or “so” in English, and the element between 可 and 了 is usually an adjective or verb phrase.",
             tables=[KL0], examples=[D(z, e) for z, e in KLE]),
        card("Activity 6 (Reading, Writing, and Speaking)",
             "A. Pair up and with your partner, use the 可……了 construction to rewrite the following sentences: 1. 徐丽的女儿特爱说英语，见到外国朋友就和人家聊天。 2. 从这里去邮局远得很，走路要四十分钟。 3. 我以前的房间非常小，只能放下一张床和一把椅子。 4. 我们的西瓜特别甜，快买一个尝尝吧。 5. 那家饭馆的烤鸭做得好吃极了。 6. A：那本书你觉得怎么样？B：写得非常好，你也借来看看吧。 7. 她一边走路一边看手机，走得非常慢。 B. Take turns translating each sentence into English, and then back into Chinese. My rewrites:",
             examples=[D(z, e) for z, e in KL6[:5]] + dlg(KL66) + [D(z, e) for z, e in KL6[5:]]),
        card("The Expression 注意到",
             "注意到 means “having noticed/observed.” 注意到 is different from 注意, as the latter means “paying attention to.” For example, 注意天气的变化 means “to pay attention to the change in weather” while 注意到天气的变化 means “to have noticed a change in the weather.” Sometimes 注意到 is used as a reminder, such as: 你注意到没有？最近你锻炼得越来越少了。",
             tables=[ZY0], examples=[D(z, e) for z, e in ZYE]),
        card("Activity 7 (Writing, Speaking, and Reading)",
             "A. Translate the following sentences into Chinese: 1. Have you noticed his new car? It is parked in front of our building. 2. I have noticed that more and more people have started to exercise. 3. Your pronunciation of this word is incorrect. Have you noticed that? 4. We have noticed that people here are very nice to outsiders. 5. He did not notice that rent here is especially expensive. 6. I have already noticed the mistakes in my homework. B. Check your work with a classmate. Refine your work using the suggested answer keys below:",
             examples=[D(z, e) for z, e in ZY7]),
    ],
    exercises=[
        M("What does 班长刚才说了 signal?", "A quotation that carries weight", ["A question", "A refusal", "A greeting"], "说了."),
        M("What does 妈妈说了，不做完作业我就不能玩儿游戏 mean?", "Mom said I can’t play games if I don’t finish my homework", ["Mom played games", "Mom finished homework", "Mom asked a question"], "说了."),
        M("What does the 可……了 construction add?", "Emphasis, like “very” or “so”", ["Past tense", "A question", "A negative"], "可…了."),
        M("What does 你妈妈看上去可年轻了 mean?", "Your mother looks so young", ["Your mother is very old", "Your mother is young at heart only", "Your mother is a teacher"], "可…了."),
        M("What is the difference between 注意 and 注意到?", "注意 is paying attention to; 注意到 is having noticed", ["They are the same", "注意到 is a question", "注意 means forget"], "注意到: have noticed."),
        M("What does 注意到天气的变化 mean?", "To have noticed a change in the weather", ["To pay attention to the weather", "To change the weather", "To forget the weather"], "注意到."),
        M("What does 你注意到没有？ often do?", "Remind the listener of something", ["End the conversation", "Say goodbye", "Give thanks"], "Reminder."),
        M("Which is the correct 可……了 rewrite of 那家饭馆的烤鸭做得好吃极了?", "那家饭馆的烤鸭做得可好吃了", ["那家饭馆的烤鸭可做得好吃", "那家饭馆可的烤鸭好吃了", "那家饭馆的烤鸭做得好吃可了"], "可好吃了."),
        F("医生___了，甜的和咸的东西吃多了对身体都不好。", "说", PART, "说了."),
        F("下完雨以后我出去散了一会儿步，可舒服___。", "了", ["吗", "呢", "吧"], "可…了."),
        F("我___意到新课表已经把说话课改到上午了。", "注", PART, "注意到."),
    ],
)

# ------------------------------------------------------------------ 5. adverbs of degree
AD0 = table(["Adverb", "Meaning", "Example"], [["极", "Extremely", "他唱歌唱得极好 – he sings extremely well"], ["最", "Most", "他唱歌唱得最好 – he sings the best among …"], ["特别", "Especially", "他唱歌唱得特别好 – he sings especially well"], ["非常", "Very", "他唱歌唱得非常好 – he sings very well"], ["十分", "Very", "他唱歌唱得十分好 – he sings very well"], ["很", "Very", "他唱歌唱得很好 – he sings very well (a little weaker than 非常 and 十分)"], ["相当", "Considerably", "他唱歌唱得相当好 – he sings considerably well (it can be stronger than 很 depending on the way it is said)"], ["挺", "Quite", "他唱歌唱得挺好 – he sings quite well"], ["稍微", "A little bit", "他唱歌唱得稍微好一点儿 – he sings a little better (still not very good)"], ["有点儿 (usually negative)", "A little bit", "他唱歌唱得有点儿不好听 – he sings a little bit poorly"]], title="Adverbs of Degree (from the strongest to the least strong)")
AD8 = [("昨天我们看了一场电影，那个电影非常好。", "Activity 8, 1 (the book’s suggested answer; 特别, 十分, 很, 相当 or 挺 also work; the original wrongly used 最): Yesterday we saw a film, and it was very good."), ("这儿的天气比我们老家稍微好一些。", "2 (the original wrongly used 相当 with 比): The weather here is a little better than in our hometown."), ("今天是个大阴天。", "3 (the original said 很大的阴天): Today is a big overcast day."),
       ("他走得极快，我怎么走也赶不上他。", "4 (特别, 十分, 很 or 相当 also work; the original said 稍快): He walks extremely fast and no matter how I walk I can’t catch up with him."), ("这一代青年人个个优秀，大有希望。", "5 (the original said 挺有希望): Every one of this generation of young people is excellent and has great promise."), ("我弟弟最不喜欢吃的菜就是鱼，一看见鱼他就头疼。", "6 (the original said 相当不喜欢): The dish my younger brother dislikes most is fish; as soon as he sees fish he gets a headache.")]
AD9 = [("极平稳 · 非常舒适 · 很有道理 · 相当厉害 · 有点儿饿", "Activity 9, Group 1 (my phrases): extremely stable; very comfortable; very reasonable; considerably formidable; a little hungry."), ("特别有礼貌 · 十分重要 · 相当严重 · 挺顺利 · 非常真实", "Group 2: especially polite; very important; considerably serious; quite smooth; very real."), ("十分美好 · 极便利 · 相当精确 · 挺准时 · 有点儿辛苦", "Group 3: very beautiful; extremely convenient; considerably precise; quite punctual; a little hard-worked.")]
L5 = lesson(
    "Lesson 28 Presentation 1 grammar: adverbs of degree",
    "极 · 最 · 特别 · 非常 · 十分 · 很 · 相当 · 挺 · 稍微 · 有点儿 · 大有前途 · 大晴天",
    requires=[],
    cards=[
        card("Adverbs of Degree",
             "Adverbs of degree are about degree of intensity and are usually used to modify adjectives and, occasionally, verbs. The table below lists the most-often used adverbs of degree, from the strongest to the least strong. 大 can be used as an adverb of degree, and it usually appears in set phrases such as 形势大好, 大红大绿, 大有前途 and 大好时光. Another common pattern for 大 to be used as an adverb of degree is 大 + monosyllable adjective + noun, such as 大晴天 and 大好人.",
             tables=[AD0]),
        card("Activity 8 (Reading, Writing, and Speaking)",
             "A. Identify the incorrect uses of adverbs of degree in the following sentences, and make corrections as needed: 1. 昨天我们看了一场电影，那个电影最好。 2. 这儿的天气比我们老家相当好一些。 3. 今天是个很大的阴天。 4. 他走得稍快，我怎么走也赶不上他。 5. 这一代青年人个个优秀，挺有希望。 6. 我弟弟相当不喜欢吃的菜就是鱼，一看见鱼他就头疼。 B. Share your work with a classmate. Go over the suggested answer key below and refine your work if necessary. Then translate each sentence into English. The book’s suggested answers:",
             examples=[D(z, e) for z, e in AD8]),
        card("Activity 9 (Reading and Speaking)",
             "A. Form groups of three. Each group takes five adjectives from below and creates five phrases using any of the adverbs discussed in Activity 8. For example: 极有礼貌 | 非常有道理 | 有点儿饿. Group 1: 平稳, 舒适, 有道理, 厉害, 饿. Group 2: 有礼貌, 重要, 严重, 顺利, 真实. Group 3: 美好, 便利, 精确, 准时, 辛苦. B. Take turns in your group, using an adjective and an adverb to compose a sentence. When you’re done, select the three best sentences and share them with the class. My phrases:",
             examples=[D(z, e) for z, e in AD9]),
    ],
    exercises=[
        M("Which adverb of degree is the strongest in the book’s list?", "极", ["稍微", "挺", "有点儿"], "From strongest: 极."),
        M("Which adverb means “most”?", "最", ["极", "挺", "稍微"], "最: most."),
        M("Which is the least strong in the list?", "有点儿 (usually negative)", ["极", "非常", "特别"], "Least strong."),
        M("What does 稍微 mean?", "A little bit", ["Extremely", "Most", "Especially"], "稍微."),
        M("What does 大有前途 show about 大?", "大 can be an adverb of degree", ["大 means big only", "大 is a noun", "大 is a question word"], "大 as adverb of degree."),
        M("Which is a 大 + monosyllable adjective + noun phrase?", "大晴天", ["大有前途", "形势大好", "大红大绿"], "大晴天."),
        M("Why is 这儿的天气比我们老家相当好一些 wrong?", "相当 cannot be used with a 比 comparison like this; use 稍微", ["Because 好 is wrong", "Because 这儿 is wrong", "Because 一些 is wrong"], "稍微 is the fix."),
        M("Which is the correct fix for 我弟弟相当不喜欢吃的菜就是鱼?", "我弟弟最不喜欢吃的菜就是鱼", ["我弟弟稍微不喜欢吃的菜就是鱼", "我弟弟有点儿喜欢吃的菜就是鱼", "我弟弟吃的菜就是鱼最"], "最不喜欢."),
        F("今天是个___阴天。", "大", PART, "大阴天."),
        F("这一代青年人个个优秀，大有希___。", "望", PART, "大有希望."),
    ],
)

UNIT = unit("第二十八课 Presentation 1: 年轻的一代, 那是, 可不, 说了, 可…了, 注意到, 程度副词", [L1, L2, L3, L4, L5])
