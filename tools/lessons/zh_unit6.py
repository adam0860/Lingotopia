"""Unit 6: family and work (lessons 48-58): 有/没有, family words, numbers 11-99 and 两, measure words and 几,
A-not-A questions, children and grandchildren, jobs, places, 在 and 哪儿, verb-object phrases, review.
Original text; the scope follows DLIFLC Chinese Basic Program Unit 1 Lesson 3 (Family), Presentations 1 and 2."""
from dsl_zh import *


# ---------------------------------------------------------------------------- 48
L48 = lesson(
    "Having: 有 and 没有",
    "我有妹妹 · 我没有哥哥 · 你有姐姐吗？",
    requires=[],
    cards=[
        card("有 means “to have”",
             "有 is the verb for having and owning: 我有妹妹, “I have a younger sister”. It is also how Chinese says “there is” or “there are”. "
             "Its negative is 没有 (méiyǒu), never 不有. In a short answer, 没有 can stand alone, and 没 is méi, in the 2nd tone. "
             "To ask a yes/no question, add 吗, as always.",
             tables=[wtable([("有", "you3", "to have"), ("没有", "mei2you3", "not to have"), ("没", "mei2", "not (before 有)"),
                             ("我有妹妹。", "wo3 you3 mei4mei5", "I have a younger sister."), ("我没有哥哥。", "wo3 mei2you3 ge1ge5", "I do not have an older brother."),
                             ("你有姐姐吗？", "ni3 you3 jie3jie5 ma5", "Do you have an older sister?")])]),
        card("Question and answer",
             "Answer with 有 for “yes” and 没有 for “no”, then add the detail if you like. 我们家 means “our family” or “our home”.",
             examples=[ex("你有弟弟吗？ 有，我有一个弟弟。", "ni3 you3 di4di5 ma5? you3, wo3 you3 yi2 ge4 di4di5", "Do you have a younger brother? Yes, I have one."),
                       ex("你有姐姐吗？ 没有，我有哥哥。", "ni3 you3 jie3jie5 ma5? mei2you3, wo3 you3 ge1ge5", "Do you have an older sister? No, I have an older brother.", hl="没有"),
                       ex("我们家有五口人。", "wo3men5 jia1 you3 wu3 kou3 ren2", "My family has five people.", hl="有"),
                       ex("他没有孩子。", "ta1 mei2you3 hai2zi5", "He has no children.", hl="没有")]),
    ],
    exercises=[
        mean("有", "you3", "to have", ["to be", "to say", "to know"]),
        mean("没有", "mei2you3", "not to have", ["not to be", "also have", "to have"]),
        rd("没有", "mei2you3", ["mei4you3", "mei2you2", "mei1you3"]),
        rd("有", "you3", ["you1", "you2", "yu3"]),
        M("What is the negative of 有?", "没有", ["不有", "不是", "没是"], "有 is negated with 没, not 不: 没有."),
        M("How do you say “I do not have an older brother”?", "我没有哥哥。", ["我不有哥哥。", "我有没哥哥。", "没我有哥哥。"], "没有 + noun."),
        M("What does 我有妹妹 mean?", "I have a younger sister.", ["I am a younger sister.", "I have an older sister.", "She has a younger sister."], "有 is have; 妹妹 is a younger sister."),
        M("What does 你有姐姐吗？ ask?", "Do you have an older sister?", ["Are you an older sister?", "What is your sister's name?", "Do you have a younger sister?"], "有 + object + 吗."),
        M("Which answers “Do you have a younger brother?” with “no”?", "没有。", ["不有。", "不对。", "没是。"], "Answer with 没有."),
        F("我___哥哥。 (I do not have)", "没有", ["不有", "不是", "没是"], "没有 negates 有.", tr="I do not have an older brother."),
        F("你___姐姐吗？", "有", ["吗", "们", "呢"], "有 is to have.", tr="Do you have an older sister?"),
        F("我们家___五口人。", "有", ["吗", "们", "呢"], "我们家有五口人: my family has five people.", tr="My family has five people."),
        F("你有弟弟___？", "吗", ["呢", "什么", "们"], "吗 makes the yes/no question.", tr="Do you have a younger brother?"),
        M("How do you say “He has no children”?", "他没有孩子。", ["他不有孩子。", "他有没孩子。", "他是没有孩子。"], "没有 + noun."),
    ],
)

