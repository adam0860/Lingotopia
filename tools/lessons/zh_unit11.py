"""Unit 11: seasons, weather and climate (lessons 103-117): the four seasons, weather words, frequency,
question words, likes, 因为…所以, 不…也不…, 可以/不能, temperature, 跟…一样, 比, 没有…这么/那么, 可是, 好+verb, review.
Original text; the scope follows DLIFLC Chinese Basic Program Unit 1 Lesson 5, Presentations 2 and 3."""
from dsl_zh import *

PART = ["吗", "们", "呢"]

# ---------------------------------------------------------------------------- 103
L103 = lesson(
    "The four seasons",
    "春天 · 夏天 · 秋天 · 冬天 · 季节",
    requires=[],
    cards=[
        card("Spring, summer, autumn, winter",
             "The four seasons are 春天 (chūntiān), 夏天 (xiàtiān), 秋天 (qiūtiān) and 冬天 (dōngtiān), and a season is a 季节 (jìjié). "
             "They always come in this order, and 天 (day, sky) is part of each name. A year has four seasons: 一年有四个季节. "
             "To ask what someone likes, use 喜欢 (xǐhuan): 你喜欢哪个季节？",
             tables=[wtable([("春天", "chun1tian1", "spring"), ("夏天", "xia4tian1", "summer"), ("秋天", "qiu1tian1", "autumn"), ("冬天", "dong1tian1", "winter"),
                             ("季节", "ji4jie2", "a season"), ("四个季节", "si4 ge4 ji4jie2", "four seasons"), ("喜欢", "xi3huan5", "to like"), ("一年", "yi4 nian2", "a year")])]),
        card("Using the seasons",
             "Season words work like time words: put them at the front of the sentence, or after the subject.",
             examples=[ex("一年有四个季节。", "yi4 nian2 you3 si4 ge4 ji4jie2", "A year has four seasons.", hl="四个季节"),
                       ex("春天、夏天、秋天和冬天。", "chun1tian1, xia4tian1, qiu1tian1 he2 dong1tian1", "Spring, summer, autumn and winter."),
                       ex("我喜欢春天。", "wo3 xi3huan5 chun1tian1", "I like spring.", hl="喜欢"),
                       ex("你喜欢哪个季节？ 我喜欢秋天。", "ni3 xi3huan5 na3 ge4 ji4jie2? wo3 xi3huan5 qiu1tian1", "Which season do you like? I like autumn.")]),
    ],
    exercises=[
        mean("春天", "chun1tian1", "spring", ["summer", "autumn", "winter"]),
        mean("夏天", "xia4tian1", "summer", ["spring", "autumn", "winter"]),
        mean("秋天", "qiu1tian1", "autumn", ["spring", "summer", "winter"]),
        mean("冬天", "dong1tian1", "winter", ["spring", "summer", "autumn"]),
        mean("季节", "ji4jie2", "a season", ["a year", "a day", "a festival"]),
        mean("喜欢", "xi3huan5", "to like", ["to hate", "to see", "to want"]),
        rd("春天", "chun1tian1", ["chun2tian1", "chun1tian3", "chun4tian1"]),
        rd("夏天", "xia4tian1", ["xia1tian1", "xia2tian1", "xia3tian1"]),
        rd("秋天", "qiu1tian1", ["qiu2tian1", "qiu4tian1", "qiu1tian4"]),
        rd("冬天", "dong1tian1", ["dong3tian1", "dong4tian1", "dong2tian1"]),
        M("Which season comes after 春天?", "夏天", ["秋天", "冬天", "春天"], "Spring, summer, autumn, winter."),
        M("Which season comes before 冬天?", "秋天", ["春天", "夏天", "冬天"], "Autumn is followed by winter."),
        M("How many seasons does a year have?", "四个", ["三个", "五个", "两个"], "Four."),
        M("How do you say “A year has four seasons”?", "一年有四个季节。", ["一年四个有季节。", "有一年四个季节。", "一年是四个季节有。"], "一年 + 有 + 四个季节."),
        M("How do you ask “Which season do you like?”", "你喜欢哪个季节？", ["你哪个喜欢季节？", "哪个你喜欢季节？", "你喜欢季节哪个？"], "喜欢 + 哪个季节."),
        F("我喜欢春___。", "天", PART, "春天 is spring.", tr="I like spring."),
        F("一年有四个___节。", "季", PART, "季节 is a season.", tr="A year has four seasons."),
        F("你喜欢哪个季___？", "节", PART, "季节 is a season.", tr="Which season do you like?"),
    ],
)

# ---------------------------------------------------------------------------- 104
L104 = lesson(
    "Weather words",
    "天气 · 热 · 冷 · 闷热 · 舒服 · 大风 · 大雪",
    requires=[],
    cards=[
        card("How is the weather?",
             "天气 (tiānqì) is weather. The basic describing words are 热 (rè, hot) and 冷 (lěng, cold), and 闷热 (mēnrè) is hot and stuffy. "
             "舒服 (shūfu) means comfortable, and in weather talk it is a gentle “nice”. A strong wind is 大风 (dàfēng) and heavy snow 大雪 (dàxuě); 大 here means “strong, heavy”. "
             "To say it is a weather: 下雨 (xià yǔ, rain falls), 下雪 (xià xuě, snow falls) and 刮风 (guā fēng, wind blows). 非常 (fēicháng) means “very”, a stronger 很.",
             tables=[wtable([("天气", "tian1qi4", "weather"), ("热", "re4", "hot"), ("冷", "leng3", "cold"), ("闷热", "men1re4", "hot and stuffy"),
                             ("舒服", "shu1fu5", "comfortable"), ("非常", "fei1chang2", "very"), ("大风", "da4feng1", "strong wind"), ("大雪", "da4xue3", "heavy snow"),
                             ("下雨", "xia4 yu3", "to rain"), ("下雪", "xia4 xue3", "to snow"), ("刮风", "gua1 feng1", "the wind blows")])]),
        card("Describing a day",
             "Use 天气 as the subject and an adjective after 很 or 非常.",
             examples=[ex("今天天气很冷。", "jin1tian1 tian1qi4 hen3 leng3", "The weather is cold today.", hl="很冷"),
                       ex("夏天非常热，有时候很闷热。", "xia4tian1 fei1chang2 re4, you3 shi2hou5 hen3 men1re4", "Summer is very hot, and sometimes hot and stuffy.", hl="非常"),
                       ex("秋天的天气很舒服。", "qiu1tian1 de5 tian1qi4 hen3 shu1fu5", "The weather in autumn is very comfortable."),
                       ex("明天下大雪。", "ming2tian1 xia4 da4 xue3", "Tomorrow there will be heavy snow.", hl="下大雪")]),
    ],
    exercises=[
        mean("天气", "tian1qi4", "weather", ["a day", "air", "a season"]),
        mean("热", "re4", "hot", ["cold", "warm", "stuffy"]),
        mean("冷", "leng3", "cold", ["hot", "cool", "windy"]),
        mean("闷热", "men1re4", "hot and stuffy", ["hot and dry", "cold and windy", "cool"]),
        mean("舒服", "shu1fu5", "comfortable", ["uncomfortable", "hot", "very"]),
        mean("非常", "fei1chang2", "very", ["not", "a little", "often"]),
        mean("大风", "da4feng1", "strong wind", ["a big storm", "heavy snow", "a fan"]),
        mean("大雪", "da4xue3", "heavy snow", ["strong wind", "heavy rain", "a snowman"]),
        mean("下雨", "xia4 yu3", "to rain", ["to snow", "to blow", "to swim"]),
        mean("刮风", "gua1 feng1", "the wind blows", ["it rains", "it snows", "it is hot"]),
        rd("天气", "tian1qi4", ["tian1qi1", "tian2qi4", "tian1qi3"]),
        rd("冷", "leng3", ["leng1", "leng2", "leng4"]),
        rd("热", "re4", ["re1", "re2", "re3"]),
        rd("非常", "fei1chang2", ["fei1chang3", "fei3chang2", "fei2chang2"]),
        M("What does 今天天气很冷 say?", "The weather is cold today.", ["Today is a cold day off.", "It is hot today.", "I am cold today."], "天气 is weather."),
        M("How do you say “It snows”?", "下雪", ["刮雪", "下风", "热雪"], "下 + 雪."),
        M("How do you say “The wind blows”?", "刮风", ["下风", "刮雨", "吹冷"], "刮 + 风."),
        F("今天天___很冷。", "气", PART, "天气 is weather.", tr="The weather is cold today."),
        F("明天___大雪。", "下", PART, "下雪 is to snow.", tr="Tomorrow there will be heavy snow."),
        F("夏天非___热。", "常", PART, "非常 is very.", tr="Summer is very hot."),
    ],
)

