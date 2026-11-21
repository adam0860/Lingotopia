"""Unit 19: Lesson 7 (School Life) Presentation 1, from the book's texts: the dialog with Sergeant Gao, telling time,
以后, the modal verbs 要 and 得, 又…又…, time when and time spent, the emails and schedules, and the vocabulary list.
The listening activities and the clock pictures are not included; the lessons say so."""
from zh_auto import *
from zh_l7_vocab import VOC1

PART = ["吗", "们", "呢"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [
    ("记者", "你好！很高兴见到你。", "Hello! I’m very happy to meet you."),
    ("高上士", "你好！我也很高兴见到你。", "Hello! I’m very happy to meet you too."),
    ("记者", "你们现在学习忙吗？", "Are you busy with your studies now?"),
    ("高上士", "很忙。不过，我们已经习惯了。", "Very busy. But we have already gotten used to it."),
    ("记者", "你们每天早上几点集合？", "What time do you have formation every morning?"),
    ("高上士", "我们早上六点半集合。", "We have formation at 6:30 in the morning."),
    ("记者", "每天有几节课？", "How many classes are there every day?"),
    ("高上士", "六节课。早上七点四十五分上课，下午两点五十下课。", "Six classes. Class starts at 7:45 in the morning, and finishes at 2:50 in the afternoon."),
    ("记者", "下课以后，你们做什么？", "After class, what do you do?"),
    ("高上士", "下课以后，我们要去操场锻炼身体。", "After class, we go to the drill field to exercise.", {"得": "dei3"}),
    ("记者", "那晚上呢？", "And in the evening?"),
    ("高上士", "晚上要做作业，还得预习课文，有时候还要值班。", "In the evening we have to do homework and also preview the text, and sometimes we also have to be on duty.", {"得": "dei3"}),
    ("记者", "你们每天真忙啊！", "You are really busy every day!"),
    ("高上士", "是啊。我们又是军人又是学生嘛。", "Yes, we are both soldiers and students."),
]
L1 = lesson(
    "Presentation 1: the school day (dialog)",
    "第七课 校园生活 · 你们每天早上几点集合？ · 我们又是军人又是学生",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss with your partner: A. How many hours do you normally spend in class at DLI? B. Who spends more time in class a day, you or Sgt. Gao in Presentation 1? C. What do you usually do in the evening?"),
        card("第七课 校园生活 Lesson 7 Student Life: objectives",
             "When you finish this lesson you will be able to: ask questions about and state the time of day; ask about and describe daily schedules; ask about and describe simple school activities; ask about and describe simple weekend activities. "
             "To do that you must master the vocabulary for these functions, telling time, the time word 以后, the modal verbs 要 and 得, the 又…又… construction, word order for “time when” and “time spent”, the question word 怎么样, the 除了… 还… construction, the complement of degree, the 先…然后… construction and the 有时…有时… construction."),
        card("Presentation 1: a reporter interviews Sergeant Gao",
             "The book also prints this dialog in traditional characters; the traditional forms of the words are in the vocabulary lesson.",
             examples=dlg(P1)),
        card("Activity 1 (Listening)",
             "The book first has you listen to the dialog and mark three statements true or false (The sergeant mostly studies in his spare time. / Being both soldier and student, the sergeant keeps a very busy schedule. / The reporter is impressed by his willingness to perform his military duties), then answer: Is Sergeant Gao a new student? How do you know? What does he do from 7:45 a.m. to 2:50 p.m.? When and where does he work out? The recording is not included, so the questions are practiced from the text above."),
    ],
    exercises=[
        M("True or false: the sergeant mostly studies in his spare time.", "False: he is busy with classes, homework and duty", ["True: he has a lot of spare time", "True: he never has homework", "False: he has no classes"], "He says he is very busy: classes, homework, previewing and duty."),
        M("True or false: being both soldier and student, the sergeant keeps a very busy schedule.", "True", ["False: he is only a student", "False: he has no duty", "False: he is not busy"], "我们又是军人又是学生嘛 — he is both, and very busy."),
        M("Is Sergeant Gao a new student? How do you know?", "No: he says they have already gotten used to it (已经习惯了)", ["Yes: he says it is his first day", "Yes: he says he is not busy", "No: he says he is a teacher"], "很忙。不过，我们已经习惯了。"),
        M("What does he do from 7:45 a.m. to 2:50 p.m.?", "He has classes (six periods)", ["He exercises", "He is on duty", "He does homework"], "早上七点四十五分上课，下午两点五十下课。"),
        M("When and where does he work out?", "After class, at the drill field", ["Before breakfast, in the dormitory", "In the evening, at the library", "At noon, at a restaurant"], "下课以后，我们要去操场锻炼身体。"),
        M("What time does the morning formation start?", "6:30", ["7:45", "6:00", "2:50"], "我们早上六点半集合。"),
        M("How many classes are there every day?", "Six", ["Four", "Five", "Seven"], "六节课。"),
        M("What do they have to do in the evening?", "Homework and previewing the text; sometimes duty", ["Class", "Formation", "Go to a restaurant"], "晚上要做作业，还得预习课文，有时候还要值班。"),
        F("你们每天早上几点___？", "集合", ["作业", "预习", "操场"], "集合 is “have formation”: 你们每天早上几点集合？"),
        F("我们早上六点___集合。", "半", ["刻", "分", "节"], "六点半 is half past six."),
        F("下课以后，我们___去操场锻炼身体。", "要", PART, "要 here means “are to / need to”."),
        F("我们___是军人又是学生嘛。", "又", PART, "又…又… means “both … and …”."),
        M("What does 值班 mean?", "be on duty", ["go to class", "have formation", "preview"], "值班 is a verb-object word, “be on duty”."),
    ],
)

# ------------------------------------------------------------------ 2. matching and rebuilding
MATCH = [("上午他们十一点半", "下课。", "c"), ("下课以后", "我们一起去操场锻炼身体好吗？", "e"), ("今天晚上我六点半值班，", "没有时间做作业了。", "b"),
         ("今天下午你去操场锻炼身体", "还是回家做作业？", "a"), ("你什么时间预习课文？", "做作业以后。", "d")]
MATCH_EN = ["They finish class at 11:30 in the morning.", "After class, shall we go to the drill field together to exercise?",
            "I am on duty at 6:30 this evening, so there is no time to do homework.", "This afternoon, are you going to the drill field to exercise, or going home to do homework?",
            "When do you preview the text? After doing homework."]
SEQ = [("我们每天的学习都很忙。", "Every day our studies are very busy."), ("每个星期一、三、五早上六点要去操场集合。", "Every Monday, Wednesday and Friday at 6 a.m. we have to go to the drill field for formation."),
       ("我们第一节课是早上七点五十五分上课。", "Our first class starts at 7:55 in the morning."), ("最后一节课是下午两点上课。", "The last class starts at 2 in the afternoon."),
       ("下课以后我们去锻炼身体。", "After class we go and exercise."), ("晚上要做很多作业，还要预习课文。", "In the evening we have to do a lot of homework, and also preview the text."),
       ("一位同学晚上还得值班。", "One classmate also has to be on duty in the evening.")]
