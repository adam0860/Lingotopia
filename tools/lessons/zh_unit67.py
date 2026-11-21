"""Unit 67: Lesson 23 (Study in China) Presentation 2 from the book's texts: Lily's email from Shenzhen, the five activities (word building, dishes, the odd
word out), 每 as a demonstrative, the soothing 的, 差不多/左右/大约/大概, 和…相比, the skill-integration blog entry about Shanghai, the using-Chinese
passages (six cities, a tutor, an internship) and the vocabulary list. Audio, pictures and links are not included; numbers the book writes as digits
are spelled out in the Chinese text; answer keys and sample sentences the book does not print are mine and labeled."""
from zh_auto import *
from zh_l23_vocab import VOC2

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4"), ('觉得', 1, 'de5'), ('干净', 0, 'gan1'), ('还有', 0, 'hai2'), ('还是', 0, 'hai2'), ('还不', 0, 'hai2'), ('感觉', 1, 'jue2'), ('得去', 0, 'dei3'), ('就得', 1, 'dei3'), ('得开会', 0, 'dei3'), ('还得', 0, 'hai2'), ('好得多', 1, 'de5'), ('新得多', 1, 'de5'), ('多得', 1, 'de5'), ('得很好', 0, 'de5'), ('度假', 1, 'jia4')):
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

# ------------------------------------------------------------------ 1. email
E1 = ("安妮，你好：你要的中文书我已经买到了，昨天给你寄过去了。收到后，请给我发个电子邮件。",
      "Hello, Annie: I have already bought the Chinese book you wanted and mailed it to you yesterday. After you receive it, please send me an email. (translation mine)")
E2 = ("我来深圳实习差不多四个月了，一切都很好。我跟一个加拿大留学生合租了一套小公寓，房租不太贵，生活也很方便。深圳有很多外地人，各种风味的菜都能吃到，所以我和朋友经常在外面吃。吃着吃着我也学会了几道中国菜，有时也自己做着吃。我最拿手的菜是麻婆豆腐和宫保鸡丁。等我回纽约后，一定让你尝尝我的手艺。",
      "I have been doing my internship in Shenzhen for almost four months now and everything is fine. I share a small apartment with a Canadian international student; the rent is not too expensive and life is convenient. Shenzhen has many people from other places and you can eat dishes of every flavor, so my friends and I often eat out. As we ate, I too learned to make a few Chinese dishes, and sometimes I cook for myself. My best dishes are mapo tofu and kung pao chicken. After I go back to New York I will definitely let you taste my cooking. (mine)")
E3 = ("我每天都挺忙的，早上七点一刻就得坐地铁去上班。和纽约的地铁相比，深圳的地铁要新得多。我一般八点左右到公司。到公司后，我马上开始工作。中午常常和同事一起去饭馆吃饭。下午我不上班，但是一、三、五的下午要去深圳大学上法律课，二、四的下午跟家教学习中文。现在我的写作和语法都进步得很快，口语也比以前好多了。",
      "I am quite busy every day; at a quarter past seven in the morning I have to take the subway to work. Compared with the New York subway, Shenzhen’s is much newer. I usually arrive at the company at about eight. After I arrive I start work right away. At noon I often go to a restaurant to eat with colleagues. In the afternoon I don’t work, but on Monday, Wednesday and Friday afternoons I go to Shenzhen University for a law class, and on Tuesday and Thursday afternoons I study Chinese with a tutor. Now my writing and grammar are both progressing fast and my spoken Chinese is much better than before. (mine)")
E4 = ("你最近怎么样？你中文进步也很大吧？希望有时间你也来中国看一看。祝你一切顺利！丽莉",
      "How have you been recently? Your Chinese must have improved a lot too? I hope you will find time to come and see China. Wishing you all the best! Lily (mine)")
L1 = lesson(
    "Lesson 23 Presentation 2: Lily’s email from Shenzhen",
    "在深圳实习 · 合租小公寓 · 麻婆豆腐 宫保鸡丁 · 早上七点一刻上班 · 一三五上法律课",
    requires=[],
    cards=[
        card("Getting Started",
             "Pair up and discuss: A. Do you have any experience working as an intern, volunteer or employee? Briefly share with the class what your work and life was like. B. Do you know anyone who has worked in China or any other countries? If so, share their working experiences. (Four photographs are not included.)"),
        card("Presentation 2: 丽莉给安妮的电子邮件", "The book also prints the email in traditional characters. The translations are mine.", examples=[D(*E1), D(*E2), D(*E3), D(*E4)]),
    ],
    exercises=[
        M("What did Lily buy for Annie?", "A Chinese book", ["A scarf", "A phone", "A ticket"], "你要的中文书我已经买到了."),
        M("What does Lily ask Annie to do after receiving it?", "Send an email", ["Call her", "Write a letter", "Visit her"], "请给我发个电子邮件."),
        M("How long has Lily been interning in Shenzhen?", "Almost four months", ["One week", "Two years", "Half a day"], "差不多四个月了."),
        M("Who does Lily share an apartment with?", "A Canadian international student", ["An American teacher", "A Chinese colleague", "Her sister"], "合租了一套小公寓."),
        M("Why can she eat many flavors of food in Shenzhen?", "There are many non-local people there", ["It is a small city", "She cooks every day", "Food is free"], "深圳有很多外地人，各种风味的菜都能吃到."),
        M("What are Lily’s best dishes?", "Mapo tofu and kung pao chicken", ["Dumplings and noodles", "Hot pot and fish", "Fried rice and soup"], "麻婆豆腐和宫保鸡丁."),
        M("When does she take the subway to work?", "At a quarter past seven in the morning", ["At six", "At noon", "At nine"], "早上七点一刻."),
        M("How does the Shenzhen subway compare with New York’s?", "It is much newer", ["It is much older", "It is dirtier", "It is smaller"], "要新得多."),
        M("When does she usually reach the company?", "At about eight", ["At about ten", "At six", "At noon"], "八点左右到公司."),
        M("Which afternoons does she have a law class?", "Monday, Wednesday and Friday", ["Tuesday and Thursday", "Saturday", "Sunday only"], "一、三、五的下午要去深圳大学上法律课."),
        M("What does she do on Tuesday and Thursday afternoons?", "Studies Chinese with a tutor", ["Goes shopping", "Rests", "Cooks"], "二、四的下午跟家教学习中文."),
        F("我来深圳___习差不多四个月了。", "实", PART, "实习: intern."),
        F("我跟一个加拿大留学生合___了一套小公寓。", "租", PART, "合租: co-rent."),
        F("等我回纽约后，一定让你尝尝我的手___。", "艺", PART, "手艺: cooking skill."),
    ],
)