# ---------------------------------------------------------------------------- 105
L105 = lesson(
    "How often it happens",
    "有时候 · 常常 · 很少 · 下大雨 · 刮大风",
    requires=[],
    cards=[
        card("Sometimes, often, rarely",
             "有时候 (yǒushíhou) is “sometimes” and 常常 (chángcháng) is “often”; both go before the verb. 很少 (hěn shǎo) is “rarely”. "
             "These time words may start the sentence or follow the subject, but they always come before the verb: 冬天常常下雪.",
             tables=[wtable([("有时候", "you3shi2hou5", "sometimes"), ("常常", "chang2chang2", "often"), ("很少", "hen3 shao3", "rarely"), ("下大雨", "xia4 da4 yu3", "heavy rain falls"),
                             ("刮大风", "gua1 da4 feng1", "strong wind blows"), ("那儿", "na4r5", "there"), ("这儿", "zhe4r5", "here")])]),
        card("There and here",
             "那儿 (nàr) is “there” and 这儿 (zhèr) is “here”. They end in the r sound, which is written 儿 and said as a light r on the previous syllable. "
             "Use them for a place: 那儿的冬天很冷 is “Winter there is cold”.",
             examples=[ex("我的老家冬天常常下大雪。", "wo3 de5 lao3jia1 dong1tian1 chang2chang2 xia4 da4 xue3", "In my hometown it often snows heavily in winter.", hl="常常"),
                       ex("那儿夏天有时候很闷热。", "na4r5 xia4tian1 you3shi2hou5 hen3 men1re4", "There, summer is sometimes hot and stuffy.", hl="有时候"),
                       ex("这儿的春天很少刮大风。", "zhe4r5 de5 chun1tian1 hen3 shao3 gua1 da4 feng1", "Here it rarely blows hard in spring."),
                       ex("你们那儿夏天热不热？", "ni3men5 na4r5 xia4tian1 re4 bu5 re4", "Is it hot in summer where you are?")]),
    ],
    exercises=[
        mean("有时候", "you3shi2hou5", "sometimes", ["often", "rarely", "never"]),
        mean("常常", "chang2chang2", "often", ["sometimes", "rarely", "always not"]),
        mean("很少", "hen3 shao3", "rarely", ["often", "sometimes", "very many"]),
        mean("那儿", "na4r5", "there", ["here", "where", "which"]),
        mean("这儿", "zhe4r5", "here", ["there", "where", "this"]),
        mean("下大雨", "xia4 da4 yu3", "heavy rain falls", ["light rain falls", "strong wind blows", "snow falls"]),
        M("Where does 常常 go?", "Before the verb", ["After the verb", "At the end", "After the object"], "Frequency words go before the verb."),
        M("What does 冬天常常下雪 mean?", "It often snows in winter.", ["It rarely snows in winter.", "It snows in summer.", "It sometimes snows."], "常常 is often."),
        M("What does 这儿的春天很少刮大风 say?", "Here it rarely blows hard in spring.", ["Here it often blows hard.", "Spring has no wind.", "There it rarely blows hard."], "很少 is rarely; 这儿 is here."),
        M("How do you say “sometimes it rains”?", "有时候下雨", ["下雨有时候", "有时下雨候", "时候有下雨"], "有时候 goes before the verb."),
        M("How do you ask “Is it hot there in summer?”", "那儿夏天热不热？", ["那儿夏天热吗不？", "夏天那儿热不吗？", "热不热那儿夏天？"], "Verb-not-verb question."),
        M("Which of these means “rarely”?", "很少", ["常常", "有时候", "非常"], "很少 is rarely."),
        F("我的老家冬天常___下大雪。", "常", PART, "常常 is often.", tr="In my hometown it often snows heavily in winter."),
        F("那___夏天有时候很闷热。", "儿", PART, "那儿 is there.", tr="There, summer is sometimes hot and stuffy."),
        F("这儿的春天很___刮大风。", "少", PART, "很少 is rarely.", tr="Here it rarely blows hard in spring."),
        F("你们那儿夏天热不___？", "热", PART, "Verb-not-verb.", tr="Is it hot in summer where you are?"),
    ],
)

# ---------------------------------------------------------------------------- 106
L106 = lesson(
    "Which, how and why",
    "哪个 · 怎么样 · 为什么",
    requires=[],
    cards=[
        card("Three question words",
             "哪个 (nǎge) is “which”: 你喜欢哪个季节？ 怎么样 (zěnmeyàng) is “how about it?”: 北京的天气怎么样？ "
             "为什么 (wèishénme) is “why” and sits before the verb: 你为什么喜欢夏天？ These words stay where the answer would go, and you do not add 吗.",
             tables=[table(["Pattern", "Meaning"],
                           [["你喜欢哪个季节？", "Which season do you like?"], ["北京的天气怎么样？", "How is the weather in Beijing?"], ["你为什么喜欢夏天？", "Why do you like summer?"],
                            ["你老家的冬天怎么样？", "How are winters in your hometown?"]], say=[0])]),
        card("Question and answer",
             "Answer 哪个 with the thing, 怎么样 with a description, and 为什么 with 因为 (because).",
             examples=[ex("你喜欢哪个季节？ 我喜欢秋天。", "ni3 xi3huan5 na3 ge4 ji4jie2? wo3 xi3huan5 qiu1tian1", "Which season do you like? I like autumn.", hl="哪个"),
                       ex("你老家的天气怎么样？ 夏天很热，冬天很冷。", "ni3 lao3jia1 de5 tian1qi4 zen3me5yang4? xia4tian1 hen3 re4, dong1tian1 hen3 leng3", "How is the weather in your hometown? Hot in summer and cold in winter.", hl="怎么样"),
                       ex("你为什么喜欢秋天？ 因为秋天很舒服。", "ni3 wei4shen2me5 xi3huan5 qiu1tian1? yin1wei4 qiu1tian1 hen3 shu1fu5", "Why do you like autumn? Because autumn is comfortable.", hl="为什么")]),
    ],
    exercises=[
        mean("哪个", "na3ge5", "which", ["that one", "this one", "where"]),
        mean("怎么样", "zen3me5yang4", "how about it?", ["how many", "why", "which"]),
        mean("为什么", "wei4shen2me5", "why", ["how about it?", "which", "when"]),
        rd("怎么样", "zen3me5yang4", ["zen4me5yang4", "zen3me5yang2", "zen2me5yang4"]),
        M("Which asks “which season”?", "哪个季节", ["什么季节", "哪里季节", "怎么季节"], "哪个 asks which."),
        M("Which asks about the weather?", "北京的天气怎么样？", ["北京的天气哪个？", "北京的天气为什么？", "北京的天气吗？"], "怎么样 asks how."),
        M("Which asks for a reason?", "你为什么喜欢夏天？", ["你哪个喜欢夏天？", "你怎么样喜欢夏天？", "你喜欢夏天怎么样？"], "为什么 asks why."),
        M("How do you answer 你为什么喜欢秋天？", "因为秋天很舒服。", ["我喜欢秋天。", "秋天在九月。", "秋天不冷。"], "为什么 is answered with 因为."),
        M("What does 你老家的冬天怎么样？ ask?", "How are winters in your hometown?", ["Which winter do you like?", "Why is winter cold?", "When is winter?"], "怎么样 is how about it."),
        M("Does a question with 哪个 need 吗?", "No", ["Yes", "Only in writing", "Only with 为什么"], "Question words already ask."),
        F("你喜欢___个季节？", "哪", PART, "哪个 is which.", tr="Which season do you like?"),
        F("你老家的天气怎么___？", "样", PART, "怎么样 is how about it.", tr="How is the weather in your hometown?"),
        F("你___什么喜欢夏天？", "为", PART, "为什么 is why.", tr="Why do you like summer?"),
        F("你老家的冬天怎___样？", "么", PART, "怎么样.", tr="How are winters in your hometown?"),
    ],
)