L2 = lesson(
    "Presentation 1 activities: matching clauses and rebuilding a paragraph",
    "上午他们十一点半下课 · 下课以后做什么？",
    requires=[],
    cards=[
        card("Activity 4: match the clauses in Column A with those in Column B",
             "The book gives these two columns (A: 1 to 5, B: a to e), and you match them and then translate each sentence into English with a partner. The matched sentences, with their book letters in the notes:",
             examples=[D(a + b, en) for (a, b, k), en in zip(MATCH, MATCH_EN)]),
        card("Activity 5: arrange the sentences into a logical paragraph",
             "The book lists seven sentences in a mixed-up order and has pairs arrange them into a coherent paragraph, then report their order to the class. The book gives no key; here is the order that makes the most sense: the general statement first, then formation, the first class, the last class, exercise after class, the evening homework, and the classmate on duty at the end. Other orders can work; talk it over with your partner.",
             examples=[D(z, e) for z, e in SEQ]),
    ],
    exercises=[M(f"Match the clause: {a} …", b, [m[1] for m in MATCH if m[1] != b][:3], f"{a}{b} — {en}") for (a, b, k), en in zip(MATCH, MATCH_EN)] + [
        M("Which sentence best opens the paragraph?", SEQ[0][0], [SEQ[4][0], SEQ[6][0], SEQ[3][0]], "A general statement about how busy the day is makes a good opening."),
        M("Which sentence fits at the end of the paragraph?", SEQ[6][0], [SEQ[0][0], SEQ[1][0], SEQ[2][0]], "Duty is the last thing in the evening."),
        M("Which sentence follows “下课以后我们去锻炼身体。”?", SEQ[5][0], [SEQ[0][0], SEQ[2][0], SEQ[3][0]], "After exercise comes the evening homework."),
        M("When is the first class?", "7:55 in the morning", ["2 in the afternoon", "6 in the morning", "Noon"], "我们第一节课是早上七点五十五分上课。"),
        M("When is the last class?", "2 in the afternoon", ["7:55 in the morning", "6 in the morning", "Evening"], "最后一节课是下午两点上课。"),
        M("When is formation each week?", "Monday, Wednesday and Friday at 6 a.m.", ["Every day at noon", "Saturday and Sunday", "Tuesday and Thursday evening"], "每个星期一、三、五早上六点要去操场集合。"),
    ],
)

# ------------------------------------------------------------------ 3. telling time
TIME_ROWS = [
    ("零点（夜里十二点）", "0:00 (midnight)"), ("一点", "1:00"), ("一点钟", "1:00 (with 钟)"), ("两点", "2:00"), ("两点钟", "2:00 (with 钟)"), ("三点", "3:00"), ("三点钟", "3:00 (with 钟)"),
    ("六点零五（分）", "6:05"), ("六点过五分", "6:05 (过 = past)"), ("六点零九（分）", "6:09"), ("六点过九分", "6:09 (过 = past)"), ("七点十分", "7:10"), ("七点过十分", "7:10 (过 = past)"),
    ("八点二十（分）", "8:20"), ("八点五十五（分）", "8:55"), ("九点差五分", "8:55 (差 = short of, five minutes to nine)"), ("差五分九点", "8:55 (five to nine)"),
    ("九点十五（分）", "9:15"), ("九点一刻", "9:15 (a quarter past nine)"), ("十点四十五（分）", "10:45"), ("十点三刻", "10:45 (three quarters)"), ("差一刻十一点", "10:45 (a quarter to eleven)"),
    ("十一点三十（分）", "11:30"), ("十一点半", "11:30 (half past eleven)"), ("十二点三十（分）", "12:30"), ("十二点半", "12:30 (half past twelve)"),
]
PERIODS = [("早上", "early morning"), ("上午", "morning"), ("中午", "noon"), ("下午", "afternoon"), ("晚上", "evening"), ("夜里", "night")]
INTERVIEW = [("你星期一到星期五几点起床？", "What time do you get up on weekdays?"), ("你们早上几点集合？", "What time do you have morning formation?"),
             ("你几点吃早饭？", "What time do you have breakfast?"), ("你几点吃晚饭？", "What time do you have dinner?"),
             ("你几点做作业？", "What time do you do homework?"), ("你几点睡觉？", "What time do you go to bed?")]
TIME_EX = [("七点四十五分", "7:45", ["7:15", "7:54", "4:57"]), ("九点一刻", "9:15", ["9:45", "9:50", "9:05"]), ("十点三刻", "10:45", ["10:15", "10:30", "10:35"]), ("十二点半", "12:30", ["12:03", "12:15", "1:20"]),
           ("六点过五分", "6:05", ["6:50", "5:06", "6:15"]), ("九点差五分", "8:55", ["9:05", "9:50", "8:05"]), ("差一刻十一点", "10:45", ["11:15", "10:15", "11:45"]), ("早上六点半", "6:30 a.m.", ["6:30 p.m.", "6:03 a.m.", "6:13 a.m."]),
           ("下午两点五十", "2:50 p.m.", ["2:15 p.m.", "5:20 p.m.", "2:05 p.m."]), ("两点", "2:00", ["12:00", "1:00", "3:00"]), ("零点", "midnight", ["noon", "1:00", "10:00"]), ("八点二十", "8:20", ["8:02", "2:08", "8:12"])]