# ------------------------------------------------------------------ 2. activities
LW = table(["和“法”组成的词 (mine)", "和“作”组成的词 (mine)"], [["法律", "写作"], ["方法", "工作"], ["办法", "作业"], ["语法", "作文"], ["文法", "合作"], ["写法", "作家"], ["说法", "操作"], ["做法", "作用"]], title="Activity 3: words with 法 and 作 (the book shows two circle diagrams, with 法律 and 写作 given; the rest is mine)", say=[0, 1])
DISH = table(["拿手菜", "主要食材", "风味"], [["麻婆豆腐", "豆腐，肉，辣椒", "四川菜，麻辣"], ["宫保鸡丁", "鸡肉，花生，辣椒", "四川菜，又辣又甜"], ["西红柿炒鸡蛋", "西红柿，鸡蛋", "家常菜，酸甜"]], title="Activity 4: dishes you can cook (the book gives the first row; the other rows are mine)", say=[0, 1, 2])
ODD = table(["词组", "不同的一个 (mine)", "原因 (mine)"], [["留学生，外地人，加拿大人，鸡丁", "鸡丁", "The others are kinds of people; 鸡丁 is food."], ["深圳，纽约，口语，华盛顿", "口语", "The others are cities; 口语 is spoken language."], ["家教，顺利，进步，实习", "顺利", "The others are things Lily does or has; 顺利 is a wish word (an adjective)."], ["手艺，尝尝，祝，合租", "手艺", "The others are verbs; 手艺 is a noun."]], title="Activity 5: the odd one out (the book gives no key; these are possible answers of mine, and other answers can be argued)", say=[0, 1])
L2 = lesson(
    "Lesson 23 Presentation 2 activities: listening, word building, dishes and the odd word out",
    "Activities 1 to 5 · 法律 写作 · 麻婆豆腐 · 留学生 外地人 · 家教 顺利",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Global listening: listen to Presentation 2 and answer: 1. What means of communication is discussed? (an email) 2. What was the topic between the respondents? (life and work as an intern in Shenzhen) 3. What is the relationship between Annie and Lily? (friends). B. Detailed listening: 1. How is Lily’s life in Shenzhen? Provide three details (a shared apartment, food of every flavor, she cooks too). 2. Why does Lily say she is very busy? What does her weekly schedule look like? (work in the morning, a law class on Monday, Wednesday and Friday afternoons, a tutor on Tuesday and Thursday afternoons). C. Pair up, discuss and share. (Audio, not included; the answers in brackets are from the text.)"),
        card("Activity 2 (Listening, Reading and Speaking)",
             "A. Listen to Passage 1 (about 安娜, an intern at Alibaba in Hangzhou; two photographs, West Lake and the Alibaba headquarters, are not included) and mark the statements True or False: 1. 安娜还没有从纽约大学毕业就已经在阿里巴巴实习了。 2. 安娜喜欢住在杭州因为那儿的房价比别的城市便宜多了。 3. 周末的时候，安娜常常去饭馆吃饭因为杭州什么风味的菜都有。 4. 安娜很喜欢做饭，可她做不好中国饭。 B. Pair up, discuss and justify your answers. C. Talk about your life in a foreign country. D. Listen to Passage 2 and mark True or False: 1. 安娜早上六点起床，七点一刻坐地铁上班。 2. 杭州的地铁比纽约的地铁干净多了，也不太挤。 3. 安娜一到公司就和同事们一起开会。 4. 安娜每个下午都去学中文，所以她的写作和语法进步很大。 E. Pair up and justify. F. Talk about your weekly schedule. (Audio, not included; the book prints no key.)"),
        card("Activity 3 (Speaking and Writing): 组词练习",
             "A. Pair up and fill in the circles with the characters that can go with 法 and 作. B. With your partner, fill in the table below the words you came up with. Each pair presents to the class.",
             tables=[LW]),
        card("Activity 4 (Speaking and Writing): 说说你会做什么中国菜",
             "A. Think of at least two Chinese dishes that you can cook well, or you enjoy, and write them in the table in Pinyin or characters. Also indicate the main ingredients and what kind of flavor the dishes have. B. Each pair presents to the class and takes notes on other pairs’ dishes. (Two photographs are not included.)",
             tables=[DISH]),
        card("Activity 5 (Reading, Writing and Speaking)",
             "A. Pair up and discuss the following words. Choose the odd word in each group and explain why it does not go with the others. B. With your partner, write a short story using the words in Step A. Use at least five words and write at least five sentences in your story. C. Each pair reads their story aloud to the class.",
             tables=[ODD]),
    ],
    exercises=[
        M("Which word goes with 法 in 法律?", "法律课", ["法国", "写作", "方便"], "法律 = law."),
        M("Which compound contains 作?", "写作", ["写字", "语法", "办法"], "写作 = writing."),
        M("Which is a Sichuan dish?", "麻婆豆腐", ["北京烤鸭", "广东早茶", "上海小笼包"], "麻婆豆腐 is Sichuan."),
        M("What are the main ingredients of mapo tofu in the book’s example?", "Tofu, meat and chili", ["Chicken and peanuts", "Fish and rice", "Noodles and eggs"], "豆腐, 肉, 辣椒."),
        M("What flavor does mapo tofu have in the book’s example?", "Numbing and spicy", ["Sweet and sour", "Salty", "Bitter"], "麻辣."),
        M("Which is the odd one: 留学生，外地人，加拿大人，鸡丁?", "鸡丁", ["留学生", "外地人", "加拿大人"], "鸡丁 is food, not a kind of person."),
        M("Which is the odd one: 深圳，纽约，口语，华盛顿?", "口语", ["深圳", "纽约", "华盛顿"], "口语 is not a city."),
        F("我最拿___的菜是麻婆豆腐和宫保鸡丁。", "手", PART, "拿手: best at."),
        F("和“法”组成的词有法___。", "律", PART, "法律: law."),
    ],
)

