"""Unit 46: Lesson 16 (Recreational Activities) Presentation 2 from the book's texts: the band dialog, 就 for ease, 越来越 and
越…越…, reduplication of measure words, 对…感兴趣, the skill-integration and using-Chinese activities (the KTV diary, two concert
passages, the concert schedule, 五月天 and three singers) and the vocabulary list. Audio, pictures, videos and websites are not
included; the book writes numbers as digits and they are spelled out here (the book prints passage 1 in traditional characters and
mixes a few traditional characters into the diary; both are given in simplified characters here); answer keys the book does not
print (and blanks it leaves for the student) are mine and labeled."""
from zh_auto import *
from zh_l16_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("得去", 0, "dei3"), ("得另外", 0, "dei3"), ("得好好", 0, "dei3"), ("得买", 0, "dei3"), ("华晨宇", 0, "hua4"), ("没去", 0, "mei2"), ("没听见", 0, "mei2"), ("没有去", 0, "mei2"), ("一块唱", 2, "chang4"), ("听起来", 0, "ting1"),
                          ("售票处", 2, "chu4"), ("还没有去过", 0, "hai2"), ("人参加", 1, "can1"), ("都会", 0, "dou1")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0 and zh[j - 1] not in "当草土天各山场内本外基实陆" and (j + 1 >= len(zh) or zh[j + 1] not in "道址方铁图球区点上下面理"):
            f[j] = "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]
NOUN = ["作业", "操场", "预习"]

# ------------------------------------------------------------------ 1. the dialog
P2 = [("马克", "平常空闲的时候你喜欢做什么？", "What do you like to do in your free time?"), ("琳达", "我以前特别喜欢去歌厅唱歌或是去舞厅跳舞。不过最近学习很紧张，已经好久没去了。", "I used to especially like going to a karaoke hall to sing or to a dance hall to dance. But recently my studies have been intense, and I haven’t gone for a long time."),
      ("马克", "学校就有一个合唱团，人人都可以参加。你要是感兴趣，可以去试试。", "The school has a choir that everyone can join. If you’re interested, you can try it."), ("琳达", "好，下课以后，我就去打听一下儿，看怎么报名。你呢，你参加合唱团了吗？", "OK, after class I’ll go ask and see how to sign up. And you, have you joined the choir?"),
      ("马克", "没有，我对合唱不太感兴趣。不过我参加了一个乐队。", "No, I’m not very interested in choral singing. But I joined a band."), ("琳达", "什么乐队？", "What band?"),
      ("马克", "摇滚乐队，我们乐队一共有三个人，张华弹吉他，我打鼓，小李是键盘手。", "A rock band. Our band has three people altogether: Zhang Hua plays guitar, I play drums, and Xiao Li is the keyboard player."), ("琳达", "听起来挺酷的。", "Sounds pretty cool."),
      ("马克", "那当然，我们的乐队还上过电视呢！粉丝也越来越多了。", "Of course! Our band has even been on TV! And the fans are getting more and more."), ("琳达", "以后你们演出的时候别忘了告诉我，我也要去听听。", "Don’t forget to tell me when you perform; I want to go listen too."),
      ("马克", "真巧，这个周末在中心公园有一个音乐节，我们乐队也会去表演。", "What a coincidence; this weekend there’s a music festival in Central Park and our band will perform there too."), ("琳达", "太好了，那我一定去。", "Great, then I’ll definitely go.")]
