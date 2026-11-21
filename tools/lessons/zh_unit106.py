"""Unit 106: Lesson 30 (Unit 5 review), Skill Integration Review Activities 7-10 (China's three waves of studying abroad, the new occupations article, the post-90s generation,
and the education article). Pictures and the three structure diagrams of Activity 8 are not included; numbers the book writes as digits are spelled out in Chinese text; topic sentences,
summaries, definitions, word-sorting keys and answers the book leaves blank are mine and labeled. The book's 有着有更高 is read as 有着更高."""
from zh_auto import *
from zh_l29_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('成长为', 1, 'zhang3'), ('家长', 1, 'zhang3'), ('增长', 1, 'zhang3'), ('舍得', 0, 'she3'), ('舍得', 1, 'de5'), ('离职率', 2, 'lv4'), ('朝九晚五', 0, 'zhao1')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段里")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

# ------------------------------------------------------------------ act 7
ART7 = [("从九十年代起，中国一共经历了三次留学热。第一波留学热开始于九十年代初。那时候，留学更多是个人选择，自费留学的慢慢开始多起来，不像以前有很多是公费出国留学的。当时出去的留学生毕业后有很多人选择了留在国外工作和生活，因为那时国外的待遇和条件比国内好得多。",
         "Activity 7, paragraph 1 (translations mine): Since the nineties, China has gone through three study-abroad booms in all. The first wave began in the early nineties. At that time studying abroad was more a personal choice; self-funded study slowly began to increase, unlike before, when many went abroad at public expense. Many of the students who went out then chose, after graduating, to stay abroad to work and live, because at that time pay and conditions abroad were far better than at home."),
        ("二零零零年左右，随着互联网的出现和发展，中国开始了第二波留学热。这些留学生多来自富裕的家庭。而且，这一次的留学热也可以分为两批：高中毕业出去留学的和本科读完之后出去留学的。他们主要是去国外读大学或研究生，希望以后可以找到一个工资高、待遇好、工作环境适合的理想工作，可以在国内或是在国外工作。",
         "Paragraph 2: Around 2000, with the appearance and development of the internet, China began its second study-abroad wave. These students mostly came from wealthy families. Moreover, this wave can be divided into two batches: those who went out after high school and those who went out after finishing a bachelor’s degree. They mainly went abroad to study at university or graduate school, hoping later to find an ideal job with high pay, good benefits and a suitable working environment, which they could do at home or abroad. (the book writes 2000 in digits)"),
        ("二零零八年以后，出国留学热继续升温，成为第三波留学热。经过二十年的快速发展，中国经济又上了一个新台阶，相当数量的普通工薪家庭也越来越有钱，开始加入留学大军。除了到国外读研究生、大学以外，去读中学、甚至小学的也越来越多。很多小留学生跟寄宿家庭住在一起，有的家庭还让妈妈一起去国外陪读，就是为了能够更好地照顾孩子，因为孩子太小，语言沟通和独立生活能力都不行。",
         "Paragraph 3: After 2008 the study-abroad fever kept heating up and became the third wave. After twenty years of rapid development, China’s economy had moved up to a new level, and a considerable number of ordinary salaried families also grew richer and richer and began to join the army of students abroad. Besides going abroad for graduate school and university, more and more go to middle school or even primary school. Many young students abroad live with host families, and some families even have the mother go along to accompany the child’s studies, precisely to look after the child better, because the child is too small and language communication and the ability to live independently are both inadequate. (the book writes 2008 in digits)"),
        ("一般来说，出国留学以后，留学生们的优势很明显。首先，他们的英文越来越好。另外，留学的经历也让他们更适应跟一个集体和团队一起工作。还有，他们也能够解决很多意外出现的问题。再加上国外的学位和对国外文化的了解，回国找工作的时候，他们特别受欢迎。但是，近些年来，这些“海归”们渐渐地失去了优势，因为回国的人特别多；还有，国内的高级人才也越来越多，这些回国的留学生们有时候找不到理想的工作，甚至成了“海待”。",
         "Paragraph 4: Generally speaking, after studying abroad, students’ advantages are obvious. First, their English gets better and better. Also, the experience makes them better suited to working with a group and a team. Besides, they can solve many problems that arise unexpectedly. Add a foreign degree and an understanding of foreign culture, and when they come home to look for work they are especially welcome. But in recent years these “returnees” (海归) have gradually lost the advantage, because very many people are returning; also, domestic high-level talent is increasing too, and these returned students sometimes can’t find an ideal job and even become “海待” (a pun on 海归, “returnees who wait”).")]