L3 = lesson(
    "Presentation 1 grammar: telling time",
    "点 · 分 · 刻 · 半 · 差 · 过 · 上午 · 下午 · 晚上",
    requires=[],
    cards=[
        card("Telling time: from the largest unit to the smallest",
             "The sequence for telling the time in Chinese runs from the largest to the smallest unit: year, month, date, AM/PM, specific time. The book’s example is 1998 年 8 月 20 号 上午 9 点零 5 分; here the numbers are written out.",
             examples=[D("一九九八年八月二十号上午九点零五分", "9:05 a.m., August 20, 1998")]),
        card("Periods of the day", "", tables=[wtable(rows_py(PERIODS))]),
        card("The hour, the quarter and the minute",
             "点 or 钟 (o’clock), 刻 (quarter hour) and 分 (minute) are the hourly units. Because they are also measure words, they come immediately after numbers. 两 is used for 2 o’clock (两点), not 二点. From 1 to 9 minutes past, 零 is put in front (六点零五, “6:05”); from 10 to 59 minutes it is not (七点十分). 过 means “past” and 差 means “short of”. A quarter hour is 一刻, three quarters is 三刻, and the half hour is 半.",
             tables=[wtable([(z, auto_py(z), e) for z, e in TIME_ROWS], headers=("Chinese", "Pinyin", "Time"))]),
        card("Activity 1: the clocks (pictures)",
             "The book shows clock faces for you to write the time under, and eight to eleven times to hear and write down (audio). Neither is included here; practice with the questions below."),
        card("Activity 2 (Speaking and Writing): interview your partner",
             "Interview your partner and fill in a table, then report the results to a new partner, speaking only Chinese. The book gives the questions in English: When do you get up during the week? What time do you have morning formation? When do you have breakfast? When do you have dinner? When do you do homework? When do you go to bed? Here is one way to say each:",
             examples=[D(z, e) for z, e in INTERVIEW]),
        card("Activity 3 (Listening, Writing and Speaking)",
             "Listen to a conversation between Wang Ying and Chen Qiang and fill in Chen Qiang’s daily routine in English (when, and what and where), then ask your partner questions about it in Chinese and check against the script (audio, not included)."),
    ],
    exercises=[M(f"What time is {z}?", t, w, f"{z} is {t}.") for z, t, w in TIME_EX] + [
        M("How do you say 2:00?", "两点", ["二点", "两分", "二刻"], "2 o’clock is 两点: 两 is used with measure words like 点."),
        M("How do you say 6:05?", "六点零五分", ["六点五分", "六点十五", "五点六分"], "From 1 to 9 minutes, 零 comes before the number."),
        M("How do you say 7:10?", "七点十分", ["七点零十分", "七点十五", "十点七分"], "From 10 minutes on there is no 零."),
        M("What does 一刻 mean?", "a quarter of an hour", ["one minute", "one hour", "half an hour"], "一刻 is 15 minutes; 三刻 is 45."),
        M("What does 半 mean in 十一点半?", "half", ["quarter", "minute", "hour"], "十一点半 is 11:30."),
        M("What does 差 mean in 九点差五分?", "short of: five minutes before nine", ["past: five minutes after nine", "exactly nine", "about nine"], "差五分九点 and 九点差五分 are both 8:55."),
        M("What does 过 mean in 六点过五分?", "past: five minutes after six", ["short of six", "exactly six", "before six"], "过 means “past”."),
        M("Which period of the day is 中午?", "noon", ["early morning", "evening", "night"], "中午 is noon."),
        M("Which period of the day is 晚上?", "evening", ["noon", "early morning", "afternoon"], "晚上 is evening."),
        M("What is the correct order for a full date and time?", "Year, month, date, AM/PM, time", ["Time, AM/PM, date, month, year", "Month, date, year, time", "AM/PM, year, month, time"], "From the largest unit to the smallest."),
        mean("下午", "xia4 wu3", "afternoon", ["morning", "evening", "noon"]),
        mean("早上", "zao3 shang5", "early morning", ["noon", "afternoon", "night"]),
    ],
)

# ------------------------------------------------------------------ 4. 以后
HOU = [
    ("每天早上集合以后，我去学校上课。", "Mornings I go to school after formation."), ("下雪以后，天很冷。", "It is cold after it snows."), ("习惯以后她很喜欢。", "She likes it a lot after getting used to it."),
    ("五分钟以后在操场集合。", "Gather in the field in 5 minutes."), ("“零零后”就是二千年以后出生的人。", "“Post-00s” are those born after 2000."), ("九一一以后很多人参军。", "After 911, many people joined the military."),
]
HOU_NOTE = [("以后再说。", "Let’s talk about it later."), ("你以后做什么工作？", "What job will you do in the future?"), ("我以后要习惯说中文。", "I will get used to speaking Chinese from now on.")]
L4 = lesson(
    "Presentation 1 grammar: the time word 以后",
    "下课以后 · V/VP/N/NP + 以后 · 以后再说",
    requires=[],
    cards=[
        card("以后: after",
             "In the presentation the reporter and Sergeant Gao had this exchange: 下课以后，你们做什么？ — 下课以后，我们要去操场锻炼身体。 下课以后 means “after class”. 以后 expresses “after”: it is used to indicate a time frame that is after something happened, or after a certain time or event. In English, “after” comes before the verb or noun; in Chinese the order is just the opposite: V/VP/N/NP + 以后. "
             "The book writes 00 后 and 2000 年 and 911 with digits; they are written out here (零零后, 二千年, 九一一).",
             examples=[D(z, e) for z, e in HOU]),
        card("以后 as a noun",
             "以后 can also be a noun by itself, meaning “later”, “in the future” or “from now on”.",
             examples=[D(z, e) for z, e in HOU_NOTE]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Pair up. Analyze one or two example sentences to discover differences between Chinese and English (word order, and so on). Share your findings with the class. B. Take turns covering up the Chinese examples while orally interpreting the English sentences into Chinese; your partner may look and give hints. "
             "C. Do a chain story as a class. The main character is 18 岁的空军马龙 (the 18-year-old Air Force airman Ma Long). The first sentence is 今天马龙五点起床。 Take turns continuing the story with 以后 until everybody has had two turns. While the story is told, each student draws simple pictures of what 马龙 has done; afterward pair up and compare your drawings to see if you got the same information.",
             examples=[D("今天马龙五点起床。", "Today Ma Long gets up at five.")]),
    ],
    exercises=[
        M("In 下课以后, where does 以后 go compared with English “after class”?", "After the word: 下课 + 以后", ["Before the word: 以后 + 下课", "At the end of the sentence only", "It cannot be used with verbs"], "English puts “after” first; Chinese puts 以后 last."),
        M("What does 下雪以后，天很冷 mean?", "It is cold after it snows", ["It snows after it is cold", "It is not cold when it snows", "It will snow tomorrow"], "下雪以后 = after it snows."),
        M("What does 五分钟以后在操场集合 mean?", "Gather in the field in 5 minutes", ["Gather in the field 5 minutes ago", "Gather at 5 o’clock", "Do not gather in the field"], "A time span + 以后 = “in … time”."),
        M("What does “后” mean in 零零后?", "born after (those born after 2000)", ["before", "behind the school", "last year"], "零零后 are the “post-00s”, born after 2000."),
        M("What does 以后再说 mean?", "Let’s talk about it later", ["Let’s talk about it now", "I never say it", "He talked before"], "以后 alone can mean “later”."),
        M("What does 你以后做什么工作？ ask?", "What job will you do in the future?", ["What job did you do before?", "What job do you have now?", "Who is your teacher?"], "以后 as a noun: “in the future”."),
        F("下课___，我们要去操场锻炼身体。", "以后", PART, "下课以后: after class."),
        F("每天早上集合___，我去学校上课。", "以后", PART, "集合以后: after formation."),
        F("五分钟以后在操场___。", "集合", ["作业", "预习", "已经"], "集合 is “have formation, muster”."),
        F("我以后要习惯说___。", "中文", PART, "说中文: speak Chinese."),
        M("How do you say “after dinner”?", "吃饭以后", ["以后吃饭", "吃饭以", "以吃饭后"], "V + 以后."),
        M("How do you say “after getting up”?", "起床以后", ["以后起床", "起以后床", "床起以后"], "起床以后."),
    ],
)

