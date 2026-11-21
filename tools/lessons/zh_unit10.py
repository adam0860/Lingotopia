"""Unit 10: cities and population (lessons 95-102): big numbers (万, 亿), zeros inside numbers, cities and
population, 最, 还是, the third tone, tank words, review. Original text; the scope follows DLIFLC Chinese
Basic Program Unit 1 Lesson 5 (City, Population, Seasons, Weather and Climate), Presentation 1."""
from dsl_zh import *

PART = ["吗", "们", "呢"]

# ---------------------------------------------------------------------------- 95
L95 = lesson(
    "Ten thousand and a hundred million",
    "万 · 亿 · 十多万 · 三百多万 · 九百多亿",
    requires=[],
    cards=[
        card("Chinese counts in ten-thousands",
             "English counts in thousands, then millions. Chinese counts in 万 (wàn, 10,000) and 亿 (yì, 100,000,000). "
             "So 100,000 is “ten ten-thousands”, 十万, and a million is “a hundred ten-thousands”, 一百万. "
             "A hundred million is 一亿. The number is built the way you build any other: 三百万 is 3,000,000, and 五千万 is 50,000,000. "
             "Before 万 and 亿 the 一 changes to yí: 一万, 一亿.",
             tables=[wtable([("万", "wan4", "ten thousand"), ("亿", "yi4", "hundred million"), ("十万", "shi2wan4", "100,000"), ("一百万", "yi4bai3wan4", "1,000,000"),
                             ("一千万", "yi4qian1wan4", "10,000,000"), ("一亿", "yi2yi4", "100,000,000"), ("三百万", "san1bai3wan4", "3,000,000"),
                             ("五千万", "wu3qian1wan4", "50,000,000")])]),
        card("多 after the round number",
             "To say “more than” a big number, put 多 after the whole round number and before 万 or 亿. 三百多万 is “over three million” and 十多万 is “over 100,000”. "
             "This is different from small numbers, where 多 comes last (二十多 for “twenty-odd”).",
             examples=[ex("我的老家有三百多万人口。", "wo3 de5 lao3jia1 you3 san1bai3duo1wan4 ren2kou3", "My hometown has a population of more than three million.", hl="三百多万"),
                       ex("这个城市有十多万人。", "zhe4 ge4 cheng2shi4 you3 shi2duo1wan4 ren2", "This city has over 100,000 people."),
                       ex("西安在中国的西北部，人口有一千两百多万。", "xi1'an1 zai4 zhong1guo2 de5 xi1bei3bu4, ren2kou3 you3 yi4qian1 liang3bai3duo1wan4", "Xi’an is in the northwest of China, with a population of over 12 million."),
                       ex("这个公司有八千多万个用户。", "zhe4 ge4 gong1si1 you3 ba1qian1duo1wan4 ge4 yong4hu4", "This company has more than 80 million users.")]),
    ],
    exercises=[
        mean("万", "wan4", "ten thousand", ["hundred thousand", "million", "thousand"]),
        mean("亿", "yi4", "hundred million", ["ten thousand", "billion", "ten million"]),
        mean("十万", "shi2wan4", "100,000", ["10,000", "1,000,000", "10,000,000"]),
        mean("一百万", "yi4bai3wan4", "1,000,000", ["100,000", "10,000,000", "100,000,000"]),
        mean("一亿", "yi2yi4", "100,000,000", ["10,000,000", "1,000,000", "10,000"]),
        rd("万", "wan4", ["wan1", "wan2", "wan3"]),
        rd("亿", "yi4", ["yi1", "yi2", "yi3"]),
        M("What is 三百万?", "3,000,000", ["300,000", "30,000,000", "3,000"], "三百 + 万 is 300 ten-thousands."),
        M("What is 五千万?", "50,000,000", ["5,000,000", "500,000,000", "500,000"], "五千 ten-thousands."),
        M("How do you say 2,000,000?", "两百万", ["二百万", "二万万", "两千万"], "两 before 百."),
        M("How do you say 10,000?", "一万", ["十千", "一千千", "百百"], "一万 is yí wàn."),
        M("What does 三百多万 mean?", "More than three million", ["Three hundred", "Exactly three million", "Under three million"], "多 after the round number means a bit more."),
        M("Where does 多 go in “over 100,000”?", "十多万", ["十万多", "多十万", "十万多个"], "多 goes before 万."),
        M("How do you say “over 50 million”?", "五千多万", ["五千万多", "多五千万", "五多千万"], "多 before 万."),
        F("我的老家有三百___万人口。", "多", ["很", "吗", "们"], "三百多万 is over three million.", tr="My hometown has over three million people."),
        F("这个城市有十___万人。", "多", ["很", "吗", "们"], "十多万 is over 100,000.", tr="This city has over 100,000 people."),
        F("一百万是一百个___。", "万", PART, "一百万 is a hundred ten-thousands.", tr="A million is a hundred ten-thousands."),
    ],
)

