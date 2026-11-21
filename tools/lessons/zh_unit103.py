"""Unit 103: Lesson 30 (Unit 5 review), Presentation Activities Review: Activity 1 (fifteen situations and the suggested answers), Activity 2 (True/False and ten dialog scripts),
Activity 3 (matching Column A with Column B). Audio and pictures are not included; numbers the book writes as digits are spelled out in Chinese text;
answers, keys, samples and translations the book leaves out are mine and labeled. Three book slips are read as 准时到达, 加塞儿 and 农民工."""
from zh_auto import *
from zh_l29_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('用不了', 2, 'liao3'), ('长大', 0, 'zhang3'), ('增长', 1, 'zhang3'), ('来不了', 2, 'liao3')):
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

PART = ["吗", "们", "呢"]

# ------------------------------------------------------------------ 1. presentation activities review, activity 1
SIT = [
 ("How making your own food can be faster than having it delivered to you. Order your food on this platform with your mobile phone and it will arrive in twenty minutes. You can also order fruit and drinks.", "(rhetorical question，叫外卖，点)",
  "自己做饭能比叫外卖快吗？用手机在这个平台上点饭，二十分钟就能到，还可以点一些水果和饮料。"),
 ("Homestays are both convenient and inexpensive, which is an important reason why we choose them. In addition, the procedure for finding one is very simple. All it requires is to move your fingers a little bit. It will take less than five minutes.", "(又…又…，是…的重要原因，另外，动动手指)",
  "民宿又方便又便宜，这是我们选它的重要原因。另外，手续也非常简单，动动手指就行，用不了五分钟。"),
 ("In the past, people used to wait a long time to get a taxi. Now they just use their smart phone to order a ride. Because the vehicle can accurately find your location, it will usually arrive on time.", "(等半天，用…叫车，准确定位)",
  "以前出行时打车往往等半天，现在就用智能手机直接预约叫车。因为车能够准确定位，所以一般都会准时到达。"),
 ("At first, we were worried that a student might develop bad habits there. Now we know that the members of her host family are all very nice and they often help her with her life needs and her studies. We are not as worried any longer.", "(养成，寄宿家庭，在生活和学习上)",
  "一开始，我们担心孩子在那里会养成一些坏习惯，现在知道她的寄宿家庭的人都很好，在生活和学习上常常帮助她，我们就不再那么担心了。"),
 ("Many parents, no matter how hard their lives are, send their children to study in America at their own expense. After getting their degrees, some of these young people choose to stay in the United States to work, and some return to China to become “haigui.”", "(不管…也要…，拿到学位，选择)",
  "很多家长，不管自己多辛苦，也要送孩子去美国自费留学。拿到学位以后，这些年轻人有的选择留在美国工作，有的回国当“海归”。"),
 ("Nowadays, Chinese people have many ways to travel abroad. Some join tour groups, some like to travel by themselves, and some take one-destination tours. Regardless of the method, most Chinese tourists like to do a lot of shopping abroad.", "(旅游方式；有的…，有的…，还有的…；不管，都…；扫货)",
  "现在中国人出国旅游的方式多种多样。有的参加旅行团，有的自由行，还有的搞定点游。不管什么样的旅游方式，多数中国游客都喜欢在国外“扫货”。"),
 ("Every day, delivery men work from dawn to night, in the wind and in the rain, and they work like soldiers fighting a battle. Aren’t they worthy of respect since they serve everyone so well?", "(起早贪黑；风里来雨里去；跟…似的；难道不…吗？)",
  "“快递小哥”每天起早贪黑，风里来雨里去，上班就跟打仗似的。他们那么辛苦地为大家服务，难道不值得尊重吗？"),
 ("You can make money by chatting on live broadcast platforms, but to make a lot of money, it helps to be an internet celebrity with many fans. Not only can you be a celebrity by chatting, but also by singing, dancing, or cooking online.", "(赚钱，网红；不仅…，而且…)",
  "在直播平台上聊天就能赚钱，但是要赚很多钱，你得是网红，有很多粉丝。不仅网上聊天能当网红，而且在网上唱歌、跳舞、做饭也能当网红。"),
 ("With the popularity of e-sports competitions, some young people have become professional e-sports players. They are characterized by high intelligence and quick responses. I know a professional player who represented China in the World Series.", "(随着，职业…选手，特点，代表)",
  "随着电竞比赛的流行，一些年轻人成为职业电竞选手。他们的特点是智力好，反应快。我认识一个职业选手，代表中国参加过世界大赛。"),
 ("People of their generation luckily live in a prosperous time. Have you noticed this? Some people have become presidents of large companies at a young age, while others have become professors at famous universities in their early 30’s.", "(赶上，注意到，年纪轻轻，三十多岁)",
  "他们这一代人真是赶上好时候了。你注意到没有？有些人年纪轻轻就当上了大公司的老板，还有的三十多岁就成了名校的教授。"),
 ("As Teacher Wang said just now, your generation grew up in a well-informed environment, and we grew up in a completely different environment, so sometimes the two generations don’t think the same way.", "(就像…说的，而，想不到一块儿)",
  "就像王老师刚才说的，你们这一代是在一个信息发达的环境长大的，而我们长大的环境完全不同，所以两代人有时候想不到一块儿。"),
 ("It’s not difficult to start a business, but it’s difficult to start a business that customers like, with fast growing sales plus advanced management styles.", "(…不难，但是…很难；管理方式)",
  "创业不难，但是，创办一个顾客喜欢、销售增长速度快、管理方式先进的企业很难。"),
 ("The number of interest classes we enrolled our child in is relatively small. Some parents signed up seven or eight classes for their kids, but teachers say that attending too many classes could be counterproductive.", "(报，算少的，效果不好)",
  "我们给孩子报的兴趣班还算少的呢。有的家长给孩子报了七八个，可是老师说上的班太多了可能效果不好。"),
 ("With a good education, children can have a better future. However, I feel that by living in a very expensive school district and attending an expensive school, the child will not necessarily receive a good education.", "(有了…才能有…；不一定)",
  "有了好的教育，孩子才能有更好的前途。但是我觉得，住很贵的学区房，上很贵的学校，孩子不一定会得到真正好的教育。"),
 ("Parents work hard in big cities but don’t make much money, so their children have no choice but to become “left-behind children.” Even if these children live with their parents in the city, they cannot afford to attend good schools there.", "(只好；就算…也上不起…)",
  "父母在大城市努力工作，但是赚钱不多，所以他们的孩子只好做“留守儿童”。就算这些孩子和父母一起住在城市里，他们也上不起那儿的好学校。"),
]
SITT = table(["No.", "The situation (the book’s English)", "Key words"], [[str(i), en, kw] for i, (en, kw, zh) in enumerate(SIT, 1)], title="Presentation Activities Review, Activity 1A: what would you say in these situations?")
ANS = [D(zh, "Suggested answer %d (the book’s key; the English is the book’s situation, with its key words in the table): %s" % (i, en)) for i, (en, kw, zh) in enumerate(SIT, 1)]
L1 = lesson(
    "Lesson 30 Presentation Activities Review: fifteen situations and the suggested answers",
    "叫外卖 · 民宿 · 预约叫车 · 寄宿家庭 · 自费留学 · 旅游方式 · 快递小哥 · 网红 · 电竞 · 学区房 · 留守儿童",
    requires=[],
    cards=[
        card("Presentation Activities Review, Activity 1 (Speaking, Writing, and Reading)", "A. Pair up. In Chinese, take turns telling your partner what you would say in the following situations. Key words have been provided. B. Go over the suggested answer keys below and refine your sentences. (The book writes the numbers in the keys with Chinese numerals; one key reads 准时达到, which looks like a slip for 准时到达, and is written here as 准时到达.)", tables=[SITT], examples=ANS),
    ],
    exercises=[
        M("Which pattern is used in “民宿又方便又便宜”?", "又…又…", ["不仅…而且…", "虽然…但是…", "一边…一边…"], "又方便又便宜."),
        M("How long does the delivered food take to arrive, in answer 1?", "Twenty minutes", ["Five minutes", "An hour", "Two hours"], "二十分钟就能到."),
        M("What can a homestay search be done with?", "Moving your fingers, in under five minutes", ["A phone call", "A visit", "A letter"], "动动手指就行，用不了五分钟."),
        M("What can the vehicle do accurately in answer 3?", "Locate your position", ["Fly", "Talk", "Cook"], "车能够准确定位."),
        M("What did the parents worry about at first in answer 4?", "That the child would develop bad habits", ["That the house was small", "That the weather was cold", "That the school was closed"], "担心孩子在那里会养成一些坏习惯."),
        M("What do some young people choose after getting their degree, in answer 5?", "Stay in the U.S. or return to China as “haigui”", ["Quit working", "Become farmers", "Study forever"], "有的选择留在美国工作，有的回国当“海归”."),
        M("What do most Chinese tourists like to do abroad, in answer 6?", "Shop a lot (扫货)", ["Sleep", "Cook", "Run"], "多数中国游客都喜欢在国外“扫货”."),
        M("What do delivery men’s days look like, in answer 7?", "From dawn to night, like fighting a battle", ["Relaxed", "Only in summer", "Only at night"], "起早贪黑，风里来雨里去，上班就跟打仗似的."),
        M("What do you need in order to earn a lot on live-broadcast platforms, in answer 8?", "To be an internet celebrity with many fans", ["A big house", "A teacher’s degree", "A car"], "你得是网红，有很多粉丝."),
        M("Which sentence describes e-sports players, in answer 9?", "They have high intelligence and quick responses", ["They are all tall", "They are all old", "They never travel"], "他们的特点是智力好，反应快."),
        F("自己做饭能比叫外卖快___？", "吗", ["呢", "吧", "啊"], "吗: question particle."),
        F("很多家长，不管自己多辛苦，也要送孩子去美国自___留学。", "费", ["己", "由", "愿"], "自费: at one’s own expense."),
        F("我们给孩子报的兴趣班还算少的___。", "呢", ["吗", "了", "吧"], "还算少的呢: a softening particle."),
        F("所以他们的孩子___做“留守儿童”。", "只好", ["一直", "常常", "就是"], "只好: have no choice but to."),
    ],
)

