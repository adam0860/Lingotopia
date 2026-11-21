"""Unit 16: Lesson 5 book texts, the rest of Presentation 3: the 51 American state names, the Presentation 3
vocabulary list and the Area Studies reading (China's territorial and administrative divisions)."""
from zh_auto import *

PART = ["吗", "们", "呢"]

# (English, Chinese) in the book's order, 51 entries; alternative names are listed separately
STATES = [
    ("Alabama", "阿拉巴马州"), ("Alaska", "阿拉斯加州"), ("Arizona", "亚利桑那州"), ("Arkansas", "阿肯色州"), ("California", "加利福尼亚州"),
    ("Colorado", "科罗拉多州"), ("Connecticut", "康涅狄格州"), ("Delaware", "特拉华州"), ("Florida", "佛罗里达州"), ("Georgia", "佐治亚州"),
    ("Hawaii", "夏威夷州"), ("Idaho", "爱达荷州"), ("Illinois", "伊利诺斯州"), ("Indiana", "印第安纳州"), ("Iowa", "衣阿华州"),
    ("Kansas", "堪萨斯州"), ("Kentucky", "肯塔基州"), ("Louisiana", "路易斯安那州"), ("Maine", "缅因州"), ("Maryland", "马里兰州"),
    ("Massachusetts", "马萨诸塞州"), ("Michigan", "密执安州"), ("Minnesota", "明尼苏达州"), ("Mississippi", "密西西比州"), ("Missouri", "密苏里州"),
    ("Montana", "蒙大拿州"), ("Nebraska", "内布拉斯加州"), ("Nevada", "内华达州"), ("New Hampshire", "新罕布什尔州"), ("New Jersey", "新泽西州"),
    ("New Mexico", "新墨西哥州"), ("New York", "纽约州"), ("North Carolina", "北卡罗来纳州"), ("North Dakota", "北达科他州"), ("Ohio", "俄亥俄州"),
    ("Oklahoma", "俄克拉何马州"), ("Oregon", "俄勒岗州"), ("Pennsylvania", "宾夕法尼亚州"), ("Rhode Island", "罗德艾兰州"), ("South Carolina", "南卡罗来纳州"),
    ("South Dakota", "南达科他州"), ("Tennessee", "田纳西州"), ("Texas", "德克萨斯州"), ("Utah", "犹他州"), ("Vermont", "佛蒙特州"),
    ("Virginia", "弗吉尼亚州"), ("Washington", "华盛顿州"), ("West Virginia", "西弗吉尼亚州"), ("Wisconsin", "威斯康星州"), ("Wyoming", "怀俄明州"),
    ("Washington, D.C.", "华盛顿特区"),
]
ALT = [("麻省", "ma2sheng3", "Massachusetts (short form of 马萨诸塞州)"), ("密歇根", "mi4xie1gen1", "Michigan (another spelling of 密执安)"),
       ("密西根", "mi4xi1gen1", "Michigan (another spelling of 密执安)"), ("北卡州", "bei3ka3zhou1", "North Carolina (short form)"),
       ("罗德岛州", "luo2de2dao3zhou1", "Rhode Island (another name)"), ("南卡州", "nan2ka3zhou1", "South Carolina (short form)"), ("德州", "de2zhou1", "Texas (short form)")]


def state_lesson(title, subtitle, chunk, note, extra_alt=None):
    rows = [(hz, auto_py(hz), en) for en, hz in chunk]
    n = len(rows)
    cards = [card("The state names (Pronunciation Review)",
                  note, tables=[wtable(rows)])]
    if extra_alt:
        cards.append(card("Other forms in the book", "The book lists these shorter or alternative names beside the full ones.", tables=[wtable(extra_alt)]))
    exs = []
    for i, (hz, py, en) in enumerate(rows):
        others = [rows[(i + k) % n] for k in (3, 7, 11)]
        exs.append(mean(hz, py, en, [o[2] for o in others]))
        exs.append(M(f"Which is {en} in Chinese?", hz, [o[0] for o in others], f"{hz} is {en}."))
    return lesson(title, subtitle, requires=[], cards=cards, exercises=exs)


L_ST1 = state_lesson("American states A to I (Alabama to Indiana)", "阿拉巴马州 … 印第安纳州", STATES[0:14],
                     "The book lists all 50 states and Washington, D.C. in Chinese, in English alphabetical order, with the pinyin. Foreign names are written with characters chosen for their sound, and every name ends in 州 (zhōu, state).")