# ---------------------------------------------------------------------------- 49
L49 = lesson(
    "Family members",
    "爷爷, 奶奶, 哥哥, 姐姐, 弟弟, 妹妹",
    requires=[],
    cards=[
        card("Older and younger",
             "Chinese has separate words for older and younger siblings, so you always say which one you mean: 哥哥 is an older brother and 弟弟 a younger brother, "
             "姐姐 an older sister and 妹妹 a younger sister. 兄弟姐妹 gathers them all: “brothers and sisters”, siblings. "
             "爷爷 and 奶奶 are your father's father and mother, and they are the words people use at home. In each of these words the second syllable is neutral, except in 兄弟姐妹.",
             tables=[wtable([("爷爷", "ye2ye5", "grandfather (father's side)"), ("奶奶", "nai3nai5", "grandmother (father's side)"), ("爸爸", "ba4ba5", "dad"), ("妈妈", "ma1ma5", "mum"),
                             ("哥哥", "ge1ge5", "older brother"), ("姐姐", "jie3jie5", "older sister"), ("弟弟", "di4di5", "younger brother"), ("妹妹", "mei4mei5", "younger sister"),
                             ("兄弟姐妹", "xiong1di4 jie3mei4", "siblings")])]),
        card("Birth order and family photos",
             "To say which older sibling, put 大 (eldest), 二 (second) or 三 (third) before the word: 大哥 is the eldest brother, 二姐 the second older sister. "
             "To show a photo, say 你看, “look”, and use 照片, which means a photo, and 家, which means family or home.",
             tables=[wtable([("大哥", "da4ge1", "eldest brother"), ("二哥", "er4ge1", "second older brother"), ("大姐", "da4jie3", "eldest sister"), ("二姐", "er4jie3", "second older sister"),
                             ("照片", "zhao4pian4", "a photo"), ("看", "kan4", "to look, to watch"), ("家", "jia1", "a family, a home")])]),
        card("In a conversation",
             "Here is how it sounds when someone shows a family photo.",
             examples=[ex("你看，这是我们家的照片。", "ni3 kan4, zhe4 shi4 wo3men5 jia1 de5 zhao4pian4", "Look, this is a photo of our family."),
                       ex("这是你哥哥吗？ 不是，这是我弟弟。", "zhe4 shi4 ni3 ge1ge5 ma5? bu2shi4, zhe4 shi4 wo3 di4di5", "Is this your older brother? No, this is my younger brother."),
                       ex("这是你大姐吗？ 不是，这是我二姐。", "zhe4 shi4 ni3 da4jie3 ma5? bu2shi4, zhe4 shi4 wo3 er4jie3", "Is this your eldest sister? No, this is my second sister.")]),
    ],
    exercises=[
        mean("哥哥", "ge1ge5", "older brother", ["younger brother", "older sister", "younger sister"]),
        mean("弟弟", "di4di5", "younger brother", ["older brother", "younger sister", "older sister"]),
        mean("姐姐", "jie3jie5", "older sister", ["younger sister", "older brother", "mother"]),
        mean("妹妹", "mei4mei5", "younger sister", ["older sister", "younger brother", "daughter"]),
        mean("爷爷", "ye2ye5", "grandfather (father's side)", ["father", "older brother", "grandmother (father's side)"]),
        mean("奶奶", "nai3nai5", "grandmother (father's side)", ["mother", "older sister", "grandfather (father's side)"]),
        mean("兄弟姐妹", "xiong1di4 jie3mei4", "siblings", ["parents", "classmates", "cousins"]),
        mean("大姐", "da4jie3", "eldest sister", ["eldest brother", "second older sister", "younger sister"]),
        mean("二哥", "er4ge1", "second older brother", ["eldest brother", "second older sister", "younger brother"]),
        mean("照片", "zhao4pian4", "a photo", ["a family", "a phone", "a classmate"]),
        rd("哥哥", "ge1ge5", ["ge2ge5", "ge4ge5", "ge3ge5"]),
        rd("弟弟", "di4di5", ["di1di5", "di2di5", "di3di5"]),
        rd("奶奶", "nai3nai5", ["nai4nai5", "nai2nai5", "nai1nai5"]),
        rd("爷爷", "ye2ye5", ["ye4ye5", "ye1ye5", "ye3ye5"]),
        rd("兄弟姐妹", "xiong1di4 jie3mei4", ["xiong2di4 jie3mei4", "xiong1di4 jie3mei2", "xiong1di4 jie2mei4"]),
        M("Which word is an older sister?", "姐姐", ["妹妹", "弟弟", "哥哥"], "姐 is older sister; 妹 is younger."),
        M("What does 大 mean in 大哥?", "Eldest", ["Big house", "Very", "Younger"], "大哥 is the eldest brother."),
        F("这是我___。 (younger brother)", "弟弟", ["哥哥", "姐姐", "爷爷"], "弟弟 is a younger brother.", tr="This is my younger brother."),
        F("你___，这是我们家的照片。", "看", ["有", "是", "吗"], "你看 means “look”.", tr="Look, this is a photo of our family."),
    ],
)

# ---------------------------------------------------------------------------- 50
L50 = lesson(
    "Numbers 11 to 99, and 二 against 两",
    "十一, 二十, 三十五 · 两个",
    requires=[],
    cards=[
        card("Building the tens",
             "Numbers above ten are built like a sum. 十一 is “ten-one” (11), 十二 is “ten-two” (12), and so on up to 十九. "
             "Twenty is 二十, “two-ten”, and 二十一 is “two-ten-one” (21). 三十五 is “three-ten-five” (35). The same pattern runs to 九十九.",
             tables=[wtable([("十一", "shi2yi1", "11"), ("十二", "shi2er4", "12"), ("十五", "shi2wu3", "15"), ("二十", "er4shi2", "20"), ("二十一", "er4shi2yi1", "21"),
                             ("三十五", "san1shi2wu3", "35"), ("四十八", "si4shi2ba1", "48"), ("六十九", "liu4shi2jiu3", "69"), ("九十九", "jiu3shi2jiu3", "99")])]),
        card("二 and 两",
             "Both mean “two”. Use 二 for counting, for digits and for the number itself: 一、二、三, 十二, 二十. "
             "Use 两 before a measure word or a noun, to say how many: 两个姐姐 is “two older sisters”. You do not say 二个. "
             "In the word 二哥 the 二 is a position in the family, not a quantity, so it stays 二.",
             examples=[ex("二十二岁", "er4shi2er4 sui4", "twenty-two years old", hl="二"),
                       ex("我有两个姐姐。", "wo3 you3 liang3 ge4 jie3jie5", "I have two older sisters.", hl="两"),
                       ex("我们家有两口人。", "wo3men5 jia1 you3 liang3 kou3 ren2", "There are two people in our family.", hl="两"),
                       ex("这是我二哥。", "zhe4 shi4 wo3 er4ge1", "This is my second older brother.", hl="二")]),
    ],
    exercises=[
        M("What number is 十五?", "15", ["50", "5", "105"], "十 + 五 = 15."),
        M("What number is 二十?", "20", ["12", "2", "22"], "二 + 十 = twenty."),
        M("What number is 三十五?", "35", ["53", "30", "25"], "三十五 is three tens and five."),
        M("What number is 四十八?", "48", ["84", "40", "38"], "Four tens and eight."),
        M("What number is 九十九?", "99", ["19", "90", "89"], "Nine tens and nine."),
        M("How do you say 12?", "十二", ["二十", "二十一", "一二"], "十 + 二."),
        M("How do you say 21?", "二十一", ["十二", "二十", "一十二"], "二十 + 一."),
        M("How do you say 69?", "六十九", ["九十六", "六十", "十六九"], "Six tens and nine."),
        rd("十二", "shi2er4", ["shi4er4", "shi2er2", "shi2er3"]),
        rd("三十五", "san1shi2wu3", ["san1shi4wu3", "san1shi2wu4", "san3shi2wu3"]),
        rd("九十九", "jiu3shi2jiu3", ["jiu3shi2jiu4", "jiu3shi4jiu3", "jiu2shi2jiu3"]),
        M("Which is correct for “two older sisters”?", "两个姐姐", ["二个姐姐", "两姐姐", "二姐姐们"], "Use 两 before a measure word."),
        M("Which is correct for “two people in the family”?", "两口人", ["二口人", "两人口", "二人口"], "两 + measure word + noun."),
        M("Why is 二姐 not 两姐?", "二 shows position in the family", ["两 is rude", "二 is a measure word", "It is a mistake"], "二姐 is “second older sister”: a position, not a quantity."),
        F("我有___个姐姐。 (two)", "两", ["二", "吗", "们"], "两 comes before the measure word 个.", tr="I have two older sisters."),
        F("我今年二十___岁。 (two)", "二", ["两", "吗", "们"], "二 in a digit.", tr="I am 22 years old."),
    ],
)

