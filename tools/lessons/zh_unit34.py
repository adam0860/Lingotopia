"""Unit 34: Lesson 12 (Unit 2 review) activities: vocabulary review, presentation activities review, grammar and usage review,
skill integration review and using Chinese in context review. Everything readable in the book is here; the audio activities, the
pictures and the question-maze board are not. Where the book leaves a table or a cloze blank, the answers are mine."""
from zh_auto import *

_D0 = D


def D(zh, en, hl=None, fixes=None):
    """D with this unit's fixed readings: 长 is always cháng here, 种着 is zhòng, 还得 is hái děi."""
    f = {"长": "chang2", "种": "zhong4"}
    if "还得" in zh:
        f["得"] = "dei3"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. objectives + vocabulary review
MENU = [("主食", "米饭、炒面、饺子"), ("肉类", "红烧肉、青椒炒牛肉、宫爆鸡丁、烤鸭"), ("汤", "酸辣汤、三鲜汤"), ("海鲜", "糖醋鱼"), ("饮料", "可乐、苹果汁、啤酒、绿茶、橙汁、咖啡"), ("素菜", "麻婆豆腐、西红柿炒鸡蛋、炒土豆丝、炒时蔬")]
V4 = [("对不起，你们点的牛肉饺子和糖醋鸡肉都卖完了。", "Sorry, the beef dumplings and the sweet and sour chicken that you ordered are all sold out."),
      ("你把我妹妹去年我过生日送给我的那本书放在哪儿了？", "Where did you put that book my younger sister gave me last year for my birthday?"),
      ("你好，我是昨天在电话上问你问题的那个想租你的公寓的人。", "Hello, I’m the person who asked you questions on the phone yesterday and wants to rent your apartment."),
      ("这是我在那家最大的商场打折的时候买的一套德国咖啡壶。", "This is a set of German coffee pots that I bought at that biggest mall when it was having a sale."),
      ("打折的童装都卖完了，不过我们还有很多不打折，可是质量和样式都很好的童装，你要不要看看？", "The discounted children’s clothing is all sold out, but we still have a lot of children’s clothing that is not discounted but is of very good quality and style. Would you like to take a look?")]
JOURNAL = ("上星期五我们全家给我母亲过生日。我们在一家有名的中餐馆订了一张桌子。那天我们一共点了五菜一汤，鸡鸭鱼肉都有，而且色味俱全。我们一边吃饭一边聊天，非常高兴！"
           "吃过饭以后，我们都把送给妈妈的生日礼物拿了出来。我妈妈常常喜欢走到海边散步，所以我送了她一双休闲运动鞋，是我到百货大楼挑的，不但价格、样式不错，而且也很舒服，走远路没问题。"
           "小弟送了她一套漂亮的餐具。除了杯子、盘子以外，还有好看的刀叉。大哥说我的父母什么都有，所以送了一个最小最方便的礼物。他帮妈妈在手机上下载了微信软件，然后从他的网上银行转了一千块钱的电子红包给妈妈。"
           "这样她想买什么只要用手机扫码就可以买到。他说连去市场买蔬菜、水果也可以用。妈妈说这些礼物她都很喜欢，谢谢我们给她过了一个愉快的生日。")
JOURNAL_E = ("Last Friday our whole family celebrated my mother’s birthday. We booked a table at a famous Chinese restaurant. That day we ordered five dishes and one soup altogether, with chicken, duck, fish and meat, and it all had color, aroma and taste. We chatted while we ate, and everyone was very happy! After the meal, we all took out the birthday presents we had for Mom. My mom often likes to walk to the seaside and stroll, so I gave her a pair of casual sports shoes that I picked at the department store; they are not only good in price and style but also comfortable, and she can walk long distances with no problem. My younger brother gave her a nice set of tableware. Besides cups and plates, there are also pretty knives and forks. My older brother said my parents have everything, so he gave the smallest and most convenient present. He helped Mom download the WeChat software on her phone and then transferred a 1,000-yuan electronic red packet from his online bank to Mom. This way, whatever she wants to buy, she only needs to scan a code with her phone. He said even buying vegetables and fruit at the market can be done this way. Mom said she liked all these presents and thanked us for giving her a happy birthday.")
JKEY = [("订", "book a table"), ("汤", "five dishes and one soup"), ("聊天", "chat while eating"), ("散步", "stroll at the seaside"), ("样式", "price and style"), ("盘子", "cups and plates"),
        ("方便", "the smallest, most convenient gift"), ("软件", "the WeChat software"), ("银行", "his online bank"), ("扫码", "scan a code"), ("蔬菜", "buy vegetables and fruit")]