A2P = ("最近琳达学习很忙，没有时间去歌厅唱歌或是去舞厅跳舞。所以马克告诉她学校就有合唱团。要是她感兴趣，她可以去打听一下看怎么报名。马克不喜欢合唱，但是他也对音乐感兴趣，所以他参加了一个摇滚乐队。他的乐队有三个人，每个人玩不一样的乐器。马克打鼓，他的朋友弹吉他和键盘。除了自己玩音乐以外，他的乐队也会在别的地方表演。下个星期他们会在一个音乐节演出。琳达打算去看看。说不定她会成为他们的粉丝。")
A2P_E = ("Recently Linda has been busy studying and has had no time to go to a karaoke hall to sing or a dance hall to dance. So Mark told her the school has a choir. If she is interested, she can ask and see how to sign up. Mark doesn’t like choral singing, but he is also interested in music, so he joined a rock band. His band has three people, and each plays a different instrument. Mark plays drums, and his friends play guitar and keyboard. Besides playing music by themselves, his band also performs elsewhere. Next week they will perform at a music festival. Linda plans to go and see. She may well become their fan. (completed text; the blanks are filled by me: 跳舞, 合唱团, 报名, 音乐, 乐队, 鼓, 吉他, 表演, 粉丝)")
L1 = lesson(
    "Lesson 16 Presentation 2: the rock band",
    "平常空闲的时候你喜欢做什么？ · 合唱团 · 摇滚乐队 · 音乐节",
    requires=[],
    cards=[
        card("Getting Started",
             "Photographs: people dancing, singing and playing instruments (not included). Pair up and discuss: A. Look at the pictures. Which activity (if any) do you enjoy? Why? B. Can you name any musical instrument in Chinese? Do you play one? When and how did you learn it?"),
        card("Presentation 2: 摇滚乐队",
             "The book also prints the dialog in traditional characters. Note: 听起来, a colloquial expression, in English similar to “sounds like”.",
             examples=dlg(P2)),
        card("Activity 1 (Listening and Speaking)",
             "A. Global listening: 1. What is the presentation about? 2. What is likely to happen next? B. Detailed listening: listen again and write personal profiles for Mark and Linda. C. Pair up; in Chinese, Student A reports Mark’s profile and Student B reports Linda’s to the class. (Audio, not included. From the dialog, mine: free-time activities; Linda will probably sign up for the choir and go to the music festival. Mark: in a rock band of three, drums, band has been on TV, not interested in choral singing, playing at the music festival. Linda: used to sing at karaoke halls and dance at dance halls, studies are intense lately, wants to join the choir.)"),
        card("Activity 2 (Reading, Speaking and Listening)",
             "A. Read the passage below and complete the sentences using the linguistic and contextual clues, without consulting Presentation 2 first. Word box: 合唱团, 音乐, 报名, 表演, 乐队, 鼓, 吉他, 粉丝, 跳舞. The book leaves nine blanks; my completed passage (mine):",
             examples=[D(A2P, A2P_E)]),
        card("Activities 2 B and C, 3 and 4",
             "B. Pair up and take turns reading each sentence aloud; discuss the strategies you used to find the correct answers. C. Listen to four sentences; in the table, transcribe what you heard and translate your transcription. (Audio, not included.) Activity 3 Class Survey (Listening and Speaking). A. Find a classmate who fits the description in the table (who joined a choir; who likes rock and roll; who was in a band; who plays an instrument; who likes to dance; who likes to sing; who has attended a concert) and ask additional questions. B. The class shares their findings in Chinese. Activity 4 (Listening and Speaking). A. Listen to a phone conversation between two friends and write the EEIs of the event (event, attendees, where, when). B. Pair up and, in Chinese, share your answers. C. Interview your partner about a musical event they attended: What music event have you attended? When and where was it held? With whom did you go? What was the arrangement of the band? What type of music was played? Did you enjoy the event? D. In Chinese, report to another classmate what you learned. (Audio, not included.)"),
    ],
    exercises=[
        M("What did Linda use to like?", "Singing at karaoke halls and dancing at dance halls", ["Playing the guitar", "Playing soccer", "Reading"], "歌厅唱歌，舞厅跳舞."),
        M("Why hasn’t Linda gone lately?", "Her studies are intense", ["She moved away", "She lost interest", "She is sick"], "最近学习很紧张."),
        M("What does Mark suggest?", "Join the school choir", ["Join the band", "Quit studying", "Sing at home"], "学校就有一个合唱团."),
        M("Is Mark in the choir?", "No, he is in a rock band", ["Yes", "No, he is in an orchestra", "No, he plays alone"], "我对合唱不太感兴趣。不过我参加了一个乐队。"),
        M("How many people are in Mark’s band?", "Three", ["Two", "Four", "Five"], "一共有三个人."),
        M("Who plays what?", "Zhang Hua guitar, Mark drums, Xiao Li keyboard", ["Mark guitar", "Xiao Li drums", "Zhang Hua keyboard"], "张华弹吉他，我打鼓，小李是键盘手."),
        M("Where will the band perform this weekend?", "At a music festival in Central Park", ["At a school", "At a concert hall", "On TV"], "这个周末在中心公园有一个音乐节."),
        M("What does 听起来挺酷的 mean?", "Sounds pretty cool", ["Sounds loud", "Sounds old", "Sounds boring"], "听起来 = sounds like."),
        M("What does 粉丝 mean?", "Fans", ["Noodles only", "Friends", "Teachers"], "粉丝: fans."),
        M("What does 真巧 mean?", "What a coincidence!", ["How cheap!", "How skillful!", "Of course!"], "真巧."),
        M("What does 打鼓 mean?", "Play the drum", ["Beat a person", "Break a drum", "Sell a drum"], "打鼓: play a drum."),
        mean("吉他", "ji2 ta1", "guitar", ["piano", "drum", "violin"]),
        F("我对合唱不太感___趣。", "兴", PART, "感兴趣."),
        F("下课以后，我就去打听一下儿，看怎么___名。", "报", PART, "报名: sign up."),
    ],
)

# ------------------------------------------------------------------ 2. 就 for ease
EA = [("学校就有一个合唱团，人人都可以参加。", "The school has a choir that everyone can join. (right there)"), ("住在这里很方便，超级市场就有三家。", "Living here is convenient; there are three supermarkets right here."), ("蒙特雷的蔬菜很便宜，五块钱就可以买到好几把。", "Vegetables in Monterey are cheap; five dollars buys several bunches."),
      ("去银行转账太麻烦，上网五分钟就可以做完。", "Going to the bank to transfer money is too troublesome; online it takes only five minutes."), ("买机票不用找旅行社，我女朋友就可以帮你。", "No need to find a travel agency to buy a plane ticket; my girlfriend can help you.")]
EB = [("我很喜欢举重，可是在蒙特雷很难找到健身房。", "Student A: I like weightlifting, but it’s hard to find a gym in Monterey."), ("你刚来，还不太熟悉蒙特雷，蒙特雷有很多健身房，你公寓的附近就有三家。", "Student B: You just arrived and aren’t familiar with Monterey yet; there are many gyms, and near your apartment there are three.")]
EC = [("你家附近就有两家比萨店，十分钟就可以走到。", "1. There are two pizza places right near your home; you can walk there in ten minutes. (mine)"), ("你不用去市中心，学校旁边就有一家很好的中国饭馆。", "2. You don’t need to go downtown; there is a very good Chinese restaurant right next to the school. (mine)"), ("你不用开车，学校的商店就有衬衫。", "3. You don’t need to drive; the school store has shirts. (mine)"),
      ("你公寓门口就有公共汽车站。", "4. There is a bus stop right at your apartment’s door. (mine)"), ("上网五分钟就可以找到很多公寓。", "5. Online you can find many apartments in five minutes. (mine)")]
