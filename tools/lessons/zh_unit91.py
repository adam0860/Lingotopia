"""Unit 91: Lesson 28 (China's Youth), Presentation 3, first half: Getting Started, Lao Li's livestream about the founder of a gift website, Activities 1-4 and the Grammar and Usage section
(inserting a question, 什么 to soften the tone, the ...不..., 但是...很... construction, 要+Verb+就+Verb...的, 同时).
Audio and pictures are not included; the traditional-character copy of the presentation is not repeated; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled."""
from zh_auto import *
from zh_l28_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('长大', 0, 'zhang3'), ('还给我看', 0, 'hai2'), ('团长', 1, 'zhang3'), ('，得经常', 1, 'dei3'), ('就得多说', 1, 'dei3')):
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
NOUN = ["前途", "目标", "材料"]

# ------------------------------------------------------------------ 1. presentation 3 + activity 1
LL = [("大家好！我是老李，谢谢各位观看我的直播节目“老李有话说”。", "Hello everyone! I’m Lao Li, and thank you all for watching my live program “Lao Li Has Something to Say.” (Presentation 3; translations mine; the traditional-character copy is not repeated)"),
      ("今天咱们聊聊九零后创业的事儿。大家有没有发现，九零后虽然才二三十岁，可是他们中的一些人已经是大公司的老板了。“礼物说”这个购物网站，听说过吧？它专卖礼品，是一位九零后创办的，叫温城辉，他的网站一年销售的礼品有几十亿元。", "Today let’s chat about post-’90s starting businesses. Have you noticed that although the post-’90s are only twenty or thirty years old, some of them are already bosses of big companies? The shopping website “Liwushuo,” you’ve heard of it, right? It sells only gifts and was founded by a post-’90s person called Wen Chenghui; the gifts his website sells in a year amount to several billion yuan. (the book writes 90 后 in digits)"),
      ("像很多九零后年轻人一样，温城辉有很多创新的想法。几年前，他看到网上礼品店虽然很多，但都没什么特色。温城辉觉得顾客买礼物不难，但是买到满意的礼物很难。所以，他就建了“礼物说”网站，给顾客一些好的建议，让顾客买到最好的礼物。另外，温城辉觉得，要做网站就做最好的。一般的平台只卖东西，可在他的平台上，顾客不但可以买到礼物，而且还可以从视频上看到使用礼物的效果。温城辉还有很多先进的管理方法，比如用高科技管理公司，使公司的销售快速增长。同时，买过东西的人，还可以在平台上向别人介绍礼物，吸引了更多的新顾客。", "Like many young post-’90s people, Wen Chenghui has many innovative ideas. A few years ago he saw that although there were many online gift shops, none had much character. Wen Chenghui felt that it is not hard for customers to buy gifts, but it is hard to buy a gift they are satisfied with. So he built the “Liwushuo” website to give customers some good suggestions so they could buy the best gift. Also, Wen Chenghui felt that if you build a website you should build the best. Ordinary platforms only sell things, but on his platform customers can not only buy gifts but also see in videos the effect of using the gifts. Wen Chenghui also has many advanced management methods, for example using high tech to manage the company, which makes the company’s sales grow fast. At the same time, people who have bought things can also introduce gifts to others on the platform, attracting more new customers."),
      ("好，今天就聊这么多。咱们下次节目再见！", "Well, that’s all for today. See you at the next program!")]
TF1 = [("温城辉和老李是朋友或同事。", "Activity 1A-1 (true or false; my key: False, the program only says Lao Li talks about him): Wen Chenghui and Lao Li are friends or colleagues."),
       ("“礼物说”是一个在互联网上卖礼物的公司。", "1A-2 (my key: True): “Liwushuo” is a company that sells gifts on the Internet."),
       ("温城辉做了一个教大家怎么买礼物的网站。", "1A-3 (my key: True, it gives customers good suggestions): Wen Chenghui made a website that teaches everyone how to buy gifts.")]
A1 = [("老李做的是直播节目“老李有话说”。", "Activity 1B-1 (my answer): Lao Li does the live program “Lao Li Has Something to Say.”"),
      ("“礼物说”是专卖礼品的购物网站，是九零后温城辉创办的，一年销售的礼品有几十亿元。", "1B-2 (my answer): “Liwushuo” is a shopping website that sells only gifts, founded by the post-’90s Wen Chenghui; it sells several billion yuan of gifts a year."),
      ("因为他看到网上礼品店虽然很多，但都没什么特色。顾客买礼物不难，买到满意的礼物很难，所以他建了这个网站，给顾客一些好的建议。", "1B-3 (my answer): Because he saw that online gift shops, though many, had no character. Buying a gift is not hard for customers, but buying a satisfying one is, so he built this website to give customers good suggestions."),
      ("在这个平台上，顾客不但可以买到礼物，而且可以从视频上看到使用礼物的效果，买过东西的人还可以向别人介绍礼物。", "1B-4 (my answer): On this platform customers can not only buy gifts but also see in videos the effect of using them, and people who have bought things can introduce gifts to others."),
      ("他有很多创新的想法，还有先进的管理方法，比如用高科技管理公司，使公司的销售快速增长。", "1B-5 (my answer): He has many innovative ideas and advanced management methods, for example using high tech to manage the company, making its sales grow fast.")]
