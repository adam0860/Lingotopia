"""Unit 49: Lesson 17 (Sports and Fitness) Presentation 2 from the book's texts: the outdoor-activities dialog, the adverb 才 (cause and
effect, only), 其他/别的, 从……起, 简直, the skill-integration passages (Lin Hong's children, the ski resort and its price table) and the
using-Chinese activities, with the vocabulary list. Audio, pictures and websites are not included; the book writes numbers and phone
numbers as digits and they are spelled out in spoken text; answer keys the book does not print (and blanks it leaves for the student)
are mine and labeled."""
from zh_auto import *
from zh_l17_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("教我", 0, "jiao1"), ("教你", 0, "jiao1"), ("长得", 0, "zhang3"), ("得有", 0, "dei3"), ("得开", 0, "dei3"), ("得做", 0, "dei3"), ("得减肥", 0, "dei3"),
                          ("得买", 0, "dei3"), ("都会", 0, "dou1"), ("没问题", 0, "mei2"), ("没关系", 0, "mei2"), ("没有时间", 0, "mei2"), ("没有别的", 0, "mei2"), ("睡不着", 2, "zhao2")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5
        if ch == "地" and j > 0 and zh[j - 1] not in "当草土天各山场内本外基实陆" and (j + 1 >= len(zh) or zh[j + 1] not in "道址方铁图球区点上下面理"):
            f[j] = "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. dialog and activities
P2 = [("李明", "张文，一个暑假没见，你怎么晒得这么黑？", "Zhang Wen, we haven’t seen each other for a whole summer vacation; how did you get so tanned?"), ("张文", "我回老家了，每个周末都去冲浪，所以才晒得这么黑。", "I went back to my hometown and went surfing every weekend, so I got this tanned."),
      ("李明", "你的老家夏天是不是很热啊？", "Is it very hot in your hometown in the summer?"), ("张文", "对，我老家在海边，一年四季都很闷热。除了游泳、冲浪以外，其他活动都做不了。李明，你的老家怎么样？", "Yes, my hometown is by the sea and it’s hot and stuffy all year round. Except for swimming and surfing, we can’t do any other activities. Li Ming, how is your hometown?"),
      ("李明", "我的老家四季分明，每个季节都可以做不同的活动，不但可以滑雪、滑冰，而且可以爬山、露营。", "My hometown has four distinct seasons, and each season you can do different activities: not only can you ski and ice-skate, but you can also hike and camp."), ("张文", "那你最喜欢干什么呢？", "Then what do you like to do most?"),
      ("李明", "我最大的爱好是滑雪，从六岁起就开始了。每年冬天，我们全家都去滑雪场度假。", "My biggest hobby is skiing; I started at the age of six. Every winter our whole family goes to a ski resort for vacation."), ("张文", "听起来很有意思。有空儿的时候，你能不能教我滑雪？", "That sounds interesting. When you have time, could you teach me to ski?"),
      ("李明", "没问题。", "No problem."), ("张文", "滑雪都需要什么装备？", "What equipment do you need for skiing?"),
      ("李明", "你得有滑雪板，还得有滑雪服，滑雪鞋，滑雪眼镜，头盔什么的。不过，不用担心，这些东西都可以在滑雪场租到。", "You need skis, and a ski suit, ski boots, ski goggles, a helmet and so on. But don’t worry; you can rent all of these at the ski resort."), ("张文", "太棒了，我简直都等不及啦。", "Great, I simply can’t wait.")]
AC4 = [("今年春节，你们全家打算去哪里度假？", "1. Where is your whole family planning to go on vacation this Spring Festival? (度假; key mine)"), ("你有空儿的时候，能不能陪我去渔人码头看看海景？", "2. When you have time, could you go with me to Fisherman’s Wharf to look at the sea view? (有空儿)"), ("这个地方风景很美，有很多树，也很安静，很适合露营。", "3. This place has beautiful scenery, lots of trees and is quiet; it’s very suitable for camping. (露营)"),
       ("下个周末我们就要去滑雪了。你的滑雪装备都准备好了吗？", "4. We’re going skiing next weekend. Is all your ski equipment ready? (装备)"), ("不用担心，滑雪用的东西，我在网上已经买了，明天就到了。", "5. Don’t worry; I already bought the skiing things online and they’ll arrive tomorrow. (担心)"), ("骑自行车的时候，不要忘了戴头盔，这样你不会受伤。", "6. When riding a bike, don’t forget to wear a helmet; that way you won’t get hurt. (头盔)"),
       ("我们学校附近有很多山，周末的时候，我们常常去爬山。", "7. There are many mountains near our school, and on weekends we often go hiking. (爬山)"), ("我最好的朋友明天要来蒙特雷看我。我高兴得等不及了。", "8. My best friend is coming to Monterey tomorrow to see me. I’m so happy I can’t wait. (等不及; the book’s blank is 我高兴地____; mine)"), ("成龙的新动作片简直太好看了。我都看了三遍了。", "9. Jackie Chan’s new action movie is simply so good. I’ve already watched it three times. (简直)"),
       ("大卫昨天租到了一辆车。我们可以一起开车去旧金山。", "10. David rented a car yesterday. We can drive to San Francisco together. (租到)")]