T7 = table(["Task", "Book’s task (the book leaves the answer lines blank)"], [
    ["A. Pre-reading", "Discuss the following topic with a partner and write down key words in Chinese: 出国留学的好处"],
    ["B", "Pair up. Each student reads two paragraphs of the news article. Determine the topic sentence in each paragraph, then write a summary of the paragraph. (Topic Sentence / Summary for each pair of paragraphs)"],
    ["C", "Share your information with your partner when you are done. Together, create a title for the article in Chinese. (The article’s own heading is 中国的三次留学热.)"],
    ["D", "Compare the three waves of Chinese students studying abroad and complete the table (留学热 | 发生时间 | 特点和不同)."]],
    title="Skill Integration Review, Activity 7 (Reading, Writing, Speaking, and Listening): the tasks")
K7 = table(["", "Topic sentence (mine)", "Summary (mine)"], [
    ["Paragraph 1", "从九十年代起，中国一共经历了三次留学热。", "第一波留学热在九十年代初，自费留学开始多起来，很多留学生毕业后留在国外工作。"],
    ["Paragraph 2", "二零零零年左右……中国开始了第二波留学热。", "第二波的留学生多来自富裕家庭，分高中毕业和本科毕业后出国两批，希望找到理想的工作。"],
    ["Paragraph 3", "二零零八年以后，出国留学热继续升温，成为第三波留学热。", "普通工薪家庭也加入留学大军，小留学生越来越多，有的妈妈还陪读。"],
    ["Paragraph 4", "一般来说，出国留学以后，留学生们的优势很明显。", "留学生的英文、团队工作能力和解决问题的能力都有优势，但近年来“海归”渐渐失去了优势。"]],
    title="Activity 7B: topic sentences and summaries (my answers; the book gives none)")
D7 = table(["留学热", "发生时间", "特点和不同 (my answers; the book leaves the table blank)"], [
    ["第一波留学热", "九十年代初", "个人选择，自费留学开始增多；毕业后很多人留在国外，因为国外待遇和条件好得多"],
    ["第二波留学热", "二零零零年左右（互联网出现和发展以后）", "多来自富裕家庭；分高中毕业和本科读完后出去两批；主要读大学或研究生，希望找到理想工作"],
    ["第三波留学热", "二零零八年以后", "普通工薪家庭也加入；中学甚至小学的小留学生越来越多，有的妈妈陪读；“海归”渐渐失去优势"]],
    title="Activity 7D: the three waves compared (my answers)")
TI7 = table(["Suggested title (mine)", "Why"], [["中国留学热的三个阶段", "It names the topic and the three stages in the article"], ["三次留学热", "A short version of the article’s own heading"]], title="Activity 7C: a title for the article (my suggestions)")
L1 = lesson(
    "Lesson 30 Skill Integration Review: China’s three waves of studying abroad",
    "留学热 · 自费留学 · 公费 · 待遇 · 工薪家庭 · 小留学生 · 寄宿家庭 · 陪读 · 海归 · 海待",
    requires=[],
    cards=[
        card("Skill Integration Review, Activity 7 (Reading, Writing, Speaking, and Listening)", "Read the news article 中国的三次留学热 and complete the tasks. The article (four paragraphs), the book’s tasks and my answers:", tables=[T7, K7, TI7, D7], examples=[D(z, e) for z, e in ART7]),
    ],
    exercises=[
        M("How many study-abroad waves has China had since the nineties, according to the article?", "Three", ["Two", "Four", "Five"], "中国一共经历了三次留学热."),
        M("In the first wave, what changed compared with earlier years?", "More students paid their own way", ["All went at public expense", "Nobody went abroad", "Only graduate students went"], "自费留学的慢慢开始多起来，不像以前有很多是公费出国留学的."),
        M("Why did many first-wave students stay abroad after graduating?", "Pay and conditions abroad were far better", ["They disliked China", "Visas were free", "Their families moved"], "因为那时国外的待遇和条件比国内好得多."),
        M("Where did second-wave students mostly come from?", "Wealthy families", ["Rural villages", "Army families", "Poor families"], "这些留学生多来自富裕的家庭."),
        M("Into which two batches could the second wave be divided?", "Those leaving after high school and those leaving after a bachelor’s degree", ["Boys and girls", "North and south", "Arts and sciences"], "高中毕业出去留学的和本科读完之后出去留学的."),
        M("Who joined the third wave?", "Ordinary salaried families", ["Only millionaires", "Only government workers", "Only farmers"], "相当数量的普通工薪家庭也越来越有钱，开始加入留学大军."),
        M("Why do some mothers go abroad with young students?", "The children are too young for language and independent living", ["The schools require it", "Mothers want to study", "Flights are cheap"], "孩子太小，语言沟通和独立生活能力都不行."),
        M("Which is NOT listed as a returnee’s advantage?", "Higher salaries guaranteed", ["Better English", "Better teamwork", "Solving unexpected problems"], "英文、团队、意外问题."),
        M("Why have returnees gradually lost their advantage?", "Many are returning and domestic talent is increasing", ["Foreign degrees are worthless", "They don’t speak Chinese", "Jobs are free"], "回国的人特别多；国内的高级人才也越来越多."),
        F("近些年来，这些“海归”们渐渐地失去了___势。", "优", ["忧", "由", "油"], "优势: advantage."),
        F("自费留学的慢慢开始多起来，不像以前有很多是公___出国留学的。", "费", ["肥", "废", "非"], "公费: at public expense."),
        F("这些回国的留学生们有时候找不到理想的工作，甚至成了“海___”。", "待", ["戴", "贷", "袋"], "海待: the book’s pun on 海归."),
    ],
)

