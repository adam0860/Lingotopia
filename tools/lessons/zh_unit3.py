"""Unit 3: first words (lessons 20-26): numbers, greetings, classroom expressions, names, services
and ranks. Original text; the vocabulary follows the practice material in DLIFLC Chinese Basic
Program Unit 1 Lesson 1 (greetings, introductions, services, ranks)."""
from dsl_zh import *


def sent(hanzi, py, en):
    return ex(hanzi, py, en)


# ---------------------------------------------------------------------------- 20
L20 = lesson(
    "Numbers 0 to 10",
    "零 一 二 三 四 五 六 七 八 九 十",
    requires=[],
    cards=[
        card("Eleven words to count with",
             "Chinese numbers are regular. You will use these every day, and they are good practice for tones. "
             "Zero is líng. Numbers above ten are built from these: eleven is “ten-one”, twenty is “two-ten”. "
             "In phone numbers and on the radio, 1 is often said yāo instead of yī, so it cannot be mistaken for 7.",
             tables=[wtable([("零", "ling2", "0"), ("一", "yi1", "1"), ("二", "er4", "2"), ("三", "san1", "3"), ("四", "si4", "4"),
                             ("五", "wu3", "5"), ("六", "liu4", "6"), ("七", "qi1", "7"), ("八", "ba1", "8"), ("九", "jiu3", "9"), ("十", "shi2", "10")])]),
        card("Reading digits",
             "To read a string of digits, say each one in turn. This is how you give a number such as a room or a phone number.",
             examples=[ex("一二三四", "yi1 er4 san1 si4", "1234"), ex("五六七八", "wu3 liu4 qi1 ba1", "5678"), ex("九零一零", "jiu3 ling2 yi1 ling2", "9010")]),
    ],
    exercises=[
        M("What is 三?", "3", ["2", "4", "5"], "三 ([[san1]]) is three: three horizontal strokes."),
        M("What is 五?", "5", ["4", "6", "9"], "五 ([[wu3]]) is five."),
        M("What is 八?", "8", ["6", "7", "9"], "八 ([[ba1]]) is eight."),
        M("What is 十?", "10", ["7", "1", "0"], "十 ([[shi2]]) is ten, a cross."),
        M("What is 零?", "0", ["1", "10", "9"], "零 ([[ling2]]) is zero."),
        M("Which character is [[liu4]]?", "六", ["五", "七", "八"], "[[liu4]] is six."),
        M("Which character is [[qi1]]?", "七", ["六", "九", "十"], "[[qi1]] is seven."),
        M("Which character is [[jiu3]]?", "九", ["八", "七", "十"], "[[jiu3]] is nine."),
        M("Which character is [[si4]]?", "四", ["三", "五", "十"], "[[si4]] is four."),
        rd("二", "er4", ["er2", "er3", "e4"], meaning="2"),
        rd("七", "qi1", ["qi3", "qi4", "ji1"], meaning="7"),
        rd("九", "jiu3", ["jiu2", "jiu4", "jiao3"], meaning="9"),
        M("How do you say 一二三四?", "[[yi1 er4 san1 si4]]", ["[[yi1 san1 er4 si4]]", "[[er4 yi1 si4 san1]]", "[[yi1 er4 san1 wu3]]"], "Read each digit in turn: yī èr sān sì."),
        M("How do you say 五六七八?", "[[wu3 liu4 qi1 ba1]]", ["[[wu3 qi1 liu4 ba1]]", "[[liu4 wu3 ba1 qi1]]", "[[wu3 liu4 qi1 jiu3]]"], "Wǔ liù qī bā."),
        M("Why is 1 sometimes said yāo in phone numbers?", "So it is not mistaken for 7", ["Because yī is rude", "Because yāo is the 2nd tone", "It is not: that is a mistake"], "On the radio and phone, yāo and qī are more distinct than yī and qī."),
    ],
)

