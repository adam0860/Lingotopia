"""Unit 20: Lesson 7 (School Life) Presentation 2, from the book's texts: David's school life in Taiwan, 怎么样, the 除了
construction, the complement of degree (1), the two passages about military schools, the emails and the vocabulary list.
The listening activities and the pictures are not included; the lessons say so."""
from zh_auto import *
from zh_l7_vocab import VOC2

PART = ["吗", "们", "呢"]
JIAO = {"教": "jiao1"}

# ------------------------------------------------------------------ 1. the dialog
P2 = [
    ("小文", "大卫，你在台湾的学习生活怎么样？", "David, how is your school life in Taiwan?"),
    ("大卫", "挺好的。开始不太习惯，现在完全适应了。", "Quite good. At first I wasn’t used to it, but now I have completely adjusted."),
    ("小文", "你们每天上几节课？", "How many classes do you have every day?"),
    ("大卫", "五节课。上午三节，下午两节。", "Five classes. Three in the morning and two in the afternoon."),
    ("小文", "都有什么课？", "What classes are there?"),
    ("大卫", "有听力课、阅读课、语法课和说话课。", "There are listening, reading, grammar and speaking classes."),
    ("小文", "你们每天作业多吗？", "Do you have a lot of homework every day?"),
    ("大卫", "还可以。差不多要做两个小时。", "It’s okay. It takes about two hours."),
    ("小文", "考试多不多？", "Are there a lot of tests?"),
    ("大卫", "很多，除了每天的生词考试以外，还有单元和期末考试。", "A lot. Besides the daily vocabulary tests, there are also unit tests and final exams."),
    ("小文", "你学习这么努力，一定考得不错吧？", "You study so hard, so you must do well on tests, right?"),
    ("大卫", "因为老师们教得很好，所以，我差不多每次都得优。", "Because the teachers teach very well, I get an A (优, top grade) almost every time.", {"教": "jiao1", 23: "de2"}),
    ("小文", "太好了。祝贺你！", "Great. Congratulations!"),
    ("大卫", "谢谢。", "Thank you."),
]
PARA = [("琳达是今年八月开始在天津大学学中文的。", "Linda began studying Chinese at Tianjin University this August."), ("她的学习生活很忙，不过她已经适应了。", "Her study life is very busy, but she has already adjusted."),
        ("她每天上午上听力课和说话课，下午上阅读课和语法课。", "Every morning she has listening and speaking classes, and in the afternoon reading and grammar classes."),
        ("除了上课，她每天还有很多作业。", "Besides classes, she has a lot of homework every day."), ("因为她学习很努力，所以每次考试她差不多都得优。", "Because she studies very hard, she gets an A on almost every test.")]