# ---------------------------------------------------------------------------- 51
L51 = lesson(
    "Measure words and 几",
    "一个, 五口, 三位 · 几口人？",
    requires=[],
    cards=[
        card("A measure word between number and noun",
             "In Chinese a number or 这/那 cannot sit directly in front of a noun: a measure word goes between them, like “a slice of bread” in English. "
             "Every noun has its own measure word, so learn them together. Three are enough for now: "
             "个 is the general one (一个哥哥), 口 counts the members of a family (五口人) and 位 counts people respectfully (三位老师).",
             tables=[wtable([("个", "ge4", "(general measure word)"), ("口", "kou3", "(measure word for family members)"), ("位", "wei4", "(respectful measure word for people)"),
                             ("一个弟弟", "yi2 ge4 di4di5", "one younger brother"), ("五口人", "wu3 kou3 ren2", "five people (in a family)"), ("三位老师", "san1 wei4 lao3shi1", "three teachers"),
                             ("这个学生", "zhe4 ge4 xue2sheng5", "this student"), ("那位老师", "na4 wei4 lao3shi1", "that teacher")])]),
        card("几 asks “how many?”",
             "几 asks for a number, usually from one to nine, and it takes a measure word too: 你有几个姐姐？ The answer simply takes the place of 几. "
             "For a number that could be larger than ten, use 多少.",
             examples=[ex("你们家有几口人？", "ni3men5 jia1 you3 ji3 kou3 ren2", "How many people are there in your family?", hl="几口"),
                       ex("我们家有七口人。", "wo3men5 jia1 you3 qi1 kou3 ren2", "There are seven in our family.", hl="七口"),
                       ex("你有几个姐姐？ 我有两个。", "ni3 you3 ji3 ge4 jie3jie5? wo3 you3 liang3 ge4", "How many older sisters do you have? I have two."),
                       ex("你们班有几位老师？", "ni3men5 ban1 you3 ji3 wei4 lao3shi1", "How many teachers does your class have?")]),
    ],
    exercises=[
        mean("个", "ge4", "(general measure word)", ["(family measure word)", "(respectful measure word)", "very"]),
        mean("口", "kou3", "(measure word for family members)", ["(general measure word)", "(respectful measure word)", "also"]),
        mean("几", "ji3", "how many (usually 1-9)", ["how many (any number)", "what", "which"]),
        rd("几", "ji3", ["ji2", "ji4", "ju3"]),
        rd("口", "kou3", ["kou1", "kou2", "kou4"]),
        M("Where does the measure word go?", "Between the number and the noun", ["After the noun", "Before the number", "It is not needed"], "Number + measure word + noun."),
        M("Which measure word counts members of a family?", "口", ["位", "个", "吗"], "五口人: five in a family."),
        M("Which measure word is respectful, for people?", "位", ["口", "个", "们"], "三位老师."),
        M("Which is the most general measure word?", "个", ["口", "位", "们"], "个 works for most nouns."),
        M("How do you say “three teachers” respectfully?", "三位老师", ["三个口老师", "三老师位", "三们老师"], "Number + 位 + noun."),
        M("How do you say “five people in a family”?", "五口人", ["五人口", "五位口", "口五人"], "五 + 口 + 人."),
        F("我们家有五___人。", "口", ["位", "吗", "们"], "口 counts family members.", tr="There are five people in our family."),
        F("我有两___姐姐。", "个", ["口", "吗", "们"], "个 is the general measure word.", tr="I have two older sisters."),
        F("那___老师姓王。", "位", ["口", "吗", "们"], "那位 is the respectful “that person”.", tr="That teacher is surnamed Wang."),
        F("你们家有___口人？", "几", ["什么", "谁", "哪"], "几 asks how many.", tr="How many people are there in your family?"),
        M("When do you use 多少 instead of 几?", "When the number could be larger than ten", ["For names", "For people only", "For places"], "几 is usually for 1-9."),
    ],
)

