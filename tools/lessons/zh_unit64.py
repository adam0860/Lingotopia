"""Unit 64: Lesson 22 (Asking for Directions) Presentation 2 from the book's texts: the directions-to-a-friend's-home dialog, the activities, the
expressions for asking and giving directions (distance, leaving a place, 沿着, passing lights, turning, landmarks, arriving, intersections, the end of the
road, highways), the activities, the skill-integration passages (highway numbers, the museum route, getting lost in Germany), the using-Chinese
activities (map apps) and the vocabulary list. Audio, maps, pictures and links are not included; numbers the book writes as digits are spelled
out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l22_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('干净', 0, 'gan1'), ('还是想', 0, 'hai2'), ('还不能', 0, 'hai2'), ('还要', 0, 'hai2'), ('还告诉', 0, 'hai2'), ('还很', 0, 'hai2'), ('还是开', 0, 'hai2'), ('还没', 0, 'hai2'), ('还有', 0, 'hai2'), ('还多', 0, 'hai2'), ('要看', 0, 'yao4'), ('得去移', 0, 'dei3'), ('得到马', 1, 'dei3'), ('局和药', 1, 'he2')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. dialog
P2 = [("张文", "马克，周末有什么安排吗？我想请几个朋友到家里聚聚。", "Mark, do you have any plans for the weekend? I’d like to invite a few friends over to my home to get together. (translation mine)"), ("马克", "太好了！我一定去。你家住哪儿？", "Great! I’ll definitely come. Where do you live?"),
      ("张文", "我把地址发给你，你在百度地图上一查就知道怎么走了。", "I’ll send you the address, and you’ll know how to get there as soon as you look it up on Baidu Maps."), ("马克", "我的手机还不能用百度地图。这样吧，你告诉我怎么走，我画个图。", "My phone still can’t use Baidu Maps. Tell you what: you tell me how to get there and I’ll draw a map."),
      ("张文", "好吧。你出了学校以后，沿着卫国路往南开，过两个红绿灯……", "OK. After you leave the school, drive south along Weiguo Road and pass two traffic lights…"), ("马克", "慢点，慢点，过两个红绿灯…", "Slow down, slow down, pass two traffic lights…"),
      ("张文", "对，在第三个红绿灯往右拐，就是兴华街。沿着兴华街一直往前开，就到了一个丁字路口。", "Right, turn right at the third traffic light and that’s Xinghua Street. Drive straight ahead along Xinghua Street and you’ll come to a T-junction."), ("马克", "什么路口？", "What kind of junction?"),
      ("张文", "丁字路口。那儿有一个停车牌。", "A T-junction. There is a stop sign there."), ("马克", "哦，知道了。你接着说。", "Oh, I see. Go on."),
      ("张文", "在那儿往左拐，你会看到一个很大的绿色路牌，从那儿上二号高速公路，往北开二十分钟左右。", "Turn left there and you’ll see a big green road sign; get on Highway 2 from there and drive north for about twenty minutes."), ("马克", "上二号高速，往北开。然后呢？", "Get on Highway 2, drive north. And then?"),
      ("张文", "然后从二十一号出口下高速路。下了高速，就是中山路，我家就在中山路十五号。", "Then take Exit 21 off the highway. Once you’re off the highway that’s Zhongshan Road, and my home is at 15 Zhongshan Road."), ("马克", "你看看，我画得对不对？", "Take a look: did I draw it right?"),
      ("张文", "（仔细看了一下）真不错！没想到你不光中文好，图也画得这么漂亮。", "(looks carefully) Really good! I didn’t expect that you were not only good at Chinese but could also draw such a beautiful map. (the book has an interjection of agreement here, “ń”, which I left out because the app cannot speak it)"),
      ("马克", "你过奖了！", "You flatter me!"), ("张文", "不过说真的，你还是想办法装个地图软件吧，那以后不管上哪儿你都不会迷路了。", "But seriously, you’d better find a way to install a map app; then wherever you go you won’t get lost.")]
L1 = lesson(
    "Lesson 22 Presentation 2: directions to a friend’s home",
    "周末聚聚 · 百度地图 · 沿着卫国路往南开 · 丁字路口 停车牌 · 上二号高速 下高速",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. How have methods of navigation changed over time? B. What are the possible ways for a driver to get directions? C. What are the popular online maps in the U.S.? Can you use these apps overseas? D. When was the last time you hand-drew a map? Why? E. What road signs may you need to refer to when giving directions to a driver? (Two photographs are not included.)"),
        card("Presentation 2: 到张文家怎么走", "The book also prints the dialog in traditional characters; the digits 2, 20, 21 and 15 are spelled out in the Chinese text. The translations are mine.", examples=dlg(P2)),
    ],
    exercises=[
        M("Why is Zhang Wen inviting Mark?", "To get together with a few friends at his home", ["To go shopping", "To study together", "To move house"], "我想请几个朋友到家里聚聚."),
        M("How would Mark normally find the way?", "Look it up on Baidu Maps", ["Call a taxi", "Ask a policeman", "Use a paper atlas"], "你在百度地图上一查就知道怎么走了."),
        M("Why can’t Mark use Baidu Maps?", "His phone can’t use it yet", ["He has no money", "He dislikes maps", "His phone was lost"], "我的手机还不能用百度地图."),
        M("What does Mark offer to do instead?", "Draw a map from the directions", ["Ask a classmate", "Take a bus", "Phone Zhang Wen"], "你告诉我怎么走，我画个图."),
        M("Which direction does he drive along Weiguo Road?", "South", ["North", "East", "West"], "沿着卫国路往南开."),
        M("Where does he turn right?", "At the third traffic light", ["At the second", "At the stop sign", "At the highway"], "在第三个红绿灯往右拐."),
        M("What is at the T-junction?", "A stop sign", ["A bus stop", "A shop", "A bridge"], "那儿有一个停车牌."),
        M("Which highway does he take?", "Highway 2", ["Highway 21", "Highway 15", "Highway 5"], "上二号高速公路."),
        M("How long does he drive north on the highway?", "About twenty minutes", ["Two hours", "Five minutes", "A whole day"], "往北开二十分钟左右."),
        M("Which exit does he take?", "Exit 21", ["Exit 2", "Exit 15", "Exit 12"], "从二十一号出口下高速路."),
        M("What is Zhang Wen’s address?", "15 Zhongshan Road", ["21 Xinghua Street", "2 Weiguo Road", "15 Renmin Road"], "中山路十五号."),
        M("What does Zhang Wen advise at the end?", "Install a map app", ["Buy a car", "Learn to draw", "Stay home"], "你还是想办法装个地图软件吧."),
        F("我把地址发给你，你在百度地图上一___就知道怎么走了。", "查", PART, "一查就知道."),
        F("你告诉我怎么走，我画个___。", "图", PART, "画个图: draw a map."),
        F("你过___了！", "奖", PART, "过奖: you flatter me."),
    ],
)

# ------------------------------------------------------------------ 2. activities
A3 = [("出了学校以后，沿着卫国路往南开，过两个红绿灯。", "1. After leaving school, drive south along Weiguo Street and pass two traffic lights. (the book’s English; the blanks are 出了, 沿着, 过; key mine)"), ("在第三个红绿灯往右拐，就是兴华街。", "2. Turn right at the third traffic light onto Xinghua Street. (往右拐)"), ("沿着兴华街一直往前开，就到了一个丁字路口。", "3. Go straight along Xinghua Street until you reach a T-junction. (一直往前开)"),
      ("在那儿往左拐，你会看到一个很大的绿色路牌，从那儿上二号高速公路，往北开二十分钟左右。", "4. Turn left at the T-junction, you will see a large green sign, take Highway 2 and drive north for about 20 minutes. (会看到, 上, 往北开)"), ("然后从二十一号出口下高速路。", "5. Take exit 21 to get off the highway onto Zhongshan Road. (从, 下高速)"), ("下了高速，就是中山路，我家就在中山路十五号。", "6. My home is at 15 Zhongshan Road. (就在)")]
L2 = lesson(
    "Lesson 22 Presentation 2 activities: landmarks, road signs and the route to Zhang Wen’s home",
    "Activities 1 to 4 · 人行道 单行道 · 出了 沿着 过 · 往右拐 · 上二号高速",
    requires=[],
    cards=[
        card("Activity 1 (Listening)",
             "A. Global listening: listen to Presentation 2 once and answer: 1. Why is Mike going to Zhang Wen’s house? (to a get-together with friends) 2. How does Zhang Wen usually navigate? (with a map app such as Baidu Maps) 3. How does Mike plan to find Zhang Wen’s house? (he will draw a map from Zhang Wen’s directions) 4. What mode of transportation will Mike use? (driving) 5. What kind of landmarks are mentioned in their conversation? (traffic lights, a T-junction, a stop sign, a green road sign, a highway exit). B. Detailed listening: listen again, draw a map of the route to Zhang Wen’s house in your notebook (the book’s blank map shows 学校, Weiguo Road, Xinghua Street, Highway 2, Exit 21 and Zhongshan Road 15), and in groups of three compare your work. (Audio, not included.)"),
        card("Activity 2 (Speaking)",
             "A. Pair up. With your partner, name the following landmarks (eight pictures; the first example is 人行道, the sidewalk). B. Name each sign correctly (twelve road-sign pictures; the first example is 单行道, one-way street). (All the pictures are not included, so the answers are not given.)"),
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Complete the sentences using the English translation. B. Pair up. Take turns reading the sentences of the completed passage. Listen to each other’s work and discuss any differences. The book prints the six sentences with blanks; the completed Chinese (key mine) with the book’s English:",
             examples=[D(z, e) for z, e in A3]),
        card("Activity 4 (Listening and Speaking)",
             "Listen to the conversation. Write step-by-step instructions in English on how to get from Xiao Wen’s house to Zhuang Hua’s house. In Chinese, explain your notes to your partner and compare your work. (Audio, not included.)"),
    ],
    exercises=[
        M("What does 人行道 mean?", "Sidewalk", ["Highway", "Crossroads", "Bridge"], "人行道: sidewalk."),
        M("What does 单行道 mean?", "One-way street", ["Two-way street", "Dead end", "Highway exit"], "单行道: one-way street."),
        M("Which fills “___学校以后，沿着卫国路往南开”?", "出了", ["到了", "坐了", "换了"], "出了学校以后."),
        M("Which fills “在第三个红绿灯___，就是兴华街”?", "往右拐", ["往右看", "往右坐", "往右买"], "往右拐."),
        M("Which fills “沿着兴华街一直往前开，___到了一个丁字路口”?", "就", ["才", "再", "又"], "就到了."),
        M("Which fills “从那儿___二号高速公路”?", "上", ["下", "看", "买"], "上高速."),
        M("Which fills “然后从二十一号出口___高速路”?", "下", ["上", "拐", "过"], "下高速."),
        M("Which fills “我家___在中山路十五号”?", "就", ["才", "还", "再"], "我家就在中山路十五号."),
        F("在那儿往左拐，你会看___一个很大的绿色路牌。", "到", PART, "会看到."),
        F("往北开二十分钟___右。", "左", PART, "左右: about."),
    ],
)

# ------------------------------------------------------------------ 3. asking, distance, leaving, along
AS = table(["对象", "怎么问"], [["问一个地方", "这个地方在哪儿？"], ["问一个地方", "（到）这个地方怎么走？"], ["问一个地方", "怎么去这个地方？"], ["问一类地方", "哪儿有这种地方？"], ["问一类地方", "这附近有这种地方吗？"]], title="Two basic ways to ask for directions", say=[1])
ASE = [("请问，这附近有地铁站吗？", "1. Excuse me, is there a subway station nearby?"), ("我想问一下，到美国大使馆怎么走？", "2. I’d like to ask, how do I get to the American Embassy?"), ("你好！你能告诉我怎么去机场吗？", "3. Hello! Can you tell me how to get to the airport?"), ("劳驾，请问哪儿有厕所？", "4. Excuse me, where is the restroom?"), ("不好意思，请问，金河饭店在哪儿？", "5. Sorry to bother you, where is the Jinhe Hotel?")]
DIS = [("文化公园离这儿不太远，走路二十分钟就到了。", "1. Culture Park is not too far from here; it takes twenty minutes on foot."), ("就在前面不远。走到停车牌那儿右拐就到了。", "2. It’s just ahead, not far. Walk to the stop sign, turn right and you’re there."), ("我家离学校二十多公里，开车需要半个小时左右。", "3. My home is more than twenty kilometers from school; it takes about half an hour by car."), ("从市中心到机场有七十多公里，坐地铁要一个多小时。", "4. From downtown to the airport is more than seventy kilometers; it takes over an hour by subway.")]
LV = [("出了北京大学东门以后，往右转。", "1. After going out of the East Gate of Peking University, turn right."), ("出了三号航站楼以后，过马路。", "2. After leaving Terminal 3, cross the road."), ("从地铁站八号出口出来以后，一直往前走。", "3. After coming out of Exit 8 of the subway station, go straight ahead."), ("从我家出来就是文华街。", "4. Coming out of my home is Wenhua Street."), ("请问，在哪儿坐出租车？——从三号门出去，往左拐就是。", "5. Excuse me, where do I get a taxi? — Go out of Gate 3 and turn left; that’s it."), ("请问邮局在哪儿？——出了学校西门以后，过马路就是。", "6. Where is the post office? — After going out of the West Gate of the school, cross the road and that’s it.")]
AL = [("沿着红星路往前开。", "1. Drive forward along Hongxing Road."), ("沿着人民路往西开五公里。", "2. Drive west along Renmin Road for five kilometers."), ("沿着三号高速往北开二十分钟。", "3. Drive north along Highway 3 for twenty minutes."), ("沿着这条小路走二百米左右。", "4. Walk about two hundred meters along this lane."), ("沿着这条路一直走到红绿灯那儿。", "5. Keep walking along this road to the traffic light.")]
L3 = lesson(
    "Lesson 22 Presentation 2 grammar: asking for and giving directions (1)",
    "请问怎么走 · 离这儿…公里 · 出了…以后 · 沿着…往…开/走",
    requires=[],
    cards=[
        card("Asking for Directions",
             "Asking for directions is still inevitable, even in this digital age. There are two basic ways to ask for direction in Chinese: for a particular place, “This Place + 在哪儿？”, “（到）This Place + 怎么走？” and “怎么去 + This Place？”; for a particular kind of place, “哪儿有 This Kind of Place？” and “这附近有 This Kind of Place 吗？”. Speakers usually begin with polite phrases like 请问；你好，我想问一下…；不好意思，你能告诉我…；劳驾, etc.",
             tables=[AS], examples=[D(z, e) for z, e in ASE]),
        card("Giving directions: distance and time",
             "Giving directions for walking or driving are the same, except the verbs used are 走 for walking and 开 for driving. Before giving detailed directions, it’s always useful to explain how far the destination is and how long it will take to get there. Patterns: 某地离这儿几公里; 从某地到某地开车需要多长时间; 从某地到某地开车多长时间就到了.",
             examples=[D(z, e) for z, e in DIS]),
        card("Leaving a place",
             "If leaving from an airport, train station, school, or similar place: 出了某地以后; 从某地出来/出去以后.",
             examples=[D(z, e) for z, e in LV]),
        card("沿着 … 往/向 … 开/走",
             "Patterns: 沿着 street + 往/向 + direction + 开/走 + a certain distance or time; 沿着 street + 往/向 + direction + 开/走到 + landmark. Notes: 1. When giving directions, 往 and 向 are interchangeable. 2. In Southern China, the relative directions 左/右 are more commonly used, while in Northern China, the cardinal directions 东/西/南/北 are more commonly used. 3. The commonly used measurement unit is 公里 for longer distances and 米 for shorter and more precise distances. You can also use “mile” 英里 and “foot” 英尺.",
             examples=[D(z, e) for z, e in AL]),
    ],
    exercises=[
        M("Which verb is used for walking directions, and which for driving?", "走 for walking, 开 for driving", ["开 for walking, 走 for driving", "Both use 坐", "Both use 看"], "走 for walking and 开 for driving."),
        M("Which question asks for a kind of place?", "这附近有地铁站吗？", ["到机场怎么走？", "金河饭店在哪儿？", "怎么去大使馆？"], "这附近有…吗?"),
        M("Which polite phrase means “Excuse me” (get someone’s attention)?", "劳驾", ["过奖", "迷路", "继续"], "劳驾 is a polite opener."),
        M("How do you say “it takes about half an hour by car”?", "开车需要半个小时左右", ["开车需要半个小时差", "开车半个小时右", "开车要半个小时给"], "半个小时左右."),
        M("Which means “after leaving the school”?", "出了学校以后", ["到学校以前", "坐学校以后", "买学校以后"], "出了…以后."),
        M("What does 沿着人民路往西开五公里 mean?", "Drive west along Renmin Road for five kilometers", ["Drive east for five minutes", "Walk west for five meters", "Take the bus west"], "沿着…往西开五公里."),
        M("Which units are used for long and short distances?", "公里 for long, 米 for short", ["米 for long, 公里 for short", "Only 英里", "Only 英尺"], "公里 / 米."),
        M("Are 往 and 向 interchangeable in directions?", "Yes", ["No, only 往 is allowed", "No, only 向 is allowed", "Only in the South"], "Note 1."),
        M("In which part of China are 左/右 more common?", "Southern China", ["Northern China", "Western China only", "Nowhere"], "Note 2."),
        F("请问邮局在哪儿？——出了学校西门以后，过马路___是。", "就", PART, "过马路就是."),
        F("我想问一___，到美国大使馆怎么走？", "下", PART, "问一下: ask."),
    ],
)

# ------------------------------------------------------------------ 4. passing, turning, landmarks, arriving
PS = [("过三个路口。", "1. Pass three intersections."), ("过两个红绿灯，到第三个往右拐。", "2. Pass two traffic lights and turn right at the third."), ("走过两个街区，看到红绿灯时往左拐。", "3. Walk past two blocks and turn left when you see a traffic light.")]
TN = [("一直往前走，在红绿灯那儿往左拐。", "1. Go straight ahead and turn left at the traffic light."), ("在第二个十字路口向右转。", "2. Turn right at the second crossroads."), ("在停车牌那儿左转，或者在丁字路口那儿左转。", "3. Turn left at the stop sign or at the T-junction. (the book writes 停车牌/丁字路口)"), ("沿着北街走到红绿灯，然后向右转。", "4. Walk along North Street to the traffic light, then turn right."),
      ("请问地铁站在哪儿？——一直往前走，走到红绿灯那儿左拐。", "5. Where is the subway station? — Go straight ahead and turn left at the traffic light."), ("沿着这条街一直走到红绿灯那儿，然后向右拐。", "6. Keep walking along this street to the traffic light, then turn right.")]
LM = [("出了学校大门，就是富兰克林大街。", "1. Out of the school gate is Franklin Street."), ("下了高速，就是中山路。", "2. Once you get off the highway, that’s Zhongshan Road."), ("在第三个红绿灯往右拐，就是兴华路。", "3. Turn right at the third traffic light and that’s Xinghua Road."), ("一直往前走，你会看到一个停车牌。", "4. Keep going straight and you will see a stop sign."), ("再走五十米左右，你会看到左边有一个蓝色的路牌。", "5. Walk about fifty meters more and you will see a blue street sign on the left.")]
CT = [("过了邮局以后，继续往前走。", "1. After passing the post office, keep going straight."), ("在第三个红绿灯往右拐，就是兴华路，沿着兴华路继续往前开。", "2. Turn right at the third traffic light and that’s Xinghua Road; keep driving along Xinghua Road.")]
AR = [("再走不远就到了。王府井大饭店就在路的西边。", "1. Go a little farther and you’re there. The Wangfujing Hotel is on the west side of the road."), ("大华旅行社就在农贸市场的对面。", "2. The Dahua Travel Agency is right opposite the farmers’ market."), ("中国银行就在你的右手边。", "3. The Bank of China is right on your right.")]
IX = [("人民北路和文太西街的十字路口", "1. the intersection of Renmin North Road and Wentai West Street"), ("文太正街和人民中路的十字路口", "2. the intersection of Wentai Main Street and Renmin Middle Road"), ("沿着文华路一直往北开，开到文化路和红星路的路口向右转。", "3. Drive straight north along Wenhua Road; at the junction of Wenhua Road and Hongxing Road turn right.")]
EN = [("离开停车场以后，沿着白云巷一直往前开，开到底，往左拐。", "Example 1 (a map): After leaving the parking lot, drive straight ahead along Baiyun Lane, to the end, then turn left."), ("你沿着玉林三巷一直往南走，走到头往右拐，就是玉林东街，再走到头，然后往左拐，就是玉林街。", "Example 2 (a map): Walk straight south along Yulin Third Lane, to the end, turn right, that’s Yulin East Street; walk to the end again and then turn left, and that’s Yulin Street.")]
L4 = lesson(
    "Lesson 22 Presentation 2 grammar: asking for and giving directions (2)",
    "过…个红绿灯 · 往左拐 往右转 · 就是 你会看到 · 继续往前开 · …就到了 · 开到底",
    requires=[],
    cards=[
        card("Passing traffic lights and intersections",
             "Pattern: 过 + number + 个红绿灯/路口. The difference between 经过 and 穿过: 经过 means “to pass by”, whereas 穿过 means “to pass through”. On the book’s map (not included) you 经过 a coffee shop and then 穿过 a park.",
             examples=[D(z, e) for z, e in PS]),
        card("Turning",
             "Notes: 1. 转 and 拐 are interchangeable when giving directions. 2. 那儿 is optional. 3. 往/向 can be omitted in this situation.",
             examples=[D(z, e) for z, e in TN]),
        card("Pointing out a landmark",
             "Patterns: 就是 + landmark; 你会看到 + landmark. And “过了 landmark 以后，继续往前走/开”.",
             examples=[D(z, e) for z, e in LM] + [D(z, e) for z, e in CT]),
        card("Arriving at the destination, naming an intersection, and the end of the road",
             "Arriving: destination 就到了; destination 就在你的右手边/左手边/前面; destination 就在 landmark 的 direction. Naming an intersection: A路和B路的（十字）路口. To the end of the road: 开/走 + 到 + 底/头.",
             examples=[D(z, e) for z, e in AR] + [D(z, e) for z, e in IX] + [D(z, e) for z, e in EN]),
    ],
    exercises=[
        M("What is the difference between 经过 and 穿过?", "经过 is passing by; 穿过 is passing through", ["They are the same", "经过 is through; 穿过 is by", "Only 穿过 is used for roads"], "Pass by vs pass through."),
        M("How do you say “pass three intersections”?", "过三个路口", ["过三个红绿灯桥", "三个过路口", "过路口三个站"], "过 + number + 个路口."),
        M("Are 转 and 拐 interchangeable?", "Yes, when giving directions", ["No", "Only 拐 is correct", "Only 转 is correct"], "Note 1."),
        M("What does 出了学校大门，就是富兰克林大街 mean?", "Out of the school gate is Franklin Street", ["Franklin Street is far from school", "The school is on Franklin Street", "The gate is closed"], "出了…就是…."),
        M("Which means “you will see a stop sign”?", "你会看到一个停车牌", ["你会坐一个停车牌", "你会买一个停车牌", "你会走一个停车牌"], "你会看到…."),
        M("What does 过了邮局以后，继续往前走 mean?", "After passing the post office keep going straight", ["Stop at the post office", "Turn left at the post office", "Go back to the post office"], "继续往前走."),
        M("Which means “is right opposite the farmers’ market”?", "就在农贸市场的对面", ["就在农贸市场的里面", "就在农贸市场的上面", "就在农贸市场的下面"], "对面."),
        M("What does 走到头 mean?", "Walk to the end of the road", ["Walk to the head of the bus", "Walk one more step", "Walk back"], "到底/到头: to the end."),
        M("Which names an intersection?", "人民北路和文太西街的十字路口", ["人民北路在文太西街里", "人民北路跟十字", "文太西街十字人民"], "A路和B路的十字路口."),
        F("在第二个十字路口向右___。", "转", PART, "向右转."),
        F("再走五十米左右，你会看___左边有一个蓝色的路牌。", "到", PART, "会看到."),
    ],
)

# ------------------------------------------------------------------ 5. highways and activities
UP = [("上京沪高速公路。", "1. Get on the Beijing–Shanghai Expressway. (a picture of the sign, not included)"), ("上三十三号高速。", "2. Get on Highway 33."), ("上一号高速。", "3. Get on Highway 1."), ("上往东行驶的四十号高速公路。", "4. Get on Highway 40 going east."), ("上往北行驶的八十五号高速公路。", "5. Get on Highway 85 going north.")]
DN = [("从一百八十九号出口下高速公路。", "1. Get off the highway at Exit 189."), ("去斗南走一百五十八号公路，从二百四十号出口下高速。", "2. To go to Dounan, take Highway 158 and get off at Exit 240."), ("再往前开两公里就是二百四十号出口，从那里下高速公路。", "3. Drive two more kilometers and that’s Exit 240; get off the highway there."), ("从二号出口下高速公路，就到了重庆北路。", "4. Get off the highway at Exit 2 and you reach Chongqing North Road."), ("从四号出口下高速，下了高速以后，就是松江路。", "5. Get off the highway at Exit 4; once off the highway, that’s Songjiang Road.")]
G2 = [("一直往前走，直到你看到医院，然后往左拐。", "1. Go straight on till you see the hospital, then turn left. (Activity 2, my Chinese)"), ("在十字路口那儿往右拐。", "2. Turn right at the intersection/traffic light."), ("走到头往左拐，我家就是二十九号。", "3. Turn left at the end of the road and my house is number 29."), ("过了路口继续往前走大约一英里。", "4. Cross the junction and keep going for about one mile."), ("在红绿灯那儿一直往前走。", "5. Go straight at the traffic light."),
      ("在右边第三条路往右拐，你会看到邮局就在右边。", "6. Take the third road on the right and you will see the post office on the right."), ("在左边第二条路往左拐，你会看到医院就在前面。", "7. Take the second road on the left and you will see the hospital straight ahead."), ("走到路的尽头，你会看到一个丁字路口。", "8. At the end of the road, you will see a T-junction."), ("医院在地铁站的对面。", "9. The hospital is opposite the subway station."), ("那座房子在饭馆的旁边。", "10. The house is next to the restaurant."), ("商店在邮局和药店的中间。", "11. The shop is between the post office and the pharmacy.")]
G4 = [("在普鲁内代尔上一零一号高速往北开，开大约四十五英里，从一号出口下高速，就到了圣何塞的南第十一街。", "1. Monterey–San Jose: enter Hwy 101N at Prunedale, follow 101N for about 45 miles, take exit 1 to S 11th St in San Jose. (Activity 4, my Chinese)"), ("从弗里蒙特街上一号公路，沿着一号公路开十英里，从一百八十三号出口下去。", "2. Monterey–Salinas: get on Hwy 1 from Fremont St., follow Hwy 1 for 10 miles, take exit 183. (mine)")]
DRT = table(["要说的内容", "我的说法 (mine)"], [["起点", "出了…以后 / 从…出来以后 / 从…出发"], ["沿着街一直走", "沿着…路一直往前走/开"], ["经过红绿灯或路口", "过两个红绿灯 / 过三个路口"], ["拐弯", "往左拐 / 往右拐 / 往左转 / 向右转"], ["继续往前", "继续往前走 / 继续往前开"], ["到了看到地标", "你会看到… / 就是…"], ["到达目的地", "…就到了 / 就在你的左手边"]],
            title="Activity 1: how to say the seven ways of giving directions (the book gives the English list; my table)", say=[1])
L5 = lesson(
    "Lesson 22 Presentation 2 grammar: highways, and activities on giving directions",
    "上高速公路 · 从…号出口下高速 · 往东行驶 · 十一个方向翻译 · 蒙特雷到圣何塞",
    requires=[],
    cards=[
        card("Getting on a highway",
             "The specific verbs for getting on and off a highway are 上 and 下. Pattern: 上高速公路 / 上往 + direction + 开的 + number + 号高速公路. (The book illustrates these with road-sign photos, not included.)",
             examples=[D(z, e) for z, e in UP]),
        card("Getting off a highway",
             "Pattern: 从 + number + 号出口下高速公路.",
             examples=[D(z, e) for z, e in DN]),
        card("Activity 1 (Speaking)",
             "How would you express the following ways of giving directions in Chinese? 1. Starting point 2. Go straight along the street 3. Passing traffic lights/intersections 4. Make turns 5. Continue to go forward 6. Arrive and see a landmark 7. Arrive at a destination.",
             tables=[DRT]),
        card("Activity 2 (Speaking)",
             "Write the following directions in Chinese (eleven sentences). The book gives the English; my Chinese:",
             examples=[D(z, e) for z, e in G2]),
        card("Activities 3 and 4",
             "Activity 3 (Speaking and Listening): Pair up. Using the map (not included), you and your partner will leave from 张华家 and from 李老师家 separately. Each partner chooses three places to go. Tell your partner the directions without revealing the destination. See if your partner can guess where you will arrive. Take turns practicing. Activity 4 (Speaking and Listening): in Chinese, describe the route below and compare your work with your partner’s. The book gives two routes in English; my Chinese:",
             examples=[D(z, e) for z, e in G4]),
    ],
    exercises=[
        M("Which verbs are used for getting on and off a highway?", "上 and 下", ["开 and 关", "走 and 停", "拐 and 转"], "上高速 / 下高速."),
        M("How do you say “get on Highway 33”?", "上三十三号高速", ["下三十三号高速", "看三十三号高速", "买三十三号高速"], "上…号高速."),
        M("How do you say “get off at Exit 189”?", "从一百八十九号出口下高速公路", ["从一百八十九号出口上高速公路", "往一百八十九号出口拐", "在一百八十九号出口买"], "从…号出口下高速."),
        M("Which means “Get on Highway 40 going east”?", "上往东行驶的四十号高速公路", ["下往东行驶的四十号高速公路", "上往西行驶的四十号高速公路", "上往东行驶的四号高速公路"], "往东行驶."),
        M("How do you say “the hospital is opposite the subway station”?", "医院在地铁站的对面", ["医院在地铁站的里面", "医院在地铁站的下面", "医院在地铁站的后面"], "对面."),
        M("How do you say “between the post office and the pharmacy”?", "在邮局和药店的中间", ["在邮局和药店的外面", "在邮局的药店", "在药店的邮局"], "…和…的中间."),
        M("How do you say “turn left at the end of the road”?", "走到头往左拐", ["走到头往右看", "走到头往后买", "走到头往下车"], "走到头往左拐."),
        M("What does 就是 point out?", "A landmark or the next street you meet", ["A price", "A time", "A person"], "就是 + landmark."),
        F("上往北行驶的八十五号高速___路。", "公", PART, "高速公路."),
        F("从四号出口下高速，下了高速以后，___是松江路。", "就", PART, "就是."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
HW = ("每条高速公路都有自己的名字。例如，北京到哈尔滨的高速公路叫“北京－哈尔滨高速公路”，简称“京哈高速”。除了名字以外，高速公路还有自己的编号。京哈高速的编号是Ｇ一。中国高速公路的编号里面有字母和数字，例如Ｇ一，Ｇ二，Ｓ六三。Ｇ是国家高速公路，Ｓ是省高速公路。",
      "Every expressway has its own name. For example, the expressway from Beijing to Harbin is called the “Beijing–Harbin Expressway”, abbreviated 京哈高速. Besides the name, an expressway also has its own number. The number of the Beijing–Harbin Expressway is G1. Chinese expressway numbers contain a letter and digits, for example G1, G2, S63. G is a national expressway, S is a provincial expressway. (the book writes the numbers as G1, G2, S63; I wrote the letters in full-width form and the digits in hanzi; translation mine)")
HW2 = ("如果编号是Ｇ和一位数字，那这条高速公路就是从北京出发的。例如，Ｇ二是从北京到上海，Ｇ四是从北京到香港。如果一条高速是南北方向的，那它的编号就有两位数字，而且第二个数字会是一，三，五，七，九，例如Ｇ十一，Ｇ十五，Ｇ六十九。如果高速公路是东西方向的，那它的编号就是Ｇ十，Ｇ三十六，Ｇ四十二……",
       "If the number is G plus one digit, then that expressway starts from Beijing. For example G2 goes from Beijing to Shanghai and G4 from Beijing to Hong Kong. If an expressway runs north–south, its number has two digits and the second digit will be 1, 3, 5, 7 or 9, for example G11, G15, G69. If an expressway runs east–west, its number is G10, G36, G42… (translation mine)")
HW3 = ("高速公路出口的编号是从高速公路的起点到这个出口的公里数。有多少公里，出口就是多少号。例如，二十五号出口离起点有二十五公里，九十八号出口离起点有九十八公里。开车的人看到现在经过的出口，就能知道离他想去的出口还有多远了。",
       "The number of an expressway exit is the number of kilometers from the start of the expressway to that exit. Whatever the kilometers are, that is the exit number. For example Exit 25 is 25 kilometers from the start and Exit 98 is 98 kilometers from the start. A driver who sees the exit he is now passing can tell how far he still is from the exit he wants. (translation mine)")
D3 = [("出了酒店以后，沿着人民南路往北开。", "1. After leaving the hotel, drive north along South Renmin Road. (Activity 3B, my Chinese)"), ("过两个路口，在第三个路口往右拐。", "2. Pass two intersections and turn right at the third intersection."), ("一直往前开，你会看到五号高速的路牌。", "3. Go straight ahead; you will see the sign for Highway 5."), ("上五号高速往北开四十公里左右。", "4. Take Highway 5 and drive north for about 40 km."), ("从十四号出口下高速，就到了广汉路。", "5. Take Exit 14 to get off the highway at Guanghan Avenue."), ("三星堆博物馆就在广汉路三四七号。", "6. The museum, the Sanxingdui Museum, is located at 347 Guanghan Avenue.")]
GE = [("十年前，我在德国留学。一个冬天的早上，我得去移民局办签证延期。我以前去过那儿，记得下车后沿着路走几分钟就有一条大河，过了桥往左拐，再走十分钟左右就可以看到移民局的大楼。",
       "Ten years ago I was studying in Germany. One winter morning I had to go to the immigration office (移民局, Yímínjú) to renew my visa (签证延期, yánqí). I had been there before and remembered that after getting off I would walk along the road for a few minutes to a big river, cross the bridge and turn left, then walk about ten more minutes and could see the immigration office building. (translation mine)"),
      ("可是，一出地铁口我就迷了路，走了几条街，也没看到桥，连河也没看见。天还很黑，路上根本没有人。正在这时，我突然看见对面走来一位德国妇女。那时候我的德语很不好，我说了三遍“移民局”，又拿出护照给她看，她才明白。可是她也不知道移民局在哪儿，而且她还告诉我，这附近也没有桥。",
       "But as soon as I came out of the subway exit I got lost; I walked several streets and saw no bridge, not even the river. It was still very dark and there was nobody on the road. Just then I suddenly saw a German woman walking toward me from across the road. My German was very poor then; I said “immigration office” three times and took out my passport to show her before she understood. But she didn’t know where the immigration office was either, and she also told me there was no bridge nearby. (mine)"),
      ("看到我着急的样子，她到停车场把车开来，说：“我带你到人多的地方去问问。”因为太早，我们开了很久才问了两个人，可他们也不知道。最后，她把车开到警察局，才问到了移民局的地址。拿到地址后我才知道，原来，我提前了好几站下车。",
       "Seeing how anxious I was, she went to the parking lot, brought her car and said, “I’ll take you to a place with more people to ask.” Because it was so early, we drove a long time before we asked two people, and they didn’t know either. In the end she drove to the police station and only then found out the address of the immigration office. After I got the address I realized that I had gotten off several stops too early. (mine)"),
      ("她抱歉地告诉我，她还要回去上班，要是有时间，她一定会送我去移民局。不过，她还是开车把我送到了附近的地铁站。我再三向她表示谢意，她却说：“如果我在你的国家迷路，你一定也会这样帮助我，对吗？”",
       "She told me apologetically that she still had to go back to work and that if she had time she would certainly have taken me to the immigration office. Still, she drove me to a nearby subway station. I thanked her again and again, but she said, “If I got lost in your country, you would certainly help me like this too, right?” (mine)")]
GQ = ("C. Take turns verbally answering the following questions. 1. “我”记忆中的路是怎么走的？ 2. 这位德国妇女是怎么帮“我”的？ 3. 最后“我们”是怎么找到地址的？ 4. “我”为什么会迷路？ 5. 这位德国妇女为什么会觉得抱歉？ 6. 文中的最后一句话是什么意思？ Answers from the text (mine): 1. After getting off, walk along the road a few minutes to a big river, cross the bridge, turn left and walk about ten more minutes. 2. She drove him to places with people to ask and finally to the police station and to a subway station. 3. At the police station. 4. He got off several stops too early. 5. She had to go back to work and could not take him to the office. 6. People should help each other wherever they are, and she assumes he would do the same for her abroad.")
L6 = lesson(
    "Lesson 22 Presentation 2 skill integration: highway numbers, a museum route and getting lost in Germany",
    "中国高速公路小知识 · 三星堆博物馆 · 在德国迷路 · 移民局 · 如果我在你的国家迷路",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking): 中国高速公路小知识",
             "A. Read the passage without the help of your dictionary. Highlight any unknown words and try to guess their meanings. B. Choose three unknown words you think are most critical for understanding the passage and guess their meanings. Pair up. Compare your guesses to your partner’s. C. In Chinese, talk with your partner about what you can understand from the following highway signs (four photographs, not included).",
             examples=[D(*HW), D(*HW2), D(*HW3)]),
        card("Activity 2 (Listening and Speaking)",
             "A. Listen to a phone call between 小王 and 马克 and sketch the route described. B. Pair up. Explain the route to your partner using a sketch. Compare your notes to see if there are any inconsistencies. (The sketch has building 32, a new North Road and an East Gate; audio is not included.)"),
        card("Activity 3 (Listening, Reading and Speaking)",
             "A. Listen to the directions on how to get to a famous museum (博物馆 Bówùguǎn) from a hotel in downtown Chengdu and answer: 1. What’s the location of the museum relative to downtown Chengdu? 2. In your notebook, draw a map of the directions from the hotel to the museum. Compare your map with your partner’s. (The map shows 人民南路, the Highway 5 and 广汉路, an Exit 39 and the hotel; audio is not included.) B. Below is a list of driving directions in English (the Sanxingdui Museum, 三星堆博物馆). Pair up and, in Chinese, take turns explaining the route to your partner. My Chinese:",
             examples=[D(z, e) for z, e in D3]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Read the passage without the help of your dictionary. Underline any unknown words and try to guess their meanings. B. Choose three unknown words you think are most critical for understanding the passage. Pair up and compare your guessed meanings with those of your partner. " + GQ,
             examples=[D(z, e) for z, e in GE]),
    ],
    exercises=[
        M("What does 京哈高速 stand for?", "The Beijing–Harbin Expressway", ["The Beijing–Hong Kong Expressway", "The Beijing–Shanghai Expressway", "A harbor road"], "简称京哈高速."),
        M("What does the letter G mean in a highway number?", "National expressway", ["Provincial expressway", "City road", "Rural lane"], "G 是国家高速公路."),
        M("What does the letter S mean?", "Provincial expressway", ["National expressway", "Airport road", "Tunnel"], "S 是省高速公路."),
        M("What does a G plus one digit mean?", "It starts from Beijing", ["It ends in Beijing", "It is east–west", "It is a toll road"], "从北京出发的."),
        M("Which expressway goes from Beijing to Shanghai?", "G2", ["G4", "G1", "G11"], "G2 是从北京到上海."),
        M("What do the exit numbers show?", "The kilometers from the start to that exit", ["The number of lanes", "The year it was built", "The number of exits"], "出口的编号是…的公里数."),
        M("How far from the start is Exit 98?", "98 kilometers", ["25 kilometers", "9 kilometers", "8 kilometers"], "九十八号出口离起点有九十八公里."),
        M("Where was the writer studying?", "Germany", ["France", "Japan", "Canada"], "我在德国留学."),
        M("Where did he need to go?", "The immigration office, to renew his visa", ["The embassy", "A bank", "The airport"], "去移民局办签证延期."),
        M("What did the German woman do to help?", "Drove him around to ask and then to a subway station", ["Gave him a map", "Walked away", "Called a taxi"], "开车…送到了附近的地铁站."),
        M("Why had he got lost?", "He got off several stops too early", ["The map was wrong", "He took the wrong road", "It was snowing"], "我提前了好几站下车."),
        F("高速公路出口的编号是从高速公路的起点到这个出口的公___数。", "里", PART, "公里数."),
        F("我再三向她表示谢___。", "意", PART, "谢意: thanks."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context
CG = ("在中国的大城市旅行不太难，地铁和机场都有英文标志。但是离开地铁和机场以后就会有麻烦了。在中国，很少有出租车司机会说英文，会读的就更少了。所以，如果你想到中国旅行，最好在出发以前就在手机上装上地图。",
      "Traveling in big cities in China is not too hard; the subways and airports have English signs. But once you leave the subway and the airport there will be trouble. In China few taxi drivers can speak English and even fewer can read it. So if you want to travel to China, it is best to install a map on your phone before you set out. (translation mine, from the Chinese text translated from The China Guide)")
CG2 = ("谷歌地图可能是最好的手机地图了。但是，谷歌所有的服务都不能在中国使用。如果你用的是苹果手机，那就比较方便了。苹果地图在中国也可以运行。中国人自己用得最多的是百度地图和高德地图。这两个地图软件都很不错，问题是，它们都只有中文。对外国人来说，要看懂可不是一件容易的事。",
       "Google Maps may be the best phone map. But none of Google’s services can be used in China. If you use an Apple phone it is more convenient: Apple Maps also works in China. The ones Chinese people use most are Baidu Maps and Gaode Maps. Both are very good; the problem is that they are only in Chinese. For foreigners, reading and understanding them is not an easy thing. (mine; the book writes “谷歌地图(Google Map)”; I left out the English in brackets)")
L7 = lesson(
    "Lesson 22 Presentation 2 using Chinese in context: map apps, routes and your weekend",
    "地图软件 · 谷歌 百度 高德 · 驾车路线 · 蒙特雷到洛杉矶 · 周末去哪儿",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking)",
             "A. The passage below is translated from the English website The China Guide. Read its introduction on using a map app in China. B. Form groups of three. Discuss the following questions using the above information: 1. What makes traveling in China easy and difficult for foreigners? 2. What are the best ways to find directions in China?",
             examples=[D(*CG), D(*CG2)]),
        card("Activity 2 (Writing and Speaking)",
             "Visit map.baidu.com to open 百度地图, which shows the 北京大学 area. Use the search bar to find the route from 北京大学东门 to 北京大学–对外汉语教育学院. Choose the 驾车 option and describe the route. (The website and screenshot are not included.)"),
        card("Activities 3 to 5 (Speaking)",
             "Activity 3: Describe the route below from Monterey to Los Angeles (a driving route in English: get on CA-1 N/CA-68 E from W Franklin St, 8 min (2.3 mi); get on US-101 S from River Rd, 31 min (25.4 mi); follow US-101 S to CA-46 E in Paso Robles and take exit 231B, 1 hr 16 min (85.6 mi); get on I-5 S in Kern County, 1 hr 2 min (63.7 mi); follow I-5 S to N Los Angeles St and take exit 2B from US-101 S, 2 hr 12 min (143 mi); continue on N Los Angeles St and drive to W 1st St). Activity 4 (Speaking and Listening): describe the walking route from the DLI/POM Access Point to the Monterey Bay Aquarium. You can use Google Maps for information. Pair up and compare your work with your partner’s. Activity 5 (Speaking): where do you usually go on the weekend? Describe the route you take, by either walking, driving, or public transportation. (Screenshots and photographs are not included.)"),
    ],
    exercises=[
        M("What makes big-city travel in China relatively easy?", "Subways and airports have English signs", ["All drivers speak English", "All maps are in English", "Everything is free"], "地铁和机场都有英文标志."),
        M("What makes it hard once you leave the subway and airport?", "Few taxi drivers speak or read English", ["There are no taxis", "There are no roads", "Maps are illegal"], "很少有出租车司机会说英文."),
        M("What does the passage advise before you travel?", "Install a map on your phone", ["Learn all the street names", "Buy a car", "Hire a guide"], "最好在出发以前就在手机上装上地图."),
        M("Which map cannot be used in China, according to the passage?", "Google Maps (all Google services)", ["Baidu Maps", "Gaode Maps", "Apple Maps"], "谷歌所有的服务都不能在中国使用."),
        M("Which maps do Chinese people use most?", "Baidu Maps and Gaode Maps", ["Google Maps and Bing", "Apple Maps only", "Paper maps"], "百度地图和高德地图."),
        M("What is the problem with Baidu and Gaode for foreigners?", "They are only in Chinese", ["They cost money", "They are slow", "They don’t work on phones"], "它们都只有中文."),
        F("苹果地图在中国也可以运___。", "行", PART, "运行: run."),
        F("对外国人来说，要看___可不是一件容易的事。", "懂", PART, "看懂: read and understand."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 22 Presentation 2 vocabulary", "17 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English; its glosses are kept as printed. The book also lists the interjection of agreement pronounced “ń” (“ok”), which I left out because the app cannot speak it.", VOC2)

UNIT = unit("第二十二课 Presentation 2: 到朋友家怎么走, 问路和指路, 高速公路", [L1, L2, L3, L4, L5, L6, L7, L8])
