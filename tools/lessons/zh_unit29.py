"""Unit 29: Lesson 10 (Housing and Rentals) Presentation 2, from the book's texts: touring the apartment, attributives, 是…可是…, existential 有,
什么时候, 如果…就…, the passage about the apartment, the vocabulary list. Audio, pictures, songs and videos are not included."""
from zh_auto import *
from zh_l10_vocab import VOC2

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

P2 = [
    ("张经理", "大卫，这就是你想租的公寓，我带你看一下吧！", "David, this is the apartment you want to rent; let me show you around!"),
    ("大卫", "客厅挺大的！沙发的颜色也很好，看起来很舒服。", "The living room is quite big! The color of the sofa is nice too, and it looks comfortable."),
    ("张经理", "我们再看看饭厅和厨房。你觉得怎么样？", "Let’s look at the dining room and kitchen too. What do you think?"),
    ("大卫", "饭厅还可以，厨房好像小了一点儿。", "The dining room is okay; the kitchen seems a little small."),
    ("张经理", "小是小了点，可是厨具很全，冰箱、洗碗机都有。", "It is a bit small, but the kitchenware is complete; there are a refrigerator and a dishwasher."),
    ("大卫", "哪个是主卧室？", "Which one is the master bedroom?"),
    ("张经理", "这是主卧室，地毯是新的。你看，卫生间也很大。", "This is the master bedroom, and the carpet is new. Look, the bathroom is big too."),
    ("大卫", "那是另一个卧室吧？", "That is the other bedroom, right?"),
    ("张经理", "对。房间里有书桌、书架，也可以作书房。", "Yes. The room has a desk and a bookshelf, and it can also be used as a study."),
    ("大卫", "这儿的环境怎么样？", "What is the neighborhood like?"),
    ("张经理", "环境很安全，交通也非常方便。", "The environment is very safe and the transportation is very convenient."),
    ("大卫", "我很喜欢这个公寓。什么时候可以签合同？", "I like this apartment very much. When can we sign the contract?"),
    ("张经理", "如果没什么问题，下周一我们就可以签合同。", "If there are no problems, we can sign the contract next Monday."),
    ("大卫", "好。谢谢您。下周见！", "Okay. Thank you. See you next week!"),
]
L1 = lesson(
    "Lesson 10 Presentation 2: touring the apartment (dialog)",
    "这就是你想租的公寓 · 小是小了点，可是… · 什么时候可以签合同？",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss. A. Have you, your friends or relatives ever rented housing? B. Did you or any of them inspect the house or apartment before renting? Why or why not? C. Can you describe your current living situation in Chinese?"),
        card("Presentation 2: 张经理 shows 大卫 the apartment",
             "The book also prints the dialog in traditional characters (for example 客廳挺大的！沙發的顏色也很好).",
             examples=dlg(P2)),
        card("Activity 1 (Listening and Speaking)",
             "A. Listen to Presentation 2 and answer: 1. What is the gist of this conversation? 2. What is the relationship between the two speakers? B. Listen again and answer: 1. What does David say about the couch? 2. What does David say about the dining room and kitchen, and how does the other person respond? 3. What is said about the master bedroom? 4. What are the items in the other bedroom? 5. What is the neighborhood like? 6. What do you think David will do next Monday? How do you know? C. Compare answers with a partner, then trade off sharing your answers with the class in Chinese. From the text: the sofa’s color is nice and it looks comfortable; the dining room is okay and the kitchen a bit small, but the manager says the kitchenware is complete; the master bedroom has a new carpet and a big bathroom; the other bedroom has a desk and a bookshelf and can be a study; the neighborhood is safe and convenient; David will probably sign the contract next Monday."),
    ],
    exercises=[
        M("What does 大卫 say about the living room?", "It is quite big", ["It is small", "It is dark", "It is dirty"], "客厅挺大的！"),
        M("What does 大卫 say about the sofa?", "The color is nice and it looks comfortable", ["It is old", "It is too big", "It is expensive"], "沙发的颜色也很好，看起来很舒服。"),
        M("What does 大卫 say about the kitchen?", "It seems a little small", ["It is very big", "It is dirty", "There is none"], "厨房好像小了一点儿。"),
        M("What does the manager say about the kitchen?", "The kitchenware is complete", ["It is the biggest room", "It has no refrigerator", "It is new"], "厨具很全，冰箱、洗碗机都有。"),
        M("What is new in the master bedroom?", "The carpet", ["The bed", "The desk", "The sofa"], "地毯是新的。"),
        M("What is in the other bedroom?", "A desk and a bookshelf", ["A bed and a closet", "A sofa", "A refrigerator"], "房间里有书桌、书架。"),
        M("What can the other bedroom be used as?", "A study", ["A kitchen", "A garage", "A dining room"], "也可以作书房。"),
        M("What is the neighborhood like?", "Safe, with convenient transportation", ["Noisy", "Far from everything", "Expensive"], "环境很安全，交通也非常方便。"),
        M("When can they sign the contract?", "Next Monday, if there is no problem", ["Today", "Next year", "Tomorrow morning"], "如果没什么问题，下周一我们就可以签合同。"),
        M("What does 什么时候可以签合同？ ask?", "When can we sign the contract?", ["Where do we sign?", "Who signs?", "How much is the contract?"], "什么时候: when."),
        F("沙发的颜色也很好，___起来很舒服。", "看", PART, "看起来: looks."),
        F("厨房好像小了一点儿，小是小了点，___是厨具很全。", "可", PART, "A是A，可是…"),
        F("这是主___室，地毯是新的。", "卧", PART, "主卧室: master bedroom."),
        F("如果没什么问题，下周一我们___可以签合同。", "就", PART, "如果…，就…"),
    ],
)

