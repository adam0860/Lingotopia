"""Unit 9: hometowns and places (lessons 80-94): 在 as a verb, compass directions, where a place is, cities and
states, where you are from, growing up, 还 and 不…了, 哪 + measure word, the zero-particle question, the negation
scale of 都, the -r ending, ship words, classroom expressions, the Chinese family, review.
Original text; the scope follows DLIFLC Chinese Basic Program Unit 1 Lesson 4 (Birthdate, Birthplace and
Hometown), Presentations 2 and 3, and its Area Studies."""
from dsl_zh import *

PART = ["吗", "们", "呢"]

# ---------------------------------------------------------------------------- 80
L80 = lesson(
    "Being somewhere: 在 and 老家",
    "他在北京 · 张老师不在 · 你的老家在哪儿？",
    requires=[],
    cards=[
        card("在 as a verb",
             "As a verb, 在 (zài) means “to be at” a place. 他在北京 is “He is in Beijing”. With no place word it means “is here” or “is in”, the place being known: 张老师不在, “Teacher Zhang is not in”. "
             "Its negative is 不在, and questions are 在吗？ or 在不在？ "
             "老家 (lǎojiā) is your hometown, the place your family comes from, and 现在 (xiànzài) is “now”.",
             tables=[table(["Form", "Example", "Meaning"],
                           [["在 + place", "他在北京。", "He is in Beijing."], ["不在", "张老师今天不在。", "Teacher Zhang is not in today."],
                            ["在吗？", "李老师在教室吗？", "Is Teacher Li in the classroom?"], ["在不在？", "她在不在教室？", "Is she in the classroom?"]], say=[1])]),
        card("Verb 在, or place before a verb?",
             "When 在 comes before another verb, it is not the main verb: it shows where the action happens. 他在北京工作 is “He works in Beijing”; the verb is 工作. "
             "When 在 stands by itself, it is the verb “to be at”: 他在北京.",
             examples=[ex("我的老家在四川。", "wo3 de5 lao3jia1 zai4 si4chuan1", "My hometown is in Sichuan.", hl="在"),
                       ex("明天我在家。", "ming2tian1 wo3 zai4 jia1", "Tomorrow I will be at home."),
                       ex("王老师也在学校。", "wang2 lao3shi1 ye3 zai4 xue2xiao4", "Teacher Wang is at school too."),
                       ex("他在北京工作。", "ta1 zai4 bei3jing1 gong1zuo4", "He works in Beijing.", hl="在北京")]),
    ],
    exercises=[
        mean("老家", "lao3jia1", "hometown", ["a family photo", "an old house", "a military base"]),
        mean("现在", "xian4zai4", "now", ["today", "soon", "tomorrow"]),
        mean("在", "zai4", "to be at", ["to have", "to be called", "to live"]),
        rd("在", "zai4", ["zai1", "zai2", "zai3"]),
        rd("老家", "lao3jia1", ["lao3jia2", "lao3jia4", "lao4jia1"]),
        rd("现在", "xian4zai4", ["xian4zai1", "xian2zai4", "xian1zai4"]),
        M("How do you say “Teacher Zhang is not in today”?", "张老师今天不在。", ["张老师今天不是在。", "张老师不今天在。", "张老师今天在不。"], "不在 is the negative of 在."),
        M("How do you say “My hometown is in Sichuan”?", "我的老家在四川。", ["我的老家是在四川。", "我的在老家四川。", "我老家四川在的。"], "老家 + 在 + place."),
        M("Which asks “Is she in the classroom?”", "她在不在教室？", ["她不在教室吗不？", "她在教室不吗？", "她不是教室？"], "在不在 + place."),
        M("What does 他在北京工作 say?", "He works in Beijing.", ["He is in Beijing.", "He is not in Beijing.", "He wants to work."], "在 + place before a verb."),
        M("What does 李老师在教室吗？ ask?", "Is Teacher Li in the classroom?", ["Where is Teacher Li?", "Is Teacher Li a teacher?", "Is Teacher Li at home?"], "在吗 asks if someone is there."),
        F("我的老家___四川。", "在", ["吗", "们", "呢"], "在 is “is in”.", tr="My hometown is in Sichuan."),
        F("她___不在教室？", "在", PART, "在不在 asks about presence.", tr="Is she in the classroom?"),
        F("明天我在___。 (at home)", "家", ["吗", "们", "呢"], "在家 is at home.", tr="Tomorrow I will be at home."),
        F("你的老家在哪___？", "儿", ["吗", "们", "呢"], "哪儿 is where.", tr="Where is your hometown?"),
    ],
)

# ---------------------------------------------------------------------------- 81
L81 = lesson(
    "East, south, west, north",
    "东南西北 · 东部 · 南边 · 南方人",
    requires=[],
    cards=[
        card("The four directions",
             "The four directions are 东 (dōng, east), 南 (nán, south), 西 (xī, west) and 北 (běi, north). When Chinese names them in a list, the order is 东南西北, east-south-west-north. "
             "Two directions together give the corners, and the first one named is the main one: 东南 is the southeast, 西北 the northwest.",
             tables=[wtable([("东", "dong1", "east"), ("南", "nan2", "south"), ("西", "xi1", "west"), ("北", "bei3", "north"), ("东南", "dong1nan2", "southeast"),
                             ("西北", "xi1bei3", "northwest"), ("东北", "dong1bei3", "northeast"), ("西南", "xi1nan2", "southwest"), ("中", "zhong1", "middle")])]),
        card("Three ways to use them",
             "Add 部 (bù, a part) to name a region: 东部 is the eastern part. Add 边 (biān, side) to say which side of something: 南边 is the south side. "
             "Add 方 (fāng, direction) and 人 for people: 南方人 are southerners and 北方人 northerners.",
             tables=[wtable([("东部", "dong1bu4", "the east part"), ("西部", "xi1bu4", "the west part"), ("南部", "nan2bu4", "the south part"), ("北部", "bei3bu4", "the north part"),
                             ("南边", "nan2bian1", "the south side"), ("北边", "bei3bian1", "the north side"), ("南方", "nan2fang1", "the south"), ("北方", "bei3fang1", "the north"),
                             ("南方人", "nan2fang1ren2", "a southerner"), ("北方人", "bei3fang1ren2", "a northerner")])],
             examples=[ex("我的老家在美国东部。", "wo3 de5 lao3jia1 zai4 mei3guo2 dong1bu4", "My hometown is in the eastern United States.", hl="东部"),
                       ex("他们住在西部。", "ta1men5 zhu4 zai4 xi1bu4", "They live in the west.")]),
    ],
    exercises=[
        mean("东", "dong1", "east", ["west", "north", "south"]),
        mean("南", "nan2", "south", ["east", "north", "west"]),
        mean("西", "xi1", "west", ["east", "north", "south"]),
        mean("北", "bei3", "north", ["south", "west", "east"]),
        mean("东南", "dong1nan2", "southeast", ["northwest", "northeast", "southwest"]),
        mean("西北", "xi1bei3", "northwest", ["southeast", "northeast", "southwest"]),
        mean("东部", "dong1bu4", "the east part", ["the east side", "the east wind", "the east gate"]),
        mean("南边", "nan2bian1", "the south side", ["the south part", "the southerner", "the south gate"]),
        mean("北方人", "bei3fang1ren2", "a northerner", ["a southerner", "an easterner", "a westerner"]),
        rd("东", "dong1", ["dong2", "dong3", "dong4"]),
        rd("西", "xi1", ["xi2", "xi3", "xi4"]),
        rd("北", "bei3", ["bei1", "bei2", "bie3"]),
        M("What is the Chinese order of the four directions in a list?", "东南西北", ["东西南北", "南北东西", "北东西南"], "East-south-west-north."),
        M("Which is the northeast?", "东北", ["北东", "西北", "东南"], "东 + 北, east named first."),
        M("Which means “the western part”?", "西部", ["西边", "西方人", "北部"], "部 names a region."),
        M("Which means “the south side”?", "南边", ["南部", "南方", "西边"], "边 is a side."),
        F("我的老家在美国___部。 (the east)", "东", ["吗", "们", "呢"], "东部 is the east part.", tr="My hometown is in the east of the US."),
        F("他是北方___。", "人", ["吗", "们", "呢"], "北方人 is a northerner.", tr="He is a northerner."),
    ],
)

