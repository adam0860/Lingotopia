"""Unit 48: Lesson 17 (Sports and Fitness) Presentation 1 from the book's texts: the gym dialog, the adverb 好 (many), the modal
particle 呢 (emphasis), the modal verb 能 and its meaning development, the verbal measure words 次/遍, the skill-integration and
using-Chinese activities (Lao Zhang's gym card, fitness plans) and the vocabulary list. Audio, pictures and websites are not
included; the book writes numbers and phone numbers as digits and they are spelled out here; answer keys the book does not print
(and blanks it leaves for the student) are mine and labeled."""
from zh_auto import *
from zh_l17_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("教得", 0, "jiao1"), ("长肉", 0, "zhang3"), ("没记", 0, "mei2"), ("没有记", 0, "mei2"), ("没用过", 0, "mei2"), ("没有中国", 0, "mei2"), ("还没有", 0, "hai2"), ("得买", 0, "dei3"), ("得很", 0, "de5"), ("教英文", 0, "jiao1"),
                          ("都会", 0, "dou1"), ("人参加", 1, "can1")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0 and zh[j - 1] not in "当草土天各山场内本外基实陆" and (j + 1 >= len(zh) or zh[j + 1] not in "道址方铁图球区点上下面理"):
            f[j] = "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [("张英", "王林，听说咱们公司附近新开了一家健身房，你想不想去试试？", "Wang Lin, I heard a new gym opened near our company; do you want to try it?"), ("王林", "张英，我都去过好几次了，还办了一张年卡呢。", "Zhang Ying, I’ve been several times already, and I even got an annual card."), ("张英", "这个健身房怎么样？", "How is this gym?"),
      ("王林", "不错，里面又大又干净，器械很全，还有一个温水游泳池。", "Pretty good; it’s big and clean inside, the equipment is complete, and there’s even a warm-water swimming pool."), ("张英", "真的？", "Really?"), ("王林", "真的。对了，现在新会员有优惠，买一个月送一个月。", "Really. By the way, new members get a deal now: buy one month, get one month free."),
      ("张英", "你去健身房都做什么运动？", "What exercise do you do at the gym?"), ("王林", "我喜欢举重，做力量训练。", "I like weightlifting and strength training."), ("张英", "我最近胖了不少，需要减肥，有什么适合我的运动吗？", "I’ve gotten quite a bit fatter recently and need to lose weight; is there any exercise suitable for me?"),
      ("王林", "你可以在跑步机上跑步，或是上瑜伽课。举重也是很好的选择。", "You can run on the treadmill or take a yoga class. Weightlifting is also a good choice."), ("张英", "可是我没用过那些器械，会不会很容易受伤？", "But I’ve never used those machines; won’t it be easy to get hurt?"),
      ("王林", "要是你怕受伤，最好先请个教练，让他帮你制定一个锻炼计划，带你一起练。", "If you’re afraid of getting hurt, it’s best to hire a coach first and have him make a workout plan for you and train with you."), ("张英", "你能给我推荐一个好教练吗？", "Could you recommend a good coach to me?"),
      ("王林", "我的教练教得不错，也很有耐心。你可以问问他。他的电话号码是八八三六，五零一一。", "My coach teaches well and is very patient. You can ask him. His phone number is 8836-5011."), ("张英", "你能不能再说一遍，我没记下来。", "Could you say it once more? I didn’t write it down."), ("王林", "八八三六，五零一一。", "8836-5011.")]
KEY5 = [("如果要学好中文，你需要制定一个学习计划。", "1. If you want to learn Chinese well, you need to make a study plan. (制定; key mine)"), ("马克，谢谢你给我推荐了一个举重教练。", "2. Mark, thanks for recommending a weightlifting coach to me. (推荐)"), ("听说你要去中国教英文了，这个工作很适合你。", "3. I heard you’re going to teach English in China; this job suits you very well. (适合)"), ("我想成为你们的会员，能不能告诉我怎么办年卡？", "4. I want to become a member; could you tell me how to get an annual card? (办)"),
        ("最近琳达没在跑步机上跑步，因为她的腿受伤了。", "5. Linda hasn’t been running on the treadmill lately because her leg is injured. (受伤)"), ("张英每天吃很多蔬菜，很少吃米饭，因为她怕变胖了。", "6. Zhang Ying eats lots of vegetables and little rice every day because she is afraid of getting fat. (怕)"), ("李丽刚告诉我怎么做运动减肥，你要不要试试？", "7. Li Li just told me how to lose weight through exercise; do you want to try? (试试)"), ("你的电话号码我没有记下来，你能不能再说一遍？", "8. I didn’t write down your phone number; could you say it again? (记下来)")]
