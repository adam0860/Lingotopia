"""Unit 52: Lesson 18 (Unit 3 review) activities, part 2: skills integration review (the airport dialogs, the Pudong entry procedures, the
San Francisco blog post, the gym advertisements, the DLI teacher's journal and the two families) and using Chinese in context review.
Everything readable in the book is here; the audio activities, the pictures, the videos and the web links are not. Where the book leaves a
table, a cloze or an answer open, the answers are mine and labeled."""
from zh_auto import *

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("长大", 0, "zhang3"), ("得到后面", 0, "dei3"), ("得走", 0, "dei3"), ("种花", 0, "zhong4"), ("种草", 0, "zhong4"), ("她种的", 1, "zhong4"), ("睡觉", 1, "jiao4"), ("睡着", 1, "zhao2"), ("没有", 0, "mei2"), ("没见", 0, "mei2"), ("教练", 0, "jiao4"),
                          ("都会", 0, "dou1"), ("坐不上", 2, "shang4"), ("好吃", 0, "hao3"), ("看护照", 0, "kan4"), ("难得", 1, "de2"), ("取得", 1, "de2")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. skills integration: the airport dialogs
AD1 = [("机场地勤", "小姐，下午好！请问您要办理登机手续吗？", "Miss, good afternoon! Do you want to check in?"), ("乘客", "你好。对，我要办理登机手续。我的飞机好像还有一个小时就要起飞了。可不可以请你办快点儿？", "Hello. Yes, I want to check in. My plane seems to take off in an hour. Could you please be quick?"), ("机场地勤", "我试试。请问您要飞往哪里呢？", "I’ll try. Where are you flying to?"), ("乘客", "飞往上海。", "To Shanghai."),
       ("机场地勤", "请出示您的电子机票和护照。", "Please show your e-ticket and passport."), ("乘客", "好的，这是我的电子机票，在手机上。这是我的护照。", "OK, this is my e-ticket, on my phone. This is my passport."), ("机场地勤", "好，我看一下。请问您要靠窗户的座位还是靠过道的座位？", "OK, let me look. Would you like a window seat or an aisle seat?"), ("乘客", "我喜欢靠窗户的座位，可以看到外面的景色。", "I like a window seat so I can see the view outside."),
       ("机场地勤", "好的。您是飞往上海的三二二号航班。座位号是四十二Ａ。这是您的登机牌。", "OK. You are on flight 322 to Shanghai. Your seat number is 42A. Here is your boarding pass. (the book writes 322 and 42A in digits and letters)"), ("乘客", "请问几点登机呢？", "What time is boarding?"), ("机场地勤", "登机的时间为下午四点。", "Boarding is at four p.m."), ("乘客", "太好了。对了，我还有两件行李需要托运。", "Great. Oh, I also have two pieces of luggage to check."),
       ("机场地勤", "对不起小姐。我们的行李托运服务在登机前一小时关闭。现在不能办理托运。", "Sorry, miss. Our baggage check service closes an hour before boarding. We can’t check luggage now."), ("乘客", "哎呀，那我怎么办啊！我能带上飞机吗？", "Oh no, what do I do! Can I take it on the plane?"), ("机场地勤", "不行。上飞机只能带一件随身行李。", "No. You can only bring one carry-on piece on the plane."),
       ("乘客", "那，这件小的我随身带。这件大的请您帮我办一下托运。我真地没有很多时间了。", "Then I’ll carry this small one with me. Please check this big one for me. I really don’t have much time. (the book writes 真地)"), ("机场地勤", "好吧。就这一次。下次您一定要早来机场。", "All right. Just this once. Next time you must come to the airport early."), ("乘客", "好的好的，我一定早来。请问，我需要从几号登机口登机呢？", "Yes, yes, I will definitely come early. Which gate do I board from?"),
       ("机场地勤", "您的航班从十五号登机口起飞。", "Your flight departs from Gate 15."), ("乘客", "谢谢！", "Thank you!"), ("机场地勤", "祝您旅途愉快！", "Have a pleasant trip!")]
AD2 = [("机场安检", "小姐，你得到后面去排队等候安检。你看，大家都在排队。", "Miss, you have to go to the back and line up for security. See, everyone is in line."), ("乘客", "对不起啊，我的航班还有四十分钟就要起飞了。我可不可以先安检啊？", "Sorry, my flight takes off in forty minutes. Can I go through security first?"), ("机场安检", "这样啊，你跟我来。你得走快速通道。这边就是。", "I see; come with me. You have to take the fast lane. It’s over here."),
       ("乘客", "太感谢你啦。", "Thank you so much."), ("机场安检", "在这个快速通道，你只要让我们的机器扫一下你的脸，机器识别后，你就可以通过安检。这是我们机场最新的“刷脸”安检服务。", "In this fast lane, you only have to let our machine scan your face, and after the machine recognizes you, you can pass security. This is our airport’s newest “face-scan” security service."), ("乘客", "真是太方便了。我就站在这儿让机器刷脸吗？", "That’s really convenient. Do I just stand here and let the machine scan my face?"),
       ("机场安检", "对，已经通过了。你可以往前走了。", "Yes, you’ve already passed. You can go ahead."), ("乘客", "你不需要看护照和登机牌吗？", "Don’t you need to look at my passport and boarding pass?"), ("机场安检", "不需要。同时，快速通道也不需要你打开行李检查。", "No need. At the same time, the fast lane doesn’t need you to open your luggage for inspection either."),
       ("乘客", "这是我第一次走快速通道和使用刷脸安检。太快了。对了，请问十五号登机口怎么走？", "This is my first time using the fast lane and the face-scan security. So fast. By the way, how do I get to Gate 15?"), ("机场安检", "从这儿往右拐，往前走五十米，你会看到很多商店、小卖部和饭馆。在星巴克咖啡馆的旁边，有一个下楼的电梯。从电梯出去，就是十到二十号登机口的候机室。左边的第五个登机口就是十五号登机口。", "From here turn right and walk forward fifty meters; you will see many shops, kiosks and restaurants. Next to the Starbucks coffee shop there is an elevator down. Going out from the elevator is the waiting hall for Gates 10 to 20. The fifth gate on the left is Gate 15."),
       ("乘客", "谢谢，谢谢！今天如果没有你的帮助，我可能坐不上我的飞机了。", "Thank you, thank you! Without your help today I might not have been able to get on my plane."), ("机场安检", "不客气。", "You’re welcome.")]
