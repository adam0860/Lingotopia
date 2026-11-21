"""Unit 62: Lesson 21 (Seeing a Doctor) Presentation 3 and Area Studies from the book's texts: the emergency-room passage, the five activities,
the compound directional complement 起来, the 把 construction with a locative complement, the negative imperative 不要 (and the negative modals),
the skill-integration activities (sick-leave notes, a back injury, a joke), the using-Chinese activities (120, an ER story, ERs in two countries),
the vocabulary list and the Area Studies reading on China's healthcare sector. Audio, pictures, videos and links are not included; numbers the
book writes as digits are spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l21_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('验血', 1, 'xie3'), ('验了血', 2, 'xie3'), ('得住院', 0, 'dei3'), ('得去', 0, 'dei3'), ('得了急', 0, 'de2'), ('得了什', 0, 'de2'), ('种在', 0, 'zhong4'), ('里种了', 1, 'zhong4'), ('干净', 0, 'gan1'), ('看好', 0, 'kan1'), ('当真', 0, 'dang4'), ('量量', 0, 'liang2'), ('量量', 1, 'liang2'), ('量了量', 0, 'liang2'), ('量了量', 2, 'liang2'), ('量血压', 0, 'liang2'), ('量体温', 0, 'liang2'), ('定得多', 1, 'dei3'), ('不得不', 1, 'de2'), ('来得早', 1, 'de5'), ('天假', 1, 'jia4'), ('还给我', 0, 'hai2')):
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

# ------------------------------------------------------------------ 1. presentation 3
ER1 = ("星期二晚上大约九点左右，我觉得肚子疼，还有点恶心。过了半个小时以后，又开始呕吐，拉肚子。差不多半夜十二点我又发起烧来，而且腹痛、腹泻也越来越厉害。我的室友张林和王明赶紧叫了一辆出租车，把我送到了医院的急诊室。",
       "On Tuesday evening at about nine o’clock I felt a pain in my stomach and a bit of nausea. Half an hour later I began vomiting and had diarrhea. At about midnight I started running a fever again, and the stomach pain and diarrhea grew worse and worse. My roommates Zhang Lin and Wang Ming hurriedly called a taxi and took me to the hospital emergency room. (translation mine)")
ER2 = ("那天晚上看急诊的病人还真不少，我们等了半个小时，医生才给我检查。他先让我验血、验尿，还给我做了一个透视，最后确诊为急性肠胃炎。医生说我的病情很严重，得住院治疗。当天夜里我就在病房里接受治疗，护士给我输了液，还给我吃了药。",
       "There really were quite a few patients in the emergency room that night; we waited half an hour before the doctor examined me. He first had me do a blood test and a urine test and also gave me an X-ray, and finally confirmed acute gastroenteritis. The doctor said my condition was serious and I had to be hospitalized for treatment. That very night I received treatment in the ward; the nurse gave me an infusion and also gave me medicine. (translation mine)")
ER3 = ("医生让我住三天院，所以星期三早上张林帮我跟老师请了病假。老师让我不要着急，安心地在医院治疗。",
       "The doctor had me stay in hospital for three days, so on Wednesday morning Zhang Lin asked the teacher for sick leave for me. The teacher told me not to worry and to keep my mind at ease while being treated in the hospital. (translation mine)")
ER4 = ("三天后，我出了院，又在宿舍休息了两天，现在感觉好多了。医生说这次我生病是因为吃了不干净的东西，让我以后一定多加小心。这次多亏了室友们及时地把我送到了医院，我从心里感谢他们。下个星期我就可以回去上课了。",
       "Three days later I left the hospital and rested another two days in the dorm, and now I feel much better. The doctor said I fell ill this time because I ate something unclean, and told me to be especially careful from now on. This time, thanks to my roommates’ timely taking me to the hospital, I thank them from my heart. Next week I can go back to class. (translation mine)")
L1 = lesson(
    "Lesson 21 Presentation 3: a night in the emergency room",
    "肚子疼 恶心 呕吐 · 叫出租车 · 急诊室 · 验血 验尿 透视 · 急性肠胃炎 · 住院 输液",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Have you ever been to an emergency room (ER)? Why did you need to go? B. Do you have any friends or relatives who have been to the ER? What happened to them? C. What treatment or examinations did you receive on your last doctor’s visit? (Four small pictures, not included.)"),
        card("Presentation 3: 急诊室", "The passage is in four paragraphs; the book also prints it in traditional characters. The translations are mine.",
             examples=[D(*ER1), D(*ER2), D(*ER3), D(*ER4)]),
    ],
    exercises=[
        M("When did the speaker first feel unwell?", "About nine on Tuesday evening", ["Monday morning", "Midnight", "Wednesday noon"], "星期二晚上大约九点左右."),
        M("What were his first symptoms?", "Stomach pain and a little nausea", ["A cough", "A rash", "A sore throat"], "肚子疼，还有点恶心."),
        M("What happened half an hour later?", "He started vomiting and had diarrhea", ["He went to sleep", "He called his teacher", "He took a shower"], "又开始呕吐，拉肚子."),
        M("What did his roommates do?", "Called a taxi and took him to the ER", ["Waited until morning", "Called his parents", "Gave him medicine at home"], "叫了一辆出租车，把我送到了医院的急诊室."),
        M("How long did they wait before the doctor examined him?", "Half an hour", ["Two hours", "Ten minutes", "All night"], "我们等了半个小时."),
        M("Which tests did the doctor order?", "Blood test, urine test and X-ray", ["Eye test and hearing test", "Heart test only", "No tests"], "验血、验尿，还做了一个透视."),
        M("What was the final diagnosis?", "Acute gastroenteritis", ["The flu", "Pneumonia", "Appendicitis"], "确诊为急性肠胃炎."),
        M("What treatment did he receive that night?", "An infusion and medicine in the ward", ["Surgery", "Only rest", "A cast"], "护士给我输了液，还给我吃了药."),
        M("How many days did he stay in hospital?", "Three", ["One", "Five", "Seven"], "医生让我住三天院."),
        M("What did the teacher tell him?", "Not to worry and to be treated at ease", ["To come to class", "To hand in homework", "To go home at once"], "老师让我不要着急，安心地在医院治疗."),
        M("What caused the illness, according to the doctor?", "He ate something unclean", ["He caught a cold", "He drank too little", "He slept too little"], "是因为吃了不干净的东西."),
        M("How does he feel about his roommates at the end?", "Grateful from the heart", ["Angry", "Embarrassed", "Indifferent"], "我从心里感谢他们."),
        F("过了半个小时以后，又开始呕___，拉肚子。", "吐", PART, "呕吐: vomit."),
        F("医生说我的病情很严重，得住___治疗。", "院", PART, "住院: be hospitalized."),
        F("这次多___了室友们及时地把我送到了医院。", "亏", PART, "多亏了: thanks to."),
    ],
)

# ------------------------------------------------------------------ 2. activities
ACT3 = [("星期二晚上大约九点左右，我觉得肚子疼，还有点恶心。", "1. 大约 + 左右. On Tuesday evening at about nine o’clock I felt a pain in my stomach and a bit of nausea. (key mine)"), ("过了半个小时以后，又开始呕吐，拉肚子。", "2. 又. Half an hour later I began vomiting again and had diarrhea."), ("差不多半夜十二点我又发起烧来，而且腹痛、腹泻也越来越厉害。", "3. 差不多, 又, 而且, 越来越."),
        ("我的室友张林和王明赶紧叫了一辆出租车，把我送到了医院的急诊室。", "4. 把."), ("那天晚上看急诊的病人还真不少，我们等了半个小时，医生才给我检查。", "5. 才."), ("他先让我验血、验尿，还给我做了一个透视，最后确诊为急性肠胃炎。", "6. 最后."), ("医生让我住三天院，所以星期三早上张林帮我跟老师请了病假。", "7. 让, 跟."), ("医生说这次我生病是因为吃了不干净的东西，让我以后一定多加小心。", "8. 因为, 让.")]
CPT = table(["头 (mine)", "词 (mine)"], [["腹", "腹痛，腹泻"], ["验", "验血，验尿"], ["头", "头疼，头晕"], ["病", "病人，病情，病房，病假，生病"], ["看", "看病，看急诊"], ["量", "量体温，量血压"], ["输", "输液"], ["流", "流鼻涕，流感"], ["发", "发烧，发炎"], ["打", "打针"],
                          ["院", "医院，住院，出院"], ["疼", "头疼，肚子疼"], ["科", "内科，外科"], ["心", "心脏，心跳"], ["药", "药房，药方，取药"], ["室", "急诊室，候诊室，病室"], ["炎", "肺炎，肠胃炎"], ["假", "病假，请假"], ["卡", "就诊卡，医保卡，病历卡"]],
            title="Activity 2: completing the terms (the book gives two groups of 19 characters and blank boxes; these are my words)", say=[1])
L2 = lesson(
    "Lesson 21 Presentation 3 activities: EEIs, word building, fill in the blanks, an ER story",
    "Activities 1 to 5 · 腹 验 头 病 看 · 大约…左右 · 把 才 让 · 急诊室的故事",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 3 once and answer: 1. What is the presentation about? 2. Summarize the required EEIs in the table: When (星期二晚上大约九点; …), Who (the speaker, with roommates 张林 and 王明), What (acute gastroenteritis), How (by taxi), Where (the hospital ER), Why (he ate something unclean). B. Detailed listening: 1. List three tests the doctor gave the speaker (blood test, urine test, X-ray). 2. What was the final diagnosis (acute gastroenteritis)? 3. What treatment did the speaker receive (hospitalization with an infusion and medicine)? 4. What did the speaker’s teacher tell him (don’t worry, be treated at ease)? 5. What is the speaker’s feeling at the end, and why (grateful to his roommates)? (Audio, not included; the answers in brackets are from the text.)"),
        card("Activity 2 (Reading, Writing and Speaking)",
             "A. Work in small groups to complete the following terms by adding characters; for example 感 (感冒/感觉) or 约 (大约/预约). Group 1: 腹, 验, 头, 病, 看, 量, 输, 流, 发, 打 (each twice). Group 2: 院, 疼, 科, 心, 病, 药, 室, 炎, 假, 卡 (each twice). B. Share your answers with the class. Mine:",
             tables=[CPT]),
        card("Activity 3 (Writing and Speaking)",
             "A. Fill in the blanks and complete the sentences using the words 左右, 又, 差不多, 而且, 越来越, 把, 最后, 才, 让, 大约, 因为, 跟; some of the words can be used more than once. B. Share your answers with a classmate and explain the English meaning of each sentence. The book prints the eight sentences with blanks and no key; the completed sentences and my key:",
             examples=[D(z, e) for z, e in ACT3]),
        card("Activity 4 (Listening, Writing and Speaking)",
             "A. Listen to the passage once and write what it is about. B. Listen again and mark the statements True or False: 1. 病人不但发烧、咳嗽，还头疼。 2. 病人开始以为是普通的感冒。 3. 病人病情越来越重，所以去医院看病。 4. 医生听了病人的心脏，给病人量了体温和血压。 5. 透视以后，医生确诊病人得了肺炎。 6. 病人不但需要吃药，而且还要打针。 7. 病人拿着医生开的药方到药店取了药。 8. 回家后，病人跟学校请了三天假休息。 9. 病人觉得以后再生病，一定得注意休息，这样可以好得快。 C. Share your answers and read the script. (Audio, not included; the book prints no key.)"),
        card("Activity 5 (Speaking, Writing and Listening): An ER Story",
             "A. Individually think of five questions you would like to ask your classmates about their ER experiences (or someone they know who had such experiences). B. Interview a classmate with your questions and write the answers in the table (同学; 急诊室的经历: 时间, 地点, 疾病, 症状, 怎么去急诊室, 检查, 诊断, 治疗, 医生建议, 其他信息). C. Report the story to the class using the information you collected."),
    ],
    exercises=[
        M("Which word fills “星期二晚上___九点左右”?", "大约", ["才", "把", "因为"], "大约…左右."),
        M("Which word fills “医生___给我检查”, after the half-hour wait?", "才", ["又", "把", "越来越"], "我们等了半个小时，医生才给我检查."),
        M("Which word fills “张林和王明赶紧叫了一辆出租车，___我送到了医院”?", "把", ["让", "跟", "才"], "把我送到了医院."),
        M("Which word fills “医生___我住三天院”?", "让", ["把", "又", "才"], "医生让我住三天院."),
        M("Which word fills “张林帮我___老师请了病假”?", "跟", ["把", "大约", "最后"], "跟老师请了病假."),
        M("Which word fills “___确诊为急性肠胃炎”, after the tests?", "最后", ["因为", "才", "左右"], "最后确诊."),
        M("Which word fills “腹痛、腹泻也___厉害”?", "越来越", ["差不多", "而且", "大约"], "越来越厉害."),
        M("Which compound contains 验?", "验血", ["住院", "取药", "打针"], "验血."),
        M("Which compound contains 炎?", "肺炎", ["内科", "病假", "输液"], "肺炎."),
        F("他先让我___血、验尿，还给我做了一个透视。", "验", PART, "验血: blood test."),
        F("最后确___为急性肠胃炎。", "诊", PART, "确诊: confirm diagnosis."),
    ],
)

# ------------------------------------------------------------------ 3. 起来
QT = table(["", "Action/state has begun", "Action/state has begun and is ongoing"], [["Without object", "V + 起来", "V + 起来 + 了"], ["", "Adj. + 起来", "Adj. + 起来 + 了"], ["With object", "V + 起 + O + 来", "V + 起 + O + 来 + 了"]], title="The compound directional complement 起来")
QE = [("差不多半夜十二点我又发起烧来。", "The book’s first example: Then I started having a fever around midnight."), ("小鸟飞起来了。", "1. The bird flew up."), ("大家都笑起来了。", "2. Everyone started laughing."), ("天气热起来了。", "3. The weather is getting hot."), ("因为很长时间没锻炼，他胖起来了。", "4. Because he hasn’t exercised for a long time, he is getting fat."),
      ("刚才还好好的，怎么现在下起雨来了？", "5. It was fine just now; how come it has started to rain?"), ("烧烤以后，同学们在草地上跳起舞来。", "6. After the barbecue the students started dancing on the grass."), ("半个小时以前，我拉起肚子来。", "7. Half an hour ago I started having diarrhea.")]
QM = [("我的鼻子堵起来了。", "My nose has started to get blocked. (Activity 1A, mine: 鼻子堵)"), ("听到这个消息，大家都兴奋起来了。", "Hearing this news everybody got excited. (兴奋, mine)"), ("看到老师，他有点紧张起来了。", "Seeing the teacher, he began to get a bit nervous. (紧张, mine)"), ("刚说了几句，他们就聊起天来了。", "After just a few sentences they started chatting. (聊天, mine)"),
      ("天气冷起来了，快下雪了。", "It’s getting cold and it’s about to snow. (冷, mine)"), ("一到周末，他就唱起歌来。", "As soon as the weekend comes he starts singing. (唱歌, mine)")]
QS = ("上个星期六我们去参加了一个烧烤晚会。一到公园，大家就聊起天来了。过了一会儿，天气热起来了，我们都喝起水来。晚饭以后，有人唱起歌来，有人跳起舞来，大家都高兴起来了。",
      "Last Saturday we went to a barbecue party. As soon as we reached the park everybody started chatting. After a while the weather got hot and we all started drinking water. After dinner some people started singing and some started dancing, and everyone cheered up. (Activity 3, my sample story)")
L3 = lesson(
    "Lesson 21 Presentation 3 grammar: the compound directional complement 起来",
    "发起烧来 · 热起来了 · 唱起歌来 · 开始 和 继续",
    requires=[],
    cards=[
        card("Compound Directional Complement 起来",
             "In Chinese, 起来 can be used both as a directional complement and as a resultative complement. As a directional complement it is similar to “up” in English, used literally as in “stand up”; as a resultative complement it often means “to start doing something” (traceable back to its directional meaning, “an upward action”). When 起来 shows that an action or state has begun and is ongoing, it is often used after a verb or an adjective, with 了 at the end of the sentence. The verbs are usually spontaneous actions like 唱, 跳, 聊, or states like 热, 冷, 好; 起来 cannot be used with planned actions. When 起来 is used with a verb that has an object, the V + 起 + O + 来 structure is often used, meaning “to start doing something”; such verb-object phrases include 唱歌, 跳舞, 吃饭, 发烧, 看书 etc.",
             tables=[QT], examples=[D(z, e) for z, e in QE]),
        card("Activity 1 (Speaking and Listening)",
             "A. Pair up. Study the two word lists and take turns selecting one word from each list to create sentences with “Verb/Adjective + 起来 + 了” or “Verb + 起 + Object + 来”. List 1: 流鼻涕, 量血压, 发烧, 嗓子疼, 鼻子堵, 头晕, 量体温, 喝水, 吃药, 高兴, 兴奋, 紧张. List 2: 输液, 刮风, 下雪, 打, 跳, 站, 唱歌, 工作, 聊天, 哭, 热, 冷. B. Share your sentences with the class. My sentences:",
             examples=[D(z, e) for z, e in QM]),
        card("Activity 2 and Activity 3",
             "Activity 2 (Listening and Speaking): A. Listen to six sentences and translate what you hear. B. Share your answers and read the scripts. (Audio, not included.) Activity 3 (Writing, Speaking and Listening): in this activity you describe your activities at an event you attended recently, using “起来 + 了” or “V + 起 + O + 来”. A. Write your story with at least four to six sentences. B. Pair up and exchange. C. Retell your partner’s story to the class. My sample:",
             examples=[D(*QS)]),
    ],
    exercises=[
        M("What does 起来 as a resultative complement often mean?", "To start doing something", ["To stand up only", "To finish something", "To stop something"], "起来: start."),
        M("What does 发起烧来 mean?", "To start having a fever", ["To recover from a fever", "To end a fever", "To measure a fever"], "发起烧来."),
        M("Which structure is used with an object?", "V + 起 + O + 来", ["V + O + 起来", "起来 + V + O", "V + 来 + 起 + O"], "V + 起 + O + 来."),
        M("Which verbs or states can take 起来?", "Spontaneous ones like 唱, 跳, 聊, 热, 冷", ["Planned actions", "Only past events", "Only nouns"], "Not with planned actions."),
        M("What does 天气热起来了 mean?", "The weather is getting hot", ["The weather was hot", "It is not hot", "Hot water is ready"], "热起来了."),
        M("What does 大家都笑起来了 mean?", "Everyone started laughing", ["Everyone stopped laughing", "Nobody laughed", "Everyone cried"], "笑起来."),
        M("How do you say “It has started to rain”?", "下起雨来了", ["下雨起来了", "起下雨来了", "下来起雨了"], "V + 起 + O + 来."),
        M("What does 小鸟飞起来了 mean (literal use)?", "The bird flew up", ["The bird fell", "The bird stopped", "The bird left the cage"], "飞起来: up."),
        F("差不多半夜十二点我又发___烧来。", "起", PART, "发起烧来."),
        F("烧烤以后，同学们在草地上跳起舞___。", "来", PART, "跳起舞来."),
        F("因为很长时间没锻炼，他胖___来了。", "起", PART, "胖起来了."),
    ],
)

# ------------------------------------------------------------------ 4. 把 locative
BL = table(["格式", "意思"], [["把 + Object + Verb + 在 or 到 + Place", "Indicating placement or relocation"]], title="The 把 construction with a locative complement")
BE = [("我的室友张林和王明赶紧叫了一辆出租车，把我送到了医院的急诊室。", "The book’s first example: My roommates Zhang Lin and Wang Ming called a cab in a hurry and sent me to the hospital emergency room."), ("我把那些树种在院子里了。", "1. I planted those trees in the yard."), ("你把自行车放在哪儿了？", "2. Where did you put the bicycle?"), ("她把老师说的话都写在笔记本上了。", "3. She wrote down everything the teacher said in her notebook."),
      ("我们快把这个病人送到医院去吧。", "4. Let’s quickly take this patient to the hospital."), ("我已经把椅子搬到楼上去了。", "5. I have already moved the chair upstairs."), ("飞机是八点半起飞的。我七点十分开车把他们送到了机场。", "6. The plane took off at half past eight. At ten past seven I drove them to the airport.")]
BC = [("我把那些树种在院子里了。", "This tells what the speaker did with the trees, namely planting them in the backyard: I have planted those trees in the yard."), ("我在院子里种了一些树。", "This describes what the speaker did in the yard: I have planted some trees in the yard.")]
BA4 = [("你把你手机放在哪儿了？", "我把手机放在书包里了。", "1. Where did you put your phone? — I put it in my bag. (B mine)"), ("老师把我的作业放到哪儿了？", "老师把你的作业放到桌子上了。", "2. Where did the teacher put my homework? — The teacher put your homework on the desk. (mine)"), ("你把你的军服送到哪儿去洗了？", "我把军服送到洗衣店去洗了。", "3. Where did you send your uniform to be washed? — I sent it to the laundry. (mine)"),
       ("值班的军人把喝了太多酒的人送到哪儿了？", "他把那个人送到医院去了。", "4. Where did the soldier on duty take the person who had drunk too much? — He took him to the hospital. (mine)"), ("今年你家人朋友给你生日礼物了吗？他们要把礼物寄到这里了吗？", "给了，他们把礼物寄到学校来了。", "5. Did your family and friends give you birthday gifts this year? Did they send the gifts here? — Yes, they sent the gifts to the school. (mine)")]
BAD = []
for q, a, e in BA4:
    lab, rest = e.split(". ", 1)
    qen, aen = rest.split(" — ", 1)
    BAD += dlg([("甲", q, lab + ". " + qen), ("乙", a, aen)])
B6 = [("请你把那本书放到桌子上。", "Please put that book on the table. (Activity 6, mine)"), ("请你把我的水瓶拿到门口去。", "Please take my water bottle to the door. (mine)"), ("请你把窗户上的纸放在老师的桌子上。", "Please put the paper from the window on the teacher’s desk. (mine)")]
L4 = lesson(
    "Lesson 21 Presentation 3 grammar: the 把 construction with a locative complement",
    "把我送到了急诊室 · 把…放在 · 把…搬到 · 把和没有把",
    requires=[],
    cards=[
        card("把-Construction with Locative Complement",
             "In a previous lesson you learned the Chinese 把 construction. The two major conditions for using it are (1) the definiteness of the object noun phrase and (2) the complexity of the verb phrase. The 把 construction is compulsory when the verb is followed by a locative complement, indicating placement or relocation of a thing or a person as a result of the action. A locative complement is made up of 在 or 到, followed by a place word. When a disposal verb takes both an object and a locative complement, the object must be placed after 把 and before the verb, leaving the verb and the complement to form one closed verbal unit. The locative complement tells where the object is moved via the disposal verb.",
             tables=[BL], examples=[D(z, e) for z, e in BE]),
        card("把-Construction with a Locative Complement vs. a Sentence Without the 把 Construction",
             "The first sentence below tells what the speaker did with the trees; the second describes what the speaker did in the yard.",
             examples=[D(z, e) for z, e in BC]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "A. Pair up and complete the following sentences using the 把 construction with a locative complement. B. Share your answers. The book prints the five questions (A) and leaves B blank; my answers:",
             examples=BAD),
        card("Activity 5 and Activity 6",
             "Activity 5 (Listening and Speaking): A. Listen to the dialog and answer: 1. What is the relationship between the two speakers? 2. What happened to the male speaker’s wallet? 3. What did he learn about his wallet? 4. What is the female speaker’s plan for tomorrow? 5. What kind of person do you think the male speaker is? 6. What kind of person is the female speaker? 7. What did the male speaker promise the female speaker? B. Share your answers and read the script with the class. (Audio, not included.) Activity 6 (Speaking, Listening and Writing): A. Pair up and take turns asking your partner to move an object in the classroom for you, using the 把 construction with a locative complement; your partner completes the action. B. When you are done, write three sentences in Chinese describing what your partner asked you to do. C. Share your sentences with the class. My three sample requests:",
             examples=[D(z, e) for z, e in B6]),
    ],
    exercises=[
        M("When is the 把 construction compulsory?", "When the verb is followed by a locative complement", ["When the verb is 是", "When there is no object", "In questions only"], "Locative complement → 把."),
        M("What is a locative complement made of?", "在 or 到 plus a place word", ["了 plus a noun", "过 plus a time", "得 plus an adjective"], "在/到 + place."),
        M("Where does the object go?", "After 把 and before the verb", ["After the verb", "At the end", "Before the subject"], "把 + object + verb."),
        M("“I planted those trees in the yard.”", "我把那些树种在院子里了。", ["我种把那些树在院子里了。", "我把种那些树在院子里了。", "我在院子里把种那些树了。"], "把 + object + verb + 在 + place."),
        M("“Where did you put the bicycle?”", "你把自行车放在哪儿了？", ["你放自行车把在哪儿了？", "你把放自行车在哪儿了？", "你在哪儿把自行车放了？"], "把自行车放在哪儿了."),
        M("What does 我已经把椅子搬到楼上去了 mean?", "I have already moved the chair upstairs", ["I sat on the chair upstairs", "I bought a chair", "I broke the chair"], "搬到楼上去."),
        M("How do 我把那些树种在院子里了 and 我在院子里种了一些树 differ?", "The first says what was done with the trees; the second says what was done in the yard", ["They mean the same", "The first is a question", "The second is passive"], "把 focuses on the object’s placement."),
        M("What does 我七点十分开车把他们送到了机场 mean?", "At ten past seven I drove them to the airport", ["They drove me to the airport", "I met them at the airport", "I forgot the airport"], "送到了机场."),
        F("我们快___这个病人送到医院去吧。", "把", PART, "把…送到."),
        F("我把那些树种___院子里了。", "在", PART, "种在院子里."),
        F("我已经把椅子搬到楼上___了。", "去", PART, "搬到楼上去."),
    ],
)

# ------------------------------------------------------------------ 5. 不要
BY = table(["格式", "意思"], [["不要 + Verb + (Object)", "Don’t do …"], ["不要 + Verb + (Object) + 了", "Stop doing …"]], title="Negative imperative 不要")
BYE = [("老师让我不要着急，安心地在医院治疗。", "The book’s first example: My teacher told me not to worry and keep my mind on the treatment in the hospital."), ("不要走。", "1. Don’t go."), ("不要打我。", "2. Don’t hit me."), ("你晚上不要开车。", "3. Don’t drive at night."), ("请不要离开我。", "4. Please don’t leave me."), ("请不要忘了关门。", "5. Please don’t forget to close the door."),
       ("上课的时候，不要玩手机。", "6. Don’t play with your phone during class."), ("不要说话了，现在开始上课。", "7. Stop talking; class is starting now."), ("不要再吃了，你都吃了三碗米饭了。", "8. Stop eating; you have already had three bowls of rice.")]
A7 = [("不要说话。", "1. Don’t talk. (Activity 7B, mine)"), ("不要告诉别人。", "2. Don’t tell others. (mine)"), ("不要动。", "3. Don’t move. (mine)"), ("不要说话了。", "4. Stop talking. (mine)"), ("不要再睡了。", "5. Stop sleeping. (mine)"), ("不要笑了。", "6. Stop laughing. (mine)"), ("不要胡闹了。", "7. Stop horsing around. (mine)")]
A8 = [("我不会游泳，你能教我吗？", "1. 不会. I can’t swim; can you teach me? (key mine)"), ("我明天要上班，不能跟你们一起去旧金山。", "2. 不能. I have to work tomorrow, so I can’t go to San Francisco with you."), ("这条河不干净，不可以在这儿游泳。", "3. 不可以. This river isn’t clean; you may not swim here."), ("老师说，明天不用上课，因为是军事训练日。", "4. 不用. The teacher said there’s no need to go to class tomorrow because it’s a military training day."),
      ("我不想去看电影，我想在家休息。", "5. 不想. I don’t want to go to a movie; I want to rest at home."), ("你身体不好，真不应该喝那么多酒。", "6. 不应该. Your health isn’t good; you really shouldn’t drink that much."), ("快起来，不要再睡了。我们得去集合。", "7. 不要. Get up, stop sleeping. We have to go to the assembly.")]
MOD = table(["English meaning", "Positive", "Negative"], [["will likely do", "会", "不会"], ["know how to do", "会", "不会"], ["able to do", "能/可以", "不能"], ["ought to do", "要/应该", "不用"], ["want to do", "想/要", "不想"], ["allowed to do", "可以", "不可以"], ["should do", "应该", "不应该"], ["prohibited to do", "", "不能/不可以"], ["need to", "要", "不要/别"]],
            title="Activity 8C: the table of modals and their negatives (the book’s table)")
CD9 = [("不要在公共场合发脾气。", "1. Don’t lose your temper in public."), ("不要随便接受表扬。", "2. Don’t accept praise casually. (the book glosses 表扬 as praise)"), ("不要一开始就用中国人的名字叫他们。", "3. Don’t call Chinese people by their first names right from the start. (the book prints 名叫, which I read as 名字叫)"), ("不要让中国人丢脸。", "4. Don’t make Chinese people lose face."), ("不要等着别人买单。", "5. Don’t wait for others to pay the bill."),
       ("不要空手去朋友家。", "6. Don’t go to a friend’s home empty-handed."), ("不要把中国人客气的时候说的“不，谢谢”当真。", "7. Don’t take the “No, thank you” that Chinese people say out of politeness seriously."), ("不要马上接受别人给的食物、饮料或礼物。", "8. Don’t accept food, drinks or gifts that others offer immediately."), ("不要在祝酒前喝酒。", "9. Don’t drink before the toast.")]
L5 = lesson(
    "Lesson 21 Presentation 3 grammar: the negative imperative 不要, and negative modals",
    "不要着急 · 不要说话了 · 不想 不能 不会 不用 不可以 不应该 不要 · 老外在中国不要做的九件事",
    requires=[],
    cards=[
        card("Negative Imperative 不要",
             "In Chinese, 不要 is a variant form of 别. It is used as a negative imperative to express a demand or command to refrain from doing something, like the English “Don’t do something.” 不要 and 别 may be used interchangeably; 别 can be seen as the short, informal form of 不要. Just like 别, 不要 appears before a verb, and the subject is usually omitted, as in English. You can also use 了 at the end of a sentence with 不要, which means to stop doing something.",
             tables=[BY], examples=[D(z, e) for z, e in BYE]),
        card("Activity 7 (Reading, Writing and Speaking)",
             "A. Watch the YouTube video and pay attention to the usage of 不要 and 别. B. Pair up and determine how you would say the sentences in Chinese: 1. Don’t talk. 2. Don’t tell others. 3. Don’t move. 4. Stop talking. 5. Stop sleeping. 6. Stop laughing. 7. Stop horsing around. Write your answers and share your work with the class. Mine:",
             examples=[D(z, e) for z, e in A7]),
        card("Activity 8 (Speaking and Listening)",
             "A. Complete the sentences with the correct word from the list 不想 | 不能 | 不会 | 不用 | 不可以 | 不应该 | 不要. B. Pair up; share your answers and explain your choices. C. Study and compare the words and their meanings in the table. The book prints the seven sentences with blanks and no key; each word fits once, and my key:",
             tables=[MOD], examples=[D(z, e) for z, e in A8]),
        card("Activity 9 (Speaking and Listening)",
             "The following article is from Chinadaily.com (adapted from world.chinadaily.com.cn): 老外在中国不要做的9件事 (nine things foreigners shouldn’t do in China). A. Scan the title and guess who should pay attention to it and what you expect to read about (看题目，猜大意). B. Work in groups of three; each student reads three items and shares the information with the group. C. Why do you think each tip is given? The nine items:",
             examples=[D(z, e) for z, e in CD9]),
    ],
    exercises=[
        M("What is 不要 compared with 别?", "Its fuller, less informal form", ["A different meaning", "A past form", "A question form"], "别 is the short, informal form."),
        M("What does 不要 + verb + 了 mean?", "Stop doing it", ["Don’t start doing it", "You may do it", "Do it again"], "不要…了: stop."),
        M("Which blank takes 不会: “我___游泳，你能教我吗？”", "不会", ["不能", "不想", "不用"], "不会: don’t know how."),
        M("Which blank takes 不能: “我明天要上班，___跟你们一起去旧金山”?", "不能", ["不会", "不用", "不想"], "不能: unable."),
        M("Which blank takes 不用: “老师说，明天___上课，因为是军事训练日”?", "不用", ["不想", "不应该", "不可以"], "不用: no need."),
        M("Which blank takes 不应该: “你身体不好，真___喝那么多酒”?", "不应该", ["不会", "不用", "不想"], "不应该: shouldn’t."),
        M("Which blank takes 不想: “我___去看电影，我想在家休息”?", "不想", ["不能", "不会", "不可以"], "不想: don’t want."),
        M("Which means “prohibited to do”?", "不能/不可以", ["不想", "不会", "不用"], "Prohibited."),
        M("What does 不要空手去朋友家 advise?", "Don’t go to a friend’s home empty-handed", ["Don’t visit friends", "Go with empty hands", "Bring a tool"], "空手."),
        M("What does 不要等着别人买单 advise?", "Don’t wait for others to pay the bill", ["Pay for everyone", "Don’t eat out", "Order only soup"], "买单."),
        F("老师让我___要着急，安心地在医院治疗。", "不", PART, "不要着急."),
        F("请不要忘了关___。", "门", PART, "关门: close the door."),
        F("不要再吃了，你都吃了三碗___饭了。", "米", PART, "米饭: rice."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
NOTE1 = ("杨老师：您好！我是大卫。今天早上九点十五分我得去看医生，因为这两天我睡得不好，而且头晕、头疼得特别厉害。特向您请假一个半小时（九点十五分至十点十五分），希望您能够批准。谢谢！您的学生：王大卫　二零二零年四月二十八日",
         "Teacher Yang: Hello! I am David. This morning at 9:15 I have to see a doctor, because for the past two days I haven’t slept well and I have been dizzy and had a very bad headache. I am asking you for one and a half hours’ leave (9:15 to 10:15) and hope you can approve it. Thank you! Your student: Wang David, April 28, 2020. (a sick-leave note, 病假条; the book writes the times and date in digits)")
NOTE2 = ("王老师：您好！刚刚我的太太打来电话，说我的孩子病了，发高烧三十九度，而且咳嗽得非常厉害。需要我回家带孩子去看病，所以今天下午的课我不能上了。特请半天假，希望您能够批准。谢谢！学生：马克　二零二零年五月六日",
         "Teacher Wang: Hello! My wife just phoned to say that my child is ill, with a high fever of 39 degrees and a very bad cough. I need to go home and take the child to see a doctor, so I can’t attend this afternoon’s class. I am asking for half a day’s leave and hope you can approve it. Thank you! Student: Mark, May 6, 2020. (a sick-leave note; the book writes the date in digits)")
NOTE3 = ("张老师：您好！昨天晚上十点我因为呕吐、腹痛和发烧，被送进了医院的急诊室。医生说我得了急性肠胃炎，需要住三天院，所以这几天不能到校上课。特向您请三天假（周二至周四），希望您能够批准。谢谢！（假条和医生证明请王兰带给您）您的学生：琳达　二零二零年六月八日",
         "Teacher Zhang: Hello! Last night at ten I was taken to the hospital emergency room because of vomiting, stomach pain and fever. The doctor said I have acute gastroenteritis and need to stay in hospital for three days, so I cannot come to school these days. I am asking you for three days’ leave (Tuesday to Thursday) and hope you can approve it. Thank you! (Please ask Wang Lan to bring you the note and the doctor’s certificate.) Your student: Linda, June 8, 2020. (the book writes the date in digits)")
NTB = table(["Student", "Request", "Reasons (Symptoms)"], [["大卫 (David)", "请假一个半小时", "这两天睡得不好，头晕，头疼得特别厉害；要去看医生"], ["马克 (Mark)", "请半天假", "孩子发高烧三十九度，咳嗽得很厉害；要带孩子去看病"], ["琳达 (Linda)", "请三天假", "呕吐、腹痛、发烧，被送进急诊室，得了急性肠胃炎，要住三天院"]],
            title="Activity 3B: what each note is about (the book leaves the table blank; this is my filling)")
SUPP3 = table(["生词 (mine)", "意思 (mine)"], [["病假", "sick leave"], ["病假条", "sick-leave note"], ["便条", "a short note"], ["事假（条）", "personal leave (note)"], ["批准", "to approve"]], title="Activity 3A: the supplementary words (the book leaves the pinyin and English blank)")
S1P = ("① 那天我们到急诊室的时候，因为是早上只有一两个病人，所以很快就有一个女医生过来问我的病情。她先给我量了量血压，听了一下心脏，然后又给我做了一个透视，拍了Ｘ光。等拍的片子出来后，医生告诉我幸亏没有伤到骨头，所以不需要住院治疗，但是得打针、输液治疗。医生先让护士给我打了止痛针，很快我的疼痛开始慢慢减轻。然后护士又给我输液，输了大概两个小时。② 我在家躺了三天，不能坐和走，只能躺着，到了第四天才能站起来。以后锻炼的时候，我一定得多加小心，不能再受伤了。",
       "① When we got to the emergency room that day, because it was morning and there were only one or two patients, a woman doctor soon came over to ask about my condition. She first measured my blood pressure and listened to my heart, then gave me an X-ray and took an X-ray picture (the book writes “X 光”; I wrote the letter in full-width form). When the picture came out the doctor told me that luckily the bone wasn’t injured, so no hospitalization was needed, but I had to have an injection and an infusion. The doctor first had the nurse give me a painkiller injection, and soon my pain slowly eased. Then the nurse gave me an infusion for about two hours. ② I lay at home for three days, unable to sit or walk, only lie; only on the fourth day could I stand up. When I exercise in the future I must be extra careful and not get hurt again. (Student 1’s two slips; translation mine)")
S2P = ("③ 上个星期一在体育馆锻炼的时候，我不小心伤到了后背，休息了几天。后来有一点好转，所以我就试着举起双手，突然后背又疼起来，而且疼痛越来越严重，最后不得不请我的同学送我去了医院的急诊室。④ 离开急诊室以前，医生给我开了两种止痛药，告诉我回家以后一定要按时吃药。最后，医生又给我开了一张医生证明，让我这个星期不要着急去上课，跟老师请几天假，就在家安心养病，多休息，少动。",
       "③ Last Monday while exercising in the gym I carelessly injured my back and rested a few days. Later it got a little better, so I tried to raise both hands, and suddenly my back hurt again, and the pain got worse and worse; finally I had no choice but to ask my classmate to take me to the hospital emergency room. ④ Before leaving the emergency room the doctor prescribed two kinds of painkillers and told me I must take them on time after getting home. Finally the doctor also gave me a doctor’s certificate and told me not to hurry to class this week, to ask the teacher for a few days’ leave, to recuperate at home with peace of mind, to rest more and move less. (Student 2’s two slips; translation mine)")
TR3 = [("后来有一点好转，所以我就试着举起双手，突然后背又疼起来，而且疼痛越来越严重，最后不得不请我的同学送我去了医院的急诊室。", "1. Later it got a little better, so I tried to raise both hands, and suddenly my back hurt again, and the pain got worse and worse; finally I had no choice but to ask my classmate to take me to the hospital emergency room. (translation mine)"), ("等拍的片子出来后，医生告诉我幸亏没有伤到骨头，所以不需要住院治疗，但是得打针、输液治疗。", "2. When the picture came out the doctor told me that luckily the bone wasn’t injured, so no hospitalization was needed, but I had to have an injection and an infusion. (mine)"),
       ("最后，医生又给我开了一张医生证明，让我这个星期不要去上课了，跟老师请几天假，就在家安心养病，多休息，少动。", "3. Finally the doctor gave me a doctor’s certificate and told me not to go to class this week, to ask the teacher for a few days’ leave, to recuperate at home with peace of mind, and to rest more and move less. (mine)")]
JOKE = ("去医院检查后，医生拿着我的报告单说：“幸亏你来得早……”我吓出了一身冷汗，以为自己得了什么重病，结果医生慢慢地说：“再晚点，我就下班了。”",
        "After the examination at the hospital the doctor held my report and said, “Luckily you came early…” I broke out in a cold sweat, thinking I had some serious illness, and then the doctor slowly said, “A little later and I would have gone off duty.” (the book’s joke; translation mine. Answer: the patient was scared because 幸亏你来得早 sounds as if a serious illness was caught only just in time; the doctor really meant he was about to finish work.)")
L6 = lesson(
    "Lesson 21 Presentation 3 skill integration: 120, sick-leave notes and a back injury",
    "120 · 病假条 · 请假 批准 · 伤到后背 · 幸亏你来得早",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing, Speaking and Reading)",
             "A. Listen to three dialogs once and answer: 1. What is 120? 2. When should people call this number? B. Listen again and complete the table (Dialog 1–3: who called 120 and the patient’s relation; the patient’s symptoms). C. Work in groups of three and share. D. Discuss: 1. What number should people call in the U.S. when they have an emergency? 2. Who is part of an emergency team in the U.S.? E. Share your answers and read the scripts. (Audio, not included; 120 is the emergency number for ambulances in China, as the scenario later in the lesson shows.)"),
        card("Activity 2 (Listening, Writing, Speaking and Reading)",
             "A. Listen to a voicemail and mark the statements True or False; pair up, share and explain your reasoning: 1. 小雨给妈妈打电话留言。 2. 小雨今天不能回家因为她病了。 3. 小雨和室友叫了一辆出租车去医院急诊室。 4. 小雨在医院呆了一个晚上，她的室友文文回宿舍了。 5. 老师下午会到医院看小雨和王玲。 6. 小雨这个周末不能回家，她得等出院以后才能回家。 B. Listen again and complete the table (who was sent to the emergency room; when; how; symptoms; details about the emergency room; examinations; diagnosis; treatment; what the speaker and her roommate did for the patient; other details). C. Form a group of three and exchange. D. Read the script and compare. (Audio, not included; the book prints no key.)"),
        card("Activity 3 (Reading, Speaking, Listening and Writing)",
             "Read the notes from three students and complete the tasks. A. Pre-reading: guess the meaning of the words 病假, 病假条, 便条, 事假（条）, 批准. B. Work in groups of three; each student reads one note, determines what it is about and what is being requested, and writes the answers in the table. C. Exchange your information. D. Each student writes a sick-leave note or a leave note in Chinese and posts it on linoit.com, including reasons and requests. E. Share your note with the class. The three notes (the book prints the dates in digits):",
             tables=[SUPP3, NTB], examples=[D(*NOTE1), D(*NOTE2), D(*NOTE3)]),
        card("Activity 4 (Reading, Speaking and Listening)",
             "Read the following passage about a student’s ER experience and complete the tasks. A. Pair up. Each student receives two slips from the teacher, reads two parts of the passage, writes a summary of each part and exchanges the information with the partner. B. Together, order the paragraphs ①–④ into a logical story and share it with the class (Correct Order: _ → _ → _ → _). My order: ③ → ① → ④ → ② (③ the injury and the trip to the ER, ① the ER treatment, ④ leaving with medicine and a note, ② three days at home). C. Translate three sentences from the passage (sample translations below). D. Share your translation with the class. Student 1’s and Student 2’s slips:",
             examples=[D(*S1P), D(*S2P)] + [D(z, e) for z, e in TR3]),
        card("Activity 5 (Reading and Speaking)",
             "Read the following dialog (a joke about a hospital) and answer the question: Why was the patient scared, initially? What did the doctor really mean?",
             examples=[D(*JOKE)]),
    ],
    exercises=[
        M("What is 120 in China?", "The emergency (ambulance) number", ["A bank hotline", "The weather line", "A taxi company"], "120 = emergency centre."),
        M("What did David ask for in his note?", "One and a half hours’ leave", ["Three days’ leave", "Half a day’s leave", "A week’s leave"], "请假一个半小时."),
        M("Why did David need to see a doctor?", "He slept badly and was dizzy with a bad headache", ["He broke his arm", "He lost his keys", "He had a toothache"], "睡得不好，头晕、头疼得特别厉害."),
        M("What did Mark ask for?", "Half a day’s leave", ["One hour", "Three days", "A week"], "特请半天假."),
        M("Why did Mark need to leave?", "His child had a high fever and a bad cough", ["His wife was away", "He was sick", "He had an exam"], "孩子发高烧三十九度，咳嗽得非常厉害."),
        M("What had happened to Linda?", "She was sent to the ER with gastroenteritis and had to stay three days", ["She broke a leg", "She had a cold", "She lost her passport"], "被送进了医院的急诊室…住三天院."),
        M("Who will bring Linda’s note and the doctor’s certificate?", "王兰 (Wang Lan)", ["Linda herself", "The doctor", "Her mother"], "请王兰带给您."),
        M("What is 批准?", "To approve", ["To refuse", "To cancel", "To forget"], "希望您能够批准."),
        M("What happened to the student in the ER passage?", "He hurt his back in the gym and later it hurt again", ["He fell from a bike", "He got a fever", "He burned his hand"], "不小心伤到了后背."),
        M("What did the doctor say about the X-ray?", "Luckily the bone was not injured", ["The bone was broken", "He needed an operation", "Nothing could be seen"], "幸亏没有伤到骨头."),
        M("What did the doctor give him before he left?", "Two painkillers and a doctor’s certificate", ["Only a bill", "A wheelchair", "A letter to his parents"], "两种止痛药…医生证明."),
        M("In the joke, what did the doctor really mean?", "A little later and he would have gone off duty", ["The illness was very serious", "The patient was very early", "The report was lost"], "再晚点，我就下班了."),
        F("特向您请假一个半小时，希望您能够___准。", "批", PART, "批准: approve."),
        F("医生又给我开了一张医生证___。", "明", PART, "证明: certificate."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese in context
CALL = [("接线员", "您好，这里是幺二零急救中心。请问出什么事了？", "Hello, this is the 120 emergency center. What has happened? (sample call, mine)"), ("我", "我的室友肚子疼得很厉害，一直呕吐，还发高烧。", "My roommate has a terrible stomach ache, keeps vomiting and has a high fever. (mine)"), ("接线员", "你们在哪儿？请告诉我地址。", "Where are you? Please tell me the address. (mine)"),
        ("我", "我们在上海复旦大学的二号宿舍楼。", "We are in Dormitory Building 2 at Fudan University in Shanghai. (mine)"), ("接线员", "病人多大年纪？他有没有意识？", "How old is the patient? Is he conscious? (mine)"), ("我", "二十岁，他有意识，可是疼得说不出话。", "Twenty. He is conscious, but in too much pain to speak. (mine)"),
        ("接线员", "好，救护车马上就到。请不要给他吃东西，也别让他一个人。", "OK, the ambulance will be there at once. Please don’t give him anything to eat, and don’t leave him alone. (mine)"), ("我", "好的，谢谢您！", "OK, thank you! (mine)")]
SL = ("王老师：您好！我是琳达。我的室友文文昨天晚上因为腹痛、呕吐和发烧，被送进了医院的急诊室。医生说她得了急性肠胃炎，需要住三天院，所以这几天不能来上课。特向您请三天假，希望您能够批准。谢谢！学生：琳达",
      "Teacher Wang: Hello! I am Linda. My roommate Wenwen was taken to the hospital emergency room last night because of stomach pain, vomiting and fever. The doctor said she has acute gastroenteritis and needs to stay three days, so she cannot come to class these days. I am asking you for three days’ leave for her and hope you can approve it. Thank you! Student: Linda. (my draft of the sick-leave note for a roommate, Activity 1C)")
ERS = ("我的室友上个星期五晚上突然肚子疼，疼得很厉害，还一直呕吐。我和另一个室友赶紧给一二零打了电话，救护车十分钟就到了，把他送到了医院的急诊室。医生给他验了血，做了透视，说他得了急性肠胃炎，需要住院。他住了三天院，现在好多了。",
       "Last Friday night my roommate suddenly had stomach pain, a terrible one, and kept vomiting. Another roommate and I hurried to call 120; the ambulance arrived in ten minutes and took him to the hospital emergency room. The doctor did a blood test and an X-ray and said he had acute gastroenteritis and needed to be hospitalized. He stayed three days and is much better now. (my sample ER story for Activity 2, organized by who, what, where, when, how and why)")
ERT = table(["问题", "在美国看急诊 (mine)", "在中国看急诊 (mine)"], [["急救电话", "九一一", "幺二零"], ["何时去急诊室", "病情很急、很严重的时候", "病情很急、很严重的时候"], ["其它信息", "自己查一查", "自己查一查"]],
            title="Activity 3: the comparison chart (the rest of the chart depends on your research; I fill only the two entries known from this lesson and general knowledge, and put 自己查一查, “look it up yourself”, in the last row)", say=[0, 1, 2])
L7 = lesson(
    "Lesson 21 Presentation 3 using Chinese in context: calling 120, an ER story, ERs in China and the U.S.",
    "看急诊 · 打幺二零 · 病假条 · 急诊室的故事 · 中美看急诊",
    requires=[],
    cards=[
        card("Activity 1 (Writing, Speaking, Listening and Reading): 看急诊",
             "Scenario: while you and your classmates are studying in Shanghai, one of your housemates has a medical emergency. You and your friend need to call the local emergency center and get your roommate to an emergency room for treatment, then help the roommate ask for sick leave and tell your teacher what happened. A. Work in groups of three. Two members prepare a phone call to the local emergency center; the other acts as the 120 operator and prepares questions to ask the callers; all jot down key words and important information. B. In your group call the emergency hotline 120 and take turns explaining what happened and what help you need; the operator responds. C. Pair up. Text your teacher to ask for sick leave for your housemate and write a draft of the sick-leave note (病假条). D. Find two other students to form a new group of three; your teacher calls you to ask what happened after receiving your message. Include: 1. when, 2. symptoms, 3. what you did, 4. checkups, 5. diagnosis, 6. treatment, 7. estimated recovery time, 8. other information. E. The class reads the sick-leave notes together. My sample call and note:",
             examples=dlg(CALL) + [D(*SL)]),
        card("Activity 2 (Writing, Speaking and Listening): 急诊室的故事",
             "Scenario: after one week recovering from a medical emergency you are back in your classroom at Fudan University in Shanghai and your teacher asks you and your classmates to share your own emergency room stories. A. Individually prepare your story in Chinese and list emergency-related vocabulary; use the EEIs (who, what, where, when, how, why) and additional information to organize it. B. Create a story based on your own experience or make one up, with at least six to eight complete sentences. C. Post your story on linoit.com and share in groups of three. My sample story:",
             examples=[D(*ERS)]),
        card("Activity 3 (Listening, Writing and Speaking): 中美看急诊",
             "Scenario: some of your Chinese friends ask you about going to an ER in the U.S., because they have heard stories about expensive medical bills, long waiting times and bad experiences. Do some research online with your classmates and create a comparison chart in Chinese showing the differences between ER visits in China and the U.S. A. Work in pairs and watch the video clip on YouTube that you found during your research (not included); in Chinese characters take notes of key words and important information. B. Research online and collect information (Student 1: the ERs in the U.S.; Student 2: the ERs in China): 1. number to call, 2. when to go to an ER, 3. how to go there, 4. what to expect, 5. expected waiting time, 6. procedures in the ER, 7. checkups and treatment, 8. how to pay (bills), 9. other information. C. Exchange information and complete the table. D. Share your completed table with the class and answer any questions. The table’s headings are 急救电话, 何时去急诊室, 怎么去急诊室, 急诊是什么样子, 等候时间, 急诊程序, 检查、治疗, 付费（账单）, 其它信息.",
             tables=[ERT]),
    ],
    exercises=[
        M("Where is the emergency scenario set?", "Shanghai", ["Chengdu", "Beijing", "Taipei"], "While studying in Shanghai."),
        M("Who plays the 120 operator in Activity 1?", "The third member of the group", ["The teacher", "A doctor", "Nobody"], "The other member acts as the operator."),
        M("What do you text your teacher?", "A request for sick leave for the housemate", ["A homework answer", "A photo of the hospital", "A thank-you note"], "ask for sick leave."),
        M("What does the teacher want to know on the phone?", "When, symptoms, what you did, checkups, diagnosis, treatment, recovery time", ["Where you bought lunch", "The price of a taxi", "Your exam scores"], "The eight points."),
        M("What are the EEIs in Activity 2?", "Who, what, where, when, how and why", ["Names, ages and phones", "Food, drink and sleep", "Yes, no and maybe"], "who, what, where, when, how, and why."),
        M("What do Chinese friends worry about in the U.S. ER?", "Expensive bills, long waits and bad experiences", ["Too many doctors", "Free food", "No parking"], "expensive medical bills, long waiting times and bad experiences."),
        F("我们赶紧给幺二零打了电话，救护___马上就到。", "车", PART, "救护车: ambulance."),
        F("医生说她得了急性肠胃炎，需要住三天___。", "院", PART, "住院: be hospitalized."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 21 Presentation 3 vocabulary", "42 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book prints 多亏(了) with the 了 in brackets; I list 多亏了.", VOC3)

# ------------------------------------------------------------------ 9. area studies
L9 = lesson(
    "Lesson 21 Area Studies: China’s Healthcare Sector, Promising for 2020 and Beyond",
    "医疗行业 · 医保覆盖 · 健康科技 · 医疗人工智能 · 2020年以后",
    requires=[],
    cards=[
        card("China’s Healthcare Sector Promising for 2020 and Beyond (1)",
             "In China, many sectors of the healthcare industry are growing rapidly. There are numerous reasons: urbanization, an aging population, a continuous rise in wages and living standards for Chinese citizens, greater innovation in high-tech and broader access to healthcare. China constantly improves its health statistics: per capita healthcare spending in China has risen from $42 in 2000 to $398 in 2016, according to World Bank statistics. China passed Japan in total healthcare spending in 2016 with $574 billion compared to Japan’s $469 billion and passed the U.S. in hospital beds per 1,000 persons, with 3.8 for China and only 2.9 in the U.S., according to OECD data. China is seeing some of the fastest growth in this category, putting it ahead of countries such as Norway, Canada and the UK. This is in part due to Chinese government policies such as increased funding for hospitals."),
        card("(2) Doctors, nurses, life expectancy and the reasons for growth",
             "The number of doctors per 1,000 inhabitants has also been continuously rising in China since 2002, from 1.13 to 2.01 in 2017, according to OECD health data, putting it above the East Asian and Pacific average. A similar development is seen in the number of nurses per 1,000 inhabitants, with 1 in 2004 rising to 2.7 in 2017. Life expectancy has also continuously risen in China: according to statistics for the United Nations World Population Prospects the current life expectancy for Chinese citizens is 76.79 years, significantly higher than the world average life expectancy of 72 years. The growing healthcare sector is in many aspects a byproduct of China’s recent economic rise. Several hundred million people were lifted out of poverty in recent decades, which led to overall higher living standards and affordability of healthcare services. This in turn created the continuously rising life expectancy, with more people reaching retirement age than ever before, which further increases the demand for healthcare services. Within the last two decades China has benefited from large-scale reforms in the fields of medical infrastructure and insurance as well as the opening-up of its healthcare market. Focus has been on developing urban areas and continuously making healthcare more accessible in rural China. This has boosted development and the number of hospitals, doctors and medical equipment."),
        card("(3) Medical insurance and health tech",
             "The most important contributor might be that, according to the State Council, China has created the world’s largest network for basic medical insurance accessible for all, and formed a healthcare service system encompassing both urban and rural areas. By the end of 2016 basic medical insurance had reached over 1.3 billion citizens nationwide, accounting for more than 95 percent of the total population. Promising industries for 2020 and beyond: health tech and medical AI. To tackle overcrowded hospitals in an innovative way, the government made it clear that health technology is a strategic area of development for China. It features heavily in both the 13th Five-Year Plan (2016–2020) and its Healthy China 2030 strategy. In April 2018 the State Council also issued new guidelines to promote internet-based healthcare, encouraging medical institutions to leverage internet-based technologies to improve the efficiency of medical services. China’s large number of smartphone and internet users (700 million today) provides large potential for more technology use in healthcare subsectors. Everything can be done via apps in the future, also called “fingertip medical treatment”. Data from the National Health Commission showed that in 2017 China’s online healthcare market reached 32.5 billion yuan ($4.6 billion), 45.87 percent higher than that of the previous year. The market will grow to 90 billion yuan by 2020."),
        card("(4) WeChat, medical AI and the outlook",
             "Tencent, for example, has already been steadily building up a network of participating hospitals, over 38,000 medical facilities as of 2017, where users can book doctors’ appointments through their WeChat Intelligent Healthcare to avoid long lines at medical facilities. Following their health checkup, patients can also conveniently access their medical reports through WeChat and pay for their medical bills. Also, China is a frontrunner in the field of medical AI. In 2018 Alibaba’s health unit introduced AI software that could help interpret CT scans and an AI medical lab to help doctors make diagnoses. Deep-learning algorithms trained through the data of billions can analyze medical outputs like CT and MRI images with a close to 100 percent accuracy. Tencent established the AI Medical Innovation System or AIMIS, an AI-powered diagnostic medical imaging service, available so far in over 10 hospitals across the country. Images of patient tissue are fed into the AI software, which can then determine in under four seconds whether the body looks normal, inflamed or cancerous. Currently over 130 Chinese companies are working on applying AI in healthcare, with their number expected to grow even further in 2020. Outlook: the healthcare market in China is expected to reach 198 billion yuan ($28.59 billion) in 2026, increasing tenfold from 2016, according to China Briefing. China believes it is the government’s duty to further regulate the market through innovative measures and policies and assure that with the growth of the healthcare sector medical treatment remains affordable for all citizens. The programs of Healthy China 2020 and Healthy China 2030 both outline comprehensive health care reforms which aim to ensure universal healthcare access as well as improve the overall health situation of all Chinese people. China has managed to progress in three fields simultaneously to ensure stable growth of the healthcare sector: reducing overcrowding of hospitals, increasing quality of healthcare, and at the same time keeping healthcare affordable and accessible to all. (References printed in the book: Chinadaily (2020), Michael Santiago (2020), Ali Sheikh (2020).)"),
    ],
    exercises=[
        M("Which factor is NOT given as a reason for growth?", "A fall in the population", ["Urbanization", "An aging population", "Rising wages and living standards"], "The list: urbanization, aging population, rising wages, innovation, access."),
        M("What was per capita healthcare spending in China in 2016?", "$398", ["$42", "$574", "$469"], "$42 in 2000 to $398 in 2016."),
        M("Compared with the U.S., how many hospital beds per 1,000 persons does China have?", "3.8 against 2.9", ["2.9 against 3.8", "1.0 against 2.0", "5 against 5"], "3.8 for China and only 2.9 in the U.S."),
        M("How did the number of doctors per 1,000 change from 2002 to 2017?", "From 1.13 to 2.01", ["From 2.01 to 1.13", "From 1 to 2.7", "No change"], "1.13 to 2.01."),
        M("What is the life expectancy of Chinese citizens now, per the passage?", "76.79 years", ["72 years", "65 years", "85 years"], "76.79 years vs a world average of 72."),
        M("How many citizens does basic medical insurance cover (end of 2016)?", "Over 1.3 billion, more than 95 percent", ["About 100 million", "About 50 percent", "Only urban citizens"], "over 1.3 billion…95 percent."),
        M("What is “fingertip medical treatment”?", "Doing everything via apps", ["Acupuncture", "Hand surgery", "Finger painting"], "Everything can be done via apps."),
        M("How large was China’s online healthcare market in 2017?", "32.5 billion yuan, 45.87 percent up", ["90 billion yuan", "198 billion yuan", "4.6 million yuan"], "32.5 billion yuan."),
        M("What can Tencent’s WeChat Intelligent Healthcare do?", "Book appointments, show reports and pay bills", ["Perform surgery", "Deliver medicine by drone", "Print insurance cards"], "book doctor’s appointments…access medical reports…pay."),
        M("How fast can Tencent’s AIMIS decide whether tissue looks normal, inflamed or cancerous?", "In under four seconds", ["In an hour", "In a day", "In a week"], "in under four seconds."),
        M("How much is the Chinese healthcare market expected to reach in 2026?", "198 billion yuan, tenfold from 2016", ["90 billion yuan", "10 billion yuan", "32.5 billion yuan"], "198 billion yuan."),
        M("Which three fields is China progressing in simultaneously?", "Reducing overcrowding, increasing quality and keeping care affordable", ["Tourism, sports and music", "Mining, steel and oil", "Fashion, film and food"], "reducing overcrowding, increasing quality, affordable."),
    ],
)

UNIT = unit("第二十一课 Presentation 3: 急诊, 起来, 把 + 处所补语, 不要, Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9])