# ------------------------------------------------------------------ 2. activities and 带 作 全
A2 = [("甲：你觉得我租的公寓怎么样？", "What do you think of the apartment I rented?"), ("乙：这都是我买的新家具，怎么样？", "These are all the new furniture I bought; how is it?"), ("甲：这是我昨天买的厨具和餐具。", "These are the kitchenware and tableware I bought yesterday.")]
A2Q = [("大卫的公寓有几个卧室？卧室大不大？", "How many bedrooms does David’s apartment have? Are the bedrooms big?"), ("大卫的公寓有几个卫生间？", "How many bathrooms does David’s apartment have?"), ("公寓的环境和交通怎么样？", "What are the environment and transportation of the apartment like?")]
A3 = [("这个公寓带不带家具？", "Does this apartment come with furniture? (带: include; come with)"), ("明天我带你去看一下那个公寓。", "Tomorrow I will take you to see that apartment. (带: take; bring)"), ("这个房间很小，可以作书房。", "This room is small and can be used as a study. (作: serve as)"),
      ("我爸爸在电脑公司工作。", "My dad works at a computer company. (工作: to work)"), ("这家文具店东西很全，你要的文具都有。", "This stationery store has everything; it has all the stationery you want. (全: complete)"), ("这个学校很安全，不认识的人不能进来。", "This school is very safe; people who are not known cannot come in. (安全: safe)")]
L2 = lesson(
    "Lesson 10 Presentation 2 activities: attributives you hear, and 带, 作, 全",
    "我租的公寓 · 我买的新家具 · 带 作 工作 全 安全",
    requires=[],
    cards=[
        card("Activity 2 (Listening, Writing and Speaking)",
             "A. Listen to Dialog 1 and fill in the blanks with the attributive constructions you hear (audio, not included). B. Listen to Dialog 2 and answer the three questions. C. Compare your answers with a partner, then read them to the class. The book prints Dialog 1 with the attributives blank; the filled-in text (from the blanks as printed: 我租的公寓, 我买的新家具, 我昨天买的厨具和餐具) is, with 甲 and 乙 as the two speakers (their order is mine):",
             examples=[D(z, e) for z, e in A2]),
        card("Dialog 2 questions",
             "The questions for Dialog 2:",
             examples=[D(z, e) for z, e in A2Q]),
        card("Activity 3 (Reading, Speaking and Writing): 带, 作/工作, 全/安全",
             "A. In pairs, write the meaning and identify the part of speech of each vocabulary item in the sentences below: 1. 带; 2. 作, 工作; 3. 全, 安全. B. One student reads a sentence aloud and the other translates it; alternate through all six sentences. C. Share your translations with the class. The translations are mine:",
             examples=[D(z, e) for z, e in A3]),
        card("Activity 4 (Writing and Speaking)",
             "Pair up. You and a friend have rented an unfurnished apartment. Make a list of the furniture you need to buy (the book gives eight bullet points), then show it to the class and explain where you want to put the furniture. (A picture of furniture is not included.)"),
    ],
    exercises=[
        M("What does 带 mean in 这个公寓带不带家具？", "Come with; include", ["Take", "Carry", "Wear"], "带家具: comes with furniture."),
        M("What does 带 mean in 我带你去看一下那个公寓？", "Take (someone)", ["Include", "Buy", "Rent"], "带你去: take you."),
        M("What does 作 mean in 可以作书房？", "Serve as, be used as", ["Do homework", "Work at", "Make a mistake"], "作书房: use as a study."),
        M("What does 工作 mean in 我爸爸在电脑公司工作？", "To work", ["To rent", "To study", "To live"], "工作: work."),
        M("What does 全 mean in 东西很全？", "Complete", ["Cheap", "New", "Heavy"], "东西很全: has everything."),
        M("What does 安全 mean?", "Safe; safety", ["Convenient", "Cheap", "Complete"], "这个学校很安全."),
        M("Which is the attribute in 我昨天买的厨具？", "我昨天买的", ["厨具", "昨天", "我"], "An attributive precedes the noun it modifies."),
        M("What does 你觉得我租的公寓怎么样？ ask?", "What do you think of the apartment I rented?", ["Where is your apartment?", "How much is the rent?", "Who rented it?"], "我租的公寓: the apartment I rented."),
        F("这个公寓___不带家具？", "带", PART, "带不带: does it come with."),
        F("这个房间很小，可以___书房。", "作", PART, "作书房: use as a study."),
        F("这个学校很___，不认识的人不能进来。", "安全", ["作业", "操场", "预习"], "安全: safe."),
        F("这家文具店东西很___，你要的文具都有。", "全", PART, "全: complete."),
    ],
)

