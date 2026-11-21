"""Unit 5: greetings and introductions, part 2 (lessons 37-47): adjectives, 很/也/都/不, countries, languages,
family, phone numbers, Chinese names, aircraft words, sound contrasts and a review. Original text; the scope
follows DLIFLC Chinese Basic Program Unit 1 Lesson 2, Presentations 2 and 3, the pronunciation review and
the area study on Chinese names."""
from dsl_zh import *


# ---------------------------------------------------------------------------- 37
L37 = lesson(
    "Adjectives as predicates",
    "我很好 · 你忙吗？ · 他不高兴",
    requires=[],
    cards=[
        card("No “to be” with an adjective",
             "In English an adjective needs “am, is, are”: I am happy. In Chinese an adjective works as the predicate by itself, with no 是. "
             "You say 我高兴, not 我是高兴. By default, though, an adjective standing alone sounds like a comparison, so there is usually an adverb in front. "
             "The usual one is 很, which here is often only a link and does not always mean “very”.",
             examples=[ex("我很高兴。", "wo3 hen3 gao1xing4", "I am happy.", hl="很高兴"),
                       ex("你好吗？ 我很好，谢谢。", "ni3 hao3 ma5? wo3 hen3 hao3, xie4xie5", "How are you? I am well, thank you.", hl="很好"),
                       ex("你忙吗？ 我不忙。", "ni3 mang2 ma5? wo3 bu4 mang2", "Are you busy? I am not busy.", hl="不忙"),
                       ex("他也很高兴。", "ta1 ye3 hen3 gao1xing4", "He is happy too.")]),
        card("Words to use",
             "These adjectives work in the pattern Subject + (adverb) + adjective. To ask, add 吗; to answer, repeat the adjective.",
             tables=[wtable([("好", "hao3", "good, well"), ("忙", "mang2", "busy"), ("高兴", "gao1xing4", "happy"), ("大", "da4", "big"),
                             ("小", "xiao3", "small"), ("对", "dui4", "right, correct"), ("不错", "bu2cuo4", "not bad, pretty good")])]),
    ],
    exercises=[
        mean("忙", "mang2", "busy", ["happy", "good", "big"]),
        mean("好", "hao3", "good, well", ["busy", "big", "right"]),
        mean("大", "da4", "big", ["small", "good", "busy"]),
        mean("小", "xiao3", "small", ["big", "good", "happy"]),
        mean("不错", "bu2cuo4", "not bad, pretty good", ["very bad", "not busy", "not happy"]),
        rd("忙", "mang2", ["mang1", "mang3", "mang4"]),
        rd("不错", "bu2cuo4", ["bu4cuo4", "bu2cuo2", "bu2cuo1"]),
        M("Do you need 是 before an adjective in Chinese?", "No", ["Yes, always", "Only in questions", "Only with 很"], "An adjective is a predicate by itself: 我很高兴."),
        M("Which sentence is correct?", "我很高兴。", ["我是很高兴。", "我高兴是。", "我很是高兴。"], "No 是 before an adjective."),
        M("How do you say “I am not busy”?", "我不忙。", ["我是不忙。", "我不是忙。", "不我忙。"], "不 goes before the adjective, with no 是."),
        M("What does 你好吗？ ask?", "How are you?", ["Are you a teacher?", "What is your name?", "Who are you?"], "好 + 吗: are you well?"),
        M("A good reply to 你高兴吗？ is…", "高兴。", ["什么。", "们。", "谁。"], "Repeat the adjective."),
        F("我___高兴。", "很", ["是", "吗", "呢"], "很 comes before the adjective.", tr="I am happy."),
        F("你忙___？", "吗", ["呢", "很", "是"], "吗 turns it into a yes/no question.", tr="Are you busy?"),
        F("我不___。 (busy)", "忙", ["是", "吗", "们"], "不 + adjective.", tr="I am not busy."),
        F("他___很高兴。 (also)", "也", ["是", "吗", "呢"], "也 before 很.", tr="He is happy too."),
    ],
)

# ---------------------------------------------------------------------------- 38
L38 = lesson(
    "很, 也, 都 and 不",
    "他们都是学生 · 我们也都很好",
    requires=[],
    cards=[
        card("Adverbs sit before the verb",
             "很 (very), 也 (also), 都 (both, all) and 不 (not) are adverbs. An adverb always comes before the verb or adjective it describes, never after it. "
             "都 means “both” for two people and “all” for more. When several are present, 也 comes first, then 都, then 很 or 不: 他们也都是学生, 我们都不是老师.",
             tables=[wtable([("也", "ye3", "also"), ("都", "dou1", "both, all"), ("很", "hen3", "very"), ("不", "bu4", "not")])]),
        card("Putting them together",
             "The subject can be one person or many. 都 refers back to the subject, so the subject should be plural.",
             examples=[ex("他也是学生。", "ta1 ye3 shi4 xue2sheng5", "He is a student too.", hl="也"),
                       ex("我们都是学生。", "wo3men5 dou1 shi4 xue2sheng5", "We are all students.", hl="都"),
                       ex("我们都不是老师。", "wo3men5 dou1 bu2shi4 lao3shi1", "None of us is a teacher.", hl="都不"),
                       ex("他们也都很高兴。", "ta1men5 ye3 dou1 hen3 gao1xing4", "They are all happy too.", hl="也都"),
                       ex("我们的中文都很好。", "wo3men5 de5 zhong1wen2 dou1 hen3 hao3", "Our Chinese is good, all of us.", hl="都")]),
    ],
    exercises=[
        mean("都", "dou1", "both, all", ["also", "very", "not"]),
        rd("都", "dou1", ["dou2", "dou3", "dou4"], why="都 is read [[dou1]] when it means “both, all”."),
        M("Where do adverbs like 也 and 都 go?", "Before the verb or adjective", ["After the object", "At the end of the sentence", "Before the subject"], "Adverbs come before what they describe."),
        M("In a sentence with both 也 and 都, which comes first?", "也", ["都", "很", "不"], "The order is 也, then 都."),
        M("What does 我们都是学生 mean?", "We are all students.", ["We are also students.", "We are not students.", "I am a student."], "都 means all."),
        M("What does 他们也都很高兴 mean?", "They are all happy too.", ["They are not happy.", "He is happy.", "They are very happy."], "也 + 都 + 很."),
        M("What does 我们都不是老师 mean?", "None of us is a teacher.", ["We are all teachers.", "I am not a teacher.", "We are also teachers."], "都不 means none, or neither."),
        M("Which sentence is correct?", "他们也都是学生。", ["他们都也是学生。", "也他们都是学生。", "他们是都也学生。"], "也 comes before 都, and both before 是."),
        M("Which sentence is correct?", "我们都不是老师。", ["我们不都是老师。", "都我们不是老师。", "我们是都不老师。"], "都 comes before 不: 都不是."),
        F("我们___是学生。 (all)", "都", ["吗", "呢", "很"], "都 means all.", tr="We are all students."),
        F("他___是学生。 (also)", "也", ["都", "很", "吗"], "也 means also.", tr="He is a student too."),
        F("他们___很好。 (all)", "都", ["吗", "是", "呢"], "都 before 很.", tr="They are all well."),
        F("我们的中文___很好。 (all)", "都", ["吗", "呢", "是"], "都 before 很.", tr="Our Chinese is good."),
        F("我们___不是学生。 (none)", "都", ["吗", "呢", "很"], "都不: none of us.", tr="None of us is a student."),
    ],
)

