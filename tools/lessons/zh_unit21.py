"""Unit 21: Lesson 7 (School Life) Presentation 3, from the book's texts: the weekend passage, 先…然后…, 有时…有时…,
the complement of degree (2), the skill-integration and in-context activities with the emails, the Area Studies reading
"Daily Routine in China" and the vocabulary list. Audio and pictures are not included; the lessons say so."""
from zh_auto import *
from zh_l7_vocab import VOC3

PART = ["吗", "们", "呢"]

# ------------------------------------------------------------------ 1. the weekend passage
P3 = [
    ("我很喜欢周末，因为周末不上课，可以做很多自己喜欢的事情。", "I like weekends very much, because there is no class on weekends and I can do many things I like."),
    ("星期六早上，我十点起床。", "On Saturday morning I get up at ten."),
    ("起床以后，我先去体育馆锻炼，然后，请几个朋友来宿舍聊天。", "After getting up, I first go to the gym to work out, and then invite a few friends to come chat in the dormitory."),
    ("中午，我们常常一起去中国饭馆吃饭。", "At noon, we often go to a Chinese restaurant to eat together."),
    ("午饭以后，我有时和女朋友去看电影，有时和同学们去海边散步。", "After lunch, sometimes I go to see a movie with my girlfriend, and sometimes I go for a walk on the beach with classmates."),
    ("星期天早上和星期六早上差不多一样，不过，星期天下午，我要去图书馆做作业，然后，我还要预习新课。", "Sunday morning is about the same as Saturday morning, but on Sunday afternoon I go to the library to do homework, and then I also have to preview the new lesson."),
    ("因为星期一要很早起床，所以我星期天晚上常常十点睡觉。", "Because I have to get up very early on Monday, I often go to bed at ten on Sunday evenings."),
]
CLOZE_OPTS = [("1", ["一定", "可是", "因为"], "因为", "因为星期六不上课，所以我经常九点起床。"), ("2", ["的时候", "九点以后", "以后"], "以后", "起床以后，我先去操场锻炼身体，"),
              ("3", ["然后", "一起", "在蒙特雷"], "然后", "…，然后和我女朋友去看电影。"), ("4", ["去饭馆吃饭", "吃饭在饭馆", "喜欢去中国饭馆"], "去饭馆吃饭", "中午我会和我女朋友去饭馆吃饭。"),
              ("5", ["经常", "三点半", "有时"], "有时", "下午我有时去图书馆看书，有时在宿舍和同学聊天。"), ("6", ["差不多不一样", "不太一样", "经常一样"], "不太一样", "星期天和星期六不太一样。"),
              ("7", ["散步在海边", "起床", "还去操场锻炼身体"], "起床", "星期天我八点半起床。"), ("8", ["一起去锻炼", "去海边和女朋友", "去图书馆做作业"], "去图书馆做作业", "下午我会去图书馆做作业。")]
EXPR = [("在…和…一起…", "do something at a certain time with someone"), ("先…，然后…", "do A first, then do B"), ("有时…，有时…", "sometimes do A, sometimes do B"), ("常常去…", "often go somewhere to do something"),
        ("差不多一样", "A and B are almost the same"), ("因为…", "because …")]
