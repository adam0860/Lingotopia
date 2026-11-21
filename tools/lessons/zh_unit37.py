"""Unit 37: Lesson 13 (At the Airport) Presentation 2 from the book's texts: the customs dialog, the action-measure complement,
到…去…, directional verbs after verbs, the skill-integration stories, using Chinese in context and the vocabulary list.
Audio, pictures, forms as images and websites are not included; answer keys the book does not print are mine."""
from zh_auto import *
from zh_l13_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"长": "chang2"}
    if any(k in zh for k in ("得上", "得坐", "得先")):
        f["得"] = "dei3"
    if "还给她的上司" in zh:
        f["还"] = "hai2"
    i = zh.find("行李")
    while i >= 0:
        f[i + 1] = "li5"          # 行李 xíngli, not the surname Lǐ
        i = zh.find("行李", i + 2)
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D   # dlg() builds its lines with zh_auto.D, so it picks up the fixes above


PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the customs dialog
P2 = [("边检员", "您好。请出示一下你的护照。", "Hello. Please show me your passport."),
      ("大卫", "这是我的护照。", "Here is my passport."),
      ("边检员", "你的签证一月到期。现在已经六月了。", "Your visa expired in January. It is already June now."),
      ("大卫", "这页是去年的签证，新的签证在下一页。", "This page is last year’s visa; the new visa is on the next page."),
      ("边检员", "哦，看到了。你这次来中国做什么？", "Oh, I see it. What are you coming to China for this time?"),
      ("大卫", "我到北京大学参加一个中文培训班。", "I’m going to Peking University to take part in a Chinese training course."),
      ("边检员", "你准备在中国呆多长时间？", "How long do you plan to stay in China?"),
      ("大卫", "培训班三个月，然后我还要到中国各地去旅行，一共差不多六个月。", "The course is three months, and then I will also travel around China, about six months altogether."),
      ("边检员", "你有没有需要报关的物品，比如食品、药品什么的？", "Do you have any items to declare, such as food, medicine and so on?"),
      ("大卫", "没有，我带的钱也没有超过两万人民币。", "No, and the money I’m carrying doesn’t exceed 20,000 RMB."),
      ("边检员", "好。请摘下眼镜，看这儿。好了，你可以入关了。祝你在中国学习愉快！", "OK. Please take off your glasses and look here. All right, you may enter. Have a good time studying in China!")]
