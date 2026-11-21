"""Unit 7: age, numbers and sounds (lessons 59-67): asking and telling age, 了 and 吧, 多 after numbers,
military numbers, lucky numbers and number scripts, sound pairs, the ü syllables, pistol words and a review.
Original text; the scope follows DLIFLC Chinese Basic Program Unit 1 Lesson 3 (Family), Presentation 3,
the pronunciation reviews and the area study on Chinese numerals."""
from dsl_zh import *


# ---------------------------------------------------------------------------- 59
L59 = lesson(
    "Asking and telling age",
    "你今年多大？ 您多大年纪了？ 你几岁了？",
    requires=[],
    cards=[
        card("Three ways to ask, by age",
             "Chinese has a different way of asking depending on who you ask. For a child under about ten, ask 你几岁了？, using 几 because the answer is a small number. "
             "For anyone older than that, an adult or a classmate, ask 你今年多大？. For an older person, about fifty or above, ask more respectfully: 您今年多大年纪了？ "
             "今年 is “this year”, 多大 literally “how big”, and 年纪 and 岁数 both mean age.",
             tables=[wtable([("你几岁了？", "ni3 ji3 sui4 le5", "How old are you? (to a child)"), ("你今年多大？", "ni3 jin1nian2 duo1 da4", "How old are you? (to an adult or peer)"),
                             ("您今年多大年纪了？", "nin2 jin1nian2 duo1 da4 nian2ji4 le5", "How old are you? (to an older person)"),
                             ("今年", "jin1nian2", "this year"), ("年", "nian2", "a year"), ("岁", "sui4", "years old"), ("年纪", "nian2ji4", "age"), ("小朋友", "xiao3peng2you5", "a child (“little friend”)")])]),
        card("Telling your age",
             "Say 我今年 and the number. 岁 comes straight after the number and means “years old”. With a two-digit number you may leave 岁 out: 我今年二十五. "
             "With a single digit you keep it: 我今年八岁.",
             examples=[ex("小朋友，你几岁了？ 我六岁。", "xiao3peng2you5, ni3 ji3 sui4 le5? wo3 liu4 sui4", "Little one, how old are you? I am six."),
                       ex("你今年多大？ 我今年二十五。", "ni3 jin1nian2 duo1 da4? wo3 jin1nian2 er4shi2wu3", "How old are you? I am twenty-five."),
                       ex("您今年多大年纪了？ 我今年六十九了。", "nin2 jin1nian2 duo1 da4 nian2ji4 le5? wo3 jin1nian2 liu4shi2jiu3 le5", "How old are you? I am sixty-nine."),
                       ex("我孙子八岁，外孙女五岁。", "wo3 sun1zi5 ba1 sui4, wai4sun1nv3 wu3 sui4", "My grandson is eight, and my granddaughter is five.")]),
    ],
    exercises=[
        mean("岁", "sui4", "years old", ["a year", "this year", "age"]),
        mean("今年", "jin1nian2", "this year", ["a year", "years old", "age"]),
        mean("年纪", "nian2ji4", "age", ["a year", "years old", "this year"]),
        mean("小朋友", "xiao3peng2you5", "a child (“little friend”)", ["an older man", "a doctor", "a classmate"]),
        rd("岁", "sui4", ["sui1", "sui2", "sui3"]),
        rd("今年", "jin1nian2", ["jin1nian4", "jin4nian2", "jin1nian1"]),
        rd("年纪", "nian2ji4", ["nian4ji4", "nian2ji2", "nian2ji1"]),
        M("Which question do you ask a five-year-old?", "你几岁了？", ["您今年多大年纪了？", "你今年多大年纪？", "你多少岁了吗？"], "几岁 is for children under about ten."),
        M("Which question do you ask a classmate?", "你今年多大？", ["你几岁了？", "您今年多大年纪了？", "你今年几大？"], "多大 is for adults and peers."),
        M("Which question do you ask a grandfather?", "您今年多大年纪了？", ["你几岁了？", "你今年多大？", "你多大年纪吗？"], "多大年纪 with 您 is the respectful form."),
        M("How do you say “I am eight” with a single digit?", "我今年八岁。", ["我今年八。", "我今年岁八。", "我八今年岁。"], "A single digit needs 岁."),
        M("Which is also correct for twenty-five?", "我今年二十五。", ["我今年二十五个。", "我二十五今年。", "我今年二五。"], "岁 can be left out after a two-digit number."),
        F("小朋友，你___岁了？", "几", ["多", "什么", "谁"], "几岁 is for a child.", tr="Little one, how old are you?"),
        F("你今年___大？", "多", ["几", "什么", "谁"], "多大 asks the age of an adult.", tr="How old are you?"),
        F("我今年六___。", "岁", ["个", "口", "位"], "岁 after a single digit.", tr="I am six."),
        F("您今年多大___了？", "年纪", ["岁数的", "学生", "孩子"], "多大年纪 is the polite question.", tr="How old are you?"),
    ],
)

