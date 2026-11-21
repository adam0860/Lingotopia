"""Unit 47: Lesson 16 (Recreational Activities) Presentation 3 and Area Studies from the book's texts: the movie-and-TV passage,
the preposition 给, 不是…就是, 虽然…但是/可是, the modal verb 会 (will), the adverb 甚至, the skill-integration and using-Chinese
activities, the vocabulary list and the Chinese Entertainment and Leisure reading. Audio, pictures, videos and websites are not
included; the book writes numbers as digits and they are spelled out here; answer keys the book does not print (and blanks it leaves
for the student) are mine and labeled."""
from zh_auto import *
from zh_l16_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("睡不着觉", 2, "zhao2"), ("着觉", 1, "jiao4"), ("睡觉", 1, "jiao4"), ("得在家", 0, "dei3"), ("还得去", 1, "dei3"), ("得好好", 0, "dei3"), ("没上过", 0, "mei2"), ("没请", 0, "mei2"), ("没给", 0, "mei2"), ("都会", 0, "dou1"), ("还没", 0, "hai2"),
                          ("人参加", 1, "can1"), ("乐队", 0, "yue4"), ("乐器", 0, "yue4"), ("看家人", 0, "kan4"), ("教朋友", 0, "jiao1")):
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

# ------------------------------------------------------------------ 1. the passage
TV = ("我和我太太都不太喜欢运动，空闲的时候，不是在家看电视，就是去电影院看电影。我太太最喜欢看肥皂剧，每天晚上吃完晚饭，她就会打开电视，一集接一集地看。她经常一边看，一边和演员一起哭，一起笑。有时候，甚至看到半夜还不睡觉。"
      "我喜欢去电影院看电影。每次出新片，我都会让太太陪我去看。我们喜欢看轻松的搞笑片和紧张的动作片，也喜欢看动画片。虽然很多人说动画片是给小孩儿看的，但是我觉得对大人来说，也很有意思，是难得放松的机会。不过我太太不喜欢看恐怖片，因为看完恐怖片她常常害怕得睡不着觉。最近，我打算在我家的地下室装一个家庭影院。这样我太太看电视的时候，我也可以看我喜欢的电影了。")
TV_E = ("My wife and I both don’t much like sports; in our free time we either watch TV at home or go to the movie theater. My wife likes soap operas best; every evening after dinner she turns on the TV and watches episode after episode. She often cries and laughs along with the actors while watching. Sometimes she even watches until midnight and still doesn’t go to sleep. I like going to the movie theater. Whenever a new film comes out I get my wife to go with me. We like light comedies and tense action movies, and also animated films. Although many people say animated films are for kids, I feel that for adults they are also interesting and a rare chance to relax. But my wife doesn’t like horror films, because after watching one she is often so scared she can’t sleep. Recently I’ve been planning to install a home theater in our basement. This way, when my wife watches TV, I can also watch the movies I like.")
NT = [("对 A 来说", "to A, for A, or regarding A"), ("一 + 集 (m.) + 接 + 一集 (m.)", "indicates “one after another”"), ("甚至…也/都", "often used to intensify the example provided")]
KEY4 = ("我的姐姐平常上班很忙，难得有机会去看电影。对她来说，最好的放松就是上网看韩国的肥皂剧。她常一吃完饭就一集接着一集地看，周末的时候还会一连看好几个钟头，有时甚至看到半夜都不睡觉。虽然她已经是一个大人，但是有时你会看到她跟着演员们一起哭，一起笑，像一个孩子一样。她的爸爸常笑她说她是上瘾了，因为周末的时候她不是在睡觉就是在看韩剧，而且只要韩国有什么新片，她都会看，他们有什么演员她也都认识。我姐姐真是个百分之百的韩剧迷。")
KEY4_E = ("My older sister is usually busy at work and rarely has the chance to go to the movies. For her, the best way to relax is to watch Korean soap operas online. She often watches one episode after another right after dinner, and on weekends she watches for several hours in a row; sometimes she even watches until midnight without sleeping. Although she is already an adult, sometimes you’ll see her crying and laughing along with the actors like a child. Her father often teases her that she is addicted, because on weekends she is either sleeping or watching Korean dramas, and whenever Korea has a new release she will watch it, and she knows all their actors. My sister is truly a hundred-percent Korean-drama fan. (completed text; the blanks are filled by me)")
L1 = lesson(
    "Lesson 16 Presentation 3: movies and TV at home",
    "不是在家看电视，就是去电影院看电影 · 肥皂剧 · 一集接一集地看 · 家庭影院",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: a couple watching TV, a movie theater (not included). Pair up and discuss: A. What is your favorite movie genre? Why do you like it? Can you name several movie genres in Chinese? B. How many hours per day do you watch TV? What kinds of programs do you enjoy?"),
        card("Presentation 3: 看电视，看电影",
             "The book also prints the passage in traditional characters. Notes: 1. 对 A 来说: to A, for A, or regarding A. 2. 一 + 集 (m.) + 接 + 一集 (m.) indicates “one after another.” 3. 甚至…也/都 is often used to intensify the example provided.",
             examples=[D(TV, TV_E)]),
        card("Activities 1 to 3",
             "Activity 1 (Reading, Speaking and Listening). A. Examine the Word Cloud and images from movies. First match a movie genre with its image by drawing lines, then add the possible emotional words from the Word Cloud that may go with the genres. B. Pair up. Select the remaining words in the word cloud that are not selected in Part A; take turns creating a sentence, which your partner listens to and translates. For example, 空闲: Student A: 我空闲的时候喜欢上网看电视剧。 Student B: When I have free time, I like to go online to watch a TV series. (The word cloud and pictures, not included.) Activity 2 (Listening, Reading, and Speaking). A. Global listening: listen to Presentation 3 once and summarize it. B. Detailed listening: listen again and take notes on the couple’s leisure activities (先生, 太太). C. Read the presentation out loud with a partner and note the similarities and differences between the husband and wife (一样的地方, 不一样的地方). (Mine: both don’t like sports and like movies and TV; the husband likes the theater, comedies, action films and animation, the wife likes soap operas and doesn’t like horror films.) Activity 3 (Listening and Speaking). A. Listen to a conversation between two friends and answer in Chinese: 1. What does Zhang Hua invite Wen Ying to do? 2. What is Zhang Hua’s preference? Why? 3. What is Wen Ying’s preference? Why? 4. Are they in agreement? How do you know? 5. What is their final decision? B. Pair up and share; Student A asks the questions and Student B answers in Chinese; then switch. C. Interview your partner about a recent film: When was the last time you went to see a movie? Where did you watch it? Whom did you go with? How much was the ticket? What was the name of the movie? What genre was it? Why did you go see it? Did you like the movie? Why or why not? D. Report your findings to another classmate. (Audio, not included.)",
             examples=[D("我空闲的时候喜欢上网看电视剧。", "When I have free time, I like to go online to watch TV series.")]),
        card("Activity 4 (Reading and Speaking)",
             "A. Complete the sentences in the passage using the words in the box: 接, 难得, 甚至, 虽然, 不是…就是, 演员, 对她来说, 肥皂剧. B. Read the passage aloud and check your answers with a classmate; discuss what strategies helped you. The book leaves the blanks; my completed passage (mine):",
             examples=[D(KEY4, KEY4_E)] + [D(a, b) for a, b in [("对 A 来说", "Note 1: to A, for A")] if False]),
    ],
    exercises=[
        M("What do the narrator and his wife do in their free time?", "Watch TV at home or go to the movies", ["Play sports", "Travel", "Read books"], "不是在家看电视，就是去电影院看电影。"),
        M("What does the wife like best?", "Soap operas", ["Action films", "News", "Sports"], "我太太最喜欢看肥皂剧。"),
        M("How does the wife watch soap operas?", "One episode after another", ["Only on weekends", "In the theater", "With the sound off"], "一集接一集地看。"),
        M("What does the husband like at the theater?", "Comedies, action movies and animation", ["Horror films", "Soap operas", "Documentaries"], "轻松的搞笑片和紧张的动作片，也喜欢看动画片。"),
        M("Why doesn’t the wife like horror films?", "She gets so scared she can’t sleep", ["They are too long", "They are expensive", "They are boring"], "害怕得睡不着觉。"),
        M("What does the husband plan to do?", "Install a home theater in the basement", ["Buy a TV", "Sell the house", "Move"], "在我家的地下室装一个家庭影院。"),
        M("What does 对 A 来说 mean?", "To A; for A", ["Against A", "After A", "Instead of A"], "对 A 来说."),
        M("What does 一集接一集 mean?", "One episode after another", ["Only one episode", "Every other episode", "No episode"], "一 + 集 + 接 + 一集."),
        M("What does 甚至 do in 甚至看到半夜还不睡觉?", "Intensifies the example", ["Negates it", "Asks a question", "Marks a past action"], "甚至 intensifies."),
        M("What does 难得 mean?", "Rare; seldom", ["Difficult to get along", "Very easy", "Very cheap"], "难得: rare."),
        mean("演员", "yan3 yuan2", "actor; actress", ["director", "audience", "teacher"]),
        F("我太太不喜欢看恐怖片，因为看完恐怖片她常常害怕___睡不着觉。", "得", PART, "害怕得…: complement of degree."),
        F("每次出新片，我都会让太太陪我去___。", "看", PART, "陪我去看."),
    ],
)

