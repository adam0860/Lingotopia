"""Unit 41: Lesson 14 (Leisure Travel) Presentation 3 and Area Studies from the book's texts: my parents visit Monterey, the
time-measure complement, the double 了 structure, compound directional verbs, the skill-integration and using-Chinese
activities (the Monterey travel blog), the vocabulary list and the Beihai Park and Xi'an readings. Audio, pictures and maps are
not included; the book writes numbers as digits and they are spelled out here; answer keys the book does not print are mine."""
from zh_auto import *
from zh_l14_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("长大", 0, "zhang3"), ("称为", 1, "wei2"), ("半只", 1, "zhi1"), ("种有", 0, "zhong4"),
                          ("睡什么觉", 3, "jiao4"), ("睡觉", 1, "jiao4"), ("度过", 0, "du4"), ("散了半个小时的步", 0, "san4"),
                          ("懒懒地", 2, "de5"), ("真地喜", 1, "de5"), ("自由地散", 2, "de5"), ("美丽的天堂", 0, "mei3")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 3
P3 = ("我在蒙特雷已经住了三年了。今年八月，爸爸妈妈都退休了，终于有时间来看我了。"
      "他们的飞机是下午四点到机场的。我开车把他们接到我住的公寓。这是他们第一次来蒙特雷，显得特别兴奋，我们一直聊到很晚。"
      "第二天我带他们去参观蒙特雷附近的景点。我们先去了水族馆。这个水族馆不算大，可是有各种各样的海洋动物。从水族馆出来，我们又去了渔人码头。码头两边都是商店和饭店。我们选了一家海鲜饭店，那家饭店的海鲜很有名，而且可以从饭店看到海景。吃完饭以后，我们又沿着海边散了半个小时的步。"
      "下个周末，我打算带爸爸妈妈去看看旧金山的金门大桥，然后再去中国城吃广式早茶。")
P3_E = ("I have been living in Monterey for three years. This August my parents both retired and finally have time to come see me. Their plane arrived at the airport at four in the afternoon. I drove and picked them up to my apartment. It was their first time coming to Monterey and they seemed especially excited; we chatted until very late. The next day I took them to visit the sights near Monterey. We first went to the aquarium. This aquarium isn’t big, but it has all kinds of marine animals. After coming out of the aquarium, we went again to Fisherman’s Wharf. Both sides of the wharf are shops and restaurants. We chose a seafood restaurant; that restaurant’s seafood is famous, and you can see the sea view from the restaurant. After the meal we walked another half hour along the seashore. Next weekend I plan to take my parents to see San Francisco’s Golden Gate Bridge, and then go to Chinatown for Cantonese-style morning tea.")
WORDS = ["退休", "渔人码头", "景点", "参观", "水族馆", "海鲜", "自由", "海洋动物", "名胜古迹", "兴奋", "中国城", "旅行团", "旧金山", "广式早茶", "第一次", "懒人", "金门大桥", "海景"]
L1 = lesson(
    "Lesson 14 Presentation 3: my parents visit Monterey",
    "爸爸妈妈终于有时间来看我了 · 渔人码头 · 金门大桥",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: Fisherman’s Wharf, a whale, jellyfish in an aquarium, the Golden Gate Bridge (not included). Pair up and answer: A. Think about a trip you have gone on with your family or friends. Where did you go? When was the trip? What did you do? Share your stories. B. Now that you have been in Monterey for a while, which tourist spots have you seen and what did you do? C. Have you been to San Francisco? If so, tell the class what you did there. D. What are your favorite things to do when you travel?"),
        card("Presentation 3",
             "The book also prints the passage in traditional characters. Notes: 1. 一直: the structure “verb + 一直 + 到 + time/event” emphasizes an ongoing duration; 到 means “until”. 2. In this presentation both 又 and 再 mean “additionally/also”; 又 indicates an action that has already taken place, while 再 indicates an action that has yet to take place.",
             examples=[D(P3, P3_E)]),
        card("Activities 1 to 3",
             "Activity 1 (Listening and Speaking). A. Global listening: 1. What is the presentation about? 2. How does the speaker feel? B. Detailed listening: 1. How did the speaker’s parents arrive? 2. Have the parents been to the speaker’s residence before? 3. List at least three details you heard about what the speaker and their parents did. 4. What is the speaker’s plan for next weekend? (Audio, not included. From the text: by plane, landing at four in the afternoon; no, it is their first time; aquarium, Fisherman’s Wharf, seafood restaurant, a walk by the sea; next weekend Golden Gate Bridge and Chinatown morning tea.) Activity 2 (Reading, Speaking and Listening). Vocabulary Game, Guessing a Word. A. Divide into two groups; each group receives an index card with words; think how to describe each word without saying it or writing the characters, using indirect description and body language. B. Group A describes and Group B guesses (Group B may ask questions). C. Switch roles. The words on the index cards:",
             examples=[D(z, "(a word to describe and guess)") for z in WORDS]),
        card("Activity 3 (Listening, Writing and Speaking)",
             "A. Listen to the dialog once and determine the topic. B. Pair up; listen again and complete the table (Location; Activities). C. Retell the story in your own words according to your notes, using the sentence patterns 以后, 然后, 最后, if possible. (Audio, not included.)"),
    ],
    exercises=[
        M("How long has the speaker lived in Monterey?", "Three years", ["Three months", "Thirty years", "One year"], "已经住了三年了。"),
        M("Why can the parents finally visit?", "They both retired", ["They won a prize", "It is a holiday", "They moved to Monterey"], "爸爸妈妈都退休了。"),
        M("How did the parents arrive?", "By plane at four in the afternoon", ["By train", "By bus", "By car at night"], "他们的飞机是下午四点到机场的。"),
        M("Have the parents been to Monterey before?", "No, it is their first time", ["Yes, many times", "Yes, last year", "They live there"], "这是他们第一次来蒙特雷。"),
        M("Where did they go first on the second day?", "The aquarium", ["Fisherman’s Wharf", "Golden Gate Bridge", "Chinatown"], "我们先去了水族馆。"),
        M("What did they eat at the wharf?", "Seafood, with a sea view", ["Dumplings", "Pizza", "Hot pot"], "海鲜，而且可以从饭店看到海景。"),
        M("What will they do next weekend?", "See the Golden Gate Bridge and have Cantonese-style morning tea in Chinatown", ["Go home", "Visit Beijing", "See the aquarium again"], "金门大桥，广式早茶。"),
        M("What does 又 indicate in 我们又去了渔人码头?", "An additional action that has already happened", ["An action yet to happen", "A negative", "A question"], "又 = already happened."),
        M("What does 再 indicate in 再去中国城?", "An additional action yet to happen", ["A completed action", "A negation", "A command"], "再 = not yet."),
        M("What does 一直聊到很晚 mean?", "We kept chatting until very late", ["We never chatted", "We chatted early", "We went to sleep"], "一直…到…"),
        mean("退休", "tui4 xiu1", "to retire", ["to rest", "to resign suddenly", "to return"]),
        F("今年八月，爸爸妈妈都退___了。", "休", PART, "退休: retire."),
    ],
)