INT = ["你最喜欢什么户外运动？", "你从几岁开始做这个运动？", "你常常在什么季节做这个运动？", "做这个活动需要什么装备？", "你在哪儿买这些装备？", "除了这个以外你还喜欢什么？"]
L1 = lesson(
    "Lesson 17 Presentation 2: outdoor activities and hobbies",
    "晒得这么黑 · 四季分明 · 最大的爱好是滑雪 · 租到装备",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Do you have any hobbies? Which is your favorite? B. What is a popular outdoor activity in your hometown? C. What is your favorite outdoor activity? What kind of equipment do you need for this activity? (Six photographs, not included.)"),
        card("Presentation 2: 户外活动",
             "The book also prints the dialog in traditional characters.",
             examples=dlg(P2)),
        card("Activities 1 and 2 (listening)",
             "Activity 1 (Listening, Writing and Speaking). A. Global listening: 1. What is discussed in this conversation? 2. What season is it now? How could you tell? B. Detailed listening: 1. How did Zhang Wen get a tan? 2. What kind of outdoor activities can the people in his hometown do during the summer? 3. How different is Li Ming’s hometown from Zhang Wen’s? 4. What does Zhang Wen ask Li Ming to do? 5. What things do you think Zhang Wen will buy after their conversation? C. Pair up, discuss and share with the class. (From the dialog, mine: outdoor activities and hometowns; it has just become the start of a new term after the summer vacation; he went surfing every weekend; swimming and surfing; Li Ming’s hometown has four distinct seasons and Zhang Wen’s is hot all year; to teach him to ski; ski gear such as a ski board and goggles.) Activity 2 (Listening, Writing and Speaking). A. Listen to Dialog 1 and answer: 1. What did the two speakers talk about? 2. What did Wang Lin say about his hometown? 3. What did Linda say about her hometown? 4. What is Linda’s favorite outdoor activity? Can Wang Lin do it too? How do you know? B–C. Discuss and conduct the same conversation with your partner. D. Listen to Dialog 1 again: 1. What did the two speakers talk about? 2. What did you hear about Linda? 3. What do you think Wang Lin will probably do after their conversation? E–F. Discuss and conduct the same conversation. (Audio, not included.)"),
        card("Activity 3 (Reading, Writing and Speaking): 举一反三",
             "A. Pair up. Using the words in the first column as a cue, write the words that show what is needed for the activities shown in the other columns: 滑雪 (skiing), 滑冰 (ice skating), 冲浪 (surfing), 游泳 (swimming). The cue words are 滑雪板, 滑雪服, 滑雪鞋, 滑雪眼镜, 滑雪帽, 滑雪场. B. With your partner, discuss the characteristics of these words and analyze how they are formed. For example, 滑雪板 = 滑雪 + 板 (snowboard = snow + board): the activity plus the thing it needs. C. Report your analyses to the class. My completed words (mine): 滑冰鞋, 滑冰帽, 滑冰场; 冲浪板, 冲浪服, 冲浪帽; 游泳衣, 游泳帽, 游泳眼镜, 游泳池 (the book leaves the table blank)."),
        card("Activity 4 (Reading, Writing and Speaking)",
             "A. Using the words 担心, 头盔, 简直, 有空儿, 等不及, 度假, 装备, 租到, 爬山, 露营, complete the sentences and translate them into English. B. Pair up and explain which strategies you used. C. One partner reads the sentences and the other translates them. The book leaves the key out; my completed sentences (mine). In sentence 9 the book writes Jackie Chan’s name in English as well:",
             examples=[D(z, e) for z, e in AC4]),
        card("Activity 5 (Reading, Speaking and Listening)",
             "A. Interview a classmate about their hobbies. Use the patterns 除了…以外, 不但…，而且… or 从…起 and …什么的 to ask and answer the interview questions. Interview at least one student in your class. The questions (the right-hand column is for the interviewee’s answers); question 7 is 其他问题 (other questions). B. Consolidate your interviewee’s answers and report to the class.",
             examples=[D(f"{i}. {q}", e) for i, (q, e) in enumerate(zip(INT, ["What outdoor sport do you like best?", "At what age did you begin this sport?", "In which season do you usually do this sport?", "What equipment does this activity need?", "Where do you buy this equipment?", "Besides this, what else do you like?"]), 1)]),
    ],
    exercises=[
        M("Why is Zhang Wen so tanned?", "He went surfing every weekend", ["He skied", "He worked outside", "He stayed home"], "每个周末都去冲浪."),
        M("What is Zhang Wen’s hometown like?", "By the sea and hot and stuffy all year", ["Four distinct seasons", "In the mountains", "Cold all year"], "一年四季都很闷热."),
        M("What can Zhang Wen do in summer at home?", "Only swimming and surfing", ["Skiing", "Camping", "Skating"], "除了游泳、冲浪以外，其他活动都做不了."),
        M("What is Li Ming’s hometown like?", "Four distinct seasons", ["Hot all year", "Rainy all year", "Cold all year"], "四季分明."),
        M("What is Li Ming’s biggest hobby?", "Skiing", ["Surfing", "Swimming", "Camping"], "我最大的爱好是滑雪."),
        M("When did Li Ming start skiing?", "From age six", ["From age sixteen", "Last winter", "This year"], "从六岁起."),
        M("What does Zhang Wen ask Li Ming?", "To teach him to ski", ["To lend money", "To book a trip", "To buy a car"], "能不能教我滑雪."),
        M("Where can the ski gear be rented?", "At the ski resort", ["At school", "Online only", "At the gym"], "可以在滑雪场租到."),
        M("What does 滑雪板 break down into?", "滑雪 + 板", ["滑 + 雪板", "雪 + 滑板", "滑雪 + 场"], "Activity + equipment."),
        M("What does 简直都等不及啦 express?", "Simply can’t wait", ["Not interested", "Will go later", "Afraid"], "简直 adds excitement."),
        mean("装备", "zhuang1 bei4", "equipment", ["board", "worry", "vacation"]),
        mean("露营", "lu4 ying2", "camping", ["surfing", "skating", "hiking"]),
        F("我的老家四季___明，每个季节都可以做不同的活动。", "分", PART, "四季分明."),
        F("这些东西都可以在滑雪场租___。", "到", PART, "租到: rent (and get)."),
    ],
)

# ------------------------------------------------------------------ 2. 才
CAI = [("我们四点才下课。", "We don’t finish class until four. (L8 and L15: later than expected)"), ("大家一直玩到天黑才回家。", "Everybody played until dark before going home. (L15 Presentation 3)"), ("我每个周末都去冲浪，所以才晒得这么黑。", "I went surfing every weekend, so I got tanned. (cause and effect)"), ("下个星期，我要去滑冰，所以我才想去买滑冰鞋。", "I’ll go ice skating next week. That’s why I want to buy skates."),
       ("这个班才两个学生。", "There are only two students in this class. (only)"), ("她才学了三个月中文。", "She only studied Chinese for three months."), ("现在才七点。还不到上课时间。", "Now it is only seven o’clock. It is not time for class yet.")]