L1 = lesson(
    "Lesson 12 (Unit 2 review): objectives and vocabulary review",
    "第十二课 单元复习课 · 菜单 · 租房词汇 · 地点 · 琳达的日记",
    requires=[],
    cards=[
        card("第十二课 单元复习课: Unit 2 Review (objectives)",
             "This lesson is designed to help you review and consolidate what you learned in Lessons 7–11. When you have completed it, you will be able to: 1. Understand conversations and short written passages containing basic information on school life, food and restaurants, shopping, renting and housing, and banking. 2. Grasp linguistic and non-linguistic features directly related to those topics, e.g. core vocabulary, grammar, sociolinguistic terms and cultural knowledge. 3. Use the above skills and knowledge to perform a variety of communicative tasks and activities."),
        card("Vocabulary Review, Activity 1: the menu",
             "A. Write each food item from the word pool under its category on the menu. The word pool: 可乐, 酸辣汤, 苹果汁, 啤酒, 米饭, 绿茶, 糖醋鱼, 麻婆豆腐, 青椒炒牛肉, 炒面, 橙汁, 红烧肉, 饺子, 咖啡, 烤鸭, 西红柿炒鸡蛋, 炒土豆丝, 三鲜汤, 炒时蔬, 宫爆鸡丁. The categories are 主食, 肉类, 汤, 海鲜, 饮料 and 素菜; the book leaves the menu blank, so the sorting below is mine. B. Pair up and write a dialog using your menu. C. Perform it for the class.",
             tables=[table(["Category", "Items from the word pool"], [(c, items) for c, items in MENU], title="菜单 (my sorting)", say=[0, 1])]),
        card("Activities 2 and 3: housing words and places",
             "Activity 2. A. In each category box write as much relevant vocabulary as you can remember, then compare with a partner. The boxes: 租房词汇, 家具, 家/房子, 方位词, 房间种类. B. Write three sentences that use at least one word from two different categories; read them to your partner, who translates them back to you. Activity 3. A. Form groups of three. Your teacher gives each of you an index card with a location written on it. Your other group members guess the location by asking you yes/no questions in Chinese about the activities people do there. The group that guesses all three locations first wins. B. In 故事接龙 fashion each group creates a story about a fun day including activities at five or more locations. C. Retell the story to the class, or record it and upload it to MS Teams as an assignment. The locations:",
             tables=[wtable(rows_py([("图书馆", "library"), ("车库", "garage"), ("宿舍", "dormitory"), ("体育馆", "gym; stadium"), ("饭馆", "restaurant"), ("院子", "yard"), ("农贸市场", "farmers’ market"), ("百货大楼", "department store"), ("操场", "drill field; sports ground"), ("食堂", "dining hall"), ("客厅", "living room"), ("地下室", "basement"), ("银行", "bank")]), title="Locations on the index cards")]),
        card("Activity 4: translate and analyze sentences",
             "A. Listen to six sentences and translate them (audio, not included). B. Read the following sentences. Highlight all the subjects, modifiers, verbs or verb phrases, and objects. Translate the sentences, then compare with a partner. The book gives no translations, so these are mine:",
             examples=[D(z, e) for z, e in V4]),
        card("Activity 5: Linda’s journal about her mom’s birthday",
             "A. Read Linda’s journal entry. Fill in the missing words using the linguistic and contextual clues. The word box: 散步, 银行, 汤, 订, 聊天, 样式, 盘子, 方, 软件, 蔬菜, 扫码. B. Read the completed entry to a partner and compare answers. C. Use the key words in the box to retell the story to your partner. The book prints the amount as a digit; here it is spelled out. The completed entry (the answers are mine):",
             examples=[D(JOURNAL, JOURNAL_E)],
             tables=[table(["Blank", "Where it goes"], [(z, e) for z, e in JKEY], title="The word for each blank, in order", say=[0])]),
        card("Activity 6: question maze",
             "Form teams of three. Examine the question maze and find the starting point. Each student throws the dice and moves to the square that corresponds to the number rolled, and responds to the content of that square in complete sentences. A purple square means you may talk about any topic you choose; on an orange triangle your teammates ask you about a topic they choose. (The board is a picture, so it is not included.)"),
    ],
    exercises=[
        M("In which category does 酸辣汤 belong on the menu?", "汤", ["饮料", "主食", "素菜"], "酸辣汤 is a soup."),
        M("In which category does 麻婆豆腐 belong?", "素菜", ["肉类", "饮料", "汤"], "Tofu in hot sauce is a vegetable dish (素菜)."),
        M("In which category does 糖醋鱼 belong?", "海鲜", ["素菜", "饮料", "汤"], "Sweet and sour fish is seafood."),
        M("In which category does 饺子 belong?", "主食", ["饮料", "汤", "海鲜"], "Dumplings are a staple (主食)."),
        M("Which of these is a drink?", "橙汁", ["炒面", "烤鸭", "红烧肉"], "橙汁 is orange juice."),
        M("What does 色味俱全 describe?", "Food with color, aroma and taste all present", ["Food that is sold out", "A restaurant with no seats", "A very cheap meal"], "色味俱全."),
        M("What did Linda’s family do for her mother’s birthday?", "Celebrated at a Chinese restaurant", ["Went to a bank", "Stayed home to study", "Flew to China"], "我们在一家有名的中餐馆订了一张桌子。"),
        M("What did Linda give her mother?", "A pair of casual sports shoes", ["A set of tableware", "An electronic red packet", "A bike"], "我送了她一双休闲运动鞋。"),
        M("What did the younger brother give?", "A set of tableware", ["Sports shoes", "An electronic red packet", "A phone"], "小弟送了她一套漂亮的餐具。"),
        M("What did the older brother give?", "An electronic red packet sent through WeChat", ["A set of tableware", "Sports shoes", "A birthday cake"], "大哥…转了一千块钱的电子红包给妈妈。"),
        M("In the journal, the brother says 连去市场买蔬菜、水果也可以用. What does 连 do here?", "Means “even”: even buying vegetables can be done this way", ["Means “connect” the market", "Means “and then”", "Asks a question"], "连…也…: even."),
        M("Which word fills the blank in 我们在一家有名的中餐馆___了一张桌子？", "订", ["卖", "吃", "洗"], "订: book, reserve."),
        M("What does 打折 mean?", "Give a discount", ["Break a plate", "Pay cash", "Open an account"], "打折: give a discount."),
        M("In sentence 2 of Activity 4, what was the book?", "A gift from the speaker’s younger sister last year", ["A dictionary the speaker bought", "A textbook for the class", "A book from the library"], "我妹妹去年我过生日送给我的那本书."),
        F("我们一边吃饭一边___天，非常高兴！", "聊", PART, "聊天: chat."),
        F("他帮妈妈在手机上下载了微信软___。", "件", PART, "软件: software."),
        F("这样她想买什么只要用手机___码就可以买到。", "扫", PART, "扫码: scan a code."),
    ],
)

# ------------------------------------------------------------------ 2. presentation activities review
PA = ("这个长周末很多商店打折，我和我太太去百货大楼买了很多东西。在卖衣服的地方，我太太买了两件衣服，颜色很好，而且都打七折。我买了一双皮鞋和两件衬衫，我都很喜欢。有一套西装原价两千五百，现在卖两千三百。我试了一下，觉得样式不错，但价钱还是有点儿贵，所以就没买。然后我们又去给儿子买了一个书包，几个笔记本和一些圆珠笔，还有一些日用品。现在在商店买东西，现金、信用卡都不需要带，用手机刷卡就可以，非常方便！")
PA_E = ("This long weekend a lot of stores had sales, and my wife and I went to the department store and bought a lot of things. In the clothing section my wife bought two pieces of clothing in nice colors, both at 30% off. I bought a pair of leather shoes and two shirts, and I like them all. There was a suit with an original price of 2,500 that now sells for 2,300. I tried it on and felt the style was good, but the price was still a bit expensive, so I didn’t buy it. Then we went to buy our son a schoolbag, several notebooks, some ballpoint pens and some daily necessities. Nowadays when you shop in stores you don’t need to bring cash or a credit card; you can pay by swiping your phone, which is very convenient!")
PB = ("我们上个星期刚搬到新租的一套公寓。新公寓有三室一厅，带家具。主卧很大，客厅也不小，但饭厅和厨房都不大。每月房租两千五，贵是贵了点儿，可是包水费、电费和网费，还有一个不需要付钱的停车位，所以我们觉得还可以。这儿交通很方便，也很安全。"
      "搬进新家我们很开心，明天要请一些朋友来聚聚。今天上午我去超市买了一些东西，为聚会做准备。我买了两斤西红柿，两把菠菜，三斤青椒，还有海鲜和牛肉。除了蔬菜，我还买了一些苹果和橘子，还有两串香蕉。")
