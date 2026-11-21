"""Unit 8: dates and birthdays (lessons 68-79): months and days, days of the week, years and counting time,
asking the date, birthdays, the zodiac, the 是...的 pattern (affirmative, negative, questions), 就, holidays,
the tone changes of 一, review. Original text; the scope follows DLIFLC Chinese Basic Program Unit 1 Lesson 4
(Birthdate, Birthplace and Hometown), Presentation 1."""
from dsl_zh import *

PART = ["吗", "们", "呢"]

# ---------------------------------------------------------------------------- 68
L68 = lesson(
    "Months and days",
    "一月 · 十二月 · 三月十四号",
    requires=[],
    cards=[
        card("Months are numbered",
             "A month is its number plus 月 (yuè), which also means “moon”. January is “month one”, 一月, and December is “month twelve”, 十二月. "
             "There are no separate names to learn. In the names of months the 一 stays in the 1st tone (yī), because it is a name and not an amount.",
             tables=[wtable([("一月", "yi1yue4", "January"), ("二月", "er4yue4", "February"), ("三月", "san1yue4", "March"), ("四月", "si4yue4", "April"),
                             ("五月", "wu3yue4", "May"), ("六月", "liu4yue4", "June"), ("七月", "qi1yue4", "July"), ("八月", "ba1yue4", "August"),
                             ("九月", "jiu3yue4", "September"), ("十月", "shi2yue4", "October"), ("十一月", "shi2yi1yue4", "November"), ("十二月", "shi2er4yue4", "December")])]),
        card("Days of the month",
             "The day is its number plus 号 (hào) in speech and 日 (rì) in writing. The larger unit comes first in Chinese: month, then day. "
             "So March 14 is 三月十四号, “March, fourteenth”.",
             tables=[wtable([("号", "hao4", "day of the month (spoken)"), ("日", "ri4", "day of the month (written)"), ("一号", "yi1hao4", "the 1st"), ("十号", "shi2hao4", "the 10th"),
                             ("十五号", "shi2wu3hao4", "the 15th"), ("二十号", "er4shi2hao4", "the 20th"), ("三十一号", "san1shi2yi1hao4", "the 31st")])],
             examples=[ex("三月十四号", "san1yue4 shi2si4hao4", "March 14", hl="三月"),
                       ex("七月四号", "qi1yue4 si4hao4", "July 4"),
                       ex("十二月二十五号", "shi2er4yue4 er4shi2wu3hao4", "December 25"),
                       ex("一月一号", "yi1yue4 yi1hao4", "January 1")]),
    ],
    exercises=[
        mean("三月", "san1yue4", "March", ["May", "June", "August"]),
        mean("七月", "qi1yue4", "July", ["June", "September", "January"]),
        mean("十一月", "shi2yi1yue4", "November", ["October", "December", "January"]),
        mean("十二月", "shi2er4yue4", "December", ["February", "November", "October"]),
        rd("月", "yue4", ["yue1", "yue2", "ye4"]),
        rd("号", "hao4", ["hao1", "hao3", "hou4"]),
        M("How do you say “October”?", "十月", ["一月", "十一月", "七月"], "十 (10) + 月."),
        M("How do you say “February”?", "二月", ["两月", "十二月", "三月"], "Months use 二, not 两: 二月."),
        M("What is 十二月二十五号?", "December 25", ["December 15", "February 25", "October 25"], "十二月 is December and 二十五号 the 25th."),
        M("What is 七月四号?", "July 4", ["April 7", "July 14", "November 4"], "七月 is July, 四号 the 4th."),
        M("How do you say “March 14”?", "三月十四号", ["十四号三月", "十四月三号", "三号十四月"], "Month first, then day."),
        M("Which is used in speech for the day of the month?", "号", ["日", "月", "年"], "号 is spoken; 日 is written."),
        M("Why is 一月 read yīyuè and not yìyuè?", "It is a name, not an amount", ["It is a question", "It is a negative", "It is a measure word"], "一 keeps the 1st tone in names of months."),
        F("今天是五___十号。", "月", ["号", "们", "吗"], "五月 is May.", tr="Today is May 10."),
        F("今天是十月一___。", "号", ["月", "们", "吗"], "一号 is the 1st.", tr="Today is October 1."),
        F("一___一号是新年。 (January)", "月", PART, "一月 is January.", tr="January 1 is New Year."),
    ],
)