L_ST2 = state_lesson("American states I to N (Iowa to New York)", "衣阿华州 … 纽约州", STATES[14:32],
                     "The second part of the book’s list. Michigan, Massachusetts and the Carolinas also have shorter or alternative names.",
                     extra_alt=ALT[0:3])
L_ST3 = state_lesson("American states N to W (North Carolina to Wyoming, and Washington, D.C.)", "北卡罗来纳州 … 华盛顿特区", STATES[32:51],
                     "The last part of the list. 华盛顿州 is the state and 华盛顿特区 (Huáshèngdùn Tèqū) is the District of Columbia, the capital; 特区 is “special district”.",
                     extra_alt=ALT[3:7])

# ---------------------------------------------------------------------------- Presentation 3 vocabulary
L_P3_VOCAB = lesson(
    "Presentation 3 vocabulary",
    "山城 · 大部分 · 阴天 · 晴天 · 经常 · 下雾 · 最高 · 气温 · 气候 · 凉快 · 平均 · 最低 · 左右 · 有意思",
    requires=[],
    cards=[
        card("Vocabulary list (Presentation 3)",
             "The book’s 29 words, with the traditional form where it differs: 阴天 陰天, 经常 經常, 下雾 下霧, 刮风 刮風, 跟…一样 跟…一樣, 气候 氣侯, 这么 這麼, 气温 氣温.",
             tables=[wtable([("山城", "shan1cheng2", "n. mountain city"), ("一年", "yi4nian2", "n. throughout the year"), ("四季", "si4ji4", "n. four seasons"), ("大部分", "da4bu4fen5", "n. most, mostly"),
                             ("阴天", "yin1tian1", "n. cloudy (trad. 陰天)"), ("很少", "hen3shao3", "adv. rarely"), ("晴天", "qing2tian1", "n. sunny"), ("经常", "jing1chang2", "adv. often (trad. 經常)"),
                             ("下雾", "xia4wu4", "v.o. foggy (trad. 下霧)"), ("最高", "zui4gao1", "adj. the highest"), ("气温", "qi4wen1", "n. temperature (trad. 氣温)"), ("下雨", "xia4yu3", "v.o. rain"),
                             ("刮风", "gua1feng1", "v.o. windy (trad. 刮風)"), ("跟…一样", "gen1 yi2yang4", "prep. the same as (trad. 跟…一樣)"), ("可是", "ke3shi4", "conj. but"), ("下雪", "xia4xue3", "v.o. snow"),
                             ("气候", "qi4hou4", "n. climate (trad. 氣侯)"), ("这么", "zhe4me5", "adv. so (trad. 這麼)"), ("凉快", "liang2kuai5", "adj. cool"), ("平均", "ping2jun1", "adv. at average"),
                             ("最低", "zui4di1", "adj. the lowest"), ("左右", "zuo3you4", "n. about"), ("好玩", "hao3wan2", "adj. fun"), ("地方", "di4fang5", "n. place"), ("好吃", "hao3chi1", "adj. delicious"),
                             ("东西", "dong1xi5", "n. things"), ("有意思", "you3yi4si5", "adj. interesting, funny"), ("意思", "yi4si5", "n. meaning"), ("蒙特雷", "meng2te4lei2", "n. Monterey")])]),
    ],
    exercises=[
        mean("山城", "shan1cheng2", "mountain city", ["a mountain", "a small city", "a state"]),
        mean("大部分", "da4bu4fen5", "most, mostly", ["a little", "all", "never"]),
        mean("阴天", "yin1tian1", "cloudy", ["sunny", "rainy", "foggy"]),
        mean("晴天", "qing2tian1", "sunny", ["cloudy", "rainy", "snowy"]),
        mean("经常", "jing1chang2", "often", ["rarely", "sometimes", "never"]),
        mean("下雾", "xia4wu4", "foggy", ["rainy", "snowy", "windy"]),
        mean("最高", "zui4gao1", "the highest", ["the lowest", "higher", "tall"]),
        mean("气温", "qi4wen1", "temperature", ["climate", "weather", "season"]),
        mean("气候", "qi4hou4", "climate", ["temperature", "weather today", "season"]),
        mean("凉快", "liang2kuai5", "cool", ["warm", "hot", "cold"]),
        mean("平均", "ping2jun1", "on average", ["the highest", "the lowest", "about"]),
        mean("最低", "zui4di1", "the lowest", ["the highest", "lower", "short"]),
        mean("左右", "zuo3you4", "about", ["left", "right", "exactly"]),
        mean("地方", "di4fang5", "place", ["ground", "a side", "a region"]),
        mean("东西", "dong1xi5", "things", ["east and west", "a market", "east"]),
        mean("有意思", "you3yi4si5", "interesting, funny", ["boring", "meaningless", "serious"]),
        mean("意思", "yi4si5", "meaning", ["interesting", "a thought", "a word"]),
        mean("一年", "yi4nian2", "throughout the year", ["one day", "this year", "last year"]),
        mean("四季", "si4ji4", "four seasons", ["four years", "four cities", "four months"]),
        M("What does the traditional form 氣侯 (in the book) correspond to?", "气候", ["气温", "天气", "季节"], "氣侯 is the book’s spelling of 氣候, 气候."),
    ],
)

