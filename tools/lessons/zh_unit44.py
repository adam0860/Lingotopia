"""Unit 44: Lesson 15 (Social Gathering) Presentation 3 and Area Studies from the book's texts: the Independence Day picnic, the
有的…有的… and 起来 notes, the V来V去 and 不…不… constructions, the adverbial marker 地, the aspect particle 着, (一)直到…才…, the
skill-integration and using-Chinese activities, the vocabulary list and the Invitations and Parties reading. Audio, pictures and
photo credits are not included; the book writes numbers as digits and they are spelled out here; answer keys the book does not
print (and blanks it leaves for the student) are mine and labeled."""
from zh_auto import *
from zh_l15_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("要数", 1, "shu3"), ("干活", 0, "gan4"), ("长得", 0, "zhang3"), ("没收到", 0, "mei2"), ("睡觉", 1, "jiao4"), ("得做", 0, "dei3"), ("市长", 1, "zhang3"), ("饺子和面条", 2, "he2"), ("坐着边", 1, "zhe5"), ("还给大家", 0, "hai2"), ("种着", 0, "zhong4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0 and zh[j - 1] not in "当草土天各山场内本外基实陆" and (j + 1 >= len(zh) or zh[j + 1] not in "道址方铁图球区点上下面理"):
            f[j] = "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the picnic
PIC = ("七月四号是独立日，大卫约了几家朋友到公园烧烤。那天的天气特别好，没有风，不冷也不热。公园里人很多，有的躺在草地上晒太阳，有的沿着小路骑自行车，还有的坐在长椅上看风景。下午一点，大家都到了。大卫准备了汉堡和热狗，琳达带来了餐具和甜点，麦克买了饮料和水果。"
       "大家一放下东西就忙起来。爸爸们烤肉，妈妈们切水果，大家一边干活，一边聊天。聚会上玩得最开心的要数孩子们了，他们高兴地在草地上跑来跑去，又笑又叫。肉烤好了，孩子们也饿了，大家围坐一起吃起来。琳达烤的苹果派最受欢迎，大家都说没吃够。饭吃完了，爸爸们又带着孩子们踢球，而妈妈们忙着收拾垃圾。大家一直玩到天黑才回家。")
PIC_E = ("July 4th is Independence Day, and David invited several families of friends to the park for a barbecue. The weather that day was especially good: no wind, neither cold nor hot. There were many people in the park; some lay on the grass sunbathing, some rode bicycles along the trail, and others sat on long benches looking at the scenery. At one in the afternoon everyone had arrived. David prepared hamburgers and hot dogs, Linda brought tableware and desserts, and Mike bought drinks and fruit. As soon as everyone put their things down they got busy. The dads grilled meat, the moms cut fruit, and everyone chatted while working. The happiest at the gathering were the children, who ran around on the lawn happily, laughing and shouting. When the meat was grilled and the children were hungry, everyone sat in a circle and began to eat. Linda’s apple pie was the most popular; everyone said they hadn’t had enough. When the meal was over, the dads took the kids to play soccer while the moms were busy tidying up the trash. Everyone played until dark before going home.")
NT1 = [("他们有的看书，有的做作业。", "They: some read, some do homework."), ("海滩上有很多人，有的站着，有的坐着，有的躺着。", "There are many people on the beach; some stand, some sit, some lie down."), ("站起来", "stand up"), ("忙起来", "get busy"), ("吃起来", "start eating"), ("好起来", "get better"), ("热起来", "get hot"), ("看起来", "it seems; it looks like (Lesson 10-2)"), ("想起来", "just come to mind (Lesson 15-1)")]
M3 = [("1. 他一边打电话", "d. 一边走来走去。", "He talked on the phone while walking back and forth."), ("2. 昨天，他们在老王家聊天", "e. 一直聊到晚上十点半。", "Yesterday they chatted at Lao Wang’s home until ten thirty at night."), ("3. 我们新租的公寓", "a. 不大不小，很合适。", "The apartment we newly rented is neither big nor small, very suitable."),
      ("4. 吃完烤肉以后，孩子们开心地", "f. 在草地上跑来跑去。", "After the barbecue the children ran around on the lawn happily."), ("5. 大家有的烤肉，", "c. 有的准备甜点，有的切水果。", "Some grilled meat, some prepared dessert, some cut fruit."), ("6. 在今天的聚会上，最不开心的", "b. 要数小李，因为他的工作刚没了。", "At today’s party the unhappiest was Xiao Li, because he had just lost his job.")]
L1 = lesson(
    "Lesson 15 Presentation 3: the Independence Day picnic",
    "七月四号是独立日 · 有的…有的… · 起来 · 一直玩到天黑才回家",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: a barbecue, kids and bikes (not included). Pair up and discuss: A. How do you usually celebrate Independence Day? B. What foods would you usually eat at a picnic on this holiday? C. What recreational activities do people enjoy, in addition to having a BBQ?"),
        card("Presentation 3: 公园烧烤",
             "The book also prints the passage in traditional characters. Notes: 1. The 有的…有的… construction: 有的 can be used multiple times in a sentence to indicate different groups engaged in various actions or states. 2. The use of 起来: as a directional complement 起来 indicates upward movement, like the English adverb “up” as in 站起来. In addition, 起来 is often used to indicate the start of an action, such as 忙起来 and 吃起来 in the Presentation above. It can also indicate the start of a state such as 好起来 and 热起来. Idiomatic expressions are also used in the form of the verb + 起来: 看起来 (Lesson 10-2) means “it seems” or “it looks like,” and 想起来 (Lesson 15-1) means “just come to mind.”",
             examples=[D(PIC, PIC_E)] + [D(z, e) for z, e in NT1]),
        card("Activities 1 and 2",
             "Activity 1 (Listening and Speaking). A. Global listening: 1. Why did David and his friends get together on that day? 2. Who worked hard for the gathering and who were the happiest? B. Detailed listening: 1. What was the weather like that day? 2. What were things like in the park? 3. What did David and Linda bring to the picnic? 4. What did the kids do? (Audio, not included. From the text, mine: Independence Day, to barbecue in the park; the dads grilled, the moms cut fruit, the children were the happiest; no wind, neither cold nor hot; many people lying on the grass, cycling on the trail, sitting on benches; David brought hamburgers and hot dogs, Linda tableware and dessert; they ran around on the lawn, laughing and shouting, then played soccer.) Activity 2 (Writing and Speaking). Pair up and fill in the table with the expressions you’ve just learned (rows: Weather; Activities in the park; BBQ; Doing something in a certain manner; Doing something back and forth; Those who were the busiest…; Some people doing A and some doing B; Something not happening until a certain time). The book leaves the cells empty; my answers (mine):",
             examples=[D("没有风，不冷也不热", "Weather: no wind, neither cold nor hot"), D("躺在草地上晒太阳，沿着小路骑自行车，坐在长椅上看风景", "Activities in the park"), D("烤肉，烧烤，汉堡和热狗，苹果派", "BBQ"), D("高兴地在草地上跑", "Doing something in a certain manner"), D("跑来跑去", "Doing something back and forth"),
                       D("要数孩子们", "Those who were the happiest…: it was the children"), D("有的躺在草地上，有的骑自行车", "Some people doing A and some doing B"), D("一直玩到天黑才回家", "Something not happening until a certain time")]),
        card("Activity 3 (Reading and Speaking)",
             "A. Match the phrases in Column A with those in Column B by writing the letters in the leftmost column. B. Pair up, compare, and take turns asking each other questions about each of the sentences. The book leaves the key out; my matches (mine): 1-d, 2-e, 3-a, 4-f, 5-c, 6-b.",
             examples=[D(a[3:] + b[3:], e) for a, b, e in M3]),
        card("Activities 4 and 5",
             "Activity 4 (Listening, Reading, and Speaking). A. Listen to a dialog and answer in English. New words: 羊肉串 (yángròu chuàn; kebab), 家长 (jiāzhǎng; parents). 1. Where and when did the gathering take place and who were the participants? 2. Why didn’t Xiao Zhang join them? 3. What did those at the gathering do after the meal? 4. What did Lao Li and his wife do? B. Pair up; take turns translating the underlined sentences into English. (Audio, not included.) Activity 5 (Reading, Speaking, and Reading). A. Pair up. Put the following sentences in order to create a logical passage; consult your dictionary if necessary. The seven sentences in the book’s order (a to g):",
             examples=[D("大家有的在草地上散步，有的沿小路骑自行车。", "a. Some of us strolled on the lawn, some rode bicycles along the trail."), D("客人们在我们家一直玩到下午四点多才离开。", "b. The guests played at our home until after four in the afternoon before they left."), D("我们准备了很多吃的东西，比如烤火鸡、南瓜饼、红薯。", "c. We prepared lots of food, such as roast turkey, pumpkin pie and sweet potatoes."), D("上个星期四是感恩节，我们请了几位朋友来和我们一起过节。", "d. Last Thursday was Thanksgiving, and we invited several friends to celebrate with us."),
                       D("在那儿玩儿了两个小时以后，大家又回到我们家，坐着边喝茶边聊天。", "e. After playing there for two hours, everyone came back to our home and sat chatting while drinking tea."), D("那天气很好，风不大，午饭以后我们去了公园。", "f. The weather was good that day, the wind was light; after lunch we went to the park."), D("我们也买了很多甜点、水果和饮料。", "g. We also bought lots of desserts, fruit and drinks.")]),
        card("Activity 5 sentence order (mine)",
             "The book leaves the order blank; my order is d, c, g, f, a, e, b (Thanksgiving; the food prepared; also bought desserts, fruit and drinks; the good weather and going to the park; activities in the park; back home with tea; the guests leave after four). B. Report your answer to the class."),
    ],
    exercises=[
        M("What holiday is July 4th?", "Independence Day", ["Thanksgiving", "New Year’s Day", "Labor Day"], "七月四号是独立日。"),
        M("What was the weather like?", "No wind, neither cold nor hot", ["Windy and cold", "Rainy", "Very hot"], "没有风，不冷也不热。"),
        M("What did David prepare?", "Hamburgers and hot dogs", ["Apple pie", "Drinks", "Fruit"], "大卫准备了汉堡和热狗。"),
        M("What did Linda bring?", "Tableware and dessert", ["Drinks and fruit", "Hamburgers", "Soccer balls"], "琳达带来了餐具和甜点。"),
        M("What did Mike buy?", "Drinks and fruit", ["Hot dogs", "Dessert", "Tableware"], "麦克买了饮料和水果。"),
        M("Who played the happiest?", "The children", ["The dads", "The moms", "The teachers"], "玩得最开心的要数孩子们了。"),
        M("Whose dish was the most popular?", "Linda’s apple pie", ["David’s hamburgers", "Mike’s fruit", "The hot dogs"], "琳达烤的苹果派最受欢迎。"),
        M("What did the dads do after the meal?", "Took the kids to play soccer", ["Cleaned up the trash", "Cut the fruit", "Went home"], "爸爸们又带着孩子们踢球。"),
        M("What did the moms do after the meal?", "Were busy tidying up the trash", ["Played soccer", "Grilled meat", "Rode bicycles"], "妈妈们忙着收拾垃圾。"),
        M("When did they go home?", "After it got dark", ["At noon", "At one", "Before the meal"], "一直玩到天黑才回家。"),
        M("What does 看起来 mean?", "It seems; it looks like", ["Look up", "Stop looking", "Look back"], "看起来 (Lesson 10-2)."),
        M("What does 想起来 mean?", "Just come to mind", ["Get up", "Think hard", "Stop thinking"], "想起来 (Lesson 15-1)."),
        F("大家一放下东西就忙起___。", "来", PART, "忙起来: get busy."),
        F("有的躺在草地上，有的沿着小路骑自行车，还___的坐在长椅上看风景。", "有", PART, "有的…有的…还有的…"),
    ],
)

