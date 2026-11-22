"""Unit 40: KBC Semester 2, Unit 9, Chapter 33 - Education in Korea (한국의 교육).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 9, Student's Edition (Validation Edition).
Audio, pictures, graphs, the word-search grid, SMART Board activities, games, role-plays, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 33 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("각(각)", "(各(各)) respectively; each", "한국의 중학교와 고등학교는 각각 일 학년부터 삼 학년까지 있습니다."),
    ("공립", "(公立) public (institution, etc.); “publicly established”", "공립학교에 다니면 돈이 적게 듭니다."),
    ("교장", "(校長) a principal; “school chief”", "우리 학교 교장 선생님은 학생들의 이름을 다 알아요."),
    ("국립", "(國立) national (institution, etc.); “nationally established”", "요세미티 국립 공원은 아주 아름답습니다."),
    ("~년제", "(年制) length of program for a school; “year system”", "저는 이 년제 대학을 다니는데 졸업 후에 유학을 갈 생각입니다."),
    ("대학원", "(大學院) a graduate school", "대학교 졸업 후에 대학원에서 공부를 더 할 계획이에요."),
    ("따라서", "therefore; so; thus", "내년에 고삼이 됩니다. 따라서 열심히 공부해야 합니다."),
    ("사립", "(私立) private (institution, etc.); “privately established”", "아이가 크면 공립학교와 사립학교 중 어디에 보내고 싶으세요?"),
    ("실업계", "(實業系) (high school) track for a vocational career", "저는 실업계 고등학교를 졸업했어요. 그런데 공부를 더 하고 싶어서 대학에 입학했습니다."),
    ("유치원", "(幼稚園) a kindergarten", "지금도 만나는 유치원 친구가 있어요?"),
    ("의무", "(義務) obligation; duty; responsibility", "한국의 의무교육 기간은 구 년이고 북한의 의무교육 기간은 십이 년이다."),
    ("인문계", "(人文系) (high school) track for college admission or academic career", "저는 대학에 가고 싶어요. 그래서 인문계 고등학교에 가려고 합니다."),
    ("입학", "(入學) entrance into school; to enter school (~하다)", "모든 부모들은 자녀가 좋은 대학에 입학하기를 바란다."),
    ("제도", "(制度) a system", "각 나라마다 그 나라에 맞는 교육 제도가 있습니다."),
    ("졸업", "(卒業) graduation; to graduate (~하다)", "고등학교 졸업 기념으로 제주도 여행을 갑니다."),
    ("초등학교", "(初等學校) an elementary school; “early grade school”", "사립 초등학교에 다니면 비용이 많이 듭니다."),
    ("총장", "(總長) a president (of a university); “general chief”", "내일 국립 대학교 총장들이 대학 시험에 대하여 의논할 예정입니다."),
    ("~학기", "(學期) a semester; “school period”", "공부를 안 해서 일 학기 성적이 좋지 않습니다."),
    ("~학년", "(學年) school year; grade", "우리 여동생은 중학교 삼 학년이고 남동생은 초등학교 오 학년이에요."),
]
_CV_B = [
    ("결석", "(缺席) absence; to be absent; to skip class (~하다)", "어제 아파서 학교에 결석했습니다."),
    ("과목", "(科目) a(n) (academic) subject", "고등학교 때 제일 좋아했던 과목이 무엇이었어요?"),
    ("과학", "(科學) science", "과학 과목은 좋아했지만 과학 선생님은 싫었어요."),
    ("교내", "(校內) in the school; on campus; intra(collegiate/school); “school inside”", "다음 주에 교내 영어대회가 있어요."),
    ("~교시", "(校時) a period (of a class); an hour (of a class)", "월요일 오 교시는 음악시간이에요."),
    ("국어", "(國語) (the) Korean (language); the national language", "국어를 잘 모르면 외국어도 잘 배울 수 없어요."),
    ("급식", "(給食) school lunch; (provision of school) meals; to provide meals (~하다)", "어제 학교급식을 먹었는데 설사를 했어요."),
    ("늦잠", "oversleeping; “late sleep”; to oversleep (~자다)", "어제 늦잠을 자서 학교에 지각했어요."),
    ("담임(선생)", "(擔任(先生)) a homeroom teacher; “teacher in charge”", "저는 담임선생님이 아주 좋아요."),
    ("도덕", "(道德) morality; ethics; moral class; “ways and virtues”", "도덕시간이 일주일에 두 시간 있습니다."),
    ("도시락", "a lunch box", "어머니께서 매일 점심 도시락을 싸 주십니다."),
    ("방과 후", "(放課 後) after class", "방과 후에는 학원에 가야 돼서 너무 바빠요."),
    ("사회", "(社會) social studies; “society”", "제가 좋아하는 과목은 국어와 사회예요."),
    ("수학", "(數學) math; “study of numbers”", "수학 시험을 잘 못 봐서 학원에 다녀야겠어요."),
    ("시간표", "(時間表) a timetable; a (class) schedule", "새 학기가 시작되어서 시간표를 새로 받았습니다."),
    ("실력", "(實力) ability; proficiency; competence; “real power”", "요즘 영어 실력이 많이 늘었어요."),
    ("야단맞다 / 혼나다", "to be scolded; to be berated", "동생하고 싸워서 부모님한테 혼났어요."),
    ("웅변", "(雄辯) a speech; eloquence; fluency (of speech)", "다음 달에 웅변 대회가 있어서 연습하고 있습니다."),
    ("자율학습", "(自律學習) self-study", "일 교시는 보통 자율학습 시간입니다."),
    ("지각", "(遲刻) being late; tardiness; to be late; to be tardy (~하다)", "아침에 지각하지 않으려고 집에서 일찍 나왔어요."),
    ("체육", "(體育) physical education", "저는 학교에 다닐 때 체육시간을 가장 좋아했어요."),
    ("칭찬", "(稱讚) praise; commendation; to praise; to commend; to compliment (~하다)", "칭찬을 받으면 기분이 좋아집니다. 우리 서로 자주 칭찬해 줍시다."),
    ("한문", "(漢文) Chinese writing", "방학 동안 한문을 무료로 가르치는 곳이 많아요."),
]
_CV_C = [
    ("결심", "(決心) a resolution; “determination of the heart”; to be determined (~하다)", "올해부터는 열심히 한국어를 공부하기로 결심했어요."),
    ("과외", "(課外) extracurricular lesson; private lesson; private tutoring; “outside work”; to do an extracurricular lesson / to receive private lessons (~하다/받다)", "한국학생들은 영어와 수학 과외를 많이 받습니다."),
    ("교제", "(交際) association; friendship; company; dating; “meeting each other”; to associate with (~하다)", "요즘 이성 교제 때문에 고민하는 학생들이 많습니다."),
    ("기말", "(學期末) end of semester; semester end", "학생들은 학기말이 되면 바빠집니다."),
    ("동네", "a (small) town; neighborhood", "우리 동네에는 유명한 해수욕장이 있어요."),
    ("등 / 등수", "(等數) the ~th (in rank); ranking", "지난 학기말 시험에서 제 동생이 일 등을 했어요. 시험을 못 봐서 반 등수가 떨어졌어요."),
    ("반대", "(反對) opposition; objection; to oppose; to object (~하다)", "이번 주말에 등산 가려고 했어요. 그런데 아내가 반대해서 집안일을 했어요."),
    ("부럽다", "to envy; to be jealous; “to be envious”", "제 친구는 여름 방학에 유럽으로 여행가요. 너무 부러워요."),
    ("불합격", "(不合格) failure; “not passing”; to fail (a test) (~하다)", "올해 대학 시험에 불합격하면 내년에 다시 봐야 해요."),
    ("성적", "(成績) (academic) grades; academic performance; academic report; “successful accumulation”", "고등학교 성적이 좋아서 원하는 대학에 갈 수 있었어요."),
    ("성적표", "(成績表) a report card; a transcript; “academic performance table”", "학기말 시험이 끝났으니까 곧 성적표가 집으로 올 거에요."),
    ("속상하다", "to be upset; “the inside hurts”", "이번 크리스마스에 고향에 못 가서 속상해요."),
    ("시키다", "to make (a person do something); to order (food)", "어머니가 저한테 방을 청소하라고 시키셨어요."),
    ("입시", "(入試) an entrance examination; acronym for 입학 시험", "제 동생은 지금 외고 입시준비를 하고 있어요."),
    ("이성", "(異性) the opposite/other gender; “different gender”", "우리 부모님은 이성 친구를 사귀는 것을 안 좋아해요."),
    ("점 / 점수", "(點數) a point/score; grades", "영어 시험에서 백 점을 받았어요. 시험 점수가 올라서 기분이 좋아요."),
    ("중간", "(中間) the middle; center; medium; interim", "중간 시험을 잘 못 봐서 이번 기말 시험을 잘 봐야 해요."),
    ("찬성", "(贊成) agreement; approval; to agree (~하다)", "올해 모임을 호텔에서 하려고 하는데 찬성하세요?"),
    ("합격", "(合格) passing (an examination, interview, screening, etc.); to pass (~하다)", "운전면허 시험에 합격했어요. 축하해 주세요."),
]
_CV_GR = [
    ("-느라(고)", "because of (doing something); due to", "어젯밤에 시험 공부하느라 잠을 잘 못 잤어요."),
    ("-도록", "so that; in order to; up to the point; until", "시험에 합격할 수 있도록 열심히 공부하세요. 밤새도록 노래를 부르면서 놀았어요."),
    ("-게 되다", "to get to; to come to; to turn out", "입대한 이후로 아침에 일찍 일어나게 됐어요."),
    ("누구 누구 / 뭐 뭐 / 어디 어디", "repeated question words", "어제 동창회에서 만난 사람이 누구 누구예요? 우리 음식은 뭐 뭐 시킬까요? 서울에 가서 어디 어디 구경했어요?"),
]
_CV_SINO = [("국립", "(國立) national (institution, etc.); “nationally established”", "국가, 국기, 국력, 국민, 공립, 주립, 시립, 도립"), ("점수", "(點數) grades; score; point", "중점, 만점, 영점, 수학, 수치, 평수")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_GR}
_EXTRA = {"~년제": "length of program for a school", "~학기": "a semester", "~학년": "school year; grade", "~교시": "a period (of a class)", "등 / 등수": "the ~th (in rank); ranking", "점 / 점수": "a point/score; grades", "-느라(고)": "because of (doing something)", "-도록": "so that; up to the point; until", "-게 되다": "to get to; to come to; to turn out", "누구 누구 / 뭐 뭐 / 어디 어디": "repeated question words", "각(각)": "respectively; each", "담임(선생)": "a homeroom teacher", "야단맞다 / 혼나다": "to be scolded; to be berated",
          "기쁘다": "to be glad; to be happy", "칭찬받다": "to be praised", "혼나다": "to be scolded", "야단맞다": "to be scolded", "혼내다": "to scold", "야단치다": "to scold", "중학교": "a middle school", "고등학교": "a high school", "대학교": "a university", "수업": "a class; a lesson",
          "국기": "a national flag", "국력": "national power", "출국": "leaving a country", "주립": "state-established", "시립": "city-established", "도립": "provincially established", "입석": "standing room", "만점": "a perfect score", "영점": "zero points", "학점": "a credit; school grades", "흑점": "a sunspot; “black spot”", "오점": "a blot; “dirty spot”", "다수": "many; a majority; “many numbers”", "소수": "a minority; a few; “few numbers”", "수치": "a numerical value",
          "예고": "an art specialty high school", "외고": "a foreign language high school", "여고": "a girls’ high school", "남고": "a boys’ high school", "입시": "an entrance examination", "국영수": "Korean, English and math", "자판기": "a vending machine", "월수금": "Monday, Wednesday and Friday", "한미": "Korea and America"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"


def _nr(v):
    st = stem(v)
    l, vv, t = _K.decompose(st[-1])
    return (st[:-1] + _K.compose(l, vv, "") if t == "ㄹ" else st) + "느라고"


_GUESS = [("국기", "a national flag"), ("국력", "national power"), ("출국", "leaving a country"), ("사립 중학교", "a private middle school"), ("공립 고등학교", "a public high school"), ("주립 대학교", "a state university")]
_KUK = [("국립 도서관", "a national library"), ("국립 대학교", "a national university"), ("국립 박물관", "a national museum"), ("도립 병원", "a provincial hospital; “province-established hospital”"), ("시립 도서관", "a municipal library; “city-established library”"), ("입석", "standing room; room for standing")]
_JEOM = [("학점", "G.P.A.; school grades; a credit"), ("흑점", "a sunspot; a spot on the sun; “black spot”"), ("만점", "a perfect score; full marks; “full mark”"), ("영점", "zero; zero point"), ("오점", "a blot; a blotch; “dirty spot”"), ("다수", "many; a large number; a majority; “many numbers”"), ("소수", "a small number; a minority; a few; “few numbers”"), ("수학", "mathematics; “study of numbers”"), ("수치", "a numerical value")]

# ================================================================== L1: objectives and Sino-Korean
L1 = lesson(
    "Ch 33 · What the chapter teaches, 국 (國) 립 (立) · 점 (點) 수 (數)",
    "한국의 교육 · 국립 · 공립 · 사립 · 점수 · 만점 · 영점",
    requires=[],
    cards=[
        card("What Chapter 33 teaches (한국의 교육)",
             "Chapter 33, “Education in Korea”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss the Korean school system, academic subjects, and a typical student’s daily routine; and talk about common concerns of students in Korea.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; –도록 (up to the point; until; in order to; so that); –느라(고) (because of; due to); repeated question words; –게 되다 (to become; to come to; to turn out); and the Sino-Korean syllables within 국립 (國立) and 점수 (點數)."),
        card("Sino-Korean in use: 국립 (國立)",
             "This Sino-Korean word means nationally run, nationally established, or simply national. So any institution or organization run by a nation can use this word, as in 국립 도서관 (a national library), 국립 대학교 (a national university), and 국립 박물관 (a national museum). As you have seen in words like 한국, 미국, 중국, and 영국, the first syllable 국 (國) means country, nation, or kingdom. The second syllable 립 (立) means establish(ed), erect(ed), or standing, as in 도립 병원 (a provincial hospital; “province-established hospital”) and 시립 도서관 (a municipal library; “city-established library”). When 립 (立) comes at the beginning of a word, the syllable changes to 입 (立), as in 입석 (standing room; room for standing). Thus the literal meaning of the word 국립 is “nationally established” or “nationally erected”. 력 (力) means power and 공 (公) means public or official.\n\n"
             "The book asks you to guess the meaning of 국기, 국력, 출국, 사립 중학교, 공립 고등학교 and 주립 대학교 (my answers are in the second table).",
             tables=[ktable(_KUK), ktable(_GUESS)]),
        card("Sino-Korean in use: 점수 (點數)",
             "This Sino-Korean word means a grade, point, mark, or score. The first syllable 점 (點) means point or spot, as in 학점 (G.P.A.; school grades; a credit), 흑점 (a sunspot; a spot on the sun; “black spot”), 만점 (perfect score; full marks; “full mark”), 영점 (zero; zero point), and 오점 (a blot; a blotch; “dirty spot”). The second syllable 수 (數) means number, as in 다수 (many; a large number; a majority; “many numbers”), 소수 (a small number; a minority; a few; “few numbers”), 수학 (mathematics; “study of numbers”), and 수치 (numerical value). Thus the literal meaning of the word 점수 is “number of points”.",
             tables=[ktable(_JEOM)]),
    ],
    exercises=uniq(
        _tr(_KUK + _GUESS + _JEOM, k=3)
        + [M("What does 국 (國) mean?", "country; nation; kingdom", ["power", "public", "number"], "한국, 미국."), M("What does 립/입 (立) mean?", "establish(ed); erect(ed); standing", ["country", "point", "power"], "국립, 입석."), M("What does 력 (力) mean?", "power", ["country", "public", "number"], "국력."), M("What does 공 (公) mean?", "public; official", ["private", "country", "power"], "공립."), M("What does 점 (點) mean?", "point; spot", ["number", "country", "stand"], "만점, 오점."), M("What does 수 (數) mean?", "number", ["point", "country", "power"], "다수, 수학."), M("What is the literal meaning of 국립?", "“nationally established”", ["“privately established”", "“number of points”", "“school chief”"], "국 + 립."), M("What is the literal meaning of 점수?", "“number of points”", ["“nationally established”", "“full mark”", "“study of numbers”"], "점 + 수."), M("Why does 립 become 입 in 입석?", "At the beginning of a word, 립 changes to 입", ["It is a different word", "It is a typo", "Because of 석"], "The book’s note."),
           F("요세미티 ___ 공원은 아주 아름답습니다. (national)", "국립", ["사립", "공립"], "국립."), F("저는 학교에 다닐 때 ___ 시간을 가장 좋아했어요. (physical education)", "체육", ["도덕", "사회"], "체육."), F("영어 시험에서 백 ___을 받았어요. (points)", "점", ["등", "과"], "점."), F("시험 ___가 올라서 기분이 좋아요. (score)", "점수", ["성적표", "입시"], "점수."),
           read_q("국립"), read_q("점수"), read_q("국립 도서관"), read_q("만점"), read_q("공립 고등학교")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_ANT = [("공립", "사립", "public", "private"), ("찬성", "반대", "agreement", "opposition"), ("속상하다", "기쁘다", "to be upset", "to be glad"), ("입학", "졸업", "entrance into school", "graduation"), ("칭찬받다", "혼나다", "to be praised", "to be scolded"), ("합격", "불합격", "passing", "failure")]
_ACR = [("예술 고등학교", "예고"), ("외국어 고등학교", "외고"), ("여자 고등학교", "여고"), ("남자 고등학교", "남고"), ("입학 시험", "입시"), ("국어, 영어, 수학", "국영수"), ("자동 판매기", "자판기"), ("월요일, 수요일, 금요일", "월수금"), ("한국, 미국", "한미"), ("초등학교, 중학교, 고등학교", "초중고")]
_ACR2 = [("남자, 여자", "남녀"), ("특별 활동", "특활"), ("과학 고등학교", "과고"), ("생활 필수 용품", "생필품")]
_CLUE = [("시험에 떨어지는 것", "불합격", "failing an exam"), ("학교를 마치는 것", "졸업", "finishing school"), ("중학교에 들어가기 전에 다니는 학교", "초등학교", "the school attended before middle school"), ("학교에 처음 들어가는 것", "입학", "entering a school for the first time"), ("찬성을 하지 않는 것", "반대", "not agreeing"), ("시험을 잘 봐서 통과하는 것", "합격", "passing by doing well on an exam"), ("좋지 않은 일 때문에 기분이 나쁨", "속상하다", "feeling bad because of something unpleasant")]
_SENT = [("제 아들은 공립 초등학교에 다닙니다. 사립 초등학교보다 돈이 많이 들지 않습니다.", "공립 / 사립", "public / private"), ("제 동생은 다음 주에 중학교를 졸업합니다. 그리고 다음 달에 외고에 입학합니다.", "졸업 / 입학", "graduation / entrance"), ("어제 운전시험을 봤는데 합격했습니다. 두 번이나 운전시험에 불합격해서 너무 걱정했었습니다.", "합격 / 불합격", "passing / failing"), ("지난번 시험을 잘 못 봐서 부모님께 혼났습니다. 그래서 이번에는 부모님이 칭찬하시도록 열심히 공부하고 있습니다.", "혼나다 / 칭찬하다", "to be scolded / to praise"), ("친구하고 이야기하다가 친구 의견에 반대를 했습니다. 그래서 친구가 화를 냈습니다. 저는 친구와 의견이 달라서 찬성할 수 없었습니다.", "반대 / 찬성", "opposition / agreement")]
L2 = lesson(
    "Ch 33 · Vocabulary Builder: antonyms, Korean acronyms and school words",
    "공립 · 사립 · 찬성 · 반대 · 입학 · 졸업 · 합격 · 불합격 · 속상하다 · 예고 · 외고 · 국영수 · 자판기",
    requires=[],
    cards=[
        card("New words and antonyms",
             "The book gives sixteen words in a box (합격, 사립, 찬성, 공립, 속상하다, 입학, 졸업, 합격, 반대, 칭찬받다, 혼나다, 불합격, 국어, 수학, 과학, 초등학교, ~학년) and asks you to circle the ones you don’t know, then match each word in Column A with its antonym in Column B. The matches (mine; the English is the book’s glosses):",
             tables=[table(["Column A", "Its antonym", "Column A English", "Antonym English"], [list(r) for r in _ANT], say=[0, 1])]),
        card("Vocabulary Learning Strategy: use new Korean acronyms",
             "An acronym is a word formed from the initial letters of a set of words, as in FAQ, NYPD, NATO and PIN. A typical Korean acronym consists of the first syllables of a set of words, as in 남고 (남자 고등학교) and 외고 (외국어 고등학교). Occasionally an acronym consists of a combination of the first syllables and the last syllable, as in 자판기 (자동 판매기). The book’s table (초•중•고 may also be written 초중고; 고등학교 1학년 is 고1, which has a digit and is not read out):",
             tables=[table(["Full wording", "Acronym"], [list(r) for r in _ACR], say=[0, 1]), table(["Full wording", "Acronym"], [["고등학교 1학년", "고1"]])]),
        card("Write the acronym (the book’s Column A; the answers are mine)",
             "The book gives seven phrases and asks you to write the acronym of each: 남자, 여자; 중학교 1학년; 고등학교 3학년; 특별 활동; 과학 고등학교; 생활 필수 용품; 입학 시험. My answers (中1 and 高3 are 중1 and 고3, with digits, and the last is already in the table above as 입시):",
             tables=[table(["Column A", "Acronym (mine)"], [list(r) for r in _ACR2], say=[0, 1]), table(["Column A", "Acronym (mine)"], [["중학교 1학년", "중1"], ["고등학교 3학년", "고3"]])]),
        card("Activity 1: word search (clues)", "The book gives seven clues and a grid of syllables to circle the words in. The grid is a picture and is left out; the clues and my answers:",
             tables=[table(["Clue", "Word (mine)", "English (mine)"], [list(r) for r in _CLUE], say=[0, 1])]),
        card("Activity 3: find the two antonyms in each text", "The book gives five short texts and asks you to underline the two antonyms in each and write their English meanings. My answers:",
             tables=[table(["Text", "The two antonyms (mine)", "English (mine)"], [list(r) for r in _SENT], say=[0])]),
        card("Activities left out", "Activities 2 and 4 (SMART Board), the PowerPoint presentation on Sino-Korean words and Activity 5 (a related-words game in two teams, with a three-second limit per word and a model of 학교: 교실, 선생님) are computer and game activities."),
    ],
    exercises=uniq(
        [M("What is the antonym of " + a + "?", b, [x[1] for x in _ANT if x[1] != b][:3], a + " ↔ " + b) for a, b, c, d in _ANT]
        + [M("What is the antonym of " + b + "?", a, [x[0] for x in _ANT if x[0] != a][:3], b + " ↔ " + a) for a, b, c, d in _ANT]
        + [M("What is the acronym of " + a + "?", b, [x[1] for x in _ACR + _ACR2 if x[1] != b][:3], a + " → " + b) for a, b in _ACR[:9] + _ACR2]
        + [M("Which word matches the clue “" + a + "”?", b, [x[1] for x in _CLUE if x[1] != b][:3], "My answer.") for a, b, c in _CLUE]
        + vocab_exercises(_pairs(["공립", "사립", "찬성", "반대", "입학", "졸업", "합격", "불합격", "속상하다", "혼나다", "국어", "과학", "수학", "초등학교"]))
        + [F("제 아들은 ___ 초등학교에 다닙니다. 사립보다 돈이 많이 들지 않습니다. (public)", "공립", ["사립", "국립"], "공립."), F("제 동생은 다음 주에 중학교를 ___합니다. (graduate)", "졸업", ["입학", "합격"], "졸업."), F("어제 운전시험을 봤는데 ___했습니다. (passed)", "합격", ["불합격", "반대"], "합격."), F("지난번 시험을 잘 못 봐서 부모님께 ___. (was scolded)", "혼났습니다", ["칭찬받았습니다", "찬성했습니다"], "혼나다."), F("저는 친구와 의견이 달라서 ___할 수 없었습니다. (agree)", "찬성", ["반대", "입학"], "찬성."),
           read_q("공립"), read_q("사립"), read_q("입학과 졸업"), read_q("합격과 불합격"), read_q("자판기")]
    ),
)

# ================================================================== L3: Topic A
_A_TXT = [
    ("한국의 학교 제도", "The Korean school system"),
    ("한국에는 유치원, 초등학교, 중학교, 고등학교, 대학교, 대학원이 있다.", "Korea has kindergartens, elementary schools, middle schools, high schools, universities and graduate schools."),
    ("초등학교는 일 학년부터 육 학년까지, 중학교와 고등학교는 각각 일 학년부터 삼 학년까지 있다.", "Elementary school runs from the first grade to the sixth grade, and middle school and high school each run from the first grade to the third grade."),
    ("그리고 대학교는 이 년제 대학과 사 년제 대학교가 있다.", "And as for colleges, there are two-year colleges and four-year universities."),
    ("초등학교와 중학교의 교육은 의무교육이다.", "Education in elementary and middle school is compulsory education."),
    ("그리고 한국의 학교는 삼월 초에 일 학기가 시작되고 팔월 말에 이 학기가 시작된다.", "And Korean schools start the first semester at the beginning of March and the second semester at the end of August."),
    ("그리고 여름 방학과 겨울 방학은 각각 한 달이 넘는다.", "And the summer vacation and the winter vacation each last more than a month."),
    ("따라서 학생들은 보통 삼월에 입학하고 이월에 졸업한다.", "Therefore students usually enter school in March and graduate in February."),
]
_A_WORDS = ["각(각)", "공립", "교장", "국립", "~년제", "대학원", "따라서", "사립", "실업계", "유치원", "의무", "인문계", "입학", "제도", "졸업", "초등학교", "총장", "~학기", "~학년"]
_KA = "The Korean academic school year begins with the spring semester (1학기) in March. The second semester (2학기) starts in late August and ends in mid-February. Korean schools have a summer break (여름방학) from mid-July to late August, and a longer winter break (겨울방학) from late December to early February. A brief spring break (봄방학) falls between mid-February and the beginning of March. The academic calendar is generally standardized nationwide, but it may vary slightly from region to region.\n\nKorea has three different types of high schools. 인문계 고등학교 (일반 고등학교 or 일반고) does not specialize in a field, and is more focused on students headed for college. 실업계 고등학교 (실업고) is vocational high school, where students specialize in fields such as technology, agriculture, or finance. 실업고 students usually look for jobs directly after graduation. The third type of school, 특수 목적 고등학교 (특목고), can be divided into specialty tracks that align with a student’s interests and career path. Science high schools (과학 고등학교 or 과고), foreign language high schools (외국어 고등학교 or 외고), and art specialty high schools (예술 고등학교 or 예고) belong to 특목고 and are known for their highly competitive entrance exams."
_NK = "Education in North Korea is strictly controlled by the government. Mandatory education (의무교육) lasts 12 years, and encompasses one year of upper kindergarten, five years of primary education, and six years of secondary education (equivalent to middle and high school in the US). Higher education is not mandatory in North Korea, and it includes three types of institutions: universities (대학교), vocational schools (전문학교), and technical schools (기술학교). Two notable universities in North Korea are the Kim Il-Sung University and Pyongyang University of Science and Technology, both located in Pyongyang."
_TYPE = [("교수들이 가르칩니다. 사 년제 대학을 졸업하고 더 공부하기 위해서 들어갑니다.", "h", "대학원"), ("의무교육이기 때문에 모든 학생들이 다녀야 합니다. 육 년 동안 다니고 졸업 후에는 중학교에 들어갑니다.", "b", "초등학교"), ("고등학교를 졸업하고 이 년 동안 공부를 하기 위해 입학합니다. 졸업 후에 공부를 계속 공부하고 싶으면 사 년제 대학으로 갈 수 있습니다.", "f", "이 년제 대학"), ("중학교를 졸업하고 입학해서 삼 년 동안 공부합니다. 보통 대학에 들어갈 공부를 합니다.", "d", "인문계 고등학교"), ("초등학교에 들어가기 전에 다닙니다. 일 년에서 삼 년 정도 다닙니다.", "a", "유치원"), ("고등학교를 졸업한 후에 들어가서 사 년 동안 공부합니다. 총장이 학교에서 가장 높은 분입니다.", "g", "사 년제 대학교")]
L3 = lesson(
    "Ch 33 · Topic A: The Korean school system (한국의 학교 제도)",
    "한국의 학교 제도 · 유치원 · 초등학교 · 중학교 · 고등학교 · 대학교 · 대학원 · 의무교육 · 인문계 · 실업계",
    requires=[],
    cards=[
        card("Topic A: The Korean school system (한국의 학교 제도)",
             "This article gives a summary of the Korean school system. (The English is mine; the book gives none; the numbers are spelled out in Hangul.)",
             examples=passage(_A_TXT)),
        card("The book’s diagram of the system", "The book adds a diagram, in this order from the bottom: 유치원 → 초등학교 → 중학교 → 고등학교 (인문계, 실업계) → 2년제 대학 or 4년제 대학교 → 대학원. (The picture itself is left out.)"),
        card("한국에서는: the school year and the high schools", _KA),
        card("북한에서는: education in North Korea", _NK),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 입학(하다) and 졸업(하다) take the form in parentheses.",
             tables=[ktable(_rows([w for w in _A_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["~년제", "length of program for a school; “year system”"], ["~학기", "a semester; “school period”"], ["~학년", "school year; grade"]])]),
        card("Activity 3 (Reading): which type of school is it?",
             "The book gives six statements and a list of eight schools (a. 유치원; b. 초등학교; c. 중학교; d. 인문계 고등학교; e. 실업계 고등학교; f. 2년제 대학; g. 4년제 대학교; h. 대학원) and asks you to write the letter of the school each statement describes. The statements are the book’s with the numbers spelled out; the answers are mine.",
             tables=[table(["Statement", "Letter", "School (mine)"], [[a, b, c] for a, b, c in _TYPE], say=[0])]),
        card("Activities left out", "The SMART Board activities, Follow-up 1 (listening to three short conversations about the Korean school system), Follow-up 2 (reading a list of useful websites, the Ministry of Education and the Seoul Metropolitan Office of Education, and ticking the sentences about the Korean education system), Activity 2 (listening to two people visiting a school) and Activity 4 (listening to a presentation, filling in comparison tables and presenting) need audio, web pages and classmates."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT[1:], k=3)
        + [M("Which school is described: “" + a[:30] + "…”?", c, [x[2] for x in _TYPE if x[2] != c][:3], "My answer.") for a, b, c in _TYPE]
        + [M("Which years do elementary schools have?", "The first to the sixth grade", ["The first to the third grade", "The first to the fourth grade", "The first to the ninth grade"], "일 학년부터 육 학년까지."), M("Which years do middle and high schools have?", "The first to the third grade, each", ["The first to the sixth grade", "The first to the fourth grade", "One year only"], "각각 일 학년부터 삼 학년까지."), M("Which education is compulsory?", "Elementary and middle school", ["High school", "University", "Graduate school"], "초등학교와 중학교의 교육은 의무교육."), M("When does the first semester start?", "At the beginning of March", ["At the end of August", "In January", "In June"], "삼월 초."), M("When does the second semester start?", "At the end of August", ["At the beginning of March", "In January", "In October"], "팔월 말."), M("How long are the summer and winter vacations?", "Each more than a month", ["A week", "Three days", "A year"], "한 달이 넘는다."), M("When do students usually enter and graduate?", "Enter in March and graduate in February", ["Enter in September", "Graduate in June", "Enter in January"], "삼월에 입학하고 이월에 졸업."),
           F("한국에는 유치원, 초등학교, 중학교, 고등학교, 대학교, ___이 있다. (graduate school)", "대학원", ["대학교", "유치원"], "대학원."), F("초등학교와 중학교의 교육은 ___교육이다. (compulsory)", "의무", ["공립", "사립"], "의무교육."), F("___ 학생들은 보통 삼월에 입학하고 이월에 졸업한다. (therefore)", "따라서", ["그리고", "그런데"], "따라서."), F("저는 ___ 고등학교를 졸업하고 대학에 입학했습니다. (vocational track)", "실업계", ["인문계", "공립"], "실업계."), F("고등학교를 졸업한 후에 사 년 동안 공부합니다. ___이 학교에서 가장 높은 분입니다. (president)", "총장", ["교장", "담임"], "총장."),
           read_q("한국의 학교 제도"), read_q("초등학교와 중학교의 교육은 의무교육이다"), read_q("학생들은 보통 삼월에 입학하고 이월에 졸업한다"), read_q("대학교는 이 년제 대학과 사 년제 대학교가 있다"), read_q("의무교육")]
    ),
)

# ================================================================== L4: Topic B
_B_TXT = [
    ("정현이의 학교는 여덟 시 반에 시작합니다.", "Jeonghyeon’s school starts at half past eight."),
    ("정현이는 보통 아침 일곱 시쯤에 일어나 아침을 먹고 여덟 시쯤 학교에 갑니다.", "Jeonghyeon usually gets up at around seven in the morning, eats breakfast and goes to school at around eight."),
    ("수업은 오전에 네 시간, 오후에 두 시간 있습니다.", "There are four hours of classes in the morning and two hours in the afternoon."),
    ("점심 시간은 사 교시 수업 후에 있습니다.", "Lunch time is after the fourth-period class."),
    ("정현이 학교는 급식을 하지 않기 때문에 정현이는 도시락을 먹습니다.", "Jeonghyeon’s school does not provide school meals, so Jeonghyeon eats a lunch box."),
    ("정현이는 여러 가지 과목 중 영어를 제일 좋아합니다.", "Among the various subjects, Jeonghyeon likes English best."),
    ("그래서 매주 금요일 육 교시 특별활동 시간에는 영어웅변반에서 활동을 합니다.", "So during the sixth-period special activity time every Friday, he does activities in the English speech club."),
    ("방과 후에는 곧장 학원에 가서 수학과 한문을 더 배웁니다.", "After class he goes straight to a private academy and learns more math and Chinese characters."),
    ("그리고 저녁 여섯 시쯤 집에 돌아와 저녁을 먹습니다.", "And at around six in the evening he returns home and eats dinner."),
    ("저녁 식사를 한 후에는 보통 두 시간 동안 숙제를 하고 컴퓨터를 하거나 가족과 함께 텔레비전을 봅니다.", "After dinner he usually does homework for two hours and uses the computer or watches television with his family."),
    ("그러나 다음 주에 교내 영어 웅변 대회가 있기 때문에 요즘에는 매일 저녁 웅변 대회 연습을 합니다.", "But because there is an English speech contest at school next week, these days he practices for the speech contest every evening."),
    ("어제는 밤새도록 연습하느라 늦잠을 잤습니다.", "Yesterday he overslept because he practiced all night long."),
    ("그래서 오늘 아침에는 지각을 해서 담임선생님에게 야단을 맞았습니다.", "So this morning he was late and was scolded by his homeroom teacher."),
    ("그렇지만 영어 선생님께서 실력이 많이 늘었다고 칭찬해 주셨습니다.", "But the English teacher praised him, saying that his skills had improved a lot."),
]
_B_WORDS = ["결석", "과목", "과학", "교내", "~교시", "국어", "급식", "-느라(고)", "늦잠", "담임(선생)", "도덕", "-도록", "도시락", "방과 후", "사회", "수학", "시간표", "실력", "야단맞다 / 혼나다", "웅변", "자율학습", "지각", "체육", "칭찬", "한문"]
_KB = "In the U.S., middle school and high school students usually move to different classrooms for each subject. In Korea, students move to different classrooms only for classes like music, art, science, and physical education. Otherwise, students stay in their homeroom and the teachers move. Teachers share a big office called a 교무실. Each section (of a class) has 20 to 30 students, and the sections are usually identified by numbers. For example, if a new class has 120 students and four sections, the sections are called 1–1반 (1학년 1반), 1–2반 (1학년 2반), 1–3반 (1학년 3반), and 1–4반 (1학년 4반). Each section has a student representative called 반장, who is generally elected by fellow classmates and has high grades. Each section also has a teacher called 담임 선생님 who is assigned to the section for the entire academic year."
_TT = [["1교시", "자율학습", "자율학습", "자율학습", "자율학습", "자율학습", "자율학습"], ["2교시", "국어", "한문", "수학", "과학", "도덕", "국어"], ["3교시", "과학", "도덕", "국어", "한문", "음악", "영어"], ["4교시", "영어", "수학", "체육", "미술", "국어", "대청소"], ["5교시", "체육", "국어", "영어", "수학", "특별활동", "-"], ["6교시", "미술", "과학", "음악", "영어", "특별활동", "-"]]
_ART = [("한국 케이블방송은 전국 중학생 천 명을 대상으로 방과 후 활동을 조사하여 결과를 발표했다.", "A Korean cable broadcaster surveyed one thousand middle school students nationwide on after-school activities and announced the results."), ("조사 결과를 보면, 중학생들이 방과 후에 하는 일은 고등학교 입학시험 준비를 위한 학원수업이 팔십오 퍼센트, 운동이나 악기 등 특기활동이 오십오 퍼센트, 교회 등 종교활동이 십삼 퍼센트인 것으로 나타났다.", "According to the results, what middle school students do after school is: private academy classes for preparing for high school entrance exams, 85%; talent activities such as sports or musical instruments, 55%; and religious activities such as church, 13%."), ("방과 후 학원수업을 받는다고 대답한 학생들의 하루 평균 학원수업 시간은 두 시간 오십오 분으로 나타났다.", "For the students who answered that they take academy classes after school, the average daily academy class time was two hours and fifty-five minutes."), ("학원수업 과목은 영어 구십 퍼센트, 수학 칠십오 퍼센트, 과학 육십오 퍼센트, 국어 오십 퍼센트, 사회 사십 퍼센트였고, 학생 일 인당 평균 삼 점 육 과목의 수업을 듣는 것으로 조사됐다.", "The academy class subjects were English 90%, math 75%, science 65%, Korean 50% and social studies 40%, and it was found that each student takes an average of 3.6 subjects.")]
L4 = lesson(
    "Ch 33 · Topic B: Jeonghyeon became a middle schooler this March (정현이는 올 3월에 중학생이 되었습니다)",
    "정현이의 하루 · 급식 · 도시락 · 특별활동 · 학원 · 늦잠 · 지각 · 야단맞다 · 시간표 · 방과 후 활동",
    requires=[],
    cards=[
        card("Topic B: Jeonghyeon became a middle schooler this March (정현이는 올 3월에 중학생이 되었습니다)",
             "The following text is about the weekday routine of a freshman in middle school. (The English is mine; the book gives none; the times and numbers are spelled out in Hangul.)",
             examples=passage(_B_TXT)),
        card("정현이의 1학년 3반 시간표 (Jeonghyeon’s timetable)", "The book gives Jeonghyeon’s weekly timetable (the periods, 월 to 토); the “-” marks the two Saturday periods that are blank in the book.",
             tables=[table(["", "월", "화", "수", "목", "금", "토"], _TT)]),
        card("한국에서는: classes and homerooms", _KB),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); 결석(하다), 급식(하다), 늦잠(을 자다), 지각(하다) and 칭찬(하다) take the forms in parentheses; –도록 and –느라(고) are explained in the grammar.",
             tables=[ktable(_rows([w for w in _B_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["~교시", "a period (of a class); an hour (of a class)"], ["-느라(고)", "because of (doing something); due to"], ["-도록", "so that; in order to; up to the point; until"]])]),
        card("Follow-up 2 (Reading): a newspaper article on after-school activities",
             "The book gives two bar graphs (A: what middle school students do after school; B: academy class subjects), asks you to write a title for each graph and label each bar in English. The graphs are pictures and are left out; the article is below, with the percentages and numbers spelled out in Hangul. The English is mine.",
             examples=passage(_ART)),
        card("The graphs’ titles and bars (mine)", "These are my answers from the article.",
             tables=[table(["Graph", "Title and bars (mine)"], [["A", "What middle school students do after school: academy classes for high school entrance exams (85%), talent activities such as sports or instruments (55%), religious activities (13%)"], ["B", "Subjects taken at academy classes: English (90%), math (75%), science (65%), Korean (50%), social studies (40%)"]])]),
        card("Activities left out", "The SMART Board activities, the partner reading of Text A and Text B and Follow-up 1 (listening to three short conversations about being tardy or absent) are computer, audio and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT + _ART, k=3)
        + [M("What time does 정현’s school start?", "Half past eight", ["Seven", "Nine", "Ten"], "여덟 시 반."), M("What time does 정현 usually get up?", "Around seven", ["Around six", "Around eight", "Around five"], "일곱 시쯤."), M("How many hours of class are there in the morning?", "Four", ["Two", "Six", "Three"], "오전에 네 시간."), M("Why does 정현 eat a lunch box?", "His school does not provide school meals", ["He likes it", "He is on a diet", "It is cheaper"], "급식을 하지 않기 때문에."), M("Which subject does 정현 like best?", "English", ["Math", "Science", "Korean"], "영어를 제일 좋아합니다."), M("Where does 정현 go right after class?", "A private academy", ["Home", "A park", "The library"], "곧장 학원에."), M("Why did 정현 oversleep yesterday?", "He practiced all night long", ["He was sick", "He watched TV", "He played games"], "밤새도록 연습하느라."), M("What did the English teacher do?", "Praised his improved skills", ["Scolded him", "Gave homework", "Ignored him"], "칭찬해 주셨습니다."),
           F("정현이는 여러 가지 ___ 중 영어를 제일 좋아합니다. (subjects)", "과목", ["학기", "학년"], "과목."), F("방과 후에는 곧장 ___에 가서 수학과 한문을 더 배웁니다. (academy)", "학원", ["도서관", "교실"], "학원."), F("어제는 밤새도록 연습하느라 ___을 잤습니다. (overslept)", "늦잠", ["낮잠", "잠"], "늦잠."), F("아침에는 지각을 해서 담임선생님에게 ___을 맞았습니다. (a scolding)", "야단", ["칭찬", "점수"], "야단을 맞다."), F("학교는 급식을 하지 않기 때문에 ___을 먹습니다. (a lunch box)", "도시락", ["간식", "과자"], "도시락."),
           read_q("정현이의 학교는 여덟 시 반에 시작합니다"), read_q("정현이는 여러 가지 과목 중 영어를 제일 좋아합니다"), read_q("방과 후에는 곧장 학원에 가서 수학과 한문을 더 배웁니다"), read_q("어제는 밤새도록 연습하느라 늦잠을 잤습니다"), read_q("영어 선생님께서 실력이 많이 늘었다고 칭찬해 주셨습니다")]
    ),
)

# ================================================================== L5: Grammar A: -도록
_DO1 = [("우리는 배가 터지도록 먹었어요.", "We ate “to the point that our stomachs exploded.” / We ate a lot. (intended meaning)"), ("밤새도록 친구와 이야기했어요.", "I talked with my friend “up to the point that the night broke.” / I talked with my friend all night long. (intended meaning)")]
_DO2 = [("대학에 갈 수 있도록 열심히 공부하겠습니다.", "I will study hard “up to the point that I can go to college” or so that I can go to college."), ("회의에 늦지 않도록 일찍 오세요.", "Come early “up to the point that you won’t be late for the meeting” or so as to not be late for the meeting.")]
_DO3 = [("교실에서는 한국말만 하도록 하세요.", "Make sure to speak Korean only in the classroom."), ("집에 가기 전에 전화하도록 할게요.", "I’ll make sure to call you before going home.")]
_DOV = [("터지다", "to burst", "터지도록"), ("아프다", "to hurt", "아프도록"), ("밤새다", "to stay up all night", "밤새도록"), ("합격하다", "to pass", "합격하도록"), ("늦다", "to be late", "늦지 않도록"), ("가다", "to go", "갈 수 있도록"), ("먹다", "to eat", "먹도록"), ("전화하다", "to call", "전화하도록")]
L5 = lesson(
    "Ch 33 · Grammar A: the conjunctive ending –도록, up to the point; until; so that",
    "-도록 · 배가 터지도록 · 밤새도록 · 늦지 않도록 · 갈 수 있도록 · -도록 하다",
    requires=[],
    cards=[
        card("–도록: “(up) to the point” or “until”",
             "The conjunctive ending –도록 literally means “(up) to the point” or “until”, as in 배가 터지도록 (to the point that the stomach explodes) and 손이 아프도록 (to the point that the hands hurt). Thus, the conjunctive ending is similar to –(으)ㄹ 때까지 (until), as in 배가 터질 때까지 (until the stomach explodes) and 손이 아플 때까지 (until the hands hurt). However, –도록 is often used to exaggerate a situation or to say something figuratively. For example (the English is the book’s):",
             examples=passage(_DO1)),
        card("–도록: “in order to”, “so as to”, “so that”", "The conjunctive ending –도록 can also be used to mean in order to, so as to, or so that. (The English is the book’s.)", examples=passage(_DO2)),
        card("–도록 하다: “make sure”", "–도록 하다, in which –도록 is immediately followed by 하다, is used to mean make sure or ensure. For example (the English is the book’s):", examples=passage(_DO3)),
        card("Forms (mine)", "Verb or adjective stem + 도록 (negative: –지 않도록).",
             tables=[table(["Verb", "Meaning", "-도록"], [list(r) for r in _DOV], say=[0, 2])]),
        card("Follow-up 1 (Reading, speaking and listening): the model", "In pairs, Partner A takes a card from Set A and conjugates the verb with –도록, and Partner B reads a text from Set B that logically connects. The book’s model (the English is mine):", examples=dlg([("A", "밤이 늦도록", "Until late at night,"), ("B", "파티하고 놀았어요.", "I partied and played.")])),
        card("Activities left out", "The word cards (Sets A and B) and Follow-up 2 (listening to four dialogs and marking the meaning of –도록) need cards, audio and classmates."),
    ],
    exercises=uniq(
        _tr(_DO1 + _DO2 + _DO3, k=3)
        + [M("What does –도록 literally mean?", "“(up) to the point” or “until”", ["“because of”", "“if”", "“although”"], "The book’s note."), M("What is –도록 similar to?", "–(으)ㄹ 때까지", ["–(으)면", "–지만", "–아/어서"], "The book’s note."), M("What does –도록 often do?", "Exaggerates a situation or says something figuratively", ["Gives a command", "Asks a question", "Marks a past event"], "The book’s note."), M("What does 밤새도록 친구와 이야기했어요 mean?", "I talked with my friend all night long", ["I talked until noon", "I will talk tonight", "I did not talk"], "Intended meaning."), M("What does –도록 하다 mean?", "Make sure; ensure", ["Try to", "Want to", "Be able to"], "The book’s note."), M("What does 회의에 늦지 않도록 일찍 오세요 mean?", "Come early so as not to be late for the meeting", ["Come late", "Do not come", "Come at noon"], "In order to."),
           F("우리는 배가 터지___ 먹었어요. (-도록)", "도록", ["느라", "게"], "-도록."), F("밤새___ 친구와 이야기했어요. (all night long)", "도록", ["느라", "에서"], "밤새도록."), F("회의에 늦지 않___ 일찍 오세요. (-도록)", "도록", ["느라", "아서"], "-지 않도록."), F("교실에서는 한국말만 하도록 ___. (make sure; polite request)", "하세요", ["가세요", "보세요"], "-도록 하세요."), F("집에 가기 전에 전화하도록 ___. (I’ll make sure)", "할게요", ["갈게요", "볼게요"], "-도록 할게요."),
           read_q("우리는 배가 터지도록 먹었어요"), read_q("밤새도록 친구와 이야기했어요"), read_q("대학에 갈 수 있도록 열심히 공부하겠습니다"), read_q("회의에 늦지 않도록 일찍 오세요"), read_q("교실에서는 한국말만 하도록 하세요")]
    ),
)

# ================================================================== L6: Grammar B: -느라(고)
_NR1 = [("어제 저녁에 어머니를 도와드리느라 숙제를 못 했어요.", "I couldn’t do my homework because I was helping my mother last night."), ("친구랑 전화로 이야기하느라 집합에 늦었어요.", "I was late for the formation because I was talking with my friend on the phone.")]
_NR2 = [("밤늦게까지 공부하느라고 수고했다.", "You took the trouble to study until late night. (I praise you!)"), ("아버지, 그 동안 저희들을 위해 일하시느라고 고생 많이 하셨어요.", "Father, you have taken pains working for us so far. (We appreciate you a lot!)")]
_NRV = [("놀다", "to play", "노느라고"), ("보다", "to watch", "보느라고"), ("하다", "to do", "하느라고"), ("만들다", "to make", "만드느라고"), ("공부하다", "to study", "공부하느라고"), ("일하다", "to work", "일하느라고"), ("돕다", "to help", "돕느라고"), ("이야기하다", "to talk", "이야기하느라고")]
_NRM = [("친구하고 놉니다", "점심을 못 먹었어요", "친구하고 노느라 점심을 못 먹었어요."), ("텔레비전을 봅니다", "다른 취미활동을 못 해요", "텔레비전을 보느라 다른 취미활동을 못 해요."), ("샤워를 합니다", "전화를 못 받았어요", "샤워를 하느라 전화를 못 받았어요."), ("비디오 게임을 합니다", "숙제를 못 했어요", "비디오 게임을 하느라 숙제를 못 했어요."), ("숙제를 합니다", "늦게 잤어요", "숙제를 하느라 늦게 잤어요."), ("한국어 공부를 합니다", "체육관에 못 가요", "한국어 공부를 하느라 체육관에 못 가요.")]
L6 = lesson(
    "Ch 33 · Grammar B: expressing a reason, –느라(고)",
    "-느라(고) · 도와드리느라 · 이야기하느라 · 공부하느라 · 수고하다 · 고생하다",
    requires=[],
    cards=[
        card("–느라(고): because (of)",
             "The conjunctive ending –느라(고), which translates as “because (of)”, is used to justify or explain away a negative or unpleasant consequence caused by the speaker’s own action. For example (the English is the book’s):",
             examples=passage(_NR1)),
        card("Three grammatical restrictions",
             "However, when using –느라(고) several grammatical restrictions apply:\n\n"
             "1. Only action verbs can be attached to –느라(고).\n2. The subject of the –느라(고) clause and the main clause that follows it must be the same.\n3. The verb in the main clause cannot be a command or suggestion.\n\n"
             "For example, the following sentences are grammatically incorrect (the book marks them with *): *배가 고프느라고 밥을 먹었어요. (a stative verb); *차 일병이 샤워하느라고 신 이병이 전화 소리를 못 들었어요. (different subjects); *기침을 많이 하느라고 병원에 가 보세요. (a command; an imperative)."),
        card("Appreciation or praise",
             "–느라(고) expresses the speaker’s appreciation or praise when it is used with the verbs in the main clause 수고하다 (to give oneself trouble; to take the trouble), 고생하다 (to have difficulty), and 애쓰다 (to endeavor; to strive; to take pains). (The English is the book’s.)",
             examples=passage(_NR2)),
        card("Forms (mine)", "Action verb stem + 느라(고) (an ㄹ-final stem drops the ㄹ: 놀다 → 노느라고; ㅂ-irregular 돕다 keeps the ㅂ: 돕느라고).",
             tables=[table(["Verb", "Meaning", "-느라고"], [list(r) for r in _NRV], say=[0, 2])]),
        card("Follow-up 3 (Reading, speaking and listening): reason and consequence",
             "The book gives six reason clauses (친구하고 놉니다; 텔레비전을 봅니다; 샤워를 합니다; 비디오 게임을 합니다; 숙제를 합니다; 한국어 공부를 합니다) to be matched with six consequences (점심을 못 먹었어요; 다른 취미활동을 못 해요; 숙제를 못 했어요; 전화를 못 받았어요; 늦게 잤어요; 체육관에 못 가요); the first match is given in the book and the answers may vary. One set of matches (mine):",
             tables=[table(["Reason", "Consequence", "Full sentence (mine)"], [list(r) for r in _NRM], say=[2])]),
        card("The model (Follow-up 3b and 5)", "The book’s models (the English is mine):", examples=dlg([("A", "친구하고 노느라고", "Because I was playing with a friend,"), ("B", "숙제를 못 했어요.", "I couldn’t do my homework.")]) + dlg([("A", "부대에서 근무하느라고 체육관에서 운동을 못 했어요.", "Because I was working at the unit, I couldn’t exercise at the gym.")])),
        card("Activities left out", "Follow-up 4 (listening to three short conversations and writing the reason and consequence) is an audio activity; Follow-up 5 (Table A and Table B for yesterday afternoon, filled in in pairs) needs the tables and a partner."),
    ],
    exercises=uniq(
        _tr(_NR1 + _NR2, k=3)
        + [M("What does –느라(고) explain?", "A negative consequence caused by the speaker’s own action", ["A wish", "A command", "A future plan"], "The book’s note."), M("Which verbs can take –느라(고)?", "Only action verbs", ["Only stative verbs", "Only nouns", "All verbs"], "Restriction 1."), M("What must be true of the subjects of the two clauses?", "They must be the same", ["They must differ", "No subject", "Both are I"], "Restriction 2."), M("What can the main clause not be?", "A command or suggestion", ["A statement", "Past tense", "Negative"], "Restriction 3."), M("What does –느라(고) express with 수고하다, 고생하다 or 애쓰다?", "The speaker’s appreciation or praise", ["Anger", "Surprise", "A request"], "The book’s note."),
           M("Why is *배가 고프느라고 밥을 먹었어요 incorrect?", "고프다 is a stative verb", ["It is past tense", "It has no subject", "It is a command"], "Restriction 1."), M("Why is *기침을 많이 하느라고 병원에 가 보세요 incorrect?", "The main clause is a command", ["The verb is stative", "The subjects differ", "It is past tense"], "Restriction 3."),
           F("어제 저녁에 어머니를 도와드리___ 숙제를 못 했어요. (-느라)", "느라", ["도록", "게"], "-느라."), F("친구랑 전화로 이야기하___ 집합에 늦었어요. (-느라)", "느라", ["도록", "게"], "-느라."), F("밤늦게까지 공부하느라고 ___. (you took the trouble; praise)", "수고했다", ["지각했다", "결석했다"], "수고하다."), F("친구하고 ___ 점심을 못 먹었어요. (-느라, playing)", "노느라", ["놀느라", "놀도록"], "ㄹ drops."), F("부대에서 근무하___ 체육관에서 운동을 못 했어요. (-느라)", "느라고", ["도록", "게"], "-느라고."),
           read_q("어제 저녁에 어머니를 도와드리느라 숙제를 못 했어요"), read_q("친구랑 전화로 이야기하느라 집합에 늦었어요"), read_q("밤늦게까지 공부하느라고 수고했다"), read_q("친구하고 노느라 점심을 못 먹었어요"), read_q("부대에서 근무하느라고 체육관에서 운동을 못 했어요")]
    ),
)

# ================================================================== L7: Topic C
_C_DLG = [
    ("지훈", "연아야, 나 외고 입시 보기로 했어.", "Yeona, I decided to take the foreign-language high school entrance exam."),
    ("연아", "그래? 부모님은 어떻게 생각하셔?", "Really? What do your parents think?"),
    ("지훈", "내 의견에 찬성하셔. 그래서 다음 주부터 과외받게 될 거야.", "They agree with my opinion. So from next week I’ll end up getting private lessons."),
    ("연아", "그럼 이제 바빠지겠구나. 넌 성적이 좋아서 시험만 잘 보면 합격할 거야.", "Then you’ll get busy now. Your grades are good, so if you just do well on the exam you’ll pass."),
    ("지훈", "넌 어때?", "How about you?"),
    ("연아", "네가 부럽다. 난 기말 시험 성적 때문에 속상해.", "I envy you. I’m upset because of my final exam grades."),
    ("지훈", "왜? 등수가 떨어졌어?", "Why? Did your rank drop?"),
    ("연아", "응, 중간 시험 때보다 팔 등이나 떨어졌어. 그리고 수학 점수는 정말 나빠.", "Yes, it dropped by as many as eight places from the midterm. And my math score is really bad."),
    ("지훈", "그럼, 학원에 다녀 봐. 학원에 다니면 성적이 좀 오를 거야.", "Then try going to an academy. If you go to an academy, your grades will go up a bit."),
    ("연아", "그래서 학원을 알아보는 중이야. 너는 학원 어디 어디를 다녔니?", "That’s why I’m looking into academies. Which academies did you go to?"),
    ("지훈", "나는 우리 동네에 있는 대성학원하고 고려학원을 다녔어.", "I went to Daesung Academy and Goryeo Academy in our neighborhood."),
]
_C_WORDS = ["-게 되다", "결심", "과외", "교제", "기말", "동네", "등 / 등수", "반대", "부럽다", "불합격", "성적", "성적표", "속상하다", "시키다", "누구 누구 / 뭐 뭐 / 어디 어디", "입시", "이성", "점 / 점수", "중간", "찬성", "합격"]
_KC = "학군 (school district) is very important in Korea. In most cities, students are assigned by lottery to a high school in their school district. Some school districts are ranked higher than others in student success on college entrance exams. Many parents seek out these better school districts for their children."
_TOPIC = [("살이 많이 쪄서 고민하는 고등학생이 많습니다. 그리고 다이어트를 하는 학생도 많습니다.", "e", "appearance"), ("부모님께 용돈을 받아서 쓰는 학생이 많았습니다. 하지만 대부분의 학생들이 용돈이 더 필요하다고 생각합니다.", "b", "allowance"), ("학생들의 가장 큰 걱정은 학교 성적입니다. 많은 학생들이 수학과 영어 점수를 가장 중요하게 생각합니다.", "c", "grades and GPA"), ("많은 학생들이 이성 친구를 사귀고 있다고 합니다. 그리고 이성 친구가 없는 학생들은 대학에 가서 이성 교제를 하길 원합니다.", "a", "interacting with the opposite gender")]
L7 = lesson(
    "Ch 33 · Topic C: I decided to take the foreign-language high school entrance exam (외고 입시 보기로 했어)",
    "외고 입시 보기로 했어 · 과외받게 될 거야 · 성적 때문에 속상해 · 등수가 떨어졌어 · 학원을 알아보는 중이야 · 학군",
    requires=[],
    cards=[
        card("Topic C: I decided to take the foreign-language high school entrance exam (외고 입시 보기로 했어)",
             "Two middle school students are talking on the phone about their concerns. (The English is mine; the book gives none; 8등 is spelled out.)",
             examples=dlg(_C_DLG)),
        card("The book’s footnote", "외고 입시 is an example of a Korean acronym. It stands for 외국어 고등학교 입학 시험 (an entrance examination for a foreign language high school)."),
        card("한국에서는: school districts (학군)", _KC),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 결심(하다), 과외(하다/받다), 교제(하다), 반대(하다), 불합격(하다), 찬성(하다) and 합격(하다) take the forms in parentheses; –게 되다 and the repeated question words are explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if _HG(w)])), table(["Pattern", "Meaning"], [["-게 되다", "to get to; to come to; to turn out"], ["누구 누구 / 뭐 뭐 / 어디 어디", "repeated question words"]])]),
        card("Follow-up 1 (Reading): the common concerns of Korean teenagers",
             "The book gives four statements about common concerns of Korean teenagers and five topics (a. interacting with the opposite gender; b. allowance; c. grades and GPA; d. communication with parents; e. appearance) and asks you to write the letter of each statement’s topic, one topic being left over. The statements are the book’s; the answers are mine (d is the topic with no match).",
             tables=[table(["Statement", "Letter", "Topic (mine)"], [[a, b, c] for a, b, c in _TOPIC], say=[0])]),
        card("Activities left out", "The SMART Board activities, the role reading of 지훈 and 연아, Follow-up 2 (listening to three conversations about falling GPA, a low SAT score or disagreement with parents) and the list of useful websites (Seoul High School, Daewon Foreign Language High School, Seoul Girls’ Commercial High School) need audio, web pages and classmates."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG), k=3)
        + [M("What did 지훈 decide?", "To take the foreign-language high school entrance exam", ["To go abroad", "To quit school", "To move"], "외고 입시 보기로 했어."), M("What do 지훈’s parents think?", "They agree with his opinion", ["They object", "They don’t know", "They are angry"], "내 의견에 찬성하셔."), M("What will 지훈 start next week?", "Private lessons", ["A job", "A trip", "A club"], "과외받게 될 거야."), M("Why is 연아 upset?", "Her final exam grades fell", ["She lost her bag", "She is sick", "She has no friends"], "기말 시험 성적 때문에 속상해."), M("By how many places did 연아’s rank drop?", "Eight", ["Two", "Five", "Eighteen"], "팔 등이나 떨어졌어."), M("What is 연아’s worst score?", "Math", ["English", "Korean", "Science"], "수학 점수는 정말 나빠."), M("What does 지훈 recommend?", "Going to an academy", ["Moving schools", "Quitting", "Sleeping more"], "학원에 다녀 봐."), M("What is 연아 doing about academies?", "Looking into them", ["Quitting one", "Teaching one", "Ignoring them"], "학원을 알아보는 중이야."),
           M("Which topic matches “학생들의 가장 큰 걱정은 학교 성적입니다”?", "Grades and GPA", ["Allowance", "Appearance", "Interacting with the opposite gender"], "My answer."), M("Which topic matches “부모님께 용돈을 받아서 쓰는 학생이 많았습니다”?", "Allowance", ["Grades and GPA", "Appearance", "Communication with parents"], "My answer."),
           F("난 기말 시험 ___ 때문에 속상해. (grades)", "성적", ["입시", "과외"], "성적."), F("왜? ___가 떨어졌어? (rank)", "등수", ["점수", "성적표"], "등수."), F("네가 ___. (I envy you)", "부럽다", ["속상하다", "기쁘다"], "부럽다."), F("다음 주부터 과외받게 ___ 거야. (will end up)", "될", ["된", "되는"], "-게 되다."), F("너는 학원 ___ 어디를 다녔니? (which ones, repeated)", "어디", ["누구", "언제"], "어디 어디."),
           read_q("외고 입시 보기로 했어"), read_q("내 의견에 찬성하셔"), read_q("기말 시험 성적 때문에 속상해"), read_q("학원을 알아보는 중이야"), read_q("학원에 다니면 성적이 좀 오를 거야")]
    ),
)

# ================================================================== L8: Grammar C: repeated question words
_RQ1 = [("어제 파티에서 고등학교 친구들을 만났어.", "I saw high school friends at a party."), ("그래? 누구 누구를 만났어?", "“Who and who” did you see? Who are they? / Which ones did you see?"), ("이기덕, 최대용하고 신창민.", "(They are) Lee Kideok, Choi Daeyong, and Shin Changmin.")]
_RQ2 = [("유럽여행 갔을 때 어디 어디 방문했어요?", "“Where and where” / Which places did you visit when you toured Europe?"), ("테니스 치러 언제 언제 가요?", "“When and when” do you go to play tennis?"), ("백화점에서 뭐 뭐 샀어요?", "“What and what” / What (multiple objects) did you buy at the department store?")]
_RQV = [("누구", "누구 누구", "who"), ("언제", "언제 언제", "when"), ("어디", "어디 어디", "where"), ("무엇 / 뭐", "뭐 뭐", "what"), ("무슨", "무슨 무슨", "what kind of"), ("어떤", "어떤 어떤", "which")]
L8 = lesson(
    "Ch 33 · Grammar C: the function of repeated question words",
    "누구 누구 · 언제 언제 · 어디 어디 · 뭐 뭐 · 여러 사람 · 여러 곳 · 여러 가지",
    requires=[],
    cards=[
        card("Repeated question words",
             "Recall the question words you learned in earlier chapters: 누구, 언제, 어디, 무엇, 무슨, and 어떤. These question words can be repeated, as in 누구 누구를 만났어요? (Who did you meet?) and 어디 어디에서 쇼핑했어요? (Where did you do shopping?). These repeated question words elicit information specific to multiple objects (persons, things, places, times, dates, etc.).",
             tables=[table(["Question word", "Repeated", "Meaning"], [list(r) for r in _RQV], say=[1])]),
        card("A conversation between two high school friends", "Speaker B repeats 누구 in his question to elicit the specific names of the high school friends Speaker A met. (The English is the book’s.)", examples=dlg([("가", _RQ1[0][0], _RQ1[0][1]), ("나", _RQ1[1][0], _RQ1[1][1]), ("가", _RQ1[2][0], _RQ1[2][1])])),
        card("More examples", "Here are more example sentences where question words repeat. (The English is the book’s.)", examples=passage(_RQ2)),
        card("Activities left out", "Follow-up 1 (listening to four exchanges and ticking the repeated question word) is an audio activity; Follow-up 2 (Schedule A and Schedule B for Suzie, a college student, completed with a partner, with the model 수지 씨는 어제 누구 누구하고 점심을 먹었어요? / 어제 어디 어디서 쇼핑을 했어요? / 어제 언제 언제 수업이 있었어요?) needs the schedules and a partner."),
    ],
    exercises=uniq(
        _tr(_RQ1 + _RQ2, k=3)
        + [M("What do repeated question words elicit?", "Information about multiple persons, things, places, times, etc.", ["A yes/no answer", "A command", "A single item only"], "The book’s note."), M("What does 누구 누구를 만났어요? ask?", "Which people did you meet?", ["Who are you?", "Where did you go?", "When did you meet?"], "누구 누구."), M("What does 어디 어디 방문했어요? ask?", "Which places did you visit?", ["Which people?", "Which times?", "Which things?"], "어디 어디."), M("What does 뭐 뭐 샀어요? ask?", "What multiple things did you buy?", ["Where did you buy?", "Who bought?", "When did you buy?"], "뭐 뭐."),
           F("그래? ___ 누구를 만났어? (who and who)", "누구", ["어디", "언제"], "누구 누구."), F("유럽여행 갔을 때 ___ 어디 방문했어요? (where and where)", "어디", ["누구", "무엇"], "어디 어디."), F("테니스 치러 언제 ___ 가요? (when and when)", "언제", ["어디", "누구"], "언제 언제."), F("백화점에서 ___ 뭐 샀어요? (what and what)", "뭐", ["누구", "어디"], "뭐 뭐."),
           read_q("어제 파티에서 고등학교 친구들을 만났어"), read_q("그래? 누구 누구를 만났어"), read_q("유럽여행 갔을 때 어디 어디 방문했어요"), read_q("테니스 치러 언제 언제 가요"), read_q("백화점에서 뭐 뭐 샀어요")]
    ),
)

# ================================================================== L9: Grammar D: -게 되다
_GD0 = [("오바마가 미국 대통령이 되었어요.", "Obama became the U.S. President."), ("건강해졌어요.", "I became healthier.")]
_GD1 = [("수술 후 다시 걷게 되었어요.", "After surgery I got to walk again."), ("다음 달에 미국으로 유학가게 되었습니다.", "I get to go to the U.S. to study next month."), ("한국 음악을 좋아하게 되었습니다.", "I came to like Korean music."), ("민 선생님께서 이번에 상을 받게 되셨어요.", "It turns out that Mr. Min will receive an award this time."), ("스무 번의 맞선 끝에 결혼하게 되었어요.", "After twenty blind dates I got married.")]
_GD2 = [("디엘아이 온 후에 뭐가 달라졌어요?", "What has changed since you came to DLI?"), ("네, 아침에 일찍 일어나게 되었어요. 그리고 매일 규칙적으로 운동도 하게 되었어요.", "Yes, I came to get up early in the morning. And I also came to exercise regularly every day."), ("최 일병은 디엘아이 온 후에 좋은 친구들을 많이 만나게 되었어요.", "Private First Class Choi has come to meet many good friends since coming to DLI.")]
_QA = [("우리 딸 지우가 이번에 외국어 고등학교에 입학하게 되었어요.", "My daughter Jiwoo has come to enter a foreign language high school this time."), ("주위에서 여러 가지 준비해야 할 것이 많다고 하는데 어떻게 해야 할지 잘 모르겠어요.", "People around me say there are many things to prepare, but I don’t know what to do."), ("사실 우리 지우는 어릴 때는 영어를 별로 안 좋아했어요.", "Actually, when Jiwoo was little she didn’t like English very much."), ("근데, 미국에 있는 이모 집에 갔다 온 후부터 영어를 아주 좋아하게 되었어요.", "But since she went to her aunt’s house in America and came back, she has come to like English a lot."), ("중학교 때는 학교 수업을 열심히 준비하고 집에서는 영어 비디오를 많이 보여 주었어요.", "In middle school she prepared for school classes diligently, and at home I showed her many English videos."), ("고등학교에 가면 좀 다르게 공부를 시켜야 할 것 같은데 어떻게 하면 좋을까요?", "When she goes to high school, I think I need to have her study a bit differently, but what would be good?")]
_GDM = [("A", "박 일병은 김치를 좋아합니까?", "Private First Class Park, do you like kimchi?"), ("B", "디엘아이에 오기 전에는 김치를 싫어했지만 지금은 김치를 좋아합니다. 한국인 친구와 한국 식당에 가서 한국음식을 먹으면서부터 김치를 좋아하게 되었어요.", "Before coming to DLI I disliked kimchi, but now I like kimchi. Since going to a Korean restaurant with a Korean friend and eating Korean food, I have come to like kimchi.")]
_GDV = [("걷다", "to walk", "걷게 되었어요"), ("가다", "to go", "가게 되었어요"), ("좋아하다", "to like", "좋아하게 되었어요"), ("받다", "to receive", "받게 되었어요"), ("결혼하다", "to marry", "결혼하게 되었어요"), ("일어나다", "to get up", "일어나게 되었어요"), ("입학하다", "to enter school", "입학하게 되었어요"), ("만나다", "to meet", "만나게 되었어요")]
L9 = lesson(
    "Ch 33 · Grammar D: –게 되다, to come to; to get to; to turn out",
    "-게 되다 · 걷게 되었어요 · 유학가게 되었습니다 · 좋아하게 되었습니다 · 결혼하게 되었어요 · ~이/가 되다 · -아/어지다",
    requires=[],
    cards=[
        card("Review: ~이/가 되다 and –아/어지다",
             "In earlier chapters you learned how to express a change in state or condition by using ~이/가 되다 and –아/어지다, both of which mean “to become”. Note that ~이/가 되다 is preceded by a noun, and –아/어지다 is preceded by a stative verb. (The English is the book’s.)",
             examples=passage(_GD0)),
        card("–게 되다: to come to; to get to; to turn out",
             "In this lesson you will learn about another grammar feature used to express a change in state or condition: –게 되다. This grammar feature works only with an action verb and means to come to, to get to, or to turn out. For example (the English is the book’s):",
             examples=passage(_GD1)),
        card("Forms (mine)", "Action verb stem + 게 되다 (past: 게 되었어요 / 게 됐어요).",
             tables=[table(["Verb", "Meaning", "-게 되었어요"], [list(r) for r in _GDV], say=[0, 2])]),
        card("Follow-up 3 (Speaking and listening): changes since coming to DLI",
             "Think about changes in your life since you came to DLI, discuss them in pairs and present two of them. The book’s models (DLI is spelled out as 디엘아이; the English is mine):",
             examples=dlg([("A", _GD2[0][0], _GD2[0][1]), ("B", _GD2[1][0], _GD2[1][1]), ("A", _GD2[2][0], _GD2[2][1])])),
        card("Follow-up 4 (Reading): a question on an education consultation website",
             "The following text was posted on the Q&A section of an education consultation website by 지우 엄마 (Jiwoo’s mother). The book asks you to circle –게 되다 and translate the sentences that contain it into English (the sentences with 게 되었어요 are the first and the fourth). The ellipsis is dropped; the English is mine.",
             examples=passage(_QA)),
        card("Follow-up 5 (Speaking and listening): experiences with the Korean language and culture", "You share changes related to Korean grammar, Korean food and Korean products using –게 되다. The book’s model (the English is mine):", examples=dlg(_GDM)),
    ],
    exercises=uniq(
        _tr(_GD0 + _GD1 + _QA[:1] + _QA[3:4], k=3)
        + [M("What does –게 되다 work with?", "Only action verbs", ["Only stative verbs", "Only nouns", "All verbs"], "The book’s note."), M("What does –게 되다 mean?", "To come to; to get to; to turn out", ["To want to", "To try to", "To be able to"], "The book’s note."), M("What precedes ~이/가 되다?", "A noun", ["A stative verb", "An action verb", "An adverb"], "Review."), M("What precedes –아/어지다?", "A stative verb", ["A noun", "An action verb", "A particle"], "Review."), M("What does 한국 음악을 좋아하게 되었습니다 mean?", "I came to like Korean music", ["I like Korean music", "I will like Korean music", "I disliked Korean music"], "–게 되다."), M("What does 수술 후 다시 걷게 되었어요 mean?", "After surgery I got to walk again", ["I will walk", "I cannot walk", "I walked before surgery"], "–게 되다."),
           F("수술 후 다시 걷___ 되었어요. (-게)", "게", ["도록", "느라"], "-게 되다."), F("다음 달에 미국으로 유학가게 ___ 습니다. (became; polite past)", "되었", ["하였", "보았"], "되었습니다."), F("한국 음악을 좋아하___ 되었습니다. (-게)", "게", ["도록", "고"], "-게 되다."), F("민 선생님께서 이번에 상을 받게 ___. (honorific past)", "되셨어요", ["하셨어요", "보셨어요"], "되시다."), F("스무 번의 맞선 끝에 결혼하게 ___. (became)", "되었어요", ["했어요", "봤어요"], "되었어요."),
           read_q("수술 후 다시 걷게 되었어요"), read_q("다음 달에 미국으로 유학가게 되었습니다"), read_q("한국 음악을 좋아하게 되었습니다"), read_q("우리 딸 지우가 이번에 외국어 고등학교에 입학하게 되었어요"), read_q("영어를 아주 좋아하게 되었어요")]
    ),
)

# ================================================================== L10: Activities: special activities article and Q&A
_TK = [("안녕하세요?", "Hello."), ("오늘은 사당중학교의 특별활동반(특활반)에 대해 소개해 드리겠습니다.", "Today I will introduce the special activity clubs of Sadang Middle School."), ("매월 첫째, 셋째 금요일(오후 한 시 이십 분부터 세 시 삼십 분까지)에 학생들은 자신들이 선택한 특별활동반에서 시간을 보냅니다.", "On the first and third Friday of every month (from 1:20 to 3:30 p.m.), students spend time in the special activity club they have chosen."), ("특활반으로는 연극반, 무용반, 미술반, 공예반, 외국어반, 음악반이 있습니다.", "The special activity clubs include a drama club, a dance club, an art club, a craft club, a foreign language club and a music club."), ("이 중에 가장 인기 있는 반은 영어반과 음악반입니다.", "Among these, the most popular clubs are the English club and the music club."), ("영어반에서는 학생들이 영어웅변을 배우거나 영어연극을 연습합니다.", "In the English club, students learn English speeches or practice English plays."), ("음악반에서는 학생들이 원하는 악기를 하나씩 배울 수 있습니다.", "In the music club, students can learn one instrument each, the one they want."), ("원하면 악기 대신 노래 부르기를 배울 수도 있습니다.", "If they want, they can also learn singing instead of an instrument."), ("학기말에는 학생들이 특활반에서 배운 것을 발표합니다.", "At the end of the semester, students present what they learned in the clubs."), ("이 발표회에는 부모님들도 초대됩니다.", "Parents are also invited to this presentation.")]
_QA2 = [("저는 실업계에 다니는 고삼 학생입니다.", "I am a third-year student in a vocational high school."), ("실업계 학생이지만 대학에 가고 싶습니다.", "I’m a vocational student, but I want to go to college."), ("성적은 좋은데, 국어, 영어, 수학이 약해서 수능 점수가 잘 안 나와요.", "My grades are good, but Korean, English and math are weak, so my college entrance exam score doesn’t come out well."), ("어떻게 공부해야 할까요?", "How should I study?"), ("우선 가고 싶은 대학을 빨리 결정하세요.", "First, decide quickly which college you want to go to."), ("그리고 그 대학에 맞게 입시 준비를 하세요.", "And prepare for the entrance exam to suit that college."), ("시험 점수보다 학교 성적을 더 중요하게 생각하는 대학도 많이 있어요.", "There are many colleges that consider school grades more important than exam scores."), ("수능 점수를 올리고 싶으면 입시 학원에 다니세요.", "If you want to raise your exam score, go to an entrance exam academy."), ("국, 영, 수는 혼자 공부하기 힘든 과목이니까요.", "Because Korean, English and math are subjects that are hard to study alone."), ("저도 실업계 고등학교를 졸업하고 대학에 들어 왔어요.", "I also graduated from a vocational high school and entered college."), ("꼭 가고 싶은 대학에 합격하기 바래요.", "I hope you pass the college you really want to go to.")]
L10 = lesson(
    "Ch 33 · Activities: Sadang Middle School’s special activity clubs and a college-entrance Q&A",
    "특별활동반 · 특활반 · 사당중학교 · 수능 · 입시 학원 · 실업계 · 고삼 · 성적 고민",
    requires=[],
    cards=[
        card("Activity 2 (Reading): an article posted by a Sadang Middle School student",
             "The following article was posted by a student at Sa-dang Middle School. It introduces the “special activities” (extracurricular activities) at her school. The book glosses 공예: craft; 발표하다: to present. The text is the book’s with the time spelled out in Hangul; the English is mine.",
             examples=passage(_TK)),
        card("The book’s three questions, answered (mine)", "The book leaves the answers blank; these are mine.",
             tables=[table(["Question", "Answer (mine)"], [["1. When are the extracurricular activities held?", "On the first and third Friday of every month, from 1:20 to 3:30 p.m."], ["2. What can students do during the music class?", "Learn one instrument each, or learn singing instead"], ["3. What do students do at the end of a semester?", "Present what they learned; parents are invited to the presentation"]])]),
        card("Activity 3 (Reading): a Q&A about a college entrance exam",
             "The book shows a Q&A on a website’s “worry Q&A > entrance exam counseling > college entrance exam” page. The question was posted by a third-year high school student whose user name and the date and view count are left out; 고3 is spelled out as 고삼. The book glosses 수능 (수학능력시험): the college entrance exam, Korean SAT. The question and the answer (the English is mine):",
             examples=passage(_QA2)),
        card("The answers (mine)", "The book asks you to identify the poster’s biographical information, the concern and the type(s) of advice (ticking boxes: focus on improving GPA; decide first which college to attend; consider attending a private coaching institute; trust yourself and study wholeheartedly until the exam). My answers:",
             tables=[table(["Item", "Answer (mine)"], [["Biographical information", "A third-year student at a vocational high school who wants to go to college"], ["Concern", "Good grades but weak Korean, English and math, so the college entrance exam score is low"], ["Advice", "Decide first which college to attend; consider attending a private coaching institute (the other two boxes are not in the answer)"]])]),
        card("Activities left out", "Activity 1 (SMART Board), Activity 2 of the listening section (a clip from the TV drama 거침없이 하이킥 and the situation chosen) and Activity 4 (a teen hotline, with two callers heard and advice written in two groups) need audio, video and classmates."),
    ],
    exercises=uniq(
        _tr(_TK[1:] + _QA2, k=3)
        + [M("Which school’s clubs are introduced?", "Sadang Middle School", ["Seoul High School", "A university", "A kindergarten"], "사당중학교."), M("When are the clubs held?", "The first and third Friday of each month", ["Every day", "Every Monday", "Once a year"], "첫째, 셋째 금요일."), M("Which are the most popular clubs?", "The English club and the music club", ["The art club", "The dance club", "The craft club"], "영어반과 음악반."), M("What can students do in the English club?", "Learn English speeches or practice English plays", ["Cook", "Swim", "Paint"], "영어웅변, 영어연극."), M("What do students do at the end of the semester?", "Present what they learned", ["Take a trip", "Take a test", "Clean the school"], "발표합니다."), M("Who asked the college-entrance question?", "A third-year vocational high school student", ["A parent", "A teacher", "A middle schooler"], "실업계에 다니는 고삼 학생."), M("What is the student’s problem?", "Weak Korean, English and math lower the exam score", ["No friends", "No money", "A long commute"], "수능 점수가 잘 안 나와요."), M("What is the first advice given?", "Decide the college you want to go to quickly", ["Quit school", "Study alone", "Skip exams"], "가고 싶은 대학을 빨리 결정하세요."),
           F("오늘은 사당중학교의 ___반에 대해 소개해 드리겠습니다. (special activity)", "특별활동", ["교내", "방과"], "특별활동반."), F("이 중에 가장 ___ 있는 반은 영어반과 음악반입니다. (popular)", "인기", ["성적", "점수"], "인기 있는."), F("학기말에는 학생들이 배운 것을 ___합니다. (present)", "발표", ["입학", "졸업"], "발표하다."), F("수능 점수를 올리고 싶으면 입시 ___에 다니세요. (academy)", "학원", ["학교", "학기"], "입시 학원."), F("꼭 가고 싶은 대학에 ___하기 바래요. (pass)", "합격", ["졸업", "불합격"], "합격."),
           read_q("사당중학교의 특별활동반에 대해 소개해 드리겠습니다"), read_q("가장 인기 있는 반은 영어반과 음악반입니다"), read_q("음악반에서는 학생들이 원하는 악기를 하나씩 배울 수 있습니다"), read_q("수능 점수를 올리고 싶으면 입시 학원에 다니세요"), read_q("꼭 가고 싶은 대학에 합격하기 바래요")]
    ),
)

# ================================================================== L11: Activity 3 of Topic B: Hyunsoo's routine (no text) + core vocab
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L11 = lesson(
    "Ch 33 · Core vocabulary and self-evaluation",
    "주요 단어 · 한국의 교육 · 학교 · 성적 · 입시 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning, and the book’s parenthesized forms such as ~하다 and ~되다 show how a noun forms a verb. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (1학년 → 일 학년; 9년 → 구 년; 100점 → 백 점; 고3 → 고삼)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and discuss the Korean school system, academic subjects, and a typical student’s daily routine; and talk about common concerns of students in Korea.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; –도록 (up to the point; until; in order to; so that); –느라(고) (because of; due to); repeated question words; –게 되다 (to become; to come to; to turn out); and the Sino-Korean syllables within 국립 (國立) and 점수 (點數)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 의무 mean?", "obligation; duty; responsibility", ["a system", "a subject", "a point"], "義務."), M("What does 제도 mean?", "a system", ["a duty", "a subject", "an exam"], "制度."), M("What does 시간표 mean?", "a timetable; a (class) schedule", ["a report card", "a subject", "a score"], "時間表."), M("What does 성적표 mean?", "a report card; a transcript", ["a timetable", "an entrance exam", "a lunch box"], "成績表."), M("What does 과외 mean?", "extracurricular lesson; private tutoring", ["a school lunch", "a speech", "a subject"], "課外."), M("What does 이성 mean?", "the opposite/other gender", ["the same gender", "a friend", "a relative"], "異性."), M("What does 합격 mean?", "passing (an examination)", ["failing", "agreeing", "opposing"], "合格."),
           F("저는 이 년제 대학을 다니는데 졸업 후에 ___을 갈 생각입니다. (study abroad)", "유학", ["입학", "결석"], "유학."), F("오늘 ___ 시험을 못 봐서 학원에 다녀야겠어요. (math)", "수학", ["도덕", "체육"], "수학."), F("올해부터는 열심히 한국어를 공부하기로 ___했어요. (resolved)", "결심", ["결석", "지각"], "결심."), F("어제 아파서 학교에 ___했습니다. (was absent)", "결석", ["지각", "합격"], "결석."), F("제 동생은 지금 외고 ___준비를 하고 있어요. (entrance exam)", "입시", ["성적", "급식"], "입시."),
           read_q("주요 단어"), read_q("한국의 교육"), read_q("성적표"), read_q("과외"), read_q("시간표")]
    ),
)

UNIT = unit("Semester 2 · Unit 9 · Chapter 33: Education in Korea (한국의 교육)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])