# ---------------------------------------------------------------------------- 107
L107 = lesson(
    "Liking most and liking least",
    "最喜欢 · 最不喜欢 · 不太喜欢",
    requires=[],
    cards=[
        card("最喜欢 and 最不喜欢",
             "Put 最 before 喜欢 to say “like best”: 我最喜欢春天. To say “like least”, put 不 between: 最不喜欢. "
             "Notice that 最 stays first and 不 sits right before the verb. 不太喜欢 is milder: “do not like very much”.",
             tables=[table(["Pattern", "Meaning"],
                           [["我最喜欢春天。", "I like spring best."], ["我最不喜欢冬天。", "I like winter least."], ["我不太喜欢夏天。", "I do not like summer very much."],
                            ["你最喜欢哪个季节？", "Which season do you like best?"]], say=[0])]),
        card("Giving a reason",
             "After the choice, add 因为 and a short reason (more in the next lessons).",
             examples=[ex("我最喜欢秋天，因为秋天很舒服。", "wo3 zui4 xi3huan5 qiu1tian1, yin1wei4 qiu1tian1 hen3 shu1fu5", "I like autumn best because it is comfortable.", hl="最喜欢"),
                       ex("我最不喜欢夏天，因为夏天很闷热。", "wo3 zui4 bu4 xi3huan5 xia4tian1, yin1wei4 xia4tian1 hen3 men1re4", "I like summer least because it is hot and stuffy.", hl="最不喜欢"),
                       ex("我不太喜欢冬天。", "wo3 bu2 tai4 xi3huan5 dong1tian1", "I do not like winter very much.")]),
    ],
    exercises=[
        mean("最喜欢", "zui4 xi3huan5", "like best", ["like a little", "do not like", "like very much"]),
        mean("最不喜欢", "zui4 bu4 xi3huan5", "like least", ["like best", "do not like very much", "like"]),
        M("What does 我最喜欢春天 say?", "I like spring best.", ["I like spring a bit.", "I like spring least.", "I like spring more than summer."], "最喜欢 is like best."),
        M("What does 我最不喜欢冬天 say?", "I like winter least.", ["I like winter best.", "I do not like winter very much.", "I like winter a bit."], "最不喜欢 is like least."),
        M("What does 我不太喜欢夏天 say?", "I do not like summer very much.", ["I like summer least.", "I like summer best.", "I like summer."], "不太 is not very."),
        M("Where does 不 go in “like least”?", "Between 最 and 喜欢", ["Before 最", "After 喜欢", "At the end"], "最不喜欢."),
        M("How do you say “Which season do you like best?”", "你最喜欢哪个季节？", ["你喜欢最哪个季节？", "你最哪个喜欢季节？", "哪个你最喜欢季节？"], "最 before 喜欢."),
        M("Which sentence gives a reason?", "我最喜欢秋天，因为秋天很舒服。", ["我最喜欢秋天，所以秋天很舒服。", "我最喜欢秋天，可是舒服。", "我喜欢秋天，还是舒服。"], "因为 starts the reason."),
        F("我___喜欢春天。 (best)", "最", PART, "最喜欢 is like best.", tr="I like spring best."),
        F("我最___喜欢冬天。 (least)", "不", PART, "最不喜欢 is like least.", tr="I like winter least."),
        F("我不___喜欢夏天。 (not very)", "太", PART, "不太 is not very.", tr="I do not like summer very much."),
        F("我最喜欢秋天，___为秋天很舒服。", "因", PART, "因为 is because.", tr="I like autumn best because it is comfortable."),
    ],
)

# ---------------------------------------------------------------------------- 108
L108 = lesson(
    "Because … so …",
    "因为 … 所以 … · 因为冬天下大雪，所以可以滑雪",
    requires=[],
    cards=[
        card("Reason and result",
             "因为 (yīnwèi) is “because” and 所以 (suǒyǐ) is “so”. In Chinese they usually come as a pair: 因为 reason, 所以 result. "
             "Unlike English, you may say both, and you may drop either one: 因为冬天很冷，所以我不喜欢冬天. "
             "Each clause has its own subject, and 所以 starts the result.",
             tables=[table(["Pattern", "Meaning"],
                           [["因为冬天很冷，所以我不喜欢冬天。", "Because winter is cold, I do not like it."], ["因为这儿很少下雪，所以不能滑雪。", "Because it rarely snows here, we cannot ski."],
                            ["因为夏天很热，所以我喜欢游泳。", "Because summer is hot, I like to swim."]], say=[0])]),
        card("New words",
             "游泳 (yóuyǒng) is to swim and 滑雪 (huáxuě) is to ski. Both are verbs, and 滑雪 is a verb with its object inside, so it cannot take another object.",
             tables=[wtable([("因为", "yin1wei4", "because"), ("所以", "suo3yi3", "so"), ("游泳", "you2yong3", "to swim"), ("滑雪", "hua2xue3", "to ski")]),],
             examples=[ex("因为夏天很热，所以我常常游泳。", "yin1wei4 xia4tian1 hen3 re4, suo3yi3 wo3 chang2chang2 you2yong3", "Because summer is hot, I often swim.", hl="所以"),
                       ex("因为我老家冬天下大雪，所以我们可以滑雪。", "yin1wei4 wo3 lao3jia1 dong1tian1 xia4 da4 xue3, suo3yi3 wo3men5 ke3yi3 hua2xue3", "Because it snows heavily in my hometown in winter, we can ski.")]),
    ],
    exercises=[
        mean("因为", "yin1wei4", "because", ["so", "but", "or"]),
        mean("所以", "suo3yi3", "so", ["because", "but", "or"]),
        mean("游泳", "you2yong3", "to swim", ["to ski", "to run", "to fly"]),
        mean("滑雪", "hua2xue3", "to ski", ["to swim", "to snow", "to skate"]),
        rd("所以", "suo3yi3", ["suo3yi4", "suo1yi3", "suo3yi2"]),
        rd("游泳", "you2yong3", ["you2yong2", "you3yong3", "you2yong4"]),
        M("What does 因为 start?", "The reason", ["The result", "A question", "A list"], "因为 gives the reason."),
        M("What does 所以 start?", "The result", ["The reason", "A question", "A list"], "所以 gives the result."),
        M("Choose the correct pair.", "因为冬天很冷，所以我不喜欢冬天。", ["所以冬天很冷，因为我不喜欢冬天。", "因为冬天很冷，因为我不喜欢冬天。", "所以冬天很冷，所以我不喜欢冬天。"], "因为 reason, 所以 result."),
        M("What does 因为这儿很少下雪，所以不能滑雪 say?", "Because it rarely snows here, we cannot ski.", ["Because we cannot ski, it rarely snows.", "It snows often, so we ski.", "It rarely snows because we ski."], "The reason is rare snow."),
        M("Can you drop 因为 and keep 所以?", "Yes", ["No, never", "Only in questions", "Only with 很少"], "Either may be dropped."),
        F("因为今天很冷，___我不去游泳。", "所以", PART, "所以 is so.", tr="Because it is cold today, I am not going to swim."),
        F("___为夏天很热，所以我喜欢游泳。", "因", PART, "因为 is because.", tr="Because summer is hot, I like to swim."),
        F("因为冬天下大雪，所以我们可以___雪。", "滑", PART, "滑雪 is to ski.", tr="Because it snows in winter, we can ski."),
        F("因为夏天很热，所以我常常游___。", "泳", PART, "游泳 is to swim.", tr="Because summer is hot, I often swim."),
    ],
)