# ---------------------------------------------------------------------------- 96
L96 = lesson(
    "Zeros inside a number, and 二 against 两",
    "一百零五 · 三万零五百 · 两千二百 · 十二万",
    requires=[],
    cards=[
        card("Say 零 for a gap",
             "When a number has a gap of one or more zeros inside it, you say 零 (líng) once for the whole gap: 105 is 一百零五, 2,008 is 两千零八, 30,500 is 三万零五百. "
             "At the end of a round number you do not say 零: 一百 is 100 and 一百二 is shorthand for 120. Nothing is said for the gap when the next digit is just one place down, so 1,100 is 一千一百.",
             tables=[wtable([("一百零五", "yi4bai3 ling2 wu3", "105"), ("一百一十", "yi4bai3 yi1shi2", "110"), ("一千零八", "yi4qian1 ling2 ba1", "1,008"),
                             ("一千一百", "yi4qian1 yi4bai3", "1,100"), ("三万零五百", "san1wan4 ling2 wu3bai3", "30,500"), ("三万五千", "san1wan4 wu3qian1", "35,000")])]),
        card("两 or 二?",
             "As the first digit of 百, 千, 万 or 亿, say 两: 两百, 两千, 两万, 两亿. In the tens and ones places, and in dates and digit strings, say 二: 十二, 二十, 二十二, 二十万 (the “20” is in the tens place of a count of ten-thousands). "
             "After a 百 or 千, either may be used, but 两 is the more common: 两千二百.",
             tables=[wtable([("两百", "liang3bai3", "200"), ("两千", "liang3qian1", "2,000"), ("两万", "liang3wan4", "20,000"), ("两亿", "liang3yi4", "200,000,000"),
                             ("十二", "shi2er4", "12"), ("二十二", "er4shi2er4", "22"), ("二十万", "er4shi2wan4", "200,000"), ("两千二百", "liang3qian1 er4bai3", "2,200")])]),
    ],
    exercises=[
        M("How do you say 105?", "一百零五", ["一百五", "一百五十", "一零五"], "A gap of zero is spoken as 零."),
        M("How do you say 110?", "一百一十", ["一百零一十", "一百零十", "一一零"], "No gap, so no 零."),
        M("How do you say 1,008?", "一千零八", ["一千八", "一千零零八", "一千八十"], "One 零 for the gap."),
        M("How do you say 2,005?", "两千零五", ["二千零五", "两千五", "两零零五"], "两 before 千; 零 for the gap."),
        M("How do you say 30,500?", "三万零五百", ["三万五百", "三万五", "三万零零五百"], "A gap between 万 and 百."),
        M("How do you say 35,000?", "三万五千", ["三万零五千", "三万五", "三五千"], "No gap."),
        M("What is 一千一百?", "1,100", ["1,001", "1,010", "11,000"], "一千 + 一百."),
        M("What is 一千零一?", "1,001", ["1,100", "1,010", "11"], "One gap."),
        M("How do you say 200?", "两百", ["二百", "二十百", "两十"], "两 before 百."),
        M("How do you say 22?", "二十二", ["两十二", "二十两", "两十两"], "二 in the tens and ones."),
        M("How do you say 200,000?", "二十万", ["两十万", "两万万", "二百千"], "二十 is in the tens place of 万."),
        M("How do you say 20,000?", "两万", ["二万", "二十千", "两千万"], "两 before 万."),
        M("How do you say 12?", "十二", ["一十二个", "十两", "一二"], "十 + 二."),
        F("两千___八 (2,008)", "零", ["百", "万", "们"], "A gap of zero is 零.", tr="2,008"),
        F("一百___五 (105)", "零", ["万", "亿", "们"], "A gap of zero is 零.", tr="105"),
        F("这个学校有两___学生。 (2,000)", "千", ["吗", "们", "呢"], "两千 is 2,000.", tr="This school has 2,000 students."),
    ],
)

