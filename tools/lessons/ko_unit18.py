"""Unit 18: KBC Semester 1, Unit 3, Chapter 11 - In Koreatown: Lodging and Dining (코리아타운에서: 숙박과 식사).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 3, Student's Edition (2022).
Audio, video clips, pictures, maps, SMART Board activities, games, role-plays, partner and class activities are
left out. The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation
of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


def _uo(*texts):
    """possessive 의 after a person word is said 에"""
    over = {}
    for t in texts:
        for w in _re.findall(r"[가-힣]+의", t):
            over[w] = _K.pron(w[:-1] + "에")
    return over


# ---- large numbers and decimals
_DG = "공일이삼사오육칠팔구"


def _g4(n):
    """a number below 10,000 in Sino-Korean: 1042 -> 천사십이 (a 1 before 천, 백, 십 is dropped)"""
    out = ""
    for val, unit in ((1000, "천"), (100, "백"), (10, "십")):
        d, n = divmod(n, val)
        if d:
            out += ("" if d == 1 else _DG[d]) + unit
    return out + (_DG[n] if n else "")


def _kn(n):
    """1926508 -> 백구십이만 육천오백팔 (four-digit groups: 조, 억, 만)"""
    if n == 0:
        return "영"
    parts = []
    for name, val in (("조", 10 ** 12), ("억", 10 ** 8), ("만", 10 ** 4)):
        g, n = divmod(n, val)
        if g:
            parts.append(("" if (g == 1 and name == "만") else _g4(g)) + name)
    if n:
        parts.append(_g4(n))
    return " ".join(parts)


def _dec(s, zero="공"):
    """35.19 -> 삼십오점 일구; 0.9 -> 영점 구; 4.08 -> 사점 공팔"""
    a, b = s.split(".")
    return f"{_kn(int(a))}점 " + "".join(zero if c == "0" else _DG[int(c)] for c in b)


def _num_opts(n, k=3):
    """wrong readings of nearby numbers"""
    out = []
    for m in (n * 10, n // 10 + 7, n + 10000, n - 100, n * 100, n + 1000000):
        r = _kn(m)
        if r != _kn(n) and r not in out and m > 0:
            out.append(r)
    return out[:k]


# ================================================================== Topic A
_A_DLG = [
    ("존스 일병", "엘에이에 한국 사람들이 많아요?", "Are there many Korean people in L.A.?"), ("제이슨", "네, 이곳에 교포들이 많이 살아요.", "Yes, many Korean expatriates live here."),
    ("존스 일병", "엘에이 한인 인구가 얼마나 돼요?", "How big is the Korean population of L.A.?"), ("제이슨", "네, 한 삼십만 명쯤 돼요. 대부분 가족 이민이나 유학생으로 많이 왔어요.", "Yes, it is about 300,000. Most came as family immigrants or as international students."),
    ("존스 일병", "그럼 한인 사회 교포 분들은 보통 어떤 일들을 하세요?", "Then what kinds of work do the expatriates of the Korean community usually do?"), ("제이슨", "사업을 하시는 분들이 많아요. 그리고 변호사, 의사, 공무원으로 근무하시는 분들도 계세요.", "Many people run businesses. And there are also people who work as lawyers, doctors and civil servants."),
    ("존스 일병", "그런데 제이슨 씨는 언제 미국에 왔어요?", "By the way, when did you come to the U.S., Jason?"), ("제이슨", "아, 제가 초등학교 일 학년 때 이민 왔어요. 저는 한인 일 점 오 세예요.", "Oh, I immigrated when I was in the first grade of elementary school. I am a 1.5-generation Korean."),
    ("존스 일병", "근데 한국말을 정말 잘하세요.", "But you speak Korean really well."), ("제이슨", "어렸을 때 한글학교를 다녔어요.", "I attended Hangul school when I was young."), ("존스 일병", "아, 그래요?", "Oh, is that so?"),
]
_A_PAIRS = [("곳", "a place"), ("교포", "a Korean living abroad"), ("근무", "duty; work; service"), ("근무하다", "to be on duty; to work; to serve"), ("그럼", "well; then"), ("다니다", "to regularly go to; to attend (school/workplace/church, etc.)"), ("대부분", "most; “large part”"),
            ("만", "ten thousand"), ("사업", "a business"), ("사업하다", "to do business"), ("사회", "a community; a society"), ("세", "a generation"), ("세대", "a generation"), ("정말", "really; truly"), ("어리다", "to be young; to be immature"), ("억", "hundred million"),
            ("유학생", "an international student; a foreign student"), ("이민", "immigration; emigration; expatriation"), ("인구", "population"), ("한글", "Hangul; the Korean alphabet; “Korean writing”"), ("한인", "a Korean expatriate; a Korean (living in the U.S. or abroad); “Korean person”")]
_A_RE = [("재미교포", "Koreans residing in the U.S."), ("재일교포", "Koreans residing in Japan"), ("재중교포", "Koreans residing in China")]
_A_MIN = [("국민", "a people; “people of a country”"), ("시민", "a citizen; “people of a city”"), ("군민", "county people"), ("민병", "a militiaman; “civilian soldier”"), ("이민", "immigration; emigration; “moving of people”")]
_A_GEN = [("한인 일 세(대)", "first-generation Koreans: the first generation in a new country"), ("한인 이 세(대)", "second-generation Koreans"), ("한인 일 점 오 세(대)", "the 1.5 generation: Koreans who immigrated before or during their early teens"), ("한인 삼 세/사 세", "third and fourth generations and up (rapidly increasing as the history of Korean immigration gets longer)")]
L1 = lesson(
    "Ch 11 · Topic A: The Korean community in the U.S.",
    "엘에이에 한국 사람들이 많아요? · 교포 · 한인 일 점 오 세 · 민 (民)",
    requires=[],
    cards=[
        card("Dialog: at a Korean Saturday school in Los Angeles",
             "PFC Jones is talking with PFC Baek’s friend, Jason Park, at a Korean Saturday School in Los Angeles where Jason teaches Korean. The Korean is the book’s, with L.A., 30만 명, 1학년 and 1.5세 spelled out in Hangul (the English is mine).",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary). The book lists ~곳, ~세(대), 근무(하다) and 사업(하다) as groups and 만 and 억 under Numbers; they are split here. -(으)ㄹ 때 and ~(으)로 are explained in their own lessons: -(으)ㄹ 때 is “when; time; at the time of”, and ~(으)로 is “(status) as”, as in 의사로 일하는 한인들이 많아요 (there are many Koreans who work as doctors).",
             tables=[ktable(_A_PAIRS)]),
        card("Footnotes",
             "교포 means Koreans residing abroad. Thus 재미교포 means Koreans residing in the U.S.; 재일교포 means Koreans residing in Japan; and 재중교포 means Koreans residing in China. 근데 is a contracted form of 그런데, which can be translated as but, however, by the way, or and.",
             tables=[ktable(_A_RE)]),
        card("Generations: 한인 일 세, 이 세, 일 점 오 세",
             "The first generation of Koreans in a new country is called 한인 1세(대), and the second generation is called 한인 2세(대). However, Koreans who immigrate to a new country before or during their early teens are called 1.5세(대) (1.5 generation). As the history of Korean immigration gets longer, the third and fourth generations and up (한인 3세/4세 and up) are rapidly increasing. The numbers are read in Sino-Korean: 일 세, 이 세, 일 점 오 세. (The table gives the digits in the first cell and the reading in the cells that are said.)",
             tables=[table(["Term", "Reading", "Meaning"], [["한인 1세(대)", "한인 일 세", "first-generation Koreans"], ["한인 2세(대)", "한인 이 세", "second-generation Koreans"], ["한인 1.5세(대)", "한인 일 점 오 세", "the 1.5 generation: immigrated before or during the early teens"], ["한인 3세/4세", "한인 삼 세, 한인 사 세", "third and fourth generations and up"]], say=[1])]),
        card("Sino-Korean in use: 민 (民)",
             "This Sino-Korean syllable means people, folks, or civil(ian), as in 국민 (a people; “people of a country”), 시민 (a citizen; “people of a city”), 군민 (county people), 민병 (a militiaman; “civilian soldier”) and 이민 (immigration; emigration; “moving of people”). The Core Vocabulary also lists 민요 and 민족 under 민 without meanings; folk song and ethnic group/nation are mine.",
             tables=[ktable(_A_MIN + [("민요", "a folk song (mine)"), ("민족", "an ethnic group; a nation (mine)")])]),
        card("Activities left out",
             "The vocabulary-builder PowerPoint, the two SMART Board activities and the Baseball Game of the Vocabulary Builder, the SMART Board parts of the Presentation Activity, Follow-Up Activity 1 (SMART Board and listening to three statements about country populations) and Follow-Up Activity 2 (listening to statements about Korean immigrants in the United States and writing the percents) are SMART Board, game or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("세대", "근무하다", "사업하다")])
        + _tr(_strip(_A_DLG)[:10]) + _tr(_A_RE) + _tr(_A_MIN)
        + [M("What does 한인 일 점 오 세 mean?", "the 1.5 generation (immigrated in the early teens or before)", ["the first generation", "the second generation", "the third generation"], "Immigrated before or during the early teens."), M("What does 재미교포 mean?", "Koreans residing in the U.S.", ["Koreans residing in Japan", "Koreans residing in China", "Americans in Korea"], "재미 = in America."),
           M("What does 재일교포 mean?", "Koreans residing in Japan", ["Koreans residing in the U.S.", "Koreans residing in China", "Japanese in Korea"], "재일 = in Japan."), M("What does 재중교포 mean?", "Koreans residing in China", ["Koreans residing in the U.S.", "Koreans residing in Japan", "Chinese in Korea"], "재중 = in China."),
           M("Which syllable means people, folks or civil(ian)?", "민 (民)", ["비 (費)", "실 (室)", "구 (口)"], "국민, 시민, 군민, 민병, 이민."), M("What does 그런데 mean in 근데?", "but; however; by the way; and", ["because", "therefore", "if"], "근데 is the contracted form of 그런데."),
           M("Where did Jason teach Korean?", "At a Korean Saturday School in Los Angeles", ["At a hotel", "At a restaurant", "At the Defense Language Institute"], "Topic A, the heading."), M("When did Jason immigrate?", "When he was in the first grade of elementary school", ["As a college student", "Last year", "After the army"], "초등학교 일 학년 때 이민 왔어요."),
           M("How big is the Korean population of L.A. according to Jason?", "About 300,000", ["About 30,000", "About 3 million", "About 3,000"], "한 삼십만 명쯤."), M("What kind of work do many Korean expatriates do, according to Jason?", "They run businesses", ["They are all students", "They are only teachers", "They do not work"], "사업을 하시는 분들이 많아요."),
           M("Why does Jason speak Korean well?", "He attended Hangul school when he was young", ["He lives in Korea", "His teacher is Korean", "He studied at DLI"], "어렸을 때 한글학교를 다녔어요."),
           F("제가 초등학교 일 학년 ___ 이민 왔어요. (when)", "때", ["곳", "만"], "때 = time."), F("한인 사회에는 변호사, 의사, 공무원으로 ___ 분들도 계세요. (work)", "근무하시는", ["공부하시는", "이민하시는"], "근무하다 = to work."),
           F("엘에이 한인 ___가 얼마나 돼요? (population)", "인구", ["사회", "이민"], "인구 = population."), F("___ 제이슨 씨는 언제 미국에 왔어요? (By the way)", "그런데", ["그래서", "그리고"], "그런데 = by the way."), F("한 삼십___ 명쯤 돼요. (ten thousand)", "만", ["억", "천"], "만 = ten thousand."),
           read_q("교포"), read_q("한인"), read_q("유학생"), read_q("이민"), read_q("한글학교를")]
    ),
)

# ================================================================== Large numbers and decimals
_BIGEX = [304257284567, 1926508, 557491, 144002, 109926, 105694, 231147, 108693, 93825, 60400, 300000, 13000, 100000000, 30000, 250000000]
_DECEX = ["35.19", "0.9", "0.7", "4.08", "3.1", "1.5", "12.5", "6.02", "2.34"]
L2 = lesson(
    "Ch 11 · Large numbers and decimals",
    "만 · 억 · 조 · 삼십오점 일구 · 영점 구 · 사점 공팔",
    requires=[],
    cards=[
        card("How to read large numbers",
             "In the U.S. we separate every three digits with a comma and name each three-digit group thousand, million, billion, trillion, etc. 304,257,284,567 reads “three hundred four billion, two hundred fifty-seven million, two hundred eighty-four thousand, five hundred sixty-seven.” In Korean we break a number into four-digit groups and name each four-digit group based on 만 (10,000), 억 (100,000,000), 조 (1,000,000,000,000), etc.; however, commas still separate every three digits when a number is in Arabic numerals. The same number is therefore read in four-digit groups: 3,042 억 5,728 만 4,567.",
             tables=[table(["Group", "Digits", "Reading"], [["억 (hundred million; 100,000,000)", "3,042", "삼천사십이억"], ["만 (ten thousand; 10,000)", "5,728", "오천칠백이십팔만"], ["the rest", "4,567", "사천오백육십칠"], ["The whole number", "304,257,284,567", _kn(304257284567)]], say=[2]),
                     table(["Thousands", "Hundreds", "Tens", "Units"], [["천 (1,000)", "백 (100)", "십 (10)", "일, 이, 삼 …"]], note="Inside a four-digit group the digits are read thousands-hundreds-tens-units; the book writes 3천4십2억 5천7백2십8만 4천5백6십7 (a digit 1 before 천, 백, 십 is not read: 천, 백, 십).")]),
        card("Large numbers from the book and from the chapter",
             "The readings below follow the four-digit rule (the book’s own readings are 백구십이만 육천오백팔 for 1,926,508 and 육만 사백 for 60,400; the others are mine, worked out with the same rule). A 1 before 만 is not read (만), but a 1 before 억 or 조 is (일억, 일조).",
             tables=[table(["Number", "Reading"], [[f"{n:,}", _kn(n)] for n in _BIGEX], say=[1])]),
        card("How to read decimals",
             "In English, 35.19 is read as “thirty-five point one nine.” Reading decimals in Korean is quite similar. “Point” is read as 점, whose literal meaning is a point or a period. Therefore 35.19 is read as 삼십오점 일구. However, there are some decimal values you should be careful with. For example, .9 and .7 are always rendered as 0.9 or 0.7 in Korean and, therefore, are read as 영점 구 and 영점 칠, respectively. When the number 0 comes after a decimal point, 0 can be read as either 공 or 영; 4.08, for example, is read as 사점 공팔 or 사점 영팔.",
             tables=[table(["Number", "Reading"], [[d, _dec(d)] for d in _DECEX[:5]] + [["4.08 (the other way)", _dec("4.08", "영")]] + [[d, _dec(d)] for d in _DECEX[5:]], say=[1])]),
        card("Percentages",
             "The book reads percent as 퍼센트 after the number, as in the Activity 3 model: 삼점일 퍼센트 (3.1%) and, in Follow-Up Activity 3 of Topic A, 사십오 퍼센트 (45%).",
             examples=[D("삼점일 퍼센트입니다.", "It is 3.1 percent."), D("사십오 퍼센트 정도가 사업을 합니다.", "About 45 percent run a business."), D("미국 인구는 삼억쯤 됩니다.", "The U.S. population is about 300 million."), D("몬트레이 인구는 삼만쯤 됩니다.", "The population of Monterey is about 30,000."), D("중국 인구가 십삼억입니다.", "The population of China is 1.3 billion.")]),
    ],
    exercises=uniq(
        [M(f"How do you read {n:,}?", _kn(n), _num_opts(n), f"{n:,} → {_kn(n)}.") for n in _BIGEX if n >= 10000]
        + [M(f"How do you read {d}?", _dec(d), [_dec(x) for x in _DECEX if x != d][:3], f"{d} → {_dec(d)}.") for d in _DECEX]
        + [M("What does 만 mean as a number?", "10,000", ["1,000", "100,000", "1,000,000"], "만 = ten thousand."), M("What does 억 mean as a number?", "100,000,000", ["10,000", "1,000,000,000", "1,000,000"], "억 = hundred million."), M("What does 조 mean as a number?", "1,000,000,000,000", ["100,000,000", "10,000", "1,000,000"], "조 = trillion."),
           M("How does Korean group the digits of a large number when it names them?", "In groups of four (만, 억, 조)", ["In groups of three", "In groups of two", "One by one"], "Four-digit groups."), M("What is 점?", "the word for “point” in a decimal", ["percent", "ten thousand", "zero"], "삼십오점 일구 = 35.19."),
           M("How can the 0 in 4.08 be read?", "공 or 영", ["일 or 이", "삼 or 사", "only 십"], "사점 공팔 or 사점 영팔."), M("How is 0.9 read?", "영점 구", ["공점 구", "일점 구", "구점 영"], "0.9 is 영점 구."),
           F("삼십오___ 일구 (35.19)", "점", ["만", "억"], "점 = point."), F("육___ 사백 명입니다. (60,400)", "만", ["억", "천"], "60,400 = 6 만 400."), F("미국 인구는 삼___쯤 됩니다. (300 million)", "억", ["만", "조"], "3억 = 삼억."),
           read_q("백구십이만 육천오백팔"), read_q("영점 구"), read_q("삼십오점 일구"), read_q("삼억")]
    ),
)


# ================================================================== Activities A
_ACT1 = [("사업", "(a) business; entrepreneurship"), ("인구", "population"), ("교회", "church"), ("한인", "Korean people (in the U.S.)"), ("가르치다", "to teach"), ("유학생", "an international student"), ("근무하다", "to work")]
_ART1 = [
    ("미국에 한국 사람이 많이 삽니다.", "Many Korean people live in the U.S."), ("한국 사람들은 미국에 이민 오기 전에 보통 의사, 간호사, 선생님, 공무원, 엔지니어, 은행원 등으로 근무했습니다.", "Before immigrating to the U.S., Korean people usually worked as doctors, nurses, teachers, civil servants, engineers, bank clerks and so on."),
    ("하지만 미국에 이민 온 후에 많은 사람들이 직업을 바꿉니다.", "But after immigrating to the U.S., many people change their jobs."), ("이민 일 세들은 미국 여러 곳에 코리아타운을 만들었습니다.", "The first-generation immigrants made Koreatowns in many places in the U.S."),
    ("거기에서 여러 가지 사업을 합니다.", "There they do various kinds of business."), ("재미교포 일 세들은 사십오 퍼센트 정도가 세탁소, 슈퍼마켓, 식당 등 사업을 합니다.", "About 45 percent of the first-generation Korean Americans run businesses such as cleaners, supermarkets and restaurants."),
    ("그러나 많은 한인 일 점 오 세와 이 세들은 의사, 간호사, 변호사, 회사원, 엔지니어, 공무원 등으로 다양한 일을 합니다.", "But many 1.5- and second-generation Koreans do a variety of jobs, as doctors, nurses, lawyers, company employees, engineers, civil servants and so on."),
]
_CEN_HEAD = f"재미교포 인구 {_kn(1926508).split('만')[0]}만 명… 캘리포니아주에 {_kn(557491).split('만')[0]}만 칠천여 명 거주"
_CEN = [
    (f"연방 인구센서스국이 발표한 {year_ko(2016)}부터 {year_ko(2020)}까지 아메리칸커뮤니티서베이(에이씨에스)에 따르면 {year_ko(2020)} 기준 재미교포 인구가 {_kn(1926508)} 명이다.", "According to the American Community Survey (ACS) of 2016 to 2020, published by the U.S. Census Bureau, the Korean-American population was 1,926,508 as of 2020."),
    (f"재미교포 인구가 가장 많은 곳은 캘리포니아 주로 {_kn(557491)} 명이다.", "The place with the largest Korean-American population is the state of California, with 557,491."),
    (f"주 내 한인은 로스앤젤레스(엘에이) 카운티는 {_kn(231147)} 명이고 오렌지 카운티는 {_kn(108693)} 명이다.", "Within the state, there are 231,147 Koreans in Los Angeles (LA) County and 108,693 in Orange County."),
    (f"뉴욕주 한인은 {_kn(144002)} 명, 뉴저지주는 {_kn(105694)} 명, 텍사스주는 {_kn(109926)} 명, 버지니아주는 {_kn(93825)} 명 등이다.", "Koreans in the state of New York number 144,002, New Jersey 105,694, Texas 109,926, Virginia 93,825, and so on."),
]
_MAP = [("A", "메릴랜드 한인 인구는 얼마입니까?", "What is the Korean population of Maryland?"), ("B", "육만 사백 명입니다.", "It is 60,400."), ("A", "몇 퍼센트입니까?", "What percent is that?"), ("B", "삼점일 퍼센트입니다.", "It is 3.1 percent.")]
_CEN_T = [("1,926,508", "the Korean population in the U.S.", 1926508), ("557,491", "the Korean population in California", 557491), ("144,002", "the Korean population in New York", 144002), ("109,926", "the Korean population in Texas", 109926), ("105,694", "the Korean population in New Jersey", 105694),
          ("231,147", "the Korean population in Los Angeles County (not in the book’s table)", 231147), ("108,693", "the Korean population in Orange County (not in the book’s table)", 108693), ("93,825", "the Korean population in Virginia (not in the book’s table)", 93825)]
L3 = lesson(
    "Ch 11 · Activities A: Korean Americans in numbers",
    "사업 · 인구 · 교회 · 한인 · 재미교포 인구 백구십이만 명 · 메릴랜드 한인 인구는 얼마입니까?",
    requires=[],
    cards=[
        card("Activity 1a: match the word with its English",
             "The book asks you to draw a line from each Korean word to its English equivalent. The answers are below (the English is the book’s).",
             tables=[ktable(_ACT1)]),
        card("Follow-Up Activity 3 (Reading): occupations of Korean immigrants",
             "The book’s article about the occupations of Korean immigrants in the U.S., with 45%, 1세 and 1.5세 spelled out in Hangul (the English is mine). 다양한 means “various”, as the book glosses.",
             examples=passage(_ART1)),
        card("The article: the table filled in",
             "My key to the book’s table (jobs of first-generation immigrants before and after immigration, and jobs of the 1.5- and second-generation citizens).",
             tables=[table(["Jobs of 1st-generation immigrants: pre-immigration", "Jobs of 1st-generation immigrants: post-immigration", "Jobs of 1.5- and 2nd-generation citizens"], [["Doctors, nurses, teachers, civil servants, engineers, bank clerks", "Businesses such as cleaners, supermarkets and restaurants (about 45 percent)", "Doctors, nurses, lawyers, company employees, engineers, civil servants, and other jobs"]])]),
        card("Activity 2 (Reading): the Korean population in the U.S.",
             "The book shows a news article (from Yonhap News) from the U.S. Census Bureau about the Korean population in the U.S. and asks you to write what the numbers represent and how they are written in Korean; the first row is done for you (1,926,508 → 백구십이만 육천오백팔). The headline reads 재미교포 인구 192만명…캘리포니아주에 55만 7천여 명 거주. The article is the book’s, with the numbers, ACS and LA spelled out in Hangul (the English is mine; the “see the numbers” hint tells you to ignore unknown words).",
             examples=[D(_CEN_HEAD, "The Korean-American population is 1.92 million… about 557,000 live in California")] + passage(_CEN)),
        card("The census numbers: how they are read",
             "The book’s table has the first five numbers; the readings of the other rows are mine, worked out with the four-digit rule.",
             tables=[table(["Number", "What it represents", "How it is written in Korean"], [[a, b, _kn(n)] for a, b, n in _CEN_T], say=[2])]),
        card("Activity 3 (Reading and speaking): population by state",
             "In the book, each partner has a map showing the Korean population of different states and the percentage of the total Korean population in the U.S., and asks for the missing information. The model is below (the book writes the numbers 60,400 and 3.1%; the English is mine).",
             examples=dlg(_MAP)),
        card("Activities left out",
             "Activity 1b (a radio show Q&A about Koreans in the U.S., listening and filling in a summary; the book’s worked example is: “What are the occupations of Koreans in the U.S.? Businesses (cleaners/grocery stores) – 43.5%; lawyers/doctors – 21.4%”) is audio. The maps of Activity 3 are pictures and the partner work is not reproduced."),
    ],
    exercises=uniq(
        vocab_exercises([(k, e) for k, e in _ACT1])
        + _tr(_strip(_MAP)) + _tr(_ART1[:7])
        + [M(f"What does {n} represent in the census article?", e.split("in ", 1)[1].replace("the U.S.", "the U.S.") if False else e[4:] if False else e, [x[1] for x in _CEN_T if x[1] != e][:3], f"{n} = {e}.") for n, e, _ in _CEN_T[:5]]
        + [M(f"How is {n} read?", _kn(v), _num_opts(v), f"{n} → {_kn(v)}.") for n, _, v in _CEN_T]
        + [M("Which state has the largest Korean-American population?", "California", ["New York", "Texas", "New Jersey"], "557,491 in California."), M("About what share of first-generation Korean Americans run businesses such as cleaners and supermarkets?", "About 45 percent", ["About 4.5 percent", "About 100 percent", "About 14 percent"], "사십오 퍼센트 정도."),
           M("What do many people do after immigrating, according to the article?", "They change their jobs", ["They stop working", "They go back to Korea", "They keep the same job"], "직업을 바꿉니다."), M("What is the Korean-American population in the U.S. as of 2020?", "1,926,508", ["557,491", "144,002", "60,400"], "백구십이만 육천오백팔 명."),
           F("재미교포 인구가 가장 많은 ___은 캘리포니아 주입니다. (place)", "곳", ["때", "만"], "곳 = place."), F("메릴랜드 한인 인구는 ___입니까? (how much)", "얼마", ["언제", "누구"], "얼마입니까 = how much is it?"), F("___ 퍼센트입니까? (how many)", "몇", ["얼마", "누구"], "몇 퍼센트 = what percent."),
           read_q("백구십이만 명"), read_q("이민 일 세들은"), read_q("메릴랜드"), read_q("카운티는")]
    ),
)

# ================================================================== Topic B: the hotel
_B_DLG1 = [
    ("호텔 직원", "어서 오세요. 어떻게 도와드릴까요?", "Welcome. How can I help you?"), ("김 이병", "안녕하세요? 빈 방이 있습니까?", "Hello. Do you have a vacant room?"), ("호텔 직원", "네, 있습니다. 언제까지 묵으시겠어요?", "Yes, we do. Until when will you stay?"),
    ("김 이병", "사흘 동안 묵고 싶어요. 숙박비가 얼마예요?", "I want to stay for three days. How much is the lodging fee?"), ("호텔 직원", "일반실은 하루에 백이십 달러입니다.", "A standard room is 120 dollars a day."),
    ("김 이병", "그 방으로 두 개 주세요. 그리고 이 호텔에 수영장이 있습니까?", "Please give me two of that room. And does this hotel have a swimming pool?"), ("호텔 직원", "네, 일 층 비상구 옆에 있습니다.", "Yes, it is next to the emergency exit on the first floor."),
]
_B_DLG2 = [
    ("호텔 직원", "프런트데스크입니다. 무엇을 도와드릴까요?", "This is the front desk. What can I help you with?"), ("존스 일병", "여기 삼백삼 호입니다. 욕실에 수건이 더 필요해요.", "This is room 303. We need more towels in the bathroom."), ("호텔 직원", "네, 알겠습니다.", "Yes, certainly."),
    ("존스 일병", "그리고 옆 방이 시끄러워요. 다른 방으로 옮기고 싶어요.", "And the room next door is noisy. I want to move to another room."), ("호텔 직원", "잠시만요… 지금 팔백십 호가 비었습니다. 그 방으로 옮기시겠습니까?", "Just a moment… Room 810 is vacant now. Would you like to move to that room?"), ("존스 일병", "네, 감사합니다.", "Yes, thank you."),
]
_B_PAIRS = [("깨끗하다", "to be clean"), ("다르다", "to be different"), ("달러", "dollar"), ("더럽다", "to be dirty"), ("돕다", "to help"), ("무료", "free of charge; “no fare”"), ("묵다", "to stay; to lodge"), ("비다", "to be empty; to be vacant"), ("비상구", "an emergency exit; “emergency mouth”"),
            ("서비스", "service"), ("수건", "a towel"), ("수영장", "a swimming pool; “swimming place”"), ("숙박비", "lodging fee"), ("스위트룸", "a suite (in a hotel)"), ("시끄럽다", "to be noisy; to be loud"), ("옮기다", "to move; to transfer"), ("욕실", "a bathroom"), ("이용", "use"), ("이용하다", "to use; to utilize"),
            ("일반실", "a standard room; “general room”"), ("체크아웃", "checkout"), ("체크아웃하다", "to check out"), ("체크인", "check-in"), ("체크인하다", "to check in"), ("필요하다", "to be needed; to be necessary"), ("프런트", "the front (reception) desk"), ("프런트데스크", "the front desk"),
            ("할인", "discount"), ("할인하다", "to discount"), ("할인받다", "to get a discount"), ("호", "a (room or apartment unit) number"), ("호텔", "a hotel")]
_B_BI = [("숙박비", "lodging fee"), ("택시비", "taxi fare (mine)"), ("학비", "school expenses; tuition (mine)")]
_B_SIL = [("침실", "a bedroom"), ("거실", "a living room"), ("세탁실", "a laundry room (mine)"), ("화장실", "a restroom; a bathroom (mine)"), ("교실", "a classroom (mine)")]
_B_KEY = [("빈 방이 있습니까?", "Do you have a vacant room?"), ("사흘 동안 묵고 싶어요.", "I want to stay for three days."), ("숙박비가 얼마예요?", "How much is the lodging fee?"), ("이 호텔에 수영장이 있습니까?", "Does this hotel have a swimming pool?"),
          ("욕실에 수건이 더 필요해요.", "I need more towels in the bathroom."), ("옆 방이 시끄러워요.", "The room next door is noisy."), ("다른 방으로 옮기고 싶어요.", "I want to move to another room."), ("방이 더러워요.", "The room is dirty. (from Activity 1 of this chapter)")]
L4 = lesson(
    "Ch 11 · Topic B: Welcome. How can I help you?",
    "빈 방이 있습니까? · 숙박비가 얼마예요? · 옆 방이 시끄러워요 · 비 (費) · 실 (室)",
    requires=[],
    cards=[
        card("Part I: checking in at the Olympic Hotel",
             "PV2 Kim is checking in at the front desk of the Olympic Hotel in Koreatown in L.A. The Korean is the book’s, with 120달러, 2개 and 1층 spelled out in Hangul (the English is mine).",
             examples=dlg(_B_DLG1)),
        card("Part II: requests and complaints",
             "PFC Jones is calling the hotel front desk with requests and complaints (the book writes 303호 and 810호; spelled out here as 삼백삼 호 and 팔백십 호).",
             examples=dlg(_B_DLG2)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary). The book lists 이용(하다), 체크아웃(하다), 체크인(하다), 프런트(데스크) and 할인(하다/받다) as groups and ~호 with a tilde; they are split here. The verb suffix 겠 has its own lesson.",
             tables=[ktable(_B_PAIRS)]),
        card("Key sentences for a hotel stay",
             "Sentences from the dialogs (and one from Activity 1) that you need to ask for a room and to make requests and complaints. The English is mine.",
             examples=[D(a, b) for a, b in _B_KEY]),
        card("Sino-Korean in use: 비 (費)",
             "This Sino-Korean syllable means expense or fee. The book asks you to guess the meaning of 숙박비, 택시비 and 학비; the answers are below (숙박비 is the lodging fee of the Core Vocabulary; the other two answers are mine).",
             tables=[ktable(_B_BI)]),
        card("Sino-Korean in use: 실 (室)",
             "This Sino-Korean syllable means a room or chamber, as in 침실 (a bedroom) and 거실 (a living room). The book asks you to guess 세탁실, 화장실 and 교실; the answers are mine.",
             tables=[ktable(_B_SIL)]),
        card("Role-play plan (Presentation Activity d)",
             "Pair up: one partner plays two customers (PV2 Kim for Part I and PFC Jones for Part II), the other the hotel clerk. As a customer: ask about rooms available for ( ) nights and the room rate; ask about a swimming pool; make a complaint about noise from the next room; make requests for more towels. As a hotel clerk: a hotel room costs ( ) dollars per night; the swimming pool is located next to the emergency exit on the ground floor; accept the customer’s request for a room change. The role-play itself is a partner activity and is not reproduced."),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity and Follow-Up Activity 2 (listening to three conversations at a hotel’s front desk and filling in the duration of stay, room rate and accommodations) are SMART Board or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, e) for k, e in _B_PAIRS if k not in ("이용", "체크아웃", "체크인", "프런트데스크", "할인", "호")])
        + _tr(_strip(_B_DLG1)) + _tr(_strip(_B_DLG2)[:5]) + _tr(_B_KEY) + _tr(_B_SIL[:2])
        + [M("What does 비 (費) mean?", "expense; fee", ["a room", "people", "a mouth"], "숙박비, 택시비, 학비."), M("What does 실 (室) mean?", "a room; chamber", ["expense; fee", "people", "a mouth"], "침실, 거실, 세탁실."), M("What is the meaning of 숙박비?", "lodging fee", ["a hotel", "a bathroom", "a swimming pool"], "숙박 + 비."),
           M("Which is the standard room price in the dialog?", "120 dollars a day", ["12 dollars a day", "1,200 dollars a day", "210 dollars a day"], "하루에 백이십 달러."), M("How long does PV2 Kim want to stay?", "Three days", ["Two days", "A week", "One night"], "사흘 동안."), M("Where is the swimming pool?", "Next to the emergency exit on the first floor", ["On the roof", "In the basement", "Next to the lobby"], "일 층 비상구 옆."),
           M("What room is PFC Jones in?", "Room 303", ["Room 810", "Room 330", "Room 130"], "삼백삼 호."), M("Which room is vacant now?", "Room 810", ["Room 303", "Room 180", "Room 308"], "팔백십 호가 비었습니다."), M("What does PFC Jones need more of?", "Towels", ["Pillows", "Soap", "Chairs"], "수건이 더 필요해요."),
           M("Why does PFC Jones want to move?", "The next room is noisy", ["The room is dirty", "The room is expensive", "The room is small"], "옆 방이 시끄러워요."),
           F("숙박비가 ___예요? (how much)", "얼마", ["언제", "누구"], "얼마예요 = how much is it?"), F("욕실에 수건이 더 ___. (are needed)", "필요해요", ["깨끗해요", "비었어요"], "필요하다 = to be needed."), F("옆 방이 ___. (noisy)", "시끄러워요", ["깨끗해요", "필요해요"], "시끄럽다 = to be noisy."),
           F("다른 방으로 ___ 싶어요. (to move)", "옮기고", ["이용하고", "묵고"], "옮기다 = to move."), F("빈 방이 ___? (Is there)", "있습니까", ["갑니까", "합니까"], "있습니까 = is there?"), F("택시___ (taxi fare)", "비", ["실", "민"], "비 = fee."), F("화장___ (restroom)", "실", ["비", "민"], "실 = room."),
           read_q("숙박비"), read_q("수영장"), read_q("일반실"), read_q("옮기고 싶어요"), read_q("프런트데스크")]
    ),
)

# ================================================================== Activities B
_AD = [
    ("스키, 골프를 즐길 수 있는 사우스 레이크 타호 스키 리조트, 하나 콘도로 오세요.", "Come to Hana Condo at the South Lake Tahoe ski resort, where you can enjoy skiing and golf."), ("겨울 방학 할인을 합니다.", "We give a winter break discount."), ("그리고 가족여행 할인도 있습니다.", "And there is also a family trip discount."),
    ("한국말과 영어로 예약할 수 있습니다.", "You can make a reservation in Korean and English."), ("하나 콘도 소개", "Introduction of Hana Condo"), ("가격: 주중 하루 백팔십 달러, 주말 이백오십 달러", "Price: 180 dollars a day on weekdays, 250 dollars on weekends"),
    ("위치: 헤븐리 스키 리조트 옆", "Location: next to the Heavenly Ski Resort"), ("시설 및 서비스: 피트니스 센터, 수영장, 무료 인터넷 서비스", "Facilities and services: fitness center, swimming pool, free internet service"),
]
_REV1 = [
    ("저는 작년 크리스마스 사흘 동안 하나 콘도에서 숙박했어요.", "I stayed at Hana Condo for three days last Christmas."), ("스키장이 바로 옆에 있어서 좋았습니다.", "It was good because the ski area was right next door."), ("그리고 숙박비도 다른 호텔보다 많이 싸요.", "And the lodging fee is much cheaper than at other hotels."),
    ("참, 군인은 십 퍼센트 할인도 받을 수 있어요.", "Oh, and military personnel can also get a 10 percent discount."), ("그렇지만 사람이 너무 많아 시끄럽고 좀 더러웠어요.", "However, there were too many people, so it was noisy and a bit dirty."),
    ("그리고 하루 더 묵고 싶었지만 방이 없었습니다.", "And I wanted to stay one more day, but there was no room."), ("레이크 타호에 가실 분들, 가실 때는 꼭 미리 예약을 하세요.", "To those who will go to Lake Tahoe: when you go, be sure to make a reservation in advance."),
]
_REV2 = [
    ("저는 매년 레이크 타호로 스키 여행을 갑니다.", "I go on a ski trip to Lake Tahoe every year."), ("올해는 가족과 함께 나흘 동안 하나 콘도에 묵었습니다.", "This year I stayed at Hana Condo for four days with my family."), ("콘도도 깨끗하고 직원들도 아주 친절했습니다.", "The condo was clean and the staff were very kind."),
    ("수영장도 있고 인터넷도 무료로 이용할 수 있습니다.", "There is a swimming pool, and you can use the internet for free."), ("하지만 수영장이 작고 사람이 많습니다.", "But the pool is small and there are many people."), ("그리고 욕실에 수건이 없습니다.", "And there are no towels in the bathroom."),
    ("꼭 가져 가세요.", "Be sure to take them with you."), ("저는 내년에도 다시 방문하고 싶습니다.", "I want to visit again next year too."),
]
_MATCH = [("방이 있습니까?", "지금 빈 방이 없습니다."), ("방이 더러워요.", "그럼 방을 옮기시겠습니까?"), ("이 호텔에 수영장이 있습니까?", "네, 일 층 비상구 옆에 있습니다."), ("옆 방이 시끄러워요.", "그럼 방을 옮기시겠습니까?")]
L5 = lesson(
    "Ch 11 · Activities B: a condo ad and two hotel reviews",
    "하나 콘도 · 호텔 이용후기 · 방이 있습니까? · 옆 방이 시끄러워요",
    requires=[],
    cards=[
        card("Activity 1a: customer questions and the clerk’s responses",
             "The book asks you to match each customer question or complaint with the appropriate response; some may have multiple answers. My key: the second and fourth complaints (dirty room, noisy next room) can both be answered with the offer to move rooms.",
             tables=[table(["Customer", "Response"], [[a, b] for a, b in _MATCH], say=[0, 1])]),
        card("Follow-Up Activity 1 (Reading): the hotel ad",
             "The book asks you to read the hotel ad, write three things that attract you (room rate, services, facilities, etc.) and complete a table. The ad is the book’s, with South Lake Tahoe spelled out in Hangul and the prices spelled out; the telephone number and the dollar signs are left out (the English is mine). The book’s text has the words 옆 and 시설 run together by a layout glitch; they are separated here.",
             examples=passage(_AD)),
        card("The ad: the table filled in",
             "My key to the book’s table. Which three things attract you is up to you.",
             tables=[table(["Information", "Details"], [["Discount offers", "A winter break discount and a family trip discount"], ["Price", "Weekdays $180 a day; weekends $250"], ["Facilities and services", "A fitness center, a swimming pool, free internet service"], ["Location", "Next to the Heavenly Ski Resort"], ["Reservations", "In Korean and English"]])]),
        card("Activity 2 (Reading): two hotel reviews",
             "You are planning to spend the Christmas holidays at Lake Tahoe and are looking on a local Korean community website for a hotel or a condo. The book shows two reviews posted by guests; the book asks you to fill in a table in English (duration of stay, positive and negative comments). The reviews are the book’s, with 10% spelled out in Hangul; the header lines with the guests’ names, IP addresses and dates are left out (the English is mine).",
             examples=[D("호텔 이용후기", "Hotel review"), D("기주 씨의 후기", "Kijoo’s review (mine)")] + passage(_REV1) + [D("수영 씨의 후기", "Sooyoung’s review (mine)")] + passage(_REV2)),
        card("The reviews: the table filled in",
             "My key to the book’s table.",
             tables=[table(["Guest", "Duration of stay", "Positive comments", "Negative comments"], [["Kijoo", "Three days (last Christmas)", "The ski area is right next door; the lodging fee is much cheaper than other hotels; military personnel get a 10 percent discount", "Too many people, so it was noisy and a bit dirty; he wanted to stay one more day but there was no room"],
                                                                                           ["Sooyoung", "Four days (this year, with her family)", "The condo is clean; the staff are very kind; there is a swimming pool; free internet", "The pool is small and there are many people; there are no towels in the bathroom (bring them)"]])]),
        card("Activities left out",
             "Activity 1b (listening to phone conversations of complaints from hotel guests and filling in the complaint and the solution), Activity 2b (pair talk about which hotel you would like to stay at and why) and Activity 3 (role-play of a hotel guest and a receptionist, Situation A: a businessperson making a hotel reservation over the phone; Situation B: calling the front desk to make complaints, with role cards) are audio or partner activities."),
    ],
    exercises=uniq(
        _tr(_AD[:4] + _AD[5:]) + _tr(_REV1[:6]) + _tr(_REV2[:7])
        + [M(f"A hotel guest says: {q} What is the clerk’s response?", r, [x for _, x in _MATCH if x != r][:2] + ["네, 알겠습니다."], "The book’s matching answer.") for q, r in _MATCH[:1] + _MATCH[2:3]]
        + [M("How much is Hana Condo on weekdays?", "$180 a day", ["$250 a day", "$18 a day", "$120 a day"], "주중 하루 백팔십 달러."), M("How much is Hana Condo on weekends?", "$250", ["$180", "$25", "$120"], "주말 이백오십 달러."), M("Which two discounts does the ad offer?", "A winter break discount and a family trip discount", ["A student discount and a military discount", "A summer discount and a weekday discount", "A senior discount and a group discount"], "겨울 방학 할인; 가족여행 할인."),
           M("How long did Kijoo stay?", "Three days", ["Two days", "Four days", "A week"], "사흘 동안."), M("How long did Sooyoung stay?", "Four days", ["Three days", "Two days", "A week"], "나흘 동안."), M("What discount can military personnel get, according to Kijoo?", "10 percent", ["15 percent", "20 percent", "50 percent"], "군인은 십 퍼센트 할인."),
           M("What was a negative point for Sooyoung?", "No towels in the bathroom", ["The staff were unkind", "The condo was dirty", "No internet"], "욕실에 수건이 없습니다."), M("What was a positive point for Kijoo?", "The ski area is right next door", ["The pool is large", "The staff are kind", "Free breakfast"], "스키장이 바로 옆에 있어서 좋았습니다."),
           M("What does Kijoo advise people going to Lake Tahoe?", "Make a reservation in advance", ["Bring towels", "Go in summer", "Stay at a motel"], "꼭 미리 예약을 하세요."), M("Which review says the condo is clean?", "Sooyoung’s", ["Kijoo’s", "Both", "Neither"], "콘도도 깨끗하고."),
           F("레이크 타호에 가실 때는 꼭 ___ 예약을 하세요. (in advance)", "미리", ["다시", "아직"], "미리 = in advance."), F("그리고 숙박비도 다른 호텔___ 많이 싸요. (than)", "보다", ["에서", "하고"], "~보다 = than."), F("인터넷도 ___로 이용할 수 있습니다. (free)", "무료", ["할인", "서비스"], "무료 = free of charge."),
           read_q("하나 콘도"), read_q("스키장이"), read_q("친절했습니다"), read_q("할인도")]
    ),
)


# ================================================================== Grammar A: -(으)ㄹ 때
def _ttae(v):
    """-(으)ㄹ 때: 자다 -> 잘 때, 먹다 -> 먹을 때, 춥다 -> 추울 때"""
    if v in _B_IRR_T:
        return _B_IRR_T[v]
    return can_(v)[:-1] + "때"


_B_IRR_T = {"춥다": "추울 때", "덥다": "더울 때", "어렵다": "어려울 때", "쉽다": "쉬울 때", "가깝다": "가까울 때"}
_T_EX = [("숙제할 때 티브이를 안 봅니다.", "When I do my homework, I don’t watch TV."), ("날씨가 좋을 때 운동합니다.", "When the weather is good, I work out."), ("심심할 때 게임을 해요.", "When I am bored, I play games."), ("심심할 때 게임을 할 거예요.", "When I am bored (in the future), I will play games."),
         ("심심할 때 게임을 했어요.", "When I was bored, I played games.")]
_T_NP = [("학교에 갈 때부터", "from the time (when) I go to school"), ("학교에 갈 때까지", "until the time (when) I go to school"), ("학교에 갈 때마다", "every time (when) I go to school")]
_T_NT = [("점심 때", "at lunchtime or early in the afternoon"), ("크리스마스 때", "during Christmas"), ("저녁 때", "at dinnertime or during evening time")]
_T_RULE = [("자다", "잘 때"), ("심심하다", "심심할 때"), ("있다", "있을 때"), ("먹다", "먹을 때")]
_T_MATCH = [("영화 볼 때", "팝콘을 먹습니다.", "When I watch a movie, I eat popcorn."), ("피곤할 때", "방에서 쉽니다.", "When I am tired, I rest in my room."), ("날씨가 좋을 때", "등산을 갑니다.", "When the weather is good, I go hiking."),
            ("모르는 단어가 있을 때", "사전을 봅니다.", "When there is a word I don’t know, I look in the dictionary."), ("날씨가 쌀쌀할 때", "코트를 입습니다.", "When the weather is chilly, I wear a coat.")]
_T_VERBS = ["자다", "가다", "보다", "하다", "공부하다", "먹다", "있다", "읽다", "좋다", "심심하다", "피곤하다", "살다", "만들다", "알다", "춥다", "배우다", "마시다"]
_T_SENT = [("저는 보통 피곤할 때 사우나를 합니다.", "I usually go to the sauna when I am tired."), ("저는 어렸을 때 미국으로 이민 왔습니다.", "I immigrated to America when I was young."), ("저는 열 살 때 미국으로 이민 왔습니다.", "I immigrated to America when I was ten years old."),
           ("더울 때는 시원한 음료수를 마시고 싶어요.", "When it is hot, I want to drink a refreshing beverage.")]
_T_F5 = [("컴퓨터를 씁니다.", "이메일을 보낼 때, 가족과 채팅을 할 때", "when I send e-mail, when I chat with my family (the book’s model)"), ("전화를 합니다.", "친구가 보고 싶을 때, 길을 잃을 때", "when I miss my friend, when I get lost (mine)"), ("방에서 잡니다.", "피곤할 때, 밤에 집에 있을 때", "when I am tired, when I am at home at night (mine)"),
         ("여행을 갑니다.", "방학 때, 연휴 때", "during a school break, during a long weekend (mine)"), ("운동을 합니다.", "날씨가 좋을 때, 스트레스를 받을 때", "when the weather is good, when I am stressed (mine)"), ("텔레비전을 봅니다.", "심심할 때, 숙제가 없을 때", "when I am bored, when I have no homework (mine)")]
L6 = lesson(
    "Ch 11 · Grammar A: the conjunctive ending -(으)ㄹ 때 (when)",
    "숙제할 때 · 날씨가 좋을 때 · 심심할 때 · 점심 때 · 크리스마스 때",
    requires=[],
    cards=[
        card("-(으)ㄹ 때: “when”",
             "In English, when we use when as a conjunction, as in when he was a boy or when the bell rings, we can translate it as at or during the time that or at the moment that. In Korean we use the conjunctive ending -(으)ㄹ 때 to express when. The same clause is translated differently depending on the main clause: 심심할 때 is “when I am bored”, “when I am bored (in the future)” or “when I was bored”; the tense of the translation is determined by the tense of the main clause, not by 때.",
             examples=[D(a, b) for a, b in _T_EX]),
        card("How to form -(으)ㄹ 때",
             "verb stem + (으)ㄹ 때. When a verb stem ends in a vowel, add ㄹ 때 (자다 → 잘 때; 심심하다 → 심심할 때). When a verb stem ends in a consonant, add 을 때 (있다 → 있을 때; 먹다 → 먹을 때). The book gives these two cases; the ㄹ-final stems (살다 → 살 때) and the ㅂ irregular stems (춥다 → 추울 때) follow the same pattern as the future attributive form and are mine.",
             tables=[table(["Condition", "Rule", "Examples"], [["Verb stem ends in a vowel", "add ㄹ 때", "자다 → 잘 때; 심심하다 → 심심할 때"], ["Verb stem ends in a consonant", "add 을 때", "있다 → 있을 때; 먹다 → 먹을 때"]]),
                     table(["Verb", "Meaning", "-(으)ㄹ 때"], [[v, "", _ttae(v)] for v in _T_VERBS], say=[0, 2], note="Stems that end in ㄹ keep it (살다 → 살 때), and ㅂ irregular stems change as usual (춥다 → 추울 때); these rows are mine.")]),
        card("때 is a noun",
             "Although we treat -(으)ㄹ 때 as a conjunctive ending that we often interpret as when, its literal translation is at the time that or at the time of; 때 literally means time, and -ㄹ/을 is an attributive form that modifies the noun 때. Thus, like other nouns, -(으)ㄹ 때 can take a noun marker. Also, the noun 때 is often preceded by a noun that denotes time, like 아침, 점심, 저녁, 크리스마스 and 휴가; in this case 때 can be translated at the time of or during the time of.",
             tables=[ktable(_T_NP), ktable(_T_NT)]),
        card("Examples from the book’s vocabulary",
             "Sentences with -(으)ㄹ 때 from the Core Vocabulary and the Topic A dialog (the English is mine; 10살 is spelled out).",
             examples=[D(a, b) for a, b in _T_SENT]),
        card("Follow-Up 1: when → what you do",
             "The book gives clauses on the left and what you can do in each situation on the right and asks you to connect them. My key makes each into a sentence with -(으)ㄹ 때 (the book’s model: 영화 볼 때 팝콘을 먹습니다 or 먹어요).",
             tables=[table(["Clause", "What you do", "Meaning"], [[a, b, c] for a, b, c in _T_MATCH], say=[0, 1])]),
        card("Follow-Up 5: situations for each statement",
             "Each partner picks three of the statements in the book’s box and writes possible situations with -(으)ㄹ 때; the book’s model is 이메일을 보낼 때, 가족과 채팅을 할 때 컴퓨터를 씁니다. The other situations are mine.",
             tables=[table(["Statement", "Situations", "Meaning"], [[a, b, c] for a, b, c in _T_F5], say=[0, 1])]),
        card("Activities left out",
             "Follow-Up 2 (listening to short statements related to travel and filling in a When / What table; the book’s first answer is “when using room service → first call the front desk”) is audio. The partner version of Follow-Up 1b and the flip-chart contest of Follow-Up 5 are partner activities."),
    ],
    exercises=uniq(
        [M(f"What is the -(으)ㄹ 때 form of {v}?", _ttae(v), ([attr(v)[1] + " 때", attr(v)[0] + " 때", if_(v)] if v not in _B_IRR_T else [stem(v) + "는 때", if_(v), stem(v) + "고 때"]), f"{v} → {_ttae(v)}.") for v in _T_VERBS]
        + _tr(_T_EX) + _tr(_T_NP) + _tr(_T_NT) + _tr(_T_SENT) + [M(f"What does {a} {b} mean?", c, [x[2] for x in _T_MATCH if x[2] != c][:3], f"{a} {b}") for a, b, c in _T_MATCH]
        + [M("What does 때 literally mean?", "time", ["place", "person", "thing"], "때 = time."), M("Which tense is the translation of -(으)ㄹ 때 determined by?", "The tense of the main clause", ["The ending 때", "The first verb", "The noun before it"], "심심할 때 게임을 했어요 = when I was bored, I played games."),
           M("Which noun does -ㄹ/을 modify in -(으)ㄹ 때?", "때", ["곳", "것", "분"], "-ㄹ/을 is an attributive form that modifies 때."), M("What does 크리스마스 때 mean?", "during Christmas", ["at lunchtime", "until Christmas", "every Christmas"], "때 after a time noun = at the time of."),
           F("영화 볼 ___ 팝콘을 먹습니다. (when)", "때", ["곳", "것"], "-(으)ㄹ 때 = when."), F("날씨가 좋___ 때 운동합니다. (the form)", "을", ["는", "은"], "좋다 ends in a consonant: 좋을 때."), F("심심___ 때 게임을 해요. (the form)", "할", ["한", "하는"], "심심하다 → 심심할 때."), F("학교에 갈 때___ 갔어요. (every time)", "마다", ["부터", "까지"], "때마다 = every time (when)."),
           F("학교에 갈 때___ 기다렸어요. (until)", "까지", ["부터", "마다"], "때까지 = until the time (when)."), F("저는 ___ 때 미국으로 이민 왔습니다. (when young)", "어렸을", ["어린", "어리는"], "어리다 → 어렸을 때."), F("저는 보통 피곤할 ___ 사우나를 합니다. (when)", "때", ["곳", "분"], "때 = time."),
           read_q("심심할 때"), read_q("점심 때"), read_q("있을 때"), read_q("크리스마스 때")]
    ),
)

# ================================================================== Grammar B: 겠
def _gs(v):
    return stem(v) + "겠습니다"


def _gh(v):
    return "드시겠습니까" if v == "먹다" else hon_stem(v) + "겠습니까"


_G_V = ["하다", "예약하다", "가다", "먹다", "묵다", "준비하다", "끊다", "공부하다", "사다", "체크인하다"]
_G_EX = [("오늘 저녁에는 비가 오겠습니다.", "It will rain tonight. (strong possibility)"), ("내일은 구름이 끼겠습니다.", "It will be cloudy tomorrow. (strong possibility)"), ("저희가 하겠습니다.", "We will do it. (strong intention)"), ("담배를 끊겠습니다.", "I will quit smoking. (strong intention)"),
         ("뭘 드시겠습니까?", "What will you have? (strong intention)"), ("담배를 끊겠습니까?", "Will you quit smoking? (strong intention)"), ("누가 파티를 준비하시겠습니까?", "Who will prepare for the party?"), ("제가 파티를 준비하겠습니다.", "I will prepare for the party.")]
_G_OTHER = [("한국말을 열심히 공부하겠습니다.", "I will study Korean hard. (the Core Vocabulary’s sentence)"), ("잘 먹겠습니다.", "I will eat well. (said before a meal; Topic C)"), ("언제까지 묵으시겠어요?", "Until when will you stay? (Topic B)"), ("배가 불러서 더 못 먹겠어요.", "I’m full, so I can’t eat any more. (Topic C)")]
_G_GA = [("저는 내일 집에 있을 거예요.", "I am going to stay home tomorrow."), ("우리는 내년에 한국에 갈 거예요.", "We are going to go to Korea next year.")]
_G_Q = [("어느 여행 패키지로 예약하시겠습니까?", "예약하다", "유럽 여행 패키지로 예약하겠습니다.", "Which travel package will you book? — I will book the Europe travel package."),
        ("무엇을 드시겠습니까?", "드시다", "비빔밥을 먹겠습니다.", "What will you have? — I will have bibimbap."),
        ("내일은 어디를 구경하시겠습니까?", "구경하다", "서울 시내를 구경하겠습니다.", "Where will you sightsee tomorrow? — I will sightsee downtown Seoul."),
        ("언제 체크인하시겠습니까?", "체크인하다", "오후 네 시에 체크인하겠습니다.", "When will you check in? — I will check in at four in the afternoon."),
        ("어느 호텔에서 숙박하시겠습니까?", "숙박하다", "신라 호텔에서 숙박하겠습니다.", "At which hotel will you stay? — I will stay at the Shilla Hotel."),
        ("마지막 날은 무엇을 하시겠습니까?", "하다", "등산을 하겠습니다.", "What will you do on the last day? — I will go hiking."),
        ("공항까지 어떻게 가시겠습니까?", "가다", "택시로 가겠습니다.", "How will you go to the airport? — I will go by taxi.")]
L7 = lesson(
    "Ch 11 · Grammar B: expressing a strong intention with -겠",
    "저희가 하겠습니다 · 뭘 드시겠습니까? · 비가 오겠습니다 · -겠 vs -(으)ㄹ 거다",
    requires=[],
    cards=[
        card("-겠: strong possibility and strong intention",
             "In English, the modal verb will, which is used to express an event or a state in the future, implies either the strong possibility of an event/state or the strong intention of the subject: It will rain tonight (strong possibility) versus I will find you! (strong intention). Similarly, the verb suffix 겠 implies the strong possibility of an event/state or the strong intention of the speaker. In an earlier chapter, on weather forecasting, the book briefly discussed that 겠 implies a strong possibility. However, when the subject of a sentence is a person, especially the first or second person, 겠 often conveys the strong intention of the person. The 겠 that conveys the strong intention of the subject is used only with an action verb.",
             examples=[D(a, b) for a, b in _G_EX[:6]]),
        card("How to form it",
             "Expressing a strong intention: action verb stem + 겠. The book’s example question and answer are below. With the honorific -(으)시- the 시 comes before 겠: 드시겠습니까, 예약하시겠습니까 (my table; 드시다 is the honorific of 먹다).",
             examples=[D(a, b) for a, b in _G_EX[6:]],
             tables=[table(["Verb", "-겠습니다", "Honorific question: -(으)시겠습니까?"], [[v, _gs(v), _gh(v)] for v in _G_V], say=[0, 1, 2])]),
        card("-겠 in the book’s other sentences",
             "Other sentences with 겠 from the chapter (the English is mine).",
             examples=[D(a, b) for a, b in _G_OTHER]),
        card("-겠 versus -(으)ㄹ 거다",
             "Recall that -(으)ㄹ 거다, which you learned about in Chapter 9, is also used to express a future event. However, -(으)ㄹ 거다 is usually used to convey a future event that the speaker has prior knowledge of or that has been planned. Thus -(으)ㄹ 거다 is usually translated as “be going to”, while 겠 for intention is “will”.",
             examples=[D(a, b) for a, b in _G_GA]),
        card("Follow-Up 3: a travel agent’s questions",
             "The book gives seven questions a travel agent might ask about customers’ intentions; you complete them by conjugating the verbs in parentheses, then answer them with a word or phrase from the list: 신라 호텔, 욕실, 유럽 여행 패키지, 오후 4시, 등산, 서울 시내, 여행 팜플렛, 택시, 비빔밥. My key and sample answers are below (the book’s model is the first pair; 4시 is spelled out as 네 시).",
             tables=[table(["Question", "Verb", "Sample answer", "Meaning"], [[q, v, a, e] for q, v, a, e in _G_Q], say=[0, 2])]),
        card("Activities left out",
             "Follow-Up 4 (listening to four conversations and writing the problems and resolutions) is audio. The partner work of Follow-Up 3b is not reproduced."),
    ],
    exercises=uniq(
        [M(f"What is the plain -겠습니다 form of {v}?", _gs(v), [stem(v) + "습니다", stem(v) + "ㄹ 거예요", hon_stem(v) + "겠습니다" if _gs(v) != hon_stem(v) + "겠습니다" else stem(v) + "었습니다"], f"{v} → {_gs(v)}.") for v in _G_V]
        + [M(f"What is the honorific question form of {v}?", _gh(v), [_gs(v), stem(v) + "습니까", _gh(v).replace("겠", "")], f"{v} → {_gh(v)}.") for v in _G_V]
        + _tr(_G_EX) + _tr(_G_OTHER) + _tr(_G_GA) + _tr([(a, e) for a, v, b, e in _G_Q[:0]])
        + [M(f"A travel agent asks: {q} Which is a fitting answer?", a, [x[2] for x in _G_Q if x[2] != a][:3], f"{q} — {a}") for q, v, a, e in _G_Q]
        + [M("What does 겠 express when the subject is a person?", "A strong intention", ["A past event", "A command", "A question only"], "저희가 하겠습니다 = we will do it."), M("What does 겠 express when the subject is the weather?", "A strong possibility", ["A strong intention", "A past event", "A request"], "비가 오겠습니다 = it will rain."),
           M("With which verbs is 겠 for intention used?", "Only action verbs", ["Only stative verbs", "Only 이다", "Any noun"], "겠 for intention goes with action verbs."), M("Which ending is usually used for a planned future event?", "-(으)ㄹ 거다", ["-겠", "-고", "-지만"], "-(으)ㄹ 거다 = be going to."),
           M("What does 뭘 드시겠습니까? mean?", "What will you have?", ["What did you eat?", "Did you eat?", "Please eat."], "드시다 is the honorific of 먹다."),
           F("제가 파티를 준비___. (I will prepare)", "하겠습니다", ["합니까", "했습니다"], "준비하다 + 겠습니다."), F("무엇을 ___? (honorific, will you have)", "드시겠습니까", ["먹겠습니까", "먹었습니까"], "드시다 + 겠습니까."), F("담배를 끊___. (I will quit)", "겠습니다", ["었습니다", "고 있습니다"], "끊겠습니다."),
           F("저는 내일 집에 있을 ___. (planned)", "거예요", ["겠습니다", "지만"], "-(으)ㄹ 거예요 = going to."), F("오늘 저녁에는 비가 오___. (possibility)", "겠습니다", ["었습니다", "ㄴ 거예요"], "비가 오겠습니다."),
           read_q("드시겠습니까"), read_q("하겠습니다"), read_q("묵으시겠어요"), read_q("끊겠습니다")]
    ),
)


# ================================================================== Topic C: dinner at PFC Baek's house
_C_DLG1 = [
    ("존스 일병", "와! 음식 냄새가 아주 좋아요. 잘 먹겠습니다.", "Wow! The food smells really good. I will eat well."), ("백 일병 어머니", "천천히 많이 먹어요. 그런데, 존스 일병은 젓가락 써 봤어요?", "Eat slowly and a lot. By the way, PFC Jones, have you tried using chopsticks?"),
    ("존스 일병", "네, 전에 써 봤지만 잘 못 써요. 혹시 포크 있으세요?", "Yes, I tried them before, but I can’t use them well. Do you happen to have a fork?"), ("백 일병 어머니", "여기 있어요. 참, 국이 좀 뜨거워요. 조심하세요.", "Here you are. Oh, the soup is a bit hot. Be careful."),
    ("존스 일병", "네, 알겠습니다.", "Yes, I understand."), ("백 일병 어머니", "국이 싱거우면 소금을 더 넣으세요.", "If the soup is bland, add more salt."),
    ("존스 일병", "별로 싱겁지 않아요. 그리고 저는 짠 음식보다 싱거운 음식을 좋아해요.", "It’s not particularly bland. And I like bland food better than salty food."),
]
_C_DLG2 = [
    ("존스 일병", "잘 먹었습니다. 국이랑 반찬이 다 맛있어요.", "Thank you for the meal. The soup and the side dishes are all delicious."), ("백 일병 어머니", "그래요? 자, 후식으로 식혜 좀 마셔 봐요.", "Is that so? Now, try some sikhye for dessert."),
    ("존스 일병", "네, 감사합니다. 와! 달고 시원해요. 아주 맛있어요.", "Yes, thank you. Wow! It’s sweet and refreshing. It’s very delicious."), ("백 일병 어머니", "그래요? 그럼, 좀 더 갖다 줄까요?", "Is that so? Then shall I bring you some more?"),
    ("존스 일병", "괜찮아요. 배가 불러서 더 못 먹겠어요. 정말 잘 먹었습니다.", "It’s all right. I’m full, so I can’t eat any more. Thank you very much for the meal."),
]
_C_PAIRS = [("국", "soup"), ("그렇지만", "but; however; nevertheless"), ("냄새", "smell; odor"), ("달다", "to be sweet"), ("뜨겁다", "to be hot (to the touch)"), ("맛", "taste"), ("배가 부르다", "to be full; “(one’s) stomach is full”"), ("별로", "not particularly; not really"), ("소금", "salt"),
            ("수저", "a spoon and chopsticks"), ("숟가락", "a spoon"), ("시다", "to be sour"), ("식혜", "sweet Korean rice punch"), ("시원하다", "to be refreshing; to be cool"), ("싱겁다", "to be bland"), ("쓰다", "to be bitter"), ("젓가락", "chopsticks"), ("짜다", "to be salty"),
            ("차다", "to be cold; to be chilly"), ("차리다", "to prepare for (food); to set (the table)"), ("천천히", "slowly"), ("포크", "a fork"), ("후식", "a dessert; “after meal”")]
_C_TASTE = [("달다", "to be sweet", "아이스크림은 달아요.", "단 맛"), ("짜다", "to be salty", "소금은 짭니다.", "짠 맛"), ("맵다", "to be spicy", "김치가 매워요.", "매운 맛"), ("시다", "to be sour", "오렌지가 십니다.", "신 맛"), ("쓰다", "to be bitter", "커피가 쓰네요.", "쓴 맛")]
_C_NOTE = [("전에", "previously; before"), ("별로", "particularly; always used in a negated sentence, as in 저는 김밥을 별로 안 좋아해요 (I do not particularly like kimbap)")]
L8 = lesson(
    "Ch 11 · Topic C: I like bland food better than salty food",
    "잘 먹겠습니다 · 젓가락 · 싱겁다 · 짜다 · 달다 · 식혜 · 잘 먹었습니다",
    requires=[],
    cards=[
        card("Dialog: dinner at PFC Baek’s house",
             "PFC Jones has been invited to dinner in PFC Baek’s house. She is talking with PFC Baek’s mother at the dinner table. The Korean is the book’s (the English is mine).",
             examples=dlg(_C_DLG1)),
        card("After the meal",
             "The second part of the dialog takes place after the meal (the book also notes that PFC Jones says “와! 달고 시원해요” after tasting the sikhye).",
             examples=dlg(_C_DLG2)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary). The book lists 배(가) 부르다 with the 가 in parentheses and -지만, -지 못하다 and -지 않다 among the words; those three have their own grammar lessons.",
             tables=[ktable(_C_PAIRS)]),
        card("Footnotes: 전에 and 별로",
             "전에 means previously or before. 별로 means particularly and is always used in a negated sentence, as in 저는 김밥을 별로 안 좋아해요 (I do not particularly like kimbap). The book’s dialog shows both: 전에 써 봤지만 and 별로 싱겁지 않아요.",
             tables=[ktable(_C_NOTE[:1])]),
        card("Types of tastes (맛의 종류)",
             "The book’s table of the five basic tastes. The example sentences are from the Core Vocabulary, except for 맵다, which the book lists in this table but not in its vocabulary list; its example sentence is mine. The last column gives the attributive form used with 맛 (a stative verb’s attributive form ends in (으)ㄴ, as in Chapter 4; the book uses 단 맛, 매운 맛, 짠 맛, 신 맛 and 쓴 맛 in Activity 3).",
             tables=[table(["Korean", "English", "Example", "With 맛"], [[a, b, c, d] for a, b, c, d in _C_TASTE], say=[0, 2, 3])]),
        card("Cultural notes: table manners and hospitality",
             "A spirit of respect for elders is found throughout Korean culture. People are served in the order of seniority and do not pick up their chopsticks or spoon before elders begin eating. It is also a Korean hospitality custom for hosts to repeatedly urge their guests to eat more. Although the younger generation is slowly moving away from this tradition, many Koreans still practice it. If you wish to stop eating, politely tell your host that you are too full when you are asked to eat more (as PFC Jones does with 배가 불러서 더 못 먹겠어요)."),
        card("Activities left out",
             "The SMART Board activities, the conversation-strip activity of the Presentation Activity (arranging strips so that they flow as a natural conversation), Follow-Up Activity 1 (SMART Board) and the Taboo Game of Follow-Up Activity 2 are SMART Board, game or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, e) for k, e in _C_PAIRS])
        + _tr(_strip(_C_DLG1)) + _tr(_strip(_C_DLG2)) + [M(f"What does {a} mean?", b, [x[1] for x in _C_TASTE if x[1] != b][:3], f"{a} = {b}.") for a, b, _, _ in _C_TASTE]
        + [M("Which taste is 짜다?", "salty", ["sweet", "sour", "bitter"], "짜다 = to be salty."), M("Which taste is 시다?", "sour", ["sweet", "salty", "bitter"], "시다 = to be sour."), M("Which taste is 쓰다 (in the taste list)?", "bitter", ["sweet", "sour", "spicy"], "쓰다 = to be bitter."),
           M("What is the attributive form of 맵다 used with 맛?", "매운 맛", ["맵는 맛", "매운 때", "맵은 맛"], "ㅂ irregular: 매운."), M("When is 별로 used?", "Always in a negated sentence", ["Only in questions", "Only in the past", "Only with nouns"], "별로 + negative."), M("What does 전에 mean?", "previously; before", ["after", "never", "soon"], "전에 써 봤지만."),
           M("Why can’t PFC Jones eat any more?", "She is full", ["The soup is hot", "She dislikes it", "She has no spoon"], "배가 불러서 더 못 먹겠어요."), M("What does PFC Jones ask for?", "A fork", ["A spoon", "Chopsticks", "A napkin"], "혹시 포크 있으세요?"), M("What is the dessert drink?", "Sikhye (sweet rice punch)", ["Coffee", "Soup", "Lemonade"], "후식으로 식혜."),
           M("Which food does PFC Jones like better?", "Bland food", ["Salty food", "Spicy food", "Sour food"], "짠 음식보다 싱거운 음식을 좋아해요."), M("Who starts eating first at a Korean meal?", "The elders", ["The youngest", "The guests", "The host’s children"], "Respect for elders."),
           F("국이 좀 ___. 조심하세요. (hot)", "뜨거워요", ["시원해요", "싱거워요"], "뜨겁다 = to be hot to the touch."), F("국이 ___ 소금을 더 넣으세요. (if bland)", "싱거우면", ["싱거워서", "싱겁고"], "싱겁다 + (으)면."), F("저는 짠 음식___ 싱거운 음식을 좋아해요. (than)", "보다", ["에서", "하고"], "~보다 = than."),
           F("후식으로 식혜 좀 마셔 ___. (try)", "봐요", ["가요", "와요"], "-아/어 보다 = try."), F("저는 김밥을 ___ 안 좋아해요. (particularly)", "별로", ["정말", "아주"], "별로 + negative."), F("배가 불러서 더 ___ 먹겠어요. (can’t)", "못", ["안", "잘"], "못 = cannot."),
           read_q("젓가락"), read_q("숟가락"), read_q("식혜"), read_q("싱겁지 않아요"), read_q("후식으로")]
    ),
)

# ================================================================== Grammar C: long-form negation
def _neg(v, hon=False):
    return stem(v) + ("지 않으세요" if hon else "지 않아요")


def _cant(v, hon=False):
    return stem(v) + ("지 못하세요" if hon else "지 못해요")


_N_ACT = ["일어나다", "먹다", "가다", "다니다", "타다", "하다", "보다", "읽다", "마시다", "쓰다", "공부하다", "배우다"]
_N_STA = ["춥다", "필요하다", "싱겁다", "맵다", "짜다", "깨끗하다", "시끄럽다", "달다"]
_N_EX = [("아침을 안 먹습니다.", "아침을 먹지 않습니다.", "I do not eat breakfast."), ("아침을 못 먹습니다.", "아침을 먹지 못합니다.", "I cannot eat breakfast.")]
_N_SENT = [("아침에 일찍 일어나지 않습니다.", "I don’t get up early in the morning."), ("짠 음식을 먹지 않습니다.", "I don’t eat salty foods."), ("몬트레이는 춥지 않습니다.", "It is not cold in Monterey."), ("아침에 일찍 일어나지 못합니다.", "I can’t get up early in the morning."),
           ("짠 음식을 먹지 못합니다.", "I can’t eat salty foods."), ("아침을 먹을 수 없습니다.", "I can’t eat breakfast. (= 먹지 못합니다)"), ("저는 술을 마시지 않아요.", "I don’t drink alcohol."), ("저는 술을 마시지 못해요.", "I can’t drink alcohol."), ("커피는 별로 마시고 싶지 않아요.", "I don’t particularly want to drink coffee.")]
_N_F1 = [("이 케익은 답니다.", "달지 않아요.", "-", "A stative verb: only the -지 않다 form."), ("스키를 타요.", "타지 않아요.", "타지 못해요.", ""), ("고모가 중국어를 하십니다.", "하지 않으세요.", "하지 못하세요.", ""),
         ("그 영화를 이번 주말에 봅니다.", "보지 않아요.", "보지 못해요.", ""), ("어머니가 신문을 읽으세요.", "읽지 않으세요.", "읽지 못하세요.", "")]
_N_SV = [("음식을 주지 않습니다.", "We will not give the contestants food. (the book’s model for the Don’ts)"), ("핸드폰을 쓰지 못합니다.", "The contestants cannot use cell phones. (the book’s model for the Can’ts)"), ("물을 주지 않습니다.", "We will not give them water. (mine)"), ("텔레비전을 보지 못합니다.", "They cannot watch TV. (mine)"), ("사하라 사막에서는 샤워를 하지 못합니다.", "In the Sahara Desert they cannot take a shower. (mine)")]
L9 = lesson(
    "Ch 11 · Grammar C: long-form negation -지 않다 and -지 못하다",
    "먹지 않아요 · 먹지 못해요 · 춥지 않아요 · 안 vs -지 않다 · 못 vs -지 못하다",
    requires=[],
    cards=[
        card("Revisiting negation: short and long forms",
             "In Chapter 7 you learned that Koreans negate a verb by placing either 안 or 못 in front of the verb: 아침을 안 먹습니다 (I do not eat breakfast), 아침을 못 먹습니다 (I cannot eat breakfast). 안 and 못 are the short forms of verb negation. In this chapter the book introduces the long forms, -지 않다 and -지 못하다. -지 못하다 is used with an action verb, but is rarely used with a stative verb; it can be used interchangeably with -(으)ㄹ 수 없다.",
             tables=[table(["Short form", "Long form", "Meaning"], [[a, b, c] for a, b, c in _N_EX], say=[0, 1])]),
        card("“Don’t”: verb stem + 지 않다",
             "With verb stems (action verbs and stative verbs), add 지 않다: 일어나다 → 일어나지 않다; 먹다 → 먹지 않다; 춥다 → 춥지 않다.",
             examples=[D(a, b) for a, b in _N_SENT[:3]]),
        card("“Can’t”: action verb stem + 지 못하다",
             "With action verb stems only, add 지 못하다: 일어나다 → 일어나지 못하다; 먹다 → 먹지 못하다.",
             examples=[D(a, b) for a, b in _N_SENT[3:]]),
        card("Verb tables",
             "The informal polite forms (-지 않아요 and -지 못해요) of action verbs, with the honorific forms, and of stative verbs, which have no -지 못하다 form. The verb tables are mine; the endings are the book’s.",
             tables=[table(["Action verb", "-지 않아요", "-지 못해요", "Honorific: -지 않으세요 / -지 못하세요"], [[v, _neg(v), _cant(v), _neg(v, True) + " / " + _cant(v, True)] for v in _N_ACT], say=[0, 1, 2, 3]),
                     table(["Stative verb", "-지 않아요"], [[v, _neg(v)] for v in _N_STA], say=[0, 1], note="Stative verbs are not negated with -지 못하다 (the book: they cannot be negated this way). The ㅂ irregular stems keep ㅂ before 지: 춥지, 맵지.")]),
        card("Follow-Up 1: negate with both forms",
             "The book asks you to negate each verb using both -지 않다 and -지 못하다, remembering that stative verbs cannot be negated with -지 못하다. The book’s models are 회사에 다녀요 → 다니지 않아요, 다니지 못해요 and 돈이 필요합니다 → 필요하지 않아요. The five answers below are mine.",
             tables=[table(["Sentence", "-지 않다", "-지 못하다", "Note"], [[a, b, c, d] for a, b, c, d in _N_F1], say=[0, 1, 2])]),
        card("Follow-Up 5: rules for a survival game",
             "In the book you are producing the show Survivor and write three things that the staff will not do for the contestants and three things that the contestants cannot do (in the Australian jungle, an island in Indonesia or the Sahara Desert). The book’s models are the first two lines; the other lines are mine.",
             examples=[D(a, b) for a, b in _N_SV]),
        card("Activities left out",
             "Follow-Up 2 (listening to Sooyoung talk about what her family members don’t or can’t do) is audio; the flip-chart part of Follow-Up 5 is a partner activity."),
    ],
    exercises=uniq(
        [M(f"What is the -지 않아요 form of {v}?", _neg(v), [stem(v) + "지 못해요", "안 " + v, stem(v) + "고 싶지 않아요"][:3], f"{v} → {_neg(v)}.") for v in _N_ACT + _N_STA]
        + [M(f"What is the -지 못해요 form of {v}?", _cant(v), [_neg(v), "안 " + v, stem(v) + "지 않으세요"], f"{v} → {_cant(v)}.") for v in _N_ACT]
        + _tr([(b, c) for a, b, c in _N_EX]) + _tr(_N_SENT)
        + [M("Which long form of negation is used only with action verbs?", "-지 못하다", ["-지 않다", "-고 싶다", "-(으)ㄹ 때"], "-지 못하다 = can’t, action verbs only."), M("Which negation can be used with stative verbs like 춥다?", "-지 않다", ["-지 못하다", "-겠", "-(으)ㄹ 수 있다"], "춥지 않다."),
           M("Which expression can replace -지 못하다?", "-(으)ㄹ 수 없다", ["-(으)ㄹ 때", "-겠", "-지만"], "아침을 먹을 수 없습니다 = 아침을 먹지 못합니다."), M("What is the short form of 먹지 않습니다?", "안 먹습니다", ["못 먹습니다", "먹을 수 있습니다", "먹겠습니다"], "안 + verb."),
           M("What is the short form of 먹지 못합니다?", "못 먹습니다", ["안 먹습니다", "먹을 수 있습니다", "먹겠습니다"], "못 + verb."),
           F("저는 술을 마시지 ___. (can’t)", "못해요", ["않아요", "싶어요"], "마시지 못해요 = I can’t drink."), F("저는 술을 마시지 ___. (don’t)", "않아요", ["못해요", "싶어요"], "마시지 않아요 = I don’t drink."),
           F("몬트레이는 춥지 ___. (isn’t)", "않습니다", ["못합니다", "싶습니다"], "A stative verb takes 않다."), F("스키를 타지 ___. (can’t)", "못해요", ["않아요", "싶어요"], "타지 못해요."), F("이 케익은 달지 ___. (isn’t)", "않아요", ["못해요", "싶어요"], "A stative verb takes 않다."),
           read_q("먹지 않아요"), read_q("먹지 못해요"), read_q("춥지 않습니다"), read_q("일어나지 못합니다")]
    ),
)

# ================================================================== Grammar D: -지만
def _jiman(v, past_=False):
    return (past(v) if past_ else stem(v)) + "지만"


_J_V = ["작다", "어렵다", "맵다", "비싸다", "춥다", "좋다", "싸다", "많다", "힘들다", "먹다", "가다", "알다"]
_J_EX = [("한국이 작지만 대만은 더 작아요.", "Korea is small, but Taiwan is smaller."), ("한국말이 어렵지만 재미있어요.", "Korean is difficult, but it is fun."), ("한국말이 어렵지만 재미있어요.", "Although Korean is difficult, it is fun."), ("김치가 맵지만 맛있습니다.", "Kimchi is spicy, but it is delicious. (the book’s model)")]
_J_VS = [("한국말이 어려워요. 그렇지만 재미있어요.", "Korean is difficult. However, it is fun."), ("저는 한국 음식을 좋아해요. 그렇지만 제 남편은 일식을 좋아해요.", "I like Korean food. However, my husband likes Japanese food. (the Core Vocabulary’s sentence)")]
_J_SENT = [("날씨가 추웠지만 밖에서 운동을 했어요.", "It was cold, but I exercised outside. (the Core Vocabulary’s sentence)"), ("네, 전에 써 봤지만 잘 못 써요.", "Yes, I tried them before, but I can’t use them well. (from the Topic C dialog)"), ("이 호텔은 비싸지만 깨끗해요.", "This hotel is expensive, but it is clean. (mine)"),
           ("수영장이 작지만 무료예요.", "The pool is small, but it is free. (mine)"), ("하루 더 묵고 싶었지만 방이 없었습니다.", "I wanted to stay one more day, but there was no room. (from the hotel review)"), ("국이 뜨겁지만 맛있어요.", "The soup is hot, but it is delicious. (mine)")]
def _join(a, b):
    first = a[:-2] + "지만"
    head, _, last = b[:-1].rpartition(" ")
    return first + " " + (head + " " if head else "") + formal(last) + "."


_J_PAIR = [("김치가 맵다.", "맛있다."), ("국이 짜다.", "맛있다."), ("한국말이 어렵다.", "재미있다."), ("호텔이 비싸다.", "깨끗하다."), ("방이 작다.", "깨끗하다."), ("커피가 쓰다.", "향이 좋다."), ("식혜가 달다.", "시원하다."), ("날씨가 춥다.", "맑다.")]
L10 = lesson(
    "Ch 11 · Grammar D: the conjunctive ending -지만 (but)",
    "김치가 맵지만 맛있어요 · 한국말이 어렵지만 재미있어요 · -지만 vs 그렇지만",
    requires=[],
    cards=[
        card("-지만: contrasting two clauses",
             "In English, when contrasting two clauses we can use conjunctions like but, although and whereas (John works harder, but Jane works smarter). In Korean we contrast two clauses by using the conjunctive ending -지만, which can be interpreted as “but”. It attaches to the verb stem (the past -았/었- comes before it: 추웠지만), and works with both action and stative verbs.",
             examples=[D(a, b) for a, b in _J_EX]),
        card("-지만 versus 그렇지만 / 하지만",
             "-지만 may seem identical in meaning to 그렇지만 or 하지만, which you have encountered frequently. The book elaborates on their differences in Chapter 12; for now, know that -지만 is the conjunctive ending and is attached to the verb in the first clause, whereas 그렇지만 or 하지만 are adverbs that come between two independent clauses separated by a period.",
             examples=[D(a, b) for a, b in _J_VS]),
        card("How to form -지만",
             "verb stem + 지만 (the ㅂ irregular stems keep ㅂ here, as before 지: 맵지만, 춥지만). For the past, add 았/었 first: 추웠지만, 비쌌지만. The table is mine.",
             tables=[table(["Verb", "-지만", "Past: -았/었지만"], [[v, _jiman(v), _jiman(v, True)] for v in _J_V], say=[0, 1, 2])]),
        card("More examples",
             "The first two sentences are the book’s (Core Vocabulary and the Topic C dialog); the third is from the hotel review of Activities B; the others are mine.",
             examples=[D(a, b) for a, b in _J_SENT]),
        card("Follow-Up 3: join two sentences with -지만",
             "In the book, partners are given two sets of eight sentence strips (not shown), and one partner reads a sentence and the other finds the sentence that goes best with it when joined by -지만; the book’s model is 김치가 맵다 + 맛있다 → 김치가 맵지만 맛있습니다. The pairs below are mine.",
             tables=[table(["First clause", "Second clause", "Joined with -지만"], [[a, b, _join(a, b)] for a, b in _J_PAIR], say=[0, 1, 2])]),
        card("Activities left out",
             "Follow-Up 4 (listening to four short exchanges between a man and a woman and translating the sentence with -지만) is audio, and the strip game of Follow-Up 3 is a partner activity."),
    ],
    exercises=uniq(
        [M(f"What is the -지만 form of {v}?", _jiman(v), [stem(v) + "고", stem(v) + "지 않아요", if_(v)], f"{v} → {_jiman(v)}.") for v in _J_V]
        + [M(f"What is the past -았/었지만 form of {v}?", _jiman(v, True), [_jiman(v), stem(v) + "고", past(v) + "고"], f"{v} → {_jiman(v, True)}.") for v in _J_V]
        + _tr(_J_EX[:2] + _J_EX[3:]) + _tr(_J_VS) + _tr(_J_SENT)
        + [M("What does -지만 mean?", "but; although", ["because", "if", "when"], "-지만 = but."), M("Where is -지만 attached?", "To the verb in the first clause", ["Between two sentences", "To a noun", "At the end of a sentence"], "한국말이 어렵지만 재미있어요."), M("What is 그렇지만?", "An adverb between two sentences", ["A verb ending", "A noun", "A particle"], "그렇지만 comes between two sentences separated by a period."),
           F("한국말이 어렵___ 재미있어요. (but)", "지만", ["고", "으면"], "어렵다 + 지만."), F("김치가 맵___ 맛있습니다. (but)", "지만", ["고", "으면"], "맵다 + 지만."), F("날씨가 추웠___ 밖에서 운동을 했어요. (but)", "지만", ["고", "으면"], "추웠 + 지만."), F("저는 한국 음식을 좋아해요. ___ 제 남편은 일식을 좋아해요. (However)", "그렇지만", ["그래서", "그리고"], "그렇지만 = however."),
           F("하루 더 묵고 ___ 방이 없었습니다. (wanted, but)", "싶었지만", ["싶고", "싶으면"], "싶었지만 = wanted, but."), read_q("맵지만"), read_q("어렵지만"), read_q("추웠지만"), read_q("그렇지만")]
    ),
)

# ================================================================== Activities C: tastes and table etiquette
_TASTE_MATCH = [("피클", "시다, 짜다", "피클은 시고 짜요.", "Pickles are sour and salty."), ("블랙 커피", "쓰다", "블랙 커피는 써요.", "Black coffee is bitter."), ("타바스코 소스", "맵다, 시다", "타바스코 소스는 맵고 셔요.", "Tabasco sauce is spicy and sour."),
                ("초콜렛", "달다", "초콜렛은 달아요.", "Chocolate is sweet."), ("김치", "맵다, 시다, 짜다", "김치는 맵고 시고 짜요.", "Kimchi is spicy, sour and salty.")]
_ETI = [
    ("한국인들은 보통 밥, 국, 찌개, 반찬을 먹습니다.", "Koreans usually eat rice, soup, stew and side dishes."), ("식사할 때 숟가락과 젓가락을 씁니다.", "When they have a meal, they use a spoon and chopsticks."), ("밥하고 국은 숟가락으로 먹고 반찬은 젓가락으로 먹습니다.", "They eat rice and soup with a spoon and side dishes with chopsticks."),
    ("그리고 음식을 주고 받을 때 두 손을 씁니다.", "And when giving and receiving food, they use both hands."), ("한국인들은 음식을 먹을 때, 나이가 많은 사람이 먼저 먹습니다.", "When Koreans eat, the older person eats first."), ("그래서 어른이 수저를 들기 전에는 수저를 들지 않습니다.", "So before an elder picks up the spoon and chopsticks, they do not pick them up."),
    ("그리고 식사할 때 보통 말을 많이 안 합니다.", "And at a meal they usually do not talk much."), ("특히 어른들과 함께 식사할 때는 이야기를 많이 하지 않습니다.", "Especially when eating together with elders, they do not talk much."), ("또 식사할 때 코를 풀지 않습니다.", "Also, they do not blow their noses at a meal."),
]
_ETI_G = [("손", "a hand"), ("어른", "an adult"), ("들다", "to lift"), ("코를 풀다", "to blow one’s nose")]
_ETI_TF = [("Koreans use chopsticks for eating steamed rice.", "F", "Rice and soup are eaten with a spoon, not chopsticks."), ("When serving and receiving food, Koreans use both hands.", "T", "Both hands are used to give and receive food."), ("In Korea, elders usually start to eat first at the meal table.", "T", "The older person eats first."),
           ("Koreans talk a lot when eating with elders.", "F", "They do not talk much when eating with elders."), ("In Korea, it is not good manners to blow one’s nose when eating.", "T", "They do not blow their noses at a meal.")]
_SURV = [("A", "단 음식은 뭐 먹어봤어요?", "What sweet foods have you tried?"), ("B", "초콜렛, 케익, 아이스크림이요. 저는 단 것을 좋아해요. 그래서 아이스크림을 자주 먹어요.", "Chocolate, cake and ice cream. I like sweet things. So I often eat ice cream."), ("A", "매운 음식도 좋아해요?", "Do you like spicy food too?"),
         ("B", "조금이요. 가끔 친구들과 멕시코 음식을 먹어요. 할라피뇨가 맵지만 맛있어요.", "A little. Sometimes I eat Mexican food with my friends. Jalapeños are spicy, but delicious.")]
_TASTES = [("단 맛", "a sweet taste"), ("매운 맛", "a spicy taste"), ("짠 맛", "a salty taste"), ("신 맛", "a sour taste"), ("쓴 맛", "a bitter taste")]
L11 = lesson(
    "Ch 11 · Activities C: tastes and Korean table etiquette",
    "피클은 시고 짜요 · 식사할 때 숟가락과 젓가락을 씁니다 · 매운 음식 뭐 먹어봤어요?",
    requires=[],
    cards=[
        card("Activity 1a: match each food with its taste",
             "The book gives five food items and five tastes (달다, 쓰다, 짜다, 맵다, 시다) and asks you to match them; some may have more than one match. The matches and sentences are mine (they may vary with the food).",
             tables=[table(["Food", "Taste", "Sentence", "Meaning"], [[a, b, c, d] for a, b, c, d in _TASTE_MATCH], say=[0, 1, 2])]),
        card("The five tastes as nouns of taste",
             "The book’s table for the survey of Activity 3 has these five taste headings, built with the attributive form of the stative verb (달다 → 단, 맵다 → 매운, 짜다 → 짠, 시다 → 신, 쓰다 → 쓴) plus 맛.",
             tables=[ktable(_TASTES)]),
        card("Activity 2 (Reading): Korean table etiquette",
             "The book’s passage about Korean table etiquette (the English is mine). Words glossed by the book: 손 (a hand), 어른 (an adult), 들다 (to lift), 코를 풀다 (to blow one’s nose).",
             tables=[ktable(_ETI_G)], examples=passage(_ETI)),
        card("True or false?",
             "The book asks you to decide whether each English statement is true according to the passage (the answers are mine).",
             tables=[table(["Statement", "T / F", "Why"], [[a, b, c] for a, b, c in _ETI_TF], say=[])]),
        card("Activity 3 (Writing and speaking): what have you tried?",
             "For each taste (단 맛, 매운 맛, 짠 맛, 신 맛, 쓴 맛) you write several food items you have tried and survey your classmates; the book’s model is below (the English is mine).",
             examples=dlg(_SURV)),
        card("Activities left out",
             "Activity 1b (listening to short exchanges to identify the food items and how they taste), the classmate survey and the pie chart or bar graph of Activity 3 (parts c and d: draw a chart on a flip chart and present it to the class) are audio or partner activities."),
    ],
    exercises=uniq(
        _tr(_strip(_SURV)) + _tr(_ETI) + _tr(_ETI_G) + _tr(_TASTES)
        + [M(f"Which taste does {a} have?", b, [x[1] for x in _TASTE_MATCH if x[1] != b][:3], f"{a}: {b}.") for a, b, _, _ in _TASTE_MATCH]
        + [M(f"True or false: {a}", "True" if b == "T" else "False", ["False" if b == "T" else "True"], c) for a, b, c in _ETI_TF]
        + [M("What do Koreans eat rice and soup with?", "A spoon", ["Chopsticks", "Hands", "A fork"], "밥하고 국은 숟가락으로."), M("What do Koreans eat side dishes with?", "Chopsticks", ["A spoon", "Hands", "A fork"], "반찬은 젓가락으로."), M("What do Koreans use when giving and receiving food?", "Both hands", ["One hand", "A tray", "Chopsticks"], "두 손을 씁니다."),
           M("Who eats first at a Korean meal?", "The older person", ["The youngest", "The guest", "The cook"], "나이가 많은 사람이 먼저."), M("Which taste is a 단 맛?", "sweet", ["salty", "sour", "spicy"], "단 = sweet."), M("Which taste is a 신 맛?", "sour", ["sweet", "salty", "bitter"], "신 = sour."),
           F("피클은 시고 ___. (salty)", "짜요", ["달아요", "써요"], "짜다 = salty."), F("블랙 커피는 ___. (bitter)", "써요", ["달아요", "시원해요"], "쓰다 = bitter."), F("초콜렛은 ___. (sweet)", "달아요", ["짜요", "써요"], "달다 = sweet."),
           F("식사할 ___ 숟가락과 젓가락을 씁니다. (when)", "때", ["곳", "분"], "-(으)ㄹ 때."), F("어른이 수저를 들기 전에는 수저를 ___ 않습니다. (pick up)", "들지", ["먹지", "주지"], "들다 = to lift."),
           read_q("피클"), read_q("블랙 커피"), read_q("두 손을"), read_q("코를 풀지 않습니다")]
    ),
)


# ================================================================== Core vocabulary and self-evaluation
_W_COM = [("교포", "a Korean living abroad", "미국에 교포가 많습니다."), ("사업", "a business", "우리 아버지는 사업을 하십니다."), ("사업하다", "to do business", "우리 아버지는 사업을 하십니다."), ("사회", "a community; a society", "미국 사회에는 이민 온 사람들이 많습니다."),
          ("세", "a generation", "저는 미국에서 태어난 한인 이 세입니다."), ("세대", "a generation", "저는 미국에서 태어난 한인 이 세대입니다."), ("유학생", "an international student; a foreign student", "미국에 공부하러 온 유학생들이 많습니다."), ("이민", "immigration; emigration; expatriation", "저는 열 살 때 미국으로 이민 왔습니다."),
          ("인구", "population", "중국에 사람이 많습니다. 중국 인구가 십삼억입니다."), ("한글", "Hangul; the Korean alphabet; “Korean writing”", "저는 한글을 배워서 한국 책을 읽을 수 있습니다."), ("한인", "a Korean expatriate; a Korean (living in the U.S. or abroad); “Korean person”", "엘에이에 한인이 많이 삽니다.")]
_W_NUM = [("만", "ten thousand", "몬트레이 인구는 삼만쯤 됩니다."), ("억", "hundred million", "미국 인구는 삼억쯤 됩니다.")]
_W_LOD = [("무료", "free of charge; “no fare”", "호텔 수영장은 무료입니다. 돈을 내지 않습니다."), ("묵다", "to stay; to lodge", "저는 여행할 때 보통 모텔에 묵습니다."), ("비다", "to be empty; to be vacant", "연휴여서 호텔에 빈방이 없어요."), ("비상구", "an emergency exit; “emergency mouth”", "호텔에는 각 층마다 비상구가 있습니다."),
          ("수건", "a towel", "샤워 후에 수건으로 닦아요."), ("수영장", "a swimming pool; “swimming place”", "이 호텔에 수영장이 있습니까?"), ("숙박비", "lodging fee", "호텔 숙박비가 모텔 숙박비보다 더 비싸요."), ("옮기다", "to move; to transfer", "방이 더러워서 다른 방으로 옮기고 싶어요."),
          ("욕실", "a bathroom", "욕실에서 샤워합니다."), ("이용", "use", "수영을 하고 싶으면 호텔 수영장을 이용하세요."), ("이용하다", "to use; to utilize", "수영을 하고 싶으면 호텔 수영장을 이용하세요."), ("일반실", "a standard room; “general room”", "이 호텔은 일반실이 삼 층부터 십 층까지 있습니다."), ("호", "a (room or apartment unit) number", "제 방은 이백삼 호입니다.")]
_W_TAS = [("달다", "to be sweet", "아이스크림은 달아요."), ("시다", "to be sour", "오렌지가 십니다."), ("싱겁다", "to be bland", "국이 좀 싱거워요. 소금 좀 주세요."), ("쓰다", "to be bitter", "커피가 쓰네요. 설탕 좀 주세요."), ("짜다", "to be salty", "소금은 짭니다.")]
_W_MEAL = [("국", "soup", "한국 사람은 보통 밥과 국을 먹어요."), ("냄새", "smell; odor", "부엌에서 맛있는 냄새가 나요."), ("뜨겁다", "to be hot (to the touch)", "뜨거운 음식은 천천히 드세요."), ("맛", "taste", "불고기 맛이 아주 좋아요."), ("배가 부르다", "to be full; “(one’s) stomach is full”", "많이 먹어서 배가 불러요."),
           ("소금", "salt", "음식이 싱거우면 소금을 넣으세요."), ("수저", "a spoon and chopsticks", "숟가락과 젓가락을 수저라고 합니다."), ("숟가락", "a spoon", "국은 숟가락으로 드세요."), ("시원하다", "to be refreshing; to be cool", "더울 때는 시원한 음료수를 마시고 싶어요."), ("식혜", "sweet Korean rice punch", "식혜가 아주 달고 시원해요."),
           ("젓가락", "chopsticks", "반찬은 젓가락으로 드세요."), ("차다", "to be cold; to be chilly", "날씨가 더우면 찬 레모네이드를 마셔요."), ("차리다", "to prepare for (food); to set (the table)", "어머니가 요리를 하고 상을 차리십니다."), ("후식", "a dessert; “after meal”", "후식으로 과일을 준비했어요.")]
_W_LOAN = [("달러", "dollar", "이 호텔 일반실은 하루에 백이십 달러입니다."), ("서비스", "service", "이 호텔은 서비스가 좋습니다."), ("스위트룸", "a suite (in a hotel)", "이 호텔은 스위트룸이 십이 층에 있습니다."), ("체크아웃", "checkout", "호텔에서는 열두 시까지 체크아웃해야 합니다."),
           ("체크아웃하다", "to check out", "호텔에서는 열두 시까지 체크아웃해야 합니다."), ("체크인", "check-in", "오후 늦게 체크인했어요."), ("체크인하다", "to check in", "오후 늦게 체크인했어요."), ("포크", "a fork", "여기 포크 좀 주세요."), ("프런트", "the front (reception) desk", "체크아웃은 프런트에서 해 주십시오."),
           ("호텔", "a hotel", "라스베가스에 카지노 호텔이 많습니다.")]
_W_OTH = [("곳", "a place", "학교는 공부하는 곳입니다."), ("그럼", "well; then", "오늘은 바빠서 못 만나요. 그럼, 내일 저녁에 만나요."), ("그렇지만", "but; however; nevertheless", "저는 한국 음식을 좋아해요. 그렇지만 제 남편은 일식을 좋아해요."), ("근무", "duty; work; service", "우리 언니는 삼성에서 근무합니다."),
          ("근무하다", "to be on duty; to work; to serve", "우리 언니는 삼성에서 근무합니다."), ("깨끗하다", "to be clean", "교실을 청소해서 깨끗합니다."), ("다니다", "to regularly go to; to attend (school/workplace/church, etc.)", "제 동생은 컴퓨터 회사에 다녀요."), ("다르다", "to be different", "이 식당은 마음에 안 들어요. 다른 식당으로 갑시다."),
          ("대부분", "most; “large part”", "엘에이 한인 대부분은 가족 이민으로 많이 왔어요."), ("더럽다", "to be dirty", "호텔 방이 좀 더러워요."), ("돕다", "to help", "무엇을 도와드릴까요?"), ("별로", "not particularly; not really", "커피는 별로 마시고 싶지 않아요."),
          ("시끄럽다", "to be noisy; to be loud", "옆 집에서 파티를 해서 아주 시끄러워요."), ("어리다", "to be young; to be immature", "저는 어렸을 때 미국으로 이민 왔습니다."), ("정말", "really; truly", "이 케이크는 정말 맛있어요."), ("천천히", "slowly", "음식이 뜨거우니까 천천히 드세요."),
          ("필요하다", "to be needed; to be necessary", "욕실에 수건이 더 필요해요."), ("할인", "discount", "백화점에서 할인하는 옷을 샀어요."), ("할인하다", "to discount", "백화점에서 할인하는 옷을 샀어요."), ("할인받다", "to get a discount", "군인은 할인을 받을 수 있어요.")]
_W_GR = [["-겠", "will; a verb infix expressing strong intention", "한국말을 열심히 공부하겠습니다."], ["-(으)ㄹ 때", "when; time; at the time of", "저는 보통 피곤할 때 사우나를 합니다."], ["~(으)로", "(status) as", "의사로 일하는 한인들이 많아요."], ["-지만", "but", "날씨가 추웠지만 밖에서 운동을 했어요."],
         ["-지 못하다", "can’t", "저는 술을 마시지 못해요."], ["-지 않다", "don’t", "저는 술을 마시지 않아요."]]
_W_SINO = [("민", "(民) people; folks", "국민, 민요, 민족, 이민"), ("비", "(費) expense; fee", "숙박비, 택시비, 학비"), ("실", "(室) a room; chamber", "화장실, 교실, 세탁실")]
_W_ALL = _W_COM + _W_NUM + _W_LOD + _W_TAS + _W_MEAL + _W_LOAN + _W_OTH
_W_SKIP = ("세대", "사업하다", "이용하다", "체크아웃하다", "체크인하다", "근무하다", "할인하다", "할인받다", "호", "이용", "체크인", "체크아웃", "근무", "사업", "프런트")
L12 = lesson(
    "Ch 11 · Core vocabulary and self-evaluation",
    "주요 단어 · 한인 사회 · 호텔 · 맛 · 식사 · 민 · 비 · 실 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). The book writes pairs together (사업(~하다), ~세(대), 이용(~하다), 체크아웃(~하다), 체크인(~하다), 프런트(데스크), 근무(~하다), 할인(~하다/~받다), 배(가) 부르다); they are split here. The book’s Additional Vocabulary section is a blank list for words you add yourself.\n\n"
             "Where a split word has no sentence of its own, it reuses the book’s sentence of the matching word (세대, 할인받다 with a military discount from the hotel review). Digits are respelled in Hangul (3만 → 삼만, 3억 → 삼억, 13억 → 십삼억, 10살 → 열 살, 203호 → 이백삼 호, 3층부터 10층까지 → 삼 층부터 십 층까지, 12층 → 십이 층, 12시 → 열두 시, 120달러 → 백이십 달러); LA is said 엘에이."),
        card("The Korean community", "", tables=[vt(_W_COM)]),
        card("Numbers", "", tables=[vt(_W_NUM)]),
        card("Lodging", "", tables=[vt(_W_LOD)]),
        card("Taste", "", tables=[vt(_W_TAS)]),
        card("At a meal table", "", tables=[vt(_W_MEAL)]),
        card("Loan words", "", tables=[vt(_W_LOAN)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_W_OTH)]),
        card("Grammar words that have their own lessons", "-겠, -(으)ㄹ 때, -지만, -지 못하다 and -지 않다 are explained in the grammar lessons of this chapter, and ~(으)로 “(status) as” is the particle of 의사로 일하는 한인들.", tables=[table(["Form", "Meaning", "Example"], _W_GR, say=[2])]),
        card("Sino-Korean vocabulary", "", tables=[vt(_W_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify the general profile of the Korean community in the U.S.; use large numbers and decimals in context; make hotel reservations and requests for services; talk about the five basic tastes; identify Korean table etiquette.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -지 않다 (do not); -지 못하다 (cannot); the conjunctive ending -지만 (but); the conjunctive ending -(으)ㄹ 때 (when); -겠 for a strong intention (will); the Sino-Korean syllables 민 (民), 비 (費) and 실 (室)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _W_ALL if k not in _W_SKIP])
        + [M(f"What does the Sino-Korean syllable {k} {e.split(' ', 1)[0]} mean?", e.split(" ", 1)[1], [x.split(" ", 1)[1] for _, x, _ in _W_SINO if x != e], f"{k} {e}.") for k, e, _ in _W_SINO]
        + [M("What does -겠 express?", "A strong intention (with an action verb)", ["A past event", "A command", "A wish"], "한국말을 열심히 공부하겠습니다."), M("What does -(으)ㄹ 때 mean?", "when; time; at the time of", ["but", "because", "if"], "피곤할 때 = when I’m tired."), M("What does -지만 mean?", "but", ["when", "because", "if"], "추웠지만 = it was cold, but …"),
           M("What does ~(으)로 mean in 의사로?", "(status) as", ["with", "from", "to"], "의사로 = as a doctor."), M("What does -지 못하다 mean?", "can’t", ["don’t", "will", "want to"], "마시지 못해요."), M("What does -지 않다 mean?", "don’t", ["can’t", "will", "want to"], "마시지 않아요."),
           M("Which Sino-Korean syllable is in 숙박비, 택시비 and 학비?", "비 (費)", ["실 (室)", "민 (民)", "구 (口)"], "비 = expense; fee."), M("Which Sino-Korean syllable is in 화장실, 교실 and 세탁실?", "실 (室)", ["비 (費)", "민 (民)", "구 (口)"], "실 = room."), M("Which Sino-Korean syllable is in 국민, 민요, 민족 and 이민?", "민 (民)", ["비 (費)", "실 (室)", "구 (口)"], "민 = people."),
           M("Which word is the antonym of 깨끗하다?", "더럽다", ["시끄럽다", "싱겁다", "필요하다"], "깨끗하다 ↔ 더럽다."), M("Which word is the antonym of 짜다?", "싱겁다", ["달다", "시다", "쓰다"], "짜다 ↔ 싱겁다."), M("Which word is the antonym of 뜨겁다?", "차다", ["시원하다", "싱겁다", "달다"], "뜨겁다 ↔ 차다."),
           F("국이 좀 ___. 소금 좀 주세요. (bland)", "싱거워요", ["짜요", "뜨거워요"], "싱겁다 → 싱거워요."), F("소금은 ___. (salty)", "짭니다", ["답니다", "씁니다"], "짜다 → 짭니다."), F("오렌지가 ___. (sour)", "십니다", ["답니다", "씁니다"], "시다 → 십니다."),
           F("호텔 수영장은 ___입니다. 돈을 내지 않습니다. (free)", "무료", ["할인", "서비스"], "무료 = free of charge."), F("저는 어렸을 때 미국으로 ___ 왔습니다. (immigrated)", "이민", ["유학생", "교포"], "이민 오다 = to immigrate."), F("오늘은 바빠서 못 만나요. ___, 내일 저녁에 만나요. (then)", "그럼", ["그래서", "그리고"], "그럼 = well; then.")]
        + [read_q("주요 단어"), read_q("체크인하다"), read_q("숙박비"), read_q("일반실"), read_q("싱겁다"), read_q("젓가락")]
    ),
)

UNIT = unit("Semester 1 · Unit 3 · Chapter 11: In Koreatown: Lodging and Dining (코리아타운에서: 숙박과 식사)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