PARA_JUMBLED = [("a", PARA[2][0]), ("b", PARA[4][0]), ("c", PARA[0][0]), ("d", PARA[3][0]), ("e", PARA[1][0])]
L1 = lesson(
    "Presentation 2: school life in Taiwan (dialog)",
    "你在台湾的学习生活怎么样？ · 开始不太习惯，现在完全适应了",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss with your partner: A. How long does it take students to get used to life at DLI? B. What classes do you take every day? How do you say them in Chinese? C. What kind of tests do you have? How do you say those in Chinese?"),
        card("Presentation 2: 小文 asks 大卫 about his life in Taiwan",
             "The book also prints this dialog in traditional characters (for example 大衛，你在台灣的學習生活怎麼樣？).",
             examples=dlg(P2)),
        card("Activities 1 to 3",
             "Activity 1 (Listening): A. Global listening: What kind of information does Xiao Wen want to find out from David? What are the main differences between David’s life in Taiwan and yours at DLI? B. Detailed listening: complete a table about David’s life in Taiwan (life in general, classes, tests, homework, grades). "
             "Activity 2 (Writing): in pairs, complete a table of expressions: kinds of classes and tests; asking how something or someone is; being completely used to something; attending five class periods every day; “in addition to …”; “about two hours”; someone does something well. "
             "Activity 3 (Listening): a dialog about Wang Zhong’s son: what and where he is studying, what classes he takes, how many classes a day, and how he is doing and why (audio, not included). The questions are practiced below from the text."),
        card("Activity 4: rearrange the sentences into a coherent paragraph",
             "A. With a partner, rearrange the five sentences (a to e) to make a paragraph: a. 她每天上午上听力课和说话课，下午上阅读课和语法课。 b. 因为她学习很努力，所以每次考试她差不多都得优。 c. 琳达是今年八月开始在天津大学学中文的。 d. 除了上课，她每天还有很多作业。 e. 她的学习生活很忙，不过她已经适应了。 "
             "B. Read the answer key below and make any necessary changes. The key (order c, e, a, d, b):",
             examples=[D(z, e, fixes={"得": "de2"}) for z, e in PARA]),
    ],
    exercises=[
        M("How many classes does David have every day?", "Five: three in the morning, two in the afternoon", ["Six: four in the morning", "Four", "Seven"], "五节课。上午三节，下午两节。"),
        M("What classes does David have?", "Listening, reading, grammar and speaking", ["Writing, math and history", "Listening and reading only", "Grammar and translation only"], "有听力课、阅读课、语法课和说话课。"),
        M("How long does David’s homework take?", "About two hours", ["About two minutes", "All day", "About five hours"], "差不多要做两个小时。"),
        M("What tests does David have?", "Daily vocabulary tests, unit tests and final exams", ["Only final exams", "Only listening tests", "No tests"], "除了每天的生词考试以外，还有单元和期末考试。"),
        M("Why does David say he gets A’s almost every time?", "Because the teachers teach very well", ["Because tests are easy", "Because he studies a little", "Because he has no homework"], "因为老师们教得很好，所以，我差不多每次都得优。"),
        M("How does David feel about school life now?", "Completely adjusted; at first he wasn’t used to it", ["Still not used to it", "He dislikes it", "He has just arrived"], "开始不太习惯，现在完全适应了。"),
        M("What does Xiao Wen say at the end?", "太好了。祝贺你！ — Great. Congratulations!", ["对不起", "没关系", "再见"], "太好了。祝贺你！"),
        M("What is the first sentence of the paragraph about Linda?", PARA[0][0], [PARA[1][0], PARA[2][0], PARA[4][0]], "It says when and where she began."),
        M("What is the last sentence of the paragraph about Linda?", PARA[4][0], [PARA[0][0], PARA[1][0], PARA[3][0]], "Because of studying hard, she gets A’s."),
        M("What comes right after “她的学习生活很忙，不过她已经适应了”?", PARA[2][0], [PARA[3][0], PARA[4][0], PARA[0][0]], "Then it describes her classes."),
        F("你学习这么努力，一定考___不错吧？", "得", PART, "考得不错: do well on a test."),
        F("除了每天的生词考试以外，___有单元和期末考试。", "还", PART, "除了…以外，还有…: “in addition to …, there are also …”."),
        F("开始不太习惯，现在___适应了。", "完全", ["作业", "操场", "预习"], "完全适应: completely adjusted."),
        mean("考试", "kao3 shi4", "test, examination", ["homework", "class", "vocabulary item"]),
        mean("适应", "shi4 ying4", "get used to, adapt", ["to take a test", "congratulate", "start"]),
    ],
)

# ------------------------------------------------------------------ 2. 怎么样
ZMY = [("他在北京的生活怎么样？", "How is his life in Beijing?"), ("今天的天气怎么样？", "How is the weather today?")]
ZMY_AB = [("甲", "他的身体怎么样？", "How is his health?"), ("乙", "他的身体很好。", "His health is very good."), ("甲", "今天的天气怎么样？", "How is the weather today?"), ("乙", "今天的天气不怎么好。", "Today’s weather is not very good.")]
ZMY_WORDS = [("身体", "How is … health?"), ("中文听力", "listening in Chinese"), ("英语", "English"), ("照片", "photos"), ("中学", "middle school"), ("公司", "company"), ("大学", "university"), ("医院", "hospital"), ("老家", "hometown"), ("中文语法", "Chinese grammar")]
ZMY_ANS = [("很好", "very good"), ("不错", "not bad"), ("还可以", "okay"), ("不怎么好", "not so good"), ("不怎么样", "not so great")]
L2 = lesson(
    "Presentation 2 grammar: the question word 怎么样",
    "他的身体怎么样？ · 今天的天气怎么样？ · 不怎么好 · 还可以",
    requires=[],
    cards=[
        card("怎么样: how is it?",
             "To ask how someone or something is, we often use the question word 怎么样, as in 他在北京的生活怎么样？ and 今天的天气怎么样？ The pattern is Subject + 怎么样？",
             examples=[D(z, e) for z, e in ZMY] + dlg(ZMY_AB)),
        card("Answers: 不错, 还可以, 不怎么好, 不怎么样",
             "The book’s model question is 大卫的爷爷的身体怎么样？ and the answer 他爷爷的身体很好 (or 不错, 还可以, 不怎么好, 不怎么样). 不怎么 + adjective is a mild negative, “not very …”.",
             tables=[wtable(rows_py(ZMY_ANS), headers=("Answer", "Pinyin", "Meaning"))],
             examples=[D("大卫的爷爷的身体怎么样？", "How is David’s grandfather’s health?"), D("他爷爷的身体很好。", "His grandfather’s health is very good.")]),
        card("Activity 1 (Speaking and Writing)",
             "Pair up as Student A and Student B. Ask five questions using the words in your column and 怎么样; your partner writes your questions and then changes them into statements. Student A’s words: 身体, 中文听力, 英语, 照片, 中学. Student B’s words: 公司, 大学, 医院, 老家, 中文语法.",
             tables=[wtable(rows_py(ZMY_WORDS), headers=("Word", "Pinyin", "Meaning"))]),
    ],
    exercises=[
        M("What does 今天的天气怎么样？ ask?", "How is the weather today?", ["What day is it today?", "Is it raining today?", "Where is the weather?"], "怎么样 asks “how is it?”"),
        M("What does 不怎么好 mean?", "not very good", ["very good", "not bad", "terrible"], "不怎么 + adjective: “not very”."),
        M("What does 不错 mean?", "not bad", ["not good", "very bad", "not very good"], "不错 is a compliment."),
        M("What does 还可以 mean?", "okay", ["great", "terrible", "no way"], "还可以 is “okay, so-so”."),
        M("Which is a positive answer to “他的身体怎么样？”?", "他的身体很好。", ["他的身体不怎么好。", "他的身体不怎么样。", "他的身体很不好。"], "很好 is the positive one."),
        M("Which is a negative answer to “今天的天气怎么样？”?", "今天的天气不怎么好。", ["今天的天气很好。", "今天的天气不错。", "今天的天气还可以。"], "不怎么好 is negative."),
        F("他在北京的生活___样？", "怎么", PART, "怎么样: how is it?"),
        F("今天的天气不___好。", "怎么", PART, "不怎么好: not very good."),
        F("大卫的爷爷的身体怎么样？ 他爷爷的身体很___。", "好", ["们", "吗", "呢"], "很好: very good."),
        mean("怎么样", "zen3 me5 yang4", "how about, how is it", ["what time", "which one", "why"]),
        mean("不错", "bu2 cuo4", "not bad", ["not good", "very bad", "so-so"]),
    ],
)