# ---------------------------------------------------------------------------- 39
L39 = lesson(
    "Countries and nationalities",
    "你是哪国人？ 我是美国人。",
    requires=[],
    cards=[
        card("Naming countries",
             "国 means country and 人 means person. A nationality is the country name plus 人: 中国人 is a Chinese person, 美国人 an American. "
             "Many foreign country names are written with characters chosen for their sounds, so the characters often do not mean anything on their own.",
             tables=[wtable([("中国", "Zhong1guo2", "China"), ("美国", "Mei3guo2", "the United States"), ("日本", "Ri4ben3", "Japan"), ("韩国", "Han2guo2", "South Korea"),
                             ("英国", "Ying1guo2", "the United Kingdom"), ("法国", "Fa3guo2", "France"), ("德国", "De2guo2", "Germany"),
                             ("西班牙", "Xi1ban1ya2", "Spain"), ("俄罗斯", "E2luo2si1", "Russia"), ("加拿大", "Jia1na2da4", "Canada"),
                             ("墨西哥", "Mo4xi1ge1", "Mexico")])]),
        card("Which country? 哪国人",
             "哪 means “which”. 哪国 is “which country”, so 你是哪国人？ asks nationality. It is said nǎ, and many people say něi in 哪国. "
             "The answer replaces 哪国: 我是美国人. As always, the word order does not change.",
             examples=[ex("你是哪国人？", "ni3 shi4 na3 guo2 ren2", "What is your nationality?", hl="哪国"),
                       ex("我是美国人。", "wo3 shi4 Mei3guo2 ren2", "I am American.", hl="美国人"),
                       ex("王老师是哪国人？ 他是中国人。", "Wang2 lao3shi1 shi4 na3 guo2 ren2? ta1 shi4 Zhong1guo2 ren2", "What is Teacher Wang's nationality? He is Chinese."),
                       ex("他不是日本人，他是韩国人。", "ta1 bu2shi4 Ri4ben3 ren2, ta1 shi4 Han2guo2 ren2", "He is not Japanese; he is Korean.")]),
    ],
    exercises=[
        mean("中国", "Zhong1guo2", "China", ["Japan", "Korea", "Germany"]),
        mean("美国", "Mei3guo2", "the United States", ["China", "France", "Spain"]),
        mean("日本", "Ri4ben3", "Japan", ["Korea", "China", "France"]),
        mean("韩国", "Han2guo2", "South Korea", ["Japan", "China", "Germany"]),
        mean("英国", "Ying1guo2", "the United Kingdom", ["France", "Germany", "Spain"]),
        mean("法国", "Fa3guo2", "France", ["Germany", "the United Kingdom", "Spain"]),
        mean("德国", "De2guo2", "Germany", ["France", "the United Kingdom", "Japan"]),
        mean("西班牙", "Xi1ban1ya2", "Spain", ["France", "Mexico", "Germany"]),
        mean("俄罗斯", "E2luo2si1", "Russia", ["Germany", "China", "Canada"]),
        rd("美国", "Mei3guo2", ["Mei2guo2", "Mei3guo3", "Mei4guo2"]),
        rd("韩国", "Han2guo2", ["Han4guo2", "Han2guo3", "Han1guo2"]),
        M("What does 哪国人 mean?", "A person of which country", ["A person from this country", "A person who is happy", "Who is the person"], "哪 is which, 国 is country, 人 is person."),
        M("How do you ask “What is your nationality?”", "你是哪国人？", ["你是什么人？", "你是谁人？", "你哪国是人？"], "Subject + 是 + 哪国人."),
        M("How do you say “I am Japanese”?", "我是日本人。", ["我是日本国。", "我日本人是。", "日本我是人。"], "Country + 人."),
        F("你是哪___人？", "国", ["位", "吗", "们"], "哪国 = which country.", tr="What is your nationality?"),
        F("他是韩国___。", "人", ["们", "吗", "位"], "Country + 人 = nationality.", tr="He is Korean."),
        F("我是___人。 (American)", "美国", ["吗", "中", "老师"], "美国人 = American.", tr="I am American."),
    ],
)

