"""Unit 23: Lesson 8 (Chinese Food and Restaurants) Presentation 2, from the book's texts: reserving a table at the Great Wall
Restaurant, spelling out a name, Verb + 一下, 最好, 不要, 才, the reservation passages, the restaurant brochure and the
vocabulary list. The listening activities, the pictures, the web forms and the fill-in tables are not included; the lessons say so."""
from zh_auto import *
from zh_l8_vocab import VOC2

PART = ["吗", "们", "呢"]
FOOD = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P2 = [
    ("服务员", "喂，您好！这里是长城饭店。", "Hello! This is the Great Wall Restaurant."),
    ("大卫", "您好。我想订一张八人的桌子。", "Hello. I would like to reserve a table for eight."),
    ("服务员", "什么时间？", "What time?"),
    ("大卫", "最好晚上六点以后，我们四点才下课。", "Preferably after six in the evening; we don’t finish class until four."),
    ("服务员", "我查一下。对不起，六点的桌子都订满了。", "Let me check. Sorry, the tables at six are all booked."),
    ("大卫", "那，七点的呢？", "Then how about seven?"),
    ("服务员", "七点的还有。", "There are still tables at seven."),
    ("大卫", "行。你们餐馆有什么特色菜？", "Okay. What specialty dishes does your restaurant have?"),
    ("服务员", "我们的广东菜很有特色。", "Our Cantonese food is very distinctive."),
    ("大卫", "太好了！我朋友很喜欢广东菜。对了，菜不要太咸，不要放味精。", "Great! My friends like Cantonese food very much. Oh, by the way, don’t make the dishes too salty, and don’t put in MSG."),
    ("服务员", "没问题，我们的菜都很清淡，你们一定喜欢。请问，你叫什么名字？", "No problem; our dishes are all mild, you will surely like them. May I ask, what is your name?"),
    ("大卫", "我叫大卫。姓石，石头的石。", "My name is David. The surname is Shi, the shi of 石头 (stone)."),
    ("服务员", "谢谢！明天晚上见。", "Thank you! See you tomorrow evening."),
]
CLOZE = [("我想订一___桌子，___是明天晚上七点的。", "张 / 最好"), ("我___。七点的桌子都___。八点的可以吗？", "查一下 / 订满了"), ("___，那就八点的吧。", "没问题"), ("我们的菜很___，不___也不辣，很少放___。", "清淡 / 咸 / 味精"), ("你___会喜欢我们的___菜。", "一定 / 特色")]
CHUN = [("服务员", "喂，您好！这里是长城饭店。", "Hello! This is the Great Wall Restaurant."), ("春生", "您好。我想订一张桌子。", "Hello. I would like to reserve a table."), ("服务员", "什么时间？", "What time?"),
        ("春生", "下星期三晚上六点半。", "Next Wednesday at six thirty in the evening."), ("服务员", "请问有几位？", "How many people, please?"), ("春生", "五个人。", "Five people."),
        ("服务员", "没问题。您贵姓？", "No problem. May I have your surname?"), ("春生", "我姓陆，陆军的陆。我叫陆春生。", "My surname is Lu, the lu of 陆军 (army). My name is Lu Chunsheng."), ("服务员", "谢谢！下星期三见！", "Thank you! See you next Wednesday!")]
L1 = lesson(
    "Presentation 2: reserving a table (dialog)",
    "我想订一张八人的桌子 · 订满了 · 不要太咸，不要放味精 · 石头的石",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss with your partner. A. Have you ever reserved a table? For what event in particular? B. What information do you need to provide when reserving a table? C. What information would you like to have from the restaurant when reserving a table? D. What kind of complications might you encounter when reserving a table?"),
        card("Presentation 2: 大卫 reserves a table at the Great Wall Restaurant",
             "The book also prints this dialog in traditional characters (for example 喂，您好！這裡是長城飯店).",
             examples=dlg(P2)),
        card("Activity 1 (Listening): global and detailed listening",
             "A. Is this conversation face-to-face or over the phone? How do you know? Why does David want to reserve a table? Why does he prefer to reserve for after 6 p.m.? B. Take notes as if you were taking David’s reservation: customer name, reservation time, number of people, special requests. (The recording is not included. From the text: it is over the phone, since the waiter answers 喂 and the restaurant is named; David wants a table for eight; he prefers after six because his class ends at four. The reservation: 石 (David), seven in the evening, tomorrow, eight people; not too salty and no MSG.)"),
        card("Activity 2: complete the sentences with the word bank",
             "Word bank: 特色, 订满了, 一定, 清淡, 咸, 味精, 最好, 查一下, 张, 没问题. Compare your work with a partner’s, then discuss your strategies for finding the right answers. The book’s five sentences, with the words that fit (the key is mine):",
             tables=[table(["Sentence", "Words"], [(a, b) for a, b in CLOZE], title="Fill in the blanks")]),
        card("Activity 3 (Reading and Speaking): another reservation",
             "Pair up. Read the conversation, complete the table (customer’s name and reservation), then perform the dialog.",
             examples=dlg(CHUN)),
    ],
    exercises=[
        M("Is this conversation face-to-face or over the phone?", "Over the phone: the waiter says 喂 and names the restaurant", ["Face-to-face: the waiter shows a table", "At the restaurant door", "By e-mail"], "喂，您好！这里是长城饭店 is how one answers the phone."),
        M("How many people is the table for?", "Eight", ["Four", "Six", "Two"], "我想订一张八人的桌子。"),
        M("Why does David prefer after six?", "His class ends at four", ["He eats late", "He works until six", "The restaurant opens at six"], "我们四点才下课。"),
        M("What is wrong with the tables at six?", "They are all booked", ["They are too small", "They are broken", "They are too expensive"], "六点的桌子都订满了。"),
        M("What time does David finally reserve?", "Seven in the evening", ["Six in the evening", "Eight in the evening", "Four in the afternoon"], "七点的还有。 行。"),
        M("What is the restaurant’s specialty?", "Cantonese food", ["Sichuan food", "Beijing roast duck", "Dumplings"], "我们的广东菜很有特色。"),
        M("What special requests does David make?", "Not too salty, and no MSG", ["Very spicy", "A table by the window", "Vegetarian food only"], "菜不要太咸，不要放味精。"),
        M("How does David spell his surname?", "石头的石", ["陆军的陆", "木子李", "孔子的孔"], "我叫大卫。姓石，石头的石。"),
        M("When does the Chunsheng reservation take place?", "Next Wednesday at 6:30 p.m., for five people", ["Tomorrow at seven, for eight", "This Saturday at noon", "Next Friday at eight, for two"], "下星期三晚上六点半。 五个人。"),
        M("How does 春生 spell his surname?", "陆军的陆", ["石头的石", "木子李", "孔子的孔"], "我姓陆，陆军的陆。"),
        F("我想订一___桌子。", "张", PART, "张 is the measure word for tables."),
        F("对不起，六点的桌子都订___了。", "满", ["再", "给", "放"], "订满了: fully booked."),
        F("我们的菜都很___，你们一定喜欢。", "清淡", ["订满", "作业", "操场"], "清淡 means mild in flavor."),
        mean("订", "ding4", "book; reserve", ["check", "put", "stone"]),
        mean("没问题", "mei2 wen4 ti2", "no problem", ["excuse me", "it would be best", "full"]),
    ],
)