L1 = lesson(
    "Lesson 17 Presentation 1: joining a gym",
    "新开了一家健身房 · 买一个月送一个月 · 请个教练 · 你能不能再说一遍",
    requires=[],
    cards=[
        card("Getting Started",
             "Photograph: a weight room (not included). Pair up and discuss: A. Do you work out every day? If so, where do you usually work out? B. How do you like the school’s gym? What kind of equipment does it have? C. What do you usually do when you work out in the gym? What equipment do you usually use?"),
        card("Presentation 1: 健身房",
             "The book also prints the dialog in traditional characters. The phone number is printed as 8836-5011; it is read digit by digit.",
             examples=dlg(P1)),
        card("Activities 1 and 2 (listening)",
             "Activity 1 (Listening and Speaking). A. Global listening: 1. What are the speakers talking about? 2. What is the relationship between these two speakers? How could you tell? B. Detailed listening: 1. What does Zhang Ying say to Wang Lin at the beginning? 2. How does Wang Lin respond? 3. What are the benefits for new members? 4. What kind of exercise does Wang Lin think would be good for Zhang Ying? 5. When Zhang Ying expresses concerns about injury, what does Wang Lin say? 6. What does Zhang Ying ask Wang Lin to do? C. Pair up, compare answers and share them with the class; conduct this conversation with your partner and share your experiences at the gym. (Audio, not included. From the dialog, mine: a gym; colleagues, since they say 咱们公司; new members get one month free for each month bought; a coach.) Activity 2 (Listening and Speaking). A. Listen to Dialog 1 and answer: 1. What are the two speakers talking about? 2. What information did Zhang Ying find useful? 3. What action do you think Zhang Ying will take next? B–C. Compare and conduct a similar conversation. D. Listen to Dialog 2: 1. What topic is discussed? 2. Why does Zhang Ying not do weightlifting at the gym? 3. What did you hear about the weightlifting coach? E–F. Compare and conduct a similar conversation. (Audio, not included.)"),
        card("Activities 3 and 4",
             "Activity 3 (Speaking and Writing). Pair up and discuss the nouns, verbs and adjectives used in Presentation 1 that are related to a gym; write them in the table by category: 健身房里有什么; 为什么去健身房; 可以做什么运动; 做运动会怎么样. (Mine: 器械, 跑步机, 温水游泳池, 教练; 减肥, 力量训练; 举重, 跑步, 瑜伽, 游泳; 变瘦, 有力量, 受伤.) Activity 4 (Speaking and Writing). How many words can you say using 卡? Write the words you know in the diagram (the book starts it with 生日卡). Mine: 生日卡, 年卡, 信用卡, 银行卡, 会员卡, 健身卡, 电话卡, 贺卡, 学生卡."),
        card("Activity 5 (Reading, Writing and Speaking)",
             "A. Complete the sentences using the verbs: 办, 怕, 记下来, 推荐, 试试, 适合, 受伤, 制定. B. Pair up, check your work, read each sentence aloud and translate it into English. The book leaves the key out; my completed sentences (mine):",
             examples=[D(z, e) for z, e in KEY5]),
        card("Activity 6 (Speaking, Writing and Listening)",
             "A. Interview a classmate using the following questions and write their responses in the right-hand column; the interviewee can use 或者 or 要是…就… to answer. 1. 你平时喜欢做什么运动？ 2. 你常常什么时候健身？ 3. 你一个人健身还是和别人一起？ 4. 你学校的健身房怎么样？ 5. 你常常选择什么器械健身？ 6. 你的健身教练教得怎么样？ 7. 运动的时候你饿了，怎么办？ 8. 你喜欢举重吗？为什么？ B. Consolidate your interview answers and report them to the class."),
    ],
    exercises=[
        M("What is new near the company?", "A gym", ["A restaurant", "A school", "A bank"], "新开了一家健身房."),
        M("What did Wang Lin buy?", "An annual card", ["A monthly card", "A treadmill", "A coach"], "办了一张年卡."),
        M("What is special about the gym?", "A warm-water swimming pool and complete equipment", ["A cinema", "A bar", "A library"], "器械很全，还有一个温水游泳池."),
        M("What deal do new members get?", "Buy one month, get one month free", ["Half price", "A free coach", "No fee"], "买一个月送一个月."),
        M("What does Wang Lin like?", "Weightlifting and strength training", ["Yoga", "Swimming", "Running"], "我喜欢举重，做力量训练."),
        M("What does Zhang Ying want?", "To lose weight", ["To gain weight", "To rest", "To swim"], "需要减肥."),
        M("What does Wang Lin suggest if she fears injury?", "Hire a coach to make a plan and train with her", ["Quit exercising", "Use no equipment", "Go home"], "最好先请个教练."),
        M("What is Wang Lin’s coach like?", "Teaches well and is patient", ["Strict and loud", "Cheap", "Young"], "教得不错，也很有耐心."),
        M("Why does Zhang Ying ask him to repeat?", "She didn’t write down the phone number", ["She didn’t hear", "She forgot the coach", "The line was bad"], "我没记下来."),
        M("What does 受伤 mean?", "Get injured", ["Be hurt feelings", "Be tired", "Be lost"], "受伤."),
        mean("健身房", "jian4 shen1 fang2", "gym", ["restaurant", "classroom", "hospital"]),
        F("我的教练教___不错，也很有耐心。", "得", PART, "教得不错: complement of degree."),
        F("现在新会员有优惠，买一个月___一个月。", "送", PART, "买一个月送一个月."),
    ],
)