# ------------------------------------------------------------------ 3. the attributive
ATT = [
    ("1. Pronouns, nouns or noun phrases", [("这是我的书，不是图书馆的书。", "This is my book, not the library’s book."), ("那是学校图书馆的书。", "That’s a school library book.")]),
    ("2. Adjectives or adjectival phrases", [("那间大房间是我父母的卧室。", "The big room is my parents’ bedroom."), ("这个又漂亮又舒服的沙发是朋友给的。", "This beautiful and comfortable sofa was given to me by a friend.")]),
    ("3. Verbs or verb phrases", [("说话的那个同学是我们的班长。", "The classmate speaking is our class leader."), ("那个坐着的女孩是我妹妹。", "That girl sitting down is my little sister.")]),
    ("4. Numeral-measure word phrases", [("我们学校有一个医院。", "There’s a hospital in our school."), ("我们教室里有十多张书桌。", "There are over ten desks in our classroom.")]),
    ("5. Subject-predicate phrases", [("你们住的房子有多大？", "How big is the house you live in?"), ("这是学生们吃饭的食堂。", "This is the cafeteria where students eat.")]),
    ("6. Verb-object phrases", [("教中文的老师都是中国人。", "The teachers who teach Chinese are all Chinese."), ("穿红衣服的女孩是我姐姐。", "The girl wearing red is my big sister.")]),
    ("7. Prepositional phrases", [("在我家的客厅里有一个书架。", "There’s a bookshelf in my living room."), ("在学校的后面有一个体育馆。", "There’s a gym behind the school.")]),
    ("8. Positional words and phrases", [("山上的房子都很贵。", "Houses on the mountain are all very expensive."), ("左边的房间是客人房。", "The room on the left is a guest room.")]),
]
ATT2 = [("前边的教室", "the classroom at the front (前边 is the attributive)"), ("教室的前边", "the front of the classroom (前边 is the modified noun)"), ("穿红衣服的那个人是我姐姐。", "The person (who is) wearing red is my big sister."), ("这就是你想租的公寓。", "This is the apartment that you would like to rent.")]
NODE = [("车库", "garage"), ("皮鞋", "leather shoes"), ("饭桌", "dining table"), ("你妈妈", "your mom"), ("我哥哥", "my older brother"), ("她妹妹", "her younger sister"), ("白衬衫", "white shirt"), ("大楼", "big building"), ("快餐", "fast food"), ("一件夹克", "a jacket"), ("两条领带", "two ties"), ("三双筷子", "three pairs of chopsticks")]
OPT = [("我们的学校", "our school"), ("我们学校", "our school"), ("他们的班", "their class"), ("他们班", "their class"), ("很多的人", "a lot of people"), ("很多人", "a lot of people"), ("不少的问题", "quite a few problems"), ("不少问题", "quite a few problems")]
L3 = lesson(
    "Lesson 10 Presentation 2 grammar: the attributive (定语) and 的",
    "我租的公寓 · 穿红衣服的女孩 · 左边的房间 · 的 is not used / optional",
    requires=[],
    cards=[
        card("The attributive",
             "An attributive is a notional word or phrase that directly precedes the noun it modifies. It is often, but not always, linked to the noun by the structural particle 的. The book’s eight types, with two examples each:",
             examples=[D(z, e) for _, xs in ATT for z, e in xs]),
        card("The attributive always comes first",
             "A Chinese attributive, whether a single word or a long phrase, must always precede the noun it modifies. Reversing the order will change both structure and meaning. In contrast, longer English attributives follow the modified part, often via a relative clause. As shown, the structural particle 的 is often used to link an attributive to the noun it modifies.",
             examples=[D(z, e) for z, e in ATT2]),
        card("When 的 is not used and when it is optional",
             "的 is not used with: nouns denoting the quality of a person or thing (车库, 皮鞋, 饭桌); pronouns indicating familial relationship (你妈妈, 我哥哥, 她妹妹); monosyllabic adjectives (白衬衫, 大楼, 快餐); numeral-measure word phrases (一件夹克, 两条领带, 三双筷子). 的 is optional with disyllabic pronouns modifying collective nouns (我们（的）学校, 他们（的）班) and with 很多, 不少 and the like (很多（的）人, 不少（的）问题).",
             tables=[wtable(rows_py(NODE), title="的 is not used"), table(["With 的", "Without 的", "English"], [("我们的学校", "我们学校", "our school"), ("他们的班", "他们班", "their class"), ("很多的人", "很多人", "a lot of people"), ("不少的问题", "不少问题", "quite a few problems")], say=[0, 1], title="的 is optional")]),
    ],
    exercises=[
        M("What is an attributive?", "A word or phrase that directly precedes the noun it modifies", ["A word that follows the noun", "A verb of speech", "A measure word"], "定语 precedes the noun."),
        M("Which particle often links an attributive to its noun?", "的", ["了", "吗", "着"], "的 is the structural particle."),
        M("What does 前边的教室 mean?", "The classroom at the front", ["The front of the classroom", "The front classroom is mine", "In front of the room"], "前边 is the attributive."),
        M("What does 教室的前边 mean?", "The front of the classroom", ["The classroom at the front", "The classroom is in front", "Before class"], "前边 is the modified noun."),
        M("Which sentence has a verb-object phrase as attributive?", "穿红衣服的女孩是我姐姐。", ["这是我的书。", "山上的房子都很贵。", "我们学校有一个医院。"], "穿红衣服: verb-object."),
        M("Which sentence has a positional word as attributive?", "左边的房间是客人房。", ["这是我的书。", "说话的那个同学是班长。", "教中文的老师是中国人。"], "左边: position word."),
        M("Which sentence has a subject-predicate phrase as attributive?", "你们住的房子有多大？", ["那间大房间是我父母的卧室。", "那是学校图书馆的书。", "山上的房子都很贵。"], "你们住: subject + predicate."),
        M("Which phrase correctly omits 的?", "我哥哥", ["我的哥哥们的", "白的衬衫的", "车库的"], "Familial pronoun phrases omit 的."),
        M("Which phrase correctly omits 的 after a monosyllabic adjective?", "白衬衫", ["白的衬衫了", "衬衫白的", "衬衫的白"], "Monosyllabic adjectives omit 的."),
        M("Which is optional?", "我们(的)学校", ["一件(的)夹克", "你(的)妈妈", "大(的)楼"], "Disyllabic pronoun + collective noun."),
        F("这是我___书，不是图书馆的书。", "的", PART, "的 links the attributive."),
        F("你们住___房子有多大？", "的", PART, "你们住的房子."),
        F("穿红衣服___女孩是我姐姐。", "的", PART, "Verb-object phrase + 的."),
    ],
)

