"""Unit 50: Lesson 17 (Sports and Fitness) Presentation 3 and Area Studies from the book's texts: the Zhang Dongming family passage,
the preposition 为了/为, the degree adverb 更, 不管……都……, the time words 后来/以后/然后, the skill-integration passages (Zhang Jun's
family, the article on Xi Jinping's hobbies, Li Jun) and the using-Chinese activities, the vocabulary list and the Sports in China
reading. Audio, pictures, videos and websites are not included; the book writes numbers as digits and they are spelled out in spoken
text; answer keys the book does not print (and blanks it leaves for the student) are mine and labeled."""
from zh_auto import *
from zh_l17_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("长得", 0, "zhang3"), ("长大", 0, "zhang3"), ("长到", 0, "zhang3"), ("得了很多", 0, "de2"), ("得吃", 0, "dei3"), ("得陪", 0, "dei3"), ("得先", 0, "dei3"), ("得去", 0, "dei3"), ("校长", 1, "zhang3"), ("睡觉", 1, "jiao4"), ("睡着", 1, "zhao2"), ("没有时间", 0, "mei2"), ("没来", 0, "mei2"),
                          ("没有给", 0, "mei2"), ("都会", 0, "dou1"), ("人参加", 1, "can1"), ("教练", 0, "jiao4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5
        if ch == "地" and j > 0 and zh[j - 1] not in "当草土天各山场内本外基实陆" and (j + 1 >= len(zh) or zh[j + 1] not in "道址方铁图球区点上下面理"):
            f[j] = "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the passage
ZD = ("张东明是一个足球迷。他最喜欢的球星是巴塞罗那俱乐部的梅西，所以他收集了很多梅西的海报。只要电视上有球赛，他就不会错过。为了看球赛，他常常熬夜。他也喜欢去现场看球，因为和别的球迷一起看球更热闹。他最大的愿望就是攒钱去巴塞罗那看一次梅西的主场比赛。有空儿的时候，他也会约几个朋友踢球。虽然他踢得不太好，可是不管输赢，他都很开心。"
      "张东明的太太是个篮球迷，她从上中学起就开始打球。后来，她在一个高中当体育老师，也是学校篮球队的教练。他们有一个儿子叫张新，今年十一岁，上六年级。他从小就跟爸爸妈妈一起看球赛。他说他长大以后要当一个体育记者，这样就可以经常去世界各地免费看球赛了。")
ZD_E = ("Zhang Dongming is a soccer fan. His favorite star is Messi of the Barcelona club, so he has collected many Messi posters. Whenever there is a match on TV, he won’t miss it. In order to watch matches, he often stays up late. He also likes to watch games live, because watching with other fans is livelier. His biggest wish is to save money and go to Barcelona to see one of Messi’s home games. When he has time, he also invites a few friends to play soccer. Although he doesn’t play very well, he is happy regardless of winning or losing. "
        "Zhang Dongming’s wife is a basketball fan; she began playing basketball from the time she was in middle school. Later she became a physical education teacher at a high school and is also the coach of the school’s basketball team. They have a son named Zhang Xin, who is eleven this year and in the sixth grade. Since childhood he has watched games with his father and mother. He says that when he grows up he wants to be a sports reporter, so that he can often go all over the world to watch matches for free.")
AC4_3 = [("张军是个足球迷。明天晚上有欧洲杯足球赛，张军打算熬夜看球赛。", "1. Zhang Jun is a soccer fan. Tomorrow night there is a European Cup match and Zhang Jun plans to stay up late to watch it. (熬夜; key mine)"), ("下个周末，大卫请我一起去工人体育场看中国女足和美国女足的现场比赛。", "2. Next weekend, David invited me to the Workers’ Stadium to watch the Chinese and American women’s soccer teams play live. (现场)"), ("王力从小就喜欢看篮球。每次电视上有篮球联赛，他都不错过。", "3. Wang Li has liked watching basketball since childhood. Whenever there is a basketball league game on TV, he never misses it. (错过; the book writes the league’s name in English)"),
         ("今天晚上德国和英国足球赛的主场在德国，你认为德国会赢吗？", "4. Tonight’s Germany–England soccer match has its home field in Germany; do you think Germany will win? (主场)"), ("李华特别喜欢足球。一上大学就参加了学校的足球俱乐部。", "5. Li Hua especially likes soccer. As soon as he went to college he joined the school’s soccer club. (俱乐部)"), ("我爸爸是个足球迷。虽然去国外看球很贵，他也要攒钱去看。", "6. My dad is a soccer fan. Although going abroad to watch a game is expensive, he wants to save money and go. (攒钱)"),
         ("昨天，我哥哥的朋友送了他一张免费的摇滚乐演出票。", "7. Yesterday my older brother’s friend gave him a free ticket to a rock concert. (免费)"), ("我弟弟最喜欢篮球，他收集了很多篮球明星的海报。", "8. My younger brother likes basketball best; he has collected many posters of basketball stars. (收集)"), ("很多人喜欢参加体育比赛，不管输赢都觉得很开心。", "9. Many people like taking part in sports competitions and feel happy whether they win or lose. (输赢)"),
         ("我最大的愿望就是去欧洲看一场世界杯足球赛。", "10. My biggest wish is to go to Europe and watch a World Cup soccer game. (愿望; the book adds the English name)")]
ODD = [("免费，攒钱，熬夜，俱乐部", "Group 1. Mine: 俱乐部 is a noun while the other three are verbs or verb-object phrases."), ("海报，愿望，错过，记者", "Group 2. Mine: 错过 is a verb while the others are nouns."), ("输赢，主场，现场，巴塞罗那", "Group 3. Mine: 输赢 is about the result while the others are places."), ("球星，球迷，体育，收集", "Group 4. Mine: 收集 is a verb while the others are nouns about sports.")]
SURVEY = [("你喜欢去现场看球赛还是喜欢在电视上看？为什么？", "1. Do you like to watch ball games live or on TV? Why?"), ("为了去现场看球赛，你会花很多钱买票吗？为什么？", "2. In order to watch a game live, would you spend a lot of money on tickets? Why?"), ("比赛不管输赢，只要能参加就很开心。你同意吗？", "3. Whether the game is won or lost, it’s enough to be able to take part. Do you agree?"), ("你认为篮球和足球，哪个更有意思？为什么？", "4. Which do you think is more interesting, basketball or soccer? Why?")]
L1 = lesson(
    "Lesson 17 Presentation 3: ball-game fans",
    "张东明是一个足球迷 · 收集海报 · 熬夜看球赛 · 最大的愿望",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: a soccer match, a basketball game (not included). Pair up and discuss: A. Do you like soccer or basketball? If yes, who is your favorite player? B. Have you ever watched or played soccer or basketball in a stadium? When was that? C. Does any of your family members or friends like to play soccer or basketball? Are they the fans of any star players? If yes, who are those players?"),
        card("Presentation 3: 球迷一家",
             "The book also prints the passage in traditional characters.",
             examples=[D(ZD, ZD_E)]),
        card("Activities 1 and 2 (listening)",
             "Activity 1 (Listening, Writing and Speaking). A. Global listening: 1. What is the topic of this presentation? 2. What is common among all the family members? B. Detailed listening: fill in the boxes with details about each family member’s recreational interests (张东明, 张太太, 儿子张新). C. Pair up, discuss and read Presentation 3 again if necessary. (From the passage, mine: ball games; they all love watching or playing ball games. 张东明: soccer fan, loves Messi, collects posters, stays up late, wishes to see Messi’s home game in Barcelona; 张太太: basketball fan, a high-school PE teacher and the coach of the school team; 张新: age eleven in sixth grade, watches games with his parents, wants to be a sports reporter.) Activity 2 (Listening, Writing and Speaking). Listen to Passages 1, 2 and 3, write a summary of each, exchange summaries, and talk with your partner about a parent’s favorite sports and players and about your own favorite sports and player and why. (Audio, not included.)"),
        card("Activity 3 (Reading and Speaking)",
             "Pair up and discuss the following words. Select any word that seems odd in each group and explain why those words were chosen. The book leaves the explanations blank; several answers are possible, and mine are:",
             examples=[D(z, e) for z, e in ODD]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Complete the sentences using the words 输赢, 错过, 攒钱, 免费, 熬夜, 收集, 愿望, 现场, 主场, 俱乐部. B. Pair up, check your work, read the sentences aloud and translate them into English. The book leaves the key out; my completed sentences (mine). The book writes NBA and FIFA World Cup in English in sentences 3 and 10; here they are 篮球联赛 and 世界杯:",
             examples=[D(z, e) for z, e in AC4_3]),
        card("Activity 5 (Reading, Speaking and Writing): Quick Survey",
             "A. Interview at least two students in your class and ask the following questions; note their answers (学生1的回答 / 学生2的回答). B. Consolidate your notes and report your findings to the class.",
             examples=[D(z, e) for z, e in SURVEY]),
    ],
    exercises=[
        M("Who is Zhang Dongming’s favorite star?", "Messi of Barcelona", ["Jordan", "Kobe", "Yao Ming"], "梅西."),
        M("What does Zhang Dongming collect?", "Messi posters", ["Tickets", "Balls", "Shirts"], "收集了很多梅西的海报."),
        M("Why does he often stay up late?", "To watch matches", ["To work", "To study", "To play"], "为了看球赛，他常常熬夜."),
        M("What is his biggest wish?", "To save money and go to Barcelona to see a home game", ["To play for Barcelona", "To become a coach", "To buy a team"], "攒钱去巴塞罗那看一次梅西的主场比赛."),
        M("How does he feel about winning or losing?", "Happy either way", ["Angry when he loses", "Only happy when he wins", "Doesn’t care at all"], "不管输赢，他都很开心."),
        M("What does his wife do?", "High-school PE teacher and basketball coach", ["Reporter", "Doctor", "Shop owner"], "高中当体育老师，也是学校篮球队的教练."),
        M("How old is Zhang Xin?", "Eleven", ["Ten", "Twelve", "Sixteen"], "今年十一岁."),
        M("What does Zhang Xin want to be?", "A sports reporter", ["A coach", "A teacher", "A player"], "要当一个体育记者."),
        M("Why does he want that job?", "To watch games around the world for free", ["Because it pays well", "Because he is shy", "Because his father said so"], "免费看球赛."),
        mean("记者", "ji4 zhe3", "reporter", ["coach", "fan", "player"]),
        mean("愿望", "yuan4 wang4", "wish", ["fan", "club", "result"]),
        F("他最大的___望就是攒钱去巴塞罗那看一次比赛。", "愿", PART, "愿望."),
        F("他也喜欢去现场看球，因为和别的球迷一起看球更___闹。", "热", PART, "热闹."),
    ],
)