A2 = [("乘坐国际航班的旅客需要办理入关手续。", "Passengers on international flights must go through entry procedures."), ("您的签证已经到期了，您不能入关。", "Your visa has expired; you cannot enter."), ("您有需要报关的物品吗？比如食品或是药品？", "Do you have any items to declare? For example food or medicine?"), ("您带的现金不能超过两万元人民币。", "The cash you carry cannot exceed 20,000 yuan RMB."), ("请摘下眼镜。", "Please take off your glasses.")]
PASS5 = ("有了一个国家的签证就可以进入这个国家了吗？不，你还需要经过边检和海关。在中国，边检是检查人员的，海关是检查物品的。如果你到中国去，中国边检员会检查你的护照、签证和入境登记卡。如果没有问题，你就可以进入中国。但是，你带的东西还需要经过海关检查。签证有不同的种类，比如旅行签证，商务签证，探亲签证，工作签证和学生签证。不同的签证可以在中国停留的时间也不一样。")
PASS5_E = ("Can you enter a country once you have a visa for it? No, you still have to pass border inspection and customs. In China, border inspection checks people and customs checks goods. If you go to China, the Chinese border inspector will check your passport, visa and entry registration card. If there is no problem, you may enter China. But the things you bring still have to pass customs inspection. There are different kinds of visas, such as tourist visas, business visas, family-visit visas, work visas and student visas. Different visas allow different lengths of stay in China.")
L1 = lesson(
    "Lesson 13 Presentation 2: entering China (border inspection)",
    "请出示一下你的护照 · 签证到期 · 你准备在中国呆多长时间？ · 有没有需要报关的物品？",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Have you ever been to another country? B. What was the purpose of your visit and how long did you stay? C. What documents are needed for travel to foreign countries? D. What questions did the customs officer ask you?"),
        card("Presentation 2: at border inspection",
             "David goes through entry at the border-inspection counter (the book also prints it in traditional characters). The book writes the amount as 两万人民币.",
             examples=dlg(P2)),
        card("Activities 1 and 2",
             "Activity 1 (Listening). A. Global listening: where does the conversation take place, and who are the speakers? B. Detailed listening: 1. What problem did the officer find with the passport and what was the traveler’s explanation? 2. How long will the traveler stay and why is he visiting? 3. What concerns does the officer have about his items? 4. What final step must be completed before he is granted entry? (Audio, not included. From the dialog: at the border inspection counter, an officer and David; the visa had expired in January but the new visa is on the next page; six months for a Chinese training course and travel; food and medicine; take off his glasses.) Activity 2 (Reading, Listening and Speaking). A. Complete the five sentences with words found in the presentation. B. Pair up, read your sentences and discuss your choices. The book leaves blanks; the completed sentences are mine:",
             examples=[D(z, e) for z, e in A2]),
        card("Activity 3 (Speaking)",
             "A. Imagine a trip you might take to China and fill in: 1. 为什么到中国 2. 准备住在哪个城市 3. 准备住多长时间 4. 需要报关的物品. B. Pair up; your partner plays the customs officer and you the passenger, going through these questions, then switch: 1. May I see your passport please? 2. Where did you fly from? 3. What is your destination? 4. What is the purpose of your visit? 5. How long are you planning to stay? 6. Where will you be staying? 7. Did you bring any food into the country? 8. How much currency are you carrying with you? 9. Do you have anything to declare?"),
        card("Activities 4 and 5",
             "Activity 4 (Listening). Listen to two dialogs between a traveler and a customs officer: Dialog 1: 1. What is the purpose of the visit? 2. Is there anything wrong with the visa? Dialog 2: 1. Which of the traveler’s belongings were described and what did the officer say about each? Transcribe unknown words and check your dictionary. (Audio, not included.) Activity 5 (Reading). Read the passage and write down the EEIs (essential elements of information); compare with a classmate. My EEIs: a visa alone is not enough; border inspection checks people and documents (passport, visa, entry card); customs checks goods; visas come in kinds (tourist, business, family-visit, work, student) with different lengths of stay.",
             examples=[D(PASS5, PASS5_E)]),
    ],
    exercises=[
        M("What does the officer ask David to do first?", "Show his passport", ["Open his suitcase", "Take off his shoes", "Sign a form"], "请出示一下你的护照。"),
        M("What did the officer notice about the visa?", "It expired in January", ["It was torn", "It was for another country", "It had no photo"], "你的签证一月到期。"),
        M("What was David’s explanation?", "The new visa is on the next page", ["He lost the visa", "The visa is at home", "The visa is a mistake"], "新的签证在下一页。"),
        M("Why is David coming to China?", "To join a Chinese training course at Peking University", ["To visit his family", "To do business", "To work as a teacher"], "我到北京大学参加一个中文培训班。"),
        M("How long will David stay in China?", "About six months", ["Three weeks", "One year", "Two days"], "一共差不多六个月。"),
        M("What does 报关 mean?", "To declare items at customs", ["To close a gate", "To book a flight", "To renew a visa"], "报关: declare at customs."),
        M("What are examples of items to declare, according to the officer?", "Food and medicine", ["Cameras and phones", "Books and clothes", "Cash only"], "食品、药品什么的."),
        M("How much money does the officer mention as the limit?", "两万人民币", ["两千人民币", "二十万人民币", "两百人民币"], "没有超过两万人民币。"),
        M("What does David have to do before entering?", "Take off his glasses and look at the officer", ["Show his luggage", "Pay a fee", "Wait an hour"], "请摘下眼镜，看这儿。"),
        M("In China, what does border inspection (边检) check?", "People", ["Goods", "Planes", "Prices"], "边检是检查人员的."),
        M("What does customs (海关) check?", "Goods", ["People", "Visas only", "Flight numbers"], "海关是检查物品的."),
        M("Which is NOT a visa kind in the passage?", "A transit-only visa", ["Tourist visa", "Student visa", "Work visa"], "旅行, 商务, 探亲, 工作, 学生."),
        mean("签证", "qian1 zheng4", "visa", ["glasses", "suitcase", "ticket"]),
        mean("摘下", "zhai1 xia4", "to take off", ["to put on", "to pick up", "to turn on"]),
        F("你的签证一月到___。", "期", PART, "到期: expire."),
        F("你准备在中国呆多长___间？", "时", PART, "多长时间: how long."),
        F("请出___一下你的护照。", "示", PART, "出示: show."),
    ],
)

