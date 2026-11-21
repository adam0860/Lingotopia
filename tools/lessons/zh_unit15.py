"""Unit 15: Lesson 5 book texts, Presentation 3 (climate and comparing): the Chongqing and Shanghai readings,
the book's examples for 跟…一样, 比 and 有, the weather report, 可是 and 好+verb, temperature conversion,
the Kunming reading and the speaking tasks. Audio items are not included."""
from zh_auto import *

PART = ["吗", "们", "呢"]

# ---------------------------------------------------------------------------- Chongqing and Shanghai
L_P3_READINGS = lesson(
    "Readings: Chongqing and Shanghai",
    "重庆是一个山城 · 最高气温四十三摄氏度 · 上海有两千四百多万人口",
    requires=[],
    cards=[
        card("Before you read (Getting Started)",
             "Pair up and discuss: A. How is the weather in Monterey? Do you like it and why? B. What do you know about Chongqing? Where is it located? C. Is the weather in Chongqing the same as it is in Monterey?"),
        card("Presentation 3: 重庆 (Chongqing)",
             "The book prints a number in digits (43, 7); they are written out here so that every word has its pinyin. 山城 is a mountain city; 平均 is “on average”; 左右 is “about”.",
             examples=[D("重庆在中国西南部，是一个山城。", "Chongqing is in the southwest of China and is a mountain city."),
                       D("重庆一年四季大部分是阴天，很少有晴天。", "Chongqing is mostly cloudy all year round, and rarely has sunny days."),
                       D("重庆的春天经常下雾。", "In spring it often fogs in Chongqing."),
                       D("夏天很热，最高气温四十三摄氏度。", "Summer is very hot, with a highest temperature of 43 degrees Celsius."),
                       D("秋天经常下雨，有时候刮风。", "In autumn it often rains and sometimes the wind blows."),
                       D("冬天跟春天一样，也常常下雾，可是很少下雪。", "Winter is the same as spring: it is often foggy too, but it rarely snows."),
                       D("重庆的气候没有蒙特雷这么好，夏天没有蒙特雷凉快，冬天比蒙特雷冷，平均最低气温七摄氏度左右。", "Chongqing’s climate is not as good as Monterey’s: summer is not as cool as Monterey’s, winter is colder than Monterey’s, with an average lowest temperature of about 7 degrees Celsius."),
                       D("重庆有很多好玩的地方、好吃的东西，是一个很有意思的城市。", "Chongqing has many fun places and delicious things, and is a very interesting city.")]),
        card("Reading (Activity 2): 上海 (Shanghai)",
             "Read the passage and answer the questions: What is the passage about? What is the weather like in spring and summer in Shanghai? What is said about autumn and winter? What is said about the uniqueness of Shanghai?",
             examples=[D("上海在中国的东南部，一年有四个季节，春天很暖和，夏天很闷热，平均最高气温三十二摄氏度。", "Shanghai is in the southeast of China and has four seasons. Spring is very warm and summer is hot and stuffy, with an average highest temperature of 32 degrees Celsius."),
                       D("上海的秋天很凉快，有时候下雨，可是很少下雾。", "Autumn in Shanghai is cool; sometimes it rains, but it is rarely foggy."),
                       D("冬天天气阴冷，很少有晴天，常常下雨，刮风，可是很少下雪。", "In winter the weather is cloudy and cold, there are few sunny days, it often rains and the wind blows, but it rarely snows."),
                       D("上海有两千四百多万人口，是一个大城市，有很多好玩、好看的地方。", "Shanghai has a population of more than 24 million. It is a big city with many fun and nice-looking places.")]),
    ],
    exercises=[
        M("Where is Chongqing?", "In the southwest of China", ["In the southeast", "In the northeast", "In Texas"], "重庆在中国西南部."),
        M("What kind of city is Chongqing?", "A mountain city", ["A port city", "A desert city", "A small village"], "是一个山城."),
        M("What is the weather in Chongqing mostly like all year?", "Cloudy", ["Sunny", "Snowy", "Windy"], "大部分是阴天."),
        M("What happens often in Chongqing in spring?", "Fog", ["Heavy snow", "Strong wind", "Heat"], "春天经常下雾."),
        M("What is the highest temperature in summer in Chongqing?", "43 °C", ["32 °C", "29 °C", "21 °C"], "最高气温四十三摄氏度."),
        M("What is Chongqing like in autumn?", "It often rains and sometimes the wind blows", ["It snows", "It is foggy", "It is hot"], "秋天经常下雨，有时候刮风."),
        M("How is Chongqing’s winter compared with Monterey’s?", "Colder", ["Warmer", "The same", "Cooler in summer"], "冬天比蒙特雷冷."),
        M("What is Chongqing’s average lowest temperature?", "About 7 °C", ["About 43 °C", "About 0 °C", "About 21 °C"], "平均最低气温七摄氏度左右."),
        M("What does the writer call Chongqing at the end?", "A very interesting city", ["A very cold city", "A small city", "A boring city"], "很有意思的城市."),
        M("Where is Shanghai?", "In the southeast of China", ["In the southwest", "In the northwest", "In the northeast"], "上海在中国的东南部."),
        M("What is summer in Shanghai like?", "Hot and stuffy", ["Cool", "Foggy", "Snowy"], "夏天很闷热."),
        M("Does it snow often in Shanghai in winter?", "No, rarely", ["Yes, often", "Yes, every day", "It never rains"], "很少下雪."),
        M("How many people does Shanghai have, according to the reading?", "More than 24 million", ["More than 31 million", "More than 21 million", "27,000"], "两千四百多万."),
        mean("山城", "shan1cheng2", "mountain city", ["a mountain", "a small city", "a state"]),
        mean("平均", "ping2jun1", "on average", ["the highest", "the lowest", "about"]),
        mean("左右", "zuo3you4", "about, around", ["left", "right", "exactly"]),
        mean("阴天", "yin1tian1", "cloudy day", ["sunny day", "rainy day", "foggy day"]),
        mean("晴天", "qing2tian1", "sunny day", ["cloudy day", "rainy day", "snowy day"]),
    ],
)

