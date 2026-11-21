"""Unit 17: Lesson 6 (Unit 1 review) activities: topics and core patterns, vocabulary and grammar review, skill integration
and using Chinese in context. Everything readable in the book is here; the audio activities and the board image are not."""
import re

from zh_auto import *

PART = ["吗", "们", "呢"]
STOP = {"a", "an", "the", "of", "for", "to", "be", "in", "or", "and", "from", "at", "with", "your", "you"}


def words(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if w not in STOP}


def pick(i, items, k=3, step=5):
    """k distractor meanings from the same list that share no word with the right answer or with each other."""
    en = items[i][2]
    out, used = [], words(en)
    n = len(items)
    for s in range(1, n):
        c = items[(i + s * step) % n]
        if c[2] == en or (words(c[2]) & used):
            continue
        out.append(c)
        used |= words(c[2])
        if len(out) == k:
            break
    assert len(out) == k, (items[i][0], en)
    return out


def rows_py(pairs, fixes=None):
    """[(hanzi, English)] -> [(hanzi, auto pinyin, English)]"""
    fixes = fixes or {}
    return [(hz, auto_py(hz, fixes.get(hz)), en) for hz, en in pairs]


# ------------------------------------------------------------------ 1. objectives, topics and core patterns
PATTERNS = [("做什么工作？", "occupation", "g"), ("……是哪国人？", "nationality", "h"), ("……几月几号？", "birthdate", "e"),
            ("……在哪儿？", "a city’s location", "f"), ("……多大？", "age", "a"), ("……是多少？", "phone number", "b"),
            ("你家有几口人？", "how many members are in one’s family", "d"), ("这是……", "introducing a third party", "c")]
TOPIC_LONG = {"occupation": "Asking one’s occupation", "nationality": "Asking one’s nationality", "birthdate": "Asking one’s birthdate",
              "a city’s location": "Asking a city’s location", "age": "Asking about one’s age", "phone number": "Asking one’s phone number",
              "how many members are in one’s family": "Asking how many members are in one’s family", "introducing a third party": "Introducing a third party"}
PAT_ROWS = [(hz, auto_py(hz), f"{letter}. {TOPIC_LONG[t]}") for hz, t, letter in PATTERNS]


def others(items, i, k=3, step=3):
    """k different items other than items[i], spread around the list."""
    out, seen, j = [], {i}, 1
    while len(out) < k:
        idx = (i + step * j) % len(items)
        j += 1
        if idx in seen:
            idx = next(x for x in range(len(items)) if x not in seen and x != i) if j > len(items) else idx
            if idx in seen:
                continue
        seen.add(idx)
        out.append(items[idx])
    return out


L1_EX = []
for i, (hz, topic, letter) in enumerate(PATTERNS):
    L1_EX.append(M(f"Which core pattern do you use for “{TOPIC_LONG[topic].lower()}”?", hz, [p[0] for p in others(PATTERNS, i)], f"{hz} is the pattern for {TOPIC_LONG[topic].lower()} (the book’s {letter})."))
for i, (hz, topic, letter) in enumerate(PATTERNS):
    L1_EX.append(M(f"What does the pattern {hz} ask about?", topic, [p[1] for p in others(PATTERNS, i, step=5)], f"{hz}: {TOPIC_LONG[topic].lower()}."))

L1 = lesson(
    "Unit 1 review: objectives, topics and core patterns",
    "第六课 单元复习 · 做什么工作？ · ……几月几号？ · 你家有几口人？",
    requires=[],
    cards=[
        card("Review: Meeting People (第六课 单元复习)",
             "The review lesson is designed to help you review and consolidate what you learned in Lessons 1 to 5. When you have completed it, you will be able to:\n"
             "1. Better understand conversations between Chinese speakers, and short written passages with basic information on: greetings and introductions; personal identification; birthdate and birthplace; family; hometown.\n"
             "2. Become familiar with the language and non-language features tied to those topics: core vocabulary and patterns; grammar; socially appropriate terms; embedded cultural knowledge.\n"
             "3. Use these language features to complete a variety of language exercises and conduct a variety of communicative activities."),
        card("Topics and core patterns, Activity 1 (Writing)",
             "The book asks you to recall the topics and sub-topics of the unit and fill in a table with four sub-topics for each of Self, Family, Hometown and City. The book leaves the table empty, so here is one way to fill it from Lessons 1 to 5:\n"
             "Self: name, age, birthdate, phone number.\n"
             "Family: parents, siblings, jobs, how many people.\n"
             "Hometown: where it is, the population, the weather, the people.\n"
             "City: location, size, the four seasons, the climate.\n"
             "Try to say a sentence about each one aloud."),
        card("Activity 2 (Reading and Speaking): match the topics with the core patterns",
             "Match the topics with the core patterns first. Then pair up and ask each other these questions in Chinese. The letters are the book’s.",
             tables=[wtable(PAT_ROWS, headers=("Core pattern", "Pinyin", "Topic (the book’s letter)"))]),
    ],
    exercises=L1_EX,
)

# ------------------------------------------------------------------ 2. vocabulary review: phrases and categories
CATS = {
    "Work (工作)": [("上尉", "captain"), ("教书", "teach"), ("医生", "doctor"), ("工程师", "engineer"), ("主妇", "housewife")],
    "Weather (天气)": [("刮风", "windy"), ("凉快", "cool"), ("闷热", "sultry"), ("下雾", "foggy"), ("阴天", "cloudy")],
    "Family (家人)": [("父母", "parents"), ("二姐", "second elder sister"), ("爷爷", "grandfather"), ("孙子", "grandson"), ("兄弟姐妹", "siblings")],
    "School (学校)": [("大学生", "college student"), ("班长", "class leader"), ("军校", "military school"), ("同学", "classmate"), ("日文系", "Japanese Department")],
}
CAT_NAMES = list(CATS)
cat_cards_tables = []
L2_EX = []
for cname, items in CATS.items():
    cat_cards_tables.append(wtable(rows_py(items), headers=("Word", "Pinyin", "Meaning"), title=cname))
allw = [(hz, en, cname) for cname, items in CATS.items() for hz, en in items]
for k, (hz, en, cname) in enumerate(allw):
    py = auto_py(hz)
    L2_EX.append(mean(hz, py, en, [w[1] for w in others(allw, k, step=7)]))
    L2_EX.append(M(f"In the book’s categories, where does {hz} ({en}) belong?", cname, [c for c in CAT_NAMES if c != cname], f"{hz} ([[{py}]]) goes under {cname}."))

PHRASES = [("军人", "soldier"), ("军校", "military school"), ("海军", "navy"), ("空军", "air force"), ("陆军", "army"), ("军官", "officer"), ("军衔", "military rank"),
           ("中国", "China"), ("美国", "America"), ("韩国", "Korea"), ("国防语言学院", "Defense Language Institute"), ("哪国人", "which country’s person"),
           ("今天", "today"), ("天气", "weather"), ("春天", "spring"), ("夏天", "summer"), ("秋天", "autumn"), ("冬天", "winter"), ("阴天", "cloudy"), ("晴天", "sunny"), ("天津", "Tianjin")]
L2_EX += [mean(hz, auto_py(hz), en, [w[1] for w in others(PHRASES, k, step=6)]) for k, (hz, en) in enumerate(PHRASES) if hz in ("军官", "军衔", "哪国人", "国防语言学院")]

