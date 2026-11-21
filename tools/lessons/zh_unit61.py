"""Unit 61: Lesson 21 (Seeing a Doctor) Presentation 2 from the book's texts: the flu dialog, the five activities, degree complements with 得,
adjectives as predicates (2), 多/少 快/慢 早/晚 before a verb, the skill-integration activities (medicine words, cold/flu/pneumonia passages, Lin Qiang),
the using-Chinese activities and the vocabulary list. Audio, pictures, videos and links are not included; numbers the book writes as digits are
spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l21_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('得的是', 0, 'de2'), ('我得的', 1, 'de2'), ('得了肺炎', 0, 'de2'), ('得打针', 0, 'dei3'), ('得吃', 0, 'dei3'), ('得做什么', 0, 'dei3'), ('看好', 0, 'kan1'), ('量量', 0, 'liang2'), ('量量', 1, 'liang2'), ('量血压', 0, 'liang2'), ('量体温', 0, 'liang2'), ('量一下', 0, 'liang2'), ('量了体', 0, 'liang2'), ('口干', 1, 'gan1'), ('也干', 1, 'gan1'), ('干净', 0, 'gan1'), ('觉得', 1, 'de5')):
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
P2 = [("医生", "你哪儿不舒服？", "Where do you feel unwell?"), ("病人", "我发烧、咳嗽，头也疼得厉害。", "I have a fever and a cough, and my head hurts badly too."), ("医生", "发烧多长时间了？", "How long have you had the fever?"),
      ("病人", "从前天早上就开始了。嗓子疼，口也干，头也有点儿晕。", "It started the morning before yesterday. My throat hurts, my mouth is dry and I’m a bit dizzy too."), ("医生", "好，先量量体温吧。三十八度五。流鼻涕吗？", "OK, let’s take your temperature first. 38.5 degrees. Do you have a runny nose? (the book has a hesitation sound before the number; I left it out because it has no standard pinyin syllable here)"),
      ("病人", "前两天流得厉害，今天不流了，但是有点堵。", "It ran badly for the past couple of days; today it has stopped, but it’s a bit blocked."), ("医生", "我听一下你的心脏，再量一下血压。", "I’ll listen to your heart and then measure your blood pressure."),
      ("病人", "大夫，都还正常吧？", "Doctor, is everything still normal?"), ("医生", "还好。看起来你得的是流感。我先给你开点儿药，再打一针，看看怎么样。", "Fine. It looks like you have the flu. I’ll first prescribe some medicine and then give you an injection, and see how it goes."),
      ("病人", "流感啊？我还担心是肺炎呢。", "The flu? I was still worried it was pneumonia."), ("医生", "不用担心。多喝水，好好休息。过两天还不好的话，再来做检查。这是你的药方。", "No need to worry. Drink more water and rest well. If you’re still not better in a couple of days, come back for an examination. Here is your prescription."),
      ("病人", "大夫，这个药我怎么吃呢？", "Doctor, how do I take this medicine?"), ("医生", "一天三次，一次两片。最好饭后吃。", "Three times a day, two tablets each time. It’s best taken after meals."),
      ("病人", "去哪儿取药和打针？", "Where do I go to collect the medicine and get the injection?"), ("医生", "先到一楼划价，付费。然后去二楼取药，打针。", "First go to the first floor to have the price worked out and pay. Then go to the second floor to collect the medicine and get the injection."),
      ("病人", "大夫，谢谢您！", "Doctor, thank you!")]
L1 = lesson(
    "Lesson 21 Presentation 2: seeing the doctor with a fever",
    "你哪儿不舒服 · 发烧 咳嗽 头疼 · 量体温 量血压 听心脏 · 流感 · 药方 划价 取药",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. When you have the flu, what are the common symptoms? B. What are the standard examinations your doctors give you during a visit? C. If you have a cold or the flu, what treatment does your doctor provide? What are your home remedies? (Four small pictures, not included.)"),
        card("Presentation 2: 看病", "The book also prints the dialog in traditional characters; the numbers are written in characters. The translations are mine.", examples=dlg(P2)),
    ],
    exercises=[
        M("What are the patient’s main complaints?", "Fever, cough and a bad headache", ["A stomach ache", "A broken leg", "A rash"], "我发烧、咳嗽，头也疼得厉害."),
        M("Since when has he had the fever?", "Since the morning before yesterday", ["Since last week", "Since this morning", "Since last month"], "从前天早上就开始了."),
        M("What other symptoms does he mention?", "Sore throat, dry mouth and slight dizziness", ["Toothache and backache", "A rash and itching", "Chest pain and a limp"], "嗓子疼，口也干，头也有点儿晕."),
        M("What is his temperature?", "38.5 degrees", ["37.8 degrees", "39 degrees", "36 degrees"], "三十八度五."),
        M("How is his runny nose now?", "It stopped but is a bit blocked", ["Still very bad", "Never started", "Completely clear"], "今天不流了，但是有点堵."),
        M("Which two examinations does the doctor do after the temperature?", "Listen to the heart and measure blood pressure", ["X-ray and blood test", "Urine and stool tests", "Eye and ear tests"], "听一下你的心脏，再量一下血压."),
        M("What does the doctor say the patient has?", "The flu", ["Pneumonia", "A cold", "Food poisoning"], "你得的是流感."),
        M("What was the patient worried about?", "Pneumonia", ["The flu", "A heart problem", "A broken bone"], "我还担心是肺炎."),
        M("How should he take the medicine?", "Three times a day, two tablets, best after meals", ["Once a day, one tablet", "Twice a day before meals", "Every hour"], "一天三次，一次两片。最好饭后吃."),
        M("Where does he go first, and then?", "First floor to pay, then second floor for medicine and injection", ["Second floor first, then first floor", "Straight home", "The pharmacy on the third floor"], "先到一楼划价，付费。然后去二楼取药，打针."),
        F("我发烧、咳___，头也疼得厉害。", "嗽", PART, "咳嗽: cough."),
        F("好，先量量体___吧。", "温", PART, "体温: body temperature."),
        F("我听一下你的心___，再量一下血压。", "脏", PART, "心脏: heart."),
        F("先到一楼划___，付费。", "价", PART, "划价: work out the price."),
    ],
)

# ------------------------------------------------------------------ 2. activities
CATG = table(["症状 (Symptoms)", "检查 (Checkups)", "诊断 (Diagnoses)", "治疗 (Treatment)"],
             [["发烧，咳嗽，头疼，嗓子疼，口干，拉肚子，头晕，流鼻涕，鼻子堵", "量体温，量血压，听心脏，验血，透视", "流感，肺炎，感冒", "休息，吃药，打针，喝水"]],
             title="Activity 2: sorting the 21 words (the book leaves the table blank; this is my sorting)", say=[0, 1, 2, 3])
MT21 = [("发烧有多长时间了？", "从昨天晚上九点开始的。", "1 + D. How long have you had the fever? — It began at nine last night. (key mine; the book writes 9 点)"), ("我得的是什么病？", "你看起来得的是流感。", "2 + G. What illness do I have? — It looks like you have the flu. (the book prints 你看起来的是流感, without 得)"),
        ("这个药我怎么吃？", "一天三次，一次一片，饭前和饭后吃都行。", "3 + A. How do I take this medicine? — Three times a day, one tablet at a time, before or after meals."), ("我去哪儿打针？", "在一楼划价、取药，然后去二楼打针。", "4 + F. Where do I go for the injection? — Work out the price and collect medicine on the first floor, then go to the second floor for the injection."),
        ("你哪儿不舒服？", "我发烧、咳嗽，头疼得厉害。", "5 + C. Where do you feel unwell? — I have a fever and a cough, and a bad headache."), ("我得做什么检查？", "量量血压、听一下心脏，再量一下体温。", "6 + B. What examinations do I need? — Measure the blood pressure, listen to the heart and take the temperature."),
        ("我发高烧吗？", "没有，你发低烧。三十七度八。", "7 + E. Do I have a high fever? — No, you have a low fever, 37.8 degrees. (key mine)")]
MQ = []
for q, a, e in MT21:
    lab, rest = e.split(". ", 1)
    qen, aen = rest.split(" — ", 1)
    MQ += dlg([("甲", q, lab + ". " + qen), ("乙", a, aen)])
L2 = lesson(
    "Lesson 21 Presentation 2 activities: symptoms, checkups, diagnoses and treatment",
    "Activities 1 to 5 · 症状 检查 诊断 治疗 · 问答配对 · 我的同学看病",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 2 once and answer: 1. What is the relationship between the two speakers? 2. What steps did the two speakers complete? B. Detailed listening: 1. What’s wrong with the second speaker? Check all the answers given (pictures). 2. What checkups did the first speaker conduct? Check all answers you hear (pictures). 3. What diagnosis was made? What treatment will the second speaker receive? 4. What was the patient’s concern? 5. What are the suggestions given to the second speaker? 6. How should the patient take his or her medicine? 7. What directions are given at the end? (the first floor and second floor lists) (Audio and pictures, not included; the answers are in the dialog.)"),
        card("Activity 2 (Reading, Writing and Speaking)",
             "A. Pair up and write the words 发烧, 量体温, 咳嗽, 量血压, 头疼, 听心脏, 嗓子疼, 验血, 口干, 流感, 拉肚子, 肺炎, 头晕, 休息, 吃药, 流鼻涕, 打针, 鼻子堵, 喝水, 透视, 感冒 in the correct columns; the pair that finishes first wins. B. Share your answers with the class.",
             tables=[CATG]),
        card("Activity 3 (Reading and Speaking)",
             "A. Match the questions in Column A with the answers in Column B (the book prints the seven questions numbered 1–7 and the answers lettered A–G, and a middle column for the letter; it prints no key). B. Share your answers with a classmate and take turns asking and answering. My pairs:",
             examples=MQ),
        card("Activity 4 and Activity 5",
             "Activity 4 (Listening, Writing and Speaking): A. Listen to the dialog and take notes in the table (症状, 病因, 检查, 诊断, 治疗, 医生建议, 怎么吃药) and share with your partner. B. Retell the story in your own words. (Audio, not included.) Activity 5 (Speaking, Listening and Writing): A. Interview two of your classmates about recent doctor’s visits and take notes in the table (什么时候, 什么地方, 为什么看医生, 症状, 医生检查, 医生诊断, 什么治疗, 医生建议, 其他信息). B. Pair up and share your information, comparing your classmates’ doctor visits."),
    ],
    exercises=[
        M("Which of these is a symptom?", "咳嗽", ["量血压", "流感", "打针"], "咳嗽 is a symptom."),
        M("Which of these is a checkup?", "听心脏", ["头晕", "肺炎", "喝水"], "听心脏 is a checkup."),
        M("Which of these is a diagnosis?", "肺炎", ["嗓子疼", "透视", "休息"], "肺炎 is a diagnosis."),
        M("Which of these is a treatment?", "打针", ["口干", "验血", "感冒"], "打针 is a treatment."),
        M("Which answer goes with “我得做什么检查？”", "量量血压、听一下心脏，再量一下体温", ["一天三次，一次一片", "我发烧、咳嗽", "在一楼划价、取药"], "6 + B."),
        M("Which answer goes with “这个药我怎么吃？”", "一天三次，一次一片，饭前和饭后吃都行", ["你看起来得的是流感", "没有，你发低烧", "我发烧、咳嗽，头疼得厉害"], "3 + A."),
        M("What temperature counts as low fever in the dialog?", "37.8 degrees", ["39 degrees", "35 degrees", "40 degrees"], "你发低烧。三十七度八."),
        M("Which question asks how long the fever has lasted?", "发烧有多长时间了？", ["我发高烧吗？", "我去哪儿打针？", "你哪儿不舒服？"], "1 + D."),
        F("你看起来得的是流___。", "感", PART, "流感: flu."),
        F("你发低___。", "烧", PART, "低烧: low fever."),
    ],
)

# ------------------------------------------------------------------ 3. degree complements
DV = table(["", "格式"], [["Without objects", "V + 得 + degree complement (degree adverb + adjective)"], ["With objects", "V + O + V + 得 + degree complement"], ["Negative", "V + 得 + 不 + degree complement (adjective)"], ["Interrogative", "V + 得 + complement (adjective) + 不 + complement (adjective)"]],
          title="Verbs with degree complements (Verb + 得 + degree complement)")
DE1 = [("前两天流得厉害，今天不流了，但是有点堵。", "1. I had a very bad runny nose over the past couple of days. Today it stopped, but my nose is a bit stuffy."), ("我发烧、咳嗽，头也疼得厉害。", "2. I had a fever and a cough. My headache was really bad, too.")]
DE2 = [("他每天起得很早。", "1. He gets up very early every day."), ("王老师讲得真好。", "2. Teacher Wang explains really well."), ("李平学得快，我学得慢。", "3. Li Ping learns fast, I learn slowly."), ("她回答问题回答得很好。", "4. She answers questions very well."), ("他说中文说得非常好。", "5. He speaks Chinese extremely well."), ("昨天晚上我睡得不好。", "6. I didn’t sleep well last night."), ("昨天晚上你睡得好不好？", "7. Did you sleep well last night?"), ("昨天晚上你睡觉睡得好不好？", "7. Did you sleep well last night? (with the object 睡觉)")]
DE3 = [("他身体好得很。", "1. His health is very good."), ("我肚子疼得厉害。", "2. My stomach hurts badly."), ("张华最近忙得要命。", "3. Zhang Hua has been extremely busy lately."), ("她高兴得跳了起来。", "4. She was so happy that she jumped up."), ("她累得说不出话。", "5. She was so tired she couldn’t speak."), ("周末的时候，马克累得不想起床。", "6. At the weekend Mark was so tired he didn’t want to get up."), ("他今天开心得很。", "7. He is very happy today."), ("他今天开心得唱起歌来。", "7. He was so happy today that he started singing.")]
DQ = [("你昨天晚上睡得好不好？", "Did you sleep well last night? (Activity 2B, mine)"), ("你打篮球打得怎么样？", "How well do you play basketball? (mine)"), ("你做饭做得好不好？", "Do you cook well? (mine)"), ("我唱歌唱得不太好。", "I don’t sing very well. (mine)"), ("你汉字写得快不快？", "Do you write characters fast? (mine)")]
L3 = lesson(
    "Lesson 21 Presentation 2 grammar: degree complements with 得",
    "疼得厉害 · 说中文说得非常好 · 好得很 · 高兴得跳了起来",
    requires=[],
    cards=[
        card("Degree Complements with 得 (Verb + 得 vs Adjective + 得)",
             "In Chinese there are two main reasons for using degree complements: to express how a verb happened or assess its quality, and to express to what extent (or degree) an adjective is true. Degree complements are usually composed of an adverb (sometimes omitted) and an adjective together. They appear after the main verb or adjective in a sentence with a 得 marker between them.",
             tables=[DV], examples=[D(z, e) for z, e in DE1 + DE2]),
        card("Adjectives with Degree Complements",
             "Degree complements with adjectives follow the basic patterns of degree complements with verbs (Adjective + 得 + degree complement). However, the complements can be adjectives, adverbs or other extents. They are often translated with the pattern “so … that” in English.",
             examples=[D(z, e) for z, e in DE3]),
        card("Activity 1 (Listening and Speaking)",
             "A. Listen to the conversation and mark the following statements True or False: 1. 王力玩得很好，爬长城不是很累。 2. 林强爬长城爬得最慢。 3. 李明最近不太忙，周末就在宿舍睡睡觉。 4. 周末的时候，天气非常好。 5. 去长城那天，别的人不高兴，因为李明没有去。 B. Pair up, share your answers and explain; then read the script. (Audio, not included; the book prints no key.)"),
        card("Activity 2 (Writing and Speaking)",
             "Find out what your classmates are good at (or not good at) using degree complements. A. Each student writes in Chinese characters three things they are good at and three they are not good at on six index cards, without labeling which is which. B. In groups of three, take turns showing one index card at a time; your partners ask you questions about it using degree complements and take notes (姓名 | things my partner is good at | things my partner is not good at). C. Pair up with a member of the other group and share what you learned. Some sample questions and answers (mine):",
             examples=[D(z, e) for z, e in DQ]),
    ],
    exercises=[
        M("Where does 得 stand in a degree complement?", "Between the verb/adjective and the complement", ["Before the verb", "At the end of the sentence", "After the object only"], "V + 得 + complement."),
        M("How do you say “He gets up very early every day”?", "他每天起得很早。", ["他每天很早起得。", "他得每天起很早。", "他每天得起很早。"], "起得很早."),
        M("What do you do when the verb has an object?", "Repeat the verb: V + O + V + 得 + complement", ["Drop the object", "Put 得 before the object", "Use 把"], "说中文说得非常好."),
        M("How do you say “I didn’t sleep well last night”?", "昨天晚上我睡得不好。", ["昨天晚上我不睡得好。", "昨天晚上我睡不得好。", "昨天晚上我没睡好得。"], "睡得不好."),
        M("How do you ask “Did you sleep well?” with 得?", "你睡得好不好？", ["你好不好睡得？", "你睡好得不好？", "你得睡好不好？"], "V + 得 + adj. + 不 + adj."),
        M("What does 张华最近忙得要命 mean?", "Zhang Hua has been extremely busy lately", ["Zhang Hua is not busy", "Zhang Hua got a new job", "Zhang Hua is ill"], "忙得要命: extremely busy."),
        M("What does 她累得说不出话 mean?", "She was so tired she couldn’t speak", ["She was not tired", "She spoke loudly", "She told a story"], "累得说不出话."),
        M("What does 前两天流得厉害 describe?", "A very bad runny nose", ["A bad headache", "A fever", "A cough"], "流得厉害."),
        F("我发烧、咳嗽，头也疼___厉害。", "得", PART, "疼得厉害: hurts badly."),
        F("王老师讲___真好。", "得", PART, "讲得真好."),
        F("他说中文说得非常___。", "好", PART, "说得非常好."),
    ],
)

# ------------------------------------------------------------------ 4. adjective predicate
AP = table(["格式", "例"], [["Subject + Degree Adverb + Adjective", "这个房间很大"], ["Subject + Adjective (may imply comparison)", "这个房间大，那个房间小"]], title="Adjectives as predicate (the book’s patterns)", say=[1])
AE = [("嗓子疼，口也干，头也有点儿晕。", "The book’s first example: I have a sore throat. My mouth is dry too. And I’m a bit dizzy too."), ("这个房间很大。", "1. This room is very big. (很 + adj. = very)"), ("他送我们的花儿真好看。", "2. The flowers he gave us are really pretty. (真 + adj. = really)"), ("你们来看我，我非常高兴。", "3. You came to see me; I’m extremely happy. (非常 + adj.)"),
      ("白先生在银行上班很忙，他太太在医院工作更忙。", "4. Mr. Bai works at a bank and is very busy; his wife works at a hospital and is even busier. (更 + adj.)"), ("我鼻子有点堵。", "5. My nose is a bit blocked. (有点/有点儿 + adj. = a bit)"), ("这个房间大，那个房间小。", "6. This room is big, that room is small. (no adverb: a comparison)")]
NEG = table(["Negative formation", "English meaning", "Example", "English meaning of the example"],
            [["不 + 很 + adj.", "Not very + adj.", "不很大", "(the book glosses it “Not very happy”, which fits 不很高兴)"], ["很 + 不 + adj.", "Very + un-adj.", "很不高兴", "Very unhappy"], ["不 + 太 + adj.", "Not too + adj.", "不太年轻", "Not too young"], ["太 + 不 + adj. + 了", "Too + un-adj.", "太不好看了", "Too unsightly"],
             ["不 + 真 + adj.", "* (not used)", "", ""], ["真 + 不 + adj.", "Truly + un-adj.", "真不干净", "Truly dirty"], ["不 + 非常 + adj.", "* (not used)", "", ""], ["非常 + 不 + adj.", "Extremely + un-adj.", "非常不好", "Extremely bad"], ["不 + 更 + adj.", "* (not used)", "", ""], ["更 + 不 + adj.", "Even more + un-adj.", "更不漂亮", "Even less pretty"]],
            title="Negative formation of adjectival predicates (the book’s table; * means not used)")
NEX = [("很不高兴", "Very unhappy"), ("不太年轻", "Not too young"), ("太不好看了", "Too unsightly"), ("真不干净", "Truly dirty"), ("非常不好", "Extremely bad"), ("更不漂亮", "Even less pretty")]
AQ = [("他的个子高不高？", "他的个子很高。", "1. Is he tall? — He is very tall. (B mine)"), ("你家离学校远不远？", "我家离学校不太远。", "2. Is your home far from school? — It is not too far. (mine)"), ("这件衣服漂亮不漂亮？", "这件衣服很漂亮。", "3. Is this piece of clothing pretty? — It is very pretty. (mine)"),
      ("这本汉语词典好吗？", "这本汉语词典非常好。", "4. Is this Chinese dictionary good? — It is extremely good. (mine)"), ("这个游戏好玩吗？", "这个游戏不太好玩。", "5. Is this game fun? — It is not too much fun. (mine)"), ("你的行李重吗？", "我的行李很重。", "6. Is your luggage heavy? — My luggage is very heavy. (mine)"),
      ("你的头疼吗？", "我的头有点儿疼。", "7. Does your head hurt? — My head hurts a little. (mine)"), ("你的宿舍大不大？", "我的宿舍不很大。", "8. Is your dorm room big? — My dorm room is not very big. (mine)")]
AQD = []
for q, a, e in AQ:
    lab, rest = e.split(". ", 1)
    qen, aen = rest.split(" — ", 1)
    AQD += dlg([("甲", q, lab + ". " + qen), ("乙", a, aen)])
TOP = [("学中文很有意思，可是汉字不太容易。听力和说话也很重要。我每天都很忙，但是我很喜欢。", "Topic 1: 学习中文 (my five-sentence description; the book leaves the lines blank)"), ("国防语言学院的老师非常好，课很多，作业也多。学生都很努力，学习很紧张。这里的宿舍不很大，可是很干净。", "Topic 2: 国防语言学院 (mine)"), ("蒙特雷的天气很好，不太冷，也不太热。海边很漂亮，风景好看得很。这里的东西有点贵，可是生活很舒服。", "Topic 3: 蒙特雷 (mine)")]
L4 = lesson(
    "Lesson 21 Presentation 2 grammar: adjectives as predicates (2)",
    "嗓子疼，口也干 · 很 真 非常 更 有点儿 · 不很 很不 · 学习中文",
    requires=[],
    cards=[
        card("Adjectives as Predicate (2)",
             "As you learned in a previous lesson, when an adjective is used predicatively in Chinese it does not need a verb-to-be (是) to help it constitute a predicate, as in 今天天气很好. A predicate-adjective sentence describes or evaluates a person or thing. Structurally, a predicate adjective generally appears with some kind of degree adverb. The degree adverbs include 很, 太, 真, 更, 非常, etc.; among them 很 is the most common. Without an adverb, the sentence usually appears in a comparative situation.",
             tables=[AP], examples=[D(z, e) for z, e in AE]),
        card("Negative Formation of Adjectival Predicate",
             "In negative formations, the ordering of the negative marker and the degree adverb is rather idiosyncratic. Some adverbs may prefer a certain sequence, and for other adverbs a different ordering may result in a completely different meaning. See the table (the book’s * means not used).",
             tables=[NEG], examples=[D(z, e) for z, e in NEX]),
        card("Activity 3 (Reading and Speaking)",
             "A. Pair up. Student 1 asks a question and Student 2 answers it with an adjective-predicate sentence; take turns. The book prints the eight questions and leaves the answers blank; my answers:",
             examples=AQD),
        card("Activity 3B and Activity 4",
             "B. Pair up. Each student selects one of the choices to complete the statements and explains the reasons: 1. 在美国看病: 很方便 | 不很方便 | 很不方便 | 太不方便了. 2. 美国军人的医保: 真好 | 不太好 | 真不好 | 太不好了. 3. 我们学校医院的服务: 很周到 | 不很周到 | 很不周到 | 太不周到了. 4. 我老家 Covid 的情况: 非常严重 | 不很严重 | 很不好 | 太糟糕了. 5. 我妈妈的身体: 非常好 | 不非常好 | 非常不好 | 太不好了. 6. 学中文: 很容易 | 不很容易 | 很不容易 | 太不容易了. 7. 蒙特雷的天气我: 很喜欢 | 不很喜欢 | 很不喜欢 | 太不喜欢了. (Note: 不非常好 in choice 5 is, by the table above, a combination that is not used.) Activity 4 (Writing and Speaking): pair up, pick a topic (学习中文, 国防语言学院 or 蒙特雷) and write at least five or six sentences with predicate adjectives; share with the class. My three:",
             examples=[D(z, e) for z, e in TOP]),
    ],
    exercises=[
        M("Does a predicate adjective need 是?", "No", ["Yes, always", "Only in questions", "Only in the negative"], "今天天气很好."),
        M("Which is the most common degree adverb?", "很", ["太", "更", "真"], "很 is the most common."),
        M("What does a bare adjective (no adverb) usually imply?", "A comparison", ["A question", "A command", "The past"], "这个房间大，那个房间小."),
        M("What does 很不高兴 mean?", "Very unhappy", ["Not very happy", "Not happy at all", "Quite happy"], "很 + 不 + adj."),
        M("What does 不太年轻 mean?", "Not too young", ["Very young", "Very old", "Younger"], "不 + 太 + adj."),
        M("Which combination is NOT used?", "不 + 非常 + adj.", ["非常 + 不 + adj.", "很 + 不 + adj.", "不 + 太 + adj."], "不非常, 不真, 不更 are not used."),
        M("What does 更不漂亮 mean?", "Even less pretty", ["Very pretty", "Not very pretty", "Prettier"], "更 + 不 + adj."),
        M("How do you say “My nose is a bit blocked”?", "我鼻子有点堵。", ["我鼻子堵有点。", "我鼻子很点堵。", "我有点鼻子堵。"], "有点 + adj."),
        M("Which sentence is a correct answer to “这个游戏好玩吗？”", "这个游戏不太好玩。", ["这个游戏不好玩很。", "这个游戏好玩不太。", "这个游戏太不玩好。"], "不太好玩."),
        F("我鼻子有点___。", "堵", PART, "堵: blocked."),
        F("白先生很忙，他太太在医院工作___忙。", "更", PART, "更忙: even busier."),
        F("这个房间___大。", "很", PART, "很大: very big."),
    ],
)

# ------------------------------------------------------------------ 5. adverbial adjuncts
AD = table(["格式", "例"], [["Adjective (多/少、快/慢、早/晚) + Verb", "多喝水"]], title="Adjectives used as adverbial adjuncts", say=[1])
AX = [("多喝水。", "Drink more water. (the book’s first example)"), ("明天早上你能早来半个小时吗？", "1. Tomorrow morning, can you come half an hour early?"), ("学习中文，一定要多听、多说、多看、多写。", "2. To learn Chinese you must listen more, speak more, read more and write more."), ("老王工作非常努力，他每天上班，总是早来晚走。", "3. Lao Wang works very hard; every day he always comes early and leaves late."),
      ("还有十分钟就要上课了，我们快跑吧！", "4. There are ten minutes until class; let’s run fast!"), ("你血压高，应该少喝酒。", "5. Your blood pressure is high; you should drink less alcohol.")]
AV = [("你快跑！", "1. (You) run quickly! (快 is an adjunct adjective; no adverb can be placed before it)"), ("你跑得很快。", "2. You run very fast. (很快 forms a degree complement and needs an adverb)")]
AS = [("你应该早点睡觉，少喝咖啡。", "Picture 1: You should go to bed earlier and drink less coffee. (Activity 5, my suggestion; the pictures are not included)"), ("你多吃蔬菜，少吃甜的。", "Picture 2: Eat more vegetables and less sweet food. (mine)"), ("你快走，要迟到了。", "Picture 3: Walk quickly, you’re going to be late. (mine)"), ("你慢点开车。", "Picture 4: Drive more slowly. (mine)"), ("你多锻炼，少看手机。", "Picture 5: Exercise more and look at your phone less. (mine)")]
LS7 = table(["", "建议 (mine)"], [["听力", "多听中文歌和新闻，多听几遍，慢一点儿听，早点儿开始练习"], ["阅读", "每天多读一点，慢慢读，少查字典，多猜意思"], ["说话", "多说，早点儿开口说，慢点儿说，少说英文"]], title="Activity 7: suggestions for each learning modality (the book leaves the spaces blank; this is my version)", say=[1])
L5 = lesson(
    "Lesson 21 Presentation 2 grammar: 多/少, 快/慢, 早/晚 before a verb",
    "多喝水 · 早来晚走 · 快跑 · 快跑 和 跑得快 的不同",
    requires=[],
    cards=[
        card("多/少、快/慢、早/晚 + Verb",
             "In Chinese, the monosyllabic adjectives 多, 少, 快, 慢, 早, 晚 can be placed before a verb to tell how an action should be performed. In such usage the adjectives are called “adverbial adjuncts.” Adverbial adjuncts are usually placed immediately before a verb.",
             tables=[AD], examples=[D(z, e) for z, e in AX]),
        card("Notes: (ADJ + Verb) vs (Verb 得 + ADJ)",
             "An adjunct adjective tells the desired or factual manner of an action. The function of the adjectival degree complement is to describe the degree of the manner carried out by a completed action or a habitual action. 快 in 快跑 is an adjunct adjective that tells how you are expected to run, and no adverb can be placed before it. 很快 in 跑得很快 forms a degree complement and describes how you run habitually; an adverb is required before the adjective.",
             examples=[D(z, e) for z, e in AV]),
        card("Activity 5 (Writing and Speaking)",
             "Give each person pictured in the first five images (six pictures, not included) a suggestion and then describe what the last picture tells us, using 多/少、快/慢、早/晚 + verb. My suggestions:",
             examples=[D(z, e) for z, e in AS]),
        card("Activity 6 and Activity 7",
             "Activity 6 (Listening, Writing and Speaking): A. Listen to the speakers and write their suggestions in the table (three speakers). B. Pair up and exchange your information; share with the class. C. Read the script and compare. (Audio, not included.) Activity 7 (Writing, Speaking and Listening), Learning Strategy: A. Pair up; each pair works on a topic of its choice. Provide suggestions on how to improve the specific learning modality of the Chinese you are having problems with, using adjectives as adverbial adjuncts (多/少 快/慢 早/晚); write them in Chinese in the spaces for Listening, Reading and Speaking performance. B. Post your suggestions on linoit.com and share with your class. My suggestions:",
             tables=[LS7]),
    ],
    exercises=[
        M("What does 多喝水 mean?", "Drink more water", ["Drank much water", "Water is a lot", "Don’t drink water"], "多 + verb."),
        M("Where do these adjectives stand?", "Immediately before the verb", ["After the verb", "After the object", "At the end of the sentence"], "Adjective + verb."),
        M("How do you say “Come half an hour early”?", "早来半个小时", ["来早半个小时", "来半个小时早", "早半个小时来的"], "早来半个小时."),
        M("What does 早来晚走 mean?", "Come early and leave late", ["Come late and leave early", "Come and leave at the same time", "Never come"], "早来晚走."),
        M("What does 你血压高，应该少喝酒 mean?", "Your blood pressure is high; you should drink less", ["Drink more", "Don’t drink water", "Take medicine"], "少喝酒."),
        M("Which sentence uses an adjunct adjective?", "你快跑！", ["你跑得很快。", "他说得很好。", "她写得很慢。"], "快跑: adjunct."),
        M("Which sentence uses a degree complement?", "你跑得很快。", ["你快跑！", "多喝水。", "早来晚走。"], "跑得很快: complement."),
        M("Can you put an adverb before the adjunct 快 in 快跑?", "No", ["Yes, 很快跑", "Yes, 太快跑", "Only in questions"], "No adverb can be placed before it."),
        F("学习中文，一定要多听、多说、多看、多___。", "写", PART, "多写: write more."),
        F("还有十分钟就要上课了，我们快___吧！", "跑", PART, "快跑: run fast."),
        F("你血压高，应该少___酒。", "喝", PART, "少喝酒."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration (1)
SUPP = table(["生词 (mine)", "意思 (mine)"], [["感冒药", "cold medicine"], ["退烧药", "fever reducer"], ["药片", "tablet, pill"], ["药水", "liquid medicine, syrup"]], title="Activity 1A: the supplementary words (the book leaves the pinyin and English blank; my meanings)")
L6 = lesson(
    "Lesson 21 Presentation 2 skill integration: the medicine, the floors, the boxes",
    "感冒药 退烧药 药片 药水 · 划价 缴费 取药 打针 · 药盒",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "A. Pre-listening: guess the meaning of the words in the table (supplementary vocabulary 补充词汇: 感冒药, 退烧药, 药片, 药水); if necessary look them up in your dictionary; predict what you will hear and share your answers. B. Listen to the dialog and mark the statements True or False: 1. 病人知道自己发烧，因为他觉得有点冷。 2. 病人发低烧，体温三十七度五。 3. 医生认为病人应该早点来看病。 4. 病人的心脏正常，但是血压有点高。 5. 病人得的是流感，所以得打针、吃药。 6. 医生开的药不但有药片，也有药水。 7. 病人可以在医院一楼的药房取药。 C. Provide more details and complete the table (patient symptoms; reasons for not seeing a doctor earlier; examinations conducted by the doctor; ways to take the medicine). D. Share and explain in groups of three. E. Read the script. F. Work in pairs and share your preference of treatment methods (打针、吃药、挂水 etc.). (Audio, not included; the book prints no key.)",
             tables=[SUPP]),
        card("Activity 2 (Listening, Speaking and Reading)",
             "A. Listen to a conversation and answer: 1. Who are the two speakers? 2. What is on the first floor and the second floor? 3. What is your impression of the nurse described in the conversation? 4. How can the patient find the injection room? B. Listen again and select the correct process the patient completes: ① 挂号处划价 → 自助机缴费 → 药房取药 → 注射室打针; ② 划价处划价 → 自助机缴费 → 药房取药 → 注射室打针; ③ 划价处划价 → 划价处缴费 → 注射室打针 → 药房取药. C. Pair up and share the information. D. Check your answers and read the script. (Audio, not included; the book prints no key.)"),
        card("Activity 3 (Reading, Writing, Speaking and Listening)",
             "A. Below are two images of medicine packaging boxes (not included). Pair up; each student reads the information on one box and fills in the table: 1. What kind of medicine is it? 2. What symptoms does it treat? 3. How should it be taken? Focus on the words you have learned. B. When you have completed your table, ask your partner for the information from their box."),
    ],
    exercises=[
        M("What is 退烧药?", "Fever reducer", ["Cold medicine", "Cough syrup", "Vitamin"], "退烧药."),
        M("What is 药水?", "Liquid medicine", ["Tablets", "Injection", "Medicine box"], "药水."),
        M("What is 药片?", "A tablet", ["Liquid", "Prescription", "Needle"], "药片."),
        M("Which process is described in Presentation 2?", "划价 → 付费 → 取药 → 打针", ["取药 → 划价 → 打针", "打针 → 付费 → 划价", "付费 → 取药 → 划价"], "先到一楼划价，付费。然后去二楼取药，打针."),
        M("What does 感冒药 treat?", "A cold", ["A broken bone", "A toothache", "Poor eyesight"], "感冒药: cold medicine."),
        M("What does 缴费 mean?", "To pay a fee", ["To collect medicine", "To make an appointment", "To see a doctor"], "缴费: pay."),
        F("医生开的药不但有药___，也有药水。", "片", PART, "药片: tablet."),
        F("先去划价处划价，然后在自助机上缴___。", "费", PART, "缴费: pay."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration (2)
COLD = ("感冒。症状有鼻子堵、流鼻涕、发热、咳嗽、头疼等。很少出现身体酸疼等全身不舒服的症状，病情比较轻。多数人不需要看医生就可以好。普通感冒通常没有明显发热，如果发热，一般也是中低烧，通常一到三天能正常，服用退烧药就可以。",
        "The common cold. Symptoms are a blocked nose, a runny nose, fever, cough, headache and so on. Aches and pains all over the body are seldom present and the condition is fairly light. Most people recover without seeing a doctor. An ordinary cold usually has no obvious fever; if there is a fever it is generally a medium-low one, usually back to normal in one to three days, and taking fever-reducing medicine is enough. (the book writes 1-3 天; translation mine)")
FLU = ("流行性感冒（流感）。症状有发热、嗓子疼、流鼻涕、全身疼痛、没有力气等。部分的病人还会出现咳嗽、高烧，甚至有肺炎的症状。流感的发病特点是起病急、进展快，病人多有明显发热，而且常常是高烧。病人需要服药、在家休息或去看医生。",
       "Influenza (the flu). Symptoms are fever, sore throat, runny nose, aches all over, lack of strength and so on. Some patients also have a cough, high fever, and even the symptoms of pneumonia. The flu is characterized by a sudden onset and quick progress; patients mostly have an obvious fever, often a high one. Patients need to take medicine, rest at home or see a doctor. (translation mine)")
PNE = ("肺炎。主要症状是发热，病人常常突然发冷，然后就是高烧。老年人可以是低烧或者不发热，咳嗽、胸痛。咳嗽会越来越厉害，有时呼吸困难。病人还会出现头疼、全身酸疼，食量减少的症状。得了肺炎的人需要马上去医院检查治疗。",
       "Pneumonia. The main symptom is fever; patients often suddenly feel cold and then have a high fever. Elderly people may have a low fever or none, with cough and chest pain. The cough gets worse and worse and sometimes breathing is difficult. Patients also have headache, aches all over and reduced appetite. A person with pneumonia needs to go to the hospital at once for examination and treatment. (translation mine)")
TRD = table(["病名", "主要症状", "可能症状", "病情轻/重 (mine)"], [["感冒", "鼻子堵、流鼻涕、发热、咳嗽、头疼", "很少身体酸疼，没有明显发热", "轻，多数人不需要看医生"], ["流感", "发热、嗓子疼、流鼻涕、全身疼痛、没有力气", "咳嗽、高烧，甚至肺炎的症状", "比较重，需要服药、休息或看医生"], ["肺炎", "发热，突然发冷，然后高烧", "咳嗽越来越厉害、胸痛、呼吸困难、头疼、全身酸疼、食量减少", "重，需要马上去医院"]],
           title="Activity 4B: the three illnesses (the book leaves the table blank; this is my filling)", say=[0, 1, 2, 3])
VOCW = table(["生词 (mine)", "意思 (mine)"], [["症状", "symptom"], ["明显", "obvious"], ["发热", "have a fever"], ["呼吸", "to breathe"], ["治疗", "to treat, treatment"]], title="Activity 4A: the supplementary words (the book leaves them blank)")
LQ = ("今天早上起床以后，林强觉得有点儿不舒服。下了课就到校医院去看病。他先挂了一个内科的号，然后就坐在内科门诊室的外面等着。过了一会儿，一个护士出来叫他进去。医生问他哪儿不舒服。林强告诉医生，他嗓子疼得厉害，不但咳嗽，而且口干，鼻子也堵得厉害。医生给他量了体温和血压，还听了听他的心脏。医生说他发高烧，三十九度，所以林强才觉得没有力气，全身都疼。不过，因为他的血压和心跳都还正常，所以医生认为他得的是流感。后来，医生给他开了一些感冒药，还让护士给他打了退烧针。医生告诉他那些感冒药他得吃一个星期，每天三次，一次两片，最好是早中晚各吃一次。另外，医生也让他不要去上课，在家休息，多喝热水。要是嗓子还疼，可以多吃梨。",
      "This morning after getting up Lin Qiang felt a bit unwell. After class he went to the school hospital to see a doctor. He first registered for internal medicine and then sat outside the internal-medicine consulting room waiting. After a while a nurse came out and called him in. The doctor asked where he felt unwell. Lin Qiang told the doctor that his throat hurt badly, that he not only coughed but his mouth was dry and his nose was badly blocked. The doctor took his temperature and blood pressure and also listened to his heart. The doctor said he had a high fever, 39 degrees, which is why Lin Qiang had no strength and ached all over. However, because his blood pressure and heartbeat were still normal, the doctor thought he had the flu. Then the doctor prescribed some cold medicine and had the nurse give him a fever-reducing injection. The doctor told him he had to take the cold medicine for a week, three times a day, two tablets each time, best once each morning, noon and evening. In addition, the doctor also told him not to go to class, to rest at home and drink plenty of hot water. If his throat still hurt he could eat more pears. (the book writes 三十九度 in characters; translation mine)")
LQT = table(["问题", "答案 (mine)"], [["Where did the patient see a doctor?", "校医院，内科"], ["Patient’s symptoms", "嗓子疼得厉害，咳嗽，口干，鼻子堵，没有力气，全身都疼"], ["Examinations conducted by the doctor", "量体温、量血压、听心脏"], ["Diagnosis", "流感（发高烧三十九度）"], ["Treatment", "开感冒药，打退烧针"],
                            ["Ways to take the medicine", "吃一个星期，每天三次，一次两片，早中晚各一次"], ["What else the patient needs to pay attention to", "不要去上课，在家休息，多喝热水；嗓子疼可以多吃梨"]],
            title="Activity 3 (second): Lin Qiang’s doctor visit (the book leaves the answers blank; this is my filling)", say=[1])
L7 = lesson(
    "Lesson 21 Presentation 2 skill integration: cold, flu or pneumonia, and Lin Qiang’s visit",
    "感冒 流感 肺炎 · 症状 · 林强的病 · 感冒药 退烧针 · 多喝热水",
    requires=[],
    cards=[
        card("Activity 4 (Reading, Writing, Speaking and Listening)",
             "The following information is from a medical magazine. A. Pre-reading: guess the meaning of the words 症状, 明显, 发热, 呼吸, 治疗 (supplementary vocabulary). B. Work in groups of three; each student reads one short passage, summarizes it in one sentence and fills in the table. C. Exchange information with your partners. D. Compare the similarities and differences among the three. E. Share your comparison with the class. The three passages:",
             tables=[VOCW, TRD], examples=[D(*COLD), D(*FLU), D(*PNE)]),
        card("Activity 3 (Reading and Speaking)",
             "A. Read the passage and complete the answers in the table. B. Pair up and exchange information. C. Use the information from this passage to create a dialog between a patient and doctor and act it out in your own words. D. Work in small groups and make a list of possible treatments or home remedies you use for treating the flu (治疗流感秘方) and post it on linoit.com or on a flip chart. E. Share your list with the class. The passage and my table:",
             tables=[LQT], examples=[D(*LQ)]),
    ],
    exercises=[
        M("Which illness is usually mild and needs no doctor?", "The common cold", ["The flu", "Pneumonia", "Gastroenteritis"], "感冒: 多数人不需要看医生."),
        M("What is typical of the flu’s onset?", "Sudden onset and fast progress", ["Slow onset", "No fever", "Only a rash"], "起病急、进展快."),
        M("Which illness needs prompt hospital examination?", "Pneumonia (肺炎)", ["The common cold", "A headache", "A runny nose"], "需要马上去医院检查治疗."),
        M("How do elderly people with pneumonia often run?", "Low fever or no fever", ["Very high fever", "A rash", "Dizziness only"], "老年人可以是低烧或者不发热."),
        M("What did Lin Qiang register for?", "Internal medicine", ["Surgery", "Dentistry", "Eye care"], "他先挂了一个内科的号."),
        M("What was his temperature?", "39 degrees", ["37.5 degrees", "38 degrees", "36 degrees"], "三十九度."),
        M("What was the diagnosis and why?", "The flu, because blood pressure and heartbeat were normal and there was a high fever", ["Pneumonia", "A cold", "An allergy"], "医生认为他得的是流感."),
        M("How should he take the cold medicine?", "For a week, three times a day, two tablets each time", ["One tablet daily", "Only at night", "Twice a week"], "吃一个星期，每天三次，一次两片."),
        M("What did the doctor advise besides medicine?", "Don’t go to class, rest at home, drink plenty of hot water, eat more pears", ["Go running", "Eat spicy food", "Go to class as usual"], "不要去上课…多吃梨."),
        F("普通感冒通常没有明___发热。", "显", PART, "明显: obvious."),
        F("病人常常突然发___，然后就是高烧。", "冷", PART, "发冷: feel chilly."),
        F("要是嗓子还疼，可以多吃___。", "梨", PART, "梨: pear."),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
CI = table(["Details", "在中国看病 (mine: what to note while watching)"], [["Who is the patient?", "一个美国学生"], ["When did he go?", "(from the video, not included)"], ["What’s wrong with him?", "(from the video)"], ["Where’s the hospital?", "成都"], ["Three details of registration", "(from the video)"], ["Doctor’s advice, treatment, getting the medicine", "(from the video)"]],
           title="Activity 1A: the note-taking table (the video is not included; only the scenario facts are filled)")
L8 = lesson(
    "Lesson 21 Presentation 2 using Chinese in context: a doctor’s visit in Chengdu and a role play",
    "在成都看病 · 要告诉医生的信息 · 要问医生的问题 · 病人和医生的角色卡",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Writing)",
             "Scenario: Doctor’s Visit in China. While you are studying at Sichuan University in Chengdu, China, you don’t feel well one day and need to see a doctor at a local hospital. Since it is your first visit and your Chinese is limited, you ask a classmate to help you find information about seeing the doctor, and you prepare a list of questions and other information you will need. A. Pair up; one partner plays the sick friend and the other the helper. Using the link given, both watch a YouTube video posted by an American student who just went to see a doctor in Chengdu and take notes in the table. B. Exchange your information. C. Discuss the differences between seeing a doctor in the U.S. and in China, as noted by the student in the video (中国 | 美国). D. Together create a list of questions and important information in Chinese that you think you will need (要告诉医生的信息 | 要问医生的问题). E. Share your information with the class. (The video is not included.)",
             tables=[CI]),
        card("Activity 2 (Speaking, Writing and Listening): role-play cards",
             "In this activity you create a role-play scenario between a patient and a doctor during a doctor’s visit. A. Each pair receives a set of role-play cards: Student 1 plays the patient and Student 2 the doctor. B. Study your card and decide what you need to say; you may jot down information or questions in Chinese pinyin or characters on your card. C. When you are ready, begin the role play. Patient card: you are sick and are seeing a doctor in a Chinese hospital; convey the following information appropriately: explain your symptoms; tell the time that you first got sick; explain your medical history; ask questions about checkups; ask about the doctor’s diagnosis; ask questions about treatments; ask about how to take medication(s); ask about anything else you need to pay attention to; ask where to get your medication or treatments; additional questions you may have. Doctor card: you are talking to your new patient and trying to figure out what their illness is; convey the following information, providing treatment and advice: ask about the patient’s conditions and symptoms; ask when the patient got sick; ask for the patient’s medical history; explain what checkups you will conduct; explain your diagnosis; explain treatment plans; tell the patient how to take his or her medicine(s); offer other advice for recovery; answer any additional questions the patient may ask."),
    ],
    exercises=[
        M("Where is the scenario set?", "Sichuan University in Chengdu", ["Beijing University", "Fudan University in Shanghai", "Taipei"], "Sichuan University in Chengdu."),
        M("Who plays the sick friend in Activity 1A?", "One partner; the other plays the helper", ["The teacher", "A doctor", "Nobody"], "one partner plays the sick friend."),
        M("What does the patient card say to ask about?", "Checkups, diagnosis, treatments and how to take medication", ["The weather", "The price of a taxi", "The next holiday"], "ask questions about checkups…"),
        M("What does the doctor card say to do?", "Ask about symptoms, explain the diagnosis and treatment, and give advice", ["Only take the temperature", "Only collect payment", "Refuse the patient"], "Convey the following information."),
        M("What are the two lists in Activity 1D?", "Information to tell the doctor and questions to ask the doctor", ["Food and drink", "Names and addresses", "Dates and times"], "要告诉医生的信息 | 要问医生的问题."),
        F("你哪儿不___服？", "舒", PART, "不舒服: unwell."),
        F("医生告诉病人怎么___药。", "吃", PART, "吃药: take medicine."),
    ],
)

# ------------------------------------------------------------------ 9. vocabulary
L9 = vocab_lesson("Lesson 21 Presentation 2 vocabulary", "24 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English (晕 is glossed “gosh” and 检查 “examinee” in the book; I give “dizzy” and “examine”).", VOC2)

UNIT = unit("第二十一课 Presentation 2: 看病, 得 补语, 形容词谓语, 多/少 快/慢 早/晚", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