L2 = lesson(
    "Lesson 16 Presentation 2 grammar: 就 to express “ease”",
    "学校就有一个合唱团 · 超级市场就有三家 · 五分钟就可以做完",
    requires=[],
    cards=[
        card("就 to express “ease”",
             "In the previous lessons and units you have learned various uses of 就, indicating “then,” “as soon as,” “just/only,” and “indeed/exactly.” In this lesson, 就 is used to express the “ease” of doing something. Subject + 就 + Verb.",
             examples=[D(z, e) for z, e in EA]),
        card("Activity 1 (Reading and Speaking)",
             "One of your friends has just moved to Monterey and, because of their unfamiliarity with the city, voiced complaints about accomplishing tasks. You want to persuade them of the convenience and ease with which the activities can be done, using the 就 pattern. Pair up: Student A makes complaints based on the situations; Student B uses the 就 pattern to persuade. The five situations: 1. 我很想吃 pizza，可是 Costco 太远。 2. 我想吃中国饭，可是不想走到蒙特雷市中心。 3. 我得买衬衫，可是我没有车。 4. 我想坐公共汽车去 Del Monte 电影院，可是我不知道哪儿有公共汽车站？ 5. 我听说蒙特雷的公寓不好找。 The book’s example and my answers (mine):",
             examples=[D(z, e) for z, e in EB + EC]),
    ],
    exercises=[
        M("What does 就 express in 学校就有一个合唱团?", "Ease: it is right there", ["Then", "Only once", "Exactly because"], "就 to express ease."),
        M("What does 超级市场就有三家 mean?", "There are three supermarkets right here", ["There are only three supermarkets in the world", "Three supermarkets closed", "Supermarkets are far"], "就有."),
        M("What does 五块钱就可以买到好几把 mean?", "Five dollars is enough to buy several bunches", ["Five dollars is too little", "Five bunches cost five dollars", "Nobody sells it"], "就可以."),
        M("What does 上网五分钟就可以做完 mean?", "Online it takes only five minutes", ["It takes five hours", "Online is impossible", "It takes at least five minutes"], "五分钟就可以做完."),
        M("Why does 我女朋友就可以帮你 use 就?", "It’s easy: no travel agency needed", ["It is forced", "It is late", "It is a question"], "Ease."),
        M("Which pattern is Subject + 就 + Verb used to show?", "How easy something is", ["A future wish", "A past experience", "A prohibition"], "Ease."),
        F("买机票不用找旅行社，我女朋友___可以帮你。", "就", PART, "Subject + 就 + Verb."),
        F("住在这里很方便，超级市场就有三___。", "家", PART, "三家."),
    ],
)

# ------------------------------------------------------------------ 3. 越来越
YL = [("大卫的中文越来越好了。", "David’s Chinese is getting better and better."), ("这里的天气越来越冷了。", "The weather here is getting colder and colder."), ("我越来越喜欢学习中文了。", "I like studying Chinese more and more.")]
YL2 = [("他越吃越多。", "The more he eats, the more he eats. (越+V+越+Adj.)"), ("他的中文越学越好。", "The more he studies, the better his Chinese gets."), ("大家都说朋友越多越好。", "Everyone says the more friends the better. (越+Adj.+越+Adj.)"), ("蒙特雷的房子越大越贵。", "In Monterey, the bigger the house the more expensive."), ("他越讲，他的太太越高兴。", "The more he talks, the happier his wife is. (Subj. 1 越 V, Subj. 2 越 Adj.)"), ("他越说，我们越害怕。", "The more he speaks, the more afraid we are.")]
YL3 = [("我的汉字越学越好。", "Student A: The more I learn characters, the better I am. (the book’s example)"), ("我们要记的生词越来越多。", "Student B: There are more and more new words we need to memorize. (the book’s example)"), ("蒙特雷的气候越来越差。", "Monterey’s climate is getting worse and worse. (mine)"), ("我的家乡越来越漂亮。", "My hometown is getting more and more beautiful. (mine)"), ("考试越来越麻烦。", "Exams are getting more and more troublesome. (mine)"), ("我的作业越来越多。", "My homework is getting more and more. (mine)")]
L3 = lesson(
    "Lesson 16 Presentation 2 grammar: the 越来越 construction",
    "越来越好 · 越吃越多 · 越多越好 · 越讲越高兴",
    requires=[],
    cards=[
        card("The 越来越 construction",
             "The 越来越 construction indicates comparison and may be used to show how a person or thing changes in a certain respect as time goes on. When the 越来越 construction is used, no other adverbs of degree, such as 很, 非常, 太, can be placed after it to modify the predicate. For example, it is incorrect to say “*天气越来越很冷了。” Subject + 越来越 + Adj./Mental Verb.",
             examples=[D(z, e) for z, e in YL]),
        card("越…越… (越 A 越 B)",
             "越来越 has a variation 越 A 越 B, which indicates that B changes according to the change of A. Subj. + 越 + V + 越 + Adj./Mental Verb (examples 1 and 2). Subj. + 越 Adj. 越 + Adj. (examples 3 and 4). Subj. 1 + 越 + V, Subj. 2 + 越 + Adj./mental Verb (examples 5 and 6).",
             examples=[D(z, e) for z, e in YL2]),
        card("Activities 2 and 3",
             "Activity 2 (Reading, Speaking, Listening) Your Opinion Counts! A. Pair up. Student A uses Column A (汉字, 蒙特雷的气候, 我的家乡, 我的朋友, 我的家人, 我的身体, 考试, 我的听力课/语法课/说话课, 我的作业) and Student B uses Column B (多, 差, 好, 漂亮, 麻烦, 有意思, 闷热, 长, 可爱) to create a sentence using 越来越/越…越…; the partner translates orally. The book’s examples and my sentences (mine):",
             examples=[D(z, e) for z, e in YL3]),
        card("Activity 2 B and Activity 3",
             "B. Using the following questions, interview your partner to learn their opinions: 1. 你觉得什么越多越好？什么越少越好？ 2. 你觉得什么越快越好？什么越慢越好？ 3. 你觉得什么越来越贵？什么越来越便宜？ 4. 你觉得什么越来越方便？什么越来越麻烦？ 5. 你觉得什么越玩越有意思？ 6. 你觉得什么越吃越好吃？ 7. 你觉得越做什么越想睡觉？ C. The class shares the findings they found interesting. Activity 3 (Listening, Speaking and Writing). A. Listen to a conversation between two friends and write four differences you heard about life in Beijing before and now. B. Pair up and, in Chinese, compare your answers by repeating the sentence using the 越来越/越…越 structure. C. Write a brief report using 越来越/越…越 about how your life has changed after coming to DLI to study Chinese; post it on Linoit and share with your classmates. (Audio, not included.)"),
    ],
    exercises=[
        M("What does 越来越 show?", "A change that grows as time goes on", ["A single change", "A comparison of two people", "A negation"], "越来越: more and more."),
        M("Which is wrong?", "天气越来越很冷了", ["天气越来越冷了", "我越来越喜欢学习中文了", "大卫的中文越来越好了"], "No degree adverb after 越来越."),
        M("What does 他的中文越学越好 mean?", "The more he studies, the better his Chinese", ["He studies less", "He forgot Chinese", "His Chinese is bad"], "越 V 越 Adj."),
        M("What does 朋友越多越好 mean?", "The more friends the better", ["Few friends is better", "Friends are many", "Friends are bad"], "越 Adj. 越 Adj."),
        M("What does 蒙特雷的房子越大越贵 mean?", "In Monterey, the bigger the house, the more expensive", ["Houses are cheap", "Houses are small", "Monterey has no houses"], "越大越贵."),
        M("What does 他越说，我们越害怕 mean?", "The more he speaks, the more afraid we are", ["He is afraid", "We are not afraid", "We stopped him"], "Subj. 1 越 V, Subj. 2 越 Adj."),
        M("What does 这里的天气越来越冷了 mean?", "The weather here is getting colder and colder", ["The weather is very warm", "It was cold yesterday", "It won’t get cold"], "越来越冷."),
        F("我___来越喜欢学习中文了。", "越", PART, "越来越."),
        F("他的中文越学越___。", "好", PART, "越学越好."),
    ],
)

