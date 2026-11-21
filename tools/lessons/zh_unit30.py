"""Unit 30: Lesson 10 (Housing and Rentals) Presentation 3 and Area Studies, from the book's texts: the family house, position words,
the particle 着, the savings article, the housing vocabulary and "Housing Conditions and Infrastructure in China".
Audio, pictures, maps, videos and web pages are not included."""
from zh_auto import *
from zh_l10_vocab import VOC3

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]
ZH4 = {"种": "zhong4"}

# ------------------------------------------------------------------ 1. the house
HOUSE = [
    "我父母的房子在纽约州的一个小城市，是一个两层楼的房子。大门在房子的中间，两边都有一个大窗户。",
    "进了大门，你会看见一个客厅。客厅里摆着一张三人沙发，沙发前面是一张咖啡桌。客厅右边是厨房，厨房旁边是饭厅。饭厅里有一张饭桌和六把椅子。书房在客厅后面，书房对面是卫生间。",
    "楼上有三个卧室。中间的主卧室是我父母的房间，里面放着一张双人床，两个床头柜，还有一个很大的衣橱。主卧室的左边是我妹妹的卧室，右边是我的卧室。我父母的房子还有一个地下室和一个车库。",
    "房子的前院是个小花园。后院种着很多果树，还有一个菜园。",
]
HOUSE_E = [
    "My parents’ house is in a small city in New York State; it is a two-story house. The front door is in the middle of the house, with a big window on each side.",
    "Going in through the front door, you will see a living room. In the living room is a three-person sofa, and in front of the sofa is a coffee table. To the right of the living room is the kitchen, and next to the kitchen is the dining room. In the dining room are a dining table and six chairs. The study is behind the living room, and across from the study is the bathroom.",
    "Upstairs are three bedrooms. The master bedroom in the middle is my parents’ room; in it are a double bed, two nightstands and a very big closet. To the left of the master bedroom is my younger sister’s bedroom, and to the right is mine. My parents’ house also has a basement and a garage.",
    "The front yard of the house is a small garden. The backyard is planted with many fruit trees, and there is also a vegetable garden.",
]
Q4 = [("房子在哪儿？有几层？", "Where is the house? How many floors?"), ("客厅里有什么？", "What is in the living room?"), ("厨房在哪儿？里面有什么？", "Where is the kitchen? What is in it?"), ("饭厅在哪儿？里面有什么？", "Where is the dining room? What is in it?"),
      ("有几个卧室？卧室在哪儿？", "How many bedrooms? Where are they?"), ("有没有地下室？有没有车库？", "Is there a basement? Is there a garage?"), ("有前院和后院吗？院子里有什么？", "Is there a front yard and a backyard? What is in the yard?")]
