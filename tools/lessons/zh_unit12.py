"""Unit 12: provinces and states (lessons 118-123): China's administrative divisions, provinces and
capitals, American states, the proverb 边学边问，才有学问, review. Original text; the scope follows DLIFLC
Chinese Basic Program Unit 1 Lesson 5, Presentation 2 (Pronunciation Review and Area Studies)."""
from dsl_zh import *

PART = ["吗", "们", "呢"]

# (province hanzi, pinyin, English, capital hanzi, pinyin, English)
NORTH_EAST = [
    ("辽宁", "liao2ning2", "Liaoning", "沈阳", "shen3yang2", "Shenyang"),
    ("吉林", "ji2lin2", "Jilin", "长春", "chang2chun1", "Changchun"),
    ("黑龙江", "hei1long2jiang1", "Heilongjiang", "哈尔滨", "ha1er3bin1", "Harbin"),
    ("河北", "he2bei3", "Hebei", "石家庄", "shi2jia1zhuang1", "Shijiazhuang"),
    ("山西", "shan1xi1", "Shanxi", "太原", "tai4yuan2", "Taiyuan"),
    ("山东", "shan1dong1", "Shandong", "济南", "ji3nan2", "Jinan"),
    ("河南", "he2nan2", "Henan", "郑州", "zheng4zhou1", "Zhengzhou"),
    ("江苏", "jiang1su1", "Jiangsu", "南京", "nan2jing1", "Nanjing"),
    ("浙江", "zhe4jiang1", "Zhejiang", "杭州", "hang2zhou1", "Hangzhou"),
    ("江西", "jiang1xi1", "Jiangxi", "南昌", "nan2chang1", "Nanchang"),
    ("安徽", "an1hui1", "Anhui", "合肥", "he2fei2", "Hefei"),
    ("福建", "fu2jian4", "Fujian", "福州", "fu2zhou1", "Fuzhou"),
]
SOUTH_WEST = [
    ("湖北", "hu2bei3", "Hubei", "武汉", "wu3han4", "Wuhan"),
    ("湖南", "hu2nan2", "Hunan", "长沙", "chang2sha1", "Changsha"),
    ("四川", "si4chuan1", "Sichuan", "成都", "cheng2du1", "Chengdu"),
    ("贵州", "gui4zhou1", "Guizhou", "贵阳", "gui4yang2", "Guiyang"),
    ("云南", "yun2nan2", "Yunnan", "昆明", "kun1ming2", "Kunming"),
    ("陕西", "shan3xi1", "Shaanxi", "西安", "xi1'an1", "Xi'an"),
    ("甘肃", "gan1su4", "Gansu", "兰州", "lan2zhou1", "Lanzhou"),
    ("青海", "qing1hai3", "Qinghai", "西宁", "xi1ning2", "Xining"),
    ("广东", "guang3dong1", "Guangdong", "广州", "guang3zhou1", "Guangzhou"),
    ("海南", "hai3nan2", "Hainan", "海口", "hai3kou3", "Haikou"),
    ("台湾", "tai2wan1", "Taiwan", "台北", "tai2bei3", "Taipei"),
]
REGIONS = [
    ("内蒙古", "nei4meng2gu3", "Inner Mongolia", "呼和浩特", "hu1he2hao4te4", "Hohhot"),
    ("广西", "guang3xi1", "Guangxi", "南宁", "nan2ning2", "Nanning"),
    ("西藏", "xi1zang4", "Tibet", "拉萨", "la1sa4", "Lhasa"),
    ("宁夏", "ning2xia4", "Ningxia", "银川", "yin2chuan1", "Yinchuan"),
    ("新疆", "xin1jiang1", "Xinjiang", "乌鲁木齐", "wu1lu3mu4qi2", "Urumqi"),
]


