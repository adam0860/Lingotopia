"""Unit 22: Lesson 8 (Chinese Food and Restaurants) Presentation 1, from the book's texts: the ordering dialog, measure words
for food and drink, 想 / 要, 再, (一)点儿, 给, the restaurant passages and the 41-word vocabulary list.
The listening activities, the pictures, the website menu and the fill-in forms are not included; the lessons say so."""
from zh_auto import *
from zh_l8_vocab import VOC1

PART = ["吗", "们", "呢"]
FOOD = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [
    ("服务员", "您好！您几位？", "Hello! How many are you?"),
    ("大卫", "两位。", "Two."),
    ("服务员", "好。这边请，坐这儿可以吗？", "Okay. This way please; is it all right to sit here?"),
    ("大卫", "可以。", "Yes."),
    ("服务员", "这是菜单。你们想喝点儿什么？", "Here is the menu. What would you like to drink?"),
    ("大卫", "我来一瓶啤酒。", "I’ll have a bottle of beer."),
    ("服务员", "您呢？", "And you?"),
    ("小文", "我要一杯橙汁。", "I want a glass of orange juice."),
    ("服务员", "这是你们的饮料，可以点菜了吗？", "Here are your drinks. Can you order now?"),
    ("大卫", "可以，你们有什么特色菜？", "Yes. What specialty dishes do you have?"),
    ("服务员", "我们的北京烤鸭最有特色，客人们都很喜欢。", "Our Beijing roast duck is the most distinctive; the guests all like it very much."),
    ("大卫", "那，我们来半只烤鸭，一个糖醋鱼。", "Then, let’s have half a roast duck and a sweet and sour fish."),
    ("小文", "再要一个西红柿炒鸡蛋吧。", "Let’s order a tomato and scrambled eggs as well."),
    ("服务员", "好。你们想要点儿什么主食？", "Okay. What staple food would you like?"),
    ("大卫", "两碗米饭，再来一盘饺子。", "Two bowls of rice, and a plate of dumplings too."),
    ("小文", "麻烦您给我们拿两双筷子。", "Could you please bring us two pairs of chopsticks?"),
    ("服务员", "好，请稍等。（五分钟后）", "Okay, a moment please. (Five minutes later)"),
    ("服务员", "这是你们的菜，请慢用。", "Here are your dishes; please enjoy."),
    ("大卫", "谢谢！", "Thank you!"),
]
L1 = lesson(
    "Presentation 1: ordering at a restaurant (dialog)",
    "您几位？ · 这边请 · 我来一瓶啤酒 · 请慢用",
    requires=[],
    cards=[
        card("Lesson 8 Chinese Food and Restaurants: objectives",
             "第八课 中国食品与餐馆. Upon completion of this lesson you will be able to: order food at a restaurant; reserve a table; describe dishes; narrate simple past events. To do this you must master: new words and phrases for these functions; formulaic expressions for eating at restaurants; the modal verbs 想, 会, 想要 and 不要; 要 as a notional verb; the preposition 给; the adverbs 再 and 才; the adverb 就 (2); 了 indicating a new event; 了 in sequential actions; the 一边…一边… construction; Verb + (一)点儿 and Verb + 一下; and the pivotal construction. Area Studies: Food in Chinese Culture."),
        card("Getting Started",
             "Pair up and discuss with your partner. A. Listen to an audio and identify the setting or environment (audio, not included). B. Have you ever eaten at a Chinese restaurant? What are your favorite dishes? C. Do you know how to say any Chinese foods or dishes in Chinese? D. Do you know any phrases to use when eating at a Chinese restaurant?"),
        card("Presentation 1: 大卫 and 小文 at a restaurant",
             "The book also prints this dialog in traditional characters (for example 服務員：你好，您幾位？).",
             examples=dlg(P1)),
        card("Activity 1 (Listening): global and detailed listening",
             "A. Listen to Presentation 1 once and answer: 1. Where does this conversation take place? 2. How many people are conversing, and what is their relationship? 3. What clues reveal the setting? B. Listen again: what are the five steps involved to be served at this restaurant? (The recording is not included. From the text: it takes place in a restaurant; a waiter and two diners, David and Xiao Wen, so three people; the clues are 菜单, 点菜, 特色菜, 筷子 and 请慢用. The five steps, my summary: 1 the waiter asks how many and seats them; 2 drinks are ordered; 3 the dishes are ordered; 4 the staple food and chopsticks are ordered; 5 they wait a few minutes and the food arrives.)"),
    ],
    exercises=[
        M("Where does the conversation take place?", "At a restaurant", ["At a school", "At a hotel desk", "At a market"], "菜单, 点菜 and 请慢用 all belong to a restaurant."),
        M("How many people sit at the table?", "Two: 大卫 and 小文", ["One", "Three", "Five"], "服务员 asks 您几位？ and 大卫 answers 两位。"),
        M("What does the waiter ask when the guests come in?", "您几位？ — How many are you?", ["你们想喝点儿什么？ — What would you like to drink?", "可以点菜了吗？ — Can you order now?", "请稍等。 — A moment, please."], "The first question counts the guests."),
        M("What does 大卫 order to drink?", "A bottle of beer", ["A cup of orange juice", "A cup of tea", "A glass of Coke"], "我来一瓶啤酒。"),
        M("What does 小文 order to drink?", "A cup of orange juice", ["A bottle of beer", "A bowl of soup", "A cup of tea"], "我要一杯橙汁。"),
        M("Which dish does the waiter recommend as the most distinctive?", "北京烤鸭 — Beijing roast duck", ["糖醋鱼 — sweet and sour fish", "饺子 — dumplings", "西红柿炒鸡蛋 — tomato and eggs"], "我们的北京烤鸭最有特色。"),
        M("How much duck do they order?", "Half a duck", ["A whole duck", "Two ducks", "A plate of duck"], "我们来半只烤鸭。"),
        M("What does 小文 suggest ordering in addition?", "西红柿炒鸡蛋 — tomato and scrambled eggs", ["饺子 — dumplings", "米饭 — rice", "鱼汤 — fish soup"], "再要一个西红柿炒鸡蛋吧。"),
        M("What staple food do they order?", "Two bowls of rice and a plate of dumplings", ["Two bowls of noodles", "One bowl of rice", "A plate of rice and a bowl of dumplings"], "两碗米饭，再来一盘饺子。"),
        M("What does 小文 ask the waiter to bring?", "Two pairs of chopsticks", ["Two cups of tea", "A menu", "A bottle of beer"], "麻烦您给我们拿两双筷子。"),
        F("服务员：您好！您几___？", "位", PART, "几位 is the polite way to ask how many people."),
        F("你们想喝点儿___？", "什么", ["作业", "操场", "预习"], "想喝点儿什么: what would you like to drink?"),
        mean("请慢用", "qing3 man4 yong4", "please enjoy (the meal)", ["this way please", "a moment please", "how many are you"]),
        mean("菜单", "cai4 dan1", "menu", ["staple food", "chopsticks", "beverage"]),
    ],
)