# ---------------------------------------------------------------------------- 97
L97 = lesson(
    "Cities and population",
    "首都 · 人口 · 多少人口 · 只有 · 百分之",
    requires=[],
    cards=[
        card("Capital, city and people",
             "人口 (rénkǒu) is population, and you ask about it with 多少: 北京有多少人口？ 首都 (shǒudū) is a capital: 北京是中国的首都. "
             "A large number is 多 and a small one is 少 (shǎo, few): 东部人口多, 西部人口少. 只有 (zhǐyǒu) means “has only”, and 很少 means “very few” or “rarely”. "
             "百分之 (bǎifēnzhī) is “percent”: 百分之五十 is 50 percent.",
             tables=[wtable([("人口", "ren2kou3", "population"), ("多少", "duo1shao3", "how many, how much"), ("首都", "shou3du1", "a capital"), ("少", "shao3", "few, little"),
                             ("只有", "zhi3you3", "has only"), ("很少", "hen3shao3", "very few, rarely"), ("百分之", "bai3fen1zhi1", "percent"), ("大城市", "da4 cheng2shi4", "a big city")])]),
        card("Talking about a place",
             "Put these together to describe a hometown: its size, its people and its place.",
             examples=[ex("北京是中国的首都。", "bei3jing1 shi4 zhong1guo2 de5 shou3du1", "Beijing is the capital of China.", hl="首都"),
                       ex("北京有多少人口？ 北京有两千多万人口。", "bei3jing1 you3 duo1shao3 ren2kou3? bei3jing1 you3 liang3qian1 duo1wan4 ren2kou3", "What is the population of Beijing? More than 20 million.", hl="多少"),
                       ex("我的老家是一个小城市，只有十几万人。", "wo3 de5 lao3jia1 shi4 yi2 ge4 xiao3 cheng2shi4, zhi3 you3 shi2ji3wan4 ren2", "My hometown is a small city with only a few hundred thousand people.", hl="只有"),
                       ex("中国东部人口多，西部人口少。", "zhong1guo2 dong1bu4 ren2kou3 duo1, xi1bu4 ren2kou3 shao3", "The east of China has many people and the west has few."),
                       ex("我们班有百分之五十的同学是东部人。", "wo3men5 ban1 you3 bai3fen1zhi1 wu3shi2 de5 tong2xue2 shi4 dong1bu4 ren2", "Half of our class are from the east.", hl="百分之五十")]),
    ],
    exercises=[
        mean("人口", "ren2kou3", "population", ["a person", "a mouth", "a family"]),
        mean("首都", "shou3du1", "a capital", ["a big city", "a state", "a base"]),
        mean("多少", "duo1shao3", "how many, how much", ["a few", "very many", "very few"]),
        mean("少", "shao3", "few, little", ["many", "big", "old"]),
        mean("只有", "zhi3you3", "has only", ["also has", "does not have", "has many"]),
        mean("百分之", "bai3fen1zhi1", "percent", ["hundred", "a hundredth part", "one hundred people"]),
        rd("人口", "ren2kou3", ["ren2kou4", "ren4kou3", "ren2kuo3"]),
        rd("首都", "shou3du1", ["shou3du2", "shou4du1", "shou3duo1"]),
        rd("少", "shao3", ["shao1", "shao2", "sao3"]),
        M("Which asks for the population?", "北京有多少人口？", ["北京有几个人？", "北京有谁？", "北京在哪儿？"], "多少人口 asks the population."),
        M("What does 北京是中国的首都 say?", "Beijing is the capital of China.", ["Beijing is the biggest city in China.", "Beijing is in the east.", "Beijing has the most people."], "首都 is capital."),
        M("What does 只有十几万人 mean?", "has only a hundred-odd thousand people", ["has over a million people", "has no people", "has ten people"], "十几万 is 110,000 to 190,000."),
        M("What is 百分之五十?", "50 percent", ["5 percent", "500 percent", "15 percent"], "百分之 + 50."),
        M("How do you say “East China has many people”?", "中国东部人口多。", ["中国东部多人口。", "中国东部人口很多的人。", "东部中国人口多。"], "Topic + 人口 + 多."),
        F("北京有两千___万人口。", "多", ["很", "吗", "们"], "两千多万 is over 20 million.", tr="Beijing has over 20 million people."),
        F("北京有多___人口？", "少", ["多", "吗", "们"], "多少 is how many.", tr="What is the population of Beijing?"),
        F("我的老家___有十几万人。 (only)", "只", ["很", "吗", "们"], "只有 is has only.", tr="My hometown has only a hundred-odd thousand people."),
        F("百___之五十的人住在东部。", "分", ["们", "吗", "呢"], "百分之 is percent.", tr="Fifty percent of the people live in the east."),
    ],
)