L1 = lesson(
    "Lesson 10 Presentation 3: my parents’ house (passage)",
    "两层楼的房子 · 客厅里摆着一张三人沙发 · 后院种着很多果树",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. Where do your parents live? How many floors does their house have? B. What do you like about their home? Is there anything special about it? C. Do you have memories of your childhood home?"),
        card("Presentation 3: 我父母的房子",
             "The book also prints the passage in traditional characters (for example 我父母的房子在紐約州的一個小城市).",
             examples=[D(z, e, fixes=ZH4) for z, e in zip(HOUSE, HOUSE_E)]),
        card("Activities 1 to 4",
             "Activity 1. A. Listen to Presentation 3 and summarize it aloud (audio, not included). B. Listen again and write, in characters or pinyin, the names of the items pictured; fill in the house diagram with the room types and the furniture mentioned (pictures, not included). C. In Chinese, compare your work with a partner. Activity 2. A. Listen to a description of David’s house and label the rooms and the furniture on a layout of upstairs (楼上) and downstairs (楼下) (audio, not included). B. Describe the upstairs to a partner while they describe the downstairs. Activity 3. Pair up. On the map, write the name of each building or geographical feature in pinyin or characters (a hospital, a mountain, a furniture store, a restaurant, a cinema, a gym, a library; the map is not included), then write a description of the location of four places using 左边, 右边, 旁边, 对面, 前面, 后面 and 中间. The book’s example is 体育馆在图书馆的前面，饭馆的对面 (the gym is in front of the library and across from the restaurant). B. Share your work with the class. Activity 4. A. Pair up and tell your partner about where you live, using these questions as a guide. B. Write your partner’s description of their housing in pinyin or characters. C. Check your partner’s notes and correct any inaccuracies.",
             examples=[D("体育馆在图书馆的前面，饭馆的对面。", "The gym is in front of the library and across from the restaurant.")] + [D(z, e) for z, e in Q4]),
    ],
    exercises=[
        M("Where is the house?", "In a small city in New York State", ["In Beijing", "On a farm", "In a big city"], "纽约州的一个小城市。"),
        M("How many floors does it have?", "Two", ["One", "Three", "Four"], "两层楼的房子。"),
        M("Where is the front door?", "In the middle of the house", ["On the left", "At the back", "On the second floor"], "大门在房子的中间。"),
        M("What is in front of the sofa?", "A coffee table", ["A TV", "A desk", "A bookshelf"], "沙发前面是一张咖啡桌。"),
        M("Where is the kitchen?", "To the right of the living room", ["To the left of the living room", "Upstairs", "Behind the study"], "客厅右边是厨房。"),
        M("What is next to the kitchen?", "The dining room", ["The study", "The garage", "The bathroom"], "厨房旁边是饭厅。"),
        M("How many chairs are in the dining room?", "Six", ["Two", "Four", "Eight"], "一张饭桌和六把椅子。"),
        M("Where is the study?", "Behind the living room", ["Upstairs", "In the basement", "In front of the sofa"], "书房在客厅后面。"),
        M("What is across from the study?", "The bathroom", ["The kitchen", "The garage", "The living room"], "书房对面是卫生间。"),
        M("How many bedrooms are upstairs?", "Three", ["Two", "One", "Four"], "楼上有三个卧室。"),
        M("Whose room is in the middle upstairs?", "His parents’", ["His sister’s", "His own", "A guest’s"], "中间的主卧室是我父母的房间。"),
        M("Where is the sister’s bedroom?", "To the left of the master bedroom", ["To the right of the master bedroom", "Downstairs", "In the basement"], "主卧室的左边是我妹妹的卧室。"),
        M("What is in the backyard?", "Many fruit trees and a vegetable garden", ["A swimming pool", "A garage", "A small garden only"], "后院种着很多果树，还有一个菜园。"),
        M("What is the front yard?", "A small garden", ["A vegetable garden", "A garage", "A parking lot"], "前院是个小花园。"),
        F("客厅里摆___一张三人沙发。", "着", PART, "摆着: is placed."),
        F("饭厅里有一张饭桌和六___椅子。", "把", PART, "把 is the measure word for chairs."),
        F("我父母的房子还有一个地下室和一个___库。", "车", PART, "车库: garage."),
    ],
)

# ------------------------------------------------------------------ 2. position words
POS = [("左边", "left side"), ("右边", "right side"), ("里边", "inside"), ("外边", "outside"), ("上边", "top, above"), ("下边", "bottom, below"), ("前边", "front"), ("后边", "back"), ("中间", "middle"), ("对面", "opposite; across from"),
       ("左面", "left"), ("右面", "right"), ("里面", "inside"), ("外面", "outside"), ("上面", "above"), ("下面", "below"), ("前面", "in front"), ("后面", "behind")]