# ---------------------------------------------------------------------------- 109
L109 = lesson(
    "Neither … nor …",
    "不冷也不热 · 不大也不小 · 不多也不少",
    requires=[],
    cards=[
        card("不 … 也不 …",
             "To say something is neither one thing nor another, use 不 + A, 也不 + B: 不冷也不热 is “neither cold nor hot”, so “just right”. "
             "The two parts are opposites, and 也 means “also”: “not cold, also not hot”. The pattern fits adjectives (不大也不小) and verbs (不吃也不喝).",
             tables=[wtable([("不冷也不热", "bu4 leng3 ye3 bu2 re4", "neither cold nor hot"), ("不大也不小", "bu2 da4 ye3 bu4 xiao3", "neither big nor small"),
                             ("不多也不少", "bu4 duo1 ye3 bu4 shao3", "neither many nor few"), ("不好也不坏", "bu4 hao3 ye3 bu2 huai4", "neither good nor bad")])]),
        card("In a sentence",
             "The whole phrase works as a description: 秋天不冷也不热. It does not need 很.",
             examples=[ex("我老家的春天不冷也不热。", "wo3 lao3jia1 de5 chun1tian1 bu4 leng3 ye3 bu2 re4", "Spring in my hometown is neither cold nor hot.", hl="不冷也不热"),
                       ex("那个城市不大也不小。", "na4 ge4 cheng2shi4 bu2 da4 ye3 bu4 xiao3", "That city is neither big nor small."),
                       ex("我们班的人不多也不少。", "wo3men5 ban1 de5 ren2 bu4 duo1 ye3 bu4 shao3", "The number of people in our class is neither many nor few.")]),
    ],
    exercises=[
        mean("不冷也不热", "bu4 leng3 ye3 bu2 re4", "neither cold nor hot", ["both cold and hot", "very cold", "not cold"]),
        mean("不大也不小", "bu2 da4 ye3 bu4 xiao3", "neither big nor small", ["both big and small", "very big", "not big"]),
        mean("不多也不少", "bu4 duo1 ye3 bu4 shao3", "neither many nor few", ["both many and few", "many", "few"]),
        M("What does 也 mean here?", "also", ["but", "so", "or"], "不 A 也不 B."),
        M("What does 秋天不冷也不热 say?", "Autumn is neither cold nor hot.", ["Autumn is both cold and hot.", "Autumn is very cold.", "Autumn is not cold."], "不冷也不热."),
        M("Does the pattern need 很?", "No", ["Yes", "Only before 冷", "Only before 也"], "The phrase stands alone."),
        M("How do you say “neither big nor small”?", "不大也不小", ["不大不也小", "也不大不小", "大不也小不"], "不 A 也不 B."),
        M("How do you say “neither cold nor hot”?", "不冷也不热", ["不冷也热不", "也不冷不热", "冷不也热不"], "不 A 也不 B."),
        M("Which sentence means “The city is neither big nor small”?", "那个城市不大也不小。", ["那个城市很大也很小。", "那个城市不大不也小。", "那个城市大也不小。"], "不大也不小."),
        F("我老家的春天不冷___不热。", "也", PART, "不 A 也不 B.", tr="Spring in my hometown is neither cold nor hot."),
        F("那个城市不大___不小。", "也", PART, "不 A 也不 B.", tr="That city is neither big nor small."),
        F("我们班的人不___也不少。", "多", PART, "不多也不少.", tr="The number of people in our class is neither many nor few."),
        F("秋天不冷也___热。", "不", PART, "也不 + B.", tr="Autumn is neither cold nor hot."),
    ],
)

# ---------------------------------------------------------------------------- 110
L110 = lesson(
    "Can and cannot: 可以 and 不能",
    "可以滑雪 · 不能滑雪 · 可以游泳吗？",
    requires=[],
    cards=[
        card("Allowed or possible",
             "可以 (kěyǐ) is “can” in the sense of “it is possible or allowed”: 夏天可以游泳. The opposite is 不能 (bù néng), “cannot”: 冬天不能游泳. "
             "Both go before the verb. A question is 可以……吗？, and the short answer is 可以 or 不可以, though 不能 is also very common.",
             tables=[table(["Pattern", "Meaning"],
                           [["夏天可以游泳。", "In summer we can swim."], ["冬天不能游泳。", "In winter we cannot swim."], ["这儿可以滑雪吗？", "Can we ski here?"],
                            ["可以，冬天下大雪。", "Yes, it snows heavily in winter."]], say=[0])]),
        card("With 因为 … 所以 …",
             "Reasons and permission go well together.",
             examples=[ex("因为这儿很少下雪，所以不能滑雪。", "yin1wei4 zhe4r5 hen3 shao3 xia4 xue3, suo3yi3 bu4 neng2 hua2xue3", "Because it rarely snows here, we cannot ski.", hl="不能"),
                       ex("因为我老家冬天下大雪，所以可以滑雪。", "yin1wei4 wo3 lao3jia1 dong1tian1 xia4 da4 xue3, suo3yi3 ke3yi3 hua2xue3", "Because it snows heavily in winter in my hometown, we can ski.", hl="可以"),
                       ex("你们那儿夏天可以游泳吗？", "ni3men5 na4r5 xia4tian1 ke3yi3 you2yong3 ma5", "Can you swim there in summer?")]),
    ],
    exercises=[
        mean("可以", "ke3yi3", "can, may", ["cannot", "should", "must"]),
        mean("不能", "bu4 neng2", "cannot", ["can", "may", "should"]),
        rd("可以", "ke3yi3", ["ke3yi4", "ke4yi3", "ke2yi3"]),
        M("What does 夏天可以游泳 say?", "In summer we can swim.", ["In summer we cannot swim.", "In summer we like to swim.", "We swim every day."], "可以 is can."),
        M("What does 冬天不能游泳 say?", "In winter we cannot swim.", ["In winter we can swim.", "In winter we do not like swimming.", "We swim in winter."], "不能 is cannot."),
        M("Where do 可以 and 不能 go?", "Before the verb", ["After the verb", "At the end", "Before the subject"], "可以 + verb."),
        M("How do you ask “Can we ski here?”", "这儿可以滑雪吗？", ["这儿滑雪吗可以？", "可以这儿吗滑雪？", "这儿吗滑雪可以？"], "可以 + verb + 吗."),
        M("Complete: 因为这儿很少下雪，所以___滑雪。", "不能", ["可以", "喜欢", "常常"], "Rare snow means no skiing."),
        M("Complete: 因为冬天下大雪，所以___滑雪。", "可以", ["不能", "不喜欢", "很少"], "Heavy snow means skiing."),
        F("夏天___游泳。 (can)", "可以", PART, "可以 is can.", tr="In summer we can swim."),
        F("冬天___能游泳。 (cannot)", "不", PART, "不能 is cannot.", tr="In winter we cannot swim."),
        F("这儿可以滑___吗？", "雪", PART, "滑雪 is to ski.", tr="Can we ski here?"),
        F("因为这儿很少下雪，所以不___滑雪。", "能", PART, "不能 is cannot.", tr="Because it rarely snows here, we cannot ski."),
    ],
)