def pair_exercises(rows, province_word="省", capital_word="省会", fill_every=2):
    """Exercises for rows of (province, capital): names, which capital, which province, a blank."""
    out = []
    n = len(rows)
    step = [3, 5, 7] if n >= 8 else [1, 2, 3]
    for i, (ph, pp, pe, ch, cp, ce) in enumerate(rows):
        others = [rows[(i + k) % n] for k in step]
        out.append(mean(ph, pp, pe, [o[2] for o in others]))
        out.append(mean(ch, cp, ce, [o[5] for o in others]))
        out.append(M(f"Which city is the capital of {pe} ({ph})?", ch, [o[3] for o in others], f"{ce} is the capital of {pe}."))
        out.append(M(f"{ch} is the capital of which place?", ph, [o[0] for o in others], f"{ce} is in {pe}."))
        if i % fill_every == 0 and len(ch) >= 2:
            out.append(F(f"{ph}的{capital_word}是{ch[:-1]}___。", ch[-1], PART, f"{ch} is the capital of {pe}.", tr=f"The capital of {pe} is {ce}."))
    return out


def table_rows(rows):
    return [(r[0], r[1], r[2]) for r in rows] + [(r[3], r[4], r[5]) for r in rows]


# ---------------------------------------------------------------------------- 118
L118 = lesson(
    "How China is divided",
    "省 · 自治区 · 直辖市 · 特别行政区 · 省会",
    requires=[],
    cards=[
        card("Four kinds of division",
             "China’s first-level divisions come in four kinds. A 省 (shěng) is a province, and its capital is a 省会 (shěnghuì). "
             "A 自治区 (zìzhìqū) is an autonomous region, “self-governing area”, and its capital is a 首府 (shǒufǔ). "
             "A 直辖市 (zhíxiáshì) is a municipality under the central government, and a 特别行政区 (tèbié xíngzhèngqū) is a special administrative region. "
             "A city is a 市 (shì). The 省 or 市 is often dropped in speech: 四川 for 四川省, 成都 for 成都市.",
             tables=[wtable([("省", "sheng3", "province"), ("省会", "sheng3hui4", "provincial capital"), ("自治区", "zi4zhi4qu1", "autonomous region"), ("首府", "shou3fu3", "capital of an autonomous region"),
                             ("直辖市", "zhi2xia2shi4", "municipality"), ("特别行政区", "te4bie2 xing2zheng4qu1", "special administrative region"), ("市", "shi4", "city"), ("中国", "zhong1guo2", "China")])]),
        card("Municipalities and special regions",
             "Four big cities are directly under the central government: 北京 (Běijīng), 天津 (Tiānjīn), 上海 (Shànghǎi) and 重庆 (Chóngqìng). "
             "There are two special administrative regions: 香港 (Xiānggǎng, Hong Kong) and 澳门 (Àomén, Macau). Their full names end in 特别行政区.",
             tables=[wtable([("北京", "bei3jing1", "Beijing"), ("天津", "tian1jin1", "Tianjin"), ("上海", "shang4hai3", "Shanghai"), ("重庆", "chong2qing4", "Chongqing"),
                             ("香港", "xiang1gang3", "Hong Kong"), ("澳门", "ao4men2", "Macau")])],
             examples=[ex("四川是中国的一个省。", "si4chuan1 shi4 zhong1guo2 de5 yi2 ge4 sheng3", "Sichuan is a province of China.", hl="省"),
                       ex("成都是四川的省会。", "cheng2du1 shi4 si4chuan1 de5 sheng3hui4", "Chengdu is the capital of Sichuan.", hl="省会"),
                       ex("上海是直辖市。", "shang4hai3 shi4 zhi2xia2shi4", "Shanghai is a municipality directly under the central government.")]),
        card("Full names and notes (from the book)",
             "The book writes each place with its type: 辽宁省 (Liáoníng Shěng), the capital 沈阳市 (Shěnyáng Shì), the municipality 北京市 (Běijīng Shì), the autonomous region 西藏自治区 (Xīzàng Zìzhìqū). "
             "The two special administrative regions have long full names: 香港特别行政区 (Xiānggǎng Tèbiéxíngzhèngqū) and 澳门特别行政区 (Àomén Tèbiéxíngzhèngqū). "
             "Notes: 1. In colloquial conversation the word 省 or 市 is often omitted. 2. 香港特别行政区 and 澳门特别行政区 are often shortened to 香港行政特区 or 香港特区, and 澳门行政特区 or 澳门特区.",
             tables=[wtable([("香港特别行政区", "xiang1gang3 te4bie2xing2zheng4qu1", "Hong Kong Special Administrative Region"), ("澳门特别行政区", "ao4men2 te4bie2xing2zheng4qu1", "Macau Special Administrative Region"),
                             ("香港特区", "xiang1gang3 te4qu1", "Hong Kong SAR (short)"), ("澳门特区", "ao4men2 te4qu1", "Macau SAR (short)"),
                             ("香港行政特区", "xiang1gang3 xing2zheng4te4qu1", "Hong Kong SAR (short)"), ("澳门行政特区", "ao4men2 xing2zheng4te4qu1", "Macau SAR (short)"),
                             ("北京市", "bei3jing1 shi4", "Beijing Municipality"), ("天津市", "tian1jin1 shi4", "Tianjin Municipality"), ("上海市", "shang4hai3 shi4", "Shanghai Municipality"), ("重庆市", "chong2qing4 shi4", "Chongqing Municipality")])]),
    ],
    exercises=[
        mean("省", "sheng3", "province", ["city", "region", "capital"]),
        mean("省会", "sheng3hui4", "provincial capital", ["province", "a big city", "a meeting"]),
        mean("自治区", "zi4zhi4qu1", "autonomous region", ["province", "municipality", "a district"]),
        mean("首府", "shou3fu3", "capital of an autonomous region", ["provincial capital", "a government", "a big city"]),
        mean("直辖市", "zhi2xia2shi4", "municipality", ["province", "autonomous region", "county"]),
        mean("特别行政区", "te4bie2 xing2zheng4qu1", "special administrative region", ["autonomous region", "province", "municipality"]),
        mean("市", "shi4", "city", ["province", "region", "village"]),
        mean("香港", "xiang1gang3", "Hong Kong", ["Macau", "Shanghai", "Tianjin"]),
        mean("澳门", "ao4men2", "Macau", ["Hong Kong", "Beijing", "Chongqing"]),
        mean("重庆", "chong2qing4", "Chongqing", ["Tianjin", "Beijing", "Shanghai"]),
        mean("天津", "tian1jin1", "Tianjin", ["Beijing", "Shanghai", "Chongqing"]),
        rd("澳门", "ao4men2", ["ao4men3", "ao2men2", "ao4men4"]),
        rd("天津", "tian1jin1", ["tian1jin4", "tian2jin1", "tian1jin3"]),
        M("How many kinds of first-level division were listed?", "Four", ["Two", "Three", "Six"], "Province, autonomous region, municipality, special administrative region."),
        M("Which are the four municipalities?", "北京、天津、上海、重庆", ["北京、上海、香港、澳门", "天津、成都、上海、重庆", "北京、广州、上海、重庆"], "Beijing, Tianjin, Shanghai, Chongqing."),
        M("Which are the two special administrative regions?", "香港和澳门", ["北京和上海", "天津和重庆", "香港和重庆"], "Hong Kong and Macau."),
        M("What is the capital of a province called?", "省会", ["首府", "直辖市", "自治区"], "省会."),
        M("What is the capital of an autonomous region called?", "首府", ["省会", "直辖市", "特别行政区"], "首府."),
        M("What does 成都是四川的省会 say?", "Chengdu is the capital of Sichuan.", ["Chengdu is a province.", "Sichuan is the capital of Chengdu.", "Chengdu is a special region."], "省会 is provincial capital."),
        F("四川是中国的一个___。", "省", PART, "四川 is a province.", tr="Sichuan is a province of China."),
        F("成都是四川的___会。", "省", PART, "省会 is provincial capital.", tr="Chengdu is the capital of Sichuan."),
        F("上海是直辖___。", "市", PART, "直辖市 is municipality.", tr="Shanghai is a municipality."),
    ],
)