# ------------------------------------------------------------------ 2. activities 4 and 5
ST = [("我是美国来的大卫。我在北京大学已经学了一年多的中文了。今年是我第一次在中国过春节。我和我的同学一起到外地去旅游。我们去了西安、上海、苏州和杭州。它们都是中国有名的城市。", "C (3): I’m David from America. I’ve been studying Chinese at Peking University for over a year. This year is my first time spending Spring Festival in China. My classmates and I went traveling to other places. We went to Xi’an, Shanghai, Suzhou and Hangzhou. They are all famous cities in China."),
      ("我们是坐高铁去的。因为春节旅游的人很多，我们在旅行社没有订到飞机票。现在中国的高铁和飞机一样，又快又舒服。我们也没有参加旅行团。可是我们都很喜欢这次旅行。", "A (1): We went by high-speed train. Because many people travel at Spring Festival, we couldn’t book plane tickets through the travel agency. Nowadays China’s high-speed rail is like a plane, fast and comfortable. We also did not join a tour group. But we all liked this trip."),
      ("在这几个城市，我们看了很多美丽的风景，也看了很多名胜古迹。我们看到的中国人都很友好。他们有的用中文和我们谈话，有的用英文和我们谈话。在上海我们先去了外滩看风景，然后去了南京路步行街逛商店，吃上海特色饭。", "B (2): In these cities we saw a lot of beautiful scenery and many historic sites. The Chinese people we met were all friendly. Some talked with us in Chinese and some in English. In Shanghai we first went to the Bund to see the view, then went to Nanjing Road pedestrian street to shop and eat Shanghai specialties.")]
INT = [("名字", "旅行的地方", "使用的交通", "和谁去的", "活动")]
L2 = lesson(
    "Lesson 14 Presentation 3 activities: passage rearrangement and trip interviews",
    "我是美国来的大卫 · 坐高铁去的 · 上海的外滩和南京路",
    requires=[],
    cards=[
        card("Activity 4 (Reading and Speaking): Passage Rearrangement",
             "A. Work in groups of three. Each student reads one paragraph of an article (Student A: 我们是坐高铁去的…; Student B: 在这几个城市…; Student C: 我是美国来的大卫…). B. Share the information from your paragraph with your group and arrange the paragraphs into a cohesive order. C. Compare your rearranged article with other groups. The book labels them 1, 2, 3 for Students A, B, C and leaves the order blank; my order (mine): C, A, B (introduction, then how they traveled, then what they saw).",
             examples=[D(z, e) for z, e in ST]),
        card("Activity 5 (Speaking, Writing and Listening)",
             "A. Each student interviews three classmates about recent trips they have taken and takes notes in the table: 姓名 (name), 旅行的地方 (place), 使用的交通 (transportation), 和谁去的 (companions), 活动 (activities). B. Pair up and exchange the information you recorded with your partner. (Photograph not included.)",
             tables=[table(["姓名", "旅行的地方", "使用的交通", "和谁去的", "活动"], [("", "", "", "", "")], title="Interview table (blank)")]),
    ],
    exercises=[
        M("Which paragraph is the introduction?", "我是美国来的大卫…", ["我们是坐高铁去的…", "在这几个城市…", "None of them"], "Paragraph C opens."),
        M("Why did they take the high-speed train?", "They couldn’t book plane tickets because many people travel at Spring Festival", ["The train is cheaper", "They fear planes", "They like slow travel"], "春节旅游的人很多，没有订到飞机票。"),
        M("How does the passage compare China’s high-speed rail to planes?", "Just as fast and comfortable", ["Slower", "Less comfortable", "More expensive"], "又快又舒服。"),
        M("Which cities did David visit?", "Xi’an, Shanghai, Suzhou, Hangzhou", ["Beijing, Tianjin, Dalian", "Guilin, Kunming", "Chengdu, Lhasa"], "西安、上海、苏州和杭州。"),
        M("What did they do first in Shanghai?", "Saw the view at the Bund", ["Shopped on Nanjing Road", "Went to the airport", "Ate dumplings"], "先去了外滩看风景。"),
        M("How did the people they met talk to them?", "Some in Chinese, some in English", ["Only in English", "Only in Chinese", "They did not talk"], "有的用中文，有的用英文。"),
        M("Did they join a tour group?", "No", ["Yes", "Only in Hangzhou", "Only in Xi’an"], "没有参加旅行团。"),
        F("我们去了西安、上海、苏州和杭___。", "州", PART, "杭州: Hangzhou."),
        F("它们都是中国有名的城___。", "市", PART, "城市: city."),
    ],
)

