"""Unit 42: Lesson 15 (Social Gathering) Presentation 1 from the book's texts: the housewarming phone call, 刚 and 刚才,
compound directional verbs as complements, 一…就…, the complement of potentiality (1), verb duplication, the skill-integration
and using-Chinese activities (invitations, emails, the picnic and the New Year flyer) and the vocabulary list. Audio, pictures
and the flyer artwork are not included; the book writes numbers as digits and they are spelled out here so every spoken line
is Chinese; answer keys the book does not print are mine."""
from zh_auto import *
from zh_l15_vocab import VOC1

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("来得了", 2, "liao3"), ("来不了", 2, "liao3"), ("吃不了", 2, "liao3"), ("干完", 0, "gan4"), ("教官", 0, "jiao4"), ("教过", 0, "jiao1"), ("不教你们", 1, "jiao1"), ("没收到", 0, "mei2"), ("找得到", 1, "de5"),
                          ("得每天", 0, "dei3"), ("得把", 0, "dei3"), ("得做", 0, "dei3"), ("得先", 0, "dei3"), ("睡觉", 1, "jiao4"), ("睡什么觉", 3, "jiao4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. dialog
P1 = [("老张", "喂，王文吗？", "Hello, is that Wang Wen?"), ("王文", "是我，你是老张吧？", "Speaking. You’re Lao Zhang, right?"), ("老张", "对，你周六下午有空儿吗？", "Yes. Do you have time on Saturday afternoon?"),
      ("王文", "有空儿啊，有什么事吗？", "Yes, why, is something up?"), ("老张", "我们刚搬了新家，想请几个朋友来我家聚聚，热闹热闹。", "We just moved into a new home and would like to invite a few friends over to get together and liven things up."),
      ("王文", "你买新房子啦！恭喜恭喜，我一定去。什么时候买的？", "You bought a new house! Congratulations, I’ll definitely come. When did you buy it?"), ("老张", "十月份，刚装修完，上星期才搬进来。", "In October. We just finished renovating and only moved in last week."),
      ("王文", "哦，新房子在哪儿？", "Oh, where is the new house?"), ("老张", "就在市图书馆旁边，刚才我已经把地址发给你了，你看看收到没有？", "Right next to the city library. I just sent you the address; take a look whether you received it."),
      ("王文", "收到了。聚会什么时候开始？", "Got it. When does the party start?"), ("老张", "三点左右吧。大家聊聊天，然后在我家吃顿便饭。", "Around three. We’ll chat and then have a simple meal at my place."),
      ("王文", "啊，糟糕，我刚想起来，星期六下午我有一场乒乓球比赛，不知道三点赛得完赛不完。", "Oh no, I just remembered, on Saturday afternoon I have a table tennis match and I don’t know whether it will be over by three."),
      ("老张", "赛不完没关系，你可以晚点儿来，我们等你。", "It doesn’t matter if it isn’t over; you can come a bit later, we’ll wait for you."), ("王文", "那好，我一赛完就去。", "Good, I’ll go as soon as the match is over."), ("老张", "好，就这么定了。星期六见。", "Fine, it’s settled. See you Saturday.")]
CAT = [("房子", "搬家、装修、地址"), ("聚会", "便饭、聚聚、热闹、顿"), ("活动", "乒乓球、比赛"), ("其他", "发给、收到、定了、恭喜、糟糕")]
EC = [("to have free time", "有空儿"), ("to congratulate a person", "恭喜"), ("to be unsure if something can be done by a certain time", "赛得完赛不完"), ("a deal", "就这么定了"), ("to invite friends over for a party", "请朋友来聚聚"), ("to have recently sent someone something", "刚才把地址发给你了"), ("to do something as soon as something else is done", "一赛完就去"), ("to have just finished doing something", "刚装修完")]
L1 = lesson(
    "Lesson 15 Presentation 1: a housewarming invitation",
    "第十五课 社交聚会 · 请几个朋友来我家聚聚 · 就这么定了",
    requires=[],
    cards=[
        card("Learning objectives and Getting Started",
             "Lesson 15 Social Gathering. After this lesson you can obtain information about inviting guests to a party and narrate how to invite friends; obtain information about what happens at a party and narrate such an event; obtain information about a picnic and narrate such an event. You must master the new words, the adverbs 刚 and 刚才, directional verb combinations used as complements, the 一…就… construction, the complement of potentiality (1) and (2), verb duplication, the 想 + V + 什么 + 就 + V + 什么 construction, the verb 让, the V + 来 + V + 去 construction, the 不…不… construction, the adverbial modifier marker 地, the aspect particle 着 and the 一直…才… construction. Getting Started. Pair up and discuss: A. How would an American typically celebrate a recent move into a new home? B. How would you invite your friends to a party at your new home? (Photographs not included.)"),
        card("Presentation 1: 请朋友来新家",
             "The book also prints the dialog in traditional characters.",
             examples=dlg(P1)),
        card("Activities 1 and 2",
             "Activity 1 (Listening and Speaking). A. Choose the correct answers: 1. What is true about Lao Zhang and Wang Wen? (They are neighbors / They often play ping pong together / They are friends.) 2. What is Lao Zhang’s plan? (To celebrate with friends once he has moved / To invite friends over for a party at his new home / To eat a simple meal with friends and then go play ping pong.) B. Detailed listening: 1. Why did Lao Zhang call Wang Wen? 2. What did you hear about Lao Zhang’s new home? 3. Would Wang Wen be able to get to Lao Zhang’s home on time? Why? (Audio, not included. From the text: they are friends; he wants to invite friends to a party at the new home; he is not sure, since he has a table tennis match.) Activity 2 (Reading, Writing, and Speaking). A. Read the words (便饭, 发给, 地址, 定了, 恭喜, 搬家, 乒乓球, 收到, 比赛, 热闹, 糟糕, 聚聚, 装修, 顿) and write each in the correct category of the table (词汇: 房子, 聚会, 活动, 其他). My sorting (mine):",
             tables=[table(["Category", "Words"], [(a, b) for a, b in CAT], title="词汇 (mine)", say=[0, 1])]),
        card("Activity 2 B: English to Chinese",
             "B. Pair up and share your work; ask each other what Chinese expressions describe the actions below and fill in what you are told. The book leaves the Chinese blank; my answers (mine, from the dialog):",
             tables=[table(["English", "Chinese"], [(a, b) for a, b in EC], title="Expressions", say=[1])]),
    ],
    exercises=[
        M("Who is calling whom?", "Lao Zhang is calling Wang Wen", ["Wang Wen is calling Lao Zhang", "A teacher calls a student", "A shop calls a customer"], "老张: 喂，王文吗？"),
        M("Why is Lao Zhang inviting friends?", "They just moved into a new home", ["It is a birthday", "It is a wedding", "It is a farewell party"], "我们刚搬了新家。"),
        M("When did Lao Zhang buy the house?", "In October", ["Last week", "Yesterday", "Next year"], "十月份."),
        M("When did they move in?", "Last week", ["In October", "Tomorrow", "Two years ago"], "上星期才搬进来。"),
        M("Where is the new house?", "Next to the city library", ["Next to a school", "Downtown", "At the airport"], "就在市图书馆旁边。"),
        M("What time does the party begin?", "Around three", ["Around noon", "Around eight", "Around midnight"], "三点左右。"),
        M("What will the guests do at the party?", "Chat and have a simple meal", ["Play ping pong", "Watch a film", "Go hiking"], "聊聊天，吃顿便饭。"),
        M("Why is Wang Wen worried?", "He has a table tennis match that may not be over by three", ["He has no gift", "He doesn’t know the address", "He has to work"], "不知道三点赛得完赛不完。"),
        M("What does Lao Zhang say?", "It doesn’t matter; come later, we’ll wait", ["Then don’t come", "Bring your racket", "Cancel the party"], "你可以晚点儿来，我们等你。"),
        M("What does 就这么定了 mean?", "It’s settled", ["It is not decided", "Let’s argue", "Let’s do it again"], "定了: deal."),
        M("What does 恭喜恭喜 do?", "Congratulates twice for heartfelt happiness", ["Asks a question", "Refuses", "Says goodbye"], "Congratulations."),
        mean("糟糕", "zao1 gao1", "too bad; terrible", ["wonderful", "delicious", "cheap"], ),
    ],
)

# ------------------------------------------------------------------ 2. activity 3 and 4
M3 = [("1", "他们的新房子", "c", "十五号以前装修得完吗？", "Their new house, can the renovation be finished before the fifteenth? (c)"), ("2", "星期天的聚会，你一定来啊！", "g", "好，就这么定了。", "You must come to Sunday’s party! / Fine, it’s settled. (g)"), ("3", "糟糕，我想起来了，", "e", "下午我还要参加乒乓球比赛呢！", "Oh no, I remembered, I still have a table tennis match in the afternoon! (e)"),
      ("4", "你们的游泳比赛，", "f", "三点以前赛得完赛不完？", "Your swimming meet, can it be finished before three? (f)"), ("5", "他一到蒙特雷工作就", "b", "在那里买了一座新房子。", "As soon as he started working in Monterey he bought a new house there. (b)"), ("6", "我一搬完家", "a", "就会把新地址发给你。", "As soon as I finish moving I will send you the new address. (a)"),
      ("7", "听说你们买新房子了，", "d", "恭喜恭喜！什么时候买的？", "I heard you bought a new house, congratulations! When did you buy it? (d)")]
L2 = lesson(
    "Lesson 15 Presentation 1 activities: matching and the two dialogs",
    "他们的新房子 · 一搬完家就… · 赛得完赛不完",
    requires=[],
    cards=[
        card("Activity 3 (Reading and Speaking)",
             "A. Match the parts in Column A with the parts in Column B and write your answers in the middle column. Column A: 1. 他们的新房子 2. 星期天的聚会，你一定来啊！ 3. 糟糕，我想起来了， 4. 你们的游泳比赛， 5. 他一到蒙特雷工作就 6. 我一搬完家 7. 听说你们买新房子了， Column B: a. 就会把新地址发给你。 b. 在那里买了一座新房子。 c. 十五号以前装修得完吗？ d. 恭喜恭喜！什么时候买的？ e. 下午我还要参加乒乓球比赛呢！ f. 三点以前赛得完赛不完？ g. 好，就这么定了。 My matching (mine): 1-c, 2-g, 3-e, 4-f, 5-b, 6-a, 7-d. B. Pair up and check each other’s work; take turns translating the sentences into English and your partner translates them back into Chinese, without consulting the table. The seven joined sentences:",
             examples=[D(a + b, e) for _, a, _, b, e in M3]),
        card("Activity 4 (Listening, Speaking, and Reading)",
             "A. Pair up. Each partner listens to one of the dialogs (Dialog 1, Dialog 2) and matches it with one of three pictures. B. Take notes from your dialog in the table in English (rows: Event; Time and Location; Invitees; The Issue; Backup Plan; columns: Dialog 1, Dialog 2); then, in Chinese, ask for details about your partner’s dialog. (Audio and pictures, not included.)"),
    ],
    exercises=[
        M("Match: 他们的新房子", "十五号以前装修得完吗？", ["好，就这么定了。", "恭喜恭喜！什么时候买的？", "就会把新地址发给你。"], "1→c."),
        M("Match: 星期天的聚会，你一定来啊！", "好，就这么定了。", ["十五号以前装修得完吗？", "三点以前赛得完赛不完？", "在那里买了一座新房子。"], "2→g."),
        M("Match: 糟糕，我想起来了，", "下午我还要参加乒乓球比赛呢！", ["就会把新地址发给你。", "恭喜恭喜！", "好，就这么定了。"], "3→e."),
        M("Match: 你们的游泳比赛，", "三点以前赛得完赛不完？", ["十五号以前装修得完吗？", "下午我还要参加比赛呢！", "好，就这么定了。"], "4→f."),
        M("Match: 他一到蒙特雷工作就", "在那里买了一座新房子。", ["就会把新地址发给你。", "恭喜恭喜！", "好，就这么定了。"], "5→b."),
        M("Match: 我一搬完家", "就会把新地址发给你。", ["恭喜恭喜！什么时候买的？", "好，就这么定了。", "在那里买了一座新房子。"], "6→a."),
        M("Match: 听说你们买新房子了，", "恭喜恭喜！什么时候买的？", ["就会把新地址发给你。", "好，就这么定了。", "三点以前赛得完赛不完？"], "7→d."),
        F("你们的游泳比___，三点以前赛得完赛不完？", "赛", PART, "比赛: match."),
        F("听说你们买新房子了，恭___恭喜！", "喜", PART, "恭喜: congratulations."),
    ],
)

# ------------------------------------------------------------------ 3. 刚 and 刚才
GG = [("我刚刚做完作业。", "I have just finished my homework."), ("天刚黑。", "It has just gotten dark."), ("他刚才出去了。", "He went out just now."), ("我刚才饿了。", "I was hungry just now."), ("刚才的新闻", "the news just now"), ("我刚下班。", "I just got off work."), ("她去年刚刚上大学。", "She just started university last year."), ("他刚才给我打了个电话。", "He called me just now.")]
GG2 = [("我刚刚走到学校。", "I have just walked to the school. (1)"), ("饭刚好，你赶快吃吧。", "The meal is just ready; eat quickly. (2)"), ("他上星期刚从美国回来。", "He just came back from the U.S. last week. (3)"), ("妈妈刚才来电话了。", "Mom called just now. (4)"), ("刚才他说他搬家了。", "Just now he said he had moved. (5)"), ("他的脸刚才红了。", "His face turned red just now. (6)"), ("刚才他的脸红了。", "Just now his face turned red. (7)")]
GX = [("A", "今天你去看电影了吗？", "Did you go to the movies today? (the book’s example, cue 看电影)"), ("B", "去了，我和小王一起去看的。我们刚刚回来。", "Yes, I went with Xiao Wang. We just got back."),
      ("A", "你作业做完了吗？", "(mine, cue 做作业) Have you finished your homework?"), ("B", "刚做完，现在要去吃饭了。", "Just finished; I’m going to eat now."), ("A", "你吃晚饭了吗？", "(mine, cue 吃晚饭) Have you eaten dinner?"), ("B", "刚才吃完，你呢？", "Just now; and you?"),
      ("A", "你给妈妈打电话了吗？", "(mine, cue 打电话) Did you call Mom?"), ("B", "刚打完。她说她很好。", "Just did. She said she is fine."), ("A", "你的房间收拾好了吗？", "(mine, cue 收拾房间) Have you tidied your room?"), ("B", "刚收拾完，很干净。", "Just finished; it’s very clean."),
      ("A", "你订机票了吗？", "(mine, cue 订机票) Did you book the plane ticket?"), ("B", "刚才订好了，下周五走。", "Booked just now; leaving next Friday.")]
L3 = lesson(
    "Lesson 15 Presentation 1 grammar: the adverbs 刚 and 刚才",
    "我们刚搬了新家 · 刚才我已经把地址发给你了 · 刚 and 刚才",
    requires=[],
    cards=[
        card("Adverbs 刚 and 刚才",
             "刚 is an adverb meaning “just a short while ago.” It appears before a verb or an adjective. Sometimes 刚 is in the form 刚刚, as in 我刚刚做完作业 / 天刚黑. 刚才 is a noun expressing time and means “just now.” It can appear before a verb or an adjective, such as 他刚才出去了 / 我刚才饿了. It can also modify a noun, such as 刚才的新闻. Note: “just a short time ago”, expressed by 刚, is relative to and determined by the speaker. It can indicate that something “just” happened five seconds ago, five days ago, or even longer, such as 我刚下班 / 她去年刚刚上大学. 刚才, on the contrary, implies that the time elapsed is short, often no more than a few minutes, such as 他刚才给我打了个电话。 Patterns: Subject + 刚(刚) + Verb/Adjective; Subject + 刚才 + Verb/Adjective; 刚才 + Subject + Verb/Adjective.",
             examples=[D(z, e) for z, e in GG]),
        card("Examples 1 to 7",
             "The book’s numbered examples:",
             examples=[D(z, e) for z, e in GG2]),
        card("Activities 1 and 2",
             "Activity 1 (Listening, Speaking, and Reading). A. Listen to the dialog and complete the sentences: 1. 儿子 ___，说他 ___。 2. 今天早上 ___，说他女朋友小于要去接他呀。 3. 小于 ___！她 ___，要她马上去学校值班。 4. 下午两点半，___。 5. ___ 发给你了。你赶快去吧。 B. Pair up and share your work; determine if 刚才 can be replaced by 刚, or vice versa, in each sentence. (Audio, not included.) Activity 2 (Speaking and Writing). A. Using the example cue 看电影, write five exchanges about things you might do over the weekend with 刚(刚) and 刚才: 1. 做作业 2. 吃晚饭 3. 打电话 4. 收拾房间 5. 订机票. B. Pair up and share; take turns telling about an event not on the table, each partner writing two exchanges. The book’s example and my five exchanges (mine):",
             examples=dlg(GX)),
    ],
    exercises=[
        M("What does 刚 mean?", "Just (a short while ago)", ["Not yet", "Soon", "Always"], "刚: just."),
        M("Which is a time noun?", "刚才", ["刚", "刚刚", "刚好"], "刚才 is a noun."),
        M("Which can modify a noun?", "刚才", ["刚", "刚刚", "已经"], "刚才的新闻."),
        M("How far back can 刚 reach?", "As far as the speaker feels is recent", ["Only seconds", "Only a few minutes", "Only today"], "Relative to the speaker."),
        M("How far back does 刚才 reach?", "Often no more than a few minutes", ["Years", "Last month", "Last week"], "Short time."),
        M("Which is correct for “She just entered university last year”?", "她去年刚刚上大学。", ["她去年刚才上大学。", "她刚才去年上大学。", "刚才她去年上大学。"], "刚 can reach a year."),
        M("What does 妈妈刚才来电话了 mean?", "Mom called just now", ["Mom will call", "Mom never calls", "Mom called last year"], "刚才: just now."),
        M("What does 饭刚好，你赶快吃吧 mean?", "The meal is just ready; eat quickly", ["The meal is bad", "The meal is cold", "Don’t eat"], "刚好: just ready."),
        F("我们___搬了新家。", "刚", PART, "刚: just."),
        F("___才我已经把地址发给你了。", "刚", PART, "刚才: just now."),
    ],
)

# ------------------------------------------------------------------ 4. compound directional complements
CC1 = [("十月份，刚装修完，上星期才搬进来。", "We just finished renovating in October and only moved in last week. (搬 + 进来)")]
CC2 = [("快爬上来！", "Climb up here quickly!"), ("不要让小猫跑出去了。", "Don’t let the kitten run out."), ("从那边走过来要半个多小时。", "Walking over from there takes more than half an hour."), ("他走回来了。", "He walked back."), ("请站起来。", "Please stand up.")]
CC3 = [("小王走过马路来和我们打招呼。", "Xiao Wang walked across the road to greet us."), ("大卫非常客气，知道我们渴了，马上跑下楼去给我们拿饮料。", "David is very polite; knowing we were thirsty, he ran downstairs right away to get us drinks."), ("周末，我和几个朋友早上六点就爬上山去看日出。", "On the weekend, a few friends and I climbed up the mountain at six in the morning to see the sunrise."), ("昨天，我看见小李走进那家商店买东西。", "Yesterday I saw Xiao Li walk into that store to shop."), ("他没赶上最后一班车，只好走回学校去。", "He missed the last bus and had to walk back to school.")]
CC4 = [("他买回来很多水果。", "He bought back a lot of fruit."), ("他买回很多水果来。", "He bought back a lot of fruit. (object between)"), ("他从书包里拿出来两本新书。", "He took two new books out of his schoolbag."), ("他从书包里拿出两本新书来。", "He took two new books out of his schoolbag. (object between)"), ("他从台湾带回来两个朋友。", "He brought two friends back from Taiwan."), ("他从台湾带回两个朋友来。", "He brought two friends back from Taiwan. (object between)")]
OR3 = [("我们爬上山去。", "We hiked up the mountain. (mine; 爬, 我们, 去, 山, 上)"), ("他跑过来了。", "He ran over here. (mine; 来, 他, 过, 了, 跑)"), ("他们都走出去了。", "They all walked out. (mine)"), ("我把书拿回来了。", "I brought the books back here. (mine)")]
L4 = lesson(
    "Lesson 15 Presentation 1 grammar: directional verb combinations as complements",
    "搬进来 · 爬上山去 · 买回来很多水果 · 走回学校去",
    requires=[],
    cards=[
        card("Compound directional verbal combinations used as complements",
             "In Presentation 1, 老张 said 十月份，刚装修完，上星期才搬进来。 (We just finished renovating in October and only moved in last week.) The compound verbal combination 进来 is attached to the main verb 搬 as a complement to indicate the direction of the movement. All the directional verbal combinations discussed in Lesson 14 can be used as complements to main verbs: 上来/去, 下来/去, 进来/去, 出来/去, 回来/去, 过来/去, 起来*, as in 跑上来/去, 跑下来/去, 跑进来/去, 跑出来/去, 跑回来/去, 跑过来/去, 跑起来**; 拿上来/去, … 拿过来/去, 拿起来. *As a compound verbal combination, 起来 indicates upward movement, thus it can only attach to verbs that imply upward actions, for example 坐起来 or 站起来. (The chart in the book writes 过/去 and 起/来 with a slash.)",
             examples=[D(z, e) for z, e in CC1] + [D(z, e) for z, e in CC2]),
        card("With an object of place: Verb + Directional Verb + Place + 来/去",
             "When a compound directional verbal combination is used as a complement with an object of place, the object is inserted within the directional verbal combination. Notes: common mistakes are *回去中国, *回来美国, *他回去家了, *回去学校 and *走回去学校, from the effect of English expressions like “go back to China” and “come back to America”.",
             examples=[D(z, e) for z, e in CC3]),
        card("With an object of things or persons: Verb + Obj. + 来/去 or Verb + 来/去 + Obj.",
             "When a compound directional verbal combination is used with an object of things or persons, the object can be inserted within the directional combination or placed after it.",
             examples=[D(z, e) for z, e in CC4]),
        card("Activities 3 and 4",
             "Activity 3 (Reading). Order the words into the correct sequence to correspond to the English translation: 1. 爬 / 我们 / 去 / 山 / 上 (We hiked up the mountain.) 2. 来 / 他 / 过 / 了 / 跑 (He ran over here.) 3. 他们 / 去 / 出 / 了 / 都 / 走 (They all walked out.) 4. 把 / 我 / 书 / 回 / 拿 / 来 / 了 (I brought the books back here.) My answers (mine):",
             examples=[D(z, e) for z, e in OR3]),
        card("Activity 4 (Listening, Reading, Writing and Speaking)",
             "Step 1 (listening): the teacher verbally gives commands (指令 zhǐlìng) to the students, who perform them accordingly. Step 2 (reading): after performing the actions, students read the note from the teacher in pairs and try to discern what they need to do. Step 3 (writing): in pairs, students write commands that can lead one of the other pairs of students to sit back down in the classroom. Step 4 (speaking): in pairs, students give commands to another pair and direct them to sit back down. (The commands and the note are given by the teacher and are not printed in the book.)"),
    ],
    exercises=[
        M("What does 进来 add to 搬进来?", "The direction of the movement", ["The time", "The reason", "The object"], "Direction complement."),
        M("Which verbs can 起来 attach to?", "Verbs implying upward movement, like 坐 and 站", ["Any verb", "Only 去", "Only nouns"], "Upward movement."),
        M("Which is correct?", "他走回学校去。", ["他走回去学校。", "他回去学校走。", "他走去回学校。"], "Place goes inside."),
        M("Which is a common mistake?", "回去中国", ["回中国去", "走回学校去", "爬上山去"], "*回去中国."),
        M("What does 不要让小猫跑出去了 mean?", "Don’t let the kitten run out", ["Let the kitten out", "The kitten is hungry", "Feed the kitten"], "跑出去."),
        M("What does 周末，我和几个朋友早上六点就爬上山去看日出 mean?", "On the weekend we climbed up the mountain at six to see the sunrise", ["We watched the sunrise at home", "We went to bed at six", "We went down the mountain"], "爬上山去."),
        M("What does 他买回来很多水果 mean?", "He bought a lot of fruit and brought it back", ["He sold fruit", "He ate fruit", "He lost the fruit"], "买回来."),
        M("Which place the object correctly with things?", "他从书包里拿出两本新书来。", ["他从书包里拿两本新书出来去。", "他拿出来书包里两本新书。", "他两本新书拿出。"], "Verb + 出 + obj + 来."),
        F("请站起___。", "来", PART, "站起来: stand up."),
        F("他没赶上最后一班车，只好走回学校___。", "去", PART, "走回学校去."),
    ],
)

# ------------------------------------------------------------------ 5. 一…就…
YJ1 = [("我一回到宿舍就开始做作业。", "I started to do my homework as soon as I got back to my dormitory."), ("孩子一到六岁就要上小学。", "When children reach six years of age, they must go to school. (the book writes 6 岁)")]
YJ2 = [("明天我一回到家就给你打了个电话。", "Tomorrow as soon as I get home I will call you. (the book prints 明天…了, as written)"), ("我一开始做作业姐姐就会把电视关上。", "As soon as I start my homework my sister will turn the TV off."), ("儿子一进家门就说，“妈，我饿了！”", "As soon as my son came in the door he said, “Mom, I’m hungry!”"), ("冬天一到我们就可以去滑雪了。", "As soon as winter comes we can go skiing."), ("工人们一到五点就下班回家。", "The workers go home as soon as it’s five o’clock.")]
YJ6 = [("老李听说老王买了新房子，就马上打电话恭喜他。", "Original (the book’s example): Lao Li heard that Lao Wang had bought a new house and immediately called to congratulate him."), ("老李一听说老王买了新房子就马上打电话恭喜他。", "Paraphrase (the book’s example)."),
       ("小王一来到书店，书店一开门就马上进去了。", "(mine) Xiao Wang arrived at the bookstore very early and went in as soon as it opened. (original: 小王很早就来到书店，书店开门后，他马上就进去了。)"), ("她一放暑假就马上坐火车回家了。", "(mine) She took the train home as soon as summer vacation began. (original: 她在北京上大学，放了暑假她马上就坐火车回家了。)"),
       ("在中国很多地方，小学生一上三年级就开始学英语。", "(mine) In many places in China, pupils begin to study English as soon as they enter third grade."), ("王太太一听说儿子有女朋友了，就马上要他把女朋友带回家让她看看。", "(mine) As soon as Mrs. Wang heard that her son had a girlfriend, she immediately asked him to bring her home for her to see.")]
L5 = lesson(
    "Lesson 15 Presentation 1 grammar: the 一…就… construction",
    "我一赛完就去 · 我一回到宿舍就开始做作业 · 冬天一到我们就可以去滑雪了",
    requires=[],
    cards=[
        card("The 一…就… Construction",
             "The 一…就… construction is used to connect two actions or events that closely follow each other. It is like the English “as soon as…” or “once… then…”. For a non-specific situation, the first clause represents the condition and the second the result. Patterns: Subject + 一…就…; Subject A + 一… Subject B + 就… From the dialog: 那好，我一赛完就去。",
             examples=[D(z, e) for z, e in YJ1]),
        card("Examples 1 to 5",
             "The book’s examples:",
             examples=[D(z, e) for z, e in YJ2]),
        card("Activities 5 and 6",
             "Activity 5 (Listening, Speaking, and Reading). A. Listen to the conversation and write the five exchanges you heard using the 一…就… construction in pinyin or characters. B. Pair up, share your work and discuss in Chinese what has upset the speakers. (Audio, not included.) Activity 6 (Reading, Writing, and Speaking). A. Pair up and paraphrase the original sentences in the table using the 一…就… construction. The book’s four originals: 小王很早就来到书店，书店开门后，他马上就进去了。 她在北京上大学，放了暑假她马上就坐火车回家了。 在中国很多地方，小学生从上三年级开始学英语。 王太太听说儿子有女朋友了，马上要他把女朋友带回家让她看看。 The book’s example and my paraphrases:",
             examples=[D(z, e) for z, e in YJ6]),
    ],
    exercises=[
        M("What does 一…就… express?", "Two actions following closely: “as soon as”", ["Because…so", "Although…but", "If…not"], "As soon as."),
        M("What does 我一赛完就去 mean?", "I’ll go as soon as the match is over", ["I will not go", "I went after the match yesterday", "I am playing"], "一赛完就去."),
        M("What does 冬天一到我们就可以去滑雪了 mean?", "As soon as winter comes we can go skiing", ["Winter is over", "We don’t ski", "We ski in summer"], "一到…就…"),
        M("What does 工人们一到五点就下班回家 mean?", "The workers go home as soon as it’s five", ["The workers start at five", "The workers work all day", "The workers never go home"], "一…就…"),
        M("What does 儿子一进家门就说 mean?", "The son said it as soon as he entered the door", ["The son did not enter", "The son was silent", "The son left"], "一进…就说."),
        M("Which sentence is correct?", "我一回到宿舍就开始做作业。", ["我回到宿舍一开始做作业就。", "我一就回到宿舍开始。", "我回到一宿舍就开始。"], "一 + V1 + 就 + V2."),
        F("我一回到宿舍___开始做作业。", "就", PART, "就: then."),
        F("孩子一到六岁就要上小___。", "学", PART, "小学: elementary school."),
    ],
)

# ------------------------------------------------------------------ 6. potentiality (1)
PO = [("我听不懂你说的话。", "I can’t understand what you’re saying."), ("你做得完作业吗？", "Can you finish the homework?"), ("我们的新家你找得到找不到？", "Can you find our new home? (object preposed)"), ("我太太要我买的那种衣服，我买不到。", "I can’t get the kind of clothes my wife wants me to buy. (object preposed)")]
PO0 = [("今天作业很多，你做得完做不完？", "There is a lot of homework today; can you finish it?"), ("我做得完。", "I can finish it.")]
PO8 = [("王英现在打乒乓球打得不好，但是以后她会打得好的。", "(mine) Wang Ying doesn’t play table tennis well now, but later she will be able to play well. (cue: able to play well)"), ("小红喜欢看书。她看不懂就让妈妈给她讲。", "(mine) Xiaohong likes to read. When she can’t understand, she has her mom explain it to her."), ("我今天得把作业做完，做不完这个周末我哪儿都不能去。", "(mine) I have to finish the homework today; if I can’t finish it, I can’t go anywhere this weekend."),
       ("小明不喜欢上英语听力课，因为很多英文句子他听不懂。", "(mine) Xiaoming doesn’t like English listening class because he can’t understand many English sentences."), ("李先生看书的时候离书很近，可他还是看不清楚。", "(mine) Mr. Li holds the book very close when reading, but he still can’t see clearly."), ("这是日文杂志。李先生没学过日文，他怎么能看得懂？", "(mine) This is a Japanese magazine. Mr. Li never studied Japanese; how could he understand it?"),
       ("林先生想买一套白色的西装，可是他去了好几家商店都买不到。", "(mine) Mr. Lin wants to buy a white suit, but he went to several stores and couldn’t get one.")]
PO9 = [("今天的作业你做得完吗？", "Do you manage to finish today’s homework? (the book’s example)"), ("我做得完。", "I can finish it."), ("今天的作业他做不好。", "He can’t do today’s homework well."), ("今天的作业他做得好吗？", "Can he do today’s homework well?"),
       ("你游得快吗？", "(mine, 游泳, 快) Can you swim fast?"), ("我游得快。", "I can swim fast."), ("他游不快。", "He can’t swim fast."), ("这个包裹你寄得快寄不快？", "(mine, 寄包裹, 慢) Can you send this package quickly?"), ("我寄得快。", "I can send it quickly.")]
L6 = lesson(
    "Lesson 15 Presentation 1 grammar: the complement of potentiality (1)",
    "赛得完赛不完 · 听不懂 · 找得到找不到 · 买不到",
    requires=[],
    cards=[
        card("Complement of Potentiality (1)",
             "A potential complement indicates the possibility or impossibility of achieving a desired result through an action. They are mostly used in negative or interrogative sentences. The affirmative form is mostly used when responding to another person’s question. Affirmative: Subject + Verb + 得 + Complement. Negative: Subject + Verb + 不 + Complement. Interrogative: Subject + Verb + 得 + Complement + 吗? / Subject + Verb + 得 + Complement + Verb + 不 + Complement? The book’s example:",
             examples=[D(z, e) for z, e in PO0]),
        card("Examples 1 to 4 and common verb + complement words",
             "Below are some common (verb + complement) words; each complement indicates the result of an action. These combinations were established through common practice, so it is best to remember the compound as a whole. When 得 or 不 is inserted between them, they become a complement of potentiality. -见: 看见, 听见, 碰见, 遇见. -懂: 看懂, 听懂, 弄懂. -到: 看到, 听到, 见到, 做到, 走到, 买到, 学到, 找到. -好: 学好, 修好, 做好, 考好, 写好, 换好, 锁好, 穿好. -完: 看完, 听完, 用完, 做完, 考完, 写完, 干完, 学完.",
             examples=[D(z, e) for z, e in PO]),
        card("Activities 7 and 8",
             "Activity 7 (Listening and Speaking). A. Listen to the conversation and mark the statements true or false; new expressions: 清楚 (qīngchu; clear), 坏了 (huàile; broken), 再说一遍 (zàishuō yībiàn; say that again). 1. David couldn’t hear Lin Hong, so he asked her to repeat what she had just said. 2. David couldn’t go to Lin Hong’s house because he didn’t understand the directions Lin provided. 3. Lin Hong and David will meet at the entrance of Dahua Movie Theatre at 8:00 because Lin Hong couldn’t make it at 7:45. (Audio, not included, so no key.) Activity 8 (Reading and Speaking). A. Complete the sentences with potential complements using the cues (the book’s cues: able to play well; not able to understand; not able to finish; not able to understand; not able to see clearly; able to understand; not able to get them). My completions (mine):",
             examples=[D(z, e) for z, e in PO8]),
        card("Activity 9 (Speaking and Writing)",
             "Work in groups of three. Take turns creating sentences using potential complements with the provided expressions: one member provides the affirmative form, one the negative and the third the interrogative form. The book’s example (做作业，完) and my answers for items 1 (游泳, 快) and 2 (寄包裹, 慢) (mine):",
             examples=[D(z, e) for z, e in PO9]),
    ],
    exercises=[
        M("What does a potential complement express?", "Whether a desired result can be achieved", ["The time of an action", "A comparison", "A future plan"], "Possibility/impossibility."),
        M("Which is the negative form?", "听不懂", ["听得懂", "听懂了", "没听懂吗"], "Verb + 不 + complement."),
        M("What does 我听不懂你说的话 mean?", "I can’t understand what you say", ["I won’t listen", "I don’t like talking", "I understood everything"], "听不懂."),
        M("What does 你做得完做不完？ ask?", "Can you finish it or not?", ["Did you finish?", "Where did you finish?", "Why not finish?"], "A-not-A potential."),
        M("What does 我买不到 mean?", "I can’t get it (it can’t be found)", ["I don’t want to buy", "I bought it", "I forgot to buy"], "买不到."),
        M("Which complement means “finished”?", "完", ["懂", "见", "好"], "做完, 看完."),
        M("Which means “understand by listening”?", "听懂", ["听见", "听完", "听好"], "懂: understand."),
        M("Which completion fits 这是日文杂志。李先生没学过日文，他怎么能___？", "看得懂", ["看不懂", "看完了", "看得完不完"], "怎么能 + 得 = rhetorical."),
        F("我听___懂你说的话。", "不", PART, "听不懂."),
        F("今天作业很多，你做___完做不完？", "得", PART, "做得完做不完."),
    ],
)

# ------------------------------------------------------------------ 7. verb duplication
VD = [("我们请几个朋友来我家聚聚，热闹热闹。", "We’ll invite a few friends to my home to get together a bit and have some fun. (gather a bit, have some fun)"), ("我们请几个朋友来我家聚，来我家热闹。", "We invite friends to gather in my home, bustling with noise. (no duplication)"), ("你看看收到没有？", "Could you check whether you received it?"), ("你看收到没有？", "Please check whether you received it. (firmer)"), ("大家聊聊天。", "Everybody chats (casually)."), ("大家聊天。", "Everybody converses."), ("你买新房子啦！恭喜恭喜！", "You bought a new house! Congratulations, congratulations! (not verb duplication, just congratulating twice)")]
S10 = [("你告诉马文，他得每天早上起来锻炼。", "Original: Tell Ma Wen he has to get up every morning and exercise."), ("你告诉马文，早上起来可以锻炼锻炼。", "(mine, softened) Tell Ma Wen he could exercise a bit after getting up in the morning."), ("你告诉马文，他早上上课以前要复习生词。", "Original: Tell Ma Wen he must review vocabulary before class in the morning."), ("你告诉马文，早上上课以前可以复习复习生词。", "(mine, softened) Tell Ma Wen he might review the new words a bit before class."),
       ("你告诉马文，有问题要问老师。", "Original: Tell Ma Wen to ask the teacher when he has questions."), ("你告诉马文，有问题可以问问老师。", "(mine, softened) Tell Ma Wen he may ask the teacher when he has questions."), ("你告诉马文，下课以后要跑步。", "Original: Tell Ma Wen to run after class."), ("你告诉马文，下课以后可以跑跑步。", "(mine, softened) Tell Ma Wen he can go for a run after class."),
       ("你告诉马文，有时间要和中国人聊天。", "Original: Tell Ma Wen to chat with Chinese people when he has time."), ("你告诉马文，有时间可以和中国人聊聊天。", "(mine, softened) Tell Ma Wen he can chat a bit with Chinese people when he has time."), ("你告诉马文，晚上睡觉以前听音乐。", "Original: Tell Ma Wen to listen to music before bed."), ("你告诉马文，晚上睡觉以前可以听听音乐。", "(mine, softened) Tell Ma Wen he can listen to a little music before bed.")]
P11 = ("每个周六我都快到中午才起床。起床以后我就去食堂吃吃午饭。吃午饭的时候，常跟几个朋友坐在一起，一边吃，一边聊聊天，开开玩笑。下午，我有时和朋友一起去电影院看看电影，有时自己一个人去渔人码头走走。一个人走的时候，如果觉得没意思，我会听听音乐，或者给我家人打打电话。晚上回到学校，我会做做作业，复习复习，看看中国电视。有时候要去值值班。")
P11_E = "Every Saturday I don’t get up until almost noon. After getting up I go to the cafeteria to have lunch. While eating lunch I often sit with a few friends, chatting and joking as we eat. In the afternoon sometimes I go to the movie theater with friends to see a movie, sometimes I go alone to Fisherman’s Wharf for a walk. When I walk alone, if I feel bored, I listen to music or call my family. In the evening back at school I do my homework, review a bit and watch Chinese TV. Sometimes I have to go on duty. (my completion, mine; the book’s cues are 吃, 聊, 开, 看, 走, 听, 打, 做, 复习, 看, 值)"
L7 = lesson(
    "Lesson 15 Presentation 1 grammar: verb duplication",
    "聚聚 · 热闹热闹 · 看看 · 聊聊天 · 恭喜恭喜",
    requires=[],
    cards=[
        card("Verb Duplication",
             "In this presentation verb duplication appears in several places: 我们请几个朋友来我家聚聚，热闹热闹。 刚才我已经把地址发给你了，你看看收到没有？ 大家聊聊天，然后在我家吃顿便饭。 Verb duplication indicates that an action lasts only a short time and is casual. It is often used to soften the tone and express one’s wishes tactfully. Notice the pronunciation: for monosyllabic verbs, the duplication is in neutral tone, e.g. 聚聚 jùju, 看看 kànkan; for two-syllable words, the second syllable is neutral, e.g. 热闹热闹 rènao rènao. Note: 恭喜恭喜 simply says congratulations twice, to show one’s heartfelt happiness for the new homeowner; it is not a case of verb duplication.",
             examples=[D(z, e) for z, e in VD]),
        card("Activity 10 (Speaking and Writing): soften the tone for a stern teacher",
             "A Chinese teacher asks you to pass his message to one of your classmates. He speaks sternly, but you want to pass his words to your classmate gently. A. Individually, soften the tone wherever you see fit. B. Work in pairs, compare your answers and discuss which paraphrases are more appropriate. The six originals and my softened versions (mine):",
             examples=[D(z, e) for z, e in S10]),
        card("Activity 11 (Reading and Writing)",
             "The following paragraph describes a DLI soldier’s weekend. Complete the paragraph using single verbs or duplicated verbs where appropriate. My completed paragraph:",
             examples=[D(P11, P11_E)]),
    ],
    exercises=[
        M("What does verb duplication indicate?", "A short, casual action; it softens the tone", ["A long action", "A past action", "A negative"], "Short and casual."),
        M("How is the second 看 in 看看 pronounced?", "Neutral tone", ["Fourth tone", "First tone", "Second tone"], "kànkan."),
        M("How is 热闹热闹 pronounced?", "rènao rènao, with the second syllable neutral", ["rènào rènào", "rénao rénao", "rèrè nàonào"], "Second syllable neutral."),
        M("Is 恭喜恭喜 verb duplication?", "No, it is just congratulating twice", ["Yes, always", "Yes, to soften", "It is a question"], "Not a duplication."),
        M("What does 你看看收到没有？ do?", "Politely asks to check whether it arrived", ["Orders sternly", "Refuses", "Asks for money"], "Softened."),
        M("What is the difference: 大家聊聊天 vs 大家聊天?", "The first is casual, “chat a bit”", ["The first is a question", "The first is past", "The first is negative"], "Duplication softens."),
        M("Which word is a duplicated two-syllable verb?", "热闹热闹", ["恭喜恭喜", "聊聊天", "看看"], "热闹热闹."),
        F("大家聊___天，然后在我家吃顿便饭。", "聊", PART, "聊聊天."),
        F("你看___收到没有？", "看", PART, "看看."),
    ],
)

# ------------------------------------------------------------------ 8. skill integration
EM = ("女儿：这个星期六下午四点左右，我和你爸爸想请一些老朋友们过来玩儿玩儿。请他们过来，第一是看看咱们的新房子，第二是大家好久不见，聚聚，热闹热闹。第三最重要，就是给我们的小外孙过一周岁生日。你是孩子的妈妈，所以我想让你给咱们家几位老朋友发个短信，请他们过来参加聚会。除了告诉他们聚会的原因和时间以外，也把地址发给他们。如果他们星期六都来得了，那最好。如果有人来不了，就请他们哪天有空儿再来。糟糕，十分钟以前我给你发了一个邮件，里面是他们的手机号码，可是有两个是错的！我马上再给你发了一个。过几分钟你看看收到没有，要是没收到就告诉我。妈妈")
EM_E = ("(Email, subject: 星期六下午) Daughter: This Saturday around four in the afternoon your father and I would like to invite some old friends over to have a good time. We invite them, first, to see our new home; second, because we haven’t seen each other for a long time, to get together and liven things up. Third and most important, to celebrate our little grandson’s first birthday. You are the child’s mother, so I’d like you to send a text message to a few of our old friends to invite them to the party. Besides telling them the reason and time of the party, also send them the address. If they can all come on Saturday, that’s best; if someone can’t come, ask them to come on another day when they are free. Oh no, ten minutes ago I sent you an email with their cell-phone numbers, but two are wrong! I’ll send you another one right away. In a few minutes see whether you received it, and if not tell me. Mom")
SMS = ("各位叔叔阿姨，你们好！这个星期六下午四点左右，我爸爸妈妈想请大家来家里聚聚。第一，看看他们的新房子；第二，大家好久不见，热闹热闹；第三，给我儿子过一周岁生日。地址是……（见下条短信）。如果星期六来不了，请告诉我们哪天有空儿，欢迎再来。谢谢！")
L8 = lesson(
    "Lesson 15 Presentation 1: skill integration",
    "孙丽请刘青来新家 · 妈妈的邮件 · 请朋友来聚会",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing, Speaking, and Reading)",
             "A. Pair up. Each partner listens to one of two passages and fills in the table in pinyin: Passage 1: Time, Location and Participants; Event; About Liu Qing. Passage 2: Event; Situation; Solution. B. Sun Li calls Liu Qing to invite her to a gathering at her new home. Perform the dialog between Sun Li and Liu Qing with your partner. (Audio, not included.)"),
        card("Activity 2 (Reading, Speaking, and Writing): the email",
             "A. Read an email and answer the questions. New word: 短信 (duǎnxìn; text message). Questions: 1. What is the occasion for the proposed gathering? 2. What does the author want her daughter to do? 3. What is the daughter supposed to do if an invitee cannot attend this Saturday? 4. What concerns the author at the end of the message? What will she do to correct this? (Mine: 1. Showing the new home, getting old friends together, and the grandson’s first birthday. 2. Send text messages inviting the old friends, with the reason, time and address. 3. Ask them to come another day when they are free. 4. Two phone numbers in the earlier email were wrong; she will send a corrected email.) The email:",
             examples=[D(EM, EM_E)]),
        card("Activity 2 B and Activity 3",
             "B. In the space provided, compose a text message that invites friends to attend the event based on the mother’s instructions; in pairs check each other’s message. My message (mine):",
             examples=[D(SMS, "(mine) Dear uncles and aunts, hello! This Saturday around four in the afternoon my parents would like to invite everyone to their home. First, to see their new house; second, since we haven’t seen each other for a long time, to have a lively time; third, my son’s first birthday. The address is… (see the next message). If you can’t come on Saturday, tell us which day you’re free; you’re welcome to come then. Thank you!")]),
        card("Activity 3 (Speaking and Writing)",
             "A. Work in groups of three. Interview your group members to learn what their plans would be if they held a gathering at home; fill in the table (Proposed Event; When & Where; Whom to Invite; Activities; rows A and B). B. Work between groups: one group gives a clue and asks the other group to figure out whose plan it is, including details. C. Within your group, convert one of the two plans into a phone conversation between the host (主人) and an invitee (朋友), five exchanges, and share it with the class."),
    ],
    exercises=[
        M("How many reasons does the mother give for the gathering?", "Three", ["One", "Five", "None"], "第一…第二…第三…"),
        M("What is the most important reason?", "Her grandson’s first birthday", ["The new house", "A wedding", "A promotion"], "第三最重要，就是给我们的小外孙过一周岁生日。"),
        M("What does the mother ask her daughter to do?", "Text the old friends with the reason, time and address", ["Cook dinner", "Buy a gift", "Clean the house"], "发个短信。"),
        M("What if someone can’t come on Saturday?", "Ask them to come another day when they are free", ["Cancel the party", "Do nothing", "Call the police"], "哪天有空儿再来。"),
        M("What did the mother get wrong?", "Two phone numbers in the email", ["The address", "The time", "The date"], "有两个是错的！"),
        M("What does 短信 mean?", "Text message", ["Short story", "Short skirt", "Short film"], "短信: text message."),
        M("What does 来得了 mean?", "Able to come", ["Can’t come", "Came already", "Will not come"], "来得了: potential."),
        F("我想让你给咱们家几位老朋友发个短___。", "信", PART, "短信."),
        F("给我们的小外孙过一周岁生___。", "日", PART, "生日."),
    ],
)

