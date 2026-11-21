"""Unit 43: Lesson 15 (Social Gathering) Presentation 2 from the book's texts: the housewarming visit dialog, the 想 + V + 什么
+ 就 + V + 什么 construction, the verb 让, the complement of potentiality (2), the skill-integration and using-Chinese
activities and the vocabulary list. Audio, pictures and telephone hot-lines as digits are handled as noted: the book writes
numbers as digits and they are spelled out here so every spoken line is Chinese; answer keys the book does not print are mine."""
from zh_auto import *
from zh_l15_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("班长", 1, "zhang3"), ("睡觉", 1, "jiao4"), ("教您", 0, "jiao1"), ("尝到", 0, "chang2"), ("找得到", 1, "de5"), ("没收到", 0, "mei2")):
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
P2 = [("老张", "王文来啦，快请进。", "Wang Wen is here! Please come in."), ("王文", "对不起，让你们久等了。老张，这是一点小礼物。", "Sorry to have kept you waiting. Lao Zhang, here is a little gift."),
      ("老张", "哎呀，人来就行了，什么都不用带。", "Oh, just coming is enough; you don’t need to bring anything."), ("王文", "一点儿小意思。是我去景德镇出差时买的一套茶具。", "Just a small token. It’s a tea set I bought when I went to Jingdezhen on a business trip."),
      ("老张", "那我就收下了，谢谢。", "Then I’ll accept it, thanks."), ("王文", "你们的新房子真大，小区也很漂亮。", "Your new house is really big, and the neighborhood is lovely too."),
      ("老张", "是呀，比以前住的公寓大多了，小区里很安静，学区也不错。离超市和社区医院都很近，生活非常方便。", "Yes, it’s much bigger than the apartment we lived in before; the neighborhood is quiet and the school district is good. It’s very close to the supermarket and the community clinic, so life is very convenient."),
      ("王文", "太好了。真为你们高兴。", "Great. I’m really happy for you."), ("老张", "来，这边坐。饮料、零食都在桌上，喜欢什么就吃什么。对了，你们几位都认识吧？", "Come, sit over here. Drinks and snacks are on the table; eat whatever you like. By the way, you all know each other, right?"),
      ("王文", "认识认识，以前都见过面。", "Yes, yes, we’ve all met before."), ("老张", "太好了。那你们先聊着，我去厨房帮我太太准备晚饭。", "Great. Then you chat first; I’ll go to the kitchen to help my wife prepare dinner."),
      ("王文", "早就听说陈姐饭做得特别好，今天终于有机会尝尝了。有什么需要我帮忙的吗？", "I heard long ago that Sister Chen cooks especially well; today I finally have the chance to taste. Is there anything I can help with?"),
      ("老张", "不用不用，都是家常便饭，马上就好。", "No need, no need; it’s just home cooking and will be ready soon.")]
AC4 = [("人来就行了，什么都不用带。", "(就行了; 什么都) Just coming is enough; you don’t need to bring anything. (mine)"), ("你们先坐着，我去倒茶。", "(先 verb 着) You sit first; I’ll go pour tea. (mine)"), ("听说你们搬家了，我真为你们高兴。", "(为…高兴) I heard you moved; I’m really happy for you. (mine)"), ("那就这么定了，星期六见。", "(就这么定了) Then it’s settled; see you Saturday. (mine)"),
       ("有什么需要我帮忙的吗？", "(有什么需要…?) Is there anything I can help with? (mine)"), ("你喜欢什么就吃什么。", "(什么…什么…) Eat whatever you like. (mine)"), ("我早就听说你们的小区很漂亮。", "(早就 + verb) I heard long ago that your neighborhood is lovely. (mine)"), ("对了，你们认识吧？", "(对了) By the way, you know each other, right? (mine)"), ("你们的新房子真大！", "(真 + adj.) Your new house is really big! (mine)")]