# ------------------------------------------------------------------ 2. activity 2
TF = table(["No.", "Statement (the book’s)", "True/False (my key; the book gives none)"], [
    ["1", "如果你想出国旅游，得把三个平台都下载到你的手机上。", "False (Dialog 1: the platforms are for ordering takeout, homestays and rides)"],
    ["2", "外卖平台和“滴滴出行”都有定位服务。", "True (Dialog 2)"],
    ["3", "第一个说话人会去欧洲留学。", "False (Dialog 3: he is told to travel to Europe, not to study)"],
    ["4", "第一个说话人在国外学的专业(major)不太好，所以他担心回国后会成为“海待”。", "False (Dialog 4: his major is good; he worries because “haigui” have lost their advantage)"],
    ["5", "这位“快递小哥”觉得他的工作太辛苦，应该学习做网络直播，将来当“网红”。", "False (Dialog 5: his friend suggests it; he declines)"],
    ["6", "第一个说话人的儿子电脑游戏玩儿得好，反应也快，很快就要当电竞员了。", "False (Dialog 6: the speaker worries; the other suggests he try)"],
    ["7", "现在的孩子从小就学英语，两个说话人是上了大学才开始学英语的。", "True (Dialog 7)"],
    ["8", "90后和00后成长的环境信息发达，所以他们知道得多，能力也很强。", "True (Dialog 8)"],
    ["9", "两个说话人都觉得，中国人为孩子的教育花钱花得太多了。", "False (Dialog 9: they explain it as a tradition)"],
    ["10", "第二个说话人担心自己的孩子不好好地做作业。", "False (Dialog 10: the child studies in the village and calls when stuck)"]],
    title="Presentation Activities Review, Activity 2A: True or False (dialogs are audio)")