# ------------------------------------------------------------------ 2. 好
HA = [("这家健身房我都去过好几次了。", "I have been to this gym a couple of times."), ("这个健身房有好几十个跑步机。", "This gym has several dozen treadmills."), ("我现在感觉好累。我想休息一会儿再写作业。", "I feel so tired now. I want to rest a while and then do homework."), ("这个房子好贵，我可买不起。", "This house is very expensive; I can’t afford it.")]
HA2 = [("这本书太有意思了，我已经看了好几遍了。", "The book’s example: This book is so interesting; I’ve already read it several times."), ("他每天跑步，一跑就是好几个小时。", "1. He runs every day, and each run lasts several hours. (跑步，小时; mine)"), ("我好几个晚上没睡觉了。", "2. I haven’t slept for several nights. (睡觉，晚上; mine)"), ("他的房间里放着好几张书桌。", "3. His room has several desks. (放，书桌; mine)"),
       ("我去滑雪滑过好几次了。", "4. I have gone skiing several times. (滑雪，次; mine)"), ("这个号码我读了好几遍才记下来。", "5. I read this number several times before I wrote it down. (记下来，遍; mine)"), ("这个星期我吃了好几顿中国菜。", "6. This week I had Chinese food several times. (吃，顿; mine)"), ("路上堵了好几个小时。", "7. The road was jammed for several hours. (堵，小时; mine)"),
       ("这个小区住着好几百人。", "8. Several hundred people live in this neighborhood. (住着，百; mine)")]
L2 = lesson(
    "Lesson 17 Presentation 1 grammar: the adverb 好 (many)",
    "好几次 · 好几十个 · 好累 · 好贵",
    requires=[],
    cards=[
        card("The adverb 好 (表示多)",
             "The adverb 好 can express “many,” “much,” or “a lot.” It is usually used with 几 before measure words to indicate “quite a few.” Here 几 means “several,” “a couple of,” or “a few.” 好几 + Measure Word + Noun. The adverb 好 also means “very” or “so” to describe the degree of an adjective. Subject + 好 + Adjective.",
             examples=[D(z, e) for z, e in HA]),
        card("Activities 1 and 2",
             "Activity 1 (Listening, Writing and Speaking). A. Listen to six sentences that use 好 and translate them into English. B. Pair up, check your translations and repeat the sentences in Chinese. (Audio, not included.) Activity 2 (Writing and Speaking). Write sentences using the adverb 好 and the words in parentheses: 1. (跑步，小时) 2. (睡觉，晚上) 3. (放，书桌) 4. (滑雪，次) 5. (记下来，遍) 6. (吃，顿) 7. (堵，小时) 8. (住着，百). Then pair up and read your sentences to your partner. The book’s example and my sentences (mine):",
             examples=[D(z, e) for z, e in HA2]),
    ],
    exercises=[
        M("What does 好几 + measure word mean?", "Quite a few", ["Very good", "Several good", "A good one"], "好几 = quite a few."),
        M("What does 我都去过好几次了 mean?", "I have been several times already", ["I went once", "I will go several times", "I have never been"], "好几次."),
        M("What does 好几十个跑步机 mean?", "Several dozen treadmills", ["A good treadmill", "A few treadmills", "Ten treadmills"], "好几十."),
        M("What does 好累 mean?", "So tired", ["Good tired", "Not tired", "A little tired"], "好 + Adj. = very."),
        M("What does 这个房子好贵 mean?", "This house is very expensive", ["This house is cheap", "This is a good house", "This house is for sale"], "好贵."),
        M("Which measure word fits 好几___ in 去过好几___ (times)?", "次", ["个", "张", "本"], "次: times."),
        F("这个健身房有好___十个跑步机。", "几", PART, "好几十."),
        F("这个房子___贵，我可买不起。", "好", PART, "好 + Adj."),
    ],
)

# ------------------------------------------------------------------ 3. 呢
NE = [("这个健身房我都去过好几次了，还办了一张年卡呢。", "I have been to this gym several times and I even have an annual card."), ("外面的雨还很大呢，咱们不要出去了。", "It is raining so hard outside; let’s not go out.")]
NE4 = [("今天外面可冷呢，我不想出去。", "Example, B: It’s really cold outside today; I don’t want to go out."), ("咱们去看电影吧。", "Example, A: Let’s go see a movie."), ("这个健身房的器械真全。", "1. A: This gym’s equipment is really complete. (mine)"), ("对，还有温水游泳池呢！", "B: Yes, and there’s even a warm-water pool! (mine)"), ("你家乡有大学吗？", "2. A: Is there a college in your hometown? (mine)"), ("有，还有好几所呢。", "B: Yes, there are several. (mine)"),
       ("这个学期你上了几门课？", "3. A: How many courses have you taken this semester? (mine)"), ("我上了六门课呢！", "B: I’ve taken six courses! (mine)"), ("再多吃点儿，多喝点儿。", "4. A: Please eat and drink more. (mine)"), ("我已经吃了好多呢，吃不下了。", "B: I’ve already eaten a lot; I can’t eat any more. (mine)"), ("这些器械真新。", "5. A: These machines are really new. (mine)"), ("是啊，我昨天用了好几个呢。", "B: Yes, I used several of them yesterday. (mine)"),
       ("你在中国买了什么？", "6. A: What did you buy in China? (mine)"), ("我买了茶叶、丝巾，还有好多别的东西呢。", "B: I bought tea, silk scarves, and lots of other things. (mine)")]