# ------------------------------------------------------------------ 2. measure words, menus, taking and placing an order
MEAS = [("一瓶啤酒", "a bottle of beer"), ("一杯橙汁", "a glass of orange juice"), ("半只烤鸭", "half a roast duck"), ("一个糖醋鱼", "a sweet and sour fish"),
        ("一个西红柿炒鸡蛋", "a tomato and scrambled eggs"), ("两碗米饭", "two bowls of rice"), ("一盘饺子", "a plate of dumplings"), ("两双筷子", "two pairs of chopsticks")]
NEWW = [("茶", "cha2", "tea"), ("猫", "mao1", "cat"), ("汤", "tang1", "soup"), ("酒", "jiu3", "liqueur, alcohol")]
MENU_WORDS = ["饮料", "米饭", "烤鸭", "橙汁", "啤酒", "西红柿炒鸡蛋", "糖醋鱼", "茶", "主食", "鱼汤", "饺子", "鸡蛋汤", "汤", "特色菜", "西红柿汤", "菜"]
MENU_EN = ["beverage", "rice", "roast duck", "orange juice", "beer", "tomato and scrambled eggs", "sweet and sour fish", "tea", "staple food", "fish soup", "dumplings", "egg drop soup", "soup", "specialty dish", "tomato soup", "dish"]
TAKE = [("你们想喝点儿什么？", "What would you like to drink?"), ("可以点菜了吗？", "Can you order now?"), ("你们想要点儿什么主食？", "What staple food would you like?")]
PLACE = [("我来一瓶啤酒。", "I’ll have a bottle of beer."), ("我要一杯橙汁。", "I want a glass of orange juice."), ("再要一个西红柿炒鸡蛋吧。", "Let’s order a tomato and scrambled eggs as well."), ("两碗米饭，再来一盘饺子。", "Two bowls of rice, and a plate of dumplings too.")]
DLG5 = [("服务员", "您好！您几位？", "Hello! How many are you?"), ("大卫", "我一个人。", "Just me."), ("服务员", "这边请，坐这儿可以吗？", "This way please; is it all right to sit here?"), ("大卫", "可以。", "Yes."),
        ("服务员", "您想喝点儿什么？", "What would you like to drink?"), ("大卫", "来一瓶啤酒吧。", "A bottle of beer, please."), ("服务员", "好的。您想点点儿什么菜？", "Okay. What dishes would you like to order?"),
        ("大卫", "一个鸡蛋汤，再来一个糖醋鱼。", "An egg drop soup, and a sweet and sour fish too."), ("服务员", "您想要点儿什么主食？", "What staple food would you like?"),
        ("大卫", "一碗米饭。麻烦你再给我拿一双筷子。", "A bowl of rice. Could you also bring me a pair of chopsticks?"), ("服务员", "好。请稍等。（五分钟以后）", "Okay. A moment, please. (Five minutes later)"),
        ("服务员", "这是您的菜，请慢用。", "Here are your dishes; please enjoy."), ("大卫", "谢谢。", "Thank you.")]
L2 = lesson(
    "Presentation 1 activities: measure words, the menu and taking an order",
    "瓶 杯 只 个 碗 盘 双 · 饮料 汤 菜 主食 · 想喝点儿什么？",
    requires=[],
    cards=[
        card("Activity 2: the measure words",
             "A. Highlight the measure words in the presentation: 瓶, 杯, 只, 个, 碗, 盘 and 双. B. Study the names of the items to see how they are related to their measure words (the book shows pictures of 碗, 盘子, 瓶子 and 杯子: the measure word is also the container). Are there similar measure words in English? (a bottle of, a cup of, a plate of …). C. Use numbers and measure words to add a caption to each of nine pictures, with the new words below (the pictures are not included).",
             tables=[wtable(rows_py([(m[0], m[1]) for m in MEAS]), title="Measure words in Presentation 1"), wtable([(h, p, e) for h, p, e in NEWW], title="New words")]),
        card("Activity 3: design a restaurant menu",
             "Work in pairs. Design a restaurant menu using the items listed below, sorting them into categories (饮料, 汤, 菜, 主食), and add other Chinese dishes you know. The items:",
             tables=[wtable(rows_py(list(zip(MENU_WORDS, MENU_EN))), title="Menu items")]),
        card("Activity 4: taking an order and placing an order",
             "A. Copy the sentences from Presentation 1 in which the waiter takes an order or the customer places an order. B. Highlight the verbs (想喝, 点菜, 想要, 来, 要, 再要, 再来). C. Pair up and, using your menu, role-play a waiter taking an order and write it into a form with four columns: 饮料, 菜, 汤, 主食.",
             examples=[D(z, e) for z, e in TAKE] + [D(z, e) for z, e in PLACE]),
        card("Activity 5: complete the dialog",
             "Complete the dialog with the phrases 请稍等, 这边请, 请慢用, 您几位 and 麻烦你; then perform it with a partner. The completed dialog (the key is mine, from the words in the book’s gaps):",
             examples=dlg(DLG5)),
    ],
    exercises=[
        M("Which measure word goes with 啤酒 in the dialog?", "瓶 (bottle)", ["杯 (cup)", "碗 (bowl)", "双 (pair)"], "一瓶啤酒: a bottle of beer."),
        M("Which measure word goes with 橙汁?", "杯 (cup, glass)", ["瓶 (bottle)", "盘 (plate)", "只 (animal)"], "一杯橙汁."),
        M("Which measure word goes with 米饭?", "碗 (bowl)", ["双 (pair)", "盘 (plate)", "瓶 (bottle)"], "两碗米饭."),
        M("Which measure word goes with 饺子?", "盘 (plate)", ["碗 (bowl)", "双 (pair)", "杯 (cup)"], "一盘饺子."),
        M("Which measure word goes with 筷子?", "双 (pair)", ["只 (animal)", "盘 (plate)", "瓶 (bottle)"], "两双筷子."),
        M("Which measure word goes with 烤鸭?", "只 (a whole or half duck)", ["双 (pair)", "杯 (cup)", "碗 (bowl)"], "半只烤鸭."),
        M("In which category does 鸡蛋汤 belong?", "汤 (soup)", ["饮料 (beverage)", "主食 (staple food)", "特色菜 (specialty dish)"], "鸡蛋汤 is a soup."),
        M("In which category does 橙汁 belong?", "饮料 (beverage)", ["汤 (soup)", "主食 (staple food)", "菜 (dish)"], "橙汁 is a drink."),
        M("In which category does 饺子 belong, as the dialog uses it?", "主食 (staple food)", ["饮料 (beverage)", "汤 (soup)", "特色菜 (specialty dish)"], "Waiter: 你们想要点儿什么主食？ — 两碗米饭，再来一盘饺子."),
        M("Which sentence is the waiter taking an order?", "你们想喝点儿什么？", ["我要一杯橙汁。", "我来一瓶啤酒。", "再要一个西红柿炒鸡蛋吧。"], "The waiter asks; the customer places the order."),
        M("Which sentence is the customer placing an order?", "我来一瓶啤酒。", ["可以点菜了吗？", "你们想喝点儿什么？", "你们想要点儿什么主食？"], "来 + measure word + item."),
        F("我要一___橙汁。", "杯", PART, "杯 is the measure word for a cup or glass."),
        F("两___米饭，再来一盘饺子。", "碗", PART, "碗 is the measure word for rice in a bowl."),
        F("麻烦您给我们拿两___筷子。", "双", PART, "双 is the measure word for things in pairs."),
        mean("茶", "cha2", "tea", ["cat", "soup", "liqueur"]),
        mean("汤", "tang1", "soup", ["tea", "cat", "liqueur"]),
    ],
)