D1 = dlg([("A", "我经常听说什么外卖平台、短租平台，还有网约车平台。这些平台都是做什么用的？", "Dialog 1 (scripts; translations mine). A: I often hear about takeout platforms, short-term rental platforms and ride-hailing platforms. What are these platforms for?"), ("B", "它们都是在网上提供服务的应用软件。把它们下载下来，就可以订外卖，订民宿，或是预约叫车。", "B: They are all apps that provide services online. Download them and you can order takeout, book a homestay, or reserve a ride.")])
D2 = dlg([("A", "咱们能知道外卖小哥什么时候把菜送到吗？", "Dialog 2. A: Can we know when the delivery man will bring the food?"), ("B", "能啊。看，这里是定位服务，随时告诉你外卖小哥走到哪里了。“滴滴出行”也有这个服务，你不是用过吗？", "B: Yes. Look, this is the location service, which tells you at any time where the delivery man has got to. DiDi Chuxing has this service too; haven’t you used it?")])
D3 = dlg([("A", "现在有公费留学，也有自费留学。在国外上学的有小学生、中学生、大学生，还有研究生。那么多人都能出国留学，为什么我不能呢？", "Dialog 3. A: Now there is study abroad at public expense and at one’s own expense. Those studying abroad include primary, middle and university students, and graduate students. So many people can study abroad; why can’t I?"), ("B", "快七十岁了，你还留什么学呀！下个月出国旅游吧，这次咱们去欧洲。你想参加旅行团呢，还是来一次自由行？", "B: You’re nearly seventy; what study abroad are you talking about! Let’s travel abroad next month, this time to Europe. Do you want to join a tour group, or have a free-travel trip?")])
D4 = dlg([("A", "我很快就要毕业了。毕业后我想回国找工作，可是现在“海归”已经没什么优势了，我会不会变成“海待”呀？", "Dialog 4. A: I’m about to graduate. After graduating I want to return home to find a job, but “haigui” no longer have much of an advantage; will I become a “haidai”?"), ("B", "别担心。你的专业好，学习成绩也不错，会找到条件和待遇都不错的工作的。", "B: Don’t worry. Your major is good and your grades are fine; you’ll find a job with good conditions and pay.")])
D5 = dlg([("A", "听说了吗？小马做网络直播成了“网红”，收入可高了。你别当“快递小哥”了，太辛苦，也当个“网红”吧。", "Dialog 5. A: Have you heard? Xiao Ma became an “internet celebrity” doing live streaming, and his income is really high. Stop being a “courier”; it’s too hard. Be an “internet celebrity” too."), ("B", "我虽然每天起早贪黑，风里来雨里去的，可是顾客尊重我，收入也稳定。再说，做网络直播的那么多，变成“网红”的有几个？", "B: Although I work from dawn to night every day in wind and rain, customers respect me and my income is stable. Besides, so many people do live streaming; how many become “internet celebrities”?")])
D6 = dlg([("A", "我儿子从小就喜欢玩儿电子游戏。我担心他不好好学习，将来找不到好工作。", "Dialog 6. A: My son has loved playing video games since he was small. I worry he won’t study well and won’t find a good job in the future."), ("B", "现在有一种专门玩儿电脑游戏的职业，叫电子竞技，玩儿得好的人可以做职业电竞员。你儿子如果玩儿得好，反应快，应该去试一试。", "B: Now there is a profession devoted to playing computer games, called e-sports, and those who play well can become professional e-sports players. If your son plays well and reacts fast, he should give it a try.")])
D7 = dlg([("A", "你注意到没有？现在不少的孩子的英语都很棒，能看英语书和英语电影。咱们呢，进大学以前连ＡＢＣ都不认识。", "Dialog 7. A: Have you noticed? Quite a few children now have very good English and can read English books and watch English films. As for us, before entering university we didn’t even know our ABC."), ("B", "那是。他们这一代学习条件太好了，从小就上英语课，还总是上网看国外的东西，英语比咱们好多了。", "B: That’s true. Their generation has such good learning conditions; they take English classes from childhood and also always look at foreign things online, so their English is much better than ours.")])
D8 = dlg([("A", "那位九零后企业家，有那么多好想法，还懂技术，会管理，他的公司一定会越做越好。", "Dialog 8. A: That entrepreneur born in the 1990s has so many good ideas, understands technology and can manage; his company will certainly do better and better."), ("B", "可不。九零后和零零后在信息发达的环境里长大，知道得多，能力也强。另外，他们的目标也高，将来一定大有前途。", "B: Exactly. People born in the 1990s and 2000s grew up in an environment of advanced information, know a lot and are capable. Also, their goals are high, and they will certainly have a bright future. (the book writes 90 后 and 00 后 with digits)")])
D9 = dlg([("A", "很多中国家长花很多钱，送孩子去参加各种兴趣班，有的甚至买特别贵的学区房，就为了让孩子上个好学校。为什么？", "Dialog 9. A: Many Chinese parents spend a lot of money sending their children to all kinds of interest classes, and some even buy very expensive homes in school districts, just so the child can attend a good school. Why?"), ("B", "重视教育是中国人的传统。家长这么做，是为了让孩子受到很好的教育，将来有一个更好的前途。", "B: Valuing education is a tradition of the Chinese people. Parents do this so that their children get a very good education and have a better future.")])
D10 = dlg([("A", "你们在北京打工这么辛苦，孩子又来不了，那他们的教育怎么办？", "Dialog 10. A: You work so hard in Beijing and the child can’t come; what about their education?"), ("B", "孩子一直在农村老家上学，学校的教学质量还不是很高。有时候作业不会做，就打电话过来问我或她爸。", "B: The child has always gone to school in the rural hometown, and the school’s teaching quality isn’t very high. Sometimes when she can’t do her homework she calls me or her dad to ask.")])
L2 = lesson(
    "Lesson 30 Presentation Activities Review: true or false and ten dialog scripts",
    "三个平台 · 定位服务 · 公费留学 · 海归和海待 · 网红 · 电竞员 · 九零后 · 学区房 · 打工的父母",
    requires=[],
    cards=[
        card("Presentation Activities Review, Activity 2 (Listening, Writing, Speaking, and Reading)",
             "A. Listen to several short dialogs and mark the following statements as either True or False. B. Pair up to discuss your answers and explain your reasoning. Go over the scripts below to check your answers. (The audio is not included; my True/False key is worked out from the scripts.)",
             tables=[TF], examples=D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8 + D9 + D10),
    ],
    exercises=[
        M("What are the three kinds of platform in Dialog 1 for?", "Ordering takeout, booking homestays and reserving rides", ["Booking flights", "Paying bills", "Learning English"], "订外卖，订民宿，或是预约叫车."),
        M("What do both the takeout platform and DiDi have, per Dialog 2?", "A location service", ["Free food", "Free rides", "A map game"], "定位服务."),
        M("What does B suggest to A in Dialog 3?", "Travel to Europe next month", ["Study abroad", "Stay at home", "Go to a museum"], "下个月出国旅游吧，这次咱们去欧洲."),
        M("What is A afraid of in Dialog 4?", "Becoming a “haidai”", ["Failing the exam", "Having no passport", "Marrying early"], "我会不会变成“海待”呀？"),
        M("Why does B decline to become an internet celebrity in Dialog 5?", "Customers respect him, his income is stable, and few succeed", ["He hates cameras", "He has no phone", "He is too old"], "顾客尊重我，收入也稳定."),
        M("What does B tell A about e-sports in Dialog 6?", "It is a profession; if the son plays well and reacts fast he should try", ["It is bad for eyes", "It is illegal", "It is only for adults"], "应该去试一试."),
        M("What did the speakers not know before university in Dialog 7?", "Their ABC", ["Math", "Chinese", "History"], "进大学以前连ＡＢＣ都不认识."),
        M("What are the nineties-born and 2000s-born generations like, per Dialog 8?", "They know a lot and are capable, with high goals", ["Lazy", "Shy", "Uneducated"], "知道得多，能力也强……目标也高."),
        M("What explains Chinese parents’ spending on education, per Dialog 9?", "Valuing education is a tradition", ["A government rule", "Bad schools", "Boredom"], "重视教育是中国人的传统."),
        M("What happens when the child in Dialog 10 can’t do homework?", "She phones her mother or father", ["She skips it", "She asks a neighbor", "She goes to the city"], "就打电话过来问我或她爸."),
        F("快七十岁了，你还留什么学___！", "呀", ["吗", "的", "了"], "呀: a particle of exclamation."),
        F("你的专业好，学习成绩也不错，会找到条件和待___都不错的工作的。", "遇", ["过", "里", "钱"], "待遇: treatment, pay."),
        F("重视教育是中国人的传___。", "统", ["说", "话", "人"], "传统: tradition."),
    ],
)