PB_E = ("Last week we just moved into a newly rented apartment. The new apartment has three bedrooms and one living room and comes with furniture. The master bedroom is big and the living room is not small, but the dining room and kitchen are not big. The monthly rent is 2,500; it is expensive, to be sure, but it includes water, electricity and internet fees, and there is a parking space that you don’t have to pay for, so we think it’s all right. Transportation here is very convenient, and it’s very safe. We are very happy to have moved into our new home and tomorrow we will invite some friends to get together. This morning I went to the supermarket and bought some things to prepare for the party. I bought two jin of tomatoes, two bunches of spinach, three jin of green peppers, and also seafood and beef. Besides vegetables, I also bought some apples and tangerines, and two bunches of bananas.")
L2 = lesson(
    "Lesson 12 (Unit 2 review): presentation activities review",
    "两篇短文：百货大楼 · 新租的公寓 · 银行对话",
    requires=[],
    cards=[
        card("Activity 1: listening to three dialogs",
             "A. Listen to three dialogs, then match each one to a picture. B. Form teams of three. Each student listens to one dialog again and fills in a table (Gist, Details), then asks teammates EEI questions in Chinese (who, what, where, when, why, how, etc.) to get the information for the other two dialogs. C. For your dialog, read the underlined sentences from the scripts your teacher provides and take turns translating them aloud. (The dialogs are audio and the pictures are not included.)"),
        card("Activity 2: Passage A (shopping)",
             "A. Pair up. Read Passage A while your partner reads Passage B. Consult a dictionary if needed, then fill in the table for your passage (The gist; Items purchased (why, for whom, how much, etc.); Items not purchased and why; Payment). B. Ask your partner questions in Chinese to fill in the other half of the table.",
             examples=[D(PA, PA_E)],
             tables=[table(["Table", "Answer (mine)"], [("The gist", "A couple shop at the department store over the long weekend sales"), ("Items purchased", "Wife: two pieces of clothing at 30% off; husband: leather shoes and two shirts; for the son: a schoolbag, notebooks, ballpoint pens, daily necessities"), ("Items not purchased and why", "A suit (original price 2,500, now 2,300): good style but still a bit expensive"), ("Payment", "By phone; no cash or credit card needed")], title="Passage A table")]),
        card("Activity 2: Passage B (the apartment)",
             "Passage B with its table (The gist; Apartment-related costs; Type and description of apartment rooms; When; Plans for tomorrow; Items purchased this morning):",
             examples=[D(PB, PB_E)],
             tables=[table(["Table", "Answer (mine)"], [("The gist", "Moved into a newly rented apartment last week; shopping for tomorrow’s get-together"), ("Apartment-related costs", "Rent 2,500 a month, including water, electricity and internet; a free parking space"), ("Type and description of rooms", "Three bedrooms, one living room, with furniture; big master bedroom, living room not small, small dining room and kitchen"), ("When", "Moved in last week; shopping this morning"), ("Plans for tomorrow", "Invite some friends over to get together"), ("Items purchased this morning", "Two jin of tomatoes, two bunches of spinach, three jin of green peppers, seafood, beef, apples, tangerines, two bunches of bananas")], title="Passage B table")]),
        card("Activity 3: the bank dialog",
             "A. Listen to the dialog and answer the questions: 1. Is the customer new or returning? How do you know? 2. What account(s) does the customer have with this bank? B. Listen again and fill in a table (Activity, Reason, How It Was Accomplished) in as much detail as possible. C. Ask a partner four questions in Chinese about the table, then read the script your teacher provides to check your answers. D. Orally translate David’s sentences into English; your partner translates them back into Chinese without looking at the script. Switch roles and translate the bank clerk’s sentences. (Audio, not included.)"),
    ],
    exercises=[
        M("What did the wife buy in Passage A?", "Two pieces of clothing at 30% off", ["A suit", "A schoolbag", "Leather shoes"], "我太太买了两件衣服…都打七折。"),
        M("What does 打七折 mean?", "Sell at 70% of the price (30% off)", ["Sell at 7% of the price", "Sell at 7 yuan", "Seven pieces for one price"], "打七折: 70% of the original price."),
        M("What did the husband buy?", "Leather shoes and two shirts", ["Two suits", "A schoolbag", "Notebooks only"], "我买了一双皮鞋和两件衬衫。"),
        M("Why didn’t he buy the suit?", "The price was still a bit expensive", ["The style was bad", "It was sold out", "It was the wrong size"], "样式不错，但价钱还是有点儿贵。"),
        M("What was the suit’s original price?", "两千五百", ["两千三百", "二百五十", "两百三十"], "原价两千五百，现在卖两千三百。"),
        M("What did they buy for their son?", "A schoolbag, notebooks and ballpoint pens", ["A suit", "Leather shoes", "A phone"], "给儿子买了一个书包，几个笔记本和一些圆珠笔。"),
        M("How do they pay in stores now?", "By phone", ["In cash", "By credit card", "By check"], "用手机刷卡就可以。"),
        M("What kind of apartment is described in Passage B?", "Three bedrooms and one living room, with furniture", ["One bedroom, no furniture", "A house with a yard", "A dormitory room"], "三室一厅，带家具。"),
        M("How much is the monthly rent?", "两千五", ["二百五", "五千", "三千"], "每月房租两千五。"),
        M("What does the rent include?", "Water, electricity and internet fees", ["Only water", "Nothing", "Food"], "包水费、电费和网费."),
        M("What is special about the parking space?", "It does not cost anything", ["It is far away", "It costs extra", "There is none"], "一个不需要付钱的停车位。"),
        M("What is the writer planning for tomorrow?", "To invite some friends to get together", ["To move out", "To sign a contract", "To go to the bank"], "明天要请一些朋友来聚聚。"),
        M("Which item was NOT bought at the supermarket?", "A suit", ["Beef", "Seafood", "Spinach"], "Passage B lists foods only."),
        M("What does 贵是贵了点儿 mean?", "It is expensive, to be sure, but …", ["It is very cheap", "It is not expensive", "It is the most expensive"], "…是…，可是… concedes a point."),
        F("我太太买了两件衣服，颜色很好，而且都打七___。", "折", PART, "打七折."),
        F("新公寓有三室一___，带家具。", "厅", PART, "三室一厅."),
    ],
)

# ------------------------------------------------------------------ 3. grammar review
CONJ = [("除了语法课和阅读课，我们还有听力课和说话课。", "Besides the grammar and reading classes, we also have listening and speaking classes."),
        ("只要努力，你就一定能学好中文。", "As long as you work hard, you will certainly learn Chinese well."),
        ("他做的什么菜都辣，连饺子里都放了辣椒。", "Every dish he makes is spicy; even the dumplings have chili in them."),
        ("那家饭店菜做得好，而且服务也很不错。", "That restaurant’s food is well made, and its service is also very good."),
        ("如果没有什么问题，我们就下课吧。", "If there are no problems, let’s end class."),
        ("房租是贵了点儿，可是不但带家具，而且连水电费都包了。", "The rent is a bit expensive, but it not only comes with furniture, it even includes the water and electricity."),
        ("如果你买三件，我就给你打九折。", "If you buy three pieces, I’ll give you 10% off."),
        ("网上开户很简单，只要在银行的网站上注册一下就可以了。", "Opening an account online is very simple; you only need to register on the bank’s website."),
        ("这件衣服虽然有点贵，但是质量很好。", "Although this piece of clothing is a bit expensive, its quality is very good.")]
SELF = [("除了做作业，我还要预习新课。", "Besides doing homework, I also have to preview the new lesson."), ("连小贩都用手机收费。", "Even the vendors use their phones to collect fees."), ("这个公寓不但很大，而且很便宜。", "This apartment is not only big but also cheap."), ("如果你喜欢，我就买给你。", "If you like it, I’ll buy it for you."),
        ("只要你注册，就可以用网上银行。", "As long as you register, you can use online banking."), ("这双鞋虽然很好看，但是有点儿贵。", "Although these shoes look good, they are a bit expensive.")]
YAO = [("我想去农贸市场看看。", "I’d like to go to the farmers’ market and have a look."), ("每天我都要去体育馆锻炼。", "Every day I have to go to the gym to work out."), ("除了做作业，我还需要预习新课。", "Besides homework, I also need to preview the new lesson."), ("你们想要点儿什么主食？", "What staple food would you like?"), ("我要一瓶啤酒。", "I’d like a bottle of beer."),
       ("菜里不要放味精。", "Don’t put MSG in the dishes."), ("我想开一个活期账户。", "I’d like to open a current account."), ("租房以前得先付一个月的押金。", "Before renting you have to pay a month’s deposit first."), ("我想要租一套有两个卧室的公寓。", "I’d like to rent an apartment with two bedrooms."), ("今天作业太多了，我得晚点儿睡觉。", "There is too much homework today; I have to go to bed a bit later.")]