# ---------------------------------------------------------------------------- 119
L119 = lesson(
    "Provinces and capitals: north and east",
    "辽宁 · 吉林 · 黑龙江 · 河北 · 山西 · 山东 · 河南 · 江苏 · 浙江 · 江西 · 安徽 · 福建",
    requires=[],
    cards=[
        card("Twelve provinces and their capitals",
             "Say a province and its 省会 together: 辽宁省 (Liáoníng Shěng), capital 沈阳市. In speech people drop 省 and 市. "
             "Learn them in the order they are listed here, from the northeast down the coast to the south.",
             tables=[wtable(table_rows(NORTH_EAST))]),
        card("山西 and 陕西, the tone pair",
             "Two provinces sound almost the same: 山西 is Shānxī (first tone, west of the mountains) and 陕西 is Shǎnxī (third tone, whose capital is 西安). "
             "The only difference is the tone of the first syllable.",
             examples=[ex("辽宁省的省会是沈阳。", "liao2ning2 sheng3 de5 sheng3hui4 shi4 shen3yang2", "The capital of Liaoning is Shenyang.", hl="沈阳"),
                       ex("山东的省会是济南。", "shan1dong1 de5 sheng3hui4 shi4 ji3nan2", "The capital of Shandong is Jinan."),
                       ex("江苏的省会是南京，浙江的省会是杭州。", "jiang1su1 de5 sheng3hui4 shi4 nan2jing1, zhe4jiang1 de5 sheng3hui4 shi4 hang2zhou1", "The capital of Jiangsu is Nanjing and the capital of Zhejiang is Hangzhou.")]),
    ],
    exercises=pair_exercises(NORTH_EAST) + [
        M("Which province is Shānxī, with the first tone?", "山西", ["陕西", "山东", "河北"], "山 is first tone."),
        M("Which province is Shǎnxī, with the third tone?", "陕西", ["山西", "河南", "江西"], "陕 is third tone."),
    ],
)