# ---------------------------------------------------------------------------- 40
L40 = lesson(
    "Languages and departments",
    "你说中文吗？ 他的韩语很好。",
    requires=[],
    cards=[
        card("Naming languages",
             "说 means to speak. A language is the first part of the country's name plus 语 or 文, both of which mean “language”: 中国 gives 中文, 英国 gives 英语 or 英文, 法国 gives 法语 or 法文. "
             "The pattern is the same for most languages. 汉语 is also Chinese, and 系 is a university department, as in 中文系.",
             tables=[wtable([("说", "shuo1", "to speak"), ("中文", "Zhong1wen2", "Chinese"), ("汉语", "Han4yu3", "Chinese"), ("英语", "Ying1yu3", "English"), ("英文", "Ying1wen2", "English"),
                             ("日语", "Ri4yu3", "Japanese"), ("韩语", "Han2yu3", "Korean"), ("法语", "Fa3yu3", "French"), ("德语", "De2yu3", "German"),
                             ("俄语", "E2yu3", "Russian"), ("西班牙语", "Xi1ban1ya2yu3", "Spanish"), ("系", "xi4", "a university department")])]),
        card("Speaking and skill",
             "To ask whether someone speaks a language, use 说 and 吗. The answer repeats the verb. To say how good someone's language is, use an adjective with no 是: 他的韩语很好.",
             examples=[ex("你说中文吗？ 说。", "ni3 shuo1 Zhong1wen2 ma5? shuo1", "Do you speak Chinese? Yes.", hl="说"),
                       ex("他说俄语吗？ 不说。", "ta1 shuo1 E2yu3 ma5? bu4 shuo1", "Does he speak Russian? No.", hl="不说"),
                       ex("他的韩语很好。", "ta1 de5 Han2yu3 hen3 hao3", "His Korean is good.", hl="很好"),
                       ex("我的中文不好。", "wo3 de5 Zhong1wen2 bu4 hao3", "My Chinese is not good.", hl="不好"),
                       ex("她是中文系的老师。", "ta1 shi4 Zhong1wen2 xi4 de5 lao3shi1", "She is a teacher in the Chinese department.")]),
    ],
    exercises=[
        mean("说", "shuo1", "to speak", ["to be", "to ask", "to know"]),
        mean("中文", "Zhong1wen2", "Chinese", ["English", "Japanese", "Korean"]),
        mean("英语", "Ying1yu3", "English", ["French", "German", "Chinese"]),
        mean("日语", "Ri4yu3", "Japanese", ["Korean", "Chinese", "English"]),
        mean("韩语", "Han2yu3", "Korean", ["Japanese", "Chinese", "Russian"]),
        mean("法语", "Fa3yu3", "French", ["German", "English", "Spanish"]),
        mean("德语", "De2yu3", "German", ["French", "English", "Spanish"]),
        mean("俄语", "E2yu3", "Russian", ["German", "English", "Chinese"]),
        mean("系", "xi4", "a university department", ["a language", "a country", "a class leader"]),
        rd("说", "shuo1", ["shuo2", "shuo3", "shuo4"]),
        rd("英语", "Ying1yu3", ["Ying2yu3", "Ying1yu4", "Ying3yu3"]),
        M("What do 语 and 文 mean at the end of 中文 and 英语?", "Language", ["Country", "Person", "Department"], "Both mean language."),
        M("How do you say “Do you speak Chinese?”", "你说中文吗？", ["你是中文吗？", "你中文说吗？", "吗你说中文？"], "说 + language + 吗."),
        M("A “no” answer to 你说中文吗？ is…", "不说。", ["不是。", "不对。", "不好。"], "Repeat the verb: 不说."),
        M("How do you say “His Korean is good”?", "他的韩语很好。", ["他的韩语是很好。", "他韩语好是。", "他是韩语很好。"], "No 是 before an adjective."),
        F("你___中文吗？", "说", ["是", "也", "很"], "说 is to speak.", tr="Do you speak Chinese?"),
        F("我的英语___好。 (not good)", "不", ["吗", "也", "是"], "不 + adjective.", tr="My English is not good."),
        F("他的中文___很好。 (also)", "也", ["吗", "是", "们"], "也 before 很.", tr="His Chinese is also good."),
    ],
)

