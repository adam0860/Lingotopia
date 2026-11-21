"""Unit 13: Lesson 5 book texts, Presentation 1 (cities and population): the dialog, the readings, the book's
example sentences, the third-tone and tank word lists, the vocabulary list and the speaking tasks.
These lessons come after the original Lesson 5 lessons (95-123) so saved progress keeps its ids.
Audio items of the book are not included; everything readable is."""
from zh_auto import *

PART = ["吗", "们", "呢"]

# ---------------------------------------------------------------------------- Presentation 1 dialog
L_P1_DIALOG = lesson(
    "Dialog: Teacher Fang and David talk about cities",
    "北京是中国的首都 · 重庆有三千一百万人口 · 百分之九十多的人口都住在东部",
    requires=[],
    cards=[
        card("Before you read: three questions (Getting Started)",
             "The book opens the presentation with three questions to talk about with a partner. "
             "A. What is the capital of the U.S.? Where is it located? "
             "B. What is the largest city in the U.S.? Do you know its population? "
             "C. Which part of the U.S. has the largest population? Do you know which part of China has the largest population?",
             tables=[]),
        card("The dialog (Presentation 1)",
             "David (陆大卫) asks his teacher, Professor Fang (方老师), about his hometown, cities and population. The figures are the ones in the book's dialog.",
             examples=dlg([
                 ("陆大卫", "方老师，你是北京人吗？", "Teacher Fang, are you from Beijing?"),
                 ("方老师", "对，我是北京人。北京是中国的首都。", "Yes, I am from Beijing. Beijing is the capital of China."),
                 ("陆大卫", "北京有多少人口？", "What is the population of Beijing?"),
                 ("方老师", "北京有两千一百多万人口。", "Beijing has a population of more than 21 million."),
                 ("陆大卫", "那北京是中国最大的城市吗？", "Then is Beijing the largest city in China?"),
                 ("方老师", "不是，中国最大的城市是重庆。重庆有三千一百万人口。", "No. The largest city in China is Chongqing. Chongqing has a population of 31 million."),
                 ("陆大卫", "中国的大城市都在东部吗？", "Are all of China's big cities in the east?"),
                 ("方老师", "不是，北京在东部，重庆在西部。", "No. Beijing is in the east and Chongqing is in the west."),
                 ("陆大卫", "中国东部人口多还是西部人口多？", "Does the east or the west of China have more people?"),
                 ("方老师", "东部人口多，百分之九十多的人口都住在东部。那美国呢？", "The east has more. More than 90 percent of the population live in the east. And the U.S.?"),
                 ("陆大卫", "美国东部、西部人口都很多，中西部人很少。", "In the U.S. both the east and the west have many people, and the middle west has few."),
                 ("方老师", "大卫，你的老家有多少人口？", "David, what is the population of your hometown?"),
                 ("陆大卫", "我的老家是一个小城市，只有十几万人。", "My hometown is a small city, with only a hundred-odd thousand people."),
             ])),
    ],
    exercises=[
        M("Where is Professor Fang from?", "Beijing", ["Chongqing", "Texas", "Chengdu"], "我是北京人."),
        M("What is Beijing, according to the dialog?", "The capital of China", ["The largest city in China", "A small city in the west", "A province"], "北京是中国的首都."),
        M("How many people does Beijing have, according to Professor Fang?", "More than 21 million", ["31 million", "More than 12 million", "A hundred-odd thousand"], "两千一百多万."),
        M("Which city does Professor Fang call the largest in China?", "Chongqing", ["Beijing", "Shanghai", "Xi’an"], "中国最大的城市是重庆."),
        M("How many people does Chongqing have, in the dialog?", "31 million", ["21 million", "13 million", "3.1 million"], "三千一百万."),
        M("Where is Chongqing, according to the dialog?", "In the west", ["In the east", "In the north", "In the middle"], "重庆在西部."),
        M("What share of China’s people live in the east?", "More than 90 percent", ["Half", "Less than 10 percent", "All of them"], "百分之九十多."),
        M("What does David say about the middle west of the U.S.?", "It has few people", ["It has the most people", "It is the biggest city", "It has no cities"], "中西部人很少."),
        M("What is David’s hometown like?", "A small city of a hundred-odd thousand people", ["A city of over 21 million", "The capital of the U.S.", "A province in the east"], "只有十几万人."),
        M("Which sentence asks for a choice?", "中国东部人口多还是西部人口多？", ["北京有多少人口？", "你是北京人吗？", "你的老家有多少人口？"], "还是 offers two choices."),
        M("How do you say “more than 90 percent”?", "百分之九十多", ["九十多百分之", "百分之多九十", "九十百分之多"], "百分之 + number + 多."),
        F("北京有两千一百___万人口。", "多", PART, "两千一百多万.", tr="Beijing has more than 21 million people."),
        F("中国东部人口多___是西部人口多？", "还", PART, "还是.", tr="Does the east or the west have more people?"),
        F("我的老家是一个小城市，___有十几万人。", "只", PART, "只有.", tr="My hometown is a small city, with only a hundred-odd thousand people."),
    ],
)

