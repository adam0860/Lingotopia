"""Unit 70: KBC Semester III, Unit 16, Lesson 5 - Private Education (사교육).
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
_MATCH5 = [("꼴찌", "the last (in ranking)", "시험에서 꼴찌 하다"), ("이성친구", "the opposite sex (friend)", "이성친구가 생기다"), ("담임 선생님", "a homeroom teacher", "담임 선생님을 만나다"), ("학기말", "the end of a semester", "오 월이 학기말이다"), ("과외", "an extracurricular lesson; tutoring", "영어 과외를 받다"), ("진로", "a future route; a career path", "진로를 정하다"), ("등수", "a rank; a place", "등수를 매기다"), ("학원", "a private institute; an academy", "학원에 다니다")]
_SIM5 = [("부족하다", "모자라다", "to be insufficient: to be short"), ("수강하다", "수업을 듣다", "to take a course: to attend a class"), ("드디어", "마침내", "at last: finally"), ("마치다", "끝내다", "to finish: to end"), ("교제하다", "사귀다", "to associate with: to go out with"), ("결심하다", "마음을 먹다", "to decide: to make up one’s mind")]
_HJ5 = [("成 성", "accomplish; achieve", "성적, 완성"), ("外 외", "the outside; exterior", "실외, 과외"), ("實 실", "practical; real", "실업계, 실력"), ("校 교", "school", "교장, 교실"), ("內 내", "the inside; interior", "교내, 내성적")]
_HJW5 = [("성적", "a grade; a mark; a result"), ("완성", "completion; accomplishment"), ("실외", "outside the room; outdoors"), ("과외", "extracurricular work; a private lesson"), ("실업계", "the (high) school track for a vocational career"), ("실력", "ability; skill; “strength to bear fruit”"), ("교장", "a principal; “school chief”"), ("교실", "a classroom"), ("교내", "the school grounds; the campus; “inside the school”"), ("내성적", "introverted")]
_OPP5 = [("교복", "사복", "a school uniform: ordinary clothes"), ("실업계", "인문계", "the vocational track: the academic track"), ("성공", "실패", "success: failure"), ("국내", "해외", "domestic: overseas"), ("제외", "포함", "exclusion: inclusion")]
_ODD5 = [("A", "실외", "과외, 성적, 입시", "실외 is outdoors; the others are about lessons, grades and entrance exams"), ("B", "완성", "학교, 교실, 교장실", "완성 is completion; the others are school places"), ("C", "특성", "성적, 등수, 시험", "특성 is a characteristic; the others are about exams and grades"), ("D", "실력", "성격, 외향적, 내성적", "실력 is ability; the others are about personality")]
_L5X = [("사복", "ordinary clothes (not a uniform)"), ("인문계", "the academic (liberal arts) track"), ("해외", "overseas"), ("국내", "domestic"), ("제외", "exclusion"), ("포함", "inclusion"), ("입시", "an entrance exam"), ("교장실", "the principal’s office"), ("특성", "a characteristic"), ("성격", "personality"), ("외향적", "extroverted"), ("모자라다", "to be short; to be insufficient"), ("충분하다", "to be enough"), ("남다", "to remain"), ("수강하다", "to take a course"), ("재수하다", "to retake the entrance exam"), ("전공하다", "to major in"), ("마침내", "finally"), ("이제", "now"), ("끝내다", "to finish"), ("육성하다", "to nurture"), ("확실하다", "to be sure"), ("교제하다", "to date; to associate with"), ("사귀다", "to make friends with; to go out with"), ("그만두다", "to quit"), ("결석하다", "to be absent"), ("시키다", "to make (someone) do")]
L1 = lesson(
    "U16 L5 · Review: school-life words and Sino-Korean 成 外 實 校 內",
    "사교육 · 단어 복습 · 한자어 복습 · 꼴찌 · 담임 선생님 · 학기말 · 과외 · 진로 · 등수 · 학원 · 成 外 實 校 內",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives eight phrases with the last word underlined and asks you to connect each underlined word with its meaning on the right. The pairs (the phrase 5월이 학기말이다 is written 오 월이 학기말이다):", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH5], say=[0, 2])]),
        card("단어 복습 2: words with a similar meaning (my answers)", "Circle the word with a similar meaning to the word on the left (A. 부족하다: 충분하다, 남다, 모자라다; B. 수강하다: 재수하다, 전공하다, 수업을 듣다; C. 드디어: 이제, 마침내, 혼자; D. 마치다: 끝내다, 육성하다, 확실하다; E. 교제하다: 시키다, 그만두다, 사귀다; F. 결심하다: 충분하다, 마음(을) 먹다, 결석하다).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [list(r) for r in _SIM5], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ5], say=[2]), ktable(_HJW5)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 교복: 내복, 외모, 사복; B. 실업계: 외고, 특목고, 인문계; C. 성공: 생성, 실패, 확실; D. 국내: 야외, 해외, 과외; E. 제외: 확실, 내용, 포함).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP5], say=[0, 1])]),
        card("한자어 복습 2: the least related word (my answers)", "Circle the word least related to the other words. My answers:", tables=[table(["", "Least related (my answer)", "The other words", "Why"], [list(r) for r in _ODD5], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L5X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH5], k=3) + _tr(_HJW5, k=3) + _tr(_L5X, k=3) + _tr([(a, c) for a, b, c in _SIM5], k=3)
        + [M("What does the syllable 成 (성) mean?", "accomplish; achieve", ["the outside", "school", "the inside"], "성적."), M("What does the syllable 外 (외) mean?", "the outside; exterior", ["accomplish", "school", "the inside"], "실외."), M("What does the syllable 實 (실) mean?", "practical; real", ["accomplish", "the outside", "school"], "실력."), M("What does the syllable 校 (교) mean?", "school", ["accomplish", "the outside", "the inside"], "교실."), M("What does the syllable 內 (내) mean?", "the inside; interior", ["accomplish", "the outside", "school"], "교내."),
           M("Which word is similar to 부족하다?", "모자라다", ["충분하다", "남다", "많다"], "To be short."), M("Which word is similar to 드디어?", "마침내", ["이제", "혼자", "아직"], "Finally."), M("Which word is similar to 교제하다?", "사귀다", ["시키다", "그만두다", "헤어지다"], "To go out with."), M("Which word is similar to 결심하다?", "마음을 먹다", ["충분하다", "결석하다", "포기하다"], "To decide."),
           M("Which word is the opposite of 교복?", "사복", ["내복", "외모", "정복"], "Ordinary clothes."), M("Which word is the opposite of 성공?", "실패", ["생성", "확실", "완성"], "Failure."), M("Which word is the opposite of 국내?", "해외", ["야외", "과외", "실외"], "Overseas."), M("Which word is the opposite of 제외?", "포함", ["확실", "내용", "제한"], "Inclusion."),
           M("Which word does not fit 학교, 교실, 교장실?", "완성", ["교무실", "도서관", "운동장"], "Completion."), M("Which word does not fit 성적, 등수, 시험?", "특성", ["점수", "입시", "합격"], "Characteristic."),
           F("영어 ___를 받고 있습니다. (a private lesson)", "과외", ["실외", "교내"], "과외."), F("시험에서 ___를 해서 속상합니다. (last place)", "꼴찌", ["일등", "등수"], "꼴찌."), F("___ 선생님께 상담했습니다. (homeroom)", "담임", ["교장", "과외"], "담임."), F("진로를 ___ 위해 상담을 받았습니다. (decide)", "정하기", ["그만두기", "결석하기"], "정하다."), F("우리 학교는 ___에 운동장이 있습니다. (inside the school grounds)", "교내", ["실외", "해외"], "교내."),
           read_q("영어 과외를 받고 있습니다"), read_q("담임 선생님을 만났습니다"), read_q("진로를 정했습니다"), read_q("학원에 다니고 있습니다"), read_q("그는 내성적인 성격입니다")]
    ),
)

# ================================================================== L2 Part 1
_DAY = [
    ("서울 서초구의 한 초등학교에 다니는 정식이에게 가장 바쁜 날은 월요일이다.", "For Jeongsik, who goes to an elementary school in Seocho-gu, Seoul, the busiest day is Monday."),
    ("기상시간은 오전 일곱 시.", "The time he gets up is 7 a.m."),
    ("아침을 챙겨 먹고 여덟 시 십 분쯤 집을 나선다.", "He sees to eating breakfast and leaves the house at about 8:10."),
    ("수업은 여덟 시 사십 분쯤 시작된다.", "Classes start at about 8:40."),
    ("오후 한 시 이십 분, 오 교시 마지막 수업이 끝나는 종이 울렸다.", "At 1:20 p.m., the bell ringing the end of the last, fifth-period class rang."),
    ("아직은 방과 후 수업이 남아 있다.", "There are still after-school classes left."),
    ("정식이는 정규 수업을 마치고 채 십 분도 안 돼 바로 방과 후 수업이 진행되는 교실로 이동해야 했다.", "Jeongsik had to move, not even ten minutes after finishing the regular classes, straight to the classroom where the after-school class is held."),
    ("오후 한 시 삼십 분부터 한 시간 동안 단소 수업, 오후 두 시 삼십 분부터 컴퓨터 수업을 한다.", "From 1:30 p.m. there is a danso class for one hour, and from 2:30 p.m. a computer class."),
    ("방과 후 수업을 모두 끝내니 오후 세 시 삼십 분이었다.", "When he finished all the after-school classes, it was 3:30 p.m."),
    ("방과 후 수업을 마친 정식이는 재빨리 책가방을 쌌다.", "Having finished the after-school classes, Jeongsik quickly packed his school bag."),
    ("일주일에 두 번 받는 영어 과외를 해야 할 시간이다.", "It is time for the English tutoring he receives twice a week."),
    ("선생님은 미국 유학을 다녀온 한국인이다.", "The teacher is a Korean who has been back from studying in America."),
    ("수업은 미국의 초등학교 교과서를 이용해 영어로 한다.", "The lesson is held in English using American elementary school textbooks."),
    ("정식이의 영어는 수준급이었다.", "Jeongsik’s English was first-rate."),
    ("과외를 마친 후 오후 여섯 시쯤 저녁을 먹었다.", "After finishing the tutoring, he ate dinner at about 6 p.m."),
    ("이미 날이 어두웠다.", "It was already dark."),
    ("그러나 정식이의 일과는 아직 끝나지 않았다.", "But Jeongsik’s daily routine was not yet over."),
    ("오후 일곱 시 검도복을 입고 검도 학원으로 향했다.", "At 7 p.m. he put on his kendo uniform and headed to the kendo academy."),
    ("두 시간 땀을 흘리고 집에 돌아오니 오후 아홉 시.", "After sweating for two hours and coming back home, it was 9 p.m."),
    ("파김치가 돼 집에 온 그는 “이제 숙제 해야 돼요”라고 했다.", "Coming home exhausted, he said, “Now I have to do my homework.”"),
    ("숙제는 물론 매일 엄마가 정해 준 분량의 문제집도 풀어야 한다.", "Besides the homework, he must also solve the amount of workbook problems that his mother sets for him every day."),
    ("정식이의 어머니는 “과하다고 느끼진 않는다.", "Jeongsik’s mother said, “I don’t feel it is excessive."),
    ("주위를 봐도 이 정도면 아주 평균적인 수준”이라고 말했다.", "Even looking around, this much is a very average level.”"),
    ("숙제를 하고 문제집과 씨름하다 보니 어느새 열한 시가 가까웠다.", "After doing homework and wrestling with the workbook, before he knew it it was close to 11 o’clock."),
]
_SPEAK5 = [("초, 중, 고등학교 다닐 때 해 본 과외 활동이나 과외 수업이 있으면 친구와 이야기해 보세요.", "If there are any extracurricular activities or private lessons you did when you were in elementary, middle and high school, talk about them with a friend."), ("학교 공부 이외에 학원이나 과외를 통해 공부나 다른 활동을 보충해 주는 것에 대해 어떻게 생각하는지 친구와 이야기해 보세요.", "Talk with a friend about what you think of supplementing study or other activities through institutes or tutoring other than school study.")]
L2 = lesson(
    "U16 L5 · Part 1 (도입 학습): an elementary schooler’s busy Monday",
    "도입 학습 · 사교육 · 학원 · 과외 · 방과 후 수업 · 단소 · 검도 · 문제집 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 한국의 사교육 — 학원, 과외 (private education in Korea) — the book’s note",
             "In Korea, many students (from elementary through high school) receive additional education after school through private institutes or personal tutoring. Elementary school students usually take a variety of after-school classes, such as music, art, sports, and foreign languages. Middle and high school students focus mainly on mathematics, English, and other major subject areas to prepare for school tests and their eventual college entrance exam. Because most parents want their children to be accepted at reputable colleges, they invest a good deal of money in private education for their children. This adds a burden to the household budget. Even though the Korean government has tried several policies to reduce the cost of private education, thus far their efforts have not been very successful."),
        card("학습활동 4 (Reading): an elementary school pupil’s daily routine",
             "The following is the daily routine of an elementary school pupil (Text and image © Kyunghyang). The text is the book’s with the times and numbers spelled out (7시 → 일곱 시; 8시 10분 → 여덟 시 십 분; 5교시 → 오 교시; 1시간 → 한 시간; 2시간 → 두 시간 and so on); the quotation marks ‘ ’ around 방과 후 수업 are removed. The English is mine.",
             examples=passage(_DAY)),
        card("학습활동 4: the questions answered (mine)",
             "1. The table: 1:30–2:30 danso (short bamboo flute) class; 2:30–3:30 computer class; between 3:30 and 6:00 English tutoring (twice a week, with a Korean teacher who studied in America, in English using American elementary school textbooks) and dinner at about 6; 7:00–9:00 kendo (Japanese fencing); 9:00–11:00 homework and the workbook his mother sets.\n\n"
             "2. His mother says she does not feel his schedule is excessive: looking around, this much is a very average level."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK5)),
        card("Activities left out", "학습활동 1 (Reading): a public-interest advertisement on education (© Kobaco) to be summarized in English; it is a picture. 학습활동 2 (Listening, tracks 001 and 002): parents talking about their children’s education, with a table of concerns and suggestions. 학습활동 3 (Reading): statistics from a survey of high school students (© Kyunghyang), with a table of percentages (33.1%: “I can do well in my studies without (after-school) private education”; 38.8%; 27.9%) and a graph (who took part, the topic of the survey, and what 30.8% represents); both are charts."),
    ],
    exercises=uniq(
        _tr(_DAY, k=3) + _tr(_SPEAK5, k=2)
        + [M("Which day is busiest for Jeongsik?", "Monday", ["Friday", "Sunday", "Wednesday"], "월요일."), M("What time does he get up?", "7 a.m.", ["9 a.m.", "5 a.m.", "noon"], "오전 일곱 시."), M("What instrument does he learn in the after-school class?", "Danso (a short bamboo flute)", ["Piano", "Violin", "Drums"], "단소."), M("How often does he have English tutoring?", "Twice a week", ["Every day", "Once a month", "Never"], "일주일에 두 번."), M("What is his tutor like?", "A Korean who studied in America", ["A native American", "A Chinese teacher", "A student"], "미국 유학을 다녀온 한국인."), M("Which martial art does he study at night?", "Kendo", ["Taekwondo", "Judo", "Karate"], "검도."), M("What time does he get home?", "9 p.m.", ["6 p.m.", "midnight", "noon"], "오후 아홉 시."), M("What does his mother think of the schedule?", "It is an average level", ["It is too much", "It is too little", "It is shameful"], "평균적인 수준."),
           F("정식이는 ___ 수업을 마치고 방과 후 수업으로 갔다. (regular)", "정규", ["비정규", "특별"], "정규 수업."), F("그는 ___가 돼 집에 왔다. (exhausted)", "파김치", ["배추김치", "총각김치"], "파김치가 되다."), F("엄마가 정해 준 ___의 문제집을 풀어야 한다. (amount)", "분량", ["수업", "시간"], "분량."), F("수업이 끝나는 ___이 울렸다. (bell)", "종", ["벨", "북"], "종."), F("그의 영어는 ___이었다. (first-rate)", "수준급", ["형편없음", "초보"], "수준급."),
           read_q("정식이에게 가장 바쁜 날은 월요일입니다"), read_q("방과 후 수업이 남아 있습니다"), read_q("영어 과외를 일주일에 두 번 받습니다"), read_q("두 시간 땀을 흘리고 집에 돌아왔습니다"), read_q("학원이나 과외에 대해 어떻게 생각합니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("형편없다", "(for things, service, etc.) to be terrible; to be awful; to be lousy", "이건 정말 형편없는 영화군요."),
    ]),
    ("학습활동 4", [
        ("과하다", "(過) to be excessive", "한국 고등학생들의 수업량이 과한 것 같아요."),
        ("기상(하다)", "(起床) getting up; getting out of bed (to get up)", "기상시간을 꼭 지켜 주세요.", "일어나다, 깨다"),
        ("문제집", "(問題集) a workbook; “problem collection”", "문제집 살 돈이 필요해요. 용돈 좀 주세요.", "교과서, 참고서"),
        ("분량", "(分量) amount; quantity; dose", "숙제의 분량이 좀 많습니다.", "양"),
        ("수준급", "(水準級) excellent; first-rate", "제 동생은 수영 실력이 수준급이에요."),
        ("울리다", "to sound; to ring", "전화벨이 크게 울렸어요."),
        ("재빨리", "quickly; rapidly", "지진이 발생하면 재빨리 안전한 곳으로 대피해야 합니다."),
        ("종", "(鐘) a bell", "수업시작을 알리는 종이 울렸어요. 시작합시다."),
        ("주위", "surroundings", "길을 건너기 전에 주위를 잘 둘러 보세요.", "주변"),
        ("파김치가 되다", "to become exhausted; to be pooped; “to become green onion kimchi”", "일을 너무 많이 했더니 파김치가 되었어요.", "지치다 | 생생하다 | 피곤하다"),
    ]),
]
L3 = lesson(
    "U16 L5 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 형편없다 · 과하다 · 기상 · 문제집 · 분량 · 수준급 · 울리다 · 재빨리 · 종 · 주위 · 파김치가 되다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book lists the related words of 파김치가 되다 as 지치다 | 생생하다 | 피곤하다; they are kept as printed (생생하다, “to be vivid; fresh”, is the opposite of being worn out).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=9, nread=7)),
)

# ================================================================== L4 Part 2 texts
_CAMP5 = [
    ("초등영어캠프 참가자 모집", "Recruiting participants for the elementary English camp (the heading)."),
    ("제주대학교 여름방학 초등영어캠프로 여러분을 초대합니다.", "You are invited to the “Jeju National University Summer Vacation Elementary English Camp.”"),
    ("제주대학교 초등영어캠프는 원어민과의 다양한 활동과 놀이를 통하여 영어에 대한 흥미를 유발시키고, 자신감을 키워 영어실력을 한층 향상시킬 뿐만 아니라, 해외어학연수를 대신할 유익한 프로그램으로 다음과 같이 캠프참가자를 모집하오니 많은 신청 부탁드립니다.", "The Jeju National University Elementary English Camp is a beneficial program that not only arouses interest in English through various activities and games with native speakers, builds confidence and raises English ability still further, but also can replace overseas language training, so we are recruiting camp participants as follows, and we ask for many applications."),
    ("모집인원: 초등 구십 명.", "Number recruited: 90 elementary pupils."),
    ("모집대상: 초등 삼 학년에서 육 학년.", "Target: elementary grades 3 to 6."),
    ("캠프기간: 이천십 년 팔 월 이 일부터 팔 월 십삼 일까지, 십일 박 십이 일.", "Camp period: from August 2 to August 13, 2010 (11 nights, 12 days)."),
    ("접수기간: 이천십 년 유월 칠 일부터 유월 삼십 일까지, 입금자 선착순 마감.", "Registration period: from June 7 to June 30, 2010 (closing on a first-come basis by those who have paid)."),
    ("신청방법: 영어캠프 홈페이지에서 회원 가입, 참가 신청, 신청서 작성.", "How to apply: on the English camp homepage, join as a member, apply to participate and fill out the application."),
    ("참가비: 구십오만 원.", "Participation fee: 950,000 won."),
    ("캠프문의: 제주대학교 외국어교육원 행정실.", "Camp inquiries: the administration office of the Jeju National University Foreign Language Education Center."),
    ("캠프 특징: 초 중학생들을 대상으로 한 이십여 차에 걸친 영어캠프 노하우.", "Camp features: know-how from some twenty English camps for elementary and middle school students."),
    ("국립제주대학교의 최신 시설과 쾌적한 비티엘 학생생활관 기숙사에서 진행되는 안전한 캠프.", "A safe camp held at the latest facilities of Jeju National University and the pleasant BTL student residence (dormitory)."),
    ("유능한 원어민과 함께하는 수준별 잉글리시 온리 프로그램.", "A level-based English Only Program with capable native speakers."),
    ("정규수업 외 문화, 퀴즈, 요리, 체육, 영화, 팝송, 역할극 등을 통한 다양한 주제별 영어학습.", "Various topic-based English learning through culture, quizzes, cooking, sports, movies, pop songs, role plays and so on, besides regular classes."),
    ("놀이를 통한 체험식 실생활 영어수업.", "Hands-on, real-life English classes through play."),
    ("원어민과 함께 하는 주말 현장체험학습 필드 트립.", "Weekend field-trip learning with native speakers."),
    ("과정수료자에게 수료증과 메모리앨범 시디 제작 수여.", "A certificate of completion and a memory album CD are produced and given to those who complete the course."),
]
_SPEAK5B = [("한국에서는 외국어를 공부하기 위해서 해당 언어권 국가로 조기 유학을 가는 경우가 많습니다.", "In Korea there are many cases of going on early study abroad to the country of the relevant language area in order to study a foreign language."), ("이러한 조기유학의 장, 단점에 대해서 친구와 이야기해 보세요.", "Talk with a friend about the advantages and disadvantages of such early study abroad.")]
_TF5 = [("The teachers in this program are all Koreans who are proficient in English.", "F", "The teachers are capable native speakers."), ("This program is designed chiefly for advanced students.", "F", "It is a level-based program for elementary pupils."), ("Participants will stay in a college dorm during the camp.", "T", "The camp is held in the student residence (dormitory) of the university."), ("The program is an intensive language program focusing on test preparation.", "F", "It focuses on activities and play, not test preparation."), ("There will be a variety of English-language activities related to culture, cooking, sports, and movies.", "T", "문화, 퀴즈, 요리, 체육, 영화.")]
L4 = lesson(
    "U16 L5 · Part 2 (본 학습): an elementary English camp advertisement",
    "본 학습 · 조기 유학 · 기러기 아빠 · 초등영어캠프 · 제주대학교 · 모집 · 선착순 · 수료증 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 조기 유학과 기러기 아빠 (early study abroad and goose dads) — the book’s note",
             "In Korea, good English-language skills are important when applying for college or for a job. Therefore, many people invest a great deal of time, effort, and money to become competent in English. Because young children can learn a new language more easily than adults, many parents send their children to English-speaking countries, including the United States, Canada, Australia, and the Philippines. Often, the mother will accompany her children abroad, leaving the father in Korea. These fathers who are left alone in Korea are called “기러기 아빠 (goose dads)” because they must “migrate” a few times a year to visit their families. Their daily lives are spent earning the money needed to support their families abroad. This trend of studying abroad can have a negative impact on children’s behavior and can create financial problems for a family, or even lead to its dissolution. There are some successful cases, but some language education experts express doubts about the ultimate benefits of sending children abroad, given the enormous cost to families."),
        card("학습활동 1 (Reading): an advertisement on a university foreign language institute’s homepage",
             "The following is an advertisement from the homepage of a university’s foreign language education center (© Cheju National University). The text is the book’s with the numbers and symbols spelled out (90명 → 구십 명; 3~6학년 → 삼 학년에서 육 학년; the camp dates → 이천십 년 팔 월 이 일부터 팔 월 십삼 일까지, 십일 박 십이 일; 6월 → 유월; 950,000원 → 구십오만 원; 20여차 → 이십여 차; BTL → 비티엘; English Only Program → 잉글리시 온리 프로그램; Field Trip → 필드 트립; CD → 시디; the arrows in the application steps are written as commas); the web address, the bank account number and the telephone numbers are left out. The English is mine.",
             examples=passage(_CAMP5)),
        card("학습활동 1: the questions answered (mine)",
             "1. It is an advertisement recruiting participants for the Jeju National University summer vacation elementary English camp.\n\n"
             "2. Elementary school pupils in grades 3 to 6 (90 places).\n\n"
             "3. Goals: arouse interest in English through activities and games with native speakers; build confidence and raise English ability further; serve as a beneficial program that can replace overseas language training.\n\n"
             "4. Steps: join as a member on the English camp homepage → apply to participate → fill out the application → (pay the fee; places close on a first-come basis by those who have paid).\n\n"
             "5. True or false:",
             tables=[table(["Statement", "T/F", "Why"], [list(r) for r in _TF5])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK5B)),
        card("Activities left out", "학습활동 2 (Listening, track 003): a YTN news item on early study abroad — which of four negative statements is not mentioned (adaptation difficulties because of language and culture; social disharmony between classes; panic caused by loneliness; not cost-effective), a table of the number of elementary school pupils studying abroad and the annual cost in 1998, 2000 and 2004, and the alternatives that education experts suggest. 학습활동 3 (Video, tracks 004 and 005): interviews on early study abroad — the difficulties of a first interviewee who went to China to study, and the two kinds of students who are the best candidates for study abroad. They are audio and video."),
    ],
    exercises=uniq(
        _tr(_CAMP5[1:], k=3) + _tr(_SPEAK5B, k=2)
        + [M("Which university runs the camp?", "Jeju National University", ["Seoul National University", "Yonsei University", "Korea University"], "제주대학교."), M("How many pupils are recruited?", "90", ["9", "190", "40"], "구십 명."), M("Which grades are the target?", "Grades 3 to 6", ["Grades 1 to 2", "Middle school", "High school"], "삼 학년에서 육 학년."), M("How long is the camp?", "11 nights, 12 days", ["2 days", "A month", "A week"], "십일 박 십이 일."), M("What is the fee?", "950,000 won", ["95,000 won", "9,500,000 won", "Free"], "구십오만 원."), M("How are applications closed?", "On a first-come basis by those who have paid", ["By lottery", "By exam", "By interview"], "입금자 선착순 마감."), M("Who teaches in the program?", "Capable native speakers", ["Only Korean teachers", "Volunteers", "Students"], "유능한 원어민."), M("Where do participants stay?", "In the student residence (dormitory)", ["In a hotel", "At home", "In tents"], "학생생활관 기숙사."), M("What do those who complete the course receive?", "A certificate and a memory album CD", ["A trophy", "A scholarship", "Money"], "수료증과 메모리앨범 시디."),
           F("캠프참가자를 ___합니다. (recruit)", "모집", ["마감", "수여"], "모집."), F("___으로 입금자부터 접수합니다. (first-come)", "선착순", ["수준별", "주제별"], "선착순."), F("과정수료자에게 ___을 수여합니다. (certificate)", "수료증", ["문제집", "입장권"], "수료증."), F("원어민과 함께 하는 활동으로 영어실력을 ___ 향상시킵니다. (further)", "한층", ["널리", "겨우"], "한층."), F("캠프의 목표는 영어에 대한 ___를 유발하는 것입니다. (interest)", "흥미", ["우려", "위화감"], "흥미."),
           read_q("제주대학교 초등영어캠프에 여러분을 초대합니다"), read_q("모집대상은 초등 삼 학년에서 육 학년입니다"), read_q("원어민과 함께하는 수준별 프로그램입니다"), read_q("과정수료자에게 수료증을 수여합니다"), read_q("조기 유학의 장점과 단점에 대해 이야기해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("노하우", "know-how", "노하우를 익히고 나면 일이 훨씬 더 쉬워질 거에요."),
        ("~을/를 통하여", "through; by; from", "해외 연수를 통하여 외국 문화에 대한 많은 경험을 했어요.", "~을/를 통해서"),
        ("마감(하다/되다)", "ending; closing; finishing; deadline (to end; to close; to finish/to be closed; to be finished)", "내일이 원서 접수 마감이에요."),
        ("모집(하다/되다)", "(募集) recruiting (to recruit/to be recruited)", "저희 학원에서는 외국어 강좌 신입생을 모집합니다."),
        ("선착순", "(先着順) by order of arrival; first-come, first-served", "선착순으로 줄을 서세요."),
        ("수료증", "(修了證) a certificate of completion", "이 과정이 끝나면 수료증을 받을 수 있습니다."),
        ("수여(하다/되다)", "(授與) presenting (an award, a certificate, etc.) (to award; to confer/to be awarded)", "성적이 좋은 학생에게 장학금이 수여되었다."),
        ("~차", "(次) times", "수십여 차에 걸친 다양한 경험을 통해 전문가가 되었다.", "~ 차례"),
        ("유익(하다)", "(有益) benefit (to be useful; to be beneficial; to be constructive)", "이번 유럽여행은 제게 유익한 경험이었어요.", "유용하다"),
        ("자신감", "(自信感) confidence; self-confidence", "면접을 볼 때는 자신감을 가지고 대답해야 합니다."),
        ("정규", "(正規) regular; formal; official", "우리 학교에서는 정규 과목 외에도 다양한 방과 후 활동을 한다.", "비정규 | 정규직, 정규교육"),
        ("주제", "(主題) a topic", "이 책의 주제가 무엇입니까?"),
        ("최신", "(最新) the newest; the latest", "이 냉장고는 최신 제품입니다."),
        ("쾌적하다", "(快適) to be pleasant; to be nice", "여기는 공기도 깨끗하고 쾌적한 환경이네요."),
        ("키우다", "to develop; to cultivate; to build up", "외국어 실력을 키우기 위해 어릴 때부터 노력했어요."),
        ("한층", "much; even; far; still", "건강해지기 위해서 한층 더 힘쓰고 있어요."),
        ("향상(하다/되다)", "(向上) improvement (to improve/to be improved)", "김 일병의 한국어 실력이 많이 향상되었어요."),
        ("흥미", "(興味) interest", "저는 컴퓨터에 흥미가 있어요."),
    ]),
    ("학습활동 2", [
        ("내실화(하다)", "(內實化) strengthening the inner value or structure (of an entity) (to strengthen the inner value or structure of)", "사교육 비용을 줄이기 위해서는 공교육을 내실화해야 한다."),
        ("머물다", "to remain; to stay", "환율이 천백 원대에 머물고 있습니다."),
        ("비교(하다/되다)", "(比較) comparison (to compare/to be compared)", "전년도에 비교해서 수출이 많이 증가했어요."),
        ("우려(하다/되다)", "(憂慮) concern; worry (to worry about/to be worried)", "각국 정부는 지구온난화에 대해 우려의 목소리를 높이고 있습니다.", "걱정하다"),
        ("위화감", "(違和感) a sense of incongruity; a sense of incompatibility; a sense of disharmony", "일부 계층의 사치로 계층간 위화감이 커져 가고 있습니다."),
        ("차단(하다/되다)", "(遮斷) blocking; shutting off (to block off; to shut off/to be blocked off; to be shut off)", "햇빛을 차단하기 위해 두꺼운 커튼을 쳤어요."),
        ("폭증(하다)", "(爆增) sharp increase; sudden increase; “explosive increase” (to suddenly increase)", "그 뉴스가 나온 후 그 배우의 홈페이지 방문자가 폭증했다.", "폭락하다 | 증가하다, 급증하다"),
        ("후유증", "(後遺症) an aftermath; aftereffects", "우리 아버지는 사고 후유증으로 고생하고 계십니다."),
    ]),
]
L5 = lesson(
    "U16 L5 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 노하우 · 마감 · 모집 · 선착순 · 수료증 · 수여 · 유익 · 자신감 · 정규 · 주제 · 최신 · 키우다 · 한층 · 향상 · 흥미 · 내실화 · 머물다 · 우려 · 위화감 · 차단 · 폭증 · 후유증",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 머물다 has 1100원대 (written 천백 원대 here). The book prints the related words of 폭증하다 as 폭락하다 | 증가하다, 급증하다; they are kept as printed (폭락하다, “to plummet”, is the opposite). The book’s two-line examples are joined into one example.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=18, nread=14)),
)

# ================================================================== L6 Part 3 texts
_TCH = [
    ("교사와 학생, 학부모 모두를 만족시키는 생활지도는 무척 어려운 일 중의 하나라고 생각한다.", "I think that guidance on school life that satisfies teachers, students and parents alike is one of the very difficult things."),
    ("특히나 요즘 체벌 금지로 인한 생활 지도의 어려움은 교실에서 말로 못 하는 경우가 많다고 한다.", "In particular, they say that the difficulty of guidance on school life caused by the ban on corporal punishment these days is often beyond words in the classroom."),
    ("문제아들이 장난을 하거나 떠들어 정상적인 수업을 할 수 없을 정도로 방해하거나 쉬는 시간에는 약하게 보이는 친구들을 괴롭히는 일이 다반사라고 한다.", "They say it is an everyday occurrence for problem children to play around or make noise and disturb to the point that normal class cannot be held, or to bully friends who look weak during breaks."),
    ("학기초 반 어머니 회의 시 학급 운영 방침을 밝히면서 장난이 심하거나 친구들을 괴롭히는 경우 또한 다른 친구들의 수업권을 훼손하는 정도가 심한 경우는 생활지도 차원에서 방과 후 한자쓰기를 하면서 지도하려고 한다고 말씀드렸다.", "At the class mothers’ meeting at the start of the semester, while stating the class management policy, I said that for cases of serious mischief or bullying friends, and cases that seriously damage other friends’ right to class, I intended to guide them, at the level of life guidance, by having them write Chinese characters after school."),
    ("참석하신 어머니들도 좋은 아이디어라고 생각하신다며 호응하셨다.", "The mothers who attended also responded positively, saying they thought it was a good idea."),
    ("말썽꾸러기 아이들은 어려운 한자를 몇 번이고 반복해서 쓰는 것에 질렸는지 지적받는 것에 매우 조심하는 경우가 많았다.", "The troublemaking children, perhaps sick of writing difficult Chinese characters repeatedly, were often very careful about being reprimanded."),
    ("그렇게 한자쓰기를 하면서 나머지 공부를 하게 되는 경우에는 간단한 내용과 함께 그 사실을 메시지로 통하여 부모님께 알려 드렸다.", "When they ended up staying behind for extra study while writing characters like that, I informed the parents of that fact by message together with a short note."),
    ("생활 지도에 왕도는 없는 것 같다.", "There seems to be no royal road to guidance on school life."),
    ("학부모님과 유기적인 연락과 학생들에게 지속적인 관심으로 보살펴 줘야겠다.", "I should look after the students with close contact with parents and continued attention."),
]
_ED = [
    ("서울시 교육청이 그제 내놓은 체벌 전면금지 방안을 둘러싸고 논란이 가열되고 있다.", "Controversy is heating up over the plan for a total ban on corporal punishment that the Seoul Metropolitan Office of Education put out the day before yesterday. (paragraph 1)"),
    ("한국교원단체총연합회 교총는 반대 입장을 분명히 했고, 교육과학기술부 역시 독단적 행위라며 비판적 견해를 드러냈다.", "The Korean Federation of Teachers’ Associations made its opposition clear, and the Ministry of Education, Science and Technology also revealed a critical view, calling it a dogmatic act."),
    ("하지만 최근 공개된 한 초등학교 교사의 폭력 동영상에서 보듯이 체벌의 탈을 쓴 교사의 폭력은 근절되지 않고 있다.", "But as seen in the violence video of an elementary school teacher released recently, teachers’ violence under the mask of corporal punishment is not being eradicated. (paragraph 2)"),
    ("일부에서 주장하는 체벌의 교육적 효과도 위력을 통한 강제로는 진정한 의미의 승복을 이끌어내기 어렵다는 점에서 받아들이기가 쉽지 않다.", "The educational effect of corporal punishment that some claim is also not easy to accept, in that it is hard to draw out true acceptance through coercion by force."),
    ("따라서 폭력에 의존하는 권위주의적인 학교문화를 바꾸고 학생과 교사의 인권이 두루 존중되는 학교문화를 만들어나가기 위해서도 체벌은 금지되는 게 마땅하다.", "Therefore, in order to change the authoritarian school culture that depends on violence and to create a school culture in which the human rights of both students and teachers are respected, corporal punishment ought to be banned."),
    ("문제는 체벌 금지를 어떻게 학교 현장에 뿌리내릴 수 있게 할 것인가다.", "The problem is how to make the ban on corporal punishment take root in the school setting. (paragraph 3)"),
    ("체벌 금지를 반대하는 쪽은 학생 상호간의 폭력뿐만 아니라 교사에 대한 학생의 폭언과 폭력 또는 수업방해 행위 등이 존재하는 현실을 걱정한다.", "Those opposed to the ban worry about the reality in which there exist not only violence among students but also students’ abusive language and violence toward teachers, acts of disrupting class, and so on."),
    ("이런 상황을 다스릴 수 있는 제도적 장치를 마련하지 않은 채 체벌만 금지할 경우 학교 현장이 큰 혼란에 빠질 수 있다는 것이다.", "They say that if only corporal punishment is banned without preparing institutional devices that can handle such situations, the school setting could fall into great confusion."),
    ("시 교육청은 이런 우려에 대해서도 충분히 귀를 기울여야 한다.", "The city Office of Education must listen carefully enough to these concerns too. (paragraph 4)"),
    ("체벌 금지는 학교 현장의 문화를 바꾸는 일이며, 그것이 선언 하나로 하루아침에 이뤄질 수는 없다.", "Banning corporal punishment is a matter of changing the culture of the school setting, and that cannot be achieved overnight by one declaration."),
    ("무엇보다 현장에서 학생 지도의 어려움을 호소하는 교사들에게 체벌이 아닌 교육적 방식으로 학생들을 이끌어갈 수 있는 길이 있음을 구체적으로 보여주는 게 필요하다.", "Above all, it is necessary to show concretely to teachers who appeal about the difficulty of guiding students in the field that there is a way to lead students by educational methods rather than corporal punishment."),
    ("교과부나 교총 역시 반대만 하지 말고 이 참에 시 도 교육청과 더불어 아이들이 인격적으로 대우받을 수 있는 학교문화를 만들어 낼 방안을 고민하기 바란다.", "We hope that the Ministry of Education and the KFTA too, rather than only opposing, will take this opportunity to think, together with the city and provincial education offices, about a plan to create a school culture in which children can be treated with dignity."),
]
_SPEAK5C = [("미국에서는 학교 교사의 체벌이 금지되어 있습니다.", "In the United States corporal punishment by school teachers is banned."), ("이러한 교사의 교육적 체벌에 대해 찬성하는지 반대하는지 의견을 이야기해 보고 왜 그렇게 생각하는지 그 이유도 말해 보세요.", "Tell your opinion on whether you are for or against such educational corporal punishment by teachers, and also tell why you think so.")]
_SUG5 = [("Seoul Metropolitan Office of Education", "Listen carefully to the concerns; recognize that the ban is a change of school culture that cannot come overnight by one declaration; concretely show teachers who appeal about the difficulty of guiding students that there is a way to lead students by educational methods other than corporal punishment."), ("The Korean Federation of Teachers’ Associations and the Ministry of Education, Science and Technology", "Not only oppose, but take this chance to think, together with the city and provincial education offices, about a plan to create a school culture in which children are treated with dignity.")]
L6 = lesson(
    "U16 L5 · Part 3 (심화 학습): banning corporal punishment",
    "심화 학습 · 체벌 금지 · 사랑의 매 · 생활지도 · 한자쓰기 · 학교문화 · 서울시 교육청 · 교총 · 인권 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 교사의 체벌 금지 (banning corporal punishment in schools) — the book’s note",
             "For centuries, parents used corporal punishment to compel their children to study hard and earn degrees to gain a higher position in society. Corporal punishment in schools was socially accepted in this tradition and was in wide use. However, in November 2010, the Seoul School District, the largest school district in South Korea, banned corporal punishment at all its schools. This stirred up an age-old controversy. Proponents of corporal punishment argue that it is necessary because it provides an immediate response to improper behavior. As a result, the student is quickly back in the classroom learning, rather than being suspended from school. Proponents call the rod (or any instrument) teachers use for corporal punishment 사랑의 매, which literally means “a rod of love.” Opponents argued that other disciplinary methods are equally or more effective and that corporal punishment must be banned from schools for good. (Image © kimyn@hani.co.kr.)"),
        card("학습활동 2 (Reading): a teacher’s posting on an information-sharing site",
             "The following is a posting by a teacher on a site for sharing information among teachers (© edunet4u.net). The text is the book’s. The English is mine.",
             examples=passage(_TCH)),
        card("학습활동 2: the questions answered (mine)",
             "1. D — a way of guiding school life that can replace corporal punishment (the teacher describes handling pupils with after-school Chinese character writing instead of corporal punishment).\n\n"
             "2. At the parents’ meeting at the start of the semester, the teacher announced the class policy: pupils who play around a great deal, bully friends, or seriously damage other children’s right to class would be guided, as life guidance, by writing Chinese characters after school. The mothers responded positively.\n\n"
             "3. As a follow-up, when pupils stayed after school to write characters and do extra study, the teacher informed the parents by message with a short note, and resolved to keep close contact with parents and give pupils continued attention."),
        card("학습활동 3 (Reading): an editorial on educational corporal punishment",
             "The following is an editorial on educational corporal punishment (© Hankyoreh). The text is the book’s with the paragraph numbers dropped (they are given in the English) and the middle dot in 폭언·폭력 written as 와. The English is mine.",
             examples=passage(_ED)),
        card("학습활동 3: the questions answered (mine)",
             "1. B — the author is opposed to using corporal punishment in schools (the editorial says that corporal punishment ought to be banned).\n\n"
             "2. The underlined sentence is not marked in the text; all the sentences are translated above (for example, “corporal punishment ought to be banned” is the editorial’s conclusion in paragraph 2).\n\n"
             "3. Arguments in paragraph 2: teachers’ violence under the mask of corporal punishment is not being eradicated (as in the recent video of an elementary school teacher’s violence); the educational effect that some claim is hard to accept, since coercion by force can hardly bring out true acceptance; and to change the authoritarian school culture that depends on violence and build one in which the human rights of students and teachers are respected, corporal punishment ought to be banned.\n\n"
             "4. The author’s suggestions:",
             tables=[table(["Concerned party", "Author’s suggestion (mine)"], [list(r) for r in _SUG5])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK5C)),
        card("Activities left out", "학습활동 1 (Listening, track 006): a YTN news item on a policy announced by the Seoul Metropolitan Office of Education on school corporal punishment — the policy and the incident that triggered it, the role of the Office’s task force, and the reaction and arguments of the Korean Federation of Teachers’ Associations. It is audio."),
    ],
    exercises=uniq(
        _tr(_TCH, k=3) + _tr(_ED, k=3) + _tr(_SPEAK5C, k=2)
        + [M("What does 사랑의 매 literally mean?", "A rod of love", ["A bell of love", "A song of love", "A gift of love"], "The book’s note."), M("When did the Seoul School District ban corporal punishment?", "November 2010", ["March 1990", "May 2000", "June 2020"], "The book’s note."), M("What do proponents say corporal punishment provides?", "An immediate response to improper behavior", ["A delayed warning", "A reward", "A suspension"], "The book’s note."),
           M("What does the teacher make misbehaving pupils do after school?", "Write Chinese characters", ["Run laps", "Clean the school", "Stand in the hall"], "한자쓰기."), M("How does the teacher inform the parents?", "By message", ["By mail", "By visit", "By newspaper"], "메시지."), M("Who responded positively to the idea?", "The mothers who attended", ["The principal", "The students", "The police"], "참석하신 어머니들."), M("Which stance does the editorial take?", "It supports banning corporal punishment", ["It supports corporal punishment", "It is neutral", "It is silent"], "체벌은 금지되는 게 마땅하다."), M("Who opposed the plan for a total ban?", "The KFTA and the Ministry of Education", ["The Seoul office", "Students", "Parents only"], "교총, 교육과학기술부."), M("What did the editorial say about changing school culture?", "It cannot be achieved overnight by one declaration", ["It is easy", "It is already done", "It is unnecessary"], "하루아침에 이뤄질 수는 없다."),
           F("체벌 ___ 방안을 둘러싸고 논란이 가열되고 있다. (total ban)", "전면금지", ["전면허용", "부분금지"], "전면금지."), F("체벌의 ___을 쓴 교사의 폭력은 근절되지 않고 있다. (mask)", "탈", ["옷", "손"], "탈을 쓰다."), F("학생과 교사의 ___이 두루 존중되는 학교문화를 만들어야 한다. (human rights)", "인권", ["입장", "행위"], "인권."), F("시 교육청은 이런 우려에 ___를 기울여야 한다. (ear)", "귀", ["눈", "입"], "귀를 기울이다."), F("생활 지도에 ___는 없는 것 같다. (royal road)", "왕도", ["매뉴얼", "경계"], "왕도."),
           read_q("체벌은 금지되는 것이 마땅합니다"), read_q("방과 후 한자쓰기로 지도하려고 합니다"), read_q("생활 지도에 왕도는 없는 것 같습니다"), read_q("아이들이 인격적으로 대우받을 수 있는 학교문화를 만들어야 합니다"), read_q("교사의 교육적 체벌에 대해 어떻게 생각합니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("갑작스럽다", "to be sudden; to be abrupt; to be unexpected", "너무 갑작스러운 소식이라서 할 말이 없군요."),
        ("공분을 사다", "(公憤) to cause public indignation or public rage", "이번 사건은 여러 사람의 공분을 샀다."),
        ("교권", "(敎權) teachers’ authority; teachers’ rights", "최근 교권이 너무 약화됐다며 걱정하는 사람들이 많습니다."),
        ("규정", "(規定) a rule; a regulation", "이 건물 내에서의 흡연은 규정에 어긋납니다.", "규칙, 법"),
        ("극약처방", "(劇藥處方) extreme measures; “prescribing extreme medicine”", "문제를 해결하기 위해 극약처방을 했는데, 오히려 더 나빠졌어요."),
        ("논란", "(論難) controversy; dispute; argument", "이 문제는 논란의 여지가 많습니다."),
        ("다수", "(多數) majority; “many numbers”", "다수의 의견을 따르도록 합시다.", "소수"),
        ("대들다", "to rebel against (one’s superior or senior); to talk back (to one’s superior or senior)", "부모님께 대들면 안 됩니다."),
        ("물의를 빚다", "to evoke criticism; to stir up trouble; to cause a scandal", "개인적인 일로 물의를 빚어서 죄송합니다.", "문제를 일으키다"),
        ("전면", "(全面) (on a) full-scale (basis); completely; “whole face”", "다음 달부터 건물 내에서의 흡연이 전면 금지된다.", "일부"),
        ("정당하다", "(正當) to be just; to be fair; to be right; to be legal", "제가 한 행동은 정당하다고 생각합니다.", "부당하다"),
        ("종합적으로", "(綜合的) overall; comprehensively; synthetically", "여러 의견을 종합적으로 분석해 보겠습니다."),
        ("주장(하다)", "(主張) a contention; a claim; an argument; (to contend; to claim; to argue)", "용의자는 계속 무죄를 주장했습니다."),
        ("체벌(하다; 가하다)", "(體罰) corporal punishment (to give corporal punishment)", "학생 체벌에 대해 찬반논란이 많습니다.", "매"),
        ("침해(하다)", "(侵害) an infringement; a violation (to infringe; to violate)", "중국에서 인권을 침해한다는 논란이 있습니다."),
        ("폐지(하다/되다)", "(廢止) an abolishment; a revocation (to abolish; to revoke/to be abolished; to be revoked)", "사형제를 폐지하자고 주장하는 사람들이 늘고 있다."),
        ("폭언", "(暴言) abusive language; violent language; “explosive language”", "저는 상사의 폭언을 참을 수 없습니다.", "욕 | 폭행"),
        ("호소(하다)", "(呼訴) an appeal; a plea (to appeal; to plead)", "구호단체들이 이재민들을 도와달라고 호소하고 있습니다."),
        ("혼란", "(混亂) confusion; chaos; disorder", "잦은 쿠데타로 사회가 혼란에 빠졌습니다.", "무질서 | 질서, 안정"),
        ("휩싸이다", "to be engulfed; to be seized (with); to be overwhelmed (with); to be filled (with)", "많은 사람들이 지진의 공포에 휩싸였다."),
    ]),
    ("학습활동 2", [
        ("다반사", "(茶飯事) everyday occurrence; common occurrence", "우리 회사는 야근이 다반사이에요.", "예삿일, 흔한 일"),
        ("말썽꾸러기", "a troublemaker; a mischief maker", "모두다 그 집 아들을 말썽꾸러기라고 합니다.", "문제아"),
        ("문제아", "(問題兒) a problem child; a troublemaker", "학교에서 모두 저를 문제아라고 생각해서 학교 가기가 싫어요.", "말썽꾸러기"),
        ("방침", "(方針) a policy; a course (of action)", "정부의 새 방침에 반대하는 사람들이 많습니다.", "정책"),
        ("방해(하다/되다)", "(妨害) disturbance; interruption; interference (to disturb; to interrupt; to interfere with/to be disturbed; to be interrupted)", "자는데 방해하지 마세요."),
        ("보살피다", "to look after; to take care of; to care for; “to look and watch”", "부모님께서 저희들을 잘 보살펴 주셨어요.", "돌보다"),
        ("생활지도", "(生活指導) guidance on life; coaching on life", "이 선생님은 학습지도와 생활지도를 모두 다 잘해 주십니다.", "학습지도"),
        ("왕도", "(王道) a royal road", "", "지름길"),
        ("유기적", "(有機的) organic; close (relationship, connection, etc.)", "저희는 다른 사회 봉사 단체들과 유기적 관계를 유지하고 있습니다."),
        ("질리다", "to be sick and tired of; to be overwhelmed", "스파게티를 너무 많이 먹어서 이제 질렸어요.", "싫증나다"),
        ("호응(하다)", "(呼應) a positive response (to positively respond to)", "대통령의 새 정책에 많은 사람이 호응했다.", "반응하다"),
        ("훼손(하다/되다)", "(毁損) damage; harm (to damage; to harm; to defame/to be damaged)", "자연을 훼손하지 마세요.", "보존하다 | 파괴하다"),
    ]),
    ("학습활동 3", [
        ("가열(하다/되다)", "(加熱) heating up; “adding heat” (to heat up/to be heated up)", "국회의원 선거에서 경쟁이 가열되고 있다."),
        ("강제로", "by force; forcibly", "탈북자들은 중국에서 강제로 쫓겨났습니다.", "스스로, 자율적으로"),
        ("견해", "(見解) a view (on/about); an opinion", "체벌에 대한 김 선생님의 견해는 무엇입니까?", "의견"),
        ("권위주의", "(權威主義) authoritarianism", "칠십 년대와 팔십 년대 권위주의 정권에 대항하는 사람들이 많았어요."),
        ("귀를 기울이다", "to listen carefully; to give careful attention to; “to lean an ear”", "다른 사람의 의견에도 귀를 기울이세요.", "주의를 기울이다"),
        ("근절(하다/되다)", "(根絶) eradication; rooting out (to eradicate; to root out/to be eradicated; to be rooted out)", "학교폭력은 근절되어야 합니다."),
        ("대우(하다/받다)", "(待遇) treatment (to treat/to be treated)", "그 친구네 집에서 아주 대우를 잘 받았어요."),
        ("더불어", "together; along with; in company with", "산업발전과 더불어 환경오염도 심해졌습니다.", "함께 | 따로, 별개로"),
        ("독단적", "(獨斷的) dogmatic", "그 사람은 모든 일에 아주 독단적이에요."),
        ("드러내다", "to show; to reveal; to expose", "그 사람은 감정을 잘 드러내지 않습니다."),
        ("마땅하다", "to be suitable; to be appropriate", "김 일병이 상을 받는 것은 마땅한 일이에요.", "당연하다"),
        ("분명히", "(分明) clearly", "조금 더 분명히 말해 주세요.", "확실히"),
        ("비판적", "(批判的) critical", "너무 비판적으로만 보지 마세요."),
        ("뿌리내리다", "to take root; to become implanted", "평화가 한반도에 뿌리내리길 바랍니다."),
        ("선언(하다/되다)", "(宣言) an announcement; a declaration; a proclamation (to announce/to be announced)", "인기 배우 김승연이 은퇴를 선언했어요."),
        ("승복(하다/되다)", "(承服) accepting a result or decision (to accept a result or decision/to be accepted)", "이번 선거 결과에 승복하겠습니다."),
        ("위력", "(威力) power; force", "국방부에서 새로 개발한 무기의 위력이 대단합니다.", "힘"),
        ("~의 탈을 쓰다", "in the likeness of; under the mask of; “wear a mask of”", "그 사람은 양의 탈을 쓰고 있지만 위험한 사람입니다."),
        ("인격", "(人格) personality; character", "유아시절은 인격을 형성하는 중요한 시기입니다."),
        ("입장", "(立場) one’s stance or position", "친구로서 제 입장이 좀 곤란합니다."),
        ("존재(하다)", "(存在) existence; presence (to exist; to be present)", "화성에 생명체가 존재합니까?"),
        ("존중(하다/되다)", "(尊重) respect (to respect/to be respected)", "제 사생활을 좀 존중해 주세요.", "존경하다"),
        ("진정한", "(眞正) true; genuine", "어려울 때 도와주는 친구가 진정한 친구입니다."),
        ("하루아침에", "to be done in a day", "성공은 하루아침에 이루어지지 않습니다.", "이루어지다"),
        ("행위", "(行爲) an act; an action; a deed", "경찰은 범법행위에 대해 엄중히 대처하기로 했습니다."),
    ]),
]
L7 = lesson(
    "U16 L5 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 교권 · 규정 · 논란 · 전면 · 정당하다 · 주장 · 체벌 · 침해 · 폐지 · 폭언 · 호소 · 혼란 · 다반사 · 말썽꾸러기 · 문제아 · 방해 · 보살피다 · 생활지도 · 왕도 · 호응 · 훼손 · 견해 · 권위주의 · 근절 · 대우 · 독단적 · 마땅하다 · 승복 · 인격 · 입장 · 존중 · 행위",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book the Hanja of 방침 is printed 方枕, a slip for 方針; of 승복 it is printed 僧服 (a monk’s robe), a slip for 承服 (to accept a decision); and of 왕도 it is printed 王度, usually written 王道; they are corrected here. The book’s example for 존재 reads 화성(Mars)에 생명체가; the English in the brackets is left out. The book’s example for 권위주의 has 70년대와 80년대 (written 칠십 년대와 팔십 년대 here).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=30, nread=24)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 5: Private Education (사교육)", [L1, L2, L3, L4, L5, L6, L7])
