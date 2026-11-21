"""Unit 38: Lesson 13 (At the Airport) Presentation 3 and Area Studies from the book's texts: the security-check story, 的样子,
the resultative complement 到, 原来, 因此, 要是…就…, the skill-integration and using-Chinese activities, the vocabulary list and
the Beijing Daxing International Airport reading. Audio, pictures, the video and the board graphics are not included;
answer keys the book does not print are mine."""
import re

from zh_auto import *
from zh_l13_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"长": "chang2", "称": "cheng1"}
    for key, idx, val in (("长大", 0, "zhang3"), ("背着", 0, "bei1"), ("得到", 0, "de2")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    if "睡好觉" in zh or "睡觉" in zh:
        i = zh.find("觉")
        f[i] = "jiao4"
    i = zh.find("行李")
    while i >= 0:
        f[i + 1] = "li5"
        i = zh.find("行李", i + 2)
    if "你得快点儿" in zh:
        f["得"] = "dei3"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the security-check story
P3 = ("“九一一”以前，乘坐航班很方便，拿到登机牌后，可以直接上飞机。现在登机前要过安检，一些人因此误了航班。"
      "去年夏天，我坐飞机去纽约看朋友。我已经在网上办好了登机手续，所以只提前了四十分钟到机场。到了机场才发现过安检要排很长的队。因为离飞机起飞只有半个小时了，我只好请排在前边的人让我往前站。大家看到我着急的样子，都让开路，让我站到了最前边。可是，过安检的时候，安检人员要检查我的背包。原来，里面有一瓶没喝完的水。过了安检，我飞快地跑到登机口，可是机门已经关了。唉，要是我早一点儿出门，就不会误机了！")
P3_E = ("Before 9/11, taking a flight was very convenient: after getting your boarding pass, you could board the plane directly. Now you have to go through security before boarding, and as a result some people miss their flights. Last summer I flew to New York to see a friend. I had already checked in online, so I arrived at the airport only forty minutes early. After arriving I found that going through security meant standing in a very long line. Because only half an hour was left before takeoff, I had no choice but to ask the people ahead of me to let me move forward. When everyone saw my anxious look, they all made way and let me stand at the very front. But when I went through security, the security staff wanted to check my backpack. As it turned out, there was a bottle of water I hadn’t finished inside. After security I ran to the boarding gate as fast as I could, but the airplane door had already closed. Ah, if only I had left home a little earlier, I wouldn’t have missed the flight!")
SCENE1 = [("大卫要乘坐十点十分的飞机，可是，他九点半才来到机场。大卫拉着一个大行李箱，背着一个背包，跑到办理登机手续的服务台。", "David is taking the 10:10 plane, but he only got to the airport at 9:30. David, pulling a big suitcase and carrying a backpack, runs to the check-in counter."),
          ("大卫：对不起，我要托运行李。", "David: Sorry, I need to check my luggage."), ("工作人员：您的机票和证件呢？", "Staff: Your ticket and ID?"), ("大卫：我已经在网上办理登机手续了。这是我的登机牌。", "David: I already checked in online. Here is my boarding pass."),
          ("工作人员：请把行李箱放到这里称一下。", "Staff: Please put the suitcase here to be weighed."), ("大卫：没超重吧？", "David: It isn’t overweight, is it?"), ("工作人员：没有。这是您的行李牌。不过，你得快点儿去安检和登机。", "Staff: No. Here is your luggage tag. But you have to hurry to security and boarding.")]
SC_MINE = [("大卫跑到安检处，前面排着很长的队。他很着急，请前面的人让他先过。", "David runs to the security checkpoint, where a long line has formed. He is anxious and asks the people ahead to let him go first. (my Scene 2 description)"),
           ("安检人员：请把背包放在这里。里面有水吗？", "Security officer: Please put your backpack here. Is there water inside? (my Scene 3)"), ("大卫：有一瓶没喝完的水。对不起，我忘了。", "David: There is a bottle of water I haven’t finished. Sorry, I forgot. (my Scene 3)"),
           ("登机口工作人员：对不起，机门已经关了。", "Gate agent: Sorry, the plane door has already closed. (my Scene 4)"), ("大卫：唉，要是我早一点儿出门就好了！", "David: Ah, if only I had left earlier! (my Scene 4)")]
ORDER = [("在网上办登机手续", "Check in online"), ("拿登机牌", "Get the boarding pass"), ("出门去机场", "Leave home for the airport"), ("提前四十分钟到机场", "Arrive 40 minutes early"), ("发现安检处排着长队", "Find a long line at security"), ("请前面的人让我往前站", "Ask the people ahead to let me forward"), ("安检人员要检查我的背包", "Security wants to check my backpack"), ("跑到登机口", "Run to the gate"), ("飞机关门", "The plane door closes")]
TRAVEL = [("Boarding place", "车站", "机场"), ("Modes of transportation", "火车、汽车", "飞机"), ("Terms for vehicles", "列车", "航班"), ("Tickets", "车票", "机票"), ("Place you wait for boarding", "站台", "登机口"), ("Getting on board", "上车", "登机"), ("Getting off", "下车", "下飞机"), ("Take off", "出发", "起飞"), ("Arrive", "到站", "到达"), ("Traveling in the vehicles", "乘车", "乘机"), ("Miss the vehicle", "误车", "误机")]
L1 = lesson(
    "Lesson 13 Presentation 3: missing a flight at security",
    "误机 · 请前面的人让我往前站 · 唉，要是我早一点儿出门…",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. What articles are not allowed on an airplane? B. Have you ever had anything confiscated at the airport security gate? C. Have you ever experienced complications at the security checkpoint? What was the problem? D. Have you ever missed a flight? Why?"),
        card("Presentation 3: a missed flight",
             "(The book also prints this passage in traditional characters. The book writes the time as 40 分钟; it is spelled out here.)",
             examples=[D(P3, P3_E)]),
        card("Activities 1 and 2",
             "Activity 1 (Listening). A. Global listening: 1. What are the repercussions of 9/11 at airports now? 2. What did the speaker say happened at the end of the passage? B. Detailed listening: what caused the speaker to miss the flight? List three details. (Audio, not included. From the text: people now must pass security, so some miss flights; the speaker ended up missing the flight because he arrived late for a long security line, a bottle of water was found in his bag, and the plane door had closed when he got to the gate.) Activity 2 (Reading). A. Using what you heard, list the nine events in order of occurrence. B. Pair up, read your sorted sentences and discuss any differences. The book’s nine items are listed in the table in the book’s order; my sorted order (mine) is the second table.",
             tables=[table(["Event (book order 1 to 9)", "Meaning"], [("请前面的人让我往前站", "Ask the people ahead to let me forward"), ("出门去机场", "Leave for the airport"), ("在网上办登机手续", "Check in online"), ("安检人员要检查我的背包", "Security wants to check my backpack"), ("提前四十分钟到机场", "Arrive 40 minutes early"), ("发现安检处排着长队", "Find a long line at security"), ("拿登机牌", "Get the boarding pass"), ("跑到登机口", "Run to the gate"), ("飞机关门", "The plane door closes")], title="The nine items", say=[0]),
                     table(["Order (mine)", "Event"], [(str(i + 1), z + " (" + e + ")") for i, (z, e) in enumerate(ORDER)], title="Sorted order (mine)")]),
        card("Activity 3 (Listening) and Activity 4 (writing scenes)",
             "Activity 3. Listen to the dialog and answer: 1. What did the passenger request at the beginning? 2. What set off the metal detector? 3. What contraband was in the passenger’s bag? (Audio, not included.) Activity 4 (Reading, Writing and Speaking). A. Pair up and write short scenarios with dialog using the information provided. Scene 1 is given as an example (location: airport check-in desk; characters: David and the check-in agent; time: 9:30 a.m.). Scene 2 is at the airport security checkpoint, 9:40 a.m. (David and other passengers lining up); Scene 3 is at the check-in desk per the book, 9:45 a.m. (David and a security officer); Scene 4 is at the boarding gate, 10:00 a.m. (David and the boarding gate agent). B. Act out the skits in order. The book’s Scene 1 and my brief Scenes 2 to 4:",
             examples=[D(z, e) for z, e in SCENE1] + [D(z, e) for z, e in SC_MINE]),
        card("Activity 5 (Writing): terms for different modes of travel",
             "In the table below are terms for different modes of travel; fill in the blanks (the book gives 列车, 站台, 登机, 出发 and 误机 as examples), pair up and discuss which terms are the most difficult to remember. The book’s columns are 陆（陆路）and 空中; my completed table:",
             tables=[table(["Row", "陆路", "空中"], [(a, b, c) for a, b, c in TRAVEL], title="旅行 (mine, with the book’s examples included)")]),
    ],
    exercises=[
        M("What changed after 9/11 for passengers?", "They must go through security before boarding", ["They can board without a ticket", "Flights became cheaper", "Airports closed at night"], "现在登机前要过安检。"),
        M("How early did the speaker arrive at the airport?", "Forty minutes before the flight", ["Two hours early", "At the last minute", "A day early"], "提前了四十分钟到机场。"),
        M("How much time was left before takeoff when he joined the line?", "Half an hour", ["Two hours", "Five minutes", "One day"], "离飞机起飞只有半个小时了。"),
        M("What did the speaker do when the line was long?", "Asked the people in front to let him forward", ["Left the airport", "Cut the line silently", "Called the airline"], "请排在前边的人让我往前站。"),
        M("What did security find?", "A bottle of water he hadn’t finished", ["A knife", "A laptop", "A passport"], "里面有一瓶没喝完的水。"),
        M("Why did he miss the flight?", "The plane door had already closed", ["The flight was cancelled", "He lost his passport", "He went to the wrong airport"], "机门已经关了。"),
        M("What does the speaker regret at the end?", "He didn’t leave home a little earlier", ["He bought the ticket", "He packed too much", "He took the plane"], "要是我早一点儿出门，就不会误机了！"),
        M("What does 误机 mean?", "To miss a flight", ["To take a flight", "To cancel a flight", "To change a flight"], "误机: miss the plane."),
        M("What does 着急 mean?", "Anxious; in a hurry", ["Tired", "Happy", "Hungry"], "着急: anxious."),
        M("In the Scene 1 example, when does David arrive at the airport?", "9:30, for a 10:10 flight", ["10:10, for a 9:30 flight", "8:00, for a 10:10 flight", "9:30, for an 11:00 flight"], "九点半才来到机场。"),
        M("What does the clerk in Scene 1 tell David at the end?", "Hurry to security and boarding", ["Take the next flight", "Go home", "Pay for extra luggage"], "你得快点儿去安检和登机。"),
        M("What is the 空中 term for “take off”?", "起飞", ["出发", "到站", "上车"], "起飞 (air); 出发 (land)."),
        M("What is the 空中 term for “getting on board”?", "登机", ["上车", "站台", "列车"], "登机 (air); 上车 (land)."),
        F("现在登机前要过安检，一些人因此误了航___。", "班", PART, "航班: flight."),
        F("我飞快地跑到登机口，可是机门已经___了。", "关", PART, "关: close."),
        F("我只好请排在前边的人让我往前___。", "站", PART, "往前站: move up to stand in front."),
    ],
)