CAI2 = [("我没有钱付房租，所以我才向你借钱。", "1. I don’t have money to pay the rent. That’s why I borrowed money from you. (key mine)"), ("这个健身房什么器械都有，所以我才来这儿锻炼。", "2. This gym has all kinds of equipment. That’s why I come here to work out."), ("这条领带才十美元，所以我才买了。", "3. This tie is only ten dollars. That’s why I bought it."), ("李华不喜欢在户外慢跑，所以她才买了一个跑步机在家锻炼。", "4. Li Hua doesn’t like to jog outdoors, so she bought a treadmill to work out at home."),
        ("简下个周末要去夏威夷度假，所以她才买了一件游泳衣。", "5. Jane will vacation in Hawaii next weekend, so she bought a swimming suit.")]
L2 = lesson(
    "Lesson 17 Presentation 2 grammar: more uses of the adverb 才",
    "所以才晒得这么黑 · 这个班才两个学生 · 才 = cause and effect, only",
    requires=[],
    cards=[
        card("More Uses of the Adverb 才",
             "The adverb 才 in Chinese has many meanings. We have learned two of them so far: in Lesson 8 and Lesson 15, the adverb 才 indicates that something happened later than expected. In this lesson the adverb 才 is used to connect cause and effect. 才 can also mean “only” and be used to express how few in quantity something is. 才 + Predicate. (The book labels the first example “L18 Presentation 1”; the sentence 我们四点才下课 is from the earlier lessons.)",
             examples=[D(z, e) for z, e in CAI]),
        card("Activities 1 and 2",
             "Activity 1 (Listening and Speaking). A. Listen to eight sentences that use 才 and translate them into English. B. Work in pairs to check your translation and repeat the sentences in Chinese. (Audio, not included.) Activity 2 (Writing and Speaking). What would you say in the following situations? Work in pairs and explain the situations by using “…，所以我才…”. 1. I don’t have money to pay the rent. That’s why I borrowed money from you. 2. This gym has all kinds of equipment. That’s why I come here to work out. 3. This tie is only $10. That’s why I bought it. 4. Li Hua doesn’t like to jog outdoors, so she bought a treadmill to work out at home. 5. Jane will vacation in Hawaii next weekend, so she bought a swimming suit. My sentences (mine):",
             examples=[D(z, e) for z, e in CAI2]),
    ],
    exercises=[
        M("What does 才 connect in 所以才晒得这么黑?", "Cause and effect", ["Time order", "A question", "A wish"], "Cause and effect."),
        M("What does 这个班才两个学生 mean?", "There are only two students in this class", ["This class is big", "Two students left", "Two classes"], "才 = only."),
        M("What does 才 mean in 我们四点才下课?", "Later than expected", ["Only", "Because", "Already"], "Later than expected."),
        M("What does 她才学了三个月中文 mean?", "She has studied Chinese for only three months", ["She studied three months ago", "She will study three months", "She studies every month"], "才 = only."),
        M("What does 现在才七点 imply?", "It’s still early", ["It’s very late", "It’s seven o’clock sharp", "It’s class time"], "才 = only/just."),
        M("Which fits “I bought skates because I’ll go skating”?", "我要去滑冰，所以我才想去买滑冰鞋", ["我要去滑冰，但是我才想去买滑冰鞋", "我才要去滑冰，所以买鞋", "我要滑冰才所以买"], "…，所以我才…"),
        F("现在___七点。还不到上课时间。", "才", PART, "才 = only."),
        F("她___学了三个月中文。", "才", PART, "才 = only."),
    ],
)

# ------------------------------------------------------------------ 3. 其他/别的
QB = [("除了游泳、冲浪以外，其他活动都做不了。", "Except for swimming and surfing, people cannot do any other activities."), ("这几本书我拿走，其他几本送给你。", "I will take these books and the other books are given to you."), ("除了唱歌跳舞，我没有别的爱好。", "Except for singing and dancing, I don’t have other hobbies."), ("这家商店没有你要的眼镜，咱们去别的商店看看吧。", "This store does not have the glasses you want. Let’s go to other stores to have a look."),
      ("我现在不去想其他的，只想好好睡一觉。", "I don’t think about other things now; I just want a good night’s sleep. (其他 as an object takes 的)"), ("除了这些东西以外，我还有别的。", "In addition to these things, I have other things. (verb 有: 别的)"), ("我没有别的，只有一个箱子。", "I have nothing else, only a box. (verb 没有: 别的)")]
QB3 = [("家里其他人都去了国外，只有他一个人在国内。", "1. All the other family members went abroad; only he is in the country. (其他; key mine)"), ("除了中文，你还会说别的外语吗？", "2. Besides Chinese, can you speak other foreign languages? (别的)"), ("要想健康，最好多吃水果蔬菜。还有别的方法吗？", "3. To be healthy, it’s best to eat more fruit and vegetables. Are there other ways? (别的; verb 有)"), ("这次单元考试，只有一个同学不及格，其他五个人都通过了。", "4. In this unit test only one student failed; the other five all passed. (其他 + number + measure word)"),
        ("这种颜色的衣服不太适合我，你有别的颜色的吗？", "5. Clothes in this color don’t suit me very well; do you have other colors? (别的)"), ("这些水果我吃不了。给我留两个桔子，其他的，你拿走吧。", "6. I can’t finish this fruit. Leave me two tangerines; you take the rest. (其他的; object)"), ("你有这么多问题，我现在只能回答一个，明天再回答其他的。", "7. You have so many questions; I can only answer one now and will answer the others tomorrow. (其他的; object)"), ("除了这些问题，还有别的吗？", "8. Besides these questions, are there any others? (别的; verb 有)")]