# ------------------------------------------------------------------ 4. reduplication of measure words
RD = [("学校就有一个合唱团，人人都可以参加。", "The school has a choir that everyone can join."), ("他天天都上网玩游戏。", "He plays games online every day."), ("他们个个都喜欢学汉字。", "They each and every one like learning characters."), ("这个风景点他去了很多次，次次都觉得有意思。", "He has been to this scenic spot many times and finds it interesting every time. (adverbial)"), ("春节到了，家家的门上都挂着红色的春字。", "Spring Festival has arrived; every home has the red character “spring” hung on its door. (attribute of the subject)")]
RD4 = [("这些照片张张都很漂亮。", "1. Every one of these photos is beautiful. (mine)"), ("她天天都去公园跳广场舞。", "2. She goes to the park to do square dancing every day. (mine)"), ("现在人人都会用手机上网。", "3. Nowadays everybody can use a phone to get online. (mine)"), ("百货公司的衣服，件件价格都很贵。", "4. The clothes at the department store: every piece is expensive. (mine)"), ("东西样样都很便宜。", "5. Everything at the warehouse store is cheap. (mine; the book writes the store name in Latin letters)"), ("他的家人个个都是军人。", "6. His family members are all in the military. (mine)"), ("我们班天天都有生词考试。", "(the book’s example) In our class there is a new-word quiz every day.")]
L4 = lesson(
    "Lesson 16 Presentation 2 grammar: reduplication of measure words (量词重叠)",
    "人人都 · 天天都 · 个个都 · 次次都 · 家家的门上都",
    requires=[],
    cards=[
        card("Reduplication of measure words (量词重叠)",
             "The reduplication of measure words indicates the meaning of “everyone or everything without exception.” It is usually followed by 都. This pattern can only be used as subjects or attributes of subjects; it cannot be used as the objects or attributes of objects. For example, one cannot say: “*我告诉人人。” “*我喜欢张张照片。” Subj. + AA + 都; AA + Subj. + 都; AA 的 + noun phrase + 都 (used as attribute of the subject).",
             examples=[D(z, e) for z, e in RD]),
        card("Activity 4 (Reading, Speaking and Writing)",
             "A. Use the characters in the box (个个, 天天, 样样, 人人, 张张, 件件) to complete the sentences with reduplication of measure words: 1. 这些照片___都很漂亮。 2. 她___都去公园跳广场舞。 3. 现在___都会用手机上网。 4. 百货公司的衣服，___价格都很贵。 5. Costco 的东西___都很便宜。 6. 他的家人___都是军人。 B. With your partner, read your answers aloud and provide a rationale. C. As a class, use the topic “our class” to find something you and your classmates have in common and create a list of sentences using reduplication of measure words (the book’s example: 我们班天天都有生词考试). The book leaves the key out; my answers: 1 张张, 2 天天, 3 人人, 4 件件, 5 样样, 6 个个 (mine):",
             examples=[D(z, e) for z, e in RD4]),
    ],
    exercises=[
        M("What does a reduplicated measure word mean?", "Everyone or everything without exception", ["A few", "Once", "Never"], "AA + 都."),
        M("What does 人人都可以参加 mean?", "Everybody can join", ["Nobody can join", "Only one person can join", "People can’t join"], "人人."),
        M("What does 天天都上网 mean?", "Goes online every day", ["Goes online once", "Never goes online", "Goes online tomorrow"], "天天."),
        M("What does 个个都喜欢学汉字 mean?", "Each and every one likes learning characters", ["One likes it", "None likes it", "Most dislike it"], "个个."),
        M("What does 次次都觉得有意思 mean?", "Finds it interesting every time", ["Found it once", "Never interesting", "Only the first time"], "次次."),
        M("Which sentence is wrong?", "我告诉人人", ["人人都来了", "天天都有考试", "家家的门上都挂着春字"], "Not as object."),
        M("Which fills 这些照片___都很漂亮？", "张张", ["件件", "人人", "个个"], "张 is the measure word for photos."),
        M("Which fills 百货公司的衣服，___价格都很贵？", "件件", ["张张", "天天", "人人"], "件 for clothes."),
        F("他的家人个个都___军人。", "是", PART, "个个都是."),
        F("她天天___去公园跳广场舞。", "都", PART, "天天都."),
    ],
)