# ------------------------------------------------------------------ 3. time-measure complement
TM1 = [("我在蒙特雷已经住了三年了。", "I have been living in Monterey for three years."), ("他学中文学了三年了。", "He has been studying Chinese for three years.")]
TM2 = [("他每天学习四个小时。", "(1) He studies four hours a day."), ("他昨天学习了四个小时。", "(2) He studied for four hours yesterday."), ("他已经学习了四个小时了。", "(3) He has already been studying for four hours."), ("他每天锻炼身体锻炼一个小时。", "(4) He exercises one hour every day."), ("他昨天锻炼身体锻炼了一个小时。", "(5) He exercised for one hour yesterday."),
       ("他锻炼身体已经锻炼了一个小时了。", "(6) He has already been exercising for an hour."), ("他每天锻炼一个小时的身体。", "(7) He exercises for one hour every day. (variation with 的)"), ("他昨天锻炼了一个小时的身体。", "(8) He exercised for one hour yesterday. (variation)"), ("他已经锻炼了一个小时的身体了。", "(9) He has been exercising for an hour already. (variation)")]
TMX = [("我昨天看电视看了两个钟头。", "(mine) I watched TV for two hours yesterday."), ("她每天睡觉睡八个小时。", "(mine) She sleeps eight hours every day."), ("我们下课以后打篮球打了一个多小时。", "(mine) After class we played basketball for over an hour."), ("上个周末我复习功课复习了大半天。", "(mine) Last weekend I reviewed my lessons for most of the day.")]
TL = [("Category 1 (time words, two columns)", "每天、今天、昨天、已经、星期天、星期五、上个周末、每个星期、昨天晚上、下课以后"), ("Category 2 (activities, two columns)", "看书、跑步、游泳、睡觉、做作业、看电视、买东西、打篮球、锻炼身体、复习功课"), ("Category 3 (durations, two columns)", "多久、两天、大半天、一下午、两个钟头、四十分钟、多长时间、半个小时、一个多小时、三个小时")]
L3 = lesson(
    "Lesson 14 Presentation 3 grammar: the time-measure complement 时量补语",
    "我在蒙特雷已经住了三年了 · 他学中文学了三年了 · 锻炼了一个小时的身体",
    requires=[],
    cards=[
        card("The Time-Measure Complement 时量补语",
             "In Chinese, a time-measure complement expresses the duration of an action (time spent). Structurally, a time-measure complement is placed after a verb’s predicate. When the verb takes both an object and a time-measure complement, the verb is usually repeated in the sentence between the object and the time-measure complement. A variation: place the time and the object together and add 的 between them, making the time a modifier of the object. Without object: S + V + Time-Measure Complement (general action); S + V + 了 + Time-Measure Complement (past action); S + V + 了 + Time-Measure Complement + 了 (continuing action). With object: S + V + O + V + Time-Measure Complement (general); S + V + O + V + 了 + Time-Measure Complement (past); S + V + O + V + 了 + Time-Measure Complement + 了 (continuing). Variation: S + V + Time-Measure Complement + 的 + O (general); S + V + 了 + Time-Measure Complement + 的 + O (past); S + V + 了 + Time-Measure Complement + 的 + O + 了 (continuing).",
             examples=[D(z, e) for z, e in TM1]),
        card("Examples 1 to 9",
             "The book’s nine examples, numbered as in the book:",
             examples=[D(z, e) for z, e in TM2]),
        card("Activity 1 (Reading, Speaking and Listening)",
             "A. Divide into groups of three. Study the three word lists and determine the category of each (the book leaves the category names blank; mine: time words, activities, durations). B. Take turns picking one word from each list and creating your own sentence using the time-measure complement. The three lists (the book prints “40 分钟” with digits and cuts off the last cell at “三个小”; shown here as 四十分钟 and 三个小时) and my sample sentences:",
             tables=[table(["List", "Words"], [(a, b) for a, b in TL], title="Word lists", say=[1])],
             examples=[D(z, e) for z, e in TMX]),
        card("Activities 2 and 3",
             "Activity 2 (Listening and Speaking). A. Listen to each of three dialogs and complete the table (What the Speaker Did; Duration). B. Form groups of three, exchange your information and share your answers with the class. (Audio, not included.) Activity 3 (Speaking, Writing and Listening). A. Each student interviews two classmates about what they did last weekend and how long they spent on each activity, using sentences with a time-measure complement, and records it in the table (Name; Last Weekend’s Activities; For How Long). B. Pair up and exchange information; compare the activities. C. Summarize your findings and present them to the class."),
    ],
    exercises=[
        M("What does a time-measure complement express?", "How long an action lasted", ["Where it happened", "Who did it", "Why it happened"], "Duration."),
        M("Where is the verb repeated?", "Between the object and the duration", ["Before the subject", "After the duration", "Nowhere"], "V + O + V + time."),
        M("Which is correct?", "他学中文学了三年了。", ["他学了三年中文了学。", "他三年学中文学。", "他学中文了三年学了。"], "V + O + V + 了 + time + 了."),
        M("What does 他已经学习了四个小时了 mean?", "He has already been studying for four hours", ["He will study four hours", "He studied yesterday", "He never studies"], "Continuing action."),
        M("What does 他昨天锻炼身体锻炼了一个小时 mean?", "He exercised for an hour yesterday", ["He exercises every day", "He hasn’t exercised", "He will exercise"], "Past action."),
        M("What does 他每天锻炼一个小时的身体 mean?", "He exercises for an hour every day", ["He exercised yesterday", "He is tired", "He walks for an hour"], "Variation with 的."),
        M("Which is a duration word?", "半个小时", ["上个周末", "看电视", "每天"], "半个小时: half an hour."),
        M("Which is an activity word?", "复习功课", ["大半天", "两个钟头", "多久"], "复习功课."),
        F("他学中文学___三年了。", "了", PART, "学了三年了."),
        F("他每天锻炼一个小时___身体。", "的", PART, "时量 + 的 + object."),
    ],
)