# ------------------------------------------------------------------ 4. attributive practice, A是A可是
ACT = [("甲：书架上的那本书是你在北京买的那本吗？", "Is the book on the shelf the one you bought in Beijing?"), ("乙：不是。我在北京买的那本书在学校里。", "No. The book I bought in Beijing is at school."),
       ("甲：你做的糖醋鱼比我做的好吃。", "The sweet and sour fish you made is tastier than the one I made."), ("乙：哪里。大家都喜欢吃你做的糖醋鱼。", "Not at all. Everyone likes to eat the sweet and sour fish you make."),
       ("甲：你在网上认识的女朋友是中国人吗？", "Is the girlfriend you met online Chinese?"), ("乙：不是。我在网上认识的女朋友是韩国人。", "No. The girlfriend I met online is Korean."),
       ("甲：你现在习惯在蒙特雷的学习和生活了吗？", "Have you gotten used to studying and living in Monterey now?"), ("乙：习惯了。我现在适应了每天很忙的生活。", "Yes. I’ve now adapted to a life that is busy every day."),
       ("甲：你上个星期穿的那件蓝衬衫很好看。", "The blue shirt you wore last week looked very nice."), ("乙：那是一个学中文的美国朋友给我买的。", "An American friend who studies Chinese bought it for me.")]
SHI = [("小是小了点，可是厨具很全，冰箱、洗碗机都有。", "It is a bit small, but it has a full array of kitchenware, a refrigerator and a dishwasher."), ("这道菜好吃是好吃，可是有点儿辣。", "This dish is delicious alright, but it’s a bit spicy."), ("这件衣服好看是好看，可是有点儿贵。", "Sure, this item of clothing looks nice, but it’s a bit expensive.")]
SHI2 = [("甲：这件衣服真好看。", "This piece of clothing is really nice."), ("乙：这件衣服好看是好看，可是有点儿贵。", "It looks nice alright, but it’s a bit expensive.")]
SHI3 = [("这个房间大是大，可是有点儿旧。", "This room is big, but a bit old."), ("这个沙发漂亮是漂亮，可是不太舒服。", "This sofa is pretty, but not very comfortable."), ("这个公寓便宜是便宜，可是离学校很远。", "This apartment is cheap, but far from school.")]
L4 = lesson(
    "Lesson 10 Presentation 2: attributive practice and 小是小了点，可是…",
    "你做的糖醋鱼 · 我在网上认识的女朋友 · A是A，可是…",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): the attributives",
             "Pair up. Highlight the attributives in each sentence. Read the dialog aloud together, each reading one part, then translate it in the space provided. The five dialogs, with 甲 and 乙 for the book’s A and B. The attributives are 书架上的, 你在北京买的, 我在北京买的, 你做的, 我做的, 你在网上认识的, 我在网上认识的, 每天很忙的, 你上个星期穿的 and 一个学中文的美国朋友给我买的 (mine):",
             examples=[D(z, e) for z, e in ACT]),
        card("Activity 2 (Listening and Writing)",
             "Listen to a conversation and translate the five sentences with attributive constructions into English; then share your work with a partner (audio, not included)."),
        card("The construction 小是小了点，可是…",
             "The construction …是…，可是… occurs most often in conversation. The first part, …是…, agrees with what someone has given their opinion on, while the second part, 可是…, qualifies that opinion with an alternative view or perspective. Pattern: A 是 A，可是….",
             examples=[D(z, e) for z, e in SHI]),
        card("Activity 3 (Speaking and Writing)",
             "Pair up and make sentences with A 是 A，可是…. One student comments on each of twelve pictures with the first part (A 是 A), then the other student qualifies the comment with the second part (可是…). Write both parts of your completed sentences in the table. Take turns on each picture so that both of you create both parts, for a total of 12 sentences. (The pictures are not included.) The book’s example, and three more of my own:",
             examples=[D(z, e) for z, e in SHI2] + [D(z, e) for z, e in SHI3]),
    ],
    exercises=[
        M("What does 书架上的那本书是你在北京买的那本吗？ ask?", "Is the book on the shelf the one you bought in Beijing?", ["Where is the book?", "Did you buy a book?", "Is the bookshelf in Beijing?"], "你在北京买的: attributive."),
        M("Which is the attributive in 我在网上认识的女朋友？", "我在网上认识的", ["女朋友", "我", "网上"], "Everything before 的."),
        M("What does 我现在适应了每天很忙的生活 mean?", "I’ve adapted to a life that is busy every day", ["I am too busy to live", "I like to be busy", "I live every day"], "每天很忙的生活."),
        M("What does 你做的糖醋鱼比我做的好吃 mean?", "The fish you made is tastier than the one I made", ["I made the fish you ate", "You are tastier than I", "The fish is sweet and sour"], "你做的 vs 我做的."),
        M("What does the 是…，可是… construction do?", "Agrees, then qualifies with a different view", ["Gives a cause and a result", "Gives a condition", "Gives a comparison"], "A 是 A，可是…"),
        M("What does 小是小了点，可是厨具很全 mean?", "It is a bit small, but the kitchenware is complete", ["It is small, so the kitchenware is complete", "It is not small", "It is small because it is cheap"], "A是A，可是…"),
        M("What does 这道菜好吃是好吃，可是有点儿辣 mean?", "This dish is delicious alright, but a bit spicy", ["This dish is spicy so it is tasty", "This dish is not tasty", "This dish is delicious and spicy"], "好吃是好吃，可是…"),
        M("Which sentence is a correct A是A，可是…?", "这件衣服好看是好看，可是有点儿贵。", ["这件衣服好看，是可是有点儿贵。", "这件衣服是好看是，可是贵。", "这件衣服好看可是是好看贵。"], "A 是 A，可是…"),
        F("小是小了点，___是厨具很全。", "可", PART, "可是: but."),
        F("这件衣服好看___好看，可是有点儿贵。", "是", PART, "好看是好看."),
        F("这是你在北京买___那本书吗？", "的", PART, "你在北京买的那本书."),
        F("我在网上认识___女朋友是韩国人。", "的", PART, "我在网上认识的女朋友."),
    ],
)

