"""Unit 74: Lesson 24 (Unit 4 review), the using-Chinese-in-context review from the book's texts: the Xi'an trip by plane or train with the teacher's
script, the role-plays at the post office and the hospital, the "I say, you draw" directions activity and Peter's email from Chengdu. Audio and pictures
are not included; numbers the book writes as digits are spelled out; the tables and answers that the book leaves blank are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('还是', 0, 'hai2'), ('还有', 0, 'hai2'), ('得改', 0, 'dei3'), ('教书', 0, 'jiao1'), ('乐山', 0, 'le4'), ('长江', 0, 'chang2'), ('我得改', 1, 'dei3'), ('得多', 0, 'de5'), ('填得', 1, 'de5'), ('彼得', 1, 'de2')):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特两圣" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. activity 1: plane or train to Xi'an
TS = ("同学们，下个月，我们班要去西安实习，体验中国历史和文化。我想让你们决定我们是坐高铁去还是坐飞机去。从北京到西安，如果坐高铁去，最快要四个半小时。商务座票价是人民币一千六百二十八元左右，一等座是八百二十五元，二等座是五百一十五元。如果坐飞机去，两个多小时就到了，票价是人民币一千五百元左右。请你们比较一下，坐哪一种交通工具对你们来说更好。你们讨论好了以后告诉我。谢谢。",
      "Classmates, next month our class is going to Xi’an for an internship, to experience Chinese history and culture. I want you to decide whether we go by high-speed train or by plane. From Beijing to Xi’an, by high-speed train it takes four and a half hours at the fastest. A business-class ticket is about 1,628 yuan, first class is 825 yuan and second class is 515 yuan. By plane it takes just over two hours and the ticket is about 1,500 yuan. Please compare, and decide which means of transport is better for you. Tell me once you have discussed it. Thank you. (the book writes the prices in digits and, in its first sentence, 我想让决定我们是…, with 你们 missing, which I added; translation mine)")
TA1 = table(["从北京到西安", "需要的时间", "票价"], [["高铁 商务座", "最快四个半小时", "人民币一千六百二十八元左右"], ["高铁 一等座", "最快四个半小时", "八百二十五元"], ["高铁 二等座", "最快四个半小时", "五百一十五元"], ["飞机", "两个多小时", "人民币一千五百元左右"]],
            title="Activity 1A: the table (the book leaves it blank; filled from the script)", say=[0, 1, 2])
TA2 = table(["", "优点", "缺点", "最后的决定"], [["坐飞机", "时间短，两个多小时就到了", "要去机场，托运行李，过安检；票价不便宜", "坐高铁"], ["坐高铁", "车站在市区，可以看风景，二等座比飞机便宜", "时间比飞机长", "坐高铁"]],
            title="Activity 1C: advantages, disadvantages and the decision (the book leaves it blank; this is one possible answer, mine)", say=[1, 2, 3])
L1 = lesson(
    "Lesson 24 Using Chinese in Context Review: a class trip to Xi’an, by plane or by train?",
    "去西安实习 · 高铁还是飞机 · 商务座 一等座 二等座 · 优点 缺点 · 最后的决定",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing and Speaking)",
             "Scenario: You are studying Chinese at a university in Beijing. Your class is going to take a field trip to Xi’an next month. Your teacher asks you to decide whether your class should take a plane or a high-speed train to get to Xi’an from Beijing. You need to compare these two types of transportation to make a final decision, and then report your decision to your teacher. A. Listen to the teacher’s information and fill in the table. B. Pair up and check the details of what you hear with your partner. Read the script if needed. C. With your partner, discuss the advantages and disadvantages of flying vs. travelling by high-speed rail. Consider the following details in your comparisons: 1. 时间 2. 票价 3. 买票和取票是不是很方便 4. 去机场和高铁站哪个更方便 5. 行李托运 6. 飞机和高铁的服务怎样 7. 自己是不是有足够的钱 8. 怎么付费 9. 可不可以看风景 10. 其它方面. D. Present your decision to the class and explain your reasoning. (Audio and two pictures, not included.)",
             tables=[TA1, TA2]),
        card("Script: the teacher’s information", "The prices are spelled out in characters.", examples=[D(*TS)]),
    ],
    exercises=[
        M("Where is the class going next month?", "Xi’an", ["Shanghai", "Chengdu", "Guangzhou"], "去西安实习."),
        M("What is the purpose of the trip?", "To experience Chinese history and culture", ["To shop", "To ski", "To visit relatives"], "体验中国历史和文化."),
        M("How long does the high-speed train take at the fastest?", "Four and a half hours", ["Two hours", "Eight hours", "One day"], "最快要四个半小时."),
        M("How much is a business-class ticket?", "About 1,628 yuan", ["About 825 yuan", "About 515 yuan", "About 1,500 yuan"], "一千六百二十八元左右."),
        M("How much is a first-class ticket?", "825 yuan", ["515 yuan", "1,628 yuan", "1,500 yuan"], "八百二十五元."),
        M("How much is a second-class ticket?", "515 yuan", ["825 yuan", "1,628 yuan", "1,500 yuan"], "五百一十五元."),
        M("How long does the flight take?", "A little over two hours", ["Four and a half hours", "Ten minutes", "A whole day"], "两个多小时."),
        M("How much is the plane ticket?", "About 1,500 yuan", ["About 515 yuan", "About 825 yuan", "About 3,000 yuan"], "一千五百元左右."),
        M("What does the teacher ask the students to do?", "Compare and decide, then tell him", ["Buy tickets", "Write a report", "Make a video"], "你们讨论好了以后告诉我."),
        M("Which is cheaper in the script?", "A second-class train ticket", ["A business-class ticket", "The plane ticket", "They cost the same"], "二等座五百一十五元."),
        F("我想让你们决定我们是坐高铁去___是坐飞机去。", "还", ["再", "就", "又"], "是…还是…."),
        F("商务座票价是人民币一千六百二十八元___右。", "左", ["上", "下", "前"], "左右: about."),
    ],
)

# ------------------------------------------------------------------ 2. activities 2 and 3: role-plays
RU = table(["你想知道的信息"], [["我想寄一个包裹到美国，您能告诉我怎么寄吗？"], ["普通航空包裹、海运和特快专递哪个快？"], ["多长时间会寄到？"], ["寄到美国要多少钱？"], ["保险费是多少？"], ["你看我填得对不对？"], ["你们收信用卡，现金和支付宝吗？"], ["我怎么知道包裹什么时候寄到？"], ["其它要问的问题"]],
           title="Activity 2A: the information you want to know (Student 1)", say=[0])
RC = table(["邮局营业员"], [["这个包裹你要寄到美国哪里？"], ["你想怎么寄？普通航空包裹，海运还是特快专递？"], ["你的包裹里有什么？有没有液体和易碎、易燃物品？"], ["你要不要买保险？"], ["你需要填一下包裹单和海关申报单。"], ["你怎么付费？"], ["收据上有二维码，扫一下就知道了。"], ["其它要问的问题"]],
           title="Activity 2A: the postal clerk’s side (Student 2)", say=[0])
HP = table(["病人"], [["我第一次来看病，您能告诉我该怎么做吗？"], ["在哪儿挂号？"], ["你们都有什么科？"], ["普通门诊还是专家门诊有什么不同？"], ["在哪儿买病历卡？"], ["在哪儿取药和付费？"], ["其它要问的问题"]],
           title="Activity 3A: the patient’s side (Student 1; the book writes 病例卡, which I wrote as 病历卡)", say=[0])
HS = table(["医院工作人员"], [["你有预约吗？"], ["你带身份证了吗？"], ["你要挂哪一科？"], ["你有什么症状？"], ["你想挂普通门诊还是专家门诊？"], ["你用什么付钱？"], ["其它要问的问题"]],
           title="Activity 3A: the hospital assistant’s side (Student 2)", say=[0])
L2 = lesson(
    "Lesson 24 Using Chinese in Context Review: role-plays at the post office and the hospital",
    "寄包裹到美国 · 普通航空包裹 海运 特快专递 · 第一次来看病 · 挂号 · 普通门诊 专家门诊",
    requires=[],
    cards=[
        card("Activity 2 (Reading and Speaking)",
             "Scenario: You are studying Chinese at a university in Shanghai. Your mother’s birthday is coming up, and you’d like to mail her a birthday gift. Go to the post office to inquire about shipping methods, and then send the gift. Your partner will play the role of postal clerk. A. Role-play: Student 1 is sending a gift to their mother. Student 2 plays the role of postal clerk. Use the information below as reference. B. Swap roles with your partner and hold the conversation again. (Three pictures are not included.)",
             tables=[RU, RC]),
        card("Activity 3 (Reading and Speaking)",
             "Scenario: You have been studying Chinese in Beijing University for about three months. You feel very ill today and go to the hospital to see a doctor. Since you are a first-time patient at a Chinese hospital, you ask several questions about hospital procedures. A. Role-Play: Student 1 plays the role of the patient, and Student 2 plays the role of the hospital assistant. Use the information below as reference. B. Swap roles with your partner and hold the conversation again. (Three pictures are not included.)",
             tables=[HP, HS]),
    ],
    exercises=[
        M("Which question asks about the speed of three mailing methods?", "普通航空包裹、海运和特快专递哪个快？", ["寄到美国要多少钱？", "保险费是多少？", "你怎么付费？"], "Speed."),
        M("Which question asks about the price?", "寄到美国要多少钱？", ["多长时间会寄到？", "你要不要买保险？", "你想怎么寄？"], "多少钱: how much."),
        M("Which does the clerk ask about the contents?", "有没有液体和易碎、易燃物品？", ["你要寄到哪里？", "你怎么付费？", "你要不要买保险？"], "易碎、易燃: fragile, flammable."),
        M("Which forms does the clerk say to fill in?", "包裹单和海关申报单", ["病历卡和身份证", "保险单和收据", "挂号单"], "包裹单和海关申报单."),
        M("What is on the receipt?", "A QR code", ["A signature", "A photo", "A stamp"], "收据上有二维码."),
        M("Which question is asked by the hospital assistant?", "你有预约吗？", ["在哪儿挂号？", "你们都有什么科？", "在哪儿取药？"], "The assistant’s side."),
        M("Which question is asked by the patient?", "在哪儿挂号？", ["你有预约吗？", "你带身份证了吗？", "你有什么症状？"], "The patient’s side."),
        M("What does the assistant ask the patient to bring?", "身份证", ["保险", "钥匙", "手机"], "你带身份证了吗？"),
        M("What does the patient want to know about 普通门诊 and 专家门诊?", "The difference", ["The price only", "The doctor’s name", "The address"], "有什么不同."),
        M("How does the assistant ask about payment?", "你用什么付钱？", ["你有预约吗？", "你要挂哪一科？", "你有什么症状？"], "付钱: pay."),
        F("你想怎么寄？普通航空包裹，海运___是特快专递？", "还", ["再", "就", "也"], "还是: or."),
        F("你需要填一下包裹单和海关申___单。", "报", ["表", "单", "告"], "申报单: declaration form."),
    ],
)

# ------------------------------------------------------------------ 3. activities 4 and 5: directions and the email
DIR = table(["The book’s template (with the brackets)", "一句话 (my sample)"], [["1. 从……(学校大门)出发", "从学校大门出发"], ["2. 沿着……大街一直往前走", "沿着第一大街一直往前走"], ["3. 过了……个红绿灯(停车牌)，", "过了三个红绿灯，"], ["4. 在十字路口(丁字路口)往左(右)拐", "在十字路口往左拐"], ["5. 上(下)高速公路", "上高速公路"], ["6. 过了两个街区(block)", "过了两个街区"], ["7. 继续往前走，走到底", "继续往前走，走到底"], ["8. 再走五分钟就到了", "再走五分钟就到了"], ["9. 你会看到……", "你会看到一家咖啡店"], ["10. 水族馆就在你的左手边(右手边)", "水族馆就在你的右手边"]],
           title="Activity 4A: the ten phrases for “我说你画” (the book’s English word “block” is for 街区; the right-hand column is my sample)", say=[1])
DS = ("从学校大门出发，沿着第一大街一直往前走，过了三个红绿灯，在十字路口往左拐。过了两个街区，继续往前走，走到底，再走五分钟就到了。你会看到一家咖啡店，水族馆就在你的右手边。",
      "Leave from the school gate and go straight along First Street; pass three traffic lights and turn left at the intersection. After two blocks, keep going to the end, and five more minutes and you are there. You will see a coffee shop, and the aquarium is on your right. (a sample route; the book gives only the ten phrases; mine)")
EM = ("杰克，你好，好久不见，希望你一切都好！我来成都教书已经半年了，我非常喜欢这里。成都不仅气候好，而且风景也美。这里的老师和学生对我特别友好。我每天给学生上两节英语课，下课以后我得改作业，备课。其他时间我自己学习中文。下班以后，我有时候和同事一起出去吃饭。成都有各种各样的餐馆，不过，大部分餐馆的菜都很辣。昨天晚上我和同事一起去吃饭，我们吃了麻婆豆腐和辣子鸡。如果你来成都，我请你吃麻辣火锅，你一定喜欢吃。",
      "Email, paragraph 1: Hello Jack, long time no see; I hope everything is fine with you! I have been teaching in Chengdu for half a year now and I like it here very much. Chengdu not only has a good climate but also beautiful scenery. The teachers and students here are especially friendly to me. Every day I teach two English classes, and after class I have to grade homework and prepare lessons. In my other time I study Chinese myself. After work I sometimes go out to eat with colleagues. Chengdu has all kinds of restaurants, but most of the restaurants’ dishes are very spicy. Last night I went out to eat with colleagues and we had mapo tofu and spicy chicken. If you come to Chengdu I will treat you to spicy hot pot; you will certainly like it. (translations in this card are mine)")
EM2 = ("周末的时候，我常常去成都一些有名的地方去逛逛。上个周末我去了成都大熊猫基地。那里的熊猫太可爱了。下个星期我打算去看乐山大佛。那个大佛在长江旁边，有七十一米高，脚上可以坐一百多个人。到时候，我给你发一些照片。你的中文学习怎么样了？有空儿给我讲讲你那里的学习和生活。谢谢。彼得",
       "Paragraph 2: On weekends I often go to look around some famous places in Chengdu. Last weekend I went to the Chengdu Giant Panda Base. The pandas there are so cute. Next week I plan to see the Leshan Giant Buddha. That Buddha is beside the Yangtze River, is 71 meters tall, and more than a hundred people can sit on its feet. By then I will send you some photos. How is your Chinese study going? When you have time, tell me about your studies and life where you are. Thanks. Peter (the book writes 71 in digits and, after 熊猫 and 乐山大佛, glosses them in pinyin and English in a vocabulary note; the book’s river name is kept as printed)")
AQ = [("彼得每天上班做什么？", "1. (the book asks about 杰克, but the email is written by 彼得 to 杰克) He teaches two English classes a day, then grades homework and prepares lessons; the rest of the time he studies Chinese. (my answer)"),
      ("彼得下班以后去哪儿吃饭？昨天晚上吃的什么菜？", "2. After work he sometimes eats out with colleagues; last night they had mapo tofu and spicy chicken. (my answer)"),
      ("周末的时候，彼得喜欢做什么？上个周末他去哪儿了？", "3. On weekends he likes to visit famous places in Chengdu; last weekend he went to the Chengdu Giant Panda Base. (my answer)"),
      ("下个星期，他想去看什么？他为什么要去那个地方？", "4. Next week he wants to see the Leshan Giant Buddha, because it is famous and huge: 71 meters tall, with room for over a hundred people on its feet; he will send photos. (my answer)")]
L3 = lesson(
    "Lesson 24 Using Chinese in Context Review: giving directions and Peter’s email from Chengdu",
    "我说你画 · 沿着大街一直往前走 · 水族馆 · 彼得在成都教书 · 大熊猫基地 · 乐山大佛",
    requires=[],
    cards=[
        card("Activity 4 (Reading, Listening, Writing and Speaking)",
             "Scenario: Your Chinese friend comes to visit you and he wants to visit the Monterey Bay Aquarium. Since you must go to school and have no time to go with your friend, you will give him/her clear directions on how to get to the Aquarium, either from your house or from your school. When you give directions, your friend will draw a simple map based on your descriptions. Your partner will play the role of your Chinese friend. A. Pair up. Student 1 gives directions to Student 2 on how to get to the Aquarium. Student 2 will draw a simple map in their workbook using Student 1’s descriptions. Use the words and phrases below for your directions (我说你画). B. Check your partner’s drawing and verify the directions. C. Now Student 2 gives directions to Student 1 on how to get to the Aquarium. Student 1 will draw a simple map in their workbook. Check the drawing against the directions upon completion. (Pictures not included.)",
             tables=[DIR],
             examples=[D(*DS)]),
        card("Activity 5 (Listening, Writing, Reading and Speaking)",
             "Scenario: Your college classmate is currently teaching English in China. He recently emailed you about his life and work in China. You will email him back to tell him about your life and studies. A. Listen to your friend’s email and answer the questions. New words: 熊猫 (panda) and 乐山大佛 (Leshan Giant Buddha); the book gives their pinyin in brackets, which I left out. The questions: 1. 杰克每天上班做什么？ 2. 下班以后，杰克去哪儿吃饭？昨天晚上吃的什么菜？ 3. 周末的时候，杰克喜欢做什么？上个周末他去哪儿了？ 4. 下个星期，他想去看什么？他为什么要去那个地方？ B. Pair up, discuss your answers with your partner. Read the script if necessary. C. Pair up, write an email to Jack about your life and studies in Monterey (TO, CC, Subject). The script:",
             examples=[D(*EM), D(*EM2)]),
        card("Activity 5A: my answers", "The book asks the four questions about 杰克, but the email is written by 彼得; the questions below name 彼得 (the writer) and the answers are mine.", examples=[D(z, e) for z, e in AQ]),
    ],
    exercises=[
        M("Who wrote the email?", "Peter, who teaches English in Chengdu", ["Jack, who studies in Monterey", "A tour guide", "A doctor"], "彼得."),
        M("How long has Peter been in Chengdu?", "Half a year", ["Two weeks", "Five years", "One day"], "已经半年了."),
        M("What is Chengdu like, according to Peter?", "Good climate and beautiful scenery", ["Cold and dry", "Very noisy", "Very small"], "气候好，而且风景也美."),
        M("How many English classes does he teach a day?", "Two", ["One", "Four", "Six"], "每天给学生上两节英语课."),
        M("What does he do after class?", "Grade homework and prepare lessons", ["Play football", "Go to the market", "Sleep"], "改作业，备课."),
        M("What did he eat last night?", "Mapo tofu and spicy chicken", ["Hot pot and fish", "Dumplings and noodles", "Roast duck"], "麻婆豆腐和辣子鸡."),
        M("Where did he go last weekend?", "The Chengdu Giant Panda Base", ["The Leshan Giant Buddha", "Beijing", "A museum"], "成都大熊猫基地."),
        M("What does he plan to see next week?", "The Leshan Giant Buddha", ["The Great Wall", "The Terracotta Army", "A hot pot restaurant"], "乐山大佛."),
        M("How tall is the Buddha?", "71 meters", ["17 meters", "100 meters", "7 meters"], "七十一米高."),
        M("What will he send Jack?", "Some photos", ["A book", "Tea", "A map"], "我给你发一些照片."),
        M("Which phrase means “keep going to the end”?", "走到底", ["走到头 (wrong)", "往后走", "停下来"], "走到底."),
        F("如果你来成都，我请你吃麻辣火___。", "锅", ["饭", "菜", "汤"], "火锅: hot pot."),
        F("水族馆就在你的右手___。", "边", ["面", "头", "里"], "右手边: on your right."),
    ],
)

UNIT = unit("第二十四课 Unit 4 review: using Chinese in context review", [L1, L2, L3])