# ------------------------------------------------------------------ 3. 想 + verb
XIANG = [("我想吃饺子。", "I would like to eat dumplings."), ("你们想喝点儿什么？", "What would you like to drink?"), ("你想点点儿什么主食？", "What staple food would you like to order?"),
         ("我不想起床。", "I don’t want to get up."), ("你想不想一起去看电影？", "Would you like to go see a movie together?"), ("你想去散步吗？", "Would you like to go for a walk?")]
YAO_XIANG = [("我要喝啤酒。", "I am going to drink some beer."), ("我想喝啤酒。", "I would like to have some beer, but I may or may not act on that.")]
DIALOG_Q = [("Dialog 1", "Who is going to see the movie?"), ("Dialog 2", "Who wants to have Chinese food?"), ("Dialog 3", "Who would like to go to China?"), ("Dialog 4", "What are they going to order?")]
L3 = lesson(
    "Presentation 1 grammar: the modal verb 想",
    "我想吃饺子 · 不想 · 想不想 · 要 against 想",
    requires=[],
    cards=[
        card("想 + Verb: would like to + verb",
             "In this usage, 想 is a modal verb. Subject + 想 + Verb [+ Object]. Negative: Subject + 不想 + Verb [+ Object]. Question: Subject + 想 + Verb [+ Object] + 吗, or Subject + 想不想 + Verb [+ Object]？",
             examples=[D(z, e) for z, e in XIANG]),
        card("要 and 想",
             "In Lesson 7 we learned the modal verb 要 + Verb pattern, for example 我要值班. While both 要 and 想 can express desire or intention, 要 is stronger in tone, implying a decision has already been made.",
             examples=[D(z, e) for z, e in YAO_XIANG]),
        card("Activity 1 (Listening)",
             "Listen to four short dialogs and answer: Dialog 1, who is going to see the movie? Dialog 2, who wants to have Chinese food? Dialog 3, who would like to go to China? Dialog 4, what are they going to order? (The recordings are not included; the patterns are practiced below.)"),
    ],
    exercises=[
        M("What does 我想吃饺子 mean?", "I would like to eat dumplings", ["I ate dumplings", "I am eating dumplings", "I cannot eat dumplings"], "想 + verb: would like to."),
        M("How do you say “I don’t want to get up”?", "我不想起床。", ["我想不起床。", "我没想起床。", "不我想起床。"], "不想 + verb."),
        M("Which sentence asks “Would you like to go for a walk?”", "你想去散步吗？", ["你想吗去散步？", "你想不去散步吗？", "你吗想去散步？"], "想 + verb + 吗."),
        M("Which is the correct “想不想” question?", "你想不想一起去看电影？", ["你想不想不一起去看电影？", "你不想想一起去看电影？", "你想一起不想去看电影？"], "Subject + 想不想 + verb."),
        M("Which sentence is stronger: a decision already made?", "我要喝啤酒。", ["我想喝啤酒。", "我不想喝啤酒。", "我可以喝啤酒。"], "要 is stronger than 想: I am going to drink beer."),
        M("What does 我想喝啤酒 imply?", "I would like some beer, but I may or may not act on it", ["I have decided to drink beer", "I drank beer already", "I don’t like beer"], "想 only expresses a wish."),
        M("How do you say “What would you like to drink?”", "你们想喝点儿什么？", ["你们想喝什么点儿？", "你们什么想喝点儿？", "你们想点儿喝什么？"], "想 + verb + 点儿 + 什么."),
        M("What does 你想点点儿什么主食 ask?", "What staple food would you like to order?", ["How many people eat?", "Where is the staple food?", "Who is the waiter?"], "点 here means to order."),
        F("我___想起床。", "不", ["也", "想", "再"], "不想 + verb: don’t want to."),
        F("你想去散步___？", "吗", ["们", "呢", "不想"], "Statement + 吗 makes a yes/no question."),
        F("你想___想一起去看电影？", "不", PART, "想不想 is the verb-not-verb question."),
        F("我想吃___。", "饺子", ["作业", "操场", "预习"], "The object of 吃 must be something to eat."),
        mean("想", "xiang3", "want to, would like to (modal)", ["to take", "to sit", "to order"]),
    ],
)