# ------------------------------------------------------------------ 5. modal verb 要
YAO = [
    ("我要做作业。", "I need to do my homework.", None), ("我还要值班。", "I must be on duty as well.", None), ("我要去火星。", "I want to go to Mars.", None), ("要小心！", "Be careful!", None),
]
YAO_TABLE = table(["", "要 = must, need", "要 = want", "要 = an order"], [
    ["Affirmative", "Subject + 要 + V", "Subject + 要 + V", "Subject + 要 + V"],
    ["Example", "我要值班。", "我要去火星。", "你要小心！"],
    ["Question", "Subject + 要 + V + 吗？", "Subject + 要 + V + 吗？ / Subject + 要不要 + V？ / Subject + 想 + V + 吗？ / Subject + 想不想 + V？", "—"],
    ["Question example", "我要值班吗？", "你要去火星吗？ / 你要不要去火星？ / 你想去火星吗？ / 你想不想去火星？", "—"],
    ["Negative", "Subject + 不用 + V / Subject + 不需要 + V", "Subject + 不想 + V / Subject + 不 + V", "Subject + 不要 + V"],
    ["Negative example", "我不用值班。 / 我不需要值班。", "我不想去火星。 / 我不去火星。", "你不要大意！"],
], title="The modal verb 要 in three meanings", say=[])
YAO_Q = [
    ("这个星期我要看医生。你这个星期要看医生吗？", "This week I have to see the doctor. Do you have to see the doctor this week?"),
    ("这个星期六我要去旧金山。你这个星期六要不要去旧金山？", "This Saturday I want to go to San Francisco. Do you want to go to San Francisco this Saturday?"),
    ("你是得锻炼呢，还是你想要锻炼？", "Do you have to exercise, or do you want to exercise?"),
]
YAO_SAY = [("大卫，你今天下午想去游泳吗？", "Ask if David wants to go swimming this afternoon.", None), ("我得做作业，今天下午我不去游泳。", "State that he needs to do his homework and will not go swimming this afternoon.", {"得": "dei3"}),
           ("小王还想回老家过春节吗？", "Ask if Xiao Wang still wants to go back to his hometown to celebrate the Chinese New Year.", None),
           ("小王要回老家过春节。这个月他不用值班。", "State that Xiao Wang wants to return to his hometown to celebrate the Chinese New Year and does not need to be on duty this month.", None),
           ("大家都要谢谢自己的父母。", "State that everyone must thank his/her parents.", None)]
L5 = lesson(
    "Presentation 1 grammar: the modal verb 要",
    "我要做作业 · 我要去火星 · 要小心！ · 不用 · 不想 · 不要",
    requires=[],
    cards=[
        card("要: must or need, want, and an order",
             "In this lesson 要 is used before a verb to show that an action is a must or a need: 我要做作业 (I need to do my homework), 我还要值班 (I must be on duty as well). 要 is also commonly used to show desire or want: 我要去火星 (I want to go to Mars). A third common use is an order or command: 要小心！ (Be careful!). "
             "Each meaning has its own negative and question forms.",
             tables=[YAO_TABLE], examples=[D(z, e) for z, e, f in YAO]),
        card("Negative forms and the question forms in detail",
             "For “must or need”, the negative is 不用 (búyòng, no need) or 不需要 (bù xūyào, don’t need): 我不用值班。 我不需要值班。 For “want”, it is 不想 or just 不: 我不想去火星。 我不去火星。 For an order, 不要: 你不要大意！ (Don’t be careless!). "
             "The questions: 我要值班吗？ for “must”; and for “want”: 你要去火星吗？ 你要不要去火星？ 你想去火星吗？ 你想不想去火星？",
             examples=[D("我不用值班。", "I don’t have to be on duty."), D("我不需要值班。", "I don’t need to be on duty."), D("我不想去火星。", "I don’t want to go to Mars."), D("我不去火星。", "I’m not going to Mars."),
                       D("你不要大意！", "Don’t be careless!"), D("我要值班吗？", "Do I have to be on duty?"), D("你要不要去火星？", "Do you want to go to Mars?"), D("你想不想去火星？", "Do you want to go to Mars?")]),
        card("When 要 could mean either",
             "When indicating must or need, and want, the affirmative forms are the same, so sometimes you do not know which meaning a speaker is expressing. For example 我要锻炼 could mean “I need to exercise” or “I want to exercise”. You can rely on the context to figure it out, or you can ask for clarification: 你是得锻炼呢，还是你想要锻炼？",
             examples=[D("我要锻炼。", "I need to exercise / I want to exercise."), D("你是得锻炼呢，还是你想要锻炼？", "Do you have to exercise, or do you want to exercise?", fixes={"得": "dei3"})]),
        card("Activity 5 and Activity 6 (Speaking and Listening)",
             "Activity 5: A. Write down three things you must do this week and share them with a partner, then ask whether they must do the same things, and take notes. B. Write down three things you want to do this Saturday, share them and ask the same. The book’s two examples are 这个星期我要看医生。你这个星期要看医生吗？ and 这个星期六我要去旧金山。你这个星期六要不要去旧金山？ "
             "Activity 6: tell a partner what you would say in Chinese for five situations. The book gives them in English; one way to say each follows.",
             examples=[D(z, e, fixes=f) for z, e, f in YAO_SAY]),
    ],
    exercises=[
        M("What does 我要做作业 mean?", "I need to do my homework", ["I don’t want to do homework", "I did my homework", "Do you do homework?"], "要 + verb: “need to” here."),
        M("What does 我要去火星 mean?", "I want to go to Mars", ["I have to go to Mars", "I went to Mars", "Don’t go to Mars"], "要 as “want”."),
        M("What does 要小心！ mean?", "Be careful!", ["I want to be careful", "I need a heart", "He is careful"], "要 as an order."),
        M("How do you say “I don’t have to be on duty”?", "我不用值班。", ["我不要值班。", "我不想值班吗？", "我值班不用。"], "The negative of “must” is 不用 or 不需要; 不要 would be “don’t”."),
        M("How do you say “I don’t want to go to Mars”?", "我不想去火星。", ["我不用去火星。", "我要不去火星。", "我不需要去火星。"], "The negative of “want” is 不想 or 不."),
        M("How do you say “Don’t be careless!”?", "你不要大意！", ["你不用大意！", "你不想大意！", "你大意不要！"], "The negative of an order is 不要."),
        M("Which question asks “Do you want to go to Mars?”?", "你想不想去火星？", ["你去不火星？", "你想去火星不吗？", "你想吗不去火星？"], "想不想 is the affirmative-negative form."),
        M("Which of these is a correct question for “want”?", "你要不要去火星？", ["你要去不火星？", "你不要去火星吗不？", "你要去火星不要吗？"], "要不要 + V."),
        M("Which question clarifies 我要锻炼?", "你是得锻炼呢，还是你想要锻炼？", ["你是锻炼吗？", "你要不要不锻炼？", "你锻炼了没有？"], "It asks: must or want?"),
        F("我不___值班。", "用", PART, "不用 means “don’t have to”."),
        F("你___不要去火星？", "要", PART, "要不要 is the affirmative-negative question."),
        F("你不___大意！", "要", PART, "不要 is “don’t” in an order."),
        F("这个星期我要看___。", "医生", PART, "看医生: see the doctor."),
        mean("要", "yao4", "want to", ["go to", "study", "get used to"]),
        mean("值班", "zhi2 ban1", "on duty", ["be busy", "have formation", "preview"]),
    ],
)