# ------------------------------------------------------------------ 3. activity 3 matching
KEY = table(["Column A", "Column B", "My key"], [["1. 现在国际航线比以前多了不少，机票也越来越便宜，", "g. 所以出国旅游的人越来越多。", "1-g"], ["2. 小宋每天忙着做快递，过春节也没见到他。", "a. 可不是嘛，越是过节他越忙，一天从早到晚就跟打仗似的。", "2-a"], ["3. 于新说她总上网聊天，也没看见她上班。她在做什么呀？", "f. 她现在是“网红”，可有名了。随着粉丝的增加，收入比以前当护士的时候多多了。", "3-f"], ["4. 那里学校的学费太贵了，", "k. 农民工的孩子上不起，他们只好留在老家当“留守儿童”。", "4-k"], ["5. 你注意到没有，现在的孩子比过去文明多了，", "c. 该排队就排队，不喜欢加塞儿。", "5-c"], ["6. 这个手机软件最好的地方，", "h. 是“一键完成”，还可以看到用户评价。", "6-h"], ["7. 你工作很辛苦，机票又这么贵，还要去美国啊？", "j. 得去陪陪孩子。我怕她一个人在那儿压力太大，不适应。", "7-j"], ["8. 现在，我静下心来想了想，", "d. 开始理解为什么你不送孩子去很贵的学校了。", "8-d"], ["9. 不管去哪里旅游，除了“扫货”以外，", "l. 她还喜欢拍很多照片。", "9-l"], ["10. “外卖小哥”什么都送，", "e. 连蔬菜或药都可以给你送到家。", "10-e"], ["11. 他们可以根据乘客的需要，提供特别的服务吗？", "b. 他们还提供大件行李和宠物服务。", "11-b"], ["12. 我们送孩子来少年宫参加画画班，", "i. 就是要培养他的各种兴趣，希望对他将来的发展有好处。", "12-i"]], title="Presentation Activities Review, Activity 3A: matching Column A with Column B (the book prints 加塞尔 and 农名工, read here as 加塞儿 and 农民工)")
M1 = [("现在国际航线比以前多了不少，机票也越来越便宜，所以出国旅游的人越来越多。", "Activity 3A, 1-g (my matched sentences; translations mine): Now there are quite a few more international routes than before and air tickets are getting cheaper, so more and more people travel abroad."),
      ("于新说她总上网聊天，也没看见她上班。", "3 (first part): Yu Xin says she is always chatting online and I haven’t seen her go to work."),
      ("那里学校的学费太贵了，农民工的孩子上不起，他们只好留在老家当“留守儿童”。", "4-k: The tuition at schools there is too expensive; migrant workers’ children can’t afford it, so they have to stay in the hometown as “left-behind children.”"),
      ("你注意到没有，现在的孩子比过去文明多了，该排队就排队，不喜欢加塞儿。", "5-c: Have you noticed that today’s children are much more civilized than in the past? They queue when they should and don’t like to cut in line."),
      ("这个手机软件最好的地方，是“一键完成”，还可以看到用户评价。", "6-h: The best thing about this phone app is that it is “one-click,” and you can also see user reviews."),
      ("现在，我静下心来想了想，开始理解为什么你不送孩子去很贵的学校了。", "8-d: Now that I have calmed down and thought about it, I am starting to understand why you don’t send your child to a very expensive school."),
      ("不管去哪里旅游，除了“扫货”以外，她还喜欢拍很多照片。", "9-l: Wherever she travels, besides shopping sprees she also likes to take lots of photos."),
      ("“外卖小哥”什么都送，连蔬菜或药都可以给你送到家。", "10-e: Delivery men deliver everything, even vegetables or medicine can be brought to your home."),
      ("我们送孩子来少年宫参加画画班，就是要培养他的各种兴趣，希望对他将来的发展有好处。", "12-i: We send our child to the Children’s Palace for the painting class precisely to cultivate his various interests, hoping it will benefit his future development.")]
