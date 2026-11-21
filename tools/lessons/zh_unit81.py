"""Unit 81: Lesson 26 (Study and Travel Abroad), Presentation 3 and Area Studies: the passage on how Chinese people travel abroad with its activities, compound-complex sentences (2),
the pattern 有些人…有些人…还有些人…, 总之, the skill-integration tasks (Chinese tourists, a graduation trip, weddings abroad), the using-Chinese tasks (a road trip, three islands, two museums),
the vocabulary list and the Area Studies reading on overseas Chinese students. Audio, pictures, videos and websites are not included; numbers the book writes as digits are spelled out in Chinese text;
answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l26_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('因此得了', 2, 'de2'), ('一定得买', 2, 'dei3'), ('你得做', 1, 'dei3'), ('你得先', 1, 'dei3'), ('你得准备', 1, 'dei3'), ('你得收拾', 1, 'dei3'), ('你得先选', 1, 'dei3'), ('家长', 1, 'zhang3'), ('不适应', 2, 'ying4'), ('行业', 0, 'hang2'), ('称为', 1, 'wei2'), ('弹吉他', 0, 'tan2')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 3 + activities 1-2
TP = [("近些年，中国人变得越来越有钱，加上签证更容易，国际航线不断增加，所以很多中国人选择去国外旅游，而且旅游的方式和目的更是多种多样。",
       "In recent years Chinese people have become richer and richer; add to that visas are easier and international air routes keep increasing, so many Chinese people choose to travel abroad, and moreover the ways and purposes of travel are even more varied. (translations in this card are mine; the book also prints the passage in traditional characters)"),
      ("以前中国人出国旅游多半是参加旅行团，让旅行团安排所有的行程，但是现在许多人选择自由行，他们自己安排旅游路线，到了国外租车自驾游，边走边看，慢慢体验当地的文化和生活。",
       "In the past Chinese people traveling abroad mostly joined tour groups and let the tour group arrange the whole itinerary, but now many people choose independent travel: they arrange their own routes, rent a car and drive themselves once abroad, looking as they go, slowly experiencing the local culture and life."),
      ("现在的中国人出国旅游的目的也不太一样。有些人是为了远离工作，放松身心，所以会选择海岛游或定点游。有些人出国是为了了解世界，学习新东西，他们会到比较古老的国家，参观名胜古迹或是博物馆。还有些人出国是为了庆祝特别的日子，比如结婚，度蜜月等等。",
       "The purposes of Chinese people traveling abroad now are also not quite the same. Some do it to get away from work and relax body and mind, so they choose island tours or set-destination tours. Some go abroad to learn about the world and learn new things; they go to rather ancient countries and visit scenic spots, historic sites or museums. Still others go abroad to celebrate special days, such as getting married, spending a honeymoon and so on."),
      ("不管旅游的方式和目的是什么，对中国人来说，购物一直都是一个重要的活动。以前中国人喜欢在世界各地“扫货”，购买国外的名牌，因为这些东西的价格比国内便宜得多。现在中国人更喜欢在旅游的时候，逛逛当地的农贸市场，买些有特色的商品或美食。总之，中国人的出国旅游越来越自由，越来越有特点。",
       "Whatever the way and purpose of travel, for Chinese people shopping has always been an important activity. In the past Chinese people liked to go on shopping sprees all over the world and buy foreign brand names, because the prices of these things were much cheaper than at home. Now Chinese people prefer, while traveling, to stroll through local farmers’ markets and buy some distinctive goods or delicacies. In short, Chinese people’s travel abroad is more and more free and more and more distinctive.")]
CAT = table(["Category", "Terms (my key)"],
            [["出国的目的", "学习，庆祝，放松"], ["可去的地方", "博物馆，海岛，名胜古迹"], ["需要的证件", "签证，护照"], ["旅游的方式", "跟旅行团，自由行，自驾游"], ["可做的活动", "逛农贸市场，扫货，买名牌，吃美食"]],
            title="Activity 1A: the fifteen terms in the book’s five categories (my key; the book’s boxes are blank)", say=[0, 1])
TT3 = table(["", "以前", "现在"],
            [["旅游的方式", "多半参加旅行团，让旅行团安排所有的行程", "许多人选择自由行，自己安排路线，租车自驾游，边走边看"],
             ["旅游的目的", "(the presentation does not say)", "远离工作，放松身心；了解世界，学习新东西；庆祝特别的日子"],
             ["购物", "在世界各地“扫货”，买国外的名牌，因为价格比国内便宜得多", "逛当地的农贸市场，买有特色的商品或美食"]],
            title="Activity 2B: my table (the book’s is blank)")
S2 = [("中国人出国旅游越来越多，旅游的方式和目的越来越多种多样，购物一直是重要的活动，但是现在的人更喜欢有特色的东西。", "Activity 2A (my summary): More and more Chinese people travel abroad, the ways and purposes are more and more varied, and shopping has always been an important activity, but people now prefer things with character."),
      ("以前中国人多半参加旅行团，现在许多人选择自由行；以前喜欢扫货，现在喜欢逛农贸市场。", "2D (my briefing): In the past Chinese people mostly joined tour groups, and now many choose independent travel; in the past they liked shopping sprees, and now they like to stroll through farmers’ markets."),
      ("近些年中国人越来越有钱，签证也更容易，所以很多人去国外旅游。有人想放松，有人想学习，也有人想庆祝结婚。", "2E (my recount in my own words): In recent years Chinese people have become richer and visas easier, so many people travel abroad. Some want to relax, some want to learn, and some want to celebrate a wedding.")]
L1 = lesson(
    "Lesson 26 Presentation 3: how Chinese people travel abroad",
    "出国旅游 · 旅行团 自由行 自驾游 · 海岛游 定点游 · 度蜜月 · 扫货 · 总之",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. If you have traveled abroad, why did you go? What motivates people to travel abroad? B. Look at the pictures. What do you most like to do when traveling and why? C. Is shopping during your travels important? What do you usually buy (other than food)? (Four pictures are not included.)"),
        card("Presentation 3: 中国人出国旅游", "The four paragraphs of the presentation.", examples=[D(*x) for x in TP]),
        card("Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. Write the terms from the word bank in their appropriate categories. Word bank: 逛农贸市场, 学习, 扫货, 博物馆, 跟旅行团, 签证, 自由行, 庆祝, 自驾游, 买名牌, 吃美食, 海岛, 名胜古迹, 护照, 放松. B. Read your categories to a partner. C. In Chinese, paraphrase (explain, describe or define) three terms of your choosing until your partner guesses the terms. The categories are the book’s; the placement of the terms is my key.",
             tables=[CAT]),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Global Listening: listen to Presentation 3 and summarize it. B. Detailed Listening: listen again and fill in the table (以前 and 现在 for 旅游的方式, 旅游的目的 and 购物). C. Read your information to a partner in Chinese to compare work. D. Based on the presentation and the table, brief your partner in Chinese on past Chinese travel abroad, while they brief you on the present. E. In your own words, recount the presentation to your partner in Chinese. (Audio; my summary, table and recounts follow.)",
             tables=[TT3], examples=[D(z, e) for z, e in S2]),
    ],
    exercises=[
        M("What three things have made more Chinese people travel abroad?", "More money, easier visas and more air routes", ["Cheaper food", "Shorter workdays", "New passports"], "越来越有钱，签证更容易，国际航线不断增加."),
        M("How did Chinese people mostly travel abroad in the past?", "With tour groups", ["On their own", "By car", "By train only"], "多半是参加旅行团."),
        M("What do many people choose now?", "Independent travel (自由行)", ["Staying home", "Only tour groups", "Only cruises"], "许多人选择自由行."),
        M("Why do some people choose island tours?", "To get away from work and relax body and mind", ["To visit museums", "To get married", "To go shopping"], "远离工作，放松身心."),
        M("Where do people who want to learn about the world go?", "To rather ancient countries, scenic spots and museums", ["To beaches", "To malls", "To airports"], "古老的国家，名胜古迹，博物馆."),
        M("Which special days do some people go abroad to celebrate?", "Weddings and honeymoons", ["Birthdays only", "New Year only", "Graduation only"], "结婚，度蜜月."),
        M("Why did Chinese people like shopping sprees abroad in the past?", "Brand names were much cheaper than at home", ["They were free", "They were rare", "They were healthier"], "价格比国内便宜得多."),
        M("What do Chinese people prefer to buy now?", "Distinctive goods or delicacies from local markets", ["Brand-name bags", "Cars", "Houses"], "逛逛当地的农贸市场，买些有特色的商品或美食."),
        M("What does the conclusion say about Chinese travel abroad?", "It is more and more free and distinctive", ["It is declining", "It is too expensive", "It is only for the rich"], "越来越自由，越来越有特点."),
        F("现在的中国人出国旅游的目的也不太一___。", "样", PART, "一样: the same."),
        F("以前中国人喜欢在世界各地“扫___”。", "货", PART, "扫货: go on a shopping spree."),
    ],
)

# ------------------------------------------------------------------ 2. activities 3-4
AQ = [("你申请过签证吗？去哪个国家？", "Activity 3C (my sample questions), for “applied for a visa”: Have you ever applied for a visa? For which country?"), ("你喜欢参加旅行团吗？为什么？", "For “prefers tour groups”: Do you like joining tour groups? Why?"),
      ("你喜欢开车去旅游吗？你去过哪里？", "For “likes road trips”: Do you like traveling by car? Where have you been?"), ("旅行的时候，你喜欢多去几个地方吗？", "For “likes to see as many places as they can”: When traveling, do you like to go to several places?"),
      ("你喜欢在一个地方休息吗？", "For “likes to just relax in one place”: Do you like to rest in one place?"), ("你想去哪里度蜜月？", "For “would like to honeymoon abroad”: Where would you like to spend your honeymoon?")]
WPK = [("用信用卡买完东西以后，你得在收据上签名。", "1a. After buying things with a credit card you have to sign the receipt. (my key: 签名)"), ("去一些国家旅行，你得去大使馆办签证。", "1b. To travel to some countries you have to go to the embassy to get a visa. (my key: 签证)"),
       ("很多人工作压力大，一放假就会远离城市到国家公园去放松一下。", "2a. Many people have great work pressure and, as soon as it is a holiday, get away from the city to a national park to relax. (my key: 远离)"), ("我离开家乡到北京工作已经一年多了，可是还是不适应北京的生活。", "2b. It has been more than a year since I left my hometown to work in Beijing, but I still haven’t adapted to life in Beijing. (my key: 离开)"),
       ("最近几年很多新人们选择婚后去海岛度蜜月。", "3a. In recent years many newlyweds choose to go to an island for their honeymoon after the wedding. (my key: 度蜜月)"), ("现在的人生活压力大，再加上工作繁忙，不少人选择晚婚或是不结婚。", "3b. People now have great life pressure, and with busy work added, quite a few choose to marry late or not to marry. (my key: 结婚)"),
       ("很多旅行社的行程包括购物和参观名胜古迹。", "4a. The itineraries of many travel agencies include shopping and visiting scenic spots and historic sites. (my key: 行程)"), ("我这次自由行的路线是从旧金山出发，经过洛杉矶到拉斯维加斯，然后坐飞机到纽约。", "4b. My route for this independent trip is to set out from San Francisco, pass through Los Angeles to Las Vegas, and then fly to New York. (my key: 路线)"),
       ("要是你参加旅行社的自由行，他们会帮你订旅馆和机票，到了目的地，你可以选择自己想做的活动。", "5a. If you join a travel agency’s independent-travel package, they will book your hotel and air tickets for you, and once at the destination you can choose the activities you want to do. (my key: 自由行)"), ("很多美国人喜欢长周末开车到各个风景点自驾游。", "5b. Many Americans like to drive to various scenic spots for a self-drive tour on long weekends. (my key: 自驾游; the book prints the blank before the full stop)")]
ST = [("我们打算去海岛度蜜月。", "Activity 4C (my sample story, one key word per sentence): We plan to spend our honeymoon on an island. (度蜜月)"), ("我们得先去办签证。", "We have to go and get a visa first. (签证)"), ("我们不想参加旅行团，选择自由行。", "We don’t want to join a tour group and choose independent travel. (自由行)"),
      ("我们自己安排了路线。", "We arranged the route ourselves. (路线)"), ("离开家乡以前，朋友们都祝我们旅行愉快。", "Before leaving our hometown, our friends all wished us a pleasant trip. (离开)")]
L2 = lesson(
    "Lesson 26 Presentation 3 activities: a talk show, finding classmates and word pairs",
    "申请过签证 喜欢旅行团 喜欢自驾游 度蜜月 · 签证 签名 · 远离 离开 · 行程 路线 · 自驾游 自由行",
    requires=[],
    cards=[
        card("Activity 3 (Listening and Speaking)",
             "A. Listen to three guests on a talk show, then fill in the table with their travel preferences (Guest 1, 2, 3: Preference and Reasons). B. Form groups of three. In Chinese, brief your partners on the first guest’s preferences and reasons, while they brief you on the other two. C. Around the classroom, find the following types of travelers and ask them at least one question in Chinese related to their preference, then fill in the table with their response: applied for a visa; prefers tour groups; likes road trips; likes to see as many places as they can during a trip; likes to just relax in one place; would like to honeymoon abroad. D. In Chinese, tell the class about the people you found and what they told you. (The talk show is audio; my sample questions follow.)",
             examples=[D(z, e) for z, e in AQ]),
        card("Activity 4 (Reading, Writing, Speaking and Listening)",
             "A. Complete the sentences with the correct choice from the following word pairs: 签证/签名; 远离/离开; 结婚/度蜜月; 行程/路线; 自驾游/自由行. B. Compare work with a partner. C. Write a story using five of the words you filled in above, using one word per sentence. D. Read your story to the class. My key and my story:",
             examples=[D(z, e) for z, e in WPK + ST]),
    ],
    exercises=[
        M("Which word fits “你得在收据上___”?", "签名", ["签证", "行程", "路线"], "签名: sign one’s name."),
        M("Which word fits “你得去大使馆办___”?", "签证", ["签名", "离开", "自驾游"], "签证: visa."),
        M("Which word fits “一放假就会___城市到国家公园去放松一下”?", "远离", ["离开", "结婚", "路线"], "远离: stay away from."),
        M("Which word fits “我___家乡到北京工作已经一年多了”?", "离开", ["远离", "签证", "行程"], "离开: leave."),
        M("Which word fits “很多新人们选择婚后去海岛___”?", "度蜜月", ["结婚", "签名", "远离"], "度蜜月: spend a honeymoon."),
        M("Which word fits “不少人选择晚婚或是不___”?", "结婚", ["度蜜月", "离开", "路线"], "结婚: marry."),
        M("Which word fits “旅行社的___包括购物和参观名胜古迹”?", "行程", ["路线", "签证", "离开"], "行程: itinerary."),
        M("Which word fits “自由行的___是从旧金山出发”?", "路线", ["行程", "签名", "结婚"], "路线: route."),
        M("Which word fits “很多美国人喜欢长周末开车到各个风景点___”?", "自驾游", ["自由行", "行程", "签证"], "自驾游: self-drive tour."),
        F("去一些国家旅行，你得去大使馆办签___。", "证", PART, "签证: visa."),
        F("很多人工作压力大，一放假就会远___城市。", "离", PART, "远离: stay away from."),
    ],
)

# ------------------------------------------------------------------ 3. compound-complex sentences (2)
MC1 = table(["联合复句 (both clauses of equal weight)", "Examples"],
            [["并列复句 (coordinate relationship)", "又…又…; 一边…一边…; 不是…就是…"], ["承接复句 (consistent/successive)", "一…就…; 先…然后…最后…"], ["递进复句 (progressive/incremental)", "不但…而且…; 不仅…还…甚至; 连…也…"], ["选择复句 (alternative relationship)", "是…还是…; 或者…或者…"]],
            title="联合复句 (the first table)")
MC2 = table(["偏正复句 (main clause + subordinate clause)", "Examples"],
            [["因果复句 (causative relationship)", "因为…所以; 由于…因此…"], ["条件复句 (conditional relationship)", "只要…就; 只有…才…; 不管…都…"], ["假设复句 (assumptive relationship)", "如果…就…; 要是…就…"], ["转折复句 (transitional/adversative)", "虽然…但是/可是/不过…"], ["目的复句 (purposive relationship)", "为了…"], ["让步复句 (concessive relationship)", "尽管…还/却…"]],
            title="偏正复句 (the second table)")
MCE = [("近些年，中国人变得越来越有钱，加上签证更容易，国际航线不断增加，所以很多中国人选择去国外旅游，而且旅游的方式和目的更是多种多样。", "Example 1: In recent years Chinese people have become richer and richer; add to that visas are easier, international air routes keep increasing, so many Chinese people choose to travel abroad, and moreover the ways and purposes of travel are even more varied. (Analysis: clause (1), 近些年…国际航线不断增加, causes the results in clauses (2) 所以很多中国人选择去国外旅游 and (3) 而且旅游的方式和目的更是多种多样, so the three clauses are in a causative relationship; 因为 is omitted from clause (1) but implied by 所以. Inside clause (1) the three factors (a) 中国人变得越来越有钱, (b) 签证更容易 and (c) 国际航线不断增加 are in a progressive relationship, marked by 加上. Clauses (2) and (3) are also progressive, because the latter provides additional information, marked by 而且.)"),
       ("除了体验不同的生活和文化以外，有些人出国是为了远离工作，放松身心，所以会选择海岛游或定点游。", "Example 2: Besides experiencing different lives and cultures, some people go abroad to get away from work and relax body and mind, so they choose island tours or set-destination tours. (Analysis: clauses (1) 除了体验不同的生活和文化以外 and (2) 有些人出国是为了远离工作，放松身心 are in a progressive relationship because they give two separate reasons why people travel; inside (2), (a) 远离工作 and (b) 放松身心 are in a purposive relationship, marked by 为了. Clauses (2) and (3) 所以会选择海岛游或定点游 are in a causative relationship because the reason in clause (2) leads to the result in clause (3).)")]
CK1 = [("因为上次的单元考试没考好，所以这次为了准备考试，他不但提早复习生词和课文，而且还跟老师做了很多的练习。", "1. Because he didn’t do well on the last unit test, this time, in order to prepare for the exam, he not only reviewed the new words and texts early but also did many exercises with the teacher. (my analysis: 因为…所以 causative; 为了 purposive; 不但…而且还 progressive; the book’s Activity 1B prints 提前 for 提早)"),
       ("选择合适的运动，不仅能提高锻炼的效果，而且让你不会受伤，所以十分重要。", "2. Choosing a suitable sport can not only improve the effect of exercise but also keep you from getting hurt, so it is very important. (my analysis: 不仅…而且 progressive; the two benefits lead to 所以十分重要, causative)"),
       ("虽然有不少小留学生因为没人照顾养成了坏习惯，但是为了让孩子有更好的学习环境、更好的前途，还是有很多父母愿意把孩子送出国。", "3. Although quite a few young international students formed bad habits because nobody looked after them, in order to give their children a better learning environment and a better future, there are still many parents willing to send their children abroad. (my analysis: 虽然…但是 transitional; 因为 causative inside the first clause; 为了 purposive)"),
       ("为了减肥，他不但每天上健身房锻炼，三餐还只吃蔬菜水果，但还是没见他瘦下来。", "4. In order to lose weight, he not only goes to the gym every day but also eats only vegetables and fruit at his three meals, but he still hasn’t got thinner. (my analysis: 为了 purposive; 不但…还 progressive; 但还是 transitional)"),
       ("不管是上网购物、订餐或是和朋友交流，人们的生活越来越离不开网路，有些人甚至因此得了网瘾。", "5. Whether shopping online, ordering meals or communicating with friends, people’s lives increasingly cannot do without the Internet, and some people even got Internet addiction because of it. (my analysis: 不管…都-type conditional; 甚至因此 progressive and causative; the book’s Activity 1B prints 玩游戏, “playing games”, instead of 订餐)")]
CS3 = [("因为我想去中国工作，所以我每天都学中文，不但学生词，而且还听中文歌。", "Activity 3A (my sample, topic 你的学习): Because I want to work in China, I study Chinese every day, learning not only new words but also listening to Chinese songs."),
       ("虽然我的生活很忙，但是为了身体健康，我还是每天运动。", "(my sample, topic 你的生活): Although my life is busy, for the sake of health I still exercise every day.")]
L3 = lesson(
    "Lesson 26 Presentation 3 grammar: compound-complex sentences 多重复句 (2)",
    "联合复句 偏正复句 · 并列 承接 递进 选择 · 因果 条件 假设 转折 目的 让步 · 因为…所以 · 不但…而且",
    requires=[],
    cards=[
        card("Compound-Complex Sentences 多重复句 (2)",
             "Compound-complex sentences 多重复句 are comprised of at least two independent clauses closely related in meaning. Understanding the relationship between these clauses can help you grasp the core meaning of long and complicated sentences. The two tables below list the kinds of relationship and their cohesive devices, and the two examples show them in use.",
             tables=[MC1, MC2], examples=[D(z, e) for z, e in MCE]),
        card("Activity 1 (Reading)",
             "A. Highlight the cohesive devices in the following compound-complex sentences and determine their function and relationships in the sentence. B. Translate the following sentences, then compare work with a partner. My analyses and translations:",
             examples=[D(z, e) for z, e in CK1]),
        card("Activity 2 (Listening, Reading and Speaking)",
             "A. For five sentences, first listen for the relationships between the clauses, then listen again to translate them. B. Read the script with a partner to check your work. C. Take turns with your partner verbally translating your sentences back into Chinese. (Audio; the sentences and script are not in the book.)"),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Choose two topics (你的生活, 你的工作, 你的学习, 你的家人, 其他话题) and write a compound-complex sentence about each one, focusing on the cohesive devices needed to express the relationships between your clauses. B. Read your sentences to a partner, make any changes they may suggest, then post your sentences on a class website for the class to read. My samples:",
             examples=[D(z, e) for z, e in CS3]),
    ],
    exercises=[
        M("What is a 并列复句?", "Coordinate relationship", ["Causative relationship", "Conditional relationship", "Concessive relationship"], "并列: coordinate."),
        M("Which pair marks a 递进复句?", "不但…而且…", ["因为…所以", "如果…就", "是…还是…"], "不但…而且: progressive."),
        M("Which pair marks a 因果复句?", "因为…所以", ["不但…而且", "只要…就", "虽然…但是"], "因为…所以: cause and effect."),
        M("Which pair marks a 条件复句?", "只有…才…", ["虽然…但是", "为了…", "先…然后…"], "只有…才…: conditional."),
        M("Which pair marks a 假设复句?", "如果…就…", ["尽管…还", "一…就…", "或者…或者…"], "如果…就…: assumptive."),
        M("Which marks a 转折复句?", "虽然…但是/可是/不过…", ["为了…", "要是…就…", "一边…一边…"], "转折: transitional."),
        M("Which marks a 目的复句?", "为了…", ["尽管…还/却…", "不管…都…", "连…也…"], "目的: purposive."),
        M("Which marks a 让步复句?", "尽管…还/却…", ["为了…", "只要…就", "是…还是…"], "让步: concessive."),
        M("Which kind of sentence is 先…然后…最后…?", "承接复句 (successive)", ["选择复句 (alternative)", "因果复句 (causative)", "转折复句 (adversative)"], "承接: successive."),
        M("In Example 1, what relationship do clauses (1), (2) and (3) have?", "Causative", ["Conditional", "Alternative", "Concessive"], "Example 1."),
        F("因为上次的单元考试没考好，所以这次___了准备考试，他不但提早复习。", "为", PART, "为了: in order to."),
        F("选择合适的运动，不仅能提高锻炼的效果，而___让你不会受伤。", "且", PART, "而且: and moreover."),
    ],
)

# ------------------------------------------------------------------ 4. 有些人…有些人…还有些人…
YS0 = table(["结构", "用法"], [["General Assertion + 有些人…有些人…还有些人…", "some folks [are/do X], some folks [are/do Y], and there are also some folks [that are/do Z]; also 有些同学…有些同学…还有些同学…, etc."]], title="段落语法: 有些人…有些人…还有些人…")
YSE = ("现在的中国人出国旅游的目的也不太一样。有些人是为了远离工作，放松身心，所以会选择海岛游或定点游。有些人出国是为了了解世界，学习新东西，他们会到比较古老的国家，参观名胜古迹或是博物馆。还有些人出国是为了庆祝特别的日子，比如结婚，度蜜月等等。",
       "Example: The purposes of Chinese people traveling abroad now are also not quite the same [general assertion]. Some do it to get away from work and relax body and mind, so they choose island tours or set-destination tours [aspect 1]. Some go abroad to learn about the world and learn new things; they go to rather ancient countries and visit scenic spots, historic sites or museums [aspect 2]. Still others go abroad to celebrate special days, such as getting married, spending a honeymoon and so on [aspect 3]. As in English, the pattern gives different aspects or examples of a general assertion.")
YK = [("有些人每天听中文广播，有些人跟中国朋友聊天，还有些人看中文电影。", "Activity 4, item 1 (my sample; the assertion is 中文要学得好有很多办法): Some people listen to Chinese radio every day, some chat with Chinese friends, and some watch Chinese movies."),
      ("有些人觉得民宿有家的感觉，有些人觉得民宿比旅馆便宜，还有些人喜欢可以自己做饭。", "Item 2 (assertion: 住民宿最近越来越受到人们的欢迎): Some people feel a homestay gives the feeling of home, some think a homestay is cheaper than a hotel, and some like being able to cook for themselves."),
      ("有些父母想让孩子学好外语，有些父母想让孩子体验不同的文化，还有些父母希望孩子能进好的大学。", "Item 3 (assertion: 很多父母送孩子出国留学的目的不同): Some parents want their children to learn foreign languages well, some want them to experience different cultures, and some hope their children can enter a good university."),
      ("有些人觉得玩游戏可以放松，有些人觉得可以认识新朋友，还有些人玩得太久，影响学习和健康。", "Item 4 (assertion: 上网玩电子游戏有好处，也有坏处): Some people feel playing games helps them relax, some feel they can meet new friends, and some play too long and it harms their study and health."),
      ("有些人觉得跟旅行团最方便，有些人觉得自由行最自由，还有些人觉得自驾游最好玩。", "Item 5 (assertion: 出国旅游什么方式最好？): Some people think a tour group is the most convenient, some think independent travel is the freest, and some think a self-drive tour is the most fun.")]
YS5 = [("我们班同学都很喜欢学中文，但他们的目的并不一样。有些同学是为了工作，有些同学是为了去中国旅游，还有些同学是因为喜欢中国文化。", "Activity 5 (the first sentence is the book’s example; the rest is my completion): The students in our class all like studying Chinese, but their purposes are not the same. Some students do it for work, some to travel in China, and some because they like Chinese culture.")]
L4 = lesson(
    "Lesson 26 Presentation 3 grammar: 有些人…有些人…还有些人… for different aspects of a general assertion",
    "有些人…有些人…还有些人… · 有些同学…有些同学…还有些同学… · 中文要学得好有很多办法 · 住民宿 · 出国留学的目的",
    requires=[],
    cards=[
        card("段落语法: 有些人…有些人…还有些人…",
             "The sentence pattern 有些人…有些人…还有些人… (or 有些同学…有些同学…还有些同学…, etc.) means “some folks [are/do X], some folks [are/do Y], and there are also some folks [that are/do Z].” As in English, it is used to provide different aspects or examples of a general assertion. Pattern: General Assertion + 有些人…有些人…还有些人…",
             tables=[YS0], examples=[D(*YSE)]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "Form groups of three. For each item below, read the general assertion aloud, then use the 有些人 pattern to provide three aspects or examples of it. Take turns until each classmate has done all five items. The assertions: 1. 中文要学得好有很多办法。 2. 住民宿最近越来越受到人们的欢迎。 3. 很多父母送孩子出国留学的目的不同。 4. 上网玩电子游戏有好处，也有坏处。 5. 出国旅游什么方式最好？ My samples:",
             examples=[D(z, e) for z, e in YK]),
        card("Activity 5 (Reading, Speaking, Listening and Writing)",
             "Ask three of your classmates in Chinese why they chose to study the language, then write a sentence using the 有些人 pattern. For example, 我们班同学都很喜欢学中文，但他们的目的并不一样。有些同学… (three blank lines). My completion:",
             examples=[D(z, e) for z, e in YS5]),
    ],
    exercises=[
        M("What does the pattern 有些人…有些人…还有些人… present?", "Different aspects or examples of a general assertion", ["Three steps in a process", "A cause and its effect", "A comparison of two things"], "General assertion plus aspects."),
        M("What comes first in the pattern?", "A general assertion", ["The third aspect", "A conclusion", "A question"], "General Assertion + …"),
        M("How many aspects does the pattern usually give?", "Three", ["One", "Two only", "Six"], "有些人…有些人…还有些人…"),
        M("In the book’s example, what is the general assertion?", "The purposes of Chinese people traveling abroad now are not quite the same", ["Chinese people don’t travel", "Tour groups are cheap", "Visas are hard"], "现在的中国人出国旅游的目的也不太一样."),
        M("What is aspect 1 in the example?", "To get away from work and relax", ["To learn new things", "To celebrate", "To shop"], "远离工作，放松身心."),
        M("What is aspect 3 in the example?", "To celebrate special days such as a wedding or honeymoon", ["To visit museums", "To study", "To relax on an island"], "还有些人出国是为了庆祝特别的日子."),
        M("Which word begins the third aspect?", "还有些人", ["有些人", "总之", "不管"], "还有些人: still others."),
        M("What can be used instead of 有些人 for classmates?", "有些同学", ["有些老师", "所有同学", "没有同学"], "有些同学…有些同学…还有些同学…"),
        F("现在的中国人出国旅游的目的也不太一样。___些人是为了远离工作。", "有", PART, "有些人: some people."),
        F("___有些人出国是为了庆祝特别的日子。", "还", PART, "还有些人: still others."),
    ],
)

# ------------------------------------------------------------------ 5. 总之
ZZ0 = table(["结构", "用法"], [["Various Points/Factors + 总之 + Conclusion/Summary", "总之 means “in short,” “in brief,” “to sum up,” “anyhow,” etc.; it often comes at the end of a passage or paragraph to summarize or conclude the aforementioned points"]], title="话语语法: 总之")
ZZE = [("你喜欢弹吉他。他喜欢唱歌。我喜欢跳舞。总之每个人都有自己喜欢的爱好。", "1. You like playing the guitar. He likes singing. I like dancing. In short, everyone has a hobby of their own."),
       ("学习要努力，工作要努力，生活也要努力。总之每件事情都要努力才能做好。", "2. Study takes effort, work takes effort, and life takes effort too. In short, everything takes effort to be done well."),
       ("我们班毕业以后，有人当老师，有人当医生。有人当老板。总之人人都有不错的工作。", "3. After our class graduates, some become teachers, some become doctors, and some become bosses. In short, everyone has a decent job.")]
ZZK = [("要是你肚子饿了想吃东西，你可以打电话点外卖，你还可以上“美团”平台订餐。总之，现在想吃什么都很方便。", "Activity 6, item 1 (my conclusion): If you are hungry and want to eat something, you can phone to order takeout, or order on the Meituan platform. In short, it is now convenient to eat whatever you want."),
       ("旅行的时候，你可以根据自己的需要选择住宿的地方。你可以露营，可以住旅馆，也可以住民宿。总之，住的地方有很多选择。", "Item 2: When traveling you can choose a place to stay according to your needs. You can camp, stay in a hotel or stay in a homestay. In short, there are many choices of where to stay."),
       ("父母在孩子小的时候，关心孩子的身体和学习，等孩子长大，也常担心孩子的工作和生活。总之，父母一辈子都在关心孩子。", "Item 3: When children are small, parents care about their bodies and study; when children grow up, they also often worry about their work and life. In short, parents care about their children all their lives."),
       ("用短租平台订房，你得先选择你要的房间，确认信息，然后再付款。总之，在短租平台订房要一步一步来。", "Item 4: To book a room on a short-term rental platform, you first have to choose the room you want, confirm the information and then pay. In short, booking on a short-term rental platform goes step by step."),
       ("高铁列车不仅速度快而且很平稳，车上还能充电和无线上网。总之，坐高铁又快又舒服。", "Item 5: High-speed trains are not only fast but also very smooth, and on board you can also charge your phone and use wireless Internet. In short, taking the high-speed train is both fast and comfortable.")]
ZZP = [("用手机有很多好处。我们可以用手机打电话，上网，买东西，还可以付钱。可是手机也有坏处，我们常常看手机看得太久，眼睛不舒服，也少了和家人朋友说话的时间。总之，手机很方便，但是我们要用得合适。", "Activity 7B (my sample paragraph on 用手机): Using a phone has many benefits. We can use it to make calls, go online, buy things and even pay. But phones also have drawbacks: we often look at them too long, our eyes feel uncomfortable, and we have less time to talk with family and friends. In short, phones are very convenient, but we should use them appropriately.")]
L5 = lesson(
    "Lesson 26 Presentation 3 grammar: 总之 for summing up",
    "总之 · 每个人都有自己喜欢的爱好 · 每件事情都要努力才能做好 · 人人都有不错的工作 · 用手机",
    requires=[],
    cards=[
        card("话语语法: 总之",
             "总之 means “in short,” “in brief,” “to sum up,” “anyhow,” etc. It often comes at the end of a passage or paragraph to summarize or conclude the aforementioned points. Pattern: Various Points/Factors + 总之 + Conclusion/Summary.",
             tables=[ZZ0], examples=[D(z, e) for z, e in ZZE]),
        card("Activity 6 (Reading and Writing)",
             "Read the sentences below and write a concluding sentence for each one using 总之. The five given sentences and my conclusions:",
             examples=[D(z, e) for z, e in ZZK]),
        card("Activity 7 (Reading, Speaking, Listening and Writing)",
             "A. Pair up. In Chinese, brainstorm the advantages and/or disadvantages of one of the following topics: 用手机; 住学校宿舍 vs. 住在校外; 参加陆军/海军/空军; 参加旅行团/自驾游/自由行. B. Write a short paragraph about the topic using 总之 to conclude your thoughts. My sample:",
             examples=[D(*x) for x in ZZP]),
    ],
    exercises=[
        M("What does 总之 mean?", "In short; to sum up", ["For example", "Because", "Although"], "总之."),
        M("Where does 总之 usually come?", "At the end, to summarize or conclude", ["At the very beginning", "Before every verb", "After the subject only"], "Place."),
        M("What does the pattern say follows 总之?", "A conclusion or summary", ["A new topic", "A question", "A list of numbers"], "Various Points + 总之 + Conclusion."),
        M("What comes before 总之?", "Various points or factors", ["Only one point", "Nothing", "A greeting"], "Various Points/Factors."),
        M("Which conclusion fits “你喜欢弹吉他。他喜欢唱歌。我喜欢跳舞。”?", "总之每个人都有自己喜欢的爱好", ["总之今天下雨", "总之我不喜欢学习", "总之我们去旅行"], "Example 1."),
        M("Which conclusion fits “学习要努力，工作要努力，生活也要努力”?", "总之每件事情都要努力才能做好", ["总之不要努力", "总之学习最容易", "总之工作不重要"], "Example 2."),
        M("Which conclusion fits the sentences about teachers, doctors and bosses?", "总之人人都有不错的工作", ["总之没有人工作", "总之大家都当老师", "总之老板不好"], "Example 3."),
        M("Which conclusion fits sentences about ordering takeout and meals online?", "总之，现在想吃什么都很方便", ["总之，现在没有饭馆", "总之，外卖很贵", "总之，大家都做饭"], "Activity 6 item 1."),
        F("学习要努力，工作要努力。___之每件事情都要努力才能做好。", "总", PART, "总之: in short."),
        F("高铁列车不仅速度快而___很平稳。", "且", PART, "而且: and moreover."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
SKV3 = table(["生词", "拼音", "English"], [["吸引", "xīyǐn", "attract"], ["打卡", "dǎkǎ", "“check in” on social media"]], title="Activity 1: new vocabulary", say=[0])
SKP3 = ("近几年来，有越来越多中国人到国外去旅游。二零一九年中国出境游客人数已经达到一点六亿，而且中国游客也是各国游客中最愿意花钱的。对中国人来说，出国旅游最重要的行程之一就是购物。只要有中国游客的地方，你常会看到他们在疯狂地扫货，日本的电器品、法国的名牌包、意大利的名牌服装都是他们购物单上一定得买的东西。为了这些中国客人，各国也推出许多吸引他们的服务，比如，提供会说中文的服务员，旅馆接送服务，用手机付款，送来店礼什么的。不过随着中国人出国旅游的经验越来越丰富，最近中国游客不再只是购物或是在景点打卡了。现在他们更喜欢有特色，高质量的旅游。对他们来说，体验外国文化，认识世界才是旅行的真正目的。",
        "In recent years more and more Chinese people travel abroad. In 2019 the number of Chinese outbound tourists had already reached 160 million, and Chinese tourists are also the most willing to spend money among tourists from all countries. For Chinese people, one of the most important parts of the itinerary of travel abroad is shopping. Wherever there are Chinese tourists, you often see them shopping like mad: Japanese electrical goods, French brand-name bags and Italian brand-name clothing are all things on their shopping lists that they must buy. For these Chinese guests, countries have also introduced many services that attract them, for example Chinese-speaking waiters, hotel pickup service, mobile payment and welcome gifts. But as Chinese people’s experience of travel abroad becomes richer, recently Chinese tourists no longer only shop or check in at scenic spots. Now they prefer distinctive, high-quality travel. For them, experiencing foreign culture and getting to know the world is the real purpose of travel. (the book writes 2019 and 1.6 in digits)")
SK1K = [("二零一九年中国出境游客的人数是一点六亿。", "Activity 1A-1 (my answer): The 1.6 refers to the 160 million Chinese outbound tourists in 2019."),
        ("日本的电器品和法国的名牌包，还有意大利的名牌服装。", "1A-2 (my answer): Japanese electrical goods and French brand-name bags (also Italian brand-name clothing)."),
        ("会说中文的服务员，旅馆接送服务，用手机付款，送来店礼。", "1A-3 (my answer): Chinese-speaking waiters, hotel pickup service, mobile payment, welcome gifts (any three)."),
        ("现在中国游客更喜欢有特色、高质量的旅游，体验外国文化，认识世界才是旅行的真正目的。", "1A-4 (my answer): Chinese tourists now prefer distinctive, high-quality travel; experiencing foreign culture and getting to know the world is the real purpose of travel.")]
SK1T = table(["一样的地方", "不一样的地方"], [["都说中国人出国旅游越来越多，购物是重要的活动，各国都有特色的旅游", "这篇说中国游客最愿意花钱，各国推出吸引他们的服务；第三篇课文说旅游的方式和目的越来越多种多样"], ["都说现在中国人更喜欢有特色的旅游", "这篇说的是出境游客人数和购物单；第三篇课文说的是旅游的方式和目的"]],
             title="Activity 1C: my table of similarities and differences (the book’s is blank)", say=[0, 1])
SKW = ("我们班打算毕业旅行去海岛。先去机场坐飞机，到了海岛以后，大家住民宿，白天在海边玩，晚上一起做饭。第一天休息，第二天潜水，第三天逛农贸市场，第四天坐飞机回家。总之，这次旅行不贵，也很好玩。",
       "Activity 2C (my sample class graduation trip plan; the dialog about 美华 in 2A is audio and not in the book): Our class plans to go to an island for the graduation trip. First we fly from the airport; once on the island everyone stays in a homestay, plays at the seaside in the daytime and cooks together in the evening. The first day we rest, the second day we dive, the third day we stroll through the farmers’ market, and the fourth day we fly home. In short, this trip is not expensive and is a lot of fun.")
SKV4 = table(["生词", "拼音", "English"], [["难忘", "nánwàng", "unforgettable"], ["婚礼", "hūnlǐ", "wedding"], ["新人", "xīnrén", "newlywed/bride"]], title="Activity 3: new vocabulary", say=[0])
WD = ("有越来越多中国年轻人选择到国外结婚，虽然在国外结婚不一定便宜，但是可以有一个比较难忘的婚礼，而且还可以游览国外美丽的风景。结婚前半年到一年，他们会先找婚礼代办公司帮他们计划和安排海外结婚的手续。新人们会在婚礼前一到两天到达，休息几天后，他们会先在几个有名的风景点拍结婚照，然后办婚礼。婚礼以后，他们会在当地度蜜月。有时候也会租车到处看看。几个最近比较热门的海外结婚地点包括欧洲、海岛、澳洲和新西兰。海岛婚礼一般比欧洲或澳、新便宜，所以很多打算邀请家人朋友参加的新人会选择这样的地方。澳洲、新西兰有美丽的高山和大湖，去欧洲能体验丰富的文化生活，每对新人可以按他们的需要做选择。总之，出国结婚的选择多种多样，只要你有钱，都可以办到。",
      "More and more young Chinese people choose to get married abroad. Although marrying abroad is not necessarily cheap, they can have a rather unforgettable wedding and also tour the beautiful scenery abroad. Half a year to a year before the wedding they first find a wedding-planning agency to help them plan and arrange the procedures for marrying overseas. The couple arrive one to two days before the wedding, and after resting a few days they first take wedding photos at several famous scenic spots and then hold the wedding. After the wedding they spend their honeymoon locally and sometimes also rent a car to look around. A few recently popular overseas wedding places include Europe, islands, Australia and New Zealand. Island weddings are generally cheaper than Europe or Australia and New Zealand, so many couples who plan to invite family and friends choose such places. Australia and New Zealand have beautiful high mountains and big lakes, and going to Europe lets you experience a rich cultural life; each couple can choose according to their needs. In short, the choices for marrying abroad are many and varied, and as long as you have money, you can do it. (the book writes 1-2 in digits)")
WQ = [("他们为什么选择到国外结婚？", "Activity 3B (my questions and answers), Q1: Why do they choose to marry abroad?"), ("因为可以有一个比较难忘的婚礼，还可以游览国外美丽的风景。", "A1: Because they can have a rather unforgettable wedding and tour the beautiful scenery abroad."),
      ("结婚前半年到一年，新人们先做什么？", "Q2: Half a year to a year before the wedding, what do the couple do first?"), ("他们先找婚礼代办公司帮他们计划和安排海外结婚的手续。", "A2: They first find a wedding-planning agency to help plan and arrange the procedures."),
      ("为什么很多人选择海岛婚礼？", "Q3: Why do many people choose island weddings?"), ("因为海岛婚礼一般比欧洲或澳、新便宜，适合邀请家人朋友参加。", "A3: Because island weddings are generally cheaper than Europe or Australia and New Zealand and suit couples who invite family and friends.")]
WS = [("越来越多中国年轻人到国外结婚，因为可以有难忘的婚礼，还可以游览风景。他们先找代办公司安排手续，到了以后先拍结婚照，再办婚礼，然后度蜜月。海岛便宜，澳洲、新西兰风景美，欧洲文化丰富。", "Activity 3A (my summary): More and more young Chinese people marry abroad, because they can have an unforgettable wedding and see the scenery. They first find an agency to arrange the procedures, and after arriving first take wedding photos, then hold the wedding and then go on honeymoon. Islands are cheap, Australia and New Zealand have beautiful scenery, and Europe has a rich culture.")]
TF = [("年轻的中国游客喜欢自由行，也比较常用移动支付。", "Activity 4C, statement 1: Young Chinese tourists like independent travel and also use mobile payment more often."), ("中国游客常去美国和欧洲购物，吃美食。", "Statement 2: Chinese tourists often go to America and Europe to shop and eat delicacies."),
      ("旅行团并没有因为自由行受欢迎而降温。", "Statement 3: Tour groups have not cooled down because independent travel is popular."), ("中国人参加旅行团多半是因为价钱便宜而且会安排吃美食。", "Statement 4: Chinese people join tour groups mostly because the price is cheap and meals of delicacies are arranged. (true or false depends on the four audios, which are not in the book, so there is no key)")]
L6 = lesson(
    "Lesson 26 Presentation 3 skill integration: Chinese tourists, a graduation trip and weddings abroad",
    "吸引 打卡 · 中国游客扫货 · 毕业旅行 · 难忘 婚礼 新人 · 到国外结婚 · 神话和事实",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Reading, Speaking and Listening)",
             "A. Read the passage and answer the questions: 1. What does the number 1.6 refer to in the first paragraph? 2. What are two things Chinese tourists tend to purchase abroad? 3. What are three kinds of services do other countries offer to Chinese tourists? 4. What does the author conclude about Chinese tourists today? B. Relate your answers to a partner in Chinese. C. Discuss with your partner in Chinese the differences and similarities between this passage and Presentation 3, then fill in the table. The passage, my answers and my table:",
             tables=[SKV3, SK1T], examples=[D(*SKP3)] + [D(z, e) for z, e in SK1K]),
        card("Skill Integration, Activity 2 (Listening, Speaking, Writing and Reading)",
             "A. Listen to the dialog and answer the questions: 1. What are two things 美华 did recently? 2. What does she plan to do next? 3. What are three services the company mentioned provides? 4. What special or extra services does this company provide? B. Relate your answers to a partner in Chinese. C. Write a class graduation trip plan with your partner in Chinese, then post it on a class website. D. As a class, decide on the best plan in Chinese. (The dialog is audio and not in the book; my sample plan follows.)",
             examples=[D(*SKW)]),
        card("Skill Integration, Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Read the passage and summarize it. B. Based on the passage content, write three questions in Chinese to ask a partner, then take turns asking and answering. C. Other than the U.S., what country would you consider getting married in and why? Discuss with your partner in Chinese. The passage, my summary and my questions:",
             tables=[SKV4], examples=[D(*WD)] + [D(z, e) for z, e in WS + WQ]),
        card("Skill Integration, Activity 4 (Listening, Speaking and Reading)",
             "A. Listen to the first two of four audios about Chinese tourist habits, while a partner listens to the last two. Then fill in your parts of the table with which habits are myths and which are true (Myth and Truth, rows 1 to 4). B. Convey your information to your partner in Chinese so they can fill in the rest of their table. C. Read the statements below and mark them true or false based on the audios. D. Discuss with your partner in Chinese what information most surprised you and why. (Audio; the four statements are:)",
             examples=[D(z, e) for z, e in TF]),
    ],
    exercises=[
        M("How many Chinese outbound tourists were there in 2019?", "160 million", ["16 million", "1.6 billion", "6 million"], "一点六亿."),
        M("Which Italian goods are on Chinese tourists’ shopping lists?", "Brand-name clothing", ["Cars", "Cameras", "Wine only"], "意大利的名牌服装."),
        M("Which of these is a service offered to attract Chinese tourists?", "Chinese-speaking waiters", ["Free flights", "Tax refunds", "Free visas"], "提供会说中文的服务员."),
        M("What do Chinese tourists prefer now?", "Distinctive, high-quality travel", ["Only shopping", "Only photos", "Only tour groups"], "有特色，高质量的旅游."),
        M("What is the real purpose of travel for them?", "Experiencing foreign culture and getting to know the world", ["Buying brand names", "Checking in on social media", "Saving money"], "体验外国文化，认识世界."),
        M("What does 打卡 mean here?", "“Check in” on social media at scenic spots", ["Punch a time clock", "Pay by card", "Pack luggage"], "打卡."),
        M("Why do many young Chinese marry abroad?", "For an unforgettable wedding and beautiful scenery", ["It is always cheaper", "It is required", "It is faster"], "比较难忘的婚礼."),
        M("What do couples do first, before the wedding?", "Take wedding photos at famous scenic spots", ["Go on honeymoon", "Rent a car", "Visit museums"], "先在几个有名的风景点拍结婚照."),
        M("Which place is generally cheaper for a wedding?", "An island", ["Europe", "Australia", "New Zealand"], "海岛婚礼一般比欧洲或澳、新便宜."),
        M("What does 新人 mean?", "Newlywed/bride", ["New teacher", "New customer", "Newcomer"], "新人: xīnrén."),
        F("海岛婚礼一般比欧洲或澳、新便___。", "宜", PART, "便宜: cheap."),
        F("他们会先找婚礼代办公司帮他们计划和安排海外结婚的手___。", "续", PART, "手续: procedures."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese
DR = ("要是你想在美国开车自驾游很容易，但是出发前你得做一些准备。你得先决定你想去哪里，要去几天。你可以上网查一下，路上有哪些有意思的风景点或名胜古迹，晚上可以住在哪里。按照这些信息，你可以安排你的路线。安排好你的旅游路线后，你得准备你的车子，如果你没有自己的车，你可以跟租车公司预定，租一台适合你的车。如果你不想花太多钱住旅馆，你也可以租一辆房车睡在车上。接下来，你得收拾行李，准备路上吃的和用的东西。收拾行李以前最好查一下天气，如果会下雨，别忘了带雨衣。另外，在美国自驾游，在路上的时间很长，而且路上不一定能找到餐厅，所以最好带一些小吃和水。有时候在路上也会生病，所以最好也准备一些常用药。最后出发前，别忘了检查你的车子，带上地图，为你的手机充电，这样要是路上有什么问题，你可以随时打电话找人帮忙。另外，别忘了也告诉你的家人你的路线，让他们放心。",
      "If you want to take a self-drive tour in America it is easy, but before setting out you have to make some preparations. You have to first decide where you want to go and for how many days. You can look online at which interesting scenic spots or historic sites there are on the way and where you can stay at night. According to this information you can arrange your route. After arranging your route, you have to prepare your car; if you don’t have your own car, you can reserve with a car rental company and rent a car that suits you. If you don’t want to spend too much on hotels, you can also rent an RV and sleep in the car. Next, you have to pack and prepare things to eat and use on the way. Before packing it is best to check the weather; if it will rain, don’t forget to bring a raincoat. In addition, on a self-drive tour in America the time on the road is long and you may not find a restaurant on the road, so it is best to bring some snacks and water. Sometimes you also get sick on the road, so it is best to also prepare some common medicines. Finally, before setting out, don’t forget to check your car, bring a map and charge your phone, so that if there is any problem on the road you can phone for help at any time. In addition, don’t forget to tell your family your route to put their minds at ease.")
CM = table(["", "第一步", "第二步", "第三步", "第四步"],
           [["Main Idea", "决定去哪里，去几天，安排路线", "准备车子", "收拾行李，准备路上吃的和用的东西", "出发前检查"],
            ["Elaboration", "上网查路上有意思的风景点或名胜古迹，晚上住在哪里，按照这些信息安排路线", "没有车就跟租车公司预定，租一台适合的车；不想住旅馆就租房车睡在车上", "先查天气，会下雨就带雨衣；带小吃和水；准备常用药", "检查车子，带上地图，为手机充电，随时打电话找人帮忙；告诉家人路线，让他们放心"]],
           title="Activity 1A: my concept map (the book’s bubbles and boxes are blank)", say=[1, 2, 3, 4])
IS1 = ("普吉岛，泰国：消费低，体验丰富，适合一家老小。旺季：十一月到四月。停留时间：四到五天。消费：机票便宜，物价不高。普吉岛特点：普吉发展得很早，有丰富的水上运动和夜生活，可以体验到泰国的文化。附近的几个小岛，包括大小ＰＰ岛、零零七岛等，海水很蓝，选择跳岛游非常不错。",
       "1. Phuket, Thailand: low cost, rich experiences, suits a whole family old and young. High season: November to April. Length of stay: four to five days. Cost: air tickets are cheap and prices are not high. Features of Phuket: Phuket developed very early and has rich water sports and nightlife, and you can experience Thai culture. The nearby small islands, including the big and small PP islands and 007 Island, have very blue sea, and an island-hopping tour is very good. (the book adds pinyin and Latin letters and numerals; spelled out here)")
IS2 = ("长滩岛，菲律宾：最好的白沙滩，超多水上运动。旺季：十一月到二月。停留时间：四天。消费：有豪华也有便宜的地方。长滩岛特点：世界上最有名最好的白沙滩，让长滩岛成为菲律宾最有名的旅游地之一。长滩岛不大，这里的美景、美食、购物、娱乐设施和酒店都在沙滩边。休闲运动成了这里最重要的体验活动。这里的购物街Ｄ－ＭＡＬＬ是整个长滩岛最热闹的地方。“星期五海滩”是长滩岛最美沙滩，在沙滩上散步非常舒服。",
       "2. Boracay, the Philippines: the best white sand beach, lots of water sports. High season: November to February. Length of stay: four days. Cost: there are both luxurious and cheap places. Features of Boracay: the world’s most famous and best white sand beach has made Boracay one of the Philippines’ most famous travel destinations. Boracay is not big; the beautiful scenery, delicacies, shopping, entertainment facilities and hotels are all by the beach. Leisure sports have become the most important experience here. The shopping street D-MALL here is the liveliest place on the whole of Boracay. “Friday Beach” is Boracay’s most beautiful beach, and strolling on the sand is very comfortable. (the book writes D-MALL in Latin letters, written here in full-width letters; the book prints the pinyin of 长滩岛 as zhǎngtāndǎo, but the standard reading, Chángtān Dǎo, is used here)")
IS3 = ("巴厘岛，印尼：岛大景点多，适合各种人，可安排多种多样的行程。旺季：四月到九月。停留时间：四天。消费：机票、酒店价钱贵一点，其他消费不高。巴厘岛特点：巴厘岛比较大，差不多跟国内一个省一样大，开发的比较早，所以有各种景点和水上活动。除了有美丽的海景、山景外，岛上还有丰富的文化。另外，这里也是有名的“婚礼之都”、“蜜月之岛”。不过亲子游、老人的休闲游、和一个人的旅行也很适合来这里。",
       "3. Bali, Indonesia: a big island with many sights, suits all kinds of people, and varied itineraries can be arranged. High season: April to September. Length of stay: four days. Cost: air tickets and hotels are a bit pricey, other costs are not high. Features of Bali: Bali is rather big, about as big as a province at home, and was developed rather early, so it has all kinds of sights and water activities. Besides beautiful sea and mountain views, the island also has a rich culture. In addition, it is the famous “capital of weddings” and “island of honeymoons”. But parent-child trips, leisure trips for older people and solo travel are also well suited to coming here. (source note: adapted from a Q&A website; the book adds the pinyin of the island names)")
IT = table(["Island", "Pros (mine)", "Cons (mine)"], [["普吉岛", "消费低，体验丰富，适合一家老小；水上运动和夜生活多；可以跳岛游", "旺季是十一月到四月，其他时候不一定好"], ["长滩岛", "有最好的白沙滩，水上运动多，美景美食购物都在沙滩边；有豪华也有便宜的地方", "岛不大，旺季只有十一月到二月，停留四天"], ["巴厘岛", "岛大景点多，适合各种人；有丰富的文化；婚礼和蜜月都很有名", "机票、酒店价钱贵一点"]],
          title="Activity 2B: the pros and cons of the three islands (the book’s table is blank)", say=[0, 1, 2])
IP = ("我们选择普吉岛。因为消费低，机票便宜，物价不高，而且有丰富的水上运动，适合一家老小。我们打算十一月去，停留五天。第一天休息，第二天到第四天玩水上运动，坐船去几个小岛，第五天逛街买东西，晚上看表演。总之，普吉岛又便宜又好玩。",
      "Activity 2D–F (my sample plan; the book asks for discussion of budget, transportation, itinerary and lodging, and for the plan to be posted and presented): We choose Phuket, because the cost is low, air tickets are cheap, prices are not high, and there are rich water sports suiting a whole family. We plan to go in November and stay five days. The first day we rest, on the second to fourth days we do water sports and take a boat to a few small islands, and on the fifth day we shop and watch a show in the evening. In short, Phuket is both cheap and fun.")
RV = table(["生词", "拼音", "English"], [["输入", "shūrù", "enter"]], title="Activity 3: new vocabulary", say=[0])
M1 = ("美国大都会博物馆。地点：纽约。参观费用：大人二十五美元；老人十七美元；学生十二美元。开放时间：星期二至星期四以及星期日：上午九点半至下午五点十五分；星期五和星期六：上午九点半至晚八点四十五分；感恩节、圣诞节以及元旦除外。大都会艺术博物馆是美国最大的艺术博物馆，也是世界著名博物馆。位在美国纽约第五大道上的八十二号大街，它的对面是另一个著名的博物馆，美国自然历史博物馆。大都会博物馆每年有超过五百万人次的游客，是纽约市最热门的旅游景点之一。",
      "1. The Metropolitan Museum of Art, USA. Location: New York. Admission: adults $25; seniors $17; students $12. Opening hours: Tuesday to Thursday and Sunday: 9:30 a.m. to 5:15 p.m.; Friday and Saturday: 9:30 a.m. to 8:45 p.m.; except Thanksgiving, Christmas and New Year’s Day. The Metropolitan Museum of Art is the largest art museum in America and also a world-famous museum. It is located on 82nd Street on Fifth Avenue in New York, across from another famous museum, the American Museum of Natural History. The Metropolitan Museum has over five million visits a year and is one of New York City’s most popular tourist attractions. (the book writes the figures in digits and adds the pinyin of the name)")
M2 = ("国家航空航天博物馆。地点：华盛顿特区。参观费用：免费。开放时间：每天十点至十七点三十分，夏季十点至十九点三十分。美国国家航空航天博物馆在一九七六年七月开馆，是一座和飞行有关的著名博物馆。每月有超过十万多个游客来这里参观。这个博物馆有二十四个展厅，每个展厅介绍飞行的历史，有名的飞行员还有最早的飞机。除了多种多样的飞机以外，这个博物馆还有许多飞机发明以前的东西，比方说热气球等。观众有很多机会能自己动手做，也可以随便拍照，非常有意思。",
      "2. The National Air and Space Museum. Location: Washington, D.C. Admission: free. Opening hours: every day 10:00 to 17:30, in summer 10:00 to 19:30. The National Air and Space Museum in the U.S. opened in July 1976 and is a famous museum about flight. Over 100,000 visitors come to visit every month. The museum has 24 exhibition halls, and each hall introduces the history of flight, famous pilots and the earliest airplanes. Besides many kinds of airplanes, the museum also has many things from before airplanes were invented, such as hot-air balloons. Visitors have many chances to do things themselves and may take photos freely, which is very interesting. (the book writes the figures in digits)")
MS = [("大都会博物馆在纽约，是美国最大的艺术博物馆，每年有超过五百万人次的游客，参观费用大人二十五美元。", "Activity 3C (my summary of museum 1): The Metropolitan Museum is in New York, the largest art museum in America, with over five million visits a year, and admission is $25 for adults."),
      ("国家航空航天博物馆在华盛顿特区，参观免费，有二十四个展厅，介绍飞行的历史，观众可以自己动手做，也可以拍照。", "(my summary of museum 2): The National Air and Space Museum is in Washington, D.C., admission is free, it has 24 halls introducing the history of flight, and visitors can do things themselves and take photos.")]
L7 = lesson(
    "Lesson 26 Presentation 3 using Chinese in context: a road trip, three islands and two museums",
    "自驾游的准备 · 房车 · 普吉岛 长滩岛 巴厘岛 · 旺季 · 大都会博物馆 · 国家航空航天博物馆 · 输入",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. Read the following instructions, then fill in the bubbles and boxes (Main Idea and Elaboration for 第一步, 第二步, 第三步, 第四步) to create a concept map. B. Using your concept map, tell the instructions to a partner in Chinese. C. Think of a road trip or foreign travel experience. Use the above format to instruct your partner on how to prepare for such a trip. Your partner will draw a concept map based on your instructions. The instructions and my concept map:",
             tables=[CM], examples=[D(*DR)]),
        card("Using Chinese in Context, Activity 2 (Reading, Speaking, Listening and Writing)",
             "You and some Chinese friends decide to go on an island trip. After researching online, you narrow it down to the three postings below. A. Form groups of three. Each member reads a different passage, then tells their partners about it. B. Discuss the pros and cons of each island, then fill in the table. C. Visit two travel sites (the book names 携程旅行 and 无二之旅; the web addresses are left out) to help plan your trip. D. Discuss the following: travel budget, transportation, itinerary, lodging. E. Post your travel plan on a class site, then present it to the class. F. As a class, decide on the best travel plan. The three postings, my table and my sample plan:",
             tables=[IT], examples=[D(*IS1), D(*IS2), D(*IS3), D(*IP)]),
        card("Using Chinese in Context, Activity 3 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the radio ad and answer the questions: 1. What happened on 9/21? 2. What is unique about this year’s event? 3. How do you apply for this benefit? 4. What do you need to be careful about? B. Compare answers with a partner. C. Read one of the museum introductions while your partner reads the other, then write a summary of it. D. Based on your summary, tell your partner about your museum. E. Tell your partner about your favorite museum and why it’s your favorite. (The radio ad is audio and not in the book; the two introductions and my summaries follow.)",
             tables=[RV], examples=[D(*M1), D(*M2)] + [D(z, e) for z, e in MS]),
        card("Using Chinese in Context, Optional Activity 4 (Listening, Writing and Speaking)",
             "A. Watch one of the following two videos while a partner watches the other, then fill in the table (Route, Recommended Stops, Additional Info): Road Trip Video 1 (0:26–1:25) and Road Trip Video 2 (1:26–2:06). B. Share your information with your partner in Chinese. C. Your teacher wants to take some visiting family members on a weeklong road trip; she asks you and your partner to help her plan it. Conduct additional research online and discuss possible routes. D. Present a PowerPoint travel plan for the class on the following: most suitable road trip vehicles, ideal number of stops per day, distance between stops, lodging and dining options, travel budget, additional information. E. As a class, decide on the best travel plan. (The videos and links are not included.)"),
    ],
    exercises=[
        M("What do you have to decide first for a self-drive tour?", "Where to go and for how many days", ["Which car to buy", "Which hotel to book", "Which songs to play"], "你得先决定你想去哪里，要去几天."),
        M("What can you rent if you don’t want to spend much on hotels?", "An RV", ["A boat", "A train", "A house"], "租一辆房车睡在车上."),
        M("What should you check before packing?", "The weather", ["The news", "The map", "The price"], "收拾行李以前最好查一下天气."),
        M("Why bring snacks and water?", "You may not find a restaurant on the road", ["They are free", "Cars need them", "The police ask for them"], "路上不一定能找到餐厅."),
        M("Which island is Phuket’s country?", "Thailand", ["The Philippines", "Indonesia", "Vietnam"], "普吉岛，泰国."),
        M("Which island is famous for its white sand beach?", "Boracay", ["Phuket", "Bali", "Hawaii"], "长滩岛: 最好的白沙滩."),
        M("Which island is called the “capital of weddings”?", "Bali", ["Boracay", "Phuket", "Singapore"], "婚礼之都."),
        M("What is the high season for Boracay?", "November to February", ["April to September", "November to April", "June to August"], "十一月到二月."),
        M("What is the admission for the Air and Space Museum?", "Free", ["$25", "$12", "$17"], "免费."),
        M("How many exhibition halls does the Air and Space Museum have?", "Twenty-four", ["Twelve", "Forty", "Six"], "二十四个展厅."),
        F("你得先决定你想去哪里，要去几___。", "天", PART, "几天: how many days."),
        F("这里的购物街是整个长滩岛最___闹的地方。", "热", PART, "热闹: lively."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 26 Presentation 3 vocabulary", "23 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. In the PDF the entry 多种多样 is broken by page layout and is written out in full.", VOC3)

# ------------------------------------------------------------------ 9. area studies
ASN = table(["Country", "New Chinese students, 2018–19"], [["U.S.", "363,341"], ["Australia", "192,984"], ["Canada", "143,412"], ["Japan", "107,269"], ["U.K.", "95,090"], ["South Korea", "68,105"], ["New Zealand", "40,323"], ["France", "35,043"], ["Germany", "34,997"], ["Russia", "22,209"]],
            title="The distribution of new Chinese students in ten countries during the 2018–19 academic year (the book prints Japan as 107, 269)")
L9 = lesson(
    "Lesson 26 Area Studies: Overseas Chinese Students",
    "玄奘 · 容闳 · 留学生 · 1978年以来的留学 · 美国的中国留学生 · K-12",
    requires=[],
    cards=[
        card("Overseas Chinese Students (1): Xuanzang and Yung Wing",
             "China has engaged in cultural exchanges with other nations for centuries. One of the most important components of cultural exchange has been study abroad. Since the early 20th century, overseas Chinese students have contributed significantly to both their home and host nations. The first overseas Chinese student of note is Xuanzang (玄奘 Xuánzàng, 602–664), a Tang 唐 Dynasty (618–907) monk who crossed the vast Gobi Desert to study Buddhism in India in 631. He returned to the Tang capital of Chang’an 长安 (西安) in 645 after 18 years of study and travel. From 1847 to 1978, over 130,000 Chinese students studied abroad. Yung Wing (容闳 Róng Hóng, 1828–1912) came to the U.S. in 1847 with two other Chinese students. In 1854, he became the first Chinese student to graduate from an American university, Yale College. He helped China conduct business with the U.S., and brought students from China to study in the U.S. through the Chinese Educational Mission. He went on to become a naturalized American citizen, although his citizenship was later revoked under the Naturalization Act of 1870. (two portraits are not included)"),
        card("(2) After 1949 and the figures since 1978",
             "After the founding of the People’s Republic of China in 1949, over 10,000 students studied overseas in the 1950s and 1960s. According to the PRC Ministry of Education, a total of 5.86 million Chinese studied abroad between 1978 and 2018; 4.32 million completed their studies, of which 3.65 million chose to return to China. In 2019, the number of Chinese students studying in the U.S. alone exceeded 1 million. The following table shows the distribution of new Chinese students studying in various countries during the 2018–19 academic year:",
             tables=[ASN]),
        card("(3) Chinese students in the U.S. and fields of study",
             "New Chinese students in the U.S. during the 2018–19 academic year numbered 363,341, a 1.7% increase over the prior year. In all, Chinese students accounted for 33.7% of international students in the U.S. In 2018–19, engineering remained the most popular field of study for overseas Chinese, with 230,780 students accounting for 21.1% of the total number in the U.S. Those studying mathematics and computer science increased by 9.4% over the previous year to 203,461, 18.6% of the U.S. total. Conversely, the number of students studying business administration decreased by 7.1% from the prior year to 182,170, 16.6% of the total."),
        card("(4) K-12 students, the effects of study abroad and the resources",
             "In recent years, overseas Chinese K-12 students have been on the rise. In 2018, roughly 85,000 Chinese students enrolled in K-12 programs in the U.S., comprising half of all foreign K-12 students, according to INS, ICE and HSI statistics. Chinese students who have studied abroad continue to affect political, economic, military, technological, educational, social and cultural change and development in China. At the same time, education abroad programs are a valuable channel for the academic exchange of science, technology, medicine and culture between China and other countries, promoting mutual understanding and friendship among nations. Resources (titles only; the web addresses are left out): 40 年赴美留学史; 留学 近代中国的五次浪潮, 北京日报."),
    ],
    exercises=[
        M("Who is the first overseas Chinese student of note?", "Xuanzang, a Tang Dynasty monk", ["Yung Wing", "Confucius", "Zheng He"], "玄奘."),
        M("Where did Xuanzang travel to study Buddhism?", "India", ["Japan", "Korea", "Persia"], "To India in 631."),
        M("When did Xuanzang return to Chang’an?", "645, after 18 years", ["631, after 5 years", "664, after 30 years", "602, after 1 year"], "645 after 18 years."),
        M("Who was the first Chinese student to graduate from an American university?", "Yung Wing", ["Xuanzang", "Sun Yat-sen", "Hu Shih"], "容闳, Yale College, 1854."),
        M("Which American university did Yung Wing graduate from?", "Yale College", ["Harvard", "Princeton", "Columbia"], "Yale College."),
        M("How many Chinese studied abroad between 1978 and 2018?", "5.86 million", ["586,000", "58.6 million", "13 million"], "5.86 million."),
        M("How many of the students who completed their studies chose to return to China?", "3.65 million", ["4.32 million", "1 million", "5.86 million"], "3.65 million of 4.32 million."),
        M("Which country had the most new Chinese students in 2018–19?", "The U.S.", ["Australia", "Canada", "Japan"], "363,341."),
        M("What share of international students in the U.S. were Chinese?", "33.7%", ["1.7%", "21.1%", "85%"], "33.7%."),
        M("What was the most popular field of study for overseas Chinese in 2018–19?", "Engineering", ["Business administration", "Medicine", "Law"], "Engineering, 230,780 students."),
        M("Which field decreased by 7.1% from the prior year?", "Business administration", ["Engineering", "Mathematics and computer science", "Art"], "Business administration, to 182,170."),
        M("Roughly how many Chinese students were enrolled in K-12 programs in the U.S. in 2018?", "85,000", ["8,500", "850,000", "1 million"], "About half of all foreign K-12 students."),
    ],
)

UNIT = unit("第二十六课 Presentation 3: 中国人出国旅游, 多重复句, 有些人, 总之, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