# ---------------------------------------------------------------------------- 120
L120 = lesson(
    "Provinces and capitals: south, west and the regions",
    "湖北 · 湖南 · 四川 · 贵州 · 云南 · 陕西 · 甘肃 · 青海 · 广东 · 海南",
    requires=[],
    cards=[
        card("Eleven more provinces",
             "These provinces run through the middle, the southwest and the northwest, and finish with the southern coast. Their capitals work the same way: name + 的省会 + capital.",
             tables=[wtable(table_rows(SOUTH_WEST))]),
        card("Five autonomous regions",
             "The five autonomous regions have a 首府 instead of a 省会: 内蒙古 (Nèiměnggǔ), 广西 (Guǎngxī), 西藏 (Xīzàng), 宁夏 (Níngxià) and 新疆 (Xīnjiāng). "
             "The full name ends in 自治区, and the longer names carry the people’s name too, but the short form is what you use.",
             tables=[wtable(table_rows(REGIONS))],
             examples=[ex("四川的省会是成都。", "si4chuan1 de5 sheng3hui4 shi4 cheng2du1", "The capital of Sichuan is Chengdu.", hl="成都"),
                       ex("西藏的首府是拉萨。", "xi1zang4 de5 shou3fu3 shi4 la1sa4", "The capital of Tibet is Lhasa.", hl="首府"),
                       ex("新疆在中国的西北部。", "xin1jiang1 zai4 zhong1guo2 de5 xi1bei3bu4", "Xinjiang is in the northwest of China.")]),
        card("The full names of the autonomous regions",
             "In the book the autonomous regions are written with their full names; the longer ones include the name of the main minority people.",
             tables=[wtable([("内蒙古自治区", "nei4meng2gu3 zi4zhi4qu1", "Inner Mongolia Autonomous Region"), ("广西壮族自治区", "guang3xi1 zhuang4zu2 zi4zhi4qu1", "Guangxi Zhuang Autonomous Region"),
                             ("西藏自治区", "xi1zang4 zi4zhi4qu1", "Tibet Autonomous Region"), ("宁夏回族自治区", "ning2xia4 hui2zu2 zi4zhi4qu1", "Ningxia Hui Autonomous Region"),
                             ("新疆维吾尔族自治区", "xin1jiang1 wei2wu2er3zu2 zi4zhi4qu1", "Xinjiang Uygur Autonomous Region")])]),
    ],
    exercises=pair_exercises(SOUTH_WEST) + pair_exercises(REGIONS, province_word="自治区", capital_word="首府", fill_every=2),
)