CLOZE_TEXT = "1. ____星期六不上课，所以我经常九点起床。起床 2. ____，我先去操场锻炼身体，3. ____和我女朋友去看电影。中午我会和我女朋友 4. ____。下午我 5. ____去图书馆看书，有时在宿舍和同学聊天。星期天和星期六 6. ____。星期天我八点半 7. ____。上午我会给爸爸妈妈打电话，下午我会 8. ____。"
L1 = lesson(
    "Presentation 3: the weekend (passage)",
    "我很喜欢周末 · 先去体育馆锻炼，然后… · 有时…有时…",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss with your partner (the book has three photos of weekend activities): A. Which of the activities pictured do you do on the weekends? B. What outdoor activities do you most like to do? C. Do you study Chinese on weekends? If so, when?"),
        card("Presentation 3: my weekend", "The book also prints the passage in traditional characters.", examples=[D(z, e) for z, e in P3]),
        card("Activity 1 (Listening)",
             "A. Global listening: What is this passage mainly about? What kind of activities does the speaker do more of? B. Detailed listening: list the indoor and outdoor activities in two tables in English and compare your lists in pairs (audio, not included; the questions are practiced below from the text)."),
        card("Activity 2 (Writing): the expressions you have just learned",
             "In pairs, complete a table of expressions for six hints. The expressions in this passage:",
             tables=[wtable(rows_py(EXPR), headers=("Expression", "Pinyin", "Hint"))]),
        card("Activity 3 (Reading): choose the expressions to complete the sentences",
             "Choose the appropriate expression from each list (a, b or c) to fill the numbered blanks, then check your work in pairs and explain your choices. The book gives no key; the key here is my reading of the text (the correct choice is c for 1, 2 and 5, a for 3 and 4, b for 6 and 7, and c for 8). The text with blanks: " + CLOZE_TEXT,
             examples=[D(c[3], "Completed sentence " + c[0] + ".") for c in CLOZE_OPTS]),
        card("Activity 4 (Listening, Speaking and Reading)",
             "Listen to a dialog and complete a table in English about what Dashan does during each time slot on Saturday and Sunday (morning, afternoon, evening). Then ask your partner in Chinese when Dashan does a certain activity, and read the script to correct any mistakes (audio, not included). New word: 打电话 dǎ diànhuà, to make a phone call.",
             tables=[wtable([("打电话", "da3 dian4 hua4", "make a phone call")])]),
    ],
    exercises=[
        M("What is the passage mainly about?", "How the writer spends the weekend", ["How the writer spends the week", "A trip to San Francisco", "Preparing for exams"], "It describes Saturday and Sunday."),
        M("Why does the writer like weekends?", "There is no class, so he can do many things he likes", ["He sleeps all day", "He has more homework", "He is on duty"], "因为周末不上课，可以做很多自己喜欢的事情。"),
        M("What time does the writer get up on Saturday?", "Ten", ["Eight", "Nine", "Seven"], "星期六早上，我十点起床。"),
        M("What does he do after getting up on Saturday?", "Works out at the gym, then invites friends to the dormitory to chat", ["Goes to the library", "Eats at a restaurant", "Takes a class"], "先去体育馆锻炼，然后，请几个朋友来宿舍聊天。"),
        M("What do they often do at noon?", "Go to a Chinese restaurant together", ["Go to the beach", "See a movie", "Study"], "中午，我们常常一起去中国饭馆吃饭。"),
        M("What does he do on Saturday afternoon?", "Sometimes sees a movie with his girlfriend, sometimes walks on the beach with classmates", ["Always goes to the library", "Always sleeps", "Always works out"], "有时和女朋友去看电影，有时和同学们去海边散步。"),
        M("How is Sunday morning compared with Saturday morning?", "About the same", ["Totally different", "Much earlier", "Much later"], "星期天早上和星期六早上差不多一样。"),
        M("What does he do on Sunday afternoon?", "Goes to the library to do homework, then previews the new lesson", ["Goes to the beach", "Sees a movie", "Is on duty"], "我要去图书馆做作业，然后，我还要预习新课。"),
        M("Why does he go to bed at ten on Sunday evenings?", "Because he has to get up very early on Monday", ["Because he is on duty", "Because he has a test", "Because he has no homework"], "因为星期一要很早起床。"),
        M("Which of these is an outdoor activity in the passage?", "Walking on the beach", ["Chatting in the dormitory", "Doing homework at the library", "Previewing a lesson"], "去海边散步 is outdoors."),
        M("Which of these is an indoor activity in the passage?", "Chatting in the dormitory", ["Walking on the beach", "A walk by the sea", "Going to the beach"], "请几个朋友来宿舍聊天 is indoors."),
    ] + [
        M(f"Activity 3, blank {c[0]}: which expression fits? (…{CLOZE_TEXT.split(c[0] + '. ____')[0][-10:]}____{CLOZE_TEXT.split(c[0] + '. ____')[1][:10]}…)", c[2], [o for o in c[1] if o != c[2]], c[3]) for c in CLOZE_OPTS],
)

# ------------------------------------------------------------------ 2. 先…然后…
XR = [("我先做作业，然后预习课文。", "I do homework first, and then preview the text."), ("我们先锻炼身体，然后去上课。", "We exercise first, and then go to class."), ("她先去北京，然后去上海。", "She goes to Beijing first, and then to Shanghai."),
      ("空军先集合，然后海军集合。", "The Air Force has formation first, and then the Navy does."), ("小张先来了美国，然后她弟弟也来了美国。", "Xiao Zhang came to America first, and then her younger brother came to America too.")]