# ---------------------------------------------------------------------------- 21
L21 = lesson(
    "Greetings and class",
    "早, 你好, 谢谢, 再见",
    requires=[],
    cards=[
        card("Hello, thanks and goodbye",
             "These are the first things you say in a Chinese classroom. 早 means “early” and is how you say good morning. "
             "你好 is the general hello, and 你们好 is hello to more than one person. When you speak to a teacher, add 老师. "
             "The word 不 changes to the 2nd tone before a 4th tone, so 不客气 is said búkèqi and written that way.",
             tables=[wtable([("早", "zao3", "good morning"), ("你好", "ni3 hao3", "hello"), ("你们好", "ni3men5 hao3", "hello (to several people)"),
                             ("老师好", "lao3shi1 hao3", "hello, teacher"), ("老师早", "lao3shi1 zao3", "good morning, teacher"),
                             ("同学们早", "tong2xue2men5 zao3", "good morning, everyone"),
                             ("谢谢", "xie4xie5", "thank you"), ("不客气", "bu2 ke4qi5", "you are welcome"),
                             ("再见", "zai4jian4", "goodbye"), ("明天见", "ming2tian1 jian4", "see you tomorrow"),
                             ("周末快乐", "zhou1mo4 kuai4le4", "have a good weekend")])]),
        card("Class begins and ends",
             "The teacher opens and closes class with these words, and students answer.",
             tables=[wtable([("上课", "shang4ke4", "class begins"), ("请坐", "qing3 zuo4", "please sit down"), ("下课", "xia4ke4", "class is over")])]),
    ],
    exercises=[
        mean("早", "zao3", "good morning", ["goodbye", "thank you", "hello"]),
        mean("谢谢", "xie4xie5", "thank you", ["goodbye", "good morning", "you are welcome"]),
        mean("再见", "zai4jian4", "goodbye", ["thank you", "hello", "class begins"]),
        mean("不客气", "bu2 ke4qi5", "you are welcome", ["thank you", "goodbye", "hello"]),
        mean("上课", "shang4ke4", "class begins", ["class is over", "goodbye", "please sit"]),
        mean("下课", "xia4ke4", "class is over", ["class begins", "good morning", "hello"]),
        mean("请坐", "qing3 zuo4", "please sit down", ["class is over", "thank you", "goodbye"]),
        mean("明天见", "ming2tian1 jian4", "see you tomorrow", ["good morning", "have a good weekend", "you are welcome"]),
        mean("周末快乐", "zhou1mo4 kuai4le4", "have a good weekend", ["see you tomorrow", "good morning", "thank you"]),
        M("What do you say to your teacher when you meet in the morning?", "老师早", ["再见", "不客气", "下课"], "老师早 ([[lao3shi1 zao3]]): good morning, teacher."),
        M("What do you say to several people when you arrive?", "你们好", ["你好", "谢谢", "请坐"], "你们好 is hello to a group. 你好 is for one person."),
        F("A: 谢谢！ B: ___！", "不客气", ["再见", "请坐", "上课"], "Someone says thank you: you answer 不客气, you are welcome.", tr="A: Thank you! B: You are welcome!"),
        F("下课了。老师说：“___！”", "再见", ["上课", "请坐", "早"], "At the end of class the teacher says 再见, goodbye.", tr="Class is over. The teacher says: “Goodbye!”"),
        M("How do you say 不客气?", "[[bu2 ke4qi5]]", ["[[bu4 ke4qi5]]", "[[bu2 ke2qi5]]", "[[bu1 ke4qi5]]"], "不 becomes 2nd tone before a 4th tone: bú kèqi."),
        M("Which means “have a good weekend”?", "周末快乐", ["明天见", "不客气", "同学们早"], "周末 is weekend and 快乐 is happy."),
    ],
)