# ---------------------------------------------------------------------------- 82
L82 = lesson(
    "Where one place is",
    "天津在北京的南边 · 在中国的西北部",
    requires=[],
    cards=[
        card("A is south of B",
             "To place one thing against another, use 在 and 的 with a direction word: A 在 B 的 南边. The part you are locating comes first and the landmark second, with 的 in between. "
             "天津在北京的南边 is “Tianjin is south of Beijing”. To place something inside a larger area, say the area and then the part: 在中国的西北部, “in the northwest of China”.",
             tables=[table(["Pattern", "Example", "Meaning"],
                           [["A 在 B 的 南边", "天津在北京的南边。", "Tianjin is south of Beijing."], ["A 在 B 的 东部", "广东在中国的东南部。", "Guangdong is in the southeast of China."],
                            ["在 … 哪儿？", "你的老家在哪儿？", "Where is your hometown?"], ["在 + area + 哪儿？", "在东部哪儿？", "Where in the east?"]], say=[1])]),
        card("Cities on the map",
             "Here are some places to practise with. The ending 市 shì means “city” and 州 zhōu “state”.",
             tables=[wtable([("北京", "bei3jing1", "Beijing"), ("天津", "tian1jin1", "Tianjin"), ("上海", "shang4hai3", "Shanghai"), ("广州", "guang3zhou1", "Guangzhou"), ("香港", "xiang1gang3", "Hong Kong"),
                             ("台湾", "tai2wan1", "Taiwan"), ("西安", "xi1'an1", "Xi'an"), ("纽约", "niu3yue1", "New York"), ("华盛顿", "hua2sheng4dun4", "Washington"), ("洛杉矶", "luo4shan1ji1", "Los Angeles")])],
             examples=[ex("天津在北京的南边。", "tian1jin1 zai4 bei3jing1 de5 nan2bian1", "Tianjin is south of Beijing.", hl="南边"),
                       ex("香港在广州的南边。", "xiang1gang3 zai4 guang3zhou1 de5 nan2bian1", "Hong Kong is south of Guangzhou."),
                       ex("西安在上海的西边。", "xi1'an1 zai4 shang4hai3 de5 xi1bian1", "Xi'an is west of Shanghai."),
                       ex("纽约在华盛顿的北边。", "niu3yue1 zai4 hua2sheng4dun4 de5 bei3bian1", "New York is north of Washington.")]),
    ],
    exercises=[
        mean("北京", "bei3jing1", "Beijing", ["Shanghai", "Tianjin", "Hong Kong"]),
        mean("上海", "shang4hai3", "Shanghai", ["Beijing", "Guangzhou", "Xi'an"]),
        mean("香港", "xiang1gang3", "Hong Kong", ["Taiwan", "Guangzhou", "Shanghai"]),
        mean("台湾", "tai2wan1", "Taiwan", ["Hong Kong", "Tianjin", "Beijing"]),
        mean("纽约", "niu3yue1", "New York", ["Washington", "Los Angeles", "Beijing"]),
        mean("洛杉矶", "luo4shan1ji1", "Los Angeles", ["New York", "Washington", "Shanghai"]),
        rd("北京", "bei3jing1", ["bei3jing3", "bei4jing1", "bei3jin1"]),
        rd("上海", "shang4hai3", ["shang4hai1", "shang3hai3", "shang4hai4"]),
        rd("香港", "xiang1gang3", ["xiang1gang1", "xiang2gang3", "xiang1gang4"]),
        M("How do you say “Tianjin is south of Beijing”?", "天津在北京的南边。", ["天津在南边北京的。", "天津的北京在南边。", "北京在天津的南边。"], "A 在 B 的 南边."),
        M("What does 北京在天津的北边 say?", "Beijing is north of Tianjin.", ["Beijing is south of Tianjin.", "Tianjin is north of Beijing.", "Beijing is in Tianjin."], "A is in the north of B."),
        M("What does 广东在中国的东南部 say?", "Guangdong is in the southeast of China.", ["Guangdong is in the northeast of China.", "China is in southeast Guangdong.", "Guangdong is southeast of Beijing."], "东南部 is the southeast part."),
        M("Which asks “Where in the east?”", "在东部哪儿？", ["东部在哪儿吗？", "哪儿东部在？", "在哪儿东边吗？"], "在 + area + 哪儿."),
        M("Which one is true: New York is…", "纽约在华盛顿的北边。", ["纽约在华盛顿的南边。", "纽约在华盛顿的西边。", "纽约在华盛顿的东南边。"], "New York is north of Washington."),
        F("天津在北京___南边。", "的", ["吗", "们", "呢"], "A 在 B 的 南边.", tr="Tianjin is south of Beijing."),
        F("香港在广州的___边。 (south)", "南", ["东", "西", "北"], "Hong Kong is south of Guangzhou.", tr="Hong Kong is south of Guangzhou."),
    ],
)

# ---------------------------------------------------------------------------- 83
L83 = lesson(
    "Cities, states and bases",
    "大城市 · 小城市 · 纽约州 · 军事基地",
    requires=[],
    cards=[
        card("Big city, small city",
             "城市 (chéngshì) is a city. Add 大 (big) or 小 (small): 大城市 and 小城市. 州 (zhōu) is a state; the big divisions of China are provinces, 省 (shěng). "
             "Add 州 to a state's short name: 纽约州 is New York state, and 德州 and 加州 are Texas and California. "
             "A place name takes 的 and 一个 when you describe it: 纽约州的一个小城市, “a small city in New York State”.",
             tables=[wtable([("城市", "cheng2shi4", "a city"), ("大城市", "da4 cheng2shi4", "a big city"), ("小城市", "xiao3 cheng2shi4", "a small city"), ("州", "zhou1", "a state"),
                             ("省", "sheng3", "a province"), ("纽约州", "niu3yue1zhou1", "New York State"), ("德州", "de2zhou1", "Texas"), ("加州", "jia1zhou1", "California"),
                             ("四川", "si4chuan1", "Sichuan"), ("军事基地", "jun1shi4 ji1di4", "a military base"), ("基地", "ji1di4", "a base")])]),
        card("Describing a place",
             "Say what kind of place it is with 是 and the size, or place it with 在: 上海是一个大城市. 我父母现在住在西部的一个军事基地 is “My parents now live on a military base in the west”.",
             examples=[ex("上海是一个大城市。", "shang4hai3 shi4 yi2 ge4 da4 cheng2shi4", "Shanghai is a big city.", hl="大城市"),
                       ex("我的老家在纽约州的一个小城市。", "wo3 de5 lao3jia1 zai4 niu3yue1zhou1 de5 yi2 ge4 xiao3 cheng2shi4", "My hometown is a small city in New York State.", hl="小城市"),
                       ex("我父母住在西部的一个军事基地。", "wo3 fu4mu3 zhu4 zai4 xi1bu4 de5 yi2 ge4 jun1shi4 ji1di4", "My parents live on a military base in the west.", hl="军事基地"),
                       ex("德州很大，在美国南部。", "de2zhou1 hen3 da4, zai4 mei3guo2 nan2bu4", "Texas is very big, in the southern United States.")]),
    ],
    exercises=[
        mean("城市", "cheng2shi4", "a city", ["a country", "a village", "a state"]),
        mean("大城市", "da4 cheng2shi4", "a big city", ["a small city", "a big state", "a big base"]),
        mean("小城市", "xiao3 cheng2shi4", "a small city", ["a big city", "a small state", "a small base"]),
        mean("州", "zhou1", "a state", ["a city", "a province", "a country"]),
        mean("省", "sheng3", "a province", ["a state", "a city", "a country"]),
        mean("基地", "ji1di4", "a base", ["a school", "a hospital", "a company"]),
        mean("军事基地", "jun1shi4 ji1di4", "a military base", ["a military school", "a city", "a hospital"]),
        rd("城市", "cheng2shi4", ["cheng4shi4", "cheng2shi2", "chen2shi4"]),
        rd("基地", "ji1di4", ["ji1di2", "ji2di4", "ji1di3"]),
        rd("州", "zhou1", ["zhou2", "zhou3", "zhou4"]),
        M("How do you say “a small city in New York State”?", "纽约州的一个小城市", ["一个小城市纽约州", "纽约州一个的小城市", "小城市的纽约州一个"], "place + 的 + 一个 + description."),
        M("What does 德州 stand for?", "Texas", ["Tennessee", "Tokyo", "Toronto"], "德州 is Texas."),
        M("What does 加州 stand for?", "California", ["Canada", "Colorado", "Texas"], "加州 is California."),
        M("What does 我父母住在一个军事基地 say?", "My parents live on a military base.", ["My parents work on a base.", "My parents are soldiers.", "My parents have a base."], "住在 is live at."),
        F("上海是一个大城___。", "市", ["们", "吗", "呢"], "城市 is a city.", tr="Shanghai is a big city."),
        F("我的老家在纽约___的一个小城市。", "州", ["们", "吗", "呢"], "纽约州 is New York State.", tr="My hometown is a small city in New York State."),
    ],
)