# ---------------------------------------------------------------------------- 69
L69 = lesson(
    "Days of the week",
    "星期一 … 星期天 · 周一",
    requires=[],
    cards=[
        card("星期 and a number",
             "The days of the week are just numbered, like the months: 星期 (xīngqī) plus a number. Monday is 星期一 and Saturday is 星期六. "
             "Sunday is the one exception: it is 星期天 in speech and 星期日 in writing, never 星期七. "
             "A shorter, less formal form uses 周 (zhōu): 周一 is Monday and 周日 is Sunday. To ask which day, put 几 in the number's place: 今天星期几？",
             tables=[wtable([("星期一", "xing1qi1yi1", "Monday"), ("星期二", "xing1qi1er4", "Tuesday"), ("星期三", "xing1qi1san1", "Wednesday"),
                             ("星期四", "xing1qi1si4", "Thursday"), ("星期五", "xing1qi1wu3", "Friday"), ("星期六", "xing1qi1liu4", "Saturday"),
                             ("星期天", "xing1qi1tian1", "Sunday (spoken)"), ("星期日", "xing1qi1ri4", "Sunday (written)"), ("周一", "zhou1yi1", "Monday (short)"),
                             ("周日", "zhou1ri4", "Sunday (short)")])]),
        card("Talking about the week",
             "Use 是 for “is” with a day, and you may leave it out: 今天(是)星期四. Put 下 before 星期 or 周 for “next” and 上 for “last”.",
             examples=[ex("今天星期几？ 今天星期四。", "jin1tian1 xing1qi1ji3? jin1tian1 xing1qi1si4", "What day is it today? It is Thursday.", hl="星期几"),
                       ex("明天是星期五。", "ming2tian1 shi4 xing1qi1wu3", "Tomorrow is Friday."),
                       ex("下周一是我的生日。", "xia4 zhou1yi1 shi4 wo3 de5 sheng1ri4", "Next Monday is my birthday.", hl="下周一"),
                       ex("我们星期一上课。", "wo3men5 xing1qi1yi1 shang4ke4", "We have class on Monday.")]),
    ],
    exercises=[
        mean("星期", "xing1qi1", "week", ["month", "day", "year"]),
        mean("星期三", "xing1qi1san1", "Wednesday", ["Monday", "Thursday", "Friday"]),
        mean("星期六", "xing1qi1liu4", "Saturday", ["Sunday", "Friday", "Thursday"]),
        mean("周一", "zhou1yi1", "Monday (short)", ["Sunday (short)", "a week", "Saturday"]),
        rd("星期", "xing1qi1", ["xing4qi1", "xing1qi3", "xin1qi1"]),
        rd("周", "zhou1", ["zhou3", "zhou4", "zou1"]),
        M("How do you say “Friday”?", "星期五", ["星期四", "星期六", "星期七"], "星期 + 五."),
        M("How do you say “Sunday” in speech?", "星期天", ["星期七", "星期零", "周天天"], "Sunday is 星期天, never 星期七."),
        M("Which question asks the day of the week?", "今天星期几？", ["今天几号？", "今天几月？", "今天什么年？"], "几 stands in for the number after 星期."),
        M("What does 下周一是我的生日 say?", "My birthday is next Monday.", ["My birthday was last Monday.", "My birthday is next month.", "My birthday is every Monday."], "下 is next."),
        M("Which is more formal?", "星期一", ["周一", "一周", "周周"], "周一 is the shorter, less formal form."),
        M("Which day comes after 星期二?", "星期三", ["星期一", "星期四", "星期五"], "二 then 三."),
        F("今天星期___？", "几", ["是", "们", "吗"], "几 asks for a number.", tr="What day is it today?"),
        F("明天是星期___。 (Friday)", "五", ["四", "六", "七"], "五 is five: Friday.", tr="Tomorrow is Friday."),
        F("下___一是我的生日。", "周", ["日", "年", "月"], "下周一 is next Monday.", tr="Next Monday is my birthday."),
    ],
)

# ---------------------------------------------------------------------------- 70
L70 = lesson(
    "Years and counting time",
    "二零零二年 · 两年 · 三天 · 两个星期",
    requires=[],
    cards=[
        card("Saying a year",
             "A year is read digit by digit, then 年 (nián): 2002 is 二零零二年, “two zero zero two year”. Zero is 零. "
             "In years, 一 stays yī. Just as in months, the word 年 is the last thing you say.",
             tables=[wtable([("年", "nian2", "year"), ("二零零二年", "er4 ling2 ling2 er4 nian2", "2002"), ("二零二五年", "er4 ling2 er4 wu3 nian2", "2025"),
                             ("一九四九年", "yi1 jiu3 si4 jiu3 nian2", "1949"), ("一七七六年", "yi1 qi1 qi1 liu4 nian2", "1776")])]),
        card("How long? Counting time",
             "To count years or days, say the number and 年 or 天 directly: 三年 is “three years”, 五天 “five days”. "
             "Weeks and months need the measure word 个: 两个星期, 三个月. For “two”, use 两 in an amount but 二 in a date or a year: 二月 is February, but 两个月 is two months. "
             "Before 年, 一 changes to the 4th tone: 一年 is yì nián, “one year”.",
             tables=[wtable([("一年", "yi4 nian2", "one year"), ("两年", "liang3 nian2", "two years"), ("三天", "san1 tian1", "three days"),
                             ("五天", "wu3 tian1", "five days"), ("两个星期", "liang3 ge4 xing1qi1", "two weeks"), ("三个月", "san1 ge4 yue4", "three months")])]),
    ],
    exercises=[
        M("How do you say 2025?", "二零二五年", ["两零两五年", "二十二五年", "二千零二十五年"], "Read the digits one by one, then 年."),
        M("How do you say 1949?", "一九四九年", ["一千九百四十九年", "十九四九年", "一九四九月"], "Digits, then 年."),
        M("How do you say “two years”?", "两年", ["二年", "两个年", "二个年"], "两 before 年 for an amount; 年 takes no 个."),
        M("How do you say “two weeks”?", "两个星期", ["二星期", "两星期个", "星期两个"], "Weeks need 个: 两个星期."),
        M("How do you say “three days”?", "三天", ["三个天", "天三", "三号天"], "天 counts days directly."),
        M("How do you say “three months”?", "三个月", ["三月", "月三个", "三号月"], "三月 would be March; 三个月 is three months."),
        M("What is 二月?", "February", ["two months", "March", "twelve months"], "二月 is the month name."),
        M("What is 两个月?", "two months", ["February", "twelve months", "the second"], "两个月 is an amount of time."),
        mean("年", "nian2", "year", ["month", "week", "day"]),
        rd("年", "nian2", ["nian1", "nian3", "nian4"]),
        rd("零", "ling2", ["ling1", "ling3", "ling4"]),
        M("What does 零 mean in 二零零二年?", "zero", ["two", "hundred", "year"], "零 is zero."),
        F("我学了两___中文。", "年", ["吗", "们", "呢"], "两年 is two years.", tr="I have studied Chinese for two years."),
        F("我们有两个___。 (weeks)", "星期", ["年", "号", "们"], "两个星期 is two weeks.", tr="We have two weeks."),
        F("二零二五___", "年", ["号", "月", "日"], "Say 年 at the end of a year.", tr="2025"),
    ],
)

