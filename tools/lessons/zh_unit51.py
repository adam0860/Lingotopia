"""Unit 51: Lesson 18 (Unit 3 review) activities, part 1: learning objectives and vocabulary review, presentation activities review,
and grammar and usage review (two lessons). Everything readable in the book is here; the audio activities, the pictures, the board game
and the videos are not. Where the book leaves a table, a cloze blank or a translation open, the answers are mine and labeled."""
from zh_auto import *

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("长大", 0, "zhang3"), ("得睡", 0, "de5"), ("得去", 0, "dei3"), ("得办", 0, "dei3"), ("得多", 0, "dei3"), ("得先", 0, "dei3"), ("睡觉", 1, "jiao4"), ("睡着", 1, "zhao2"), ("睡不着", 2, "zhao2"), ("没有", 0, "mei2"), ("没见", 0, "mei2"), ("没去", 0, "mei2"), ("没看", 0, "mei2"), ("没吃", 0, "mei2"),
                          ("都会", 0, "dou1"), ("教练", 0, "jiao4"), ("还得", 1, "dei3"), ("看得清", 1, "de5"), ("办得", 1, "de5"), ("中了", 0, "zhong4"), ("参加", 0, "can1"), ("觉也不", 0, "jiao4"), ("教别人", 0, "jiao1"), ("越长越", 1, "zhang3"), ("长着", 0, "zhang3"), ("两只", 1, "zhi1")):
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

# ------------------------------------------------------------------ 1. objectives + vocabulary review
SOP = table(["", "登机手续", "安检手续", "入关手续"],
            [["护照", "出示", "出示", "出示，检查，到期"], ["登机牌", "拿登机牌，换座位", "出示", "无"], ["行李", "托运行李，称，行李牌，随身行李", "随身行李，检查", "报关"], ["座位", "靠窗户，靠走道", "无", "无"], ["物品", "无", "药品，食品", "药品，食品，报关"], ["其他", "排队", "排队", "签证，填表，照相，排队"]],
            title="Activity 1: the words sorted into the three procedures (my sorting; the book leaves the table blank and says words may be used in more than one)", say=[0, 1, 2, 3])
SOPL = [("先出示护照和机票，然后托运行李，最后拿登机牌。", "First show your passport and ticket, then check your luggage, and finally get your boarding pass. (a 3-step check-in SOP, mine)"), ("先排队，然后把随身行李放在机器上检查，最后拿好您的护照和登机牌。", "First line up, then put your carry-on luggage on the machine to be checked, and finally take your passport and boarding pass. (security SOP, mine)"),
        ("先填表，然后排队出示护照和签证，最后去报关。", "First fill in the form, then line up to show your passport and visa, and finally go declare at customs. (entry SOP, mine)")]
CHARS = [("迷", "球迷, 歌迷, 影迷, 戏迷, 足球迷, 摇滚迷, 网迷"), ("会", "聚会, 音乐会, 会员, 开会, 一会儿, 演唱会, 机会"), ("厅", "客厅, 饭厅, 舞厅, 歌厅, 音乐厅, 大厅"), ("球", "足球, 篮球, 乒乓球, 打球, 踢球, 球赛, 球星, 球迷, 棒球")]
CARDS = ["在体育馆打乒乓球", "去外地/国外旅游", "去公园划船", "上网打游戏", "去滑雪场滑雪", "去音乐厅听音乐会", "去滑冰场滑冰", "去舞厅跳舞", "在跑步机上跑步", "在家看肥皂剧", "在体育场看球赛", "去健身房上瑜伽课", "去国家公园露营", "去游泳池游泳", "去海边冲浪", "在宿舍弹吉他", "在公园烤肉", "去长城爬山"]
V3 = [("旅客在登机前不但要经过安全检查，甚至有些旅客的随身行李还要打开检查。", "1. Before boarding, passengers not only have to go through a security check; even the carry-on luggage of some passengers has to be opened and checked."), ("到国外旅游的乘客在海关需要办理出关手续。外国游客到中国来旅游需要办理入关手续。", "2. Passengers traveling abroad need to go through exit procedures at customs. Foreign tourists coming to China need to go through entry procedures."),
      ("出国旅行，一个旅客可以托运两件行李，但最重不能超过五十公斤，所以上飞机前最好在家先称一称。", "3. When traveling abroad a passenger may check two pieces of luggage, but the heaviest cannot exceed fifty kilograms, so it’s best to weigh them at home before boarding."), ("我们学校的棒球队每个月要参加一次比赛，所以下课后，球员们要参加两个小时的训练。", "4. Our school’s baseball team takes part in a game once a month, so after class the players have two hours of training."),
      ("从四月十九日起旧金山有一个国际电影节，那个星期，天天都有很多人在电影院门口排队买票。", "5. From April 19 there is an international film festival in San Francisco; that week, every day many people lined up outside the movie theaters to buy tickets.")]
RETIRE = ("老王工作了三十年，下个月就要退休了。他的太太想帮他办一个聚会，邀请了一些朋友参加。其中多半是住在附近的朋友和同事。不过有一个朋友很特别。他是老王的同学李力。李力说已经二十多年没见到老王了，机会难得，特地坐飞机从中国来恭喜他。老王和他太太去机场接他。等了半天没见到他，原来李力变胖了，老王简直就认不出来了。后来还是李力先认出老王才见到面的。离开机场后，老王先带老李到三藩市的几个景点参观。"
          "这是李力第一次来三藩市，很多地方对他来说都很新鲜，所以他很兴奋。他们看了渔人码头、金门大桥、和中国城。老王看到海边和公园到处都是人。这些人不是来游览的游客就是在做运动的当地人。有的在跑步，有的在踢球，还有的在骑自行车。大家都非常开心。逛了三个小时以后，他们开车回家。因为李力已经超过十四个小时没休息了，所以一到老王家，他就在沙发上睡着了。")
RETIRE_E = ("Lao Wang has worked for thirty years and will retire next month. His wife wanted to throw him a party and invited some friends to attend, most of them friends and colleagues who live nearby. But one friend was special: Li Li, Lao Wang’s classmate. Li Li said he had not seen Lao Wang for more than twenty years, and since such an opportunity is rare, he made a special trip by plane from China to congratulate him. Lao Wang and his wife went to the airport to pick him up. They waited a long time without seeing him; it turned out Li Li had gotten fatter, and Lao Wang simply couldn’t recognize him. In the end Li Li recognized Lao Wang first and they met. After leaving the airport, Lao Wang first took Lao Li to visit a few sights in San Francisco. "
            "It was Li Li’s first time in San Francisco and many places were fresh to him, so he was very excited. They saw Fisherman’s Wharf, the Golden Gate Bridge and Chinatown. Lao Wang saw that the seaside and the park were full of people everywhere. These people were either tourists out sightseeing or locals exercising. Some were jogging, some were playing soccer and some were riding bikes. Everyone was very happy. After strolling for three hours they drove home. Because Li Li had been without rest for more than fourteen hours, as soon as he got to Lao Wang’s home he fell asleep on the sofa. (The blanks are filled with the words in the box; the filled-in words are mine, and the book writes the number of years as a digit.)")
