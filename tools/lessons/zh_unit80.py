"""Unit 80: Lesson 26 (Study and Travel Abroad), Presentation 2: the history of overseas Chinese students (海归, 海龟, 海待, 海带) with its activities, the adverb 并,
the adverbs 多半(儿) and 大多, 被 Verb 为, 尽管 vs. 不管, the skill-integration tasks (applying abroad, returning students), the using-Chinese tasks (jokes, advice, three study-abroad options)
and the vocabulary list. Audio, pictures, charts, videos and websites are not included; numbers the book writes as digits are spelled out; answers the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l26_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('称为', 1, 'wei2'), ('选为', 1, 'wei2'), ('译为', 1, 'wei2'), ('翻译为', 2, 'wei2'), ('都得回国', 1, 'dei3'), ('都得努力', 1, 'dei3'), ('你得做', 1, 'dei3'), ('你得先', 1, 'dei3'), ('还得回答', 1, 'dei3'), ('行业', 0, 'hang2'), ('家长', 1, 'zhang3'), ('不适应', 2, 'ying4'), ('热和回', 1, 'he2'), ('钢琴弹了', 2, 'tan2'), ('觉得自己', 1, 'de5'), ('他得申请', 1, 'dei3')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. presentation 2 + activities 1-2
PP = [("九十年代以前，出国留学的机会并不多，而且多半儿都是公费留学，毕业后都要回国服务。后来，中国经济发展了，自费出国留学的越来越多。条件稍微好一点的家庭，不管多辛苦，父母都会想办法送孩子出国。",
       "Before the nineties there were not many chances to study abroad, and most of it was at public expense; after graduating, everyone had to return home to serve. Later, China’s economy developed, and more and more people went abroad to study at their own expense. Families in slightly better circumstances, no matter how hard it was, would find a way to send their children abroad. (translations in this card are mine; the book also prints the passage in traditional characters)"),
      ("开始的时候，大部分学生都是去读研究生。因为是自费的，而且当时国外的待遇和条件都比国内好得多，所以毕业后，许多人都选择留在国外生活和工作。可是也有一些人选择回国，他们被称为“海归”，“海龟”。在他们看来，国外的学位在国内很受欢迎，再加上会外语，不怕找不到好工作。但是由于国内的人才越来越多，“海归”们渐渐失去了以前的优势，所以有些回国以后找不到理想的工作，就成了“海待”，“海带”。",
       "At the beginning most students went to do graduate studies. Because it was at their own expense, and because the benefits and conditions abroad were then much better than at home, after graduating many people chose to stay abroad to live and work. But some people chose to return home, and they were called 海归 (returnees), or 海龟 (sea turtles, a pun on the same sound). In their view, foreign degrees were very welcome at home, and adding that they knew foreign languages, they were not afraid of failing to find a good job. But because the talent at home kept growing, the 海归 gradually lost their former advantage, so some, after returning, could not find an ideal job and became 海待 (waiting), or 海带 (kelp, again a pun). (the book prints the second name of each pair in brackets)"),
      ("尽管这样，中国的出国热还是没有降温。现在除了到国外读研究生以外，去读大学、中学、甚至小学的也越来越多，而且更多的人是为了体验生活，丰富自己的经历。",
       "Even so, China’s craze for going abroad has still not cooled. Now, besides going abroad to do graduate studies, more and more people go to university, middle school and even primary school, and more people do it to experience life and enrich their own experience.")]
TSF = table(["热", "生", "费"], [["热情", "学生", "学费"], ["热闹", "生活", "生活费"], ["热门", "研究生", "自费"], ["热水", "留学生", "公费"], ["出国热", "新生", "费用"], ["留学热", "生日", "花费"]],
            title="Activity 1A: words with 热, 生 and 费 (the class fills these in on a website; my lists)", say=[0, 1, 2])
K1 = [("一般来说，工资高的公司，工作的条件也不错。", "1. Generally speaking, at companies with high pay the working conditions are also good. (my key: 条件)"),
      ("每个公司都希望找到最好的人才，所以很多工作都需要经过面试。", "2. Every company hopes to find the best talent, so many jobs require an interview. (my key: 人才)"),
      ("在工作申请表上，告诉公司你的优势可以帮你加分。", "3. On a job application form, telling the company your strengths can earn you points. (my key: 优势)"),
      ("理想的工作和你真正找到的工作有时候会不一样。", "4. The ideal job and the job you actually find are sometimes different. (my key: 理想)"),
      ("在中国找到一个好工作需要一个好的学位。", "5. To find a good job in China you need a good degree. (my key: 学位)"),
      ("有研究生的学位对找工作有好处。", "6. Having a graduate degree is a benefit in looking for a job. (my key: 研究生)"),
      ("公费念书，国家除了会帮你付学费以外，有时候连生活费国家也包了。", "7. Studying at public expense, besides paying your tuition the state sometimes even covers your living expenses. (my key: 公费; the unused word is 毕业)")]
TL1 = table(["九十年代以前", "经济发展时期", "最近几年"],
            [["出国留学的机会并不多", "自费出国留学的越来越多", "国内的人才越来越多，海归渐渐失去优势"],
             ["多半儿都是公费留学", "条件好一点的家庭，不管多辛苦，都想办法送孩子出国", "有些海归找不到理想的工作，成了海待"],
             ["毕业后都要回国服务", "大部分学生读研究生，许多人毕业后留在国外", "出国热没有降温，去读大学、中学、甚至小学的越来越多"]],
            title="Activity 2B: my timeline (the book’s is blank; its first heading reads 90 年代以前)", say=[0, 1, 2])
A2 = [("中国学生出国留学从公费到自费，越来越多；有些人回国成了海归，也有些成了海待；出国热还没有降温。", "Activity 2A (my summary): Chinese students going abroad went from public to private expense and kept growing in number; some returned and became 海归, some became 海待; the craze has not cooled."),
      ("海龟就是回国的留学生，也叫海归。他们一开始很受欢迎，因为国外的学位在国内很受欢迎，他们又会外语，不怕找不到好工作。", "2C-1 (my answer): 海龟 are the students who returned home, also called 海归. At first they were very welcome, because foreign degrees were popular at home and they also knew foreign languages, so they were not afraid of failing to find a good job."),
      ("海带就是回国后找不到理想工作的留学生，也叫海待。因为国内的人才越来越多，海归渐渐失去了以前的优势。", "2C-2 (my answer): 海带 are returned students who could not find an ideal job after coming home, also called 海待. Because the talent at home kept growing, the 海归 gradually lost their former advantage."),
      ("九十年代以前出国留学的机会不多，多半儿是公费，毕业后都要回国。后来经济发展了，自费留学的越来越多，大部分去读研究生，许多人留在国外。也有一些人回国，叫海归。最近几年，国内人才越来越多，海归失去优势，有些成了海待。现在去国外读大学、中学、甚至小学的也越来越多。", "2D (my description): Before the nineties there were few chances to study abroad, mostly at public expense, and everyone had to return after graduating. Later, with economic development, more and more studied at their own expense, mostly graduate studies, and many stayed abroad. Some returned and were called 海归. In recent years, with more and more talent at home, the 海归 lost their advantage and some became 海待. Now more and more go abroad for university, middle school and even primary school.")]
L1 = lesson(
    "Lesson 26 Presentation 2: from 海龟 to 海带, the history of overseas Chinese students",
    "出国留学 · 公费 自费 · 海归 海龟 海待 海带 · 降温 · 理想的工作 · 学位 优势 人才",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up. Discuss the following questions with your partner. A. Would you like to study in China or Taiwan someday? Why or why not? B. Would you like to work in China or Taiwan someday? If so, what kind of work? C. What are the pros and cons to you studying abroad? (Four pictures are not included.)"),
        card("Presentation 2: 出国留学的历史", "The three paragraphs of the presentation.", examples=[D(*x) for x in PP]),
        card("Activity 1 (Speaking, Listening, Writing and Reading)",
             "A. In groups of three, brainstorm words, expressions and phrases containing each of the three characters 热, 生 and 费. Post your work on a class website. B. After you post your lists, guess the meanings of additional words your teacher supplies. C. Choose from the word bank below to fill in the blanks in the sentences. Use each word only once; there is one more word than you will need. Word bank: 理想, 学位, 公费, 研究生, 条件, 优势, 人才, 毕业. D. Compare answers with a partner, then translate the sentences. My lists and my key:",
             tables=[TSF], examples=[D(z, e) for z, e in K1]),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Global Listening: listen to Presentation 2 once through and write a summary of it. B. Detailed Listening: listen again and fill in the timeline with the relevant EEIs (九十年代以前, 经济发展时期, 最近几年). C. Perform the presentation with a partner, then answer individually: 1. Who are the 海龟? Why were 海龟 so welcome at first? 2. Who are the 海带? Why did 海龟 become 海带? D. Using your summary, timeline and answers, describe the historical changes to overseas Chinese students to your partner in Chinese. (Audio; my summary, timeline and answers follow.)",
             tables=[TL1], examples=[D(z, e) for z, e in A2]),
    ],
    exercises=[
        M("What kind of study abroad was mostly available before the nineties?", "Study at public expense", ["Study at one’s own expense", "Study in middle school", "Study with a scholarship from a company"], "多半儿都是公费留学."),
        M("What did students have to do after graduating in that period?", "Return home to serve", ["Stay abroad", "Find a job abroad", "Study again"], "毕业后都要回国服务."),
        M("What did most students study at the beginning?", "Graduate studies", ["Middle school", "Primary school", "Language classes only"], "大部分学生都是去读研究生."),
        M("Why did many people stay abroad at first?", "The benefits and conditions abroad were much better", ["They had no passports", "They disliked China", "Visas were free"], "待遇和条件都比国内好得多."),
        M("Who are the 海归?", "Students who returned home", ["Students who stayed abroad", "Foreign teachers", "Sea turtles"], "选择回国的人."),
        M("Why were 海归 welcome at first?", "Foreign degrees were popular and they knew foreign languages", ["They were rich", "They were famous", "They worked for free"], "国外的学位在国内很受欢迎，再加上会外语."),
        M("Why did some 海归 become 海带?", "The talent at home grew and they lost their advantage", ["They forgot Chinese", "They were too young", "They had no degree"], "国内的人才越来越多，渐渐失去了以前的优势."),
        M("What has not cooled down?", "The craze for going abroad", ["The weather", "The economy", "The tuition"], "出国热还是没有降温."),
        M("Which word fills “每个公司都希望找到最好的___”?", "人才", ["学位", "公费", "毕业"], "人才: talent."),
        M("Which word fills “理想的工作和你真正找到的工作有时候会不一样” as its first word?", "理想", ["条件", "优势", "研究生"], "理想: ideal."),
        F("条件稍微好一点的家庭，不管多辛苦，父母都会想办法送孩子出___。", "国", PART, "出国: go abroad."),
        F("毕业后都要回国服___。", "务", PART, "服务: serve."),
        F("海归们渐渐失___了以前的优势。", "去", PART, "失去: lose."),
    ],
)

# ------------------------------------------------------------------ 2. activities 3-4
CT = table(["连接词", "Meaning and use (my answers)"], [["不管", "no matter…; the next clause has 都 or 还是"], ["而且", "moreover; adds a further point"], ["由于", "because of; gives the reason, often with 所以 later"], ["尽管", "although; the next clause has 可是 and 却 or 还是"], ["所以", "so, therefore; gives the result"], ["除了", "besides, except; often with 以外 or 还"]],
          title="Activity 3A: the six connectors (my answers)", say=[0])
CK = ("最近几年，由于中国经济发展了，有越来越多父母选择让孩子出国留学。尽管不是所有的家庭都有好的经济条件，但是很多中国的父母不管多辛苦还是愿意把钱花在孩子的教育上。除了送孩子出国读研究生以外，不少家长让孩子去国外读高中、中学甚至小学。虽然孩子出国后不一定能马上适应当地的生活和学习，而且有外国的学位也不一定能找到理想的工作，但是对很多父母来说，出国念书不但可以让孩子多看看世界，还可以为孩子提供更多方面的发展。这些优势是在国内学习所没法比的。所以出国留学热一直没有降温。",
      "In recent years, because China’s economy has developed, more and more parents choose to let their children study abroad. Although not every family has good economic conditions, many Chinese parents, no matter how hard it is, are still willing to spend money on their children’s education. Besides sending children abroad for graduate studies, quite a few parents let their children go abroad for high school, middle school and even primary school. Although children abroad cannot necessarily adapt right away to local life and study, and moreover a foreign degree does not necessarily bring an ideal job, for many parents studying abroad can not only let the child see more of the world but also provide more all-round development. These advantages cannot be matched by studying at home. So the craze for studying abroad has never cooled. (my key: 由于, 尽管, 不管, 除了, 而且, 所以)")
TR = [("九十年代以前，出国留学的机会并不多，而且多半儿都是公费留学，毕业后都得回国服务。", "1. Before the nineties there were not many chances to study abroad, and most of it was at public expense; (they) all had to return home to serve after graduating. (the omitted subject is “the students”)"),
      ("因为是自费的，而且当时国外的待遇和条件都比国内好得多，所以毕业后，许多人都选择留在国外生活和工作。", "2. Because (it) was at their own expense, and because the benefits and conditions abroad were then much better than at home, after graduating many people chose to stay abroad to live and work. (the omitted subject of “was at their own expense” is “the study”)"),
      ("在他们看来，国外的学位在国内很受欢迎，再加上会外语，不怕找不到好工作。", "3. In their view, foreign degrees were very welcome at home, and (they) knew foreign languages besides, so (they) were not afraid of failing to find a good job. (the omitted subject is “they”)")]
TT = table(["时间词", "Meaning"], [["九十年代以前", "before the nineties"], ["后来", "later"], ["开始的时候", "at the beginning"], ["当时", "at that time"], ["毕业后", "after graduating"], ["回国以后", "after returning home"], ["渐渐", "gradually"], ["现在", "now"]],
          title="Activity 3D: the transitional time words in the presentation (my list)", say=[0])
SC = [("小王想出国留学。", "3E story chain (my sample), line 1: Xiao Wang wants to study abroad."), ("可是由于他家的经济条件不太好，所以他得申请奖学金。", "Line 2: But because his family’s economic conditions are not so good, he has to apply for a scholarship."),
      ("尽管申请很难，他还是每天努力准备。", "Line 3: Although applying is hard, he still prepares hard every day."), ("而且不管多忙，他都去图书馆学习。", "Line 4: Moreover, no matter how busy he is, he goes to the library to study.")]
NV = table(["生词", "拼音", "English"], [["读研", "dúyán", "do graduate studies"], ["考研", "kǎoyán", "test into grad school"]], title="Activity 4: new vocabulary", say=[0])
L2 = lesson(
    "Lesson 26 Presentation 2 activities: connectors, time words and a story chain",
    "不管 而且 由于 尽管 所以 除了 · 时间词 · 故事接龙 · 读研 考研",
    requires=[],
    cards=[
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Discuss the meaning and usage of the connectors with a partner. B. Fill in the blanks in the passage with the connectors above (there are six blanks, one for each connector). C. Translate the following sentences from the presentation. Pay attention to the omitted subject when translating. D. Scan the presentation and list the transitional time words. E. Pair up for 故事接龙: start a story with a sentence and then have your partner continue the story with their own sentence; switch back and forth until you have used at least four connectors. My answers:",
             tables=[CT, TT], examples=[D(*CK)] + [D(z, e) for z, e in TR] + [D(z, e) for z, e in SC]),
        card("Activity 4 (Listening and Speaking)",
             "A. Listen to two Chinese students talk about their experiences abroad, then answer the questions. Dialog 1: 1. What happened to the student after graduation? 2. To what does he attribute his present state? 3. What does his friend think about it? 4. How does the student now feel about studying abroad, and why? Dialog 2: 1. What has the student decided to do after graduation? 2. What is his friend’s concern? 3. What is the student’s rationale for his decision? 4. What are his plans for the future? B. Using your answers as a guideline, report on Dialog 1 to a partner in Chinese, while they report on Dialog 2. (Audio; the scripts are not in the book.)",
             tables=[NV]),
    ],
    exercises=[
        M("Which connector fits “最近几年，___中国经济发展了”?", "由于", ["除了", "不管", "所以"], "由于: because of."),
        M("Which connector fits “___不是所有的家庭都有好的经济条件，但是…”?", "尽管", ["而且", "所以", "由于"], "尽管: although."),
        M("Which connector fits “…父母___多辛苦还是愿意把钱花在孩子的教育上”?", "不管", ["而且", "除了", "所以"], "不管: no matter."),
        M("Which connector fits “___送孩子出国读研究生以外”?", "除了", ["不管", "所以", "尽管"], "除了…以外: besides."),
        M("Which connector fits “…不一定能马上适应，___有外国的学位也不一定能找到理想的工作”?", "而且", ["所以", "除了", "不管"], "而且: moreover."),
        M("Which connector fits “…没法比的。___出国留学热一直没有降温”?", "所以", ["尽管", "而且", "不管"], "所以: so."),
        M("What does 读研 mean?", "Do graduate studies", ["Read a book", "Test into grad school", "Study abroad for a week"], "读研: dúyán."),
        M("What does 考研 mean?", "Test into grad school", ["Do graduate studies", "Give an exam", "Fail a test"], "考研: kǎoyán."),
        M("Which is a transitional time word in the presentation?", "后来", ["因为", "可是", "但是"], "后来: later."),
        F("但是___于国内的人才越来越多，海归们渐渐失去了以前的优势。", "由", PART, "由于: because."),
        F("除了送孩子出国读研究生以___，不少家长让孩子去国外读高中。", "外", PART, "以外: besides."),
    ],
)

# ------------------------------------------------------------------ 3. adverb 并
BG0 = table(["结构", "用法"], [["S + 并 + 不 + Verb/Adj.", "并 goes before 不"], ["S + 并 + 没(有) + Verb/Adj.", "并 goes before 没"], ["S + V 得 + 并 + 不 + Adj.", "并 goes before 不 after the 得 complement marker"]], title="并 patterns")
BE = [("他的中文说得不好。", "Speaker’s observation or opinion: His Chinese is not good."), ("他的中文说得并不好。", "The speaker disagrees with those who think his Chinese is good: His Chinese is actually not good."),
      ("九十年代以前，出国留学的机会并不多。", "1. Before the nineties there were actually not many chances to study abroad."), ("年纪轻轻就出国留学并不容易，会有很多的困难。", "2. Going abroad to study at a young age is not easy at all and there will be many difficulties."),
      ("虽然我弹钢琴弹了十多年，但是我并不喜欢这种乐器。", "3. Although I have played the piano for more than ten years, I don’t actually like this instrument."), ("尽管我中文学了三年，但我的中文学得并不好。", "4. Although I have studied Chinese for three years, my Chinese is not actually good.")]
BA1 = [("你记错了，他并不是去年毕业的，是今年毕业的。", "1. (my key) You remembered wrong; he did not graduate last year, he graduated this year."), ("其实我去过法国，并没有去过意大利。", "2. (my key) Actually I have been to France; I have not been to Italy."),
       ("我们并不是男女朋友，我们只是好朋友。", "3. (my key) We are not boyfriend and girlfriend; we are just good friends."), ("谁说他跑得很慢，他跑得并不慢，比我们快多了。", "4. (my key) Who says he runs very slowly? He doesn’t run slowly at all; he is much faster than we are.")]
BD = dlg([("老师", "你这次考试没考好，我觉得你没有认真复习。", "Teacher (my sample role-play): You didn’t do well on this test; I think you didn’t review seriously."),
          ("学生", "我并不是没有复习，我每天都复习两个小时。", "Student: It isn’t that I didn’t review; I reviewed two hours every day."),
          ("老师", "可是你常常上课迟到。", "Teacher: But you are often late for class."),
          ("学生", "我并没有常常迟到，我只迟到过一次。", "Student: I am not often late; I have only been late once."),
          ("老师", "你晚上打游戏打得太晚了吧？", "Teacher: Don’t you stay up too late playing games at night?"),
          ("学生", "我并不是天天打游戏，只是周末玩一会儿。", "Student: I don’t play games every day, only a little at the weekend."),
          ("老师", "那你觉得为什么没考好？", "Teacher: Then why do you think you didn’t do well?"),
          ("学生", "因为这次的考试并不简单，很多同学都没考好。", "Student: Because this test was not easy; many classmates didn’t do well.")])
L3 = lesson(
    "Lesson 26 Presentation 2 grammar: the adverb 并 for emphasizing disagreement",
    "并不 并没有 说得并不好 · 机会并不多 · 并不容易 · 并不喜欢 · 学得并不好",
    requires=[],
    cards=[
        card("The Adverb 并",
             "The adverb 并 is placed before 不 or 没 to emphasize disagreement, point out a flaw in an argument, or reveal the truth about a situation.",
             tables=[BG0], examples=[D(z, e) for z, e in BE]),
        card("Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. Rewrite the following sentences using 并: 1. 你记错了，他是今年毕业的，不是去年毕业的。 2. 其实我去过法国，没有去过意大利。 3. 我们不是男女朋友，我们只是好朋友。 4. 谁说他跑得很慢，他跑得比我们快多了。 B. Read your sentences to a partner to compare work. My key:",
             examples=[D(z, e) for z, e in BA1]),
        card("Activity 2 (Speaking and Listening)",
             "Role-play with a partner using 并. Switch roles and repeat. Scenario: During counseling, your teacher (partner) pinpoints some bad habits that led to your failing a test. Defend yourself and provide your side of the story. My sample dialog:",
             examples=BD),
    ],
    exercises=[
        M("Where is 并 placed?", "Before 不 or 没", ["After 了", "At the end of the sentence", "Before the subject"], "并 goes before 不 or 没."),
        M("What does 并 emphasize?", "Disagreement, a flaw in an argument, or the truth", ["A past habit", "A polite request", "A future plan"], "Use of 并."),
        M("How does 他的中文说得并不好 differ from 他的中文说得不好?", "The speaker disagrees with those who think his Chinese is good", ["It means his Chinese is good", "It is a question", "It is a command"], "The speaker’s stance."),
        M("Which is correct?", "他并没有去过法国", ["他没并有去过法国", "他去并没过法国", "并他没有去过法国"], "并 + 没(有)."),
        M("Which is correct for “Actually I don’t like this instrument”?", "我并不喜欢这种乐器", ["我不并喜欢这种乐器", "我喜欢并不这种乐器", "并我不喜欢这种乐器"], "并 + 不 + Verb."),
        M("Which is correct for “my Chinese is not actually good”?", "我的中文学得并不好", ["我的中文学并得不好", "我的中文并学得不好得", "我的中文学得不并好"], "V 得 + 并 + 不 + Adj."),
        M("Which sentence rewrites “我们不是男女朋友” with 并?", "我们并不是男女朋友", ["我们是并不男女朋友", "并我们不是男女朋友", "我们不是并男女朋友"], "并不是."),
        M("In the role-play, what does 我并不是没有复习 mean?", "It isn’t that I didn’t review", ["I will review", "I forgot to review", "I reviewed a lot yesterday"], "Defending yourself."),
        F("九十年代以前，出国留学的机会___不多。", "并", PART, "并不多."),
        F("其实我去过法国，___没有去过意大利。", "并", PART, "并没有."),
    ],
)

# ------------------------------------------------------------------ 4. 多半(儿) / 大多
DB0 = table(["", "Parts of speech", "Meaning", "Form"], [["多半, 大多", "adverb", "mostly, largely; frequently, often; most likely, probably", "follows the subject and precedes the verb"], ["大部分, 大多数, 多数", "noun", "mostly, largely; most/majority of", "subject or object; may add another noun"]], title="多半, 大多 and 大部分, 大多数, 多数")
DE1 = [("到夏威夷游览的游客多半是日本人。", "1. (mostly) The tourists who visit Hawaii are mostly Japanese."), ("周末的时候我们全家人多半去爬山。", "2. (most of the time) At weekends our whole family mostly goes hiking."), ("这件事多半是他做的。", "3. (most likely) This was most likely done by him.")]
DE2 = [("老年人出国旅游大多喜欢参加旅行团。", "1. Old people traveling abroad mostly like to join tour groups."), ("大多数的中国人，特别是女人都不喜欢喝冰水。", "2. Most Chinese people, especially women, don’t like to drink iced water."), ("中国的人口大部分都在东部。很少人住在西部。", "3. Most of China’s population is in the east. Very few people live in the west.")]
DS3 = [("中文系的老师大多数说话很清楚，多半喜欢和学生聊天，大部分老师每天都准备很多练习。", "Activity 3A (my model sentences for the pattern, about the group 中文系的老师): Most Chinese-department teachers speak very clearly, mostly like chatting with students, and most teachers prepare many exercises every day."),
       ("中国人大多喜欢喝热水，多半不喜欢喝冰水，大部分人过春节都回家和家人团聚。", "(my model sentences, about the group 中国人): Chinese people mostly like to drink hot water, mostly don’t like iced water, and most go home to be with their family for the Spring Festival.")]
CH = table(["图表", "标题和内容"], [["图表一", "中国留学生毕业后回国原因: 无法融入外国文化, 没有得到签证, 更喜欢国内的环境, 家庭和爱情, 国内工作机会更多 (bar chart, scale 0 to 70)"], ["图表二", "中国学生留学目的地 (pie chart; the slices are not in the text)"], ["图表三", "中国游客2018年旅游目的地: 香港, 澳门, 泰国, 日本, 越南, 韩国, 美国, 台湾, 其他地区"], ["图表四", "2018年中国出境游客安排旅游路线的渠道: 网络, 旅行团, 亲友介绍, 其他 (bar chart, scale up to 160)"]],
           title="Activity 4A: the four charts (the bars and slices are graphics and are not in the text)")
CS = [("中国留学生毕业后回国，多半是因为国内工作机会更多。", "Chart 1 (my model sentence for the pattern; the book’s bars are not in the text): Chinese students returning after graduation do so mostly because there are more job opportunities at home."),
      ("中国学生留学，大多选择去英语国家。", "Chart 2 (my model sentence): Chinese students studying abroad mostly choose English-speaking countries."),
      ("大部分中国游客去亚洲的地方旅游。", "Chart 3 (my model sentence): Most Chinese tourists travel to places in Asia."),
      ("大多数中国出境游客通过网络安排旅游路线。", "Chart 4 (my model sentence): Most Chinese tourists going abroad arrange their route through the Internet.")]
L4 = lesson(
    "Lesson 26 Presentation 2 grammar: the adverbs 多半(儿) and 大多",
    "多半儿 大多 · 大部分 大多数 多数 · 多半是日本人 · 大多喜欢参加旅行团 · 看图表说话",
    requires=[],
    cards=[
        card("The Adverbs 多半(儿) and 大多",
             "Preceding the verb, the adverbs 多半(儿) and 大多 mean “mostly,” “most often,” “most of the time,” “most likely,” etc. Pattern: S + 多半(儿) / 大多 + V + O. 大部分, 大多数 and 多数 mean “most,” “for the most part,” “majority of,” etc. They differ from 多半(儿) and 大多 in that they are nouns and never mean “most often” or “most likely.”",
             tables=[DB0], examples=[D(z, e) for z, e in DE1 + DE2]),
        card("Activity 3 (Reading, Speaking, Listening and Writing)",
             "A. Pair up. Choose two groups of people from the options (国防语言学院的学生, 我们班的同学, 中文系的老师, 中国人/美国人, 陆军/海军/空军的军人), discuss them in Chinese, then list at least three of their common characteristics using 多半, 大多, 多数, 大多数 or 大部分. B. Post your list on a class website to share with the class. C. As a class, select the best list of characteristics. My model sentences:",
             examples=[D(z, e) for z, e in DS3]),
        card("Activity 4: 看图表说话 (Reading, Writing, Speaking and Listening)",
             "A. For each of the four charts, write a sentence generalizing its information using 多半, 大多, 多数, 大多数 or 大部分. B. Read your sentences to a partner to compare work. The charts are graphics, so only their titles and categories are given here; the sentences are models of the pattern, not readings of the book’s data.",
             tables=[CH], examples=[D(z, e) for z, e in CS]),
    ],
    exercises=[
        M("Where does 多半(儿) go in a sentence?", "Before the verb", ["At the end", "Before the subject", "After the object"], "Adverbs precede the verb."),
        M("Which of these is an adverb?", "大多", ["大部分", "大多数", "多数"], "多半 and 大多 are adverbs."),
        M("Which of these is a noun?", "大多数", ["多半", "大多", "多半儿"], "大部分, 大多数 and 多数 are nouns."),
        M("What can 多半 mean that 大部分 cannot?", "Most likely", ["The majority of", "Most of the people", "Most of the country"], "这件事多半是他做的."),
        M("What does 周末的时候我们全家人多半去爬山 mean?", "At weekends our whole family mostly goes hiking", ["We never go hiking", "We go hiking on Mondays", "We will go hiking tomorrow"], "Most of the time."),
        M("What does 这件事多半是他做的 mean?", "It was most likely done by him", ["It was never done", "He did it twice", "Nobody did it"], "Most likely."),
        M("Where does most of China’s population live, according to the book?", "In the east", ["In the west", "In the north only", "In the south only"], "中国的人口大部分都在东部."),
        M("Which does the book say most Chinese people, especially women, don’t like?", "Iced water", ["Hot water", "Tea", "Milk"], "不喜欢喝冰水."),
        F("到夏威夷游览的游客___半是日本人。", "多", PART, "多半: mostly."),
        F("老年人出国旅游___多喜欢参加旅行团。", "大", PART, "大多: mostly."),
    ],
)

# ------------------------------------------------------------------ 5. 被 Verb 为
BW0 = table(["结构", "用法"], [["Recipient of Action 被 (Agent) Verb 为", "formal equivalent of 被…叫做 and 被…称为, “to be addressed as”"], ["= Agent 把 Recipient + Verb 为", "the same meaning with 把"]], title="被 Verb 为")
BW1 = [("有一些人选择回国，他们被称为“海龟”。", "1. Some people chose to return home, and they were called “sea turtles.”"), ("人们把他们称为海龟。", "= People call them sea turtles."),
       ("乔治华盛顿被美国人称为国父。", "2. George Washington is called the father of the country by Americans."), ("美国人把乔治华盛顿称为国父。", "= Americans call George Washington the father of the country."),
       ("苏州和杭州被人们称为鱼米之乡。", "3. Suzhou and Hangzhou are called the land of fish and rice."), ("人们把苏州和杭州称为鱼米之乡。", "= People call Suzhou and Hangzhou the land of fish and rice.")]
BW2 = table(["结构", "意思", "例子"], [["R 被 (A) Verb 做", "R was Verb-ed as (colloquial)", "被叫做, 被称为"], ["R 被 (A) Verb 为", "R was Verb-ed as (formal)", "被选为, 被译为, 被当成, 被换成"], ["R 被 (A) Verb 成", "R was Verb-ed into (formal)", "被改成, 被翻译成"]], title="The three patterns")
BW3 = [("蒙特雷的人把国防语言学院叫做ＤＬＩ。", "1. People in Monterey call the Defense Language Institute DLI. (the book writes DLI in Latin letters, written here in full-width letters)"), ("广东菜也被称为粤菜。", "2. Guangdong food is also called Cantonese food."),
       ("他喜欢说笑话，他常被班上同学当成开心果。", "3. He likes telling jokes, and the classmates often regard him as the class clown."), ("她因为喜欢为同学服务，所以被选为班长。", "4. Because she likes serving her classmates, she was chosen as class monitor.")]
BW5 = [("一年级的学生被我们叫做新生。", "1. (my key) First-year students are called freshmen by us."), ("重庆被人们叫做中国的雾都。", "2. (my key) Chongqing is called the fog capital of China."),
       ("公司的桌椅都被老板换成新的。", "3. (my key) The company’s desks and chairs were all replaced with new ones by the boss."), ("这间美国名人住过的房子被人们改成博物馆。", "4. (my key) This house where an American celebrity lived was turned into a museum."),
       ("海明威的一本书的书名被人们翻译为“老人与海”。", "5. (my key) The title of one of Hemingway’s books was translated by people as “The Old Man and the Sea.” (the book adds the pinyin of 海明威 in brackets, left out here)")]
BW6 = [("北京被叫做中国的首都。", "Activity 6 (my samples; the five pictures are not included): Beijing is called the capital of China."), ("他被选为班长。", "He was chosen as class monitor."), ("这个房子被改成饭馆。", "This house was turned into a restaurant.")]
L5 = lesson(
    "Lesson 26 Presentation 2 grammar: 被 Verb 为 for “to be addressed as”",
    "被称为 被叫做 被选为 被译为 被当成 被换成 被改成 被翻译成",
    requires=[],
    cards=[
        card("被 Verb 为",
             "The formal equivalent of the colloquial 被…叫做 and 被…称为 means “to be addressed as.”",
             tables=[BW0, BW2], examples=[D(z, e) for z, e in BW1 + BW3]),
        card("Activity 5 (Reading, Writing, Speaking and Listening)",
             "A. Rewrite the following sentences using 被 Verb 成/做/为: 1. 我们把一年级的学生叫做新生。 2. 人们把重庆叫做中国的雾都。 3. 老板把公司的桌椅都换成新的。 4. 人们把这间美国名人住过的房子改成博物馆。 5. 人们把海明威的一本书的书名翻译为“老人与海”。 B. Read your sentences to a partner to compare work. C. Translate the sentences. My key and translations:",
             examples=[D(z, e) for z, e in BW5]),
        card("Activity 6: 看图说话 (Speaking and Listening)",
             "Pair up. Take turns making sentences about each picture using 被 Verb 成/做/为. (Five pictures are not included.)",
             examples=[D(z, e) for z, e in BW6]),
    ],
    exercises=[
        M("What does 被…称为 mean?", "To be addressed as", ["To be sent to", "To be afraid of", "To be late for"], "被称为: to be called."),
        M("Which is more formal?", "被称为", ["被叫做", "被喊做", "被说成"], "被…称为 is the formal one."),
        M("What is 人们把他们称为海龟 in the 被 pattern?", "他们被人们称为海龟", ["他们把人们称为海龟", "人们被他们称为海龟", "海龟被人们称他们"], "R 被 A Verb 为."),
        M("Which pattern means “was turned into”?", "被改成", ["被叫做", "被称为", "被选为"], "被改成: turned into."),
        M("Which fits “她被选___班长”?", "为", ["吗", "着", "过"], "被选为班长."),
        M("What does 广东菜也被称为粤菜 mean?", "Guangdong food is also called Cantonese food", ["Cantonese food is not Guangdong food", "Guangdong food is expensive", "Nobody eats Cantonese food"], "被称为."),
        M("What does 被当成开心果 mean?", "Be regarded as the class clown", ["Be given a fruit", "Be sent away", "Be asked a question"], "被当成."),
        M("Which sentence is the 被 version of “老板把公司的桌椅都换成新的”?", "公司的桌椅都被老板换成新的", ["老板被公司的桌椅换成新的", "老板的桌椅被公司都换", "新的桌椅把老板换成"], "被换成."),
        F("苏州和杭州被人们称___鱼米之乡。", "为", PART, "被称为: be called."),
        F("这间名人住过的房子被人们改___博物馆。", "成", PART, "被改成: be turned into."),
    ],
)

# ------------------------------------------------------------------ 6. 尽管 vs. 不管
JG0 = table(["结构", "用法"], [["尽管 + S + V + O, 可(是) S + (却 or 还[是]) + Focus of the Sentence", "尽管 means “although” or “even though”; stronger than the colloquial 虽然; at the beginning of the sentence; 可(是) and 却 or 还(是) in the next clause stress the focus on the latter clause"]], title="尽管…可是")
JG1 = [("尽管中文很难学，可我却对中文最感兴趣。", "1. Although Chinese is hard to learn, I am most interested in Chinese."), ("尽管购物是中国人出国旅游的重要活动，可中国人买的东西却越来越多样。", "2. Although shopping is an important activity of Chinese people traveling abroad, the things Chinese people buy are more and more varied."),
       ("尽管上网点餐外送又方便又便宜，可是我还是喜欢在家自己做饭。", "3. Although ordering meals online for delivery is both convenient and cheap, I still like to cook at home myself."), ("尽管住民宿让你有家的感觉，可我还是喜欢旅馆的干净和舒适。", "4. Although staying in a homestay gives you the feeling of home, I still like the cleanliness and comfort of a hotel.")]
BU0 = table(["结构", "用法"], [["不管 + Question Word…, S + 都 + Focus of the Sentence", "no matter who/what/where/when/why/how"], ["不管 + 是 + Option A + 还是 + Option B, S + 都…", "no matter whether A or B"], ["不管 + Verb/Adj. + 不 + Verb/Adj., S + 都…", "no matter whether it is so or not"], ["不管 + 多 + Adj., S + 都…", "no matter how adjective"]], title="不管…都 (“no matter,” “regardless of,” “despite”; at the beginning of the sentence, followed by 都 or 还是 in the next clause to stress that the action or decision will not change)")
BU1 = [("不管花多少钱，她的父母都要送她出国留学。", "1. No matter how much money it costs, her parents will send her abroad to study."), ("不管在国内读研究生还是去国外读，学生都得努力学习才能毕业。", "2. Whether doing graduate studies at home or abroad, students have to study hard to graduate."),
       ("不管待遇、条件好不好，他还是决定回国工作。", "3. Whether the benefits and conditions are good or not, he still decided to return home to work."), ("不管中文有多难，我都要学会。", "4. No matter how hard Chinese is, I am going to learn it.")]
JB = table(["", "尽管…可是", "不管…都"], [["Type", "让步复句 (concessive compound sentence)", "条件复句 (conditional compound sentence)"], ["Form", "尽管 + Sentence, 可是 + S + (却/还)", "不管 + Question Word / Verb/Adj. + 不 + Verb/Adj. / A 还是 B / 多 + Adj., S + 都…"], ["Use", "emphasizes the focus on the subsequent clause", "stresses that the action or decision will not change"], ["Meaning", "although, even though", "no matter, regardless of, despite, etc."]], title="尽管 vs. 不管 (the comparison table)")
JK = [("不管离家多远，中国人都会在春节的时候回家和家人团聚。", "1. (my key: 不管) No matter how far from home, Chinese people will go home at the Spring Festival to reunite with their families."),
      ("尽管生活在国外多年，很多华人还是会庆祝许多传统的中国节日。", "2. (my key: 尽管) Although they have lived abroad for many years, many overseas Chinese still celebrate many traditional Chinese festivals."),
      ("尽管他家的经济条件不错，但是他还是半工半读赚他的学费。", "3. (my key: 尽管) Although his family’s economic conditions are good, he still works half-time and studies half-time to earn his tuition."),
      ("不管是参加旅行团还是自驾游，到各地看看都能了解世界，体验不同的生活和文化。", "4. (my key: 不管) Whether joining a tour group or driving yourself, going to see different places lets you understand the world and experience different lives and cultures. (the book prints stray spaces; removed)"),
      ("尽管他有名校的学位，可因他少了工作经验，还是没找到工作。", "5. (my key: 尽管) Although he has a degree from a famous school, because he lacks work experience he still hasn’t found a job. (the book prints 可因他; kept as printed)"),
      ("不管有没有醉酒，只要喝了酒就不应该开车。", "6. (my key: 不管) Whether drunk or not, as long as you have drunk alcohol you should not drive.")]
L6 = lesson(
    "Lesson 26 Presentation 2 grammar: 尽管 vs. 不管",
    "尽管…可是 · 不管…都 · 让步复句 · 条件复句 · 不管多难我都要学会 · 尽管上网点餐又方便又便宜",
    requires=[],
    cards=[
        card("尽管 vs. 不管",
             "Like 虽然, the conjunction 尽管 means “although” or “even though,” but is stronger in meaning than the more colloquial 虽然. It comes at the beginning of the sentence and is followed by 可(是) and 却 or 还(是) in the subsequent clause to further emphasize the focus on the latter clause. 不管 means “no matter (who/what/where/when/why/how),” “regardless of,” “despite,” etc. It comes at the beginning of the sentence and is followed by 都 or 还是 in the subsequent clause to stress that the action or decision in the initial clause will not change.",
             tables=[JG0, BU0, JB], examples=[D(z, e) for z, e in JG1 + BU1]),
        card("Activity 7 (Reading, Writing, Speaking and Listening)",
             "A. Complete the following sentences with 不管 or 尽管 (six blanks). B. Read your completed sentences to a partner, then translate them together. My key:",
             examples=[D(z, e) for z, e in JK]),
    ],
    exercises=[
        M("Which means “although” and is stronger than 虽然?", "尽管", ["不管", "所以", "除了"], "尽管."),
        M("Which means “no matter”?", "不管", ["尽管", "而且", "由于"], "不管."),
        M("What usually follows 不管 in the next clause?", "都 or 还是", ["可是", "所以", "但是"], "不管…都."),
        M("What usually follows 尽管 in the next clause?", "可(是), 却 or 还(是)", ["都", "因此", "除非"], "尽管…可是."),
        M("Which type of sentence is 不管…都?", "条件复句 (conditional)", ["让步复句 (concessive)", "因果复句 (causal)", "并列复句 (coordinate)"], "Types."),
        M("Which fits “___离家多远，中国人都会在春节的时候回家团聚”?", "不管", ["尽管", "而且", "所以"], "不管…多…都."),
        M("Which fits “___生活在国外多年，很多华人还是会庆祝传统节日”?", "尽管", ["不管", "除了", "由于"], "尽管…还是."),
        M("Which fits “___有没有醉酒，只要喝了酒就不应该开车”?", "不管", ["尽管", "虽然", "因为"], "不管有没有…"),
        F("不管中文有多难，我___要学会。", "都", PART, "不管…都."),
        F("尽管购物是中国人出国旅游的重要活动，可中国人买的东西___越来越多样。", "却", PART, "尽管…可…却."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
SKP = ("去美国念研究生不太难，但是你得做一些准备。首先，你得先决定你要去哪里念。一般来说公立学校比较便宜。私立学校比较贵。如果你选的学校在大城市，住宿费和生活费也会比较高。你可以多找几所学校，因为不是所有的学校申请了，都会被选上。第二步，找到了几家学校后，你可以上网查一下学校的信息，还有他们申请的要求。他们会告诉你需要准备哪些考试，要不要面试什么的。第三步就是准备好他们要的东西以后，你可以上网填他们的申请表，除了你的个人信息以外，你还得回答一些问题，让他们知道你为什么想申请这个学校，还有你的优势是什么。最后等几个月，他们就会寄信通知你是不是可以上他们的学校。",
       "Going to America for graduate school is not too hard, but you have to make some preparations. First, you have to decide where you want to study. Generally speaking, public schools are cheaper. Private schools are more expensive. If the school you choose is in a big city, lodging and living expenses will also be higher. You can look for several schools, because not every school you apply to will accept you. The second step, after finding a few schools, you can go online and look up the schools’ information and their application requirements. They will tell you which exams you need to prepare for and whether there is an interview and so on. The third step, after preparing what they want, you can fill in their application form online; besides your personal information you also have to answer some questions to let them know why you want to apply to this school and what your strengths are. Finally, wait a few months and they will send a letter to inform you whether you can attend their school.")
MM1 = table(["第一步", "第二步", "第三步", "第四步"], [["决定去哪里念：公立学校比较便宜，私立学校比较贵，大城市的住宿费和生活费比较高，多找几所学校", "上网查学校的信息和申请的要求：要准备哪些考试，要不要面试", "准备好他们要的东西，上网填申请表：个人信息，为什么想申请这个学校，自己的优势", "等几个月，学校寄信通知你可不可以上他们的学校"]], title="Activity 1A: my mind map for applying to a master’s program abroad (the book’s boxes are blank)", say=[0, 1, 2, 3])
MM2 = table(["第一步", "第二步", "第三步", "第四步"], [["听老师的要求，买好课本和用品", "上课以前先预习生词和课文", "上课认真听，积极说中文", "下课以后复习，考试以前多练习"]], title="Activity 1C: a sample mind map for preparing and studying in a language class (mine; the book asks about your own school)", say=[0, 1, 2, 3])
SKJ = table(["", "以前的留学生", "现在的留学生"], [["Purpose", "公费留学，毕业后回国服务", "体验生活，丰富自己的经历"], ["Level of Education", "研究生", "研究生、大学、中学、甚至小学"], ["Life Abroad", "许多人毕业后留在国外生活和工作", "孩子不一定能马上适应当地的生活和学习"]], title="Activity 3A: my table, taken from the Presentation 2 text and the Lesson 26 grammar passage (the book’s audio script is not in the text)")
SKV = table(["生词", "拼音", "English"], [["奖学金", "jiǎngxuéjīn", "scholarship"]], title="Activity 3: new vocabulary", say=[0])
G1 = [("以前的海归和最近几年的有什么不同？", "Group 1, Q1: What is the difference between the 海归 of the past and those of recent years?"), ("海归们的工资待遇比国内的求职者有优势。海归的平均工资比国内聘用的高二千五百元左右，但是大多数海归对理想的工资还是比公司愿意提供的高得多，所以会有一些海龟回国后好几个月都还没找到工作。", "Q3's answer B: The 海归’s pay and benefits have an advantage over domestic job seekers. The average salary of 海归 is about 2,500 yuan higher than that of those hired at home, but most 海归’s idea of an ideal salary is still much higher than what companies are willing to offer, so some 海龟 have not found a job for several months after returning."),
      ("你觉得海归回国的原因是什么？", "Group 1, Q2: What do you think the reasons for the 海归 returning are?"), ("我想主要是中国经济快速的发展，国内的工作机会多、而且工资和待遇条件也提高不少。另外，如果没有工作签证，要留在国外工作很困难。", "Q2's answer A: I think mainly China’s rapid economic development: there are many job opportunities at home, and pay, benefits and conditions have also improved a lot. In addition, without a work visa it is very hard to stay abroad to work."),
      ("海归们的工资待遇怎么样？", "Group 1, Q3: How are the 海归’s pay and benefits?"), ("最大的不同是以前回国的海归不多，很多都选择留在留学地工作和生活。现在回国的海归是出国的留学生人数的百分之八十。我想这是最大的不同。", "Q1's answer C: The biggest difference is that in the past not many 海归 returned and many chose to stay and work and live where they studied. Now the returnees are eighty percent of the number of students who went abroad. I think this is the biggest difference.")]
G2 = [("海归回国后常去哪里找工作？", "Group 2, Q1: Where do 海归 often go to look for work after returning?"), ("海归们回国后，多半会先选择在经济发展快，国际化的大都市找工作。其中北京、上海、成都是他们选择的前三名。另外，他们找的工作也集中在几个行业，比方说，通信、科技、电子和互联网等是几个比较热门的海归工作。当然除了一些大城市，也有越来越多的海归选择回家乡发展。", "Q1's answer B: After returning, 海归 mostly first choose to look for work in big cities with fast economic development that are international. Among them Beijing, Shanghai and Chengdu are their top three choices. In addition, the jobs they look for are concentrated in a few industries; for example, communications, technology, electronics and the Internet are some rather popular jobs for 海归. Of course, besides some big cities, more and more 海归 choose to return to their hometowns to develop."),
      ("从哪里回来的海归比较受欢迎？", "Group 2, Q2: Where do the returned students who are more welcome come from?"), ("从地区来看，欧美国家的留学生普遍更受老板的欢迎。从法国、美国、德国毕业的海归平均竞争力最高，英国海归排名第五。", "Q2's answer A: By region, students from Europe and America are generally more welcomed by bosses. 海归 who graduated from France, America and Germany have the highest average competitiveness, and the British 海归 rank fifth."),
      ("为什么有些海归成了海带？", "Group 2, Q3: Why did some 海归 become 海带?"), ("主要是因为海归们在国外学习多年，对国内的市场信息了解得不够，而且也不知道国内公司的需要。第二，很多海归们觉得自己有国外留学的优势，所以常希望找到职位较高或是工资较高的工作，但是不一定能顺利找到。第三，有些海归自我感觉良好，不仅常对公司或老板提出要求，而且对公司不满意的时候，容易换工作。", "Q3's answer C: Mainly because the 海归 studied abroad for many years, don’t know enough about domestic market information, and also don’t know the needs of domestic companies. Second, many 海归 feel they have the advantage of foreign study, so they often hope to find jobs with higher positions or higher pay, but cannot necessarily find them smoothly. Third, some 海归 have a good opinion of themselves, not only often making demands on companies or bosses but also changing jobs easily when they are not satisfied with the company. (source note: adapted from a news website)")]
MT = table(["Group 1", "Group 2"], [["1 → C", "1 → B"], ["2 → A", "2 → A"], ["3 → B", "3 → C"]], title="Activity 4A: the matching (my key, by content; the book prints the questions and answers in different orders)")
SKS = [("海归回国多半是因为国内经济发展快，工作机会多，而且没有工作签证很难留在国外。他们回国后多半先去北京、上海、成都这样的大城市找工作，常在通信、科技、电子和互联网行业。有些海归成了海带，因为不了解国内市场，要求太高，或者自我感觉太好。", "Activity 4B (my oral-report summary): 海归 return mostly because the economy at home is developing fast, there are many job opportunities, and without a work visa it is hard to stay abroad. After returning they mostly first go to big cities such as Beijing, Shanghai and Chengdu to find work, often in communications, technology, electronics and the Internet. Some become 海带 because they don’t know the domestic market, ask too much or think too well of themselves.")]
L7 = lesson(
    "Lesson 26 Presentation 2 skill integration: applying abroad, returning students and the 海归 questions",
    "申请研究生 · 四个步骤 · 奖学金 · 以前的留学生 现在的留学生 · 海归回国的原因 · 海归的工资待遇 · 为什么成了海带",
    requires=[],
    cards=[
        card("Skill Integration, Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. Read the passage, then create a mind map of the application process for a master’s degree program abroad (第一步, 第二步, 第三步, 第四步). B. Compare maps with a partner in Chinese. C. Create a similar mind map for class preparation and study at DLI (the Defense Language Institute). D. Based on your map, instruct your partner on how to prepare and study at DLI. Your partner will listen, write down the key steps, then read them back to you. The passage and my maps:",
             tables=[MM1, MM2], examples=[D(*SKP)]),
        card("Skill Integration, Activity 2 (Listening, Speaking, Writing and Reading)",
             "A. In groups of three, listen to three students discuss their studies abroad (海龟 1, 海龟 2, 海龟 3). Divide up the passages, one per student, and summarize their experiences. B. Report your summary in Chinese, then fill in the other tables with your partners’ summaries. C. Read all three audio scripts to check the accuracy of your group’s summaries. (Audio; the scripts are not in the book.)"),
        card("Skill Integration, Activity 3 (Listening, Speaking, Reading and Writing)",
             "A. Listen to an expert discuss overseas Chinese students past and present, then fill in the tables (以前的留学生 and 现在的留学生: Purpose, Level of Education, Life Abroad). B. Report your findings to a partner in Chinese. C. Read the script to check your work. D. Write a skit with your partner about these students, then perform it for the class. (Audio; my table is from the printed text.)",
             tables=[SKV, SKJ]),
        card("Skill Integration, Activity 4 (Reading, Speaking, Listening and Writing)",
             "A. Form groups of two. Both groups match their questions to the correct answers. B. Both groups summarize each of their answers and give an oral report on them in Chinese, taking notes on the other group’s report. C. Both groups prepare a presentation on 海归 and present it to the class. The questions and answers (the book prints the answers out of order; here each answer follows its question):",
             tables=[MT], examples=[D(z, e) for z, e in G1 + G2 + SKS]),
    ],
    exercises=[
        M("According to the passage, which schools are generally cheaper?", "Public schools", ["Private schools", "Schools in big cities", "Schools abroad only"], "公立学校比较便宜."),
        M("What is higher if the school is in a big city?", "Lodging and living expenses", ["Nothing", "Only tuition", "Only the exams"], "住宿费和生活费也会比较高."),
        M("What is the third step in applying?", "Fill in the application form online", ["Wait for a letter", "Look up schools", "Decide where to study"], "第三步…填他们的申请表."),
        M("What does the application form ask besides personal information?", "Why you want to apply and what your strengths are", ["Your bank balance", "Your passport number", "Your favorite food"], "为什么想申请这个学校，还有你的优势是什么."),
        M("What does 奖学金 mean?", "Scholarship", ["Tuition", "Allowance", "Salary"], "奖学金: jiǎngxuéjīn."),
        M("Why do 海归 return, according to the answer to question 2?", "China’s economy is developing fast and there are more job opportunities", ["Foreign food is bad", "They miss the weather", "They want to study again"], "中国经济快速的发展，国内的工作机会多."),
        M("What makes staying abroad hard, according to that answer?", "Having no work visa", ["Having no money", "Having no friends", "Having no degree"], "没有工作签证，要留在国外工作很困难."),
        M("Which three cities are the top choices for returning 海归?", "Beijing, Shanghai and Chengdu", ["Beijing, Tianjin and Xi’an", "Shanghai, Hangzhou and Nanjing", "Chengdu, Chongqing and Wuhan"], "北京、上海、成都."),
        M("Which students are generally most welcomed by bosses?", "Those from Europe and America", ["Those from Africa", "Those from Asia", "Those from Australia only"], "欧美国家的留学生普遍更受老板的欢迎."),
        M("Which is NOT one of the reasons some 海归 became 海带?", "They had no degree", ["They don’t know the domestic market enough", "They hope for jobs that are too high", "They feel too good about themselves"], "The three reasons."),
        F("你可以上网___他们的申请表。", "填", PART, "填: fill in."),
        F("他们就会寄信___知你是不是可以上他们的学校。", "通", PART, "通知: inform."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese
EX1 = [("“你是怎么从海龟变成海带的？”留学生笑着说：我们只是留学热和回国潮都赶上了。", "Exchange 1: “How did you turn from a sea turtle into kelp?” The student said with a smile: We just caught both the study-abroad craze and the wave of returning home. (my explanation: the joke is about students who studied abroad at the peak of the craze and then returned at the peak of the return wave, when jobs were scarce; source note: selected from a website)"),
       ("以前面试官知道你是海归：真厉害！现在面试官知道你是海归：真有钱！", "Exchange 2: In the past when the interviewer knew you were a 海归: Wow, impressive! Now when the interviewer knows you are a 海归: Wow, rich! (my explanation: a foreign degree used to show ability, but now it suggests mainly that the family could afford it)")]
QL = [("在国外学习和生活，我该怎么适应当地的饮食？", "Activity 2A (my sample questions): Studying and living abroad, how should I adapt to the local food?"), ("我怎么才能交到当地的朋友？", "How can I make local friends?"), ("如果听不懂老师说的话，我应该怎么办？", "If I can’t understand what the teacher says, what should I do?"), ("我想家的时候，怎么办？", "When I miss home, what should I do?"), ("留学期间我可以打工吗？", "Can I work part-time during my studies?")]
PB = ("出国前收拾行李是每个留学生都会遇到的问题。有些人担心到新的环境会不适应，所以带些自己常用的东西，像是小丽第一次去美国留学，她担心当地的饮食和口味会不习惯，就在行李中带了不少中国食品，打算到了美国自己做饭，结果下飞机过海关的时候，才发现很多东西特别是肉类都不能带进美国。所以出国前最好先查一下留学的目的地入境时的要求，才不会有麻烦。而且现在国外许多地区都有中国超市，大部分吃的、用的都可以买到，不用担心。",
      "Packing before going abroad is a problem every international student will meet. Some people worry they won’t adapt to a new environment, so they bring things they commonly use. For example, when 小丽 went to study in America for the first time, she worried she wouldn’t get used to the local food and taste, so she brought quite a lot of Chinese food in her luggage, intending to cook for herself in America; but when passing through customs after getting off the plane she found that many things, especially meat, could not be brought into America. So before going abroad it is best to first check the entry requirements of the study destination, so as not to have trouble. Moreover, many regions abroad now have Chinese supermarkets, and most things to eat and use can be bought, so there is no need to worry.")
PC2 = ("不管是不是第一次离家，自己一个人在国外留学生活，容易想家或有一些心理上的问题，在纽约读研究生的王同学就建议到新的环境，多交些新朋友，这样不但能丰富自己的留学生活，还能让自己从朋友那里体验到不同国家的文化。",
       "Whether or not it is the first time away from home, living and studying abroad alone makes it easy to be homesick or to have some psychological problems; 王 (a student doing graduate studies in New York) suggests that in a new environment you make more new friends, which can not only enrich your life abroad but also let you experience the cultures of different countries from your friends.")
PC3 = ("另一位在英国读大学的张同学建议，出国前在一些网路平台上找和自己读同一所大学的中国留学生，或是和大学的中国同学会联系，提前和他们交流一些留学信息，到了留学地，他们也能在生活上和学习上帮助你尽快适应当地的生活。",
       "Another student, 张, who studies at a university in Britain, suggests that before going abroad you look on some online platforms for Chinese students at the same university as you, or contact the university’s Chinese student association, and exchange some study-abroad information with them in advance; once you arrive, they can also help you in life and study to adapt to local life as soon as possible.")
PC4 = ("最后，虽然留学生出国留学的目的不太一样，但每个留学生都需要对以后有清楚的计划，想好要走的每一步。比方说，在英国读研究生的李同学知道自己留学是为了增加专业知识，这样回国找工作时才能有更多的选择。所以他在出国前就已经计划好，要用一年拿到学位，顺利毕业，然后找到实习机会，他说虽然平时学习压力大，但因为他有清楚的计划让他能更好的利用时间，也让他的留学生活变得更加丰富。",
       "Finally, although international students go abroad with different purposes, every one needs a clear plan for the future and to think through each step to take. For example, 李, who does graduate studies in Britain, knows he is studying abroad to increase his professional knowledge, so that he will have more choices when looking for work after returning. So before going abroad he had already planned to get the degree in one year, graduate smoothly and then find an internship; he says that although the study pressure is usually great, his clear plan lets him make better use of time and also makes his life abroad richer. (source note: adapted from a news website)")
AV = table(["Student", "Advice (my answers)"], [["小丽", "出国前先查一下留学目的地入境时的要求，不要带肉类等不能入境的东西"], ["王同学", "到新的环境多交新朋友，丰富留学生活，体验不同国家的文化"], ["张同学", "出国前在网路上找同校的中国留学生，或和中国同学会联系，提前交流留学信息"], ["李同学", "对以后有清楚的计划，想好要走的每一步"]], title="Activity 2B: the advice table (the book’s is blank)", say=[0, 1])
UP3 = [("孩子年龄越小，语言学习的速度也就越快，所以外语能力很快提高。再加上孩子如果在当地上高中，有了那里的学位，申请大学也比较容易。但是由于孩子年龄小，身心都不成熟，所以适应上会有比较多的困难。要是没人照顾，很容易交上坏朋友，养成坏习惯。父母会比较担心。", "Passage 1, applying to a high school abroad after middle school: The younger the child, the faster language learning is, so foreign-language ability improves quickly. In addition, if the child attends high school locally and has a degree from there, applying to university is also easier. But because the child is young and not mature in body and mind, there are more difficulties in adapting. If nobody looks after them it is easy to make bad friends and form bad habits. Parents will worry more."),
       ("高中毕业以后再留学，好处是孩子在国内高中已经学到一些基本知识，身心也基本成熟，所以适应上会比小留学生顺利一点。而且国外的大学教育有很多选择，除了公立学校以外，还有私立学校可选，学校的环境、设备都比较好，学习上也比较自由，学生可以按自己的兴趣发展。但是因为国内高中的生活比较紧张，除了准备高考以外，还要为出国做准备，孩子在这个时候申请留学会有不小的压力。", "Passage 2, applying to a foreign undergraduate program after high school: The benefit of studying abroad after high school is that the child has learned some basic knowledge in high school at home and is basically mature in body and mind, so adapting is a bit smoother than for young students. Also, university education abroad has many choices: besides public schools there are private schools to choose from, the schools’ environment and facilities are rather good, study is freer, and students can develop according to their own interests. But because life in high school at home is rather tense, besides preparing for the college entrance exam they must also prepare for going abroad, so applying to study abroad at this time brings no small pressure."),
       ("大学毕业后到国外读硕士，只需一到两年时间就能拿到学位，所以不需要花太多钱，而且要是成绩好，还有机会拿到奖学金，所以比较适合家庭条件没有那么好的留学生。另外，大学毕业生已经是个成熟的大人，适应国外的生活可能比小留学生快，但是语言能力可能没有小留学生提高得那么快。再加上留学时间短，要在当地找到工作留下来也不那么容易，所以留学后回国的人较多。", "Passage 3, applying to a foreign master’s program after university: Going abroad for a master’s after university takes only one to two years to get the degree, so you don’t need to spend too much money, and if your grades are good there is also a chance to get a scholarship, so it suits students whose family conditions are not so good. In addition, a university graduate is already a mature adult and may adapt to life abroad faster than young students, but language ability may not improve as fast as theirs. Add that the study time is short, so it is not so easy to find work locally and stay, and therefore more people return home after studying. (source note: adapted from a website)")]
PCT = table(["", "Pros (mine)", "Cons (mine)"], [["初中毕业申请国外高中", "语言学习快，外语能力很快提高；有当地的学位，申请大学比较容易", "身心不成熟，适应有困难；没人照顾容易交坏朋友、养成坏习惯；父母担心"], ["高中毕业申请国外本科", "已经学到基本知识，身心基本成熟，适应比较顺利；大学选择多，环境和设备好，学习自由", "国内高中生活紧张，要准备高考和出国，压力不小"], ["大学毕业申请国外硕士", "一到两年就能拿到学位，不需要花太多钱；成绩好可以拿奖学金；成熟，适应快", "语言能力提高没有那么快；留学时间短，在当地找工作留下来不容易"]], title="Activity 3A: the pros and cons of the three options (the book’s tables are blank)", say=[0, 1, 2])
L8 = lesson(
    "Lesson 26 Presentation 2 using Chinese in context: jokes, advice from four students and three study-abroad options",
    "海龟变海带 · 留学热 回国潮 · 收拾行李 · 新朋友 · 同学会 · 清楚的计划 · 初中 高中 大学毕业后留学",
    requires=[],
    cards=[
        card("Using Chinese in Context, Activity 1 (Reading, Speaking and Listening)",
             "A. Read the exchanges and explain the social phenomena they refer to. B. Discuss your explanations with a partner in Chinese. The exchanges and my explanations:",
             examples=[D(z, e) for z, e in EX1]),
        card("Using Chinese in Context, Activity 2 (Speaking, Listening, Writing and Reading)",
             "A. In groups of three, generate a list of questions in Chinese that Chinese students might have when studying abroad (five blanks). B. Read the post about four overseas Chinese students, then fill in the table with the advice derived from their experiences. C. Take turns with a partner summarizing or paraphrasing each student’s experience and advice in Chinese. D. Form groups of three. You play a U.S. university recruiter in China while your partners play two Chinese students. Conduct a Q&A session to provide them with practical information on attending your school. Switch roles and repeat. My questions, the post and my table:",
             tables=[AV], examples=[D(z, e) for z, e in QL] + [D(*PB), D(*PC2), D(*PC3), D(*PC4)]),
        card("Using Chinese in Context, Activity 3 (Reading, Speaking and Listening)",
             "A. In groups of three, read one passage each, then fill in the pros and cons of your respective study abroad option. B. Convey your pros and cons to your teammates in Chinese so they can fill in the other two tables. C. As a group, brainstorm in Chinese any other pros and cons you can think of for each option, then decide which option is the best choice. D. Report your decision and reasoning to the class in Chinese. The three passages and my table:",
             tables=[PCT], examples=[D(*x) for x in UP3]),
        card("Using Chinese in Context, Optional Activity 4 (Listening and Speaking)",
             "A. Watch videos with two overseas Chinese students at the links in the book, then answer the questions. Video 1 (2:47–5:20): 1. According to the student, how does education in the U.S. and China differ? 2. What does she think of her life in the U.S.? 3. What are her future plans? Video 2 (1:49–2:58): 1. What does the student find to be most difficult about living abroad and why? 2. What example does she cite to support her opinion? B. Compare answers with a partner in Chinese. C. Record a short video in Chinese on your experiences, challenges and strategies in learning Chinese, then post it on the class site. D. Watch all the videos, then discuss as a class which video you think is the best and why. (The videos and links are not included.)"),
    ],
    exercises=[
        M("How does the joke “留学热和回国潮都赶上了” turn a 海龟 into 海带?", "The student caught both the going-abroad craze and the returning wave", ["He missed both", "He learned to cook kelp", "He bought a turtle"], "Exchange 1."),
        M("How has the meaning of being a 海归 changed in Exchange 2?", "From “impressive” to “rich”", ["From “rich” to “impressive”", "From “poor” to “rich”", "It has not changed"], "真厉害 to 真有钱."),
        M("What did 小丽 bring in her luggage?", "A lot of Chinese food", ["Many books", "A bicycle", "Winter clothes only"], "带了不少中国食品."),
        M("What could not be brought into America?", "Many things, especially meat", ["Rice cookers", "Books", "Clothes"], "很多东西特别是肉类都不能带进美国."),
        M("What does 王同学 advise?", "Make more new friends in the new environment", ["Stay in your room", "Only talk to Chinese friends", "Call home hourly"], "多交些新朋友."),
        M("What does 张同学 advise doing before going abroad?", "Find Chinese students at the same university online", ["Buy a new phone", "Learn to drive", "Find a part-time job"], "在一些网路平台上找和自己读同一所大学的中国留学生."),
        M("What does 李同学 stress?", "A clear plan for every step", ["A large allowance", "A fast flight", "A big suitcase"], "对以后有清楚的计划."),
        M("What is a pro of applying abroad for high school after middle school?", "Foreign-language ability improves quickly", ["The tuition is free", "The child is more mature", "There is no pressure"], "外语能力很快提高."),
        M("What is a pro of a master’s degree abroad after university?", "It takes only one to two years", ["It takes six years", "It is always free", "It gives a job at once"], "只需一到两年时间就能拿到学位."),
        M("What is a con of going abroad after high school?", "Life in the domestic high school is tense and the pressure is not small", ["The child is too young", "There are no good schools", "It takes one year only"], "孩子在这个时候申请留学会有不小的压力."),
        F("出国前最好先查一下留学的目的地入境时的要___。", "求", PART, "要求: requirements."),
        F("要是成绩好，还有机会拿到奖学___。", "金", PART, "奖学金: scholarship."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 26 Presentation 2 vocabulary", "23 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. Several cells are broken by page layout in the PDF; the entries 降温, 回国, 海待, 公费 and 丰富 are written out in full. The entry -热 is a suffix and is listed here as 热.", VOC2)

UNIT = unit("第二十六课 Presentation 2: 海归和海带, 并, 多半儿, 被…为, 尽管和不管", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