# ------------------------------------------------------------------ 2. 给
GE = [("每天我妈妈给我做早饭。", "Every day my mom makes breakfast for me."), ("我的朋友给我买一杯咖啡。", "My friend buys a cup of coffee for me."), ("请给我拿一双筷子。", "Please get me a pair of chopsticks."), ("这个周末我想给我太太开一个生日派对。", "This weekend I want to throw a birthday party for my wife."), ("我今天没给小王买领带。", "I didn’t buy a tie for Xiao Wang today.")]
GE1 = [("去年母亲节，你给你母亲买了什么礼物？", "A: Last Mother’s Day, what gift did you buy for your mother?"), ("去年母亲节，我给我母亲买了一束花。", "B: Last Mother’s Day I bought my mother a bouquet of flowers. (mine)"), ("今年呢？今年你给她买什么礼物？", "A: And this year? What gift will you buy her this year?"), ("今年我想给她买一条围巾。", "B: This year I want to buy her a scarf. (mine)"),
       ("小李，你常常给你父母打电话吗？", "A: Xiao Li, do you often call your parents?"), ("我常常给他们打电话，差不多每个星期两三次。", "B: I often call them, about two or three times a week. (mine)"), ("他们也常常给你打电话吗？", "A: Do they often call you too?"), ("他们也常常给我打电话。", "B: They often call me too. (mine)")]
L2 = lesson(
    "Lesson 16 Presentation 3 grammar: the preposition 给",
    "给我做早饭 · 给我太太开一个生日派对 · 没给小王买领带",
    requires=[],
    cards=[
        card("The preposition 给",
             "The preposition 给 means “for” or “for the benefit of.” The preposition 给 and the noun that follows it form a prepositional phrase that modifies the main verb of the sentence. A prepositional phrase precedes the main verb in the sentence. An auxiliary verb such as 会, 想, or 能 usually precedes the preposition. The negative form 不 and 没有 precedes the auxiliary verb and the preposition. Statement: Subj. + 给 + Recipient + (Verb Phrase); Subj. + (Modal Verb) + 给 + Recipient + (Verb Phrase). Negation: Subj. + 不/没 + (Modal Verb) + 给 + Recipient + (Verb Phrase).",
             examples=[D(z, e) for z, e in GE]),
        card("Activities 1 and 2",
             "Activity 1 (Reading, Speaking, Listening and Writing). A. Pair up. Read and complete the following dialogs using 给 (Dialog 1: 去年母亲节，你给你母亲买了什么礼物？ / 今年呢？今年你给她买什么礼物？ Dialog 2: 小李，你常常给你父母打电话吗？ / 他们也常常给你打电话吗？). B. Interview your partner and list five things your partner did or wanted to do for others; post your list on Linoit. The book leaves the answers blank; my completed dialogs (mine): Activity 2 (Listening & Speaking). A. Listen to the conversation twice and mark each statement True or False: 1. Mr. Lin’s wife never buys ties for him. 2. The tie that Mr. Lin is wearing was given to him by his sister. 3. Lao Li asked Mr. Lin’s sister to buy the same tie for him. 4. Lao Li will be given the tie. B. Pair up, go over each statement and explain your answers; make corrections. (Audio, not included.)",
             examples=[D(z, e) for z, e in GE1]),
    ],
    exercises=[
        M("What does 给 mean as a preposition?", "For (the benefit of)", ["To buy", "Because of", "In spite of"], "给: for."),
        M("Where does the 给 phrase go?", "Before the main verb", ["After the main verb", "At the end", "After the object"], "A prepositional phrase precedes the main verb."),
        M("Where does a modal verb go with 给?", "Before 给", ["After 给", "After the verb", "Instead of 给"], "Modal verb precedes the preposition."),
        M("What does 每天我妈妈给我做早饭 mean?", "My mom makes me breakfast every day", ["I make breakfast for mom", "My mom eats breakfast", "I eat breakfast every day"], "给我做早饭."),
        M("What does 请给我拿一双筷子 mean?", "Please get me a pair of chopsticks", ["Please give me a fork", "Please eat chopsticks", "I will get chopsticks"], "给我拿."),
        M("What does 这个周末我想给我太太开一个生日派对 mean?", "This weekend I want to throw my wife a birthday party", ["My wife wants a party", "I have no wife", "I will attend a party"], "给我太太开."),
        M("How is 我今天没给小王买领带 negated?", "没 before 给", ["给 before 没", "不 after 给", "没 after 买"], "没 precedes the preposition."),
        F("每天我妈妈___我做早饭。", "给", PART, "给我做早饭."),
        F("我今天没给小王买___带。", "领", PART, "领带: tie."),
    ],
)