# ---------------------------------------------------------------------------- 跟…一样
L_P3_YIYANG = lesson(
    "The book’s patterns: 跟…一样, and the Zhao Ming dialog",
    "NP1 跟 NP2 一样 + adjective · 不一样 · 一样吗？ · 一样不一样？",
    requires=[],
    cards=[
        card("跟 … 一样: patterns",
             "跟…一样 shows that two things or persons are identical when compared. Patterns: NP1 跟 NP2 一样 + adjective; NP1 跟 NP2 一样 + VP (verbs of emotion, like 喜欢, 想). "
             "Negative: NP1 跟 NP2 不一样 + adjective. Questions: NP1 跟 NP2 一样 + adjective 吗？ and NP1 跟 NP2 一样不一样 + adjective？",
             examples=[D("我弟弟跟我一样高。", "My younger brother is as tall as I am."),
                       D("李先生跟王先生一样喜欢学生。", "Mr. Li loves his students just the same as Mr. Wang does."),
                       D("这个教室跟那个教室不一样大。", "This classroom and that classroom are not the same in size."),
                       D("今年夏天跟去年夏天一样热吗？", "Is this summer as hot as last summer?"),
                       D("今年夏天跟去年夏天一样不一样热？", "Is this summer as hot as last summer? (verb-not-verb form)")]),
        card("Activity 1: a conversation between two Chinese students",
             "In the book you highlight the 跟…一样 patterns, write translations and role-play. 习惯 (xíguàn) means “to be used to”.",
             examples=dlg([
                 ("A", "赵明，你习惯这儿的天气吗？", "Zhao Ming, are you used to the weather here?"),
                 ("B", "习惯。我们老家的天气跟这儿的一样，冬天不冷，夏天不热。", "Yes. The weather in our hometown is the same as here: winter is not cold and summer is not hot."),
                 ("A", "我们老家的天气跟这儿的不一样，所以我不太习惯。", "The weather in our hometown is different from here, so I am not quite used to it."),
                 ("B", "你们老家是不是冬天很冷，夏天很热？", "Is it that winter is very cold and summer is very hot in your hometown?"),
                 ("A", "对。", "Yes."),
             ])),
        card("Activity 2: short dialogs (from pictures)",
             "The book shows pictures and asks you to complete the answers in pinyin. Dialog 1: a gym compared with your school’s gym. Dialog 2: winter in your hometown compared with New York. Dialog 3: two aircraft, 强击机 (qiángjījī, attack aircraft) and 轰炸机 (hōngzhàjī, bomber).",
             examples=[D("这个体育馆跟你们学校的体育馆一样吗？", "Is this gym the same as your school’s gym?"),
                       D("你们老家的冬天跟纽约的冬天一样冷吗？", "Is the winter in your hometown as cold as the winter in New York?"),
                       D("强击机跟轰炸机不一样。", "An attack aircraft is not the same as a bomber.")]),
        card("Activity 3: same and different",
             "Write three weather phenomena of your hometown and of Monterey that are the same and different, for each season, and exchange the information with a classmate."),
    ],
    exercises=[
        M("What does 我弟弟跟我一样高 say?", "My younger brother is as tall as I am.", ["My younger brother is taller than I am.", "My younger brother is different from me.", "I am taller."], "跟 … 一样高."),
        M("What does 李先生跟王先生一样喜欢学生 say?", "Mr. Li loves students just as Mr. Wang does.", ["Mr. Li is the same as Mr. Wang.", "Mr. Li is a student of Mr. Wang.", "Mr. Li does not like students."], "一样 + verb of emotion."),
        M("What does 这个教室跟那个教室不一样大 say?", "The two classrooms are not the same size.", ["This classroom is bigger.", "That classroom is bigger.", "Both are big."], "不一样大."),
        M("Which is the 吗 question?", "今年夏天跟去年夏天一样热吗？", ["今年夏天跟去年夏天一样不一样热？", "今年夏天比去年夏天热。", "今年夏天没有去年夏天热。"], "Pattern + 吗."),
        M("Which is the verb-not-verb question?", "今年夏天跟去年夏天一样不一样热？", ["今年夏天跟去年夏天一样热吗？", "今年夏天比去年夏天热吗？", "今年夏天有去年夏天热吗？"], "一样不一样."),
        M("Is Zhao Ming used to the weather here?", "Yes", ["No", "Only in summer", "He did not say"], "习惯."),
        M("How is the weather in Zhao Ming’s hometown compared with here?", "The same: winter is not cold and summer is not hot", ["Different: winter is very cold", "Hotter", "Rainier"], "跟这儿的一样."),
        M("Why is the other student not used to the weather here?", "Their hometown weather is different", ["It is too hot here", "It rains a lot here", "They have no friends here"], "我们老家的天气跟这儿的不一样."),
        M("What is the other student’s hometown like?", "Winter is very cold and summer is very hot", ["Cool all year", "Rainy all year", "Snowy all year"], "冬天很冷，夏天很热."),
        mean("习惯", "xi2guan4", "to be used to", ["to like", "to hate", "to learn"]),
        mean("强击机", "qiang2ji1ji1", "attack aircraft", ["bomber", "helicopter", "transport plane"]),
        mean("轰炸机", "hong1zha4ji1", "bomber", ["attack aircraft", "fighter", "helicopter"]),
        F("我弟弟___我一样高。", "跟", PART, "跟 … 一样.", tr="My younger brother is as tall as I am."),
        F("这个教室跟那个教室不一___大。", "样", PART, "不一样.", tr="This classroom and that classroom are not the same size."),
        F("你习惯这儿的天___吗？", "气", PART, "天气.", tr="Are you used to the weather here?"),
    ],
)