# ------------------------------------------------------------------ 6. modal verb 得
DEI = [
    ("他得去看医生。", "He has to go and see the doctor."), ("今天晚上我得去学校值班。", "Tonight I have to go to school for duty."), ("他们也得去操场集合吗？", "Do they have to go to the drill field for formation too?"),
    ("你今天晚上得值班吗？", "Do you have to be on duty tonight?"), ("海军今天不用去操场集合。", "The Navy doesn’t have to go to the drill field for formation today."),
    ("海军今天不需要去操场集合。", "The Navy doesn’t need to go to the drill field for formation today."),
]
L6 = lesson(
    "Presentation 1 grammar: the modal verb 得 (děi)",
    "我得去学校上课 · 你今天晚上得值班吗？ · 不用 / 不需要",
    requires=[],
    cards=[
        card("得 (děi): must",
             "When used as a modal verb, 得 (pronounced děi) expresses the obligation or need to carry out an action, similar to the English “must”: 我得去学校上课。 The negative form is 不用 / 不需要 (xūyào: need). The patterns are: Affirmative: Subject + 得 + Verb + Object. Interrogative: Subject + 得 + Verb + Object + 吗？ Negative: Subject + 不用 / 不需要 + Verb + Object. "
             "The book gives the examples without English; the translations here are added. (Do not confuse it with the structural particle 得, pronounced de, in 说得好, which comes later in this lesson.)",
             examples=[D("我得去学校上课。", "I have to go to school for class.", fixes={"得": "dei3"})] + [D(z, e, fixes={"得": "dei3"}) for z, e in DEI]),
        card("Activity 7 and Activity 8",
             "Activity 7: listen to a dialog and take notes on the activities that must be done (who, when, what); then listen again and fill in the blanks of three sentences: 小张想 (wants to) 今天晚上和老李一起去吃日本饭，____。 小张说明天中午可以吗？老李说____。 老李请小张去他家吃晚饭，小张说____。 (audio, not included). "
             "Activity 8: write a paragraph in pinyin about what you plan to do after school today, using the modal verb 得 wherever appropriate, and share it with a partner."),
    ],
    exercises=[
        M("How is 得 pronounced when it means “must”?", "děi", ["dé", "de (neutral)", "dēi"], "The modal verb 得 is děi."),
        M("What does 他得去看医生 mean?", "He has to go and see the doctor", ["He went to see the doctor", "He doesn’t want to see the doctor", "He is a doctor"], "得 + verb = must."),
        M("What does 今天晚上我得去学校值班 mean?", "Tonight I have to go to school for duty", ["Tonight I went to school", "Tonight I don’t have duty", "Tonight I want to go to school"], "得 = have to; 值班 = be on duty."),
        M("Which is the negative of 得?", "不用 / 不需要", ["不得", "没得", "不要"], "The negative of 得 is 不用 or 不需要."),
        M("What does 海军今天不用去操场集合 mean?", "The Navy doesn’t have to go to the drill field today", ["The Navy mustn’t go to the field", "The Navy went to the field", "The Navy has formation today"], "不用 = no need."),
        M("How do you make 你今天晚上得值班 a question?", "Add 吗: 你今天晚上得值班吗？", ["Add 得: 你得今天晚上得值班？", "Swap the order: 值班得你今天晚上？", "Add 不: 你不今天晚上得值班？"], "Subject + 得 + Verb + Object + 吗？"),
        F("他___去看医生。", "得", PART, "得 (děi) is “must”."),
        F("他们也得去操场___吗？", "集合", ["作业", "预习", "已经"], "去操场集合: go to the drill field for formation."),
        F("你今天晚上得值班___？", "吗", ["们", "呢", "了"], "Subject + 得 + Verb + Object + 吗？ — 们 and 呢 do not make this a yes/no question."),
        F("海军今天不___去操场集合。", "用", PART, "不用 means “need not”."),
        mean("得", "dei3", "have to, must", ["want to", "go to", "get used to"]),
    ],
)