# ---------------------------------------------------------------------------- 22
L22 = lesson(
    "Classroom questions",
    "有问题吗？ 听懂了吗？",
    requires=[],
    cards=[
        card("Asking and answering in class",
             "To ask whether someone has a question, add 吗 to the end of a statement: 有问题吗? "
             "The answer is just the verb: 有 (I do) or 没有 (I do not). "
             "To ask whether someone understood what they heard, say 听懂了吗? and answer 听懂了 or 没听懂. "
             "If you did not catch something, you can ask 请你再说一遍, please say it again.",
             tables=[wtable([("有问题吗", "you3 wen4ti2 ma5", "any questions?"), ("有", "you3", "yes, I have"), ("没有", "mei2you3", "no, I have none"),
                             ("听懂了吗", "ting1dong3le5 ma5", "did you understand (by listening)?"), ("听懂了", "ting1dong3le5", "I understood"),
                             ("没听懂", "mei2 ting1dong3", "I did not understand"), ("请你再说一遍", "qing3 ni3 zai4 shuo1 yi2bian4", "please say it again")])]),
        card("How 吗 works",
             "吗 turns a statement into a yes/no question without changing the word order. Compare the two lines.",
             examples=[ex("你有问题。", "ni3 you3 wen4ti2", "You have a question."), ex("你有问题吗？", "ni3 you3 wen4ti2 ma5", "Do you have a question?")]),
    ],
    exercises=[
        mean("有问题吗", "you3 wen4ti2 ma5", "any questions?", ["thank you", "please sit", "class is over"]),
        mean("没有", "mei2you3", "no, I have none", ["yes, I have", "goodbye", "any questions?"]),
        mean("听懂了", "ting1dong3le5", "I understood", ["I did not understand", "any questions?", "say it again"]),
        mean("没听懂", "mei2 ting1dong3", "I did not understand", ["I understood", "I have a question", "goodbye"]),
        mean("请你再说一遍", "qing3 ni3 zai4 shuo1 yi2bian4", "please say it again", ["please sit down", "any questions?", "I understood"]),
        M("You did not understand what the teacher said. You say…", "没听懂", ["听懂了", "没有", "不客气"], "没听懂: I did not understand."),
        M("You want the teacher to repeat. You say…", "请你再说一遍", ["有问题吗", "听懂了", "下课"], "请你再说一遍: please say it again."),
        M("The teacher asks 有问题吗？ and you have none. You say…", "没有", ["有", "听懂了", "再见"], "没有: I do not have any."),
        M("The teacher asks 有问题吗？ and you do have a question. You say…", "有", ["没有", "没听懂", "不客气"], "有: yes, I have."),
        M("What does 吗 do at the end of a sentence?", "Makes it a yes/no question", ["Makes it negative", "Makes it past tense", "Makes it polite"], "吗 ([[ma5]]) marks a yes/no question."),
        F("听懂了___？", "吗", ["的", "了", "有"], "吗 at the end makes it a yes/no question.", tr="Did you understand?"),
        M("How is 没听懂 said?", "[[mei2 ting1dong3]]", ["[[mei3 ting1dong3]]", "[[mei2 ting2dong3]]", "[[mei2 ting1dong1]]"], "méi tīng dǒng."),
        M("How is 有问题吗 written in pinyin?", "[[you3 wen4ti2 ma5]]", ["[[you3 wen4ti2 ma3]]", "[[you2 wen4ti2 ma5]]", "[[you3 wen2ti2 ma5]]"], "yǒu wèntí ma: ma is neutral and has no mark."),
    ],
)

# ---------------------------------------------------------------------------- 23
L23 = lesson(
    "My name is…",
    "我姓…, 我叫…",
    requires=[],
    cards=[
        card("I, you, he, she",
             "Chinese pronouns do not change shape. 我 is I or me, 你 is you, 您 is the polite you for one person, and 他 and 她 are he and she, "
             "which sound exactly alike. Add 们 to make a plural: 你们, 他们.",
             tables=[wtable([("我", "wo3", "I, me"), ("你", "ni3", "you"), ("您", "nin2", "you (polite)"), ("他", "ta1", "he, him"), ("她", "ta1", "she, her"),
                             ("你们", "ni3men5", "you (plural)"), ("他们", "ta1men5", "they")])]),
        card("Giving your name",
             "A Chinese name puts the family name first. 姓 is for the family name and 叫 is for the whole name or the given name. "
             "To ask someone politely for their family name, say 请问，您贵姓? (“May I ask, what is your honourable surname?”). "
             "To ask a name casually, say 你叫什么名字?",
             tables=[wtable([("姓", "xing4", "to have the family name"), ("叫", "jiao4", "to be called"), ("什么", "shen2me5", "what"),
                             ("名字", "ming2zi5", "a name"), ("请问", "qing3wen4", "may I ask…"), ("贵姓", "gui4xing4", "your honourable surname")])]),
            card("Putting it together",
             "Read these short exchanges aloud. The names are only examples.",
             examples=[ex("请问，您贵姓？", "qing3wen4, nin2 gui4xing4", "May I ask your surname?"),
                       ex("我姓张。", "wo3 xing4 Zhang1", "My surname is Zhang."),
                       ex("你叫什么名字？", "ni3 jiao4 shen2me5 ming2zi5", "What is your name?"),
                       ex("我叫张华。", "wo3 jiao4 Zhang1 Hua2", "My name is Zhang Hua.")]),
    ],
    exercises=[
        mean("我", "wo3", "I, me", ["you", "he", "they"]),
        mean("您", "nin2", "you (polite)", ["you (plural)", "I", "she"]),
        mean("他们", "ta1men5", "they", ["you (plural)", "he", "I"]),
        mean("名字", "ming2zi5", "a name", ["what", "surname", "thank you"]),
        mean("请问", "qing3wen4", "may I ask…", ["thank you", "goodbye", "what"]),
        mean("什么", "shen2me5", "what", ["a name", "may I ask", "to be called"]),
        M("What is the difference between 他 and 她 when spoken?", "None: both are [[ta1]]", ["他 is 1st tone and 她 is 3rd", "他 is formal", "They are different words"], "他 and 她 are written differently but sound the same."),
        M("Which means “you” to be polite to one person?", "您", ["你", "你们", "他"], "您 is the polite you."),
        M("Which means “you” to a group?", "你们", ["您", "我们", "他们"], "你们 is you (plural)."),
        F("我___张。", "姓", ["好", "是", "有"], "姓 introduces the family name: 我姓张, my surname is Zhang.", tr="My surname is Zhang."),
        F("我___张华。", "叫", ["姓", "是", "好"], "叫 gives your name: 我叫张华.", tr="My name is Zhang Hua."),
        F("你叫___名字？", "什么", ["谁", "哪", "怎么"], "你叫什么名字? is the way to ask “what is your name?”", tr="What is your name?"),
        M("Which question asks politely for a family name?", "请问，您贵姓？", ["你叫什么名字？", "你好吗？", "你是谁？"], "您贵姓 asks for the family name, and is the polite way."),
        M("In Chinese, which name comes first?", "The family name", ["The given name", "It depends on the person", "The title"], "Chinese names put the family name first: 张华 is Zhāng (family) Huá (given)."),
        M("How is 我叫张华 said?", "[[wo3 jiao4 Zhang1 Hua2]]", ["[[wo2 jiao4 Zhang1 Hua2]]", "[[wo3 jiao3 Zhang1 Hua2]]", "[[wo3 jiao4 Zhang1 Hua4]]"], "Wǒ jiào Zhāng Huá."),
    ],
)