# ------------------------------------------------------------------ 2. phone numbers and spelling names
RESTS = [("林姐饭店", "Linjie Restaurant (365-9088)"), ("好又来酒家", "Haoyoulai Restaurant (157-3296)"), ("东北餐馆", "Northeastern Restaurant (157-3360)"), ("山城饭馆", "Shancheng Restaurant (356-8705)"), ("台湾小吃店", "Taiwanese Snack Shop (809-5763)"), ("韩国冷面馆", "Korean Cold Noodle House (869-5703)")]
SPELL = [("我姓李，木子李。", "My surname is Li, the Li made of 木 and 子."), ("我叫陆明，陆军的陆，明天的明。", "My name is Lu Ming: the lu of 陆军 and the ming of 明天."), ("我姓孔，孔子的孔。", "My surname is Kong, the kong of Confucius (孔子).")]
SURN = [("张", "Zhang", "弓长张"), ("陈", "Chen", "耳东陈"), ("吴", "Wu", "口天吴"), ("林", "Lin", "双木林"), ("章", "Zhang", "立早章"), ("许", "Xu", "言午许"), ("胡", "Hu", "古月胡"), ("吕", "Lü", "双口吕")]
PHONE = [("喂，您好！这里是青龙酒楼。", "Hello! This is the Qinglong Restaurant."), ("请问，您贵姓？", "May I ask, what is your surname?"), ("请问，您需要什么帮助？", "May I ask, what help do you need?")]
L2 = lesson(
    "Presentation 2 activities: answering the phone and spelling out a name",
    "喂，您好！ · 林姐饭店 · 木子李 · 陆军的陆 · 孔子的孔",
    requires=[],
    cards=[
        card("Activity 4: answer the phone as the host",
             "In Chinese, your partner reads out a phone number at random from the list below. On hearing the number, answer the phone as though you were the host or hostess at the corresponding restaurant, and take the reservation; take turns until you have taken reservations for all six numbers. For example, you hear 219-3576 (the Qinglong Restaurant), so you answer: 喂，您好！这里是青龙酒楼. Also use 请问, 您贵姓? and 请问, 您需要 (xūyào, need) 什么帮助 (bāngzhù, help)?",
             examples=[D(z, e) for z, e in PHONE],
             tables=[wtable(rows_py(RESTS), title="The six restaurants and their numbers")]),
        card("Activity 5: specifying the characters of a name",
             "Because there are so many homophones in Chinese (for example 陆 lù and 卢 lú, 李 lǐ and 黎 lí), people usually specify the characters in their names. There are three main methods, each with its own formulaic expression: 1. break down the character components (mainly for surnames); 2. cite a commonly known word that contains the character; 3. refer to a famous person who shares the same character.",
             examples=[D(z, e) for z, e in SPELL]),
        card("Activity 5A: use the first method for these surnames",
             "Use the first method (我姓李，木子李) to specify the surnames 张 Zhāng, 陈 Chén, 吴 Wú, 林 Lín, 章 Zhāng, 许 Xǔ, 胡 Hú and 吕 Lǚ. The usual formulas (the key is mine):",
             tables=[wtable([(f, auto_py(f), f"{a}: {b}") for a, b, f in SURN], title="Spelling out the surnames")]),
        card("Activities 5B, 6 and 7",
             "5B: specify your full Chinese name using any of the three methods. Activity 6: think of a special occasion for which you might need to make a restaurant reservation and complete the table 我想订一张桌子: 几个人？ 最好什么时间？ Then role-play customer and receptionist with the form: customer name, reservation time, number in party; switch roles and perform for the class. Activity 7: A. Listen to a dialog and write the reservation as if you were the receptionist (number in party, preferred time, reserved time; audio, not included). B. Pair up: Student A is the receptionist, and without showing it to Student B first crosses out a few of the table sizes and reservation times in the form for the Great Wall Restaurant: Lunch 11:00 a.m.–3:00 p.m. with tables for 10, 8, 6, 4 and 2 and slots 11:00–12:00, 12:00–1:00, 1:00–2:00, 2:00–3:00; Dinner 4:00–10:00 p.m. with the same table sizes and slots 4:00–5:00, 5:00–6:00, 7:00–8:00, 8:00–9:00, 9:00–10:00. Student B makes a reservation while A takes down the customer name, phone, preferred time, reserved time and number in party, and tells B which tables and times are available. Switch roles and repeat."),
    ],
    exercises=[
        M("How does the host answer the phone?", "喂，您好！这里是青龙酒楼。", ["您几位？", "这边请。", "请慢用。"], "喂 is “hello” on the phone; 这里是 + name says who is speaking."),
        M("Which question asks for a customer’s surname politely?", "请问，您贵姓？", ["你叫什么？", "你是谁？", "您几位？"], "贵姓 is the polite way to ask a surname."),
        M("Which question asks what help the customer needs?", "请问，您需要什么帮助？", ["请问，您贵姓？", "请问，您几位？", "请问，几点？"], "需要什么帮助: what help do you need?"),
        M("Why do people spell out their names in Chinese?", "There are many homophones in Chinese", ["The characters are too long", "Names are secret", "Teachers insist on it"], "陆 lù and 卢 lú sound alike."),
        M("Which method is used in 我姓李，木子李?", "Break down the character’s components", ["Cite a known word with the character", "Name a famous person", "Write it in pinyin"], "木 + 子 = 李."),
        M("Which method is used in 陆军的陆?", "Cite a commonly known word containing the character", ["Break down the components", "Name a famous person", "Write it in pinyin"], "陆军 (army) contains 陆."),
        M("Which method is used in 孔子的孔?", "Refer to a famous person with the same character", ["Break down the components", "Cite a common word", "Write it in pinyin"], "孔子 is Confucius."),
        M("How would you spell the surname 林 by components?", "双木林", ["耳东陈", "弓长张", "古月胡"], "林 is two 木 (trees)."),
        M("How would you spell the surname 胡 by components?", "古月胡", ["双木林", "言午许", "口天吴"], "胡 = 古 + 月."),
        M("How would you spell the surname 吴 by components?", "口天吴", ["双口吕", "立早章", "耳东陈"], "吴 = 口 + 天."),
        M("How would you spell the surname 吕 by components?", "双口吕", ["口天吴", "双木林", "古月胡"], "吕 is two 口 (mouths)."),
        F("我姓李，___子李。", "木", ["火", "口", "月"], "李 is 木 over 子."),
        F("我叫陆明，陆军的陆，明天的___。", "明", ["陆", "军", "天"], "The word for 明 is 明天."),
        mean("帮助", "bang1 zhu4", "help", ["need", "surname", "reserve"]),
    ],
)