L1 = lesson(
    "Lesson 18 (Unit 3 review): skills integration review, the airport dialogs",
    "办理登机手续 · 托运行李 · 快速通道 · 刷脸安检",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading): check-in",
             "A. Listen to the dialog once and answer: 1. Where does the dialog take place? What is the second speaker doing there? 2. What is the urgency for the second speaker? 3. What trouble is the second speaker having? B. Listen again and answer the detailed questions: 1. Where does the second speaker want to go? 2. What does the first speaker check with the second speaker about? 3. What kind of seat would the second speaker prefer? 4. Provide two details of the second speaker’s flight. 5. What’s the solution for the second speaker’s luggage? 6. Where can the second speaker board the flight? C. Read the script together; share how you usually check in at airports. (Audio and two photographs, not included; the script is below.) My answers from the script: at an airport check-in counter, the passenger is checking in; her plane takes off in about an hour; she has two bags to check but baggage check has closed; she wants Shanghai; the agent asks about the seat; she prefers a window seat; flight 322, seat 42A, boarding at four p.m. from Gate 15; one big bag is checked this one time and she carries the small one.",
             examples=dlg(AD1)),
        card("Activity 2 (Listening, Writing, Speaking and Reading): security",
             "A. Listen to the dialog and answer: 1. What is the dialog about? 2. What new service was the second speaker able to use? List three details about the service. B. Draw a diagram in your notebook according to the first speaker’s instructions at the end of the dialog. C. Share your answers with a classmate. D. Read the script and compare your information. (Audio, not included; the script is below.) My answers: the dialog is about getting through airport security; the new service is the face-scan fast lane: you stand while the machine scans your face, you need not show a passport or boarding pass, and you need not open your luggage. The route to Gate 15: turn right, walk fifty meters past shops and restaurants, take the elevator down beside the coffee shop, and Gate 15 is the fifth gate on the left.",
             examples=dlg(AD2)),
    ],
    exercises=[
        M("What does the passenger want to do?", "Check in", ["Buy a ticket", "Rent a car", "Change money"], "我要办理登机手续."),
        M("Where is the passenger flying?", "Shanghai", ["Beijing", "Xi’an", "Chengdu"], "飞往上海."),
        M("What seat does she prefer?", "A window seat", ["An aisle seat", "A seat in the back", "A seat by the door"], "我喜欢靠窗户的座位."),
        M("When does boarding start?", "Four p.m.", ["Three p.m.", "Five p.m.", "Noon"], "登机的时间为下午四点."),
        M("Why can’t she check her luggage normally?", "The service closes an hour before boarding", ["She has no ticket", "The bags are too heavy", "It is a holiday"], "行李托运服务在登机前一小时关闭."),
        M("How many carry-on pieces can she take on the plane?", "One", ["Two", "Three", "None"], "只能带一件随身行李."),
        M("Which gate does her flight leave from?", "Gate 15", ["Gate 10", "Gate 20", "Gate 5"], "十五号登机口."),
        M("What is the new service in the second dialog?", "A face-scan fast lane for security", ["A free taxi", "A luggage robot", "A language guide"], "刷脸安检."),
        M("What does she not need to show in the fast lane?", "Her passport and boarding pass", ["Her face", "Her phone", "Her ticket money"], "不需要看护照和登机牌."),
        M("Where is the elevator down to Gates 10 to 20?", "Next to the Starbucks coffee shop", ["Next to the bank", "Behind the gate", "At the entrance"], "在星巴克咖啡馆的旁边."),
        M("Which gate is the fifth on the left?", "Gate 15", ["Gate 5", "Gate 20", "Gate 10"], "左边的第五个登机口就是十五号登机口."),
        F("请出示您的电子机票和___照。", "护", PART, "护照: passport."),
        F("你只要让我们的机器扫一下你的脸，机器识别后，你就可以通过安___。", "检", PART, "安检: security check."),
        F("今天如果没有你的帮助，我可能坐不___我的飞机了。", "上", PART, "坐不上: unable to get on."),
    ],
)

# ------------------------------------------------------------------ 2. skills integration: Activities 3-6
STEPS = table(["步骤", "上海浦东机场入关流程 (my summary)"],
              [["1. 航班到达", "飞机到了以后，跟着指示牌走到检验检疫的地方"], ["2. 检验检疫", "检查体温，需要的话填写健康表"], ["3. 边防检查", "排队出示护照和签证，边防检查人员检查"], ["4. 提取行李", "到行李转盘去找自己的行李"], ["5. 海关检查", "没有东西要报关就走绿色通道，有就走红色通道"], ["6. 离开机场", "过了海关就可以离开机场，坐地铁或出租车"]],
              title="Activity 6: the entry procedure at Shanghai Pudong Airport (the book prints six signs as pictures, so this summary is mine and general)", say=[0, 1])