# ------------------------------------------------------------------ 2. action-measure complement
AM = [("昨天，我去了一次医院。", "Yesterday I went to the hospital once."), ("我看了两次这个电影。", "I’ve seen this movie twice."), ("李老师去年回了两次国。", "Teacher Li went back to her country twice last year."), ("你一周锻炼了几次？", "How many times did you work out in a week?"), ("我一个星期去商店买一次东西。", "I go to the store to buy things once a week.")]
AM1 = [("他去了两次水族馆。", "He went to the aquarium twice. (the book’s example)"), ("他去了两次旧金山。", "He has been to San Francisco twice."), ("他看了三次书。", "He read a book three times."), ("他租了一次车。", "He rented a car once."), ("他一个星期去一次商店。", "He goes to the store once a week."), ("他锻炼了几次？", "How many times did he work out?")]
L2 = lesson(
    "Lesson 13 Presentation 2 grammar: the action-measure word 次",
    "去了一次医院 · 看了两次这个电影 · 一周锻炼了几次？",
    requires=[],
    cards=[
        card("Action-measure word as complement 动量词",
             "Earlier you learned measure words for nouns, like 一盘饺子, 两条领带, 一套公寓. Verbs can also take measure words as complements: the action-measure complement is formed by a numeral and an action-measure word. In this lesson the officer asks David 你这次来中国做什么？; the 次 in this sentence is an action-measure word. Two of the most commonly used are 下 (discussed in Lesson 8; it indicates a short and quick action) and 次, which means the number of times an action occurred. As a complement, the numeral-measure unit comes after the verb. When the verb takes an object, the placement varies: if the object is a noun, it appears after the measure word; if it is a pronoun, it appears before the measure word. Patterns: Verb + Number + Measure Word (+ Noun); Verb + (Pronoun) + Number + Measure Word.",
             examples=[D(z, e) for z, e in AM]),
        card("Activities 1 and 2",
             "Activity 1 (Speaking). Describe how often 马小文 did each activity since coming to Monterey, using complete Chinese sentences. The book’s example: visit the aquarium, two times: 他去了两次水族馆. Then: 1. gone to San Francisco, two times; 2. read a book, three times; 3. rented a car, once; 4. gone to the store, once a week; 5. exercised, how many times; and three other things he may have done. My sentences:",
             examples=[D(z, e) for z, e in AM1]),
        card("Activity 2 (Speaking)",
             "In groups of three, reflect on your basic training and the many restrictions you had, and how often you had to do certain things. List your experiences and share them with the class. The book’s example:",
             examples=[D("一周只能打一次电话。", "We could only make a phone call once a week.")]),
    ],
    exercises=[
        M("What does an action-measure word count?", "The number of times an action happens", ["The number of objects", "The time of day", "The place of an action"], "次: times."),
        M("Where does the numeral-measure unit go?", "After the verb", ["Before the subject", "After the object always", "At the start of the sentence"], "Verb + number + measure."),
        M("Where does a noun object go?", "After the measure word", ["Before the measure word", "Before the verb", "It is dropped"], "Verb + number + measure + noun."),
        M("Where does a pronoun object go?", "Before the measure word", ["After the measure word", "At the end", "It is dropped"], "Verb + pronoun + number + measure."),
        M("What does 我看了两次这个电影 mean?", "I have seen this movie twice", ["I saw two movies", "I saw this movie second", "I will see this movie"], "两次: twice."),
        M("What does 下 indicate as an action-measure word?", "A short, quick action", ["A long process", "A habit", "A question"], "一下: a bit."),
        M("What does 你一周锻炼了几次？ ask?", "How many times did you work out in a week?", ["Where did you work out?", "When did you work out?", "Why do you work out?"], "几次: how many times."),
        M("Which sentence is correct?", "他去了两次水族馆。", ["他去水族馆了两次。", "他两次去了水族馆。", "他了去两次水族馆。"], "Verb + 了 + number + measure + noun."),
        F("昨天，我去了一___医院。", "次", PART, "一次: once."),
        F("我一个星期去商店买一次东___。", "西", PART, "东西: things."),
        F("一周只能打一次电___。", "话", PART, "打电话: make a call."),
    ],
)