# ---------------------------------------------------------------------------- 60
L60 = lesson(
    "The particles 了 and 吧",
    "您多大年纪了？ 你是中国人吧？",
    requires=[],
    cards=[
        card("了 softens a sentence",
             "Put 了 on the end of an age question or answer and it sounds softer and more polite: 你今年多大了？ is gentler than 你今年多大？ "
             "The meaning is the same in English. 了 has other jobs too, such as showing that something has changed or finished, and you will meet them later. For now it softens questions and answers about age.",
             examples=[ex("您多大年纪了？", "nin2 duo1 da4 nian2ji4 le5", "How old are you? (soft and polite)", hl="了"),
                       ex("我今年二十五了。", "wo3 jin1nian2 er4shi2wu3 le5", "I am twenty-five.", hl="了"),
                       ex("他们几岁了？ 他们八岁了。", "ta1men5 ji3 sui4 le5? ta1men5 ba1 sui4 le5", "How old are they? They are eight.")]),
        card("吧 asks for confirmation",
             "吧 on the end of a statement turns it into a question that expects the answer “yes”: you think you know, and you want to check. "
             "你是中国人吧？ is “You are Chinese, right?” A positive answer is often 对. Compare it with 吗, which is a plain open question.",
             tables=[wtable([("你是中国人吧？", "ni3 shi4 Zhong1guo2 ren2 ba5", "You are Chinese, right?"), ("他是你哥哥吧？", "ta1 shi4 ni3 ge1ge5 ba5", "He is your older brother, right?"),
                             ("你们教官是少校吧？", "ni3men5 jiao4guan1 shi4 shao4xiao4 ba5", "Your instructor is a major, right?"), ("你是中国人吗？", "ni3 shi4 Zhong1guo2 ren2 ma5", "Are you Chinese? (open question)")]),
                     wtable([("吗", "ma5", "an open yes/no question"), ("吧", "ba5", "“right?”, expects yes"), ("呢", "ne5", "“and you?”, a follow-up"), ("了", "le5", "softens an age sentence")],
                            headers=("Particle", "Pinyin", "Use"))]),
        card("A quick example",
             "Answering a 吧 question is easy: confirm with 对 or correct it.",
             examples=[ex("你妈妈是韩国人吧？ 对，我妈妈是韩国人。", "ni3 ma1ma5 shi4 Han2guo2 ren2 ba5? dui4, wo3 ma1ma5 shi4 Han2guo2 ren2", "Your mother is Korean, right? Yes, she is."),
                       ex("他们都有孩子了吧？ 有。", "ta1men5 dou1 you3 hai2zi5 le5 ba5? you3", "They all have children by now, right? Yes.")]),
    ],
    exercises=[
        mean("吧", "ba5", "“right?”, expects yes", ["an open yes/no question", "“and you?”", "very"]),
        rd("吧", "ba5", ["ba2", "ba4", "bu5"]),
        M("What does 了 do in 您多大年纪了？", "Makes it softer and more polite", ["Makes it past tense", "Makes it negative", "Makes it a question"], "了 softens the question."),
        M("What does 吧 do?", "Asks for confirmation of what you assume", ["Asks “and you?”", "Means “not”", "Makes a plural"], "吧 expects yes."),
        M("What does 你是中国人吧？ mean?", "You are Chinese, right?", ["Are you Chinese?", "Who is Chinese?", "I am Chinese."], "吧 expects the answer yes."),
        M("What is the difference between 吗 and 吧?", "吗 is an open question; 吧 expects yes", ["吧 is polite; 吗 is rude", "They mean the same", "吗 expects yes"], "吗 asks openly; 吧 checks an assumption."),
        M("A good reply to 他是你哥哥吧？ when it is true is…", "对，他是我哥哥。", ["不客气。", "他是什么。", "没有。"], "对 confirms."),
        M("Which question is softest?", "你今年多大了？", ["你今年多大？", "你多大今年？", "你今年多大吧？"], "了 softens."),
        F("你是中国人___？ (you assume yes)", "吧", ["什么", "们", "的"], "吧 confirms an assumption.", tr="You are Chinese, right?"),
        F("你们都有孩子了___？ (you assume yes)", "吧", ["什么", "们", "的"], "吧 at the end.", tr="You all have children by now, right?"),
        F("您今年多大年纪___？ (soft)", "了", ["什么", "们", "谁"], "了 softens.", tr="How old are you?"),
        F("我今年二十五___。 (soft)", "了", ["什么", "们", "谁"], "了 at the end.", tr="I am twenty-five."),
        M("Which particle asks the follow-up “and you?”", "呢", ["吧", "了", "吗"], "你呢."),
        M("Which sentence is a plain open question?", "你是老师吗？", ["你是老师吧？", "你是老师了？", "你是老师呢？"], "吗 asks openly."),
    ],
)