SHEN = [("你觉得这套西装怎么样？", "What do you think of this suit?"), ("那套公寓有多大？", "How big is that apartment?"), ("你就一个人，怎么租这么大的房子？", "You are just one person; why rent such a big house?"), ("你们什么时候考试？", "When do you have the test?"), ("我们就租这套公寓，怎么样？", "Let’s just rent this apartment, how about it?"),
        ("我想去农贸市场买点儿水果，像苹果，香蕉什么的。", "I’d like to go to the farmers’ market to buy some fruit, like apples, bananas and so on."), ("妈妈做的什么菜我都喜欢。", "I like any dish Mom makes."), ("我不知道怎么在网上办手续。", "I don’t know how to do the procedures online.")]
YIDIAN = [("你想喝点儿什么？", "What would you like to drink?"), ("我可以看一下你的机票吗？", "May I see your flight ticket?"), ("我最近有点儿忙。", "I’ve been a bit busy recently."), ("请问，这件衬衫有点儿小，能给我一件大一点儿的吗？", "Excuse me, this shirt is a little small. Can I have a larger one?"), ("这双鞋能便宜一点儿吗？", "Can this pair of shoes be a little cheaper?"), ("有点儿贵，不过是最新的样式，质量也很好。", "It’s a bit expensive, but it’s the latest style and the quality is good.")]
EMAIL = ("小文：我到台湾已经好几个月了。这里的天气跟我们老家很不一样，到这里很长时间以后我才适应了。我住的地方离学校很近，走路十几分钟就到了。我每天早上五点起床，我先锻炼身体，然后再去上课。这里的学习很紧张，我们每天都有七节课，下午五点才下课。因为今天有一个考试，我昨晚十二点才睡觉。我每天都去一家小饭店吃晚饭，那家饭店就在我的公寓楼旁边，非常方便。还有一个月我就回去了，我买了一个礼物送给你。我想你一定会喜欢的。祝好！大卫")
EMAIL_E = ("Xiaowen: I have already been in Taiwan for several months. The weather here is very different from our hometown, and only after a long time here did I adapt. Where I live is very close to school; it takes just over ten minutes to walk there. Every morning I get up at five, first I exercise, and then I go to class. Studying here is intense; we have seven classes every day and don’t finish until five in the afternoon. Because there is a test today, I didn’t go to sleep until twelve last night. Every day I go to a small restaurant for dinner; that restaurant is right next to my apartment building, which is very convenient. In one more month I will be going back, and I bought a gift to give you. I think you will surely like it. All the best! David")
BA9 = [("把碗放在桌子上。", "Put the bowl on the table."), ("你把我的手机放在哪儿了？", "Where did you put my cellphone?"), ("我们都把作业做完了。", "We all finished our homework."), ("请不要把饮料带进图书馆。", "Please don’t bring beverages into the library."), ("你得把你的银行账户和电子钱包连在一起。", "You need to link your bank account to your e-wallet.")]
DE11 = [("他说中文说得很快。", "He speaks Chinese very fast. (the book’s example)"), ("他说中文说得不怎么样。", "He doesn’t speak Chinese all that well. (the book’s example)"), ("她写汉字写得不错。", "She writes characters quite well."), ("我做菜做得不好。", "I don’t cook well."), ("我做作业做得很快。", "I do my homework very fast."), ("他吃饭吃得很多。", "He eats a lot."), ("我们考试考得怎么样？", "How did we do on the test?"), ("我游泳游得不怎么样。", "I don’t swim all that well.")]
L3 = lesson(
    "Lesson 12 (Unit 2 review): grammar and usage review",
    "量词 · 除了…还… · 连…都… · 不但…而且… · 如果…就… · 只要…就… · 虽然…但是… · 把 · 得",
    requires=[],
    cards=[
        card("Activity 1: measure words and shopping lists",
             "A. What does a best man need to wear to a wedding? Make a shopping list with the appropriate measure words and compare with a partner. B. What do you need to furnish an apartment? Make a shopping list with your partner using measure words. C. Your class is planning a Chinese dinner party. Add the quantity and measure words for 啤酒, 奶茶, 白米饭, 橙汁, 饺子, 烤鸭, 麻婆豆腐 and 筷子. D. Choose more items from 苹果, 香蕉, 西瓜, 胡萝卜, 菠菜, 黄瓜, 草莓, 鸡, 牛肉, 包子, tell your partner your choices with quantities, and have them write them down. The book leaves the lists blank; these suggestions are mine:",
             tables=[table(["List", "Items with measure words (mine)"], [("The best man", "一套西装、一件衬衫、一条领带、一双皮鞋、一双袜子"), ("Furnishing an apartment", "一张床、一张桌子、一把椅子、一个沙发、一台冰箱、一条地毯、一个书架、一个衣橱"), ("The dinner party", "四瓶啤酒、五杯奶茶、六碗白米饭、三瓶橙汁、两盘饺子、一只烤鸭、一盘麻婆豆腐、十双筷子"), ("At the market", "三斤苹果、两串香蕉、一个西瓜、两斤胡萝卜、一把菠菜、三根黄瓜、两斤草莓、一只鸡、两斤牛肉、六个包子")], title="Shopping lists", say=[1])]),
        card("Activity 2: the postal label",
             "Read this package label for the Chinese postal service (邮政特快专递). Using it as a guide, rewrite the sender and recipient addresses, fees, package weight and sending dates in English on the label that follows. The label gives: 寄件人 (sender) 马小文, 东城街五号, 青岛, 山东; 收件人 (recipient) 高大卫, 125 号三街, 蒙特雷市, 加州, 美国; 费用 (fees in yuan): 邮费 146.67, 保价费 25.00, 封装费 5.98, 其他费用 14.32, 费用合计 191.97; 包裹重量 (kg): 实际重量 2.50, 计费重量 2.30; 寄件人签名 马小文, 时间 2020.4.20 9:30. The English version (mine):",
             tables=[table(["Item", "In English"], [("Sender’s address", "Ma Xiaowen, No. 5 Dongcheng Street, Qingdao, Shandong"), ("Recipient’s address", "Gao Dawei, 125 Third Street, Monterey, California, USA"), ("Total fees", "191.97 yuan (postage 146.67, insurance 25.00, packing 5.98, other 14.32)"), ("Package weight", "2.50 kg actual weight; 2.30 kg billed weight (as printed)"), ("Sending date and time", "April 20, 2020, 9:30")], title="The label in English")]),
        card("Activity 3: conjunctions",
             "Complete the sentences with the conjunctions in the table: 除了…(以外), 还/也…; 连…都/也…; (不但)…而且…; 如果…就…; 只要…就…; 虽然…但是…. The book prints the sentences with blanks; the answers below are mine, with 如果 or 只要 where either fits.",
             examples=[D(z, e) for z, e in CONJ]),
        card("Activity 4: write sentences with the patterns",
             "A. Write sentences with 除了…以外，还/也…, 连…都/也…, （不但）…而且…, 如果…就…, 只要…就…, 虽然…但是…. B. Read your sentences to a partner while they translate them orally. One set of examples (mine):",
             examples=[D(z, e) for z, e in SELF]),
        card("Activity 5: 要, 想, 想要, 得, 不要, 需要",
             "Complete the sentences with 要, 想, 想要, 得(děi), 不要 or 需要, then compare with a partner and explain any differences. The book leaves the blanks; my answers (other choices can work in a few of them):",
             examples=[D(z, e, fixes={"得": "dei3"} if "得" in z else None) for z, e in YAO]),
        card("Activity 6: 什么, 什么的, 多, 什么时候, 怎么, 怎么样",
             "Complete the sentences with 什么, 什么的, 多, 什么时候, 怎么 or 怎么样 and compare with a partner. My answers:",
             examples=[D(z, e) for z, e in SHEN]),
        card("Activities 7 and 8: (一)点儿, 一下, 有点儿, and the email",
             "Activity 7. Translate the sentences below using (一)点儿, 一下 or 有点儿: 1. What would you like to drink? 2. May I see your flight ticket? 3. I’ve been a bit busy recently. 4. Excuse me, this shirt is a little small. Can I have a larger one? 5. Can this pair of shoes be a little cheaper? 6. It’s a bit expensive, but it’s the latest model and the quality is good. My translations:",
             examples=[D(z, e) for z, e in YIDIAN]),
        card("Activity 8: email with 已经, 还有, 才, 就, 离, 再, 都",
             "Complete the email with 已经, 还有, 才, 就, 离, 再 or 都; some words may be used more than once. The book’s text has a blank before 一个月 and one after 我; I read it as 还有 … 就. The completed email (my answers):",
             examples=[D(EMAIL, EMAIL_E)]),
        card("Activities 9 to 11: 把, the voicemail and the degree complement 得",
             "Activity 9. Translate the sentences using 把 and compare with a partner: 1. Put the bowl on the table. 2. Where did you put my cellphone? 3. We all finished our homework. 4. Please don’t bring beverages into the library. 5. You need to link your bank account to your e-wallet. My translations:",
             examples=[D(z, e, fixes={"得": "dei3"} if "得" in z else None) for z, e in BA9]),
        card("Activities 10 and 11",
             "Activity 10 (Listening and Speaking). Listen to the voicemail and take notes on what Xiaoming’s mother asked him to do; the new word is 报纸 (bàozhǐ: newspaper). Then discuss in Chinese what she told him to do. (Audio, not included.) Activity 11. Pair up and make sentences connecting the terms on the left (说中文, 写汉字, 做菜, 做作业, 吃饭, 考试, 游泳) with the adjectives on the right (a. 怎么样, b. 好, c. 快, d. 多, e. 不错, f. 不好, g. 不怎么样) using the degree complement 得, taking turns until you have each said seven sentences. The book’s two examples and my sentences:",
             examples=[D(z, e) for z, e in DE11]),
    ],
    exercises=[
        F("___语法课和阅读课，我们还有听力课和说话课。", "除了", ["虽然", "只要", "连"], "除了…还…: besides…also…"),
        F("___努力，你就一定能学好中文。", "只要", ["除了", "虽然", "连"], "只要…就…: as long as…"),
        F("他做的什么菜都辣，___饺子里都放了辣椒。", "连", ["除了", "虽然", "只要"], "连…都…: even…"),
        F("这件衣服___有点贵，但是质量很好。", "虽然", ["除了", "只要", "连"], "虽然…但是…: although…"),
        F("那家饭店菜做得好，___服务也很不错。", "而且", ["但是", "所以", "然后"], "而且 adds a further point."),
        F("如果没有什么问题，我们___下课吧。", "就", PART, "如果…就…: if…then…"),
        F("我想去农贸市场看___。", "看", PART, "看看: have a look."),
        F("租房以前___先付一个月的押金。", "得", PART, "得 (děi): have to."),
        F("菜里___要放味精。", "不", PART, "不要: don’t."),
        F("你觉得这套西装___么样？", "怎", PART, "怎么样: how is it?"),
        F("那套公寓有___大？", "多", PART, "多大: how big?"),
        F("请不要___饮料带进图书馆。", "把", PART, "把 + object + verb."),
        F("我们都把作业做___了。", "完", PART, "做完: finish."),
        F("他说中文说___很快。", "得", PART, "The degree complement 得."),
        F("这双鞋能便宜一___儿吗？", "点", PART, "(一)点儿: a bit."),
        M("What do 要, 想 and 想要 have in common in 我想要一瓶啤酒?", "All express wanting something", ["All mean “must”", "All are negative", "All mean “need not”"], "要/想/想要: want."),
        M("Which sentence means “I’ve been a bit busy recently”?", "我最近有点儿忙。", ["我最近一点儿忙。", "我最近一下忙。", "我最近有一下忙。"], "有点儿 + adjective."),
        M("Which sentence is correct?", "把碗放在桌子上。", ["放把碗在桌子上。", "碗把放在桌子上。", "把放碗在桌子上。"], "把 + object + verb + 在…"),
        M("What does the total fee on the postal label add up to?", "191.97 yuan", ["146.67 yuan", "25.00 yuan", "5.98 yuan"], "146.67 + 25.00 + 5.98 + 14.32 = 191.97."),
        M("Which place is the recipient on the postal label located?", "Monterey, California", ["Qingdao, Shandong", "Beijing", "Taiwan"], "蒙特雷市, 加州."),
        M("In David’s email, how far is his apartment from school?", "Very close; ten-odd minutes on foot", ["Two hours by bus", "Next to the library", "In another city"], "走路十几分钟就到了。"),
        M("At what time does David get up each morning?", "At five", ["At six-thirty", "At nine", "At ten"], "我每天早上五点起床。"),
    ],
)