# ---------------------------------------------------------------------------- 比 and 有
L_P3_BI = lesson(
    "The book’s patterns: 比, 没有 and 有 … 这么/那么",
    "NP1 比 NP2 + adjective · NP1 没有 NP2 · NP1 有 NP2 那么 + adjective",
    requires=[],
    cards=[
        card("比: patterns",
             "比 indicates different degrees of comparison between two things or persons. Basic: NP1 比 NP2 + adjective; NP1 比 NP2 + VP (of mental verbs). "
             "Negative: NP1 没有 NP2 + VP; NP1 不比 NP2 + VP. Interrogative: NP1 有没有 NP2 + VP？ NP1 比 NP2 + VP？ NP1 有 NP2 + VP 吗？ "
             "In the book some words are in brackets because they may be left out, such as the repeated noun after 比.",
             examples=[D("重庆的雾天比蒙特雷多。", "Chongqing has more foggy days than Monterey."),
                       D("我老家的冬天比北京暖和。", "Winters in my hometown are warmer than in Beijing."),
                       D("我比大卫喜欢夏天。", "I like summer more than David does."),
                       D("他比我们想家。", "He misses home more than we do."),
                       D("蒙特雷的风没有纽约大。", "The wind in Monterey is not as strong as in New York."),
                       D("他不比小王高。", "He is not taller than Xiao Wang."),
                       D("今年的春天风有没有去年的大？", "Is the wind this spring as strong as last year’s?"),
                       D("今天的气温比昨天的高吗？", "Is today’s temperature higher than yesterday’s?"),
                       D("你老家的夏天有上海热吗？", "Is summer in your hometown as hot as in Shanghai?")]),
        card("有: the same degree, with a high standard",
             "Unlike 跟 … 一样, which also shows identical comparison, NP1 有 NP2 (这/那么) + adjective suggests the speaker regards the degree of NP2 as high. "
             "Basic: NP1 有 NP2 (这/那么) + adjective. Negative: NP1 没有 NP2 (这/那么) + adjective. Questions: … 吗？ and … 有没有 …？",
             examples=[D("纽约的夏天有华盛顿的夏天那么热。", "Summer in New York is as hot as summer in Washington."),
                       D("我有我妹妹那么爱看书。", "I like reading as much as my younger sister does."),
                       D("上海的冬天没有北京的冬天那么冷。", "Winter in Shanghai is not as cold as winter in Beijing."),
                       D("上海的冬天有北京的冬天那么冷吗？", "Is winter in Shanghai as cold as winter in Beijing?"),
                       D("上海的冬天有没有北京的冬天那么冷？", "Is winter in Shanghai as cold as winter in Beijing? (verb-not-verb form)")]),
        card("Activities 4 to 8 in the book",
             "Activity 4: listen to two brothers talk about the weather and fill in their opinions and reasons; the new word is 锻炼 (duànliàn, exercise). "
             "Activity 5: interview a classmate with at least five questions about how their hometown differs from Monterey in size, population and weather, e.g. 你的老家人口比蒙特雷多吗？, then write a short paragraph beginning …在美国的…部/…州。…有…人口，比蒙特雷…。 "
             "Activity 7: complete five sentences with comparison constructions: 今天的气温…昨天的气温差不多。 今天早上的风…昨天早上的风…。 今天晚上的天气…今天早上的天气…。 今天早上的风…今天晚上的风…。 晚上的气温…早上的气温…。 "
             "Activity 8: use a weather report to finish eight sentences beginning 上海的气温比…, 西安的气温没有…, 北京的气温跟…, 台北的气温比…, 香港跟北京一样…, 南京的天气一样都有小雨, 香港的气温不一样, 西安的气温…高。"),
        card("Weather report (Activity 8)",
             "中国部分主要城市天气预报: the book’s table of eight cities. 晴 is sunny, 阴 cloudy, 小雨 light rain, 中雨 moderate rain, 大雨 heavy rain.",
             tables=[table(["City", "Weather", "Temperature (°C)"],
                           [["北京", "晴", "20 – 30"], ["天津", "小雨", "22 – 30"], ["上海", "中雨", "26 – 29"], ["南京", "小雨", "23 – 26"],
                            ["重庆", "阴", "21 – 29"], ["西安", "阴", "20 – 27"], ["香港", "晴", "27 – 31"], ["台北", "大雨", "25 – 28"]], say=[0])]),
    ],
    exercises=[
        M("What does 重庆的雾天比蒙特雷多 say?", "Chongqing has more foggy days than Monterey.", ["Monterey has more foggy days.", "Both have the same fog.", "Chongqing is foggier than Shanghai."], "比 … 多."),
        M("What does 我比大卫喜欢夏天 say?", "I like summer more than David does.", ["David likes summer more.", "I like David.", "We both like summer."], "NP1 比 NP2 + mental verb."),
        M("What does 蒙特雷的风没有纽约大 say?", "Monterey’s wind is not as strong as New York’s.", ["Monterey’s wind is stronger.", "They have the same wind.", "New York has no wind."], "没有 … 大."),
        M("What does 他不比小王高 say?", "He is not taller than Xiao Wang.", ["He is shorter than Xiao Wang.", "He is taller.", "He is Xiao Wang."], "不比 denies the comparison."),
        M("What does 今天的气温比昨天的高吗？ ask?", "Is today’s temperature higher than yesterday’s?", ["Is it hot today?", "What was yesterday’s temperature?", "Is it warm?"], "比 … 高吗."),
        M("What does 你老家的夏天有上海热吗？ ask?", "Is summer in your hometown as hot as in Shanghai?", ["Does your hometown have Shanghai?", "Is Shanghai hotter?", "Where is your hometown?"], "有 … 热吗."),
        M("What does 纽约的夏天有华盛顿的夏天那么热 say?", "Summer in New York is as hot as in Washington.", ["New York is cooler than Washington.", "Washington is hotter.", "New York has no summer."], "有 … 那么 + adjective."),
        M("What does 我有我妹妹那么爱看书 say?", "I like reading as much as my sister.", ["My sister likes reading less.", "I do not like reading.", "I have a sister who reads."], "有 … 那么."),
        M("Which sentence is the verb-not-verb question?", "上海的冬天有没有北京的冬天那么冷？", ["上海的冬天有北京的冬天那么冷吗？", "上海的冬天比北京的冬天冷。", "上海的冬天没有北京的冬天那么冷。"], "有没有."),
        M("In the weather report, which city is sunny with the highest temperature range (27–31 °C)?", "香港", ["北京", "天津", "台北"], "香港 晴 27–31."),
        M("In the weather report, which city has heavy rain?", "台北", ["上海", "天津", "南京"], "台北 大雨."),
        M("In the weather report, which city has moderate rain?", "上海", ["南京", "天津", "重庆"], "上海 中雨."),
        M("Which two cities are both cloudy?", "重庆 and 西安", ["北京 and 香港", "天津 and 南京", "上海 and 台北"], "重庆 阴, 西安 阴."),
        M("Which two cities both have light rain?", "天津 and 南京", ["北京 and 西安", "上海 and 台北", "重庆 and 香港"], "天津 小雨, 南京 小雨."),
        M("In the weather report, which city is sunny with 20–30 °C?", "北京", ["上海", "南京", "台北"], "北京 晴 20 – 30."),
        mean("锻炼", "duan4lian4", "to exercise", ["to rest", "to practise", "to sleep"]),
        F("重庆的雾天___蒙特雷多。", "比", PART, "比.", tr="Chongqing has more foggy days than Monterey."),
        F("蒙特雷的风___有纽约大。", "没", PART, "没有.", tr="Monterey’s wind is not as strong as New York’s."),
        F("上海的冬天___没有北京的冬天那么冷？", "有", PART, "有没有.", tr="Is winter in Shanghai as cold as winter in Beijing?"),
    ],
)