SUMMARY = [("老王退休前，他的老同学李力特地从中国飞来参加他的退休聚会，老王带他参观了旧金山。", "Before Lao Wang’s retirement his old classmate Li Li flew in specially from China to attend his retirement party, and Lao Wang showed him around San Francisco. (one-sentence summary, mine)")]
MUSIC = table(["Category", "Words from the word pool"],
              [["音乐种类", "流行音乐，交响乐，摇滚乐，京剧，音乐剧"], ["表演的地方", "音乐厅，舞厅"], ["乐队/乐团", "合唱团，主唱，贝斯手，鼓手，吉他手，键盘手，粉丝"], ["乐器", "吉他，钢琴，鼓，键盘"], ["听音乐的方式", "光盘，下载音乐，看/听视频"], ["表演方式", "音乐会，演唱会，唱歌，跳舞"]],
              title="Activity 5: the Lesson 16 music words sorted (my sorting; the book leaves the diagram blank)", say=[0, 1])
L1 = lesson(
    "Lesson 18 (Unit 3 review): objectives and vocabulary review",
    "第十八课 复习课 · 登机/安检/入关手续 · 迷会厅球 · 老王的退休聚会 · 音乐词汇",
    requires=[],
    cards=[
        card("第十八课 复习课: Unit 3 Review (objectives)",
             "This lesson is designed to help you consolidate what you have learned in Lessons 13 to 17 via comprehensive reviews, enhancement practice, skill-building activities and real-life applications. When you have completed it, you will be able to: better understand conversations between speakers of Chinese as well as short written passages containing basic information on the following topics: At an airport; Leisure Travel; Social Gatherings; Recreational Activities; Sports and Fitness. Become more familiar with the linguistic and non-linguistic features directly related to these topics, such as core vocabulary and patterns, grammar, appropriate social terms and embedded cultural knowledge. Use these language features to complete a variety of language exercises and conduct various communication activities."),
        card("Vocabulary Review, Activity 1: airport procedures",
             "A. Write the vocabulary terms listed below in the correct category in the table (some vocabulary may be used in more than one category): 护照, 换座位, 托运行李, 签证, 随身行李, 药品, 食品, 登机牌, 靠窗户, 靠走道, 照相, 检查, 出示, 到期, 填表, 排队, 报关, 称, 行李牌, and the three headings 登机手续, 安检手续, 入关手续. B. Your group volunteers in the local airport to assist Chinese tourists with check-in. In groups of three: 1. Each student selects one check-in procedure and orders the terms into sequential steps (you can add other learned vocabulary). 2. Practice giving verbal instructions to help Chinese tourists complete the procedure; be sure to use 先…然后…最后…. 3. Create a 3–4 step SOP (Standard Operating Procedure) in Chinese and post it online. C. The whole class votes for the best SOP. My sample SOPs (mine):",
             tables=[SOP], examples=[D(z, e) for z, e in SOPL]),
        card("Activity 2: characters and index cards",
             "A. Form groups of three. Your teacher shows one character at a time from the table: 迷, 会, 厅, 球. Each group comes up with as many vocabulary words or phrases that contain the character within a time limit; the team that writes the most wins. B. Each student gets a set of index cards with phrases that contain a location and a hobby and paraphrases what is on the card without giving away the location or the hobby; the other group members guess. The cards: " + "，".join(CARDS) + "。 C. Each group incorporates at least five different phrases and grammar patterns to create a story about their “last long weekend” (故事接龙), and reports it to the class or uploads a recording. The suggested grammar points: resultative complement 完、到、好; potential complement 得; A 离 B…; 又/再; 次/遍; 要是…; 虽然…但是; 不是…就是; 越…越; duration 了; double 了; 让; 甚至; 不管; 给. My words for the four characters (mine):",
             tables=[table(["Character", "Words (mine)"], [[c, w] for c, w in CHARS], title="迷 会 厅 球", say=[0, 1])]),
        card("Activity 3: long sentences",
             "A. Listen to and translate five sentences (audio, not included). B. Analyze these long sentences: highlight the subject, verb (or verb phrase) and object in each sentence; then translate each sentence and check with your partner. The book leaves the translations blank; mine follow (the book writes 50 公斤 and 4 月 19 日 as digits):",
             examples=[D(z, e) for z, e in V3]),
        card("Activity 4: Lao Wang’s retirement party",
             "A. Read the passage and use the linguistic and contextual clues to complete the sentences with the words in the box: 退休, 超过, 兴奋, 对…来说, 到处, 机会, 参观, 参加, 简直, 恭喜, 附近, 原来. B. Pair up and read the entire passage aloud to check your answers; discuss what strategies you used. C. Write a one-sentence summary of the story. The completed passage and my summary:",
             examples=[D(RETIRE, RETIRE_E)] + [D(z, e) for z, e in SUMMARY]),
        card("Activities 5 and 6",
             "Activity 5. A. Below are words you learned in Lesson 16 presentations and from other sections in the lesson. Use the diagram to place each word in the correct category: 合唱团, 吉他, 流行音乐, 主唱, 音乐会, 光盘, 贝斯手, 交响乐, 演唱会, 鼓手, 吉他手, 键盘手, 钢琴, 鼓, 摇滚乐, 下载音乐, 看/听视频, 粉丝, 音乐厅, 舞厅, 唱歌, 跳舞, 音乐剧, 京剧, 键盘. The diagram’s categories are 音乐种类, 表演的地方, 乐队/乐团, 乐器, 听音乐的方式 and 表演方式. B. Pair up and take turns creating sentences using at least two words from the diagram; your partner translates. Activity 6 (Board game). Create groups of three; each member rolls the dice, moves to the space indicated and answers the question in that space in a complete sentence; on a dark blue space you may choose any topic, and on an orange space your partner chooses. (The board is a picture, so it is not included.)",
             tables=[MUSIC]),
    ],
    exercises=[
        M("In which procedure do you 托运行李?", "登机手续 (check-in)", ["安检手续", "入关手续", "None of them"], "托运行李 belongs to check-in."),
        M("In which procedure do you 填表 and 报关?", "入关手续 (entering the country)", ["登机手续", "安检手续", "None of them"], "Entry procedures include forms and customs."),
        M("What pattern should the SOP steps use?", "先…然后…最后…", ["不管…都…", "虽然…但是…", "越…越…"], "先…然后…最后… (first, then, finally)."),
        M("Which word fits 球迷, 歌迷, 影迷?", "迷", ["会", "厅", "球"], "迷 = fan."),
        M("What does 老王 do next month?", "Retires", ["Moves to China", "Starts a business", "Goes to a hospital"], "下个月就要退休了."),
        M("Who is Li Li?", "Lao Wang’s old classmate who flew in from China", ["Lao Wang’s son", "A tour guide", "A neighbor"], "他是老王的同学李力."),
        M("Why couldn’t Lao Wang recognize him at first?", "Li Li had gotten fatter", ["Li Li wore a mask", "Li Li was in another airport", "It was too dark"], "原来李力变胖了."),
        M("Where did Lao Wang take Li Li?", "Fisherman’s Wharf, the Golden Gate Bridge and Chinatown", ["Disneyland", "Las Vegas", "Beijing"], "渔人码头、金门大桥、和中国城."),
        M("What had Li Li not done for more than fourteen hours?", "Rest", ["Eat", "Drive", "Talk"], "已经超过十四个小时没休息了."),
        M("Which is a musical instrument?", "钢琴", ["音乐厅", "粉丝", "光盘"], "钢琴 is a piano."),
        M("Which is a place to perform?", "舞厅", ["键盘手", "流行音乐", "鼓"], "舞厅 is a dance hall."),
        M("What does 旅客在登机前不但要经过安全检查，甚至…还要打开检查 mean?", "Even the carry-on luggage of some passengers has to be opened", ["No one is checked", "All luggage is lost", "Passengers board first"], "甚至 intensifies the example."),
        F("到国外旅游的乘客在海关需要办理出关___续。", "手", PART, "手续: procedure."),
        F("李力说已经二十多年没见到老王了，机会___得。", "难", PART, "难得: rare."),
        F("老王看到海边和公园___处都是人。", "到", PART, "到处: everywhere."),
    ],
)