# ---------------------------------------------------------------------------- 84
L84 = lesson(
    "Where are you from?",
    "你是哪儿人？ · 我是北京人 · 我是广东人",
    requires=[],
    cards=[
        card("哪儿人",
             "To ask where someone is from, say 你是哪儿人？ and answer with the place plus 人: 我是北京人, “I am from Beijing”, literally “a Beijing person”. "
             "It also works with a country (我是美国人) and a region (我是南方人). A polite form is 您是哪儿的人？ and a question about the hometown itself is 你的老家在哪儿？ "
             "When you speak about a group, 都 means all of them, and 不都 means “not all”.",
             tables=[wtable([("你是哪儿人？", "ni3 shi4 na3r5 ren2", "Where are you from?"), ("您是哪儿的人？", "nin2 shi4 na3r5 de5 ren2", "Where are you from? (polite)"),
                             ("我是北京人。", "wo3 shi4 bei3jing1 ren2", "I am from Beijing."), ("她是广东人。", "ta1 shi4 guang3dong1 ren2", "She is from Guangdong."),
                             ("他是美国人。", "ta1 shi4 mei3guo2 ren2", "He is American.")])]),
        card("Southerners and northerners",
             "If you only know the region, say 南方人 or 北方人. A group can be mixed, and then you say 有 … 也有 …, “there are … and also …”.",
             examples=[ex("你是哪儿人？ 我是上海人。", "ni3 shi4 na3r5 ren2? wo3 shi4 shang4hai3 ren2", "Where are you from? I am from Shanghai.", hl="哪儿人"),
                       ex("您是南方人？ 对，我是广东人。", "nin2 shi4 nan2fang1ren2? dui4, wo3 shi4 guang3dong1 ren2", "You are a southerner? Yes, I am from Guangdong."),
                       ex("我们的老师有南方人，也有北方人。", "wo3men5 de5 lao3shi1 you3 nan2fang1ren2, ye3 you3 bei3fang1ren2", "Among our teachers there are southerners and northerners.", hl="有"),
                       ex("张老师是北方人，她的老家在西安。", "zhang1 lao3shi1 shi4 bei3fang1ren2, ta1 de5 lao3jia1 zai4 xi1'an1", "Teacher Zhang is a northerner; her hometown is in Xi'an.")]),
    ],
    exercises=[
        mean("你是哪儿人？", "ni3 shi4 na3r5 ren2", "Where are you from?", ["Who are you?", "Where do you live?", "How old are you?"]),
        mean("广东人", "guang3dong1 ren2", "a person from Guangdong", ["a southerner", "a Chinese teacher", "a person from Beijing"]),
        mean("北方人", "bei3fang1ren2", "a northerner", ["a southerner", "an easterner", "a person from the west"]),
        mean("南方人", "nan2fang1ren2", "a southerner", ["a northerner", "an easterner", "a person from the west"]),
        rd("广东", "guang3dong1", ["guang3dong2", "guang4dong1", "guan3dong1"]),
        M("What do you say to ask where someone is from?", "你是哪儿人？", ["你是什么？", "你在哪儿？", "你叫什么？"], "哪儿人 asks where."),
        M("How do you say “I am from Beijing”?", "我是北京人。", ["我在北京人。", "我是人北京。", "北京是我人。"], "place + 人."),
        M("What does 我是南方人 say?", "I am a southerner.", ["I am going south.", "I live in the south.", "I teach in the south."], "南方人 is a southerner."),
        M("Which means “There are southerners and also northerners”?", "有南方人，也有北方人。", ["南方人是北方人。", "有南方人和也北方人。", "都是南方人。"], "有…也有…"),
        M("Which is the polite form of the question?", "您是哪儿的人？", ["你是谁的人？", "你是哪里吗？", "您在哪儿人？"], "您 is polite."),
        M("What does 她的老家在西安 say?", "Her hometown is in Xi'an.", ["She works in Xi'an.", "She is old.", "She lives in Xi'an now."], "老家 is hometown."),
        F("你是哪儿___？", "人", ["们", "吗", "呢"], "哪儿人 is where from.", tr="Where are you from?"),
        F("我是上海___。", "人", ["们", "吗", "呢"], "上海人 is from Shanghai.", tr="I am from Shanghai."),
        F("张老师是北方人，她的___家在西安。", "老", ["吗", "们", "呢"], "老家 is hometown.", tr="Teacher Zhang is a northerner; her hometown is in Xi'an."),
    ],
)