# ------------------------------------------------------------------ 4. double 了
DL1 = [("我在蒙特雷住了三个月了。", "I have been living in Monterey for three months. (ongoing: double 了)"), ("我在蒙特雷住过三个月。", "I lived in Monterey for three months. (experience: 过)"), ("我去年在蒙特雷住了三个月。", "Last year I lived in Monterey for three months. (completed past)")]
DL2 = [("王老师已经在美国住了十二年了。", "Teacher Wang has already lived in the U.S. for twelve years."), ("小明，你吃饭怎么这么慢，你已经吃了半个小时了，还在吃。", "Xiaoming, why are you eating so slowly? You’ve already eaten for half an hour and are still eating."), ("他骑自行车骑了两个小时了。", "He has been riding his bike for two hours."), ("我们坐飞机已经坐了十五个小时了，怎么还没到呀？", "We’ve already been on the plane for fifteen hours; why haven’t we arrived yet?"),
       ("大卫，你学中文学了多久了？", "David, how long have you been studying Chinese?"), ("我在国防语言学院学中文学了一年多了。", "I’ve been studying Chinese at the Defense Language Institute for over a year."), ("我已经跑了半个小时的步了。", "I’ve already been running for half an hour.")]
L4 = lesson(
    "Lesson 14 Presentation 3 grammar: the double 了 structure",
    "我在蒙特雷住了三个月了 · 学中文学了多久了？ · 跑了半个小时的步了",
    requires=[],
    cards=[
        card("Double 了 Structure (indicating an ongoing situation)",
             "In Chinese, the double 了 structure (with both the verb 了 and the sentence 了) indicates an ongoing situation when a sentence contains a time-measure complement. This is similar to the English “…have been doing something for a period of time”. In the first example the first 了 is placed after the verb, followed by a time-measure complement (duration), and the second 了 is placed at the end of the sentence. The verbs used in this structure must be continuative verbs or verb phrases, such as 住, 上课, 学习, 游泳, 打电话, 看电视. Patterns: Sub. + Verb + 了 + Time-Measure Complement + 了; Sub. + Verb + Object + Verb + 了 + Time-Measure Complement + 了; Subject + Verb + 了 + Time-Measure Complement + Object + 了.",
             examples=[D(z, e) for z, e in DL1]),
        card("Examples 1 to 6",
             "The book’s examples (the book writes “十二年”, “十五个小时” in characters):",
             examples=[D(z, e) for z, e in DL2]),
        card("Activities 4 to 6",
             "Activity 4 (Reading, Speaking and Listening). Pair up. A. Ask your partner if they do the activities every day (锻炼, 上课, 睡觉, 做作业, 看电视) and, if so, for how long. B. Ask whether they did the activities yesterday (锻炼, 上课, 吃晚饭, 做作业, 看电视, 逛商店) and for how long. C. Ask how long they have been doing the listed activities: 学中文, 在蒙特雷住, 开车, 在陆军/空军/海军工作. Activity 5 (Listening and Speaking). Listen to the dialog and answer: 1. What has the second speaker been doing and for how long? 2. What are the first speaker’s hobbies? How long has he been doing them? 3. What has changed about the first speaker? 4. What is the second speaker’s suggestion and why? (Audio, not included.) Activity 6 (Speaking and Listening). Ask a classmate about their hobbies and how long they have been doing them using the double 了 structure. A. Write your own hobbies in the table 我的爱好 in Chinese characters. B. Interview three classmates about their hobbies and how long they have been doing them (Name; Hobbies; Duration). C. Pair up, exchange information, then summarize your classmates’ hobbies and report them to the class."),
    ],
    exercises=[
        M("What does the double 了 structure indicate?", "An ongoing situation: “have been doing for a period of time”", ["A future plan", "A negation", "A question"], "Verb 了 + duration + sentence 了."),
        M("Which sentence says he still lives in Monterey?", "我在蒙特雷住了三个月了。", ["我在蒙特雷住过三个月。", "我去年在蒙特雷住了三个月。", "我没住过蒙特雷。"], "Double 了."),
        M("What does 我在蒙特雷住过三个月 mean?", "I once lived in Monterey for three months", ["I have lived there three months and still do", "I will live there", "I don’t live there"], "过: experience."),
        M("What does 我们坐飞机已经坐了十五个小时了 mean?", "We’ve already been on the plane for fifteen hours", ["We will fly fifteen hours", "We arrived", "We hate planes"], "Ongoing."),
        M("What does 你学中文学了多久了？ ask?", "How long have you been studying Chinese?", ["Where do you study?", "Why do you study?", "Who is your teacher?"], "多久."),
        M("Which verbs fit the structure?", "Continuative verbs like 住 and 学习", ["Momentary verbs like 死 and 到", "Only nouns", "Only adjectives"], "Continuative verbs."),
        M("What does 我已经跑了半个小时的步了 mean?", "I’ve been running for half an hour already", ["I will run", "I never run", "I ran yesterday"], "Double 了 with 的."),
        F("他骑自行车骑___两个小时了。", "了", PART, "骑了两个小时了."),
        F("王老师已经在美国住了十二年___。", "了", PART, "sentence 了."),
    ],
)

# ------------------------------------------------------------------ 5. compound directional verbs
CV = [("爸爸，你下班了吗？快回来吧。", "Dad, are you off work? Come back quickly. (A, mine: example 1)"), ("爸爸很快就回去。", "Dad will go back very soon. (B)"), ("我就在三楼，你快上来吧！", "I’m on the third floor; come up quickly! (A, example 2)"), ("我马上就上去。", "I’ll go up right away. (B)"),
      ("你来了？快进来吧。随便坐。", "You’re here? Come on in. Sit anywhere. (A, example 3)"), ("那间是你的书房吧？我能进去看一下吗？", "Is that your study? Can I go in and take a look? (B)"), ("进屋来，我有话跟你说。", "Come into the room; I have something to say to you. (example 4)"), ("等一下，我下楼去拿点东西。", "Wait a moment; I’m going downstairs to get something. (example 5)")]