L3 = lesson(
    "Lesson 17 Presentation 2 grammar: the demonstrative pronoun 其他/别的",
    "其他活动 · 别的爱好 · 其他的 · 有别的",
    requires=[],
    cards=[
        card("The Demonstrative Pronoun 其他/别的",
             "The demonstrative pronouns 其他 and 别的 are almost the same as “other.” They can be placed before nouns and used as subjects and objects, but there are slight differences between them. 其他 can be used with numbers and measure words, but 别的 cannot. 其他 can also be used with or without 的. 其他 + Number + Measure Word + Noun; 别的 + Noun. When 其他 is used as an object, it is usually accompanied by 的 (as a subject 其他 can stand without 的; 别的 can be used as a subject, an object and an attribute, with or without 的). 别的 is usually used as an object instead of 其他 if the verb is “有” or “没有”.",
             examples=[D(z, e) for z, e in QB]),
        card("Activity 3 (Reading and Speaking): 考考你",
             "A. Complete the sentences using 其他 or 别的. B. Discuss the answers with a classmate and explain why you chose either 其他 or 别的 in the sentences. The book leaves the key out; my completed sentences (mine):",
             examples=[D(z, e) for z, e in QB3]),
    ],
    exercises=[
        M("Which can be used with a number and a measure word?", "其他", ["别的", "Both", "Neither"], "其他 + number + measure word + noun."),
        M("Which is usually used as the object after 有 or 没有?", "别的", ["其他", "Both equally", "Neither"], "有别的 / 没有别的."),
        M("What does 其他 take when it is an object?", "的", ["了", "过", "着"], "其他的."),
        M("Which fits 其他___五个人都通过了 (the other five)?", "其他", ["别的", "其他的", "另外的"], "其他 + number."),
        M("Which fits 你有___颜色的吗？", "别的", ["其他五", "其他几", "其他一个"], "别的 + noun."),
        M("Which fits 除了中文，你还会说___外语吗？", "别的", ["其他五", "其他一", "其他两"], "别的 + noun."),
        F("除了这些问题，还有___吗？", "别的", PART, "还有别的."),
        F("家里___人都去了国外，只有他一个人在国内。", "其他", PART, "其他人."),
        F("这些水果我吃不了。给我留两个桔子，___的，你拿走吧。", "其他", PART, "其他的 as object."),
    ],
)

# ------------------------------------------------------------------ 4. 从…起
CQ = [("我从一月一号起，每天会去健身房运动。", "Starting from January 1st, I will go to the gym every day. (Subject + 从…起)"), ("从一月一号起，我每天会去健身房运动。", "From January 1st on, I will go to the gym every day. (从…起 at the beginning)"), ("这个大楼不太方便，从三楼起才有电梯。", "This building is not very convenient; there are elevators only from the third floor up."),
      ("从明天开始，我每天去体育馆游泳。", "From tomorrow on, I will go swimming at the gym every day. (从…开始 = 从…起)"), ("从下个星期开始，我们要学习第四单元的课本。", "From next week on, we will study the textbook of Unit 4.")]
CQ4 = [("你最近胖了不少，得减肥了。", "1. A: You’ve gotten quite a bit fatter recently; you have to lose weight."), ("从明天起，我每天早上去跑步。", "B: From tomorrow on, I’ll go running every morning. (mine)"), ("你几岁开始学滑冰的？", "2. A: At what age did you start to learn ice skating?"), ("我从七岁起就开始学滑冰了。", "B: I started learning ice skating at the age of seven. (mine)"),
       ("这个小区环境怎么样？", "3. A: How is the environment in this neighborhood?"), ("很不错，从搬来这里起，我每天早上都能听到小鸟唱歌。", "B: Very nice; ever since I moved here I can hear the birds sing every morning. (mine)"), ("听说这个周末梅西百货商店的衣服大降价。", "4. A: I heard the clothes at Macy’s will be on sale this weekend."), ("对，从这个周末起，所有的衣服都打五折。", "B: Yes, from this weekend on all the clothes are half price. (mine)"),
       ("中国的学生从什么时候开始学外语？", "5. A: From when do students in China start to learn foreign languages?"), ("从小学三年级起就开始学英语了。", "B: They begin learning English from the third grade of elementary school. (mine)")]
CQ5 = [("我的爱好是游泳。从五岁起我就开始学游泳了。", "My hobby is swimming. I began learning to swim from the age of five. (the book’s starter; the continuation is mine)"), ("我每年夏天都去海边游泳。", "I go swimming at the beach every summer. (mine)"), ("从去年起，我每个星期都去学校的游泳馆练习两次。", "Since last year, I have practiced at the school pool twice every week. (mine)"), ("游泳不但对身体好，而且可以让我放松。", "Swimming is not only good for the body but also lets me relax. (mine)"), ("除了游泳以外，我还喜欢爬山和露营什么的。", "Besides swimming, I also like hiking, camping and so on. (mine)")]
L4 = lesson(
    "Lesson 17 Presentation 2 grammar: the prepositional structure 从……起",
    "从一月一号起 · 从三楼起才有电梯 · 从…开始",
    requires=[],
    cards=[
        card("The Prepositional Structure 从……起",
             "从……起 means “from … on” and indicates the beginning of something. It is used as an adverbial adjunct between the subject and the predicate. It can also be placed at the beginning of a sentence. Subject + 从…起，+ Predicate; 从…起，Subject + Predicate. 从……起 can be replaced by 从……开始 and carry the same meaning.",
             examples=[D(z, e) for z, e in CQ]),
        card("Activities 4 and 5",
             "Activity 4 (Listening, Writing and Speaking). A. Listen to the dialogs and write responses using the pattern 从…起. B. Work in pairs to practice the dialogs (you can also read from the script provided by the teacher). The five questions are printed in the book; the answers are blank, so mine follow. Activity 5 (Writing and Speaking). In groups, write at least five sentences about your favorite hobby using 从…起 and tell your story to your group; the book’s starter is 我的爱好是游泳。从五岁起我就开始… My story (mine):",
             examples=[D(z, e) for z, e in CQ4] + [D(z, e) for z, e in CQ5]),
    ],
    exercises=[
        M("What does 从…起 indicate?", "The beginning of something (from … on)", ["The end of something", "The place", "The reason"], "从…起: from … on."),
        M("What can replace 从…起?", "从…开始", ["从…到", "跟…", "对…"], "Same meaning."),
        M("Where can 从…起 appear?", "Before the subject or between subject and predicate", ["Only at the end", "After the object", "Only in questions"], "Two positions."),
        M("What does 从三楼起才有电梯 mean?", "There are elevators only from the third floor up", ["There is no elevator", "Elevators on the third floor only", "Three elevators"], "从三楼起."),
        M("Which sentence is correct?", "我从七岁起就开始学滑冰了", ["我起从七岁就开始学滑冰了", "我七岁从起就学滑冰了", "从起我七岁开始"], "从…起 around the time."),
        M("What does 从明天开始，我每天去体育馆游泳 mean?", "From tomorrow on I will swim at the gym every day", ["I swam yesterday", "I never swim", "I swim at home"], "从明天开始."),
        F("从一月一号___，我每天会去健身房运动。", "起", PART, "从…起."),
        F("我___六岁起就开始滑雪了。", "从", PART, "从…起."),
    ],
)