# ---------------------------------------------------------------------------- 71
L71 = lesson(
    "Asking the date",
    "今天几号？ · 今年是哪一年？ · 明年 · 下个月",
    requires=[],
    cards=[
        card("Questions about the date",
             "Replace the number with 几 for a month, a day or a day of the week. For a year, use 哪一年, “which year”. "
             "You may add 是, but you do not have to: 今天(是)几号？ The larger unit comes first, so a full date runs year, month, day, weekday.",
             tables=[wtable([("今天几号？", "jin1tian1 ji3 hao4", "What date is it today?"), ("今天星期几？", "jin1tian1 xing1qi1 ji3", "What day is it today?"),
                             ("今天几月几号？", "jin1tian1 ji3 yue4 ji3 hao4", "What is today's date?"), ("现在是几月？", "xian4zai4 shi4 ji3 yue4", "What month is it now?"),
                             ("今年是哪一年？", "jin1nian2 shi4 na3 yi4 nian2", "Which year is this year?")])]),
        card("Time words",
             "These words set the time. 今 is “this”, 明 “tomorrow or next”, 昨 and 去 “yesterday or last”.",
             tables=[wtable([("今天", "jin1tian1", "today"), ("明天", "ming2tian1", "tomorrow"), ("昨天", "zuo2tian1", "yesterday"), ("今年", "jin1nian2", "this year"),
                             ("明年", "ming2nian2", "next year"), ("去年", "qu4nian2", "last year"), ("这个月", "zhe4 ge4 yue4", "this month"),
                             ("下个月", "xia4 ge4 yue4", "next month"), ("上个月", "shang4 ge4 yue4", "last month"), ("下星期", "xia4 xing1qi1", "next week")])],
             examples=[ex("今天是三月五号，星期三。", "jin1tian1 shi4 san1yue4 wu3hao4, xing1qi1san1", "Today is March 5, Wednesday."),
                       ex("今年是哪一年？ 今年是二零二五年。", "jin1nian2 shi4 na3 yi4 nian2? jin1nian2 shi4 er4 ling2 er4 wu3 nian2", "Which year is it? It is 2025.")]),
    ],
    exercises=[
        mean("今天", "jin1tian1", "today", ["tomorrow", "yesterday", "this year"]),
        mean("明天", "ming2tian1", "tomorrow", ["today", "yesterday", "next year"]),
        mean("昨天", "zuo2tian1", "yesterday", ["today", "tomorrow", "last year"]),
        mean("去年", "qu4nian2", "last year", ["this year", "next year", "last month"]),
        mean("明年", "ming2nian2", "next year", ["last year", "this year", "next month"]),
        mean("下个月", "xia4 ge4 yue4", "next month", ["last month", "this month", "next week"]),
        rd("今天", "jin1tian1", ["jin1tian2", "jin4tian1", "jin1tiao1"]),
        rd("昨天", "zuo2tian1", ["zuo3tian1", "zuo2tian2", "zuo4tian1"]),
        M("Which question asks the day of the month?", "今天几号？", ["今天星期几？", "今天几月？", "今年哪一年？"], "几号 asks for the date."),
        M("Which question asks for the full date?", "今天几月几号？", ["今天几号？", "今天星期几？", "现在几月？"], "Month and day."),
        M("Which asks “which year?”", "今年是哪一年？", ["今天是几号？", "今天星期几？", "今年是几月？"], "哪一年 asks for the year."),
        M("How do you say “Today is March 5, Wednesday”?", "今天是三月五号，星期三。", ["今天是五号三月，星期三。", "今天是星期三，三月五日号。", "三月今天五号，星期三。"], "Month, day, weekday."),
        F("今天几月几___？", "号", ["年", "们", "吗"], "几号 asks the date.", tr="What is today's date?"),
        F("___年是二零二五年。 (this year)", "今", ["明", "去", "昨"], "今年 is this year.", tr="This year is 2025."),
        F("下个___是十一月。 (month)", "月", ["年", "号", "天"], "下个月 is next month.", tr="Next month is November."),
    ],
)

# ---------------------------------------------------------------------------- 72
L72 = lesson(
    "Birthdays",
    "生日 · 你的生日是几月几号？ · 真巧！ · 太好了！",
    requires=[],
    cards=[
        card("Asking about a birthday",
             "生日 (shēngrì) is a birthday. Ask 你的生日是几月几号？ and answer with the date. To ask the weekday, say 你的生日是星期几？ "
             "过 (guò) means to celebrate or to spend a day, so 过生日 is to celebrate a birthday, and you wish someone 生日快乐, “happy birthday”.",
             tables=[wtable([("生日", "sheng1ri4", "a birthday"), ("过生日", "guo4 sheng1ri4", "to celebrate a birthday"), ("生日快乐", "sheng1ri4 kuai4le4", "Happy birthday"),
                             ("你的生日是几月几号？", "ni3 de5 sheng1ri4 shi4 ji3 yue4 ji3 hao4", "When is your birthday?"),
                             ("我的生日是五月二十号。", "wo3 de5 sheng1ri4 shi4 wu3yue4 er4shi2hao4", "My birthday is May 20.")])]),
        card("Little words for a chat",
             "Some small words make a conversation sound natural. 真巧 (zhēn qiǎo) is “what a coincidence”, 太好了 (tài hǎo le) “wonderful”, "
             "对了 (duì le) “by the way”, and 哦 (ò) is a surprised “oh”. 啦 (la) is a lively 了, and 和 (hé) is “and”. "
             "可以 (kěyǐ) means “can” or “may”.",
             examples=[ex("你的生日是几月几号？ 我的生日是三月三号。", "ni3 de5 sheng1ri4 shi4 ji3 yue4 ji3 hao4? wo3 de5 sheng1ri4 shi4 san1yue4 san1hao4", "When is your birthday? March 3."),
                       ex("我们的生日都是三月三号。真巧！", "wo3men5 de5 sheng1ri4 dou1 shi4 san1yue4 san1hao4. zhen1 qiao3", "Our birthdays are both March 3. What a coincidence!", hl="真巧"),
                       ex("今天是我的生日。 生日快乐！", "jin1tian1 shi4 wo3 de5 sheng1ri4. sheng1ri4 kuai4le4", "Today is my birthday. Happy birthday!"),
                       ex("对了，你的生日是星期几？", "dui4le5, ni3 de5 sheng1ri4 shi4 xing1qi1 ji3", "By the way, what day is your birthday?", hl="对了")]),
    ],
    exercises=[
        mean("生日", "sheng1ri4", "a birthday", ["a holiday", "a year", "a class"]),
        mean("过生日", "guo4 sheng1ri4", "to celebrate a birthday", ["to be born", "to have a class", "to go home"]),
        mean("真巧", "zhen1 qiao3", "what a coincidence", ["very big", "very far", "very old"]),
        mean("太好了", "tai4 hao3 le5", "wonderful", ["too bad", "not good", "very good-looking"]),
        mean("对了", "dui4le5", "by the way", ["that is wrong", "not yet", "thank you"]),
        rd("生日", "sheng1ri4", ["sheng1ri2", "shen1ri4", "sheng3ri4"]),
        rd("巧", "qiao3", ["qiao1", "qiao2", "qiao4"]),
        rd("过", "guo4", ["guo2", "guo3", "gou4"]),
        M("Which question asks when a birthday is?", "你的生日是几月几号？", ["你是哪年出生的？", "你几岁了？", "今天星期几？"], "几月几号 asks the date."),
        M("What do you say to a friend on their birthday?", "生日快乐！", ["太好了！", "真巧！", "对了！"], "生日快乐 is happy birthday."),
        M("What do you say when two birthdays are the same day?", "真巧！", ["生日快乐！", "对不起！", "再见！"], "真巧 is what a coincidence."),
        M("How do you say “My birthday is on May 20”?", "我的生日是五月二十号。", ["我的五月二十号是生日。", "五月二十号我的生日。", "我生日是二十号五月。"], "是 + month and day."),
        F("今天是我的___日。", "生", ["年", "月", "号"], "生日 is a birthday.", tr="Today is my birthday."),
        F("你的生日是几月几___？", "号", ["年", "们", "吗"], "几月几号.", tr="When is your birthday?"),
        F("我们都是三月三号的生日，真___！", "巧", ["吗", "们", "呢"], "真巧 is what a coincidence.", tr="We both have a March 3 birthday, what a coincidence!"),
    ],
)