# ------------------------------------------------------------------ 2. 为了/为
WL = [("为了看球赛，他常常熬夜。", "In order to watch ball games, he often stays up late. (为了 + Verb)"), ("为了减肥，她常常去健身房运动。", "In order to lose weight, she often goes to the gym to exercise."), ("为了家人，她什么都愿意做。", "For her family, she is willing to do anything. (为了 + Noun)"),
      ("放暑假的时候，妈妈为我做很多好吃的。", "During summer vacation, Mom makes lots of delicious food for me. (为 + Pronoun)"), ("我们校长为老师和学生做了很多事。", "Our principal has done many things for the teachers and students. (为 + Noun)")]
WL2 = [("王林为了挣钱交学费。", "1. Why does Wang Lin work as a waiter in a restaurant on weekends? To earn money for tuition. (mine)"), ("老李为了看世界杯足球赛。", "2. Why did Old Li stay up late? In order to watch the World Cup match. (mine)"), ("赵新为了陪生病的孩子去医院。", "3. Why didn’t Zhao Xin come to work today? To take his sick child to the hospital. (mine)"),
       ("大卫为了参加学校的足球比赛。", "4. Why does David practice soccer every day? In order to take part in the school soccer game. (mine)"), ("小明的妈妈为了给他过生日。", "5. Why is Xiao Ming’s mother inviting many friends to his home next weekend? In order to celebrate his birthday. (mine)")]