# ------------------------------------------------------------------ 3. 到…去…
DQ = [("我到学校去上课。", "I go to school to attend class."), ("你到哪儿去买机票？", "Where are you going to buy an air ticket?"), ("我到机场去接朋友。", "I’m going to the airport to pick up a friend."), ("我到图书馆去借书。", "I’m going to the library to borrow books."), ("他们到哪家电影院去看电影？", "Which movie theater are they going to for a movie?"), ("我到图书馆去。", "I’m going to the library. (= 我去图书馆)")]
DQ3 = [("到农贸市场去买点儿水果。", "Go to the farmers’ market to buy some fruit."), ("到北京去参加汉语培训班。", "Go to Beijing to take a Chinese training course."), ("到操场去集合。", "Go to the drill field to fall in."), ("到图书馆去借书。", "Go to the library to borrow books."), ("到图书馆去还书。", "Go to the library to return books."), ("到机场去接朋友。", "Go to the airport to pick up a friend."), ("到银行去换钱。", "Go to the bank to change money."), ("到海边去散步。", "Go to the seaside for a walk.")]
DQ4 = [("先到网上去订机票。", "First go online to book the ticket."), ("然后到机场去办理登机手续。", "Then go to the airport to check in."), ("再到安检处去过安检。", "Then go to the security checkpoint to go through security."), ("最后到登机口去上飞机。", "Finally go to the boarding gate to board the plane.")]
L3 = lesson(
    "Lesson 13 Presentation 2 grammar: the 到…去… construction",
    "我到学校去上课 · 你到哪儿去买机票？ · 到机场去接朋友",
    requires=[],
    cards=[
        card("到…去… construction",
             "The 到…去… construction is similar to the English “go to” or “leave for (someplace)” pattern. Subject + 到 + Place + 去 + Verb (+ Obj.). Note: 到 + Place + 去 is equal to 去 + Place; for example 我到图书馆去 = 我去图书馆.",
             examples=[D(z, e) for z, e in DQ]),
        card("Activity 3 (Reading)",
             "Complete the sentences using appropriate places and actions; pair up and read your sentences to each other, noting the differences. The eight sentences begin 到 ___ 去买点儿水果, 到 ___ 去参加汉语培训班, 到 ___ 去集合, 到 ___ 去借书, and 到图书馆去 ___, 到机场去 ___, 到银行去 ___, 到海边去 ___. My completions:",
             examples=[D(z, e) for z, e in DQ3]),
        card("Activity 4 (Writing and Listening)",
             "A. Pair up and brainstorm four steps involved in taking a flight using the 到…去… structure (Step 1 to Step 4). B. Listen to the passage and write down the differences from your own process, then discuss with your partner. (Audio, not included.) My four steps:",
             examples=[D(z, e) for z, e in DQ4]),
    ],
    exercises=[
        M("What does 到…去… resemble in English?", "“go to” or “leave for”", ["“come from”", "“because of”", "“instead of”"], "到 + place + 去."),
        M("Which equals 我到图书馆去?", "我去图书馆。", ["我从图书馆去。", "我在图书馆去。", "我去图书馆了吗？"], "到 + place + 去 = 去 + place."),
        M("Where does the verb of purpose go in 到…去…?", "After 去", ["Before 到", "Between 到 and the place", "It cannot appear"], "到 + place + 去 + verb."),
        M("What does 你到哪儿去买机票？ ask?", "Where are you going to buy a ticket?", ["When will you fly?", "Who will buy the ticket?", "How much is the ticket?"], "到哪儿去: to where."),
        M("What does 我到机场去接朋友 mean?", "I’m going to the airport to pick up a friend", ["I’m a friend from the airport", "I’m taking a plane with a friend", "My friend works at the airport"], "接朋友: pick up a friend."),
        M("What does 他们到哪家电影院去看电影？ ask?", "Which cinema are they going to?", ["Which movie are they watching?", "Who is going to the movie?", "When is the movie?"], "哪家电影院."),
        M("Which sentence is in correct order?", "我到学校去上课。", ["我去到学校上课。", "到我学校去上课。", "我上课到学校去。"], "Subject + 到 + place + 去 + verb."),
        F("我到银行___换钱。", "去", PART, "到银行去换钱."),
        F("我___图书馆去借书。", "到", PART, "到…去…."),
        F("到海边去散___。", "步", PART, "散步: take a walk."),
    ],
)