# ---------------------------------------------------------------------------- 可是, 好+verb, temperature
L_P3_MORE = lesson(
    "The book’s notes: 可是, 好 + verb and temperature conversion",
    "蒙特雷不太大，可是很美 · 好说 好学 好听 · 摄氏度 华氏度",
    requires=[],
    cards=[
        card("The conjunction 可是",
             "可是 is like “but” and connects two clauses: Clause 1 + 可是 + Clause 2.",
             examples=[D("我老家的冬天很冷，可是可以滑雪。", "Winter in my hometown is very cold, but you can ski."),
                       D("蒙特雷不太大，可是很美。", "Monterey is not very big, but it is very beautiful.")]),
        card("Activities 9 and 10: 可是 practice",
             "Activity 9: write the opposite idea after 可是: 蒙特雷的风景很美，可是…… 我很喜欢中文，可是…… 纽约是美国最有名的城市，可是…… 加州的天气很好，可是…… "
             "Activity 10: one partner says five negative things about Monterey and life here, for example 中文很难。 The other answers with the positive side after 可是, for example 可是，中文很有用。",
             examples=[D("蒙特雷的风景很美。", "The scenery in Monterey is very beautiful."),
                       D("纽约是美国最有名的城市。", "New York is the most famous city in the U.S."),
                       D("中文很难。", "Chinese is hard."),
                       D("可是，中文很有用。", "But Chinese is very useful.")]),
        card("“好 + verb” as an adjective",
             "好 and a verb can form an adjective meaning “pleasant to …” or “easy to …”. 好看 means pleasant to look at, good-looking; 好说 means easy to say. Activity 11 asks for the meanings of 好说, 好学, 好听, 好玩, 好吃.",
             tables=[wtable([("好说", "hao3shuo1", "easy to say"), ("好学", "hao3xue2", "easy to learn"), ("好听", "hao3ting1", "pleasant to hear"), ("好玩", "hao3wan2", "fun"), ("好吃", "hao3chi1", "delicious"), ("好看", "hao3kan4", "pleasant to look at")])]),
        card("Skill Integration: temperatures in two scales",
             "In the book you listen to a dialog about today’s temperature in Monterey and Xi’an in Fahrenheit and Celsius. Here is the conversion from Activity 2. "
             "°F = °C × 1.8 + 32 and °C = (°F − 32) ÷ 1.8. Read 1.8 as 一点八 (yī diǎn bā). For example, 30 °C: 30 × 1.8 = 54, 54 + 32 = 86, so 30 °C is 86 °F. "
             "Practice: 海南省夏天最高气温有三十五点九摄氏度。三十五点九摄氏度是多少华氏度？ 35.9 × 1.8 = 64.62, 64.62 + 32 = 96.62, so it is 96.62 °F. "
             "Common conversions: 0 °C = 32 °F; 37 °C = 98.6 °F; 38 °C = 100.4 °F; 39 °C = 102.2 °F; 40 °C = 104 °F; 100 °C = 212 °F.",
             tables=[table(["°C", "°F"], [["0", "32"], ["37", "98.6"], ["38", "100.4"], ["39", "102.2"], ["40", "104"], ["100", "212"]])],
             examples=[D("海南省夏天最高气温有三十五点九摄氏度。", "The highest temperature in summer in Hainan is 35.9 degrees Celsius."),
                       D("三十五点九摄氏度是多少华氏度？", "How many degrees Fahrenheit is 35.9 degrees Celsius?")]),
    ],
    exercises=[
        M("What does 蒙特雷不太大，可是很美 say?", "Monterey is not very big, but it is very beautiful.", ["Monterey is big and beautiful.", "Monterey is big, so it is beautiful.", "Monterey is not beautiful."], "可是 is but."),
        M("What does 我老家的冬天很冷，可是可以滑雪 say?", "Winter in my hometown is cold, but you can ski.", ["Winter is cold, so you cannot ski.", "Winter is warm.", "It never snows."], "可是 is but."),
        M("Which is a good answer after “中文很难”?", "可是，中文很有用。", ["所以，中文很难。", "因为，中文很难。", "也，中文很难。"], "可是 introduces the positive side."),
        M("What does 好说 mean?", "easy to say", ["easy to eat", "easy to learn", "fun"], "好 + 说."),
        M("What does 好学 mean?", "easy to learn", ["easy to say", "pleasant to hear", "delicious"], "好 + 学."),
        M("What does 好听 mean?", "pleasant to hear", ["easy to learn", "fun", "delicious"], "好 + 听."),
        M("What does 好玩 mean?", "fun", ["delicious", "pleasant to hear", "easy to say"], "好 + 玩."),
        M("What does 好吃 mean?", "delicious", ["fun", "easy to learn", "pleasant to hear"], "好 + 吃."),
        M("°F = ?", "°C × 1.8 + 32", ["°C × 1.8 − 32", "(°C − 32) ÷ 1.8", "°C × 5 ÷ 9"], "°F = °C x 1.8 + 32."),
        M("°C = ?", "(°F − 32) ÷ 1.8", ["°F × 1.8 + 32", "°F × 1.8 − 32", "(°F + 32) ÷ 1.8"], "°C = (°F − 32) ÷ 1.8."),
        M("30 °C in Fahrenheit is…", "86 °F", ["54 °F", "98.6 °F", "62 °F"], "30 × 1.8 + 32 = 86."),
        M("35.9 °C in Fahrenheit is…", "96.62 °F", ["64.62 °F", "68.0 °F", "99.6 °F"], "35.9 × 1.8 = 64.62; + 32 = 96.62."),
        M("37 °C in Fahrenheit is…", "98.6 °F", ["100.4 °F", "37.6 °F", "86 °F"], "37 × 1.8 + 32 = 98.6."),
        M("40 °C in Fahrenheit is…", "104 °F", ["72 °F", "100.4 °F", "102.2 °F"], "40 × 1.8 + 32 = 104."),
        M("100 °C in Fahrenheit is…", "212 °F", ["180 °F", "132 °F", "100 °F"], "100 × 1.8 + 32 = 212."),
        M("How do you read 1.8?", "一点八", ["一八点", "点一八", "一点点八"], "一点八."),
        F("蒙特雷不太大，___是很美。", "可", PART, "可是.", tr="Monterey is not very big, but it is very beautiful."),
        F("这首歌很好___。 (nice to hear)", "听", PART, "好听.", tr="This song is nice to listen to."),
    ],
)