# ---------------------------------------------------------------------------- 98
L98 = lesson(
    "The most: 最",
    "最大 · 最小 · 最多 · 最好 · 最高 · 最低",
    requires=[],
    cards=[
        card("最 before an adjective",
             "最 (zuì) means “the most” and goes before an adjective: 最大 is “biggest”, 最小 “smallest”, 最多 “most”, 最好 “best”, 最高 “highest” and 最低 “lowest”. "
             "To use it before a noun, add 的: 最大的城市 is “the biggest city”. The same word works in questions: 谁的中文最好？ asks whose Chinese is best.",
             tables=[wtable([("最", "zui4", "the most"), ("最大", "zui4 da4", "biggest"), ("最小", "zui4 xiao3", "smallest"), ("最多", "zui4 duo1", "most"), ("最好", "zui4 hao3", "best"),
                             ("最高", "zui4 gao1", "highest, tallest"), ("最低", "zui4 di1", "lowest")])]),
        card("Examples",
             "Notice how 最 sits right before the adjective, and 的 links the adjective to the noun.",
             examples=[ex("我是我们家最小的孩子。", "wo3 shi4 wo3men5 jia1 zui4 xiao3 de5 hai2zi5", "I am the youngest child in our family.", hl="最小"),
                       ex("在我们班，李明的中文最好。", "zai4 wo3men5 ban1, li3 ming2 de5 zhong1wen2 zui4 hao3", "In our class, Li Ming’s Chinese is the best.", hl="最好"),
                       ex("这是我们学校最大的教室。", "zhe4 shi4 wo3men5 xue2xiao4 zui4 da4 de5 jiao4shi4", "This is the biggest classroom in our school."),
                       ex("在你家，谁的年龄最大？", "zai4 ni3 jia1, shei2 de5 nian2ling2 zui4 da4", "In your family, who is the oldest?")]),
    ],
    exercises=[
        mean("最", "zui4", "the most", ["a little", "also", "very"]),
        mean("最大", "zui4 da4", "biggest", ["bigger", "very big", "big"]),
        mean("最小", "zui4 xiao3", "smallest", ["smaller", "very small", "small"]),
        mean("最好", "zui4 hao3", "best", ["better", "very good", "good"]),
        mean("最高", "zui4 gao1", "highest, tallest", ["higher", "very high", "high"]),
        mean("最低", "zui4 di1", "lowest", ["lower", "very low", "low"]),
        rd("最", "zui4", ["zui1", "zui2", "zui3"]),
        rd("最大", "zui4 da4", ["zui4 da1", "zui2 da4", "zui4 dai4"]),
        M("What does 我是我们家最小的孩子 say?", "I am the youngest child in our family.", ["I have the youngest child.", "I am the smallest person.", "I am the eldest child."], "最小 is youngest here."),
        M("What does 谁的中文最好？ ask?", "Whose Chinese is the best?", ["Who studies Chinese?", "Whose Chinese is bad?", "Who likes Chinese?"], "最好 asks for the best."),
        M("How do you say “the biggest city”?", "最大的城市", ["最的大城市", "大最的城市", "城市最大"], "最 + adjective + 的 + noun."),
        M("Where does 最 go?", "Before the adjective", ["After the adjective", "Before the subject", "At the end"], "最 + adjective."),
        M("How do you say “the lowest temperature”? (the pattern)", "最低气温", ["最气温低", "气温最的低", "低最气温"], "最低 + noun."),
        F("这是我们学校___大的教室。", "最", ["很", "吗", "们"], "最大 is biggest.", tr="This is the biggest classroom in our school."),
        F("在我们班，谁的中文最___？", "好", ["吗", "们", "呢"], "最好 is best.", tr="In our class, whose Chinese is best?"),
        F("他是我们班最高___学生。", "的", ["吗", "们", "呢"], "的 links the adjective and the noun.", tr="He is the tallest student in our class."),
        F("我是家里最小___孩子。", "的", ["吗", "们", "呢"], "最小的孩子.", tr="I am the youngest child at home."),
    ],
)