# ------------------------------------------------------------------ 4. skill integration review
TF2 = [("大卫和他的三个朋友一起去吃饭。", "David goes to eat with his three friends."), ("他们已经在网上订了桌子。", "They already booked a table online."), ("这家餐馆的特色菜是烤鸭。", "This restaurant’s specialty is roast duck."), ("大卫喜欢吃清淡的菜。", "David likes light dishes."), ("大卫的朋友马克不喜欢咸的菜。", "David’s friend Mark doesn’t like salty dishes.")]
DLI = ("大哥：你好！你上次问我我在国防语言学院的生活怎么样？怎么说呢？一开始我不太习惯，现在完全适应了。在国防语言学院学习，因为我们又是军人又是学生，所以非常忙。我们每天早上六点半集合，然后上六节课，早上七点四十五分上课，下午两点五十下课。每天我们有阅读课、听力课、语法课和说话课。中午我们有一个小时吃饭的时间。下午下课以后我们去操场锻炼身体，晚上还得做作业、预习生词和课文。有时候我们还要值班。所以，我常常十点以后才能睡觉。"
       "不过，我很喜欢这儿的周末，因为有时间可以做我想做的事情。星期六和星期天，我差不多九点半起床。早饭以后，我先去体育馆锻炼身体，然后和朋友去中国饭馆吃午饭、聊天。下午，有时我和同学去看电影、有时去海边散步、有时去购物买东西。星期天晚上我常常去图书馆做作业，因为星期一要上课。好了，今天就说到这儿吧。下个星期给你打电话。祝好！弟弟")