# ------------------------------------------------------------------ 7. 又…又…
YOU = [
    ("他又喜欢滑雪又喜欢游泳。", "He likes both skiing and swimming."), ("他又工作又上大学。", "He both works and goes to college."), ("今天旧金山又刮风又下雨。", "Today San Francisco is both windy and rainy."),
    ("他又是儿子又是爸爸。", "He is both a son and a father."), ("他又是老师又是军人。", "He is both a teacher and a soldier."), ("我们这儿又舒服又好玩儿。", "It is both comfortable and fun here."),
]
Y_VERBS = [("学中文", "study Chinese"), ("教英文", "teach English"), ("值班", "be on duty"), ("锻炼身体", "exercise"), ("喜欢", "like"), ("下雨", "rain"), ("下雾", "be foggy"), ("刮风", "be windy")]
Y_ADJ = [("好玩", "fun"), ("高兴", "happy"), ("可爱", "cute"), ("舒服", "comfortable"), ("有意思", "interesting"), ("好", "good"), ("早", "early"), ("凉快", "cool"), ("大", "big")]
Y_NOUN = [("老师", "teacher"), ("医生", "doctor"), ("军人", "soldier"), ("学生", "student"), ("作业", "homework"), ("儿子", "son"), ("女儿", "daughter"), ("公司", "company"), ("学校", "school"), ("工程师", "engineer")]
L7 = lesson(
    "Presentation 1 grammar: the 又…又… construction",
    "他又工作又上大学 · 又大又好 · 又是老师又是军人",
    requires=[],
    cards=[
        card("又…又…: both … and …",
             "The 又…又… construction connects two expressions to show a coordinate relationship. It emphasizes that the situations or qualities in the two expressions exist together. The book’s example is 他又喜欢滑雪又喜欢游泳. It is used to connect two verbal expressions (又 + Verbal Expression 1 + 又 + Verbal Expression 2) or two adjectival expressions (又 + Adjectival Expression 1 + 又 + Adjectival Expression 2). Nouns can be joined with 又是…又是….",
             examples=[D(z, e) for z, e in YOU]),
        card("Activity 9 and Activity 10",
             "Activity 9: listen to six statements and revise them with 又…又…, then ask a partner a question about each (audio, not included). "
             "Activity 10: pair up. Take turns picking two appropriate expressions from the lists below and asking your partner to connect them in a sentence with 又…又…. Each person thinks up and says three sentences aloud, then writes them in a table. The book’s example is 儿子，女儿 → 张老师又有儿子又有女儿。 Then read your partner’s sentences and choose one to read to the class.",
             tables=[wtable(rows_py(Y_VERBS), headers=("Verbs", "Pinyin", "Meaning")), wtable(rows_py(Y_ADJ), headers=("Adjectives", "Pinyin", "Meaning")), wtable(rows_py(Y_NOUN), headers=("Nouns", "Pinyin", "Meaning"))],
             examples=[D("张老师又有儿子又有女儿。", "Teacher Zhang has both a son and a daughter.")]),
    ],
    exercises=[
        M("What does 又…又… mean?", "both … and …", ["neither … nor …", "first … then …", "sometimes … sometimes …"], "又…又… joins two things that are both true."),
        M("What does 他又工作又上大学 mean?", "He both works and goes to college", ["He neither works nor studies", "He works, then goes to college", "He sometimes works"], "又工作又上大学."),
        M("What does 今天旧金山又刮风又下雨 mean?", "Today San Francisco is both windy and rainy", ["Today San Francisco is neither windy nor rainy", "Today it is windy, then rainy", "San Francisco is a windy city"], "又刮风又下雨."),
        M("What does 他又是老师又是军人 mean?", "He is both a teacher and a soldier", ["He is a teacher, not a soldier", "He is neither", "He was a soldier, then a teacher"], "又是…又是… joins nouns."),
        M("What does 我们这儿又舒服又好玩儿 mean?", "It is both comfortable and fun here", ["It is neither comfortable nor fun here", "It is comfortable but not fun", "It is fun sometimes"], "又舒服又好玩儿."),
        M("What does 张老师又有儿子又有女儿 mean?", "Teacher Zhang has both a son and a daughter", ["Teacher Zhang has a son or a daughter", "Teacher Zhang has no children", "Teacher Zhang is a son"], "又有…又有…"),
        F("他___喜欢滑雪又喜欢游泳。", "又", PART, "又…又… needs 又 twice."),
        F("我们这儿又舒服___好玩儿。", "又", PART, "又舒服又好玩儿."),
        F("他又是老师又是___。", "军人", ["作业", "操场", "已经"], "又是老师又是军人: both a teacher and a soldier."),
        F("今天旧金山又刮风又___。", "下雨", ["学习", "预习", "值班"], "刮风 and 下雨 both describe weather."),
        M("Which sentence is correct?", "他又工作又上大学。", ["他又工作上大学又。", "他工作又又上大学。", "又他工作上大学又。"], "又 + expression 1 + 又 + expression 2."),
        mean("又", "you4", "both … and (in 又…又…)", ["but", "go to", "because"]),
    ],
)

# ------------------------------------------------------------------ 8. time when and time spent
WHEN = [("我们早上六点半集合。", "We have formation at 6:30 in the morning."), ("早上七点四十五分我们上课。", "At 7:45 in the morning we have class.")]
SPENT = [("（我做作业）差不多要做两个小时。", "(I do homework) for about two hours.")]
L8 = lesson(
    "Presentation 1 grammar: “time when” and “time spent”",
    "早上六点半集合 · 做两个小时 · 差不多",
    requires=[],
    cards=[
        card("Word order: when something happens and how long it lasts",
             "In Chinese, when telling what time an action occurs, the time word must be before the verb or before the subject. When stating how long an action lasts, the duration must come after the verb. The book’s examples for the time when are below; the duration example is from Presentation 2’s dialog (大卫：差不多要做两个小时).",
             examples=[D(z, e) for z, e in WHEN] + [D("我做作业差不多要做两个小时。", "I do homework for about two hours.")]),
        card("Putting it together",
             "Time when: Subject + time + verb, or time + subject + verb (我们早上六点半集合 / 早上七点四十五分我们上课). Time spent: verb + duration (做两个小时). The two can go in one sentence: 我早上做作业做两个小时 (“In the morning I do homework for two hours”).",
             examples=[D("我们早上做作业做两个小时。", "In the morning we do homework for two hours.")]),
    ],
    exercises=[
        M("Where does the time word go for “when an action happens”?", "Before the verb or before the subject", ["After the verb", "At the end of the sentence only", "Anywhere"], "我们早上六点半集合 / 早上六点半我们集合."),
        M("Where does the duration go for “how long an action lasts”?", "After the verb", ["Before the subject", "Before the verb", "At the start of the sentence"], "做两个小时: the duration follows the verb."),
        M("Which sentence is correct for “We have formation at 6:30 in the morning”?", "我们早上六点半集合。", ["我们集合早上六点半。", "集合我们早上六点半。", "早上我们集合六点半。"], "Time word before the verb."),
        M("Which sentence is correct for “I do homework for two hours”?", "我做作业做两个小时。", ["我两个小时做作业做。", "我做两个小时作业做。", "两个小时我做做作业。"], "Verb + duration, after the verb is repeated."),
        M("Which sentence means “At 7:45 we have class”?", "七点四十五分我们上课。", ["我们上课七点四十五分。", "上课七点四十五分我们。", "我们七点上课四十五分。"], "Time + subject + verb."),
        F("我们早上六点半___。", "集合", ["作业", "预习", "已经"], "The time word comes before 集合."),
        F("我做作业差不多要做两个___。", "小时", ["作业", "操场", "节课"], "小时 means “hour”; 两个小时 is two hours."),
        mean("差不多", "cha4 bu4 duo1", "about, almost", ["often", "every day", "must"]),
    ],
)