# ------------------------------------------------------------------ 5. 对…感兴趣
GX = [("我对合唱不太感兴趣。", "I am not very interested in choral singing."), ("我对这个人感兴趣。", "I am interested in this person."), ("他对参加乐队感兴趣。", "He is interested in joining a band."), ("他对学习外语很感兴趣。", "He is very interested in learning foreign languages."), ("老师对她以后的打算很感兴趣。", "The teacher is very interested in her future plans.")]
GX5 = [("你对旅游感兴趣吗？", "Student A: Are you interested in travel? (the book’s example)"), ("对，我对旅游感兴趣。", "Student B: Yes, I’m interested in travel."), ("不，我对旅游不感兴趣。", "No, I’m not interested in travel."), ("你对坐飞机旅游感兴趣还是坐火车旅游感兴趣？", "Are you interested in traveling by plane or by train? (additional question)"), ("我对坐火车旅游感兴趣。", "I’m interested in traveling by train."), ("为什么？", "Why? (additional question)")]
GZ = ("我高中的时候开始对弹吉他很感兴趣。那个时候我去听了一场吉他音乐会。里面的吉他手弹得很棒！后来我的妈妈送了我一把吉他当生日礼物，所以我就开始自学吉他。")
GZ_E = "When I was in high school I began to be very interested in playing the guitar. At that time I went to a guitar concert. The guitarist there played wonderfully! Later my mother gave me a guitar as a birthday present, so I started to teach myself guitar. (the book’s example card)"
L5 = lesson(
    "Lesson 16 Presentation 2 grammar: 对…感兴趣",
    "我对合唱不太感兴趣 · 他对学习外语很感兴趣 · 旅游、音乐、乐器",
    requires=[],
    cards=[
        card("对…感兴趣",
             "In English, we use statements to say that we are “interested in something.” In this construction, “something” terminates the sentence. However, in Chinese, you “对 something 感兴趣.” Statement: Subj. + 对 + something/person/verb phrase + 感兴趣。 Negation: Subj. + 对 + something/person/verb phrase + 不 + 感兴趣。",
             examples=[D(z, e) for z, e in GX]),
        card("Activity 5 (Reading, Speaking, and Listening)",
             "A. Below are topics people may be interested in (旅游, 参加聚会, 参观 XXX, 音乐, 学乐器, 看电影, 锻炼/健身). Interview your classmates; in addition to the topic question, ask at least one follow-up question to get more information and write the responses in the table (Who, Additional info). If the answer is no, move on to the next student. B. Guessing game: each student writes 3–4 sentences on a blank card describing what they are interested in and why, using 对…感兴趣; the teacher gathers the cards and puts them in a box; each student draws a card and reads it aloud, and the class guesses who wrote it (if a student draws their own card they draw another). The book’s example dialog and example card:",
             examples=[D(z, e) for z, e in GX5] + [D(GZ, GZ_E)]),
    ],
    exercises=[
        M("How do you say “interested in X”?", "对 X 感兴趣", ["感兴趣 X 对", "X 对感兴趣", "感 X 兴趣"], "对 + something + 感兴趣."),
        M("How do you negate it?", "对…不感兴趣", ["不对…感兴趣", "没对…感兴趣", "对…感不兴趣"], "不 before 感兴趣."),
        M("What does 我对合唱不太感兴趣 mean?", "I’m not very interested in choral singing", ["I love choral singing", "I can’t sing", "I don’t know the choir"], "不太感兴趣."),
        M("What does 他对学习外语很感兴趣 mean?", "He is very interested in learning foreign languages", ["He can’t learn languages", "He teaches languages", "He dislikes languages"], "很感兴趣."),
        M("What does 老师对她以后的打算很感兴趣 mean?", "The teacher is very interested in her future plans", ["The teacher has no plans", "She is interested in the teacher", "She has no plans"], "对…感兴趣."),
        M("How did the example writer start learning guitar?", "Her mother gave her a guitar as a birthday gift", ["She bought one", "A teacher gave one", "She found one"], "妈妈送了我一把吉他当生日礼物."),
        F("他对参加乐队___兴趣。", "感", PART, "感兴趣."),
        F("你___旅游感兴趣吗？", "对", PART, "对…感兴趣."),
    ],
)