DLI_E = ("Big brother: Hello! Last time you asked me how my life at the Defense Language Institute is. How shall I put it? At first I wasn’t quite used to it, and now I have completely adapted. Studying at DLI, because we are both military and students, we are very busy. Every day at 6:30 in the morning we fall in, then we have six classes, starting at 7:45 and ending at 2:50 in the afternoon. Every day we have reading, listening, grammar and speaking classes. At noon we have an hour to eat. After class in the afternoon we go to the drill field to exercise, and in the evening we still have to do homework and preview new words and texts. Sometimes we also have to stand duty. So I often can’t go to sleep until after ten. But I really like the weekends here, because there is time to do what I want. On Saturday and Sunday I get up at about 9:30. After breakfast I first go to the gym to exercise, then go with friends to a Chinese restaurant for lunch and chat. In the afternoon, sometimes my classmates and I go to a movie, sometimes to the seaside for a walk, and sometimes shopping. On Sunday evening I often go to the library to do homework, because there is class on Monday. All right, that’s all for today. I’ll call you next week. All the best! Little brother")
HOUSE = ("我家在华盛顿州的西雅图市。我们家的房子是一个三层楼的房子。房子的前边有一个小花园，里边种着很多漂亮的花。后边是个大院子，里面种着一些蔬菜和果树。"
         "我家的屋顶是深咖啡色的，外墙是浅黄色的，大门是红色的。进门后，你会看见一个大客厅，客厅里摆着一张长沙发，一个两人沙发和一张咖啡桌。客厅的后墙上有四个大窗户，所以客厅很明亮。"
         "客厅的对面是厨房，厨房的旁边是饭厅，饭厅里有一张饭桌和六把椅子。客厅的左边是书房，书房很小，只摆着一张办公桌，一个书架和一台电脑。书房的旁边是个卫生间。"
         "二楼有三个卧室，第一个房间是我弟弟的房间，旁边是一个卫生间，这个卫生间是我弟弟和妹妹共用的。卫生间的右边是我妹妹的房间。最里面是我爸爸妈妈住的主卧室，他们有自己的卫生间。主卧室里摆着一张大双人床，两个床头柜，一个躺椅，还有一个很大的衣橱。"
         "我的房间在三楼，三楼是一个阁楼，有一个卫生间，还有一个很小的活动室。我喜欢有自己的空间。我们的房子还有一个地下室和一个车库。地下室是我们的健身房和游戏室。车库里除了停车，还放着爸爸的很多工具。他最喜欢在那儿做木工。")
HOUSE_E = ("My family lives in Seattle, Washington State. Our house is a three-story house. In front of the house there is a small garden planted with many pretty flowers. Behind is a big yard planted with some vegetables and fruit trees. The roof of our house is dark brown, the outer walls are light yellow, and the front door is red. After you enter the door, you will see a big living room; in it are placed a long sofa, a two-seater sofa and a coffee table. On the back wall of the living room there are four big windows, so the living room is very bright. Across from the living room is the kitchen, and next to the kitchen is the dining room, which has a dining table and six chairs. To the left of the living room is the study; the study is very small and has only a desk, a bookshelf and a computer. Next to the study is a bathroom. On the second floor there are three bedrooms. The first room is my younger brother’s, next to it is a bathroom shared by my younger brother and sister. To the right of the bathroom is my younger sister’s room. At the very back is the master bedroom where my parents live; they have their own bathroom. In the master bedroom are a big double bed, two nightstands, a recliner, and a very big closet. My room is on the third floor, which is an attic with a bathroom and a very small activity room. I like having my own space. Our house also has a basement and a garage. The basement is our gym and game room. In the garage, besides parking, there are also many of Dad’s tools. He likes to do woodworking there best.")
NEWS = ("以前，外国人因为没有中国国内银行卡或手机号码等，往往无法注册使用中国移动支付。现在，支付宝、微信支付可以跟国外银行卡绑定，为很多外国朋友在中国使用移动支付打开了“方便之门”。"
        "在中国工作或学习的外国人，在购物付款的时候，比如是“扫码”支付，还是现金、刷卡支付，就会告诉中国人他们来中国多长时间了。美国留学生琳达说，“我看到在中国几乎所有的商店都有移动支付的二维码，扫一扫付款，又快又方便。”这是她第二次来中国，两年前第一次来的时候，因为需要中国银行卡和手机号才能成功注册，她没有办法使用中国的移动支付。琳达说，在美国她常常使用现金和信用卡，而在中国大多数人“扫码”就可以支付。"
        "百分之二十的外国网友说不能像中国人一样用手机支付，是他们来中国时最大的麻烦。“我的两位中国室友帮助我开通了移动支付。用手机什么都可以‘扫一扫’，超级快，非常好用。”来自法国的马克说。"
        "二零一八年在中国工作的外国人已经有九十五万人。很多来中国学习、工作、生活的外国人跟琳达和马克一样，都已经习惯了移动支付的方便，除了购物、付房租、订餐以外，他们也用移动支付买机票、付学费什么的。")
NEWS_E = ("In the past, because foreigners did not have a Chinese domestic bank card or phone number, they often could not register to use Chinese mobile payment. Now Alipay and WeChat Pay can be linked to foreign bank cards, opening a “door of convenience” for many foreign friends using mobile payment in China. When foreigners working or studying in China pay for purchases, whether they pay by “scanning the code” or by cash or card, it tells Chinese people how long they have been in China. Linda, an American study-abroad student, says, “I see that in China almost every store has a mobile payment QR code, and scanning to pay is both fast and convenient.” This is her second time in China; two years ago on her first visit, because a Chinese bank card and phone number were needed to register successfully, she had no way to use Chinese mobile payment. Linda says that in the U.S. she often uses cash and credit cards, while in China most people can pay by “scanning the code”. Twenty percent of foreign netizens say that not being able to pay by phone like Chinese people is the biggest trouble when they come to China. “My two Chinese roommates helped me turn on mobile payment. With a phone you can ‘scan’ anything; it’s super fast and very easy to use,” says Mark, who comes from France. In 2018 there were already 950,000 foreigners working in China. Many foreigners who come to China to study, work and live, like Linda and Mark, have gotten used to the convenience of mobile payment; besides shopping, paying rent and ordering meals, they also use mobile payment to buy plane tickets, pay tuition and so on.")
NEWS_T = [("以前，外国人因为没有中国国内银行卡或手机号码等，往往无法注册使用中国移动支付。现在，支付宝、微信支付可以跟国外银行卡绑定，为很多外国朋友在中国使用移动支付打开了“方便之门”。", "In the past, because foreigners did not have a Chinese bank card or phone number, they often could not register for Chinese mobile payment. Now Alipay and WeChat Pay can be linked to foreign bank cards, opening a “door of convenience” for many foreign friends."),
          ("在中国工作或学习的外国人，在购物付款的时候，比如是“扫码”支付，还是现金、刷卡支付，就会告诉中国人他们来中国多长时间了。", "When foreigners working or studying in China pay, whether by “scanning the code” or by cash or card, it tells Chinese people how long they have been in China."),
          ("百分之二十的外国网友说不能像中国人一样用手机支付，是他们来中国时最大的麻烦。", "Twenty percent of foreign netizens say that not being able to pay by phone like Chinese people is their biggest trouble in China."),
          ("很多来中国学习、工作、生活的外国人跟琳达和马克一样，都已经习惯了移动支付的方便，除了购物、付房租、订餐以外，他们也用移动支付买机票、付学费什么的。", "Many foreigners who come to China to study, work and live, like Linda and Mark, are used to the convenience of mobile payment; besides shopping, paying rent and ordering meals, they also use it to buy plane tickets, pay tuition and so on.")]