# ---------------------------------------------------------------------------- 73
L73 = lesson(
    "The twelve animals",
    "属马 · 鼠 牛 虎 兔 龙 蛇 马 羊 猴 鸡 狗 猪",
    requires=[],
    cards=[
        card("A year for each animal",
             "Chinese years run in a cycle of twelve animals, and you belong to the animal of your birth year. "
             "属 (shǔ) means “to belong to”, so you say 我属马, “I am a horse”. The cycle repeats every twelve years: 2002 is a horse year, 马年, and so are 2014 and 2026. "
             "The zodiac year begins at the Spring Festival, so a birthday in early January or February can belong to the animal of the year before.",
             tables=[wtable([("鼠", "shu3", "rat"), ("牛", "niu2", "ox"), ("虎", "hu3", "tiger"), ("兔", "tu4", "rabbit"), ("龙", "long2", "dragon"), ("蛇", "she2", "snake"),
                             ("马", "ma3", "horse"), ("羊", "yang2", "sheep, goat"), ("猴", "hou2", "monkey"), ("鸡", "ji1", "rooster"), ("狗", "gou3", "dog"), ("猪", "zhu1", "pig")])]),
        card("Asking and answering",
             "Ask 你属什么？ and answer 我属 plus the animal. You can also talk about the year itself: 2020 is 鼠年, a rat year.",
             examples=[ex("你属什么？ 我属马。", "ni3 shu3 shen2me5? wo3 shu3 ma3", "What is your animal? I am a horse.", hl="属"),
                       ex("二零零二年是马年，你是属马的。", "er4 ling2 ling2 er4 nian2 shi4 ma3nian2, ni3 shi4 shu3 ma3 de5", "2002 is a horse year, so you are a horse.", hl="马年"),
                       ex("今年是鼠年，明年是牛年。", "jin1nian2 shi4 shu3nian2, ming2nian2 shi4 niu2nian2", "This year is the rat year, next year the ox year."),
                       ex("二零零一年是蛇年，我姐姐属蛇。", "er4 ling2 ling2 yi1 nian2 shi4 she2nian2, wo3 jie3jie5 shu3 she2", "2001 is a snake year, and my older sister is a snake.")]),
    ],
    exercises=[
        mean("鼠", "shu3", "rat", ["ox", "tiger", "pig"]),
        mean("牛", "niu2", "ox", ["rat", "horse", "dog"]),
        mean("虎", "hu3", "tiger", ["dragon", "rabbit", "monkey"]),
        mean("兔", "tu4", "rabbit", ["tiger", "rat", "sheep"]),
        mean("龙", "long2", "dragon", ["snake", "tiger", "rooster"]),
        mean("蛇", "she2", "snake", ["dragon", "monkey", "pig"]),
        mean("马", "ma3", "horse", ["ox", "sheep", "dog"]),
        mean("羊", "yang2", "sheep, goat", ["horse", "monkey", "rabbit"]),
        mean("猴", "hou2", "monkey", ["tiger", "dog", "pig"]),
        mean("鸡", "ji1", "rooster", ["dragon", "dog", "rat"]),
        mean("狗", "gou3", "dog", ["pig", "rat", "ox"]),
        mean("猪", "zhu1", "pig", ["dog", "rooster", "rabbit"]),
        rd("鼠", "shu3", ["shu1", "shu2", "shu4"]),
        rd("龙", "long2", ["long1", "long3", "long4"]),
        rd("蛇", "she2", ["she1", "she3", "she4"]),
        rd("属", "shu3", ["shu1", "shu2", "shu4"]),
        M("What does 我属马 mean?", "I was born in a horse year.", ["I have a horse.", "I like horses.", "I am a horse trainer."], "属 + animal gives your birth-year animal."),
        M("How many animals are in the cycle?", "Twelve", ["Ten", "Eight", "Twenty"], "The cycle has twelve animals."),
        M("Which animal is 2001?", "蛇", ["马", "龙", "鼠"], "二零零一年 is a snake year."),
        M("Which animal is 2002?", "马", ["蛇", "羊", "猴"], "二零零二年 is a horse year."),
        M("Which year is a rat year?", "二零二零年", ["二零二一年", "二零二二年", "二零一九年"], "2020 starts a new cycle with the rat."),
        M("Which question asks your zodiac animal?", "你属什么？", ["你几岁？", "你叫什么？", "你是哪国人？"], "属什么 asks which animal."),
        F("我___马。 (belong to)", "属", PART, "属 is to belong to.", tr="I am a horse."),
        F("二零零二年是___年。 (horse)", "马", ["牛", "鼠", "龙"], "2002 is a horse year.", tr="2002 is a horse year."),
    ],
)