# ------------------------------------------------------------------ 3. 除了
CL = [("我们除了上听力课以外，还/也上阅读课。", "Besides having listening class, we also have reading class."),
      ("除了上听力课以外，我们还/也上阅读课。", "Besides having listening class, we also have reading class."),
      ("除了星期三，星期五早上我们还/也要集合。", "Besides Wednesday, on Friday mornings we also have formation."),
      ("我们班的同学除了班长以外，都不是陆军。", "In our class, except for the class leader, nobody is in the Army."),
      ("除了班长以外，我们班的同学都不是陆军。", "Except for the class leader, nobody in our class is in the Army.")]
CL2 = [("甲：除了琳达以外，我们班谁还是陆军？", "Besides Linda, who else in our class is in the Army?"), ("乙：除了琳达以外，马强和我也是陆军。", "Besides Linda, Ma Qiang and I are in the Army too."),
       ("甲：除了大卫以外，谁还喜欢德州的天气？", "Besides David, who else likes Texas weather?"), ("乙：除了大卫以外，谁都不喜欢德州的天气。", "Besides David, nobody likes Texas weather.")]
CL3 = [("冬天除了山上以外，这几个地方都不经常下雪。", "In winter, except for the mountains, it doesn’t snow often in these places."), ("冬天除了纽约以外，华盛顿也经常下雪。", "In winter, besides New York, it also often snows in Washington."),
       ("除了大卫以外，我们都不是加州大学的学生。", "Except for David, none of us is a student of the University of California."), ("除了大卫以外，我们也是加州大学的学生。", "Besides David, we are also students of the University of California.")]