L2 = lesson(
    "Unit 1 review: phrases with 军 国 天, and the four categories",
    "军 · 国 · 天 · 工作 · 天气 · 家人 · 学校",
    requires=[],
    cards=[
        card("Vocabulary and Grammar, Activity 1 A: brainstorm phrases",
             "The book has you break into groups of three and brainstorm phrases that contain 军, 国 and 天. Your teacher sets a time limit, and the group with the most phrases wins. Here are many of the phrases you have met in Unit 1.",
             tables=[wtable(rows_py(PHRASES), headers=("Phrase", "Pinyin", "Meaning"), title="Phrases with 军, 国 and 天")]),
        card("Activity 1 B: write the words in their correct categories",
             "The book lists these 20 words in one jumbled box: 大学生 上尉 班长 父母 二姐 刮风 爷爷 主妇 医生 军校 凉快 教书 工程师 孙子 闷热 下雾 同学 阴天 日文系 兄弟姐妹. Sort them into four columns: Work, Weather, Family, School.",
             tables=cat_cards_tables),
        card("Activity 1 C",
             "Check your answers with your group. Choose the four most difficult words and make Chinese sentences with them out loud; your group members translate your sentences."),
    ],
    exercises=L2_EX,
)

# ------------------------------------------------------------------ 3. questions and sentence order
QA = [
    ("蒙特雷的夏天不太热，经常下雾。", "Monterey’s summer is not too hot and often foggy.", "不太热，经常下雾", "蒙特雷的夏天怎么样？", "How is Monterey’s summer?",
     ["蒙特雷有多少人？", "你爸爸在哪儿工作？", "你是几月几号来的？"]),
    ("我爸爸在电脑公司工作。", "My father works at a computer company.", "电脑公司", "你爸爸在哪儿工作？", "Where does your father work?",
     ["你爸爸多大？", "蒙特雷的夏天怎么样？", "你的老家在德州的哪儿？"]),
    ("我的老家在德州的南部。", "My hometown is in the south of Texas.", "南部", "你的老家在德州的哪儿？", "Where in Texas is your hometown?",
     ["你是几月几号来的？", "你妈妈做什么工作？", "蒙特雷有多少人？"]),
    ("我是三月五号来国防语言学院的。", "I came to the Defense Language Institute on March 5.", "三月五号", "你是几月几号来国防语言学院的？", "What day did you come to the Defense Language Institute?",
     ["你的老家在德州的哪儿？", "你爸爸在哪儿工作？", "蒙特雷有多少人？"]),
    ("我妈妈是陆军少校。", "My mother is an Army major.", "陆军少校", "你妈妈做什么工作？", "What does your mother do?",
     ["你妈妈多大？", "你爸爸在哪儿工作？", "蒙特雷的夏天怎么样？"]),
    ("蒙特雷有两万八千多人。", "Monterey has more than 28,000 people.", "两万八千多人", "蒙特雷有多少人？", "How many people does Monterey have?",
     ["蒙特雷的夏天怎么样？", "你的老家在德州的哪儿？", "你爸爸多大？"]),
]
ORDER = [
    ("这 / 谁 / 是 / 同学 / 位？", "Who is this student?", "这位同学是谁？", ["这谁是同学位？", "谁这位是同学？", "是这位谁同学？"]),
    ("也 / 的 / 你太太 / 是 / 中文系 / 吗 / 老师？", "Is your wife also a teacher in the Chinese Department?", "你太太也是中文系的老师吗？", ["你太太是也中文系的老师吗？", "也你太太是老师中文系的吗？", "你太太也是老师中文系的吗？"]),
    ("你 / 的 / 都 / 什么 / 兄弟姐妹 / 做 / 工作？", "What kinds of jobs do your siblings have?", "你的兄弟姐妹都做什么工作？", ["你的兄弟姐妹做都什么工作？", "你的都兄弟姐妹做什么工作？", "什么你的兄弟姐妹都做工作？"]),
    ("一个 / 老家 / 纽约州 / 我 / 的 / 东部 / 在 / 的 / 小城市", "My hometown is in a small city in eastern New York State.", "我的老家在纽约州东部的一个小城市。", ["我的老家在东部纽约州的一个小城市。", "我的老家纽约州在东部的一个小城市。", "我老家的在纽约州东部一个的小城市。"]),
    ("东部 / 人口 / 九十 / 都 / 住 / 在 / 百分之 / 多 / 的", "More than 90% of the population live on the East Coast.", "百分之九十多的人口都住在东部。", ["九十百分之多的人口都住在东部。", "百分之九十多的人口住都在东部。", "百分之多九十的人口都住在东部。"]),
    ("重庆 / 蒙特雷 / 那么 / 夏天 / 没有 / 的 / 凉快。", "Chongqing’s summer is not as cool as Monterey’s.", "重庆的夏天没有蒙特雷的那么凉快。", ["重庆的夏天没有那么蒙特雷的凉快。", "重庆的夏天蒙特雷的没有那么凉快。", "重庆的夏天没有的蒙特雷那么凉快。"]),
]
L3_EX = []
for a, aen, under, q, qen, wrong in QA:
    L3_EX.append(M(f"Activity 2 C: which question goes with the answer “{a.replace('两万八千多人', '2万八千多人')}”, if the underlined part is “{under}” ({qen.lower().rstrip('?')})?", q, wrong,
                   f"{q} ({qen}) is answered by “{a}”.", ))
for scr, en, ans, wrong in ORDER:
    L3_EX.append(M(f"Reorder the words into a correct sentence: {scr}  ({en})", ans, wrong, f"The correct order is {ans} ({en})."))

L3 = lesson(
    "Unit 1 review: write the questions and reorder the sentences",
    "蒙特雷的夏天怎么样？ · 这位同学是谁？ · 重庆的夏天没有蒙特雷的那么凉快。",
    requires=[],
    cards=[
        card("Vocabulary and Grammar, Activity 2: questions and answers",
             "In the book you listen to six questions and write both the questions and your answers (audio, not included), then you read six answers and write the questions that fit the underlined information. The six answers are below, with the information the book underlines, and a model question for each. The book leaves the blanks empty, so the questions here are suggestions. In the book the last answer writes “2”; here it is spelled out as 两万八千多人.",
             examples=[x for a, aen, under, q, qen, wrong in QA for x in (D(f"问：{q}", qen), D(f"答：{a}", aen))]),
        card("Activity 3: reorder the words into correct sentences",
             "The book gives six jumbled sentences with the English translation. Reorder the words, check your answers with a partner, then take turns reading the sentences aloud. Here are the six correct sentences.",
             examples=[D(ans, en) for scr, en, ans, wrong in ORDER]),
    ],
    exercises=L3_EX,
)

# ------------------------------------------------------------------ 4. Activity 4: the eleven blanks
BANK = [("多", "duo1", "how (+ adjective), more than"), ("位", "wei4", "measure word for people"), ("多少", "duo1 shao3", "how many"), ("日文系", "ri4 wen2 xi4", "Japanese Department"),
        ("叫", "jiao4", "be called"), ("几", "ji3", "how many (a small number)"), ("不", "bu4", "no, not"), ("呢", "ne5", "question particle (and you?)"),
        ("贵姓", "gui4 xing4", "your surname (polite)"), ("都", "dou1", "both, all"), ("也", "ye3", "also")]