# ---------------------------------------------------------------------------- 74
L74 = lesson(
    "Born in: the 是…的 pattern",
    "你是哪年出生的？ · 我是在纽约出生的。",
    requires=[],
    cards=[
        card("Asking about a known event",
             "出生 (chūshēng) means “to be born”. To ask when or where it happened, Chinese uses the pattern 是 … 的. "
             "You use it when both people already know that something happened and you want the details: when, where, how or with whom. "
             "是 goes before the detail, and 的 goes at the end of the sentence. In everyday speech you may drop 是: 他在纽约出生的.",
             tables=[table(["Pattern", "Example"], [["是 + detail + verb + 的", "他是在纽约出生的。"], ["detail = when", "我是二零零二年出生的。"], ["detail = where", "你是在哪儿出生的？"]], say=[1])]),
        card("What the detail can be",
             "The detail sits between 是 and the verb. Questions use 哪一年, 在哪儿 and 什么时候 (shénme shíhou, “when”) in the same place.",
             examples=[ex("你是哪一年出生的？", "ni3 shi4 na3 yi4 nian2 chu1sheng1 de5", "What year were you born?", hl="哪一年"),
                       ex("我是二零零二年出生的。", "wo3 shi4 er4 ling2 ling2 er4 nian2 chu1sheng1 de5", "I was born in 2002."),
                       ex("他是在纽约出生的。", "ta1 shi4 zai4 niu3yue1 chu1sheng1 de5", "He was born in New York.", hl="在纽约"),
                       ex("你是什么时候认识你太太的？", "ni3 shi4 shen2me5 shi2hou5 ren4shi5 ni3 tai4tai5 de5", "When did you meet your wife?"),
                       ex("我们是昨天来的。", "wo3men5 shi4 zuo2tian1 lai2 de5", "We came yesterday.", hl="昨天")])]
    ,
    exercises=[
        mean("出生", "chu1sheng1", "to be born", ["to live", "to grow up", "to celebrate"]),
        rd("出生", "chu1sheng1", ["chu1sheng4", "chu2sheng1", "cu1sheng1"]),
        M("What does 你是哪一年出生的？ ask?", "What year were you born?", ["Where were you born?", "How old are you?", "When is your birthday?"], "哪一年 asks the year."),
        M("What does 你是在哪儿出生的？ ask?", "Where were you born?", ["What year were you born?", "Where do you live?", "Where are you going?"], "在哪儿 asks the place."),
        M("What does 我是二零零二年出生的 say?", "I was born in 2002.", ["I will be born in 2002.", "I am 2002 years old.", "I have lived since 2002."], "是 + year + 出生 + 的."),
        M("Where does 是 go in the pattern?", "Before the detail", ["After the verb", "At the end", "Before the subject"], "是 + detail + verb + 的."),
        M("Where does 的 go in the pattern?", "At the end of the sentence", ["Before 是", "After the subject", "Before the detail"], "的 closes the pattern."),
        M("Which one drops 是 correctly?", "他在纽约出生的。", ["他在纽约出生。的", "他纽约在出生的。", "他在出生纽约的。"], "是 may be dropped in a statement."),
        M("Which sentence is in the 是…的 pattern?", "我是在北京出生的。", ["我出生在北京了。", "我在北京。", "我是北京。"], "是 + 在北京 + 出生 + 的."),
        M("Which asks “When did you meet your wife?”", "你是什么时候认识你太太的？", ["你太太是什么时候？", "你认识你太太吗？", "你太太认识你吗？"], "什么时候 sits in the detail slot."),
        F("你是哪一年出生___？", "的", ["吗", "们", "呢"], "的 ends the pattern.", tr="What year were you born?"),
        F("我是在上海出生___。", "的", ["吗", "们", "呢"], "是…的.", tr="I was born in Shanghai."),
        F("我们是昨天来___。", "的", ["吗", "们", "呢"], "是…的.", tr="We came yesterday."),
        F("你是什么___候认识他的？ (when)", "时", ["号", "岁", "年"], "什么时候 is when.", tr="When did you meet him?"),
    ],
)