# ------------------------------------------------------------------ 4. 要 + noun
YAON = [("你想要什么饮料？", "What beverage would you like?"), ("我要一杯橙汁。", "I want a glass of orange juice."), ("你要什么主食？", "What staple food do you want?"), ("我要一盘饺子。", "I want a plate of dumplings."), ("你们想要饺子还是米饭？", "Do you want dumplings or rice?")]
MENU3 = [("汤", "豆腐汤 · 西红柿鸡蛋汤 · 酸辣汤 · 酸菜鱼汤"), ("特色菜", "糖醋鱼 · 麻婆豆腐 · 烤鸭 · 西红柿炒鸡蛋 · 豆腐鱼"), ("主食", "白米饭 · 蛋炒饭 · 水饺 · 牛肉炒面"), ("饮料", "啤酒 · 橙汁 · 绿茶 · 可乐")]
NEW3 = [("牛肉", "niu2 rou4", "beef"), ("可乐", "ke3 le4", "Coke"), ("面", "mian4", "noodles")]
ASK13 = [("你想学中文还是韩文？", "Do you want to study Chinese or Korean?"), ("你想学法文吗？", "Do you want to study French?"), ("你晚饭要吃什么？", "What are you going to eat for dinner?"), ("你要什么主食？", "What staple food do you want?"),
         ("我周末要去海边玩儿，你想一起去吗？", "I am going to the beach this weekend; would you like to come along?"), ("你想要几个孩子？", "How many children do you want?"), ("你要去看电影吗？", "Are you going to see a movie?"),
         ("你想做什么工作？", "What job would you like to do?"), ("你要茶还是啤酒？", "Do you want tea or beer?"), ("你想在电脑公司工作还是在医院工作？", "Would you like to work at a computer company or at a hospital?"),
         ("你想在加州上大学还是去德州上大学？", "Would you like to go to college in California or in Texas?"), ("你想什么时候去中国饭店？", "When would you like to go to a Chinese restaurant?"), ("你最想去哪个国家？", "Which country do you most want to go to?")]
L4 = lesson(
    "Presentation 1 grammar: 要 + noun, and menu questions",
    "你想要什么饮料？ · 我要一杯橙汁 · 美味家常菜 · 你想学中文还是韩文？",
    requires=[],
    cards=[
        card("要 + Noun",
             "To order food using 要, place 要 before the noun (object). In this case 要 is the main verb of the sentence. Subject + (Modal Verb) + 要 + Object.",
             examples=[D(z, e) for z, e in YAON]),
        card("Activity 2 (Listening)",
             "Listen to four sentences, translate them, and decide whether 要 serves as a modal or a main verb in each (the recordings are not included). Rule of thumb: 要 before a verb is modal (want to, am going to); 要 before a noun is the main verb (want, order)."),
        card("Activity 3: the menu 美味家常菜 (Tasty Home Cooking)",
             "Choose the food and drink you would like to order, then write questions to ask a partner what they would like to order, using the modal verbs 想 and 想要 and the main verb 要 wherever appropriate. New words: 牛肉 beef, 可乐 Coke, 面 noodles.",
             tables=[table(["Category", "Items"], [(a, b) for a, b in MENU3], title="美味家常菜"), wtable(NEW3, title="New words")]),
        card("Activity 4: thirteen questions with 想 and 要",
             "Choose three sentences from the following list to ask your partner.",
             examples=[D(z, e) for z, e in ASK13]),
    ],
    exercises=[
        M("In 我要一杯橙汁, is 要 a modal or a main verb?", "A main verb: it is followed by a noun", ["A modal verb: it is followed by a verb", "A measure word", "A question word"], "要 + noun: want, order."),
        M("In 我要去看电影, is 要 a modal or a main verb?", "A modal verb: it is followed by a verb", ["A main verb: it is followed by a noun", "A measure word", "An adjective"], "要 + verb: am going to."),
        M("What does 你想要什么饮料？ ask?", "What beverage would you like?", ["Where is the beverage?", "Who wants a beverage?", "How many beverages are there?"], "想要 + noun."),
        M("What does 你们想要饺子还是米饭？ ask?", "Would you like dumplings or rice?", ["Would you like dumplings and rice?", "Do you have dumplings?", "Where is the rice?"], "还是 offers a choice."),
        M("What does 你晚饭要吃什么？ ask?", "What are you going to eat for dinner?", ["Who cooks dinner?", "When is dinner?", "Where is dinner?"], "要 + verb: going to."),
        M("What does 你想学中文还是韩文？ ask?", "Do you want to study Chinese or Korean?", ["Do you speak Chinese and Korean?", "Where do you study?", "Who teaches Chinese?"], "还是 offers a choice."),
        M("Which sentence asks about a future decision?", "我周末要去海边玩儿。", ["我周末想去海边玩儿吗？", "我周末不想去海边。", "我周末去过海边。"], "要 + verb states a decision."),
        M("Which question asks about a wish for the future?", "你想要几个孩子？", ["你有几个孩子？", "你几岁？", "你在哪儿工作？"], "想要 + number + 个孩子: how many children do you want?"),
        M("What does 牛肉炒面 mean, from the menu?", "Stir-fried noodles with beef", ["Beef soup", "Fried rice with egg", "A plate of dumplings"], "牛肉 (beef) + 炒 (stir-fry) + 面 (noodles)."),
        M("Which item on the menu is a drink?", "可乐", ["蛋炒饭", "酸辣汤", "水饺"], "可乐 is Coke."),
        F("你想___什么饮料？", "要", ["再", "给", "放"], "想要 + noun: would like."),
        F("你要茶___啤酒？", "还是", ["也", "吗", "再"], "还是 joins the two choices of a question."),
        F("我周末要去海边玩儿，你想一起去___？", "吗", ["们", "呢", "不想"], "Yes/no question with 吗."),
        mean("可乐", "ke3 le4", "Coke", ["beef", "noodles", "tea"]),
        mean("牛肉", "niu2 rou4", "beef", ["Coke", "noodles", "soup"]),
    ],
)