# ---------------------------------------------------------------------------- 52
L52 = lesson(
    "Either-or questions: 有没有, 是不是",
    "你有没有兄弟姐妹？ 这是不是你哥哥？",
    requires=[],
    cards=[
        card("Verb + not + verb",
             "Besides 吗, there is another yes/no question: put the verb or adjective and its negative side by side. 你有兄弟姐妹吗？ becomes 你有没有兄弟姐妹？ "
             "and 这是你哥哥吗？ becomes 这是不是你哥哥？ It is like “Do you have siblings or not?” and can sound a little more direct than 吗. "
             "The 不 in the middle is unstressed, in the neutral tone, and with 有 the negative is 没有.",
             tables=[wtable([("你有没有姐姐？", "ni3 you3 mei2 you3 jie3jie5", "Do you have an older sister (or not)?"), ("这是不是你哥哥？", "zhe4 shi4 bu5 shi4 ni3 ge1ge5", "Is this your older brother (or not)?"),
                             ("你高兴不高兴？", "ni3 gao1xing4 bu5 gao1xing4", "Are you happy (or not)?"), ("你看不看？", "ni3 kan4 bu5 kan4", "Do you look at it (or not)?")])]),
        card("Answering",
             "You answer exactly as you would a 吗 question: repeat the verb, or say 不 plus the verb. An answer with 有 or 是 does not repeat the question; it answers it.",
             examples=[ex("你有没有姐姐？ 有，我有两个姐姐。", "ni3 you3 mei2 you3 jie3jie5? you3, wo3 you3 liang3 ge4 jie3jie5", "Do you have older sisters? Yes, I have two."),
                       ex("这是不是你哥哥？ 不是，这是我弟弟。", "zhe4 shi4 bu5 shi4 ni3 ge1ge5? bu2shi4, zhe4 shi4 wo3 di4di5", "Is this your older brother? No, it is my younger brother."),
                       ex("那位是不是老师？ 不是，他是我们的班长。", "na4 wei4 shi4 bu5 shi4 lao3shi1? bu2shi4, ta1 shi4 wo3men5 de5 ban1zhang3", "Is that person a teacher? No, he is our class leader.")]),
    ],
    exercises=[
        M("How do you turn 你有姐姐吗？ into a verb + not + verb question?", "你有没有姐姐？", ["你有姐姐没有？", "你不有姐姐？", "你有不有姐姐？"], "With 有 the negative is 没有: 有没有."),
        M("How do you turn 这是你哥哥吗？ into a verb + not + verb question?", "这是不是你哥哥？", ["这是你哥哥是不是？", "这不是你哥哥吗？", "这是你不是哥哥？"], "是不是 goes where 是 was."),
        M("How do you turn 你高兴吗？ into a verb + not + verb question?", "你高兴不高兴？", ["你不高兴吗？", "你高兴高兴？", "你高兴吗不高兴？"], "Adjective + 不 + adjective."),
        M("Which is the verb + not + verb question for “Do you speak Chinese?”", "你说不说中文？", ["你说中文不说？", "你不说中文？", "你说吗中文？"], "说不说 + object."),
        M("How is the 不 in 是不是 pronounced?", "Neutral tone", ["4th tone", "2nd tone", "1st tone"], "The middle 不 is unstressed."),
        M("A good “yes” answer to 你有没有兄弟姐妹？ is…", "有。", ["是。", "对。", "好。"], "Repeat 有."),
        M("A good “no” answer to 这是不是你哥哥？ is…", "不是。", ["没有。", "不有。", "没是。"], "不是 negates 是."),
        F("你有___有姐姐？", "没", ["不", "吗", "们"], "有没有 is the verb + not + verb form of 有.", tr="Do you have an older sister?"),
        F("这是___是你哥哥？", "不", ["没", "吗", "们"], "是不是.", tr="Is this your older brother?"),
        F("你高兴___高兴？", "不", ["没", "吗", "们"], "高兴不高兴.", tr="Are you happy?"),
        F("你看___看？", "不", ["没", "吗", "们"], "看不看.", tr="Do you look at it?"),
        rd("没有", "mei2you3", ["mei4you3", "mei2you2", "mei1you3"]),
        M("Compared with a 吗 question, a verb + not + verb question…", "Can sound a little more direct", ["Is rude", "Is only for older people", "Cannot be answered with 有"], "It can sound stronger."),
        M("Which question cannot be right?", "你有没有姐姐吗？", ["你有没有姐姐？", "你有姐姐吗？", "这是不是你哥哥？"], "Do not use 吗 and verb + not + verb together."),
    ],
)