L2 = lesson(
    "Lesson 18 (Unit 3 review): skills integration review, Activities 3 to 6",
    "旅行视频 · 周先生周太太的礼物 · 补充词汇 · 上海浦东机场入关流程",
    requires=[],
    cards=[
        card("Activity 3 (Listening, Speaking and Reading): the travel video",
             "Form groups of three. Watch a video online and complete the tasks. A. Watch the first segment (0:00–2:06) and the last segment (6:46–end) together or individually and answer: 1. What is the video about? 2. What different topics does the speaker describe in the video? List all the topics. 3. What is the last segment about? What does the speaker suggest travelers do, and why? B. Share your answers with your group members. C. Individually, each student watches a different segment (Student A 2:06–2:53; Student B 2:53–4:46; Student C 4:46–6:46) and completes a table with 景点, 活动, 餐饮, 买票 and 其它. D. Share your information with your partners and take notes. E. Together, complete the 旅行计划 (a table with 目的地, 为什么去那儿, 景点&活动 for 第一天, 第二天 and 第三天, and then 买票, 餐饮, 交通 and 住宿). F. Share your completed travel plan with the class. Do you think this is a good travel plan? (The video and its link are not included.)"),
        card("Activity 4 (Listening, Speaking and Reading): a visit to a friend",
             "A. Use the images to predict what you will hear in the dialog. B. Listen to the dialog and select the correct answers: 1. What kinds of gifts did Mr. Zhou and Mrs. Zhou bring for their friend? (Flowers / A painting / Tea) 2. What kind of food did Li Ming and his wife like? (Cantonese / Sichuan / Shanghai food) 3. Which of the following is FALSE about Li Ming’s neighborhood? (It’s not only beautiful, but also very convenient. / It’s close to restaurants, supermarkets, a gas station and the ocean. / It’s a bit far from his friend’s house.) 4. What did Li Ming do to his new house? (Added a reading room. / Bought some furniture. / Replaced the carpet on the first floor with wooden flooring.) 5. What does Mrs. Li prefer? (To chat with friends in the living room. / To cook alone in the kitchen. / To show her friends around the house.) C. Pair up and share your answers. D. Read the script and check your information with the class. E. With your partner, share a gathering you recently attended. (This is a listening activity; the audio and the script are not in the book’s text, so there is no key.)"),
        card("Activity 5 (Listening, Writing, Reading and Speaking): supplementary words",
             "A. Before listening, work with a classmate to guess the meaning of these words, then look them up and write them in pinyin with tone marks and their English meanings: 补充词汇 宅男, 白马王子, 睡袋. B. In groups of three, listen to three speakers talk about their casual or sports activities; each student listens to one speaker and writes a summary. C. After listening, exchange information and match each speaker to one of three images. D. Read the scripts and check. E. Compare all the stories and tell each other whose story you liked the most. (Audio and pictures, not included.) My look-ups: 宅男 zhái nán, “homebody guy; a man who stays home”; 白马王子 báimǎ wángzǐ, “Prince Charming; a girl’s dream partner”; 睡袋 shuìdài, “sleeping bag”."),
        card("Activity 6 (Reading, Writing, Speaking and Listening): arriving in Shanghai",
             "Read the procedures for foreign travelers arriving at Shanghai Pudong International Airport and complete the tasks. A. After you arrive, you see six signs (pictures, not included). Pair up and discuss what each sign means and what you should do at each step. B. Each partner reads three steps and summarizes the main points of each step in Chinese characters or pinyin in the table: 上海浦东机场入关流程 (一): 1. 航班到达, 2. 检验检疫, 3. 边防检查; (二): 4. 提取行李, 5. 海关检查, 6. 离开机场. C. Exchange information with your partner. D. Share your answers with the class. My summary of the six steps:",
             tables=[STEPS]),
    ],
    exercises=[
        M("Which step comes first when you arrive at Pudong Airport?", "航班到达", ["离开机场", "提取行李", "海关检查"], "Step 1."),
        M("Which step comes between 边防检查 and 海关检查?", "提取行李", ["航班到达", "离开机场", "检验检疫"], "Steps 3, 4, 5."),
        M("Which step is the last?", "离开机场", ["边防检查", "海关检查", "提取行李"], "Step 6."),
        M("What do you show at 边防检查?", "Your passport and visa", ["Your bank card", "Your hotel booking", "Your photograph"], "Border check."),
        M("What is 睡袋?", "A sleeping bag", ["A handbag", "A backpack", "A pillow"], "睡袋 = sleeping bag."),
        M("What is 白马王子?", "Prince Charming", ["A white horse", "A king", "A soldier"], "白马王子 = Prince Charming."),
        M("What is 宅男?", "A man who stays home", ["A famous man", "A tour guide", "A taxi driver"], "宅男 = homebody."),
        M("Where does 海关检查 take place?", "At customs", ["At a hotel", "At a bank", "At a market"], "海关 = customs."),
        F("上海浦东机场入关流程的第四步是提___行李。", "取", PART, "提取行李: claim luggage."),
        F("没有东西要报关的人，可以走绿色通___。", "道", PART, "通道: lane."),
    ],
)

# ------------------------------------------------------------------ 3. blog post and gym ads
BLOG = ["说到这次到美国的旅行，我们旅行的第一站是旧金山。当天到达旧金山的时候是早上的九点半，我们没有休息，就直接去了第一个目的地——渔人码头。", "旧金山的渔人码头离市区很近，交通非常方便，也是每个去旧金山的游客一定会去的地方，而且那儿的海鲜真的很好吃！我们吃饭的餐馆在码头上，从窗户就可以看到著名的金门大桥，而且还可以看到附近成群的海狮。这是我第一次看到海狮，它们懒洋洋地晒着太阳，显得非常舒服，只是不知道它们喜不喜欢被人看的感觉。渔人码头这边的街头还有很多商店，可以逛逛。",
        "然后我们去看了金门大桥，这座大桥已经成了美国一个著名的景点。在桥上有很多可以拍照的地方，我们在桥上看到的景色非常美。沿着桥边往下走，可以看到大桥、沙滩和海水。我们还在海风中散了一个小时的步。", "第二天，我们去了旧金山的唐人街，也就是中国城。旧金山的唐人街是美国西部最大的，和纽约的唐人街差不多，街头都是汉字，两边有很多的中国饭馆、商店、书店和茶店什么的。唐人街有不少地道的中餐，我们选了一家最老的广东饭馆，吃了广式点心、喝了广东早茶。",
        "后来，我们又去了比较有名的九曲花街，我在网上看到过很多这条街的照片，所以就对这条街非常感兴趣。九曲花街，就是一条有很多花的街，景色很特别。两边的房屋有公寓、有单栋楼，每个房子都有自己的特色，高度、颜色和大门都不同。", "下次要是再去旧金山，我们打算去一些有名的酒吧喝喝酒或是坐市内观光车看看别的名胜古迹和街道。"]