# ---------------------------------------------------------------------------- 24
L24 = lesson(
    "Branches of service",
    "海军, 陆军, 空军, 海军陆战队",
    requires=[],
    cards=[
        card("Who serves in what",
             "The names of the services are built from the same parts. 军 means military or army. 海 is sea, 陆 is land and 空 is sky, "
             "so 海军 is the navy, 陆军 the army and 空军 the air force. 海军陆战队 is the marine corps: “sea-force land-fighting unit”. "
             "To say what service you are in, use 是: 我是海军 literally means “I am navy”. Put 美国 in front to say it is the American one.",
             tables=[wtable([("海军", "hai3jun1", "navy"), ("陆军", "lu4jun1", "army"), ("空军", "kong1jun1", "air force"),
                             ("海军陆战队", "hai3jun1 lu4zhan4dui4", "marine corps"), ("军人", "jun1ren2", "a service member"),
                             ("是", "shi4", "to be"), ("美国", "mei3guo2", "the United States")])]),
        card("I am… you are… he is…",
             "The same three sentence patterns work for every service.",
             examples=[ex("我是海军。", "wo3 shi4 hai3jun1", "I am in the navy."),
                       ex("你是陆军。", "ni3 shi4 lu4jun1", "You are in the army."),
                       ex("他是空军。", "ta1 shi4 kong1jun1", "He is in the air force."),
                       ex("她是海军陆战队。", "ta1 shi4 hai3jun1 lu4zhan4dui4", "She is in the marine corps."),
                       ex("我是美国陆军。", "wo3 shi4 mei3guo2 lu4jun1", "I am in the US Army.")]),
    ],
    exercises=[
        mean("海军", "hai3jun1", "navy", ["army", "air force", "marine corps"]),
        mean("陆军", "lu4jun1", "army", ["navy", "air force", "a service member"]),
        mean("空军", "kong1jun1", "air force", ["navy", "army", "marine corps"]),
        mean("海军陆战队", "hai3jun1 lu4zhan4dui4", "marine corps", ["navy", "army", "air force"]),
        mean("军人", "jun1ren2", "a service member", ["navy", "teacher", "friend"]),
        M("Which character means “sea”?", "海", ["陆", "空", "军"], "海 is sea, so 海军 is the navy."),
        M("Which character means “land”?", "陆", ["海", "空", "军"], "陆 is land, so 陆军 is the army."),
        M("Which character means “sky”?", "空", ["海", "陆", "军"], "空 is sky, so 空军 is the air force."),
        M("Which character appears in the name of all the services?", "军", ["海", "陆", "空"], "军 means military or forces."),
        M("How do you say “I am in the army”?", "我是陆军。", ["你是陆军。", "我是海军。", "他是陆军。"], "我 is I, 是 is to be, 陆军 is army."),
        M("What does 你是空军 mean?", "You are in the air force.", ["I am in the air force.", "You are in the navy.", "He is in the air force."], "你 is you and 空军 is air force."),
        F("她___海军陆战队。", "是", ["叫", "姓", "有"], "是 links a person to a service: 她是海军陆战队.", tr="She is in the marine corps."),
        F("我是___海军。", "美国", ["吗", "们", "有"], "美国 in front says it is the United States Navy.", tr="I am in the US Navy.", ),
        M("Which is the correct pinyin for 海军?", "[[hai3jun1]]", ["[[hai3jun3]]", "[[hai4jun1]]", "[[hai3jun4]]"], "Hǎijūn: 3rd tone then 1st tone. The 3rd is a half-third."),
        M("How is 陆军 said?", "[[lu4jun1]]", ["[[lu4jun2]]", "[[lu3jun1]]", "[[lu4jun4]]"], "Lùjūn."),
    ],
)