L4 = lesson(
    "Lesson 12 (Unit 2 review): skill integration review",
    "国防语言学院的生活 · 我家的房子 · 外国人也能在中国“扫码”",
    requires=[],
    cards=[
        card("Activities 1 to 4 (listening)",
             "Activity 1. A. Listen to the dialog and mark five statements true or false (statements below; audio, so no key is given). B. Listen again and fill in a table with the drinks, dishes, soups and staples that David and Mark ordered. C. Read the script and perform the dialog. Activity 2. A. Listen to a dialog about going somewhere to buy a shirt, and answer: 1. Where do the speakers want to go? 2. Why? 3. What does the first speaker say about the second speaker? 4. What does the first speaker plan to do? 5. What does the second speaker suggest? B. Listen again; complete Table 1 (凯丽的衬衫) while a partner completes Table 2 (网上购物) with four EEIs each, then exchange information to fill in Table 3 (Linda’s purchases at the farmers’ market: items, total spent, payment method). D. In groups of three, discuss your own shopping habits (online vs. in-person shopping). Activity 3. A. Listen to the phone call about renting: how was the conversation conducted, and which of three apartments (两室一厅, 三室两厅二卫, 四室两厅二卫) would interest the applicant? B. What does the manager recommend, what is the total of the first payment and what does it include, what are three details about the facilities and surroundings, and when can the applicant sign the contract? D. Tell your partner about a place you once rented. Activity 4. A. Where does the bank conversation take place and what does the customer want to do? B. Fill in a table: the three steps for opening an account, the account(s) opened and why, the currency exchange amount and rate, and the online banking services. (All audio, not included.) The Activity 1 statements:",
             examples=[D(z, e) for z, e in TF2]),
        card("Activity 5: an email from a DLI student",
             "A. Scan the email message from a DLI student (the book prints the subject 国防语言学院的生活) and answer: 1. What is the email about? 2. How has the student changed? 3. What are the two major topics? (Mine: 1. His life at DLI. 2. At first he wasn’t used to it; now he has completely adapted. 3. His weekday schedule and his weekends.) B. Reread the second paragraph while a partner rereads the third, then write a Chinese summary of your paragraph and read it to your partner. C. Read your summary to the class.",
             examples=[D(DLI, DLI_E)]),
        card("Activity 6: the house passage",
             "A. Read the passage and write an appropriate title in Chinese (mine: 我家的房子). B. In your notebook draw a picture of the place described and compare pictures with the class. C. Form groups of three; each student completes one vocabulary list (List 1—Furniture, List 2—Rooms, List 3—Layout) and reads it to the group. My lists are below the passage.",
             examples=[D(HOUSE, HOUSE_E)],
             tables=[table(["List", "From the passage (mine)"], [("List 1—Furniture", "沙发、咖啡桌、饭桌、椅子、办公桌、书架、电脑、双人床、床头柜、躺椅、衣橱"), ("List 2—Rooms", "客厅、厨房、饭厅、书房、卫生间、卧室、主卧室、阁楼、活动室、地下室、车库"), ("List 3—Layout", "三层楼；前边是小花园，后边是大院子；客厅的对面是厨房，厨房的旁边是饭厅；客厅的左边是书房；二楼有三个卧室；三楼是阁楼；还有地下室和车库")], title="Vocabulary lists", say=[1])]),
        card("Activity 7: 外国人也能在中国“扫码”",
             "A. Read the headline of the news article (中国网事—外国人在中国, written by 王武). What new development do you think the article is reporting? Compare answers with a partner. The book prints digits (20%, 2018, 95万); they are spelled out here. Reference: xinhuanet.com.",
             examples=[D(NEWS, NEWS_E)]),
        card("Activity 7 B and the statements",
             "B. Read the article again and mark the statements true or false. The book’s statement 3 runs on into the line numbered 4 (the numbering glitches), so there are six statements; the answers are mine from the article: 1. 以前外国人在中国不能扫码支付。 (True: they often could not register.) 2. 现在外国人可以很方便地在中国使用国外银行卡付款。 (True.) 3. 中国人只要看外国人是用“扫码”支付，还是现金、刷卡支付，就可以知道他们来中国多长时间了。 (True, as the article puts it.) 4. 琳达一到中国，就学会了“扫码”支付。 (False: her first time she had no way to use it.) 5. 大多数的外国人说不能用手机支付是他们在中国最大的麻烦。 (False: it is twenty percent.) 6. 现在在中国的外国人已经习惯了手机支付，连学费和房租也用扫码支付。 (True.) C. Translate the sentences below, two for you and two for your partner, then review each other’s work. My translations:",
             examples=[D(z, e) for z, e in NEWS_T]),
    ],
    exercises=[
        M("What time does the DLI student fall in each morning?", "六点半", ["七点四十五", "九点半", "十点"], "每天早上六点半集合。"),
        M("How many classes does he have a day?", "Six", ["Four", "Seven", "Eight"], "上六节课."),
        M("When do classes start?", "7:45 in the morning", ["6:30 in the morning", "2:50 in the afternoon", "9:30 in the morning"], "早上七点四十五分上课。"),
        M("When do classes end?", "2:50 in the afternoon", ["7:45", "10:00 at night", "12:00 noon"], "下午两点五十下课。"),
        M("What does he do after class in the afternoon?", "Exercises on the drill field", ["Goes to the library", "Watches a movie", "Goes to the bank"], "下午下课以后我们去操场锻炼身体。"),
        M("When does he usually get to bed?", "After ten", ["At eight", "At nine", "At noon"], "我常常十点以后才能睡觉。"),
        M("What does he like about the weekends?", "He has time to do what he wants", ["No homework at all", "Classes are shorter", "He sleeps all day"], "有时间可以做我想做的事情。"),
        M("Where does the student go on Sunday night, and why?", "The library, because there is class on Monday", ["The gym, to exercise", "A restaurant", "The seaside"], "星期天晚上我常常去图书馆做作业，因为星期一要上课。"),
        M("In the house passage, what is planted in the front garden?", "Many pretty flowers", ["Vegetables and fruit trees", "Only grass", "Nothing"], "里边种着很多漂亮的花。"),
        M("What color is the front door?", "Red", ["Light yellow", "Dark brown", "Blue"], "大门是红色的。"),
        M("Why is the living room bright?", "There are four big windows on the back wall", ["There is no roof", "The walls are white", "It has many lamps"], "后墙上有四个大窗户，所以客厅很明亮。"),
        M("Where is the narrator’s room?", "On the third floor, in the attic", ["On the second floor", "In the basement", "Next to the study"], "我的房间在三楼，三楼是一个阁楼。"),
        M("What is the basement used for?", "A gym and game room", ["Parking", "A study", "A kitchen"], "地下室是我们的健身房和游戏室。"),
        M("What does the father like doing in the garage?", "Woodworking", ["Cooking", "Painting", "Playing games"], "他最喜欢在那儿做木工。"),
        M("What new development does the news article report?", "WeChat Pay and Alipay can be linked to foreign bank cards", ["Cash is no longer accepted", "Foreigners must leave China", "Banks have closed"], "支付宝、微信支付可以跟国外银行卡绑定。"),
        M("How many foreigners worked in China in 2018, according to the article?", "九十五万", ["二十万", "五万", "九百万"], "二零一八年…九十五万人。"),
        M("What percentage of foreign netizens said they couldn’t pay by phone like the Chinese?", "百分之二十", ["百分之九十五", "百分之五", "百分之五十"], "百分之二十的外国网友."),
        M("Who helped Mark turn on mobile payment?", "His two Chinese roommates", ["His teacher", "His mother", "A bank clerk"], "我的两位中国室友帮助我开通了移动支付。"),
        mean("集合", "ji2 he2", "to fall in (military formation)", ["to go online", "to give a discount", "to open an account"]),
        mean("值班", "zhi2 ban1", "to be on duty", ["to take a walk", "to scan a code", "to sign a contract"]),
        F("我们每天早上六点半___合。", "集", PART, "集合: fall in."),
        F("我们的房子还有一个地下室和一个车___。", "库", PART, "车库: garage."),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context review
QS = [("每天早上几点起床？几点集合？", "What time do you get up every morning? What time do you fall in?"), ("每天几点上课，几点下课？中午在哪儿吃午饭？", "What time do classes start and end every day? Where do you eat lunch?"), ("每天上几节课？上午几节课？下午几节课？", "How many classes a day? How many in the morning? How many in the afternoon?"), ("每天都有什么课？", "What classes are there every day?"),
      ("每天的作业多不多？需要多长时间做完作业？", "Is there a lot of homework every day? How long does it take to finish?"), ("考试多不多？都有什么考试？考得怎么样？", "Are there many tests? What tests are there? How did you do?"), ("周末几点起床？几点睡觉？", "What time do you get up and go to bed on weekends?"), ("星期六常常做什么？", "What do you often do on Saturdays?"),
      ("星期天常常做什么？", "What do you often do on Sundays?"), ("有没有其它想要让你父母知道的？", "Is there anything else you want your parents to know?")]
AD = [("房子在哪儿？房子有几层楼？什么颜色？", "Where is the house? How many floors does it have? What color is it?"), ("出租的房间每月房租是多少？包不包水电费，上网费？", "How much is the monthly rent for the room? Are water, electricity and internet included?"), ("房子的外面什么样？有没有院子？院子里种着什么？", "What does the outside look like? Is there a yard? What is planted in it?"), ("房子有几个卧室？你的卧室, 你朋友的卧室, 房客的卧室都在哪儿？", "How many bedrooms? Where are your bedroom, your friend’s bedroom and the tenant’s bedroom?"),
      ("房客的卧室带不带家具？如果带家具，都有什么？", "Does the tenant’s bedroom come with furniture? If so, what?"), ("房客可不可以在厨房做饭？如果可以，你有什么厨具？", "May the tenant cook in the kitchen? If so, what kitchenware do you have?"), ("如果房客喜欢你的房子，什么时候可以住进来？", "If the tenant likes your house, when can they move in?"), ("要不要付押金？付多少押金？", "Is a deposit required? How much?"),
      ("你要找什么样的房客？哪国人？男的还是女的？做什么工作？", "What kind of tenant are you looking for? Which nationality? Male or female? What job?"), ("联系人是谁？联系电话号码是多少？", "Who is the contact person? What is the contact phone number?")]
L5 = lesson(
    "Lesson 12 (Unit 2 review): using Chinese in context review",
    "生活如何？ · 同乐会菜单 · 买礼物 · 出租启事 · 银行和微信支付",
    requires=[],
    cards=[
        card("Activity 1: life at DLI",
             "A. A Chinese friend emails you (the subject is 生活如何？) to ask about life at DLI and lists ten questions. B. Ask a partner the questions in the email and write their answers. C. Write an email in pinyin or characters to answer your friend. The ten questions:",
             examples=[D(z, e) for z, e in QS]),
        card("Activity 2: a Chinese potluck",
             "A. Form groups of three to plan a Chinese potluck for your class. In Chinese, brainstorm a menu and write at least three items for each category: 1. 饮料, 2. 餐具, 3. 主食, 4. 菜 (with its 特色: 味道, 地方, 民族等), 5. 水果, 6. 甜点. B. With another group, combine your two menus into a final menu and present it to the class on butcher block paper."),
        card("Activity 3: role play at the department store",
             "A. You are working in Shanghai but want to celebrate Christmas in the U.S. Before leaving, you buy gifts for your family at a department store; your partner plays the sales associate. B. Switch roles and repeat. The customer may buy: 衣服, 皮鞋, 领带, 衬衫, 西装, 袜子, 裤子, 围巾, 毛巾, 牙刷, 牙膏, 书包, 笔记本, 圆珠笔, 其它; and may ask the sales associate: 1. 每个东西多少钱 2. 有没有打折、促销或是优惠. The sales associate may ask the customer: 1. 衣服的颜色: 蓝色, 黑色, 红色等 2. 衣服的大小: 小号, 中号, 大号 3. 穿多大号码的鞋 4. 怎么付钱: 现金, 信用卡, 微信."),
        card("Activity 4: a rental ad",
             "A. Pair up. You and a MIIS classmate rent a house and want to share it with a Chinese student. Write a rental ad in Chinese on butcher block or a large sheet of paper, addressing these ten questions. B. Post the ad on the classroom wall and read other pairs’ ads. C. With a different partner, role-play the MIIS housemate while your partner plays the Chinese student who calls about your room for rent. D. Switch to a third partner and play the Chinese student. The questions:",
             examples=[D(z, e) for z, e in AD]),
        card("Activity 5: banking at the Chinese University of Hong Kong",
             "You are nearing completion of a one-year Education Abroad Program at the Chinese University of Hong Kong. The EAP director asks you to make a Chinese PowerPoint presentation for next year’s students to show them how to open a bank account, register for online banking, and use WeChat Pay. A. Divide into three groups: Group A lists the steps for opening a bank account (怎么开银行账户; 怎么把美元换成人民币), Group B the steps for setting up online accounts and banking services (怎么注册网上银行; 介绍网上银行业务), and Group C the steps for using WeChat Pay (怎么注册移动支付). B. Present your work to the class in Chinese and explain the benefits of using these services. C. Consolidate the work of all three groups into one PowerPoint."),
    ],
    exercises=[
        M("What does 周末几点起床？ ask?", "What time do you get up on weekends?", ["What do you eat on weekends?", "Where do you go on weekends?", "Who do you see on weekends?"], "起床: get up."),
        M("What does 考得怎么样？ ask?", "How did you do on the test?", ["When is the test?", "Is the test hard?", "Where is the test?"], "考得怎么样: how did you do."),
        M("What does 包不包水电费？ ask?", "Are water and electricity included?", ["Is the room big?", "Is the rent expensive?", "Is there a yard?"], "包: include."),
        M("What does 带不带家具？ ask?", "Does it come with furniture?", ["Is it near the bank?", "Is it a new house?", "Is there a garage?"], "带家具: with furniture."),
        M("What does 要不要付押金？ ask?", "Is a deposit required?", ["Is the rent paid?", "Is a contract needed?", "Is there a parking space?"], "押金: deposit."),
        M("Which is a category of the potluck menu?", "甜点", ["作业", "操场", "大门"], "饮料, 餐具, 主食, 菜, 水果, 甜点."),
        M("In the department-store role play, who asks 穿多大号码的鞋？", "The sales associate", ["The customer", "The bank clerk", "The landlord"], "The 营业员 asks about shoe size."),
        M("Which means “payment methods” the sales associate may ask about?", "现金, 信用卡, 微信", ["蓝色, 黑色, 红色", "小号, 中号, 大号", "皮鞋, 领带, 衬衫"], "怎么付钱."),
        M("What are the three groups in Activity 5?", "Opening an account, online banking, and WeChat Pay", ["Rent, food and school", "Shopping, housing and banking", "Menus, ads and emails"], "Group A, B, C."),
        mean("促销", "cu4 xiao1", "sales promotion", ["to book", "to scan a code", "to get used to"]),
        mean("押金", "ya1 jin1", "deposit", ["rent", "bill", "cash"]),
        F("你要找什么样的房___？", "客", PART, "房客: tenant."),
    ],
)

UNIT = unit("第十二课 单元复习课 Unit 2 review: activities", [L1, L2, L3, L4, L5])
