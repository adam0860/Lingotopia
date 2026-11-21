"""Unit 101: Lesson 29 (Education in China), Presentation 3 vocabulary list and the Area Studies page on China's education.
The Area Studies text is the book's English text; the reference line (a web address) and the pictures are not included."""
from zh_auto import *
from zh_l29_vocab import VOC3

_D0 = D


def D(zh, en, hl=None, fixes=None):
    f = {"称": "cheng1", "长": "chang2"}
    for key, idx, val in (("那得看", 1, "dei3"), ("得一个人", 0, "dei3"), ("方便得多", 2, "de5"), ("便宜得多", 2, "de5"), ("快得多", 1, "de5"), ("好得多", 1, "de5"), ("少得多", 1, "de5"), ("大得多", 1, "de5"), ("贵得多", 1, "de5"), ("慢得多", 1, "de5"), ("得亲自", 0, "dei3"), ("得自己", 0, "dei3"), ("得在旅馆", 0, "dei3"), ("得知道", 0, "dei3"), ("得加班", 0, "dei3"), ("得帮忙", 0, "dei3"), ("了解", 0, "liao3"), ("去不了", 2, "liao3"), ("校长", 1, "zhang3"), ("着急", 0, "zhao2"),
                          ("选为", 1, "wei2"), ("都得", 1, "dei3"), ("没有", 0, "mei2"), ("没超重", 0, "mei2"), ("没去过", 0, "mei2"), ("还没去", 1, "mei2"), ("没有什么", 0, "mei2"), ("都会", 0, "dou1"), ("睡觉", 1, "jiao4"), ("教练", 0, "jiao4"), ("参加", 0, "can1"), ("参军", 0, "can1"), ("列车长", 2, "zhang3"), ("得看", 0, "dei3"), ("得多", 0, "de5"), ("填得", 1, "de5"), ("得设", 0, "dei3"), ("写得", 1, "de5"), ("得直接", 0, "dei3"), ("得靠", 0, "dei3"), ("挣钱", 0, "zheng4"), ("分行", 1, "hang2"), ("送还给", 1, "huan2"), ("还给", 0, "huan2"), ("班长", 1, "zhang3"), ("得把", 0, "dei3"), ("两地", 1, "di4")):
        j = zh.find(key)
        while j >= 0:
            f[j + idx] = val
            j = zh.find(key, j + 1)
    for j, ch in enumerate(zh):  # 地 as the adverbial marker is de5; keep dì in 草地, 当地, 地道, 地址, ...
        if ch == "地" and j > 0:
            f[j] = "de5" if zh[max(0, j - 2):j + 1] in ("极大地", "方便地") else "di4" if (zh[max(0, j - 2):j + 1] in ("目的地", "留学地", "旅游地") or zh[j - 1] in "当草土天各山场内本外基实陆特两圣亩" or (j + 1 < len(zh) and zh[j + 1] in "道址方铁图球区点上下面理形段里")) else "de5"
    f.update(fixes or {})
    return _D0(zh, en, hl, f)


import zh_auto as _za
_za.D = D

PART = ["吗", "们", "呢"]

# ------------------------------------------------------------------ 1. vocabulary
L1 = vocab_lesson("Lesson 29 Presentation 3 vocabulary", "17 words from the book’s Presentation 3 list",
                  "Presentation 3 vocabulary (listen and repeat)", "The book’s table with characters, traditional characters, pinyin, part of speech and English. The book prints the entry 不起 as the suffix -不起; here it is listed as 不起.", VOC3)