# ---------------------------------------------------------------------------- 111
L111 = lesson(
    "Temperature and climate",
    "温度 · 气温 · 度 · 零下 · 摄氏 · 华氏 · 气候",
    requires=[],
    cards=[
        card("Degrees",
             "温度 (wēndù) and 气温 (qìwēn, air temperature) are “temperature”. 度 (dù) is “degree”: 二十度 is 20 degrees. "
             "Below zero is 零下 (língxià): 零下五度 is “minus 5”. Two scales: 摄氏 (shèshì) is Celsius and 华氏 (huáshì) is Fahrenheit. "
             "气候 (qìhòu) is climate, the weather over many years, and 天气 is the weather of a day.",
             tables=[wtable([("温度", "wen1du4", "temperature"), ("气温", "qi4wen1", "air temperature"), ("度", "du4", "degree"), ("零下", "ling2xia4", "below zero"),
                             ("摄氏", "she4shi4", "Celsius"), ("华氏", "hua2shi4", "Fahrenheit"), ("气候", "qi4hou4", "climate"), ("今天", "jin1tian1", "today")])]),
        card("Fahrenheit to Celsius",
             "Water freezes at 0 °C, which is 32 °F, and boils at 100 °C, which is 212 °F. To change Fahrenheit into Celsius, subtract 32, then multiply by 5 and divide by 9. "
             "So 68 °F is 68 − 32 = 36, times 5 is 180, divided by 9 is 20 °C. The pairs to remember: 50 °F is 10 °C, 68 °F is 20 °C, 86 °F is 30 °C and 104 °F is 40 °C.",
             tables=[table(["华氏", "摄氏"], [["华氏三十二度", "摄氏零度"], ["华氏五十度", "摄氏十度"], ["华氏六十八度", "摄氏二十度"], ["华氏八十六度", "摄氏三十度"],
                                           ["华氏二百一十二度", "摄氏一百度"]], say=[0, 1])],
             examples=[ex("今天的气温是二十度。", "jin1tian1 de5 qi4wen1 shi4 er4shi2 du4", "Today’s temperature is 20 degrees.", hl="二十度"),
                       ex("冬天的气温有时候是零下十度。", "dong1tian1 de5 qi4wen1 you3shi2hou5 shi4 ling2xia4 shi2 du4", "In winter the temperature is sometimes minus 10.", hl="零下"),
                       ex("华氏六十八度是摄氏二十度。", "hua2shi4 liu4shi2ba1 du4 shi4 she4shi4 er4shi2 du4", "68 °F is 20 °C.")]),
    ],
    exercises=[
        mean("温度", "wen1du4", "temperature", ["weather", "climate", "a season"]),
        mean("气温", "qi4wen1", "air temperature", ["climate", "a season", "weather"]),
        mean("度", "du4", "degree", ["time", "year", "weather"]),
        mean("零下", "ling2xia4", "below zero", ["above zero", "zero degrees", "freezing"]),
        mean("摄氏", "she4shi4", "Celsius", ["Fahrenheit", "a degree", "a thermometer"]),
        mean("华氏", "hua2shi4", "Fahrenheit", ["Celsius", "a degree", "a season"]),
        mean("气候", "qi4hou4", "climate", ["weather today", "a season", "temperature"]),
        rd("气温", "qi4wen1", ["qi4wen2", "qi2wen1", "qi4wen4"]),
        rd("零下", "ling2xia4", ["ling2xia2", "ling1xia4", "ling3xia4"]),
        M("What is 零下五度?", "minus 5 degrees", ["5 degrees", "50 degrees", "15 degrees"], "零下 is below zero."),
        M("What is the difference between 天气 and 气候?", "天气 is the day’s weather; 气候 is long-term", ["They are the same", "天气 is long-term", "气候 is only wind"], "Climate is the long run."),
        M("32 °F in Celsius is…", "0 °C", ["32 °C", "10 °C", "−32 °C"], "Water freezes at 32 °F."),
        M("212 °F in Celsius is…", "100 °C", ["212 °C", "180 °C", "50 °C"], "Water boils at 212 °F."),
        M("50 °F in Celsius is…", "10 °C", ["18 °C", "5 °C", "30 °C"], "(50 − 32) × 5 ÷ 9 = 10."),
        M("68 °F in Celsius is…", "20 °C", ["36 °C", "30 °C", "15 °C"], "(68 − 32) × 5 ÷ 9 = 20."),
        M("86 °F in Celsius is…", "30 °C", ["54 °C", "20 °C", "40 °C"], "(86 − 32) × 5 ÷ 9 = 30."),
        M("104 °F in Celsius is…", "40 °C", ["72 °C", "30 °C", "50 °C"], "(104 − 32) × 5 ÷ 9 = 40."),
        M("41 °F in Celsius is…", "5 °C", ["9 °C", "10 °C", "0 °C"], "(41 − 32) × 5 ÷ 9 = 5."),
        M("Which is colder?", "5 °C", ["50 °F", "68 °F", "86 °F"], "5 °C is 41 °F, the coldest."),
        F("今天的气___是二十度。", "温", PART, "气温 is air temperature.", tr="Today’s temperature is 20 degrees."),
        F("冬天的气温有时候是零___十度。", "下", PART, "零下 is below zero.", tr="In winter the temperature is sometimes minus 10."),
        F("华氏六十八度是摄氏二十___。", "度", PART, "度 is degree.", tr="68 °F is 20 °C."),
    ],
)