# ---------------------------------------------------------------------------- 25
L25 = lesson(
    "Ranks",
    "少尉, 中尉, 上尉… 少校, 中校, 上校… 少将, 中将, 上将",
    requires=[],
    cards=[
        card("A pattern you can learn once",
             "Chinese officer ranks are built from two parts. The first part says the grade: 少 (junior), 中 (middle) or 上 (senior). "
             "The second says the group: 尉 (company-grade officer), 校 (field-grade officer) or 将 (general officer). "
             "Put them together and you get nine ranks. These are also the Chinese names used for the matching US officer ranks.",
             tables=[table(["Grade", "尉 wèi", "校 xiào", "将 jiàng"],
                           [["少 shào: junior", "少尉 [[shao4wei4]]", "少校 [[shao4xiao4]]", "少将 [[shao4jiang4]]"],
                            ["中 zhōng: middle", "中尉 [[zhong1wei4]]", "中校 [[zhong1xiao4]]", "中将 [[zhong1jiang4]]"],
                            ["上 shàng: senior", "上尉 [[shang4wei4]]", "上校 [[shang4xiao4]]", "上将 [[shang4jiang4]]"]],
                           title="Officer ranks", note="For the US: second lieutenant, first lieutenant, captain; major, lieutenant colonel, colonel; major general, lieutenant general, general. Brigadier general is 准将 [[zhun3jiang4]].")]),
        card("Other useful words",
             "兵 is a soldier or private. 军官 is an officer, and 军士 is a non-commissioned officer. 军衔 is a military rank. "
             "The Chinese army is called 中国人民解放军, the People's Liberation Army. Ranks and their names change over time, so check a current source before relying on any list.",
             tables=[wtable([("兵", "bing1", "a soldier, a private"), ("士兵", "shi4bing1", "an enlisted soldier"), ("军官", "jun1guan1", "an officer"),
                             ("军士", "jun1shi4", "a non-commissioned officer"), ("军衔", "jun1xian2", "a military rank"),
                             ("中国人民解放军", "Zhong1guo2 Ren2min2 Jie3fang4jun1", "the People's Liberation Army"),
                             ("列兵", "lie4bing1", "a private (PLA)")])]),
    ],
    exercises=[
        mean("少尉", "shao4wei4", "second lieutenant", ["first lieutenant", "captain", "major"]),
        mean("中尉", "zhong1wei4", "first lieutenant", ["second lieutenant", "captain", "colonel"]),
        mean("上尉", "shang4wei4", "captain", ["first lieutenant", "major", "colonel"]),
        mean("少校", "shao4xiao4", "major", ["captain", "lieutenant colonel", "colonel"]),
        mean("中校", "zhong1xiao4", "lieutenant colonel", ["major", "colonel", "captain"]),
        mean("上校", "shang4xiao4", "colonel", ["lieutenant colonel", "major", "general"]),
        mean("少将", "shao4jiang4", "major general", ["lieutenant general", "general", "colonel"]),
        mean("上将", "shang4jiang4", "general", ["major general", "lieutenant general", "colonel"]),
        M("In a rank name, which character means “senior”?", "上", ["少", "中", "尉"], "上 is the top grade: 上尉, 上校, 上将."),
        M("In a rank name, which character means “junior”?", "少", ["上", "中", "将"], "少 is the lowest grade: 少尉, 少校, 少将."),
        M("Which part of the name says it is a general officer?", "将", ["尉", "校", "兵"], "将 marks general officers: 少将, 中将, 上将."),
        M("Which part of the name says it is a field-grade officer (major to colonel)?", "校", ["尉", "将", "兵"], "校 marks majors, lieutenant colonels and colonels."),
        M("Which is the more senior rank?", "上校", ["少校", "中校", "少尉"], "上 is senior to 中 and 少, and 校 outranks 尉."),
        M("Which is the more senior rank?", "中将", ["少将", "上校", "中校"], "将 outranks 校, and 中将 is above 少将."),
        mean("军衔", "jun1xian2", "a military rank", ["an officer", "a soldier", "a navy"]),
        mean("军官", "jun1guan1", "an officer", ["a military rank", "a soldier", "an army"]),
        M("Why check a current source for ranks?", "Ranks and their names change over time", ["They never change", "Only the US changes them", "Only the pinyin changes"], "Armies reorganise their ranks, so names and lists can be out of date."),
    ],
)