# ------------------------------------------------------------------ 2. 的样子
YZ = [("他看起来四十多岁的样子。", "He looks about forty. (noun + 样子, physical appearance)"), ("我要记住你的样子。", "I want to remember how you look. (pronoun + 样子, physical appearance)"), ("照我的样子打球。", "Play ball the way I do. (pronoun + 样子, standard for imitation)"), ("我喜欢她笑的样子。", "I like the way she smiles. (verb + 样子, physical appearance)"), ("他看起来很着急的样子。", "He looks very anxious. (adjective + 样子, apparent mental state)"), ("好像要下雨的样子。", "It looks like it’s going to rain. (verb + 样子, condition or trend)")]
YZ1 = [("看你的样子好像没睡好觉。", "You look like you didn’t sleep well."), ("我喜欢那个房子的样子。", "I like the look of that house."), ("他生气的样子很吓人。", "He looks scary when he’s angry."), ("你笑的样子真好看。", "You look really good when you smile."), ("看他的样子，一定是跟女朋友分手了。", "Judging by how he looks, he must have broken up with his girlfriend."), ("他没有要停下来的样子。", "He shows no sign of stopping."),
       ("他的样子有了很大的变化。", "His appearance has changed a lot."), ("他好像很有钱的样子。", "He seems to be rich."), ("他显出不高兴的样子。", "He showed an unhappy look."), ("他走路的样子像个海员。", "The way he walks is like a sailor’s."), ("他吃东西的样子很难看。", "The way he eats is ugly."), ("你好像很累的样子。", "You look very tired.")]
L2 = lesson(
    "Lesson 13 Presentation 3 grammar: 的样子",
    "我要记住你的样子 · 你笑的样子真好看 · 好像要下雨的样子",
    requires=[],
    cards=[
        card("的样子",
             "的样子 can be placed after nouns, pronouns, verbs or adjectives to describe: physical shape, image or appearance; apparent mental state; a standard representation of something for people to see and imitate; and (in spoken language) a condition or trend. Pattern: Noun/Pronoun/Verb/Adjective + 的样子. The book’s notes are in the English lines.",
             examples=[D(z, e) for z, e in YZ]),
        card("Activity 1 (Reading)",
             "Translate the sentences into English (the book glosses 好像 hǎoxiàng seem, 生气 shēng qì angry, 吓人 xiàrén scary, 显出 xiǎnchū appear, 海员 sailor, 难看 nánkàn ugly). The twelve sentences are listed here with my translations (mine):",
             examples=[D(z, e) for z, e in YZ1]),
    ],
    exercises=[
        M("What can 的样子 describe?", "Appearance, apparent mental state, a model to imitate, or a trend", ["Only a person’s name", "Only the time", "Only prices"], "Four uses."),
        M("What does 我要记住你的样子 mean?", "I want to remember how you look", ["I want to be like you", "I want to forget you", "I want to see you tomorrow"], "pronoun + 样子."),
        M("What does 照我的样子打球 mean?", "Play ball the way I do", ["Look at me playing", "I play ball like you", "Don’t play ball"], "standard for imitation."),
        M("What does 好像要下雨的样子 mean?", "It looks like it’s going to rain", ["It rained yesterday", "It never rains", "The rain is over"], "condition or trend."),
        M("What does 他看起来很着急的样子 mean?", "He looks very anxious", ["He is not in a hurry", "He is late", "He is angry"], "apparent mental state."),
        M("What does 他没有要停下来的样子 mean?", "He shows no sign of stopping", ["He stopped", "He is very tired", "He is leaving"], "没有…的样子."),
        M("What does 他走路的样子像个海员 mean?", "The way he walks is like a sailor’s", ["He is a sailor", "He walks to the sea", "He walks every day"], "海员: sailor."),
        M("What does 你好像很累的样子 mean?", "You look very tired", ["You are very hungry", "You don’t want to go", "You are not tired"], "好像…的样子."),
        F("你笑的___子真好看。", "样", PART, "样子: look."),
        F("他好像很有钱的样___。", "子", PART, "样子."),
    ],
)