# ---------------------------------------------------------------------------- 61
L61 = lesson(
    "Round numbers and 多",
    "四十多岁 · 一百 · 两千 · 一万",
    requires=[],
    cards=[
        card("Hundreds, thousands and ten thousands",
             "百, 千 and 万 are 100, 1,000 and 10,000. They work like 十: 三百 is 300, 四千 is 4,000, 五万 is 50,000. "
             "For 100, 1,000 and 10,000 you say the 一 first: 一百, 一千, 一万. For 200, 2,000 and 20,000 you normally use 两: 两百, 两千, 两万. "
             "The 一 in 一百 and 一千 is said yì, and in 一万 it is said yí.",
             tables=[wtable([("百", "bai3", "hundred"), ("千", "qian1", "thousand"), ("万", "wan4", "ten thousand"), ("一百", "yi4bai3", "100"), ("三百", "san1bai3", "300"),
                             ("两百", "liang3bai3", "200"), ("一千", "yi4qian1", "1,000"), ("两千", "liang3qian1", "2,000"), ("一万", "yi2wan4", "10,000")])]),
        card("“More than…”: 多 after the number",
             "多 after a round number means “and a bit more”, so 四十多 is “forty-odd”, more than forty. It goes after the 十, 百, 千 or 万, and then comes the measure word and the noun: "
             "三十多个学生 is “more than thirty students”. It is a rough number, so it fits ages, crowds and sizes.",
             examples=[ex("我孩子都四十多了。", "wo3 hai2zi5 dou1 si4shi2 duo1 le5", "Even my children are over forty.", hl="四十多"),
                       ex("我们学校有一千多个学生。", "wo3men5 xue2xiao4 you3 yi4qian1 duo1 ge4 xue2sheng5", "Our school has more than a thousand students.", hl="一千多"),
                       ex("中文系有十多位老师。", "Zhong1wen2 xi4 you3 shi2 duo1 wei4 lao3shi1", "The Chinese department has over ten teachers.", hl="十多"),
                       ex("我父母今年都六十多了。", "wo3 fu4mu3 jin1nian2 dou1 liu4shi2 duo1 le5", "My parents are both in their sixties now.")]),
    ],
    exercises=[
        mean("百", "bai3", "hundred", ["thousand", "ten thousand", "ten"]),
        mean("千", "qian1", "thousand", ["hundred", "ten thousand", "ten"]),
        mean("万", "wan4", "ten thousand", ["hundred", "thousand", "million"]),
        rd("百", "bai3", ["bai1", "bai2", "bai4"]),
        rd("千", "qian1", ["qian2", "qian3", "qian4"]),
        rd("万", "wan4", ["wan1", "wan2", "wan3"]),
        M("What number is 三百?", "300", ["30", "3,000", "103"], "三 + 百."),
        M("What number is 四千?", "4,000", ["400", "40", "4,004"], "四 + 千."),
        M("How do you say 200?", "两百", ["二个百", "二十百", "两个百"], "Say 两 before 百 for 200."),
        M("What does 四十多 mean?", "More than forty", ["Exactly forty", "Fewer than forty", "Forty and one"], "多 after a round number means more."),
        M("What does 三十多个学生 mean?", "More than thirty students", ["Thirty students", "Fewer than thirty students", "Thirty-three students"], "三十多 is thirty-odd."),
        M("Where does 多 go in “more than twenty teachers”?", "二十多位老师", ["多二十位老师", "二十位多老师", "二十位老师多"], "多 comes right after the round number."),
        M("What does 我今年二十多岁 mean?", "I am in my twenties.", ["I am twenty.", "I am thirty.", "I am under twenty."], "二十多岁 is twenty-odd."),
        F("我孩子都四十___了。", "多", ["很", "也", "吗"], "四十多 is over forty.", tr="Even my children are over forty."),
        F("我们学校有一___多个学生。", "千", ["们", "吗", "呢"], "一千多个学生 is over a thousand students.", tr="Our school has over a thousand students."),
        F("中文系有二十___位老师。", "多", ["很", "也", "吗"], "二十多位 is over twenty.", tr="The Chinese department has over twenty teachers."),
    ],
)

# ---------------------------------------------------------------------------- 62
register("洞", "dong4", "military digit")
register("幺", "yao1", "military digit")
register("拐", "guai3", "military digit")
register("勾", "gou1", "military digit")
register("洞洞拐", "dong4 dong4 guai3", "military digits")
register("幺洞洞洞", "yao1 dong4 dong4 dong4", "military digits")
register("幺两三", "yao1 liang3 san1", "military digits")
register("三四六", "san1 si4 liu4", "military digits")
register("拐八勾洞", "guai3 ba1 gou1 dong4", "military digits")