SUN = [("下个星期天我先去图书馆做作业，然后去中国饭馆吃饭。", "Next Sunday I will first go to the library to do homework, and then go to a Chinese restaurant to eat. (a model plan; the book leaves this blank)")]
L2 = lesson(
    "Presentation 3 grammar: the 先…，然后… construction",
    "我先做作业，然后预习课文 · 她先去北京，然后去上海",
    requires=[],
    cards=[
        card("先…，然后…: first … then …",
             "The 先…，然后… construction shows actions in sequence. Same subject: Subject + 先 + Verb Phrase，然后 + Verb Phrase. Different subjects: Subject A + 先 + Verb Phrase，然后 + Subject B + Verb Phrase.",
             examples=[D(z, e) for z, e in XR]),
        card("Activity 1 and Activity 2",
             "Activity 1: A. Listen to a dialog and put in order the events shown in four pictures. B. In pairs, use 先…，然后… to write three sentences describing the sequence of events in the dialog, then read the script and check your work (audio and pictures, not included). "
             "Activity 2: A. Use 先…，然后… to write your plan for next Sunday (your plan and your partner’s plan). B. Tell your partner in Chinese what your plan for next Sunday is; listen to your partner’s plan, take notes, then present their plan to the class in Chinese. A model:",
             examples=[D(z, e) for z, e in SUN]),
    ],
    exercises=[
        M("What does 先…，然后… mean?", "first … then …", ["both … and …", "sometimes … sometimes …", "neither … nor …"], "先 = first; 然后 = then."),
        M("What does 我先做作业，然后预习课文 mean?", "I do homework first, then preview the text", ["I preview the text first, then do homework", "I do both at once", "I never do homework"], "先 comes first."),
        M("What does 她先去北京，然后去上海 mean?", "She goes to Beijing first, then to Shanghai", ["She goes to Shanghai first", "She goes to Beijing and Shanghai at the same time", "She doesn’t go anywhere"], "先去北京，然后去上海."),
        M("Which sentence has two different subjects?", "空军先集合，然后海军集合。", ["我们先锻炼身体，然后去上课。", "我先做作业，然后预习课文。", "她先去北京，然后去上海。"], "Different subjects: 空军 … 海军."),
        M("What does 小张先来了美国，然后她弟弟也来了美国 mean?", "Xiao Zhang came to America first, then her younger brother came too", ["Her brother came first", "They came together", "Neither came"], "先…然后: sequence, with two subjects."),
        M("Which is correct for “We exercise first and then go to class”?", "我们先锻炼身体，然后去上课。", ["我们锻炼先身体，去上课然后。", "我们然后锻炼身体，先去上课。", "先然后我们锻炼身体去上课。"], "Subject + 先 + VP，然后 + VP."),
        F("我先做作业，___预习课文。", "然后", PART, "然后 means “and then”."),
        F("我们___锻炼身体，然后去上课。", "先", PART, "先 means “first”."),
        F("空军先集合，然后___集合。", "海军", ["作业", "操场", "预习"], "Different subjects: the Navy has formation after the Air Force."),
        mean("先", "xian1", "first", ["then", "often", "already"]),
        mean("然后", "ran2 hou4", "and then, after that", ["first", "often", "sometimes"]),
    ],
)

# ------------------------------------------------------------------ 3. 有时…有时…
YS = [("雨有时大有时小。", "Sometimes the rain is heavy, sometimes it is light."), ("我有时去有时不去。", "Sometimes I go, sometimes I don’t."), ("我们有时去中国饭馆吃饭，有时去日本饭馆吃饭。", "Sometimes we eat at a Chinese restaurant, sometimes at a Japanese restaurant."),
      ("他有时星期六来看我，有时星期天来看我。", "Sometimes he comes to see me on Saturday, sometimes on Sunday."), ("有时我去看他，有时他来看我。", "Sometimes I go to see him, sometimes he comes to see me."),
      ("有时张老师给我们上听力课，有时王老师给我们上听力课。", "Sometimes Teacher Zhang teaches us listening, sometimes Teacher Wang does.")]
YS_BOOK = [("她有时在美国过春节，有时在中国过春节。", "Sometimes she celebrates the Chinese New Year in America, sometimes in China."), ("他有时读课文，有时预习生词。", "Sometimes he reads the text, sometimes he previews new words.")]
YS_SAY = [("星期六我有时七点半起床，有时八点起床。", "On Saturday, I sometimes get up at 7:30, and sometimes at 8:00."), ("晚上我有时做阅读作业，有时做听力作业。", "In the evening, I sometimes do reading homework, and sometimes listening homework."),
          ("有时我值班，有时我们班长值班。", "Sometimes I am on duty, and sometimes our class leader is."), ("夏天我老家有时雨下得很大，有时雨下得很小。", "In summer in my hometown, sometimes it rains very hard, and sometimes very lightly."),
          ("他有时去哥哥家过春节，有时哥哥来他家过春节。", "Sometimes he goes to his older brother’s house for the Chinese New Year, sometimes his older brother comes to his house.")]