L1 = lesson(
    "Lesson 15 Presentation 2: visiting the new home",
    "对不起，让你们久等了 · 一点小意思 · 喜欢什么就吃什么",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: a gathering and an elderly couple (not included). Pair up and discuss: A. What would you bring if you were invited to a housewarming party? B. What would guests be likely to talk about at a housewarming party?"),
        card("Presentation 2: 到老张家",
             "The book also prints the dialog in traditional characters. Notes: 1. 对了: in addition to “correct”, 对了 can also be used to indicate “by the way”. For example 对了，小王，今年你想在哪里过春节？ 2. 先 + verb + 着 is an idiomatic expression used to be excused from an ongoing action or state. For example 你们先吃着，我去打个电话；你先坐着，我马上就回来。 3. 早就 V = 很早以前就 V.",
             examples=dlg(P2) + [D("对了，小王，今年你想在哪里过春节？", "By the way, Xiao Wang, where do you want to spend Spring Festival this year?"), D("你们先吃着，我去打个电话。", "You go ahead and eat; I’ll go make a phone call."), D("你先坐着，我马上就回来。", "You sit down first; I’ll be right back.")]),
        card("Activities 1 to 3",
             "Activity 1 (Listening and Speaking). A. Global listening: 1. What occasion is discussed? 2. What are Lao Zhang and his wife serving their guests? B. Detailed listening: 1. What gift did Wang Wen bring? 2. What did you hear about Lao Zhang’s new home? 3. Has Wang Wen eaten food prepared by Lao Zhang’s wife before? What did he say? (Audio, not included. From the text: a housewarming; drinks, snacks and a home-style dinner; a tea set from Jingdezhen; big, a quiet neighborhood, good school district, near the supermarket and community clinic; no, but he had heard long ago she cooks especially well.) Activity 2 (Listening, Speaking and Reading). A. Listen to six dialogs and translate them into English. B. Pair up, compare your translations and take turns translating the sentences back into Chinese. Activity 3 (Listening, Speaking, and Reading). A. Listen to the message and write the main idea in English. B. Listen again and fill in the table (Details: Wang Li; New Home; Surroundings & Facilities; The Party). C. Rewrite the passage as a dialog between 小玉 and 王丽 (four exchanges). (Audio, not included.)"),
        card("Activity 4 (Writing and Speaking)",
             "A. Use the expressions provided to write complete sentences: 1. 就行了; 什么都 2. 先 verb 着 3. 为…高兴 4. 就这么定了 5. 有什么需要…? 6. 什么…什么… 7. 早就 + verb 8. 对了 9. 真 + adj. B. Pair up and take turns saying one of your sentences in English; your partner repeats it in Chinese. My sentences (mine):",
             examples=[D(z, e) for z, e in AC4]),
    ],
    exercises=[
        M("What did Wang Wen bring?", "A tea set from Jingdezhen", ["Fruit", "Flowers", "Wine"], "一套茶具."),
        M("Why does Lao Zhang say not to bring anything?", "Just coming is enough", ["He has everything", "It is rude", "He is rich"], "人来就行了，什么都不用带。"),
        M("How does the new house compare with the old apartment?", "Much bigger", ["Smaller", "The same", "Older"], "比以前住的公寓大多了。"),
        M("What is near the new home?", "A supermarket and a community clinic", ["An airport", "A zoo", "A factory"], "离超市和社区医院都很近。"),
        M("What can guests eat?", "Whatever they like from drinks and snacks", ["Only fruit", "Nothing", "Only dinner"], "喜欢什么就吃什么。"),
        M("What does Lao Zhang go to do?", "Help his wife prepare dinner in the kitchen", ["Take a nap", "Go shopping", "Make a call"], "去厨房帮我太太准备晚饭。"),
        M("What had Wang Wen heard about Chen Jie?", "She cooks especially well", ["She is a doctor", "She is a teacher", "She dislikes cooking"], "早就听说陈姐饭做得特别好。"),
        M("What does 家常便饭 mean here?", "Home-style food", ["A fancy banquet", "Fast food", "Takeout"], "家常便饭."),
        M("What does 你们先聊着 mean?", "You carry on chatting first", ["Stop talking", "Don’t chat", "Chat later"], "先 + verb + 着."),
        M("What does 对了 mean in 对了，你们几位都认识吧？", "By the way", ["Correct", "Wrong", "Goodbye"], "对了: by the way."),
        M("What does 早就听说 mean?", "Heard a long time ago", ["Will hear soon", "Never heard", "Just heard"], "早就 V = 很早以前就 V."),
        F("老张：哎呀，人来就___了，什么都不用带。", "行", PART, "就行了: it’s enough."),
    ],
)