# ------------------------------------------------------------------ 2. area studies
H1 = ("China was the first country in the world to have a complete educational system. According to historic record, as early as the Xia Dynasty (夏朝 2070–1600 BC) China had schools. There were two types of schools in the Western Zhou Dynasty (西周 1046–771 BC): 国学 and 乡学. 国学 was established in the capital of the Western Zhou Dynasty and the capitals of the feudal states. 国学 was divided into “universities” and “elementary schools.” Only the children of slave owners and nobles could enter 国学. 乡学 was set up in various places for the children of ordinary slave owners and nobles to study. The earliest institution of higher learning in ancient times was 太学 in the Western Han Dynasty (西汉 202 BC–9 AD). Emperor Wu (汉武帝) of the Western Han Dynasty accepted the advice of the famous thinker and master of classics Dong Zhongshu (董仲舒) and founded 太学 in 长安 (now 西安), the capital of the country in Han Dynasty. However, it was not until the end of the Qing Dynasty (清朝 1644–1912) that schools with modern education methods began to appear in China. After the founding of the People’s Republic of China, the undertaking of education has been further developed.")
H2 = ("Since 1986, China has implemented nine years of compulsory education, including six years of elementary school and three years of junior high school for students between the ages of 6 and 15. In 2010, about 82.5% of students would choose to continue their three-year high school education. The government-sponsored national examination for general higher education institutions is a prerequisite for entering most higher education institutions. In 2010, 27% of senior high school graduates will continue to receive four years of undergraduate education. Additionally, postgraduate education is also provided, and the government has established intermediate and advanced technical schools to provide students with vocational education.")
H3 = ("The education of the People’s Republic of China is under the supervision of the Ministry of Education of the People’s Republic of China. The provincial people’s governments set up education departments, and lower-level institutions set up education bureaus to manage local educational affairs. In 2019, China has a total of 161,811 elementary schools, 51,982 junior high schools, 13,737 senior high schools, 10,299 secondary vocational schools, 2,663 regular colleges and universities, and 1,418 higher vocational colleges. As of 2015, the literacy rate of the population over the age of 15 is 96.4% (males 98.2%, females 94.5%). In contrast, in 1950 the literacy rate was only 20% of the population.")
H4 = ("Preschool education in China generally starts at the age of three, in kindergarten. Preschool education in China is generally divided into three stages: lower classes (小班 3–4 years old), middle classes (中班 4–5 years old), and upper classes (大班 5–6 years old). In some kindergartens and elementary schools, there are also “preschools” to educate children under the age of 6 to adapt to school life. Life in kindergarten consists of many learning activities and educational games, with three meals a day. Preschool is similar to school, but the time is shorter and there are more outdoor activities.")
H5 = ("China’s spending on education remained above 4 percent of the gross domestic product (GDP) in 2018. That year, public spending on education in China reached 3.49 billion yuan (as printed; a national total would be in trillions, so this looks like a slip in the book). Even though educational spending in China improved a lot in the last decades, when calculated per student, expenditure is still far behind developed countries. While spending per student on education in OECD countries averaged nearly $15,600 U.S. in 2016, it reached only $5,300 U.S. per student in China in 2018, which is less than one third of that spent by other developed countries. This fact sheds some light on the average quality of the educational system in China and reminds us that China is an extremely large and populous country. In China some elite schools in the big cities coexist with vast numbers of schools in the countryside operating on a completely different level of quality. For this reason, in China’s big cities, more than 70% of students can go to college. In contrast, less than 5 percent of students in poor rural areas can go to college. Therefore, China still has a long way to go before it can provide the best education for every student in the country, despite the great progress that has been made in the past decades.")
L2 = lesson(
    "Lesson 29 Area Studies: China’s Education",
    "夏朝 · 西周 · 国学和乡学 · 太学 · 九年义务教育 · 小班 中班 大班 · 教育经费",
    requires=[],
    cards=[
        card("China’s Education: from ancient schools to the People’s Republic", H1),
        card("Compulsory education and higher education", H2),
        card("Administration, school numbers and literacy", H3),
        card("Preschool education", H4),
        card("Spending on education and the urban-rural gap", H5),
    ],
    exercises=[
        M("According to the page, which country was the first to have a complete educational system?", "China", ["Greece", "Egypt", "Rome"], "China was the first country in the world to have a complete educational system."),
        M("As early as which dynasty did China have schools, according to historic record?", "The Xia Dynasty", ["The Qing Dynasty", "The Han Dynasty", "The Tang Dynasty"], "As early as the Xia Dynasty."),
        M("Which two types of schools were there in the Western Zhou Dynasty?", "国学 and 乡学", ["太学 and 国学", "小班 and 大班", "乡学 and 太学"], "国学 and 乡学."),
        M("Who could enter 国学?", "Only children of slave owners and nobles", ["Anyone", "Only farmers’ children", "Only girls"], "Only the children of slave owners and nobles."),
        M("What was the earliest institution of higher learning in ancient times?", "太学 in the Western Han Dynasty", ["国学 in the Zhou", "A school in the Qing", "A kindergarten"], "太学 in the Western Han Dynasty."),
        M("Whose advice did Emperor Wu accept in founding 太学?", "Dong Zhongshu’s", ["Confucius’s", "Mencius’s", "Sima Qian’s"], "He accepted the advice of Dong Zhongshu."),
        M("When did schools with modern education methods begin to appear in China?", "Not until the end of the Qing Dynasty", ["In the Xia Dynasty", "In the Han Dynasty", "In 1986"], "Not until the end of the Qing Dynasty."),
        M("How many years of compulsory education has China implemented since 1986?", "Nine", ["Six", "Twelve", "Three"], "Six years of elementary school and three of junior high."),
        M("About what share of students chose to continue to high school in 2010?", "82.5%", ["28.5%", "52.5%", "98.5%"], "About 82.5%."),
        M("What share of senior high graduates continued to undergraduate education in 2010?", "27%", ["72%", "7%", "2.7%"], "27%."),
        M("What was the literacy rate of the population over 15 as of 2015?", "96.4%", ["64.9%", "20%", "99%"], "96.4%."),
        M("What was the literacy rate in 1950?", "20%", ["50%", "2%", "90%"], "Only 20% of the population."),
        M("At what age does preschool education in China generally start?", "Three", ["One", "Five", "Seven"], "Generally starts at the age of three."),
        M("How old are children in the 大班 (upper class)?", "5 to 6", ["3 to 4", "4 to 5", "7 to 8"], "大班 5–6 years old."),
        M("What did the page say about per-student spending in China in 2018?", "$5,300, less than one third of other developed countries", ["$15,600, equal to OECD", "$530,000", "Nothing"], "It reached only $5,300 per student."),
        M("Which share of students in big cities can go to college, per the page?", "More than 70%", ["Less than 5%", "About 27%", "100%"], "More than 70%."),
    ],
)

UNIT = unit("第二十九课 中国的教育 Presentation 3: 词汇, Area Studies", [L1, L2])
