"""Unit 65: Lesson 22 (Asking for Directions) Presentation 3 and Area Studies from the book's texts: the Beijing Capital International Airport passage,
the activities (terminal terms, questions, the Baiyun Airport passages), simple explanatory text (the house), the skill-integration passages (Pudong and
Hongqiao airports, airport stories), the using-Chinese activities (a living room, the air-travel process), the vocabulary list and the Area Studies
reading on China's tourism. Audio, maps, pictures and links are not included; numbers the book writes as digits are spelled out in the Chinese text;
answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l22_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('干净', 0, 'gan1'), ('长途', 0, 'chang2'), ('行李', 0, 'xing2'), ('还有', 0, 'hai2'), ('还要', 0, 'hai2'), ('还是', 0, 'hai2'), ('银行', 0, 'yin2'), ('银行', 1, 'hang2'), ('中心', 0, 'zhong1'), ('层为', 1, 'wei2')):
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
AP1 = ("首都国际机场位于北京市东北郊，离北京市中心二十五公里左右，是中国最大、最繁忙的机场。它每周有一万多个航班，仅次于美国的亚特兰大机场。",
       "Capital International Airport is located in the northeast suburbs of Beijing, about 25 kilometers from the center of Beijing, and is the largest and busiest airport in China. It has more than 10,000 flights a week, second only to Atlanta’s airport in the United States. (translation mine)")
AP2 = ("首都机场有三个航站楼，最新建成的三号航站楼有地上四层，地下两层。主楼一层是国际出发大厅，这里有行李托运处、国际候机厅、海关和上百个登机口。大厅外停着很多接送旅客的出租汽车和机场巴士。二层是旅客到达大厅和行李提取大厅；三层为国内旅客出发大厅和地铁站台，从北京市区出发的地铁机场专线就直接开到这里；四层是餐饮区，这里有中西餐厅、酒吧、商场等各种服务设施。在航站楼各处都有服务台、自动提款机和外币兑换机。",
       "Capital Airport has three terminals; the newest, Terminal 3, has four floors above ground and two below. The first floor of the main building is the international departure hall, which has the baggage check-in (consignment) counters, the international departure lounge, customs and up to a hundred boarding gates. Outside the hall many taxis and airport buses stand picking up and dropping off passengers. The second floor is the arrival hall and baggage claim hall; the third floor is the domestic departure hall and the subway platform, to which the dedicated airport subway line from the city directly runs; the fourth floor is the dining area, with Chinese and Western restaurants, bars, shopping malls and all kinds of service facilities. Throughout the terminal there are service desks, ATMs and foreign-currency exchange machines. (mine)")
AP3 = ("首都机场有十八条巴士线路开往北京市区和近郊地区，交通十分方便。另外，还有一条地铁专线往返于市区东直门和首都机场之间。",
       "Capital Airport has eighteen bus lines going to the Beijing urban area and the nearby suburbs, so transportation is very convenient. In addition, there is a dedicated subway line running back and forth between Dongzhimen in the city and Capital Airport. (mine)")
L1 = lesson(
    "Lesson 22 Presentation 3: Beijing Capital International Airport",
    "首都国际机场 · 位于东北郊 · 三号航站楼 · 一层到四层 · 巴士线路 地铁专线",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. What are the main facilities you can find in an airport? B. What are some modes of transportation in use today? C. Watch the promo of Beijing Capital International Airport. (Two photographs and the video are not included.)"),
        card("Presentation 3: 首都国际机场", "The book also prints the passage in traditional characters; the numbers are spelled out in the Chinese text as the book does. The translations are mine.", examples=[D(*AP1), D(*AP2), D(*AP3)]),
    ],
    exercises=[
        M("Where is Capital International Airport?", "In the northeast suburbs of Beijing", ["In downtown Beijing", "In the south of Beijing", "In Tianjin"], "位于北京市东北郊."),
        M("How far is it from the city center?", "About 25 kilometers", ["About 2 kilometers", "About 250 kilometers", "About 12 kilometers"], "离北京市中心二十五公里左右."),
        M("How many flights does it have each week?", "More than 10,000", ["More than 1,000", "About 100", "More than 100,000"], "每周有一万多个航班."),
        M("Which airport is the only one busier?", "Atlanta’s airport in the United States", ["Chicago’s", "Tokyo’s", "London’s"], "仅次于美国的亚特兰大机场."),
        M("How many terminals does Capital Airport have?", "Three", ["Two", "Four", "Five"], "首都机场有三个航站楼."),
        M("How many floors does Terminal 3 have?", "Four above ground and two below", ["Two above and four below", "Six above ground", "Three above ground"], "地上四层，地下两层."),
        M("What is on the first floor of the main building?", "The international departure hall", ["The dining area", "The subway platform", "The arrival hall"], "主楼一层是国际出发大厅."),
        M("What is on the second floor?", "The arrival hall and baggage claim hall", ["The dining area", "The departure hall", "The bars"], "二层是旅客到达大厅和行李提取大厅."),
        M("Which floor has the subway platform?", "The third floor", ["The first floor", "The fourth floor", "The basement only"], "三层为国内旅客出发大厅和地铁站台."),
        M("What is on the fourth floor?", "The dining area", ["The customs", "The boarding gates", "The taxis"], "四层是餐饮区."),
        M("How many bus lines go to the urban and suburban areas?", "Eighteen", ["Eight", "Eighty", "Three"], "有十八条巴士线路."),
        M("Which subway station does the airport line connect to?", "Dongzhimen", ["Jianguomen", "Wangfujing", "Xidan"], "往返于市区东直门和首都机场之间."),
        F("首都国际机场___于北京市东北郊。", "位", PART, "位于: be located at."),
        F("大厅外停着很多接送旅客的出租汽车和机场___士。", "巴", PART, "巴士: bus."),
        F("在航站楼各处都有服务台、自动提款机和外币兑换___。", "机", PART, "兑换机: exchange machine."),
    ],
)

# ------------------------------------------------------------------ 2. activities
BY = ("白云国际机场位于广州市北郊，离广州市中心大约三十公里。它是中国三大国际机场之一，可以直达一百三十多个国内城市和八十多个国外城市。",
      "Baiyun International Airport is located in the north suburbs of Guangzhou, about 30 kilometers from the center of Guangzhou. It is one of China’s three major international airports and has direct flights to more than 130 domestic cities and more than 80 foreign cities. (translation mine; the book writes the numbers in digits)")
BY2 = ("白云机场有两座航站楼。一号航站楼共有四层，包括地上三层和地下一层。第三层为出发大厅，第二层为商业区，第一层为到达大厅，地下一层是地铁站、停车场和机场酒店。",
       "Baiyun Airport has two terminals. Terminal 1 has four floors in all, three above ground and one below. The third floor is the departure hall, the second floor the commercial area, the first floor the arrival hall, and the basement is the subway station, parking lot and airport hotel. (mine)")
BY3 = ("在一号航站楼和二号航站楼之间有一座四层的大楼，这是中国南方最大的交通中心。中心有地铁站、长途汽车站、公交站，还有一个室内停车楼和两个室外停车场。",
       "Between Terminal 1 and Terminal 2 there is a four-story building, the largest transportation center in southern China. The center has a subway station, a long-distance bus station and a bus stop, and also an indoor parking building and two outdoor parking lots. (mine)")
Q2 = [("首都国际机场位于哪儿？", "1. Where is Capital International Airport located? (my question for 首都国际机场位于北京市东北郊)"), ("首都国际机场离北京市中心有多远？", "2. How far is Capital International Airport from the center of Beijing? (my question)"), ("首都国际机场怎么样？它每周有多少个航班？", "3. What is Capital International Airport like? How many flights does it have each week? (my question)")]
TERMS = table(["航站楼的词语", "意思 (mine)"], [["海关", "customs"], ["登机口", "boarding gate"], ["出租汽车", "taxi"], ["旅客到达大厅", "arrival hall"], ["餐饮区", "dining area"], ["国际出发大厅", "international departure hall"], ["行李托运处", "baggage check-in counter"], ["国际候机厅", "international departure lounge"], ["机场巴士", "airport bus"], ["航站楼", "terminal building"], ["行李提取大厅", "baggage claim hall"], ["外币兑换机", "foreign-currency exchange machine"], ["地铁站台", "subway platform"], ["国内出发大厅", "domestic departure hall"], ["商场", "shopping mall"], ["中西餐厅", "Chinese and Western restaurants"], ["酒吧", "bar"], ["服务台", "service desk"], ["自动提款机", "ATM"]],
              title="Activity 1B: the 19 terms for the terminal layout (the book gives the Chinese; the English glosses are mine)", say=[0])
L2 = lesson(
    "Lesson 22 Presentation 3 activities: the terminal layout, questions and Baiyun Airport",
    "Activities 1 to 4 · 航站楼的设施 · 为句子提问 · 白云国际机场 · 一号航站楼",
    requires=[],
    cards=[
        card("Activity 1 (Listening)",
             "A. Global listening: listen to Presentation 3 once and answer: 1. What is the location of the airport relative to Beijing city? (the northeast suburbs, about 25 km from the center) 2. What comparison was made with the airport in Atlanta, GA? (Beijing’s is second only to Atlanta’s in the number of weekly flights) 3. Why is transportation to the airport convenient? (eighteen bus lines and a dedicated subway line) 4. Draw a rough layout of the terminal. B. Detailed listening: listen again and refine the layout using the terms below. (Audio, not included.)",
             tables=[TERMS]),
        card("Activity 2 (Reading, Writing, Speaking and Listening)",
             "A. Read the first paragraph of the presentation. Write a question for each underlined sentence: 1. 首都国际机场位于北京市东北郊 2. 离北京市中心二十五公里左右 3. 是中国最大、最繁忙的机场。它每周有一万多个航班，仅次于美国的亚特兰大机场。 B. In groups of three, share your questions. Vote for the best question for each sentence. My questions:",
             examples=[D(z, e) for z, e in Q2]),
        card("Activity 3 (Reading)",
             "Read about Beijing Capital International Airport (BCIA) before 2008 and complete the following tasks: 1. How did BCIA improve after 2008? 2. Sketch the layout of the terminal and mark the facilities in Chinese. 3. Pair up. Using your sketch, describe the layout of the terminal, in Chinese. (The reading about the airport before 2008 is not in the text I was given; the book shows it as a picture.)"),
        card("Activity 4 (Reading and Speaking)",
             "Read the introduction of Baiyun International Airport and accomplish the following tasks: 1. Pair up. Verbally translate the first paragraph for your partner. 2. Sketch the layout of the terminals and the transportation center of Baiyun Airport. The introduction (the book writes the numbers 30, 130 and 80 in digits):",
             examples=[D(*BY), D(*BY2), D(*BY3)]),
    ],
    exercises=[
        M("Where is Baiyun International Airport?", "In the north suburbs of Guangzhou", ["In the south of Guangzhou", "In Shenzhen", "In Hong Kong"], "位于广州市北郊."),
        M("How far is it from the city center?", "About 30 kilometers", ["About 3 kilometers", "About 130 kilometers", "About 80 kilometers"], "大约三十公里."),
        M("How many domestic cities does it fly to directly?", "More than 130", ["More than 80", "About 30", "Over 300"], "一百三十多个国内城市."),
        M("How many terminals does Baiyun have?", "Two", ["Three", "Four", "One"], "有两座航站楼."),
        M("What is on the third floor of Terminal 1?", "The departure hall", ["The arrival hall", "The commercial area", "The subway station"], "第三层为出发大厅."),
        M("What is on the second floor of Terminal 1?", "The commercial area", ["The departure hall", "The arrival hall", "The parking lot"], "第二层为商业区."),
        M("What is in the basement of Terminal 1?", "The subway station, parking lot and airport hotel", ["The customs", "The boarding gates", "The restaurants"], "地下一层是地铁站、停车场和机场酒店."),
        M("What is between Terminal 1 and Terminal 2?", "A four-story transportation center", ["A park", "A hotel only", "A river"], "之间有一座四层的大楼."),
        M("Which means “customs”?", "海关", ["登机口", "服务台", "酒吧"], "海关."),
        F("它是中国三大国际机场之___，可以直达一百三十多个国内城市。", "一", PART, "之一: one of."),
        F("第二层为商业___。", "区", PART, "商业区: commercial area."),
    ],
)

# ------------------------------------------------------------------ 3. explanatory text
HH = ("我的老家在纽约。我们家的房子有两层楼，非常漂亮。楼下有一个大客厅。客厅旁边是厨房，对面是书房。楼上有三个卧室。我父母的卧室在左边，妹妹的卧室在右边，中间那个小一点儿的是我的。我们家还有一个地下室和一个车库。房子后边有一个大院子，院子里有两棵苹果树。房子前边有一个小花园，里边种着很多花。",
      "My hometown is New York. Our house has two floors and is very beautiful. Downstairs there is a big living room. Next to the living room is the kitchen, and opposite is the study. Upstairs there are three bedrooms. My parents’ bedroom is on the left, my sister’s bedroom is on the right, and the smaller one in the middle is mine. Our house also has a basement and a garage. Behind the house is a big yard with two apple trees in it. In front of the house is a small garden with many flowers planted in it. (translation mine)")
L3 = lesson(
    "Lesson 22 Presentation 3 grammar: simple explanatory text",
    "我家的房子 · 楼下 楼上 · 旁边 对面 中间 · 后边 前边 · 空间顺序",
    requires=[],
    cards=[
        card("Simple Explanatory Text",
             "An explanatory text is a type of non-fiction text that explains a process (for example, how something works or why something happens). Activity 1 (Reading): Read the space-oriented explanatory passage 我家的房子 and answer the questions: 1. What’s the structure of the passage? 2. What’s the specific order of the content part? 3. Highlight the main spatial transfer words in the passage. My answers: 1. A general statement first (my hometown, the house has two floors and is beautiful) and then the details, floor by floor and then outside. 2. From the inside to the outside and from the bottom to the top: downstairs (living room, kitchen, study), upstairs (three bedrooms, left, right, middle), basement and garage, the yard behind, the garden in front. 3. 楼下, 旁边, 对面, 楼上, 左边, 右边, 中间, 后边, 前边, 里边.",
             examples=[D(*HH)]),
        card("Activity 2 (Speaking)",
             "Pair up. Describe the house shown below to each other (a floor plan; the picture is not included)."),
    ],
    exercises=[
        M("What does an explanatory text explain?", "A process, how something works or why it happens", ["A person’s feelings", "A joke", "A poem"], "explains a process."),
        M("How many floors does the writer’s house have?", "Two", ["One", "Three", "Four"], "两层楼."),
        M("What is next to the living room?", "The kitchen", ["The study", "The garage", "The bedroom"], "客厅旁边是厨房."),
        M("What is opposite the kitchen side, across from the living room?", "The study", ["The kitchen", "The garage", "The basement"], "对面是书房."),
        M("Which bedroom is in the middle?", "The writer’s", ["The parents’", "The sister’s", "The guest’s"], "中间那个小一点儿的是我的."),
        M("What is in the yard behind the house?", "Two apple trees", ["A swimming pool", "A garage", "A tree house"], "院子里有两棵苹果树."),
        M("What is in front of the house?", "A small garden", ["The yard", "The garage", "The study"], "房子前边有一个小花园."),
        M("Which are spatial transfer words?", "左边 and 中间", ["我们 and 他们", "很多 and 一些", "非常 and 特别"], "Spatial words."),
        F("楼上有三个卧___。", "室", PART, "卧室: bedroom."),
        F("房子___边有一个大院子。", "后", PART, "后边: behind."),
    ],
)

# ------------------------------------------------------------------ 4. skill integration
PD = ("上海浦东国际机场是中国最大的国际机场之一，离上海市中心三十公里。浦东机场的候机楼有三层楼。一楼是迎宾大厅，二楼是到达大厅，三楼是出发大厅。走进迎宾大厅，你可以看到国际行李提取处在一楼的左边，国内行李提取处在一楼的右边。从一楼走上二楼去，在到达大厅，你可以看到国内到达通道在大厅的右边，国际到达通道在大厅的左边。走上三楼去，你可以看到左边是国内登机服务处，右边是国际登机服务处。中间是医疗急救服务处。出发大厅的两边都有邮局、餐厅和商店等服务设施。",
      "Passage 1: Shanghai Pudong International Airport is one of the largest international airports in China, 30 kilometers from the center of Shanghai. The terminal at Pudong has three floors. The first floor is the welcome hall, the second the arrival hall, the third the departure hall. Walking into the welcome hall you can see the international baggage claim on the left of the first floor and the domestic baggage claim on the right. Going up from the first floor to the arrival hall on the second you can see the domestic arrival passage on the right of the hall and the international arrival passage on the left. Going up to the third floor you can see the domestic check-in service on the left and the international one on the right. In the middle is the medical emergency service. On both sides of the departure hall there are service facilities such as a post office, restaurants and shops. (translation mine; the book gives the readings of 浦东 and 迎宾 in pinyin in brackets, which I left out)")
HQ = ("上海虹桥国际机场是中国的三大国际机场之一，离上海市中心十三公里。上海虹桥国际机场有两座候机楼，一座是国际候机楼，一座是国内候机楼。每座候机楼都有两层，一层是到达大厅，二层是出发大厅。在一层和二层都有各种服务设施，像商店、餐厅等。在国内到达大厅，旅客下飞机以后可以看到前面有四个行李提取处。旅客取完行李，走出大厅的时候，可以看到在大厅出口的左右两边都有洗手间。大厅外面有很多出租汽车和机场大巴。旅客还可以看到在大厅门外的左边有一个行李寄存处，右边有一个宾馆服务处。",
      "Passage 2: Shanghai Hongqiao International Airport is one of China’s three major international airports, 13 kilometers from the center of Shanghai. Hongqiao has two terminals, one international and one domestic. Each terminal has two floors, the first the arrival hall and the second the departure hall. On both floors there are all kinds of service facilities, such as shops and restaurants. In the domestic arrival hall, after getting off the plane passengers can see four baggage claims ahead. After taking their baggage and walking out of the hall they can see restrooms on both the left and right of the hall exit. Outside the hall there are many taxis and airport buses. Passengers can also see a baggage storage on the left outside the hall door and a hotel service counter on the right. (mine; the book prints 象商店, which I read as 像商店, and the pinyin of 虹桥 and 寄存处 in brackets, which I left out)")
SH = [("早上九点，在北京首都国际机场的出发大厅，一个人带着大包小包的行李，他这是要到哪里去呢？", "1. At nine in the morning, in the departure hall of Beijing Capital International Airport, a man carrying big and small bags: where is he going? (the book’s prompt; my translation)"), ("在出发大厅，我们看到一个带小狗的男孩。", "2. In the departure hall we saw a boy with a puppy."), ("在安检入口，我们看到一位父亲来送儿子上飞机。", "3. At the security-check entrance we saw a father who came to see his son off on the plane."),
      ("在国际候机厅里，我们看到一位六十多岁的老大爷。老大爷看起来非常高兴，因为这是他第一次出国。", "4. In the international departure lounge we saw an old man in his sixties. He looked very happy, because it was his first time abroad. (the book prints 非常很高兴; I read 非常高兴)"), ("已经是晚上十一点五十分了，国际候机厅里还有人在等飞机。", "5. It was already ten to midnight and in the international departure lounge there were still people waiting for planes. (the book writes 11:50; I spelled out the time)")]
JC = ("北京首都国际机场有二百五十二条国内和国际航线，可以把中国人送到全世界大多数的国家和地区。在春节期间，还有四分之一乘客是要离家远行的。",
      "Airport Stories: Beijing Capital International Airport has 252 domestic and international routes and can take Chinese people to most countries and regions of the world. During the Spring Festival a quarter of the passengers are leaving home to travel far. (translation mine; adapted from tv.cctv.com in the book)")
TL = table(["", "Atlanta International Airport", "Beijing Capital International Airport"], [["First paragraph", "(your notes after reading and listening)", "(your notes)"], ["Second paragraph", "(your layout sketch)", "(your layout sketch)"], ["Third paragraph: transportation", "(your notes)", "(your notes)"]], title="Activity 2: the comparison chart (the book leaves it blank; audio not included)")
L4 = lesson(
    "Lesson 22 Presentation 3 skill integration: Pudong and Hongqiao airports, a comparison and airport stories",
    "上海浦东国际机场 · 上海虹桥国际机场 · 迎宾大厅 · 行李提取处 · 机场故事",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking and Listening)",
             "A. Form two groups. Group A reads Passage 1 and Group B reads Passage 2. After reading the passage, draw a layout of the airport terminal in your notebook (the book gives a three-level frame: 三楼, 二楼到达大厅, 一楼迎宾大厅), and note any additional information. When you are done, discuss the passage with your group to ensure you understand it thoroughly. B. Pair up with a student from the other group. Explain the information in your passage based on your drawing and additional information. Listen to your partner’s report and fill in the table. C. Go back to your original group and talk about the information you obtained about the other airport. If there are any inconsistencies, read your partner’s passage to make corrections.",
             examples=[D(*PD), D(*HQ)]),
        card("Activity 2 (Reading, Listening and Speaking)",
             "Compare Atlanta International Airport and Beijing Capital International Airport. Read the first paragraph of Presentation 3 and listen to clip 1 and write down the differences between the two airports; refer to the second paragraph of Presentation 3 and listen to clip 2 and in your notebook draw a rough layout of the Atlanta airport and compare it with your drawing of the Beijing airport; read the third paragraph of Presentation 3 and listen to clip 3: what mode of transportation is described? (Audio, not included.)",
             tables=[TL]),
        card("Activity 3 (Reading, Listening and Speaking)",
             "A. Read the prompts, listen to the following interviews at Beijing Capital International Airport and take notes for each instance. B. Which story did you find the most compelling? Did any of the stories surprise you? Discuss your answers with your classmates. (The interviews are audio, not included.)",
             examples=[D(*JC)] + [D(z, e) for z, e in SH]),
    ],
    exercises=[
        M("How far is Pudong Airport from the center of Shanghai?", "30 kilometers", ["13 kilometers", "3 kilometers", "300 kilometers"], "离上海市中心三十公里."),
        M("How far is Hongqiao Airport from the center?", "13 kilometers", ["30 kilometers", "3 kilometers", "30 meters"], "离上海市中心十三公里."),
        M("How many floors does the Pudong terminal have?", "Three", ["Two", "Four", "One"], "候机楼有三层楼."),
        M("What is on the first floor at Pudong?", "The welcome hall", ["The departure hall", "The arrival hall", "The restaurants"], "一楼是迎宾大厅."),
        M("Where is the international baggage claim at Pudong?", "On the left of the first floor", ["On the right of the first floor", "On the third floor", "Outside the hall"], "国际行李提取处在一楼的左边."),
        M("What is in the middle of the third floor?", "The medical emergency service", ["The post office", "The restaurant", "The customs"], "中间是医疗急救服务处."),
        M("How many terminals does Hongqiao have?", "Two, one international and one domestic", ["One", "Three", "Four"], "两座候机楼."),
        M("How many baggage claims can passengers see ahead in the domestic arrival hall?", "Four", ["Two", "Six", "Ten"], "前面有四个行李提取处."),
        M("What is on the left outside the hall door at Hongqiao?", "A baggage storage", ["A hotel counter", "A taxi stand", "A restroom"], "左边有一个行李寄存处."),
        M("What is on the right outside the hall door?", "A hotel service counter", ["A baggage storage", "A restroom", "A bank"], "右边有一个宾馆服务处."),
        M("How many routes does Beijing Capital Airport have?", "252", ["25", "125", "520"], "二百五十二条国内和国际航线."),
        M("What share of passengers travel far from home during the Spring Festival?", "A quarter", ["Half", "A tenth", "Three quarters"], "四分之一乘客."),
        F("国际行李提取处在一楼的左___。", "边", PART, "左边."),
        F("机场巴士和出租汽车都在大厅___面。", "外", PART, "大厅外面."),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context
LR = ("这是我们家的客厅。客厅里有一个三人沙发。沙发前边有一个咖啡桌，桌子上面有一瓶花。咖啡桌左边是一个双人沙发，右边是一个单人沙发。我们喜欢坐在客厅里聊天，看电视。",
      "This is our living room. In the living room there is a three-seat sofa. In front of the sofa is a coffee table, with a vase of flowers on the table. On the left of the coffee table is a two-seat sofa and on the right a single sofa. We like to sit in the living room, chat and watch TV. (translation mine)")
AT = ("首先，我在网上买机票，然后选好座位。到了机场以后，我先去航空公司的柜台办理登机手续，托运行李，拿到登机牌。接着，我走到安检入口，通过安检，再去候机厅。最后，听到广播以后，我到登机口排队，上飞机。",
      "First I buy the ticket online and then choose a seat. After arriving at the airport I first go to the airline counter to check in, check my baggage and get my boarding pass. Next I walk to the security-check entrance, go through security and then to the departure lounge. Finally, after hearing the announcement, I line up at the boarding gate and board the plane. (my sample explanation of the air-travel process for Activity 3, using time transfer words)")
L5 = lesson(
    "Lesson 22 Presentation 3 using Chinese in context: airport layouts, a living room and the air-travel process",
    "机场平面图 · 起飞到登机 · 客厅描述 · 时间和空间顺序 · 成都双流机场转机",
    requires=[],
    cards=[
        card("Activities 1 and 2 (Speaking and Listening)",
             "Activity 1: Pair up. Explain one of the diagrams below to your partner and your partner will explain the other to you. In your notebook, draw the layout based on the description from your partner, then compare your sketch to the original picture. Picture 1: layout of a three-story airport terminal. Picture 2: the layout of an airport international arrival terminal. Activity 2: Pair up. Work with your partner to explain the simple airport layout (a terminal design showing the departure upper level and arrival levels). The areas on the picture: 1. Departures Lounge 2. Gates and jet bridges 3. Security Clearance Gates 4. Baggage Check-in 5. Baggage Carousels. (The diagrams are not included.)"),
        card("Activity 3 (Speaking)",
             "Explain the process of air travel from buying a ticket to boarding the plane. My sample, using time transfer words:",
             examples=[D(*AT)]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Read the short description of a living room and discuss the questions with a classmate: 1. What is the structure of the whole passage? 2. Why does the content part start with the 三人沙发? 3. Highlight the spatial transferring words in the passage. My answers: 1. A general statement first (this is our living room), then the furniture from the biggest to the smallest, then the family’s use of the room. 2. It is the largest piece of furniture and the center of the room, from which the others are placed (in front, left, right). 3. 前边, 上面, 左边, 右边. B. Pair up. Tell your partner a description of your bedroom. Then, together, come up with a revised description. (A photograph is not included.)",
             examples=[D(*LR)]),
        card("Activities 5 and 6",
             "Activity 5 (Speaking and Listening): using the mixed order of time and space, describe the house below. Read your description to your partner. Listen to and discuss the differences. Come up with a revised group work. (A floor plan, not included.) Activity 6 (Speaking): A. Below is information on how to transfer from domestic flight to international flight (including Hong Kong, Macao, and Taiwan, 港澳台) at Chengdu Shuangliu International Airport. Think about how to explain this process, using proper time transfer words. B. Pair up. Read your explanation to your partner and compare each other’s work. (The airport’s information sheet is not included.)"),
    ],
    exercises=[
        M("Which word begins a sequence of steps?", "首先", ["最后", "接着", "所以"], "首先 = first."),
        M("Which word means “next”?", "接着", ["首先", "最后", "但是"], "接着."),
        M("Which word closes the sequence?", "最后", ["首先", "然后", "接着"], "最后 = finally."),
        M("Where is the coffee table in the living room?", "In front of the sofa", ["Behind the sofa", "On the sofa", "Outside"], "沙发前边有一个咖啡桌."),
        M("What is on the table?", "A vase of flowers", ["A TV", "A cat", "A book"], "桌子上面有一瓶花."),
        M("Which sofa is on the left of the coffee table?", "The two-seat sofa", ["The three-seat sofa", "The single sofa", "No sofa"], "咖啡桌左边是一个双人沙发."),
        M("What does the family like to do in the living room?", "Chat and watch TV", ["Cook", "Sleep", "Play basketball"], "聊天，看电视."),
        M("Why does the description start with the three-seat sofa?", "It is the biggest piece and the reference point", ["It is the cheapest", "It is the oldest", "It is in the garden"], "The largest piece first."),
        F("首先，我在网上买机___。", "票", PART, "机票: air ticket."),
        F("最后，听到广播以后，我到登机口排队，上飞___。", "机", PART, "飞机: airplane."),
    ],
)

# ------------------------------------------------------------------ 6. vocabulary
L6 = vocab_lesson("Lesson 22 Presentation 3 vocabulary", "34 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English; its glosses are kept as printed. The book prints 上(百) with the 百 in brackets; I list 上百.", VOC3)

# ------------------------------------------------------------------ 7. area studies
L7 = lesson(
    "Lesson 22 Area Studies: China’s Tourism",
    "出境游 · 国内游 · 入境游 · 黄金周 · 世界旅游组织",
    requires=[],
    cards=[
        card("China’s Tourism (1): outbound tourism",
             "China tourism has seen unprecedented development in recent years due to the sustainable economic growth and the great improvement in Chinese people’s living standards and consumption level. Outbound Tourism: In the past ten years, China’s outbound tourism has maintained a double-digit growth, and China has become the world’s largest source of outbound tourists since 2013. In the year of 2018, there were 149.72 million outbound trips, which created a tremendous market for foreign countries. The hottest destinations include South Korea, Japan, Thailand, France, Italy, Switzerland, Germany, USA, Singapore and Maldives. According to the statistics of the Ministry of Culture and Tourism of China, less than 5 out of 100 mainland residents travel abroad, which indicates the great potential of the overseas tourism market. Based on China’s huge population, a further and sustained growth of outbound visitors is expected."),
        card("(2) Domestic tourism",
             "Chinese domestic tourism keeps expanding steadily. In 2018, there were 5,539 million domestic tourist trips. As an important element of China’s tourist market, the domestic market benefits a lot from the large population. In the recent decades, domestic traveling greatly enhances the employment, consumption and economic development of the country. Currently, the most popular destinations for domestic travelers include Beijing, Shanghai, Guangzhou, Xi’an, Guilin, Hangzhou, Sanya, Lhasa, Chengdu, Lijiang, Hong Kong, and Macau. The visitor quantity soars to amazing numbers during the peak seasons, especially the two golden weeks (the National Day Holiday and the Chinese New Year). In the seven days of the National Day Holiday in 2019, the country received a total of 802 million domestic tourists, and the domestic tourism revenue reached ¥649.71 billion. Associated with this prosperity might be the problems of traffic and the tourist service capacity, so foreigners who plan a visit to China should try to avoid these rush periods."),
        card("(3) Inbound tourism and the top 20 destinations",
             "Inbound Tourism: China is a vast land rich in tourism resources. The country’s wide variety of terrain and climate shape numerous natural attractions. On top of that, her long history, resplendent culture and distinctive customs are always appealing to foreign visitors. China has steadily been the fourth largest international travel destination, after France, Spain, and the United States. The inbound tourism trips rocketed to an impressive 141.2 million in the year of 2018. The top 20 destinations in China for overseas tourists: 1. Hong Kong 2. Shanghai 3. Beijing 4. Macau 5. Guangzhou 6. Shenzhen 7. Sanya 8. Xi’an 9. Hangzhou 10. Chengdu 11. Qingdao 12. Dalian 13. Xiamen 14. Zhuhai 15. Nanjing 16. Haikou 17. Guilin 18. Suzhou 19. Chongqing 20. Tianjin. Some of these destinations are renowned for their glorious history, boast picturesque landscapes, are endowed with very colorful ethnic features or are economically prosperous (the Forbidden City, the Li River, Shanghai and Inner Mongolia are shown in photographs, not included). In 1995, the World Tourism Organization (UNWTO) predicted that by 2020 China would be the fourth largest market in the world (UNWTO Tourism 2020 Vision). China will have reached this target well before 2020 and there is still great potential for China’s inbound tourism. Source: Ministry of Culture and Tourism of the People’s Republic of China."),
    ],
    exercises=[
        M("Since when has China been the world’s largest source of outbound tourists?", "2013", ["2000", "2018", "2008"], "since 2013."),
        M("How many outbound trips were there in 2018?", "149.72 million", ["14.9 million", "1,497 million", "5,539 million"], "149.72 million."),
        M("About how many of 100 mainland residents travel abroad?", "Fewer than 5", ["About 50", "About 20", "About 80"], "less than 5 out of 100."),
        M("How many domestic tourist trips were there in 2018?", "5,539 million", ["149.72 million", "802 million", "141.2 million"], "5,539 million."),
        M("What are the two golden weeks?", "The National Day holiday and the Chinese New Year", ["Labor Day and Mid-Autumn", "Christmas and Easter", "Spring and autumn breaks"], "the two golden weeks."),
        M("How many domestic tourists did China receive in the 2019 National Day holiday?", "802 million", ["149.72 million", "141.2 million", "5,539 million"], "802 million."),
        M("How much was the domestic tourism revenue in the 2019 National Day holiday?", "¥649.71 billion", ["¥649.71 million", "¥141.2 billion", "¥5,539 billion"], "¥649.71 billion."),
        M("What advice is given to foreigners planning a visit?", "Avoid the rush periods", ["Visit only in the golden weeks", "Visit only Beijing", "Bring a car"], "try to avoid these rush periods."),
        M("Which rank does China hold among international travel destinations?", "Fourth, after France, Spain and the United States", ["First", "Second", "Tenth"], "fourth largest."),
        M("How many inbound trips were there in 2018?", "141.2 million", ["149.72 million", "802 million", "5.5 million"], "141.2 million."),
        M("Which is first on the list of the top 20 destinations for overseas tourists?", "Hong Kong", ["Beijing", "Shanghai", "Macau"], "1. Hong Kong."),
        M("What did UNWTO predict in 1995?", "That China would be the fourth largest market by 2020", ["That China would be first by 2000", "That China would close its borders", "That tourism would end"], "UNWTO Tourism 2020 Vision."),
    ],
)

UNIT = unit("第二十二课 Presentation 3: 首都国际机场, 说明文, 机场平面图, Area Studies", [L1, L2, L3, L4, L5, L6, L7])