# ------------------------------------------------------------------ act 8
ART8 = [("随着中国经济和科技快速发展，大家所做的工作和从事的职业也发生了很大的变化。新的职业和工种不停地出现，在中国公布的新职业中，除了大家最熟悉的网约配送员以外，还新增了直播销售员、电子竞技员、人工智能训练师、无人机驾驶员等新职业和新工种。",
         "Activity 8, paragraph 1 (translations mine): With the rapid development of China’s economy and technology, the work people do and the occupations they engage in have also changed greatly. New occupations and types of work keep appearing; among the new occupations announced in China, besides the online-platform delivery worker everyone knows best, live-stream seller, e-sports player, AI trainer, drone pilot and other new occupations and types of work have been added."),
        ("网约配送员，也就是大家最熟悉的“外卖小哥”、“快递小哥”这样的新职业。他们通过移动互联网平台，接收客户订单，然后根据订单的需要，按照平台提供的智能路线，在最短的时间内将订单物品送到指定地点或用户的手上。现在，一小时买菜、叫外卖、送快递等服务越来越普遍。",
         "Paragraph 2: The online-platform delivery worker (网约配送员) is the new occupation everyone knows best as the “takeout guy” or “courier guy.” Through the mobile-internet platform they receive customer orders and then, according to the order’s needs and following the smart route the platform provides, deliver the ordered goods in the shortest time to the designated place or into the user’s hands. Now one-hour grocery buying, takeout and express delivery services are more and more common."),
        ("直播销售员，就是人们熟知的“电商主播”和“带货网红”这样的职业。一支话筒、一个摄像头、一台电脑就可以打造出一种前所未有的购物体验，网红主播们正在改变大家的购物习惯。许多观众说，物美价廉是他们喜爱直播购物的最重要原因。不少主播也会在带货的同时，增加直播的娱乐和互动活动，这样他们的粉丝越来越多，流量也越来越大。",
         "Paragraph 3: The live-stream seller (直播销售员) is the occupation people know as the “e-commerce host” and the “goods-selling internet celebrity.” One microphone, one camera and one computer can create a shopping experience never seen before, and influencer hosts are changing everyone’s shopping habits. Many viewers say that good quality at a low price is the most important reason they like live-stream shopping. Quite a few hosts also add entertainment and interactive activities to the live stream while selling goods, so their fans grow more and more numerous and their traffic larger and larger."),
        ("以前，大家对电子竞技员这类职业的看法就是：他们是对电子游戏和网络游戏入迷的人。很多人认为电竞就是打游戏，他们甚至说电竞是“电子海洛因”。所以，很多家长和老师都担心孩子和学生打游戏，更不用说让他们以后做这样的工作了。可是，现在这种职业终于有了自己正式的名字“电子竞技员”，也就是从事不同类型电子竞技项目比赛、陪练、体验及活动表演的人员。电子竞技职业已经成长为一个成熟的职业。",
         "Paragraph 4: Before, people’s view of occupations like the e-sports player was that they were people addicted to video games and online games. Many people thought e-sports was just playing games and even called e-sports “electronic heroin.” So many parents and teachers worried about children and students playing games, let alone letting them do such work later. But now this occupation has finally got its own formal name, “e-sports player” (电子竞技员), meaning personnel engaged in competition, practice-partnering, experience-testing and activity performances in different types of e-sports events. The e-sports profession has grown into a mature profession.")]