# ------------------------------------------------------------------ 3. resultative complement 到
DAO = [("我回到家就上床睡觉了。", "As soon as I got home I went to bed."), ("我昨天晚上看电视看到十二点半。", "Last night I watched TV until 12:30."), ("把碗和筷子放到桌子上去。", "Put the bowls and chopsticks on the table."), ("甲：你买到车票了吗？", "Did you manage to buy a ticket?"), ("乙：我没有买到星期五的票，买到星期六的了。", "I couldn’t get a Friday ticket; I got a Saturday one.")]
DAO3 = [("甲：你们照相照完了没有？饭菜都做好了，要吃饭了。", "Have you finished taking pictures? The meal is all prepared; it’s time to eat."), ("乙：照完了。我把照相机收好就来。", "Done. I’ll come as soon as I put the camera away."), ("甲：那袋糖放哪儿了？你妹妹找不到。", "Where did the bag of sweets go? Your sister can’t find it."), ("乙：我已经吃完了。", "I’ve already finished it."), ("甲：你都吃完了？", "You finished it all?"),
        ("乙：对不起。我想再去买一袋的，可是没买到。那种糖已经卖完了。", "Sorry. I wanted to go buy another bag, but I couldn’t get any. That kind of candy is sold out."), ("甲：小文，那本书你买到了吗？", "Xiaowen, did you get that book?"), ("乙：没买到。我去书店的时候，已经卖完了。", "No. By the time I went to the bookstore, it was sold out."), ("甲：我跟大年说好了，今天下课以后去东风书店看看。你跟我们一起去吧。", "I’ve arranged with Danian to go to Dongfeng Bookstore after class today. Come with us.")]
DAO4 = [("我做完作业就到。", "I’ll be there as soon as I finish my homework."), ("集合完以后我就到。", "I’ll be there after the formation."), ("我找不到我们都喜欢的啤酒。卖完了！", "I can’t find the beer we both like. It’s sold out!"), ("我女朋友找到鞋子，我们就到。", "We’ll be there as soon as my girlfriend finds her shoes."), ("对不起，我可能会晚一点儿。我修好电脑就到。", "Sorry, I’ll be a little late. I’ll be there as soon as I get my computer fixed."), ("我太太在做饭。她做好这个菜，我们就到。", "My wife is cooking. We’ll be there once she gets this dish cooked."), ("我还没有找到我的手机。", "I haven’t found my phone yet. (my own extra reason)")]
L3 = lesson(
    "Lesson 13 Presentation 3 grammar: the resultative complement 到",
    "回到家 · 看到十二点半 · 放到桌子上去 · 买到车票",
    requires=[],
    cards=[
        card("Resultative Complement 到",
             "The resultative complement 到 indicates that the action of the verb preceding the complement reaches a given point, in either space or time. In its extended meaning, it also indicates successfully acquiring something. Affirmative: Subj. + Verb + 到 + Obj. Negative: Subj. + 没（有）+ Verb + 到 + Obj.",
             examples=[D(z, e) for z, e in DAO]),
        card("Activities 2 and 3",
             "Activity 2 (Listening). Listen to four short dialogs: 1. What was the male speaker’s request? 2. When will the phone call be made and to which number? 3. Is there an airplane present? How can you tell? 4. What is the male speaker’s problem and its cause? (Audio, not included.) Activity 3 (Reading). Read the short dialogs and complete the sentences using verbs with the correct resultative complements 完, 好 and 到, including negative forms. The book leaves the blanks; my completed dialogs:",
             examples=[D(z, e) for z, e in DAO3]),
        card("Activity 4 (Writing and Reading)",
             "小文 is texting his friend to see when they will arrive for a potluck meal. Translate the responses into Chinese using the appropriate resultative complement, then add more of your own: 1. I will be there as soon as I finish my homework. 2. I will be there after the formation. 3. I cannot find the beer we both like. It’s sold out! 4. We will be there as soon as my girlfriend finds her shoes. 5. Sorry, I am running a little late. I will be there as soon as I get my computer fixed. 6. My wife is cooking. We will be there once she gets this dish cooked. 7. What other reasons might they have? My translations:",
             examples=[D(z, e) for z, e in DAO4]),
    ],
    exercises=[
        M("What does the complement 到 indicate?", "The action reaches a point in space or time, or something is successfully obtained", ["The action is negative", "The action is repeated", "The action will begin"], "到: reach / obtain."),
        M("How do you negate a verb with 到?", "没(有) + verb + 到", ["不 after 到", "没 after the object", "别 before the verb"], "没有买到."),
        M("What does 我回到家就上床睡觉了 mean?", "As soon as I got home I went to bed", ["I stayed home all day", "I couldn’t sleep", "I will go to bed later"], "回到家: arrive home."),
        M("What does 我昨天晚上看电视看到十二点半 mean?", "I watched TV until 12:30 last night", ["I watched TV at 12:30 tomorrow", "I watched TV for 12 hours", "I didn’t watch TV"], "看到十二点半: until 12:30."),
        M("What does 你买到车票了吗？ ask?", "Did you manage to get the ticket?", ["Did you sell the ticket?", "Where is the ticket?", "How much is the ticket?"], "买到: manage to buy."),
        M("What does 我没有买到星期五的票 mean?", "I didn’t manage to get a Friday ticket", ["I didn’t go on Friday", "I sold the Friday ticket", "I don’t like Friday"], "没有买到."),
        M("Which means “sold out”?", "卖完了", ["买到了", "做好了", "找到了"], "卖完: sold out."),
        M("Which fits: 我去书店的时候，书已经___了。(sold out)", "卖完", ["买到", "看到", "放到"], "卖完."),
        F("我没有___到星期五的票。", "买", PART, "买到: manage to buy."),
        F("把碗和筷子放___桌子上去。", "到", PART, "放到: put onto."),
        F("那种糖已经卖___了。", "完", PART, "卖完: sold out."),
    ],
)

# ------------------------------------------------------------------ 4. 原来
YL1 = [("你原来的短发也很可爱。", "Your original short hair was cute too."), ("这件衣服原来的价格是九百九十九块。", "This piece of clothing’s original price was 999 yuan."), ("她现在的男朋友比原来的那位有钱。", "Her boyfriend now is richer than the former one."), ("我没有变，我还是原来的我。", "I haven’t changed; I’m still the same me."), ("她原来的工资比现在高。", "Her original salary was higher than now.")]
YL2 = [("这是我原来住的地方。", "This is where I used to live."), ("我原来住在东部，几个月前才搬到这里。", "I used to live in the east and only moved here a few months ago."), ("他们原来是同学，现在是男女朋友。", "They were originally classmates; now they are boyfriend and girlfriend."), ("我父亲原来也是军人。", "My father was also a soldier originally."), ("我原来不喜欢日本菜，后来觉得日本菜很好。", "I originally didn’t like Japanese food; later I found it very good.")]
YL3 = [("原来是你！", "So it was you all along!"), ("原来你们认识？", "So you both knew each other this whole time?"), ("原来是这样！", "Oh, so it’s like that!"), ("原来你这么有钱！", "It turns out you are so rich!"), ("原来，背包里有一瓶水。", "It turned out that there was a bottle of water in the backpack.")]
YL5 = [("原来是你啊！我刚才没看出来。", "So it’s you! I didn’t recognize you just now."), ("他还住在原来的地方。", "He still lives in the same place."), ("我们学会了很多原来不懂的东西。", "We’ve learned many things we didn’t understand before."), ("原来是这样啊，那是我错了。", "Oh, so that’s how it is; then I was wrong."), ("难怪他的中文说得这么好，原来他太太是台湾人。", "No wonder his Chinese is so good; it turns out his wife is from Taiwan."),
       ("我还是原来的我。", "I’m still the same me."), ("我说夜里怎么这么冷，原来是下雪了。", "I wondered why it was so cold at night; it turns out it was snowing."), ("我原来不习惯这里的生活，现在好多了。", "I originally wasn’t used to life here; now it’s much better."), ("几十年过去了，我的老家还是原来的样子。", "Decades have passed and my hometown still looks the way it used to.")]