# ------------------------------------------------------------------ 2. presentation activities review
PA15 = [("换座位之前，请让我看一下您的机票和登机牌。", "1. Please show me your ticket and boarding pass before I change your seat. (换，之前，让; Chinese answers are mine)"), ("让我先称一下您的行李。托运完行李以后，您需要到那边过安检。", "2. Let me weigh your luggage first. After checking in your luggage, you need to go through the security check over there. (先，以后，需要)"), ("您的护照六个月以后到期。您有什么东西需要报关吗？", "3. Your passport will expire in six months. Do you have anything to declare? (到期，报关)"),
        ("我误了飞机，因为我到了机场才知道机场这么忙。", "4. I missed the plane because I didn’t know the airport was so busy until I arrived there. (误机，因为，到了…才…)"), ("你去过南京吗？没去过的话，最好去看看。那儿有很多名胜古迹。", "5. Have you ever been to Nanjing? If you haven’t, you’d better go and see it. There are a lot of famous tourist attractions there. (去过…，最好，名胜古迹)"), ("我在蒙特雷已经住了快两年了，可是这是我第一次来参观水族馆。", "6. I have been living in Monterey for almost two years, but this is my first visit to the aquarium. (…了…了，次，参观)"),
        ("我们在老王的新家聚会。这儿很热闹，请你也来参加。你十二点以前来得了吗？", "7. We are having a party at Lao Wang’s new home. It’s a lot of fun here, so please come and join us. Will you be able to come before twelve? (热闹，参加，来得了)"), ("我跟你说了什么也不用带。好吧，这里有饮料和零食，你们喜欢什么就吃什么。", "8. I told you not to bring anything. OK, here are some drinks and snacks; help yourselves to whatever you like. (什么也…，什么…什么…)"),
        ("有的人在烤肉，有的人坐在长椅上聊天，有的人在草地上踢足球。", "9. Some are barbecuing, some are sitting on a bench and chatting, and some are playing soccer on the grass. (有的…有的…，在+verb)"), ("我从来没有在网上跟别人玩过游戏。我一个星期只玩两个小时，一个人玩，因为我不想让自己上瘾。", "10. I have never played games online against other people. I only play two hours a week, by myself, because I don’t want to become addicted. (从来没…，因为，让，上瘾)"),
        ("我空闲的时候喜欢唱歌，我还参加了一个合唱团。我们合唱团每个星期练习一次。要是你感兴趣，也可以参加我们。", "11. I like to sing when I have free time, and I’ve also joined a choir. Our choir practices once a week. If you are interested, you can also join us. (空闲，参加，次，要是，感兴趣)"), ("虽然我喜欢看恐怖片，但是我很少一个人看，因为我会害怕得晚上几乎睡不着觉。", "12. Although I like to watch horror movies, I seldom watch them alone because I would become so scared that I can hardly sleep at night. (虽然…但是…，很少，因为，害怕)"),
        ("你可以买一个跑步机在家锻炼，或是来我们的健身房用我们的。我还是觉得你需要一个教练帮你制定一个锻炼计划。", "13. You can buy a treadmill to work out at home or come to the gym to use ours. I still think you need a coach to help you make an exercise plan. (或是，还是，制定)"), ("我不但喜欢滑雪，而且喜欢教别人滑雪。我从小学起就开始滑雪了。", "14. Not only do I like to ski, I also like to teach other people to ski. I started skiing when I was in elementary school. (不但…而且…，别人，从…起)"),
        ("要是他最喜欢的美国篮球队在中国时间半夜有比赛，不管第二天要不要上班，他都会熬夜看球赛。", "15. If his favorite American basketball team plays a game in the middle of the night in China time, he will stay up late to watch the game even if he needs to go to work the next day. (半夜，不管…都…，熬夜)")]
MATCH = [("请问，出国旅游需要办什么手续？", "你得办护照和签证。", "1 – c"), ("让我看一下您的登机牌好吗？", "好的。能不能给我换成靠窗的座位？", "2 – d"), ("您准备在蒙特雷住多长时间？", "差不多三个月，然后去纽约看儿子。", "3 – a"), ("你怎么会误了航班呢？", "谁知道过安检花了那么长时间啊！", "4 – f"), ("坐飞机从上海去纽约需要多长时间？", "上次我花了差不多十五个小时。", "5 – h"),
         ("从车站到公园只要十分钟，你怎么开了这么久？", "路上太堵了，我想开快也开不快呀。", "6 – e"), ("今天这儿怎么到处都是人？", "现在哪个名胜古迹都有很多人。", "7 – b"), ("你开车开了四五个小时了，累了吧？", "还好，再过二十多分钟就到机场了。", "8 – g")]