T8A = table(["Task", "Book’s task"], [
    ["A", "Skim the article very quickly and determine its structure. In the diagram that follows on the next page, each paragraph is numbered, and different structures are shown (结构图 (1), (2), (3)). Select the one diagram that shows the correct order of the article, then share your answer with a classmate. (The three diagrams are not reproduced here; the layout of the numbered boxes is not clear enough in the text. My own reading of the structure: paragraph 1 introduces the new occupations in general, and paragraphs 2, 3 and 4 each describe one of them.)"],
    ["B. Speed Reading", "Work in groups of three. Individually, working as quickly as possible, find the definitions of the terms (网约配送员, 直播销售员, 电子竞技员) from the article, then underline the sentences that contain them. Share your work with your group members and complete the table in Chinese characters."],
    ["C", "In your group, read more information about the three occupations in the related paragraphs. Distribute the words from the list. Each student selects all the related words for one occupation. Then share your results with your team members."],
    ["D", "In your own words, describe the occupation you read about in Step C. Add more information if you can: 这是什么职业? 哪些人做这样的职业? 这样的职业需要做什么?"]],
    title="Skill Integration Review, Activity 8 (Reading, Writing, Speaking and Listening): the tasks")
T8B = table(["Terms", "Definition in Chinese (my answers; the book leaves the table blank)"], [
    ["网约配送员", "通过移动互联网平台接收客户订单，按照智能路线把订单物品送到指定地点或用户手上的人，也就是“外卖小哥”“快递小哥”。"],
    ["直播销售员", "就是人们熟知的“电商主播”和“带货网红”，用话筒、摄像头和电脑直播带货。"],
    ["电子竞技员", "从事不同类型电子竞技项目比赛、陪练、体验及活动表演的人员。"]],
    title="Activity 8B: definitions (my answers)")
T8C = table(["新职业", "相关词汇 (my key; the book leaves the table blank)"], [
    ["网约配送员", "移动互联网 · 客户订单 · 智能路线 · 外卖 · 快递 · 物品"],
    ["直播销售员", "话筒 · 摄像头 · 电脑 · 带货 · 娱乐 · 粉丝 · 购物 · 物美价廉 · 互动 · 流量"],
    ["电子竞技员", "陪练 · 电子海洛因 · 网络游戏 · 电子游戏 · 电子竞技项目"]],
    title="Activity 8C: the word list (words: 移动互联网 话筒 客户订单 陪练 智能路线 / 摄像头 电脑 电子海洛因 带货 网络游戏 / 娱乐 电子游戏 粉丝 购物 电子竞技项目 / 外卖 物美价廉 快递 互动 流量 物品)")
L2 = lesson(
    "Lesson 30 Skill Integration Review: new occupations in China",
    "新职业 · 网约配送员 · 直播销售员 · 电子竞技员 · 外卖小哥 · 带货网红 · 物美价廉 · 粉丝 · 流量 · 电子海洛因",
    requires=[],
    cards=[
        card("Skill Integration Review, Activity 8 (Reading, Writing, Speaking and Listening)", "Read the news article about new occupations and complete the tasks. The article (four paragraphs), the book’s tasks, and my answers and key:", tables=[T8A, T8B, T8C], examples=[D(z, e) for z, e in ART8]),
    ],
    exercises=[
        M("Which new occupation is named first, as the one everyone knows best?", "网约配送员 (online-platform delivery worker)", ["Drone pilot", "AI trainer", "Live-stream seller"], "大家最熟悉的网约配送员."),
        M("What do delivery workers receive through the platform?", "Customer orders", ["Salaries only", "Invitations", "Videos"], "接收客户订单."),
        M("How do they decide their route?", "They follow the smart route the platform provides", ["They guess", "They ask passers-by", "They use paper maps"], "按照平台提供的智能路线."),
        M("What equipment can create a new shopping experience for live-stream sellers?", "A microphone, a camera and a computer", ["A truck", "A cash register", "A printing press"], "一支话筒、一个摄像头、一台电脑."),
        M("What is the viewers’ most important reason for liking live shopping?", "Good quality at a low price", ["Free shipping", "Famous hosts", "Gifts"], "物美价廉是他们喜爱直播购物的最重要原因."),
        M("How do hosts gain more fans and traffic?", "By adding entertainment and interaction while selling", ["By lowering their voice", "By staying silent", "By selling nothing"], "增加直播的娱乐和互动活动."),
        M("What did many people used to call e-sports?", "“Electronic heroin”", ["Sports", "Art", "Education"], "他们甚至说电竞是“电子海洛因”."),
        M("What does the formal occupation of e-sports player include?", "Competition, practice-partnering, experience-testing and performances", ["Only watching games", "Only repairing computers", "Only selling games"], "比赛、陪练、体验及活动表演."),
        F("他们通过移动互联网平台，接收客户___单。", "订", ["顶", "钉", "丁"], "订单: order form."),
        F("许多观众说，物美价___是他们喜爱直播购物的最重要原因。", "廉", ["连", "莲", "怜"], "物美价廉: good and cheap."),
        F("他们甚至说电竞是“电子海洛___”。", "因", ["英", "音", "印"], "海洛因: heroin."),
        F("电子竞技职业已经成长为一个成___的职业。", "熟", ["淑", "书", "树"], "成熟: mature."),
    ],
)