# ------------------------------------------------------------------ 5. 再
ZAI = [("再要一个西红柿炒鸡蛋吧。", "Let’s order a tomato and scrambled eggs as well."), ("请给我两碗米饭，再来一盘饺子。", "Please give me two bowls of rice, and a plate of dumplings too."),
       ("我想再点一个糖醋鱼。", "I would like to order another sweet and sour fish."), ("服务员，请再给我们两双筷子。", "Waiter, please give us two more pairs of chopsticks.")]
L5 = lesson(
    "Presentation 1 grammar: the adverb 再",
    "再要一个… · 再来一盘… · 再给我们两双筷子",
    requires=[],
    cards=[
        card("Adverb 再",
             "While the meaning of the adverb 再 depends on context, in this lesson it means “in addition”. Pattern: 再 + Verb + Object.",
             examples=[D(z, e) for z, e in ZAI]),
        card("Activities 5 and 6",
             "Activity 5 (Listening): listen to three dialogs: What does the woman suggest? What do the speakers plan to order? (recordings not included). Activity 6 (Speaking): pair up, use your menu to role-play waiter and customer, and use 再 wherever appropriate; switch roles and repeat (the book shows two pictures of diners)."),
    ],
    exercises=[
        M("What does 再 mean in 再要一个西红柿炒鸡蛋吧?", "in addition, as well", ["never", "already", "at the same time"], "再 + verb + object: order one more."),
        M("What does 我想再点一个糖醋鱼 mean?", "I would like to order another sweet and sour fish", ["I do not want sweet and sour fish", "I ordered sweet and sour fish yesterday", "I can cook sweet and sour fish"], "再点: order in addition."),
        M("What does 请再给我们两双筷子 ask for?", "Two more pairs of chopsticks", ["Two bowls of rice", "Chopsticks for the waiter", "No chopsticks"], "再给: give in addition."),
        M("Where does 再 go in a sentence?", "Before the verb", ["After the object", "At the end", "Before the subject"], "再 + Verb + Object."),
        M("How do you say “Let’s order a plate of dumplings as well”?", "再要一盘饺子吧。", ["要再一盘饺子吧。", "要一盘饺子再吧。", "再一盘要饺子吧。"], "再 + 要 + number + measure word + noun."),
        M("How do you say “Please give me two more bowls of rice”?", "请再给我两碗米饭。", ["请给再我两碗米饭。", "请给我两碗米饭再。", "再请给两碗我米饭。"], "再 sits just before 给."),
        F("请给我两碗米饭，___来一盘饺子。", "再", ["也", "吗", "们"], "再 + verb: and also."),
        F("服务员，请___给我们两双筷子。", "再", ["也", "吗", "们"], "再给: give more."),
        mean("再", "zai4", "again; once more; and then; in addition", ["just, simply (emphasis)", "arrive", "take"]),
    ],
)

# ------------------------------------------------------------------ 6. (一)点儿
DIAN = [("我可以喝点儿酒吗？", "May I drink a little wine?"), ("吃点儿菜吧。", "Have some food."), ("再喝点儿啤酒！", "Have some more beer!"), ("你们想喝点儿什么？", "What would you like to drink?"), ("你们想要点儿什么主食？", "What staple food would you like?")]
DIAN_Q = [("你们想喝点儿什么？", "What would you like to drink?"), ("您想吃点儿什么？", "What would you like to eat?"), ("要不要再来点儿汤？", "Would you like some more soup?")]
DIAN_HOST = [("吃点儿菜吧。", "Have some food."), ("再喝点儿啤酒！", "Have some more beer!"), ("多吃点儿。", "Eat a little more.")]
L6 = lesson(
    "Presentation 1 grammar: Verb + (一)点儿 to soften the tone",
    "喝点儿 · 吃点儿菜吧 · 想要点儿什么主食 · 委婉语气",
    requires=[],
    cards=[
        card("Verb + (一)点儿 to soften the tone of voice (委婉语气)",
             "(一)点儿 usually means “a little bit”: 我喝了一点儿酒 (I drank a little wine). It is also used in imperative and request sentences to make a suggestion or request sound more tactful, polite or casual. The character 一 can be omitted. The noun that follows (一)点儿 can also be omitted when it is clear from context. Pattern: Verb + (一)点儿 + Noun.",
             examples=[D("我喝了一点儿酒。", "I drank a little wine.")] + [D(z, e) for z, e in DIAN]),
        card("Activity 7 (Speaking)",
             "A. In groups of three, think of questions containing (一)点儿 that a waiter or waitress might ask the diners. B. In the same group, think of things a host might say to a dinner guest containing (一)点儿. Share your work with the class. Some of mine (the book leaves the answer open):",
             examples=[D(z, e) for z, e in DIAN_Q] + [D(z, e) for z, e in DIAN_HOST]),
    ],
    exercises=[
        M("What does (一)点儿 usually mean in 我喝了一点儿酒?", "a little bit", ["a lot", "every day", "at once"], "我喝了一点儿酒: I drank a little wine."),
        M("What does (一)点儿 add in 吃点儿菜吧?", "It makes the suggestion sound polite and casual", ["It makes it a question", "It makes it negative", "It makes it past"], "Verb + 点儿 softens a request."),
        M("Which part can be omitted in (一)点儿?", "The character 一", ["The character 点", "The verb", "The subject always"], "吃点儿 = 吃一点儿."),
        M("What does 你们想喝点儿什么？ ask?", "What would you like to drink?", ["How much beer do you drink?", "Who wants to drink?", "Where do you drink?"], "A polite waiter’s question."),
        M("What does 再喝点儿啤酒！ mean?", "Have some more beer!", ["Don’t drink beer!", "I drank beer.", "Where is the beer?"], "再 + 喝 + 点儿 + noun."),
        M("What does 我可以喝点儿酒吗？ ask?", "May I drink a little wine?", ["Do you drink wine every day?", "Where is the wine?", "Who drinks wine?"], "可以 + verb + 点儿 + noun + 吗."),
        M("Where is the noun in Verb + (一)点儿 + Noun?", "After 点儿", ["Before the verb", "Before 点儿", "At the beginning"], "喝点儿酒: the noun follows 点儿."),
        M("Which is the more tactful request?", "吃点儿菜吧。", ["吃菜。", "你吃菜！", "吃了菜。"], "点儿 and 吧 soften the tone."),
        F("你们想要___什么主食？", "点儿", ["一下", "吗", "们"], "想要点儿什么 is the polite question."),
        F("吃点儿菜___。", "吧", ["吗", "们", "呢"], "吧 makes a friendly suggestion."),
        mean("点儿", "dian3r5", "a little; a bit", ["a pair", "a bowl", "a plate"]),
    ],
)