# ------------------------------------------------------------------ 3. 不是…就是
BS = [("每天吃完晚饭，他妈妈不是看电视剧，就是看书。", "After dinner every day his mother either watches TV series or reads."), ("他约会不是去咖啡厅，就是去电影院。", "On dates he either goes to a coffee shop or to the movies."), ("周末他不是在宿舍打游戏，就是睡觉。", "On weekends he is either playing games in the dorm or sleeping."), ("每年的假期我不是回老家看家人，就是出国旅游。", "Every vacation I either go back to my hometown to see family or travel abroad."),
      ("这个周末不是我们去你们家，就是你们来我们家。", "This weekend it’s either we go to your home or you come to ours."), ("这个周末不是你们来我们家，就是我们去你们家。", "(= This weekend it’s either you come to our home or we go to yours.)")]
BS3 = [("你们每天第一节课都是什么课？", "Example, A: What class is your first class every day?"), ("不是听力课，就是阅读课。", "B: Either listening class or reading class. (the book’s example)"), ("你们长周末都做什么？", "1. A: What do you do on long weekends? (mine)"), ("不是去旅游，就是在宿舍睡觉。", "B: Either we travel or we sleep in the dorm. (mine)"),
       ("星期五晚上你们都做什么？", "2. A: What do you do on Friday evenings? (mine)"), ("不是出去吃饭，就是看电影。", "B: Either go out to eat or watch a movie. (mine)"), ("每天下课以后你们都做什么？", "3. A: What do you do after class every day? (mine)"), ("不是去操场锻炼，就是去图书馆学习。", "B: Either exercise at the field or study at the library. (mine)"),
       ("放寒假你们都做什么？", "4. A: What do you do during winter break? (mine)"), ("不是回老家，就是出国旅游。", "B: Either go back to our hometown or travel abroad. (mine)")]
L3 = lesson(
    "Lesson 16 Presentation 3 grammar: the 不是…就是 construction",
    "不是看电视剧，就是看书 · 不是回老家，就是出国旅游",
    requires=[],
    cards=[
        card("The 不是…就是… construction",
             "The 不是…就是… construction indicates “it must be one or the other.” In a compound/complex sentence, 不是 is always used in the first clause, while 就是 is used in the second. Clauses introduced by 不是 and 就是 can be interchanged without affecting the meaning. 不是 A，就是 B.",
             examples=[D(z, e) for z, e in BS]),
        card("Activities 3 and 4",
             "Activity 3 (Speaking and Listening). Below is one of DLI students’ routines (two pictures, not included). A. Pair up. Student A uses the time in the left column to generate a question and Student B answers using the images on the right with 不是…就是. The times: 1. 长周末 2. 星期五晚上 3. 每天下课以后 4. 放寒假. B. (故事接龙) Form groups of three. Each student writes a sentence about their routines/hobbies using 不是…就是…; Student A creates a sentence; Student B repeats A’s sentence and adds their own; Student C repeats A’s and B’s sentences before giving theirs, and so on. The book’s example and my answers (the pictures decide the real answers, so mine are guesses):  Activity 4 (Listening, Speaking and Writing). A. Listen to the conversation between two friends once and answer: 1. What is the main topic of the conversation? 2. What conclusions do the speakers draw about the topic? B. Listen again and write the sentences that use 不是…就是… and translate them into English. C. Pair up and in Chinese check your answers. (Audio, not included.)",
             examples=[D(z, e) for z, e in BS3]),
    ],
    exercises=[
        M("What does 不是 A，就是 B express?", "It must be one or the other", ["Neither A nor B", "Both A and B", "A and then B"], "不是…就是: it must be one or the other."),
        M("Which clause does 不是 introduce?", "The first", ["The second", "Either", "Neither"], "不是 is always in the first clause."),
        M("Can the two clauses be swapped?", "Yes, without changing the meaning", ["No", "Only in questions", "Only in negatives"], "Interchangeable."),
        M("What does 周末他不是在宿舍打游戏，就是睡觉 mean?", "On weekends he is either gaming in the dorm or sleeping", ["He never games", "He neither games nor sleeps", "He games and sleeps"], "不是…就是…"),
        M("What does 每年的假期我不是回老家看家人，就是出国旅游 mean?", "Every vacation I either visit my hometown family or travel abroad", ["I stay home", "I never travel", "I travel and visit"], "不是…就是…"),
        M("What does 这个周末不是我们去你们家，就是你们来我们家 mean?", "Either we go to your home or you come to ours", ["Neither", "Both", "Next weekend"], "不是…就是…"),
        F("他约会不是去咖啡厅，___是去电影院。", "就", PART, "不是…就是…"),
        F("每天吃完晚饭，他妈妈不是看电视剧，就是看___。", "书", PART, "不是…就是…"),
    ],
)

# ------------------------------------------------------------------ 4. 虽然…但是
SR = [("虽然我很想去舞厅跳舞，可是我们明天有考试，得在家准备。", "Although I really want to go dancing at a dance hall, we have an exam tomorrow and I have to prepare at home."), ("爷爷虽然八十岁了，但是身体还很好。", "Although Grandpa is eighty, his health is still very good."), ("虽然中文很难，但是我越学越有意思。", "Although Chinese is hard, the more I study the more interesting it gets."), ("虽然今天下雨，但是我还得去操场锻炼身体。", "Although it’s raining today, I still have to go to the field to exercise."),
      ("虽然他家很有钱，但是他从来不多花钱。", "Although his family is rich, he never spends extra money."), ("他虽然总是准备得很好，但是每次考试还是很紧张。", "Although he always prepares very well, he is still very nervous at every exam."), ("这双皮鞋虽然很贵，可是质量很好。", "Although this pair of shoes is expensive, the quality is very good. (same subject at the beginning)"), ("虽然王英学得很好，可是李明比她学得更好。", "Although Wang Ying studies very well, Li Ming studies even better. (different subjects)")]
