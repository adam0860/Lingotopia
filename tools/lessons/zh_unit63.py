"""Unit 63: Lesson 22 (Asking for Directions) Presentation 1 from the book's texts: the embassy dialog, the five activities, 还 as a modal adverb,
approximate numbers, the expressions for taking the subway and the bus, the skill-integration directions (David, the travel agency), the using-Chinese
activities (Zaicheng in Qingdao) and the vocabulary list. Audio, maps, pictures and links are not included; numbers the book writes as digits are
spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l22_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('干净', 0, 'gan1'), ('还以为', 0, 'hai2'), ('还担心', 0, 'hai2'), ('还可以', 0, 'hai2'), ('还不错', 0, 'hai2'), ('还行', 0, 'hai2'), ('还没', 0, 'hai2'), ('还真', 0, 'hai2'), ('还在', 0, 'hai2'), ('还好', 0, 'hai2'), ('还高', 0, 'hai2'), ('还上过', 0, 'hai2'), ('您得到马', 1, 'dei3')):
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

# ------------------------------------------------------------------ 1. dialog
P1 = [("马克", "请问，到美国大使馆怎么走？", "Excuse me, how do I get to the American Embassy? (translation mine)"), ("路人", "美国大使馆？我还真不知道。那边有位民警，你去问问他吧！", "The American Embassy? I really don’t know. There is a traffic policeman over there; go and ask him!"),
      ("马克", "谢谢。（走到民警面前）您好！能麻烦您一下吗？", "Thanks. (walks up to the policeman) Hello! May I trouble you for a moment?"), ("民警", "没问题。什么事儿？", "No problem. What is it?"),
      ("马克", "我护照丢了，要去大使馆补办，可是一出火车站我就迷路了。", "I lost my passport and need to go to the embassy to get it replaced, but as soon as I came out of the train station I got lost."),
      ("民警", "哦，去美国大使馆啊。到对面的地铁站，乘二号线，坐四站到东直门，然后…", "Oh, to the American Embassy. Go to the subway station opposite, take Line 2, ride four stops to Dongzhimen, and then…"),
      ("马克", "对不起。您能说慢一点儿吗？", "Sorry. Could you speak a little more slowly?"), ("民警", "你看见那边的地铁站了吗？在那儿坐二号线到东直门，然后换四一八路公交车，坐到安家楼站下车。", "Do you see the subway station over there? Take Line 2 from there to Dongzhimen, then change to bus number 418 and ride to Anjialou Station and get off."),
      ("马克", "要坐几站到安家楼？", "How many stops to Anjialou?"), ("民警", "六站吧？你上了车再问问司机。", "Six, I think? Ask the driver again after you get on."), ("马克", "好。下车以后呢？", "OK. And after I get off?"),
      ("民警", "下车以后往东走，你会经过一座立交桥，继续往前走，在十字路口那儿往左拐，再走四五分钟就到了。大使馆就在你的左手边。", "After you get off, walk east. You will pass an overpass. Keep going forward, turn left at the crossroads, and in another four or five minutes you will be there. The embassy is on your left."),
      ("马克", "那儿有什么标志吗？", "Is there any sign there?"), ("民警", "门前有一面美国国旗，你到那儿就可以看见了。", "There is an American flag in front of the gate; you will see it when you get there."), ("马克", "谢谢！", "Thank you!")]
L1 = lesson(
    "Lesson 22 Presentation 1: how to get to the embassy",
    "请问怎么走 · 迷路 · 乘地铁 换公交 · 往东走 往左拐 · 左手边",
    requires=[],
    cards=[
        card("Unit 4 overview and Lesson 22 objectives (请问怎么走, Asking for Directions)",
             "Unit 4, Survival Skill and Social Factors. Lesson 22 topic: Ask for directions. Tasks and functions: obtain and provide simple directions; ask and provide directions; understand and explain ways of taking public transportation; describe facilities and provide directions at an airport. Grammar: 还 as a modal adverb; common expressions for taking public transportation; the basic structure of explanatory text; approximate numbers. Area Studies: China’s Tourism. Upon completion of this lesson you will be able to: ask for directions; understand and give directions for driving, walking, and taking public transportation; describe facilities and provide directions at an airport. To do so you must master: new words and phrases for these functions; common expressions used when taking public transportation; the general expressions for giving directions; the basic structure of explanatory text; 还 as a modal adverb; approximate numbers."),
        card("Getting Started",
             "Pair up and discuss: A. How do you usually get directions when you go someplace new? B. What is the best way to get directions when taking public transportation? C. Have you ever gotten lost? How did you find directions? D. Has anyone ever asked you for help with directions? How did you help them? E. In the internet era, do you think people can still get lost? Under what circumstances might that happen? (A photograph is not included.)"),
        card("Presentation 1: 到美国大使馆怎么走", "The book also prints the dialog in traditional characters; the digits 2 and 418 are spelled out in the Chinese text. The translations are mine.", examples=dlg(P1)),
    ],
    exercises=[
        M("Where does Mark want to go?", "The American Embassy", ["The train station", "The airport", "A bookstore"], "到美国大使馆怎么走?"),
        M("Why does he need to go there?", "He lost his passport", ["He lost his phone", "He wants a visa for a friend", "He works there"], "我护照丢了，要去大使馆补办."),
        M("Why did Mark get lost?", "He had just come out of the train station", ["His phone had no battery", "He took the wrong bus", "He had no map"], "一出火车站我就迷路了."),
        M("Who does the first passerby suggest he ask?", "The traffic policeman nearby", ["The driver", "A taxi", "A teacher"], "那边有位民警，你去问问他吧!"),
        M("Which subway line does Mark take?", "Line 2", ["Line 4", "Line 5", "Line 8"], "乘二号线."),
        M("How many stops does he ride on the subway?", "Four", ["Two", "Six", "Eight"], "坐四站到东直门."),
        M("Which bus does he change to?", "Bus 418", ["Bus 320", "Bus 1", "Bus 208"], "换四一八路公交车."),
        M("How many bus stops does the policeman guess?", "Six", ["Four", "Two", "Ten"], "六站吧?"),
        M("Which way does he walk after leaving the bus?", "East", ["West", "South", "North"], "下车以后往东走."),
        M("Where does he turn left?", "At the crossroads", ["At the overpass", "At the station", "At the flag"], "在十字路口那儿往左拐."),
        M("Where is the embassy?", "On his left", ["On his right", "Behind the station", "Under the overpass"], "大使馆就在你的左手边."),
        M("What sign tells him he has arrived?", "An American flag in front of the gate", ["A red lantern", "A big clock", "A bus stop"], "门前有一面美国国旗."),
        F("我护照丢了，要去大使馆___办。", "补", PART, "补办: replace."),
        F("下车以后往东走，你会经过一座立交___。", "桥", PART, "立交桥: overpass."),
        F("在十字路口那儿往左___。", "拐", PART, "往左拐: turn left."),
    ],
)

# ------------------------------------------------------------------ 2. activities
A2 = [("到前面的地铁站，乘二号线，坐四站到东直门，然后换四一八路公交车，坐到安家楼站下车。再往东走二百米左右就到了。", "The book’s English: Go to the subway station in front, take Line 2 and go four stops to Dongzhimen; then change to bus number 418 and get off at Anjialou. Walk about 200 meters east and you will be there. The blanks are 地铁站, 二号线, 坐四站, 换, 公交车, 站下车, 往东走. (key mine; the book prints 418 and 200 in digits)")]
A4 = dlg([("甲", "请问，图书馆怎么走？", "Excuse me. How do I get to the library?"), ("乙", "从这儿一直往前走，你会经过一座立交桥。往前走，在一个很大的十字路口那儿往右拐。走三四分钟，图书馆就在你的左边。", "Go straight ahead from here and you will pass an overpass. Continue walking forward and turn right at a large intersection. Walk another three or four minutes and the library is on your left. (completed from the book’s English; the key is mine)")])
L2 = lesson(
    "Lesson 22 Presentation 1 activities: routes to the embassy and the library",
    "Activities 1 to 5 · 二号线 东直门 四一八路 安家楼 · 经过立交桥 · 十字路口往右拐",
    requires=[],
    cards=[
        card("Activity 1 (Listening)",
             "A. Global listening: listen to Presentation 1 once and answer: 1. Where does Mike need to go? Why? (the American Embassy, to replace his lost passport) 2. Who gave Mike directions? (a passerby and a traffic policeman) 3. What kind of public transportation does Mike need to take? (the subway and a bus). B. Detailed listening: 1. Draw a map of Mike’s route to his destination in your notebook (a subway and bus route, then a walking route, ending near 安家楼; the blank map is not included). 2. In groups of three, compare your work and discuss any inconsistencies. (Audio, not included; the answers in brackets are from the text.)"),
        card("Activity 2 (Reading, Speaking and Listening)",
             "A. Using the English translation, complete the sentences with the correct Chinese words. B. Pair up. Read your work to your partner. Listen and discuss the differences. The completed paragraph:",
             examples=[D(*A2[0])]),
        card("Activity 3 (Listening, Writing, Reading and Speaking)",
             "A. There is more than one way to get to the Embassy from the train station. Listen to two different routes (Route 1, Route 2). Take note of the routes and transcribe the names of the stations. B. Pair up. Compare your notes with your partner’s. C. There are three different routes, including the one in the presentation. Rank the three routes according to your preference. Tell your partner the reason(s) for your ranking. D. Vote as a class to see which route is the most preferred and which is least preferred. (Audio, not included.)"),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Using the English translation, complete the sentences with the correct Chinese words. B. Pair up. Read your work to your partner. Listen and discuss the differences. The book gives the English and the blanks 怎么走, 往前走, 经过, 十字路口, 往右拐, 三四, 左边; my completion:",
             examples=A4),
        card("Activity 5 (Writing and Speaking)",
             "A. Using the map, write a short set of instructions on how to get to the U.S. Embassy from the China World Hotel (香格里拉饭店 Xiānggélǐlā fàndiàn); type in Pinyin or characters. The map marks a traffic light, 红绿灯 (hónglǜdēng), the U.S. Embassy Main Building and Visa Building, the China World Hotel and a DLIFLC logo. B. In groups of three, compare your work with that of your partners. (The map is not included, so I have not written a sample route.)"),
    ],
    exercises=[
        M("What does Activity 1 ask you to draw?", "Mike’s route to his destination", ["A picture of the embassy", "A map of China", "A floor plan"], "Draw a map of Mike’s route."),
        M("How many routes are compared in Activity 3?", "Three, including the one in the presentation", ["One", "Two only", "Five"], "There are three different routes."),
        M("Which word fills “到前面的___，乘二号线”?", "地铁站", ["停车场", "火车站", "公园"], "到前面的地铁站."),
        M("Which word fills “坐四站到东直门，然后___四一八路公交车”?", "换", ["买", "借", "拿"], "然后换公交车."),
        M("Which phrase means “walk about 200 meters east”?", "往东走二百米左右", ["往西走二百米左右", "往东开两公里", "往北走三分钟"], "往东走二百米左右就到了."),
        M("Which fills “你会___一座立交桥”?", "经过", ["乘坐", "看见了", "到达了"], "你会经过一座立交桥."),
        M("Which fills “在一个很大的十字路口那儿往右___”?", "拐", ["看", "坐", "开"], "往右拐."),
        M("Where is the library at the end?", "On your left", ["On your right", "Straight ahead", "Behind you"], "图书馆就在你的左边."),
        F("到前面的地铁站，___二号线，坐四站到东直门。", "乘", PART, "乘 is the formal verb for taking a line."),
        F("再走三四分钟，图书馆就在你的___边。", "左", PART, "左边."),
    ],
)

# ------------------------------------------------------------------ 3. 还
H1 = [("美国大使馆？我还真不知道。", "The book’s example 1: The American Embassy? I really don’t know. (还 expresses surprise: something the speaker just realized he should have known)"), ("我看，你是上网上瘾了。——还真有点儿。", "2. I think you’re addicted to the internet. — Yes, a bit actually. (还 again expresses surprise; the book prints 上网瘾了, which I read as 上网上瘾了)"), ("你看起来这么年轻，我还以为你是学生呢！", "3. You look so young, I thought you were a student! (the speaker is surprised that his earlier thought was wrong)"),
      ("流感啊？我还担心是肺炎呢。", "4. The flu? I was afraid it was pneumonia. (还 expresses relief from an original worry)"), ("听起来挺酷的。——那当然，我们的乐队还上过电视呢！", "5. It sounds pretty cool. — Of course; our band has even been on TV! (还 creates a sense of pride and can be translated “even”)")]
H2 = [("饭厅还可以，厨房好像小了一点儿。", "1. The dining room is OK; the kitchen seems a little small."), ("这次她考得还好。", "2. She did fairly well on this exam. (the book prints 考的)"), ("这家饭店做的菜还不错。", "3. The dishes at this restaurant are pretty good."), ("这件衣服的颜色还行，就是样式有点老。", "4. The color of this garment is all right; the style is just a bit old-fashioned."),
      ("他比爸爸还高了！", "Note: He is even taller than his father! (还 + adjective in a comparative sentence works as emphasis)"), ("我卖的西瓜比篮球还大，比糖还甜。", "My watermelons are even bigger than a basketball and sweeter than candy.")]
H3 = [("这个房子还可以，但是有点儿贵。", "1. 还 weakens the positive adjective: This house is OK, but a bit expensive. (key mine)"), ("我还没去过中国的邮局。", "2. 还没 = not yet (the ordinary meaning, “still/yet”): I haven’t been to a Chinese post office yet."), ("他唱得比专业歌手还好。", "3. 还 in a comparison emphasizes: He sings even better than a professional singer."),
      ("晚上一个人走路，还真有点儿害怕。", "4. 还真 expresses surprise at oneself: Walking alone at night, I really am a bit scared."), ("你还在这儿？我还以为你回家了呢。", "5. First 还 = still; second 还以为…呢 expresses surprise that the earlier thought was wrong: You’re still here? I thought you had gone home.")]
L3 = lesson(
    "Lesson 22 Presentation 1 grammar: 还 as a modal adverb",
    "我还真不知道 · 我还以为…呢 · 还担心…呢 · 还可以 还不错 · 比…还…",
    requires=[],
    cards=[
        card("还 Used to Express a Certain Mood or Tone",
             "Aside from its many other meanings and usages, 还 can also be used to express certain moods or tones, depending on the context. Pattern: Subject + 还 + Predicate. In sentences 1 and 2, 还 expresses a surprised tone, indicating something the speaker just realized but thinks he should have known or realized before. In sentence 3, the speaker is surprised that his previous thoughts were wrong. In sentence 4, 还 expresses a tone of relief from original worries. In sentence 5, 还 creates a sense of pride and can be translated as “even” in English. Without 还, these sentences are bland, even though they still convey the same meaning.",
             examples=[D(z, e) for z, e in H1]),
        card("还 before a positive adjective",
             "Another common use of 还 is to place it in front of a positive adjective to weaken it, or to make the speaker’s tone less enthusiastic. Pattern: Subject + 还 + Positive Adjective (好 / 行 / 可以 / 不错). Notes: when “还 + adjective” is used in a comparative sentence, it functions as emphasis.",
             examples=[D(z, e) for z, e in H2]),
        card("Activity 1 (Reading and Speaking)",
             "Read the following sentences and explain the function of each use of 还. Then pair up and check your answer with your partner’s. The book gives the five sentences; the explanations are mine:",
             examples=[D(z, e) for z, e in H3]),
    ],
    exercises=[
        M("What does 还 express in 美国大使馆？我还真不知道?", "Surprise at something the speaker should have known", ["Relief", "Pride", "Weakening"], "还 shows a surprised tone."),
        M("What does 还 express in 我还以为你是学生呢?", "Surprise that the earlier thought was wrong", ["Relief", "Pride", "Anger"], "还以为…呢."),
        M("What does 还 express in 流感啊？我还担心是肺炎呢?", "Relief from an original worry", ["Pride", "Surprise at a rule", "Anger"], "还担心…呢."),
        M("What does 还 express in 我们的乐队还上过电视呢?", "Pride, like “even”", ["Relief", "Doubt", "Fear"], "还…呢: pride."),
        M("What does 还 do in 饭厅还可以?", "Weakens the adjective, less enthusiastic", ["Strengthens it", "Negates it", "Turns it into a question"], "还 + positive adjective: weaker."),
        M("Which adjectives does the weakening pattern use?", "好, 行, 可以, 不错", ["大, 小, 多, 少", "冷, 热, 凉", "高, 矮, 胖"], "好/行/可以/不错."),
        M("What does 还 do in 他比爸爸还高了?", "Emphasizes the comparison", ["Weakens the comparison", "Makes it a question", "Turns it into the past"], "比…还…: emphasis."),
        M("What does 我还没去过中国的邮局 mean?", "I haven’t been to a Chinese post office yet", ["I don’t want to go", "I went twice", "It was closed"], "还没: not yet."),
        F("你看起来这么年轻，我___以为你是学生呢！", "还", PART, "还以为…呢."),
        F("这家饭店做的菜还___错。", "不", PART, "还不错."),
    ],
)

# ------------------------------------------------------------------ 4. approximate numbers
AN = table(["说法", "意思"], [["几分钟", "a few minutes"], ["十几分钟", "between 10–20 minutes"], ["十多分钟", "between 10–20 minutes"], ["二十来分钟", "between 20–30 minutes"], ["二十分钟左右", "about 20 minutes"], ["二十分钟上下", "about 20 minutes"]], title="Approximate numbers", say=[0])
AE = [("再走四五分钟就到了。", "The book’s example 1: Walk four or five more minutes and you’ll be there."), ("教室里只有两三个学生。", "2. There are only two or three students in the classroom."), ("操场上有十七八个学生在锻炼。", "3. There are seventeen or eighteen students exercising on the playground."), ("他看起来三十五六岁的样子。", "4. He looks about thirty-five or thirty-six."), ("西安市的人均工资是六七千元人民币。", "5. The average income per person in Xi’an is six or seven thousand yuan.")]
LE = [("我请你喝两杯。", "1. I’ll treat you to a couple of drinks."), ("来，下两盘（棋）！", "2. Come on, let’s play a couple of games (of chess)!"), ("过两天就是爸爸的生日了。", "3. In a couple of days it’s Dad’s birthday."), ("到我这儿来玩儿两天吧。", "4. Come and stay with me a couple of days.")]
A2E = [("我今天买了十一个苹果。", "1. The book’s wrong sentence: 我今天买了十十一个苹果. Fix (mine): numbers ending in 0 cannot be placed next to another number, so say 十一个 (exactly eleven) or 十几个 (about ten-odd): I bought eleven apples today."), ("操场上有十五六个学生。", "2. Wrong: 十五十六个. Two-digit numbers used together must be shortened: There are fifteen or sixteen students on the playground. (fix mine)"), ("我认识两三个中国朋友。", "3. Wrong: 二三个. 二 before a measure word is 两: I know two or three Chinese friends. (fix mine)"), ("我吃了六七个饺子。", "4. Wrong: 六八个. Adjacent approximate numbers must be consecutive (六七 or 七八): I ate six or seven dumplings. (fix mine)"),
        ("张文：过两天咱们去看电影吧。——马克：好的，是后天吗？", "5. Wrong: 过两天 is an unspecified “in a couple of days” (like 几天), not exactly the day after tomorrow, so Mark’s question is a misunderstanding: Zhang Wen: Let’s go to the movies in a couple of days. — Mark: OK, do you mean the day after tomorrow? (key mine)")]
A3W = [("他今年五六十岁了。", "1. Mr. Wang is fifty to sixty years old. (Activity 3, mine)"), ("他在这所大学工作二三十年了。", "2. He has been working at the university for twenty to thirty years. (mine)"), ("他的工资每个月五六千元左右。", "3. His salary is around five or six thousand yuan a month. (mine)"), ("他每个班有二十五六个学生。", "4. He has twenty-five or twenty-six students in each class. (mine)"), ("他每个星期上十四五个小时的课。", "5. He teaches fourteen or fifteen hours a week. (mine)"), ("他每天晚上十一二点才下班。", "6. He does not finish work until eleven or twelve every night. (mine)")]
POEM = [("一望二三里，烟村四五家，门前六七树，八九十枝花。", "Activity 4: the poem of numbers. As far as the eye can see, two or three li; a misty village of four or five homes; before the door six or seven trees; eight, nine, ten sprays of flowers. (translation mine)")]
L4 = lesson(
    "Lesson 22 Presentation 1 grammar: approximate numbers",
    "几分钟 十几分钟 二十来分钟 二十分钟左右 · 四五分钟 两三个 十七八个 · 两 as 几 · 一望二三里",
    requires=[],
    cards=[
        card("Approximate Numbers",
             "There are various ways to express an approximate number. Another way to express approximation is by using two numbers together; usually the smaller number is placed before the larger. Pattern: Number + (Number + 1).",
             tables=[AN], examples=[D(z, e) for z, e in AE]),
        card("Notes",
             "1. When 二 and 三 are used together as single-digit numbers and followed by a measure word, 二 usually is in the form of 两, like 两三个菜, 两三斤苹果. 2. Numbers that end with “0” cannot be used with adjacent numbers, like “9, 10” or “10, 11”. 3. When two-digit numbers are used together, they must be shortened; “16 or 17” would be 十六七, and “30 to 40” would be 三四十. Note that even when used alone, 两 can be an unspecified number. Like the English phrase “a couple of”, 两 is an unspecified number in the sentences below and is equivalent to 几, or “a few.”",
             examples=[D(z, e) for z, e in LE]),
        card("Activity 2 (Reading)",
             "Pair up. With your partner, discuss what is wrong with the following sentences. The book prints the five wrong sentences (it prints the digit-free forms 十十一, 十五十六, 二三, 六八 and the 过两天 dialog); my corrections and reasons:",
             examples=[D(z, e) for z, e in A2E]),
        card("Activity 3 (Speaking)",
             "Pair up. Read about Mr. Wang and take turns saying the underlined phrases in Chinese: 1. Mr. Wang is 50–60 years old. 2. He has been working at the university for 20–30 years. 3. His salary is around ¥5000–6000 a month. 4. He teaches 25 to 26 students in each class. 5. He teaches 14–15 hours per week. 6. He does not finish work until 11 p.m.–12 a.m. every night. My sentences:",
             examples=[D(z, e) for z, e in A3W]),
        card("Activity 4 (Reading)", "Read the poem aloud and note the poetic use of numbers (the book adds a picture, not included).", examples=[D(z, e) for z, e in POEM]),
    ],
    exercises=[
        M("What does 十几分钟 mean?", "Between 10 and 20 minutes", ["Exactly ten minutes", "Between 20 and 30 minutes", "About an hour"], "十几: 11–19."),
        M("What does 二十来分钟 mean?", "Between 20 and 30 minutes", ["Exactly 20 minutes", "A few minutes", "Under ten minutes"], "二十来: 20–30."),
        M("How do you say “four or five minutes”?", "四五分钟", ["四个五分钟", "四和五分钟", "四有五分钟"], "Two adjacent numbers together."),
        M("How do you say “seventeen or eighteen students”?", "十七八个学生", ["十七十八个学生", "十七和十八个学生", "十七个十八学生"], "Two-digit numbers are shortened."),
        M("How do you say “two or three Chinese friends”?", "两三个中国朋友", ["二三个中国朋友", "二个三个中国朋友", "两和三个中国朋友"], "二 before a measure word is 两."),
        M("Why is 十十一 wrong?", "Numbers that end in 0 cannot be placed next to another number", ["It is too big", "It needs 两", "It has no measure word"], "Note 2."),
        M("What does 过两天 mean?", "In a couple of days (not exactly two)", ["Exactly the day after tomorrow", "Two days ago", "Every two days"], "两 as an unspecified number, like 几."),
        M("What does 来，下两盘！ mean?", "Come on, let’s play a couple of games!", ["Let’s play two exact games", "Let’s eat two plates", "Let’s go down two floors"], "两盘: a couple of games."),
        F("他看起来三十五___岁的样子。", "六", PART, "三十五六岁."),
        F("教室里只有___三个学生。", "两", PART, "两三个."),
    ],
)

# ------------------------------------------------------------------ 5. public transportation
TP = table(["步骤", "表达", "English"], [["从起点", "从某地 / 在某地", "From the starting point"], ["乘地铁", "乘/坐 + 地铁 + 几号线", "Taking a subway (乘 is more formal than 坐)"], ["坐几站", "坐 + 几 + 站", "Making several stops"], ["下车", "到/在 + 某站 + 下车", "Getting off the subway at a certain stop"], ["换线", "换 + 几号线", "Transferring subway lines"], ["到达", "…就到了。/ 就到…了。", "Arriving at the destination"]],
           title="Common expressions for taking the subway (the book writes the blanks with ～ and #; I used 某地, 几号线 and 几)", say=[1])
BE = [("到对面的地铁站，乘二号线，坐四站到东直门。", "From the dialog: Go to the subway station opposite, take Line 2, go four stops to Dongzhimen."), ("在那儿坐二号线到东直门，然后换四一八路公交车，坐到安家楼站下车。", "Take Line 2 there to Dongzhimen, then change to bus 418 and ride to Anjialou Station and get off. (the same expressions work for buses, which are marked with 路 instead of 线)")]
L5 = lesson(
    "Lesson 22 Presentation 1 grammar: taking the subway and the bus",
    "从/在 · 乘/坐 地铁几号线 · 坐几站 · 到/在…站下车 · 换…线 · …就到了",
    requires=[],
    cards=[
        card("Common Expressions Used When Taking Public Transportation",
             "In China, subway routes are often coded with numbers, colors, or the name of the main destination. As you can see on the Beijing subway map (not included), there are 地铁4号线, 地铁5号线, 地铁8号线, 地铁大兴线, 地铁大兴机场线 and 地铁亦庄线. The expressions for taking a bus are the same as those for the subway. Buses are usually marked with 路 instead of 线.",
             tables=[TP], examples=[D(z, e) for z, e in BE]),
        card("Activities 7 and 8 (Speaking)",
             "Activity 7: A. 马克 is at Terminal 3 at the Beijing Capital International Airport. Tell him how to get to 建国门 by subway, using the map and search results as a reference (Map A). B. 马克 wants to go to the 王府井 shopping center from 北京大学. Tell him how to get there by subway, using Map B. Activity 8: A. Use the bus routes below to find a way to get from 火车站 to 钟楼站 in Xi’an. B. Use the bus route below to find a way to get from 钟楼站 to the Terracotta Warriors Museum (兵马俑) in Xi’an. New word: 终点站 (zhōngdiǎn zhàn; last stop; terminal). (The subway maps, search results and bus-route screenshots are not included.)"),
    ],
    exercises=[
        M("Which is more formal, 乘 or 坐?", "乘", ["坐", "They are the same", "Neither is used for subways"], "乘 is more formal than 坐."),
        M("How do you say “take Line 2”?", "乘二号线", ["吃二号线", "买二号线", "看二号线"], "乘/坐 + 地铁 + line."),
        M("How do you say “ride four stops”?", "坐四站", ["站四坐", "坐站四", "四坐站"], "坐 + number + 站."),
        M("How do you say “get off at Anjialou Station”?", "在安家楼站下车", ["在安家楼站上车", "到安家楼站买车", "往安家楼站拐"], "到/在 + station + 下车."),
        M("How do you say “change to Line 4”?", "换四号线", ["拐四号线", "借四号线", "停四号线"], "换 + line."),
        M("What do buses use instead of 线?", "路", ["站", "号", "桥"], "Buses are marked with 路."),
        M("Which means “the last stop”?", "终点站", ["十字路口", "停车牌", "立交桥"], "终点站: last stop."),
        F("到对面的地铁站，___二号线，坐四站到东直门。", "乘", PART, "乘 + line."),
        F("坐四站到东直门，然后___四一八路公交车。", "换", PART, "换 = change."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
S3 = dlg([("大卫", "请问，从这儿到美国大使馆怎么走？", "Excuse me, how do I get to the American Embassy from here?"), ("路人", "你从这儿过马路，到对面坐三二零路公交车，然后在天安门换往东开的一路公共汽车，坐五站到建国门下车。", "Cross the road here, take bus 320 on the other side, then at Tiananmen change to bus 1 going east, ride five stops and get off at Jianguomen."), ("大卫", "在哪儿下车？我没听清楚。您能不能再说一遍？", "Where do I get off? I didn’t hear clearly. Could you say it once more?"),
          ("路人", "在建国门下车。下车后再走二十多分钟就到了。", "Get off at Jianguomen. After you get off, walk another twenty-odd minutes and you will be there."), ("大卫", "那在建国门下了车怎么走？", "And how do I walk after getting off at Jianguomen?"),
          ("路人", "下了车，你会看到一座立交桥，你在红绿灯那儿过马路，然后沿着那条路往北走，在第二个十字路口向右拐，再一直往前走就到了。", "After getting off you will see an overpass. Cross the road at the traffic light, then walk north along that road, turn right at the second crossroads, and keep going straight ahead; you’ll be there."),
          ("大卫", "大使馆在路的左边还是右边？", "Is the embassy on the left or the right side of the road?"), ("路人", "我不太清楚，不过大楼前有美国国旗。你到那儿就知道了。", "I’m not too sure, but there is an American flag in front of the building. You’ll know when you get there."), ("大卫", "谢谢您！", "Thank you!"), ("路人", "不客气。", "You’re welcome.")])
S4 = dlg([("甲", "请问到大华旅行社怎么走？", "Excuse me, how do I get to the Dahua Travel Agency?"), ("乙", "您从前边儿那个立交桥底下一直往北走，到了十字路口往西拐，路北有个菜市场，菜市场的旁边是个银行，在银行那儿向北拐，沿着那条街往北走不远，有个农贸市场，农贸市场的对面就是大华旅行社。", "From under that overpass ahead, go straight north; at the crossroads turn west; on the north side of the road there is a vegetable market, next to the vegetable market is a bank; at the bank turn north, walk north along that street not far, and there is a farmers’ market; Dahua Travel Agency is right opposite the farmers’ market."),
          ("甲", "谢谢！哎，坐公共汽车能不能到那儿？", "Thanks! Oh, can I get there by bus?"), ("乙", "可以，不过您得到马路对面去坐车。您要是在马路这边儿坐车，您就坐到别的地方去了。", "You can, but you have to go across the road to catch the bus. If you take the bus on this side, you’ll end up somewhere else.")])
L6 = lesson(
    "Lesson 22 Presentation 1 skill integration: maps, buses and directions to the travel agency",
    "过马路 · 三二零路 换一路 · 沿着那条路往北走 · 大华旅行社 · 到马路对面去坐车",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading and Speaking)",
             "Pair up. Listen to each audio segment (eight segments) and use the map to find the destination it describes. Mark the number of the corresponding segment on the map. Compare your work with your partner’s. The map’s labels (the picture is not included) are: 人民南路, 商场, 医院, 体育馆, 公共汽车站, 书店, 西大街, 电影院, 理发店, 停车场, 咖啡厅, 中国饭馆, 东大街, 邮局, 图书馆, 银行, 学校, with traffic lights at the crossings."),
        card("Activity 2 (Listening and Writing)",
             "Listen to the passage and, in Pinyin or characters, write the name of each building on the map (a DLIFLC map with numbered buildings; audio and map are not included)."),
        card("Activity 3 (Reading, Listening and Speaking)",
             "Read the passage and complete the tasks. A. Using what you read, draw the bus route in your notebook and circle the buses David needs to take (a Beijing bus-route map around 天安门, 西单, 东单, 建国门, 王府井, 前门大街; the map is not included). B. Using the instructions from the passerby, how should David get to the American Embassy after leaving the bus? In your notebook, draw the route on the map (建国门站, 立交桥) and mark the approximate location of the embassy. Compare your work with your partner’s. The book prints the bus numbers 320 and 1 in digits; I spelled them out.",
             examples=S3),
        card("Activity 4 (Listening, Reading and Speaking)",
             "A. Listen to the dialog (Conversation 1). In your notebook, draw the route to the American embassy from where the speaker and the traffic police are, and mark the location of the embassy (audio and map not included). B. Pair up. Using your drawing, give your partner directions. Then compare your drawings. C. Read Conversation 2. Draw the route to the intended destination in your notebook and mark the destination on the map (the map shows 立交桥, 菜市场 and 农贸市场). B. Pair up and compare your drawings.",
             examples=S4),
        card("Activity 5 (Listening and Speaking)",
             "Conversation 1: A. Listen to the dialog and take notes on the route you hear. B. Pair up. Student 1, using your notes, convey the directions to your partner. Student 2, listen carefully for any differences from your route map. Then switch roles and repeat. Conversation 2: C. Listen to the conversation and discuss: 1. What did David ask at the airport information desk? 2. What information did David receive? 3. How did David get to the airport shuttle bus station? (Audio, not included.)"),
    ],
    exercises=[
        M("Which bus does David take first?", "Bus 320", ["Bus 418", "Bus 1", "Bus 208"], "坐三二零路公交车."),
        M("Where does he change buses?", "Tiananmen", ["Dongzhimen", "Xidan", "Wangfujing"], "在天安门换."),
        M("How many stops does he ride on the second bus?", "Five", ["Four", "Six", "Two"], "坐五站到建国门下车."),
        M("How far must he walk after getting off?", "More than twenty minutes", ["Two minutes", "Two hours", "Not at all"], "再走二十多分钟."),
        M("Which way does he walk along the road after crossing at the light?", "North", ["South", "East", "West"], "沿着那条路往北走."),
        M("Where does he turn right?", "At the second crossroads", ["At the first traffic light", "At the overpass", "At the flag"], "在第二个十字路口向右拐."),
        M("What helps him recognize the embassy?", "An American flag in front of the building", ["A red gate", "A statue", "A clock tower"], "大楼前有美国国旗."),
        M("What is opposite the farmers’ market?", "Dahua Travel Agency", ["The bank", "The vegetable market", "The overpass"], "农贸市场的对面就是大华旅行社."),
        M("What is next to the vegetable market?", "A bank", ["A school", "A cinema", "A post office"], "菜市场的旁边是个银行."),
        M("Which side must you catch the bus on?", "The other side of the road", ["Under the overpass", "At the bank", "Inside the market"], "您得到马路对面去坐车."),
        F("你从这儿过马___，到对面坐三二零路公交车。", "路", PART, "过马路: cross the road."),
        F("农贸市场的对___就是大华旅行社。", "面", PART, "对面: opposite."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context
Z1 = ("大家好，我叫在成。我现在在中国青岛。这里离韩国很近，从首尔坐飞机一个小时就到了。我现在在机场，我要去青岛市区。刚才我问怎么去市区，他们说我需要坐大巴。",
      "Part 1: Hello everyone, my name is Zaicheng. I am in Qingdao, China now. It is very close to Korea; from Seoul it takes one hour by plane. I am at the airport now and I want to go to downtown Qingdao. Just now I asked how to get to the city and they said I need to take the shuttle bus. (translation mine)")
Z2 = ("我坐上了大巴，窗外的景色很美。慢慢地我看见很多高楼，好像到了市区。我下了车，可是不知道这是什么地方。因为没有网络，所以我不能查地图问路。啊，马路对面就有一个公交车站，我去问问等车的人。",
      "Part 2: I got on the shuttle bus and the scenery outside the window was beautiful. Gradually I saw many tall buildings, as if I had reached the city. I got off, but I didn’t know where this was. Because there was no network, I couldn’t check the map to ask the way. Ah, there is a bus stop across the road; I’ll go and ask the people waiting for the bus. (translation mine)")
Z3 = ("我坐到山东路以后下了车，可是还没有找到我要去的酒店。我问了两三个人，谁都不知道西吴路在哪儿。我只好坐出租车。",
      "Part 3: After riding to Shandong Road I got off, but I still hadn’t found the hotel I was going to. I asked two or three people, and nobody knew where Xiwu Road was. I had no choice but to take a taxi. (translation mine)")
Z4 = ("我终于到了酒店。你们都看到我在中国没有网络，迷路的样子了。",
      "I finally reached the hotel. You have all seen how I got lost in China without a network. (the book’s closing line; the book’s credit line reads 宰成-米达: 一个韩国男生在中国迷路了, “a Korean boy gets lost in China”)")
L7 = lesson(
    "Lesson 22 Presentation 1 using Chinese in context: subway maps, Nanjing and Zaicheng in Qingdao",
    "北京地铁 · 金陵饭店 · 在成在青岛 · 没有网络 · 坐出租车",
    requires=[],
    cards=[
        card("Activity 1 and Activity 2 (Speaking and Listening)",
             "Activity 1: You are planning to visit several tourist attractions (yellow frames on the map) in Beijing from 人民大学 (with the person icon). Pair up and take turns giving directions on how to take the subway and transfer to an attraction without revealing your destination to your partner. Your partner will listen to your instructions and figure out your destination. Activity 2: Go to map.bjsubway.com, click on the two stations of your interest to set as 起点 and 终点 (zhōngdiǎn; destinations) and describe the route. A. 三号航站楼 to 中国美术馆. B. 人民大学 to 奥林匹克公园. C. Click on any two stations of interest and describe the route. (Maps and the website are not included.)"),
        card("Activity 3 (Speaking)",
             "You are in Nanjing and are staying at the Jinling Hotel. You want to travel to the places listed below from your hotel. Pair up. Work with your partner to choose five destinations you both want to visit and describe the route to each. Listen to each other to see whose description is clearer. Destinations: 工商银行, 胜利电影院, 老广东菜馆, 新街口百货商店, 大华电影院, 人民商场, 同庆楼菜馆, 动物商场, 延安影剧院. (The map is not included.)"),
        card("Activity 4 (Reading, Listening and Speaking)",
             "Read the short passages and listen to the conversations between Zaicheng and local Chinese people; then answer the questions. Part 1 questions (conversation with the ticket-booth clerk): 1. Where is he from? 2. Where does he want to go? 3. According to the clerk, what route should he take? 4. Where is the bus station? Part 2 questions (conversation with an old man): 1. How does Zaicheng know he is closer to downtown? 2. What is Zaicheng’s usual way to navigate? Why must he use the “old way”? 3. What is his alternate destination? 4. How will Zaicheng get to his destination (list at least three details)? Part 3 questions (taxi driver and police): 1. How will he get to the hotel from where he is? 2. Why don’t people know the street Zaicheng is looking for? (Audio, not included; the passages are:)",
             examples=[D(*Z1), D(*Z2), D(*Z3), D(*Z4)]),
    ],
    exercises=[
        M("Where is Zaicheng from?", "Korea (he flew from Seoul)", ["Japan", "Singapore", "Canada"], "从首尔坐飞机一个小时就到了."),
        M("Which Chinese city is he in?", "Qingdao", ["Nanjing", "Xi’an", "Shanghai"], "我现在在中国青岛."),
        M("What did they tell him to take to the city?", "The shuttle bus (大巴)", ["A taxi", "The subway", "A train"], "他们说我需要坐大巴."),
        M("Why can’t he check a map?", "He has no network", ["His phone is lost", "He can’t read maps", "The map is wrong"], "因为没有网络，所以我不能查地图问路."),
        M("Who does he decide to ask at the bus stop?", "The people waiting for the bus", ["The driver", "A policeman", "A shopkeeper"], "我去问问等车的人."),
        M("What does he do in the end to reach the hotel?", "Takes a taxi", ["Walks", "Takes the subway", "Calls a friend"], "我只好坐出租车."),
        M("What did nobody know?", "Where Xiwu Road is", ["Where the airport is", "Where the bus stop is", "Where Shandong Road is"], "谁都不知道西吴路在哪儿."),
        F("我坐上了大巴，窗外的景___很美。", "色", PART, "景色: scenery."),
        F("我下了车，可是不___道这是什么地方。", "知", PART, "不知道: don’t know."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 22 Presentation 1 vocabulary", "23 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book prints 号线 and 路 with (x) in front, as in 二号线 and 四一八路; the book’s glosses are kept as printed, including its entries for 乘 (“multiply”), 丢 (“throw”) and 民警 (“traffic police”; the book’s pinyin jǐngchá is a slip, the word is mínjǐng).", VOC1)

UNIT = unit("第二十二课 Presentation 1: 到大使馆怎么走, 还, 约数, 乘地铁和公交", [L1, L2, L3, L4, L5, L6, L7, L8])