# ------------------------------------------------------------------ 3. 每, 的
MS = [("她做的每道菜都好吃。", "1. Every dish she cooks is very delicious."), ("我们班每个学生都很努力学习。", "2. Every student in our class studies very hard."), ("我每天都挺忙的。", "3. I am busy every day. (天, 年, 周, 次 etc. are measure words themselves)"), ("她妈妈每年都来美国度假。", "4. Her mother comes to America for vacation every year."),
      ("每班有几个女学生？每班有三个女学生。", "5. How many female students are in each class? Each class has three. (都 is not always used)"), ("每个学生有四本书。", "6. Every student has four books. (都 optional)"), ("每个学生有两个工作。", "7. Every student has two jobs. (都 optional)")]
DE = [("我每天都挺忙的。", "1. I’m very busy every day. (的 shows the speaker is certain)"), ("别着急，他会好起来的。", "2. Don’t worry, he will get better. (会 … 的 emphasizes certainty)")]
DR = [("好啊，高铁挺快的，几个小时就到了，比坐飞机方便多了。", "The book’s example: Student A: 我们坐高铁去北京怎么样？ Student B: Good idea, the high-speed train is pretty fast; it takes only a few hours, much more convenient than flying."), ("我打算去邮局寄，邮局的价格便宜，也很安全的。", "1. I plan to mail it at the post office; the post office is cheap and also safe. (reply to 这个包裹你打算怎么寄？, mine)"), ("别担心，你吃几天药就会好的。", "2. Don’t worry, you’ll get better after a few days of medicine. (reply to the doctor question, mine)"),
      ("你的血压不会有问题的，很正常。", "3. Your blood pressure won’t have a problem; it’s normal. (mine)"), ("好吃，它们都很好吃的。", "4. Yes, they are both very tasty. (mine)"), ("中国的地铁挺新的，也挺干净的。", "5. Chinese subways are quite new and also quite clean. (mine)"), ("别紧张，你复习得很好，一定会考好的。", "6. Don’t be nervous; you’ve reviewed well and will certainly do well. (mine)")]