DIALOG4 = [
    ("A", "请问，您贵姓？", "Excuse me, what is your surname?"),
    ("B", "我姓王，叫大力。你呢？", "My surname is Wang, and I’m called Dali. And you?"),
    ("A", "我叫张英。您是中文系的学生吗？", "I’m called Zhang Ying. Are you a student in the Chinese Department?"),
    ("B", "对。你也是中文系的学生吗？", "Yes. Are you also a student in the Chinese Department?"),
    ("A", "不，我是日文系的学生。", "No, I’m a student in the Japanese Department."),
    ("B", "你们日文系的学生都是军人吗？", "Are all the students in your Japanese Department military?"),
    ("A", "不，我们日文系有一个学生不是军人。", "No, one student in our Japanese Department is not military."),
    ("B", "你们日文系有多少学生？", "How many students are there in your Japanese Department?"),
    ("A", "二十多个。", "Twenty-some."),
    ("B", "你们有几位老师？", "How many teachers do you have?"),
    ("A", "四位。", "Four."),
]
BLANKS = [  # (prompt with one ___, answer, three wrong words that make an impossible sentence, why)
    ("甲：请问，您___？", "贵姓", ["多少", "几", "位"], "请问，您贵姓？ asks someone’s surname politely."),
    ("乙：我姓王，叫大力。你___？", "呢", ["位", "几", "多"], "你呢？ means “and you?”."),
    ("甲：我___张英。您是中文系的学生吗？", "叫", ["呢", "位", "日文系"], "我叫张英 means “I’m called Zhang Ying”."),
    ("乙：对。你___是中文系的学生吗？", "也", ["呢", "位", "多"], "你也是… means “are you also…”."),
    ("甲：不，我是___的学生。", "日文系", ["贵姓", "呢", "多少"], "日文系的学生 is “a student of the Japanese Department”."),
    ("乙：你们日文系的学生___是军人吗？", "都", ["位", "呢", "叫"], "都 means “all”."),
    ("甲：___，我们日文系有一个学生不是军人。", "不", ["位", "呢", "几"], "不 answers “no” to the question."),
    ("乙：你们日文系有___学生？", "多少", ["贵姓", "呢", "不"], "多少 asks “how many”."),
    ("甲：二十___个。", "多", ["呢", "贵姓", "叫"], "二十多个 is “twenty-some”."),
    ("乙：你们有___位老师？", "几", ["呢", "贵姓", "叫"], "几位 asks “how many” of people."),
    ("甲：四___。", "位", ["呢", "贵姓", "日文系"], "四位 is “four (people)”."),
]
L4 = lesson(
    "Unit 1 review: key grammar points in a dialog",
    "贵姓 · 呢 · 叫 · 也 · 日文系 · 都 · 不 · 多少 · 多 · 几 · 位",
    requires=[],
    cards=[
        card("Vocabulary and Grammar, Activity 4 (Reading and Writing)",
             "The book gives you eleven words (numbered 1 to 11) and an eleven-blank dialog between two students, and you write the number of the word in the blank where it belongs. The word list and the finished dialog are here. (The book’s speakers A and B are written 甲 and 乙.)",
             tables=[wtable([(hz, py, en) for hz, py, en in BANK])], examples=dlg(DIALOG4)),
    ],
    exercises=[F(p, a, w, why) for p, a, w, why in BLANKS] + [mean(hz, py, en, [b[2] for b in others([x for x in BANK if x[0] == hz or "how" not in x[2]], [x[0] for x in BANK if x[0] == hz or "how" not in x[2]].index(hz), step=4)]) for k, (hz, py, en) in enumerate(BANK)],
)

# ------------------------------------------------------------------ 5. patterns for the seasons and the family
SEASON_EX = [
    ("上海的夏天跟重庆的夏天一样热。", "Shanghai’s summer is as hot as Chongqing’s."),
    ("蒙特雷的夏天没有重庆那么热。", "Monterey’s summer is not as hot as Chongqing’s."),
    ("重庆的夏天比蒙特雷热。", "Chongqing’s summer is hotter than Monterey’s."),
    ("因为我喜欢滑雪，所以我喜欢冬天。", "Because I like to ski, I like winter."),
    ("蒙特雷的春天不冷也不热。", "Monterey’s spring is neither cold nor hot."),
    ("夏天可以游泳。", "In summer you can swim."),
]
FAMILY_EX = [
    ("你家有几口人？", "How many people are in your family?"),
    ("你姐姐是老师还是医生？", "Is your older sister a teacher or a doctor?"),
    ("你哥哥多大？", "How old is your older brother?"),
    ("你妈妈做什么工作？", "What does your mother do?"),
    ("你爸爸是在哪儿出生的？", "Where was your father born?"),
    ("他们住在哪儿？", "Where do they live?"),
    ("我哥哥是陆军上尉，我姐姐是老师。", "My older brother is an Army captain; my older sister is a teacher."),
]
L5 = lesson(
    "Unit 1 review: comparing seasons and talking about your family",
    "跟……一样 · 没有……那么 · 比 · 因为 · 不……也不…… · 可以 · 还是",
    requires=[],
    cards=[
        card("Activity 5 (Writing and Speaking): compare the four seasons of your hometown with Monterey",
             "Pair up and compare the four seasons of your hometown with those of Monterey. Explain your reasoning by using all of these grammar patterns: 跟……（不）一样, 没有……这么（那么）, ……比……, 因为……, 不……也不……, 可以. Your description should start with: 我的老家在…… (“My hometown is in …”). Here is one example sentence for each pattern.",
             examples=[D(z, e) for z, e in SEASON_EX]),
        card("Activity 6 (Listening, Writing and Speaking): your partner’s family",
             "A. Pair up and ask for your partner’s family information with all of these patterns (you need not follow the order): ……几……, ……谁, ……做什么？ ……多大？ 在哪儿……？ 是……的……, ……还是…… .\n"
             "B. Take notes while you ask. Then report your classmate’s family information to the class, starting your description with: …是…… . Here are some question and answer sentences built from those patterns.",
             examples=[D(z, e) for z, e in FAMILY_EX]),
    ],
    exercises=[
        F("蒙特雷的夏天没有重庆___热。", "那么", PART, "没有……那么 means “not as … as”."),
        F("重庆的夏天___蒙特雷热。", "比", PART, "A 比 B + adjective means “A is more … than B”."),
        F("你姐姐是老师___医生？", "还是", PART, "A 还是 B asks “A or B?”."),
        F("蒙特雷的春天不冷___不热。", "也", PART, "不……也不…… means “neither … nor …”."),
        F("夏天___以游泳。", "可", PART, "可以 means “can”."),
        F("你家有___口人？", "几", PART, "你家有几口人？ asks how many people are in the family."),
        M("Which pattern means “as … as”?", "跟……一样", ["没有……那么", "比", "因为……"], "跟……一样 means “the same as”."),
        M("Which pattern means “not as … as”?", "没有……那么", ["跟……一样", "不……也不……", "可以"], "没有……那么 means “not as … as”."),
        M("Which pattern means “neither … nor …”?", "不……也不……", ["跟……一样", "没有……那么", "是……的"], "不……也不…… means “neither … nor …”."),
        M("Which pattern means “because”?", "因为……", ["比", "还是", "可以"], "因为 means “because”."),
        M("Which pattern means “A or B?” in a question?", "……还是……", ["……比……", "因为……", "没有……那么"], "还是 offers a choice in a question."),
        M("Which pattern means “can”?", "可以", ["因为……", "比", "还是"], "可以 means “can, may”."),
    ],
)

# ------------------------------------------------------------------ 6. board game
BOARD = [
    ("从这里开始", "Start here"), ("纽约", "New York"), ("介绍两个中国的城市", "Introduce two Chinese cities"), ("你的手机号码", "Your cellphone number"),
    ("父母亲的工作", "Your parents’ jobs"), ("家人", "Your family"), ("你的教官", "Your instructor"), ("中文系", "The Chinese Department"),
    ("老家的天气", "The weather in your hometown"), ("老家的人口", "The population of your hometown"), ("最喜欢的季节", "Your favorite season"),
    ("国防语言学院", "The Defense Language Institute"), ("一个中学老师", "A middle-school teacher"), ("说三种语言", "Name three languages"),
    ("最喜欢的工作", "Your favorite job"), ("蒙特雷的气候", "Monterey’s climate"), ("为什么学中文", "Why you study Chinese"),
    ("夏天最喜欢做什么", "What you like to do most in summer"), ("美国和中国的首都", "The capitals of the U.S. and China"), ("你的小学", "Your elementary school"),
    ("说三个军衔", "Name three military ranks"), ("你的出生地", "Your birthplace"), ("一个男的朋友/同学", "A male friend or classmate"),
    ("一个女的朋友/同学", "A female friend or classmate"), ("兄弟姐妹", "Your brothers and sisters"), ("问你的同学三个问题", "Ask your classmates three questions"),
    ("一个基地", "A base"), ("一个好朋友", "A good friend"), ("四季", "The four seasons"), ("有意思的东西", "Something interesting"), ("一张照片", "A photo"),
    ("说三个国家", "Name three countries"), ("用“比”造一个句子", "Make a sentence with 比"), ("教你英文的人", "The person who taught you English"),
    ("很想住的城市", "A city you would love to live in"), ("你的生日", "Your birthday"), ("你的身体怎么样", "How your health is"), ("一个岁数很大的人", "A very old person"),
    ("一个好玩的城市", "A fun city"), ("和班上同学一样的地方", "How you are the same as your classmates"), ("今年", "This year"),
    ("陆军和空军不一样的地方", "How the Army and the Air Force differ"), ("你住过的州", "The states you have lived in"),
    ("说什么都没关系", "Yellow square: say anything you like"), ("随意", "Orange square: your partner picks any topic"), ("再玩一次？", "Play again?"),
]
BOARD_FIX = {"教你英文的人": {0: "jiao1"}, "一个岁数很大的人": {3: "shu5"}}
BOARD_ROWS = rows_py(BOARD, BOARD_FIX)
BOARD_EX = []
for k, (hz, py, en) in enumerate(BOARD_ROWS):
    if hz in ("从这里开始", "说什么都没关系", "随意", "再玩一次？"):
        continue
    BOARD_EX.append(mean(hz, py, en, [w[2] for w in others(BOARD_ROWS[1:40], (k - 1) % 39, step=4) if w[2] != en]))