# ------------------------------------------------------------------ act 9
ART9 = [("中国的九零后大多是独生子女，很少有兄弟姐妹，他们得到了更多的关心和照顾。从小他们的生活环境和学习条件就不一样，除了有更好的学校教育以外，每个家庭也都舍得把钱花在孩子身上，让他们从小就学外语和各种技能。再加上互联网和个人电脑的普及，他们还可以在网上找到很多的学习材料。所以，很多人的外语能力很强，文化和教育程度也更高。",
         "Activity 9, paragraph 1 (translations mine): Most of China’s post-90s are only children with few brothers or sisters, and they received more care and attention. From childhood their living environment and study conditions were different: besides better school education, every family was willing to spend money on its child and let them learn foreign languages and various skills from an early age. Add the spread of the internet and personal computers, and they can also find a lot of study material online. So many have strong foreign-language ability and a higher level of culture and education. (the book writes 90 in digits)"),
        ("跟“七零后”“八零后”相比，九零后在工作以后，他们的离职率明显比较高。要是工作不合适，他们马上就会换工作。对于九零后，稳定的工作不再能够满足他们，他们更注重理想的工作，有前途的工作。找工作时，他们最看重的是工作要能够实现个人的理想。还有的认为，工作必须适合自己的兴趣，做人开心最重要。",
         "Paragraph 2: Compared with the “post-70s” and “post-80s,” the post-90s clearly have a higher turnover rate once they start working. If a job isn’t suitable, they will change jobs right away. For the post-90s, a stable job can no longer satisfy them; they value an ideal job, a job with prospects. When looking for work, what they care about most is that the job can realize their personal ideals. Some also think that a job must suit one’s interests and that being happy is what matters most. (the book writes 70, 80 and 90 in digits)"),
        ("进入职场后的九零后们，他们常常有着更高的目标和梦想。很多九零后选择了创业这条路，他们创办公司，自己当老板。马欢是一家自媒体创业公司的创始人。大学毕业之后，他进入一家单位开始朝九晚五的生活。但是，日复一日的工作和无趣的生活让他选择了辞职，开始互联网创业。经过几年的努力和管理，他的自媒体公司吸引了众多的读者，粉丝超过了二十五万，文章的阅读量也在快速增长，他也开始变得小有名气。马欢在创业中感受到快乐，实现了自我的价值。",
         "Paragraph 3: The post-90s who have entered the workplace often have higher goals and dreams. Many post-90s chose the road of starting a business: they set up companies and become their own bosses. Ma Huan is the founder of a self-media startup. After graduating from university he joined an organization and began a nine-to-five life. But the day-after-day work and dull life made him choose to resign and start an internet business. After several years of effort and management, his self-media company attracted a great many readers, his fans exceeded 250,000, the reading volume of his articles is growing fast, and he is beginning to become somewhat well known. In starting a business Ma Huan has felt joy and realized his self-worth. (the book prints 常常有着有更高的目标, with a doubled 有; read here as 有着更高的目标. The book writes 90 and 25 万 in digits.)"),
        ("中国的九零后，爱思考、想法独特，思想独立，个人能力也很强，他们正成为有前途的一代人。",
         "Paragraph 4: China’s post-90s love to think, have unique ideas and independent thought, and have strong personal ability; they are becoming a generation with a future.")]