POSX = [("我家房子的前边有一家商店。", "There is a store in front of my house. (subject)"), ("日本饭馆在那个大楼的后面。", "The Japanese restaurant is at the back of that building. (object)"), ("左边的那张桌子是我的。", "The desk on the left is mine. (attributive)"), ("对面的那个大楼是中国银行。", "The building opposite is the Bank of China. (attributive)")]
POSN = [("桌子上边", "on top of the table"), ("医院对面", "opposite of the hospital"), ("厨房右边", "to the right of the kitchen"), ("书房和客厅中间", "in the middle of the study and the living room")]
POS2 = [("房子的右边", "the right side of the house"), ("右边的房子", "the house on the right")]
L2 = lesson(
    "Lesson 10 Presentation 3 grammar: the position words 左边 右边 旁边 中间 前面 后面 对面 里面",
    "桌子上边 · 医院对面 · 厨房右边 · 房子的右边 / 右边的房子",
    requires=[],
    cards=[
        card("The position words",
             "Many position words are formed by attaching the suffix 边 or 面 to directional words like 左/右, 里/外, 上/下 or 前/后. You may also place a noun immediately before a position word to further specify its position, for example 厨房左边 or 学校前面. The book’s table: 左, 右, 里, 外, 上, 下, 前, 后 + 边 or 面, and 中间 and 对面 by themselves.",
             tables=[wtable(rows_py(POS), title="Position words")]),
        card("Position words as subjects, objects and attributives",
             "Position words can be subjects, objects or attributives. A position word specifies a location with a reference point. Chinese positional order is the reverse of English: Noun + Position in Chinese, Position + Noun in English.",
             examples=[D(z, e) for z, e in POSX] + [D(z, e) for z, e in POSN]),
        card("Modifier before the element it modifies",
             "In Chinese a modifier always comes before the element it modifies. It is the same for position words when they modify a noun. In 房子的右边 (the right side of the house) 右边 is a noun, while in 右边的房子 (the house on the right) it is an adjective.",
             examples=[D(z, e) for z, e in POS2]),
        card("Activities 1 to 3",
             "Activity 1. A. Listen to the audio and draw in your notebook a layout of the university described (Xiamen University, 厦门大学; audio and picture not included). B. Compare layouts with a partner, then use position words to discuss the location of your class building and its surroundings. Activity 2 (Reading and Writing). Pair up and, from the images (not included), complete the sentences with position words: 这是我的老家 (图书馆, 学校, 医院, 电影院 …); the five presidents 老布什, 奥巴马, 小布什, 克林顿 and 卡特 (小布什, 老布什, 卡特 …); and 这是小明的卧室 (小明的床, 床头柜, 闹钟, 室内植物, 地毯 …). Activity 3. A. Complete the sentences from the seating picture of 大卫, 张文, 李红, 琳达, 林东, 王英, 夏冬 and 白雪; the book starts with 白雪坐在王英的左边, and then 林东, 王英, 大卫 and 张文 … B. Compare sentences with a partner. C. Take turns describing your classmates’ seating with 左边, 右边, 旁边, 中间, 前面, 后面 and/or 对面.",
             examples=[D("这是我的老家。", "This is my hometown."), D("白雪坐在王英的左边。", "Bai Xue sits to the left of Wang Ying."), D("这是小明的卧室。", "This is Xiao Ming’s bedroom.")]),
    ],
    exercises=[
        M("What are 边 and 面 attached to?", "Directional words like 左/右, 里/外, 上/下, 前/后", ["Verbs", "Measure words", "Numbers"], "左边, 前面…"),
        M("What does 左边 mean?", "Left side", ["Right side", "Middle", "Opposite"], "左边."),
        M("What does 对面 mean?", "Opposite; across from", ["Behind", "Next to", "Inside"], "对面."),
        M("What does 中间 mean?", "Middle", ["Left side", "Front", "Outside"], "中间."),
        M("What does 医院对面 mean?", "Opposite the hospital", ["Behind the hospital", "Inside the hospital", "A hospital’s face"], "Noun + position."),
        M("What does 厨房右边 mean?", "To the right of the kitchen", ["To the left of the kitchen", "Inside the kitchen", "In front of the kitchen"], "Noun + position."),
        M("What does 桌子上边 mean?", "On top of the table", ["Under the table", "Beside the table", "In front of the table"], "上边: top."),
        M("What does 房子的右边 mean?", "The right side of the house", ["The house on the right", "The right house", "A house on the right side"], "Modified noun."),
        M("What does 右边的房子 mean?", "The house on the right", ["The right side of the house", "The right of the house", "Beside the house"], "右边 is the attributive."),
        M("Which sentence uses a position word as an attributive?", "左边的那张桌子是我的。", ["我家房子的前边有一家商店。", "日本饭馆在那个大楼的后面。", "医院在学校对面。"], "左边的 + noun."),
        M("Which sentence uses a position word as the subject?", "我家房子的前边有一家商店。", ["左边的那张桌子是我的。", "日本饭馆在那个大楼的后面。", "对面的那个大楼是银行。"], "前边 is the subject."),
        M("How does the Chinese positional order compare to English?", "Reversed: noun + position", ["Identical", "Position + noun", "No order"], "桌子上边 = on top of the table."),
        F("日本饭馆在那个大楼的___面。", "后", PART, "后面: behind."),
        F("书房和客厅___间", "中", PART, "中间: in the middle."),
        F("体育馆在图书馆的前面，饭馆的___面。", "对", PART, "对面: across from."),
    ],
)