L3 = lesson(
    "Lesson 17 Presentation 1 grammar: the modal particle 呢 (emphasis)",
    "还办了一张年卡呢 · 外面的雨还很大呢 · 可冷呢",
    requires=[],
    cards=[
        card("The modal particle 呢 (表示强调)",
             "The modal particle 呢 is used to ask questions, but it can also be used at the end of a statement to express a certain mood or attitude. It is used by the speaker to sound more confident and convincing. Statement + 呢.",
             examples=[D(z, e) for z, e in NE]),
        card("Activities 3 and 4",
             "Activity 3 (Listening, Writing and Speaking). A. Listen to six sentences with 呢 and translate them into English. B. Work in pairs to check your translations and repeat the sentences in Chinese. (Audio, not included.) Activity 4 (Writing and Speaking). What would you say using 呢 in the following situations? 1. Your friend makes a comment on the equipment in the new gym. 2. Your teacher asks whether there is a college in your hometown. 3. Your classmates ask you how many courses you have taken this semester. 4. Your host asks you to eat and drink more, but you have already eaten and drunk a lot. 5. Your friend comments on the equipment in the gym. 6. Your friend asks you what you bought in China; you name several things. The book’s example and my dialogs (mine):",
             examples=[D(z, e) for z, e in NE4]),
    ],
    exercises=[
        M("What does 呢 do at the end of a statement?", "Makes the speaker sound confident and convincing", ["Makes it a question", "Marks the past", "Shows doubt"], "呢 for emphasis."),
        M("What does 外面的雨还很大呢 convey?", "It’s raining hard, so let’s not go", ["It stopped raining", "It’s sunny", "It will rain tomorrow"], "Emphasis."),
        M("What does 还办了一张年卡呢 add?", "Emphasis: I even got an annual card", ["Doubt", "A question", "A wish"], "还…呢."),
        M("Which sentence uses 呢 for emphasis?", "今天外面可冷呢", ["你呢？", "我也不知道", "你去吗"], "可冷呢."),
        M("Which use of 呢 is NOT emphasis?", "你呢？ (and you?)", ["今天可冷呢", "还有好几个呢", "雨还很大呢"], "Question use."),
        F("外面的雨还很大___，咱们不要出去了。", "呢", ["吗吗", "们们", "了了"], "呢."),
    ],
)

# ------------------------------------------------------------------ 4. 能
NN = [("大卫告诉张文，他还没有中国的信用卡，不能在网上买东西。", "David told Zhang Wen that he doesn’t have a Chinese credit card yet and can’t shop online. (L9 Presentation 3, possibility)"), ("网上能做的事可多了。", "There’s a lot you can do online. (L16 Presentation 1, possibility)"), ("你能给我推荐一个好教练吗？", "Could you recommend a good coach to me? (request)"), ("你能不能再说一遍，我没记下来。", "Could you say it once more? I didn’t write it down. (request)"),
      ("能给我拿一双筷子吗？", "A: Could you get me a pair of chopsticks?"), ("好。/行。/可以。", "B: OK. / Sure. / Fine."), ("你能快点儿吗？", "A: Could you hurry?"), ("不行，我受伤了。", "B: No, I’m injured."), ("他体能很好。", "His physical fitness is good. (capability, noun)"), ("他体能好，能跑马拉松。", "He is fit and capable of running a marathon. (able to, verb)"),
      ("他很能说。", "He is talkative and well spoken. (good at)"), ("不到十六岁不能跑马拉松。", "You are not allowed to run a marathon if you are under sixteen. (permission)"), ("这种天气，能跑马拉松吗？", "Is it possible to run a marathon in such weather? (possibility)"), ("你能和我一起跑马拉松吗？", "Could you please run a marathon with me? (request)")]