L2 = lesson(
    "Lesson 17 Presentation 3 grammar: the preposition 为了/为",
    "为了看球赛 · 为了减肥 · 为我做很多好吃的 · 为了 = in order to; 为 = for",
    requires=[],
    cards=[
        card("The Preposition 为了/为",
             "The preposition 为了 indicates the purpose of an action. It means “in order to” and is often used at the beginning of the sentence. 为了 + Noun/Verb. The preposition 为 means “for,” “for the reason of,” “for the sake of,” and “on behalf of.” 为 can precede nouns and pronouns. 为 + Noun/Pronoun. The book prints the five examples without English; the translations are mine.",
             examples=[D(z, e) for z, e in WL]),
        card("Activities 1 and 2",
             "Activity 1 (Listening, Writing, Speaking and Reading). A. Listen to six sentences with 为了/为 and translate them into English. B. Pair up, discuss your translations and repeat them in Chinese. (Audio, not included; the book’s instruction here says 才 by mistake.) Activity 2 (Reading and Speaking): 猜一猜! Pair up and answer the following questions with 为了. 1. 王林为什么周末的时候在餐馆当服务员？ 2. 昨天晚上有世界杯足球赛。老李为什么熬夜？ 3. 你知道今天赵新为什么没来上班？ 4. 你知道大卫为什么天天要练习踢足球？ 5. 小明的妈妈为什么下个周末请很多朋友来他家？ My guesses (mine):",
             examples=[D(z, e) for z, e in WL2]),
    ],
    exercises=[
        M("What does 为了 indicate?", "The purpose of an action (in order to)", ["The place", "The time", "The result"], "为了 = in order to."),
        M("What does 为 mean before a noun or pronoun?", "For / for the sake of / on behalf of", ["In order to", "Because of the past", "Instead"], "为 + noun/pronoun."),
        M("Where is 为了 often placed?", "At the beginning of the sentence", ["At the end", "After the object", "Before 吗"], "为了 at the start."),
        M("What does 为了减肥，她常常去健身房运动 mean?", "In order to lose weight, she often goes to the gym", ["She lost weight at the gym", "She hates the gym", "She will go once"], "为了减肥."),
        M("What does 妈妈为我做很多好吃的 mean?", "Mom cooks lots of delicious food for me", ["I cook for Mom", "Mom ate lots", "Mom bought lots"], "为我."),
        M("Which fits “For her family she would do anything”?", "为了家人，她什么都愿意做", ["因为家人，她什么都愿意", "家人为了她什么都愿意做", "她什么都家人愿意做"], "为了 + noun."),
        F("___了看球赛，他常常熬夜。", "为", PART, "为了."),
        F("我们校长___老师和学生做了很多事。", "为", PART, "为 + noun."),
    ],
)

# ------------------------------------------------------------------ 3. 更
GN = [("他喜欢去现场看球，因为和别的球迷一起看球更热闹。", "He likes to watch games live, because watching with other fans is livelier. (更 + Adj.)"), ("张新喜欢篮球和足球，但更喜欢乒乓球。", "Zhang Xin likes basketball and soccer, but likes table tennis even more. (更 + Verb)"), ("在现场看球比在家里看球更热闹。", "Watching a game live is even livelier than watching at home. (A 比 B 更 + Adj.)"), ("我们的球队比你们的球队打得更好。", "Our team plays even better than your team.")]
GN4 = [("你经常在网上买东西吗？", "Example. A: Do you often shop online?"), ("有时候在网上买，但是我更喜欢去商店买。", "B: Sometimes I buy online, but I prefer going to the stores. (the book’s example)"), ("王英，你喜欢去哪儿锻炼身体？", "1. A: Wang Ying, where do you like to exercise?"), ("我喜欢去健身房，但是我更喜欢去海边跑步。", "B: I like going to the gym, but I like running by the sea even more. (mine)"),
       ("李东，你喜欢哪个篮球明星？", "2. A: Li Dong, which basketball star do you like?"), ("我喜欢乔丹，不过我更喜欢科比。", "B: I like Jordan, but I like Kobe more. (mine; the book writes the names in English too)"), ("林老师，听说您做饭做得非常好？", "3. A: Teacher Lin, I heard you cook very well?"), ("还可以，不过我太太做得比我更好。", "B: Not bad, but my wife cooks even better than I do. (mine)"),
       ("今年蒙特雷的冬天不是很冷。", "4. A: This year Monterey’s winter isn’t very cold."), ("是啊，不过夏威夷的冬天更暖和。", "B: Yes, but Hawaii’s winter is even warmer. (mine)"), ("琳达，你喜欢打什么球？", "5. A: Linda, what ball sport do you like to play?"), ("我喜欢足球和篮球，不过我更喜欢乒乓球。", "B: I like soccer and basketball, but I like table tennis even more. (mine)"),
       ("马克，你喜欢什么户外运动？", "6. A: Mark, what outdoor sport do you like?"), ("我喜欢滑雪和滑冰，但是我更喜欢冲浪。", "B: I like skiing and ice skating, but I like surfing even more. (mine)")]