L6 = lesson(
    "Unit 1 review: the board game",
    "你的出生地 · 老家的天气 · 说三种语言 · 用“比”造一个句子 · 请告诉我们……",
    requires=[],
    cards=[
        card("Activity 7 (Reading, Speaking and Listening): Board Game",
             "Separate into groups of three. Each member throws a die. Using the layout of the board, each student moves the number of spaces equal to the number thrown and answers the question in that square. All answers must be in complete sentences. Some boxes may need more than one sentence. If your die falls on a purple box, you can pick any topic for your response. If it falls on an orange square, your partner may choose any topic for your reply. "
             "The board itself is a large picture (not included here); its squares are listed below in order. The book writes 2 and 3 as digits in two squares; they are written out here. The centre of the board says 请告诉我们（你的）…… (“Please tell us (your) …”).",
             tables=[wtable(BOARD_ROWS, headers=("Square", "Pinyin", "What to talk about"))]),
    ],
    exercises=BOARD_EX,
)

# ------------------------------------------------------------------ 7. Skill Integration: 马小文
MA = [
    ("我姓马，叫小文，今年十七岁。", "My surname is Ma, I’m called Xiaowen, and I am seventeen this year."),
    ("我的家乡在中国山东省。", "My hometown is in Shandong Province, China."),
    ("我的父母都是在山东一个小城市出生的。", "My parents were both born in a small city in Shandong."),
    ("那里人口不多，只有两万五千多人。", "The population there is not large, only more than 25,000 people."),
    ("城里没有大学，只有一所中学和一所小学，我是在美国加州出生的。", "There is no college in the city, only one middle school and one elementary school. I was born in California, U.S.A."),
    ("我问我父母：“我是中国人还是美国人？”", "I asked my parents: “Am I Chinese or American?”"),
    ("我父母说：“我们的老家在中国，我们都是中国人。”", "My parents said: “Our hometown is in China; we are all Chinese.”"),
    ("我想，我是在美国出生的，我是中国人，也是美国人。", "I think: I was born in America; I am Chinese, and also American."),
]
MA_WORDS = [("家乡", "jia1 xiang1", "hometown"), ("山东", "shan1 dong1", "Shandong (province)"), ("省", "sheng3", "province"), ("所", "suo3", "measure word for schools"),
            ("想", "xiang3", "think, want to"), ("出生", "chu1 sheng1", "be born"), ("人口", "ren2 kou3", "population"), ("还是", "hai2 shi4", "or (in a question)"), ("加州", "jia1 zhou1", "California")]
L7 = lesson(
    "Unit 1 review: reading 马小文’s passage",
    "我姓马，叫小文 · 家乡 · 一所中学和一所小学 · 我是中国人还是美国人？",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Reading and Writing)",
             "A. Read the passage and fill in the table in English with the essential elements of information: the author’s name, age and birthplace, his parents’ birthplace, the main features of the parents’ birthplace, and the main topic of discussion between the author and his parents.\nB. Summarize the passage orally.\nThe passage (the book writes the numbers 17 and 25,000 as digits; they are written out here):",
             examples=[D(z, e) for z, e in MA]),
        card("New words in the passage", "Words you need to read the passage.", tables=[wtable(MA_WORDS)]),
    ],
    exercises=[
        M("What is the author’s name?", "Ma Xiaowen", ["Ma Xiaoying", "Wang Dali", "Zhang Ying"], "我姓马，叫小文: surname Ma, given name Xiaowen."),
        M("How old is the author?", "17", ["27", "7", "70"], "今年十七岁: seventeen this year."),
        M("Where was the author born?", "California, U.S.A.", ["Shandong, China", "Texas", "Beijing"], "我是在美国加州出生的."),
        M("Where were the author’s parents born?", "A small city in Shandong, China", ["California", "Shanghai", "A large city in Texas"], "我的父母都是在山东一个小城市出生的."),
        M("What is the population of the parents’ birthplace?", "More than 25,000", ["More than 52,000", "About 2,500", "More than 250,000"], "只有两万五千多人: only more than 25,000."),
        M("What schools does the parents’ birthplace have?", "One middle school and one elementary school, but no college", ["Three colleges", "Only a college", "No schools at all"], "城里没有大学，只有一所中学和一所小学."),
        M("What do the author and his parents discuss?", "Whether he is Chinese or American", ["Where to move", "His school grades", "His phone number"], "我问我父母：我是中国人还是美国人？"),
        M("What do the parents say?", "Our hometown is in China; we are all Chinese", ["You are only American", "We are all American", "We have no hometown"], "我们的老家在中国，我们都是中国人。"),
        M("What does the author conclude?", "He is both Chinese and American", ["He is only Chinese", "He is only American", "He is neither"], "我是中国人，也是美国人。"),
        F("城里没有大学，只有一___中学。", "所", PART, "所 is the measure word for schools."),
        F("我的家乡___中国山东省。", "在", PART, "在 says where something is."),
        mean("家乡", "jia1 xiang1", "hometown", ["hospital", "city", "base"]),
        mean("所", "suo3", "measure word for schools", ["measure word for photos", "measure word for people", "measure word for family members"]),
        mean("想", "xiang3", "think, want to", ["ask", "be born", "teach"]),
    ],
)

# ------------------------------------------------------------------ 8. Skill Integration: 谢英, 李红 and 刘国华
D3 = [
    ("谢", "李红，你身体好吗？", "Li Hong, how is your health?"),
    ("李", "很好！谢英，你身体怎么样？", "Very good! Xie Ying, how is your health?"),
    ("谢", "很好。李红，这是我的男朋友刘国华。国华，这是我中学的同学李红。", "Very good. Li Hong, this is my boyfriend Liu Guohua. Guohua, this is Li Hong, my middle-school classmate."),
    ("李", "刘先生，您好！", "Mr. Liu, how do you do!"),
    ("刘", "李小姐，您好！", "Miss Li, how do you do!"),
    ("李", "刘先生，您在哪里工作？", "Mr. Liu, where do you work?"),
    ("刘", "我是医生，在医院工作。这是我的名片。", "I’m a doctor, and I work at a hospital. This is my business card."),
    ("李", "谢谢。我在学校里教书，我没有名片！", "Thank you. I teach at a school; I don’t have a business card!"),
    ("刘", "没关系！您工作忙吗？", "No problem! Is your work busy?"),
    ("李", "很忙。您呢？", "Very busy. And you?"),
    ("刘", "不太忙。李小姐是哪儿的人？", "Not too busy. Where is Miss Li from?"),
    ("李", "我跟谢英都是南方人。刘先生是不是北京人？", "Xie Ying and I are both Southerners. Is Mr. Liu from Beijing?"),
    ("刘", "不是。我是天津人。", "No. I’m from Tianjin."),
]
D3_WORDS = [("身体", "shen1 ti3", "health, body"), ("男朋友", "nan2 peng2 you5", "boyfriend"), ("先生", "xian1 sheng5", "Mr., sir"), ("小姐", "xiao3 jie3", "Miss"),
            ("名片", "ming2 pian4", "business card"), ("没关系", "mei2 guan1 xi5", "no problem"), ("忙", "mang2", "busy"), ("南方人", "nan2 fang1 ren2", "Southerner"), ("天津", "tian1 jin1", "Tianjin")]