CVT = [("进", "进来", "进去"), ("出", "出来", "出去"), ("上", "上来", "上去"), ("下", "下来", "下去"), ("回", "回来", "回去"), ("过", "过来", "过去"), ("起", "起来", "无")]
SUR1 = [("从大门", "…"), ("书店", ""), ("二楼", ""), ("三楼", ""), ("西餐厅", ""), ("吃饭", ""), ("从西餐厅", ""), ("走 电梯", ""), ("从电梯", ""), ("书店", "")]
L5 = lesson(
    "Lesson 14 Presentation 3 grammar: compound directional verbs",
    "出来 · 进去 · 回来 · 上来 · 下去 · 我下楼去拿点东西",
    requires=[],
    cards=[
        card("Compound Directional Verbs",
             "In Presentation 3 the author says: 从水族馆出来，我们又去了渔人码头。 (From the aquarium, we went to Fisherman’s Wharf.) 出来 is a combination of two directional verbs: 出, “go out”, and 来, which indicates the action is toward the speaker. Such a combination is called a compound directional verb. All the directional verbs in the chart, except 起, can be combined with 来/去; 起 can only combine with 来 (the table shows 无, “none”, for 起去). Patterns: Subject + 进来/进去/出来/出去/上来/上去/下来/下去/回来/回去/过来/过去 + (verb phrase); Subject + 进/出/上/下/回/过 + place + 来/去 + (verbal phrase). The book’s chart has 进, 出, 上, 下, 回, 过, 起 in the first row, with 来 and 去 below, and sketches for each compound (not included).",
             tables=[table(["Verb", "+ 来", "+ 去"], [(a, b, c) for a, b, c in CVT], title="Compound directional verbs", say=[0, 1, 2])],
             examples=[D("从水族馆出来，我们又去了渔人码头。", "From the aquarium we went to Fisherman’s Wharf.")]),
        card("Examples 1 to 5",
             "The book’s examples (A and B are two speakers):",
             examples=[D(z, e) for z, e in CV]),
        card("Activity 7 (Speaking and Listening): Airport Surveillance",
             "Pair up. Each student plays a detective at an airport, Detective A or Detective B. Detective A observes Subject 1 (code name 狗熊) and tells Detective B 狗熊’s route, using compound directional verbs and the “V + directional verb” structures from Lesson 13. Detective B draws the route on a blank map. Detective A may use the words below the map as clues. Round 1: Detective A is outside the airport; the clues are in order: 1. 从大门 ___ 书店。 2. ___ 二楼 … 3. ___ 三楼 … 4. 西餐厅 … 5. ___ 吃饭 … 6. 从西餐厅 ___ … 7. 走 电梯 … 8. 从电梯 ___ 书店。 (the book’s lines are partly blank and laid out on the map). Round 2: switch locations; Detective A is inside the airport; clues: 1. 从大门 … 2. 跑 二楼 … 3. 走 国际候机厅 … 4. 从国际候机厅 … 5. 走 二楼的电梯 … 6. 从三楼的电梯 … 7. 吃饭 … 8. 跑 二楼 … 9. 又 二楼 坐电梯 … 10. 坐电梯 一楼。 (The maps are pictures and not included; the blanks are for compound directional verbs, for example 进来/进去, 上去, 下来, 出来.)"),
    ],
    exercises=[
        M("What does 出来 combine?", "出 (go out) and 来 (toward the speaker)", ["出 and 去", "进 and 去", "上 and 来"], "出 + 来."),
        M("Which verb can combine only with 来?", "起", ["进", "回", "过"], "起来 only."),
        M("Which means “go in” (away from the speaker)?", "进去", ["进来", "出来", "回来"], "去: away."),
        M("Which means “come up” (toward the speaker)?", "上来", ["上去", "下去", "过去"], "来: toward."),
        M("What does 我马上就上去 mean?", "I’ll go up right away", ["I’ll come down", "I’ll come in", "I’ll go out"], "上去: go up."),
        M("What does 快进来吧 mean?", "Come on in", ["Go out", "Go away", "Hurry up and leave"], "进来."),
        M("What does 进屋来 mean?", "Come into the room", ["Leave the room", "Close the door", "Go upstairs"], "进屋来."),
        M("What does 我下楼去拿点东西 mean?", "I’m going downstairs to fetch something", ["I’m coming upstairs", "I’m leaving", "I’m buying a house"], "下楼去."),
        F("你来了？快进___吧。", "来", PART, "进来: come in."),
        F("我能进___看一下吗？", "去", PART, "进去: go in."),
        F("从水族馆出___，我们又去了渔人码头。", "来", PART, "出来."),
    ],
)

# ------------------------------------------------------------------ 6. blog
BL1 = ("自由行，蒙特雷游记，一。去年夏天，孩子放暑假的时候，我和太太终于有时间带着两个孩子第一次到美国加州的蒙特雷玩。我们在蒙特雷一共玩了四天，孩子们都特别兴奋，因为在蒙特雷我们度过了非常有意思的四天。"
       "我们是从上海坐飞机到旧金山机场的。旧金山机场离蒙特雷有两个半小时的车程，所以下了飞机以后，我们在机场租了一辆车，沿着一零一高速公路一直开到蒙特雷。第一天到达蒙特雷的时候已经是晚上九点了，我们计划在这儿住三个晚上。我们住的酒店就在市中心，离景点、饭馆和海边都很近。可以步行去很多地方。"
       "第二天吃完早饭以后，我们一家四口就从酒店走到蒙特雷的渔人码头参观。蒙特雷的渔人码头是加州第一个较大的渔人码头。码头附近有很多的商店、饭馆、小吃摊，你还可以看到很多停在海湾里的游船，自由起飞的海鸟和懒懒地晒着太阳的海豹和海狮。在这里我们自由地散步，感到生活真美好！中午我们就在码头上一家有名的海鲜饭馆吃了饭，然后我们去了旁边的海滩晒太阳、散步，孩子们在沙滩上玩沙子。")