L3 = lesson(
    "Lesson 23 Presentation 2 grammar: 每 as a demonstrative and the soothing 的",
    "每道菜都 · 每天都 · 每年都 · 都不一定要用 · 会…的 · 他会好起来的",
    requires=[],
    cards=[
        card("The Use of 每 as a Demonstrative",
             "每 is a demonstrative, meaning “each” and “every”. Like all demonstratives, it requires the assistance of a measure word before it can be placed before a noun. Generally, 都 is added to the predicate in sentences with 每 to highlight variety: 每 + Measure Word + Noun + 都. Certain words, like 天, 年, 周, 次, etc., do not use measure words because they themselves are already measure words: 每天（年，周，次…）都…. 都 is not always used in sentences with 每.",
             examples=[D(z, e) for z, e in MS]),
        card("Activity 1 (Listening, Writing and Speaking)",
             "A. Listen to six sentences with 每…都… and translate them into English. B. Pair up and check your translations with your partner. Then retell the sentences in Chinese with your partner. (Audio, not included.)"),
        card("The Use of 的 (a soothing tone)",
             "The particle 的 is most often a structural particle, but it can also be a sentence-final particle which indicates that the speaker is certain about what is said. When used this way, it expresses a type of “mood” and is thus called a “modal particle”. Frequently, the statement will include 会 or 一定会 to emphasize the speaker’s certainty. Pattern: Statement + 的.",
             examples=[D(z, e) for z, e in DE]),
        card("Activity 2 (Reading and Speaking)",
             "Pair up. Student A says something and Student B responds with 的. The book’s example: A: 我们坐高铁去北京怎么样？ B: 好啊，高铁挺快的，几个小时就到了，比坐飞机方便多了。 Then: 1. A: 这个包裹你打算怎么寄？去邮局寄还是让快递公司寄？ 2. A: 大夫，你觉得我这个病什么时候才能好？ 3. A: 大夫，护士刚给我量了血压，我想知道我的血压是不是正常。 4. A: 你觉得麻婆豆腐和宫保鸡丁好吃吗？ 5. A: 你知道中国的地铁是不是很新，很干净？ 6. A: 明天就要单元考试了。我很紧张，怕考不好。 The book leaves B blank; my replies:",
             examples=[D(z, e) for z, e in DR]),
    ],
    exercises=[
        M("What does 每 mean?", "Each, every", ["Some", "Few", "Half"], "每: each, every."),
        M("What does 每 need before a noun?", "A measure word", ["A verb", "An adverb", "Nothing"], "每 + measure word + noun."),
        M("Which word is usually added to the predicate with 每?", "都", ["才", "又", "再"], "每…都…."),
        M("Which words need no measure word after 每?", "天, 年, 周, 次", ["本, 张, 个", "只, 条, 双", "杯, 瓶, 碗"], "They are measure words themselves."),
        M("What does 她做的每道菜都好吃 mean?", "Every dish she cooks is delicious", ["She cooks one dish", "Some dishes are tasty", "She never cooks"], "每道菜都好吃."),
        M("What does the sentence-final 的 show?", "The speaker is certain about what is said", ["A question", "A past action", "A command"], "modal particle."),
        M("What do statements with this 的 often include?", "会 or 一定会", ["从来", "刚才", "已经"], "会 … 的."),
        M("What does 别着急，他会好起来的 mean?", "Don’t worry, he will get better", ["He is not getting better", "He is hurrying", "He got better yesterday"], "会…的: certain."),
        F("她妈妈每___都来美国度假。", "年", PART, "每年都."),
        F("我们班每个学生___很努力学习。", "都", PART, "每…都…."),
    ],
)

# ------------------------------------------------------------------ 4. approximations, 和…相比
AB = table(["词", "意思", "例句"], [["差不多", "almost, more or less", "差不多九点了，我们得开会了。"], ["左右", "more or less, about, or so", "安娜每天早上八点左右到公司。"], ["大约", "around, about (formal)", "高铁大约半个小时来一趟车。"], ["大概", "approximately, more or less; or to speculate, make a guess", "电视节目大概二十分钟有一个广告。 他今天没来上课，大概生病了。"]], title="The adverbs 差不多, 左右, 大约, 大概", say=[0, 2])
AE = [("我学了差不多四个月的中文了。", "差不多 + number + measure word: I have studied Chinese for almost four months."), ("张老师今年大约三十岁。", "大约 + number + measure word: Teacher Zhang is about thirty this year. (the book writes 30 in digits)"), ("这件衣服大概五十块钱。", "大概 + number: This garment is about fifty yuan."), ("我每天六点左右起床。", "number + measure word + 左右: I get up at about six every day.")]
BL = [("大概二十万人民币。", "A: 这辆车你花了多少钱？ B: About 200,000 yuan. (大概 implies the speaker is unclear or uncertain about the amount, or perhaps cannot remember)"), ("二十万人民币左右。", "B: Around 200,000 yuan. (左右 implies a greater level of accuracy or certainty)")]
CM = [("从蒙特雷开到旧金山差不多两个小时左右。", "1. It takes about two hours to drive from Monterey to San Francisco."), ("我老家夏天最高气温大约有四十摄氏度左右。", "2. The highest temperature in my hometown in summer is about 40 degrees Celsius."), ("这辆汽车大概才十万多人民币左右。", "3. This car is only about 100,000 yuan. (the book writes 40 in digits in sentence 2)")]
A4 = [("他大概是日本人。", "1. He is probably Japanese. (key mine; the book gives the blanks without an answer)"), ("今天中午有九十华氏度左右。", "2. It is about 90 degrees Fahrenheit at noon today. (左右)"), ("我今天差不多八点才到学校。", "3. I didn’t get to school until almost eight today. (差不多)"), ("大概明年这个时候，我就可以毕业了。", "4. About this time next year I can graduate. (大概)"), ("丽莉在深圳实习了差不多四个月了。", "5. Lily has been interning in Shenzhen for almost four months. (差不多)"), ("我们学校大约有三千多留学生。", "6. Our school has about three thousand international students. (大约)"), ("现在快两点了，他怎么还没到？大概路上堵车了。", "7. It’s nearly two; why hasn’t he arrived yet? Probably there’s a traffic jam. (大概)"), ("差不多十一点了，咱们该睡觉了，明天还得早起呢。", "8. It’s almost eleven; we should go to bed, we still have to get up early tomorrow. (差不多)")]
XB = [("和纽约的地铁相比，深圳的地铁要新得多。", "1. Compared with the New York subway, the Shenzhen subway is much newer."), ("中国跟三十年前相比，发生了巨大的变化。", "2. Compared with thirty years ago, China has undergone enormous changes. (the book prints a space after 中国)"), ("和东部比，我更喜欢美国的西部。", "3. Compared with the East, I like the American West more."), ("我的中文和上个月比，有了很大的进步。", "4. Compared with last month, my Chinese has made great progress.")]
XC = [("和刚学中文的时候比，我现在的中文进步了很多。", "1. Compared with when I had just begun to learn Chinese, my Chinese has improved a lot now. (Activity 5, my completion)"), ("和蒙特雷的气候相比，北京的冬天冷多了。", "2. Compared with the climate of Monterey, Beijing’s winter is much colder. (mine)"), ("和中国的人口数量相比，美国的人口少多了。", "3. Compared with China’s population, America’s population is much smaller. (mine)"), ("跟旧金山这个大城市比，蒙特雷小多了。", "4. Compared with a big city like San Francisco, Monterey is much smaller. (mine)"),
      ("和一般的大学比，我们学校的学生学外语的时间更长。", "5. Compared with ordinary universities, the students at our school spend more time learning foreign languages. (mine)"), ("和中国产品的价格比，进口产品的价格贵得多。", "6. Compared with the prices of Chinese products, the prices of imported products are much higher. (mine)")]
