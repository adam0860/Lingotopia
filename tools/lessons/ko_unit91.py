"""Unit 91: KBC Semester III, Unit 18, Lesson 6 - The World Economy (세계 경제).
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
_MATCH6 = [("가난", "poverty", "가난 때문에 힘들다"), ("활성화", "vitalization; galvanization", "정책이 활성화되다"), ("투자", "an investment", "증권 투자가 증가하다"), ("차이", "a difference", "성격 차이로 싸우다"), ("인력", "human resource", "인력 채용이 감소하다"), ("물가", "price of commodities", "물가가 상승하다"), ("강화", "consolidation; reinforcement", "양국 관계가 강화되다"), ("거래", "business transaction; trade", "현금 거래가 증가하다"), ("의존", "reliance; dependence", "부모에게 의존하다"), ("구호", "relief; aid", "구호 물자를 보내다")]
_HJ6 = [("自 자", "oneself; by oneself", "자신감, 자국"), ("國 국", "nation; country; kingdom", "국영, 전국적"), ("團 단", "gathering; group", "여단, 단체"), ("同 동", "the same; together (co-; col-; com-; con-; cor-)", "동거, 동감"), ("貧 빈", "poverty; shortage", "빈혈, 빈약")]
_HJW6 = [("자신감", "self-confidence"), ("자국", "one’s own country"), ("국영", "state-run; operated by the government"), ("전국적", "nationwide"), ("여단", "a brigade"), ("단체", "a group"), ("동거", "cohabitation"), ("동감", "an agreement; “same feeling”"), ("빈혈", "anemia"), ("빈약", "poorness; scantiness")]
_SIM6 = [("협동", "협력", "cooperation: collaboration"), ("단합", "단결", "unity: solidarity"), ("동일하다", "같다", "to be identical: to be the same")]
_OPP6 = [("단체", "개인", "a group: an individual"), ("자율", "타율", "autonomy: heteronomy"), ("빈곤", "부유", "poverty: wealth")]
_L6X = [("협상", "negotiation"), ("진동", "vibration"), ("이동", "movement"), ("분단", "division"), ("단속", "a crackdown"), ("공단", "an industrial complex"), ("동조하다", "to side with"), ("동의하다", "to agree"), ("협동하다", "to cooperate"), ("수단", "a means"), ("집단", "a group"), ("전체", "the whole"), ("세율", "a tax rate"), ("이율", "an interest rate"), ("비율", "a ratio"), ("빈부", "rich and poor"), ("극빈", "extreme poverty"), ("부족", "shortage")]
L1 = lesson(
    "U18 L6 · Review: world-economy words and Sino-Korean 自 國 團 同 貧",
    "세계 경제 · 단어 복습 · 한자어 복습 · 가난 · 활성화 · 투자 · 인력 · 물가 · 강화 · 거래 · 의존 · 구호 · 自 國 團 同 貧",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its meaning", "The book gives ten phrases with a word underlined and ten English meanings. The underline is not marked in the text; the pairs below are my reading:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH6], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ6], say=[2]), ktable(_HJW6)]),
        card("한자어 복습 1: the word closest in meaning (my answers)", "Circle the word closest in meaning to the word on the left (A. 협동: 협상, 협력, 진동, 이동; B. 단합: 분단, 단속, 공단, 단결; C. 동일하다: 동조하다, 같다, 동의하다, 협동하다).", tables=[table(["Word", "Closest (my answer)", "Meaning"], [list(r) for r in _SIM6], say=[0, 1])]),
        card("한자어 복습 2: the word with the opposite meaning (my answers)", "Circle the word opposite in meaning to the word on the left (A. 단체: 수단, 개인, 집단, 전체; B. 자율: 세율, 타율, 이율, 비율; C. 빈곤: 부유, 부족, 빈부, 극빈).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP6], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L6X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001–003): you hear three items, choose the related word from a box (경제협력, 관세협상, 무상원조, 시장개척) and write its English meaning. It is audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH6], k=3) + _tr(_HJW6, k=3) + _tr(_L6X, k=4)
        + [M("What does the syllable 自 (자) mean?", "oneself; by oneself", ["nation", "group", "poverty"], "자신감."), M("What does the syllable 國 (국) mean?", "nation; country; kingdom", ["oneself", "group", "the same"], "국영."), M("What does the syllable 團 (단) mean?", "gathering; group", ["nation", "the same", "poverty"], "단체."), M("What does the syllable 同 (동) mean?", "the same; together", ["oneself", "group", "poverty"], "동감."), M("What does the syllable 貧 (빈) mean?", "poverty; shortage", ["nation", "group", "the same"], "빈약.")
           , M("Which word is closest to 협동?", "협력", ["협상", "진동", "이동"], "Cooperation."), M("Which word is closest to 단합?", "단결", ["분단", "단속", "공단"], "Unity."), M("Which word is the opposite of 단체?", "개인", ["수단", "집단", "전체"], "An individual."), M("Which word is the opposite of 자율?", "타율", ["세율", "이율", "비율"], "Heteronomy."), M("Which word is the opposite of 빈곤?", "부유", ["부족", "빈부", "극빈"], "Wealth.")
           , F("___ 때문에 힘들다. (poverty)", "가난", ["의존", "구호"], "가난."), F("물___가 상승하다. (prices)", "가", ["거래", "강화"], "물가."), F("부모에게 ___하다. (to depend)", "의존", ["구호", "거래"], "의존하다."), F("___ 물자를 보내다. (relief)", "구호", ["투자", "물가"], "구호 물자.")]
        + [read_q("가난 때문에 힘들다"), read_q("증권 투자가 증가하다"), read_q("양국 관계가 강화되다"), read_q("부모에게 의존하다")]
    ),
)

# ================================================================== L2 Part 1
_RARE6 = [
    ("희토류 금속은 스칸듐, 이트륨 등 희귀한 금속 원소를 지칭하며 아이팟에서부터 풍력터빈, 컴퓨터, 휴대전화, 하이브리드 자동차, 미사일까지 첨단기술 제품 제조에 필수적이며 중국은 천구백팔십 년대부터 저가로 희토류 금속을 수출해 왔다.", "Rare earth metals refer to rare metallic elements such as scandium and yttrium; they are essential for manufacturing high-tech products from iPods to wind turbines, computers, mobile phones, hybrid cars and missiles, and China has exported rare earth metals at low prices since the 1980s."),
    ("이 때문에 미국, 유럽연합 등은 경제성이 떨어진 자국 광산을 폐쇄하는 대신 중국산에 대한 의존도를 높여 왔으며 현재 중국의 세계 시장점유율은 구십오 퍼센트에 달한다.", "For this reason the United States, the European Union and others have, instead of closing their own mines that lost economic viability, raised their dependence on Chinese products, and China’s current share of the world market reaches 95 percent."),
    ("희토류 대중 의존도가 커지는 가운데 중국은 최근 몇 년 새 사실상 수출 통제에 나서고 있으며 이로 인해 공급난에 처하게 된 미국, 일본, 유럽연합, 멕시코 등은 중국이 부당하게 희토류 아홉 개 금속 수출을 제한하고 있다며 세계무역기구에 제소한 데 이어 자구책 강구에 나서고 있다.", "While dependence on China for rare earths grows, China has in the last few years in effect taken to controlling exports, and the United States, Japan, the European Union, Mexico and others, which have fallen into supply shortages because of this, sued before the World Trade Organization, saying that China is unjustly restricting the export of nine rare earth metals, and are following up by seeking self-help measures."),
]
_ANG6 = [
    ("나라는 석유 부자, 그러나 국민은 지독한 가난", "The country is rich in oil, but the people are terribly poor"),
    ("앙골라는 지난해 석유 수출로 삼백억 달러, 약 이십팔조 오천억 원이라는 거금을 벌었다.", "Last year Angola earned a huge sum of 30 billion dollars (about 28.5 trillion won) from oil exports."),
    ("세계적인 반도체회사를 가진 한국이 반도체 수출을 통해 번 돈과 맞먹는다.", "It matches the money that Korea, which has world-class semiconductor companies, earns from semiconductor exports."),
    ("그러면 석유 수입은 앙골라 보통 사람들의 생활에 얼마나 도움이 되었을까.", "Then how much has the oil income helped the lives of ordinary Angolans?"),
    ("대답은 전혀 아니다라는 것이다.", "The answer is “not at all.”"),
    ("석유 팔아 번 돈이 국민들에게 돌아가지 않는 이유는 간단하다.", "The reason the money earned by selling oil does not go back to the people is simple."),
    ("만성화된 아프리카 국가 지도자들의 부패 때문이다.", "It is because of the chronic corruption of African national leaders."),
    ("아프리카 다른 나라들처럼 앙골라도 정부의 투명성이 크게 부족하다.", "Like other African countries, Angola also greatly lacks government transparency."),
]
_SUU6 = [
    ("수입의 감소로 외식을 하지 않는 가정이 늘어나고 있습니다.", "A. Because of the decrease in income, the number of households that do not eat out is increasing."),
    ("올해 화장품 수입량이 전년에 비해 삼십 퍼센트 증가했습니다.", "B. This year’s import volume of cosmetics rose 30 percent compared with the year before."),
    ("한국의 컴퓨터 제조 회사들은 중국으로부터 금속을 수입합니다.", "C. Korean computer manufacturers import metals from China."),
    ("자동차 판매 수입이 증가했지만 이 회사는 여전히 적자입니다.", "D. Although the income from car sales rose, this company is still in the red."),
]
_SPEAK6 = [("본인이 사용하는 외국산 제품 세 개를 골라 원산지, 가격, 성능 등에 대해서 이야기해 보세요.", "Choose three foreign-made products you use and talk about their origin, price, performance and so on.")]
L2 = lesson(
    "U18 L6 · Part 1 (도입 학습): rare earths and oil-rich Angola",
    "도입 학습 · 희토류 · 자원의 무기화 · 앙골라 · 석유 수출 · 부패 · 수입 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a newspaper article on China’s rare earth metals (Kyunghyang)", "The book asks three questions in English: what 희토류 금속 is and how it is used; what the United States and the European Union depend on China for and why; and what China has been doing in recent years and how other countries reacted. The numbers are spelled in Hangul; “EU” and “WTO” are dropped (the Korean names stand). The article, with my English:", examples=passage(_RARE6)),
        card("My answers to 학습활동 2", "A. 희토류 금속 are rare metallic elements such as scandium and yttrium, essential for making high-tech products such as iPods, wind turbines, computers, mobile phones, hybrid cars and missiles. B. They depend on China for rare earth metals, because China has exported them cheaply since the 1980s, so they closed their own less economical mines and China now holds 95 percent of the world market. C. China has in effect been controlling its exports of rare earths; the US, Japan, the EU, Mexico and others sued it before the WTO, saying it unjustly restricts the export of nine metals, and are looking for measures to help themselves."),
        card("학습활동 3: a newspaper article on Angola (Kyunghyang)", "The book asks three questions: what the underlined 300억 달러 refers to; the causes of poverty in Angola; and the meaning of the underlined 수입 in the article, with the choice of two of four sentences that use it the same way. The figures are spelled in Hangul. The article, with my English:", examples=passage(_ANG6)),
        card("The four sentences for question 3", "The book’s four sentences, with my English (the book’s “증가했 습니다” has a stray space and 30퍼센트 is in digits, corrected here):", examples=passage(_SUU6)),
        card("My answers to 학습활동 3", "1. The 30 billion dollars (about 28.5 trillion won) that Angola earned from oil exports last year. 2. The chronic corruption of African national leaders, and the great lack of government transparency; the oil money does not go back to the people. 3. In the article 수입 means “income; revenue” (money earned). The two sentences that use it this way: A and D (B and C use 수입 for “import”)."),
        card("말해 봅시다! (speaking)", "The book’s prompt (it says “3개”, which I wrote 세 개; the English is mine):", examples=passage(_SPEAK6)),
        card("Activities left out", "학습활동 1 (Reading): three sets of charts and pictures (from Hankyoreh and Kyunghyang), for each of which you tick the related captions (e.g. mineral resource output around the world; crude oil deposits; imports of crude oil; crude oil production by oil companies; profits of major oil companies; number of employees and wages in oil companies; poverty in African countries; United Nations medical funds support to African nations; living cost in African countries). They are pictures. 학습활동 2, part 2 (Listening, track 004): a YTN news item on China’s rare earths: what 자원의 무기화 refers to, what China’s policy change is and what resource specialists have warned. It is audio."),
    ],
    exercises=uniq(
        _tr(_RARE6, k=3) + _tr(_ANG6, k=3) + _tr(_SUU6, k=3)
        + [M("Which country holds about 95 percent of the world rare earth market?", "China", ["The United States", "Japan", "Mexico"], "중국의 세계 시장점유율은 구십오 퍼센트."), M("What did the US, Japan, the EU and Mexico do about China’s export restrictions?", "Sued before the World Trade Organization", ["Imposed sanctions", "Started mining in Africa", "Ended trade with China"], "세계무역기구에 제소."), M("How much did Angola earn from oil exports last year?", "30 billion dollars", ["3 billion dollars", "300 billion dollars", "28.5 billion dollars"], "삼백억 달러."), M("Why does the oil money not go back to Angolan people?", "Because of corruption", ["Because of low oil prices", "Because of wars", "Because of taxes"], "부패."), M("What does 수입 mean in the Angola article?", "Income", ["Import", "Imitation", "Purchase"], "Income."), M("Which sentence uses 수입 as “import”?", "C", ["A", "D", "None"], "수입하다.")]
        + [F("희토류 금속은 첨단기술 제품 제조에 ___적이다. (essential)", "필수", ["부당", "만성"], "필수적."), F("중국의 세계 시장___율은 구십오 퍼센트에 달한다. (share)", "점유", ["독점", "확보"], "시장점유율."), F("석유 수입은 앙골라 보통 사람들의 생활에 도움이 되지 못했다. 그 이유는 ___ 때문이다. (corruption)", "부패", ["제소", "할당"], "부패."), F("앙골라는 석유 수출로 번 돈이 한국의 반도체 수출 수입과 ___. (to match)", "맞먹는다", ["부패한다", "제소한다"], "맞먹다.")]
        + [read_q("희토류 금속은 첨단기술 제품 제조에 필수적이다"), read_q("앙골라는 지난해 석유 수출로 삼백억 달러를 벌었다"), read_q("만성화된 아프리카 국가 지도자들의 부패 때문이다"), read_q("외국산 제품 세 개를 골라 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("매장(하다/되다)", "(埋藏) burial (to bury/to be buried; to lie under)", "북극에는 많은 지하자원이 매장되어 있다."),
        ("현황", "(現況) present condition; current state of affairs", "연초에 재정경제부에서 경제 현황 보고서를 발표했다.", "상황"),
    ]),
    ("학습활동 2", [
        ("경향", "(傾向) a tendency; a trend; an inclination", "그 사람은 옷을 화려하게 입는 경향이 있습니다."),
        ("광산", "(鑛山) a mine; “ore mountain”", "광산이 붕괴돼 사망자가 발생했습니다."),
        ("금속", "(金屬) a metal", "여기서 많이 나오는 금속이 무엇입니까?"),
        ("대란", "(大亂) a crisis; a serious disturbance; a great commotion; “great war”", "금융대란으로 주택 가격이 폭락하고 있습니다.", "위기"),
        ("독점(하다/되다)", "(獨占) monopoly (to monopolize/to be monopolized)", "그 배우는 삼성과 독점으로 광고 계약을 맺었습니다."),
        ("부당(하다)", "(不當) unfairness (to be unjustified; to be unreasonable)", "노동자들이 회사측의 부당한 해고에 맞서 파업을 하고 있습니다."),
        ("원소", "(元素) a (chemical) element", ""),
        ("자구책", "(自救策) a measure/plan (to save oneself)", "불황을 극복하기 위한 기업의 자구책이 필요한 시기입니다.", "조치, 방안"),
        ("제소(하다/되다)", "(提訴) lawsuit (to sue/to be sued)", "철강 덤핑 문제가 공정무역위원회에 제소되었습니다.", "소송하다, 소송을 제기하다"),
        ("차원", "(次元) a dimension; a level", "이 문제는 국가 차원에서 논의되어야 합니다."),
        ("필수(적)", "(必修的) a must (required; indispensible; compulsory)", "운동은 건강유지에 필수입니다.", "생활필수품, 생필품"),
        ("할당(하다/되다)", "(割當) allocation; an assignment; an allotment (to assign; to allocate/to be assigned)", "오늘도 하루에 할당된 생산량을 채우지 못했습니다."),
        ("확보(하다/되다)", "(確保) securing (to secure/to be secured)", "경제발전을 위해서는 우수한 인력의 확보가 반드시 필요합니다."),
        ("희토류", "rare earth elements; rare earth metals; a set of 17 chemical elements in the periodic table, specifically the 15 lanthanides plus scandium and yttrium", ""),
    ]),
    ("학습활동 3", [
        ("만성", "(慢性) chronic", "만성적인 교통문제를 해결하기 위해 지하철 노선을 신설해야 합니다.", "고질적"),
        ("맞먹다", "to be equal to; to match", "이 전자제품은 일반 노동자 한 달 월급과 맞먹습니다.", "상당하다"),
        ("부패(하다/되다)", "(腐敗) corruption; decomposition; spoil (to be corrupt; to decompose)", "정부는 부정부패 문제를 해결하겠다고 했습니다."),
    ]),
]
L3 = lesson(
    "U18 L6 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 매장 · 현황 · 경향 · 광산 · 금속 · 대란 · 독점 · 부당 · 원소 · 자구책 · 제소 · 차원 · 필수 · 할당 · 확보 · 희토류 · 만성 · 맞먹다 · 부패",
    requires=[],
    cards=[card("A note on the Korean in this list", "매장 has a homonym 매장 (賣場), “a shop; a store”. The book prints the Hanja of 필수(적) as 必修(的); I kept it as printed (the usual Hanja for “a must; indispensable” is 必須). 희토류 has no Hanja and no example in the book; its long gloss is the book’s. 필수 lists 생활필수품 (생필품) as a related word; 자구책 lists 조치, 방안 as similar; 제소 lists 소송하다, 소송을 제기하다. The 광산 gloss here is “ore mountain”, while Lesson 5 glossed it “mineral mountain”.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=12)),
)

# ================================================================== L4 Part 2
_AFR6 = [
    ("한국, 뜨는 시장 아프리카의 마음을 사라", "Korea: win the heart of Africa, the rising market"),
    ("정부가 아프리카 원조를 두 배로 늘리고, 경제발전 경험 공유사업을 대폭 확대키로 하는 등 아프리카 대륙에 대한 본격적인 구애에 들어갔다.", "The government has entered a full-scale courtship of the African continent, such as doubling aid to Africa and greatly expanding projects to share its economic development experience."),
    ("우선 현재 오억 구천만 달러 수준인 대외경제협력기금 지원을 향후 오 년간 십억 구천만 달러로 확대하고, 아프리카 개발은행에 설치한 한국과 아프리카 경제협력 신탁기금을 재원으로 천백만 달러 규모의 경제발전 경험 공유 및 기술협력 사업을 진행키로 했다.", "First, it will expand support from the Economic Development Cooperation Fund, now at the level of 590 million dollars, to 1.09 billion dollars over the next five years, and, using the Korea-Africa Economic Cooperation Trust Fund set up at the African Development Bank as its resource, carry out projects worth 11 million dollars for sharing economic development experience and technical cooperation."),
    ("정부가 이번에 대규모 경협방안을 내놓은 데는 최근 세계시장에서 신흥 투자처로 급부상하고 있는 아프리카 국가들과의 스킨십을 강화하기 위한 목적이 깔려 있다.", "Behind the government’s putting out this large-scale economic cooperation plan lies the aim of strengthening ties with African countries, which have recently emerged rapidly as a new investment destination in the world market."),
    ("최근 아프리카 국가들은 내정이 안정되면서 연간 오에서 육 퍼센트대의 고성장대에 진입한데다 전 세계 인구의 십사 퍼센트에 달하는 십억 명이 살고 있어 신흥 교역시장으로서의 매력도 적지 않다.", "Recently African countries have entered a high-growth range of 5 to 6 percent a year as their domestic politics stabilized, and a billion people, 14 percent of the world’s population, live there, so its charm as an emerging trading market is not small."),
    ("특히 아프리카의 교역비중이 현재는 전 세계의 이 점 사 퍼센트에 그치고 있지만, 중국과 인도 등을 중심으로 자원수요가 지속적으로 증가할 것으로 예상되면서 자원개발을 중심으로 외국자본의 투자유입이 탄력을 받을 것이라는 분석이 나오고 있다.", "In particular, although Africa’s share of trade is at present only 2.4 percent of the world, an analysis is emerging that, as demand for resources is expected to keep rising, centered on China and India, the inflow of foreign capital investment, centered on resource development, will gain momentum."),
    ("기획재정부 주형환 대외경제국장은 아프리카의 경우 아직은 유럽의 영향력이 크기 때문에 당장 우리가 주요 플레이어가 될 수는 없지만 우리 경제발전 경험에 대한 관심이 높고 우리가 다른 나라를 식민지배한 경험이 없다는 점에서 매우 우호적이다라면서 교역의존도가 높은 우리로서는 향후 아프리카도 투자 다변화의 지평이 될 것으로 본다고 말했다.", "Ju Hyeong-hwan, director of the External Economic Affairs Bureau of the Ministry of Strategy and Finance, said that in Africa Europe’s influence is still large, so we cannot immediately become a major player, but there is great interest in our economic development experience and it is very friendly in that we have no experience of colonizing other countries, and that for us, who depend highly on trade, Africa too will become a horizon for diversifying investment in the future."),
]
_FAIR6 = [
    ("지구촌을 살리는 착한 소비, 공정무역", "Good consumption that saves the global village: fair trade"),
    ("부자는 더욱 부자로, 가난한 자는 더욱 가난하게 만드는 지금의 무역 구조를 바로잡기 위한 노력, 공정무역에 대해 에코생협 최재숙 이사에게 들었다.", "We heard from Choi Jae-sook, a director of Eco Co-op, about fair trade, the effort to put right today’s trade structure that makes the rich richer and the poor poorer."),
    ("선진국의 소비자들이 가난한 나라의 생산자들이 만든 물건을 공정한 가격에 거래함으로써, 원조가 아닌 경제활동을 통해 빈곤 문제를 해결하고자 하는 글로벌 시민운동이죠.", "It is a global civic movement in which consumers in developed countries trade at fair prices the goods made by producers in poor countries, hoping to solve the poverty problem through economic activity rather than aid."),
    ("이제껏 우리가 별생각 없이 소비해 온 물건들의 가격구조를 살펴 보면 다소 충격적인 진실을 알 수 있다.", "If we look at the price structure of the goods we have consumed until now without much thought, we can find a somewhat shocking truth."),
    ("사십 달러 하는 청바지 한 벌을 만들 때 노동자에게 돌아가는 임금은 영 점 이칠 달러에 불과하다.", "When a pair of jeans priced at 40 dollars is made, the wage that goes to the worker is only 0.27 dollars."),
    ("정작 소비자는 비싼 값을 주고 청바지를 구입하지만 생산자는 터무니없이 적은 노동의 대가를 받고 있는 셈이다.", "In effect, the consumer pays a high price and buys the jeans, but the producer receives an absurdly small reward for the labor."),
    ("이렇듯 지금의 무역구조는 선진국은 더 많은 이윤을 가져가 부자가 되고 제삼 세계 생산자들은 더욱더 가난해지는 구조다.", "Like this, today’s trade structure is one in which developed countries take more profit and become rich while Third World producers become ever poorer."),
    ("제삼 세계의 농부들이 생존 자체가 어려울 만큼의 임금을 받고 생산하는 물건들을 소비자가 비싼 가격에 소비하고 있는 현실은 한 번쯤 생각해 봐야 할 문제다.", "The reality that consumers consume at high prices the goods that Third World farmers produce for wages so low that survival itself is hard is a problem worth thinking about at least once."),
]
_SPEAK6B = [("보통 물건을 구입할 때 우선적으로 고려하는 것은 무엇인지 이야기해 보세요.", "Talk about what you usually consider first when buying something."), ("공정무역을 통해 수입한 원자재로 만든 아래 제품 중에 하나를 선택해서 반 친구들이 소비자라고 생각하고 제품을 선전하세요.", "Choose one of the following products made with raw materials imported through fair trade, and advertise it, thinking of your classmates as consumers."), ("제품의 품질에 대한 설명과 함께 공정무역 제품의 정의와 필요성도 설명해 주세요.", "Along with an explanation of the product’s quality, also explain the definition and necessity of fair trade products."), ("티셔츠, 운동화, 초콜릿, 축구공, 장미꽃, 커피.", "T-shirt, sneakers, chocolate, soccer ball, roses, coffee.")]
L4 = lesson(
    "U18 L6 · Part 2 (본 학습): Korea’s Africa policy and fair trade",
    "본 학습 · 아프리카 경제외교 · 원조 · 신흥 시장 · 교역 · 공정무역 · 착한 소비 · 이윤 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a newspaper article on Korea’s policy toward Africa (Kyunghyang)", "The book asks three questions in English: the government’s new policy on Africa and its underlying purpose; why foreign investors are attracted to African countries; and why African countries favor economic ties with Korea. The figures are spelled in Hangul and the abbreviation EDCF and the quotation marks are dropped; the official is named by his public post, as in the article. The article, with my English:", examples=passage(_AFR6)),
        card("My answers to 학습활동 2", "1. The government will double aid to Africa and greatly expand projects that share Korea’s economic development experience (more fund support and a trust fund for technical cooperation); the purpose is to strengthen ties with African countries that are becoming a new investment destination. 2. Their domestic politics have stabilized and they are in a high-growth range of 5 to 6 percent; they hold 14 percent of the world’s population (a billion people), so they are an attractive emerging trading market; and resource demand from China and India is expected to rise, drawing foreign investment into resource development. 3. Africa takes a keen interest in Korea’s economic development experience, and Korea has no experience of colonizing other countries, so it is seen as very friendly."),
        card("학습활동 3: an article on fair trade (Kyunghyang)", "The book asks in English what problem the article mentions and what 공정무역 is. The article names the interviewed co-op director (she gives her views in the published interview), which I kept. The figures are spelled in Hangul and 제3세계 is written 제삼 세계. The article, with my English:", examples=passage(_FAIR6)),
        card("My answers to 학습활동 3", "A. The problem: today’s trade structure makes the rich richer and the poor poorer; for example, of a pair of jeans priced at 40 dollars only 0.27 dollars goes to the worker, while producers in the Third World earn too little to survive and developed countries take most of the profit. B. 공정무역 (fair trade): consumers in developed countries trade at fair prices the goods made by producers in poor countries, aiming to solve poverty through economic activity rather than aid."),
        card("말해 봅시다! (speaking)", "The book’s two prompts, which I split into four sentences; the six products are listed as one line (the English is mine):", examples=passage(_SPEAK6B)),
        card("Activities left out", "학습활동 1 (Listening, track 005 and 006): a YTN news item on resource development in the Arctic: you explain in English the resources of the Svalbard islands, explain the treaty of 1920 in Korean, and transcribe and translate the last sentence (which begins 하지만) with its implication. 학습활동 3, part 2 (Listening, track 007): a YTN news item on the coffee industry: the problems coffee farmers face and why the coffee sold by the civic organization is called 착한 커피 (“good coffee”). They are audio."),
    ],
    exercises=uniq(
        _tr(_AFR6, k=3) + _tr(_FAIR6, k=3) + _tr(_SPEAK6B, k=3)
        + [M("By how much will the government increase aid to Africa?", "Double it", ["Triple it", "Cut it by half", "Keep it the same"], "두 배."), M("What share of the world’s population lives in Africa, according to the article?", "14 percent", ["2.4 percent", "95 percent", "5 percent"], "십사 퍼센트."), M("What share of world trade does Africa account for now?", "2.4 percent", ["14 percent", "24 percent", "6 percent"], "이 점 사 퍼센트."), M("Why is Korea seen as friendly in Africa?", "It has no experience of colonizing other countries", ["It gives the most aid", "It buys the most oil", "It speaks French"], "식민지배한 경험이 없다."), M("How much of a 40-dollar pair of jeans goes to the worker?", "0.27 dollars", ["4 dollars", "27 dollars", "0.027 dollars"], "영 점 이칠 달러."), M("What is fair trade, in the article’s words?", "Trading at fair prices with producers in poor countries to solve poverty", ["Sending aid money to poor countries", "Banning imports from poor countries", "Taxing luxury goods"], "공정무역.")]
        + [F("정부가 아프리카 원조를 두 배로 늘리고 ___사업을 확대하기로 했다. (sharing)", "공유", ["유입", "독점"], "공유."), F("신흥 ___시장으로서의 매력이 적지 않다. (trading)", "교역", ["광물", "금융"], "교역."), F("선진국은 더 많은 ___을 가져간다. (profit)", "이윤", ["윤리", "탄력"], "이윤."), F("청바지 생산자는 ___없이 적은 대가를 받고 있다. (absurdly)", "터무니", ["부당", "매력"], "터무니없이."), F("한국은 아프리카 시장에 대한 ___를 시작했다. (courtship)", "구애", ["식민", "내정"], "구애.")]
        + [read_q("정부가 아프리카 원조를 두 배로 늘리기로 했다"), read_q("아프리카는 신흥 교역시장으로서의 매력이 적지 않다"), read_q("공정무역은 글로벌 시민운동이다"), read_q("제품의 품질에 대한 설명과 함께 공정무역 제품의 필요성도 설명해 주세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("냉전", "(冷戰) the Cold War; a cold war", "구십 년대에 냉전시대가 막을 내렸습니다."),
        ("보고", "(寶庫) a repository (of treasure)", "바다는 천연자원의 보고입니다."),
        ("부추기다", "to incite; to instigate", "거리의 담배광고가 청소년의 흡연을 부추기고 있습니다."),
        ("인접(하다)", "(隣接) adjoining (to adjoin; to lie close; to border on)", "이번 폭우로 섬진강에 인접한 지역에 홍수피해가 심합니다.", "가깝다"),
        ("쟁탈(하다)", "(爭奪) a struggle; a scramble (to struggle for)", "라이벌 관계에 있는 두 회사가 시장을 선점하기 위해 쟁탈전을 벌이고 있습니다.", "쟁탈전"),
        ("치솟다", "to soar; to skyrocket", "장마철을 맞아 야채 값이 치솟고 있습니다.", "뜨다, 오르다, 폭등하다"),
        ("치열하다", "(熾烈) to be fierce; to be intense", "이번 승진심사에 사원들 간의 경쟁이 치열합니다.", "거세다"),
    ]),
    ("학습활동 2", [
        ("공유(하다/되다)", "(共有) sharing (to share/to be shared)", "한국정부와 미국정부는 중요한 안보관련 정보를 공유하고 있습니다."),
        ("교역(하다/되다)", "(交易) trade; commerce (to trade/to be traded)", "새 정부 들어 남북 교역이 눈에 띄게 줄었습니다.", "무역"),
        ("구애(하다)", "(求愛) courtship (to try to win someone’s love)", "그 여자는 그의 계속된 구애에 결혼을 결심했다."),
        ("내정", "(內政) internal affairs", "타국의 내정에 간섭하지 맙시다."),
        ("매력", "(魅力) charm; attraction; magnetism", "저는 그의 매력 있는 웃음이 참 좋아요."),
        ("부상(하다)", "(浮上) surging; floating (to float)", "국제영화제를 개최한 후에 전주가 새로운 문화도시로 부상하고 있습니다."),
        ("식민", "(植民) colonization", "우리나라는 일본의 식민 통치를 받았습니다.", "식민지, 식민지배"),
        ("신흥", "(新興) new; emerging", "구세력과 신흥세력간에 갈등이 깊다.", "새"),
        ("우호", "(友好) friendship", "한미 양국간에는 우호적인 관계가 유지되고 있다.", "우호적"),
        ("유입(하다/되다)", "(流入) inflow; influx (to pour in; to flow in)", "외국 투자자본이 한국으로 많이 유입되고 있다."),
        ("탄력", "(彈力) elasticity; flexibility", "이 옷감은 탄력이 좋아서 입으면 아주 편합니다."),
        ("향후", "(向後) henceforth; from now on", "회사는 향후 삼 년간 채용을 하지 않기로 결정했습니다.", "앞으로"),
    ]),
    ("학습활동 3", [
        ("동원(하다/되다)", "(動員) mobilization (to mobilize/to be mobilized)", "음주단속에 많은 경찰관이 동원되었다."),
        ("면화", "(綿花) (raw) cotton", "최근 면화가격이 상승하고 있습니다."),
        ("시세", "(時勢) market price", "이 아파트 시세가 얼마나 합니까?", "가격"),
        ("원두", "(原豆) coffee beans", "저는 원두커피를 좋아합니다."),
        ("윤리", "(倫理) ethics; morality", "이번 일에 윤리적인 판단을 하는 것은 옳지 않다고 생각합니다.", "도덕"),
        ("이윤", "(利潤) profit; gain", "기업의 목표는 이윤을 남기는 것입니다.", "이익"),
        ("절대적으로", "(絶對的) absolutely; completely", "이 행사에 필요한 자원봉사자가 절대적으로 부족합니다.", "상대적"),
        ("종사하다", "(從事) to engage (in business); to pursue (a calling); to follow (a profession); to practice (medicine)", "정보통신산업에 종사하는 인력이 증가하고 있다."),
        ("주도(하다/되다)", "(主導) taking the lead (in) (to take the lead/to be led)", "이 프로젝트는 정부가 주도하는 대표적인 사업이다.", "앞장서다"),
        ("진실", "(眞實) a truth; a fact", "진실은 언젠가는 밝혀지게 되어 있어요.", "사실 / 거짓"),
        ("터무니없다", "to be preposterous; to be absurd; to be unfounded; to be unreasonable", "그런 터무니없는 소문은 믿지 마세요."),
    ]),
]
L5 = lesson(
    "U18 L6 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 냉전 · 보고 · 부추기다 · 인접 · 쟁탈 · 치솟다 · 치열하다 · 공유 · 교역 · 구애 · 내정 · 매력 · 부상 · 식민 · 신흥 · 우호 · 유입 · 탄력 · 향후 · 동원 · 면화 · 시세 · 원두 · 윤리 · 이윤 · 절대적으로 · 종사하다 · 주도 · 진실 · 터무니없다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives homonyms: 보고 (報告), “a report”; 부상 (負傷), “injury”, beside 부상 (浮上). 신흥 lists the prefix 새~ as related (I wrote 새). 진실 lists 사실 as similar and 거짓 as the opposite (joined with a slash). The examples had digits in the book (90년대, 3년간), which I spelled out (구십 년대, 삼 년간). 교역 appeared in Lesson 4 with a different set of related words.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=22, nread=18)),
)

# ================================================================== L6 Part 3
_KOR6 = [
    ("유가, 곡물가 등 원자재 가격이 최근 들어 급속히 상승하고 있다.", "Raw material prices such as oil and grain prices have recently been rising rapidly."),
    ("중국과 인도 등 신흥개발 도상국가의 적극적인 내수 소비 탓에 해외 원자재 가격이 하루가 다르게 오르는 것이다.", "Overseas raw material prices are rising day by day because of the active domestic consumption of emerging developing countries such as China and India."),
    ("특히 이 같은 원자재 가격 상승은 수입물가 상승, 기업의 부담 증가, 물가 상승, 서민 생활 불안이라는 악순환으로 이어지고 있다.", "In particular, such a rise in raw material prices is leading to a vicious circle of a rise in import prices, a growing burden on companies, a rise in prices and unrest in ordinary people’s lives."),
    ("이에 따라 전 세계는 자원을 확보하기 위해 총성 없는 전쟁을 벌이고 있다.", "Accordingly, the whole world is waging a “war without gunshots” to secure resources."),
    ("이와 같은 세계의 자원 대란 속에서 우리 정부도 최근 해외자원 개발 사업에 매진하고 있다.", "Amid such a world resource crisis, our government too has recently been devoting itself to overseas resource development projects."),
    ("한국은 선진 국가 그룹 중에서 자원이 가장 빈약한 나라다.", "Korea is the country with the poorest resources in the group of advanced countries."),
    ("한국의 광산물 자급도는 지난해 기준으로 십 퍼센트 정도에 머문다.", "Korea’s self-sufficiency in mineral products stays at about 10 percent by last year’s standard."),
    ("특히 금속광물의 자급도는 일 퍼센트에 지나지 않는다.", "In particular, the self-sufficiency in metallic minerals is no more than 1 percent."),
    ("한국은 이에 따라 매년 총수입액의 오 퍼센트에 해당하는 광물원료를 해외에서 수입해 오고 있다.", "Accordingly, Korea has been importing from abroad every year mineral raw materials equal to 5 percent of its total imports."),
    ("그러면 북한은 어떤가.", "Then what about North Korea?"),
    ("남한과 정반대로 세계적인 자원 잠재 부국이다.", "In complete contrast to South Korea, it is a world-class potentially resource-rich country."),
    ("북한은 국토의 팔십 퍼센트에 걸쳐 이백여 종의 유용한 광물자원이 분포되어 있으며, 대한광업진흥공사의 추정에 따르면 북한의 광물자원 가치는 삼천칠백십구조 원으로 남한의 십팔 배에 달한다.", "In North Korea more than 200 kinds of useful mineral resources are distributed over 80 percent of its land, and according to an estimate by the Korea Resources Corporation, the value of North Korea’s mineral resources is 3,719 trillion won, 18 times that of South Korea."),
    ("특히 북한의 마그네사이트와 우라늄은 세계 최고 수준의 매장량을 자랑한다.", "In particular, North Korea’s magnesite and uranium boast world-class reserves."),
    ("하지만 남북한의 지하자원 공동개발은 전무한 실정이다.", "But joint development of underground resources by the two Koreas is non-existent."),
    ("이 같은 틈을 타 중국 등 제삼 국은 북한의 지하자원에 눈독을 들이고 있다.", "Taking advantage of this gap, third countries such as China are coveting North Korea’s underground resources."),
    ("특히 북한은 중국에 우호 가격으로 지하자원을 판매해 국제 시세의 삼분의 일에도 못 미치는 것으로 알려졌다.", "In particular, North Korea is known to sell underground resources to China at a “friendship price” that is less than a third of the international market price."),
    ("남북경협의 이상적인 모델이 남한이 북한 지하자원 개발에 참여하는 것이지만, 아직까지 좋은 기회를 살리지 못하고 있다.", "The ideal model of inter-Korean economic cooperation is for South Korea to take part in developing North Korea’s underground resources, but it has not yet made use of the good opportunity."),
    ("남북이 비교우위가 있는 경공업 제품과 지하자원을 서로 교환하면 양측에 모두 이익이다.", "If the two Koreas exchange light industrial products and underground resources, in which each has a comparative advantage, both sides benefit."),
    ("남한은 외국이 북한 지하자원을 점유하기 전에 하루 빨리 북한의 지하자원 개발에 참여하는 것이 실용이 아닐까.", "Wouldn’t it be practical for South Korea to take part in developing North Korea’s underground resources as soon as possible, before foreign countries occupy them?"),
]
_OPT6 = [
    ("평화협상에도 불구하고 중동지역은 여전히 분쟁이 발생할 가능성이 아주 높다.", "A. Despite peace negotiations, the Middle East still has a very high possibility of conflict."),
    ("아프리카 지역에서 중국은 원유를 비롯한 주요 자원의 개발에 적극 나서고 있다.", "B. In Africa, China is actively taking part in the development of major resources, beginning with crude oil."),
    ("북한과 남한은 휴전 후 오십 년 동안 휴전선을 사이에 두고 크고 작은 군사적 충돌을 해 왔다.", "C. For fifty years after the armistice, North and South Korea have had military clashes, large and small, across the armistice line."),
    ("남미 자동차 시장에서 우위를 점하기 위해 일본과 한국은 치열하게 경쟁하고 있다.", "D. To take the upper hand in the South American car market, Japan and Korea are competing fiercely."),
]
_SPEAK6C = [("유에스에이아이디는 저개발 국가에 대한 지원을 담당하는 미국정부기관입니다.", "USAID is the US government agency in charge of aid to underdeveloped countries."), ("여러분이 유에스에이아이디의 활동에 참여한다고 가정하세요.", "Suppose you take part in USAID’s activities."), ("먼저 저개발 국가 하나를 선정한 후 어떤 도움이 필요하고 어떻게 도울 수 있는지 그리고 그 국가를 도와야 하는 이유는 무엇인지 반 친구들에게 말해 보세요.", "First choose one underdeveloped country, then tell your classmates what help it needs, how it can be helped and why that country should be helped.")]
L6 = lesson(
    "U18 L6 · Part 3 (심화 학습): raw materials and the resources of the two Koreas",
    "심화 학습 · 원자재 가격 · 자원 대란 · 총성 없는 전쟁 · 광물자원 · 자급도 · 남북 경협 · 비교우위 · 악순환 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a newspaper article on the underground resources of North and South Korea (Kyunghyang)", "The book asks five questions: the main idea (four choices); a comparison of the resources of South and North Korea; a word that could replace the underlined 하루가 다르게 (choices 갑자기, 꾸준히, 정확하게, 틀리게); the effect of rising raw material prices on the economy; and which of four sentences best illustrates the underlined 총성 없는 전쟁. The underlines are not marked in the text, but the phrases named in the questions are clear. The figures are spelled in Hangul; I wrote “중국·인도” as 중국과 인도 and the book’s arrows (→) as commas, and 제3국 as 제삼 국. The article, with my English:", examples=passage(_KOR6)),
        card("The four sentences for question 5", "The book’s four sentences, with my English:", examples=passage(_OPT6)),
        card("My answers to 학습활동 2", "1. A: South Korea has to take an active part in developing North Korea’s resources (the article’s last sentence argues it). 2. South Korea: resources are the poorest among advanced countries; self-sufficiency in mineral products about 10 percent and in metallic minerals 1 percent; it imports mineral raw materials worth 5 percent of its total imports each year. North Korea: a potentially resource-rich country; more than 200 kinds of useful minerals over 80 percent of its land, worth 3,719 trillion won (18 times the South’s), with world-class reserves of magnesite and uranium. 3. My choice is B 꾸준히 (steadily; day by day without stopping), although 하루가 다르게 means “changing every day”, and the book does not give the answer, so this is a guess. 4. Higher raw material prices raise import prices, which burdens companies, which pushes up prices and so makes ordinary people’s lives unstable: a vicious circle. 5. My choice is B (the competition to secure resources is the “war without gunshots”), also my reading."),
        card("말해 봅시다! (speaking)", "The book’s prompt, which I split into three sentences; the book writes “USAID (the United States Agency for International Development)”, which I wrote 유에스에이아이디 (the English is mine):", examples=passage(_SPEAK6C)),
        card("Activities left out", "학습활동 1 (Listening, Writing, track 008): a YTN documentary on international economic problems: you fill a table on the “brain drain” (두뇌유출 현상: meaning, reason, consequences), describe the countermeasures of African countries and draft in Korean an announcement for a campaign against the brain drain in Korea. 학습활동 3 (Listening, track 009): an interview with a representative of a Korean government agency: the tasks of the Korea International Cooperation Agency (한국국제협력단) and the main reasons Korea should help underdeveloped countries. They are video and audio."),
    ],
    exercises=uniq(
        _tr(_KOR6, k=3) + _tr(_OPT6, k=3) + _tr(_SPEAK6C, k=2)
        + [M("What share of South Korea’s mineral products is self-supplied?", "About 10 percent", ["About 1 percent", "About 80 percent", "About 50 percent"], "십 퍼센트."), M("How does the value of North Korea’s mineral resources compare with South Korea’s?", "18 times", ["3 times", "Half", "The same"], "십팔 배."), M("Which two minerals does North Korea boast world-class reserves of?", "Magnesite and uranium", ["Copper and tin", "Silver and zinc", "Gold and iron"], "마그네사이트와 우라늄."), M("At what price does North Korea sell resources to China?", "Less than a third of the international market price", ["Twice the market price", "The market price", "Half the market price"], "삼분의 일에도 못 미침."), M("What does 총성 없는 전쟁 refer to in the article?", "The fierce competition to secure resources", ["A peace treaty", "A civil war", "A trade embargo"], "자원 확보."), M("What is the vicious circle described?", "Higher import prices, burdens on firms, higher prices and unrest in ordinary lives", ["Lower wages, lower spending and higher savings", "Higher exports, a stronger currency and fewer jobs", "More mines, more waste and more floods"], "악순환.")]
        + [F("한국은 광물자원이 ___한 나라다. (poor; scanty)", "빈약", ["풍부", "막대"], "빈약하다."), F("남북한의 지하자원 공동개발은 ___한 실정이다. (non-existent)", "전무", ["봉착", "미비"], "전무하다."), F("중국 등 제삼 국은 북한의 지하자원에 ___을 들이고 있다. (to covet)", "눈독", ["공백", "탄력"], "눈독을 들이다."), F("원자재 가격 상승이 서민 생활 불안이라는 ___환으로 이어지고 있다. (vicious)", "악순", ["선순", "순환"], "악순환.")]
        + [read_q("한국은 선진 국가 그룹 중에서 자원이 가장 빈약한 나라다"), read_q("북한은 세계적인 자원 잠재 부국이다"), read_q("남북한의 지하자원 공동개발은 전무한 실정이다"), read_q("전 세계는 자원을 확보하기 위해 총성 없는 전쟁을 벌이고 있다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("고국", "(故國) one’s homeland; one’s native country", "그 사람은 고국을 떠나 타국에서 오랫동안 생활했어요.", "모국, 타국"),
        ("고질(적)", "(痼疾的) chronic; incorrigible; long-standing", "이 문제는 우리 사회에서 오랜 시간 지속되어 온 고질적 문제입니다.", "만성, 고질병"),
        ("공백을 메우다", "(空白) to fill in the blank", "휴가 간 김 대리의 공백을 메우기 위해 제가 야근을 하고 있습니다."),
        ("막대하다", "(莫大) to be huge; to be enormous", "우리나라 사람들은 영어 교육에 막대한 돈을 쏟아 붓습니다.", "거대하다"),
        ("미비하다", "(未備) to be incomplete; to be inadequate", "이 도시는 숙박시설이 미비해 큰 행사를 치르지 못합니다."),
        ("병폐", "(病弊) a malady; an evil; a vice; evil practices", "이 문제는 우리 사회의 뿌리깊은 병폐입니다."),
        ("봉착(하다)", "(逢着) encountering (a difficult situation or problem) (to encounter)", "이번 총격사건으로 인해 금강산 관광이 새로운 문제에 봉착했습니다."),
        ("부실(하다)", "(不實) weakness; incompleteness; unreliability (to be weak; to be incomplete; to be unreliable)", "그 건물은 기초가 부실합니다.", "약하다, 부실 기업, 부실 공사"),
        ("이주(하다)", "(移住) move; migration (to move; to migrate)", "우리 가족은 도시로 이주하기로 결정했습니다.", "이사하다, 이민 가다"),
        ("인재", "(人材) a talented person; a person of ability", "정부는 인재를 육성하기 위한 프로젝트를 시행하겠다고 했습니다."),
    ]),
    ("학습활동 2", [
        ("광물", "(鑛物) mineral", "이 지역의 광물을 개발한다고 합니다."),
        ("내수", "(內需) domestic consumption", "이 제품은 내수용으로 제조한 것입니다."),
        ("눈독을 들이다", "(毒) to covet", "남의 물건에 눈독을 들이지 마세요.", "욕심 내다"),
        ("비교우위", "(比較優位) comparative advantage", "이 제품은 성능에 비해 가격이 저렴해 타사 제품에 비해 비교우위가 있습니다."),
        ("빈약(하다)", "(貧弱) poorness; scantiness; meagerness; “poor and weak” (to be poor; to be scanty; to be meager; to be limited)", "저는 지식이 빈약해서 잘 알지 못합니다.", "풍부하다"),
        ("서민", "(庶民) an ordinary person; “commoner”", "국회의원 후보들이 서민들을 위한 정치를 하겠다고 공약을 내걸었습니다."),
        ("악순환", "(惡循環) vicious circle", "질이 좋지 않은 제품을 생산하는 이 기업은 수익을 내지 못해 제품의 질을 향상시키지 못하는 악순환을 벗어나지 못하고 있습니다."),
        ("잠재(하다/되다)", "(潛在) latency (to be latent)", "우승을 하지 못했지만 저 선수는 잠재된 능력이 뛰어납니다.", "잠재력"),
        ("전무(하다)", "(全無) nonexistence (to be nonexistent; to be unprecedented)", "이번 일은 전무후무한 사건이다.", "없다"),
    ]),
    ("학습활동 3", [
        ("더불어", "together with; along with", "모든 사람이 더불어 함께 사는 사회를 만들고 싶습니다.", "같이, 함께"),
        ("미화", "(美貨) U.S. currency", "미화 만 불 이상 소지하신 분은 세관에 신고해 주시기 바랍니다.", "달러"),
        ("재난", "(災難) a disaster; a catastrophe", "여름에는 재난영화가 큰 인기입니다.", "재해, 화"),
        ("전수(하다)", "(傳授) transmission (of skills or knowledge) (to transmit; to pass down; to teach)", "제가 가진 전통 문화에 대한 지식을 학생들에게 전수하고 싶습니다."),
        ("초청(하다/되다)", "(招請) invitation (to invite/to be invited)", "내일 김 선생님의 초청 강연회에 가려고 합니다."),
        ("파견(하다/되다)", "(派遣) dispatch (to dispatch; to send/to be dispatched)", "엘에이 지사에 파견 근무 나갈 사람을 찾고 있습니다."),
    ]),
]
L7 = lesson(
    "U18 L6 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 고국 · 고질 · 공백을 메우다 · 막대하다 · 미비하다 · 병폐 · 봉착 · 부실 · 이주 · 인재 · 광물 · 눈독을 들이다 · 비교우위 · 빈약 · 서민 · 악순환 · 잠재 · 전무 · 더불어 · 미화 · 재난 · 전수 · 초청 · 파견",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives the homonym 미화 (美化), “glamorization; embellishment”, beside 미화 (美貨). 눈독을 들이다 carries the single Hanja 毒. 인재 appeared in Lesson 3 with a slightly different gloss. The examples had digits and Latin letters in the book (10,000불, LA지사), which I spelled out (만 불, 엘에이 지사). 내수 appeared before with “domestic demand or consumption”; here it is “domestic consumption”.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=20, nread=16)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 6: The World Economy (세계 경제)", [L1, L2, L3, L4, L5, L6, L7])
