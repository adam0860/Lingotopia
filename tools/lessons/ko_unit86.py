"""Unit 86: KBC Semester III, Unit 18, Lesson 1 - The Domestic Economy (국내 경제).
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
_MATCH1 = [("지출", "spending; expenditure", "식비를 지출하다"), ("물가", "price of commodities", "물가가 많이 오르다"), ("빚", "debt; loan", "빚을 내어 집을 사다"), ("관리비", "utility bills", "관리비가 많이 나오다"), ("저축", "savings; deposit in bank", "월급의 이십 퍼센트를 저축하다"), ("수요", "demand", "수요가 증가하다"), ("급증", "rapid increase", "수출이 급증하다"), ("신용", "credit", "신용 등급이 올라가다")]
_OPP1 = [("아끼다", "낭비하다", "to save: to waste"), ("줄이다", "늘리다", "to reduce: to increase"), ("과소비하다", "절약하다", "to overspend: to economize"), ("판매하다", "구매하다", "to sell: to buy"), ("급증하다", "급감하다", "to increase rapidly: to decrease rapidly"), ("단기", "장기", "short term: long term"), ("출금", "입금", "withdrawal: deposit"), ("불황", "호황", "a slump: a boom")]
_HJ1 = [("急 급", "rapid; urgent", "긴급, 급증"), ("費 비", "expense; fee", "소비, 식비"), ("産 산", "produce", "산업, 농산물"), ("品 품", "thing; article; stuff", "가전제품, 품질"), ("計 계", "calculate; figure", "가계, 계산")]
_HJW1 = [("긴급", "emergency"), ("급증", "rapid increase"), ("소비", "consumption"), ("식비", "food expenses"), ("산업", "industry"), ("농산물", "agricultural products"), ("가전제품", "appliances"), ("품질", "quality"), ("가계", "household budget"), ("계산", "calculation")]
_SIM1 = [("낭비", "과소비", "waste: overspending"), ("집계", "통계", "a total count: statistics"), ("급감", "급락", "a rapid decrease: a sharp fall"), ("금품", "귀중품", "money and goods: valuables (my best guess)"), ("자산", "재산", "assets: property")]
_CAT1 = [("관리비, 식비, 의복 구입비", "생활비", "utilities, food, clothing: living expenses"), ("연필, 공책, 지우개", "학용품", "pencil, notebook, eraser: school supplies"), ("냉장고, 세탁기, 청소기", "가전제품", "refrigerator, washer, cleaner: appliances"), ("쌀, 콩, 사과", "농산물", "rice, beans, apples: agricultural products")]
_L1X = [("지출하다", "to spend"), ("저축하다", "to save money"), ("입금", "a deposit"), ("출금", "a withdrawal"), ("구매하다", "to buy"), ("판매하다", "to sell"), ("낭비하다", "to waste"), ("절약하다", "to economize"), ("호황", "a boom"), ("불황", "a slump"), ("단기", "short term"), ("장기", "long term"), ("비용", "a cost"), ("숙박비", "lodging expenses"), ("계산대", "a cashier counter"), ("통계", "statistics"), ("집계", "a total count"), ("계획", "a plan"), ("급감", "a rapid decrease"), ("급락", "a sharp fall"), ("응급", "an emergency"), ("급속", "rapidity"), ("금품", "money and goods"), ("명품", "a famous-brand product"), ("신상품", "a new product"), ("귀중품", "a valuable"), ("가공품", "a processed product"), ("자산", "assets"), ("부동산", "real estate"), ("생산", "production"), ("재산", "property"), ("생활비", "living expenses"), ("학용품", "school supplies"), ("의복 구입비", "clothing purchase costs"), ("냉장고", "a refrigerator"), ("세탁기", "a washing machine"), ("청소기", "a vacuum cleaner")]
L1 = lesson(
    "U18 L1 · Review: money words and Sino-Korean 急 費 産 品 計",
    "국내 경제 · 단어 복습 · 한자어 복습 · 지출 · 물가 · 빚 · 관리비 · 저축 · 수요 · 급증 · 신용 · 急 費 産 品 計",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives eight phrases with one word underlined and asks you to connect each with its English meaning on the right. The underline is not marked in the text; the pairs below are my best reading. The book writes 20% in digits; I wrote it out:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH1], say=[0, 2])]),
        card("단어 복습 2: the opposite word (my matching)", "Connect each word on the left with the word of the opposite meaning on the right (the right-hand words are 구매하다, 급감하다, 입금, 장기, 낭비하다, 절약하다, 호황, 늘리다; the lines are not drawn in the text, so this matching is mine):", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP1], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ1], say=[2]), ktable(_HJW1)]),
        card("한자어 복습 1: the most similar word (my answers)", "Circle the word closest in meaning to the word on the left (A. 낭비: 비용, 소비, 과소비, 숙박비; B. 집계: 계산대, 통계, 가계, 계획; C. 급감: 급락, 급증, 응급, 급속; D. 금품: 명품, 신상품, 귀중품, 가공품; E. 자산: 부동산, 산업, 생산, 재산). The answer to D is a guess, since 금품 can also mean “money and valuables”.", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM1], say=[0, 1])]),
        card("한자어 복습 2: the word that includes all three (my answers)", "Choose from the box (생활비, 농산물, 품질, 학용품, 낭비, 가전제품) the word that includes the three words of each line:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _CAT1], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L1X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH1], k=3) + _tr(_HJW1, k=3) + _tr(_L1X, k=4) + _tr([(a, b) for a, b, c in _OPP1[:4]], k=3)
        + [M("What does the syllable 急 (급) mean?", "rapid; urgent", ["expense", "produce", "calculate"], "급증."), M("What does the syllable 費 (비) mean?", "expense; fee", ["rapid", "produce", "thing"], "소비."), M("What does the syllable 産 (산) mean?", "produce", ["rapid", "expense", "calculate"], "산업."), M("What does the syllable 品 (품) mean?", "thing; article; stuff", ["rapid", "expense", "calculate"], "품질."), M("What does the syllable 計 (계) mean?", "calculate; figure", ["rapid", "produce", "thing"], "가계.")
           , M("Which word is the opposite of 출금?", "입금", ["장기", "호황", "구매하다"], "Deposit."), M("Which word is the opposite of 불황?", "호황", ["입금", "장기", "늘리다"], "Boom."), M("Which word is the opposite of 단기?", "장기", ["입금", "호황", "절약하다"], "Long term."), M("Which word covers 쌀, 콩, 사과?", "농산물", ["학용품", "가전제품", "생활비"], "Agricultural products."), M("Which word covers 연필, 공책, 지우개?", "학용품", ["농산물", "가전제품", "생활비"], "School supplies."), M("Which word covers 관리비, 식비, 의복 구입비?", "생활비", ["농산물", "학용품", "가전제품"], "Living expenses."), M("Which word is similar to 급감?", "급락", ["급증", "응급", "급속"], "A sharp fall.")
           , F("식비를 ___하다. (to spend)", "지출", ["저축", "수요"], "지출하다."), F("___가 많이 오르다. (prices)", "물가", ["수요", "관리비"], "물가."), F("월급의 이십 퍼센트를 ___하다. (to save)", "저축", ["지출", "급증"], "저축하다."), F("___가 증가하다. (demand)", "수요", ["물가", "신용"], "수요."), F("___ 등급이 올라가다. (credit)", "신용", ["수요", "지출"], "신용 등급.")]
        + [read_q("식비를 지출하다"), read_q("월급의 이십 퍼센트를 저축하다"), read_q("신용 등급이 올라가다"), read_q("수출이 급증하다")]
    ),
)

# ================================================================== L2 Part 1
_JAP1 = [
    ("대 일본 무역적자 더 늘었다", "The trade deficit with Japan has grown further"),
    ("우리나라의 대 일본 무역적자 규모가 더 커지고 있다.", "Korea’s trade deficit with Japan is growing larger."),
    ("일 일 지식경제부가 발표한 칠 월 수출입동향 잠정치에 따르면 올 일 월부터 칠 월까지 이십 일 기준 우리나라의 대 일본 수출은 백사십이억 구천칠백만 달러, 수입은 삼백사십오억 육백만 달러로 이백이억 구백만 달러의 무역적자를 기록했다.", "According to the provisional “July import and export trends” announced on the 1st by the Ministry of Knowledge Economy, Korea’s exports to Japan from January to July of this year (as of the 20th) were 14.297 billion dollars and imports were 34.506 billion dollars, recording a trade deficit of 20.209 billion dollars."),
    ("지난해 같은 기간과 비교해 수출은 삼십이 점 일 퍼센트, 수입은 삼십팔 점 삼 퍼센트 각각 늘어난 규모다.", "Compared with the same period last year, exports grew by 32.1 percent and imports by 38.3 percent respectively."),
    ("우리나라가 강세를 보이고 있는 반도체, 기계산업의 경우 일본 부품, 소재에 대한 의존도가 여전하기 때문이다.", "This is because, in the semiconductor and machinery industries, in which Korea is strong, the dependence on Japanese parts and materials remains."),
    ("이와 달리 우리나라의 대 중국 무역흑자 규모는 갈수록 늘어나는 추세다.", "In contrast, Korea’s trade surplus with China is on a trend of growing as time goes by."),
    ("올 일 월부터 칠 월까지 이십 일 기준 우리나라의 대 중국 수출은 육백십칠억 천만 달러, 수입은 삼백칠십칠억 천백만 달러로 무역흑자 규모가 이백삼십구억 구천구백만 달러에 이른다.", "From January to July of this year (as of the 20th), Korea’s exports to China were 61.71 billion dollars and imports were 37.711 billion dollars, so the trade surplus reaches 23.999 billion dollars."),
    ("우리나라의 대 중국 수출은 무선통신기기 마이너스 삼십육 점 칠 퍼센트를 제외한 반도체 백십칠 점 육 퍼센트, 석유제품 육십일 점 일 퍼센트, 액정 디바이스 사십 점 이 퍼센트 등 대부분 품목이 증가했다.", "In Korea’s exports to China, most items increased, such as semiconductors (117.6 percent), petroleum products (61.1 percent) and liquid crystal devices (40.2 percent), except wireless communication devices (minus 36.7 percent)."),
]
_SPEAK1 = [("자신의 지난 달 지출에 대해 이야기해 보세요.", "Talk about your spending last month."), ("돈을 어디에 얼마나 썼는지 친구와 이야기해 보세요.", "Tell a friend where and how much money you spent."), ("미국의 최근 경제 뉴스를 발표하고 서로 이야기해 보세요.", "Present the latest economic news of the United States and talk with each other about it.")]
L2 = lesson(
    "U18 L1 · Part 1 (도입 학습): the trade deficit with Japan and surplus with China",
    "도입 학습 · 무역적자 · 무역흑자 · 수출 · 수입 · 반도체 · 의존도 · 대 일본 · 대 중국 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 4: an article on Korea’s trade (Naeil)", "The book asks you to fill in an English table (trade with Japan and with China: surplus or deficit, exports and imports in dollars, items that contributed). The book writes the figures in digits and 對 in Hanja, which I wrote in Hangul. The article, with my English:", examples=passage(_JAP1)),
        card("My answers to 학습활동 4", "Trade with Japan: deficit; exports 14.297 billion dollars, imports 34.506 billion dollars, deficit 20.209 billion dollars; the deficit grew because the semiconductor and machinery industries still depend on Japanese parts and materials. Trade with China: surplus; exports 61.71 billion dollars, imports 37.711 billion dollars, surplus 23.999 billion dollars; semiconductors, petroleum products and liquid crystal devices (and most other items) increased, while wireless communication devices fell."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK1)),
        card("Activities left out", "학습활동 1: a graph of one of Korea’s economic indicators, which you identify with a classmate (a chart). 학습활동 2 (Listening, track 001): a conversation between two housewives about recent price increases: you fill an English table (the vegetables mentioned, the price increase, other costs that will increase). 학습활동 3 (Listening and video, tracks 002 and 003): a YTN news item on vegetable prices: you fill a table with the percent of the price change and the reason for it for cabbage, garlic, and radishes and cucumbers. It is audio and video."),
    ],
    exercises=uniq(
        _tr(_JAP1[1:], k=3)
        + [M("Which ministry announced the “July import and export trends”?", "The Ministry of Knowledge Economy", ["The Ministry of Defense", "The Ministry of Education", "The Ministry of Health"], "지식경제부."), M("What does Korea have with Japan, according to the article?", "A trade deficit", ["A trade surplus", "No trade", "A free trade treaty"], "무역적자."), M("Why does the deficit with Japan keep growing?", "Korean industries still depend on Japanese parts and materials", ["Korea exports nothing to Japan", "Korea has no semiconductors", "Japan stopped buying"], "의존도가 여전."), M("What does Korea have with China?", "A growing trade surplus", ["A trade deficit", "No trade", "A fixed trade"], "무역흑자."), M("Which item fell in Korea’s exports to China?", "Wireless communication devices", ["Semiconductors", "Petroleum products", "Liquid crystal devices"], "마이너스."), M("By what percent did exports to Japan grow compared with last year?", "32.1 percent", ["38.3 percent", "117.6 percent", "61.1 percent"], "삼십이 점 일 퍼센트.")]
        + [F("우리나라의 대 일본 무역___ 규모가 더 커지고 있다. (deficit)", "적자", ["흑자", "수요"], "무역적자."), F("대 중국 무역___ 규모는 갈수록 늘어나는 추세다. (surplus)", "흑자", ["적자", "물가"], "무역흑자."), F("일본 부품, 소재에 대한 ___가 여전하다. (dependence)", "의존도", ["수요", "신용"], "의존도."), F("지난해 같은 기간과 ___해 수출이 늘었다. (to compare)", "비교", ["계산", "저축"], "비교하다.")]
        + [read_q("우리나라의 대 일본 무역적자 규모가 더 커지고 있다"), read_q("일본 부품과 소재에 대한 의존도가 여전하다"), read_q("대 중국 무역흑자 규모는 갈수록 늘어나는 추세다"), read_q("자신의 지난 달 지출에 대해 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("덜하다", "to be less", "이 놀이공원은 주말에는 복잡하고 평일에는 덜해요.", "더하다"),
        ("무", "a radish", "저는 배추김치보다는 무김치가 더 좋아요."),
        ("포기", "counter for vegetables such as cabbage, lettuce, etc.", "요즘 배추 한 포기에 얼마나 해요?"),
    ]),
    ("학습활동 3", [
        ("급등하다", "(急騰) to rise rapidly", "중동분쟁 때문에 유가가 급등했어요.", "급락하다"),
        ("까다", "to peel (off)", "깐 마늘", "벗기다"),
        ("달리다", "to be in short supply", "새로 출시된 스마트폰은 공급이 달려서 사려면 몇 달을 기다려야 한다."),
        ("-(으)ㄴ 듯하다", "to seem; to appear; to look (like); to be as if", "그 사람은 학생인 듯 했어요."),
        ("소매가", "(小賣價) retail (price)", "요즘 금값의 소매가가 삼 점 칠오 그램에 이십오만 원이 넘는다고 합니다.", "도매가"),
        ("안팎", "more or less; “inside and outside”", "올 하반기에 생필품 가격이 오 퍼센트 안팎으로 오를 것이라고 합니다.", "내외"),
        ("잦다", "to be frequent", "남편이 실직한 후에 부부 싸움이 잦아졌다."),
        ("폭염", "(暴炎) heat wave; scorching heat; “fierce heat”", "경기 지방에 폭염 주의보가 내렸습니다.", "무더위, 찜통 더위, 열대야"),
    ]),
    ("학습활동 4", [
        ("갈수록", "as time goes by", "갈수록 봄과 가을이 짧아지고 있어요."),
        ("액정", "(液晶) liquid crystal", "액정 시계"),
        ("여전하다", "(如前) to remain the same; “same as before”", "아버지는 옛날에도 골프를 잘 치셨는데 지금도 여전하세요."),
    ]),
]
L3 = lesson(
    "U18 L1 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 덜하다 · 무 · 포기 · 급등 · 까다 · 달리다 · 듯하다 · 소매가 · 안팎 · 잦다 · 폭염 · 갈수록 · 액정 · 여전하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no Hanja or example for 액정 beyond the phrase 액정 시계, and 까다’s example is the phrase 깐 마늘. 포기 has a homonym 抛棄, “giving up”; 달리다 has the homonym meaning “to run; to race”. The book writes the entry as “소매(가)” and “도매(가)”, which I wrote as 소매가 and 도매가; the examples of 소매가 and 안팎 have 3.75g, 25만 원 and 5% in digits, which I spelled out (삼 점 칠오 그램, 이십오만 원, 오 퍼센트). In the example of 덜하다 the book has no space in “주말에는복잡하고”, which I corrected; in the example of 듯하다 it spells “듯 했어요” with a space, which I kept.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=8, nread=7)),
)

# ================================================================== L4 Part 2
_SUN1 = [
    ("저축은행 햇살론 일 호 대출자는 삼십 대 직장인", "The first Sunshine Loan borrower at a savings bank is a worker in his thirties"),
    ("한 인쇄소에 다니는 직장인 한 사람이 이십육 일 오전 팔백만 원을 대출받고 활짝 웃는 표정으로 저축은행 문을 나섰다.", "A worker at a printing shop left the savings bank with a broad smile on the morning of the 26th after taking out a loan of 8 million won."),
    ("이 직장인은 이날 출시된 서민전용 대출상품 햇살론의 저축은행 일 호 대출자다.", "He is the first savings-bank borrower of the Sunshine Loan, the loan product exclusively for ordinary people launched that day."),
    ("이 직장인은 직장 근처의 저축은행이 문을 열기를 기다려 상담을 받은 뒤 연 십이 점 팔 퍼센트의 이자율로 팔백만 원의 생계자금을 원리금 삼 년 분할 상환 조건으로 빌렸다.", "After waiting for the savings bank near his workplace to open and receiving a consultation, he borrowed living funds of 8 million won at an annual interest rate of 12.8 percent on the condition of repaying the principal and interest in installments over three years."),
    ("인쇄소에 근무한 것은 사 년 정도로 연소득은 천육백만 원 내외다.", "He has worked at the printing shop for about four years, and his annual income is around 16 million won."),
    ("결혼 일 년 차인 이 직장인은 임신 육 개월인 부인의 출산을 앞두고 병원비를 비롯해 목돈이 필요하지만 신용등급이 칠 등급이어서 그동안 은행을 이용하긴 쉽지 않았다.", "In his first year of marriage, he needs a lump sum, including hospital costs, ahead of the childbirth of his wife, who is six months pregnant, but because his credit rating is grade 7, using a bank had not been easy until now."),
    ("대부업체를 이용하자니 사십 퍼센트가 넘는 고금리가 너무 부담스러워 행여나 하는 마음으로 햇살론을 찾게 됐다.", "Using a lending company was too burdensome with its high interest of over 40 percent, so he came to look for the Sunshine Loan with a faint hope."),
    ("그는 대출을 받은 직후 “대부분 서민은 신용등급이 낮아 은행 대출을 받기가 어렵다”며 “정부와 저축은행에서 신용등급이 낮은 경우에도 낮은 금리로 대출해 주는 제도를 만들어 줘 감사하다”고 말했다.", "Right after taking out the loan, he said, “Most ordinary people have low credit ratings, so it is hard to get a bank loan,” and, “I am grateful that the government and the savings banks have created a system that lends at a low interest rate even to those with low credit ratings.”"),
    ("그러나 그는 “신용등급이 칠 등급이어서 최대 대출액이 팔백만 원인데 대출금액을 조금 더 확대해 줬으면 좋겠다”고 아쉬움을 표시하기도 했다.", "But he also expressed his regret, saying, “Because my credit rating is grade 7, the maximum loan amount is 8 million won; I wish they would expand the loan amount a little more.”"),
    ("또 “팔백만 원을 대출받으면서 삼 년치 보증수수료 이십사만 원을 미리 냈는데 적지 않은 돈”이라며 “서민을 위해 정부에서 보증을 해 주는 만큼 보증수수료를 안 받든가, 줄여 줬으면 좋겠다”고 제안했다.", "He also suggested, “When I took out the 8 million won, I paid 240,000 won of guarantee fees for three years in advance, which is not a small amount; since the government gives the guarantee for ordinary people, I wish they would not charge a guarantee fee, or reduce it.”"),
]
_FSS1 = [
    ("서민금융상담 서울 광주 대전 발길", "Financial counseling for ordinary people: visits to Seoul, Gwangju and Daejeon"),
    ("금융감독원은 다음달 서울과 광주, 대전에서 찾아가는 맞춤형 서민금융상담 서비스를 시행한다고 십사 일 밝혔다.", "The Financial Supervisory Service announced on the 14th that next month it will carry out its “visiting, tailored financial counseling for ordinary people” service in Seoul, Gwangju and Daejeon."),
    ("이번 행사에서 금감원과 미소금융중앙재단, 신용회복위원회 등 열 개 기관은 서민금융에 대한 정보와 개별 상담 등을 진행하게 된다.", "At this event, ten institutions, including the FSS, the Micro-Credit Central Foundation and the Credit Counseling and Recovery Service, will provide information on financing for ordinary people and individual consultations."),
    ("십일 월 십오 일 서울을 시작으로 십팔 일 광주, 십구 일 대전 행사가 예정돼 있다.", "Events are scheduled starting in Seoul on November 15, then Gwangju on the 18th and Daejeon on the 19th."),
    ("금감원은 특히 현장에 개별 상담 창구를 운영해 사금융 피해는 물론 서민대출상품 설명, 개인파산, 개인회생 등의 절차에 대한 상담을 벌일 예정이다.", "The FSS plans in particular to run individual counseling desks on site, offering consultations not only on damage from private lending but also on explanations of loan products for ordinary people and procedures such as personal bankruptcy and personal rehabilitation."),
    ("조성목 금감원 서민금융지원실장은 “지난해 시범운영했는데 참가자들의 반응이 좋아 올해는 참여기관을 늘려 확대시행하게 됐다”며 “신용관리 방법과 종잣돈 마련하는 노하우 등 가계 경제를 살리는 방안도 설명할 계획”이라고 말했다.", "Jo Seong-mok, head of the FSS’s Support Office for Financing of Ordinary People, said, “We ran a pilot last year and the participants’ response was good, so this year we have increased the participating institutions and expanded the program,” and, “We plan to explain ways of reviving household economies, such as credit management methods and know-how for building seed money.”"),
    ("금융감독원, 서민금융 일일구 서비스, 한국이지론 누리집에서 참가 신청이 가능하다.", "You can apply to take part on the websites of the Financial Supervisory Service, the “Financial Services for Ordinary People 119” and Korea Easy Loan."),
]
_SPEAK1B = [("신용등급이 낮은 친구가 있습니다.", "You have a friend with a low credit rating."), ("그 친구에게 신용등급을 높일 수 있는 방법에 대해 이야기해 주세요.", "Tell that friend about ways to raise a credit rating."), ("미국에서 학생이나 군인이 받을 수 있는 대출에 대해 이야기해 보세요.", "Talk about the loans a student or a soldier can get in the United States."), ("얼마나 얼마 동안 받을 수 있는지, 이자 등 어떤 조건이 있는지 말해 보세요.", "Tell how much and for how long it can be received, and what conditions, such as interest, apply.")]
L4 = lesson(
    "U18 L1 · Part 2 (본 학습): the Sunshine Loan and financial counseling for ordinary people",
    "본 학습 · 신용등급 · 미소금융 · 금융감독원 · 햇살론 · 대출 · 이자율 · 상환 · 서민금융상담 · 사금융 · 파산 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 (Let’s find out): the book’s three notes", "1. 신용등급 (credit rating): In Korea, a person’s credit is rated from 1 to 10, with 1등급 the highest and 10등급 the lowest. A person with a credit rating of 10 is called a 신용불량자 (delinquent borrower; “bad credit person”). A credit rating can affect several aspects of a person’s life, even the ability to get a job; a 신용불량자 cannot get a loan or any banking services. 2. 미소금융 (Micro-Credit), launched in Korea in 2009, is a small loan service that helps low-income individuals or those with bad credit (lower than a rating of 7) achieve financial independence; the loans are for establishing a source of income such as a small business, require no security deposit or guarantee, and are usually from 5 to 50 million won with a 2.0 to 4.5% interest rate. 3. 금융감독원 (a.k.a. 금감원, the Financial Supervisory Service) was established on 2 January 1999 under the amended act for the Establishment of Financial Supervisory Organizations, bringing together four supervisory bodies (banking, securities, insurance and non-bank) into one; its main function is examination and supervision of financial institutions."),
        card("학습활동 2: an article about a worker who used the Sunshine Loan (Kyunghyang)", "The book asks you to fill an English table (the borrower’s occupation and income, loan amount, interest rate and repayment plan) and to answer why he applied for the loan and which areas of the Sunshine Loan he thinks could be improved. The book names the borrower by his family name and age and gives his workplace’s district and the bank’s name; because he is a private person, I left those out and wrote “a worker”. The figures are spelled in Hangul. The article, with my English:", examples=passage(_SUN1)),
        card("My answers to 학습활동 2", "Table: occupation and income: a printing-shop worker, about 16 million won a year; loan amount: 8 million won; interest rate: 12.8 percent a year; repayment plan: principal and interest in installments over three years. A. Why: he needs a lump sum, including hospital costs, ahead of the birth of his child; with a credit rating of grade 7, using a bank was not easy; a lending company’s interest of over 40 percent was too heavy. B. Areas to improve: he wishes the maximum loan amount (8 million won) were a little larger, and the guarantee fee (240,000 won for three years, paid in advance) were waived or reduced."),
        card("학습활동 3: an article about financial counseling (Hankyoreh)", "The book asks (1) what financial service the announcement is about, (2) which services it offers (improved investment products; bankruptcy filing; help for people looking for a better-paying job; help for people victimized by loan sharks; credit restoration), and (3) to translate the underlined sentence (the underline is not marked in the text). The arrow of the headline cannot be read aloud, so I removed it; the website addresses are left out and “119” is written 일일구. The article, with my English:", examples=passage(_FSS1)),
        card("My answers to 학습활동 3", "1. “Visiting, tailored financial counseling for ordinary people”, run by the Financial Supervisory Service with other institutions in Seoul, Gwangju and Daejeon. 2. Bankruptcy filing; help for people victimized by loan sharks (private lending); credit restoration. (Not: improved investment products, nor help finding a better-paying job.)"),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts (the English is mine):", examples=passage(_SPEAK1B)),
        card("Activities left out", "학습활동 1 (Listening and video, tracks 004 and 005): a YTN news item about the new Sunshine Loan (햇살론): you answer who can apply, what the interest rate is, and what the figures 10,000,000 won and 50,000,000 won indicate, then check with the video. It is audio and video."),
    ],
    exercises=uniq(
        _tr(_SUN1[1:], k=3) + _tr(_FSS1[1:], k=3)
        + [M("What is the Sunshine Loan?", "A loan product exclusively for ordinary people", ["A mortgage for rich people", "A credit card", "A savings plan for children"], "서민전용 대출상품."), M("How much did the worker borrow?", "8 million won", ["80 million won", "800,000 won", "1.6 million won"], "팔백만 원."), M("What was the interest rate of his loan?", "12.8 percent a year", ["2.8 percent", "40 percent", "4.5 percent"], "십이 점 팔 퍼센트."), M("Why was using a bank not easy for him?", "His credit rating was grade 7", ["He had no job", "He was a minor", "He lived abroad"], "칠 등급."), M("What did he wish for the guarantee fee?", "That it be waived or reduced", ["That it be raised", "That it be paid monthly", "That it be refunded to the bank"], "안 받든가, 줄여."), M("When will the FSS counseling events be held, according to the article?", "In Seoul, Gwangju and Daejeon next month", ["Only in Seoul", "Only online", "In Busan next year"], "서울과 광주, 대전."), M("Which of these is among the services offered?", "Consultation on personal bankruptcy", ["Help getting a job", "Stock tips", "Free loans"], "개인파산."), M("What lowest rating means a person is a 신용불량자?", "Grade 10", ["Grade 1", "Grade 5", "Grade 7"], "십 등급.")]
        + [F("신용___이 칠 등급이어서 최대 대출액이 팔백만 원이다. (credit rating)", "등급", ["금리", "자금"], "신용등급."), F("원리금 삼 년 ___ 상환 조건으로 빌렸다. (installment)", "분할", ["회복", "파산"], "분할."), F("대부업체의 사십 퍼센트가 넘는 ___는 너무 부담스러웠다. (high interest)", "고금리", ["저금리", "원금"], "고금리."), F("개인파산, 개인___ 등의 절차에 대한 상담을 벌인다. (rehabilitation)", "회생", ["상환", "시행"], "개인회생.")]
        + [read_q("햇살론은 서민전용 대출상품이다"), read_q("신용등급이 낮아 은행 대출을 받기가 어렵다"), read_q("보증수수료를 안 받든가 줄여 줬으면 좋겠다"), read_q("서민금융상담 서비스를 시행한다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("대부업체", "(貸付業體) a lending company", "", "사금융"),
        ("대출(하다/받다)", "(貸出) a loan (to loan)", "등록금 대출을 받으려면 어떻게 해야 합니까?"),
        ("떨어지다", "to fall behind; to be low(er); to be inferior; “to fall”", "준성 씨가 병헌 씨에 비해 외국어 실력이 떨어진다."),
        ("등급", "(等級) rating; class; grade", "외환위기 때 우리나라의 신용등급이 하향 조정되었습니다."),
        ("서민", "(庶民) the (common) people; working classes; “commoners”", "정치인들이 서민 경제를 살리겠다는 공약을 내걸었습니다."),
        ("시행(하다/되다)", "(施行) implementation (to implement/to be implemented)", "새로운 법이 언제부터 시행됩니까?"),
        ("자금", "(資金) fund; money; capital", "사업 자금을 빌리려고 하는데 이자율이 얼마나 될까요?"),
        ("초반", "(初盤) the early phase; the early stage", "삼십 대 초반으로 보이는 남자가 한 선생님을 찾아왔었습니다.", "중반, 후반"),
        ("출범(하다)", "(出帆) launching (to launch)", "새 정부 출범 이후로 남북관계가 경색되었습니다."),
    ]),
    ("학습활동 2", [
        ("금리", "(金利) interest rate; lending rate", "한국은행이 금리를 내리기로 결정했습니다.", "이자율"),
        ("분할", "(分割) division; installment; “dividing into pieces”", "냉장고를 십 개월 분할로 샀어요.", "할부"),
        ("상환(하다)", "(償還) repayment; payback (to repay)", "은행에서 돈을 대출했는데 상환할 능력이 없어요."),
        ("아쉬움", "a feeling that more (of something) is desired", "우루과이와의 축구 경기는 아쉬움이 남는 경기였다. 조금 더 적극적으로 공격을 했으면 이길 수도 있었을 텐데.", "아깝다"),
        ("원리금", "(元利金) principal and interest", "원리금 상환 날짜를 연장해 주세요.", "원금, 이자"),
    ]),
    ("학습활동 3", [
        ("금융감독원", "Financial Supervisory Service (FSS)", "", "금감원"),
        ("누리집", "home page", "제 누리집을 많이 방문해 주세요.", "홈피, 누리꾼"),
        ("맞춤형", "(型) tailored; “tailor type”", "맞춤형 여행지도. 맞춤형 건강관리."),
        ("사금융", "(私金融) private loan; private money lending", "은행에서 대출을 받지 못한 사람들이 돈을 빌리기 위해 사금융을 찾습니다.", "사채"),
        ("살리다", "to save; to salvage; to spare", "경제를 살리기 위해 전 국민이 노력하고 있습니다."),
        ("종잣돈", "(種子) seed money", "우리는 사업을 하기 위해 종잣돈을 마련하려고 합니다."),
        ("파산(하다)", "(破産) bankruptcy (to go bankrupt)", "경제가 나빠지면서 파산을 신청하는 개인이 늘고 있습니다."),
        ("회복(하다/되다)", "(恢復) recovery; restoration (to restore/to be restored)", "경기가 서서히 회복되고 있습니다."),
        ("회생(하다)", "(回生) coming to life again (to come to life again; to resurrect)", "환자가 회생할 가능성이 얼마나 됩니까?"),
    ]),
]
L5 = lesson(
    "U18 L1 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 대부업체 · 대출 · 등급 · 서민 · 시행 · 자금 · 초반 · 출범 · 금리 · 분할 · 상환 · 아쉬움 · 원리금 · 금융감독원 · 누리집 · 맞춤형 · 사금융 · 살리다 · 종잣돈 · 파산 · 회복 · 회생",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 대부업체 and 금융감독원 (which has no Hanja there and lists the short form 금감원) and gives for 맞춤형 only the Hanja 型 and two phrases. 대부업체 lists 사금융 as a related word. 원리금 lists 원금 (principal) and 이자 (interest) as related words. 초반 lists 중반 and 후반 (the middle and the late phase). The book writes 30대 and 10개월 in digits, which I spelled out. The examples of 아쉬움 have two sentences, which I joined. The names in the example of 떨어지다 (준성, 병헌) are the book’s.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=12)),
)

# ================================================================== L6 Part 3
_HYU1 = [
    ("차 브랜드, 생활 속으로 씽씽", "Car brands zoom into everyday life"),
    ("국내에서는 그동안 생소했던 자동차회사의 브랜드 컬렉션 마케팅이 본격화되고 있다.", "In Korea, the brand collection marketing of car companies, which had been unfamiliar until now, is getting into full swing."),
    ("최근 현대, 기아차가 잇따라 관련 상품들을 내놓으면서 자동차 브랜드 컬렉션에 대한 관심이 높아지고 현대차는 따로 관련 팀을 꾸려 상품을 집중 개발하는 중이다.", "As Hyundai and Kia have recently put out related products one after another, interest in car brand collections is rising, and Hyundai has set up a separate team and is intensively developing products."),
    ("브랜드 컬렉션 마케팅은 단순하게 말하면 자동차 브랜드를 이용해 다른 상품을 개발하는 것이다.", "Brand collection marketing, simply speaking, is developing other products by using a car brand."),
    ("최근 현대차가 내놓은 제네시스의 다이캐스팅 단조로 만든 장난감, 쏘나타와 투싼 자전거 등이 대표적인 예다.", "Representative examples are the die-casting of the Genesis (a toy made by forging) that Hyundai recently put out, and the Sonata and Tucson bicycles."),
    ("업체로서는 이런 브랜드 컬렉션 마케팅이 일석이조를 넘어 삼조, 사조의 효과를 낸다.", "For the company, this kind of brand collection marketing has the effect not of two birds with one stone but of three, four."),
    ("우선 소비자가 일상 자동차 브랜드가 찍힌 상품에 물들면서 그 브랜드에 대한 친근함과 애착을 높일 수 있다.", "First, as consumers become tinged by products stamped with a car brand in daily life, they can raise their familiarity with and attachment to that brand."),
    ("특히 어린이를 겨냥한 키즈 마케팅은 미래 잠재고객에게 브랜드 선호도를 높일 수 있는 기회다.", "In particular, kids marketing aimed at children is a chance to raise brand preference among future potential customers."),
    ("현대차가 올해 초 꾸린 유스마케팅팀도 이 부분에 주목하고 있다.", "The youth marketing team that Hyundai set up early this year is also paying attention to this part."),
    ("유스마케팅팀 권기철 과장은 “청소년이나 어린이들이 앞으로 구매력을 갖춘 고객으로 성장한 뒤를 노리는 측면도 있지만 그들의 주위에 있는 어른들에게도 브랜드 이미지를 높이는 효과가 있다”고 말했다.", "Gwon Gi-cheol, section head of the youth marketing team, said, “There is the aspect of aiming at the time after young people and children grow into customers with purchasing power, but it also has the effect of raising the brand image among the adults around them.”"),
    ("현대차 로고가 찍힌 장난감을 갖고 놀거나 붕붕차를 타는 아이는 커서 현대차 고객이 될 가능성이 높고 더불어 함께 놀아 주는 부모도 고객으로 끌어들일 수 있는 가능성이 생긴다는 말이다.", "It means that a child who plays with a toy stamped with the Hyundai logo or rides a toy car is likely to become a Hyundai customer when grown, and that there is also a possibility of drawing in the parents who play with the child as customers."),
    ("현대, 기아차는 앞으로 더 다양한 상품을 출시하는 것과 동시에 장기적으로는 게임이나 애니메이션 등 콘텐츠 사업에까지 이런 브랜드 마케팅을 적용할 계획이다.", "Hyundai and Kia plan to release a greater variety of products in the future and, at the same time, in the long term to apply this kind of brand marketing even to content businesses such as games and animation."),
    ("현대차 관계자는 “전에는 현대차 브랜드를 붙여 봤자 그걸 누가 살까 하는 생각이 강했지만 이제는 양상이 조금 달라지고 있다”며 “현대차의 디자인이 접목된 창의적인 생활 속 소품들을 계속 낼 것”이라고 말했다.", "A Hyundai official said, “Before, there was a strong feeling of ‘even if we attach the Hyundai brand, who would buy it?’, but now the situation is changing a little,” and, “We will keep putting out creative everyday accessories grafted with Hyundai’s design.”"),
]
_SPEAK1C = [("미국의 최근 경제지표에 대해서 아는 대로 이야기해 보세요.", "Talk, as far as you know, about the latest economic indicators of the United States."), ("돈이 충분히 많다면 어디에 어떻게 쓰고 싶은지 서로 이야기해 보세요.", "Tell each other where and how you would like to spend money if you had plenty of it."), ("미국의 부자들 중에서 돈을 잘 쓰는 사람에 대해서 이야기해 보세요.", "Talk about people among the rich in the United States who spend their money well."), ("어떻게 돈을 벌었는지, 어떻게 잘 쓰고 있는지 이야기하세요.", "Tell how they earned their money and how they spend it well.")]
L6 = lesson(
    "U18 L1 · Part 3 (심화 학습): brand collection marketing of car companies",
    "심화 학습 · 브랜드 컬렉션 마케팅 · 키즈 마케팅 · 일석이조 · 애착 · 잠재고객 · 현대차 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: an article on the brand collection marketing of Hyundai and Kia (Hankyoreh)", "The book asks: (1) what brand collection marketing is and some examples; (2) what the author means by 일석이조 for car brand collection marketing; (3) the long-term plans of Hyundai-Kia for brand marketing. The company and model names are those of the published article; the parenthesis after 다이캐스팅 (“a toy made by forging”) I kept as part of the sentence, the quotation marks around 씽씽 and 다이캐스팅 are dropped, and “현대․기아차” is written 현대, 기아차. The article, with my English:", examples=passage(_HYU1)),
        card("My answers to 학습활동 2", "1. Brand collection marketing is, simply, developing other products using a car brand; examples: the die-cast Genesis toy and Sonata and Tucson bicycles. 2. 일석이조 means killing two birds with one stone; the article says that for the company this marketing does even better, with three or four effects: consumers become more familiar with and attached to the brand; children become future potential customers with higher brand preference; and the parents who play with them can also be drawn in (and the brand image rises among the adults around the children). 3. To release a greater variety of products, and in the long term to apply the brand marketing even to content businesses such as games and animation."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the third has two sentences; the English is mine):", examples=passage(_SPEAK1C)),
        card("Activities left out", "학습활동 1 (Listening, tracks 006 and 007): a YTN interview on the previous year’s Korean economic indicators: you summarize the first question and answer, and complete a summary of the second (among 30 OECD members only three nations …). 학습활동 3 (Listening, track 008): a radio talk by an expert: you summarize what the speaker says and what his organization is, and fill a table with the topic and details of his two messages. They are audio."),
    ],
    exercises=uniq(
        _tr(_HYU1[1:], k=3)
        + [M("What is brand collection marketing, simply speaking?", "Developing other products using a car brand", ["Selling used cars", "Lowering car prices", "Building car factories abroad"], "다른 상품을 개발."), M("Which is an example given in the article?", "A Sonata bicycle", ["A Genesis airplane", "A Tucson watch", "A Kia refrigerator"], "쏘나타와 투싼 자전거."), M("Whom does kids marketing aim at?", "Future potential customers", ["Retired people", "Foreign tourists", "Car dealers"], "미래 잠재고객."), M("What does 일석이조 mean?", "Killing two birds with one stone", ["Building a stone bridge", "One stone, no birds", "Two stones, one bird"], "One stone, two birds."), M("How else can the marketing affect the adults around children?", "It raises the brand image", ["It lowers car prices", "It makes them move", "It sells them toys"], "브랜드 이미지."), M("What long-term plan do Hyundai and Kia have?", "To apply brand marketing even to games and animation", ["To stop making toys", "To sell only bicycles", "To close the team"], "콘텐츠 사업."), M("How did the Hyundai official say the situation has changed?", "It used to be doubtful anyone would buy brand goods, but now it is changing", ["Nobody buys cars", "Prices have fallen", "Toys are banned"], "양상이 조금 달라지고 있다.")]
        + [F("현대차는 따로 관련 팀을 ___ 상품을 집중 개발하는 중이다. (to set up)", "꾸려", ["노려", "겨냥해"], "꾸리다."), F("어린이를 ___한 키즈 마케팅은 미래 잠재고객을 위한 기회다. (aimed at)", "겨냥", ["애착", "친근"], "겨냥하다."), F("브랜드에 대한 친근함과 ___을 높일 수 있다. (attachment)", "애착", ["본격화", "일석이조"], "애착."), F("브랜드를 붙여 ___ 그걸 누가 살까 하는 생각이 강했다. (even if)", "봤자", ["보러", "보니"], "-아/어 봤자.")]
        + [read_q("브랜드 컬렉션 마케팅이 본격화되고 있다"), read_q("브랜드 컬렉션 마케팅은 일석이조를 넘어 삼조 사조의 효과를 낸다"), read_q("어린이를 겨냥한 마케팅은 미래 잠재고객에게 브랜드 선호도를 높일 수 있는 기회다"), read_q("돈이 충분히 많다면 어디에 어떻게 쓰고 싶은지 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("다시 말씀 드려서", "in other words; “saying (it) again”", ""),
        ("대응(하다)", "(對應) action; response (to respond)", "이번 북한의 공격에 대해 정부가 어떤 대응을 할지 주목된다."),
        ("면하다", "(免) to escape; to avoid", "안전벨트를 하고 있어서 다행히 큰 부상은 면했다."),
        ("선방(하다)", "(善防) good defense (to put up a good defense; to defend well)", "일본과의 핸드볼에서 골키퍼의 선방으로 한국이 이겼다."),
        ("실질", "(實質) real; actual", "말만 하지 말고 실질적인 도움을 주세요."),
        ("원화", "(貨) won", "환율이 오르면 원화 가치가 떨어집니다."),
        ("위기", "(危機) a crisis", "우리나라 제조업이 위기에 있습니다."),
        ("이룩하다", "to accomplish", "우리나라는 천구백칠십 년대에 눈부신 경제 발전을 이룩했습니다.", "이루다"),
        ("인상(하다/되다)", "(引上) increase (to increase/to be increased)", "새해에 공공요금이 인상되었습니다.", "오르다 / 인하되다, 내리다"),
        ("자원", "(資源) natural resources", "우리나라는 우수한 인적자원이 많습니다.", "인적자원, 천연자원"),
        ("환산(하다/되다)", "(換算) converting (to convert; to change/to be converted)", "주부가 하는 집안일을 돈으로 환산하면 얼마나 될까요?"),
        ("환율", "(換率) a currency rate", "환율이 올라서 수출이 많이 증가했습니다."),
    ]),
    ("학습활동 2", [
        ("겨냥하다", "to aim at", "이 음악은 십 대 청소년들을 겨냥하고 있습니다."),
        ("꾸리다", "to manage; to run", "김병호 씨는 작은 회사를 꾸려 나가고 있습니다.", "살림을 꾸리다, 가정을 꾸려 나가다"),
        ("끌어들이다", "to induce or get someone involved in; to attract; to draw", "투자자들을 끌어들이기 위해 광고를 크게 했다."),
        ("내놓다", "to put out; to release", "그 회사는 새로운 디자인으로 신제품을 내놓았습니다.", "출시하다"),
        ("노리다", "to be after; to be out for; to have an eye on", "소매치기가 내 지갑을 노렸다."),
        ("다이캐스팅", "a die casting", ""),
        ("단순하게 말하면", "(單純) simply speaking", ""),
        ("물들다", "to be influenced; to be tinged; “to be dyed”", "나쁜 애들하고 놀더니 물들었구나. 다시는 그 애들을 만나지 마라."),
        ("본격화", "(本格化) full-scale; kicked into high gear", "다음 달부터 대통령 선거 운동이 본격화될 예정이다."),
        ("-아/어 봤자", "This conjunctive ending is used to imply that a certain effort will not produce any desired results. Because of this implication, the connective ending is often followed by 소용 없다 (no use).", "아무리 전화해 봤자 소용 없다. 운동을 해 봤자 운동 후에 많이 먹으니 살이 빠지지 않는다."),
        ("애착(을 가지다)", "(愛着) attachment (to a person/thing) (to be attached to; to have an attachment)", "이 차는 제 첫 번째 차에요. 그래서 특별한 애착을 가지고 있습니다."),
        ("일석이조", "(一石二鳥) killing two birds with one stone; “one stone, two birds”", "이 예금 상품은 수익성과 안정성이 다 높아서 일석이조입니다."),
        ("친근함", "(親近) being close; being familiar", "우리 옆집 사람은 제 어머니하고 비슷하게 생겼어요. 그래서 친근함을 느껴요."),
    ]),
    ("학습활동 3", [
        ("건전성", "(健全性) soundness; being sound", "이 회사에 대해 자산건전성을 평가하고 있습니다."),
        ("공익(적)", "(公益 or 公益的) (for) public interest; (for) the common good", "공익을 위해 전 국민이 노력합시다."),
        ("금융 기관", "(金融 機關) a financial institute", "저는 금융기관에서 일하고 있습니다."),
        ("기본", "(基本) basic; basis", "이 책은 컴퓨터에 기본이 없는 사람도 쉽게 이해할 수 있습니다."),
        ("나눔", "sharing", "한국 사회가 잘 살게 되면서 나눔의 문화도 성장하고 있습니다."),
        ("더 (이상) 바랄 게 없다", "nothing else is desired", "아들이 좋은 직장에 취직하고 좋은 여자를 만나 결혼하게 되어 이제 더 바랄 게 없네요."),
        ("설립(하다/되다)", "(設立) foundation; establishment; setting up (to found; to establish / to be founded; to be established)", "우리 회사는 중국 현지에 공장을 설립할 계획입니다."),
        ("수입", "(收入) income", "이번 달은 수입보다 지출이 더 많네요."),
        ("원칙", "(原則) a principle", "그 사람은 무슨 일이 있어도 원칙을 지킵니다."),
        ("지출(하다)", "(支出) expenditure; spending (to expend; to spend)", "이제부터 지출을 좀 줄여야겠어요."),
        ("통합(하다/되다)", "(統合) merging; combining (to merge/to be merged)", "학생 수가 줄어서 이 지역 초등학교를 통합한다고 합니다."),
        ("한도", "(限度) a limit; limitation", "이번 달에는 제출이 많아서 카드 한도를 넘었어요."),
        ("확립(하다/되다)", "(確立) establishment (to establish/to be established)", "정부는 법질서를 확립하겠다고 했습니다."),
        ("확보(하다/되다)", "(確保) securing (to secure/to be secured)", "지금은 자금 확보가 시급합니다."),
    ]),
]
L7 = lesson(
    "U18 L1 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 대응 · 면하다 · 선방 · 실질 · 원화 · 위기 · 이룩하다 · 인상 · 자원 · 환산 · 환율 · 겨냥하다 · 꾸리다 · 끌어들이다 · 내놓다 · 노리다 · 물들다 · 본격화 · 봤자 · 애착 · 일석이조 · 친근함 · 건전성 · 공익 · 나눔 · 설립 · 수입 · 원칙 · 지출 · 통합 · 한도 · 확립 · 확보",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no Hanja or example for 다시 말씀 드려서 (which it glosses “in other words”), 다이캐스팅, 나눔 and 이룩하다 (which lists 이루다 as similar). 원화 has only the Hanja 貨 in the book. 수입 has a homonym 輸入, “import”. 인상 lists 오르다 (to rise) and, after the slash, 인하되다, 내리다 (to be lowered; to go down). 자원 lists 인적자원, 천연자원 as related. The example of 한도 has 제출 for 지출 in the book (a typo), which I kept. The grammar entry -아/어 봤자 is explained with the book’s own English and two examples; the book writes 1970년대 and 10대 in digits, which I spelled out.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 1: The Domestic Economy (국내 경제)", [L1, L2, L3, L4, L5, L6, L7])