BL1_E = ("Independent travel, Monterey travel notes (1). Last summer, when the kids were on summer vacation, my wife and I finally had time to take our two children to Monterey, California, for the first time. We played in Monterey for four days in all; the children were all especially excited because in Monterey we spent four very interesting days. We flew from Shanghai to San Francisco airport. San Francisco airport is a two-and-a-half-hour drive from Monterey, so after getting off the plane we rented a car at the airport and drove along Highway 101 all the way to Monterey. When we arrived in Monterey on the first day it was already nine in the evening; we planned to stay here three nights. Our hotel was downtown, very close to the sights, restaurants and the sea; we could walk to many places. On the second day after breakfast our family of four walked from the hotel to Monterey’s Fisherman’s Wharf. Monterey’s Fisherman’s Wharf is California’s first fairly large fisherman’s wharf. Near the wharf there are many shops, restaurants and snack stalls, and you can see many pleasure boats moored in the bay, seabirds taking off freely, and seals and sea lions lazily sunbathing. Here we strolled freely and felt that life is truly wonderful! At noon we ate at a famous seafood restaurant on the wharf, then went to the beach next to it to sunbathe and stroll, and the children played with sand on the beach.")
BL2 = ("自由行，蒙特雷游记，二。第三天我们去了蒙特雷最有名的景点水族馆。去水族馆以前，我们先在他们的网站上预订了我们参观的时间，这样你不用排队买票。蒙特雷的水族馆是一家很大的水族馆，有各种各样的海洋动物。在水族馆的中间有一个特大的水族箱，里面不但有千万条小鱼一起游来游去，而且还可以看到一些大鱼在你的头顶上游过。除了看海洋动物以外，孩子们还可以用手接近动物，他们显得又紧张又兴奋。水族馆的工作人员真地喜爱大海、喜爱那些美丽的海洋动物，孩子们有什么问题，他们都可以回答。"
       "第四天我们全家开车去了蒙特雷附近的一个风景区，也是一个州立的公园。这个公园离蒙特雷大约十五公里，公园入口处有一个小停车场。停车以后，我们就一直沿着海边的小路走，看到了美丽的海景、高大的古树、特别的石头和金色阳光下的海面。我们全家拍了很多照片，这儿像是一个美丽的天堂。"
       "虽然四天的旅行很快就过去了，但是我打算以后还要带太太和孩子们再来蒙特雷玩，因为这儿有美丽的景色、可爱的动物、友好的人们和可口的美食。")