# ------------------------------------------------------------------ 5. 简直
JZ = [("你能教我滑雪，太棒了。我简直等不及了。", "It is great that you can teach me to ski. I simply cannot wait."), ("她男朋友长得简直太帅了。", "Her boyfriend is simply so handsome."), ("我简直不知道该怎么谢你。", "I just don’t know how I should thank you."), ("这个地方简直太美了！", "This place is simply so beautiful! (correct)"), ("这个地方简直美极了！", "This place is simply beautiful! (correct)")]
JZ6 = [("这个菜简直太辣了，我吃不了。", "1. This dish is simply so spicy; I can’t eat it. (the incorrect version is 简直辣了; key mine)"), ("天气这么热，我简直睡不着。", "2. The weather is so hot that I simply can’t sleep. (the incorrect version is 我睡不着简直)"), ("这件大衣简直太漂亮了，我想再买一件给我姐姐。", "3. This coat is simply so beautiful; I want to buy another one for my older sister. (the incorrect version is 简直漂亮)"),
       ("昨晚的音乐会上，她简直太紧张，忘了怎么唱了。", "4. At last night’s concert she was simply so nervous that she forgot how to sing. (the incorrect version is 她简直紧张)"), ("公共汽车太挤了，我简直挤不上去。", "5. The bus was so crowded that I simply couldn’t get on. (the incorrect version is 我挤不上去简直)")]