SCRIPT = [("李", "王老师，谢谢邀请大家来你这儿聚会。你做的菜太好吃了！", "Teacher Wang, thank you for inviting everyone to your place for the party. The food you made is so delicious!"), ("王", "哪里哪里，李老师。马上就要过年了，大家在一起热闹热闹。哎，这是你们合唱团的照片吧？好漂亮啊！你在这儿，后边这位是你先生，对不对？", "Not at all, Teacher Li. The New Year is coming soon, so let’s have fun together. Hey, is this a photo of your choir? So beautiful! You’re here, and the one behind is your husband, right? (the book’s layout is garbled here; the speakers follow the sense)"),
          ("李", "对。我们合唱团差不多每个周末都活动。除了唱歌，我们也跳舞。", "Right. Our choir meets almost every weekend. Besides singing we also dance."), ("王", "上次你们演出，一个女生唱《我爱你中国》唱得太好了。", "At your last performance a girl sang “I Love You, China” so well."), ("李", "对，她是我们班上的学生。我们那次演出还上了电视呢。", "Yes, she’s a student in our class. Our performance even was on TV."),
          ("王", "真棒！我有空儿的时候，不是在微信上看东西，就是上网玩儿游戏，很少活动，身体经常不舒服。看来得多参加活动。", "Great! When I have free time I’m either looking at things on WeChat or playing games online and seldom move, and my body often feels unwell. It seems I should take part in more activities."), ("李", "我听你弹过钢琴，弹得非常好，你先生弹吉他也弹得不错。你们参加我们合唱团的乐队吧。", "I’ve heard you play the piano, and you play very well, and your husband plays the guitar quite well too. Join our choir’s band."),
          ("王", "我没问题，可是我先生不一定感兴趣。他只要有时间就看电视，最喜欢看搞笑的。", "I have no problem, but my husband may not be interested. As long as he has time he watches TV, and likes comedy best."), ("李", "哈哈，我也喜欢看电视，不过我最喜欢看的是动画。这样吧，我让我先生给他打个电话，要他一定参加！", "Ha ha, I also like TV, but what I like to watch most is animation. How about this: I’ll have my husband call him and tell him he must join!")]
TF3 = [("王老师搬家了。她请朋友们到她的新家聚了聚。", "1. Teacher Wang moved house. She invited friends to her new home. — False (the script never mentions a move; it is a Chinese New Year gathering; key mine)"), ("王老师和她先生经常参加合唱团的活动。", "2. Teacher Wang and her husband often take part in the choir’s activities. — True (photo and 差不多每个周末都活动)"), ("李老师有一张合唱团的照片。", "3. Teacher Li has a photo of the choir. — False (the photo is at the speaker’s place)"),
       ("王老师的一个美国朋友唱中国歌唱得非常好。", "4. One of Teacher Wang’s American friends sings Chinese songs very well. — False (a female student in the class)"), ("李老师很喜欢上网玩儿游戏。", "5. Teacher Li likes playing online games very much. — False (she does it in her free time but regrets not being active)"), ("王老师的先生可能会给李老师的先生打电话。", "6. Teacher Wang’s husband may call Teacher Li’s husband. — True (让我先生给他打个电话)")]
L2 = lesson(
    "Lesson 18 (Unit 3 review): presentation activities review",
    "十五个翻译句子 · 问答配对 · 合唱团聚会对话 · 家人的运动",
    requires=[],
    cards=[
        card("Activity 1 (Speaking, Writing and Reading): how to say it",
             "Pair up and, in Chinese, tell your partner how to say the following 15 sentences; take turns, using the key words provided. The book gives the English; the Chinese answers below are mine (the key words are in parentheses). The book prints “12:00” as digits.",
             examples=[D(z, e) for z, e in PA15]),
        card("Activity 2 (Reading and Speaking): match the sentences",
             "A. Match the sentences in Column B with those in Column A by writing the letters in the leftmost column (the book leaves the key out; mine follows each pair). B. Pair up, check your work and take turns translating each sentence into English.",
             tables=[table(["Column A", "Column B", "Key (mine)"], [[a, b, k] for a, b, k in MATCH], say=[0, 1])]),
        card("Activity 3 (Listening and Speaking): the choir party",
             "A. Listen to the dialog and mark each statement as True or False (audio, not included; the script is printed below and my answers come from it). B. Pair up and discuss your answers and why you chose them; go over the script to check your work.",
             examples=[D(f"{s}：{z}", e) for s, z, e in SCRIPT] + [D(z, e) for z, e in TF3]),
        card("Activity 4 (Listening, Writing and Speaking)",
             "Listen to the statements and fill in the table in Chinese using the information you heard: for 哥哥, 姐姐, 弟弟 and 我 write 什么运动, 什么时间, 什么地方 and 其他. (Audio and a picture, not included.)"),
    ],
    exercises=[
        M("Which answer matches 请问，出国旅游需要办什么手续？", "你得办护照和签证。", ["差不多三个月。", "路上太堵了。", "上次我花了十五个小时。"], "Passport and visa."),
        M("Which answer matches 你怎么会误了航班呢？", "谁知道过安检花了那么长时间啊！", ["你得办护照。", "还好，再过二十分钟就到。", "现在哪个景点都有人。"], "The security check took so long."),
        M("Which answer matches 今天这儿怎么到处都是人？", "现在哪个名胜古迹都有很多人。", ["上次我花了十五个小时。", "路上太堵了。", "你得办签证。"], "Every sight is crowded now."),
        M("Which answer matches 你开车开了四五个小时了，累了吧？", "还好，再过二十多分钟就到机场了。", ["差不多三个月。", "好的，换靠窗的。", "你得办护照。"], "Another twenty minutes to the airport."),
        M("What are Teacher Li and Teacher Wang celebrating?", "A get-together before the New Year", ["A birthday", "A wedding", "A graduation"], "马上就要过年了，大家在一起热闹热闹."),
        M("How often does the choir meet?", "Almost every weekend", ["Every day", "Once a year", "Never"], "差不多每个周末都活动."),
        M("What does Teacher Wang do in her free time?", "Looks at WeChat or plays games online", ["Climbs mountains", "Plays sports", "Cooks"], "不是在微信上看东西，就是上网玩儿游戏."),
        M("What does Teacher Wang’s husband like to watch?", "Comedy", ["Horror movies", "News", "Cooking shows"], "最喜欢看搞笑的."),
        M("What will Teacher Li have her husband do?", "Call Teacher Wang’s husband and ask him to join", ["Buy a guitar", "Join the band", "Leave the choir"], "让我先生给他打个电话."),
        M("What is 误机?", "To miss a flight", ["To change a seat", "To check luggage", "To weigh luggage"], "误机 = miss the plane."),
        F("请问，出国旅游需要办什么手___？", "续", PART, "手续: procedures."),
        F("你得___护照和签证。", "办", PART, "办: handle."),
        F("我们合唱团差不多每个周末都活___。", "动", PART, "活动."),
    ],
)