BLOG_E = ["1. Speaking of this trip to America, the first stop of our trip was San Francisco. We arrived in San Francisco at nine-thirty in the morning that day, and without resting we went straight to the first destination, Fisherman’s Wharf.", "2. Fisherman’s Wharf in San Francisco is very close to downtown and transportation is very convenient; it is a place every tourist to San Francisco is sure to go, and the seafood there is really delicious! The restaurant where we ate was on the pier, and from the window you could see the famous Golden Gate Bridge and also the herds of sea lions nearby. It was my first time seeing sea lions; they lazily bask in the sun and look very comfortable, but I don’t know whether they like being looked at. On the streets by the Wharf there are also many shops to browse.",
          "3. Then we went to see the Golden Gate Bridge, which has become a famous American sight. There are many photo spots on the bridge and the scenery we saw from it was very beautiful. Walking down along the side of the bridge, you can see the bridge, the beach and the sea. We also strolled for an hour in the sea breeze.", "4. On the second day we went to San Francisco’s Chinatown. San Francisco’s Chinatown is the largest in the western U.S. and similar to New York’s; the streets are full of Chinese characters, and on both sides are many Chinese restaurants, shops, bookstores, tea shops and so on. Chinatown has quite a lot of authentic Chinese food; we chose the oldest Cantonese restaurant and had Cantonese dim sum and Cantonese morning tea.",
          "5. Later we went to the rather famous Lombard Street (“Nine-Bend Flower Street”). I had seen many photos of this street online, so I was very interested in it. It is a street with a lot of flowers and special scenery. The houses on both sides include apartments and single buildings; each has its own character, with different heights, colors and doors.", "6. Next time we go to San Francisco, we plan to go to some famous bars for a drink or take a city sightseeing bus to see other sights and streets."]
ITIN = table(["段落", "时间", "景点", "活动"],
             [["第一段", "第一天早上九点半", "渔人码头", "没有休息，直接去"], ["第二段", "第一天", "渔人码头", "吃海鲜，看海狮，逛街头的商店"], ["第三段", "第一天", "金门大桥", "拍照，沿着桥边走，在海风中散步一个小时"], ["第四段", "第二天", "唐人街（中国城）", "吃广式点心，喝广东早茶"], ["第五段", "后来", "九曲花街", "看花和不同的房子，拍照"], ["第六段", "下次", "有名的酒吧，市内观光车", "喝酒，看别的名胜古迹和街道"]],
             title="畅游旧金山日程表 (my itinerary; the book leaves the table blank)", say=[0, 1, 2, 3])
AD_A = table(["阳光健身房", "Details"],
             [["健身 | 游泳 | 减肥 | 瑜伽 | 球类", ""], ["先在加入 VIP 可有半价优惠", "年卡 999 元，季卡 299 元"], ["专业教练 1 对 1 私人课程", ""], ["集体大班或小班课程", ""], ["比赛级温水游泳池 2 个", ""], ["瑜伽大师亲自讲课", ""], ["最新锻炼器械（举重、跑步）", ""], ["环境优美，空间大", ""], ["交通方便，每人一个车位", ""], ["电话", "13813845454"], ["地址", "北京市朝阳区新星大道 5 楼 502"]],
             title="Advertisement 1: 阳光健身房 (the book prints “先在加入”)")
AD_B = table(["达力健身俱乐部", "Details"],
             [["健身 | 举重 | 球类 | 家庭运动 | 24 小时营业", ""], ["新会员加入，第一个月免费", "器械年卡 888 元；家庭卡 1280 元"], ["超级服务，各种课程", ""], ["高档设施：跑步机、划船机、举重", ""], ["冷水、温水游泳池、儿童泳池", ""], ["适合家庭的运动（游泳、篮球、网球）", ""], ["女士减肥操课、舞蹈课", ""], ["电影、电视随你看", ""], ["淋浴房、休息室", ""], ["电话", "010-8324-7688"], ["地址", "北京市海淀区大学路 239 号 15 栋"]],
             title="Advertisement 2: 达力健身俱乐部")
L3 = lesson(
    "Lesson 18 (Unit 3 review): skills integration review, the San Francisco blog and the gym advertisements",
    "畅游旧金山 · 旅行日程表 · 阳光健身房 vs 达力健身俱乐部",
    requires=[],
    cards=[
        card("Activity 7 (Reading, Writing, Speaking and Listening): 畅游旧金山",
             "Read the following post from a Chinese blogger and complete the tasks. A. Read the title of the blog post and predict what you will read about; in Chinese, share your prediction with a classmate. B. Work in groups of three. Each group member reads two paragraphs and takes notes of the blogger’s itinerary in the table, using Chinese characters or pinyin (段落, 时间, 景点, 活动 for Paragraphs 1–6). C. Ask for information from your partners to complete the itinerary. D. Post your complete itinerary online and share with the class. The post (the book credits it as adapted from a travel website, and prints “改遍”) in six paragraphs; the blank table is filled in by me below.",
             examples=[D(z, e) for z, e in zip(BLOG, BLOG_E)], tables=[ITIN]),
        card("Activity 8 (Reading, Writing, Speaking and Listening): join a gym",
             "You and your partner would like to join a gym or a fitness club. Read the advertisements (below) and complete the tasks. A. Each student writes what they need to consider when joining a gym or fitness club; make a list of your requirements and considerations. B. Pair up and share your list. C. As a pair, each partner reads one advertisement and highlights the information the other partner thinks is important, then shares it. D. Ask questions about the advertisement your partner reads if you need to learn more; then decide which gym or fitness club you would like to join and explain why. E. Share your decisions with the class. (The ads are printed with photos, not included.)",
             tables=[AD_A, AD_B]),
    ],
    exercises=[
        M("Where did the blogger go first in San Francisco?", "Fisherman’s Wharf", ["Chinatown", "Lombard Street", "The Golden Gate Bridge"], "第一个目的地——渔人码头."),
        M("What time did they arrive?", "Nine-thirty in the morning", ["Noon", "Evening", "Six a.m."], "早上的九点半."),
        M("What animals did they see near the wharf?", "Sea lions", ["Dolphins", "Pandas", "Seals in a zoo"], "成群的海狮."),
        M("What did the sea lions do?", "Lazily basked in the sun", ["Swam fast", "Barked loudly", "Ran away"], "懒洋洋地晒着太阳."),
        M("What did they do on the Golden Gate Bridge?", "Took photos and strolled for an hour", ["Rented a boat", "Swam", "Ate dinner"], "拍照…散了一个小时的步."),
        M("Where did they go on the second day?", "Chinatown", ["Disneyland", "A museum", "A ski resort"], "第二天，我们去了旧金山的唐人街."),
        M("What did they eat in Chinatown?", "Cantonese dim sum and Cantonese morning tea", ["Sichuan hot pot", "Pizza", "Sushi"], "广式点心、广东早茶."),
        M("Why were they interested in Lombard Street?", "They had seen many photos of it online", ["A friend lives there", "It is cheap", "It is near the hotel"], "我在网上看到过很多这条街的照片."),
        M("What do they plan for next time?", "Bars and a sightseeing bus tour", ["A cruise", "Camping", "Skiing"], "酒吧…市内观光车."),
        M("Which gym offers the first month free to new members?", "达力健身俱乐部", ["阳光健身房", "Both", "Neither"], "新会员加入，第一个月免费."),
        M("Which gym has a parking space for every member?", "阳光健身房", ["达力健身俱乐部", "Both", "Neither"], "每人一个车位."),
        M("Which gym is open twenty-four hours?", "达力健身俱乐部", ["阳光健身房", "Both", "Neither"], "24 小时营业."),
        F("我们吃饭的餐馆在码头上，从窗户就可以看到___名的金门大桥。", "著", PART, "著名: famous."),
        F("这些人不是来游览的游客就是在做运动的当___人。", "地", PART, "当地人: locals."),
    ],
)