L4 = lesson(
    "Lesson 23 Presentation 2 grammar: 差不多, 左右, 大约, 大概 and 和…相比",
    "差不多四个月 · 八点左右 · 大约半个小时 · 大概二十万 · 和纽约的地铁相比",
    requires=[],
    cards=[
        card("The Adverbs 差不多, 左右, 大约, 大概",
             "The adverbs 差不多, 左右, 大约, 大概 are used to express approximations and can be interchangeable, but there are some differences. 差不多, 大约 and 大概 are placed before a number and measure word, whereas 左右 is placed after a number and measure word. Although 大概 and 左右 are used to make estimations or draw inferences, occasionally they have different connotations.",
             tables=[AB], examples=[D(z, e) for z, e in AE] + [D(z, e) for z, e in BL]),
        card("左右 with the others",
             "左右 can be used with 差不多, 大约 and 大概 to express approximations.",
             examples=[D(z, e) for z, e in CM]),
        card("Activities 3 and 4 (Reading and Speaking)",
             "Activity 3: Pair up. Each student asks their partner questions, who responds with 差不多, 左右, 大约, or 大概. A组问题: 1. 你每天几点睡觉？几点起床？ 2. 周末的时候，你大概几点起床，几点睡觉？ 3. 你每天大概学习多少个小时？ 4. 一个星期你大概学习多少个生词？ 5. 你大概一个月花多少钱？ B组问题: 1. 你打算什么时候回老家看父母？ 2. 你多长时间给你父母打一次电话？ 3. 在你老家，夏天的最高气温有多少？冬天的最低气温呢？ 4. 你老家有多少人口？ 5. 在你老家，多少钱才能买到一座房子？ Activity 4: Pair up, complete the sentences with 差不多, 左右, 大约, or 大概. The completed sentences (key mine):",
             examples=[D(z, e) for z, e in A4]),
        card("The Prepositional Phrase 和……相比",
             "The prepositional phrase 和……相比 is used to compare two things (A and B) with an emphasis on A. 跟 is also used with 相比. In colloquial Chinese, “相” can be omitted. Pattern: 和（跟）+ B +（相）比，A……",
             examples=[D(z, e) for z, e in XB]),
        card("Activity 5 (Reading and Speaking)",
             "A. Pair up. Student A will say the first part of the sentence and Student B will continue with the second part: 1. 和刚学中文的时候比，… 2. 和蒙特雷的气候相比… 3. 和中国的人口数量相比，… 4. 跟旧金山这个大城市比，… 5. 和一般的大学比，… 6. 和（跟）中国产品的价格比，… B. With your partner, create your own sentences. C. Share your group work with the class. My completions:",
             examples=[D(z, e) for z, e in XC]),
    ],
    exercises=[
        M("Where is 左右 placed?", "After the number and measure word", ["Before the number", "Before the verb", "At the beginning of the sentence"], "Number + measure word + 左右."),
        M("Which of these is placed before a number?", "大约", ["左右", "了", "的"], "差不多/大约/大概 + number."),
        M("Which is formal?", "大约", ["差不多", "左右", "大概"], "大约 is formal."),
        M("Which one can also mean “probably”?", "大概", ["左右", "差不多", "大约"], "大概: guess."),
        M("What does 他今天没来上课，大概生病了 mean?", "He didn’t come to class today; he’s probably ill", ["He is definitely ill", "He came late", "He was never ill"], "大概: speculate."),
        M("Which answer sounds more precise: 大概二十万 or 二十万左右?", "二十万人民币左右", ["大概二十万人民币", "Neither", "Both the same"], "左右 implies greater certainty."),
        M("How do you say “almost four months”?", "差不多四个月", ["四个月差不多的", "四差不多个月", "差四个月不多"], "差不多 + number + measure."),
        M("What does 和纽约的地铁相比，深圳的地铁要新得多 mean?", "Compared with New York’s subway, Shenzhen’s is much newer", ["Shenzhen’s subway is older", "They are the same age", "There is no subway in Shenzhen"], "和…相比, A…."),
        M("What can be omitted in colloquial Chinese in 和…相比?", "相", ["和", "比", "新"], "“相” can be omitted."),
        F("我每天六点___右起床。", "左", PART, "六点左右."),
        F("张老师今年___约三十岁。", "大", PART, "大约."),
    ],
)