L4 = lesson(
    "Lesson 17 Presentation 1 grammar: the modal verb 能",
    "能给我推荐一个好教练吗 · 能不能再说一遍 · 能 = capability, permission, possibility, request",
    requires=[],
    cards=[
        card("The modal verb 能",
             "The modal verb 能 in Chinese can express different meanings. We have learned two so far: 1. 能 indicates possibility. 2. In this presentation, 张英 asked 王林 能给我推荐一个好教练吗？ and 能不能再说一遍，我没记下来。 In these two sentences, 能 is used to make a request; its meaning is similar to “could you please…?” in English. When responding to such requests, you may use 能, 好, 行 or 可以. The Meaning Development of 能: Chinese modal verbs are derived from verbs with substantial meanings. The original meaning of 能 is capability, and it has developed into many other related meanings: capability (noun) → able to (verb) → good at (modal verb) → permission (may, allow) → possibility → make a request (could you please…?). All these usages can be interchangeable with 可以 except for the meaning “good at.”",
             examples=[D(z, e) for z, e in NN]),
        card("Activities 5 and 6",
             "Activity 5 (Listening). Listen to the conversation and answer: 1. What does the man ask the woman to do? 2. What is said about Li Jian? 3. What is the woman’s concern? 4. What will they do after the band’s performance ends? (Audio, not included.) Activity 6 (Speaking and Listening). A. Individually write one request for each of your classmates in your small class; walk around, propose your request to each of them, and take notes of their answers (同学一 to 同学五). B. Pair up. Imagine you are in the following scenarios: 在公园里烧烤; 在网上玩游戏; 在健身房健身. Student A asks whether it is possible to do something in the scenario and Student B responds. The book’s example: 我们能烧烤水果吗？ 不能。/不行。 My questions (mine):",
             examples=[D("我们能烧烤水果吗？", "Can we barbecue fruit? (the book’s example)"), D("不能。", "No. (the book’s example)"), D("我们能在公园里烧烤吗？", "Can we barbecue in the park? (mine)"), D("能，可是要先打电话问一问。", "Yes, but we have to call and ask first. (mine)"), D("我们能在网上玩游戏吗？", "Can we play games online? (mine)"), D("可以，但是不能玩太久。", "Yes, but not for too long. (mine)"), D("我们能在健身房吃东西吗？", "Can we eat in the gym? (mine)"), D("不行，只能喝水。", "No, only water. (mine)")]),
    ],
    exercises=[
        M("How does 能给我推荐一个好教练吗？ use 能?", "To make a request", ["To show ability", "To refuse", "To show a past action"], "Request: could you…?"),
        M("How can you agree to a request with 能?", "好, 行, or 可以", ["不行", "没有", "别"], "Responses: 能, 好, 行, 可以."),
        M("What does 他很能说 mean?", "He is talkative and well spoken", ["He can’t speak", "He speaks softly", "He is silent"], "能 = good at."),
        M("What does 不到十六岁不能跑马拉松 express?", "Permission (not allowed)", ["Capability", "A request", "Good at"], "能 = permission."),
        M("What does 他体能很好 mean?", "His physical fitness is good", ["He is tall", "He is fast", "He is rich"], "体能: noun capability."),
        M("What does 这种天气，能跑马拉松吗？ ask?", "Is it possible to run a marathon in such weather?", ["Can you run?", "Are you allowed?", "Could you run with me?"], "Possibility."),
        M("What can 能 NOT be interchanged with 可以 for?", "“Good at”", ["Permission", "Possibility", "Request"], "Except for “good at”."),
        F("你___给我拿一双筷子吗？", "能", PART, "能 for a request."),
        F("你能快点儿吗？ 不行，我受___了。", "伤", PART, "受伤: injured."),
    ],
)

# ------------------------------------------------------------------ 5. 次/遍
CB = [("我看过三遍。", "I have seen it three times. (Verb + Number + Measure Word)"), ("我去过三次医院。", "I have been to the hospital three times. (Verb + Number + Measure Word + Noun)"), ("我看过他三次。", "I have seen him three times. (Verb + Pronoun + Number + Measure Word)"), ("这部电影我看了三遍。", "I watched this movie three times (each time from beginning to end)."), ("这部电影我看了三次。", "I watched this movie three times (the process is not emphasized).")]
CB7 = [("今天晚上的作业是把课文读三遍。", "1. Tonight’s homework is to read the text three times. (遍; key mine)"), ("老张，听说你最近身体不好，去过好几次医院了。", "2. Lao Zhang, I heard you haven’t been well lately and have been to the hospital several times. (次)"), ("这个问题你已经问我很多次了，我不想回答你。", "3. You’ve asked me this question many times already; I don’t want to answer. (次)"), ("你的电话号码我没记下来，你能再说一遍吗？", "4. I didn’t write down your phone number; could you say it once more? (遍)"),
       ("你以前见过张老师的太太吗？", "5. A: Have you met Teacher Zhang’s wife before?"), ("见过。就见过一次。", "B: Yes, just once. (次)"), ("你一个星期上几次瑜伽课？", "6. A: How many yoga classes do you take a week?"), ("只上两次。", "B: Only two. (次)")]