# ---------------------------------------------------------------------------- book examples: 多, 最, 还是
L_P1_GRAMMAR = lesson(
    "The book’s examples: 多, 最 and 还是",
    "八千多万 · 九百多亿 · 最小 · 最多 · 还是",
    requires=[],
    cards=[
        card("The numeral 多 (book note)",
             "When 多 follows 十万, 百万, 千万, 百亿, 万亿 and so on, 多 usually comes before the second numeral: 十多万 is over 100 thousand, 三百多万 over 3 million, "
             "八千多万 over 80 million and 九百多亿 over 90 billion.",
             tables=[wtable([("十多万", "shi2duo1wan4", "over 100 thousand"), ("三百多万", "san1bai3duo1wan4", "over 3 million"), ("八千多万", "ba1qian1duo1wan4", "over 80 million"),
                             ("九百多亿", "jiu3bai3duo1yi4", "over 90 billion")])],
             examples=[D("北京有七十多万大学生。", "There are more than 700,000 college students in Beijing."),
                       D("我的老家有三百多万人口。", "My hometown has a population of more than three million."),
                       D("西安在中国的西北部，人口有一千两百多万。", "Xi’an is in the northwest of China with a population of over 12 million.")]),
        card("The superlative 最 (book note and examples)",
             "最 is placed before an adjective to form its superlative: 最 + adjective.",
             examples=[D("我是我们家最小的孩子。", "I am the youngest child in the family."),
                       D("在我们班，琳达的中文最好。", "Linda’s Chinese is the best in our class."),
                       D("中国是人口最多的国家。", "China is the most populous country.")]),
        card("Practice questions with 最 (Activity 3)",
             "Student A asks, Student B answers with the same pattern.",
             examples=[D("谁是我们班最好的学生？", "Who is the best student in our class?"),
                       D("哪个城市是中国最大的城市？", "Which city is the largest city in China?"),
                       D("美国哪个城市人口最多？", "Which city in the U.S. has the largest population?"),
                       D("在你家，谁的年龄最大？", "In your family, whose age is the greatest?"),
                       D("哪个国家的人口最多？", "Which country has the largest population?")]),
        card("The choice question with 还是 (book note and examples)",
             "还是 asks which of two choices is correct, like “or” in English: Option A + 还是 + Option B?",
             examples=[D("你爸爸是北方人还是南方人？", "Is your father a northerner or a southerner?"),
                       D("你姐姐在中学教书还是在大学教书？", "Does your eldest sister teach in a middle school or a college?"),
                       D("美国东部人口多还是西部人口多？", "Does the east or the west have the greater population in the U.S.?"),
                       D("你的老家在纽约还是在华盛顿？", "Is your hometown in New York or in Washington?"),
                       D("中国人口多还是日本人口多？", "Does China or Japan have more people? (the book’s example for pairs such as 美国/英国, 北京/上海, 纽约/洛杉矶)")]),
    ],
    exercises=[
        M("How do you say “over 80 million”?", "八千多万", ["八多千万", "多八千万", "八千万多"], "多 before 万."),
        M("How do you say “over 90 billion”?", "九百多亿", ["九百亿多", "九多百亿", "多九百亿"], "多 before 亿."),
        M("What does 北京有七十多万大学生 say?", "There are more than 700,000 college students in Beijing.", ["There are 70 college students in Beijing.", "Beijing has over 7 million students.", "There are 7,000 college students."], "七十多万 is over 700,000."),
        M("What does 在我们班，琳达的中文最好 say?", "Linda’s Chinese is the best in our class.", ["Linda studies Chinese the most.", "Linda is the best teacher.", "Linda is in the Chinese class."], "最好 is best."),
        M("What does 我是我们家最小的孩子 say?", "I am the youngest child in the family.", ["I am the smallest person.", "I have the youngest child.", "I am the only child."], "最小的孩子 is the youngest child."),
        M("What does 中国是人口最多的国家 say?", "China is the most populous country.", ["China has many countries.", "China is the biggest country.", "China has few people."], "人口最多 is the largest population."),
        M("Which asks “Which city in the U.S. has the largest population?”", "美国哪个城市人口最多？", ["哪个美国城市人口多最？", "美国最哪个城市人口？", "人口美国哪个最城市？"], "美国 + 哪个城市 + 人口最多."),
        M("Which asks “In your family, whose age is the greatest?”", "在你家，谁的年龄最大？", ["在你家，最谁的年龄大？", "你家在，谁年龄的最大？", "在你家，年龄谁的最大？"], "谁的年龄最大."),
        M("Choose the question that offers a choice between two jobs.", "你姐姐在中学教书还是在大学教书？", ["你姐姐在中学教书吗还是大学？", "你姐姐还是在中学教书大学？", "你姐姐教书在中学大学还是？"], "A 还是 B."),
        M("Is 你的老家在纽约还是在华盛顿？ answered with yes or no?", "No, you name one of the two", ["Yes", "No", "Only with 吗"], "A choice question is answered with one choice."),
        mean("最", "zui4", "the most", ["a little", "also", "very"]),
        mean("还是", "hai2shi5", "or (in questions)", ["still (in a statement)", "and", "also"]),
        F("我是我们家___小的孩子。", "最", PART, "最小.", tr="I am the youngest child in the family."),
        F("你姐姐在中学教书___是在大学教书？", "还", PART, "还是.", tr="Does your eldest sister teach in a middle school or a college?"),
    ],
)