# ------------------------------------------------------------------ 6. skill integration
DI = ("我是一个大学二年级的学生，我平常的休闲娱乐不太多。我最大的爱好是跟朋友去ＫＴＶ唱歌。我的爸妈都告诉我ＫＴＶ不好，我应该好好努力学习，如果我真要做什么休闲活动，就应该去参观博物馆，看看展览什么的，可是他们不知道，在那儿唱歌我可以完全放松，不但可以唱很多新歌和老歌，而且中文歌唱完了，还可以唱英文歌。有时我自己一个人唱，有时和朋友一块唱。有时我们甚至会一边唱，一边跳。开心极了！我们常一去就是好几个小时。唱累了，那儿的服务员还会给我们送上各种吃的。你想这么好的服务去哪儿找。不过在ＫＴＶ唱歌一个小时要三百多块钱，吃东西还得另外付钱，所以我的钱越来越少了。我得好好努力学习，这样爸妈才会给我更多零用钱。")
DI_E = ("I am a second-year university student, and my usual recreation is not much. My biggest hobby is going to KTV (karaoke) with friends to sing. My parents both tell me KTV is bad, that I should study hard, and that if I really want to do some leisure activity I should visit museums and look at exhibitions and so on, but they don’t know that singing there lets me relax completely: I can sing many new and old songs, and when I finish the Chinese songs I can also sing English songs. Sometimes I sing by myself, and sometimes with friends. Sometimes we even sing and dance at the same time. Great fun! We often go and stay several hours. When we’re tired from singing, the waiters there bring us all kinds of food. Where else would you find such good service? However, singing at KTV costs over three hundred yuan an hour, and eating costs extra, so my money keeps getting less. I have to study hard so that my parents will give me more pocket money. (The book writes KTV in Latin letters; full-width letters here.)")
PA1 = ("两年以前，我在中国的南京市工作。我的工作不太忙，有空的时候，我常常去听音乐会。我喜欢流行音乐，也喜欢交响乐。要是有有名的西方交响乐团来南京演出，我一定会去看。有一次，我在报上看到新闻，美国的旧金山交响乐团要来中国演出。我很高兴，马上发电子邮件告诉我的朋友。可是他告诉我，旧金山交响乐团只在上海演出一场。时间是下个月的五号。我想，南京离上海不远，开车只要两个多小时。我还没有去过上海，我很想去上海看看。所以，我告诉我的朋友，我一定得去看这场音乐会。一个月后，我去上海看了音乐会。那场音乐会下午开始，中国的观众很多，也很热情。我想那是我看过的最好的演出之一。看完演出，我还在上海逛了大商场，也参观了几个有名的风景点。我觉得这次的上海二日游很有意思。下次我还要再来！")
PA1_E = ("Two years ago I worked in Nanjing, China. My work wasn’t very busy, and when I had free time I often went to concerts. I like pop music and also symphonic music. If a famous Western symphony orchestra came to Nanjing to perform, I would definitely go. Once I saw in the paper that the San Francisco Symphony Orchestra was coming to China to perform. I was very happy and immediately emailed my friend. But he told me the San Francisco Symphony would perform only one show, in Shanghai, on the fifth of next month. I thought, Nanjing is not far from Shanghai; by car it takes only a bit over two hours. I hadn’t been to Shanghai and wanted to see it. So I told my friend I had to go to this concert. A month later I went to Shanghai and saw the concert. It began in the afternoon; the Chinese audience was large and enthusiastic. I think it was one of the best performances I’ve seen. After the show I also strolled the big shopping malls in Shanghai and visited a few famous scenic spots. I found this two-day Shanghai trip very interesting. I’ll come again next time! (Passage 1, printed in traditional characters in the book.)")
PA2 = ("我在上海出差的时候，听过一次音乐会。记得那是一个星期六的下午，我问旅馆服务员上海什么地方有音乐会。服务员马上就给上海音乐厅打了一个电话，然后告诉我上海音乐厅晚上七点半有一场音乐会，是中国流行音乐。下午六点半，我坐地铁到上海音乐厅，在售票处买到票以后，我拿着票高高兴兴地走进音乐厅。我一走进音乐厅的大门，一位服务员就热情地走过来问我的座位在哪儿，需不需要帮助。我告诉他我自己可以找到座位。那天听音乐会的人很多。演出结束以后，大家都站起来鼓掌。离开音乐厅的时候，我在音乐厅的门口买了一张中国流行音乐的光盘。我很喜欢那张光盘上的音乐。到现在，有时间的时候，我还经常听那张光盘。")
PA2_E = ("When I was on a business trip in Shanghai I once attended a concert. I remember it was a Saturday afternoon; I asked the hotel attendant where in Shanghai there was a concert. The attendant immediately phoned the Shanghai Concert Hall and told me there was a concert at the hall at seven thirty in the evening, Chinese pop music. At six thirty in the afternoon I took the subway to the hall, and after buying a ticket at the ticket office I walked happily into the hall holding the ticket. As soon as I walked through the gate, an attendant warmly came over and asked where my seat was and whether I needed help. I told him I could find the seat myself. There were a lot of people at the concert that day. After the performance everyone stood up and applauded. When I left the hall I bought a CD of Chinese pop music at the entrance. I liked the music on that CD very much. Even now, when I have time, I still often listen to it.")
L6 = lesson(
    "Lesson 16 Presentation 2: skill integration",
    "ＫＴＶ唱歌 · 两个音乐会 · 旧金山交响乐团 · 上海音乐厅",
    requires=[],
    cards=[
        card("Activities 1 and 3 (listening)",
             "Activity 1 (Listening and Speaking). A. Listen to the dialogs twice and answer the questions. Dialog 1: 1. What is the upcoming event? When and where will it be held? 2. What will the male speaker do for the female speaker? 3. What is the female speaker instructed to do? Dialog 2: 1. What is the topic of the conversation? 2. What questions are asked by the first speaker? (list three) 3. What advice is given by the second speaker? (list two) B. In Chinese, share your answers with your partner. Activity 3 (Listening and Speaking). Below are two conversations between a male and a female. Listen once and answer the questions for each conversation (What is the relationship between the two speakers? Where did this conversation most likely take place? What did they discuss? / What information has the male speaker requested from the female speaker? (list two)); listen again to learn additional details and decide which conversation happens first and which next, and give your rationale. (Audio, not included.)"),
        card("Activity 2 (Reading, Speaking and Listening): a college student’s diary",
             "New vocabulary: 休闲娱乐 (xiūxián yúlè; entertainment and recreation), 爱好 (àihào; hobby), 博物馆 (bówùguǎn; museum). A. Read a college student’s diary entry and, in English, write a summary. B. Pair up. Each partner writes three questions from the passage to ask of their partner. C. Take turns with your partner using the prompts to retell the story: 1. 我最大的爱好是：为什么？ 2. 但是爸爸妈妈觉得：因为…，所以…",
             examples=[D(DI, DI_E)]),
        card("Activity 4 (Reading, Listening and Speaking): two concert passages",
             "New vocabulary: 交响乐团 (jiāoxiǎngyuè tuán; Symphony Orchestra), 观众 (guānzhòng; Audience), 鼓掌 (gǔzhǎng; applaud), 光盘 (guāngpán; CD). Below are two passages about two people’s concert experience. A. Pair up. Student A reads Passage 1 and Student B reads Passage 2; take notes in the box provided (Specific event; Location; How he found out about it; Concert details; What he did after the event). B. In Chinese, Student A shares the information from Passage 1 with Student B, and Student B shares Passage 2. C. With your partner, write the similarities and differences between the two passages.",
             examples=[D(PA1, PA1_E), D(PA2, PA2_E)]),
    ],
    exercises=[
        M("What is the diary writer’s biggest hobby?", "Singing at KTV with friends", ["Visiting museums", "Studying", "Playing sports"], "最大的爱好是跟朋友去ＫＴＶ唱歌."),
        M("What do the parents think the writer should do?", "Study hard and visit museums", ["Sing more", "Work part time", "Travel"], "应该好好努力学习，参观博物馆."),
        M("Why does the writer’s money keep getting less?", "KTV costs over three hundred yuan an hour, plus food", ["He lost it", "He bought a car", "He pays rent"], "一个小时要三百多块钱，吃东西还得另外付钱."),
        M("What will the writer do to get more pocket money?", "Study hard", ["Work", "Sing", "Beg"], "好好努力学习，这样爸妈才会给我更多零用钱."),
        M("Where did Passage 1’s writer work two years ago?", "Nanjing", ["Shanghai", "Beijing", "San Francisco"], "我在中国的南京市工作."),
        M("Which orchestra came to perform in Passage 1?", "The San Francisco Symphony", ["The Shanghai Symphony", "The Berlin Philharmonic", "A rock band"], "美国的旧金山交响乐团."),
        M("How far is Nanjing from Shanghai by car?", "A bit over two hours", ["Ten minutes", "Twelve hours", "A day"], "开车只要两个多小时."),
        M("How did Passage 2’s writer find out about the concert?", "The hotel attendant phoned the concert hall", ["From a newspaper", "From an email", "From a friend"], "服务员马上就给上海音乐厅打了一个电话."),
        M("What did Passage 2’s writer buy after the concert?", "A CD of Chinese pop music", ["A T-shirt", "A book", "A poster"], "买了一张中国流行音乐的光盘."),
        M("What did the audience do at the end of Passage 2’s concert?", "Stood up and applauded", ["Left quietly", "Sang along", "Danced"], "大家都站起来鼓掌."),
        F("我告诉我的朋友，我一定___去看这场音乐会。", "得", PART, "得 (děi): must."),
        F("唱累了，那儿的服务员还会给我们送上各___吃的。", "种", PART, "各种."),
    ],
)