MD = [dlg([("A", "小宋每天忙着做快递，过春节也没见到他。", "Activity 3A, 2-a (as a short dialog; translations mine). A: Xiao Song is busy delivering packages every day; I didn’t even see him at Spring Festival."), ("B", "可不是嘛，越是过节他越忙，一天从早到晚就跟打仗似的。", "B: Exactly; the more of a holiday it is, the busier he is, and from morning till night each day it’s just like a battle.")]),
      dlg([("A", "你工作很辛苦，机票又这么贵，还要去美国啊？", "7-j. A: Your work is hard and the air ticket is so expensive; are you still going to America?"), ("B", "得去陪陪孩子。我怕她一个人在那儿压力太大，不适应。", "B: I have to go keep the child company. I’m afraid she’ll be under too much pressure there alone and not adapt.")]),
      dlg([("A", "他们可以根据乘客的需要，提供特别的服务吗？", "11-b. A: Can they provide special services according to passengers’ needs?"), ("B", "他们还提供大件行李和宠物服务。", "B: They also provide services for large luggage and pets.")]),
      dlg([("A", "于新说她总上网聊天，也没看见她上班。她在做什么呀？", "3-f. A: Yu Xin says she is always chatting online and I haven’t seen her go to work. What is she doing?"), ("B", "她现在是“网红”，可有名了。随着粉丝的增加，收入比以前当护士的时候多多了。", "B: She’s an “internet celebrity” now and quite famous. As her fans increase, her income is much more than when she was a nurse.")])]