# ---------------------------------------------------------------------------- 41
L41 = lesson(
    "Family: parents and spouse",
    "父亲, 母亲, 父母 · 你父母都是…吗？",
    requires=[],
    cards=[
        card("Parents",
             "爸爸 and 妈妈 are dad and mum, and they are what people say at home. 父亲 and 母亲 are the more formal words, father and mother, "
             "and 父母 is “parents”. As with other close family, the 的 is usually dropped: 你父母, 我父亲, 她母亲.",
             tables=[wtable([("爸爸", "ba4ba5", "dad"), ("妈妈", "ma1ma5", "mum"), ("父亲", "fu4qin1", "father"), ("母亲", "mu3qin1", "mother"),
                             ("父母", "fu4mu3", "parents"), ("太太", "tai4tai5", "wife"), ("先生", "xian1sheng5", "husband"),
                             ("朋友", "peng2you5", "friend")])]),
        card("Asking about family",
             "Put the family word where the subject is and add 哪国人 or 吗. 都 is natural when you ask about both parents.",
             examples=[ex("你父母都是美国人吗？", "ni3 fu4mu3 dou1 shi4 Mei3guo2 ren2 ma5", "Are your parents both American?", hl="都"),
                       ex("不是，我父亲是美国人，母亲是中国人。", "bu2shi4, wo3 fu4qin1 shi4 Mei3guo2 ren2, mu3qin1 shi4 Zhong1guo2 ren2", "No: my father is American and my mother is Chinese."),
                       ex("你太太是哪国人？", "ni3 tai4tai5 shi4 na3 guo2 ren2", "What is your wife's nationality?"),
                       ex("她是德国人，她也说中文。", "ta1 shi4 De2guo2 ren2, ta1 ye3 shuo1 Zhong1wen2", "She is German; she also speaks Chinese.")]),
    ],
    exercises=[
        mean("父亲", "fu4qin1", "father", ["mother", "parents", "husband"]),
        mean("母亲", "mu3qin1", "mother", ["father", "parents", "wife"]),
        mean("父母", "fu4mu3", "parents", ["father", "mother", "friends"]),
        mean("爸爸", "ba4ba5", "dad", ["mum", "husband", "teacher"]),
        mean("妈妈", "ma1ma5", "mum", ["dad", "wife", "friend"]),
        rd("父亲", "fu4qin1", ["fu2qin1", "fu4qin2", "fu3qin1"]),
        rd("母亲", "mu3qin1", ["mu4qin1", "mu3qin2", "mu2qin1"]),
        rd("父母", "fu4mu3", ["fu2mu3", "fu4mu4", "fu4mu2"]),
        M("Which are the more formal words for parents?", "父亲 and 母亲", ["爸爸 and 妈妈", "太太 and 先生", "同学 and 朋友"], "父亲, 母亲 are father and mother, in formal speech."),
        M("What does 你父母都是美国人吗？ ask?", "Are your parents both American?", ["What is your mother's name?", "Are you American?", "Who are your parents?"], "都 means both."),
        M("What does 我父亲是美国人，母亲是中国人 mean?", "My father is American and my mother is Chinese.", ["My mother is American and my father is Chinese.", "My parents are both Chinese.", "My parents are both American."], "父亲 is father, 母亲 is mother."),
        M("How do you ask “What is your wife's nationality?”", "你太太是哪国人？", ["你太太是谁人？", "你先生是哪国人？", "你太太哪国是人？"], "太太 is wife."),
        M("Which word means “parents”?", "父母", ["太太", "先生", "朋友"], "父母 means parents."),
        F("我___是美国人，母亲是中国人。 (father)", "父亲", ["吗", "呢", "们"], "父亲 means father.", tr="My father is American; my mother is Chinese."),
        F("你太太是哪___人？", "国", ["位", "吗", "们"], "哪国人 asks for nationality.", tr="What is your wife's nationality?"),
    ],
)

# ---------------------------------------------------------------------------- 42
L42 = lesson(
    "Phone numbers",
    "电话号码, 手机 · 多少？",
    requires=[],
    cards=[
        card("Asking for a number",
             "电话 is a telephone, 手机 is a cell phone (“hand machine”), and 号码 is a number. "
             "多少 means “how many” or “how much”, and it is the question word for numbers. The answer replaces 多少 as usual. "
             "对了 is “oh, right”, a handy way to change the subject to the number.",
             tables=[wtable([("电话", "dian4hua4", "a telephone"), ("手机", "shou3ji1", "a cell phone"), ("号码", "hao4ma3", "a number"),
                             ("多少", "duo1shao3", "how many, how much"), ("电话号码", "dian4hua4 hao4ma3", "a phone number"), ("手机号码", "shou3ji1 hao4ma3", "a cell phone number"),
                             ("对了", "dui4le5", "oh yes, by the way")])]),
        card("Saying digits",
             "Say each digit in turn, even for a long number. For 1, people usually say yāo instead of yī on the phone and the radio, so that it cannot be mistaken for 7 (qī). "
             "The character 幺 is used for 1 when it is read yāo. In military radio use the digits 0, 7 and 9 are said 洞, 拐 and 勾; Lesson 62 teaches them.",
             examples=[ex("你的电话号码是多少？", "ni3 de5 dian4hua4 hao4ma3 shi4 duo1shao3", "What is your phone number?", hl="多少"),
                       ex("我的号码是幺三五，二四六八。", "wo3 de5 hao4ma3 shi4 yao1 san1 wu3, er4 si4 liu4 ba1", "My number is 135, 2468.", hl="幺"),
                       ex("对了，你的手机号码是多少？", "dui4le5, ni3 de5 shou3ji1 hao4ma3 shi4 duo1shao3", "By the way, what is your cell phone number?"),
                       ex("我的手机号码是九零幺七，八六五四。", "wo3 de5 shou3ji1 hao4ma3 shi4 jiu3 ling2 yao1 qi1, ba1 liu4 wu3 si4", "My cell phone number is 9017 8654.")]),
    ],
    exercises=[
        mean("电话", "dian4hua4", "a telephone", ["a cell phone", "a number", "a name"]),
        mean("手机", "shou3ji1", "a cell phone", ["a telephone", "a number", "a name"]),
        mean("号码", "hao4ma3", "a number", ["a telephone", "a name", "a language"]),
        mean("多少", "duo1shao3", "how many, how much", ["who", "what", "which"]),
        rd("电话", "dian4hua4", ["dian4hua2", "dian3hua4", "dian4hua1"]),
        rd("手机", "shou3ji1", ["shou3ji2", "shou4ji1", "shou2ji1"]),
        rd("号码", "hao4ma3", ["hao4ma1", "hao3ma3", "hao4ma4"]),
        rd("多少", "duo1shao3", ["duo2shao3", "duo1shao4", "duo1shao1"]),
        M("How do you ask “What is your phone number?”", "你的电话号码是多少？", ["你的电话号码是哪？", "你的电话号码是谁？", "你的电话号码是吗？"], "多少 is the question word for numbers."),
        M("Why is 1 often said yāo in phone numbers?", "So it is not confused with 7", ["Because it is polite", "Because it is the 3rd tone", "Because it is rude"], "yāo and qī are clearer apart than yī and qī."),
        M("Which character is read yāo and stands for 1?", "幺", ["么", "六", "十"], "幺 is yāo."),
        M("How do you say 一三五？ on the phone?", "[[yao1 san1 wu3]]", ["[[yi1 san1 wu3]]", "[[yao1 si4 wu3]]", "[[yao1 san1 liu4]]"], "Say yāo for 1."),
        M("How do you say 九零？", "[[jiu3 ling2]]", ["[[jiu3 liu4]]", "[[jiu1 ling2]]", "[[qi1 ling2]]"], "九 is jiǔ and 零 is líng."),
        F("你的电话号码是___？", "多少", ["谁", "吗", "们"], "多少 asks for a number.", tr="What is your phone number?"),
        F("你的手机___是多少？", "号码", ["电话", "手机", "多少"], "号码 is a number.", tr="What is your cell phone number?"),
        F("___，你的手机号码是多少？ (by the way)", "对了", ["谢谢", "再见", "请坐"], "对了 changes the subject politely.", tr="By the way, what is your cell phone number?"),
    ],
)