L3 = lesson(
    "Lesson 17 Presentation 3 grammar: the degree adverb 更",
    "和别的球迷一起看球更热闹 · 更喜欢乒乓球 · A 比 B 更…",
    requires=[],
    cards=[
        card("The Degree Adverb 更",
             "The degree adverb 更 can be used before adjectives/verbs to express “even more.” 更 + Adjective/Verb. 更 is also used in a sentence that shows comparison when introduced by 比. A 比 B + 更 + Adjective.",
             examples=[D(z, e) for z, e in GN]),
        card("Activities 3 and 4",
             "Activity 3 (Listening, Speaking and Writing). A. Listen to the conversation and take notes on what activities each speaker likes to do with their spare time and why they prefer one activity over others (the table has 喜欢 / 更喜欢 / 因为 for each speaker, beginning with 王力). B. Using the information you have heard about the use of 更, write a few descriptive sentences beneath each of four groups of images. (Audio and pictures, not included.) Activity 4 (Reading, Writing and Speaking). A. Complete the brief dialogs with 更 and the words in parentheses. B. Pair up, check your sentences and translate what you wrote into English. The book’s example and my answers (mine):",
             examples=[D(z, e) for z, e in GN4]),
    ],
    exercises=[
        M("What does 更 express?", "Even more", ["Not at all", "A little", "Exactly"], "更 = even more."),
        M("Where does 更 go in a 比 sentence?", "After 比 B, before the adjective", ["Before 比", "At the end", "After the adjective"], "A 比 B 更 + Adj."),
        M("What does 张新…但更喜欢乒乓球 mean?", "He likes table tennis even more", ["He dislikes table tennis", "He plays no ball", "He likes only soccer"], "更喜欢."),
        M("What does 在现场看球比在家里看球更热闹 mean?", "Watching live is livelier than watching at home", ["Watching at home is livelier", "Both are boring", "Watching live is cheaper"], "比…更…"),
        M("Which is correct?", "我们的球队比你们的球队打得更好", ["我们的球队更比你们的球队打得好", "我们的球队比你们的球队更打得好", "更我们的球队比你们打得好"], "A 比 B 打得更好."),
        M("Which sentence expresses a preference?", "我喜欢足球，但是我更喜欢篮球", ["我很喜欢足球", "我不喜欢足球", "我昨天看了足球"], "更喜欢."),
        F("夏威夷的冬天___暖和。", "更", PART, "更 + adjective."),
        F("在现场看球___在家里看球更热闹。", "比", PART, "A 比 B 更…"),
    ],
)

# ------------------------------------------------------------------ 4. 不管…都…
BG = [("虽然他踢得不太好，可是不管输赢，他都很开心。", "Although he doesn’t play very well, he is very happy regardless of winning or losing."), ("不管明天下不下雨，我们都要去爬山。", "We must go hiking whether it rains or not."), ("妈妈常常对我说，不管你有没有时间，都得吃早饭。", "My mother always says to me, whether you have time or not, you must eat breakfast.")]
BG6 = [("今天我做晚饭，你想吃什么？", "1. A: I’ll cook dinner today; what do you want to eat?"), ("不管你做什么，我都爱吃。", "B: No matter what you cook, I love it. (mine)"), ("这个周末我们去哪儿玩比较好？", "2. A: Where would be better to go this weekend?"), ("不管去哪儿，我都愿意。", "B: No matter where, I’m willing. (mine)"),
       ("今天我有点儿不开心，我可以不上课吗？", "3. A: I’m a little unhappy today; may I skip class?"), ("不管你开心不开心，都得去上课。", "B: Whether you’re happy or not, you have to go to class. (mine)"), ("我不太喜欢逛商店，你和别人去行吗？", "4. A: I don’t much like shopping; is it OK if you go with someone else?"), ("不管你喜欢不喜欢，今天你都得陪我去。", "B: Whether you like it or not, you have to go with me today. (mine)"),
       ("我不想弹钢琴，我可以玩游戏吗？", "5. A: I don’t want to play the piano; may I play games?"), ("不管你想不想弹，都得先练习半个小时。", "B: Whether you want to or not, you have to practice for half an hour first. (mine)"), ("我知道你不高兴，你今天谁都不想见吗？", "6. A: I know you’re unhappy; do you not want to see anyone today?"), ("不管谁来，我都不想见。", "B: No matter who comes, I don’t want to see them. (mine)")]
JOKE = [("爸爸：小明，爸爸今天太累了，不管谁打来电话，你都说我不在家。", "Dad: Xiao Ming, Dad is too tired today. No matter who calls, you say I’m not at home."), ("小明（接电话）：喂，我爸爸说他不在家。", "Xiao Ming (answering the phone): Hello, my dad says he’s not at home.")]
L4 = lesson(
    "Lesson 17 Presentation 3 grammar: the construction 不管……都……",
    "不管输赢，他都很开心 · 不管明天下不下雨，我们都要去爬山 · 开心一刻",
    requires=[],
    cards=[
        card("The Construction 不管…，都…",
             "不管 means “no matter,” “regardless” and “in despite of.” It appears at the beginning of the sentence. 都 is used in the second part of the sentence to emphasize that the action or decision will not change. 不管…，都…",
             examples=[D(z, e) for z, e in BG]),
        card("Activities 5 and 6",
             "Activity 5 (Listening and Speaking). A. Listen to six sentences with 不管…，都… and translate them into English. B. In pairs, check your translation and repeat the sentences in Chinese. (Audio, not included.) Activity 6 (Reading and Writing). Pair up and write answers to the six questions using 不管…，都… (the book leaves the lines blank; mine):",
             examples=[D(z, e) for z, e in BG6]),
        card("Activity 7 (Reading and Speaking): 开心一刻",
             "Read the joke. Do you find it funny? Do you have a joke to tell the class?",
             examples=[D(z, e) for z, e in JOKE]),
    ],
    exercises=[
        M("What does 不管…，都… mean?", "No matter …, … all the same", ["Because …, so …", "If …, then …", "Although …, but …"], "不管…都…: regardless."),
        M("Where does 不管 appear?", "At the beginning of the sentence", ["At the end", "After 都", "Before the object"], "不管 first."),
        M("What does 都 emphasize here?", "The action or decision will not change", ["The past", "A question", "A wish"], "都 emphasizes it won’t change."),
        M("What does 不管输赢，他都很开心 mean?", "He is happy whether he wins or loses", ["He is sad when he loses", "He always wins", "He doesn’t play"], "不管输赢."),
        M("What does 不管明天下不下雨，我们都要去爬山 mean?", "We’ll go hiking whether or not it rains", ["We’ll go if it rains", "We won’t go", "We’ll go only if it’s sunny"], "不管下不下雨."),
        M("What is the joke’s twist?", "Xiao Ming tells the caller his dad says he’s not at home", ["Dad answers the phone", "Xiao Ming hangs up", "The caller hangs up"], "我爸爸说他不在家."),
        F("不管输赢，他___很开心。", "都", PART, "不管…都…"),
        F("___管你有没有时间，都得吃早饭。", "不", PART, "不管."),
    ],
)