# ---------------------------------------------------------------------------- 99
L99 = lesson(
    "Choosing: 还是",
    "你是南方人还是北方人？ · 东部人口多还是西部人口多？",
    requires=[],
    cards=[
        card("A or B?",
             "还是 (háishi) asks the listener to choose between two options, like “or” in a question: Option A 还是 Option B? "
             "你爸爸是北方人还是南方人？ is “Is your father a northerner or a southerner?”. You answer by naming one: 他是南方人. "
             "还是 belongs to questions; a plain statement with “or” uses another word later.",
             tables=[table(["Question", "Meaning"],
                           [["你爸爸是北方人还是南方人？", "Is your father a northerner or a southerner?"], ["东部人口多还是西部人口多？", "Does the east or the west have more people?"],
                            ["你的老家在纽约还是在华盛顿？", "Is your hometown in New York or Washington?"], ["你姐姐在中学教书还是在大学教书？", "Does your sister teach at a middle school or a university?"]], say=[0])]),
        card("How to answer",
             "There is no yes or no. Pick one option and say it as a whole short sentence, or just give the option.",
             examples=[ex("你是学生还是老师？ 我是学生。", "ni3 shi4 xue2sheng5 hai2shi5 lao3shi1? wo3 shi4 xue2sheng5", "Are you a student or a teacher? I am a student.", hl="还是"),
                       ex("你喜欢夏天还是冬天？ 我喜欢冬天。", "ni3 xi3huan5 xia4tian1 hai2shi5 dong1tian1? wo3 xi3huan5 dong1tian1", "Do you like summer or winter? I like winter."),
                       ex("你要茶还是咖啡？", "ni3 yao4 cha2 hai2shi5 ka1fei1", "Do you want tea or coffee?"),
                       ex("北京大还是上海大？", "bei3jing1 da4 hai2shi5 shang4hai3 da4", "Is Beijing bigger or Shanghai?")]),
    ],
    exercises=[
        mean("还是", "hai2shi5", "or (in questions)", ["still (in a statement)", "and", "also"]),
        rd("还是", "hai2shi4", ["hai1shi4", "hai3shi4", "hai4shi4"]),
        M("What is 你是学生还是老师？ asking?", "Are you a student or a teacher?", ["Are you a student, and a teacher?", "Are you a student?", "Who is a teacher?"], "还是 offers two choices."),
        M("How do you answer 你喜欢夏天还是冬天？", "I like winter.", ["Yes.", "No.", "I do not know."], "Name one of the options."),
        M("Which is a good question with 还是?", "你爸爸是北方人还是南方人？", ["你爸爸是北方人还是南方人吗？", "你爸爸是还是北方人南方人？", "你爸爸还是北方人是南方人？"], "A 还是 B, with no 吗."),
        M("Does a 还是 question take 吗?", "No", ["Yes, always", "Only in the north", "Only in writing"], "还是 already asks the question."),
        M("How do you ask “Is Beijing or Shanghai bigger?”", "北京大还是上海大？", ["北京还是大上海大？", "北京大上海大还是？", "还是北京大上海大？"], "A + adjective 还是 B + adjective."),
        M("How do you ask “Is your hometown in New York or Washington?”", "你的老家在纽约还是在华盛顿？", ["你的老家纽约还是在在华盛顿？", "你的还是老家在纽约在华盛顿？", "你的老家在还是纽约华盛顿？"], "在 A 还是在 B."),
        F("你是学生___是老师？", "还", PART, "还是 is or.", tr="Are you a student or a teacher?"),
        F("你喜欢夏天还是冬___？", "天", PART, "冬天 is winter.", tr="Do you like summer or winter?"),
        F("东部人口多还___西部人口多？", "是", PART, "还是 is or.", tr="Does the east or the west have more people?"),
        F("你的老家在纽约还是在华盛___？", "顿", PART, "华盛顿.", tr="Is your hometown in New York or Washington?"),
    ],
)