# ------------------------------------------------------------------ 3. verb + 一下
YIXIA = [("你过来！", "Come over here!"), ("你过来一下！", "Come over here a second!"), ("我查一下。", "Let me check."), ("请等一下。", "Please wait a moment."), ("你看一下这本书。", "Take a look at this book."), ("我查一下地图。", "Let me check the map.")]
SEVEN = [("少吃糖。", "少吃点儿糖。", "Eat less sugar."), ("喝茶吧！", "喝点儿茶吧！", "Have some tea!"), ("最好先查地图。", "最好先查一下地图。", "It’s best to check the map first."),
         ("下个周末，你去见我父母好吗？", "下个周末，你去见一下我父母好吗？", "Next weekend, would you go and meet my parents?"), ("你想再来米饭吗？", "你想再来点儿米饭吗？", "Would you like some more rice?"),
         ("先休息吧。", "先休息一下吧。", "Take a rest first."), ("给你们介绍，这位是王老师。", "给你们介绍一下，这位是王老师。", "Let me introduce you: this is Teacher Wang.")]
L3 = lesson(
    "Presentation 2 grammar: Verb + 一下",
    "我查一下 · 请等一下 · 你过来一下 · 一点儿 against 一下",
    requires=[],
    cards=[
        card("Verb + 一下",
             "To convey that an action is carried out briefly or casually, 一下 can be added to the verb. Verb + 一下 can also indicate an attempt to do something. Finally, like (一)点儿, 一下 can be added to soften the tone of a statement. Compare 你过来！(Come over here!) and 你过来一下！(Come over here a second!). Pattern: (Subject) + Verb + 一下 (+ Object). The difference between 一点儿 and 一下 is that 一点儿 refers to quantity, while 一下 refers to action.",
             examples=[D(z, e) for z, e in YIXIA]),
        card("Activity 1: add (一)点儿 or 一下 to the sentences",
             "Add (一)点儿 or 一下 to the seven sentences and say them out loud. (New words: 休息 xiūxi, to rest; 介绍 jièshào, to introduce.) One way to do it (the key is mine):",
             examples=[D(b, e) for a, b, e in SEVEN]),
    ],
    exercises=[
        M("What does 一下 add to a verb?", "It makes the action brief or casual, or softens the tone", ["It makes the action past", "It makes the action negative", "It means “one hour”"], "Verb + 一下: briefly, casually."),
        M("Which sentence is softer: 你过来！ or 你过来一下！?", "你过来一下！", ["你过来！", "They are equal", "Neither is polite"], "一下 softens the command."),
        M("What does 我查一下 mean?", "Let me check (briefly)", ["I checked for a year", "I never check", "Check it all day"], "查一下: check, take a quick look."),
        M("What does 一点儿 refer to?", "Quantity", ["Action", "Time", "Place"], "一点儿 refers to quantity; 一下 to action."),
        M("What does 一下 refer to?", "Action", ["Quantity", "Time", "Place"], "一下 refers to the action."),
        M("Which sentence is right for “Let me introduce you”?", "给你们介绍一下。", ["给你们一下介绍。", "给你们介绍点儿。", "一下给你们介绍。"], "介绍 is an action, so 一下 follows the verb."),
        M("Which is right for “Eat less sugar” (a quantity)?", "少吃点儿糖。", ["少吃一下糖。", "少一下吃糖。", "少吃糖一下。"], "糖 is a noun, so 点儿 is the right word."),
        M("Which is right for “Take a rest first”?", "先休息一下吧。", ["先休息点儿吧。", "先一下休息吧。", "休息先一下吧。"], "休息 is an action, so 一下."),
        M("Where does 一下 go?", "After the verb", ["Before the verb", "At the end of any sentence", "Before the subject"], "Verb + 一下 (+ Object)."),
        F("请等___。", "一下", ["点儿", "吗", "们"], "等一下: wait a moment."),
        F("我查一下___。", "地图", ["吗", "们", "呢"], "查一下 + object."),
        F("你过来___！", "一下", ["点儿", "们", "呢"], "一下 softens 过来."),
        mean("一下", "yi2 xia4", "a bit (for quick or brief actions)", ["table", "stone", "MSG"]),
        mean("查", "cha2", "check", ["put", "reserve", "full"]),
    ],
)