# ---------------------------------------------------------------------------- 43
L43 = lesson(
    "Chinese names",
    "姓 and 名 · 王, 李, 张, 刘…",
    requires=[],
    cards=[
        card("Surname first, given name second",
             "A Chinese name has two parts: the surname (姓) comes first and the given name (名) comes second. "
             "Most surnames are one character, like 王, 李 and 张, but a few are two, such as 欧阳 and 司马, which are called compound surnames. "
             "Given names are usually one or two characters, so a full name usually has two to four. "
             "Women keep their own surname after marriage.",
             tables=[table(["Name", "Surname 姓", "Given name 名"],
                           [["张华", "张", "华"], ["李明", "李", "明"], ["王小红", "王", "小红"], ["欧阳文", "欧阳", "文"], ["司马平", "司马", "平"]],
                           title="Splitting names", say=[0, 1, 2])]),
        card("Twenty common surnames",
             "There are only a few hundred common surnames, but countless given names: the opposite of English, where first names repeat and surnames vary. These are among the most common.",
             tables=[wtable([("王", "Wang2", "Wáng, also “king”"), ("李", "Li3", "Lǐ, also “plum”"), ("张", "Zhang1", "a common surname"), ("刘", "Liu2", "a common surname"), ("陈", "Chen2", "a common surname"),
                             ("杨", "Yang2", "a common surname"), ("黄", "Huang2", "Huáng, also “yellow”"), ("赵", "Zhao4", "a common surname"), ("吴", "Wu2", "a common surname"), ("周", "Zhou1", "a common surname")],
                            headers=("Surname", "Pinyin", "Note"), title="Surnames 1-10"),
                     wtable([("徐", "Xu2", "a common surname"), ("孙", "Sun1", "a common surname"), ("马", "Ma3", "Mǎ, also “horse”"), ("朱", "Zhu1", "a common surname"), ("胡", "Hu2", "a common surname"),
                             ("郭", "Guo1", "a common surname"), ("何", "He2", "a common surname"), ("林", "Lin2", "Lín, also “forest”"), ("高", "Gao1", "Gāo, also “tall”"), ("罗", "Luo2", "a common surname")],
                            headers=("Surname", "Pinyin", "Note"), title="Surnames 11-20")]),
        card("Choosing a given name",
             "Parents often choose characters for a good meaning, such as strength, beauty, health or good fortune, or simply a pleasant sound. "
             "Boys' names are more likely to use words like 强 (strong) and 伟 (great), and girls' names words for flowers, beauty and gentleness. "
             "Some names show the era: after 1949 names like 建军, “build the army”, became common.",
             examples=[ex("他姓王，叫王强。", "ta1 xing4 Wang2, jiao4 Wang2 Qiang2", "His surname is Wang; he is called Wang Qiang."),
                       ex("她姓欧阳，叫欧阳文。", "ta1 xing4 Ou1yang2, jiao4 Ou1yang2 Wen2", "Her surname is Ouyang; she is called Ouyang Wen."),
                       ex("你好，我姓林，叫林建军。", "ni3 hao3, wo3 xing4 Lin2, jiao4 Lin2 Jian4jun1", "Hello, my surname is Lin; I am called Lin Jianjun.")]),
    ],
    exercises=[
        M("In a Chinese name, which part comes first?", "The surname", ["The given name", "The title", "It depends on the person"], "姓 comes first."),
        M("What is the surname in 张华？", "张", ["华", "张华", "None"], "张 is the surname; 华 is the given name."),
        M("What is the given name in 李明？", "明", ["李", "李明", "None"], "明 is the given name."),
        M("What is the surname in 欧阳文？", "欧阳", ["欧", "阳文", "文"], "欧阳 is a two-character surname."),
        M("What is the given name in 王小红？", "小红", ["王", "红", "王小"], "小红 is a two-character given name."),
        M("What do you call a two-character surname?", "A compound surname", ["A given name", "A title", "A nickname"], "欧阳 and 司马 are compound surnames."),
        M("What does a woman usually do with her surname after marriage?", "Keep her own", ["Take her husband's", "Give it to her children", "Drop it"], "Chinese women keep their original surname."),
        M("How are surnames and given names usually distributed in Chinese?", "Few common surnames, countless given names", ["Few given names, countless surnames", "Both are few", "Both are countless"], "There are few common surnames, but given names are countless."),
        rd("王", "Wang2", ["Wang1", "Wang3", "Weng2"], meaning="the surname Wang"),
        rd("李", "Li3", ["Li1", "Li2", "Li4"], meaning="the surname Li"),
        rd("张", "Zhang1", ["Zhang2", "Zhang3", "Zhang4"], meaning="the surname Zhang"),
        rd("刘", "Liu2", ["Liu1", "Liu3", "Liu4"], meaning="the surname Liu"),
        rd("陈", "Chen2", ["Chen1", "Chen3", "Chen4"], meaning="the surname Chen"),
        rd("赵", "Zhao4", ["Zhao1", "Zhao2", "Zhao3"], meaning="the surname Zhao"),
        rd("孙", "Sun1", ["Sun2", "Sun3", "Sun4"], meaning="the surname Sun"),
        rd("高", "Gao1", ["Gao2", "Gao3", "Gou1"], meaning="the surname Gao"),
        M("Which surname is read Zhōu?", "周", ["朱", "赵", "张"], "周 is Zhōu."),
        M("Which surname is read Hé?", "何", ["胡", "黄", "郭"], "何 is Hé."),
    ],
)