# ---------------------------------------------------------------------------- 53
L53 = lesson(
    "Children and grandchildren",
    "孩子, 儿子, 女儿, 孙子, 外孙女",
    requires=[],
    cards=[
        card("Your children and theirs",
             "孩子 is a child or children. 儿子 is a son and 女儿 a daughter. For grandchildren, Chinese separates your son's children from your daughter's: "
             "your son's are 孙子 (grandson) and 孙女 (granddaughter), and your daughter's are 外孙 and 外孙女, where 外 means “outside”. "
             "女儿 is written nǚ'ér, with an apostrophe because the second syllable begins with a vowel.",
             tables=[wtable([("孩子", "hai2zi5", "a child, children"), ("儿子", "er2zi5", "a son"), ("女儿", "nv3'er2", "a daughter"), ("孙子", "sun1zi5", "a grandson (son's son)"),
                             ("孙女", "sun1nv3", "a granddaughter (son's daughter)"), ("外孙女", "wai4sun1nv3", "a granddaughter (daughter's daughter)"),
                             ("外", "wai4", "outside, foreign")])]),
        card("Talking to an older person",
             "大爷 (and the warmer 老大爷) is a respectful way to speak to an older man. 身体 is the body or your health, 真 means “really”, and 可爱 means cute. "
             "Complimenting someone's health is a polite thing to do.",
             tables=[wtable([("大爷", "da4ye5", "sir (to an older man)"), ("老大爷", "lao3 da4ye5", "grandpa (to an older man)"), ("身体", "shen1ti3", "body, health"),
                             ("真", "zhen1", "really"), ("可爱", "ke3'ai4", "cute")]),
                     ],
             examples=[ex("大爷，您身体真好！", "da4ye5, nin2 shen1ti3 zhen1 hao3", "Sir, your health is really good!"),
                       ex("您有几个孩子？ 两个，一个儿子，一个女儿。", "nin2 you3 ji3 ge4 hai2zi5? liang3 ge4, yi2 ge4 er2zi5, yi2 ge4 nv3'er2", "How many children do you have? Two, a son and a daughter."),
                       ex("你看，这是我孙子，这是我外孙女。", "ni3 kan4, zhe4 shi4 wo3 sun1zi5, zhe4 shi4 wo3 wai4sun1nv3", "Look, this is my grandson and this is my granddaughter (my daughter's daughter)."),
                       ex("你的孩子真可爱！", "ni3 de5 hai2zi5 zhen1 ke3'ai4", "Your child is really cute!")]),
    ],
    exercises=[
        mean("孩子", "hai2zi5", "a child, children", ["a son", "a daughter", "a classmate"]),
        mean("儿子", "er2zi5", "a son", ["a daughter", "a child", "a grandson"]),
        mean("女儿", "nv3'er2", "a daughter", ["a son", "a child", "a granddaughter"]),
        mean("孙子", "sun1zi5", "a grandson (son's son)", ["a son", "a daughter's son", "a younger brother"]),
        mean("外孙女", "wai4sun1nv3", "a granddaughter (daughter's daughter)", ["a granddaughter (son's daughter)", "a daughter", "a grandmother"]),
        mean("身体", "shen1ti3", "body, health", ["a family", "a hospital", "a name"]),
        mean("真", "zhen1", "really", ["very", "also", "not"]),
        mean("可爱", "ke3'ai4", "cute", ["happy", "busy", "big"]),
        rd("孩子", "hai2zi5", ["hai4zi5", "hai2zi3", "hai1zi5"]),
        rd("儿子", "er2zi5", ["er4zi5", "er2zi3", "er3zi5"]),
        rd("女儿", "nv3'er2", ["nv3'er4", "nv4'er2", "nv2'er2"]),
        rd("身体", "shen1ti3", ["shen2ti3", "shen1ti1", "shen1ti4"]),
        M("What does 外 add to 外孙女?", "She is your daughter's child", ["She is foreign", "She is older", "She is your son's child"], "外孙 are your daughter's children; 孙 your son's."),
        M("What do you call a granddaughter on your son's side?", "孙女", ["外孙女", "女儿", "妹妹"], "孙女 is son's daughter."),
        M("How do you politely greet an older man?", "大爷，您好！", ["弟弟，你好！", "孩子，你好！", "同学，你好！"], "大爷 is a respectful address."),
        M("How do you ask “How many children do you have?”", "您有几个孩子？", ["您有什么孩子？", "您是几个孩子？", "您有孩子几个？"], "几 + measure word + noun."),
        F("我有两个孩子，一个儿子，一个___。", "女儿", ["孙子", "妹妹", "弟弟"], "女儿 is a daughter.", tr="I have two children, a son and a daughter."),
        F("大爷，您身体___好！", "真", ["吗", "也", "是"], "真好: really good.", tr="Sir, your health is really good!"),
    ],
)

# ---------------------------------------------------------------------------- 54
L54 = lesson(
    "Jobs",
    "做什么工作？ 医生, 工程师, 老师, 教官",
    requires=[],
    cards=[
        card("What do you do?",
             "To ask someone's job, say 做什么工作？, literally “do what work?”. 做 means to do and 工作 means work or a job. "
             "To answer, use 是 and the job: 我是医生. 教官 is an instructor, especially in a military school. 家庭主妇 is a homemaker. "
             "A 大学生 is a college student and a 中学生 is a middle-school student.",
             tables=[wtable([("做", "zuo4", "to do"), ("工作", "gong1zuo4", "work, a job; to work"), ("医生", "yi1sheng1", "a doctor"), ("工程师", "gong1cheng2shi1", "an engineer"),
                             ("老师", "lao3shi1", "a teacher"), ("教官", "jiao4guan1", "an instructor"), ("军官", "jun1guan1", "an officer"), ("家庭主妇", "jia1ting2 zhu3fu4", "a homemaker"),
                             ("大学生", "da4xue2sheng5", "a college student"), ("中学生", "zhong1xue2sheng5", "a middle-school student"), ("司机", "si1ji1", "a driver"),
                             ("工人", "gong1ren2", "a worker"), ("护士", "hu4shi5", "a nurse")])]),
        card("Asking and answering",
             "Asking about a relative uses the same pattern.",
             examples=[ex("你父亲做什么工作？", "ni3 fu4qin1 zuo4 shen2me5 gong1zuo4", "What does your father do?", hl="做什么工作"),
                       ex("他是军校教官。", "ta1 shi4 jun1xiao4 jiao4guan1", "He is an instructor at a military school.", hl="教官"),
                       ex("你母亲呢？ 她是家庭主妇。", "ni3 mu3qin1 ne5? ta1 shi4 jia1ting2 zhu3fu4", "And your mother? She is a homemaker."),
                       ex("我大哥是医生，二哥是工程师。", "wo3 da4ge1 shi4 yi1sheng1, er4ge1 shi4 gong1cheng2shi1", "My eldest brother is a doctor and my second brother is an engineer.")]),
    ],
    exercises=[
        mean("医生", "yi1sheng1", "a doctor", ["a nurse", "a teacher", "an engineer"]),
        mean("工程师", "gong1cheng2shi1", "an engineer", ["a doctor", "a driver", "a teacher"]),
        mean("教官", "jiao4guan1", "an instructor", ["a student", "an engineer", "a doctor"]),
        mean("家庭主妇", "jia1ting2 zhu3fu4", "a homemaker", ["a nurse", "a student", "a teacher"]),
        mean("大学生", "da4xue2sheng5", "a college student", ["a middle-school student", "a teacher", "a driver"]),
        mean("司机", "si1ji1", "a driver", ["a worker", "a nurse", "a doctor"]),
        mean("护士", "hu4shi5", "a nurse", ["a doctor", "a worker", "a driver"]),
        mean("工作", "gong1zuo4", "work, a job; to work", ["to teach", "to speak", "to ask"]),
        rd("医生", "yi1sheng1", ["yi2sheng1", "yi1sheng2", "yi4sheng1"]),
        rd("工程师", "gong1cheng2shi1", ["gong1cheng4shi1", "gong1cheng2shi4", "gong3cheng2shi1"]),
        rd("教官", "jiao4guan1", ["jiao3guan1", "jiao4guan3", "jiao4guan4"]),
        rd("工作", "gong1zuo4", ["gong2zuo4", "gong1zuo2", "gong1zuo1"]),
        M("How do you ask “What does your father do?”", "你父亲做什么工作？", ["你父亲是什么工作？", "你父亲做谁工作？", "你父亲什么做工作？"], "做 + 什么 + 工作."),
        M("How do you answer “He is a doctor”?", "他是医生。", ["他做医生吗。", "他有医生。", "他是什么。"], "是 + job."),
        F("你父亲做什么___？", "工作", ["医生", "教官", "大学生"], "做什么工作 asks the job.", tr="What does your father do?"),
        F("我大哥是___，他在医院工作。 (doctor)", "医生", ["教官", "司机", "学生"], "医生 is a doctor.", tr="My eldest brother is a doctor."),
        F("她是家庭主妇，她不___。 (work)", "工作", ["医生", "教官", "好"], "不工作: does not work.", tr="She is a homemaker; she does not work."),
    ],
)