# ------------------------------------------------------------------ 9. using Chinese in context
PIC = ("马龙，你好！刚才李教官告诉我，学校已经同意我们班下星期三搞野餐活动了。我想请你来组织一下，好吗？时间和地点，准备什么样的食品、饮料以及怎么准备，你和同学们决定。下星期一以前，每位老师会交给你十二元钱。另外，上次我们班组织春节聚餐，还有很多纸盘、刀叉和餐巾纸没用完，就不需要再买了。我会带一些春卷过去，刘老师会带一些水果。我还有一个建议。以前教过你们的孙老师和高老师，虽然现在不教你们了，但她们都很关心你们的学习。特别是孙老师，每个星期都给我打电话，问你们的情况。我知道你们也很想念她们。你能不能写一封信，请她们参加我们的野餐呢？张老师")
PIC_E = ("Ma Long, hello! Just now Instructor Li told me that the school has agreed to let our class hold a picnic next Wednesday. I’d like you to organize it, all right? You and the classmates decide the time and place, what kind of food and drinks to prepare and how. Before next Monday, each teacher will give you twelve yuan. In addition, last time our class organized the Spring Festival dinner there were still many paper plates, knives and forks and napkins unused, so there is no need to buy more. I’ll bring some spring rolls and Teacher Liu will bring some fruit. I have one more suggestion. Teachers Sun and Gao, who taught you before, although they no longer teach you now, both care a lot about your studies. Especially Teacher Sun, who calls me every week to ask about you. I know you also miss them very much. Could you write a letter inviting them to join our picnic? Teacher Zhang")
FLY = [("蒙特雷华人庆新春联欢会", "上边（红色部分）：标题"), ("美食", "中国美食、中国传统音乐、歌曲和舞蹈"), ("红包", "十二岁以下的孩子都有红包，祝大家好运"), ("时间", "二零二一年一月十八日，星期六，中午十二点到下午三点"), ("地点", "蒙特雷社区中心")]
FLY_Z = ("蒙特雷华人庆新春联欢会，欢迎大家来参加！时间：二零二一年一月十八日，星期六，中午十二点到下午三点。地点：蒙特雷社区中心。我们准备了丰富的中国美食，还有中国传统的音乐、歌曲和舞蹈。十二岁以下的孩子都可以得到一个好运红包。")
L9 = lesson(
    "Lesson 15 Presentation 1: using Chinese in context (invitations, picnic, New Year flyer)",
    "两个留言 · 班级野餐 · 蒙特雷华人庆新春联欢会",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Speaking, and Writing)",
             "You are David and your partner is Linda, studying at Beijing University; the Chinese New Year is coming. Today you received two voice messages from Chinese friends inviting you to gatherings at their homes (photographs not included). A. Pair up. Listen to one message each; in English write the key information in the table (什么时间, 什么地点, 谁还参加, 做什么, 带什么礼物; 第一个留言, 第二个留言). New words: 地道 (dìdào; genuine), 表演 (biǎoyǎn; performance), 逛 (guàng; walk around), 大餐 (dà cān; feast), 书法 (shūfǎ; calligraphy). B. Share your information and take notes on your partner’s. C. Because of a time conflict you can attend only one gathering; discuss and decide which. D. Write a reply email to Wang Dong’s invitation (your partner replies to Xu Ying) and share it with the class. (Audio, not included.)"),
        card("Activity 2 (Reading, Writing, and Speaking): the class picnic",
             "You are the class leader and it is time for your class to have a picnic. A. Read the email from Zhang Laoshi, leader of the teaching team. The email:",
             examples=[D(PIC, PIC_E)]),
        card("Activity 2 B to D",
             "B. Make a plan for the picnic and fill in the table in pinyin or characters: 地点; 开始时间和结束时间; 参加人员; 需要准备的东西. C. Write an email inviting Sun Laoshi and Gao Laoshi to the picnic, including the kind of event, the time, location, what food will be provided, who will attend and whether guests need to bring anything (subject: 邀请). D. Pair up, go over your email with your partner, refine it and share it with the class."),
        card("Activity 3 (Reading, Writing, and Speaking): the New Year flyer",
             "The Chinese New Year is coming and the local Chinese community is preparing a major celebration; one of your teachers is the organizer and needs your help. A. Below is an old flyer in English (Monterey Bay Chinese Community Chinese New Year Celebration; 蒙特雷华人庆新春联欢会; “2021 Year of Ox” beside “鼠年大庆” in the book; Chinese gourmet foods; Chinese traditional music, songs and dances; red envelopes of good fortune for children under 12; 12 PM to 3 PM, Saturday, Jan 18, 2021; Monterey Community Center). Design a new flyer in Chinese that is more specific to this year’s event, for example by listing the food and drinks provided. Write the Chinese version in the table (位置: 上边（红色部分）, 中间（蓝色部分）, 下边（黑色部分）; 中文). B. In pairs, share and refine your flyer. C. Write an email to inform members of the Chinese Speaking Club of this event (subject: 邀请). The book’s flyer and my Chinese flyer text (mine; the book’s year and animal do not match, so I left them out of the title):",
             tables=[table(["位置", "中文 (mine)"], [(a, b) for a, b in FLY], title="Flyer plan", say=[0, 1])],
             examples=[D(FLY_Z, "(mine) The Monterey Chinese Community Spring Festival gala, everyone is welcome! Time: Saturday, January 18, 2021, noon to 3 p.m. Place: Monterey Community Center. We have prepared rich Chinese food, plus traditional Chinese music, songs and dances. Every child under twelve can get a good-luck red envelope.")]),
    ],
    exercises=[
        M("What are you asked to do in Activity 1?", "Decide which of two invitations to accept and write a reply", ["Plan a wedding", "Book a flight", "Buy a house"], "Two voice messages."),
        M("Who is the picnic organizer?", "The class leader, Ma Long", ["Teacher Zhang", "Teacher Sun", "Instructor Li"], "马龙: 请你来组织一下。"),
        M("When is the picnic?", "Next Wednesday", ["Next Monday", "Tomorrow", "Next month"], "下星期三搞野餐活动。"),
        M("How much will each teacher give?", "Twelve yuan", ["One yuan", "One hundred yuan", "Nothing"], "每位老师会交给你十二元钱。"),
        M("What will Teacher Zhang bring?", "Spring rolls", ["Fruit", "Paper plates", "Drinks"], "我会带一些春卷过去。"),
        M("Who will bring fruit?", "Teacher Liu", ["Teacher Sun", "Teacher Gao", "Teacher Zhang"], "刘老师会带一些水果。"),
        M("Why is there no need to buy paper plates?", "Many were left over from the Spring Festival dinner", ["They are free", "They are banned", "The store is closed"], "还有很多纸盘…没用完。"),
        M("What does Teacher Zhang suggest?", "Invite Teachers Sun and Gao to the picnic", ["Cancel the picnic", "Have it indoors", "Invite the principal"], "写一封信，请她们参加我们的野餐。"),
        M("Why does Teacher Zhang say Teacher Sun cares?", "She calls every week to ask about the class", ["She teaches them now", "She is their neighbor", "She is their relative"], "每个星期都给我打电话。"),
        M("What is Activity 3’s task?", "Design a Chinese flyer for the Chinese New Year celebration", ["Translate a menu", "Write a speech", "Sell tickets"], "New flyer."),
        mean("野餐", "ye3 can1", "picnic", ["barbecue", "banquet", "breakfast"]),
        F("我想请你来组___一下，好吗？", "织", PART, "组织: organize."),
    ],
)
L10 = vocab_lesson("Lesson 15 Presentation 1 vocabulary", "23 words from the book’s Presentation 1 list",
                   "Presentation 1 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC1)

UNIT = unit("第十五课 社交聚会 Presentation 1: housewarming invitation, 刚, directional complements, 一…就…, potentiality (1), verb duplication", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