# ------------------------------------------------------------------ 2. V来V去
LQ = [("很多鸟在天上飞来飞去。", "Many birds fly back and forth in the sky."), ("他看来看去，都看不出那位医生写了什么。", "He looked this way and that, but could not make out what the doctor had written."), ("我不喜欢靠过道的座位，因为总有人在旁边走来走去。", "I don’t like aisle seats, because there are always people walking back and forth next to them."),
      ("他把沙发搬来搬去，也没找到合适的地方。", "He moved the sofa around, but still didn’t find a suitable place."), ("这件事他想来想去，不知道应该怎么办。", "He thought it over and over, and didn’t know what to do.")]
LQ1 = [("爸爸做了很多菜，她尝来尝去，还是觉得烤鸭最好吃。", "Dad made many dishes; she tasted this and that, and still felt the roast duck was the best. (mine)"), ("早上很多人在公园里走来走去。", "In the morning many people walk back and forth in the park. (mine)"), ("这句话我听来听去，还是听不懂。", "I listened to this sentence over and over and still couldn’t understand it. (mine)"),
       ("我在公共汽车站等来等去，还是没有车过来。", "I waited at the bus stop for a long time and still no bus came. (mine)"), ("这些肉他烤来烤去。因为烤得时间太长，已经不好吃了。", "He grilled this meat over and over. Because it was grilled for too long, it’s no longer tasty. (mine)")]
L2 = lesson(
    "Lesson 15 Presentation 3 grammar: the V + 来 + V + 去 construction",
    "飞来飞去 · 挑来选去 · 走来走去 · 想来想去",
    requires=[],
    cards=[
        card("The V + 来 + V + 去 construction",
             "This construction indicates that an action happens repeatedly or moves back and forth. It is generally used with two verbs that are either identical or synonymous, for example 飞来飞去 and 挑来选去. Subject + V + 来 + V + 去. (Note: if the verb has an object, the object is usually at the beginning of the sentence.)",
             examples=[D(z, e) for z, e in LQ]),
        card("Activity 1 (Writing and Speaking)",
             "Work in pairs to rewrite the following sentences using the V + 来 + V + 去 construction. The originals: 爸爸做了很多菜，她尝尝这个，又尝尝那个，还是觉得烤鸭最好吃。 早上很多人在公园里来回走路。 这句话我听了一遍又一遍，还是听不懂。 我在公共汽车站等了很长时间，还是没有车过来。 这些肉他烤了又烤。因为烤得时间太长，已经不好吃了。 The book leaves the rewritten column empty; my rewrites (mine):",
             examples=[D(z, e) for z, e in LQ1]),
    ],
    exercises=[
        M("What does V + 来 + V + 去 indicate?", "An action repeated or back and forth", ["A finished action", "A future plan", "A negative"], "Repeatedly or back and forth."),
        M("What does 飞来飞去 mean?", "Fly back and forth", ["Fly away", "Fly high", "Stop flying"], "飞来飞去."),
        M("What does 走来走去 mean?", "Walk back and forth", ["Walk home", "Walk fast", "Stop walking"], "走来走去."),
        M("What does 想来想去 suggest?", "Thinking something over and over", ["Not thinking", "Quickly deciding", "Forgetting"], "想来想去."),
        M("Where does the object usually go?", "At the beginning of the sentence", ["After 去", "After 来", "Between 来 and 去"], "The object is usually fronted."),
        M("What does 他把沙发搬来搬去 mean?", "He moved the sofa around", ["He bought a sofa", "He sold the sofa", "He sat on the sofa"], "搬来搬去."),
        M("What does 他看来看去，都看不出 mean?", "He looked over and over but couldn’t make it out", ["He didn’t look", "He saw clearly", "He closed his eyes"], "看来看去."),
        F("很多鸟在天上飞来飞___。", "去", PART, "飞来飞去."),
        F("这件事他想来想去，不知道应该怎么___。", "办", PART, "怎么办."),
    ],
)