# ---------------------------------------------------------------------------- readings: Sichuan and California
L_P1_READINGS = lesson(
    "Two readings: Sichuan and California",
    "四川 · 成都 · 四川大学 · 加州 · 洛杉矶 · 蒙特雷",
    requires=[],
    cards=[
        card("Reading 1: 四川 (Sichuan)",
             "Group A reads this passage in the book. New words in it: 以前 (yǐqián, before), 省会 (shěnghuì, capital city), 外国 (wàiguó, foreign). 成都 is Chéngdū.",
             examples=[D("四川在中国的西南部，人口有八千三百七十多万，以前是中国人口最多的省。", "Sichuan is in the southwest of China with a population of more than 83.7 million, and it used to be the province with the largest population in China."),
                       D("四川最大的城市是成都。", "The largest city in Sichuan is Chengdu."),
                       D("成都是四川的省会，人口有一千六百多万。", "Chengdu is the capital of Sichuan, with a population of more than 16 million."),
                       D("四川有很多好大学。", "Sichuan has many good universities."),
                       D("四川大学就在成都，有七万多学生和五千四百多老师。", "Sichuan University is right in Chengdu, with more than 70,000 students and more than 5,400 teachers."),
                       D("四川大学也有很多外国学生。", "Sichuan University also has many foreign students."),
                       D("他们在那儿学习中文。", "They study Chinese there.")]),
        card("Reading 2: 加州 (California)",
             "Group B reads this passage. 洛杉矶 is Luòshānjī (Los Angeles); 蒙特雷 is Méngtèléi (Monterey).",
             examples=[D("加州在美国的西部，人口有三千九百三十多万，是美国人口最多的州。", "California is in the west of the U.S., with a population of more than 39.3 million, and it is the state with the largest population in the U.S."),
                       D("加州最大的城市是洛杉矶，在加州的西南部。", "The largest city in California is Los Angeles, in the southwest of California."),
                       D("洛杉矶也是美国西部最大的城市，有三百九十七万多人口。", "Los Angeles is also the largest city in the western U.S., with a population of more than 3.97 million."),
                       D("我们学校在加州的蒙特雷市。", "Our school is in the city of Monterey, California."),
                       D("蒙特雷是一个小城市，人口不多，只有两万七千多人。", "Monterey is a small city. Its population is not large; it has only more than 27,000 people."),
                       D("我们学校有很多学中文的学生，也有很多中文老师。", "Our school has many students who study Chinese, and also many Chinese teachers.")]),
        card("Put the statements in order (Activity 4)",
             "Read these seven statements, then put them in a logical order with a partner: "
             "1. 四川最大的城市是成都。 2. 我妈妈的老家在重庆。 3. 四川在中国的西南部。 4. 重庆是中国最大的城市。 5. 我爸爸的老家在四川。 6. 重庆有三千一百万人口。 7. 成都有一千六百三十多万人口。 "
             "One logical order is 4, 6, 2, 5, 3, 1, 7.",
             examples=[D("四川最大的城市是成都。", "The largest city in Sichuan is Chengdu."),
                       D("我妈妈的老家在重庆。", "My mother’s hometown is in Chongqing."),
                       D("四川在中国的西南部。", "Sichuan is in the southwest of China."),
                       D("重庆是中国最大的城市。", "Chongqing is the largest city in China."),
                       D("我爸爸的老家在四川。", "My father’s hometown is in Sichuan."),
                       D("重庆有三千一百万人口。", "Chongqing has a population of 31 million."),
                       D("成都有一千六百三十多万人口。", "Chengdu has a population of more than 16.3 million.")]),
    ],
    exercises=[
        M("Where is Sichuan?", "In the southwest of China", ["In the northwest", "In the east", "In the northeast"], "四川在中国的西南部."),
        M("What is the largest city in Sichuan?", "Chengdu", ["Chongqing", "Los Angeles", "Beijing"], "四川最大的城市是成都."),
        M("What is Chengdu to Sichuan?", "Its provincial capital", ["A university", "A foreign student", "A county"], "成都是四川的省会."),
        M("How many students does Sichuan University have?", "More than 70,000", ["More than 5,400", "More than 16 million", "27,000"], "七万多学生."),
        M("How many teachers does Sichuan University have?", "More than 5,400", ["More than 70,000", "More than 16 million", "27,000"], "五千四百多老师."),
        M("What do the foreign students do at Sichuan University?", "Study Chinese", ["Teach English", "Study in Texas", "Work at a company"], "他们在那儿学习中文."),
        M("What is special about California in the U.S.?", "It has the largest population among the states", ["It is in the east", "It has the smallest cities", "It has no schools"], "是美国人口最多的州."),
        M("What is the largest city in California?", "Los Angeles", ["Monterey", "Chengdu", "San Francisco"], "加州最大的城市是洛杉矶."),
        M("Where is Los Angeles in California?", "In the southwest", ["In the northeast", "In the middle", "In the east"], "在加州的西南部."),
        M("How many people live in Monterey?", "More than 27,000", ["More than 3.97 million", "More than 39.3 million", "Over 21 million"], "只有两万七千多人."),
        M("Which sentence tells you Monterey is small?", "蒙特雷是一个小城市，人口不多。", ["蒙特雷是加州最大的城市。", "蒙特雷在西南部。", "我们学校有很多学生。"], "小城市，人口不多."),
        M("In the order 4, 6, 2, 5, 3, 1, 7, what comes first?", "重庆是中国最大的城市。", ["四川最大的城市是成都。", "我爸爸的老家在四川。", "成都有一千六百三十多万人口。"], "Statement 4 comes first in the book’s story."),
        M("In that story, what is the last statement?", "成都有一千六百三十多万人口。", ["重庆有三千一百万人口。", "我妈妈的老家在重庆。", "四川在中国的西南部。"], "Statement 7 closes the story."),
        mean("外国", "wai4guo2", "foreign country", ["a country", "the outside", "a foreigner"]),
        mean("以前", "yi3qian2", "before, in the past", ["now", "later", "in front"]),
        F("成都是四川的省___。", "会", PART, "省会.", tr="Chengdu is the capital of Sichuan."),
        F("四川大学也有很多外___学生。", "国", PART, "外国.", tr="Sichuan University also has many foreign students."),
    ],
)