# ------------------------------------------------------------------ 3. 着
ZH1 = [("客厅里摆着一张三人沙发。", "There is a three-person sofa in the living room."), ("主卧室里放着一张双人床。", "There is a double bed in the master bedroom."), ("院子里种着很多花和果树。", "Many flowers and fruit trees are planted in the yard.")]
ZH2 = [("他的电脑在开着。", "His computer is on."), ("你手里拿着什么书？", "What book are you holding?"), ("马克今天穿着一件蓝色衬衫。", "Mark is wearing a blue shirt today."), ("琳达躺着在沙发上看电视。", "Linda is lying on the couch watching TV.")]
ZH3 = [("王老师喜欢坐着讲课。", "Professor Wang likes to sit while teaching."), ("大卫喜欢站着看书。", "David likes to stand while reading.")]
ZHA4 = [("甲：琳达，你这个公寓里住着几个人？", "Linda, how many people live in this apartment of yours?"), ("乙：一共三个人，我，珍妮和玛丽。", "Three people altogether: me, Jenny and Mary."), ("甲：你们的客厅里都有什么家具？", "What furniture do you have in your living room?"), ("乙：客厅里放着一个沙发，两把椅子，和一张咖啡桌。", "In the living room are a sofa, two chairs and a coffee table."),
        ("甲：你们的厨房和饭厅大不大？", "Are your kitchen and dining room big?"), ("乙：不太大。厨房旁边摆着一张饭桌和三把椅子，就是我们吃饭的地方。", "Not very. Beside the kitchen are a dining table and three chairs; that’s where we eat."), ("甲：这个公寓有车库吗？", "Does this apartment have a garage?"), ("乙：有，可是只有一个停车位。现在车库停着珍妮的车。", "Yes, but there is only one parking space. Right now Jenny’s car is parked in the garage.")]