# ------------------------------------------------------------------ 3. 不…不…
BB = [("这部电影不长不短。", "This movie is neither long nor short."), ("这个房子不大不小。", "This house is neither big nor small."), ("他是一个做事不急不慢的人。", "He is a person who does things neither hurriedly nor slowly."), ("爸爸给他买了一张不高不矮的书桌。", "Dad bought him a desk that is neither tall nor short."), ("小李说话不快不慢。", "Xiao Li speaks neither fast nor slow."), ("老王不言不语地看着电视。", "Lao Wang watched TV without saying a word.")]
BB3 = ("小李的女朋友王丽今年二十四岁，长得不高不矮，不胖不瘦，说话的时候总是笑。今天小李和她去看了一场电影。他们约好三点半在电影院门口见面，可是小李三点就在电影院门口等。王丽呢，不早不晚三点半到那儿。看完电影，小李带王丽去一家不大不小的饭馆吃晚饭。那儿的菜虽然有点儿咸，但味道不错。他们点了四个菜，花了不多不少八十元钱。吃完饭，他们又到了海边，不快不慢地散了一会儿步。然后，小李送王丽回到她那套不大不小离海边不远不近的公寓。")
BB3_E = ("Xiao Li’s girlfriend Wang Li is twenty-four this year; she is neither tall nor short, neither fat nor thin, and always smiles when she talks. Today Xiao Li and she went to see a movie. They had agreed to meet at the movie theater entrance at three thirty, but Xiao Li was already waiting there at three. Wang Li arrived there neither early nor late, at three thirty. After the movie, Xiao Li took Wang Li to a restaurant that was neither big nor small for dinner. Although the food there was a bit salty, the taste was good. They ordered four dishes, which cost exactly eighty yuan. After eating they went to the seaside and took a walk neither fast nor slow. Then Xiao Li took Wang Li back to her apartment, which is neither big nor small and neither far nor near the sea.")
BB4 = [("他不高不矮，不胖不瘦。", "Someone you know: He is neither tall nor short, neither fat nor thin. (mine)"), ("蒙特雷的天气不冷不热。", "The weather in Monterey: neither cold nor hot. (mine)"), ("我们学校不大不小。", "DLI (the school): neither big nor small. (mine, a general sentence about a school)"), ("那个公园不远不近。", "A park: neither far nor near. (mine)")]
L3 = lesson(
    "Lesson 15 Presentation 3 grammar: the 不…不… construction",
    "不大不小 · 不冷不热 · 不急不慢 · 不快不慢地散步",
    requires=[],
    cards=[
        card("The 不…不… construction",
             "The 不…不… construction is used to express that neither A nor B are true; in colloquial Chinese it is often used to indicate a desirable state, such as 这双皮鞋不大不小 (neither too big nor too small) or 蒙特雷的天气不冷不热 (not too cold, not too hot). 不…不… + 的 + Noun (Noun Phrase). 不…不… + 地 + Verb (Verb Phrase).",
             examples=[D(z, e) for z, e in BB]),
        card("Activity 3 (Reading, Writing, and Speaking)",
             "A. In the passage the book gives, fill in the blanks with the words provided in parentheses using the 不…不… construction: 高、矮; 胖、瘦; 早、晚; 大、小; 多、少; 快、慢; 大、小; 远、近. B. Answer the questions: 1. 王丽长得什么样？ 2. 王丽什么时候去的电影院？ 3. 他们的晚饭吃得怎么样？ 4. 吃完晚饭以后他们做什么了？ (Mine: 不高不矮，不胖不瘦，爱笑; 三点半; 菜有点儿咸，但味道不错，四个菜八十元; 去海边不快不慢地散步，然后小李送她回公寓.) C. Check your work against the complete passage:",
             examples=[D(BB3, BB3_E)]),
        card("Activity 4 (Writing and Speaking)",
             "Work in pairs to write two phrases using the 不…不… construction to describe a person, the weather and some places. The rows in the book are: Someone you know; The weather in Monterey; DLI; A park. The book leaves them blank; my phrases (mine):",
             examples=[D(z, e) for z, e in BB4]),
    ],
    exercises=[
        M("What does 不…不… express?", "Neither A nor B (often a desirable state)", ["Both A and B", "Either A or B", "A and then B"], "Neither/nor."),
        M("What does 不大不小 mean?", "Neither big nor small", ["Very big", "Very small", "Not here"], "不大不小."),
        M("What does 不冷不热 describe?", "Weather that is just right", ["Freezing weather", "Hot weather", "Rainy weather"], "Not too cold, not too hot."),
        M("What does 王丽不早不晚三点半到那儿 mean?", "She arrived exactly at three thirty", ["She was late", "She was early", "She didn’t come"], "不早不晚."),
        M("What does 花了不多不少八十元钱 mean?", "It cost exactly eighty yuan", ["It cost a lot", "It cost nothing", "It cost less than eighty"], "不多不少."),
        M("What does 他是一个做事不急不慢的人 mean?", "He does things at a steady pace", ["He is always rushing", "He is lazy", "He doesn’t work"], "不急不慢."),
        M("What does 老王不言不语地看着电视 mean?", "Lao Wang watched TV silently", ["Lao Wang talked a lot", "Lao Wang turned off the TV", "Lao Wang sang"], "不言不语地."),
        F("这个房子不大不___。", "小", PART, "不大不小."),
        F("小李说话不快不___。", "慢", PART, "不快不慢."),
    ],
)

# ------------------------------------------------------------------ 4. 地
DD = [("他开心地笑了。", "He laughed happily."), ("我们慢慢地走到公园。", "We walked slowly to the park."), ("大家都在认真地做作业。", "Everyone is doing homework seriously."), ("她飞快地跑回家。", "She ran home very fast."), ("你们要多多地说中文。", "You should speak Chinese a lot.")]
DD6 = [("你说得太快，我没听清。", "A: You speak too fast; I didn’t hear clearly."), ("好，我慢慢地说。", "B: OK, I’ll speak slowly. (mine)"), ("小英，客人快到了，你把客厅简单地收拾一下。", "A: Xiaoying, the guests are about to arrive; tidy the living room simply. (mine)"), ("妈，我要去值班，你让小强收拾吧。", "B: Mom, I have to go on duty; let Xiaoqiang tidy up."),
       ("大卫，我们已经安全地到达北京了。", "A: David, we have already arrived safely in Beijing. (mine)"), ("太好了！你们在北京开心地玩儿几天吧。", "B: Great! Have a few happy days in Beijing. (mine)")]
