"""Unit 92: Lesson 28 (China's Youth), Presentation 3, second half: the skill-integration tasks (how Wen Chenghui started with postcards, an essay on a young teacher of reading,
an entrepreneurs' forum) and the using-Chinese tasks (situations, a young woman who sprays cotton fields with drones, and three young entrepreneurs to nominate).
Audio and pictures are not included; numbers the book writes as digits are spelled out in Chinese text; web addresses and source sites are left out;
answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l28_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('长大', 0, 'zhang3'), ('样得到', 1, 'de2'), ('机得飞', 1, 'dei3'), ('地得多少', 1, 'dei3'), ('有了无人机', 1, 'le5'), ('习了无人机', 1, 'le5'), ('始了无人机', 1, 'le5'), ('种棉花', 0, 'zhong4'), ('还给顾客', 0, 'hai2')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["前途", "目标", "材料"]

# ------------------------------------------------------------------ 1. skill integration 1
WQ = [("你是怎么想起来创业的？", "Activity 1A (my four questions for Wen Chenghui): How did you come up with starting a business?"), ("你最开始做的是什么生意？", "What business did you start with?"), ("你的第一桶金是怎么得到的？", "How did you earn your first bucket of gold (first big sum)?"), ("互联网对你的生意有什么帮助？", "How has the Internet helped your business?")]
WW = table(["词", "Meaning (mine)"], [["生意", "business, trade"], ["创意", "creative idea"], ["组织", "organize"], ["聪明", "smart, clever"], ["产品", "product"], ["第一桶金", "the first bucket of gold, the first big sum of money"], ["模式", "model, pattern"], ["合作", "cooperate"]], title="Activity 1B: the words to check in a dictionary first", say=[0])
WD = [("王辛", "温城辉是怎么开始创业的？", "Wang Xin: How did Wen Chenghui start his business? (Activity 1D script; translations mine)"),
      ("马林", "那是上大学的时候。一天，他忽然想，校园的风景这么美，要是把它画成明信片，再卖给学校的学生，生意大概会不错。", "Ma Lin: It was when he was at university. One day he suddenly thought, the campus scenery is so beautiful; if he painted it onto postcards and sold them to the school’s students, business would probably be good."),
      ("王辛", "结果怎么样？", "Wang Xin: How did it turn out?"),
      ("马林", "很成功，明信片卖了很多。然后，他又组织不同学校的学生，做不同的校园的风景明信片，生意越做越大。", "Ma Lin: Very successful; he sold many postcards. Then he organized students from different schools to make postcards of different campuses’ scenery, and the business grew bigger and bigger."),
      ("王辛", "对，要做就做大的。可是，做一个学校不难，同时做很多学校会不会很难呢？", "Wang Xin: Right, if you do it, do it big. But doing one school is not hard; wouldn’t doing many schools at the same time be very hard?"),
      ("马林", "一切通过互联网来做，就没那么难了。不同学校的人找风景，再请人画成画，最后在网上销售。", "Ma Lin: If everything is done through the Internet, it isn’t that hard. People at different schools find scenery, then have people paint it into pictures, and finally it is sold online."),
      ("王辛", "太聪明了！销售情况怎么样？", "Wang Xin: Very clever! How are the sales?"),
      ("马林", "很好。有了新产品，他只要发一条微博，转发给本校的学生，大家就都知道了。一个星期在一个学校就能卖一万张明信片。", "Ma Lin: Very good. When there is a new product, he only needs to post a microblog and have it forwarded to the students of his own school, and everyone knows. In one week at one school he can sell ten thousand postcards."),
      ("王辛", "同时在很多学校做，能卖多少明信片啊！", "Wang Xin: Doing it at many schools at the same time, how many postcards that can sell!"),
      ("马林", "对。他的第一桶金就是这样得到的。", "Ma Lin: Yes. His first bucket of gold was earned just this way."),
      ("王辛", "网上找人提供想法，网上再找人去画，最后网上销售。这个模式太棒了。", "Wang Xin: Finding people online to provide ideas, finding people online to paint, and finally selling online. This model is wonderful."),
      ("马林", "他自己说，没有网络，不会有人跟他合作，更不会做得像现在这么大。", "Ma Lin: He says himself that without the Internet nobody would cooperate with him, still less would it have become as big as it is now."),
      ("王辛", "可不。现在的年轻人又聪明，又懂高科技，一定大有前途。", "Wang Xin: Exactly. Today’s young people are both clever and understand high tech; they certainly have a great future.")]
WA = [("开始时他的模式是：网上找人提供想法，网上再找人去画，最后在网上销售。", "Activity 1B-1 (my answer): What was Wen Chenghui’s business model at the start? Finding people online to provide ideas, finding people online to paint, and finally selling online."), ("他的成功离不开互联网。", "1B-2 (my answer): What does his success depend on? It cannot be separated from the Internet.")]
WT = table(["关于", "细节 (my sample, from the script)"], [["开始的创意", "上大学的时候，他想把美丽的校园风景画成明信片，卖给学校的学生"], ["创作生产模式", "不同学校的人找风景，再请人画成画，一切通过互联网来做，同时做很多学校"], ["销售", "最后在网上销售；有了新产品，发一条微博，转发给本校的学生；一个星期在一个学校就能卖一万张明信片"], ["互联网的重要", "没有网络，不会有人跟他合作，更不会做得像现在这么大"]], title="Activity 1C: the details table (the book leaves the cells empty)")
WE = table(["Field", "Sample (mine)"], [["TO", "我的中国朋友"], ["CC", "(none)"], ["Subject", "温城辉是怎么开始创业的"]], title="Activity 1E: the e-mail header (the book leaves TO, CC and Subject blank)")
WEM = [("你好！我最近听说了温城辉创业的故事，想告诉你。他上大学的时候，想把校园的风景画成明信片，卖给学校的学生，结果很成功。后来他组织不同学校的学生，做不同校园的风景明信片，一切通过互联网来做：网上找人提供想法，网上再找人去画，最后在网上销售。一个星期在一个学校就能卖一万张明信片，他的第一桶金就是这样得到的。他自己说，没有网络，不会有人跟他合作，更不会做得像现在这么大。", "Activity 1E (my sample e-mail): Hello! I recently heard the story of how Wen Chenghui started his business and wanted to tell you. When he was at university he wanted to paint the campus scenery onto postcards and sell them to the students, and it was very successful. Later he organized students from different schools to make postcards of different campuses’ scenery, doing everything through the Internet: finding people online to provide ideas, finding people online to paint, and finally selling online. In one week at one school he could sell ten thousand postcards, and that is how he earned his first bucket of gold. He says himself that without the Internet nobody would have cooperated with him, still less would it have become as big as it is now.")]
L1 = lesson(
    "Lesson 28 Presentation 3 skill integration: how Wen Chenghui started his business with postcards",
    "温城辉的创业 · 校园风景明信片 · 第一桶金 · 模式 · 合作 · 离不开互联网 · 大有前途",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Speaking, Listening, Writing, and Reading)",
             "A. If you had an opportunity to ask Wen Chenghui (温城辉) questions about his early days in entrepreneurship, what questions would you ask? Write four questions and share them with a classmate. B. Listen to the dialog about Wen Chenghui’s experiences when he began his business and answer the questions. Check your dictionary for the meanings of 生意, 创意, 组织, 聪明, 产品, 第一桶金, 模式 and 合作 first. 1. 开始时温城辉创业的模式是什么？ 2. 他的成功离不开什么？ C. Listen to the dialog again. Then pair up and discuss the following topics. Provide as many details as possible in the table. D. Go over the script and refine your notes. E. Write an email to a Chinese friend and tell them about Wen Chenghui’s early business experiences. My questions, the words, the script, my answers, table and e-mail:",
             tables=[WW, WT, WE], examples=[D(z, e) for z, e in WQ] + dlg(WD) + [D(z, e) for z, e in WA + WEM]),
    ],
    exercises=[
        M("What did Wen Chenghui first decide to turn campus scenery into?", "Postcards", ["Calendars", "Movies", "Books"], "把它画成明信片."),
        M("Who did he sell the first postcards to?", "Students at his school", ["Tourists", "Teachers abroad", "Shops only"], "再卖给学校的学生."),
        M("How did he make many schools’ postcards without it being very hard?", "Everything was done through the Internet", ["He drew all himself", "He hired a factory", "He moved to each school"], "一切通过互联网来做，就没那么难了."),
        M("How did he tell students about new products?", "He posted a microblog for forwarding", ["He printed flyers", "He called each student", "He used the radio"], "他只要发一条微博，转发给本校的学生."),
        M("How many postcards could he sell in a week at one school?", "Ten thousand", ["One hundred", "One thousand", "A million"], "一个星期在一个学校就能卖一万张明信片."),
        M("What is the “first bucket of gold”?", "His first big sum of money", ["His first school", "His first postcard", "His first friend"], "他的第一桶金就是这样得到的."),
        M("What does his success depend on?", "The Internet", ["Luck only", "A big loan", "A famous teacher"], "没有网络，不会有人跟他合作."),
        M("What do Wang Xin and Ma Lin think of today’s young people?", "They are clever and have a great future", ["They are lazy", "They know nothing", "They have no ideas"], "一定大有前途."),
        F("没有网络，不会有人跟他合___。", "作", ["看", "想", "说"], "合作: cooperate."),
        F("他的第一桶___就是这样得到的。", "金", ["书", "钱", "水"], "第一桶金."),
        F("这个模___太棒了。", "式", ["子", "型", "样"], "模式: model."),
    ],
)

# ------------------------------------------------------------------ 2. skill integration 2-3
UG = table(["Expression", "Meaning (mine)"], [["瞧不起", "look down on"], ["解读", "interpret, explain"], ["非要…不可", "must; insist on"], ["公众号", "official (WeChat) account"]], title="Activity 2A: the underlined expressions (the underlining is lost in the text; these are the ones I take to be meant)")
US = [("这些年轻人很聪明，不要瞧不起他们。", "Activity 2A, 1: These young people are very smart; don’t look down on them. (translations mine)"), ("这篇文章我们看不太懂，请您解读一下好吗？", "2: We can’t quite understand this article; could you interpret it for us?"),
      ("我们一起吃完饭以后，他非要付钱不可。", "3: After we ate together, he insisted on paying."), ("她每个星期在自己的公众号上发表一篇文章。", "4: Every week she publishes an article on her own official account.")]
ES = ("我小时候最不喜欢大人瞧不起我，但等我过了三十岁，也开始觉得二十来岁的人做什么事都不行了。一天，我们单位的小王转给我一个公众号，说是她大学同学小周办的，每星期发一篇关于读书的文章。我想，我都读了三十多年的书了，还需要看年轻人关于读书的文章吗？所以根本就没看。过了几个月，小王又说那个人要在网上上课，教“怎么解读一本书，成为讲书人”，并请她带一个朋友参加。小王非要我跟她一起参加不可，我就只好参加了。没想到，小周的课马上就把我吸引住了，越听越喜欢。后来我试了一下他讲的方法，真的很有效果！过了不久，我自己也开始在网上讲自己看的书，并且越来越受欢迎。后来，我每个月在网上讲课的收入超过了工资。把爱好变成赚钱的方法，这是年轻人教我的！年轻人不是很有经验，但是他们很喜欢创新，所以他们做的很多事情，代表了将来发展的方向。",
      "When I was little I most disliked adults looking down on me, but after I passed thirty I too began to feel that people in their twenties could do nothing right. One day Xiao Wang at our workplace forwarded me an official account, saying it was run by her university classmate Xiao Zhou, who posted one article a week about reading. I thought, I have read books for more than thirty years; do I still need to read young people’s articles about reading? So I didn’t read it at all. After a few months, Xiao Wang said that person was going to teach online, teaching “how to interpret a book and become a book talker,” and asked her to bring a friend. Xiao Wang insisted I join her, so I had no choice but to attend. Unexpectedly, Xiao Zhou’s class captivated me at once, and the more I listened the more I liked it. Later I tried the method he taught, and it really worked! Not long after, I began to talk online about books I had read, and became more and more popular. Later, my monthly income from teaching online exceeded my salary. Turning a hobby into a way to make money, this is what a young person taught me! Young people are not very experienced, but they love to innovate, so many things they do represent the direction of future development. (Activity 2B, an essay; the book writes 20 and 30 in digits; translation mine)")
ET = [("作者自己是个年轻人，她觉得岁数大的人不应该瞧不起年轻人。", "Activity 2B-1 (true or false; my key: False, the author is over thirty): The author is a young person herself and feels that older people should not look down on young people."),
      ("小周在网上教怎么给别人讲一本自己看过的书。", "2B-2 (my key: True): Xiao Zhou teaches online how to tell others about a book you have read."),
      ("作者听说小周要开课，非常高兴，马上就报名参加了。", "2B-3 (my key: False, Xiao Wang insisted and she attended reluctantly): The author was very happy to hear Xiao Zhou would give a class and signed up right away."),
      ("作者从小周讲的课里学到了很多东西。", "2B-4 (my key: True): The author learned a lot from Xiao Zhou’s class."),
      ("作者觉得年轻人又聪明赚钱又多，所以应该向他们学习。", "2B-5 (my key: False, the article does not say this; the book prints 先他们学习, apparently 向): The author feels young people are both smart and earn a lot, so we should learn from them.")]
ET2 = [("我小时候最不喜欢大人瞧不起我，但等我过了三十岁，也开始觉得二十来岁的人做什么事都不行了。", "Activity 2C, 1 (my translation): When I was little I most disliked adults looking down on me, but after I passed thirty I too began to feel that people in their twenties could do nothing right."),
       ("我想，我都读了三十多年的书了，还需要看年轻人关于读书的文章吗？所以根本就没看。", "2: I thought, I have read books for more than thirty years; do I still need to read young people’s articles about reading? So I didn’t read it at all."),
       ("没想到，小周的课马上就把我吸引住了，越听越喜欢。后来我试了一下他讲的方法，真的很有效果！", "3: Unexpectedly, Xiao Zhou’s class captivated me at once, and the more I listened the more I liked it. Later I tried the method he taught, and it really worked!"),
       ("把爱好变成赚钱的方法，这是年轻人教我的！年轻人不是很有经验，但是他们很喜欢创新，所以他们做的很多事情，代表了将来发展的方向。", "4: Turning a hobby into a way to make money, this is what a young person taught me! Young people are not very experienced, but they love to innovate, so many things they do represent the direction of future development.")]
AD = [("朋友", "你小时候喜欢大人瞧不起你吗？", "Activity 2D (my sample dialog between the author and a friend, from the passage; translations mine). Friend: When you were little, did you like adults looking down on you?"),
      ("作者", "当然不喜欢，可是过了三十岁，我也开始觉得二十来岁的人做什么事都不行了。", "Author: Of course not, but after I passed thirty I too began to feel that people in their twenties could do nothing right."),
      ("朋友", "那你后来为什么参加了小周的课？", "Friend: Then why did you later attend Xiao Zhou’s class?"),
      ("作者", "小王转给我一个公众号，是她大学同学小周办的，我根本就没看。过了几个月，小周要在网上上课，小王非要我跟她一起参加不可，我就只好参加了。", "Author: Xiao Wang forwarded me an official account run by her university classmate Xiao Zhou and I didn’t read it at all. A few months later Xiao Zhou was going to teach online, Xiao Wang insisted I join her, so I had to attend."),
      ("朋友", "那课怎么样？", "Friend: And how was the class?"),
      ("作者", "没想到，小周的课马上就把我吸引住了。我试了一下他讲的方法，真的很有效果！", "Author: Unexpectedly, it captivated me at once. I tried his method and it really worked!"),
      ("朋友", "后来呢？", "Friend: And then?"),
      ("作者", "我自己也开始在网上讲书，越来越受欢迎，每个月在网上讲课的收入超过了工资。", "Author: I began to talk about books online myself, became more and more popular, and my monthly income from teaching online exceeded my salary."),
      ("朋友", "你现在怎么看年轻人？", "Friend: How do you see young people now?"),
      ("作者", "年轻人不是很有经验，但是他们很喜欢创新，他们做的很多事情，代表了将来发展的方向。", "Author: Young people are not very experienced, but they love to innovate, and many things they do represent the direction of future development.")]
FA1 = ("昨天在上海参加了一个企业家论坛，其中有一场的内容是向九零后学习互联网。一大帮七零后、六零后的企业家，坐在那里听着台上五个九零后年轻的创业者，讲解他们创业的心得。", "Yesterday I attended an entrepreneurs’ forum in Shanghai, one session of which was about learning the Internet from the post-’90s. A large group of post-’70s and post-’60s entrepreneurs sat there listening to five young post-’90s founders on the stage explain what they had learned from starting their businesses. (Activity 3, an authentic blog post; the book writes 90 后, 70 后, 60 后 in digits and names its source, a blog site; translations mine)")
FA2 = ("回答问题的时候，他们都回答问题得很简单，也很直接，没有那些客套。一位七零后企业家说：“你们不用考虑各种关系，也很成功。我们这些年天天应酬，酒都白喝了。”", "When answering questions they all answered very simply and directly, without the pleasantries. A post-’70s entrepreneur said, “You don’t have to consider all kinds of connections, and you are successful all the same. We have been socializing every day these years, and all that drinking was in vain.” (the book prints 他们都回答问题得很简单, apparently 回答得很简单)")
FA3 = ("听着他们在讲话，我想，台下很多人今天很有钱，但是，他们不懂高科技，过几年他们很可能就不会这么富有。台上的年轻一代有知识，爱学习，虽然他们现在还不富有，但是明天将会是他们的。", "Listening to them speak, I thought, many people in the audience are very rich today, but they don’t understand high tech and in a few years they may well not be so wealthy. The young generation on the stage have knowledge and love learning; although they are not rich yet, tomorrow will be theirs.")
FA4 = ("我想起前不久听了一次课，主讲的老师说，他要向自己的子女学习，因为他们常常是对的。这位老师说得有道理。中国有五千年的历史，中国文化强调尊重老人。这并不错，可是，有些东西前辈应该向后辈学习。", "I remembered a lecture I heard not long ago, in which the teacher said he wants to learn from his own children because they are often right. This teacher has a point. China has a history of five thousand years, and Chinese culture stresses respect for the old. This is not wrong, but there are some things that the older generation should learn from the younger. (the book breaks two lines of this paragraph awkwardly; I join them)")
FS = [("昨天作者在上海参加了一个企业家论坛，七零后、六零后的企业家听五个九零后的创业者讲创业的心得。九零后回答问题简单直接，作者觉得台下的人有钱但不懂高科技，年轻一代有知识，爱学习，明天是他们的。作者还说，有些东西前辈应该向后辈学习。", "Activity 3B (my sample summary, in Chinese; the book asks for English): Yesterday the author attended an entrepreneurs’ forum in Shanghai where post-’70s and post-’60s entrepreneurs listened to five post-’90s founders talk about their experiences. The post-’90s answered simply and directly; the author feels the audience are rich but don’t understand high tech, while the young generation have knowledge and love learning and tomorrow is theirs. The author also says that in some things the older generation should learn from the younger.")]
FQ = [("这是什么论坛？在哪儿开的？", "Activity 3C (my eight questions, two per paragraph), paragraph 1: What forum was this? Where was it held?"), ("台上是什么人？台下是什么人？", "Who were on the stage? Who were in the audience?"),
      ("九零后回答问题的时候怎么样？", "Paragraph 2: How did the post-’90s answer questions?"), ("那位七零后企业家说了什么？", "What did the post-’70s entrepreneur say?"),
      ("作者觉得台下的人有什么问题？", "Paragraph 3: What problem does the author see in the people in the audience?"), ("为什么说明天是年轻一代的？", "Why does the author say tomorrow belongs to the young generation?"),
      ("那位老师为什么要向自己的子女学习？", "Paragraph 4: Why did the teacher want to learn from his own children?"), ("中国文化强调什么？作者怎么看？", "What does Chinese culture stress, and how does the author see it?")]
L2 = lesson(
    "Lesson 28 Presentation 3 skill integration: a young teacher of reading, and an entrepreneurs’ forum",
    "瞧不起 · 解读 · 公众号 · 非要…不可 · 小周的课 · 向九零后学习互联网 · 企业家论坛",
    requires=[],
    cards=[
        card("Skill Integration, Activity 2 (Reading, Speaking, and Writing)",
             "A. Pair up. Guess the meaning of each underlined expression in each of the sentences. Then consult a dictionary to check your guesses. B. Read the essay. Then mark the statements as either True or False. C. Pair up and discuss your answers. Then work together to translate the sentences into English. D. Pair up. Create a dialog between the author and a friend using the information in the passage. Act out the dialog for the class. The expressions, the sentences, the essay, my key, translations and sample dialog:",
             tables=[UG], examples=[D(z, e) for z, e in US] + [D(*ES)] + [D(z, e) for z, e in ET + ET2] + dlg(AD)),
        card("Skill Integration, Activity 3 (Reading, Writing, and Speaking)",
             "A. Read the authentic material below. Underline any unknown words, and then highlight those words that are critical to your understanding of the passage. Guess what they mean and share your guesses with a classmate. Then consult a dictionary to confirm your guesses. B. Summarize the passage in English. C. Share your summary with your partner. Then, in Chinese, ask each other questions about the passage. (Each partner asks eight questions, two per paragraph.) The passage, a sample summary and my eight questions:",
             examples=[D(*FA1), D(*FA2), D(*FA3), D(*FA4)] + [D(z, e) for z, e in FS + FQ]),
    ],
    exercises=[
        M("What did the author dislike as a child?", "Adults looking down on her", ["Reading", "School", "Cooking"], "最不喜欢大人瞧不起我."),
        M("What did Xiao Zhou’s official account publish?", "An article about reading each week", ["Cooking videos", "News about sports", "Music"], "每星期发一篇关于读书的文章."),
        M("What did Xiao Zhou’s online class teach?", "How to interpret a book and become a book talker", ["How to cook", "How to drive", "How to sing"], "怎么解读一本书，成为讲书人."),
        M("Why did the author attend the class?", "Xiao Wang insisted she join", ["She was bored", "She was paid", "She was asked by Xiao Zhou"], "小王非要我跟她一起参加不可."),
        M("What happened to the author’s income later?", "Her online teaching income exceeded her salary", ["It disappeared", "It stayed the same", "It halved"], "收入超过了工资."),
        M("What do young people lack but make up for, according to the author?", "Experience, made up by love of innovation", ["Time, made up by money", "Friends", "Teachers"], "不是很有经验，但是他们很喜欢创新."),
        M("Where was the entrepreneurs’ forum held?", "Shanghai", ["Beijing", "Xi’an", "Hong Kong"], "昨天在上海参加了一个企业家论坛."),
        M("How many young founders were on the stage?", "Five", ["Two", "Ten", "Fifty"], "台上五个九零后年轻的创业者."),
        M("What did the teacher say about his own children?", "They are often right", ["They are lazy", "They are always wrong", "They are too young"], "因为他们常常是对的."),
        F("小王___要我跟她一起参加不可。", "非", ["不", "没", "别"], "非要…不可: insist on."),
        F("我想，我都读了三十多年的书了，还需要看年轻人关于读书的文章___？", "吗", ["们", "了", "的"], "…吗: question."),
        F("中国文化强调尊重老___。", "人", ["吗", "了", "的"], "尊重老人: respect for the old."),
    ],
)

# ------------------------------------------------------------------ 3. using Chinese 1-2
UC1 = [("有。比如温城辉，他创办了“礼物说”网站，一年销售的礼品有几十亿元。", "Using Chinese in Context, Activity 1, 1 (my answer, two sentences): Yes. For example Wen Chenghui founded the “Liwushuo” website, and the gifts it sells in a year amount to several billion yuan."),
       ("“礼物说”是一个专卖礼品的购物网站。顾客在那儿不但可以买到礼物，而且可以从视频上看到使用礼物的效果。它还给顾客一些好的建议，让顾客买到满意的礼物。", "2 (my answer, three sentences): “Liwushuo” is a shopping website that sells only gifts. Customers there can not only buy gifts but also see in videos the effect of using them. It also gives customers good suggestions so they can buy a satisfying gift."),
       ("“礼物说”有自己的特色，会给顾客好的建议。他们用高科技管理公司，使销售快速增长，买过东西的人还可以向别人介绍礼物，吸引了更多的新顾客。", "3 (my answer, three sentences): “Liwushuo” has its own character and gives customers good suggestions. They use high tech to manage the company, making sales grow fast, and people who have bought things can introduce gifts to others, attracting more new customers."),
       ("我会开一个网上的咖啡店。我会先研究顾客喜欢什么，再找人帮我做，最后在网上销售。", "4 (a sample answer of mine, three sentences; this is a personal question): I would open an online coffee shop. I would first study what customers like, then find people to help me make it, and finally sell online.")]
RB = ("几年前，戎梦雅从英国学习结束回到新疆，帮助父母种棉花。每到洒药的时候，就要花钱找人帮忙，很麻烦，速度也很慢。后来戎梦雅学习无人机技术，并和哥哥买了一架无人机，开始了无人机洒药。二零一六年七月成立了自己的公司，每年给新疆几十万亩棉田洒药，月收入十万多元。", "A few years ago, Róng Mèngyǎ returned to Xinjiang from studying in Britain to help her parents grow cotton. Whenever it was time to spray pesticide, they had to pay people to help, which was troublesome and slow. Later Rong Mengya studied drone technology, bought a drone with her older brother and began spraying with a drone. In July 2016 she founded her own company, which sprays several hundred thousand mu of cotton fields in Xinjiang every year, with a monthly income of over a hundred thousand yuan. (Using Chinese, Activity 2A, a brief bio; the book writes 2016 in digits and glosses the name with pinyin; translations mine)")
RW = table(["词", "Meaning (mine; the underlining in the book is lost, so these are the words I take to be meant)"], [["洒药", "spray pesticide"], ["无人机", "drone"], ["成立", "found, establish"], ["亩", "mu (about one-sixth of an acre)"], ["棉田", "cotton field"]], title="Activity 2A: words to look up", say=[0])
RQ = [("你为什么从英国回到新疆？", "Activity 2B (my sample questions for Rong Mengya): Why did you come back to Xinjiang from Britain?"), ("你是怎么想起来用无人机洒药的？", "How did you come up with using a drone to spray pesticide?"), ("用无人机洒药，效果怎么样？", "How well does spraying with a drone work?"), ("你们的公司是什么时候成立的？", "When was your company founded?"), ("现在你们的收入怎么样？", "How is your income now?")]
RS = [("各位听众，现在我给大家讲一个九零后开公司，用无人机给棉田洒农药的故事。", "Script (translations mine). Dear listeners, now I will tell you a story of a post-’90s person who started a company and uses drones to spray pesticide on cotton fields."),
      ("大家都知道，新疆每年生产很多棉花，它的棉花产量呢，是全国产量的百分之八十还多。和许多新疆孩子一样，九零后的戎梦雅是棉田陪着长大的。她父母三十年来到了新疆，现在种着四千多亩棉田。但是，给棉田撒农药特别辛苦。一般情况下，每年要给棉田要洒六次农药。用老方法洒药，一天只能洒两百亩地，洒完四千亩地得多少天啊！", "As everyone knows, Xinjiang produces a lot of cotton every year, and its cotton output is more than eighty percent of the national output. Like many Xinjiang children, post-’90s Rong Mengya grew up accompanied by cotton fields. Her parents came to Xinjiang thirty years ago (the book prints 三十年来到了新疆) and now grow more than four thousand mu of cotton. But spraying pesticide on cotton fields is especially hard work. Generally the fields must be sprayed six times a year (the book prints 要给棉田要洒; I keep it as printed). With the old method one can spray only two hundred mu a day, so how many days it takes to spray four thousand mu! (the book writes 4000 and 200 in digits)"),
      ("在英国学习的时候，戎梦雅玩儿过无人机。后来，她看到一台能撒农药的无人机，很感兴趣，就去深圳学习了无人机技术，回家后和哥哥一起买了一台。有了无人机，怎么洒药的效果最好呢？他们试了很多次，最后找到了效果最好的方法，比如放多少水，多少药，无人机得飞多高多快，等等。接着，他们用无人机把自己家的棉田洒了一遍，和以前的老方法比，速度快了很多倍。", "When she studied in Britain, Rong Mengya had played with drones. Later she saw a drone that could spray pesticide and was very interested, so she went to Shenzhen to study drone technology and, back home, bought one with her older brother. Once they had a drone, how could it spray with the best effect? They tried many times and finally found the method with the best effect, for example how much water and how much medicine to put in, how high and fast the drone must fly, and so on. Then they used the drone to spray their own family’s cotton fields once, and compared with the old method the speed was many times faster."),
      ("看到他们用无人机洒农药，当地很多种棉花的人也开始感兴趣了。戎梦雅就和哥哥成立了公司，又买了几台无人机，帮助别人给棉田洒药。二零一六年年底，戎梦雅和哥哥在哈密地区，给七万多亩棉田洒药，一次就赚了差不多三十万元。现在，平均每个月他们的收入都超过十万元。", "Seeing them use drones to spray pesticide, many local cotton growers also became interested. Rong Mengya then founded a company with her brother and bought several more drones to help others spray their cotton fields. At the end of 2016, Rong Mengya and her brother sprayed more than seventy thousand mu of cotton fields in the Hami region, earning nearly three hundred thousand yuan in one go. Now their income averages over a hundred thousand yuan every month."),
      ("好，故事讲完了。这个故事告诉了我们什么呢？我觉得，它告诉我们，现在的年轻人非常聪明，了解的信息又多，又愿意学习最新的技术，所以他们这一代大有前途，值得我们学习。您说呢？", "Well, the story is finished. What does it tell us? I think it tells us that young people today are very smart, know a lot of information and are willing to learn the latest technology, so this generation has a great future and is worth learning from. What do you think?")]
RT = table(["关于", "信息 (my sample, from the script)"], [["戎梦雅的经历和她的家庭", "九零后，在新疆的棉田陪着长大；父母种着四千多亩棉田；她在英国学习，玩儿过无人机"], ["买无人机给棉田洒药", "看到能撒农药的无人机很感兴趣，去深圳学习了无人机技术，和哥哥一起买了一台；试了很多次，找到效果最好的方法；速度比老方法快了很多倍"], ["成立公司给别人的棉田洒药", "当地很多种棉花的人也感兴趣，她和哥哥成立了公司，又买了几台无人机；二零一六年年底在哈密给七万多亩棉田洒药，一次赚了差不多三十万元；现在平均每个月的收入超过十万元"]], title="Activity 2C: the table (the book leaves the cells empty)")
L3 = lesson(
    "Lesson 28 Presentation 3 using Chinese in context: situations, and Rong Mengya who sprays cotton fields with drones",
    "九零后创业者 · 礼物说有什么特点 · 戎梦雅 · 无人机 · 洒农药 · 棉田 · 新疆 · 哈密",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Reading, Writing, and Speaking)",
             "Pair up and take turns telling your partner what you would say in each of the situations. Provide as many details as possible. Upon completion, switch roles and repeat the activity. 1. 有人问你，中国的九零后有没有成功的创业者。 (two or more sentences) 2. 听说中国很多年轻人喜欢去“礼物说”网站买礼物。那是一个什么样的网站？ (three or more sentences) 3. 温城辉领导下的“礼物说”有什么特点？ (three or more sentences) 4. 如果你也想创业的话，你会做什么？怎么做？ (three or more sentences) My answers:",
             examples=[D(z, e) for z, e in UC1]),
        card("Using Chinese in Context, Activity 2 (Reading, Writing, Listening, and Speaking)",
             "As a UNESCO representative in China working on a study about China’s young people, you find yourself in Xinjiang waiting to interview a young woman named 戎梦雅. A. Read a brief bio about this person; consult a dictionary for the underlined words. B. Pair up and discuss the questions you will ask 戎梦雅. C. Listen to Róng talk about her experiences and fill in the table. Share your work with your partner, then go over the script to refine your work. D. Conduct the interview. Your partner will play the role of 戎梦雅. The bio, the words, the script, my table and my questions:",
             tables=[RW, RT], examples=[D(*RB)] + [D(z, e) for z, e in RQ + RS]),
    ],
    exercises=[
        M("Where did Rong Mengya return after studying abroad?", "Xinjiang", ["Shanghai", "Beijing", "Hami"], "从英国学习结束回到新疆."),
        M("What did she help her parents grow?", "Cotton", ["Rice", "Tea", "Wheat"], "帮助父母种棉花."),
        M("What did she buy with her brother?", "A drone", ["A tractor", "A truck", "A boat"], "买了一架无人机."),
        M("What share of the national cotton output does Xinjiang produce?", "More than eighty percent", ["About ten percent", "Exactly half", "About one percent"], "全国产量的百分之八十还多."),
        M("How many times a year must the fields generally be sprayed?", "Six", ["One", "Twenty", "A hundred"], "每年要给棉田要洒六次农药."),
        M("How much could be sprayed in a day with the old method?", "About two hundred mu", ["About two mu", "About twenty thousand mu", "About two million mu"], "一天只能洒两百亩地."),
        M("Where did Rong Mengya learn drone technology?", "Shenzhen", ["Britain", "Hami", "Xi’an"], "就去深圳学习了无人机技术."),
        M("How much did they earn in one go in Hami at the end of 2016?", "Nearly three hundred thousand yuan", ["Three yuan", "Three thousand yuan", "Three million yuan"], "一次就赚了差不多三十万元."),
        M("What does the story tell us about today’s young people?", "They are smart and worth learning from", ["They are lazy", "They are careless", "They have no future"], "值得我们学习."),
        F("她看到一台能撒农药的无人___。", "机", ["车", "船", "人"], "无人机: drone."),
        F("他们试了很多次，最后找到了效果最好的方___。", "法", ["字", "情", "吗"], "方法: method."),
    ],
)

# ------------------------------------------------------------------ 4. using Chinese 3 + vocabulary
G1 = ("郭浩是一九九零年出生的。刚上大学的时候，一天有人问他，大学毕业后你打算做什么？他想也没想就说，我要创业。为了做好创业的准备，上大学时，他利用各种机会练习演讲，提高自己交流的能力。他也努力学习各种知识，差不多每门课都考一百分，多次得到国家奖学金。后来在读研究生期间，他找了十八位同学，成立了一个移动互联网工作室，为一些大公司开发软件。后来大家都去大公司工作，离开了工作室，只有他一个人留下来，坚持创业。", "Guo Hao was born in 1990. When he had just entered university, one day someone asked him, what do you plan to do after graduating? Without thinking he said, I want to start a business. To prepare well for starting a business, at university he used every opportunity to practice speaking and improved his ability to communicate. He also studied hard in all kinds of subjects, scoring 100 in nearly every course, and received the national scholarship several times. Later, during his graduate studies, he found eighteen classmates and set up a mobile Internet studio that developed software for some big companies. Afterwards everyone went to work in big companies and left the studio; only he stayed on and persisted in his business. (Activity 3A, Passage 1: 创业明星郭浩; the book writes 1990, 100 and 18 in digits; translations mine)")
G2 = ("二零一六年，郭浩在西安创建了他自己的公司。同一年，他的公司推出了一个智慧互动服务平台。他们的平台很棒，对一些高科技公司来说十分有用，但开始的时候卖得并不好。他就想办法改变销售渠道，终于让更多人熟悉、了解了他的产品，现在这个平台已经卖到全国两百多个城市，为几万家公司提供服务。几年前，他被评为西安市“创业明星。”", "In 2016 Guo Hao founded his own company in Xi’an. In the same year his company launched a smart interactive service platform. Their platform was excellent and very useful to some high-tech companies, but at first it did not sell well. He thought of ways to change the sales channels and finally got more people familiar with and understanding his product; now this platform has sold in more than two hundred cities across the country and serves tens of thousands of companies. A few years ago he was named a “Star of Entrepreneurship” of Xi’an.")
Z1 = ("张林轩，今年二十岁，是聊网的创始人。他的网站为中国学生提供了一个新的学习英语的平台。现在网站还在测试，没有正式运营。从公司注册到现在半年的时间，他已经得到几百万元的投资，估计公司现在的价值已经超过一千万。", "Zhang Linxuan, twenty years old this year, is the founder of Liaowang (Talkways). His website provides Chinese students a new platform for learning English. The website is still being tested and has not formally begun operating. In the half year from the company’s registration until now he has already received several million yuan in investment, and the company’s value is estimated to have exceeded ten million. (Passage 2: 聊网创始人张林轩; the book gives the site’s web address, which I leave out; the book writes 20 in digits; translations mine)")
Z2 = ("在他的网上，美国有名大学的学生或毕业生当老师，一对一和中国学生用英语通过视频聊天，让中国学生学习地道的英语。每次课程结束以后，学生会对老师的教学情况打分，来保证老师上课的质量。由于美国的大学生不是专业老师，他们的收费并不高，一个小时一般二十美元左右。如果是在中国，找一个外国老师上同样的课，价格要高五到十倍。", "On his site, students or graduates of well-known American universities serve as teachers and chat with Chinese students one on one by video in English, letting Chinese students learn authentic English. After each class the student rates the teacher’s teaching, which ensures the quality of the teacher’s classes. Since American university students are not professional teachers, their charges are not high, generally about 20 U.S. dollars an hour. In China, finding a foreign teacher for the same class would cost five to ten times as much.")
X1 = ("“新新小吃”是一家开发小吃的公司。它的创始人都是九零后网络工程师，他们只懂电脑和网络，不懂小吃，但却可以做最好的小吃。", "“Xinxin Snacks” is a company that develops snacks. Its founders are all post-’90s network engineers who understand only computers and networks, not snacks, but can still make the best snacks. (Passage 3: 用互联网技术开发小吃的“新新小吃”公司; translations mine)")
X2 = ("为了开发一种小吃，他们先分析网上的各种信息，研究小吃的成分和味道，再设计制作的过程。新产品做好以后，他们会请喜欢小吃的朋友尝一尝，他们说好吃，就继续做下去。由于他们用的机器都是用电脑控制，所以很精确，做出来的每个产品的样子和味道都是一样的。", "To develop a snack, they first analyze all kinds of information online, study the snack’s ingredients and flavor, and then design the process of making it. After a new product is made, they invite friends who like snacks to taste it, and if they say it is delicious, they carry on. Since the machines they use are all computer-controlled, they are very precise, and every product made looks and tastes the same.")
X3 = ("那些很复杂特别有名的小吃他们也能做。对他们来说，只要花足够的时间，就能做出来，并且做得非常好。老百姓熟悉的一些小吃，几十年没有什么变化，而“新新小吃的”的产品，总是在改进，味道越做越好。", "They can also make those very complicated, especially famous snacks. For them, as long as they spend enough time they can make them, and make them very well. Some snacks ordinary people know have not changed in decades, while the products of “Xinxin Snacks” are always being improved and taste better and better. (the book prints “新新小吃的”的产品 with a stray 的; I print “新新小吃”的产品)")
PS = [("郭浩一九九零年出生，上大学时就想创业，努力学习，练习演讲。读研究生时他和同学成立了工作室，后来只有他留下来。二零一六年他在西安创建了公司，推出了智慧互动服务平台，改变销售渠道后，现在已经卖到全国两百多个城市。", "Activity 3A, Passage 1 (my summary in Chinese): Guo Hao was born in 1990 and wanted to start a business from his university days, studying hard and practicing speaking. In graduate school he and classmates set up a studio, and later only he stayed on. In 2016 he founded a company in Xi’an and launched a smart interactive service platform; after changing the sales channels it has sold in more than two hundred cities nationwide."),
      ("张林轩今年二十岁，他的聊网让中国学生和美国大学生一对一用英语视频聊天，学习地道的英语。网站还在测试，他已经得到几百万元的投资，学生打分保证质量，收费也不高。", "Passage 2 (my summary): Zhang Linxuan is twenty; on his Liaowang site Chinese students chat one on one by video in English with American university students to learn authentic English. The site is still being tested and he has already received several million yuan of investment; student ratings ensure quality and the fees are low."),
      ("“新新小吃”的创始人是九零后网络工程师，他们不懂小吃，但是用电脑分析网上的信息，用电脑控制机器，所以做得很精确，小吃总是在改进，味道越做越好。", "Passage 3 (my summary): The founders of “Xinxin Snacks” are post-’90s network engineers; they don’t know snacks, but analyze online information by computer and control machines by computer, so they work precisely and the snacks keep improving and taste better and better.")]
RK = table(["", "Activity 3B: rank the three nominees"], [["Passage 1", "Rank (for the group to decide; no key)"], ["Passage 2", "Rank (for the group to decide; no key)"], ["Passage 3", "Rank (for the group to decide; no key)"]], title="Activity 3B and C: choosing the nominee (the book asks the groups and the class to decide, so I give no answer)")
L4 = lesson(
    "Lesson 28 Presentation 3 using Chinese in context: nominating young entrepreneurs",
    "创业明星郭浩 · 聊网创始人张林轩 · 新新小吃 · 一对一 · 精确 · 提名 · 国际青年创业者奖",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 3 (Reading, Writing, and Speaking)",
             "You are part of an international panel that will nominate recipients for the Global Young Entrepreneurs Awards and you are in charge of the China section. A. Divide into groups of three. Members of each group read different passages below and provide a summary in Chinese. B. Share your work in your group. Compare the three cases and decide who to nominate. Rank the other two nominees. C. The whole class then discusses the nominations together. Each group explains how they came to their decision. The class picks a final nominee and decides the ranking of the other two. The three passages and my summaries:",
             tables=[RK], examples=[D(*G1), D(*G2), D(*Z1), D(*Z2), D(*X1), D(*X2), D(*X3)] + [D(z, e) for z, e in PS]),
    ],
    exercises=[
        M("When was Guo Hao born?", "1990", ["1999", "1980", "2000"], "郭浩是一九九零年出生的."),
        M("What did Guo Hao say when asked what he would do after graduating?", "I want to start a business", ["I want to rest", "I want to travel", "I don’t know"], "我要创业."),
        M("What kind of studio did Guo Hao set up in graduate school?", "A mobile Internet studio", ["A cooking studio", "A music studio", "A film studio"], "成立了一个移动互联网工作室."),
        M("In which city did Guo Hao found his company in 2016?", "Xi’an", ["Beijing", "Shanghai", "Shenzhen"], "郭浩在西安创建了他自己的公司."),
        M("How old is Zhang Linxuan?", "Twenty", ["Thirty", "Ten", "Fifty"], "张林轩，今年二十岁."),
        M("Who teach on Zhang Linxuan’s site?", "Students or graduates of well-known American universities", ["Chinese professors", "Robots", "Retired teachers"], "美国有名大学的学生或毕业生当老师."),
        M("About how much does an hour cost on his site?", "About twenty U.S. dollars", ["About two U.S. dollars", "About two hundred", "Free"], "一个小时一般二十美元左右."),
        M("What do the founders of “Xinxin Snacks” understand?", "Only computers and networks", ["Only snacks", "Only cooking", "Nothing"], "他们只懂电脑和网络，不懂小吃."),
        M("Why are their products all the same?", "Their machines are computer-controlled and very precise", ["They are made by hand", "They are cheap", "They are old recipes"], "用的机器都是用电脑控制，所以很精确."),
        F("他想也没想就说，我要创___。", "业", ["作", "办", "新"], "创业: start a business."),
        F("他们的收费并不高，一个小时一般二十美元___右。", "左", ["上", "下", "前"], "左右: about."),
        F("他们总是在改进，味道越做越___。", "好", ["多", "少", "大"], "越做越好."),
    ],
)

UNIT = unit("第二十八课 Presentation 3: 明信片的故事, 向九零后学习, 戎梦雅, 创业明星", [L1, L2, L3, L4])
