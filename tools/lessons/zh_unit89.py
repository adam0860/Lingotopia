"""Unit 89: Lesson 28 (China's Youth), Presentation 2: Getting Started, the mother's e-mail to her daughter, Activities 1-4 and the Grammar and Usage section
(就是 expressing insistence, 就像…说的, parallel sentences, 呢 to express contrast, expressions with 点).
Audio and pictures are not included; the traditional-character copy of the e-mail is not repeated; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l28_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('长大', 0, 'zhang3'), ('觉得自己', 1, 'de5'), ('我们得多说', 2, 'dei3'), ('我们得多读', 2, 'dei3')):
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

# ------------------------------------------------------------------ 1. getting started, presentation 2, activity 1
EM = [("女儿，你已经回学校了。妈妈给你发个邮件，想跟你聊聊。", "Daughter, you have already gone back to school. Mom is sending you an e-mail because I want to chat with you. (Presentation 2, an e-mail from a mother to her daughter; translations mine)"),
      ("上个周末咱们出去买东西，你就是不让我开车，一定要骑共享单车，说是为了保护环境。当时妈妈很不理解，心想，这零零后是怎么了？现在静下心来，妈妈越想越觉得女儿有道理。就像你说的，世界是我们每个人的，大家都要爱护它。", "Last weekend when we went out shopping, you simply wouldn’t let me drive and insisted on riding a shared bike, saying it was to protect the environment. At the time Mom didn’t understand at all and thought, what is the matter with these post-’00s? Now that I have calmed down, the more I think about it, the more I feel my daughter is right. Just as you said, the world belongs to each of us, and everyone should cherish it. (the book writes 00 后 in digits)"),
      ("妈妈也在想，为什么咱们有时想不到一块儿呢？这可能是因为我们长大的环境不同。妈妈以前的生活条件没有你们的好，没坐过飞机，没出过国，更没有互联网，对外面的事情了解得很少。你们呢，从小就用互联网，生活在一个信息发达的世界，知道的事情比我们多多了，所以你们不只想着自己，而且也常常关心世界上的事情。还有一点，就是看到不对的事情，你们就会说出来，比妈妈这一代强。", "Mom has also been wondering why we sometimes can’t think alike. Perhaps it is because the environments we grew up in were different. Mom’s living conditions before were not as good as yours; I never rode in a plane, never went abroad, and there certainly was no Internet, so I knew very little about things outside. You, on the other hand, have used the Internet since childhood and live in a world with developed information; you know many more things than we do, so you don’t only think of yourselves but also often care about things in the world. One more thing: when you see something wrong, you speak out, which is better than Mom’s generation."),
      ("以后，妈妈要多跟你交流。下次你回来，咱们一起骑共享单车去郊外看风景。", "From now on, Mom wants to communicate with you more. The next time you come back, let’s ride shared bikes together to the suburbs to see the scenery."),
      ("就说这么多。妈妈爱你！", "That’s all I’ll say for now. Mom loves you!")]
A1 = [("妈妈想跟女儿聊聊，说说自己的想法，也想以后多跟女儿交流。", "Activity 1A-1 (my answer): Why did the mother write this e-mail? She wanted to chat with her daughter, share her thoughts, and communicate with her more in the future."),
      ("妈妈觉得女儿有道理，女儿这一代知道的事情多，关心世界上的事情，比妈妈这一代强。", "1A-2 (my answer): How does the mother feel about her daughter’s generation? She thinks her daughter is right; this generation knows more, cares about what happens in the world and is better than the mother’s generation."),
      ("上个周末买东西的时候，女儿不让妈妈开车，一定要骑共享单车，妈妈当时很不理解。", "1B-1 (my answer): What upset the mother last weekend? When they went shopping, her daughter wouldn’t let her drive and insisted on shared bikes; at the time she didn’t understand."),
      ("妈妈静下心来想，越想越觉得女儿有道理。", "1B-2 (my answer): How did the mother feel afterward? After calming down, the more she thought about it the more she felt her daughter was right."),
      ("妈妈以前没坐过飞机，没出过国，没有互联网，对外面的事情了解得很少；女儿从小就用互联网，生活在一个信息发达的世界，知道的事情比妈妈多多了。", "1B-3 (my answer): The mother had never flown or gone abroad, had no Internet and knew little about the outside; the daughter has used the Internet since childhood and lives in a developed information world, knowing much more."),
      ("妈妈这一代看到不对的事情，可能不会说出来，她觉得女儿这一代比她强。", "1B-4 (my answer): The mother’s generation probably would not speak out when seeing improper behavior, and she thinks her daughter’s generation does better.")]
L1 = lesson(
    "Lesson 28 Presentation 2: a mother’s e-mail to her daughter",
    "共享单车 · 保护环境 · 想不到一块儿 · 静下心来 · 就像你说的 · 信息发达 · 说出来",
    requires=[],
    cards=[
        card("Presentation 2: Getting Started",
             "Pair up. Discuss the following questions with your partner. A. How do young people in the U.S. care for the environment? Give an example. B. What impact has technology had on young people in the U.S.? C. What topics do you and your parents not agree on? (Discussion questions; the book gives no answers.)"),
        card("Presentation 2: the e-mail (the book gives the simplified and traditional versions; the traditional text is not repeated)",
             "A mother writes to her daughter, who has gone back to school, about last weekend’s shopping trip and about how their two generations grew up.",
             examples=[D(z, e) for z, e in EM]),
        card("Presentation 2 Activities, Activity 1 (Listening and Speaking)",
             "A. Global Listening: Listen to Presentation 2 and answer the questions. 1. Why did the mother write this email? 2. How does the mother feel about her daughter’s generation? B. Detailed Listening: Listen to Presentation 2 again and answer the questions. 1. What upset the mother last weekend? 2. How did the mother feel about it afterward? 3. List the differences between the respective environments in which the mother and daughter grew up. 4. How would the mother most likely respond if she witnessed improper behavior? My answers, in Chinese:",
             examples=[D(z, e) for z, e in A1]),
    ],
    exercises=[
        M("Why did the mother write the e-mail?", "She wanted to chat with her daughter", ["She wanted to borrow money", "She wanted to buy a bike", "She was angry at her husband"], "想跟你聊聊."),
        M("What did the daughter insist on last weekend?", "Riding a shared bike", ["Driving the car", "Taking a taxi", "Walking home"], "一定要骑共享单车."),
        M("Why did the daughter want to ride a shared bike?", "To protect the environment", ["To save money", "To exercise", "To go faster"], "说是为了保护环境."),
        M("How did the mother feel at the time?", "She did not understand", ["She was happy", "She was proud", "She was sleepy"], "当时妈妈很不理解."),
        M("What did the mother think after calming down?", "Her daughter is right", ["Her daughter is wrong", "Her daughter is rude", "Her daughter is lazy"], "越想越觉得女儿有道理."),
        M("What had the mother never done before?", "Flown on a plane or gone abroad", ["Eaten out", "Gone to school", "Ridden a bike"], "没坐过飞机，没出过国."),
        M("What does the mother say about her daughter’s generation?", "They also care about what happens in the world", ["They only think of themselves", "They know less than she does", "They dislike the Internet"], "也常常关心世界上的事情."),
        M("Where does the mother want to ride shared bikes next time?", "To the suburbs to see the scenery", ["To the airport", "To the school", "To a store"], "骑共享单车去郊外看风景."),
        F("上个周末咱们出去买东西，你就是不让我开___。", "车", ["书", "话", "饭"], "开车: drive."),
        F("你们不只想着自己，而且也常常关心世界上的事___。", "情", ["吗", "们", "了"], "事情: things."),
        F("妈妈以前的生活条件没有你们的___。", "好", ["多", "少", "大"], "没有你们的好: not as good as yours."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2-4
VT = table(["动词", "Objects (my key; some verbs take several)", "Phrases"],
           [["保护", "4, 5", "保护地球，保护环境"], ["理解", "2, 3", "理解朋友，理解她说的话"], ["爱护", "4, 5", "爱护地球，爱护环境"], ["关心", "2, 4, 5", "关心朋友，关心地球，关心环境"], ["共享", "1", "共享美食"]],
           title="Activity 2A: the verbs and objects (1. 美食 2. 朋友 3. 她说的话 4. 地球 5. 环境)")
S2 = [("你静下心来想一想，就会理解他为什么这样做。", "Activity 2B-1 (my sentence; 静下心来 and 理解): If you calm down and think it over, you will understand why he does it this way."), ("妈妈不让我去，可我一定要去。", "2B-2 (my sentence; 不让 and 一定要): Mom won’t let me go, but I insist on going."),
      ("你说得有道理，我们俩想到一块儿去了。", "2B-3 (my sentence; 有道理 and 想到一块儿): What you say makes sense; the two of us think alike."), ("看到不对的事情，如果你发现了，就应该说出来。", "2B-4 (my sentence; 发现 and 说出来): When you see something wrong, if you notice it, you should speak out."),
      ("当时我不理解，现在我明白了。", "2B-5 (my sentence; 当时 and 现在): At the time I didn’t understand; now I do.")]
SCR3 = [("妈妈，看了您的邮件，我真高兴。谢谢妈妈这么理解我！", "Activity 3 script (the daughter’s reply; translations mine): Mom, I was really happy to read your e-mail. Thank you, Mom, for understanding me so much!"),
        ("您说得有道理，由于长大的环境不一样，我们有时候会想得不一样。还记得您给我讲过，当年您来北京上大学，先坐公共汽车，再坐长途公共汽车，又坐火车，路上走了四五天。现在呢，从老家来北京，半天就到了。特别是有了互联网，世界变得越来越小，大家很容易知道世界上发生的事情。北极离我们非常远，以前谁也不会关心那么一个地方。可现在大家生活在一个信息发达的世界，我们了解到，地球在变得越来越暖和，北极的冰在慢慢地融化。如果这样发展下去，再过几十年，地球的很多地方就不能住人了。", "You are right; because the environments we grew up in are different, we sometimes think differently. I remember you told me that when you came to Beijing for university, you first took a bus, then a long-distance bus, then a train, and spent four or five days on the road. Now, from our hometown to Beijing takes half a day. Especially with the Internet, the world has become smaller and smaller and everyone can easily learn what is happening in the world. The Arctic is very far from us, and in the past nobody cared about such a place. But now everyone lives in a world of developed information; we have learned that the earth is getting warmer and warmer and the ice in the Arctic is slowly melting. If this goes on, in a few decades many places on earth will not be fit to live in."),
        ("我也想告诉妈妈，女儿能有今天，是因为我从小就有很好的生活和学习条件，这一切都是您和爸爸给我的。第一次见到电脑的时候您已经十八岁了，而我七八岁就有了自己的电脑，可以天天上网了。女儿要好好地谢谢爸爸妈妈！", "I also want to tell Mom that the reason your daughter is where she is today is that I have had very good living and learning conditions since childhood; all of this was given to me by you and Dad. When you first saw a computer you were already eighteen, while I had my own computer at seven or eight and could go online every day. Your daughter wants to thank Mom and Dad properly!"),
        ("女儿爱您！", "Your daughter loves you!")]
TF3 = [("这是女儿给妈妈的电子邮件，她谈到互联网对人们的影响。", "Activity 3A-1 (true or false; my key: True): This is the daughter’s e-mail to her mother, in which she talks about the Internet’s influence on people."),
       ("女儿觉得妈妈当年应该坐飞机去北京上大学。", "3A-2 (my key: False): The daughter thinks her mother should have flown to Beijing for university back then."),
       ("女儿说，妈妈年轻的时候，交通和信息都没有现在这么发达。", "3A-3 (my key: True): The daughter says that when her mother was young, transportation and information were not as developed as now."),
       ("女儿很感谢爸爸妈妈，因为他们让她最好的学校上学。", "3A-4 (my key: False, she thanks them for good living and learning conditions; the book prints 让她最好的学校上学 without 去): The daughter thanks her parents because they let her attend the best school."),
       ("妈妈一直不会用电脑，而女儿很小就有自己的电脑了。", "3A-5 (my key: False, the script says only that the mother first saw a computer at eighteen): The mother has never been able to use a computer, while the daughter had her own computer very young.")]
WK3 = table(["词", "Meaning (mine)"], [["北极", "the Arctic"], ["融化", "melt"]], title="Activity 3A: the words to work out first", say=[0])
SUM3 = [("女儿谢谢妈妈理解她。她说，由于长大的环境不同，她们有时想得不一样。妈妈当年来北京上大学要走四五天，现在半天就到了，有了互联网，大家很容易知道世界上发生的事情，比如北极的冰在慢慢融化。女儿也谢谢爸爸妈妈从小给她很好的条件，让她七八岁就有了自己的电脑。", "Activity 3B (my sample summary, in Chinese): The daughter thanks her mother for understanding her. She says that because they grew up in different environments they sometimes think differently. When her mother came to Beijing for university it took four or five days; now it takes half a day, and with the Internet everyone easily learns what happens in the world, such as the Arctic ice slowly melting. She also thanks her parents for the good conditions they gave her from childhood, so that she had her own computer at seven or eight.")]
CL1 = ("有一次我去文具店，买了一盒圆珠笔。我旁边一个看上去不到二十岁的女孩子，告诉服务员她要买笔芯，不买笔。我说了一句，“用笔芯多麻烦。”那女孩儿转过头来，笑着说，“是麻烦，可是塑料很难降解，用得越少越好啊。”她还告诉我，塑料不但对环境不好，还会伤害海里的动物。一些海洋动物，就因为吃了人们丢在海里的塑料袋，生了病，甚至死了……", "Once I went to a stationery store and bought a box of ballpoint pens. Next to me was a girl who looked under twenty, telling the clerk she wanted to buy refills, not pens. I said, “Using refills is so much trouble.” The girl turned her head and said with a smile, “It is trouble, but plastic is very hard to break down, and the less we use the better.” She also told me that plastic is not only bad for the environment but also harms animals in the sea. Some marine animals, just because they ate the plastic bags people threw into the sea, got sick or even died… (Activity 4A, with the blanks filled by my key; the book writes 20 in digits)")
CL2 = ("她说的这些，我好像以前也听说过，但从来没觉得自己该做些什么。现在看到她认真的样子，我有点儿不好意思。回到家，我静下心来想了又想，觉得能理解他们了，也开始知道为什么我们和他们常常想不到一块儿了。这些零零后，是在互联网的环境下长大的。他们从小就学到了前几代无法学到的知识，所以常常站得比我们高，想得也比我们远。他们的年龄虽然比我们小很多，但是在有些方面，比我们更成熟。他们觉得关心世界、爱护地球是他们该做的事，并且能说出他们的想法，来教育别人。就这一点来说，我们得好好地向他们学习。", "I seem to have heard these things she said before, but I never felt I should do something. Now, seeing her earnest look, I feel a little embarrassed. Back home I calmed down and thought it over and over, and felt I could understand them, and began to know why we and they often can’t think alike. These post-’00s grew up in the environment of the Internet. From childhood they learned knowledge that earlier generations could not learn, so they often stand higher than we do and think farther ahead. Although they are much younger than we are, in some respects they are more mature than we are. They feel that caring about the world and cherishing the earth is what they should do, and they can state their ideas to educate others. In this regard, we have to learn from them properly. (the book writes 00 后 in digits)")
KEY4 = table(["Blank", "Answer (my key)", "Blank", "Answer (my key)"],
             [["1", "b 看上去", "8", "c 站得"], ["2", "a 笑着说", "9", "b 想得"], ["3", "b 越少越好", "10", "a 关心"], ["4", "c 甚至", "11", "b 爱护"], ["5", "c 听说过", "12", "b 说出"], ["6", "a 静下心来", "13", "b 好好地"], ["7", "a 想不到一块儿", "", ""]],
             title="Activity 4A: the answers to the thirteen blanks (the book gives the choices only)")
SUM4 = [("一个女孩子买笔时只买笔芯，说塑料很难降解，用得越少越好，还会伤害海里的动物。作者听了以后有点儿不好意思，静下心来想，觉得能理解零零后了：他们是在互联网的环境下长大的，站得高，想得远，在有些方面比我们更成熟，我们得好好地向他们学习。", "Activity 4 summary (my sample, in Chinese): A girl buying pens bought only refills, saying plastic is very hard to break down, the less used the better, and it also harms sea animals. After hearing this the writer felt a little embarrassed, calmed down and thought, and felt able to understand the post-’00s: they grew up with the Internet, stand higher and think farther, and in some respects are more mature than we are, so we should learn from them properly.")]
L2 = lesson(
    "Lesson 28 Presentation 2 activities: matching verbs, the daughter’s reply and the girl who bought refills",
    "保护 理解 爱护 关心 共享 · 北极 融化 · 笔芯 塑料 降解 · 站得高 想得远",
    requires=[],
    cards=[
        card("Activity 2 (Reading, Writing, and Speaking)",
             "A. Match the following verbs with their objects by writing the number(s) in parentheses. Some verbs may take more than one object. Verbs: 保护, 理解, 爱护, 关心, 共享. Objects: 1. 美食 2. 朋友 3. 她说的话 4. 地球 5. 环境. B. Share your work with a classmate. Together, create sentences using the expressions provided: 1. 静下心来，理解 2. 不让，一定要 3. 有道理，想到一块儿 4. 发现，说出来 5. 当时，现在. My key and sentences:",
             tables=[VT], examples=[D(z, e) for z, e in S2]),
        card("Activity 3 (Listening, Speaking, and Reading)",
             "A. Listen to the dialog and mark the statements as either True or False. First determine the meaning of 北极 and 融化, then share your work with a classmate. B. Listen to the dialog again and write a summary in English. C. Share your summary with your partner in Chinese. Then use the script below to make any necessary corrections. The statements, my key, the script and a sample summary:",
             tables=[WK3], examples=[D(z, e) for z, e in TF3 + SCR3 + SUM3]),
        card("Activity 4 (Reading and Speaking)",
             "A. Choose the correct answers to fill in the blanks, then summarize the passage in English. The book gives thirteen blanks with three choices each (1. a. 听起来 b. 看上去 c. 说她自己; 2. a. 笑着说 b. 又笑又说 c. 笑了说; 3. a. 最少就好 b. 越少越好 c. 少了当然好; 4. a. 快快地 b. 有的 c. 甚至; 5. a. 知道过 b. 被告诉过 c. 听说过; 6. a. 静下心来 b. 边休息边 c. 让自己; 7. a. 想不到一块儿 b. 想不在一起 c. 想不到很多; 8. a. 长得 b. 跳得 c. 站得; 9. a. 住得 b. 想得 c. 感觉得; 10. a. 关心 b. 理解 c. 认识; 11. a. 明白 b. 爱护 c. 打扫; 12. a. 提供 b. 说出 c. 告诉; 13. a. 好好的 b. 好好地 c. 好好得). B. In Chinese, share your summary with a classmate. The passage with my key filled in:",
             tables=[KEY4], examples=[D(*CL1), D(*CL2)] + [D(z, e) for z, e in SUM4]),
    ],
    exercises=[
        M("Which objects go with 保护 in my key?", "地球 and 环境", ["美食", "朋友", "她说的话"], "保护地球，保护环境."),
        M("Which object goes with 共享?", "美食", ["地球", "环境", "朋友"], "共享美食."),
        M("How long did the mother’s trip to Beijing take in the daughter’s story?", "Four or five days", ["Half a day", "One hour", "A month"], "路上走了四五天."),
        M("How long does the trip from the hometown to Beijing take now?", "Half a day", ["Four or five days", "Two weeks", "One hour"], "半天就到了."),
        M("What is happening to the Arctic ice, according to the daughter?", "It is slowly melting", ["It is growing", "It is staying the same", "It is moving"], "北极的冰在慢慢地融化."),
        M("How old was the mother when she first saw a computer?", "Eighteen", ["Eight", "Thirty", "Fifty"], "第一次见到电脑的时候您已经十八岁了."),
        M("What did the girl in the stationery store buy?", "Pen refills, not pens", ["A box of pens", "A notebook", "Nothing"], "她要买笔芯，不买笔."),
        M("What does plastic do to sea animals, according to the girl?", "It harms them", ["It feeds them", "It makes them stronger", "Nothing"], "还会伤害海里的动物."),
        M("What does the writer feel after seeing the girl’s earnest look?", "A little embarrassed", ["Angry", "Proud", "Sleepy"], "我有点儿不好意思."),
        F("北极的冰在慢慢地___化。", "融", ["学", "水", "热"], "融化: melt."),
        F("他们觉得关心世界、爱___地球是他们该做的事。", "护", ["看", "想", "跑"], "爱护: cherish."),
        F("就这一点来说，我们得好好地向他们学___。", "习", ["校", "生", "年"], "学习: learn."),
    ],
)

# ------------------------------------------------------------------ 3. grammar: 就是
J1 = [("我要他别抽烟了，可他就是要抽。", "I told him to stop smoking, but he just insists on smoking. (Grammar and Usage, 就是 Expressing Insistence; translations mine)"), ("别人都去睡觉了，可他就是要打游戏。", "Everyone else has gone to bed, but he just insists on playing games."), ("我要他跟我一起去锻炼，可他就是不去。", "I wanted him to go exercise with me, but he just won’t go.")]
J2 = [("A", "网上的书包又便宜又好看，为什么你一定要去商店买呢？", "A: Backpacks online are both cheap and good-looking; why must you go buy one at a store?"), ("B", "我就是喜欢那家商店的东西。", "B: I simply like the things in that store."),
      ("A", "纽约太冷了，你还是搬到加州来住吧。", "A: New York is too cold; you had better move to California to live."), ("B", "我就是喜欢纽约，别的地方都不想去。", "B: I simply like New York and don’t want to go anywhere else.")]
JN = [("我要他别抽烟了，可他就是要抽。", "Permissible: I told him to stop smoking, but he just insists on smoking."), ("我要他别抽烟了，可他一定要抽。", "Permissible: … but he insists on smoking."), ("我要他别抽烟了，可他非抽不可。", "Permissible: … but he must smoke."),
      ("我请他吃水果，可他就是不吃。", "Permissible (the book prints 我请他水果, apparently missing 吃): I invited him to eat fruit, but he just won’t eat it.")]
JNT = table(["", "Sentences"], [["It is not permissible to say", "我请他吃水果，可他一定不要吃 / 可他非不吃不可。"]], title="Note: 一定要 and 非…不可 are used only in affirmative sentences, while 就是 can be used both ways (the book’s incorrect sentences)")
JS = [("今天这么冷，我要我儿子多穿点儿衣服，可他还是要穿衬衣去上学。", "Activity 1B script, 1: It is so cold today; I told my son to wear more clothes, but he still insists on wearing a shirt to school."),
      ("这家菜店的东西很贵，我想到另一家菜店去买菜，可是我先生非要在这里买不可。", "2: The things in this vegetable store are expensive and I wanted to buy vegetables at another one, but my husband insists on buying here."),
      ("我告诉他，电影院已经关门了，可他一定要去电影院看电影。", "3: I told him the cinema had already closed, but he insisted on going to the cinema to watch a movie."),
      ("医生不让他喝酒，可是他非喝不可。", "4: The doctor won’t let him drink, but he has to drink."),
      ("我不想去，为什么你一定要我去呢？", "5: I don’t want to go; why do you insist that I go?"),
      ("今天不是特别的日子，可王民非要送鲜花给我不可。", "6: Today is not a special day, but Wang Min insists on giving me fresh flowers."),
      ("她知道学中文比较难，但是她一定要学，而且要学得很好。", "7: She knows learning Chinese is rather difficult, but she insists on learning it and wants to learn it very well."),
      ("爸爸告诉他夜里不能上网玩儿游戏，可他根本不听。", "8: Dad told him he can’t play online games at night, but he just doesn’t listen at all.")]
JM = [("今天这么冷，我要我儿子多穿点儿衣服，可他就是要穿衬衣去上学。", "Activity 1A, my version with 就是, 1: … but he just insists on wearing a shirt to school."), ("这家菜店的东西很贵，我想到另一家菜店去买菜，可是我先生就是要在这里买。", "2: … but my husband just insists on buying here."),
      ("我告诉他，电影院已经关门了，可他就是要去电影院看电影。", "3: … but he just insists on going to the cinema."), ("医生不让他喝酒，可是他就是要喝。", "4: The doctor won’t let him drink, but he just insists on drinking."),
      ("我不想去，为什么你就是要我去呢？", "5: I don’t want to go; why do you just insist on my going?"), ("今天不是特别的日子，可王民就是要送鲜花给我。", "6: Today is not a special day, but Wang Min just insists on giving me flowers."),
      ("她知道学中文比较难，但是她就是要学，而且要学得很好。", "7: She knows Chinese is difficult, but she just insists on studying it, and wants to study it very well."), ("爸爸告诉他夜里不能上网玩儿游戏，可他就是不听。", "8: Dad told him not to play online games at night, but he just won’t listen.")]
L3 = lesson(
    "Lesson 28 Presentation 2 grammar: 就是 expressing insistence",
    "就是要 · 就是不 · 一定要 · 非…不可 · 就是 can be used both affirmatively and negatively",
    requires=[],
    cards=[
        card("就是 Expressing Insistence",
             "In addition to expressing emphasis, 就是 can also be used to indicate the desire to do something “no matter what,” implying a degree of inflexibility. This expression is often followed by a modal verb, such as 要 and 想 in affirmative sentences. Note: Both 一定要 and 非…不可 also express desire, but they are used only in affirmative sentences, while 就是 can be used both affirmatively and negatively.",
             tables=[JNT], examples=[D(z, e) for z, e in J1] + dlg(J2) + [D(z, e) for z, e in JN]),
        card("Grammar and Usage, Activity 1 (Listening, Writing, Speaking, and Reading)",
             "A. Listen to the sentences and write a modified version of each using 就是 (eight audio items, which are not included; the script is given in B). B. Share your work with a classmate, then use the script below to refine your work. Take turns translating the modified sentences into English. The script, and my versions with 就是:",
             examples=[D(z, e) for z, e in JS + JM]),
    ],
    exercises=[
        M("What does 就是 add to a verb like 要 or 想?", "Insistence “no matter what”", ["Politeness", "Past tense", "A question"], "indicates the desire to do something no matter what."),
        M("In 他就是要抽, what does the speaker mean?", "He insists on smoking", ["He forgot to smoke", "He cannot smoke", "He wants to quit"], "他就是要抽."),
        M("Which of these can be used in negative sentences too?", "就是", ["一定要", "非…不可", "None of them"], "就是 can be used both affirmatively and negatively."),
        M("Which sentence is not permissible according to the Note?", "我请他吃水果，可他一定不要吃", ["我请他吃水果，可他就是不吃", "我要他别抽烟，可他非抽不可", "我要他别抽烟，可他就是要抽"], "一定要 is used only affirmatively."),
        M("What does 他就是不去 mean?", "He just won’t go", ["He just went", "He wants to go", "He forgot to go"], "我要他跟我一起去锻炼，可他就是不去."),
        M("Why does the speaker in the dialog insist on that store?", "She simply likes its things", ["It is cheaper", "It is closer", "It is bigger"], "我就是喜欢那家商店的东西."),
        F("我要他别抽烟了，可他就是要___。", "抽", ["看", "去", "吃"], "抽烟: smoke."),
        F("我就是___欢那家商店的东西。", "喜", ["想", "爱", "要"], "喜欢: like."),
        F("医生不让他喝酒，可是他非喝不___。", "可", ["会", "能", "用"], "非…不可: must."),
    ],
)

# ------------------------------------------------------------------ 4. 就像...说的 and parallel sentences
X1 = [("就像老师说的，我们得多说中文。", "Just as the teacher said, we have to speak more Chinese. (Discourse Grammar: 就像…说的; translations mine)"), ("就像电视上说的，这几天东部一直在下大雨。", "Just as it said on TV, it has been raining heavily in the east these past few days."),
      ("就像您刚才说的，我们得多读一些真实语料。", "Just as you said a moment ago, we have to read more authentic material."), ("就像以前我爷爷总说的，早起早睡身体好。", "Just as my grandfather always used to say, going to bed and rising early is good for your health."),
      ("就像网上说的，小孩子学外语学得特别快。", "Just as it says online, little children learn foreign languages especially fast.")]
X2 = [("就像教官说的，军人一定要守纪律。", "Activity 2A-1 (my completion): Just as the drill instructor said, soldiers must keep discipline."), ("就像班长说的，我们要互相帮助。", "2A-2 (my completion): Just as the class monitor said, we should help each other."),
      ("就像老师说的，学语言要多听多说。", "2A-3 (my completion): Just as the teacher said, to learn a language you must listen and speak a lot."), ("就像他太太说的，他工作太忙，应该多休息。", "2A-4 (my completion): Just as his wife said, he works too hard and should rest more."),
      ("就像她先生说的，周末我们去郊外骑车吧。", "2A-5 (my completion): Just as her husband said, let’s go cycling in the suburbs this weekend."), ("就像我妈妈说的，出门要多穿衣服。", "2A-6 (my completion): Just as my mother said, wear more clothes when you go out.")]
PS1 = [("家是一盏明亮的灯，家是一把结实的伞，家是一张舒服的床。", "Home is a bright lamp, home is a sturdy umbrella, home is a comfortable bed. (Parallel Sentences, example 1; translations mine)"), ("快乐是一幅画，快乐是一首歌，快乐是一片海。", "Happiness is a painting, happiness is a song, happiness is a sea."), ("时间就是速度，时间就是效率，时间就是生命。", "Time is speed, time is efficiency, time is life.")]
PS3 = [("生活是一杯酒，生活是一本书，生活是一支歌。", "Activity 3B script, 1: Life is a glass of wine, life is a book, life is a song. (my basic idea in English: life has many flavors and is something to savor)"), ("书是营养，书是明灯，书是朋友。", "2: Books are nourishment, books are bright lamps, books are friends. (idea: books feed, guide and accompany us)"),
       ("有阳光就会有黑云，有晴天就会有风雨，有进步就会有困难。", "3: Where there is sunshine there will be dark clouds, where there are clear days there will be wind and rain, where there is progress there will be difficulties. (idea: good and bad come together)"),
       ("朋友是冬天里的一杯热茶，是夏天里的一道凉风，是秋天里的一句“你好！”", "4: A friend is a cup of hot tea in winter, a cool breeze in summer, a “hello!” in autumn. (idea: friends bring comfort in every season)"),
       ("忘不了同学们对我的帮助，忘不了老师们对我的教导，忘不了学校对我的爱护。", "5: I can’t forget my classmates’ help, I can’t forget my teachers’ guidance, I can’t forget the school’s care. (idea: gratitude for help, teaching and care)")]
L4 = lesson(
    "Lesson 28 Presentation 2 grammar: 就像…说的 and parallel sentences",
    "就像老师说的 · 就像网上说的 · 排比句 · 家是一盏明亮的灯 · 时间就是生命 · 朋友是冬天里的一杯热茶",
    requires=[],
    cards=[
        card("Discourse Grammar: 就像…说的",
             "The expression 就像…说的 introduces what was said previously, and it usually implies that the words carry weight. Activity 2: A. With a classmate, complete the following statements: 1. 就像教官说的， 2. 就像班长说的， 3. 就像老师说的， 4. 就像他太太说的， 5. 就像她先生说的， 6. 就像我妈妈说的， B. Take turns asking your partner to create similar sentences. Provide your partner with the beginning part of the sentence. My completions:",
             examples=[D(z, e) for z, e in X1 + X2]),
        card("Parallel Sentences",
             "Parallel sentences in Chinese are three or more sentences used together that share the same structure and implication. They can create a sense of rhythm and vigor. Activity 3: A. Listen to the statements and, in English, write the basic idea of each (five audio items, which are not included). B. Share your work with a classmate. Then use the scripts below to refine your work. The scripts, with my basic ideas:",
             examples=[D(z, e) for z, e in PS1 + PS3]),
    ],
    exercises=[
        M("What does 就像…说的 do?", "Introduces what was said previously", ["Asks a question", "Expresses regret", "Gives a command"], "introduces what was said previously."),
        M("What does 就像老师说的 mean?", "Just as the teacher said", ["If the teacher says so", "Because of the teacher", "The teacher asked"], "就像老师说的."),
        M("What are parallel sentences?", "Three or more sentences with the same structure", ["One long sentence", "Two questions", "A list of names"], "three or more sentences … share the same structure."),
        M("What effect do parallel sentences create?", "Rhythm and vigor", ["Politeness", "Confusion", "Humor"], "They can create a sense of rhythm and vigor."),
        M("In 时间就是生命, what is time compared with?", "Life", ["Money", "A river", "A friend"], "时间就是速度，时间就是效率，时间就是生命."),
        M("What is a friend compared with in winter?", "A cup of hot tea", ["A cool breeze", "A painting", "A song"], "朋友是冬天里的一杯热茶."),
        F("就像电视上说___，这几天东部一直在下大雨。", "的", PART, "就像…说的."),
        F("家是一盏明亮的灯，家是一把结实的伞，家是一张舒服的___。", "床", ["书", "车", "饭"], "家是一张舒服的床."),
        F("忘不了同学们对我的帮助，忘不了老师们对我的___导。", "教", ["学", "看", "说"], "教导: guidance."),
    ],
)

# ------------------------------------------------------------------ 5. 呢 for contrast and 点 expressions
NE1 = [("他太太因为忙没时间收拾房间。他呢，有时间也不想收拾。", "His wife is too busy to tidy the room. As for him, even if he has time he doesn’t want to tidy it. (呢 to Express Contrast; translations mine)"), ("他白天在公司忙一天，晚上呢，还要上网学中文。", "He is busy at the company all day, and in the evening he still has to go online to study Chinese."),
       ("今天一下班我就回家了，平时呢，我会先去体育馆锻炼一会儿才回家。", "Today I went home as soon as I got off work; usually, though, I go to the gym for a while first and only then go home.")]
NE4 = [("平时我一到学校就去操场锻炼身体，今天呢，因为要考试，我直接去了教室。", "Activity 4B suggested answer 1: Usually as soon as I get to school I go to the playground to exercise, but today, because of an exam, I went straight to the classroom."), ("冬天我喜欢滑雪，夏天呢，我喜欢游泳。", "2: In winter I like to ski; in summer I like to swim."),
       ("现在你们的生活条件太好了。我呢，已经上中学了还不知道电视是什么样子。", "3: Your living conditions now are too good. As for me, I was already in middle school and still didn’t know what a television looked like."), ("老张很喜欢唱歌，他儿子呢，什么音乐也不喜欢。", "4: Lao Zhang likes singing very much; his son, though, doesn’t like any music."),
       ("他喜欢边听音乐边学习。我呢，喜欢学习的时候只学习，别的什么也不做。", "5: He likes to study while listening to music. I, on the other hand, like to do only studying when I study and nothing else."), ("星期六我要参加小王的婚礼，星期天呢，我们一家人要去旧金山买东西。", "6: On Saturday I am going to Xiao Wang’s wedding; on Sunday my family is going to San Francisco to shop.")]
NE4Q = table(["Original sentences for Activity 4A (add 呢 to the middle of each)", ""], [["1", "平时我一到学校就去操场锻炼身体，今天因为要考试，我直接去了教室。"], ["2", "冬天我喜欢滑雪，夏天我喜欢游泳。"], ["3", "现在你们的生活条件太好了。我已经上中学了还不知道电视是什么样子。"], ["4", "老张很喜欢唱歌，他儿子什么音乐也不喜欢。"], ["5", "他喜欢边听音乐边学习。我喜欢学习的时候只学习，别的什么也不做。"], ["6", "星期六我要参加小王的婚礼，星期天我们一家要去旧金山买东西。"]], title="Activity 4A: the sentences before adding 呢")
DT = table(["Expression", "Use (the book’s explanation)"], [["1. 还有一点", "one more thing: to bring up something new"], ["2. 关于这一点", "concerning this point: to say more about something"], ["3. 在这一点上", "concerning this point: to say more about something"], ["4. 就这一点来说", "in this regard: to say more about something"], ["5. 说(or 谈)几点看法/想法/观点/意见", "to share one’s views"]], title="话语语法: Expressions to Bring up or Elaborate on a Topic (点 occasionally means “point” or “thing”)")
D5 = [("关于这一点，大家还有什么要说的吗？", "Activity 5A-1 (translations mine): Concerning this point, does everyone have anything else to say?"), ("说到学中文，还有一点也很重要，就是多看多听真实语料。", "5A-2: Speaking of learning Chinese, there is one more important thing: read and listen to a lot of authentic material."),
      ("我觉得，在这一点上咱们想得都一样，没什么不同。", "5A-3: I think that on this point we all think the same, with no difference."), ("关于保护环境的问题，我讲两点自己的想法。", "5A-4: On the question of protecting the environment, let me state two of my own ideas."),
      ("就这一点来说，我们还有很多不足。", "5A-5: In this regard, we still have many shortcomings."), ("关于你们的计划，我来说几点自己的意见。", "5A-6: About your plan, let me give a few opinions of my own.")]
D5M = [("还有一点，学中文一定要多听多说。", "Activity 5B (my sample sentences, 1): One more thing: to learn Chinese you must listen and speak a lot."), ("关于这一点，我也有自己的想法。", "2: Concerning this point, I have my own ideas too."), ("在这一点上，我们的看法一样。", "3: On this point, our views are the same."),
       ("就这一点来说，他比我强。", "4: In this regard, he is better than I am."), ("关于环保，我想说几点看法。", "5: About environmental protection, I would like to share a few views.")]
L5 = lesson(
    "Lesson 28 Presentation 2 grammar: 呢 to express contrast and expressions with 点",
    "他呢 · 晚上呢 · 平时呢 · 还有一点 · 关于这一点 · 在这一点上 · 就这一点来说 · 说几点看法",
    requires=[],
    cards=[
        card("呢 to Express Contrast",
             "In colloquial Chinese, the particle 呢 can be used to signal a pause to express contrast. Activity 4: A. Modify the following sentences by adding 呢 to the middle of each. B. Share your work with a classmate. Go over the suggested answers below and take turns translating each into English. The examples and the book’s suggested answers:",
             tables=[NE4Q], examples=[D(z, e) for z, e in NE1 + NE4]),
        card("话语语法: Expressions to Bring up or Elaborate on a Topic",
             "点 occasionally means “point” or “thing.” In conversation, we can use expressions with 点 to bring up a topic or to elaborate on a topic. Activity 5: A. Translate the following sentences into English, then share them with a classmate. B. Create five sentences using the expressions introduced above, then say their English equivalents to your partner, one at a time. Your partner will say them back to you in Chinese. The sentences, with my translations and my five sentences:",
             tables=[DT], examples=[D(z, e) for z, e in D5 + D5M]),
    ],
    exercises=[
        M("What does 呢 signal in 他呢，有时间也不想收拾?", "A pause that expresses contrast", ["A question", "A past action", "A command"], "the particle 呢 can be used to signal a pause to express contrast."),
        M("Which sentence adds 呢 in the middle to show contrast?", "冬天我喜欢滑雪，夏天呢，我喜欢游泳", ["冬天我喜欢滑雪呢夏天", "呢冬天我喜欢滑雪", "冬天我喜欢滑雪，夏天我喜欢游泳吗"], "冬天我喜欢滑雪，夏天呢，我喜欢游泳."),
        M("What does 还有一点 do?", "Brings up something new", ["Ends a talk", "Says goodbye", "Asks a question"], "还有一点 (one more thing)."),
        M("What does 就这一点来说 mean?", "In this regard", ["In the end", "At this time", "In this place"], "就这一点来说 (in this regard)."),
        M("Which expression shares one’s views?", "说几点看法", ["关于这一点", "还有一点", "在这一点上"], "说(or 谈)几点看法/想法/观点/意见."),
        M("What does 关于这一点 do?", "Says more about something already mentioned", ["Changes the topic", "Asks for help", "Ends the sentence"], "concerning this point."),
        F("今天一下班我就回家了，平时___，我会先去体育馆锻炼一会儿才回家。", "呢", ["吗", "们", "了"], "平时呢: contrast."),
        F("关于保护环境的问题，我讲两点自己的想___。", "法", ["字", "情", "吗"], "想法: idea."),
        F("在这一点___，咱们想得都一样。", "上", ["下", "里", "外"], "在这一点上."),
    ],
)

UNIT = unit("第二十八课 Presentation 2: 妈妈的电子邮件, 活动, 就是, 就像…说的, 排比句, 呢, 点", [L1, L2, L3, L4, L5])
