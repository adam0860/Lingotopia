"""Unit 68: Lesson 23 (Study in China) Presentation 3 and Area Studies from the book's texts: Luo Wen's passage about Tianjin, the four activities,
尽管…可是…, …极了, the existence words 有 and 是, compound-complex sentences, the skill-integration reports (Diyala, the hot pot journal), the
using-Chinese application information (Shanghai Chinese Medicine University), the vocabulary list and the Area Studies reading on international
students in China. Audio, pictures, videos and links are not included; numbers the book writes as digits are spelled out in the Chinese text;
answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('干净', 0, 'gan1'), ('还有', 0, 'hai2'), ('还是', 0, 'hai2'), ('还不', 0, 'hai2'), ('感觉', 1, 'jue2'), ('还得', 0, 'hai2'), ('还要', 0, 'hai2'), ('还是要', 0, 'hai2'), ('还拍', 0, 'hai2'), ('还常常', 0, 'hai2'), ('还了解', 0, 'hai2'), ('得预习', 0, 'dei3'), ('还得预', 1, 'dei3'), ('变得', 1, 'de5'), ('获得', 1, 'de2'), ('教那', 0, 'jiao1')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 3
R1 = ("我叫罗文，是泰国人，现在住在天津。天津是一个现代大都市，有很多西式风格的建筑，还有一条美丽的海河。尽管这儿的冬天特别冷，可是我却很喜欢，因为我没见过雪，所以每次下雪我都高兴极了。",
      "My name is Luo Wen; I am Thai and now live in Tianjin. Tianjin is a modern metropolis with many Western-style buildings and a beautiful Hai River. Although the winters here are especially cold, I like them very much, because I had never seen snow, so every time it snows I am extremely happy. (translation mine)")
R2 = ("我在天津医科大学学习中医和汉语。我住在留学生宿舍里，宿舍周围有很多树和花儿。我的房间不太大，但是很舒适，而且晚上可以看到城市的夜景。宿舍一楼有一个西餐厅和一个南亚餐厅。有时候我去这两个餐厅吃饭，有时候去中国学生食堂吃饭。我还常常和朋友们一起上街买菜，然后自己做饭。我觉得买菜、做饭是很有意思的事情。周末我会和朋友们一起去逛街。",
      "I study Chinese medicine and Chinese at Tianjin Medical University. I live in the international students’ dormitory, which is surrounded by many trees and flowers. My room is not very big but very comfortable, and in the evening I can see the city’s night view. On the first floor of the dorm there is a Western restaurant and a South Asian restaurant. Sometimes I eat at these two restaurants and sometimes at the Chinese students’ canteen. I also often go out with friends to buy groceries and then cook myself. I think buying groceries and cooking are very interesting things. On weekends I go shopping with friends. (mine)")
R3 = ("我们的课程很紧张，每天有四节中医课，还有两节语言课。下课以后，我先做作业，然后休息一下，听听音乐，看看书，或者和朋友聊一会儿天儿。六点半我吃晚饭。晚饭后我会跟室友散一会儿步。回到宿舍后，我不仅要复习一下当天学过的内容，而且还得预习一下第二天的课程，然后再和爸爸妈妈视频聊天。和他们说话是我每天最开心的事。虽然我每天都很忙，但是我非常喜欢这里的生活。我很感谢父母给我这个机会，让我来中国学习中医和汉语。",
      "Our courses are intense: every day there are four Chinese medicine classes and two language classes. After class I first do homework, then rest a bit, listen to music, read, or chat with friends for a while. At six thirty I eat dinner. After dinner I take a walk with my roommates for a while. After getting back to the dorm I not only have to review what I learned that day but also have to preview the next day’s lessons, and then video-chat with my parents. Talking with them is the happiest thing of my day. Although I am busy every day, I like life here very much. I am very grateful to my parents for giving me this opportunity to come to China to study Chinese medicine and Chinese. (mine)")
L1 = lesson(
    "Lesson 23 Presentation 3: Luo Wen studies Chinese medicine in Tianjin",
    "罗文在天津 · 下雪高兴极了 · 留学生宿舍 · 四节中医课 · 视频聊天",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Do you know anything about Tianjin? What can you say about it? B. Do you have experience learning foreign languages in other countries? If so, could you briefly share it? C. How much do you know about Chinese medicine? Do you know anyone who has learned Chinese medicine? (Four photographs are not included.)"),
        card("Presentation 3: 罗文在天津", "The book also prints the passage in traditional characters. The translations are mine.", examples=[D(*R1), D(*R2), D(*R3)]),
    ],
    exercises=[
        M("Where is Luo Wen from?", "Thailand", ["Korea", "Japan", "India"], "是泰国人."),
        M("Where does he live now?", "Tianjin", ["Beijing", "Shanghai", "Shenzhen"], "现在住在天津."),
        M("What river does Tianjin have?", "The Hai River", ["The Yellow River", "The Yangtze", "The Huangpu"], "一条美丽的海河."),
        M("Why does he like the cold winter?", "He had never seen snow", ["He likes cold food", "He can ski", "He likes wearing coats"], "因为我没见过雪."),
        M("What does he study at Tianjin Medical University?", "Chinese medicine and Chinese", ["Law and Chinese", "Computers", "Business"], "学习中医和汉语."),
        M("What can he see from his room in the evening?", "The city’s night view", ["The river", "A forest", "A playground"], "晚上可以看到城市的夜景."),
        M("What restaurants are on the dorm’s first floor?", "A Western and a South Asian restaurant", ["Two Chinese restaurants", "A hot pot place", "A bakery"], "一个西餐厅和一个南亚餐厅."),
        M("What does he think about buying groceries and cooking?", "Very interesting", ["Boring", "Too tiring", "Too expensive"], "是很有意思的事情."),
        M("How many Chinese medicine classes does he have each day?", "Four", ["Two", "Six", "One"], "每天有四节中医课."),
        M("What does he do right after class?", "Homework", ["Sleep", "Dinner", "Shopping"], "下课以后，我先做作业."),
        M("What is the happiest thing of his day?", "Talking with his parents", ["Eating dinner", "Seeing snow", "Cooking"], "和他们说话是我每天最开心的事."),
        F("尽管这儿的冬天特别冷，可是我___很喜欢。", "却", PART, "可是…却…."),
        F("每次下雪我都高兴___了。", "极", PART, "高兴极了."),
        F("我不仅要复习一下当天学过的内容，而且还得___习一下第二天的课程。", "预", PART, "预习: preview."),
    ],
)

# ------------------------------------------------------------------ 2. activities
YX = table(["和“医”组成的词 (mine)", "和“习”组成的词 (mine)"], [["医生", "学习"], ["医院", "复习"], ["中医", "预习"], ["医科", "练习"], ["医学", "习惯"], ["看医生", "实习"], ["医药", "自习"], ["西医", "习作"]], title="Activity 3: words with 医 and 习 (the book shows two bubble diagrams; the words are mine)", say=[0, 1])
A4 = [("罗文现在住在天津，他特别喜欢在天津这个大都市生活。", "1. Luo Wen now lives in Tianjin and especially likes living in this big city, Tianjin. (key mine: 都市)"), ("他住的公寓的周围有各种各样的建筑，既有古代的，也有现代的，而且风格万千，形式多样，不仅有中式的，也有西式的。", "2. Around his apartment there are all kinds of buildings, both ancient and modern, with a thousand styles and many forms, not only Chinese-style but also Western-style. (建筑, 现代, 风格, 西式; 周围 is already printed in the book’s text)"), ("刚到天津时，罗文每个周末都逛街、拍照，拍视频，然后发给他父母。", "3. When he first arrived in Tianjin, Luo Wen went shopping, took photos and shot videos every weekend and then sent them to his parents. (逛街, 视频)"), ("每次跟父母通话时，他聊天的内容差不多都是关于天津的建筑。", "4. Every time he talked with his parents, what he chatted about was almost always about the buildings of Tianjin. (内容)")]
L2 = lesson(
    "Lesson 23 Presentation 3 activities: questions, word building and the buildings of Tianjin",
    "Activities 1 to 4 · 医生 学习 · 都市 建筑 现代 风格 西式 · 逛街 视频 内容",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Global listening: listen to Presentation 3 and answer: 1. What is the main idea of this presentation? (Luo Wen’s study and life in Tianjin) 2. Who is the speaker? (Luo Wen, a Thai student). B. Detailed listening: 1. 天津是个什么样的城市？ (a modern metropolis with many Western-style buildings and a beautiful river) 2. 罗文为什么喜欢天津的冬天？ (he had never seen snow) 3. 罗文住的地方怎么样？ (an international students’ dorm with trees and flowers, a small but comfortable room and a night view) 4. 他在哪儿吃饭？ (the dorm’s Western and South Asian restaurants and the Chinese students’ canteen) 5. 他喜欢做饭吗？你怎么知道？ (yes, he thinks buying groceries and cooking are very interesting) 6. 下课以后，他做什么？ (homework, rest, music, reading or chatting) 7. 晚饭以后，他做什么？ (a walk with roommates, review, preview, a video chat with his parents). C. Pair up, discuss and share. (Audio, not included; the answers in brackets are from the text.)"),
        card("Activity 2 (Listening, Writing and Speaking)",
             "A. Listen to Passage 1 and answer: 1. Where is Bill? What is he doing there? 2. What is the city like where Bill is staying? Provide three details. B. Pair up and discuss. C. Listen to Passage 2 and answer: 1. 比尔住在哪里？他住的地方怎么样？ 2. 比尔在哪儿吃饭？吃饭的地方怎么样？ 3. 比尔做饭的手艺怎么样？你怎么知道的？ D. Pair up and discuss. E. Talk about your dorm and cafeteria with your partner. F. Listen to Passage 3 and write Bill’s daily activities (上什么课, 下课以后, 晚饭后, 周末). G. Pair up and discuss Bill’s schedule. H. Talk about your schedule with your partner. (Audio, not included.)"),
        card("Activity 3 (Speaking and Writing): 组词练习",
             "A. Pair up and fill in the bubbles with the words that can go with 医 and 习. B. Report your team’s work to the class and compare it with the other team’s work. Note the words that you didn’t write.",
             tables=[YX]),
        card("Activity 4 (Reading, Speaking and Writing)",
             "A. Pair up, read the passage, and complete it using the words listed: 现代, 都市, 西式, 建筑, 内容, 风格, 视频, 逛街, 周围. B. Pair up and check your work. C. Pair up and create your own story using the above words. Share your story with the class. The book’s passage has eight blanks for nine words, since 周围 is already printed in the text; the completed passage (key mine):",
             examples=[D(z, e) for z, e in A4]),
    ],
    exercises=[
        M("Which word fills “大___生活”?", "都市", ["建筑", "风格", "视频"], "大都市."),
        M("Which word fills “各种各样的___”?", "建筑", ["内容", "视频", "逛街"], "各种各样的建筑."),
        M("Which word fills “既有古代的，也有___的”?", "现代", ["西式", "都市", "周围"], "古代 / 现代."),
        M("Which word fills “___万千，形式多样”?", "风格", ["内容", "视频", "建筑"], "风格万千."),
        M("Which word fills “每个周末都___、拍照”?", "逛街", ["视频", "内容", "西式"], "逛街."),
        M("Which word fills “拍___”?", "视频", ["风格", "建筑", "都市"], "拍视频."),
        M("Which compound contains 医?", "中医", ["复习", "实习", "练习"], "中医."),
        M("Which compound contains 习?", "预习", ["医院", "医生", "医科"], "预习."),
        F("他聊天的___容差不多都是关于天津的建筑。", "内", PART, "内容: content."),
        F("罗文每个周末都逛街、拍照，拍___频，然后发给他父母。", "视", PART, "视频: video."),
    ],
)

# ------------------------------------------------------------------ 3. 尽管, 极了
JG = [("尽管天津的冬天特别冷，可是我却很喜欢这儿的冬天。", "1. Although winter in Tianjin is especially cold, I like the winter here."), ("尽管我没有太多的钱，可是我生活得很幸福。", "2. Although I don’t have much money, I live very happily."), ("尽管她学习很努力，可是她却没有很大的进步。", "3. Although she studies very hard, she has not made great progress. (是 can be omitted after 可, and 却 or 还是 can be added after 可是)"), ("尽管中文很难，可是我还是要学。", "4. Although Chinese is hard, I still want to learn it.")]
MT = [("尽管我已经学了四个月的中文了，可我的发音还是不太好。", "1 → d. Although I have studied Chinese for four months, my pronunciation is still not very good. (key mine)"), ("尽管玛丽学习很努力，可是她的单元考试没有通过。", "2 → f. Although Mary studies hard, she didn’t pass her unit test."), ("尽管有时候我妈妈的血压不太高，可是医生让她天天吃降压药。", "3 → g. Although my mother’s blood pressure is not too high sometimes, the doctor has her take blood-pressure medicine every day."),
      ("尽管天天开车上班对身体不好，可是买车的人还是越来越多。", "4 → b. Although driving to work every day is bad for health, more and more people still buy cars."), ("尽管老张今天感觉不舒服，可他还是要去上班。", "5 → a. Although Lao Zhang feels unwell today, he still has to go to work."), ("尽管喝酒对身体不好，可很多人还是喜欢喝。", "6 → c. Although drinking is bad for health, many people still like to drink."), ("尽管今天早上会下雨，可我们还得去操场集合。", "7 → e. Although it will rain this morning, we still have to go to the playground to assemble. (the book prints no comma after 下雨)")]
JL = [("罗文很喜欢雪，每次下雪，他都高兴极了。", "1. Luo Wen likes snow very much; every time it snows he is extremely happy."), ("考试那天，我紧张极了，结果考得不好。", "2. On the exam day I was extremely nervous and as a result did not do well."), ("他跑得快极了。", "3. He runs extremely fast. (Verb + 得 + adjective + 极了)"), ("大卫说中文说得好极了。", "4. David speaks Chinese extremely well."), ("这个小孩可爱极了。", "The book’s example for Activity 2: This child is extremely cute."), ("我爷爷今年已经八十九岁了，可他的身体棒极了。", "Activity 2C’s example: My grandfather is already eighty-nine this year but his health is extremely good. (the book writes 89 in digits)")]
L3 = lesson(
    "Lesson 23 Presentation 3 grammar: 尽管…可是… and …极了",
    "尽管…，可是… · 可是…却/还是… · 高兴极了 · 快极了 · 好极了",
    requires=[],
    cards=[
        card("The Construction 尽管……，可是……",
             "The conjunction 尽管 means “although” or “even though” and is a little stronger than 虽然 in emphasizing contrast. It can be followed by 可是, which further emphasizes a shift in meaning in the second part of a statement. In the construction “尽管……，可是……”, 是 can be omitted. In addition, 却 or 还是 can be added after 可是.",
             examples=[D(z, e) for z, e in JG]),
        card("Activity 1 (Reading and Speaking)",
             "A. Pair up and match the statements in Column A with those in Column B to make complete sentences. Write the letters from Column B in the table. Column B: a. 可他还是要去上班。 b. 可是买车的人还是越来越多。 c. 可很多人还是喜欢喝。 d. 可我的发音还是不太好。 e. 可我们还得去操场集合。 f. 可是她的单元考试没有通过。 g. 可是医生让她天天吃降压药。 B. Pair up, read the above sentences aloud and translate them into English. C. Students take turns creating their own sentences using “尽管……，可是……”. The book gives no key; my matching (1–d, 2–f, 3–g, 4–b, 5–a, 6–c, 7–e):",
             examples=[D(z, e) for z, e in MT]),
        card("The Expression ……极了",
             "The expression ……极了 is a degree complement and is used to intensify both positive and negative adjectives. It means “extremely” or “very” and is used in spoken, colloquial Chinese. Pattern: Subject + Adjective + 极了. As a degree complement, the structure “adjective + 极了” can be placed after 得: Subject + Verb + 得 + Adjective + 极了.",
             examples=[D(z, e) for z, e in JL]),
        card("Activity 2 (Writing and Speaking)",
             "A. Pair up and talk about the images using the expression “……极了” and write your comments beneath each image (six photographs: not included). Example: 这个小孩可爱极了。 B. Share your group work with the class. C. Pair up and discuss your family members using ……极了. Each partner says at least three sentences. Example: 我爷爷今年已经八十九岁了，可他的身体棒极了。"),
    ],
    exercises=[
        M("What does 尽管 mean?", "Although, even though", ["Because", "If", "Unless"], "尽管: although."),
        M("How does 尽管 compare with 虽然?", "A little stronger in emphasizing contrast", ["Weaker", "The same", "Only used in writing"], "a little stronger than 虽然."),
        M("What may be added after 可是?", "却 or 还是", ["了 or 过", "吗 or 呢", "就 or 才"], "却 or 还是."),
        M("What does 尽管中文很难，可是我还是要学 mean?", "Although Chinese is hard, I still want to learn it", ["Chinese is easy so I learn it", "I will not learn Chinese", "I learned Chinese yesterday"], "尽管…可是…还是…."),
        M("Match: 尽管喝酒对身体不好，", "可很多人还是喜欢喝", ["可我们还得去操场集合", "可是她的单元考试没有通过", "可他还是要去上班"], "6 → c."),
        M("Match: 尽管玛丽学习很努力，", "可是她的单元考试没有通过", ["可我的发音还是不太好", "可他还是要去上班", "可是买车的人还是越来越多"], "2 → f."),
        M("What does ……极了 mean?", "Extremely", ["A little", "Not at all", "Probably"], "极了: extremely."),
        M("Which is correct?", "他跑得快极了", ["他跑快极了得", "他得跑快极了", "他跑极了得快"], "V + 得 + adj + 极了."),
        M("What does 考试那天，我紧张极了 mean?", "I was extremely nervous on exam day", ["I was calm", "I forgot the exam", "I took no exam"], "紧张极了."),
        F("尽管中文很难，可是我还___要学。", "是", PART, "还是."),
        F("罗文很喜欢雪，每次下雪，他都高兴___了。", "极", PART, "高兴极了."),
    ],
)

# ------------------------------------------------------------------ 4. 有和是, 多重复句
YS = [("我家旁边有一个公园。", "1. There is a park next to my house. (有 only denotes what exists in a place)"), ("我家旁边是一个公园。", "2. Next to my house is a park. (是 also specifies what it is)"), ("我家旁边有一个公园。是什么公园？是景山公园。", "A: There is a park next to my house. B: What park is it? A: (Next to my house) is Jingshan Park."),
      ("孩子前边有个人。", "Right: There is a person in front of the child."), ("孩子前边有妈妈。", "Wrong: with 有 the object is usually a general reference, not “the mother”."), ("孩子前边是妈妈。", "Right: In front of the child is the mother."), ("妈妈在孩子前面。", "Right: The mother is in front of the child.")]
S3 = [("学校门口有一辆小汽车。", "1. 学校门口是一辆小汽车 — false. Correction (mine): 有, because the car is a general reference: There is a car at the school gate."), ("百货大楼前面有一个广场。", "2. 百货大楼前面有一个广场 — true: There is a square in front of the department store."), ("我家房子前面有一棵树。", "3. 我家房子前面是一棵树 — false. Correction (mine): 有: There is a tree in front of my house."), ("我家的树上有两只小鸟。", "4. 我家的树上是两只小鸟 — false. Correction (mine): 有: There are two little birds in my tree."),
      ("图书馆旁边是一片小树林。", "5. 图书馆旁边是一片小树林 — true: Next to the library is a small wood. (key mine)"), ("这个包里有手机和钱包。", "6. A: 这个包里有什么东西？ B: 这个包里有手机和钱包。 — true: What is in this bag? There is a phone and a wallet.")]
S4 = [("图书馆里有很多中文报纸。", "1. There are a lot of Chinese newspapers in the library. (有; Activity 4, key mine)"), ("卧室旁边是一个洗手间。", "2. Next to the bedroom is a bathroom. (是)"), ("你左边是谁？", "3. Who is on your left? (是)"), ("邮局对面有一个银行。", "4. There is a bank across from the post office. (有)"), ("天津有很多西式建筑。", "5. There is a lot of western-style architecture in Tianjin. (有)"), ("超市对面是一个咖啡店。", "6. Across from the supermarket is a coffee shop. (是)")]
CL = table(["关系", "关联词"], [["递进关系 (progressive)", "不但/不仅…，而且/还/也/甚至还…"], ["转折关系 (transitional)", "虽然/尽管…，但是/却/可是…"], ["因果关系 (causative)", "因为/由于…，所以…"]], title="The compound-complex sentence 多重复句: three types", say=[1])
CE = [("刚开始是有点儿难，可是我很有兴趣，就不觉得那么难了，而且越学越爱学。", "1. [转折关系] 可是…就不觉得那么难了 + [递进关系] 而且…: At the beginning it was a bit hard, but I was very interested and did not find it so hard, and moreover the more I learned the more I loved learning."), ("尽管这儿的冬天特别冷，可是我却很喜欢，因为我没见过雪，所以每次下雪我都高兴极了。", "2. [转折关系] 尽管…可是…却… + [因果关系] 因为…所以…: Although winter here is especially cold, I like it, because I had never seen snow, so every time it snows I am extremely happy.")]
A5 = [("罗文的房间不太大，但是很舒适，而且晚上可以看到城市的夜景。", "1. 但是 = transitional; 而且 = progressive. Luo Wen’s room is not very big but very comfortable, and also in the evening he can see the city’s night view. (Activity 5, mine)"), ("尽管“老外”是很友好的称呼，但是我还是不喜欢别人叫我“老外”，因为他们用“老外”这个词的时候，就指着我，让别人看我，让我感觉很不舒服。", "2. 尽管…但是 = transitional; 因为 = causative. Although “laowai” is a friendly term, I still don’t like being called “laowai”, because when they use the word they point at me and make others look at me, which makes me feel very uncomfortable."), ("在西方国家，人们不仅不问别人的年龄，而且也不问赚多少钱，但是在中国，大家都喜欢问，不过这是中国人向你表示友好的一种方式。", "3. 不仅…而且 = progressive; 但是 and 不过 = transitional. In Western countries people not only don’t ask others’ ages but also don’t ask how much they earn, but in China everyone likes to ask; however, it is a way for Chinese to show you friendliness.")]
L4 = lesson(
    "Lesson 23 Presentation 3 grammar: 有 and 是 for existence, and compound-complex sentences",
    "旁边有一个公园 · 旁边是景山公园 · 孩子前边有个人 · 递进 转折 因果 · 不仅…而且… 虽然…但是…",
    requires=[],
    cards=[
        card("The Existence Words 有 and 是",
             "有 is used to indicate the existence of someone or something in a particular place: Location Word + 有 + Noun/Noun Phrase/Someone. 是 is used to indicate existence when we know there is someone or something in a particular place, but we want to know specifically who the person or what the thing is: Location Word + 是 + Noun/Noun Phrase/Someone. 有 only denotes what exists in a certain place, while a sentence that uses 是 not only indicates that a thing exists in a certain place, but also further specifies what that thing is. The object of a sentence indicating existence with 有 is usually a general reference, while the object of a sentence indicating existence with 是 is usually a specific reference.",
             examples=[D(z, e) for z, e in YS]),
        card("Activity 3 (Reading and Speaking)",
             "Pair up and mark the following statements as either True or False. Correct any false statements and explain why they are false. The book prints the six statements without a key; my answers and corrections:",
             examples=[D(z, e) for z, e in S3]),
        card("Activity 4 (Writing and Speaking)",
             "A. Translate the following sentences into Chinese by using 有 or 是: 1. There are a lot of Chinese newspapers in the library. 2. Next to the bedroom is a bathroom. 3. Who is on your left? 4. There is a bank across from the post office. 5. There is a lot of western-style architecture in Tianjin. 6. Across from the supermarket is a coffee shop. B. Pair up and share your translations and explain why you used 有 or 是. My Chinese:",
             examples=[D(z, e) for z, e in S4]),
        card("The Compound-Complex Sentences 多重复句",
             "The compound-complex sentence 多重复句 has at least two sentences. There are several types of compound-complex sentences in Chinese that indicate different relationships such as progressive relation (递进复句), transitional relation (转折复句) and causative relation (因果复句) etc.",
             tables=[CL], examples=[D(z, e) for z, e in CE]),
        card("Activities 5 and 6",
             "Activity 5 (Reading, Writing and Speaking): A. Read the sentences and highlight the conjunctions. Mark them with a progressive relation (递进复句), a transitional relation (转折复句) or a causative relation (因果复句). B. Pair up and explain the relationship between the clauses in each sentence. My answers:",
             examples=[D(z, e) for z, e in A5]),
        card("Activity 6 (Listening, Writing and Speaking)",
             "A. Listen to six compound-complex sentences and translate them into English. B. Pair up and check your translations with your partner. Discuss the functions of the compound-complex sentences. C. With your partner, create three compound-complex sentences by using the following patterns or conjunctions: 不但/不仅…，而且/还/也/甚至还…; 虽然/尽管…，但是/却/可是…; 因为/由于…，所以…. D. Share your team’s work with the class. (Audio, not included.)"),
    ],
    exercises=[
        M("Which word indicates mere existence in a place?", "有", ["是", "在", "把"], "有 denotes what exists."),
        M("Which word also specifies what the thing is?", "是", ["有", "给", "对"], "是 specifies."),
        M("Which is correct?", "孩子前边有个人", ["孩子前边有妈妈", "孩子前边是个人 (generic)", "孩子前边有是妈妈"], "有 + general reference."),
        M("Which is also correct?", "孩子前边是妈妈", ["孩子前边有妈妈", "孩子前边有了妈妈", "孩子前边妈妈有"], "是 + specific reference."),
        M("Which sentence is correct for “There is a car at the school gate”?", "学校门口有一辆小汽车", ["学校门口是一辆小汽车", "学校门口有是一辆小汽车", "学校门口在一辆小汽车"], "general reference → 有."),
        M("Which sentence is correct for “Who is on your left?”", "你左边是谁？", ["你左边有谁？", "你左边在谁？", "你谁在左边？"], "Asking for a specific person → 是."),
        M("Which type is 不仅…而且…?", "Progressive", ["Transitional", "Causative", "Conditional"], "递进."),
        M("Which type is 虽然…但是…?", "Transitional", ["Progressive", "Causative", "Additive"], "转折."),
        M("Which type is 因为…所以…?", "Causative", ["Progressive", "Transitional", "Hypothetical"], "因果."),
        F("我家旁边有一个公园。——___什么公园？", "是", PART, "是什么公园: which park is it."),
        F("___管这儿的冬天特别冷，可是我却很喜欢。", "尽", PART, "尽管: although."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
DY1 = ("在四川成都一家中医医院，一位黑人中医突然火了起来。他叫迪亚拉，来自非洲马里共和国。他皮肤黑黑的，牙齿很白，穿着医院的白衣服，口袋中插着一支笔，很熟练地给病人诊脉、针灸。",
       "Paragraph 1: In a Chinese medicine hospital in Chengdu, Sichuan, a Black doctor of Chinese medicine suddenly became famous. His name is Diyala and he is from the Republic of Mali in Africa. His skin is dark and his teeth are very white; he wears the hospital’s white uniform with a pen in his pocket and very skillfully takes patients’ pulses and does acupuncture. (translation mine; adapted in the book from an article by the reporter Guo Linlin of Beijing Youth Daily; the book glosses 迪亚拉, 皮肤, 诊脉 and 针灸 in pinyin, which I left out)")
DY2 = ("迪亚拉在一九八四年从马里医学院毕业后就来到中国学习中医。在中国的三十多年中，他先后在北京、广州和成都等城市学习，获得了博士后学位。他是中国第一个有中医学博士的外国人。为了学习中医，迪亚拉阅读了很多中国的古书，翻译汉语词典，听中国古代的戏剧，逛博物馆等。他不仅精通中医，还了解中国文化，而且汉字写得也特别好。",
       "Paragraph 2: After graduating from the Mali medical school in 1984, Diyala came to China to study Chinese medicine. In more than thirty years in China he studied successively in Beijing, Guangzhou, Chengdu and other cities and obtained a post-doctoral degree. He is the first foreigner in China with a doctorate in Chinese medicine. To study Chinese medicine, Diyala read many ancient Chinese books, translated Chinese dictionaries, listened to ancient Chinese drama and visited museums. He is not only proficient in Chinese medicine but also understands Chinese culture, and he writes Chinese characters especially well too. (mine; the book writes 1984 in digits)")
DY3 = ("最近，北京青年报记者采访了他。记者问他在中国学中医有没有感到很难。他说，“为了能看懂中医的古书，我学了一年半的汉语。除了和中国同学一起上课外，我自己还要努力学习。我买了一些工具书，背或者翻译这些书，不懂就去问老师，和老中医交流学习。”记者又问他有没有病人不愿意让他看病或者不相信他。迪亚拉说，“刚开始工作的时候，很少有病人找我看病，十天才看过两个病人。后来，大家知道我看病很好，我才开始变得每天都很忙。”",
       "Paragraph 3: Recently a reporter from Beijing Youth Daily interviewed him. The reporter asked whether he found it very hard to study Chinese medicine in China. He said, “To be able to read the ancient books of Chinese medicine I studied Chinese for a year and a half. Besides attending class with my Chinese classmates I also had to study hard myself. I bought some reference books, memorized or translated them, asked teachers when I didn’t understand, and exchanged ideas with old Chinese doctors.” The reporter also asked whether any patients were unwilling to let him treat them or didn’t trust him. Diyala said, “When I first started working very few patients came to me; in ten days I saw only two patients. Later everyone knew that I treat patients well and only then did I start to be busy every day.” (mine)")
DY4 = ("现在，迪亚拉已经在成都结婚了。他和太太有两个孩子。他打算在非洲成立一个中医治疗中心，教那里的医生用中医给病人看病。",
       "Paragraph 4: Now Diyala is already married in Chengdu. He and his wife have two children. He plans to set up a Chinese medicine treatment center in Africa and teach the doctors there to treat patients with Chinese medicine. (mine)")
HG = [("我的朋友何雷学过中文，但他的中文没我好。", "1. My friend He Lei has studied Chinese but his Chinese is not as good as mine. (T/F statements for Activity 3B; the book prints no key; audio not included)"), ("我的朋友何雷不喜欢吃辣的火锅因为他会拉肚子。", "2. My friend He Lei doesn’t like spicy hot pot because it gives him diarrhea."), ("因为是夏天，所以火锅店里的人不多。", "3. Because it is summer there are not many people in the hot pot restaurant."), ("我们吃了很多蔬菜，肉和海鲜，感觉非常饱。", "4. We ate a lot of vegetables, meat and seafood and felt very full."), ("我的朋友何雷说他以后也来中国学中文。", "5. My friend He Lei says he will also come to China to study Chinese later.")]
L5 = lesson(
    "Lesson 23 Presentation 3 skill integration: Ma Ke, the doctor from Mali and a hot pot journal",
    "力马克学中文 · 迪亚拉在成都 · 中医 针灸 · 火锅日记",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Listen to a recording about an American student and write the main idea. B. Transcribe the missing words in Pinyin and translate them into English: 1. 力马克是一个…的美国年轻人。他的老家在美国…州的…。 2. 学了中文以后，他慢慢地对中国的…和文化有了兴趣，常常看中国的…和…。 C. Pair up and discuss. D. Listen again and answer: 1. 力马克除了会中文，他还会哪种外语？你怎么知道的？ 2. 是什么事情让他开始学中文的？ 3. 学了中文以后，他对什么感兴趣？他喜欢看什么？ 4. 来中国学中文以后，他的中文水平怎么样？ 5. 大家说马克的中文很好，他是怎么回答的？ 6. 马克每天都把自己的生活和学习情况写下来，这样做有什么好处？ E. Discuss and share. F. Discuss: 1. 力马克在学中文以前学过日语，这对他学汉语有什么帮助？ 2. 力马克喜欢中国历史和哲学，也喜欢看中国新闻和电影，你觉得这对他学中文有什么好处？ 3. 力马克每天都把自己的生活和学习写下来。你是不是也这样？你觉得这么做对你学中文有什么帮助？ (Audio, not included.)"),
        card("Activity 2 (Reading, Writing and Speaking)",
             "A. In two groups, read the following news report about Diyala from the Republic of Mali. Group A reads Paragraphs 1 and 2 and Group B reads Paragraphs 3 and 4. Summarize each passage and note any unfamiliar words. B. Pair up with a member of the other group. Exchange your summary and discuss the meanings of any unfamiliar words. C. Discuss: 1. 为什么迪亚拉在中国火了？ 2. 为了学好中医，他是怎么做的？ 3. 学中医对他来说难不难？你是怎么知道的？ 4. 他是一个外国人，病人喜欢让他看病吗？ 5. 现在他的生活情况怎么样？以后有什么打算?",
             examples=[D(*DY1), D(*DY2), D(*DY3), D(*DY4)]),
        card("Activity 3 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the journal of an American student studying in China (two photographs not included) and write down the main ideas. New word: 火锅 (huǒguō; hot pot). B. Listen again and mark the statements True or False. C. Pair up and discuss; read the script if necessary. D. Write the meanings of the following words and discuss with your partner: 少数民族 shǎoshù mínzú, 研究 yánjiū, 饱 bǎo. E. With your partner, talk about your experience eating hot pot. The five statements:",
             examples=[D(z, e) for z, e in HG]),
    ],
    exercises=[
        M("Where was Diyala from?", "The Republic of Mali in Africa", ["Egypt", "Nigeria", "Kenya"], "来自非洲马里共和国."),
        M("In which city’s hospital did he become famous?", "Chengdu", ["Beijing", "Shanghai", "Guangzhou"], "在四川成都一家中医医院."),
        M("What does he do skillfully for patients?", "Takes pulses and does acupuncture", ["Surgery", "X-rays", "Dentistry"], "诊脉、针灸."),
        M("When did he graduate from the Mali medical school?", "1984", ["1948", "2004", "1994"], "一九八四年."),
        M("What is he the first of?", "The first foreigner in China with a doctorate in Chinese medicine", ["The first Mali doctor", "The first teacher", "The first cook"], "中国第一个有中医学博士的外国人."),
        M("How long did he study Chinese before reading the old medical books?", "A year and a half", ["Ten years", "One month", "Three weeks"], "我学了一年半的汉语."),
        M("How many patients did he see in his first ten days?", "Two", ["Twenty", "None", "Ten"], "十天才看过两个病人."),
        M("What does he plan to do in Africa?", "Set up a Chinese medicine treatment center", ["Open a school of languages", "Open a restaurant", "Write a book"], "成立一个中医治疗中心."),
        M("How many children does he have?", "Two", ["One", "Three", "None"], "他和太太有两个孩子."),
        F("为了能看懂中医的古书，我学了一年___的汉语。", "半", PART, "一年半."),
        F("他不仅精___中医，还了解中国文化。", "通", PART, "精通: be proficient in."),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese
SH = table(["项目", "内容"], [["招收学生", "希望提高汉语水平，对中医有兴趣并计划学习中医的外国学生"], ["主要课程", "综合汉语，中医汉语阅读，推拿，保健体育"], ["申请时间", "二零二一年一月十日前"], ["学习时间", "二零二一年九月至十二月"], ["上课地点", "蔡伦路一二零零号上海中医药大学国际教育学院浦东校区"], ["入学条件", "身体健康，持国外护照，高中或高中以上毕业，汉语水平考试成绩三级一百八十分以上"], ["收费", "报名费：人民币四百五十元每人；学费：人民币一万一千元每学期（包课本费）；住宿费：住校内需要申请，具体费用请看附件；也可以住校外。"], ["报名材料", "护照首页，高中或高中以上学历毕业证书，汉语水平考试证书，电子照片"], ["联系方式", "电话号码：五一三二，二二五五；咨询地点：上海中医药大学国际教育学院二楼招生办公室（二三零室）；地址：上海市浦东新区张江高科技园区蔡伦路一二零零号"]],
           title="Activity 1A: 上海中医药大学国际学生语言生招生信息 (the book writes the dates and numbers in digits and “HSK” after 汉语水平考试, which I spelled out or left out; the postcode is blank in the book)", say=[1])
L6 = lesson(
    "Lesson 23 Presentation 3 using Chinese in context: applying to a Chinese medicine university",
    "上海中医药大学 · 申请时间 学习时间 · 入学条件 收费 · 艾伦的学习问题 · 菜市场的故事",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking)",
             "Scenario: you are going to graduate from the Chinese basic course and would like to study Chinese medicine in China after you graduate. You found application information for Shanghai Chinese Medicine University and would like to know more about the application process, the courses, expenses etc., so you call the university to obtain the information you need. A. Pair up and read the application information with your partner. Note any unfamiliar words and look them up in your dictionary. B. Role-play: call the university to inquire about the application process, courses, expenses etc. Your partner plays the university assistant. You want to know: 你们都有什么课程？每天上几节课？你们的老师怎么样？都是中医大夫吗？学校的宿舍怎么样？几个人一个房间？有单人房吗？怎么收费？学校有没有食堂？饭菜怎么样？学校有体育馆吗？里面的设施怎么样？报名的钱必须付人民币吗？怎么付钱？ The school wants to know: 你为什么要学中医？你学了多长时间的汉语？你的汉语水平怎么样？你喜欢住在学校还是校外？在我们学校学完以后，你有什么计划？ C. Report to the class whether you would apply to this school and explain your reasons.",
             tables=[SH]),
        card("Activities 2 and 3 (Listening, Reading, Writing and Speaking)",
             "Activity 2. Scenario: you are studying Chinese at a university in China. One of your classmates tells you about his difficulties learning Chinese. Your teacher brings up the student’s difficulties with the class for discussion in hopes that they can contribute some suggestions to help him. A. Listen to Allen’s monolog and summarize his learning difficulties (艾伦有哪些学习上的问题？). B. Pair up and check; read the script if necessary. C. Pair up and make suggestions you think will help Allen overcome his learning difficulties. D. Each pair presents its suggestions to the class. Activity 3. A. Listen to the story and write a summary. B. Pair up and discuss; read the script if necessary. C. Pair up and talk about a time when you studied in a foreign country or in another city. Did you have similar experiences? Did you visit a farmer’s market, talk to foreigners or talk to vendors? Share one of your most interesting experiences in class. (Audio and photographs are not included.)"),
    ],
    exercises=[
        M("Who does the university admit?", "Foreign students who want to improve Chinese and are interested in Chinese medicine", ["Only Chinese students", "Only doctors", "Anyone with money"], "招收学生."),
        M("Which is a main course?", "推拿", ["计算机", "法律", "金融"], "主要课程: 综合汉语，中医汉语阅读，推拿，保健体育."),
        M("When is the application deadline?", "Before January 10, 2021", ["Before September 2021", "Before December 2020", "Anytime"], "二零二一年一月十日前."),
        M("When is the study period?", "September to December 2021", ["January to March", "June to July", "The whole year"], "二零二一年九月至十二月."),
        M("Where does the course take place?", "The Pudong campus of the International Education College", ["Beijing", "Hangzhou", "Online"], "浦东校区."),
        M("What HSK level is required?", "Level 3, 180 points or above", ["Level 1", "Level 6", "No test"], "三级一百八十分以上."),
        M("How much is the application fee?", "450 yuan per person", ["4,500 yuan", "45 yuan", "11,000 yuan"], "四百五十元每人."),
        M("How much is the tuition?", "11,000 yuan per semester, textbooks included", ["450 yuan", "1,100 yuan", "110,000 yuan"], "一万一千元每学期（包课本费）."),
        M("Can students live off campus?", "Yes", ["No", "Only first-year students", "Only with permission of the police"], "也可以住校外."),
        M("Which is a required application document?", "A passport first page and a high-school diploma", ["A driver’s license", "A bank statement", "A marriage certificate"], "护照首页，高中或高中以上学历毕业证书."),
        F("申请时间：二零二一年一月十日___。", "前", PART, "前: before."),
        F("学费：人民币一万一千元每学期，___课本费。", "包", PART, "包: includes."),
    ],
)

# ------------------------------------------------------------------ 7. vocabulary
L7 = vocab_lesson("Lesson 23 Presentation 3 vocabulary", "19 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English; its glosses are kept as printed.", VOC3)

# ------------------------------------------------------------------ 8. area studies
L8 = lesson(
    "Lesson 23 Area Studies: International Students in China",
    "来华留学生 · 学生人数 · 来源国 · 最受欢迎的地方 · 为什么选择中国",
    requires=[],
    cards=[
        card("International Students in China (1)",
             "The number of international students studying in China has been increasing over the past decade, along with the number of foreigners working and traveling in China. According to the Chinese Ministry of Education statistics, in 2018 a total of 492,185 foreign students from 196 countries studied in 1,004 higher education institutions in 31 regions across the country. This is an increase of 3,013 people over 2017, just 0.62%. (The above data does not include Hong Kong, Macao and Taiwan.) In 2016, China was the third largest receiver of international students globally, with 442,773 international students. By 2018 this number grew to 492,185 (10.49% growth from 2017). In 2018 China was the most popular country in Asia for international students and the second most popular in the world. The number of international students in China has grown steadily since 2003, with no impact from the rise of terrorism or the 2008 global financial crisis. In contrast to the reported decline of enrollment in the U.S. and the UK, China’s international student population continues to increase. China is now the leading destination for Anglophone African students. (A chart of international students in China, 2003–2017, from Wikipedia, is not included.)"),
        card("(2) Statistics by country in 2018",
             "Statistics of International Students by Continent in 2018. All African countries grouped together: 81,562 students (2017: 61,594), 16.57% of the total. By country (rank in 2018: country, students in 2018, students in 2017, percent of total in 2018, rank in 2017): 1. South Korea, 50,600 (70,540), 10.28%, rank 1. 2. Thailand, 28,608 (23,044), 5.81%, rank 2. 3. Pakistan, 28,023 (18,626), 5.69%, rank 3. 4. India, 23,192 (18,717), 4.71%, rank 5. 5. United States, 20,996 (23,838), 4.27%, rank 4. 6. Russia, 19,239 (17,971), 3.91%, rank 6. 7. Indonesia, 15,050 (14,714), 3.06%, rank 8. 8. Laos, 14,645, 2.98%. 9. Japan, 14,230 (13,595), 2.89%, rank 7. 10. Kazakhstan, 11,784 (13,996), 2.39%, rank 9. 11. Vietnam, 11,299 (10,639), 2.30%. 12. Bangladesh, 10,735, 2.18%. 13. France, 10,695, 2.17%. 14. Mongolia, 10,158, 2.06%. 15. Malaysia, 9,479, 1.93%. (Source: Wikipedia; the book’s printed figure for South Korea’s 2018 total, 50,600, is smaller than its 2017 figure of 70,540, as printed.)"),
        card("(3) Top locations, degrees and scholarships",
             "The Top 10 Locations for International Students: 1. Beijing 80,786; 2. Shanghai 61,400; 3. Jiangsu 45,778; 4. Zhejiang 38,190; 5. Liaoning 27,879; 6. Tianjin 23,691; 7. Guangdong 22,034; 8. Hubei 21,371; 9. Yunnan 19,311; 10. Shandong 19,078. Provinces (regions) with more than 10,000 people: Guangxi 15,217; Sichuan 13,990; Heilongjiang 13,429; Shaanxi 12,919; Fujian 10,340. The total number of foreign students receiving academic education in China is 258,122, accounting for 52.44% of the total number of foreign students in China, an increase of 16,579 over 2017, and an increase of 6.86% over the same period last year. There are 85,062 foreign masters and doctoral students, an increase of 12.28% over 2017. Of these there are 25,618 doctoral students and 59,444 masters students. In 2018 there were 234,063 non-degree international students. There are 63,041 international students assisted by the Chinese government scholarship, accounting for 12.81% of the total number of students in China, and 429,144 international students funded by other resources, accounting for 87.19%."),
        card("(4) Why China",
             "Various factors combine to make China a desirable destination for international students. 1. China boasts a significant number of world-class universities. 2. Universities in China are attractive research centers. 3. It costs less than studying in developed countries. 4. There is a huge diversity of universities and programs. 5. There are more career opportunities due to China’s growing economic strength. 6. Many graduate and postgraduate programs are offered in English. 7. A huge number of scholarships are on offer from the Chinese government. China is openly pursuing a policy of growing its soft power globally, by way of persuasion and attraction. Attracting international students, especially by way of scholarships, is one effective way of growing this influence. References: www.moe.gov.cn; International Students in China."),
    ],
    exercises=[
        M("How many foreign students studied in China in 2018?", "492,185", ["442,773", "50,600", "258,122"], "492,185 from 196 countries."),
        M("How many countries did they come from?", "196", ["31", "1,004", "50"], "from 196 countries."),
        M("How many higher education institutions hosted them?", "1,004", ["196", "31", "492"], "1,004 higher education institutions."),
        M("Where did China rank as a receiver of international students in 2018?", "Second in the world and first in Asia", ["First in the world", "Tenth in the world", "Second in Asia"], "most popular in Asia, second in the world."),
        M("Which country sent the most students in 2018?", "South Korea", ["Thailand", "Pakistan", "India"], "1. South Korea."),
        M("Which place hosted the most international students?", "Beijing", ["Shanghai", "Jiangsu", "Zhejiang"], "1. 80,786 Beijing."),
        M("How many foreign students receive academic education (degrees)?", "258,122", ["234,063", "85,062", "492,185"], "258,122."),
        M("How many are masters students?", "59,444", ["25,618", "85,062", "63,041"], "59,444 masters."),
        M("How many are funded by the Chinese government scholarship?", "63,041", ["429,144", "234,063", "85,062"], "63,041."),
        M("Which of these is a reason students choose China?", "It costs less than studying in developed countries", ["It has no exams", "It is closer to the U.S.", "Everything is free"], "It costs less."),
        M("What policy does the passage say China pursues with scholarships?", "Growing its soft power", ["Closing its schools", "Reducing foreign contacts", "Raising tuition"], "growing its soft power globally."),
        M("Which statement about the trend is true?", "The number has grown steadily since 2003", ["It fell after 2008", "It fell because of terrorism", "It has stayed the same"], "grown steadily since 2003."),
    ],
)

UNIT = unit("第二十三课 Presentation 3: 罗文在天津, 尽管…可是…, 极了, 有和是, 多重复句, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8])