# ---------------------------------------------------------------------------- 112
L112 = lesson(
    "The same as: 跟 … 一样",
    "A 跟 B 一样 · 一样冷 · 不一样",
    requires=[],
    cards=[
        card("A is the same as B",
             "跟 (gēn) here means “with”, and 一样 (yíyàng) means “same”. A 跟 B 一样 says “A is the same as B”. To say in what way, add an adjective: A 跟 B 一样冷, “A is as cold as B”. "
             "For “different”, use 不一样: A 跟 B 不一样. Note that 一 changes to yí before the fourth tone in 一样.",
             tables=[table(["Pattern", "Meaning"],
                           [["北京跟上海一样。", "Beijing is the same as Shanghai."], ["北京跟上海一样大。", "Beijing is as big as Shanghai."], ["北京跟上海不一样。", "Beijing is different from Shanghai."],
                            ["我老家的冬天跟这儿一样冷。", "Winters in my hometown are as cold as here."]], say=[0])]),
        card("Same, or not the same",
             "The negative puts 不 before 一样 only: 不一样 (bù yíyàng). The tones are written as they are said: 不 is bù and 一 is yí.",
             examples=[ex("我的老家跟这儿一样热。", "wo3 de5 lao3jia1 gen1 zhe4r5 yi2yang4 re4", "My hometown is as hot as here.", hl="一样"),
                       ex("夏天的天气跟冬天的天气不一样。", "xia4tian1 de5 tian1qi4 gen1 dong1tian1 de5 tian1qi4 bu4 yi2yang4", "The weather in summer is different from the weather in winter.", hl="不一样"),
                       ex("你的手机跟我的手机一样吗？", "ni3 de5 shou3ji1 gen1 wo3 de5 shou3ji1 yi2yang4 ma5", "Is your phone the same as mine?")]),
    ],
    exercises=[
        mean("一样", "yi2yang4", "same", ["different", "a kind", "like"]),
        mean("不一样", "bu4 yi2yang4", "different", ["the same", "very good", "not good"]),
        mean("跟", "gen1", "with, and", ["after", "from", "at"]),
        rd("一样", "yi2yang4", ["yi4yang4", "yi2yang2", "yi1yang4"]),
        M("What does 北京跟上海一样大 say?", "Beijing is as big as Shanghai.", ["Beijing is bigger than Shanghai.", "Beijing is different from Shanghai.", "Beijing and Shanghai are both small."], "A 跟 B 一样 + adjective."),
        M("What does 北京跟上海不一样 say?", "Beijing is different from Shanghai.", ["Beijing is the same as Shanghai.", "Beijing is not Shanghai.", "Beijing is far from Shanghai."], "不一样 is different."),
        M("How do you say “My hometown is as hot as here”?", "我的老家跟这儿一样热。", ["我的老家一样跟这儿热。", "我的老家跟这儿热一样。", "我的老家这儿跟一样热。"], "A 跟 B 一样 + adjective."),
        M("Where does 不 go?", "Before 一样", ["Before 跟", "After 一样", "Before the adjective"], "跟 B 不一样."),
        M("What does 你的手机跟我的手机一样吗？ ask?", "Is your phone the same as mine?", ["Whose phone is it?", "Do you have a phone?", "Is my phone new?"], "跟 … 一样 asks about sameness."),
        M("How do you say “Summer weather is different from winter weather”?", "夏天的天气跟冬天的天气不一样。", ["夏天的天气不一样跟冬天的天气。", "夏天的天气跟冬天的天气一样不。", "夏天的天气跟不一样冬天的天气。"], "不一样 after the second part."),
        F("北京跟上海___样大。", "一", PART, "一样 is same.", tr="Beijing is as big as Shanghai."),
        F("我的老家___这儿一样热。", "跟", PART, "跟 … 一样.", tr="My hometown is as hot as here."),
        F("夏天跟冬天不一___。", "样", PART, "不一样.", tr="Summer is different from winter."),
        F("夏天的天气跟冬天的天气___一样。", "不", PART, "不一样.", tr="The weather in summer is different from winter."),
    ],
)

# ---------------------------------------------------------------------------- 113
L113 = lesson(
    "Comparing with 比",
    "A 比 B + adjective · 比 … 冷一点儿 · 比 … 冷多了",
    requires=[],
    cards=[
        card("A is more … than B",
             "比 (bǐ) means “compared with”. Put it between the two things, and put the adjective last: A 比 B + adjective. 北京比上海冷 is “Beijing is colder than Shanghai”. "
             "Do not use 很 before the adjective in this pattern. To say how much more, add 一点儿 (yìdiǎnr, a little) or 多了 (duō le, much more) after the adjective.",
             tables=[table(["Pattern", "Meaning"],
                           [["北京比上海冷。", "Beijing is colder than Shanghai."], ["今年比去年热一点儿。", "This year is a little hotter than last year."], ["冬天比秋天冷多了。", "Winter is much colder than autumn."],
                            ["我比我姐姐高。", "I am taller than my older sister."]], say=[0])]),
        card("Not as much as",
             "To say “not more than”, put 不 before 比: A 不比 B + adjective. 我不比他高 means “I am not taller than him”. It simply denies the comparison. "
             "A longer way to say that A is less is 没有 (next lesson).",
             examples=[ex("夏天比春天热。", "xia4tian1 bi3 chun1tian1 re4", "Summer is hotter than spring.", hl="比"),
                       ex("这儿比那儿冷一点儿。", "zhe4r5 bi3 na4r5 leng3 yi4dian3r5", "It is a little colder here than there.", hl="一点儿"),
                       ex("冬天比秋天冷多了。", "dong1tian1 bi3 qiu1tian1 leng3 duo1 le5", "Winter is much colder than autumn.", hl="多了"),
                       ex("你比我高吗？", "ni3 bi3 wo3 gao1 ma5", "Are you taller than me?")]),
    ],
    exercises=[
        mean("比", "bi3", "compared with, than", ["same as", "with", "not"]),
        mean("一点儿", "yi4dian3r5", "a little", ["much", "a lot", "very"]),
        mean("多了", "duo1 le5", "much more", ["a little", "less", "many"]),
        rd("比", "bi3", ["bi1", "bi2", "pei3"]),
        M("What does 北京比上海冷 say?", "Beijing is colder than Shanghai.", ["Shanghai is colder than Beijing.", "Beijing is as cold as Shanghai.", "Beijing is very cold."], "A 比 B + adjective."),
        M("Where does the adjective go?", "After B", ["Before 比", "After 比 and before B", "At the start"], "A 比 B + adjective."),
        M("Can you say 北京比上海很冷?", "No", ["Yes", "Only in writing", "Only in questions"], "No 很 in the 比 pattern."),
        M("What does 冬天比秋天冷多了 say?", "Winter is much colder than autumn.", ["Winter is a little colder than autumn.", "Winter is as cold as autumn.", "Autumn is colder than winter."], "多了 is much more."),
        M("What does 这儿比那儿冷一点儿 say?", "It is a little colder here than there.", ["It is much colder here.", "It is warmer here.", "They are the same."], "一点儿 is a little."),
        M("How do you say “I am taller than my sister”?", "我比我姐姐高。", ["我高比我姐姐。", "我比高我姐姐。", "我比我姐姐很高。"], "A 比 B + adjective."),
        M("How do you say “I am not taller than him”?", "我不比他高。", ["我比他不高。", "我比不他高。", "我没比他高。"], "不 before 比."),
        F("北京___上海冷。", "比", PART, "比 is than.", tr="Beijing is colder than Shanghai."),
        F("这儿比那儿冷一点___。", "儿", PART, "一点儿 is a little.", tr="It is a little colder here than there."),
        F("冬天比秋天冷___了。", "多", PART, "多了 is much more.", tr="Winter is much colder than autumn."),
        F("我不___他高。", "比", PART, "不比.", tr="I am not taller than him."),
    ],
)