# ------------------------------------------------------------------ 7. 给
GEI = [("请给我一杯水。", "Please give me a cup of water."), ("王老师给我一本书。", "Teacher Wang gave me a book."), ("麻烦您给我们拿两双筷子。", "Could you please bring two pairs of chopsticks to us?")]
GEI2 = [("请给她来杯橙汁，给我来杯茶。", "Juice for her and tea for me, please."), ("我想给饭馆打电话。", "I want to call the restaurant."), ("他要我给他点个烤鱼。", "He wants me to order a grilled fish for him."),
        ("我给你们做个蛋炒饭吧。", "Let me cook some egg fried rice for you."), ("请给我拿一本英文菜单。", "Please give me an English menu.")]
GEI_SAY = [("快！给她拿一杯水。", "Quick! Bring her a cup of water."), ("请给他点一盘饺子。", "Please order a plate of dumplings for him."), ("你想让我给你做一杯咖啡吗？", "Do you want me to make you a cup of coffee?"),
           ("麻烦你给我炒点儿鸡蛋，好吗？", "Could you please fry me some eggs?"), ("给我打电话！", "Call me!"), ("他喜欢吃辣的，我给他点一个四川菜。", "He likes spicy food. I will order him a Sichuan dish.")]
L7 = lesson(
    "Presentation 1 grammar: 给 as a preposition",
    "麻烦您给我们拿… · 我想给饭馆打电话 · 给 + receiver + verb",
    requires=[],
    cards=[
        card("As a verb, 给 means “to give”; as a preposition it introduces the receiver",
             "As a verb 给 means to give: 请给我一杯水. In 麻烦您给我们拿两双筷子, 给 is a preposition that introduces the receiver of the action, 给我们 (to us); (给 + receiver) often appears before a verb phrase. Pattern: Subject + (给 receiver) + VP.",
             examples=[D(z, e) for z, e in GEI]),
        card("More examples",
             "Activity 8: A. Pair up and highlight the (给 + object) in the sentences, then read them aloud in Chinese and in English.",
             examples=[D(z, e) for z, e in GEI2]),
        card("Activity 8B: how would you say these in Chinese?",
             "The book asks you to draft six sentences; one possible answer for each (the key is mine):",
             examples=[D(z, e) for z, e in GEI_SAY]),
    ],
    exercises=[
        M("What does 给 mean in 请给我一杯水?", "give (a verb)", ["to (a preposition)", "wait", "order"], "给我一杯水: give me a cup of water."),
        M("What does 给我们 mean in 麻烦您给我们拿两双筷子?", "for us (introducing the receiver)", ["we gave", "from us", "with us"], "给 + receiver is a preposition here."),
        M("Where does (给 + receiver) appear?", "Before a verb phrase", ["After the verb", "At the end of the sentence", "Before the subject"], "Subject + (给 receiver) + VP."),
        M("What does 我想给饭馆打电话 mean?", "I want to call the restaurant", ["I want to give the restaurant a phone", "The restaurant called me", "I want to eat at a restaurant"], "给饭馆打电话: make a call to the restaurant."),
        M("What does 我给你们做个蛋炒饭吧 mean?", "Let me cook some egg fried rice for you", ["You cook egg fried rice for me", "I ate egg fried rice", "I don’t want egg fried rice"], "给你们 + 做."),
        M("What does 请给我拿一本英文菜单 mean?", "Please bring me an English menu", ["Please read the English menu", "Please sell me a book", "Please order an English menu"], "拿 = take, bring."),
        M("How do you say “Call me!”", "给我打电话！", ["我给打电话！", "打给电话我！", "电话给我打了！"], "给 + receiver + verb phrase."),
        M("How do you say “Please order a plate of dumplings for him”?", "请给他点一盘饺子。", ["请点给他一盘饺子。", "请他给点饺子一盘。", "给请他点一盘饺子。"], "给他 comes before 点."),
        F("请___她来杯橙汁，给我来杯茶。", "给", ["再", "要", "放"], "给 introduces the receiver."),
        F("我想给饭馆___电话。", "打", ["拿", "做", "喝"], "打电话 means to make a phone call."),
        mean("给", "gei3", "for, for the benefit of (preposition); to give", ["again; and then", "arrive", "take"]),
    ],
)

# ------------------------------------------------------------------ 8. skill integration
MATCH8 = [("d", "有饺子吗？", "Do you have dumplings?"), ("a", "先来一只烤鸭吧。", "Let’s start with a roast duck."), ("b", "来一瓶啤酒和一杯可乐。", "A bottle of beer and a glass of Coke."), ("c", "十分钟就好。", "It will be ready in ten minutes."),
          ("e", "有五个人。", "There are five people."), ("f", "我们去长城饭店，怎么样？", "Shall we go to the Great Wall Restaurant?"), ("g", "请稍等一下。", "Please wait a moment."), ("h", "很好。", "Very good.")]
PASS1 = [("在我住的地方有一家小面馆。那家面馆太小了，只有一个人，他又是老板，又是服务员。不过，那里的饭菜都很好吃，最有特色的是牛肉面。我常常去那儿吃牛肉面。时间长了，老板看见我就问：“今天又吃牛肉面？”", "Where I live there is a small noodle restaurant. It is so small that there is only one person; he is both the owner and the waiter. But the food there is delicious; the most distinctive dish is beef noodles. I often go there to eat beef noodles. After a while, when the owner sees me, he asks: “Beef noodles again today?”"),
         ("马克在中国的一所大学教英文。学校有好几位外国老师。他们常常一起去饭馆吃饭。每次都是马克点菜，因为他在中国的时间最长，中文也最好。在中国，除了非常有名的大饭店，小饭店里的菜单都是中文，很多服务员也不会说英文。", "Mark teaches English at a university in China. The school has several foreign teachers. They often eat at restaurants together. Every time Mark orders, because he has been in China the longest and his Chinese is the best. In China, except for very famous big restaurants, the menus in small restaurants are in Chinese, and many waiters cannot speak English either."),
         ("中国人吃饭的习惯跟我们很不一样。在我们那儿每一个人点自己的菜，吃自己的菜，但是在中国，大家一起点菜，一起吃。不过中国和西方最不一样的是：西方最好的饭馆常常也是最贵的，在中国最好的饭馆常常都不贵。", "Chinese eating habits are very different from ours. Where we are, everyone orders their own dish and eats their own dish, but in China everyone orders together and eats together. But the biggest difference between China and the West is that the best restaurants in the West are often also the most expensive, while in China the best restaurants are often not expensive."),
         ("现在很多饭店都开始用点菜机。有一天，我和朋友一起去饭馆吃饭。我们点菜的时候，服务员在点菜机上不停地按。我的朋友说：“请不要在我们点菜的时候玩儿手机，好吗？！”", "Now many restaurants have begun to use order machines. One day I went to a restaurant with a friend. While we were ordering, the waiter kept pressing the order machine. My friend said: “Please don’t play with your cell phone while we are ordering, okay?!”")]