# ------------------------------------------------------------------ 5. skill integration
BG = ("最近我忙着在上海找房子，前两天中介带我去徐汇区看了一个房子。这个房子很干净，有很多窗户，厨房也很大，而且离地铁站只有五分钟，交通很方便，我很喜欢，马上和他签了租房合同，付了半年的房租。",
      "Recently I have been busy looking for a place in Shanghai; a couple of days ago an agent (中介, zhōngjiè) took me to see an apartment in Xuhui District. The apartment is very clean with lots of windows and a big kitchen, and it is only five minutes from the subway station, so transportation is very convenient. I liked it very much, signed the rental contract with him immediately and paid half a year’s rent. (translation mine)")
BG2 = ("昨天早上，我从宾馆搬到了新租的房子。收拾好东西以后，我先去附近的家乐福买了一些东西。然后又去中国电信开通了网络服务。回到家后，我觉得非常累，想洗澡放松一下，结果却发现没有热水。我马上打电话给房东问他怎么回事，房东说需要把热水器打开才有热水。我按他说的，打开开关，热水就出来了。",
       "Yesterday morning I moved from the hotel into the newly rented apartment. After tidying up, I first went to a nearby Carrefour to buy a few things. Then I went to China Telecom to get the internet service connected. After getting home I felt very tired and wanted to wash and relax, but found there was no hot water. I immediately phoned the landlord to ask what was wrong, and he said I had to turn on the water heater to have hot water. I did as he said and turned on the switch (开关, kāiguān), and the hot water came out. (mine)")
BG3 = ("我来到上海差不多一个星期了，还没有看到太阳，天总是阴的，前天下雨了，感觉有点儿冷。今天我们公司的一个美国同事要回国，所以我们为他举办了一个聚会。大家在一起吃饭，聊天，然后去黄浦江坐游船看风景。我还拍了一个小视频，打算寄给我父母看。",
       "I have been in Shanghai for almost a week and still haven’t seen the sun; the sky is always overcast, and the day before yesterday it rained and felt a bit cold. Today an American colleague at our company is going back to his country, so we held a party for him. We ate and chatted together and then took a cruise on the Huangpu River to see the scenery. I also took a short video and plan to send it to my parents. (mine)")
BA = [("说话人找到的房子怎么样？", "1. What was the apartment the speaker found like? Answer (mine): clean, with many windows and a big kitchen, five minutes from the subway."), ("说话人搬到租好的房子里以后做了什么？", "2. What did the speaker do after moving in? Answer (mine): went shopping at Carrefour, had the internet connected, found no hot water and called the landlord."), ("上海那个星期的天气怎么样？", "3. What was the weather like that week? Answer (mine): overcast all the time, it rained and felt cold."), ("今天说话人做了什么？", "4. What did the speaker do today? Answer (mine): went to a farewell party for a colleague with a meal, chat and a river cruise.")]
L5 = lesson(
    "Lesson 23 Presentation 2 skill integration: working abroad, finding a home in Shanghai",
    "外国人在中国工作 · 来中国的目的 · 前途 网友 发挥 挑战 · 在上海找房子",
    requires=[],
    cards=[
        card("Activity 1 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the recording and write the main idea. B. Listen and transcribe the missing words in Pinyin, then translate into English: 还有一些外国人在中国从事…、贸易、…和投资方面的工作，因为中国是一个…大市场，和经济活动有关的工作机会很多。 C. Pair up and discuss. D. Listen again and answer: 1. 在中国教英语的外国人都是从说英语的国家来的吗？ 2. 除了教英文，外国人在中国还做什么工作？ 3. 为什么很多外国人觉得在中国工作和生活压力小？ 4. 这些在中国工作和学习的人回国以后会怎么样？ E. Discuss and share. F. Discuss: 1. 学完中文以后，你有没有去中国或是台湾工作和生活的计划？ 2. 如果你打算去中国或是台湾，你想做什么？ 3. 你喜欢这种“一边工作一边旅游”的生活方式吗？你打算将来去哪个国家过这样的生活？ (Audio, not included.)"),
        card("Activity 2 (Listening, Reading, Writing and Speaking)",
             "A. Listen to the recording and fill in the table 我来中国的目的 (mùdì; purpose): 第一个目的, 第二个目的, 第三个目的, with 其他信息. B. Pair up and discuss; read the script if necessary. C. Define the following words with your partner, using a dictionary if necessary: 前途 qiántú, 网友 wǎngyǒu, 发挥 fāhuī, 挑战 tiǎozhàn. D. Discussion: 说话人觉得在中国教英文没有挑战，不能发挥他的中文能力，你同意他的话吗？为什么？ (Audio, not included.)"),
        card("Activity 3 (Reading, Writing and Speaking)",
             "A. Read a blog entry by an American who works in China and answer the questions: 1. 说话人找到的房子怎么样？ 2. 说话人搬到租好的房子里以后做了什么？ 3. 上海那个星期的天气怎么样？ 4. 今天说话人做了什么？ B. Pair up and discuss. C. With your partner, discuss your experience of finding an apartment in another city or abroad. The blog entry (the book glosses 中介 and 开关 in pinyin in brackets) and my answers:",
             examples=[D(*BG), D(*BG2), D(*BG3)] + [D(z, e) for z, e in BA]),
    ],
    exercises=[
        M("Which district is the apartment in?", "Xuhui", ["Pudong", "Minhang", "Jing’an"], "徐汇区."),
        M("How far is the apartment from the subway?", "Five minutes", ["Fifty minutes", "Five hours", "Right next door"], "离地铁站只有五分钟."),
        M("How much rent did he pay at once?", "Half a year’s", ["One month’s", "Two years’", "None"], "付了半年的房租."),
        M("Where did he move from?", "A hotel", ["A dorm", "His parents’ home", "A friend’s house"], "从宾馆搬到了新租的房子."),
        M("Where did he shop nearby?", "Carrefour", ["A night market", "A pharmacy", "A bookstore"], "家乐福."),
        M("What did he do at China Telecom?", "Had the internet service connected", ["Bought a phone", "Paid the bill", "Applied for a job"], "开通了网络服务."),
        M("What was wrong when he got home?", "There was no hot water", ["No electricity", "No door key", "No furniture"], "没有热水."),
        M("How was the problem solved?", "He turned on the water heater switch", ["He called a plumber", "He took a cold shower", "He moved out"], "打开开关，热水就出来了."),
        M("How has the weather been in Shanghai?", "Overcast, with rain and a bit cold", ["Hot and sunny", "Snowing", "Foggy only"], "天总是阴的."),
        M("What did the company hold a party for?", "An American colleague going home", ["A birthday", "A new year", "A wedding"], "一个美国同事要回国."),
        F("这个房子很干净，有很多___户，厨房也很大。", "窗", PART, "窗户: windows."),
        F("我马上和他签了租房合___。", "同", PART, "合同: contract."),
    ],
)