# ---------------------------------------------------------------------------- 75
L75 = lesson(
    "是…的: no and questions",
    "他不是在纽约出生的。 · 他是不是在纽约出生的？",
    requires=[],
    cards=[
        card("Saying no",
             "To deny the detail, put 不 before 是: 不是 + detail + verb + 的. This time you cannot drop 是. "
             "So 他不是在纽约出生的 means “He was not born in New York”; the real place is something else.",
             tables=[table(["Form", "Pattern", "Example"],
                           [["Statement", "是 + detail + verb + 的", "他是在纽约出生的。"], ["Negative", "不是 + detail + verb + 的", "他不是在纽约出生的。"],
                            ["Question 1", "是 + detail + verb + 的吗？", "他是在纽约出生的吗？"], ["Question 2", "是不是 + detail + verb + 的？", "他是不是在纽约出生的？"]], say=[2])]),
        card("Both questions mean the same",
             "A yes/no question can end with 吗 or use 是不是 before the detail. 是不是 is a bit more neutral. Answer with 是 or 不是, then add the real detail.",
             examples=[ex("你是在北京出生的吗？ 是，我是在北京出生的。", "ni3 shi4 zai4 bei3jing1 chu1sheng1 de5 ma5? shi4, wo3 shi4 zai4 bei3jing1 chu1sheng1 de5", "Were you born in Beijing? Yes, I was."),
                       ex("你是不是在北京出生的？ 不是，我是在上海出生的。", "ni3 shi4 bu2 shi4 zai4 bei3jing1 chu1sheng1 de5? bu2 shi4, wo3 shi4 zai4 shang4hai3 chu1sheng1 de5", "Were you born in Beijing? No, I was born in Shanghai.", hl="不是"),
                       ex("她不是二零零二年出生的。", "ta1 bu2 shi4 er4 ling2 ling2 er4 nian2 chu1sheng1 de5", "She was not born in 2002.")]),
    ],
    exercises=[
        M("How do you say “He was not born in New York”?", "他不是在纽约出生的。", ["他是不在纽约出生的。", "他在纽约不出生的。", "他不在纽约出生是的。"], "不 goes before 是."),
        M("Can you drop 是 in a negative?", "No, 不是 stays", ["Yes, always", "Only in questions", "Only with 的"], "A negative needs 不是."),
        M("Which is a correct yes/no question?", "你是在北京出生的吗？", ["你是吗在北京出生的？", "你吗是在北京出生的？", "你是在北京出生吗的？"], "是…的吗."),
        M("Which is the A-not-A form?", "你是不是在北京出生的？", ["你是在不北京出生的？", "你是在北京不出生的？", "你不是在北京出生的？"], "是不是 before the detail."),
        M("Which answers “Were you born in Beijing?” with “no”?", "不是，我是在上海出生的。", ["不对，我是在上海出生。", "没有，我是在上海出生的。", "不，我上海出生的是。"], "不是, then the real detail."),
        M("What does 她不是二零零二年出生的 say?", "She was not born in 2002.", ["She was born in 2002.", "She will not be born in 2002.", "She is not 2002."], "不是 denies the year."),
        M("Which of these is both correct and in the pattern?", "他是在北京上大学的。", ["他是在北京大学上的。", "他在北京是上大学。", "他上在北京大学是的。"], "是 + place + verb + 的."),
        M("Both forms 吗 and 是不是 are…", "yes/no questions", ["negatives", "answers", "statements"], "They are two ways to ask."),
        F("他___是在纽约出生的。", "不", ["吗", "们", "呢"], "不是 is the negative.", tr="He was not born in New York."),
        F("你是___是在北京出生的？", "不", ["吗", "们", "呢"], "是不是 forms the question.", tr="Were you born in Beijing?"),
        F("你是在北京出生的___？", "吗", ["们", "呢", "的"], "吗 ends a yes/no question.", tr="Were you born in Beijing?"),
        F("我不是在上海出生的，我是在北京出生___。", "的", ["吗", "们", "呢"], "是…的 again.", tr="I was not born in Shanghai; I was born in Beijing."),
        F("不___，我是在上海出生的。", "是", ["吗", "们", "呢"], "不是 is “no, not so”.", tr="No, I was born in Shanghai."),
    ],
)

# ---------------------------------------------------------------------------- 76
L76 = lesson(
    "就 for emphasis and “soon”",
    "下星期就是我的生日了 · 她就是南方人",
    requires=[],
    cards=[
        card("就 means “exactly”",
             "就 (jiù) comes before a verb, a place phrase or 是 to stress a fact, like “indeed” or “exactly” in English. "
             "Before a noun or an adjective you need 是 too: 就是. 她就是南方人, “She is a southerner, indeed”. 我就住在这儿 is “I live right here”.",
             tables=[table(["Pattern", "Example", "Meaning"],
                           [["就是 + noun", "她就是南方人。", "She is a southerner indeed."], ["就 + 在 + place", "我老家就在中国北方。", "My hometown is right in the north of China."],
                            ["就 + verb", "我就住在这儿。", "I live right here."], ["就是 + adjective", "他的中文就是好。", "His Chinese really is good."]], say=[1])]),
        card("就 also means “soon”",
             "With a time word, 就 can mean that something comes soon or is close: 下星期就是我的生日了, “my birthday is already next week”. "
             "The 了 at the end adds the feeling of “it is almost here”.",
             examples=[ex("下星期就是我的生日了。", "xia4 xing1qi1 jiu4 shi4 wo3 de5 sheng1ri4 le5", "My birthday is next week already.", hl="就"),
                       ex("他就是老师，不是学生。", "ta1 jiu4 shi4 lao3shi1, bu2 shi4 xue2sheng5", "He is a teacher indeed, not a student.", hl="就是"),
                       ex("我老家就在中国北方。", "wo3 lao3jia1 jiu4 zai4 zhong1guo2 bei3fang1", "My hometown is right in the north of China.", hl="就在")]),
    ],
    exercises=[
        mean("就", "jiu4", "just, exactly; soon", ["still", "also", "not"]),
        rd("就", "jiu4", ["jiu1", "jiu2", "jiu3"]),
        M("What does 她就是南方人 mean?", "She is a southerner, indeed.", ["She is not a southerner.", "She is going to the south.", "She is from the north."], "就是 stresses a fact."),
        M("What does 下星期就是我的生日了 mean?", "My birthday is next week already.", ["My birthday was last week.", "I have no birthday.", "My birthday is next year."], "就…了 is “soon”."),
        M("What does 我就住在这儿 mean?", "I live right here.", ["I used to live here.", "I do not live here.", "I want to live here."], "就 + verb is emphasis."),
        M("Which needs 是 after 就?", "Before a noun", ["Before a verb", "Before a place word", "Before a number"], "就是 + noun."),
        M("Where does 就 go?", "Before the verb or 是", ["At the end", "After the verb", "Before the subject"], "就 comes before the verb."),
        M("Which sentence stresses “he is a teacher indeed”?", "他就是老师。", ["他是就老师。", "就他老师是。", "他老师就。"], "就是 + noun."),
        M("Which stresses “His Chinese really is good”?", "他的中文就是好。", ["他的中文是就好。", "他的就中文好。", "就他的中文是好。"], "就是 + adjective."),
        F("她___是南方人。", "就", ["吗", "们", "呢"], "就是 stresses a fact.", tr="She is a southerner, indeed."),
        F("我老家___在中国北方。", "就", ["也", "吗", "们"], "就在 is “right in”.", tr="My hometown is right in the north of China."),
        F("下星期就是我的生日___。", "了", ["吗", "们", "呢"], "了 adds “already”.", tr="My birthday is next week already."),
        F("他的中文就___好。", "是", PART, "Before an adjective you need 就是.", tr="His Chinese is really good."),
    ],
)