# ------------------------------------------------------------------ 5. 后来/以后/然后
HL = [("她从上中学起就开始打球。后来，她在一个高中当体育老师。", "She began playing from middle school on. Later she became a PE teacher at a high school. (后来: past)"), ("他说他长大以后要当一个体育记者。", "He says that when he grows up he wants to become a sports reporter. (以后: future)"), ("十年前我在这儿住过，以后就再没来过。", "Ten years ago I lived here; ever since then I have never come again. (以后)"), ("十年前我在这儿住过，后来就再没来过。", "Ten years ago I lived here; after that I never came again. (后来)"),
      ("这个问题以后再说。", "Let’s talk about this problem later. (correct)"), ("我下课以后去看你。", "I’ll go see you after class. (以后 after a clause; correct. 我下课后来去看你 is incorrect.)"), ("那天我们先去了银行，然后才回学校。", "That day we first went to the bank and then went back to school. (然后, past)"), ("那天我们先去了银行，后来才回学校。", "That day we first went to the bank and later went back to school. (后来, past)"), ("明天我们先去银行，然后再回学校。", "Tomorrow we’ll first go to the bank and then go back to school. (然后, future)")]
HL7 = [("我小学的时候喜欢踢足球，上了中学后来我开始喜欢篮球了。", "1. When I was in elementary school I liked soccer; after I started middle school I began to like basketball. (后来; key mine)"), ("小明以前常常打游戏，后来学习很紧张，他爸爸不让他玩了。", "2. Xiao Ming used to play video games often, later his studies got tense and his father didn’t let him play. (后来)"), ("到了美国以后，张华再也没有给我打过电话。", "3. After arriving in the U.S., Zhang Hua never called me again. (以后)"), ("我们先去农贸市场买东西，然后再找个饭馆吃饭。", "4. We first go to the farmers’ market to shop and then find a restaurant to eat. (然后)"),
       ("进了电影院以后，我找好座位坐下了。", "5. After entering the cinema I found a seat and sat down. (以后)"), ("后来电影没意思，我就睡着了。", "6. Later the movie was boring and I fell asleep. (后来)"), ("昨晚的球赛太精彩了。球赛完了以后，大家还是非常兴奋，不愿意离开体育场。", "7. Last night’s game was so exciting. After the game ended, everyone was still very excited and didn’t want to leave the stadium. (以后)")]