# ---------------------------------------------------------------------------- 114
L114 = lesson(
    "Not as … as: 没有 … 这么 / 那么",
    "上海没有北京这么冷 · 北京有上海那么热吗？",
    requires=[],
    cards=[
        card("没有 for “not as”",
             "没有 (méiyǒu) is the opposite of 比 for “less”. A 没有 B + adjective says “A is not as … as B”. 上海没有北京冷 is “Shanghai is not as cold as Beijing”. "
             "Add 这么 (zhème) or 那么 (nàme), “so, that”, before the adjective to give it force: 上海没有北京这么冷, with 这么 for something near the speaker and 那么 for something far.",
             tables=[table(["Pattern", "Meaning"],
                           [["上海没有北京冷。", "Shanghai is not as cold as Beijing."], ["上海没有北京这么冷。", "Shanghai is not as cold as Beijing (that cold)."],
                            ["夏天没有冬天那么冷。", "Summer is not as cold as winter."]], say=[0])]),
        card("Asking with 有",
             "A positive question uses 有 (not 没有): 北京有上海那么热吗？ means “Is Beijing as hot as Shanghai?”, and the speaker often thinks the answer is no. "
             "You can also ask 有没有: 北京有没有上海那么热？",
             examples=[ex("我老家没有这儿这么热。", "wo3 lao3jia1 mei2you3 zhe4r5 zhe4me5 re4", "My hometown is not as hot as here.", hl="没有"),
                       ex("冬天没有秋天那么舒服。", "dong1tian1 mei2you3 qiu1tian1 na4me5 shu1fu5", "Winter is not as comfortable as autumn."),
                       ex("北京有上海那么热吗？", "bei3jing1 you3 shang4hai3 na4me5 re4 ma5", "Is Beijing as hot as Shanghai?", hl="有"),
                       ex("你们那儿有没有这儿这么冷？", "ni3men5 na4r5 you3 mei2 you3 zhe4r5 zhe4me5 leng3", "Is it as cold where you are as it is here?")]),
    ],
    exercises=[
        mean("没有", "mei2you3", "not as … as, does not have", ["has", "also has", "is the same"]),
        mean("这么", "zhe4me5", "so, this (much)", ["that much", "a little", "not"]),
        mean("那么", "na4me5", "so, that (much)", ["this much", "a little", "not"]),
        rd("这么", "zhe4me5", ["zhe4me4", "zhe3me5", "zhe2me5"]),
        M("What does 上海没有北京冷 say?", "Shanghai is not as cold as Beijing.", ["Shanghai is colder than Beijing.", "Shanghai has no Beijing.", "Shanghai is as cold as Beijing."], "A 没有 B + adjective."),
        M("Which is the opposite of 比 for “less”?", "没有", ["不比", "一样", "也"], "没有 means not as … as."),
        M("What does 夏天没有冬天那么冷 say?", "Summer is not as cold as winter.", ["Summer is colder than winter.", "Summer is as cold as winter.", "Summer is very cold."], "没有 … 那么."),
        M("What does 北京有上海那么热吗？ ask?", "Is Beijing as hot as Shanghai?", ["Does Beijing have Shanghai?", "Is Beijing hotter than Shanghai?", "Where is Beijing?"], "有 … 那么 asks whether it reaches that degree."),
        M("When do you use 这么?", "When the thing is near the speaker", ["When it is far", "In questions only", "In the past"], "这 is near; 那 is far."),
        M("How do you say “My hometown is not as hot as here”?", "我老家没有这儿这么热。", ["我老家这儿没有这么热。", "我老家不有这儿这么热。", "我老家没这儿有这么热。"], "A 没有 B 这么 adjective."),
        M("How do you ask “Is it as cold there as here?”", "那儿有没有这儿这么冷？", ["那儿没有有这儿这么冷？", "那儿有这儿没有这么冷？", "那儿有没有冷这儿这么？"], "有没有 + B + 这么 + adjective."),
        F("上海___有北京冷。", "没", PART, "没有 is not as.", tr="Shanghai is not as cold as Beijing."),
        F("夏天没有冬天___么冷。", "那", PART, "那么 is that.", tr="Summer is not as cold as winter."),
        F("我老家没有这儿这___热。", "么", PART, "这么 is so.", tr="My hometown is not as hot as here."),
        F("北京___上海那么热吗？ (positive question)", "有", PART, "有 … 那么.", tr="Is Beijing as hot as Shanghai?"),
    ],
)

# ---------------------------------------------------------------------------- 115
L115 = lesson(
    "But: 可是",
    "冬天很冷，可是我喜欢冬天",
    requires=[],
    cards=[
        card("可是 joins two ideas",
             "可是 (kěshì) means “but” and starts the second clause: 冬天很冷，可是我喜欢冬天. It does not need a partner like 因为 … 所以 …. "
             "Use it when the second part goes against what you would expect from the first. It is spoken and written equally, and 但是 (dànshì) means the same.",
             tables=[table(["Pattern", "Meaning"],
                           [["夏天很热，可是我喜欢夏天。", "Summer is hot, but I like summer."], ["他是南方人，可是他不喜欢热。", "He is a southerner, but he does not like heat."],
                            ["这儿不大，可是人很多。", "This place is not big, but it has many people."]], say=[0])]),
        card("Opposite ideas",
             "A 可是 sentence sets two things against each other. If the second part just adds to the first, use 也 or 和 instead.",
             examples=[ex("我老家不大，可是很舒服。", "wo3 lao3jia1 bu2 da4, ke3shi4 hen3 shu1fu5", "My hometown is not big, but it is very comfortable.", hl="可是"),
                       ex("冬天下大雪，可是我不能滑雪。", "dong1tian1 xia4 da4 xue3, ke3shi4 wo3 bu4 neng2 hua2xue3", "It snows heavily in winter, but I cannot ski."),
                       ex("他的中文很好，可是他不是中国人。", "ta1 de5 zhong1wen2 hen3 hao3, ke3shi4 ta1 bu2 shi4 zhong1guo2 ren2", "His Chinese is very good, but he is not Chinese.")]),
    ],
    exercises=[
        mean("可是", "ke3shi4", "but", ["so", "because", "also"]),
        rd("可是", "ke3shi4", ["ke3shi2", "ke4shi4", "ke2shi4"]),
        M("What does 冬天很冷，可是我喜欢冬天 say?", "Winter is cold, but I like winter.", ["Winter is cold, so I like winter.", "Winter is cold because I like it.", "I like winter, and it is cold."], "可是 is but."),
        M("Where does 可是 go?", "At the start of the second clause", ["At the end", "After the verb", "Before the subject of the first clause"], "可是 + second idea."),
        M("Does 可是 need a partner?", "No", ["Yes, 因为", "Yes, 所以", "Yes, 也"], "可是 stands alone."),
        M("Which word means the same as 可是?", "但是", ["所以", "因为", "还是"], "但是 also means but."),
        M("Which sentence is natural?", "夏天很热，可是我喜欢夏天。", ["夏天很热，所以我喜欢夏天。", "夏天很热，可是夏天。", "可是夏天，很热我喜欢。"], "热 and 喜欢 contrast."),
        M("What does 这儿不大，可是人很多 say?", "This place is not big, but it has many people.", ["This place is big and has many people.", "This place is not big, so it has few people.", "This place has no people."], "可是 contrasts."),
        F("夏天很热，___我喜欢夏天。", "可是", PART, "可是 is but.", tr="Summer is hot, but I like summer."),
        F("他的中文很好，可___他不是中国人。", "是", PART, "可是 is but.", tr="His Chinese is very good, but he is not Chinese."),
        F("我老家不大，___是很舒服。", "可", PART, "可是 is but.", tr="My hometown is not big, but it is very comfortable."),
        F("冬天下大雪，可是我不___滑雪。", "能", PART, "不能 is cannot.", tr="It snows heavily in winter, but I cannot ski."),
    ],
)