SR5 = [("林红有两个孩子。林红还想再生一个。", "Example, the original: Lin Hong has two children. Lin Hong still wants another one."), ("虽然林红已经有两个孩子，可是她还想再生一个。", "Rewritten (the book’s example): Although Lin Hong already has two children, she still wants another."), ("虽然大卫唱歌的时候有点紧张，但是大家都觉得大卫唱得很好听。", "1. Although David was a bit nervous singing, everyone thought he sang well. (mine)"),
       ("虽然王明很喜欢陈丽，常常送花儿给她，但是他还没请陈丽出去吃过饭。", "2. Although Wang Ming likes Chen Li a lot and often sends her flowers, he hasn’t yet taken her out to dinner. (mine)"), ("虽然小华是班里最好的学生，但是小华的妈妈觉得小华可以学得更好。", "3. Although Xiaohua is the best student in the class, Xiaohua’s mother thinks she can do even better. (mine)"),
       ("虽然王太太每天下班以后都很累，但是她每天都要给全家准备可口的晚餐。", "4. Although Mrs. Wang is tired every day after work, she still has to prepare a tasty dinner for the whole family every day. (mine)"), ("这个同学虽然没上过吉他课，但是吉他弹得非常好。", "Part C example: Although this classmate has never taken a guitar class, he plays guitar extremely well."), ("你们猜猜他是谁？", "Can you guess who he is? (猜 cāi; guess)")]
L4 = lesson(
    "Lesson 16 Presentation 3 grammar: 虽然…，但是/可是…",
    "虽然中文很难，但是我越学越有意思 · 虽然…可是… · 同一个主语",
    requires=[],
    cards=[
        card("虽然…，但是/可是…",
             "This pattern means “although…, but…”. In English you wouldn’t normally use “but”, but it is required in Chinese. Both 但是 and 可是 precede the subject in a clause. 虽然…，但是/可是… If both clauses share the same subject, then the subject is generally placed at the beginning of the sentence. If the two clauses do not have a common subject, 虽然 and 但是/可是 are usually placed before the subjects in each clause.",
             examples=[D(z, e) for z, e in SR]),
        card("Activities 5 and 6",
             "Activity 5 (Reading, Speaking and Listening). A. Read the sentences next to each of four illustrations (pictures, not included), rewrite each sentence with 虽然…但是/可是… and then translate them. The first one has been done for you. B. Pair up; go over your rewritten sentences and take turns translating them. C. Each student creates one sentence about one classmate or teacher using 虽然…但是; the other students listen and guess who the person is. Activity 6 (Reading, Speaking and Listening). A. Listen to a conversation between two friends; in Chinese write the strengths and weaknesses of 林强, 李东, 张大年 and 陈华 in the table, then answer: What final decision was made? (Audio, not included.) The originals are: 1. 大卫唱歌的时候有点紧张。大家都觉得大卫唱得很好听。 2. 王明很喜欢陈丽，常常送花儿给她。王明还没请陈丽出去吃过饭。 3. 小华是班里最好的学生。小华的妈妈觉得小华可以学得更好。 4. 王太太每天下班以后都很累，她每天都要给全家准备可口的晚餐。 The book’s example and my rewrites (mine):",
             examples=[D(z, e) for z, e in SR5]),
    ],
    exercises=[
        M("What does 虽然…，但是… mean?", "Although…, but…", ["Because…, so…", "If…, then…", "Not only…, but also…"], "虽然…但是…"),
        M("Is 但是 required in Chinese?", "Yes, even though English drops “but”", ["No", "Only in writing", "Only in questions"], "Required in Chinese."),
        M("Where does 但是/可是 go?", "Before the subject of its clause", ["After the subject", "At the end", "Before 虽然"], "Precedes the subject."),
        M("What does 爷爷虽然八十岁了，但是身体还很好 mean?", "Although Grandpa is eighty, his health is still good", ["Grandpa is sick", "Grandpa is young", "Grandpa is eighty because he is well"], "虽然…但是…"),
        M("What does 虽然中文很难，但是我越学越有意思 mean?", "Although Chinese is hard, the more I study the more interesting", ["Chinese is easy", "I stopped studying", "Chinese is boring"], "虽然…但是…"),
        M("What does 他虽然总是准备得很好，但是每次考试还是很紧张 mean?", "He always prepares well but is still nervous at each exam", ["He never prepares", "He isn’t nervous", "He fails every exam"], "虽然…但是…"),
        M("Which subject placement is correct when both clauses share a subject?", "Subject at the beginning (这双皮鞋虽然很贵，可是质量很好)", ["Subject twice", "Subject at the end", "No subject"], "Common subject at the beginning."),
        F("虽然今天下雨，___是我还得去操场锻炼身体。", "但", PART, "但是."),
        F("这双皮鞋虽然很贵，___是质量很好。", "可", PART, "可是."),
    ],
)