T9 = table(["Task", "Book’s task"], [
    ["A", "Work in groups of three. Each student reads one of the first three paragraphs. Find and underline the topic sentence in your paragraph. Then summarize the paragraph in the space provided (Student 1 第一段 / Student 2 第二段 / Student 3 第三段)."],
    ["B", "Exchange your information with your group members when you are done."],
    ["C", "Read paragraph four together and discuss the relationship between it and the previous three paragraphs."],
    ["D", "In your group, discuss the characteristics of the Millennial generation in the U.S. (Characteristics of Millennials 美国千禧一代的特点: a blank box.)"],
    ["E", "Compare the differences and similarities between the Chinese generations born from 1990 to 2000 and the U.S. Millennial generation. (中国90后 vs 美国千禧一代: a table with 相同点 and 不同点, both blank.)"]],
    title="Skill Integration Review, Activity 9 (Reading, Writing, Speaking and Listening): the tasks")
K9 = table(["Paragraph", "Topic sentence (mine)", "Summary (mine)"], [
    ["第一段", "中国的九零后大多是独生子女，很少有兄弟姐妹，他们得到了更多的关心和照顾。", "九零后多是独生子女，家庭舍得花钱，学习条件好，所以外语、文化和教育程度更高。"],
    ["第二段", "跟“七零后”“八零后”相比，九零后在工作以后，他们的离职率明显比较高。", "九零后更注重理想的、有前途的工作，工作不合适就马上换。"],
    ["第三段", "进入职场后的九零后们，他们常常有着更高的目标和梦想。", "很多九零后选择创业，像马欢那样离开朝九晚五的生活，在创业中实现自我价值。"],
    ["第四段", "(the whole paragraph is the conclusion)", "总结前三段：九零后爱思考、有想法、独立、能力强，是有前途的一代人。"]],
    title="Activity 9A and 9C: topic sentences, summaries and the role of paragraph four (my answers; the book gives none)")
L3 = lesson(
    "Lesson 30 Skill Integration Review: China’s post-90s generation",
    "九零后 · 独生子女 · 离职率 · 注重 · 前途 · 创业 · 创始人 · 朝九晚五 · 辞职 · 自媒体 · 粉丝 · 自我价值",
    requires=[],
    cards=[
        card("Skill Integration Review, Activity 9 (Reading, Writing, Speaking and Listening)", "Read the news report about China’s post-90s generation and complete the tasks. The report (four paragraphs), the book’s tasks and my answers:", tables=[T9, K9], examples=[D(z, e) for z, e in ART9]),
    ],
    exercises=[
        M("Why did most post-90s receive more care and attention?", "They are mostly only children", ["They are older", "They live abroad", "They have many siblings"], "大多是独生子女，很少有兄弟姐妹，他们得到了更多的关心和照顾."),
        M("What are families willing to spend money on, per paragraph 1?", "Their child’s learning of foreign languages and skills", ["Cars", "Travel", "Jewelry"], "舍得把钱花在孩子身上，让他们从小就学外语和各种技能."),
        M("How does the post-90s turnover rate compare with the post-70s and post-80s?", "Clearly higher", ["The same", "Lower", "Unknown"], "离职率明显比较高."),
        M("What do the post-90s care about most when job hunting?", "Realizing personal ideals", ["A stable salary", "Short hours", "A famous company"], "最看重的是工作要能够实现个人的理想."),
        M("What is Ma Huan’s company?", "A self-media startup", ["A restaurant", "A school", "A bank"], "马欢是一家自媒体创业公司的创始人."),
        M("Why did Ma Huan resign?", "The day-after-day work and dull life", ["He was fired", "He moved abroad", "He retired"], "日复一日的工作和无趣的生活让他选择了辞职."),
        M("How many fans does his company have?", "More than 250,000", ["More than 25", "More than 2,500", "More than 25 million"], "粉丝超过了二十五万."),
        M("What role does paragraph four play?", "It sums up the first three paragraphs as a conclusion", ["It starts a new topic", "It gives a joke", "It lists sources"], "他们正成为有前途的一代人."),
        F("中国的九零后大多是独___子女。", "生", ["身", "立", "自"], "独生子女: only child."),
        F("他进入一家单位开始朝九晚___的生活。", "五", ["六", "七", "八"], "朝九晚五: nine to five."),
        F("日复一日的工作和无趣的生活让他选择了辞___。", "职", ["织", "直", "值"], "辞职: resign."),
        F("他们更注重理想的工作，有前___的工作。", "途", ["图", "涂", "徒"], "前途: prospects."),
    ],
)