CL_EXPR = [("喜欢游泳", "like to swim"), ("每天学中文", "study Chinese every day"), ("很有意思", "is interesting"), ("锻炼身体", "exercise"), ("很可爱", "is cute"), ("国防语言学院", "the Defense Language Institute")]
L3 = lesson(
    "Presentation 2 grammar: the 除了… (以外) construction",
    "除了…以外，还… · 除了…以外，都… · 除了班长以外",
    requires=[],
    cards=[
        card("除了…(以外): in addition to, or except for",
             "When 除了… (以外) is used with 还 or 也, it means “in addition to …”. Using 以外 is optional. For example: 我们每天除了学中文（以外），还/也锻炼身体。 When it is used with the adverb 都, it shows exclusiveness and means “with the exception of …”. For example: 除了小王（以外），我们都喜欢锻炼身体。",
             examples=[D("我们每天除了学中文以外，还锻炼身体。", "Every day, besides studying Chinese, we also exercise."), D("除了小王以外，我们都喜欢锻炼身体。", "Except for Xiao Wang, we all like to exercise.")]),
        card("The patterns",
             "In addition to … Same subject: Subject + 除了…，也/还…。 or 除了…，Subject + 也/还…。 Different subjects: 除了 Subject A…，Subject B 也/还…。 Except for … Same subject: Subject + 除了…，都…。 or 除了…，Subject + 都…。 Different subjects: 除了 Subject A…，Subject B (the rest) 都…。"),
        card("Examples (the book’s five)", "The book gives these without English; the translations are added.", examples=[D(z, e) for z, e in CL]),
        card("Activity 2 (Listening and Reading)",
             "A. Listen to a dialog and answer: In this class, who doesn’t attend formation every morning and why? In addition to formation, what else do they do every morning? Where do they have morning formation? B. Share your answers in pairs. C. Check against the script (audio, not included)."),
        card("Activity 3 (Speaking and Writing)",
             "A. Pair up. Using the 除了 construction, think of someone in your class and ask your partner if anyone else in the class has something in common with them. If no one does, use 都 to show exclusivity. Take notes (who, things in common, exceptions). The book’s two examples are 琳达，陆军 and 大卫，德州的天气:",
             examples=[D(z, e) for z, e in CL2]),
        card("Activity 3 B",
             "Think of a sentence using the 除了… construction and one of the expressions below. Your partner tries to guess the sentence; when they get it right, switch and do the next expression, until all the expressions have been used. Write your partner’s questions in a table. The book’s examples (经常下雪 and 加州大学):",
             tables=[wtable(rows_py(CL_EXPR), headers=("Expression", "Pinyin", "Meaning"))], examples=[D(z, e) for z, e in CL3]),
    ],
    exercises=[
        M("What does 除了…以外，还… mean?", "in addition to …, also …", ["except for …", "instead of …", "before …"], "With 还 or 也, 除了 means “in addition to”."),
        M("What does 除了…以外，都… mean?", "except for …, all …", ["in addition to …", "because of …", "after …"], "With 都, 除了 means “except for”."),
        M("What does 我们班的同学除了班长以外，都不是陆军 mean?", "Except for the class leader, nobody in our class is in the Army", ["Besides the class leader, we are also in the Army", "Everyone in our class is in the Army", "The class leader is not in the Army"], "除了…都不…: exception."),
        M("What does 除了上听力课以外，我们还上阅读课 mean?", "Besides listening class, we also have reading class", ["Except for listening class, we have no class", "We have listening class instead of reading class", "We don’t have reading class"], "除了…还…: in addition."),
        M("What does 除了大卫以外，谁都不喜欢德州的天气 mean?", "Besides David, nobody likes Texas weather", ["David doesn’t like Texas weather", "Everybody likes Texas weather", "Besides David, others like it too"], "谁都不: nobody."),
        M("Is 以外 required in the 除了 construction?", "No, it is optional", ["Yes, always", "Only with 都", "Only with 还"], "The use of 以外 is optional."),
        F("除了星期三，星期五早上我们___要集合。", "还", PART, "还 / 也 means “also” in the “in addition to” pattern."),
        F("除了班长以外，我们班的同学___不是陆军。", "都", PART, "都 shows exclusiveness: the rest all …"),
        F("我们___了上听力课以外，还上阅读课。", "除", PART, "除了…以外."),
        F("除了琳达以外，我们班谁___是陆军？", "还", PART, "谁还…: “who else …?”"),
        mean("除了", "chu2 le5", "except; besides", ["already", "plus", "complete"]),
    ],
)

# ------------------------------------------------------------------ 4. complement of degree (1)
DEG = [("中文字大卫写得怎么样？", "How does David write Chinese characters?"), ("他写得很好。", "He writes very well."), ("昨天的作业她做得怎么样？", "How did she do yesterday’s homework?"), ("她做得真好。", "She did it really well."),
       ("你们那儿雨下得大吗？", "Does it rain hard where you are?"), ("我们这儿雨下得很大。", "It rains very hard here."), ("旧金山的雾下得大，蒙特雷的雾下得不大。", "San Francisco’s fog is heavy; Monterey’s fog is not heavy. (a comparison)")]
DEG_NEG = [("她做得不好。", "She didn’t do it well."), ("我说得不好。", "I don’t speak well."), ("他做得好不好？", "Did he do it well?"), ("旧金山的雾下得大不大？", "Is San Francisco’s fog heavy?"),
           ("今天她来得早不早？", "Did she come early today?"), ("今天她来得很早吗？", "Did she come very early today?")]
DEG_OBJ = [("他做作业做得很好。", "He does homework very well."), ("他作业做得很好。", "He does homework very well."), ("作业他做得很好。", "As for homework, he does it very well."),
           ("她说中文说得很好。", "She speaks Chinese very well."), ("她中文说得很好。", "She speaks Chinese very well."), ("中文她说得很好。", "As for Chinese, she speaks it very well."),
           ("她考听力考得很好。", "She does very well on listening tests."), ("她听力考得很好。", "She does very well on listening tests."), ("听力她考得很好。", "As for listening, she does very well on the tests.")]