L4 = lesson(
    "Lesson 13 Presentation 3 grammar: 原来",
    "原来的 · 我原来住在东部 · 原来是你！ · 原来，背包里有一瓶水",
    requires=[],
    cards=[
        card("原来",
             "原来 means “original” or “former” as an adjective, and “originally” as an adverb. As an adverb it can also mean “all along” or “as it turns out” and indicates a sudden realization of something previously unknown. As an adjective: 原来 + 的 + Noun. As an adverb: Subj. + 原来 + Predicate. As “all along”: 原来 + New/True Information. The book’s examples with numbers are spelled out here (999 is 九百九十九).",
             examples=[D(z, e) for z, e in YL1] + [D(z, e) for z, e in YL2] + [D(z, e) for z, e in YL3]),
        card("Activity 5 (Reading and Speaking)",
             "Translate the following sentences into English, then pair up and compare answers (the book glosses 难怪 nánguài as “no wonder” and 我说 as “I wondered”). The book’s nine sentences, with my translations:",
             examples=[D(z, e) for z, e in YL5]),
    ],
    exercises=[
        M("What does 原来 mean as an adjective?", "Original; former", ["New", "Strange", "Only"], "原来的 + noun."),
        M("What does 原来 mean as a sudden realization?", "As it turns out", ["From now on", "Very soon", "In the future"], "原来是你！"),
        M("What does 她原来的工资比现在高 mean?", "Her original salary was higher than now", ["Her salary is higher now", "She has no salary", "She earns the same"], "原来的工资."),
        M("What does 我原来住在东部 mean?", "I used to live in the east", ["I will live in the east", "I live in the east now", "I never lived in the east"], "原来 as an adverb."),
        M("What does 原来你这么有钱！ express?", "Surprise: so you are this rich", ["A question about money", "A request", "A complaint about prices"], "新信息."),
        M("What does 难怪 mean?", "No wonder", ["Why not", "Not difficult", "Maybe"], "难怪: no wonder."),
        M("What does 他还住在原来的地方 mean?", "He still lives in the same place", ["He doesn’t live there", "He moved far away", "He wants to move"], "原来的地方."),
        M("What does 几十年过去了，我的老家还是原来的样子 mean?", "After decades my hometown still looks the way it used to", ["My hometown has changed a lot", "I never went home", "Decades are too long"], "原来的样子."),
        F("你原来的短发也很可___。", "爱", PART, "可爱: cute."),
        F("我没有变，我还是原来的___。", "我", PART, "原来的我: the same me."),
        F("原来___这样！", "是", PART, "原来是这样: so that’s how it is."),
    ],
)

# ------------------------------------------------------------------ 5. 因此
YC = [("现在登机前要安检，一些人因此误了航班。", "Now there is security before boarding, and some people therefore miss their flights."), ("小文上课玩儿手机，老师因此批评了他。", "Xiaowen played with his phone in class, and the teacher therefore criticized him. (批评 pīpíng: criticize)"), ("蒙特雷很少下雨，因此气候很干旱。", "It seldom rains in Monterey, so the climate is very dry."), ("这里风景美，天气也好，因此，有很多人到这里旅游。", "The scenery here is beautiful and the weather is good, so many people come here to travel."), ("他是家里最小的儿子，因此，他得到了父母最多的爱。", "He is the youngest son in the family, so he received the most love from his parents.")]
YC6 = [("在这个小地方很难找到工作，因此很多年轻人离开这里去了大城市。", "It’s hard to find work in this small place, so many young people have left for big cities. (1→C)"), ("小文没有交作业，老师因此批评了他。", "Xiaowen didn’t hand in his homework, so the teacher criticized him. (2→B)"), ("李老师讲课讲得很好，因此同学们都喜欢上他的课。", "Teacher Li teaches very well, so the students all like his class. (3→D)"), ("她在重庆出生长大，因此她很了解这里的生活。", "She was born and raised in Chongqing, so she understands life here well. (4→F)"),
       ("他的话让大家都笑了，教室里的气氛因此轻松了很多。", "His words made everyone laugh, and the mood in the classroom became much more relaxed. (5→G)"), ("因为我有梦想，所以我一直在努力。", "Because I have a dream, I have been working hard. (6→E: 所以 goes with 因为)"), ("他一直不习惯大城市的生活，所以在离开二十年以后，他又回到了老家。", "He never got used to life in big cities, so after twenty years away he went back to his hometown. (7→A)")]
Q7 = [("你为什么参军？", "Why did you join the military?"), ("你为什么选择这个军种？", "Why did you choose this service branch?"), ("你喜欢现在的生活吗？为什么？", "Do you like your life now? Why?")]
L5 = lesson(
    "Lesson 13 Presentation 3 grammar: 因此 versus 所以",
    "现在登机前要安检，一些人因此误了航班 · 因此 · 所以",
    requires=[],
    cards=[
        card("因此",
             "因此 (literally “because of this”) means “therefore”. Its meaning is similar to 所以, but the usage is different: 因此 is more formal; 因此 can be placed directly after a subject, while 所以 can only be used at the beginning of the result clause; 所以 is compatible with 因为, whereas 因此 is not, because 因此 already includes the meaning of 因为. Patterns: Cause, 因此 + Effect; Cause, Subj. + 因此 + Effect.",
             examples=[D(z, e) for z, e in YC]),
        card("Activity 6 (Reading)",
             "Match the causes and results and complete the sentences with 因此 and 所以 as needed (both may be used in some sentences), then translate them orally. The causes: 1. 在这个小地方很难找到工作。 2. 小文没有交作业。 3. 李老师讲课讲得很好。 4. 她在重庆出生长大。 5. 他的话让大家都笑了。 6. 因为我有梦想。 7. 他一直不习惯大城市的生活。 The results: A. …，在离开二十年以后，他又回到了老家。 B. 老师…批评了他。 C. 很多年轻人…离开这里去了大城市。 D. …，同学们都喜欢上他的课。 E. …我一直在努力。 F. …她很了解这里的生活。 G. 教室里的气氛…轻松了很多。 The book prints 20 年 as digits. My matches and completions (mine):",
             examples=[D(z, e) for z, e in YC6]),
        card("Activity 7 (Writing and Speaking)",
             "A. Think about answers to the questions below. B. Pair up and share your responses; your partner then reports them to the class using 因此 sentences.",
             examples=[D(z, e) for z, e in Q7]),
    ],
    exercises=[
        M("What does 因此 mean?", "Therefore", ["Because", "However", "Although"], "因此: therefore."),
        M("Which is more formal?", "因此", ["所以", "Both are equally informal", "Neither"], "因此 is more formal."),
        M("Where can 因此 go that 所以 cannot?", "Directly after the subject of the result clause", ["At the end of a sentence", "Before 因为", "After a verb"], "Cause, Subj. + 因此 + Effect."),
        M("Which goes with 因为?", "所以", ["因此", "Both", "Neither"], "因为…所以…"),
        M("Which sentence is correct?", "因为我有梦想，所以我一直在努力。", ["因为我有梦想，因此我一直在努力。", "因为我有梦想，因此，所以努力。", "我有梦想，因为所以努力。"], "因为…所以…"),
        M("What does 蒙特雷很少下雨，因此气候很干旱 mean?", "It seldom rains in Monterey, so the climate is very dry", ["It rains a lot, so it is humid", "Monterey is a dry city but rainy", "It rains only in winter"], "因此: so."),
        M("What does 他是家里最小的儿子，因此，他得到了父母最多的爱 mean?", "He’s the youngest son, so he got the most love from his parents", ["He is the oldest son and loved", "His parents don’t love him", "He is an only son"], "因此: so."),
        M("Match: 小文没有交作业 →", "老师因此批评了他", ["同学们都喜欢上他的课", "我一直在努力", "他又回到了老家"], "2→B."),
        F("小文上课玩儿手机，老师因___批评了他。", "此", PART, "因此: therefore."),
        F("因为我有梦想，___以我一直在努力。", "所", PART, "所以: so."),
    ],
)