# ---------------------------------------------------------------------------- 85
L85 = lesson(
    "Born and grown up",
    "我是在那儿出生，长大的。 · 长 zhǎng",
    requires=[],
    cards=[
        card("长大: to grow up",
             "长大 (zhǎngdà) means “to grow up”. Here 长 is read zhǎng, “to grow”, and not cháng, “long”. "
             "It fits the 是…的 pattern you already know, since you know the person grew up and now give the place: 我是在那儿长大的. "
             "You can join two verbs after one place: 我是在四川出生，长大的.",
             tables=[wtable([("长大", "zhang3da4", "to grow up"), ("长", "zhang3", "to grow (not cháng, long)"), ("出生", "chu1sheng1", "to be born"), ("那儿", "na4r5", "there"),
                             ("这儿", "zhe4r5", "here"), ("哪儿", "na3r5", "where")])]),
        card("Telling your story",
             "Combine what you know. After a question like 你是在那儿出生的吗？, a full answer repeats the pattern.",
             examples=[ex("你是在哪儿长大的？ 我是在纽约长大的。", "ni3 shi4 zai4 na3r5 zhang3da4 de5? wo3 shi4 zai4 niu3yue1 zhang3da4 de5", "Where did you grow up? I grew up in New York.", hl="长大"),
                       ex("我是在那儿出生的，也是在那儿长大的。", "wo3 shi4 zai4 na4r5 chu1sheng1 de5, ye3 shi4 zai4 na4r5 zhang3da4 de5", "I was born there and grew up there too."),
                       ex("吴老师是在四川出生，长大的。", "wu2 lao3shi1 shi4 zai4 si4chuan1 chu1sheng1, zhang3da4 de5", "Teacher Wu was born and grew up in Sichuan."),
                       ex("我不是在老家长大的。", "wo3 bu2 shi4 zai4 lao3jia1 zhang3da4 de5", "I did not grow up in my hometown.")]),
    ],
    exercises=[
        mean("长大", "zhang3da4", "to grow up", ["to be born", "to get old", "to be tall"]),
        mean("那儿", "na4r5", "there", ["here", "where", "which"]),
        mean("这儿", "zhe4r5", "here", ["there", "where", "this"]),
        mean("哪儿", "na3r5", "where", ["here", "there", "who"]),
        rd("长", "zhang3", ["zhang1", "zhang4", "zhan3"]),
        rd("长大", "zhang3da4", ["zhang3da1", "zhang4da4", "zhang2da4"]),
        M("How is 长 read in 长大?", "zhǎng", ["cháng", "zhāng", "chǎng"], "长 is zhǎng when it means to grow."),
        M("Which asks “Where did you grow up?”", "你是在哪儿长大的？", ["你是哪儿长大的人？", "你在长大哪儿？", "你长大是哪儿？"], "是 + 在哪儿 + 长大 + 的."),
        M("What does 我是在纽约长大的 say?", "I grew up in New York.", ["I live in New York.", "I was born in New York.", "I am a New Yorker."], "长大 is to grow up."),
        M("How do you say “Teacher Wu was born and grew up in Sichuan”?", "吴老师是在四川出生，长大的。", ["吴老师四川在出生长大。", "吴老师是出生长大在四川的。", "吴老师在四川的出生长大。"], "Two verbs before one 的."),
        M("How do you say “I did not grow up in my hometown”?", "我不是在老家长大的。", ["我是不在老家长大的。", "我没是在老家长大的。", "我在老家不长大的。"], "不是…的."),
        F("我是在那儿___大的。", "长", ["吗", "们", "呢"], "长大 is to grow up.", tr="I grew up there."),
        F("你是在哪儿长大___？", "的", ["吗", "们", "呢"], "是…的.", tr="Where did you grow up?"),
        F("我是在那儿出生的，也是在那儿长大___。", "的", ["吗", "们", "呢"], "是…的.", tr="I was born there and also grew up there."),
    ],
)

# ---------------------------------------------------------------------------- 86
L86 = lesson(
    "Still: 还 and 不…了",
    "你父母还住在那儿吗？ · 他们不住在那儿了。",
    requires=[],
    cards=[
        card("还 means “still”",
             "还 (hái) before a verb means “still” or “yet”. 她还教我们中文 is “She still teaches us Chinese”. To ask, add 吗: 她还教你们中文吗？ "
             "To say it is no longer so, use 不 … 了: 她不教我们中文了, “She no longer teaches us Chinese”. 了 here marks a change.",
             tables=[table(["Form", "Pattern", "Example"],
                           [["still", "还 + verb", "她儿子还在北京。"], ["no longer", "不 + verb + 了", "她儿子不在北京了。"], ["question", "还 + verb + 吗？", "她儿子还在北京吗？"]], say=[2])]),
        card("Where do your parents live?",
             "A natural conversation about the family uses all three forms together.",
             examples=[ex("你父母还住在那儿吗？ 不住在那儿了。", "ni3 fu4mu3 hai2 zhu4 zai4 na4r5 ma5? bu2 zhu4 zai4 na4r5 le5", "Do your parents still live there? They no longer live there.", hl="还"),
                       ex("她还教我们中文。", "ta1 hai2 jiao1 wo3men5 zhong1wen2", "She still teaches us Chinese."),
                       ex("她不教我们中文了。", "ta1 bu2 jiao1 wo3men5 zhong1wen2 le5", "She no longer teaches us Chinese.", hl="不教"),
                       ex("我爷爷奶奶还住在老家。", "wo3 ye2ye5 nai3nai5 hai2 zhu4 zai4 lao3jia1", "My grandparents still live in our hometown.")]),
    ],
    exercises=[
        mean("还", "hai2", "still, yet", ["also", "very", "already"]),
        mean("住", "zhu4", "to live", ["to grow", "to be born", "to work"]),
        rd("还", "hai2", ["hai1", "hai3", "hai4"]),
        rd("住", "zhu4", ["zhu1", "zhu2", "zhu3"]),
        M("What does 她还教我们中文 mean?", "She still teaches us Chinese.", ["She no longer teaches us Chinese.", "She also learns Chinese.", "She teaches us now."], "还 is still."),
        M("What does 她不教我们中文了 mean?", "She no longer teaches us Chinese.", ["She still teaches us Chinese.", "She does not like Chinese.", "She teaches us tomorrow."], "不…了 is no longer."),
        M("How do you ask “Does he still live there?”", "他还住在那儿吗？", ["他住在还那儿吗？", "他还吗住在那儿？", "还他住在那儿吗？"], "还 + verb + 吗."),
        M("How do you say “They no longer live there”?", "他们不住在那儿了。", ["他们没住在那儿了。", "他们不了住在那儿。", "他们不住在那儿。"], "不 + verb + 了."),
        M("What does 了 do in 不住了?", "Marks a change", ["Marks a question", "Makes it past tense", "Means “and”"], "了 shows the situation changed."),
        M("What does 我爷爷奶奶还住在老家 say?", "My grandparents still live in our hometown.", ["My grandparents no longer live at home.", "My grandparents live far away.", "My grandparents are old."], "还住在 is still lives in."),
        F("她儿子还在北京___？", "吗", ["们", "呢", "的"], "吗 ends the question.", tr="Is her son still in Beijing?"),
        F("她儿子不在北京___。", "了", ["吗", "们", "呢"], "不…了 is no longer.", tr="Her son is no longer in Beijing."),
        F("你父母___住在那儿吗？", "还", ["吗", "们", "呢"], "还 is still.", tr="Do your parents still live there?"),
        F("他们不___在那儿了。 (live)", "住", ["吗", "们", "呢"], "不住在 is not live at.", tr="They no longer live there."),
    ],
)