# ------------------------------------------------------------------ 3. grammar review, part 1
G1 = [("我订的是靠窗户的座位。", "1. What I booked is a window seat. (的; key mine)"), ("她的英语说得怎么样？", "2. How well does she speak English? (得)"), ("孩子们学什么都学得很快。", "3. Children learn whatever they study very fast. (得)"), ("考试前她紧张得睡不着觉。", "4. Before the test she was so nervous that she couldn’t sleep. (得)"), ("世界杯的时候，我先生一晚一晚地看球赛，觉也不睡了。", "5. During the World Cup, my husband watched games night after night and didn’t even sleep. (地)"),
      ("聚会的时候，最忙的就是妈妈们了。她们忙得连饭也没时间吃。", "6. At a party, the busiest are the mothers. They are so busy that they don’t even have time to eat. (的, 得)"), ("字太小了，你看得清看不清？", "7. The characters are too small; can you see them clearly or not? (得)"), ("她急得哭了起来。", "8. She got so anxious that she began to cry. (得)"), ("他每天在跑步机上跑一个小时的步，现在他跑得越来越快了。", "9. He runs on the treadmill for an hour every day, and now he runs faster and faster. (的, 得)"),
      ("她开心地笑了。", "10. She smiled happily. (地; or 她开心得笑了, so happy that she laughed)"), ("他高兴地唱起歌来。", "11. He happily began to sing. (地; or 他高兴得唱起歌来, so happy that he started to sing)")]
BIRD = ("小鸟飞到了大树的上面，它高兴地叫起来：“我会飞啦！”小鸟飞到了大山的上空，它又高兴地喊起来：“我真的会飞啦！”")
BIRD_E = ("The little bird flew above the big tree and happily began to cry out, “I can fly!” The bird flew into the sky over the big mountain and happily shouted again, “I really can fly!” (completed with 的/地; mine)")
FOX = ("狐狸在树林里找吃的，他看见乌鸦的嘴里有一块肉。狐狸馋得流口水。他对乌鸦说：“亲爱的乌鸦，你的羽毛真好看！”乌鸦不说话。狐狸又说：“您的孩子们都好吗？”乌鸦还是不说话。狐狸想了想，说：“您的歌唱得好极了！”乌鸦高兴地唱起来，她嘴里的肉掉下来。狐狸叼起肉，飞快地跑了。")
FOX_E = ("The fox was looking for food in the woods when he saw a piece of meat in the crow’s mouth. The fox was so greedy that he drooled. He said to the crow, “Dear Crow, your feathers are so beautiful!” The crow said nothing. The fox said again, “How are your children?” The crow still said nothing. The fox thought for a moment and said, “You sing extremely well!” The crow happily began to sing, and the meat in her mouth fell down. The fox picked up the meat and ran away quickly. (completed with 的/得/地; mine)")
SHEN = [("暑假快到了，你有什么打算？", "1. The summer vacation is coming; what are your plans? (interrogative: what)"), ("你不想说点儿什么吗？", "2. Don’t you want to say something? (indefinite: something)"), ("参加旅行团有什么意思啊？一点儿都不自由。", "3. What’s the point of joining a tour group? There’s no freedom at all. (rhetorical: there’s no point)"), ("聚会以前，我得去买点儿什么。", "4. Before the party I have to go and buy something. (indefinite: something)"), ("我男朋友什么运动都喜欢。", "5. My boyfriend likes every kind of sport. (any/every)"),
        ("放假了！我想什么时候起床就什么时候起床。", "6. It’s vacation! I’ll get up whenever I want. (whatever/whenever: 什么…就什么…)"), ("我对游泳滑雪什么的都很感兴趣。", "7. I’m interested in swimming, skiing and so on. (什么的: etc.)"), ("什么时候到我的新家来玩儿吧。", "8. Come to my new home some time. (什么时候: some time)"), ("马上就要考试了，看什么电影啊？", "9. The exam is coming up soon; why watch a movie? (rhetorical: don’t)")]
SPR = [("天气越来越暖和了。", "The weather is getting warmer and warmer. (越来越)"), ("白天越来越长，晚上越来越短。", "The days are getting longer and the nights shorter."), ("树叶越长越绿，花越开越多。", "The leaves grow greener and greener, and the more the flowers open. (越…越…)"), ("雪越下越少，天气越暖和，小鸟就越来越多了。", "The snow falls less and less; the warmer the weather, the more birds there are.")]
G4 = [("他每天不是打游戏就是睡觉。", "Group 1 不是…就是… — 1. Every day he is either playing games or sleeping."), ("我吃得很简单，不是面条就是米饭。", "2. I eat very simply: it’s either noodles or rice. (mine)"), ("周末我不是去爬山就是去游泳。", "3. On weekends I either go hiking or go swimming. (mine)"),
      ("他虽然每天锻炼，可还是很胖。", "Group 2 虽然…但是/可是… — 1. Although he exercises every day, he is still very fat."), ("加拿大虽然地方大，但是人口不多。", "2. Although Canada is large, its population is not big. (mine)"), ("这个手机虽然很贵，但是质量很好。", "3. Although this phone is expensive, its quality is very good. (mine)"),
      ("天气不好，很多航班因此停飞了。", "Group 3 因此 — 1. The weather was bad, so many flights were canceled as a result."), ("我太太对恐怖片又喜欢又害怕，因此她常常看完以后睡不着觉。", "2. My wife both likes and fears horror movies; therefore she often can’t sleep after watching. (mine)"), ("他每天锻炼身体，因此很少生病。", "3. He exercises every day and therefore rarely gets sick. (mine)"),
      ("要是写不完作业的话，我就睡不着觉。", "Group 4 要是…就… — 1. If I can’t finish my homework, I can’t fall asleep."), ("要是坐地铁，就不会迟到了。", "2. If you take the subway, you won’t be late. (mine)"), ("要是明天不下雨，我们就去爬山。", "3. If it doesn’t rain tomorrow, we’ll go hiking. (mine)"),
      ("你不管穿什么都好看。", "Group 5 不管…都… — 1. No matter what you wear, you look good."), ("不管多忙，他每天都去健身房。", "2. No matter how busy, he goes to the gym every day. (mine)"), ("不管天气怎么样，我们都要去野餐。", "3. No matter what the weather is like, we’ll go on a picnic. (mine)"),
      ("我一直觉得你们有点像，原来他是你弟弟！", "Group 6 原来 (the book numbers it Group 5 again) — 1. I always thought you two looked alike; it turns out he’s your younger brother!"), ("我以前不知道为什么有一个北京，还有一个南京，后来才知道，原来北京在北方，南京在南方。", "2. I didn’t know before why there is a Beijing and also a Nanjing; later I found out that Beijing is in the north and Nanjing in the south. (mine; the book’s sentence is left unfinished)"), ("我找了半天手机，原来它在我的包里。", "3. I looked for my phone for ages; it turns out it was in my bag. (mine)")]