# ------------------------------------------------------------------ 4. 最好
ZUIHAO = [("（你）最好十点以前睡觉。", "You had better go to bed before ten."), ("你最好今天给他打一个电话。", "You had better call him today."), ("上课以前，最好预习一下课文。", "Before class, it is best to preview the text."),
          ("晚上最好不要喝咖啡。", "In the evening it is best not to drink coffee."), ("最好不要吃太多糖。", "It is best not to eat too much sugar.")]
ZUIHAO_SAY = [("现在已经十二点了，你最好不要玩儿电子游戏了。", "It’s 12 a.m., but your roommate is still playing a video game: You had better not play video games any more."), ("你作业做了很长时间了，最好休息一下。", "Your roommate has been doing homework for a long time: You had better take a rest."),
              ("你最好每天早上锻炼身体。", "Your friend failed the PT test: You had better exercise every morning."), ("你最好少放点儿糖。", "Your friend puts too much sugar in his coffee: You had better put in less sugar."),
              ("我们最好看一下地图。", "You are lost on the way to Chinatown: We had better look at the map.")]
L4 = lesson(
    "Presentation 2 grammar: 最好 as “had better”",
    "最好晚上六点以后 · 最好十点以前睡觉 · 最好不要…",
    requires=[],
    cards=[
        card("最好: “it would be best to” or “had better”",
             "As we have learned, 最好 means “the best”, as in 我老家最好的季节是春天. 最好 can also mean “it would be best to” or “had better”. It is often used when giving advice or even politely making demands, as in the line from Presentation 2, “最好晚上六点以后.” Pattern: (Subject) + 最好 + Predicate.",
             examples=[D(z, e) for z, e in ZUIHAO]),
        card("Activity 2 (Speaking): polite suggestions with 最好",
             "Use 最好 to make polite suggestions aloud for five situations: 1. It’s 12 a.m., but your roommate is still playing a video game. 2. Your roommate has been doing homework for a long time and is very tired. 3. Your friend failed their PT test. 4. Your friend puts too much sugar in his coffee. 5. You are driving with your friend to Chinatown in San Francisco, but you get lost. One possible answer each (the key is mine):",
             examples=[D(z, e) for z, e in ZUIHAO_SAY]),
    ],
    exercises=[
        M("What does 最好 mean in 最好晚上六点以后?", "it would be best to; preferably", ["the best", "the worst", "very good"], "As advice or preference, 最好 means “had better”."),
        M("What does 你最好十点以前睡觉 mean?", "You had better go to bed before ten", ["You went to bed at ten", "You are the best at sleeping", "You sleep ten hours"], "最好 + advice."),
        M("What does 晚上最好不要喝咖啡 mean?", "In the evening it is best not to drink coffee", ["In the evening the best coffee is cold", "You must drink coffee", "Coffee is good"], "最好不要 + verb: best not to."),
        M("What does 上课以前，最好预习一下课文 mean?", "Before class, it is best to preview the text", ["After class, preview the text", "The text is the best", "Never preview the text"], "最好 + predicate."),
        M("What does 最好 mean in 我老家最好的季节是春天?", "the best", ["had better", "would like", "must"], "最好的季节: the best season."),
        M("Where does 最好 go?", "After the subject, before the predicate", ["At the end", "Before the subject", "After the object"], "(Subject) + 最好 + Predicate."),
        M("Which is the right way to say “You had better call him today”?", "你最好今天给他打一个电话。", ["你今天给他最好打一个电话。", "最好你给他今天打电话一个。", "你给他最好打电话今天。"], "The time word goes after 最好."),
        M("Which is polite advice for a friend who put too much sugar in his coffee?", "你最好少放点儿糖。", ["你最好多放糖。", "你放糖了。", "糖很好。"], "最好 + 少 + verb."),
        F("上课以前，___预习一下课文。", "最好", ["再", "给", "才"], "最好 makes the advice polite."),
        F("晚上最好___要喝咖啡。", "不", ["没", "吗", "们"], "最好不要: best not to."),
        F("我们___十点以前睡觉。", "最好", ["一下", "点儿", "们"], "最好 + predicate."),
        mean("最好", "zui4 hao3", "had better; it would be best", ["no problem", "check", "mild"]),
    ],
)

# ------------------------------------------------------------------ 5. 不要
BUYAO = [("不要太咸。", "Don’t make it too salty."), ("最好不要放味精。", "It’s best not to put in MSG."), ("不要说英文。", "Don’t speak English."), ("上课的时候不要玩儿手机。", "Don’t play with your cell phone during class."), ("不要太晚睡觉。", "Don’t go to bed too late.")]
BUYAO3 = [("上课时不要睡觉。", "Don’t sleep in class."), ("周末不要太晚起床。", "Don’t get up too late on weekends."), ("每天都要吃早饭。", "Eat breakfast every day."), ("不要太晚睡觉。", "Don’t go to bed too late."),
          ("要努力学习，不要玩手机。", "Study hard; don’t play with your phone."), ("每天都要预习和复习。", "Preview and review every day."), ("不要太晚做作业。", "Don’t do homework too late.")]