# ------------------------------------------------------------------ 4. journal and two families
DLI = ["上个周末是一个长周末，所以我们请了一些朋友到家里来聚一聚。星期六那天是个阳光灿烂、风和日丽的日子，气温大约七十华氏度，不冷不热，非常适合聚会。我们大概请了十几个朋友，他们有的带来了自己的孩子，有的带来了男朋友或女朋友，甚至有的还把爸妈也带来了，一下子我们家后院到处都是人，热闹极了。",
       "我和太太准备了餐具、桌子、椅子和一些饮料、果汁和冰块。在客人们到以前，我已经把烧烤的东西准备好了，烤羊肉和烤鸡腿、鸡翅是我的拿手菜。我太太还亲自做了一个苹果派作为大家的甜点。", "马克和他的女朋友带来了一些啤酒和热狗。张林和他的爸妈准备了很多中式的食品：烧牛肉、鸡蛋饼和饺子。我太太的同学安娜买了两大盒水果，有草莓、菠萝、西瓜等等，另外她还做了一个意大利面。",
       "大家都到了以后，我们把所有的饭菜、酒、饮料、水果、餐具等摆到了桌子上，然后大家就开始一边吃、一边喝、一边聊天。在大家吃着的时候，我还忙着我的烧烤，因为我想给大家吃热的烤肉。孩子们很快就吃好了，然后他们就在院子里的草地上跑来跑去地玩。我们大人们则围坐在桌边，开心地喝酒聊天。大家一直玩到下午五点才回家。"]
DLI_E = ["1. Last weekend was a long weekend, so we invited some friends to our home to get together. Saturday was a sunny, bright and pleasant day, with a temperature of about seventy degrees Fahrenheit, neither cold nor hot, perfect for a party. We invited about a dozen or so friends; some brought their own children, some brought boyfriends or girlfriends, and some even brought their parents too, so all at once our backyard was full of people everywhere, extremely lively.",
         "2. My wife and I prepared tableware, tables, chairs and some drinks, juice and ice cubes. Before the guests arrived I had already gotten the barbecue things ready; grilled lamb, grilled chicken legs and wings are my specialties. My wife also personally made an apple pie as everyone’s dessert.", "3. Mark and his girlfriend brought some beer and hot dogs. Zhang Lin and his parents prepared lots of Chinese food: braised beef, egg pancakes and dumplings. My wife’s classmate Anna bought two big boxes of fruit, including strawberries, pineapple, watermelon and so on, and she also made a pasta dish.",
         "4. After everyone had arrived, we set all the dishes, wine, drinks, fruit and tableware on the table, and then everyone began eating, drinking and chatting. While everyone was eating I was still busy with my barbecue because I wanted everyone to eat hot grilled meat. The children finished eating quickly, then ran around playing on the grass in the yard. We adults sat around the table drinking and chatting happily. Everyone played until five in the afternoon before going home. (The book writes 70 as digits.)"]
DTF = [("作者邀请朋友们到他家参加一个生日聚会。", "1. The author invited friends to a birthday party at his home. — False (it was a get-together over the long weekend; key mine)"), ("那天的天气晴朗，不冷不热。", "2. The weather that day was clear, neither cold nor hot. — True"), ("参加聚会的都是作者和他太太的朋友。", "3. Everyone at the party was a friend of the author and his wife. — False (some brought their children and even parents)"), ("作者最喜欢烤牛肉、羊肉和鸡肉，都是他的拿手菜。", "4. The author likes grilling beef, lamb and chicken, all his specialties. — False (his specialties are lamb, chicken legs and wings; no beef)"),
       ("聚会上，安娜带来了水果和甜点，还有意大利面。", "5. At the party Anna brought fruit and dessert, and also pasta. — False (the dessert, an apple pie, was made by the author’s wife)"), ("聚会开始以后，作者和大家一起围着桌子坐下来，边吃边聊。", "6. After the party started, the author sat around the table with everyone eating and chatting. — False (he was busy with the barbecue)"), ("孩子们很饿，他们跟大人们吃得时间一样长。", "7. The children were hungry and ate for as long as the adults. — False (they finished quickly)")]
FAM1 = ["我们家是一个非常中式的家庭，只有三口人，我爸爸、妈妈和我。我爸妈都是爱静不爱动的人，他们喜欢呆在家里，做他们喜欢的事情。", "我妈妈是个家庭主妇，所以她特别喜欢做饭，而且她做的饭也特别好吃。另外，她也喜欢看电视。肥皂剧，她可以一部接一部地看，她不但晚上看，白天有空的时候也看。有时候，甚至还让我陪着她一起看。最近呢，她迷上了用微信跟她的朋友们聊天，视频聊天、语音聊天什么的，她都会。",
        "我爸呢，虽然他也喜欢看电视，但是他更爱看书。在他的书房里有很多书，国内的、国外的都有。因为我爸是医生，所以他也看很多医学的书。除了看书以外，我爸也喜欢在周末的时候跟邻居们或老朋友们一起下下棋，打打牌。我妈害怕我爸出去打牌，因为他打牌可以打两三个小时，甚至忘了回家。可我爸说打牌是他难得的放松的机会。", "对我爸妈来说，他们仅有的运动就是散步。我们小区的对面就是一个大公园，他们喜欢早上或是晚饭后去公园里一边散步一边聊天，有时候也看看广场上的大妈们跳广场舞。",
        "我自己喜欢看电影，常常跟我的同学或朋友们一起去电影院看电影。我们不是看恐怖片，就是看动作片，有时候也看看搞笑片。还有，我也喜欢打游戏。我不但跟同学一起打游戏，而且也在网上跟网友一起打游戏。别的空闲时间，我会去体育馆或学校的操场打打篮球，我也喜欢看美国的职业篮球比赛。"]