L3 = lesson(
    "Presentation 3 grammar: the 有时…，有时… construction",
    "雨有时大有时小 · 我有时去有时不去 · 有时我去看他，有时他来看我",
    requires=[],
    cards=[
        card("有时…，有时…: sometimes … sometimes …",
             "The 有时…，有时… construction shows that sometimes one action or state occurs, while sometimes another occurs. Connecting phrases: Subject + 有时…，有时…. Connecting sentences: 有时 + Subject A …，有时 + Subject B …. The book’s opening examples are below, followed by its six examples.",
             examples=[D(z, e) for z, e in YS_BOOK] + [D(z, e) for z, e in YS]),
        card("Activity 3 (Speaking)",
             "Tell your partner how you would say five sentences in Chinese: 1. On Saturday, you sometimes get up at 7:30 and sometimes at 8:00. 2. In the evening, you sometimes do reading homework and sometimes listening homework. 3. Sometimes you go on duty, and sometimes your class leader goes on duty. 4. During the summer in your hometown, sometimes it rains very hard and sometimes very lightly. 5. Sometimes he goes to his older brother’s house to celebrate the Chinese New Year, and sometimes his older brother comes to his house. The book gives these in English; one way to say each:",
             examples=[D(z, e) for z, e in YS_SAY]),
        card("Activity 4 (Speaking)",
             "A. In Chinese, interview two classmates about their activities last Saturday (remind them to use 有时…，有时… as much as possible) and take notes in a table (Saturday morning, afternoon and evening for Student A and Student B). B. In Chinese, share your information with a partner; then choose one of your partner’s interviewees and report their activities to the class in Chinese."),
    ],
    exercises=[
        M("What does 有时…，有时… mean?", "sometimes … sometimes …", ["first … then …", "both … and …", "because … so …"], "有时 = sometimes."),
        M("What does 雨有时大有时小 mean?", "Sometimes the rain is heavy, sometimes it is light", ["The rain is heavy, then light", "It rains and it is big", "It rains a lot"], "有时大有时小."),
        M("What does 我有时去有时不去 mean?", "Sometimes I go, sometimes I don’t", ["I go, then I don’t go", "I never go", "I always go"], "有时去有时不去."),
        M("What does 有时我去看他，有时他来看我 mean?", "Sometimes I go to see him, sometimes he comes to see me", ["I go to see him and he comes to see me", "He never comes", "I see him every day"], "Two subjects: 我 and 他."),
        M("Which sentence connects two sentences (different subjects)?", "有时张老师给我们上听力课，有时王老师给我们上听力课。", ["雨有时大有时小。", "我有时去有时不去。", "他有时读课文，有时预习生词。"], "有时 + Subject A …，有时 + Subject B …."),
        M("Which sentence connects two phrases (same subject)?", "我们有时去中国饭馆吃饭，有时去日本饭馆吃饭。", ["有时我去看他，有时他来看我。", "有时张老师上课，有时王老师上课。", "有时下雨，有时下雪天。"], "Subject + 有时…，有时…."),
        F("她___在美国过春节，有时在中国过春节。", "有时", PART, "有时…，有时…."),
        F("雨有时大有时___。", "小", PART, "大 and 小 are opposites."),
        F("他有时星期六来看我，有时星期天___看我。", "来", PART, "来看我: comes to see me."),
        F("我们有时去中国饭馆吃饭，有时去日本饭馆___。", "吃饭", ["作业", "操场", "预习"], "去饭馆吃饭: go to a restaurant to eat."),
        mean("有时", "you3 shi2", "sometimes", ["often", "always", "never"]),
    ],
)

# ------------------------------------------------------------------ 4. complement of degree (2)
CD2 = [
    ("她做作业做得比我做得好。", "She does homework better than I do."), ("她做作业做得比我好。", "She does homework better than I do."), ("她做作业比我做得好。", "She does homework better than I do."),
    ("他说中文说得比我说得好很多。", "He speaks Chinese much better than I do."), ("他说中文说得比我好很多。", "He speaks Chinese much better than I do."), ("他说中文比我说得好很多。", "He speaks Chinese much better than I do."),
    ("她起床起得比我起得早得多。", "She gets up much earlier than I do."), ("她起床起得比我早得多。", "She gets up much earlier than I do."), ("她起床比我起得早得多。", "She gets up much earlier than I do."),
    ("我看电影看得比她看得多多了。", "I watch many more movies than she does."), ("我看电影看得比她多多了。", "I watch many more movies than she does."), ("我看电影比她看得多多了。", "I watch many more movies than she does."),
]
CD2_NEG = [
    ("我做作业做得没有她做得那么好。", "I don’t do homework as well as she does."), ("我做作业做得没有她那么好。", "I don’t do homework as well as she does."), ("我做作业没有她做得那么好。", "I don’t do homework as well as she does."),
    ("我说英语说得没有他说得那么好。", "I don’t speak English as well as he does."), ("我说英语说得没有他那么好。", "I don’t speak English as well as he does."), ("我说英语没有他说得那么好。", "I don’t speak English as well as he does."),
    ("她做作业做得有没有我做得那么好？", "Does she do homework as well as I do?"), ("她做作业做得有没有我那么好？", "Does she do homework as well as I do?"), ("她做作业有没有我做得那么好？", "Does she do homework as well as I do?"),
    ("我起床起得有没有你起得那么早？", "Do I get up as early as you do?"), ("我起床起得有没有你那么早？", "Do I get up as early as you do?"), ("我起床有没有你起得那么早？", "Do I get up as early as you do?"),
]
A5 = [("大卫写中文字写得比琳达好多了。", "David writes Chinese characters much better than Linda does."), ("琳达读中文读得比大卫好得多。", "Linda reads Chinese much better than David does."),
      ("大卫做作业做得没有琳达那么好。", "David doesn’t do homework as well as Linda does."), ("琳达说中文说得有没有大卫那么好？", "Does Linda speak Chinese as well as David does?")]