CASH = ("从今年六月起，我就在一家小商店做服务员。后来我发现，离商店不太远的地方有一所社区大学。从我工作的地方开车到那儿只要十五分钟。所以，每天下班以后，我就在附近的快餐店随便吃点儿东西，然后就开车到学校去上课。我每周有四次课，上课的时间是从晚上六点到九点，下课以后再开车回家。每天这样跑来跑去，简直太累了。但是我想，以后我一定能找到更好的工作。")
CASH_E = ("Since this June I have been working as a clerk in a small store. Later I found out that not far from the store there is a community college. It is only fifteen minutes by car from where I work to there. So every day after work I grab something to eat at a fast-food place nearby, and then I drive to school to attend class. I have class four times a week, from six to nine in the evening, and I drive home after class. Running around like this every day is simply too tiring. But I think that in the future I will certainly find a better job. (The completed story is mine; the book blanks the words 后来, 以后, 然后, 从…到…, 从…起, 到…去… and 离, and glosses 社区大学 and 快餐店 in English.)")
YZ = [("她昨天来晚了，今天又来晚了。", "1. She was late yesterday and was late again today. (又)"), ("王老师不在，你明天再来吧。", "2. Teacher Wang isn’t in; come again tomorrow. (再)"), ("我昨天已经跑过步了，今天不想再跑了。", "3. I already ran yesterday and don’t want to run again today. (再)"), ("太晚了，快睡觉吧。作业明天再做也行。", "4. It’s too late; go to bed. The homework can be done tomorrow. (再)"), ("他下星期又要出差了。", "5. He is going on a business trip again next week. (又)"),
      ("在饭店吃完饭以后，我们又散了半个小时的步才回家。", "6. After eating at the restaurant we also strolled for half an hour before going home. (又)"), ("你等一会儿再走吧，外边正下着雨呢。", "7. Wait a while before you leave; it’s raining outside. (再)")]
L3 = lesson(
    "Lesson 18 (Unit 3 review): grammar and usage review, part 1",
    "的/得/地 · 什么 · 越来越 · 六组句型 · 以后/然后/后来 · 又/再",
    requires=[],
    cards=[
        card("Activity 1 (Writing): 的, 得 or 地",
             "A. Complete the sentences using the possessive marker 的, the degree complement marker 得, or the adverbial modifier marker 地. Compare your work with a classmate. Note: numbers 10 and 11 can be completed in different ways; how do their meanings differ? (Mine: 地 describes the manner, “smiled happily”; 得 gives the result, “so happy that she laughed.”) The book leaves the key out; mine follows (the book’s blanks sit where 的, 得 and 地 are).",
             examples=[D(z, e) for z, e in G1]),
        card("Activity 1, Optional: two stories",
             "B. Optional. Complete the two stories (The Little Bird; The Fox and the Crow) with 的, 得 or 地; the completed texts are mine.",
             examples=[D(BIRD, BIRD_E), D(FOX, FOX_E)]),
        card("Activity 2 (Reading and Speaking): the uses of 什么",
             "Pair up. Read the following sentences and discuss the meanings of the different uses of 什么 with your partner. The book gives no explanations; mine are in the translations.",
             examples=[D(z, e) for z, e in SHEN]),
        card("Activity 3 (Speaking): 越来越/越…越…",
             "In two groups, use 越来越 or 越…越… to describe the changes in nature when winter gives way to spring. The group that comes up with the most ideas wins. (Two photographs, not included.) My sentences (mine):",
             examples=[D(z, e) for z, e in SPR]),
        card("Activity 4 (Writing and Speaking): six groups of patterns",
             "A. For each of the six groups of sentences: 1. Translate the sentence. 2. Complete the sentence. 3. Create your own sentence using the same structure. B. Pair up and share your work with your partner. The patterns are 不是…就是…, 虽然…但是/可是…, 因此, 要是…就…, 不管…都… and 原来 (the book heads the last group 不管…都… by mistake). The first sentence of each group is the book’s; the completions and my own sentences are mine:",
             examples=[D(z, e) for z, e in G4]),
        card("Activity 5 (Writing, Reading, Speaking and Listening): the young cashier",
             "Read the story of a young cashier who wants to advance her studies. Complete the sentences using 以后, 然后, 后来, 从…到…, 从…起, 到…去… and 离. Then pair up and compare your work; discuss any differences. My completed story:",
             examples=[D(CASH, CASH_E)]),
        card("Activity 6 (Reading and Writing): 又 or 再",
             "Use either 又 or 再 to correctly complete the sentences. The key is mine:",
             examples=[D(z, e) for z, e in YZ]),
    ],
    exercises=[
        M("Which marker completes 她的英语说___怎么样？", "得", ["的", "地", "着"], "说得怎么样: degree complement."),
        M("Which marker completes 我订___是靠窗户的座位？", "的", ["得", "地", "了"], "我订的: a nominal phrase."),
        M("Which marker completes 他高兴___唱起歌来？ (happily began to sing)", "地", ["的", "得", "了"], "地: manner."),
        M("What is the difference between 她开心地笑了 and 她开心得笑了?", "地 = laughed happily; 得 = so happy that she laughed", ["No difference", "Past vs. future", "Question vs. statement"], "地 = manner; 得 = result."),
        M("What does 什么 mean in 你不想说点儿什么吗？", "Something (indefinite)", ["What (question)", "Anything", "Nothing"], "Indefinite."),
        M("What does 什么 mean in 参加旅行团有什么意思啊？", "A rhetorical “what’s the point?”", ["A real question", "Something", "Everything"], "Rhetorical."),
        M("What does 我男朋友什么运动都喜欢 mean?", "My boyfriend likes every sport", ["My boyfriend likes no sport", "What sport does he like?", "Something sporty"], "什么…都 = any/every."),
        M("What does 什么的 mean in 游泳滑雪什么的?", "And so on", ["What of it", "Who", "Anything"], "什么的 = etc."),
        M("What does 不管…都… express?", "No matter …, all the same", ["If …, then …", "Although …, but …", "Because …, so …"], "不管…都…"),
        M("Which fits “It turns out he’s your brother!”?", "原来他是你弟弟！", ["后来他是你弟弟！", "然后他是你弟弟！", "因此他是你弟弟！"], "原来 = it turns out."),
        M("Which fits 今天又来晚了 (late again)?", "又", ["再", "才", "就"], "又 for a repeated past action."),
        M("Which fits 明天___来吧 (come again tomorrow)?", "再", ["又", "才", "就"], "再 for a future repeat."),
        F("孩子们学什么都学___很快。", "得", PART, "学得很快."),
        F("考试前她紧张___睡不着觉。", "得", PART, "紧张得…"),
        F("世界杯的时候，我先生一晚一晚___看球赛。", "地", PART, "一晚一晚地."),
        F("每天下班以后，我就在附近的快餐店随便吃点儿东西，___就开车到学校去上课。", "然后", PART, "然后."),
    ],
)