# ------------------------------------------------------------------ 6. 要是…就…
YS = [("我要是早十分钟出门，就不会误机了！", "If I had left ten minutes earlier, I wouldn’t have missed the flight!"), ("要是有钱的话，我就去很多国家旅行。", "If I had money, I would travel to many countries."), ("要是我去晚了，你们就先吃，不要等我。", "If I’m late, go ahead and eat; don’t wait for me."), ("你要喜欢就多吃点儿。", "If you like it, eat more."), ("我要是会游泳就好了！", "If only I could swim!")]
DV8 = [("要是我有钱，我就不用在那个图书馆工作了。", "If I had money, I wouldn’t have to work in that library. (A1)"), ("要是我不工作，我就有更多的时间学习。", "If I didn’t work, I would have more time to study. (A2)"), ("要是我有更多的时间学习，我的成绩就会好一些。", "If I had more time to study, my grades would be better. (A3)"),
       ("要是我的成绩更好，我就可以上更好的大学。", "If my grades were better, I could go to a better college. (B4)"), ("要是我上更好的大学，将来就能赚更多的钱。", "If I go to a better college, I could earn more money in the future. (B5)"), ("我现在需要钱。", "I need money now. (B6)")]
MILK = ("一个女孩走在路上，她的手里提着一桶牛奶，看起来很高兴的样子。昨天晚上，她做了一个梦，梦到自己挤了很多很多的牛奶，卖了很多很多的钱。女孩一边走一边想，这个梦要是真的就好了。她又想，如果我真有那么多钱，我应该买些什么呢？对了！我要给自己买一条漂亮的新裙子。我要是穿上漂亮的裙子，就可以和别的女孩一样去参加舞会。我要是去参加舞会的话，就可能会认识一个又帅又有钱的男孩。要是他爱上我，我们就结婚！要是能和这样的人结婚，我就……就在这时，唉，可怜的女孩！她手里的桶掉到地上，牛奶洒了一地。")
MILK_E = ("A girl is walking on the road, carrying a bucket of milk in her hand, looking very happy. Last night she had a dream: she dreamed that she milked a great deal of milk and sold it for a great deal of money. As she walked she thought, “If only this dream were true!” She also thought, “If I really had that much money, what should I buy? Oh yes! I’ll buy myself a pretty new dress. If I wear a pretty dress, I can go to the dance like other girls. If I go to the dance, I might meet a handsome and rich boy. If he falls in love with me, we’ll get married! If I can marry such a person, I will… will…” Just then, alas, poor girl! The bucket in her hand fell to the ground and the milk spilled all over.")
L6 = lesson(
    "Lesson 13 Presentation 3 grammar: 要是…就… (if…then…)",
    "要是…就… · 要是…的话 · 要是…就好了！ · 挤牛奶的女孩",
    requires=[],
    cards=[
        card("要是…就… construction (if…then…)",
             "The 要是…就… construction is a very common way to form conditional statements in Chinese. It is very similar to 如果…就… in usage and formality. Pattern: 要是 + Supposed Condition (+ 的话), Subj. + 就 + Response to the Condition. 1. The two clauses can share the same subject or have different subjects. The subject in the conditional clause can be placed either before or after 要是, but the subject in the result clause can only be placed before 就. We do not say * 要是天气不好，就我们不去海边; this is different from the subject’s location in English “if…then…”. 2. Variations: 要是 can be omitted (Sentence 1 below); 要是 can be simplified to 要 to be more colloquial (Sentence 4); “的话” may be added to the end of the conditional clause (Sentence 2); 要是…就好了！ is a fixed expression for “If only…!” (Sentence 5).",
             examples=[D(z, e) for z, e in YS]),
        card("Activity 8 (Speaking and Listening)",
             "Pair up. David is considering quitting his part-time job. Translate David’s thoughts in Column A into Chinese and read them to your partner; your partner does the same for Column B. Take notes, discuss David’s dilemma and help him reach a reasonable decision. Column A: 1. If I had money, I would not have to work in that library. 2. If I did not work, I would have more time to study. 3. If I had more time to study, my grades would be better. Column B: 4. If I had better grades, I could go to a better college. 5. If I go to a better college, I could earn more money in the future. 6. I need money now. My translations:",
             examples=[D(z, e) for z, e in DV8]),
        card("Activity 9 (Reading): 挤牛奶的女孩",
             "A. Read the story (the picture is not included); note any unknown words and guess their meanings. B. Pair up; choose the three unknown words you think are most critical for understanding the story and verify with your partner. C. Complete the sentence “要是能和这样的人结婚，我就……” and share it with the class. My completion: 要是能和这样的人结婚，我就有一个幸福的家了。",
             examples=[D(MILK, MILK_E), D("要是能和这样的人结婚，我就有一个幸福的家了。", "If I could marry such a person, I would have a happy home. (my completion)")]),
    ],
    exercises=[
        M("What does 要是…就… express?", "A condition and its result (if…then…)", ["A comparison", "A contrast (although)", "A sequence of times"], "要是 + condition, 就 + result."),
        M("Where can the subject of the result clause go?", "Only before 就", ["After 就", "At the end", "It cannot appear"], "Subj. + 就."),
        M("Which is NOT possible?", "要是天气不好，就我们不去海边。", ["要是天气不好，我们就不去海边。", "天气不好的话，我们就不去海边。", "天气要是不好，我们就不去海边。"], "The result subject cannot follow 就."),
        M("What does 要是…就好了！ express?", "“If only…!”", ["“Whenever…”", "“Unless…”", "“Even if…”"], "Fixed expression."),
        M("What does 的话 do at the end of a conditional clause?", "Marks it as a condition (“if…”)", ["Makes it a question", "Negates it", "Makes it past tense"], "…的话."),
        M("What does 你要喜欢就多吃点儿 mean?", "If you like it, eat more", ["If you eat, you will like it", "Eat less", "Don’t eat if you like it"], "要 = 要是."),
        M("What does 我要是会游泳就好了！ mean?", "If only I could swim!", ["I can swim well", "I will learn to swim", "I don’t want to swim"], "要是…就好了."),
        M("What did the girl dream about?", "Milking a lot of milk and selling it for lots of money", ["Going to a ball", "Buying a house", "Becoming a teacher"], "梦到自己挤了很多很多的牛奶，卖了很多很多的钱。"),
        M("What did she plan to buy first?", "A pretty new dress", ["A house", "A cow", "A car"], "我要给自己买一条漂亮的新裙子。"),
        M("What happened at the end of the story?", "The bucket fell and the milk spilled", ["She married a rich boy", "She went to the dance", "She sold the milk"], "牛奶洒了一地。"),
        F("要是我有钱，我___不用在那个图书馆工作了。", "就", PART, "要是…就…"),
        F("要是有钱的___，我就去很多国家旅行。", "话", PART, "…的话: if."),
        F("我要是早十分钟出门，就不会___机了！", "误", PART, "误机: miss the flight."),
    ],
)

