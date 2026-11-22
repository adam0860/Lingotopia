"""Unit 69: KBC Semester III, Unit 16, Lesson 4 - College Entrance Examination (대학입시).
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
_OPP4 = [("결석", "출석", "absence: attendance"), ("불합격", "합격", "failing: passing"), ("인문계", "실업계", "the academic (liberal arts) track: the vocational track"), ("졸업", "입학", "graduation: entering school"), ("반대", "찬성", "opposition: agreement"), ("칭찬", "벌", "praise: punishment"), ("학기", "방학", "a school term: a school vacation")]
_BOX4 = [("과외", "private tutoring; extracurricular activity"), ("급식", "school meals; a school lunch"), ("성적표", "a report card"), ("시간표", "a timetable; a schedule"), ("의무교육", "compulsory education"), ("체육", "physical education"), ("학비", "school expenses; tuition")]
_HJ4 = [("點 점", "point; spot", "학점, 만점"), ("數 수", "number", "수학, 수치"), ("立 립", "establish", "공립, 사립"), ("生 생", "life; birth", "생일, 생사"), ("學 학", "study; learn", "학교, 학년")]
_HJW4 = [("학점", "a credit; a grade"), ("만점", "full credit"), ("수학", "mathematics"), ("수치", "a numerical value"), ("공립", "public (institution)"), ("사립", "private (institution)"), ("생일", "a birthday"), ("생사", "life and death"), ("학교", "a school (institution)"), ("학년", "a grade; “school year”")]
_OPP4B = [("단점", "장점", "a weak point: a strong point"), ("사립", "공립", "private: public"), ("휴학", "복학", "taking a leave of absence: returning to school"), ("학생", "선생", "a student: a teacher"), ("복수", "단수", "plural: singular")]
_ODD4 = [("A", "어학", "취학, 진학, 퇴학", "어학 is language study; the others are about entering, advancing or leaving school"), ("B", "동생", "유학생, 신입생, 졸업생", "동생 is a younger sibling; the others are kinds of students"), ("C", "수수료", "과목, 성적, 점수", "수수료 is a fee; the others are about schoolwork and grades"), ("D", "보증금", "등록금, 학비, 수업료", "보증금 is a deposit; the others are school fees")]
_L4X = [("장점", "a strong point"), ("단점", "a weak point"), ("점수", "a score"), ("복학", "returning to school"), ("퇴학", "dropping out; expulsion"), ("휴학", "a leave of absence from school"), ("신입생", "a new student"), ("유학생", "a student studying abroad"), ("졸업생", "a graduate"), ("취학", "starting school"), ("진학", "going on to a higher school"), ("어학", "language study"), ("과목", "a subject"), ("성적", "grades; results"), ("수수료", "a service charge; a fee"), ("등록금", "a registration fee"), ("수업료", "tuition"), ("보증금", "a deposit"), ("단수", "singular"), ("복수", "plural"), ("독립", "independence"), ("건립", "erecting; founding"), ("등수", "a rank (place)")]
L1 = lesson(
    "U16 L4 · Review: school words and Sino-Korean 點 數 立 生 學",
    "대학입시 · 단어 복습 · 한자어 복습 · 결석 · 출석 · 입학 · 졸업 · 인문계 · 실업계 · 과외 · 급식 · 성적표 · 의무교육 · 學 點 數 立 生",
    requires=[],
    cards=[
        card("단어 복습 1: the opposites", "The book asks you to connect each word on the left with the word of opposite or contrasting meaning on the right. The pairs:", tables=[table(["Word", "Opposite", "Meaning"], [list(r) for r in _OPP4], say=[0, 1])]),
        card("단어 복습 2: the words of the box", "The book plays seven descriptions (tracks 001 to 007) and asks you to choose the matching word from the box. The listening is audio and is left out; the seven words of the box, with my meanings, are:", tables=[ktable(_BOX4)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ4], say=[2]), ktable(_HJW4)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 단점: 학점, 점수, 장점; B. 사립: 독립, 공립, 건립; C. 휴학: 복학, 퇴학, 입학; D. 학생: 선생, 신입생, 유학생; E. 복수: 점수, 단수, 등수).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP4B], say=[0, 1])]),
        card("한자어 복습 2: the odd word out (my answers)", "In each group of four words, circle the one whose character differs from the other three. My answers:", tables=[table(["", "Odd one (my answer)", "The other three", "Why"], [list(r) for r in _ODD4], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L4X)]),
    ],
    exercises=uniq(
        _tr(_BOX4, k=3) + _tr(_HJW4, k=3) + _tr(_L4X, k=3) + _tr([(a, c) for a, b, c in _OPP4], k=3)
        + [M("What does the syllable 點 (점) mean?", "point; spot", ["number", "establish", "life"], "학점."), M("What does the syllable 數 (수) mean?", "number", ["point", "establish", "study"], "수학."), M("What does the syllable 立 (립) mean?", "establish", ["point", "number", "life"], "공립."), M("What does the syllable 生 (생) mean?", "life; birth", ["point", "number", "study"], "생일."), M("What does the syllable 學 (학) mean?", "study; learn", ["point", "number", "establish"], "학교."),
           M("Which word is the opposite of 결석?", "출석", ["합격", "입학", "찬성"], "Attendance."), M("Which word is the opposite of 졸업?", "입학", ["출석", "방학", "합격"], "Entering school."), M("Which word is the opposite of 학기?", "방학", ["벌", "찬성", "합격"], "A vacation."), M("Which word is the opposite of 사립?", "공립", ["독립", "건립", "자립"], "Public."), M("Which word is the opposite of 휴학?", "복학", ["퇴학", "입학", "졸업"], "Returning to school."), M("Which word is the opposite of 복수?", "단수", ["점수", "등수", "횟수"], "Singular."),
           M("Which word does not fit 취학, 진학, 퇴학?", "어학", ["입학", "복학", "졸업"], "Language study."), M("Which word does not fit 유학생, 신입생, 졸업생?", "동생", ["학생", "대학생", "선배"], "A younger sibling."), M("Which word does not fit 등록금, 학비, 수업료?", "보증금", ["입학금", "장학금", "학자금"], "A deposit."),
           F("그 학생은 시험에서 ___을 받았습니다. (full credit)", "만점", ["학점", "수치"], "만점."), F("저는 ___학교에 다니고 있습니다. (public)", "공립", ["사립", "독립"], "공립."), F("올해 ___이 되어 신나요. (new student)", "신입생", ["졸업생", "유학생"], "신입생."), F("건강이 나빠져서 ___을 했습니다. (leave of absence)", "휴학", ["복학", "입학"], "휴학."), F("우리 학교는 ___ 학교입니다. (private)", "사립", ["공립", "국립"], "사립."),
           read_q("그 학생은 시험에서 만점을 받았습니다"), read_q("올해 대학교에 입학했습니다"), read_q("공립 학교와 사립 학교가 있습니다"), read_q("휴학을 하고 복학을 했습니다"), read_q("성적표를 받았습니다")]
    ),
)

# ================================================================== L2 Part 1
_ADM = [
    ("지난 이천칠 년 정부 지원으로 시행된 입학사정관제.", "The admissions officer system, carried out with government support in 2007."),
    ("이천십 학년도 대학 수시 전형에서 전국 팔십칠 개 대학이 전체 모집인원의 십 퍼센트를 이 제도를 통해 선발했다.", "In the college rolling admission screening for the 2010 academic year, 87 colleges nationwide selected 10 percent of the total number of recruits through this system."),
    ("지금까지 대학은 학생부나 수능시험, 대학별고사 등 성적 위주로 학생을 선발해 왔다.", "Until now colleges have selected students mainly on grades, such as the school record, the college scholastic ability test and each college’s own exam."),
    ("그 결과 초 중등학교에서는 지나친 점수 위주의 경쟁이 일어나게 되었고, 대학에서는 각 전공에 맞는 잠재력과 소질을 가진 학생을 선발하는 데 한계가 있었다.", "As a result, excessive score-centered competition arose in elementary and secondary schools, and in colleges there were limits in selecting students with the potential and aptitude suited to each major."),
    ("이러한 점을 극복하고자 시행된 입학사정관제.", "The admissions officer system, enforced to overcome these points."),
    ("교육과학기술부는 입학사정관제는 대학이 고등학교 교육과정, 대학의 학생 선발 방법 등에 대한 전문가를 채용하고, 이들을 활용해 학생의 성적, 개인 환경, 잠재력 및 소질 등을 종합적으로 판단해 신입생을 선발하는 제도를 의미한다고 밝힌다.", "The Ministry of Education, Science and Technology states that the admissions officer system means a system in which a college hires experts on the high school curriculum, the college’s student selection methods and so on, and uses them to judge students’ grades, personal circumstances, potential, aptitude and so on comprehensively to select new students."),
    ("이 제도의 궁극적인 목적은 당장의 점수 차이보다는 대학 입학 후 발휘할 학생들의 잠재능력을 중시해 학생을 선발하는 데 있다.", "The ultimate purpose of this system is to select students by valuing the potential ability that students will show after entering college rather than immediate differences in score."),
    ("일 단계 사전공지: 지원자격, 선발기준, 선발방법, 제출서류 안내.", "Step 1, advance notice: guidance on eligibility to apply, selection criteria, selection methods and documents to submit."),
    ("이 단계 서류심사와 자격심사: 학교생활기록부, 자기소개서, 추천서, 수능성적 제출.", "Step 2, document screening and qualification screening: submission of the school life record, a self-introduction, recommendation letters and the college scholastic ability test results."),
    ("삼 단계 심층면접과 토론: 잠재력, 창의성, 소질, 인성 및 적성 파악, 교육환경 조사.", "Step 3, in-depth interview and discussion: grasping potential, creativity, talent, character and aptitude, and a survey of the educational environment."),
    ("사 단계 최종선발: 합격자 결정.", "Step 4, final selection: deciding the successful applicants."),
]
_SPEAK4 = [("미국 중고등학교의 과외활동에 대해서 이야기해 보세요.", "Talk about extracurricular activities at American middle and high schools."), ("북한의 교육에 대해서 아는 것을 서로 이야기해 보세요.", "Tell each other what you know about education in North Korea.")]
_SENT4 = [("현 정부의 교육정책 기조는 자율과 경쟁입니다.", "The basis of the present government’s education policy is “autonomy and competition.”"), ("내년부터 서울에서는 고교선택제가 실시됩니다.", "From next year a high school choice system will be implemented in Seoul."), ("학교 자율화도 시행됩니다.", "The autonomy of schools will also be carried out.")]
L2 = lesson(
    "U16 L4 · Part 1 (도입 학습): the admissions officer system",
    "도입 학습 · 입학사정관 · 정시 모집 · 수시 모집 · 입학사정관제 · 남북한 교육체계 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 1: 입학사정관 (admissions officers) — the book’s note",
             "In the past, selection of students for admission to college in Korea was based primarily on entrance exam results. However, colleges have recently been moving to 입학사정관제 (an admission process system) similar to the American system. Colleges screen students according to a “whole person” concept that includes test scores, secondary school GPAs, volunteer work, talents, and other criteria. (Image © Kyunghyang.)"),
        card("알아봅시다 2: 정시 모집 and 수시 모집 — the book’s note",
             "Every winter, a few months before the academic year starts in March, colleges and universities in Korea recruit most of their students. This regular fixed-time recruitment is known as 정시 모집. Colleges and universities also frequently recruit a small number of students throughout the academic year. This frequent recruitment is known as 수시 모집."),
        card("학습활동 4 (Reading): a magazine article on the admissions officer system",
             "The following is a magazine article on education (Text and images © Kyunghyang), headed 정보가 힘이다! ‘입학사정관제’로 대학 가기 (Information is power! Going to college by the “admissions officer system”). The text is the book’s with the numbers spelled out (2007년 → 이천칠 년; 2010학년도 → 이천십 학년도; 87개 → 팔십칠 개; 10% → 십 퍼센트; 1단계 → 일 단계 and so on); the middle dot · is written as 와 or removed and the quotation marks ‘ ’ are removed. The English is mine.",
             examples=passage(_ADM)),
        card("학습활동 4: the questions answered (mine)",
             "1. The Ministry of Education adopted the new system to overcome the problems of selecting students mainly by grades: excessive score-centered competition in elementary and secondary schools, and colleges’ limit in selecting students with the potential and aptitude suited to each major. Its ultimate purpose is to select students by valuing the potential ability they will show after entering college rather than the immediate differences in score.\n\n"
             "2. The meaning (the sentence the Ministry gives, which I take to be underlined): “입학사정관제는 대학이 고등학교 교육과정, 대학의 학생 선발 방법 등에 대한 전문가를 채용하고, 이들을 활용해 학생의 성적, 개인 환경, 잠재력 및 소질 등을 종합적으로 판단해 신입생을 선발하는 제도를 의미한다.” — The admissions officer system means a system in which a college hires experts on the high school curriculum, the college’s student selection methods and so on, and uses them to judge students’ grades, personal circumstances, potential and aptitude comprehensively to select new students.\n\n"
             "3. Step 1: Furnish information in advance — colleges provide information regarding eligibility, selection criteria, selection methods and documents to be submitted. Step 2: Document and qualification screening — students submit school records, personal essays, recommendations and entrance exam scores. Step 3: Interview and in-depth discussion — colleges evaluate students’ potential, creativity, talent, personality, aptitude and educational background. Step 4: Final selection — colleges select the students to be accepted for admission."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK4)),
        card("Activities left out", "학습활동 1 (Reading): a table comparing the education systems of South and North Korea (© edunet4u.net), with four statements to check (that South Korea has a longer period for elementary school; that North Korea has a combined secondary school while South Korea separates middle and high school; and which country’s students begin secondary and post-secondary education at an earlier age). The table is a picture. 학습활동 2 (Video, track 008): a public-interest ad from an education site — which jobs are mentioned (teacher, computer researcher, hotel cook, professor, documentary director, choreographer) and which word replaces “땀” (sweat; among 시험, 노력, 고민, 눈물). 학습활동 3 (Video, tracks 009 and 010): scenes from the drama “Unstoppable High Kick” (지붕 뚫고 하이킥), on a celebration, the son’s reaction, a competition and its award ceremony."),
    ],
    exercises=uniq(
        _tr(_ADM, k=3) + _tr(_SENT4, k=2) + _tr(_SPEAK4, k=2)
        + [M("When was the admissions officer system first carried out?", "2007", ["1997", "2017", "1987"], "이천칠 년."), M("How many colleges used it in the 2010 rolling admission?", "87", ["8", "187", "27"], "팔십칠 개."), M("What share of recruits did they select through it?", "10 percent", ["1 percent", "50 percent", "90 percent"], "십 퍼센트."), M("What did colleges mainly select on before?", "Grades", ["Looks", "Age", "Hobbies"], "성적 위주."), M("What does the system value more than immediate scores?", "Potential ability after entering college", ["Family wealth", "Age", "Sports"], "잠재능력."), M("How many steps are there?", "Four", ["Two", "Seven", "One"], "사 단계."), M("What happens in step 3?", "In-depth interview and discussion", ["Document screening", "Final selection", "Advance notice"], "심층면접과 토론."), M("What is submitted in step 2?", "School records, a self-introduction, recommendations, test scores", ["Only a photo", "Only an exam", "Only fees"], "서류심사."),
           F("입학사정관제는 학생의 ___을 중시한다. (potential)", "잠재력", ["점수", "나이"], "잠재력."), F("지금까지 대학은 ___ 위주로 학생을 선발했다. (grades)", "성적", ["소질", "인성"], "성적."), F("서류심사에서는 ___를 제출한다. (a recommendation letter)", "추천서", ["합격증", "영수증"], "추천서."), F("마지막 단계에서 ___자를 결정한다. (successful applicant)", "합격", ["불합격", "지원"], "합격자."), F("정부는 ___과 경쟁을 정책 기조로 삼았다. (autonomy)", "자율", ["강제", "규제"], "자율."),
           read_q("입학사정관제는 학생의 잠재력을 중시합니다"), read_q("성적 위주로 학생을 선발해 왔습니다"), read_q("서류심사와 심층면접을 합니다"), read_q("내년부터 고교선택제가 실시됩니다"), read_q("북한의 교육에 대해 아는 것을 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 3", [
        ("경시대회", "(競試大會) a competition (through tests)", "", "수학 경시대회, 에세이 경시대회"),
        ("기특하다", "(奇特) to be admirable; to be praiseworthy; to be commendable. This word is used when an adult commends children or youths for their good deeds, not the other way around.", "너, 참 기특하다. 학원을 한 번도 안 다니고 전교 일 등을 하고 말이야."),
        ("외고", "(外高) a foreign language high school (short form of 외국어 고등학교)", ""),
    ]),
    ("학습활동 4", [
        ("발휘(하다)", "(發揮) display (of one’s skill, talent, ability); exhibition (to display; to exhibit; to show)", "한국 국가대표 축구 선수들이 월드컵에서 실력을 발휘했습니다.", "보이다"),
        ("선발(하다/되다)", "(選拔) selection (to select; to pick out/to be selected)", "이동국 선수가 국가대표 선수로 선발되었습니다.", "뽑다, 선택하다"),
        ("인성", "(人性) character; personality", "요즘 학교 교육은 너무 성적에만 치중해서 인성 교육을 소홀히 하는 것 같아요.", "성격"),
        ("창의성", "(創意性) creativity; ingenuity", "창의성이 있는 학생들은 예술 분야에서 뛰어나다.", "창의력"),
        ("판단(하다)", "(判斷) judgment (to judge)", "아이들을 성적으로만 판단하지 마세요."),
        ("한계", "(限界) limit; limitation", "마라톤을 하면서 체력의 한계를 많이 느꼈어요."),
    ]),
]
L3 = lesson(
    "U16 L4 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 경시대회 · 기특하다 · 외고 · 발휘 · 선발 · 인성 · 창의성 · 판단 · 한계",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 기특하다 has 전교 1등 (written 전교 일 등 here). The book’s note on 기특하다 is kept in the meaning.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=6, nread=5)),
)

# ================================================================== L4 Part 2 texts
_SPEAK4B = [("친구와 함께 시험 성적 때문에 고민했던 경험에 대해서 이야기해 보세요.", "Talk with a friend about an experience of worrying because of test grades."), ("미국에서 대학교에 진학하기 위한 준비과정과 지원 절차에 대해 친구와 이야기해 보세요.", "Talk with a friend about the preparation process and application procedure for going on to university in the United States.")]
L4 = lesson(
    "U16 L4 · Part 2 (본 학습): the student’s worry and the education policy",
    "본 학습 · 시험 성적 고민 · 제주시 · 사교육 · 고교선택제 · 자율과 경쟁 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3 (Listening): the education policy sentences", "The book plays a KBS news commentary on private education (track 012) and asks which topic it concerns (among: improving the quality of public education; limiting the hours of private institute night classes; limiting private education; government ratification of the new educational system), which past countermeasures the government took, and what the author advises the government. It then asks you to translate three sentences from the clip into English. The sentences, which are text, are the book’s; the translation is mine:", examples=passage(_SENT4)),
        card("학습활동 3: my answers", "1. The topic of the commentary is best described by C, limiting private education (the vocabulary of the activity — 사교육, 공교육, 규제, 명문, 실효성, 시행 — points to a discussion of regulating private education and how effective such measures are). This answer is my best guess, as the audio is not here.\n\n3. The three sentences are translated above."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK4B)),
        card("Activities left out", "학습활동 1 (Reading · Speaking): a picture of an entry on the education site edunet4u.net in which a student, 최재용, writes about his worry over a test score (what kind of day he is having, and completing a sentence about why he does not want to show the test to his parents). 학습활동 2 (Listening, track 011): a YTN news item on a school established in Jeju City (all classes but Korean and Social Studies in English; true/false statements). These are a picture and audio."),
    ],
    exercises=uniq(
        _tr(_SENT4 + _SPEAK4B, k=3)
        + [M("What is the basis of the government’s education policy?", "Autonomy and competition", ["Uniformity", "Free tuition", "Strict control"], "자율과 경쟁."), M("What will be implemented in Seoul from next year?", "A high school choice system", ["A ban on cram schools", "A new uniform", "A longer school year"], "고교선택제."), M("What else will be carried out?", "School autonomy", ["School closures", "Exam abolition", "A merger of schools"], "학교 자율화."),
           F("내년부터 서울에서는 고교___제가 실시됩니다. (choice)", "선택", ["선발", "경쟁"], "고교선택제."), F("현 정부의 교육정책 ___는 자율과 경쟁입니다. (basis)", "기조", ["한계", "인성"], "기조."),
           read_q("현 정부의 교육정책 기조는 자율과 경쟁입니다"), read_q("내년부터 서울에서는 고교선택제가 실시됩니다"), read_q("학교 자율화도 시행됩니다"), read_q("시험 성적 때문에 고민했던 경험이 있습니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("괜히", "in vain; uselessly; for no (good) reason", "엄마한테 괜히 거짓말을 했다."),
        ("어차피", "(於此彼) anyway; anyhow", "그 돈은 어차피 갚아야 할 돈이다."),
    ]),
    ("학습활동 2", [
        ("흡수(하다/되다)", "(吸收) absorption (to absorb/to be absorbed)", "이 천은 물을 잘 흡수해서 수건으로 쓰면 좋아요."),
        ("본격적", "(本格的) full-scale; full-blown; full-fledged; real; genuine", "본격적인 수사가 시작되었습니다."),
        ("불리하다", "(不利) to be disadvantageous", "상황이 우리한테 너무 불리합니다.", "불이익"),
        ("서민", "(庶民) common people; working-class people; “commoners”", "물가가 너무 올라 서민들이 어려움을 겪고 있다.", "귀족"),
        ("존재(하다)", "(存在) existence; presence (to exist; to be present)", "저는 신의 존재를 믿습니다."),
    ]),
    ("학습활동 3", [
        ("내신성적", "(內申成績) a school GPA; a school record", "저는 내신성적이 좋지 않아서 걱정이 됩니다."),
        ("심야", "(深夜) night; “deep night”", "심야와 주말에는 통화요금이 할인됩니다.", "심야방송, 심야버스"),
        ("규제(하다)", "(規制) regulation; control; restriction (to regulate; to control; to restrict)", "보건복지부는 이 약의 사용을 규제합니다."),
        ("명문", "(名門) prestige; prestigious; “a gate with a name”", "케네디 가족은 모두 명문 대학에 입학했습니다.", "무명, 비명문"),
        ("사교육", "(私敎育) private education; private extra curriculum; private tutoring", "학부모들의 사교육비 부담이 점점 늘어나고 있습니다.", "공교육"),
        ("실효성", "(實效性) effectiveness", "새 법안이 실효성이 있을지 의문입니다.", "효과"),
        ("시행(하다/되다)", "(施行) enforcement; implementation (to enforce; to implement/to be enforced; to be implemented)", "한국도 이제 주 오 일 근무제를 시행하고 있습니다.", "실시되다"),
    ]),
]
L5 = lesson(
    "U16 L4 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 괜히 · 어차피 · 흡수 · 본격적 · 불리하다 · 서민 · 존재 · 내신성적 · 심야 · 규제 · 명문 · 사교육 · 실효성 · 시행",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 시행 has 주 5일 (written 주 오 일 here).")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=10, nread=8)),
)

# ================================================================== L6 Part 3 texts
_P1 = [("저희 대학교에 입학하게 된 것을 축하 드립니다.", "Congratulations on being admitted to our university."), ("학교 오리엔테이션은 삼 월 오 일 학교 강당에서 있습니다.", "The school orientation will be held in the school auditorium on March 5."), ("오리엔테이션 전에 온라인을 통해 전공 과목과 필수 과목의 수강신청을 마치시기 바랍니다.", "Please finish registering for your major subjects and required subjects online before the orientation.")]
_P2 = [("윤상현 학생은 앞으로 이과 분야의 전공을 하는 것이 적당한 것으로 결과가 나왔습니다.", "The result came out that it is appropriate for the student Yun Sang-hyeon to major in the natural sciences field in the future."), ("저희들이 추천하는 전공으로는 건축학, 수학, 생물학입니다.", "The majors we recommend are architecture, mathematics and biology."), ("문과 학생이라면 디자인학, 경영학, 무역학을 추천합니다.", "If he were a liberal arts student, we would recommend design, business administration and trade studies.")]
_P3 = [("오성진 학생은 공부뿐만 아니라 봉사활동 클럽활동도 아주 열심히 하는 훌륭한 학생입니다.", "The student Oh Seong-jin is an excellent student who works very hard not only at study but also at volunteer work and club activities."), ("특히 음악에 소질이 많고 지역 내 대회에서도 여러 번 수상을 하였습니다.", "In particular, he has a lot of talent for music and has won prizes several times in competitions within the region."), ("앞으로 음악을 전공하여 많은 사람들에게 기쁨을 안길 것입니다.", "In the future he will major in music and bring joy to many people.")]
_SPEAK4C = [("여기에서 언급된 촌지에 관련해 얘기해 봅시다.", "Let us talk about the 촌지 mentioned here."), ("촌지 관행을 없애기 위해서 학교, 교사, 부모, 그리고 정부에서 어떤 노력을 해야 한다고 생각합니까?", "What efforts do you think schools, teachers, parents and the government should make to do away with the practice of 촌지?")]
L6 = lesson(
    "U16 L4 · Part 3 (심화 학습): 촌지, the arts and science tracks, and three result notices",
    "심화 학습 · 촌지 · 문과 · 이과 · 계열 선택 · 학과계열선정검사 · 오리엔테이션 · 전공 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 1: 촌지 — the book’s note",
             "촌지 (寸志), which literally means “a knuckle[ful] of intention” or “a small sincerity,” refers to a little gift that a person gives to a benefactor or lifesaver in order to convey “small” appreciation. Today, however, 촌지 often refers to bribes or cash gifts people give to their benefactors in exchange for “special” treatment. Even though the word 촌지 can apply to all forms of bribes, it is commonly used in reference to education and the bribes offered by parents to teachers. (Image © Hankyoreh.)"),
        card("알아봅시다 2: 문과 and 이과 track selection — the book’s note",
             "While in high school, students have to choose either the liberal arts track (문과) or natural sciences track (이과) in preparation for their major area of study in college. Depending on the chosen area, students have differing subject requirements. For example, 이과 계열 students would focus more on science and mathematics, while 문과 계열 students would focus primarily on social studies and Korean literature. (The book adds a footnote: 문이과 is a compound word made with 문과 and 이과.)"),
        card("학습활동 1 (Reading): a Q&A on the aptitude test for a major area", "The book gives a Q&A exchange on the 학과계열선정검사 (aptitude test for major area of study) (© Naeil), a picture whose question is not in the text, so it is left out here. Question 2 gives three short passages (the book’s text; the date 3월 5일 is spelled 삼 월 오 일; the English is mine) and asks which passage most closely relates to the test results discussed in the Q&A.\n\nPassage 1:", examples=passage(_P1)),
        card("학습활동 1: Passage 2", "Passage 2:", examples=passage(_P2)),
        card("학습활동 1: Passage 3", "Passage 3:", examples=passage(_P3)),
        card("학습활동 1: my answers", "1. The Q&A question is in the picture and is not in the text, so I cannot translate it.\n\n2. Passage 2 is the one that relates to test results: it reports the result of an aptitude test (“the result came out that it is appropriate to major in the natural sciences field”) and recommends majors, while Passage 1 is a welcome and orientation notice and Passage 3 is a recommendation of a student’s activities and talent. (This is my answer from the passages alone, since the Q&A is not here.)\n\n3. Summary of Passage 2: the results of the aptitude test show that the student Yun Sang-hyeon is suited to a natural sciences major; the recommended majors are architecture, mathematics and biology, and if he were a liberal arts student they would recommend design, business administration and trade studies."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK4C)),
        card("Activities left out", "학습활동 2 (Listening, track 013): a YTN news item on a graduation ceremony — why the students are unique (they are 만학도, late learners) and what many of them plan to do after graduation. 학습활동 3 (Listening, track 014): a Donga news commentary on 촌지 given to teachers — the tone of the passage, what percentages such as 46.8% and 18.6% indicate (the book gives 46.8%: “It is not bribery, but it is bad practice.”), the parents’ intention in giving 촌지, and the speaker’s solution. They are audio."),
    ],
    exercises=uniq(
        _tr(_P1 + _P2 + _P3, k=3) + _tr(_SPEAK4C, k=2)
        + [M("What does 촌지 originally mean?", "A small gift to show small appreciation", ["A large donation", "A school fee", "A prize"], "The book’s note."), M("What does 촌지 often mean today?", "Bribes or cash gifts for special treatment", ["Free lunches", "School supplies", "Study aid"], "The book’s note."), M("Who commonly gives 촌지 in the education context?", "Parents to teachers", ["Teachers to students", "Students to parents", "Schools to the state"], "The book’s note."), M("Which track focuses on science and mathematics?", "이과", ["문과", "체육과", "예술과"], "The book’s note."), M("Which track focuses on social studies and Korean literature?", "문과", ["이과", "공과", "농과"], "The book’s note."),
           M("Which passage reports an aptitude test result?", "Passage 2", ["Passage 1", "Passage 3", "None"], "윤상현 학생."), M("What does Passage 1 announce?", "A university orientation on March 5", ["A test result", "A prize", "A trip"], "오리엔테이션."), M("What talent does 오성진 have?", "Music", ["Math", "Painting", "Sports"], "음악에 소질."), M("Which majors are recommended for 윤상현 in the natural sciences?", "Architecture, mathematics, biology", ["Law, history, art", "Music, dance, drama", "Cooking, farming, fishing"], "건축학, 수학, 생물학."),
           F("저는 이과보다는 ___가 적성에 더 맞아요. (liberal arts)", "문과", ["이과", "체육"], "문과."), F("학교에서 ___ 정보를 제공합니다. (useful)", "유용한", ["고통스러운", "촌스러운"], "유용하다."), F("그 교사는 학부모로부터 ___를 받았다. (a small gift)", "촌지", ["학비", "수업료"], "촌지."), F("저는 이과로 ___할 생각이에요. (go on to a higher school)", "진학", ["퇴학", "휴학"], "진학."), F("최종적으로 합격자를 ___했습니다. (decided)", "결정", ["거절", "묵살"], "결정."),
           read_q("오리엔테이션은 삼 월 오 일 강당에서 있습니다"), read_q("이과 분야의 전공을 하는 것이 적당합니다"), read_q("음악에 소질이 많고 여러 번 수상을 했습니다"), read_q("촌지 관행을 없애기 위해 노력해야 합니다"), read_q("문과와 이과 중에서 하나를 선택해야 합니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("문과", "(文科) liberal arts", "저는 이과보다는 문과가 적성에 더 맞아요.", "이과"),
        ("선호(하다)", "(選好) preference (to prefer)", "한국에서는 이 브랜드를 선호하는 사람이 많습니다."),
        ("유용하다", "(有用) to be useful; to be helpful; to be valuable", "인터넷에는 유용한 정보가 많습니다."),
        ("이과", "(理科) natural science", "저는 이과로 진학할 생각이에요.", "문과"),
        ("제시(하다/되다)", "(提示) suggestion; indication (to suggest/to be suggested)", "비판만 하지 마시고 대안을 제시해 주세요."),
        ("최종적(으로)", "(最終的) final(ly); last(ly)", "이 소설의 최종 결말이 궁금합니다."),
        ("특성", "(特性) characteristic; nature", "이 제품의 특성을 좀 설명해 주세요.", "특징"),
        ("학문", "(學問) academic learning; (one’s) academic studies", "나는 한때 교수가 되려고 학문에 열중한 적이 있었다.", "학업"),
    ]),
    ("학습활동 2", [
        ("고통", "(苦痛) pain; agony; torment", "치료를 받는 게 너무 고통스러워요."),
        ("만학도", "(晩學徒) “a late learner” (owing to economic hardships, etc.)", "우리 어머니는 만학도로 대학에 입학하셨어요."),
        ("머뭇거리다", "to hesitate; to be hesitant", "한국말을 할 때 머뭇거리게 된다."),
        ("순간", "(瞬間) moment; instant", "제가 집에 들어간 순간 전화가 왔어요."),
        ("열정", "(熱情) passion; ardor", "그분은 학생을 가르치는 데 온 열정을 다 합니다.", "정열"),
        ("한", "(恨) (deep) resentment; sorrow; regret", "공부를 못한 것이 한이 되어서 자식들은 모두 대학에 보내고 싶습니다."),
    ]),
    ("학습활동 3", [
        ("거절(하다)", "(拒絶) rejection; refusal (to reject; to refuse)", "저는 그 사람을 보고 싶지 않아서 초대를 거절했어요.", "거부하다, 마다하다"),
        ("관행", "(慣行) practice; custom; convention; norm", "과거에는 군대 내에서의 폭력이 관행이었다.", "관례"),
        ("뇌물", "(賂物) bribe; kickback", "그 국회의원은 뇌물을 받은 혐의로 구속되었다."),
        ("마다하다", "to refuse; to reject", "돈이 된다면 어떤 일도 마다하지 않는다.", "거절하다, 거부하다"),
        ("불이익", "(不利益) disadvantage", "아직도 여자라는 이유로 직장에서 불이익을 당하는 여직원들이 있습니다.", "이익"),
        ("이기심", "(利己心) selfishness; self-centeredness", "이 사건은 인간의 이기심 때문에 벌어진 일입니다.", "이기적"),
        ("자명하다", "(自明) to be obvious; to be certain; to be clear; to be self-explanatory", "태양이 동쪽에서 뜨는 것은 자명한 이치입니다.", "확실하다"),
        ("자발적", "(自發的) voluntary", "학생들이 자발적으로 나서서 이 일을 추진하기로 했습니다."),
        ("준법", "(遵法) law-abiding", "어렸을 때부터 준법정신에 대한 교육을 받아야 합니다."),
        ("촌지", "(寸志) a small gift; “small token of appreciation”", "그 교사는 학부모로부터 촌지를 받았다."),
        ("충격", "(衝擊) impact; shock", "이 사건은 제게 큰 충격입니다."),
        ("현명하다", "(賢明) to be wise; to be sensible", "어려움을 해결하기 위해서는 현명한 결정이 필요합니다.", "지혜롭다"),
    ]),
]
L7 = lesson(
    "U16 L4 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 문과 · 이과 · 선호 · 유용하다 · 제시 · 최종적 · 특성 · 학문 · 고통 · 만학도 · 머뭇거리다 · 열정 · 한 · 거절 · 관행 · 뇌물 · 마다하다 · 불이익 · 이기심 · 자명하다 · 자발적 · 준법 · 촌지 · 충격 · 현명하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book prints the related word of 이기심 as 이기적; it is kept as printed. The Hanja of 한 (恨) is the same character as in the Korean cultural term 한 (deep sorrow and resentment).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=18, nread=14)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 4: College Entrance Examination (대학입시)", [L1, L2, L3, L4, L5, L6, L7])