L62 = lesson(
    "Military numbers",
    "洞 幺 两 三 四 五 六 拐 八 勾",
    requires=[],
    cards=[
        card("Why there are two sets of digits",
             "Many numbers sound alike, especially over a radio or a bad phone line: yī and qī, sì and shí. So the Chinese military uses its own spoken digits. "
             "Four of them are different words entirely (0 is 洞, 1 is 幺, 7 is 拐, 9 is 勾), 2 is said 两 instead of 二, and 5 is said wù instead of wǔ. "
             "3, 4, 6 and 8 are the same as usual. Taiwan's armed forces use the same system.",
             tables=[table(["Digit", "Civilian", "Pinyin", "Military", "Pinyin"],
                           [["0", "零", "[[ling2]]", "洞", "[[dong4]]"], ["1", "一", "[[yi1]]", "幺", "[[yao1]]"], ["2", "二", "[[er4]]", "两", "[[liang3]]"],
                            ["3", "三", "[[san1]]", "三", "[[san1]]"], ["4", "四", "[[si4]]", "四", "[[si4]]"], ["5", "五", "[[wu3]]", "五", "[[wu4]]"],
                            ["6", "六", "[[liu4]]", "六", "[[liu4]]"], ["7", "七", "[[qi1]]", "拐", "[[guai3]]"], ["8", "八", "[[ba1]]", "八", "[[ba1]]"],
                            ["9", "九", "[[jiu3]]", "勾", "[[gou1]]"]],
                           title="Civilian and military digits", say=[1, 3])]),
        card("Reading numbers on the radio",
             "Military digits are said one at a time, whatever the size of the number. So 1000 is not “one thousand” but “yāo dòng dòng dòng”, and 007 is “dòng dòng guǎi”. "
             "Here is how some numbers sound.",
             examples=[ex("幺两三", "yao1 liang3 san1", "1 2 3", hl="幺"),
                       ex("三四六", "san1 si4 liu4", "3 4 6 (the same as civilian digits)"),
                       ex("拐八勾洞", "guai3 ba1 gou1 dong4", "7 8 9 0"),
                       ex("幺洞洞洞", "yao1 dong4 dong4 dong4", "1000 (one, zero, zero, zero)"),
                       ex("洞洞拐", "dong4 dong4 guai3", "007")]),
    ],
    exercises=[
        M("Which military digit means 0?", "洞", ["幺", "拐", "勾"], "洞 [[dong4]] is zero."),
        M("Which military digit means 1?", "幺", ["洞", "拐", "勾"], "幺 [[yao1]] is one."),
        M("Which military digit means 7?", "拐", ["洞", "幺", "勾"], "拐 [[guai3]] is seven."),
        M("Which military digit means 9?", "勾", ["洞", "幺", "拐"], "勾 [[gou1]] is nine."),
        M("How is 2 said in the military?", "[[liang3]]", ["[[er4]]", "[[san1]]", "[[dong4]]"], "Military 2 is 两."),
        M("How is 5 said in the military?", "[[wu4]]", ["[[wu3]]", "[[wu2]]", "[[wu1]]"], "Military 5 is wù, not wǔ."),
        M("What number is 拐?", "7", ["9", "1", "0"], "拐 is seven."),
        M("What number is 勾?", "9", ["7", "1", "0"], "勾 is nine."),
        M("What number is 洞?", "0", ["1", "7", "9"], "洞 is zero."),
        M("How is 1000 said in military digits?", "幺洞洞洞", ["幺千", "一千", "幺百洞"], "Digits are read one at a time: 1, 0, 0, 0."),
        M("How is 007 said in military digits?", "洞洞拐", ["洞拐洞", "拐洞洞", "洞洞勾"], "0 0 7."),
        M("Why does the military have its own digits?", "So numbers cannot be confused on a radio", ["Because the old digits are wrong", "Because it is a secret code", "For decoration"], "Many numbers sound alike on a bad line."),
        rd("洞", "dong4", ["dong1", "dong2", "dong3"]),
        rd("拐", "guai3", ["guai1", "guai2", "guai4"]),
        rd("勾", "gou1", ["gou2", "gou3", "guo1"]),
        M("What is 幺两三 as ordinary digits?", "123", ["132", "1203", "213"], "1, 2, 3."),
    ],
)