FAM1_E = ["Passage 1. Our family is a very Chinese-style family, with only three people: my dad, my mom and me. My parents both love quiet rather than activity; they like to stay at home and do the things they like.", "My mom is a housewife, so she especially likes cooking, and what she cooks is especially delicious. She also likes watching TV. Soap operas she can watch one after another, not only in the evening but also in the daytime when she has time. Sometimes she even makes me watch with her. Recently she has gotten into chatting with her friends on WeChat; video chat, voice chat and so on, she can do all of it.",
          "My dad, although he also likes TV, loves reading even more. In his study there are many books, both domestic and foreign. Because my dad is a doctor he also reads many medical books. Besides reading, my dad also likes to play chess and cards with neighbors or old friends on weekends. My mom worries about his going out to play cards, because he can play for two or three hours and even forget to come home. But my dad says playing cards is his rare chance to relax.", "For my parents, their only exercise is walking. Across from our neighborhood is a big park, and they like to go to the park in the morning or after dinner to walk and chat, and sometimes watch the aunties on the square dance.",
          "I like watching movies myself and often go to the cinema with classmates or friends. We watch either horror movies or action movies, and sometimes comedies. Also I like playing games; I play not only with classmates but also online with online friends. In other free time I go to the gym or the school’s playground to play basketball, and I also like watching American professional basketball games."]
FAM2 = ["我们家有四口人，在美国我们这样的家庭很多。我们家有我爸爸、妈妈、哥哥和我。我们家的人都喜欢玩、喜欢动。", "我爸是个美式足球迷，也就是美国人说的橄榄球迷。他周末的时候不是约朋友一起去打橄榄球，就是喜欢在电视上看橄榄球比赛。有时候他也带着我们全家去现场看球赛，因为比赛现场人山人海，非常热闹。比赛的输赢对他来说没有关系，重要的是可以和那么多球迷一起看球，一起为球队加油，那就是他最开心的事。",
        "在我们家，我妈喜欢去海边散步或跑步。有时候她也喜欢带着我们家的狗一起去散步。只要天气好，她就会出门，因为海边的景色太美，她不想错过。要是我妈不出门，她喜欢在后院里种花、种草，我们家花园里有她种的各种各样的花，美极了。", "我哥是个摇滚迷，他和他的大学同学有一个乐队，平时有空的时候，他们就一起练习、一起参加音乐会的表演。在他的房间里，他收集了很多摇滚明星的海报，墙上贴满了著名乐队的照片。不管是哪个乐队或歌手，他都知道。我很高兴，因为在家里可以常常听到我哥免费的音乐会。",
        "我自己呢，喜欢很多户外活动，比如：冲浪、爬山、滑雪等等。因为我在海边长大，所以从小就喜欢游泳，然后开始学冲浪。我们这个州有很多有名的国家公园，我喜欢和朋友或是家人一起去国家公园爬山。冬天的时候，我们家喜欢一起去滑雪场滑雪。"]
FAM2_E = ["Passage 2. Our family has four people; in America there are many families like ours. In our family there are my dad, my mom, my older brother and me. Everyone in our family likes to play and likes to be active.", "My dad is an American-football fan, that is, a football fan as Americans say. On weekends he either invites friends to play football or likes to watch football games on TV. Sometimes he also takes the whole family to watch games live, because the venue is a sea of people and very lively. Winning or losing doesn’t matter to him; what matters is being able to watch with so many fans and cheer on the team together, and that is his happiest thing.",
          "In our family, my mom likes to walk or run by the sea. Sometimes she also likes to take our dog along for a walk. As long as the weather is good she goes out, because the seaside scenery is so beautiful that she doesn’t want to miss it. If my mom doesn’t go out, she likes to plant flowers and grass in the backyard; in our garden are all kinds of flowers she planted, extremely beautiful.", "My brother is a rock fan; he and his college classmates have a band, and when they have free time they practice together and take part in concert performances together. In his room he has collected many posters of rock stars and the wall is covered with photos of famous bands. No matter which band or singer, he knows them. I’m very glad, because at home I can often hear my brother’s free concerts.",
          "As for me, I like many outdoor activities, such as surfing, mountain climbing and skiing. Because I grew up by the sea, I have liked swimming since childhood and then began to learn surfing. Our state has many famous national parks, and I like to go hiking in national parks with friends or family. In winter our family likes to go skiing together at a ski resort."]
FT = table(["家人的休闲娱乐", "Passage 1 (mine)", "Passage 2 (mine)"],
           [["爸爸", "看电视，更爱看书，下棋，打牌", "橄榄球迷，打橄榄球，看球赛，去现场看球"], ["妈妈", "做饭，看肥皂剧，用微信聊天，散步", "去海边散步或跑步，带狗散步，种花种草"], ["哥哥", "无", "摇滚迷，有乐队，练习，表演，收集海报"], ["我", "看电影，打游戏，打篮球，看职业篮球比赛", "冲浪，爬山，滑雪，游泳"]],
           title="Activity 9: what each family member does for fun (the book leaves the tables blank)", say=[0, 1, 2])
