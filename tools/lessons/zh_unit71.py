"""Unit 71: Lesson 24 (Unit 4 review), the grammar and usage review from the book's texts: prepositions, matching clauses, time words, modal
words, adjectives, verb phrases, giving directions, wise sayings and the relations between clauses. Audio and pictures are not included; the
book prints no answer keys for these activities, so the completed sentences, matchings and explanations are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('还是', 0, 'hai2'), ('还有', 0, 'hai2'), ('还跟', 0, 'hai2'), ('睡八个小时的觉', 6, 'jiao4'), ('睡觉', 1, 'jiao4'), ('得很好', 0, 'de5'), ('得到', 0, 'de2'), ('得多', 0, 'de5'), ('得太快', 0, 'de5'), ('得懂', 0, 'de5'), ('得最', 0, 'de5'), ('得比', 0, 'de5'), ('干得', 0, 'gan4'), ('得多', 0, 'de5'), ('得对', 0, 'de5'), ('称为', 1, 'wei2'), ('得很', 0, 'de5'), ('吃得', 1, 'de5'), ('睡得', 1, 'de5'), ('起得', 1, 'de5'), ('知道得', 2, 'de5'), ('说得', 1, 'de5')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. activity 1
G1 = [("出了宿舍门往南走。", "1. Leave the dorm door and walk south. (往)"),
      ("服务员对每位顾客都很热情。", "2. The attendant is warm toward every customer. (对)"),
      ("请跟我来。", "3. Please come with me. (跟)"),
      ("我对中国文化很有兴趣。", "4. I am very interested in Chinese culture. (对)"),
      ("你跟他说了些什么？", "5. What did you say to him? (跟; 对 also works)"),
      ("她把我介绍给了她的父母。", "6. She introduced me to her parents. (给)"),
      ("对你来说，家庭重要还是工作重要？", "7. For you, which is more important, family or work? (对)"),
      ("为了孩子，他们从农村搬到了城里。", "8. For the sake of their child they moved from the countryside to the city. (为了)"),
      ("我们向旅客们表示歉意。", "9. We apologize to the passengers. (向)"),
      ("我们都为你高兴。", "10. We are all happy for you. (为)"),
      ("我每天都给他打电话。", "11. I call him every day. (给)"),
      ("吃完晚饭后，我还跟她一起去看了一场电影。", "12. After dinner I also went with her to see a movie. (跟)")]
G1B = [("对大多数人来说，健康比金钱更重要。", "1. For most people, health is more important than money."),
       ("有人说，知识就是力量。对我来说，知识就是幸福。", "2. Some people say knowledge is power. For me, knowledge is happiness."),
       ("真正的朋友是别的人都离开你的时候，向你走来的那个人。", "3. A true friend is the one who walks toward you when everyone else has left you."),
       ("胜利不会向我们走来，只能是我们向胜利走去。", "4. Victory will not walk toward us; it can only be that we walk toward victory.")]
L1 = lesson(
    "Lesson 24 Grammar and Usage Review: prepositions 跟 向 往 对 为 为了 给",
    "往南走 · 对顾客热情 · 跟我来 · 把我介绍给父母 · 向旅客表示歉意 · 为你高兴 · 向胜利走去",
    requires=[],
    cards=[
        card("Activity 1 (Writing), part A",
             "Complete each sentence by writing the correct prepositions 跟，向，往，对，为，为了，or 给 in the space provided. The book prints the twelve sentences with a blank; the completed sentences below are my key, each with the word that fills the blank:",
             examples=[D(z, e) for z, e in G1]),
        card("Activity 1, part B",
             "Pair up, translate the following sentences into English, and discuss your work with your partner. The translations are mine.",
             examples=[D(z, e) for z, e in G1B]),
    ],
    exercises=[
        F("出了宿舍门___南走。", "往", ["对", "跟", "给"], "往 + direction + verb."),
        F("服务员___每位顾客都很热情。", "对", ["往", "跟", "给"], "对 + person: toward."),
        F("请___我来。", "跟", ["往", "对", "为了"], "跟: with, follow."),
        F("我___中国文化很有兴趣。", "对", ["向", "往", "给"], "对…有兴趣."),
        F("她把我介绍___了她的父母。", "给", ["往", "对", "为了"], "介绍给: introduce to."),
        F("___孩子，他们从农村搬到了城里。", "为了", ["往", "跟", "向"], "为了: for the sake of."),
        F("我们___旅客们表示歉意。", "向", ["往", "跟", "为了"], "向…表示歉意: apologize to."),
        F("我们都___你高兴。", "为", ["往", "给", "向"], "为…高兴: be happy for."),
        F("我每天都___他打电话。", "给", ["往", "对", "为了"], "给…打电话: call."),
        F("吃完晚饭后，我还___她一起去看了一场电影。", "跟", ["往", "对", "给"], "跟…一起: together with."),
        M("Which preposition goes with the direction in 往东走?", "往", ["对", "跟", "给"], "往: toward a direction."),
        M("What does 对大多数人来说，健康比金钱更重要 mean?", "For most people, health is more important than money", ["Most people have money", "Health is cheaper than money", "Money brings health"], "对…来说."),
        M("Which means “walk toward victory”?", "向胜利走去", ["对胜利走去", "给胜利走去", "往胜利来走"], "向…走去."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2 and 3
MA = [("这道菜不仅好吃，而且很有营养。", "1 → D. This dish is not only delicious but also very nutritious. (key mine)"),
      ("尽管老板很热情，但是谁都知道，他只是为了得到更多的钱。", "2 → E. Although the boss is very warm, everyone knows he only wants to get more money. (mine)"),
      ("他不但提前做完了，而且做得很好。", "3 → A. He not only finished ahead of time but also did it very well. (mine)"),
      ("你说在街上看见我了？可我根本就没有出去。", "4 → B. You say you saw me on the street? But I didn’t go out at all. (mine)"),
      ("说不说都一样，反正没有人会听我的。", "5 → F. It is the same whether I speak or not; nobody will listen to me anyway. (mine)"),
      ("我没有时间参加这个活动，另外，我也不太感兴趣。", "6 → G. I have no time to take part in this activity; besides, I am not very interested. (mine)"),
      ("刚来的时候我很不适应这里的天气，不过现在已经习惯了。", "7 → C. When I first came I was not used to the weather here, but I am used to it now. (mine)")]
TM = [("最近我很忙，每天都要学习到很晚。", "1. 最近: recently. I have been very busy recently and study until late every day. (all sample sentences in this card are mine)"),
      ("最近几天天气很冷，我都穿着大衣。", "2. 最近几天: the last few days. It has been cold the last few days, and I have been wearing my overcoat."),
      ("等我做完作业才能去看电影。", "3. 等…才: only after. I can go to the movies only after I finish my homework."),
      ("我刚到中国的时候，一句中文也不会说。", "4. 刚: just. When I had just arrived in China I could not say a word of Chinese."),
      ("刚才老师说了什么？我没听懂。", "5. 刚才: a moment ago. What did the teacher say just now? I didn’t understand."),
      ("我早就知道他是中国人了。", "6. 早就: long ago. I knew long ago that he is Chinese."),
      ("等你来的时候，我给你做麻婆豆腐。", "7. 等…的时候: when. When you come I will make mapo tofu for you."),
      ("上上周我去了上海。", "8. 上上周: the week before last. The week before last I went to Shanghai."),
      ("下个月我要去北京看朋友。", "9. 下个月: next month. Next month I am going to Beijing to see friends."),
      ("大后天我们有考试。", "10. 大后天: three days from now. We have an exam three days from now."),
      ("看了医生，我才知道是流感。", "11. 看了…我才: only after seeing. Only after seeing the doctor did I know it was the flu."),
      ("刚开始学中文的时候，我觉得汉字太难了。", "12. 刚开始…的时候: when just starting. When I first started learning Chinese I thought the characters were too hard.")]
L2 = lesson(
    "Lesson 24 Grammar and Usage Review: matching clauses and time words",
    "不仅…而且… · 尽管…但是… · 反正 · 另外 · 最近 刚才 早就 · 等…才 · 大后天",
    requires=[],
    cards=[
        card("Activity 2 (Reading)",
             "Match the clauses in Column A and Column B to make complete sentences. Write the letters from Column B in the left column of the table. Column A: 1. 这道菜不仅好吃， 2. 尽管老板很热情， 3. 他不但提前做完了， 4. 你说在街上看见我了？ 5. 说不说都一样， 6. 我没有时间参加这个活动， 7. 刚来的时候我很不适应这里的天气， Column B: A. 而且做得很好。 B. 可我根本就没有出去。 C. 不过现在已经习惯了。 D. 而且很有营养。 E. 但是谁都知道，他只是为了得到更多的钱。 F. 反正没有人会听我的。 G. 另外，我也不太感兴趣。 The book gives no key; my matching, joined into sentences:",
             examples=[D(z, e) for z, e in MA]),
        card("Activity 3 (Writing and Speaking)",
             "A. You have learned several words and phrases for time reference in this Unit. Choose five words or phrases from the list below to write sentences using your own experience: 最近 | 最近几天 | 等…才 | 刚 | 刚才 | 早就 | 等…的时候 | 上上周 | 下个月 | 大后天 | 看了…我才 | 刚开始…的时候. B. Pair up. Read your sentences to your partner, making sure you understand each other. Then, together, study the words that were not used. One sample sentence for each of the twelve:",
             examples=[D(z, e) for z, e in TM]),
    ],
    exercises=[
        M("Which ending goes with 这道菜不仅好吃，?", "而且很有营养。", ["可我根本就没有出去。", "反正没有人会听我的。", "不过现在已经习惯了。"], "1 → D."),
        M("Which ending goes with 尽管老板很热情，?", "但是谁都知道，他只是为了得到更多的钱。", ["而且做得很好。", "另外，我也不太感兴趣。", "而且很有营养。"], "2 → E."),
        M("Which ending goes with 他不但提前做完了，?", "而且做得很好。", ["可我根本就没有出去。", "另外，我也不太感兴趣。", "反正没有人会听我的。"], "3 → A."),
        M("Which ending goes with 你说在街上看见我了？", "可我根本就没有出去。", ["不过现在已经习惯了。", "而且很有营养。", "反正没有人会听我的。"], "4 → B."),
        M("Which ending goes with 说不说都一样，?", "反正没有人会听我的。", ["另外，我也不太感兴趣。", "不过现在已经习惯了。", "而且做得很好。"], "5 → F."),
        M("Which ending goes with 我没有时间参加这个活动，?", "另外，我也不太感兴趣。", ["反正没有人会听我的。", "可我根本就没有出去。", "而且很有营养。"], "6 → G."),
        M("Which ending goes with 刚来的时候我很不适应这里的天气，?", "不过现在已经习惯了。", ["而且做得很好。", "另外，我也不太感兴趣。", "但是谁都知道。"], "7 → C."),
        M("Which word means “the week before last”?", "上上周", ["下个月", "大后天", "刚才"], "上上周."),
        M("Which word means “three days from now”?", "大后天", ["上上周", "刚才", "最近"], "大后天."),
        M("Which word means “a moment ago”?", "刚才", ["早就", "刚开始", "最近"], "刚才."),
        F("等我做完作业___能去看电影。", "才", ["就", "也", "都"], "等…才: only after."),
        F("我___就知道他是中国人了。", "早", ["刚", "才", "再"], "早就: long ago."),
    ],
)

# ------------------------------------------------------------------ 3. activities 4 and 5
M4 = [("你每天晚上应该睡八个小时的觉。", "1. You should have eight hours of sleep every night. (应该)"),
      ("你不应该吃着东西说话。", "2. You shouldn’t talk while eating. (不应该; 不要 also works)"),
      ("你不能在这儿停车。", "3. You can’t park here. (不能)"),
      ("晚上一个人去那个地方恐怕不太安全吧。", "4. I’m afraid it’s not safe to go there alone at night. (恐怕)"),
      ("我今天要跟朋友去演唱会，大概晚上十点回来。", "5. I will go to a concert with a friend, and I will be back by around ten p.m. (大概)"),
      ("这个节日也许对大家都不太重要，但是我希望你们不要忘记。", "6. This holiday may not be important to you, but I hope none of you will forget it. (也许)"),
      ("学音乐还是学画画，要看孩子自己的兴趣。", "7. The decision to learn a musical instrument or art should depend on the child’s own preference. (要看)"),
      ("别问了，我不想说。", "8. Stop asking, I don’t want to talk about it. (别; 不要 also works)"),
      ("你不需要看那本书。", "9. You don’t need to read that book. (不需要)"),
      ("你一定要小心。", "10. You have definitely got to be careful. (the word bank has no word for this blank; the natural word is 一定, which is mine)"),
      ("往左转，你会看见一家邮局。", "11. Make a left turn and you will see the post office. (会)")]
M5 = [("坐高铁比坐飞机方便得多。", "1. It is much more convenient to take the high-speed train than an airplane. (key mine)"),
      ("考试那天，我紧张极了。", "2. I was super nervous the day I took the examination. (mine)"),
      ("他说得太快了，你们听得懂吗？", "3. He speaks so quickly. Can you understand? (mine)"),
      ("我的电脑很旧，你的电脑很新。", "4. My computer is old and yours is new. (mine)"),
      ("知道得最多的人，说得最少。", "5. The person who knows the most speaks the least. (mine)")]
SY = [("起得比鸡早，睡得比狗晚，吃得比猪差，干得比牛多。", "Some people make fun of themselves and say that their life is like this: they get up earlier than the chickens, go to bed later than the dogs, eat worse than the pigs and work more than the oxen. (the saying expresses an overworked, poorly fed life; translation mine)"),
      ("多听，多看，多想，多做，少说。", "Listen more, look more, think more, do more, speak less. (the advice to be modest and to learn by practice; translation mine)")]
L3 = lesson(
    "Lesson 24 Grammar and Usage Review: modal words and adjectives",
    "应该 不应该 不能 恐怕 大概 也许 要看 别 不需要 会 · 方便得多 · 紧张极了 · 起得比鸡早",
    requires=[],
    cards=[
        card("Activity 4 (Reading and Writing)",
             "Complete the sentences according to their English translations using the following words: 要看 | 恐怕 | 别 | 不要 | 大概 | 也许 | 不能 | 不需要 | 会 | 不应该 | 应该. The book prints the eleven sentences with a blank and the English; my key, with the word in brackets. The bank has eleven words for ten blanks plus a blank (item 10) that needs 一定, so one bank word is left over:",
             examples=[D(z, e) for z, e in M4]),
        card("Activity 5 (Speaking and Listening), part A",
             "In this unit, you learned the various usages of adjectives. Pair up and complete the sentences according to their English translations. The book prints partial sentences; my completed sentences:",
             examples=[D(z, e) for z, e in M5]),
        card("Activity 5, parts B to D",
             "B. Listen to a dialog between a wife and husband and answer the questions: 1. Where did this conversation likely take place? 2. What is the intention of the wife? 3. What is the husband’s attitude? (audio, not included) C. Some people make fun of themselves and say that their life is like this: 起得比鸡早，睡得比狗晚，吃得比猪差，干得比牛多。 1. What does the saying want to express? 2. Do you agree with this advice? Why? D. Listen to two explanations of the following advice. Which do you prefer? Do you have your own explanation? 多听，多看，多想，多做，少说。 (audio, not included).",
             examples=[D(z, e) for z, e in SY]),
    ],
    exercises=[
        F("你每天晚上___睡八个小时的觉。", "应该", ["不能", "恐怕", "别"], "应该: should."),
        F("你___吃着东西说话。", "不应该", ["应该", "大概", "会"], "不应该: shouldn’t."),
        F("你___在这儿停车。", "不能", ["应该", "也许", "大概"], "不能: can’t."),
        F("晚上一个人去那个地方___不太安全吧。", "恐怕", ["别", "会", "应该"], "恐怕: I’m afraid."),
        F("我今天要跟朋友去演唱会，___晚上十点回来。", "大概", ["恐怕", "别", "不能"], "大概: about."),
        F("这个节日___对大家都不太重要。", "也许", ["别", "应该", "不能"], "也许: maybe."),
        F("学音乐还是学画画，___孩子自己的兴趣。", "要看", ["别", "恐怕", "不能"], "要看: depends on."),
        F("___问了，我不想说。", "别", ["也许", "应该", "大概"], "别: don’t."),
        F("你___看那本书。", "不需要", ["应该", "也许", "大概"], "不需要: don’t need to."),
        F("往左转，你___看见一家邮局。", "会", ["别", "不能", "恐怕"], "会: will."),
        M("What does 坐高铁比坐飞机方便得多 mean?", "The train is much more convenient than the plane", ["The plane is more convenient", "They are the same", "The train is much slower"], "比…得多: much more."),
        M("What does 知道得最多的人，说得最少 mean?", "The person who knows the most speaks the least", ["Everyone speaks a lot", "The one who speaks most knows most", "Nobody knows anything"], "V得最…."),
        M("In 起得比鸡早，睡得比狗晚…, what is the saying about?", "Working very hard for little", ["Having a good life", "Keeping pets", "Eating a lot"], "A joke about overwork."),
    ],
)

# ------------------------------------------------------------------ 4. activities 6, 7, 8
V6 = [("生男生女都一样。", "1. Boys or girls, it’s all the same. (the book’s caption beside the photo: 跳起舞来唱起歌, start dancing and singing; all translations mine)"),
      ("打是亲，骂是爱。", "2. Hitting is affection, scolding is love. (a proverb: those who hit or scold you do it out of love)"),
      ("我在大街上走着走着就迷路了。", "3. I was walking along the street and, before I knew it, got lost. (V着V着就…: while doing something, a change happens)"),
      ("说着说着，她就哭了起来。", "4. As she was talking, she started to cry. (V起来: start to)"),
      ("跳起舞来唱起歌", "The picture caption: start dancing and start singing.")]
V7 = [("请问，这附近有地铁站吗？", "1. Excuse me, is there a subway station near here? (all sample Chinese in this card is mine)"),
      ("大华商店离这儿不太远，走二十分钟就到了。", "2. Dahua Store is not too far from here, just a 20-minute walk."),
      ("出了地铁站，一直往前走。", "3. After leaving the subway station, keep walking forward."),
      ("沿着这条路走到红绿灯，然后往右拐。", "4. Follow this road to the traffic light and then turn right."),
      ("过了三个十字路口，在停车牌那儿往左拐。", "5. After three intersections, turn left at the stop sign."),
      ("你会看到一家邮局。", "6. You will see a post office."),
      ("过了邮局，继续往前走。", "7. After passing the post office, keep going forward."),
      ("中国银行就在你的右手边。", "8. The Bank of China is on your right."),
      ("上往北去的六十五号高速公路。", "9. Take northbound Highway 65. (the number is spelled out)"),
      ("从四十七号出口下高速公路。", "10. Leave the highway from Exit 47."),
      ("坐地铁三号线，坐六站，在中山公园站下车。", "11. Take line 3 subway, get off at Zhongshan Park station after six stops."),
      ("换乘十二路公共汽车。", "12. Transfer to bus No. 12.")]
L4 = lesson(
    "Lesson 24 Grammar and Usage Review: verb phrases and giving directions",
    "生男生女都一样 · 走着走着就迷路了 · 说着说着哭了起来 · 沿着这条路 · 过了三个十字路口 · 十二路公共汽车",
    requires=[],
    cards=[
        card("Activity 6 (Reading)",
             "Translate each sentence into English. Pay attention to the verb/verb phrase. The English is mine.",
             examples=[D(z, e) for z, e in V6]),
        card("Activity 7 (Speaking and Writing)",
             "Pair up and, in Chinese, take turns speaking the translations of the following directions. The book prints the English; the Chinese below is mine, with the numbers spelled out.",
             examples=[D(z, e) for z, e in V7]),
        card("Activity 8 (Speaking)", "Pair up. Describe the layout of your living quarters to your partner. (The photograph is not included.)"),
    ],
    exercises=[
        M("What does 走着走着就迷路了 mean?", "While walking I got lost", ["I walked home", "I asked the way", "I ran fast"], "V着V着就…."),
        M("What does 说着说着，她就哭了起来 mean?", "As she was talking she started to cry", ["She stopped talking", "She laughed", "She sang"], "V起来: start."),
        M("What does 打是亲，骂是爱 express?", "Those who scold you do it out of love", ["Hitting is forbidden", "Love is cheap", "Family is far"], "The proverb."),
        M("Which means “keep walking straight”?", "一直往前走", ["往后退", "站在这儿", "坐下来"], "一直往前走."),
        M("Which means “turn left”?", "往左拐", ["往右拐", "往前走", "往后走"], "往左拐."),
        M("Which means “follow this road”?", "沿着这条路", ["对着这条路", "给这条路", "为这条路"], "沿着: along."),
        M("Which means “it is on your right”?", "在你的右手边", ["在你的左手边", "在你的前面", "在你的后面"], "右手边."),
        M("Which means “get off at the stop”?", "下车", ["上车", "换车", "停车"], "下车."),
        M("Which means “transfer to bus 12”?", "换乘十二路公共汽车", ["坐十二个站", "走十二分钟", "买十二张票"], "换乘."),
        M("Which means “leave the highway from the exit”?", "从出口下高速公路", ["从出口上高速公路", "沿着出口走", "在出口停车"], "下高速."),
        F("出了地铁站，___往前走。", "一直", ["一定", "一起", "一共"], "一直: straight on."),
        F("过了三个十字路口，往左___。", "拐", ["走", "看", "买"], "往左拐."),
    ],
)

# ------------------------------------------------------------------ 5. activities 9 and 10
T9 = [("读书使人更有智慧。", "1. Reading makes people wiser. (translations in this card are mine)"),
      ("年轻时，我被叫做赌徒，现在我被称为银行家，但我一直在做同样的工作。", "2. When I was young I was called a gambler; now I am called a banker, but I have always been doing the same work."),
      ("社会应该让富人、勤快人和聪明人都能同时到达终点，才是公平的。", "3. Society should let the rich, the diligent and the clever all reach the finish line at the same time; only then is it fair."),
      ("我心中的欢乐不是我自己的，我把欢乐写进音乐，是为了让全世界都感到欢乐。", "4. The joy in my heart is not mine alone; I write joy into music in order to let the whole world feel joy.")]
T10 = [("越来越多的人去看中医，有的人是因为中药不但副作用小，而且价钱也比较便宜，还有的人是想试试新的治疗方法。", "1. 有的人…，还有的人… are parallel reasons; inside the first reason 因为 gives a cause and 不但…而且… is progressive. (my answers in this card)"),
       ("北京是美丽的，我知道，因为我不但是北京人，而且到过欧美，看见过很多西方的名城。", "2. 因为 gives the cause of “I know”; 不但…而且… adds a second reason, a progressive link."),
       ("地方那么大，事情那么多，我知道的真是太少了，虽然我就出生在那里，一直到二十多岁才离开。", "3. The first two clauses are parallel and lead to the result “I know too little”; 虽然… is a concession placed after the main clause: although I was born there and left only after twenty."),
       ("这个培训很受欢迎，参加的人非常多，不但有本校的学生，还有外校的学生，甚至还有外国学生。", "4. The first clause is the cause and the second the result; 不但…还…甚至还… is a progressive series, each one going further."),
       ("我想回到我自己的家里去，尽管它简陋，尽管它破旧，但在那里我是自由的。", "5. 尽管…，尽管…，但… is a transition: although the home is simple and shabby, there I am free.")]
L5 = lesson(
    "Lesson 24 Grammar and Usage Review: translating wise sayings and complex sentences",
    "读书使人更有智慧 · 被称为银行家 · 到达终点 · 不但…而且… · 虽然 · 尽管…但…",
    requires=[],
    cards=[
        card("Activity 9 (Reading and Speaking)",
             "Translate the following sentences into English, using your dictionary when necessary. Compare your work with that of a classmate. The English is mine.",
             examples=[D(z, e) for z, e in T9]),
        card("Activity 10 (Reading)",
             "Use your own words to explain the relationship between the clauses in each complex sentence. The book gives no key; my answers:",
             examples=[D(z, e) for z, e in T10]),
    ],
    exercises=[
        M("What does 读书使人更有智慧 mean?", "Reading makes people wiser", ["Reading is hard", "People read less", "Wisdom is cheap"], "使: make."),
        M("In sentence 2, what has stayed the same?", "The work he does", ["His age", "His name", "His city"], "一直在做同样的工作."),
        M("What does the sentence about fairness say?", "Everyone should reach the finish line together", ["Only the rich win", "Nobody should win", "The clever go first"], "同时到达终点."),
        M("Why does the speaker write joy into music?", "To let the whole world feel joy", ["To make money", "To be famous", "To forget sorrow"], "为了让全世界都感到欢乐."),
        M("What kind of link is 不但…而且…?", "Progressive", ["Transitional", "Causal", "Conditional"], "递进."),
        M("What kind of link is 尽管…但…?", "Transitional", ["Progressive", "Causal", "Parallel"], "转折."),
        M("What kind of link is 因为…?", "Causal", ["Progressive", "Transitional", "Parallel"], "因果."),
        M("In 越来越多的人去看中医, how many reasons are given?", "Three", ["One", "Two", "Five"], "价钱便宜, 副作用小, 想试新方法 (the first has two parts)."),
        F("年轻时，我___叫做赌徒，现在我被称为银行家。", "被", ["把", "给", "对"], "被: passive."),
        F("读书使人更有智___。", "慧", ["会", "惠", "回"], "智慧: wisdom."),
        F("我想回到我自己的家里去，尽___它简陋，但在那里我是自由的。", "管", ["量", "快", "是"], "尽管: although."),
    ],
)

UNIT = unit("第二十四课 Unit 4 review: grammar and usage review", [L1, L2, L3, L4, L5])
