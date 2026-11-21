"""Unit 83: Lesson 27 (New Careers), Presentation 2, first half: the passage about online streamers and internet celebrities with its listening activities, the words with 网 and the fill-in activity,
the patterns 把…叫做/看做/当做, 说到/想到/提到, 主要是因为, and the pre-explanation and post-explanation paragraph types.
Audio, pictures, videos and websites are not included; numbers the book writes as digits are spelled out in Chinese text; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l27_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4")):
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

# ------------------------------------------------------------------ 1. presentation 2 + activities 1-2
PA1 = ("你知道吗？在网上聊天，唱歌，吃饭也可以赚钱。随着互联网的发展，网路直播成了一个热门职业。主播们在直播平台上唱歌，跳舞，做饭，卖货，和观众互动。观众喜欢的话，就给他们打赏，他们再和网站分成。有不少主播特别受欢迎，有很多粉丝，人们把这些主播叫做“网红”。",
       "Do you know? Chatting, singing and eating online can also make money. With the development of the Internet, online live streaming has become a popular profession. On live-streaming platforms the streamers sing, dance, cook, sell goods and interact with the audience. If the audience likes it, they give the streamers rewards, and the streamers then share the profit with the website. Quite a few streamers are especially popular and have many fans; people call these streamers “internet celebrities” (网红). (translations in this card are mine)")
PA2 = ("说到“网红”，人们就会想到淘宝网的薇娅。每次直播时，她都有六百多万的粉丝观看，两个小时就可以卖到两亿多的商品。“网红主播”李子柒有最多的国外观众，她的粉丝超过千万。人们喜欢她的视频，主要是因为画面非常美，还可以了解到中国的美食和文化。不仅人可以当“网红”，而且一些名胜古迹也成了“网红”。比如，有六百年历史的故宫也在网上直播，成了“网红景点”，让更多的年轻人了解古代文物，爱上传统文化。",
       "Speaking of “internet celebrities”, people think of Viya of Taobao. Every time she streams, more than six million fans watch, and in two hours she can sell over 200 million yuan of goods. The “influencer streamer” Li Ziqi has the most foreign viewers, and her fans number over ten million. People like her videos mainly because the pictures are very beautiful and one can also learn about Chinese food and culture. Not only people can be “internet celebrities”; some famous scenic spots and historic sites have also become “internet celebrities”. For example, the Forbidden City, with a history of six hundred years, also streams online and has become an “internet-celebrity scenic spot”, letting more young people learn about ancient cultural relics and fall in love with traditional culture.")
PA3 = ("现在，网络直播已经成为很多人喜爱的工作，而且越来越火。", "Now online live streaming has become a job that many people love, and it is getting hotter and hotter. (the book also prints the passage in traditional characters)")
G2 = [("现在，越来越多的人喜欢在网路平台上直播什么？", "Activity 2A-1 (audio Passage 1): Now, more and more people like to live-stream what on online platforms?"), ("在中国，人们把那些受欢迎的主播叫什么？", "2A-2: In China, what do people call those popular streamers?"), ("这些受欢迎的主播的收入怎么样？他们的钱是怎么来的？", "2A-3: How is the income of these popular streamers? Where does their money come from?"),
      ("薇娅是淘宝网粉丝最多的“网红”。", "Activity 2D-1 (true or false, audio Passage 2): Viya is the “internet celebrity” with the most fans on Taobao."), ("薇娅第一次直播聊天时没有人观看。", "2D-2: When Viya first streamed a chat, nobody watched."), ("薇娅在直播平台上只卖服装和化妆品。", "2D-3: Viya sells only clothing and cosmetics on the streaming platform."), ("薇娅特别能卖货，两个小时可以卖出两亿多的商品。", "2D-4: Viya is especially good at selling; in two hours she can sell over 200 million yuan of goods."),
      ("李子柒从小就和爷爷直播怎么做饭。", "Activity 2G-1 (true or false, audio Passage 3): Since childhood Li Ziqi has live-streamed with her grandfather how to cook."), ("李子柒的视频不仅画面好看，而且做出来的美食也漂亮。", "2G-2: Li Ziqi’s videos not only have beautiful pictures, but the food she makes is also pretty."), ("李子柒的粉丝特别多，油管上就有一万个粉丝。", "2G-3: Li Ziqi has an especially large number of fans; on YouTube alone she has ten thousand fans. (the book writes YouTube in Latin letters after 油管)")]
GQ = [("你知道吗？在美国有哪些著名的网红？他们直播什么？", "Getting Started A (the book’s questions are in English; Chinese is mine): Do you know any famous internet influencers in the U.S.? What do they broadcast?")]
L1 = lesson(
    "Lesson 27 Presentation 2: online streamers and internet celebrities",
    "网路直播 · 主播 · 打赏 · 分成 · 网红 · 薇娅 · 李子柒 · 故宫",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. Do you know any famous internet influencers in the U.S.? What do they broadcast? B. Which social media platforms are they active on? C. How does one become an internet influencer? (Four pictures are not included.)"),
        card("Presentation 2: 网路直播和“网红”", "The three paragraphs of the presentation; the book also prints them in traditional characters.", examples=[D(*PA1), D(*PA2), D(*PA3)]),
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Global Listening: listen to Presentation 2 once through and answer the question: 1. What is discussed in this presentation? B. Detailed Listening: listen again and answer: 1. What do the streamers usually do on social media platforms? 2. How do streamers monetize their content? 3. Why are influencers called “internet celebrities”? 4. What did you learn about Viya on Taobao? 5. Why are Li Ziqi’s videos so popular? How many followers does she have? 6. What was said about the Forbidden City? C. Pair up, discuss the answers and share them with the class. My answers, from the presentation: A. 1. Online live streaming and internet celebrities. B. 1. They sing, dance, cook, sell goods and interact with the audience. 2. The audience gives rewards, and the streamers share the profit with the website. 3. Because they are especially popular and have many fans. 4. She has over six million viewers each time and can sell over 200 million yuan of goods in two hours. 5. The pictures are beautiful and viewers learn about Chinese food and culture; over ten million fans. 6. It has also become an “internet-celebrity scenic spot” by streaming online."),
        card("Activity 2 (Listening, Reading, and Speaking)",
             "A. Listen to Passage 1 and answer the questions. B. Pair up and discuss your answers. C. Talk with your partner about your favorite online influencers. D. Listen to Passage 2 and mark the statements as True or False. E. Pair up, discuss and justify your answers. F. With your partner, discuss an American streamer who sells merchandise online. G. Listen to Passage 3 and mark the statements as True or False. H. Pair up, discuss and justify your answers. I. Talk with your partner about your favorite food blogger. The passages are audio and not in the book, so the key is given only for 2D-4, which the presentation itself supports: it is True (my key). The questions and statements are the book’s:",
             examples=[D(z, e) for z, e in G2]),
    ],
    exercises=[
        M("What do streamers do on streaming platforms?", "Sing, dance, cook, sell goods and interact with the audience", ["Only teach", "Only watch", "Only sleep"], "主播们…唱歌，跳舞，做饭，卖货，和观众互动."),
        M("How do streamers earn money from the audience?", "Rewards that they share with the website", ["School fees", "Tickets", "Rent"], "打赏…和网站分成."),
        M("What do people call very popular streamers?", "网红", ["快递小哥", "海归", "保安"], "人们把这些主播叫做“网红”."),
        M("About how many fans watch Viya each time she streams?", "More than six million", ["Six hundred", "Sixty", "Six"], "六百多万的粉丝观看."),
        M("How much can Viya sell in two hours?", "Over 200 million yuan of goods", ["Two hundred yuan", "Two thousand yuan", "Nothing"], "两亿多的商品."),
        M("Who has the most foreign viewers?", "Li Ziqi", ["Viya", "Xiao Song", "Lao Li"], "李子柒有最多的国外观众."),
        M("Why do people like Li Ziqi’s videos?", "The pictures are beautiful and viewers learn about Chinese food and culture", ["They are very short", "They are free", "They are in English"], "画面非常美…了解到中国的美食和文化."),
        M("How old is the Forbidden City’s history, according to the passage?", "Six hundred years", ["Sixty years", "Six years", "Six thousand years"], "有六百年历史的故宫."),
        M("What did the Forbidden City become by streaming online?", "An internet-celebrity scenic spot", ["A school", "A hotel", "A market"], "成了“网红景点”."),
        F("随着互联网的发展，网路直播成了一个热___职业。", "门", PART, "热门: popular."),
        F("观众喜欢的话，就给他们打___。", "赏", PART, "打赏: reward."),
        F("她的___丝超过千万。", "粉", PART, "粉丝: fans."),
    ],
)

# ------------------------------------------------------------------ 2. activities 3-5
WT = table(["词", "拼音", "Meaning (mine)"], [["网路", "wǎnglù", "network"], ["互联网", "hùliánwǎng", "the Internet"], ["网络", "wǎngluò", "network, online"], ["网上", "wǎngshàng", "online"], ["上网", "shàngwǎng", "go online"], ["网站", "wǎngzhàn", "website"], ["网店", "wǎngdiàn", "online shop"], ["淘宝网", "Táobǎowǎng", "Taobao.com"], ["网红", "wǎnghóng", "internet celebrity"], ["网红景点", "wǎnghóng jǐngdiǎn", "internet-celebrity scenic spot"], ["网约车", "wǎngyuēchē", "ride-hailing car"], ["网友", "wǎngyǒu", "online friend"], ["网球", "wǎngqiú", "tennis"]], title="Activity 3: words with 网 (my sample, from this lesson and earlier lessons)", say=[0])
PPN = table(["Gloss in the book", "Meaning"], [["Papi 酱 (jiàng)", "Papi Jiang, an internet celebrity; the book glosses 酱 as jiàng"]], title="Activity 4, sentence 1: the name in Latin letters is not spoken")
K4 = [("“网红”Ｐａｐｉ酱第一次做网路直播时，一个半小时的节目，有两千人观看。", "Activity 4A-1 (my key: 网路直播): When “internet celebrity” Papi Jiang first did a live stream, her one-and-a-half-hour show had two thousand viewers."), ("故宫在网上直播古代文物以后，成了年轻人了解中国文化的网红景点。", "4A-2 (my key: 网红景点): After the Forbidden City streamed ancient cultural relics online, it became an internet-celebrity scenic spot for young people to learn about Chinese culture."),
      ("“网红”们在直播平台上不仅可以唱歌，跳舞，还可以和观众互动。", "4A-3 (my key: 互动): On streaming platforms “internet celebrities” can not only sing and dance but also interact with the audience."), ("薇娅是淘宝网最赚钱的主播，被称为“直播一姐”和“淘宝一姐”。", "4A-4 (my key: 主播): Viya is the money-making-est streamer on Taobao and is called the “First Sister of live streaming” and the “First Sister of Taobao”."),
      ("受欢迎的“网红”会得到观众的打赏，然后需要和直播平台分成。", "4A-5 (my key: 打赏, 分成): Popular “internet celebrities” get rewards from the audience and then have to share the profit with the streaming platform."), ("李子柒有很多外国粉丝。她的美食视频让很多外国人更喜爱中国饮食了。", "4A-6 (my key: 粉丝): Li Ziqi has many foreign fans. Her food videos make many foreigners like Chinese food even more.")]
S5 = [("随着网路直播的出现，出现了很多网红。人们把有很多粉丝的主播叫作“网红”。他们每次直播都和观众互动，观众喜欢的话就给他们打赏，他们再和平台分成。", "Activity 5 (my sample notes on a favorite online personality, using 随着……的出现, 把……叫作 and 和……分成): With the appearance of online live streaming, many internet celebrities have appeared. People call streamers with many fans “internet celebrities”. Every time they stream they interact with the audience; if the audience likes it they give rewards, and the streamers then share the profit with the platform.")]
L2 = lesson(
    "Lesson 27 Presentation 2 activities 3-5: words with 网, fill in the blanks and online personalities",
    "网路 · 网红景点 · 网路直播 · 打赏 · 分成 · 互动 · 随着……的出现 · 把……叫作",
    requires=[],
    cards=[
        card("Activity 3 (Speaking and Writing)",
             "A. Pair up and list words from Presentation 2, or that you learned previously with the character 网, and discuss the meaning of the words. (The book prints a word web with 网 in the middle.) B. Share your work with the class. My sample:",
             tables=[WT]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Pair up and complete the sentences using the words below: 主播 | 粉丝 | 网路直播 | 打赏 | 网红景点 | 分成 | 互动. B. With your partner, read the sentences aloud and translate them into English. C. Share your work with the class. My key (the book leaves the blanks empty):",
             tables=[PPN], examples=[D(z, e) for z, e in K4]),
        card("Activity 5 (Writing and Speaking)",
             "A. Pair up and use the following words and expressions to talk about your favorite online personalities. Make notes in the space provided: 随着……的出现 | 把……叫作 | 和……分成; 互动 | 粉丝 | 直播 | 平台. B. Share your discussion with the class. My sample:",
             examples=[D(*S5[0])]),
    ],
    exercises=[
        M("Which word fits “网红们在直播平台上还可以和观众___”?", "互动", ["分成", "打赏", "文物"], "互动: interact."),
        M("Which word means “share profit”?", "分成", ["互动", "粉丝", "主播"], "分成."),
        M("Which word means “reward” given by the audience?", "打赏", ["互动", "文物", "历史"], "打赏."),
        M("What did the Forbidden City become after streaming?", "网红景点", ["网路直播", "分成", "粉丝"], "成了年轻人了解中国文化的网红景点."),
        M("Who is called “直播一姐” and “淘宝一姐”?", "薇娅", ["李子柒", "小宋", "老李"], "薇娅是淘宝网最赚钱的主播."),
        M("What do foreign fans of Li Ziqi come to like even more?", "Chinese food", ["Hot weather", "Trains", "Hotels"], "更喜爱中国饮食."),
        M("What does 网上 mean?", "Online", ["Under the net", "A fishing net", "Next door"], "网上."),
        M("What does 网站 mean?", "Website", ["Bus stop", "Fishing place", "Library"], "网站."),
        F("“网红”们在直播平台上还可以和观众互___。", "动", PART, "互动: interact."),
        F("受欢迎的“网红”会得到观众的打___。", "赏", PART, "打赏: reward."),
        F("需要和直播平台分___。", "成", PART, "分成: share profit."),
    ],
)

# ------------------------------------------------------------------ 3. 把…叫做/看做/当做
BA0 = table(["结构", "用法"], [["Subject + 把 + A + 叫做 + B", "expresses the meaning “call A (as) B” or “A is known as B”"], ["Subject + 把 + A + 看做/当做 + B", "把 can also be used with the verbs 看 and 当, which means “regard A as B”"]], title="The Pattern 把……叫做……")
BAE = [("人们把有很多粉丝的直播主播叫做“网红”。", "叫做 1. People call live-stream hosts with many fans “internet celebrities”."), ("在中国，大家喜欢把快递员叫做“快递小哥”。", "叫做 2. In China, everyone likes to call couriers “courier guys”."),
       ("中国人把长城看做中国的象征。", "看做 1. Chinese people regard the Great Wall as a symbol of China."), ("他把自行车当做主要交通工具，去哪儿都骑自行车。", "当做 2. He regards the bicycle as his main means of transportation and rides a bicycle wherever he goes.")]
BA2 = [("我最喜欢的网红是一个美食博主，人们把她叫做“美食小姐”。她的视频画面特别美，很多人把看她的视频当做每天最放松的时间。我把她看做我学做饭的老师。她的粉丝都把她当做自己的朋友。她还把自己做的美食在网上卖，很多人都喜欢买。", "Activity 2A (my sample paragraph, five sentences, about my favorite influencer using 把……叫做/看做/当做): My favorite internet celebrity is a food blogger, and people call her “Miss Food”. Her video pictures are especially beautiful, and many people regard watching her videos as the most relaxing time of the day. I regard her as my teacher for learning to cook. Her fans all regard her as their friend. She also sells the food she makes online, and many people like to buy it.")]
L3 = lesson(
    "Lesson 27 Presentation 2 grammar: 把……叫做/看做/当做",
    "把…叫做 · 把…看做 · 把…当做 · 网红 · 快递小哥 · 长城 · 自行车",
    requires=[],
    cards=[
        card("The Pattern 把……叫做……",
             "The pattern 把……叫做 expresses the meaning “call … (as) …” or “… is known as …”. Subject + 把 + A + 叫做 + B. 把 can also be used with the verbs 看 and 当, which means “regard … as …”. Subject + 把 + A + 看做/当做 + B.",
             tables=[BA0], examples=[D(z, e) for z, e in BAE]),
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Listen to the sentences with 叫做/看做/当做 (six items) and translate what you hear into English. B. Pair up and check your translation with your partner’s. Then say the sentences aloud in Chinese with your partner. (Audio; the sentences are not in the book.)"),
        card("Activity 2 (Writing and Speaking)",
             "A. Write a paragraph about your favorite influencer by using “把……叫做/看做/当做……”. Write at least five sentences. B. Pair up and read your story to your partner. C. Share your story with the class. My sample:",
             examples=[D(*BA2[0])]),
    ],
    exercises=[
        M("What does 把A叫做B mean?", "Call A as B", ["Give A to B", "Move A to B", "Ask A about B"], "叫做."),
        M("Which verbs can replace 叫做 to mean “regard as”?", "看做/当做", ["说做/听做", "走做/跑做", "买做/卖做"], "看做/当做."),
        M("What do people call streamers with many fans?", "网红", ["保安", "厨师", "司机"], "把…叫做“网红”."),
        M("What do people in China like to call couriers?", "快递小哥", ["网红", "厨师", "老师"], "把快递员叫做“快递小哥”."),
        M("What do Chinese people regard the Great Wall as?", "A symbol of China", ["A bridge", "A river", "A school"], "把长城看做中国的象征."),
        M("What does 他把自行车当做主要交通工具 mean?", "He regards the bicycle as his main transportation", ["He sold his bicycle", "He broke his bicycle", "He bought a car"], "当做."),
        M("Which sentence is correct?", "我把她看做我的老师", ["我看做她把我的老师", "我把我的老师她看做", "把我她看做的老师"], "把 + A + 看做 + B."),
        F("人们把有很多粉丝的主播叫___“网红”。", "做", PART, "叫做."),
        F("中国人把长城看___中国的象征。", "做", PART, "看做."),
    ],
)

# ------------------------------------------------------------------ 4. 说到/想到/提到
SD0 = table(["结构", "用法"], [["说到/想到/提到……，elaboration", "at the beginning of a sentence, to attract the audience’s attention to a topic mentioned earlier and elaborated upon; equivalent to “speaking of”, “thinking of” and “mentioning/referring to”"], ["Subject + 说到/想到/提到 + Object", "in the middle of a sentence, as verbs meaning “speak about/mention”, “think of” and “mention/refer to”"]], title="说到/想到/提到")
SDE = [("说到“网红”，人们就会想到淘宝网的薇娅。", "At the beginning 1. Speaking of “internet celebrities”, people think of Viya of Taobao."), ("想到明天就要期中考试了，我心里特别紧张。", "2. Thinking that the midterm exam is tomorrow, I feel especially nervous."), ("提到那个很火的主播，我常常在她的购物平台上买衣服。", "3. Mentioning that very hot streamer, I often buy clothes on her shopping platform."),
       ("每次直播时，她都要说到打赏的事。", "In the middle 1. Every time she streams, she mentions the matter of rewards."), ("我想到了一个记单词的好办法。", "2. I thought of a good way to remember words."), ("昨天同学聚会时，周红提到了她在淘宝网开网店了。", "3. At the classmates’ party yesterday, Zhou Hong mentioned that she had opened an online shop on Taobao.")]
SD3 = [("说到“网红”，我就想到李子柒，她的视频画面特别美。", "Activity 3A-1 (my sample, 说到“网红”): Speaking of “internet celebrities”, I think of Li Ziqi; the pictures in her videos are especially beautiful."), ("想到故宫，我就想到它六百年的历史和那些古代文物。", "3A-2 (想到故宫): Thinking of the Forbidden City, I think of its six hundred years of history and those ancient cultural relics."),
       ("提到“外卖小哥”，大家都会说他们很辛苦，风里来雨里去的。", "3A-3 (提到“外卖小哥”): Mentioning “takeout guys”, everyone says they work very hard, braving wind and rain."), ("说到“爱彼迎”，很多游客都喜欢住民宿，因为又便宜又有特点。", "3A-4 (说到“爱彼迎”; the book adds the English name Airbnb): Speaking of Airbnb, many tourists like to stay in homestays because they are cheap and distinctive."),
       ("提到叫车软件，我常常用它叫车，不用现金，很方便。", "3A-5 (提到叫车软件): Mentioning ride-hailing apps, I often use one to call a car, no cash needed, which is very convenient."), ("想到下周的考试，我心里有点儿紧张，要好好复习。", "3A-6 (想到下周的考试): Thinking of next week’s exam, I feel a bit nervous and must review well.")]
L4 = lesson(
    "Lesson 27 Presentation 2 grammar: 说到/想到/提到",
    "说到… · 想到… · 提到… · 说到“网红” · 想到故宫 · 提到叫车软件 · 想到考试",
    requires=[],
    cards=[
        card("说到/想到/提到",
             "说到, 想到, 提到 are used at the beginning of a sentence to attract the audience’s attention to a topic mentioned earlier and elaborated upon. These terms are, respectively, equivalent to “speaking of,” “thinking of,” and “mentioning” or “referring to” in English. 说到/想到/提到……, elaboration. They can also be used as verbs in the middle of a sentence to mean “speak about/mention,” “think of,” and “mention/refer to,” respectively. Subject + 说到/想到/提到 + Object.",
             tables=[SD0], examples=[D(z, e) for z, e in SDE]),
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Pair up and write brief paragraphs on the following topics with your partner: 1. 说到“网红” 2. 想到故宫 3. 提到“外卖小哥” 4. 说到“爱彼迎” (Airbnb) 5. 提到叫车软件 6. 想到下周的考试. B. Share your work with the class. My samples:",
             examples=[D(z, e) for z, e in SD3]),
    ],
    exercises=[
        M("What does 说到 mean at the beginning of a sentence?", "Speaking of", ["Because of", "Instead of", "In spite of"], "说到."),
        M("What does 想到 mean at the beginning of a sentence?", "Thinking of", ["Speaking of", "Mentioning", "Regardless of"], "想到."),
        M("What does 提到 mean at the beginning of a sentence?", "Mentioning", ["Thinking of", "Because of", "Instead of"], "提到."),
        M("In 说到“网红”，人们就会想到淘宝网的薇娅, who comes to mind?", "Viya of Taobao", ["Li Ziqi", "Xiao Song", "Lao Li"], "想到淘宝网的薇娅."),
        M("Why is the speaker nervous in 想到明天就要期中考试了，我心里特别紧张?", "The midterm exam is tomorrow", ["It is raining", "The streamer is late", "The courier is late"], "期中考试."),
        M("What did Zhou Hong mention at the classmates’ party?", "She opened an online shop on Taobao", ["She got married", "She went abroad", "She lost her phone"], "提到了她在淘宝网开网店了."),
        M("In 我想到了一个记单词的好办法, what is 想到 used as?", "A verb", ["A noun", "A measure word", "A question word"], "想到了: verb."),
        F("___到“网红”，人们就会想到淘宝网的薇娅。", "说", PART, "说到."),
        F("想___明天就要期中考试了，我心里特别紧张。", "到", PART, "想到."),
        F("提到那个很火的主播，我常常在她的购物平___上买衣服。", "台", PART, "平台: platform."),
    ],
)

# ------------------------------------------------------------------ 5. 主要是因为
ZH0 = table(["结构", "用法"], [["Main clause (effect)，主要是因为……", "主要是因为 introduces a causal relationship and can be used if the speaker wants to state the effect before the cause; 主要是 is used before 因为 to emphasize that it is the main reason for the effect"]], title="主要是因为")
ZHE = [("人们喜欢她的视频，主要是因为画面非常美。", "1. People like her videos mainly because the pictures are very beautiful."), ("很多游客都喜欢住民宿，主要是因为有些民宿既有特点又便宜。", "2. Many tourists like to stay in homestays, mainly because some homestays are both distinctive and cheap.")]
ZH4 = [("这个“网红”有很多粉丝，主要是因为她的视频画面很美，也很有意思。", "Activity 4A-1 (my sample): This “internet celebrity” has many fans, mainly because her video pictures are beautiful and interesting."), ("这个直播平台的观众特别多，主要是因为很多受欢迎的主播都在这里直播。", "4A-2: This streaming platform has an especially large audience, mainly because many popular streamers stream here."),
       ("很多观众愿意给这个主播打赏，主要是因为他唱歌唱得特别好听。", "4A-3: Many viewers are willing to give this streamer rewards, mainly because he sings especially well."), ("很多人喜欢去淘宝网买东西，主要是因为东西多，价钱便宜，送货也快。", "4A-4: Many people like to shop on Taobao, mainly because there are many goods, prices are cheap and delivery is fast."),
       ("李子柒在国外有很多粉丝，主要是因为她的视频让人们了解到中国的美食和文化。", "4A-5: Li Ziqi has many fans abroad, mainly because her videos let people learn about Chinese food and culture."), ("现在故宫也成了“网红”，主要是因为故宫在网上直播，让更多的年轻人了解古代文物。", "4A-6: The Forbidden City has now also become an “internet celebrity”, mainly because it streams online and lets more young people learn about ancient cultural relics.")]
ZH5 = [("网路直播越来越火，主要是因为人们可以在网上互动，也可以一边看一边买东西。", "Activity 5A-1 (my answer): Online live streaming is getting hotter and hotter, mainly because people can interact online and can buy things while watching."), ("很多人喜欢自驾游，主要是因为自己开车去玩儿，时间和路线都比较自由。", "5A-2: Many people like self-drive tours, mainly because when you drive yourself, the time and route are fairly free."),
       ("有些中国人喜欢去国外扫货，主要是因为国外的有些东西比中国便宜，质量也好。", "5A-3: Some Chinese like to go on shopping sprees abroad, mainly because some things abroad are cheaper than in China and of good quality."), ("一些父母把孩子送到国外学习，主要是因为他们希望孩子学好外语，了解外面的世界。", "5A-4: Some parents send their children abroad to study, mainly because they hope their children learn foreign languages well and learn about the outside world."),
       ("很多中国留学生选择回国工作和生活，主要是因为中国的经济发展很快，机会很多。", "5A-5: Many Chinese students abroad choose to return and work and live in China, mainly because China’s economy is developing fast and there are many opportunities.")]
L5 = lesson(
    "Lesson 27 Presentation 2 grammar: 主要是因为",
    "主要是因为 · 为什么网路直播越来越火 · 为什么喜欢自驾游 · 扫货 · 民宿 · 回国工作",
    requires=[],
    cards=[
        card("主要是因为",
             "主要是因为 introduces a causal relationship and can be used if the speaker wants to state the effect before the cause. 主要是 is used before 因为 to emphasize that it is the main reason for the effect. Main Clause (effect), 是因为……",
             tables=[ZH0], examples=[D(z, e) for z, e in ZHE]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Pair up and write a short paragraph that explains the reasons for the following phenomena: 1. 这个“网红”有很多粉丝，主要是因为…… 2. 这个直播平台的观众特别多，主要是因为…… 3. 很多观众愿意给这个主播打赏，主要是因为…… 4. 很多人喜欢去淘宝网买东西，主要是因为…… 5. 李子柒在国外有很多粉丝，主要是因为…… 6. 现在故宫也成了“网红”，主要是因为…… B. Share your paragraphs with the class. My samples:",
             examples=[D(z, e) for z, e in ZH4]),
        card("Activity 5 (Reading, Writing, and Speaking)",
             "A. Pair up and discuss the following topics; then provide answers for them by using 主要是因为: 1. 为什么网路直播越来越火？ 2. 为什么很多人喜欢自驾游？ 3. 为什么有些中国人喜欢去国外“扫货”？ 4. 为什么一些父母把孩子送到国外学习？ 5. 为什么很多中国留学生选择回国工作和生活？ B. Share your conclusions with the class. My answers:",
             examples=[D(z, e) for z, e in ZH5]),
    ],
    exercises=[
        M("What does 主要是因为 emphasize?", "The main reason", ["The time", "The place", "The person"], "主要是…因为."),
        M("Where does 主要是因为 usually stand in the sentence?", "After the effect", ["Before the effect", "At the very end", "Inside a noun"], "Main clause (effect), 是因为…"),
        M("Why do people like Li Ziqi’s videos, according to the sentence?", "The pictures are very beautiful", ["They are very short", "They are free", "They are loud"], "主要是因为画面非常美."),
        M("Why do many tourists like to stay in homestays?", "Some are both distinctive and cheap", ["They are far away", "They are expensive", "They have no beds"], "既有特点又便宜."),
        M("Which sentence is correct?", "很多人喜欢自驾游，主要是因为时间自由", ["主要是因为时间自由，很多人喜欢自驾游主要", "很多人喜欢主要是因为自驾游，时间自由", "主要是很多人喜欢自驾游，因为时间自由是"], "Pattern."),
        M("What does 扫货 mean in 国外“扫货”?", "A shopping spree", ["Sweeping the floor", "Selling goods", "Cooking"], "扫货."),
        F("人们喜欢她的视频，主___是因为画面非常美。", "要", PART, "主要: mainly."),
        F("很多游客都喜欢住民宿，主要是___为有些民宿既有特点又便宜。", "因", PART, "因为: because."),
    ],
)

# ------------------------------------------------------------------ 6. 前解释 and 后解释
QJ0 = table(["Term", "Meaning", "Structure"], [["前解释 (pre-explanation)", "a paragraph begins with a statement of fact that naturally leads to a concept", "Statement of fact → concept"], ["后解释 (post-explanation)", "a paragraph introduces a concept first and then explains it", "Introduction of a concept → simpler explanation"]], title="前解释和后解释 (jiěshì)")
QJE = [("主播们在直播平台上唱歌，跳舞，做饭，卖货，和观众互动。观众喜欢的话，就给他们打赏，他们再和网站分成。有不少主播特别受欢迎，有很多粉丝，人们把这些主播叫做“网红”。", "前解释 example: On streaming platforms the streamers sing, dance, cook, sell goods and interact with the audience. If the audience likes it, they give rewards, and the streamers then share the profit with the website. Quite a few streamers are especially popular and have many fans; people call these streamers “internet celebrities”."),
       ("我们常常提到的“网红”，就是那些特别受欢迎，有很多粉丝的网路直播的主播。", "后解释 example 1: The “internet celebrities” we often mention are just those live-stream hosts who are especially popular and have many fans."),
       ("大家说到的“海归”，是指那些有国外学习和工作经验的留学生回到中国的人。", "后解释 example 2: The “sea turtles” (海归) that people talk about refers to those students who have study and work experience abroad and have returned to China.")]
QJ6 = [("现在，城市里总能看到这样一些人，穿着整齐的衣服，开着一个装满货物的车子，起早贪黑地把货物送给接收货物的顾客，他们就是我们熟悉的“快递小哥”。", "Activity 6A-1: Now in cities we can always see such people, wearing neat clothes and driving a vehicle full of goods, delivering goods to the customers who receive them from dawn to night; they are the “courier guys” we are familiar with. (my key: 前解释, since it begins with facts and leads to the concept 快递小哥)"),
       ("近几年，有一个很流行的词“海待”，也叫“海带”。“海待”或是“海带”指的是那些从国外留学回来，找不到合适工作的人。", "6A-2: In recent years there is a very popular word “海待”, also called “海带”. “海待” or “海带” refers to those who have come back from studying abroad and cannot find a suitable job. (my key: 后解释, since it introduces the term first and then explains it; the book’s quotation marks are misplaced and I have fixed them. 海待 and 海带 are both read hǎidài; 海带 also means kelp, a pun on 海归 “sea turtle”)")]
QJB = [("现在，越来越多的游客不住旅馆，而是住在普通人家里。房子干净，价钱便宜，还有家的感觉，这样的住处叫做“民宿”。", "Activity 6B-1 (my 前解释 for “民宿”): Now more and more tourists do not stay in hotels but in ordinary families’ homes. The houses are clean and cheap and feel like home; such places to stay are called “homestays”."),
       ("“民宿”是指那些普通人家提供给游客住的房子。", "6B-1 (my 后解释): “Homestay” refers to those houses that ordinary families provide for tourists to stay in."),
       ("有的人晚上喝了酒，不能开车，就在手机上找一个司机，帮他把车开回家，这样的司机叫做“代驾”。", "6B-2 (my 前解释 for “代驾”): Some people have drunk alcohol at night and cannot drive, so they find a driver on the phone to drive their car home for them; such a driver is called a “designated driver”."),
       ("“代驾”是指那些帮喝了酒的人把车开回家的司机。", "6B-2 (my 后解释): “Designated driver” refers to those drivers who help people who have been drinking drive their cars home.")]
L6 = lesson(
    "Lesson 27 Presentation 2 grammar: 前解释 and 后解释",
    "前解释 · 后解释 · 网红 · 快递小哥 · 海归 · 海待 · 民宿 · 代驾",
    requires=[],
    cards=[
        card("前解释和后解释",
             "前解释 refers to “pre-explanation”, meaning that a paragraph begins with a statement of fact that naturally leads to a concept. 后解释 refers to a “post-explanation”, meaning that a paragraph introduces a concept first and then explains it.",
             tables=[QJ0], examples=[D(z, e) for z, e in QJE]),
        card("Activity 6 (Reading, Writing and Speaking)",
             "A. Pair up, identify 前解释 and 后解释 in the following passages, and explain the difference between them. B. With your partner, write a short paragraph on the following topics using the methods 前解释 and 后解释: 1. 什么是“民宿” 2. 什么是“代驾”. C. Share your work with the class. The two passages with my key, then my sample paragraphs:",
             examples=[D(z, e) for z, e in QJ6 + QJB]),
    ],
    exercises=[
        M("How does a 前解释 paragraph begin?", "With a statement of fact", ["With a concept", "With a question", "With a name"], "前解释: fact → concept."),
        M("How does a 后解释 paragraph begin?", "By introducing a concept", ["With a story", "With a number", "With a joke"], "后解释: concept → explanation."),
        M("Which kind of explanation is the passage about “快递小哥” in Activity 6A-1?", "前解释", ["后解释", "Neither", "Both"], "It starts with people we see."),
        M("Which kind is the passage about “海待” in Activity 6A-2?", "后解释", ["前解释", "Neither", "Both"], "It introduces the word first."),
        M("What does “海归” refer to?", "Students who studied or worked abroad and returned to China", ["Fishermen", "Divers", "Sea animals"], "有国外学习和工作经验的留学生回到中国的人."),
        M("What does “海待” refer to?", "People who came back from abroad and cannot find a suitable job", ["People who like the sea", "People who love tea", "People who sell fish"], "找不到合适工作的人."),
        M("Which is a 后解释 sentence?", "“民宿”是指那些普通人家提供给游客住的房子", ["现在，越来越多的游客住在普通人家里", "游客不住旅馆", "房子干净，价钱便宜"], "It defines the term."),
        F("“海待”指的是那些找不到合___工作的人。", "适", PART, "合适: suitable."),
        F("我们常常提到的“网红”，就是那些特别受欢迎，有很多粉___的主播。", "丝", PART, "粉丝: fans."),
    ],
)

UNIT = unit("第二十七课 Presentation 2: 网红, 把…叫做, 说到, 主要是因为, 前解释和后解释", [L1, L2, L3, L4, L5, L6])