# ---------------------------------------------------------------------------- 55
L55 = lesson(
    "Places of work and study",
    "医院, 公司, 学校, 军校, 学院",
    requires=[],
    cards=[
        card("Where people work and study",
             "医院 is a hospital and 公司 is a company. 学校 is a school. 军校 is a military school, short for 军事学校. "
             "中学 is a middle or high school, 大学 is a university and 学院 is a college or institute, as in 空军学院, an air force academy. "
             "In these words 学 means study and 校 means school.",
             tables=[wtable([("医院", "yi1yuan4", "a hospital"), ("公司", "gong1si1", "a company"), ("电脑公司", "dian4nao3 gong1si1", "a computer company"),
                             ("学校", "xue2xiao4", "a school"), ("军校", "jun1xiao4", "a military school"), ("中学", "zhong1xue2", "a middle or high school"),
                             ("大学", "da4xue2", "a university"), ("学院", "xue2yuan4", "a college, an institute"), ("空军学院", "kong1jun1 xue2yuan4", "an air force academy")])]),
        card("Who works where",
             "Jobs and places match up in a typical family.",
             examples=[ex("我大哥是医生，他在医院工作。", "wo3 da4ge1 shi4 yi1sheng1, ta1 zai4 yi1yuan4 gong1zuo4", "My eldest brother is a doctor; he works in a hospital."),
                       ex("我二哥是工程师，他在电脑公司工作。", "wo3 er4ge1 shi4 gong1cheng2shi1, ta1 zai4 dian4nao3 gong1si1 gong1zuo4", "My second brother is an engineer; he works at a computer company."),
                       ex("我姐姐是老师，她在中学工作。", "wo3 jie3jie5 shi4 lao3shi1, ta1 zai4 zhong1xue2 gong1zuo4", "My older sister is a teacher; she works at a middle school.")]),
    ],
    exercises=[
        mean("医院", "yi1yuan4", "a hospital", ["a company", "a school", "a college"]),
        mean("公司", "gong1si1", "a company", ["a hospital", "a school", "a family"]),
        mean("学校", "xue2xiao4", "a school", ["a hospital", "a company", "a college"]),
        mean("军校", "jun1xiao4", "a military school", ["a university", "a hospital", "a company"]),
        mean("中学", "zhong1xue2", "a middle or high school", ["a university", "a hospital", "an academy"]),
        mean("大学", "da4xue2", "a university", ["a middle school", "a hospital", "a company"]),
        mean("学院", "xue2yuan4", "a college, an institute", ["a hospital", "a company", "a classmate"]),
        mean("空军学院", "kong1jun1 xue2yuan4", "an air force academy", ["a hospital", "a computer company", "a middle school"]),
        rd("医院", "yi1yuan4", ["yi1yuan2", "yi2yuan4", "yi1yuan3"]),
        rd("公司", "gong1si1", ["gong1si4", "gong2si1", "gong1si2"]),
        rd("学校", "xue2xiao4", ["xue2xiao1", "xue4xiao4", "xue2xiao2"]),
        rd("大学", "da4xue2", ["da4xue4", "da2xue2", "da4xue1"]),
        M("A doctor usually works in a…", "医院", ["公司", "中学", "军校"], "医生 work in a 医院."),
        M("An engineer at a computer company works in a…", "公司", ["医院", "中学", "大学"], "电脑公司 is a computer company."),
        M("Which character means “school” in 学校 and 军校?", "校", ["学", "军", "医"], "校 is school."),
        F("我二哥在电脑___工作。", "公司", ["吗", "们", "呢"], "公司 is a company.", tr="My second brother works at a computer company."),
        F("我姐姐在___工作，她是医生。", "医院", ["吗", "们", "呢"], "医院 is a hospital.", tr="My sister works in a hospital; she is a doctor."),
    ],
)