# ------------------------------------------------------------------ 7. skill integration
SOT = ("离开德国的时候，我的朋友索提亚到慕尼黑机场送我。因为我的德语不太好，所以他和我一起去办理了登机手续，把行李也托运了。我跟他说了再见，然后自己去安检。没想到，我在这里遇到了麻烦。工作人员让我打开箱子检查。原来，里面有几把我在德国买的小刀。工作人员说，这样的东西只能托运，不能随身带上飞机。我想，那就只能在机场找一个邮局寄回国了。我离开了安检，可是不知道机场有没有邮局，而且飞机快起飞了。正在着急的时候，我看见索提亚向我走来！原来，他想看到我过了安检再走。我在安检处排了那么长时间的队他也没有离开。我赶紧把小刀都给了他，说：“留下一把你最喜欢的，剩下的寄给我！”回国以后不久，我就收到了从德国寄来的几把精美的小刀。")
SOT_E = ("When I left Germany, my friend Sotiya came to Munich airport to see me off. Because my German isn’t very good, he went with me to check in and checked my luggage too. I said goodbye to him and then went to security by myself. Unexpectedly, I ran into trouble here. The staff asked me to open my suitcase for inspection. As it turned out, inside there were several knives I had bought in Germany. The staff said that such things can only be checked, not carried onto the plane. I thought, then I can only find a post office in the airport and mail them home. I left security, but I didn’t know whether the airport had a post office, and the plane was about to take off. While I was anxious, I saw Sotiya walking toward me! As it turned out, he had wanted to see me through security before leaving. He hadn’t left even though I had stood in line at security for so long. I hurried to give him all the knives and said: “Keep the one you like best and mail the rest to me!” Not long after I returned home, I received several exquisite knives mailed from Germany.")
Q3 = [("“我”的工作是什么？", "What is the narrator’s job?"), ("“我”为什么那么晚才到机场？", "Why did the narrator get to the airport so late?"), ("“我”是怎么办登机手续的？", "How did the narrator check in?"), ("“我”有几件托运行李？几件随身带的行李？", "How many checked and carry-on pieces?"), ("安检的地方排队的人多吗？", "Were there many people lining up at security?"), ("“我”在安检有什么麻烦吗？", "Did the narrator have trouble at security?"), ("“我”的鞋子怎么了？", "What happened to the narrator’s shoes?"), ("广播里说的是什么？", "What did the announcement say?"), ("“我”有没有赶上飞机？", "Did the narrator catch the plane?")]
ST1 = ("一个年轻人一大早要去赶火车，因为怕时间来不及，他想走一条最短的路，就是农场的一条小路。他问农场的主人：“我可以从你的农场过一下吗？这样可以快一点儿，因为我要坐早上六点的火车。”农场主说：“当然可以！要是我农场里的公牛发现了你，就是早上五点的火车你都能赶上！”")
ST1_E = ("A young man had to catch a train early in the morning. Afraid there wouldn’t be enough time, he wanted to take the shortest route, a path through a farm. He asked the farm’s owner: “May I pass through your farm? That would be a bit faster, because I’m taking the six o’clock train in the morning.” The farmer said: “Of course! If the bull on my farm spots you, you could catch even the five o’clock train!”")
ST2 = ("王先生在生活小事上非常粗心。有一次他需要到美国去开会，他提前两个小时就到了机场，心里想，这次一定不会误机了。他轻松地走到航空公司的服务台边，说：“请给我办理登机手续。”值机员认真地看了看他的机票，说：“对不起，先生，您错过您的航班了。”他惊讶地说：“这不可能！飞机提前起飞了吗？”值机员说：“很抱歉。您的航班昨天就起飞了。”")
ST2_E = ("Mr. Wang is very careless about small things in life. Once he had to go to the United States for a meeting; he arrived at the airport two hours early and thought, “This time I’m surely not going to miss the flight.” He walked easily up to the airline’s service desk and said: “Please check me in.” The check-in agent looked carefully at his ticket and said: “Sorry, sir, you’ve missed your flight.” He said in surprise: “That’s impossible! Did the plane take off early?” The agent said: “I’m very sorry. Your flight took off yesterday.”")
L7 = lesson(
    "Lesson 13 Presentation 3: skill integration",
    "索提亚送我 · 小刀 · 农场的公牛 · 王先生错过航班",
    requires=[],
    cards=[
        card("Activity 1 (Listening and Speaking)",
             "A. Listen to Dialog 1 and answer: 1. The passenger had to leave items behind at the security point; what are they? 2. What options did the passenger have with these items? 3. What did the passenger decide, and why? B. Listen to Dialog 2 and answer: 1. What does the security officer ask the passengers to do at the beginning? 2. What did the officer find in one passenger’s bag? 3. Why can’t this item be brought onto the plane? Pair up and compare. (Audio, not included.)"),
        card("Activity 2 (Reading): at Munich airport",
             "A. Read the passage; mark any unknown word and guess its meaning. B. Write three unknown words critical to your understanding; pair up and discuss their meanings, checking your dictionary for disagreements. C. Using the passage, listen to seven statements and mark each true or false (audio, not included).",
             examples=[D(SOT, SOT_E)]),
        card("Activity 3 (Listening, Reading and Speaking)",
             "A. Listen to the passage; transcribe any unknown words you hear and look up their meanings (audio, not included). B. Answer the following questions, then pair up and discuss your answers in Chinese:",
             examples=[D(z, e) for z, e in Q3]),
        card("Activity 4 (Reading, Speaking and Listening): Story 1",
             "A. Pair up. Each partner reads one of the two stories and answers the questions that follow. Story 1 questions: 1. Why does the young man want to take a short cut? 2. Where does the short cut go? 3. Will the young man take the short cut? Why? (Mine: 1. He is afraid he won’t catch the six o’clock train. 2. Through a path across a farm. 3. Probably not, because of the bull.)",
             examples=[D(ST1, ST1_E)]),
        card("Story 2",
             "Story 2 questions: 1. Has Mr. Wang missed his flight before? How do you know? 2. What is Mr. Wang’s mistake this time? (Mine: 1. Probably yes: the text says he is careless and thinks 这次一定不会误机了, “this time I surely won’t miss it”. 2. He came on the wrong day; his flight left yesterday.) B. Explain three critical words in your passage to your partner, then retell the story; let your partner answer the questions you did and compare.",
             examples=[D(ST2, ST2_E)]),
    ],
    exercises=[
        M("Who saw the narrator off at Munich airport?", "His friend Sotiya", ["His teacher", "His mother", "A colleague"], "我的朋友索提亚到慕尼黑机场送我。"),
        M("Why did Sotiya go with him to check in?", "His German wasn’t very good", ["He was lost", "He had no ticket", "He was late"], "因为我的德语不太好."),
        M("What did security find in the suitcase?", "Several small knives", ["Bottles of water", "Medicine", "A laptop"], "里面有几把我在德国买的小刀。"),
        M("What did the staff say about the knives?", "They can only be checked, not carried on", ["They are illegal everywhere", "They must be thrown away", "They need a visa"], "这样的东西只能托运，不能随身带上飞机。"),
        M("Why did Sotiya stay?", "He wanted to see the narrator through security", ["He missed his bus", "He had to work", "He forgot his phone"], "他想看到我过了安检再走。"),
        M("What did the narrator do with the knives?", "Gave them to Sotiya to keep and mail", ["Mailed them from the airport", "Threw them away", "Checked them in"], "我赶紧把小刀都给了他."),
        M("What did the narrator receive after returning home?", "Several fine knives mailed from Germany", ["A letter", "A bag of candy", "A ticket"], "收到了从德国寄来的几把精美的小刀。"),
        M("Why does the young man want to cut across the farm?", "To get to the station faster", ["To see the farm", "To buy milk", "To visit the owner"], "这样可以快一点儿。"),
        M("What is the farmer’s joke?", "If the bull sees you, you could catch an earlier train", ["The bull is friendly", "The train is late", "The path is closed"], "就是早上五点的火车你都能赶上！"),
        M("What is Mr. Wang’s mistake?", "His flight left yesterday", ["He lost his passport", "He went to the wrong airport", "He arrived too late today"], "您的航班昨天就起飞了。"),
        M("How early did Mr. Wang arrive?", "Two hours early", ["Ten minutes early", "At the last minute", "One day early"], "提前两个小时就到了机场。"),
        mean("粗心", "cu1 xin1", "careless", ["anxious", "very quick", "formal"]),
    ],
)