# ------------------------------------------------------------------ 5. existential 有, 什么时候
YOU = [("房间里有一个书桌和一个书架。", "There is a desk and a bookshelf in the room."), ("我家的厨房里没有洗碗机。", "There is no dishwasher in my kitchen."), ("你的老家有没有大学？", "Is there a college in your hometown?")]
YOU_Q = [("甲：这个房间里有什么？", "What is in this room?"), ("乙：这个房间里有一个书桌和一个书架。", "There is a desk and a bookshelf in this room."),
         ("甲：你家客厅里有什么？", "What is in your living room?"), ("甲：冰箱里有没有水果？", "Is there any fruit in the refrigerator?"), ("甲：这个图书馆里有多少书？", "How many books are in this library?"), ("甲：这个饭馆有什么菜？", "What dishes does this restaurant have?"), ("甲：这个学校有多少老师和学生？", "How many teachers and students does this school have?")]
SHME = [("我很喜欢这个公寓。咱们什么时候可以签合同？", "I really like this apartment. When can we sign the contract?"), ("你明天什么时候锻炼身体？", "When are you going to work out tomorrow?"), ("琳达是什么时候开始学中文的？", "When did Linda start learning Chinese?")]
IQ = [("你每天什么时候起床？", "When do you get up every day?"), ("你每天什么时候去学校上课？", "When do you go to school for class every day?"), ("你每天什么时候锻炼身体？", "When do you work out every day?"), ("你什么时候开始学中文的？", "When did you start learning Chinese?"), ("你什么时候完全适应这里的生活？", "When will you fully adapt to life here?"), ("你什么时候有期末考试？", "When do you have your final exam?")]
L5 = lesson(
    "Lesson 10 Presentation 2 grammar: existential 有 and 什么时候",
    "房间里有一个书桌 · 厨房里没有洗碗机 · 你什么时候起床？",
    requires=[],
    cards=[
        card("The existential sentence with 有",
             "The verb 有 is also used in existential sentences, i.e., sentences that express the existence (or absence) of someone or something. In this case, 有 is similar to the English “there is/are”. Pattern: Place + 有 + Object.",
             examples=[D(z, e) for z, e in YOU]),
        card("Activity 4 (Reading and Speaking)",
             "Pair up. Take turns asking and answering the following questions. Then take turns asking and answering similar questions about your classroom and residence. The book’s example, then its five questions:",
             examples=[D(z, e) for z, e in YOU_Q]),
        card("The question word 什么时候",
             "Similar to the English word “when”, 什么时候 is used to ask questions about time. Whereas English question words must come at the beginning of the sentence, Chinese question words simply take the syntactic place of the item being asked about; no sentence rearrangement is needed. Pattern: Subject + 什么时候 + Predicate?",
             examples=[D(z, e) for z, e in SHME]),
        card("Activity 5 (Reading, Speaking and Writing)",
             "Interview two classmates about their daily life and studies. Write down their responses in a table (Interviewee 1 and Interviewee 2) and report your interview results to the class. The example questions:",
             examples=[D(z, e) for z, e in IQ]),
    ],
    exercises=[
        M("What does the existential 有 express?", "The existence or absence of someone or something", ["Possession only", "An action in the past", "A request"], "Place + 有 + object: there is/are."),
        M("What is the pattern of the existential 有?", "Place + 有 + object", ["Object + 有 + place", "有 + place + object", "Place + object + 有"], "房间里有一个书桌."),
        M("What does 房间里有一个书桌和一个书架 mean?", "There is a desk and a bookshelf in the room", ["I have a desk and a bookshelf", "The room is a desk", "A bookshelf is my room"], "Place + 有 + object."),
        M("What does 我家的厨房里没有洗碗机 mean?", "There is no dishwasher in my kitchen", ["My kitchen is a dishwasher", "I have a dishwasher", "My dishwasher is in the kitchen"], "没有: there isn’t."),
        M("Which asks if there is a college in your hometown?", "你的老家有没有大学？", ["你有没有老家的大学？", "大学有你的老家吗？", "你的大学老家有没有？"], "有没有."),
        M("What does 什么时候 mean?", "When", ["What", "Where", "How"], "Used to ask about time."),
        M("Where does 什么时候 go in Chinese?", "In the place of the time being asked about", ["Always at the start", "Always at the end", "Before the subject"], "No rearrangement needed."),
        M("Which sentence asks “When will you work out tomorrow?”", "你明天什么时候锻炼身体？", ["什么时候你明天锻炼身体？", "你锻炼身体明天什么时候？", "明天你锻炼身体什么？"], "Subject + 什么时候 + predicate."),
        M("What does 琳达是什么时候开始学中文的？ ask?", "When did Linda start learning Chinese?", ["What does Linda learn?", "Why does Linda learn Chinese?", "Who teaches Linda?"], "是…的 with 什么时候."),
        F("房间里___一个书桌和一个书架。", "有", PART, "有: there is."),
        F("我家的厨房里___有洗碗机。", "没", PART, "没有: there is no."),
        F("你每天什么___起床？", "时候", ["作业", "操场", "预习"], "什么时候: when."),
        F("冰箱里有___有水果？", "没", PART, "有没有."),
    ],
)

