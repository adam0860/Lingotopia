"""Unit 71: KBC Semester III, Unit 16, Lesson 6 - Alternative Schools and Adult Education (대안 학교 및 평생 교육).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 16, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH6 = [("경쟁", "competition", "경쟁이 심화되다"), ("실망", "disappointment", "시험에 떨어져서 실망하다"), ("원어민", "a native speaker", "원어민 강사를 뽑다"), ("확대", "expansion; enlargement", "복지혜택을 확대하다"), ("사례", "an example; an instance", "성공사례를 분석하다"), ("평가", "evaluation", "학생을 평가하다"), ("열풍", "fever; frenzy; bandwagon", "영어 열풍이 불다"), ("이별", "parting; farewell", "가족과 이별하다"), ("기준", "standard; criteria", "기준을 마련하다")]
_HJ6 = [("專 전", "only; exclusive", "전임, 전공"), ("語 어", "language", "원어민, 표준어"), ("入 입", "entering; getting in", "입시, 입학"), ("敎 교", "teaching", "교사, 교육"), ("望 망", "outlook; hope", "희망, 전망")]
_HJW6 = [("전임", "full-time; “exclusively charged”"), ("전공", "a major"), ("원어민", "a native speaker"), ("표준어", "a standard language"), ("입시", "an entrance examination"), ("입학", "entrance into school"), ("교사", "a teacher"), ("교육", "education"), ("희망", "a wish; hope"), ("전망", "a view; a prospect")]
_OPP6 = [("표준어", "사투리", "a standard language: a dialect"), ("절망", "희망", "despair: hope"), ("입학생", "졸업생", "an entering student: a graduate"), ("교사", "학생", "a teacher: a student")]
_REL6 = [("A", "종교", "불교, 개신교, 천주교", "religion: Buddhism, Protestantism, Catholicism"), ("B", "외국어", "불어, 독어, 중국어", "foreign languages: French, German, Chinese"), ("C", "교육자", "교수, 교관, 교사", "educators: professor, instructor, teacher"), ("D", "대학교", "전공, 부전공, 복수전공", "university: major, minor, double major")]
_L6X = [("사투리", "a dialect"), ("불어", "French"), ("한국어", "Korean"), ("절망", "despair"), ("입학생", "an entering student"), ("입시생", "an entrance-exam candidate"), ("졸업생", "a graduate"), ("신입생", "a new student; a freshman"), ("교수", "a professor"), ("교장", "a principal"), ("교관", "an instructor (military)"), ("불교", "Buddhism"), ("개신교", "Protestantism"), ("천주교", "the Catholic Church"), ("독어", "German"), ("중국어", "Chinese"), ("부전공", "a minor"), ("복수전공", "a double major"), ("교육자", "an educator"), ("외국어", "a foreign language"), ("종교", "religion"), ("대학교", "a university"), ("조기유학", "early study abroad"), ("기러기 아빠", "a “wild goose dad”"), ("합격", "passing (an exam)"), ("불합격", "failing (an exam)"), ("취학", "entering school"), ("송금", "remitting money"), ("끼니", "a meal"), ("교과서", "a textbook")]
L1 = lesson(
    "U16 L6 · Review: school and exam words and Sino-Korean 專 語 入 敎 望",
    "대안 학교 및 평생 교육 · 단어 복습 · 한자어 복습 · 경쟁 · 실망 · 원어민 · 확대 · 사례 · 평가 · 열풍 · 이별 · 기준 · 專 語 入 敎 望",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives nine phrases with the last word underlined and asks you to connect each underlined word with its meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH6], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ6], say=[2]), ktable(_HJW6)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 표준어: 사투리, 불어, 한국어; B. 절망: 실망, 전망, 희망; C. 입학생: 입시생, 졸업생, 신입생; D. 교사: 교수, 학생, 교장).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP6], say=[0, 1])]),
        card("한자어 복습 2: the related word (my answers)", "Choose from the box (교육자, 입시, 외국어, 종교, 대학교) the word most related to the three words on the right; 입시 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Why"], [list(r) for r in _REL6], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L6X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 008): you hear a description or a hint for each of eight words and write the letter of the word that fits. The eight words are A. 조기유학, B. 기러기 아빠, C. 합격, D. 취학, E. 송금, F. 끼니, G. 불합격 and H. 교과서; their meanings are in the word list above. It is audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH6], k=3) + _tr(_HJW6, k=3) + _tr(_L6X, k=3) + _tr([(a, c) for a, b, c in _OPP6], k=3)
        + [M("What does the syllable 專 (전) mean?", "only; exclusive", ["language", "teaching", "hope"], "전공."), M("What does the syllable 語 (어) mean?", "language", ["only", "entering", "hope"], "원어민."), M("What does the syllable 入 (입) mean?", "entering; getting in", ["language", "teaching", "outlook"], "입학."), M("What does the syllable 敎 (교) mean?", "teaching", ["language", "entering", "only"], "교육."), M("What does the syllable 望 (망) mean?", "outlook; hope", ["teaching", "language", "entering"], "희망."),
           M("Which word is the opposite of 표준어?", "사투리", ["불어", "한국어", "독어"], "A dialect."), M("Which word is the opposite of 절망?", "희망", ["실망", "전망", "소망"], "Hope."), M("Which word is the opposite of 입학생?", "졸업생", ["입시생", "신입생", "교수"], "A graduate."), M("Which word is the opposite of 교사?", "학생", ["교수", "교장", "교관"], "A student."),
           M("Which word fits 불교, 개신교, 천주교?", "종교", ["외국어", "교육자", "대학교"], "Religion."), M("Which word fits 불어, 독어, 중국어?", "외국어", ["종교", "교육자", "대학교"], "Foreign languages."), M("Which word fits 교수, 교관, 교사?", "교육자", ["종교", "외국어", "대학교"], "Educators."), M("Which word fits 전공, 부전공, 복수전공?", "대학교", ["종교", "외국어", "교육자"], "University."),
           F("원어민 ___를 뽑았습니다. (instructor)", "강사", ["학생", "친구"], "원어민 강사."), F("영어 ___이 불고 있습니다. (fever)", "열풍", ["바람", "소풍"], "열풍."), F("가족과 ___했습니다. (to part)", "이별", ["경쟁", "평가"], "이별하다."), F("복지혜택을 ___했습니다. (to expand)", "확대", ["평가", "이별"], "확대하다."), F("시험에 떨어져서 ___했습니다. (to be disappointed)", "실망", ["경쟁", "기준"], "실망하다."),
           read_q("경쟁이 심화되었습니다"), read_q("원어민 강사를 뽑았습니다"), read_q("영어 열풍이 불고 있습니다"), read_q("기준을 마련했습니다"), read_q("성공사례를 분석합니다")]
    ),
)

# ================================================================== L2 Part 1
_CRED = [
    ("가정 형편이나 개인적인 여건 때문에 대학 진학을 포기하는 사람들이 있다.", "There are people who give up going on to college because of family circumstances or personal conditions."),
    ("평생교육진흥원에서는 혼자서도 대학 학위를 딸 수 있는 학점은행제를 운영하고 있다.", "The Lifelong Education Promotion Institute runs the 학점은행제 (credit bank system), with which one can earn a college degree even on one’s own."),
    ("고교 졸업자나 동등 이상의 학력을 가진 사람은 누구나 가능하다.", "Anyone who is a high school graduate or has an equal or higher level of schooling can do it."),
    ("학점은행제는 학교 밖에서 이루어지는 다양한 형태의 학습과 자격을 학점으로 인정하고 그 학점을 누적해 기준을 충족하면 전문대학 또는 대학 졸업과 동등한 학위를 수여하는 제도다.", "The 학점은행제 is a system that recognizes various forms of learning and qualifications taking place outside school as credits, and, when those credits are accumulated and the standard is met, awards a degree equal to a junior college or college graduation."),
    ("학점 취득은 평가인정기관으로 지정된 대학 및 평생교육원, 직업능력개발훈련시설, 각종 학원 등 다양한 평생교육과 직업교육 시설에서 평가인정 학습과목을 이수하는 등 다양한 방법이 있다.", "There are various ways of obtaining credits, such as completing accredited courses at various lifelong and vocational education facilities, including universities and lifelong education centers designated as evaluation-accredited institutions, vocational skills development and training facilities, and all kinds of private institutes."),
    ("최근 학점은행제 교육기관이 늘어나면서 기관 선택이 중요해졌다.", "Recently, as the educational institutions of the 학점은행제 have increased, choosing an institution has become important."),
    ("평생교육진흥원 평가인정팀 관계자는 학위를 취득하기 위해 학점은행제를 이용할 때 우선적으로 평생교육진흥원 홈페이지에 있는 교육훈련기관 검색을 통해 해당 기관이 요건을 충족하는지를 확인해보는 것이 좋다고 조언했다.", "An official of the Institute’s evaluation and accreditation team advised that when using the 학점은행제 to obtain a degree, it is good first of all to check, through the education and training institution search on the Institute’s homepage, whether the institution in question meets the requirements."),
]
_SPEAK6A = [("미국에서는 홈스쿨링을 하는 사람들이 많지만, 한국에서는 홈스쿨링으로 교육을 시키는 부모가 많지 않습니다.", "In the United States there are many people who do homeschooling, but in Korea there are not many parents who educate by homeschooling."), ("먼저 홈스쿨링이 무엇인지, 그리고 홈스쿨링을 하려면 무엇이 필요한지 생각해 보세요.", "First think about what homeschooling is and what is needed to do homeschooling."), ("그리고 홈스쿨링이 무엇인지 잘 모르는 한국사람들에게 설명을 하는 것처럼 반 친구들에게 생각한 것을 이야기해 보세요.", "Then tell your classmates what you thought, as if explaining to Koreans who do not know well what homeschooling is.")]
L2 = lesson(
    "U16 L6 · Part 1 (도입 학습): 혁신학교 and the 학점은행제",
    "도입 학습 · 혁신학교 · 평생교육 · 학점은행제 · 학위 · 학점 · 평생교육진흥원 · 홈스쿨링 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 혁신학교 (innovative school) — the book’s note",
             "혁신학교 “innovative school” is a school with fewer than 25 students per class and 6 or fewer classes per grade. This type of school was created by the Korean government in response to a troubled public education system in which strong competition for the college entrance exam created dissatisfaction among teachers, students, and parents. Once a regular school is designated as 혁신학교, the government supports the school in order to maximize the autonomy of the teachers and the participation of students."),
        card("학습활동 2 (Reading): the 학점은행제 (credit bank system)",
             "The following is an explanation of the 학점은행제 (© Kyunghyang). The text is the book’s; the quotation marks ‘ ’ and “ ” are removed, and the middle dot in 평생·직업교육시설 is written 평생교육과 직업교육 시설. The English is mine.",
             examples=passage(_CRED)),
        card("학습활동 2: the questions answered (mine)",
             "1. Before reading, guess in English what the 학점은행제 is: for example, “a bank of credits”, a system in which you can gather credits from different places.\n\n"
             "2. After reading:\n"
             "A. The guess should be modified if necessary: the 학점은행제 is a system that recognizes learning and qualifications gained outside school as credits and awards a college degree when enough credits are accumulated to meet the standard.\n\n"
             "B. The qualification: being a high school graduate or having an equivalent or higher level of schooling.\n\n"
             "C. The advice: before using the system, check on the homepage of the Lifelong Education Promotion Institute, through the education and training institution search, whether the institution you choose meets the requirements.\n\n"
             "D. People who would be interested: those who gave up going to college because of family circumstances or personal conditions, working adults who cannot attend a university, and anyone who wants a degree without going to a regular college."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK6A)),
        card("Activities left out", "학습활동 1 (Listening, track 009): an explanation of 평생교육 (lifelong education) (© edunet4u.net); you give its English meaning and say what is advised. 학습활동 3 (Listening, tracks 010 and 011): a YTN news report on a 혁신학교: how it differs from a regular school, what 경기도 plans for 혁신학교 and what is needed to establish more of them. It is audio."),
    ],
    exercises=uniq(
        _tr(_CRED, k=3) + _tr(_SPEAK6A, k=2)
        + [M("How many students per class does a 혁신학교 have, at most?", "Fewer than 25", ["Fewer than 5", "Fewer than 50", "More than 40"], "The book’s note."), M("What does the government do once a school is designated as 혁신학교?", "It supports the school", ["It closes it", "It merges it", "It ignores it"], "The book’s note."), M("What does a 혁신학교 aim to maximize?", "The autonomy of the teachers and participation of the students", ["The number of classes", "The tuition", "The school hours"], "The book’s note."),
           M("Who runs the 학점은행제?", "The Lifelong Education Promotion Institute", ["The police", "A private company", "The army"], "평생교육진흥원."), M("Who can use the 학점은행제?", "High school graduates or those with equal schooling", ["Only university students", "Only children", "Only foreigners"], "고교 졸업자나 동등 이상의 학력."), M("What does the 학점은행제 award once the standard is met?", "A degree", ["A prize", "A pension", "A visa"], "학위."), M("What should one check first when choosing an institution?", "Whether it meets the requirements", ["Its price", "Its size", "Its location"], "요건."),
           F("대학 학위를 딸 수 있는 ___를 운영하고 있다. (credit bank system)", "학점은행제", ["평생교육", "혁신학교"], "학점은행제."), F("학점을 ___해 기준을 충족하면 학위를 수여한다. (to accumulate)", "누적", ["취득", "포기"], "누적하다."), F("학점 ___은 다양한 방법이 있다. (acquisition)", "취득", ["포기", "설립"], "취득."), F("해당 기관이 ___을 충족하는지 확인해야 한다. (requirement)", "요건", ["공약", "예산"], "요건."), F("대학 ___을 포기하는 사람들이 있다. (going on to)", "진학", ["졸업", "입시"], "진학."),
           read_q("학점은행제를 운영하고 있습니다"), read_q("고교 졸업자는 누구나 가능합니다"), read_q("해당 기관이 요건을 충족하는지 확인해 보세요"), read_q("홈스쿨링이 무엇인지 설명해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("걸치다", "(for a range of time or space) to extend; to span; to spread", "그 산은 전라도와 경상도에 걸쳐 있습니다. 우리는 삼 일에 걸쳐 시험을 봅니다."),
        ("생애", "(生涯) one’s life; lifetime", "올해는 제 생애 최고의 해입니다.", "삶, 인생"),
        ("학창시절", "(學窓時節) one’s school days", "생각해 보니 학창시절이 가장 재미있었어요."),
    ]),
    ("학습활동 2", [
        ("누적(하다/되다)", "(累積) accumulation (to accumulate/to be accumulated)", "우리나라의 누적 적자가 얼마나 됩니까?"),
        ("동등하다", "(同等) to be equal; to be of the same rank", "앞으로는 계약직 직원들도 정규직 직원들과 동등한 혜택을 받게 됩니다."),
        ("요건", "(要件) requirement; (pre)requisite", "지원하는 데 필요한 자격 요건이 무엇입니까?", "조건"),
        ("이수(하다)", "(履修) completing a course of study (to complete a course of study)", "박사학위에 필요한 과정은 다 이수했어요."),
        ("충족(하다; 시키다/되다)", "(充足) meeting (a requirement, criteria, etc.) (to meet/to be met)", "자격 요건을 충족하는 지원자들이 많습니다."),
        ("취득(하다)", "(取得) acquisition; acquiring; obtaining (to acquire; to obtain a license, diploma, etc.)", "어제 운전면허증을 취득했습니다.", "따다, 얻다, 획득하다"),
    ]),
    ("학습활동 3", [
        ("공약", "(公約) a pledge; a commitment; “public promise”", "그 사람은 선거 때 내세운 공약을 하나도 지키지 않았어요.", "약속"),
        ("선행(하다;되다)", "(先行) precedence (to precede)", "이 문제를 해결하려면 자금확보가 선행되어야 합니다."),
        ("설립(하다/되다)", "(設立) establishment; foundation (to establish; to found/to be established; to be founded)", "우리 학교가 언제 설립되었습니까?", "세우다"),
        ("시도(하다/되다)", "(試圖) an attempt; a trial (to make an attempt; to try/to be tried)", "한 번 시도해 본 후에 이야기해 봅시다."),
        ("신나다", "to be excited; to be elated", "아이들이 소풍을 간다고 신났어요."),
        ("예산", "(豫算) budget", "예산이 없어서 복지시설이 문을 닫는다고 합니다."),
        ("율동", "(律動) rhythm; rhythmic movement", "아이들이 율동 연습을 하고 있어요."),
        ("토론(하다)", "(討論) a discussion; a debate (to discuss; to debate)", "아이들이 토론 수업에 열심히 참여합니다.", "토의, 상의"),
        ("합치다", "to combine; to unite", "우리가 힘을 합치면 이 문제를 쉽게 해결할 수 있을 거예요."),
        ("확보(하다/되다)", "(確保) securing; procuring (to secure/to be secured)", "경찰에서 이번 사건을 풀 증거를 확보했습니다."),
        ("휴식", "(休息) a rest; relaxation; a break", "십 분간 휴식하겠습니다."),
    ]),
]
L3 = lesson(
    "U16 L6 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 걸치다 · 생애 · 학창시절 · 누적 · 동등하다 · 요건 · 이수 · 충족 · 취득 · 공약 · 선행 · 설립 · 시도 · 신나다 · 예산 · 율동 · 토론 · 합치다 · 확보 · 휴식",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s examples with digits are written out: 3일 → 삼 일 and 10분간 → 십 분간.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=12)),
)

# ================================================================== L4 Part 2
_HOME = [
    ("획일적인 학교교육에 대한 불만과 공교육 질 저하 현상 등이 맞물리면서 한국에서도 새로운 대안이 적지 않게 제시됐다.", "As dissatisfaction with uniform school education and the decline in the quality of public education interlock, quite a few new alternatives have been put forward in Korea too."),
    ("홈스쿨링도 그 중에 하나다.", "Homeschooling is one of them."),
    ("홈스쿨링이란 말 그대로 학교 대신 집에서 교육하는 방법.", "Homeschooling, as the word says, is a method of educating at home instead of school."),
    ("홈스쿨링은 일 년에 오만여 명이나 학교교육에서 이탈하는 학교교육의 부적응 학생에게 대안이 될 수 있다는 장점이 있다.", "Homeschooling has the advantage that it can be an alternative for the “students who fail to adapt to school education,” as many as 50,000 or so of whom break away from school education in a year."),
    ("김 교수로부터 홈스쿨링에 대해 들어 본다.", "We hear about homeschooling from Professor Kim."),
    ("한국의 홈스쿨링 실태는 어떤가.", "(Question) What is the state of homeschooling in Korea?"),
    ("미국의 경우 한 해에 백십만 명이 홈스쿨링을 한다.", "(Answer) In the case of America, 1.1 million people do homeschooling in a year."),
    ("홈스쿨링 학습을 하는 학생의 실력이 십 퍼센트 이상 앞선 것으로 평가되고 있다.", "The ability of students who study by homeschooling is evaluated as being ahead by more than 10 percent."),
    ("매년 이십 퍼센트가 늘어나는 추세에 있다.", "It is on a trend of increasing by 20 percent every year."),
    ("최근 들어선 학교 부적응자에 대한 대안교육이 아니라 교육의 다양성과 창조성 제고를 위한 홈스쿨링이 늘고 있다.", "Recently, it is not alternative education for those who fail to adapt to school but homeschooling for improving the diversity and creativity of education that is increasing."),
    ("한국도 공교육에 대한 불신에서 비롯된 대안교육으로 홈스쿨링에 대한 관심이 일기 시작하는 단계에 있다.", "Korea too is at the stage where interest in homeschooling is beginning to rise as an alternative education arising from distrust of public education."),
    ("현재는 천여 명이 공교육을 포기하고 홈스쿨링을 하고 있다.", "At present about 1,000 people have given up public education and are homeschooling."),
    ("하지만, 그 잠재적 수요는 매우 크다.", "But the potential demand is very large."),
    ("한 해에 탈학교 학생이 오만 명에 이르고 있다.", "The number of “out-of-school” students reaches 50,000 a year."),
    ("홈스쿨링을 위한 기반여건이 매우 취약한데.", "(Question) The base conditions for homeschooling are very weak, aren’t they?"),
    ("물론 홈스쿨링을 하려면 홈스쿨링을 하는 방법을 알아야 한다.", "(Answer) Of course, to do homeschooling you need to know how to do homeschooling."),
    ("홈스쿨링을 하려는 부모를 위한 코스나 전문튜터 양성을 위한 교육과정도 있다.", "There are courses for parents who want to do homeschooling and also an educational program for training specialist tutors."),
    ("한국튜터인증협회가 그것이다.", "The Korea Tutor Certification Association is that."),
    ("이곳에서 홈스쿨링 전문교사 양성과 홈스쿨링 학부형을 위한 과정을 만들어 진행하고 있다.", "Here they have created and are running courses for training specialist homeschooling teachers and for homeschooling parents."),
    ("전자교과서 학습을 고집하는 이유는.", "(Question) What is the reason you insist on studying with electronic textbooks?"),
    ("교과서는 학생이 효과적이고 체계적인 학습을 할 수 있도록 만들어진 가장 훌륭한 교재다.", "(Answer) The textbook is the best teaching material made so that students can study effectively and systematically."),
    ("그런 교과서가 학생에게 외면당하고 있다.", "Such textbooks are being turned away from by students."),
    ("학원학습이나 참고서와 문제집 위주의 주입식 학습을 하고 있는 게 현실이다.", "The reality is that they are doing cram-style study centered on institute study or reference books and workbooks."),
    ("교과서는 학생 스스로 공부하기 어렵다는 단점이 있다.", "The textbook has the weakness that it is hard for students to study by themselves."),
    ("이런 단점을 보완하기 위해 여러 기능을 넣어 자율적 학습을 할 수 있도록 도움을 주도록 설계된 게 전자교과서다.", "The electronic textbook is what was designed, by putting in various functions to make up for this weakness, to help students study autonomously."),
    ("전자교과서의 핵심은 반응식 학습이다.", "The core of the electronic textbook is interactive learning."),
]
_SPEAK6B = [("홈스쿨링의 장점과 단점에 대해 생각해 보고 반 친구들한테 의견을 이야기해 보세요.", "Think about the advantages and disadvantages of homeschooling and tell your classmates your opinion.")]
_TXT6 = [("Traditional textbooks (weakness)", "They are hard for students to study from by themselves; students turn away from them and rely on institute study, reference books and workbooks, and cram-style learning."), ("Electronic textbooks (merits)", "They are designed with various functions to make up for that weakness, so students can study autonomously; their core is interactive learning.")]
L4 = lesson(
    "U16 L6 · Part 2 (본 학습): homeschooling and electronic textbooks",
    "본 학습 · 홈스쿨링 · 전자교과서 · 대안교육 · 공교육 · 탈학교 · 튜터 · 한국튜터인증협회 · 반응식 학습 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): an interview with a professor who proposes homeschooling and electronic textbooks",
             "The following is a summary of an interview with a professor who proposed homeschooling and the use of electronic textbooks (© Kyunghyang). The text is the book’s with the numbers spelled out (1년 → 일 년; 5만여 명 → 오만여 명; 110만 명 → 백십만 명; 10% → 십 퍼센트; 20% → 이십 퍼센트; 1,000여 명 → 천여 명; 5만 명 → 오만 명), the middle dot in 참고서·문제집 written 참고서와 문제집, and the quotation marks removed. The interviewer’s questions are marked (Question) and the professor’s answers (Answer) in the English only. The English is mine.",
             examples=passage(_HOME)),
        card("학습활동 3: the questions answered (mine)",
             "1. Positive aspects of homeschooling: it can be an alternative for the students who fail to adapt to school education (about 50,000 a year leave it); in America, homeschooled students’ ability is evaluated as more than 10 percent ahead; it is increasing by 20 percent every year; and recently it is increasing for the sake of diversity and creativity in education.\n\n"
             "2. A parent interested in homeschooling can gather information from the courses for parents who want to do homeschooling and the educational program for training specialist tutors, such as those run by the Korea Tutor Certification Association, which created courses for training specialist homeschooling teachers and for homeschooling parents.\n\n"
             "3. The table:",
             tables=[table(["", "Summary (mine)"], [list(r) for r in _TXT6])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK6B)),
        card("Activities left out", "학습활동 1 (Listening, track 012): a middle school student speaking to adults about her thoughts (© Seoul Education Research & Information Institute): how she feels about going to a 학원 and why, what she wants her parents to do, and the speaker’s tone (A. mocking, B. cynical, C. sincere, D. resentful). 학습활동 2 (Listening, track 013): a voice letter from a mother whose daughter is entering high school (© edunet4u.net), with a table of how she changed her ideas before and after the talk, a summary of the daughter’s remarks, and what the mother thinks the daughter should do first. It is audio."),
    ],
    exercises=uniq(
        _tr(_HOME, k=3)
        + [M("What is homeschooling?", "Educating at home instead of at school", ["Studying at an institute", "Studying abroad", "Studying at night school"], "학교 대신 집에서 교육하는 방법."), M("How many Americans homeschool in a year (per the interview)?", "1.1 million", ["11,000", "110,000", "11 million"], "백십만 명."), M("How is homeschooled students’ ability evaluated?", "More than 10 percent ahead", ["Equal", "Behind", "Not measured"], "십 퍼센트 이상 앞선."), M("By how much does American homeschooling grow each year?", "20 percent", ["2 percent", "50 percent", "5 percent"], "이십 퍼센트."), M("Roughly how many Koreans homeschool at present?", "About 1,000", ["About 100,000", "About 10", "About 5 million"], "천여 명."), M("How many ‘out-of-school’ students are there in Korea each year?", "About 50,000", ["About 500", "About 5,000", "About 5 million"], "오만 명."), M("What is the Korea Tutor Certification Association?", "A body that trains homeschool tutors and runs courses for parents", ["A school", "A ministry", "A bank"], "한국튜터인증협회."), M("What is the core of the electronic textbook?", "Interactive learning", ["Memorization", "Games", "Lectures"], "반응식 학습."), M("What weakness of textbooks does the professor mention?", "It is hard for students to study by themselves", ["They are too expensive", "They are too short", "They are out of date"], "학생 스스로 공부하기 어렵다."),
           F("학교 대신 ___에서 교육하는 방법이다. (home)", "집", ["학원", "회사"], "집."), F("교과서가 학생에게 ___당하고 있다. (to be turned away from)", "외면", ["존중", "평가"], "외면당하다."), F("공교육에 대한 ___에서 비롯된 대안교육이다. (distrust)", "불신", ["신뢰", "관심"], "불신."), F("전자교과서의 핵심은 ___식 학습이다. (interactive)", "반응", ["주입", "일방"], "반응식."), F("홈스쿨링의 ___ 수요는 매우 크다. (potential)", "잠재적", ["현실적", "실질적"], "잠재적 수요."),
           read_q("홈스쿨링이란 학교 대신 집에서 교육하는 방법입니다"), read_q("공교육에 대한 불신에서 비롯되었습니다"), read_q("전자교과서의 핵심은 반응식 학습입니다"), read_q("홈스쿨링의 장점과 단점에 대해 생각해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("뒤처지다", "to lag behind", "결석을 많이 해서 공부가 많이 뒤처집니다."),
        ("무리(이)다", "to be too much; to be impossible", "숙제가 너무 많아서 오늘 저녁에 다 하는 것은 무리입니다."),
        ("북돋다", "to boost; to encourage; to cheer up", "저희 어머니는 항상 저의 자신감을 북돋아 주십니다.", "격려하다"),
        ("사려 깊다", "(思慮) to be considerate", "제 동생은 나이는 어리지만 저보다 훨씬 더 사려 깊어요."),
        ("어설프다", "to be clumsy", "새로 입사한 그 직원은 아직은 일하는 것이 어설픕니다."),
        ("역효과", "(逆效果) an opposite effect", "아이들을 너무 엄하게 대하면 오히려 역효과가 납니다."),
        ("입장", "(立場) one’s position; one’s situation", "이 문제에 대한 정부의 공식 입장은 무엇입니까?"),
        ("타율적", "(他律的) involuntary", "아이들이 타율적으로 공부하지 않고 자율적으로 공부하도록 도와줘야 합니다.", "자율적"),
    ]),
    ("학습활동 2", [
        ("대견(하다; 스럽다)", "to feel proud of (the subject of a sentence). This verb is rarely used when the person being spoken of is higher in social status than the speaker.", "이번에 장학금을 탄 우리 아들이 대견스럽습니다."),
        ("보람 (있다)", "worth; a sense of being rewarded (to be worthwhile)", "봉사활동은 힘들지만 보람 있는 일입니다."),
        ("확신(하다)", "(確信) conviction; confidence; assurance (to be sure; to be certain; to feel confident)", "저는 그 사람이 맞다고 확신합니다."),
    ]),
    ("학습활동 3", [
        ("고집(하다/스럽다)", "(固執) stubbornness; obstinacy (to insist; to persist/to be stubborn; to be obstinate)", "그 사람은 고집이 너무 세서 대화가 안 됩니다."),
        ("기반", "(基盤) a base; a foothold", "그 사람은 정치적 기반이 약해서 선거에 이길 수 없을 거예요.", "토대"),
        ("대안", "(代案) an alternative", "지금으로서는 대안이 없습니다."),
        ("맞물리다", "to mesh; to interlock; to interconnect; to interlink", "장수와 웰빙문화가 맞물려 있습니다."),
        ("문제집", "(問題集) a workbook", "교과서만으로 공부하기가 어렵습니다. 문제집을 한 권 사야겠어요.", "참고서, 교과서"),
        ("불신(하다)", "(不信) distrust; mistrust (to distrust; to mistrust)", "정치에 대한 국민들의 불신이 더 심해지고 있습니다.", "신뢰"),
        ("소외감", "(疏外感) a sense of alienation", "새로 전학간 학교에 친구가 없어서 소외감을 많이 느끼고 있습니다."),
        ("실태", "(實態) the actual condition; the true state; reality", "이 보고서는 우리나라 기업의 장애인 고용 실태에 대한 자세한 내용을 담고 있습니다."),
        ("외면하다", "(外面) to turn away from; to disregard; to turn one’s back on; to ignore", "정부는 이번 사건의 진실을 외면하고 있습니다.", "무시하다"),
        ("제고(하다)", "(提高) improving; enhancing (to improve; to enhance)", "기업이 생산성을 제고하기 위해 여러 가지 노력을 하고 있습니다."),
        ("(품)질", "(品質) quality (of a product)", "우리 회사 제품은 품질이 아주 좋습니다.", "양"),
        ("참고서", "(參考書) a reference book", "영어 성적이 많이 떨어졌어요. 영어 참고서를 하나 사야겠어요.", "문제집, 교과서"),
        ("창조성", "(創造性) creativity", "재미있는 작품을 쓰려면 창조성이 꼭 필요합니다."),
        ("취약하다", "(脆弱) to be weak; to be fragile; to be vulnerable", "이 지역은 홍수에 취약합니다."),
        ("포기(하다)", "(抛棄) abandonment; renunciation (to give up; to abandon; to renounce)", "그 사람은 무슨 일이든 쉽게 포기합니다."),
        ("홈스쿨링", "homeschooling", "요즘은 한국에서도 홈스쿨링을 하는 사람이 늘어나고 있습니다."),
        ("획일적", "(劃一的) uniform; monolithic; lockstep", "각기 다른 문제에 대해 획일적인 기준을 적용하면 안 됩니다."),
    ]),
]
L5 = lesson(
    "U16 L6 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 뒤처지다 · 무리 · 북돋다 · 사려 깊다 · 어설프다 · 역효과 · 타율적 · 대견하다 · 보람 · 확신 · 고집 · 기반 · 맞물리다 · 불신 · 소외감 · 실태 · 외면하다 · 제고 · 참고서 · 창조성 · 취약하다 · 획일적",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book the entry for 입장 is also in Lesson 5 with the same meaning; 대안 is also repeated in Part 3 of this lesson. The book’s example for 이 문제에 대한 정부의 공식 입장 has no other changes.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=22, nread=18)),
)

# ================================================================== L6 Part 3 texts
_INT = [
    ("공교육과 비교해 어떤 점이 매력이었나요?", "(Question 1) Compared with public education, what was the attraction?"),
    ("입시 스트레스로부터 자유롭다는 점이 크게 다가왔어요.", "(Answer) The point that it is free from entrance-exam stress struck me greatly."),
    ("일반 중학교와 고등학교 과정은 대학 입시에 초점이 맞춰져 있다는 게 가장 큰 단점이죠.", "The biggest drawback of the regular middle and high school course is that it is focused on the college entrance exam."),
    ("공부 잘하는 아이들, 상위 오 퍼센트 이내에서 입시 경쟁이 이루어지고 나머지 아이들은 사실상 방치되고 있어요.", "The entrance-exam competition takes place among the children who study well, within the top 5 percent, and the rest of the children are in effect being neglected."),
    ("대안학교가 생긴 지 십 년 됐습니다.", "(Question 2) It has been ten years since alternative schools came into being."),
    ("여전히 풀어야 할 숙제가 있다면 무엇일까요?", "If there is still a homework to solve, what would it be?"),
    ("법인화 제도에 대한 문제겠죠.", "(Answer) It would be the problem of the incorporation system."),
    ("대부분의 미인가 대안학교는 정부나 지자체로부터 재정적 지원을 받지 못하고 굉장히 열악한 상황이에요.", "Most unapproved alternative schools cannot receive financial support from the government or local governments and are in a very poor situation."),
    ("우리가 일상생활에서 지불하는 교육세가 미인가 학교에는 가지 않고 있어요.", "The education tax that we pay in daily life does not go to unapproved schools."),
    ("대안학교 입학을 고민 중인 아이와 학부모에게 어떤 조언을 해 주고 싶으신가요?", "(Question 3) What advice would you like to give to children and parents who are considering entering an alternative school?"),
    ("아이가 재밌고 즐겁게 인생 공부를 한다고 생각하고 부모가 아이들 교육에 좀 더 열린 마음을 가졌으면 좋겠어요.", "(Answer) I would like them to think that the child studies life happily and enjoyably, and I wish parents would have a somewhat more open mind about the children’s education."),
    ("또 너무 피상적으로 접근하지 말고 일 년 정도 알아보고 오시라고 말씀드리고 싶어요.", "Also, I would like to say, do not approach it too superficially; look into it for about a year and then come."),
    ("너무 급하게 결정하면 힘들 수 있어요.", "If you decide too hastily, it can be hard."),
    ("왔다가 떠나더라도 그게 좋은 경험과 에너지가 될 수 있어요.", "Even if you come and then leave, that can become a good experience and energy."),
    ("그게 또 대안학교의 역할이라고 생각하고요.", "And I think that is also the role of an alternative school."),
]
_PAR = [
    ("중학교 이 학년 아들아이가 있다.", "I have a son in the second year of middle school."),
    ("만 팔 년 공교육을 받는 동안, 아이가 가진 단점은 더 커지고 장점은 갈수록 사그라지는 모습을 가슴 아프게 지켜보았다.", "During the full eight years of public education, I watched with a heavy heart as the child’s weaknesses grew bigger and his strengths faded more and more."),
    ("고민 끝에 내년에 전인교육을 지향하는 대안학교에 입학하고자 수속을 밟는 중이다.", "After agonizing, I am going through the procedures to enter an alternative school that aims at well-rounded education next year."),
    ("의무교육이 구 년인 현행법상 중학교까진 대안학교를 인정하는 법령이 없어서, 아이는 출석부상에 유령 학생으로 남아 있고, 학교에선 사고결석 처리를 해야만 한다.", "Under the current law, in which compulsory education is nine years, there is no statute recognizing alternative schools up to middle school, so the child remains on the attendance book as a ghost student, and the school has to process it as an absence due to an accident."),
    ("대안학교가 학력 인정이 되지 않은 탓에 학부모와 학교 모두 찜찜하고 번거로운 형식을 취해야만 하는 것이다.", "Because alternative schools are not recognized for academic credentials, both parents and school have to take an uncomfortable and cumbersome form."),
    ("안병영 교육부총리가 대안학교를 지원하겠다는 성명을 발표했다.", "Deputy Prime Minister for Education An Byeong-yeong announced a statement that he would support alternative schools."),
    ("초등학교와 중학교 대안학교가 학력 인정이 되지 않는 현행 제도를 개선하겠다고 했다.", "He said he would improve the current system in which elementary and middle school alternative schools are not recognized for academic credentials."),
    ("현재 대안학교에 아이를 보내고 있거나, 그럴 의향이 있는 학부모에겐 반가운 소식이다.", "It is welcome news for parents who are currently sending a child to an alternative school or intend to."),
    ("그런데도 아직 교육 공무원들은 대안교육을 공교육의 적으로 경계하는 근시안적 사고에 머물러 있는 경우가 많다.", "Even so, education officials often still remain in a shortsighted way of thinking, being wary of alternative education as the enemy of public education."),
    ("대안학교의 가장 큰 어려움은 재정 부문이다.", "The biggest difficulty of alternative schools is the financial side."),
    ("아이들을 교육하기 위해 많은 돈이 드는 건 기정사실임에도, 학교 육성 기금에 해당하는 기여금에 대해 마치 부정한 뇌물인 양 보도하기도 한다.", "Although it is an established fact that educating children costs a lot of money, the press even reports the contributions, which correspond to a school development fund, as if they were an unlawful bribe."),
    ("참된 교육에 대한 목마름과 현재의 교육에 대한 대안을 갈망하는 이들이 모여 주머닛돈 모아 학교를 세우고자 하는 의지가 포함된 대안학교도 있음을 간과한 채 말이다.", "And this while overlooking that there are also alternative schools that include the will of those thirsting for true education and longing for an alternative to present education, gathering together and pooling their pocket money to set up a school."),
    ("공교육 구조에 적응하지 못하고 일탈한 학생은 해마다 수천 명이 된다고 한다.", "They say that students who fail to adapt to the public education structure and break away number several thousand every year."),
    ("공교육 자체 안에서 올바른 교육의 미래에 대한 청사진을 제시하는 것이 현실적으로 힘들다면, 공교육 밖의 다양한 움직임에 한번 귀를 기울여 보는 것은 어떨까?", "If it is realistically hard to present a blueprint for the future of right education within public education itself, how about listening for once to the various movements outside public education?"),
    ("대안교육을 진정한 교육의 파트너로 받아들일 때 우리나라는 교육에 대한 모든 국민의 뜨거운 관심과 열망에 걸맞은 교육대국이 될 수 있을 것이다.", "When we accept alternative education as a true partner of education, our country will be able to become an education powerhouse that fits the hot interest and desire of all the people for education."),
]
_SPEAK6C = [("대안교육에 대해 찬성하는지 반대하는지 자신의 의견과 그 이유에 대해 반 친구들과 이야기해 보세요.", "Tell your classmates whether you are for or against alternative education, and your opinion and the reasons for it.")]
_MAT6 = [("1", "입시 스트레스로부터 자유롭다는 점이 크게 다가왔어요 … 상위 오 퍼센트 이내에서 입시 경쟁이 이루어지고 나머지 아이들은 사실상 방치되고 있어요.", "Free from entrance-exam stress; the regular course is focused on the college entrance exam"), ("2", "법인화 제도에 대한 문제겠죠 … 교육세가 미인가 학교에는 가지 않고 있어요.", "The incorporation system: unapproved schools get no financial support or education tax"), ("3", "아이가 재밌고 즐겁게 인생 공부를 한다고 생각하고 … 일 년 정도 알아보고 오시라고 말씀드리고 싶어요.", "Open mind; do not approach superficially; look into it for about a year")]
_UND6 = [("찜찜하고 번거로운 형식", "Alternative schools are not credited as schools up to middle school, so the child stays on the attendance book as a “ghost student” and the school has to process the absence as an accident-related absence; both parents and school have to go through an awkward, cumbersome formality."), ("근시안적 사고", "Education officials often still see alternative education as the “enemy of public education” and the press even reports the contributions as if they were bribes, overlooking that some schools are set up by people pooling their own pocket money for true education.")]
L6 = lesson(
    "U16 L6 · Part 3 (심화 학습): alternative schools",
    "심화 학습 · 대안학교 · 공교육 · 미인가 · 법인화 · 전인교육 · 학력 인정 · 기여금 · 근시안적 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 대안학교 (alternative school) — the book’s note",
             "In an effort to cope with the troubled public education system, alternative schools known as 대안학교 were created in the 1990s. A 대안학교 is an educational establishment that uses a nontraditional curriculum and methodology. Despite differing philosophies and teaching methods in every alternative school, each emphasizes a well-rounded education and offers a more flexible program than what is typically found in a traditional school."),
        card("학습활동 1 (Reading): an interview with a mother whose child attends an alternative school",
             "The following is an interview with a mother whose child attends an alternative school (© Kyunghyang). In the book the questions are on the left and the answers are in a jumbled order on the right; you read and write the number of the matching question on the line of each answer. Here each question is followed by its answer. The text is the book’s with the numbers spelled out (10년 → 십 년; 5% → 오 퍼센트; 1년 → 일 년) and the middle dots in 중·고등학교 written 중학교와 고등학교. The English is mine.",
             examples=passage(_INT)),
        card("학습활동 1: the matching answered (mine)",
             "In the book the three answers are printed in this order: the first (the incorporation system) goes with question 2, the second (the open-mind advice) goes with question 3 and the third (free from entrance-exam stress) goes with question 1. The question numbers are not printed in the text; I number them in the order printed. So the numbers to write on the three lines are 2, 3 and 1.",
             tables=[table(["Question", "Answer (beginning), summary"], [[r[0], r[1]] for r in _MAT6], say=[1])]),
        card("학습활동 3 (Reading): a parent’s newspaper contribution",
             "The following is a piece contributed to a newspaper by the parent of a child who attends an alternative school (© Hankyoreh). The text is the book’s with the numbers spelled out (중2 → 중학교 이 학년; 만 8년 → 만 팔 년; 9년 → 구 년), the middle dot in 초·중 written 초등학교와 중학교, and the quotation marks ‘ ’ removed. The English is mine.",
             examples=passage(_PAR)),
        card("학습활동 3: the questions answered (mine)",
             "1. The author watched, through eight years of public education, the child’s weaknesses grow bigger and his strengths fade, and after agonizing decided to enter him next year in an alternative school that aims at well-rounded education.\n\n"
             "2. B — Mainstream education should accept alternative education as a partner (the last paragraph asks the reader to listen to the movements outside public education and to accept alternative education as a true partner).\n\n"
             "3. The two underlined phrases are not marked in the text; the phrases the book underlines look like the two printed with a gap before them (찜찜하고 번거로운 형식 in paragraph 1 and 근시안적 사고 in paragraph 2), so the best guesses are:",
             tables=[table(["Phrase", "Summary (mine)"], [list(r) for r in _UND6])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK6C)),
        card("Activities left out", "학습활동 2 (Listening and Writing, track 014): an editorial on the illiteracy rate (© Donga) with a main-point question (A. to urge the government to design a better test for measuring reading ability; B. to praise parents for their devotion to improving their children’s reading ability; C. to determine the causes of poor reading ability; D. to urge people to increase their reading ability), questions on how reading level was measured, the meaning of 실질적인 문맹률, what triggered the sharp decrease in illiteracy, and a written answer in Korean on how to reduce the real illiteracy rate. It is audio."),
    ],
    exercises=uniq(
        _tr(_INT, k=3) + _tr(_PAR, k=3) + [M("In which decade were alternative schools created in Korea?", "The 1990s", ["The 1960s", "The 1970s", "The 2010s"], "The book’s note."), M("What does a 대안학교 use?", "A nontraditional curriculum and methodology", ["A strict military curriculum", "Only online lessons", "Only textbooks"], "The book’s note."), M("What do all alternative schools emphasize?", "A well-rounded education", ["Test scores", "Sports only", "Foreign languages only"], "The book’s note."),
           M("What attracted the mother to the alternative school?", "Being free from entrance-exam stress", ["The low tuition", "The short school day", "The sports teams"], "입시 스트레스로부터 자유롭다."), M("What is the biggest drawback of regular middle and high school courses, according to the mother?", "They are focused on the college entrance exam", ["They are too short", "They are too easy", "They have no teachers"], "대학 입시에 초점."), M("What is the problem the mother mentions for unapproved alternative schools?", "They cannot receive financial support", ["They have too many students", "They have no teachers", "They are too large"], "재정적 지원."), M("What does the mother advise about deciding?", "Look into it for about a year before deciding", ["Decide as quickly as possible", "Never come", "Ask nobody"], "일 년 정도 알아보고."),
           M("Why does the author’s son stay on the attendance book as a ghost student?", "No law recognizes alternative schools up to middle school", ["He never attended", "He is a foreigner", "He is too young"], "법령이 없어서."), M("How many years is compulsory education here?", "Nine years", ["Six years", "Twelve years", "Three years"], "구 년."),
           F("대안학교를 ___으로 경계하는 사람들이 있다. (the enemy)", "적", ["친구", "손님"], "공교육의 적."), F("학생은 출석부상에 ___ 학생으로 남아 있다. (ghost)", "유령", ["신입", "우수"], "유령 학생."), F("기여금을 마치 부정한 ___인 양 보도하기도 한다. (bribe)", "뇌물", ["선물", "예산"], "뇌물."), F("대안학교는 ___교육을 지향한다. (well-rounded)", "전인", ["입시", "주입식"], "전인교육."), F("공교육 밖의 다양한 움직임에 ___를 기울여 보자. (ear)", "귀", ["눈", "손"], "귀를 기울이다.")]
        + [read_q("대안학교가 생긴 지 십 년 됐습니다"), read_q("입시 스트레스로부터 자유롭습니다"), read_q("대안교육을 교육의 파트너로 받아들여야 합니다"), read_q("대안교육에 대해 찬성하십니까 반대하십니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("공교육", "(公敎育) public education", "공교육이 무너졌다고 우려하는 목소리가 높습니다.", "사교육"),
        ("대안", "(代案) an alternative", "무너진 공교육에 대한 대안이 있습니까?", "방안"),
        ("매력", "(魅力) charm; appeal; attraction", "그 사람은 아주 매력이 있어요."),
        ("미인가", "(未認可) not officially approved", "이 학교는 정식인가를 받은 학교입니다.", "승인"),
        ("방치(하다/되다)", "(放置) leaving a thing or person as it is; negligence (to leave a thing or person as it is/to be neglected)", "가출 청소년들을 그대로 방치하면 안 됩니다."),
        ("법인화(하다/되다)", "(法人化) incorporating a business entity or school (to incorporate/to be incorporated)", "최근 몇몇 국립대학이 법인화하려는 움직임을 보이고 있습니다."),
        ("상위", "(上位) top; “higher place”", "세계 경제의 상위 다섯 개국이 어떤 나라들입니까?", "하위"),
        ("열악하다", "(劣惡) to be poor; to be inadequate; to be deteriorated", "열악한 경제상황으로 인해 기업이 수익을 내지 못하고 있습니다."),
        ("자유롭다", "(自由) to be free; to be unrestricted", "우리 회사는 출퇴근 시간이 자유롭습니다."),
        ("초점", "(焦點) focus; a focal point", "카메라의 초점이 맞지 않습니다."),
        ("피상적", "(皮相的) superficial; shallow", "논의가 너무 피상적으로 이루어져서 결론을 내리기가 힘듭니다."),
    ]),
    ("학습활동 2", [
        ("교육열", "(敎育熱) zeal for education; enthusiasm for education", "한국의 부모들은 일반적으로 교육열이 높습니다."),
        ("기적", "(奇蹟) a miracle", "그 사람은 화재 현장에서 기적적으로 구조되었습니다."),
        ("눈을 돌리다", "to pay attention to; “to turn an eye to”", "이제 우리도 환경문제에 눈을 돌려야 합니다.", "관심을 갖다"),
        ("만점", "(滿點) a perfect score; “full point”", "저는 수학은 만점을 받았는데 영어는 잘 못 했어요."),
        ("매체", "(媒體) a medium; media", "요즘은 대중매체가 발달되어 실시간으로 뉴스가 보도됩니다.", "대중매체"),
        ("문맹률", "(文盲率) illiteracy rate", "아프리카 지역의 문맹률이 높습니다."),
        ("미흡하다", "(未洽) to be insufficient; to be unsatisfactory", "교육부는 사교육 대책을 발표했지만, 미흡한 점이 많습니다."),
        ("서러움", "sorrow; sadness", "저는 부모님이 안 계셔서 서러움을 많이 겪었습니다.", "서럽다"),
        ("쇠퇴(하다)", "(衰退) declining; deterioration; dwindling (to decline; to deteriorate; to dwindle)", "작년부터 아버지 사업이 쇠퇴하기 시작했어요."),
        ("실질적", "(實質的) actual; real; practical", "이번 회담은 실질적인 성과가 없습니다."),
    ]),
    ("학습활동 3", [
        ("간과하다", "(看過) to overlook; to fail to notice", "이 제안은 한 가지 중요한 점을 간과하고 있습니다."),
        ("갈망(하다)", "(渴望) longing for; yearning for (to long for; to yearn for)", "제 친구는 유학을 갈망하고 있습니다.", "열망"),
        ("걸맞다", "to be suitable for; to be a fit for; to be commensurate with", "나이에 걸맞은 행동을 하세요.", "알맞다"),
        ("귀를 기울이다", "to listen carefully; to give careful attention to; “to lean one’s ear”", "다른 사람의 의견에도 귀를 기울이세요.", "주의를 기울이다"),
        ("근시안적(이다)", "(近視眼的) (to be) shortsighted; (to be) myopic", "정부가 발표한 정책은 근시안적인 정책입니다."),
        ("기여금", "(寄與金) monetary contribution", "이 학교는 부모가 낸 기여금으로 지어졌습니다.", "기부금"),
        ("기정사실", "(旣定事實) an established fact; a fixed fact", "이제 금융위기를 기정사실로 받아들이고 대책을 마련해야 합니다."),
        ("뇌물", "(賂物) a bribe", "공무원들이 뇌물을 받은 것으로 드러났습니다."),
        ("번거롭다", "to be cumbersome; to be inconvenient", "이 기계는 성능은 좋지만 작동이 어려워서 쓰기가 번거롭습니다.", "불편하다"),
        ("부정(하다)", "(不正) illegality; dishonesty; “not right” (to be unlawful; to be dishonest)", "얼마 전 치러진 선거가 부정선거였다는 주장을 하는 사람들이 있습니다.", "부정부패, 부정입학, 부정선거"),
        ("사그라지다/사그라들다", "to die down; to subside", "처음에는 화가 많이 났지만, 시간이 지나면서 화가 사그라졌습니다.", "수그러지다/수그러들다"),
        ("성명", "(聲明) a statement; an announcement", "이번 사건에 대해 아직 정부가 공식 성명을 발표하지 않았습니다."),
        ("열망(하다)", "(熱望) a strong desire; strong wish (to long for; to desire)", "그 사람들은 자유를 열망하며 탈출을 시도했습니다.", "갈망하다"),
        ("유령", "(幽靈) a ghost; a specter", "이 집은 유령이 나온다고 합니다."),
        ("의향", "(意向) intention", "저는 이번 선거에 출마할 의향이 없습니다.", "의도"),
        ("일탈(하다)", "(逸脫) deviation from; breaking away (to deviate from)", "저는 가끔 일상에서 일탈하고 싶습니다.", "벗어나다"),
        ("적", "(敵) an enemy", "흰 쌀밥은 다이어트의 적입니다."),
        ("전인교육", "(全人敎育) well-rounded education; “whole-person education”", "성적만을 강요하는 교육이 아니라 전인교육을 강화하려는 움직임이 있습니다."),
        ("주머닛돈", "(small amount of) pocket money; “pocket money”", "학부모들이 주머닛돈을 모아 가난한 아이들을 위해 장학금을 마련했습니다.", "푼돈, 쌈짓돈"),
        ("지향(하다)", "(志向) aim (to aim; to pursue)", "이 학교는 전인교육을 지향합니다."),
        ("찜찜하다", "to feel uncomfortable; to be leery", "어젯밤에 숙제를 다 하지 못하고 잠을 자서 기분이 찜찜했습니다."),
        ("참되다", "to be true; to be genuine; to be sincere; to be faithful", "저는 참되게 살려고 노력하고 있어요."),
        ("청사진", "(靑寫眞) a blueprint", "미래의 청사진을 제시해 주세요."),
        ("출석부", "(出席簿) an attendance book; a roll book", "학생 이름이 출석부에 다 올라가 있습니까?"),
        ("현행", "(現行) existing; currently under practice", "정부는 경범죄에 대한 벌금을 현행 십만 원에서 이십만 원으로 올렸습니다."),
        ("형식", "(形式) formality; a form", "저는 형식을 너무 따지고 싶지는 않아요.", "내용"),
    ]),
]
L7 = lesson(
    "U16 L6 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 공교육 · 대안 · 매력 · 미인가 · 방치 · 법인화 · 열악하다 · 초점 · 피상적 · 교육열 · 문맹률 · 미흡하다 · 실질적 · 간과하다 · 갈망 · 걸맞다 · 기여금 · 뇌물 · 번거롭다 · 유령 · 전인교육 · 지향 · 청사진 · 출석부",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives two extra notes under this list: 부정 (不正) “illegality; dishonesty” is not the 부정 (否定) “denial”; and 성명 (聲明) “a statement; an announcement” is not the 성명 (姓名) “a full name”. The book’s examples 상위 5개국 and 10만 원에서 20만 원으로 are written 상위 다섯 개국 and 십만 원에서 이십만 원으로. 대안 and 귀를 기울이다 are repeated from earlier lessons.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=30, nread=24)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 6: Alternative Schools and Adult Education (대안 학교 및 평생 교육)", [L1, L2, L3, L4, L5, L6, L7])