# ------------------------------------------------------------------ 7. context
SCH = table(["节目", "日期", "时间", "地点"],
            [["京剧《空城计》", "二零二零年五月十四日和二十八日", "下午一点半和晚上七点一刻", "上海京剧院"], ["音乐剧《音乐之声》", "二零二零年五月四日到十日", "晚上七点；星期六、星期天加早场，下午两点，各一场", "上海大剧院"], ["德国爱乐交响乐团", "二零二零年五月十二日和十三日", "晚上七点半", "上海音乐厅"], ["新裤子乐队演唱会", "二零二零年五月九日和十日", "晚上八点", "上海体育场"]],
            title="This week’s performances (the book gives dates and times as digits; my reading of the layout)", say=[0, 1, 2, 3])
BD = ("五月天是一个一九九九年在台湾成军的摇滚乐队。乐队一共有五个人。一个主唱。两个吉他手，一个贝斯手和一个鼓手。他们来自台湾各地，多半的队员以前在高中就认识了，那时他们在学校组成了一个乐队。后来他们开始在很多酒吧和餐厅演唱。慢慢地越来越多的人认识他们，喜欢他们的音乐了。到现在他们一共出了九张唱片，也在许多地方开过演唱会，每一场演唱会都有几万人参加。除了台湾以外，他们也到过日本、中国和美国演出，所以在世界各地都有很多的粉丝。")
BD_E = ("Mayday is a rock band formed in Taiwan in 1999. The band has five people: one lead singer, two guitarists, one bass player and one drummer. They come from all over Taiwan, and most of the members already knew each other in high school, when they formed a band at school. Later they began to sing in many bars and restaurants. Slowly more and more people got to know them and like their music. By now they have put out nine albums altogether and have held concerts in many places, with tens of thousands attending each concert. Besides Taiwan they have also performed in Japan, China and the US, so they have many fans all over the world.")
SG = [("李宇春：一九八四年生，四川人。二零零五年她还在上大学三年级的时候，她的妈妈帮她报名参加了一个电视台的歌唱比赛，在那次比赛中她得了第一名，开始有越来越多人认识她。她做的音乐非常多样，有摇滚、嘻哈，电子舞曲，中国风等。除了唱歌以外，她也是一名女演员，她演过电影、电视剧和话剧。另外她也很有爱心，帮助过许多儿童。", "Li Yuchun: born in 1984, from Sichuan. In 2005, when she was still in her third year of university, her mother signed her up for a TV station’s singing contest, and she won first place in it; more and more people began to know her. The music she makes is very varied: rock, hip-hop, electronic dance music, Chinese style and so on. Besides singing she is also an actress who has acted in movies, TV series and stage plays. In addition she is very kind-hearted and has helped many children."),
      ("周杰伦：一九七九年出生在台湾台北，父母都是老师。他从小学习钢琴，高中就读音乐班。他的音乐非常多样。除了流行音乐以外，他的中国嘻哈和说唱音乐也很受欢迎。成名后他不但唱歌，开演唱会，还拍电影，开餐厅。", "Jay Chou: born in 1979 in Taipei, Taiwan, both parents teachers. He learned piano from childhood and attended a music class in high school. His music is very varied. Besides pop, his Chinese hip-hop and rap are also very popular. After becoming famous he not only sings and holds concerts but also makes movies and opens restaurants."),
      ("华晨宇：一九九零年出生在中国湖北省，他上了湖北武汉音乐学院，会好几种乐器。他参加过许多电视歌唱比赛，也给许多电视剧写过歌。他唱的歌多半都是自己做的。他的歌不仅是流行音乐，也关心许多世界问题。虽然他很年轻，但已经是中国最受欢迎的男歌手了。", "Hua Chenyu: born in 1990 in Hubei Province, China; he attended Hubei’s Wuhan Conservatory of Music and can play several instruments. He has taken part in many TV singing contests and has written songs for many TV series. Most of the songs he sings he made himself. His songs are not only pop music but also care about many world problems. Although he is young, he is already the most popular male singer in China.")]