L4 = lesson(
    "Lesson 15 Presentation 3 grammar: the adverbial modifier marker 地",
    "高兴地告诉我 · 慢慢地走 · 你跑得很慢 vs. 你慢慢地跑过去",
    requires=[],
    cards=[
        card("The adverbial modifier marker 地",
             "An adverb is a part of speech that modifies (i.e., describes) a verb. When an adverb describes the manner of a verb, it is often formed with an adjective and marked by the adverbial modifier 地. Example: 小王高兴地告诉我，她考上北京大学了。 An adverbial expression is different from a complement expression. A complement expression is descriptive in nature, whereas an adverbial expression tells the “attitude” or manner of an action. Also, a complement is most often used in connection with a habitual action, or an action that has already taken place, whereas an adverbial modifier may also refer to an action that has yet to happen. Example: 你跑得很慢 vs. 你慢慢地跑过去。 Adjective + 地 + Verb (+ Object).",
             examples=[D("小王高兴地告诉我，她考上北京大学了。", "Xiao Wang happily told me that she got into Peking University."), D("你跑得很慢。", "You run very slowly. (complement)"), D("你慢慢地跑过去。", "Run over slowly. (adverbial)")] + [D(z, e) for z, e in DD]),
        card("Activities 5 and 6",
             "Activity 5 (Listening, Writing, and Speaking). A. Listen to the conversation and write the six sentences you heard using either an adverbial 地 or a complement 得 construction, then translate them into English. B. Pair up and compare. (Audio, not included.) Activity 6 (Writing and Speaking). A. Complete the exchanges using 地 in each one: Exchange 1: 好，我___。(慢，说) Exchange 2: 小英，客人快到了，你把客厅___。(简单，收拾) Exchange 3: 我们已经___北京了。(安全，到达) 你们在北京___几天吧。(开心，玩儿) B. Pair up and check each other’s work; translate into English and back into Chinese. My completed exchanges (mine):",
             examples=[D(z, e) for z, e in DD6]),
    ],
    exercises=[
        M("What does 地 do in 慢慢地走?", "Marks an adverbial modifier before the verb", ["Marks a complement after the verb", "Means “ground”", "Makes a question"], "Adjective + 地 + Verb."),
        M("What does 你慢慢地跑过去 express?", "The manner of an action yet to happen", ["A finished action", "How well you run", "A habit"], "Adverbial: may refer to a future action."),
        M("What does 你跑得很慢 describe?", "How you run (a complement)", ["A future plan", "Where you run", "Who runs"], "Complement of degree."),
        M("What does 他开心地笑了 mean?", "He laughed happily", ["He laughed a lot", "He did not laugh", "He was laughed at"], "开心地笑."),
        M("What does 她飞快地跑回家 mean?", "She ran home very fast", ["She walked home", "She stayed home", "She drove home"], "飞快地."),
        M("What does 大家都在认真地做作业 mean?", "Everyone is doing homework seriously", ["Everyone finished", "Nobody works", "Everyone is playing"], "认真地."),
        M("What does 你们要多多地说中文 mean?", "You should speak Chinese a lot", ["Don’t speak Chinese", "Speak less", "Speak English"], "多多地."),
        F("小王高兴___告诉我，她考上北京大学了。", "地", PART, "Adjective + 地 + Verb."),
        F("你说得太快，我没听___。", "清", PART, "听清: hear clearly."),
    ],
)

# ------------------------------------------------------------------ 5. 着
ZH = [("客厅里摆着一张三人沙发。", "In the living room is placed a three-person sofa."), ("主卧室里面放着一张双人床。", "In the master bedroom is placed a double bed."), ("后院种着很多果树。", "In the backyard are planted many fruit trees."), ("爸爸们又带着孩子们踢球。", "The dads again took the kids to play soccer."), ("妈妈们忙着收拾垃圾。", "The moms were busy tidying up the trash.")]
ZH2 = [("大明在院子里站着。", "Daming is standing in the yard."), ("他穿着军服。", "He is wearing a military uniform."), ("军服上写着他的名字。", "His name is written on the uniform."), ("她坐着讲课。", "She lectures sitting down."), ("王老师笑着说：“没关系。”", "Teacher Wang said with a smile: “It doesn’t matter.”"), ("有的人沿着小路骑自行车。", "Some people ride bicycles along the trail.")]
ZH3 = [("李老师在教室里坐着。", "Teacher Li is sitting in the classroom."), ("教室里放着四张桌子和十把椅子。", "In the classroom are placed four tables and ten chairs."), ("李老师不坐着讲课。", "Teacher Li doesn’t lecture sitting down."), ("教室里没有放着桌子和椅子。", "There are no tables and chairs placed in the classroom."), ("李老师在教室里坐着讲课吗？", "Does Teacher Li lecture sitting in the classroom?"), ("教室里放着四张桌子和十把椅子吗？", "Are there four tables and ten chairs in the classroom?"),
       ("李老师有没有在教室里坐着？", "Is Teacher Li sitting in the classroom?"), ("教室里是不是放着四张桌子和十把椅子？", "Are there four tables and ten chairs placed in the classroom?")]
A7 = [("李", "王先生，这套公寓带什么样的家具？", "Mr. Wang, what kind of furniture does this apartment come with?"), ("王", "您来看一下客厅。里面摆着一张沙发，放着一个咖啡桌，还有一个电视柜。", "Take a look at the living room. Inside are a sofa, a coffee table and a TV cabinet. (blank filled by me)"), ("李", "卧室里呢？", "And in the bedrooms?"), ("王", "每间卧室里摆着一张床，床的两边放着床头柜。", "Every bedroom has a bed, and beside the bed are nightstands. (blank filled by me)"),
      ("李", "很好。我们就租这套公寓吧。哪天我们可以搬进来？", "Very good. Let’s rent this apartment. Which day can we move in?"), ("王", "后天就可以。你们家有几口人？", "The day after tomorrow is fine. How many people are in your family?"), ("李", "四口。我和我太太，还有两个女儿。", "Four. My wife and I, and two daughters."), ("王", "她们也来了吧？", "They came too, right?"),
      ("李", "来了。在门外站着的是我太太。", "Yes. The one standing outside the door is my wife. (blank filled by me)"), ("王", "和她说话的那个女孩儿是您女儿吗？", "Is the girl talking with her your daughter?"), ("李", "对，是我大女儿。我小女儿在车里坐着。", "Yes, that’s my older daughter. My younger daughter is sitting in the car. (blank filled by me)")]