L8 = lesson(
    "Unit 1 review: 谢英, 李红 and 刘国华 meet",
    "李红，你身体好吗？ · 这是我的男朋友刘国华 · 我是天津人",
    requires=[],
    cards=[
        card("Skill Integration, Activity 3 (Reading and Speaking)",
             "Work in groups of three. Read the following conversation and answer the six questions aloud, using Chinese expressions from the conversation when needed to give examples. The questions: 1. How do the two women greet each other? 2. In your opinion, why do they greet each other this way? 3. Who is Liu Guohua? What does he do? 4. How does he greet Ms. Li? Why? 5. What is Ms. Li’s occupation? What is her workload like? 6. Are all three people from southern China?",
             examples=dlg(D3)),
        card("Words in the conversation", "Some of these are new here.", tables=[wtable(D3_WORDS)]),
    ],
    exercises=[
        M("How do the two women greet each other?", "By asking about each other’s health (身体好吗？)", ["By asking each other’s age", "By exchanging business cards", "By asking where the other works"], "李红，你身体好吗？ — 谢英，你身体怎么样？"),
        M("Why do the two women greet each other this way?", "They are old classmates and close friends, so they are informal and caring", ["They are meeting for the first time", "They are at work", "They are in the military"], "They were middle-school classmates, so they greet each other warmly, not formally."),
        M("Who is Liu Guohua?", "Xie Ying’s boyfriend, a doctor who works at a hospital", ["Li Hong’s husband, a teacher", "A student from Tianjin", "Xie Ying’s teacher"], "这是我的男朋友刘国华。我是医生，在医院工作。"),
        M("How does Liu Guohua greet Li Hong?", "李小姐，您好！ — politely, because they have just met", ["李红，你好吗？ — as an old friend", "老师，你好！", "同学，你好！"], "They have just met, so he uses 小姐 and the polite 您."),
        M("What is Li Hong’s occupation and workload?", "She teaches at a school and is very busy", ["She is a doctor and not busy", "She is an engineer and not busy", "She is a housewife and very busy"], "我在学校里教书。很忙。"),
        M("Are all three people from southern China?", "No: the two women are Southerners, but Liu Guohua is from Tianjin", ["Yes, all three", "No, nobody is", "Only Liu Guohua is a Southerner"], "我跟谢英都是南方人。… 我是天津人。"),
        M("What does Li Hong say when Liu Guohua gives her his card?", "She thanks him and says she teaches at a school and has no card", ["She gives him her card", "She says she is a doctor too", "She asks for his phone number"], "谢谢。我在学校里教书，我没有名片！"),
        mean("名片", "ming2 pian4", "business card", ["photo", "map", "phone number"]),
        mean("没关系", "mei2 guan1 xi5", "no problem", ["thank you", "excuse me", "welcome"]),
        mean("小姐", "xiao3 jie3", "Miss", ["Mr.", "teacher", "classmate"]),
        mean("男朋友", "nan2 peng2 you5", "boyfriend", ["girlfriend", "classmate", "husband"]),
        mean("忙", "mang2", "busy", ["cool", "cold", "fun"]),
    ],
)

# ------------------------------------------------------------------ 9. measure words, and the listening activities
MW = [("七", "张", "照片", "photo", ["位", "口", "所"]), ("两", "个", "姐姐", "older sister", ["张", "所", "家"]), ("八", "张", "地图", "map", ["位", "口", "所"]),
      ("四", "个", "中国人", "Chinese person", ["张", "所", "家"]), ("五", "家", "银行", "bank", ["位", "口", "张"]), ("六", "个", "学生", "student", ["张", "所", "家"]),
      ("一", "个", "哥哥", "older brother", ["张", "所", "家"]), ("三", "位", "老师", "teacher", ["口", "张", "所"]), ("九", "所", "学校", "school", ["位", "口", "张"]),
      ("十", "张", "名片", "business card", ["位", "口", "所"])]
MW_WORDS = [("张", "zhang1", "measure word for flat things (photos, maps, cards)"), ("个", "ge4", "general measure word"), ("位", "wei4", "polite measure word for people"),
            ("口", "kou3", "measure word for family members"), ("家", "jia1", "measure word for families, companies, banks"), ("所", "suo3", "measure word for schools")]
L9_EX = []
for n, mw, noun, en, wrong in MW:
    L9_EX.append(F(f"{n}___{noun}", mw, wrong, f"{n}{mw}{noun}: “{mw}” is the measure word for {en}.".replace("is the measure word for", "goes with")))
L9_EX += [mean(hz, py, en, [b[2] for b in others(MW_WORDS, k, step=2)]) for k, (hz, py, en) in enumerate(MW_WORDS)]
L9 = lesson(
    "Unit 1 review: measure words, and the listening activities",
    "七张照片 · 两个姐姐 · 五家银行 · 三位老师 · 九所学校 · 十张名片",
    requires=[],
    cards=[
        card("Skill Integration, Activity 6 (Reading and Writing): measure words",
             "Fill in each blank with the correct measure word. The book gives ten phrases: 七__照片, 两__姐姐, 八__地图, 四__中国人, 五__银行, 六__学生, 一__哥哥, 三__老师, 九__学校, 十__名片. The measure words you need for Unit 1 are here.",
             tables=[wtable(MW_WORDS)], examples=[D(f"{n}{mw}{noun}", f"{n} {en}s") for n, mw, noun, en, wrong in MW]),
        card("The listening activities (audio is not included)",
             "Several Unit 1 review activities are recordings, so they cannot be reproduced here. They are, in the book’s order:\n"
             "• Vocabulary and Grammar, Activity 2 A: six spoken questions, to write down with your own answers.\n"
             "• Skill Integration, Activity 2: Sergeant Gao’s biographical information, to take notes in English and then report in Chinese.\n"
             "• Activity 4: a dialog between two students, to answer three questions (how many students and teachers in the Japanese Department, how many students in the Chinese Department), then ask your instructor about the Chinese Department: number of students, number of teachers, number of civilian students, number of military students.\n"
             "• Activity 5: numbers of people in the U.S. who speak Russian (俄文), Japanese (日文), Chinese (中文) and Spanish (西班牙文) at home; write the numbers in Arabic numerals.\n"
             "• Activity 7: two reports; fill in given name, surname, rank, service, origin, city of residence and phone number, in pinyin.\n"
             "• Using Chinese in Context: three men giving personal data (李大年, 王军, 陈力), an overheard conversation, a Xinhua News Agency interview with a soldier, and the SCOLA conversation among three people. Your teacher can play the recordings in class."),
    ],
    exercises=L9_EX,
)

# ------------------------------------------------------------------ 10. profile and ad
PROFILE = [("姓名", "马小英", "name: 马小英 (Ma Xiaoying)"), ("性别", "女", "gender: 女 (female)"), ("年龄", "二十九", "age: 29"), ("文化", "大学", "education: university"),
           ("职业", "中学教师", "occupation: middle-school teacher"), ("父母职业", "大学老师", "parents’ occupation: university teachers"),
           ("兄弟姐妹", "一个弟弟（中学生）", "siblings: a younger brother (a middle-school student)"),
           ("觅", "年龄：二十六到五十；文化：大学；职业：老师、医生、工程师、军官", "looking for: age 26–50; university education; a teacher, doctor, engineer or officer")]