# ---------------------------------------------------------------------------- Area Studies
L_AREA = lesson(
    "Area studies: China’s territorial and administrative divisions",
    "中华人民共和国 · 23 provinces, 5 autonomous regions, 4 municipalities, 2 special administrative regions",
    requires=[],
    cards=[
        card("The People’s Republic of China (中华人民共和国)",
             "The People’s Republic of China (PRC) is situated in East Asia on the western rim of the Pacific Ocean. It has a total area of 9.6 million square kilometers. Its north-to-south length is 5,500 kilometers and it stretches 5,200 kilometers from east to west. "
             "Its entire national border is 22,800 kilometers long. China is bordered by North Korea to the east; Mongolia to the north; Russia to the northeast; and Kazakhstan to the northwest. "
             "It is bordered by Kyrgyzstan, Tajikistan, Afghanistan, and Pakistan to the west; India, Nepal, and Bhutan to the southwest; and Burma (Myanmar), Laos, and Vietnam to the south. "
             "Across the seas to the east and southeast are South Korea, Japan, the Philippines, Brunei, Malaysia, and Indonesia. "
             "The Chinese mainland is flanked by the Bohai Sea (渤海), the Yellow Sea (黄海), the East China Sea (东海) and the South China Sea (南海). China’s coastline is 32,000 kilometers long, with 18,000 kilometers of mainland and 14,000 kilometers of island coastline.",
             tables=[wtable([("渤海", "bo2hai3", "the Bohai Sea"), ("黄海", "huang2hai3", "the Yellow Sea"), ("东海", "dong1hai3", "the East China Sea"), ("南海", "nan2hai3", "the South China Sea")])]),
        card("The South China Sea",
             "China claims sovereignty over the South China Sea (南海) and its numerous islands, atolls, and reefs. However, Southeast Asian nations like Vietnam and the Philippines also have territorial claims in this resource-rich region with strategic sea lanes. "
             "Because it is one of the world’s busiest shipping routes, the U.S. and other Pacific nations insist the South China Sea remains open international waters."),
        card("Administrative divisions",
             "Due to China’s sizeable population and territory, it has governed the nation with tightly organized and integrated administrative divisions since ancient times. China’s administration is currently based on a three-level system dividing the nation into administrative units of three different sizes: provinces, counties and townships. "
             "The entire nation is divided into: 23 provinces (the PRC also considers Taiwan 台湾 a province, as it does not recognize the island as a sovereign nation); "
             "5 autonomous regions: Tibet 西藏, Xinjiang 新疆, Inner Mongolia 内蒙古, Ningxia 宁夏 and Guangxi 广西, where the predominant ethnic minority has a degree of legislative power; "
             "4 municipalities: Beijing 北京, Tianjin 天津, Shanghai 上海 and Chongqing 重庆; and 2 special administrative regions: Hong Kong 香港 and Macao 澳门.",
             tables=[wtable([("省", "sheng3", "province"), ("自治区", "zi4zhi4qu1", "autonomous region"), ("直辖市", "zhi2xia2shi4", "municipality"), ("特别行政区", "te4bie2 xing2zheng4qu1", "special administrative region"),
                             ("台湾", "tai2wan1", "Taiwan"), ("西藏", "xi1zang4", "Tibet"), ("新疆", "xin1jiang1", "Xinjiang"), ("内蒙古", "nei4meng2gu3", "Inner Mongolia"), ("宁夏", "ning2xia4", "Ningxia"),
                             ("广西", "guang3xi1", "Guangxi"), ("香港", "xiang1gang3", "Hong Kong"), ("澳门", "ao4men2", "Macao")])]),
        card("Prefectures, counties and townships",
             "Currently there are approximately 335 prefectures in China, although the number changes frequently. Of the nation’s almost 3,000 county-level administrative units, about half are counties, while the rest are mostly municipal districts (市辖区). "
             "In rural areas, townships are called villages (乡), while in urban areas they are referred to as towns (镇). "
             "The book ends with a chart of the structural hierarchy of the administrative divisions and the basic-level autonomies of the People’s Republic of China: provincial level (1st), prefectural level (2nd), county level (3rd), township level (4th) and basic-level autonomy (5th). "
             "The chart itself is a large diagram and is not reproduced here.",
             tables=[wtable([("市辖区", "shi4xia2qu1", "municipal district"), ("乡", "xiang1", "township, village (rural)"), ("镇", "zhen4", "town (urban)"), ("县", "xian4", "county")])]),
    ],
    exercises=[
        M("According to the reading, what is China’s total area?", "9.6 million square kilometers", ["5.5 million", "22,800 square kilometers", "32,000 square kilometers"], "9.6 million."),
        M("How long is China’s coastline?", "32,000 kilometers", ["22,800 kilometers", "5,500 kilometers", "14,000 kilometers"], "32,000 km: 18,000 mainland and 14,000 island."),
        M("How long is China’s entire national border?", "22,800 kilometers", ["32,000 kilometers", "5,200 kilometers", "9,600 kilometers"], "22,800 km."),
        M("Which sea is called 黄海?", "The Yellow Sea", ["The Bohai Sea", "The East China Sea", "The South China Sea"], "黄海."),
        M("Which sea is called 南海?", "The South China Sea", ["The Yellow Sea", "The Bohai Sea", "The East China Sea"], "南海."),
        M("Which sea is called 渤海?", "The Bohai Sea", ["The Yellow Sea", "The East China Sea", "The South China Sea"], "渤海."),
        M("Which sea is called 东海?", "The East China Sea", ["The South China Sea", "The Yellow Sea", "The Bohai Sea"], "东海."),
        M("Which countries does the reading say also have claims in the South China Sea?", "Vietnam and the Philippines", ["Japan and Korea", "Russia and Mongolia", "India and Nepal"], "Vietnam and the Philippines."),
        M("What does the reading say the U.S. and other Pacific nations insist on?", "That the South China Sea remains open international waters", ["That it belongs to the U.S.", "That it is closed", "That it has no ships"], "Open international waters."),
        M("How many levels does China’s administration have, in the reading?", "Three: provinces, counties and townships", ["Two", "Five only", "One"], "A three-level system."),
        M("How many provinces does the reading list?", "23", ["22", "34", "5"], "23 provinces."),
        M("How many autonomous regions are listed?", "5", ["4", "2", "23"], "5 autonomous regions."),
        M("How many municipalities are listed?", "4", ["5", "2", "23"], "4 municipalities."),
        M("How many special administrative regions are listed?", "2", ["4", "5", "23"], "Hong Kong and Macao."),
        M("Which is NOT one of the five autonomous regions?", "四川", ["西藏", "新疆", "内蒙古"], "四川 is a province."),
        M("Which is NOT one of the four municipalities?", "广州", ["北京", "天津", "重庆"], "广州 is a provincial capital."),
        M("Which two places are the special administrative regions?", "香港 and 澳门", ["北京 and 上海", "天津 and 重庆", "西藏 and 新疆"], "Hong Kong and Macao."),
        M("About how many prefectures are there, according to the reading?", "About 335", ["About 3,000", "About 23", "About 5"], "Approximately 335."),
        M("What are townships called in rural areas?", "Villages (乡)", ["Towns (镇)", "Districts (市辖区)", "Counties (县)"], "乡 in rural areas."),
        M("What are townships called in urban areas?", "Towns (镇)", ["Villages (乡)", "Districts (市辖区)", "Counties (县)"], "镇 in urban areas."),
        mean("省", "sheng3", "province", ["city", "region", "capital"]),
        mean("县", "xian4", "county", ["province", "village", "city"]),
        mean("镇", "zhen4", "town", ["county", "village", "district"]),
    ],
)

UNIT = unit("第五课 The book’s texts: American states, vocabulary and area studies", [L_ST1, L_ST2, L_ST3, L_P3_VOCAB, L_AREA])