L4 = lesson(
    "Lesson 18 (Unit 3 review): skills integration review, a party journal and two families",
    "长周末聚会 · 一个中式家庭 · 一个美式家庭",
    requires=[],
    cards=[
        card("Activity 9 (Reading, Writing, Speaking and Listening): the DLI teacher’s journal",
             "Read the following journal of a teacher at the Defense Language Institute and complete the tasks. A. Make a list of things you often bring to social gatherings (我常常带去派对或聚会的东西), then pair up and share it. B. Each partner reads two paragraphs of the passage and writes a summary of that part. C. Exchange the information and together mark each of the statements True or False (my key follows the passage). D. Share your answers with the class.",
             examples=[D(z, e) for z, e in zip(DLI, DLI_E)] + [D(z, e) for z, e in DTF]),
        card("Activity 9 (Reading, Writing, Speaking and Listening): two families",
             "Read the passages about two families and complete the tasks. A. Pair up; one partner reads Passage 1 and the other reads Passage 2; take notes in the table below each passage (家人的休闲娱乐: 爸爸, 妈妈, 我 for Passage 1; 爸爸, 妈妈, 哥哥, 我 for Passage 2). B. Exchange information with your partner and complete the table for that passage. C. Compare the two families with your own and find any differences or similarities. The two passages (the tables are filled in by me):",
             examples=[D(z, e) for z, e in zip(FAM1, FAM1_E)] + [D(z, e) for z, e in zip(FAM2, FAM2_E)], tables=[FT]),
    ],
    exercises=[
        M("What kind of day was the party?", "A sunny, pleasant day of about seventy degrees", ["A rainy day", "A snowy day", "A very hot day"], "阳光灿烂、风和日丽…不冷不热."),
        M("What are the author’s specialties?", "Grilled lamb, chicken legs and wings", ["Dumplings", "Apple pie", "Pasta"], "烤羊肉和烤鸡腿、鸡翅是我的拿手菜."),
        M("Who made the apple pie?", "The author’s wife", ["Anna", "Mark", "Zhang Lin’s mother"], "我太太还亲自做了一个苹果派."),
        M("What did Mark and his girlfriend bring?", "Beer and hot dogs", ["Dumplings", "Fruit", "Pasta"], "啤酒和热狗."),
        M("What did Anna bring?", "Two big boxes of fruit and a pasta dish", ["Dumplings", "Hot dogs", "Beer"], "水果…意大利面."),
        M("What did the children do after eating?", "Ran around and played on the grass", ["Cooked", "Did homework", "Went home"], "在院子里的草地上跑来跑去地玩."),
        M("When did everyone go home?", "After five in the afternoon", ["At noon", "At midnight", "At eight in the evening"], "一直玩到下午五点才回家."),
        M("What is the Passage 1 family like?", "A very Chinese family of three who love quiet", ["A large noisy family", "A family of four who love sports", "A family who never watch TV"], "非常中式的家庭，只有三口人…爱静不爱动."),
        M("What does the dad in Passage 1 do?", "He is a doctor who likes reading, chess and cards", ["A football coach", "A band member", "A chef"], "我爸是医生…看书…下棋，打牌."),
        M("What is the mom’s recent hobby in Passage 1?", "Chatting with friends on WeChat", ["Skiing", "Running", "Swimming"], "迷上了用微信跟她的朋友们聊天."),
        M("What kind of fan is the dad in Passage 2?", "An American-football fan", ["A soccer fan", "A tennis fan", "A golf fan"], "美式足球迷."),
        M("What is the brother in Passage 2?", "A rock fan with a band", ["A basketball fan", "A chess player", "A swimmer"], "摇滚迷，有一个乐队."),
        M("Where did the narrator in Passage 2 grow up?", "By the sea", ["In the mountains", "In a desert", "In a big city center"], "我在海边长大."),
        F("我们大人们则围___在桌边，开心地喝酒聊天。", "坐", PART, "围坐: sit around."),
        F("他们不是看恐怖片，就是看动作片，有时候也看看搞笑___。", "片", PART, "搞笑片: comedy."),
    ],
)

# ------------------------------------------------------------------ 5. using Chinese in context review
MAIL = [("同学们，大家好，", "Hello, everyone,"), ("祝贺你们完成了第三单元的学习并取得了优异的成绩。这个周末我想请同学们到我家来烧烤，放松一下。我最近刚买了一个房子，上个星期才搬进来。我家房子很大，有很多好玩的东西，比如卡拉ＯＫ机，乒乓球台等。我想请你们一起想一想烧烤需要准备什么，你们会带什么吃的，你们希望我给你们做什么中国菜，还有饭后我们做什么娱乐活动。想好了以后，请给我发一个电子邮件告诉我，我好提前做准备。", "Congratulations on completing Unit 3 and achieving excellent results. This weekend I’d like to invite you to my home for a barbecue to relax. I just bought a house recently and only moved in last week. My house is big and has lots of fun things, such as a karaoke machine, a table tennis table and so on. I’d like you to think together about what we need to prepare for the barbecue, what food you’ll bring, what Chinese dishes you’d like me to make for you, and what entertainment we’ll do after the meal. After you’ve thought it through, please email me so I can prepare in advance."),
        ("谢谢。周末见！王老师", "Thank you. See you at the weekend! Teacher Wang")]
BBQ = table(["你们需要准备的", "Sample answers (mine)"],
            [["你们带什么吃的", "水果，饮料，零食，甜点"], ["希望王老师做什么中国菜", "饺子，炒面，宫爆鸡丁，红烧肉"], ["烧烤想烤什么", "牛肉，羊肉，鸡翅，玉米，蔬菜"], ["准备什么餐具", "盘子，杯子，筷子，刀叉"], ["想喝什么饮料", "可乐，橙汁，绿茶，啤酒"], ["饭后做什么娱乐活动", "唱卡拉ＯＫ，打乒乓球，聊天"]],
            title="Activity 3: the party table (the book leaves it blank; the answers are mine)", say=[0, 1])
SURV = table(["题目", "问题"],
             [["电脑游戏", "最喜欢哪一个游戏？ 和谁一起玩？ 什么时候玩？"], ["社交网络", "最喜欢哪一个社交网络？ 通常做什么？"], ["音乐网站", "最喜欢哪一个网站？ 通常做什么？ 喜欢什么音乐？ 最喜欢哪个歌手？"], ["电影", "最喜欢看什么电影？ 最喜欢的电影演员？ 喜欢在哪儿看电影？"], ["业余爱好和休闲活动", "喜欢唱歌还是跳舞？ 会什么乐器？ 喜欢什么电视节目？ 喜欢什么体育运动？"]],
             title="问卷调查 (the book’s survey, with two blank answer columns: 你的回答 and 你同学的回答)", say=[0, 1])