# ------------------------------------------------------------------ 2. 想+V+什么+就+V+什么
SW = [("我们是老朋友了，你想说什么就说什么。", "We’re old friends; say whatever you want to say.")]
SW1 = [("你想买什么就买什么。", "Buy whatever you want."), ("他们要去哪儿就去哪儿。", "They go wherever they want to go."), ("她不能想请谁就请谁。", "She can’t invite whoever she wants."), ("他不是喜欢什么时候来就什么时候来。", "It’s not that he comes whenever he likes."), ("我要买多少就买多少吗？", "Can I buy as much as I want?"), ("我是不是想怎么做就怎么做？", "Can I do it however I want?")]
SW2 = [("在饭馆点菜", "甲：你想吃什么就点什么。乙：好，我想吃什么就点什么，别客气。", "A: Order whatever you want to eat. B: OK, I’ll order whatever I want; no need to be polite. (mine)"), ("去电影院看电影", "甲：我们看什么电影？乙：你想看什么就看什么。", "A: What movie shall we watch? B: Watch whatever you want. (mine)"), ("什么时候吃晚饭", "甲：我们什么时候吃晚饭？乙：你想什么时候吃就什么时候吃。", "A: When shall we have dinner? B: Whenever you want. (mine)"), ("去哪儿买衣服", "甲：我们去哪儿买衣服？乙：你喜欢去哪儿就去哪儿。", "A: Where shall we buy clothes? B: Wherever you like. (mine)")]
L2 = lesson(
    "Lesson 15 Presentation 2 grammar: 想 + Verb + 什么 + 就 + Verb + 什么",
    "喜欢什么就吃什么 · 你想买什么就买什么 · 想怎么做就怎么做",
    requires=[],
    cards=[
        card("The 想 + Verb + 什么 + 就 + Verb + 什么 construction",
             "This construction indicates that one can do as one likes. The question word 什么 serves as a reference to an open/unnamed object. Instead of 想 you can also use 要, 愿意, 喜欢, etc.; other question words such as 谁, 哪儿, 多少, 什么时候 and 怎么 can also be used this way. Affirmative: 想 + Verb + Question Word + 就 + Verb + Question Word. Negative: 不(是/能) 想 + Verb + Question Word + 就 + Verb + Question Word. Interrogative: 想 + Verb + Question Word + 就 + Verb + Question Word + 吗？ / 是不是想 + Verb + Question Word + 就 + Verb + Question Word？",
             examples=[D(z, e) for z, e in SW + SW1]),
        card("Activities 1 and 2",
             "Activity 1 (Listening, Speaking, and Reading). A. Listen to six sentences and complete them with the construction: 1. 你愿意 ___。 2. 你想 ___。 3. 你要 ___。 4. 你愿意 ___。 5. 你想 ___。 6. 你喜欢 ___。 B. Take turns translating each sentence into English; your partner repeats it in Chinese. (Audio, not included.) Activity 2 (Speaking, Writing, and Reading). A. Pair up. Using the scenarios (在饭馆点菜, 去电影院看电影, 什么时候吃晚饭, 去哪儿买衣服) ask your partner a question; they answer with the construction or its variations; write the sentences in Chinese. B. Share two interactions with the class. My interactions (mine):",
             examples=[D(b, e) for _, b, e in SW2]),
    ],
    exercises=[
        M("What does 想 + V + 什么 + 就 + V + 什么 express?", "Doing as one likes", ["Not knowing what to do", "Refusing", "Asking a question"], "As one likes."),
        M("What does 你想买什么就买什么 mean?", "Buy whatever you want", ["What do you want to buy?", "Don’t buy anything", "Buy nothing"], "你想买什么就买什么."),
        M("What does 他们要去哪儿就去哪儿 mean?", "They go wherever they want", ["They don’t go anywhere", "Where do they go?", "They can’t go"], "哪儿…哪儿."),
        M("What does 她不能想请谁就请谁 mean?", "She can’t invite whoever she wants", ["She invites everyone", "She invites nobody", "Who does she invite?"], "不能想…就…"),
        M("Which question words can be used this way?", "谁, 哪儿, 多少, 什么时候, 怎么", ["Only 什么", "Only 吗", "Only 为什么"], "Other question words."),
        M("Which verb can replace 想?", "要, 愿意, 喜欢", ["吗", "了", "过"], "Variants."),
        M("How does 我们是老朋友了，你想说什么就说什么 sound?", "Encouraging: say what you like", ["Angry", "Cold", "Silent"], "Free to speak."),
        F("你想买什么___买什么。", "就", PART, "想…就…"),
        F("他们要去哪儿就去___儿。", "哪", PART, "哪儿…哪儿."),
    ],
)