# ---------------------------------------------------------------------------- 63
L63 = lesson(
    "Lucky numbers and number scripts",
    "6, 8, 9 and 4 · 520 · 壹 贰 叁",
    requires=[],
    cards=[
        card("Numbers that sound like other words",
             "Chinese is full of word play, and numbers join in because many words share a sound. 8 (bā) is liked because it rhymes with 发 (fā), “get rich”. "
             "6 (liù) sounds like 溜, “smooth”, and 禄, “good fortune”. 9 (jiǔ) sounds like 久, “lasting a long time”. "
             "4 (sì) sounds like 死 (sǐ), “to die”, so some buildings skip floor 4 and some people avoid it.",
             tables=[wtable([("六", "liu4", "6: sounds like 溜 “smooth”"), ("八", "ba1", "8: sounds like 发 “get rich”"), ("九", "jiu3", "9: sounds like 久 “lasting”"),
                             ("四", "si4", "4: sounds like 死 “to die”"), ("发", "fa1", "to get rich"), ("久", "jiu3", "a long time"), ("死", "si3", "to die")])]),
        card("Number messages",
             "Strings of digits are used as messages. 520, wǔ èr líng, sounds like 我爱你, “I love you”, and May 20 is treated as a day for gifts. "
             "518 sounds like 我要发, “I will get rich”, and 168 like 一路发, “prosperity all the way”.",
             tables=[wtable([("我爱你", "wo3 ai4 ni3", "I love you (520)"), ("我要发", "wo3 yao4 fa1", "I want to get rich (518)"), ("一路发", "yi2 lu4 fa1", "prosper all the way (168)")])]),
        card("Three ways to write numbers",
             "Arabic digits (阿拉伯数字) are used for calculation, signs and phone numbers. Chinese-character numbers (汉字数字), such as 一二三, are used in text. "
             "A third set, the formal capital numbers (大写数字), uses more complicated characters that are hard to alter, so they are used on cheques and in accounting to prevent fraud. "
             "Zero can be written 〇 or 零.",
             tables=[wtable([("一", "yi1", "壹 (formal) 1"), ("二", "er4", "贰 (formal) 2"), ("三", "san1", "叁 (formal) 3"), ("四", "si4", "肆 (formal) 4"), ("五", "wu3", "伍 (formal) 5"),
                             ("六", "liu4", "陆 (formal) 6"), ("七", "qi1", "柒 (formal) 7"), ("八", "ba1", "捌 (formal) 8"), ("九", "jiu3", "玖 (formal) 9"), ("十", "shi2", "拾 (formal) 10")],
                            headers=("Ordinary", "Pinyin", "Formal (written, same sound)"))]),
    ],
    exercises=[
        M("Why is 8 considered lucky?", "It sounds like 发, “get rich”", ["It looks like a house", "It sounds like 死", "It is the first number"], "八 [[ba1]] is close to 发 [[fa1]]."),
        M("Why is 4 often avoided?", "It sounds like 死, “to die”", ["It sounds like 发", "It is too small", "It is the same as 10"], "四 [[si4]] sounds like 死 [[si3]]."),
        M("What does 9 sound like?", "久, “lasting”", ["死, “to die”", "发, “get rich”", "爱, “love”"], "九 [[jiu3]] and 久 [[jiu3]] sound the same."),
        M("What does 6 sound like?", "溜, “smooth”", ["死, “to die”", "久, “lasting”", "爱, “love”"], "六 [[liu4]] sounds like 溜."),
        M("What does 520 sound like?", "我爱你, “I love you”", ["我要发", "一路发", "我是你"], "wǔ èr líng sounds like wǒ ài nǐ."),
        M("What does 518 stand for?", "我要发, “I will get rich”", ["我爱你", "一路发", "我是你"], "wǔ yāo fā."),
        M("What does 168 stand for?", "一路发, “prosper all the way”", ["我爱你", "我要发", "我是你"], "yī lù fā."),
        M("Which writing is used for calculation, signs and phone numbers?", "Arabic digits", ["Formal capital numbers", "Chinese-character numbers only", "Military digits"], "Arabic digits are used for practical things."),
        M("Why are formal capital numbers used on cheques?", "They are hard to alter", ["They are shorter", "They are older", "They are easier"], "Complicated characters prevent fraud."),
        M("Which character is the formal form of 1?", "壹", ["一", "贰", "叁"], "壹 is the formal one."),
        M("Which character is the formal form of 3?", "叁", ["三", "壹", "肆"], "叁 is the formal three."),
        M("Which character is the formal form of 8?", "捌", ["八", "柒", "玖"], "捌 is the formal eight."),
        M("Which character is the formal form of 10?", "拾", ["十", "伍", "陆"], "拾 is the formal ten."),
        rd("发", "fa1", ["fa2", "fa3", "fu1"]),
        rd("久", "jiu3", ["jiu1", "jiu2", "jiu4"]),
        rd("死", "si3", ["si1", "si2", "si4"]),
    ],
)