# ---------------------------------------------------------------------------- 56
L56 = lesson(
    "At a place: 在 and 哪儿",
    "他在医院工作 · 你在哪儿工作？",
    requires=[],
    cards=[
        card("在 puts the place before the verb",
             "在 means “at” or “in”. The place phrase comes before the verb in Chinese, where English puts it after: 他在医院工作 is “he at-hospital works”. "
             "The pattern is Subject + 在 + place + verb. 在 is also a verb by itself, “to be at”, as in 老师在家, “the teacher is at home”.",
             tables=[wtable([("在", "zai4", "at, in; to be at"), ("在医院工作", "zai4 yi1yuan4 gong1zuo4", "to work at a hospital"), ("在家", "zai4 jia1", "at home"),
                             ("在学校", "zai4 xue2xiao4", "at school"), ("在美国", "zai4 Mei3guo2", "in America")])]),
        card("哪儿 means “where”",
             "哪儿 asks for a place. It is written nǎ'er in pinyin and said nǎr: the 儿 is a small “r” sound added to the end of the syllable. "
             "As always, the question word sits in the place the answer will go.",
             examples=[ex("你在哪儿工作？", "ni3 zai4 na3'er5 gong1zuo4", "Where do you work?", hl="哪儿"),
                       ex("我在医院工作。", "wo3 zai4 yi1yuan4 gong1zuo4", "I work at a hospital.", hl="医院"),
                       ex("你弟弟在哪儿上大学？", "ni3 di4di5 zai4 na3'er5 shang4 da4xue2", "Where does your younger brother go to college?"),
                       ex("他在空军学院上大学。", "ta1 zai4 kong1jun1 xue2yuan4 shang4 da4xue2", "He goes to the Air Force Academy."),
                       ex("老师在哪儿？ 老师在家。", "lao3shi1 zai4 na3'er5? lao3shi1 zai4 jia1", "Where is the teacher? The teacher is at home.")]),
    ],
    exercises=[
        mean("在", "zai4", "at, in; to be at", ["to have", "to teach", "also"]),
        mean("哪儿", "na3'er5", "where", ["who", "what", "which country"]),
        rd("在", "zai4", ["zai1", "zai2", "zai3"]),
        M("Where does the place phrase go in a Chinese sentence?", "Before the verb", ["After the verb", "At the very end", "Before the subject"], "Subject + 在 + place + verb."),
        M("How do you say “He works at a hospital”?", "他在医院工作。", ["他工作在医院。", "他医院在工作。", "在他医院工作。"], "在 + place + verb."),
        M("How do you ask “Where do you work?”", "你在哪儿工作？", ["你工作在哪儿？", "你哪儿在工作？", "在你哪儿工作？"], "哪儿 takes the place of the answer."),
        M("How do you ask “Where is the teacher?”", "老师在哪儿？", ["老师是哪儿？", "哪儿老师在？", "老师有哪儿？"], "在 here is a verb: to be at."),
        M("How do you say “My sister teaches in a middle school”?", "我姐姐在中学教书。", ["我姐姐教书在中学。", "我姐姐中学在教书。", "在我姐姐中学教书。"], "在 + place + verb phrase."),
        M("How is 哪儿 said aloud?", "Like nǎr", ["Like nàr", "Like něn", "Like nā'er in two beats"], "The 儿 adds an r sound to the syllable."),
        F("他___医院工作。", "在", ["有", "是", "很"], "在 + place.", tr="He works at a hospital."),
        F("你在___工作？", "哪儿", ["什么", "谁", "几"], "哪儿 asks where.", tr="Where do you work?"),
        F("他在空军学院上___。", "大学", ["医院", "公司", "照片"], "上大学: to go to college.", tr="He goes to college at the Air Force Academy."),
        F("老师在___？ 老师在家。", "哪儿", ["什么", "谁", "几"], "哪儿 asks where.", tr="Where is the teacher?"),
        F("我在美国___。 (work)", "工作", ["在", "有", "是"], "在美国工作: work in America.", tr="I work in America."),
    ],
)