PROF_WORDS = [("个人资料", "ge4 ren2 zi1 liao4", "personal record, profile"), ("姓名", "xing4 ming2", "name"), ("性别", "xing4 bie2", "gender"), ("年龄", "nian2 ling2", "age"), ("文化", "wen2 hua4", "education, culture"),
              ("职业", "zhi2 ye4", "occupation"), ("觅", "mi4", "look for"), ("教师", "jiao4 shi1", "teacher"), ("军官", "jun1 guan1", "military officer"), ("女", "nv3", "female"), ("男", "nan2", "male")]
AD = [
    ("征婚广告", "Marriage-seeking ad (征婚广告)"),
    ("刘东，三十九岁，身高一米八，上海人，工程师，大学毕业。", "Liu Dong, 39 years old, 1.80 meters tall, from Shanghai, an engineer, a college graduate."),
    ("在广州市工作。离异。有一个八岁的女儿。", "Works in Guangzhou. Divorced. Has an eight-year-old daughter."),
    ("本人身体很好。爱好是看书、看电影。", "In very good health. Hobbies are reading and watching movies."),
    ("交友条件：女大学生，三十五岁以下，在广州学习、工作。", "Requirements for a friend: a female college graduate under 35 who studies or works in Guangzhou."),
    ("电话：七六零四九一二八五三", "Phone: 7604912853"),
]
AD_WORDS = [("征婚", "zheng1 hun1", "seek a marriage partner"), ("广告", "guang3 gao4", "advertisement"), ("身高", "shen1 gao1", "height"), ("米", "mi3", "meter"), ("毕业", "bi4 ye4", "graduate"),
            ("离异", "li2 yi4", "divorced"), ("爱好", "ai4 hao4", "hobby"), ("交友", "jiao1 you3", "make friends"), ("条件", "tiao2 jian4", "requirement, condition"), ("以下", "yi3 xia4", "below, under"),
            ("本人", "ben3 ren2", "oneself, I"), ("电影", "dian4 ying3", "movie"), ("广州", "guang3 zhou1", "Guangzhou"), ("学习", "xue2 xi2", "study")]
L10 = lesson(
    "Unit 1 review: 马小英’s profile and 刘东’s ad",
    "个人资料 · 姓名 · 年龄 · 职业 · 征婚广告 · 刘东，三十九岁",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1: 马小英’s personal record",
             "Ma Xiaoying is a 29-year-old woman who wants to meet a man through a matchmaker. This excerpt is from her personal record, which she submitted to a computer matchmaking service in Beijing. Read it carefully and decide what kind of man she would like to meet. (The book lists the items 1 to 8.)",
             tables=[table(["Item", "Pinyin", "Her record"], [[a, f"[[{auto_py(a)}]]", f"{b}  ({c})"] for a, b, c in PROFILE], say=[0])]),
        card("Words in the profile", "", tables=[wtable(PROF_WORDS)]),
        card("Activity 1 B and C (listening and speaking)",
             "B. Listen to three men (李大年, 王军, 陈力) give their personal data and fill in a table in English: age, education, occupation, father’s occupation and mother’s occupation (audio, not included).\n"
             "C. Pair up. Pick the man you believe will be the best match for Ma Xiaoying and explain your choice."),
        card("Activity 2 (Reading, Writing and Speaking): 刘东’s ad",
             "A. Use the information in the ad to fill in a table in English: name, gender, age, workplace, education, occupation, health condition, family members, requirements. B. Report the information aloud to your class. The book prints the numbers as digits (39, 1.80 米, 7604912853); here they are written out so they can be read aloud. Height 1.80 米 is read yì mǐ bā.",
             examples=[D(z, e) for z, e in AD]),
        card("Words in the ad", "", tables=[wtable(AD_WORDS)]),
    ],
    exercises=[
        M("How old is Ma Xiaoying?", "29", ["26", "50", "39"], "年龄: 二十九 (29)."),
        M("What is Ma Xiaoying’s occupation?", "Middle-school teacher", ["University teacher", "Doctor", "Engineer"], "职业：中学教师."),
        M("What are her parents’ occupations?", "University teachers", ["Middle-school teachers", "Doctors", "Engineers"], "父母职业：大学老师."),
        M("Whom does she have as a sibling?", "A younger brother, a middle-school student", ["An older sister", "Two brothers", "No siblings"], "兄弟姐妹：一个弟弟（中学生）."),
        M("What age range does she want her match to be?", "26 to 50", ["29 to 39", "20 to 25", "50 to 60"], "觅 年龄：26–50."),
        M("What education does she want?", "University", ["Middle school", "None required", "Elementary school"], "文化：大学."),
        M("Which occupation is NOT on her list?", "Student", ["Teacher", "Doctor", "Military officer"], "职业：老师、医生、工程师、军官."),
        mean("职业", "zhi2 ye4", "occupation", ["age", "gender", "name"]),
        mean("年龄", "nian2 ling2", "age", ["occupation", "gender", "education"]),
        mean("性别", "xing4 bie2", "gender", ["name", "age", "education"]),
        mean("军官", "jun1 guan1", "military officer", ["teacher", "doctor", "engineer"]),
        M("How old is Liu Dong?", "39", ["29", "35", "8"], "三十九岁 (39)."),
        M("How tall is Liu Dong?", "1.80 meters", ["1.08 meters", "1.80 centimeters", "8 meters"], "身高一米八."),
        M("Where is Liu Dong from?", "Shanghai", ["Guangzhou", "Beijing", "Tianjin"], "上海人."),
        M("Where does Liu Dong work?", "Guangzhou", ["Shanghai", "Beijing", "Chongqing"], "在广州市工作."),
        M("What is Liu Dong’s occupation?", "Engineer", ["Doctor", "Teacher", "Soldier"], "工程师."),
        M("What is Liu Dong’s family situation?", "Divorced, with an eight-year-old daughter", ["Married, with a son", "Single, with no children", "Divorced, with a 39-year-old son"], "离异。有一个八岁的女儿."),
        M("What are Liu Dong’s hobbies?", "Reading and watching movies", ["Skiing and swimming", "Cooking", "Playing games"], "爱好是看书、看电影."),
        M("What kind of friend is Liu Dong looking for?", "A female college graduate under 35 who studies or works in Guangzhou", ["Any woman over 35", "A female teacher in Shanghai", "A male engineer in Guangzhou"], "女大学生，三十五岁以下，在广州学习、工作."),
        mean("离异", "li2 yi4", "divorced", ["married", "retired", "born"]),
        mean("爱好", "ai4 hao4", "hobby", ["height", "weather", "city"]),
        mean("身高", "shen1 gao1", "height", ["health", "age", "hobby"]),
        mean("毕业", "bi4 ye4", "graduate", ["be born", "teach", "study"]),
    ],
)