# ---------------------------------------------------------------------------- 87
L87 = lesson(
    "Which one? 哪 + measure word",
    "哪位老师 · 哪个州 · 哪国人 · 哪个班",
    requires=[],
    cards=[
        card("哪 needs a measure word",
             "哪 (nǎ) means “which”. In Chinese a noun that follows 哪 needs a measure word in between: 哪位老师, “which teacher”, and never 哪老师. "
             "The measure word is the same one you would use to count the noun: 位 for people you respect, 个 for most things, and 国 in 哪国人, “which country's person”.",
             tables=[table(["Question", "Meaning"],
                           [["哪位老师是上海人？", "Which teacher is from Shanghai?"], ["哪个同学是你们的班长？", "Which student is your class leader?"],
                            ["你是哪国人？", "Which country are you from?"], ["你的老家在哪个州？", "Which state is your hometown in?"], ["你是哪个班的学生？", "Which class are you in?"]], say=[0])]),
        card("Answering",
             "Answer by naming the thing. 哪 (nǎ, “which”) is a different word from 哪儿 (nǎr, “where”) and from 那 (nà, “that”).",
             examples=[ex("哪位老师是北京人？ 张老师是北京人。", "na3 wei4 lao3shi1 shi4 bei3jing1 ren2? zhang1 lao3shi1 shi4 bei3jing1 ren2", "Which teacher is from Beijing? Teacher Zhang.", hl="哪位"),
                       ex("你的老家在哪个州？ 在加州。", "ni3 de5 lao3jia1 zai4 na3 ge4 zhou1? zai4 jia1zhou1", "Which state is your hometown in? California.", hl="哪个"),
                       ex("你是哪国人？ 我是美国人。", "ni3 shi4 na3 guo2 ren2? wo3 shi4 mei3guo2 ren2", "Which country are you from? I am American.", hl="哪国"),
                       ex("你是哪个班的学生？", "ni3 shi4 na3 ge4 ban1 de5 xue2sheng5", "Which class are you a student in?")]),
    ],
    exercises=[
        mean("哪", "na3", "which", ["that", "this", "who"]),
        rd("哪", "na3", ["na1", "la3", "ma3"]),
        M("What does 哪位老师是上海人？ ask?", "Which teacher is from Shanghai?", ["Where is the teacher from?", "Who is the teacher?", "Is the teacher from Shanghai?"], "哪位 is which (person)."),
        M("What does 你是哪国人？ ask?", "Which country are you from?", ["Where is your home?", "Who are you?", "How many people are in your country?"], "哪国人 is which country's person."),
        M("Which is correct?", "哪位老师", ["哪老师", "哪们老师", "哪的老师"], "哪 needs a measure word."),
        M("Which is correct?", "你的老家在哪个州？", ["你的老家在哪州？", "你的老家哪个在州？", "你的老家在州哪个？"], "哪个州."),
        M("Which asks “Which class are you in?”", "你是哪个班的学生？", ["你是班哪个的学生？", "你的班是哪学生？", "你是学生哪个班？"], "哪个班."),
        M("Which question asks “Which student is the class leader?”", "哪个同学是班长？", ["同学哪个班长是？", "哪同学是班长？", "是班长哪个同学？"], "哪个 + noun."),
        M("Which measure word is polite for “which teacher”?", "位", ["个", "口", "们"], "位 is polite for people."),
        M("Are 哪 and 那 the same?", "No: 哪 is “which”, 那 is “that”", ["Yes", "Only in writing", "Only in the south"], "Different characters and tones."),
        F("哪___老师是北京人？", "位", ["们", "吗", "呢"], "哪位老师.", tr="Which teacher is from Beijing?"),
        F("你的老家在哪个___？", "州", ["们", "吗", "呢"], "哪个州.", tr="Which state is your hometown in?"),
        F("你是哪___人？ (country)", "国", ["们", "吗", "呢"], "哪国人.", tr="Which country are you from?"),
        F("你是哪个班___学生？", "的", ["们", "吗", "呢"], "的 links 班 and 学生.", tr="Which class are you a student in?"),
    ],
)

# ---------------------------------------------------------------------------- 88
L88 = lesson(
    "Surprise: the question with no particle",
    "你是南方人？ · 你没有哥哥？",
    requires=[],
    cards=[
        card("Rising tone, no particle",
             "A yes/no question usually ends in 吗 or 吧. But when you are surprised, you can take the word order of a statement, add no particle at all, and raise your voice at the end. "
             "你是南方人？ means “You are from the south?!”. You use it when you have just learned something unexpected, and you want it confirmed.",
             tables=[table(["Statement", "Surprised question", "Feeling"],
                           [["你是老师。", "你是老师？", "I did not know you were a teacher."], ["你没有哥哥。", "你没有哥哥？", "You have no older brother?"],
                            ["今天是星期三。", "今天是星期三？", "Is it really Wednesday?"]], say=[0, 1])]),
        card("Choosing between the three",
             "吗 asks openly. 吧 says “I think so, right?”. A question with no particle says “Really? I had not expected that”.",
             examples=[ex("我是军人。 你是军人？", "wo3 shi4 jun1ren2. ni3 shi4 jun1ren2", "I am in the military. You are?!", hl="你是军人？"),
                       ex("我们家都是军人。 你们家都是军人？", "wo3men5 jia1 dou1 shi4 jun1ren2. ni3men5 jia1 dou1 shi4 jun1ren2", "Everyone in my family is in the military. Everyone?!"),
                       ex("您是中文系老师？", "nin2 shi4 zhong1wen2 xi4 lao3shi1", "You are a teacher in the Chinese department?!")]),
    ],
    exercises=[
        M("What does 你是南方人？ express?", "Surprise", ["A command", "A negative", "A polite request"], "No particle plus a rising tone shows surprise."),
        M("What happens to the voice at the end?", "It rises", ["It falls", "It stays low", "It whispers"], "A rising tone."),
        M("Which sentence is a surprised question?", "你没有哥哥？", ["你没有哥哥吗？", "你没有哥哥吧？", "你没有哥哥呢？"], "No particle."),
        M("Which one is the open yes/no question?", "你是军人吗？", ["你是军人？", "你是军人吧？", "你是军人呢？"], "吗 asks openly."),
        M("Which one expects the answer yes?", "你是军人吧？", ["你是军人？", "你是军人吗？", "你是军人了？"], "吧 expects confirmation."),
        M("How do you show surprise at “Today is Wednesday”?", "今天是星期三？", ["今天是星期三吗？", "今天是星期三吧？", "今天是星期三呢？"], "Rising tone."),
        M("Which means “Everyone in your family is in the military?!”", "你们家都是军人？", ["你们家都是军人吗？", "你们家都是军人吧？", "你们家是都军人？"], "Statement order plus a rising tone."),
        M("Which word order does a surprised question use?", "The same as a statement", ["Verb first", "Object first", "Question word first"], "The word order is unchanged."),
        M("What do you add to a surprised question?", "Nothing", ["吗", "吧", "呢"], "No particle."),
        F("你有孩子___？ (an open question)", "吗", ["们", "呢", "的"], "吗 asks openly.", tr="Do you have children?"),
        F("你是军人___？ (you think so)", "吧", ["们", "呢", "的"], "吧 expects yes.", tr="You are in the military, right?"),
        F("我们___是老师。 (all of us)", "都", ["吗", "们", "呢"], "都 is all.", tr="All of us are teachers."),
    ],
)