L5 = lesson(
    "Lesson 17 Presentation 1 grammar: the verbal measure words 次/遍",
    "看过三遍 · 去过三次医院 · 看过他三次 · 次 and 遍",
    requires=[],
    cards=[
        card("The verbal measure words 次/遍",
             "The verbal measure words 次/遍 are used to form an action-measure complement. As a complement, the numeral-measure unit appears after the verb. When the verb takes an object, the placement of the action-measure varies according to the nature of the object: if the object is a noun, it appears after the measure word; if it is a pronoun, it appears before the measure word. Verb + Number + Measure Word; Verb + Number + Measure Word + Noun; Verb + Pronoun + Number + Measure Word. Both 次 and 遍 indicate the frequency of an action, but 次 indicates the frequency of an action, whereas 遍 emphasizes the entire process of doing something. 这部电影我看了三遍 expresses “I watched a movie three times and every time from the beginning to the end,” while 看了三次 does not emphasize the process of watching at all.",
             examples=[D(z, e) for z, e in CB]),
        card("Activity 7 (Reading, Writing and Speaking)",
             "A. Pair up and complete the sentences using 次 or 遍; then share your work with your partner and explain your choice for each sentence. B. Practice the dialogs aloud with your partner. The book leaves the key out; my completed sentences (mine):",
             examples=[D(z, e) for z, e in CB7]),
    ],
    exercises=[
        M("What does 次 indicate?", "The frequency of an action", ["The whole process", "The duration", "The object"], "次: frequency."),
        M("What does 遍 emphasize?", "The entire process from beginning to end", ["Only the number", "Only the time", "The place"], "遍: process."),
        M("Where does a pronoun object go?", "Before the measure word", ["After the measure word", "At the start", "After the verb and measure"], "我看过他三次."),
        M("Where does a noun object go?", "After the measure word", ["Before the measure word", "At the end of the sentence", "Before the verb"], "我去过三次医院."),
        M("Which is natural for “read the text three times from start to finish”?", "把课文读三遍", ["把课文读三次", "把课文三遍读", "读课文把三遍"], "遍 emphasizes the whole process."),
        M("Which fits “I have been to the hospital several times”?", "去过好几次医院", ["去过好几遍医院", "去好几次过医院", "好几次去医院过"], "次 for frequency."),
        M("Which fits 你的电话号码我没记下来，你能再说一___吗？", "遍", ["次", "个", "回合"], "再说一遍."),
        F("你一个星期上几___瑜伽课？", "次", PART, "几次."),
        F("这个问题你已经问我很多___了。", "次", PART, "很多次."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
LZ1 = ("老张是一个电脑工程师。以前，因为工作忙没有时间去运动。他家住六楼，每天下班回家时，他不坐电梯，而是走楼梯来锻炼身体。最近几年，他感觉天天爬楼梯回家有点儿累，就开始坐电梯了，结果身体变得越来越胖。上个星期，公司为了大家的健康，给每个人一个月发五百块钱，让大家去健身房办一张健身卡。老张不想去，可是如果不办健身卡，公司就不发这五百块了。为了能拿到这些钱，也为了自己的健康，老张只好去办个年卡。")
LZ1_E = ("Lao Zhang is a computer engineer. In the past, because work was busy he had no time to exercise. His home is on the sixth floor, and every day when he came home from work he didn’t take the elevator but walked the stairs to exercise. In recent years he felt that climbing the stairs every day was a bit tiring, so he started taking the elevator, and as a result he got fatter and fatter. Last week the company, for everyone’s health, gave each person 500 yuan a month and asked them to get a gym card at a gym. Lao Zhang didn’t want to go, but if he didn’t get a gym card the company wouldn’t pay out the 500 yuan. In order to get the money, and for his own health, Lao Zhang had no choice but to get an annual card.")
LZ2 = ("老张有了健身卡以后，每天下班以后就去他家附近的健身房。这家健身房刚开不久，里面非常干净漂亮，而且什么器械都有。老张有时候在跑步机上跑步，或者练习举重，有时候还去温水游泳池游泳。几个星期以后，老张感觉身体有力量了，人也瘦了很多，而且每天回家又开始爬楼梯了。周末的时候，他和太太一起去公园锻炼。他太太和朋友们跳广场舞，他就和他的朋友一起打太极拳、下棋。老张觉得生活越来越有意思了。")
LZ2_E = ("After Lao Zhang got the gym card, every day after work he went to the gym near his home. This gym had just opened not long before; it was very clean and pretty inside, and had every kind of equipment. Sometimes Lao Zhang ran on the treadmill or practiced weightlifting, and sometimes he also swam in the warm-water pool. A few weeks later he felt his body had strength, he had become much thinner, and he began climbing the stairs home again every day. On weekends he went to the park with his wife to exercise. His wife and her friends danced square dances while he and his friends practiced Tai Chi and played chess. Lao Zhang felt that life was becoming more and more interesting.")
PU = ("每个到健身房运动的人都有不同的目的，有的人生活和工作太紧张，运动可以让他们放松。有的人是因为太胖了，想要减肥。还有一些人觉得自己太瘦了，想要用运动让自己多长肉。也有一些人不是很胖，但是希望运动可以让自己永远都不胖。请谈谈你的看法：你认为除了去健身房，还有别的方法可以让人们放松，减肥，长肉，不变胖吗？")
PU_E = ("Everyone who goes to the gym has a different purpose: some people’s life and work are too tense, and exercise lets them relax. Some are too fat and want to lose weight. Still others feel they are too thin and want to use exercise to put on muscle. Some are not very fat but hope exercise will keep them from ever getting fat. Please give your view: besides going to the gym, do you think there are other ways for people to relax, lose weight, gain muscle and not get fat?")
L6 = lesson(
    "Lesson 17 Presentation 1: skill integration",
    "老张的健身卡 · 尽管…但是… · 广场舞 · 去健身房的目的",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing, Reading and Speaking)",
             "A. Listen to a news report about Li Kai and write a summary, including three EEIs. B. Pair up and discuss the summary; with your partner, talk about a private fitness studio and private coach in the U.S. that you are familiar with. C. Listen to the sentences and transcribe the missing information (in pinyin), then translate each into English. Sentence 1: 尽管他每小时三百五十到四百五十元，但是李凯的课____。 Sentence 2: 那时候，人们来____，觉得____。 D. Pair up and check your transcriptions and translations. E. Write a sentence using the pattern 尽管…，但是…，and provide an example of how the expression 有面子 is used. F. With your partner, discuss: 1. 美国的健身房多不多？哪些人去健身房运动？ 2. 他们为什么去健身房？ 3. 美国健身房的收费贵不贵？需要办会员卡吗？每月多少钱？ 4. 美国有私人教练吗？你知道一个小时多少钱？ 5. 你常常去学校的健身房吗？你在那儿做什么运动？你觉得那儿怎么样？ (Audio, not included. The book prints the prices as digits.)",
             examples=[D("尽管他每小时要三百五十到四百五十元，但是李凯的课还是很受欢迎。", "Although he charges 350 to 450 yuan per hour, Li Kai’s classes are still very popular. (my own sentence, since the audio is not included; mine)"), D("请这么有名的教练给他上课，他觉得很有面子。", "Having such a famous coach teach him, he feels he has “face”. (my example of 有面子; mine)")]),
        card("Activity 2 (Reading and Speaking): Lao Zhang’s story",
             "A. Read the following passages and answer the questions. Passage 1: 1. What did Lao Zhang do for exercise before? 2. Why did he become heavier in recent years? 3. What prompted him to get an annual fitness card? Passage 2: 1. What activities did Lao Zhang do at the gym? 2. What physical changes did Lao Zhang notice after exercising? 3. Why did Lao Zhang feel that life was becoming more interesting? B. Pair up, compare your answers and share them with the class. C. Discuss: 1. 你还有什么好的健身方法推荐给老张？至少说出两个方法。 2. 如果你每个月有五百美元的健身费，你想怎么健身？为什么要这么做？ D. Report the results of your discussion to the class. The book gives the amount as digits; the new words are 瘦 (shòu; thin), 广场舞 (square dance), 太极拳 (tàijíquán; Tai Chi), 下棋 (xiàqí; chess).",
             examples=[D(LZ1, LZ1_E), D(LZ2, LZ2_E)]),
        card("Activity 3 (Listening, Writing, Reading and Speaking)",
             "A. Listen to the recording and answer the questions in pinyin or characters. New words: 气功 (qìgōng; qigong), 羽毛球 (yǔmáoqiú; badminton), 抱怨 (bàoyuàn; complain), 影响 (yǐngxiǎng; influence, affect). Questions: 中国人在公园里做什么？ 美国人在公园里做什么？ 为什么有的人不喜欢广场舞？ B. Pair up, discuss your answers, identify any unknown words and determine their meanings. C. Discuss: 1. 美国人喜欢什么时候健身？他们怎么健身？ 2. 美国有没有广场舞？他们在哪儿跳广场舞？哪些人喜欢跳广场舞？ (Audio, not included.)"),
        card("Activity 4 (Reading and Speaking)",
             "A. Read the passage. B. In pairs, discuss the topics listed in the table (the purpose 目的: 放松, 减肥, 长肉, 不变胖) and provide at least two solutions for each (你认为适合的方法). C. Report the results of your discussion to the class. New words: 目的 (mùdì; purpose), 瘦 (shòu; thin).",
             examples=[D(PU, PU_E)]),
    ],
    exercises=[
        M("What did Lao Zhang do for exercise before?", "Walked up the stairs to his sixth-floor home", ["Ran in the park", "Went to a gym", "Swam"], "走楼梯来锻炼身体."),
        M("Why did Lao Zhang get fatter?", "He started taking the elevator", ["He ate more", "He slept more", "He stopped working"], "开始坐电梯了，结果身体变得越来越胖."),
        M("Why did Lao Zhang get a gym card?", "The company paid him only if he got one", ["His wife told him", "A doctor told him", "He lost a bet"], "如果不办健身卡，公司就不发这五百块了."),
        M("What did Lao Zhang do at the gym?", "Ran on the treadmill, lifted weights and swam", ["Played basketball", "Did yoga only", "Played chess"], "跑步机上跑步，举重，游泳."),
        M("What changed after a few weeks?", "He felt stronger and became thinner", ["He got fatter", "He got sick", "He quit"], "身体有力量了，人也瘦了很多."),
        M("What does Lao Zhang’s wife do at the park?", "Square dance", ["Tai Chi", "Chess", "Run"], "他太太和朋友们跳广场舞."),
        M("What does Lao Zhang do with friends at the park?", "Tai Chi and chess", ["Square dance", "Badminton", "Swimming"], "打太极拳、下棋."),
        M("Why do some people go to the gym (passage)?", "To relax, lose weight, gain muscle or stay slim", ["Only to socialize", "Only for money", "Only to swim"], "放松、减肥、长肉、不变胖."),
        M("What does 目的 mean?", "Purpose", ["Direction", "Result", "Place"], "目的: purpose."),
        mean("健康", "jian4 kang1", "health", ["hunger", "danger", "strength"]),
        F("他不坐电梯，___是走楼梯来锻炼身体。", "而", PART, "不…而是…"),
        F("老张觉得生活越来越有意___了。", "思", PART, "有意思."),
    ],
)