# ------------------------------------------------------------------ 9. the emails
MAIL_A = [
    ("小山：", "Xiaoshan:"), ("你好！现在我们学习很忙。每天早上七点三刻开始上课，下午四点半下课。", "Hello! We are very busy studying now. Every morning class begins at a quarter to eight, and finishes at 4:30 in the afternoon."),
    ("白天我们要上六节课，晚饭以后还得上两节课。不过我已经习惯了。", "In the daytime we have six classes, and after dinner we have to have two more. But I have already gotten used to it."),
    ("今天是星期六，作业不多，下午我要出去锻炼身体。现在西安的天气不冷也不热，我很喜欢。", "Today is Saturday, there is not much homework, and this afternoon I am going out to exercise. The weather in Xi’an now is neither cold nor hot, and I like it very much."),
    ("你们学校怎么样？现在你每天做什么？", "How is your school? What do you do every day now?"), ("大卫", "David"),
]
MAIL_B = [
    ("琳达：", "Linda:"), ("你好！现在我已经是一家中学的英文老师了！我们的学校又大又好，我非常喜欢。", "Hello! I am already an English teacher at a middle school now! Our school is both big and good, and I like it very much."),
    ("我每天早上七点以前去学校。我上午教第一节和第三节课，下午教第二节课。", "Every morning I go to school before 7:00. In the morning I teach the first and third classes, and in the afternoon the second class."),
    ("上午第一节课七点半开始，第三节课九点半开始，下午第二节课是两点开始。", "In the morning the first class begins at 7:30 and the third at 9:30; the second class in the afternoon begins at 2:00."),
    ("下午四点大家都下课以后，我会在教室里和学生说说话，看看他们的作业。", "At 4:00 in the afternoon, after everyone has finished class, I talk with the students in the classroom and look at their homework."),
    ("现在你每天几点开始上课？下课以后做什么？晚上呢？", "What time does your class begin every day now? What do you do after class? And in the evening?"), ("马文", "Ma Wen"),
]
SAT = [("星期六你一般做什么？", "What do you usually do on Saturdays?"), ("你几点做？", "When do you do it?"), ("你在哪儿做？", "Where do you do it?")]
L9 = lesson(
    "Presentation 1 skill integration: two emails",
    "小山 · 琳达 · 每天早上七点三刻开始上课 · 我已经习惯了",
    requires=[],
    cards=[
        card("Activity 2 (Reading, Writing and Speaking): Email A and Email B",
             "Pair up. Read Email A while your partner reads Email B. Then ask your partner for the main idea of the email they read, and the details about who, what, when, where and any other information about each activity; take notes in pinyin or characters. Finally, based on your notes, write an email in pinyin or characters to answer the two questions at the end of the email your partner read.\nEmail A, from David to Xiaoshan:",
             examples=[D(z, e) for z, e in MAIL_A]),
        card("Email B, from Ma Wen to Linda", "", examples=[D(z, e) for z, e in MAIL_B]),
        card("Activity 3 (Speaking and Writing): what do you do on Saturdays?",
             "In groups of three, each student interviews two other students to find out what they usually do on Saturdays, when and where (consult a dictionary if necessary), recording what, when and where in a table. Then take turns naming one activity mentioned and ask the other students to tell you who does what, when and where, and tell the class about one of your group’s activities. Three questions you can use:",
             examples=[D(z, e) for z, e in SAT]),
    ],
    exercises=[
        M("Who writes Email A?", "David (大卫), to 小山", ["Ma Wen, to Linda", "Linda, to David", "Xiaoshan, to Ma Wen"], "The signature is 大卫."),
        M("When do classes begin in Email A?", "A quarter to eight in the morning", ["Half past seven", "Nine", "Eight-thirty"], "每天早上七点三刻开始上课 (7:45)."),
        M("When do classes finish in Email A?", "4:30 in the afternoon", ["2:50", "3:30", "6:00"], "下午四点半下课."),
        M("How many classes do they have in the daytime in Email A?", "Six, and two more after dinner", ["Two", "Six, and none after dinner", "Eight in the daytime"], "白天我们要上六节课，晚饭以后还得上两节课."),
        M("What does the writer of Email A plan for Saturday afternoon?", "Go out to exercise", ["Do a lot of homework", "Be on duty", "Take a class"], "下午我要出去锻炼身体."),
        M("What is the weather like in Xi’an in Email A?", "Neither cold nor hot", ["Very cold", "Very hot", "Rainy"], "现在西安的天气不冷也不热."),
        M("What is Ma Wen’s job?", "English teacher at a middle school", ["Student at a military school", "Doctor", "Engineer"], "我已经是一家中学的英文老师了."),
        M("What is Ma Wen’s school like?", "Both big and good", ["Small and old", "Big but bad", "Far away"], "我们的学校又大又好."),
        M("When does Ma Wen go to school every morning?", "Before 7:00", ["After 9:00", "At noon", "At 8:30"], "我每天早上七点以前去学校."),
        M("When does the first class begin in Email B?", "7:30", ["9:30", "2:00", "4:00"], "第一节课七点半开始."),
        M("When does the second class (afternoon) begin in Email B?", "2:00", ["7:30", "9:30", "4:00"], "下午第二节课是两点开始."),
        M("What does Ma Wen do after everyone finishes class at 4:00?", "Talks with students in the classroom and looks at their homework", ["Goes to the drill field", "Goes home", "Teaches another class"], "我会在教室里和学生说说话，看看他们的作业."),
        F("现在我们学习很___。", "忙", PART, "学习很忙: very busy studying."),
        F("每天早上七点三刻___上课。", "开始", ["作业", "预习", "已经"], "开始上课: class begins."),
        mean("三刻", "san1 ke4", "three quarters of an hour (45 minutes)", ["three minutes", "three hours", "half an hour"]),
    ],
)

# ------------------------------------------------------------------ 10. using Chinese in context
SCHED_MTT = [("1", "8:40 AM", "9:25 AM"), ("2", "9:35 AM", "10:20 AM"), ("Break", "10:20 AM", "10:40 AM"), ("3", "10:40 AM", "11:25 AM"), ("Lunch", "11:25 AM", "12:00 PM"),
             ("4", "12:00 PM", "12:45 PM"), ("5", "12:55 PM", "1:40 PM"), ("Break", "1:40 PM", "2:00 PM"), ("6", "2:00 PM", "2:45 PM"), ("7", "2:55 PM", "3:40 PM")]
SCHED_WF = [("1", "8:40 AM", "9:15 AM"), ("2", "9:25 AM", "10:00 AM"), ("Break", "10:00 AM", "10:20 AM"), ("3", "10:20 AM", "10:55 AM"), ("Lunch", "10:55 AM", "11:20 AM"),
            ("4", "11:20 AM", "11:50 AM"), ("5", "12:00 PM", "12:30 PM"), ("Break", "12:30 PM", "12:50 PM"), ("6", "12:50 PM", "1:20 PM"), ("7", "1:30 PM", "2:00 PM")]
LAOLI = [("老李", "美国中学一天上几节课？", "How many classes does an American middle school have in a day?"), ("你", "一天上七节课。", "Seven classes a day."),
         ("老李", "上午几点上课？", "What time does class start in the morning?"), ("你", "上午八点四十上课。", "Class starts at 8:40 in the morning.")]