# ---------------------------------------------------------------------------- 89
L89 = lesson(
    "All, not all, none: 都, 不都, 都不",
    "我们都是 · 我们不都是 · 我们都不是",
    requires=[],
    cards=[
        card("Three degrees",
             "都 (dōu) means “all” or “both” and sits after the subject, before the verb. The order of 不 and 都 changes the meaning. "
             "不都 is a partial negative: “not all”, some are and some are not. 都不 is a full negative: “none”, “neither”. "
             "So 我们班不都是海军 means some of the class are in the Navy and some are not, while 我们班都不是海军 means nobody in the class is.",
             tables=[table(["Form", "Example", "Meaning"],
                           [["都", "我们都学中文。", "All of us study Chinese."], ["不都", "我们不都是中文系的学生。", "Not all of us are Chinese majors."],
                            ["都不", "他们都不是韩语系的学生。", "None of them are Korean majors."]], say=[1])]),
        card("Pairs of people",
             "With two people, 都 is “both” and 都不 is “neither”.",
             examples=[ex("他和他太太都是美国人。", "ta1 he2 ta1 tai4tai5 dou1 shi4 mei3guo2 ren2", "He and his wife are both American.", hl="都"),
                       ex("我弟弟和妹妹不都住在老家。", "wo3 di4di5 he2 mei4mei5 bu4 dou1 zhu4 zai4 lao3jia1", "My younger brother and sister do not both live in our hometown.", hl="不都"),
                       ex("我和我太太都不是南方人。", "wo3 he2 wo3 tai4tai5 dou1 bu2 shi4 nan2fang1ren2", "My wife and I are neither of us southerners.", hl="都不")]),
    ],
    exercises=[
        mean("都", "dou1", "all, both", ["also", "very", "not"]),
        M("How is 都 read in 我们都是学生?", "dōu", ["dū", "dóu", "dǒu"], "As an adverb, 都 is dōu."),
        M("What does 不都 mean?", "not all", ["none", "all", "also"], "不都 is a partial negative."),
        M("What does 都不 mean?", "none, neither", ["not all", "all", "both"], "都不 is a full negative."),
        M("What does 我们不都是海军 mean?", "Not all of us are in the Navy.", ["None of us are in the Navy.", "All of us are in the Navy.", "We are the Navy."], "不都 is not all."),
        M("What does 我们都不是海军 mean?", "None of us are in the Navy.", ["Not all of us are in the Navy.", "All of us are in the Navy.", "We are not many."], "都不 is none."),
        M("How do you say “Both of them are American”?", "他们都是美国人。", ["他们是都美国人。", "都他们是美国人。", "他们美国人都是。"], "都 before the verb."),
        M("How do you say “Neither of them is a southerner”?", "他们都不是南方人。", ["他们不都是南方人。", "他们是都不南方人。", "都不他们是南方人。"], "都不 is neither."),
        M("How do you say “Not all of them are southerners”?", "他们不都是南方人。", ["他们都不是南方人。", "他们不是都南方人。", "他们是不都南方人。"], "不都 is not all."),
        M("Where does 都 go?", "After the subject, before the verb", ["At the end", "Before the subject", "After the verb"], "都 is an adverb."),
        F("我们___学中文。 (all of us)", "都", ["吗", "们", "呢"], "都 is all.", tr="All of us study Chinese."),
        F("我们不___是中文系的学生。 (not all)", "都", ["吗", "们", "呢"], "不都 is not all.", tr="Not all of us are Chinese majors."),
        F("他们都___是韩语系的学生。 (none)", "不", ["吗", "们", "呢"], "都不 is none.", tr="None of them are Korean majors."),
        F("他和他太太都是美国___。", "人", ["吗", "们", "呢"], "都 is both.", tr="He and his wife are both American."),
    ],
)

# ---------------------------------------------------------------------------- 90
L90 = lesson(
    "The -r ending",
    "花儿 · 这儿 · 哪儿 · 一会儿 · 玩儿",
    requires=[],
    cards=[
        card("er becomes r",
             "The sound er (ér, 儿, “son”) can be added at the end of a word, and then it shrinks to a retroflex r. It is typical of the Beijing dialect and is spoken by many northerners. "
             "In writing, the character 儿 is added, and in pinyin only an r: 花 + 儿 gives 花儿 (huār), “flower”. "
             "Curl your tongue back as you finish the syllable. After -i, -n or -ng, those endings fade when you say it, but the pinyin keeps them: 小孩儿 (xiǎoháir), 玩儿 (wánr), 电影儿 (diànyǐngr).",
             tables=[wtable([("儿", "er2", "son, child"), ("歌儿", "ge1r5", "a song"), ("花儿", "hua1r5", "a flower"), ("小孩儿", "xiao3hai2r5", "a small child"),
                             ("男孩儿", "nan2hai2r5", "a boy"), ("女孩儿", "nv3hai2r5", "a girl"), ("玩儿", "wan2r5", "to play"), ("一会儿", "yi2hui4r5", "a little while")])]),
        card("What the r does",
             "The -r can do three jobs. It can make a thing small or dear: 小鸟儿 is a little bird. It can change the meaning of a word: 头 is a head but 头儿 is a boss. "
             "It can turn a verb into a noun: 画 is to draw and 画儿 is a picture. Words you will use all the time are 这儿, 那儿 and 哪儿, “here, there, where”.",
             tables=[wtable([("小鸟儿", "xiao3niao3r5", "a little bird"), ("头", "tou2", "a head"), ("头儿", "tou2r5", "a boss, a leader"), ("画", "hua4", "to draw"), ("画儿", "hua4r5", "a picture"),
                             ("这儿", "zhe4r5", "here"), ("那儿", "na4r5", "there"), ("哪儿", "na3r5", "where"), ("一块儿", "yi2kuai4r5", "together")])]),
    ],
    exercises=[
        mean("这儿", "zhe4r5", "here", ["there", "where", "this"]),
        mean("那儿", "na4r5", "there", ["here", "where", "that"]),
        mean("哪儿", "na3r5", "where", ["here", "there", "who"]),
        mean("花儿", "hua1r5", "a flower", ["a song", "a picture", "a small child"]),
        mean("歌儿", "ge1r5", "a song", ["a flower", "a picture", "a bird"]),
        mean("玩儿", "wan2r5", "to play", ["to eat", "to run", "to work"]),
        mean("一会儿", "yi2hui4r5", "a little while", ["a moment ago", "together", "a meeting"]),
        mean("一块儿", "yi2kuai4r5", "together", ["a little while", "a piece", "everyone"]),
        mean("头儿", "tou2r5", "a boss, a leader", ["a head", "a hat", "a hair"]),
        mean("画儿", "hua4r5", "a picture", ["to draw", "a flower", "a story"]),
        mean("小孩儿", "xiao3hai2r5", "a small child", ["a small bird", "a boy", "a student"]),
        M("What does 男孩儿 mean?", "a boy", ["a girl", "a small child", "a man"], "男孩儿 is a boy."),
        M("What does 女孩儿 mean?", "a girl", ["a boy", "a woman", "a daughter"], "女孩儿 is a girl."),
        M("How is 花儿 written in pinyin?", "huār", ["huá", "huǎr", "huàr"], "huā + r."),
        M("How is 哪儿 written in pinyin?", "nǎr", ["nàr", "nǎ", "nár"], "nǎ + r."),
        M("How is 这儿 written in pinyin?", "zhèr", ["zhér", "zhè", "zhēr"], "zhè + r."),
        M("What is the difference between 头 and 头儿?", "头 is a head; 头儿 is a boss", ["No difference", "头儿 is a small head", "头 is a boss"], "The r can change the meaning."),
        M("What is the difference between 画 and 画儿?", "画 is to draw; 画儿 is a picture", ["No difference", "画儿 is to paint", "画 is a picture"], "The r can change the part of speech."),
        M("What does the character 儿 stand for in 花儿?", "The r ending", ["A son", "A flower", "A small child"], "It is written 儿 and pronounced r."),
        F("你的老家在哪___？", "儿", ["吗", "们", "呢"], "哪儿 is where.", tr="Where is your hometown?"),
        F("我们一块___去。", "儿", ["吗", "们", "呢"], "一块儿 is together.", tr="We are going together."),
    ],
)

