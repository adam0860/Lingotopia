"""Unit 86: Lesson 27 (New Careers), Presentation 3, second half and the end of the lesson: the skill-integration tasks (a Fortnite contest, e-sports at the Asian Games, Faker),
the using-Chinese tasks (persuading a mother, a survey about students and games, game recommendations), the vocabulary list and the Area Studies page on e-commerce in rural China.
Audio, pictures and videos are not included; numbers the book writes as digits are spelled out in Chinese text; Latin-letter names in the spoken text are written full-width;
the bracketed glosses are given in tables; web addresses are left out; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l27_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('行业', 0, 'hang2'), ('家长', 1, 'zhang3'), ('已经得到了', 2, 'de2'), ('友得了第几名', 1, 'de2'), ('会得到多少钱', 1, 'de2'), ('拿到多少奖金', 0, 'na2'), ('赛上得到冠军', 2, 'de2'), ('还得到了', 1, 'de2'), ('好学校', 0, 'hao3'), ('中得了银牌', 1, 'de2'), ('队得了金牌', 1, 'de2'), ('获得很多', 1, 'de2')):
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

# ------------------------------------------------------------------ 1. skill integration 1-2
FG = table(["词", "拼音", "Meaning (the book’s gloss)"], [["堡垒之夜", "bǎolěi zhī yè", "Fortnite World Cup"], ["在线上", "zài xiànshàng", "online"], ["决赛", "juésài (the book prints uésài)", "finals"], ["荷兰", "Hélán", "Netherlands"], ["投资", "tóuzī", "investment"], ["开发", "kāifā", "develop"]], title="Activity 1A: new words (生词)", say=[0])
FQ = [("有多少人报名参加比赛？有多少人参加决赛？", "Activity 1B-1 (audio): How many people signed up for the contest? How many took part in the finals?"), ("决赛那天，有多少人观看？", "1B-2: On the day of the finals, how many people watched?"), ("参加比赛的选手的年龄有多大？平均年龄多大？", "1B-3: How old were the players in the contest? What was the average age?"), ("参加决赛的选手已经得到了多少钱？如果赢了冠军会得到多少钱？", "1B-4: How much money had the finalists already received? How much would they get if they won the championship?"),
      ("二十一岁荷兰青年Ｄａｖｅ和他的英国队友得了第几名？拿到多少奖金？", "1B-5: In what place did the 21-year-old Dutch youth Dave and his British teammate finish? How much prize money did they get? (the book writes 21 and the name Dave in Latin letters)"), ("“堡垒之夜”有多少人玩？是哪个国家开发的？", "1B-6: How many people play “Fortnite”? Which country developed it?")]
FD = [("你看过电竞比赛吗？是在现场看还是在线上看？", "Activity 1D: Have you watched an e-sports contest? Did you watch on the spot or online?"), ("你看过的电竞比赛是哪一个？比赛的奖金是多少？", "Which e-sports contest did you watch? How much was the prize money?"), ("最后是哪个队赢了冠军？", "In the end, which team won the championship?"), ("如果你给刚听过的这篇文章一个标题，你会写什么？", "If you gave the article you just heard a title, what would you write?")]
GA = ("八月二十六日，在二零一八年雅加达亚运会电竞表演赛上，当大屏幕上放出“胜利”这个词的时候，中国电竞队主教练兴奋地和队员们抱在一起。在“王者荣耀国际版”表演赛中，中国队以二比零战胜了台北队，获得了亚运会电竞项目的第一块金牌。",
      "Group A: On August 26, at the e-sports exhibition match of the 2018 Jakarta Asian Games, when the word “victory” appeared on the big screen, the head coach of the Chinese e-sports team excitedly hugged the team members. In the “Arena of Valor” exhibition match the Chinese team beat the Taipei team 2 to 0 and won the first gold medal of the Asian Games e-sports events. (translation mine; the book writes the dates and scores in digits and 2018 without 年, which I added so it reads aloud)")
GB = ("八月二十七日，在个人项目“皇室战争”比赛中，中国选手黄成辉经过十二小时的比赛后，获得了这个项目的银牌。在八月二十九日“英雄联盟”表演赛中，中国队以三比一战胜了韩国队，获得这个项目的金牌。当这三个表演项目全部结束后，中国队获得两块金牌和一块银牌。",
      "Group B: On August 27, in the individual event “Royale” (the book glosses 皇室战争 as Battle Royale), the Chinese player Huang Chenghui won the silver medal in this event after twelve hours of play. In the “League of Legends” exhibition match on August 29, the Chinese team beat the Korean team 3 to 1 and won the gold medal in this event. When all three exhibition events had ended, the Chinese team had won two gold medals and one silver medal. (translation mine)")
GC = ("这是中国电竞队第一次参加亚运会电竞表演赛。中国队取得这么好的成绩，对电竞产业来说是一件很重要的事情，同时也会改变了一些人的看法。以前，很多人认为电竞和玩游戏一样，不能作为一种职业，但现在电竞成为亚运会的表演项目，以后会成为正式的比赛项目，这会给电竞行业的发展带来巨大的影响。",
      "Group C: This is the first time the Chinese e-sports team took part in the Asian Games e-sports exhibition matches. That the Chinese team got such good results is a very important thing for the e-sports industry, and it will also change some people’s views. In the past many people thought e-sports was the same as playing games and could not be a profession, but now e-sports has become an exhibition event of the Asian Games and will become an official competition event later, which will bring a huge impact on the development of the e-sports industry. (translation mine; the book prints 会改变了, which looks like a slip for 会改变)")
GG = table(["Gloss in the book", "Meaning"], [["雅加达 (Yǎjiādá; Jakarta)", "Jakarta"], ["屏幕 (píngmù; screen)", "screen"], ["胜利 (shènglì; victory)", "victory"], ["王者荣耀国际版 (Arena of Valor)", "the international version of Kings of Glory"], ["皇室战争 (huángshì zhànzhēng, Battle Royale)", "the book’s gloss; the game is usually known in English as Clash Royale"], ["标题 (biāotí; title)", "title"]], title="Activity 2A: the glosses in brackets (left out of the spoken text)")
GS = [("中国电竞队在二零一八年雅加达亚运会电竞表演赛上，以二比零战胜台北队，获得了第一块金牌。", "Activity 2A, my summary of Group A: At the 2018 Jakarta Asian Games e-sports exhibition, the Chinese team beat the Taipei team 2 to 0 and won the first gold medal."),
      ("中国选手黄成辉在“皇室战争”中得了银牌，中国队又在“英雄联盟”中以三比一战胜韩国队得了金牌，一共两块金牌和一块银牌。", "My summary of Group B: Chinese player Huang Chenghui won silver in “Royale”, and the Chinese team beat Korea 3 to 1 in “League of Legends” for gold, two golds and one silver in all."),
      ("这是中国电竞队第一次参加亚运会，成绩很好，会改变人们对电竞的看法，对电竞行业的发展有巨大的影响。", "My summary of Group C: This was the Chinese e-sports team’s first Asian Games; the results were good and will change people’s view of e-sports, with a huge impact on the industry’s development.")]
GT = [("如果你给刚读过的这篇文章一个标题，你会写什么？", "Activity 2C: If you gave the article you just read a title, what would you write?"), ("为什么说中国电竞队在亚运会上得到冠军，对中国电竞产业很重要？", "Why do we say that the Chinese e-sports team winning a championship at the Asian Games is very important for China’s e-sports industry? (my answer: because it changes people’s view that e-sports is only playing games, and e-sports may become an official event)"), ("很多人认为电竞和玩电子游戏差不多，你有什么看法？", "Many people think e-sports and playing video games are about the same; what is your view?")]
L1 = lesson(
    "Lesson 27 Presentation 3 skill integration: a Fortnite contest and e-sports at the Asian Games",
    "堡垒之夜 · 决赛 · 荷兰 · 亚运会电竞表演赛 · 王者荣耀国际版 · 皇室战争 · 英雄联盟",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the recording and write the main idea in a sentence. B. Listen to the recording again and answer the questions. C. Pair up and discuss your answers with your partner. Read the script if necessary. D. Talk about the following topics with your partner. (The recording and pictures are not included, so there is no key; the new words, questions and topics are the book’s.)",
             tables=[FG], examples=[D(z, e) for z, e in FQ + FD]),
        card("Skill Integration, Activity 2 (Reading, Writing and Speaking)",
             "A. In three groups, A, B and C, read the assigned passage and write a summary of your group’s passage. B. Re-group students by pairing one student from each group with a student from a different group. Exchange your summary with your new partner. C. Pair up and talk about the following topics with your partner. The three passages, the glosses, my summaries and the topics:",
             tables=[GG], examples=[D(*GA), D(*GB), D(*GC)] + [D(z, e) for z, e in GS + GT]),
    ],
    exercises=[
        M("Which game’s world cup is discussed in Activity 1?", "Fortnite (堡垒之夜)", ["StarCraft", "League of Legends", "Chess"], "堡垒之夜."),
        M("What does 决赛 mean?", "Finals", ["Semifinals", "Rules", "Fans"], "决赛: finals."),
        M("What does 荷兰 mean?", "The Netherlands", ["Holland Park", "England", "Germany"], "荷兰: Netherlands."),
        M("In which game did the Chinese team beat Taipei 2 to 0?", "Arena of Valor (王者荣耀国际版)", ["League of Legends", "Royale", "Fortnite"], "中国队以二比零战胜了台北队."),
        M("What did Huang Chenghui win?", "A silver medal in an individual event", ["A gold medal in a team event", "Nothing", "A car"], "获得了这个项目的银牌."),
        M("Who did the Chinese team beat 3 to 1 in League of Legends?", "The Korean team", ["The Taipei team", "The Dutch team", "The British team"], "战胜了韩国队."),
        M("How many gold and silver medals did China win in the three events?", "Two gold and one silver", ["Three gold", "One gold and two silver", "Three silver"], "两块金牌和一块银牌."),
        M("What did many people used to think about e-sports?", "That it was the same as playing games and not a profession", ["That it was a sport for children", "That it was dangerous", "That it was free"], "不能作为一种职业."),
        M("What will e-sports become later, according to Group C?", "An official competition event", ["A school subject", "A holiday", "A song"], "以后会成为正式的比赛项目."),
        F("当大屏幕上放出“胜利”这个词的时候，中国电竞队主教练兴奋地和队员们抱在一___。", "起", PART, "抱在一起: hugged each other."),
        F("中国队取得这么好的成绩，对电竞产___来说是一件很重要的事情。", "业", PART, "产业: industry."),
        F("这会给电竞行业的发展带来巨大的影___。", "响", PART, "影响: impact."),
    ],
)

# ------------------------------------------------------------------ 2. skill integration 3-4
FK = ("说到游戏“英雄联盟”，不能不提到韩国职业选手李相赫。李相赫于一九九六年五月七日在韩国首尔出生，他的游戏账户名叫Ｆａｋｅｒ。李相赫和爸爸在一起生活，他爸爸一直相信他天生就是一个电竞职业选手。二零一一年十二月，他开始玩“英雄联盟”，他很快就知道这个游戏的玩法。不管是学习还是玩游戏，他都非常努力。即使喜欢玩游戏，他的学习成绩也非常好，而且还得到了首尔大学的入学资格，但是他没有去上大学，他选择了电竞职业，加入了国际电子竞技俱乐部，成为一名“英雄联盟”的电竞选手。Ｆａｋｅｒ的电竞技术非常好，获得很多次冠军，是“英雄联盟”比赛中获得冠军最多的职业选手。",
      "Speaking of the game “League of Legends”, one cannot fail to mention the Korean professional player Li Xianghe (Lee Sang-hyeok). Li Xianghe was born in Seoul, Korea, on May 7, 1996, and his game account name is Faker. Li Xianghe lives with his father, who has always believed he was born to be a professional e-sports player. In December 2011 he began to play “League of Legends” and soon knew how the game is played. Whether studying or playing games, he works very hard. Even though he likes playing games, his grades are very good, and he even got a qualification to enter Seoul National University, but he did not go to university; he chose the e-sports profession, joined an international e-sports club and became an e-sports player of “League of Legends”. Faker’s e-sports skill is very good; he has won many championships and is the professional player with the most championships in “League of Legends” matches. (translation mine; the book names the club SKT T1, left out of the spoken text, and writes the dates in digits)")
FKG = table(["Gloss in the book", "Meaning"], [["李相赫 (lǐxiānghè)", "the player’s name; the book gives his in-game name as Faker"], ["首尔 (shǒuěr, Seoul)", "Seoul"], ["资格 (zīgé, qualification)", "qualification"], ["SKT T1", "the club he joined (left out of the spoken text)"]], title="Activity 3A: the glosses in brackets")
FKS = [("李相赫是韩国“英雄联盟”职业选手，游戏账户名叫Ｆａｋｅｒ。他学习成绩很好，也很努力，但是没有去上首尔大学，而是选择了电竞职业，获得了很多次冠军。", "Activity 3A, my summary: Li Xianghe is a Korean professional “League of Legends” player whose game account name is Faker. His grades were very good and he worked hard, but he did not go to Seoul National University and chose the e-sports profession instead, winning many championships.")]
FKQ = [("你有没有看过李相赫“英雄联盟”的比赛？你觉得他在比赛中表现怎么样？", "Activity 3B: Have you watched Li Xianghe’s “League of Legends” matches? How do you think he performs in contests?"), ("在全球，哪个电竞选手玩“英雄联盟”玩得最好？", "Worldwide, which e-sports player plays “League of Legends” best?"), ("李相赫没有去上大学而去做电竞选手，你觉得他的做法怎么样？", "Li Xianghe did not go to university but became an e-sports player; what do you think of what he did?")]
EM4 = table(["Field", "Sample (mine)"], [["TO", "Faker"], ["CC", "(none)"], ["Subject", "请问怎么平衡学习和玩游戏"]], title="Activity 4A: the e-mail header (the book leaves TO, CC and Subject blank)")
EM4T = [("你好！我是一名大学生，正在学中文。我也很喜欢玩“英雄联盟”，常常看你的比赛。我想请问你，怎么才能平衡学习和玩游戏？谢谢！", "Activity 4A (my sample e-mail): Hello! I am a university student studying Chinese. I also like playing “League of Legends” and often watch your matches. I’d like to ask you: how can one balance studying and playing games? Thank you! (Activity 4B asks you to pretend to be Faker and write the reply; I give no sample, since it would put invented words into a real person’s mouth.)")]
L2 = lesson(
    "Lesson 27 Presentation 3 skill integration: Faker and an e-mail about balancing study and games",
    "李相赫 · 英雄联盟 · 首尔大学 · 入学资格 · 电竞职业 · 学习和游戏 · 电子邮件",
    requires=[],
    cards=[
        card("Skill Integration, Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up and read the passages about Li Xianghe (Faker) and write a summary. B. With your partner, talk about the following topics. C. Share your discussion with the class. The passage (printed under the heading 李相赫, with two photos), the glosses, my summary and the questions:",
             tables=[FKG], examples=[D(*FK)] + [D(z, e) for z, e in FKS + FKQ]),
        card("Skill Integration, Activity 4 (Writing and Speaking)",
             "A. Pair up and compose a short e-mail to Faker. In your e-mail, introduce yourself to Faker and ask him how to balance studying and video game playing. B. With your partner, pretend that you are Faker and write an e-mail responding to the questions about balancing studying and video game playing. C. Share your writing with the class.",
             tables=[EM4], examples=[D(*EM4T[0])]),
    ],
    exercises=[
        M("Which game is Li Xianghe famous for?", "League of Legends", ["StarCraft", "Fortnite", "Chess"], "“英雄联盟”."),
        M("Where was he born?", "Seoul, Korea", ["Beijing", "Tokyo", "New York"], "在韩国首尔出生."),
        M("Who does he live with?", "His father", ["His teacher", "His cousin", "Alone"], "和爸爸在一起生活."),
        M("What has his father always believed?", "That he was born to be a professional e-sports player", ["That games are bad", "That he should be a doctor", "That he should move abroad"], "天生就是一个电竞职业选手."),
        M("How were his grades?", "Very good", ["Very bad", "Average", "Not mentioned"], "学习成绩也非常好."),
        M("What did he get an entry qualification for?", "Seoul National University", ["Peking University", "Yale", "Harvard"], "首尔大学的入学资格."),
        M("What did he choose to do?", "The e-sports profession instead of university", ["University instead of games", "A job in a bank", "To stop playing"], "选择了电竞职业."),
        M("What is said about his championships?", "He has won the most of any professional League of Legends player", ["He has never won", "He won one", "He won only abroad"], "获得冠军最多的职业选手."),
        F("李相赫和爸爸在一起生___。", "活", PART, "生活: live."),
        F("他选择了电竞职___。", "业", PART, "职业: profession."),
        F("他的电竞___术非常好。", "技", PART, "技术: skill."),
    ],
)

# ------------------------------------------------------------------ 3. using Chinese in context
UC1 = [("电竞行业在中国越来越火，现在已有五十万电子竞技员。", "Activity 1A-1 (true or false, audio; the book writes 50 万 in digits): The e-sports industry is getting hotter in China, and there are now already 500,000 e-sports players."), ("在中国，有的大学开始招收电竞专业的学生。", "1A-2: In China, some universities have begun to admit students in e-sports majors."), ("尽管电竞发展很快，很多人还是认为电竞员不是一个正式的工作。", "1A-3: Although e-sports is developing fast, many people still think e-sports players do not have a proper job."),
       ("所有的电竞员工资都很高，可以在一线城市买房子和汽车。", "1A-4: All e-sports players have very high pay and can buy houses and cars in first-tier cities."), ("电竞员除了每月的工资以外还有一些其他的收入。", "1A-5: Besides the monthly salary, e-sports players have some other income.")]
PC = table(["好的方面", "不好的方面"], [["做自己喜欢的事", "要长时间训练，压力很大"], ["电竞在中国非常流行，选手可以有大量的粉丝，成为明星", "选手要年轻，年纪大了反应慢，就很难再比赛"], ["可以代表国家参加大赛，得冠军", "有些人还不把电竞看作一个正式的工作"], ["现在人们认识到电子游戏是一种智力活动", "玩游戏的时间太长，对学习和身体都不好"]], title="Activity 1C: 当电竞员的好处和坏处 (my sample, from Presentation 3 and the skill-integration passages; the book leaves the table empty)")
UA = ("根据最近的一个调查，现在大学生平均一天要玩两个小时的游戏，男生女生都玩，而且越是好学校，玩游戏的人越多，很多人对这个调查结果表示担心。其实，把游戏看作是很可怕的事情是不对的。从这次调查结果来看，有不少和我们以前对游戏的看法有不同的地方。比如，我们过去认为男孩子更喜欢玩游戏，但这次调查却表明，男女都喜欢玩游戏，这说明游戏受到很多人的喜爱。另外我们也应该认识到，游戏已经成为一种娱乐和社交工具，就像有些人喜欢唱歌，游泳，下棋一样。",
      "Paragraph 1. According to a recent survey, university students now play games for two hours a day on average, boys and girls both play, and the better the school the more people play games; many people expressed worry about the result of this survey. Actually, it is wrong to regard games as a very frightening thing. Judging from the result of this survey, there are quite a few differences from our former views of games. For example, we used to think boys liked playing games more, but this survey shows that both boys and girls like playing games, which shows that games are loved by many people. In addition we should also realize that games have become a tool for entertainment and socializing, just as some people like singing, swimming and playing chess. (translation mine)")
UB = ("这次调查还发现好学校的学生更爱玩游戏，很多人认为他们进了好学校就放松了学习。我不这样认为。有些学生既会学习又会玩，也喜欢社交活动，因为他们有好的学习方法，所以有时间去玩自己喜欢的东西。当然，如果大学生每天就是玩电子游戏，而没有其他的社交活动，或是对学习以及生活中的事情没有兴趣，这就需要去改变这种情况。",
      "Paragraph 2. This survey also found that students at good schools like playing games even more, and many people think that once they enter a good school they relax their studies. I don’t think so. Some students both study well and play well and also like social activities; because they have good study methods, they have time to play what they like. Of course, if a university student just plays video games every day, without other social activities, or has no interest in studying and the things in life, then this situation needs to be changed. (translation mine; the book divides the text into three paragraphs, with the second beginning at 其实, and the third at 这次调查还发现; I print it as two blocks)")
UK = table(["", "主要词汇和信息 (my sample)"], [["第一段", "调查; 大学生平均一天玩两个小时; 男女都玩; 好学校玩的人更多; 游戏是娱乐和社交工具"], ["第二段", "看作很可怕是不对的; 以前认为男孩子更喜欢; 调查表明男女都喜欢"], ["第三段", "好学校的学生更爱玩; 不是放松学习; 有好的学习方法; 每天只玩游戏就需要改变"]], title="Activity 2A: key words and information, by paragraph (my sample)")
US = [("先做完作业和复习，再玩游戏，不要让游戏影响学习。", "Activity 2B suggestion 1 (mine): Finish homework and review first and then play games; don’t let games affect studying."), ("订一个时间表，每天只玩一两个小时，到时间就关机。", "Suggestion 2 (mine): Make a timetable, play only an hour or two a day and turn off the machine when time is up."), ("多参加社交活动和运动，找一些别的兴趣。", "Suggestion 3 (mine): Take part in more social activities and sports and find other interests.")]
GRA = table(["游戏直播平台", "游戏主播", "有多少粉丝", "为什么好看"], [["Twitch; YouTube", "(look up your favorite)", "(look up)", "可以一边看比赛一边和主播聊天"]], title="Activity 3A, Group A: game streaming (the book leaves the cells empty; one sample row, mine)")
GRB = table(["游戏名字", "游戏玩主", "游戏特点", "为什么好玩"], [["我的世界 (Minecraft)", "(look up your favorite; the book’s heading prints 玩主)", "可以自己盖房子，造东西", "很自由，可以跟朋友一起玩"]], title="Activity 3A, Group B: video games (the book leaves the cells empty; one sample row, mine)")
L3 = lesson(
    "Lesson 27 Presentation 3 using Chinese in context: persuading a mother, balancing study and play, game recommendations",
    "当电竞员的好处和坏处 · 游戏调查 · 大学生玩游戏 · 平衡学习和玩 · 游戏直播平台 · 游戏名字",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Listening, Reading, Writing and Speaking)",
             "Scenario: Your Chinese roommate is going to graduate from college and wants to be an e-sports player. However, his mother doesn’t want him to engage in e-sports and hopes he can find a regular job. Your roommate asks you to persuade his mother to agree with his decision. A. Listen to the recording and mark the following statements as either True or False. B. Pair up and check your answers with your partner’s. Discuss what information can be used to convince your roommate’s mother. C. With your partner, discuss the pros and cons of playing e-sports as a career, using information from the recording and your personal experience. Provide at least three points for each aspect. D. Each pair takes turns presenting the pros and cons to persuade your roommate’s mother. (The recording is not in the book, so the statements have no key.)",
             tables=[PC], examples=[D(z, e) for z, e in UC1]),
        card("Using Chinese in Context, Activity 2 (Reading, Writing and Speaking)",
             "Scenario: You are currently enrolled in an intensive Chinese basic course and your schedule of Chinese studies is very tight. Your teacher is aware that some students spend a lot of time playing video games or watching game streaming. To help students better manage their time, your teacher initiates a discussion in the class on how to balance study and play. A. Pair up, read the article, and write the key words and key information that are useful for your discussion on how to help your classmates achieve this balance. B. In two groups, read the article again and discuss whether you agree with the author’s opinion. Find new suggestions to help your classmates better manage time and balance study and play. Provide at least three suggestions. C. Each group takes turns presenting their suggestions, followed by questions and discussion. The article, my key words and my suggestions:",
             tables=[UK], examples=[D(*UA), D(*UB)] + [D(z, e) for z, e in US]),
        card("Using Chinese in Context, Activity 3 (Reading, Writing, and Speaking)",
             "Scenario: You are sharing an apartment with a Chinese student. Your roommate has just come to the U.S. and wants to know which social media platform has interesting game streaming and streamers. Your roommate also asks you to recommend some fun video games and the best players. A. Form two groups; Group A discusses game streaming on social media and Group B discusses video games. Write suggestions in the table and prepare to explain why they are interesting to your roommate. B. Present your discussion to the class and explain why your roommate would like your suggestions. The two tables, with one sample row each:",
             tables=[GRA, GRB]),
    ],
    exercises=[
        M("What does the survey say about university students’ game time?", "About two hours a day on average", ["Ten hours a day", "None", "Only on weekends"], "平均一天要玩两个小时的游戏."),
        M("Which kind of school has more students playing games?", "Better schools", ["Worse schools", "Only art schools", "No schools"], "越是好学校，玩游戏的人越多."),
        M("What does the author say about treating games as frightening?", "It is wrong", ["It is right", "It is necessary", "It is new"], "是不对的."),
        M("What did people used to think about who likes games?", "Boys like them more", ["Girls like them more", "Only adults like them", "Nobody likes them"], "我们过去认为男孩子更喜欢玩游戏."),
        M("What does the survey show instead?", "Both boys and girls like playing games", ["Only boys like games", "Only girls like games", "Nobody plays"], "男女都喜欢玩游戏."),
        M("What have games become, according to the author?", "A tool for entertainment and socializing", ["A school subject", "A kind of food", "A kind of money"], "一种娱乐和社交工具."),
        M("What do some students do, according to the third paragraph?", "Study well and play well and enjoy social activities", ["Never study", "Never play", "Only sleep"], "既会学习又会玩."),
        M("When does the author think the situation needs to change?", "When a student only plays games every day and has no other interests", ["When a student plays games once a week", "When a student likes sports", "When a student studies hard"], "如果大学生每天就是玩电子游戏…"),
        F("根据最近的一个调___，现在大学生平均一天要玩两个小时的游戏。", "查", PART, "调查: survey."),
        F("游戏已经成为一种娱乐和社___工具。", "交", PART, "社交: social contact."),
        F("有些学生既会学习又会玩，也喜欢社交活___。", "动", PART, "活动: activities."),
    ],
)

# ------------------------------------------------------------------ 4. vocabulary
L4 = vocab_lesson("Lesson 27 Presentation 3 vocabulary", "19 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. Several cells are broken by page layout in the PDF; the entries 英雄联盟, 王者荣耀, 星际争霸 and 电竞 are written out in full.", VOC3)

# ------------------------------------------------------------------ 5. area studies
AS1 = ("Ten years ago, the choice of products that 800 million rural Chinese consumers could buy depended on what the commissaries sold. Nowadays, when farmers place orders on their mobile phones, goods from cities can be delivered directly to the village. Farmers can buy the same goods at the same price as buyers in the city. Receiving express deliveries has become a part of daily life. In fact, as early as 2014, China launched e-commerce projects in rural areas. It has supported 1,180 counties and achieved coverage of 832 national-level, poverty-stricken counties so far. Rural e-commerce has developed rapidly, and rural online retail sales have increased from 180 billion yuan in 2014 to 1.7 trillion yuan in 2019, as the overall scale has expanded 8.4 times.")
AS2 = ("The development of rural e-commerce has achieved remarkable results. Due to the construction of rural infrastructure over the years, including the rapid development of communications, logistics, and electronic payment, the various obstacles to e-commerce in the countryside were eliminated. Statistics show that the current number of rural Internet users in China has exceeded 250 million. The average number of bank cards held by each individual in rural areas across the country is 3.61. The number of mobile banking and online banking accounts in rural areas has reached 816 million and 712 million respectively. Banking institutions, third-party payment institutions, telecommunications operators, and Internet technology companies have strengthened their cooperation by allowing rural households to use mobile payments and online payments, which gradually eliminate payment service gaps in rural areas. Nowadays, online shopping has become a norm in farmers’ lives. More and more services and commodities have entered the countryside through e-commerce, which has changed farmers’ lives and consumption habits. (The picture caption reads: 拼多多创尔女装官方旗舰店主播聂建茹正在直播, “Nie Jianru, the streamer of the Pinduoduo Chuang’er women’s wear official flagship store, is live streaming”; the picture is not included.)")
AS3 = ("At the same time, growing rural e-commerce has greatly broadened the sales channels of agricultural products and promoted farmers’ entrepreneurship and employment. Marketing local produce through livestreaming platforms became popular. According to statistics published by the Alibaba Group, at the end of March 2020, more than 60,000 Chinese farmers were registered as hosts on the Taobao platform. Fields, greenhouses, warehouses and even fishing boats have been transformed into livestreaming studios. The fresh food channel on Taobao alone brings together 168,000 types of agricultural products from 832 poor counties in China and has made 2.5 billion yuan (352 million USD) in sales since January 2020. The agricultural specialty products of some poor villages have become “net celebrity” brands in a short period of time.")
AS4 = ("In order to help farmers better adapt to this new kind of sales channel, government at all levels and the main e-commerce platforms in China have taken various measures to support these new hosts, providing technical training or organizing events dedicated to the sale of products from the country’s poorest regions. Rural e-commerce logistics continue to accelerate the trend of “industrial products exported to the countryside and agricultural products imported to the city”. It has also provided support for the production and sales of agricultural products. Sales of agricultural products through livestreaming platforms have played an important role in the fight against poverty in recent years. The development of rural e-commerce and the implementation of targeted poverty alleviation are deeply integrated to increase the income of the poor while solving unemployment. According to data from the China E-commerce Poverty Alleviation Alliance in 2019, its member units sold more than 2.8 billion yuan of agricultural products in poverty-stricken areas, covering 842 enterprises in 478 poverty-stricken counties in 22 provinces and assisted 80,000 farmers. As of March 2020, national-level e-commerce in poverty-stricken counties has employed more than 9 million farmers. E-commerce has effectively achieved poverty alleviation and rural revitalization in China. References (titles of the sites only; the web addresses are left out): Logclub, Sina Finance, China.org.cn and ChinAfrica.")
L5 = lesson(
    "Lesson 27 Area Studies: E-commerce in Rural China",
    "农村电商 · 直播卖农产品 · 淘宝 · 脱贫 · 手机支付 · 农民 · 乡村振兴",
    requires=[],
    cards=[
        card("E-commerce in Rural China (1): deliveries to the village", AS1),
        card("(2): infrastructure and payment", AS2),
        card("(3): livestreaming farmers", AS3),
        card("(4): support measures and the fight against poverty", AS4),
    ],
    exercises=[
        M("How many rural Chinese consumers were mentioned ten years ago?", "800 million", ["80 million", "8 million", "8 billion"], "800 million."),
        M("What can farmers do now when they place orders on their phones?", "Get goods from cities delivered directly to the village", ["Only buy local goods", "Pay more than city buyers", "Stop shopping"], "Goods are delivered directly."),
        M("When did China launch rural e-commerce projects?", "2014", ["1994", "2004", "2024"], "As early as 2014."),
        M("How many counties has it supported?", "1,180", ["118", "11,800", "832"], "1,180 counties."),
        M("How many national-level poverty-stricken counties are covered?", "832", ["1,180", "478", "22"], "832."),
        M("What were rural online retail sales in 2019?", "1.7 trillion yuan", ["180 billion yuan", "2.5 billion yuan", "9 million yuan"], "From 180 billion in 2014 to 1.7 trillion in 2019."),
        M("By how many times did the overall scale expand?", "8.4", ["84", "0.84", "4.8"], "8.4 times."),
        M("Roughly how many rural Internet users exceed in number?", "250 million", ["25 million", "2.5 billion", "250,000"], "Exceeded 250 million."),
        M("What is the average number of bank cards held by each rural individual?", "3.61", ["36.1", "0.361", "1"], "3.61."),
        M("How many farmers were registered as hosts on Taobao by the end of March 2020?", "More than 60,000", ["More than 600", "More than 6 million", "Exactly 6"], "More than 60,000."),
        M("Where have livestreaming studios been set up?", "Fields, greenhouses, warehouses and even fishing boats", ["Only in Beijing", "Only in schools", "Only in hotels"], "Fields, greenhouses, warehouses, fishing boats."),
        M("How many types of agricultural products does the Taobao fresh food channel bring together?", "168,000", ["16,800", "1.68 million", "832"], "168,000 types."),
        M("What is the trend that rural e-commerce logistics accelerate?", "Industrial products exported to the countryside and agricultural products imported to the city", ["Only exporting grain", "Closing villages", "Stopping deliveries"], "The quoted trend."),
        M("How many farmers had national-level e-commerce in poverty-stricken counties employed as of March 2020?", "More than 9 million", ["More than 90,000", "More than 900", "More than 90 million"], "More than 9 million."),
    ],
)

UNIT = unit("第二十七课 Presentation 3: 堡垒之夜, 亚运会电竞, 李相赫, 游戏和学习, 词汇, Area Studies", [L1, L2, L3, L4, L5])