# ---------------------------------------------------------------------------- 100
L100 = lesson(
    "The third tone",
    "老家 · 老人 · 老师 · 老百姓 · 领子",
    requires=[],
    cards=[
        card("Third tone before every tone",
             "The third tone dips and rises (ǎ), but when something follows, you only say the dip. In 老家 (lǎojiā), 老人 (lǎorén), 老式 (lǎoshì) the 老 is a low tone that stays down. "
             "The big exception: two third tones in a row. The first one becomes a second tone, a rising one: 老手 is written lǎoshǒu but said láoshǒu. "
             "The pinyin in the app is spelled with the underlying tone, so you apply the change as you read.",
             tables=[wtable([("老家", "lao3jia1", "hometown (3rd + 1st)"), ("老兵", "lao3bing1", "a veteran (3rd + 1st)"), ("老人", "lao3ren2", "an old person (3rd + 2nd)"),
                             ("老实", "lao3shi5", "honest (3rd + neutral)"), ("老手", "lao3shou3", "an old hand (3rd + 3rd: said láoshǒu)"), ("老式", "lao3shi4", "old-fashioned (3rd + 4th)"),
                             ("领子", "ling3zi5", "a collar (3rd + neutral)"), ("嗓子", "sang3zi5", "throat, voice (3rd + neutral)")])]),
        card("老 is not always “old”, and 子 is a marker",
             "Used as a prefix, 老 often has no “old” in it: 老师 is a teacher, 老乡 is someone from your home town, 老鹰 is an eagle and 老百姓 means ordinary people. "
             "The suffix 子 has no meaning of its own: it marks a noun, and is always in the neutral tone.",
             tables=[wtable([("老师", "lao3shi1", "a teacher"), ("老乡", "lao3xiang1", "a fellow townsman"), ("老鹰", "lao3ying1", "an eagle"), ("老百姓", "lao3bai3xing4", "ordinary people"),
                             ("老年人", "lao3nian2ren2", "elderly people"), ("饺子", "jiao3zi5", "dumplings")])]),
    ],
    exercises=[
        mean("老家", "lao3jia1", "hometown", ["an old house", "an old man", "a family"]),
        mean("老兵", "lao3bing1", "a veteran", ["a new soldier", "an old man", "an officer"]),
        mean("老人", "lao3ren2", "an old person", ["a hometown", "an adult", "an ordinary person"]),
        mean("老实", "lao3shi5", "honest", ["old", "teacher", "real"]),
        mean("老手", "lao3shou3", "an old hand", ["a hand", "an old man", "a beginner"]),
        mean("老式", "lao3shi4", "old-fashioned", ["new", "a teacher", "honest"]),
        mean("老师", "lao3shi1", "a teacher", ["an old man", "a veteran", "a student"]),
        mean("老百姓", "lao3bai3xing4", "ordinary people", ["old people", "a hundred people", "soldiers"]),
        mean("饺子", "jiao3zi5", "dumplings", ["a collar", "a throat", "a child"]),
        M("How is 老 said in 老手?", "láo (2nd tone)", ["lǎo (3rd tone)", "lào (4th tone)", "lāo (1st tone)"], "Two third tones in a row: the first rises."),
        M("How is 老手 really said?", "láoshǒu", ["lǎoshǒu", "lǎoshóu", "làoshǒu"], "3rd + 3rd becomes 2nd + 3rd."),
        M("What tone does 子 have in 领子?", "Neutral", ["First", "Second", "Fourth"], "The suffix 子 is always neutral."),
        M("What does the suffix 子 mean?", "Nothing; it marks a noun", ["small", "child", "old"], "子 only marks a noun."),
        M("Is 老 always “old”?", "No: in 老师 it is just a prefix", ["Yes", "Only in names", "Only before 人"], "老师 is a teacher."),
        M("Which word does not mean “old”?", "老师", ["老人", "老式", "老年人"], "老师 is teacher."),
        rd("老师", "lao3shi1", ["lao3shi2", "lao4shi1", "lao3shi4"]),
        rd("嗓子", "sang3zi5", ["sang3zi4", "sang1zi5", "sang3zi3"]),
    ],
)