YM = ("姚明从小就喜欢篮球。上小学时，每天下课以后，他先去打篮球，然后再回家。后来，他去上海的体育运动技术学院训练篮球。那个时候，他的身高是一米九一，比别人高很多。到了那儿以后，教练让他多睡觉，这样他会长得更高。后来，他的身高长到二米二六。一九九八年他开始在中国国家篮球队打球，得了很多冠军。后来他成为了美国职业篮球联赛的球员。")
YM_E = ("Yao Ming has liked basketball since childhood. In elementary school, after class every day he first went to play basketball and then went home. Later he went to the Shanghai Sports Technical Institute to train in basketball. At that time his height was 1.91 meters, much taller than others. After arriving there, the coach had him sleep more so that he would grow even taller. Later his height grew to 2.26 meters. In 1998 he began playing for the Chinese national basketball team and won many championships. Later he became a player in the American professional basketball league (the NBA). (The book writes the height and year as digits and the league as NBA.)")
L5 = lesson(
    "Lesson 17 Presentation 3 grammar: the time words 后来 vs. 以后",
    "后来 for the past · 以后 for past and future · 然后 · 姚明",
    requires=[],
    cards=[
        card("The Time Words 后来 vs. 以后",
             "Both 后来 and 以后 can be translated as “afterwards,” but they are not always interchangeable. 以后 can be used to refer to both past and future events, whereas 后来 is restricted to only the past. 以后 can be used after a clause to express the meaning “after…,” while 后来 cannot. 然后, which you learned earlier, is another expression that can be translated as “afterward.” It has the same function as 后来, but 然后 can be used to refer to both past and future time frames. The incorrect sentences the book marks are 这个问题后来再说 and 我下课后来去看你.",
             examples=[D(z, e) for z, e in HL]),
        card("Activity 7 (Reading and Speaking): 考考你",
             "A. Complete the sentences using 后来, 以后 or 然后. B. Pair up and compare your answers, explaining the differences between 后来, 以后 and 然后. The book leaves the key out; my completed sentences (mine):",
             examples=[D(z, e) for z, e in HL7]),
        card("Activity 8 (Reading, Writing and Speaking): Yao Ming",
             "A. Read the passage below about the Chinese basketball player Yao Ming and write a summary, paying attention to 后来, 以后 and 然后. B. Pair up and compare your summaries. C. Tell your partner about your interests and hobbies using 后来, 以后 and 然后 (your story).",
             examples=[D(YM, YM_E)]),
    ],
    exercises=[
        M("Which word refers only to the past?", "后来", ["以后", "然后", "Both 以后 and 然后"], "后来: only the past."),
        M("Which can refer to past and future?", "以后 and 然后", ["Only 后来", "Only 以后", "None"], "以后 and 然后."),
        M("Which is correct?", "这个问题以后再说", ["这个问题后来再说", "这个问题然后再说后来", "后来这个再问题说"], "以后 (future)."),
        M("Which is correct?", "我下课以后去看你", ["我下课后来去看你", "我下课然后后来看你", "我后来下课去看你"], "以后 after a clause."),
        M("Which fits “first the bank, then back to school (future)”?", "明天我们先去银行，然后再回学校", ["明天我们先去银行，后来再回学校", "明天我们先去银行，后来才回学校", "明天先银行去后来回学校"], "然后 for future."),
        M("What happened to Yao Ming after he arrived at the institute?", "The coach had him sleep more so he would grow taller", ["He quit basketball", "He studied medicine", "He moved to America"], "教练让他多睡觉."),
        M("How tall did Yao Ming grow?", "2.26 meters", ["1.91 meters", "2.00 meters", "1.80 meters"], "二米二六."),
        F("到了美国___，张华再也没有给我打过电话。", "以后", PART, "以后 after a clause."),
        F("小明以前常常打游戏，___学习很紧张，他爸爸不让他玩了。", "后来", PART, "后来: past."),
        F("我们先去农贸市场买东西，___再找个饭馆吃饭。", "然后", PART, "然后."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
XI = ("最近中国国家主席习近平接受了俄罗斯记者的采访。当记者问他有些什么爱好时，他说：“我爱阅读、看电影、旅游、散步。说到体育活动，我喜欢游泳、爬山等运动，我还喜欢足球、排球、篮球、网球、武术等运动。另外，我也喜欢看冰雪类比赛，像冰球和花样滑冰比赛什么的。”"
      "习近平在年轻的时候就特别喜欢足球，他不但喜欢踢球，而且也爱看球赛。他的父亲习仲勋在北京工作的时候，习近平就常常去北京工人体育馆的足球场踢球。每次有大的足球赛时，他早早地就跑去体育馆的售票窗口排队买票看比赛。"
      "在二零零八年七月，北京办奥林匹克运动会以前，习近平到北京附近检查足球场地的时候，穿着皮鞋就在草地上踢起了足球，看到他踢球的人都认为他踢得很棒，还说他一定常常练习踢球。"
      "除了踢足球踢得很好以外，习近平游泳也游得非常好。在《华盛顿邮报》的书面采访中，他说：“我爱运动，游泳是我的最爱。锻炼身体不但让我的身体更健康，也让我的工作更有效率！”")
XI_E = ("Recently China’s President Xi Jinping gave an interview to a Russian reporter. When the reporter asked him what hobbies he has, he said: “I love reading, watching movies, traveling and taking walks. As for sports, I like swimming, mountain climbing and the like, and I also like soccer, volleyball, basketball, tennis, martial arts and so on. In addition, I also like watching ice-and-snow competitions, such as ice hockey and figure skating.” "
        "When he was young Xi Jinping especially liked soccer; he not only liked to play but also loved watching matches. When his father Xi Zhongxun worked in Beijing, Xi Jinping often went to play soccer on the soccer field of the Beijing Workers’ Gymnasium. Every time there was a big soccer match, he would run to the stadium’s ticket window early to line up to buy tickets to watch the game. "
        "In July 2008, before Beijing hosted the Olympic Games, when Xi Jinping went to the area near Beijing to inspect soccer fields, he started playing soccer on the grass in leather shoes, and the people who saw him play thought he played very well and said he must practice playing often. "
        "Besides playing soccer very well, Xi Jinping also swims very well. In a written interview with the Washington Post he said: “I love sports, and swimming is my favorite. Exercising not only makes my body healthier but also makes my work more efficient!” (The book glosses 俄罗斯, 武术, 奥林匹克 and 效率 in pinyin and writes the year as digits.)")
L6 = lesson(
    "Lesson 17 Presentation 3: skill integration",
    "张军一家的爱好 · 习近平的爱好 · 李军这样的球迷",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing, Reading and Speaking)",
             "A. Listen to the monolog and write the EEIs (essential elements of information) about Zhang Jun’s family in pinyin: for each of 爸爸, 妈妈, 哥哥 and 我, fill in 爱好 (…迷) and 其他信息. B. Pair up and exchange your EEIs, then read the script and summarize it. C. Talk about your family members’ interest in sports with your partner and note the information (你同学的家人: 爸爸, 妈妈, 兄弟姐妹, 你同学本人; 体育爱好 and 其他信息). D. Report the hobbies of your partner’s family members to the class. (Audio and script, not included.)"),
        card("Activity 2 (Reading, Writing and Speaking): the interview article",
             "Read the article about Chinese President Xi Jinping. A. Pair up. The teacher cuts the article into four to six segments and mixes them up. Each pair picks two or three segments and arranges them in logical order, then (1) writes any words you don’t know and discusses their meanings, and (2) summarizes the segments and prepares to retell them to a new partner. B. Pair up with a new partner: read your summary and explain the new words; re-order all the segments and summarize the entire article in a few sentences. C. Talk about any American president that you know of who likes sports. (Photograph, public domain, not included.)",
             examples=[D(XI, XI_E)]),
        card("Activity 3 (Listening, Writing, Reading and Speaking)",
             "A. Listen to the passage about Li Jun and note the EEIs in pinyin. New words: 采访 (cǎifǎng; interview), 大喊大叫 (dà hǎn dà jiào; yell), 生气 (shēngqì; upset), 受不了 (shòu bùliǎo; can’t stand). B. Pair up and, using what you heard, mark the statements as True or False and explain why any is false: 1. 李军工作很忙，很少去现场看球赛。 2. 李军的太太常常和他一起看球赛。 3. 李军通常周末看球赛，平时看其他的电视节目。 4. 李军的太太经常自己逛商店。 5. 李军和朋友看球的时候，非常安静。 6. 李军的太太在自己的房间里看球。 C. In two groups discuss: 1. 你喜欢李军这样的球迷吗？为什么？ 2. 你是球迷吗？你是一个什么样的球迷？ 3. 在美国，什么球迷最多？为什么会有这么多的球迷？ 4. 请说说你最喜欢的一场球赛。 (Audio, not included, so no answers for the statements.)"),
    ],
    exercises=[
        M("What did the Russian reporter ask Xi Jinping?", "What hobbies he has", ["Where he was born", "Who his father is", "What he does for work"], "有些什么爱好."),
        M("Which sports does he say he likes?", "Swimming, mountain climbing, soccer, volleyball, basketball, tennis and martial arts", ["Only golf", "Only skiing", "Only chess"], "游泳、爬山…"),
        M("Which ice-and-snow events does he like to watch?", "Ice hockey and figure skating", ["Skiing", "Curling", "Speed skating"], "冰球和花样滑冰."),
        M("What did he especially like when he was young?", "Soccer", ["Tennis", "Golf", "Chess"], "特别喜欢足球."),
        M("Where did he often play soccer?", "On the field at the Beijing Workers’ Gymnasium", ["At school", "At home", "On a beach"], "北京工人体育馆的足球场."),
        M("What did he do before big matches?", "Ran early to the ticket window and lined up", ["Stayed home", "Bought tickets online", "Slept"], "早早地就跑去体育馆的售票窗口排队买票."),
        M("What did people think when they saw him play in 2008?", "That he played very well and must practice often", ["That he was a beginner", "That he was joking", "That he was hurt"], "认为他踢得很棒."),
        M("What is his favorite sport according to the written interview?", "Swimming", ["Soccer", "Tennis", "Hiking"], "游泳是我的最爱."),
        M("What does he say exercise does for his work?", "Makes it more efficient", ["Makes it easier", "Makes it shorter", "Nothing"], "更有效率."),
        F("习近平不但喜欢踢球，___且也爱看球赛。", "而", PART, "不但…而且…"),
        F("他早早___就跑去体育馆的售票窗口排队。", "地", PART, "早早地."),
    ],
)