L5 = lesson(
    "Lesson 15 Presentation 3 grammar: the aspect particle 着",
    "客厅里摆着沙发 · 带着孩子们踢球 · 忙着收拾垃圾 · 笑着说",
    requires=[],
    cards=[
        card("The aspect particle 着",
             "The aspect particle 着 appears after a verb indicating the state or continuation of an action in a static mode. Example: 大明在院子里站着；客厅里放着一张沙发。 We can use the pattern verb + 着 to modify the following verb, thus indicating the state or manner in which the action is carried out. Example: 她坐着讲课。 In Lesson 10 Presentation 3 we learned: 客厅里摆着一张三人沙发。主卧室里面放着一张双人床。后院种着很多果树。 In the current presentation: 爸爸们又带着孩子们踢球，而妈妈们忙着收拾垃圾。 In all these sentences, the aspect particle 着 appears after a verb indicating continuation, either a) indicating an existing state, such as sentences 1 to 3; or b) indicating the manner of carrying out an action, such as sentences 4 and 5. Manner and action: 带着孩子们 (taking the kids) + 踢球 (to play soccer); 忙着 (being busy) + 收拾垃圾 (to clean up). *着 can also be a suffix for some words to form a preposition, such as 沿着 in this presentation.",
             examples=[D(z, e) for z, e in ZH] + [D(z, e) for z, e in ZH2]),
        card("Patterns and examples",
             "Affirmative: Subject + Verb + 着; Subject + Verb + 着 + Verb (+ Object). Negative: Subject + 不/没有 + verb + 着 (+ Object); Subject + 不是/没有 + verb + 着 + Verb (+ Object). Interrogative: Subject + Verb + 着 + 吗？; Subject + Verb + 着 + Verb (+ Object) + 吗？ Affirmative-Negative: Subject + 有没有/是不是 + verb + 着？; Subject + 有没有/是不是 + Verb + 着 + Verb (+ Object)？ The eight examples:",
             examples=[D(z, e) for z, e in ZH3]),
        card("Activities 7 and 8",
             "Activity 7 (Listening, Reading, and Speaking). A. Listen to the conversation and complete the sentences in Pinyin from what you heard. The blanks are filled in below by me in characters (mine, since the audio is not included). B. Pair up; translate each sentence into English while your partner translates back to Chinese. Activity 8 (Speaking). A. Describe people and things in your classroom, using the aspect particle 着 whenever possible (People: Teacher, Classmate A, Classmate B; Things: Item A, Item B, Item C). B. Share your work in pairs.",
             examples=dlg(A7)),
    ],
    exercises=[
        M("What does 着 indicate after a verb?", "A continuing state or the manner of an action", ["A completed action", "A past experience", "A question"], "State or manner."),
        M("What does 客厅里摆着一张三人沙发 mean?", "A three-person sofa is placed in the living room", ["A sofa was sold", "Three people sit in the living room", "The sofa is broken"], "Existing state."),
        M("What does 她坐着讲课 mean?", "She lectures sitting down", ["She stands to lecture", "She sits and listens", "She doesn’t lecture"], "Manner."),
        M("What does 王老师笑着说 mean?", "Teacher Wang said with a smile", ["Teacher Wang laughed at me", "Teacher Wang didn’t speak", "Teacher Wang cried"], "笑着说."),
        M("What does 妈妈们忙着收拾垃圾 mean?", "The moms were busy tidying up the trash", ["The moms threw trash", "The moms were resting", "The moms went home"], "忙着."),
        M("How do you negate 着 with a place or state?", "没有 + verb + 着", ["verb + 没 + 着", "不 + 着", "着 + 不"], "没有 + verb + 着."),
        M("What does 沿着 mean in 沿着小路骑自行车?", "Along", ["Across", "Against", "Behind"], "沿着: along."),
        M("What does 他穿着军服 describe?", "He is wearing a uniform", ["He bought a uniform", "He washed a uniform", "He took off a uniform"], "State."),
        F("军服上写___他的名字。", "着", PART, "写着: is written."),
        F("爸爸们又带___孩子们踢球。", "着", PART, "带着: taking."),
    ],
)

# ------------------------------------------------------------------ 6. 直到…才…
ZD = [("昨天晚上一直到十点半我才做完作业。", "Last night I didn’t finish my homework until ten thirty."), ("昨天晚上我一直到十点半才做完作业。", "Last night I didn’t finish my homework until ten thirty."), ("直到十岁他还没上小学。", "Until ten he had not yet started elementary school."), ("他直到十岁还没上小学。", "He had not yet started elementary school until he was ten."),
      ("直到晚上十二点他都不睡觉。", "He doesn’t go to sleep until twelve at night."), ("他直到晚上十二点都不睡觉。", "He doesn’t sleep until twelve at night."), ("是不是直到周末你才给我打电话？", "Is it that you didn’t call me until the weekend?"), ("你是不是直到周末才给我打电话？", "Is it that you didn’t call me until the weekend?"), ("昨天他一直到十点才回家。", "Yesterday he didn’t go home until ten.")]