BL2_E = ("Independent travel, Monterey travel notes (2). On the third day we went to Monterey’s most famous sight, the aquarium. Before going, we first booked our visit time on their website, so you don’t have to queue to buy tickets. Monterey’s aquarium is a very large aquarium with all kinds of marine animals. In the middle is a huge tank where not only thousands of small fish swim around together, but you can also see some big fish swim over your head. Besides watching marine animals, the children could also touch animals with their hands, and they looked both nervous and excited. The aquarium staff truly love the sea and those beautiful marine animals, and they could answer any questions the children had. On the fourth day our whole family drove to a scenic area near Monterey, also a state park. This park is about fifteen kilometers from Monterey and has a small parking lot at its entrance. After parking, we walked along the small path by the sea, and saw beautiful sea views, tall old trees, special rocks, and the sea surface in the golden sunlight. We took many photos; this place is like a beautiful paradise. Although the four-day trip passed quickly, I plan to bring my wife and children to Monterey again later, because there are beautiful scenery, lovely animals, friendly people and delicious food here.")
CT = [("海豹", "hǎibào", "seal"), ("海狮", "hǎishī", "sea lion"), ("天堂", "tiāntáng", "paradise; heaven")]
MONO = ("在长城上休息的时候，旁边坐了一对母子，我问母亲：“您是来北京旅游的吗？”她说：“对啊。”我又问她五六岁的儿子：“小朋友，你从哪儿来啊？”小朋友说：“从妈妈肚子里。”")
MONO_E = "While resting on the Great Wall, a mother and son sat next to me. I asked the mother: “Are you here in Beijing for a trip?” She said: “Yes.” I then asked her five- or six-year-old son: “Little friend, where do you come from?” The little boy said: “From Mommy’s tummy.” (the book’s title: 肚子)"
ITIN = [("第一天", "从上海坐飞机到旧金山，租车开到蒙特雷，晚上九点到酒店。"), ("第二天", "走到渔人码头，在海鲜饭馆吃午饭，去海滩晒太阳、散步。"), ("第三天", "去水族馆，看各种海洋动物。"), ("第四天", "开车去州立公园，沿着海边的小路走，拍照。")]
L6 = lesson(
    "Lesson 14 Presentation 3: skill integration and the Monterey travel blog",
    "自由行蒙特雷游记 · 海豹 · 海狮 · 肚子",
    requires=[],
    cards=[
        card("Skill Integration: Activities 1 and 2",
             "Activity 1 (Listening, Writing, Speaking and Reading). Photographs: Shanghai, Chengdu, Lhasa and the Potala Palace (not included). A. Work in groups of three. Each member listens to one travel monolog (Monologs 1, 2, 3) and writes a summary of it. B. Exchange summaries. C. Read the scripts together and check your information. D. Compare the stories and tell each other which speaker’s travel experience you liked most and why. (Audio, not included.) Activity 2 (Listening, Writing, Speaking and Reading). A. Listen to the dialog once and determine the topic: the two speakers are talking about ___. B. Listen again and order the activities and events as described by the second speaker, taking notes in pinyin or characters: 到了 … 以后, 先, 然后, 中午, 午饭以后, 然后, 最后. C. Pair up and share your information. D. Use the information to retell the story, adding as many details as you can. E. Read the script with your class. (Audio, not included.)"),
        card("Using Chinese in Context, Activity 3 (Reading, Writing, Speaking and Listening)",
             "Read the travel blog post and complete the tasks. A. Pre-reading: study the following words and think about any Chinese words you know that use similar word-formation structures; share with a classmate. 海豹 hǎibào seal; 海狮 hǎishī sea lion; 天堂 tiāntáng paradise; heaven. B. Divide into two groups; Group 1 reads blog post 1 and Group 2 reads blog post 2. Write a summary for each paragraph in the table (Main Idea and Details) and share. The book prints the numbers as digits (四天, 101, 15) and “一、二” as (一) (二); spelled out here. Blog Post 1:",
             examples=[D(BL1, BL1_E)]),
        card("Blog Post 2",
             "Photograph: Pixabay/comuirgheasa (not included).",
             examples=[D(BL2, BL2_E)]),
        card("Activity 3 C and D, and Activity 4",
             "C. Pair up with a member of the other group. Each partner exchanges information from their paragraphs. Write the blogger’s daily travel itinerary in the table (第一天, 第二天, 第三天, 第四天). My itinerary (mine) is in the first example below. D. With the same partner, recommend places in Monterey and nearby for the blogger’s next trip (Recommended Places; Activities) in Chinese characters and share with the class. Activity 4 (Reading and Speaking). Read the dialog and answer: 1. Why did the speaker get different answers from the mother and the child? (Mine: the mother understood “come from” as where she came from for the trip, while the child understood where babies come from.)",
             examples=[D(a + "：" + b, "(mine: " + a + " of the blogger’s itinerary)") for a, b in ITIN] + [D(MONO, MONO_E)]),
    ],
    exercises=[
        M("How many days did the family spend in Monterey?", "Four", ["Two", "Seven", "One"], "一共玩了四天。"),
        M("How did they get from the airport to Monterey?", "In a rental car along Highway 101", ["By train", "By bus", "By taxi"], "租了一辆车，沿着一零一高速公路。"),
        M("How far is San Francisco airport from Monterey?", "Two and a half hours’ drive", ["Five minutes", "A day", "Ten hours"], "两个半小时的车程。"),
        M("What did they see at the wharf?", "Boats, seabirds, seals and sea lions", ["Camels", "Skyscrapers", "A zoo"], "游船，海鸟，海豹和海狮。"),
        M("How did they avoid queuing at the aquarium?", "They booked their visit time on the website", ["They arrived at dawn", "They paid extra", "They skipped it"], "预订了我们参观的时间，不用排队买票。"),
        M("How did the children feel when touching animals?", "Both nervous and excited", ["Bored", "Angry", "Sleepy"], "又紧张又兴奋。"),
        M("How far is the state park from Monterey?", "About fifteen kilometers", ["About one hundred kilometers", "About one kilometer", "About fifty kilometers"], "大约十五公里。"),
        M("What does 天堂 mean?", "Paradise; heaven", ["Hell", "Sea", "Garden"], "天堂."),
        M("What does 海豹 mean?", "Seal", ["Sea lion", "Whale", "Octopus"], "海豹."),
        M("What is the joke in 肚子?", "The child answers “from Mommy’s tummy”", ["He is from Beijing", "He lives on the Great Wall", "He is from the U.S."], "从妈妈肚子里。"),
        mean("游记", "you2 ji4", "travel notes", ["game record", "travel ticket", "travel agency"]),
        F("孩子们在沙滩上玩沙___。", "子", PART, "沙子: sand."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context
POINTS = [("旅行时间", "什么时候，多久"), ("旅行地点", "国家，城市"), ("旅行伙伴", "和谁一起去"), ("旅行方式", "怎么去的"), ("旅行活动", "做了什么"), ("难忘的原因", "为什么难忘")]
TOPICS = ["第一次到美国旅行", "第一次去中国旅行", "第一次去纽约旅行", "第一次去北京旅行", "第一次去旧金山旅行", "第一次去上海旅行", "第一次去巴黎旅行", "第一次到法国旅行", "第一次到墨西哥旅行", "第一次到意大利旅行", "第一次到火星旅行", "第一次到月球旅行"]
QS = [("目的地", "Destination"), ("时间", "When the trip was taken"), ("旅行伙伴", "Travel partners"), ("交通方式", "Modes of transportation"), ("住宿", "Accommodations"), ("活动", "Activities"), ("特别的记忆", "Special memories about the trip")]
L7 = lesson(
    "Lesson 14 Presentation 3: using Chinese in context (unforgettable trip, story relay, interview)",
    "最难忘的一次旅行 · 故事接龙 · 第一次出国旅行",
    requires=[],
    cards=[
        card("Activity 1 (Writing, Speaking and Listening): 最难忘的一次旅行",
             "Scenario: you and your classmates are planning to compete in an upcoming Chinese speech contest in California; the theme this year is “an unforgettable trip”. Your class will hold a practice round. A. Prepare your speech about an unforgettable trip; organize your thoughts about the points below and jot down key information (prepare a cue card if necessary). B. In groups of three take turns sharing your trip in Chinese using these structures when possible: 第一天… 第二天… 第三天… 最后一天… or 先… 又… 然后… …以后 然后又… Your group members offer suggestions. C. Within your group decide who has the most interesting and unforgettable story; that student presents to the class. D. The class gives feedback on each speech. (Photograph not included.)",
             tables=[table(["要点", "说明"], [(a, b) for a, b in POINTS], title="Points to organize", say=[0, 1])]),
        card("Activity 2 (Speaking and Listening): Story Relay 故事接龙: 第一次___旅行",
             "You and your classmates create a story in Chinese about the first time traveling somewhere. A. Work in small groups to choose a topic for your story and discuss what should be covered; write down key words in Chinese. The topics: 第一次到美国旅行; 第一次去中国旅行; 第一次去纽约/北京/旧金山/上海/巴黎旅行; 第一次到法国/墨西哥/意大利旅行; 第一次到火星/月球旅行; or create your own. B. One group starts the relay with the first story about the topic chosen; each student provides one sentence at a time; students from the other group continue, in turn, using complete and complex sentences with the vocabulary and grammar you have learned. C. Continue until you finish the story, with no fewer than 18 sentences and no more than 30. D. The other group starts the next round with its own topic. E. As a class, compare the two stories and decide which one is better liked.",
             examples=[D(z, "(a story topic)") for z in TOPICS]),
        card("Activity 3 (Speaking, Listening and Writing): Travel Interview, First Trip Abroad",
             "Scenario: you are a student journalist at Nanjing University. The school newspaper asked you to interview international students about their first trip abroad or to any big city or famous place, and then write an article. A. Before the interviews, think about your questions and make sure they cover the points below; write down your questions and key words in Chinese characters. B. Interview two classmates and write notes in the table (问题; 学生（一） 姓名; 学生（二） 姓名; rows 目的地, 时间, 旅行伙伴, 交通方式, 住宿, 活动, 特别的记忆). C. After the interviews write your report and email it to the editor of the school newspaper.",
             tables=[table(["问题", "Meaning"], [(a, b) for a, b in QS], title="Interview rows", say=[0])]),
    ],
    exercises=[
        M("What is the theme of the speech contest?", "An unforgettable trip", ["My family", "My hobbies", "My school"], "最难忘的一次旅行."),
        M("Which structure suits telling a trip in order?", "先…又…然后…以后", ["不但…而且…", "虽然…但是…", "既然…就…"], "Sequence structures."),
        M("How many sentences should the story relay have?", "No fewer than 18 and no more than 30", ["Exactly 5", "At least 100", "As many as you like"], "Between 18 and 30."),
        M("Which topic is NOT in the list?", "第一次去日本旅行", ["第一次到美国旅行", "第一次到火星旅行", "第一次去巴黎旅行"], "Listed topics."),
        M("What role do you play in Activity 3?", "A student journalist interviewing international students", ["A tour guide", "A police officer", "A hotel clerk"], "Student journalist."),
        M("What do you do after the interviews?", "Write a report and email it to the editor", ["Post it on a wall", "Give a speech", "Burn it"], "Email the editor."),
        F("最难忘的一次旅___。", "行", PART, "旅行: trip."),
        F("第一次到火星旅行，故事___龙。", "接", PART, "故事接龙: story relay."),
    ],
)
L8 = vocab_lesson("Lesson 14 Presentation 3 vocabulary", "27 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 9. Area Studies
L9 = lesson(
    "Lesson 14 Area Studies: Beihai Park and Xi’an",
    "北海公园 · 西安 · 兵马俑 · 丝绸之路",
    requires=[],
    cards=[
        card("Beihai Park (北海公园)",
             "Beihai Park (Chinese: Beihai Gongyuan 北海公园), also known as the Winter Palace, is a public park and former imperial garden located in the northwestern part of the Imperial City, Beijing. First built in the 11th century, it is among the largest of all Chinese gardens and contains numerous historically important structures, palaces, and temples. Since 1925, the place has been open to the public as a park. It is also connected at its northern end to the Shichahai (什刹海). The park has an area of more than 69 hectares (171 acres), with a lake that covers more than half of the entire park. (Photograph: the White Pagoda in Beihai Park 白塔, not included. Article source: Wikipedia.)"),
        card("Xi’an (西安)",
             "Xi’an, also known as Sian, is called the birthplace of Chinese civilization. Xi’an is the capital of Shaanxi Province. It is one of the oldest cities in China, is the oldest prefecture capital and one of the Four Great Ancient Capitals. Xi’an was the capital of 13 imperial dynasties, the most for any city, and many ancient structures are preserved. Since the 11th century BC, Xi’an became a cultural and political center of China, under several of the most important dynasties in Chinese history, including Western Zhou (西周), Qin (秦), Western Han (西汉), Sui (隋), and Tang (唐). Xi’an is the starting point of the Silk Road and home to the Terracotta Army of Emperor Qin Shi Huang."),
        card("Xi’an today",
             "Since the 1980s, as part of the economic growth of inland China, especially for the central and northwest regions, the city of Xi’an has re-emerged as a cultural, industrial, and educational center of the entire central-northwest region, with many facilities for scientific research and development, national security and space exploration. Xi’an currently holds sub-provincial status, administering nine districts and four counties. In 2019, it was named one of the seven main mega-cities of China. Xi’an is a popular tourist destination with foreigners and locals alike. Being near the central part of China, Xi’an is a crossroads for many of the great Chinese cuisines. Dumplings, noodles, lamb, and kabobs all contribute to the list of best dishes in Xi’an. (Photographs: Xi’an Bell Tower and Terracotta warriors, not included. Article source: Wikipedia.)"),
    ],
    exercises=[
        M("What is another name for Beihai Park?", "The Winter Palace", ["The Summer Palace", "The Forbidden City", "The Temple of Heaven"], "Also known as the Winter Palace."),
        M("When was Beihai Park first built?", "In the 11th century", ["In 1925", "In the 1980s", "In 2019"], "First built in the 11th century."),
        M("When did the park open to the public?", "1925", ["1911", "1949", "2019"], "Since 1925."),
        M("How much of the park does the lake cover?", "More than half", ["A tenth", "A quarter", "None"], "More than half."),
        M("What is Xi’an called?", "The birthplace of Chinese civilization", ["The Pearl of the Orient", "The Garden City", "The Water Town"], "Birthplace of Chinese civilization."),
        M("How many imperial dynasties had Xi’an as capital?", "Thirteen", ["Three", "Eight", "Twenty"], "13 dynasties."),
        M("Xi’an is the starting point of what?", "The Silk Road", ["The Grand Canal", "The Great Wall", "The Yangtze"], "Starting point of the Silk Road."),
        M("Which famous attraction is in Xi’an?", "The Terracotta Army", ["The Bund", "The Potala Palace", "West Lake"], "Terracotta Army of Qin Shi Huang."),
        M("Which province is Xi’an the capital of?", "Shaanxi", ["Shanxi", "Henan", "Sichuan"], "Capital of Shaanxi Province."),
        M("Why is Xi’an a crossroads for cuisines?", "It is near the central part of China", ["It is by the sea", "It has no restaurants", "It is in the south"], "Near the central part of China."),
    ],
)

UNIT = unit("第十四课 休闲旅游 Presentation 3: parents visit, 时量补语, double 了, compound directional verbs, Monterey blog, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