# ------------------------------------------------------------------ 7. context
NOTICE = [("中国杯国际足球锦标赛", "China Cup International Soccer Championship"), ("比赛时间：九月二十一日到二十五日", "Match dates: September 21 to 25"), ("比赛地点：北京工人体育场", "Venue: Beijing Workers’ Stadium"), ("参赛球队：中国，泰国，韩国，日本", "Participating teams: China, Thailand, Korea, Japan"), ("主办机构：中国足球协会", "Organizer: the Chinese Football Association"), ("购票电话：六七一零三二六六", "Ticket phone: 6710-3266 (read digit by digit)")]
CALL = [("一张票多少钱？", "How much is one ticket?"), ("星期三的票有吗？", "Are there tickets for Wednesday?"), ("星期三是哪国和哪国比赛？", "Which countries play on Wednesday?"), ("中国和韩国哪天比赛？", "On what day do China and Korea play?"), ("什么时间比赛？", "At what time is the match?"), ("你们体育场有停车场吗？", "Does your stadium have a parking lot?"), ("停车场一小时多少钱？", "How much is the parking lot per hour?"),
        ("你要买哪天的票？", "(Ticket seller) Which day’s tickets do you want to buy?"), ("你想买几张？", "(Ticket seller) How many do you want?"), ("怎么付钱？", "(Ticket seller) How will you pay?")]
STAR = ["你要介绍的球星是谁？", "他是哪个球队的？", "他的老家在哪儿？", "他是几号球员？", "他从什么时候起在这个球队打球？", "他的球队赢了多少次？", "他们最近的一次比赛是什么时候？", "除了打球，他有什么兴趣和爱好？"]
STAR_E = ["Who is the star you will introduce?", "Which team is he on?", "Where is his hometown?", "What is his number?", "Since when has he played for this team?", "How many times has his team won?", "When was their most recent game?", "Besides playing ball, what interests and hobbies does he have?"]
PROCON = table(["", "优点 (advantages)", "缺点 (disadvantages)", "最后的决定 (final decision)"],
               [["篮球", "场地小，人少也能玩，冬天可以在室内打，对长个子有好处", "容易受伤，比赛的时候很累", ""], ["足球", "可以和很多朋友一起踢，对身体好，不用太多装备", "场地大，练习需要的时间长，下雨天不能踢", ""]],
               title="Activity 3: a sample pros-and-cons table (mine; the book leaves it blank)", say=[0, 1, 2])