ZA9 = [("小李经常吃北京烤鸭吧？", "Xiao Li often eats Peking duck, right?"), ("昨天你们去哪儿了？", "Where did you go yesterday?"), ("你们那儿今天下雨了吗？", "Did it rain where you are today?")]
ZA10 = [("我昨天一直到晚上十一点才睡觉。", "I didn’t go to sleep until eleven last night. (mine)"), ("他一直到三十岁才结婚。", "He didn’t get married until he was thirty. (mine)"), ("我们一直等到八点才吃饭。", "We didn’t eat until eight. (mine)"), ("她直到今天早上才看到我的邮件。", "She didn’t see my email until this morning. (mine)"), ("他们一直玩到天黑才回家。", "They played until dark before going home. (mine)")]
L6 = lesson(
    "Lesson 15 Presentation 3 grammar: the (一)直到…才… construction",
    "一直到十点才回家 · 直到十岁还没上小学 · 一直玩到天黑才回家",
    requires=[],
    cards=[
        card("The (一)直到…才… construction",
             "This construction expresses the idea of “not until….” Example: 昨天他一直到十点才回家。 Affirmative: (一)直到 + Time/Event + Subject + 才…; Subject + (一)直到 + Time/Event + 才… Negative: (一)直到 + Time/Event + Subject + 都/还 + 不/没…; Subject + (一)直到 + Time/Event + 都/还 + 不/没… The eight examples (the book prints them in two columns, 1 to 8; the first example is repeated at the end):",
             examples=[D(z, e) for z, e in ZD]),
        card("Activities 9 and 10",
             "Activity 9 (Listening, Speaking, Writing and Reading). A. Listen to the questions and write your answers in Chinese: 1. 问的是什么问题？ 2. 小李经常吃北京烤鸭吧？ 3. 昨天你们去哪儿了？ 4. 问的是什么问题？ 5. 你们那儿今天下雨了吗？ (Audio, not included; questions 1 and 4 are on the audio only. The three printed questions:) B. Pair up and share; translate each sentence into English and back into Chinese.",
             examples=[D(z, e) for z, e in ZA9]),
        card("Activity 10 (Speaking and Writing)",
             "A. Think of five real situations that can be described using the (一)直到…才… construction. B. Pair up. Take turns describing one situation to your partner, and they will provide a sentence using the construction. Share two of your sentences with the class. The book leaves five blank lines; my five sentences (mine):",
             examples=[D(z, e) for z, e in ZA10]),
    ],
    exercises=[
        M("What does (一)直到…才… express?", "Not until…", ["As soon as…", "Even though…", "Instead of…"], "Not until."),
        M("What does 昨天他一直到十点才回家 mean?", "He didn’t go home until ten yesterday", ["He went home at ten", "He never went home", "He went home early"], "Not until ten."),
        M("What does 他直到十岁还没上小学 mean?", "He had not started school until age ten", ["He started school at ten", "He graduated at ten", "He hated school"], "Negative: 还没."),
        M("What does 直到晚上十二点他都不睡觉 mean?", "He doesn’t sleep until twelve at night", ["He sleeps at twelve", "He sleeps all day", "He never sleeps"], "都不."),
        M("Which word follows the time in the affirmative pattern?", "才", ["就", "了", "过"], "才."),
        M("Which words follow the time in the negative pattern?", "都/还 + 不/没", ["才 + 了", "就 + 了", "把 + 了"], "都/还 + 不/没."),
        M("What does 是不是直到周末你才给我打电话？ ask?", "Is it that you didn’t call until the weekend?", ["Did you call me today?", "Will you call on Sunday?", "Where were you?"], "Affirmative-negative question."),
        F("昨天晚上我一直到十点半___做完作业。", "才", PART, "一直到…才…"),
        F("他们一直玩到天黑才回___。", "家", PART, "回家."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
EM = ("爸爸、妈妈过年好！刚才看到爸爸发来的视频。全家十几口人在一起过年，又吃又喝又说又笑，真热闹。爸爸、妈妈的身体看上去也不错，太好了！"
      "美国加州春节不放假，但今年春节是个星期天，大家不上班，很多华人朋友在我们学校的礼堂聚了聚。那天，大家每个人都带了一两个菜，还准备了各种饮料、水果、甜点。我做了一个红烧肉，还有一个水煮鱼，大家都很喜欢。那天最忙的要数您儿媳萍萍了。她组织了一些朋友给大家表演节目。有的唱歌，有的跳舞，很受欢迎。我最喜欢的节目是孩子们的舞蹈，里面也有您的孙子和孙女。看他们在舞台上高兴地跳来跳去，觉得特别开心。聚会从中午十二点开始，一直到下午四点才结束。"
      "明年我和萍萍打算带着两个孩子回老家，和爸爸妈妈还有其他家人一起过年。多多保重！您的儿媳、孙子、孙女也祝您身体健康！二林")
EM_E = ("Dad and Mom, happy New Year! I just saw the video Dad sent. The whole family, over ten people, spent the New Year together, eating, drinking, talking and laughing; so lively. Dad and Mom look well too, which is great! In California, the US, there is no holiday for Spring Festival, but this year Spring Festival was on a Sunday and nobody was at work, so many Chinese friends gathered in our school’s auditorium. That day everyone brought one or two dishes, and there were also all kinds of drinks, fruit and desserts. I made a red-braised pork and a boiled fish, which everyone liked. The busiest that day was your daughter-in-law Pingping. She organized some friends to perform for everyone. Some sang, some danced, and it was very popular. My favorite item was the children’s dance, which included your grandson and granddaughter. Watching them jump around happily on the stage, I felt especially happy. The party started at twelve noon and did not end until four in the afternoon. Next year Pingping and I plan to take our two children back to our hometown to spend the New Year with you and our other family. Take good care! Your daughter-in-law, grandson and granddaughter also wish you good health! Erlin")
SC = table(["Item", "活动一", "活动二", "活动三"],
           [["活动", "马小文女朋友的生日", "庆祝老张买新房、搬家", "马兵和太太结婚二十周年"], ["时间", "星期六中午", "星期六晚上", "星期天中午"], ["地点", "中山饭店", "老张的新家", "东湖饭店"], ["饮料、菜、甜点", "啤酒、果汁、广东菜、点心", "啤酒、橙汁、茶水、四川菜、巧克力", "啤酒、茶水、咖啡、上海菜、蛋糕"],
            ["参加者", "马小文的父母和哥哥、妹妹", "老张一家和老张的四位朋友和家人", "马兵的兄弟姐妹和几位朋友"], ["聚会以后", "去公园散步", "去海边看风景", "坐游船"]],
           title="Activity 3 scenarios (columns as I read the book’s table)", say=[1, 2, 3])
NAR = ("星期六中午，马小文的父母、哥哥和妹妹在中山饭店给马小文的女朋友过生日。大家喝了啤酒和果汁，吃了广东菜和点心。吃完饭以后，大家一起去公园散步。")
L7 = lesson(
    "Lesson 15 Presentation 3: skill integration",
    "二林的邮件 · 过年好 · 三个聚会的安排",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, and Speaking)",
             "A. Listen to the two dialogs and match them with the pictures (A, B, C; one is irrelevant). Check each other’s work in pairs. New expressions: 小声点儿 (xiǎoshēng diǎnr; be quiet), 蛋糕 (dàngāo; cake). B. Pair up. Each partner listens to a dialog and writes the EEIs in the space provided. C. Ask your partner to tell you the main idea of their dialog; take notes. D. Discuss the main differences between the two dialogs with your partner; report your findings to the class. (Audio and pictures, not included.)"),
        card("Activity 2 (Reading, Speaking, and Writing): Erlin’s email",
             "A. Read the email below (the book prints TO, CC and Subject lines empty). Look up any unfamiliar words, then answer in English: 1. Why did Erlin write this message? 2. How did his family in China celebrate Chinese New Year? 3. What did the Chinese community do to celebrate Chinese New Year on Sunday? 4. What did Erlin, his wife, and children do respectively for the gathering? (Mine: to say Happy New Year to his parents and tell them about his celebration; over ten people gathered, eating, drinking, talking and laughing; they gathered in the school auditorium, each bringing dishes, drinks, fruit and dessert, with performances; Erlin made red-braised pork and boiled fish, Pingping organized the performances, and the children danced.) B. Pair up and compare; ask each other three questions in Chinese about the details. C. Work with your partner to rewrite the passage as a dialog between Erlin and his father (five exchanges) and act it out.",
             examples=[D(EM, EM_E)]),
        card("Activity 3 (Reading, Speaking, and Writing)",
             "Form groups of three. Each member reads one scenario below, consults a dictionary and writes down new words.",
             tables=[SC]),
        card("Activity 3 A to C",
             "A. Each group member creates a narration about one event in their own words, consisting of six to eight sentences, and shares it in the group. B. Take turns asking your group member three questions about your story; they answer as fluently as possible. C. Take turns telling your partners two expressions you have just learned; they tell you their meanings in English. The book leaves the lines blank; the start of a narration (mine, for the first event):",
             examples=[D(NAR, "On Saturday noon Ma Xiaowen’s parents, older brother and younger sister celebrated his girlfriend’s birthday at Zhongshan Restaurant. They had beer and juice and ate Cantonese food and dim sum. After the meal they all went for a walk in the park. (mine)")]),
    ],
    exercises=[
        M("Why did Erlin write?", "To say Happy New Year and tell about his celebration", ["To ask for money", "To cancel a trip", "To ask for a recipe"], "过年好."),
        M("How many people gathered in the family’s New Year video?", "More than ten", ["Two", "Five", "Fifty"], "全家十几口人."),
        M("Why was there a Spring Festival gathering at the school?", "It was on Sunday, so nobody worked", ["It was a school holiday", "Classes were cancelled", "It was a festival of the school"], "今年春节是个星期天，大家不上班。"),
        M("What dishes did Erlin make?", "Red-braised pork and boiled fish", ["Dumplings", "Roast duck", "Fried rice"], "红烧肉，水煮鱼."),
        M("Who was the busiest that day?", "Pingping, the daughter-in-law", ["Erlin", "The children", "The grandfather"], "最忙的要数您儿媳萍萍."),
        M("What was Erlin’s favorite program?", "The children’s dance", ["The singing", "The speech", "The food"], "孩子们的舞蹈."),
        M("When did the gathering end?", "Four in the afternoon", ["Noon", "Midnight", "Six"], "一直到下午四点才结束."),
        M("What do Erlin and Pingping plan for next year?", "Take the children back to the hometown for New Year", ["Stay in California", "Go to Japan", "Hold another party"], "打算带着两个孩子回老家."),
        M("What does 小声点儿 mean?", "Be quiet", ["Come quickly", "Sit down", "Look here"], "小声点儿."),
        M("Where is the second scenario’s party?", "At Lao Zhang’s new home", ["Zhongshan Restaurant", "East Lake Restaurant", "The park"], "老张的新家."),
        M("What do guests do after Ma Bing’s anniversary meal?", "Take a boat ride", ["Walk in the park", "See the sea view", "Go home"], "坐游船."),
        F("美国加州春节不___假。", "放", PART, "放假: have a holiday."),
        F("聚会从中午十二点开始，一直到下午四点___结束。", "才", PART, "一直到…才…"),
    ],
)