# ---------------------------------------------------------------------------- Kunming + forecasts
L_P3_KUNMING = lesson(
    "Reading: Kunming, the Spring City",
    "昆明又叫春城 · 平均气温二十一摄氏度 · 天气预报",
    requires=[],
    cards=[
        card("Reading (Skill Integration, Activity 3)",
             "Read about Kunming and answer the questions. New words: 昆明 (Kūnmíng), 干 (gān, dry), 回 (huí, to go back). Numbers in the book are digits and are written out here: 21, 29, 10 and −2.",
             examples=[D("周老师的老家在云南省昆明市。", "Teacher Zhou’s hometown is Kunming, Yunnan Province."),
                       D("云南省在中国的西南部，昆明是云南省的省会。", "Yunnan Province is in the southwest of China, and Kunming is its capital."),
                       D("昆明一年四季都跟春天一样，所以昆明又叫“春城”。", "All four seasons in Kunming are like spring, so Kunming is also called the “Spring City”."),
                       D("昆明的春天天气暖和，很少下雨，所以气候很干。", "Spring in Kunming is warm and it rarely rains, so the climate is very dry."),
                       D("夏天没有非常热的天气，但是下很多雨。", "In summer there is no extremely hot weather, but it rains a lot."),
                       D("夏天平均气温二十一摄氏度左右，最高气温二十九摄氏度左右。", "The average summer temperature is about 21 degrees Celsius, and the highest is about 29."),
                       D("秋天不太凉，很少下雨。", "Autumn is not too cool and it rarely rains."),
                       D("冬天也没有非常冷的天气，晴天很多，平均气温十摄氏度左右，最低气温零下二摄氏度左右。", "Winter has no extremely cold weather either, with many sunny days; the average temperature is about 10 degrees Celsius and the lowest is about minus 2."),
                       D("冬天和春天、秋天一样，没有很多雨。", "Winter, like spring and autumn, does not have a lot of rain."),
                       D("周老师非常喜欢昆明的气候，她常常回老家看父母。", "Teacher Zhou likes the climate of Kunming very much and often goes back to her hometown to see her parents.")]),
        card("Questions in the book (Activity 3, B and C)",
             "Take turns asking and answering: 1. 昆明春天的天气怎么样？ 2. 夏天很热吗？夏天的平均气温是多少？ 3. 秋天很凉快吗？你怎么知道的？ 4. 冬天的天气怎么样？最低气温是多少？ 5. 昆明什么季节雨最多？ "
             "Then read a weather report on Kunming (a table in the book) and find: 1. 昆明哪个月最暖和？气温是多少？ 2. 哪个月最冷？气温是多少？ 3. 哪个月雨最多？下多少雨？",
             examples=[D("昆明春天的天气怎么样？", "How is the weather in Kunming in spring?"),
                       D("夏天很热吗？夏天的平均气温是多少？", "Is summer hot? What is the average temperature in summer?"),
                       D("秋天很凉快吗？你怎么知道的？", "Is autumn cool? How do you know?"),
                       D("冬天的天气怎么样？最低气温是多少？", "How is the weather in winter? What is the lowest temperature?"),
                       D("昆明什么季节雨最多？", "In which season does it rain the most in Kunming?")]),
        card("Forecast questions (Activity 4)",
             "Student A reads the weather forecast of Guangzhou and Student B that of Changchun (they are pictures in the book). Both answer: 1. 今天广州气温多少度？ 2. 今天阴天还是晴天？ 3. 今天最高气温是多少？ 4. 今天最低气温是多少？ 5. 今天风大不大？ "
             "The same five questions are asked about 长春.",
             examples=[D("今天广州气温多少度？", "What is the temperature in Guangzhou today?"),
                       D("今天阴天还是晴天？", "Is it cloudy or sunny today?"),
                       D("今天最高气温是多少？", "What is the highest temperature today?"),
                       D("今天最低气温是多少？", "What is the lowest temperature today?"),
                       D("今天风大不大？", "Is the wind strong today?")]),
    ],
    exercises=[
        M("Where is Kunming?", "In Yunnan, in the southwest of China", ["In Sichuan", "In Jilin", "In Texas"], "云南省在中国的西南部."),
        M("Why is Kunming called the Spring City?", "All four seasons there are like spring", ["It has a spring festival", "It always rains in spring", "It is very cold"], "一年四季都跟春天一样."),
        M("Why is the climate in Kunming dry in spring?", "It is warm and rarely rains", ["It snows", "It rains every day", "It is windy"], "很少下雨，所以气候很干."),
        M("What is the average summer temperature in Kunming?", "About 21 °C", ["About 10 °C", "About 29 °C", "About −2 °C"], "二十一摄氏度左右."),
        M("What is the highest summer temperature in Kunming?", "About 29 °C", ["About 21 °C", "About 43 °C", "About 10 °C"], "二十九摄氏度左右."),
        M("What is the average winter temperature in Kunming?", "About 10 °C", ["About 21 °C", "About −2 °C", "About 29 °C"], "十摄氏度左右."),
        M("What is the lowest winter temperature in Kunming?", "About minus 2 °C", ["About minus 10 °C", "About 0 °C", "About 10 °C"], "零下二摄氏度左右."),
        M("Does Kunming have a lot of rain in winter?", "No", ["Yes", "Only in autumn", "It always snows"], "没有很多雨."),
        M("What does Teacher Zhou often do?", "Go back to her hometown to see her parents", ["Ski in Beijing", "Swim in Texas", "Teach in Monterey"], "常常回老家看父母."),
        M("In which season does it rain a lot in Kunming?", "Summer", ["Winter", "Spring", "Autumn"], "夏天下很多雨."),
        mean("春城", "chun1cheng2", "Spring City", ["a spring", "a summer city", "Beijing"]),
        mean("干", "gan1", "dry", ["wet", "cold", "windy"]),
        mean("回", "hui2", "to go back", ["to go away", "to look", "to ask"]),
        F("昆明一年四季都跟春天一___。", "样", PART, "一样.", tr="All four seasons in Kunming are like spring."),
        F("昆明又叫“春___”。", "城", PART, "春城.", tr="Kunming is also called the “Spring City”."),
        F("今天阴天___是晴天？", "还", PART, "还是.", tr="Is it cloudy or sunny today?"),
    ],
)