# ---------------------------------------------------------------------------- 44
L44 = lesson(
    "Aircraft words",
    "飞机, 直升机, 战斗机, 轰炸机",
    requires=[],
    cards=[
        card("机, the machine",
             "机 means a machine, and it ends most words for aircraft. 飞 is to fly, so 飞机 is “flying machine”, an aeroplane. "
             "The name for each type adds a descriptive part in front: 直升 (rising straight up) gives 直升机, a helicopter, and 轰炸 (to bomb) gives 轰炸机, a bomber. "
             "You will meet these words in the air force, 空军.",
             tables=[wtable([("飞机", "fei1ji1", "an aeroplane"), ("战斗机", "zhan4dou4ji1", "a combat aircraft"), ("歼击机", "jian1ji1ji1", "a fighter"),
                             ("强击机", "qiang2ji1ji1", "a ground-attack aircraft"), ("轰炸机", "hong1zha4ji1", "a bomber"), ("直升机", "zhi2sheng1ji1", "a helicopter"),
                             ("运输机", "yun4shu1ji1", "a transport aircraft"), ("机", "ji1", "a machine")])]),
        card("In sentences",
             "These words work like any noun.",
             examples=[ex("他是空军，他的飞机很大。", "ta1 shi4 kong1jun1, ta1 de5 fei1ji1 hen3 da4", "He is in the air force; his aircraft is big."),
                       ex("这是直升机，那是轰炸机。", "zhe4 shi4 zhi2sheng1ji1, na4 shi4 hong1zha4ji1", "This is a helicopter; that is a bomber."),
                       ex("你是陆军，你的直升机也很大吗？", "ni3 shi4 lu4jun1, ni3 de5 zhi2sheng1ji1 ye3 hen3 da4 ma5", "You are in the army; is your helicopter big too?")]),
    ],
    exercises=[
        mean("飞机", "fei1ji1", "an aeroplane", ["a helicopter", "a bomber", "a telephone"]),
        mean("直升机", "zhi2sheng1ji1", "a helicopter", ["an aeroplane", "a bomber", "a fighter"]),
        mean("轰炸机", "hong1zha4ji1", "a bomber", ["a helicopter", "a fighter", "an aeroplane"]),
        mean("战斗机", "zhan4dou4ji1", "a combat aircraft", ["a bomber", "a helicopter", "a transport aircraft"]),
        mean("歼击机", "jian1ji1ji1", "a fighter", ["a bomber", "a helicopter", "a transport aircraft"]),
        mean("运输机", "yun4shu1ji1", "a transport aircraft", ["a bomber", "a fighter", "a helicopter"]),
        rd("飞机", "fei1ji1", ["fei2ji1", "fei1ji2", "fei3ji1"]),
        rd("直升机", "zhi2sheng1ji1", ["zhi4sheng1ji1", "zhi2sheng2ji1", "zhi2sheng1ji2"]),
        rd("轰炸机", "hong1zha4ji1", ["hong2zha4ji1", "hong1zha3ji1", "hong1zha4ji2"]),
        M("What does 机 mean on its own?", "A machine", ["A fighter", "A person", "A country"], "机 is machine; it ends most aircraft words."),
        M("Which character ends nearly every word for an aircraft?", "机", ["军", "飞", "空"], "机 is the machine."),
        M("Which character means “to fly”?", "飞", ["机", "空", "军"], "飞 is to fly."),
        F("这是___，那是轰炸机。 (helicopter)", "直升机", ["手机", "电话", "号码"], "直升机 is a helicopter.", tr="This is a helicopter; that is a bomber."),
        F("他是空军，他的___很大。 (aircraft)", "飞机", ["手机", "电话", "号码"], "飞机 is an aeroplane.", tr="He is in the air force; his aircraft is big."),
        M("Which word is a bomber?", "轰炸机", ["直升机", "运输机", "战斗机"], "轰炸 is to bomb."),
    ],
)