L4 = lesson(
    "Presentation 2 grammar: the complement of degree (1)",
    "他写得很好 · 她说中文说得很好 · 她做得不好 · 他做得好不好？",
    requires=[],
    cards=[
        card("得 + complement: judging how an action is done",
             "The Complement of Degree is often used to judge or comment on an action. It normally needs an adverb of degree, as in 她说中文说得真好, where 真 is the adverb of degree that modifies the complement 好. If there is no adverb of degree before the complement, it implies a comparison: 她说中文说得好 suggests that she speaks Chinese well compared with some others. "
             "The pattern is Subject + Verb + 得 + (Adverb of Degree +) Complement. Here 得 is the structural particle, pronounced de (neutral tone), not děi.",
             examples=[D(z, e) for z, e in DEG]),
        card("Negative and affirmative-negative questions",
             "Negative and affirmative-negative questions do NOT take adverbs of degree. Negative: Subject + Verb + 得 + 不 + Complement. Question: Subject + Verb + 得 + Complement + 不 + Complement? Or: Subject + Verb + 得 + (Adverb of Degree +) Complement + 吗？",
             examples=[D(z, e) for z, e in DEG_NEG]),
        card("A verb with an object",
             "With a transitive verb (verb + object), the verb is repeated after the object and before 得; the complement of degree then comes after 得. The object can also be moved to the front of the sentence, either before the predicate or before the entire sentence. Patterns: Subject + Verb1 + Object + Verb1 + 得 + Complement; Subject + Object + Verb + 得 + Complement; Object + Subject + Verb + 得 + Complement.",
             examples=[D(z, e) for z, e in DEG_OBJ]),
        card("Activity 4 (Writing)",
             "Using the words in the table, write sentences for each of seven items: 1. Someone does something well. 2. Someone does not do something well. 3. Someone does something really well. 4. Someone does not do something very well. 5. Ask if someone does something really well. 6. It rained really hard some place this summer. 7. It didn’t snow very hard some place this winter. "
             "The book’s example: someone does something really well 大卫说中文说得非常好。 and the question 大卫说中文说得非常好吗？ Then share your sentences with a partner and make any necessary corrections.",
             examples=[D("大卫说中文说得非常好。", "David speaks Chinese really well."), D("大卫说中文说得非常好吗？", "Does David speak Chinese really well?")],
             tables=[wtable(rows_py([("听力", "listening"), ("语法", "grammar"), ("说话", "speaking"), ("阅读", "reading"), ("学习", "study"), ("温度", "temperature"), ("考试", "test"), ("天气", "weather")]), headers=("Nouns", "Pinyin", "Meaning")),
                     wtable(rows_py([("说", "speak"), ("写", "write"), ("读", "read"), ("教", "teach"), ("游泳", "swim"), ("滑雪", "ski"), ("下雨", "rain"), ("下雪", "snow"), ("刮风", "be windy")], JIAO), headers=("Verbs", "Pinyin", "Meaning")),
                     wtable(rows_py([("好", "good"), ("大", "big"), ("小", "small"), ("少", "few"), ("可爱", "cute"), ("有意思", "interesting"), ("舒服", "comfortable"), ("忙", "busy"), ("早", "early"), ("高兴", "happy"), ("好玩", "fun")]), headers=("Adjectives", "Pinyin", "Meaning"))]),
    ],
    exercises=[
        M("What does 他写得很好 mean?", "He writes very well", ["He writes a lot", "He wrote it yesterday", "He is a good writer"], "Verb + 得 + very + adjective."),
        M("What does 她做得真好 mean?", "She did it really well", ["She did it a lot", "She didn’t do it well", "She is real"], "真 is the adverb of degree."),
        M("What does 她说中文说得很好 mean?", "She speaks Chinese very well", ["She speaks very much Chinese", "She likes Chinese", "She speaks Chinese a little"], "Verb + object + verb + 得 + complement."),
        M("Which is the correct negative of “She did it well”?", "她做得不好。", ["她不做得好。", "她做不得好。", "她没做得好。"], "Subject + Verb + 得 + 不 + Complement."),
        M("Which is the correct affirmative-negative question for “Did he do it well?”", "他做得好不好？", ["他做好不好得？", "他得做好不好？", "他不做得好？"], "Verb + 得 + complement + 不 + complement."),
        M("Which sentence puts the object first?", "作业他做得很好。", ["他做作业做得很好。", "他作业做得很好。", "他做得作业很好。"], "Object + Subject + Verb + 得 + Complement."),
        M("Which sentence is correct for “She speaks Chinese very well”?", "她说中文说得很好。", ["她说中文得很好。", "她说得中文很好。", "她说中文说很好得。"], "The verb is repeated after the object, before 得."),
        M("What does 她说中文说得好 (no adverb) imply?", "She speaks Chinese well compared with others", ["She speaks very, very well", "She doesn’t speak Chinese", "She speaks only Chinese"], "Without an adverb of degree there is a comparison."),
        M("Do negative questions take adverbs of degree?", "No", ["Yes, always 很", "Only 真", "Only 非常"], "Negative and affirmative-negative questions do not take adverbs of degree."),
        F("她做___不好。", "得", PART, "做得不好: didn’t do it well."),
        F("他说中文说___很好。", "得", PART, "The structural particle 得 follows the verb."),
        F("她说中文___得很好。", "说", ["们", "吗", "呢"], "The verb is repeated: 说中文说得很好."),
        F("他做得好___好？", "不", PART, "好不好: affirmative-negative question."),
        F("今天她来得早不___？", "早", ["们", "吗", "呢"], "早不早: affirmative-negative question."),
        F("旧金山的雾下得大___大？", "不", PART, "大不大: is it heavy?"),
        mean("得", "de5", "structural particle (as in 说得好)", ["have to, must", "go to", "get used to"]),
    ],
)