# ---------------------------------------------------------------------------- 116
L116 = lesson(
    "Good to …: 好 + verb",
    "好吃 · 好看 · 好听 · 好玩 · 好用",
    requires=[],
    cards=[
        card("好 before a verb",
             "好 (hǎo) before certain verbs makes an adjective meaning “good to …”, “pleasant to …”: 好吃 (hǎochī) is “tasty”, 好看 (hǎokàn) “nice to look at”, 好听 (hǎotīng) “nice to hear”, "
             "好玩 (hǎowán) “fun” and 好用 (hǎoyòng) “easy to use”. These are adjectives, so 很 can go in front: 很好吃. "
             "Do not confuse these with 天气好, “the weather is good”, where 好 is just an adjective on its own.",
             tables=[wtable([("好吃", "hao3chi1", "tasty"), ("好看", "hao3kan4", "nice-looking"), ("好听", "hao3ting1", "nice to listen to"), ("好玩", "hao3wan2", "fun"),
                             ("好用", "hao3yong4", "easy to use"), ("好学", "hao3xue2", "easy to learn")])]),
        card("In sentences",
             "Say what the thing is, then the 好 word with 很.",
             examples=[ex("这个饺子很好吃。", "zhe4 ge4 jiao3zi5 hen3 hao3chi1", "These dumplings are very tasty.", hl="好吃"),
                       ex("这个城市很好玩。", "zhe4 ge4 cheng2shi4 hen3 hao3wan2", "This city is a lot of fun.", hl="好玩"),
                       ex("春天的天气很好，花很好看。", "chun1tian1 de5 tian1qi4 hen3 hao3, hua1 hen3 hao3kan4", "The weather in spring is nice and the flowers are pretty."),
                       ex("这个手机好用吗？", "zhe4 ge4 shou3ji1 hao3yong4 ma5", "Is this phone easy to use?"),
                       ex("这首歌很好听。", "zhe4 shou3 ge1 hen3 hao3ting1", "This song is nice to listen to.")]),
    ],
    exercises=[
        mean("好吃", "hao3chi1", "tasty", ["to eat well", "very much", "hungry"]),
        mean("好看", "hao3kan4", "nice-looking", ["to read well", "to watch a lot", "good to hear"]),
        mean("好听", "hao3ting1", "nice to listen to", ["good to eat", "nice-looking", "fun"]),
        mean("好玩", "hao3wan2", "fun", ["tasty", "nice-looking", "easy to use"]),
        mean("好用", "hao3yong4", "easy to use", ["fun", "tasty", "nice-looking"]),
        mean("好学", "hao3xue2", "easy to learn", ["to study well", "fun", "not hard"]),
        rd("好听", "hao3ting1", ["hao3ting2", "hao3ting4", "hao2ting1"]),
        rd("好玩", "hao3wan2", ["hao3wan1", "hao3wan4", "hao4wan2"]),
        M("Can 很 go before 好吃?", "Yes", ["No", "Only before 好看", "Only in questions"], "好吃 is an adjective."),
        M("What does 这个城市很好玩 say?", "This city is a lot of fun.", ["This city is good at playing.", "This city has a game.", "This city is far."], "好玩 is fun."),
        M("What does 好看 describe?", "Something nice to look at", ["Something nice to eat", "Something nice to hear", "Something easy to use"], "看 is to look."),
        M("How do you say “These dumplings are very tasty”?", "这个饺子很好吃。", ["这个饺子好很吃。", "这个很饺子好吃。", "这个饺子吃很好。"], "很 + 好吃."),
        M("How do you ask “Is this phone easy to use?”", "这个手机好用吗？", ["这个手机吗好用？", "这个好用手机吗？", "这个手机用好吗？"], "好用 + 吗."),
        F("这个饺子很好___。", "吃", PART, "好吃 is tasty.", tr="These dumplings are very tasty."),
        F("这个城市很好___。", "玩", PART, "好玩 is fun.", tr="This city is a lot of fun."),
        F("春天的花很好___。", "看", PART, "好看 is pretty.", tr="The flowers in spring are pretty."),
        F("这首歌很好___。", "听", PART, "好听 is nice to listen to.", tr="This song is nice to listen to."),
    ],
)

# ---------------------------------------------------------------------------- 117
L117 = lesson(
    "Review: seasons and weather",
    "季节 · 天气 · 因为…所以 · 不…也不… · 比 · 一样 · 没有 · 可是",
    requires=[],
    cards=[
        card("What you can now do",
             "You can name the seasons, describe weather and temperature, give reasons, compare two things and contrast ideas. These questions mix them.",
             examples=[ex("我最喜欢秋天，因为秋天不冷也不热。", "wo3 zui4 xi3huan5 qiu1tian1, yin1wei4 qiu1tian1 bu4 leng3 ye3 bu2 re4", "I like autumn best because it is neither cold nor hot."),
                       ex("冬天比秋天冷多了，可是可以滑雪。", "dong1tian1 bi3 qiu1tian1 leng3 duo1 le5, ke3shi4 ke3yi3 hua2xue3", "Winter is much colder than autumn, but we can ski."),
                       ex("上海没有北京这么冷。", "shang4hai3 mei2you3 bei3jing1 zhe4me5 leng3", "Shanghai is not as cold as Beijing.")]),
    ],
    exercises=[
        mean("季节", "ji4jie2", "a season", ["a year", "a day", "a festival"]),
        mean("天气", "tian1qi4", "weather", ["a day", "air", "a season"]),
        mean("滑雪", "hua2xue3", "to ski", ["to swim", "to snow", "to skate"]),
        mean("因为", "yin1wei4", "because", ["so", "but", "or"]),
        mean("可是", "ke3shi4", "but", ["so", "because", "also"]),
        mean("一样", "yi2yang4", "same", ["different", "a kind", "like"]),
        rd("气温", "qi4wen1", ["qi4wen2", "qi2wen1", "qi4wen4"]),
        M("Which means “Winter is colder than autumn”?", "冬天比秋天冷。", ["冬天秋天比冷。", "冬天比冷秋天。", "比冬天秋天冷。"], "A 比 B + adjective."),
        M("Which means “Shanghai is not as cold as Beijing”?", "上海没有北京冷。", ["上海比北京没有冷。", "上海有没北京冷。", "上海不有北京冷。"], "A 没有 B + adjective."),
        M("Which means “as big as”?", "跟 … 一样大", ["比 … 大", "没有 … 大", "不 … 也不 … 大"], "跟 … 一样."),
        M("Which means “neither cold nor hot”?", "不冷也不热", ["也冷也热", "很冷很热", "不冷不也热"], "不 A 也不 B."),
        M("Complete: 因为这儿很少下雪，___不能滑雪。", "所以", ["可是", "还是", "因为"], "所以 gives the result."),
        M("Complete: 夏天很热，___我喜欢夏天。", "可是", ["所以", "因为", "还是"], "The two ideas contrast."),
        M("68 °F in Celsius is…", "20 °C", ["36 °C", "30 °C", "15 °C"], "(68 − 32) × 5 ÷ 9 = 20."),
        M("What does 好吃 mean?", "tasty", ["to eat well", "very hungry", "much food"], "好 + 吃."),
        F("我最喜欢秋天，因为秋天不冷___不热。", "也", PART, "不 A 也不 B.", tr="I like autumn best because it is neither cold nor hot."),
        F("冬天___秋天冷多了。", "比", PART, "比 is than.", tr="Winter is much colder than autumn."),
        F("上海没有北京这___冷。", "么", PART, "这么 is so.", tr="Shanghai is not as cold as Beijing."),
    ],
)

UNIT = unit("第五课 Seasons and weather", [L103, L104, L105, L106, L107, L108, L109, L110, L111, L112, L113, L114, L115, L116, L117])