# ------------------------------------------------------------------ 8. context
SUN = ("马龙：你好！谢谢你邀请我参加星期三的聚会！很长时间没见到同学们，这次见面，发现大家的中文比以前更好了，我非常高兴。那天的活动组织得真不错。我在系里开会一直开到十一点半才过去，到那儿一看，啊，你们准备了那么多又好吃又好看的菜，还有各种饮料和水果，太棒了！我特别喜欢同学们做的苹果派，王老师做的牛肉也好吃，很受欢迎。西瓜是你买的吧？那么甜，我吃了可不少呢。"
       "大家坐着边吃边聊，都是讲中文。看来同学们都喜欢学中文，学习也很努力，这是让老师们最开心的事儿。很高兴见到你太太和你们的儿子。你儿子我以前见过，这次又看到他，发现这孩子比上次高了很多，也更可爱了。再次感谢你邀请我参加这次活动！孙老师")
SUN_E = ("Ma Long: Hello! Thank you for inviting me to Wednesday’s gathering! I hadn’t seen the students for a long time; meeting this time, I found everyone’s Chinese better than before, and I’m very happy. The event was really well organized. My meeting at the department went on until eleven thirty before I could come over; when I got there, ah, you had prepared so many delicious and good-looking dishes, plus all kinds of drinks and fruit; wonderful! I especially liked the apple pie the students made, and the beef Teacher Wang made was also tasty and popular. The watermelon was bought by you, right? So sweet; I ate quite a lot. Everyone sat eating and chatting while speaking Chinese. It seems the students all like learning Chinese and study very hard, which is what makes teachers happiest. I was very glad to see your wife and your son. I had seen your son before; seeing him again this time, I found he is much taller than last time and cuter. Thank you again for inviting me to this event! Teacher Sun")
POT = ("前几天同学老王打来电话，说小钱从美国回来了，想和老同学们一起吃个饭。我说，这次不去饭店吃了，咱们去海边来一次百乐餐怎么样？老王说，好啊，你来组织吧。我马上发邮件给每个同学，告诉他们我的计划，请他们到时候每人带一个菜去海边。老王准备喝的东西，我准备餐具和甜点。"
       "聚会那天，我早早地坐公共汽车到了海边，发现有一半的同学早就到了。他们边喝茶边聊天，十分热闹。小钱和他太太也在，还给大家带来了美国巧克力。一会儿大家就都到了，各种各样的饭菜放在一起，差不多有二十个，有鱼、牛肉、猪肉、素菜……，还有饺子和面条。我买了一个大蛋糕，老王带了啤酒、葡萄酒和饮料。大家边吃边聊天，说了很多上大学时候的事。最后，小钱说，欢迎大家明年去美国，到加州玩儿几天。到时候，他会请大家到他们家吃烤肉，大家一起热闹热闹。")
