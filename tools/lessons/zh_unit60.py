"""Unit 60: Lesson 21 (Seeing a Doctor) Presentation 1 from the book's texts: registering at the hospital, the six activities (map, 证, dialogs, Linda's
passage, the flow chart), 应该/该, 别, 那么/这么, the skill-integration activities (registration chart and two hospital notices), the using-Chinese
activities and the vocabulary list. Audio, pictures, links and the song lyrics of Activity 8 are not included; numbers the book writes as digits are
spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l21_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('得买', 0, 'dei3'), ('得付', 0, 'dei3'), ('得等', 0, 'dei3'), ('得带', 0, 'dei3'), ('得早', 0, 'dei3'), ('挂号处', 2, 'chu4'), ('交费处', 2, 'chu4'), ('划价处', 2, 'chu4'), ('到处', 1, 'chu4'), ('看好', 0, 'kan1')):
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
P1 = [("病人", "你好！请问在哪儿挂号？", "Hello! Where do I register, please?"), ("导医", "你是第一次来看病吧？", "This is your first time here to see a doctor, isn’t it?"),
      ("病人", "是的，我第一次来你们医院看病，还没有预约。", "Yes, it’s my first time seeing a doctor at your hospital, and I haven’t made an appointment."), ("导医", "这样啊，你带身份证了吗？第一次挂号需要身份证。", "I see. Did you bring your ID card? For the first registration you need an ID card."),
      ("病人", "带了。", "I did."), ("导医", "你要挂哪一科？", "Which department do you want to register for?"),
      ("病人", "我还不清楚该挂哪一科。我有点发烧、头疼，还拉肚子。", "I’m still not clear which department I should register for. I have a bit of a fever, a headache and diarrhea."), ("导医", "应该挂内科。我们有普通门诊和专家门诊，你想挂哪一种？", "You should register for internal medicine. We have regular outpatient and specialist outpatient; which kind do you want?"),
      ("病人", "我的病情没有那么严重，就挂普通门诊吧。", "My condition isn’t that serious, so I’ll register for the regular outpatient clinic."), ("导医", "挂号的时候，你得买一本病历。", "When you register you have to buy a medical record book."),
      ("病人", "医保卡呢？你们需不需要？", "What about a medical insurance card? Do you need it?"), ("导医", "没有医保卡也可以，但你得付现金。", "It’s fine without a medical insurance card, but you have to pay cash."),
      ("病人", "好的，谢谢你。", "OK, thank you."), ("导医", "对了，你还可以办一个就诊卡。有了就诊卡以后，你就可以直接在网上扫码预约了。", "Oh, and you can also get a patient card. Once you have the patient card you can scan the code and make appointments directly online."),
      ("病人", "太好了，下次我一定试试。", "Great, next time I’ll definitely try it."), ("导医", "下次看病的时候，别忘了带上就诊卡和病历本。", "Next time you see the doctor, don’t forget to bring the patient card and the medical record book.")]
L1 = lesson(
    "Lesson 21 Presentation 1: registering at the hospital",
    "在哪儿挂号 · 第一次看病 · 内科 普通门诊 专家门诊 · 病历 医保卡 就诊卡",
    requires=[],
    cards=[
        card("Learning objectives (Lesson 21, Seeing a Doctor, 看病)",
             "Upon completion of this lesson you will be able to: ask for information about registering in a hospital; discuss your diseases and symptoms with a doctor and ask questions about examinations, taking medicines and filling prescriptions; describe your experience when seeing a doctor or going to an ER. To do so you must master the new words and phrases in the Core Vocabulary section, the modal verb 应该/该 (能愿动词), the use of 那么/这么, the use of 别 (negative imperative), degree complements with 得 (程度补语), adjectives as predicates (2) (形容词谓语), adjectives used as adverbial adjuncts, the compound directional complement 起来 (趋向结构), the 把 construction with a locative complement and the use of 不要 (negative imperative). The Area Studies topic is China’s healthcare sector, promising for 2020 and beyond. The lesson belongs to Unit 4, Survival Skills and Social Factors."),
        card("Getting Started",
             "Pair up and discuss: A. What should you do if you go to a doctor for the first time in the U.S.? B. Examine the images (not included) and guess what you need to do when you see a hospital doctor in China for the first time. C. How do you usually make an appointment with doctors in the U.S.?"),
        card("Presentation 1: 在医院挂号", "The book also prints the dialog in traditional characters. The translations are mine.", examples=dlg(P1)),
    ],
    exercises=[
        M("What does the patient ask at the start?", "Where to register", ["Where the pharmacy is", "How much the medicine costs", "Where the taxi stand is"], "请问在哪儿挂号?"),
        M("Why does the guide nurse ask for an ID card?", "The first registration needs one", ["Every visit needs one", "To open a bank account", "To pay the bill"], "第一次挂号需要身份证."),
        M("Which three symptoms does the patient have?", "A bit of fever, a headache and diarrhea", ["A cough, a sore throat and a rash", "A toothache and a sore leg", "A cold, a cough and dizziness"], "发烧、头疼，还拉肚子."),
        M("Which department does the guide nurse suggest?", "内科 (internal medicine)", ["外科 (surgery)", "牙科 (dentistry)", "眼科 (eye)"], "应该挂内科."),
        M("Why does the patient choose the regular outpatient clinic?", "His condition isn’t that serious", ["Specialists are closed", "It is free", "He knows the doctor"], "我的病情没有那么严重."),
        M("What does the patient have to buy when registering?", "A medical record book (病历)", ["A medicine box", "A bus ticket", "A hospital gown"], "你得买一本病历."),
        M("What happens if he has no medical insurance card?", "He has to pay cash", ["He cannot register", "He pays by phone only", "He gets a discount"], "没有医保卡也可以，但你得付现金."),
        M("What can he do after getting a 就诊卡?", "Scan the code and book appointments online", ["Skip the doctor", "Get free medicine", "Register in two departments"], "直接在网上扫码预约."),
        M("What reminder does the guide nurse give at the end?", "Bring the patient card and the record book next time", ["Come early", "Bring cash", "Bring a friend"], "别忘了带上就诊卡和病历本."),
        M("What does 看病 mean?", "To see a doctor", ["To watch a movie", "To visit a sick friend", "To look at a map"], "看病: see a doctor."),
        F("你带身份___了吗？", "证", PART, "身份证: ID card."),
        F("我的病情没有那么严___，就挂普通门诊吧。", "重", PART, "严重: serious."),
        F("挂号的时候，你得买一本病___。", "历", PART, "病历: medical record."),
        F("下次看病的时候，别___了带上就诊卡和病历本。", "忘", PART, "别忘了: don’t forget."),
    ],
)

# ------------------------------------------------------------------ 2. activities 1-6
FLOORS = table(["楼层 (mine)", "地方"], [["三楼", "无"], ["二楼", "外科门诊，候诊室，内科门诊"], ["一楼", "挂号处，导医台，交费处，药房，划价处，医院大门"]],
               title="Activity 2: the hospital map (the labels stand at the bottom of each band of the picture; the third-floor band is empty, which fits question C)", say=[1])
PLC = table(["地方 (mine)", "在那儿可以做什么 (mine)"],
            [["挂号处", "挂号，买病历本"], ["导医台", "问路，问怎么挂号、挂哪一科"], ["交费处", "交费"], ["划价处", "划价"], ["药房", "取药"], ["医院大门", "进出医院"], ["候诊室", "等护士叫号"], ["内科门诊、外科门诊", "看病"]],
            title="Activity 2A: what you can do at each place (my answers; the book leaves it open)", say=[0, 1])
ZH = table(["带“证”的词 (mine)", "意思"], [["身份证", "ID card"], ["学生证", "student card"], ["工作证", "work badge"], ["驾驶证", "driver’s license"], ["证件", "documents of identity"], ["证明", "certificate, to prove"], ["医生证明", "doctor’s note"], ["签证", "visa"]],
           title="Activity 3: words with 证 (the book leaves the diagram blank; these are mine)", say=[0])
DL4 = [("你好，请问挂号处在哪儿？", "挂号处在一楼大厅的左边。", "1. A: Hello, where is the registration desk, please? B: The registration desk is on the left of the first-floor hall. (A’s blank filled by me)"), ("挂号的时候，我都需要带什么？", "你得带身份证和医保卡。", "2. A: When I register, what do I need to bring? B: You have to bring your ID card and your medical insurance card. (B’s blank mine)"),
       ("你想挂哪一科？", "我想挂内科。我有点发烧，还头疼。", "3. A: Which department do you want to register for? B: I want internal medicine. I have a bit of a fever and a headache. (mine)"), ("有了病历卡以后，你就可以直接在网上预约了。", "太好了，下次我一定试试。", "4. A: Once you have the record card, you can make appointments directly online. B: Great, next time I’ll definitely try it. (A’s blank mine)"),
       ("以后看病的时候，别忘了带上身份证和病历本。", "好的，我知道了。", "5. A: When you see the doctor in the future, don’t forget to bring your ID card and record book. B: OK, I know. (A’s blank mine)")]
DLG4 = []
for a, b, e in DL4:
    lab, rest = e.split(" A: ", 1)
    qa, rb = rest.split(" B: ", 1)
    DLG4 += dlg([("甲", a, lab + " A: " + qa), ("乙", b, "B: " + rb)])
LN1 = ("琳达以前从来没在中国看过病。第一次去医院看病以前，朋友告诉琳达最好带上她的护照，因为到了医院以后挂号的时候需要出示证件。如果她不知道在哪儿挂号，或是挂哪一科，可以去导医台问导医。",
       "Linda had never seen a doctor in China before. Before going to the hospital for the first time, her friend told her it was best to bring her passport, because after reaching the hospital she would need to show identification when registering. If she doesn’t know where to register, or which department, she can ask the guide nurse at the guide desk. (Student A’s part; the printed blanks are filled by me)")
LN2 = ("挂号时，她得买一本病历本，填好个人信息，然后去候诊室里等着护士叫号。叫到她的号时，她就可以进去看病了。看过一次病后，下次再去看病可以直接用就诊卡在网上预约，非常方便。但是，看病时她还是得带着病历本。",
       "When registering, she has to buy a medical record book and fill in her personal information, then wait in the waiting room for the nurse to call her number. When her number is called she can go in to see the doctor. After seeing the doctor once, next time she can use the patient card to make an appointment online directly, which is very convenient. But when seeing the doctor she still has to bring the record book. (Student B’s part; blanks mine)")
LN3 = ("琳达说，在中国看病跟在美国不一样。在美国看病，不需要去医院挂号，只要提前打电话或者上网预约就可以了。不过看病时也需要带着身份证和保险卡。",
       "Linda says that seeing a doctor in China is not the same as in the U.S. In the U.S. you don’t need to go to the hospital to register; you only need to call or book online ahead of time. But when seeing the doctor you also need to bring your ID and insurance card. (Student C’s part; blanks mine)")
FLW = table(["步骤", "初诊 (first visit)", "复诊 (return visit)"],
            [["第一步", "导医台", "出示身份证、医保卡、病历卡"], ["第二步", "出示身份证、医保卡", "自助挂号机挂号"], ["第三步", "选择挂号科室：普通或专家，内科或外科", "候诊室候诊"], ["第四步", "挂号窗口挂号", "就诊（看病）"],
             ["第五步", "购买、填写病历本", ""], ["第六步", "办病历卡", ""], ["第七步", "候诊室候诊", ""], ["第八步", "就诊（看病）", ""]],
            title="Activity 6: 门诊挂号流程图, the outpatient registration flow chart (my reading of the picture; 复诊 branch reads: show ID/insurance/record card, register at the self-service machine, wait, see the doctor)")
L2 = lesson(
    "Lesson 21 Presentation 1 activities: the hospital map, 证, dialogs, the flow chart",
    "Activities 1 to 6 · 挂号处 导医台 药房 · 带证的词 · 琳达在中国看病 · 门诊挂号流程图",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 1 once and answer: 1. What is the presentation about? 2. Where are the speakers? Is the first speaker familiar with the location? 3. What would the first speaker do after the conversation? B. Detailed listening: 1. What should the first speaker bring? 2. What is wrong with the first speaker? List three symptoms. 3. What are the available choices, and what is the decision? 4. What does the second speaker tell the first speaker to do? 5. What can the first speaker do on the next visit? 6. What reminder is given? (Audio, not included; the answers are in the dialog above.)"),
        card("Activity 2 (Reading, Speaking and Writing)",
             "A. Use the locations on the map to describe what you generally can do at each location. B. Pair up and share your answers. C. Could you add any other departments or rooms on the third floor? The map and my answers:",
             tables=[FLOORS, PLC]),
        card("Activity 3 (Reading, Writing and Speaking)",
             "How many words do you know that use the character 证? Write as many as you can in the diagram (use your dictionary if necessary). Mine:",
             tables=[ZH]),
        card("Activity 4 (Reading, Writing and Speaking)",
             "Pair up. Read the following sentences and complete the dialogs in your own words. The book prints one half of each exchange; the other half is my own completion:",
             examples=DLG4),
        card("Activity 5 (Listening, Speaking and Reading)",
             "A. Listen to the audio passage and answer: 1. What is the main idea of the passage? 2. What does she need to do before going to a hospital in China for the first time? 3. What does she need to do after she registers? 4. What are the differences between seeing a doctor in China and in the U.S.? B. Work in groups of three; listen again and each member transcribes the missing sentences in their part (Student A, B, C). C. Share your answers and explain the meanings of the missing sentences; then read the script together. The audio and script are not included; the three parts below have the missing sentences filled by me:",
             examples=[D(*LN1), D(*LN2), D(*LN3)]),
        card("Activity 6 (Reading, Speaking, Listening and Writing)",
             "A. Study the diagram of the registration procedure at a Chinese hospital. B. Pair up. Student 1 works at the hospital’s front desk and Student 2 is a patient; the patient asks as many questions as possible to learn the registration procedure and the partner provides the information. C. After the conversation, create a flow chart of the procedure of seeing a doctor in the U.S. and share it with the class.",
             tables=[FLW]),
    ],
    exercises=[
        M("On the map, where is 挂号处?", "On the first floor", ["On the second floor", "On the third floor", "On the roof"], "Activity 4 says 挂号处在一楼大厅的左边."),
        M("On the map, where are 内科门诊 and 外科门诊?", "On the second floor", ["On the first floor", "On the third floor", "Outside"], "二楼."),
        M("Where do you wait for the nurse to call your number?", "候诊室", ["药房", "划价处", "医院大门"], "候诊室: waiting room."),
        M("Where do you get medicine?", "药房", ["导医台", "挂号处", "候诊室"], "药房: pharmacy."),
        M("Which word contains 证?", "身份证", ["病历本", "预约", "挂号"], "身份证."),
        M("Which documents does Linda need on a first visit?", "ID or passport", ["A library card", "A bus pass", "A concert ticket"], "出示证件."),
        M("In the flow chart, where does a first visit begin?", "导医台", ["自助挂号机", "候诊室", "药房"], "初诊 → 导医台."),
        M("In the flow chart, what do you do right after registering at the window?", "Buy or fill in the record book", ["See the doctor", "Pay the cash", "Leave"], "购买/填写病历本."),
        M("What do return patients (复诊) show?", "ID, insurance card and record card", ["Only a ticket", "Only cash", "A letter"], "出示身份证/医保卡/病历卡."),
        M("How is seeing the doctor in the U.S. different, according to the passage?", "You don’t go to the hospital to register, you make an appointment ahead", ["There are no doctors", "It is free", "You must queue at dawn"], "不需要去医院挂号."),
        F("你得带身份___和医保卡。", "证", PART, "身份证."),
        F("到了候___室，她要等着护士叫号。", "诊", PART, "候诊室: waiting room."),
    ],
)

# ------------------------------------------------------------------ 3. 应该
YG = table(["", "格式"], [["Positive", "Subject + 应该 + Verb + Object"], ["Negative", "Subject + 不 + 应该 + Verb + Object"], ["Interrogative", "Subject + 应该 + Verb + Object + (吗) ? · Subject + 应该 + 不应该 + Verb + Object ? · Subject + 应不应该 + Verb + Object ?"]],
           title="The modal verb 应该/该: the book’s patterns")
YE = [("第一次到医院去看病，你应该带着你的身份证。", "1. When you go to the hospital for the first time, you should take your ID card."), ("他太累了，应该回家休息。", "2. He is too tired; he should go home and rest."), ("你身体不好，应该常常锻炼，不应该吸烟。", "3. Your health is poor; you should exercise often and should not smoke. (the book glosses 吸烟 as xī yān, smoke)"),
      ("虽然小明不对，但是你也不应该打他。", "4. Although Xiaoming is wrong, you shouldn’t hit him either."), ("睡觉以前，应该刷牙吗？", "5. Should one brush one’s teeth before going to bed?"), ("我应该不应该告诉他这件事？", "6. Should I or shouldn’t I tell him this?"),
      ("你头疼，应不应该吃点药？", "7. You have a headache: should you take some medicine?"), ("马克，该你说了。", "8. Mark, it’s your turn to speak. (here 该 means “it’s your turn”; 应该 should not be used in this sense)")]
YN = [("这个句子不太难，你应该会翻译吧。", "1. This sentence is not too hard. You should be able to translate it. (应该 as expectation)"), ("他是中国人，应该喜欢吃饺子。", "2. He’s Chinese and should like dumplings. (应该 as a logical conclusion)"), ("我还不清楚该挂哪一科。", "The book’s first example: I’m still not clear which department I should register for. (该 is the informal form)")]
YM = [("你应该多喝水，早点睡觉。", "You should drink more water and go to bed earlier. (Activity 1A, mine)"), ("你不应该上课的时候玩手机。", "You shouldn’t play with your phone in class. (1B, mine)"), ("我应该不应该告诉老师我生病了？", "Should I tell the teacher I’m sick? (1D, mine)"), ("你应不应该去看医生？", "Should you go to see a doctor? (1D, mine)")]
CR = table(["我们应该／该做什么？ (mine)", "我们不应该／该做什么？ (mine)"], [["准时上课；上课认真听；多说汉语；每天做作业；有问题就问老师", "迟到；上课玩手机；上课吃东西；用英语聊天；不做作业"]],
           title="Activity 3: classroom shoulds and shouldn’ts (the book leaves the table blank; this is my list)", say=[0, 1])
L3 = lesson(
    "Lesson 21 Presentation 1 grammar: the modal verb 应该 / 该",
    "你应该带着身份证 · 不应该吸烟 · 应不应该 · 该你说了",
    requires=[],
    cards=[
        card("The Modal Verb 应该",
             "In Chinese, the modal 应该/该 denotes a moral obligation or practical necessity, similar to “ought to” or “should” in English. 应该 is the most common way to express “should,” and 该 is an informal way to say it. When 应该/该 is used as a modal verb it appears before a regular verb. Its negative is formed with 不, and its interrogative forms include both the 吗-question and the affirmative-negative patterns. Notes: 应该 may also be used like “should” in the sense of expressing “expectation” or “a logical conclusion.”",
             tables=[YG], examples=[D(z, e) for z, e in YE + YN]),
        card("Activity 1 (Writing, Speaking and Listening)",
             "In this activity you will advise your classmates what they should or shouldn’t do, using the optative verb 应该/该. A. Write five sentences for each of your classmates that tell them what they should do (应该/该). B. Write five sentences that tell them what they should not do (不应该/不该). C. Take turns giving sincere advice. D. In groups of three, one of you asks for advice using 应该不应该 / 该不该 / 应不应该 and the other two offer suggestions. The book leaves the lines blank; my sentences:",
             examples=[D(z, e) for z, e in YM]),
        card("Activity 2 and Activity 3",
             "Activity 2 (Listening, Writing and Speaking): listen to the passage and write the suggestions on what you should do when you see a doctor for the first time at a Chinese hospital (a table, 第一次去中国医院看病的建议). (Audio, not included.) Activity 3 (Speaking, Listening and Writing), Classroom Shoulds and Shouldn’ts: your class has a meeting on updating your classroom norms. A. Form groups of three and discuss what your class should and shouldn’t do in the classroom or during class; write your ideas in the table. B. Report your advice to the class. C. The class votes on the Dos and Don’ts and writes them on a flip chart for the classroom wall.",
             tables=[CR]),
    ],
    exercises=[
        M("What does 应该 express?", "Moral obligation or practical necessity (“should”)", ["Past experience", "Ability", "Permission"], "应该 = should."),
        M("Which is the informal form of 应该?", "该", ["可", "会", "要不要"], "该 is informal."),
        M("Where does 应该 stand?", "Before the main verb", ["After the object", "At the end of the sentence", "Before the subject"], "Subject + 应该 + verb."),
        M("How do you negate 应该?", "不应该", ["没应该", "应该不", "别应该"], "不应该."),
        M("Which sentence is a correct “should or shouldn’t” question?", "你头疼，应不应该吃点药？", ["你头疼，应该吃不吃药吗？", "你头疼，吃药应该不吗？", "你应该头疼不应该吃药？"], "应不应该."),
        M("What does 该你说了 mean?", "It’s your turn to speak", ["You should speak", "You must not speak", "You said it"], "该你说了: your turn (not 应该)."),
        M("What does 他是中国人，应该喜欢吃饺子 express?", "A logical expectation", ["An order", "A prohibition", "A promise"], "应该 can express expectation."),
        M("Which sentence is a prohibition?", "你不应该打他。", ["你应该回家休息。", "你应该带身份证。", "你应该吃药。"], "不应该."),
        F("第一次到医院去看病，你___该带着你的身份证。", "应", PART, "应该: should."),
        F("他太累了，应该回家___息。", "休", PART, "休息: rest."),
        F("虽然小明不对，但是你也不应该___他。", "打", PART, "打: hit."),
    ],
)

# ------------------------------------------------------------------ 4. 别
BE = [("对不起，我忘了你的生日是哪天。", "1. Sorry, I forgot which day your birthday is."), ("别忘了你明天早上要坐七点的飞机。", "2. Don’t forget you’re taking the seven o’clock flight tomorrow morning."), ("下次看病的时候，别忘了带上就诊卡和病历本。", "1. (别) Next time you see the doctor, don’t forget to bring the patient card and the record book."), ("下次看病的时候，不要忘了带上就诊卡和病历本。", "2. (不要) The same with 不要: 别 and 不要 can be used interchangeably.")]
BP = [("别动！", "1. Don’t move!"), ("请别说话。", "2. Please don’t talk!"), ("吃饭的时候，别说话。", "3. Don’t talk while eating."), ("请别叫太多的菜。我真地吃不下。", "4. Please don’t order too many dishes. I really can’t eat them all."), ("十二点了，该睡觉了，别看了！", "5. It’s twelve o’clock, time to sleep, stop watching!"),
      ("别说了，我不想听。", "6. Stop talking, I don’t want to hear it."), ("别问了，我不想说。", "7. Stop asking, I don’t want to say."), ("别玩了，快去写作业。", "8. Stop playing and go do your homework quickly.")]
BG = table(["格式", "意思"], [["别 + Verb + (Object)", "Don’t do …"], ["别 + Verb + (Object) + 了", "Stop doing …"]], title="Prohibitive 别 (negative imperative marker)")
UK = [("别晚交作业。晚交作业，直接减百分之十的作业成绩。", "1. Don’t hand in homework late. Late homework loses 10% of the homework grade directly. (the book writes 10%)"), ("别晚上一个人出门。英国深夜在街道上有不少从夜店酒吧出来的醉汉。", "2. Don’t go out alone at night. In the U.K. late at night there are quite a few drunks coming out of nightclubs and bars on the streets. (the book glosses 醉汉 as zuìhàn)"),
      ("别生病。英国留学看病要花很多时间，在医院里永远得等，而且看一次病要花好多钱。", "3. Don’t get sick. Seeing a doctor while studying in the U.K. takes a lot of time, you always have to wait in the hospital, and one visit costs a lot of money."), ("别在路上长时间看手机，一定要看好自己的包包和贵重物品。英国的小偷很多。", "4. Don’t look at your phone for a long time on the road; be sure to keep an eye on your bag and valuables. There are many thieves in the U.K."),
      ("别总是跟中国留学生一起玩。出来留学，多交几个外国朋友，锻炼英语能力和口语听力能力，感受外国的文化。", "5. Don’t always hang out with Chinese students. When you study abroad, make more foreign friends, practice your English and your speaking and listening, and feel the foreign culture."), ("别吃太多甜食和高热量食物。英国人热爱甜品，好吃但是无助于减肥。", "6. Don’t eat too many sweets and high-calorie foods. The British love desserts; they taste good but do not help you lose weight."),
      ("别带着护照到处跑，千万要看好。丢了护照补办很麻烦，花钱还花时间。", "7. Don’t carry your passport around; be sure to keep it safe. Replacing a lost passport is troublesome, costing money and time."), ("别听信不认识的人，尝试毒品。国内国外一个样，毒品不要试。", "8. Don’t believe people you don’t know and try drugs. At home or abroad it’s the same: don’t try drugs.")]
TIPS = [("别迟到！", "Don’t be late! (mine, a tip for new recruits)"), ("别说话了，快起床！", "Stop talking and get up quickly! (mine)"), ("别忘了叠被子。", "Don’t forget to make your bed. (mine)"), ("别玩手机了，该睡觉了。", "Stop playing with your phone; it’s time for bed. (mine)")]
L4 = lesson(
    "Lesson 21 Presentation 1 grammar: the prohibitive 别",
    "别忘了 · 别动 · 别说了 · 在英国千万别做什么",
    requires=[],
    cards=[
        card("Prohibitive 别",
             "In this lesson the guide nurse told the patient: 下次看病的时候，别忘了带上就诊卡和病历本。别忘了 is a fixed expression meaning “Don’t forget.” 了 is often used in this expression to focus on preventing the result of 忘. When 别 is used as a negative imperative marker it is similar to the English “Don’t!”. 别 and 不要 can be used interchangeably. A negative imperative is formed by placing 别 before a verb. When used for stopping an action that has been going on for a while, 了 is added to the end of the sentence.",
             tables=[BG], examples=[D(z, e) for z, e in BE + BP]),
        card("Activity 4 (Speaking and Listening)",
             "Game: A Naughty Kid. A. Work in groups of three. Take turns telling your group members “Don’t do something” using 别 + verb; the student who receives the command does the opposite. Example: Student A: 别唱歌！ Student B begins singing loudly. B. In groups of three, Student A gives a command to Student B with 应该; Student B does not follow the advice and performs the opposite; Student C uses 别…了 to stop Student B. Students take turns playing A, B and C. (Pictures, not included.)"),
        card("Activity 5 (Reading, Speaking and Listening)",
             "A. Read the following blog post about studying in the U.K. and guess from the title what it is about: 在英国千万别做什么？ B. Pair up, read the article and discuss whether the advice also fits the situation in the U.S. The eight items:",
             examples=[D(z, e) for z, e in UK]),
        card("Activity 6 (Writing, Speaking, Listening and Reading)",
             "Tips to New Recruits. In this activity you give advice to new recruits who will start basic training soon: tell them what you are frequently told to do, or not do, during basic training, using 别 + verb or 别 + verb + 了. A. Individually think of three to five things you were told not to do or to stop doing during basic training and take notes in the table. B. In a group of three share your list and write your tips on a flip chart. C. Share your tips with the class. A few of mine (the book leaves the table blank):",
             examples=[D(z, e) for z, e in TIPS]),
    ],
    exercises=[
        M("What does 别忘了 mean?", "Don’t forget", ["I forgot", "Forget it", "Never mind"], "别忘了: don’t forget."),
        M("Which word is interchangeable with 别?", "不要", ["不应该", "没有", "不是"], "别 and 不要."),
        M("What does 别 + verb + 了 mean?", "Stop doing it", ["Don’t start doing it", "Finish doing it", "Do it again"], "别 + verb + 了: stop."),
        M("How do you say “Don’t move!”?", "别动！", ["不动了！", "没动！", "别不动！"], "别动!"),
        M("How do you say “Stop talking, I don’t want to hear it”?", "别说了，我不想听。", ["别说，我不想听了。", "不说了，我别想听。", "别听了，我不想说。"], "别说了."),
        M("Which sentence stops an action that is already going on?", "别玩了，快去写作业。", ["别玩手机。", "请别说话。", "别动！"], "了 shows stopping."),
        M("What does the blog warn about homework in the U.K.?", "Late homework loses 10% of the grade", ["Late homework is ignored", "No homework is given", "Homework is only on paper"], "晚交作业，直接减百分之十的作业成绩."),
        M("Why shouldn’t you carry your passport around?", "Replacing a lost passport is troublesome", ["It is heavy", "It is too expensive", "It is not valid"], "丢了护照补办很麻烦."),
        M("What does the blog say about seeing a doctor in the U.K.?", "It takes a lot of time and money", ["It is free", "It is fast", "There are no doctors"], "看病要花很多时间…花好多钱."),
        F("下次看病的时候，___忘了带上就诊卡和病历本。", "别", PART, "别忘了."),
        F("请___叫太多的菜。我真地吃不下。", "别", PART, "请别…"),
        F("十二点了，该睡觉了，别看___！", "了", ["吗", "们", "呢"], "别看了: stop watching."),
    ],
)

# ------------------------------------------------------------------ 5. 那么 这么
NM = table(["", "格式"], [["Statement", "Sub. + 那么/这么 + adj./mental verbs (想/喜欢/爱…)"], ["Negation", "Sub. + 没有 + 那么/这么 + adj./mental verbs (想/喜欢/爱…)"]], title="那么/这么 (to emphasize degree)")
NE = [("我的病情没有那么严重，就挂普通门诊吧。", "The book’s first example: I’m not that sick, so I will register with a regular outpatient doctor."), ("天气这么冷，我不想出去锻炼了。", "1. The weather is so cold that I don’t want to go out to exercise."), ("老师今天那么忙，你还是不要去找她了吧。", "2. The teacher is so busy today; you’d better not go to find her."), ("你那么聪明，一定可以学好中文。", "3. You’re so smart; you can surely learn Chinese well."),
      ("他说得这么快，你们听得懂吗？", "4. He speaks so fast; can you understand?"), ("其实，北京的冬天没有那么冷。", "5. Actually, Beijing’s winter isn’t that cold."), ("他的中文不错，但也没有像你说的那么好。", "6. His Chinese is good, but not as good as you say. (the book writes 象)"), ("你这么喜欢玩手机，我那么不喜欢你只玩手机，不跟我聊天。", "7. You like playing with your phone so much, and I dislike so much that you only play with your phone and don’t chat with me.")]
ND = [("你和我关系这么好。", "1. You and I are on such good terms. (close by)"), ("你和他关系那么好。", "1. You and he are on such good terms. (not close by)"), ("他的病情没有你说的这么严重。", "2. His condition isn’t as serious as you say (here, near)."), ("他的病情没有他说的那么严重。", "2. His condition isn’t as serious as he says (there, far)."),
      ("他那么高，你这么矮。", "3. He (over there) is so tall, and you (right here) are so short."), ("她小时候那么能说，她现在怎么这么安静？", "4. She was so talkative when she was young. How is she so quiet now?")]
SM = [("这次考试我考得这么糟糕，一定通不过了。", "糟糕: I did so badly on this exam that I surely won’t pass. (the book’s example)"), ("你这么熬夜，身体会有问题的。", "熬夜: Staying up so late, your health will have problems. (the book’s example)"),
      ("今天这么闷热，我不想出去。", "闷热: It’s so hot and stuffy today that I don’t want to go out. (mine)"), ("你这么自由，真让我羡慕。", "自由: You are so free; I really envy you. (mine)"), ("那部电影那么恐怖，我不敢看。", "恐怖: That movie is so scary that I don’t dare to watch it. (mine)"),
      ("听到这个好消息，他这么兴奋。", "兴奋: Hearing this good news he is so excited. (mine)"), ("周末那么轻松，我可以睡到十点。", "轻松: The weekend is so relaxed that I can sleep until ten. (mine)"), ("这个歌这么流行，大家都会唱。", "流行: This song is so popular that everyone can sing it. (mine)"),
      ("办这个手续这么麻烦，我不想去了。", "麻烦: Going through this procedure is so troublesome that I don’t want to go. (mine)"), ("你的朋友那么漂亮，一定很受欢迎。", "漂亮: Your friend is so pretty and must be very popular. (mine)"), ("他教学生那么耐心，学生都喜欢他。", "耐心: He is so patient in teaching students that they all like him. (mine)"),
      ("你这么训练，一定会越来越强。", "训练: Training like this, you will surely get stronger and stronger. (mine)"), ("他们那么减肥，身体会不好的。", "减肥: Dieting that hard, their health will suffer. (mine)"), ("他这么干活，大家都很佩服他。", "干活: He works so hard that everyone admires him. (mine)"),
      ("你这么走路，什么时候才能到？", "走路: Walking like this, when will you ever arrive? (mine)"), ("今天的安检这么安检，我们要排很长的队。", "安检 (my sentence is awkward; see the next line)")]
SM = SM[:-1] + [("今天机场的安检这么严格，我们得早点到。", "安检: The security check at the airport is so strict today that we must arrive early. (mine)"), ("这家商店这么促销，一定会有很多人来。", "促销: With the shop running such a sale, many people will surely come. (mine)"), ("你这么做饭，我觉得太好吃了。", "做饭: Cooking like this, I think it’s delicious. (mine)"), ("他这么喝酒，对身体不好。", "喝酒: Drinking like this is bad for his health. (mine)"), ("你那么学习，一定能考好。", "学习: Studying like that, you will surely do well on the test. (mine)")]
L5 = lesson(
    "Lesson 21 Presentation 1 grammar: 那么 and 这么",
    "没有那么严重 · 这么冷 · 这么 (近) 和 那么 (远) · 一起造句",
    requires=[],
    cards=[
        card("The Use of 那么/这么",
             "In English, “that” and “so” are often used to emphasize the degree of an adjective. In Chinese, 那么 and 这么 serve the same function and may be used with both adjectives and verbs, carrying the meaning “in that manner (那么)” or “so…, in such a manner (这么).” Structurally 那么/这么 is placed before an adjective or a verb. Negation is made with 没有.",
             tables=[NM], examples=[D(z, e) for z, e in NE]),
        card("Difference between 这么 and 那么",
             "In Chinese 那么 and 这么 are essentially interchangeable, but they differ slightly. 这么 is used when the subject is near (in space or in time), when you would say “this” or 这个: 这么 + adj. = this + adj. (something close by). 那么 is used when the subject is far away (or in the past or not present), when you would say “that”: 那么 + adj. = that + adj. (something not close by).",
             examples=[D(z, e) for z, e in ND]),
        card("Activity 7 (Reading, Speaking and Listening)",
             "A competition to create as many sentences as possible using 那么/这么 + adj. or 那么/这么 + verb, with words from two cards. The adjective card: 糟糕, 闷热, 自由, 恐怖, 兴奋, 轻松, 流行, 麻烦, 漂亮, 耐心. The verb-phrase card: 熬夜, 训练, 减肥, 干活, 走路, 安检, 促销, 做饭, 喝酒, 学习. Work in two teams; each team picks one word from either card and tells it to the rival team, who create a sentence with 那么/这么 using that word and add more information if they can; then switch. The team with the most sensible and logical sentences wins. The book’s two examples and my sentences for the rest:",
             examples=[D(z, e) for z, e in SM]),
        card("Activity 8 (Listening, Reading, Writing and Speaking)",
             "A. Use the video link to listen to a Chinese pop song, 《没那么简单》 by 黄小琥 (Huang Xiaohu). B. Pair up, read the lyrics, find the meaning of the four sentences that follow and translate them into English. C. Share your answers with the class. The book prints the lyrics with pinyin and then four lines of the song that all use 没那么/没有那么 (… 简单 / … 容易). I leave the lyrics and those four lines out because they are song lyrics. The pattern in them is the one you have just learned: 没那么/没有那么 + adjective means “not that + adjective”, for example 学中文没有那么难。"),
    ],
    exercises=[
        M("What do 这么 and 那么 emphasize?", "The degree of an adjective or a verb", ["The time of an action", "The place of an action", "The number of things"], "To emphasize degree."),
        M("Where is 那么/这么 placed?", "Before an adjective or a verb", ["After the adjective", "At the end", "Before the subject"], "Before adj./verb."),
        M("How do you negate it?", "Sub. + 没有 + 那么/这么 + adj.", ["Sub. + 不 + 那么 + adj.", "Sub. + 那么 + 没 + adj.", "没有 + Sub. + 那么 + adj."], "没有那么."),
        M("Which is used when the subject is near?", "这么", ["那么", "Neither", "Both are far"], "这么 = near."),
        M("Which is used for something far away or in the past?", "那么", ["这么", "Neither", "Both are near"], "那么 = far."),
        M("“I’m not that sick, so I’ll register for the regular outpatient clinic.”", "我的病情没有那么严重，就挂普通门诊吧。", ["我的病情不那么严重，就挂普通门诊吧。", "我的病情那么没严重，就挂普通门诊吧。", "我的病情没严重那么，就挂普通门诊吧。"], "没有那么严重."),
        M("“The weather is so cold that I don’t want to go out.”", "天气这么冷，我不想出去锻炼了。", ["天气没这么冷，我不想出去。", "天气冷这么，我想出去。", "天气这么冷，我想出去。"], "天气这么冷."),
        M("Which sentence puts 他 far and 你 near?", "他那么高，你这么矮。", ["他这么高，你那么矮。", "他那么高，你那么矮。", "他这么高，你这么矮。"], "那 = far, 这 = near."),
        M("What does 你这么熬夜，身体会有问题的 mean?", "Staying up this late, your health will have problems", ["You never stay up", "Your health is fine", "You should sleep less"], "熬夜: stay up late."),
        F("我的病情没有那___严重。", "么", PART, "那么."),
        F("北京的冬天没有那么___。", "冷", PART, "冷: cold."),
        F("他说得这___快，你们听得懂吗？", "么", PART, "这么."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
CH = table(["预约方式", "办法"],
           [["手机预约", "支付宝生活号；微信公众号"], ["在线平台预约", "平安医疗导航平台；平安互联医疗平台支付宝生活号；平安预约医疗服务平台；平安联挂号服务"], ["电话预约", "医院预约电话 (the book prints the numbers 133 12570 12962 86986 and 0293–96238963)"], ["医院预约、社区预约", "诊间预约（医生诊间提前一个月预约）；社区卫生服务中心（提前十天预约）；自助机预约"], ["预约时间", "提前一周下午两点"]],
           title="Activity 3: the appointment chart (the website addresses printed in the chart are not reproduced)")
S1 = ("人工窗口挂号。挂号交费人工窗口位于门诊六到八楼。带身份证的病人，可到人工窗口填写病历信息登记表，购买病历本或办理病历卡，挂普通门诊看病。网上提前预约好了，如何挂号？一、可用支付宝或微信“预约取号”功能，完成手机取号。二、也可以在门诊大厅自助机上使用“预约取号”功能，自助取号。三、或是到门诊六到八楼人工窗口取号。",
      "Registering at the manual window. The manual registration and payment windows are on floors 6 to 8 of the outpatient building. Patients with an ID card can go to a manual window, fill in the medical-record information form, buy a record book or get a record card, and register for a regular outpatient visit. If you have booked online in advance, how do you register? 1. You can use the “collect number for appointment” function of Alipay or WeChat to collect a number on your phone. 2. You can also use the “collect number for appointment” function on the self-service machine in the outpatient hall. 3. Or go to the manual windows on floors 6 to 8 to collect a number. (Student 1’s part; the book writes 6-8 and 1、2、3; translation mine)")
S2 = ("自助机挂号。一、门诊各楼层的自助机有自助挂号、缴费、预约挂号、预约取号和自助办卡、账户管理等功能。二、自助机可以用现金、支付宝、银行卡等方式支付。三、第一次看病的病人，可以使用自助机办理病历卡：（一）用二代身份证通过自助机自助办理；（二）有支付宝的病人，可以使用自助机的“支付宝刷脸”功能自助办理；（三）也可以使用手机应用或支付宝申请电子病历卡或医保卡。",
      "Registering at the self-service machine. 1. The self-service machines on each floor of the outpatient building have the functions of self-service registration, payment, appointment registration, collecting a number for an appointment, getting a card and account management. 2. The machines accept cash, Alipay, bank cards and other ways of payment. 3. Patients on a first visit can use the machine to get a record card: (1) with the second-generation ID card through the machine; (2) patients with Alipay can use the machine’s “Alipay face scan” function; (3) or apply for an electronic record card or insurance card with a phone app or Alipay. (Student 2’s part; translation mine)")
ADV = table(["", "优点 (mine)"], [["人工窗口", "可以买病历本或办病历卡，有问题可以问工作人员"], ["自助机", "功能多，可以用现金、支付宝、银行卡付钱，也可以自己办卡"], ["网上预约", "提前预约好，到医院用手机或自助机取号就行了"]],
           title="Activity 5: the advantages of the three ways (the book leaves the table blank; this is my filling)", say=[1])
L6 = lesson(
    "Lesson 21 Presentation 1 skill integration: registration chart and two hospital notices",
    "挂号流程 · 预约方式 · 人工窗口挂号 · 自助机挂号 · 初诊 复诊",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking and Reading)",
             "A. Pair up; each student listens to one segment of a conversation and answers questions. Segment 1: 1. What happened to the woman’s son? 2. Is the mother familiar with the place? How do you know? 3. What suggestion does the second speaker give? 4. Which department should the mother register for? 5. What does the mother ask the second speaker to do for her? 6. What does the mother need to show the second speaker, and why? Segment 2: 1. How long does the mother have to wait? 2. What should the mother pay attention to? 3. What should the mother fill out? 4. What should she do on future visits? 5. What is her registration number? 6. What reminder is the mother given at the end? B. Exchange information with your partner in Chinese. C. Listen to the entire conversation and reorder the activities 1. 准备医保卡, 2. 买病历本, 3. 填病历本, 4. 挂号, 5. 预约 in the sequence you hear. D. Share your answers and read the script. (Audio, not included; my sequence from the flow chart: 预约 → 准备医保卡 → 挂号 → 买病历本 → 填病历本.)"),
        card("Activity 2 (Listening, Speaking and Reading)",
             "A. Listen to a dialog and mark each statement True or False: 1. 病人不知道在哪儿挂号。 2. 病人第一次来看病。 3. 病人已经打电话预约了。 4. 病人挂的是普通门诊内科。 5. 王大夫是医院最有名的专家。 6. 病人最近开始头疼。 7. 病人只有医保卡，没有病历卡。 8. 病人不需要在挂号窗口排队挂号。 B. Listen again and answer in detail: 1. How could the patient get his registration number from the self-service registration machine? List at least three details. 2. What payment methods does the self-service machine accept? C. Pair up and share. D. Read the script. (Audio, not included; the book prints no key.)"),
        card("Activity 3 (Reading, Speaking and Listening)",
             "Answer the following questions based on the information in the chart: 1. What is the information about? 2. How many ways are patients permitted to register and what are they? 3. When should patients make their appointment? 4. What registration methods were used when you visited the doctor?",
             tables=[CH]),
        card("Activity 4 (Reading, Writing, Speaking and Listening)",
             "A. Pair up and read the patient guide for a hospital in Taiwan at the link given (wd.vghtpe.gov.tw). You read Part 1 and your partner reads Part 2; write a summary of the part you read, including what the guide is about and what patients should and should not do (under the headings 初诊/初診 and 复诊/複診). B. In Chinese, exchange your information. C. What are the differences between the registration process in hospitals in Taiwan and in the U.S.? Share your thoughts with the class. (The linked guide is not included.)"),
        card("Activity 5 (Reading, Writing, Speaking and Listening)",
             "You want to understand the best way to register at a hospital in China, so you find the information below on a hospital’s website. A. Pair up; each student reads their own part, then notes the advantages in their partner’s part. B. Share your information and complete the table with your partner’s. C. Compare the information and decide which way you prefer; share your choice with the class. D. Learn three new Chinese words from the passages (my three: 自助, 缴费, 人工). Student 1 and Student 2:",
             tables=[ADV], examples=[D(*S1), D(*S2)]),
    ],
    exercises=[
        M("Where are the manual registration and payment windows?", "On floors 6 to 8 of the outpatient building", ["On the first floor only", "In the garden", "In the pharmacy"], "位于门诊六到八楼."),
        M("Who can register at the manual window on a first visit?", "Patients with an ID card", ["Only doctors", "Only children", "Nobody"], "带身份证的病人."),
        M("What can you do at the manual window?", "Fill in the info form, buy a record book or card, and register", ["Only pay", "Only collect medicine", "Only take a number"], "填写病历信息登记表，购买病历本或办理病历卡."),
        M("What can you use to collect a number if you booked online?", "Alipay or WeChat “collect number for appointment”", ["A letter", "A taxi", "A bank check"], "预约取号 功能."),
        M("Which payments does the self-service machine accept?", "Cash, Alipay, bank cards", ["Only coins", "Only stamps", "Nothing"], "现金、支付宝、银行卡."),
        M("How can a first-visit patient get a record card from the machine?", "With the second-generation ID card or Alipay face scan", ["With a phone call", "With a letter", "With a doctor’s note"], "二代身份证 / 支付宝刷脸."),
        M("How far ahead is a clinic-room (诊间) appointment made?", "One month", ["One day", "Ten days", "One year"], "医生诊间提前一个月预约."),
        M("How far ahead is a community health center appointment made?", "Ten days", ["One month", "One week", "One day"], "提前十天预约."),
        M("What word means “self-service”?", "自助", ["人工", "缴费", "预约"], "自助."),
        M("What word means “manual (by a person)”?", "人工", ["自助", "手机", "窗口"], "人工."),
        F("自助机可以用现金、支付宝、银行卡等方式___付。", "支", PART, "支付: pay."),
        F("网上提前预约好了，如何挂___？", "号", PART, "挂号: register."),
    ],
)

# ------------------------------------------------------------------ 7. using Chinese
PRC = table(["流程", "中国 (mine)", "美国 (mine)"],
            [["预约", "打电话、用手机或网上预约，也可以到医院的自助机预约", "打电话或上网预约"], ["挂号", "带身份证、医保卡到挂号窗口或自助机挂号，买病历本", "到诊所前台登记，出示保险卡"], ["看病", "在候诊室等护士叫号，叫到号就进去看病", "在候诊室等护士叫名字，然后看医生"], ["取药", "先划价、交费，然后去药房取药", "医生开药方，到药店取药"]],
            title="Activity 1B: the process in China and in the U.S. (the chart in the book is a picture, not included; the China column is from this lesson and the U.S. column is my general description)", say=[1, 2])
QQ = [("请问，挂号和预约最方便的办法是什么？", "1. Excuse me, what is the most convenient way to register and make an appointment? (mine)"), ("去医院的时候，我要带什么？", "2. What do I need to bring when I go to the hospital? (mine)"), ("我头疼，还有点发烧，应该挂哪一科？", "3. I have a headache and a bit of fever; which department should I register for? (mine)"),
      ("挂号需要填什么表？要不要买病历本？", "4. What forms do I need to fill in to register? Do I need to buy a record book? (mine)"), ("你们收不收外国人的医保卡？", "5. Do you accept foreigners’ medical insurance cards? (mine)"), ("可以用现金付钱，还是只能用手机付钱？", "6. Can I pay with cash, or only by phone? (mine)")]
L7 = lesson(
    "Lesson 21 Presentation 1 using Chinese in context: helping a friend see a doctor in Beijing",
    "北京大学的朋友生病了 · 中国和美国看病的流程 · 打电话问医院",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking)",
             "Scenario: while studying at Beijing University, one of your American friends became ill and had to go to a hospital in Beijing. You and your classmates need to research to help your friend make an appointment and register, and explain the similarities and differences between Chinese and U.S. procedures. A. During your research online you find a chart (a picture, not included). Work in pairs; one of you reads the part about China and the other the part about the U.S. B. Exchange information and, in Chinese characters or pinyin, take notes in the table (流程: 预约, 挂号, 看病, 取药). C. Based on your notes, write the similarities and differences (相同点 / 不同点). D. Share your result in the class. My table:",
             tables=[PRC]),
        card("Activity 2 (Writing, Speaking and Listening)",
             "Scenario: after learning the procedures of making an appointment and registering in a Chinese hospital, you and your classmates call the hospital where you will take your friend and want more information. A. Work in pairs and make a list of questions to ask, covering: 1. the most convenient way to book an appointment, 2. what to bring, 3. which department to register for, 4. paperwork, 5. insurance, 6. payment. B. Each pair calls the hospital (the teacher and two students play the patient-assistance worker) and writes down the answers. C. In a group of three share the information and decide how to handle the appointment and registration. D. After the discussion call the hospital again, make an appointment and register your friend. My six questions:",
             examples=[D(z, e) for z, e in QQ]),
    ],
    exercises=[
        M("Who needs help in the scenario?", "An American friend studying in Beijing", ["A teacher in Shanghai", "A doctor in Taipei", "A nurse in Chengdu"], "In Beijing."),
        M("What do you need to explain to your friend?", "The similarities and differences between Chinese and U.S. procedures", ["Only the price", "Only the food", "Only the map"], "similarities and differences."),
        M("Which four steps are in the process table?", "预约, 挂号, 看病, 取药", ["买票, 坐车, 下车, 付钱", "起床, 洗脸, 吃饭, 睡觉", "预习, 复习, 考试, 毕业"], "预约, 挂号, 看病, 取药."),
        M("Which question asks what to bring?", "去医院的时候，我要带什么？", ["可以用现金付钱吗？", "我应该挂哪一科？", "请问挂号处在哪儿？"], "我要带什么."),
        M("Which question asks about payment?", "可以用现金付钱，还是只能用手机付钱？", ["你们收不收外国人的医保卡？", "我头疼应该挂哪一科？", "挂号需要填什么表？"], "付钱 = pay."),
        M("Which question asks about insurance?", "你们收不收外国人的医保卡？", ["去医院的时候，我要带什么？", "挂号需要填什么表？", "可以用现金付钱吗？"], "医保卡."),
        F("我头疼，还有点发___，应该挂哪一科？", "烧", PART, "发烧: have a fever."),
        F("挂号需要填什么___？", "表", PART, "表: form."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 21 Presentation 1 vocabulary", "24 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第二十一课 Presentation 1: 在医院挂号, 应该, 别, 那么/这么", [L1, L2, L3, L4, L5, L6, L7, L8])