# ---------------------------------------------------------------------------- 57
L57 = lesson(
    "Verb + object phrases",
    "教书, 上课, 说话, 吃饭, 看书",
    requires=[],
    cards=[
        card("Common verb + object pairs",
             "Many everyday actions in Chinese are a verb with its own object, and the pair often translates into a single English verb. "
             "教书 is “teach books” and means to teach. 吃饭 is “eat rice” and means to eat. 说话 is “speak words”, to talk. 上课 means to have a class, and 上大学 is to go to college. "
             "With an object in the pair you can still add a more specific object: 教英文, 说中文.",
             tables=[wtable([("教书", "jiao1shu1", "to teach"), ("教英文", "jiao1 Ying1wen2", "to teach English"), ("说话", "shuo1hua4", "to talk"), ("说中文", "shuo1 Zhong1wen2", "to speak Chinese"),
                             ("上课", "shang4ke4", "to have a class"), ("上大学", "shang4 da4xue2", "to go to college"), ("吃饭", "chi1fan4", "to eat"),
                             ("看书", "kan4shu1", "to read, to look at a book"), ("看照片", "kan4 zhao4pian4", "to look at photos"), ("学中文", "xue2 Zhong1wen2", "to study Chinese")])]),
        card("Combining with 在",
             "Put 在 and a place before the whole phrase.",
             examples=[ex("我姐姐在中学教书。", "wo3 jie3jie5 zai4 zhong1xue2 jiao1shu1", "My older sister teaches at a middle school."),
                       ex("她教什么？ 教英文。", "ta1 jiao1 shen2me5? jiao1 Ying1wen2", "What does she teach? English."),
                       ex("我在大学学中文。", "wo3 zai4 da4xue2 xue2 Zhong1wen2", "I study Chinese at college."),
                       ex("我们在家吃饭。", "wo3men5 zai4 jia1 chi1fan4", "We eat at home.")]),
    ],
    exercises=[
        mean("教书", "jiao1shu1", "to teach", ["to read", "to speak", "to study"]),
        mean("说话", "shuo1hua4", "to talk", ["to teach", "to eat", "to study"]),
        mean("吃饭", "chi1fan4", "to eat", ["to talk", "to read", "to teach"]),
        mean("看书", "kan4shu1", "to read, to look at a book", ["to eat", "to teach", "to work"]),
        mean("上课", "shang4ke4", "to have a class", ["to teach", "to read", "to eat"]),
        mean("上大学", "shang4 da4xue2", "to go to college", ["to work at a company", "to teach", "to eat"]),
        mean("学中文", "xue2 Zhong1wen2", "to study Chinese", ["to speak Chinese", "to teach Chinese", "to read Chinese"]),
        rd("教书", "jiao1shu1", ["jiao4shu1", "jiao1shu2", "jiao2shu1"]),
        rd("吃饭", "chi1fan4", ["chi2fan4", "chi1fan2", "chi4fan4"]),
        rd("说话", "shuo1hua4", ["shuo2hua4", "shuo1hua2", "shuo1hua1"]),
        rd("看书", "kan4shu1", ["kan1shu1", "kan4shu2", "kan3shu1"]),
        M("What does 教英文 mean?", "to teach English", ["to study English", "to speak English", "to read English"], "教 is to teach."),
        M("How do you say “She works at a hospital”?", "她在医院工作。", ["她工作在医院。", "她医院在工作。", "她在工作医院。"], "在 + place + verb."),
        M("How do you say “My sister teaches in a middle school”?", "我姐姐在中学教书。", ["我姐姐教书在中学。", "我姐姐在教书中学。", "我姐姐中学教书在。"], "在 + place + verb phrase."),
        F("我姐姐在中学___。 (teaches)", "教书", ["吃饭", "看书", "上课"], "教书 is to teach.", tr="My older sister teaches at a middle school."),
        F("我们在家___。 (eat)", "吃饭", ["教书", "上课", "工作"], "吃饭 is to eat.", tr="We eat at home."),
        F("她教什么？ 教___。 (English)", "英文", ["医院", "公司", "看书"], "教英文: teach English.", tr="What does she teach? English."),
    ],
)

# ---------------------------------------------------------------------------- 58
L58 = lesson(
    "Review: family and work",
    "有, 几, 在, 哪儿, 做什么工作",
    requires=[],
    cards=[
        card("What you have covered",
             "You can now say who is in your family, how many there are, what each person does and where. These questions mix it all together.",
             examples=[ex("你们家有几口人？ 我们家有五口人。", "ni3men5 jia1 you3 ji3 kou3 ren2? wo3men5 jia1 you3 wu3 kou3 ren2", "How many people in your family? There are five of us."),
                       ex("你父亲做什么工作？ 他在军校教书。", "ni3 fu4qin1 zuo4 shen2me5 gong1zuo4? ta1 zai4 jun1xiao4 jiao1shu1", "What does your father do? He teaches at a military school."),
                       ex("你有没有兄弟姐妹？ 我有两个姐姐。", "ni3 you3 mei2 you3 xiong1di4 jie3mei4? wo3 you3 liang3 ge4 jie3jie5", "Do you have siblings? I have two older sisters.")]),
    ],
    exercises=[
        M("What is the negative of 有?", "没有", ["不有", "不是", "没是"], "没有."),
        M("Which measure word counts family members?", "口", ["位", "个", "们"], "五口人."),
        M("How do you say “I have two older sisters”?", "我有两个姐姐。", ["我有二个姐姐。", "我有两姐姐。", "我二有个姐姐。"], "Use 两 before the measure word."),
        M("Which question asks “How many people are in your family?”", "你们家有几口人？", ["你们家有什么人？", "你们家几口是人？", "你们家有谁口人？"], "几 + 口 + 人."),
        M("Which question asks a person's job?", "他做什么工作？", ["他在哪儿工作？", "他是谁？", "他姓什么？"], "做什么工作."),
        M("Which question asks where someone works?", "他在哪儿工作？", ["他做什么工作？", "他是谁？", "他有几个孩子？"], "在哪儿."),
        M("Which sentence puts the place correctly?", "他在医院工作。", ["他工作在医院。", "他工作医院在。", "在他工作医院。"], "在 + place + verb."),
        M("Which is the verb + not + verb question?", "你有没有姐姐？", ["你有姐姐吗？", "你有姐姐没？", "你姐姐有吗？"], "有没有."),
        M("What is a 二哥?", "A second older brother", ["A second younger brother", "An eldest brother", "A second older sister"], "二哥."),
        mean("孩子", "hai2zi5", "a child, children", ["a son", "a daughter", "a classmate"]),
        mean("医院", "yi1yuan4", "a hospital", ["a company", "a school", "a college"]),
        mean("教官", "jiao4guan1", "an instructor", ["a doctor", "an engineer", "a driver"]),
        rd("哥哥", "ge1ge5", ["ge2ge5", "ge4ge5", "ge3ge5"]),
        rd("工作", "gong1zuo4", ["gong2zuo4", "gong1zuo2", "gong1zuo1"]),
        F("我们家有五___人。", "口", ["位", "吗", "们"], "口 counts family members.", tr="There are five people in our family."),
        F("我哥哥在医院___。", "工作", ["有", "是", "很"], "工作: to work.", tr="My older brother works at a hospital."),
        F("你有___有兄弟姐妹？", "没", ["不", "吗", "们"], "有没有.", tr="Do you have siblings?"),
    ],
)

UNIT = unit("第三课 Family and work", [L48, L49, L50, L51, L52, L53, L54, L55, L56, L57, L58])
