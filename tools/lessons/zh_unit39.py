"""Unit 39: Lesson 14 (Leisure Travel) Presentation 1 from the book's texts: the trip to Beihai Park dialog, the experience marker
过, the preposition 离, 从…到…, the skill-integration passages (Temple of Heaven, Old Summer Palace, Panjiayuan), the Beijing
transportation guide and the vocabulary list. Audio, pictures, maps and videos are not included; the book writes the numbers as
digits and they are spelled out here so that every spoken line is Chinese; answer keys the book does not print are mine."""
from zh_auto import *
from zh_l14_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("长大", 0, "zhang3"), ("称为", 1, "wei2"), ("半只", 1, "zhi1"), ("朝阳", 0, "chao2"), ("种有", 0, "zhong4"),
                          ("学生还可以", 2, "hai2"), ("起价为", 2, "wei2"), ("统一为", 2, "wei2"), ("成为", 1, "wei2"), ("作为", 1, "wei2"), ("休闲地从", 2, "de5"), ("方便地订", 2, "de5")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for k in ("得做", "得需", "得带", "得花", "得坐", "得先", "得去", "得买"):
        j = zh.find(k)
        while j >= 0:
            f[j] = "dei3"
            j = zh.find(k, j + 1)
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [("张英", "周末我想去北海公园玩玩，要不要一起去？", "This weekend I want to go to Beihai Park to have some fun. Do you want to go together?"),
      ("琳达", "好啊，来北京这么长时间，我还没去过北海呢。你打算怎么去？坐公共汽车还是骑自行车？", "Sure. I’ve been in Beijing for so long and still haven’t been to Beihai. How do you plan to go? Take the bus or ride a bike?"),
      ("张英", "坐公车或是骑车都太花时间。咱们打车去怎么样？", "Taking the bus or riding a bike both take too much time. How about taking a taxi?"),
      ("琳达", "这儿离北海公园挺远的，而且现在路上这么堵，打车有点儿贵。", "It’s quite far from here to Beihai Park, and with the road this jammed now, a taxi is a bit expensive."),
      ("张英", "那，你想怎么去？", "Then how do you want to go?"),
      ("琳达", "坐地铁吧，又快又便宜。从北海北站下车，然后走路到北海公园。", "Let’s take the subway, it’s both fast and cheap. Get off at Beihai North Station, then walk to Beihai Park."),
      ("张英", "走路啊？天气这么热，我可不想走。", "Walk? The weather is so hot, I really don’t want to walk."),
      ("琳达", "没关系的，从地铁站到北海公园走路只要五分钟，而且路两边都是树，在树下走很凉快的。", "It doesn’t matter. From the subway station to Beihai Park it only takes five minutes on foot, and there are trees on both sides of the road; walking under the trees is very cool."),
      ("张英", "真的？", "Really?"),
      ("琳达", "真的。你要是还觉得热，我请你吃冰淇淋。", "Really. If you still feel hot, I’ll treat you to ice cream."),
      ("张英", "好吧，就按你说的做。", "All right, let’s do as you say."),
      ("琳达", "到了公园，咱们可以在湖里划船，散步聊天，上山看风景。", "Once we get to the park, we can row a boat on the lake, stroll and chat, and go up the hill to see the scenery."),
      ("张英", "好主意！", "Good idea!")]