HEALTH = [("不要吃太多糖。", "Don’t eat too much sugar."), ("最好不要喝太多可乐。", "It’s best not to drink too much Coke."), ("不要太晚睡觉。", "Don’t go to bed too late."), ("最好不要整天坐着玩儿手机。", "It’s best not to sit all day playing with your phone."), ("每天要多喝水。", "Drink more water every day.")]
L5 = lesson(
    "Presentation 2 grammar: 不要 for negative commands",
    "不要太咸 · 不要放味精 · 上课的时候不要玩儿手机",
    requires=[],
    cards=[
        card("不要: negative commands",
             "Negative commands like “don’t” are formed with 不要. Patterns: (Subject) + 不要 + Verb [+ Object] and (Subject) + 不要 + Adjective. The subject is usually omitted, as in English.",
             examples=[D(z, e) for z, e in BUYAO]),
        card("Activity 3: which commands might apply to you?",
             "A. Which of these seven commands might apply to you? B. Write a few negative commands to remind your classmates of things they shouldn’t do.",
             examples=[D(z, e) for z, e in BUYAO3]),
        card("Activity 4 (Speaking): eight pictures about health",
             "Based on eight pictures (not included), use 不要 and 最好不要 to make suggestions for maintaining good health. Some of mine (the book leaves the answer open):",
             examples=[D(z, e) for z, e in HEALTH]),
    ],
    exercises=[
        M("What does 不要 express?", "A negative command: don’t …", ["A past action", "A wish", "A question"], "不要 + verb or adjective."),
        M("What does 不要太咸 mean?", "Don’t make it too salty", ["It isn’t salty", "It is very salty", "Add more salt"], "不要 + 太 + adjective."),
        M("What does 不要说英文 mean?", "Don’t speak English", ["I can’t speak English", "Speak English", "English isn’t easy"], "不要 + verb + object."),
        M("What does 上课的时候不要玩儿手机 mean?", "Don’t play with your cell phone during class", ["Play with your phone after class", "The phone is in class", "Class has no phone"], "…的时候 + 不要."),
        M("What does 每天都要吃早饭 mean?", "You must eat breakfast every day", ["Don’t eat breakfast", "Never eat", "Breakfast is every day"], "要 here means must, not 不要."),
        M("Which sentence is a polite “best not to”?", "最好不要放味精。", ["不放味精吗？", "放味精。", "没放味精。"], "最好不要 softens the order."),
        M("Why is the subject usually omitted in 不要 sentences?", "As in English commands, the listener is understood", ["Chinese has no subjects", "It is rude to say it", "It is a question"], "Like “Don’t …” in English."),
        M("Which means “Don’t go to bed too late”?", "不要太晚睡觉。", ["不要睡觉太晚。", "太不要晚睡觉。", "睡觉不太要晚。"], "不要 + 太 + adjective + verb."),
        F("上课时___要睡觉。", "不", ["没", "吗", "们"], "不要 is the negative command."),
        F("不要放___。", "味精", ["作业", "操场", "预习"], "放味精: put in MSG."),
        F("最好不要吃太多___。", "糖", ["作业", "操场", "预习"], "吃糖: eat sugar."),
        mean("味精", "wei4 jing1", "MSG", ["salty", "mild", "table"]),
        mean("咸", "xian2", "salty", ["MSG", "mild", "full"]),
    ],
)

# ------------------------------------------------------------------ 6. 才
CAI = [("我四点才下课。", "I don’t finish class until four."), ("我晚饭以后才做作业。", "I don’t do homework until after dinner."), ("我考试前才开始努力学习。", "I don’t start studying hard until just before the test."),
       ("周末他九点才起床。", "On weekends he doesn’t get up until nine."), ("到了台湾几个月以后，我才适应了这里的生活。", "It was not until a few months after arriving in Taiwan that I got used to life here.")]
CAI5 = [("我两个月以前才开始学中文。", "I only began studying Chinese two months ago."), ("作业太多了！我每天晚上十一点以后才睡觉。", "There’s too much homework! I don’t go to bed until after eleven every night."), ("我早上六点以后才起床。", "I don’t get up until after six in the morning."),
        ("星期六和星期天，我十点才起床。", "On Saturdays and Sundays I don’t get up until ten."), ("我八岁才上学。", "I didn’t start school until I was eight.")]