POT_E = ("A few days ago my classmate Lao Wang called and said Xiao Qian had come back from the US and wanted to have a meal with old classmates. I said, this time let’s not eat at a restaurant; how about having a potluck by the sea? Lao Wang said, good, you organize it. I immediately emailed every classmate to tell them my plan and ask each to bring a dish to the seaside. Lao Wang would prepare the drinks and I would prepare tableware and dessert. On the day of the gathering I took the bus early to the seaside and found that half of the classmates had arrived long before. They were drinking tea and chatting; very lively. Xiao Qian and his wife were also there and had brought American chocolate for everyone. Soon everybody had arrived; all kinds of food were put together, almost twenty dishes, including fish, beef, pork, vegetables…, as well as dumplings and noodles. I bought a big cake, and Lao Wang brought beer, wine and drinks. Everyone ate and chatted and talked about many things from their university days. In the end Xiao Qian said, everyone is welcome to come to the US next year and play for a few days in California. By then he will invite everyone to his home to have a barbecue and have fun together.")
SUMM = ("星期六下午，大约五百人来到蒙特雷社区中心庆祝春节，市长是特别客人。活动十一点半开始，市长向华人社区祝贺春节，也感谢他们对本地社区的贡献。接着是文化表演，大家唱歌，跳传统舞蹈，观众不停地欢呼鼓掌，特别是学生们的表演。主办方在当地的中餐馆订了菜，很多人也带来了自己做的菜。刘奶奶带来了她包的饺子，她说她老家的人除夕一定要吃饺子。庆祝活动三点半左右结束。蒙特雷已经连续七年举办春节庆祝活动。")
SUMM_E = "Mine: On Saturday afternoon about five hundred people came to Monterey Community Center to celebrate Chinese New Year, with the mayor as special guest. The event started at eleven thirty; the mayor congratulated the Chinese community and thanked it for its contribution. Next came cultural performances: singing and traditional dances, and the audience kept cheering and applauding, especially for the students. The organizers ordered food from local Chinese restaurants and many people brought home-made food. Mrs. Liu brought dumplings, saying people in her hometown must eat dumplings on New Year’s Eve. The event ended around three thirty. Monterey has hosted the celebration for seven years."
L8 = lesson(
    "Lesson 15 Presentation 3: using Chinese in context",
    "孙老师的邮件 · 百乐餐 · 春节庆祝活动",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, and Speaking): Sun Laoshi’s email",
             "Last Wednesday your class had a very successful picnic. You invited both Sun Laoshi and Gao Laoshi, but only Sun was able to attend. A. Both teachers contacted you after the event. In pairs, you read Sun Laoshi’s email (subject 孙老师的邮件), and your partner listens to Gao Laoshi’s message (audio, not included). B. Share the main idea of your message with your partner and write down what you heard; to double-check, read the script of Gao Laoshi’s message while your partner reads Sun Laoshi’s email, and give each other feedback. C. Work together to write an email to Gao Laoshi (subject 给高老师的邮件) and describe what happened at the picnic last Wednesday; include the EEIs plus information about the weather, food, and what attendees were talking about. D. Share your email with the class.",
             examples=[D(SUN, SUN_E)]),
        card("Activity 2 (Writing, Reading, and Speaking): the potluck",
             "You are a graduate student at Shenzhen University in China; the president of the Graduate Student Club wants you to help organize an American-style potluck during the coming weekend. A. First, listen to an audio file you found online, then write in Chinese a brief description of potlucks in the United States (audio, not included). B. The potluck took place yesterday. You want to write an article for the Graduate Students Newsletter about the event (title 我们的百乐餐). Use your past experiences and imagination. The following passage may also help. C. Share your work in pairs.",
             examples=[D(POT, POT_E)]),
        card("Activity 3 (Writing and Speaking): the Chinese New Year report",
             "The local Chinese community celebrated the Chinese New Year last Saturday, and you did your part by helping to prepare a flyer in Chinese for the event. A. Below is a report about the event in the local newspaper. Write a summary in Chinese to share with your classmates, including the EEIs plus several important details. The report: “Around 500 people crowded the Monterey Community Center on Saturday afternoon to celebrate the Chinese New Year, with Monterey’s Mayor as special guest. The event started at 11:30. Speaking at the celebration, Mayor Smith congratulated the Chinese community on the arrival of the Chinese New Year, and he also thanked them for their contribution to the local community. Following the speeches were cultural performances. The performers sang songs and performed traditional Chinese dances. The audience loved the performances so much that they kept cheering and applauding, especially for those done by students from DLI. The organizers ordered food from local Chinese restaurants, and many participants brought their home-made food as well. One elderly lady, Mrs. Liu, brought dumplings she had made. She told the reporter that people in her hometown have to eat dumplings on Chinese New Year’s Eve. The celebrations ended around 3:30 pm. Monterey has been hosting annual celebrations of Chinese Lunar New Year for the last seven years.” B. Pair up and, in Chinese, ask each other about the event. (Pictures, not included.) My Chinese summary:",
             examples=[D(SUMM, SUMM_E)]),
    ],
    exercises=[
        M("Which teacher attended the picnic?", "Sun Laoshi", ["Gao Laoshi", "Both", "Neither"], "Only Sun was able to attend."),
        M("Why did Teacher Sun arrive late?", "A department meeting ran until eleven thirty", ["Traffic", "He was sick", "He forgot"], "开会一直开到十一点半."),
        M("What did Teacher Sun especially like?", "The apple pie the students made", ["The watermelon", "The hamburgers", "The tea"], "我特别喜欢同学们做的苹果派."),
        M("What makes teachers happiest, according to the email?", "Students liking and working hard at Chinese", ["Free food", "Short classes", "Early finish"], "这是让老师们最开心的事儿."),
        M("What did Teacher Sun notice about the host’s son?", "He is taller and cuter than last time", ["He is shorter", "He is sick", "He was absent"], "比上次高了很多，也更可爱了."),
        M("What did the narrator suggest instead of a restaurant?", "A potluck by the sea", ["A banquet", "A picnic at school", "A barbecue at home"], "咱们去海边来一次百乐餐."),
        M("What did Xiao Qian bring?", "American chocolate", ["Dumplings", "Wine", "A cake"], "美国巧克力."),
        M("What did the narrator buy?", "A big cake", ["Beer", "Fish", "Noodles"], "我买了一个大蛋糕."),
        M("What did Xiao Qian invite everyone to do?", "Visit California and have a barbecue at his home", ["Cook dumplings", "Go to the seaside", "Join a club"], "他会请大家到他们家吃烤肉."),
        M("How many people came to the Chinese New Year event?", "Around five hundred", ["Around fifty", "Around five thousand", "Around two hundred"], "Around 500."),
        M("Who was the special guest?", "Monterey’s mayor", ["A professor", "A reporter", "A student"], "Monterey’s Mayor."),
        M("What did Mrs. Liu bring?", "Homemade dumplings", ["Cake", "Beer", "Chocolate"], "Dumplings she had made."),
        mean("百乐餐", "bai3 le4 can1", "potluck", ["banquet", "breakfast", "buffet"]),
        F("我在系里开会一直开到十一点半___过去。", "才", PART, "一直…才…"),
    ],
)
L9 = vocab_lesson("Lesson 15 Presentation 3 vocabulary", "30 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 10. Area Studies
L10 = lesson(
    "Lesson 15 Area Studies: Invitations and Parties",
    "邀请和聚会 · family celebrations · weddings · business receptions",
    requires=[],
    cards=[
        card("Invitations and Parties",
             "Like all cultures, the Chinese have parties and celebrations to mark rites of passage or important transitions and passages from one stage of life to another. These celebrations share the good fortune of families, promote the success of firms and reaffirm the value of traditions to Chinese both in China and overseas. In general, formal invitations are not very common for Chinese family celebrations, which include housewarming, birthdays, funerals, annual family get-togethers during the autumn, and spring festivals. This is not to say that anyone can attend the celebrations, but the custom of delivering a formal written invitation for family activities is less popular in China than it is in the U.S. Family celebrations are frequently coordinated by word of mouth, phone calls or text messaging. Formal business dinners and government-sponsored banquets, on the other hand, often use written invitations similar to those used in Western cultures. Whether it is an informal phone call or a formal invitation card, the information given is essentially the same. The invitee is informed of the special occasion, when and where the celebration will be held and (often) what to wear or bring. (Photographs, not included.)"),
        card("Family parties and weddings",
             "Family parties are usually held for culturally identified special occasions. In China these include special birthdays, like celebrating the first month anniversary of a new baby’s birth or the 60th birthday of an adult. For these types of celebrations families invite relatives from near and far and prepare special dishes that are usually eaten only at these special occasions. These parties are likely to be held in the family’s home or the home of a close relative that is large enough to accommodate all the guests. Weddings also are an occasion for large family gatherings. Traditional Chinese society has many wedding rituals and party customs. These elaborate traditions were practiced less frequently in the twentieth century, because of war and internal strife that faced China in the first half of the century. After the founding of the People’s Republic of China, weddings in the city remained low key and were a smaller scale than the large gatherings of the past, which were still common in many parts of the countryside. Today, with China’s economic reforms, increased stability and growing wealth, weddings are again becoming larger and more complex. Some couples have traditional Chinese weddings, some follow Western ceremonies, and some do both!"),
        card("Business receptions and conclusion",
             "Business receptions and dinners are another sort of party. A foreign businessman or businesswoman may receive an invitation from a senior representative of a Chinese company who will host a dinner or evening reception to which the businessperson is invited. These invitations might also include a reference to attire and even the end time for the function, particularly if it is a reception and not a dinner. Some large enterprises or manufacturing corporations in China also host parties to celebrate their success or any positive changes that occur in their business and the surrounding community. These firms will post announcements on their public bulletin boards to tell their employees where and when to go for the celebration. They also may use invitation letters or even faxes and phone calls to invite local officials to participate as well. In conclusion, Chinese culture shares a link to Western culture in the use of parties and invitations to celebrate significant cultural events. Even though the holidays, foods and customs are unique to China, the activity is one common to the whole world. While formal invitations are less popular in China today than in the West, businesspeople, academics and other professionals who travel to China may well receive a formal dinner, banquet or even a party invitation from a firm or government organization’s representative that they work with. References: “Chinese Festivals and Events” (chinahighlights.com); “Cultural Atlas-China Etiquette” (culturalatlas.sbs.com.au)."),
    ],
    exercises=[
        M("How are Chinese family celebrations usually coordinated?", "By word of mouth, phone calls or text messaging", ["By formal written invitations", "By newspaper ads", "By posters only"], "Frequently coordinated by word of mouth, phone calls or text messaging."),
        M("Which events often use written invitations?", "Formal business dinners and government banquets", ["Birthdays", "Housewarmings", "Funerals"], "Written invitations for formal business dinners."),
        M("What information does an invitation give?", "The occasion, when and where, and often what to wear or bring", ["Only the price", "Only the menu", "Only the address"], "The invitee is informed of the special occasion."),
        M("Which birthday is celebrated in China?", "A baby’s first month and an adult’s 60th", ["Every year at 18", "Only the 100th", "No birthdays"], "First month and 60th birthday."),
        M("Where are family parties usually held?", "In the family’s home or a close relative’s large home", ["In a hotel only", "In a park only", "In a restaurant only"], "Family’s home or close relative’s home."),
        M("Why were traditional weddings practiced less in the twentieth century?", "War and internal strife", ["Lack of interest", "Law", "Weather"], "War and internal strife."),
        M("What is happening to weddings today?", "They are becoming larger and more complex", ["They are disappearing", "They are becoming smaller", "They are always the same"], "Again becoming larger and more complex."),
        M("How do firms announce celebrations to employees?", "On public bulletin boards", ["On television", "By radio", "By mail only"], "Post announcements on bulletin boards."),
        M("How may firms invite local officials?", "With invitation letters, faxes and phone calls", ["With emails only", "By text only", "By posters"], "Invitation letters, faxes and phone calls."),
        M("What do Chinese and Western cultures share?", "Using parties and invitations to celebrate significant events", ["The same holidays", "The same foods", "The same customs"], "A link in the use of parties and invitations."),
    ],
)

UNIT = unit("第十五课 社交聚会 Presentation 3: picnic, 来…去, 不…不…, 地, 着, 直到…才…, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