# ------------------------------------------------------------------ 8. using Chinese in context
POST = ("经常坐飞机的人都知道，乘坐飞机一定要在航班起飞前三十分钟办理登机手续。这是为什么呢？首先我们要知道，什么是起飞时间。起飞时间是飞机关机门的时间，而不是飞机离地升空的时间。在停止办理登机手续到关机门之间，机场的工作人员还有很多工作要做。比如：1. 把旅客托运的行李装上飞机，2. 对办完登机手续的旅客进行安全检查，3. 让旅客到指定的登机口检票登机，4. 检查飞机上旅客的人数，看和地面检票人数是不是一样。按规定，一百座以下的飞机要在起飞前六十分钟就开始办理登机手续，一百座以上的飞机要提前九十分钟开始办理登机手续。因此，请旅客们一定要提前到机场办理登机手续。办完登机手续以后，还要及时进行安全检查，并到登机口候机。")
POST_E = ("Those who often fly know that to take a plane you must check in 30 minutes before the flight takes off. Why is that? First we need to know what the takeoff time is. The takeoff time is the time the plane’s door is closed, not the time the plane leaves the ground. Between the end of check-in and the closing of the door, airport staff still have a lot of work to do, for example: 1. load passengers’ checked luggage on the plane; 2. carry out security checks on passengers who have finished check-in; 3. have passengers check their tickets and board at the designated gate; 4. check the number of passengers on the plane against the number checked at the gate. By regulation, check-in for planes with fewer than 100 seats begins 60 minutes before takeoff, and for planes with more than 100 seats 90 minutes before takeoff. Therefore, passengers must arrive early at the airport to check in. After check-in you still must go through the security check in good time and wait at the boarding gate.")
SEC = [("请把装液体的袋子拿出来，放在盘子里。", "Take out your bag of liquids and put it in the tray."), ("请把皮带摘下来，放在盘子里。", "Take off your belt and put it in the tray."), ("请把鞋子和外套脱下来，放在盘子里。", "Take off your shoes and coat and put them in the tray."), ("请把手表摘下来，放在盘子里。", "Take off your watch and put it in the tray."), ("请把口袋里的东西都拿出来。", "Take everything out of your pockets."), ("请把电脑从箱子里拿出来。", "Take your computer out of your suitcase.")]
BOARD = ["你喜欢靠窗户的座位还是靠过道的座位？", "你住的地方附近有国际机场吗？", "你上次坐飞机是从哪儿到哪儿？", "你喜欢哪家航空公司？为什么？", "你坐过几次飞机？", "你喜欢坐飞机还是坐火车？为什么？", "你会在飞机上睡觉吗？", "你上次坐飞机是什么时候？", "你上次排队是做什么？", "头等舱和经济舱有什么不一样？", "你喜欢飞机上的食物吗？", "你在网上办登机手续还是在机场办？",
         "你有护照吗？是什么时候办的？", "你今年会坐飞机去哪儿？", "飞机票为什么很贵？", "机票和登机牌有什么不一样？", "坐飞机出国需要带什么证件？", "在美国托运行李需要付钱吗？", "你在飞机上会做什么？", "哪些东西不能随身带上飞机？说两种。", "为什么需要行李牌？", "你会提前多长时间到机场？", "在机场安检时旅客需要做什么？", "你最想坐飞机去哪个国家？",
         "你误过航班吗？", "你喜欢在机场商店买东西吗？", "哪些物品需要报关？", "怎样办理登机手续？", "你坐飞机换过座位吗？", "美国人去哪些国家不需要签证？"]
L8 = lesson(
    "Lesson 13 Presentation 3: using Chinese in context",
    "为什么要提前办理登机手续？ · 安检提示 · 机场问答棋",
    requires=[],
    cards=[
        card("Activity 1 (Reading and Speaking)",
             "Why is the check-in gate closed before the departure time of the flight? Read this online post (from blog.sina.com.cn/ceayoung) and report to your partner. The book prints the numbers as digits (30, 100, 60, 90); they are spelled out here.",
             examples=[D(POST, POST_E)]),
        card("Activity 2 (Speaking)",
             "Pair up. You play the airport security officer and your partner the passenger, then switch roles. The book’s prompts are in English; a Chinese version of each (mine):",
             examples=[D(z, e) for z, e in SEC]),
        card("Activities 3 and 4",
             "Activity 3 (Writing). Have you ever had to endure a long wait at the airport security checkpoint? Here is a tip on how to speed up the security check for your next trip: watch the video “Speedy Security!” and transcribe what you hear as a tip for your Chinese friends. (Video, not included.) Activity 4 (Writing, Speaking and Listening). A. Work in three groups. The first group acts as the airport check-in agent and the second as the security officer; each comes up with a list of reminders for passengers. For the third group, your cousin is going to fly for the first time to visit you; give him a list of things to pay attention to about check-in, luggage and the security check. B. Each group reports its list to the class; compare and help the third group refine its list for the cousin."),
        card("Activity 5 (Reading and Speaking): question board",
             "Pair up. Each player rolls the dice twice, the first time for the horizontal line and the second for the vertical line; wherever the dice land, answer the question in that square. If it lands on the “Ask any question!” square, answer any question your partner asks. The board is a 6 by 6 grid with several “Ask any question!” squares; its text is laid out in the book as a picture, so I list the questions below in reading order, which may differ from the grid order:",
             examples=[D(z, "(a board question; the book gives no translation)") for z in BOARD[:10]] + [D(z, "(a board question)") for z in BOARD[10:]]),
    ],
    exercises=[
        M("What counts as the takeoff time?", "The time the plane’s door closes", ["The time the plane leaves the ground", "The time the passengers arrive", "The time the gate opens"], "起飞时间是飞机关机门的时间。"),
        M("When should you check in, according to the post?", "At least 30 minutes before takeoff", ["Exactly at takeoff", "10 minutes after boarding", "One day before"], "起飞前三十分钟办理登机手续。"),
        M("How early does check-in begin for planes with under 100 seats?", "60 minutes before takeoff", ["30 minutes", "90 minutes", "120 minutes"], "一百座以下的飞机要在起飞前六十分钟."),
        M("How early does check-in begin for planes with over 100 seats?", "90 minutes before takeoff", ["60 minutes", "30 minutes", "15 minutes"], "一百座以上的飞机要提前九十分钟."),
        M("Which is NOT one of the staff’s tasks between check-in close and door close?", "Selling tickets at the counter", ["Loading checked luggage", "Security-checking checked-in passengers", "Counting boarded passengers"], "Four listed tasks."),
        M("What does 候机 mean?", "To wait at the gate for boarding", ["To book a flight", "To print a ticket", "To land"], "到登机口候机."),
        M("What does 请把鞋子和外套脱下来 ask you to do?", "Take off your shoes and coat", ["Put on your shoes", "Weigh your shoes", "Wash your coat"], "脱下来: take off."),
        M("What does 你误过航班吗？ ask?", "Have you ever missed a flight?", ["Do you like flights?", "Is your flight delayed?", "Have you booked a flight?"], "误: miss."),
        M("What does 头等舱和经济舱有什么不一样？ ask?", "What’s the difference between first and economy class?", ["Which cabin is cheaper?", "Where is first class?", "Which class do you like?"], "头等舱 / 经济舱."),
        mean("候机", "hou4 ji1", "to wait for boarding", ["to check luggage", "to fly", "to show a passport"]),
        F("起飞时间是飞机关机___的时间。", "门", PART, "机门: aircraft door."),
        F("请旅客们一定要提前到机场办理登机手___。", "续", PART, "手续: procedure."),
    ],
)