# ------------------------------------------------------------------ 11. business cards and the party
CARDS = [
    ("张自强", "zhang1 zi4 qiang2", "Zhang Ziqiang", "总后勤部军需装备研究所技术开发部", "科研技术处处长 总工程师", "中国·北京·西直门北大街35号", "100088", "86-10-65671922 62289153（办）", "86-10-65671922 62289104"),
    ("赵小东", "zhao4 xiao3 dong1", "Zhao Xiaodong", "北京语言学院中文系", "教授", "中国·北京·中关村", "100056", "86-10-65789653 62289234（办）", "86-10-65789490 62288976"),
    ("刘安生", "liu2 an1 sheng1", "Liu Ansheng", "中国科学院生物工程研究所", "总工程师", "中国·北京·前门大街109号", "100123", "86-10-65568932 64538753（办）", "86-10-65198273 67893434"),
    ("李平", "li3 ping2", "Li Ping", "中国西安医学院", "主任医师", "中国·西安", "300789", "86-29-56791343 57992267（办）", "86-29-56789123 54288761"),
]
CARD_TEXT = "\n\n".join(f"Card {i + 1}: {unit_} / {name} / {title}\n地址：{addr}   邮编：{zip_}\n电话：{tel}   传真：{fax}" for i, (name, npy, nen, unit_, title, addr, zip_, tel, fax) in enumerate(CARDS))
CARD_WORDS = (rows_py([(c[3], "") for c in CARDS][:0]) if False else [])
CARD_ROWS = [(c[0], c[1], f"{c[2]}, name on card {i + 1}") for i, c in enumerate(CARDS)]
TITLE_ROWS = [(t, auto_py(t), en) for t, en in [
    ("总后勤部军需装备研究所技术开发部", "General Logistics Department, Quartermaster Equipment Research Institute, Technology Development Department"),
    ("科研技术处处长", "Director of the Scientific Research and Technology Division"), ("总工程师", "chief engineer"),
    ("北京语言学院中文系", "Beijing Language Institute, Chinese Department"), ("教授", "professor"), ("中国科学院生物工程研究所", "Chinese Academy of Sciences, Institute of Bioengineering"),
    ("中国西安医学院", "Xi’an Medical College, China"), ("主任医师", "chief physician")]]
CARD_FIELDS = [("地址", "di4 zhi3", "address"), ("邮编", "you2 bian1", "postal code"), ("电话", "dian4 hua4", "phone"), ("传真", "chuan2 zhen1", "fax"), ("办", "ban4", "(office) work number"),
               ("中关村", "zhong1 guan1 cun1", "Zhongguancun (Beijing)"), ("西直门", "xi1 zhi2 men2", "Xizhimen (Beijing)"), ("前门", "qian2 men2", "Qianmen (Beijing)"), ("西安", "xi1 an1", "Xi’an")]
L11 = lesson(
    "Unit 1 review: the business cards and the party",
    "张自强 · 赵小东 · 刘安生 · 李平 · 名片 · 地址 · 电话",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 3 (Reading and Speaking): you are a guest at a party",
             "You are a guest at a party at the home of your Chinese friend, and you want to become acquainted with other Chinese guests.\n"
             "A. Choose one of the four business cards below as your identification. Spend five minutes studying your card and make up your hometown, birthplace and family.\n"
             "B. At the party you need to: 1. Introduce yourself. 2. Have a conversation with another person to learn: the name, hometown, birthplace, profession and phone number of that person; and the names, ages, relationships and professions of that person’s family members.\n"
             "C. With your partner, meet another pair and introduce your partner to them."),
        card("The four business cards", CARD_TEXT, tables=[wtable(CARD_ROWS, headers=("Name", "Pinyin", "On the card"))]),
        card("Organizations and titles on the cards", "", tables=[wtable(TITLE_ROWS)]),
        card("Words on a business card", "", tables=[wtable(CARD_FIELDS)]),
    ],
    exercises=[
        M("Whose card gives the title 教授?", "赵小东", ["张自强", "刘安生", "李平"], "赵小东 is a professor at the Beijing Language Institute’s Chinese Department."),
        M("Whose card says 主任医师?", "李平", ["张自强", "赵小东", "刘安生"], "李平 is a chief physician at the Xi’an Medical College."),
        M("Which two people are 总工程师?", "张自强 and 刘安生", ["赵小东 and 李平", "张自强 and 李平", "赵小东 and 刘安生"], "张自强 and 刘安生 are both chief engineers."),
        M("Who works at the Chinese Academy of Sciences’ Institute of Bioengineering?", "刘安生", ["张自强", "赵小东", "李平"], "中国科学院生物工程研究所 is on 刘安生’s card."),
        M("Who works in Xi’an?", "李平", ["张自强", "赵小东", "刘安生"], "Only 李平’s address is 中国·西安."),
        M("Whose address is in Zhongguancun?", "赵小东", ["张自强", "刘安生", "李平"], "赵小东: 中关村."),
        M("Whose address is on Qianmen Street?", "刘安生", ["张自强", "赵小东", "李平"], "刘安生: 前门大街109号."),
        M("Whose address is on North Xizhimen Street?", "张自强", ["赵小东", "刘安生", "李平"], "张自强: 西直门北大街35号."),
        M("Which card’s phone number begins with the Xi’an area code 29?", "李平", ["张自强", "赵小东", "刘安生"], "李平’s phone numbers begin 86-29; the Beijing cards begin 86-10."),
        mean("地址", "di4 zhi3", "address", ["fax", "phone", "postal code"]),
        mean("邮编", "you2 bian1", "postal code", ["address", "phone", "fax"]),
        mean("传真", "chuan2 zhen1", "fax", ["phone", "address", "postal code"]),
        mean("教授", "jiao4 shou4", "professor", ["chief engineer", "doctor", "teacher’s assistant"]),
        mean("总工程师", "zong3 gong1 cheng2 shi1", "chief engineer", ["professor", "chief physician", "director"]),
        mean("主任医师", "zhu3 ren4 yi1 shi1", "chief physician", ["chief engineer", "professor", "nurse"]),
    ],
)

# ------------------------------------------------------------------ 12. 王太太 and the navy report
WANG = [
    ("王太太是上海人。", "Mrs. Wang is from Shanghai."),
    ("她是在上海生的。", "She was born in Shanghai."),
    ("她的父母都是南方人。", "Her parents are both Southerners."),
    ("上海是中国的一个大城市，城市人口有一千二百六十多万。", "Shanghai is a large city in China, with an urban population of more than 12.6 million."),
    ("王太太有一儿一女。都是大学生。", "Mrs. Wang has a son and a daughter. Both are college students."),
    ("王太太今年五十二岁。", "Mrs. Wang is 52 years old this year."),
]
NAVY = [
    ("中国海军三艘军舰，航行七千七百海里，于一九九七年三月二十一号到达美国加州圣地亚哥军港。", "Three Chinese Navy warships, after sailing 7,700 nautical miles, arrived at the San Diego naval port in California, U.S.A., on March 21, 1997."),
    ("这是中国海军第一次访问美国。", "This was the Chinese Navy’s first visit to the United States."),
    ("圣地亚哥军港是美国在西海岸最大的海军基地。", "The San Diego naval port is the largest naval base of the United States on the West Coast."),
]
NAVY_WORDS = [("军舰", "jun1 jian4", "warship"), ("航行", "hang2 xing2", "sail, voyage"), ("海里", "hai3 li3", "nautical mile"), ("于", "yu2", "on, at (formal)"), ("到达", "dao4 da2", "arrive"),
              ("圣地亚哥", "sheng4 di4 ya4 ge1", "San Diego"), ("军港", "jun1 gang3", "naval port"), ("访问", "fang3 wen4", "visit"), ("第一次", "di4 yi1 ci4", "the first time"),
              ("西海岸", "xi1 hai3 an4", "West Coast"), ("海军基地", "hai3 jun1 ji1 di4", "naval base"), ("艘", "sou1", "measure word for ships")]