# ------------------------------------------------------------------ 6. 如果...就...
RG1 = [("如果没什么问题，下周一我们就可以签合同。", "If there are no problems, we can sign the contract next Monday."), ("如果天气不好，我们就不去海边散步。", "If the weather is no good, we won’t go walking at the beach.")]
RG2 = [("如果明天下雨，我们就不去爬山了。", "If it rains tomorrow, we won’t go hiking."), ("明天如果下雨，我们就不去爬山了。", "If it rains tomorrow, we won’t go hiking.")]
RG3 = [("明天天气不好，我们就不去海边野餐。", "If the weather is bad tomorrow, we won’t go picnic at the beach."), ("好吃你就多吃点儿。", "If it tastes good, eat some more.")]
RG_K = [("如果你不喜欢去看电影，我们就不去了。", "If you don’t like going to the movies, we won’t go."), ("如果你喜欢这件衣服的样式，你就去试衣间试试。", "If you like the style of this piece of clothing, go try it on in the fitting room."), ("如果你晚上不想做饭，我们就去一家中国饭馆吃饭。", "If you don’t feel like cooking in the evening, we’ll go to a Chinese restaurant to eat."),
        ("如果你觉得带现金很麻烦，你就用微信扫码付钱。", "If you think carrying cash is troublesome, pay by scanning a code with WeChat."), ("如果这个公寓没有停车位，我们就不租了。", "If this apartment has no parking space, we won’t rent it.")]