L9 = vocab_lesson("Lesson 13 Presentation 3 vocabulary", "26 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC3)

# ------------------------------------------------------------------ 10. Area Studies
AX = [("Passengers per year", "up to 45 million by 2021; 100 million in the future"), ("Terminal area", "700,000 square meters; ground transportation center 80,000 square meters"), ("Runways", "four now; seven eventually"), ("Aircraft terminals (gates)", "79 now"), ("Flights per year", "over 620,000 eventually"), ("Maximum walk from the center to a gate", "about 8 minutes"), ("Check-in self-service points", "400"), ("Customs clearance (before)", "5 to 7 minutes; now no waiting for most passengers"), ("Inspection waiting time", "reduced by 50%")]
L10 = lesson(
    "Lesson 13 Area Studies: Beijing Daxing International Airport (PKX)",
    "北京大兴国际机场 · 海星 · 凤凰 · 感应式通关",
    requires=[],
    cards=[
        card("Beijing Daxing International Airport (PKX)",
             "Beijing Daxing International Airport (PKX), also known as Beijing New Airport, is one of the largest airport terminals in the world. It is one of two international airports for Beijing, along with Beijing Capital International Airport. This new airport is located south of the Daxing District (the southern suburbs of Beijing). This new mega-airport hub is expected to handle up to 45 million passengers per year by 2021, and to reach an amazing 100 million passengers per year in the future. Daxing airport’s exotic shape has earned it the nickname “The Starfish.” It is of enormous dimensions with a vast terminal covering 700,000 m²; with a ground transportation center extending 80,000 m². Currently Daxing Airport has four runways and 79 aircraft terminals. Eventually the airport will have 7 runways and be able to serve over 620,000 flights per year.",
             tables=[table(["Fact", "Figure from the reading"], [(a, b) for a, b in AX], title="Key facts")]),
        card("Layout and design",
             "Passengers can go to the central terminal, where all the shops and facilities are located, and then head to their departure gates, situated in one of the corridors. Despite the huge size of the airport, the walking distance between the center and each gate is short. Passengers can shop and wander around care-free, knowing that their gate is only 8 minutes away at maximum. For passengers with long layovers between flights, the airport has a hotel, lounges, restaurants and even a 24-hour fitness center. Daxing Airport’s design is inspired by Chinese tradition and culture. Typical Chinese touches are combined with futuristic elements. While five outdoor traditional Chinese gardens adorn the five corridors, the airport’s shape can be compared to a giant phoenix, a very characteristic Chinese symbol. (Photographs from cctv.com.cn are not included.)"),
        card("Speed and smart services",
             "At Daxing Airport, speed is the priority. 5-G based technology and smart services cut down on waiting time. Facial recognition procedures make paper tickets unnecessary and 400 self-service points make checking in a breeze. Self-service baggage processes also help to optimize the traveller’s experience. You can track your luggage with E-tag technology. Daxing Airport has built intelligent customs, or “inductive customs clearance” that serves passengers with no waiting time. In the past when entering the country, passengers had to form long lines to pick up luggage and then pass through a machine inspection. Customs clearance times could be as long as 5 to 7 minutes. At Daxing International Airport (except for a small number of key passengers and luggage that need to enter the inspection area for customs inspection) most passengers no longer need to carry their luggage or line up to go through machine inspection."),
        card("Combined inspection",
             "The customs and the security inspection departments share the inspection site and combine both customs inspection of luggage and items with the security inspection process. In this way, two “checkpoints” for customs inspection and airport security are combined. Passengers only need to check in their baggage once when leaving the country and go through only one inspection. The waiting time for inspections can be reduced by 50%. When unpacking and inspection is required, the customs and security inspections use separate inspection rooms, which provide more complete protection for passengers’ privacy. References: Wikipedia, Beijing Daxing International Airport; CCTV, Newly Completed Daxing Airport from Inside."),
    ],
    exercises=[
        M("Which other international airport serves Beijing?", "Beijing Capital International Airport", ["Hongqiao", "Pudong", "Baiyun"], "Along with Beijing Capital."),
        M("Where is Daxing airport?", "South of the Daxing District, in Beijing’s southern suburbs", ["North of Beijing", "In Tianjin", "In the city center"], "Located south of the Daxing District."),
        M("What is Daxing airport’s nickname?", "The Starfish", ["The Dragon", "The Crane", "The Eagle"], "“The Starfish.”"),
        M("What can the airport’s shape be compared to?", "A giant phoenix", ["A dragon", "A butterfly", "A pagoda"], "A giant phoenix."),
        M("How many outdoor traditional Chinese gardens are there?", "Five, one for each corridor", ["One", "Three", "Ten"], "Five outdoor gardens adorn the five corridors."),
        M("How many runways does Daxing have now?", "Four", ["Seven", "Two", "Ten"], "Currently four; eventually seven."),
        M("How long is the maximum walk from the center to a gate?", "About 8 minutes", ["About 30 minutes", "About 2 minutes", "About an hour"], "Only 8 minutes away at maximum."),
        M("What does facial recognition make unnecessary?", "Paper tickets", ["Passports", "Luggage", "Security officers"], "Facial recognition procedures make paper tickets unnecessary."),
        M("How many self-service check-in points does it have?", "400", ["40", "4,000", "14"], "400 self-service points."),
        M("By how much can inspection waiting time be reduced?", "50%", ["5%", "25%", "90%"], "Reduced by 50%."),
        M("What do the customs and security departments share?", "The inspection site", ["Their uniforms", "Their luggage tags", "Their gate"], "They share the inspection site."),
        M("Why are separate inspection rooms used for unpacking?", "To protect passengers’ privacy", ["To save electricity", "To make it faster", "Because of lack of space"], "More complete protection for passengers’ privacy."),
    ],
)

UNIT = unit("第十三课 人在机场 Presentation 3: security, 的样子, 到, 原来, 因此, 要是…就…, and Area Studies", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