# ------------------------------------------------------------------ 5. Passages A and B
PA = [
    ("我叫王军，是中国国防大学的学生。", "My name is Wang Jun, and I am a student at China’s National Defense University."),
    ("我是去年上大学的，现在已经完全适应军校的生活了。", "I started college last year, and now I have completely adjusted to life at a military school."),
    ("我每天早上五点三刻起床。起床以后，我先去操场集合，然后去吃早饭。", "Every morning I get up at a quarter to six. After I get up, I first go to the drill field for formation, and then go to eat breakfast."),
    ("我们每天有七节课。上午七点半到教室去上课，十一点二十分下课。", "We have seven classes every day. In the morning at 7:30 we go to the classroom for class, and class ends at 11:20."),
    ("十一点半我去吃午饭。下午一点开始上课，三点五十分下课。", "At 11:30 I go to eat lunch. In the afternoon class begins at 1:00 and ends at 3:50."),
    ("下课以后，我们得到操场去锻炼身体。", "After class, we have to go to the drill field to exercise.", {"得": "dei3"}),
    ("我晚上六点半吃晚饭。晚饭以后，我和同学们一起做作业。我十点十五分睡觉。", "I eat dinner at 6:30 in the evening. After dinner, my classmates and I do homework together. I go to bed at 10:15."),
]
PB = [
    ("我叫李明，是中国人民解放军外语学院英语系的学生。", "My name is Li Ming, and I am a student in the English Department of the Foreign Language Institute of the PLA."),
    ("我每天都很忙，除了上课以外，还要做很多作业，有时候还得值班。", "I am busy every day: besides going to class, I have to do a lot of homework, and sometimes I also have to be on duty.", {"得": "dei3"}),
    ("我们每天上七节课。我早上六点起床，然后去操场集合，六点四十吃早饭。", "We have seven classes every day. I get up at 6:00, and then go to the drill field for formation, and I eat breakfast at 6:40."),
    ("上午八点到十二点，我们上英语听力和阅读课，下午一点到五点，我们上说话课、语法课，还有翻译课。", "From 8:00 to 12:00 in the morning we have English listening and reading classes; from 1:00 to 5:00 in the afternoon we have speaking class, grammar class, and also translation class."),
    ("下午五点到六点我锻炼身体。因为我们有很多作业，所以我常常晚上十点半以后睡觉。", "From 5:00 to 6:00 in the afternoon I exercise. Because we have a lot of homework, I often go to bed after 10:30 in the evening."),
    ("我们没有生词考试，但是每一课都有考试，还有单元考试和期末考试。", "We don’t have vocabulary tests, but there is a test for every lesson, and also unit tests and final exams."),
    ("我学习很努力，所以考得不错。", "I study very hard, so I do well on tests."),
]
PAB_WORDS = [("翻译", "fan1 yi4", "translation, translate"), ("国防大学", "guo2 fang2 da4 xue2", "National Defense University"), ("人民解放军", "ren2 min2 jie3 fang4 jun1", "People’s Liberation Army"), ("外语学院", "wai4 yu3 xue2 yuan4", "Foreign Language Institute"), ("英语系", "ying1 yu3 xi4", "English Department")]
L5 = lesson(
    "Presentation 2 skill integration: two military-school passages",
    "王军 · 李明 · 每天有七节课 · 起床以后，我先去操场集合，然后去吃早饭",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Writing and Reading)",
             "Three recordings are matched with pictures (the third dialog adds the word 难 nán, difficult). In groups of three each person listens to one dialog and completes a table (what the dialog is about and three details), then translates its first four lines, and asks the other two students for the rest of the information. Audio and pictures are not included."),
        card("Activity 2 (Reading, Writing and Speaking): Passage A and Passage B",
             "Divide into two groups. Group 1 reads Passage A while Group 2 reads Passage B, and each completes a table in pinyin or characters: who the passage is about; what it is about; the AM activities and times; the PM activities and times. Then pair up with someone from the other group and ask them questions in Chinese to complete your table. With your new partner, write a Chinese dialog between one of you and one of the persons in the passages, and act it out.\nPassage A:",
             examples=[D(z[0], z[1], fixes=(z[2] if len(z) > 2 else None)) for z in PA]),
        card("Passage B", "", examples=[D(z[0], z[1], fixes=(z[2] if len(z) > 2 else None)) for z in PB]),
        card("Names and words in the passages", "", tables=[wtable(PAB_WORDS)]),
        card("Activity 3 (Speaking and Writing)",
             "In Chinese, ask three of your classmates about their classes on a particular day. Also ask how much time they spend on each of the following homework or study areas: listening, reading, writing and vocabulary. Take notes in pinyin or characters, and share your information with the class in Chinese."),
    ],
    exercises=[
        M("Who is Passage A about?", "王军, a student at China’s National Defense University", ["李明, a student at a foreign language institute", "大卫", "A teacher"], "我叫王军，是中国国防大学的学生。"),
        M("When did 王军 start college?", "Last year", ["This year", "Three years ago", "Last month"], "我是去年上大学的。"),
        M("What time does 王军 get up?", "5:45 (a quarter to six)", ["6:00", "5:30", "7:30"], "我每天早上五点三刻起床。"),
        M("What does 王军 do after he gets up?", "Goes to the drill field for formation, then eats breakfast", ["Eats breakfast, then goes to class", "Does homework", "Goes to bed"], "起床以后，我先去操场集合，然后去吃早饭。"),
        M("How many classes does 王军 have every day, and when does the morning class end?", "Seven; the morning class ends at 11:20", ["Six; at 11:30", "Seven; at 12:00", "Five; at 10:50"], "我们每天有七节课。… 十一点二十分下课。"),
        M("What time does 王军 eat dinner?", "6:30", ["5:30", "7:30", "6:00"], "我晚上六点半吃晚饭。"),
        M("What time does 王军 go to bed?", "10:15", ["10:50", "9:15", "11:15"], "我十点十五分睡觉。"),
        M("Who is Passage B about?", "李明, an English Department student at the PLA Foreign Language Institute", ["王军", "大卫", "Linda"], "我叫李明，是中国人民解放军外语学院英语系的学生。"),
        M("What time does 李明 get up?", "6:00", ["5:45", "6:40", "8:00"], "我早上六点起床。"),
        M("When does 李明 eat breakfast?", "6:40", ["6:00", "7:30", "8:00"], "六点四十吃早饭。"),
        M("What classes does 李明 have in the afternoon?", "Speaking, grammar and translation", ["Listening and reading", "Only grammar", "Calligraphy"], "下午一点到五点，我们上说话课、语法课，还有翻译课。"),
        M("When does 李明 exercise?", "From 5:00 to 6:00 in the afternoon", ["In the morning at 6:00", "After 10:30 at night", "At noon"], "下午五点到六点我锻炼身体。"),
        M("Why does 李明 often go to bed after 10:30?", "Because they have a lot of homework", ["Because he has duty every night", "Because he has no classes", "Because he likes movies"], "因为我们有很多作业，所以我常常晚上十点半以后睡觉。"),
        M("Does 李明’s school have vocabulary tests?", "No, but every lesson has a test, plus unit and final exams", ["Yes, every day", "No tests at all", "Only final exams"], "我们没有生词考试，但是每一课都有考试，还有单元考试和期末考试。"),
        mean("翻译", "fan1 yi4", "translation, translate", ["calligraphy", "grammar", "listening"]),
        mean("睡觉", "shui4 jiao4", "go to bed, sleep", ["get up", "eat", "exercise"]),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese in context
CLASSES = [("听力课", "listening class"), ("阅读课", "reading class"), ("语法课", "grammar class"), ("说话课", "speaking class"), ("写作课", "writing class (xiězuò kè)"), ("翻译课", "translation class (fānyì kè)"),
           ("辩论课", "debate class (biànlùn kè)"), ("自习课", "self-study class (zìxí kè)")]
MAIL = [
    ("苏教官：", "Instructor Su:"), ("你好！", "Hello!"),
    ("我们班的马大卫是个很好的学生，以前每次单元考试，阅读和听力他都考得很好。", "Ma Dawei in our class is a very good student; on every unit test before, he did very well on reading and listening."),
    ("可是前个月他每天晚上都要值班，学习的时间很少，所以这次单元考试，他的听力和阅读都没有以前考得好。", "But last month he had to be on duty every evening and had very little time to study, so on this unit test his listening and reading were not as good as before."),
    ("现在怎么做好呢？他想这样：除了星期一到星期五努力学习以外，他还想每个星期六和星期天都学习四个小时的中文。", "What is the best thing to do now? He wants to do this: besides studying hard from Monday to Friday, he also wants to study Chinese for four hours every Saturday and Sunday."),
    ("你以前是学生的时候学习就非常好，你看马大卫在周末学习什么，怎么学好呢？", "When you were a student, you studied extremely well. What do you think Ma Dawei should study on weekends, and how can he do it well?"),
    ("谢谢！", "Thank you!"), ("王红", "Wang Hong"),
]
SURVEY = [("设计", "she4 ji4", "design"), ("了解", "liao3 jie3", "to know, to understand")]
L6 = lesson(
    "Presentation 2: class schedules, an email for help and a survey",
    "听力课 · 阅读课 · 苏教官 · 马大卫 · 设计 · 了解",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1: a two-day intensive course",
             "You are a Chinese instructor at UCLA. A college in Singapore asks you and a Chinese colleague to design a teaching schedule for a two-day intensive Chinese course. A. Review the possible classes below, decide which ones would fit the program and the duration of each, and complete a table in Chinese (Day 1 and Day 2: duration and class). B. On the phone with a colleague (your partner), ask for their class arrangement in Chinese, then work together to finalize the two-day schedule and share it with the class in Chinese.",
             tables=[wtable(rows_py(CLASSES), headers=("Class", "Pinyin", "Meaning"))]),
        card("Activity 2 (Reading, Writing and Speaking): an email from 王老师",
             "You are now an MLI (military language instructor) in the Chinese school and have just received an email from Wang Laoshi asking for your help. A. Read the email, then write in Chinese in a table how you think Ma Dawei should spend the eight hours mentioned in the message (Saturday and Sunday: duration and action); consult a dictionary if necessary. B. In Chinese, share your suggestions with a partner and devise a final plan; then write a short Chinese email to Wang Laoshi presenting your ideas.",
             examples=[D(z, e) for z, e in MAIL]),
        card("Activity 3 (Listening, Writing and Speaking): a survey",
             "You are studying at Nanjing University while working part-time at the International Students Office. The director, Wang Zhong, asks you to design a survey of international students. A. Listen to Mr. Wang’s message (audio, not included), then write the five questions that go on the questionnaire, and devise the answer choices on a scale of 1 to 5, from very poor to very good, or from not enough to too many. "
             "B. Pilot the questionnaire: in Chinese, ask a partner the questions, record the answers, then switch roles. C. Work together to write Mr. Wang an email in Chinese briefing him on the results.",
             tables=[wtable(SURVEY)]),
    ],
    exercises=[
        M("What does Wang Laoshi say about Ma Dawei before last month?", "He was a very good student and did well on reading and listening on every unit test", ["He was a poor student", "He never took tests", "He was a teacher"], "以前每次单元考试，阅读和听力他都考得很好。"),
        M("Why did Ma Dawei’s test results drop?", "He was on duty every evening last month and had little time to study", ["He was sick", "He had no homework", "He moved to a new school"], "前个月他每天晚上都要值班，学习的时间很少。"),
        M("What does Ma Dawei want to do?", "Study four hours on Saturday and four on Sunday, besides studying Monday to Friday", ["Stop studying on weekends", "Study only on Friday", "Take a vacation"], "他还想每个星期六和星期天都学习四个小时的中文。"),
        M("How many weekend hours does that make in total?", "Eight", ["Four", "Twelve", "Two"], "Four hours on each of Saturday and Sunday: eight."),
        M("Who sent the email?", "王红 (Wang Hong), to Instructor 苏", ["苏教官, to 王红", "马大卫, to 王红", "大卫, to 琳达"], "The signature is 王红 and it is addressed to 苏教官."),
        M("Which class is 翻译课?", "Translation class", ["Debate class", "Writing class", "Self-study class"], "翻译 fānyì: translation."),
        M("Which class is 辩论课?", "Debate class", ["Translation class", "Listening class", "Self-study class"], "辩论 biànlùn: debate."),
        M("Which class is 自习课?", "Self-study class", ["Speaking class", "Debate class", "Writing class"], "自习 zìxí: study on your own."),
        M("What does 设计 mean?", "design", ["to know", "to test", "to start"], "设计 shèjì: design."),
        M("What does 了解 mean?", "to know, to understand", ["design", "congratulate", "adapt"], "了解 liǎojiě."),
        mean("设计", "she4 ji4", "design", ["to know", "to start", "to test"]),
        mean("了解", "liao3 jie3", "to know, to understand", ["design", "congratulate", "to test"]),
        mean("听力课", "ting1 li4 ke4", "listening class", ["reading class", "grammar class", "speaking class"]),
        mean("语法课", "yu3 fa3 ke4", "grammar class", ["listening class", "reading class", "speaking class"]),
    ],
)

# ------------------------------------------------------------------ 7. vocabulary
L7 = vocab_lesson("Presentation 2 vocabulary (26 words)", "一定 · 不错 · 努力 · 单元 · 听力 · 完全 · 小时 · 开始 · 考试 · 语法 · 阅读 · 除了",
                  "Vocabulary list (Presentation 2)",
                  "The book’s 26 words, with the traditional form where it differs. The book prints 得 as dé for the structural particle; it is read de (neutral tone) in 考得不错.", VOC2)

UNIT = unit("第七课 校园生活 Presentation 2: school life in Taiwan, 怎么样, 除了 and 得", [L1, L2, L3, L4, L5, L6, L7])