L12 = lesson(
    "Unit 1 review: 王太太 and the navy report",
    "王太太是上海人 · 中国海军三艘军舰 · 圣地亚哥军港",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 4 (Listening, Reading and Speaking): Mr. and Mrs. Wang",
             "An overseas Chinese couple, Mr. and Mrs. Wang, are visiting China. A. Listen to Passage 1 and translate it orally into English (audio, not included). B. Read Passage 2 and translate it into English orally. In the book the numbers are digits (1260 多万 and 52 岁); here they are written out.",
             examples=[D(z, e) for z, e in WANG]),
        card("Activity 5 (Reading, Listening and Speaking): the summary report",
             "A. Read the summary report and answer the four questions: When did the Chinese Navy arrive in San Diego? What is unique about the San Diego naval base? How many nautical miles did the Chinese Navy travel? How many Chinese warships arrived in the U.S.? B. Listen to an interview between a Xinhua News Agency reporter and a Chinese soldier, then ask one more question using the information (audio, not included). C. Pair up and prepare interview questions using two-way interpretation: Student 1 is a Los Angeles Times reporter who cannot speak Chinese, Student 2 is the interpreter, and the teacher is a Chinese soldier.",
             examples=[D(z, e) for z, e in NAVY]),
        card("Words in the report", "", tables=[wtable(NAVY_WORDS)]),
    ],
    exercises=[
        M("Where is Mrs. Wang from?", "Shanghai", ["Beijing", "Tianjin", "Chongqing"], "王太太是上海人。"),
        M("Where was Mrs. Wang born?", "Shanghai", ["Beijing", "California", "Xi’an"], "她是在上海生的。"),
        M("Where are Mrs. Wang’s parents from?", "Southern China", ["Northern China", "California", "Shandong"], "她的父母都是南方人。"),
        M("What is Shanghai’s urban population, according to the passage?", "More than 12.6 million", ["More than 1.26 million", "More than 126 million", "More than 26,000"], "城市人口有一千二百六十多万。"),
        M("What children does Mrs. Wang have?", "A son and a daughter, both college students", ["Two sons", "A daughter only", "Three children, all in middle school"], "王太太有一儿一女。都是大学生。"),
        M("How old is Mrs. Wang?", "52", ["25", "62", "12"], "五十二岁."),
        M("When did the Chinese Navy arrive in San Diego?", "March 21, 1997", ["March 5, 1997", "March 21, 1998", "May 21, 1997"], "一九九七年三月二十一号."),
        M("What is unique about the San Diego naval base?", "It is the largest U.S. naval base on the West Coast, and it was the Chinese Navy’s first visit to the U.S.", ["It is on the East Coast", "It is the smallest base", "It is in Texas"], "最大的海军基地; 第一次访问美国."),
        M("How many nautical miles did the Chinese Navy travel?", "7,700", ["7,000", "700", "77,000"], "航行七千七百海里."),
        M("How many Chinese warships arrived?", "Three", ["Two", "Five", "Seven"], "三艘军舰."),
        mean("军舰", "jun1 jian4", "warship", ["base", "school", "soldier"]),
        mean("海里", "hai3 li3", "nautical mile", ["kilometer", "meter", "hour"]),
        mean("到达", "dao4 da2", "arrive", ["leave", "visit", "sail"]),
        mean("访问", "fang3 wen4", "visit", ["arrive", "sail", "live"]),
        mean("西海岸", "xi1 hai3 an4", "West Coast", ["East Coast", "naval base", "South"]),
    ],
)

# ------------------------------------------------------------------ 13. interrogation, overheard conversations
INTERR = [
    ("你叫什么名字？", "What is your name?"), ("你是哪国人？", "What is your nationality?"), ("你的老家在哪儿？", "Where is your hometown?"),
    ("你是在哪儿出生的？", "Where were you born?"), ("你今年多大？", "How old are you this year?"), ("你做什么工作？", "What is your job?"),
    ("你是哪个军种的？", "Which military service are you in?"), ("你是什么军种？", "What is your military service?"),
    ("你的军衔是什么？", "What is your military rank?"), ("你是什么军衔？", "What is your military rank?"),
]
L13 = lesson(
    "Unit 1 review: interrogation questions and overheard conversations",
    "你是哪个军种的？ · 你的军衔是什么？ · 军种 · 军衔",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 6 (Speaking and Writing): the interrogation",
             "You are assigned to interrogate illegal Chinese-speaking immigrants who came to the United States by boat. Your supervisor needs some information on those you have interrogated.\n"
             "A. Work in pairs. Your classmate plays the role of an illegal immigrant. While interrogating your partner, take notes in a table, then exchange roles so each partner plays both parts.\n"
             "B. The instructor plays your supervisor. Report the information you have obtained.\n"
             "The table has eight items: 1. Name, 2. Nationality, 3. Hometown, 4. Birthplace, 5. Birth year or age, 6. Profession, 7. Military service, if any, 8. Military rank, if any.\n"
             "Notes: 1. When asking someone’s military service and rank, these sentences are useful: a. 你是哪个军种的？ or 你是什么军种？ b. 你的军衔是什么？ or 你是什么军衔？ 2. In this activity, each immigrant gets a flash card, made by your instructor, with their background information.\n"
             "The first two questions below are the book’s; the others are built from the patterns of the unit so that you can cover all eight items.",
             examples=[D(z, e) for z, e in INTERR]),
        card("Activity 7: overheard conversations",
             "The “overheard conversation” aims at developing your ability to gain the gist of a conversation in which you are not a participant. The language you will hear is quite unrestricted. At your present level you will understand only a small portion of what you hear, but you can also glean information from the speakers’ tone of voice, the speed with which they speak, and the functional vocabulary you have already noted and practiced. This is one of your final learning objectives for the Basic Course.\n"
             "Overhearing conversations can be great fun. The secret is to maintain your level of attention throughout. If things are said that you don’t follow, ignore them and keep listening. If you make a conscious effort to avoid getting stuck trying to figure out one phrase, or “tuning out”, you will pick up much more. This is not a translation exercise, and you will not be asked to reproduce any of this language. You are listening for any information that could be of use to you.\n"
             "A. Listen and write the male speaker’s name in pinyin with tone marks (segment 1). B. Listen and write the male speaker’s personal information in English (segment 2). C. Listen again and write any additional information you heard (segment 3). D. Present the information you have gathered to the class in Chinese. (Audio, not included.)"),
        card("Activity 8: a U.S.–China military conference in Beijing",
             "You work for the Department of Defense and are attending a U.S.–China military conference in Beijing. During a break you overhear three people exchange their personal information (a SCOLA recording, not included). Listen for information about each person and write notes in a table: name, nationality, military service, military rank, phone number. Then check what you have obtained with other students by asking them questions in Chinese.\n"
             "Note: regarding the issue of maritime security, Chinese and U.S. military forces held their first annual meeting in 1998."),
        card("New words", "", tables=[wtable([("军种", "jun1 zhong3", "military service (branch)"), ("军衔", "jun1 xian2", "military rank"), ("哪个", "na3 ge4", "which"), ("出生", "chu1 sheng1", "be born"), ("工作", "gong1 zuo4", "work, job")])]),
    ],
    exercises=[
        M("Which sentence asks someone’s military rank?", "你的军衔是什么？", ["你是哪个军种的？", "你今年多大？", "你是哪国人？"], "军衔 means military rank."),
        M("Which sentence asks someone’s military service (branch)?", "你是哪个军种的？", ["你的军衔是什么？", "你叫什么名字？", "你做什么工作？"], "军种 means military service."),
        M("Which sentence asks where someone was born?", "你是在哪儿出生的？", ["你的老家在哪儿？", "你今年多大？", "你是什么军衔？"], "出生 means be born."),
        M("Which sentence asks someone’s age?", "你今年多大？", ["你是哪国人？", "你叫什么名字？", "你是什么军种？"], "多大 asks about age."),
        M("Which sentence asks someone’s nationality?", "你是哪国人？", ["你今年多大？", "你的老家在哪儿？", "你是什么军衔？"], "哪国人 asks which country someone is from."),
        M("Which sentence asks someone’s name?", "你叫什么名字？", ["你做什么工作？", "你是哪国人？", "你今年多大？"], "叫什么名字 asks what someone is called."),
        mean("军种", "jun1 zhong3", "military service (branch)", ["military rank", "military school", "soldier"]),
        mean("军衔", "jun1 xian2", "military rank", ["military service", "military school", "base"]),
        M("What is the first Chinese–U.S. military maritime security meeting mentioned in the book’s note?", "It was held in 1998", ["It was held in 1988", "It was held in 2008", "It has never been held"], "The note says the first annual meeting was held in 1998."),
    ],
)

UNIT = unit("第六课 单元复习 Review: Meeting People", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])