TOPICS = ["你去哪个健身房健身？", "那里的环境怎么样？", "一个月多少钱？有没有优惠？", "那个健身房有什么器械和设施？", "你在那儿做什么运动？", "你一个星期去几次？", "你觉得什么运动适合我？", "你老家一年四季的天气怎么样？", "每个季节可以做什么户外运动？", "在你老家，人们常常最喜欢什么运动？", "你最喜欢什么运动？", "你从几岁起就开始做这个运动？", "做这个运动需要什么设备？",
          "你家人喜欢看球赛吗？", "他们最喜欢看什么球赛？", "他们在家里看还是去现场看？", "他们最喜欢的球星是谁？", "除了看球赛，你家人喜欢打什么球？", "你最喜欢什么球？", "你最喜欢的球星是谁？为什么喜欢？"]
L5 = lesson(
    "Lesson 18 (Unit 3 review): using Chinese in context review",
    "给女儿的出国建议 · 北京西安旅行计划 · 烧烤派对 · 问卷调查 · 室友聊天",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing and Speaking): the voice mail from your teacher",
             "Scenario: You received a voice mail from your Chinese teacher in China. Her daughter is going to America to study at a high school, but she is concerned about her trip to the U.S. Your teacher asks you to write and explain the procedures for boarding a plane, the security check and passing through U.S. customs. A. Listen to the voice mail and write a summary in pinyin or characters (张老师留言的主要意思是什么？). B. Form three groups. Each group explains one procedure and writes notes in the table: 第一组 登机前需要做什么; 第二组 安检时候做什么; 第三组 入美国海关时做什么. C. After your discussion, consolidate all three groups’ work into one document and email it to your teacher (TO: 张老师; Subject:). (Audio and pictures, not included.)"),
        card("Activity 2 (Reading, Writing and Speaking): Beijing and Xi’an",
             "Scenario: You are studying Chinese at Tianjin University. Your class plans to take a field trip to Beijing and Xi’an next month. You can only stay in Beijing for two days and Xi’an for one day. You are tasked by your teacher to make an itinerary for this trip and decide what you would like to see, given your time constraints. Divide into two groups and write up an itinerary; your teacher will select the best one. The places shown: 天安门广场, 长城, 北海公园, 西安古城, 秦始皇兵马俑, 大雁塔. A. In your group, discuss and choose your itinerary by following the considerations in the diagram: for 天津: 旅游团/自己去, 什么时候出发, 怎么去北京 (开车, 坐火车, 坐飞机); for 北京 and 西安: 时间怎么安排, 游览哪个地方, 要不要导游, 交通工具, 在哪儿吃饭, 住民宿/旅馆. B. In your group, create your itinerary and submit it to your teacher by email (TO: 老师; Subject: 旅游计划). (Photographs of 中国民宿, not included.)"),
        card("Activity 3 (Reading, Speaking and Writing): the barbecue party",
             "Scenario: Your class just completed Unit 3 and would like to have a party to celebrate. Your teacher suggests having a barbecue party at her house, which she recently bought because it is a big house where you can have a lot of fun. To ensure a successful party, you and your classmates must prepare for it. A. Pair up, read the email below and verbally summarize it for your partner. B. With your partner, think of what you will need for the party and fill in the table. C. Summarize your findings and write them in an email to Professor Wang (TO:; Subject:). The email (the book writes “卡拉 OK”) and my sample table:",
             examples=[D(z, e) for z, e in MAIL], tables=[BBQ]),
        card("Activity 4 (Reading, Writing and Speaking): the survey",
             "Scenario: You are studying Chinese at a university in China and work part-time in the International Students Office. The university would like to know what the international students like to do in their spare time so that they can better serve their needs. You and your classmates are asked to conduct a survey about your activities, and to analyze it and write a report to the International Students Office. A. Pair up. Ask your partner the questions in the table and note their answers. B. Each pair reports their survey results in turn by posting their responses on the wall. C. Analyze your class’s responses; write a report (问卷调查结果分析) and submit it to the International Students Office.",
             tables=[SURV]),
        card("Activity 5 (Reading and Speaking): the roommate",
             "Role-Play Scenario: You are sharing an apartment with a Chinese student who studies at California State University, Monterey Bay. After dinner, you chat with your housemate about their gym, their outdoor activities and ball games. Your partner plays the part of the Chinese housemate. A. Pair up and discuss the following topics. B. Note any similarities or differences between what you and your partner discussed in the table: 一样的地方 / 不一样的地方.",
             examples=[D(f"{i}. {q}", "") for i, q in enumerate(TOPICS, 1)]),
    ],
    exercises=[
        M("What does the voice mail ask you to explain?", "Boarding, the security check and U.S. customs", ["Hotel booking", "Visa fees", "Currency exchange"], "登机、安检、入美国海关."),
        M("Where is the class’s field trip?", "Beijing and Xi’an", ["Shanghai and Hangzhou", "Beijing only", "Xi’an only"], "北京和西安."),
        M("How long will they stay in Xi’an?", "One day", ["Two days", "A week", "Half a day"], "Xi’an for one day."),
        M("What is Teacher Wang’s new house good for?", "A barbecue with lots of fun things like karaoke and a table tennis table", ["A big exam", "A quiet study", "A concert hall"], "房子很大，有很多好玩的东西."),
        M("What does Teacher Wang ask the class to send her?", "An email saying what to prepare and bring", ["A phone call", "A letter", "Nothing"], "请给我发一个电子邮件告诉我."),
        M("What does the survey in Activity 4 ask about?", "Games, social networks, music, movies, hobbies", ["Only sports", "Only food", "Only travel"], "问卷调查."),
        M("Where are you sharing an apartment in Activity 5?", "Near California State University, Monterey Bay", ["In Beijing", "In Shanghai", "In New York"], "California State University, Monterey Bay."),
        M("What do you ask about gym membership?", "How much a month and whether there is a discount", ["Where the teacher lives", "What movie is on", "How tall the coach is"], "一个月多少钱？有没有优惠？"),
        F("你从几岁___就开始做这个运动？", "起", PART, "从…起."),
        F("你最喜欢的球星是谁？为什么___欢？", "喜", PART, "喜欢."),
    ],
)

UNIT = unit("第十八课 Unit 3 review: skills integration and using Chinese in context", [L1, L2, L3, L4, L5])
