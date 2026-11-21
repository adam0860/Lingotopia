"""Unit 66: Lesson 23 (Study in China) Presentation 1 from the book's texts: the dialog on how to learn Chinese, the five activities (word
comparisons, word choice), 对…来说 and 对, the adverb 刚, the verbal phrase as subject, V着V着, the skill-integration passages (if I were a teacher), the
using-Chinese passages (Jack and Helen, seven principles) and the vocabulary list. Audio, pictures, videos and links are not included; answer keys
and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('干净', 0, 'gan1'), ('还有', 0, 'hai2'), ('还是', 0, 'hai2'), ('还不', 0, 'hai2'), ('得懂', 0, 'de5'), ('就得先', 1, 'dei3'), ('还要', 0, 'hai2'), ('感觉', 1, 'jue2'), ('教学生', 0, 'jiao1'), ('教了二', 0, 'jiao1'), ('我教她', 1, 'jiao1'), ('教他们', 0, 'jiao1'), ('说得好就', 1, 'de5')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. dialog
P1 = [("主持人", "大卫，琳达，你们中文学得都不错，今天请你们来和我们交流一下学中文的体会。大卫，你先说吧。", "David, Linda, you both do well in Chinese. Today we have invited you to share your experience of learning Chinese. David, you go first. (translation mine)"),
      ("大卫", "我觉得学好中文，兴趣最重要。我从小就对中国文化感兴趣，喜欢看中国的功夫片，所以我特别喜欢学中文。", "I think interest is the most important thing in learning Chinese well. Since I was little I have been interested in Chinese culture and liked watching Chinese kung fu movies, so I especially like learning Chinese."),
      ("主持人", "对很多人来说，中文是世界上最难学的语言，你觉得呢？", "For many people Chinese is the hardest language in the world to learn. What do you think?"),
      ("大卫", "刚开始是有点儿难，可是我很有兴趣，就不觉得那么难了，而且越学越爱学。", "At the beginning it was a bit hard, but I was very interested, so I didn’t find it so hard, and the more I learned the more I loved learning."),
      ("主持人", "琳达，你的中文说得非常好，一定也有很多学习体会吧？", "Linda, you speak very good Chinese; you must have a lot of learning experience too?"),
      ("琳达", "我觉得多说多练很重要。一开始就主动和中国人说中文，说不好，说不多都没关系，慢慢地你的中文表达能力就提高了。", "I think speaking and practicing a lot is important. Speak Chinese with Chinese people on your own initiative from the start; it doesn’t matter if you can’t speak well or much, and slowly your Chinese expression ability will improve."),
      ("大卫", "我觉得经常看真实语料，对学中文最有帮助。我常常看电影、新闻、综艺节目什么的。", "I think often watching authentic materials helps the most in learning Chinese. I often watch movies, news, variety shows and so on."),
      ("主持人", "真实语料很难，你能看得懂吗？", "Authentic materials are hard; can you understand them?"), ("大卫", "看不懂时我就看字幕，看着看着，也就看懂了。", "When I can’t understand, I read the subtitles, and as I watch, I come to understand."),
      ("琳达", "我再说一点，就是要常常学习别人的好方法。前两天，我在网上看到了一位美国老大爷谈学习中文的经验，讲得很好。", "Let me add one more point: you should often learn from other people’s good methods. A couple of days ago I saw online an old American man talking about his experience of learning Chinese, and he spoke very well."),
      ("大卫", "对，我也看过，他一共讲了七条经验，我都试了一下，效果还不错。", "Yes, I watched it too. He gave seven pieces of advice in all; I tried them all and the results were quite good."),
      ("主持人", "你们今天讲得都很好，希望能对学中文的朋友有一些帮助。谢谢你们。", "You both spoke very well today, and I hope it will help friends who are learning Chinese. Thank you.")]
L1 = lesson(
    "Lesson 23 Presentation 1: how we learn Chinese",
    "学中文的体会 · 兴趣最重要 · 多说多练 · 看真实语料 · 看着看着就看懂了",
    requires=[],
    cards=[
        card("Unit 4 overview and Lesson 23 objectives (在中国留学, Study in China)",
             "Lesson 23 topic: Studying in China. Tasks and functions: discuss the experience of learning Chinese; describe work and life in China; narrate life and studying in China. Grammar: 对…来说 vs. 对; the adverb 刚 (at first); the verbal phrase as subject; Verb + 着 + Verb + 着; the use of 每 as a demonstrative; the use of 的 (a soothing tone); the adverbs 差不多, 左右, 大约, 大概; the phrase 和…相比; 尽管…, 可是…; the expression …极了; the existence of 有 and 是; simple compound-complex sentences 多重复句. Area Studies: International Students in China. Upon completion of this lesson you will be able to: discuss the experience of learning Chinese; describe work and life in China via email; describe living and studying in China."),
        card("Getting Started",
             "Pair up and discuss: A. You have been learning Chinese for several months now. What do you think is the best way to learn Chinese? B. What do you think is the best way to practice speaking Chinese? C. Do you use authentic materials to learn Chinese? Can you name some Chinese websites or TV shows that are helpful for you? (Four photographs are not included.)"),
        card("Presentation 1: 学中文的体会", "The book also prints the dialog in traditional characters. The translations are mine.", examples=dlg(P1)),
    ],
    exercises=[
        M("What does David think is the most important thing in learning Chinese?", "Interest", ["Money", "Time", "A good teacher"], "学好中文，兴趣最重要."),
        M("What has David been interested in since he was little?", "Chinese culture and kung fu movies", ["Chinese food only", "Chinese cars", "Chinese sports"], "对中国文化感兴趣，喜欢看中国的功夫片."),
        M("How did David feel at the beginning?", "It was a bit hard", ["It was very easy", "He wanted to quit", "He did not study"], "刚开始是有点儿难."),
        M("What did he say about learning more and more?", "The more he learned, the more he loved learning", ["The more he learned, the more he hated it", "He forgot everything", "He learned nothing"], "越学越爱学."),
        M("What does Linda think is important?", "Speaking and practicing a lot", ["Reading only", "Writing characters", "Memorizing grammar"], "多说多练很重要."),
        M("What does Linda say about not speaking well or much?", "It doesn’t matter", ["It is shameful", "It must be corrected at once", "Never speak"], "说不好，说不多都没关系."),
        M("What authentic materials does David watch?", "Movies, news and variety shows", ["Only cartoons", "Only sports", "Only commercials"], "电影、新闻、综艺节目."),
        M("What does David do when he can’t understand?", "Reads the subtitles", ["Turns it off", "Asks a friend", "Looks up every word"], "看不懂时我就看字幕."),
        M("What did Linda see online a couple of days ago?", "An old American man talking about learning Chinese", ["A kung fu movie", "A news report", "A cooking show"], "一位美国老大爷谈学习中文的经验."),
        M("How many pieces of experience did the old man give?", "Seven", ["Five", "Three", "Ten"], "他一共讲了七条经验."),
        M("How were the results when David tried them?", "Quite good", ["Terrible", "Nothing happened", "He did not try"], "效果还不错."),
        F("我从小就对中国文化___兴趣。", "感", PART, "感兴趣: be interested in."),
        F("看不懂时我就看字幕，看着看着，也就看___了。", "懂", PART, "看懂: understand by watching."),
        F("一开始就主___和中国人说中文。", "动", PART, "主动: on one’s own initiative."),
    ],
)

# ------------------------------------------------------------------ 2. activities
CMP = table(["词", "意思和用法 (mine)"], [["体会", "insight gained from experience; 学中文的体会"], ["体验", "to experience firsthand; 体验中国人的生活"], ["经验", "accumulated experience; 有经验的老师"], ["效果", "effect, result of a method; 学习效果"], ["结果", "outcome, result of an event or exam; 考试的结果"], ["表达", "to express (thoughts, feelings in words); 表达能力"], ["表示", "to show, to mean; 表示爱, 表示什么意思"], ["方法", "method, way of doing; 学习方法"], ["办法", "way out, means to solve a problem; 想办法"], ["希望", "to hope (verb or noun); 希望你来"], ["愿望", "wish, desire (noun); 新年的愿望"]],
            title="Activity 3: comparing the five word groups (the book asks you to discuss; my notes)", say=[0])
A3 = [("比尔在中国住了一年多，对中国文化和中国人的生活有了很多体验。", "1a. Bill has lived in China for more than a year and has had many experiences of Chinese culture and the life of Chinese people. (key mine: 体验; 体会 would also be possible)"), ("大卫已经学了一年的中文，他会跟你谈谈他学中文的体会。", "1b. David has studied Chinese for a year and will talk with you about his insights into learning Chinese. (体会)"), ("高老师是一个非常有经验的老师，她教中文已经教了二十多年了。", "1c. Teacher Gao is a very experienced teacher; she has been teaching Chinese for more than twenty years. (经验)"),
      ("我用了琳达介绍的学习方法后，我的学习效果提高了很多。", "2a. After using the learning method Linda introduced, my learning results have improved a lot. (效果)"), ("期中考试的结果出来了。我考得不太好。", "2b. The mid-term exam results are out. I didn’t do very well. (结果)"),
      ("他常常给父母打电话或是发短信来表达对他们的爱。", "3a. He often phones or texts his parents to express his love for them. (表达)"), ("你知道这句话表示什么意思吗？", "3b. Do you know what this sentence means? (表示)"),
      ("那个美国老人介绍了很多学中文的好方法，我打算试一下。", "4a. That old American man introduced many good methods of learning Chinese and I plan to try them. (方法)"), ("你知道有什么办法能让学生们都喜欢学中文吗？", "4b. Do you know any way to make all students like learning Chinese? (办法)"),
      ("我希望下个月能在蒙特雷见到我的父母。", "5a. I hope to see my parents in Monterey next month. (希望)"), ("快过年了。你新年的愿望是什么？", "5b. The New Year is coming. What is your New Year’s wish? (愿望)")]
A4 = [("我喜欢看中国电影来学中文，看不懂时，就看一下字幕。", "1. I like to watch Chinese movies to learn Chinese; when I can’t understand, I look at the subtitles. (key mine: 字幕)"), ("近几年中国有很多搞笑的综艺节目，非常有意思，我很爱看。", "2. In recent years China has had many funny variety shows; they are very interesting and I love watching them. (综艺节目)"), ("想学好中文，应该多和老师和同学交流一下学习方法。", "3. If you want to learn Chinese well, you should talk with teachers and classmates about learning methods. (交流)"),
      ("李军每天起床后一定得看新闻，想了解世界上发生了什么事。", "4. Li Jun has to watch the news every day after getting up; he wants to know what is happening in the world. (新闻)"), ("保罗的中文非常好，也很热心，常常主动帮助其他同学。", "5. Paul’s Chinese is very good and he is warmhearted; he often volunteers to help other students. (主动)"), ("我最近说话能力比以前强了很多，因为我天天都练说话。", "6. My speaking ability has become much stronger than before recently, because I practice speaking every day. (能力)"),
      ("每天上课，老师都给我们听一个真实语料来训练我们的听力。", "7. Every class the teacher has us listen to one piece of authentic material to train our listening. (真实语料)"), ("由于我每天都听中文，我的听力水平有了很大的提高。", "8. Because I listen to Chinese every day, my listening level has improved greatly. (提高)")]
L2 = lesson(
    "Lesson 23 Presentation 1 activities: the table, word comparisons and word choice",
    "Activities 1 to 5 · 体会 体验 经验 · 效果 结果 · 表达 表示 · 方法 办法 · 希望 愿望",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Global listening: listen to Presentation 1 and answer: 1. What is the relationship between the three speakers? (a host and two guests, David and Linda) 2. What are they talking about? (their experience of learning Chinese). B. Detailed listening: listen again and, in the table (怎么才能学好中文, 关于真实语料, 关于美国老大爷; columns 大卫, 琳达, 他们怎么做的, 其他信息), write what David and Linda said (from the text: David: interest; authentic materials and subtitles; he tried the old man’s seven tips with good results. Linda: speak and practice a lot, take the initiative; learn from other people’s methods). C. Pair up, discuss and share. (Audio, not included.)"),
        card("Activity 2 (Listening, Writing and Speaking)",
             "Dialog 1: A. Listen and answer: 1. What did the two speakers chiefly discuss? 2. What does Peter say at the beginning about learning Chinese? How does he support his view? 3. What are Lisa’s concerns about learning Chinese? 4. What does Peter say in response? B. Pair up and discuss. C. Conduct the same conversation with your partner. Dialog 2: D. Listen and answer: 1. What is the main idea of this audio? 2. List at least three details about Anna’s speaking Chinese. 3. What are the benefits of Anna’s methods? E. Pair up and discuss. F. Conduct the same conversation, discussing how to improve speaking. (Audio, not included.)"),
        card("Activity 3 (Reading, Speaking and Writing): 词汇对比",
             "A. Pair up and compare the provided words. Discuss their differences with your partner. Decide which words will best complete the sentences and provide your reasons: 1. 体会, 体验, 经验 2. 效果, 结果 3. 表达, 表示 4. 方法, 办法 5. 希望, 愿望. B. Report your work to the class and request feedback. The book gives the blanks without a key; my notes and completed sentences:",
             tables=[CMP], examples=[D(z, e) for z, e in A3]),
        card("Activity 4 (Reading, Speaking and Writing)",
             "A. Complete the sentences using the following words: 交流, 主动, 提高, 能力, 字幕, 真实语料, 综艺节目, 新闻. B. Pair up and check your work with that of your partner; then take turns reading each sentence aloud and translating it into English. The completed sentences (key mine):",
             examples=[D(z, e) for z, e in A4]),
        card("Activity 5 (Speaking and Writing)",
             "A. Pair up and ask each other “对你来说，什么最难学？” Give advice using the patterns “越学越爱学”, “看着看着，也就看懂了” or “多说多练”, etc. Each partner asks at least three questions. Write your questions, your partner’s responses and your suggestions in the table. The book’s example: A: 对你来说，学中文什么最难学？ B: 对我来说，听力最难学。 A: 你应该多听真实语料，你的听力就会提高。 B. Report your partner’s responses and your suggestions to the class."),
    ],
    exercises=[
        M("Which word fits “大卫学中文的___”?", "体会", ["结果", "办法", "愿望"], "学中文的体会."),
        M("Which word fits “非常有___的老师”?", "经验", ["表示", "愿望", "结果"], "有经验的老师."),
        M("Which word fits “考试的___出来了”?", "结果", ["效果", "办法", "体验"], "考试的结果."),
        M("Which word fits “学习___提高了很多”?", "效果", ["结果", "愿望", "表示"], "学习效果."),
        M("Which word fits “这句话___什么意思”?", "表示", ["表达", "希望", "方法"], "表示: mean."),
        M("Which word fits “能让学生们都喜欢学中文的___”?", "办法", ["结果", "愿望", "经验"], "有什么办法."),
        M("Which word fits “你新年的___是什么”?", "愿望", ["希望", "表示", "效果"], "新年的愿望."),
        M("Which word fits “看不懂时就看___”?", "字幕", ["新闻", "能力", "交流"], "看字幕."),
        M("Which word fits “常常___帮助其他同学”?", "主动", ["提高", "新闻", "字幕"], "主动帮助."),
        F("每天上课，老师都给我们听一个真实语___来训练我们的听力。", "料", PART, "语料: corpus."),
        F("由于我每天都听中文，我的听力水平有了很大的提___。", "高", PART, "提高: improvement."),
    ],
)

# ------------------------------------------------------------------ 3. 对...来说, 刚
DQ1 = [("对很多人来说，中文是世界上最难学的语言。", "1. The book’s example: For many people Chinese is the hardest language in the world. (= 很多人觉得中文是世界上最难学的语言。)"), ("动画片对大人来说，也很有意思。", "Cartoons are also very interesting for adults. (= 大人也觉得动画片有意思。)"), ("对学生来说，预习和复习都很重要。", "2. For students, both previewing and reviewing are important. (the speaker feels they are important for students)"), ("对电视新闻来说，真实非常重要。", "For TV news, truthfulness is very important. (the speaker feels truthfulness matters for TV news)")]
DQ2 = [("开完药方后，医生对你说了什么？", "1. What did the doctor say to you after writing the prescription?"), ("我们的老师对我们非常耐心。", "2. Our teachers are very patient with us."), ("我对合唱不太感兴趣。", "3. I am not very interested in chorus.")]
GA = [("刚开始是有点儿难，可是后来我就觉得容易多了。", "1. At the beginning it was hard, but later I felt it was much easier."), ("我刚到北京时，谁都不认识。", "2. When I first arrived in Beijing, I did not know anyone.")]
GB = [("我刚到中国时，一句中文也不会。", "1. When I first arrived in China, I could not speak any Chinese."), ("保罗刚做完作业就去打篮球了。", "2. Paul just finished his homework and then went to play basketball."), ("我刚才在图书馆看见你了。", "3. I saw you at the library just now.")]
G3 = [("刚才，我看了一个非常有意思的中国电影。", "1. 刚才 = just now: Just now I watched a very interesting Chinese movie. (Student A, translation mine)"), ("我听说大卫刚买了一辆新车，因为最近汽车大降价。", "2. 刚 = just: I heard that David just bought a new car, because car prices have recently dropped sharply."), ("我刚开始听真实语料时，一点儿也听不懂，后来听多了就听懂了。", "3. 刚开始 = at first: When I first began listening to authentic materials I couldn’t understand at all, but later after listening more I did."),
      ("我刚才在网上看了一个综艺节目叫“欢乐喜剧人”，特别搞笑。", "4. 刚才: Just now I watched a variety show online called “Happy Comedians”; it was really funny. (Student B)"), ("刚开始去中国餐馆吃饭时，我还不会说中文。现在我可以用中文点菜了。", "5. 刚开始: When I first went to eat at Chinese restaurants I couldn’t speak Chinese yet. Now I can order in Chinese."), ("安娜刚从中国回来，下个星期来给我们谈谈她在中国学中文的体会。", "6. 刚: Anna has just come back from China and next week will come to tell us about her experience of learning Chinese there.")]
L3 = lesson(
    "Lesson 23 Presentation 1 grammar: 对…来说 and 对, and the adverb 刚",
    "对很多人来说 · 对你说 对我感兴趣 · 刚开始 · 刚 和 刚才",
    requires=[],
    cards=[
        card("The Colloquial Expression 对…来说",
             "The pattern 对…来说 is used to introduce a point of view, meaning “as for…”. 1. It introduces a person’s perspective. 2. It introduces a topic in discussion.",
             examples=[D(z, e) for z, e in DQ1]),
        card("The Preposition 对",
             "The preposition 对 means “to” or “toward” an object or target. Pattern: 对 + Object + Verb.",
             examples=[D(z, e) for z, e in DQ2]),
        card("Activities 1 and 2",
             "Activity 1 (Listening, Writing and Speaking): A. Listen to six sentences that use 对…来说 or 对 and translate them into English. B. Pair up and check your translation; then say the sentences in Chinese. (Audio, not included.) Activity 2 (Reading and Speaking): 说说你的看法. Pair up. Use 对…来说 to write your opinions about the following topics and explain your opinion: 1. 你学中文时觉得什么比较难？为什么？ 2. 你觉得家庭重要还是工作重要？为什么？ 3. 你觉得有好身体重要还是有钱重要？为什么？ 4. 找工作时，你觉得学习机会最重要还是工资最重要？为什么？ 5. 去餐馆吃饭，你觉得饭菜好吃最重要还是服务最重要？为什么？"),
        card("The Adverb 刚 (at first)",
             "A. The adverb 刚 can be placed before a verb to indicate “at first”: 刚 + Verb (时) + a situation which no longer exists or is changed. B. Compare 刚 and 刚才. In a previous lesson you learned that the adverb 刚 means “just” or “a short while ago”; it emphasizes that the action just happened a short time ago. 刚才 is a time noun and emphasizes something occurred “just now”. 刚 (adverb) = at first; 刚 (adverb) = just, a short while ago; 刚才 (noun) = just now.",
             examples=[D(z, e) for z, e in GA] + [D(z, e) for z, e in GB]),
        card("Activity 3 (Reading and Speaking): 比较“刚”和“刚才”",
             "Pair up. Student A reads Sentences 1–3 aloud and Student B translates them into English; Student B reads Sentences 4–6 aloud and Student A translates them into English. The sentences with my translations:",
             examples=[D(z, e) for z, e in G3]),
    ],
    exercises=[
        M("What does 对…来说 introduce?", "A point of view, “as for…”", ["A time", "A place", "A result"], "introduce a point of view."),
        M("What does 对很多人来说，中文是世界上最难学的语言 mean?", "For many people Chinese is the hardest language in the world", ["Many people teach Chinese", "Chinese is easy", "Most people speak Chinese"], "对很多人来说."),
        M("What does 对 + object + verb mean?", "To or toward the object", ["From the object", "Without the object", "After the object"], "对: to, toward."),
        M("What does 我们的老师对我们非常耐心 mean?", "Our teachers are very patient with us", ["Our teachers are away", "Our teachers don’t like us", "Our teachers are young"], "对…耐心."),
        M("What does 刚开始是有点儿难 mean?", "At first it was a bit hard", ["Just now it was hard", "It is still hard", "It will be hard"], "刚开始: at first."),
        M("Which means “just now”?", "刚才", ["刚开始", "刚到", "刚做完"], "刚才 is a time noun."),
        M("What does 保罗刚做完作业就去打篮球了 mean?", "Paul had just finished his homework when he went to play basketball", ["Paul never did his homework", "Paul plays basketball every day", "Paul will do homework tomorrow"], "刚: just."),
        M("What does 我刚到北京时，谁都不认识 mean?", "When I first arrived in Beijing, I knew nobody", ["I know everybody in Beijing", "I have never been to Beijing", "I will arrive tomorrow"], "刚到: when I first arrived."),
        F("___很多人来说，中文是世界上最难学的语言。", "对", PART, "对…来说."),
        F("我___才在图书馆看见你了。", "刚", PART, "刚才: just now."),
    ],
)

# ------------------------------------------------------------------ 4. verbal subject, V着V着
VS = [("说不好，说不多都没关系。", "1. It doesn’t matter that you cannot speak well or speak more."), ("吃得太多会变胖。", "2. Eating too much will make you fat.")]
VA = [("多听，多说，多写，多读，对提高你的中文水平有好处。", "1. Subject: 多听，多说，多写，多读. Listening, speaking, writing and reading more is good for improving your Chinese level. (Activity 4, mine)"), ("说中文时，说得太慢不好，说得太快也不好。", "2. Subject: 说得太慢, 说得太快. When speaking Chinese, speaking too slowly is not good and speaking too fast is not good either."), ("每天早上，回电子邮件是他最重要的工作之一。", "3. Subject: 回电子邮件. Every morning, answering email is one of his most important jobs."),
      ("多学一门外语可以给你更多的机会。", "4. Subject: 多学一门外语. Learning one more foreign language can give you more opportunities."), ("做瑜伽是一种很好的体育运动。", "5. Subject: 做瑜伽. Doing yoga is a very good kind of sport."), ("看书学习会使人变得聪明。", "6. Subject: 看书学习. Reading and studying makes people clever. (the book ends this sentence with a period in English style)")]
KZ = [("看不懂时我就看字幕，看着看着就看懂了。", "1. If I don’t understand, I watch the subtitles. As I was watching, I got it. (pattern: V + 着 + V + 着 + 就 … 了, a repeated action leads to a new situation)"), ("昨天做听力作业时，听着听着，我就睡着了。", "2. Yesterday when I was doing listening homework, I fell asleep as I was listening."),
      ("说着说着，我就发现自己有点儿糊涂了。", "3. I was talking and talking, and then I found myself a bit confused. (V着V着 also indicates a state of unawareness)"), ("我在北京的大街上走着走着就走迷路了。", "4. As I was walking on the street in Beijing, I got lost.")]
ST6 = ("我刚到中国时，一句中文也不会，对我来说，什么都很难。刚才我看了一个中文电视节目，看着看着就看懂了不少。对我来说，这就是一个好消息。我听着听着，就听懂了老师的话。",
       "When I first arrived in China I couldn’t speak a word of Chinese, and for me everything was hard. Just now I watched a Chinese TV show, and as I watched, I came to understand quite a lot. For me this is good news. As I listened, I came to understand what the teacher said. (Activity 6, my short sample using 对, 对…来说, 刚, 刚才 and V着V着就…了)")
L4 = lesson(
    "Lesson 23 Presentation 1 grammar: the verbal phrase as subject and V着V着",
    "说不好说不多都没关系 · 吃得太多会变胖 · 看着看着就看懂了 · 走着走着就走迷路了",
    requires=[],
    cards=[
        card("The Verbal Phrase Used as Subject",
             "In addition to nouns and pronouns, the verbal phrase can also be used as a subject in a sentence. Pattern: Subject (Verbal Phrase) + Predicate.",
             examples=[D(z, e) for z, e in VS]),
        card("Activity 4 (Reading and Speaking)",
             "A. Read the following sentences and highlight the verbal phrases used as subjects. Then translate the sentences into English. B. Pair up and explain to each other why you think the parts of the sentence you underlined are verbal phrases used as subjects. Then discuss your translations. My answers:",
             examples=[D(z, e) for z, e in VA]),
        card("The Pattern Verb + 着 + Verb + 着",
             "A. The pattern V + 着 V + 着 is used to indicate that an action has been repeated for a period of time, and as a result a new situation has arisen: Verb + 着 + Verb + 着 + 就……了. B. V + 着 V + 着 also indicates that the action that is repeated leads to a state of unawareness.",
             examples=[D(z, e) for z, e in KZ]),
        card("Activities 5 and 6",
             "Activity 5 (Listening, Writing and Speaking): A. Listen to six sentences with the pattern V + 着 + V + 着 and translate them into English. B. Pair up and check your translation; then say the sentences in Chinese to your partner. (Audio, not included.) Activity 6 (Writing and Speaking): A. Create a short story using the following words and patterns: 对, 对……来说, 刚, 刚才, (说)着(说)着就……. B. Pair up and share your story. My sample:",
             examples=[D(*ST6)]),
    ],
    exercises=[
        M("What can be the subject of a sentence besides nouns and pronouns?", "A verbal phrase", ["An adverb only", "A measure word", "A particle"], "verbal phrase as subject."),
        M("Which part is the subject in 吃得太多会变胖?", "吃得太多", ["会变胖", "变胖", "太多会"], "吃得太多 is a verbal phrase."),
        M("Which part is the subject in 做瑜伽是一种很好的体育运动?", "做瑜伽", ["体育运动", "很好的", "一种"], "做瑜伽."),
        M("What does V着V着 indicate?", "A repeated action leads to a new situation", ["A single quick action", "A past habit", "A future plan"], "V着V着就…了."),
        M("What does 看着看着就看懂了 mean?", "As I kept watching, I came to understand", ["I never understood", "I watched once", "I watched without sound"], "看着看着."),
        M("What does 听着听着，我就睡着了 mean?", "I fell asleep as I listened", ["I woke up while listening", "I did not listen", "I listened carefully"], "听着听着睡着了."),
        M("What does 走着走着就走迷路了 mean?", "While walking I got lost", ["I walked home", "I found the way", "I stopped walking"], "走迷路."),
        M("What does V着V着 also indicate?", "A state of unawareness", ["Anger", "Politeness", "Distance"], "unawareness."),
        F("说着说着，我就发现自己有点儿___涂了。", "糊", PART, "糊涂: confused."),
        F("说不好，说不多都没___系。", "关", PART, "没关系."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
TZ = [("张老师", "同学们，你们在中国已经学了四个多月的中文了，你们一定很了解外国人学习中文的困难。今天我想请你们谈谈，如果你是一个中文老师，你觉得你怎么能让你的学生学好中文。", "Students, you have already studied Chinese in China for more than four months, and you must understand foreigners’ difficulties in learning Chinese. Today I would like you to talk about how, if you were a Chinese teacher, you would help your students learn Chinese well. (translation mine)"),
      ("大卫", "如果我是老师，我会让学生学更多的生词，一开始至少每天十个单词。我也会马上教他们基本的语法，这样学生会早点说话和简单地表达他们的想法。如果他们会用中文说话，他们会很高兴，就更有热情和动力去学好中文。", "If I were a teacher I would have students learn more new words, at least ten words a day at the start. I would also teach them basic grammar right away, so that students can speak earlier and express their ideas simply. If they can speak in Chinese they will be very happy and have more enthusiasm and motivation to learn well."),
      ("琳达", "我觉得一开始要教学生正确的发音和语调，应该鼓励学生多说。还有我上课肯定不用英语，我只让学生听汉语，因为他们需要练习听力。可能刚开始只能听懂一点儿，但是他们会越来越习惯汉语的发音和语调。我也会经常用中文问学生一些问题，让他们一边听一边说话。另外，学生要多和老师交流。老师和学生交流会帮助他们提高说话能力，而且这样的中文课很热闹，很有意思。", "I think at the start one should teach students correct pronunciation and intonation and encourage them to speak more. Also I would definitely not use English in class; I would let students hear only Chinese, because they need to practice listening. Perhaps at first they can understand only a little, but they will get more and more used to the sounds and intonation of Chinese. I would also often ask students questions in Chinese so they listen and speak at the same time. In addition, students should communicate more with the teacher. Teacher–student communication helps them improve their speaking, and such a Chinese class is lively and interesting."),
      ("马克", "我在美国学中文的时候，我的一些老师很像中国传统的老师，上课不停地讲，让学生记笔记。那样的学习让我感觉很累，想睡觉。我觉得如果讲新语法，可以让学生记笔记，然后让他们用这个新语法试着说一些句子，这样可以知道学生会不会用这个语法。我经常听到学英语的中国学生说他们会读英语，但是不能说。因为他们在英语课上没有机会说英语。", "When I studied Chinese in the U.S., some of my teachers were very like traditional Chinese teachers: they talked non-stop in class and made students take notes. That kind of learning made me feel tired and sleepy. I think when teaching new grammar, you can have students take notes and then have them try to say some sentences with the new grammar, so you know whether students can use it. I often hear Chinese students who study English say they can read English but cannot speak it, because they have no chance to speak English in English class."),
      ("安娜", "我会让学生增加词汇量，学更多的语法，写好汉字，还要注意发音和语调。我也让他们多写中文，多读中文书和新闻。比如让学生看最近的新闻，然后在课上给大家讲这个新闻，谈谈他们对这个新闻的看法，问他们有没有解决这些问题的方法等。", "I would have students increase their vocabulary, learn more grammar, write characters well, and pay attention to pronunciation and intonation. I would also have them write more Chinese and read more Chinese books and news. For example, have students read the latest news, then tell everyone about this news in class, talk about their views of it, ask whether they have ways to solve these problems, and so on. (the book omits a verb before 最近的新闻; I read 看)"),
      ("张老师", "你们说得都很好。以后老师和学生要多交流。只有多了解学生的想法和学习情况，才能更好地帮助学生。", "You all spoke very well. In future teachers and students should communicate more. Only by understanding students’ ideas and learning situation better can we help students better.")]
L5 = lesson(
    "Lesson 23 Presentation 1 skill integration: David’s email, if I were a teacher and Xuelian",
    "周阳的电子邮件 · 如果我是老师 · 听力 口语 · 雪莲怎么学中文",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the email David gets from his Chinese friend Zhou Yang. Write the main idea in one sentence and at least three EEIs (Essential Elements of Information). B. Listen to the following sentences twice. Transcribe the missing information in Pinyin and translate them into English: 1. 听起来你学英文… 2. 他们教我一句成语…，所以我一有时间就练习中文。 C. Pair up and check. D. Listen to the email from David to Zhou Yang and answer: 1. 这个电子邮件的主要意思是什么？ 2. 大卫的老师告诉大卫怎么才能学好中文？ 3. 大卫和谁用中文聊天？和他们聊天有什么好处？ 4. 最后大卫让周阳怎么做可以提高他的英文水平？ E. Pair up and discuss, and share with the class. F. Discuss: 1. 大卫在网上和中国人聊天学中文。你觉得这个方法适合你吗？ 2. 除了在网上聊天以外，你觉得还有什么方法可以和中国人练习中文？ 3. 大卫建议周阳可以去“英语角”学英文。你觉得对周阳有帮助吗？你的学校有没有“中文角”？ 4. 你觉得学好外语一定要有语言环境吗？如果没有，是不是就不能学好外语？请谈谈你的看法。 (The emails are audio, not included.)"),
        card("Activity 2 (Reading, Writing and Speaking)",
             "A. Divide into two groups. Each group reads three passages and writes the summary of the passages in the table. Mark any unfamiliar words and discuss their meanings. Group A: 张老师, 大卫, 琳达. Group B: 马克, 安娜, 张老师. B. Form new groups. Pair students from Group A with students from Group B. Exchange information about what you read. C. Discussion: 1. 你觉得每天至少要学十个单词少不少？你认为每天应该学多少？为什么？ 2. 你喜欢老师用英语给你们上课吗？为什么？ 3. 你上中文课时，老师说话多还是你说话多？你喜欢记笔记吗？为什么？ 4. 你觉得安娜说得对不对？为什么？ D. Share your group discussion with the class. The passages:",
             examples=dlg(TZ)),
        card("Activity 3 (Listening, Reading, Writing and Speaking): 我如何学习中文？",
             "A. Watch a video segment about Xuelian and answer: 1. 雪莲是什么时候开始学中文的？她为什么选择学中文？ 2. 她最喜欢中文的哪个方面？ 3. 她后来为什么去了台湾？ 4. 她认为中文哪三个部分很难学？ 5. 她最喜欢的学习方法是什么？ B. Pair up and discuss. C. In groups discuss: 1. 雪莲觉得中文比西班牙语好学，你同意吗？ 2. 雪莲认为中文的语法比英文的语法简单，你同意吗？ 3. 你觉得雪莲的学习方法怎么样？谈谈你的看法。 (The video is not included.)"),
    ],
    exercises=[
        M("How long have the students studied Chinese in China?", "More than four months", ["One week", "Two years", "Ten days"], "已经学了四个多月."),
        M("How many new words a day would David teach at the start?", "At least ten", ["One", "Fifty", "None"], "至少每天十个单词."),
        M("Why would David teach grammar right away?", "So students can speak earlier and express ideas simply", ["Because grammar is easy", "To avoid speaking", "To prepare an exam"], "早点说话和简单地表达."),
        M("What would Linda not use in class?", "English", ["Chinese", "Pictures", "Songs"], "我上课肯定不用英语."),
        M("Why does Linda want students to hear only Chinese?", "They need to practice listening", ["They hate English", "It is cheaper", "The teacher can’t speak English"], "因为他们需要练习听力."),
        M("What did Mark dislike about traditional teaching?", "The teacher talked non-stop and students only took notes", ["Too many pictures", "Too much singing", "Short classes"], "上课不停地讲，让学生记笔记."),
        M("What do Chinese students of English often say, according to Mark?", "They can read English but cannot speak it", ["They can speak but not read", "They can do neither", "They can do both well"], "会读英语，但是不能说."),
        M("What does Anna want students to do with the news?", "Read recent news and tell the class about it", ["Memorize it", "Translate it only", "Ignore it"], "在课上给大家讲这个新闻."),
        M("What does Teacher Zhang conclude?", "Teachers and students should communicate more", ["Students should talk less", "Teachers should talk more", "Exams should be harder"], "老师和学生要多交流."),
        F("老师和学生交流会帮助他们提___说话能力。", "高", PART, "提高."),
        F("我觉得一开始要教学生正确的发音和语___。", "调", PART, "语调: intonation."),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese
JH = [("张老师", "非常感谢你们来我们班介绍你们的学习经验。今天想请你们讲讲你们是怎么练习口语的。", "Thank you very much for coming to our class to introduce your learning experience. Today I would like you to talk about how you practiced speaking. (translation mine)"),
      ("杰克", "我觉得要想说得好就得先听得懂，如果听不懂中国人说的话，就不能和他们交流。除了上课听中文以外，下课以后我在网上找一些听力材料，一遍遍听，一遍遍跟着重复，这样，我的听力和说话能力都提高了，老师上课说的话我差不多都能听懂，回答问题也有信心了。有些句子，因为听多了，说话的时候，一张嘴就能说出来。", "I think if you want to speak well you must first be able to understand; if you can’t understand what Chinese people say, you can’t communicate with them. Besides listening to Chinese in class, after class I find listening materials online, listen over and over and repeat after them over and over; in this way both my listening and speaking improved, I can understand almost everything the teacher says in class, and I have confidence answering questions. Some sentences, because I have heard them so much, come out as soon as I open my mouth."),
      ("海伦", "我的方法和你不一样。我喜欢和中国人聊天学中文。我们学校除了我们的老师以外，没有别的中国人，我就去附近的大学找中国留学生练口语。有时候她教我中文，我教她英文。", "My method is different from yours. I like chatting with Chinese people to learn Chinese. In our school there are no Chinese people apart from our teachers, so I go to a nearby university to find Chinese international students to practice speaking with. Sometimes she teaches me Chinese and I teach her English."),
      ("杰克", "当然，光听录音还不够，我也常常找中国人说话，比如我们的老师。还有我在网上和中国人聊天，不仅训练我打字的速度，而且也训练我的说话能力。", "Of course, just listening to recordings isn’t enough; I also often find Chinese people to talk to, for example our teacher. Also I chat with Chinese people online, which trains not only my typing speed but also my speaking ability."),
      ("海伦", "我还有一个方法就是写日记。每天把我做的事情和学习的情况都写下来。每次学一些新的单词，我就用这些单词写日记。我一直都这么做，我觉得效果很好，我的表达能力越来越好。", "I have another method, which is writing a diary. Every day I write down what I did and how my studies went. Each time I learn some new words I use them to write my diary. I have always done this; I find the effect very good and my ability to express myself gets better and better."),
      ("张老师", "你们说得都很好，很有道理，对我们的同学很有帮助。我想我们可以根据自己的情况试一下。不管用什么方法，只要每天坚持说中文，用中文，就一定会有很大的进步。", "You both spoke very well and made good sense, which helps our students a lot. I think we can each try according to our own situation. Whatever method you use, as long as you persist every day in speaking and using Chinese, you will certainly make great progress.")]
PR = table(["生词", "拼音", "English"], [["大脑", "dànǎo", "brain"], ["次序", "cìxù", "order"], ["刺激", "cìjī", "stimulate"], ["输入", "shūrù", "input"], ["词组", "cízǔ", "phrase"], ["文法", "wénfǎ", "grammar"], ["好奇心", "hàoqíxīn", "curiosity"], ["相声", "xiàngsheng", "crosstalk"], ["强迫", "qiǎngpò", "force"], ["动力", "dònglì", "motivation"], ["态度", "tàidù", "attitude"], ["变化", "biànhuà", "change"], ["害怕", "hàipà", "afraid"], ["互联网", "hùliánwǎng", "the Internet"]], title="Activity 3: the new words for Steven Kaufmann’s seven principles of learning Chinese", say=[0])
L6 = lesson(
    "Lesson 23 Presentation 1 using Chinese in context: the listening test, Jack and Helen, seven principles",
    "听力问题 · 杰克和海伦怎么练口语 · 七个学习原则 · 坚持说中文",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing and Speaking)",
             "Scenario: your class has just finished the mid-unit listening tests. After the tests, your teacher conducts a critique session and brings up some of the problems. Your teacher asks you to discuss them and come up with solutions. A. Listen to your teacher’s critique and write the listening problems the teacher mentions (第一个问题, 第二个问题, 第三个问题). B. Form three groups; each group discusses one problem and makes suggestions for solving it. Provide at least three suggestions and justify why these suggestions will help improve listening comprehension. C. Each group reports to the class. Select the best suggestions. D. Group discussion: 除了刚才大家讨论的听力问题，还有哪些听力问题？你有什么建议来解决这些问题？ (Audio, not included; the table of problems and suggestions is blank.)"),
        card("Activity 2 (Reading, Writing and Speaking)",
             "Scenario: you have been studying Chinese for over four months. Your teacher Professor Zhang invites two students, Jack and Helen, who just graduated from the Chinese basic course with great results, to talk about how they learned Chinese. Below is a written record of their conversation. A. Read the conversation. Summarize what Jack and Helen said in the table (杰克的方法, 海伦的方法). B. In two groups discuss: 1. 你同意杰克和海伦的学习方法吗？为什么？ 2. 你还有什么好的方法介绍给大家？ C. Report your group discussion to the class.",
             examples=dlg(JH)),
        card("Activity 3 (Listening, Reading, Writing and Speaking)",
             "A. Watch a video clip about seven principles of learning Chinese from Steven Kaufmann. Summarize the seven principles he describes in the video, starting at 1:42. B. Form two groups; Group A discusses principles 1–3 and Group B discusses principles 4–7. Discuss whether you agree or disagree with these principles and explain your opinion. C. Within your group discuss: 1. 你觉得应该怎么培养学中文的兴趣？ 2. 你认为怎么才能提高学中文的动力？ D. Share your group discussion with the class. (The video is not included.)",
             tables=[PR]),
    ],
    exercises=[
        M("What does Jack say you must do first to speak well?", "Be able to understand", ["Write essays", "Buy a dictionary", "Move to China"], "要想说得好就得先听得懂."),
        M("How does Jack practice listening?", "Finds materials online and listens and repeats over and over", ["Reads novels", "Watches silent films", "Takes long walks"], "一遍遍听，一遍遍跟着重复."),
        M("What is Helen’s main method?", "Chatting with Chinese people", ["Writing essays only", "Memorizing words", "Watching TV"], "我喜欢和中国人聊天学中文."),
        M("Who does Helen find to practice with?", "Chinese international students at a nearby university", ["Teachers at her school", "Shopkeepers", "Her classmates"], "去附近的大学找中国留学生练口语."),
        M("How do Helen and her partner help each other?", "She teaches Chinese and Helen teaches English", ["They both pay", "They only chat", "They swap notes"], "她教我中文，我教她英文."),
        M("What does Jack say about chatting online?", "It trains typing speed and speaking ability", ["It is a waste of time", "It trains only listening", "It is too hard"], "不仅训练我打字的速度，而且也训练我的说话能力."),
        M("What is Helen’s other method?", "Writing a diary", ["Singing", "Reading aloud", "Making flashcards"], "写日记."),
        M("What does Professor Zhang conclude?", "Whatever method, keep speaking and using Chinese every day", ["Only Jack’s method works", "Stop speaking", "Study only grammar"], "只要每天坚持说中文，用中文."),
        M("What does 动力 mean?", "Motivation", ["Power plant", "Direction", "Distance"], "动力: motivation."),
        M("What does 害怕 mean?", "Afraid", ["Happy", "Tired", "Hungry"], "害怕: afraid."),
        F("不管用什么方法，只要每天坚持说中文，就一定会有很大的进___。", "步", PART, "进步: progress."),
        F("我的表达能力越来越___。", "好", PART, "越来越好."),
    ],
)

# ------------------------------------------------------------------ 7. vocabulary
L7 = vocab_lesson("Lesson 23 Presentation 1 vocabulary", "24 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English; its glosses are kept as printed.", VOC1)

UNIT = unit("第二十三课 Presentation 1: 学中文的体会, 对…来说, 刚, V着V着", [L1, L2, L3, L4, L5, L6, L7])