JZ7 = [("这个电影院的座位简直太舒服了！", "1. The seats in this theater are simply so comfortable! (mine)"), ("这个电影简直好看极了。", "The movie is simply great. (mine)"), ("这里的山简直太美了，我简直不想回去。", "2. The mountains here are simply so beautiful; I simply don’t want to go back. (mine)"), ("这个露营的地方风景简直美极了，空气也特别好。", "3. The scenery of this campsite is simply gorgeous and the air is especially good. (mine)")]
L5 = lesson(
    "Lesson 17 Presentation 2 grammar: the adverb 简直",
    "简直等不及了 · 简直太帅了 · 简直美极了 · 简直 + 太…了 / …极了",
    requires=[],
    cards=[
        card("The Adverb 简直",
             "The adverb 简直 means “simply” or “completely” in English and can be used to modify adjective phrases or verb phrases, adding a tone of excitement on the part of the speaker. Subject + 简直 + adjective phrase/verb phrase. 简直 cannot be followed directly by an unmodified adjective. The modifiers 太 and 极了 can be used with 简直 to modify adjectives: 这个地方简直美！ is incorrect; 这个地方简直太美了 and 这个地方简直美极了！ are correct.",
             examples=[D(z, e) for z, e in JZ]),
        card("Activity 6 (Reading, Writing and Speaking)",
             "Pair up and read the sentences that use the adverb 简直. Identify the incorrect sentences, discuss why they are incorrect and how to correct them. Then translate them into English. The book prints two versions of each sentence (one correct, one incorrect); the key is mine, and the correct versions are:",
             examples=[D(z, e) for z, e in JZ6]),
        card("Activity 7 (Reading, Writing and Speaking)",
             "What would you say in the following situations? Pair up and comment on the situations with your partner using 简直. 1. You are in a movie theatre with a friend, commenting on the movie, the auditorium or the seats. 2. You are hiking with your friend and admiring the mountains and surroundings. 3. You are camping with your friend and commenting on the environment or surroundings of the campsite. My sentences (mine):",
             examples=[D(z, e) for z, e in JZ7]),
    ],
    exercises=[
        M("What does 简直 add to a sentence?", "A tone of excitement (“simply”)", ["Doubt", "The past", "A question"], "Excitement."),
        M("What may NOT directly follow 简直?", "An unmodified adjective", ["太 + adjective", "A verb phrase", "Adjective + 极了"], "简直美 is wrong."),
        M("Which is correct?", "这个地方简直太美了", ["这个地方简直美", "这个地方简直美了", "这个地方美简直"], "简直 + 太…了."),
        M("Which is also correct?", "这个地方简直美极了", ["这个地方简直美极", "这个地方极了简直美", "这个地方简直极美了"], "简直 + …极了."),
        M("Where does 简直 go in 我简直挤不上去?", "Before the verb phrase", ["At the end", "After 挤", "After 上去"], "Subject + 简直 + VP."),
        M("What does 我简直不知道该怎么谢你 mean?", "I just don’t know how to thank you", ["I don’t want to thank you", "I thanked you", "I know how"], "简直不知道."),
        F("这个菜简直___辣了，我吃不了。", "太", PART, "简直 + 太…了."),
        F("这个地方风景简直美___了！", "极", PART, "美极了."),
        F("公共汽车太挤了，我___挤不上去。", "简直", PART, "简直 before the verb phrase."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
DL = [("张华", "马克，你喜欢什么运动？", "Mark, what sports do you like? (my reconstruction; the book gives this as a listening cloze)"), ("马克", "我喜欢的运动特别多，像游泳、冲浪、滑雪、滑冰、骑自行车、爬山、露营，还有打篮球。我老家四季分明，每个季节可以做不同的运动。张华，你喜欢什么？", "I like a great many sports, such as swimming, surfing, skiing, ice skating, cycling, hiking, camping and also basketball. My hometown has four distinct seasons and each season you can do different sports. Zhang Hua, what do you like?"),
      ("张华", "我喜欢室内运动，像游泳、乒乓球、羽毛球和篮球。我常常参加乒乓球比赛，每次比赛，我都很紧张。", "I like indoor sports, such as swimming, table tennis, badminton and basketball. I often take part in table tennis matches, and every match I get very nervous."), ("马克", "我也很喜欢这些活动，可是我不会打乒乓球，你可以教我吗？", "I like these activities too, but I can’t play table tennis; can you teach me?"),
      ("张华", "可以。我们可以去学校的体育馆练习。", "Yes. We can practice at the school gym."), ("马克", "太好了。我简直等不及了。我需要买什么装备？", "Great. I simply can’t wait. What equipment do I need to buy?"),
      ("张华", "你得买一个球拍，一些乒乓球，还有球鞋和运动服。", "You have to buy a racket, some table tennis balls, and also sneakers and sports clothes."), ("马克", "没问题，我今天下课以后就去体育用品商店买。", "No problem; after class today I’ll go to the sporting goods store to buy them.")]
LH1 = ("林红有两个孩子，都很喜欢运动。儿子今年十二岁，喜欢游泳，女儿今年十岁，喜欢滑冰。每天放学以后，是林红一天最忙的时候，她要先去送儿子去游泳馆游泳，然后再送女儿去滑冰场学滑冰。林红的先生是电脑工程师，每天很忙，没有时间，只好林红一个人接送孩子。送完孩子以后，她马上回家做晚饭，她想在孩子们回家以前把饭做好，因为她知道孩子们回家以后会又累又饿，需要马上吃饭。她一边做饭一边看时间，到五点半的时候，她得开车去把孩子们一个一个地接回家。孩子们吃完饭还得做功课，所以不能太晚去接他们。林红常常想，如果在她家附近能有一个体育馆该有多好啊。体育馆里最好有游泳池和滑冰场，这样她就不用每天开车跑这么多个地方了。")
LH1_E = ("Lin Hong has two children, and both like sports. Her son is twelve this year and likes swimming; her daughter is ten and likes ice skating. After school every day is Lin Hong’s busiest time of the day: she first takes her son to the swimming pool to swim and then takes her daughter to the skating rink to learn skating. Lin Hong’s husband is a computer engineer and is very busy every day with no time, so Lin Hong has to pick up and drop off the children alone. After dropping off the children, she goes home right away to cook dinner; she wants to have the meal ready before the children get home, because she knows that when they get home they will be both tired and hungry and will need to eat right away. She watches the time while cooking, and at five-thirty she has to drive and pick the children up one by one. After dinner the children still have to do homework, so she can’t go to pick them up too late. Lin Hong often thinks how nice it would be if there were a gym near her home. It would be best if the gym had a swimming pool and a skating rink; that way she wouldn’t have to drive to so many places every day.")
TF = [("林红的两个孩子都喜欢游泳。", "1. Both of Lin Hong’s children like swimming. — False (the son swims, the daughter skates; key mine)"), ("林红的孩子每天放学以后先不回家。", "2. Lin Hong’s children do not go home first after school. — True"), ("每天不是林红接送孩子就是她先生接送。", "3. Either Lin Hong or her husband picks up and drops off the children every day. — False (her husband has no time)"), ("孩子回到家以后，林红才给他们做饭。", "4. Lin Hong only cooks for the children after they get home. — False (she cooks before they get home)"), ("林红家附近有一个大体育馆，里面什么都有。", "5. There is a big gym near Lin Hong’s home with everything in it. — False (she only wishes for one)")]
LH2 = ("下个月，林红的孩子就要放寒假了。因为孩子们都喜欢运动，林红打算带孩子们去一个既可以度假又可以运动的地方。昨天她在电视上看到一个滑雪度假村的广告。这个度假村是新开的，看起来又大又漂亮，而且离家很近，开车不到两个小时。滑雪设备可以自己带，也可以在那儿租。如果不会滑雪也没关系，这个度假村提供初级滑雪课，教你怎么滑。滑雪度假村的设施也很全，有中、西式餐厅、咖啡厅、滑雪用具商店、超市等服务设施，随时为滑雪者提供一流的服务。林红觉得这是个度假的好地方，她打算上网订票，然后一家人准备去那儿滑雪。")
LH2_E = ("Next month Lin Hong’s children will be on winter vacation (寒假 hánjià). Because the children all like sports, Lin Hong plans to take them to a place where they can both take a vacation and exercise. Yesterday she saw an advertisement on TV for a ski resort. This resort is newly opened and looks big and beautiful, and it is close to home, less than two hours by car. You can bring your own ski equipment or rent it there. If you don’t know how to ski it doesn’t matter; the resort offers beginner ski classes that teach you how to ski. The resort’s facilities are also complete, with Chinese and Western restaurants, a coffee shop, ski-gear stores, a supermarket and other service facilities, offering skiers first-class service at any time. Lin Hong thinks this is a good place for a vacation; she plans to book tickets online and then the family will go skiing there.")
T4 = table(["时间", "平日", "周末", "元旦、春节期间"],
           [["2 小时", "120 元/人", "180 元/人", "200 元/人"], ["3 小时", "140 元/人", "200 元/人", "240 元/人"], ["4 小时", "160 元/人", "240 元/人", "280 元/人"], ["5 小时", "180 元/人", "280 元/人", "320 元/人"], ["6 小时", "200 元/人", "320 元/人", "340 元/人"], ["7 小时", "220 元/人", "360 元/人", "380 元/人"], ["8 小时", "240 元/人", "390 元/人", "420 元/人"],
            ["夜场", "120 元/人/场", "", ""], ["门票", "20 元/人", "20 元/人", "30 元/人"]], title="滑雪消费价格 (ski prices; the book prints one cell as 240 元人, here 240 元/人)")
T4b = table(["自带雪具滑雪票", "价格"], [["平日 4 小时滑雪", "130 元/人"], ["平日全天滑雪", "150 元/人"], ["周末及假日 4 小时滑雪", "190 元/人"], ["周末及假日全天滑雪", "230 元/人"]], title="自带雪具 (own equipment)")
T4c = table(["出租 / 其他", "价格"], [["头盔", "30 元/个"], ["滑雪服", "30 元/套"], ["滑雪镜", "20 元/副/次"], ["雪具养护", "100-200 元/套"], ["存衣柜", "20 元/个"], ["VIP 室", "300 元/小时/间"]], title="雪具租用和 VIP 室 (rentals and VIP room)")
L6 = lesson(
    "Lesson 17 Presentation 2: skill integration",
    "你喜欢什么运动 · 林红的孩子 · 滑雪度假村 · 滑雪消费价格",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading and Speaking)",
             "A. Listen to the conversation and transcribe the missing information in pinyin that you heard; then translate it into English orally. The book prints the conversation with blanks (audio, not included); my reconstruction of the whole conversation from the surrounding text, so the filled-in words are mine. B. Write down any words you don’t know and discuss their meanings with your partner. C. Pair up and read the conversation aloud. D. Discuss: 1. What is the topic of this conversation? 2. What is the relationship between these two speakers? How can you tell? 3. Among the activities mentioned, which one do you enjoy doing? Explain why. Make notes on what your partner likes to do and why (喜欢做的 / 原因).",
             examples=dlg(DL)),
        card("Activity 2 (Reading and Speaking): Lin Hong’s children",
             "A. Read the passage and write a summary of it in pinyin or characters. B. Read the passage again and mark each statement as True or False (key mine). C. Pair up and discuss: 1. 美国的孩子放学以后也去做运动吗？他们都做什么运动？ 2. 美国的妈妈们是不是也和林红一样每天去接送孩子？",
             examples=[D(LH1, LH1_E)] + [D(z, e) for z, e in TF]),
        card("Activity 3 (Reading, Writing and Speaking): the ski resort",
             "A. Read the passage and write a short summary in pinyin or characters. B. Pair up and exchange your summaries. C. Translate the sentence 滑雪度假村的设施也很全，有中、西式餐厅、咖啡厅、滑雪用具商店、超市等服务设施，随时为滑雪者提供一流的服务 into English (my translation: The ski resort’s facilities are also complete, with Chinese and Western restaurants, coffee shops, ski-equipment stores, supermarkets and other service facilities, providing skiers with first-class service at any time). D. Discuss: 1. 你会滑雪吗？你从什么时候开始滑雪的？ 2. 你通常去哪里滑雪？ 3. 在美国，你去过滑雪度假村滑雪吗？这个度假村在哪儿？ 4. 这个度假村都有什么设施？ 5. 你第一次滑雪是什么时候？请讲讲你第一次滑雪的经历。",
             examples=[D(LH2, LH2_E)]),
        card("Activity 4 (Reading, Writing and Speaking): ski prices",
             "A. Pair up, read the information in the table below about a ski resort in China and answer the questions: 1. What information is conveyed? 2. How does the price per person differ? 3. Can you save money by using your own equipment? What are the rates? 4. How much would it cost if you rent the equipment? 5. What is said about the VIP room? B. Check your answers with your partner. C. Discuss: 1. 你觉得这个滑雪场贵不贵？你会去这里滑雪吗？为什么？ 2. 美国的滑雪场怎么样？比这个滑雪场贵还是便宜？ 3. 美国的滑雪场有没有 VIP 室？你认为 VIP 室会有什么样的服务？ The prices are in yuan (元); the book’s VIP notes: 1. It must be booked one day in advance with a 50% deposit; if you do not arrive on time it is held for one hour. 2. A small conference room is available; the projector costs 100 yuan per use.",
             tables=[T4, T4b, T4c]),
    ],
    exercises=[
        M("What does Lin Hong do right after school?", "Takes her son to swim, then her daughter to skate", ["Goes to work", "Goes shopping", "Does homework"], "先送儿子去游泳馆…再送女儿去滑冰场."),
        M("Why does Lin Hong alone take the children?", "Her husband is very busy", ["He lives far away", "He doesn’t drive", "He doesn’t like sports"], "先生…每天很忙，没有时间."),
        M("Why does she cook before they get home?", "They will be tired and hungry", ["She likes cooking early", "They eat out", "Her husband is hungry"], "又累又饿."),
        M("What does she wish for?", "A gym near home with a pool and skating rink", ["A new car", "A bigger house", "More children"], "附近能有一个体育馆."),
        M("What is the ski resort in the passage like?", "Newly opened, big and beautiful, under two hours’ drive", ["Old and small", "Very far", "In another country"], "新开的…开车不到两个小时."),
        M("What if you can’t ski?", "The resort offers beginner classes", ["You can’t go", "You must bring a coach", "You must pay double"], "提供初级滑雪课."),
        M("Weekday 4-hour ski price?", "160 yuan per person", ["120 yuan", "240 yuan", "280 yuan"], "平日 4 小时 160 元/人."),
        M("Weekend 4-hour ski price?", "240 yuan per person", ["160 yuan", "280 yuan", "190 yuan"], "周末 4 小时 240 元/人."),
        M("Weekday 4 hours with your own equipment?", "130 yuan per person", ["160 yuan", "150 yuan", "190 yuan"], "自带雪具 平日 4 小时 130 元/人."),
        M("What is the VIP room price?", "300 yuan per hour per room", ["100 yuan per use", "50 yuan", "30 yuan per piece"], "300 元/小时/间."),
        F("林红打算带孩子们去一个既可以度假___可以运动的地方。", "又", PART, "既…又…"),
        F("她想在孩子们回家以前把饭做___。", "好", PART, "做好."),
    ],
)