# ---------------------------------------------------------------------------- 77
L77 = lesson(
    "Holidays",
    "春节 · 新年 · 国庆节 · 圣诞节 · 感恩节",
    requires=[],
    cards=[
        card("Festivals with a fixed date",
             "节 (jié) is a festival or holiday. Some have the same date every year in the usual calendar: New Year is January 1, Labour Day May 1, "
             "American Independence Day July 4, China's National Day October 1 and Christmas December 25. "
             "The Spring Festival, 春节, follows the old calendar, so its date moves from late January to mid-February, and Qingming is in early April. "
             "Thanksgiving is on the fourth Thursday of November.",
             tables=[wtable([("新年", "xin1nian2", "New Year (January 1)"), ("春节", "chun1jie2", "Spring Festival (Chinese New Year)"), ("清明节", "qing1ming2 jie2", "Qingming Festival (early April)"),
                             ("劳动节", "lao2dong4 jie2", "Labour Day (May 1)"), ("独立日", "du2li4 ri4", "Independence Day (July 4)"), ("国庆节", "guo2qing4 jie2", "National Day (October 1)"),
                             ("感恩节", "gan3'en1jie2", "Thanksgiving"), ("圣诞节", "sheng4dan4 jie2", "Christmas (December 25)")])]),
        card("Talking about them",
             "Ask 春节是几月几号？ for a date and say what you will do with 过: 过春节 is to celebrate the Spring Festival. 一起 (yìqǐ) means “together”.",
             examples=[ex("国庆节是十月一号。", "guo2qing4jie2 shi4 shi2yue4 yi1hao4", "National Day is October 1.", hl="国庆节"),
                       ex("圣诞节是十二月二十五号。", "sheng4dan4jie2 shi4 shi2er4yue4 er4shi2wu3hao4", "Christmas is December 25."),
                       ex("我们一起过春节。", "wo3men5 yi4qi3 guo4 chun1jie2", "We celebrate the Spring Festival together.", hl="一起"),
                       ex("你们美国的独立日是几月几号？ 是七月四号。", "ni3men5 mei3guo2 de5 du2li4ri4 shi4 ji3 yue4 ji3 hao4? shi4 qi1yue4 si4hao4", "When is your Independence Day? July 4.")]),
    ],
    exercises=[
        mean("春节", "chun1jie2", "Spring Festival", ["National Day", "Labour Day", "Christmas"]),
        mean("新年", "xin1nian2", "New Year", ["Spring Festival", "birthday", "next year"]),
        mean("国庆节", "guo2qing4 jie2", "National Day", ["Labour Day", "Thanksgiving", "Spring Festival"]),
        mean("劳动节", "lao2dong4 jie2", "Labour Day", ["National Day", "Independence Day", "New Year"]),
        mean("独立日", "du2li4 ri4", "Independence Day", ["Labour Day", "National Day", "Christmas"]),
        mean("圣诞节", "sheng4dan4 jie2", "Christmas", ["Thanksgiving", "New Year", "Spring Festival"]),
        mean("感恩节", "gan3'en1jie2", "Thanksgiving", ["Christmas", "New Year", "Labour Day"]),
        mean("清明节", "qing1ming2 jie2", "Qingming Festival", ["Spring Festival", "Labour Day", "Christmas"]),
        rd("节", "jie2", ["jie3", "jie4", "jue2"]),
        rd("春节", "chun1jie2", ["chun1jie4", "cun1jie2", "chun2jie2"]),
        M("What is 节?", "a festival, a holiday", ["a month", "a week", "a birthday"], "节 is a holiday."),
        M("Which holiday is on December 25?", "圣诞节", ["国庆节", "劳动节", "新年"], "圣诞节 is Christmas."),
        M("Which holiday is on October 1 in China?", "国庆节", ["春节", "圣诞节", "独立日"], "国庆节 is National Day."),
        M("Which holiday is on May 1?", "劳动节", ["国庆节", "感恩节", "新年"], "劳动节 is Labour Day."),
        M("Why does the date of 春节 change each year?", "It follows the old calendar", ["It is on a Monday", "It is always on a Saturday", "It has no date"], "The Spring Festival follows the old calendar."),
        M("How do you say “We celebrate the Spring Festival together”?", "我们一起过春节。", ["我们过一起春节。", "一起我们春节过。", "我们春节一起的过。"], "一起 comes before the verb."),
        F("我们一起___春节。 (celebrate)", "过", ["吗", "们", "呢"], "过春节 is to celebrate the Spring Festival.", tr="We celebrate the Spring Festival together."),
        F("国庆节是十月一___。", "号", ["年", "们", "吗"], "一号 is the 1st.", tr="National Day is October 1."),
    ],
)