# ---------------------------------------------------------------------------- pronunciation: third tone and tanks
L_P1_PRON = lesson(
    "Pronunciation review: the third tone and tank words",
    "老家 · 老兵 · 老茧 · 老练 · 老两口儿 · 火箭炮坦克",
    requires=[],
    cards=[
        card("Practice 1: the third tone (Part A)",
             "The book groups words with a third-tone syllable first by what follows it. Read each word aloud, then listen and repeat. "
             "Remember: before another third tone the first one is said with a rising tone, so 老手 sounds like láoshǒu. The pinyin below is the written (underlying) tone.",
             tables=[wtable([("老家", "lao3jia1", "hometown (3rd + 1st)"), ("老兵", "lao3bing1", "veteran (3rd + 1st)"), ("老人", "lao3ren2", "elderly people (3rd + 2nd)"),
                             ("老实", "lao3shi5", "honest (3rd + 2nd)"), ("老手", "lao3shou3", "old hand, veteran (3rd + 3rd)"), ("老茧", "lao3jian3", "callosity (3rd + 3rd)"),
                             ("老练", "lao3lian4", "experienced, tactful (3rd + 4th)"), ("老式", "lao3shi4", "old-fashioned (3rd + 4th)"), ("领子", "ling3zi5", "collar (3rd + neutral)"),
                             ("嗓子", "sang3zi5", "throat, voice (3rd + neutral)"), ("老百姓", "lao3bai3xing4", "ordinary people, civilian (polysyllabic)"),
                             ("老年人", "lao3nian2ren2", "elderly people (polysyllabic)"), ("老两口儿", "lao3liang3kou3r5", "the elderly couple (idiomatic)"),
                             ("老实可靠", "lao3shi5ke3kao4", "honest and reliable (idiomatic)")])]),
        card("Note on 老 and -子 (from the book)",
             "老 literally means “old”, but as a prefix in words for certain people and occupations, and for certain plants and animals, its independent meaning of “old” may not apply: "
             "老师 lǎoshī (teacher), 老乡 lǎoxiāng (fellow townsman), 老鹰 lǎoyīng (eagle), 老百姓 lǎobǎixìng (ordinary people). "
             "The suffix -子 has no concrete meaning and only serves as a noun marker. It is always read in the neutral tone when used as a suffix.",
             tables=[wtable([("老师", "lao3shi1", "teacher"), ("老乡", "lao3xiang1", "fellow townsman"), ("老鹰", "lao3ying1", "eagle"), ("老百姓", "lao3bai3xing4", "ordinary people")])]),
        card("Practice 1, Part B: transcribe with tone marks",
             "The book asks you to listen to these words and write them with tone marks. Here they are with the answers.",
             tables=[wtable([("老小", "lao3xiao3", "grown-ups and children"), ("饺子", "jiao3zi5", "dumplings"), ("老大", "lao3da4", "eldest child"),
                             ("老成", "lao3cheng2", "experienced; steady"), ("老主顾", "lao3zhu3gu4", "regular customer"), ("老夫老妻", "lao3fu1lao3qi1", "an old married couple")])]),
        card("Practice 2: military terms",
             "Two photographs begin this practice: a tank formation in the troop review during the celebration of the 70th anniversary of the founding of the People’s Republic of China, "
             "and the most advanced amphibious infantry fighting vehicle independently developed by China.",
             tables=[wtable([("坦克", "tan3ke4", "tank"), ("装甲车", "zhuang1jia3che1", "armored vehicle"), ("装甲部队", "zhuang1jia3 bu4dui4", "armored unit"), ("坦克部队", "tan3ke4 bu4dui4", "tank unit"),
                             ("轻坦克", "qing1 tan3ke4", "light tank"), ("重坦克", "zhong4 tan3ke4", "heavy tank"), ("两栖坦克", "liang3qi1 tan3ke4", "amphibious tank"),
                             ("火箭炮坦克", "huo3jian4pao4 tan3ke4", "rocket-launching tank")])],
             examples=[D("坦克方队接受检阅。", "The tank formation is reviewed."),
                       D("中国自主研制的最先进两栖步战车。", "The most advanced amphibious infantry fighting vehicle independently developed by China.")]),
    ],
    exercises=[
        mean("老家", "lao3jia1", "hometown", ["an old house", "an old man", "a family"]),
        mean("老兵", "lao3bing1", "veteran", ["a new soldier", "an old man", "an officer"]),
        mean("老茧", "lao3jian3", "callosity", ["an old house", "silk", "a coat"]),
        mean("老练", "lao3lian4", "experienced, tactful", ["old-fashioned", "honest", "tired"]),
        mean("老式", "lao3shi4", "old-fashioned", ["experienced", "honest", "new"]),
        mean("老两口儿", "lao3liang3kou3r5", "the elderly couple", ["two old men", "two mouths", "a family of four"]),
        mean("老实可靠", "lao3shi5ke3kao4", "honest and reliable", ["old and tired", "experienced", "old-fashioned"]),
        mean("老小", "lao3xiao3", "grown-ups and children", ["old and small", "the youngest", "elderly people"]),
        mean("老大", "lao3da4", "eldest child", ["old and big", "a veteran", "a teacher"]),
        mean("老成", "lao3cheng2", "experienced; steady", ["a finished job", "honest", "old-fashioned"]),
        mean("老主顾", "lao3zhu3gu4", "regular customer", ["an old master", "a boss", "a teacher"]),
        mean("老夫老妻", "lao3fu1lao3qi1", "an old married couple", ["an old teacher", "two old men", "an elderly couple’s house"]),
        mean("火箭炮坦克", "huo3jian4pao4 tan3ke4", "rocket-launching tank", ["light tank", "heavy tank", "amphibious tank"]),
        mean("装甲部队", "zhuang1jia3 bu4dui4", "armored unit", ["tank unit", "an armored vehicle", "a light tank"]),
        M("What does 老 mean in 老师?", "Nothing like “old”; it is a prefix", ["old", "very", "former"], "老师 is a teacher."),
        M("How is 老手 really said?", "láoshǒu", ["lǎoshǒu", "lǎoshóu", "làoshǒu"], "Third + third becomes second + third."),
        M("What is the suffix -子 in 领子 and 嗓子?", "A noun marker in the neutral tone", ["A word for child", "A word for small", "A word for old"], "子 has no concrete meaning."),
        M("Which word is a plant or animal, not a person?", "老鹰", ["老乡", "老师", "老百姓"], "老鹰 is an eagle."),
    ],
)