# ---------------------------------------------------------------------------- scenarios
L_P3_TASKS = lesson(
    "Presentation 3 speaking tasks",
    "Monterey weather · coffee shop conversation · San Francisco and San Jose",
    requires=[],
    cards=[
        card("Activity 1 (Using Chinese in Context): the coffee shop",
             "You are studying at a coffee shop in downtown Monterey and a Chinese tourist is drinking coffee next to you. Greet the person and ask how they like the weather in Monterey compared with the weather in their hometown. "
             "Share your impression too. Pair up and exchange: your hometown; the weather in your hometown; the highest temperature in summer; the lowest temperature in winter; a comparison with the weather in Monterey. "
             "Use the table in the book to note your partner’s information (你老家的天气和气温与蒙特雷的比较 and 中国游客老家的天气和气温与蒙特雷的比较), then summarize and report it to the class.",
             examples=[D("你们老家的天气跟蒙特雷的一样吗？", "Is the weather in your hometown the same as in Monterey?"),
                       D("夏天最高气温是多少？", "What is the highest temperature in summer?"),
                       D("冬天最低气温是多少？", "What is the lowest temperature in winter?")]),
        card("Activity 2: a field trip",
             "Your class plans a field trip to a Chinese community in the Bay Area. Your teacher asks you to find the temperature and weather in San Francisco and San Jose and to recommend a destination. "
             "Group A prepares a weather report on San Francisco and Group B one on San Jose. Discuss: how many seasons; the weather in different seasons; which season is best and which is not good; the high temperature in the day and the low temperature at night; "
             "a comparison with the other city; and good places to eat and have fun. Write a group report, present it, and let the class and the teacher vote for the best place."),
    ],
    exercises=[
        M("Which question compares the weather where you are from with Monterey?", "你们老家的天气跟蒙特雷的一样吗？", ["你们老家有几个人？", "你们老家在哪儿？", "你们老家的人口多少？"], "跟 … 一样吗."),
        M("Which asks for the highest summer temperature?", "夏天最高气温是多少？", ["冬天最低气温是多少？", "夏天雨多不多？", "春天风大不大？"], "最高气温."),
        M("Which asks for the lowest winter temperature?", "冬天最低气温是多少？", ["夏天最高气温是多少？", "冬天下雪吗？", "秋天凉快吗？"], "最低气温."),
        mean("气温", "qi4wen1", "air temperature", ["climate", "weather", "season"]),
        mean("最高", "zui4gao1", "the highest", ["the lowest", "higher", "tall"]),
        mean("最低", "zui4di1", "the lowest", ["the highest", "lower", "short"]),
    ],
)

UNIT = unit("第五课 The book’s texts: climate and comparing", [L_P3_READINGS, L_P3_YIYANG, L_P3_BI, L_P3_MORE, L_P3_KUNMING, L_P3_TASKS])