# ---------------------------------------------------------------------------- 121
L121 = lesson(
    "American states in Chinese",
    "美国 · 州 · 加利福尼亚 · 纽约 · 德克萨斯 · 华盛顿",
    requires=[],
    cards=[
        card("Foreign names by sound",
             "美国 (Měiguó) is the USA, “the beautiful country”, and a state is a 州 (zhōu). Most American state and city names are written in Chinese by their sound, "
             "so the characters are chosen for sound, not meaning. They can be long, and many have a short form: 加利福尼亚 is shortened to 加州 and 德克萨斯 to 德州.",
             tables=[wtable([("美国", "mei3guo2", "the USA"), ("州", "zhou1", "state"), ("加利福尼亚", "jia1li4fu2ni2ya4", "California"), ("加州", "jia1zhou1", "California (short)"),
                             ("纽约", "niu3yue1", "New York"), ("德克萨斯", "de2ke4sa4si1", "Texas"), ("德州", "de2zhou1", "Texas (short)"), ("佛罗里达", "fo2luo2li3da2", "Florida"),
                             ("华盛顿", "hua2sheng4dun4", "Washington"), ("夏威夷", "xia4wei1yi2", "Hawaii"), ("阿拉斯加", "a1la1si1jia1", "Alaska")])]),
        card("Cities and a question",
             "City names follow the same method: 蒙特雷 is Monterey, 旧金山 is San Francisco (it means “old gold mountain”) and 洛杉矶 is Los Angeles. "
             "华盛顿 is the name of a state and of the capital of the USA; the context tells you which one.",
             tables=[wtable([("蒙特雷", "meng2te4lei2", "Monterey"), ("旧金山", "jiu4jin1shan1", "San Francisco"), ("洛杉矶", "luo4shan1ji1", "Los Angeles"), ("芝加哥", "zhi1jia1ge1", "Chicago")])],
             examples=[ex("华盛顿是美国的首都。", "hua2sheng4dun4 shi4 mei3guo2 de5 shou3du1", "Washington is the capital of the USA.", hl="首都"),
                       ex("蒙特雷在加利福尼亚州。", "meng2te4lei2 zai4 jia1li4fu2ni2ya4 zhou1", "Monterey is in the state of California.", hl="州"),
                       ex("你的老家在哪个州？ 我的老家在德克萨斯州。", "ni3 de5 lao3jia1 zai4 na3 ge4 zhou1? wo3 de5 lao3jia1 zai4 de2ke4sa4si1 zhou1", "Which state is your hometown in? My hometown is in Texas.")]),
    ],
    exercises=[
        mean("美国", "mei3guo2", "the USA", ["China", "England", "Germany"]),
        mean("州", "zhou1", "state", ["province", "city", "country"]),
        mean("加利福尼亚", "jia1li4fu2ni2ya4", "California", ["Texas", "Florida", "Washington"]),
        mean("加州", "jia1zhou1", "California (short)", ["Texas (short)", "Florida", "Alaska"]),
        mean("纽约", "niu3yue1", "New York", ["Washington", "Texas", "Hawaii"]),
        mean("德克萨斯", "de2ke4sa4si1", "Texas", ["California", "Florida", "Alaska"]),
        mean("德州", "de2zhou1", "Texas (short)", ["California (short)", "New York", "Florida"]),
        mean("佛罗里达", "fo2luo2li3da2", "Florida", ["Texas", "Hawaii", "California"]),
        mean("华盛顿", "hua2sheng4dun4", "Washington", ["New York", "Texas", "Florida"]),
        mean("夏威夷", "xia4wei1yi2", "Hawaii", ["Alaska", "Florida", "Texas"]),
        mean("阿拉斯加", "a1la1si1jia1", "Alaska", ["Hawaii", "Texas", "California"]),
        mean("蒙特雷", "meng2te4lei2", "Monterey", ["Los Angeles", "San Francisco", "Chicago"]),
        mean("旧金山", "jiu4jin1shan1", "San Francisco", ["Los Angeles", "Monterey", "Chicago"]),
        mean("洛杉矶", "luo4shan1ji1", "Los Angeles", ["San Francisco", "Monterey", "Chicago"]),
        mean("芝加哥", "zhi1jia1ge1", "Chicago", ["Los Angeles", "San Francisco", "Monterey"]),
        rd("纽约", "niu3yue1", ["niu3yue4", "niu2yue1", "niu3yue2"]),
        rd("夏威夷", "xia4wei1yi2", ["xia4wei1yi4", "xia2wei1yi2", "xia4wei2yi2"]),
        M("Are the characters in 加利福尼亚 chosen for their meaning?", "No, for their sound", ["Yes, for their meaning", "Only the first one", "Only the last one"], "Foreign names are written by sound."),
        M("What is the short form of 德克萨斯州?", "德州", ["德克", "德斯", "萨州"], "德 + 州."),
        M("What is the short form of 加利福尼亚州?", "加州", ["利州", "福州", "亚州"], "加 + 州."),
        M("What does 华盛顿 refer to?", "A state and the capital of the USA", ["Only a state", "Only a city in China", "Only a province"], "Context tells which."),
        M("How do you say “Which state is your hometown in?”", "你的老家在哪个州？", ["你的老家哪个州在？", "你的老家在哪个州吗？", "哪个州你的老家？"], "在 + 哪个州."),
        M("What does 蒙特雷在加利福尼亚州 say?", "Monterey is in the state of California.", ["Monterey is the capital of California.", "California is in Monterey.", "Monterey is in Texas."], "在 + place."),
        F("纽约是美国的一个___。", "州", PART, "州 is state.", tr="New York is a state of the USA."),
        F("华盛顿是美国的首___。", "都", PART, "首都 is capital.", tr="Washington is the capital of the USA."),
        F("你的老家在哪个___？", "州", PART, "州 is state.", tr="Which state is your hometown in?"),
    ],
)

