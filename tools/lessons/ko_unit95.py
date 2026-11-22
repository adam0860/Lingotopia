"""Unit 95: KBC Semester III, Unit 18, Lesson 10 - Government Policies (정부 정책).
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
_MATCH10 = [("정부", "a government", "정부정책에 반대하다"), ("중앙", "center; the middle", "중앙으로 가다"), ("복지", "welfare", "복지사회를 건설하다"), ("참여", "participation", "선거에 참여하다"), ("재정", "finances; financial affairs", "재정적자에 시달리다"), ("저소득층", "low-income group", "저소득층을 위한 의료개혁"), ("지방자치단체", "a local government", "지방자치단체장 선거를 하다"), ("보장", "guarantee", "사회보장제도가 발달되다"), ("의무", "obligation; duty; responsibility", "한국에서는 병역이 의무이다"), ("공중보건", "public health", "공중보건을 위해 힘쓰다"), ("분쟁해결", "settlement; solution", "분쟁해결을 위해 나서다"), ("계약", "a contract", "계약이 만료되다")]
_AUD10 = [("육아휴직", "childcare leave"), ("건강보험", "health insurance"), ("무상급식", "free school meals"), ("장애인 복지", "welfare for the disabled")]
_HJ10 = [("給 급", "providing; supply", "발급, 급식"), ("中 중", "middle; hitting; in the middle", "집중, 중독"), ("推 추", "push; suppose", "추진, 추이"), ("擴 확", "extending; widening", "확산, 확성기"), ("決 결", "decision; determination", "판결, 결의")]
_HJW10 = [("발급", "issuing"), ("급식", "provision of school lunch"), ("집중", "concentration"), ("중독", "poisoning; addiction"), ("추진", "propel; pushing ahead"), ("추이", "development of an event; progress of an event"), ("확산", "spreading"), ("확성기", "a loudspeaker"), ("판결", "a judgment; a judicial decision"), ("결의", "a resolution")]
_SIM10 = [("결심", "결정", "resolution: decision"), ("공급", "보급", "supply: spreading; supply (my pick)"), ("중지", "중단", "stopping: discontinuing")]
_ODD10 = [("지급, 급여, 봉급, 월급", "지급", "지급 is paying out; the other three are kinds of pay"), ("확장, 확대, 확충, 확인", "확인", "확인 is checking; the other three are expanding"), ("추진, 추리, 추정, 추측", "추진", "추진 is pushing ahead; the other three are guessing"), ("완결, 미결, 타결, 해결", "미결", "미결 is unsettled; the other three are settled")]
_L10X = [("수급", "supply and demand; receiving"), ("환급", "a refund"), ("자급", "self-sufficiency"), ("중순", "the middle ten days of a month"), ("중심", "the center"), ("봉급", "a salary"), ("월급", "a monthly salary"), ("지급", "payment; paying out"), ("급여", "pay; wages"), ("확장", "expansion"), ("확대", "enlargement"), ("확충", "expansion; reinforcement"), ("확인", "confirmation"), ("추리", "reasoning; deduction"), ("추정", "an estimate"), ("추측", "a guess"), ("완결", "completion"), ("미결", "pending; unsettled"), ("타결", "a settlement"), ("해결", "a solution")]
L1 = lesson(
    "U18 L10 · Review: policy words and Sino-Korean 給 中 推 擴 決",
    "정부 정책 · 단어 복습 · 한자어 복습 · 복지 · 재정 · 저소득층 · 보장 · 의무 · 공중보건 · 계약 · 給 中 推 擴 決",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its meaning", "The book gives twelve phrases with a word underlined and twelve English meanings. The underlines are not marked in the text; the pairs below are my reading:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH10], say=[0, 2])]),
        card("The words of 단어 복습 2", "In the audio activity three clips explain welfare policies; you write the related word from the box (육아휴직, 건강보험, 무상급식, 장애인 복지) and its English meaning. The box words are below; the English is mine:", tables=[ktable(_AUD10)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ10], say=[2]), ktable(_HJW10)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word similar in meaning to the word on the left (A. 결심: 관심, 결정, 의심, 결제; B. 공급: 수급, 환급, 보급, 자급; C. 중지: 중단, 중독, 중심, 중순). The choice of 보급 for 공급 is my reading.", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM10], say=[0, 1])]),
        card("한자어 복습 2: the word with a different meaning (my answers)", "In each line of four words circle the one whose meaning differs from the other three:", tables=[table(["Four words", "Different", "Why (mine)"], [list(r) for r in _ODD10], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L10X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001–003): three audio clips on welfare policies. They are audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH10], k=3) + _tr(_AUD10, k=3) + _tr(_HJW10, k=3) + _tr(_L10X, k=4)
        + [M("What does the syllable 給 (급) mean?", "providing; supply", ["middle", "push", "decision"], "급식."), M("What does the syllable 中 (중) mean?", "middle; hitting", ["providing", "push", "extending"], "집중."), M("What does the syllable 推 (추) mean?", "push; suppose", ["providing", "extending", "decision"], "추진."), M("What does the syllable 擴 (확) mean?", "extending; widening", ["providing", "push", "decision"], "확산."), M("What does the syllable 決 (결) mean?", "decision; determination", ["providing", "middle", "extending"], "판결.")
           , M("Which word is similar to 결심?", "결정", ["관심", "의심", "결제"], "Decision."), M("Which word is similar to 중지?", "중단", ["중독", "중심", "중순"], "Discontinuing."), M("Which of 확장, 확대, 확충, 확인 differs in meaning?", "확인", ["확장", "확대", "확충"], "Checking, not expanding."), M("Which of 추진, 추리, 추정, 추측 differs in meaning?", "추진", ["추리", "추정", "추측"], "Pushing ahead, not guessing."), M("Which of 완결, 미결, 타결, 해결 differs in meaning?", "미결", ["완결", "타결", "해결"], "Unsettled, not settled.")
           , F("정부___에 반대하다. (policy)", "정책", ["재정", "복지"], "정부정책."), F("___사회를 건설하다. (welfare)", "복지", ["재정", "의무"], "복지."), F("한국에서는 병역이 ___이다. (duty)", "의무", ["보장", "계약"], "의무."), F("___적자에 시달리다. (finance)", "재정", ["복지", "공중"], "재정적자.")]
        + [read_q("정부정책에 반대하다"), read_q("복지사회를 건설하다"), read_q("한국에서는 병역이 의무이다"), read_q("분쟁해결을 위해 나서다")]
    ),
)

# ================================================================== L2 Part 1
_PHOTO10 = [
    ("정부는 국가의 재정 적자를 줄이고자 사기업들이 보험시장에 참여하는 정책을 고려하고 있다.", "The government is considering a policy for private companies to take part in the insurance market in order to reduce the national fiscal deficit."),
    ("정부는 정부의 재정 적자 문제를 해결하고자 각 공기업을 민영화시키는 정책을 고려하고 있다.", "The government is considering a policy of privatizing each public enterprise in order to solve the government’s fiscal deficit problem."),
    ("정부는 노령인구의 취업 문제를 해결하기 위해 육십오 세 이상 노인 고용 의무 정책을 시행하고자 한다.", "The government intends to carry out a policy making it obligatory to employ people aged 65 and over, to solve the employment problem of the elderly population."),
    ("정부는 각 사업장의 임시 계약 고용직의 근무 기간을 이 년에서 사 년으로 연장하는 정책을 통과시켰다.", "The government passed a policy extending the working period of temporary contract employees at each workplace from two years to four years."),
    ("정부는 초등학교, 중학교, 고등학교의 무상 급식은 불가능하다는 입장을 보였다.", "The government took the position that free meals at elementary, middle and high schools are impossible."),
    ("정부는 장애인에게 실질적인 도움을 줄 수 있는 정책을 세워야 한다.", "The government should draw up policies that can give the disabled real help."),
]
_PEN10 = [
    ("보건복지부는 이천십일 년 기초노령연금 수급 대상자의 소득 인정액 기준을 노인 단독가구는 칠십사만 원 이하, 노인부부 가구는 백십팔만 사천 원 이하로 정했다고 삼십 일 밝혔다.", "The Ministry of Health and Welfare announced on the 30th that it set the income-recognized-amount criteria for recipients of the basic old-age pension in 2011 at 740,000 won or less for single-person elderly households and 1,184,000 won or less for elderly couple households."),
    ("이는 올해 소득 인정액 기준인 칠십만 원 이하, 노인 부부 가구 백십이만 원 이하에 비해 사만 원 오른 금액이다.", "This is an amount 40,000 won higher than this year’s criteria of 700,000 won or less (1,120,000 won or less for elderly couple households)."),
    ("기초노령연금은 만 육십오 세 이상 노인가구 중 소득 인정액, 소득과 재산을 포함해 산정한 금액이 기준보다 낮은 가구에 매달 일정액이 지급된다.", "The basic old-age pension is paid a fixed monthly amount to those households aged 65 and over whose income-recognized amount, an amount calculated including income and property, is lower than the criteria."),
    ("이에 따라 기초노령연금 지급 대상자는 올해 삼백칠십오만 명에서 내년 삼백팔십칠만 명으로 십이만 명 늘어날 것으로 보인다.", "Accordingly, the number of recipients of the basic old-age pension is expected to increase by 120,000, from 3.75 million this year to 3.87 million next year."),
    ("유월 말 현재 전국적으로 전체 노인의 육십구 퍼센트인 삼백칠십일만 명이 월 최대 구만 원, 부부가 동시에 받을 경우 각 최고 칠만 이천 원을 받고 있다.", "As of the end of June, nationwide 3.71 million people, 69 percent of all the elderly, are receiving up to 90,000 won a month (up to 72,000 won each when both spouses receive it at the same time)."),
    ("복지부 관계자는 노인 대부분이 근로빈곤층에 속하는 만큼 혜택을 늘리기 위해 소득 인정액 기준을 올렸다면서 자녀들의 소득이나 재산과 상관없이 만 육십오 세 이상 노인가구는 소득 인정액 기준에 따라 연금을 받을 수 있다고 말했다.", "An official of the Ministry of Welfare said, “Because most of the elderly belong to the working poor, we raised the income-recognized-amount criteria to increase the benefit,” and “regardless of their children’s income or property, households of the elderly aged 65 and over can receive the pension according to the income-recognized-amount criteria.”"),
    ("기초노령연금 신청은 해당 주소지 읍사무소, 면사무소, 동 주민센터 및 가까운 국민연금관리공단 지사에 하면 된다.", "Applications for the basic old-age pension can be made at the town office, township office or neighborhood community center of one’s address and at the nearest branch of the National Pension Service."),
]
_SPEAK10 = [("미국의 노령인구 비율은 어떻게 됩니까? 반 친구와 인터넷을 이용해 찾아 보세요. 또한 노인들에게 어떤 복지 혜택이 주어지는지도 토론해 보세요.", "What is the proportion of the elderly population in the United States? Find out with a classmate using the internet. Also discuss what welfare benefits are given to the elderly.")]
L2 = lesson(
    "U18 L10 · Part 1 (도입 학습): policy protests and the basic old-age pension",
    "도입 학습 · 정부 정책 · 재정 적자 · 민영화 · 노인 고용 · 무상 급식 · 기초노령연금 · 소득 인정액 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: sentences for protest photos (Kyunghyang)", "The book shows photographs of demonstrations against several policies, each with a sentence; you check the sentences that match the photos. The photos are left out; the six sentences, with my English (the numbers are spelled in Hangul and “초·중·고등학교” is written out):", examples=passage(_PHOTO10)),
        card("학습활동 3: a news article on the basic old-age pension (Kyunghyang)", "The book asks four questions: which sentence best describes the article, which word cannot replace 소득 in the underlined sentence, how much 69 percent of pensioners currently receive a month, and to translate the underlined sentence into English. The underline is not marked in the text; I take it to be the sentence defining who gets the pension (the third below), which contains 소득. The numbers are spelled in Hangul and “읍·면사무소” is written 읍사무소, 면사무소. The article, with my English:", examples=passage(_PEN10)),
        card("My answers to 학습활동 3", "1. A (the Ministry of Health and Welfare announced a criteria change for pensioners). 2. C 공급 (월급, 봉급 and 연봉 are all pay; 공급 means supply). 3. Up to 90,000 won a month (72,000 each for couples receiving it together). 4. “The basic old-age pension is paid a fixed monthly amount to those households aged 65 and over whose income-recognized amount (an amount calculated including income and property) is lower than the criteria.”"),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK10)),
        card("Activities left out", "학습활동 2 (Listening, tracks 004 and 005): two YTN news items on policies the government will carry out: you tick the related field (education, politics, economics, welfare) and write the detailed policy in English. 학습활동 4 (Listening, track 006): a YTN news item on Seoul’s new welfare policy: why it was developed, its four measures (one given: building care facilities for elderly people with Alzheimer’s disease) and how it will be implemented. They are audio. The photographs of 학습활동 1 are left out too."),
    ],
    exercises=uniq(
        _tr(_PHOTO10, k=3) + _tr(_PEN10, k=3)
        + [M("Which policy is the government said to consider to reduce the deficit?", "Privatizing public enterprises", ["Closing all schools", "Raising pensions for everyone", "Banning private insurance"], "민영화."), M("How long is the working period for temporary contract workers extended to?", "From two years to four years", ["From one year to two years", "From four years to six years", "From two years to ten years"], "이 년에서 사 년."), M("What is the criterion for a single-person elderly household in 2011?", "740,000 won or less", ["700,000 won or less", "1,184,000 won or less", "90,000 won or less"], "칠십사만 원."), M("How many recipients are expected next year?", "3.87 million", ["3.75 million", "3.71 million", "12 million"], "삼백팔십칠만."), M("What is the maximum monthly pension?", "90,000 won", ["72,000 won", "740,000 won", "40,000 won"], "구만 원."), M("What percentage of the elderly is receiving the pension now?", "69 percent", ["12 percent", "375 percent", "9 percent"], "육십구 퍼센트.")]
        + [F("정부는 공기업을 ___시키는 정책을 고려하고 있다. (privatize)", "민영화", ["국유화", "융합"], "민영화."), F("노인 고용 ___ 정책을 시행하고자 한다. (obligation)", "의무", ["계약", "자격"], "의무."), F("기초___연금 (old-age)", "노령", ["청년", "아동"], "기초노령연금."), F("소득 ___액 기준 (recognized)", "인정", ["기부", "확인"], "소득 인정액.")]
        + [read_q("기초노령연금은 만 육십오 세 이상 노인가구에 매달 일정액이 지급된다"), read_q("정부는 장애인에게 실질적인 도움을 줄 수 있는 정책을 세워야 한다"), read_q("정부는 공기업을 민영화시키는 정책을 고려하고 있다"), read_q("노인들에게 어떤 복지 혜택이 주어지는지 토론해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("실효성", "(實效性) effectiveness", "새로운 제도가 실효성이 없다는 지적이 일고 있습니다."),
        ("융합(하다/되다)", "(融合) blend; fusion (to blend/to be blended)", "이 제품은 미디어와 이동통신 기술을 융합한 것입니다.", "화합하다"),
    ]),
    ("학습활동 3", [
        ("국민연금관리공단", "(國民年金管理公團) the National Pension System", ""),
        ("노령연금", "(老齡年金) an old-age pension", "노령연금을 받을 수 있는 나이가 몇 세입니까?"),
    ]),
    ("학습활동 4", [
        ("전환점", "(轉換點) a turning point", "인터넷의 발명은 현대 문화의 큰 전환점이 되었다."),
    ]),
]
L3 = lesson(
    "U18 L10 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 실효성 · 융합 · 국민연금관리공단 · 노령연금 · 전환점",
    requires=[],
    cards=[card("A note on the Korean in this list", "국민연금관리공단 is the National Pension System’s management corporation (the article calls its branch 국민연금관리공단 지사); it has no example in the book. 융합 lists 화합하다 as related. The list is short (five entries); the activities of Part 1 use many words that are not listed, since they are reviewed in earlier lessons.")] + vocab_cards(_V1),
    exercises=uniq([M("What does 국민연금관리공단 stand for?", "the National Pension System", ["a turning point", "an old-age pension", "effectiveness"], "國民年金管理公團."), M("What does 실효성 mean?", "effectiveness", ["a turning point", "an old-age pension", "a blend"], "實效性."), M("What does 전환점 mean?", "a turning point", ["effectiveness", "a blend", "a pension"], "轉換點."), M("What does 노령연금 mean?", "an old-age pension", ["a health insurance", "a turning point", "a loan"], "老齡年金."), M("What does 융합 mean?", "blend; fusion", ["effectiveness", "a pension", "a turning point"], "融合."), read_q("새로운 제도가 실효성이 없다는 지적이 일고 있습니다"), read_q("인터넷의 발명은 현대 문화의 큰 전환점이 되었다"), read_q("노령연금을 받을 수 있는 나이가 몇 세입니까")]),
)

# ================================================================== L4 Part 2
_DIS10 = [
    ("진짜 자립하려면 주거 지원 꼭 필요", "To really live independently, housing support is a must"),
    ("어릴 때부터 누워서 지냈어요. 심심하면 혼자서 라디오를 뜯었다가 다시 조립했지요. 이제 그 솜씨를 살려 전파사를 차리고 싶어요.", "“Since I was little I have spent my days lying down. When I was bored I took a radio apart by myself and put it together again. Now I want to use that skill and open a radio repair shop.”"),
    ("지체장애 뇌병변 일 급 장애인인 한 남자는 스물한 살 때부터 십구 년 동안 시설에서만 살았다.", "A man with a physical disability (brain lesion) of grade 1 lived only in a facility for 19 years from the age of twenty-one."),
    ("그는 지금 홀로서기를 준비 중이다.", "He is now preparing to stand on his own."),
    ("집단생활이 몸에 밴 그는 자립한다는 게 무척 힘들다는 것을 잘 안다.", "Having group life ingrained in him, he knows well that living independently is extremely hard."),
    ("하지만 스스로 헤쳐 나간다.", "But he is making his own way."),
    ("지하철을 타는 걸 생각하는 것만으로도 너무 행복하다.", "Just thinking of riding the subway makes him very happy."),
    ("그는 지금 중증장애인요양시설에서 독립하기 위해 서울의 한 구청을 상대로 소송을 진행 중이다.", "He is now pursuing a lawsuit against a Seoul district office in order to become independent from a care facility for the severely disabled."),
    ("자립생활을 위해서는 주거지원이 필수적이다.", "Housing support is essential for independent living."),
    ("법원은 구체적인 규정이 없다는 이유로 주거지원을 정부의 의무가 아니라고 판단하고 있지만, 미국 등 다른 나라에서는 이미 오래전부터 자립 생활권을 장애인의 기본권으로 보고 있다.", "The court judges that housing support is not the government’s duty on the grounds that there is no specific provision, but in other countries such as the United States the right to independent living has long been seen as a basic right of the disabled."),
    ("천구백구십구 년 미국에서 두 명의 정신장애인이 시설수용이 아닌 지역사회 자립 형태로 지원해 달라는 소송에서 승소한 적도 있다.", "In 1999 in the United States, two people with mental disabilities also won a lawsuit asking to be supported through independent living in the community rather than institutional confinement."),
    ("옴스테드 판결로 불리는 이 판례는 수많은 정신장애인의 탈시설과 자립생활에 영향을 끼쳤다.", "This precedent, called the “Olmstead decision,” influenced the deinstitutionalization and independent living of a great many people with mental disabilities."),
    ("흔히 뇌성마비로 불리는 뇌병변은 뇌신경의 손상 등으로 근육이 굳어 힘이 없거나 운동장애를 일으킨다.", "Brain lesions, commonly called cerebral palsy, cause muscles to stiffen and weaken or cause movement disorders through damage to the brain nerves and so on."),
    ("하지만 인지능력은 정상인과 같아서 스스로 생활과 교육과 학습능력을 갖춰, 자립생활을 하는 데 부족함이 없다는 평가가 나와 있다.", "But since cognitive ability is the same as that of persons without the condition, they have the ability to live, be educated and learn by themselves, and there is an assessment that they lack nothing for independent living."),
    ("그는 모든 장애인들, 특히 뇌병변 동료들에게 희망을 주기 위해 끝까지 싸우겠다며 그들이 시설을 나와 자립해 자유롭게 살게 하고 싶다고 밝혔다.", "He said he would fight to the end to give hope to all the disabled, especially his fellow brain-lesion sufferers, and that he wants them to leave facilities, become independent and live freely."),
    ("시설장애인들의 자립을 돕는 장애와 인권 발바닥 행동의 박숙경 활동가는 시설 장애인들은 자신의 선택권을 보장받지 못한 채 살아 왔다며 정부는 공동생활가정이나 자립생활 등으로 지원방식을 변경해야 한다고 주장했다.", "Activist Park Suk-gyeong of “Disability and Human Rights Footprint Action,” which helps the independence of disabled people in facilities, argued that disabled people in facilities have lived without their right of choice being guaranteed, and that the government should change its method of support to group homes or independent living."),
]
_SPEAK10B = [("미국은 다른 나라에 비해서 장애인을 위한 정책이나 배려가 잘 되어 있는 나라로 꼽힙니다. 다른 나라에 장애인을 위한 정책을 제안한다면 어떤 것들이 우선되어야 할지 함께 토론해 보세요.", "The United States is counted as a country with well-developed policies and consideration for the disabled compared with other countries. If you were to propose policies for the disabled to another country, discuss together which should come first.")]
L4 = lesson(
    "U18 L10 · Part 2 (본 학습): independent living for the disabled",
    "본 학습 · 장애인 · 자립 · 주거 지원 · 시설 · 뇌병변 · 옴스테드 판결 · 기본권 · 선택권 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a news article on independent living (Hankyoreh)", "The book asks four questions: biographical information on the man in the article, why he is suing the district office, what the underlined phrase 옴스테드 판결 refers to, and what the underlined activist suggests to the government. In the book the man is named, with his age and the name of his facility (and a photo); because he is a private individual, I leave out his name, age and the facility’s name and call him “a man” (the questions name him as 황인현). The activist is named as in the article (a quoted representative of a group). The numbers are spelled in Hangul, the dots between words are written out as 와/과 or commas, and “1급” is 일 급. The article, with my English:", examples=passage(_DIS10)),
        card("My answers to 학습활동 2", "1. The man has a grade-1 physical disability (brain lesion); he lay down for much of his childhood and took radios apart and put them together again, and wants to open a radio repair shop; from age 21 he lived in a facility for 19 years and is now preparing to live independently. 2. He wants to leave the care facility and live independently, and he sues because housing support is essential for that but the court holds it is not the government’s duty for lack of a specific provision. 3. The Olmstead decision is the 1999 US ruling in which two people with mental disabilities won their lawsuit asking to be supported in community independent living rather than in an institution; it influenced the deinstitutionalization and independent living of many people. 4. The activist 박숙경 suggests that the government change its method of support to group homes or independent living, since people in facilities have not had their right of choice guaranteed."),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK10B)),
        card("Activities left out", "학습활동 1 (Listening, track 007): a YTN news item on health insurance: the changes made next year corresponding with 5.9 percent up, 1.6 percent up and 20 percent down, the main reason the ministry raised the premium, and a check-list of how the new premium will affect health care (premiums for the self-employed will increase; benefits for newborn babies and challenged people will be reduced; expensive cancer medication will be covered; government support for prenatal care will increase). 학습활동 3 (Listening, track 008): a KBS interview about the disabled: the interviewee’s biography, what Mr. Chung suggests about the annual event for the handicapped, what policies the Seongnam city government plans to enact, and what he suggests that non-disabled people do. They are audio."),
    ],
    exercises=uniq(
        _tr(_DIS10, k=3)
        + [M("How long did the man live in a facility?", "19 years", ["9 years", "21 years", "40 years"], "십구 년."), M("What does he want to open?", "A radio repair shop", ["A restaurant", "A school", "A hospital"], "전파사."), M("What is the lawsuit against?", "A Seoul district office", ["The Supreme Court", "A hospital", "The president"], "구청."), M("Why does the court say housing support is not the government’s duty?", "There is no specific provision", ["It costs too much", "The man is not disabled", "It is the family’s duty"], "구체적인 규정이 없다."), M("What is the Olmstead decision?", "A 1999 US ruling for community independent living", ["A Korean law on pensions", "A 2010 UN treaty", "A court order on schools"], "옴스테드 판결."), M("What does 박숙경 want the government to change?", "The method of support, toward group homes or independent living", ["The date of elections", "The tax system", "The school curriculum"], "지원방식.")]
        + [F("자립생활을 위해서는 주거지원이 ___적이다. (essential)", "필수", ["의무", "일회"], "필수적."), F("집단생활이 몸에 ___ 그는 자립이 힘든 것을 안다. (ingrained)", "밴", ["찬", "된"], "몸에 배다."), F("국가는 국민의 ___권을 보장해야 한다. (basic)", "기본", ["선거", "자립"], "기본권."), F("그는 지금 ___서기를 준비 중이다. (on one’s own)", "홀로", ["혼자", "스스로"], "홀로서기.")]
        + [read_q("자립생활을 위해서는 주거지원이 필수적이다"), read_q("정부는 공동생활가정이나 자립생활 등으로 지원방식을 변경해야 한다"), read_q("시설 장애인들은 자신의 선택권을 보장받지 못한 채 살아 왔다"), read_q("다른 나라에 장애인을 위한 정책을 제안한다면 어떤 것들이 우선되어야 할까요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("의결(하다/되다)", "(議決) a decision through discussion (to decide through discussion; to resolve/to be passed)", "새해 예산안이 국회에서 의결되었습니다.", "결정하다"),
        ("의료수가", "(醫療酬價) the charge for medical treatment; a medical fee", ""),
        ("자영업자", "(自營業者) a self-employed person", "한국 이민 일 세대 중에는 자영업을 하는 사람들이 많다."),
        ("중증질환", "(重症疾患) a serious disease; a serious illness", "이 보험은 중증질환자에게 특히 좋은 상품입니다."),
        ("항목", "(項目) an item; an article", "이 항목에 대해 질문이 있습니다."),
    ]),
    ("학습활동 2", [
        ("기본권", "(基本權) basic (fundamental) human rights; natural rights", "국가는 국민의 기본권을 보장해야 한다."),
        ("뇌병변", "(腦病變) brain lesions", "", "뇌성마비"),
        ("몸에 배다", "to be accustomed; to be used to", "몸에 밴 나쁜 습관은 고치기 어렵습니다.", "익숙해지다"),
        ("조립(하다/되다)", "(組立) assembling (to assemble; to put together/to be assembled)", "우리 아이는 조립하는 장난감을 좋아합니다."),
        ("판례", "(判例) a (judicial) precedent", "이번 판결은 기존의 판례를 깨는 결정입니다."),
        ("홀로서기", "becoming independent; independence; “standing alone”", "대학 졸업 후 많은 학생들이 홀로서기를 시도한다.", "자립"),
    ]),
    ("학습활동 3", [
        ("거창하다", "(巨創) to be grand in scale; to be enormous", "그 연설은 거창하게 시작했지만 내용이 별로 없었어요."),
        ("계기", "(契機) an opportunity that triggers or causes a change; a turning point", "그는 결혼을 계기로 담배를 끊었다.", "동기"),
        ("귀를 기울이다", "(idiom) to pay heed to; to listen carefully; “to lean ears (toward)”", "제 말에 귀를 좀 기울여 주세요."),
        ("일회성", "(一回性) one-time (event); single shot", "일회성으로 끝나는 행사가 아닌 지속적인 관심이 필요합니다.", "지속성"),
        ("재활(하다)", "(再活) rehabilitation (to rehabilitate)", "영화배우들 중에는 마약 재활 치료를 받는 사람들이 많다.", "재기하다"),
        ("지자체", "(地自體) short form of 지방자치단체 (an [autonomous] local government)", "지자체 선거"),
    ]),
]
L5 = lesson(
    "U18 L10 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 의결 · 의료수가 · 자영업자 · 중증질환 · 항목 · 기본권 · 뇌병변 · 몸에 배다 · 조립 · 판례 · 홀로서기 · 거창하다 · 계기 · 귀를 기울이다 · 일회성 · 재활 · 지자체",
    requires=[],
    cards=[card("A note on the Korean in this list", "계기 carries the homonym 계기 (計器), “a meter; an instrument”; 동기 is its related word. 뇌병변 lists 뇌성마비 (cerebral palsy) as related. 의료수가 has no example in the book. The example of 자영업자 had “1세대”, which I spelled 일 세대. 지자체’s example is only the phrase 지자체 선거. The English of 홀로서기 is the book’s (“becoming independent; independence”).")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3
_KIM10 = [
    ("김문수 복지 권한 중앙 집중 바꿔야", "Kim Moon-soo: the concentration of welfare authority in the center must change"),
    ("김문수 경기지사가 이번에는 각종 복지정책에 대해 쓴소리를 했다.", "Gyeonggi Governor Kim Moon-soo this time spoke bitter words about various welfare policies."),
    ("김 지사는 이십삼 일 오후 코엑스에서 열린 경기복지재단 창립 삼 주년 기념 심포지엄에 참석, 축사를 통해 복지에 관한 한 중앙에 집중된 힘이 바뀌어야 한다고 주장했다.", "On the afternoon of the 23rd Governor Kim attended the symposium commemorating the third anniversary of the founding of the Gyeonggi Welfare Foundation, held at COEX, and in his congratulatory address argued that as far as welfare is concerned, the power concentrated in the center must change."),
    ("그는 현재 한국의 복지정책에 대해 사람 위주가 아니라 높은 곳, 중앙부처에서 하나씩 하고 있다고 지적한 뒤 너무 높은 곳에서 쥐고 있는 권한을 과감히 아래로 주어야 한다고 말했다.", "About Korea’s current welfare policy, he pointed out that “it is not centered on people but is done one by one in a high place, the central ministries,” and then said, “The authority held in too high a place must be boldly given down.”"),
    ("그동안 정부의 권한을 지방정부에 대폭 이양해야 한다고 주장해 온 김 지사가 복지분야 정책 역시 정부가 갖고 있는 권한을 지방에 이양할 것을 요구한 것이다.", "Governor Kim, who has been arguing all along that the government’s authority should be transferred on a large scale to local governments, thus demanded that for welfare policy too the authority the government holds be transferred to the localities."),
    ("김 지사는 어린이 키우는 것만 해도 담당 부처가 복지부와 여성부 어디인지 모르겠다고 비판한 뒤 복지정책이 돈, 제도 위주가 아닌 가장 어려운 사람을 중심으로 생각하는 근본적인 발상의 전환이 필요하다고 밝혔다.", "After criticizing that “even for raising children, I do not know which is the ministry in charge, the Ministry of Welfare or the Ministry of Gender Equality,” Governor Kim said that “a fundamental change of thinking is needed, in which welfare policy is thought of centered on the most needy people rather than centered on money and institutions.”"),
    ("그는 복지와 관련해 재원 면에서 지자체가 가질 수 있는 힘이 없고, 대통령이 말을 해야 문제가 해결된다고도 했다.", "He also said that, in connection with welfare, local governments have no power in terms of financial resources, and that problems are solved only when the president speaks."),
    ("김 지사는 복지는 적은 돈으로 현장 및 사람 맞춤형, 통합형으로 돼야 한다고 강조했다.", "Governor Kim stressed that welfare must be on-site, tailored to people and integrated, using little money."),
    ("이날 심포지엄에서는 복지 관련 분야 전문가 백오십여 명이 참석한 가운데 사회복지 정책의 패러다임 변화와 복지정책의 융합에 대한 주제 발표 및 토론이 이어졌다.", "At the symposium that day, with some 150 experts in welfare-related fields attending, topic presentations and discussions followed on the paradigm change in social welfare policy and the fusion of welfare policies."),
]
_TAX10 = [
    ("청와대를 비롯해 정치권에서 감세정책 철회 논쟁이 한창이다.", "In political circles, including the Blue House, the debate over withdrawing the tax-cut policy is in full swing."),
    ("구체적인 내용을 뜯어 보면 한심하다.", "Pulled apart in its details, it is pathetic."),
    ("법인세와 근로소득세의 최고 구간 세율을 예정대로 인하하느니 마느니 하는 수준의 논란에 그치고 있기 때문이다.", "This is because it stops at a level of dispute over whether or not to cut, as scheduled, the top-bracket rates of the corporate tax and the earned-income tax."),
    ("이천팔 년 구 월 세계경제 위기를 핑계로 발표된 감세정책은 이미 실패임이 드러났다.", "The tax-cut policy announced in September 2008 on the pretext of the world economic crisis has already been shown to be a failure."),
    ("먼저 국가채무가 급증했다.", "First, the national debt has soared."),
    ("관리대상수지 기준으로 이천팔 년 이명박 정부 출범 이후 올해 말까지 약 구십조 원의 재정 적자를 기록할 것으로 추정된다.", "On the basis of the managed fiscal balance, a fiscal deficit of about 90 trillion won is estimated to be recorded from the launch of the Lee Myung-bak government in 2008 to the end of this year."),
    ("외환위기 때보다 갑절 가량 늘어난 것이다.", "That is about double the increase of the time of the foreign exchange crisis."),
    ("국가채무 증가는 경기 침체와 재정부양책 남발에 따른 영향도 있지만, 감세정책의 악영향을 과소평가할 수 없다.", "The increase in national debt also has the influence of the economic slump and the reckless issue of fiscal stimulus measures, but the bad effects of the tax-cut policy cannot be underestimated."),
    ("둘째, 감세를 통한 경기진작 효과도 높이 평가하기 어렵다.", "Second, the economy-boosting effect through tax cuts is also hard to rate highly."),
    ("이천구 년 국내총생산 총액 천육십사조 원 대비 이십사 퍼센트가 넘는 공공부채를 늘린 위에 대규모 감세까지 했다.", "On top of increasing public debt of more than 24 percent of the 2009 total gross domestic product of 1,064 trillion won, they even made large-scale tax cuts."),
    ("또 온 국민이 고환율을 감내하며 수출 대기업을 도와줬는데도 올해 육 퍼센트 성장에 그친다면 이것이 자랑할 일인가.", "Moreover, even though the whole nation put up with a high exchange rate and helped the large export companies, if growth stops at 6 percent this year, is this something to boast about?"),
    ("끝으로 현 정부는 감세정책의 한 명분으로 중저소득층의 민생안정 및 소비기반 확충을 내세웠다.", "Finally, the present government put forward “stabilizing the livelihoods of the middle and low-income groups and expanding the consumption base” as one justification of the tax-cut policy."),
    ("양두구육이었다.", "It was 양두구육."),
    ("근로자 가구 소득을 다섯 개 분위로 나눴을 때 감세정책 실시 이후 최상위 오 분위 계층이 내는 경상 조세 부담은 감소 추세가 확연하다.", "When the income of worker households is divided into five quintiles, the current tax burden paid by the top fifth quintile since the tax-cut policy was carried out shows a clear downward trend."),
    ("반면 저소득층인 일, 이 분위 경상 조세 부담은 삼십에서 오십 퍼센트나 늘었다.", "In contrast, the current tax burden of the low-income first and second quintiles increased by as much as 30 to 50 percent."),
    ("저소득층의 세 부담을 늘리면서 어떻게 중저소득층의 민생 안정을 도모하고 소비기반을 확충한다는 말인가.", "How can one say one is seeking the stability of the livelihoods of the middle and low-income groups and expanding the consumption base while increasing the low-income groups’ tax burden?"),
    ("급속한 인구감소와 고령화에 따라 향후 경제 활력은 떨어지고 사회복지 수요는 급증하게 된다.", "With rapid population decline and aging, economic vitality will fall and the demand for social welfare will soar."),
    ("따라서 경제활동을 위축시키지 않으면서도 급증하는 사회복지 수요에 전략적으로 대비하는 근본적인 세수구조 개혁을 단행해야 한다.", "Therefore a fundamental reform of the tax revenue structure that prepares strategically for the soaring demand for social welfare without shrinking economic activity must be carried out."),
    ("그 기본 작업이 자산경제 부문에 대한 세 부담을 늘리고 투명한 소득 파악과 탈세에 대한 엄격한 처벌을 통해 근원적인 세 부담의 형평성을 확보하는 것임은 말할 나위도 없다.", "It goes without saying that the basic work is to increase the tax burden on the asset economy sector and secure fundamental fairness in the tax burden through transparent grasp of income and strict punishment of tax evasion."),
    ("그런데도 현 정부는 이미 실패로 드러난 부자 감세에 집착하며 천문학적인 공공부채를 남발하고 있다.", "Even so, the present government clings to the “tax cut for the rich,” already shown to be a failure, and is recklessly issuing astronomical public debt."),
    ("마치 대한민국이 자신들의 임기 동안에만 존속하는 나라인 것처럼 착각하는 모양새다.", "It looks as if they are under the illusion that the Republic of Korea is a country that exists only during their term of office."),
    ("현 정부의 무책임한 감세 및 재정 탕진은 국민 전체에 대한 범죄행위에 가깝다.", "The present government’s irresponsible tax cuts and squandering of finances come close to a criminal act against the whole people."),
]
_SPEAK10C = [("학급을 두 모둠으로 나누어 한 모둠은 복지정책에 대한 김 지사의 주장에 찬성하는 입장에서, 다른 모둠은 반대하는 입장에서 토론해 보세요.", "Divide the class into two groups and debate, one group for Governor Kim’s argument about welfare policy and the other against it.")]
L6 = lesson(
    "U18 L10 · Part 3 (심화 학습): a governor on welfare policy and an editorial on tax cuts",
    "심화 학습 · 복지 권한 · 중앙집권 · 이양 · 발상의 전환 · 감세정책 · 국가채무 · 경기진작 · 양두구육 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a governor’s opinion on welfare policy (Kyunghyang)", "The book asks four questions: Governor Kim’s opinion about the current welfare policy, a translation of the first underlined sentence, what Governor Kim thinks should happen to the welfare system (second underlined sentence), and a class debate. The underlines are not marked in the text; I take the first to be the sentence about the power concentrated in the center and the second to be the sentence about a change of thinking in welfare policy. Governor Kim is a public official, named as in the article. The numbers are spelled in Hangul, the quotation marks and parentheses are dropped, and the headline is given without the quotation marks. The article, with my English:", examples=passage(_KIM10)),
        card("My answers to 학습활동 1", "1. He thinks welfare policy is run from the top by the central ministries, one item at a time, rather than centered on people; authority held too high must be boldly handed down to local governments, and local governments lack financial resources. 2. First underlined sentence (my reading): “As far as welfare is concerned, the power concentrated in the center must change.” 3. Second underlined sentence (my reading): welfare policy needs a fundamental change of thinking, centering on the most needy people rather than on money and institutions; it should be on-site, tailored to people, integrated and low-cost."),
        card("학습활동 3: an editorial on the tax-cut policy (Hankyoreh)", "The book asks three questions: the tone of the passage (A. objective, B. sympathetic, C. critical, D. tender), three facts the author gives to show that the tax-cut policy has failed, and which sentence best explains the underlined word 양두구육 (four choices A–D). The editorial is long and, in the book, runs onto a second page. The numbers are spelled in Hangul, “GDP” is dropped after 국내총생산, and the quotation marks are dropped. The editorial, with my English:", examples=passage(_TAX10)),
        card("My answers to 학습활동 3", "1. C (critical). 2. First: the national debt has soared; about 90 trillion won of fiscal deficit by the end of this year since 2008, about double the increase at the time of the foreign exchange crisis. Second: the economy-boosting effect is hard to rate highly; public debt of more than 24 percent of 2009 GDP was added on top of large-scale tax cuts, and growth still stops at 6 percent. Third: the stated aim of stabilizing the livelihoods of the middle and low-income groups was a sham; after the cuts the tax burden of the top quintile fell clearly while that of the first and second quintiles rose 30 to 50 percent. 3. C (the policy looks as if it is for the poor but in fact helps only the rich). The book does not gloss 양두구육; the Chinese proverb 羊頭狗肉 means “sheep’s head, dog meat,” that is, advertising one thing and selling another (my gloss)."),
        card("말해 봅시다! (speaking)", "The book’s debate prompt of 학습활동 1 (the English is mine):", examples=passage(_SPEAK10C)),
        card("Activities left out", "학습활동 2 (Listening, Speaking, track 009): a debate program on TV (MBC): which policy is the topic (A. 건강보험, B. 임대주택, C. 비정규직, D. 무상급식), the attitude of the man who is against the policy (rational, arrogant, angry, confident), a summary of the facts the congressman uses to support the policy, and a class discussion on whether the government should provide all students with free meals. It is video and audio; the vocabulary of the activity (결식아동, 생활보호 대상자, 엄연하다) points to free school meals, which I take to be choice D (my guess)."),
    ],
    exercises=uniq(
        _tr(_KIM10, k=3) + _tr(_TAX10, k=3)
        + [M("What does Governor Kim say about welfare authority?", "It should be handed down from the center to local governments", ["It should be concentrated in the president", "It should go to private companies", "It should be abolished"], "이양."), M("What kind of welfare does he stress?", "On-site, tailored to people, integrated, with little money", ["Money-centered and institution-centered", "Only for the rich", "Only for children"], "맞춤형, 통합형."), M("What is the editorial’s tone?", "Critical", ["Objective", "Sympathetic", "Tender"], "C."), M("How large a fiscal deficit does the editorial cite?", "About 90 trillion won", ["About 9 trillion won", "About 1,064 trillion won", "About 24 trillion won"], "구십조 원."), M("By how much did the tax burden of the low-income quintiles rise?", "30 to 50 percent", ["3 to 5 percent", "300 percent", "It fell"], "삼십에서 오십 퍼센트."), M("What does 양두구육 describe here?", "A policy that looks pro-poor but helps only the rich", ["A policy that most people want", "A policy that helps the self-employed", "A tax on the rich"], "C.")]
        + [F("복지 권한을 지방으로 ___해야 한다. (to transfer)", "이양", ["의결", "집착"], "이양."), F("근본적인 ___의 전환이 필요하다. (thinking)", "발상", ["계기", "재원"], "발상의 전환."), F("감세정책의 ___ 논쟁이 한창이다. (withdrawal)", "철회", ["의결", "도모"], "철회."), F("저소득층의 세 부담을 ___면서 민생 안정을 도모한다는 말인가. (increasing)", "늘리", ["줄이", "없애"], "늘리다.")]
        + [read_q("복지에 관한 한 중앙에 집중된 힘이 바뀌어야 한다"), read_q("복지정책이 돈과 제도 위주가 아닌 가장 어려운 사람을 중심으로 생각해야 한다"), read_q("외환위기 때보다 갑절 가량 늘어난 것이다"), read_q("정부의 감세정책은 이미 실패임이 드러났다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("권한", "(權限) a given authority", "이 문제는 제 권한 밖의 일입니다.", "권리"),
        ("발상의 전환", "(發想轉換) paradigm shift; changing one’s way of thinking; thinking outside the box", "혁신을 위해서는 발상의 전환이 필요합니다."),
        ("이양(하다/되다)", "(移讓) transfer (of power, territory, etc.); handover (to transfer/to be transferred)", "지자체 실시 이후 중앙정부의 권한이 대부분 지방정부로 이양되었습니다."),
        ("재원", "(財源) finances; source of revenue; economic resources", "국민연금의 재원이 부족하다고 합니다."),
        ("중앙집권", "(中央集權) centralized authoritarian rule; centralized power system", "요즘은 그런 중앙집권적인 통제를 좋아하는 사람은 없습니다."),
        ("축사", "(祝辭) a congratulatory message", "이제 사장님의 축사가 이어지겠습니다."),
    ]),
    ("학습활동 2", [
        ("결식아동", "(缺食兒童) children skipping meals; underfed children", "서울 시장 당선자는 결식아동을 줄이겠다고 말했습니다."),
        ("생활보호 대상자", "(生活保護對象者) a welfare system recipient", "생활보호 대상자의 범위를 확대해야 한다는 주장이 있습니다."),
        ("엄연하다", "(儼然) to be undeniable; to be clear", "믿고 싶지 않겠지만 그것은 엄연한 현실입니다."),
    ]),
    ("학습활동 3", [
        ("경기진작", "(景氣振作) boosting of the economy", "정부의 경기진작책이 얼마나 실효가 있을지 모르겠습니다."),
        ("공공부채", "(公共負債) public debt", "올해 공공부채가 너무 많이 늘었대요."),
        ("도모하다", "(圖謀) to plan; to aim; to promote", "해외 업체와의 협력을 도모하려고 합니다.", "계획하다"),
        ("민생안정", "(民生安定) the stabilization of people’s lives; stabilized livelihoods of the people", "새 정부는 민생안정을 기조로 삼겠다고 했습니다."),
        ("세수", "(稅收) the tax revenue", "경기가 나빠지면서 세수도 줄었습니다."),
        ("위축(되다)", "(萎縮) shrinking; withering; contracting (to shrink; to be daunted; to be intimidated)", "경제 불황으로 주택 경기가 위축되었습니다."),
        ("집착(하다)", "(執着) obsession (to be obsessed with; to feel overly attached)", "그 사람은 성공에 너무 집착합니다."),
        ("착각(하다)", "(錯覺) illusion; delusion; confusion; misunderstanding (to delude; to misunderstand)", "제가 잠시 사람을 착각했어요. 죄송합니다."),
        ("탕진(하다)", "(蕩盡) dissipation; wasting; squandering (to squander; to waste)", "노름으로 재산을 다 탕진했어요."),
        ("확연하다", "(確然) to be definite; to be clear; to be plain", "두 사람의 입장 차이는 확연합니다."),
    ]),
]
L7 = lesson(
    "U18 L10 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 권한 · 발상의 전환 · 이양 · 재원 · 중앙집권 · 축사 · 결식아동 · 생활보호 대상자 · 엄연하다 · 경기진작 · 공공부채 · 도모하다 · 민생안정 · 세수 · 위축 · 집착 · 착각 · 탕진 · 확연하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives homonyms: 재원 (才媛), “a talented young woman”, and 세수 (洗手), “washing one’s face”. 발상의 전환 is printed with a gap between the two Hanja of 發想 and 轉換; I joined them. 탕진 appeared in Lesson 8 of this Unit with a similar gloss. The example of 공공부채 has the colloquial ending -대요 (“I hear that…”). The examples of 착각 have two sentences, joined. The book does not list 양두구육, which the editorial underlines.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=18, nread=16)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 10: Government Policies (정부 정책)", [L1, L2, L3, L4, L5, L6, L7])