# ---------------------------------------------------------------------------- 45
L45 = lesson(
    "Sound pairs: initials",
    "j q x · z c s · zh ch sh r",
    requires=[],
    cards=[
        card("j, q, x with ü",
             "After j, q and x the “u” is really ü (the dots are dropped), so jī and jū, qī and qū, xī and xū sound different even though the letters look nearly the same. "
             "Say the pairs aloud and listen for the lip rounding in the second word.",
             tables=[wtable([("鸡", "ji1", "a chicken"), ("居", "ju1", "to live"), ("七", "qi1", "seven"), ("区", "qu1", "a region"),
                             ("西", "xi1", "west"), ("需", "xu1", "to need"), ("节", "jie2", "a festival"), ("决", "jue2", "to decide")],
                            title="j q x: i or ü")]),
        card("z, c, s and zh, ch, sh, r",
             "z, c and s are made with the tongue tip flat behind the teeth; zh, ch, sh and r with the tip curled back. z and zh are not puffed, and c and ch are puffed.",
             tables=[wtable([("杂", "za2", "mixed"), ("擦", "ca1", "to wipe"), ("撒", "sa1", "to sprinkle"), ("在", "zai4", "at, in"), ("村", "cun1", "a village"),
                             ("酸", "suan1", "sour"), ("孙", "sun1", "the surname Sun"), ("错", "cuo4", "wrong")], title="z c s"),
                     wtable([("这", "zhe4", "this"), ("出", "chu1", "to go out"), ("杀", "sha1", "to kill"), ("肉", "rou4", "meat"), ("人", "ren2", "a person"),
                             ("燃", "ran2", "to burn"), ("绕", "rao4", "to wind around")], title="zh ch sh r")]),
    ],
    exercises=[
        rd("鸡", "ji1", ["qi1", "xi1", "zhi1"], meaning="a chicken"),
        rd("居", "ju1", ["qu1", "xu1", "zhu1"], meaning="to live"),
        rd("区", "qu1", ["ju1", "xu1", "chu1"], meaning="a region"),
        rd("需", "xu1", ["ju1", "qu1", "su1"], meaning="to need"),
        rd("七", "qi1", ["ji1", "xi1", "chi1"], meaning="seven"),
        rd("决", "jue2", ["que2", "xue2", "jie2"], meaning="to decide"),
        rd("杂", "za2", ["ca2", "sa2", "zha2"], meaning="mixed"),
        rd("擦", "ca1", ["za1", "sa1", "cha1"], meaning="to wipe"),
        rd("撒", "sa1", ["za1", "ca1", "sha1"], meaning="to sprinkle"),
        rd("在", "zai4", ["cai4", "sai4", "zhai4"], meaning="at, in"),
        rd("村", "cun1", ["zun1", "sun1", "chun1"], meaning="a village"),
        rd("这", "zhe4", ["che4", "she4", "ze4"], meaning="this"),
        rd("出", "chu1", ["zhu1", "shu1", "cu1"], meaning="to go out"),
        rd("杀", "sha1", ["zha1", "cha1", "sa1"], meaning="to kill"),
        rd("肉", "rou4", ["lou4", "zhou4", "shou4"], meaning="meat"),
        rd("人", "ren2", ["zhen2", "shen2", "ren4"], meaning="a person"),
        M("In which word is the tongue tip flat, behind the teeth?", "擦 [[ca1]]", ["出 [[chu1]]", "杀 [[sha1]]", "人 [[ren2]]"], "c is made with the tip flat; ch, sh and r are curled."),
        M("In which word is the tongue tip curled back?", "杀 [[sha1]]", ["撒 [[sa1]]", "擦 [[ca1]]", "杂 [[za2]]"], "sh is curled; s, c and z are flat."),
    ],
)

# ---------------------------------------------------------------------------- 46
L46 = lesson(
    "Sound pairs: finals",
    "ua/uo · uo/ou · ie/üe · iao/iu · en/eng · in/ing",
    requires=[],
    cards=[
        card("Pairs that look alike",
             "Many final pairs differ in a single sound. Listen to what changes: the final glide (ua and uo), the order of the vowels (uo and ou), "
             "the lip shape (ie and üe), the ending vowel (iao and iu) and the ending nasal (n and ng).",
             tables=[wtable([("袜", "wa4", "a sock"), ("卧", "wo4", "to lie down"), ("瓜", "gua1", "a melon"), ("锅", "guo1", "a pot"), ("画", "hua4", "a picture"),
                             ("货", "huo4", "goods")], title="ua and uo"),
                     wtable([("偷", "tou1", "to steal"), ("拖", "tuo1", "to drag"), ("走", "zou3", "to walk"), ("左", "zuo3", "left"), ("够", "gou4", "enough"),
                             ("过", "guo4", "to pass")], title="ou and uo"),
                     wtable([("夜", "ye4", "night"), ("月", "yue4", "the moon"), ("歇", "xie1", "to rest"), ("靴", "xue1", "boots")], title="ie and üe")]),
        card("More pairs",
             "iao and iu: jiào and jiù. en and eng, in and ing: the ending n has the tongue tip up at the end, and ng has it back.",
             tables=[wtable([("叫", "jiao4", "to call"), ("旧", "jiu4", "old"), ("笑", "xiao4", "to laugh"), ("秀", "xiu4", "excellent"), ("敲", "qiao1", "to knock"),
                             ("秋", "qiu1", "autumn")], title="iao and iu"),
                     wtable([("分", "fen1", "to divide"), ("风", "feng1", "wind"), ("镇", "zhen4", "a town"), ("政", "zheng4", "politics"), ("人", "ren2", "a person"),
                             ("仍", "reng2", "still")], title="en and eng"),
                     wtable([("金", "jin1", "gold"), ("京", "jing1", "a capital"), ("寝", "qin3", "to sleep"), ("请", "qing3", "please, to invite"), ("您", "nin2", "you (polite)"),
                             ("宁", "ning2", "rather")], title="in and ing")]),
    ],
    exercises=[
        rd("袜", "wa4", ["wo4", "wai4", "wu4"], meaning="a sock"),
        rd("卧", "wo4", ["wa4", "wei4", "wu4"], meaning="to lie down"),
        rd("瓜", "gua1", ["guo1", "guai1", "gu1"], meaning="a melon"),
        rd("锅", "guo1", ["gua1", "guai1", "gu1"], meaning="a pot"),
        rd("货", "huo4", ["hua4", "hou4", "hu4"], meaning="goods"),
        rd("偷", "tou1", ["tuo1", "tu1", "tao1"], meaning="to steal"),
        rd("拖", "tuo1", ["tou1", "tu1", "tao1"], meaning="to drag"),
        rd("走", "zou3", ["zuo3", "zu3", "zao3"], meaning="to walk"),
        rd("左", "zuo3", ["zou3", "zu3", "zao3"], meaning="left"),
        rd("够", "gou4", ["guo4", "gu4", "gao4"], meaning="enough"),
        rd("夜", "ye4", ["yue4", "yi4", "ya4"], meaning="night"),
        rd("月", "yue4", ["ye4", "yu4", "yuan4"], meaning="the moon"),
        rd("靴", "xue1", ["xie1", "xu1", "xuan1"], meaning="boots"),
        rd("叫", "jiao4", ["jiu4", "jian4", "jie4"], meaning="to call"),
        rd("旧", "jiu4", ["jiao4", "jian4", "jie4"], meaning="old"),
        rd("秋", "qiu1", ["qiao1", "qian1", "qu1"], meaning="autumn"),
        rd("风", "feng1", ["fen1", "fang1", "fei1"], meaning="wind"),
        rd("镇", "zhen4", ["zheng4", "zhan4", "zhun4"], meaning="a town"),
        rd("金", "jin1", ["jing1", "jian1", "jun1"], meaning="gold"),
        rd("请", "qing3", ["qin3", "qiang3", "qian3"], meaning="please, to invite"),
        rd("您", "nin2", ["ning2", "nan2", "nen2"], meaning="you (polite)"),
        M("Which pair differs only by the ending n against ng?", "金 [[jin1]] and 京 [[jing1]]", ["夜 [[ye4]] and 月 [[yue4]]", "瓜 [[gua1]] and 锅 [[guo1]]", "叫 [[jiao4]] and 旧 [[jiu4]]"], "n and ng differ by the ending nasal."),
        M("Which pair differs only by ie against üe?", "夜 [[ye4]] and 月 [[yue4]]", ["金 [[jin1]] and 京 [[jing1]]", "走 [[zou3]] and 左 [[zuo3]]", "分 [[fen1]] and 风 [[feng1]]"], "ie and üe differ by the lip rounding."),
    ],
)