# ---------------------------------------------------------------------------- 122
L122 = lesson(
    "A proverb: 边学边问，才有学问",
    "边 … 边 … · 才 · 学问",
    requires=[],
    cards=[
        card("Doing two things at once",
             "边 … 边 … (biān … biān …) joins two actions that happen together: 边走边说 is “talk while walking”. Put 边 before each verb. "
             "The two verbs are both actions and the subject is the same person. 边学边问 is “learn while asking”.",
             tables=[wtable([("边走边说", "bian1 zou3 bian1 shuo1", "talk while walking"), ("边吃边看", "bian1 chi1 bian1 kan4", "eat while watching"), ("边学边问", "bian1 xue2 bian1 wen4", "learn while asking"),
                             ("学问", "xue2wen4", "learning, knowledge"), ("才", "cai2", "only then")])]),
        card("The whole proverb",
             "边学边问，才有学问。 means “Learn while you ask, and only then will you have knowledge”. 才 (cái) here says that a result comes only on one condition. "
             "学问 (xuéwen) is learning or scholarship, and uses 问 (wèn, ask) as part of the word, because asking is the way to learn.",
             examples=[ex("边学边问，才有学问。", "bian1 xue2 bian1 wen4, cai2 you3 xue2wen4", "Learn while asking, and only then will you have learning.", hl="才"),
                       ex("他喜欢边走边说。", "ta1 xi3huan5 bian1 zou3 bian1 shuo1", "He likes to talk while walking.", hl="边"),
                       ex("我们边学中文边问老师。", "wo3men5 bian1 xue2 zhong1wen2 bian1 wen4 lao3shi1", "We ask the teacher while learning Chinese.")]),
    ],
    exercises=[
        mean("边学边问", "bian1 xue2 bian1 wen4", "learn while asking", ["ask before learning", "learn and then ask", "learn from the side"]),
        mean("学问", "xue2wen4", "learning, knowledge", ["a question", "a school", "an answer"]),
        mean("才", "cai2", "only then", ["also", "already", "very"]),
        mean("边走边说", "bian1 zou3 bian1 shuo1", "talk while walking", ["walk then talk", "walk to the side", "walk and be quiet"]),
        rd("才", "cai2", ["cai1", "cai3", "cai4"]),
        rd("学问", "xue2wen4", ["xue2wen2", "xue3wen4", "xue2wen3"]),
        M("What does 边 … 边 … do?", "Joins two actions done at the same time", ["Joins two nouns", "Says one action follows another", "Asks a question"], "Two actions together."),
        M("Where does 边 go?", "Before each verb", ["After each verb", "Before the subject", "At the end"], "边 + verb 边 + verb."),
        M("How do you say “talk while walking”?", "边走边说", ["走边说边", "边走说边", "走边边说"], "边 + verb + 边 + verb."),
        M("What does 边学边问，才有学问 teach?", "You learn by asking as you study", ["You must be quiet", "Learning is easy", "Ask before you study"], "Asking while learning brings knowledge."),
        M("What does 才 mean in the proverb?", "only then", ["also", "already", "very"], "A condition for a result."),
        M("What is 学问?", "learning, knowledge", ["a school", "a question", "a teacher"], "学 + 问."),
        M("How do you say “We ask the teacher while learning Chinese”?", "我们边学中文边问老师。", ["我们边学边中文问老师。", "我们学中文边问边老师。", "边我们学中文问老师边。"], "边 + verb + (object) + 边 + verb."),
        F("边学边问，___有学问。", "才", PART, "才 is only then.", tr="Learn while asking, and only then will you have learning."),
        F("他喜欢___走边说。", "边", PART, "边 … 边 ….", tr="He likes to talk while walking."),
        F("边学边问，才有学___。", "问", PART, "学问 is learning.", tr="Learn while asking, and you will have learning."),
        F("我们边学中文边___老师。", "问", PART, "边学边问.", tr="We ask the teacher while learning Chinese."),
    ],
)