# ------------------------------------------------------------------ 3. 让
RA = [("她让我看她的照片。", "She let me look at her photos. (to let/allow)"), ("老师让我们读两遍课文。", "The teacher asked us to read the text twice. (to ask)"), ("这顿饭让你花了那么多钱，很不好意思。", "This meal made you spend so much money; I feel bad. (to cause)"), ("这里的天气让大家感觉很舒服。", "The weather here makes everyone feel comfortable. (to cause a feeling)"), ("我们都给她让路。", "We all made way for her. (to yield)")]
RB = [("他让我开他的车去银行。", "He let me drive his car to the bank."), ("爸爸、妈妈让她坐飞机回家过春节。", "Her father and mother had her fly home for Spring Festival."), ("她的电子邮件让我想起很多事情。", "Her email reminded me of many things."), ("王老师的话让大家很高兴。", "Teacher Wang’s words made everyone very happy."), ("班长不让我们在教室里说英文。", "The class leader doesn’t let us speak English in the classroom."), ("大家不给他让路。", "Nobody made way for him."), ("军队让你在校外租房住吗？", "Does the military let you rent a place off campus?"), ("下个周末学校让不让你回老家？", "Does the school let you go back to your hometown next weekend?")]
RS = [("老师让我们每天复习生词。", "A teacher asks students to do something: The teacher asks us to review vocabulary every day. (mine)"), ("爸爸妈妈让孩子在周末晚点儿睡觉。", "Parents let children do something: Parents let the kids go to bed later on weekends. (mine)"), ("这个消息让我很高兴。", "Something makes you feel a certain way: This news makes me very happy. (mine)"), ("我让他先走。", "You let someone go first: I let him go first. (mine)")]
L3 = lesson(
    "Lesson 15 Presentation 2 grammar: the verb 让",
    "让你们久等了 · 老师让我们读两遍课文 · 班长不让我们说英文",
    requires=[],
    cards=[
        card("Verb 让",
             "The verb 让 is often used to express: 1. To let or allow someone to do something. 2. To ask someone to do something. 3. To cause something to happen. 4. To cause someone to feel a certain way. 5. To yield. Affirmative: Subject + 让 + Object + Verb (+ Object). Negative: Subject + 不让 + Object + Verb (+ Object). Interrogative: Subject + 让 + Object + Verb (+ Object) + 吗？ Affirmative-negative: Subject + 让不让 + Object + Verb (+ Object)？",
             examples=[D(z, e) for z, e in RA]),
        card("Examples 1 to 8",
             "The book’s examples:",
             examples=[D(z, e) for z, e in RB]),
        card("Activities 3 and 4",
             "Activity 3 (Listening, Writing, Speaking, and Reading). A. Listen to six sentences and write in English what you hear. B. Take turns translating each sentence into Chinese. (Audio, not included.) Activity 4 (Writing and Speaking). A. Write complete sentences using the scenarios given, using 让 in each: a teacher asks students to do something; parents let children do something; something makes you feel a certain way; you let someone go first. B. Pair up and share; take turns asking each other questions using the sentences you both wrote. My sentences (mine):",
             examples=[D(z, e) for z, e in RS]),
    ],
    exercises=[
        M("What does 她让我看她的照片 mean?", "She let me look at her photos", ["She looked at my photos", "She asked me to leave", "She sold me photos"], "让: let."),
        M("What does 老师让我们读两遍课文 mean?", "The teacher asked us to read the text twice", ["The teacher read it twice", "We read it once", "We didn’t read"], "让: ask."),
        M("What does 这里的天气让大家感觉很舒服 mean?", "The weather here makes everyone feel comfortable", ["The weather is bad", "Everyone left", "It rained"], "让: cause a feeling."),
        M("What does 我们都给她让路 mean?", "We all made way for her", ["We blocked her", "We followed her", "We asked her to leave"], "让路: yield."),
        M("How do you say “doesn’t let”?", "不让", ["没让", "让不", "别让"], "Subject + 不让 + Object + Verb."),
        M("What does 班长不让我们在教室里说英文 mean?", "The class leader doesn’t let us speak English in class", ["The class leader speaks English", "We must speak English", "The class leader is absent"], "不让."),
        M("What does 下个周末学校让不让你回老家？ ask?", "Will the school let you go home next weekend?", ["Do you want to go home?", "Where is your hometown?", "Is the school open?"], "让不让."),
        M("What does 王老师的话让大家很高兴 mean?", "Teacher Wang’s words made everyone happy", ["Everyone was angry", "Teacher Wang left", "Everyone left"], "让: cause."),
        F("班长___让我们在教室里说英文。", "不", PART, "不让."),
        F("她的电子邮件让我想起很多事___。", "情", PART, "事情."),
    ],
)

# ------------------------------------------------------------------ 4. potentiality (2)
CP = [("陈姐饭做得好做不好？", "Can Ms. Chen cook well? (potentiality)"), ("陈姐饭做得好。", "Ms. Chen can cook well. (potentiality)"), ("陈姐饭做得特别好。", "Ms. Chen cooks very well. (degree)"), ("陈姐做得好饭吗？", "Can Ms. Chen cook well? (potentiality, object after)"), ("陈姐做得好饭。", "Ms. Chen can cook well."), ("陈姐做饭做得很好。", "Ms. Chen cooks very well. (degree, verb repeated)"),
      ("陈姐做不好饭。", "Ms. Chen cannot cook well. (potentiality negative)"), ("陈姐做饭做得不好。", "Ms. Chen doesn’t cook well. (degree negative)"), ("我记得住电话号码。", "I am able to remember phone numbers. (only potentiality)"), ("我记电话号码记得很好。", "I remember phone numbers well. (only degree)")]
CP5 = [("小李做得好中国菜。", "Cue: 做中国菜，好 (potentiality, the book’s example): Xiao Li can cook Chinese food well."), ("小李做中国菜做得很好。", "(degree) Xiao Li cooks Chinese food very well."),
       ("他写得好中文字。", "(mine, 写中文字，好) He can write Chinese characters well."), ("他写中文字写得很好。", "He writes Chinese characters very well."), ("她说得清楚中文。", "(mine, 说中文，清楚) She can speak Chinese clearly."), ("她说中文说得很清楚。", "She speaks Chinese very clearly."),
       ("我听得懂老师说的话。", "(mine, 老师说的话，听懂) I can understand what the teacher says."), ("我听老师说的话听得很懂。", "(mine) I understand what the teacher says very well. (this degree use is unusual)"), ("他收拾得干净房间。", "(mine, 收拾房间，干净) He can tidy the room clean."), ("他收拾房间收拾得很干净。", "He tidies the room very clean."),
       ("我写得好作业。", "(mine, 写作业，好) I can do the homework well."), ("我写作业写得很好。", "I do homework very well.")]