CART = [("如果你考了一百分，爸爸就高兴死了。", "If you get a hundred, Dad will be dead happy."), ("我还是想不及格吧，爸爸你可别死！", "I’d better fail instead; Dad, don’t you die!")]
L6 = lesson(
    "Lesson 10 Presentation 2 grammar: the conditional 如果…，就…",
    "如果没什么问题，就… · 明天如果下雨 · 好吃你就多吃点儿",
    requires=[],
    cards=[
        card("如果…，就… (A and B)",
             "A. The 如果…，就… construction indicates a conditional relationship between two clauses in a complex sentence. Like the English “if…then…”, 如果 indicates the supposed condition in the clause, while 就 indicates the result if that condition pertains. B. While a subject can come either before or after 如果, it can only come before 就: 如果 + Subject1…, Subject2 + 就…; Subject1 + 如果…, Subject2 + 就….",
             examples=[D(z, e) for z, e in RG1] + [D(z, e) for z, e in RG2]),
        card("如果 can be left out (C)",
             "Colloquially, 如果 can be left out: …，就….",
             examples=[D(z, e) for z, e in RG3]),
        card("Activity 6 (Reading, Writing and Speaking)",
             "A. Pair up. Take turns reading the clauses on the left aloud as you link them to the relevant clauses on the right with 如果…，就…, then write the complete sentences. Left: 你不喜欢去看电影, 你喜欢这件衣服的样式, 你晚上不想做饭, 你觉得带现金很麻烦, 这个公寓没有停车位. Right: 你去试衣间试试, 我们不租了, 你用微信扫码付钱, 我们不去了, 我们去一家中国饭馆吃饭. B. Read a sentence aloud while your partner translates it into English; take turns until you have done all five. A possible matching (the key is mine):",
             examples=[D(z, e) for z, e in RG_K]),
        card("Activity 7 (Reading): a cartoon, and Activity 8: a song",
             "开心一刻！ Read the cartoon’s captions aloud in pairs, then translate them (the cartoon is not included). Activity 8 (Reading and Speaking): the book has the children’s song “If You’re Happy Clap Your Hands” (如果开心你就跟我拍拍手) with the Chinese words, pinyin and English; you sing along while noting its use of 如果…，就…. It has four verses — clapping, stomping, shouting “Wonderful!”, and doing all three — and every verse is built on 如果(感到)开心你就跟我…. The song’s words are not copied here.",
             examples=[D(z, e) for z, e in CART]),
    ],
    exercises=[
        M("What does 如果…，就… express?", "A condition and its result", ["A cause and an effect that already happened", "A contrast", "A choice"], "if…then…"),
        M("Which of the two words indicates the result?", "就", ["如果", "Both", "Neither"], "如果 gives the condition, 就 the result."),
        M("Where can the subject of the first clause go?", "Before or after 如果", ["Only before 如果", "Only after 如果", "Only before 就"], "如果明天下雨 / 明天如果下雨."),
        M("Where can the second subject go?", "Only before 就", ["Only after 就", "Before or after 就", "Only at the end"], "Subject2 + 就…"),
        M("What does 如果天气不好，我们就不去海边散步 mean?", "If the weather is bad, we won’t walk at the beach", ["We walk at the beach because it’s bad", "The weather is good", "We walk when it rains"], "如果…，就…"),
        M("What does 好吃你就多吃点儿 mean?", "If it tastes good, eat some more", ["It tastes bad", "Eat less", "You are eating a lot"], "如果 omitted."),
        M("Which sentence is correct?", "明天如果下雨，我们就不去爬山了。", ["如果明天下雨，就我们不去爬山了。", "明天如果下雨，就我们不去爬山了。", "我们如果就明天下雨不去爬山了。"], "就 follows the subject."),
        M("Which is the best match for 你不喜欢去看电影，…?", "我们就不去了。", ["你就去试衣间试试。", "你就用微信扫码付钱。", "我们就不租了。"], "Sensible pairing."),
        M("Which is the best match for 这个公寓没有停车位，…?", "我们就不租了。", ["你就去试衣间试试。", "你就用微信扫码付钱。", "我们就去中国饭馆吃饭。"], "Sensible pairing."),
        F("___果没什么问题，下周一我们就可以签合同。", "如", PART, "如果: if."),
        F("如果明天下雨，我们___不去爬山了。", "就", PART, "就 introduces the result."),
        F("明天___果下雨，我们就不去爬山了。", "如", PART, "Subject + 如果."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
PASS_B = "今天上午，我的老同学带我一起去看我想租的公寓。这是一个两室一厅的房子，看起来非常新。客厅挺大的，能有三十多平米，还带了一个双人沙发和一个新的地毯。厨房有一些厨具，不是很全，有一个冰箱，一个微波炉和一个洗碗机。饭厅不太大，也没有家具。不过这不是很大的问题，因为我就一个人住在这里。平时我也不太喜欢做饭，常常去饭馆吃。我看了一下卧室，觉得挺好的，主卧室很大，卫生间也很大。另一个卧室不太大，可以作客人房，也可以作书房。两个卧室都没有家具。公寓的环境很安全，而且交通也方便，我们都很喜欢，最后，我和王经理签了合同，也付了一个月的房租和押金。王经理给了我公寓的钥匙。这个周末，我得去商店买很多东西，然后准备搬家。"
PASS_BE = "This morning my old classmate took me to see the apartment I want to rent. It is a two-bedroom, one-living-room place and looks very new. The living room is quite big, about thirty-odd square meters, and comes with a double sofa and a new carpet. The kitchen has some kitchenware, not complete, with a refrigerator, a microwave and a dishwasher. The dining room is not very big and has no furniture. But this is not a big problem, because I live here by myself. I don’t much like cooking anyway and often eat out. I had a look at the bedrooms and thought they were quite good: the master bedroom is big and the bathroom is big too. The other bedroom is not very big and can be a guest room or a study. Neither bedroom has furniture. The apartment’s environment is very safe and transportation is also convenient; we both like it. In the end, I signed the contract with Manager Wang and also paid a month’s rent and deposit. Manager Wang gave me the apartment key. This weekend I have to go to the stores to buy a lot of things, and then get ready to move."
APPL = [("烤箱", "kao3 xiang1", "oven"), ("微波炉", "wei1 bo1 lu2", "microwave"), ("抽油烟机", "chou1 you2 yan1 ji1", "kitchen fan"), ("面包机", "mian4 bao1 ji1", "toaster"), ("搅拌器", "jiao3 ban4 qi4", "blender"), ("滤水器", "lv4 shui3 qi4", "water filter")]
L7 = lesson(
    "Lesson 10 Presentation 2 skill integration: signing the contract, kitchen appliances",
    "签了合同 · 钥匙 · 搬家 · 微波炉 烤箱 抽油烟机 · 在中国住过的地方",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading and Speaking)",
             "New words (生词): 微波炉 wēibōlú microwave; 钥匙 yàoshi key; 搬家 bānjiā move (residence). A. Listen to the monolog and write a summary (audio, not included). B. Read the passage and answer: 1. What are the advantages of this apartment? 2. What are the disadvantages? 3. What items is the speaker likely to buy this weekend? C. Compare your answers with a partner. D. In Chinese, tell your partner about your experiences looking for houses, apartments or dorms, including a description of those housing options. From the passage: advantages are the new look, the big living room, the safe environment and convenient transportation; disadvantages are the kitchenware that is not complete and no furniture in the dining room and the two bedrooms; this weekend he will probably buy furniture, bedding and kitchen things.",
             examples=[D(PASS_B, PASS_BE)]),
        card("Activity 2 (Listening and Speaking): a video about Rhymee Yao",
             "A. Watch a video about Rhymee Yao and write a summary (video, not included). B. Watch again and answer: 1. What furniture does her dorm room have? 2. What appliances does the kitchen have? 3. What is one thing she dislikes about her dorm room? C. Pair up and discuss your likes and dislikes about the dorm room, writing your lists in the table (最喜欢的地方, 最不喜欢的地方). D. Report your lists to the class. The new words:",
             tables=[wtable(APPL, title="生词")]),
        card("Activity 3 (Listening, Writing and Speaking)",
             "You meet three Chinese MIIS students at a café talking about the places they have lived in China. A. Listen and write the name of each student in pinyin or characters under the picture that matches the place they describe (audio and pictures, not included). B. Describe your current accommodations in pinyin or Chinese characters. C. Do your best not to consult your written description as you describe these accommodations to a partner."),
    ],
    exercises=[
        M("Who took the speaker to see the apartment?", "His old classmate", ["Manager Wang", "His mother", "A friend from work"], "我的老同学带我一起去看。"),
        M("How big is the living room?", "Thirty-odd square meters", ["Three square meters", "Three hundred square meters", "Thirteen square meters"], "能有三十多平米。"),
        M("What does the living room come with?", "A double sofa and a new carpet", ["A table and chairs", "A TV and a desk", "A bed"], "一个双人沙发和一个新的地毯。"),
        M("Which kitchen appliances does the apartment have?", "A refrigerator, a microwave and a dishwasher", ["An oven and a toaster", "A blender only", "A water filter and an oven"], "一个冰箱，一个微波炉和一个洗碗机。"),
        M("Why is the empty dining room not a big problem?", "He lives alone and does not often cook", ["He eats out and has a big family", "He will buy furniture tomorrow", "It is very small"], "我就一个人住在这里。平时我也不太喜欢做饭。"),
        M("What can the second bedroom be used as?", "A guest room or a study", ["A kitchen", "A garage", "A dining room"], "可以作客人房，也可以作书房。"),
        M("What did he pay when signing?", "A month’s rent and deposit", ["A year’s rent", "Nothing", "Only the deposit"], "付了一个月的房租和押金。"),
        M("What did 王经理 give him?", "The key", ["A contract copy only", "A sofa", "A parking pass"], "给了我公寓的钥匙。"),
        M("What will he do this weekend?", "Buy many things and get ready to move", ["Sign the contract", "Cook dinner", "Visit the manager"], "得去商店买很多东西，然后准备搬家。"),
        mean("微波炉", "wei1 bo1 lu2", "microwave", ["oven", "toaster", "blender"]),
        mean("烤箱", "kao3 xiang1", "oven", ["microwave", "toaster", "water filter"]),
        mean("搬家", "ban1 jia1", "move (residence)", ["key", "dishwasher", "sofa"]),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
L8 = lesson(
    "Lesson 10 Presentation 2 using Chinese in context: a roommate, a news story, a house in Las Vegas",
    "…好像… · 小是小，可是… · 麻雀虽小，五脏俱全",
    requires=[],
    cards=[
        card("Activity 1 (Writing and Speaking)",
             "A. Imagine you are now studying at MIIS and want to find a Chinese roommate for the apartment you are renting. Draw a layout of the apartment in your notebook and label the rooms in Chinese. B. Pair up. Show the apartment to your prospective renter (your partner) and specify which areas will be shared. During the showing the renter comments on the apartment using …好像…, while you respond with the patterns …小是小，可是… and 如果…，就…. Conclude the conversation by scheduling a time to sign the contract. Switch roles and repeat."),
        card("Activity 2 (Listening, Writing and Speaking)",
             "A. Form two groups of three. You are studying Chinese at Taiwan Normal University in Taipei and your teacher assigns a group project on rental apartments in Taiwan. In your online research you find an interesting news story; watch the video and write a summary in English with these guides: 1. What exactly is this news item about? 2. What’s unique about the apartment featured in the story? 3. What are the advantages of this type of apartment? B. Discuss what the Chinese proverb 麻雀虽小，五脏俱全 (máquè suīxiǎo, wǔzàng jùquán: although a sparrow is tiny, it has all its vital organs) refers to in this news story. C. Prepare a presentation comparing standard apartments with this new kind of rental arrangement, listing their advantages and disadvantages in Chinese. D. Present your findings to the class in Chinese. (The video is not included.)",
             examples=[D("麻雀虽小，五脏俱全", "Although a sparrow is tiny, it has all its vital organs.")]),
        card("Activity 3 (Listening and Speaking)",
             "A. Your Chinese friend wants to buy a house in Las Vegas. They send you a Chinese real estate agent’s video tour of the house to get your opinion. Watch the clip and summarize it so you can better advise your friend. B. Pair up. Discuss the house with your Chinese friend (your partner) and explain what you like and dislike about it. Switch roles and repeat. (The video is not included.)"),
    ],
    exercises=[
        M("What does …好像… express?", "It seems…, it looks as if…", ["It is certain…", "It was…", "Please…"], "厨房好像小了一点儿。"),
        M("What does the proverb 麻雀虽小，五脏俱全 mean?", "Although small, it has everything it needs", ["Sparrows are tiny", "Small things are cheap", "Small birds are full"], "Although a sparrow is tiny, it has all its vital organs."),
        M("Which sentence qualifies a view with 可是?", "房间小是小，可是很干净。", ["房间小，所以很干净。", "房间不小，也很干净。", "房间如果小，就很干净。"], "A是A，可是…"),
        M("Which sentence uses 如果…，就…?", "如果你喜欢，我们就租。", ["你喜欢是喜欢，可是贵。", "这个公寓不但大，而且新。", "这个公寓好像很大。"], "如果…，就…"),
        M("Which sentence uses …好像…?", "厨房好像小了一点儿。", ["如果你喜欢，我们就租。", "这个公寓不但大，而且新。", "小是小了点，可是厨具很全。"], "好像: seems."),
        mean("麻雀", "ma2 que4", "sparrow", ["dishwasher", "contract", "carpet"]),
        mean("五脏俱全", "wu3 zang4 ju4 quan2", "has all its vital organs (complete in every part)", ["has a safe environment", "signs a contract", "is a very new room"]),
    ],
)

UNIT = unit("第十课 租房和住房 Presentation 2: touring the apartment", [L1, L2, L3, L4, L5, L6, L7, L8,
    vocab_lesson("Lesson 10 Presentation 2 vocabulary", "19 words from the book’s Presentation 2 list", "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)])