L1 = lesson(
    "Lesson 28 Presentation 3: a livestream about the post-’90s who start businesses",
    "老李有话说 · 九零后创业 · 礼物说 · 温城辉 · 创新 · 先进的管理方法 · 快速增长",
    requires=[],
    cards=[
        card("Presentation 3: Getting Started",
             "Pair up. Discuss the following questions with your partner. A. Can you share a brief story about a young American entrepreneur? B. If you were to become an entrepreneur, what business would you choose? (Discussion questions; the book gives no answers.)"),
        card("Presentation 3: Lao Li’s livestream",
             "A host of a livestream program tells about Wen Chenghui, who founded a gift-shopping website.",
             examples=[D(z, e) for z, e in LL]),
        card("Presentation 3 Activities, Activity 1 (Listening and Speaking)",
             "A. Global Listening: Listen to Presentation 3 and mark the following statements as either True or False. 1. 温城辉和老李是朋友或同事。 2. “礼物说”是一个在互联网上卖礼物的公司。 3. 温城辉做了一个教大家怎么买礼物的网站。 B. Detail Listening: Listen to Presentation 3 again and answer the questions. 1. 老李做的是什么节目？ 2. “礼物说”是一个什么网站？ 3. 温城辉为什么要建“礼物说”这个网站？ 4. “礼物说”有什么特点？ 5. 温城辉创业有什么特点？ My key and answers:",
             examples=[D(z, e) for z, e in TF1 + A1]),
    ],
    exercises=[
        M("What is the name of Lao Li’s program?", "老李有话说 (Lao Li Has Something to Say)", ["Gift Talk", "Business News", "Morning Show"], "直播节目“老李有话说”."),
        M("What does the website “Liwushuo” sell?", "Gifts", ["Clothes", "Food", "Books"], "它专卖礼品."),
        M("Who founded “Liwushuo”?", "A post-’90s person named Wen Chenghui", ["Lao Li", "A post-’70s person", "A foreign company"], "是一位九零后创办的，叫温城辉."),
        M("About how much do the gifts sold on the site amount to in a year?", "Several billion yuan", ["Several thousand yuan", "Several hundred yuan", "Nothing"], "一年销售的礼品有几十亿元."),
        M("What did Wen Chenghui find hard for customers?", "Buying a satisfying gift", ["Finding a website", "Paying", "Waiting"], "买到满意的礼物很难."),
        M("What can customers see in videos on his platform?", "The effect of using the gifts", ["The factory", "Lao Li", "The weather"], "从视频上看到使用礼物的效果."),
        M("What management method is mentioned?", "Using high tech to manage the company", ["Working longer hours", "Cutting prices", "Selling the company"], "用高科技管理公司."),
        M("How do buyers help bring in new customers?", "They introduce gifts to others on the platform", ["They pay more", "They stop buying", "They sell the site"], "买过东西的人，还可以在平台上向别人介绍礼物."),
        F("今天咱们聊聊九零后创业的事___。", "儿", ["子", "们", "了"], "事儿: matter."),
        F("它专卖礼品，是一位九零后创___的。", "办", ["看", "想", "说"], "创办: found."),
        F("温城辉还有很多先进的管理方___。", "法", ["字", "情", "吗"], "方法: method."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2-4
T2 = table(["关于", "中文词语 (my sample, from the presentation)"], [["九零后", "年轻，才二三十岁，创业，大公司的老板，有创新的想法"], ["创业", "创办，建网站，成立公司，做老板，有创新的想法"], ["吸引顾客", "给顾客好的建议，让顾客买到满意的礼物，看到使用礼物的效果，向别人介绍礼物，有特色"], ["管理", "先进的管理方法，用高科技管理公司，使公司的销售快速增长"]], title="Activity 2A: the table (the book gives the four topics and leaves the cells empty)")
T2B = table(["", "Jumbled expressions for Activity 2B"], [["1", "大公司的 | 创业的很多 | 也有很成功的 | 老板了 | 九零后 | 有的已经是"], ["2", "要用就要用 | 没什么 | 一般的 | 特色 | 最好的 | 购物软件"], ["3", "他的新网站 | 很多顾客 | 快速 | 使销售额 | 增长 | 吸引了"], ["4", "人们感兴趣的 | 是一位八零后创办的 | “今日头条” | 它专门介绍 | 新闻和信息"], ["5", "而且 | 使用礼物的 | 那个网站 | 方法和效果 | 还介绍 | 不但卖礼物"]], title="Activity 2B: reorder the expressions to make logical and correct sentences (the book writes 80 后 and 90 后 in digits)")
SA2 = [("九零后创业的很多，也有很成功的，有的已经是大公司的老板了。", "Activity 2C suggested answer 1: Many post-’90s people start businesses, and some are very successful; some are already bosses of big companies. (translations mine)"), ("一般的购物软件没什么特色，要用就要用最好的。", "2: Ordinary shopping apps have no particular character; if you use one, use the best."),
       ("他的新网站吸引了很多顾客，使销售额快速增长。", "3: His new website attracted many customers and made sales grow quickly."), ("“今日头条”是一位八零后创办的，它专门介绍人们感兴趣的新闻和信息。", "4: “Toutiao” was founded by a post-’80s person and specializes in news and information people are interested in. (the book glosses nothing here)"),
       ("那个网站不但卖礼物，而且还介绍使用礼物的方法和效果。", "5: That website not only sells gifts but also introduces the methods and effects of using them.")]
B3 = table(["", "Beginnings for Activity 3A (listen and complete)"], [["1", "九零后虽然年龄不大，"], ["2", "温城辉这个人你听说过吧？"], ["3", "用他的想法来做网站，"], ["4", "我先生管理公司很辛苦。"], ["5", "他们不但给我介绍了礼物特点，"], ["6", "在网上买一般的衣服不难，"], ["7", "建一个网上的礼品店没什么难的，"], ["8", "现在很多九零后创办了自己公司。"]], title="Activity 3A: the sentence beginnings printed in the book (the rest is audio)")
SC3 = [("九零后虽然年龄不大，可是他们中有些人创业非常成功。", "Activity 3B script, 1 (translations mine): Although the post-’90s are not old, some of them have been very successful in starting businesses."),
       ("温城辉这个人你听说过吧？他是九零后，有一个网上买礼品的平台，特别受年轻人的欢迎。", "2: You’ve heard of Wen Chenghui, right? He is post-’90s and has an online platform for buying gifts that is especially popular with young people."),
       ("用他的想法来做网站，一定能吸引很多顾客，销售额会越来越高。", "3: If you build the website with his idea, it will certainly attract many customers and sales will get higher and higher."),
       ("我先生管理公司很辛苦。他的生日快到了，我会给他买件礼物，要买就买他最喜欢的。", "4: My husband works hard managing his company. His birthday is coming, and I will buy him a gift; if I buy, I’ll buy what he likes best."),
       ("他们不但给我介绍了礼物特点，而且还给我看了使用礼物的效果。", "5: They not only introduced the gift’s features to me but also showed me the effect of using it."),
       ("在网上买一般的衣服不难，但是买到我喜欢的衣服很难，所以我只好到商店去买。", "6: Buying ordinary clothes online is not hard, but buying clothes I like is, so I have no choice but to go buy at a store."),
       ("建一个网上的礼品店没什么难的，但是能吸引大量的年轻的顾客，使销售额快速增长，很难。", "7: Building an online gift shop is nothing hard, but attracting large numbers of young customers and making sales grow fast is hard."),
       ("现在很多九零后创办了自己公司。他们一般都有很多创新的想法，同时还用高科技来管理公司。", "8: Many post-’90s people now have founded their own companies. They generally have many innovative ideas and at the same time use high tech to manage the company.")]
EX4 = [("A", "今天老李的直播节目聊什么？", "Activity 4A-1 (expressions: 90 后, 创业; the answers are mine): A: What did Lao Li’s livestream talk about today?"), ("B", "今天老李聊九零后创业的事儿。", "B: Today Lao Li talked about post-’90s starting businesses."),
       ("A", "现在年轻人创办公司不难吧？", "4A-2 (不难, 创新, 很难): A: It isn’t hard for young people to found companies now, is it?"), ("B", "创办公司不难，但是要有创新的想法，成功很难。", "B: Founding a company is not hard, but having innovative ideas and succeeding is hard."),
       ("A", "他们的公司为什么那么成功？", "4A-3 (高科技, 要做就…): A: Why is their company so successful?"), ("B", "因为他们用高科技管理公司，而且要做就做最好的。", "B: Because they use high tech to manage the company, and if they do it they do the best."),
       ("A", "那他是怎么做到的呢？", "4A-4 (介绍, 吸引, 同时): A: Then how did he do it?"), ("B", "他在网站上介绍礼物，吸引了很多顾客，同时让买过东西的人向别人介绍礼物。", "B: He introduces gifts on the site and attracts many customers, and at the same time lets people who have bought things introduce gifts to others."),
       ("A", "你是怎么想起来要做购物网站的？", "4A-5 (像…一样, 想法): A: How did you come up with the idea of making a shopping website?"), ("B", "像很多九零后年轻人一样，我有很多创新的想法。", "B: Like many young post-’90s people, I have many innovative ideas."),
       ("A", "九零后才二三十岁，很年轻啊。", "4A-6 (虽然, 可是, 老板): A: The post-’90s are only twenty or thirty, very young."), ("B", "虽然他们才二三十岁，可是有的已经是大公司的老板了。", "B: Although they are only twenty or thirty, some are already bosses of big companies."),
       ("A", "刚开始他们的网站没能吸引很多顾客，那后来呢？", "4A-7 (建议, 快速, 增长): A: At first their website could not attract many customers; what happened later?"), ("B", "后来他们给顾客一些好的建议，销售就快速增长了。", "B: Later they gave customers some good suggestions and sales grew fast."),
       ("A", "现在购物网站太多了。他的有什么不一样吗？", "4A-8 (一般, 可, 同时): A: There are too many shopping websites now. What is different about his?"), ("B", "一般的网站只卖东西，可他的网站同时还能让顾客看到使用礼物的效果。", "B: Ordinary websites only sell things, but his also lets customers see the effect of using the gifts.")]
L2 = lesson(
    "Lesson 28 Presentation 3 activities: the table, reordering sentences, listening scripts and exchanges",
    "吸引顾客 · 管理 · 要用就要用最好的 · 使销售额快速增长 · 今日头条 · 建议 · 同时",
    requires=[],
    cards=[
        card("Activity 2 (Writing, Reading, and Speaking)",
             "A. Pair up and fill in the table with the expressions you’ve just learned. B. Reorder the expressions below to make logical and correct sentences. C. Pair up and share your sentences. Then go over the suggested answers below and refine your work if necessary. The table, the jumbled expressions and the book’s suggested answers:",
             tables=[T2, T2B], examples=[D(z, e) for z, e in SA2]),
        card("Activity 3 (Listening, Writing, Reading, and Speaking)",
             "A. Listen and complete the following statements with what you hear. B. Pair up and share your answers. Then check your work against the scripts below. Take turns translating the sentences into English. The beginnings and the scripts:",
             tables=[B3], examples=[D(z, e) for z, e in SC3]),
        card("Activity 4 (Reading, Writing, and Speaking)",
             "A. Complete the exchanges using the expressions provided (the book gives the questions, A, and the expressions in brackets, and leaves B blank). B. Pair up, share and refine your work. Then, take turns translating the exchanges into English and your partner translates them back into Chinese. My completed exchanges:",
             examples=dlg(EX4)),
    ],
    exercises=[
        M("In 要用就要用最好的, what is the idea?", "If you use one, use the best", ["Use the cheapest", "Don’t use any", "Use the oldest"], "要用就要用最好的."),
        M("What does 使销售额快速增长 mean?", "Make sales grow quickly", ["Make sales fall", "Make sales stop", "Make sales secret"], "使销售额快速增长."),
        M("What is “今日头条” according to the suggested answer?", "A service introducing news and information", ["A shoe shop", "A restaurant", "A school"], "它专门介绍人们感兴趣的新闻和信息."),
        M("Who is “今日头条” said to be founded by?", "A post-’80s person", ["A post-’60s person", "A teacher", "A foreign company"], "是一位八零后创办的."),
        M("How does the wife in the script decide on her husband’s gift?", "She will buy what he likes best", ["She will buy the cheapest", "She will skip it", "She will make it"], "要买就买他最喜欢的."),
        M("Why does the speaker in script 6 go to the store?", "She can’t find the clothes she likes online", ["Stores are cheaper", "She hates the Internet", "Online shops are closed"], "买到我喜欢的衣服很难，所以我只好到商店去买."),
        M("What do many post-’90s people use to manage their companies, at the same time?", "High tech", ["Old methods", "Nothing", "Newspapers"], "同时还用高科技来管理公司."),
        M("What does an ordinary platform do, according to exchange 8?", "Only sells things", ["Shows the effect of gifts", "Gives free gifts", "Hires many people"], "一般的网站只卖东西."),
        F("九零后虽然年龄不大，___是他们中有些人创业非常成功。", "可", ["但", "和", "跟"], "虽然…可是…."),
        F("他的新网站吸引了很多顾客，使销售额快速增___。", "长", ["大", "高", "多"], "增长: increase."),
        F("要用就要用最好___。", "的", PART, "最好的."),
    ],
)

# ------------------------------------------------------------------ 3. grammar: question insertion and 什么
Q5 = [("中文系新来了一位老师，是南京人，北京语言大学毕业的。", "Discourse Grammar: Inserting a Question to Draw Listener’s Attention. 1a (direct): A new teacher has arrived in the Chinese department; he is from Nanjing and graduated from Beijing Language and Culture University. (translations mine)"), ("听说了吗？中文系新来了一位老师，是南京人，北京语言大学毕业的。", "1b (with a question): Have you heard? A new teacher has arrived in the Chinese department; he is from Nanjing and graduated from Beijing Language and Culture University."),
      ("老张的小儿子要去美国加州上大学了。", "2a: Lao Zhang’s youngest son is going to university in California."), ("老张的小儿子你认识吧？他要去美国加州上大学了。", "2b: You know Lao Zhang’s youngest son, right? He is going to university in California."),
      ("锻炼太多对身体也不好。", "3a: Too much exercise is not good for the body either."), ("你知道吗？锻炼太多对身体也不好。", "3b: Did you know? Too much exercise is not good for the body either."),
      ("这几天马路上的车比以前少多了。", "4a: These days there are far fewer cars on the road than before."), ("你发现没有？这几天马路上的车比以前少多了。", "4b: Have you noticed? These days there are far fewer cars on the road than before."),
      ("今天新华商场的女装打七折。", "5a: Women’s clothing at Xinhua Mall is 30 percent off today."), ("听说了吗？今天新华商场的女装打七折呢。", "5b: Have you heard? Women’s clothing at Xinhua Mall is 30 percent off today.")]
M1 = [("你知道吗？九零后才二三十岁，可有的已经是大公司的老板了。", "Activity 1A-1 (my version beginning with a question; translations mine): Did you know? The post-’90s are only twenty or thirty, but some are already bosses of big companies."), ("你知道怎么才能学好中文吗？要学好中文就得多说。", "1A-2: Do you know how to learn Chinese well? To learn Chinese well you have to speak a lot."),
      ("你看过那部新电影吗？那部新电影很好看。", "1A-3: Have you seen that new movie? That new movie is very good."), ("你发现没有？咱们这儿现在能看到蓝天了！", "1A-4: Have you noticed? We can see blue sky here now!"),
      ("你知道吗？后来她越想越觉得女儿说得有道理。", "1A-5: Do you know what? Later, the more she thought, the more she felt her daughter was right.")]
M1B = [("你去过蒙特雷的海边吗？那儿的风景特别美。", "Activity 1B (my five sample sentences about Monterey or DLI, each starting with a question): Have you been to the Monterey seaside? The scenery there is especially beautiful."), ("你知道吗？蒙特雷的夏天不太热。", "Did you know? Summers in Monterey are not too hot."),
       ("听说了吗？学校下个星期有一次中文考试。", "Have you heard? The school has a Chinese exam next week."), ("你发现没有？这几天学校里的人比以前少多了。", "Have you noticed? These days there are far fewer people at school than before."), ("你认识我们的中文老师吧？她是北京人。", "You know our Chinese teacher, right? She is from Beijing.")]
SH = [("这儿没有草和树。", "什么 to Soften the Tone in a Negative Sentence (the book marks each change with an arrow): 1. There is no grass or trees here. (translations mine)"), ("这儿没什么草和树。", "→ There isn’t much grass or many trees here."),
      ("他这么说没道理。", "2. It is unreasonable for him to say so."), ("他这么说没什么道理。", "→ There isn’t much reason in what he says."),
      ("那个电影不好看。", "3. That movie is not good."), ("那个电影没什么好看的。", "→ That movie is not much to watch. (好看的 here is a noun phrase)"),
      ("我今天太忙了，中午都没吃饭。", "4. I was too busy today and didn’t even eat lunch."), ("我今天太忙了，中午都没吃什么饭。", "→ I was too busy today and didn’t eat much of a lunch."),
      ("做这个工作我没经验。", "5. I have no experience in doing this job."), ("做这个工作我没什么经验。", "→ I don’t have much experience in doing this job."),
      ("那首歌不好听。", "Note: With adjectives, 怎么 is used to soften the tone. Instead of this: That song is not nice to listen to."), ("那首歌不怎么好听。", "say this: That song isn’t all that nice to listen to.")]
SX = [("A", "今天公园里的人多不多？", "Activity 2A-1 (the book’s suggested answers; translations mine). A: Are there many people in the park today?"), ("B", "今天公园里没什么人。", "B: There aren’t many people in the park today."),
      ("A", "今天你们有听力作业吗？", "2. A: Do you have listening homework today?"), ("B", "今天我们没什么听力作业。", "B: We don’t have much listening homework today."),
      ("A", "他们的网站的特色是什么？", "3. A: What is the special feature of their website?"), ("B", "他们的网站没什么特色。", "B: Their website doesn’t have much of a special feature."),
      ("A", "老李他们那儿的风景怎么样？好看吗？", "4. A: How is the scenery where Lao Li and the others are? Is it pretty?"), ("B", "他们那儿没什么好看的风景。", "B: There isn’t much pretty scenery where they are."),
      ("A", "听说你写了一本书，是吗？", "5. A: I hear you wrote a book, is that so?"), ("B", "我没写什么书。", "B: I haven’t written any book to speak of."),
      ("A", "你在杭州认识很多人吧？", "6. A: You know a lot of people in Hangzhou, don’t you?"), ("B", "我在杭州不认识什么人。", "B: I don’t know many people in Hangzhou.")]
L3 = lesson(
    "Lesson 28 Presentation 3 grammar: inserting a question to draw the listener’s attention, and 什么 to soften a negative sentence",
    "听说了吗？ · 你知道吗？ · 你发现没有？ · 没什么草和树 · 没什么道理 · 不怎么好听",
    requires=[],
    cards=[
        card("Discourse Grammar: Inserting a Question to Draw Listener’s Attention",
             "To describe something in spoken Chinese, you may start by asking a question. This can help attract the listener’s attention. The following examples show two methods of description; one is direct (a), and the other begins with a question (b). Activity 1: A. Modify the statements so they begin with a question: 1. 九零后才二三十岁，可有的已经是大公司的老板了。 2. 要学好中文就得多说。 3. 那部新电影很好看。 4. 咱们这儿现在能看到蓝天了！ 5. 后来她越想越觉得女儿说得有道理。 B. Pair up and share your work. Each partner will write five sentences that describe things in Monterey or DLI, each starting with a question. The examples, my versions and my sentences:",
             examples=[D(z, e) for z, e in Q5 + M1 + M1B]),
        card("什么 to Soften the Tone in a Negative Sentence",
             "Sometimes 什么 is used before a noun or noun phrase in a negative sentence to soften the tone a bit. It is similar to “little” or “few” in English. With adjectives, 怎么 is used to soften the tone. Activity 2: A. Complete the exchanges using 什么 to soften the tone. B. Pair up and check your work. Check the suggested answers below to refine your work. The examples and the book’s suggested answers:",
             examples=[D(z, e) for z, e in SH] + dlg(SX)),
    ],
    exercises=[
        M("Why might you start a description with a question like 听说了吗？", "To attract the listener’s attention", ["To end the talk", "To ask for money", "To say goodbye"], "This can help attract the listener’s attention."),
        M("Which sentence starts with a question?", "你知道吗？锻炼太多对身体也不好", ["锻炼太多对身体也不好", "不要锻炼", "锻炼很好"], "你知道吗？…."),
        M("What does 这儿没什么草和树 mean?", "There isn’t much grass or many trees here", ["There is lots of grass", "There are no people", "It rains here"], "没什么 softens the tone."),
        M("What does 什么 do before a noun in a negative sentence?", "Softens the tone", ["Makes it a question", "Makes it past tense", "Makes it louder"], "to soften the tone a bit."),
        M("Which is used to soften the tone with adjectives?", "怎么", ["什么", "哪里", "多少"], "那首歌不怎么好听."),
        M("What does 那首歌不怎么好听 mean?", "That song isn’t all that nice to listen to", ["That song is wonderful", "That song is long", "I wrote that song"], "不怎么好听."),
        M("Which is the softened answer to ‘Do you have listening homework today?’", "今天我们没什么听力作业", ["今天我们不作业", "今天作业很多", "我们没作业了吗"], "今天我们没什么听力作业."),
        F("听说了吗？今天新华商场的女装打七___呢。", "折", ["块", "月", "天"], "打七折: 30 percent off."),
        F("他这么说没什么道___。", "理", ["字", "话", "书"], "道理: reason."),
        F("今天公园里没什么___。", "人", ["吗", "了", "的"], "没什么人."),
    ],
)

# ------------------------------------------------------------------ 4. grammar: ...不..., 但是...很..., 要...就..., 同时
C1 = [("她学中文开始得不早，但是学得很好。", "The …不…, 但是…很… Construction: 1. She did not start learning Chinese early, but she learns it very well. (translations mine)"), ("一次两次早起床锻炼身体不难，但是每天早起床锻炼身体很难。", "2. Getting up early to exercise once or twice is not hard, but doing so every day is very hard."),
      ("我不觉得他的想法很好，但是很理解他为什么这么想。", "3. I don’t think his idea is very good, but I understand very well why he thinks so."), ("他对我很好，很像是我的哥哥，但他不是我哥哥。", "4. He is very good to me and is very much like my older brother, but he is not my brother."),
      ("我的英文阅读很好，但是我的英语口语不好。", "5. My English reading is very good, but my spoken English is not.")]
Q3 = [("说话人怎么了？", "Activity 3A-1 (questions as printed; my answers follow in the scripts below): What happened to the speaker?"), ("在那个地方他有很多好朋友吗？", "3A-2: Does he have many good friends in that place?"), ("蒙特雷秋天常下雨吗？", "3A-3: Does it often rain in Monterey in autumn?"), ("大家都能上电视吗？", "3A-4: Can everyone get on TV?"), ("他妈妈高兴还是不高兴？", "3A-5: Is his mother happy or unhappy?"), ("他儿子最近学习认真不认真？", "3A-6: Has his son been studying seriously lately?")]
S3 = [("今天中午我不小心把电话丢了，很不开心，可是下午又找到了，我马上又高兴了。", "Activity 3B script, 1 (translations mine): At noon today I carelessly lost my phone and was very unhappy, but I found it again in the afternoon and was happy again right away."), ("在那儿他认识的人很多，可是好朋友没有几个。", "2: He knows many people there, but has few good friends."),
      ("蒙特雷冬天下雨很多，但是秋天下得不多。", "3: It rains a lot in Monterey in winter, but not much in autumn."), ("看电视很容易，可是上电视却没那么容易。", "4: Watching TV is easy, but getting on TV is not so easy."),
      ("我几个星期没给家里打电话，妈妈不高兴，可今天我突然回家，她高兴地跳了起来。", "5: I hadn’t called home for several weeks and my mom was unhappy, but today I suddenly came home and she jumped for joy."), ("他儿子最近学习很不认真，可是玩儿游戏特别认真。", "6: His son has been very careless in his studies lately, but is especially serious about playing games.")]
S3M = [("每天做听力作业不难，但是每天做完所有的作业很难。", "Activity 3C (my three sentences, 1): Doing the listening homework each day is not hard, but finishing all the homework every day is very hard."), ("我的汉字写得不好，但是我的发音很好。", "2: My characters are not well written, but my pronunciation is very good."), ("蒙特雷夏天不太热，但是风很大。", "3: Monterey summers are not too hot, but it is very windy.")]
Y1 = [("你的手机该换了。要换就换个好的，我给你钱。", "The 要+Verb+就+Verb …的 Construction (similar to “get a good one if you really want it”): 1. Your phone should be replaced. If you replace it, get a good one; I’ll give you the money. (translations mine)"), ("这个工程咱们来做吧，要做就做个最有意思的。", "2. Let’s do this project; if we do it, let’s do the most interesting one.")]
Y2 = [("A", "电影院里同时演三个电影，咱们看哪个？", "3. A: Three movies are showing at the cinema at the same time; which shall we watch?"), ("B", "看这个吧，同学们都说好。要看就看大家都喜欢的。", "B: Let’s watch this one; classmates all say it’s good. If we watch, let’s watch what everyone likes."),
      ("A", "中午咱们去哪儿吃饭。", "4. A: Where shall we go for lunch? (the book ends this question with a period)"), ("B", "去海边那家中餐馆吧，在这儿它比较有名，要去就去好的。", "B: Let’s go to that Chinese restaurant by the sea; it is rather famous here, and if we go, let’s go to a good one.")]
Y3 = [("吃的东西我要买就买最好的，可他呢，要买就买最便宜的。", "5. For food, if I buy, I buy the best, but he, if he buys, buys the cheapest.")]
YM = [("我要买手机就买最新的。", "Activity 4B (my four sample statements; the book asks for two true and two false ones, which is for the learner to decide), 1: If I buy a phone, I buy the newest."), ("要吃中餐就去海边那家中餐馆吃。", "2: If you want Chinese food, go to that Chinese restaurant by the sea."), ("要学中文就学最难的。", "3: If you study Chinese, study the hardest kind."), ("要喝咖啡就喝最便宜的。", "4: If you drink coffee, drink the cheapest.")]
TS1 = [("我们是学生，同时我们也是军人，得经常参加军事训练。", "Discourse Grammar: Adverb 同时 (at the same time, on the other hand). 1. We are students, and at the same time we are also soldiers and have to take part in military training often. (translations mine)"), ("中国是一个经济大国，同时它也是一个发展中国家。", "2. China is a big economic power, and at the same time it is also a developing country."),
       ("他很想找一个好工作，同时他也不想住得离家太远。", "3. He very much wants to find a good job, and at the same time he doesn’t want to live too far from home."), ("张老师要我们好好准备下星期的考试，同时她也要我们不要熬夜，注意休息。", "4. Teacher Zhang wants us to prepare well for next week’s exam, and at the same time she also wants us not to stay up late and to get rest."),
       ("我每天花很多时间在手机上看东西，同时我也知道这样做对身体不好。", "5. I spend a lot of time every day looking at things on my phone, and at the same time I also know that doing so is bad for my health.")]
TJ = table(["", "Jumbled expressions for Activity 5A"], [["1", "教英语 | 他也是 | 同时 | 他 | 合唱团的团长 | 在附近的中学"], ["2", "最好的 | 我同学 | 朋友 | 同时 | 他是 | 他也是 | 我"], ["3", "非常棒 | 风景 | 同时 | 加州的 | 加州的 | 大学 | 很漂亮 | 也"], ["4", "再吃几天药 | 注意休息 | 同时 | 你还得 | 要"], ["5", "她也 | 同时 | 一张生日卡 | 一份礼物 | 送给妈妈 | 她寄给妈妈"]], title="Activity 5A: rearrange the expressions to make logical and correct sentences")
TS2 = [("他在附近的中学教英语，同时他也是合唱团的团长。", "Activity 5B suggested answer 1: He teaches English at a nearby middle school, and at the same time he is also the head of the choir."), ("他是我同学，同时他也是我最好的朋友。", "2: He is my classmate, and at the same time he is also my best friend."), ("加州的风景很漂亮，同时加州大学也非常棒。", "3: California’s scenery is beautiful, and at the same time the University of California is also excellent."), ("你还得再吃几天药，同时要注意休息。", "4: You still have to take medicine for a few more days, and at the same time you should rest."), ("她寄给妈妈一张生日卡。同时，她也送给妈妈一份礼物。", "5: She mailed her mother a birthday card. At the same time, she also gave her mother a gift.")]
TSM = [("我每天都要上课。同时，我还要做很多作业。", "Activity 5C (my four sentences with 同时 at the beginning, 1): I have class every day. At the same time, I also have a lot of homework."), ("我在学习中文。同时，我也在了解中国文化。", "2: I am studying Chinese. At the same time, I am also learning about Chinese culture."), ("我喜欢蒙特雷的天气。同时，我也喜欢这里的海边。", "3: I like Monterey’s weather. At the same time, I also like the seaside here."), ("我要好好学习。同时，我也要注意休息。", "4: I want to study hard. At the same time, I also want to get enough rest.")]
L4 = lesson(
    "Lesson 28 Presentation 3 grammar: …不…, 但是…很…, 要+Verb+就+Verb…的 and 同时",
    "不难，但是很难 · 要买就买最好的 · 同时 · 他也是 · 再吃几天药，同时要注意休息",
    requires=[],
    cards=[
        card("The …不…, 但是…很… Construction",
             "This construction emphasizes a certain aspect over another aspect. With it the speaker first acknowledges the existence of one aspect, and then says something to emphasize the other. This is not a fixed usage, and similar expressions can be used to replace 不, 但是 and 很 respectively. The structure can also be turned into …很…, 但是…不… or others that are similar. Activity 3: A. Listen to the short dialogs and answer the questions in Chinese. Use the …不…, 但是…很… or similar constructions. B. Pair up and share your work. Then go over the scripts to refine your sentences. C. Write three sentences describing your studies or life, using the construction or its variations. Share your work with your partner. The examples, the questions, the scripts and my three sentences:",
             examples=[D(z, e) for z, e in C1 + Q3 + S3 + S3M]),
        card("The 要+Verb+就+Verb …的 Construction",
             "This construction is similar to “get a good one if you really want it,” or “do it this way if you really want to do it.” Activity 4: A. Pair up. Study each of the pictures (six pictures, which are not included), and take turns saying something about each one using the construction. B. Write four statements using the construction. Two of the statements will be false and the other two true. Share your statements with the class, and have your classmates guess which two statements are true. The examples and my four statements:",
             examples=[D(z, e) for z, e in Y1] + dlg(Y2) + [D(z, e) for z, e in Y3 + YM]),
        card("Discourse Grammar: Adverb 同时",
             "In addition to indicating two or more things happening at the same time, 同时 can also be used at the beginning of a sentence to indicate “at the same time” or “on the other hand.” Activity 5: A. Rearrange the expressions provided to make logical and correct sentences. Then share your work with a classmate. B. Go over the suggested answers below and refine your work if necessary. C. Write four statements that describe you and your life at DLI. Use 同时 at the beginning of each sentence. Share your work with your partner. The examples, the suggested answers and my four sentences:",
             tables=[TJ], examples=[D(z, e) for z, e in TS1 + TS2 + TSM]),
    ],
    exercises=[
        M("What does the …不…，但是…很… construction do?", "Emphasizes one aspect over another", ["Asks a question", "Expresses a past event", "Gives an order"], "emphasizes a certain aspect over another aspect."),
        M("What does 看电视很容易，可是上电视却没那么容易 contrast?", "Watching TV and getting on TV", ["TV and radio", "Work and sleep", "Day and night"], "看电视很容易，可是上电视却没那么容易."),
        M("What does 要买就买最好的 mean?", "If you buy, buy the best", ["Don’t buy anything", "Buy the cheapest", "Buy two"], "要…就…的."),
        M("What is the 要+Verb+就+Verb …的 construction like in English?", "“Get a good one if you really want it”", ["“I used to…”", "“Never again”", "“Maybe not”"], "similar to get a good one if you really want it."),
        M("What does 同时 at the start of a sentence mean?", "At the same time; on the other hand", ["Never", "In the past", "By the way only"], "同时 at the beginning of a sentence."),
        M("In script 5, why does the mother jump for joy?", "Her child suddenly came home", ["She won a prize", "She got a gift", "She found her phone"], "今天我突然回家，她高兴地跳了起来."),
        M("What does the son do seriously in the script?", "Play games", ["Study", "Cook", "Run"], "玩儿游戏特别认真."),
        M("Which is the suggested answer of 5 in Activity 5B?", "她寄给妈妈一张生日卡。同时，她也送给妈妈一份礼物", ["她送给妈妈一张生日卡同时", "同时她也生日卡", "一份礼物她寄给妈妈了同时"], "the book’s suggested answer."),
        F("她学中文开始得不早，但是学得___好。", "很", ["太", "不", "没"], "…不…，但是…很…."),
        F("你还得再吃几天药，同___要注意休息。", "时", ["天", "年", "月"], "同时: at the same time."),
        F("这个工程咱们来做吧，要做就做个最有意___的。", "思", ["见", "义", "念"], "有意思: interesting."),
    ],
)

UNIT = unit("第二十八课 Presentation 3: 老李的直播, 温城辉, 活动, 问题, 什么, 不…但是…很…, 要…就…, 同时", [L1, L2, L3, L4])