# ------------------------------------------------------------------ 4. directional verbs after verbs
DV = [("上课前，他走进教室。", "Before class, he walked into the classroom."), ("下课，他走出教室。", "After class, he walked out of the classroom."), ("中午他跑上山吃饭。", "At noon, he ran up the hill to have lunch."), ("吃完饭，他走下山。", "After lunch, he walked down the hill."), ("三点，他走回宿舍。", "At 3 p.m., he walked back to his dorm.")]
DV5 = [("我们爬上山看日出。", "We hiked up the mountain to see the sunrise."), ("他跑过桥见我们。", "He ran over the bridge to see us."), ("他拿起手机打电话给我。", "He picked up his phone to call me."), ("他从书包拿出一本书。", "He took out a book from his bookbag.")]
DV6 = [("昨天，我看见小李走进一个商店买东西。", "Yesterday I saw Xiao Li walk into a store to buy things. (the book’s example)"), ("老师先坐下，然后，拿起课本开始上课。", "The teacher first sits down and then picks up the textbook and begins class. (the book’s example)")]
L4 = lesson(
    "Lesson 13 Presentation 2 grammar: directional verbs after verbs",
    "摘下眼镜 · 走进教室 · 跑上山 · 拿出一本书",
    requires=[],
    cards=[
        card("Simple directional verbs used to indicate direction of action",
             "The directional verbs discussed in Presentation 1 can be put after verbs to indicate the direction of an action. In Presentation 2 the officer asks David 摘下眼镜, “take down your glasses”; here the directional verb 下 is a complement that indicates the direction of 摘. Verb + Directional Verb + Object.",
             examples=[D(z, e) for z, e in DV]),
        card("Activities 5 and 6",
             "Activity 5 (Reading). Reorder the words into the correct sequence to match the English translation: 1. 爬 我们 看 山 上 日出 (sunrise): We hiked up the mountain to see the sunrise. 2. 他 见 过 跑 桥 我们: He ran over the bridge to see us. 3. 他 打 给我 拿 手机 起 电话: He picked up his phone to call me. 4. 从 拿 一本书 书包 出 他: He took out a book from his bookbag. My ordered sentences: Activity 6 (Reading). Pair up and describe a real or imaginary directional action or actions with the “V + directional verb” structure, then take turns repeating the activity at least three times.",
             examples=[D(z, e) for z, e in DV5] + [D(z, e) for z, e in DV6]),
    ],
    exercises=[
        M("In 摘下眼镜, what does 下 show?", "The direction of the action 摘", ["The time", "A question", "The number"], "Directional complement."),
        M("What does 他走进教室 mean?", "He walked into the classroom", ["He walked out of the classroom", "He ran to class", "He cleaned the classroom"], "走进: walk in."),
        M("What does 他走出教室 mean?", "He walked out of the classroom", ["He walked into the classroom", "He closed the classroom", "He left the school"], "走出: walk out."),
        M("What does 中午他跑上山吃饭 mean?", "At noon he ran up the hill to eat", ["He ran down the hill", "He ate on the way home", "He ate at noon on the track"], "跑上山: run up the hill."),
        M("What does 吃完饭，他走下山 mean?", "After eating he walked down the hill", ["After eating he went up the hill", "He didn’t eat", "He walked home"], "走下山: walk down."),
        M("Which sequence means “He took out a book from his bookbag”?", "他从书包拿出一本书。", ["他拿书包出一本书从。", "他一本书从书包拿出。", "从他书包拿一本书出。"], "从 + place + verb + 出 + object."),
        M("Which sequence means “We hiked up the mountain to see the sunrise”?", "我们爬上山看日出。", ["我们看日出爬上山。", "爬上我们山看日出。", "我们山爬上看日出。"], "爬上山, then 看日出."),
        M("Which means “He picked up his phone”?", "他拿起手机", ["他拿手机起", "他起拿手机", "手机拿起他"], "拿起: pick up."),
        F("上课前，他走___教室。", "进", PART, "走进: walk in."),
        F("老师先坐___，然后，拿起课本开始上课。", "下", PART, "坐下: sit down."),
        F("他跑___桥见我们。", "过", PART, "跑过: run over."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
S1 = ("我叫张力，我太太叫章丽，汉字不一样，可是写成拼音都是Zhang Li。所以在护照和机票上，我们的名字是一样的。有一次在法国海关，工作人员问我：“你为什么一个人买两张机票？”我说：“有一张是我太太的，我们的名字一样。”海关人员说：“你们的姓当然是一样的，可是名怎么会一样呢？”我说：“我们的姓和名都一样。”她不相信：“男人和女人的名怎么会一样？”我解释说：“我们的名字发音是一样的，但不是同一个字，意思不一样。”她很怀疑地看着我，又拿着我们的机票和护照看了很长时间，还给她的上司打了个电话。最后，她说：“把你们的中文名字写下来。”我把那几个汉字写了下来，她看了半天，最后终于让我们过了海关。她一边在护照上盖章一边说：“你们中国人的名字真有意思！”")
S1_E = ("My name is Zhang Li and my wife’s name is Zhang Li too (different characters), but written in pinyin both are Zhang Li. So on our passports and plane tickets our names are the same. Once at French customs the officer asked me: “Why are you, one person, buying two tickets?” I said: “One of them is my wife’s; our names are the same.” The customs officer said: “Your surnames are of course the same, but how can your given names be the same?” I said: “Our surnames and given names are both the same.” She didn’t believe it: “How can a man’s and a woman’s given names be the same?” I explained: “Our names sound the same, but they aren’t the same characters and the meanings are different.” She looked at me doubtfully, held our tickets and passports and looked at them for a long time, and even phoned her superior. In the end she said: “Write down your Chinese names.” I wrote the characters down, she looked at them for a long while, and finally let us through customs. As she stamped our passports she said: “Your Chinese people’s names are really interesting!”")
S2 = ("有一次我从成都坐飞机到旧金山，下飞机以后，很多中国人排队过海关。站在我前面的女孩抱着一个很可爱的玩具熊。有一个小胖子工作人员走过来问：“这只玩具熊是你的？”女孩儿有点儿紧张，说：“是我的。”那个工作人员说：“你在这儿等着，我很快就回来。”说完他就跑去叫另一位工作人员，然后两个人一起往这边跑来。大家都紧张起来，有什么问题吗？在熊的肚子里有什么东西吗？毒品？很多现金？或者是中国人出国爱带的食品药品什么的？这时，小胖子工作人员把手机给同事，说：“来，给我和这只熊照张相！”")
S2_E = ("Once I flew from Chengdu to San Francisco, and after getting off the plane many Chinese people queued up for customs. The girl standing in front of me was holding a very cute teddy bear (wánjùxióng). A chubby staff member came over and asked: “Is this teddy bear yours?” The girl was a bit nervous and said: “It’s mine.” The staff member said: “Wait here, I’ll be back soon.” After saying that he ran off to call another staff member, and then the two of them ran over this way together. Everyone got nervous: was there a problem? Was there something inside the bear’s belly? Drugs? A lot of cash? Or the food and medicine Chinese people like to take abroad? Just then the chubby staff member handed his phone to his colleague and said: “Come on, take a picture of me and this bear!”")
TFS1 = [("他和他太太的名字是一样的。", "He and his wife have the same name."), ("他和太太一起去法国。", "He and his wife go to France together."), ("工作人员让他把他和太太的中文名字写下来。", "The officer had him write down his and his wife’s Chinese names."), ("海关工作人员认识汉字。", "The customs officer knows Chinese characters."), ("工作人员最后让他们过了海关。", "In the end the officer let them through customs.")]
TFS2 = [("飞机上有很多中国人。", "There were many Chinese on the plane."), ("海关有好几位工作人员。", "There were several customs staff."), ("工作人员觉得有一位女乘客有问题。", "The officer thought one female passenger had a problem."), ("那个女孩带了应该报关的东西。", "The girl carried items that should be declared."), ("工作人员给女孩和熊照了一张照片。", "The officer took a picture of the girl and the bear.")]
OUT = ("比如你从杭州的萧山机场去南非看世界杯，要是你已经有签证，你就要办理出关手续。等你飞了十多个小时，到了南非约翰内斯堡机场。你就要办理入关手续。在快到目的地的时候，空乘会让旅客填写一些表。下飞机以后，就要办理入关手续，海关官员会问你一些问题，比如你为什么要来南非，住在什么地方，什么时候离开。还会检查行李，要是都没有问题，他们会在你护照上盖章。你就正式到达了南非，可以去看比赛了。")
OUT_E = ("For example, if you go from Hangzhou’s Xiaoshan Airport to South Africa to watch the World Cup and you already have a visa, you have to go through exit procedures. After you have flown for more than ten hours and arrived at Johannesburg airport in South Africa, you have to go through entry procedures. When you are about to arrive at the destination, the flight attendants have passengers fill out some forms. After getting off the plane you go through entry procedures; customs officials ask you some questions, such as why you are coming to South Africa, where you will stay and when you will leave. They also inspect your luggage, and if everything is fine they stamp your passport. You have officially arrived in South Africa and can go watch the matches.")
L5 = lesson(
    "Lesson 13 Presentation 2: skill integration",
    "张力和章丽 · 玩具熊 · 什么是出关？什么是入关？",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Writing)",
             "A. Listen to the dialogs and fill in the table for Travelers 1 to 5: purpose of visit; intended length of stay; location of stay; items to declare (Y/N); first time to China (Y/N); documents mentioned. B. Pair up, take turns sharing the information you entered and discuss the differences. (Audio, not included.)"),
        card("Activity 2 (Reading, Speaking and Listening): Story 1",
             "A. Pair up. Two Chinese people are talking about their experiences with foreign customs; each partner reads one of the stories (use your dictionary when necessary). B. Without rereading, tell your story to your partner, then mark the statements true or false. The book writes the shared pinyin name as Zhang Li; because every spoken line here is Chinese only, the Chinese line says 都是一样的 (“is the same”) and the spelling is kept in the English line.",
             examples=[D(S1.replace("都是Zhang Li。", "都是一样的。"), S1_E)]),
        card("Story 1 statements",
             "The five statements about Story 1 (the book gives no key; mine: 1. True. 2. True. 3. True. 4. False, since she asked him to write the names down and looked at them a long time. 5. True):",
             examples=[D(z, e) for z, e in TFS1]),
        card("Story 2",
             "Story 2 and its statements (my key: 1. True. 2. False, only two officers are mentioned. 3. False, the officer just wanted a picture. 4. False. 5. False, he took a picture of himself with the bear):",
             examples=[D(S2, S2_E)] + [D(z, e) for z, e in TFS2]),
        card("Activity 3 (Reading, Speaking and Writing)",
             "A. Below is an answer posted online about international travel (什么是出关？什么是入关？). Read it and note any unknown words. B. Highlight the words you think are critical for understanding the passage and guess their meaning; compare with a classmate. C. Do you think the text defines the terms clearly? If not, type in your own definition of 出关 and 入关. My definitions: 出关 is completing the exit formalities (passport and visa check) when leaving a country; 入关 is completing the entry formalities on arrival (forms, officer’s questions, luggage inspection, passport stamp).",
             examples=[D(OUT, OUT_E)]),
    ],
    exercises=[
        M("Why are Zhang Li’s and Zhang Li’s names the same on passports?", "Both are written in pinyin as the same name", ["They are the same person", "They have the same characters", "They are twins"], "汉字不一样，可是写成拼音都是…"),
        M("What did the French customs officer find strange?", "Two tickets for one person with the same name", ["A missing passport", "A forged ticket", "A very heavy bag"], "你为什么一个人买两张机票？"),
        M("How did the speaker explain the names?", "They sound the same but are different characters with different meanings", ["They are the same characters", "They are nicknames", "They are family names only"], "不是同一个字，意思不一样。"),
        M("What did the officer ask him to do?", "Write down the Chinese names", ["Show a marriage certificate", "Call his wife", "Pay a fine"], "把你们的中文名字写下来。"),
        M("What did she say as she stamped the passports?", "Chinese names are really interesting", ["Go back home", "Welcome to France", "Don’t travel again"], "你们中国人的名字真有意思！"),
        M("In Story 2, what was the girl holding?", "A teddy bear", ["A passport", "A suitcase", "A baby"], "抱着一个很可爱的玩具熊。"),
        M("What did the passengers fear was inside the bear?", "Drugs or cash, or food and medicine", ["A bomb", "A phone", "A cat"], "毒品？很多现金？食品药品什么的？"),
        M("What did the officer really want?", "A photo of himself with the bear", ["To arrest the girl", "To search her luggage", "To take the bear"], "给我和这只熊照张相！"),
        M("According to the online answer, when is exit formality done?", "Before leaving, at the departure airport", ["After landing", "On the plane", "At the hotel"], "办理出关手续."),
        M("What do customs officials do on entry, per the answer?", "Ask questions, inspect luggage and stamp the passport", ["Sell tickets", "Change money", "Book hotels"], "会问你一些问题…检查行李…盖章."),
        mean("海关", "hai3 guan1", "customs", ["boarding gate", "security check", "luggage tag"]),
        F("她一边在护照上盖___一边说话。", "章", PART, "盖章: stamp."),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese in context
IDS = [("A German tourist", "德国人", "flown in from Japan; wants to stay three weeks in a hotel for sightseeing; passport expires May 5, 2021"), ("A visiting grandchild", "法国人", "visiting grandpa who lives here; summer vacation, two months at grandpa’s house; passport expires August 6, 2021"), ("An exchange student", "美国人", "six months at a language school, staying in a dormitory; passport expires December 31, 2021"),
       ("A business traveler", "美国人", "two-week business trip selling wine, staying in a hotel; passport expires May 7, 2021"), ("A university professor", "日本人", "going to a conference in Beijing, three days in a hotel; passport expires March 6, 2021"), ("A visiting brother", "加拿大人", "visiting his brother at his house until July 20; passport expires July 31, 2021")]
L6 = lesson(
    "Lesson 13 Presentation 2: using Chinese in context",
    "外国人入境卡 · 海关记录表 · 海关申报单",
    requires=[],
    cards=[
        card("Activity 1 (Speaking): choose an identity",
             "A. Each student chooses one identity from the following characters (each card also shows a passport with name, nationality, expiration date and number, and a photo; the photos are not included). B. Fill in the 外国人入境卡 (foreigner entry card) using your character’s information and your own where applicable.",
             tables=[table(["Character", "Nationality", "Situation"], [(a, b, c) for a, b, c in IDS], title="The six characters (book order)", say=[1])]),
        card("The 外国人入境卡",
             "The entry card (请交边防检查官查验) asks for: 姓, 名, 国籍, 护照号码, 在华地址, 男/女, 出生日期 (年, 月, 日), 入境事由 (only one may be ticked: 会议, 访问, 观光, 探亲, 就业, 学习, 返回常住地, 定居, 其他), 签证号码, 签证签发地, 航班号/船名/车次, then the statement 以上申明真实正确 and a signature line. (The form itself is an image and is not included.)"),
        card("Activities 2 and 3",
             "Activity 2 (Reading and Writing). A. Work in groups of three. One group plays customs officers for three places: 中国, 新加坡 and 台湾; the other group plays the travelers, each going to be interviewed by all three officers using their character’s information from Activity 1. The officers use the Customs Recording Sheet (Name, Nationality, Purpose of Visit, Intended Length of Stay, Location of Stay, Items to Declare? (Y/N), First Time? (Y/N)) to record each traveler’s information and sign the traveler’s visa after granting entry. B. The two groups switch roles and repeat. Activity 3 (Reading and Speaking). Pair up. Another form you must fill out before arriving is a customs declaration form. Read the sample form (a picture, not included) without using your dictionary and discuss with your partner what items must be declared if you are traveling to China."),
    ],
    exercises=[
        M("What is the 外国人入境卡?", "The foreigner entry card", ["A luggage tag", "A boarding pass", "A hotel card"], "外国人入境卡."),
        M("What does 入境事由 ask for?", "The purpose of entry", ["The date of birth", "The address", "The flight number"], "事由: reason."),
        M("What does 国籍 ask for?", "Nationality", ["Passport number", "Visa number", "Address"], "国籍: nationality."),
        M("What does 观光 mean on the entry card?", "Sightseeing", ["Business", "Study", "Work"], "观光: sightseeing."),
        M("What does 探亲 mean?", "Visiting relatives", ["Studying", "Working", "Attending a meeting"], "探亲: visit family."),
        M("Which three places do the officers represent in Activity 2?", "中国, 新加坡, 台湾", ["中国, 日本, 韩国", "中国, 香港, 澳门", "新加坡, 德国, 法国"], "Activity 2."),
        mean("国籍", "guo2 ji2", "nationality", ["address", "date of birth", "flight number"]),
        mean("观光", "guan1 guang1", "sightseeing", ["to study", "to work", "to attend a meeting"]),
    ],
)

L7 = vocab_lesson("Lesson 13 Presentation 2 vocabulary", "19 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十三课 人在机场 Presentation 2: customs, 次, 到…去…, directional verbs", [L1, L2, L3, L4, L5, L6, L7])
