"""Unit 41: KBC Semester 2, Unit 9, Chapter 34 - College Life (대학 생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 9, Student's Edition (Validation Edition).
Audio, video, pictures, charts, the crossword and soccer-game boards, SMART Board activities, role-plays, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 34 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("강의", "(講義) a lecture; to give a lecture; to lecture (~하다)", "김 교수님은 일주일에 아홉 시간씩 강의합니다."),
    ("건축공학", "(建築工學) architectural engineering", "우리 형은 대학에서 건축공학을 전공했어요."),
    ("경영학", "(經營學) (the study of) business administration", "우리 학교 경영학과 교수님들은 대부분 미국에서 공부하셨습니다."),
    ("경제학", "(經濟學) (the study of) economics", "경제학을 전공한 사람들은 취직하기가 쉽습니다."),
    ("교양(과목)", "(敎養(科目)) elective courses; general education courses; liberal arts courses/subjects", "일 학년 때는 전공과목보다 교양과목을 더 많이 공부합니다."),
    ("교육학", "(敎育學) (the study of) education", "대학에서 교육학을 전공하고 싶습니다."),
    ("국문학", "(國文學) (the study of) Korean literature", "국문학을 전공하는 제 친구는 글쓰기를 좋아합니다."),
    ("드디어", "finally; at last", "제 동생이 드디어 대학생이 되었어요."),
    ("물리학", "(物理學) (the study of) physics", "물리학과를 졸업 하면 취직이 잘 돼서 인기가 아주 높습니다."),
    ("복수전공", "(複數專攻) double major; to double-major in (~하다)", "진수는 영문학과 교육학을 복수전공하고 있습니다."),
    ("부전공", "(副專攻) a minor (area/study); “secondary major”; to minor in ~ (~하다)", "국문과 학생들은 부전공으로 교육학을 많이 선택합니다."),
    ("수강", "(受講) taking/attending a lecture/course; “receiving a lecture”; to take a course (~하다)", "이번 학기에는 영어회화 과목을 수강할 생각입니다."),
    ("신문방송학", "(新聞放送學) (the study of) journalism; “study of newspapers and broadcasting”", "대학에서 신문방송학을 전공한 후에 기자로 일합니다."),
    ("신입생", "(新入生) a freshman; “newly entering student”", "오늘은 우리 과 신입생 환영회가 있습니다."),
    ("심리학", "(心理學) (the study of) psychology; “study of mentality”", "심리학을 전공하면 어떤 직업을 가질 수 있습니까?"),
    ("아르바이트", "a part-time job; an odd job (from the German word arbeit)", "대학생에게 중고생 과외는 가장 인기 있는 아르바이트입니다."),
    ("영문학", "(英文學) (the study of) English literature", "영문학을 전공하는 학생들은 미국과 영국 문학을 공부합니다."),
    ("재수", "(再修) studying again (for an entrance exam); “repeat study”; to study again (~하다)", "대학에 불합격해서 재수를 할 생각입니다."),
    ("전공", "(專攻) a major; to major in (~하다)", "대학에서 무슨 과목을 전공하셨습니까?"),
    ("컴퓨터공학", "(工學) (the study of) computer engineering", "컴퓨터공학과를 졸업하고 인텔에서 일하고 싶어요."),
    ("학점", "(學點) (college) credit; grade (in a subject); “learning points”", "학점이 좋으면 취직하기 쉽습니다."),
    ("화학", "(化學) (the study of) chemistry", "화학은 공부하기 어려운 과목입니다."),
]
_CV_B = [
    ("그만두다", "to quit; to stop; to give up", "대학원에서 공부를 더 하고 싶어서 다니던 직장을 그만두었다."),
    ("등록금", "(登錄金) tuition; “registration money”", "우리 대학 등록금이 계속 오르고 있어요."),
    ("복학", "(復學) coming back to school (from a temporary leave); “recovering school”; to come back to school (~하다)", "다음 학기에 복학할 예정이에요."),
    ("부족", "(不足) lack; insufficiency; to not be/have enough; to lack; to be insufficient (~하다)", "돈이 조금 부족해서 좋은 선물을 사지 못했어요."),
    ("자취", "(自炊) living away from one’s family and cooking food for oneself; “self cooking”; to cook food for oneself (~하다)", "대학교에 들어가면 학교 주변에서 자취를 할 생각이에요."),
    ("장학금", "(奬學金) a scholarship; “encouraging learning money”", "이 대학은 장학금을 받는 학생들이 많습니다."),
    ("적성", "(適性) an aptitude", "국문학은 제 적성에 맞지 않습니다."),
    ("축제", "(祝祭) a festival; “celebrative ritual”", "오 월에 우리 학교 축제가 있습니다."),
    ("충분", "(充分) sufficiency; to be enough; to be sufficient (~하다)", "주말에 잠을 충분히 자서 기분이 좋습니다."),
    ("하숙", "(下宿) boarding; lodging; room and board; to board/lodge (~하다)", "학교 가까운 곳에 하숙집을 구하고 싶어요."),
    ("학비", "(學費) a school expense; tuition", "학비가 비싸서 아르바이트를 해야겠어요."),
    ("학생회", "(學生會) a student association; the student body; “students meeting”", "학생회에서 신입생 환영 행사를 합니다."),
]
_CV_C = [
    ("과정 / 코스", "(課程) a course; curriculum", "국방 외국어 대학의 한국어 과정은 육십사 주입니다."),
    ("등록", "(登錄) registration; to register (~하다)", "이번 학기 등록 기간이 언제 끝납니까?"),
    ("마치다", "to finish; to end; to complete", "수업을 마친 후에 운동하러 갈 거예요."),
    ("박사", "(博士) a doctoral degree; a person with a Ph.D. (degree)", "미국에 있는 대학원 박사과정에 들어갈 계획입니다."),
    ("부담", "(負擔) a burden; to bear a burden / to be burdensome (~하다 / 되다)", "학비가 많이 올라서 부담이 됩니다."),
    ("석사", "(碩士) a master’s (degree); a person with a master’s (degree)", "석사를 마친 후 박사과정에서 공부를 계속할 거예요."),
    ("어학 연수", "(語學 硏修) foreign language study (abroad); “language research and study”", "영어를 배우기 위해서 미국으로 어학 연수를 갔어요."),
    ("어학원", "(語學院) a language institute", "어학원에서 영어회화과목을 수강하고 있어요."),
    ("인턴(사원)", "((社員)) an intern", "여름 방학 동안 컴퓨터 회사에서 인턴사원으로 일했어요."),
    ("일자리", "a job; “work spot”", "요즘 일자리가 많이 없어서 아르바이트 구하기가 힘들어요."),
    ("자격", "(資格) a qualification", "석사과정 입학 자격에 대해서 알고 싶어요."),
    ("자격증", "(資格證) a certificate; a license", "자격증이 많으면 직업을 쉽게 구할 수 있습니다."),
    ("제공", "(提供) providing; to provide / to be provided (~하다/되다)", "하숙집에서 아침과 저녁을 제공해 줍니다."),
    ("진로", "(進路) a (future) route; a course; a (career) path; “forward road”", "대학 졸업 후 진로는 결정했습니까?"),
    ("취업 / 취직", "(就業 / 就職) getting a job; employment; “acquiring a job”; to get a job; to be employed (~하다)", "요즘은 취직하기가 너무 어렵습니다."),
    ("학사", "(學士) a bachelor’s (degree); a person with a bachelor’s (degree)", "대학을 졸업해서 학사 학위를 받았어요."),
    ("학위", "(學位) an academic degree", "유학 가서 박사 학위를 받았습니다."),
    ("회화", "(會話) conversational foreign language", "외국어 학원에서 영어 회화를 공부하고 있어요."),
]
_CV_LOAN = [("아르바이트", "a part-time job; an odd job (from the German word arbeit)", "이번 학기에는 아르바이트를 해야겠어요. 아르바이트 자리를 하나 알아봐 주세요."), ("인턴", "an intern", "요즘 대학생들은 졸업하기 전에 일하고 싶은 회사에서 인턴사원으로 일을 많이 합니다.")]
_CV_GR = [
    ("-이/가 없어요 (double negatives)", "double negatives for emphasis: (없는 / 모르는 / …) ~이/가 없어요", "그 친구는 술을 너무 좋아해서 안 마셔 본 술이 없어요."),
    ("~말고 / -지 말고", "(do) not … but", "저는 커피 말고 주스 주세요. 졸지 말고 공부하세요."),
    ("~같이 / 처럼 / 같은", "like", "김 일병같이 한국말을 잘 하고 싶습니다. 선생님과 같은 사람이 되고 싶어요."),
    ("-(으)면 -(으)ㄹ수록", "the more … (the more)", "영어는 공부할수록 어려운 것 같아요."),
]
_CV_SINO = [("기간", "(期間) period/duration/interval of time", "학기, 정기, 시기, 간식, 주간, 야간"), ("교환", "(交換) exchange", "교통, 교대, 교차로, 환전, 환율, 환승역"), ("부전공", "(副專攻) a minor", "부반장, 부사장, 부교수, 전공, 전문의, 전문가, 공격, 침공, 공방전")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_LOAN}
_EXTRA = {"교양(과목)": "elective courses; general education courses", "과정 / 코스": "a course; curriculum", "어학 연수": "foreign language study (abroad)", "인턴(사원)": "an intern", "취업 / 취직": "getting a job; employment",
          "강사": "a lecturer", "강당": "an auditorium", "휴학": "taking a leave of absence from school", "전과": "changing one’s major/department", "교과서": "a textbook", "과 사무실": "a department office", "유전공학": "genetic engineering", "환경공학": "environmental engineering", "전기공학": "electrical engineering", "문학": "literature", "공학": "engineering", "과목": "a(n) (academic) subject",
          "부학장": "an associate dean; an assistant dean", "부사장": "a vice-president (of a company)", "부사령관": "a deputy commander", "부조종사": "an assistant pilot; a co-pilot", "부팀장": "an assistant team leader", "부반장": "an assistant class leader", "전용차선": "a bus-only lane", "전문가": "an expert; a specialist", "전매": "monopoly; “exclusive (ownership on) sale”", "공격": "an attack; offense", "공방전": "an offensive and defensive battle", "침공": "an invasion (of another country); “invasion and attack”",
          "학기": "a semester; a term; “school period”", "초기": "the early period; an early stage; “first period”", "말기": "the last period; the last stage; “last period”", "정기": "a regular interval; a fixed time; a fixed period", "부자간": "“between father and son”", "공간": "space; room; “air gap”", "시간": "time; “time gap”", "야간": "night; nighttime; “night gap”",
          "교제": "dating; going out; “interact and meet”", "교배": "crossbreeding; “interact and mate”", "교통": "traffic; “exchange of moving”", "교우": "making friends; “interact with a friend”", "교신": "exchange of messages; communication", "환기": "ventilation; “exchange of air”", "환율": "an exchange rate", "환전": "money exchanging", "환풍기": "a ventilation fan; “exchange-of-wind machine”", "교차로": "an intersection; a crossroads", "환승역": "a transfer station",
          "-이/가 없어요 (double negatives)": "double negatives for emphasis", "~말고 / -지 말고": "(do) not … but", "~같이 / 처럼 / 같은": "like", "-(으)면 -(으)ㄹ수록": "the more … (the more)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"

_BU = [("부학장", "an associate dean; an assistant dean"), ("부사장", "a vice-president (of a company)"), ("부사령관", "a deputy commander"), ("부조종사", "an assistant pilot; a co-pilot"), ("부팀장", "an assistant team leader"), ("부반장", "an assistant class leader; an assistant section leader")]
_JEON = [("전용차선", "a bus-only lane"), ("전문가", "an expert; a specialist"), ("전매", "monopoly; “exclusive (ownership on) sale”"), ("공격", "an attack; offense"), ("공방전", "an offensive and defensive battle"), ("침공", "an invasion (of another country); “invasion and attack”")]
_GI = [("학기", "a semester; a term; “school period”"), ("초기", "the early period; an early stage; “first period”"), ("말기", "the last period; the last stage; “last period”"), ("정기", "a regular interval; a fixed time; a fixed period")]
_GAN = [("부자간", "“between father and son”"), ("공간", "space; room; “air gap”"), ("시간", "time; “time gap”"), ("야간", "night; nighttime; “night gap”")]
_GYO = [("교제", "dating; going out; “interact and meet”"), ("교배", "crossbreeding; “interact and mate”"), ("교통", "traffic; “exchange of moving”"), ("교우", "making friends; “interact with a friend”"), ("교신", "exchange of messages; communication; correspondence")]
_HWAN = [("환기", "ventilation; “exchange of air”"), ("환율", "an exchange rate"), ("환전", "money exchanging; exchange of money"), ("환풍기", "a ventilation fan; “exchange-of-wind machine”")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 34 · What the chapter teaches, 부 (副) 전 (專) 공 (攻) · 교 (交) 환 (換) · 기 (期) 간 (間)",
    "대학 생활 · 부전공 · 교환 · 기간 · 부사장 · 교통 · 환율 · 학기",
    requires=[],
    cards=[
        card("What Chapter 34 teaches (대학 생활)",
             "Chapter 34, “College Life”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss academic majors and classes and other college-related activities like registration; identify and discuss aspects of college life, such as employment and common concerns; and discuss plans for after graduating from college.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; using double negatives for emphasis; ~말고/–지 말고 (do not … but); ~같이/처럼 and ~같은 (like); the conjunctive ending –(으)면 –(으)ㄹ수록; and the Sino-Korean syllables within 부전공 (副專攻), 교환 (交換), and 기간 (期間)."),
        card("Sino-Korean in use: 부전공 (副專攻)",
             "This Sino-Korean word means a minor (academic subject). The first syllable 부 (副) literally means “come close (to the first)”, and it normally means secondary, vice-, assistant, deputy, or co- when it heads a title, as in 부학장 (an associate dean; an assistant dean), 부사장 (a vice-president [of a company]), 부사령관 (a deputy commander), 부조종사 (an assistant pilot; a co-pilot), 부팀장 (an assistant team leader), and 부반장 (an assistant class leader; an assistant section leader). The word 전공 itself means a major (academic subject) or specialty. The second syllable 전 (專) means only or exclusive(ly), as in 버스 전용차선 (bus-only lane), 전문가 (an expert; a specialist), and 전매 (monopoly; “exclusive [ownership on] sale”). The last syllable 공 (攻) means hit or attack, as in 공격 (an attack; offense), 공방전 (offensive and defensive battle), 침공 (an invasion [of another country]; “invasion and attack”). Thus the literal meaning of the word 부전공 is “secondary major”, and the word refers to a secondary focus of a bachelor’s degree.",
             tables=[ktable(_BU), ktable(_JEON)]),
        card("Sino-Korean in use: 교환 (交換)",
             "This Sino-Korean word means exchange, swap, or barter. The shape of the Chinese character 交 (교) depicts a person walking (with the purpose of interacting with other people). Thus, the underlying meaning is interaction (among people), and the syllable can be translated as exchange, interchange, intersect, or interact, as in 교제 (dating; going out; “interact and meet”), 교배 (crossbreeding; “interact and mate”), 교통 (traffic; “exchange of moving”), 교우 (making friends; “interact with a friend”), and 교신 (exchange of messages; communication; correspondence). The syllable 환 (換) means exchange, as in 환기 (ventilation; “exchange of air”), 환율 (exchange rate), 환전 (money exchanging; exchange of money), and 환풍기 (a ventilation fan; “exchange-of-wind machine”). Thus the literal meaning of the word 교환 is “interact and exchange”, and the word refers to the act of giving or taking one thing in return for another.\n\n"
             "The book asks you to guess the meaning of 교차로 and 환승역 (my answers: an intersection; a crossroads — and a transfer station).",
             tables=[ktable(_GYO), ktable(_HWAN), ktable([("교차로", "an intersection; a crossroads"), ("환승역", "a transfer station")])]),
        card("Sino-Korean in use: 기간 (期間)",
             "This Sino-Korean word means the duration of time, the interval of time, or period, as in 한국에서는 겨울방학기간이 길어요 (The duration of a winter break is long in Korea). The first syllable 기 (期) means period of time or term, as in 학기 (a semester; a term; “school period”), 초기 (the early period; an early stage; “first period”), 말기 (the last period; the last stage; “last period”), and 정기 (a regular interval; a fixed time; a fixed period). The second syllable 간 (間) means gap, between, or distance, as in 부자간 (“between father and son”), 공간 (space; room; “air gap”), 시간 (time; “time gap”), and 야간 (night; nighttime; “night gap”). Thus the literal meaning of the word 기간 is “duration gap” or “interval gap”.",
             tables=[ktable(_GI), ktable(_GAN)]),
    ],
    exercises=uniq(
        _tr(_BU + _JEON + _GYO + _HWAN + _GI + _GAN, k=3)
        + [M("What does 부 (副) mean at the head of a title?", "secondary; vice-; assistant; deputy", ["only", "attack", "exchange"], "부사장, 부반장."), M("What does 전 (專) mean?", "only; exclusive(ly)", ["secondary", "attack", "period"], "전문가."), M("What does 공 (攻) mean?", "hit; attack", ["only", "exchange", "gap"], "공격."), M("What does 교 (交) mean?", "exchange; interact", ["period", "gap", "attack"], "교제, 교통."), M("What does 환 (換) mean?", "exchange", ["period", "gap", "only"], "환율."), M("What does 기 (期) mean?", "period of time; term", ["gap", "attack", "exchange"], "학기."), M("What does 간 (間) mean?", "gap; between; distance", ["term", "attack", "exchange"], "시간."),
           M("What is the literal meaning of 부전공?", "“secondary major”", ["“interact and exchange”", "“duration gap”", "“study of numbers”"], "부 + 전 + 공."), M("What is the literal meaning of 교환?", "“interact and exchange”", ["“secondary major”", "“duration gap”", "“school period”"], "교 + 환."), M("What is the literal meaning of 기간?", "“duration gap” or “interval gap”", ["“secondary major”", "“interact and exchange”", "“school expense”"], "기 + 간."),
           F("국문과 학생들은 ___으로 교육학을 많이 선택합니다. (a minor)", "부전공", ["복수전공", "전공"], "부전공."), F("진수는 영문학과 교육학을 ___하고 있습니다. (double major)", "복수전공", ["부전공", "전공"], "복수전공."), F("한국에서는 겨울방학 ___이 길어요. (the duration)", "기간", ["공간", "시간"], "기간."),
           read_q("부전공"), read_q("교환"), read_q("기간"), read_q("부사장"), read_q("환승역")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_G1 = ["전공", "부전공", "복수전공", "국문학", "영문학"]
_G2 = ["컴퓨터공학", "환경공학", "유전공학", "전기공학"]
_G3 = ["교과서", "과목", "과 사무실", "전과"]
_G4 = ["강사", "강당", "강의", "수강"]
_G5 = ["학점", "학비", "휴학", "복학"]
_GRP = [("Majors and fields of study", _G1), ("Fields of engineering", _G2), ("Textbook, subject, department office, changing majors", _G3), ("Lecture-related words", _G4), ("Credits, fees and leaves of absence", _G5)]
_SYL = [("전공", "a major"), ("문학", "literature"), ("공학", "engineering"), ("과", "a department; a class"), ("강", "giving a lecture"), ("학", "learning")]
_XW = [("휴학", "학교를 잠시 쉬는 것", "1 across"), ("컴퓨터공학", "컴퓨터 하드웨어, 소프트웨어, 프로그래밍에 관련된 공부", "4 across"), ("수강", "수업을 신청하여 듣는 것", "6 across"), ("영문학", "영국과 미국의 시나 소설 등을 공부하는 것", "8 across"), ("복학", "학교를 쉬었다가 다시 돌아와서 공부하는 것", "10 across"), ("학점", "한 학기 동안 과목을 들어서 받는 점수", "2 down"), ("전공", "대학에서 전문적으로 공부하는 과목", "3 down"), ("학비", "학교에서 공부를 하는데 쓰는 돈", "5 down"), ("강의", "대학의 수업", "7 down"), ("국문학", "한국의 시나 소설 등을 공부하는 것", "9 down"), ("복수전공", "대학에서 전공을 둘 이상 하는 것", "10 down")]
_HYUN = [("대학", "University"), ("현수는 이 년 전에 휴학을 하고 군대에 입대했다.", "Hyunsoo took a leave of absence two years ago and enlisted in the military."), ("그리고 지난달에 제대를 했다.", "And last month he was discharged."), ("현수는 다음 학기에 학교에 복학할 예정이다.", "Hyunsoo plans to return to school next semester."), ("그래서 오늘 학교 은행에 가서 학비도 내고 인터넷으로 수강 신청도 했다.", "So today he went to the school bank and paid his tuition and also registered for classes on the internet."), ("모두 십팔 학점을 신청했다.", "He signed up for eighteen credits in all."), ("현수의 전공은 국문학이다.", "Hyunsoo’s major is Korean literature."), ("하지만 요즘 많은 학생들이 취업 때문에 복수전공을 한다고 한다.", "But they say that many students these days double-major because of employment."), ("그래서 현수도 다음 학기부터 유전공학을 하나 더 전공하려고 한다.", "So Hyunsoo also plans to major in one more subject, genetic engineering, from next semester.")]
L2 = lesson(
    "Ch 34 · Vocabulary Builder: majors, engineering fields, school words and a crossword",
    "전공 · 부전공 · 복수전공 · 국문학 · 영문학 · 컴퓨터공학 · 휴학 · 복학 · 수강 · 학점 · 학비",
    requires=[],
    cards=[
        card("Study the groups of words",
             "The book shows three boxes of words and asks you to think about why they are grouped this way and to write a guess in English under each box. The words are 전공, 부전공, 복수전공, 국문학, 영문학; 컴퓨터공학, 환경공학, 유전공학, 전기공학, 교과서, 과목, 과 사무실, 전과; and 강사, 강당, 학점, 휴학, 강의, 수강, 학비, 복학. My groupings:",
             tables=[table(["Group (mine)", "Words"], [[n, ", ".join(ws)] for n, ws in _GRP], say=[1])]),
        card("The meanings of the new words (the book’s Core Vocabulary, plus mine for the rest)", "Words that appear in the Core Vocabulary have the book’s meanings; 강사 (a lecturer), 강당 (an auditorium), 휴학 (taking a leave of absence from school), 전과 (changing one’s major/department), 교과서 (a textbook), 과 사무실 (a department office), 유전공학 (genetic engineering), 환경공학 (environmental engineering) and 전기공학 (electrical engineering) are mine.",
             tables=[ktable(_rows(["전공", "부전공", "복수전공", "국문학", "영문학", "컴퓨터공학", "과목", "강의", "수강", "학점", "학비", "복학"]) + [(k, _EXTRA[k]) for k in ["강사", "강당", "휴학", "전과", "교과서", "과 사무실", "유전공학", "환경공학", "전기공학"]])]),
        card("Step b: the syllables", "The book gives six syllables or words and asks you to match them with six English meanings (the matches are mine):", tables=[ktable(_SYL)]),
        card("Activity 2: the crossword clues, answered", "The book gives eleven clues for a crossword (the grid is a picture and is left out). The clues and my answers:",
             tables=[table(["Number", "Clue", "Answer (mine)"], [[c, a, b] for b, a, c in _XW], say=[1, 2])]),
        card("Activity 3: Hyunsoo’s return to college", "The book asks you to complete the paragraph with words from the box (국문학 수강 학점 학비 휴학 복수 전공 공학 복학). The text below is completed with my answers, in this order: 휴학, 복학, 학비, 수강, 학점, 국문학, 복수전공, 공학; 2년 and 18학점 are spelled out. The English is mine.", examples=passage(_HYUN)),
        card("Activities left out", "Activity 1 (listening to four descriptions and choosing 휴학, 영문학, 복수전공, 복학 or 교육학), Activity 4 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 5 (a soccer-board sentence-making game in two teams, with the model 내년에 영어를 전공할 거예요 from 전공 + 내년) are audio, computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["전공", "부전공", "복수전공", "국문학", "영문학", "컴퓨터공학", "과목", "강의", "수강", "학점", "학비", "복학"]))
        + _tr(_SYL, k=3)
        + _tr(_HYUN[1:], k=3)
        + [M("Which word matches the clue “" + a + "”?", b, [x[0] for x in _XW if x[0] != b][:3], "My answer.") for b, a, c in _XW]
        + [F("현수는 이 년 전에 ___을 하고 군대에 입대했다. (took a leave)", "휴학", ["복학", "수강"], "휴학."), F("현수는 다음 학기에 학교에 ___할 예정이다. (return)", "복학", ["휴학", "전공"], "복학."), F("오늘 학교 은행에 가서 ___도 내고 수강 신청도 했다. (tuition)", "학비", ["학점", "전공"], "학비."), F("모두 십팔 ___을 신청했다. (credits)", "학점", ["학비", "학년"], "학점."), F("현수의 ___은 국문학이다. (major)", "전공", ["복학", "수강"], "전공."), F("현수도 다음 학기부터 유전공학을 하나 더 ___하려고 한다. (major in)", "전공", ["복학", "휴학"], "전공하다."),
           read_q("전공"), read_q("복수전공"), read_q("휴학과 복학"), read_q("수강 신청"), read_q("현수의 전공은 국문학이다")]
    ),
)

# ================================================================== L3: Topic A
_A_TXT = [
    ("미진 씨는 한국대학교 학생입니다.", "Mijin is a student at Hanguk University."),
    ("일 년 동안 재수를 하고 올해 드디어 대학교에 입학했습니다.", "After studying again for a year, she has finally entered university this year."),
    ("미진 씨의 전공은 영문학입니다.", "Mijin’s major is English literature."),
    ("이 학년이 되면 부전공이나 복수전공으로 신문방송학도 공부할 계획입니다.", "When she becomes a sophomore, she plans to study journalism too as a minor or a double major."),
    ("이번 봄 학기에는 심리학이나 교육학 같은 교양과목을 많이 수강하려고 합니다.", "This spring semester, she intends to take many elective courses such as psychology or education."),
    ("매일 저녁 아르바이트를 해야 하기 때문에 많은 학점을 들을 수 없습니다.", "Because she has to work a part-time job every evening, she cannot take many credits."),
    ("그래서 십이 학점만 신청하려고 합니다.", "So she intends to sign up for only twelve credits."),
    ("미진 씨는 내일 신입생 환영회에 갑니다.", "Mijin is going to the freshman welcome party tomorrow."),
    ("대학교 사 년 동안 강의도 열심히 듣고 동아리 활동에도 부지런히 참여할 생각입니다.", "For her four years of university she plans to listen to lectures diligently and take part diligently in club activities too."),
]
_A_WORDS = ["강의", "건축공학", "경영학", "경제학", "교양(과목)", "교육학", "국문학", "드디어", "물리학", "복수전공", "부전공", "수강", "신문방송학", "신입생", "심리학", "아르바이트", "영문학", "재수", "전공", "컴퓨터공학", "학점", "화학"]
_KA = "In Korea, when high school graduates are not admitted to the college or university to which they applied, many of them choose to spend another year taking additional college prep courses in order to get into the college or university to which they originally applied. This process is called 재수 (再修) and literally means “studying again”; the students who do this are called 재수생 (再修生)."
_INT = [("저는 사람의 생각에 대해서 관심이 많아요. 무슨 생각으로 어떤 행동을 하는지 알고 싶어요.", "e", "심리학"), ("저는 독서가 취미예요. 셰익스피어를 좋아해서 셰익스피어 책은 영어로 다 읽었어요. 나중에 영국으로 유학 가고 싶어요.", "d", "영문학"), ("저는 여가시간을 주로 컴퓨터 게임을 하거나 프로그램을 만들면서 보내요.", "a", "컴퓨터공학"), ("저는 사람들이 이용하기 편한 건물을 디자인하고 싶어요. 또 세계에서 가장 아름다운 건물을 내 손으로 만들고 싶어요.", "f", "건축공학"), ("저는 나중에 큰 회사의 사장이 되고 싶습니다. 회사와 직원들을 잘 관리하는 방법에 대해 배우고 싶어요.", "c", "경영학"), ("저는 우리나라의 문학을 좋아해요. 특히 소설에 관심이 많습니다. 우리나라의 소설에 대해 공부하고 싶어요.", "b", "국문학")]
L3 = lesson(
    "Ch 34 · Topic A: Did you sign up for classes? (수강신청 했어?)",
    "수강신청 했어 · 미진 씨의 전공 · 재수 · 교양과목 · 신입생 환영회 · 동아리 활동 · 심리학 · 경영학 · 건축공학",
    requires=[],
    cards=[
        card("Topic A: Did you sign up for classes? (수강신청 했어?)",
             "The following text is about Mijin’s plans for first-year college classes. (The English is mine; the book gives none; the numbers are spelled out in Hangul.)",
             examples=passage(_A_TXT)),
        card("한국에서는: 재수 (studying again)", _KA),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 강의(하다), 복수전공(하다), 부전공(하다), 수강(하다), 재수(하다) and 전공(하다) take the form in parentheses.", tables=[ktable(_rows(_A_WORDS))]),
        card("Follow-up 1 (Reading): which major fits each student’s interest?",
             "The book gives six statements by high school seniors and seven majors (a. 컴퓨터공학; b. 국문학; c. 경영학; d. 영문학; e. 심리학; f. 건축공학; g. 경제학) and asks you to write the letter of the best major for each; one major has no match. The statements are the book’s (the book glosses 소설: novel); the answers are mine (g, 경제학, is the one with no match).",
             tables=[table(["Statement", "Letter", "Major (mine)"], [[a, b, c] for a, b, c in _INT], say=[0, 2])]),
        card("Activities left out", "The SMART Board activities, Follow-up 2 (listening to three dialogs about a male student’s academic plan), the list of useful websites (Seoul National University, Yonsei University), Activity 1 (SMART Board) and Activity 2 (listening to a graduate speak to freshmen and filling in her majors and achievements) are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT, k=3)
        + [M("Which major fits: “" + a[:28] + "…”?", c, [x[2] for x in _INT if x[2] != c][:3], "My answer.") for a, b, c in _INT]
        + [M("What is 미진 씨’s major?", "English literature", ["Psychology", "Education", "Economics"], "전공은 영문학."), M("How long did 미진 study for the entrance exam again?", "One year", ["Two years", "Six months", "Three years"], "일 년 동안 재수."), M("What might she study as a minor or double major?", "Journalism", ["Chemistry", "Physics", "Law"], "신문방송학."), M("What kind of courses will she take this spring?", "Electives such as psychology or education", ["Only her major", "Only math", "None"], "교양과목."), M("Why can she not take many credits?", "She has to work a part-time job every evening", ["She is sick", "She is lazy", "She has no money"], "아르바이트를 해야 하기 때문에."), M("How many credits does she plan to take?", "Twelve", ["Two", "Eighteen", "Twenty"], "십이 학점."), M("Where is she going tomorrow?", "The freshman welcome party", ["The library", "A concert", "The airport"], "신입생 환영회."),
           F("올해 ___ 대학교에 입학했습니다. (finally)", "드디어", ["따라서", "그리고"], "드디어."), F("이번 봄 학기에는 심리학이나 교육학 같은 ___을 많이 수강하려고 합니다. (electives)", "교양과목", ["전공", "학점"], "교양과목."), F("일 년 동안 ___를 하고 올해 대학교에 입학했습니다. (studying again)", "재수", ["수강", "복학"], "재수."), F("미진 씨는 내일 ___ 환영회에 갑니다. (freshman)", "신입생", ["졸업생", "재학생"], "신입생."), F("대학교 사 년 동안 ___도 열심히 듣고 동아리 활동에도 참여할 생각입니다. (lectures)", "강의", ["학비", "학점"], "강의."),
           read_q("수강신청 했어"), read_q("미진 씨의 전공은 영문학입니다"), read_q("올해 드디어 대학교에 입학했습니다"), read_q("신입생 환영회에 갑니다"), read_q("동아리 활동에도 부지런히 참여할 생각입니다")]
    ),
)

# ================================================================== L4: Activities of Topic A: majors article and class timetable
_NEWS = [("자연계열 취업 인기학과 인문계열 외국어 강세", "Natural sciences: popular departments for employment; humanities: foreign languages are strong"), ("최근 삼 년간 주요 대학 모집에서 자연계열은 취업에 유리한 학과를, 인문계열은 외국어 관련학과를 선호하는 경향이 있다는 분석이 나왔다.", "An analysis has come out that in admissions at major universities over the last three years, natural sciences applicants tend to prefer departments favorable for employment and humanities applicants tend to prefer foreign-language-related departments."), ("한 조사에 의하면 이천이십삼 학년도 대입 정시모집에서 서울지역 열 개 대학의 의학계열을 제외한 자연계열 선호학과를 분석한 결과, 컴퓨터 관련 학과가 일 위를 차지했다고 이십사 일 밝혔다.", "According to one survey, in analyzing the preferred natural sciences departments, excluding medical fields, at ten Seoul-area universities in the regular admissions for the 2023 academic year, computer-related departments took first place, it said on the 24th."), ("이어 반도체 관련 학과, 네 개, 십삼 점 삼 퍼센트, 인공지능, 세 개, 십 퍼센트 관련 학과 순이었다.", "They were followed by semiconductor-related departments (four, 13.3%) and artificial-intelligence-related departments (three, 10.0%) in that order."), ("인문계열은 최근 삼 년 연속 외국어 관련 학과가 최상위권을 차지한 것으로 나타났다.", "In the humanities, foreign-language-related departments were found to have taken the top rank for three years in a row."), ("서울의 열한 개 대학의 이천이십삼 학년도 입시 경쟁률을 분석한 결과, 외국어 관련 학과가 서른네 개 인기학과 중 일곱 개, 이십 점 육 퍼센트로 일 위를 차지했고, 이어 사회과학, 여섯 개, 십칠 점 육 퍼센트, 경영, 다섯 개, 십사 점 칠 퍼센트 순이었다.", "In analyzing the 2023 admissions competition rates of eleven universities in Seoul, foreign-language-related departments took first place with seven of the thirty-four popular departments (20.6%), followed by social sciences (six, 17.6%) and business (five, 14.7%) in that order.")]
_TT1 = [["국어 1", "국어국문학과", "2", "목 11, 12", "인문대학 303호"], ["기초물리", "물리학과", "6", "목 9, 10, 11 / 금 9, 10, 11", "자연과학대학 202호 / 실습실 1호"], ["사회봉사", "사회복지학과", "2", "목 11, 12", "사회과학대학 202호"], ["매스컴과 현대사회", "사회학과", "3", "월 11, 12 / 수 12", "사회과학대학 606호"], ["현대사회와 리더십", "사회학과", "3", "월 11, 12 / 수 12", "사회과학대학 202호"], ["식습관과 환경", "식품공학과", "3", "월 11 / 수 11, 12", "공과대학 107호"], ["심리학의 이해", "심리학과", "2", "화 11, 12", "사회과학대학 101호"], ["언어의 이해", "언어학과", "3", "월 10 / 수 9, 10", "인문대학 211호"], ["영문학의 이해", "영어영문학과", "2", "화 9, 10", "인문대학 102호"], ["페미니즘과 영문학", "영어영문학과", "3", "월 11 / 수 11, 12", "인문대학 204호"], ["클래식음악의 이해", "음악교육과", "1", "금 9", "사범대학 401호"], ["일본어 회화 A", "일어일문학과", "2", "목 9, 10", "인문대학 102호"], ["일본어 회화 B", "일어일문학과", "2", "목 9, 10", "인문대학 103호"], ["중국문화 읽기", "중어중문학과", "3", "월 9, 10 / 수 9", "인문대학 204호"], ["현대사회와 스포츠", "체육교육과", "2", "화 11, 12", "사범대학 106호"], ["수영", "체육교육과", "1", "금 9", "중앙체육관"], ["테니스", "체육교육과", "1", "금 9", "중앙체육관"], ["태권도", "체육교육과", "1", "금 9", "중앙체육관"], ["생활 컴퓨터", "컴퓨터학부", "3", "월 9, 10 / 수 9", "공과대학 실습실 1호"], ["기초화학", "화학과", "6", "목 9, 10, 11 / 금 9, 10, 11", "자연과학대학 111호 / 실습실 3호"], ["환경과 건강", "환경공학과", "3", "월 10 / 수 9, 10", "공과대학 202호"]]
L4 = lesson(
    "Ch 34 · Topic A activities: popular majors and a night-class timetable",
    "인기학과 · 자연계열 · 인문계열 · 경쟁률 · 수강신청서 · 교양과목 강의시간표 · 9학점",
    requires=[],
    cards=[
        card("Activity 3 (Reading): a news article on the popularity of college majors",
             "The following news article is about the popularity of college majors in college entrance exams. The book asks two things: the overall trend in preferred majors (applicants for humanities; applicants for natural sciences) and a table of the first, second and third popular majors. The headline’s quotation marks and the “·” marks are dropped, and the numbers are spelled out in Hangul; the English is mine.",
             examples=passage(_NEWS)),
        card("The answers (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Item", "Answer (mine)"], [["Trend: humanities", "Foreign-language-related departments are preferred"], ["Trend: natural sciences", "Departments favorable for employment are preferred"], ["Popular majors: humanities", "1st foreign languages (7 of 34, 20.6%); 2nd social sciences (6, 17.6%); 3rd business (5, 14.7%)"], ["Popular majors: natural sciences", "1st computer-related; 2nd semiconductor-related (4, 13.3%); 3rd artificial intelligence (3, 10.0%)"]])]),
        card("Activity 4 (Reading, speaking and writing): which classes shall I take this semester?",
             "You work in Korea and decide to take classes at a local college near your workplace. Since you work during the day, you want to take night classes that provide nine credits. The book gives the first-semester general-education timetable (교양과목 강의시간표) and asks you to choose classes, fill in a registration form (수강신청서) with nine credits and ask three classmates about their plans. The class periods are: 9교시 18:00~18:45; 10교시 18:55~19:40; 11교시 19:50~20:35; 12교시 20:45~21:30. The timetable (course; department; credits; day and period; room):",
             tables=[table(["과목", "개설학과", "학점", "시간 (교시)", "강의실"], _TT1)]),
        card("Activities left out", "The picking of classes, the registration form and the classmate interviews need the form and classmates."),
    ],
    exercises=uniq(
        _tr(_NEWS[1:], k=3)
        + [M("What do natural sciences applicants prefer?", "Departments favorable for employment", ["Foreign languages", "Arts", "Education"], "취업에 유리한 학과."), M("What do humanities applicants prefer?", "Foreign-language-related departments", ["Computer science", "Medicine", "Law"], "외국어 관련학과."), M("Which natural sciences department took first place?", "Computer-related departments", ["Semiconductor", "Artificial intelligence", "Medicine"], "컴퓨터 관련 학과."), M("Which humanities field was first?", "Foreign languages", ["Social science", "Business", "Law"], "외국어 관련 학과."), M("How many credits does the night student want?", "Nine", ["Two", "Twelve", "Eighteen"], "9학점."), M("When is the 11교시 class?", "19:50 to 20:35", ["18:00 to 18:45", "18:55 to 19:40", "20:45 to 21:30"], "11교시."), M("How many credits are 기초물리 and 기초화학?", "Six each", ["Two each", "Three each", "One each"], "6학점."),
           F("자연계열은 취업에 ___한 학과를 선호한다. (favorable)", "유리", ["불리", "충분"], "유리하다."), F("외국어 관련 학과가 ___ 위를 차지했다. (first)", "일", ["이", "삼"], "일 위."), F("서울의 열한 개 대학의 입시 ___률을 분석했다. (competition)", "경쟁", ["합격", "등록"], "경쟁률."), F("인문계열은 외국어 관련 학과가 최상위권을 ___했다. (took)", "차지", ["제공", "부담"], "차지하다."), F("국어국문학과, 영어영문학과는 ___대학 건물에서 수업이 있다. (humanities college)", "인문", ["자연과학", "사범"], "인문대학."),
           read_q("인기학과"), read_q("자연계열은 취업에 유리한 학과를 선호한다"), read_q("외국어 관련 학과가 일 위를 차지했다"), read_q("수강신청서"), read_q("교양과목 강의시간표")]
    ),
)

# ================================================================== L5: Topic B
_B_DLG = [
    ("소희", "어, 선배, 오랜만이에요.", "Oh, senior, it’s been a while."),
    ("우진", "그래, 오랜만이다. 잘 지내?", "Yeah, it’s been a while. How are you?"),
    ("소희", "네. 언제 제대했어요?", "Fine. When were you discharged?"),
    ("우진", "응. 지난달에 제대해서 다음 학기에 복학해.", "Yeah. I was discharged last month, so I’ll come back to school next semester."),
    ("소희", "그래요? 저는 다음 학기에 휴학해요. 아르바이트를 하면서 등록금을 벌려고요.", "Is that so? I’m taking a leave of absence next semester. I’m going to earn my tuition while working part-time."),
    ("우진", "그래? 무슨 일을 하려고?", "Really? What job are you going to do?"),
    ("소희", "중고생 영어과외 하려고요. 그런데 요즘 학교 축제기간인데, 선배는 특별한 계획 있어요?", "I’m going to tutor middle and high schoolers in English. By the way, it’s the school festival period these days; do you have any special plans, senior?"),
    ("우진", "아니. 요즘에 학교 앞 식당에서 아르바이트하고 있어. 그래서 조금 바빠.", "No. These days I’m working part-time at a restaurant in front of the school. So I’m a little busy."),
    ("소희", "그렇구나. 선배도 식당일 말고 과외 아르바이트를 하면 어때요?", "I see. How about you also doing a tutoring part-time job instead of restaurant work?"),
    ("우진", "가르치는 것은 내 적성에 안 맞아. 참, 소희야. 내가 자취방을 찾고 있는데, 혹시 아는 곳 있어?", "Teaching doesn’t suit my aptitude. Oh, Sohee. I’m looking for a rented room; do you happen to know of a place?"),
    ("소희", "방을 옮기시려고요?", "You’re going to move rooms?"),
    ("우진", "응. 지금 하숙하고 있는데 하숙비가 너무 비싸. 그래서 자취를 할 생각이야.", "Yes. I’m boarding now but the boarding fee is too expensive. So I’m thinking of cooking for myself in a rented room."),
]
_B_WORDS = ["그만두다", "등록금", "~말고 / -지 말고", "복학", "부족", "자취", "장학금", "적성", "축제", "충분", "하숙", "학비", "학생회"]
_KB = "College freshmen participate in several major events in their first year. In February they usually attend a welcome meeting known as 신입생 환영회 or 신입생 오리엔테이션. At this meeting, freshmen learn about college life and meet with seniors and faculty members. Once they officially start college in March, they usually go on a school excursion called MT (membership training), which is designed to strengthen the bonds between students. They also participate in a campus festival (대학축제), either in mid-spring or autumn. Activities such as contests and concerts are offered during the campus festival.\n\nWhen Korean students attend college near their parents’ home, they usually live with their parents and commute. However, when attending college away from home, students often must choose one of the following living arrangements: a boarding house (하숙집), a rented room (자취방), an on-campus dormitory (기숙사), or a home of their relatives (친척집). 하숙집 usually provides a private room and two meals, and 자취방 requires that students cook their own meals. 자취 is cheaper than 하숙. Students living at a boarding house are called 하숙생; students living in a rented room are called 자취생. Koreans refer to living at a boarding house as 하숙하다 and to living in a rented room as 자취하다.\n\nLike most college students, Korean students have many concerns. Career path is the top concern (60.0%), followed by academic performance (25.2%), financial difficulties (9.5%), adaptation to university life (4.2%), and other (1.1%). Data in the chart reflect survey results of 28,247 respondents from 283 colleges in 2017."
_QB = [("이번에 한국 대학 물리학과에 합격했습니다.", "I passed the physics department of a Korean university this time."), ("대학 생활에 대해 알고 싶은 것이 많아요.", "There are many things I want to know about college life."), ("대학에 가면 어떤 활동을 할 수 있나요?", "What activities can I do if I go to college?"), ("그리고 대학 생활을 잘 하려면 어떻게 해야 하나요?", "And what should I do to do well in college life?"), ("우선 합격을 축하합니다.", "First of all, congratulations on passing."), ("저는 얼마 전에 제대하고 다음 학기에 복학해요.", "I was discharged not long ago and will return to school next semester."), ("대학에서는 공부만 하는 것이 아닙니다.", "In college you don’t only study."), ("동아리 활동, 학과 엠티, 축제, 아르바이트, 학생회 활동 등 할 것이 아주 많아요.", "There is a lot to do: club activities, department MT, festivals, part-time jobs, student association activities and so on."), ("일 학년, 이 학년 때는 여러 가지 활동을 많이 하세요.", "In your first and second years, do many different activities."), ("동아리 활동이나 학생회 활동을 하면 선배와 후배를 많이 알 수 있어 좋습니다.", "If you do club or student association activities, it is good because you can get to know many seniors and juniors."), ("그리고 아르바이트도 해 보세요.", "And try a part-time job too."), ("용돈도 벌 수 있고 좋은 사회 경험이 됩니다.", "You can earn spending money and it becomes a good social experience."), ("보통 삼 학년, 사 학년이 되면 취업 준비를 시작합니다.", "Usually when you become a third- or fourth-year student, you start preparing for employment."), ("전공 공부도 열심히 하고 영어, 인턴사원 등 많은 준비를 해야 합니다.", "You have to study your major hard and also make many preparations such as English and an internship.")]
L5 = lesson(
    "Ch 34 · Topic B: I’m coming back to school next semester (다음 학기에 복학해)",
    "다음 학기에 복학해 · 휴학 · 등록금 · 아르바이트 · 하숙 · 자취 · 축제 · 신입생 환영회 · 대학 생활 Q&A",
    requires=[],
    cards=[
        card("Topic B: I’m coming back to school next semester (다음 학기에 복학해)",
             "Two college students are discussing college life. (The English is mine; the book gives none.)",
             examples=dlg(_B_DLG)),
        card("한국에서는: college life, housing and concerns", _KB),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 복학(하다), 부족(하다), 자취(하다), 충분(하다) and 하숙(하다) take the form in parentheses; ~말고/–지 말고 is explained in the grammar.",
             tables=[ktable(_rows([w for w in _B_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["~말고 / -지 말고", "(do) not … but"]])]),
        card("Follow-up 2 (Reading): a Q&A about college life",
             "The following Q&A about college life is posted on a website (지식 Q/A > 대학 > 대학 생활), titled 대학 신입생이 됩니다 (I’m becoming a college freshman), by user freshman12 (the date and view count are left out). The book asks you to fill in a table in English: information about the questioner and the respondent, the college activities mentioned, and advice for freshmen/sophomores and juniors/seniors. The book glosses MT = membership training, school excursion; 용돈: allowance. The text is the book’s with the school years spelled out; the English is mine.",
             examples=passage(_QB)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Item", "Answer (mine)"], [["Questioner", "Has just passed the physics department of a Korean university and wants to know about college life"], ["Respondent", "Was discharged not long ago and returns to school next semester"], ["College activities", "Club activities, department MT, festivals, part-time jobs, student association activities"], ["Advice for freshmen/sophomores", "Do many kinds of activities; clubs and the student association let you know seniors and juniors; try a part-time job for spending money and social experience"], ["Advice for juniors/seniors", "Begin preparing for employment; study the major hard and prepare English and an internship"]])]),
        card("Activities left out", "The sentence strips for Sohee and Woojin (arranging the conversation in order and reading in pairs), Follow-up 1 (listening to three conversations between a younger student and a senior about tuition, a part-time job or housing) and the SMART Board activity are audio, paper and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG) + _QB, k=3)
        + [M("When was 우진 discharged?", "Last month", ["Last year", "Next month", "Yesterday"], "지난달에 제대해서."), M("What will 우진 do next semester?", "Return to school", ["Take a leave", "Graduate", "Quit"], "복학해."), M("What will 소희 do next semester?", "Take a leave of absence", ["Return to school", "Graduate", "Study abroad"], "휴학해요."), M("Why will 소희 work part-time?", "To earn her tuition", ["For fun", "For a trip", "For a car"], "등록금을 벌려고요."), M("What part-time job will 소희 do?", "English tutoring for middle and high schoolers", ["Restaurant work", "Delivery", "Teaching Korean"], "중고생 영어과외."), M("Where is 우진 working part-time?", "A restaurant in front of the school", ["A library", "A school", "A store"], "학교 앞 식당."), M("Why doesn’t 우진 want to tutor?", "Teaching doesn’t suit his aptitude", ["It pays little", "It is far", "He is shy"], "내 적성에 안 맞아."), M("Why does 우진 want to move?", "Boarding costs too much", ["It is noisy", "It is far", "He dislikes it"], "하숙비가 너무 비싸."),
           F("저는 다음 학기에 ___해요. (take a leave)", "휴학", ["복학", "졸업"], "휴학."), F("아르바이트를 하면서 ___을 벌려고요. (tuition)", "등록금", ["장학금", "용돈"], "등록금."), F("가르치는 것은 내 ___에 안 맞아. (aptitude)", "적성", ["전공", "학점"], "적성."), F("선배도 식당일 ___ 과외 아르바이트를 하면 어때요? (instead of)", "말고", ["처럼", "같이"], "~말고."), F("지금 ___하고 있는데 하숙비가 너무 비싸. (boarding)", "하숙", ["자취", "복학"], "하숙."),
           read_q("다음 학기에 복학해"), read_q("저는 다음 학기에 휴학해요"), read_q("가르치는 것은 내 적성에 안 맞아"), read_q("하숙비가 너무 비싸"), read_q("동아리 활동, 학과 엠티, 축제, 아르바이트, 학생회 활동 등 할 것이 아주 많아요")]
    ),
)

# ================================================================== L6: Grammar A: double negatives
_DN1 = [("앤드류 짐먼은 한국음식을 다 먹을 수 있어요.", "Andrew Zimmern can eat any Korean food."), ("앤드류 짐먼은 못 먹는 한국음식이 없어요.", "There is no Korean food that Andrew Zimmern cannot eat!")]
_DN2 = [("저희 가게에는 없는 물건이 없어요.", "There are no things we do not have in our store. (literal meaning) / Our store has everything! (intended meaning)"), ("제 남자 친구는 못 하는 운동이 없어요.", "There is no sport my boyfriend cannot do. (literal meaning) / My boyfriend can do any type of sport. (intended meaning)"), ("서 교수님을 모르는 사람이 없어요.", "There is no one who does not know Professor Seo. (literal meaning) / Everyone knows who Professor Seo is. (intended meaning)"), ("한국 드라마를 안 본 학생이 없어요.", "There is no student who has not seen Korean drama. (literal meaning) / Every student has seen Korean drama. (intended meaning)")]
_AD = [("창영 가구 백화점", "Changyeong Furniture Department Store"), ("아직도 저희 백화점을 모르십니까?", "Do you still not know our department store?"), ("누구나 다 아는 가구 백화점", "The furniture department store everyone knows"), ("모르는 사람이 아무도 없는 창영 가구 백화점", "Changyeong Furniture Department Store, which no one fails to know"), ("없는 가구가 없습니다", "There is no furniture we do not have"), ("오늘 저희 백화점에 놀러 오세요", "Come visit our department store today"), ("가구에 대해 모르는 게 없는 직원들이 친절하게 상담해 드립니다.", "Staff who know everything about furniture will kindly advise you.")]
_DNF = [("없는 물건이 없어요", "Everything exists; “no thing is lacking”"), ("못 하는 운동이 없어요", "Can do any sport"), ("모르는 사람이 없어요", "Everyone knows"), ("안 본 학생이 없어요", "Every student has seen it"), ("안 마셔 본 술이 없어요", "Has tried every drink"), ("못 먹는 음식이 없어요", "Can eat any food"), ("가 보지 않은 나라가 없어요", "Has been to every country")]
L6 = lesson(
    "Ch 34 · Grammar A: emphasis using double negatives, ~이/가 없다",
    "이중부정 · 없는 물건이 없어요 · 못 하는 운동이 없어요 · 모르는 사람이 없어요 · 안 본 학생이 없어요",
    requires=[],
    cards=[
        card("Compare the two sentences",
             "Compare the following two sentences (the English is the book’s). Although both sentences convey the same meaning, the second sentence contains double negatives (못 and 없어요) and emphasizes that Andrew can eat any Korean food. Koreans use double negatives for emphasis. In this chapter, you will practice sentences that contain double negatives and end in ~이/가 없다.",
             examples=passage(_DN1)),
        card("More examples", "The book’s examples, with the literal and intended meanings (the English is the book’s):", examples=passage(_DN2)),
        card("Patterns (mine)", "negative verb in attributive form + noun + 이/가 없어요 = “there is no … that does not …”, i.e. “every …”.",
             tables=[table(["Pattern", "Intended meaning (mine)"], [list(r) for r in _DNF], say=[0])]),
        card("Follow-up 1 (Reading): a furniture department store advertisement",
             "The book gives an advertisement for furniture sold at a department store and asks you to underline all the sentences that contain a double negative and translate them into English. The advertisement is the book’s (the exclamation marks are left out; the address 광주 북구 누문동 235-9 and the telephone number 062-487-2903 are not read out). The English is mine.",
             examples=passage(_AD)),
        card("The sentences with double negatives, translated (mine)", "The book leaves the lines blank; these are my answers.",
             tables=[table(["Sentence with a double negative", "English (mine)"], [["모르는 사람이 아무도 없는 창영 가구 백화점", "Changyeong Furniture Department Store, which no one fails to know"], ["없는 가구가 없습니다", "There is no furniture we do not have (we have every kind of furniture)"], ["가구에 대해 모르는 게 없는 직원들이 친절하게 상담해 드립니다.", "Staff who know everything about furniture (there is nothing they do not know) will kindly advise you"]], say=[0])]),
        card("Activities left out", "Follow-up 2 (listening to four conversations and translating the sentence with a double negative) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_DN1 + _DN2 + _AD[1:], k=3)
        + [M("What do double negatives do in Korean?", "Emphasize", ["Soften a statement", "Ask a question", "Make a request"], "The book’s note."), M("What does 저희 가게에는 없는 물건이 없어요 mean (intended)?", "Our store has everything", ["Our store is empty", "Our store is closed", "Our store has nothing new"], "Intended meaning."), M("What does 제 남자 친구는 못 하는 운동이 없어요 mean (intended)?", "My boyfriend can do any sport", ["My boyfriend dislikes sports", "My boyfriend cannot do any sport", "My boyfriend watches sports"], "Intended meaning."), M("What does 서 교수님을 모르는 사람이 없어요 mean (intended)?", "Everyone knows Professor Seo", ["No one likes him", "Few know him", "He knows everyone"], "Intended meaning."), M("What does 한국 드라마를 안 본 학생이 없어요 mean (intended)?", "Every student has seen Korean dramas", ["No student likes them", "Few students watch them", "I haven’t seen them"], "Intended meaning."),
           F("앤드류 짐먼은 못 먹는 한국음식이 ___! (there is none)", "없어요", ["많아요", "있어요"], "없어요."), F("저희 가게에는 없는 물건이 ___. (there is none)", "없어요", ["많아요", "있어요"], "없어요."), F("서 교수님을 ___ 사람이 없어요. (who does not know)", "모르는", ["아는", "만난"], "모르는."), F("한국 드라마를 ___ 학생이 없어요. (who has not watched)", "안 본", ["본", "보는"], "안 본."), F("제 남자 친구는 ___ 운동이 없어요. (that he cannot do)", "못 하는", ["잘 하는", "좋아하는"], "못 하는."),
           read_q("저희 가게에는 없는 물건이 없어요"), read_q("제 남자 친구는 못 하는 운동이 없어요"), read_q("서 교수님을 모르는 사람이 없어요"), read_q("한국 드라마를 안 본 학생이 없어요"), read_q("가구에 대해 모르는 게 없는 직원들이 친절하게 상담해 드립니다")]
    ),
)

# ================================================================== L7: Grammar B: -지 말고 / ~말고
_ML1 = [("교실에서 영어를 하지 마세요.", "Please do not speak English in the classroom."), ("교실에서 영어를 하지 말고 한국말을 하세요.", "Please do not speak English in the classroom, but speak Korean. / Please speak Korean in the classroom instead of speaking English.")]
_ML2 = [("수업시간에 떠들지 말고 공부하세요.", "Please do not make noises but study in class. / Please study instead of making noise."), ("김 상병, 졸지 말고 일어서세요.", "Please do not doze off but stand up, PFC Kim.")]
_ML3 = [("금요일 말고 토요일에 만납시다.", "Let’s meet Saturday instead of (meeting) Friday."), ("영어 말고 한국말을 하세요.", "Please speak Korean instead of (speaking) English.")]
_ML4 = [("오늘은 놀지 말고 공부하세요.", "Do study today, instead of playing."), ("오늘 점심 먹지 말고 저녁 먹을까요?", "How about having dinner, instead of having lunch?"), ("오늘 점심 말고 저녁 먹을까요?", "How about having dinner, instead of lunch?")]
_MLM = [("공원에서 산책하지 말고 영화를 볼까요?", "How about watching a movie instead of taking a walk in the park?"), ("운동 말고 영화를 봅시다.", "Let’s watch a movie instead of exercising.")]
_MLV = [("떠들다", "to make noise", "떠들지 말고"), ("졸다", "to doze off", "졸지 말고"), ("놀다", "to play", "놀지 말고"), ("먹다", "to eat", "먹지 말고"), ("하다", "to do", "하지 말고"), ("가다", "to go", "가지 말고"), ("마시다", "to drink", "마시지 말고")]
L7 = lesson(
    "Ch 34 · Grammar B: expressing “please do not … but”, –지 말고 / ~말고",
    "-지 말고 · ~말고 · 떠들지 말고 공부하세요 · 졸지 말고 일어서세요 · 금요일 말고 토요일에",
    requires=[],
    cards=[
        card("–지 마세요 turns into –지 말고",
             "Compare the following two sentences (the English is the book’s). The expression –지 마세요, which you learned in Chapter 4, is used to make a request or command to not do something, as in the first sentence. However, when the request or command is immediately followed by another request or command, –지 마세요 turns into –지 말고, as in the second sentence. Thus, –지 말고 can translate to “do not do [something] but” or “instead of doing [something]”.",
             examples=passage(_ML1)),
        card("More examples with –지 말고", "The book’s examples (the English is the book’s):", examples=passage(_ML2)),
        card("When the same verb is used for both requests: ~말고",
             "When the same verb is used for both requests, the first verb is dropped. In this case, 말고 is used. The book writes the dropped parts in parentheses: 금요일(에 만나지) 말고 토요일에 만납시다; 영어(를 하지) 말고 한국말을 하세요. (The English is the book’s.)",
             examples=passage(_ML3)),
        card("More examples", "Here are more example sentences with –지 말고 or ~말고. (The English is the book’s.)", examples=passage(_ML4)),
        card("Forms (mine)", "Verb stem + 지 말고 (the same for all verbs); noun + 말고.",
             tables=[table(["Verb", "Meaning", "-지 말고"], [list(r) for r in _MLV], say=[0, 2])]),
        card("Follow-up 3 (Speaking and listening): the model", "In pairs, one partner reads a phrase or word from a list and the other makes a sentence using –지 말고 / ~말고. The book’s model (the English is mine):", examples=dlg([("A", "공원에서 산책하다.", "To take a walk in the park."), ("B", _MLM[0][0], _MLM[0][1]), ("B", "운동.", "Exercise."), ("A", _MLM[1][0], _MLM[1][1])])),
        card("Activities left out", "The word lists given by the teacher and Follow-up 4 (listening to three conversations and writing the suggested activity and the alternative) need lists, audio and a partner."),
    ],
    exercises=uniq(
        _tr(_ML1 + _ML2 + _ML3 + _ML4 + _MLM, k=3)
        + [M("What does –지 마세요 express?", "A request or command not to do something", ["A wish", "A question", "A past action"], "The book’s note."), M("When does –지 마세요 turn into –지 말고?", "When another request or command follows immediately", ["In a question", "In the past", "With a noun"], "The book’s note."), M("How can –지 말고 be translated?", "“do not … but” or “instead of doing”", ["“because of”", "“until”", "“if”"], "The book’s note."), M("When is ~말고 used?", "When the same verb is used for both requests", ["When the verbs differ", "In a question", "Only in the past"], "The book’s note."), M("What does 금요일 말고 토요일에 만납시다 mean?", "Let’s meet on Saturday instead of Friday", ["Let’s meet Friday and Saturday", "Let’s not meet", "I met on Friday"], "~말고."),
           F("수업시간에 떠들___ 공부하세요. (-지 말고)", "지 말고", ["지 마세요", "고 말고"], "-지 말고."), F("김 상병, 졸지 ___ 일어서세요. (but)", "말고", ["마세요", "않고"], "-지 말고."), F("금요일 ___ 토요일에 만납시다. (instead of)", "말고", ["처럼", "같이"], "~말고."), F("오늘은 놀지 말고 ___. (study)", "공부하세요", ["노세요", "자세요"], "공부하세요."), F("오늘 점심 말고 ___ 먹을까요? (dinner)", "저녁", ["아침", "간식"], "저녁."),
           read_q("교실에서 영어를 하지 말고 한국말을 하세요"), read_q("수업시간에 떠들지 말고 공부하세요"), read_q("김 상병, 졸지 말고 일어서세요"), read_q("금요일 말고 토요일에 만납시다"), read_q("오늘 점심 말고 저녁 먹을까요")]
    ),
)

# ================================================================== L8: Activities (Topic B): freshman survey
_SV = [("한국대학교 학생상담센터는 올해 신입생 삼천오백 명을 대상으로 대학생활과 관련한 설문 조사결과를 이십 일 발표했다.", "The Hanguk University Student Counseling Center announced on the 20th the results of a survey on college life covering 3,500 freshmen this year."), ("조사 결과, 대학 입학 후 고민을 묻는 질문에 학비문제, 삼십오 점 팔 퍼센트라고 대답한 학생이 가장 많았다.", "In the results, the most students answered tuition problems (35.8%) to the question asking about worries after entering college."), ("다음으로 학교 전공공부, 이십오 퍼센트, 시간관리, 십사 점 육 퍼센트, 취업문제, 십삼 점 사 퍼센트, 이성교제, 삼 점 사 퍼센트, 기타, 칠 점 팔 퍼센트 등의 순으로 대답했다.", "Next, they answered in the order of major studies (25%), time management (14.6%), employment (13.4%), dating (3.4%), other (7.8%) and so on."), ("신입생의 대부분이 아르바이트를 원했고, 아르바이트를 하는 이유로는 용돈, 육십일 점 일 퍼센트, 학비, 이십육 점 구 퍼센트, 사회경험, 오 점 일 퍼센트, 생활비, 삼 점 구 퍼센트, 기타, 삼 퍼센트 등을 꼽았다.", "Most freshmen wanted part-time jobs, and as reasons for working part-time they chose spending money (61.1%), tuition (26.9%), social experience (5.1%), living expenses (3.9%), other (3.0%) and so on.")]
L8 = lesson(
    "Ch 34 · Topic B activities: a survey of college freshmen",
    "신입생 설문조사 · 학비문제 · 전공공부 · 시간관리 · 취업문제 · 이성교제 · 용돈 · 생활비 · 사회경험",
    requires=[],
    cards=[
        card("Activity 4 (Reading): a news article about a survey of college freshmen",
             "The following news article is about a survey covering aspects of college freshman life. The book gives the hint to focus on the words you know; it asks you to write English titles for two pie charts (the charts are pictures and are left out) and fill in a table for each chart. The text is the book’s, with the numbers, dates and percentages spelled out in Hangul; the English is mine.",
             examples=passage(_SV)),
        card("The charts, labelled (mine)", "The pie-chart slices 가 to 바 (Chart A) and A to E (Chart B) are labelled in the book’s table, partly (다 = time management, 마 = dating, 바 = other; A = earning personal expenses, C = social experience, E = other). The titles and the full labels, from the article (mine):",
             tables=[table(["Chart", "Title (mine)", "Slices (mine)"], [["A", "Worries after entering college (3,500 freshmen)", "가 tuition (35.8%); 나 major studies (25%); 다 time management (14.6%); 라 employment (13.4%); 마 dating (3.4%); 바 other (7.8%)"], ["B", "Reasons freshmen work part-time", "A spending money (61.1%); B tuition (26.9%); C social experience (5.1%); D living expenses (3.9%); E other (3.0%)"]])]),
        card("Activities left out", "Activity 1 (Two-in-One Vocabulary Review, SMART Board), Activity 2 (listening to two conversations about a concern and advice), Activity 3 (a video clip from the drama “Rooftop Romance”) and Activity 5 (a role-play about concerns and advice about college life, with a table to jot down ideas) are audio, video, computer and partner activities."),
    ],
    exercises=uniq(
        _tr(_SV, k=3)
        + [M("How many freshmen were surveyed?", "3,500", ["350", "35,000", "500"], "삼천오백 명."), M("What worry was the most common?", "Tuition", ["Dating", "Employment", "Time management"], "학비문제."), M("Which worry came second?", "Major studies", ["Time management", "Tuition", "Dating"], "학교 전공공부."), M("Which worry was the least common in the list?", "Dating", ["Time management", "Employment", "Tuition"], "이성교제 삼 점 사 퍼센트."), M("What is the most common reason for working part-time?", "Spending money", ["Tuition", "Social experience", "Living expenses"], "용돈."), M("Which reason came second?", "Tuition", ["Spending money", "Living expenses", "Social experience"], "학비."),
           F("한국대학교 학생상담센터는 올해 신입생 삼천오백 명을 ___으로 조사했다. (target)", "대상", ["이유", "제공"], "대상."), F("학비문제라고 ___한 학생이 가장 많았다. (answered)", "대답", ["부탁", "문의"], "대답하다."), F("아르바이트를 하는 ___로는 용돈이 가장 많았다. (reason)", "이유", ["대상", "과정"], "이유."), F("신입생의 대부분이 아르바이트를 ___. (wanted)", "원했다", ["그만두었다", "마쳤다"], "원하다."), F("다음으로 학교 전공공부, 시간관리, ___문제 등의 순으로 대답했다. (employment)", "취업", ["학비", "이성"], "취업문제."),
           read_q("학생상담센터"), read_q("학비문제라고 대답한 학생이 가장 많았다"), read_q("신입생의 대부분이 아르바이트를 원했다"), read_q("용돈"), read_q("생활비")]
    ),
)

# ================================================================== L9: Topic C
_C_DLG = [
    ("준태", "민영아, 졸업한 다음에 뭐 할 거야?", "Minyeong, what are you going to do after graduating?"),
    ("민영", "난 미국으로 유학 갈 거야. 석사 과정에 들어가고 싶어.", "I’m going to study in America. I want to enter a master’s program."),
    ("준태", "그래? 미국 대학원에 들어가기가 어렵지?", "Really? It’s hard to get into an American graduate school, isn’t it?"),
    ("민영", "응. 자격 조건이 까다로워. 특히 영어를 잘 해야 해. 그래서 며칠 전에 어학원에 등록했어.", "Yes. The qualification requirements are demanding. You especially have to be good at English. So I enrolled in a language institute a few days ago."),
    ("준태", "그렇구나. 참, 현수도 유학 준비한대. 현수랑 같이 공부해 봐.", "I see. Oh, I hear Hyunsoo is also preparing to study abroad. Try studying together with Hyunsoo."),
    ("민영", "좋은 생각이야. 현수는 미국에 어학 연수도 갔다 왔지?", "Good idea. Hyunsoo also went on a language study program in America, didn’t he?"),
    ("준태", "응. 그래서 영어 회화를 아주 잘 해. 나도 현수같이 영어를 잘 하면 좋겠어. 영어는 정말 어려워.", "Yes. So he’s very good at conversational English. I wish I could speak English as well as Hyunsoo. English is really hard."),
    ("민영", "맞아. 영어는 공부할수록 어려운 것 같아. 참, 넌 진로 결정했어?", "Right. English seems to get harder the more you study. Oh, have you decided on your career path?"),
    ("준태", "응. 난, 취업할 생각이야. 그런데 요즘 일자리가 별로 없어서 걱정이야.", "Yes. I’m thinking of getting a job. But I’m worried because there aren’t many jobs these days."),
    ("민영", "그래도 넌 자격증도 많고 학점도 좋잖아. 그러니까 취직이 잘 될 거야.", "Still, you have many certificates and good grades. So you’ll surely get a job."),
]
_C_WORDS = ["~같이 / 처럼 / 같은", "과정 / 코스", "등록", "마치다", "박사", "부담", "석사", "어학 연수", "어학원", "-(으)ㄹ수록", "인턴(사원)", "일자리", "자격", "자격증", "제공", "진로", "취업 / 취직", "학사", "학위", "회화"]
_FLY = [("이천이십삼 한미 여름 어학연수 프로그램 참가자 모집", "Recruiting participants for the 2023 Korea-U.S. summer language study program"), ("주한미국대사관", "U.S. Embassy in Korea"), ("한미 여름 어학연수 프로그램은 이천이십삼 년 칠 월 삼 일부터 사 주 동안 미국 동부에 위치한 대학 세 곳에서 진행됩니다.", "The Korea-U.S. summer language study program will be held for four weeks starting on July 3, 2023, at three universities located on the U.S. East Coast."), ("지원 자격 요건", "Application eligibility requirements"), ("현재 한국의 대학에 다니는 학생.", "Students currently attending a university in Korea."), ("특별 활동에 적극적으로 참여한 학생.", "Students who have actively participated in special activities."), ("미국 유학 경험이 거의 또는 전혀 없는 학생.", "Students with little or no experience studying in the U.S."), ("영어 능력", "English ability"), ("현재 영어 능력에 상관없이 누구나 지원할 수 있습니다.", "Anyone can apply regardless of current English ability."), ("학생들은 프로그램 시작 전, 간단한 영어 능력 시험을 보고 그 결과에 따라 반을 나누게 됩니다.", "Before the program starts, students will take a simple English proficiency test and be divided into classes according to the results."), ("장학금 지원", "Scholarship support"), ("이 프로그램은 전액 장학금이 지원됩니다.", "This program is supported by a full scholarship."), ("주한미국대사관은 학비, 주거비용, 식비, 교통비 및 국제선 항공료 등 참가자의 모든 비용을 전액 지원합니다.", "The U.S. Embassy in Korea fully covers all participants’ costs, such as tuition, housing costs, food costs, transportation costs and international airfare."), ("지원 방법", "How to apply"), ("이 프로그램에 관심있는 학생들은 지원서와 모든 제출 서류들을 이천이십이 년 삼 월 십삼 일 전까지 이메일 주소로 제출하시면 됩니다.", "Students interested in this program can submit the application and all required documents to the e-mail address by March 13, 2022 (as the book prints the year).")]
L9 = lesson(
    "Ch 34 · Topic C: What will you do after you graduate? (졸업한 다음에 뭐 할 거야?)",
    "졸업한 다음에 뭐 할 거야 · 유학 · 석사 과정 · 자격 조건 · 어학원 · 어학 연수 · 진로 · 취업 · 자격증 · 어학연수 프로그램 모집",
    requires=[],
    cards=[
        card("Topic C: What will you do after you graduate? (졸업한 다음에 뭐 할 거야?)",
             "Two Korean college students are talking about their plans for after graduation. (The English is mine; the book gives none.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 등록(하다), 부담(하다/되다), 제공(하다/되다) and 취업/취직(하다) take the forms in parentheses; ~같이/처럼/같은 and –(으)ㄹ수록 are explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["~같이 / 처럼 / 같은", "like"], ["-(으)면 -(으)ㄹ수록", "the more … (the more)"]])]),
        card("Follow-up 1 (Reading): a flyer for a Korea–U.S. language exchange program",
             "The flyer is about a Korea–U.S. language exchange program. The book asks you to fill in a table in English: period of event; location; eligible candidates; English ability; scholarship; how to apply. The flyer is the book’s with the dates and numbers spelled out in Hangul; the e-mail address is not read out (AmericanEnglishSeoul@state.gov). The English is mine.",
             examples=passage(_FLY)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Item", "Answer (mine)"], [["Period of event", "Four weeks from July 3, 2023"], ["Location", "Three universities on the U.S. East Coast"], ["Eligible candidates", "Students currently at a Korean university who have actively taken part in special activities and have little or no experience studying in the U.S."], ["English ability", "Anyone may apply whatever their English; a simple English test before the program places students in classes"], ["Scholarship", "A full scholarship covering tuition, housing, food, transportation and international airfare"], ["How to apply", "E-mail the application and all required documents by March 13 (the book prints 2022)"]])]),
        card("Activities left out", "The word table for Topic C (to fill in Korean or English), the SMART Board activity and Follow-up 2 (listening to three conversations about graduation plans) are computer and audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG) + _FLY[2:3] + _FLY[11:14], k=3)
        + [M("What will 민영 do after graduating?", "Study in America for a master’s degree", ["Get a job", "Marry", "Travel"], "미국으로 유학."), M("What is difficult about American graduate school?", "The qualification requirements", ["The cost only", "The distance", "The food"], "자격 조건이 까다로워."), M("What did 민영 do a few days ago?", "Enrolled in a language institute", ["Took an exam", "Moved", "Quit a job"], "어학원에 등록했어."), M("What did 준태 suggest?", "Study together with Hyunsoo", ["Study alone", "Go to America", "Skip English"], "현수랑 같이 공부해 봐."), M("What did 현수 do in America?", "A language study program", ["A job", "A degree", "A vacation"], "어학 연수."), M("What does 준태 plan to do?", "Get a job", ["Study abroad", "Marry", "Rest"], "취업할 생각."), M("What worries 준태?", "There are few jobs these days", ["His grades", "His English", "His health"], "일자리가 별로 없어서."), M("Why will 준태 get a job well, says 민영?", "He has many certificates and good grades", ["He has money", "He has friends", "He is tall"], "자격증도 많고 학점도 좋잖아."),
           F("난 미국으로 유학 갈 거야. ___ 과정에 들어가고 싶어. (master’s)", "석사", ["박사", "학사"], "석사."), F("현수는 미국에 ___ 연수도 갔다 왔지? (language)", "어학", ["회화", "일자리"], "어학 연수."), F("넌 ___ 결정했어? (career path)", "진로", ["자격", "과정"], "진로."), F("그래도 넌 ___도 많고 학점도 좋잖아. (certificates)", "자격증", ["일자리", "학위"], "자격증."), F("나도 현수___ 영어를 잘 하면 좋겠어. (like)", "같이", ["처럼 말고", "말고"], "~같이."),
           read_q("졸업한 다음에 뭐 할 거야"), read_q("난 미국으로 유학 갈 거야"), read_q("자격 조건이 까다로워"), read_q("현수는 미국에 어학 연수도 갔다 왔지"), read_q("넌 자격증도 많고 학점도 좋잖아")]
    ),
)

# ================================================================== L10: Grammar C: like
_LK1 = [("준기는 제 동생같이 말합니다.", "Junki speaks like my younger brother."), ("준기는 제 동생처럼 말합니다.", "Junki speaks like my younger brother (the same with 처럼)."), ("준기는 동생 같은 친구예요.", "Junki is a friend of mine (who is) like my brother.")]
_LK2 = [("제임스는 한국 사람같이 한국말을 해요.", "James speaks Korean like (native) Korean people."), ("제임스는 한국 사람처럼 한국말을 해요.", "James speaks Korean like (native) Korean people (with 처럼)."), ("우리 집을 카페같이 만들었어요.", "I made my house (look) like a café."), ("우리 집을 카페처럼 만들었어요.", "I made my house (look) like a café (with 처럼)."), ("우리 누나 같은 여자와 결혼하고 싶어요.", "I would like to marry a woman like my older sister."), ("영화 같은 이야기를 들었어요.", "I heard a story (that was) like a movie.")]
_LKM = [("누가 마이클 잭슨처럼 춤을 잘 춥니까?", "Who dances well like Michael Jackson?"), ("김 일병이 마이클 잭슨같이 춤을 잘 춥니다.", "Private First Class Kim dances well like Michael Jackson."), ("최 상병은 어떤 곳에서 살고 싶어요?", "Corporal Choi, what kind of place do you want to live in?"), ("몬트레이 같은 바닷가에서 살고 싶어요.", "I want to live by a seaside like Monterey.")]
_LKQ = [("어떤 곳에서 살고 싶어요?", "What kind of place do you want to live in?"), ("어떤 음식을 먹고 싶어요?", "What kind of food do you want to eat?"), ("어떤 사람을 좋아합니까?", "What kind of person do you like?"), ("어떤 식당을 좋아합니까?", "What kind of restaurant do you like?"), ("어떤 스포츠를 잘 합니까?", "What kind of sport are you good at?"), ("어떤 영화배우를 싫어합니까?", "What kind of movie actor do you dislike?")]
_LKS = [("우리 형같이 컴퓨터를 잘하고 싶어요.", "I want to be good at computers like my older brother."), ("김 일병은 뭘 잘하고 싶어요?", "Private First Class Kim, what do you want to be good at?"), ("저는 우리 형같이 컴퓨터를 잘하고 싶어요. 그리고 최 일병처럼 농구를 잘하고 싶어요.", "I want to be good at computers like my older brother. And I want to be good at basketball like Private First Class Choi.")]
L10 = lesson(
    "Ch 34 · Grammar C: expressing likeness, ~같이 / ~처럼 and ~같은",
    "~같이 · ~처럼 · ~같은 · 동생같이 말합니다 · 동생 같은 친구 · 카페처럼 · 영화 같은 이야기",
    requires=[],
    cards=[
        card("~같이, ~처럼 and ~같은",
             "In English, when we express likeness or similarity, we use “like”, as in Bill acts like John or a brother like my best friend. The Korean equivalents of this are ~같이, ~처럼, or ~같은. However, ~같이 and ~처럼, which are interchangeable, modify a verb; whereas ~같은 modifies a noun. For example (the English is the book’s):",
             examples=passage(_LK1)),
        card("Note on the spacing", "Note that in the first sentence 동생같이 or 동생처럼 modifies the verb 말합니다; in the second sentence 동생 같은 modifies the noun 친구 that immediately follows it. Keep in mind that there is a space between a noun and 같은 (e.g., 동생 같은, not 동생같은)."),
        card("More examples", "Here are more example sentences that have ~같이/처럼 or ~같은. (The English is the book’s.)", examples=passage(_LK2)),
        card("Follow-up 1 (Listening and speaking): the models", "In pairs, one partner asks a question with a noun and verb phrase from a list and the other answers with ~같이/처럼; then they take turns asking a question from the Question List and answering with ~같은. The book’s models (the English is mine):", examples=dlg([("A", _LKM[0][0], _LKM[0][1]), ("B", _LKM[1][0], _LKM[1][1]), ("A", _LKM[2][0], _LKM[2][1]), ("B", _LKM[3][0], _LKM[3][1])])),
        card("The Question List", "The book’s six questions (the English is mine):", examples=passage(_LKQ)),
        card("Follow-up 5 (Speaking and listening): 우리 형같이 컴퓨터를 잘하고 싶어요", "You think about activities your family members or friends are good at and ask your partner what they would like to be as good at. The book’s model (the English is mine):", examples=dlg([("A", _LKS[1][0], _LKS[1][1]), ("B", _LKS[2][0], _LKS[2][1])])),
        card("Activities left out", "The word lists (List A and List B) and Follow-up 2 (listening to four conversations and translating the sentence with ~같이/처럼) need lists, audio and a partner."),
    ],
    exercises=uniq(
        _tr(_LK1 + _LK2 + _LKM + _LKQ + _LKS, k=3)
        + [M("What do ~같이 and ~처럼 modify?", "A verb", ["A noun", "A particle", "A number"], "The book’s note."), M("What does ~같은 modify?", "A noun", ["A verb", "A particle", "An adverb"], "The book’s note."), M("Are ~같이 and ~처럼 interchangeable?", "Yes", ["No", "Only in questions", "Only in the past"], "The book’s note."), M("Is there a space between a noun and 같은?", "Yes (동생 같은)", ["No (동생같은)", "Sometimes", "Only before verbs"], "The book’s note."), M("What does 영화 같은 이야기를 들었어요 mean?", "I heard a story like a movie", ["I watched a movie", "I told a story", "I like movies"], "~같은."), M("What does 제임스는 한국 사람처럼 한국말을 해요 mean?", "James speaks Korean like a native Korean", ["James is Korean", "James likes Korean people", "James teaches Korean"], "~처럼."),
           F("준기는 제 동생___ 말합니다. (like; verb)", "같이", ["같은", "말고"], "~같이."), F("준기는 동생 ___ 친구예요. (like; noun)", "같은", ["같이", "처럼"], "~같은."), F("우리 집을 카페___ 만들었어요. (like)", "처럼", ["같은", "말고"], "~처럼."), F("우리 누나 ___ 여자와 결혼하고 싶어요. (like)", "같은", ["같이", "처럼"], "~같은."), F("김 일병이 마이클 잭슨___ 춤을 잘 춥니다. (like)", "같이", ["같은", "말고"], "~같이."),
           read_q("준기는 제 동생같이 말합니다"), read_q("준기는 동생 같은 친구예요"), read_q("우리 집을 카페처럼 만들었어요"), read_q("우리 누나 같은 여자와 결혼하고 싶어요"), read_q("영화 같은 이야기를 들었어요")]
    ),
)

# ================================================================== L11: Grammar D: -(으)면 -(으)ㄹ수록
_SU1 = [("사람이 많이 오면 올수록 파티가 재미있어요.", "The more people come, the more fun the party is."), ("많으면 많을수록 즐거워요.", "The more, the merrier.")]
_SU2 = [("사람이 많이 올수록 파티가 재미있어요.", "The more people come, the more fun the party is."), ("많을수록 더 즐거워요.", "The more, the merrier.")]
_SU3 = [("날씨가 추워지면 추워질수록 감기환자가 늘어나요.", "The colder the weather gets, the more the number of patients with colds increases."), ("날씨가 추워질수록 감기환자가 늘어나요.", "The colder the weather gets, the more the number of patients with colds increases (without –(으)면)."), ("한국 음식은 먹으면 먹을수록 맛있어요.", "The more I eat Korean food, the more delicious it is."), ("한국 음식은 먹을수록 맛있어요.", "The more I eat Korean food, the more delicious it is (without –(으)면)."), ("김 선생님을 알면 알수록 존경하게 돼요.", "The more I know Mr. Kim, the more I respect him."), ("김 선생님을 알수록 존경하게 돼요.", "The more I know Mr. Kim, the more I respect him (without –(으)면).")]
_SUM = [("커피를 많이 마시면 마실수록", "the more you drink coffee"), ("커피를 많이 마시면 마실수록 밤에 잠이 안 와요.", "The more coffee you drink, the less you can sleep at night.")]
_SUV = [("많다", "to be many", "많으면 많을수록"), ("오다", "to come", "오면 올수록"), ("먹다", "to eat", "먹으면 먹을수록"), ("알다", "to know", "알면 알수록"), ("공부하다", "to study", "공부하면 공부할수록"), ("어렵다", "to be difficult", "어려우면 어려울수록"), ("춥다", "to be cold", "추우면 추울수록"), ("마시다", "to drink", "마시면 마실수록"), ("살다", "to live", "살면 살수록")]
L11 = lesson(
    "Ch 34 · Grammar D: cause and effect, –(으)면 –(으)ㄹ수록, the more … the more",
    "-(으)면 -(으)ㄹ수록 · 많으면 많을수록 · 먹으면 먹을수록 · 알면 알수록 · 공부할수록",
    requires=[],
    cards=[
        card("Double comparatives",
             "In English, we often express a cause-and-effect relationship by using double comparatives, as in “The more people come, the more fun the party is.” Note that the first comparative (clause) the more people come functions as a cause and the second comparative (clause) the more fun the party is functions as an effect. In Korean, we can express this cause-and-effect relationship by using the conjunctive ending –(으)면 –(으)ㄹ수록. For example (the English is the book’s):",
             examples=passage(_SU1)),
        card("–(으)면 is optional", "–(으)면 in –(으)면 –(으)ㄹ수록 is optional and can be deleted. (The English is the book’s.)", examples=passage(_SU2)),
        card("More examples", "Here are more example sentences with the conjunctive ending (the book writes the optional part in parentheses; both versions are given; the English is the book’s):", examples=passage(_SU3)),
        card("Forms (mine)", "Verb or adjective stem + (으)면 + the same stem + (으)ㄹ수록 (a stem ending in ㄹ drops the ㄹ: 알면 알수록; ㅂ-irregular stems change ㅂ to 우: 어려우면 어려울수록).",
             tables=[table(["Verb", "Meaning", "-(으)면 -(으)ㄹ수록"], [list(r) for r in _SUV], say=[0, 2])]),
        card("Follow-up 3 (Speaking and listening): the model", "In pairs, one partner draws a card, translates the English clause into Korean with –(으)면 –(으)ㄹ수록, and the other repeats it and adds a logical effect. The book’s model (the English is mine):", examples=dlg([("A", _SUM[0][0], _SUM[0][1]), ("B", _SUM[1][0], _SUM[1][1])])),
        card("Activities left out", "The card sets and Follow-up 4 (listening to four dialogs, identifying the topic and translating the sentence with –(으)면 –(으)ㄹ수록) need cards, audio and a partner."),
    ],
    exercises=uniq(
        _tr(_SU1 + _SU2 + _SU3[::2] + _SUM, k=3)
        + [M("What does –(으)면 –(으)ㄹ수록 express?", "A cause-and-effect relationship, “the more … the more”", ["A wish", "A command", "A past event"], "The book’s note."), M("Is –(으)면 required in –(으)면 –(으)ㄹ수록?", "No, it is optional", ["Yes, always", "Only with nouns", "Only in questions"], "The book’s note."), M("What does 많으면 많을수록 즐거워요 mean?", "The more, the merrier", ["It is not fun", "Few are better", "Nothing is fun"], "The book’s example."), M("What does 한국 음식은 먹을수록 맛있어요 mean?", "The more I eat Korean food, the more delicious it is", ["I never eat Korean food", "Korean food is not tasty", "I ate Korean food yesterday"], "-(으)ㄹ수록."), M("What does 김 선생님을 알수록 존경하게 돼요 mean?", "The more I know Mr. Kim, the more I respect him", ["I dislike Mr. Kim", "I will meet Mr. Kim", "Mr. Kim respects me"], "-(으)ㄹ수록."),
           F("사람이 많이 오면 ___ 파티가 재미있어요. (the more)", "올수록", ["오는데", "오고"], "오면 올수록."), F("많으면 ___ 즐거워요. (the more)", "많을수록", ["많아서", "많고"], "많을수록."), F("한국 음식은 먹으면 ___ 맛있어요. (the more I eat)", "먹을수록", ["먹는데", "먹고"], "먹을수록."), F("김 선생님을 알면 ___ 존경하게 돼요. (the more I know)", "알수록", ["알을수록", "아는데"], "알다 → 알수록."), F("날씨가 추워지면 추워질___ 감기환자가 늘어나요. (the more)", "수록", ["는데", "고"], "추워질수록."),
           read_q("사람이 많이 오면 올수록 파티가 재미있어요"), read_q("많으면 많을수록 즐거워요"), read_q("한국 음식은 먹으면 먹을수록 맛있어요"), read_q("김 선생님을 알수록 존경하게 돼요"), read_q("커피를 많이 마시면 마실수록 밤에 잠이 안 와요")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Loan words", _CV_LOAN), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L12 = lesson(
    "Ch 34 · Core vocabulary and self-evaluation",
    "주요 단어 · 대학 생활 · 전공 · 학점 · 진로 · 취업 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (9시간 → 아홉 시간; 1학년 → 일 학년; 5월 → 오 월; 64주 → 육십사 주)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and discuss academic majors and classes and other college-related activities like registration; identify and discuss aspects of college life, such as employment and common concerns; and discuss plans for after graduating from college.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; using double negatives for emphasis; ~말고/–지 말고 (do not … but); ~같이/처럼 and ~같은 (like); the conjunctive ending –(으)면 –(으)ㄹ수록; and the Sino-Korean syllables within 부전공 (副專攻), 교환 (交換), and 기간 (期間)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 석사 mean?", "a master’s (degree)", ["a doctoral degree", "a bachelor’s degree", "a certificate"], "碩士."), M("What does 박사 mean?", "a doctoral degree; a Ph.D.", ["a master’s degree", "a bachelor’s degree", "a license"], "博士."), M("What does 학사 mean?", "a bachelor’s (degree)", ["a master’s degree", "a doctoral degree", "a major"], "學士."), M("What does 진로 mean?", "a (future) route; a career path", ["a course", "a qualification", "a license"], "進路."), M("What does 일자리 mean?", "a job; “work spot”", ["a part-time job", "a license", "a scholarship"], "일자리."), M("What does 장학금 mean?", "a scholarship", ["tuition", "an allowance", "a salary"], "奬學金."), M("What does 등록금 mean?", "tuition; “registration money”", ["a scholarship", "an allowance", "a salary"], "登錄金."),
           F("우리 대학 ___이 계속 오르고 있어요. (tuition)", "등록금", ["장학금", "용돈"], "등록금."), F("이 대학은 ___을 받는 학생들이 많습니다. (scholarship)", "장학금", ["등록금", "학비"], "장학금."), F("유학 가서 박사 ___를 받았습니다. (degree)", "학위", ["자격", "과정"], "학위."), F("요즘은 ___하기가 너무 어렵습니다. (getting a job)", "취직", ["복학", "휴학"], "취직."), F("학점이 좋으면 ___하기 쉽습니다. (getting a job)", "취직", ["입학", "졸업"], "취직."),
           read_q("주요 단어"), read_q("대학 생활"), read_q("장학금"), read_q("진로"), read_q("자격증")]
    ),
)

UNIT = unit("Semester 2 · Unit 9 · Chapter 34: College Life (대학 생활)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