# ------------------------------------------------------------------ 6. using Chinese
CITY = [("成都", "对西方人来说，成都是一个非常有味道的城市，这里有很多漂亮的竹林，还有大熊猫保护区。成都人的生活轻松、悠闲，非常适合喜欢安静的外国人。虽然四川话和普通话不一样，但成都能让外国人感受到真正的中国文化，欣赏到美丽的自然景色。", "Chengdu: For Westerners Chengdu is a very flavorful city with many beautiful bamboo forests and a giant panda reserve. Chengdu people’s life is relaxed and leisurely, very suitable for foreigners who like quiet. Although the Sichuan dialect is different from Mandarin, Chengdu lets foreigners feel real Chinese culture and enjoy beautiful natural scenery. (translation mine)"),
        ("广州", "广州是中国四个最大的城市之一。广州的商业活动非常活跃，很多外国人来这里做生意。广州和香港很近，这两个城市的人都说广东话。", "Guangzhou: Guangzhou is one of the four biggest cities in China. Business activity in Guangzhou is very active and many foreigners come here to do business. Guangzhou is close to Hong Kong, and people in both cities speak Cantonese. (mine)"),
        ("杭州", "杭州是一个轻松、浪漫的城市，也是一个有悠久历史的古城。对喜欢中国文化和历史的外国人来说，杭州是最好的选择。另外杭州有很多科技公司，马云的阿里巴巴总公司就在杭州。", "Hangzhou: Hangzhou is a relaxed, romantic city and also an ancient city with a long history. For foreigners who like Chinese culture and history, Hangzhou is the best choice. In addition Hangzhou has many technology companies; Jack Ma’s Alibaba headquarters is in Hangzhou. (mine)"),
        ("深圳", "深圳在香港旁边，也是中国四大城市之一。深圳有很多科技公司和贸易公司，是一个非常开放、自由的城市，非常受外国专业人士的喜爱。", "Shenzhen: Shenzhen is next to Hong Kong and is also one of China’s four big cities. Shenzhen has many technology and trading companies and is a very open and free city, much loved by foreign professionals. (mine)"),
        ("北京", "北京是中国的首都，既是古老的城市，又是现代化的大都市。北京有最好的大学，也有和美国硅谷一样的中关村。百度和联想公司都在那里。北京有各个国家的大使馆，很多外国公司也喜欢把总部设在北京。", "Beijing: Beijing is China’s capital, both an ancient city and a modern metropolis. Beijing has the best universities and also Zhongguancun, which is like America’s Silicon Valley; Baidu and Lenovo are both there. Beijing has the embassies of every country and many foreign companies like to put their headquarters in Beijing. (mine)"),
        ("上海", "上海是中国最大的城市，是一个国际大都市。上海的生活丰富多彩，中西文化汇集，很多外国人喜欢在这里工作和生活。上海是经济、金融中心，有很多的工作机会。", "Shanghai: Shanghai is China’s largest city, an international metropolis. Life in Shanghai is rich and colorful, Chinese and Western cultures meet, and many foreigners like to work and live here. Shanghai is an economic and financial center and has many job opportunities. (mine)")]
CITYD = [D(zh, en) for _, zh, en in CITY]
INTRO = ("随着中国经济的不断发展，越来越多的外国人来中国工作和学习。老外们通常喜欢去哪些城市呢？下面是老外们选出的最想去的六座城市，我们来看看他们是怎么描述这几个城市的？",
         "With the continuous development of China’s economy more and more foreigners come to China to work and study. Which cities do foreigners usually like to go to? Below are the six cities that foreigners picked as the ones they most want to go to; let’s see how they describe them. (translation mine)")