# ---------------------------------------------------------------------------- 26
L26 = lesson(
    "Review: pronunciation and first words",
    "Sounds, tones, greetings, names and services",
    requires=[],
    cards=[
        card("What you have covered",
             "Lesson 1 gave you the whole sound system: 21 initials, the finals, the spelling rules and five tones, and the third-tone and neutral-tone patterns. "
             "It also gave you your first words: numbers to ten, greetings, class expressions, how to say your name, the services and the ranks. "
             "These questions mix it all together.",
             examples=[ex("你好！我叫张华。", "ni3 hao3! wo3 jiao4 Zhang1 Hua2", "Hello! My name is Zhang Hua."),
                       ex("我是海军。", "wo3 shi4 hai3jun1", "I am in the navy."),
                       ex("再见，明天见！", "zai4jian4, ming2tian1 jian4", "Goodbye, see you tomorrow!")]),
    ],
    exercises=[
        M("Which initial is said with a strong puff and the tongue tip down?", "q", ["j", "ch", "c"], "Q is aspirated and made with the tip down. Ch is curled, c is at the teeth."),
        M("Which initial sounds like the ds in “buds”?", "z", ["zh", "c", "j"], "Z is d + s."),
        M("How is the i in [[shi4]] pronounced?", "As a curled buzz", ["Like “ee”", "As a buzz at the teeth", "It is silent"], "After sh the i is a curled buzz."),
        M("How is ü written after j?", "u, with no dots", ["ü", "yu", "v"], "After j, q and x the dots are dropped: ju, qu, xu."),
        M("How is the final ia written with no initial?", "ya", ["ia", "wa", "yia"], "A bare i becomes y."),
        M("Where does the tone mark go in [[liu4]]?", "On the u", ["On the i", "On the l", "On both"], "In iu the mark goes on the second vowel."),
        M("Which tone falls sharply?", "The 4th", ["The 1st", "The 2nd", "The 3rd"], "The 4th tone is a sharp fall."),
        M("How is 你好 said?", "[[ni2 hao3]]", ["[[ni3 hao3]]", "[[ni4 hao3]]", "[[ni1 hao3]]"], "Two 3rd tones: the first is said as a 2nd tone."),
        M("What is the neutral tone?", "A light, short syllable with no mark", ["A very high tone", "A sharp fall", "A silent syllable"], "It is said lightly and has no tone mark."),
        rd("六", "liu4", ["liu1", "liu2", "liu3"], meaning="6"),
        mean("五", "wu3", "5", ["4", "6", "9"]),
        mean("谢谢", "xie4xie5", "thank you", ["goodbye", "hello", "you are welcome"]),
        M("What do you answer to 谢谢？", "不客气", ["请坐", "上课", "明天见"], "不客气: you are welcome."),
        F("我___李明。", "叫", ["姓", "是", "好"], "叫 gives the whole name: 我叫李明.", tr="My name is Li Ming."),
        M("What does 我是陆军 mean?", "I am in the army.", ["I am in the navy.", "You are in the army.", "He is in the army."], "陆军 is army."),
        mean("上校", "shang4xiao4", "colonel", ["major", "captain", "general"]),
        M("What does 有问题吗？ ask?", "Do you have any questions?", ["Did you understand?", "What is your name?", "Is class over?"], "有问题吗 asks if there are questions."),
    ],
)

UNIT = unit("第一课 First words and greetings", [L20, L21, L22, L23, L24, L25, L26])