# ---------------------------------------------------------------------------- 64
L64 = lesson(
    "Sound pairs: z/zh, s/sh, j/zh, x/sh, r",
    "早 · 找 · 三 · 山 · 少校 · 日本",
    requires=[],
    cards=[
        card("z against zh, s against sh",
             "These pairs differ only in where the tongue is: flat against the teeth for z and s, curled back for zh and sh.",
             tables=[wtable([("早", "zao3", "morning, early"), ("找", "zhao3", "to look for"), ("宗", "zong1", "ancestor"), ("中", "zhong1", "middle"),
                             ("赞", "zan4", "to praise"), ("战", "zhan4", "war"), ("三", "san1", "three"), ("山", "shan1", "a mountain"), ("赏", "shang3", "to reward")],
                            title="z / zh and s / sh")]),
        card("j against zh, x against sh, and r",
             "j and x are made with the tongue tip down behind the lower teeth and the middle of the tongue raised, zh and sh with the tip curled back. r is a curled, buzzing sound, "
             "like a soft English “r” without rounding the lips too much.",
             tables=[wtable([("记者", "ji4zhe3", "a reporter"), ("证件", "zheng4jian4", "an ID, a certificate"), ("军装", "jun1zhuang1", "a military uniform"), ("小说", "xiao3shuo1", "a novel"),
                             ("少校", "shao4xiao4", "a major"), ("上学", "shang4xue2", "to go to school"), ("热烈", "re4lie4", "warm, enthusiastic"), ("日本", "Ri4ben3", "Japan"), ("日子", "ri4zi5", "a day, a date")],
                            title="j / zh, x / sh, r")]),
    ],
    exercises=[
        rd("早", "zao3", ["zhao3", "cao3", "sao3"], meaning="morning"),
        rd("找", "zhao3", ["zao3", "chao3", "shao3"], meaning="to look for"),
        rd("宗", "zong1", ["zhong1", "cong1", "song1"], meaning="ancestor"),
        rd("中", "zhong1", ["zong1", "chong1", "zhuang1"], meaning="middle"),
        rd("赞", "zan4", ["zhan4", "can4", "san4"], meaning="to praise"),
        rd("战", "zhan4", ["zan4", "chan4", "shan4"], meaning="war"),
        rd("三", "san1", ["shan1", "zan1", "can1"], meaning="three"),
        rd("山", "shan1", ["san1", "zhan1", "chan1"], meaning="a mountain"),
        rd("赏", "shang3", ["sang3", "zhang3", "chang3"], meaning="to reward"),
        rd("记者", "ji4zhe3", ["zhi4zhe3", "ji4ze3", "ji4zhe4"]),
        rd("军装", "jun1zhuang1", ["jun1zhuan1", "zhun1zhuang1", "jun1zhuang2"]),
        rd("小说", "xiao3shuo1", ["shao3shuo1", "xiao3suo1", "xiao3shuo2"]),
        rd("少校", "shao4xiao4", ["xiao4shao4", "sao4xiao4", "shao4shao4"]),
        rd("上学", "shang4xue2", ["shang4xue4", "xiang4xue2", "shang4xue1"]),
        rd("热烈", "re4lie4", ["le4lie4", "re4lie2", "she4lie4"]),
        rd("日本", "Ri4ben3", ["Zhi4ben3", "Ri4ben2", "Ri2ben3"]),
        M("In which word is the tongue flat against the teeth?", "三 [[san1]]", ["山 [[shan1]]", "找 [[zhao3]]", "战 [[zhan4]]"], "s is flat; sh and zh are curled."),
        M("In which word is the tongue curled back?", "山 [[shan1]]", ["三 [[san1]]", "早 [[zao3]]", "赞 [[zan4]]"], "sh is curled; s and z are flat."),
    ],
)