# ---------------------------------------------------------------------------- 47
L47 = lesson(
    "Review: greetings and introductions",
    "Meeting, asking, nationality, languages and numbers",
    requires=[],
    cards=[
        card("What you have covered",
             "You can now greet someone, ask and give names, ask whether someone is a student or teacher, ask who someone is, introduce a third person, "
             "say what nationality and languages people have, and ask for a phone number. The questions below mix all of this.",
             examples=[ex("您好！请问，您贵姓？", "nin2 hao3! qing3wen4, nin2 gui4xing4", "Hello! May I ask your surname?"),
                       ex("这位是我的朋友，他是美国人，也说中文。", "zhe4wei4 shi4 wo3 de5 peng2you5, ta1 shi4 Mei3guo2 ren2, ye3 shuo1 Zhong1wen2", "This is my friend. He is American and also speaks Chinese."),
                       ex("对了，你的手机号码是多少？", "dui4le5, ni3 de5 shou3ji1 hao4ma3 shi4 duo1shao3", "By the way, what is your cell phone number?")]),
    ],
    exercises=[
        M("Which turns a statement into a yes/no question?", "吗", ["呢", "什么", "谁"], "吗 goes on the end of a statement."),
        M("Which is the polite form of “you”?", "您", ["你们", "他", "她们"], "您 is polite."),
        M("What does 你呢？ ask?", "And you?", ["Who are you?", "Are you a teacher?", "What is your name?"], "呢 follows up."),
        M("Which question asks for a person?", "他是谁？", ["他姓什么？", "他是哪国人？", "他是学生吗？"], "谁 asks who."),
        M("Which question asks for nationality?", "你是哪国人？", ["你叫什么名字？", "你说中文吗？", "你是谁？"], "哪国人 asks nationality."),
        M("Which word for “this person” is polite?", "这位", ["这们", "这吗", "这呢"], "这位 is the polite form."),
        M("Which means “We are all students”?", "我们都是学生。", ["我们也是学生。", "我们不是学生。", "我是学生。"], "都 means all."),
        M("How is 不 pronounced in 不是?", "[[bu2]]", ["[[bu4]]", "[[bu1]]", "[[bu3]]"], "Before a 4th tone it is bú."),
        M("How do you say “I am not busy”?", "我不忙。", ["我不是忙。", "我忙不。", "我是不忙。"], "No 是 before an adjective."),
        M("What does 他的韩语很好 mean?", "His Korean is good.", ["He is Korean.", "He speaks French.", "His Korean is not good."], "韩语 is Korean."),
        F("你是中国人___？", "吗", ["呢", "什么", "们"], "吗 on the end.", tr="Are you Chinese?"),
        F("我___是老师。 (not)", "不", ["吗", "呢", "们"], "不 before 是.", tr="I am not a teacher."),
        F("他们___是学生。 (all)", "都", ["吗", "呢", "们"], "都 means all.", tr="They are all students."),
        F("你___中文吗？", "说", ["是", "也", "很"], "说 is to speak.", tr="Do you speak Chinese?"),
        F("你的电话号码是___？", "多少", ["谁", "吗", "们"], "多少 asks for numbers.", tr="What is your phone number?"),
        mean("认识", "ren4shi5", "to know (a person)", ["to speak", "to ask", "to be called"]),
        mean("父母", "fu4mu3", "parents", ["a wife", "a husband", "friends"]),
        mean("手机", "shou3ji1", "a cell phone", ["a telephone", "a number", "an aeroplane"]),
        rd("美国", "Mei3guo2", ["Mei2guo2", "Mei3guo3", "Mei4guo2"]),
        rd("说", "shuo1", ["shuo2", "shuo3", "shuo4"]),
    ],
)

UNIT = unit("第二课 People, languages and numbers", [L37, L38, L39, L40, L41, L42, L43, L44, L45, L46, L47])