WRD = table(["生词", "拼音", "English"], [["工资", "gōngzī", "salary"], ["待遇", "dàiyù", "benefit"], ["奖金", "jiǎngjīn", "bonus"], ["补助", "bǔzhù", "subsidy"]], title="Activity 3: the new words", say=[0])
RPLY = ("小楠，你好：收到你的邮件，知道你在杭州的阿里巴巴实习，一切都很顺利，我真为你高兴。我对阿里巴巴的实习机会很感兴趣。你能告诉我怎么申请吗？实习的工资和待遇怎么样？有没有奖金和补助？我的中文还不太好，会不会有问题？希望你尽快回信。祝你一切顺利！",
        "Hello, Xiaonan: I received your email and learned that you are interning at Alibaba in Hangzhou and everything is going well; I am really happy for you. I am very interested in the internship opportunities at Alibaba. Can you tell me how to apply? What are the salary and benefits of the internship like? Are there bonuses and subsidies? My Chinese is still not very good; will that be a problem? I hope you will reply soon. Wishing you all the best! (my sample reply to Activity 3C; translation mine)")
L6 = lesson(
    "Lesson 23 Presentation 2 using Chinese in context: six cities, a tutor and an internship email",
    "外国人最想去的六座城市 · 找家教 · 阿里巴巴实习 · 工资 待遇 奖金 补助",
    requires=[],
    cards=[
        card("Activity 1 (Reading, Writing and Speaking)",
             "Scenario: your class is going to graduate and several of you would like to work and live in China. Your teacher just saw a news report about the most favored cities for foreigners and recommends it to you. Read about these cities and research them online; then select a city for your journey. A. In two groups, Group A reads about Chengdu, Guangzhou and Hangzhou and Group B reads about Shenzhen, Beijing and Shanghai. Summarize the passage about each city in the table. B. Within your group, fill in the table with information on the city your group likes most and your reasons. C. Each group presents its selection and reasons to the class. (Six photographs are not included.)",
             examples=[D(*INTRO)] + CITYD),
        card("Activity 2 (Listening, Writing, Reading and Speaking)",
             "Scenario: you are working for an American company in China. You want to improve your Chinese and find a private tutor. You hear an advertisement on the radio about a Chinese teacher and you are interested. Call this teacher to schedule a private lesson. A. Listen to the radio advertisement and write a summary. B. Pair up and discuss; read the script if needed. C. Role-play: call this teacher and ask for the information you need; your partner plays the teacher at the tutoring center. Questions you want to ask: 你们的家教中心在哪儿？你们都有什么课？你们的老师怎么样？一节课多少钱？到家里上课多少钱？什么时间上课？一次上几个小时？ Questions the tutoring center wants to ask: 你是怎么知道我们家教中心的？你以前学过中文吗？在哪儿学的？你为什么要请家教？你想在哪方面提高你的中文水平？你住在哪儿？你想一次学几个小时？ (Audio, not included.)"),
        card("Activity 3 (Listening, Writing, Reading and Speaking)",
             "Scenario: you have just received an email from your old classmate, who is working as an intern for Alibaba in Hangzhou, China. After reading the email, you reply, expressing your interest in working for Alibaba and hoping to learn more about becoming an intern. A. Listen to the email and write a summary (audio, not included). B. Pair up, discuss and read the script if necessary. C. With your partner, reply to your classmate’s email (TO: 小楠; Subject: 你写给小楠的电子邮件). D. Share your email with the class. My sample reply:",
             tables=[WRD], examples=[D(*RPLY)]),
    ],
    exercises=[
        M("Which city has bamboo forests and a giant panda reserve?", "Chengdu", ["Beijing", "Shanghai", "Shenzhen"], "成都…竹林…大熊猫保护区."),
        M("Which dialect do Guangzhou and Hong Kong share?", "Cantonese", ["Mandarin", "Sichuanese", "Shanghainese"], "这两个城市的人都说广东话."),
        M("Which city has the Alibaba headquarters?", "Hangzhou", ["Beijing", "Shenzhen", "Chengdu"], "马云的阿里巴巴总公司就在杭州."),
        M("Which city is next to Hong Kong and full of technology companies?", "Shenzhen", ["Shanghai", "Guangzhou", "Hangzhou"], "深圳在香港旁边."),
        M("Which city has Zhongguancun, like Silicon Valley?", "Beijing", ["Shanghai", "Chengdu", "Hangzhou"], "中关村."),
        M("Which city is China’s largest?", "Shanghai", ["Beijing", "Guangzhou", "Shenzhen"], "上海是中国最大的城市."),
        M("Which city has the embassies of all countries?", "Beijing", ["Shanghai", "Chengdu", "Guangzhou"], "北京有各个国家的大使馆."),
        M("What does 奖金 mean?", "Bonus", ["Salary", "Benefit", "Subsidy"], "奖金: bonus."),
        M("What does 待遇 mean?", "Benefits, treatment", ["Bonus", "Rent", "Travel"], "待遇: benefit."),
        F("我对阿里巴巴的实习机会很感___趣。", "兴", PART, "感兴趣."),
        F("实习的工___和待遇怎么样？", "资", PART, "工资: salary."),
    ],
)

# ------------------------------------------------------------------ 7. vocabulary
L7 = vocab_lesson("Lesson 23 Presentation 2 vocabulary", "23 words from the book’s Presentation 2 list",
                  "Presentation 2 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English; its glosses are kept as printed.", VOC2)

UNIT = unit("第二十三课 Presentation 2: 丽莉在深圳, 每…都, 的, 差不多左右大约大概, 和…相比", [L1, L2, L3, L4, L5, L6, L7])