# ---------------------------------------------------------------------------- 91
L91 = lesson(
    "Ship words",
    "军舰 · 潜艇 · 驱逐舰 · 航空母舰",
    requires=[],
    cards=[
        card("舰 and 艇",
             "Two characters tell you the size of a vessel. 舰 (jiàn) is a large warship and 艇 (tǐng) a small boat or a submarine. "
             "Put a word in front to say what the vessel does: 巡洋 means cruising the oceans, 驱逐 is to drive off, 扫雷 is to sweep mines and 补给 is to supply. "
             "These are names to recognise; later lessons use them in sentences.",
             tables=[wtable([("军舰", "jun1jian4", "a warship"), ("潜艇", "qian2ting3", "a submarine"), ("快艇", "kuai4ting3", "a speedboat"), ("巡逻艇", "xun2luo2ting3", "a patrol boat"),
                             ("巡洋舰", "xun2yang2jian4", "a cruiser"), ("补给舰", "bu3ji3jian4", "a supply ship"), ("驱逐舰", "qu1zhu2jian4", "a destroyer"),
                             ("登陆舰", "deng1lu4jian4", "a landing ship"), ("扫雷舰", "sao3lei2jian4", "a minesweeper"), ("航空母舰", "hang2kong1 mu3jian4", "an aircraft carrier"),
                             ("导弹巡航舰", "dao3dan4 xun2hang2jian4", "a missile cruiser")])]),
        card("A word to use them",
             "海军 (hǎijūn) is the Navy. 他是海军 says he is a sailor. "
             "For now, point and name the vessels with 这是 and 那是.",
             examples=[ex("这是军舰。", "zhe4 shi4 jun1jian4", "This is a warship."),
                       ex("那是潜艇。", "na4 shi4 qian2ting3", "That is a submarine."),
                       ex("他是海军，在驱逐舰上工作。", "ta1 shi4 hai3jun1, zai4 qu1zhu2jian4 shang4 gong1zuo4", "He is in the Navy and works on a destroyer.")]),
    ],
    exercises=[
        mean("军舰", "jun1jian4", "a warship", ["an aircraft", "a barracks", "a base"]),
        mean("潜艇", "qian2ting3", "a submarine", ["a speedboat", "a warship", "a patrol boat"]),
        mean("快艇", "kuai4ting3", "a speedboat", ["a submarine", "a destroyer", "a cruiser"]),
        mean("巡逻艇", "xun2luo2ting3", "a patrol boat", ["a speedboat", "a submarine", "a supply ship"]),
        mean("巡洋舰", "xun2yang2jian4", "a cruiser", ["a destroyer", "a minesweeper", "a landing ship"]),
        mean("补给舰", "bu3ji3jian4", "a supply ship", ["a cruiser", "a warship", "a patrol boat"]),
        mean("驱逐舰", "qu1zhu2jian4", "a destroyer", ["a cruiser", "a minesweeper", "a submarine"]),
        mean("登陆舰", "deng1lu4jian4", "a landing ship", ["a supply ship", "a destroyer", "a speedboat"]),
        mean("扫雷舰", "sao3lei2jian4", "a minesweeper", ["a destroyer", "a landing ship", "a cruiser"]),
        mean("航空母舰", "hang2kong1 mu3jian4", "an aircraft carrier", ["a supply ship", "a cruiser", "a destroyer"]),
        mean("导弹巡航舰", "dao3dan4 xun2hang2jian4", "a missile cruiser", ["a destroyer", "a patrol boat", "an aircraft carrier"]),
        rd("舰", "jian4", ["jian1", "jian2", "jian3"]),
        rd("艇", "ting3", ["ting1", "ting2", "ting4"]),
        rd("潜艇", "qian2ting3", ["qian2ting1", "qian3ting3", "qian2ting4"]),
        rd("驱逐舰", "qu1zhu2jian4", ["qu1zhu1jian4", "qu2zhu2jian4", "qu1zhu2jian1"]),
        M("What does 舰 tell you about a vessel?", "It is a large warship", ["It is small", "It flies", "It is a boat for fishing"], "舰 is a large warship."),
        M("What does 艇 tell you?", "It is a small boat", ["It is a large warship", "It flies", "It is a base"], "艇 is a small boat."),
        M("Which means “the Navy”?", "海军", ["空军", "陆军", "军人"], "海 is sea, 军 is military."),
        F("那是潜___。 (a submarine)", "艇", PART, "潜艇 is a submarine.", tr="That is a submarine."),
        F("这是军___。 (a warship)", "舰", PART, "军舰 is a warship.", tr="This is a warship."),
    ],
)

# ---------------------------------------------------------------------------- 92
L92 = lesson(
    "Classroom expressions",
    "现在我们做听力练习 · 请你慢一点儿说",
    requires=[],
    cards=[
        card("What your teacher says",
             "These are phrases your teacher uses every day. The first tells you to sit: 上课了，请坐好, “Class has started, please sit properly”. "
             "Then comes 现在我们做 plus a kind of 练习 (liànxí, “exercise”). Learn the kinds by their parts: 语音 is pronunciation, 听力 listening, 阅读 reading, 会话 conversation, 翻译 translation, 听写 dictation, 写字 writing characters.",
             tables=[wtable([("练习", "lian4xi2", "an exercise, to practise"), ("语音", "yu3yin1", "pronunciation"), ("听力", "ting1li4", "listening"), ("阅读", "yue4du2", "reading"),
                             ("会话", "hui4hua4", "conversation"), ("翻译", "fan1yi4", "translation"), ("听写", "ting1xie3", "dictation"), ("写字", "xie3zi4", "to write characters")])]),
        card("Phrases to ask the teacher",
             "Two requests are worth learning now. 大点儿声 (dà diǎnr shēng) is “louder” and 慢一点儿 (màn yìdiǎnr) is “a little more slowly”. 请 (qǐng) makes both polite.",
             examples=[ex("上课了，请坐好。", "shang4ke4 le5, qing3 zuo4hao3", "Class is starting; please sit properly.", hl="请坐好"),
                       ex("现在我们做听力练习。", "xian4zai4 wo3men5 zuo4 ting1li4 lian4xi2", "Now we do the listening exercise.", hl="听力练习"),
                       ex("请你大点儿声说。", "qing3 ni3 da4 dian3r5 sheng1 shuo1", "Please speak a little louder.", hl="大点儿声"),
                       ex("请你慢一点儿说。", "qing3 ni3 man4 yi4dian3r5 shuo1", "Please speak a little more slowly.", hl="慢一点儿")]),
    ],
    exercises=[
        mean("练习", "lian4xi2", "an exercise, to practise", ["a class", "a test", "a book"]),
        mean("语音", "yu3yin1", "pronunciation", ["listening", "reading", "translation"]),
        mean("听力", "ting1li4", "listening", ["reading", "pronunciation", "dictation"]),
        mean("阅读", "yue4du2", "reading", ["writing", "listening", "translation"]),
        mean("会话", "hui4hua4", "conversation", ["pronunciation", "dictation", "reading"]),
        mean("翻译", "fan1yi4", "translation", ["conversation", "listening", "pronunciation"]),
        mean("听写", "ting1xie3", "dictation", ["translation", "reading", "conversation"]),
        mean("写字", "xie3zi4", "to write characters", ["to read characters", "to speak", "to listen"]),
        rd("练习", "lian4xi2", ["lian4xi1", "lian2xi2", "lian4xi4"]),
        rd("语音", "yu3yin1", ["yu3yin2", "yu2yin1", "yu4yin1"]),
        rd("听力", "ting1li4", ["ting1li2", "ting2li4", "ting1li1"]),
        rd("翻译", "fan1yi4", ["fan1yi2", "fan2yi4", "fan1yi1"]),
        M("What does 上课了，请坐好 mean?", "Class is starting; please sit properly.", ["Class is over; please go.", "Please open your books.", "Please stand up."], "上课了 is class begins."),
        M("What do you say to ask someone to speak louder?", "请你大点儿声说。", ["请你慢一点儿说。", "请你坐好。", "请你写字。"], "大点儿声 is a little louder."),
        M("What do you say to ask someone to speak more slowly?", "请你慢一点儿说。", ["请你大点儿声说。", "请你再说。", "请你坐好。"], "慢一点儿 is a little slower."),
        M("What does 现在我们做阅读练习 mean?", "Now we do the reading exercise.", ["Now we do the listening exercise.", "Now we do the writing exercise.", "Now we do the speaking exercise."], "阅读 is reading."),
        F("现在我们做听___练习。 (listening)", "力", PART, "听力 is listening.", tr="Now we do the listening exercise."),
        F("请你慢一点儿___。 (speak)", "说", PART, "说 is to speak.", tr="Please speak a little more slowly."),
        F("上课了，请___好。 (sit)", "坐", PART, "坐好 is to sit properly.", tr="Class is starting; please sit properly."),
    ],
)

