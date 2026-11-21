"""Unit 84: Lesson 27 (New Careers), Presentation 2, second half: the skill-integration tasks (Viya, Li Ziqi, Guo Jierui), the using-Chinese tasks (Li Jiaqi and Viya, Dianxi Xiaoge, PewDiePie)
and the vocabulary list. Audio, pictures, videos and websites are not included; numbers the book writes as digits are spelled out in Chinese text;
Latin-letter names in the spoken text are written full-width; the bracketed glosses are given in tables; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l27_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('重庆', 0, 'chong2'), ('觉得看', 1, 'de5'), ('教大家', 0, 'jiao1')):
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
NOUN = ["主播", "粉丝", "直播"]

# ------------------------------------------------------------------ 1. skill integration 1-2 (Viya, Li Ziqi)
VQ1 = [("为什么薇娅被称为“淘宝第一女主播”？", "Activity 1B, Segment 1, 1 (audio): Why is Viya called the “No. 1 female streamer on Taobao”?"), ("薇娅做直播以前做过什么工作？", "Segment 2, 2: What jobs did Viya do before live streaming?"), ("薇娅第一次做直播有多少人看？", "3: How many people watched Viya’s first live stream?"), ("她参加主播卖货比赛的结果怎样？", "4: What was the result of her taking part in a streamer sales contest?"), ("薇娅在直播间里卖什么？她的商品好卖吗？", "Segment 3, 1: What does Viya sell in her live room? Do her goods sell well?"), ("为什么说薇娅直播间里的商品很有竞争力？", "Segment 4, 1: Why do we say the goods in Viya’s live room are very competitive?")]
VD = [("你知道美国有哪些卖商品的直播平台？", "Activity 1D: Do you know which live-streaming platforms selling goods there are in the U.S.?"), ("你知道谁是最能卖货的主播？", "Do you know who the best-selling streamer is?"), ("你最喜欢哪个主播？你常常在那个直播平台买什么？", "Which streamer do you like best? What do you often buy on that platform?"), ("你觉得在直播平台买东西有什么好的地方和不好的地方？", "What do you think are the good points and the bad points of buying things on a streaming platform?")]
LZ = ("“美食博主”李子柒现在火了，油管上的粉丝超过千万，全球粉丝有一亿多，这位九零后女孩是怎么做到呢？李子柒家在四川农村。在她很小的时候，父母离婚了，她和爷爷奶奶一起生活。因为家里生活困难，她十四岁就去城里打工，做过饭馆的服务员，也在酒吧工作过。有一次，她奶奶病得很厉害，她决定回老家照顾奶奶。回来后，她开了一个淘宝网店。为了让生意好起来，她拍了一些视频介绍自己的网店。后来，她就把自己做饭的过程拍下来，放到网上，结果这些视频越来越受欢迎。因为没有时间做网店，她就把淘宝店关掉了。李子柒的视频大部分是做美食，不同的季节做不同的菜，也有一些视频是做手工的，比如手工造纸，用竹子做家具等。她的视频画面优美，还有好听的音乐，做出来的菜也漂亮，让人看了就想吃。很多人觉得看她做菜就是一种享受，她在视频里一句话也不说，静静地做菜，让人觉得特别放松。一个粉丝说，“看你的视频，是我一天中感到最安静的时候。”现在，李子柒有了自己的品牌，在淘宝网开了一个店，卖她自己做的各种美食。",
      "The “food blogger” Li Ziqi is hot now: she has over ten million fans on YouTube and over 100 million fans worldwide. How did this post-90s girl do it? Li Ziqi’s home is in the countryside of Sichuan. When she was very young her parents divorced and she lived with her grandparents. Because life at home was hard, she went to the city to work at fourteen, worked as a restaurant waitress and also worked in a bar. Once her grandmother was very sick, and she decided to go back to her hometown to take care of her. After coming back she opened a Taobao online shop. To make business better, she shot some videos to introduce her shop. Later she filmed her own cooking process and put it online, and as a result these videos became more and more popular. Because she had no time to run the shop, she closed her Taobao shop. Most of Li Ziqi’s videos are about food, making different dishes in different seasons; some videos are about handicrafts, such as making paper by hand and making furniture from bamboo. Her videos have beautiful pictures and nice music, and the dishes she makes are pretty, making people want to eat when they see them. Many people feel watching her cook is a kind of enjoyment; she says not one word in the videos and cooks quietly, which makes people feel especially relaxed. One fan said, “Watching your videos is the time of my day when I feel the quietest.” Now Li Ziqi has her own brand and has opened a shop on Taobao selling the various foods she makes herself. (translation mine; the book prints YouTube in Latin letters after 油管 and writes 90 and 14 in digits; it prints “做到呢”, which probably lacks 的)")
LZK = [("李子柒是四川农村的女孩，她做美食视频，现在是有一亿多全球粉丝的“美食博主”。", "Activity 2A, main idea (mine): Li Ziqi is a girl from rural Sichuan who makes food videos and is now a “food blogger” with over 100 million fans worldwide."),
       ("油管上的粉丝超过一千万，全球粉丝有一亿多。", "2B-1 (my answer): She has over ten million fans on YouTube and over 100 million worldwide."), ("因为她很小的时候父母离婚了，家里生活困难。", "2B-2 (my answer): Because her parents divorced when she was very young, and life at home was hard."), ("她做过饭馆的服务员，也在酒吧工作过。", "2B-3 (my answer): She worked as a restaurant waitress and also worked in a bar."),
       ("她开了一个淘宝网店，拍视频介绍自己的网店，后来把自己做饭的过程拍下来放到网上，又把淘宝店关掉了。", "2B-4 (my answer): She opened a Taobao online shop, shot videos to introduce it, later filmed her own cooking and put it online, and closed the Taobao shop."),
       ("大部分是做美食，不同的季节做不同的菜，也有手工造纸，用竹子做家具等手工视频。", "2B-5 (my answer): Most are about food, different dishes in different seasons, plus handicraft videos such as making paper by hand and furniture from bamboo."),
       ("因为画面优美，音乐好听，做出来的菜也漂亮，她不说话，静静地做菜，让人特别放松。", "2B-6 (my answer): Because the pictures are beautiful, the music is nice, the dishes are pretty, and she cooks quietly without speaking, which makes people especially relaxed."),
       ("她在自己的淘宝网店里卖。", "2B-7 (my answer): In her own Taobao shop.")]
LZD = [("你知道美国的美食博主吗？你最喜欢哪一个？", "Activity 2D: Do you know food bloggers in the U.S.? Which one do you like best?"), ("说说你喜欢的美食博主是一个什么样的人。", "Tell about what kind of person your favorite food blogger is."), ("你知道她/他有多少粉丝？", "Do you know how many fans she/he has?"), ("她/他常常做什么样的菜？", "What kind of dishes does she/he often make?")]
L1 = lesson(
    "Lesson 27 Presentation 2 skill integration: Viya and Li Ziqi",
    "薇娅 · 淘宝第一女主播 · 竞争力 · 美食博主 · 李子柒 · 九零后 · 淘宝网店 · 手工",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the recording and write the main idea you hear. B. Listen to the recording again, in segments, and answer the questions about each segment. C. Pair up and discuss the main idea and any questions about the details. Read the script if necessary. D. With your partner, discuss the following topics. E. Share your group discussion with the class. (The recording is not in the book, so there is no key; the questions are the book’s.)",
             examples=[D(z, e) for z, e in VQ1 + VD]),
        card("Skill Integration, Activity 2 (Reading, Writing and Speaking)",
             "A. Pair up and read the article about Li Ziqi and summarize the main idea in one sentence. B. Pair up and read the article again. Write the details about Li Ziqi in the table: 1. 她有多少粉丝？ 2. 她为什么和爷爷奶奶住？ 3. 她在城里做过什么？ 4. 她回老家后做了什么？ 5. 她的视频是什么内容？ 6. 为什么她的视频受欢迎？ 7. 她的美食在哪儿卖？ C. Discuss the answers with your partner. D. With your partner, talk about food influencers in the U.S. E. Share your discussion with the class. The article, my main idea and my answers:",
             examples=[D(*LZ)] + [D(z, e) for z, e in LZK]),
        card("Skill Integration, Activity 2D: talk about food influencers in the U.S.",
             "Discuss the following topics with your partner:",
             examples=[D(z, e) for z, e in LZD]),
    ],
    exercises=[
        M("Where is Li Ziqi’s home?", "The countryside of Sichuan", ["Beijing", "Shanghai", "Yunnan"], "李子柒家在四川农村."),
        M("Who did Li Ziqi live with when she was young?", "Her grandparents", ["Her teacher", "Her aunt", "Nobody"], "和爷爷奶奶一起生活."),
        M("How old was she when she went to work in the city?", "Fourteen", ["Four", "Forty", "Twenty-four"], "十四岁."),
        M("Why did she go back to her hometown?", "Her grandmother was very sick", ["She lost her job", "She wanted to study", "She was bored"], "她奶奶病得很厉害."),
        M("Why did she close her Taobao shop?", "She had no time to run it", ["It had no customers", "It was too expensive", "It was robbed"], "因为没有时间做网店."),
        M("What are some of her handicraft videos about?", "Making paper by hand and bamboo furniture", ["Fixing cars", "Painting walls", "Making clothes"], "手工造纸，用竹子做家具."),
        M("What does she say in her videos?", "Not one word", ["Only English", "Only songs", "Questions"], "一句话也不说."),
        M("What does she do now besides videos?", "Sells foods she makes on Taobao under her own brand", ["Teaches at a school", "Drives a taxi", "Runs a hotel"], "有了自己的品牌."),
        F("她的视频___面优美，还有好听的音乐。", "画", PART, "画面: picture."),
        F("很多人觉得看她做菜就是一种享___。", "受", PART, "享受: enjoyment."),
        F("为了让生意好起来，她拍了一些视___介绍自己的网店。", "频", PART, "视频: video."),
    ],
)

# ------------------------------------------------------------------ 2. skill integration 3-5 (video, Guo Jierui)
LV3 = [("李子柒在做什么食物？", "Activity 3A-1 (video): What food is Li Ziqi making?"), ("她用了什么蔬菜？", "3A-2: What vegetable does she use?"), ("除了牛肉，她还往锅里放了什么东西？", "3A-3: Besides beef, what else does she put in the pot?"), ("你还知道哪些食材？", "3A-4: What other food ingredients do you know?")]
GJ1 = ("在中国，郭杰瑞被称为美国“网红”。他原名叫Ｊｅｒｒｙ　Ｋｏｗａｌ，是纽约人。小时候他和家人一起来过中国。上大学的时候，他在台湾大学做交换学生，毕业后回到纽约。二零一七年，郭杰瑞开始拍中文视频，介绍中美文化。在他的视频里，他不仅介绍各种中国美食，而且还和中国的美食博主一起合作，教大家怎么做菜。在他很多视频里，他很能吃辣的，他常常说“这个不辣”。有一次，他去吃特别辣的重庆火锅，可他一点也不觉得辣。这么一个又能吃辣的又热爱中国美食的美国人，很快在ｂｉｌｉｂｉｌｉ网站赢得了不少粉丝。他的视频特别受欢迎，到现在，他在今日头条有三百二十一万粉丝，在ｂｉｌｉｂｉｌｉ网站有二百五十万粉丝。有了粉丝的支持，郭杰瑞更有信心去发现中国美食和文化。",
       "In China, Guo Jierui is called an American “internet celebrity”. His original name is Jerry Kowal and he is from New York. When he was little he came to China with his family. When he went to university he was an exchange student at National Taiwan University, and after graduating he returned to New York. In 2017 Guo Jierui began making Chinese videos introducing Chinese and American culture. In his videos he not only introduces all kinds of Chinese food but also collaborates with Chinese food bloggers, teaching everyone how to cook. In many of his videos he can eat spicy food and often says “This isn’t spicy”. Once he went to eat especially spicy Chongqing hotpot but didn’t feel it was spicy at all. Such an American who both can eat spicy food and loves Chinese food quickly won quite a few fans on the bilibili website. His videos are especially popular; up to now he has 3.21 million fans on Today’s Headlines and 2.5 million fans on bilibili. With his fans’ support, Guo Jierui is even more confident about discovering Chinese food and culture. (translation mine; the book writes the year and the fan counts in digits and Latin letters)")
GJ2 = ("去年三月，郭杰瑞发现云南普洱不仅有普洱茶，而且咖啡豆的质量也非常好，一些国外大公司像星巴克、雀巢等都从云南买咖啡豆。很多人不知道自己喝的咖啡其实是从云南来的。了解到这一情况后，郭杰瑞就想把云南咖啡卖到外国去。经过大半年的准备，郭杰瑞的云南咖啡卖出去了。他说他不仅要让世界了解云南咖啡，还想帮助云南的咖啡农民过上更好的生活，这是非常有意义的事情。",
       "Last March Guo Jierui discovered that Pu’er in Yunnan has not only Pu’er tea but also coffee beans of very good quality, and some large foreign companies such as Starbucks and Nestlé buy coffee beans from Yunnan. Many people don’t know that the coffee they drink actually comes from Yunnan. After learning of this situation, Guo Jierui wanted to sell Yunnan coffee abroad. After more than half a year of preparation, Guo Jierui’s Yunnan coffee was sold. He said he not only wants the world to know Yunnan coffee but also wants to help Yunnan’s coffee farmers live a better life, which is a very meaningful thing.")
GGL = table(["Gloss in the book", "Meaning"], [["郭杰瑞 (Guōjiéruì)", "Guo Jierui, the name of the American internet celebrity"], ["Jerry Kowal", "his original name"], ["今日头条 (Headlines Today)", "the news app Today’s Headlines"], ["bilibili", "a video website"], ["普洱 (pǔ’ěr)", "Pu’er, a place in Yunnan"], ["咖啡豆 (coffee beans)", "coffee beans"], ["星巴克 (xīngbākè, Starbucks)", "Starbucks"], ["雀巢 (quècháo, Nestle)", "Nestlé"]], title="Activity 4A: the glosses in brackets (left out of the spoken text)")
GJK = [("郭杰瑞是一个在中国很有名的美国网红，他拍中文视频介绍中美文化和中国美食，还想把云南咖啡卖到外国去。", "Activity 4A, main idea (mine): Guo Jierui is an American internet celebrity who is famous in China; he makes Chinese videos introducing Chinese and American culture and Chinese food, and wants to sell Yunnan coffee abroad."),
       ("郭杰瑞小时候就来过中国做交换学生。", "4B-1 (the book’s statement; my key: False, as a child he came with his family, and he was an exchange student when he went to university)"), ("郭杰瑞常常在他的视频里介绍中国美食，但他不能吃辣的。", "4B-2 (my key: False, he can eat spicy food)"), ("郭杰瑞在中国的粉丝非常多，所以他被称为美国网红。", "4B-3 (my key: True)"),
       ("一些国外大公司像星巴克、雀巢等让他去云南买咖啡豆。", "4B-4 (my key: False, those companies buy coffee beans from Yunnan themselves; he wanted to sell Yunnan coffee abroad)"), ("郭杰瑞帮助云南农民把咖啡豆卖了出去，他觉得他做了很有意义的事。", "4B-5 (my key: True)")]
GV5 = [("郭杰瑞在这个视频里主要讲的什么话题？", "Activity 5A-1 (video): What topic does Guo Jierui mainly talk about in this video?"), ("你同意他的看法吗？", "5A-2: Do you agree with his view?")]
L2 = lesson(
    "Lesson 27 Presentation 2 skill integration: a video and Guo Jierui",
    "李子柒做饭 · 郭杰瑞 · 美国网红 · 重庆火锅 · 云南咖啡 · 星巴克 · 有意义",
    requires=[],
    cards=[
        card("Skill Integration, Activity 3 (Listening, Reading, Writing and Speaking)",
             "A. Watch a video clip about Li Ziqi’s cooking and answer the questions. B. With your partner, talk about how she cooks this dish. (The video and a picture are not included, so there is no key; the questions are the book’s.)",
             examples=[D(z, e) for z, e in LV3]),
        card("Skill Integration, Activity 4 (Reading, Writing and Speaking)",
             "A. Read the following article and write the main idea in one sentence. B. Pair up and read the article again; then mark the statements as either True or False. C. Check and discuss your answers with your partner. The article, in two parts, the glosses and my key:",
             tables=[GGL], examples=[D(*GJ1), D(*GJ2)] + [D(z, e) for z, e in GJK]),
        card("Skill Integration, Activity 5 (Listening, Reading and Speaking)",
             "A. Watch a video clip and think about the following questions. B. Pair up and talk about the video with your partner. C. On YouTube, find a video made by Guo Jierui and share it with your classmates. (The video is not included, so there is no key.)",
             examples=[D(z, e) for z, e in GV5]),
    ],
    exercises=[
        M("Where is Guo Jierui from?", "New York", ["Beijing", "Taipei", "Chongqing"], "是纽约人."),
        M("Where was he an exchange student?", "National Taiwan University", ["Peking University", "Fudan University", "Harvard"], "在台湾大学做交换学生."),
        M("In what year did he start making Chinese videos?", "2017", ["1997", "2007", "2027"], "二零一七年."),
        M("What does he often say in his videos?", "“This isn’t spicy”", ["“This is expensive”", "“This is cold”", "“This is salty”"], "这个不辣."),
        M("Which hotpot did he eat that did not feel spicy to him?", "Chongqing hotpot", ["Beijing hotpot", "Yunnan hotpot", "Taipei hotpot"], "重庆火锅."),
        M("On which website did he quickly win fans?", "bilibili", ["Taobao", "Starbucks", "Nestlé"], "在bilibili网站赢得了不少粉丝."),
        M("What did he discover about Pu’er in Yunnan?", "It also has very good coffee beans", ["It has no tea", "It has no farmers", "It has no companies"], "咖啡豆的质量也非常好."),
        M("What did he want to do with Yunnan coffee?", "Sell it abroad", ["Drink it all", "Forget it", "Ban it"], "把云南咖啡卖到外国去."),
        M("What did he want to help the Yunnan coffee farmers do?", "Live a better life", ["Move to the city", "Learn English", "Stop farming"], "过上更好的生活."),
        F("上大学的时候，他在台湾大学做___换学生。", "交", PART, "交换: exchange."),
        F("他很能吃辣的，可他一点也不觉得___。", "辣", PART, "辣: spicy."),
        F("这是非常有___义的事情。", "意", PART, "有意义: meaningful."),
    ],
)

# ------------------------------------------------------------------ 3. using Chinese 1 (Li Jiaqi, Viya)
LJ1 = ("近几年，随着网络平台的发展，出现了很多带货网红，网红主播成为了热门职业，很多年轻人想成为网络主播，因为这个职业能带来相当多的收入。其实，很多人不知道这个职业也需要努力工作才能做得好。说到带货网红，薇娅是淘宝网最能卖货的主播，被叫做“淘宝一姐”。除了薇娅，淘宝网还有一个特别能卖货的男主播，叫李佳琦。因为他在淘宝网上卖口红卖得最多，被叫做“口红一哥”。二零一八年“双十一”，他和马云比赛卖口红，结果他卖得比马云多。李佳琦现在有粉丝大约五千万。",
       "In recent years, with the development of online platforms, many sales-driving internet celebrities have appeared; internet-celebrity streamer has become a popular profession, and many young people want to become online streamers because this profession can bring considerable income. Actually, many people don’t know that this profession also takes hard work to do well. Speaking of sales-driving internet celebrities, Viya is the best-selling streamer on Taobao and is called the “First Sister of Taobao”. Besides Viya, Taobao has another especially good male streamer, called Li Jiaqi. Because he sells the most lipstick on Taobao, he is called the “First Brother of Lipstick”. At Double Eleven 2018 he competed with Jack Ma in selling lipstick, and he sold more than Jack Ma. Li Jiaqi now has about 50 million fans. (translation mine; the book prints 买口红 in the sentence “他在淘宝网上买口红卖得最多”, an evident slip for 卖口红, which I have corrected, and writes 2018 and 5000 万 in digits)")
LJ2 = ("李佳琦在大学的专业是艺术，他的化妆课成绩非常好。大学毕业后，他就去卖化妆品。很多顾客买口红不喜欢自己试，他就用自己的嘴试口红。后来，他参加淘宝直播比赛，获得了很好的成绩，成为淘宝有名的主播。除了自己赚钱，他也做了很多次公益直播，帮助农民卖货。去年，他获得了“最受欢迎网络红人奖”，被选入“福布斯三十岁以下精英榜”。",
       "Li Jiaqi’s major at university was art, and his makeup class grades were very good. After graduating he went to sell cosmetics. Many customers who buy lipstick don’t like to try it themselves, so he tried lipsticks on his own lips. Later he took part in a Taobao live-stream contest, got very good results and became a famous Taobao streamer. Besides earning money for himself, he has also done many charity live streams, helping farmers sell goods. Last year he won the “Most Popular Internet Personality Award” and was selected for the “Forbes Under 30 Elite List”.")
LJG = table(["Gloss in the book", "Meaning"], [["李佳琦 (Lǐjiāqí)", "Li Jiaqi"], ["口红 (kǒuhóng, lipstick)", "lipstick"], ["化妆 (huàzhuāng, makeup)", "makeup"], ["化妆品 (huàzhuāngpǐn, cosmetics)", "cosmetics"], ["公益 (charity)", "charity"], ["福布斯 (Fúbùsī, Forbes)", "Forbes"], ["精英榜 (jīngyīng bǎng, elite list)", "elite list"]], title="Activity 1A: the glosses in brackets (left out of the spoken text)")
LJK = [("因为这个职业能带来相当多的收入。", "Activity 1A-1 (my answer): Because this profession can bring considerable income."), ("李佳琦是淘宝网的男主播，因为他卖口红卖得最多，被叫做“口红一哥”，现在有大约五千万粉丝。", "1A-2 (my answer): Li Jiaqi is a male streamer on Taobao; because he sells the most lipstick he is called the “First Brother of Lipstick”, and he now has about fifty million fans."),
       ("他在大学的专业是艺术，化妆课成绩非常好。毕业后，他去卖化妆品。", "1A-3 (my answer): His major at university was art and his makeup class grades were very good. After graduating he went to sell cosmetics."), ("他也做了很多次公益直播，帮助农民卖货。", "1A-4 (my answer): He has also done many charity live streams, helping farmers sell goods."),
       ("他获得了“最受欢迎网络红人奖”，被选入“福布斯三十岁以下精英榜”。", "1A-5 (my answer): He won the “Most Popular Internet Personality Award” and was selected for the “Forbes Under 30 Elite List”.")]
LJV = [("她在直播间卖什么？", "Activity 1C, Group A (Viya’s live sales, video): What does she sell in the live room?"), ("你觉得她卖得怎么样？", "How do you think she sells?"), ("他在卖什么？举个例子。", "Group B (Li Jiaqi’s lipstick live sales, video): What is he selling? Give an example."), ("你觉得他卖得怎么样？", "How do you think he sells?")]
LJR = [("网络直播卖货在中国越来越火。李佳琦和薇娅是淘宝网最有名的两个主播，薇娅被叫做“淘宝一姐”，李佳琦被叫做“口红一哥”，他有大约五千万粉丝。二零一八年“双十一”，他和马云比赛卖口红，结果他卖得比马云多。他们卖得那么好，主要是因为他们很努力，也很会和观众互动。", "Activity 1D (my sample report, built from the article; the book’s prompts are: how is live-stream selling in China, the background of Li Jiaqi and Viya, what do they sell on the platform, how do they sell and why do they sell so well): Live-stream selling in China is getting hotter and hotter. Li Jiaqi and Viya are the two most famous streamers on Taobao; Viya is called the “First Sister of Taobao”, Li Jiaqi the “First Brother of Lipstick”, and he has about fifty million fans. At Double Eleven 2018 he competed with Jack Ma in selling lipstick and sold more. They sell so well mainly because they work hard and are good at interacting with the audience.")]
L3 = lesson(
    "Lesson 27 Presentation 2 using Chinese in context: streaming sales in China, Li Jiaqi and Viya",
    "带货网红 · 淘宝一姐 · 口红一哥 · 李佳琦 · 化妆品 · 公益直播 · 福布斯 · 精英榜",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Listening, Reading, Writing and Speaking)",
             "Scenario: You are enrolled in a Chinese basic course and have been studying Chinese for a year. Your teacher assigns a group project asking you to write a report about streaming sales in China. You will present your group report to the class. A. Read the article and answer the following questions: 1. 现在为什么很多年轻人想成为网络主播？ 2. 李佳琦是谁？他为什么被叫做“口红一哥”？他有多少粉丝？ 3. 李佳琦在大学的成绩怎么样？毕业后，他去做什么？ 4. 除了自己直播赚钱，他还做了什么好事？ 5. 他获得了什么奖？他被选入什么精英榜？ B. Pair up and check your answers with your partner’s and decide how the information can help you with the group project. The article, the glosses and my answers:",
             tables=[LJG], examples=[D(*LJ1), D(*LJ2)] + [D(z, e) for z, e in LJK]),
        card("Activity 1C-E: videos, report and presentation",
             "C. Divide into two groups. Watch the live sales of Li Jiaqi and Viya on YouTube and write the information that you think is useful for your group project. D. Within your group, write a report about Li Jiaqi and Viya. Consolidate the information you collected from the reading and the videos. You may include: how is online live-stream selling in China; an introduction to the background of Li Jiaqi and Viya; what do they sell on the platform; how do they sell and why do they sell so well. E. Each group takes turns presenting their report to the class. The video questions are the book’s; the report is my sample:",
             examples=[D(z, e) for z, e in LJV + LJR]),
    ],
    exercises=[
        M("Why do many young people want to become online streamers?", "The profession can bring considerable income", ["It is easy and needs no work", "It is free", "It is only for old people"], "能带来相当多的收入."),
        M("Who is called the “First Sister of Taobao”?", "Viya", ["Li Jiaqi", "Li Ziqi", "Xiao Song"], "被叫做“淘宝一姐”."),
        M("Why is Li Jiaqi called the “First Brother of Lipstick”?", "He sells the most lipstick on Taobao", ["He is the tallest", "He is the oldest", "He owns a bank"], "卖口红卖得最多."),
        M("How many fans does Li Jiaqi have, roughly?", "Fifty million", ["Five thousand", "Fifty", "Five"], "大约五千万."),
        M("Who did he compete with in selling lipstick at Double Eleven 2018?", "Jack Ma", ["Viya", "Guo Jierui", "Dou Liguo"], "他和马云比赛卖口红."),
        M("What was Li Jiaqi’s major at university?", "Art", ["Law", "Cooking", "Physics"], "专业是艺术."),
        M("How did he try lipsticks for customers?", "On his own lips", ["On a doll", "On paper", "He did not try them"], "用自己的嘴试口红."),
        M("What good deed has he done besides earning money?", "Charity live streams helping farmers sell goods", ["Built hotels", "Taught Chinese", "Opened a school"], "公益直播，帮助农民卖货."),
        M("Which list was he selected for?", "The Forbes Under 30 Elite List", ["The Nobel list", "The Olympic list", "The Taobao list"], "福布斯三十岁以下精英榜."),
        F("李佳琦在大学的专业是艺___。", "术", PART, "艺术: art."),
        F("他也做了很多次公益直播，帮助农民卖___。", "货", PART, "卖货: sell goods."),
        F("说到带货网红，薇娅是淘宝网最能卖货的主___。", "播", PART, "主播: streamer."),
    ],
)

# ------------------------------------------------------------------ 4. using Chinese 2-3 (Dianxi Xiaoge, PewDiePie)
DX = ("说起美食博主，除了四川女孩李子柒，还有一个很受大家喜爱的美食博主叫滇西小哥。如果你没有看过她的视频，从名字上看，以为她是个男生，实际上她和李子柒一样，是个农村女孩。在视频里，她每天穿着普通的衣服，戴着草帽，有一条可爱的狗，做着漂亮、可口的饭菜给家里人吃。人们常常把她和李子柒比较。她们的视频很多人都爱看，在油管上都有很多粉丝，是最受欢迎的美食博主。",
      "Speaking of food bloggers, besides the Sichuan girl Li Ziqi, there is another food blogger much loved by everyone called Dianxi Xiaoge (“Little Brother of Western Yunnan”). If you haven’t watched her videos, judging from the name you might think she is a boy, but in fact, like Li Ziqi, she is a country girl. In her videos she wears ordinary clothes every day and a straw hat, has a lovely dog, and makes pretty, delicious meals for her family. People often compare her with Li Ziqi. Many people love to watch both of their videos, both have many fans on YouTube, and they are the most popular food bloggers. (translation mine; the book prints her name with the pinyin Diānxī Xiǎogē and says 油管 as YouTube)")
DXE = [("滇西小哥是一个很受大家喜爱的美食博主，是个农村女孩，名字像男生。", "Activity 2A, EEIs (essential elements of information; my list) 1: Dianxi Xiaoge is a much-loved food blogger, a country girl whose name sounds like a boy’s."), ("她每天穿着普通的衣服，戴着草帽，有一条可爱的狗，做饭菜给家里人吃。", "2: She wears ordinary clothes and a straw hat every day, has a lovely dog and cooks meals for her family."), ("她和李子柒常常被人们比较，她们在油管上都有很多粉丝。", "3: People often compare her with Li Ziqi; both have many fans on YouTube.")]
DXN = table(["", "李子柒", "滇西小哥"], [["家乡在哪儿", "", ""], ["有多少粉丝", "", ""], ["家里有什么人", "", ""], ["和家人的关系怎样", "", ""], ["做什么样的菜", "", ""], ["视频效果怎么样", "", ""], ["谁帮她们做视频", "", ""], ["她们现在的事业怎么样", "", ""]], title="Activity 2C: the notes table from the video (the book leaves the cells empty; the video is not included)")
DXC = table(["相同的地方", "不同的地方"], [["都是农村女孩；都做美食视频；在油管上都有很多粉丝；都是最受欢迎的美食博主", "李子柒是四川女孩，她的视频有好听的音乐，她一句话也不说；滇西小哥的名字像男生，她每天戴着草帽，有一条可爱的狗，做饭菜给家里人吃"]], title="Activity 2F: 比较李子柒和滇西小哥 (my sample, from the two articles only)")
PW = table(["Item", "Data (as printed in the book)"], [["Title", "PewDiePie 网红频道详情数据与分析报告; 数据更新时间 2021-07-08"], ["粉丝数", "1.1 亿"], ["总观看量", "347.7 万 0.25% (printed in this order in the book)"], ["总视频数", "4366"], ["直播收入", "230.34 万元"], ["粉丝数全球排名", "3rd (前 1%)"], ["很棒的频道", "(前 1%)"], ["单个视频合作参考费用", "63.58 万元"], ["CPM", "174.17 元-202.04 元"], ["预估曝光量", "338.01 万"], ["单月 YouTube 广告联盟收入", "155.39 万元 - 480.98 万元"], ["CPM", "11.7 元-36.23 元"]], title="Activity 3A: the report on PewDiePie (Latin letters and digits; not spoken)")
PWA = [("他有一点一亿粉丝，全球排名第三，在前百分之一。", "Activity 3A-1 (my answer, from the report): He has 110 million fans and ranks third in the world, in the top one percent."), ("按报告上写的，总观看量是三百四十七点七万。", "3A-2 (my answer, from the report; the book’s figure is printed with a stray 0.25%): According to the report the total views are 3.477 million."),
       ("他每个月的油管广告联盟收入大约是一百五十五万元到四百八十一万元，另外还有直播收入和合作视频的费用。", "3A-5 (my answer, from the report): His monthly YouTube ad-alliance income is about 1.55 million to 4.81 million yuan, plus live-stream income and fees for sponsored videos. (3A-3 and 3A-4 ask about his streams and why people like his videos; the report does not say, so they have no key)")]
PWQ = [("你知道他在油管上通常直播什么？", "Activity 3A-3: Do you know what he usually streams on YouTube?"), ("为什么很多人喜欢他的视频？", "3A-4: Why do many people like his videos?")]
L4 = lesson(
    "Lesson 27 Presentation 2 using Chinese in context: Dianxi Xiaoge and PewDiePie",
    "滇西小哥 · 美食博主 · 比较李子柒 · 相同和不同 · PewDiePie · 粉丝数 · 广告收入",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 2 (Reading, Listening, Writing and Speaking)",
             "Scenario: You are enrolled in a Chinese basic course and have been studying Chinese for a year. Your teacher assigns a group project asking you to write about new careers in China, focusing on food bloggers. You will present your group report in the class. A. Read the passage and write the EEIs below. B. Pair up and discuss the details of the reading and decide how you can use them for your group project. C. Divide the class into two groups; watch a video about Li Ziqi and Dianxi Xiaoge. Write your notes in the table. E. Within your group, discuss your notes and decide how you can use the information in your project. F. With your group members, write a report on the similarities and differences between Li Ziqi and Dianxi Xiaoge. G. Each group presents its report to the class. (Parts C and E rest on the video, which is not included.) The passage, my EEIs, the notes table and my sample comparison:",
             tables=[DXN, DXC], examples=[D(*DX)] + [D(z, e) for z, e in DXE]),
        card("Using Chinese in Context, Activity 3 (Reading, Writing and Speaking)",
             "Scenario: You are sharing an apartment with a Chinese student in Monterey. Your roommate has just come to the United States and is very interested in American YouTubers. Your roommate asks you to provide a brief introduction to your favorite YouTuber. A. Pair up and talk about the recent report about PewDiePie. Your partner plays the role of your roommate and asks the following questions. You explain the report to your roommate by answering the questions: 1. PewDiePie 有多少粉丝？在全球排第几？ 2. 全球有多少人看他的视频？ 3. 你知道他在油管上通常直播什么？ 4. 为什么很多人喜欢他的视频？ 5. 每月他能赚多少钱？他的钱从哪儿来的？ B. With your partner, introduce another YouTuber that you like to your roommate. You may ask your roommate to introduce a Chinese influencer to you as well. The report, my answers and the questions without a key:",
             tables=[PW], examples=[D(z, e) for z, e in PWA + PWQ]),
    ],
    exercises=[
        M("Who is Dianxi Xiaoge?", "A food blogger who is a country girl", ["A boy from Beijing", "A courier", "A teacher"], "实际上她和李子柒一样，是个农村女孩."),
        M("Why might you think she is a boy?", "Because of her name", ["Because of her voice", "Because of her hat", "Because of her dog"], "从名字上看，以为她是个男生."),
        M("What does she wear in her videos?", "Ordinary clothes and a straw hat", ["A uniform", "A suit", "A dress and a crown"], "穿着普通的衣服，戴着草帽."),
        M("What pet does she have?", "A lovely dog", ["A cat", "A bird", "A fish"], "有一条可爱的狗."),
        M("Who do people often compare her with?", "Li Ziqi", ["Viya", "Li Jiaqi", "Guo Jierui"], "人们常常把她和李子柒比较."),
        M("What do Li Ziqi and Dianxi Xiaoge have in common?", "Both are country girls with many fans on YouTube", ["Both live in Beijing", "Both are boys", "Both are couriers"], "农村女孩…都有很多粉丝."),
        M("Which is true of Li Ziqi but not said of Dianxi Xiaoge?", "She says not one word in her videos", ["She makes food", "She has fans", "She is a country girl"], "一句话也不说."),
        M("What does the PewDiePie report say about his world ranking by fans?", "Third", ["First", "Tenth", "Last"], "全球排名 3rd."),
        F("她和李子柒一样，是个农___女孩。", "村", PART, "农村: countryside."),
        F("人们常常把她和李子柒比___。", "较", PART, "比较: compare."),
        F("他的单月广告联盟收入大约是一百五十五万元到四百八十一___元。", "万", PART, "万: ten thousand."),
    ],
)

# ------------------------------------------------------------------ 5. vocabulary
L5 = vocab_lesson("Lesson 27 Presentation 2 vocabulary", "22 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book prints 互联网 as a verb (v.); I give it as a noun. The pinyin of 网红景点 is broken across lines by the PDF layout and is written out in full here.", VOC2)

UNIT = unit("第二十七课 Presentation 2: 薇娅, 李子柒, 郭杰瑞, 李佳琦, 滇西小哥 and vocabulary", [L1, L2, L3, L4, L5])