L6 = lesson(
    "Presentation 2 grammar: 才 for “later than expected”",
    "我四点才下课 · 晚饭以后才做作业 · 十点才起床",
    requires=[],
    cards=[
        card("才 + verb",
             "The adverb 才 can be used to indicate that something happened later than expected. Its English equivalent is “not until”. Pattern: Subject + Time + 才 + Verb.",
             examples=[D(z, e) for z, e in CAI]),
        card("Activity 5: which statements apply to you?",
             "A. Which of these five statements might apply to you? B. Based on your own situation, write three more statements using 才 and read them to the class.",
             examples=[D(z, e) for z, e in CAI5]),
        card("Activity 6: a weekday and weekend table",
             "A. Complete a table with the times you do these activities on weekdays (星期一～星期五) and weekends (星期六～星期天): 起床, 锻炼, 早饭, 午饭, 晚饭, 做作业, 睡觉. B. Your partner asks you in Chinese when you do these activities on the weekends; when applicable, answer using 才."),
    ],
    exercises=[
        M("What does 才 show in 我四点才下课?", "Something happened later than expected", ["Something happened earlier than expected", "Something happened twice", "Something will not happen"], "才 = not until."),
        M("What is the English equivalent of 才?", "not until", ["already", "again", "also"], "我四点才下课: I don’t finish until four."),
        M("What does 周末他九点才起床 mean?", "On weekends he doesn’t get up until nine", ["On weekends he gets up at nine, early", "He never gets up", "He gets up at ninety"], "Time + 才 + verb."),
        M("What does 我八岁才上学 mean?", "I didn’t start school until I was eight", ["I started school at eight, very early", "I went to school eight times", "I am eight"], "才: later than expected."),
        M("Where does 才 go?", "After the time word, before the verb", ["At the end", "Before the subject", "After the object"], "Subject + Time + 才 + Verb."),
        M("Which is right for “I don’t do homework until after dinner”?", "我晚饭以后才做作业。", ["我才晚饭以后做作业。", "我做作业晚饭以后才。", "晚饭才我以后做作业。"], "Time + 才 + verb."),
        M("Which is right for “I don’t get up until ten”?", "我十点才起床。", ["我才十点起床吗。", "十点我起床才。", "我起床十点才。"], "十点 + 才 + 起床."),
        M("Which sentence shows the speaker thinks it is late?", "我每天晚上十一点以后才睡觉。", ["我每天晚上九点就睡觉。", "我每天睡觉。", "我早上六点起床。"], "才 shows lateness."),
        F("我四点___下课。", "才", ["再", "给", "放"], "才 + verb: not until."),
        F("周末他九点___起床。", "才", ["再", "给", "放"], "九点才起床."),
        F("到了台湾几个月以后，我___适应了这里的生活。", "才", ["再", "给", "放"], "几个月以后才: not until months later."),
        mean("才", "cai2", "just; later than expected", ["had better", "put", "table"]),
        mean("时间", "shi2 jian1", "time", ["table", "stone", "MSG"]),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
FORM = [("预订日期", "reservation date (closed Sundays and the first Monday of every month)"), ("预订时间", "reservation time: 12:00, 12:30, 13:00, 13:30; 18:00, 19:00, 20:00, 21:00"), ("人数", "number of people"),
        ("姓名", "name: 姓 (surname) and 名 (given name)"), ("称呼", "title: 先生 (Mr.) or 女士 (Ms.)"), ("手机号码", "cell phone number"), ("电子邮件", "e-mail"), ("特别要求", "special requests")]
PASS_R1 = ("春节快到了，我和四个朋友想去一家中国饭店吃晚饭。他们都想吃饺子，还想吃辣子鸡、糖醋鱼、麻婆豆腐。小文说他可以吃辣的，不过不要太辣。我给那家饭店打电话，说我们想订一张这个星期六下午六点的桌子。服务员告诉我，他们只有八点的了。因为春节的时候在饭店吃饭的人太多。最后，我只好订了八点的。",
           "The Spring Festival is coming and I and four friends want to go to a Chinese restaurant for dinner. They all want dumplings, and also spicy chicken, sweet and sour fish and mapo tofu. Xiaowen says he can eat spicy food, but not too spicy. I called the restaurant and said we wanted a table for six o’clock this Saturday afternoon. The waiter told me they only had eight o’clock left, because too many people eat in restaurants during the Spring Festival. In the end I had no choice but to book eight o’clock.")
PASS_R2 = ("今天是我先生的生日。我们想和孩子们一起到九龙饭店吃晚饭。那家饭店的饭菜很好吃，每天人都挺多的。不过我今天太忙了，到下午四点才给饭店打电话。我说，我想订一张五个人的桌子，最好是今天下午五点的，不过，七点以前的都行。可是服务员说，今天的桌子都已经订满了。不过他说，他们在东城有一家分店。我可以给那里打电话。",
           "Today is my husband’s birthday. We want to have dinner with the children at the Jiulong Restaurant. The food there is delicious and it is quite crowded every day. But I was too busy today and did not call the restaurant until four in the afternoon. I said I wanted a table for five, preferably at five this afternoon, but anything before seven would do. But the waiter said that all the tables today are booked. But he said they have a branch in the east of the city. I could call there.")
L7 = lesson(
    "Presentation 2 skill integration: the online form and two reservation stories",
    "预订时间 · 人数 · 特别要求 · 春节 · 订满了 · 分店",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): an online reservation form",
             "A. Make restaurant reservations online by highlighting your preferences and completing the table with either characters or pinyin (the web page, with the language and service tabs, is not included). B. In pairs, role-play customer and receptionist to make the same reservation by phone; don’t forget the customary courtesy expressions; switch roles and repeat. The fields of the form:",
             tables=[wtable(rows_py(FORM[:0] + [(a, b) for a, b in FORM]), title="餐桌预订 (table reservation)")]),
        card("Activity 2 (Listening and Speaking): two phone dialogs",
             "A. Student A listens to Dialog 1 and Student B to Dialog 2 (audio, not included). Dialog 1: When does the customer want to reserve a table? What times are available? What are the details of the confirmed reservation? Dialog 2: Why did the customer call? What was the misunderstanding? What are the details of the final reservation? B. Compare answers in two groups. C. Return to your partner and convey the important information in Chinese."),
        card("Activity 3 (Reading and Speaking): two passages",
             "A. Read the passages and complete the forms: Passage 1 (Reservation Event, Reservation Request, Available Times, Final Result, Special Requests) and Passage 2 (Reservation Event, Preferred Times, Available Times, Final Result). B. Pair up and, based on Passage 1, role-play the phone conversation between customer and receptionist; switch roles and repeat for Passage 2.",
             examples=[D(*PASS_R1), D(*PASS_R2)]),
    ],
    exercises=[
        M("Passage 1: what is the occasion?", "A dinner for the Spring Festival with four friends", ["A birthday", "A wedding", "A business meeting"], "春节快到了，我和四个朋友想去一家中国饭店吃晚饭。"),
        M("Passage 1: how many people will eat?", "Five: the speaker and four friends", ["Four", "Six", "Eight"], "我和四个朋友."),
        M("Passage 1: what foods do they want?", "Dumplings, spicy chicken, sweet and sour fish and mapo tofu", ["Only dumplings", "Roast duck and noodles", "Vegetarian dishes only"], "饺子、辣子鸡、糖醋鱼、麻婆豆腐."),
        M("Passage 1: what does 小文 request?", "He can eat spicy food, but not too spicy", ["No spicy food at all", "As spicy as possible", "No meat"], "小文说他可以吃辣的，不过不要太辣。"),
        M("Passage 1: what time did the speaker want, and what was available?", "Six on Saturday; only eight was available", ["Eight; only six was available", "Seven; nothing was available", "Noon; only one o’clock"], "他们只有八点的了。"),
        M("Passage 1: why was only eight available?", "Too many people eat out during the Spring Festival", ["The restaurant was closed", "The cooks were sick", "It was a holiday for the restaurant"], "因为春节的时候在饭店吃饭的人太多。"),
        M("Passage 1: what was the final result?", "The speaker booked eight o’clock", ["The speaker did not book", "The speaker booked six", "The speaker booked a different restaurant"], "最后，我只好订了八点的。"),
        M("Passage 2: what is the occasion?", "The speaker’s husband’s birthday", ["The Spring Festival", "Her own birthday", "Her children’s school trip"], "今天是我先生的生日。"),
        M("Passage 2: when did she phone the restaurant?", "At four in the afternoon", ["At noon", "In the morning", "At seven"], "到下午四点才给饭店打电话。"),
        M("Passage 2: what did she ask for?", "A table for five at five o’clock; before seven would do", ["A table for two", "A table at nine", "A private room"], "最好是今天下午五点的，不过，七点以前的都行。"),
        M("Passage 2: what did the waiter say?", "All of today’s tables were booked, but the branch in the east might help", ["Come at nine", "There is a table at six", "They are closed"], "今天的桌子都已经订满了；在东城有一家分店。"),
        M("In the web form, what does 特别要求 ask for?", "Special requests", ["Surname", "Phone number", "Number of people"], "特别要求: special requests."),
        M("What does 称呼 ask for in the form, with 先生 and 女士 as the choices?", "How to address you (Mr. or Ms.)", ["Your address", "Your job", "Your age"], "称呼: form of address."),
        F("我今天太忙了，到下午四点___给饭店打电话。", "才", ["再", "给", "放"], "才: not until four."),
        F("今天的桌子都已经订___了。", "满", ["再", "给", "放"], "订满了: fully booked."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
Q6 = [("你（你的家人，朋友）上一次订饭店是什么时候？是为什么？", "When was the last time you (your family, friends) reserved a restaurant? Why?"), ("是打电话订的吗？", "Did you reserve by phone?"), ("为什么订那家饭店？", "Why did you reserve that restaurant?"),
      ("订的是什么时间？有几个人？", "What time did you reserve? How many people were there?"), ("有什么特别的要求吗？", "Were there any special requests?"), ("你是和谁一起去的？每人点自己的菜还是大家一起吃？", "Whom did you go with? Did each person order their own dish, or did everyone eat together?")]
BROCH = [("长城饭店（四颗星，评论二百零七条）", "Great Wall Restaurant (four stars, 207 reviews). Introduction: traditional Chinese food, home-style Sichuan dishes. Specialties: pickled-cabbage fish, boiled fish, sweet and sour fish."),
         ("中华园（四颗星，评论一百六十七条）", "Zhonghua Garden (four stars, 167 reviews). Home-style northern dishes. Specialties: egg-flower soup, sweet and sour shrimp, kung pao chicken, stir-fried three delicacies."),
         ("中华园（四颗星，评论二百三十五条）", "Zhonghua Garden (four stars, 235 reviews). Sichuan food and Sichuan snacks. Specialties: mapo tofu, hot pot."),
         ("中华园（四星半，评论三百四十一条）", "Zhonghua Garden (four and a half stars, 341 reviews). Cantonese food and seafood. Specialties: Cantonese soy-sauce chicken, Cantonese shrimp dumplings, Cantonese-style roast duck.")]
REVIEWS = [("这是我第一次来这家饭店。这里的菜很好吃，服务员也很友好，听我说中文他很高兴。", "This is my first time at this restaurant. The food here is delicious and the waiters are friendly; he was very happy to hear me speak Chinese."),
           ("我常常和朋友们到这家饭店吃晚饭。这里的服务员都很好，饭菜也很好。每次在这里吃饭我们都很高兴。", "I often have dinner with friends at this restaurant. The waiters here are all very good and the food is good too. Every time we eat here we are happy."),
           ("我喜欢这家饭店。饭菜很好吃，又不太贵。饭店很干净。这里的火锅很有特色！", "I like this restaurant. The food is delicious and not too expensive. The restaurant is very clean. The hot pot here is very distinctive!"),
           ("这家饭店很小，只有五六张小桌子，可是每份菜都挺多。老板也很好，每次去吃饭都给我们免费的小吃！", "This restaurant is very small, with only five or six little tables, but every dish has quite a lot. The owner is also good; every time we eat there he gives us free snacks!")]
REVQ = [("你常去这家饭店吗？", "Do you often go to this restaurant?"), ("最近一次是什么时候去的？", "When did you go most recently?"), ("你自己去的还是和朋友一起去的？", "Did you go alone or with friends?"), ("这家饭店的服务怎么样？", "How is the service at this restaurant?"),
        ("你喜欢这家饭店吗？为什么？", "Do you like this restaurant? Why?"), ("你最喜欢/不喜欢的菜是什么？为什么？", "What is your favorite or least favorite dish? Why?"), ("你给这家饭店几星？", "How many stars do you give this restaurant?")]
EMAIL = ("我住的地方有一家中国饭店。我常常去那儿吃晚饭，每个星期三四次。不过，那里有的菜很贵，有的菜挺咸，味精也很多，常吃对身体不好。可是，我也不想自己做饭，太麻烦，而且，我每天工作都很忙，没有太多时间做饭。你有什么好主意？",
         "There is a Chinese restaurant where I live. I often go there for dinner, three or four times a week. But some of the dishes there are expensive, some are quite salty, and there is a lot of MSG, so it is bad for your health to eat it often. But I also don’t want to cook for myself; it is too much trouble, and besides I am very busy at work every day and don’t have much time to cook. Do you have any good ideas?")
REPLY = [("我觉得你最好不要常去那家饭店吃饭。", "I think you had better not go to that restaurant often."), ("你可以先查一下附近别的饭店，找一家菜清淡、不放味精的。", "You can first look up other restaurants nearby and find one with mild dishes and no MSG."),
         ("周末你也可以做一点儿简单的菜，一次多做一点儿，下个星期再吃。", "On weekends you can also cook some simple dishes, make a bit more each time, and eat it next week.")]
L8 = lesson(
    "Presentation 2: using Chinese in context (restaurant brochure, reviews, e-mail)",
    "长城饭店 · 最新评论 · 你给这家饭店几星？ · 你有什么好主意？",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking): six questions",
             "In groups of three, take turns asking each other the following six questions to discuss your experiences making restaurant reservations.",
             examples=[D(z, e) for z, e in Q6]),
        card("Activity 2 (Reading and Speaking): a brochure of local Chinese restaurants",
             "A. Read the following brochure and decide which restaurant to have dinner at (the book shows four entries; three of them are labeled 中华园). Fill in your choice of restaurant and the reason for your choice. B. Get together with classmates who chose the same restaurant, list the times each of you wants to go and your special requests. C. Discuss which time works best for everyone, then call the restaurant to make a reservation while a student from another group plays the host or hostess (lunch 11:00 a.m.–3:00 p.m. and dinner 4:00–10:00 p.m., tables for 10, 8, 6, 4 and 2, with slots 11:00–12:00, 12:00–1:00, 1:00–2:00, 2:00–3:00; 4:00–6:00, 6:00–8:00, 8:00–10:00). The four entries, and the latest review of each:",
             examples=[D(z, e) for z, e in BROCH] + [D(z, e) for z, e in REVIEWS]),
        card("Activity 3 (Reading, Writing and Speaking): write a review",
             "A. Think of a Chinese restaurant you have been to and write a review in Chinese based on seven questions, then share details of your own experience on the review page (the form, with 取消 cancel and 提交 submit, is not included). B. A partner translates your review into English; discuss the translation to ensure accuracy. C. List your reservation preferences and call the restaurant your partner recommended.",
             examples=[D(z, e) for z, e in REVQ]),
        card("Activities 4 and 5: plan a dinner outing; reply to a friend’s e-mail",
             "Activity 4: in two groups of three, plan a dinner outing in Chinese: compare the three restaurants you reviewed and agree on one; agree on the best time; list your special requests; call the restaurant; one student from the other group plays the host while two write down the details. Activity 5: read this e-mail from a friend and reply with your advice. The e-mail, and one possible reply (the reply is mine):",
             examples=[D(*EMAIL)] + [D(z, e) for z, e in REPLY]),
    ],
    exercises=[
        M("In the brochure, which restaurant is named 长城饭店 and what is its specialty?", "A traditional Sichuan restaurant whose specialties include 酸菜鱼, 水煮鱼 and 糖醋鱼", ["A Cantonese restaurant with seafood", "A hot pot restaurant", "A northern restaurant with kung pao chicken"], "简介：传统中餐，家常四川菜."),
        M("Which brochure entry serves 广式烤鸭 and 广东虾饺?", "The Cantonese restaurant with 341 reviews", ["The hot pot restaurant", "The Great Wall Restaurant", "The northern-style restaurant"], "简介：广东菜，海鲜."),
        M("Which entry is known for 火锅?", "The Sichuan restaurant with 235 reviews", ["The Cantonese restaurant", "The Great Wall Restaurant", "The northern restaurant"], "特色菜：麻婆豆腐，火锅."),
        M("In the review, what makes the first customer happy?", "The waiter was happy to hear him speak Chinese", ["The food was free", "The restaurant was empty", "He got a discount"], "听我说中文他很高兴。"),
        M("In the third review, why does the reviewer like the restaurant?", "Good food, not too expensive, clean, and the hot pot is distinctive", ["Cheap but dirty", "Only tourists go there", "It is open all night"], "饭菜很好吃，又不太贵。饭店很干净。火锅很有特色！"),
        M("In the fourth review, what does the owner give?", "Free snacks every time", ["Free beer", "A discount card", "Nothing"], "每次去吃饭都给我们免费的小吃！"),
        M("In the fourth review, how big is the restaurant?", "Very small: five or six little tables", ["Very big", "Two floors", "Only one table"], "只有五六张小桌子."),
        M("What question asks how many stars you give a restaurant?", "你给这家饭店几星？", ["你常去这家饭店吗？", "你最喜欢什么菜？", "你和谁一起去的？"], "几星: how many stars."),
        M("What is the problem in the friend’s e-mail?", "The friend eats at a restaurant three or four times a week, but the food is salty and has MSG; the friend does not want to cook", ["The friend cannot find a restaurant", "The friend has no money", "The friend dislikes Chinese food"], "常吃对身体不好。 可是，我也不想自己做饭."),
        M("Why doesn’t the friend want to cook?", "It is too much trouble and the friend is very busy at work", ["The friend cannot cook", "The friend has no kitchen", "The friend dislikes vegetables"], "太麻烦，而且我每天工作都很忙."),
        M("What does the friend ask at the end?", "你有什么好主意？ — Do you have any good ideas?", ["你几位？", "你在哪儿工作？", "你想吃什么？"], "你有什么好主意？"),
        F("你给这家饭店___星？", "几", PART, "几星 asks for a number."),
        F("你喜欢这家饭店吗？___什么？", "为", ["还", "放", "查"], "为什么: why."),
        mean("评论", "ping2 lun4", "review, comment", ["table", "reserve", "salty"]),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Presentation 2 vocabulary (21 words)", "一下 · 才 · 最好 · 订 · 桌子 · 清淡 · 没问题 · 餐馆",
                  "Vocabulary list (Presentation 2)",
                  "The book’s 21 words, with the traditional form where it differs.", VOC2)

UNIT = unit("第八课 中国食品与餐馆 Presentation 2: reserving a table", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