L3 = lesson(
    "Lesson 30 Presentation Activities Review: matching Column A with Column B",
    "国际航线 · 过节越忙 · 网红 · 留守儿童 · 不加塞儿 · 一键完成 · 陪读 · 大件行李 · 培养兴趣",
    requires=[],
    cards=[
        card("Presentation Activities Review, Activity 3 (Reading and Speaking)", "A. Match the parts in Column A with those in Column B by writing the letter in the leftmost column. B. Check your answers with a partner. Take turns translating the sentences into English. The book gives no key; the matching below is mine.", tables=[KEY], examples=[D(z, e) for z, e in M1] + [x for dd in MD for x in dd]),
    ],
    exercises=[
        M("Which ending goes with “现在国际航线比以前多了不少，机票也越来越便宜，”?", "所以出国旅游的人越来越多", ["连蔬菜或药都可以给你送到家", "她还喜欢拍很多照片", "不喜欢加塞儿"], "1-g."),
        M("Which ending goes with “小宋每天忙着做快递，过春节也没见到他。”?", "越是过节他越忙，跟打仗似的", ["所以出国旅游的人越来越多", "她现在是“网红”", "是“一键完成”"], "2-a."),
        M("Which ending goes with “他们可以根据乘客的需要，提供特别的服务吗？”?", "他们还提供大件行李和宠物服务", ["该排队就排队", "得去陪陪孩子", "连蔬菜都送"], "11-b."),
        M("Which ending goes with “那里学校的学费太贵了，”?", "农民工的孩子上不起，他们只好留在老家", ["她还喜欢拍很多照片", "收入比以前多多了", "不适应"], "4-k."),
        M("Which ending goes with “这个手机软件最好的地方，”?", "是“一键完成”，还可以看到用户评价", ["是“网红”", "是排队", "是宠物服务"], "6-h."),
        M("Which ending goes with “我们送孩子来少年宫参加画画班，”?", "就是要培养他的各种兴趣", ["连蔬菜都送", "不用上班", "得去陪陪孩子"], "12-i."),
        F("现在的孩子比过去文___多了，该排队就排队，不喜欢加塞儿。", "明", ["化", "学", "字"], "文明: civilized."),
        F("“外卖小哥”什么都送，连蔬菜或药都可以给你送到___。", "家", ["门", "房", "店"], "送到家: deliver to home."),
        F("她现在是“网红”，可有___了。", "名", ["钱", "力", "用"], "有名: famous."),
    ],
)

UNIT = unit("第三十课 复习课 Unit 5 Review: 课文活动复习", [L1, L2, L3])
