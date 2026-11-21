"""Unit 69: Lesson 24 (Unit 4 review), the vocabulary review from the book's texts: the meaning of each character, words with 假 速 病 邮,
synonyms and antonyms, questions for given answers, word order, and the Lesson 21 concept map. Audio, pictures and the board game are not
included; the book prints no answer keys for these activities, so the answers and sample words are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('恶心', 0, 'e3'), ('还是', 0, 'hai2'), ('还有', 0, 'hai2'), ('得不错', 0, 'de5'), ('假', 0, 'jia4')):
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

# ------------------------------------------------------------------ 1. activity 1
T1 = table(["A 栏", "B 栏"], [["特等", "进步"], ["身份证", "快递量"], ["腹泻", "代售"], ["贺卡", "预订"], ["沿途", "病历"], ["行驶", "病情"], ["确诊", "验血"], ["提高", "原因"], ["增加", "快递"], ["代发", "往返"], ["手艺", "易碎"], ["经验", "海运"]],
           title="Activity 1: Column A and Column B (the book underlines one character in each word; the underlining is not in the text)", say=[0, 1])
L1 = lesson(
    "Lesson 24 Vocabulary Review: the meaning of each character",
    "特等 腹泻 沿途 · 进步 代售 易碎 · 每个字的意思",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Speaking, Listening and Writing)",
             "When previewing or reviewing vocabulary, knowing the meaning of the vocabulary as a whole is important, but knowing the meaning of each character is equally as important. It will help you expand your vocabulary by knowing the core meaning of characters in vocabulary. A. Pair up. Student A will read each vocabulary item in column A aloud and determine the meaning of the underlined characters in each phrase. Student B will do the same for column B. B. Students A and B each pick three words from the other column to form sentences. Their partner then translates the sentences.",
             tables=[T1]),
        card("Core meanings of some characters (mine)",
             "The book gives no key. These meanings are mine: 特 special (特等 special class); 腹 belly (腹泻 diarrhea); 贺 congratulate (贺卡 greeting card); 沿 along (沿途 along the way); 驶 drive (行驶 travel by vehicle); 确 definite (确诊 diagnose for certain); 提 raise (提高 raise, improve); 增 increase (增加 increase); 代 on behalf of (代发 issue on behalf of); 艺 skill (手艺 craftsmanship); 进 advance (进步 progress); 量 amount (快递量 express volume); 售 sell (代售 sell as an agent); 订 book (预订 book in advance); 历 record (病历 medical record); 情 condition (病情 state of an illness); 验 test (验血 blood test); 因 cause (原因 reason); 递 deliver (快递 express delivery); 返 return (往返 round trip); 易 easy (易碎 easily broken); 运 transport (海运 sea transport)."),
    ],
    exercises=[
        M("In 特等, what does 特 mean?", "Special", ["Very cheap", "Fast", "Old"], "特: special."),
        M("In 腹泻, what does 腹 mean?", "Belly", ["Foot", "Head", "Hand"], "腹: belly."),
        M("In 贺卡, what does 贺 mean?", "Congratulate", ["Complain", "Send", "Borrow"], "贺: congratulate."),
        M("In 沿途, what does 沿 mean?", "Along", ["Across", "Against", "After"], "沿: along."),
        M("In 确诊, what does 确 mean?", "Definite", ["Possible", "Slow", "Wrong"], "确: certain."),
        M("In 代发, what does 代 mean?", "On behalf of", ["Generation only", "Before", "Instead of nothing"], "代: on behalf of."),
        M("In 手艺, what does 艺 mean?", "Skill", ["Art museum", "Hand", "Taste"], "艺: skill, art."),
        M("In 易碎, what does 易 mean?", "Easy", ["Heavy", "Hard", "Cheap"], "易: easy."),
        M("In 海运, what does 运 mean?", "Transport", ["Luck only", "Sea", "Lose"], "运: transport."),
        M("In 往返, what does 返 mean?", "Return", ["Go", "Wait", "Pay"], "返: return."),
        M("In 快递量, what does 量 mean?", "Amount", ["Measure only", "Speed", "Weight only"], "量: amount."),
        M("In 预订, what does 预 mean?", "In advance", ["After", "Together", "Free"], "预: in advance."),
        F("身___证", "份", PART, "身份证: ID card."),
        F("快___量", "递", PART, "快递: express delivery."),
    ],
)

# ------------------------------------------------------------------ 2. activity 2
T2 = table(["假", "速", "病", "邮"], [["放假", "高速", "病人", "邮局"], ["病假", "快速", "病房", "邮票"], ["请假", "速度", "病历", "邮费"], ["假期", "减速", "病情", "邮件"], ["暑假", "加速", "看病", "邮筒"], ["假日", "快速", "生病", "邮寄"]],
           title="Activity 2A: words that contain one character (the book gives only the four characters; the words are mine, mostly from the Unit 4 lessons)", say=[0, 1, 2, 3])
SYN = [("交流，交通，表达，填表", "1. Mine: 交流 and 表达 are close in meaning (communicate / express); none of these is the opposite of another."),
       ("休息，体会，体检，体验", "2. Mine: 体会 and 体验 are close in meaning (to experience, to appreciate)."),
       ("运行，锻炼，健身，空运", "3. Mine: 锻炼 and 健身 are close in meaning (to exercise); 运行 means to run (a service) and 空运 is air transport."),
       ("进步，散步，发展，出发", "4. Mine: 进步 and 发展 are close in meaning (progress / develop); 散步 is to take a walk and 出发 is to set off."),
       ("增加，提供，提取，减少", "5. Mine: 增加 and 减少 are opposites (increase / decrease); 提供 provides and 提取 withdraws."),
       ("空闲，繁忙，舒服，适合", "6. Mine: 空闲 and 繁忙 are opposites (free / busy); 舒服 and 适合 are both about being comfortable or fitting.")]
L2 = lesson(
    "Lesson 24 Vocabulary Review: words with 假 速 病 邮, synonyms and antonyms",
    "放假 高速 病人 邮局 · 交流 表达 · 增加 减少 · 空闲 繁忙",
    requires=[],
    cards=[
        card("Activity 2 (Reading, Speaking and Listening)",
             "A. Form groups of three. Your teacher will show one character (from the table) at a time. Each group will think of as many vocabulary/phrases that contain that character as they can. The teacher will set a time to complete the task. The team that compiles the most vocabulary wins. B. Read each set of words below and highlight the words that share similar meanings (synonyms) or have opposite meanings (antonyms). The book gives no key; my answers are in the next card. C. Using the words in Part B, select three non-answer words and explain the meaning of that phrase in your own words, without giving away the exact wording. Your partner will guess which phrase you are suggesting. Students take turns. For example: 做这件事的时候，有时候你需要验血、验尿 — answer: 体检.",
             tables=[T2]),
        card("Part B: the six sets of words (answers mine)", "Each set is printed with “synonyms?” and “antonyms?” beside it.", examples=[D(z, e) for z, e in SYN]),
    ],
    exercises=[
        M("Which pair of words are close in meaning?", "交流 and 表达", ["交通 and 填表", "交流 and 填表", "交通 and 表达"], "交流 ≈ 表达."),
        M("Which pair of words are close in meaning?", "体会 and 体验", ["休息 and 体检", "体检 and 体会", "休息 and 体验"], "体会 ≈ 体验."),
        M("Which pair of words are close in meaning?", "锻炼 and 健身", ["运行 and 空运", "运行 and 健身", "空运 and 锻炼"], "锻炼 ≈ 健身."),
        M("Which pair of words are close in meaning?", "进步 and 发展", ["散步 and 出发", "散步 and 发展", "进步 and 出发"], "进步 ≈ 发展."),
        M("Which pair of words are opposites?", "增加 and 减少", ["提供 and 提取 (exactly opposite)", "增加 and 提供", "提取 and 减少"], "增加 ↔ 减少."),
        M("Which pair of words are opposites?", "空闲 and 繁忙", ["舒服 and 适合", "空闲 and 舒服", "繁忙 and 适合"], "空闲 ↔ 繁忙."),
        M("做这件事的时候，有时候你需要验血、验尿 — which word fits?", "体检", ["体验", "体会", "休息"], "体检: a physical examination."),
        M("Which word does NOT contain 病?", "放假", ["病人", "病房", "病历"], "放假 has 假."),
        M("Which word does NOT contain 邮?", "快递", ["邮局", "邮票", "邮筒"], "快递 has no 邮."),
        M("Which word contains 速?", "高速", ["放假", "邮寄", "病情"], "高速: expressway."),
        F("你每年什么时候放___？", "假", PART, "放假: have a holiday."),
        F("请把包裹放进___筒里。", "邮", PART, "邮筒: post box."),
    ],
)

# ------------------------------------------------------------------ 3. activities 3 and 4
QA = [("快递要几个工作日才能到？", "Q (mine) to the book’s answer 1. How many working days does express take to arrive?"),
      ("三个工作日。", "A (book) 1. Three working days."),
      ("寄国际包裹要填什么表？", "Q (mine) to answer 2. What forms do you fill in to send an international package?"),
      ("海关申报单、包裹单。", "A (book) 2. A customs declaration form and a package form."),
      ("你哪儿不舒服？", "Q (mine) to answer 3. Where do you feel unwell?"),
      ("我发烧、咳嗽，头也疼得厉害。", "A (book) 3. I have a fever and a cough, and my head hurts badly too."),
      ("这个药怎么吃？", "Q (mine) to answer 4. How should I take this medicine?"),
      ("一天三次，一次两片，最好饭后吃。", "A (book) 4. Three times a day, two tablets each time, best after meals."),
      ("高铁上有什么样的座位？", "Q (mine) to answer 5. What kinds of seats are there on the high-speed train?"),
      ("有一等座、二等座，还有商务座和特等座。", "A (book) 5. There are first-class seats and second-class seats, and also business-class and premium seats."),
      ("高铁票怎么买？", "Q (mine) to answer 6. How do I buy a high-speed train ticket?"),
      ("你可以在网上或者在手机上预订，当然也可以直接到车站去买。", "A (book) 6. You can book online or on your phone, and of course you can also buy directly at the station.")]
RE = [("沿着这条路一直往东走。", "1. Go straight east along this road. (my order; the words: 路 沿着 往 一直 这 条 走 东)"),
      ("为了给孩子付大学学费，他周末甚至也工作。", "2. In order to pay his child’s college tuition he even works on weekends. (my order)"),
      ("如果你的身体不好，你就应该少吃快餐，多锻炼身体。", "3. If your health is poor, you should eat less fast food and exercise more. (my order)"),
      ("高铁票比机票便宜一点儿，我还是坐高铁吧。", "4. High-speed train tickets are a bit cheaper than plane tickets; I’d better take the train. (my order)"),
      ("你今天在语法课上回答问题回答得不错。", "5. You answered questions quite well in grammar class today. (my order)"),
      ("我把医生开的病假单拿给老师签字。", "6. I take the sick-leave slip the doctor issued to the teacher to sign. (my order)")]
L3 = lesson(
    "Lesson 24 Vocabulary Review: questions for given answers and word order",
    "三个工作日 · 海关申报单 · 一天三次 · 沿着这条路 · 把病假单拿给老师",
    requires=[],
    cards=[
        card("Activity 3 (Listening, Reading and Speaking)",
             "A. Listen to each question and answer them using what you know and have learned from the presentations (audio, not included). B. Pair up. Students check their answers by retelling the conversation. C. Read the answer for each question and recreate its question. D. Pair up. Student A will ask the question and Student B will answer. Students take turns. The book prints the six answers and leaves the questions blank; the questions are mine:",
             examples=[D(z, e) for z, e in QA]),
        card("Activity 4 (Listening, Reading and Speaking)",
             "A. Listen to and translate each of the following sentences (audio, not included). B. Rearrange the following words to form a logical sentence, then translate the sentence into English. The words as printed: 1. 路 沿着 往 一直 这 条 走 东. 2. 大学 孩子 付 为了 给 学费 周末 工作 他 也 甚至. 3. 你的 不好 就 你 锻炼身体 少 吃 如果 快餐 应该 身体 多. 4. 高铁票 我 比 一点儿 高铁 吧 机票 还是 坐 便宜. 5. 上 回答 语法课 不错 在 今天 你 问题 回答 得. 6. 我 病假单 医生 老师 把 开的 拿给 签字. C. Pair up. Check your answers with those of your partner. The book leaves the sentences blank; mine:",
             examples=[D(z, e) for z, e in RE]),
    ],
    exercises=[
        M("Which question fits the answer 三个工作日？", "快递要几个工作日才能到？", ["你哪儿不舒服？", "这个药怎么吃？", "高铁票怎么买？"], "Asks how long."),
        M("Which question fits the answer 海关申报单、包裹单？", "寄国际包裹要填什么表？", ["高铁上有什么座位？", "你有几个孩子？", "你想吃什么？"], "Forms."),
        M("Which question fits the answer 我发烧、咳嗽，头也疼得厉害？", "你哪儿不舒服？", ["你去哪儿？", "邮局在哪儿？", "你叫什么名字？"], "Symptoms."),
        M("Which question fits the answer 一天三次，一次两片？", "这个药怎么吃？", ["你怎么去？", "这个药多少钱？", "你发烧吗？"], "Dosage."),
        M("Which question fits the answer 有一等座、二等座，还有商务座和特等座？", "高铁上有什么样的座位？", ["几点出发？", "几点到北京？", "票价多少？"], "Seat classes."),
        M("Which question fits the answer 你可以在网上或者在手机上预订？", "高铁票怎么买？", ["你在哪儿工作？", "你多大了？", "药店在哪儿？"], "How to buy."),
        M("What does 沿着这条路一直往东走 mean?", "Go straight east along this road", ["Turn west at this road", "Stop at the east gate", "Take the road home"], "沿着…一直往…走."),
        M("What does 他周末甚至也工作 mean?", "He even works on weekends", ["He rests on weekends", "He works only on weekends", "He never works"], "甚至: even."),
        M("What does 如果你的身体不好，你就应该少吃快餐 mean?", "If your health is poor you should eat less fast food", ["Eat more fast food", "Your body is good", "Fast food is healthy"], "如果…就…."),
        M("What does 我把病假单拿给老师签字 mean?", "I take the sick-leave slip to the teacher to sign", ["I lose the slip", "The teacher gives me a slip", "I sign for the teacher"], "把…拿给…."),
        F("你今天在语法课上回答问题回答___不错。", "得", PART, "V + 得 + adj."),
        F("高铁票比机票便宜一点儿，我___是坐高铁吧。", "还", PART, "还是: had better."),
    ],
)

# ------------------------------------------------------------------ 4. activities 5 and 6
CM = table(["类别", "词"], [["医院的部门", "内科 外科 门诊"], ["看病的证件", "身份证 医保卡 病历卡"], ["看病的手续", "预约 挂号 划价 付费 取药"], ["症状", "发烧 咳嗽 流鼻水 嗓子疼 腹泻 呕吐 恶心"], ["检查", "量心跳 量血压 验血 验尿 透视"], ["治疗", "打针 吃药 开药 喝水"], ["病名", "感冒 流感 肺炎 肠胃炎"]],
           title="Activity 5A: the concept map around 看医生 (my placement; the book gives the 31 words and the seven category names and leaves the map blank; the book writes 恶心 as 噁心)", say=[0, 1])
L4 = lesson(
    "Lesson 24 Vocabulary Review: the Lesson 21 concept map and the board game",
    "看医生 · 医院的部门 看病的证件 看病的手续 · 症状 检查 治疗 病名",
    requires=[],
    cards=[
        card("Activity 5 (Reading, Speaking and Listening)",
             "A. Below is vocabulary you learned in Lesson 21. Use the concept map to place the words in the correct categories. The words: 透视 噁心 肠胃炎 验血 呕吐 取药 验尿 发烧 身份证 外科 打针 腹泻 流感 感冒 门诊 肺炎 医保卡 吃药 流鼻水 划价 量心跳 量血压 嗓子疼 咳嗽 预约 挂号 开药 喝水 病历卡 付费 内科. The categories: 医院的部门 · 治疗 · 看病的证件 · 看病的手续 · 看医生 (the centre) · 症状 · 检查 · 病名. B. Pair up. Take turns writing three sentences that use at least two vocabulary words from the concept map. Your partner will translate your sentences.",
             tables=[CM]),
        card("Activity 6 (Reading, Speaking and Listening)",
             "Board Game: Form groups of three. Each member will roll the die and move their marker the number of spaces shown on the die and answer the question in that space. Answer in complete sentences. Some spaces may require you to say more than one sentence. If your marker falls on a purple space, you can pick any topic to speak about. If your marker falls on an orange space, your partner chooses a question for you. (The board is a picture and is not included.)"),
    ],
    exercises=[
        M("Which category does 内科 belong to?", "医院的部门", ["症状", "病名", "检查"], "内科 is a department."),
        M("Which category does 医保卡 belong to?", "看病的证件", ["治疗", "症状", "病名"], "A document for seeing a doctor."),
        M("Which category does 挂号 belong to?", "看病的手续", ["症状", "检查", "病名"], "A procedure."),
        M("Which category does 咳嗽 belong to?", "症状", ["治疗", "检查", "病名"], "A symptom."),
        M("Which category does 验血 belong to?", "检查", ["治疗", "症状", "病名"], "An examination."),
        M("Which category does 打针 belong to?", "治疗", ["检查", "症状", "病名"], "A treatment."),
        M("Which category does 肺炎 belong to?", "病名", ["治疗", "检查", "症状"], "An illness name."),
        M("Which is a symptom?", "嗓子疼", ["划价", "门诊", "病历卡"], "A sore throat."),
        M("Which is a document?", "身份证", ["预约", "付费", "取药"], "ID card."),
        M("Which is an examination?", "量血压", ["吃药", "喝水", "外科"], "Taking blood pressure."),
        F("我想预___一个专家门诊。", "约", PART, "预约: make an appointment."),
        F("请先去挂___，再去划价。", "号", PART, "挂号: register."),
    ],
)

UNIT = unit("第二十四课 Unit 4 review: vocabulary review", [L1, L2, L3, L4])