# ------------------------------------------------------------------ 5. 会
HU = [("每天晚上吃完晚饭，她就会打开电视，一集接一集地看。", "Every evening after dinner she turns on the TV and watches episode after episode."), ("你想他明天会参加演出吗？", "Do you think he will take part in the performance tomorrow?"), ("天这么黑，等一会儿会下雨吗？", "It’s so dark; will it rain in a while?"), ("下班以后我会给你打电话。", "After work I will call you."), ("下个星期要考试，这个周末我不会去看电影。", "There is an exam next week, so I won’t go to the movies this weekend.")]
HU7 = [("每次你去看电影以前，", "Student A: Before every time you go to the movies, (the book’s example)"), ("每次我去看电影以前，我都会先上网买票。", "Student B: Before every time I go to the movies, I will buy tickets online first. (the book’s example)"), ("每天下课以后，我会去图书馆。", "After class every day, I will go to the library. (mine)"), ("明年夏天我会去中国。", "Next summer I will go to China. (mine)")]
L5 = lesson(
    "Lesson 16 Presentation 3 grammar: the modal verb 会 (will)",
    "她就会打开电视 · 他明天会参加演出吗 · 这个周末我不会去看电影",
    requires=[],
    cards=[
        card("The modal verb 会",
             "In Lesson 8, you learned how to use the modal verb 会 when expressing a learned skill. In this lesson the modal verb 会 is used to indicate that something will happen or something that someone will do. Statement: Subject + 会 + Verb + Object. Negation: Subject + 不 + 会 + Verb + Object.",
             examples=[D(z, e) for z, e in HU]),
        card("Activities 7 and 8",
             "Activity 7 (Speaking, Listening and Reading). A. Complete “my” sentence. Pair up. Student A begins the sentence by giving a specific time, and Student B finishes it using 会 to indicate what they will do at that time; then switch. B. Listen to the conversation and mark each statement True or False: 1. Xiao Zhang believes that David will come to the party if he can. 2. Xiao Zhang believes that David’s girlfriend may not speak Chinese. 3. Xiao Zhang believes that even if David’s girlfriend won’t come to the party, David will still come. C. Check your answers with your partner. D. Read the script with your partner and differentiate the usages of 会 in the conversation. (Audio, not included.) Activity 8 (Speaking, Listening and Writing). Your class is making a class profile page on the MS Teams Wiki. Select one classmate and interview them about their life at DLI as a student: their recreational activities, future plans and any other topic of interest; write a brief report using grammar points such as 给, 会, 不是…就是, 虽然…但是, 对…来说, 甚至…也/都; post it to the MS Teams Wiki (我的同学 XXX). The book’s example and my sentences:",
             examples=[D(z, e) for z, e in HU7]),
    ],
    exercises=[
        M("What does 会 indicate in this lesson?", "That something will happen", ["A learned skill", "A past action", "A wish"], "会 = will."),
        M("What does 下班以后我会给你打电话 mean?", "After work I will call you", ["I called you", "You will call me", "I never call"], "会 = will."),
        M("What does 你想他明天会参加演出吗？ ask?", "Do you think he will take part tomorrow?", ["Does he know how?", "Did he take part?", "Is he able to?"], "会 + future."),
        M("How do you negate 会 (will)?", "不会", ["没会", "会不", "别会"], "Subject + 不 + 会."),
        M("What does 这个周末我不会去看电影 mean?", "I won’t go to the movies this weekend", ["I can’t see movies", "I don’t like movies", "I went last weekend"], "不会."),
        M("What does 天这么黑，等一会儿会下雨吗？ ask?", "Will it rain in a while?", ["Did it rain?", "Is it dark?", "Why is it dark?"], "会下雨."),
        F("下班以后我___给你打电话。", "会", PART, "会 + Verb: will."),
        F("下个星期要考试，这个周末我不___去看电影。", "会", PART, "不会."),
    ],
)

