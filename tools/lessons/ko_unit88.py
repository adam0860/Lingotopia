"""Unit 88: KBC Semester III, Unit 18, Lesson 3 - Employment (취업).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 18, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH3 = [("소지하다", "to possess; to carry", "여권을 소지하다"), ("우대하다", "to give preferential treatment", "외국인을 우대하다"), ("추진하다", "to propel; to drive", "계획을 추진하다"), ("도입하다", "to introduce; to adopt", "새 제도를 도입하다"), ("침체되다", "to be stagnated; to be stagnant", "경기가 침체되다"), ("기피하다", "to avoid; to evade", "병역을 기피하다"), ("감축하다", "to reduce; to downsize", "종업원을 감축하다"), ("채용되다", "to be employed", "대기업에 채용되다"), ("제출하다", "to submit; to turn in", "서류를 제출하다"), ("접수하다", "to receive; to accept", "원서를 접수하다")]
_PAIR3 = [("청년", "노년", "youth: old age"), ("폐업", "개업", "closing a business: opening a business"), ("구인", "구직", "seeking a person: seeking a job"), ("불리", "유리", "disadvantage: advantage"), ("참가", "불참", "taking part: not taking part"), ("단기", "장기", "short term: long term"), ("유능", "무능", "capable: incapable"), ("해고", "채용", "dismissal: hiring")]
_HJ3 = [("求 구", "seeking", "구직, 구인"), ("面 면", "face; surface", "면접, 표면"), ("半 반", "half", "하반기, 절반"), ("用 용", "use", "고용, 다용도"), ("書 서", "book; document", "이력서, 증명서")]
_HJW3 = [("구직", "seeking a job"), ("구인", "recruiting a person"), ("면접", "a (face-to-face) interview"), ("표면", "a surface"), ("하반기", "the second half of a year"), ("절반", "a half"), ("고용", "employment"), ("다용도", "multipurpose"), ("이력서", "a resume"), ("증명서", "a certificate")]
_SIM3 = [("표면", "겉", "a surface: the outside"), ("지원서", "신청서", "an application form: an application"), ("전반적", "대체로", "overall: on the whole"), ("고용", "채용", "employment: hiring")]
_CAT3 = [("이력서, 증명서, 신고서", "서류", "resume, certificate, report form: documents"), ("정면, 후면, 측면", "방면", "front, rear, side: direction"), ("비누, 치약, 면도기", "세면도구", "soap, toothpaste, razor: toiletries"), ("애용, 활용, 전용", "이용", "frequent use, utilization, exclusive use: use")]
_L3X = [("여권", "a passport"), ("외국인", "a foreigner"), ("병역", "military service"), ("종업원", "an employee"), ("대기업", "a large company"), ("원서", "an application form"), ("청년", "a young person; youth"), ("노년", "old age"), ("폐업", "closing a business"), ("개업", "opening a business"), ("불참", "non-attendance"), ("유능", "capability"), ("무능", "incapability"), ("해고", "dismissal"), ("겉", "the outside"), ("지원서", "an application form"), ("인증서", "a certificate of authentication"), ("신고서", "a report form"), ("신청서", "an application"), ("보고서", "a report"), ("전반적", "overall"), ("후반전", "the second half (of a game)"), ("대체로", "on the whole"), ("부분적", "partial"), ("악용", "abuse; misuse"), ("전용", "exclusive use"), ("유용", "usefulness"), ("정면", "the front"), ("후면", "the rear"), ("측면", "the side"), ("비누", "soap"), ("치약", "toothpaste"), ("면도기", "a razor"), ("애용", "frequent use"), ("활용", "utilization"), ("세면도구", "toiletries"), ("방면", "a direction; a field"), ("이용", "use"), ("서류", "documents"), ("품목", "an item")]
L1 = lesson(
    "U18 L3 · Review: job-hunting words and Sino-Korean 求 面 半 用 書",
    "취업 · 단어 복습 · 한자어 복습 · 소지 · 우대 · 추진 · 도입 · 침체 · 기피 · 감축 · 채용 · 제출 · 접수 · 求 面 半 用 書",
    requires=[],
    cards=[
        card("단어 복습 1: connect each verb with its meaning", "The left column of the book has ten phrases with the verb underlined; the underline is not marked in the text, so I give the verb of each phrase and its meaning:", tables=[table(["Verb", "Meaning", "Phrase"], [list(r) for r in _MATCH3], say=[0, 2])]),
        card("단어 복습 2: the word with the opposite meaning (my matching)", "The lines are not drawn in the text; the pairs below are the opposites as I read them:", tables=[table(["Word", "Opposite", "Meaning"], [list(r) for r in _PAIR3], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ3], say=[2]), ktable(_HJW3)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word closest in meaning to the word on the left (A. 표면: 안, 겉, 위, 아래; B. 지원서: 인증서, 신고서, 신청서, 보고서; C. 전반적: 하반기, 후반전, 대체로, 부분적; D. 고용: 악용, 전용, 유용, 채용).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM3], say=[0, 1])]),
        card("한자어 복습 2: the word that includes all three (my answers)", "Choose from the box (세면도구, 방면, 이용, 서류, 품목) the word that includes the three words of each line:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _CAT3], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L3X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH3], k=3) + _tr(_HJW3, k=3) + _tr(_L3X, k=4) + _tr([(a, b) for a, b, c in _PAIR3], k=3)
        + [M("What does the syllable 求 (구) mean?", "seeking", ["face; surface", "half", "use"], "구직."), M("What does the syllable 面 (면) mean?", "face; surface", ["seeking", "half", "book"], "면접."), M("What does the syllable 半 (반) mean?", "half", ["seeking", "use", "book"], "절반."), M("What does the syllable 用 (용) mean?", "use", ["seeking", "half", "face"], "고용."), M("What does the syllable 書 (서) mean?", "book; document", ["use", "half", "face"], "이력서.")
           , M("Which word is similar to 표면?", "겉", ["안", "위", "아래"], "The outside."), M("Which word is similar to 지원서?", "신청서", ["인증서", "신고서", "보고서"], "An application."), M("Which word is similar to 전반적?", "대체로", ["하반기", "후반전", "부분적"], "On the whole."), M("Which word is similar to 고용?", "채용", ["악용", "전용", "유용"], "Hiring."), M("Which word covers 이력서, 증명서, 신고서?", "서류", ["방면", "이용", "품목"], "Documents."), M("Which word covers 정면, 후면, 측면?", "방면", ["서류", "이용", "세면도구"], "Direction."), M("Which word covers 비누, 치약, 면도기?", "세면도구", ["서류", "방면", "이용"], "Toiletries."), M("Which word covers 애용, 활용, 전용?", "이용", ["서류", "방면", "품목"], "Use.")
           , F("여권을 ___하다. (to carry)", "소지", ["우대", "제출"], "소지하다."), F("외국인을 ___하다. (to give preferential treatment)", "우대", ["기피", "접수"], "우대하다."), F("병역을 ___하다. (to avoid)", "기피", ["소지", "도입"], "기피하다."), F("서류를 ___하다. (to submit)", "제출", ["소지", "감축"], "제출하다."), F("종업원을 ___하다. (to reduce)", "감축", ["제출", "우대"], "감축하다.")]
        + [read_q("여권을 소지하다"), read_q("새 제도를 도입하다"), read_q("병역을 기피하다"), read_q("원서를 접수하다")]
    ),
)

# ================================================================== L2 Part 1
_GRAPH3 = [
    ("전반적으로 실업률이 감소하고 있다.", "Overall, the unemployment rate is decreasing."),
    ("청년 실업률은 전체 실업률과 비교할 때 심각한 문제는 아니다.", "Compared with the overall unemployment rate, the youth unemployment rate is not a serious problem."),
    ("이천십 년 들어서 실업률이 급격하게 증가했다.", "The unemployment rate has risen rapidly since 2010."),
    ("노동시장에서 비정규직의 비중은 대학생들의 선호도에 비해서 매우 작다.", "The share of non-regular workers in the labor market is very small compared with college students’ preference."),
    ("노동시장에서 대기업의 비중은 십이 점 구 퍼센트밖에 안 된다.", "The share of large companies in the labor market is only 12.9 percent."),
    ("대학생들의 중소기업과 중견기업에 대한 선호도는 비슷한 수준이다.", "College students’ preference for small and medium-sized companies and for mid-level companies is at a similar level."),
]
_FAIR3 = [
    ("도전 플러스, 일자리 플러스. 서울시, 국내 최대 규모 일자리 박람회 개최", "Challenge Plus, Jobs Plus. The Seoul city government holds the largest job fair in Korea."),
    ("서울시, 세텍에서 이천십 년 서울 일자리 박람회 개최", "The Seoul city government holds the 2010 Seoul Job Fair at SETEC."),
    ("구 월 십사 일부터 나흘간 오프라인 박람회, 팔 월 십육 일부터 십일 월 삼십 일까지 온라인 박람회 진행", "An offline fair for four days from September 14, and an online fair from August 16 to November 30."),
    ("우수인재 박람회 현장 채용 실시, 구직자 세분화해 전문채용프로그램 제공, 구직자에겐 이력서 및 자기소개서 무료컨설팅 실시, 전문가 상담도 진행", "On-site hiring at the talent fair, specialized hiring programs offered by segmenting job seekers, free consulting on resumes and self-introductions for job seekers, and expert counseling as well."),
    ("서울시민들의 일자리를 찾아 주기 위해 서울시가 대규모 만남의 장을 마련한다.", "To find jobs for Seoul citizens, the Seoul city government prepares a large-scale meeting place."),
    ("서울시가 단독으로 주최하는 서울 일자리 박람회는 총 이천 개 구인기업과 이십만 명의 구직자가 참가하는 국내 최대 규모로서, 구 월 행사에 앞서 오는 팔 월 십육 일부터 십일 월 삼십 일까지 온라인에서도 병행하여 박람회가 진행된다.", "The Seoul Job Fair, hosted by the Seoul city government alone, is the largest in Korea, with a total of 2,000 recruiting companies and 200,000 job seekers taking part, and ahead of the September event it is also run in parallel online from August 16 to November 30."),
]
_SPEAK3 = [("군대에 입대하기 전에 어떤 일을 했습니까?", "What work did you do before you entered the military?"), ("아르바이트나 직장 경험에 대해서 옆 친구와 이야기해 보세요.", "Talk with the friend next to you about your part-time job or workplace experience.")]
L2 = lesson(
    "U18 L3 · Part 1 (도입 학습): the wage peak system, graphs and a job fair",
    "도입 학습 · 임금피크제 · 실업률 · 정규직 · 비정규직 · 중견기업 · 일자리 박람회 · 구직자 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 임금피크제 (the salary peak system)", "The book’s note is in English. In short: Korea is aging rapidly, yet the average retirement age is under 60 (at local conglomerates 57.3 in 2010, according to Yonhap News). In 2001 the Korea Chamber of Commerce and Industry proposed the 임금피크제: aging workers are guaranteed the choice to keep working past retirement age at a salary lower than their peak salary. It is often seen as a win-win: businesses keep salary costs down for experienced workers and older workers keep earning. A few financial institutions started it in 2001 and it has become more and more popular since."),
        card("학습활동 1: statements about the graphs", "Two graphs (from Kyunghyang) about employment and unemployment come with six statements, of which you tick the ones that agree with the graphs. The graphs are pictures, so I cannot tell which statements are true; here are the statements, with my English (2010 and 12.9% are spelled in Hangul):", examples=passage(_GRAPH3)),
        card("학습활동 2: an advertisement for a job fair", "The book asks you to (1) complete a table of event dates, place and participants and (2) write in English the four special services and say which you would find most interesting. The advertisement (Hankyoreh), with the numbers spelled in Hangul, “SETEC” as 세텍 and “Plus” as 플러스; the English is mine:", examples=passage(_FAIR3)),
        card("My answers to 학습활동 2", "1. Event dates: offline fair for four days from September 14; online fair from August 16 to November 30. Place: SETEC (Seoul). Participants: 2,000 recruiting companies and 200,000 job seekers. 2. The four services: on-site hiring at the talent fair; specialized hiring programs for segmented groups of job seekers; free consulting on resumes and self-introductions; expert counseling. (Which is the most interesting is your choice.)"),
        card("말해 봅시다! (speaking)", "The book’s prompt (two sentences; the English is mine):", examples=passage(_SPEAK3)),
        card("Activities left out", "학습활동 3 (Listening, Writing, Speaking, track 001): a YTN news report on unemployment: in English you write how the newscaster defines 임금피크제, what the numbers 49세 and 56.7세 represent, who would prefer the system and why, its advantages for employer and employee, and in Korean at least two reasons why you think it could be a good solution for unemployment. It is video and audio."),
    ],
    exercises=uniq(
        _tr(_GRAPH3, k=3) + _tr(_FAIR3, k=3) + _tr(_SPEAK3, k=2)
        + [M("What does 임금피크제 let aging workers do?", "Keep working past retirement age at a lower salary than their peak", ["Retire early with a bonus", "Work only part time at the same salary", "Work abroad"], "Salary peak system."), M("When was the system proposed by the Korea Chamber of Commerce and Industry?", "2001", ["2010", "1997", "1988"], "In 2001."), M("Which city government holds the job fair in the ad?", "Seoul", ["Busan", "Daegu", "Incheon"], "서울시."), M("How many recruiting companies take part in the fair?", "2,000", ["20,000", "200", "200,000"], "이천 개."), M("How many job seekers take part?", "200,000", ["2,000", "20,000", "2,000,000"], "이십만 명."), M("Until when does the online fair run?", "November 30", ["September 14", "August 16", "December 31"], "십일 월 삼십 일.")]
        + [F("서울 일자리 ___회 (a job fair)", "박람", ["회의", "박수"], "박람회."), F("구인기업과 ___가 참가한다. (job seekers)", "구직자", ["구인자", "고용자"], "구직자."), F("노동시장에서 ___의 비중은 매우 작다. (non-regular workers)", "비정규직", ["대기업", "정규직"], "비정규직."), F("실업률이 ___하게 증가했다. (rapidly)", "급격", ["점진", "서서"], "급격하게.")]
        + [read_q("전반적으로 실업률이 감소하고 있다"), read_q("노동시장에서 비정규직의 비중은 매우 작다"), read_q("서울시가 단독으로 일자리 박람회를 주최한다"), read_q("군대에 입대하기 전에 어떤 일을 했습니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("급격하게", "(急激) rapidly; suddenly; drastically", "우리 사회는 급격하게 변화하고 있습니다.", "빠르게"),
        ("정규직", "(正規職) a regular position; a permanent job", "신규 일자리를 모두 정규직으로 만들겠다고 합니다.", "비정규직, 임시직"),
        ("중견", "(中堅) mid-level; of middle standing; leading; the backbone (of an organization)", "중견 기업. 중견 간부."),
    ]),
    ("학습활동 2", [
        ("개최(하다/되다)", "(開催) holding or hosting an event (to hold or host an event/to be held or hosted)", "다음 월드컵은 어디에서 개최됩니까?", "열다, 열리다"),
        ("단독", "(單獨) exclusive; sole; lone", "단독 인터뷰. 단독 책임.", "공동, 합동"),
        ("세분화(하다/되다)", "(細分化) subdividing; categorizing (to subdivide; to categorize/to be subdivided; to be categorized)", "저희 회사는 고객에 따라 세분화된 서비스를 제공하고 있습니다.", "전문화"),
        ("인재", "(人材) a talented person; a capable person; an outstanding individual", "디엘아이 학생들은 국방부의 인재들입니다.", "인력"),
        ("장", "(場) a venue; a place; a stage", "이번 행사는 남북한 이산가족들에게 만남의 장이 되었다."),
    ]),
    ("학습활동 3", [
        ("기여(하다)", "(寄與) contribution (to contribute [to])", "김수연 씨는 우리 회사에 입사하면 어떤 기여를 할 수 있습니까?", "공헌하다"),
        ("명예퇴직", "(名譽退職) voluntary resignation; early retirement; “honorary retirement”", "요즘은 사십 대에 명예퇴직을 많이 합니다.", "명퇴, 조기퇴직"),
        ("선언(하다)", "(宣言) announcement; declaration (to announce; to declare)", "김 교수님은 서울 시장에 출마하겠다고 선언했습니다.", "발표하다"),
        ("절감(하다/되다)", "(節減) retrenchment; the cutting of expenses (to retrench; to cut down/to be retrenched; to be cut down)", "기업들은 비용을 절감하기 위해 해외에서 제품을 생산하기도 합니다.", "줄다, 감소하다 / 늘다, 증가하다"),
        ("정리해고(하다/되다)", "(整理解雇) layoff (caused by company restructuring) (to lay off/to be laid off)", "그 회사에서 오만 명을 정리해고 하겠다고 발표하자 직원들이 이에 반대하는 시위를 하고 있습니다."),
        ("지점장", "(支店長) a manager of a branch (office)", ""),
        ("직위", "(職位) one’s position or office", "그 사람은 뇌물수수 혐의로 직위해제 되었습니다.", "직책, 지위"),
        ("체감(하다)", "(體感) feeling (changes); sensing; “bodily feeling” (to feel; to sense)", "요즘 쇼핑을 해 보면 체감 물가는 정부가 발표한 물가보다 훨씬 높게 느껴져요. 운동을 시작한 후부터 몸의 변화를 체감합니다.", "느낌, 느끼다"),
        ("측면", "(側面) the side; the flank", "이번 문제는 여러 가지 측면에서 분석해 봐야 한다."),
        ("판단(하다)", "(判斷) judgment; decision (to judge; to decide)", "상황 판단을 잘 못하겠어요.", "정하다, 결정하다"),
    ]),
]
L3 = lesson(
    "U18 L3 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 급격하게 · 정규직 · 중견 · 개최 · 단독 · 세분화 · 인재 · 기여 · 명예퇴직 · 선언 · 절감 · 정리해고 · 직위 · 체감 · 측면 · 판단",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives two example phrases for 중견 and 단독, which I joined with a period. 절감 lists 줄다, 감소하다 as similar words and 늘다, 증가하다 as opposites; I joined them with a slash. 지점장 has no example in the book. 인재 has the abbreviation DLI in its example, which I spelled in Hangul (디엘아이), and 40대 and 5만 명 in the examples are spelled out (사십 대, 오만 명).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=12)),
)

# ================================================================== L4 Part 2
_STAT3 = [
    ("오 월 취업자가 삼십육만 명 늘었지만 이십 대 청년 취업자는 십만 명 가까이 줄어 청년 실업이 심각해지고 있는 것으로 나타났다.", "Although the number of employed in May rose by 360,000, the number of employed young people in their twenties fell by nearly 100,000, which shows that youth unemployment is becoming serious."),
    ("경제활동이 활발한 삼십 대 취업자도 감소세를 보였다.", "The number of employed in their thirties, who are economically active, also showed a downward trend."),
    ("십오 일 통계청이 발표한 오 월 고용동향에 따르면 전체 고용지표는 회복세를 이어 가고 있는 것으로 조사됐다.", "According to the May employment trends announced by Statistics Korea on the 15th, the overall employment indicators were found to be continuing their recovery."),
    ("오 월 취업자는 지난해 같은 달 보다 삼십오만 오천 명, 일 점 오 퍼센트 늘어난 이천사백육십육만 천 명으로 사상 최대를 기록했다.", "The number of employed in May, 24,661,000, up 355,000 (1.5 percent) from the same month last year, was a record high."),
    ("취업자는 지난해 시월 이후 여덟 개월 연속 매월 삼십만 명 이상 증가하고 있다.", "The number of employed has been rising by more than 300,000 every month for eight months in a row since last October."),
    ("산업별로는 수출 호조가 이어지고 있는 제조업 취업자 수가 전년 동월 대비 십만 천 명 늘었고, 서비스업은 이십육만 명 증가했다.", "By industry, the number of employed in manufacturing, where good exports continue, rose by 101,000 over the same month of the previous year, and in services by 260,000."),
    ("특히 이십 대 취업자는 삼백칠십이만 이천 명으로 지난해 같은 달 삼백팔십이만 천 명보다 구만 팔천 명 감소했다.", "In particular, the number of employed in their twenties was 3,722,000, a decrease of 98,000 from 3,821,000 in the same month last year."),
    ("삼십 대 취업자도 만 오천 명 감소한 오백팔십사만 삼천 명으로 조사됐다.", "The number of employed in their thirties was also found to be 5,843,000, down by 15,000."),
    ("비경제활동인구 중 구직활동 대신 취업학원 등에 다니는 취업준비자들은 오십팔만 팔천 명으로 구만 천 명 줄었다.", "Among the economically inactive population, those preparing for employment who attend job-training academies instead of looking for work numbered 588,000, down by 91,000."),
    ("올해 경기가 회복되면서 취업준비를 하던 사람들이 본격적으로 구직활동에 나섰기 때문이라고 통계청은 설명했다.", "Statistics Korea explained that this is because, as the economy recovered this year, people who had been preparing for employment started in earnest to look for jobs."),
    ("실업자는 팔십일만 구천 명으로 이만 육천 명, 삼 점 삼 퍼센트 증가했고, 실업률은 삼 점 이 퍼센트로 전년 동월과 동일했다.", "The number of unemployed rose by 26,000 (3.3 percent) to 819,000, and the unemployment rate was 3.2 percent, the same as in the same month of the previous year."),
]
_TAB3 = [["Overall employment", "increase", "up 355,000 (1.5%) to 24,661,000, a record high"], ["Employment in manufacturing", "increase", "up 101,000"], ["Employment in the service sector", "increase", "up 260,000"], ["Employment of people in their 20s", "decrease", "down 98,000 to 3,722,000"], ["Employment of people in their 30s", "decrease", "down 15,000 to 5,843,000"], ["Active job seekers", "increase", "the article gives only those preparing for jobs (down 91,000 to 588,000), who turned to active job hunting"], ["Overall unemployment", "increase", "unemployed up 26,000 (3.3%) to 819,000; the rate stayed at 3.2%"]]
_CASE1 = [
    ("사 년 전 대학을 졸업한 한 남성은 서울 상위권 대학을 졸업한 후 첫 직장으로 여성용품을 만드는 중소기업에 입사했지만 반년 만에 그만뒀다.", "A man who graduated from university four years ago, after graduating from a top-ranked university in Seoul, joined a small company making women’s goods as his first job but quit within half a year."),
    ("급여가 기대에 크게 못 미친 데다 미래도 불투명하다는 게 이유였다.", "The reason was that the pay fell far short of his expectations and that the future was also unclear."),
    ("그는 이후 삼 년간 공시족, 즉 공무원시험 준비족으로 살아 왔다.", "Since then he had lived for three years as a 공시족, that is, a person preparing for the civil service exam."),
    ("시험 낙방이 되풀이됐고 생활비와 학원비도 감당하기 어렵게 되자 결국 최근에는 이마저도 포기한 채 백수가 됐다.", "Failures in the exam were repeated, and when living costs and academy fees became hard to bear, in the end he recently gave up even this and became jobless."),
    ("그는 어디서부터 뭘 어떻게 해야 할지 모르겠다며 씁쓸해했다.", "He said bitterly that he did not know where to start or what to do and how."),
]
_CASE2 = [
    ("서울의 사 년제 대학을 다니는 한 여학생은 올해 오 학년을 다닌다.", "A female student at a four-year university in Seoul is in her “fifth year” this year."),
    ("졸업학점은 지난해 다 채웠지만 취업이 안 돼 졸업을 한 학기 늦추기로 한 것이다.", "She completed her graduation credits last year, but because she could not find a job she decided to put off graduation by one semester."),
    ("겨울방학에도 매일 오전 학교 도서관으로 가 외국어와 기업체 인성과 적성 시험 준비를 하고 밤늦게 돌아오는 날의 연속이다.", "Even during the winter vacation, she goes to the school library every morning to prepare for foreign languages and companies’ character and aptitude tests, and returns late at night, day after day."),
    ("지난 학기에 기업체 수십 곳에 지원했지만 안 돼 이번이 마지막이란 심정으로 준비하고 있다고 그 학생은 말했다.", "The student said that she had applied to dozens of companies last semester without success and is now preparing with the feeling that this is the last time."),
    ("졸업을 유예하거나 졸업하고 취업준비에 몰두하는 친구들이 주변에 수두룩하다.", "There are plenty of friends around her who postpone graduation or graduate and devote themselves to job preparation."),
    ("취업이 어려우니까 부모님도 우리에게 부담을 주지 않으려고 하지만 갑갑한 것은 똑같다.", "Since finding work is hard, our parents try not to put pressure on us, but we feel just as stifled."),
]
_SPEAK3B = [("현재 미국의 청년들의 취업 및 실업 문제에 대해 생각해 보고 그 해결책에 대해서도 생각해 보세요.", "Think about the employment and unemployment problems of young people in the United States today and also think about solutions to them."), ("그리고 옆 사람과 이야기해 보세요.", "Then talk about it with the person next to you.")]
L4 = lesson(
    "U18 L3 · Part 2 (본 학습): employment statistics and youth unemployment",
    "본 학습 · 취업 통계 · 취업자 · 실업률 · 청년 실업 · 공시족 · 낙방 · 취업준비 · 졸업 유예 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a newspaper article on employment statistics (Hankyoreh)", "The book asks you to tick increase or decrease for seven items in a table and write the detailed statistics beside each. The article’s figures are spelled in Hangul; the English is mine:", examples=passage(_STAT3)),
        card("My answers to 학습활동 1", "The book’s table has seven rows. The article does not quite name the “active job seekers” row; I read it from the part about those preparing for jobs:", tables=[table(["Item", "Increase / decrease", "Detailed statistics"], _TAB3)]),
        card("학습활동 2, case 1: a graduate who gave up on exams", "The book has the pair read one case each, summarize it in English and retell it in Korean to the partner. The book gives the man’s pseudonym, age and school type; because he is a private person I wrote “a man” and “he”. The case (Kyunghyang), with my English:", examples=passage(_CASE1)),
        card("학습활동 2, case 2: a student in her “fifth year”", "Likewise the student’s name, initial and age are dropped. The case, with my English (the book’s quotation marks around her words are removed, and 인·적성 is written 인성과 적성):", examples=passage(_CASE2)),
        card("My English summaries for 학습활동 2", "Case 1: after graduating from a top Seoul university he left his first job at a small company within six months because of low pay and an unclear future, then spent three years preparing for the civil service exam, failed repeatedly, could not afford living and academy costs, and has now given up and is jobless and bitter. Case 2: a female university student delayed graduation by a semester because she could not find a job, studies every day at the library for foreign languages and company aptitude tests, applied to dozens of companies without success, and says many friends are in the same position and that her parents try not to pressure her but everyone feels stifled."),
        card("말해 봅시다! (speaking)", "The book’s prompt (two sentences; the English is mine):", examples=passage(_SPEAK3B)),
        card("Activities left out", "학습활동 3 (Listening, Speaking): part of a speech by President Lee Myung-bak (YTN). Track 002: you write in English what social issue he speaks about, to whom he expresses his concerns and what his message is. Track 003: you write what personal experience he tells and its implication, translate into English two sentences from the speech (세상에 경험만큼 좋은 스승은 없습니다; 젊은 나이에 얻었던 경험이 이후에 난관을 겪을 때 마다 두고두고 도움이 되었습니다) and then share what you learned from your own workplace experience. They are audio. The two sentences can be read: “There is no teacher as good as experience” and “The experience I gained at a young age helped me again and again whenever I went through difficulties afterwards.”"),
    ],
    exercises=uniq(
        _tr(_STAT3, k=3) + _tr(_CASE1, k=3) + _tr(_CASE2, k=3)
        + [M("How many more people were employed in May than a year earlier?", "355,000", ["36,000", "3,550,000", "101,000"], "삼십오만 오천 명."), M("What was the unemployment rate?", "3.2 percent", ["3.3 percent", "1.5 percent", "8 percent"], "삼 점 이 퍼센트."), M("Which age group’s employment fell by about 100,000?", "People in their twenties", ["People in their thirties", "People in their forties", "All ages"], "이십 대."), M("What does 공시족 mean?", "People preparing for the civil service exam", ["People who change jobs often", "People studying abroad", "Retired people"], "공무원시험 준비족."), M("Why did the student delay her graduation?", "She could not find a job", ["She was ill", "She lacked credits", "She went abroad"], "취업이 안 돼."), M("Why did Statistics Korea say fewer people were preparing for jobs?", "They started actively looking for jobs as the economy recovered", ["They gave up", "They emigrated", "They enrolled in schools"], "경기가 회복되면서.")]
        + [F("전체 고용지표는 ___세를 이어 가고 있다. (recovery)", "회복", ["감소", "하락"], "회복세."), F("수출 ___가 이어지고 있다. (a favorable trend)", "호조", ["지표", "동향"], "수출 호조."), F("시험 ___이 되풀이됐다. (failure in an exam)", "낙방", ["유예", "포기"], "낙방."), F("졸업을 ___하거나 취업준비에 몰두하는 친구들. (to postpone)", "유예", ["낙방", "포기"], "유예하다.")]
        + [read_q("오 월 취업자가 삼십육만 명 늘었다"), read_q("이십 대 청년 취업자는 십만 명 가까이 줄었다"), read_q("시험 낙방이 되풀이됐다"), read_q("졸업을 유예하는 친구들이 주변에 수두룩하다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("동향", "(動向) a (general) trend; tendency; “moving direction”", "우리는 한 달에 두 번씩 시장 동향을 조사합니다.", "경향, 추세"),
        ("~세", "(usually combined with a noun and showing an increase/decrease) a trend of ~; the tendency of ~; “power of ~”", "증가세, 감소세, 폭등세 등.", ""),
        ("지표", "(指標) an index; indices", "경제 지표들이 상승 곡선을 그리고 있습니다."),
        ("취업(하다)", "(就業) getting a job; employment (to find/get a job)", "요즘은 취업이 너무 어렵습니다.", "취직, 실업, 실직, 취업자, 취업인구"),
        ("호조", "(好調) a favorable (economic) trend; a favorable tendency", "최근 수출이 호조를 보이면서 경제가 좋아지고 있습니다."),
    ]),
    ("학습활동 2", [
        ("가명", "(假名) a pseudonym; an alias; “a false name”", "그 사람이 본인 이름이라고 밝힌 김신우는 가명인 것으로 드러났습니다.", "실명, 성명, 별명, 익명, 필명, 예명"),
        ("낙방(하다)", "(落榜) failure (on an examination/test) (to fail an exam)", "제 친구는 대학입시에서 낙방하고 바로 군대에 갔어요.", "떨어지다, 실패하다, 낙제하다 / 붙다, 합격하다"),
        ("되풀이(하다/되다)", "repetition; reiteration (to repeat/to be repeated)", "저는 똑같은 실수를 되풀이하고 싶지 않아요.", "반복하다"),
        ("미치다", "to reach; to meet; to match up to; to affect; to influence", "야채 공급이 수요에 못 미치고 있습니다.", "미치지 못하다, 못 미치다"),
        ("상위권", "(上位圈) a high (upper) bracket/category", "우리 아들 성적은 반에서 상위권에 속해요.", "하위권, 중위권"),
        ("수두룩하다", "(colloquial) to be lots of; to be plenty of", "요즘 취업 못한 젊은이들이 어디에나 수두룩합니다.", "많다, 흔하다"),
        ("심정", "(心情) one’s feelings; one’s heart", "지금 심정이 어떠십니까?", "기분, 감정"),
        ("씁쓸하다", "to be (somewhat) bitter", "진실을 알고 나니 좀 씁쓸합니다."),
        ("연속", "(連續) (in) continuation; (in) sequence; in a row", "샌프란시스코 자이언츠 팀은 다섯 경기에서 연속 승리를 거두었다."),
        ("유예(하다/되다)", "(猶豫) postponement; deferral (to postpone; to suspend/to be postponed; to be suspended)", "형 집행을 일 년간 유예한다.", "연기하다"),
        ("인성", "(人性) character; personality; human nature", "교육부는 학생들의 인성을 강화하겠다고 발표했습니다.", "적성, 성격"),
        ("포기(하다)", "(抛棄) abandonment; giving up (to abandon; to give up)", "상황이 어려워도 포기하지 말고 끝까지 해 봅시다.", "그만두다"),
    ]),
    ("학습활동 3", [
        ("건설(하다/되다)", "(建設) construction; building (to build; to construct/to be built; to be constructed)", "요즘 건설 경기가 좋지 않습니다.", "짓다, 세우다, 만들다"),
        ("고달프다", "to be weary; to be exhausted/exhausting; to be very tired/tiring", "직장생활이 너무 고달픕니다."),
        ("난관", "(難關) a difficult impasse; a dead end", "사건 수사가 난관에 부딪쳤어요.", "어려움"),
        ("~ 남짓", "(a little) more than; over", "집에서 학교까지 한 시간 남짓 걸립니다."),
        ("밀림", "(密林) a jungle; a dense forest", "이 지역은 밀림지역입니다."),
        ("신발 끈을 조이다", "(idiom) to make a fresh resolution; to reestablish or solidify one’s determination; to roll up one’s sleeves; “to tighten up the shoestring”", "이제 새롭게 신발 끈을 조이고 열심히 노력합시다."),
        ("움츠리다", "to flinch; to cower", "추워서 어깨를 움츠렸다."),
        ("탓하다", "to blame", "남을 탓하기 전에 자신의 잘못을 돌아보세요.", "비난하다"),
        ("해법", "(解法) a solution", "이 문제에 대해 특별한 해법을 찾을 수 없습니다.", "방법, 해결책"),
    ]),
]
L5 = lesson(
    "U18 L3 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 동향 · 지표 · 취업 · 호조 · 가명 · 낙방 · 되풀이 · 미치다 · 상위권 · 수두룩하다 · 심정 · 씁쓸하다 · 연속 · 유예 · 인성 · 포기 · 건설 · 고달프다 · 난관 · 남짓 · 밀림 · 신발 끈을 조이다 · 움츠리다 · 탓하다 · 해법",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book also lists 동향 (同鄕), “(from) the same native place”, as a homonym of 동향, and 지표 (地表), “the surface (of the earth)”, as a homonym of 지표; for 미치다 it notes the homonym “to be crazy; to be deranged”. 낙방 lists 떨어지다, 실패하다, 낙제하다 as similar and 붙다, 합격하다 as opposites (I joined them with a slash). The examples of 연속 and 유예 had digits in the book (5경기, 1년간), spelled out here. ~세 and ~ 남짓 are written with the book’s tilde; 고달프다 and several others have no similar words listed.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=20, nread=16)),
)

# ================================================================== L6 Part 3
_EDIT3 = [
    ("노동자들을 위한 기념일이지만 비정규직은 서럽고, 실업자는 소외되고, 정규직은 불편한 날이 노동절이다.", "Labor Day is a commemoration day for workers, but a day on which the non-regular worker is sad, the unemployed is excluded and the regular worker is uncomfortable."),
    ("고용위기는 더 이상 방치하기 힘든 지점에 이르렀다.", "The employment crisis has reached a point where it is hard to leave it alone any longer."),
    ("비정규직이 전체 노동자의 삼분의 이에 육박하고, 경제활동인구의 일곱 명 중 한 명이 사실상 실업자다.", "Non-regular workers are close to two thirds of all workers, and one in seven of the economically active population is in effect unemployed."),
    ("이는 개인 삶의 위기만이 아니다.", "This is not only a crisis in individuals’ lives."),
    ("내수기반을 무너뜨려 성장잠재력을 갉아먹는 국민경제의 위기이자 양극화를 심화시키는 민주주의의 위기이다.", "It is a crisis of the national economy, which destroys the base of domestic demand and eats away growth potential, and a crisis of democracy, which deepens polarization."),
    ("그런데도 정부는 대안이 없다며, 임금을 깎고 비정규직만 더 늘리려 할 뿐이다.", "Even so, the government says there is no alternative and only tries to cut wages and increase non-regular workers."),
    ("물론 어둡기만 하지는 않다.", "Of course it is not only dark."),
    ("올 노동절에는 새로운 풍경이 더해졌다.", "A new scene was added to this year’s Labor Day."),
    ("비정규직 철폐를 위한 노조와 시민단체 미행은 노동절에 앞서 구 일간 자전거를 타고 전국 비정규직 투쟁 사업장을 방문하는 질주란 행사를 벌였다.", "Mihaeng, a labor union and civic group for abolishing non-regular work, held an event called “Dash” ahead of Labor Day, in which for nine days they rode bicycles to visit workplaces across the country where non-regular workers were struggling."),
    ("개별 사업장을 넘어 비정규직 문제를 공론화한 첫 시도였다.", "It was the first attempt to bring the non-regular work problem into public debate beyond individual workplaces."),
    ("청년실업의 대안을 찾는 이십 대 당사자 단체 희망청은 일하지 않는 사람들의 메이데이란 행사를 열었다.", "Huimangcheong, a group of those concerned in their twenties looking for alternatives to youth unemployment, held an event called “May Day of People Who Do Not Work.”"),
    ("주어진 일자리가 아니라 스스로 하고 싶은 일터를 만들어 보자고 나선 것이다.", "They stepped forward to propose creating, not a given job, but a workplace they themselves want to work at."),
    ("이는 절망의 가장 깊은 곳에서 돋는 희망의 신호라고도 할 수 있다.", "This can also be called a sign of hope sprouting from the deepest place of despair."),
    ("비정규직과 청년실업의 심각성은 새삼스러운 게 아니다.", "The seriousness of non-regular work and youth unemployment is nothing new."),
    ("하지만 진정 심각한 문제는 고용위기가 너무 크고 복잡해서 대안이 없다고 여기는 사회의 냉소주의와 자포자기에 있다.", "But the truly serious problem lies in society’s cynicism and giving up in despair, which consider that there is no alternative because the employment crisis is too big and complicated."),
    ("대안과 해법은 찾아 내고 발견하는 것이지 하늘에서 떨어지는 게 아니다.", "Alternatives and solutions are things you find and discover; they do not fall from the sky."),
    ("대안은 정부가 고용안정으로 정책기조를 바꾸고 기업에 고통분담을 강제할 때, 그리고 정규직이 비정규직 실업자들과 연대할 때 발견될 수 있다.", "Alternatives can be found when the government changes the policy basis to job stability and forces companies to share the pain, and when regular workers show solidarity with non-regular workers and the unemployed."),
]
_SPEAK3C = [("미국의 고용시장에서는 비정규직, 파트타임, 풀타임 직원으로 일할 때 어떤 차이들이 있는지 생각해 보세요.", "Think about what differences there are in the American job market between working as a non-regular, part-time or full-time employee."), ("또 미국 고용시장의 가장 큰 문제가 무엇인지 생각해 보고 옆 친구와 의견을 교환해 보세요.", "Also think about what the biggest problem of the American job market is and exchange opinions with the friend next to you.")]
L6 = lesson(
    "U18 L3 · Part 3 (심화 학습): an editorial on the employment crisis",
    "심화 학습 · 고용위기 · 노동절 · 비정규직 · 청년실업 · 희망의 신호 · 냉소주의 · 자포자기 · 대안 · 고통분담 · 연대 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a newspaper editorial on the employment crisis (Kyunghyang)", "The book has four questions in English: how serious the situation in the first paragraph is; the two examples of the underlined “sign of hope”; the two things the underlined “truly serious problem” refers to; and the two solutions the author proposes. The underlines are not marked in the text, but the phrases named in the questions are clear. The editorial’s figures are spelled in Hangul and I wrote 노조와 시민단체 for “노조·시민단체”; the organizations’ names are the book’s as I could read them. The English is mine:", examples=passage(_EDIT3)),
        card("My answers to 학습활동 2", "1. Very serious: non-regular workers are close to two thirds of all workers and one in seven of the economically active population is in effect unemployed; it is a crisis of individual lives, of the national economy (the base of domestic demand) and of democracy (polarization). 2. The two examples of the sign of hope: the group Mihaeng’s nine-day bicycle “Dash” to workplaces where non-regular workers struggle, and the young people’s group Huimangcheong’s “May Day of People Who Do Not Work”, which proposed creating workplaces they want. 3. The truly serious problem is society’s cynicism (냉소주의) and its giving up in despair (자포자기). 4. The government should change its policy basis to job stability and force companies to share the pain, and regular workers should show solidarity with non-regular workers and the unemployed."),
        card("말해 봅시다! (speaking)", "The book’s prompt (two sentences; the English is mine):", examples=passage(_SPEAK3C)),
        card("Activities left out", "학습활동 1 (Listening, Speaking, Writing): parts of a YTN television program on employment, in three segments (tracks 004, 005, 006). You answer in English which two social problems are mentioned and what program is being implemented to solve them; fill a table with the preconceptions of three college seniors about small and medium-size companies (interviewees 이호영, 김효태, 방지나) and then what they say after experiencing them (김효태, 방지나, 이지형), guessing before watching; and write in Korean three reasons for your evaluation of the program and your own ideas. It is video and audio."),
    ],
    exercises=uniq(
        _tr(_EDIT3, k=3)
        + [M("What fraction of all workers are non-regular workers, according to the editorial?", "Close to two thirds", ["One seventh", "Half", "One tenth"], "삼분의 이에 육박."), M("How many of seven economically active people are in effect unemployed?", "One", ["Two", "Seven", "Three"], "일곱 명 중 한 명."), M("What did Mihaeng do for nine days?", "Rode bicycles to visit workplaces of struggling non-regular workers", ["Went on a hunger strike", "Held a job fair", "Wrote petitions"], "질주."), M("What do the editorial’s two “signs of hope” show?", "People trying to find alternatives themselves", ["The government’s new policy", "A fall in unemployment", "Company bonuses"], "희망의 신호."), M("What does the editorial call the truly serious problem?", "Cynicism and giving up in despair", ["Low wages", "A lack of jobs abroad", "Too many graduates"], "냉소주의와 자포자기."), M("Whom must the government force to share the pain?", "Companies", ["Students", "Unions", "Consumers"], "기업에 고통분담을 강제.")]
        + [F("정부가 정책___를 고용안정으로 바꿔야 한다. (basis)", "기조", ["기반", "대안"], "정책기조."), F("정규직이 비정규직과 ___할 때 대안이 발견될 수 있다. (to show solidarity)", "연대", ["투쟁", "소외"], "연대하다."), F("비정규직은 서럽고 실업자는 ___된다. (to be excluded)", "소외", ["연대", "분담"], "소외되다."), F("절망의 가장 깊은 곳에서 ___는 희망의 신호. (to sprout)", "돋", ["서럽", "육박"], "돋다.")]
        + [read_q("비정규직이 전체 노동자의 삼분의 이에 육박한다"), read_q("고용위기는 더 이상 방치하기 힘든 지점에 이르렀다"), read_q("대안과 해법은 하늘에서 떨어지는 게 아니다"), read_q("정규직이 비정규직 실업자들과 연대할 때 대안이 발견될 수 있다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("습득(하다/되다)", "(習得) acquisition (through study/learning) (to acquire/to be acquired)", "어린아이들은 어른보다 언어습득에 유리하다.", "배우다"),
        ("혁신(하다/되다)", "(革新) innovation (to innovate/to be innovated)", "품질 혁신을 통해 경쟁력을 강화해야 한다."),
        ("딸리다/달리다", "(colloquial) to be short of; to be lacking in (power, money, capacity, etc.)", "요즘 저희 회사에 일손이 딸려서 야근을 해야 해요.", "부족하다, 모자라다"),
        ("일터", "a workplace", "노동부에서 장애인들에게 일터를 마련해 준다고 합니다.", "직장"),
    ]),
    ("학습활동 2", [
        ("강제(하다)", "(强制) compulsion; coercion (to force; to coerce)", "기체에 문제가 생겨서 강제 착륙을 해야 합니다.", "강요하다"),
        ("공론", "(公論) public or general opinion", "야당 대표는 이 문제에 대해 공론에 부치겠다고 했습니다.", "여론"),
        ("기반", "(基盤) a base; a footing; a foothold", "이 기업은 재정적 기반이 튼튼하다.", "기초"),
        ("기조", "(基調) a central fact; a basis", "정상회담 이후로 남북간에 평화와 협력의 기조가 마련되었다."),
        ("내수", "(內需) domestic demand or consumption", "경기침체로 인하여 내수가 감소했다."),
        ("냉소주의", "(冷笑主義) cynicism", "이 사회에 팽배한 냉소주의가 큰 문제입니다."),
        ("노조", "(勞組) a labor union", "노조 지도부는 파업을 결의했습니다.", "노동조합"),
        ("대안", "(代案) an alternative (plan, idea, etc.)", "현실적인 대안을 제시해 주세요.", "방안"),
        ("돋다", "to come up; to bud; to sprout", "새롭게 희망이 돋는 것을 느꼈다."),
        ("분담(하다)", "(分擔) dividing/sharing (of labor or expense); “fractional burdening” (to divide [up]; to share)", "식사비용은 모두가 분담합시다.", "나누다"),
        ("서럽다", "to be (vexed and) sad", "남자친구와 헤어지고 서럽게 웁니다.", "슬프다"),
        ("소외(시키다/되다)", "(疎外) isolation; exclusion (to isolate; to alienate; to exclude/to be isolated; to be alienated; to be excluded)", "소외된 이웃들을 위해 봉사를 하고 싶습니다."),
        ("연대(하다)", "(連帶) solidarity (to band together)", "개도국들은 한국에 대해 연대감을 느낀다고 합니다.", "함께 하다, 연합하다"),
        ("육박(하다)", "(肉薄) closing in upon; being close at hand (to close in upon; to be close at hand; to come near)", "이번 달 판매액이 십만 달러에 육박하고 있습니다."),
        ("자포자기(하다)", "(自暴自棄) giving up in despair (to give up in despair)", "범인은 실직 후 자포자기의 심정으로 범행을 저질렀다고 했습니다.", "포기, 절망"),
        ("절망(하다)", "(絶望) despair; hopelessness (to despair of; to lose hope)", "절망하지 말고 희망을 가지세요.", "희망"),
        ("투쟁(하다)", "(鬪爭) a fight; a struggle (to fight; to struggle)", "노동자들은 단식 투쟁을 벌이겠다고 했습니다.", "싸우다"),
    ]),
]
L7 = lesson(
    "U18 L3 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 습득 · 혁신 · 딸리다 · 일터 · 강제 · 공론 · 기반 · 기조 · 내수 · 냉소주의 · 노조 · 대안 · 돋다 · 분담 · 서럽다 · 소외 · 연대 · 육박 · 자포자기 · 절망 · 투쟁",
    requires=[],
    cards=[card("A note on the Korean in this list", "연대 has a homonym 연대 (聯隊), “a regiment”, in the book. 자포자기 lists 포기 and 절망 as similar words, and 절망 lists 희망 (hope) as its opposite. 딸리다/달리다 are given together as variants of the colloquial verb. The book writes 10만 달러 in the example of 육박 in digits, which I spelled out (십만 달러).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=18, nread=15)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 3: Employment (취업)", [L1, L2, L3, L4, L5, L6, L7])