A1Q = "Listen to Presentation 1 once. A. Global listening: 1. What are the two speakers discussing? 2. What do the two speakers finally decide upon? B. Listen again for details: 1. Are both speakers familiar with the place they described? How do you know? 2. How can they get there? List the three different ways described. 3. What agreement did the speakers reach? 4. What can the speakers do at their destination? (Audio, not included. From the text: 1. Going to Beihai Park this weekend, and how to get there. 2. They decide to take the subway and walk the last part. 1. No, Linda hasn’t been; she says she hasn’t been to Beihai yet. 2. Bus, bicycle, taxi (and the subway they finally choose). 3. Zhang Ying will go as Linda suggests. 4. Row a boat on the lake, stroll and chat, go up the hill to see the scenery.)"
L1 = lesson(
    "Lesson 14 Presentation 1: going to Beihai Park",
    "第十四课 休闲旅游 · 坐公共汽车还是骑自行车？ · 坐地铁吧，又快又便宜",
    requires=[],
    cards=[
        card("Learning objectives and Getting Started",
             "Lesson 14 Leisure Travel. After this lesson you can compare different modes of transportation, discuss travel plans (destinations, travel times, modes of travel) and describe your travel experiences. You must master: the new words, the experience marker 过, the preposition 离, the construction 从…到…, 什么 + 吗, the rhetorical question 反问句, 多 in exclamatory sentences, 还是 for preference, the time-measurement complement 时量补语, the double 了 structure and compound directional verbs. Getting Started. Pair up and discuss: A. How do you usually get around in Monterey? B. How do you get to class each day? C. What modes of transportation do you use when you travel, and why?"),
        card("Presentation 1: 去北海公园",
             "The book prints the dialog in both simplified and traditional characters and shows photographs of the Beijing rail map, Tiananmen, Beihai and Wangfujing (not included). The note: 可. The adverb 可 is used to add emphasis to a verb; its function is similar to the adverb 真. (The book writes “5 分钟”; spelled out here.)",
             examples=dlg(P1)),
        card("Activity 1 (Listening and Speaking)", A1Q),
    ],
    exercises=[
        M("Where do Zhang Ying and Linda want to go?", "Beihai Park", ["The Great Wall", "Tiananmen", "The Summer Palace"], "周末我想去北海公园玩玩。"),
        M("Has Linda been to Beihai?", "No, not yet", ["Yes, twice", "Yes, last week", "She lives there"], "我还没去过北海呢。"),
        M("Why does Zhang Ying reject the bus and bike?", "They take too much time", ["They are too expensive", "There are none", "They are dangerous"], "坐公车或是骑车都太花时间。"),
        M("Why does Linda reject a taxi?", "It’s far, the road is jammed and a taxi is a bit expensive", ["It is too slow", "Taxis don’t go there", "She doesn’t like cars"], "离北海公园挺远的，路上这么堵，打车有点儿贵。"),
        M("What does Linda suggest?", "Take the subway and then walk", ["Take a taxi", "Ride a bike", "Stay home"], "坐地铁吧，又快又便宜。"),
        M("Where do they get off the subway?", "Beihai North Station", ["Tiananmen Station", "Wangfujing Station", "Xizhimen Station"], "从北海北站下车。"),
        M("How long does it take to walk from the station to the park?", "Five minutes", ["Fifty minutes", "One hour", "Two minutes"], "走路只要五分钟。"),
        M("What does Linda offer if Zhang Ying still feels hot?", "Ice cream", ["A drink", "A taxi", "A hat"], "我请你吃冰淇淋。"),
        M("What will they do in the park?", "Row a boat, stroll and chat, go up the hill to see the view", ["Swim", "See a movie", "Go shopping"], "划船，散步聊天，上山看风景。"),
        M("What does 可 do in 我可不想走?", "It adds emphasis, like 真", ["It negates the verb", "It means “can”", "It marks the past"], "可 adds emphasis."),
        M("What does 打车 mean?", "To take a taxi", ["To drive a car", "To hit a car", "To park"], "打车: take a cab."),
        M("What does 就按你说的做 mean?", "Let’s do as you say", ["I will not do it", "You do it", "Do it later"], "按: according to."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2 to 5
MODES = [("公共汽车", "bus"), ("公车", "bus"), ("地铁", "subway"), ("出租车", "taxi"), ("自行车", "bicycle"), ("火车", "train"), ("飞机", "airplane"), ("轮船", "ship"), ("摩托车", "motorbike"), ("校车", "school bus"), ("三轮车", "pedicab"), ("网约车", "ride-hailing car")]
A3 = [("我还没有去过上海呢。到中国这么久，我也想去！", "(1, B reply, mine) I haven’t been to Shanghai yet either. I’ve been in China so long; I want to go too!"),
      ("这儿离长城很远，坐公共汽车太花时间了。", "(2, A, mine) It is far from here to the Great Wall; the bus takes too much time."),
      ("从学校到公园走路只要十分钟，而且路上有很多树。", "(3, A, mine) From the school to the park it only takes ten minutes on foot, and there are many trees along the way."),
      ("在国家公园，咱们可以爬山、划船、野餐，还可以看日出。", "(4, A, mine) In the national park we can hike, row a boat, have a picnic, and also watch the sunrise."),
      ("坐地铁，又快又便宜。", "(5, A, mine) Take the subway; it’s both fast and cheap.")]
QA = [("1", "从学校到香山有多远？", "c", "我们大约有二十公里。", "How far is it from the school to the Fragrant Hills? About 20 km."),
      ("2", "春节你有什么打算？", "d", "我计划去外地看看。", "What are your plans for Spring Festival? I plan to see other places."),
      ("3", "你们是怎么去香山的？", "h", "我们是坐校车去的。", "How did you get to the Fragrant Hills? We went by school bus."),
      ("4", "你们在山上看到了什么？", "b", "我们看到了城外的景色。", "What did you see on the hill? We saw the scenery outside the city."),
      ("5", "你们看了哪些名胜？", "g", "我们游览了香山附近的名胜。", "Which sights did you visit? We toured the sights near the Fragrant Hills."),
      ("6", "你们是几点从学校出发的？", "a", "我们七点就从学校出发了。", "At what time did you leave school? We left school at seven."),
      ("7", "你们是几点到的香山？", "f", "我们九点左右到了香山。", "When did you arrive? We arrived around nine."),
      ("8", "你喜欢坐飞机旅行吗？", "e", "喜欢，坐飞机又快又舒服。", "Do you like traveling by plane? Yes, it’s fast and comfortable.")]
DLG5 = [("甲", "你们是怎么去香山的？", "How did you get to the Fragrant Hills?"), ("乙", "我们是坐校车去的。", "We went by school bus."), ("甲", "你们是几点从学校出发的？", "At what time did you leave school?"), ("乙", "我们七点就从学校出发了。", "We left school at seven."),
        ("甲", "你们是几点到的香山？", "When did you arrive?"), ("乙", "我们九点左右到了香山。", "We arrived around nine."), ("甲", "你们在山上看到了什么？", "What did you see on the hill?"), ("乙", "我们看到了城外的景色。", "We saw the scenery outside the city."),
        ("甲", "你们看了哪些名胜？", "Which sights did you see?"), ("乙", "我们游览了香山附近的名胜。", "We toured the sights near the Fragrant Hills."), ("甲", "春节你有什么打算？", "What are your plans for Spring Festival?"), ("乙", "我计划去外地看看。", "I plan to see other places."),
        ("甲", "你喜欢坐飞机旅行吗？", "Do you like traveling by plane?"), ("乙", "喜欢，坐飞机又快又舒服。", "Yes, it’s fast and comfortable.")]
L2 = lesson(
    "Lesson 14 Presentation 1 activities: modes of transportation",
    "公共汽车 · 地铁 · 打车 · 我们是坐校车去的",
    requires=[],
    cards=[
        card("Activity 2 (Writing and Speaking): vocabulary mind map",
             "A. Use the diagram (“Modes of Transportation”, with photographs) to write the modes of transportation in Chinese characters; add as many as you can. B. Pair up and share your work. C. Discuss the advantages and disadvantages of each mode. The book leaves the map blank; my list:",
             examples=[D(z, e) for z, e in MODES]),
        card("Activity 3 (Reading, Writing, and Speaking)",
             "A. Complete each dialog with your own words, in Chinese. B. Pair up and share. 1. A: 到中国这么久，我还没有去过上海呢？ B: ___. 2. A: ___. B: 咱们打车去怎么样？ 3. A: 从 ___ 到 ___，走路只要 ___，而且 ___。 B: 真的吗？那我们周末就去吧。 4. A: 在国家公园，咱们可以 ___、___、___，还可以 ___。 B: 这么多活动，可以玩三天啦。 5. A: 坐 ___，又 ___ 又 ___。 B: 比骑自行车好多啦。 My completions (the book leaves them to you):",
             examples=[D(z, e) for z, e in A3]),
        card("Activity 4 (Listening, Speaking and Reading)",
             "Listen to the dialogs and answer the questions; pair up and share. Dialog 1: 1. What plans did the two speakers make for the weekend? Place a check mark above each image that shows one of their activities (three photographs). 2. Place a check mark above each mode of transportation the speakers chose (three photographs). 3. What mode of transportation will the speakers use, and why? 4. Where and when will they meet? Dialog 2: 1. What will the second speaker do over the weekend? 2. What is the first speaker’s plan? 3. What mode of transportation will the first speaker use? 4. What does the second speaker want to learn? 5. List three details the second speaker has planned for the weekend. 6. List three activities the first speaker has planned. (Audio and pictures, not included.)"),
        card("Activity 5 (Reading, Speaking, Listening, and Writing)",
             "A. Match each question with its likely answer and share your answers with a classmate. The questions: 1. 从学校到香山有多远？ 2. 春节你有什么打算？ 3. 你们是怎么去香山的？ 4. 你们在山上看到了什么？ 5. 你们看了哪些名胜？ 6. 你们是几点从学校出发的？ 7. 你们是几点到的香山？ 8. 你喜欢坐飞机旅行吗？ The answers: a. 我们七点就从学校出发了。 b. 我们看到了城外的景色。 c. 大约有 20 公里。 d. 我计划去外地看看。 e. 喜欢，坐飞机又快又舒服。 f. 我们九点左右到了香山。 g. 我们游览了香山附近的名胜。 h. 我们是坐校车去的。 My matching (mine): 1-c, 2-d, 3-h, 4-b, 5-g, 6-a, 7-f, 8-e. B. Put the sentences into a logical order and create a dialog with your partner. My dialog (mine; the answer c is shown here as 二十公里):",
             examples=dlg(DLG5)),
    ],
    exercises=[
        M("Match: 你们是怎么去香山的？", "我们是坐校车去的。", ["我们七点就出发了。", "大约有二十公里。", "我计划去外地看看。"], "3→h."),
        M("Match: 从学校到香山有多远？", "大约有二十公里。", ["我们是坐校车去的。", "我们九点左右到了。", "喜欢，坐飞机又快又舒服。"], "1→c."),
        M("Match: 春节你有什么打算？", "我计划去外地看看。", ["我们七点就出发了。", "我们看到了城外的景色。", "我们游览了名胜。"], "2→d."),
        M("Match: 你们在山上看到了什么？", "我们看到了城外的景色。", ["我们九点左右到了香山。", "我们是坐校车去的。", "大约有二十公里。"], "4→b."),
        M("Match: 你们是几点到的香山？", "我们九点左右到了香山。", ["我们七点就出发了。", "我计划去外地看看。", "我们是坐校车去的。"], "7→f."),
        M("What does 名胜 refer to?", "Famous scenic spots", ["Famous people", "Famous foods", "Famous stores"], "游览名胜."),
        M("What does 出发 mean?", "To set out; to depart", ["To arrive", "To return", "To rest"], "出发: depart."),
        M("What does 计划 mean?", "To plan", ["To cancel", "To finish", "To forget"], "计划: plan."),
        F("坐飞机又快又___服。", "舒", PART, "舒服: comfortable."),
        F("我们七点就从学校出___了。", "发", PART, "出发: depart."),
    ],
)

# ------------------------------------------------------------------ 3. 过
GU = [("我去过日本。", "I have been to Japan."), ("来国防语言学院以前，大卫学过西班牙文。", "Before coming to the Defense Language Institute, David had studied Spanish."), ("我没有去过华盛顿。", "I haven’t been to Washington. (没（有） is optional.)"), ("我奶奶没坐过飞机。", "My grandmother has never taken a plane."),
      ("你去过中国吗？", "Have you been to China?"), ("我去过北京，也去过上海。", "I’ve been to Beijing and also to Shanghai."), ("你父母见过你的男朋友没有？", "Have your parents met your boyfriend?")]
GU2 = [("你去过长城没有？", "Have you been to the Great Wall? (experience, 过)"), ("你今天去了长城没有？", "Did you go to the Great Wall today? (a specific scheduled event, 了)"), ("我去过纽约。", "I have been to New York. (experience, 过)"), ("去年夏天我去了纽约。", "Last summer I went to New York. (a specific time, 了)")]
QG = [("你去过中国吗？", "Have you ever been to China? (mine)"), ("你吃过北京烤鸭吗？", "Have you ever eaten Peking duck? (mine)"), ("你学过哪些外语？", "Which foreign languages have you studied? (mine)")]
L3 = lesson(
    "Lesson 14 Presentation 1 grammar: the experience marker 过",
    "我还没去过北海 · 我奶奶没坐过飞机 · 去过长城没有？",
    requires=[],
    cards=[
        card("The Experience Marker 过",
             "In Chinese, when the aspect particle 过 is used immediately after a verb, it indicates a past experience. It is like the meaning of “ever” in English. When 过 is used as an experience marker, it follows the verb and precedes the object if there is one. Its negative is formed with 没有 and its interrogative forms include both the 吗-question and the affirmative-negative patterns. Positive: Subject + Verb + 过 + Object. Negative: Subject + 没(有) + Verb + 过 + Object. Interrogative: Subject + Verb + 过 + Object + 吗？ / Subject + Verb + 过 + Object + 没有？ Example from the dialog: 来北京这么长时间，我还没去过北海呢。 (I have been in Beijing for so long; however, I haven’t been to Beihai Park yet.)",
             examples=[D(z, e) for z, e in GU]),
        card("Experience marker 过 versus past tense 了",
             "The “Verb + 过 + Object” pattern emphasizes that an event has been experienced at least once in the past. The “Verb + 了 + Object” pattern indicates that a specific action has taken place with reference to a specific point in time. If you ask a tourist if they have been to the Great Wall since they came to China, you use 过. If you want to ask a tourist if they went to the Great Wall as scheduled, you use 了.",
             examples=[D(z, e) for z, e in GU2]),
        card("Activities 1 to 3",
             "Activity 1 (Writing, Speaking and Listening). Pair up. A. Write three questions using 过. B. Take turns asking your partner about past experiences using the questions you wrote. C. Each student asks the teacher one question about his/her past experiences. My three sample questions are below. Activity 2 (Listening and Speaking). Listen to the passage and answer in English: 1. What cities in China has the speaker been to? 2. Where and for how long did the speaker study Chinese? 3. What is the speaker’s plan for this summer? (Audio, not included.) Activity 3 (Speaking, Listening, Writing and Reading). Interview a classmate: one student interviews about foreign language learning experiences (table: Name; Learned foreign languages before?; If yes, which language(s)?; If not, any plans to learn?) and the other about foreign travel experiences (table: Name; Has traveled abroad before?; If yes, which country/city?; If not, any travel plans?), using 过 as needed. B. Exchange the information you gathered. C. Talk with the other pairs to complete: 1. 我们班一共有 ___ 位同学学过外语，他们学过的外语有：___。 2. 我们班一共有 ___ 位同学去过外国，他们去过的国家有：___。",
             examples=[D(z, e) for z, e in QG]),
    ],
    exercises=[
        M("What does 过 after a verb indicate?", "A past experience (“ever”)", ["A future plan", "A command", "A continuing action"], "Experience marker."),
        M("How do you negate an experience with 过?", "没(有) + verb + 过", ["不 + verb + 过", "verb + 过 + 不", "别 + verb + 过"], "我没去过华盛顿."),
        M("Where does 过 go relative to the object?", "After the verb, before the object", ["After the object", "Before the verb", "At the end of the sentence"], "Verb + 过 + Object."),
        M("What does 我奶奶没坐过飞机 mean?", "My grandmother has never taken a plane", ["My grandmother is on a plane", "My grandmother doesn’t like planes", "My grandmother took a plane"], "没坐过."),
        M("Which asks about a specific scheduled visit today?", "你今天去了长城没有？", ["你去过长城没有？", "你去过长城吗？", "你想去长城吗？"], "了 for a specific time."),
        M("Which asks whether you have ever been to the Great Wall?", "你去过长城没有？", ["你今天去了长城没有？", "你明天去长城吗？", "你在长城吗？"], "过 for experience."),
        M("What does 去年夏天我去了纽约 mean?", "Last summer I went to New York", ["I have been to New York", "I will go to New York", "I want to go to New York"], "了 with a specific time."),
        M("What does 你父母见过你的男朋友没有？ ask?", "Have your parents met your boyfriend?", ["Do your parents like him?", "Is your boyfriend here?", "Where is your boyfriend?"], "见过…没有."),
        F("我去___日本。", "过", PART, "去过: have been to."),
        F("我奶奶没坐过飞___。", "机", PART, "飞机."),
        F("你父母见过你的男朋友没___？", "有", PART, "没有: A-not-A question."),
    ],
)

# ------------------------------------------------------------------ 4. 离
LI = [("你们家离学校有多远？可以走路去吗？", "How far is your home from school? Can you go on foot?"), ("我们家离学校不远，走路五分钟就到了。", "Our home is not far from school; it takes five minutes on foot."), ("蒙特雷离旧金山很远，开车需要两个半小时。", "Monterey is far from San Francisco; it takes two and a half hours by car."), ("地铁站离公园大门很近，出了地铁站可以看到公园在马路对面。", "The subway station is very close to the park gate; after leaving the station you can see the park across the road."),
      ("现在离春节很近了，所以商店里到处都是人。", "It is very close to Spring Festival now, so the stores are full of people."), ("飞机离起飞不到十分钟了，不能打电话了。", "The plane is less than ten minutes from takeoff; you can’t make phone calls now."), ("现在离考试还有两天，大家都在忙着复习。", "Now there are two more days until the exam; everybody is busy reviewing.")]
LIPAIR = [("学校离图书馆很近。", "(mine) The school is very close to the library."), ("宿舍离海边不远，走路十分钟就到了。", "(mine) The dorm is not far from the beach; it takes ten minutes on foot."), ("现在离春节还有两个月。", "(mine) Now there are two more months until Spring Festival."), ("旧金山离纽约很远，坐飞机要五个多小时。", "(mine) San Francisco is far from New York; it takes over five hours by plane."),
          ("我家离公园不远。", "(mine) My home is not far from the park."), ("公共汽车站离市中心有三公里。", "(mine) The bus stop is three kilometers from downtown."), ("机场离我的公寓不太远，坐车半个小时。", "(mine) The airport is not too far from my apartment; it is half an hour by car."), ("中国饭馆离我的公寓很近。", "(mine) The Chinese restaurant is very close to my apartment.")]
L4 = lesson(
    "Lesson 14 Presentation 1 grammar: the preposition 离",
    "这儿离北海公园挺远的 · 离春节很近了 · 离考试还有两天",
    requires=[],
    cards=[
        card("The preposition 离",
             "The preposition 离 in Chinese indicates the temporal or spatial distance between two points. It is like “from” or “away” in English. Structurally, the two points have to be nouns of place or time in a sentence, and the main predicates often involve an adjective of distance, namely 远 (far) or 近 (near), or the distance or time spent. Patterns: A + 离 + B + 很远/很近/不远/不近…; A + 离 + B + (有/不到) distance; A + 离 + B + (有/不到) time spent. Example from the dialog: 这儿离北海公园挺远的。 (It is pretty far from here to Beihai Park.)",
             examples=[D(z, e) for z, e in LI]),
        card("Activity 5 (Reading, Speaking and Listening)",
             "Work in pairs and practice using 离 with the following words. Each time one student selects one word from the blue card and the other one a word from the green card. Create sentences together using the required pattern and add more information if you can. Blue card: 1. 学校 2. 宿舍 3. 现在 4. 旧金山 5. 我家 6. 公共汽车站 7. 机场 8. 中国饭馆. Green card: a. 电影院 b. 春节 c. 海边 d. 公园 e. 纽约 f. 市中心 g. 图书馆 h. 我的公寓. The book leaves the sentences to you; my sample sentence for each blue-card word:",
             examples=[D(z, e) for z, e in LIPAIR]),
        card("Activity 6 (Speaking, Writing and Listening)",
             "A Chinese student is going to start their study at the Middlebury Institute of International Studies at Monterey (MIIS) and would like to know about the school’s location and how far or close it is from local facilities, shopping malls, recreational places and other cities. Create a short video with your phone and provide the information. Your video will be posted on a Chinese social media platform. A. Work in pairs to find the distance from MIIS to all the related places, list the places you would include, and take turns practicing sentences with the 离…很远/很近 pattern. B. Record your video, with you and your partner taking turns describing the location of MIIS and the distances. C. Share your video with the class. (Video, not included.)"),
    ],
    exercises=[
        M("What does 离 express?", "Distance in space or time between two points", ["Direction", "Cause", "Comparison"], "离: from/away."),
        M("Which is correct?", "我家离学校很近。", ["我家从学校很近。", "我家离很近学校。", "离我家学校很近。"], "A + 离 + B + 很近."),
        M("What does 蒙特雷离旧金山很远 mean?", "Monterey is far from San Francisco", ["Monterey is near San Francisco", "Monterey is in San Francisco", "I went from Monterey"], "很远: far."),
        M("What does 现在离春节很近了 mean?", "It is very close to Spring Festival now", ["Spring Festival is over", "It is far from Spring Festival", "I like Spring Festival"], "离 with time."),
        M("What does 飞机离起飞不到十分钟了 mean?", "The plane is less than ten minutes from takeoff", ["The plane took off ten minutes ago", "The plane is ten minutes late", "The plane flies ten minutes"], "不到: less than."),
        M("What does 现在离考试还有两天 mean?", "There are two days left until the exam", ["The exam is over", "The exam is in two weeks", "I passed the exam"], "离…还有."),
        M("What can follow A + 离 + B?", "很远, 很近, or a distance or time spent", ["Only a verb", "Only a noun", "Only 吗"], "Predicates."),
        F("这儿___北海公园挺远的。", "离", PART, "离: from."),
        F("我们家离学校不___，走路五分钟就到了。", "远", PART, "不远: not far."),
        F("地铁站离公园大门很___。", "近", PART, "很近: very close."),
    ],
)

# ------------------------------------------------------------------ 5. 从…到…
CD = [("从我的公寓到学校大门，走路十分钟就到了。", "From my apartment to the school gate it takes ten minutes on foot."), ("请问，从这儿到购物中心有多远？", "Excuse me, how far is it from here to the shopping center?"), ("从第一课到第五课，我们都没有语法问题。", "From Lesson 1 to Lesson 5, we had no grammar problems."), ("你们每天从几点到几点上课？", "From what time to what time do you have class every day?"), ("从上海到北京坐火车得需要几个小时？", "How many hours does it take to go from Shanghai to Beijing by train?")]
CD2 = [("从学校到银行有两英里。", "From the school to the bank is two miles. (从…到…)"), ("学校离银行有两英里。", "The school is two miles from the bank. (离)"), ("从圣诞节到春节还有一个多月。", "From Christmas to Spring Festival is still more than a month. (从…到…)"), ("圣诞节离春节还有一个多月。", "Christmas is more than a month from Spring Festival. (离)")]
CD7 = [("我们从学校走到海边，走了半个小时。", "(1, mine) We walked from the school to the beach, half an hour."), ("从小学到高中，我的成绩一直很好。", "(2, mine) From elementary school to high school my grades were always good."), ("从晚上七点到十点，我得做作业。", "(3, mine) From seven to ten in the evening, I have to do homework."), ("从学校到市中心，坐地铁只要二十分钟。", "(4, mine) From school to downtown it takes only twenty minutes by subway."),
       ("从北京烤鸭到炒饭，每个菜都不错。", "(5, mine) From Peking duck to fried rice, every dish is good."), ("从蒙特雷到旧金山开车，只需要三个小时。", "(6, mine) Driving from Monterey to San Francisco only takes three hours.")]
PLAN8 = ("这个周末我打算去海边。我家离海边不远，走路十五分钟就到了。星期六早上，从九点到十一点，我要去图书馆做作业。下午我跟朋友一起去海边散步。从海边到中国饭馆走路只要五分钟，我们打算在那儿吃晚饭。星期天我想从早上十点睡到十二点。")
PLAN8E = "This weekend I plan to go to the beach. My home is not far from the beach; it takes fifteen minutes on foot. Saturday morning, from nine to eleven, I will go to the library to do homework. In the afternoon I will go for a walk at the beach with friends. From the beach to the Chinese restaurant it is only five minutes on foot; we plan to eat dinner there. On Sunday I want to sleep from ten to twelve. (my sample, mine)"
L5 = lesson(
    "Lesson 14 Presentation 1 grammar: 从…到…",
    "从地铁站到北海公园走路只要五分钟 · 从 versus 离",
    requires=[],
    cards=[
        card("Prepositional Construction 从…到…",
             "In Chinese, the construction 从…到… indicates “from one point to another”, either temporally or spatially. Similar to 离, the two locations must be nouns of place or time. The preposition 从 indicates the starting location or time. Patterns: 从 point A 到 point B + ADJ/V; 从 time A 到 time B + ADJ/V. Example from the dialog: 从地铁站到北海公园走路只要五分钟。 (It only takes five minutes to walk from the subway station to Beihai Park.)",
             examples=[D(z, e) for z, e in CD]),
        card("The difference between 从 and 离",
             "Note the difference between 从 and 离. 从…到…: 从学校到银行有两英里。 离: 学校离银行有两英里。 从…到…: 从圣诞节 (shèng dàn jié) 到春节还有一个多月。 离: 圣诞节离春节还有一个多月。",
             examples=[D(z, e) for z, e in CD2]),
        card("Activities 7 and 8",
             "Activity 7 (Writing and Speaking). Complete the sentences using 从…到… and share with a classmate: 1. 上个周末，我和几个朋友一起去海边散步。我们 ___。 2. 以前我的学习很好，___。 3. ___，我得做作业。 4. 现在在北京坐车很方便，___。 5. 这家中国饭馆的菜很好吃，___。 6. ___，只需要三个小时。 My completions (the book leaves them to you; the full sentences are shown):",
             examples=[D(z, e) for z, e in CD7]),
        card("Activity 8: Weekend plans",
             "Talk about your plans for this weekend using 从…到… and 离. A. Think about where you are going to go and what you are going to do, and make notes. B. Create a short paragraph with six to eight sentences describing your plans using 从…到… and 离. Share with a classmate. My sample paragraph (mine):",
             examples=[D(PLAN8, PLAN8E)]),
    ],
    exercises=[
        M("What does 从…到… express?", "From one point to another, in space or time", ["Because…so…", "If…then…", "Not only…but also…"], "从 A 到 B."),
        M("Which is correct?", "从学校到银行有两英里。", ["从学校银行有两英里。", "到学校从银行有两英里。", "学校从银行有两英里。"], "从…到…"),
        M("Which is the 离 version of 从学校到银行有两英里?", "学校离银行有两英里。", ["学校从银行有两英里。", "离学校银行有两英里。", "学校到银行有两英里。"], "离 pattern."),
        M("What does 你们每天从几点到几点上课？ ask?", "From what time to what time class is each day", ["Where class is", "Who teaches", "How many classes there are"], "从几点到几点."),
        M("What does 从上海到北京坐火车得需要几个小时？ ask?", "How many hours it takes by train from Shanghai to Beijing", ["How far Shanghai is", "Which train to take", "How much the train ticket costs"], "得需要: must take."),
        M("What does 从第一课到第五课，我们都没有语法问题 mean?", "From Lesson 1 to 5 we had no grammar problems", ["Lesson 5 is hard", "We skipped Lesson 3", "We have a grammar test"], "从…到… with lessons."),
        M("Which sentence uses 从…到… correctly?", "从我的公寓到学校大门，走路十分钟就到了。", ["从我的公寓学校大门，走路十分钟。", "我的公寓从学校到大门。", "走路从十分钟到学校。"], "从 A 到 B + V."),
        F("___地铁站到北海公园走路只要五分钟。", "从", PART, "从: from."),
        F("从地铁站___北海公园走路只要五分钟。", "到", PART, "到: to."),
        F("你们每天从几点到几点上___？", "课", PART, "上课: attend class."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
TF = [("王明打算五月二号出去玩。", "Wang Ming plans to go out on May 2. (the book prints 五月 2 号 with the digit 2)"), ("大卫在北京一直忙着学习，所以没有好好玩过。", "David has been busy studying in Beijing, so he hasn’t had a real good time."), ("王明想去故宫和天安门广场，可是大卫想去王府井。", "Wang Ming wants to go to the Forbidden City and Tiananmen Square, but David wants to go to Wangfujing."), ("在北京打车比坐公交车快。", "In Beijing taking a taxi is faster than taking the bus."),
      ("坐公交车可以看风景和街道，还不堵车。", "On the bus you can see scenery and streets and there are no traffic jams."), ("王明和大卫可以坐二十三路公共汽车，坐五站下车。", "Wang Ming and David can take bus 23 and get off after five stops."), ("从天安门广场，王明和大卫得坐地铁去故宫。", "From Tiananmen Square, Wang Ming and David have to take the subway to the Forbidden City.")]
TT = ("北京的天坛公园离市中心三公里，公园比较近也比较大，而且还可以坐地铁直达它的东门。从地铁二号线出发，然后转四号线就可直达“天坛公园东门”站。北京地铁怎么坐都是二元。要是你买一张交通卡还能打四折。如果你选择乘坐公交车，你可以看到长安街道路两边的大楼和树木。十五路公交车总站在天桥商场，下车后往东走就是天坛公园的西门。"
      "天坛公园非常漂亮，很适合散步和拍照。天坛的颜色特别美：蓝色、绿色的屋顶，红色的墙，白色的栏杆，还有金色的内墙。阳光下这些多彩的颜色真是太美了。因为风景很好，所以拍出来的照片也都很美。"
      "天坛东门的对面是一家烤鸭店，很多人去吃，常常需要等位子和桌子。这儿的北京烤鸭，很便宜而且味道也不错，半只鸭子才三十九元，还有一个汤，比别的地方多了一道菜。吃完饭以后，你还可以去附近的咖啡馆喝咖啡，或是去茶馆喝茶。")
TT_E = ("The Temple of Heaven Park in Beijing is three kilometers from downtown. The park is fairly close and fairly big, and you can take the subway directly to its east gate. Start from subway Line 2 and then transfer to Line 4 to go directly to “Temple of Heaven East Gate” station. Any subway ride in Beijing costs two yuan. If you buy a transportation card you also get 40% off (the book’s “打4折”, literally four-tenths price). If you choose the bus, you can see the buildings and trees on both sides of Chang’an Avenue. The terminus of bus 15 is at Tianqiao Shopping Mall; after getting off, walk east and you reach the west gate of the park. The Temple of Heaven Park is very beautiful and well suited for strolling and taking pictures. Its colors are especially beautiful: blue and green roofs, red walls, white railings, and golden inner walls. Under the sun these colorful colors are really lovely. Because the scenery is good, the photos you take are all beautiful. Opposite the east gate is a roast duck restaurant; many people eat there and often need to wait for a seat or table. The Peking duck here is cheap and tastes good: half a duck is only thirty-nine yuan, and there is a soup too, one more dish than elsewhere. After eating you can go to a nearby café for coffee or to a teahouse for tea.")
YM = ("北京的圆明园被称为“万园之园”。园内水面上种有大片的荷花，夏天的时候，荷花开放，整个园内有看不完的美景。划着游船游玩圆明园也是一种不错的休闲。春秋是游玩圆明园最好的季节，北京的春秋不冷不热，气候适中。暑假的时候，学生很多，天气也比较热。"
      "你可以先坐地铁二号线到西直门站，然后换地铁十三号线到“五道口”站，再打车到圆明园。打车只需要十元左右。圆明园的门票只要十元，而且学生还可以半价。"
      "从圆明园东门出来，往前走就可以看到清华大学的西门，因为学校很大，可以选择坐校内车看一下校园，坐校内车得花半个小时左右。你也可以租个自行车，花一个小时骑车逛一次清华园。租自行车每个小时十元。另外，你得带上身份证，在学校大门登记后才可以进入。"
      "从清华大学出来以后，你可以坐地铁去王府井购物、吃饭、逛街。晚上还可以逛夜市，去酒吧喝酒。")
YM_E = ("Beijing’s Old Summer Palace (Yuanmingyuan) is called the “Garden of Gardens”. Large areas of lotus are planted on the water in the garden; in summer when the lotus flowers bloom, there is endless beautiful scenery throughout the garden. Paddling a pleasure boat around the Old Summer Palace is also a nice way to relax. Spring and autumn are the best seasons to visit; Beijing’s spring and autumn are neither cold nor hot, with a moderate climate. In the summer vacation there are many students and the weather is also rather hot. You can first take subway Line 2 to Xizhimen, then change to Line 13 to “Wudaokou” station, then take a taxi to the Old Summer Palace. A taxi only costs about ten yuan. Admission is only ten yuan, and students get half price. Coming out of the east gate, walk straight ahead and you will see the west gate of Tsinghua University. Because the school is big, you can choose to take the on-campus bus to look at the campus, which takes about half an hour; you can also rent a bicycle and spend an hour touring Tsinghua Garden. Bicycle rental is ten yuan an hour. In addition, you must bring your ID card and register at the school gate before you can enter. After leaving Tsinghua, you can take the subway to Wangfujing for shopping, eating and strolling. At night you can also stroll the night market and have a drink at a bar.")
PJY = ("潘家园旧货市场规模很大，经营各种文物书画、文房四宝、民族特色产品、瓷器及木器家具等，共有三千多摊位。全国各个省市的商家都在此设摊经营，吸引着大批中外游客。地址：朝阳区东三环潘家园华威里十八号。交通：乘三十四、六百七十四、八百零二路公交车潘家园桥西站下。")
PJY_E = ("Panjiayuan Antique Market is very large, dealing in all kinds of cultural relics, calligraphy and paintings, the four treasures of the study, ethnic specialty products, porcelain and wooden furniture, with over three thousand stalls. Merchants from every province and city in the country set up stalls here, attracting large numbers of Chinese and foreign tourists. Address: No. 18 Huaweili, Panjiayuan, East Third Ring Road, Chaoyang District. Transportation: take bus 34, 674 or 802 and get off at Panjiayuan Bridge West stop.")
SM_TT = "天坛公园离市中心不远，可以坐地铁直达，风景很美，适合散步和拍照。门对面的烤鸭店又便宜又好吃。我推荐去天坛公园。"
SM_YM = "圆明园被称为“万园之园”，春秋最适合去，可以划船看荷花。从圆明园可以走到清华大学，再坐地铁去王府井。我推荐去圆明园。"
L6 = lesson(
    "Lesson 14 Presentation 1: skill integration",
    "天坛公园 · 圆明园 · 潘家园旧货市场",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking, Writing and Reading)",
             "Photos: Beijing streets, the Forbidden City, Tiananmen Square, Wangfujing Street. A. Listen to the dialog and mark each statement as True or False (audio, not included, so the key is not given here). B. Pair up, share your work and explain your answers. C. Read the script (the script is not printed in the student version). The seven statements:",
             examples=[D(z, e) for z, e in TF]),
        card("Activity 2 (Listening, Speaking, Writing and Reading)",
             "A. Listen to the dialog and identify the topic of the conversation. B. Listen again and write the essential elements of information (EEIs) in the table: When, Where, Who, What, How. C. Listen once more and answer: 1. Has the first speaker been to the place described by the second speaker? 2. Which route of travel did the second speaker recommend? 3. What could the first speaker and his friends do at the recommended location? List at least two details. 4. How can they get to the second place described in the dialog? D. Share your answers with your partner, then read the script with the class. (Audio, not included.)"),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. You and your friend are making plans for the coming weekend. The descriptions you found on a travel website of two historic places are below. You read one article and your friend reads the other; each of you writes a summary of the location, including why you would visit it and whether you would recommend it. B. Work in pairs and recite your summaries aloud in Chinese. C. Decide where you will go over the weekend. The book prints numbers as digits (3, 2, 4, 15, 39, 10, 13, 2 and so on); they are spelled out here. The book’s boxes for the summaries are blank; my short summaries follow the passages. 天坛公园:",
             examples=[D(TT, TT_E), D(SM_TT, "Summary (mine): The Temple of Heaven Park is not far from downtown, you can take the subway directly, the scenery is beautiful, and it suits strolling and photos. The roast duck restaurant across the gate is cheap and delicious. I recommend going to the Temple of Heaven Park.")]),
        card("圆明园",
             "Summary box: Reasons to Visit and Recommendations (mine below).",
             examples=[D(YM, YM_E), D(SM_YM, "Summary (mine): The Old Summer Palace is called the “Garden of Gardens”; spring and autumn are best, you can paddle a boat and see lotus. From it you can walk to Tsinghua University and then take the subway to Wangfujing. I recommend going to the Old Summer Palace.")]),
        card("Activity 4 (Reading, Writing, Speaking and Listening)",
             "A. Pair up. Read the following advertisement and answer the questions; share your answers. Questions: 1. Who would be interested in this advertisement? 2. What can you buy at this place? 3. How do you get to this location? (Mine: 1. Tourists and people who like antiques, cultural relics, calligraphy and paintings, porcelain or furniture. 2. Cultural relics, calligraphy and paintings, the four treasures of the study, ethnic specialty products, porcelain, wooden furniture. 3. Take bus 34, 674 or 802 to Panjiayuan Bridge West.) B. Find three new words and learn what they mean; write your three words and their English meanings, then share them in groups of three.",
             examples=[D(PJY, PJY_E)]),
    ],
    exercises=[
        M("How far is the Temple of Heaven Park from downtown?", "Three kilometers", ["Thirty kilometers", "Three hundred meters", "Thirteen kilometers"], "离市中心三公里。"),
        M("How do you reach the park by subway?", "Line 2, then transfer to Line 4 to the East Gate station", ["Line 1 to Tiananmen", "Line 13 to Wudaokou", "Line 8 to the Olympic Center"], "地铁二号线…转四号线."),
        M("How much is a subway ride in Beijing?", "Two yuan, whatever the distance", ["Ten yuan", "One yuan by distance", "Free"], "怎么坐都是二元。"),
        M("What discount does a transportation card give?", "Forty percent off (打四折 in the book)", ["Half price", "Free rides", "No discount"], "能打四折."),
        M("What colors are mentioned at the Temple of Heaven?", "Blue and green roofs, red walls, white railings, golden inner walls", ["Only red", "Only gold", "Black walls"], "颜色特别美."),
        M("How much is half a roast duck near the east gate?", "Thirty-nine yuan, with a soup", ["Ninety yuan", "Nineteen yuan", "Free"], "半只鸭子才三十九元，还有一个汤。"),
        M("Why is the Old Summer Palace called 万园之园?", "It is known as the “Garden of Gardens”", ["It has ten thousand trees", "It has ten thousand visitors", "It is ten thousand years old"], "被称为“万园之园”。"),
        M("When is the best time to visit the Old Summer Palace?", "Spring and autumn", ["Summer", "Winter", "Only at night"], "春秋是游玩圆明园最好的季节。"),
        M("How much is admission to the Old Summer Palace?", "Ten yuan; students pay half", ["Free", "One hundred yuan", "Twenty yuan for everyone"], "门票只要十元，学生半价。"),
        M("What must you bring to enter Tsinghua University?", "Your ID card, and register at the gate", ["A student visa", "A ticket", "A bicycle"], "你得带上身份证，在学校大门登记。"),
        M("What does the Panjiayuan Antique Market sell?", "Cultural relics, calligraphy and paintings, porcelain, furniture", ["Fresh fruit", "Phones", "Clothes only"], "经营各种文物书画…"),
        M("How many stalls does Panjiayuan have?", "More than three thousand", ["Thirty", "Three hundred", "Thirteen"], "共有三千多摊位。"),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context: transportation guide
TX = ("白天，五点到二十三点，起价为三公里十元，超过三公里后，每公里二元；夜间，二十三点到五点，起价为三公里十一元，超过三公里后，每公里二点四元。过路过桥费乘客支付。北京的黑出租很多，不要坐这样的出租车。北京经常堵车，在上下班时，不要打车，乘坐地铁更好。")
TX_E = "Daytime, 5:00 to 23:00, the base fare is 10 yuan for 3 km, and after 3 km it is 2 yuan per km; at night, 23:00 to 5:00, the base fare is 11 yuan for 3 km, and after 3 km it is 2.4 yuan per km. Road and bridge tolls are paid by the passenger. There are many unlicensed taxis in Beijing; don’t take such taxis. Beijing often has traffic jams; at rush hour don’t take a taxi, taking the subway is better. (Numbers spelled out; the book’s slashes are rewritten.)"
WY = ("在北京你也可以随时使用网约车，比如说滴滴出行，只要在手机上下载滴滴出行的打车软件，你就可以非常方便地订车、打车了。滴滴打车的起步价是八元，然后按里程收费，每公里一点五九元。")
WY_E = "In Beijing you can also use a ride-hailing app at any time, for example Didi: just download the Didi app on your phone and you can very conveniently book and hail a car. Didi’s base fare is 8 yuan, then it charges by mileage at 1.59 yuan per kilometer."
SL = ("北京的客运三轮车一般都聚集在市中心和旅游热点等地，每到节假日因为出租车堵车太多，所以人们都去选可以穿过小街道的三轮车。再加上乘三轮车看街景很方便，三轮车的费用常常比出租车高一点。乘坐人力三轮车游老街，大约需要一个半到两个小时，按路线长短收费，一般在三十到一百元左右，可讨价还价，拿到打折的价。人力三轮车也是老北京的特色。")
SL_E = "Beijing’s passenger pedicabs generally gather downtown and at tourist hot spots. On every holiday, because there are too many taxi traffic jams, people choose pedicabs, which can pass through small streets. In addition, riding a pedicab makes it convenient to see the street scenes; the cost of a pedicab is often a bit higher than a taxi. Touring the old streets on a pedicab takes about an hour and a half to two hours, charged by the length of the route, generally about 30 to 100 yuan; you can bargain and get a discounted price. The pedicab is also a feature of old Beijing."
BS = [("公交观光专线车", "公交观光车共有五路，主要去市内各大景点，每条线路各有特色。", "Sightseeing bus lines: there are five routes, mainly going to the major sights in the city; each route has its own character."),
      ("旅游专线公交", "这类车去市区和郊区或外省市景点。不包括门票。游客自己买门票，自己进景点游览。每到一个景点，司机会告诉游客回去的时间。", "Tourist special buses: these go to sights in the city, suburbs, or other provinces. Tickets are not included. Tourists buy their own tickets and tour on their own. At each stop the driver tells tourists the time to return."),
      ("普通公交车", "北京公交车非常多，到市内和郊区各地的都有，还有夜班车、旅游车和专线车等。北京的一些主要街道有公交车专用车道，在堵车时乘坐公交车要比开车和坐出租车方便。市区内公车统一票价一元，郊区公车一元起，路远的加收零点五到一元票价。", "Ordinary buses: Beijing has very many buses, going everywhere in the city and suburbs, with night buses, tourist buses and special lines. Some main streets have bus-only lanes, so in a traffic jam taking a bus is more convenient than driving or taking a taxi. Within the city the fare is a flat 1 yuan, suburban buses start at 1 yuan, and long routes add 0.5 to 1 yuan.")]
DT = ("北京地铁线路包括一号线、二号线、四号线、五号线、八号线、十号线、十三号线等等。北京地铁票价统一为二元，机场快线除外，票价二十五元，想坐多少次，想坐多远都可以。地铁一、二号线穿过北京老城和市内众多景点与商业中心；八号线直接进入奥运中心；四号线在景点、大学、购物的地方停靠。")
DT_E = "Beijing subway lines include lines 1, 2, 4, 5, 8, 10, 13 and so on. The Beijing subway fare is a flat 2 yuan (the Airport Express excepted, fare 25 yuan); you can ride as many times and as far as you like. Lines 1 and 2 pass through the old city and many sights and commercial centers; Line 8 goes directly into the Olympic Center; Line 4 stops at sights, universities and shopping areas."
DT2 = [("一号线", "军事博物馆、西单、天安门、王府井、国贸"), ("二号线", "西直门、宣武门、前门、北京站、雍和宫、鼓楼大街、积水潭"), ("四号线", "黄村火车站、北京南站、陶然亭、宣武门、西单、国家图书馆、中关村、北京大学、圆明园")]
ZX = ("骑自行车，可以休闲地从一个景点骑到另一个景点，游览北京的老街。北京有公共自行车出租点，主要在地铁和商业区等地方。在北京的许多大饭店也有出租自行车的服务，日租金在二十到三十元左右。")
ZX_E = "Riding a bicycle, you can leisurely ride from one sight to another and tour Beijing’s old streets. Beijing has public bicycle rental points, mainly at subways and commercial areas. Many big hotels in Beijing also rent bicycles; the daily rental is about 20 to 30 yuan."
ZP = [("什刹海附近，单人车每小时十元，双人车每小时二十元，押金五百元。", "Near Shichahai: single bike 10 yuan an hour, tandem 20 yuan an hour, deposit 500 yuan."), ("侣松园宾馆对面，单人车每小时五元，双人车每小时十元，押金三百元。", "Opposite Lüsongyuan Hotel: single bike 5 yuan an hour, tandem 10 yuan an hour, deposit 300 yuan."), ("前门大街上，全聚德的对面，每天二十元，押金三百元。", "On Qianmen Street, opposite Quanjude: 20 yuan a day, deposit 300 yuan.")]
L7 = lesson(
    "Lesson 14 Presentation 1: using Chinese in context (getting around Beijing)",
    "打车 · 网约车 · 三轮车 · 公交车 · 地铁 · 骑自行车",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing, and Speaking): scenario",
             "While studying at Beijing University, you and your classmates plan to go to Tiananmen Square, the Forbidden City and the Wangfujing Department Store over the weekend (route: 北京大学 to 天安门广场 to 故宫 to 王府井大街). Compare the available modes of transportation, discuss their advantages and disadvantages, decide how you will travel and explain your reasoning. 1. 出租车 (taxi). The book prints the numbers as digits (“10 元/3 公里”); they are spelled out here.",
             examples=[D(TX, TX_E)]),
        card("网约车 and 人力三轮车",
             "2. 网约车 (ride-hailing). The pedicab is described in a separate box.",
             examples=[D(WY, WY_E), D(SL, SL_E)]),
        card("公交车 (buses)",
             "The three kinds of bus described in the book:",
             examples=[D(z, e) for _, z, e in BS]),
        card("地铁 (subway) and 骑自行车 (bicycle)",
             "The book also shows the subway website and the lines’ main stops: line 1: 军事博物馆、西单、天安门、王府井、国贸; line 2: 西直门、宣武门、前门、北京站、雍和宫、鼓楼大街、积水潭; line 4: 黄村火车站、北京南站、陶然亭、宣武门、西单、国家图书馆、中关村、北京大学、圆明园. Some bicycle rental points are listed below.",
             examples=[D(DT, DT_E), D(ZX, ZX_E)] + [D(z, e) for z, e in ZP]),
        card("Activity 1 (continued)",
             "A. Work in pairs. Read the information about the mode of transportation given to you by your teacher; take notes on its advantages and disadvantages in Chinese characters or pinyin (table: Mode of Transportation, Advantages, Disadvantages); search online for more if needed. B. Work in groups of three. Students from each pair recommend the mode they studied; your partners ask for its advantages and disadvantages; complete the table (rows: 公交车, 地铁, 打车：出租车, 滴滴打车, 其它：骑自行车, 人力三轮车). C. Return to your pairs and decide which mode you will use; you can combine modes. D. Present your decisions and choices to the class."),
    ],
    exercises=[
        M("What is the base fare for a daytime taxi?", "Ten yuan for the first three kilometers", ["Two yuan", "One hundred yuan", "Free"], "起价为三公里十元."),
        M("What does the guide say about unlicensed taxis?", "Don’t take them", ["They are cheaper so take them", "They are the only option", "They are free"], "不要坐这样的出租车。"),
        M("What is recommended at rush hour?", "Take the subway", ["Take a taxi", "Drive", "Ride a bike"], "乘坐地铁更好。"),
        M("What is Didi?", "A ride-hailing app", ["A bus company", "A subway line", "A hotel"], "滴滴出行的打车软件。"),
        M("Why do people choose pedicabs on holidays?", "They can pass through small streets", ["They are free", "They are faster than the subway", "Taxis are banned"], "可以穿过小街道的三轮车."),
        M("What is the flat Beijing subway fare?", "Two yuan, except the Airport Express", ["One yuan", "Ten yuan", "By distance"], "票价统一为二元。"),
        M("What does Line 8 go directly to?", "The Olympic Center", ["The airport", "Tiananmen", "Tsinghua"], "八号线直接进入奥运中心。"),
        M("How much is the flat fare on city buses?", "One yuan", ["Ten yuan", "Five yuan", "Free"], "市区内公车统一票价一元。"),
        M("Where do public bicycle rental points mainly stand?", "At subways and commercial areas", ["Only at airports", "Only in the suburbs", "Only at hotels"], "主要在地铁和商业区。"),
        M("What deposit is asked near Shichahai?", "Five hundred yuan", ["Fifty yuan", "Five yuan", "No deposit"], "押金五百元."),
        M("Which bus type does not include tickets to the sights?", "旅游专线公交", ["普通公交车", "公交观光专线车", "夜班车"], "不包括门票."),
        mean("堵车", "du3 che1", "traffic jam", ["car accident", "parking lot", "car wash"]),
    ],
)

# ------------------------------------------------------------------ 8. mini project and vocabulary
L8 = lesson(
    "Lesson 14 Presentation 1: mini project, a weekend plan",
    "香山 · 圆明园 · 颐和园 · 慕田峪长城 · 八达岭长城",
    requires=[],
    cards=[
        card("Activity 2 (Speaking, Listening, and Writing): Mini Project, A Weekend Plan",
             "After your first two weeks of study at Qinghua University in Beijing, you and your friends decide to explore the region. You need to create a weekend plan and present it to your class; the class will vote on which plan they prefer. A. Work in groups of three. Each group selects one of the maps and circles the locations they would like to visit. Map 1: 香山, 圆明园, 颐和园. Map 2: 慕田峪长城, 八达岭长城 (photographs not included). B. Each group watches a video about an interesting location on its map (video 1 for map 1: Summer Palace; video 2 for map 2: Mutianyu Great Wall, first three minutes), takes notes and discusses whether to recommend it. (Videos, not included.) C. After the video, study your map again; decide whether you would like to visit other places on it. Create a weekend plan together on a white board or flip chart, in Chinese characters: where you will go, the activities, the types of transportation, travel durations and schedules. D. Present your plan to the class; the class votes."),
    ],
    exercises=[
        M("Which places are on Map 1?", "香山, 圆明园, 颐和园", ["八达岭长城, 慕田峪长城", "故宫, 天坛", "北海, 什刹海"], "Map 1."),
        M("Which places are on Map 2?", "慕田峪长城, 八达岭长城", ["香山, 圆明园", "颐和园, 北海", "故宫, 王府井"], "Map 2."),
        M("What must a weekend plan include?", "Where, activities, transportation, travel durations and schedules", ["Only the weather", "Only the cost", "Only the names"], "Plan contents."),
        M("What is 长城 in English?", "The Great Wall", ["The Forbidden City", "The Summer Palace", "The Temple of Heaven"], "长城: Great Wall."),
        M("What is 颐和园 in English?", "The Summer Palace", ["The Old Summer Palace", "The Great Wall", "Beihai Park"], "颐和园: Summer Palace."),
        M("What does the class do after presentations?", "Votes on which plan to use", ["Writes an exam", "Goes home", "Pays a fee"], "The class will vote."),
    ],
)
L9 = vocab_lesson("Lesson 14 Presentation 1 vocabulary", "26 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十四课 休闲旅游 Presentation 1: Beihai Park, 过, 离, 从…到…, Beijing transport guide", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