# ------------------------------------------------------------------ 7. context
CTX = table(["你想知道的信息 (what you want to know)", "你朋友要告诉你的信息 (what your friend tells you)"],
            [["这个健身房在哪儿？", "健身房离学校很近"], ["你在那里健身有多久了？", "在那里健身差不多半年了"], ["你觉得这个健身房怎么样？", "又大又干净"], ["里面有什么器械？", "器械很全"], ["你在那儿做什么运动？", "温水游泳池，跑步机，举重，骑单车，瑜伽"], ["怎么收费？是每月还是每个小时？", "力量训练，受伤"],
             ["如果办年卡，需要多少钱？", "办年卡，有优惠，买一送一"], ["如果是新会员，有没有优惠？", "我认识一个私人教练，耐心"], ["第一次去健身是不是免费？", "给他打电话"], ["这个健身房有私人教练吗？", "他的号码是一三三四五六七八九一零"], ["私人教练怎么收费？", "（the book’s last cell is cut off）"]],
            title="Activity 1 (the book prints two lists side by side; the row alignment here is only approximate, and the phone number is spelled out)", say=[0])
L7 = lesson(
    "Lesson 17 Presentation 1: using Chinese in context",
    "在北京找健身房 · 超重同学的健身计划 · 私人教练的广告",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): role play",
             "Role-play: You have been studying Chinese in Beijing for over three months. The Chinese course is very intensive, and you feel tired every day, so you are thinking about finding a gym so that you can energize yourself and stay fit. You’ve learned that your Chinese friend has been going to a gym for a long time and you’d like to join it. Ask your friend about joining the gym. A. Pair up. Your partner plays the role of your Chinese friend and you ask about joining the gym, using the information below as a reference. B. Write your partner’s responses below for your reference. C. Switch roles with your partner and repeat the conversation.",
             tables=[CTX]),
        card("Activity 2 (Reading, Writing and Speaking): a fitness plan",
             "Scenario: You are studying Chinese at a military language institute in Monterey, California. In a recent physical test, one of your classmates failed due to his weight. In order to help him lose the excess weight, you are tasked by your supervisor to make a fitness plan for him. Divide the class into two groups. Each group designs a plan and presents it to the class. Select the best one and then email it to your supervisor. A. In groups, brainstorm and discuss a fitness plan for your overweight classmate. Your plan can include: 1. 这个同学的身体有什么问题？ 2. 他每天应该几点起床，几点睡觉？ 3. 他适合做什么运动？什么时候做？ 4. 做这些运动为什么对他好？ 5. 他每天应该吃什么、喝什么？ 6. 他不应该吃什么、喝什么？ 7. 除了这些以外，他还应该做什么？ B. Note the details of your plan with your group members (健身计划). C. Each group takes turns presenting their fitness plan to the class, and the class selects the best one. D. Write an email to your supervisor and submit your best fitness plan."),
        card("Activity 3 (Listening, Reading and Speaking): the coach’s commercial",
             "Scenario: You have been working in the U.S. Embassy in Beijing for more than three months and you are very tired after work, so you’d like to find a gym and work out with a coach. Yesterday, on your way home, you heard a commercial on the radio about a fitness coach. You call this coach and ask him about the gym and his program. A. Listen to the commercial and answer the questions: 1. 这个广告主要说什么？ 2. 李刚是什么样的人？他会帮你做什么？ 3. 你觉得你会去这个健身馆吗？为什么？ B. Pair up and discuss your answers; read the script if necessary. C. Role-play. With your partner, call the fitness coach about the gym and fitness program; your partner plays the coach. You may ask: 你的健身馆在哪儿？ 你在那儿当健身教练多久了？ 你们那里都有什么运动器械？ 你怎么帮我制定健身计划？ 如果你帮我训练，每天多长时间？ 你怎么收费？ 我可以不可以先试试你的课？ D. Note your partner’s responses below for your reference. E. Switch roles and repeat the role-play. (Audio and script, not included.)"),
    ],
    exercises=[
        M("Where is the friend’s gym?", "Very close to the school", ["Far from the school", "In another city", "At home"], "健身房离学校很近."),
        M("How long has the friend gone there?", "About half a year", ["A week", "Ten years", "A day"], "差不多半年了."),
        M("What is the gym like?", "Big and clean with complete equipment", ["Small and old", "Dirty", "Empty"], "又大又干净，器械很全."),
        M("What activities are available?", "Warm-water pool, treadmill, weights, cycling, yoga", ["Only yoga", "Only weights", "Only swimming"], "温水游泳池，跑步机，举重，骑单车，瑜伽."),
        M("What discount is mentioned for annual cards?", "Buy one, get one free", ["Half price", "No discount", "Free first month"], "办年卡，有优惠，买一送一."),
        M("What trouble can strength training cause?", "Injury", ["Sleep", "Hunger", "Thirst"], "力量训练，受伤."),
        M("What do you ask the coach in Activity 3?", "Where the gym is, how long he has coached, equipment, plan, time and price", ["Only the price", "Only the phone number", "Nothing"], "你的健身馆在哪儿…"),
        M("What is Activity 2’s task?", "Make a fitness plan for an overweight classmate", ["Plan a trip", "Plan a party", "Write a story"], "Fitness plan."),
        F("我认识一个私人教练，很有耐___。", "心", PART, "耐心: patient."),
        F("你的健身馆在哪___？", "儿", PART, "哪儿: where."),
    ],
)
L8 = vocab_lesson("Lesson 17 Presentation 1 vocabulary", "28 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十七课 体育健身 Presentation 1: gym, 好 (many), 呢, 能, 次/遍, Lao Zhang’s fitness plan", [L1, L2, L3, L4, L5, L6, L7, L8])