L8 = lesson(
    "Presentation 1 skill integration: orders and four passages about restaurants",
    "有饺子吗？ · 十分钟就好 · 小面馆 · 马克点菜 · 点菜机",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Reading): match the questions with the answers",
             "Listen to eight questions (audio, not included) and match each with its answer, a to h (shown here as 甲 to 辛, in the book’s order). The eight answers:",
             examples=[D(f"{dict(zip('abcdefgh', '甲乙丙丁戊己庚辛'))[k]}．{z}", e) for k, z, e in sorted(MATCH8)]),
        card("Activity 2 (Reading and Listening): four passages",
             "Pair up. Student A reads Passages 1 and 2 and answers the questions; Student B reads Passages 3 and 4. Then each listens to the partner’s passages (audio, not included) and answers the same questions; compare all four. The questions: Passage 1: What does the speaker say about the restaurant? Passage 2: How do the teachers order their dishes and why? Passage 3: What differences between Chinese and Westerners are mentioned? Passage 4: What would the waiter’s likely response to the diner’s comment be? (New word: 按 àn, push or press.)",
             examples=[D(z, e) for z, e in PASS1]),
        card("Activity 3 (Listening, Reading, Writing and Speaking)",
             "A. In groups of three, group 1 listens to Passage 1 and group 2 to Passage 2 (audio, not included) and each student fills in a table with the columns 客人, 饮料, 汤, 菜, 主食 and Special Requests. B. One student from each group acts as waiter or waitress and the other group are the customers; act out your passages from memory, with the customary courtesies and formulaic expressions."),
    ],
    exercises=[
        M("Which of the eight answers is itself a question for the waiter?", "有饺子吗？ — Do you have dumplings?", ["很好。", "十分钟就好。", "有五个人。"], "d (丁). 有饺子吗？ is a question; the others are statements."),
        M("Which answer fits “How many are you?”", "有五个人。", ["很好。", "请稍等一下。", "来一瓶啤酒和一杯可乐。"], "几位？ asks for the number of people."),
        M("Which answer fits “What would you like to drink?”", "来一瓶啤酒和一杯可乐。", ["有五个人。", "十分钟就好。", "很好。"], "An order of drinks."),
        M("Which answer fits “How long will the food take?”", "十分钟就好。", ["有五个人。", "很好。", "有饺子吗？"], "就 shows the time is short."),
        M("Which answer fits “Shall we go to the Great Wall Restaurant?”", "很好。 — Fine.", ["有五个人。", "十分钟就好。", "请稍等一下。"], "怎么样？ asks for an opinion."),
        M("Passage 1: why is the small noodle restaurant special?", "The owner is both owner and waiter; beef noodles are the specialty", ["It has many waiters", "It only serves rice", "It is very big"], "他又是老板，又是服务员。最有特色的是牛肉面。"),
        M("Passage 1: what does the owner say when he sees the speaker?", "今天又吃牛肉面？ — Beef noodles again today?", ["您几位？", "请慢用。", "再见。"], "The speaker comes so often."),
        M("Passage 2: who orders for the foreign teachers, and why?", "Mark, because he has been in China the longest and his Chinese is the best", ["The waiter, because he speaks English", "The oldest teacher", "Nobody orders"], "每次都是马克点菜."),
        M("Passage 2: in what language are the menus in small restaurants?", "Chinese", ["English", "French", "Only pictures"], "小饭店里的菜单都是中文."),
        M("Passage 3: how do Chinese people order compared with Westerners?", "Everyone orders together and eats together", ["Everyone orders their own dish", "Only the host orders", "The waiter decides"], "在中国，大家一起点菜，一起吃."),
        M("Passage 3: what is the biggest difference mentioned?", "In China the best restaurants are often not expensive", ["Chinese food is spicier", "Chinese restaurants are smaller", "Westerners eat later"], "中国最好的饭馆常常都不贵."),
        M("Passage 4: what was the waiter doing?", "Pressing on the order machine while they ordered", ["Playing a video game", "Cooking", "Writing the order by hand"], "服务员在点菜机上不停地按."),
        M("Passage 4: what does the friend say?", "Please don’t play with your cell phone while we are ordering", ["Please bring the menu", "Please wait a moment", "Please sit here"], "请不要在我们点菜的时候玩儿手机，好吗？！"),
        F("时间长了，老板看见我就问：“今天___吃牛肉面？”", "又", PART, "又 here means “again”."),
        F("他___是老板，又是服务员。", "又", PART, "又…又… joins the two roles."),
    ],
)

# ------------------------------------------------------------------ 9. using Chinese in context
SITU = [("这个菜辣不辣？", "You want to know if the dish is spicy: Is this dish spicy?"), ("我想试一下筷子。", "You want to try chopsticks: I would like to try chopsticks."), ("你们今天的特色菜是什么？", "You want to know what today’s special is: What is your special today?"),
        ("你们有啤酒吗？", "You want to know if they have beer: Do you have beer?"), ("我要三小碗米饭，一盘饺子。", "You want to order three small bowls of rice and a plate of dumplings: I want three small bowls of rice and a plate of dumplings."),
        ("一盘饺子有几个？", "You want to know how many dumplings per plate: How many dumplings are on a plate?"), ("只有四个？那我要三盘。", "The waiter says there are only four, so you order three plates: Only four? Then I’ll have three plates."), ("我要一杯可乐。", "You want to order a glass of Coke: I want a glass of Coke.")]