# ---------------------------------------------------------------------------- 78
L78 = lesson(
    "The tone changes of 一",
    "yī · yì · yí: 一个 · 一年 · 一点儿",
    requires=[],
    cards=[
        card("Three tones for one character",
             "The character 一 (“one”) is the 1st tone, yī, when it stands alone, ends a word or is an ordinal: 一, 二, 三; 二十一; 星期一; 一月. "
             "Before a 1st, 2nd or 3rd tone it becomes the 4th tone, yì: 一张照片 (yì zhāng zhàopiàn), 一年 (yì nián), 一点儿 (yìdiǎnr). "
             "Before a 4th tone it becomes the 2nd, yí: 一个 (yí gè). The pinyin in this app shows the changed tone, so just read what you see.",
             tables=[table(["Rule", "Example", "Pinyin", "Meaning"],
                           [["alone or at the end: yī", "二十一", "[[er4shi2yi1]]", "twenty-one"], ["before tone 1, 2, 3: yì", "一年", "[[yi4 nian2]]", "one year"],
                            ["before tone 1, 2, 3: yì", "一点儿", "[[yi4dian3r5]]", "a little"], ["before tone 4: yí", "一个", "[[yi2 ge4]]", "one (of)"]], say=[1])]),
        card("A quick method",
             "Look at the syllable after 一. If it is a 4th tone, say yí. If it is anything else, say yì. If nothing follows, say yī.",
             examples=[ex("我今年二十一。", "wo3 jin1nian2 er4shi2yi1", "I am twenty-one this year.", hl="二十一"),
                       ex("一年有十二个月。", "yi4 nian2 you3 shi2er4 ge4 yue4", "A year has twelve months.", hl="一年"),
                       ex("请你慢一点儿说。", "qing3 ni3 man4 yi4dian3r5 shuo1", "Please speak a little more slowly.", hl="一点儿"),
                       ex("我有一个哥哥。", "wo3 you3 yi2 ge4 ge1ge5", "I have one older brother.", hl="一个")]),
    ],
    exercises=[
        M("How is 一 read in 二十一?", "yī", ["yí", "yì", "yǐ"], "At the end of a number it stays yī."),
        M("How is 一 read in 一个?", "yí", ["yī", "yì", "yǐ"], "Before a 4th tone it is yí."),
        M("How is 一 read in 一年?", "yì", ["yī", "yí", "yǐ"], "Before a 2nd tone it is yì."),
        M("How is 一 read in 一点儿?", "yì", ["yī", "yí", "yǐ"], "Before a 3rd tone it is yì."),
        M("How is 一 read in 星期一?", "yī", ["yí", "yì", "yǐ"], "Last in the word, so yī."),
        M("How is 一 read in 一月?", "yī", ["yí", "yì", "yǐ"], "It is a name, so yī."),
        M("How is 一 read in 一张照片?", "yì", ["yī", "yí", "yǐ"], "Before the 1st tone 张 it is yì."),
        M("What decides the tone of 一?", "The tone of the next syllable", ["The tone before it", "The speaker's age", "The measure word only"], "Look at the following syllable."),
        M("Which is the correct pinyin of 一个?", "[[yi2 ge4]]", ["[[yi1 ge4]]", "[[yi4 ge4]]", "[[yi3 ge4]]"], "yí gè."),
        M("Which is the correct pinyin of 一年?", "[[yi4 nian2]]", ["[[yi1 nian2]]", "[[yi2 nian2]]", "[[yi3 nian2]]"], "yì nián."),
        M("Which is the correct pinyin of 二十一?", "[[er4shi2yi1]]", ["[[er4shi2yi4]]", "[[er4shi2yi2]]", "[[er4shi2yi3]]"], "yī at the end."),
        M("Which is the correct pinyin of 一点儿?", "[[yi4dian3r5]]", ["[[yi1dian3r5]]", "[[yi2dian3r5]]", "[[yi3dian3r5]]"], "yìdiǎnr."),
        F("我有___个哥哥。 (one)", "一", ["吗", "们", "呢"], "一个 is one.", tr="I have one older brother."),
        F("请你慢一点儿___。 (speak)", "说", ["吗", "们", "呢"], "说 is to speak.", tr="Please speak a little more slowly."),
    ],
)

# ---------------------------------------------------------------------------- 79
L79 = lesson(
    "Review: dates and birthdays",
    "月 号 星期 年 · 生日 · 属 · 是…的 · 就",
    requires=[],
    cards=[
        card("What you can now do",
             "You can say any date, the day of the week and the year, ask when someone was born, name the animal of a birth year and use 是…的 and 就. "
             "Mix them in these questions.",
             examples=[ex("你是哪年出生的？ 我是二零零二年出生的。", "ni3 shi4 na3 nian2 chu1sheng1 de5? wo3 shi4 er4 ling2 ling2 er4 nian2 chu1sheng1 de5", "What year were you born? I was born in 2002."),
                       ex("你的生日是几月几号？ 下星期就是我的生日了。", "ni3 de5 sheng1ri4 shi4 ji3 yue4 ji3 hao4? xia4 xing1qi1 jiu4 shi4 wo3 de5 sheng1ri4 le5", "When is your birthday? It is next week."),
                       ex("二零零二年是马年，你属马。", "er4 ling2 ling2 er4 nian2 shi4 ma3nian2, ni3 shu3 ma3", "2002 is a horse year, so you are a horse.")]),
    ],
    exercises=[
        M("How do you say “Tuesday”?", "星期二", ["星期两", "星期天", "二星期"], "星期 + 二."),
        M("How do you say “August 8”?", "八月八号", ["八号八月", "八月八年", "八月八天"], "Month, then day."),
        M("How do you say “2008”?", "二零零八年", ["二千零八年", "两零零八年", "二零零八号"], "Read the digits."),
        M("Which question asks the date?", "今天几月几号？", ["你属什么？", "你是哪国人？", "你是谁？"], "几月几号."),
        M("Which question asks your birth year?", "你是哪一年出生的？", ["你几岁？", "你叫什么？", "你在哪儿？"], "是 + 哪一年 + 出生的."),
        M("What does 我属龙 say?", "I am a dragon (born in a dragon year).", ["I have a dragon.", "I like dragons.", "I live near a dragon."], "属 + animal."),
        M("Which is the negative of 我是在北京出生的?", "我不是在北京出生的。", ["我是不在北京出生的。", "我没是在北京出生的。", "我在北京不出生的。"], "不是…的."),
        M("What does 就 do in 她就是南方人?", "It stresses the fact", ["It makes it negative", "It makes it a question", "It means “and”"], "就是 is “indeed”."),
        M("How do you say “two months”?", "两个月", ["二月", "二个月", "月二个"], "两 + 个 + 月."),
        M("How is 一 read in 一个?", "yí", ["yī", "yì", "yǐ"], "Before the 4th tone it is yí."),
        mean("生日", "sheng1ri4", "a birthday", ["a year", "a festival", "a week"]),
        mean("明天", "ming2tian1", "tomorrow", ["yesterday", "today", "next year"]),
        rd("星期", "xing1qi1", ["xing4qi1", "xing1qi3", "xin1qi1"]),
        F("今天星期___？", "几", ["号", "们", "吗"], "几 asks for the day.", tr="What day is it today?"),
        F("你是哪一年出生___？", "的", PART, "是…的.", tr="What year were you born?"),
        F("我___牛。 (I belong to the ox)", "属", PART, "属 + animal.", tr="I am an ox."),
    ],
)

UNIT = unit("第四课 Dates and birthdays", [L68, L69, L70, L71, L72, L73, L74, L75, L76, L77, L78, L79])