ZHS = [("他手里拿着咖啡。", "He is holding a coffee in his hand."), ("这个客厅里摆着一个沙发，地毯和电视。", "In this living room are a sofa, a carpet and a TV."), ("她在办公室坐着打电话。", "She sits in the office making a phone call."), ("她在办公室坐着写字。", "She sits in the office writing.")]
L3 = lesson(
    "Lesson 10 Presentation 3 grammar: the particle 着",
    "摆着 放着 种着 · 开着 拿着 穿着 躺着 · 坐着讲课 站着看书",
    requires=[],
    cards=[
        card("着 for existence",
             "When used to indicate that something exists in a certain location, 着 pairs with a stative verb to indicate stasis. Pattern: Place + Stative Verb + 着 + Object.",
             examples=[D(z, e, fixes=ZH4) for z, e in ZH1]),
        card("着 as the continuous aspect marker",
             "着 is also the continuous aspect marker, most often used with ongoing or static action verbs like 开, 关, 穿, 戴 and 躺. Pattern: Verb + 着.",
             examples=[D(z, e) for z, e in ZH2]),
        card("着 for the manner of another action",
             "Finally, 着 is used when one action describes the manner or state in which another action is performed. Pattern: Verb 1 + 着 + Verb 2.",
             examples=[D(z, e) for z, e in ZH3]),
        card("Activity 4 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the conversation and complete the transcript in pinyin or characters (audio, not included). B. Pair up and determine whether each 着 in the dialog is an existential or a continuous aspect marker. C. With your partner, write two or more sentences with 着, one expressing existence and one a continuing action or state. D. Read your sentences to the class. The book prints the transcript with blanks; my completion (all the 着 here are existential):",
             examples=[D(z, e, fixes=ZH4) for z, e in ZHA4]),
        card("Activities 5, 6 and 7",
             "Activity 5. Pair up. For each image (not included) use 着 and the words provided to ask and answer questions: 穿 with clothes, pants and shoes; 拿 with a book; 背 with a school bag; a coffee table with 摆 and flowers; the bedroom with 放, a bed, a nightstand and a carpet; the yard with 种, flowers and trees. Write your partner’s answers in the blanks, label each 着 as existential or continuous, and check each other’s work. The book’s example is 这个客厅里摆着什么？ (existential) with the answer 这个客厅里摆着一个沙发，地毯和电视, and 他手里拿着什么？ (continuous) with 他手里拿着咖啡. Activity 6. Take turns describing six pictures with “Verb 1 + 着 + Verb 2”, then write your partner’s descriptions; the example is 她在办公室坐着打电话 / 她在办公室坐着写字. Activity 7 (Speaking and Listening): Guess Who! 猜一猜是谁！ Using 着, describe a classmate’s dress, posture or behavior while the others guess who it is; the first to guess describes another student until everyone has been described.",
             examples=[D(z, e) for z, e in ZHS]),
    ],
    exercises=[
        M("What does 客厅里摆着一张三人沙发 mean?", "There is a three-person sofa in the living room", ["The sofa is being moved", "I have a sofa", "The living room is a sofa"], "Place + stative verb + 着 + object."),
        M("What does 主卧室里放着一张双人床 mean?", "There is a double bed in the master bedroom", ["I am putting a bed in", "The bed was put there yesterday", "The master bedroom is a bed"], "放着: is placed."),
        M("What does 院子里种着很多花和果树 mean?", "Many flowers and fruit trees are planted in the yard", ["I am planting trees", "The yard is a garden", "Flowers have no trees"], "种着: is planted."),
        M("What does 他的电脑在开着 mean?", "His computer is on", ["He is opening the computer", "He turned it off", "He bought a computer"], "开着: is on."),
        M("What does 你手里拿着什么书？ ask?", "What book are you holding?", ["What book did you buy?", "Where is your book?", "Who gave you the book?"], "拿着: holding."),
        M("What does 马克今天穿着一件蓝色衬衫 mean?", "Mark is wearing a blue shirt today", ["Mark bought a blue shirt", "Mark will wear a shirt", "Mark has no shirt"], "穿着: wearing."),
        M("What does 王老师喜欢坐着讲课 mean?", "Professor Wang likes to sit while teaching", ["Professor Wang sat down to teach", "Professor Wang teaches sitting down tomorrow", "Professor Wang is sitting"], "Verb 1 + 着 + verb 2."),
        M("What does 大卫喜欢站着看书 mean?", "David likes to stand while reading", ["David stands to buy books", "David is reading a book", "David does not read"], "站着看书."),
        M("Which use of 着 does 车库停着珍妮的车 have?", "Existence", ["Continuous action", "Manner of another action", "A past event"], "Place + stative verb + 着 + object."),
        M("Which use of 着 does 他手里拿着咖啡 have?", "Continuous state", ["Manner of another action", "Future plan", "Existence in a place"], "拿着: holding."),
        M("Which sentence uses Verb 1 + 着 + Verb 2?", "她在办公室坐着打电话。", ["她手里拿着咖啡。", "客厅里摆着沙发。", "院子里种着花。"], "坐着打电话."),
        F("客厅里摆___一张三人沙发。", "着", PART, "着 after the stative verb."),
        F("主卧室里放___一张双人床。", "着", PART, "放着."),
        F("王老师喜欢坐___讲课。", "着", PART, "坐着讲课."),
        F("马克今天穿___一件蓝色衬衫。", "着", PART, "穿着."),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
ART = [
    "六年前，小李是一个刚毕业的大学生，每个月的工资不到三千元。这些钱要吃饭，租房，还要付别的费用，过年回家还得给父母一些钱，生活非常不容易。",
    "他说：“我租的房子只有八九个平方米，只能放一张床，一个衣橱和一张桌子，没有暖气，也不能做饭，每个月房租二百八十元，我住了六年。”小李还说：“这么便宜的房子现在找不到了，不过，就是因为这么便宜的房租，我才攒了一些钱，去年买了自己的房子。”",
    "关于怎么省钱买房，小李说：“首先，跟房东住在一起或是和同学合租的房子很便宜；另外，没有暖气的房子也不太贵，自己可以买个电暖气，也不用交暖气费；然后，如果公司有食堂，租一个不带厨房的单间也可以。如果你想省钱，最好租这样的房子。”",
]
ART_E = [
    "Six years ago Xiao Li was a recently graduated college student whose salary was less than 3,000 yuan a month. That money had to cover food and rent and other expenses, and at New Year he also had to give his parents some money to go home, so life was not easy.",
    "He said: “The room I rented was only eight or nine square meters, with room for only a bed, a closet and a table; there was no heating and I could not cook; the monthly rent was 280 yuan, and I lived there for six years.” Xiao Li also said: “You can’t find such cheap housing anymore, but it was precisely because of such cheap rent that I was able to save some money, and last year I bought my own house.”",
    "About how to save money to buy a house, Xiao Li said: “First, a place shared with the landlord or rented together with classmates is cheap. Next, a place without heating isn’t too expensive either; you can buy an electric heater yourself and not pay a heating fee. Then, if your company has a cafeteria, renting a single room without a kitchen is fine too. If you want to save money, it’s best to rent this kind of place.”",
]
GLOS = [("毕业", "bi4 ye4", "graduate"), ("工资", "gong1 zi1", "salary"), ("暖气", "nuan3 qi4", "heater"), ("攒", "zan3", "save"), ("省钱", "sheng3 qian2", "save money")]
ADV = [("甲：我们把这个书架放在哪儿？", "Where shall we put this bookshelf?"), ("乙：把它放在窗户旁边，床的对面。", "Put it next to the window, across from the bed.")]
L4 = lesson(
    "Lesson 10 Presentation 3 skill integration: a house layout, arranging furniture, saving for a house",
    "把它放在窗户旁边 · 小李的省钱买房 · 毕业 工资 暖气 攒 省钱",
    requires=[],
    cards=[
        card("Activities 1 and 2",
             "Activity 1. A. Listen to the audio and answer in Chinese: 1. How is the area outside the house described? 2. How is the living room furnished? 3. What is the layout of the first floor? 4. What is the layout of the second floor? 5. How are the basement and garage described? B. Compare answers with a partner and discuss the layout of the house in Chinese. C. Read the script together, then draw a simple layout of the house in your notebooks, labeling each room in Chinese. D. In Chinese, tell your partner how your dream house would be different from this one while your partner drafts a layout of it; check the work for accuracy. E. Present your house layout from C and your dream house layout from D to the class. Activity 2. A. Listen to a monolog about a newly rented apartment and take notes on the layout and how the new occupant plans to furnish it (audio, not included). B. Pair up. Using position words, advise 张文 how best to arrange his new furniture, appliances and decorations in the living room and two bedrooms, in pinyin or characters, with the reasons for your recommendations. The book’s example is below. C. In Chinese, describe to your partner how the furniture in your current home is arranged. D. Share your recommendations to 张文 with the class, then tell the class in Chinese about your partner’s living space and how its furniture is arranged.",
             examples=[D(z, e) for z, e in ADV]),
        card("Activity 3 (Reading, Speaking and Writing): the article about 小李",
             "A. Read the article and summarize it in English. B. Share your summary with a partner. C. In Chinese, discuss the two questions with your partner, then write a strategy for saving money: What do you think of the way Xiao Li saves for a house? If you were him, how would you save money for a house? D. Present your strategy to the class in Chinese. The book glosses 毕业, 工资, 暖气, 攒 and 省钱 in parentheses and prints the figures as digits; the amounts are spelled out here.",
             examples=[D(z, e, fixes={"得": "dei3"}) for z, e in zip(ART, ART_E)],
             tables=[wtable(GLOS, title="Glossed words")]),
    ],
    exercises=[
        M("Where does 张文 put the bookshelf, according to the example?", "Next to the window, across from the bed", ["Behind the door", "In the kitchen", "On the bed"], "把它放在窗户旁边，床的对面。"),
        M("What does 把它放在窗户旁边 mean?", "Put it next to the window", ["Take it out of the window", "Look at the window", "Open the window"], "旁边: beside."),
        M("What was 小李 six years ago?", "A recent college graduate", ["A cook", "A teacher", "A manager"], "刚毕业的大学生."),
        M("About how much was his monthly salary?", "Less than 3,000 yuan", ["More than 30,000 yuan", "280 yuan", "Exactly 3,000 yuan"], "工资不到三千元。"),
        M("How big was the room he rented?", "Eight or nine square meters", ["Eighty square meters", "Eight hundred square meters", "Three square meters"], "只有八九个平方米."),
        M("What could the room hold?", "A bed, a closet and a table", ["A sofa and a TV", "A kitchen", "A bed only"], "只能放一张床，一个衣橱和一张桌子."),
        M("What was the monthly rent?", "280 yuan", ["2,800 yuan", "28 yuan", "3,000 yuan"], "每个月房租二百八十元."),
        M("How long did he live there?", "Six years", ["Two years", "Ten years", "One year"], "我住了六年。"),
        M("What did he do last year?", "Bought his own house", ["Moved to a dorm", "Changed jobs", "Rented a bigger room"], "去年买了自己的房子。"),
        M("Which is NOT one of his money-saving tips?", "Buy a house with a kitchen", ["Live with the landlord or rent with classmates", "Rent a place with no heating and buy an electric heater", "Rent a single room without a kitchen if the company has a cafeteria"], "He says a room without a kitchen is fine."),
        mean("毕业", "bi4 ye4", "graduate", ["salary", "heater", "save money"]),
        mean("工资", "gong1 zi1", "salary", ["graduate", "heater", "save"]),
        mean("暖气", "nuan3 qi4", "heating; heater", ["salary", "graduate", "save money"]),
        mean("省钱", "sheng3 qian2", "save money", ["salary", "graduate", "heater"]),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context
L5 = lesson(
    "Lesson 10 Presentation 3 using Chinese in context: describing a house, renting for a teacher, 蜗居 and 房奴",
    "种着 摆着 放着 · 湾区华人资讯网 · 蜗居 房奴",
    requires=[],
    cards=[
        card("Activity 1 (Speaking and Listening)",
             "A. Pair up. Imagine that you are at MIIS pursuing a degree in Chinese translation and interpretation. A Chinese classmate (your partner) calls you about sharing the house you rent. Describe your house’s layout, furnishings and surroundings to your classmate, using position words and the patterns “Place + 有 + Object” and “Place + 种着/摆着/放着 + Object”. Your partner draws the layout in a notebook from your description. C. Check the accuracy of your partner’s layout, then switch roles and repeat. D. Present your layouts to the class in Chinese."),
        card("Activity 2 (Speaking, Reading, Listening and Writing)",
             "A. Form two groups of three. One of your immersion teachers in Taipei wants to vacation in Monterey for a month with her husband and young daughter, and asks you to find a rental for about $2,000 for the month. Search suitable places on the websites ChineseinSFBay.com (湾区华人资讯网), CCYP.com (分类信息网) and airbnb.com (爱彼迎) (not included). B. Find the best place and fill in a table in Chinese with the questions below. C. Present your group’s selection to the class with your reasons; the class votes which of the two places is the better fit and explains in Chinese. D. As a class, write an email to your Chinese teacher describing your final selection, including its layout, furnishing, amenities, immediate surroundings and local conveniences.",
             examples=[D("房子在哪儿？", "Where is the house?"), D("房子外面什么样？", "What does the outside of the house look like?"), D("房子里面有什么？", "What is inside the house?"), D("每个房间都在哪里？", "Where is each room?"), D("每个房间里都有什么家具？", "What furniture is in each room?"), D("其他好的地方，交通，环境等。", "Other good points: transportation, environment, etc.")]),
        card("Activity 3 (Reading, Speaking and Writing): urban housing issues",
             "A. Pair up for a project on Chinese urban housing issues. Research the terms 蜗居 (wōjū) and 房奴 (fángnú) online and how they relate to housing in China, and write their definitions. B. Watch Episode 1 of the series 蜗居 (“Dwelling Narrowness”, 2009) and write a summary of the episode (the video is not included). C. In Chinese, discuss with your partner whether the U.S. has housing conditions similar to those described by 蜗居. D. Write a short report about urban housing conditions in China and present it to the class in Chinese.",
             tables=[wtable([("蜗居", "wo1 ju1", "tiny cramped dwelling (literally “snail dwelling”)"), ("房奴", "fang2 nu2", "“house slave”: someone whose mortgage eats up their income")], title="Terms to research")]),
    ],
    exercises=[
        M("Which pattern describes things planted in a yard?", "Place + 种着 + object", ["Place + 摆着 + object", "Place + 放着 + object", "Place + 有着 + object"], "种: plant."),
        M("Which pattern describes things placed on a table?", "Place + 摆着 + object", ["Place + 种着 + object", "Place + 看着 + object", "Place + 想着 + object"], "摆: place."),
        M("What is 湾区华人资讯网?", "A website for Chinese people in the Bay Area", ["A bank", "A school", "A TV show"], "湾区华人资讯网 (ChineseinSFBay.com)."),
        M("What does 房子外面什么样？ ask?", "What does the outside of the house look like?", ["Where is the house?", "How much is it?", "Who lives in it?"], "什么样: what kind."),
        mean("蜗居", "wo1 ju1", "tiny cramped dwelling", ["house slave", "garden", "garage"]),
        mean("房奴", "fang2 nu2", "house slave (mortgage-burdened owner)", ["tiny cramped dwelling", "garden", "landlord"]),
        mean("车库", "che1 ku4", "garage", ["basement", "garden", "closet"]),
        mean("地下室", "di4 xia4 shi4", "basement", ["garage", "garden", "closet"]),
    ],
)

# ------------------------------------------------------------------ 6. vocabulary
L6 = vocab_lesson("Lesson 10 Presentation 3 vocabulary", "29 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 7. Area Studies
CITY = [("北京", "Beijing"), ("上海", "Shanghai"), ("广州", "Guangzhou"), ("重庆", "Chongqing"), ("天津", "Tianjin"), ("武汉", "Wuhan"), ("成都", "Chengdu"), ("郑州", "Zhengzhou"), ("西安", "Xi’an")]
L7 = lesson(
    "Lesson 10 Area Studies: housing conditions and infrastructure in China",
    "国家中心城市 · 人口密度 · 人均住房面积 · 高铁",
    requires=[],
    cards=[
        card("Housing conditions and infrastructure in China (1)",
             "Due to China’s large population and land mass, living conditions vary greatly. Currently the world’s most populous country at 1,394,015,977, China’s urban population represents 61.4% of the total (July 2020 est.). Compounding this challenge, China’s overall population density is 153 people per square kilometer, or 397 people per square mile. In comparison, US population density is only 92.9 people per square mile. Living conditions have improved dramatically since economic reforms began in 1978, especially in the large cities and coastal regions. Back then, the floor area per person for urban residents was only 6.7 square meters; it has now risen to 36.9 square meters. Most urban residents live in apartment buildings and some new wealthy residents live in mansions. (The book’s photographs are not included.)"),
        card("Infrastructure and the nine national central cities",
             "Economic reform has greatly improved China’s transportation system and overall infrastructure. By the end of 2019, 40 cities had opened 211 urban rail lines spanning 6,730 kilometers. As of December 2019, the total high-speed rail mileage exceeded 35,000 kilometers and the total mileage of routes operating over 300 kph exceeded 10,000 kilometers, accounting for more than two thirds of all global high speed rail. China now has more than 54,000 three-star or higher hotels, and the addition of many shopping centers, parks and recreational areas has further increased people’s quality of life. In the wake of rapid economic development, nine major “national central cities” (国家中心城市) have emerged in China: Beijing, Shanghai, Guangzhou, Chongqing, Tianjin, Wuhan, Chengdu, Zhengzhou and Xi’an. These metropolises not only play a central role in China’s economic development, they also compose a national grid to strategically drive regional development, compete internationally, and enhance China’s reputation and standing in the world.",
             tables=[wtable(rows_py(CITY), title="国家中心城市")]),
        card("The countryside",
             "While living conditions in the countryside still lag behind those in the cities, the floor area per person of rural residents reached 46.7 square meters in 2017, which is more spacious than that of their urban counterparts. Many rural residents still reside in homes built into caves or made from bamboo, or in yurts and other traditional dwellings. However, economic reforms have allowed some rural areas to prosper, resulting in construction booms with large, modern houses built in traditionally rural and undeveloped areas."),
    ],
    exercises=[
        M("What percentage of China’s population is urban (July 2020 est.)?", "61.4%", ["16.4%", "41.6%", "91.4%"], "61.4% of the total."),
        M("What is China’s overall population density?", "153 people per square kilometer", ["15 people per square kilometer", "1,530 people per square kilometer", "92.9 people per square kilometer"], "153 per sq km, or 397 per sq mile."),
        M("What was the floor area per urban resident before the reforms of 1978?", "6.7 square meters", ["36.9 square meters", "46.7 square meters", "67 square meters"], "Only 6.7 square meters."),
        M("What is the urban floor area per person now?", "36.9 square meters", ["6.7 square meters", "46.7 square meters", "3.7 square meters"], "It has now risen to 36.9."),
        M("How many urban rail lines were open in 40 cities by the end of 2019?", "211", ["21", "2,110", "40"], "211 urban rail lines."),
        M("What share of the world’s high-speed rail does China have?", "More than two thirds", ["About one tenth", "About half", "Less than a quarter"], "More than two thirds."),
        M("How many “national central cities” are there?", "Nine", ["Three", "Seven", "Twelve"], "Nine major national central cities."),
        M("Which city is NOT one of the nine?", "Shenzhen", ["Chengdu", "Wuhan", "Xi’an"], "Shenzhen is not on the book’s list."),
        M("What was the rural floor area per person in 2017?", "46.7 square meters", ["6.7 square meters", "36.9 square meters", "4.7 square meters"], "More spacious than the urban 36.9."),
        mean("成都", "cheng2 du1", "Chengdu", ["Wuhan", "Tianjin", "Beijing"]),
        mean("武汉", "wu3 han4", "Wuhan", ["Chengdu", "Tianjin", "Beijing"]),
        mean("重庆", "chong2 qing4", "Chongqing", ["Chengdu", "Wuhan", "Beijing"]),
    ],
)

UNIT = unit("第十课 租房和住房 Presentation 3: houses, position words, and Area Studies", [L1, L2, L3, L4, L5, L6, L7])