# ---------------------------------------------------------------------------- vocabulary list of Presentation 1
L_P1_VOCAB = lesson(
    "Presentation 1 vocabulary and speaking tasks",
    "最 · 万 · 只有 · 少 · 百分之 · 还是 · 大城市 · 千 · 百 · 重庆 · 首都 · 李丽",
    requires=[],
    cards=[
        card("Vocabulary list (Presentation 1)",
             "The book’s list for this presentation, with the traditional form where it differs: 万 萬, 还是 還是, 重庆 重慶, 李丽 李麗.",
             tables=[wtable([("最", "zui4", "adv. the most"), ("万", "wan4", "n. ten thousand (trad. 萬)"), ("只有", "zhi3you3", "v. only have"), ("少", "shao3", "adj./adv. few, little"),
                             ("百分之", "bai3fen1zhi1", "n. percent"), ("还是", "hai2shi5", "conj. still, or (trad. 還是)"), ("大城市", "da4 cheng2shi4", "n. large city"), ("千", "qian1", "num. thousand"),
                             ("百", "bai3", "num. hundred"), ("重庆", "chong2qing4", "n. Chongqing (trad. 重慶)"), ("首都", "shou3du1", "n. capital"), ("李丽", "li3 li4", "n. a full Chinese name (trad. 李麗)")])]),
        card("Speaking tasks in the book (Using Chinese in Context)",
             "Activity 1. You are studying at the city library and a Chinese student is sitting beside you reading a book. Introduce yourself and start by talking about each other’s family and hometown. "
             "Ask for: nationality; hometown and its geographic location; the size and population of the hometown; the largest city in your country; the college, if any, and its number of students and teachers; "
             "family members and their occupations. Then report your partner’s information to the class. "
             "Activity 2. You are a student at Beijing University and the U.S. Embassy has invited you to the Annual Education Forum held in Beijing, where you will introduce American major cities to attract Chinese students. "
             "Each group researches one U.S. city: its name, geographic location, size and population, number of colleges, which college is the largest, numbers of teachers and students, and extra information. "
             "Write a profile on a flipchart, present it, and let the class vote on which city to present at the forum."),
    ],
    exercises=[
        mean("最", "zui4", "the most", ["a little", "also", "very"]),
        mean("万", "wan4", "ten thousand", ["thousand", "hundred thousand", "million"]),
        mean("只有", "zhi3you3", "only have", ["also have", "do not have", "have many"]),
        mean("少", "shao3", "few, little", ["many", "big", "old"]),
        mean("百分之", "bai3fen1zhi1", "percent", ["hundred", "a hundredth part", "one hundred people"]),
        mean("大城市", "da4 cheng2shi4", "large city", ["small city", "capital", "province"]),
        mean("千", "qian1", "thousand", ["hundred", "ten thousand", "million"]),
        mean("百", "bai3", "hundred", ["thousand", "ten", "ten thousand"]),
        mean("重庆", "chong2qing4", "Chongqing", ["Chengdu", "Beijing", "Shanghai"]),
        mean("首都", "shou3du1", "capital", ["a big city", "a state", "a base"]),
        mean("李丽", "li3 li4", "a full Chinese name", ["a city", "a province", "a university"]),
        M("What do the traditional forms 萬 and 重慶 correspond to?", "万 and 重庆", ["百 and 重庆", "万 and 首都", "千 and 少"], "萬 is 万; 重慶 is 重庆."),
    ],
)

UNIT = unit("第五课 The book’s texts: cities and population", [L_P1_DIALOG, L_P1_GRAMMAR, L_P1_READINGS, L_P1_PRON, L_P1_VOCAB])