L7 = lesson(
    "Lesson 17 Presentation 3: using Chinese in context",
    "中国杯国际足球锦标赛 · 介绍美国球星 · 篮球还是足球",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): the ticket office",
             "Role-Play: You are studying Chinese at Beijing University in China. You like soccer very much and hope to watch a soccer match at the stadium. You saw a notice in the newspaper about the China Cup International Soccer Championship and you’d like to see it. Call the ticket office to ask about the game schedule, the availability and price of tickets, which match you want to see, etc. A. Pair up and read the notice below; think of questions with your partner. B. Call the ticket office; your partner plays the ticket seller. You may use the following questions as reference (你要问的问题 / 接电话人的问题 and 其他问题). C. Note your information. The book prints the dates and the phone number in digits; here they are spelled out.",
             examples=[D(z, e) for z, e in NOTICE] + [D(z, e) for z, e in CALL]),
        card("Activity 2 (Reading, Speaking and Writing): popular American athletes",
             "Scenario: You are studying Chinese at a university in China. Your teacher assigns you a project to introduce popular American athletes. You will choose one star player each from basketball (篮球 lánqiú), baseball (棒球 bàngqiú) and football (橄榄球 gǎnlǎnqiú). Divide into three groups; each group reports on one player. A. In your group, discuss which player you’d like to introduce, following the questions as a guide (conduct online research if necessary): the table has Group 1 (篮球球星), Group 2 (棒球球星) and Group 3 (橄榄球球星) under 报告内容, and the questions below plus 其他信息. B. Consolidate your group discussion and prepare a PowerPoint presentation. C. Each group takes turns to present their player to the class. (Pictures, not included.)",
             examples=[D(f"{i}. {q}", f"{e}") for i, (q, e) in enumerate(zip(STAR, STAR_E), 1)]),
        card("Activity 3 (Listening, Writing and Speaking): which team to join",
             "Scenario: You are studying Chinese in a university in China. You just heard a radio announcement on campus that the school is recruiting players for basketball and soccer, sports you really enjoy playing. However, you can only join one team because your Chinese studies are very intensive and you don’t have time to play two sports. Seek advice from your classmates to help you decide which sport to play. A. Listen to the radio announcement and write a summary. (Audio, not included.) B. Divide into two groups. Discuss the advantages and disadvantages of basketball and soccer and explain which sport is better for you. C. Each group presents its discussion to the class and explains why they made the right choice; you will make a final decision about which sport to play. The book leaves the table blank; a sample:",
             tables=[PROCON]),
    ],
    exercises=[
        M("What is the competition in the notice called?", "中国杯国际足球锦标赛", ["世界杯足球赛", "欧洲杯足球赛", "亚洲杯足球赛"], "中国杯国际足球锦标赛."),
        M("Where is it held?", "Beijing Workers’ Stadium", ["Shanghai Stadium", "Bird’s Nest", "A school gym"], "北京工人体育场."),
        M("Which teams take part?", "China, Thailand, Korea and Japan", ["China and America", "Germany and England", "Brazil and Spain"], "中国，泰国，韩国，日本."),
        M("Who organizes it?", "The Chinese Football Association", ["The school", "The city", "A TV station"], "中国足球协会."),
        M("What do you ask the ticket office?", "Price, dates, which teams play, time, parking", ["Only your name", "Only the weather", "Nothing"], "你要问的问题."),
        M("What does the ticket seller ask you?", "Which day, how many tickets, how to pay", ["Your age", "Your job", "Your address"], "接电话人的问题."),
        M("What project does Activity 2 assign?", "Introduce popular American athletes", ["Plan a trip", "Write a poem", "Cook a meal"], "Introduce popular American athletes."),
        M("Why can you join only one team in Activity 3?", "Chinese studies are too intensive", ["Both are too expensive", "No coach", "The school forbids it"], "Chinese studies are very intensive."),
        F("你们体育场有停车___吗？", "场", PART, "停车场."),
        F("他是几号___员？", "球", PART, "球员."),
    ],
)
L8 = vocab_lesson("Lesson 17 Presentation 3 vocabulary", "24 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 9. Area Studies
L9 = lesson(
    "Lesson 17 Area Studies: Sports in China",
    "足球 · 篮球 · 乒乓球 · 排球 · traditional sports · minority sports · the sports industry",
    requires=[],
    cards=[
        card("Sports in China: soccer, basketball and ping pong",
             "Chinese people today enjoy a variety of competitive sports. Among them, football (soccer) is one of the most popular. Football games earn the highest television ratings of any sport in the country. The Chinese Football Association (CFA) established China’s first professional football league in 2004, the Chinese Super League (CSL), the premier football league in China. However, at the international level, Chinese football has enjoyed little success despite the amount of support it receives from fans. Basketball is now the number one sport in China. There are about 300 million basketball fans, ranking first in all sports. The total number of basketball courts in China is close to 800,000. The Chinese Men’s Basketball Professional League has a huge number of followers. It starts in October or November each year and ends around April of the following year. The league’s scale, management, operation and attention are all rated as the best professional league in China. Ping pong (乒乓球) is a popular and revered game in China. Apart from the national teams, the table tennis community in the country continues to produce many world-class players, and this depth of skill allows the country to continue dominating world titles after a short break during the 1990s. The overwhelming dominance of China in the sport has triggered a series of rule changes in the International Table Tennis Federation."),
        card("Volleyball, traditional sports and the sports industry",
             "Volleyball is another very popular game in China, especially on school campuses. The China Women’s National Volleyball Team is one of the leading squads in women’s international volleyball. The team became the world’s first team with “five consecutive championships” in the 1980s. It went on to win another five world championships from 2003 to 2019. China has inherited a variety of traditional sports, which have very distinct Chinese characteristics. The most popular ones are martial arts, taijiquan (shadow boxing), qigong (deep breathing exercises), Xiangqi (Chinese chess), Weiqi (known as “Go” in the West) and mahjong. Taijiquan is a kind of Chinese boxing that combines control of breath, mind and body. It emphasizes body movement following mind movement, tempering toughness with gentleness and graceful carriage. Qigong is a unique Chinese way of keeping fit. It aims at enhancing health, prolonging life, curing illness and improving physiological functions by concentrating the mind and regulating breathing. Xiangqi and Weiqi were two of the five sports featured at the 2008 World Mind Sports Games held in Beijing. There are also various entertaining and competitive sports activities in the minority inhabited areas. For example, wrestling and horsemanship are popular among Mongols, Uyghurs and Kazaks. Tibetan people like yak racing very much, and people in Korean communities enjoy “seesaw jumping.” Crossbow archery is very trendy among the Miao, and dragon-boat racing attracts a large number of followers among the Dai ethnic minority. Sports has become a huge industry in China. The total output of China’s national sports industry is about 3 trillion yuan, and the added value of the sports industry is over one trillion yuan, more than 1% of China’s GDP. (Photographs, not included.)"),
    ],
    exercises=[
        M("Which sport earns the highest television ratings in China?", "Football (soccer)", ["Basketball", "Ping pong", "Volleyball"], "Football games earn the highest television ratings."),
        M("When was the Chinese Super League established?", "2004", ["1994", "2008", "1980"], "Established in 2004."),
        M("Which sport is now number one in China?", "Basketball", ["Soccer", "Ping pong", "Volleyball"], "Basketball is now the number one sport."),
        M("About how many basketball fans does China have?", "300 million", ["30 million", "800,000", "3 trillion"], "About 300 million."),
        M("When does the men’s basketball league run?", "October or November to about April", ["June to August", "January to March", "All year"], "Starts in Oct/Nov and ends around April."),
        M("What has China’s dominance in ping pong triggered?", "A series of rule changes at the International Table Tennis Federation", ["Its removal from the Games", "A ban on Chinese players", "A new league"], "Rule changes."),
        M("Which team won five consecutive world championships in the 1980s?", "The China Women’s National Volleyball Team", ["The men’s football team", "The table tennis team", "The basketball team"], "Five consecutive championships in the 1980s."),
        M("What is taijiquan?", "A kind of Chinese boxing combining control of breath, mind and body", ["A kind of chess", "A ball game", "A running race"], "Combines control of breath, mind and body."),
        M("Which two sports were featured at the 2008 World Mind Sports Games in Beijing (among five)?", "Xiangqi and Weiqi", ["Taijiquan and qigong", "Mahjong and ping pong", "Wrestling and archery"], "Xiangqi and Weiqi."),
        M("Which minority enjoys dragon-boat racing?", "The Dai", ["The Miao", "The Tibetans", "The Mongols"], "Dragon-boat racing among the Dai."),
        M("What share of GDP is the sports industry’s added value?", "More than 1%", ["About 50%", "About 0.01%", "Exactly 10%"], "More than 1% of China’s GDP."),
    ],
)

UNIT = unit("第十七课 体育健身 Presentation 3: ball-game fans, 为了/为, 更, 不管…都…, 后来/以后/然后, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