# ---------------------------------------------------------------------------- 93
L93 = lesson(
    "The Chinese family",
    "家人 · 国家 · 四世同堂 · 回老家过春节",
    requires=[],
    cards=[
        card("Family in Chinese life",
             "The family has been central to Chinese society for thousands of years. 国家 (guójiā) is the word for a nation, and it is made of 国 (country) and 家 (family): a nation is a “national family”. "
             "Respect for elders is a core value. The old ideal was 四世同堂 (sìshìtóngtáng): four generations living under one roof. "
             "家人 (jiārén) means the people in your family.",
             tables=[wtable([("家人", "jia1ren2", "family members"), ("国家", "guo2jia1", "a nation"), ("家庭", "jia1ting2", "a family, a household"),
                             ("四世同堂", "si4shi4tong2tang2", "four generations under one roof"), ("回老家", "hui2 lao3jia1", "to go back to one's hometown")])]),
        card("Spring Festival and small families",
             "Around the Spring Festival, millions of people travel to their hometowns to be with their families. It is the biggest yearly journey of people in the world. "
             "From 1979 until 2016, a policy limited most couples to one child (独生子女政策), so many children grew up as an only child, a 独生子女 (dúshēng zǐnǚ). "
             "Today the typical urban family is small, and more grandparents help raise children, while 养老院 (yǎnglǎoyuàn), homes for older people, are a newer trend.",
             examples=[ex("春节我要回老家。", "chun1jie2 wo3 yao4 hui2 lao3jia1", "I am going back to my hometown for the Spring Festival.", hl="回老家"),
                       ex("我爷爷奶奶还住在老家，我们一起过春节。", "wo3 ye2ye5 nai3nai5 hai2 zhu4 zai4 lao3jia1, wo3men5 yi4qi3 guo4 chun1jie2", "My grandparents still live in our hometown, and we celebrate the Spring Festival together."),
                       ex("他是独生子女。", "ta1 shi4 du2sheng1 zi3nv3", "He is an only child.", hl="独生子女"),
                       ex("我的家人都在北京。", "wo3 de5 jia1ren2 dou1 zai4 bei3jing1", "My family are all in Beijing.")]),
    ],
    exercises=[
        mean("家人", "jia1ren2", "family members", ["a hometown", "a nation", "a household"]),
        mean("国家", "guo2jia1", "a nation", ["a family", "a hometown", "a city"]),
        mean("家庭", "jia1ting2", "a family, a household", ["a nation", "a city", "a base"]),
        M("What does 四世同堂 describe?", "Four generations under one roof", ["Four brothers in one city", "A very large house", "Four years of school"], "世 is a generation."),
        mean("回老家", "hui2 lao3jia1", "to go back to one's hometown", ["to go to school", "to be born", "to buy a house"]),
        mean("独生子女", "du2sheng1 zi3nv3", "an only child", ["a twin", "a grandchild", "a stepchild"]),
        rd("家人", "jia1ren2", ["jia1ren4", "jia2ren2", "jia1ren1"]),
        rd("国家", "guo2jia1", ["guo2jia2", "guo3jia1", "guo2jia4"]),
        rd("回", "hui2", ["hui1", "hui3", "hui4"]),
        M("What two parts make up 国家?", "国 (country) and 家 (family)", ["国 (country) and 人 (person)", "大 (big) and 家 (family)", "国 (country) and 老 (old)"], "A nation is a national family."),
        M("When do many people go back to their hometown?", "At the Spring Festival", ["On National Day only", "On Mondays", "At New Year's Eve only"], "春节 is the main time."),
        M("From when to when was the one-child policy in effect?", "1979 to 2016", ["1949 to 1979", "1990 to 2000", "2016 to now"], "It ran from 1979 until 2016."),
        M("What does 他是独生子女 say?", "He is an only child.", ["He is a twin.", "He has two sisters.", "He is a student."], "独生子女 is an only child."),
        F("春节我要___老家。 (go back to)", "回", PART, "回 is to go back.", tr="I am going back to my hometown for the Spring Festival."),
        F("我的家___都在北京。 (family members)", "人", PART, "家人 are family members.", tr="My family are all in Beijing."),
    ],
)

# ---------------------------------------------------------------------------- 94
L94 = lesson(
    "Review: hometowns and places",
    "老家 · 东南西北 · 哪儿人 · 还 · 哪 + 位 · 都",
    requires=[],
    cards=[
        card("What you can now do",
             "You can say where you are from and where you grew up, place a city on the map, tell whether someone still lives somewhere, ask “which one” and say “all”, “not all” and “none”. "
             "These questions mix it together.",
             examples=[ex("你的老家在哪儿？ 我的老家在美国东部。", "ni3 de5 lao3jia1 zai4 na3r5? wo3 de5 lao3jia1 zai4 mei3guo2 dong1bu4", "Where is your hometown? In the eastern United States."),
                       ex("你父母还住在那儿吗？ 不住在那儿了。", "ni3 fu4mu3 hai2 zhu4 zai4 na4r5 ma5? bu2 zhu4 zai4 na4r5 le5", "Do your parents still live there? No longer."),
                       ex("我们的老师有南方人，也有北方人。", "wo3men5 de5 lao3shi1 you3 nan2fang1ren2, ye3 you3 bei3fang1ren2", "Among our teachers there are southerners and northerners.")]),
    ],
    exercises=[
        M("Which asks where someone is from?", "你是哪儿人？", ["你在哪儿？", "你是谁？", "你几岁？"], "哪儿人."),
        M("How do you say “The east of the United States”?", "美国东部", ["美国东边人", "东美国部", "美国的东方"], "area + 部."),
        M("Which is the northwest?", "西北", ["北西", "东南", "东北"], "西 + 北."),
        M("How do you say “Tianjin is south of Beijing”?", "天津在北京的南边。", ["北京在天津的南边。", "天津是北京的南边。", "天津南边在北京的。"], "A 在 B 的 南边."),
        M("What does 他不是在这儿长大的 say?", "He did not grow up here.", ["He grew up here.", "He is not here.", "He is not growing."], "不是…的."),
        M("What does 我们不都是南方人 mean?", "Not all of us are southerners.", ["None of us are southerners.", "All of us are southerners.", "We do not know."], "不都 is not all."),
        M("What does 我们都不是南方人 mean?", "None of us are southerners.", ["Not all of us are southerners.", "All of us are southerners.", "Some are."], "都不 is none."),
        M("Which asks “Which state is it in?”", "在哪个州？", ["在哪州？", "哪个在州？", "州在哪个？"], "哪个州."),
        M("Which is the surprised question?", "你是南方人？", ["你是南方人吗？", "你是南方人吧？", "你是南方人呢？"], "No particle."),
        M("Which means “She no longer works here”?", "她不在这儿工作了。", ["她还在这儿工作。", "她没在这儿工作。", "她在这儿不工作。"], "不…了."),
        M("What does 还 mean?", "still", ["also", "very", "all"], "还 is still."),
        mean("老家", "lao3jia1", "hometown", ["a house", "an old man", "a base"]),
        mean("城市", "cheng2shi4", "a city", ["a state", "a nation", "a base"]),
        rd("长大", "zhang3da4", ["zhang3da1", "zhang4da4", "zhang2da4"]),
        F("你的老家在哪个___？", "州", PART, "哪个州.", tr="Which state is your hometown in?"),
        F("你父母___住在那儿吗？", "还", ["吗", "们", "呢"], "还 is still.", tr="Do your parents still live there?"),
        F("我们___不是南方人。 (none of us)", "都", ["吗", "们", "呢"], "都不 is none.", tr="None of us are southerners."),
    ],
)

UNIT = unit("第四课 Hometowns and places", [L80, L81, L82, L83, L84, L85, L86, L87, L88, L89, L90, L91, L92, L93, L94])