# ------------------------------------------------------------------ 6. 甚至
SZ = [("我太太喜欢看肥皂剧……，有时候，甚至看到半夜还不睡觉。", "My wife likes soap operas…; sometimes she even watches until midnight without sleeping."), ("他玩游戏上瘾，甚至不吃不喝也要玩游戏。", "He is addicted to computer games and doesn’t even care about eating and drinking."), ("唐朝乐队非常有名，甚至有人说它是中国最好的摇滚乐队。", "The Tang Dynasty band is very famous; some people even say it is the best rock band in China.")]
SZ2 = [("大卫连牙刷、毛巾都在网上买。", "David buys even toothbrushes and towels online. (连…都…, Lesson 9)"), ("大卫甚至牙刷、毛巾都在网上买。", "(连 replaced by 甚至)"), ("大卫甚至连牙刷、毛巾都在网上买。", "(连 reinforced by 甚至)"), ("他喜欢看电影，动作片，搞笑片，连动画片他都喜欢看。", "1. He likes movies: action films, comedies, even animated films he likes to watch."), ("他喜欢看电影，动作片，搞笑片，甚至动画片他都喜欢看。", "2. (甚至)"), ("他喜欢看电影，动作片，搞笑片，甚至连动画片他都喜欢看。", "3. (甚至连)")]
L6 = lesson(
    "Lesson 16 Presentation 3 grammar: the adverb 甚至",
    "甚至看到半夜 · 甚至不吃不喝 · 甚至…都/也… and 连…都/也…",
    requires=[],
    cards=[
        card("Adverb 甚至",
             "In the presentation: 我太太喜欢看肥皂剧…，有时候，甚至看到半夜还不睡觉。 In this sentence, 甚至 is used to highlight the severeness of a behavior. 甚至 is used in the following pattern to highlight a high degree of a certain behavior or situation: …，甚至 N/VP + (还/都/也) VP; …，甚至 + Sentence.",
             examples=[D(z, e) for z, e in SZ]),
        card("甚至…都/也… vs 连…都/也…",
             "甚至…都/也… focuses on highlighting a “high degree”; 连…都/也… focuses on emphasizing inclusiveness (including the out of the ordinary). In Lesson 9, Presentation 3, we learned 连…都/也…, which emphasizes inclusiveness; in such sentences, 连 can be replaced or reinforced with 甚至 to highlight the high degree. However, 连 cannot be used to replace 甚至 in sentences that focus on highlighting a high degree of a certain behavior or situation, for example: *我太太喜欢看肥皂剧……，有时候，连看到半夜还不睡觉。 *他玩游戏上瘾，连不吃不喝也要玩游戏。 *唐朝乐队非常有名，连有人说它是中国最好的摇滚乐队。 Activity 9 (Speaking): 1. Think of a person you know well who is indulging in certain hobbies; use 甚至 to report his/her actions or behaviors. 2. Think of something you extremely dislike; use 甚至 and 连…都/也… to talk about it. 3. Think of something you admire very much; use 甚至 and 连…都/也… to talk about it. More examples:",
             examples=[D(z, e) for z, e in SZ2]),
    ],
    exercises=[
        M("What does 甚至 highlight?", "A high degree of a behavior or situation", ["A negation", "A wish", "A past habit"], "甚至 highlights a high degree."),
        M("What does 他玩游戏上瘾，甚至不吃不喝也要玩游戏 mean?", "He is addicted and will even play without eating or drinking", ["He doesn’t play", "He eats while playing", "He plays only after eating"], "甚至."),
        M("What does 唐朝乐队…甚至有人说它是中国最好的摇滚乐队 mean?", "Some people even say it is the best rock band in China", ["It is unknown", "It is the worst band", "It broke up"], "甚至有人说."),
        M("Which focuses on inclusiveness?", "连…都/也…", ["甚至 alone", "虽然…但是", "不是…就是"], "连…都/也…: inclusiveness."),
        M("Can 连 replace 甚至 in 甚至看到半夜还不睡觉?", "No", ["Yes", "Only in questions", "Only in the past"], "*连看到半夜还不睡觉."),
        M("Which sentence is correct?", "大卫甚至连牙刷、毛巾都在网上买", ["大卫连甚至牙刷、毛巾在网上买", "大卫甚至牙刷、毛巾在网上都买", "大卫连牙刷、毛巾甚至在网上买"], "甚至连…都…"),
        F("他喜欢看电影，动作片，搞笑片，___至动画片他都喜欢看。", "甚", PART, "甚至."),
        F("大卫连牙刷、毛巾___在网上买。", "都", PART, "连…都…"),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
SEG = [("除了在家看电视看电影以外，现在的年轻人也流行用手机、用笔记本电脑看。他们每个月付费，用网上的软件下载电影和电视节目。这样不管他们在什么地方，什么时候都能看到想看的电视和电影。", "Segment 1: Besides watching TV and movies at home, young people now also like to watch on phones and laptops. They pay a monthly fee and use online software to download movies and TV programs. This way, wherever and whenever they are, they can watch the TV and movies they want."),
       ("现在许多人家里有好几台电视。有些人家里甚至一个房间就有一台电视。所以家里人常常不在同一个房间看电视，他们想看什么节目就看什么节目。美国人家里的电视也很大，很多人家里都装了家庭影院，而且因为在电影院看电影越来越贵，所以越来越多人喜欢在家看电影了。", "Segment 2: Now many families have several TVs. Some families even have a TV in every room. So family members often don’t watch TV in the same room; they watch whatever program they want. American families’ TVs are also big, many have installed home theaters, and because going to the theater is getting more and more expensive, more and more people like to watch movies at home."),
       ("以前在美国白天看电视的多半是家庭主妇，所以那个时候肥皂剧很流行。妈妈们喜欢一边做家事，一边看电视。那个时候美国人家里只有一台电视，孩子下课，先生下班以后大家会一起看电视，而且看的是同一个电视节目。", "Segment 3: In the past in the US, most of those who watched TV in the daytime were housewives, so soap operas were popular. Mothers liked to do housework while watching TV. At that time American families had only one TV, and after the children got out of school and the husband got off work everyone would watch TV together, the same program.")]
ZF = ("我妈妈是个电视迷。她每天晚上看电视都要看到很晚才睡觉。妈妈喜欢看各种电视节目，像电视剧、体育节目、音乐舞蹈节目和各种健身节目等。妈妈最喜欢看的电视节目是电视剧。只要有电视剧，她都一定一集接着一集地看，不睡觉都没关系。"
      "我姐姐是个舞迷，她一有时间就跟朋友一起去跳舞。她不但喜欢去舞厅跳舞，而且也喜欢去露天舞场跳舞。姐姐每次跳舞都穿得很漂亮。她跳舞跳得很好，所以她除了自己跳舞以外，还教朋友跳舞。姐姐不仅喜欢跳舞，而且也喜欢看各种舞蹈比赛。"
      "我是一个球迷，不仅喜欢参加各种球类活动，而且喜欢看各种球类比赛。我小学的时候开始打乒乓球。中学的时候参加了学校乒乓球队。上大学的时候，我又参加了学校的足球队，下课以后常去操场练习踢球。周末的时候我还常和朋友一起到公园去踢足球。要是我知道哪儿有球赛，我一定会去看。如果买不到票，我就在电视上看。")
ZF_E = ("My mother is a TV fan. Every evening she watches TV until very late before going to sleep. Mother likes all kinds of TV programs, such as TV series, sports programs, music and dance programs and various fitness programs. Her favorite is TV series. As long as there is a series she will definitely watch episode after episode, and doesn’t mind not sleeping. My sister is a dance fan; whenever she has time she goes dancing with friends. She likes dancing not only in dance halls but also on open-air dance floors. She always dresses beautifully to dance. She dances very well, so besides dancing herself she also teaches friends to dance. She likes not only dancing but also watching all kinds of dance competitions. I am a ball-sports fan; I like not only taking part in all kinds of ball activities but also watching all kinds of ball games. I started playing table tennis in elementary school and joined the school table tennis team in middle school. At university I joined the school soccer team and often went to the field after class to practice kicking. On weekends I also often go to the park with friends to play soccer. If I know where there is a game I will definitely go see it; if I can’t get a ticket I watch it on TV.")
Q20 = [("我是中国人吗？", "Am I Chinese?"), ("我是男演员/男明星吗？", "Am I a male actor/male star?"), ("我常演动作片吗？", "Do I often act in action movies?"), ("我很好看吗？", "Am I good-looking?"), ("我差不多三十几岁吗？", "Am I about in my thirties?")]
L7 = lesson(
    "Lesson 16 Presentation 3: skill integration",
    "二十个问题 · 买电影票 · 电视的变化 · 电视迷、舞迷、球迷",
    requires=[],
    cards=[
        card("Activity 1: Play 20 Questions, Who am I?",
             "A. Each student walks around the classroom and asks each classmate yes/no questions to acquire information about that person until the student guesses the correct actor (six photographs of actors, not included). The book’s example questions are below. B. Each student posts his/her favorite actor or actress’s picture, writes a short intro about the celebrity on Linoit, and shares it with the class.",
             examples=[D(z, e) for z, e in Q20]),
        card("Activity 2 (Listening and Speaking): buying movie tickets in Taiwan",
             "Li Xiaowen just moved to Taiwan. He is taking his family to a movie theater for the first time. A. Listen to the conversation and write the EEIs: What did they see? How many tickets were bought? What kinds of tickets were bought? When was the movie shown? Where did they sit? How much did the tickets cost? What payment method was used? B. Guess the meaning of the following words: 全票 and 早场 (mine: full-price ticket; morning show). C. Pair up, read the script aloud and check your answers. D. Role-play: find a movie you want to see this weekend, follow the format of the conversation, and purchase a ticket; your partner plays the person in the ticket booth; switch roles. (Audio and script, not included.)"),
        card("Activity 3 (Reading, Speaking and Listening): three segments",
             "A. Form groups of three. Each member chooses one of the segments to read. B. Within your group, explain the content of your segment in Chinese; take notes on the other members’ reports. C. As a team, use the information you gathered to note the correct order of the segments in the passage, and provide your rationale and summary (one sentence). My key (mine): the order is Segment 3 (the past), Segment 2 (now, many TVs), Segment 1 (the newest trend, phones and laptops); the passage describes how TV watching in the US went from one shared family TV to many TVs and to mobile streaming.",
             examples=[D(z, e) for z, e in SEG]),
        card("Activity 4 (Reading, Speaking and Listening): Zhang Hua’s family",
             "The passage below describes the hobbies of Zhang Hua’s family members. A. Read the passage and write a personal profile for each family member (Mother, Sister, Myself). B. In groups of three, each student gives an oral report on their family members’ hobbies. C. Work with your group members to determine the meaning of the underlined words using context and write them in the table: 节目, 健身, 露天舞场, 球类, 球队. (Mine: program; keep fit; open-air dance floor; ball sports; ball team.)",
             examples=[D(ZF, ZF_E)]),
    ],
    exercises=[
        M("Which segment describes the oldest situation?", "Segment 3 (one TV and housewives)", ["Segment 1", "Segment 2", "None"], "以前在美国…只有一台电视."),
        M("What do young people use to watch now (Segment 1)?", "Phones and laptops", ["Only TVs", "Only cinemas", "Only radios"], "用手机、用笔记本电脑看."),
        M("Why do more people watch movies at home (Segment 2)?", "Going to the theater is more and more expensive", ["Theaters closed", "TVs are free", "Movies are shorter"], "在电影院看电影越来越贵."),
        M("Who is a TV fan in Zhang Hua’s family?", "Mother", ["Sister", "Zhang Hua", "Father"], "我妈妈是个电视迷."),
        M("What does the sister like?", "Dancing, and teaching friends to dance", ["Watching TV", "Soccer", "Table tennis"], "我姐姐是个舞迷."),
        M("What did Zhang Hua do in middle school?", "Joined the school table tennis team", ["Joined the soccer team", "Learned to dance", "Watched TV"], "中学的时候参加了学校乒乓球队."),
        M("What does Zhang Hua do if he can’t get a ticket?", "Watches the game on TV", ["Stays home", "Plays himself", "Gives up"], "如果买不到票，我就在电视上看."),
        M("What does 迷 mean in 电视迷, 舞迷, 球迷?", "Fan; enthusiast", ["Lost", "Mystery", "Teacher"], "迷: fan."),
        M("What does 健身 mean?", "Keep fit", ["Eat well", "Build a gym", "Lose weight"], "健身."),
        F("我姐姐是个舞___，她一有时间就跟朋友一起去跳舞。", "迷", PART, "舞迷: dance fan."),
        F("妈妈最喜欢看的电视节目是电视___。", "剧", PART, "电视剧: TV series."),
    ],
)

# ------------------------------------------------------------------ 8. context
GENRE = table(["Chinese", "Meaning (mine)"],
              [["新闻节目", "news program"], ["游戏节目", "game show"], ["肥皂剧", "soap opera"], ["喜剧/剧集", "sitcom / TV series"], ["真人秀", "reality show"], ["脱口秀", "talk show"], ["儿童节目", "children’s program"], ["体育节目", "sports program"],
               ["动画片", "animated film"], ["动作片", "action movie"], ["剧情片", "drama film"], ["爱情片", "romance film"], ["喜剧片/搞笑片", "comedy film"], ["恐怖片", "horror film"], ["西部片", "western"], ["华语片", "Chinese-language film"]],
              title="Activity 1 A: TV and movie vocabulary (the book leaves the meanings blank; mine)", say=[0])
L8 = lesson(
    "Lesson 16 Presentation 3: using Chinese in context",
    "电视和电影 · 爸爸妈妈的爱好 · 华纳威秀影城 · 电影院指南",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking and Listening)",
             "A. Pair up. Read the following vocabulary (新闻节目, 游戏节目, 肥皂剧, 喜剧/剧集, 真人秀, 脱口秀 (kǒu xiù), 儿童节目, 体育节目; 动画片, 动作片, 剧情 (jù qíng) 片, 爱情片, 喜 (xǐ) 剧片/搞笑片, 恐怖片, 西部片, 华语片) and write the meaning of each entry. B. Share your answers with your partner and discuss what strategies you used, especially for words containing new characters. C. Use the following questions to interview your partner. Movie habits (Student A): 1. How often do you watch a movie? 2. Where do you watch movies? 3. Which movie theater do you go to in Monterey? 4. How do you usually go there? 5. What movie genres do you like? Why? 6. What movie genres do you dislike? Why? 7. What is your favorite movie of all time? 8. Do you prefer watching movies at home or at the theater? Why? TV habits (Student B): 1. How often do you watch TV? 2. On what platform do you watch TV shows (streaming, cable, etc.)? 3. What kinds of TV shows do you like? Why? 4. What kinds of TV shows do you rarely see? Why? 5. What is the longest record of you watching TV nonstop? 6. What is your favorite TV show of all time? 7. Do you prefer watching TV or movies? Why? D. Report your findings to another classmate. E. As a class, share any interesting findings.",
             tables=[GENRE]),
        card("Activities 2 and 3",
             "Activity 2 (Listening, Speaking and Writing). A. Pair up. Each student listens to two short passages and determines the hobby of each family member (Student A: 爸爸, 妈妈; Student B: 我, 弟弟); take notes in the table. B. In Chinese, exchange information with your partner and help them fill in their table. C. Write a short passage about one of your family member’s hobbies. (Audio, not included.) Activity 3 (Reading, Speaking and Writing). You are in a Taiwanese language immersion program. You and your classmate are planning to go to 华纳威秀影城 (huá nà wēi xiù yǐng chéng), one of the biggest movie theater chains in Taiwan, to see a movie this weekend. A. Go to the website linked in the book to find a movie you both want to see and use their online service to practice purchasing tickets. B. Post your search results and give an oral report about your plan; it needs to include the movie title, its genre, date and show time, ticket price and duration. (Website, not included.)"),
        card("Activity 4 (Speaking, Listening, Writing and Reading): Movie Theater Guide Project",
             "You are asked by your teacher to help the Monterey Chinese Community Association create an entertainment guide about movie theaters to enrich the local Chinese community’s entertainment and recreation options. Nearby movie theaters in Monterey: Osio Theater, Century Theaters in the Del Monte Shopping Center, Lighthouse 4 Cinemas in Pacific Grove. A. Form groups of three. Each member selects one theater to research, either from their own experience or by going to the theater’s website to find out about its facilities and services; you can also use Google Maps to find locations and surroundings. B. Give an oral report on what you found and discuss the layout and information you will include in your guide: the theater’s location, transportation options, ticket prices, number of theaters and movies playing, the services and facilities, your overall rating, and other topics. Be creative! C. Each group publishes its written guide on the MS Teams Wiki; the whole class reviews each work and votes for the best theater guide."),
    ],
    exercises=[
        M("What is 肥皂剧?", "A soap opera", ["A cooking show", "A news show", "A sports show"], "肥皂剧."),
        M("What is 动作片?", "An action movie", ["A cartoon", "A romance", "A horror film"], "动作片."),
        M("What is 恐怖片?", "A horror movie", ["A comedy", "A drama", "A western"], "恐怖片."),
        M("What is 搞笑片?", "A comedy", ["A tragedy", "A documentary", "A musical"], "搞笑片."),
        M("What is 真人秀?", "A reality show", ["A cartoon", "A talk show", "A game show"], "真人秀."),
        M("What is 脱口秀?", "A talk show", ["A reality show", "A news program", "A soap opera"], "脱口秀."),
        M("What is 华语片?", "A Chinese-language film", ["A western", "A cartoon", "An action film"], "华语片."),
        M("What is 华纳威秀影城?", "A big movie theater chain in Taiwan", ["A cinema in Beijing", "A TV network", "A streaming site"], "One of the biggest movie theater chains in Taiwan."),
        M("What must the oral report in Activity 3 include?", "Title, genre, date and show time, ticket price and duration", ["Only the title", "Only the price", "A review"], "Activity 3 B."),
        F("我喜欢看轻松的搞笑___和紧张的动作片。", "片", PART, "搞笑片."),
    ],
)
L9 = vocab_lesson("Lesson 16 Presentation 3 vocabulary", "27 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 10. Area Studies
L10 = lesson(
    "Lesson 16 Area Studies: Chinese Entertainment and Leisure",
    "中国人的娱乐和休闲 · travel · the internet · live entertainment · sports · seniors",
    requires=[],
    cards=[
        card("Chinese Entertainment and Leisure",
             "In the past in China, television was the first choice of leisure activity after work or on the weekend. With the increase in disposable income and changing lifestyles, Chinese leisure activities are becoming more diverse. Travelling ranks #1 on the billboard chart of “Ten most popular leisure activities among Chinese.” Nearly 50% of people spend their leisure time travelling. In 2008, Chinese travelers took over 45 million foreign trips. That figure increased to 162 million in 2018. Domestic tourism has also tripled over this period. Using the internet is the second most common leisure activity for Chinese people. The digital revolution, especially the rise of social media and e-commerce, has had a deep impact on the leisure habits of the Chinese. Like the rest of the developed world, China has grown fond of smartphones that can perform an endless list of tasks, from talking to friends, shopping, and playing games. Chinese internet users now spend an average of 4.7 hours per day on their phones for entertainment like e-reading, music streaming, karaoke, video streaming, mobile gaming, live streaming, and, of course, watching short videos."),
        card("Shopping, karaoke, movies and the performing arts",
             "Although technology has allowed people to spend their free time browsing the internet, other leisure activities are still popular. Shopping is very popular in China, particularly among women. The other leisure-related area that has been growing is dining out, particularly foreign food and restaurants alongside the homegrown ones. Karaoke is also a common social activity in China. It is often conducted in a small room with close friends and combined with alcoholic drinks. China now has more than 60,000 movie screens, the most of any nation on earth, almost all built within the last 10 years. Chinese moviegoers are young and tend to be centered in the cities. Young Chinese are showing more interest in the performing arts like theater, dance, and music, to name a few. Live entertainment is in demand as young people are more willing to pay for it than previous generations. By 2019, China had over 10,000 performing groups, more than 10,000 brokerage firms and 1,800 professional theaters, whose number is growing every year, according to the secretary-general of the China Association of Performing Arts."),
        card("Sports and seniors",
             "Sports is a large part of the Chinese people’s lives. Sports fans fill the whole spectrum of sporting venues. According to data from the National Bureau of Statistics, in 2019, there were 3.162 million sports venues in China, with an average of 1.86 square meters per person. From traditional gyms, swimming pools, and badminton halls to emerging climbing gyms and ski resorts, the Chinese have more choices than ever for fitness. Chinese people prefer outdoor sporting activities, but even indoors many people are getting into shape using various types of body-building equipment or by practicing aerobic exercise following TV instruction. Roller skating and golf have recently gained popularity as well. Elderly people like practicing Taijiquan, Qi Gong or Square Dancing in parks. They go very early in the morning or near dusk. Public square dance is an exercise routine performed to music in squares, parks, or open spaces. These activities are popular with middle-aged and retired women, with over 100 million practitioners due to the low cost and ease of participation. It has become increasingly common for governments at different levels to set up special places for seniors to engage in recreational activities for the newly retired to make new social contacts. There are many senior recreational centers with various types of recreational facilities in both cities and rural areas. Seniors play cards, chess, and practice calligraphy. There are different types of senior universities and night schools that retired people attend. Chinese people are no longer content with merely good food and an easy life but are pursuing a healthier and higher quality of life. (Pictures, not included.)"),
    ],
    exercises=[
        M("What was the first choice of leisure in the past?", "Television", ["Travel", "Karaoke", "Sports"], "Television was the first choice."),
        M("Which leisure activity ranks first today?", "Travelling", ["The internet", "Shopping", "Karaoke"], "Travelling ranks #1."),
        M("How many foreign trips did Chinese travelers take in 2018?", "162 million", ["45 million", "4.7 million", "60,000"], "162 million in 2018."),
        M("Which is the second most common leisure activity?", "Using the internet", ["Travelling", "Reading", "Dining out"], "Using the internet is second."),
        M("How many hours do Chinese users spend on phones per day for entertainment?", "4.7 hours on average", ["1 hour", "10 hours", "30 minutes"], "4.7 hours per day."),
        M("How is karaoke often held in China?", "In a small room with close friends, often with alcohol", ["In a stadium", "Outdoors", "At school"], "Often conducted in a small room."),
        M("How many movie screens does China have?", "More than 60,000, the most of any nation", ["About 6,000", "About 600", "About 600,000"], "More than 60,000."),
        M("Who is more willing to pay for live entertainment?", "Young people", ["Seniors", "Children", "Tourists"], "Young people are more willing to pay."),
        M("What do elderly people like practicing in parks?", "Taijiquan, Qi Gong and square dancing", ["Rock climbing", "Skiing", "Golf"], "Elderly people like practicing Taijiquan, Qi Gong or Square Dancing."),
        M("How many practitioners does public square dance have?", "Over 100 million", ["About 1 million", "About 10,000", "About 3 million"], "Over 100 million practitioners."),
        M("What do governments set up for retirees?", "Special places for recreation and new social contacts", ["Free housing", "Free flights", "Movie theaters"], "Special places for seniors."),
    ],
)

UNIT = unit("第十六课 娱乐活动 Presentation 3: movies and TV, 给, 不是…就是, 虽然…但是, 会, 甚至, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