L4 = lesson(
    "Lesson 15 Presentation 2 grammar: the complement of potentiality (2)",
    "做得好 versus 做得很好 · 记得住 · 做不好饭 versus 做得不好",
    requires=[],
    cards=[
        card("Distinctions between a complement of potentiality and a complement of degree",
             "1. A complement of potentiality never takes an adverbial modifier (such as 很, 非常, 特别), but a complement of degree generally appears with an adverbial modifier of degree. 2. A complement of potentiality can take an object directly after it; a complement of degree cannot and must repeat the verb. 3. A complement of potentiality is negated by placing 不 between the verb and the complement, but a complement of degree is negated by placing 不 after 得. 4. Some words can only be used as complements of potentiality, and some only as complements of degree.",
             examples=[D(z, e) for z, e in CP]),
        card("Activity 5 (Writing and Speaking)",
             "A. Pair up. Create sentence pairs using the given cue: one sentence with a complement of potentiality and the other with a complement of degree. For example, cue: 做中国菜，好 → 小李做得好中国菜 / 小李做中国菜做得很好。 The cues: 写中文字，好; 说中文，清楚; 老师说的话，听懂; 收拾房间，干净; 写作业，好. B. Pair up, compare your work and ask your partner to translate your sentences into English. The book’s example and my pairs (mine; some cues, such as 听懂, naturally fit only one pattern):",
             examples=[D(z, e) for z, e in CP5]),
    ],
    exercises=[
        M("Which complement never takes 很?", "Potentiality", ["Degree", "Both", "Neither"], "Potentiality takes no degree adverb."),
        M("Which complement repeats the verb with an object?", "Degree", ["Potentiality", "Both", "Neither"], "做饭做得很好."),
        M("Which negation is for potentiality?", "做不好饭", ["做得不好", "不做得好", "做好不"], "不 between verb and complement."),
        M("Which negation is for degree?", "做饭做得不好", ["做不好饭", "不做饭好", "做不饭好"], "不 after 得."),
        M("What does 陈姐做饭做得特别好 mean?", "Ms. Chen cooks very well", ["Ms. Chen can cook", "Ms. Chen can’t cook", "Ms. Chen cooks specially"], "Degree."),
        M("What does 陈姐做不好饭 mean?", "Ms. Chen cannot cook well", ["Ms. Chen doesn’t cook well", "Ms. Chen cooks very well", "Ms. Chen cooks late"], "Potentiality negative."),
        M("Which is only a potentiality complement?", "记得住", ["做得很好", "说得很清楚", "跑得很快"], "我记得住电话号码."),
        M("Which sentence is a complement of degree?", "我记电话号码记得很好", ["我记得住电话号码", "我记不住电话号码", "我记得住吗"], "Degree."),
        F("陈姐饭做___特别好。", "得", PART, "做得特别好."),
        F("陈姐做___好饭。", "不", PART, "做不好饭."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
ST2 = ("今天我们家真是热闹。我儿子女儿请了很多朋友来我们家，庆祝我和我太太结婚三十周年。我儿子女儿早就告诉大家，什么东西都不要带，可是朋友们还是带来了各种各样的礼物，有鲜花，有水果，还有艺术品，说是他们的一点儿小意思。老万知道我太太喜欢打乒乓球，就送了她一套乒乓球拍。我喜欢喝茶，我女儿的男朋友就送了我一套日本茶具。大家都是好意，我们只好收下。"
       "今天的菜都是我的一位朋友准备的。他是广东人，广东菜做得特别好。有机会在北方的一个小城市尝到地道的广东菜，让大家非常高兴。今天也有很多孩子参加聚会。我女儿除了给他们准备了一些饮料和零食以外，还买了一些玩具。他们喜欢吃什么就吃什么，喜欢玩儿什么就玩儿什么。"
       "今天我和我太太过得十分开心，我们很感谢大家对我们的祝福。")
ST2_E = ("Today our home was really lively. My son and daughter invited many friends to our home to celebrate the thirtieth anniversary of my wife’s and my marriage. My son and daughter had told everyone long ago not to bring anything, but friends still brought all kinds of gifts: flowers, fruit, and works of art, saying it was a small token. Lao Wan knew my wife likes table tennis and gave her a set of table tennis paddles. I like tea, so my daughter’s boyfriend gave me a Japanese tea set. They all meant well, so we had no choice but to accept. Today’s dishes were all prepared by a friend of mine. He is from Guangdong and cooks Cantonese food especially well. Having the chance to taste authentic Cantonese food in a small northern city made everyone very happy. Many children also came to the party. Besides preparing drinks and snacks for them, my daughter also bought some toys. They ate whatever they liked and played with whatever they liked. Today my wife and I were very happy, and we are very grateful for everyone’s blessings.")
TR = [("对不起，让你们久等了。我们很早就出门了，在来的路上还看了一套新公寓，我们很喜欢。", "1. (mine; 让, 早, 地) Sorry to have kept you waiting. We left home very early, and on the way here we looked at a new apartment; we like it very much."), ("这是我们带给你们的茶具，是我去上海出差时买的。一点小意思，希望你们喜欢。", "2. (mine; 小意思) We’ve brought you this tea set. I bought it on a business trip to Shanghai. It’s just a small token; we hope you like it."),
      ("我们喜欢的那套公寓比现在住的大多了，又漂亮又安静，离超市也很近。", "3. (mine; 大多了, 又…又…) The apartment we like is much bigger than where we live now; it’s pretty and quiet and very close to the supermarket."), ("你做的菜真好吃！好，我喜欢什么菜就吃什么菜。", "4. (mine; 真, 什么…什么…) The dishes you made are so delicious! OK, I’ll eat whichever dish I like."),
      ("这是你写的吗？我早就听说你的书法写得很好，今天终于有机会看到你的作品了。", "5. (mine; 早, 有机会) Did you write this? I heard long ago that your calligraphy is very good; today I finally have the chance to see your work."), ("对了，我们搬进新家以后就请你们来。我们请你们吃家常便饭，什么都不用带，人来就行了。", "6. (mine; 对了, 什么都) By the way, we’ll invite you over once we move into our new home. We’ll treat you to home cooking; please don’t bring anything, just yourselves.")]
SK1 = [("马静和她先生刚刚参加了一个聚会。", "1. Ma Jing and her husband have just attended a party."), ("老张也是王真的朋友。", "2. Lao Zhang is also Wang Zhen’s friend."), ("马静的先生早就听说王真做鱼做得很好。", "3. Ma Jing’s husband heard long ago that Wang Zhen cooks fish very well."), ("王真的新房子很漂亮，可是很贵。", "4. Wang Zhen’s new house is very beautiful but very expensive."), ("王真的孙子现在上小学，那个学校非常好。", "5. Wang Zhen’s grandson is now in elementary school, and that school is very good.")]
L5 = lesson(
    "Lesson 15 Presentation 2: skill integration",
    "结婚三十周年 · 一点儿小意思 · 书法",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, and Speaking)",
             "A. Listen to a WeChat message twice and write a summary in English. New words: 重要 (zhòngyào; important), 不好意思 (bù hǎoyìsi; feel sorry). B. Listen again and refine your summary. C. Read the statements and mark each True or False (the book gives no key and it depends on the audio, so none is given here). (Audio, not included.) The five statements:",
             examples=[D(z, e) for z, e in SK1]),
        card("Activity 2 (Reading and Speaking)",
             "A. Read the passage, consulting your dictionary as needed, then answer in English: What was the occasion? Did the guests listen to the host’s request? Why were the dishes served so special? How were the young children treated? (Mine: a thirtieth wedding anniversary; no, they still brought gifts; a friend from Guangdong cooked authentic Cantonese food in a northern city; they could eat and play whatever they liked.) B. Pair up and compare; take turns translating the underlined sentences into English and back into Chinese. C. Role play: you are the passage’s author and your partner is a guest. Welcome your guest; receive the present; discuss the food; include what kids can eat and do; thank your guest for attending.",
             examples=[D(ST2, ST2_E)]),
        card("Activity 3 (Speaking, Writing, and Reading)",
             "A. Pair up and take turns writing the Chinese equivalents of the English sentences, using the expressions provided in parentheses. 1. Sorry to have kept you waiting. We left home very early, and went to look at a new apartment on our way here. We like it very much. (让, 早, 地) 2. We have brought you this tea set. I bought it when I was on a business trip in Shanghai. It is just a small token of appreciation and we hope you like it. (小意思) 3. The apartment we like is much larger than our current one. It is both pretty and quiet, and very close to the supermarket. (大多了, 又…又…) 4. The dishes you’ve made are so delicious! Yes, I’ll help myself with whatever dish I like. (真, 什么…什么…) 5. Did you write this? I heard a long time ago that you are very good at calligraphy (书法), and finally I have an opportunity to see your work (作品). (早, 有机会) 6. By the way, we will invite you to our new home as soon as we have moved into it. We will treat you to some simple homemade food. Please don’t bring anything, just yourselves. (对了, 什么都) B. Together, go over the Chinese sentences you have written. My sentences (mine):",
             examples=[D(z, e) for z, e in TR]),
        card("Activity 3 C and D",
             "C. In pairs, create a dialog that will happen at a gathering. It will include: an exchange of polite remarks upon your arrival at your friend’s home; telling your friend what you like about their new home; commenting on the food and the calligraphy; inviting your friend and their family to your new apartment once you’ve moved in (主人 / 你, five exchanges). D. Perform your dialog for the class."),
    ],
    exercises=[
        M("What is the occasion in Activity 2’s passage?", "A thirtieth wedding anniversary", ["A birthday", "A new home", "A graduation"], "结婚三十周年。"),
        M("Did the guests follow the request to bring nothing?", "No, they still brought many gifts", ["Yes, no gifts", "They brought only food", "They brought nothing"], "朋友们还是带来了各种各样的礼物。"),
        M("What did Lao Wan give?", "A set of table tennis paddles", ["A tea set", "Flowers", "A painting"], "一套乒乓球拍。"),
        M("What did the daughter’s boyfriend give?", "A Japanese tea set", ["Table tennis paddles", "Fruit", "A book"], "一套日本茶具。"),
        M("Why were the dishes special?", "A Cantonese friend made authentic Cantonese food in a northern city", ["They were free", "They were imported", "They were cold"], "有机会在北方的一个小城市尝到地道的广东菜。"),
        M("How were the children treated?", "They could eat and play whatever they liked", ["They were sent home", "They could only eat rice", "They could only play outside"], "喜欢吃什么就吃什么。"),
        M("Why did the host accept the gifts?", "They were well-meant and he had no choice", ["He wanted to resell them", "He was greedy", "They were expensive"], "大家都是好意，我们只好收下。"),
        M("What does 地道 mean?", "Authentic", ["Underground", "Cheap", "Quick"], "地道: genuine."),
        M("What does 不好意思 mean?", "Feel sorry; embarrassed", ["Not interesting", "Not good", "Not mine"], "不好意思."),
        mean("艺术品", "yi4 shu4 pin3", "work of art", ["art teacher", "art school", "artist"]),
        F("他们喜欢吃什么就吃什么，喜欢玩儿什么就玩儿___么。", "什", PART, "什么…什么…"),
        F("今天我和我太太过得十分开___。", "心", PART, "开心: happy."),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese in context
WS = [("你", "王老师，您好！"), ("王", "大卫，你好！欢迎欢迎，快请进。"), ("你", "这是一盒咖啡，是前些日子我父母从美国带来的，送给您，一点小意思。"), ("王", "你太客气了。我跟你说过，来我家什么都不用带，人来就行了。大卫你看，谁来了？"), ("你", "啊，是杜老师！"), ("杜", "我很好。好久不见了，大卫。"),
      ("王", "大卫刚来我们学校的时候，只会说几句中文，现在说得这么好了。"), ("杜", "是啊。我也记得他游泳游得很好。那时琳达还是他的女朋友，听说现在他们已经有孩子了。"), ("你", "对。琳达刚刚生了孩子，不能来，她也很想念老师们。"), ("王", "菜已经好了，都是家常便饭。咱们去饭厅吃饭吧。"),
      ("你", "啊，做了这么多菜。早就听说师母做菜做得特别好，今天终于有机会尝尝了。"), ("王", "都是家常便饭。这里有啤酒和茶，还有饮料，你们想喝什么就喝什么。"), ("你", "谢谢！王老师，您做菜一定做得很好吧？"), ("王", "我呀，什么菜也不会做。再说，工作那么忙，也没有时间学。不过，有一件事我很喜欢做。"),
      ("你", "什么事？"), ("王", "就是到了周末，请我的学生们来我这儿，大家一起聊聊天，吃吃饭。大卫，以后你要经常来哦。")]
JY = ("上门家宴服务。朋友聚会，去饭店吗？最有名的饭店也不一定能做出您喜欢吃的菜。而且，饭店做菜往往放很多鸡精，对身体不好。另外，在饭店吃一顿大餐要花很多钱，不合算。怎么办？建议您跟我们联系，我们有最好的厨师，用最健康的食材，给您做一桌最好吃的大餐！我们去您家，您点什么菜我们就做什么菜，又快又好又便宜。此外，要是您想学，饭后我们还可以教您做一个名菜。请马上打美味热线：八零零，三三三，二一二一。")
JY_E = "Home banquet service. A friends’ gathering: go to a restaurant? Even the most famous restaurant may not be able to make the dishes you like. Moreover, restaurants often put in a lot of chicken essence, which is bad for health. Besides, a big meal at a restaurant costs a lot and isn’t worth it. What to do? We suggest you contact us: we have the best chefs, use the healthiest ingredients, and make you a table of the most delicious dishes! We come to your home and cook whatever dish you order; fast, good and cheap. In addition, if you want to learn, after the meal we can also teach you a famous dish. Call the delicious hot-line now: 800-333-2121 (read digit by digit)."
TJ = ("特色家宴。预订热线：八零零，三三一，九九九一。营业时间：早餐六点半到九点，午餐十点到十四点，晚餐十七点到二十一点半。设施服务：可以用信用卡，有停车位，无线上网，有自己的房间。餐厅地址：中山北路一千八百八十号二楼，交通很方便。餐厅环境：安静、舒服、漂亮。菜系特色：广东菜，上午有早茶。")
TJ_E = "Special banquet. Reservation hot-line: 800-331-9991. Business hours: breakfast 6:30 to 9:00, lunch 10:00 to 14:00, dinner 17:00 to 21:30. Facilities and services: credit cards accepted, parking, wireless internet, private rooms. Restaurant address: 2nd floor, 1880 Zhongshan North Road, very convenient transportation. Environment: quiet, comfortable, pretty. Cuisine: Cantonese food, with morning tea in the morning."
L6 = lesson(
    "Lesson 15 Presentation 2: using Chinese in context",
    "王老师退休了 · 上门家宴服务 · 特色家宴 · 美国的开放式聚会",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing, Listening, and Speaking): visiting Mr. Wang",
             "You just learned that Mr. Wang, your professor from years ago at Nanjing University, has retired. You and your old classmates all liked him and miss him very much. A. You received an old audio file containing an exchange you had with Mr. Wang and another teacher when you were his guest; a few sections are unintelligible. Read the script and provide the missing parts according to the context. B. Pair up and compare; then listen to the repaired audio and make corrections. The book leaves the blanks; my completed script (mine; the speakers are 你, 王 and 杜):",
             examples=[D(a + "：" + b, "(script line; the blanks are filled by me)") for a, b in WS]),
        card("Activity 2 (Reading, Writing, and Speaking): New Year’s Day",
             "You are a visiting professor at Guangzhou University and New Year’s Day is coming. A. It’s one week before; you are planning a celebration. In groups of three compare the two services below, decide which is best and fill in the table (上门家宴服务 versus 特色家宴: 好的地方, 不好的地方, 选哪个 & 为什么). The book prints phone numbers and times as digits; they are spelled out here.",
             examples=[D(JY, JY_E), D(TJ, TJ_E)]),
        card("Activity 2 B and C, and Activity 3",
             "B. It is New Year’s Day and the guests have arrived. Each member of the group (the organizer, the cook and one of the guests) makes a speech in Chinese using the talking points. Organizer: welcome everybody to the event; what the event is about, who the attendants are; how the event will proceed (enjoy whatever drinks and food they like; exchange gifts after the meal, etc.); any questions? Cook: thank them for the opportunity to serve; describe the food, drinks and dessert; any questions? Guest: thank the organizer and the cook; comment on the environment, the food and the drinks; invite people to your new home to celebrate the Chinese New Year in a few weeks. C. It is now January 2. Write an email to a Chinese friend describing how the event went; include the EEIs in six to eight sentences. Activity 3 (Listening, Reading, Speaking, and Writing). You are training the managers of a Chinese company in Shanghai on American culture; one category is socializing. A. Today’s topic is house parties (开放式聚会) in America. Mr. Zhu, a guest speaker, first shares his experience while living in America. Listen to his description and write a summary. New words: 开放 (kāifàng; open), 邀请 (yāoqǐng; invite), 安排 (ānpái; arrange), 邻居 (línjū; neighbor), 主人 (zhǔrén; host), 变成 (biànchéng; become). B. You organized a house party at your apartment the following day. Pictures taken during the party are shown (not included); tell your Chinese colleague (your partner) what happened; then switch. C. Write an email to a Chinese friend describing the party you held and share it with your partner. (Audio and pictures, not included.)"),
    ],
    exercises=[
        M("Whom is David visiting?", "His old professor Mr. Wang", ["His boss", "His father", "A classmate"], "王老师."),
        M("What gift does David bring?", "A box of coffee from his parents", ["Tea", "Fruit", "Flowers"], "一盒咖啡."),
        M("Who else is at Mr. Wang’s home?", "Teacher Du", ["Linda", "David’s mother", "Teacher Gao"], "是杜老师！"),
        M("Why couldn’t Linda come?", "She had just had a baby (my completion)", ["She was working", "She was angry", "She was abroad"], "琳达刚刚生了孩子。"),
        M("What does Mr. Wang like to do?", "Invite students over on weekends to chat and eat", ["Cook fancy food", "Travel", "Teach cooking"], "请我的学生们来我这儿。"),
        M("What does the home banquet service offer?", "Chefs who cook at your home whatever you order", ["A fixed menu at a restaurant", "A bus tour", "Cooking classes only"], "您点什么菜我们就做什么菜。"),
        M("What does the home banquet service say against restaurants?", "They often use much chicken essence and cost a lot", ["They are too small", "They are too far", "They are closed"], "放很多鸡精，对身体不好；花很多钱，不合算。"),
        M("What cuisine does the 特色家宴 restaurant serve?", "Cantonese food, with morning tea", ["Sichuan food", "Japanese food", "Fast food"], "广东菜，上午有早茶。"),
        M("What are two facilities of the 特色家宴 restaurant?", "Credit cards and parking", ["A pool and a gym", "A zoo and a pool", "A theater"], "可以用信用卡，有停车位。"),
        M("What is Activity 3’s topic?", "House parties in America", ["Weddings", "Business meetings", "Funerals"], "开放式聚会."),
        mean("厨师", "chu2 shi1", "chef", ["waiter", "guest", "host"]),
        F("我们有最好的厨___。", "师", PART, "厨师: chef."),
    ],
)
L7 = vocab_lesson("Lesson 15 Presentation 2 vocabulary", "22 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十五课 社交聚会 Presentation 2: visiting the new home, 想…什么就…什么, 让, potentiality (2), banquets", [L1, L2, L3, L4, L5, L6, L7])
