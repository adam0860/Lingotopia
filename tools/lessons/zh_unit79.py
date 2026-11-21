"""Unit 79: Lesson 26 (Study and Travel Abroad), Presentation 1: the dialog about sending a daughter abroad with its activities, 这么 + adjective, topic-comment sentences,
比如…等等/什么的, 可不是嘛, the skill-integration tasks (homestay families, Daming's letter, the host's advice), the using-Chinese tasks (boarding schools, preparing children,
a counselor's view and the debate) and the vocabulary list. Audio, pictures, videos and websites are not included; numbers the book writes as digits are spelled out;
answers that the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l26_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('不得不', 1, 'de2'), ('妞妞', 0, 'niu1'), ('妞妞', 1, 'niu1'), ('家长', 1, 'zhang3'), ('不适应', 2, 'ying4'), ('这种地方', 1, 'zhong3'), ('但是还愿意', 2, 'hai2'), ('都得努力', 1, 'dei3'), ('都得讲英', 1, 'dei3'), ('你得注意', 1, 'dei3'), ('你得选菜', 1, 'dei3'), ('进好学校', 1, 'hao3')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] == "目的地" or zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 1
P1 = [("张太太", "李姐，听说你家妞妞去国外上学了？", "Mrs. Zhang: Sister Li, I heard your Niuniu has gone abroad to school? (translations in this card are mine)"),
      ("李太太", "对，她现在在美国上中学。", "Mrs. Li: Yes, she is in middle school in America now."),
      ("张太太", "这么小，你们就把她送出国啊？", "Mrs. Zhang: So young, and you sent her abroad?"),
      ("李太太", "唉，还不是因为国内学习压力大，怕孩子太辛苦！", "Mrs. Li: Sigh, isn’t it because the study pressure at home is great and we were afraid the child would be too worn out!"),
      ("张太太", "她一个人在国外生活能适应吗？", "Mrs. Zhang: Can she adapt to living abroad alone?"),
      ("李太太", "她从小没离开过我们，刚开始确实不适应，我还过去陪读了好几个月。", "Mrs. Li: She had never left us since she was little, and at the beginning she really didn’t adapt; I even went over to accompany her studies for several months."),
      ("张太太", "你回国后，妞妞现在住在哪儿？", "Mrs. Zhang: After you came back, where does Niuniu live now?"),
      ("李太太", "我们帮她找了个寄宿家庭。有寄宿家庭照顾她，我就比较放心了。", "Mrs. Li: We found her a homestay family. With a homestay family looking after her, I feel rather relieved."),
      ("张太太", "她跟寄宿家庭能沟通吗？", "Mrs. Zhang: Can she communicate with the homestay family?"),
      ("李太太", "一开始是挺困难的，现在好多了。那家有两个女儿，和她的年龄差不多，常常在生活上和学习上帮助她。", "Mrs. Li: At the beginning it was quite difficult; now it’s much better. That family has two daughters about her age, who often help her in life and in study."),
      ("张太太", "那太好了，听说一些小留学生由于没有人照顾，养成了一些坏习惯，比如逃学，喝酒，抽烟什么的。", "Mrs. Zhang: That’s great. I heard that some young international students, because nobody looks after them, develop bad habits, such as skipping school, drinking and smoking."),
      ("李太太", "是啊，他们还小，很多地方都不成熟。", "Mrs. Li: Yes, they are still young and in many ways not mature."),
      ("张太太", "你们分隔两地，还是会担心吧？", "Mrs. Zhang: You are separated in two places; you still worry, don’t you?"),
      ("李太太", "当然，所以我们常常和她视频聊天，而且我和先生一有空儿，就做“空中飞人”飞过去看她。", "Mrs. Li: Of course, so we often video chat with her, and whenever my husband and I have time we become “trapeze artists” and fly over to see her."),
      ("张太太", "可怜天下父母心，一切都是为了孩子。", "Mrs. Zhang: Pitiful are the hearts of parents everywhere; everything is for the children."),
      ("李太太", "可不是嘛！车来了，我得走了。", "Mrs. Li: You said it! The bus is here, I have to go."),
      ("张太太", "好。下次再聊！", "Mrs. Zhang: OK. Let’s chat next time!")]
NEG = [("国内学习压力大，孩子太辛苦。", "Negative phrases from the dialog, with sample sentences (mine): 压力大, 辛苦: The study pressure at home is great and the children are too worn out."),
       ("刚开始他不适应，也有很多困难。", "不适应, 困难: At the beginning he didn’t adapt and had many difficulties."),
       ("小留学生没有人照顾，养成了逃学、喝酒、抽烟的坏习惯。", "坏习惯, 逃学, 喝酒, 抽烟: Young students with nobody looking after them develop the bad habits of skipping school, drinking and smoking."),
       ("父母分隔两地，常常担心孩子，觉得孩子不成熟，很可怜。", "分隔两地, 担心, 不成熟, 可怜: Parents separated in two places often worry about the child and feel the child is not mature and rather pitiful.")]
CORE = table(["词", "核心意思 (my answers)"], [["压力", "压: press, weigh down; 力: force. Pressure, stress."], ["陪读", "陪: accompany; 读: study. To accompany a child who studies abroad."], ["成熟", "成: become; 熟: ripe. Mature, fully grown."], ["放心", "放: put down; 心: heart. To put the heart at ease, not to worry."], ["困难", "困: trapped; 难: hard. Difficulty."], ["逃学", "逃: escape; 学: school. To skip school."]],
             title="Activity 1B: the core meaning of each underlined character (the book’s box is blank; the answers are mine)", say=[0])
K2 = [("她们可能是朋友或者邻居，李太太的女儿去美国上中学了。", "Activity 2A (my answers): The two speakers are probably friends or neighbors; Mrs. Li’s daughter has gone to middle school in America."),
      ("妞妞是李太太的女儿，在美国上中学，一开始不适应，现在住在寄宿家庭。", "2B-1 (mine): Niuniu is Mrs. Li’s daughter; she is in middle school in America, didn’t adapt at the beginning, and now lives with a homestay family."),
      ("语言沟通有困难，不适应生活，也可能养成坏习惯。", "2B-2 (mine): language difficulties, not adapting to life, and possibly developing bad habits."),
      ("帮她找了寄宿家庭，过去陪读，常常视频聊天，还飞过去看她。", "2B-3 (mine): they found her a homestay family, went over to accompany her studies, often video chat and fly over to see her.")]
D3 = [("因为国内学习压力大，怕孩子太辛苦。", "A (my completion): Because the study pressure at home is great and we were afraid the child would be too tired."),
      ("她住在一个寄宿家庭里。", "A (mine): She lives in a homestay family."),
      ("一开始有点困难，现在好多了。", "A (mine): It was a bit difficult at the beginning; now it’s much better."),
      ("担心，所以我们常常和她视频聊天。", "A (mine): We do worry, so we often video chat with her."),
      ("是啊，还是会担心，所以一有空儿我就飞过去看她。", "A (mine): Yes, we still worry, so whenever I have time I fly over to see her.")]
QS3 = [("怎么这么小就把孩子送出国啊？", "Q1: How come you sent your child abroad so young?"), ("你孩子现在住在哪儿？", "Q2: Where does your child live now?"), ("她跟寄宿家庭能沟通吗？", "Q3: Can she communicate with the homestay family?"), ("你们不在身边，不担心她养成什么坏习惯吗？", "Q4: With you not around, aren’t you worried she will develop some bad habits?"), ("你和孩子分隔两地，还是会担心吧？", "Q5: You and your child are separated in two places; you still worry, don’t you?")]
WP = table(["第一组", "第二组", "第三组", "第四组", "第五组", "第六组"], [["适应", "一切", "放心", "辛苦", "成熟", "沟通"], ["适合", "所有", "担心", "努力", "养成", "聊天"]],
           title="Activity 5: the word pairs", say=[0, 1, 2, 3, 4, 5])
K5 = [("很多寄宿学校的学生一开始很难适应离开家住校的生活，因为样样事都得自己来。", "1a. Many boarding-school students find it hard at first to adapt to the life of leaving home and living at school, because they have to do everything themselves. (my key: 适应)"),
      ("选择一个适合自己的寄宿家庭才能顺利在国外求学、生活。", "1b. Only by choosing a homestay family that suits you can you study and live abroad smoothly. (my key: 适合)"),
      ("中国父母从小关心孩子的一切，照顾他们生活上、学习上大大小小的事。", "2a. Chinese parents care about everything of their child from an early age and look after big and small matters in life and study. (my key: 一切)"),
      ("我父母把他们所有的钱都花在我们的教育上，我们才能上好学校，才能出国念书。", "2b. My parents spent all their money on our education, so we could go to good schools and study abroad. (my key: 所有)"),
      ("因为担心在寄宿家庭的生活，很多父母常常给孩子打电话关心他们。", "3a. Because they worry about life in the homestay, many parents often call their children to show concern. (my key: 担心)"),
      ("从小我就能自己照顾自己，所以出国念书，我父母很放心。", "3b. I could look after myself from an early age, so when I went abroad to study my parents were very relieved. (my key: 放心)"),
      ("不管在哪里学习都得努力，这样才会有好的前途。", "4a. No matter where you study you have to work hard; only then will you have a good future. (my key: 努力)"),
      ("不管我的父母工作多辛苦，他们都要让我出国念书。", "4b. No matter how hard my parents worked, they wanted me to study abroad. (my key: 辛苦)"),
      ("小时候要养成好的生活习惯，长大才能自己照顾自己。", "5a. You have to form good living habits when you are little to be able to look after yourself when you grow up. (my key: 养成)"),
      ("要是没有成熟的身心，很难适应国外辛苦的留学生活。", "5b. Without a mature body and mind it is hard to adapt to the hard life of studying abroad. (my key: 成熟)"),
      ("如果有学习上的困难，要随时和老师沟通。", "6a. If there are difficulties in study, communicate with the teacher at any time. (my key: 沟通)"),
      ("现在的人除了打电话也喜欢用视频聊天。", "6b. Besides phone calls, people now also like to video chat. (my key: 聊天)")]
L1 = lesson(
    "Lesson 26 Presentation 1: sending a daughter abroad to study",
    "出国热 · 小留学生 · 寄宿家庭 · 陪读 · 空中飞人 · 可怜天下父母心 · 可不是嘛",
    requires=[],
    cards=[
        card("Learning objectives and grammar of Lesson 26 (Study and Travel Abroad, 出国热)",
             "Unit 5, Social Factors. Lesson 26 topic: Describe characteristics of overseas Chinese students; discuss issues overseas Chinese students face; compare overseas Chinese students at different periods in their studies; analyze Chinese tourist travel methods and purposes. Grammar: 这么 + adj. + further explanation; 主题句; 比如…, 等等; 可不是嘛 / 可不是吗?; 并; 多半儿; 被 Verb 为; 尽管 vs. 不管; 多重复句; 有些人…有些人…还有些人; 总之. Area Studies: Overseas Chinese Students."),
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. What do you consider the pros and cons of sending children abroad to study? B. What issues do you think a child or teenager might face when studying abroad? C. How would you help your children cope with their new environment? (Three pictures are not included.)"),
        card("Presentation 1: 妞妞出国", "The book also prints the dialog in traditional characters. The translations are mine.", examples=dlg(P1)),
        card("Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. In the box below, identify the phrases with negative connotations and write one sentence for each. Then read your sentences to a partner, who will translate them back to you. B. Discuss the core meaning of each underlined character with your partner and write the meaning below: 压力, 陪读, 成熟, 放心, 困难, 逃学. (The book’s boxes are blank; mine follow.)",
             tables=[CORE], examples=[D(z, e) for z, e in NEG]),
        card("Activity 2 (Listening, Speaking and Reading)",
             "A. Global Listening: Listen to Presentation 1 once through and answer the questions. 1. What is the likely relationship between the two speakers? 2. What information is exchanged in the conversation? B. Detailed Listening: 1. Who is 妞妞? What three things have you learned about her? 2. What three difficulties might overseas Chinese students like 妞妞 face? 3. What are three ways her parents have helped her to adapt? Then share your answers with a partner in Chinese and perform the presentation together. (Audio; my answers from the text:)",
             examples=[D(z, e) for z, e in K2]),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Pair up. Complete the following dialog, then practice performing it together. B. Perform your dialog for the class. The five questions are the book’s; the answers are mine:",
             examples=[D(q, qe) for q, qe in QS3] + [D(a, ae) for a, ae in D3]),
        card("Activity 4 (Listening, Writing, Reading and Speaking)",
             "A. Listen to the interview with a homestay host. After listening through once, write down as many of the interviewer’s questions as you can remember. After listening through a second time do the same for the host’s replies (Interview Questions | Responses, rows 1–4). B. Work with a partner to complete and correct your questions and responses as much as possible. C. Listen to the interview a third time and make any necessary corrections or additions. D. Perform the interview script with your partner. Switch roles and repeat. (Audio; the script is not in the book.)"),
        card("Activity 5 (Reading, Writing, Speaking and Listening)",
             "A. Fill in the blanks with the correct choice from the word pairs: 适应/适合; 一切/所有; 放心/担心; 辛苦/努力; 成熟/养成; 沟通/聊天. B. Compare work with a partner. C. Write a story with at least five sentences using five of the vocabulary items from above. D. Read your story to your partner and ask each other questions about your stories in Chinese. The completed sentences (my key):",
             tables=[WP], examples=[D(z, e) for z, e in K5]),
    ],
    exercises=[
        M("What does Mrs. Zhang ask about at the start?", "Whether Niuniu has gone abroad to school", ["Whether Mrs. Li is moving", "Where the bus stop is", "What time it is"], "听说你家妞妞去国外上学了？"),
        M("Why did Mrs. Li send her daughter abroad so young?", "The study pressure at home is great", ["Free tuition", "A scholarship", "A job offer"], "国内学习压力大，怕孩子太辛苦."),
        M("What did Mrs. Li do for several months?", "Went over to accompany her studies (陪读)", ["Took a holiday", "Worked abroad", "Studied English"], "陪读了好几个月."),
        M("Who lives in the homestay family with Niuniu?", "Two daughters about her age", ["Two sons", "A grandmother only", "No children"], "两个女儿，和她的年龄差不多."),
        M("Which bad habits do some young students develop?", "Skipping school, drinking and smoking", ["Reading and sleeping", "Painting and singing", "Running and swimming"], "逃学，喝酒，抽烟."),
        M("How do they keep in touch with Niuniu?", "Video chat and flying over (空中飞人)", ["Letters only", "Telegrams", "Never"], "视频聊天…飞过去看她."),
        M("What does 可不是嘛 mean?", "Exactly; you said it", ["Of course not", "Maybe", "I don’t know"], "可不是嘛."),
        M("Which word fits “选择一个___自己的寄宿家庭”?", "适合", ["适应", "成熟", "沟通"], "适合: suit."),
        M("Which word fits “一开始很难___离开家的生活”?", "适应", ["适合", "养成", "一切"], "适应: adapt."),
        M("Which word fits “小时候要___好的生活习惯”?", "养成", ["成熟", "担心", "聊天"], "养成: form."),
        F("现在的人除了打电话也喜欢用视频___天。", "聊", PART, "聊天: chat."),
        F("不管我的父母工作多___苦，他们都要让我出国念书。", "辛", PART, "辛苦: hard."),
        F("因为担心在寄宿家庭的生活，很多父母常常给孩子打电话___心他们。", "关", PART, "关心: show concern."),
    ],
)

# ------------------------------------------------------------------ 2. 这么 + adj.
ZM0 = table(["结构", "用法"], [["这么 + Adj. + Comment/Question", "remarks on a significant or surprising fact or aspect, often followed by a comment or question"]],
            title="话语语法: 这么 + Adjective")
ZE = [("她现在在美国上中学。", "1. Q: She is in middle school in America now."), ("这么小，你们就把她送出国啊？", "A: So young, and you sent her abroad?"),
      ("李华最近开了一家公司，当上了老板。", "2. Q: Li Hua recently opened a company and became a boss."), ("这么年轻，他就当了老板。", "A: So young, and he became a boss."),
      ("这件衬衫一件八百块。", "3. Q: This shirt costs 800 yuan each. (the book writes 800 in digits)"), ("这么贵，你还要买啊？", "A: So expensive, and you still want to buy it?"),
      ("我要在一个月内减肥十公斤。可我现在只减了一公斤。", "4. Q: I want to lose 10 kilos within a month, but I have only lost one so far. (the book writes 10 in digits)"), ("这么困难，你还要继续做啊？", "A: So difficult, and you still want to carry on?")]
ZA1 = [("自由行得自己上网订票、订旅馆，还要自己安排行程。", "1. A: With independent travel you have to book tickets and hotels online yourself and arrange the itinerary yourself."), ("这么麻烦。我还是跟旅行团吧。", "B (the book’s example): So troublesome. I’d rather join a tour group."),
       ("送孩子出国念书一年得花上好几十万。", "2. A: Sending a child abroad to study costs several hundred thousand a year."), ("这么贵，你们还要送孩子出国啊？", "B (my answer): So expensive, and you still send your child abroad?"),
       ("我五分钟前上“美团”下单点外卖，饭马上就送到了。", "3. A: Five minutes ago I placed a takeout order on Meituan, and the food arrived right away."), ("这么快，我还以为要等半个小时呢。", "B (my answer): So fast; I thought I’d have to wait half an hour."),
       ("我奶奶九十岁了，天天去公园运动。", "4. A: My grandmother is ninety and goes to the park to exercise every day. (the book writes 90 in digits)"), ("这么大年纪，她还天天去运动啊？", "B (my answer): At such an age, she still exercises every day?"),
       ("住民宿有厨房可以自己做饭。", "5. A: A homestay has a kitchen where you can cook yourself."), ("这么方便，我下次也要住民宿。", "B (my answer): So convenient; next time I’ll stay in a homestay too."),
       ("这个健身房什么服务设施都有，所以会员很多。", "6. A: This gym has every kind of service and facility, so it has many members."), ("这么好，我也想办一张会员卡。", "B (my answer): So good; I’d like to get a membership card too.")]
ZA2 = [("这么年轻，你就结婚了，还生了三个孩子。", "The book’s example: So young, and you got married and even had three children. (the book writes 3 in digits)"),
       ("这么忙，你还每天学习中文啊？", "My sample: So busy, and you still study Chinese every day?")]
L2 = lesson(
    "Lesson 26 Presentation 1 grammar: 这么 + adjective for remarking on a surprising fact",
    "这么小 你们就把她送出国啊 · 这么年轻 · 这么贵 你还要买啊 · 这么困难 你还要继续做啊 · 这么麻烦",
    requires=[],
    cards=[
        card("话语语法: 这么 + Adjective",
             "A speaker uses 这么 + adjective to remark on a significant or surprising fact or aspect. It is often followed by a comment or question.",
             tables=[ZM0], examples=[D(z, e) for z, e in ZE]),
        card("Activity 1 (Reading and Writing)",
             "A. For each statement below, write a response using the 这么 + adj. pattern. The first one has been done as an example for you. The book’s B lines for items 2 to 6 are blank; the answers are mine.",
             examples=[D(z, e) for z, e in ZA1]),
        card("Activity 2 (Speaking and Writing)",
             "A. Interview a partner in Chinese to find out three significant, impressive, interesting or surprising facts about them. B. Write a sentence for each one of these facts using 这么 + adj. C. Read your sentences to your partner, then ask them a few follow-up questions in Chinese.",
             examples=[D(z, e) for z, e in ZA2]),
    ],
    exercises=[
        M("What does 这么 + adjective remark on?", "A significant or surprising fact", ["A future plan", "A past habit", "A polite request"], "Remarks."),
        M("What often follows 这么 + adj.?", "A comment or question", ["A number", "A date", "A name"], "Comment/Question."),
        M("What does 这么小，你们就把她送出国啊？ express?", "Surprise that she is so young", ["Approval", "A threat", "Thanks"], "这么小."),
        M("Which is a response to “这件衬衫一件八百块”?", "这么贵，你还要买啊？", ["这么便宜，你还要买啊？", "这么快，你还要买啊？", "这么远，你还要买啊？"], "这么贵."),
        M("Which is a response to “我奶奶九十岁了，天天去公园运动”?", "这么大年纪，她还天天去运动啊？", ["这么小，她还去运动啊？", "这么冷，她还去运动啊？", "这么远，她不去运动啊？"], "My answer."),
        M("Which is a response to “自由行得自己上网订票、订旅馆”?", "这么麻烦。", ["这么便宜。", "这么好吃。", "这么近。"], "The book’s example."),
        M("Which fits a statement that someone became a boss very early?", "这么年轻，他就当了老板", ["这么老，他就当了老板", "这么远，他就当了老板", "这么冷，他就当了老板"], "这么年轻."),
        F("___么贵，你还要买啊？", "这", PART, "这么 + adj."),
        F("这么困难，你还要继___做啊？", "续", PART, "继续: continue."),
    ],
)

# ------------------------------------------------------------------ 3. 主题句
TC0 = table(["结构", "用法"], [["Sentence Topic + Comment on Topic", "the topic sets up what will be commented on; it is not the grammatical subject"]],
            title="主题句 Topic-Comment Sentences")
TCE = [("有寄宿家庭照顾她，我就比较放心了。", "1. With a homestay family looking after her, I feel rather relieved. (topic: 有寄宿家庭照顾她; comment: 我就比较放心了)"),
       ("去中国旅游，我觉得还是两个星期比较合适。", "2. As for traveling to China, I think two weeks is still more suitable."),
       ("在中国看病，还是挂专家门诊比较保险。", "3. As for seeing a doctor in China, it is still safer to register for a specialist clinic."),
       ("出国读研究生，还是去英国念比较快拿到学位。", "4. As for going abroad for graduate school, it is still quicker to get the degree by studying in Britain.")]
TS0 = ("中国的父母觉得孩子只有上好学校，以后才能有好的工作、好的生活。所以从小就帮孩子计划好以后的路，帮孩子报名上各种各样的学习班。除了学习，其他的事父母都包了。美国的父母从小让孩子从玩和游戏中学习，孩子长大后，让孩子从工作中、生活中学到很多经验，他们很少告诉孩子应该怎么做，总是让孩子自己做决定。",
       "The book’s example passage: Chinese parents think that children can have good jobs and a good life later only if they go to good schools. So from early on they plan the child’s future path and sign the child up for all kinds of classes. Apart from study, parents take care of everything else. American parents let children learn through play and games from an early age, and when children grow up let them learn a lot of experience from work and life; they seldom tell children what to do and always let children make their own decisions.")
TSS = [("怎样教育孩子，中国父母觉得学习比什么都重要。", "The book’s summary: As for how to educate children, Chinese parents feel study is more important than anything."),
       ("怎样教育孩子，东西方的父母有不同的看法。", "Or: As for how to educate children, Eastern and Western parents have different views.")]
TP1 = ("要有健康的身体，你得注意少吃甜食，多吃营养的东西，比如蔬菜、水果等。另外，还要多喝水，每天最少要喝八杯水。除了饮食以外，你还得注意你的睡眠。每天最好早睡早起，睡足八个小时。最后，你还得选择适合你的运动，不管你做什么运动，每天最好运动一到两个小时。",
       "Passage 1: To have a healthy body, you must watch that you eat less sweet food and eat more nutritious things, such as vegetables and fruit. In addition, drink more water, at least eight glasses a day. Besides diet, you also have to watch your sleep: it is best to go to bed and get up early every day and sleep a full eight hours. Finally, you have to choose the exercise that suits you; no matter what exercise you do, it is best to exercise one to two hours a day. (the book writes 1-2 in digits)")
TP2 = ("很多父母为孩子选择寄宿学校是因为寄宿学校通常是比较贵，在那里学习，孩子能有比较好的学习环境和质量。下课后，老师还会帮孩子辅导功课。另外，很多孩子从小没离开过家，很多事都不会做。寄宿学校可以照顾孩子的日常生活，也训练孩子自理生活的能力。",
       "Passage 2: Many parents choose boarding schools for their children because boarding schools are usually more expensive, and studying there the children can have a better learning environment and quality. After class the teachers will also tutor the children’s homework. In addition, many children have never left home and cannot do many things. Boarding schools can look after the children’s daily life and also train the children’s ability to look after themselves.")
TSM = [("要有健康的身体，饮食、睡眠和运动都要注意。", "Passage 1 summary (mine): To have a healthy body, diet, sleep and exercise all need attention."),
       ("为孩子选择寄宿学校，好处是环境好，有人辅导，还能训练自理的能力。", "Passage 2 summary (mine): As for choosing a boarding school for a child, the benefits are a good environment, tutoring and training in self-care.")]
TCS = [("下星期我们考试。", "S1 (topic): Next week we have an exam."), ("我们这星期最好先不去旧金山了。", "S2 (comment 1): We had better not go to San Francisco this week."), ("我们找时间一起复习复习吧！", "S3 (comment 2): Let’s find time to review together!")]
L3 = lesson(
    "Lesson 26 Presentation 1 grammar: 主题句, topic-comment sentences",
    "有寄宿家庭照顾她我就比较放心了 · 去中国旅游还是两个星期比较合适 · 怎样教育孩子 · 下星期我们考试",
    requires=[],
    cards=[
        card("主题句 Topic-Comment Sentences",
             "In topic-comment sentences, the topic of the sentence is followed by a comment on it. Grammatically, the topic is not the subject of the sentence, but rather sets up what is going to be commented on in the sentence.",
             tables=[TC0], examples=[D(z, e) for z, e in TCE]),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Summarize each of the passages below in one sentence using a topic-comment structure. Example (the passage, then the summary):",
             examples=[D(*TS0)] + [D(z, e) for z, e in TSS]),
        card("Activity 3: Passage 1 and Passage 2", "My summaries follow each passage in the next card.", examples=[D(*TP1), D(*TP2)]),
        card("Activity 3: my summaries; parts B and C",
             "B. Read your sentences to a partner, then decide who wrote the best summary for each passage. C. Form groups of three. State a topic related to yourself or the class, while your two classmates comment on it. The book’s example is S1, S2, S3 below. The book leaves the summary lines blank; mine are the first two sentences.",
             examples=[D(z, e) for z, e in TSM + TCS]),
    ],
    exercises=[
        M("In a topic-comment sentence, what follows the topic?", "A comment on it", ["A question word", "A number", "A name"], "Topic + comment."),
        M("Is the topic the grammatical subject?", "No, it sets up what will be commented on", ["Yes, always", "Only in questions", "Only in the past"], "Not the subject."),
        M("In 有寄宿家庭照顾她，我就比较放心了, what is the topic?", "有寄宿家庭照顾她", ["我就比较放心了", "比较", "放心"], "Topic."),
        M("In 有寄宿家庭照顾她，我就比较放心了, what is the comment?", "我就比较放心了", ["有寄宿家庭", "照顾她", "妞妞"], "Comment."),
        M("Which is a topic-comment sentence?", "去中国旅游，我觉得还是两个星期比较合适", ["我去中国旅游了", "你去中国旅游吗", "他去过中国"], "Topic: 去中国旅游."),
        M("What is the topic of the book’s example summary?", "怎样教育孩子", ["中国父母", "学习班", "美国父母"], "怎样教育孩子 (topic)."),
        M("Which sentence shows a topic and a comment?", "出国读研究生，还是去英国念比较快拿到学位", ["我出国读研究生", "他念研究生吗", "研究生很多"], "Topic + comment."),
        F("在中国看病，还是挂专家门诊比较___险。", "保", PART, "保险: safe."),
        F("去中国旅游，我觉得还是两个星期比较合___。", "适", PART, "合适: suitable."),
    ],
)

# ------------------------------------------------------------------ 4. 比如
BR0 = table(["结构", "用法"], [["…, 比如 N1, N2, N3…等等/什么的", "lists nouns as examples of an entity or phenomenon"], ["…, 比如 VP, VP, VP…等等/什么的", "lists verb phrases as examples"], ["…, 比如 + Sentence (什么的)", "when followed by a sentence, 等等 and 什么的 are usually omitted"]],
            title="比如… 等等/什么的")
BR1 = table(["Examples", "Meanings"], [["比如 (colloquial), 例如 (formal), 譬如 pìrú (formal)", "such as…"], ["比如说 (colloquial), 比方说 (colloquial), 譬如说 (formal), 举例来说 (formal)", "for example; for instance"]],
            title="Words for “such as” and “for example” (the book’s table)")
BE1 = [("一些小留学生由于没有人照顾，养成了一些坏习惯，比如逃学，喝酒，抽烟什么的。", "1. Some young international students, because nobody looks after them, develop bad habits, such as skipping school, drinking and smoking."),
       ("你有没有需要报关的物品，比如食品、药品什么的。", "2. Do you have any items that need to be declared, such as food and medicine?"),
       ("周末的时候，我总是很忙，比如到郊外爬山、去海边冲浪或是去图书馆学习等等。", "3. At weekends I am always busy, for example going hiking in the countryside, surfing at the seaside or studying at the library.")]
BE2 = [("他什么都不会做，比如他不会开车，不会做饭。", "1. He can’t do anything; for example he can’t drive and can’t cook."),
       ("中国到处都是名胜古迹，比如兵马俑、故宫，都非常值得一看。", "2. China is full of scenic spots and historic sites, such as the Terracotta Army and the Forbidden City, all well worth seeing."),
       ("在手机上下载一个应用软件，比如“美团”或是“饿了么”就可以点啦。", "3. Download an app on your phone, such as Meituan or Ele.me, and you can order.")]
BM4 = table(["A 列", "B 列"], [["1. 上订餐平台点外卖有几个手续，", "D. 比如你得选菜、下单，还得追踪你点的餐什么时候会送到。"], ["2. 他的兴趣爱好多种多样，", "C. 比如唱歌、跳舞、踢球什么。"], ["3. 旧金山国际机场有很多服务设施，", "A. 例如行李托运处、提款机、外币兑换处等。"], ["4. 要学好中文除了努力，还得有好的办法，", "E. 比方说多看真实语料，多和中国人交流，都能提高学习效果。"], ["5. 在国外生活有几件事非常重要，", "B. 比方说，你最好喜欢自己动手，还要能不怕吃苦。"]],
            title="Activity 4A: the matching, in my key order (the book prints the endings in the order A to E; the key is mine)")
BT4 = [("上订餐平台点外卖有几个手续，比如你得选菜、下单，还得追踪你点的餐什么时候会送到。", "1. Ordering takeout on a meal-ordering platform has several steps, for example you must choose dishes, place the order and also track when your food will be delivered. (the book prints 上订餐平台, with a stray 上; kept as printed)"),
       ("他的兴趣爱好多种多样，比如唱歌、跳舞、踢球什么。", "2. His interests and hobbies are varied, such as singing, dancing and playing football."),
       ("旧金山国际机场有很多服务设施，例如行李托运处、提款机、外币兑换处等。", "3. San Francisco International Airport has many service facilities, such as baggage check-in, ATMs and foreign-currency exchange counters."),
       ("要学好中文除了努力，还得有好的办法，比方说多看真实语料，多和中国人交流，都能提高学习效果。", "4. To learn Chinese well, besides working hard you also need good methods; for example reading more authentic material and communicating more with Chinese people can both improve learning results."),
       ("在国外生活有几件事非常重要，比方说，你最好喜欢自己动手，还要能不怕吃苦。", "5. There are several things that are very important in living abroad; for example, you had better like doing things yourself and also be able to endure hardship.")]
L4 = lesson(
    "Lesson 26 Presentation 1 grammar: 比如…等等/什么的 for giving examples",
    "比如 例如 譬如 · 比如说 比方说 举例来说 · 逃学 喝酒 抽烟什么的 · 兵马俑 故宫 · 旧金山国际机场的服务设施",
    requires=[],
    cards=[
        card("比如… 等等/什么的",
             "比如…等等/什么的 is used to list nouns or verb phrases as examples of a particular entity or phenomenon. It is similar to “such as…, etc. / and so on” in English. While 等等 is more formal than the colloquial 什么的, both may be omitted. Similar expressions include 比如, 例如 and 譬如. When 比如 is followed by a sentence, 等等 and 什么的 are usually omitted.",
             tables=[BR0, BR1], examples=[D(z, e) for z, e in BE1]),
        card("比如 followed by a sentence", "The English is mine.", examples=[D(z, e) for z, e in BE2]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Match the sentence beginnings on the left with their appropriate endings on the right. B. Pair up. Read the complete sentences aloud, switching between you until all five sentences have been read. C. Translate the sentences on your own, then compare translations with your partner. The book gives no key; the matches and the translations are mine:",
             tables=[BM4], examples=[D(z, e) for z, e in BT4]),
    ],
    exercises=[
        M("What is 比如 like in English?", "“Such as”", ["“Because”", "“Although”", "“Instead”"], "比如."),
        M("Which is more formal than 比如?", "例如", ["比方说", "比如说", "什么的"], "例如 (formal)."),
        M("Which is more formal, 等等 or 什么的?", "等等", ["什么的", "Both equal", "Neither"], "等等 is more formal."),
        M("What happens to 等等 and 什么的 when 比如 is followed by a sentence?", "They are usually omitted", ["They are doubled", "They come first", "They become 吗"], "Usually omitted."),
        M("Which completes 要学好中文除了努力，还得有好的办法，___?", "比方说多看真实语料，多和中国人交流", ["例如行李托运处、提款机", "比如唱歌、跳舞", "比如你得选菜、下单"], "Match 4."),
        M("Which completes 他的兴趣爱好多种多样，___?", "比如唱歌、跳舞、踢球什么", ["例如行李托运处", "比如你得选菜", "比方说多看语料"], "Match 2."),
        M("Which completes 旧金山国际机场有很多服务设施，___?", "例如行李托运处、提款机、外币兑换处等", ["比如唱歌、跳舞", "比方说你最好自己动手", "比如你得选菜"], "Match 3."),
        M("What does 举例来说 mean?", "For example (formal)", ["By the way", "In short", "Of course"], "举例来说."),
        F("你有没有需要报关的物品，比如食品、药品什___？", "么", PART, "什么的."),
        F("中国到处都是名胜古迹，比___兵马俑、故宫，都非常值得一看。", "如", PART, "比如."),
    ],
)

# ------------------------------------------------------------------ 5. 可不是嘛
KB0 = table(["结构", "用法"], [["A: Assertion", "an assertion that someone just made"], ["B: 可不是嘛/吗 (+ further support to echo the assertion)", "strongly agrees and often adds elaboration, emphasis or testimony"]],
            title="话语语法: 可不是嘛/吗")
KE = [("那个风景点很远吧？", "1. A: That scenic spot is far, isn’t it? (assertion)"), ("可不是吗，坐车要一个小时呢。", "B: You said it, it takes an hour by car. (echo)"),
      ("坐早上八点的飞机，时间很紧张。", "2. A: Taking the eight o’clock plane in the morning, time is very tight."), ("可不是吗，五点以前就得起床。", "B: You said it, you have to get up before five."),
      ("听说今年夏天北京很热。", "3. A: I heard Beijing is very hot this summer."), ("可不是吗，连续半个月气温都在三十五摄氏度以上。", "B: You said it, for half a month running the temperature has been above 35 degrees Celsius. (the book writes 35 in digits)")]
L5 = lesson(
    "Lesson 26 Presentation 1 grammar: 可不是嘛/吗 for strong agreement",
    "可不是吗 · 坐车要一个小时呢 · 五点以前就得起床 · 连续半个月气温都在三十五摄氏度以上 · 谁说不是呢 没错 的确 确实",
    requires=[],
    cards=[
        card("话语语法: 可不是嘛/吗",
             "The colloquial expression 可不是嘛/吗 is used to strongly agree with an assertion someone just made. It is often followed by the speaker’s further elaboration, emphasis or testimony to echo the assertion. It is thus similar in meaning and function to the English “you can say that again,” “absolutely” or “that’s very/so true.” Similar Chinese expressions are 可不吗?, 可不(是), 谁说不是呢?, 说得对, 没错, 的确 and 确实, among others.",
             tables=[KB0], examples=[D(z, e) for z, e in KE]),
        card("Activity 5 (Listening, Writing and Speaking)",
             "A. Listen to the following dialogs and in Chinese write down the agreed-upon assertion in each one (rows 1–5). B. Read your answers to a partner. (Audio and a picture; the scripts are not in the book.)"),
    ],
    exercises=[
        M("What is 可不是嘛 used for?", "To strongly agree with an assertion", ["To refuse", "To ask a question", "To say goodbye"], "Strong agreement."),
        M("What does it often come with?", "Further elaboration to echo the assertion", ["A question", "A command", "A refusal"], "Elaboration."),
        M("Which means “you can say that again”?", "可不是嘛", ["可是吗", "不是嘛", "可以吗"], "可不是嘛."),
        M("Which is NOT a similar expression?", "我不知道", ["谁说不是呢", "没错", "的确"], "Similar expressions."),
        M("A: 那个风景点很远吧？ B: ___，坐车要一个小时呢。", "可不是吗", ["不是吗", "是吗", "怎么吗"], "可不是吗."),
        M("What does B add in “可不是吗，五点以前就得起床”?", "Support for the tight schedule", ["A refusal", "A question", "A joke"], "Echo."),
        M("A: 听说今年夏天北京很热。 What does B’s echo say?", "For half a month it has been above thirty-five degrees", ["It is cold", "It rains daily", "It snows"], "连续半个月气温都在三十五摄氏度以上."),
        F("可不是___，坐车要一个小时呢。", "吗", ["吧", "呢", "了"], "可不是吗."),
        F("可不是吗，五点以前就___起床。", "得", PART, "得 děi: must."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration 1-3
SK1 = table(["生词", "拼音", "English"], [["管理", "guǎnlǐ", "manage"], ["学区", "xuéqū", "school district"]], title="Activity 1: new vocabulary", say=[0])
HS = ("你想让你的孩子出国留学吗？那么找到适合你孩子的寄宿家庭是在国外顺利留学很重要的一步。你可以根据孩子的需要，为他们选择下面几种寄宿家庭。第一种是华人家庭。他们通常是已经住在国外多年的中国家庭。有些家长觉得孩子住在华人家庭，在语言、文化和生活习惯上差不多，所以沟通和适应比较没问题。但是也担心孩子在华人家庭不能锻炼英文，也不能真正认识美国文化。另一种寄宿家庭是一般的美国家庭，常常是一对父母带着两三个孩子住在大房子里。如果选择这样的家庭，孩子不但可以学习语言，可以跟着寄宿家庭了解当地的文化，还可以和寄宿家庭的其他孩子像兄弟姐妹一样生活。这是很多独生子女在国内体验不到的，但是也因为寄宿家庭自己已经有几个孩子，可能没有太多时间可以照顾你的孩子。第三种寄宿家庭是孩子都已经长大，离开家，自己也已经退休的家庭。这些人多半年纪较大，但是还愿意接受国际学生，了解不同的文化。他们跟一般的美国家庭比，生活没有那么忙，所以有更多的时间可以照顾学生，而且这些老人的生活比较健康，也喜欢安静，所以孩子在这种家庭可以专心学习。要是你的孩子喜欢热闹，可能就不适合这样的家庭。",
      "Do you want your child to study abroad? Then finding a homestay family that suits your child is a very important step for studying smoothly abroad. According to your child’s needs you can choose among the following kinds of homestay families. The first kind is a Chinese family, usually a Chinese family that has lived abroad for many years. Some parents feel that if the child lives in a Chinese family the language, culture and living habits are similar, so communication and adaptation are fairly unproblematic, but they also worry that the child cannot practice English in a Chinese family and cannot truly get to know American culture. Another kind of homestay family is an ordinary American family, often a couple with two or three children living in a big house. If you choose such a family, the child can not only learn the language and learn the local culture with the homestay family but also live like brothers and sisters with the family’s other children, which many only children cannot experience at home; but because the family already has several children, they may not have much time to look after your child. The third kind of homestay family is a family whose children have grown up and left home and who have retired themselves. These people are mostly older but still willing to accept international students and learn about different cultures. Compared with ordinary American families they are less busy, so they have more time to look after the student, and the old people live a healthier life and like quiet, so the child can concentrate on study in this kind of family. If your child likes liveliness, it may not suit such a family. (source note: adapted from a homestay website)")
MM = table(["寄宿家庭", "好处", "坏处"], [["华人家庭", "语言、文化和生活习惯差不多，沟通和适应没问题", "不能锻炼英文，也不能真正认识美国文化"], ["一般美国家庭", "可以学习语言，了解当地文化，像兄弟姐妹一样生活", "家里已经有几个孩子，没有太多时间照顾"], ["退休老人家庭", "有更多时间照顾学生，生活健康安静，可以专心学习", "年纪较大，不适合喜欢热闹的孩子"]],
           title="Activity 2A: my mind map as a table (the book’s mind map is blank)", say=[0, 1, 2])
EM = ("亲爱的爸妈：来美国留学已经三个月了，现在才有时间给你们写信。虽然你们从小让我上英语班为我出国做准备，可是到了国外我才发现自己没有办法马上和当地人交流。现在我天天和住宿家庭的爸妈人说英文。他们人很好，但在学习上完全不会帮助我，他们只管我的吃和住。但是每天吃的都是沙拉、汉堡或是热狗，我真不习惯。美国的学校虽然没有很多考试，但是每学期都有好几个报告要写，还要分小组和同学交流，还得自己上网学习。而且上课有时老师说得太快，我听不懂，也不好意思一直问。为了学习英语，你们帮我找了一所中国人很少的高中，但是因为我的英文不好，很难交到朋友。所以我现在的朋友都是几个跟我差不多的小留学生。唉，我真不知道为什么要出国，留在国内上学不是也很好吗？我想我的朋友，我想你们！你们的儿子，大明",
      "Dear Mom and Dad: It has been three months since I came to study in America, and only now do I have time to write to you. Although you had me attend English classes from childhood to prepare for going abroad, only when I got abroad did I find that I had no way of communicating with local people right away. Now I speak English every day with my homestay parents. They are very nice people, but they don’t help me at all with study; they only take care of my food and lodging. But every day what I eat is salad, hamburgers or hot dogs, and I really am not used to it. Although American schools don’t have many exams, every semester there are several reports to write, and I also have to exchange with classmates in groups and study online myself. And in class the teacher sometimes speaks too fast, I can’t understand, and I’m embarrassed to keep asking. To learn English you found me a high school with few Chinese people, but because my English is not good it’s hard to make friends, so my friends now are a few young students like me. Sigh, I really don’t know why I should go abroad; wouldn’t staying at home to go to school be good too? I miss my friends, I miss you! Your son, Daming. (the book prints 住宿家庭的爸妈人说英文 with a stray 人; kept as printed. The book’s header lines TO, CC and Subject are blank.)")
EA = [("他来美国三个月了，爸妈从小让他上英语班，为出国做准备。", "4A-1 (my answer): He has been in America for three months, and his parents had him attend English classes from childhood to prepare for going abroad."),
      ("他们人很好，但在学习上完全不会帮助他，只管他的吃和住。", "4A-2 (my answer): They are very nice but don’t help him with study at all; they only take care of his food and lodging."),
      ("没有很多考试，但是要写很多报告，要分小组交流，还得自己上网学习，老师有时说得太快。", "4A-3 (my answer): There are not many exams but many reports to write, group work, and online self-study, and the teacher sometimes speaks too fast."),
      ("他觉得很不习惯，很难交到朋友，不知道为什么要出国。", "4A-4 (my answer): He feels very unsettled, finds it hard to make friends, and doesn’t know why he should go abroad.")]
RE = [("亲爱的大明：收到你的信，我们很想你。刚到国外，一切都不容易，慢慢就会适应的。吃的方面，你可以自己学着做几个中国菜。学习上，你可以多问老师，也可以找同学一起学习。我们每个周末都会跟你视频聊天。你是个好孩子，我们相信你。爸爸妈妈", "A reply from the parents (my sample): Dear Daming: Receiving your letter, we miss you very much. Just arrived abroad, nothing is easy, and you will adapt slowly. For food, you could learn to cook a few Chinese dishes yourself. In study, you can ask the teacher more and also find classmates to study with. Every weekend we will video chat with you. You are a good child and we believe in you. Dad and Mom")]
TL2 = [("第一、不要让孩子在读十一年级、十二年级时出国，如果孩子已经上十二年级，就读完高中再出国。因为高中最后两年，生活和学习的压力特别大，那个时候出国会遇到比较多的问题，而且新来的学生，要适应新的环境、文化，而且在美国读书并不轻松，特别是想进好学校，需要很大的努力。不要觉得来美国就不用吃苦、不用努力。", "First: don’t let the child go abroad in the 11th or 12th grade; if the child is already in the 12th grade, finish high school before going abroad. Because in the last two years of high school the pressure of life and study is especially great, going abroad then runs into more problems, and a newly arrived student has to adapt to a new environment and culture; moreover studying in America is not easy, especially if you want to enter a good school, which takes great effort. Don’t think that coming to America means no hardship and no effort is needed. (the book writes 11 and 12 in digits)"),
       ("第二、很多中国大陆的留学公司，没来过美国，也不了解美国。他们有时候会把学生安排到很“乡下”的地方，真到了这种地方，孩子会生活得很辛苦。美国人不重视吃，大多不会花太多时间在做饭上，更不会特别为孩子做中餐、注意孩子的营养。中国孩子吃不惯美国人做的西餐，在外面有时候也买不到中餐，自己又不能开车，有的学校连热食都不卖，天天吃冷餐，真的会过得非常辛苦。", "Second: many study-abroad companies in mainland China have never been to America and don’t know America. They sometimes arrange students in very “rural” places, and once they are really in such a place the children live a hard life. Americans don’t attach importance to eating, mostly don’t spend much time cooking, and especially won’t cook Chinese food for the child or watch the child’s nutrition. Chinese children can’t get used to the Western food Americans make, sometimes can’t buy Chinese food outside, can’t drive themselves, and some schools don’t even sell hot food, so eating cold meals every day really is very hard."),
       ("最后，父母最好多和孩子沟通，交流，常打电话、视频了解孩子在国外的生活，也能让孩子知道虽然分隔两地，父母还是很关心他或她。这样，孩子要是有什么事，也不会把事放在心里，不敢让父母知道，或是因此交上坏朋友，养成坏习惯。", "Finally, parents had better communicate and exchange more with the child, often calling and video chatting to learn about the child’s life abroad, which also lets the child know that although separated in two places the parents still care about him or her. This way, if something happens to the child, he or she won’t keep it in his or her heart and not dare let the parents know, or make bad friends and form bad habits because of it. (the book writes 他/她; here 他或她; source note: adapted from a newspaper website)")]
SG = [("不要让孩子在十一年级、十二年级时出国，最好读完高中再出国。", "Suggestion 1 (my list): Don’t let the child go abroad in grades eleven and twelve; it is best to finish high school first."),
      ("不要让留学公司随便安排很“乡下”的地方，要了解吃的和交通问题。", "Suggestion 2 (my list): Don’t let a study-abroad company arrange a very “rural” place carelessly; look into the food and transportation problems."),
      ("多和孩子沟通，常打电话、视频，让孩子知道父母很关心他或她。", "Suggestion 3 (my list): Communicate more with the child, call and video chat often, and let the child know the parents care.")]
L6 = lesson(
    "Lesson 26 Presentation 1 skill integration: homestay families, a letter home and a host’s advice",
    "寄宿家庭 华人家庭 美国家庭 退休的家庭 · 大明的信 · 寄宿家庭的妈妈的建议 · 十一年级 十二年级",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Listening and Speaking)",
             "A. Listen to a reporter interview a homestay host, then write a summary of the interview. B. Share your summary with your partner in Chinese. C. Listen to the dialog again and extract the EEIs. D. Role-play the interview with the information you have gathered. Switch roles and repeat. (Audio; the script is not in the book.)",
             tables=[SK1]),
        card("Skill Integration, Activity 2 (Reading, Writing, Speaking and Listening)",
             "A. Read the following passage from a homestay business, then fill in the mind map below in Chinese (寄宿家庭: 好处 and 坏处 for each of three kinds). B. Explain your mind map to a partner in Chinese. C. In Chinese, discuss with your partner what kind of homestay family you would choose for your children, and why.",
             tables=[MM], examples=[D(*HS)]),
        card("Skill Integration, Activity 3 (Listening, Writing, Speaking and Reading)",
             "A. Pair up. Two students on a talk show share their experiences studying in the U.S. Listen to the first student’s experiences while your partner listens to the second student. Fill in the table (Student 1 and Student 2: Who; Life abroad; Feelings about their experience). B. In Chinese, tell your partner about the student experience you listened to, then fill in the rest of the table with the other student’s information. C. Read the scripts to check your information. (Audio; the scripts are not in the book.)"),
        card("Skill Integration, Activity 4 (Reading, Speaking and Writing)",
             "A. Read the following email from a Chinese student to his parents, then answer the questions. 1. What do the first two lines of the email tell you about the student? 2. How does his homestay family treat him? 3. What are three EEIs about his school life? 4. How does he feel about his study abroad experience overall? B. In Chinese, discuss with a partner how to help 大明 adjust to his life abroad. C. Write a return email as 大明’s parents to comfort and advise him. The email, then my answers and a sample reply:",
             examples=[D(*EM)] + [D(z, e) for z, e in EA] + [D(*RE[0])]),
        card("Skill Integration, Activity 5 (Reading, Speaking and Listening)",
             "A. Read the passage below, then list the suggestions (建议 jiànyì) the homestay host provides to parents who wish to send their children to school in the U.S. B. Share your list with your partner in Chinese. The passage: 寄宿家庭的妈妈王美香对要送孩子出国的中国家长们有几点建议：",
             examples=[D(*x) for x in TL2] + [D(z, e) for z, e in SG]),
    ],
    exercises=[
        M("Which is the first kind of homestay family?", "A Chinese family", ["A retired family", "An ordinary American family", "A hotel"], "第一种是华人家庭."),
        M("What is the worry about a Chinese homestay family?", "The child can’t practice English or get to know American culture", ["It is too expensive", "It is too noisy", "It is too far"], "不能锻炼英文."),
        M("What can children do in an ordinary American family?", "Live like brothers and sisters with the other children", ["Live alone", "Cook for the family", "Work for money"], "像兄弟姐妹一样生活."),
        M("What is the possible problem with a family that already has children?", "They may not have much time to look after your child", ["They are too rich", "They speak Chinese", "They have no kitchen"], "没有太多时间照顾."),
        M("Who are the third kind of homestay hosts?", "Retired people whose children have left home", ["Young couples", "Students", "Teachers"], "已经退休的家庭."),
        M("What is Daming’s complaint about his homestay family?", "They only take care of his food and lodging, not his study", ["They are rude", "They are too strict", "They never speak"], "只管我的吃和住."),
        M("What food is Daming not used to?", "Salad, hamburgers and hot dogs", ["Rice", "Noodles", "Soup"], "沙拉、汉堡或是热狗."),
        M("Why is it hard for Daming to make friends?", "His English is not good and there are few Chinese at the school", ["He is too busy", "He is too shy", "He has no phone"], "我的英文不好，很难交到朋友."),
        M("When does the host say a child should not go abroad?", "In the 11th or 12th grade", ["In the 1st grade", "In the 5th grade", "After college"], "不要让孩子在读十一年级、十二年级时出国."),
        M("What is the host’s last suggestion?", "Communicate more with the child by phone and video", ["Send more money", "Visit once a year", "Change the school"], "多和孩子沟通."),
        F("你们帮我找了一所中国人很少的高中，但是因为我的英文不好，很难交到朋___。", "友", PART, "朋友: friends."),
        F("他们只___我的吃和住。", "管", PART, "只管: only take care of."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese
UP1 = ("英国的寄宿学校通常是小班上课，有很好的设施和质量，所以寄宿学校的毕业生常常能顺利进入有名的大学学习。而且学生住在学校里，在学习上、生活上都有人照顾，家长可以比较放心。另外，寄宿学校提供多种多样的课，除了上课以外，还有很多课外活动，比方说划船、骑马等，可以发展学生的兴趣爱好。周末的时候，学校还会安排学生看演出，参观各地的名胜古迹或博物馆，丰富孩子的生活。最后，寄宿学校有来自各国的学生，学生可以和别的同学交流，了解不同的文化，还可以互相学习、互相帮助。但是寄宿学校通常是私立的，所以学费比较贵，还有要进寄宿学校也不容易，有很多条件，如果你的成绩不好，很难进到好的寄宿学校。另外，寄宿学校多半在乡下，虽然风景很美，但是交通和生活会有一些不方便。",
       "Passage 1, British boarding schools: British boarding schools usually have small classes and have very good facilities and quality, so graduates of boarding schools can often enter famous universities smoothly. Also, students live at school and are looked after in study and life, so parents can feel fairly relieved. In addition, boarding schools offer a variety of courses; besides classes there are many extracurricular activities, such as rowing and horse riding, which develop students’ interests and hobbies. At weekends the school also arranges for students to watch performances and visit scenic spots, historic sites or museums, enriching the children’s life. Finally, boarding schools have students from all countries, who can exchange with other classmates, learn about different cultures and learn from and help each other. But boarding schools are usually private, so the tuition is rather expensive; also getting into a boarding school is not easy and has many conditions, and if your grades are not good it is hard to get into a good one. In addition, boarding schools are mostly in the countryside, and although the scenery is beautiful, transportation and daily life are somewhat inconvenient.")
UP2 = ("很多父母会安排让孩子住在美国人的寄宿家庭，这样孩子上课还有下课都得讲英文，孩子的语言能力在很短的时间会有很大的进步。因为是住在美国人的家里，孩子天天和他们生活在一起，看电视聊天，参加家庭聚会，和他们一块过节等，这样可以比较快了解美国文化和适应当地的生活。如果寄宿家庭也有孩子，寄宿家庭的兄弟姐妹还可以在生活上、学习上帮助他或她。另外，寄宿家庭平常会让孩子自己收拾房间，洗碗，洗衣什么的，这些事可以训练孩子自己照顾自己的能力。但是对孩子来说，外国家庭的生活习惯和饮食习惯可能很不一样，有时也会有沟通上的困难，适应起来会不太容易。还有，寄宿家庭的环境和质量都不大一样，也不能像寄宿学校提供二十四小时的照顾，父母可能会比较担心孩子安全的问题。",
       "Passage 2, American homestay families: Many parents arrange for their children to live in American homestay families, so the children must speak English both in and after class, and their language ability will improve greatly in a very short time. Because they live in Americans’ homes, the children live with them every day, watching TV and chatting, joining family gatherings and celebrating holidays together, so they can understand American culture and adapt to local life more quickly. If the homestay family also has children, the family’s brothers and sisters can also help him or her in life and study. In addition, homestay families usually let the child tidy the room, wash dishes and do laundry, which can train the child’s ability to look after himself or herself. But for the child, the living and eating habits of a foreign family may be very different, there may sometimes be communication difficulties, and adapting may not be easy. Also, the environment and quality of homestay families are not all the same, and they cannot provide twenty-four-hour care as a boarding school does, so parents may worry more about the child’s safety. (the book writes 24 in digits and 他/她, written 他或她 here)")
PC = table(["", "Pros (mine)", "Cons (mine)"], [["英国的寄宿学校", "小班上课，设施和质量好，有人照顾，课外活动多，同学来自各国", "学费贵，不容易进，多半在乡下，交通不方便"], ["美国的寄宿家庭", "语言进步快，了解美国文化，兄弟姐妹帮助，训练自理能力", "生活和饮食习惯不同，沟通有困难，环境不一样，安全问题"]],
           title="Activity 1: the pros and cons of the two passages (the book’s table is blank; mine is below)")
AD3 = [("在孩子出国前，父母可以为他们做好一些准备：", "Advice on preparing children for study abroad: Before the child goes abroad, parents can make some preparations: (the four numbered points follow; source note: adapted from a study-abroad website)"),
       ("第一，锻炼孩子一个人生活的能力。在平时的生活中就要多让孩子自己动手，例如让他们自己整理自己的房间，收拾自己的学习用品，让他们自己做决定。如果有机会的话，还可以让他们参加夏令营等活动，这样不仅能锻炼他们自理的能力，还能让他们多和别人交流。", "1. Train the child’s ability to live alone. In everyday life let the child do things himself or herself more, for example tidy his own room, put away his own study things and make his own decisions. If there is a chance, you can also let them join summer camps and the like, which not only trains their self-care but also lets them communicate more with others."),
       ("第二，提高外语交流能力。在平时的生活中让孩子多看一些国外的动画片，帮孩子报名上一些口语班，锻炼他们的开口说话的能力，或是在出国旅游的时候，让孩子多和外国人交流。", "2. Improve foreign-language communication ability. In everyday life let the child watch more foreign cartoons, sign the child up for some speaking classes to train the ability to open their mouths and speak, or, when traveling abroad, let the child communicate more with foreigners."),
       ("第三，了解国外文化，提高孩子的交往能力。出国前多让孩子了解国外的文化和习俗，例如外国的节日等，这样不但能增加孩子和外国孩子交流的话题，也能帮孩子更快地适应国外的生活。", "3. Learn about foreign culture and improve the child’s social ability. Before going abroad let the child learn more about foreign culture and customs, such as foreign festivals, which not only gives the child more topics for talking with foreign children but also helps the child adapt to life abroad faster."),
       ("第四，锻炼孩子主动学习的能力。在国内许多同学做完作业需要家长帮助检查，甚至需要家长陪着做作业。有不会的问题，总是马上问老师或问父母，自己不会主动去想。所以训练孩子的自我学习的能力，让他们学会利用电脑网路查找信息。这样，要是有不懂的生词或是有想要了解的知识，都能很快的找到答案。", "4. Train the child’s ability to learn on his own initiative. At home many students need parents to check their homework after finishing it and even need parents to sit with them while doing it. With problems they can’t do, they always ask the teacher or parents right away and don’t think actively themselves. So train the child’s self-study ability and let them learn to use computers and the Internet to look up information, so that if there are unknown new words or knowledge they want to learn, they can quickly find the answers.")]
LST = [("锻炼孩子一个人生活的能力，提高外语交流能力，了解国外文化，锻炼主动学习的能力。", "Activity 3D, my list of suggestions: train the ability to live alone, improve foreign-language communication, learn about foreign culture, and train active learning.")]
LT_ = ("我觉得低龄留学不适合每个孩子，特别是孩子的身心都还不成熟。刚来英语不好，自主生活、自主学习的能力也不行，再加上没有父母陪在身边，所以很多孩子开始逃学、打游戏，最后，来了美国几年什么也没学到。而且就算家长可以出来陪读，父母长期分隔两地，妈妈在国外陪读，爸爸在国内赚钱，时间久了，对父母的感情也不好。再说，就算父母能每天和孩子视频也比不上天天陪在身边。虽然低龄留学也有好处，比如能更好的学习英语，能早一点适应当地的生活。但是年纪小的孩子在国外久了，想法越来越西化，之后父母虽然还能用中文和孩子交流，但是沟通起来可能有困难。我知道很多父母把孩子送出来读初中或高中就是为了想逃离国内中考和高考的压力，但是在这里念高中一点也不轻松，再加上上面提到的一些问题，我觉得让孩子低龄留学这件事，父母得好好想清楚。",
       "李老师 is a counselor at a high school in New York. She talks in a program about her view of studying abroad at a young age. I think studying abroad at a young age is not suitable for every child, especially when the child’s body and mind are not yet mature. At the beginning the English is not good and the ability to live and study independently is also lacking; add to that no parents at the child’s side, so many children start skipping school and playing games, and in the end learn nothing after several years in America. And even if the parents can come out to accompany the studies, with parents separated for a long time, the mother accompanying abroad and the father earning money at home, after a long time the feelings toward the parents are also not good. Besides, even if the parents can video chat with the child every day, it is no match for being at the child’s side every day. Although studying abroad young has benefits, such as learning English better and adapting to local life earlier, children who are young and abroad for a long time become more and more Westernized in their thinking, and afterwards, although the parents can still talk with the child in Chinese, communication may be difficult. I know many parents send their children out to junior or senior high school to escape the pressure of the domestic high-school and college entrance exams, but studying high school here is not easy at all, and with the problems mentioned above, I think that as for letting a child study abroad young, parents must think it over carefully. (source note: adapted from a Q&A website)")
LK = [("她认为低龄留学不适合每个孩子，因为孩子的身心还不成熟。", "Activity 4A-1 (my answer): She thinks studying abroad young is not suitable for every child, because the child’s body and mind are not yet mature."),
      ("很多孩子逃学、打游戏，什么也没学到；父母分隔两地，感情不好；孩子越来越西化，沟通有困难。", "4A-2 (my answer): Many children skip school and play games and learn nothing; parents separated in two places have strained feelings; children become more Westernized and communication is difficult."),
      ("她觉得在美国念高中一点也不轻松。", "4A-3 (my answer): She thinks high school in America is not easy at all.")]
UV = table(["生词", "拼音", "English"], [["感情", "gǎnqíng", "emotions, feelings"], ["西化", "xīhuà", "westernized"]], title="Activity 4: new vocabulary", say=[0])
DB = table(["步骤", "辩论"], [["第一步", "Group 1 will brainstorm ideas, take notes and organize their arguments for children studying abroad. Group 2 will prepare to argue against studying abroad. (10 minutes)"], ["第二步", "Each group presents their argument while the other group takes notes."], ["第三步", "Each group then rebuts the other. (This step may be repeated several times.)"], ["第四步", "Each group delivers their summation and closing arguments."], ["第五步", "The teacher decides which group wins."]],
           title="Activity 4C: the debate steps (the book numbers them 1 to 5 in English; the Chinese step names are mine)", say=[0])
L7 = lesson(
    "Lesson 26 Presentation 1 using Chinese in context: boarding schools, advice and a counselor’s view",
    "英国的寄宿学校 · 美国的寄宿家庭 · 出国前的准备 · 低龄留学 · 李老师 · 西化 · 辩论",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. Read Passage 1 while a partner reads Passage 2, then fill in the table with the pros and cons of studying abroad in the country your passage addresses. B. In Chinese, share your findings with your partner and fill in the table for the other passage. C. In Chinese, discuss which country you would choose if you were a parent, and why. Passage 1: 英国的寄宿学校; Passage 2: 美国的寄宿家庭.",
             tables=[PC], examples=[D(*UP1), D(*UP2)]),
        card("Using Chinese in Context, Activity 2 (Listening and Speaking)",
             "A. Watch the VOA Chinese videos in the link and answer the questions. Clip 1 (0:59–1:36): 1. What is school life like for Chinese students in the U.S.? Clip 2 (4:42–5:32): 2. What contributions do Chinese students and their culture make to the school? Clip 3 (5:44–5:59): 3. What does the American student say about her Chinese friend? Clip 4 (6:00–6:17): 4. What does the American student say about his Chinese friend and their weekend activities together? B. Compare answers with a partner in Chinese. C. In Chinese, discuss with your partner any Chinese students you may have known in high school or college. (The videos and the link are not included.)"),
        card("Using Chinese in Context, Activity 3 (Listening, Speaking, Reading and Writing)",
             "A. Watch the talk show at the following link and perform the tasks below: Clip 1 (1:06–2:02): 1. Describe the interviewee. Clip 2 (6:27–7:43): 2. Describe her experience abroad. B. Share your work with a partner in Chinese. C. Read the following advice on how to prepare children for study abroad. D. Summarizing this advice, write a list of suggestions in Chinese and post it on a website. (The talk show is not included.) The advice and my list:",
             examples=[D(z, e) for z, e in AD3 + LST]),
        card("Using Chinese in Context, Activity 4 (Reading, Speaking, Listening and Writing)",
             "A. Read the following passage and answer the questions. 1. What does 李老师 think about Chinese children studying in the U.S., and why? 2. What are three examples she cites to support her opinion? 3. What does she think about the learning environment in U.S. high schools? B. Compare answers with a partner in Chinese. C. Form two groups for a Chinese debate on sending children abroad to study. The passage, my answers and the debate steps:",
             tables=[UV, DB], examples=[D(*LT_)] + [D(z, e) for z, e in LK]),
    ],
    exercises=[
        M("What are class sizes usually like in British boarding schools?", "Small", ["Very large", "Online only", "Mixed ages"], "小班上课."),
        M("What are two extracurricular activities named for British boarding schools?", "Rowing and horse riding", ["Football and tennis", "Singing and dancing", "Chess and cards"], "划船、骑马."),
        M("Why is tuition high at British boarding schools?", "They are usually private", ["They are far away", "They are new", "They are small"], "通常是私立的."),
        M("What is a main benefit of an American homestay family?", "The child’s language improves in a short time", ["It is free", "It has a pool", "It is near home"], "语言能力在很短的时间会有很大的进步."),
        M("How does a homestay family train a child’s self-care?", "By having the child tidy, wash dishes and do laundry", ["By cooking for the child", "By hiring a maid", "By banning chores"], "自己收拾房间，洗碗，洗衣."),
        M("What is one worry about homestay families?", "They cannot give twenty-four-hour care", ["They are too strict", "They speak Chinese", "They are too rich"], "不能提供二十四小时的照顾."),
        M("Which is NOT among the four ways to prepare a child for study abroad?", "Buy a car for the child", ["Train living alone", "Improve foreign-language ability", "Train active learning"], "The four points."),
        M("What does 李老师 think about low-age study abroad?", "It is not suitable for every child", ["It is suitable for everyone", "It is always best", "It is cheap"], "低龄留学不适合每个孩子."),
        M("What happens to many children without parents beside them?", "They skip school and play games", ["They win prizes", "They learn quickly", "They go home"], "开始逃学、打游戏."),
        M("What does 西化 mean?", "Westernized", ["Western food", "A westbound train", "Western holidays"], "西化."),
        F("特别是孩子的身心都还不成___。", "熟", PART, "成熟: mature."),
        F("父母长期分___两地，时间久了，对父母的感情也不好。", "隔", PART, "分隔: separate."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 26 Presentation 1 vocabulary", "27 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. Two cells of the table are broken by page layout in the PDF; the entries 困难, 陪读, 空中飞人 and 可不是嘛 are written out in full.", VOC1)

UNIT = unit("第二十六课 Presentation 1: 妞妞出国, 这么, 主题句, 比如, 可不是嘛", [L1, L2, L3, L4, L5, L6, L7, L8])