# ------------------------------------------------------------------ act 10
ART10 = [("中国人自古以来就非常重视教育，可以说这是中国人的一个好传统。教育家孔子在两千多年前就开始设立自己的学堂，学生们跟着孔子不但学习中国文化知识，还学习孔子的思想，孔子希望通过教育让国家更强大。同时，中国的家庭也相信教育可以改变一个人的前途。因此，每一个中国家庭，只要有一点能力，都会想尽一切办法来让自己的孩子能够上更好的学校，接受更好的教育。",
          "Activity 10, paragraph 1 (translations mine): Chinese people have valued education very much since ancient times, and one can say this is a good tradition of the Chinese. The educator Confucius began setting up his own school more than two thousand years ago; students who followed Confucius studied not only Chinese cultural knowledge but also Confucius’ thought, and Confucius hoped to make the country stronger through education. At the same time, Chinese families also believe education can change a person’s future. Therefore every Chinese family, as long as it has a little ability, will think of every way to let its children go to a better school and receive a better education."),
         ("中国古代“孟母三迁”的故事，说的就是伟大的思想家孟子小时候，他的母亲三次搬家，为的是让他有好的老师、好的邻居、好的同学，以便受到好的教育。而在现代的中国，这样的家庭到处都是。很多的家庭都会花高价买学区房，好让自己的孩子可以上更好的学校。还有的家庭把孩子送到私立学校或双语学校，让孩子可以学习更加国际化的课程。更有钱的家庭就直接把孩子送到国外去留学，希望他们的孩子以后可以有更大的优势。",
          "Paragraph 2: The ancient Chinese story of “Mencius’ mother moved three times” tells how, when the great thinker Mencius was small, his mother moved house three times so that he would have good teachers, good neighbors and good classmates and thereby receive a good education. In modern China such families are everywhere. Many families will pay a high price for a house in a good school district so that their children can go to a better school. Some families send their children to private or bilingual schools so they can study more internationalized courses. Richer families directly send their children abroad to study, hoping their children will have a bigger advantage later."),
         ("除了注意孩子的学习环境以外，家长们也特别关注孩子学习和各方面能力的培养。上学以前，孩子们会被送到早教班，学习各种智力开发的课程和游戏。上学以后，家长们给孩子们报名参加各种兴趣班、补习班。外语是家长们最喜欢给孩子们选的课程。另外，还有各种音乐课程，舞蹈课，美术课。高年级的还会参加各种数学、化学、物理等竞赛班的学习。",
          "Paragraph 3: Besides paying attention to the children’s learning environment, parents also especially care about the cultivation of their children’s learning and abilities in all respects. Before school, children are sent to early-education classes to study courses and games that develop intelligence. After they start school, parents sign their children up for all kinds of interest classes and tutoring classes. Foreign languages are the course parents like best to choose for their children. There are also music courses, dance classes and art classes. Older students also join mathematics, chemistry, physics and other competition classes."),
         ("有的家长特别希望孩子以后可以成功，所以给了孩子很多的压力。有些人还被戏称为“虎妈”和“狼爸”，就是因为他们教育孩子的方式特别严厉。但是这样做的效果并不好，有时候让孩子觉得父母不尊重他们的学习自由，慢慢地失去了学习的兴趣，和父母的关系也变得越来越紧张。",
          "Paragraph 4: Some parents especially hope their children will succeed later, and so they put a lot of pressure on them. Some are even jokingly called “tiger moms” and “wolf dads” precisely because their way of educating children is especially strict. But this approach does not work well; sometimes it makes children feel their parents do not respect their freedom to study, so they slowly lose interest in learning and their relationship with their parents grows more and more tense.")]
T10 = table(["Task", "Book’s task"], [
    ["A", "Read the article and highlight the topic sentence of each paragraph. If you cannot find the topic sentence, use your own words to summarize the paragraph in one Chinese sentence. (Four numbered blank lines.)"],
    ["B", "After you finish, pair up and share your topic sentences with a partner."],
    ["C", "Each student reads two paragraphs and writes the answers for the following questions. Student 1 (Paragraphs 1 and 2): 1. 为什么每个中国家庭想送自己的孩子上更好的学校，接受更好的教育? 2. 什么是“孟母三迁”的故事? 3. 现代中国家庭为了孩子的教育常常做什么? Student 2 (Paragraphs 3 and 4): 1. 中国的父母怎么培养孩子的学习和各方面的能力? 2. 什么是“虎妈”和“狼爸”? 3. 中国的家长给孩子太多的压力造成什么样的后果?"],
    ["D", "Share your answers with your partner and find out the answers to your partner’s questions."],
    ["E", "Individually, write a short paragraph that describes how your parents taught you, their educational styles and methods, etc. Write five to eight sentences to complete this task. (The title line is 父母对我的教育.)"],
    ["F", "Work in groups of three and share your stories."]],
    title="Skill Integration Review, Activity 10 (Reading, Writing, Speaking, and Listening): the tasks")