# ---------------------------------------------------------------------------- 123
L123 = lesson(
    "Review: provinces, states and the proverb",
    "省 · 省会 · 首府 · 州 · 边 … 边 …",
    requires=[],
    cards=[
        card("What you can now do",
             "You can name the kinds of Chinese divisions, say a province and its capital, read American state names and use 边 … 边 …. These questions mix them.",
             examples=[ex("成都是四川的省会，拉萨是西藏的首府。", "cheng2du1 shi4 si4chuan1 de5 sheng3hui4, la1sa4 shi4 xi1zang4 de5 shou3fu3", "Chengdu is the capital of Sichuan and Lhasa is the capital of Tibet."),
                       ex("蒙特雷在加州，华盛顿是美国的首都。", "meng2te4lei2 zai4 jia1zhou1, hua2sheng4dun4 shi4 mei3guo2 de5 shou3du1", "Monterey is in California and Washington is the capital of the USA.")]),
    ],
    exercises=[
        M("What is the capital of Guangdong (广东)?", "广州", ["海口", "南宁", "长沙"], "Guangzhou."),
        M("What is the capital of Hubei (湖北)?", "武汉", ["长沙", "郑州", "南昌"], "Wuhan."),
        M("What is the capital of Shandong (山东)?", "济南", ["南京", "太原", "济宁"], "Jinan."),
        M("What is the capital of Yunnan (云南)?", "昆明", ["贵阳", "成都", "南宁"], "Kunming."),
        M("What is the capital of Jilin (吉林)?", "长春", ["沈阳", "哈尔滨", "长沙"], "Changchun."),
        M("What is the capital of Gansu (甘肃)?", "兰州", ["西宁", "银川", "西安"], "Lanzhou."),
        M("What is the capital of Tibet (西藏)?", "拉萨", ["银川", "昆明", "西宁"], "Lhasa."),
        M("Xinjiang’s capital is…", "乌鲁木齐", ["呼和浩特", "银川", "拉萨"], "Urumqi."),
        M("Which is not a municipality?", "成都", ["北京", "天津", "重庆"], "Chengdu is a provincial capital."),
        M("Which is a special administrative region?", "澳门", ["天津", "杭州", "广州"], "Macau."),
        M("What do you call the capital of an autonomous region?", "首府", ["省会", "首都", "市区"], "首府."),
        M("Which province has the third tone Shǎnxī?", "陕西", ["山西", "山东", "河北"], "陕西."),
        mean("州", "zhou1", "state", ["province", "city", "country"]),
        mean("加州", "jia1zhou1", "California (short)", ["Texas (short)", "Florida", "Alaska"]),
        mean("蒙特雷", "meng2te4lei2", "Monterey", ["Los Angeles", "San Francisco", "Chicago"]),
        mean("学问", "xue2wen4", "learning, knowledge", ["a question", "a school", "an answer"]),
        M("What does 边 … 边 … do?", "Joins two actions at the same time", ["Joins two nouns", "Asks a question", "Says one after another"], "边 + verb 边 + verb."),
        F("成都是四川的___会。", "省", PART, "省会.", tr="Chengdu is the capital of Sichuan."),
        F("拉萨是西藏的首___。", "府", PART, "首府.", tr="Lhasa is the capital of Tibet."),
        F("他喜欢边走___说。", "边", PART, "边 … 边 ….", tr="He likes to talk while walking."),
    ],
)

UNIT = unit("第五课 Provinces and states", [L118, L119, L120, L121, L122, L123])