L4 = lesson(
    "Presentation 3 grammar: the complement of degree (2), comparisons",
    "做得比我好 · 好得多 · 多多了 · 没有她那么好 · 有没有我那么好？",
    requires=[],
    cards=[
        card("Comparing with 比",
             "Complement of Degree constructions are used to make comparisons. The full pattern is A + Verb1-Object + Verb1 得 + 比 B + Verb1 得 + Complement. It can be simplified by skipping one “Verb 得”: A + Verb1-Object + Verb1 得 + 比 B + Complement, or A + Verb1-Object + 比 B + Verb1 得 + Complement. "
             "Complement + 很多 / 得多 / 多了 means “much more …”. The book’s examples, each in its three forms:",
             examples=[D(z, e) for z, e in CD2]),
        card("Negative and affirmative-negative questions with 没有 and 有没有",
             "To negate, use 没有 instead of 不: A + Verb1-Obj. + Verb1 得 + 没有 B + Verb1 得 + (那么) Complement; this can also be simplified by skipping one “Verb1 得”. Affirmative-negative questions use 有没有: A + Verb1-Obj. + Verb1 得 + 有没有 B (+ Verb1 得) + (那么) Complement? 那么 is often inserted before the complement.",
             examples=[D(z, e) for z, e in CD2_NEG]),
        card("Activity 5 (Reading, Writing and Speaking)",
             "A. Write sentences using the expressions provided. The book’s example: 我哥哥，我，说日文，好 → 我哥哥说日文说得比我说得好。 or 我哥哥说日文说得比我好 / 我哥哥说日文比我说得好。 The four items are: 1. 大卫，琳达，写中文字，好，多了; 2. 琳达，大卫，读中文，好得多; 3. 大卫，琳达，做作业，没有，好，那么; 4. 琳达，大卫，说中文，那么，有没有，好. B. Read your sentences to a partner. The book gives no key; model sentences:",
             examples=[D("我哥哥说日文说得比我说得好。", "My older brother speaks Japanese better than I do.")] + [D(z, e) for z, e in A5]),
    ],
    exercises=[
        M("What does 她做作业做得比我好 mean?", "She does homework better than I do", ["I do homework better than she does", "She does homework as well as I do", "She does not do homework"], "A + … + 比 B + complement."),
        M("What does 他说中文说得比我好很多 mean?", "He speaks Chinese much better than I do", ["I speak Chinese much better than he does", "He speaks Chinese a little", "We speak equally well"], "好很多: much better."),
        M("What does 她起床起得比我早得多 mean?", "She gets up much earlier than I do", ["I get up much earlier than she does", "She gets up a bit later", "She doesn’t get up"], "早得多: much earlier."),
        M("What does 我看电影看得比她多多了 mean?", "I watch many more movies than she does", ["She watches many more than I do", "I watch as many as she does", "I never watch movies"], "多多了: much more."),
        M("What does 我做作业做得没有她那么好 mean?", "I don’t do homework as well as she does", ["I do homework better than she does", "She doesn’t do homework", "We do it equally well"], "没有 + B + 那么 + adjective: “not as … as”."),
        M("What does 她做作业做得有没有我那么好？ ask?", "Does she do homework as well as I do?", ["Does she have homework?", "Do I have homework?", "Who does homework?"], "有没有 forms the affirmative-negative question."),
        M("Which three phrases can follow the complement to mean “much more”?", "很多, 得多, 多了", ["一点, 一些, 差不多", "很少, 不多, 太多", "有时, 常常, 经常"], "Complement + 很多 / 得多 / 多了."),
        M("Which word replaces 不 in the negative comparison?", "没有", ["有没有", "比", "更"], "To negate, use 没有 instead of 不."),
        M("Which word is often inserted before the complement after 没有 or 有没有?", "那么", ["因为", "然后", "有时"], "那么 is often inserted before the complement."),
        F("她做作业做得___我做得好。", "比", PART, "比 compares A and B."),
        F("我做作业做得___有她那么好。", "没", PART, "没有: “not as … as”."),
        F("她做作业做得___没有我那么好？", "有", PART, "有没有: affirmative-negative question."),
        F("我看电影看得比她多___了。", "多", PART, "多多了: much more."),
        F("他说中文说得比我好很___。", "多", PART, "好很多: much better."),
        mean("比", "bi3", "compared with, than", ["because", "first", "sometimes"]),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
SAY7 = [
    ("你现在已经完全习惯在国防语言学院的学生生活了。", "You are now completely accustomed to student life at DLI.", None),
    ("这个星期五没有作业，所以你可以做自己喜欢的事情。", "As you don’t have homework this Friday, you can do something you enjoy.", None),
    ("星期六早上起床以后，你常常去体育馆锻炼，然后去海边散步。", "After you get up Saturday mornings, you often go to the gym to work out, and then take a walk on the beach.", None),
    ("星期六下午，你有时在宿舍和同学聊天，有时和朋友去看电影。", "Saturday afternoons, sometimes you chat with classmates in the dormitory, sometimes you go see a movie with friends.", None),
    ("星期天早上，你先去图书馆做作业，然后和朋友去中国饭馆吃饭。", "Sunday mornings, you first do your homework at the library, then you go eat at a Chinese restaurant with friends.", None),
    ("星期天下午，你常常在宿舍和同学一起学习生词。", "Sunday afternoons, you often stay in the dormitory studying vocabulary with a classmate.", None),
    ("因为星期一早上要很早起床，所以星期天晚上九点以前你要预习新课。", "Because Monday mornings you have to get up early, you need to preview the new presentation before 9 p.m. Sunday evening.", None),
]
L5 = lesson(
    "Presentation 3 skill integration: weekend plans and hobbies",
    "你现在已经完全习惯… · 星期六早上起床以后 · 你的爱好是什么？",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Reading and Speaking)",
             "A. Listen to the passage and mark five statements true or false: 1. The speaker talks about how he spent last weekend. 2. His girlfriend likes Chinese food, so most weekends they eat Chinese. 3. He and his girlfriend often go to the library on Saturday. 4. His normal sequence is: workout, chat with classmates, eat take-out, walk on the beach and then read at the library. 5. Some Saturdays he has duties after dinner, so he gets to bed late. "
             "B. Read the script your teacher provides and check your work; ask a partner three questions about the passage. C. Pair up: while your partner looks away from the script, orally translate one of the underlined sentences so your partner can translate it back into Chinese; review the script. (The recording is not included; the five statements are checked against the Presentation 3 passage below.)"),
        card("Activity 2 (Speaking and Writing): say it in Chinese",
             "A. Tell your partner how you would say seven sentences in Chinese (the book gives them in English). B. Work with a partner to write a dialog based on part A, then perform it for the class. One way to say each sentence:",
             examples=[D(z, e, fixes=f) for z, e, f in SAY7]),
        card("Activity 3 (Speaking and Writing): hobbies",
             "In Chinese, interview three classmates to find out what their hobbies are and when they usually do them, and write your notes in Chinese in a table (name, hobby, when); consult a dictionary if necessary. B. Pair up. Each student thinks of one classmate and one of their hobbies; your partner asks questions in Chinese to find out who you were thinking of and their hobby. C. When both partners have asked and answered the questions, repeat step B with a different partner."),
    ],
    exercises=[
        M("True or false: the speaker talks about how he spent last weekend.", "False: he describes what he usually does on weekends", ["True: he describes only last weekend", "True: he was on duty", "False: he talks about the week"], "The passage says 常常 and 有时 — usual habits."),
        M("True or false: his girlfriend likes Chinese food, so most weekends they eat Chinese.", "Not stated: the passage says they often go to a Chinese restaurant at noon, not why", ["True: because she likes Chinese food", "False: they never go", "True: because it is cheap"], "中午，我们常常一起去中国饭馆吃饭。 The passage does not give a reason."),
        M("True or false: he and his girlfriend often go to the library on Saturday.", "False: on Saturday they sometimes see a movie; the library is on Sunday afternoon", ["True", "False: they never go out", "True: every Saturday morning"], "星期天下午，我要去图书馆做作业。"),
        M("True or false: his normal Saturday sequence is workout, chat, eat, walk on the beach, library.", "False: the library is on Sunday, and Saturday afternoon is a movie or the beach", ["True", "False: he sleeps all day", "True: but the library is first"], "星期六: gym, chat, noon at a restaurant, afternoon movie or beach."),
        M("True or false: some Saturdays he has duties after dinner, so he gets to bed late.", "Not in this passage: he goes to bed at ten on Sunday evenings", ["True: he is on duty every Saturday", "False: he never goes to bed", "True: he goes to bed at midnight"], "因为星期一要很早起床，所以我星期天晚上常常十点睡觉。"),
        M("How do you say “After getting up on Saturday morning, I often go to the gym”?", "星期六早上起床以后，我常常去体育馆锻炼。", ["星期六早上以后起床，我常常去体育馆锻炼。", "我常常去体育馆锻炼星期六早上起床。", "起床星期六早上以后，我去常常体育馆。"], "Time + 起床以后 + 常常 + verb."),
        M("How do you say “Sometimes I chat with classmates, sometimes I see a movie”?", "有时我和同学聊天，有时我去看电影。", ["有时我和同学聊天，然后我去看电影。", "我先和同学聊天，有时去看电影。", "有时有时我聊天看电影。"], "有时…，有时…."),
        M("How do you say “First do homework at the library, then eat at a restaurant”?", "先去图书馆做作业，然后去饭馆吃饭", ["去图书馆做作业，先然后去饭馆吃饭", "然后去图书馆做作业，先去饭馆吃饭", "先然后做作业去图书馆"], "先 … 然后 …"),
        F("因为星期一要很早起床，___我星期天晚上常常十点睡觉。", "所以", PART, "因为…，所以…."),
        F("星期天和星期六差不多___。", "一样", ["作业", "操场", "预习"], "差不多一样: almost the same."),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese in context
CLUB = [
    ("各位同学：", "Dear fellow students:"), ("你们好！", "Hello!"),
    ("长周末快要到了，我们怎么过一个有意思的周末呢？请各位同学告诉我们您想怎么过，好吗？", "The long weekend is coming soon; how can we spend an interesting weekend? Please tell us how you would like to spend it, okay?"),
    ("比如，星期六、星期天这两天，您想做什么事，什么时间做。", "For example, on these two days, Saturday and Sunday: what you would like to do, and at what time."),
    ("下面是一个表格，请填一下。我们会根据你们的意见，组织一些有意思的活动。", "Below is a form; please fill it in. Based on your opinions, we will organize some interesting activities."),
    ("谢谢！", "Thank you!"), ("研究生俱乐部", "The Graduate Student Club"),
]
ZL = [
    ("大卫老师：", "Teacher David:"), ("您好！", "Hello!"),
    ("您还记得我吗？去年夏天，您在我们这儿的英文班教课的时候，我是您的学生。我们都喜欢上您的课。", "Do you still remember me? Last summer, when you taught in the English class here, I was your student. We all liked your classes.", {"教": "jiao1"}),
    ("我想明年去美国上大学。美国的好大学一定有很多，您能不能给我介绍一所呢？", "I want to go to college in America next year. There must be many good universities in America; could you recommend one to me?"),
    ("请告诉我学校的情况，另外，我也最想知道那儿的学生周末会做什么。", "Please tell me about the school; also, I most want to know what the students there do on weekends."),
    ("谢谢您！", "Thank you!"), ("张琳", "Zhang Lin"),
]
L6 = lesson(
    "Presentation 3: plans for a long weekend, and an email to a teacher",
    "长周末 · 研究生俱乐部 · 张琳 · 大卫老师 · 打电话",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Listening, Speaking and Reading)",
             "Work in pairs. You are studying at Guangzhou University. On Friday, one of your WeChat groups posts two audios about plans for Saturday (three pictures). A. Listen to Audio 1 while your partner listens to Audio 2; write your notes in English in a table (time, location, activity). B. Ask your partner questions to complete the table. C. Go over the scripts and correct them, then discuss in Chinese which plan works best for both of you, and explain your decision to the class in Chinese (audio, not included)."),
        card("Activity 2 (Reading, Writing and Speaking): an email from the Graduate Student Club",
             "You are in Beijing for graduate studies and your Graduate Student Club has sent an email asking for suggestions on how to spend the coming long weekend. A. Read the email below (use a dictionary if necessary), then complete the tables in Chinese: Saturday and Sunday, four items each. B. Share your suggestions in pairs and modify them from your partner’s feedback. C. Speak in Chinese with another classmate who is secretary of the Graduate Student Club: give them your suggestions and answer their questions.",
             examples=[D(z, e) for z, e in CLUB]),
        card("Activity 3 (Reading, Writing and Speaking): Zhang Lin’s email",
             "A. Read the following email and consult a dictionary when necessary; then reply to your former English student to answer her questions. B. Pair up. Read your email reply to your partner and answer any questions your partner may have.",
             examples=[D(z[0], z[1], fixes=(z[2] if len(z) > 2 else None)) for z in ZL]),
    ],
    exercises=[
        M("Who sent the first email, and to whom?", "The Graduate Student Club, to all students", ["A teacher, to one student", "A student, to a teacher", "A company, to a client"], "The email begins 各位同学 and is signed 研究生俱乐部."),
        M("What is the club asking for?", "Suggestions on how to spend the coming long weekend", ["Money for a trip", "Homework", "A class schedule"], "请各位同学告诉我们您想怎么过。"),
        M("What does the club want to know for Saturday and Sunday?", "What you want to do, and at what time", ["Who your teacher is", "Where you were born", "How old you are"], "星期六、星期天这两天，您想做什么事，什么时间做。"),
        M("What will the club do with the answers?", "Organize some interesting activities based on the students’ opinions", ["Print them in a newspaper", "Cancel the weekend", "Give grades"], "我们会根据你们的意见，组织一些有意思的活动。"),
        M("Who writes the second email?", "张琳, a former student of 大卫老师", ["大卫老师, to 张琳", "琳达, to 大卫", "王红, to 苏教官"], "The signature is 张琳."),
        M("When was Zhang Lin David’s student?", "Last summer, in the English class", ["Last winter", "Next year", "Ten years ago"], "去年夏天，您在我们这儿的英文班教课的时候，我是您的学生。"),
        M("What does Zhang Lin want to do next year?", "Go to college in America", ["Teach English", "Join the military", "Move to Hangzhou"], "我想明年去美国上大学。"),
        M("What does she ask David?", "To recommend one university and tell her what students there do on weekends", ["To recommend a restaurant", "To lend her money", "To write a letter for her"], "给我介绍一所…；那儿的学生周末会做什么。"),
        mean("周末", "zhou1 mo4", "weekend", ["week", "holiday", "midnight"]),
        mean("记得", "ji4 de5", "remember", ["forget", "believe", "start"]),
    ],
)

