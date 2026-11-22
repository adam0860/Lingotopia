"""Unit 73: KBC Semester III, Unit 16, Lesson 8 - An Aging Society: Low Birthrates and Government Countermeasures (고령화 사회: 저출산과 정부의 대책).
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
_MATCH8 = [("직장", "a workplace", "환경이 좋은 직장에서 근무하다"), ("저출산", "low birthrate", "저출산 문제가 심각하다"), ("노인", "an elderly person", "노인을 위한 무료공연을 열다"), ("복지", "welfare", "이 직장은 복지 시설이 좋다"), ("보험", "insurance", "자녀들을 위해 보험을 들다"), ("맞벌이 부부", "a working couple", "맞벌이 부부를 위한 탁아소를 운영하다"), ("사회", "a society", "고령화 사회로 들어서다"), ("양로원", "a nursing home", "양로원에서 자원 봉사하다"), ("추세", "a trend", "비만이 증가하는 추세다"), ("어린이", "children", "어린이 수영교실이 열리다"), ("건강", "health", "건강 상담을 받다"), ("정책", "a policy", "경제 정책을 결정하다")]
_HJ8 = [("低 저", "low", "저가, 저출산율"), ("老 노/로", "getting old", "노인, 양로원"), ("場 장", "place; yard", "시장, 직장"), ("院 원", "house; institute", "학원, 법원"), ("福 복", "luck; happiness", "복지, 행복")]
_HJW8 = [("저가", "low price"), ("저출산율", "a low birthrate"), ("노인", "an elderly person; a senior citizen"), ("양로원", "a nursing home"), ("시장", "a market"), ("직장", "a workplace"), ("학원", "a (private) educational institute"), ("법원", "a court; “law house”"), ("복지", "welfare"), ("행복", "happiness")]
_ENG8 = [("고저", "height; ups and downs"), ("저임금", "low wages"), ("저기압", "low (atmospheric) pressure"), ("노년", "old age"), ("생노병사", "birth, aging, sickness and death"), ("노후", "one’s later years"), ("공장", "a factory"), ("전시장", "an exhibition hall"), ("예식장", "a wedding hall"), ("동물원", "a zoo"), ("식물원", "a botanical garden"), ("고아원", "an orphanage"), ("복권", "a lottery ticket"), ("축복", "a blessing"), ("복지국가", "a welfare state")]
_SIM8 = [("최저", "최소", "the lowest: the minimum"), ("경로", "존대", "respect for the aged: treating with respect"), ("매장", "가게", "a store: a shop"), ("유아원", "유치원", "a nursery school: a kindergarten")]
_L8X = [("최다", "the most (in number)"), ("최고", "the highest; the best"), ("최장", "the longest"), ("최소", "the minimum"), ("존대", "treating with respect"), ("무시", "ignoring"), ("경사", "a slope; a happy occasion"), ("경치", "scenery"), ("가게", "a shop"), ("매매", "buying and selling"), ("매연", "exhaust smoke"), ("포장", "packaging"), ("유치원", "a kindergarten"), ("대학원", "a graduate school"), ("탁아소", "a day nursery"), ("보험", "insurance"), ("추세", "a trend"), ("정책", "a policy")]
L1 = lesson(
    "U16 L8 · Review: aging-society words and Sino-Korean 低 老 場 院 福",
    "고령화 사회: 저출산과 정부의 대책 · 단어 복습 · 한자어 복습 · 직장 · 저출산 · 노인 · 복지 · 보험 · 맞벌이 부부 · 양로원 · 추세 · 정책 · 低 老 場 院 福",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives twelve phrases with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH8], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ8], say=[2]), ktable(_HJW8)]),
        card("한자어 복습 1: the English meanings (my answers)", "Write the English meanings of these words (A. 고저, 저임금, 저기압; B. 노년, 생노병사, 노후; C. 공장, 전시장, 예식장; D. 동물원, 식물원, 고아원; E. 복권, 축복, 복지국가):", tables=[ktable(_ENG8)]),
        card("한자어 복습 2: the word with the closest meaning (my answers)", "Circle the word with the closest meaning to the word on the left (A. 최저: 최다, 최고, 최장, 최소; B. 경로: 존대, 무시, 경사, 경치; C. 매장: 가게, 매매, 매연, 포장; D. 유아원: 고아원, 유치원, 학원, 대학원).", tables=[table(["Word", "Closest (my answer)", "Meaning"], [list(r) for r in _SIM8], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L8X)]),
        card("Activities left out", "단어 복습 2 (Listening, track 001): part of a radio talk show on Korean society; you write the key words you hear and summarize the content. It is audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH8], k=3) + _tr(_HJW8, k=3) + _tr(_ENG8, k=3) + _tr(_L8X, k=3) + _tr([(a, c) for a, b, c in _SIM8], k=3)
        + [M("What does the syllable 低 (저) mean?", "low", ["old", "place", "luck"], "저가."), M("What does the syllable 老 (노/로) mean?", "getting old", ["low", "house", "luck"], "노인."), M("What does the syllable 場 (장) mean?", "place; yard", ["low", "old", "luck"], "시장."), M("What does the syllable 院 (원) mean?", "house; institute", ["low", "old", "luck"], "학원."), M("What does the syllable 福 (복) mean?", "luck; happiness", ["low", "old", "place"], "복지."),
           M("Which word means the same as 최저?", "최소", ["최다", "최고", "최장"], "The minimum."), M("Which word means the same as 경로?", "존대", ["무시", "경사", "경치"], "Treating with respect."), M("Which word means the same as 매장?", "가게", ["매매", "매연", "포장"], "A shop."), M("Which word means the same as 유아원?", "유치원", ["고아원", "학원", "대학원"], "A kindergarten."),
           F("자녀들을 위해 ___을 들었습니다. (insurance)", "보험", ["정책", "추세"], "보험."), F("___ 문제가 심각합니다. (low birthrate)", "저출산", ["고령화", "복지"], "저출산."), F("비만이 증가하는 ___입니다. (trend)", "추세", ["정책", "보험"], "추세."), F("___에서 자원봉사를 합니다. (a nursing home)", "양로원", ["고아원", "학원"], "양로원."), F("맞벌이 부부를 위한 ___를 운영합니다. (day nursery)", "탁아소", ["유치원", "대학원"], "탁아소.")]
        + [read_q("저출산 문제가 심각합니다"), read_q("고령화 사회로 들어섰습니다"), read_q("양로원에서 자원봉사를 합니다"), read_q("맞벌이 부부를 위한 탁아소를 운영합니다"), read_q("경제 정책을 결정했습니다")]
    ),
)

# ================================================================== L2 Part 1
_NEWS8 = [
    ("이십오 일 행정안전부에 따르면 지난해 중앙행정기관에서 육아휴직을 신청한 공무원은 천칠백이십삼 명으로, 이천육 년의 천이백오십일 명보다 삼십칠 점 칠 퍼센트 증가했다.", "According to the Ministry of Public Administration and Security on the 25th, the number of civil servants who applied for childcare leave at central administrative agencies last year was 1,723, an increase of 37.7 percent from 2006 (1,251)."),
    ("이 가운데 여성공무원은 이천사 년 구 점 이 퍼센트 육백구십팔 명, 이천오 년 십사 점 삼 퍼센트 팔백사십육 명, 이천육 년 이십 점 이 퍼센트 천백십오 명에서 지난해 이십이 점 삼 퍼센트 천육백 명으로 꾸준히 늘고 있는 것으로 나타났다.", "Among them, female civil servants were shown to be steadily increasing, from 9.2 percent (698) in 2004, 14.3 percent (846) in 2005 and 20.2 percent (1,115) in 2006 to 22.3 percent (1,600) last year."),
]
_QA8 = [
    ("저출산 문제가 심각한데 후보님의 출산장려정책이 궁금합니다.", "(Question 1) The low birthrate problem is serious, and I am curious about the candidate’s policy to encourage childbirth."),
    ("고령화 사회에서 노인들의 일자리 확대를 위한 계획은 있나요?", "(Question 2) In an aging society, is there a plan to expand jobs for the elderly?"),
    ("영유아 무상교육과 공공 보육시설 확대 계획이 있는지요?", "(Question 3) Is there a plan for free education for infants and young children and for expanding public childcare facilities?"),
    ("사 세까지 어린이의 의, 식, 주를 서울시가 책임지도록 하겠습니다.", "(Answer A) I will make the Seoul city government responsible for the clothing, food and housing of children up to age 4."),
    ("우선, 사 세까지 어린이의 건강보험 본인부담금을 전액 지원해 의료비에 대한 걱정을 없애고, 월 십만 원씩 맘마수당인 아동수당을 지급하고, 국공립 어린이집을 동마다 세 개씩 만들겠습니다.", "First, I will fully support the self-pay portion of the health insurance of children up to age 4 to eliminate worries about medical costs, pay a child allowance called the “mamma allowance” of 100,000 won a month, and build three national or public daycare centers in every neighborhood."),
    ("아이를 낳고 싶은 서울을 만들겠습니다.", "(Answer B) I will make a Seoul where people want to have children."),
    ("아이를 낳을 수 있는 환경을 조성해 주는 것이 최우선입니다.", "Creating an environment in which people can have children is the top priority."),
    ("키우기가 어려운데 무조건 낳으라고만 하는 것은 진정한 출산장려정책이 아닙니다.", "Telling people unconditionally to have children when raising them is hard is not a true childbirth-encouragement policy."),
    ("기본적으로 노인들을 위한 일자리를 무조건적으로 확충하는 것보다는 노인 복지를 제대로 갖추는 것이 우선이라고 생각합니다.", "(Answer C) Basically, I think that putting proper elderly welfare in place comes before expanding jobs for the elderly unconditionally."),
    ("노인들의 복지를 위해서는 지역별로 노인 주치의 제도를 확립하고 기초노령연금을 현실화해야 합니다.", "For the elderly’s welfare, we must establish a family-doctor system for the elderly in each region and make the basic old-age pension realistic."),
]
_SPEAK8A = [("저출산 문제를 해결하기 위해서 한국 정부가 어떻게 해야 할지 이야기해 보세요.", "Talk about what the Korean government should do to solve the low birthrate problem.")]
_PLAT8 = [("Countermeasures for low birthrates", "Create an environment in which people can have children; Seoul takes responsibility for children up to age 4 (full support of the self-pay portion of health insurance, a 100,000-won monthly child allowance, three public daycare centers per neighborhood)"), ("Plan for an aging society", "Put proper elderly welfare in place first rather than unconditionally expanding jobs: a family-doctor system for the elderly in each region and a realistic basic old-age pension")]
L2 = lesson(
    "U16 L8 · Part 1 (도입 학습): childcare leave and a mayoral candidate’s answers",
    "도입 학습 · 육아휴직 · 여성공무원 · 저출산 · 출산장려정책 · 고령화 · 기초노령연금 · 노인 주치의 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading and Speaking): a newspaper article on working women",
             "The following is a newspaper article on working women (text and image © Kyunghyang). The text is the book’s with the numbers spelled out (25일 → 이십오 일; 1723명 → 천칠백이십삼 명; 37.7% → 삼십칠 점 칠 퍼센트 and so on); the brackets around the figures are written as plain wording. The English is mine.",
             examples=passage(_NEWS8)),
        card("학습활동 1: the questions answered (mine)",
             "1. D — the number of female civil servants using maternity (childcare) leave is increasing.\n\n"
             "2. Possible reasons for the trend, to discuss in Korean: more women hold public jobs; the government encourages childcare leave and has made it easier to take; the cost of raising children is high and women want to keep their jobs; public offices are more secure and accept leave more readily than private companies."),
        card("학습활동 3 (Reading): questions and answers during a Seoul mayoral election",
             "The following is a newspaper article summarizing the questions of citizens and the answers of a Seoul mayoral candidate during the election period (text and image © Kyunghyang). The text is the book’s with the numbers spelled out (4세 → 사 세; 10만 원 → 십만 원; 3개 → 세 개); the quotation marks and the brackets in ‘맘마수당(아동수당)’ are written as 맘마수당인 아동수당. In the book each question is followed by the name, age and district of the housewife who asked it; those details are left out here. The English is mine; the labels are in the English only.",
             examples=passage(_QA8)),
        card("학습활동 3: the questions answered (mine)",
             "1. Matching: Question 1 – Answer B (the childbirth-encouragement policy); Question 2 – Answer C (jobs for the elderly); Question 3 – Answer A (free education for infants and young children and public childcare facilities).\n\n"
             "2. The candidate’s platform:",
             tables=[table(["Social issue", "Candidate’s campaign platform (mine)"], [list(r) for r in _PLAT8])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK8A)),
        card("Activities left out", "학습활동 2 (Listening, track 002): a KBS news item about North Korea: the UN’s definition of an aging society, and which statement gives the main topic (A. North Korea is the fastest aging society; B. North Korea is implementing a pro-life policy; C. North Koreans are suffering from famine; D. North Korea has an aging society). It is audio."),
    ],
    exercises=uniq(
        _tr(_NEWS8, k=2) + _tr(_QA8, k=3)
        + [M("What increased by 37.7 percent from 2006?", "Civil servants applying for childcare leave", ["Births", "School fees", "Pensions"], "육아휴직을 신청한 공무원."), M("Which agency released the figures?", "The Ministry of Public Administration and Security", ["The Ministry of Defense", "The Ministry of Education", "A newspaper"], "행정안전부."), M("Which answer deals with children up to age 4?", "Answer A", ["Answer B", "Answer C", "None"], "사 세까지 어린이."), M("Which question deals with elderly jobs?", "Question 2", ["Question 1", "Question 3", "None"], "노인들의 일자리."), M("What does the candidate say should come first for the elderly?", "Proper welfare", ["More jobs without conditions", "Less pension", "Fewer doctors"], "노인 복지를 제대로 갖추는 것이 우선."), M("What is the candidate’s top priority for births?", "An environment in which people can have children", ["Fines", "Slogans", "Taxes"], "아이를 낳을 수 있는 환경."),
           F("육아___을 신청한 공무원이 늘었다. (leave)", "휴직", ["휴가", "휴학"], "육아휴직."), F("___노령연금을 현실화해야 한다. (basic)", "기초", ["최저", "일반"], "기초노령연금."), F("출산___정책이 궁금합니다. (encouragement)", "장려", ["제한", "금지"], "출산장려정책."), F("노인 ___ 제도를 확립해야 한다. (family doctor)", "주치의", ["의사", "간호사"], "노인 주치의 제도."), F("국공립 ___을 동마다 세 개씩 만들겠습니다. (daycare center)", "어린이집", ["학원", "병원"], "어린이집.")]
        + [read_q("육아휴직을 신청한 공무원이 늘고 있습니다"), read_q("저출산 문제가 심각합니다"), read_q("아이를 낳고 싶은 서울을 만들겠습니다"), read_q("노인 주치의 제도를 확립해야 합니다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("육아", "(育兒) raising children; child care", "저희 회사에서 육아문제를 해결하기 위해 회사 내에 놀이방을 설치하기로 했어요."),
        ("휴직(하다)", "(休職) leave of absence (for an extended period of time); “resting from one’s job” (to take a leave of absence)", "우리 회사는 최고 일 년 동안 육아를 위해 휴직할 수 있습니다.", "휴가, 휴학, 휴교"),
    ]),
    ("학습활동 2", [
        ("고령화", "(高齡化) aging; “high age-ization”", "우리나라는 벌써 고령화 사회에 접어들었다고 합니다.", "저출산"),
        ("규정(하다/되다)", "(規定) a rule; a regulation (to stipulate/to be stipulated)", "고속도로의 규정 속도가 몇 킬로입니까?"),
        ("시급하다", "(時急) to be urgent", "수재민 지원이 시급합니다.", "조속하다"),
        ("실정", "(實情) the actual state; the real state", "많은 학생들이 시험에 떨어지는 실정입니다."),
    ]),
    ("학습활동 3", [
        ("기초(하다)", "(基礎) foundation; basis (to be based on; to be founded on)", "계약서에 기초해서 돈을 지급합니다."),
        ("수당", "(手當) extra pay; an allowance; a bonus", "이번 달에는 야근이 잦아서 야근 수당이 많습니다.", "연봉, 월급"),
        ("영유아", "(嬰幼兒) infants and young children", "저희 탁아소는 신생아와 영유아들을 대상으로 합니다.", "영아, 유아, 탁아소, 출산"),
        ("장려(하다/되다)", "(奬勵) encouragement (to encourage; to promote/to be encouraged; to be promoted)", "국가에서 소형차 구입을 장려하고 있습니다."),
        ("주치의", "(主治醫) one’s family doctor", "환자들은 일반적으로 주치의에게 많이 의존합니다."),
        ("책임", "(責任) responsibility; duty; obligation; accountability", "이번 일은 제 책임이 큽니다."),
        ("확립(하다/되다)", "(確立) establishment (to establish/to be established)", "사회의 질서를 확립하기 위해 제도를 정비하고 있습니다.", "세우다"),
    ]),
]
L3 = lesson(
    "U16 L8 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 육아 · 휴직 · 고령화 · 규정 · 시급하다 · 실정 · 기초 · 수당 · 영유아 · 장려 · 주치의 · 책임 · 확립",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 휴직 has 1년 (written 일 년 here).")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=7)),
)

# ================================================================== L4 Part 2
_ADOPT8 = [
    ("아이를 입양할 때 고개 조아려 가며, 겨우겨우 나흘 휴가를 받았어요.", "(Quotation) When I adopted the child, bowing low, I barely managed to get four days of leave."),
    ("제가 낳았더라면 당당히 삼 개월 출산휴가를 받았을 텐데 말이죠.", "If I had given birth, I would have confidently gotten three months of maternity leave."),
    ("아침에 일어나자마자 출근하다 보니 유대관계를 만들 시간이 너무 부족하죠.", "Since I go to work as soon as I get up in the morning, there is far too little time to build a bond."),
    ("맞벌이 부부인 김은아 씨와 한진우 씨는 지난해 사 월 결혼 오 년 만에 한 달 된 여아를 입양했다.", "The working couple Kim Eun-a and Han Jin-u adopted a one-month-old baby girl last April, five years after their marriage. (The book gives both as 31 and as pseudonyms.)"),
    ("김 씨가 초등학교 때 심장판막증으로 수술을 한 뒤 계속 약을 먹어야 해, 임신 대신 입양을 결정한 것이다.", "Because Ms. Kim had to keep taking medicine after an operation for a heart valve disease in elementary school, they decided on adoption instead of pregnancy."),
    ("김 씨는 둘째도 입양하고 싶지만 직장 사정 때문에 나중으로 미룰 수밖에 없다고 말했다.", "Ms. Kim said that she wants to adopt a second child too, but because of her job situation she has no choice but to put it off until later."),
    ("고아 수출국이라는 오명을 벗고 저출산 문제를 풀기 위해 정부가 국내 입양을 장려하고 있지만, 입양 휴가 등 사회적 배려는 여전히 부족한 것으로 나타났다.", "The government is encouraging domestic adoption in order to shed the stigma of being an “orphan-exporting country” and to solve the low birthrate problem, but social consideration such as adoption leave still turned out to be lacking."),
    ("특히 국내 입양아 열 명 중 여덟 명에서 아홉 명이 한 살 미만의 영유아라는 점에서 입양 휴가가 절실하다고 전문가들은 얘기한다.", "Experts say adoption leave is especially urgent since eight or nine out of ten domestically adopted children are infants under one year old."),
    ("홀트아동복지회 김은희 사회복지사는 입양은 출산만큼이나 가족에게 큰 변화라며 부모와 아기가 서로 정을 붙이고 익숙해지도록 돕는 최소한의 사회적 배려로 입양 휴가는 반드시 필요하다고 말했다.", "Kim Eun-hee, a social worker at the Holt Children’s Services, said that adoption is as big a change for a family as childbirth, and that adoption leave is absolutely necessary as the minimum social consideration to help parents and baby get attached and used to each other."),
    ("이에 우리 정부는 지난해 칠 월 이 주 입양 휴가제를 도입했다.", "In response, our government introduced a two-week adoption leave system last July."),
    ("하지만 지난해 십일 월부터 공무원을 대상으로 시행되고 있을 뿐이다.", "But it has been implemented only for civil servants since last November."),
    ("자산총액 기준 십 대 그룹 가운데 입양 휴가제를 도입한 곳은 단 한 곳도 없다.", "Among the ten largest groups by total assets, there is not a single one that has introduced an adoption leave system."),
]
_PET8 = [
    ("동물매개치료사", "(Title) Animal-assisted therapist"),
    ("도대체 이게 무슨 일을 하는 직업이죠?", "“What on earth is the work this job does?”"),
    ("이주연 씨의 명함을 본 사람들은 예외 없이 되묻는다.", "People who see Ms. Lee Ju-yeon’s business card ask back without exception."),
    ("몸과 마음이 아픈 사람들이 동물을 통해서 치료를 받을 수 있게 사람과 동물을 이어 주는 일이에요.", "“It is the work of connecting people and animals so that people whose bodies and minds hurt can receive treatment through animals.”"),
    ("그래도 여전히 고개를 갸웃거리는 이들이 많다.", "Even so, there are still many who tilt their heads."),
    ("그만큼 동물매개치료사란 직업이 드문 탓이다.", "That is because the job of animal-assisted therapist is that rare."),
    ("이 씨는 우리나라에서 몇 명 안 되는 동물매개치료사다.", "Ms. Lee is one of the few animal-assisted therapists in our country."),
    ("일주일에 이틀은 서울에 있는 사회복지관과 노인병원, 어린이 주간보호시설 등 열 군데 남짓을 찾아가 치료프로그램을 진행한다.", "Two days a week she visits about ten places in Seoul, such as social welfare centers, geriatric hospitals and children’s day-care facilities, and runs therapy programs."),
    ("훈련된 치료 도우미견을 데리고 가 환자들이 삼십 분에서 사십 분 동안 개들과 어울리면서 기분이 좋아지게 해 주는 것이 그의 일이다.", "Her job is to bring trained therapy helper dogs and make the patients feel better as they mix with the dogs for 30 to 40 minutes."),
    ("환자들이 개를 씻기고, 개털을 빗질해 주고 먹이를 주면서 자연스럽게 마음의 안정을 찾아간다는 게 이 씨의 설명이다.", "Ms. Lee explains that the patients naturally find peace of mind as they wash the dog, brush its fur and feed it."),
    ("동물을 통한 이런 치료방법이 정확하게 수치상으로 효과를 보여 주는 것은 아니지만 이렇게 정기적으로 도우미 개들과 어울리다 보면 환자들이 서서히 마음을 열어 가게 된다고 한다.", "This kind of treatment through animals does not show an effect precisely in numbers, but they say that if they mix with the helper dogs regularly like this, the patients gradually come to open their hearts."),
    ("자기 이름조차 기억하지 못하는 치매 어르신들이 도우미견의 이름을 부르고, 처음 개를 소개받을 때는 본체만체 하며 웃음기라곤 없던 자폐 어린이들이 개들과 어울리면서 자주 웃는 모습을 보면 제 마음도 열리는 것 같습니다.", "“When I see elderly people with dementia who cannot even remember their own names calling the helper dog’s name, and autistic children who pretended not to see the dog and had no trace of a smile when first introduced to it often smiling as they mix with the dogs, my own heart seems to open too.”"),
    ("이 씨는 수의학과를 졸업한 뒤 전공과는 다른 일을 하다가 우연히 삼성에스디아이에서 도우미개 관련 사업을 한다는 말을 듣고 이천일 년 관련 업무를 자원해 입사했다.", "After graduating from a veterinary medicine department, Ms. Lee worked in a field different from her major, and then happened to hear that Samsung SDI was running a business related to helper dogs, and in 2001 she volunteered for the related work and joined the company."),
    ("이후 이 씨는 미국 노스텍사스대에서 정식으로 동물매개치료사 과정을 이수한 뒤 정식으로 활동을 시작했다.", "Afterwards Ms. Lee formally completed the animal-assisted therapist course at the University of North Texas in the United States and formally began her activities."),
    ("센터에서 도우미견에게 기본 복종훈련과 특기 훈련을 시키고, 도우미견을 씻기고 먹이는 일도 이 씨의 몫이다.", "At the center, giving the helper dogs basic obedience training and special-skills training, and washing and feeding them, are also Ms. Lee’s share of the work."),
    ("일 년에 네 차례씩 운영하는 치료 도우미견과 함께 하는 자원봉사자 교육도 한다.", "She also gives training for volunteers who work with therapy helper dogs, run four times a year."),
    ("이렇게 바쁘게 일하는 한편 환자들의 마음을 더 잘 읽기 위해 가톨릭대에서 심리학 석사 과정을 밟고 있다.", "While working this busily, she is also pursuing a master’s course in psychology at the Catholic University in order to read the patients’ minds better."),
    ("자폐증이나 발달장애가 있는 자녀를 둔 부모들이 치료 도우미견을 분양해 달라고 하거나 치료를 요청해 오는 경우가 종종 있지만 현재 형편으로는 요구를 다 들어줄 수가 없어서 늘 아쉬워요.", "“There are often cases where parents with children with autism or developmental disabilities ask for a therapy helper dog or request treatment, but with our present circumstances we cannot meet all the requests, so I always feel regret.”"),
]
_SPEAK8B = [("애완동물을 기를 때 생기는 좋은 점과 불편한 점 세 가지씩을 생각해서 반 친구들에게 이야기해 보세요.", "Think of three good points and three inconvenient points that arise when raising a pet and tell your classmates.")]
_TF8 = [("The government limits the number of international adoptions.", "F", "The article says the government encourages domestic adoption; it does not say that it limits international adoptions."), ("The age of domestically adopted babies is mostly under 1 year old.", "T", "Eight or nine out of ten are infants under one."), ("The government and the top 10 companies have created favorable adoption-related leave policies.", "F", "Only the government (for civil servants) has; none of the top ten groups has.")]
_THER8 = [("Job title", "동물매개치료사 (animal-assisted therapist)"), ("Educational background", "Graduated from a veterinary medicine department; completed the animal-assisted therapist course at the University of North Texas (USA); now pursuing a master’s course in psychology at the Catholic University"), ("Duties (details)", "Visits about ten places (social welfare centers, geriatric hospitals, children’s day-care facilities) two days a week and runs therapy programs, bringing trained therapy helper dogs for 30 to 40 minutes; trains the dogs (basic obedience and special skills), washes and feeds them; runs volunteer training four times a year")]
L4 = lesson(
    "U16 L8 · Part 2 (본 학습): adoption leave and the animal-assisted therapist",
    "본 학습 · 입양 휴가 · 고아 수출국 · 영유아 · 동물매개치료사 · 도우미견 · 자폐증 · 치매 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2 (Reading): a newspaper article on adoption",
             "The following is a newspaper article on adoption (text and image © Hankyoreh). The text is the book’s with the numbers spelled out (3개월 → 삼 개월; 4월 → 사 월; 5년 → 오 년; 10명 중 8~9명 → 열 명 중 여덟 명에서 아홉 명; 1살 → 한 살; 7월 → 칠 월; 2주 → 이 주; 11월 → 십일 월; 10대 그룹 → 십 대 그룹), the ages and the note 가명 (pseudonym) in the brackets after the couple’s names left out (they are in the English), and the quotation marks removed. The English is mine.",
             examples=passage(_ADOPT8)),
        card("학습활동 2: the questions answered (mine)",
             "1. C — “It takes time to get used to the child after adoption, but I couldn’t get proper leave.”\n\n"
             "2. B — To help adoption, “a second birth,” the adoption leave system must be made active (the last paragraph says the system has been introduced only for civil servants and none of the ten largest groups has it).\n\n"
             "3. The statements, true (T) or false (F):",
             tables=[table(["Statement", "T/F", "Why"], [list(r) for r in _TF8])]),
        card("학습활동 3 (Reading and Speaking): an article on a job",
             "The following is a newspaper article on a job (© Kyunghyang and Hankyoreh). The text is the book’s with the numbers spelled out (10여 곳 → 열 군데 남짓; 30~40분 → 삼십 분에서 사십 분; 2001년 → 이천일 년; 4차례 → 네 차례) and the quotation marks removed. The English is mine.",
             examples=passage(_PET8)),
        card("학습활동 3: the questions answered (mine)",
             "1. The information about the person in the article:",
             tables=[table(["", "Information (mine)"], [list(r) for r in _THER8])]),
        card("학습활동 3: questions 2 and 3 (mine)",
             "2. The positive responses to the treatment: the patients naturally find peace of mind as they wash, brush and feed the dogs; they gradually open their hearts when they mix regularly with the helper dogs; elderly people with dementia who cannot remember their own names call the dog’s name; and autistic children who had no trace of a smile smile often as they mix with the dogs.\n\n"
             "3. Other ways dogs assist humans (my ideas): guide dogs for the blind, hearing dogs for the deaf, search-and-rescue dogs, police and drug-detection dogs, herding and guard dogs, service dogs for people with disabilities, and companionship."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine; 3가지씩 is written 세 가지씩):", examples=passage(_SPEAK8B)),
        card("Activities left out", "학습활동 1 (Listening and Speaking, track 003): a news item from North Korea on a nursing home (© Chosun Central Television): what event was held there in 2008, what propaganda measure is mentioned, and, as a class, the positive aspects of the U.S. welfare system. It is audio."),
    ],
    exercises=uniq(
        _tr(_ADOPT8, k=3) + _tr(_PET8, k=3)
        + [M("How much leave did the couple get when they adopted?", "Four days", ["Three months", "Two weeks", "One year"], "나흘 휴가."), M("How old was the adopted baby when the couple adopted her?", "One month", ["One year", "Five years", "Ten days"], "한 달 된 여아."), M("Why did they decide on adoption?", "Ms. Kim had to keep taking medicine after a heart operation", ["They could not afford a child", "They disliked pregnancy", "They had a large family"], "심장판막증."), M("What adoption leave did the government introduce?", "Two weeks", ["One day", "Three months", "One year"], "이 주."), M("To whom does the adoption leave system apply so far?", "Civil servants", ["All workers", "Teachers only", "Company employees"], "공무원을 대상으로."), M("What is the job of an animal-assisted therapist?", "Connecting people and animals so that people can be treated through animals", ["Selling pets", "Training racing dogs", "Treating sick animals only"], "사람과 동물을 이어 주는 일."), M("How often does she visit places for therapy programs?", "Two days a week", ["Every day", "Once a month", "Once a year"], "일주일에 이틀."), M("How long do patients mix with the dogs?", "30 to 40 minutes", ["5 minutes", "Two hours", "All day"], "삼십 분에서 사십 분."), M("What did she study at the university in America?", "The animal-assisted therapist course", ["Law", "Cooking", "Music"], "동물매개치료사 과정."),
           F("아이를 ___할 때 겨우 나흘 휴가를 받았다. (to adopt)", "입양", ["출산", "양육"], "입양."), F("입양 휴가는 ___ 필요하다. (absolutely)", "반드시", ["가끔", "절대로"], "반드시."), F("치료 도우미견은 환자들의 ___을 열어 준다. (hearts)", "마음", ["문", "손"], "마음을 열다."), F("도우미견에게 기본 ___훈련을 시킨다. (obedience)", "복종", ["수영", "요리"], "복종훈련."), F("___ 어린이들이 개들과 어울리면서 자주 웃는다. (autistic)", "자폐", ["영리한", "건강한"], "자폐 어린이.")]
        + [read_q("입양 휴가제를 도입했습니다"), read_q("고아 수출국이라는 오명을 벗어야 합니다"), read_q("동물매개치료사는 몸과 마음이 아픈 사람들을 도와줍니다"), read_q("애완동물을 기르는 것에 대해 어떻게 생각합니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("경사", "(慶事) a happy occasion", "집도 사고 아이도 태어나고 경사가 끊이지 않습니다."),
        ("경애(하다)", "(敬愛) respect and affection (to love, respect, and hold in high esteem)", "경애하는 김정일 장군"),
        ("연로자", "(年老者) an elderly person; a senior citizen", "이 프로그램은 연로자를 대상으로 합니다.", "노인 | 양로원, 고령화 | 련로자"),
        ("사회주의", "(社會主義) socialism", "천구백구십 년대에 동구권의 사회주의가 몰락했습니다."),
        ("혈육", "(血肉) a family (by birth); one’s own flesh and blood; “blood and flesh”", "김 선생님에게는 여동생이 유일한 혈육입니다.", "가족, 자식"),
    ]),
    ("학습활동 2", [
        ("고개를 조아리다", "to bow low; to kowtow", "", "머리를 조아리다"),
        ("유대", "(紐帶) a bond; a link; a tie", "이번 여행을 통해 가족간의 유대 관계가 돈독해졌어요.", "관계"),
        ("입양(하다/되다)", "(入養) an adoption; “(bringing) in and raising” (to adopt/to be adopted)", "저는 아이를 하나 입양하고 싶어요."),
        ("절실하다", "(切實) to be urgent; to be desperate; to be acute", "지진으로 해외 자원봉사자의 도움이 절실합니다."),
        ("정을 붙이다", "(情) to get (emotionally) attached; to share affection with; “to attach one’s feeling”", "새로운 이웃들과 정을 붙이고 삽니다."),
    ]),
    ("학습활동 3", [
        ("고개를 갸웃하다", "to express uncertainty; “to nod the head slantwise”", "설명을 듣고도 내 동생은 고개를 갸웃했다."),
        ("드물다", "to be rare; to be unusual; to be uncommon", "이 지역에는 눈이 오는 것이 드물다."),
        ("매개", "(媒介) a medium; a carrier", "우리는 음악을 매개로 처음 만났어요.", "매체"),
        ("몫", "a share; a quota", "그 사람은 두 사람 몫을 합니다."),
        ("발달장애", "(發達障碍) developmental disability", "우리 아이는 발달장애를 겪고 있습니다."),
        ("복종(하다)", "(服從) obedience (to obey)", "군인은 명령에 복종해야 한다."),
        ("본체만체하다", "to pretend not to have seen; to neglect; to slight", "그 일이 있은 후 그녀는 나를 본체만체했다."),
        ("이수(하다/되다)", "(履修) completion (of an academic course) (to complete; to finish/to be completed; to be finished)", "이번 학기에 수학과목을 이수했어요."),
        ("자폐증", "(自閉症) autism; “self-closing syndrome”", "자폐증에 걸린 아이는 말을 잘 하지 않습니다."),
        ("치매", "(癡呆) dementia; Alzheimer’s disease", "할머니가 치매 초기 증상을 보이고 계십니다."),
    ]),
]
L5 = lesson(
    "U16 L8 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 경사 · 경애 · 연로자 · 사회주의 · 혈육 · 고개를 조아리다 · 유대 · 입양 · 절실하다 · 정을 붙이다 · 고개를 갸웃하다 · 드물다 · 매개 · 몫 · 발달장애 · 복종 · 본체만체하다 · 이수 · 자폐증 · 치매",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 경애 is the phrase 경애하는 김정일 장군, a North Korean honorific for its former leader (the word is used in North Korean writing), and the related words of 연로자 end with the North Korean spelling 련로자. The book’s example for 사회주의 has 1990년대 (written 천구백구십 년대 here).")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3
_ART8A = [
    ("하이둠은 대학을 다니면서 첫 두 아이를 낳았다.", "(Article 1) Heidum had her first two children while attending university."),
    ("셋째 아이를 낳은 것은 일 년 전.", "She had her third child a year ago."),
    ("현재 직장에서 일하던 중이었다.", "She was working at her current workplace."),
    ("국가에서 운영하는 공공 보육시설이 있는데요.", "“There are public childcare facilities run by the state."),
    ("대부분 일하는 엄마들이 이걸 이용해요.", "Most working mothers use them."),
    ("이미 앞서 두 아이도 대학 공부하면서 그렇게 키웠고요.", "I already raised the first two children that way too while studying at university.”"),
    ("아이가 셋이다.", "There are three children."),
    ("드는 비용은 한국 돈으로 구십육만 원 정도다.", "The cost is about 960,000 won in Korean money."),
    ("기저귀, 식사 등등 모두 포함돼 있으니까 비싼 건 아니에요.", "“Diapers, meals and so on are all included, so it isn’t expensive.”"),
    ("하이둠의 수입은 월 삼만 팔천 크로네, 약 구백이십만 원이다.", "Heidum’s income is 38,000 kroner a month, about 9.2 million won."),
    ("수입 중 순수 보육비가 차지하는 비율이 십 분의 일가량에 불과한 셈이다.", "The share of pure childcare cost in her income thus comes to only about one tenth."),
    ("덴마크에선 아이는 사회가 키운다는 생각이 보편적이다.", "In Denmark the idea that “society raises the child” is universal."),
    ("지자체마다 연령대별 공공 보육시설이 충분히 갖춰져 있다.", "Every local government has public childcare facilities for each age group sufficiently in place."),
    ("취학 아동들을 위한 방과 후 보육시설, 학교 여가시간 시설 등도 있다.", "There are also after-school childcare facilities for school-age children, school leisure-time facilities and so on."),
    ("하이둠이 다니는 브루엘 앤 케어는 탄력적 근무시간제를 시행하고 있다.", "The company Heidum works for, Brüel & Kjær, implements a flexible working-hours system."),
    ("주 삼십칠 시간만 채우면, 그 안에서 출퇴근시간 조정이 자유롭다.", "As long as she fills 37 hours a week, she is free to adjust commuting times within that."),
    ("일과 가족의 양립을 위해서다.", "This is for the compatibility of work and family."),
    ("산전 후 휴가와 육아휴직도 일상적 권리일 뿐이다.", "Pre- and postnatal leave and childcare leave are also just ordinary rights."),
    ("저는 아이들이 북적거리는 게 좋아요.", "“I like the children bustling about."),
    ("세 명이 좀 많은가요?", "Are three a bit many?"),
    ("앞으로 적어도 한 명쯤은 더 가질 생각인데요.", "In the future I plan to have at least one more.”"),
]
_ART8B = [
    ("김동은 씨는 불과 두 달 전 회사 다니던 때를 떠올렸다.", "(Article 2) Kim Dong-eun recalled the time, just two months ago, when she was going to her company."),
    ("비용이 만만찮았다.", "The cost was not easy."),
    ("도우미 비용이 월 백오십만 원.", "The helper’s fee was 1.5 million won a month."),
    ("또 쌍둥이인지라 분유, 기저귀, 유아 목욕용품 등 필수품들에 대한 지출도 배로 나갔다.", "Also, because they were twins, spending on necessities such as powdered milk, diapers and baby bath items also doubled."),
    ("남편과 맞벌이로 버는데도 수입의 사십 퍼센트 이상이 순수 육아비로 나갔다.", "Even though she and her husband earned as a working couple, more than 40 percent of their income went to pure childcare costs."),
    ("육아비 부담이 너무 컸어요.", "“The burden of childcare costs was too big."),
    ("이럴 바에야 남의 손에 아이를 맡기는 것보다 내가 그만두고 키우는 게 낫겠다 싶어 고민을 했지요.", "If it is going to be like this, I worried that it might be better for me to quit and raise the child than to leave the child in someone else’s hands.”"),
    ("그렇게 결국 팔 년간 정든 회사를 떠났다.", "So in the end she left the company she had grown attached to over eight years."),
    ("결국 일 대신 아이를 택한 거죠.", "“In the end I chose the child instead of work.”"),
    ("육아휴직이요?", "“Childcare leave?"),
    ("당연히 못 했죠.", "Of course I couldn’t take it."),
    ("저희 회사 같은 경우 육아휴직은 기본적으로 없다고 보면 돼요.", "In a case like my company, you can see it as basically nonexistent."),
    ("쓰는 경우는 거의 못 봤는데요.", "I have hardly seen anyone use it."),
    ("그런 분위기에서 눈치 보여서 어떻게 사용해요.", "In such an atmosphere, how can anyone use it, feeling people’s looks?”"),
    ("김 씨는 눈물 겨운 사연을 가진 엄마들이 많다고 했다.", "Ms. Kim said there are many mothers with tearful stories."),
    ("오후 여섯 시가 되면 총알같이 나가야 하는 엄마들이 많죠.", "“There are many mothers who have to dash out like a bullet at 6 p.m."),
    ("십 분이라도 넘으면 육아 도우미 아주머니들이 추가비용을 받아요.", "If it goes over even ten minutes, the childcare helper women charge extra."),
    ("시집이나 친정에 아이 데리러 가야 하는 경우도 많고.", "There are also many cases where they must go to pick up the child at the in-laws’ or their own parents’ home."),
    ("근데 또 일이 오후 여섯 시에 딱 끝나는 게 아니잖아요.", "But work doesn’t end exactly at 6 p.m., right?"),
    ("발만 동동 구르는 거죠.", "All they can do is stamp their feet anxiously."),
    ("아이가 아플 때도요.", "Also when the child is sick."),
    ("특별히 휴가 내지 말라고 하는 건 아닌데 눈치가 엄청 보여요.", "It’s not that they specifically tell you not to take leave, but you feel enormous pressure from people’s looks.” (The book prints 내지 마 하는, a slip for 내지 말라고 하는.)"),
    ("엄마들이 가장 원하는 건 믿을 수 있는 양육자, 양육 시설이에요.", "“What mothers want most is a trustworthy caregiver and childcare facility."),
    ("엄마가 아이 낳고 사회에 복귀하려면 결국 그런 게 필요하잖아요.", "In the end, that is what a mother needs if she wants to return to society after giving birth.”"),
]
_STM8 = [
    ("주변에서 경제적 능력이 없어 아이를 더 이상 낳지 않는 경우가 아주 많아요.", "“Around me there are very many cases of people who do not have more children because they lack economic ability.” — Korean, Kim Dong-eun"),
    ("아이를 키우는 데 돈이 너무 많이 들어가서 저축을 하거나 여가생활을 즐길 수가 없어요.", "“Raising children takes so much money that I can’t save or enjoy leisure.” — Korean, Kim Dong-eun"),
    ("직장생활과 육아를 동시에 잘 할 수 있는 여건이 안 돼 있으니 여성이 능력을 발휘하기 쉽지 않아요.", "“The conditions for doing both work life and childcare well at the same time are not in place, so it isn’t easy for women to show their ability.” — Korean, Kim Dong-eun"),
    ("직장의 스케줄을 개인의 사정에 맞게 조절할 수 있기 때문에 자녀가 많은 직장여성을 쉽게 찾아 볼 수 있어요.", "“Because workplace schedules can be adjusted to individual circumstances, you can easily find working women with many children.” — Danish, Heidum"),
]
_DKTAB8 = [("Child-care expenses", "About 960,000 won a month for three children, with diapers and meals included; only about one tenth of her income (about 9.2 million won)", "A helper costs 1.5 million won a month and necessities doubled because of the twins; more than 40 percent of the couple’s income goes to pure childcare costs"), ("Child-care support at the workplace", "A flexible working-hours system (37 hours a week, free to adjust commuting times); pre- and postnatal leave and childcare leave are ordinary rights", "Childcare leave basically does not exist and no one uses it; mothers have to leave at 6 p.m. sharp and feel the pressure of people’s looks"), ("Change of job after birth", "She keeps working and plans at least one more child", "She quit the company she had worked at for eight years and chose the children instead of work")]
_AGE8 = [
    ("노인복지확대", "(Heading) Expansion of elderly welfare"),
    ("기초노령연금의 수혜자는 내년 칠 월부터는 약 삼백만 명으로 확대된다.", "The beneficiaries of the basic old-age pension will be expanded to about 3 million people from July next year."),
    ("육십오 세 이상 노인의 육십 퍼센트가량이 혜택을 받는다.", "About 60 percent of the elderly aged 65 or over receive the benefit."),
    ("그러나 노인복지는 여전히 걸음마 수준이다.", "But elderly welfare is still at the toddling level."),
    ("특히 혼자 사는 저소득층 노인들에게는 정부의 손길이 절실하다.", "In particular, the government’s helping hand is urgently needed by low-income elderly people who live alone."),
    ("팔 일 보건복지부가 발표한 자료에 따르면 육십오 세 이상 독거노인 팔십팔만 명의 월평균 소득은 이십오만 사천 원에 불과하다.", "According to data announced by the Ministry of Health and Welfare on the 8th, the average monthly income of the 880,000 elderly people aged 65 or over living alone is only 254,000 won."),
    ("내년 기초노령 연금이 도입돼 합산된다고 해도 최저생계비에 미치지 못한다.", "Even if the basic old-age pension is introduced next year and added up, it falls short of the minimum cost of living."),
    ("또 독거노인 중 구십이 퍼센트에게는 자식이나 형제자매가 있는 것으로 조사됐다.", "Also, it was found that 92 percent of the elderly living alone have children or brothers and sisters."),
    ("더 이상 노인 문제의 해답은 가족이 아니란 의미다.", "It means that the answer to the elderly problem is no longer the family."),
    ("가장 원만한 해결책은 복지정책과 더불어 노인들에게 일자리를 제공하는 것이다.", "The most satisfactory solution is to provide jobs to the elderly along with welfare policy."),
    ("최근에는 평균수명이 팔십 세에 육박하고 있어 직장에서 은퇴하고 난 뒤에도 이십 년 가까이 시간이 남는다.", "Recently, average life expectancy is approaching 80, so even after retiring from the workplace nearly 20 years remain."),
    ("그러나 우리나라 노인의 경제활동 참여율은 삼십일 퍼센트 수준에 불과하다.", "But the economic-activity participation rate of our elderly is only about 31 percent."),
    ("게다가 수익성 경제활동이 절실한 독거노인의 경제활동 참여율은 십육 퍼센트로 더 떨어진다.", "Moreover, the participation rate of elderly people living alone, who urgently need profit-making economic activity, falls further to 16 percent."),
    ("정부가 노인 시험감독관, 노인 주유원 등 민간부문 일자리를 개발하고 있지만 이천사 년 이만 오천 개로 시작한 노인일자리는 올해 십일만 개 수준에 그치고 있다.", "The government is developing private-sector jobs such as elderly exam proctors and elderly gas-station attendants, but the elderly jobs that started at 25,000 in 2004 stop at about 110,000 this year."),
    ("이 중 자원봉사에 가까운 공익형이 오십사 점 삼 퍼센트이고 수익을 창출하는 시장형이나 인력 파견형은 십 퍼센트도 되지 않는다.", "Of these, the public-interest type close to volunteering is 54.3 percent, and the market type that creates profit and the manpower-dispatch type are less than 10 percent."),
    ("그나마도 지속적으로 공급되지 않아 일 년 미만에 그치는 경우가 다반사다.", "Even these are not supplied continuously, so it is common for them to last less than a year."),
    ("복지부 관계자는 고령화는 지금보다 미래에 더 큰 문제가 될 수 있다며 복지재원을 늘리는 것도 중요하지만 충실한 일자리 창출 등에서도 해결책을 찾아봐야 한다고 말했다.", "An official of the Ministry said that aging could become a bigger problem in the future than now, and that while increasing welfare funds is important, solutions should also be sought in creating substantial jobs and so on."),
]
_SPEAK8C = [("요즘 한국은 세계에서 가장 빠른 고령화 속도를 보이고 있는데요.", "These days Korea shows the fastest aging speed in the world."), ("고령화의 원인과 그로 인해 나타나는 문제점에는 어떤 것들이 있습니까?", "What are the causes of aging and the problems that arise from it?"), ("그리고 고령화를 막기 위해 정부가 할 수 있는 일은 무엇인지 이야기해 보세요.", "And talk about what the government can do to stop aging.")]
L6 = lesson(
    "U16 L8 · Part 3 (심화 학습): two mothers, and the aging problem",
    "심화 학습 · 덴마크 · 보육시설 · 탄력적 근무시간제 · 육아휴직 · 육아비 · 기초노령연금 · 독거노인 · 노인 일자리 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2 (Reading and Speaking): a Danish mother and a Korean mother after childbirth",
             "The following are two newspaper articles on the lives after childbirth of a woman in Denmark and a woman in Korea (© Kyunghyang). The text is the book’s with the numbers spelled out (1년 → 일 년; 96만 원 → 구십육만 원; 3만8000크로네(약 920만원) → 삼만 팔천 크로네, 약 구백이십만 원; 10분의 1 → 십 분의 일; 37시간 → 삼십칠 시간; 150만 원 → 백오십만 원; 40% → 사십 퍼센트; 8년 → 팔 년; 6시 → 여섯 시) and the quotation marks removed. In the English, quotation marks mark the speakers’ words. The English is mine.",
             examples=passage(_ART8A + _ART8B)),
        card("학습활동 2: the questions answered (mine)",
             "1. The table:",
             tables=[table(["", "Danish mother (Heidum)", "Korean mother (Kim Dong-eun)"], [list(r) for r in _DKTAB8])]),
        card("학습활동 2: question 2 — who would say it (mine)",
             "Identify which mother would most likely make each additional comment. The first three are the Korean mother, 김동은 씨; the last is the Danish mother, 하이둠 씨. Question 3 asks for your own policy ideas as a policy maker (for example: public childcare facilities in every area, flexible working hours, guaranteed and usable childcare leave, childcare cost support, and reliable caregivers).",
             examples=passage(_STM8)),
        card("학습활동 3 (Reading): a newspaper article on aging",
             "The following is a newspaper article on aging (text and image © Kyunghyang). The text is the book’s with the numbers spelled out (7월 → 칠 월; 300만 명 → 삼백만 명; 65세 → 육십오 세; 60% → 육십 퍼센트; 8일 → 팔 일; 88만 명 → 팔십팔만 명; 25만4000원 → 이십오만 사천 원; 92% → 구십이 퍼센트; 80세 → 팔십 세; 20년 → 이십 년; 31% → 삼십일 퍼센트; 16% → 십육 퍼센트; 2004년 2만5000개 → 이천사 년 이만 오천 개; 11만 개 → 십일만 개; 54.3% → 오십사 점 삼 퍼센트; 10% → 십 퍼센트; 1년 → 일 년), the quotation marks removed. The English is mine.",
             examples=passage(_AGE8)),
        card("학습활동 3: the questions answered (mine)",
             "1. The economic activities of elderly people in Korea in the fourth paragraph: jobs the government has developed in the private sector, such as elderly exam proctors and elderly gas-station attendants; about 110,000 such jobs this year, most of them the public-interest type close to volunteering (54.3 percent), with the profit-making market type and manpower-dispatch type under 10 percent, and often lasting less than a year.\n\n"
             "2. The solution the writer recommends: along with welfare policy, provide jobs to the elderly (the most satisfactory solution), and, as the official says, create substantial jobs rather than only increasing welfare funds.\n\n"
             "3. The underlined sentence in the second paragraph is not marked in the text; the best guess is 더 이상 노인 문제의 해답은 가족이 아니란 의미다: “This means that the answer to the elderly problem is no longer the family.” The writer says this because 92 percent of the elderly living alone have children or brothers and sisters, yet they live on a very low income, so the family evidently cannot solve the problem.\n\n"
             "4. D — 초보적인 (elementary; at a beginner’s level), the word that best replaces 걸음마 (toddling)."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK8C)),
        card("Activities left out", "학습활동 1 (Listening, track 004): a commentary on low birthrates (© Donga): the current status of the Korean population according to a U.N. report, an example proving that the population in Seoul has decreased, the speaker’s two concerns about population decrease, and the main causes. It is audio."),
    ],
    exercises=uniq(
        _tr(_ART8A + _ART8B, k=3) + _tr(_AGE8, k=3) + _tr(_STM8, k=3)
        + [M("How many children does Heidum have?", "Three", ["One", "Two", "Five"], "아이가 셋."), M("About what share of her income does childcare cost?", "One tenth", ["Half", "One third", "All of it"], "십 분의 일."), M("How many hours a week does she need to work?", "37 hours", ["10 hours", "60 hours", "24 hours"], "주 삼십칠 시간."), M("Why did Kim Dong-eun quit her job?", "Childcare costs were too high", ["She was fired", "She retired", "She moved abroad"], "육아비 부담."), M("How long had she worked at the company?", "Eight years", ["Two years", "Eighteen years", "Eight months"], "팔 년."), M("What percentage of income went to childcare for the Korean couple?", "More than 40 percent", ["About 10 percent", "About 5 percent", "None"], "사십 퍼센트 이상."),
           M("How many people will receive the basic old-age pension from next July?", "About 3 million", ["About 30,000", "About 300 million", "About 300"], "삼백만 명."), M("What is the average monthly income of elderly people living alone?", "254,000 won", ["2.5 million won", "25,400 won", "25 million won"], "이십오만 사천 원."), M("What share of the elderly living alone have children or siblings?", "92 percent", ["29 percent", "9 percent", "50 percent"], "구십이 퍼센트."), M("What is the economic-activity participation rate of the elderly?", "About 31 percent", ["About 3 percent", "About 61 percent", "About 91 percent"], "삼십일 퍼센트."),
           F("덴마크에서는 ___ 근무시간제를 시행한다. (flexible)", "탄력적", ["획일적", "고정적"], "탄력적 근무시간제."), F("육아휴직은 ___ 없다고 보면 된다. (basically)", "기본적으로", ["가끔", "절대로"], "기본적으로."), F("노인복지는 여전히 ___ 수준이다. (toddling)", "걸음마", ["최고", "세계"], "걸음마."), F("평균수명이 팔십 세에 ___하고 있다. (to come close to)", "육박", ["도달", "하락"], "육박하다."), F("독거노인에게는 정부의 ___이 절실하다. (helping hand)", "손길", ["눈길", "발길"], "손길.")]
        + [read_q("덴마크에서는 아이는 사회가 키운다고 생각합니다"), read_q("육아비 부담이 너무 컸습니다"), read_q("독거노인에게는 정부의 손길이 절실합니다"), read_q("고령화의 원인은 무엇입니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("가시(적)", "(可視的) visible; tangible", "새로운 제도의 가시적 성과는 좀 기다려야 할 것 같습니다."),
        ("교원", "(敎員) the teaching staff; faculty", "교원 자격시험을 준비하고 있습니다.", "교사, 선생님"),
        ("쇠퇴(하다)", "(衰退) dwindling; decline; decadence; deterioration (to dwindle; to decline; to decay; to deteriorate)", "지난 십 년간 이 지역 경제가 쇠퇴하고 있습니다."),
        ("수급", "(需給) supply and demand", "수급 불균형으로 농산물 가격이 심하게 오르고 있습니다.", "수요, 공급"),
        ("울음", "crying; weeping", "아이 울음 소리 때문에 밤을 샜어요.", "웃음 | 울다"),
        ("정원", "(定員) fixed number; (fixed/seating) capacity", "지원자 수가 정원 미달이어서 지원자 모두가 합격입니다."),
        ("통폐합(하다/되다)", "(統廢合) merging (to merge/to be merged)", "지난해 이 은행은 경영난으로 지점 세 개를 통폐합했다."),
        ("파탄(하다/되다)", "(破綻) a failure (economic); a bankruptcy (to fail; to go bankrupt/to be failed; to be bankrupted)", "전쟁으로 인해 국가 재정이 파탄됐습니다."),
        ("현황", "(現況) present condition; current situation", "뉴스에서 수해의 피해현황을 시시각각 보도하고 있습니다."),
    ]),
    ("학습활동 2", [
        ("기저귀", "a diaper", "기저귀 값이 너무 올라서 부담됩니다."),
        ("눈치(보다)", "a sense; a facial expression; a look; “corner of the eye” (to try to read one’s mind by glancing at the face)", "우리 반 학생들은 눈치가 빨라서 한국말을 잘 배웁니다. 직원들이 모두 사장님의 눈치를 보고 있습니다."),
        ("떠올리다", "to recall; to recollect", "어제 사고를 떠올리면 지금도 화가 납니다.", "기억하다, 생각하다"),
        ("발을 동동구르다", "pace around nervously/anxiously; jump up and down nervously; “to stamp one’s feet repeatedly”", "출근 시간이 가까워 오는데 버스가 오지 않아 발을 동동 굴렀어요."),
        ("보편적", "(普遍的) universal; general", "요즘은 핵가족이 보편적인 가족의 형태입니다."),
        ("복귀(하다)", "(復歸) returning (to one’s original position); a comeback (to return; to come back)", "휴가가 끝나고 다음 주에 직장에 복귀합니다.", "돌아가다"),
        ("북적거리다", "hustle and bustle; to be crowded (with people); to be packed", "그 식당은 손님들로 북적거렸습니다.", "붐비다"),
        ("분유", "(粉乳) powdered milk; powdered formula", "모유가 부족하니까 아이에게 분유를 먹이세요.", "우유, 출산, 영유아"),
        ("불과(하다)", "(不過) just; only (to be nothing more than)", "그 회사는 직원이 세 명에 불과합니다."),
        ("쌍둥이", "(雙) twins", "저한테는 쌍둥이 언니가 있습니다.", "두 쌍둥이, 세 쌍둥이, 네 쌍둥이"),
        ("양립(하다/되다)", "(兩立) coexistence; compatibility (to coexist)", "저희 경영진은 육아와 직장이 양립할 수 있도록 최선을 다하겠습니다."),
        ("지자체", "(地自體) a local autonomous government entity; a short form of 지방자치단체", ""),
        ("탄력", "(彈力) flexibility; resilience; spring; bounce", "날씨가 더워지면서 탄력 근무제를 시행하는 회사가 늘고 있습니다."),
    ]),
    ("학습활동 3", [
        ("걸음마", "toddling", "우리 사업은 아직 걸음마 단계입니다."),
        ("공익", "(公益 or 共益) public interest(s); common good", "공익을 위해 개인의 이익을 포기해야 합니까?", "사리, 사익"),
        ("다반사", "(茶飯事) a common case; a daily event; common; frequent", "요즘은 폭우로 정전이 되는 것이 다반사입니다."),
        ("독거노인", "(獨居老人) a senior citizen who lives alone", "고령화 사회에 들어서면서 독거노인들이 늘고 있습니다."),
        ("손길", "(helping) hand", "아이에게는 엄마의 손길이 필요합니다.", "도움"),
        ("수혜자", "(受惠者) a beneficiary", "이 복지프로그램의 가장 큰 수혜자는 독거노인들입니다."),
        ("육박하다", "(肉薄) to come close up (to a certain number or a limit)", "이 마을의 육십오 세 이상 노인이 칠십 퍼센트에 육박합니다.", "가깝다"),
        ("최저생계비", "(最低生計費) the minimum cost of living", "최저생계비 책정을 놓고 국회에서 논란이 한창입니다.", "최저생활비"),
    ]),
]
L7 = lesson(
    "U16 L8 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가시적 · 교원 · 쇠퇴 · 수급 · 정원 · 통폐합 · 파탄 · 현황 · 기저귀 · 눈치 · 떠올리다 · 보편적 · 복귀 · 북적거리다 · 분유 · 쌍둥이 · 양립 · 지자체 · 탄력 · 걸음마 · 공익 · 독거노인 · 손길 · 수혜자 · 육박하다 · 최저생계비",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives an extra note under 정원 (定員): 정원 (庭園) means “a yard; a garden”. The book’s examples with numbers are written out: 10년간 → 십 년간, 3개 → 세 개, 3명 → 세 명, 65세 → 육십오 세 and 70퍼센트 → 칠십 퍼센트. The book gives the Hanja of 공익 as 公益/共益 (written 公益 or 共益 here) and has no example for 지자체, only a note that it is a short form of 지방자치단체. The related word of 울음 is 웃음 (opposite) and 울다 (verb).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=26, nread=20)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 8: An Aging Society: Low Birthrates and Government Countermeasures (고령화 사회: 저출산과 정부의 대책)", [L1, L2, L3, L4, L5, L6, L7])
