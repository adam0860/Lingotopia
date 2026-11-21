"""Unit 85: Lesson 27 (New Careers), Presentation 3, first half: the passage about e-sports and the player Li Xiaofeng with its listening activities,
the word-pair and game activities, and the patterns 随着, 认识到/了解到/打听到, 当(职业)需要…… and 有了……后.
Audio and pictures are not included; numbers the book writes as digits are spelled out in Chinese text; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l27_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('行业', 0, 'hang2'), ('家长', 1, 'zhang3'), ('，得过两次', 1, 'de2'), ('，得了好几次', 1, 'de2'), ('得不了冠军', 0, 'de2'), ('得不了冠军', 2, 'liao3'), ('常常得亚军', 2, 'de2'), ('好学校', 0, 'hao3'), ('随着风摇动', 1, 'zhe5'), ('教他怎', 0, 'jiao1')):
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
NOUN = ["游戏", "选手", "比赛"]

# ------------------------------------------------------------------ 1. presentation 3 + activities 1-2
PB1 = ("你听说过玩电脑游戏也是一种职业吗？这种职业就是近些年流行的电子竞技。以前，家长们担心孩子打游戏对学习不好，但是随着电竞职业的出现，人们认识到电子游戏是一种很好的智力活动。",
       "Have you heard that playing computer games is also a profession? This profession is the e-sports that has been popular in recent years. In the past parents worried that children playing games was bad for their studies, but with the appearance of the e-sports profession people have come to realize that video games are a very good mental activity. (translations in this card are mine)")
PB2 = ("电子竞技并不像打游戏那么简单。对职业选手来说，当电竞员需要长时间的训练和合作。电竞职业的最大特点是要求选手反应快，所以参加职业比赛的都是年轻人，大部分在二十岁左右。李晓峰是中国第一代电竞选手。上初中时，他跟表弟学会了“星际争霸”的游戏，就迷上了电竞，后来，更成为一名职业选手。他代表中国队参加世界电子竞技大赛，得过两次冠军和两次亚军。",
       "E-sports is not as simple as playing games. For a professional player, being an e-sports player requires long hours of training and cooperation. The biggest feature of the e-sports profession is that it requires players to react fast, so those who take part in professional competitions are all young people, mostly around twenty years old. Li Xiaofeng is a first-generation Chinese e-sports player. In junior high school he learned the game “StarCraft” from his younger cousin and got hooked on e-sports, and later became a professional player. He represented the Chinese team in the world e-sports contest and won two championships and two runner-up places.")
PB3 = ("现在，电子竞技在中国非常流行，有了“英雄联盟”和“王者荣耀”这两个游戏后，电竞行业就更火了，许多游戏主播和游戏职业选手都有大量的粉丝，成为了明星。",
       "Now e-sports is very popular in China. After the two games “League of Legends” and “Kings of Glory” appeared, the e-sports industry became even hotter, and many game streamers and professional game players have large numbers of fans and have become stars. (the book also prints the passage in traditional characters)")
H2 = [("现在中国有多少电子竞技队和电竞职业选手？", "Activity 2A-1 (audio Passage 1): How many e-sports teams and professional e-sports players are there in China now?"), ("以前家长们为什么不让孩子玩电脑游戏？", "2A-2: Why did parents in the past not let children play computer games?"), ("现在为什么很多人认为打游戏很好？", "2A-3: Why do many people now think playing games is good?"), ("电子竞技什么时候成为亚运会的比赛项目？", "2A-4: When did e-sports become a competition event of the Asian Games?"),
      ("电子竞技和一般的电脑游戏一样，打得好就能成为电竞选手。", "Activity 2C-1 (true or false, audio Passage 2; my key: False, because the presentation says e-sports is not as simple as playing games): E-sports is the same as ordinary computer games; if you play well you can become an e-sports player."),
      ("中国有五点二九亿人玩网络游戏，所以很多中国人都是电竞职业选手。", "2C-2: 529 million people in China play online games, so many Chinese are professional e-sports players. (the book writes 5.29 亿 in digits)"), ("职业电竞员每天要训练十几个小时的游戏。", "2C-3: Professional e-sports players train for over ten hours a day."),
      ("职业电竞员的年龄一般很年轻，因为这个职业需要选手反应快。", "2C-4 (my key: True, as the presentation says): Professional e-sports players are generally very young because this profession needs players to react fast."),
      ("李晓峰从小就喜欢电竞，想成为职业电竞选手。", "Activity 2E-1 (true or false, audio Passage 3): Li Xiaofeng has liked e-sports since childhood and wanted to become a professional e-sports player."), ("李晓峰的爸爸让他打游戏，因为他的学习成绩很好。", "2E-2: Li Xiaofeng’s father let him play games because his grades were very good."),
      ("李晓峰的表弟教他怎么玩“英雄联盟”的游戏。", "2E-3 (my key: False, as the presentation says he learned StarCraft from his cousin): Li Xiaofeng’s cousin taught him how to play “League of Legends”."), ("李晓峰的爸爸支持他成为一名电竞职业选手。", "2E-4: Li Xiaofeng’s father supported him becoming a professional e-sports player.")]
L1 = lesson(
    "Lesson 27 Presentation 3: e-sports and Li Xiaofeng",
    "电子竞技 · 电竞职业 · 智力活动 · 李晓峰 · 星际争霸 · 英雄联盟 · 王者荣耀 · 冠军",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. Do you like to play video games? Which game is your favorite? B. Do you enjoy or participate in e-sports? Who are your favorite players? C. What are the similarities between e-sports and traditional sports? (Four pictures are not included.)"),
        card("Presentation 3: 电子竞技", "The three paragraphs of the presentation; the book also prints them in traditional characters.", examples=[D(*PB1), D(*PB2), D(*PB3)]),
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Global Listening: listen to Presentation 3 once through and answer the question: 1. What is the main idea of this presentation? B. Detailed Listening: listen again and answer: 1. What is a common preconception held by parents regarding video games? 2. What are the physical and mental requirements for professional e-sports players? 3. What is said about Li Xiaofeng? 4. What is one reason for the recent boom of the e-sports industry in China? C. Pair up, discuss the answers and share them with the class. My answers, from the presentation: A. 1. E-sports has become a popular profession in China. B. 1. That playing games is bad for children’s studies. 2. Long training and cooperation, quick reactions, and youth (mostly around twenty). 3. He is a first-generation Chinese e-sports player who learned StarCraft from his cousin in junior high, became a professional and won two championships and two runner-up places for China. 4. The two games “League of Legends” and “Kings of Glory” appeared."),
        card("Activity 2 (Listening, Reading, and Speaking)",
             "A. Listen to Passage 1 and answer the questions. B. Pair up and discuss the answers and talk about the popularity of e-sports in the U.S. C. Listen to Passage 2 and mark the statements as True or False. D. Pair up, discuss and justify your answers. Talk about the lives and work of professional e-sports players in the U.S. E. Listen to Passage 3 and mark the statements as True or False. F. Pair up, discuss your answers, and talk about your favorite e-sports player. The passages are audio and not in the book, so my key is given only for 2C-1, 2C-4 and 2E-3, which the presentation itself decides. The questions and statements are the book’s:",
             examples=[D(z, e) for z, e in H2]),
    ],
    exercises=[
        M("What does 电子竞技 mean?", "E-sports", ["Electric trains", "Electronic books", "Radio"], "电子竞技."),
        M("What did parents in the past worry about?", "That playing games was bad for studies", ["That games cost too much", "That games were too short", "That games were too easy"], "担心孩子打游戏对学习不好."),
        M("What do people realize now?", "Video games are a very good mental activity", ["Games are always bad", "Games are free", "Games are only for adults"], "很好的智力活动."),
        M("What is the biggest feature of the e-sports profession?", "It requires players to react fast", ["It requires a car", "It requires a degree in art", "It requires living abroad"], "要求选手反应快."),
        M("About how old are most professional players?", "Around twenty", ["Around ten", "Around fifty", "Around seventy"], "大部分在二十岁左右."),
        M("Who is the first-generation Chinese e-sports player in the passage?", "Li Xiaofeng", ["Li Ziqi", "Li Jiaqi", "Xiao Song"], "李晓峰."),
        M("From whom did Li Xiaofeng learn StarCraft?", "His younger cousin", ["His teacher", "His father", "His neighbor"], "他跟表弟学会了“星际争霸”."),
        M("What did Li Xiaofeng win for China?", "Two championships and two runner-up places", ["One Nobel Prize", "Three gold medals in swimming", "Nothing"], "得过两次冠军和两次亚军."),
        M("Which two games made the e-sports industry even hotter?", "League of Legends and Kings of Glory", ["Chess and Go", "Soccer and tennis", "Cards and dice"], "“英雄联盟”和“王者荣耀”."),
        F("以前，家长们担心孩子打游戏对学习不___。", "好", PART, "不好: not good."),
        F("他跟表弟学会了“星际争霸”的游戏，就迷___了电竞。", "上", PART, "迷上: got hooked."),
        F("他代表中国队参加世界电子竞技大___。", "赛", PART, "大赛: contest."),
    ],
)

# ------------------------------------------------------------------ 2. activities 3-4
W3 = [("有了“英雄联盟”和“王者荣耀”这两个游戏后，电竞行业变得越来越火。", "Activity 3A-1a (my key: 行业): After the two games “League of Legends” and “Kings of Glory” appeared, the e-sports industry became hotter and hotter."), ("现在中国出现了很多新职业，比如“快递小哥”、“网红”等。", "1b (职业): Now many new professions have appeared in China, such as “courier guys” and “internet celebrities”."),
      ("职业电竞选手的压力非常大，所以需要很强的体力来进行训练。", "2a (选手; the book prints no comma before 所以): The pressure on professional e-sports players is very great, so they need strong physical strength for training."), ("我早上在网上下了一个单，下午货就送到了。“快递小哥”真是我们的好帮手。", "2b (帮手): I placed an order online in the morning and the goods arrived in the afternoon. “Courier guys” really are our good helpers."),
      ("玩网路游戏的人很多，但只有很少一些人才能成为职业电竞员。", "3a (职业): Many people play online games, but only a very few can become professional e-sports players."), ("张军喜欢直播游戏，但是他只是一个业余的电竞爱好者。", "3b (业余): Zhang Jun likes to live-stream games, but he is only an amateur e-sports fan."),
      ("李晓峰经常参加各种电竞大赛，得了好几次冠军。", "4a (冠军): Li Xiaofeng often takes part in all kinds of e-sports contests and has won the championship several times."), ("王刚的运气不太好，每次比赛他都得不了冠军，常常得亚军。", "4b (亚军): Wang Gang’s luck is not so good; in every contest he cannot win the championship and often gets second place."),
      ("做电竞员的大部分都是年轻人，因为这个运动需要反应快。", "5a (反应): Most e-sports players are young people because this sport needs fast reactions."), ("现在很多人认识到打电子游戏也是一种智力运动。", "5b (智力): Now many people realize that playing video games is also a mental sport."),
      ("电子竞技这个职业要求电竞选手们的长期训练和合作。", "6a (合作): The e-sports profession requires long-term training and cooperation from the players."), ("李晓峰曾经多次代表中国去参加世界竞技大赛，并获得优秀的成绩。", "6b (代表): Li Xiaofeng has many times represented China in world competitions and achieved excellent results.")]
G4 = [("随着电脑的发展，出现了很多好玩的游戏。“星际争霸”并不像别的游戏那么容易，玩的人要想很多办法。“英雄联盟”是五个人一队，大家要合作，很多人迷上了它。“王者荣耀”可以在手机上玩，并不像电脑游戏那么麻烦，也有很多人迷上了它。", "Activity 4A (my sample notes on three popular games, using 随着……出现, 并不像……那么…… and 迷上了……): With the development of computers, many fun games have appeared. “StarCraft” is not as easy as other games, and players must think of many ways. “League of Legends” is played in teams of five, everyone has to cooperate, and many people got hooked on it. “Kings of Glory” can be played on a phone and is not as troublesome as computer games, and many people also got hooked on it. (the book gives the three game titles with pictures and a table “游戏特点” left empty)")]
L2 = lesson(
    "Lesson 27 Presentation 3 activities 3-4: word pairs and popular games",
    "职业 行业 · 选手 帮手 · 职业 业余 · 冠军 亚军 · 智力 反应 · 合作 代表 · 迷上 · 并不像……那么……",
    requires=[],
    cards=[
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up, compare the meaning of the words in each box, and complete each sentence with the correct word. Translate each sentence into English. The boxes are 1. 职业, 行业 2. 选手, 帮手 3. 职业, 业余 4. 冠军, 亚军 5. 智力, 反应 6. 合作, 代表. B. Share your work with the class. My key and translations:",
             examples=[D(z, e) for z, e in W3]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Pair up and use the following words and expressions to talk about three popular games: 随着……出现 | 并不像……那么…… | 迷上了……. Have you played these games? Talk about the features of the three games and why they are fun. B. Share your group discussion with the class. My sample:",
             examples=[D(*G4[0])]),
    ],
    exercises=[
        M("Which word fits “电竞___变得越来越火”?", "行业", ["业余", "帮手", "亚军"], "行业: industry."),
        M("Which word fits “现在中国出现了很多新___”?", "职业", ["业余", "选手", "代表"], "职业: profession."),
        M("Which word fits “快递小哥真是我们的好___”?", "帮手", ["选手", "冠军", "智力"], "帮手: helper."),
        M("What does 业余 mean?", "Amateur; spare time", ["Professional", "Winner", "Reaction"], "业余."),
        M("Which word fits “李晓峰经常参加各种电竞大赛，得了好几次___”?", "冠军", ["亚军", "业余", "反应"], "冠军: champion."),
        M("What does 亚军 mean?", "Second place", ["First place", "Third place", "Last place"], "亚军."),
        M("Which word fits “这个运动需要___快”?", "反应", ["智力", "合作", "代表"], "反应: reaction."),
        M("Which word fits “李晓峰曾经多次___中国去参加世界竞技大赛”?", "代表", ["合作", "反应", "业余"], "代表: represent."),
        F("电子竞技这个职业要求电竞选手们的长期训练和合___。", "作", PART, "合作: cooperate."),
        F("现在很多人认识到打电子游戏也是一种智___运动。", "力", PART, "智力: intelligence."),
        F("王刚的运气不太好，每次比赛他都得不了冠___。", "军", PART, "冠军: champion."),
    ],
)

# ------------------------------------------------------------------ 3. 随着
SZ0 = table(["结构", "用法"], [["随着 + Noun Phrase，Subject + Predicate", "随着 means “along with”, “in the wake of” and “following”; used in the first part of the sentence, it indicates that a change in the first part causes a respective change in the second part"], ["Subject + 随着 + Noun/Pronoun + Verbal Phrase", "随着 can also be used after a subject to indicate “moving together with”"]], title="The Usage of 随着")
SZE = [("随着互联网的发展，网路直播成了一个热门职业。", "At the beginning 1. With the development of the Internet, online live streaming has become a popular profession."), ("随着电竞职业的出现，人们认识到电子游戏是一种很好的智力活动。", "2. With the appearance of the e-sports profession, people have realized that video games are a very good mental activity."),
       ("大家随着音乐跳起舞来。", "After a subject 1. Everyone started to dance to the music."), ("比尔随着家人一起搬到了洛杉矶。", "2. Bill moved to Los Angeles together with his family.")]
SZ2 = [("树随着风摇动。", "Activity 2A-1 (my sample; the book glosses 摇动 as yáodòng): The tree sways with the wind."), ("他随着女朋友去了中国。", "2A-2: He went to China with his girlfriend."), ("大家随着音乐跳舞。", "2A-3: Everyone dances to the music."), ("她随着音乐唱起歌来。", "2A-4: She began to sing along with the music.")]
L3 = lesson(
    "Lesson 27 Presentation 3 grammar: the usage of 随着",
    "随着…… · 随着互联网的发展 · 随着电竞职业的出现 · 随着音乐跳舞 · 随着家人",
    requires=[],
    cards=[
        card("The Usage of 随着",
             "随着 means “along with,” “in the wake of,” and “following.” When 随着 is used in the first part of the sentence, it indicates that a change in the first part causes a respective change in the second part. 随着 + Noun Phrase, Subject + Predicate. 随着 can also be used after a subject to indicate “moving together with.” Subject + 随着 + Noun/Pronoun + Verbal Phrase.",
             tables=[SZ0], examples=[D(z, e) for z, e in SZE]),
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Listen to the sentences with 随着 (six items) and translate what you hear into English. B. Pair up and check your translations with your partner. Then say sentences in Chinese to your partner. (Audio; the sentences are not in the book.)"),
        card("Activity 2 (Writing and Speaking)",
             "A. Pair up and create sentences with your partner, using the pattern “Subject + 随着 + Noun + Verbal Phrase” and the words given below: 1. 树，风，摇动 2. 女朋友，去，中国 3. 音乐，跳舞 4. 音乐，唱歌. B. Read the sentences that you have created aloud and translate them into English. C. Share your sentences with the class. (Four pictures are not included.) My samples:",
             examples=[D(z, e) for z, e in SZ2]),
    ],
    exercises=[
        M("What does 随着 mean?", "Along with; following", ["Instead of", "Without", "Against"], "随着."),
        M("What does the first part with 随着 cause?", "A change in the second part", ["A question", "A refusal", "A greeting"], "A change in the first part causes a change in the second."),
        M("Which sentence puts 随着 at the beginning?", "随着互联网的发展，网路直播成了一个热门职业", ["大家随着音乐跳起舞来", "比尔随着家人一起搬到了洛杉矶", "他随着女朋友去了中国"], "随着 + Noun Phrase, …"),
        M("What does 大家随着音乐跳起舞来 mean?", "Everyone started to dance to the music", ["Everyone stopped the music", "Everyone sang a song", "Everyone went home"], "随着音乐."),
        M("With whom did Bill move to Los Angeles?", "His family", ["His teacher", "His boss", "His dog"], "比尔随着家人一起搬到了洛杉矶."),
        M("Which sentence is correct?", "他随着女朋友去了中国", ["他女朋友去了中国随着", "随着他女朋友去了中国他", "去了中国随着他女朋友"], "Subject + 随着 + Noun + Verbal Phrase."),
        F("___着互联网的发展，网路直播成了一个热门职业。", "随", PART, "随着."),
        F("大家随着音乐跳起___来。", "舞", PART, "跳起舞来: started to dance."),
    ],
)

# ------------------------------------------------------------------ 4. 认识到/了解到/打听到
RL0 = table(["结构", "用法"], [["Subject + 认识到/了解到/打听到 + Noun/Sentence", "verb-complement compound words; 到 is a result complement indicating that the outcome of the verb is achieved with a certain degree of effort. 认识到: “be aware of”, “have knowledge of”, “realize”; 了解到: “learn about”; 打听到: “inquire and find out”"]], title="认识到/了解到/打听到")
RLE = [("随着电竞职业的出现，人们认识到电子游戏是一种很好的智力活动。", "1. With the appearance of the e-sports profession, people have realized that video games are a very good mental activity."), ("自从了解到怎么开网店以后，他几乎天天都在网上卖各种东西。", "2. Ever since he learned how to open an online shop, he has sold all kinds of things online almost every day."), ("小刚从他表弟那里打听到这个网路游戏的名字。", "3. Xiao Gang found out the name of this online game from his younger cousin.")]
RL3 = [("李晓峰了解到北京有很多电竞比赛的机会，所以他来到北京学习电竞。", "Activity 3A-1 (my key: 了解到; 打听到 also fits): Li Xiaofeng learned that Beijing has many e-sports contest opportunities, so he came to Beijing to study e-sports."), ("现在，人们渐渐认识到当电竞员是很赚钱的工作。", "3A-2 (认识到): Now people gradually realize that being an e-sports player is a very lucrative job."),
       ("他到现在还没有认识到学中文有多么重要。", "3A-3 (认识到): Up to now he hasn’t realized how important learning Chinese is."), ("看李子柒的视频，不仅能学会做中国菜，还能了解到中国文化。", "3A-4 (了解到): Watching Li Ziqi’s videos, one can not only learn to cook Chinese dishes but also learn about Chinese culture."),
       ("王军刚刚从同学那里打听到一个特别好玩的网路游戏。", "3A-5 (打听到): Wang Jun has just found out about a particularly fun online game from a classmate."), ("在这部电影里，观众们可以了解到中国现在的社会问题。", "3A-6 (了解到): In this film, audiences can learn about China’s social problems today.")]
RL4 = [("小丽很喜欢打游戏。她从同学那里打听到有一个新的电竞比赛，就去报了名。她了解到比赛的奖金很高，参加的人也很多。比赛以后，她认识到只有长期的训练才能得到好成绩。现在她每天都去训练，也认识到学习和玩游戏都很重要。", "Activity 4A (my sample story, five sentences, about video games and e-sports): Xiao Li likes playing games very much. She found out from a classmate that there is a new e-sports contest and signed up. She learned that the contest prize is high and many people take part. After the contest she realized that only long-term training can bring good results. Now she goes to training every day and has also realized that both studying and playing games are important.")]
L4 = lesson(
    "Lesson 27 Presentation 3 grammar: 认识到, 了解到 and 打听到",
    "认识到 · 了解到 · 打听到 · 结果补语 到 · 电竞比赛 · 网路游戏",
    requires=[],
    cards=[
        card("认识到/了解到/打听到",
             "认识到, 了解到, 打听到 are verb-complement compound words. 到 is a result complement indicating that the outcome of the verb is achieved with a certain degree of effort. 认识到 is equivalent to “be aware of,” “to have knowledge of,” or “realize” in English, whereas 了解到 means “learn about”; 打听到 means to “inquire and find out.” Subject + 认识到/了解到/打听到 + Noun/Sentence.",
             tables=[RL0], examples=[D(z, e) for z, e in RLE]),
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up and complete the sentences with 认识到, 了解到 and 打听到. B. With your partner, discuss the meaning of 认识到, 了解到, 打听到 in the sentences and translate them into English. My key and translations (the book leaves the blanks empty):",
             examples=[D(z, e) for z, e in RL3]),
        card("Activity 4 (Writing and Speaking)",
             "A. Write a short story about video games and e-sports by using 认识到, 了解到, 打听到. Write at least five sentences. B. Pair up and read your story to your partner. C. Share your stories with the class. My sample:",
             examples=[D(*RL4[0])]),
    ],
    exercises=[
        M("What does 认识到 mean?", "Realize; be aware of", ["Forget", "Sell", "Refuse"], "认识到."),
        M("What does 了解到 mean?", "Learn about", ["Give up", "Throw away", "Send"], "了解到."),
        M("What does 打听到 mean?", "Inquire and find out", ["Listen to music", "Hit and break", "Hear nothing"], "打听到."),
        M("What is 到 in these words?", "A result complement", ["A measure word", "A question particle", "A noun"], "到: result complement."),
        M("Which fits “小刚从他表弟那里___这个网路游戏的名字”?", "打听到", ["认识到", "了解到", "没想到"], "打听到: found out."),
        M("Which fits “现在，人们渐渐___当电竞员是很赚钱的工作”?", "认识到", ["打听到", "走到", "看到"], "认识到: realize."),
        M("Which fits “看李子柒的视频，还能___中国文化”?", "了解到", ["打听到", "认识到", "没学到"], "了解到: learn about."),
        F("他到现在还没有认识___学中文有多么重要。", "到", PART, "认识到."),
        F("王军刚刚从同学那里打听到一个特别好___的网路游戏。", "玩", PART, "好玩: fun."),
    ],
)

# ------------------------------------------------------------------ 5. 当(职业)需要, 有了…后
DX0 = table(["结构", "用法"], [["当 + 职业 + 需要 + 条件", "introduces the conditions that a certain type of occupation requires"], ["Verbal phrase + 需要 + 条件", "can also indicate the conditions for completing a task"]], title="当(职业)需要……(表示条件)")
DXE2 = [("对职业选手来说，当电竞员需要长时间的训练和合作。", "Occupation 1. For professional players, being an e-sports player requires long training and cooperation."), ("当外卖员需要了解餐馆附近的街道，用最快的速度把外卖送给顾客。", "2. Being a takeout deliverer requires knowing the streets near the restaurants and delivering takeout to customers at the fastest speed."),
        ("学外语需要做大量的听力练习和阅读练习。", "Task 1. Learning a foreign language requires a great deal of listening practice and reading practice."), ("做作业需要先复习一下当天学的，然后再写。", "2. Doing homework requires first reviewing what you learned that day, and then writing.")]
DX5 = [("当职业篮球运动员需要长期的训练，很强的体力，还需要很好的合作精神。", "Activity 5A-1 (my sample, 当职业篮球运动员): Being a professional basketball player requires long-term training, great physical strength and also a good spirit of cooperation."), ("当老师需要认真地准备课，耐心地教学生，还需要了解每一个学生。", "5A-2 (当老师): Being a teacher requires preparing lessons carefully, teaching students patiently and getting to know every student."), ("当军人需要经过很多训练，身体要好，还需要听从命令。", "5A-3 (当军人): Being a soldier requires going through a lot of training, being in good health and obeying orders.")]
YL0 = table(["结构", "用法"], [["有了……后，impact + elaboration", "introduces something that leads to a certain impact and further elaborates on it"]], title="有了……后，……")
YLE = [("有了“英雄联盟”和“王者荣耀”这两个游戏后，电竞行业就更火了，许多游戏主播和游戏职业选手都有大量的粉丝，成为了明星。", "Example (the book marks 电竞行业就更火了 as the impact, and 许多游戏主播和游戏职业选手都有大量的粉丝，成为了明星 as the elaboration): After the two games “League of Legends” and “Kings of Glory” appeared, the e-sports industry became even hotter, and many game streamers and professional players have large numbers of fans and have become stars.")]
YL6 = [("有了网约车后，人们的出行变得方便多了，不用站在路边等着好长时间才来一趟的公交车，也不用天天在地铁上和别人挤在一起，只要在手机软件上输入你的地址，车很快就来了。", "Activity 6A-1 (my key: the structure is 有了网约车后; the impact is 人们的出行变得方便多了; the elaboration is everything after it. The book prints 手机上软件上, which I have corrected to 手机软件上): After ride-hailing appeared, people’s travel became much more convenient: you no longer stand at the roadside waiting a long time for a bus that comes once in a while, nor squeeze in with others on the subway every day; you just enter your address in a phone app and the car comes very soon."),
       ("出门旅游，很多人喜欢住民宿。有了爱彼迎后，旅游住宿就更方便了，在爱彼迎的网站上可以找到各种各样的房子，有的价钱比一般的旅馆便宜很多，而且还可以和房主聊天，认识别的客人。", "6A-2 (my key: the structure is 有了爱彼迎后; the impact is 旅游住宿就更方便了; the elaboration is the rest): When going out to travel, many people like to stay in homestays. After Airbnb appeared, tourist lodging became even more convenient: on the Airbnb website you can find all kinds of houses, some are much cheaper than ordinary hotels, and you can also chat with the host and get to know other guests."),
       ("有了智能手机后，人们的生活变得方便多了。出门不用带很多现金，用手机就能付钱；想买东西，在网上下个单，第二天快递员就把东西送到家里来了。", "Activity 6B (my sample on something new that affects our lives, with impact and elaboration): After smartphones appeared, people’s lives became much more convenient. You don’t need to carry much cash when going out, since you can pay with your phone; when you want to buy something, you place an order online and the next day the courier brings it to your home.")]
L5 = lesson(
    "Lesson 27 Presentation 3 grammar: 当(职业)需要…… and 有了……后",
    "当电竞员需要 · 学外语需要 · 做作业需要 · 有了…后 · 有了网约车后 · 有了爱彼迎后",
    requires=[],
    cards=[
        card("当(职业)需要……(表示条件)",
             "The structure 当(职业)需要…… introduces the conditions that a certain type of occupation requires. 当 + 职业 + 需要 + 条件. This structure can also indicate the conditions for completing a task. Verbal phrase + 需要 + 条件.",
             tables=[DX0], examples=[D(z, e) for z, e in DXE2]),
        card("Activity 5 (Reading, Writing and Speaking)",
             "A. Pair up and write a short paragraph for the following topics by using the structure “当(职业)需要……” with your partner: 1. 当职业篮球运动员需要什么条件？ 2. 当老师需要怎么做？ 3. 当军人需要做什么？ B. Share what you have written with the class. My samples:",
             examples=[D(z, e) for z, e in DX5]),
        card("有了……后，……",
             "The structure 有了……后 is used to introduce something that leads to a certain impact and further elaborate on it. 有了……后, impact + elaboration.",
             tables=[YL0], examples=[D(z, e) for z, e in YLE]),
        card("Activity 6 (Reading, Writing and Speaking)",
             "A. Read the following passages. Identify the structure 有了……后, and highlight the sentences that show impact and elaboration. B. Pair up and think about something new or innovative that can impact society or our lives. Write a short paragraph about it using the structure 有了……后 and the impact and elaboration of your work. C. Share your pair’s writing with the class. The passages with my key, then my sample:",
             examples=[D(z, e) for z, e in YL6]),
    ],
    exercises=[
        M("What does 当 + 职业 + 需要 + 条件 introduce?", "The conditions an occupation requires", ["The salary", "The age", "The name"], "条件."),
        M("What does 当外卖员需要了解餐馆附近的街道 say?", "Being a takeout deliverer requires knowing the streets near restaurants", ["Takeout is free", "Restaurants are closed", "Streets are new"], "当外卖员需要…"),
        M("What does 学外语需要做大量的听力练习和阅读练习 say?", "Learning a foreign language needs lots of listening and reading practice", ["Foreign languages are easy", "One should only read", "Listening is not needed"], "需要."),
        M("What does 做作业需要先复习一下当天学的 say?", "Doing homework requires first reviewing what you learned that day", ["Homework is optional", "Review after sleeping", "Never review"], "做作业需要…"),
        M("What does 有了……后 introduce?", "Something that leads to a certain impact", ["A question", "A negative", "A time word only"], "有了…后."),
        M("In 有了网约车后，人们的出行变得方便多了, what is the impact?", "People’s travel became much more convenient", ["Cars became cheaper", "The subway closed", "Buses became free"], "出行变得方便多了."),
        M("What does 爱彼迎 let you do, according to the passage?", "Find all kinds of houses and chat with the host", ["Buy a car", "Order takeout", "Play games"], "各种各样的房子…和房主聊天."),
        F("当电竞员需___长时间的训练和合作。", "要", PART, "需要: requires."),
        F("有了网约车后，人们的出行变得方___多了。", "便", PART, "方便: convenient."),
    ],
)

UNIT = unit("第二十七课 Presentation 3: 电子竞技, 随着, 认识到, 当(职业)需要, 有了…后", [L1, L2, L3, L4, L5])