CAL = [("8:30 am–9:20 am", "书法课"), ("9:45 am–10:35 am", "书法课"), ("10:50 am–11:40 am", "中国文化课"), ("1:10 pm–2:00 pm", "书法课"), ("2:25 pm–3:15 pm", "书法课"), ("3:45 pm–4:35 pm", "中国文化课"), ("5:00 pm–5:35 pm", "回答问题")]
CAMP = [("6:30 am", "Get up"), ("7:20 am", "Breakfast"), ("12:30 pm", "Lunch"), ("6:40", "Dinner"), ("7:20 pm", "Homework"), ("8:45 pm", "New lesson preview"), ("10:00 pm", "Bedtime")]
CAMP_ZH = [("起床", "qi3 chuang2", "get up"), ("早饭", "zao3 fan4", "breakfast"), ("午饭", "wu3 fan4", "lunch"), ("晚饭", "wan3 fan4", "dinner"), ("做作业", "zuo4 zuo4 ye4", "homework"), ("预习新课", "yu4 xi2 xin1 ke4", "preview the new lesson"), ("睡觉", "shui4 jiao4", "go to bed")]
L10 = lesson(
    "Presentation 1: class schedules, calligraphy and a summer camp",
    "一天上几节课？ · 书法课 · 中国文化课 · 游览 · 看电影",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1: an American middle school’s schedule",
             "Your friend Lao Li is sending his son to America for middle school. You found the school’s class schedule on the Internet and want to share it with Lao Li. A partner plays Lao Li and asks five questions about the schedule; answer them from the daily schedule below. The book’s two examples are in Chinese here (the times are written out):",
             examples=dlg(LAOLI),
             tables=[table(["Period", "Start", "End"], [list(r) for r in SCHED_MTT], title="Daily schedule: Monday, Tuesday and Thursday"),
                     table(["Period", "Start", "End"], [list(r) for r in SCHED_WF], title="Daily schedule: Wednesday and Friday")]),
        card("Activity 1 B: the email",
             "Write an email to Lao Li telling him the times his son is supposed to arrive at and leave school on the different days, and share it with your partner."),
        card("Activity 2 (Speaking, Writing and Reading): calligraphy classes",
             "One of your classmates wants to learn Chinese calligraphy. It is winter break and you have just learned that the East-West Center at the University of Hawaii offers online calligraphy classes. Call your classmate (played by your partner). Before you tell them the good news, find out what their daily schedule during winter break is like and fill in a table in Chinese (time and activity). "
             "Then tell your classmate what the class schedule is like from the table below, after looking at the new words first, and discuss which class they should attend. Remember that California is three hours ahead of Hawaii (the book’s note).",
             tables=[wtable([("书法", "shu1 fa3", "calligraphy"), ("文化", "wen2 hua4", "culture")]), table(["时间 Time", "课程 Course"], [[a, b] for a, b in CAL], title="The class schedule", say=[1])]),
        card("Activity 3 (Listening, Speaking and Writing): a summer camp in China",
             "Your friend’s daughter wants to attend a Chinese summer camp in China, and you offer to look into the camps. A. You call Mr. Sun, who runs a camp in Hangzhou, to find out what a typical day is like there; he returns your call later and leaves a message (audio, not included), and you take notes in English. "
             "Then your friend’s daughter calls Mr. Sun to double-check the schedule and asks about the times of a few other things (the table below). Divide into groups of three to play: 1) Mr. Sun (Chinese only), 2) the daughter (English only), and 3) the interpreter; rotate roles until everyone has interpreted. You can also create your own events and times.",
             tables=[wtable([("游览", "you2 lan3", "tour"), ("看电影", "kan4 dian4 ying3", "watch a movie")]), table(["Activity", "Time"], [[a, b] for b, a in CAMP], title="Camp times to ask about"),
                     wtable(CAMP_ZH, headers=("Activity in Chinese", "Pinyin", "Meaning"))]),
    ],
    exercises=[
        M("How many classes a day does the American middle school have?", "Seven", ["Six", "Eight", "Five"], "一天上七节课。"),
        M("When does period 1 start on Monday?", "8:40 AM", ["8:30 AM", "9:35 AM", "9:15 AM"], "Period 1 starts at 8:40 on every day."),
        M("When does period 1 end on Monday, Tuesday and Thursday?", "9:25 AM", ["9:15 AM", "9:35 AM", "10:20 AM"], "Monday, Tuesday and Thursday period 1: 8:40 to 9:25."),
        M("When does period 1 end on Wednesday and Friday?", "9:15 AM", ["9:25 AM", "10:00 AM", "9:35 AM"], "Wednesday and Friday period 1: 8:40 to 9:15."),
        M("When does lunch begin on Monday?", "11:25 AM", ["10:55 AM", "12:00 PM", "11:20 AM"], "Lunch is 11:25 to 12:00 on Monday."),
        M("When does lunch begin on Wednesday?", "10:55 AM", ["11:25 AM", "12:00 PM", "11:20 AM"], "Lunch is 10:55 to 11:20 on Wednesday."),
        M("When does school end on Monday, Tuesday and Thursday?", "3:40 PM", ["2:00 PM", "2:45 PM", "3:15 PM"], "Period 7 ends at 3:40."),
        M("When does school end on Wednesday and Friday?", "2:00 PM", ["3:40 PM", "1:20 PM", "2:45 PM"], "Period 7 ends at 2:00."),
        M("How long is period 1 on Monday?", "45 minutes", ["35 minutes", "30 minutes", "50 minutes"], "8:40 to 9:25 is 45 minutes."),
        M("How long is period 1 on Wednesday?", "35 minutes", ["45 minutes", "50 minutes", "25 minutes"], "8:40 to 9:15 is 35 minutes."),
        M("What does the 书法课 teach?", "Calligraphy", ["Chinese culture", "Answering questions", "Singing"], "书法 is calligraphy."),
        M("Which course is held at 10:50 am–11:40 am?", "中国文化课 (Chinese culture)", ["书法课 (calligraphy)", "回答问题 (answering questions)", "No class"], "The 10:50 slot is the culture class."),
        M("What is the last item on the calligraphy schedule?", "回答问题 (question time)", ["书法课", "中国文化课", "A break"], "5:00 pm–5:35 pm: 回答问题."),
        M("What does 游览 mean?", "tour", ["watch a movie", "swim", "preview"], "游览 yóulǎn: tour."),
        M("What does 看电影 mean?", "watch a movie", ["tour", "eat", "sleep"], "看电影 kàn diànyǐng."),
        mean("书法", "shu1 fa3", "calligraphy", ["culture", "grammar", "tour"]),
        mean("文化", "wen2 hua4", "culture", ["calligraphy", "grammar", "movie"]),
        mean("睡觉", "shui4 jiao4", "go to bed, sleep", ["get up", "eat", "study"]),
    ],
)

# ------------------------------------------------------------------ 11. vocabulary
L11 = vocab_lesson("Presentation 1 vocabulary (25 words)", "下午 · 下课 · 不过 · 习惯 · 以后 · 作业 · 值班 · 集合",
                   "Vocabulary list (Presentation 1)",
                   "The book’s 25 words, with the traditional form where it differs. 得 is děi here (“have to, must”); 要 is the modal verb “want to”.", VOC1)

UNIT = unit("第七课 校园生活 Presentation 1: the school day, time, 以后, 要, 得 and 又…又…", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])