# ------------------------------------------------------------------ 4. grammar review, part 2
TR7 = [("我在蒙特雷住了三年了，去过很多风景美丽的地方，但是我还没去过水族馆。昨天我和朋友去了那里，真的不错！", "1. I have lived in Monterey for three years and have been to many places with beautiful scenery, but I hadn’t been to the aquarium yet. Yesterday I went there with a friend, and it was really good! (translation mine)"),
       ("我直到二十五岁才开始谈恋爱。下个月我要结婚了。我和他是在北京认识的。你会来参加我的婚礼吗？", "2. I didn’t start dating until I was twenty-five. Next month I’m getting married. He and I met in Beijing. Will you come to my wedding?"), ("你等会儿再打电话来吧。我正在和我弟弟打乒乓球呢，我们快打完了。", "3. Call again in a little while. I’m playing table tennis with my younger brother and we’re almost done."),
       ("我吃过生鱼片，可是从来没吃过生蘑菇，也从来不知道那么多菜都可以生吃。", "4. I’ve eaten sashimi, but I’ve never eaten raw mushrooms, and never knew that so many dishes can be eaten raw.")]
DV = [("大卫上星期去了加拿大。", "1. David went to Canada last week. (mine)"), ("他是坐飞机去的。", "2. He went there by plane."), ("他以前从来没去过中国。", "3. He has never been to China before."), ("他今天要去中国。", "4. He is going to China today."), ("他正在等他的航班。", "5. He is waiting for his flight."), ("飞机就要起飞了。", "6. The plane is about to take off.")]
W8 = [("为了让大家听清楚，老师又慢慢地说了一遍。", "1. In order to let everyone hear clearly, the teacher slowly said it again. (为了; key mine)"), ("我想为你唱一首歌。", "2. I want to sing a song for you. (为)"), ("我再给你一次机会。", "3. I’ll give you one more chance. (给)"), ("班长给同学们发了一个邮件。", "4. The class monitor sent an email to the classmates. (给)"), ("你怎么这样对父母说话？", "5. How can you talk to your parents like this? (对)"), ("她给了我很多的帮助。", "6. She gave me a lot of help. (给)"), ("他对学外语很有兴趣。", "7. He is very interested in learning foreign languages. (对)")]
JIU = [("他就是你要找的人。", "1. He is exactly the person you’re looking for. — c, exactly (key mine)"), ("我一下课就给你打电话。", "2. I’ll call you as soon as class is over. — b, as soon as"), ("还有半个小时飞机就起飞了。", "3. In half an hour the plane will take off. — f, about to"), ("其他的菜都很好，就这个有点儿咸。", "4. The other dishes are all good; only this one is a bit salty. — e, just/small quantity"), ("飞机九点起飞，我七点就到机场了。", "5. The plane takes off at nine, and I was at the airport as early as seven. — a, earliest"),
       ("我弟弟不是玩手机就是看电脑。", "6. My younger brother is either on his phone or looking at the computer. — i, only two possibilities"), ("只要你高兴就行。", "7. As long as you’re happy, it’s fine. — h, as long as … then"), ("如果累了，就早点睡吧。", "8. If you’re tired, go to bed early. — d, if … then"), ("住在这里很方便，商店就有好几家。", "9. Living here is convenient; there are several stores alone. — g, easiness")]
A10 = [("你喜欢我还是我的钱？", "A1. Do you like me or my money? (还是; key mine)"), ("快十一点了，你们还是先睡觉吧，作业可以明天再做。", "A2. It’s almost eleven; you’d better go to bed first and do the homework tomorrow. (还是: had better)"), ("用手机或者电脑都可以上网。", "A3. You can go online with a phone or a computer. (或者/或是)"),
       ("星期六早上我十点才起床。", "B1. On Saturday morning I didn’t get up until ten. (才: later than expected)"), ("我们才学了三个月的中文。", "B2. We have only studied Chinese for three months. (才: only)"), ("怎么才能减肥？", "B3. How can one lose weight? / What does it take to lose weight? (才: only if)"), ("就是因为下雨，所以他才没去小王家。", "B4. It was precisely because of the rain that he didn’t go to Xiao Wang’s home. (才: cause and effect)"),
       ("逛完水族馆以后，我们还去了渔人码头。", "C1. After we finished visiting the aquarium, we also went to Fisherman’s Wharf. (完)"), ("各种装备都可以在滑雪场租到。", "C2. All kinds of equipment can be rented at the ski resort. (到)"), ("我订的是靠过道的座位，我想换成靠窗户的。", "C3. I booked an aisle seat and want to change it to a window seat. (成)"), ("大家一直玩儿到天黑才回家。", "C4. Everyone played until dark before going home. (到)"), ("肉烤好了以后，大家就坐下来一起野餐。", "C5. After the meat was cooked, everyone sat down for a picnic together. (好)"), ("网上买东西真方便，鼠标一点，东西就送到家门口了。", "C6. Shopping online is really convenient: one click of the mouse and the things are delivered to your doorstep. (到)"),
       ("你去过长城吗？去过，我去过三次。", "D1. Have you been to the Great Wall? Yes, I’ve been three times. (次)"), ("你的电话号码是多少？我以前给过你一遍吧？我忘了，你再说一遍吧！", "D2. What’s your phone number? I gave it to you once before, didn’t I? I forgot; say it again! (遍; the book’s first blank here is 一次 or 一遍; mine uses 遍 for repeating the number)"), ("听说你最近身体不太好，常常去医院。对，这个月我已经去过四次医院了。", "D3. I heard you haven’t been well lately and often go to the hospital. Yes, this month I’ve already been to the hospital four times. (次)"), ("你看过这部电影吗？看过。我都看了三遍了。", "D4. Have you seen this movie? Yes, I’ve watched it three times already. (遍)"),
       ("王老师刚才还在这儿，现在去哪儿了？他刚开会去了。", "E1. Teacher Wang was just here; where has he gone now? He just went to a meeting. (刚才, 刚)"), ("刚才的事儿你看见了吗？我刚到，没看见。", "E2. Did you see what just happened? I just arrived and didn’t see. (刚才, 刚)")]