# ---------------------------------------------------------------------------- 101
L101 = lesson(
    "Military words: tanks",
    "坦克 · 装甲车 · 装甲部队 · 轻坦克 · 重坦克",
    requires=[],
    cards=[
        card("Tanks and armoured vehicles",
             "坦克 (tǎnkè) is a tank, a word borrowed from English. 装甲 (zhuāngjiǎ) is armour, so 装甲车 is an armoured vehicle. "
             "部队 (bùduì) is a military unit, and so 坦克部队 is a tank unit and 装甲部队 an armoured unit. "
             "A word in front says what kind of tank: 轻 (qīng) is light, 重 (zhòng) is heavy, and 两栖 (liǎngqī) is amphibious, “living in two places”.",
             tables=[wtable([("坦克", "tan3ke4", "a tank"), ("装甲车", "zhuang1jia3che1", "an armoured vehicle"), ("部队", "bu4dui4", "a military unit"), ("坦克部队", "tan3ke4 bu4dui4", "a tank unit"),
                             ("装甲部队", "zhuang1jia3 bu4dui4", "an armoured unit"), ("轻坦克", "qing1 tan3ke4", "a light tank"), ("重坦克", "zhong4 tan3ke4", "a heavy tank"),
                             ("两栖坦克", "liang3qi1 tan3ke4", "an amphibious tank")])]),
        card("Using the words",
             "These are names to recognise. Use 这是 and 那是 to point to something, and 他在 plus a unit to say where someone serves.",
             examples=[ex("这是坦克。", "zhe4 shi4 tan3ke4", "This is a tank."),
                       ex("那是装甲车。", "na4 shi4 zhuang1jia3che1", "That is an armoured vehicle."),
                       ex("他在坦克部队工作。", "ta1 zai4 tan3ke4 bu4dui4 gong1zuo4", "He serves in a tank unit.", hl="坦克部队")]),
    ],
    exercises=[
        mean("坦克", "tan3ke4", "a tank", ["a truck", "a jeep", "a ship"]),
        mean("装甲车", "zhuang1jia3che1", "an armoured vehicle", ["a tank", "a jeep", "a bus"]),
        mean("部队", "bu4dui4", "a military unit", ["a school", "a base", "a hospital"]),
        mean("坦克部队", "tan3ke4 bu4dui4", "a tank unit", ["a tank school", "an armoured vehicle", "a heavy tank"]),
        mean("装甲部队", "zhuang1jia3 bu4dui4", "an armoured unit", ["a tank", "a navy unit", "an air unit"]),
        mean("轻坦克", "qing1 tan3ke4", "a light tank", ["a heavy tank", "an amphibious tank", "a tank unit"]),
        mean("重坦克", "zhong4 tan3ke4", "a heavy tank", ["a light tank", "an amphibious tank", "a tank unit"]),
        mean("两栖坦克", "liang3qi1 tan3ke4", "an amphibious tank", ["a heavy tank", "a light tank", "a ship"]),
        rd("坦克", "tan3ke4", ["tan3ke1", "tan2ke4", "tan4ke4"]),
        rd("装甲车", "zhuang1jia3che1", ["zhuang1jia3che2", "zhuang4jia3che1", "zhuang1jia4che1"]),
        rd("部队", "bu4dui4", ["bu4dui1", "bu3dui4", "bu4dui2"]),
        M("What does 装甲 mean?", "armour", ["tank", "unit", "speed"], "装甲 is armour."),
        M("What does 两栖 suggest?", "amphibious", ["heavy", "light", "fast"], "两栖 means living in two places."),
        M("How do you say “a tank unit”?", "坦克部队", ["部队坦克", "坦克的车", "车坦克部队"], "坦克 + 部队."),
        M("Which is the opposite of 轻坦克?", "重坦克", ["两栖坦克", "坦克部队", "装甲车"], "轻 is light, 重 heavy."),
        F("这是___克。 (tank)", "坦", PART, "坦克 is a tank.", tr="This is a tank."),
        F("他在坦克部___工作。", "队", PART, "部队 is a unit.", tr="He serves in a tank unit."),
    ],
)