# ------------------------------------------------------------------ 7. Area Studies
AREA = [
    "China is a geographically diverse country with a vast population. Although most people still live in the countryside, it is in the cities where business, technology, education, and culture continue to advance and evolve. An overview of daily routines in the city will therefore lend insight into today’s China.",
    "Many Chinese begin their day exercising in local parks or city squares. While some do Western-style aerobics, traditional Chinese morning exercises are more common. Groups greet the sunrise with organized sessions of taijiquan, wushu and other traditional Chinese disciplines. People participate in these exercises right next to other groups that practice ballroom and modern dancing.",
    "After their workouts, they return home, bathe, have breakfast and prepare for the day. For city dwellers, at least, breakfast is not much different than in the West. Some even skip breakfast, snacking on the go as they head to school or work.",
    "Although many families own cars, most workers and students still rely on public transportation or bicycles. After school, some students may go home, play soccer, basketball or ping-pong, while others stay late on campus and study. High school students preparing for the national college entrance exams may use this time to take preparatory courses for the exams. Chinese urbanites can shop at giant department stores, small street markets, fashion boutiques, or traditional Chinese medicine shops. Friends meet in libraries, coffee shops, or internet cafes after work or class.",
    "As evenings settle in, families return home to prepare their dinners, or they go to restaurants for more formal dining with relatives, business partners or friends. Dinner is usually between 6 and 8 p.m. In China, many men learn to cook as a hobby—on special occasions it is not unusual for husbands to do the cooking.",
    "On evenings, weekends and holidays, people go to clubs, bars and internet cafes. Some go to see movies or plays, Chinese and Western operas, or soccer and basketball games. Chinese cities are large and densely populated, so there is guaranteed to be a big crowd at every event. None of this would be possible, however, without China’s excellent public transportation system. Subways will usually run until midnight, while buses and cabs operate throughout the night.",
    "Just like young Americans, young people in China often stay up late talking on their cell phones, watching movies or shows online, or playing video games. As China’s economy continues to grow, Chinese city life grows richer and more varied in its wake.",
]
L7 = lesson(
    "Area Studies: daily routine in China",
    "Daily Routine in China · taijiquan · public transportation · dinner between 6 and 8",
    requires=[],
    cards=[card("Daily Routine in China (1): the city and the morning", AREA[0] + "\n\n" + AREA[1] + "\n\n" + AREA[2]),
           card("Daily Routine in China (2): the day and the evening", AREA[3] + "\n\n" + AREA[4]),
           card("Daily Routine in China (3): nights, weekends and the young", AREA[5] + "\n\n" + AREA[6] + "\n\nReference: wikipedia.org. (The book’s photos, all from People.com.cn, are not included.)")],
    exercises=[
        M("According to the reading, where do most people in China still live?", "In the countryside", ["In large cities", "Near the coast only", "In the mountains only"], "Although most people still live in the countryside, the cities are where business, technology, education and culture advance."),
        M("How do many Chinese begin their day?", "Exercising in local parks or city squares", ["Eating a large breakfast", "Driving to work", "Studying"], "Many Chinese begin their day exercising."),
        M("Which kind of morning exercise is more common?", "Traditional Chinese exercises", ["Western-style aerobics", "Running marathons", "Swimming"], "Traditional Chinese morning exercises are more common."),
        M("Which traditional disciplines are named?", "Taijiquan and wushu", ["Judo and karate", "Yoga and pilates", "Boxing and wrestling"], "Groups greet the sunrise with taijiquan, wushu and other traditional disciplines."),
        M("Which groups practice next to the traditional exercise groups?", "Groups that practice ballroom and modern dancing", ["Soccer teams", "Singing groups", "Chess clubs"], "Right next to other groups that practice ballroom and modern dancing."),
        M("How is city breakfast compared with the West?", "Not much different; some even skip it", ["Very different and very large", "Always eaten at a restaurant", "Always rice"], "Breakfast is not much different than in the West."),
        M("How do most workers and students get around?", "By public transportation or bicycle", ["By car", "By plane", "On foot only"], "Most workers and students still rely on public transportation or bicycles."),
        M("What do high school students preparing for the college entrance exams may do after school?", "Take preparatory courses for the exams", ["Play ping-pong only", "Go home and sleep", "Work at a store"], "They may take preparatory courses for the exams."),
        M("Where do friends meet after work or class?", "Libraries, coffee shops or internet cafes", ["Only at home", "Only at restaurants", "Only at parks"], "Friends meet in libraries, coffee shops, or internet cafes."),
        M("When is dinner usually eaten?", "Between 6 and 8 p.m.", ["Between 3 and 5 p.m.", "After 10 p.m.", "At noon"], "Dinner is usually between 6 and 8 p.m."),
        M("What does the reading say about men and cooking?", "Many men learn to cook as a hobby, and husbands may do the cooking on special occasions", ["Men never cook", "Only restaurants cook", "Men cook only at the army"], "Many men learn to cook as a hobby."),
        M("Why are there big crowds at every event?", "Chinese cities are large and densely populated", ["Tickets are free", "Events are rare", "Cities are small"], "Chinese cities are large and densely populated."),
        M("Until when do subways usually run?", "Until midnight", ["Until 6 p.m.", "All night", "Until 3 a.m."], "Subways will usually run until midnight, while buses and cabs operate throughout the night."),
        M("What do buses and cabs do at night?", "Operate throughout the night", ["Stop at midnight", "Run only on weekends", "Do not run in cities"], "Buses and cabs operate throughout the night."),
        M("What do young people in China do, as the reading says, like young Americans?", "Stay up late on their phones, watching shows or playing video games", ["Go to bed at 8 p.m.", "Study all night", "Go to church"], "Young people often stay up late talking on cell phones, watching movies or shows online, or playing video games."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Presentation 3 vocabulary (27 words)", "一样 · 中午 · 事情 · 体育馆 · 先 · 周末 · 图书馆 · 宿舍 · 有时 · 然后 · 起床 · 饭馆",
                  "Vocabulary list (Presentation 3)",
                  "The book’s 27 words, with the traditional form where it differs.", VOC3)

UNIT = unit("第七课 校园生活 Presentation 3: the weekend, 先…然后…, 有时…有时…, comparisons and area studies", [L1, L2, L3, L4, L5, L6, L7, L8])