# ---------------------------------------------------------------------------- 65
L65 = lesson(
    "The ü syllables: yu, yue, yuan, yun",
    "鱼 语 月 远 云 运 · 选举 句子 决定",
    requires=[],
    cards=[
        card("When ü stands alone",
             "A syllable cannot start with a bare ü. The spelling rule is to write y in front and drop the dots: ü becomes yu, üe becomes yue, üan becomes yuan and ün becomes yun. "
             "Do not be fooled by the u, since these are all really ü sounds, with rounded lips. Compare yuè (月, a month) with yè (夜, night), and yún (云, a cloud) with yín (银, silver).",
             tables=[wtable([("迂", "yu1", "roundabout"), ("鱼", "yu2", "a fish"), ("语", "yu3", "language"), ("遇", "yu4", "to meet"),
                             ("月", "yue4", "a month, the moon"), ("约", "yue1", "approximately"),
                             ("冤", "yuan1", "injustice"), ("圆", "yuan2", "round"), ("远", "yuan3", "far"), ("怨", "yuan4", "to blame"),
                             ("晕", "yun1", "dizzy"), ("云", "yun2", "a cloud"), ("允", "yun3", "to permit"), ("运", "yun4", "to transport")],
                            title="With y: yu, yue, yuan, yun")]),
        card("After j, q and x",
             "After j, q and x the same ü is also written u, because j, q and x never go with a real u. Say each word with rounded lips.",
             tables=[wtable([("选举", "xuan3ju3", "an election"), ("捐献", "juan1xian4", "to donate"), ("预约", "yu4yue1", "to make an appointment"), ("句子", "ju4zi5", "a sentence"),
                             ("决定", "jue2ding4", "to decide"), ("允许", "yun3xu3", "to permit"), ("取决", "qu3jue2", "to depend on"), ("拒绝", "ju4jue2", "to refuse"),
                             ("援军", "yuan2jun1", "reinforcements"), ("预习", "yu4xi2", "to prepare before class"), ("需求", "xu1qiu2", "a need, a demand")],
                            title="ü after j, q, x and y")]),
    ],
    exercises=[
        rd("鱼", "yu2", ["yu1", "yu3", "yu4"], meaning="a fish"),
        rd("语", "yu3", ["yu1", "yu2", "yuan3"], meaning="language"),
        rd("遇", "yu4", ["yu1", "yu2", "yu3"], meaning="to meet"),
        rd("月", "yue4", ["ye4", "yue1", "yue2"], meaning="a month"),
        rd("远", "yuan3", ["yuan1", "yuan2", "yuan4"], meaning="far"),
        rd("圆", "yuan2", ["yuan1", "yuan3", "yuan4"], meaning="round"),
        rd("云", "yun2", ["yin2", "yun1", "yun3"], meaning="a cloud"),
        rd("运", "yun4", ["yun1", "yun2", "yin4"], meaning="to transport"),
        rd("选举", "xuan3ju3", ["xian3ju3", "xuan3ju4", "xuan2ju3"]),
        rd("句子", "ju4zi5", ["ju4zi3", "ju2zi5", "qu4zi5"]),
        rd("决定", "jue2ding4", ["jue2ding2", "que2ding4", "jue4ding4"]),
        rd("允许", "yun3xu3", ["yin3xu3", "yun3xu2", "yun2xu3"]),
        M("How is the ü sound written at the start of a syllable?", "With y: yu", ["With w: wu", "ü on its own", "With j: ju"], "A bare ü becomes yu."),
        M("How is ün written with no initial?", "yun", ["wun", "un", "yin"], "ün becomes yun."),
        M("How is üe written with no initial?", "yue", ["wue", "ye", "yie"], "üe becomes yue."),
        M("How is üan written with no initial?", "yuan", ["wan", "yian", "yan"], "üan becomes yuan."),
        M("How do 月 and 夜 differ?", "月 [[yue4]] has ü, 夜 [[ye4]] does not", ["Only in tone", "They are the same", "夜 has ü"], "yuè has rounded lips at the start."),
        M("Which syllable has an ü sound?", "云 [[yun2]]", ["银 [[yin2]]", "音 [[yin1]]", "英 [[ying1]]"], "yún is ü + n; yín is i + n."),
    ],
)

# ---------------------------------------------------------------------------- 66
register("手枪", "shou3qiang1", "pistol")
L66 = lesson(
    "Military words: pistols",
    "手枪 · 左轮手枪 · 自动手枪 · 五四式",
    requires=[],
    cards=[
        card("Naming pistols",
             "手 is the hand and 枪 is a firearm, so 手枪 is a pistol, a “hand gun”. Types are named by a word in front. 左轮 means “left wheel”, from the turning cylinder, "
             "so 左轮手枪 is a revolver. 自动 means automatic, so 自动手枪 is an automatic pistol. Models are named with a number and 式, which means “type” or “model”: "
             "五四式手枪 is the Type 54 pistol and 五九式手枪 the Type 59. These are names of Chinese service pistols. The table gives the ordinary reading; in military speech the 五 is said wù, as in Lesson 62.",
             tables=[wtable([("手", "shou3", "hand"), ("枪", "qiang1", "a firearm"), ("手枪", "shou3qiang1", "a pistol"), ("左轮手枪", "zuo3lun2 shou3qiang1", "a revolver"),
                             ("自动手枪", "zi4dong4 shou3qiang1", "an automatic pistol"), ("式", "shi4", "a type, a model"), ("五四式手枪", "wu3 si4 shi4 shou3qiang1", "Type 54 pistol"),
                             ("五九式手枪", "wu3 jiu3 shi4 shou3qiang1", "Type 59 pistol")])]),
        card("Reading the model numbers",
             "In the military the model name is read with military digits, so 五 is wù. Compare this with 手机, “cell phone”: it also begins with 手, “hand”.",
             examples=[ex("这是一把手枪。", "zhe4 shi4 yi4 ba3 shou3qiang1", "This is a pistol."),
                       ex("那是左轮手枪。", "na4 shi4 zuo3lun2 shou3qiang1", "That is a revolver."),
                       ex("他有一把自动手枪。", "ta1 you3 yi4 ba3 zi4dong4 shou3qiang1", "He has an automatic pistol.")]),
    ],
    exercises=[
        mean("手枪", "shou3qiang1", "a pistol", ["a rifle", "a cell phone", "a hand"]),
        mean("左轮手枪", "zuo3lun2 shou3qiang1", "a revolver", ["an automatic pistol", "a rifle", "a cell phone"]),
        mean("自动手枪", "zi4dong4 shou3qiang1", "an automatic pistol", ["a revolver", "a computer", "a rifle"]),
        mean("五四式手枪", "wu3 si4 shi4 shou3qiang1", "Type 54 pistol", ["Type 59 pistol", "a revolver", "an automatic rifle"]),
        mean("手", "shou3", "hand", ["head", "foot", "eye"]),
        mean("枪", "qiang1", "a firearm", ["a hand", "a type", "a pistol"]),
        mean("式", "shi4", "a type, a model", ["a hand", "a firearm", "a number"]),
        rd("手枪", "shou3qiang1", ["shou3qiang2", "shou4qiang1", "shou2qiang1"]),
        rd("左轮手枪", "zuo3lun2 shou3qiang1", ["zuo3lun4 shou3qiang1", "zuo2lun2 shou3qiang1", "zuo3lun2 shou4qiang1"]),
        rd("自动手枪", "zi4dong4 shou3qiang1", ["zi4dong1 shou3qiang1", "zi2dong4 shou3qiang1", "zi4dong4 shou3qiang3"]),
        M("What does 自动 mean?", "Automatic", ["Left wheel", "Type", "Hand"], "自动 is automatic."),
        M("What does 左轮 mean literally?", "Left wheel", ["Automatic", "Type", "Hand gun"], "左 is left and 轮 is wheel."),
        M("How is the digit 五 said in military speech?", "[[wu4]]", ["[[wu3]]", "[[wu2]]", "[[wu1]]"], "Military 5 is wù."),
        F("这是___手枪。 (a revolver)", "左轮", ["自动", "电话", "照片"], "左轮手枪 is a revolver.", tr="This is a revolver."),
        F("他有一把___手枪。 (automatic)", "自动", ["左轮", "电脑", "号码"], "自动手枪 is automatic.", tr="He has an automatic pistol."),
    ],
)