# ------------------------------------------------------------------ 7. context
WORDS = table(["Word bank (词汇)"], [["海边"], ["海景"], ["风景"], ["晒太阳"], ["躺"], ["草地"], ["比赛"], ["游泳"], ["冲浪"], ["踢球"], ["骑自行车"], ["滑雪"], ["滑冰"], ["爬山"], ["露营"]], title="Activity 1: outdoor activities and settings (the book prints them as a word cloud)", say=[0])
SKI_AD = [("欢乐滑雪，畅玩无限", "Happy skiing, endless fun."), ("香山滑雪场", "Xiangshan Ski Resort"), ("截止日期：十二月三十一日", "Deadline: December 31."), ("盛大开业，全场五折", "Grand opening: everything half price."), ("详情请电：四零零，六一七，八八八八", "For details please call 400-617-8888 (read digit by digit).")]
PLAN = [("第一天：在蒙特雷海边骑自行车，去渔人码头看海景。", "Day 1: ride bikes along the Monterey shore and go to Fisherman’s Wharf to see the sea view. (my sample plan; mine)"), ("第二天：去卡梅尔的海滩晒太阳，躺在草地上休息。", "Day 2: sunbathe on the beach at Carmel and rest lying on the grass."), ("第三天：开车去大苏尔爬山、露营，看海景。", "Day 3: drive to Big Sur to hike, camp and see the coast."), ("第四天：开车去圣克鲁斯冲浪，开车不到一个半小时。", "Day 4: drive to Santa Cruz to surf, less than an hour and a half by car."), ("第五天：开车去旧金山玩一天，晚上回来。", "Day 5: drive to San Francisco for a day and come back in the evening.")]
L7 = lesson(
    "Lesson 17 Presentation 2: using Chinese in context",
    "家乡的户外活动 · 刘冲一家的户外活动安排 · 香山滑雪场",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking): role play",
             "Role-play: You are studying Chinese in a university in China. While at a weekend party at your Chinese teacher’s house you are talking with one of your teacher’s friends who likes outdoor activities very much, so you exchange information about activities in your hometown. A. Pair up. Your partner plays the role of the Chinese friend. Discuss outdoor activities during the seasons in your hometown (the vocabulary below is a cue). B. In pairs, discuss your favorite outdoor activity with your partner and explain why you enjoy it (最喜欢的户外活动 / 为什么喜欢这个活动 for 你自己 and 你的朋友). (Photograph, not included.)",
             tables=[WORDS]),
        card("Activity 2 (Listening, Reading, Writing and Speaking): Liu Chong’s family",
             "Scenario: You received a voice mail from your Chinese friend in Beijing. Your friend told you that his family would be visiting Monterey next month and asked you to make arrangements for outdoor activities during their stay. You asked your classmates to help you to think about the things your Chinese friends could do. A. Listen to the recording and write a summary of what you heard. (Audio, not included.) B. Divide into two groups. In your group, discuss an outdoor activity plan for Liu Chong’s family. Consider: 1. 刘冲一家在蒙特雷只呆五天。 2. 他们喜欢户外活动。 3. 选择适合他们的活动。 4. 最好在蒙特雷附近或是开车不超过四个小时。 C. After discussion with your group members, write down your arrangements for the outdoor activities (给刘冲一家的户外活动安排). D. Each group takes turns presenting their plan and the class selects the best one. Email the best plan to Liu Chong. The book leaves the plan blank; a sample plan (mine):",
             examples=[D(z, e) for z, e in PLAN]),
        card("Activity 3 (Reading, Writing and Speaking): the ski-resort call",
             "Role-play: You are studying Chinese at Beijing University in China. Winter vacation is coming, and you plan to go skiing with your friends. You saw an advertisement for a ski resort, and you’d like to know more about it. Call the resort and ask for the information you need. A classmate will play the role of the receptionist at the resort. A. In pairs, read the advertisement and discuss the content (the book prints the advertisement with pictures, not included). B. Call the ski resort to ask for more information; your partner plays the receptionist. You may use the questions below as a reference and make notes when you speak to the receptionist: 你们的滑雪场在哪儿？ 开车需要多长时间到你们的滑雪场？ 门票一个人多少钱？ 我不会滑雪，你们有人教怎么滑雪吗？ 可以自己带滑雪设备吗？ 你们出租滑雪设备吗？你们都有什么设备？ 有吃饭的地方吗？ 有没有住的地方？一个晚上多少钱？ 滑雪场可以上网吗？ 滑雪场有商店吗？ 你们有停车场吗？停车场收费吗？ 其他问题。",
             examples=[D(z, e) for z, e in SKI_AD]),
    ],
    exercises=[
        M("What is the ski resort in the advertisement called?", "香山滑雪场", ["欢乐滑雪场", "无限滑雪场", "北京滑雪场"], "香山滑雪场."),
        M("What is the opening offer?", "Everything half price", ["Free tickets", "Free rental", "A free night"], "盛大开业，全场五折."),
        M("When does the offer end?", "December 31", ["January 1", "June 30", "October 1"], "截止日期：十二月三十一日."),
        M("How long will Liu Chong’s family stay in Monterey?", "Five days", ["Two days", "A month", "A week"], "只呆五天."),
        M("What is the limit on the driving distance for their plan?", "No more than four hours", ["One hour", "Ten hours", "No limit"], "开车不超过四个小时."),
        M("What do Liu Chong’s family like?", "Outdoor activities", ["Shopping", "Museums", "Concerts"], "他们喜欢户外活动."),
        M("What do you ask the resort receptionist?", "Where it is, how long to drive, ticket price, lessons, rentals, food, lodging, parking", ["Only the price", "Only the phone number", "Nothing"], "Questions listed."),
        M("What should you do with the activity plan?", "Present it to the class, then email the best one to Liu Chong", ["Throw it away", "Keep it secret", "Call him"], "Email the best plan."),
        F("你们的滑雪场在哪___？", "儿", PART, "哪儿: where."),
        F("滑雪场有停车___吗？", "场", PART, "停车场."),
    ],
)
L8 = vocab_lesson("Lesson 17 Presentation 2 vocabulary", "17 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十七课 体育健身 Presentation 2: outdoor activities, 才, 其他/别的, 从…起, 简直, Lin Hong and the ski resort", [L1, L2, L3, L4, L5, L6, L7, L8])
