"""Unit 54: Lesson 19 (Travel by High-Speed Rail) Presentation 1 from the book's texts: the father-and-son dialog about riding the high-speed
rail home for the Mid-Autumn Festival, the adverb 早(就), the prepositions 为 and 给, the adverb 反正, the skill-integration activities
(the conductor's announcement, the high-speed rail passage), the using-Chinese activities (Wang Gang's trip planning, the provincial high-speed
rail table) and the vocabulary list. Audio, pictures, links and the student's own writing blanks are not included; numbers the book writes
as digits are spelled out in the Chinese text here; answer keys the book does not print (and sentences whose blanks were lost) are mine
and labeled."""
from zh_auto import *
from zh_l19_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("列车长", 2, "zhang3"), ("贵不了", 2, "liao3"), ("参军", 0, "can1"), ("没有", 0, "mei2"), ("没问题", 0, "mei2"), ("没那么", 0, "mei2"), ("没什么", 0, "mei2"), ("没想好", 0, "mei2"),
                          ("没买", 0, "mei2"), ("没去", 0, "mei2"), ("没洗", 0, "mei2"), ("没做", 0, "mei2"), ("还没", 1, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("长大", 0, "zhang3"),
                          ("得好好", 0, "dei3"), ("多得", 1, "de5"), ("教练", 0, "jiao4"), ("觉得买", 1, "de5"), ("下得有", 1, "de5")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "di4" if (zh[j - 1] in "当草土天各山场内本外基实陆特" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P1 = [("儿子", "爸，中秋节快到了，我们公司放长假，我陪您回老家看看吧。", "Dad, the Mid-Autumn Festival is coming and my company has a long holiday; let me go back to your hometown with you."), ("爸爸", "好啊，我们坐火车还是坐飞机？", "Good. Shall we take the train or fly?"),
      ("儿子", "坐高铁吧。虽然坐飞机快一些，但是加上去机场和安检的时间，和坐高铁差不多。", "Let’s take the high-speed rail. Although flying is a bit faster, once you add the time to get to the airport and the security check, it is about the same as the high-speed rail."), ("爸爸", "行，高铁站就在市区，也很方便。我早就想坐坐了。高铁也有硬卧、软卧什么的吗？", "OK. The high-speed rail station is right in the city, which is convenient too. I’ve wanted to ride it for a long time. Does the high-speed rail also have hard sleepers, soft sleepers and so on?"),
      ("儿子", "有些有，不过我们坐的这条线只有一等座、二等座，还有商务座和特等座。", "Some do, but the line we’re taking only has first-class seats, second-class seats, and also business-class and special-class seats."), ("爸爸", "票价是多少？", "How much is the fare?"),
      ("儿子", "商务座和特等座稍微贵一点儿。一等座八百零六，二等座五百二。咱们买一等的吧。", "Business and special class are slightly more expensive. First class is 806 and second class is 520. Let’s buy first class."), ("爸爸", "我看，坐二等的就可以了。反正时间短，一等、二等都差不多。", "I think second class is fine. The trip is short anyway, so first and second class are about the same."),
      ("儿子", "那就听您的。到时候，我带您到餐车好好吃一顿。", "Then we’ll do as you say. When the time comes I’ll take you to the dining car for a good meal."), ("爸爸", "太好了，我当兵的时候，就爱吃火车上的饭菜。", "Great. When I was a soldier I loved the food on trains."),
      ("儿子", "现在高铁上的饭菜可比您那个时候好多了，而且每隔一段时间还有售货车为您提供各种饮料和零食。", "The food on the high-speed rail now is much better than in your day, and every so often a sales cart offers you all kinds of drinks and snacks."), ("爸爸", "我不喜欢喝饮料，他们有没有热茶？", "I don’t like drinks; do they have hot tea?"),
      ("儿子", "没问题，每节车厢都有热水器，可以泡茶。", "No problem; every carriage has a water heater, so you can make tea."), ("爸爸", "看来高铁就是不一样啊。", "It seems the high-speed rail really is different."),
      ("儿子", "而且，高铁的窗户特别大，您还可以好好地看一下沿途的风景和变化。", "And the windows on the high-speed rail are very big, so you can also take a good look at the scenery and the changes along the way.")]
L1 = lesson(
    "Lesson 19 Presentation 1: going home by high-speed rail",
    "中秋节放长假 · 高铁还是飞机 · 一等座二等座 · 餐车和热茶",
    requires=[],
    cards=[
        card("Learning objectives (Lesson 19, Travel by High-Speed Rail, 坐高铁旅行)",
             "Unit 4 is Survival Skills and Social Factors. In this lesson you will obtain information and describe a plan for a train ride in China, a ride on China’s high-speed rail, and the services of China’s high-speed rail system. To do so you must master the new words and phrases, the adverb 早(就), the prepositions 为 and 给, the adverb 反正, more about the use of 次, the adverb 根本, the adverb 一定, the modal verb 会, 等 expressing when, the noun 最近, the adverb 才, the prepositions 向, 往 and 对, and the conjunction 由于. The Area Studies topic is China’s transportation system."),
        card("Getting Started",
             "Photograph: a train (not included). Pair up and discuss with your partner: A. Under what circumstances would you travel by train in the U.S.? B. What is your opinion of Amtrak’s services?"),
        card("Presentation 1: 坐高铁回老家",
             "The book also prints the dialog in traditional characters. The fares are read as numbers (806 is 八百零六, 520 is read 五百二).",
             examples=dlg(P1)),
    ],
    exercises=[
        M("What festival is coming?", "The Mid-Autumn Festival", ["The Spring Festival", "The Dragon Boat Festival", "National Day"], "中秋节快到了."),
        M("Why does the son offer to go home with his father?", "His company has a long holiday", ["He lost his job", "His father is sick", "He wants to move"], "我们公司放长假."),
        M("Why does the son suggest the high-speed rail?", "With airport and security time added, flying takes about as long", ["Planes are not allowed", "It is free", "The airport is closed"], "加上去机场和安检的时间，和坐高铁差不多."),
        M("Where is the high-speed rail station?", "In the city", ["Far in the suburbs", "At the airport", "Beside the home town"], "高铁站就在市区."),
        M("Which seats does their line have?", "First, second, business and special class", ["Only hard sleepers", "Soft sleepers and hard sleepers", "Only standing room"], "一等座、二等座，还有商务座和特等座."),
        M("How much is a first-class seat?", "Eight hundred and six", ["Five hundred and twenty", "Eight hundred and sixty", "Six hundred and eight"], "一等座八百零六."),
        M("Which class does the father choose?", "Second class", ["First class", "Business class", "Special class"], "坐二等的就可以了."),
        M("Why does the father say second class is fine?", "The trip is short anyway", ["He is poor", "He likes standing", "First class is full"], "反正时间短."),
        M("What did the father like when he was a soldier?", "The food on the train", ["The seats", "The windows", "The tickets"], "我当兵的时候，就爱吃火车上的饭菜."),
        M("What does the father want to drink?", "Hot tea", ["Cola", "Juice", "Coffee"], "他们有没有热茶？"),
        M("How can he make tea on the train?", "Each carriage has a water heater", ["The conductor brings a kettle", "He brings a thermos", "There is a tea shop"], "每节车厢都有热水器，可以泡茶."),
        M("What does the son say about the windows?", "They are very big, good for seeing the scenery", ["They cannot be opened", "They are tinted dark", "They are very small"], "窗户特别大."),
        F("每节车___都有热水器，可以泡茶。", "厢", PART, "车厢: carriage."),
        F("高铁站就在市___，也很方便。", "区", PART, "市区: urban area."),
        F("商务座和特等座___微贵一点儿。", "稍", PART, "稍微: slightly."),
    ],
)

# ------------------------------------------------------------------ 2. Activities 1-4
SENT2 = [("虽然坐商务座贵一些，可是舒服多了。反正有您儿子给您买车票，别担心。", "1. Although the business-class seat costs a little more, it is much more comfortable. Anyway your son is buying you the ticket, so don’t worry. (商务座, 反正; the blanks were lost in the text, so this key is mine)"), ("甲：看来坐软卧和坐硬卧就是不一样啊！乙：是啊。我早就要你买软卧票，可你就是不买。", "2. A: It seems a soft sleeper really is different from a hard sleeper! B: Yes. I told you long ago to buy a soft-sleeper ticket, but you just wouldn’t. (硬卧, 早就, 就是; mine)"),
         ("甲：我看你还是买靠窗的座位好，可以好好地看看沿途的风景。乙：好，听你的。", "3. A: I think you’d better buy a window seat, so you can take a good look at the scenery along the way. B: OK, I’ll do as you say. (我看, 好好地, 沿途, 听你的; mine)"), ("现在火车上为旅客提供的服务比以前多多了，也好多了。", "4. The services the train provides for passengers now are far more numerous than before, and much better too. (提供, 多多了; mine)"),
         ("现在去青岛的高铁每隔两个小时就有一趟。放假后我陪您去那儿玩儿玩儿吧。", "5. Now the high-speed rail to Qingdao has one train every two hours. After the holiday I’ll go there with you for some fun. (隔, 趟, 放假; mine)")]
MATCH = [("虽然坐高铁快一些，可是加上去车站和等车的时间，和自己开车也差不多了。", "1 + d. Although the high-speed rail is a bit faster, adding the time to get to the station and wait for the train, it is about the same as driving yourself. (key mine)"), ("咱们坐高铁回老家吧，车站就在市区。坐高铁比您那个时候坐火车可舒服多了。", "2 + f. Let’s take the high-speed rail home; the station is right in the city. The high-speed rail is much more comfortable than the train in your day. (mine)"),
         ("要是你想好好地看看沿途的风景和变化，最好坐高铁。别的火车窗户太小，看不清楚。", "3 + a. If you want a good look at the scenery and changes along the way, it’s best to take the high-speed rail. The windows on other trains are too small to see clearly. (mine)"), ("你坐的那条线，除了一等座和二等座，有没有商务座和特等座？", "4 + g. On the line you’re taking, besides first and second class, are there business and special class seats? (mine)"),
         ("反正到北京还有两小时，我带您到餐车好好地吃一顿，怎么样？", "5 + b. There are two hours left to Beijing anyway; how about I take you to the dining car for a good meal? (mine)"), ("虽然车票贵了不少，可是躺着多舒服呀。软卧就是不一样！", "6 + c. Although the ticket costs quite a bit more, how comfortable it is lying down. A soft sleeper really is different! (mine; the book prints 贵不了不少)"),
         ("坐高铁很贵，咱们坐一般的快车就行了，就是慢一点儿，没关系。", "7 + e. The high-speed rail is expensive; an ordinary fast train will do, it’s only a bit slower, no problem. (mine)")]
TAB2 = table(["坐高铁的理由", "高铁设施", "高铁票价", "高铁服务"],
             [["中秋节放长假，陪爸爸回老家；加上去机场和安检的时间，和坐飞机差不多；高铁站就在市区", "窗户特别大，每节车厢都有热水器，有餐车", "一等座八百零六，二等座五百二，商务座和特等座稍微贵一点儿", "售货车提供各种饮料和零食，有热茶，饭菜比以前好多了"]],
             title="Activity 2 A: expressions about riding the high-speed rail (the book leaves the table blank; this is my fill from the dialog)", say=[0, 1, 2, 3])
L2 = lesson(
    "Lesson 19 Presentation 1 activities: 坐高铁的理由, completing and matching",
    "Activities 1 to 4 · 趟 我看 提供 反正 硬卧 商务座 多多了 · 配对",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: listen to Presentation 1 and write answers: 1. Did the son make a considerate travel plan for his father? How do you know? 2. On what issue did the father and son not quite agree initially? B. Detailed listening: 1. What prompted the speakers to travel? 2. What was the father’s opinion about choosing the class of seating? 3. What did the father like to eat and drink? 4. How was the food on a high-speed train? 5. Why did the son mention the windows on the train? (Audio not included.) My answers from the dialog: yes, the son compared plane and train times, looked at the seat classes, the fares, the food, the tea and the windows; they first disagreed about first or second class; the long holiday for the Mid-Autumn Festival; second class is enough because the trip is short; train meals and hot tea; far better than before; so the father can enjoy the scenery and changes along the way."),
        card("Activity 2 (Reading, Speaking and Writing)",
             "A. Pair up and think about expressions related to riding a train in Presentation 1 and write them in the table. B. With your partner, use the expressions 趟, 我看, 提供, 反正, 硬卧, 商务座, 多多了, 隔, 早就, 放假, 就是, 沿途, 好好地 and 听你的 to correctly complete the five sentences. The printed sentences lost their blanks in the text, so the completed sentences below are my reconstruction.",
             tables=[TAB2], examples=[D(z, e) for z, e in SENT2]),
        card("Activity 3 (Reading and Speaking)",
             "A. Match the parts in Column A with the parts in Column B by writing the letters in the middle column; then share your work with a classmate. B. Check each other’s work: Student A translates the sentences into English and Student B translates them back into Chinese without looking at the table. Column B: a. 最好坐高铁。别的火车窗户太小，看不清楚。 b. 我带您到餐车好好地吃一顿，怎么样？ c. 软卧就是不一样！ d. 和自己开车也差不多了。 e. 就是慢一点儿，没关系。 f. 坐高铁比您那个时候坐火车可舒服多了。 g. 商务座和特等座？ The book prints no key; my matched sentences:",
             examples=[D(z, e) for z, e in MATCH]),
        card("Activity 4 (Listening, Writing, Speaking and Reading)",
             "A. Listen to an email message and answer in Chinese: 1. 马中民在电子邮件里主要说什么？ 2. 以前王忠怎么去远的地方？ B. Listen again for details and fill in the table 坐飞机和坐高铁的不同 (时间, 票价, 服务). C. Share your work with a classmate, then check your partner’s work against the script. (Audio only, not included; the book does not print the script.)"),
    ],
    exercises=[
        M("In the matching, which line completes “虽然坐高铁快一些，可是加上去车站和等车的时间”?", "和自己开车也差不多了", ["软卧就是不一样！", "就是慢一点儿，没关系", "商务座和特等座？"], "Key 1 + d."),
        M("Which line goes with “你坐的那条线，除了一等座和二等座，有没有”?", "商务座和特等座？", ["软卧就是不一样！", "和自己开车也差不多了", "我带您到餐车好好地吃一顿"], "Key 4 + g."),
        M("Which line goes with “虽然车票贵了不少，可是躺着多舒服呀”?", "软卧就是不一样！", ["商务座和特等座？", "最好坐高铁", "就是慢一点儿，没关系"], "Key 6 + c."),
        M("Which expression fills “看来坐软卧和坐___就是不一样啊！”?", "硬卧", ["商务座", "沿途", "放假"], "硬卧: hard sleeper."),
        M("Which word means “every (time interval)” in “现在去青岛的高铁每___两个小时就有一趟”?", "隔", ["早", "段", "站"], "每隔: every other."),
        M("Which expression means “I’ll do as you say”?", "听你的", ["我看", "反正", "沿途"], "听你的."),
        M("What does 好好地看看沿途的风景 mean?", "Take a good look at the scenery along the way", ["Look for the station", "Photograph the train", "Wait for the scenery"], "好好地: properly; 沿途: along the way."),
        M("What is 放假?", "To have a holiday or vacation", ["To go to work", "To stop a train", "To buy a ticket"], "放假."),
        F("要是你想好好地看看___途的风景和变化，最好坐高铁。", "沿", PART, "沿途: along the way."),
        F("现在火车上为旅客___供的服务比以前好多了。", "提", PART, "提供: provide."),
    ],
)

# ------------------------------------------------------------------ 3. 早就
Z1 = [("他早来了。", "He came early (he has already been here a while)."), ("我早听说中国的高铁了。", "I heard about China’s high-speed rail long ago.")]
Z2 = [("我早就做完作业了。", "1. I finished my homework long ago."), ("那儿的天气早就很热了。", "2. The weather there got hot long ago."), ("去青岛的高铁早就发车了，你怎么还在这儿等呢？", "3. The high-speed train to Qingdao left long ago; why are you still waiting here? (the book prints 你这么还在)"), ("我早就想请你来看看我们的新房子了。", "4. I’ve wanted to invite you to see our new house for a long time."),
      ("甲：你哥哥早就去北京上大学了吧？乙：他去得没那么早，今年刚上二年级。", "5. A: Your older brother went to Beijing for college long ago, didn’t he? B: He didn’t go that early; he’s only in his second year this year."), ("甲：你早就搬到加州来住了吧？乙：没那么早，去年刚过来。", "6. A: You moved to California to live long ago, didn’t you? B: Not that early; I just came last year.")]
ZA1 = [("甲：你去过长城吗？乙：我早就去过了，我去的时候，你还是个小孩子呢。", "1. A: Have you been to the Great Wall? B: I went long ago; when I went you were still a little kid. (the book prints the second half; the rest is mine)"), ("甲：你的听力作业做完了吗？乙：早就做完了。我是昨天晚上做完的。", "2. A: Have you finished your listening homework? B: Long ago. I finished it last night. (mine)"),
       ("甲：我早就告诉你要买机票了，你怎么还没买？乙：我一直在忙啊！", "3. A: I told you long ago to buy the plane ticket; why haven’t you bought it yet? B: I’ve been busy all along! (mine)"), ("甲：你哥哥早就大学毕业了吧？乙：他大学毕业是去年才大学毕业的，没那么早。", "4. A: Your older brother graduated from college long ago, didn’t he? B: He only graduated from college last year; not that early. (the book prints B; A is mine)"),
       ("甲：锻炼完身体以后，咱们把衣服洗洗吧。乙：我早就洗好了。", "5. A: After we work out, let’s wash our clothes. B: I washed them long ago. (mine)")]
ZA2 = [("今天我早就起床了，因为我要坐九点的飞机去华盛顿。", "1. Today I got up early, because I’m taking the nine o’clock plane to Washington. (revised with 早就; mine)"), ("他早就告诉过我了。", "2. He told me long ago. (mine)"), ("雨早就不下了。咱们快走吧。", "3. The rain stopped long ago. Let’s hurry. (mine)"), ("他参军没那么早。前年他还在上高中呢。", "4. He didn’t join the army that early. The year before last he was still in high school. (mine; the negative form 没那么早)"),
       ("图书馆早就关门了。你别去了。", "5. The library closed long ago. Don’t go. (mine)"), ("我早就想学开飞机了，可是从来没有机会。", "6. I’ve wanted to learn to fly a plane for a long time, but I’ve never had the chance. (mine)")]
L3 = lesson(
    "Lesson 19 Presentation 1 grammar: the adverb 早(就)",
    "早 + 就 · 没那么早 · long before the time assumed",
    requires=[],
    cards=[
        card("The adverb 早就",
             "早 can be used before (V/VP + 了) to indicate the action (V/VP) has occurred for a while or for some time. 就 or 已(经) is often used after 早 and forms 早就 or 早已 to emphasize the action occurred “long before the time assumed”. For instance, “李老师早就从中国回来了” implies that Li Laoshi had come back long before others assumed he would. Affirmative: Subject + 早(就) + Verb phrase / Adjective phrase + 了. Interrogative: Subject + 早(就) + Verb phrase / Adjective phrase + 了 + 吗？ Negative: Subject + 没那么早 (+ other part; often omitted).",
             examples=[D(z, e) for z, e in Z1]),
        card("Examples (1 to 6)", "The dialogs 5 and 6 show the negative 没那么早.", examples=[D(z, e) for z, e in Z2]),
        card("Grammar Activity 1 (Reading, Writing, Speaking and Listening)",
             "A. With a classmate, complete the exchanges, using 早就 once in each exchange: 1. A: 你去过长城吗？ B: ___的时候，你还是个小孩子呢。 2. A: 你的听力作业做完了吗？ B: ___。我是___ 3. A: 我___，你怎么还没买？ B: 我一直在忙啊！ 4. A: ___ B: 他大学毕业是去年才大学毕业的，没那么早。 5. A: 锻炼完身体以后，咱们把衣服洗洗吧。 B: ___ B. Listen to the exchanges and see if you can improve your work (audio, not included). The book leaves the blanks to the student; my completed exchanges:",
             examples=[D(z, e) for z, e in ZA1]),
        card("Grammar Activity 2 (Reading and Speaking)",
             "A. Revise the sentences in Column A using 早就: 1. 今天我起床特别早，因为我要坐九点的飞机去华盛顿。 2. 他很长时间以前就告诉过我了。 3. 雨一小时以前就不下了。咱们快走吧。 4. 他参军不太早。前年他还在上高中呢。 5. 图书馆关门很长时间了。你别去了。 6. 我很久以前就想学开飞机，可是从来没有机会。 B. Share your work with a classmate. Then take turns asking each other questions. My revisions (the book leaves the column blank):",
             examples=[D(z, e) for z, e in ZA2]),
        card("Grammar Activity 3 (Writing and Speaking)",
             "Write five statements about something you have done much sooner than expected using the adverb 早就. Two of the statements should be false and the other three should be true. Share your statements with the class. The class will guess which three statements are true. (Your own sentences, so there is nothing to print.)"),
    ],
    exercises=[
        M("What does 早就 stress?", "The action happened long before the time assumed", ["The action will happen soon", "The action never happens", "The action is very slow"], "早就: long ago."),
        M("What word often follows 早 in this pattern?", "就", ["了", "吗", "呢"], "早就 / 早已."),
        M("What is the negative reply pattern?", "没那么早", ["不早就", "没早就", "早不就"], "没那么早."),
        M("Which sentence means “I finished my homework long ago”?", "我早就做完作业了", ["我早做作业就了", "我做完早就作业了", "我就早做完作业了"], "Subject + 早就 + VP + 了."),
        M("Which sentence means “The library closed long ago”?", "图书馆早就关门了", ["图书馆关门早就了", "图书馆就早关门了", "早图书馆就关门了"], "早就 before the verb."),
        M("How does the brother answer “你哥哥早就去北京上大学了吧？”?", "他去得没那么早，今年刚上二年级", ["他早就去了", "他明年去", "他不去北京"], "没那么早."),
        M("Revise “他很长时间以前就告诉过我了” with 早就.", "他早就告诉过我了", ["他早告诉就过我了", "他就早告诉过我了", "早他就告诉过我了"], "早就 before the verb."),
        M("Which sentence expresses a long-held wish?", "我早就想请你来看看我们的新房子了", ["我想早就请你", "我请早就你来", "早我就请想你"], "早就想."),
        F("去青岛的高铁早就发___了，你怎么还在这儿等呢？", "车", PART, "发车: depart."),
        F("我早就想学开___机了，可是从来没有机会。", "飞", PART, "开飞机: fly a plane."),
    ],
)

# ------------------------------------------------------------------ 4. 为 and 给
W1 = [("请给我们拿一双筷子。", "Please get us a pair of chopsticks. (colloquial)"), ("请为客人提供筷子。", "Please provide chopsticks for the guests. (formal)"), ("服务员给我送来了茶水。", "The waiter brought me tea. (colloquial)"), ("列车工作人员热情地为旅客送茶水。", "The train staff warmly bring tea for the passengers. (formal)")]
W2 = [("我给小王发了一个邮件。", "1. I sent Xiao Wang an email. (给 introduces the recipient of delivery)"), ("有时间给你爸妈去个电话。", "2. When you have time call your parents.")]
W3 = [("他们为谁参军？", "1. Who are they joining the army for?"), ("我这样做是为你好。", "2. I do this for your own good."), ("她为陆军工作了二十多年。", "3. She has worked for the army for more than twenty years."), ("他为让爸爸高兴带他回老家。", "4. He took his father back to his hometown to make him happy."), ("大家都为学好中文努力。", "5. Everyone works hard in order to learn Chinese well.")]
W4 = [("你不用为我担心。", "1. You don’t need to worry about me."), ("大家都为你高兴。", "2. Everyone is happy for you.")]
WA4 = [("服务员把啤酒给我们送过来了。", "1. The waiter brought the beer over to us. (the book’s picture, Your Beer)"), ("他们为谁参军？", "2. Who are they joining the military for?"), ("军队为我租了一套公寓。", "3. The army rented an apartment for me."), ("妈妈给我买了一个新手机。", "4. Mom bought me a new phone."), ("我给他买了一串香蕉。", "5. I bought him a bunch of bananas."), ("给我看一下照片好吗？", "6. May I see the photos?")]
WA5 = [("医生为病人看病。", "A doctor treats patients. (sample, mine)"), ("医生给病人开药。", "A doctor prescribes medicine for patients. (mine)"), ("老师为学生上课。", "A teacher teaches classes for students. (mine)"), ("老师给学生讲故事。", "A teacher tells students stories. (mine)"), ("列车服务员为旅客提供服务。", "A train attendant provides service for the passengers. (mine)"), ("列车服务员给旅客送茶水。", "A train attendant brings the passengers tea. (mine)")]
L4 = lesson(
    "Lesson 19 Presentation 1 grammar: the prepositions 为 and 给",
    "for the beneficiary · colloquial 给 and formal 为 · reason and purpose",
    requires=[],
    cards=[
        card("The prepositions 为 and 给",
             "In Lesson 7 and in this lesson we learned these two sentences: 请给我们拿一双筷子。售货车为您提供各种饮料和零食。 In both sentences, 给 and 为 can be translated as “for” and introduce the beneficiaries. In terms of introducing beneficiaries, 给 and 为 are interchangeable, but 给 is more colloquial and 为 is more formal. The original meaning of 给 is to give, and the original meaning of 为 is “in order to” or “for the purpose of”. Therefore, their usage sometimes overlaps and other times they remain distinct.",
             examples=[D(z, e) for z, e in W1]),
        card("给 introduces the recipient of delivery; 为 does not", "Examples:", examples=[D(z, e) for z, e in W2]),
        card("为 introduces reason and purpose and takes complex objects; 给 does not", "Examples:", examples=[D(z, e) for z, e in W3]),
        card("为 can be used in abstract sentences; 给 is often used in concrete sentences", "Examples:", examples=[D(z, e) for z, e in W4]),
        card("Grammar Activity 4 (Speaking and Writing)",
             "A. Describe each image using 为 or 给 in the table: 1. Your beer. 2. They joined the military for … 3. This phone is yours! 4. You want to buy this. 5. An apartment has been rented for you. 6. You want to see the photos. (Pixabay pictures, not included.) B. Share your sentences with a classmate, and then read the possible answers below:",
             examples=[D(z, e) for z, e in WA4]),
        card("Grammar Activity 5 (Listening, Writing and Speaking)",
             "A. An adult is asking their five-year-old niece about things people do, such as doctors, teachers and attendants on a train. In her answers, the girl often uses 为 and 给. Pair up and write what the girl could have said, using 为 and 给 as often as possible: 医生, 老师, 列车服务员. B. Listen to the passage again and write what you hear Zhenzhen say about the following people: 医生, 老师, 列车服务员, 爸爸妈妈. C. Share your answers with your partner. Go over the script and refine your work. (Audio, not included; the book prints no script. My samples for Step A:)",
             examples=[D(z, e) for z, e in WA5]),
    ],
    exercises=[
        M("Which of 给 and 为 is more colloquial?", "给", ["为", "Both equally", "Neither"], "给 is colloquial; 为 is formal."),
        M("Which sentence is the formal one?", "请为客人提供筷子", ["请给我们拿一双筷子", "服务员给我送来了茶水", "我给小王发了一个邮件"], "为 is formal."),
        M("Which preposition introduces the recipient of delivery?", "给", ["为", "Both", "Neither"], "我给小王发了一个邮件."),
        M("Which preposition introduces reason and purpose?", "为", ["给", "Both", "Neither"], "为 introduces reason and purpose."),
        M("What does “我这样做是为你好” mean?", "I do this for your own good", ["I do this for money", "I do this because of you", "I do this to make you leave"], "为你好."),
        M("What does “他们为谁参军？” ask?", "Who are they joining the army for?", ["Who joins the army?", "When do they join?", "Why is the army small?"], "为谁参军."),
        M("Which sentence uses 为 abstractly?", "你不用为我担心", ["我给他买了一串香蕉", "妈妈给我买了一个新手机", "我给小王发了一个邮件"], "为 can be abstract; 给 is concrete."),
        M("Which picture sentence says Mom bought me a phone?", "妈妈给我买了一个新手机", ["军队为我租了一套公寓", "我给他买了一串香蕉", "给我看一下照片好吗"], "Activity 4 key."),
        F("她为陆军工___了二十多年。", "作", PART, "工作: work."),
        F("军队为我租了一套___寓。", "公", PART, "公寓: apartment."),
    ],
)

# ------------------------------------------------------------------ 5. 反正
F1 = [("不管你想不想买，反正我要买。", "No matter whether you want to buy it or not, I’m buying it anyway."), ("不论雨下得有多大，我反正怎么都要去上班。", "No matter how hard the rain falls, I’m going to work anyway."), ("不管飞机票多便宜，我反正不想坐飞机。", "No matter how cheap the plane ticket is, I don’t want to fly anyway.")]
F2 = [("咱们出去散散步吧，反正现在也没什么事。", "Let’s go out for a walk; there’s nothing going on now anyway."), ("我去买菜吧，反正我要开车去银行。", "I’ll go buy groceries; I’m driving to the bank anyway."), ("你想买一等座就买吧，反正比二等座贵不了多少。", "If you want to buy first class then buy it; it’s not much more than second class anyway."), ("你要回中国就回吧，反正现在机票很便宜。", "If you want to go back to China then go; plane tickets are cheap now anyway.")]
FA7 = [("有“反正”：我今天不去了，反正明天还有时间。", "With 反正: I’m not going today; there’s time tomorrow anyway. (mine)"), ("没有“反正”：我今天不去了，因为明天还有时间。", "Without 反正: I’m not going today, because there’s time tomorrow. (mine)"), ("有“反正”：不管你同意不同意，反正我要去。", "With 反正: Whether you agree or not, I’m going anyway. (mine)"), ("没有“反正”：不管你同意不同意，我都要去。", "Without 反正: Whether you agree or not, I’m going. (mine)"),
       ("有“反正”：咱们坐火车吧，反正时间短。", "With 反正: Let’s take the train; the trip is short anyway. (mine)"), ("没有“反正”：咱们坐火车吧，因为时间短。", "Without 反正: Let’s take the train because the trip is short. (mine)")]
L5 = lesson(
    "Lesson 19 Presentation 1 grammar: the adverb 反正",
    "不管…反正… · suggested action, 反正 + reason · anyway",
    requires=[],
    cards=[
        card("The adverb 反正 (1): 不管/不论 + X/Y …, 反正 Z",
             "The adverb 反正 has two uses. 1. Used in the pattern (不管/不论 + X/Y) …, 反正 Z …, it indicates “regardless of / no matter if X (or Y), Z will happen anyway”. Examples:",
             examples=[D(z, e) for z, e in F1]),
        card("The adverb 反正 (2): suggested action, 反正 + reason",
             "2. Used to provide reasons or excuses for doing or not doing something, it usually uses the structure “suggested action, 反正 + reason”. Examples:",
             examples=[D(z, e) for z, e in F2]),
        card("Grammar Activities 6 and 7",
             "Activity 6 (Listening, Writing and Speaking): A. Listen to the six statements and write a revised version of each using 反正. B. Share your work with a classmate; then go over the script and suggested answers and refine your sentences. (Audio, not included; the book prints no script.) Activity 7 (Writing and Speaking): A. Write four pairs of sentences in the table: one sentence uses the adverb 反正 and the other does not, while both express the same idea (有“反正” / 没有“反正”). B. Pair up and take turns saying a sentence to your partner without using 反正; your partner will say one to you using 反正. The book leaves the table to the student; my sample pairs:",
             examples=[D(z, e) for z, e in FA7]),
    ],
    exercises=[
        M("How many uses does 反正 have in this lesson?", "Two", ["One", "Three", "Four"], "(1) 不管…反正; (2) reason."),
        M("What does “不管你想不想买，反正我要买” mean?", "Whether or not you want to buy it, I’m buying it anyway", ["I won’t buy it", "You must buy it", "Nobody buys it"], "不管…反正…."),
        M("What does “不管飞机票多便宜，我反正不想坐飞机” mean?", "No matter how cheap the ticket, I don’t want to fly anyway", ["I want a cheap ticket", "Tickets are free", "I’ll fly tomorrow"], "不管…反正…."),
        M("Which sentence gives a reason for a suggestion?", "咱们出去散散步吧，反正现在也没什么事", ["不管你想不想买，反正我要买", "我早就想坐坐了", "他们为谁参军"], "Suggested action, 反正 + reason."),
        M("What does “你想买一等座就买吧，反正比二等座贵不了多少” mean?", "Buy first class if you like; it’s not much more than second class anyway", ["First class is far more expensive", "Don’t buy any seat", "Second class is sold out"], "贵不了多少."),
        M("Why will the speaker buy groceries in “我去买菜吧，反正我要开车去银行”?", "He is driving to the bank anyway", ["The shop is closed", "He has no money", "The bank is far"], "反正 + reason."),
        M("What does “你要回中国就回吧，反正现在机票很便宜” mean?", "Go back to China if you want; tickets are cheap now anyway", ["Don’t go to China", "Tickets are expensive", "You can’t buy a ticket"], "反正 + reason."),
        M("Which word can replace 不管 in the first pattern?", "不论", ["不但", "因为", "虽然"], "不管/不论."),
        F("不管飞机票多便宜，我___正不想坐飞机。", "反", PART, "反正: anyway."),
        F("我去买菜吧，反正我要开车去银___。", "行", PART, "银行: bank."),
    ],
)

# ------------------------------------------------------------------ 6. Skill Integration 1-2
ANN = [("我是本次列车的列车长李丽。欢迎您乘坐由北京开往上海的Ｇ一次列车！", "1. I am Li Li, the conductor of this train. Welcome aboard train G1 from Beijing to Shanghai! (the book writes G1)"), ("列车一共运行一千三百一十八公里，时间是四小时二十八分，平均每小时车速接近三百五十公里。", "2. The train runs 1,318 kilometers in total, taking four hours and twenty-eight minutes, an average speed of nearly 350 kilometers per hour. (the book writes the numbers as digits)"),
       ("在京沪高铁线上，现在每天有六十多辆高速列车从北京开往上海，也有六十多辆高速列车从上海开往北京。", "3. On the Beijing–Shanghai high-speed line there are now more than sixty high-speed trains a day from Beijing to Shanghai and more than sixty from Shanghai to Beijing."), ("全车提供免费无线上网服务。车上还有餐车，每节车厢也有热水器，您可以用热水泡茶。", "4. The whole train offers free wireless internet. There is also a dining car, and every carriage has a water heater, so you can make tea with hot water."),
       ("本次列车沿途经过天津市和河北、山东等五个省。", "5. Along the way this train passes through Tianjin and five provinces including Hebei and Shandong. (as the book says, 天津市 and 河北、山东 are counted among the five)"), ("如果您需要什么帮助，请告诉列车工作人员，他们会很高兴地为您服务。", "6. If you need any help, please tell the train staff; they will gladly serve you.")]
TF19 = [("这是列车长做的广播。", "1. This is an announcement made by the train conductor. — True (key mine)"), ("这趟列车在北京和上海之间运行，沿途停五次。", "2. This train runs between Beijing and Shanghai and stops five times along the way. — False (it says the train passes through Tianjin and five provinces; it does not say it stops five times; mine)"), ("这趟列车的速度大约是每小时三百五十公里。", "3. This train travels at around 350 km per hour. — True"), ("每天有六十多辆高速列车在北京和上海之间运行。", "4. There are over sixty high-speed trains traveling between Beijing and Shanghai daily. — True"), ("旅客要去餐车买饮料和零食。", "5. Passengers are asked to go to the dining car to buy drinks and snacks. — False (the announcement only says there is a dining car and a water heater in each carriage; mine)")]
DLG19 = [("旅客", "请问，这趟车一共要开多长时间？", "Excuse me, how long does this train take in all?"), ("列车长", "一共四小时二十八分。", "Four hours and twenty-eight minutes in all."), ("旅客", "车上有餐车吗？我想买点儿吃的。", "Is there a dining car on the train? I’d like to buy something to eat."), ("列车长", "有。每节车厢也有热水器，您可以泡茶。", "Yes. Every carriage also has a water heater, so you can make tea."),
         ("旅客", "车上可以上网吗？", "Can I get online on the train?"), ("列车长", "可以，全车提供免费无线上网服务。", "Yes, the whole train has free wireless internet."), ("旅客", "谢谢，如果有问题我再来找您。", "Thank you; if I have a problem I’ll come find you."), ("列车长", "没问题，请告诉列车工作人员，他们会很高兴地为您服务。", "No problem; please tell the train staff and they will gladly serve you.")]
L6 = lesson(
    "Lesson 19 Presentation 1 skill integration: the conductor’s announcement",
    "列车长的广播 · 京沪高铁 · 对错题 · 与列车长对话",
    requires=[],
    cards=[
        card("Skill Integration Activity 1 (Listening, Speaking, Writing and Reading)",
             "A. Listen to the dialog between David and Liu Dong and answer in Chinese (面 in this dialog means “noodle”): 1. 刘冬是什么人？ 2. 她现在经常坐火车去哪儿？为什么？ 3. 二十多年前她不喜欢坐火车去成都，为什么？ B. Listen again and fill in the table 关于 / 细节 (details) with 以前的火车 and 现在的高铁. C. Pair up and ask your partner at least three questions using the information you learned in Step A. D. Playing David’s character, write an email to a Chinese friend telling them what you learned (TO, CC, Subject). E. Go over the script and then refine your email. (Audio, not included; the book prints no script.)"),
        card("Skill Integration Activity 2 (Reading, Speaking and Writing): the announcement",
             "A. Listen to the passage and mark each statement True or False. (The audio is not included; the book prints the announcement as Step B, below, and my key follows from it.) B. Pair up and take turns translating the sentences into English: Student 1 reads in Chinese and speaks the English version while Student 2 listens to the English and repeats it in Chinese without reading the sentences. The six sentences (the book writes 1318, 4, 28, 350 and 60 as digits and “G1 次”):",
             examples=[D(z, e) for z, e in ANN]),
        card("The True or False statements and my key",
             "The statements below are the book’s five; the keys are mine, from the announcement.",
             examples=[D(z, e) for z, e in TF19]),
        card("Skill Integration Activity 2 C: a dialog with the conductor",
             "C. Work in pairs to create a dialog between an international traveler and a train conductor (旅客 / 列车长, five turns each) using the information you’ve learned and act it out for the class. The book leaves the lines blank; this is a sample dialog (mine).",
             examples=dlg(DLG19)),
    ],
    exercises=[
        M("Who is making the announcement?", "The train conductor Li Li", ["A passenger", "A waiter", "A pilot"], "我是本次列车的列车长李丽."),
        M("Which train is it?", "The one running from Beijing to Shanghai", ["From Shanghai to Xi’an", "From Beijing to Tianjin only", "From Guangzhou to Hong Kong"], "由北京开往上海."),
        M("How long does the whole trip take?", "Four hours and twenty-eight minutes", ["Two hours", "Eight hours", "Four hours and eighteen minutes"], "时间是四小时二十八分."),
        M("What is the average speed?", "Nearly 350 kilometers per hour", ["About 150 kilometers per hour", "About 250 kilometers per hour", "About 500 kilometers per hour"], "平均每小时车速接近三百五十公里."),
        M("How many kilometers does the train run in total?", "1,318", ["1,138", "318", "13,180"], "一千三百一十八公里."),
        M("How many trains a day run in each direction?", "More than sixty", ["More than six", "About twenty", "More than six hundred"], "六十多辆."),
        M("What is free on the train?", "Wireless internet", ["Tea", "Lunch", "Newspapers"], "全车提供免费无线上网服务."),
        M("What does each carriage have?", "A water heater", ["A shop", "A bed", "A television"], "每节车厢也有热水器."),
        M("Is the statement “Passengers are asked to go to the dining car to buy drinks and snacks” true?", "False; the announcement only says there is a dining car", ["True", "True but only at night", "The announcement says nothing about a dining car"], "Key mine."),
        F("本次列车沿___经过天津市和河北、山东等五个省。", "途", PART, "沿途: along the way."),
        F("如果您需要什么帮助，请告诉列车工作___员。", "人", PART, "工作人员: staff."),
    ],
)

# ------------------------------------------------------------------ 7. Skill Integration 3 + Using Chinese in Context
HSR = ["中国的高速铁路，是目前世界上最大规模的高速铁路网，从二零零三年十月十二日第一条高速铁路通车，到二零一九年十二月，总里程达到三万五千公里，其中时速达三百公里的线路总里程超过一万公里，占世界的三分之二以上。包括香港在内的三十一个省级行政区已经有了高铁。另外，目前武汉到广州、北京到上海、北京到天津的高速铁路，都达到了每小时三百五十公里的全世界最高速度。按照计划，在二零二五年中国将建成三万八千公里长的高速铁路网。",
       "中国大陆人口非常多，人们的出行对高速铁路的需求很大。而中国大陆各地气候和地形又不一样，给建设高铁带来很多困难。因此，建设高速铁路的时候，中国根据不同地区的情况，建成了针对不同气候、不同地形的高铁系统。",
       "高铁给中国人的生活和工作方式带来了很大变化，促进了沿路地区的经济发展，也使中国大陆开始进入“高铁社会”。目前没有时速二百公里以上的铁路运营的地区，只有澳门和西藏。中国也在积极争取参加其他国家高速铁路的建设。"]
HSR_E = ["1. China’s high-speed railway is currently the world’s largest-scale high-speed rail network. From the opening of the first high-speed line on October 12, 2003 to December 2019, the total mileage reached 35,000 kilometers, of which the lines running at 300 km/h exceed 10,000 kilometers in total, more than two thirds of the world’s. The 31 provincial-level administrative regions, including Hong Kong, already have high-speed rail. In addition, the lines from Wuhan to Guangzhou, Beijing to Shanghai and Beijing to Tianjin all reach 350 kilometers per hour, the highest speed in the world. According to the plan, in 2025 China will complete a high-speed rail network 38,000 kilometers long. (the book writes the numbers as digits and misprints 达了到)",
         "2. Mainland China has a very large population, and people’s travel creates a big demand for high-speed rail. But climate and terrain differ across mainland China, which brings many difficulties to building high-speed rail. Therefore, when building high-speed rail, China built, according to the conditions in different regions, high-speed rail systems targeted at different climates and different terrains.",
         "3. High-speed rail has brought great changes to the way Chinese people live and work, promoted the economic development of the regions along the lines, and also made mainland China begin to enter the “high-speed rail society”. At present the only places without railways operating at over 200 kilometers per hour are Macao and Tibet. China is also actively seeking to take part in building other countries’ high-speed railways."]
PROV = table(["排序", "省", "高铁里程 (公里)", "人口 (万人)", "GDP (十亿元)"], [["1", "广东省", "2,095", "11,346", "10,767"], ["2", "辽宁省", "2,033", "4,359", "2,500"], ["3", "江西省", "1,941", "4,647", "2,476"], ["4", "湖南省", "1,892", "6,899", "3,975"]],
             title="2019年中国各省市区高铁里程前四名 (the book’s table; as printed)")
ROUTE = table(["路线", "时间", "车次", "座位", "票价"], [["北京到上海", "", "", "", ""], ["上海到西安", "", "", "", ""], ["西安到广州", "", "", "", ""], ["广州到香港", "", "", "", ""]],
              title="Using Chinese in Context Activity 2 C: the route table the student fills from a booking website (blank in the book)")
CTX = [("春节快到了，你和一位朋友想去杭州玩儿几天。你说最好坐高铁去，她问为什么。", "1. The Spring Festival is coming and you and a friend want to go to Hangzhou for a few days. You say it’s best to take the high-speed rail and she asks why."), ("你觉得买一等座的票最合适，她问为什么。", "2. You think buying first-class tickets is most suitable, and she asks why."), ("她问你高速列车上的服务怎么样。", "3. She asks what the service on the high-speed train is like."), ("她想知道，在高速列车上可以看什么、做什么。", "4. She wants to know what you can look at and do on a high-speed train.")]
L7 = lesson(
    "Lesson 19 Presentation 1 skill integration and using Chinese in context: China’s high-speed rail",
    "中国高铁里程 · 三小时高铁圈 · 王刚的语音留言 · 各省高铁里程",
    requires=[],
    cards=[
        card("Skill Integration Activity 3 (Reading, Speaking and Writing): the passage",
             "A. Read the passage and determine the meanings of the underlined expressions (the underlining is not in the text). Then, in English, write an email to a friend about China’s high-speed rail (TO, CC, Subject). B. Share your email with a classmate. Then each partner asks at least four questions. C. You play the role of an international traveler and your partner is a Chinese high-speed rail official. Ask questions about China’s high-speed rail, then switch roles and repeat. The passage (the book writes the numbers as digits and “3.5万”):",
             examples=[D(z, e) for z, e in zip(HSR, HSR_E)]),
        card("Using Chinese in Context Activity 1 (Reading and Speaking)",
             "Pair up and take turns telling your partner what you would say in the following situations. Provide as many details as possible using two or three sentences. When you are done, switch roles and repeat the activity. (A photograph of a train station, not included.)",
             examples=[D(z, e) for z, e in CTX]),
        card("Using Chinese in Context Activity 2 (Listening, Writing, Reading and Speaking): Wang Gang’s voice mail",
             "You are David. Recently you told Wang Gang, your Chinese friend in Beijing, that you plan to take your parents on a visit to China for a couple of weeks in August. A. Learn the meanings of these words first, 根据, 建议, 安排, 决定 and 信息, then listen to a voice mail from Wang Gang and take notes in Chinese. (Audio, not included; the book prints no script.) B. Pair up, share your notes and then go over the script. C. Use one of the book’s two websites (links not included) or a site of your choice to find which trains you would take to the destinations listed below, then discuss your choices with your partner. D. Call Wang Gang (played by your partner) and tell him in Chinese about the trains you and your parents will take; he will explain how he will book the tickets and answer your questions.",
             tables=[ROUTE]),
        card("Using Chinese in Context Activity 2 (Reading, Speaking and Writing): the provincial rail systems",
             "You are a graduate student at the University of Macao and you are writing a paper about the provincial high-speed rail systems in China. A. Pair up and answer your academic advisor’s questions about the high-speed rail systems in several provinces; your partner plays the advisor. B. Choose one of the first two provinces, Guangdong and Liaoning. Find which cities can be reached within four hours from the capital city, get the train schedule information and find a tourist attraction to visit in each city. (The two maps, 广东省广州市三小时高铁圈 and 辽宁省沈阳市三小时高铁圈, are not included.) C. Your partner explores the other provinces. D. Share your findings with your partner and discuss which province you would both recommend to friends. E. Write a brief introduction, 200 to 300 characters long, telling your advisor about one three-hour high-speed rail line.",
             tables=[PROV]),
    ],
    exercises=[
        M("What does the passage say about China’s high-speed rail network?", "It is the largest in the world", ["It is the smallest", "It has only one line", "It is under construction only"], "最大规模的高速铁路网."),
        M("When did the first high-speed line open?", "On October 12, 2003", ["In 1999", "In 2010", "On January 1, 2019"], "二零零三年十月十二日第一条高速铁路通车."),
        M("How many kilometers had the network reached by December 2019?", "35,000", ["3,500", "38,000", "350,000"], "总里程达到三万五千公里."),
        M("What share of the world’s 300 km/h lines does China have?", "More than two thirds", ["About a half", "Less than a tenth", "All of them"], "占世界的三分之二以上."),
        M("Which route reaches the world’s top speed of 350 km/h?", "Beijing to Shanghai", ["Beijing to Lhasa", "Macao to Zhuhai", "Lhasa to Chengdu"], "北京到上海 is named."),
        M("How many kilometers long will the network be by 2025?", "38,000", ["35,000", "3,800", "48,000"], "三万八千公里."),
        M("Which two places had no railway over 200 km/h at the time?", "Macao and Tibet", ["Hong Kong and Beijing", "Hainan and Taiwan", "Tibet and Xinjiang"], "只有澳门和西藏."),
        M("Why was building high-speed rail difficult in China?", "Climates and terrain differ across the mainland", ["The population is small", "There is no money", "There are no mountains"], "气候和地形又不一样."),
        M("Which province ranked first in 2019 high-speed rail mileage?", "Guangdong", ["Liaoning", "Jiangxi", "Hunan"], "广东省 2,095 km."),
        F("按照计划，在二零二五年中国将建成三万八千公里长的高速铁___网。", "路", PART, "高速铁路网: high-speed rail network."),
        F("高铁给中国人的生活和工作方式带来了很大变___。", "化", PART, "变化: change."),
    ],
)

# ------------------------------------------------------------------ 8. vocabulary
L8 = vocab_lesson("Lesson 19 Presentation 1 vocabulary", "38 words from the book’s Presentation 1 list",
                  "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十九课 Presentation 1: 坐高铁回老家, 早就, 为/给, 反正, high-speed rail skills", [L1, L2, L3, L4, L5, L6, L7, L8])