HE = ("画上有一条大河，河上有一座长长的桥，桥下有好几条小小的船。有一条船是白色的，其他的都是黑色的。河边有一棵很高的树，树上长着很多苹果，个个都很红。树下躺着一个可爱的小男孩儿，看起来很开心的样子。孩子的身边有两只小白狗。")
HE_E = ("In the picture there is a big river; over the river there is a long bridge; under the bridge there are several tiny boats. One boat is white and the others are black. By the river there is a very tall tree with many apples growing on it, each very red. Under the tree lies a lovable little boy who looks very happy. Beside the child are two little white dogs. (This is the passage with the unnecessary 的 removed, which is the book’s task; the book’s original has 大的河, 很多的苹果, 很红的, 小的男孩儿 and 小的白的狗, and glosses 河, 桥 and 船 in pinyin; mine.)")
NIGHT = [("房间中间放着一张台球桌。", "A billiard table stands in the middle of the room. (mine; the picture is not included, so these describe the painting as I know it)"), ("墙上挂着一个钟。", "A clock hangs on the wall."), ("天花板上吊着几盏黄色的灯。", "Several yellow lamps hang from the ceiling."), ("几个人坐在桌子旁边，低着头。", "A few people sit at the tables with their heads down."), ("一个穿白衣服的男人站着，看着前面。", "A man in white stands, looking ahead.")]
SH = [("那本书在桌子上。", "1. The book is on the table. (key mine)"), ("书上是怎么说的？", "2. What does the book say?"), ("画上有什么？", "3. What is in the picture?"), ("在飞机上除了睡觉还能做什么？", "4. Besides sleeping, what else can you do on a plane?"), ("在火车上也可以上网。", "5. You can also go online on a train."), ("你可以在网上查一下。", "6. You can look it up online."), ("车在半路上坏了。", "7. The car broke down halfway."), ("他在学习上给了我很多帮助。", "8. He gave me a lot of help with my studies."), ("我在语法上还有很多问题。", "9. I still have many problems with grammar.")]
L4 = lesson(
    "Lesson 18 (Unit 3 review): grammar and usage review, part 2",
    "时态翻译 · 为了/为/给/对 · 就的九种用法 · 或者/还是 · 才 · 完到好成 · 次/遍 · 刚/刚才 · 着 · 上",
    requires=[],
    cards=[
        card("Activity 7 (Reading and Speaking): verb tenses",
             "A. Translate the sentences into English, paying careful attention to the verb tenses. The book glosses 谈恋爱, 婚礼, 乒乓球 and 生蘑菇 in pinyin and writes 25 as a digit. B. Now it is your turn to talk about David: translate six English sentences into Chinese and compare with a classmate. The translations in part A and my Chinese for part B are mine:",
             examples=[D(z, e) for z, e in TR7] + [D(z, e) for z, e in DV]),
        card("Activity 8 (Reading and Speaking): 为了, 为, 给, 对",
             "Complete the sentences using 为了, 为, 给 and 对. Read your work to a classmate and discuss any differences you find. The book leaves the key out (and glosses 机会 as “opportunity”); mine:",
             examples=[D(z, e) for z, e in W8]),
        card("Activity 9 (Reading): the functions of 就",
             "Match the 就 in each sentence with its function by writing the letters in the leftmost column: a. earliest; b. as soon as; c. exactly; d. if…then…; e. just/small quantity; f. about to; g. easiness; h. as long as…then…; i. expressing the only two possibilities. The key is mine:",
             examples=[D(z, e) for z, e in JIU]),
        card("Activity 10 (Reading, Listening, Writing and Speaking)",
             "A. Pair up. Use 或者/或是 and 还是 to complete the sentences; then translate them into English orally. B. Translate the sentences into English, paying attention to the different use of 才. C. Use the resultative complements 好, 到, 完 and 成 to complete the sentences. D. Complete the dialogs using the action measure words 次 and 遍. E. Fill the blanks with either 刚 or 刚才 where appropriate. The book leaves the key out (and writes 11 点 as a digit); mine:",
             examples=[D(z, e) for z, e in A10]),
        card("Activity 11 (Reading and Speaking): unnecessary 的; the painting",
             "A. The passage below is the description of a picture. Read it, highlight any unnecessary uses of 的, and translate it into English. B. Examine the image of “The Night Café” by Vincent van Gogh. Use the verb + aspect particle 着 to describe the painting. Form two groups; each group creates five sentences and reports to the class; after listening, combine the descriptions. (The painting is a picture, so it is not included.)",
             examples=[D(HE, HE_E)] + [D(z, e) for z, e in NIGHT]),
        card("Activity 12 (Reading and Speaking): (在) noun + 上",
             "Pair up. Take turns verbally translating the following (在) noun + 上 phrases into English. The translations are mine:",
             examples=[D(z, e) for z, e in SH]),
    ],
    exercises=[
        M("What does 我直到二十五岁才开始谈恋爱 mean?", "I didn’t start dating until I was twenty-five", ["I dated at twenty-five", "I will date at twenty-five", "I never dated"], "直到…才…"),
        M("Which fits 为了___大家听清楚，老师又说了一遍？", "让", ["对", "给", "往"], "为了让大家听清楚: in order to let everyone hear."),
        M("Which fits 我想___你唱一首歌？", "为", ["对", "往", "在"], "为你唱: sing for you."),
        M("Which fits 他___学外语很有兴趣？", "对", ["为", "往", "把"], "对…有兴趣."),
        M("What does 就 mean in 我一下课就给你打电话？", "As soon as", ["Exactly", "Earliest", "About to"], "一…就…"),
        M("What does 就 mean in 还有半个小时飞机就起飞了？", "About to", ["As soon as", "If…then", "Exactly"], "就 = about to."),
        M("What does 就 mean in 他就是你要找的人？", "Exactly", ["Earliest", "About to", "If…then"], "就是 = exactly."),
        M("What does 就 mean in 我弟弟不是玩手机就是看电脑？", "Expresses the only two possibilities", ["Exactly", "As soon as", "Earliest"], "不是…就是…"),
        M("Which fits 你喜欢我___我的钱？", "还是", ["或者", "和", "跟"], "还是 in a question: or."),
        M("Which fits 用手机___电脑都可以上网？", "或者", ["还是", "和", "就"], "或者 in a statement."),
        M("What does 怎么才能减肥？ mean?", "How can one (only) lose weight?", ["Why did you lose weight?", "When will you lose weight?", "Who lost weight?"], "怎么才能…"),
        M("Which complement fits 各种装备都可以在滑雪场租___？", "到", ["完", "成", "好"], "租到: rent and get."),
        M("Which complement fits 我想换___靠窗户的？", "成", ["到", "完", "好"], "换成: change into."),
        M("What is wrong with 大的河 in the picture description?", "The 的 is unnecessary: 大河", ["The measure word is missing", "河 is wrong", "Nothing is wrong"], "Short adjectives go straight before the noun."),
        M("What does 在语法上 mean in 我在语法上还有很多问题?", "In terms of grammar", ["On the grammar", "At the grammar", "Above grammar"], "(在) noun + 上 = in the aspect of."),
        F("你可以在网___查一下。", "上", PART, "在网上."),
        F("车在半路___坏了。", "上", PART, "在半路上."),
        F("王老师___才还在这儿，现在去哪儿了？", "刚", PART, "刚才."),
        F("我吃过生鱼片，可是从来没吃过生蘑菇，也从来不知道那么多菜都可以生___。", "吃", PART, "生吃."),
    ],
)

UNIT = unit("第十八课 Unit 3 review: objectives, vocabulary, presentation activities and grammar", [L1, L2, L3, L4])