L7 = lesson(
    "Lesson 16 Presentation 2: using Chinese in context",
    "演唱会的票 · 五月天 · 李宇春、周杰伦、华晨宇 · 年代售票",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading and Speaking): buying concert tickets",
             "New vocabulary: 演唱会 (yǎnchàng huì; concert), 京剧 (Jīngjù; Beijing Opera), 音乐剧 (yīnyuè jù; musical). Liu Yawen just moved to Shanghai and would like to attend a Chinese concert for the first time. A. Listen to the conversation and extract the EEIs: What does she want to see? How many tickets did she buy? When is the event? Where does she want to sit? How much do the tickets cost? How does she choose to pay? B. Pair up, read the script aloud and check your answers. C. Role play: read the schedule below and find a music performance you would like to see this week. Follow the format of the conversation and purchase a ticket; your partner plays the salesperson in the ticket booth; then switch. (Audio and the script, not included.)",
             tables=[SCH]),
        card("Activity 2 (Reading and Speaking): 五月天",
             "A. Below are new words from the passage that contain characters you have already learned. Guess the meaning based on the linguistic and contextual clues: 主唱 (zhǔchàng), 酒吧 (jiǔbā), 贝斯手 (bèisī shǒu), 唱片 (chàngpiàn). (Mine: lead singer; bar; bass player; record/album.) B. In English, write a brief introduction about this band using what you read. C. Select a band or a singer that you enjoy, post a picture of the band on Linoit and give an oral report to the class.",
             examples=[D(BD, BD_E)]),
        card("Activity 3 (Reading, Speaking and Listening): three influential singers",
             "New vocabulary: 钢琴 (gāngqín; Piano). Below are three influential singers on the Chinese music scene: 李宇春 (Lǐ Yǔchūn), 周杰伦 (Zhōu Jiélún), 华晨宇 (Huá Chényǔ); the book prints a photograph for each (not included). A. Form groups of three. Each student selects one singer and reads the description; take notes in the column under the singer’s name. B. Go to the internet and conduct a search on the singer you chose and add the information you find. C. Tell your group members about your singer; the group members listen and take notes in the table. The new word 嘻哈 (xīhā; hip-hop) and 说唱 (shuōchàng; rap) appear in the texts.",
             examples=[D(z, e, fixes={"得": "de2"} if "她得了第一名" in z else None) for z, e in SG]),
        card("Activity 4 Optional (Reading, Speaking and Listening): See a show!",
             "年代售票 is a popular site for purchasing tickets for a variety of entertainment and live performances in Taiwan. A. Pair up. Use the links the book gives to watch video clips on how to purchase tickets using the site; Student A takes notes on odd-numbered steps and Student B on even-numbered steps (steps 1 to 10); create step-by-step instructions in the table. B. Pair up. Go to the site and discuss which show you would like to see, including the type of performance, the date, time, price and location. C. Post your plans on Linoit and report to your class. (Videos and websites, not included.)"),
    ],
    exercises=[
        M("What is the band 五月天?", "A rock band formed in Taiwan in 1999", ["A pop duo", "A choir", "A jazz trio"], "一九九九年在台湾成军的摇滚乐队."),
        M("How many people are in 五月天?", "Five", ["Three", "Four", "Seven"], "乐队一共有五个人."),
        M("What did they do after high school?", "Sang in bars and restaurants", ["Left music", "Toured the world", "Went to college"], "开始在很多酒吧和餐厅演唱."),
        M("How many albums have they released?", "Nine", ["Three", "Five", "Twelve"], "一共出了九张唱片."),
        M("Where was 李宇春 born and what did she win?", "Sichuan; first place in a TV singing contest", ["Beijing; an acting prize", "Taiwan; a piano contest", "Hubei; a rap contest"], "四川人；得了第一名."),
        M("What instrument did 周杰伦 learn from childhood?", "Piano", ["Guitar", "Drums", "Violin"], "他从小学习钢琴."),
        M("What did 周杰伦 do after becoming famous?", "Held concerts, made movies and opened restaurants", ["Became a teacher", "Left music", "Opened a school"], "还拍电影，开餐厅."),
        M("Where did 华晨宇 study?", "Wuhan Conservatory of Music, Hubei", ["Taipei", "Sichuan", "Beijing"], "湖北武汉音乐学院."),
        M("What does 嘻哈 mean?", "Hip-hop", ["Rap only", "Jazz", "Opera"], "嘻哈: hip-hop."),
        M("Which is the Beijing opera in the schedule?", "《空城计》", ["《音乐之声》", "德国爱乐交响乐团", "新裤子乐队演唱会"], "京剧《空城计》."),
        M("Where is 《音乐之声》 staged?", "上海大剧院", ["上海京剧院", "上海音乐厅", "上海体育场"], "上海大剧院."),
        F("到现在他们一共出了九张唱___。", "片", PART, "唱片: album."),
    ],
)
L8 = vocab_lesson("Lesson 16 Presentation 2 vocabulary", "30 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English.", VOC2)

UNIT = unit("第十六课 娱乐活动 Presentation 2: rock band, 就 (ease), 越来越, reduplicated measure words, 对…感兴趣, concerts and singers", [L1, L2, L3, L4, L5, L6, L7, L8])