# ---------------------------------------------------------------------------- 67
L67 = lesson(
    "Review: family, age and numbers",
    "Everything from Lesson 3",
    requires=[],
    cards=[
        card("What you have covered",
             "You can now describe your family, give ages, say where people work, use round numbers, and read digits the military way. These questions mix it together.",
             examples=[ex("您今年多大年纪了？ 我今年六十九了。", "nin2 jin1nian2 duo1 da4 nian2ji4 le5? wo3 jin1nian2 liu4shi2jiu3 le5", "How old are you? I am sixty-nine."),
                       ex("他们都是军人，一个是少校，一个是上尉。", "ta1men5 dou1 shi4 jun1ren2, yi2 ge4 shi4 shao4xiao4, yi2 ge4 shi4 shang4wei4", "They are both service members, one a major and one a captain."),
                       ex("你们家有几口人？", "ni3men5 jia1 you3 ji3 kou3 ren2", "How many people are there in your family?")]),
    ],
    exercises=[
        M("Which question do you ask a child?", "你几岁了？", ["你今年多大？", "您今年多大年纪了？", "你多少岁吗？"], "几岁 for children."),
        M("Which question do you ask an older person?", "您今年多大年纪了？", ["你几岁了？", "你今年多大？", "你多大了吗？"], "Polite form."),
        M("What does 四十多 mean?", "More than forty", ["Exactly forty", "Under forty", "Forty-one"], "多 after a round number."),
        M("What does 你是中国人吧？ expect?", "Yes", ["No", "A name", "A number"], "吧 expects confirmation."),
        M("What does 了 do in 他几岁了？", "Softens the question", ["Makes it past tense", "Makes it negative", "Means “and you?”"], "了 softens it."),
        M("How do you say 200?", "两百", ["二百个", "二个百", "两个百"], "两 before 百."),
        M("Which military digit is 7?", "拐", ["洞", "幺", "勾"], "拐 is seven."),
        M("Which military digit is 9?", "勾", ["洞", "幺", "拐"], "勾 is nine."),
        M("Which number sounds like 我爱你?", "520", ["518", "168", "404"], "wǔ èr líng."),
        M("Which place does a doctor usually work in?", "医院", ["军校", "公司", "中学"], "医生 work in 医院."),
        M("How do you say “He works at a hospital”?", "他在医院工作。", ["他工作在医院。", "他医院工作在。", "在他医院工作。"], "在 + place + verb."),
        M("How do you write ü with no initial?", "yu", ["wu", "ü", "ju"], "A bare ü becomes yu."),
        mean("孙子", "sun1zi5", "a grandson (son's son)", ["a son", "a daughter's son", "a younger brother"]),
        mean("家庭主妇", "jia1ting2 zhu3fu4", "a homemaker", ["a nurse", "a student", "a teacher"]),
        rd("岁", "sui4", ["sui1", "sui2", "sui3"]),
        rd("没有", "mei2you3", ["mei4you3", "mei2you2", "mei1you3"]),
        F("我们家有五___人。", "口", ["位", "吗", "们"], "口 counts family members.", tr="There are five people in our family."),
        F("您今年多大年纪___？", "了", ["什么", "们", "谁"], "了 softens.", tr="How old are you?"),
        F("你有___有兄弟姐妹？", "没", ["不", "吗", "们"], "有没有.", tr="Do you have siblings?"),
    ],
)

UNIT = unit("第三课 Age, numbers and sounds", [L59, L60, L61, L62, L63, L64, L65, L66, L67])