DISHES = [("蚂蚁上树", "ma3 yi3 shang4 shu4", "Ants on a Tree"), ("全家福", "quan2 jia1 fu2", "Happy Family"), ("松鼠鱼", "song1 shu3 yu2", "Squirrel Fish"), ("罗汉斋", "luo2 han4 zhai1", "Buddha’s Delight"),
          ("小白龙过江", "xiao3 bai2 long2 guo4 jiang1", "Little White Dragon Crosses the River"), ("鱼香肉丝", "yu2 xiang1 rou4 si1", "Fish-Flavored Pork Slices"), ("红烧狮子头", "hong2 shao1 shi1 zi5 tou2", "Soy Sauce-Braised Lion’s Head")]
LUNCH = [("菜", "鱼香牛肉 · 糖醋虾 · 烤鸭"), ("汤", "鱼头汤 · 酸辣汤 · 蛋花汤"), ("主食", "米饭 · 饺子 · 炒面"), ("饮料", "青岛啤酒 · 橙汁 · 可乐")]
L9 = lesson(
    "Presentation 1: using Chinese in context (situations, lunch and dish names)",
    "你们有啤酒吗？ · 午餐自由组合 · 蚂蚁上树 · 全家福",
    requires=[],
    cards=[
        card("Activity 1 (Speaking): what should you say?",
             "The book gives eight situations in English and asks what you should say. One possible Chinese for each (the key is mine):",
             examples=[D(z, e) for z, e in SITU]),
        card("Activity 2: a fast-food lunch combination, 午餐自由组合",
             "Fast food delivery is very popular in China. Choose your lunch combination by checking the items on the menu: one dish, one soup, one staple food and one drink (一菜一汤 + 一个主食 + 一个饮料). B. Ask a partner in Chinese what they would like from each category.",
             tables=[table(["Category", "Items"], LUNCH, title="午餐自由组合")]),
        card("Activities 3 and 4: order lunch, name a restaurant",
             "Activity 3: pair up and each use 40 dollars to order lunch for two from the Full Moon Mandarin Cuisine menu on the book’s website link, writing the selections in Chinese; then compare and decide on a final order (the website menu is not included). Activity 4: in groups of three, name your new restaurant (饭店名字) and design its menu (菜单) with the columns 汤, 菜, 主食 and 饮料; then take turns role-playing waiter or waitress and write down the other group’s orders."),
        card("Activity 5: the names of Chinese dishes",
             "A. Listen to the names of seven dishes and transcribe them (audio, not included; the characters and the book’s English names are given here). B. In your group, discuss each dish and guess why it has that name.",
             tables=[wtable(DISHES, title="Dishes with picturesque names")]),
    ],
    exercises=[
        M("How do you ask “Do you have beer?”", "你们有啤酒吗？", ["你们啤酒有吗？", "有你们啤酒吗？", "啤酒你们吗有？"], "有 + noun + 吗."),
        M("How do you ask what today’s special is?", "你们今天的特色菜是什么？", ["你们今天的什么是特色菜吗？", "今天的菜是特色什么？", "特色菜你们吗？"], "特色菜 means a specialty dish."),
        M("How do you ask how many dumplings are on a plate?", "一盘饺子有几个？", ["饺子一盘有吗？", "几个有一盘饺子？", "一盘几个饺子吗？"], "几 + measure word."),
        M("How do you order “a glass of Coke”?", "我要一杯可乐。", ["我要一碗可乐。", "我要一双可乐。", "我要一盘可乐。"], "杯 goes with drinks in a glass."),
        M("How do you ask if a dish is spicy?", "这个菜辣不辣？", ["这个菜辣吗不？", "这个辣菜吗？", "这个菜不辣辣？"], "A not-A question: 辣不辣."),
        M("What does a lunch combination 一菜一汤 + 一个主食 + 一个饮料 include?", "One dish, one soup, one staple and one drink", ["Two dishes and one soup", "One soup and two drinks", "Only a staple and a drink"], "The combination is 一菜一汤 plus 一个主食 plus 一个饮料."),
        M("Which dish is “Ants on a Tree”?", "蚂蚁上树", ["全家福", "松鼠鱼", "罗汉斋"], "蚂蚁 (ants) + 上树 (climb the tree)."),
        M("Which dish is “Happy Family”?", "全家福", ["蚂蚁上树", "松鼠鱼", "罗汉斋"], "全家 (the whole family) + 福 (fortune)."),
        M("Which dish is “Squirrel Fish”?", "松鼠鱼", ["蚂蚁上树", "全家福", "罗汉斋"], "松鼠 means squirrel."),
        M("Which dish is “Buddha’s Delight”?", "罗汉斋", ["蚂蚁上树", "全家福", "松鼠鱼"], "罗汉斋 is a vegetarian dish."),
        M("Which dish is “Little White Dragon Crosses the River”?", "小白龙过江", ["鱼香肉丝", "红烧狮子头", "松鼠鱼"], "小白龙 (little white dragon) + 过江 (cross the river)."),
        M("Which dish is “Soy Sauce-Braised Lion’s Head”?", "红烧狮子头", ["鱼香肉丝", "小白龙过江", "罗汉斋"], "红烧 (braised in soy sauce) + 狮子头 (lion’s head)."),
        F("你们今天的___菜是什么？", "特色", PART, "特色菜: specialty dish."),
        F("我要三小碗米饭，一盘___。", "饺子", ["作业", "操场", "预习"], "The thing ordered must be food."),
        mean("鱼香肉丝", "yu2 xiang1 rou4 si1", "fish-flavored pork slices", ["happy family", "ants on a tree", "squirrel fish"]),
    ],
)

# ------------------------------------------------------------------ 10. vocabulary
L10 = vocab_lesson("Presentation 1 vocabulary (41 words and expressions)", "主食 · 点菜 · 烤鸭 · 筷子 · 您几位？ · 请慢用",
                   "Vocabulary list (Presentation 1)",
                   "The book’s 35 words and the six fixed expressions often used in a restaurant, with the traditional form where it differs.", VOC1)

UNIT = unit("第八课 中国食品与餐馆 Presentation 1: ordering food at a restaurant", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