K10 = table(["Question", "My answer (the book gives none)"], [
    ["A. Topic sentences", "1. 中国人自古以来就非常重视教育。 2. 在现代的中国，为了让孩子受到好的教育，这样的家庭到处都是。 3. 家长们也特别关注孩子学习和各方面能力的培养。 4. 有的家长特别希望孩子以后可以成功，所以给了孩子很多的压力。"],
    ["C Student 1, 1", "因为中国人重视教育，相信教育可以改变一个人的前途。"],
    ["C Student 1, 2", "孟子小时候，他的母亲为了让他有好的老师、邻居和同学，三次搬家。"],
    ["C Student 1, 3", "买学区房，把孩子送到私立学校或双语学校，更有钱的家庭送孩子出国留学。"],
    ["C Student 2, 1", "上学前送孩子去早教班；上学后报各种兴趣班、补习班，例如外语、音乐、舞蹈、美术和竞赛班。"],
    ["C Student 2, 2", "教育孩子的方式特别严厉的家长。"],
    ["C Student 2, 3", "孩子觉得父母不尊重他们的学习自由，慢慢失去学习的兴趣，和父母的关系越来越紧张。"]],
    title="Activity 10: my answers")
L4 = lesson(
    "Lesson 30 Skill Integration Review: education in Chinese families",
    "重视教育 · 孔子 · 孟母三迁 · 学区房 · 私立学校 · 双语学校 · 早教班 · 兴趣班 · 补习班 · 虎妈 · 狼爸 · 严厉",
    requires=[],
    cards=[
        card("Skill Integration Review, Activity 10 (Reading, Writing, Speaking, and Listening)", "Read the article from an educational magazine and complete the tasks. The article (four paragraphs), the book’s tasks and my answers:", tables=[T10, K10], examples=[D(z, e) for z, e in ART10]),
    ],
    exercises=[
        M("Who began setting up his own school more than two thousand years ago?", "Confucius", ["Mencius", "Laozi", "Mozi"], "教育家孔子在两千多年前就开始设立自己的学堂."),
        M("What did Confucius hope to achieve through education?", "A stronger country", ["A bigger family", "A famous name", "More land"], "孔子希望通过教育让国家更强大."),
        M("Why did Mencius’ mother move house three times?", "So he would have good teachers, neighbors and classmates", ["To escape taxes", "To be near relatives", "To find work"], "为的是让他有好的老师、好的邻居、好的同学."),
        M("What do many modern families pay a high price for?", "A house in a good school district", ["A car", "A trip abroad", "A pet"], "很多的家庭都会花高价买学区房."),
        M("Where are children sent before they start school?", "Early-education classes", ["Boarding schools", "Factories", "Hospitals"], "上学以前，孩子们会被送到早教班."),
        M("Which course do parents most like to choose for their children?", "Foreign languages", ["Cooking", "Farming", "Sewing"], "外语是家长们最喜欢给孩子们选的课程."),
        M("Who are called “tiger moms” and “wolf dads”?", "Parents who educate their children in an especially strict way", ["Parents who work abroad", "Parents who never study", "Parents who own pets"], "他们教育孩子的方式特别严厉."),
        M("What can too much pressure lead to?", "Children lose interest in learning and relations grow tense", ["Higher grades always", "Children skip meals", "More free time"], "慢慢地失去了学习的兴趣，和父母的关系也变得越来越紧张."),
        F("中国人自古以来就非常重视___育。", "教", ["学", "读", "写"], "教育: education."),
        F("上学以前，孩子们会被送到早___班。", "教", ["叫", "较", "轿"], "早教班: early-education class."),
        F("有些人还被戏称为“虎妈”和“狼___”。", "爸", ["把", "吧", "罢"], "狼爸: wolf dad."),
        F("他们教育孩子的方式特别严___。", "厉", ["利", "力", "立"], "严厉: strict."),
    ],
)

UNIT = unit("第三十课 复习课 Unit 5 Review: 综合技能复习 (2)", [L1, L2, L3, L4])