# ---------------------------------------------------------------------------- 102
L102 = lesson(
    "Review: cities and population",
    "万 亿 零 · 人口 · 最 · 还是 · 老",
    requires=[],
    cards=[
        card("What you can now do",
             "You can read big numbers, give a population, name the biggest or the most, offer a choice with 还是 and read the third tone. These questions mix them.",
             examples=[ex("北京有多少人口？ 北京有两千多万人口。", "bei3jing1 you3 duo1shao3 ren2kou3? bei3jing1 you3 liang3qian1 duo1wan4 ren2kou3", "What is the population of Beijing? Over 20 million."),
                       ex("东部人口多还是西部人口多？", "dong1bu4 ren2kou3 duo1 hai2shi5 xi1bu4 ren2kou3 duo1", "Does the east or the west have more people?"),
                       ex("我是我们家最小的孩子。", "wo3 shi4 wo3men5 jia1 zui4 xiao3 de5 hai2zi5", "I am the youngest child in our family.")]),
    ],
    exercises=[
        M("How do you say 3,000,000?", "三百万", ["三千万", "三十万", "三万万"], "三百 ten-thousands."),
        M("How do you say 2,008?", "两千零八", ["两千八", "二千零零八", "两零零八"], "两千 + 零 + 八."),
        M("How do you say 200,000?", "二十万", ["两十万", "两万万", "二百千"], "二十 ten-thousands."),
        M("What does 十几万 mean?", "110,000 to 190,000", ["10,000", "Over a million", "100"], "十几 is eleven to nineteen."),
        M("What does 三百多万 mean?", "More than three million", ["Exactly three million", "Under three million", "Three hundred"], "多 after the round number."),
        M("What is 百分之五十?", "50 percent", ["5 percent", "15 percent", "500"], "百分之 + number."),
        M("How do you say “the biggest city”?", "最大的城市", ["大最的城市", "最城市大", "城市最的大"], "最 + adjective + 的 + noun."),
        M("Which asks a choice?", "你是学生还是老师？", ["你是学生吗？", "你是老师吧？", "你是学生老师？"], "还是 offers two choices."),
        M("How is 老手 said?", "láoshǒu", ["lǎoshǒu", "lǎoshóu", "làoshǒu"], "3rd + 3rd."),
        M("What does 首都 mean?", "a capital", ["a big city", "a state", "a base"], "首都 is a capital."),
        mean("人口", "ren2kou3", "population", ["a person", "a mouth", "a family"]),
        mean("坦克", "tan3ke4", "a tank", ["a truck", "a jeep", "a ship"]),
        rd("人口", "ren2kou3", ["ren2kou4", "ren4kou3", "ren2kuo3"]),
        F("北京有两千___万人口。", "多", ["很", "吗", "们"], "两千多万 is over 20 million.", tr="Beijing has over 20 million people."),
        F("这是我们学校___大的教室。", "最", ["很", "吗", "们"], "最大.", tr="This is the biggest classroom in our school."),
        F("东部人口多还___西部人口多？", "是", PART, "还是 is or.", tr="Does the east or the west have more people?"),
    ],
)

UNIT = unit("第五课 Cities and population", [L95, L96, L97, L98, L99, L100, L101, L102])
