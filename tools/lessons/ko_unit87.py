"""Unit 87: KBC Semester III, Unit 18, Lesson 2 - Economic Activities (경제활동).
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
_MATCH2 = [("발급하다", "to issue", "신용카드를 발급하다"), ("투자하다", "to invest", "주식에 투자하다"), ("구입하다", "to make a purchase", "홈쇼핑에서 구입하다"), ("급등하다", "to increase rapidly", "가격이 급등하다"), ("교환하다", "to exchange", "물건을 교환하다"), ("대출받다", "to get a loan", "학비를 은행에서 대출받다"), ("낭비하다", "to waste", "돈을 낭비하다"), ("요구하다", "to demand", "환불을 요구하다")]
_PAIR2 = [("증가하다", "감소하다", "to increase: to decrease"), ("낭비하다", "절약하다", "to waste: to economize"), ("줄이다", "늘리다", "to reduce: to increase"), ("빌리다", "갚다", "to borrow: to pay back"), ("구입하다", "판매하다", "to purchase: to sell"), ("상승하다", "하락하다", "to rise: to fall"), ("인상하다", "인하하다", "to raise (a price): to lower"), ("취업하다", "실직하다", "to get a job: to lose a job")]
_HJ2 = [("船 선", "ship; boat", "어선, 화물선"), ("期 기", "period of time; term", "분기, 장기"), ("業 업", "business; work; occupation", "기업, 조선업"), ("勢 세", "power; influence; force", "강세, 추세"), ("進 진", "go forward; progress", "진로, 선진국")]
_HJW2 = [("어선", "a fishing boat"), ("화물선", "a cargo ship"), ("분기", "a quarter/term (of a year)"), ("장기", "long-term"), ("기업", "a business; an enterprise"), ("조선업", "shipbuilding industry"), ("강세", "a bullish tendency (in the stock market); “strong power”"), ("추세", "trend"), ("진로", "a (future) path; course"), ("선진국", "an advanced country")]
_SIM2 = [("진급", "승진", "advancement in rank: promotion"), ("진행", "추진", "progress: pushing forward"), ("강세", "우세", "bullish tendency: superiority"), ("시기", "때", "a period: a time"), ("선박", "배", "a vessel: a boat")]
_CAT2 = [("공업, 서비스업, 무역업", "산업", "industry, service, trade: industries"), ("유조선, 어선, 군함", "선박", "tanker, fishing boat, warship: vessels"), ("장기, 만기, 단기", "기간", "long term, maturity, short term: period"), ("강세, 약세, 열세", "추세", "bullish, bearish, inferior: trend")]
_L2X = [("신용카드", "a credit card"), ("주식", "stock; shares"), ("홈쇼핑", "home shopping"), ("교환", "an exchange"), ("환불", "a refund"), ("갚다", "to pay back"), ("감소하다", "to decrease"), ("하락하다", "to fall"), ("인하하다", "to lower (a price)"), ("실직하다", "to lose a job"), ("진급", "advancement in rank"), ("진입", "entry"), ("진학", "going on to a higher school"), ("승진", "a promotion"), ("진행", "progress"), ("후진", "backwardness"), ("추진", "pushing forward"), ("증세", "a symptom"), ("약세", "a bearish tendency"), ("우세", "superiority"), ("열세", "inferiority"), ("시기", "a period"), ("선박", "a vessel"), ("선장", "a ship captain"), ("공업", "industry (manufacturing)"), ("서비스업", "the service industry"), ("무역업", "the trade business"), ("유조선", "an oil tanker"), ("군함", "a warship"), ("만기", "maturity (of a term)"), ("단기", "short term"), ("기간", "a period"), ("어업", "the fishing industry"), ("산업", "an industry")]
L1 = lesson(
    "U18 L2 · Review: economic-activity words and Sino-Korean 船 期 業 勢 進",
    "경제활동 · 단어 복습 · 한자어 복습 · 발급 · 투자 · 구입 · 급등 · 교환 · 대출 · 낭비 · 요구 · 船 期 業 勢 進",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives eight phrases with a word underlined and asks you to connect each with its English meaning. The underline is not marked in the text; the pairs below are my best reading:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH2], say=[0, 2])]),
        card("단어 복습 2: the words used as partners (my matching)", "Connect each word on the left with the word used as its counterpart on the right (the right-hand words are 늘리다, 갚다, 감소하다, 하락하다, 인하하다, 절약하다, 실직하다, 판매하다; the lines are not drawn in the text, so the matching is mine):", tables=[table(["Word", "Counterpart (my answer)", "Meaning"], [list(r) for r in _PAIR2], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ2], say=[2]), ktable(_HJW2)]),
        card("한자어 복습 1: the most similar word (my answers)", "Circle the word closest in meaning to the word on the left (A. 진급: 진입, 진학, 승진; B. 진행: 후진, 추진, 진로; C. 강세: 증세, 약세, 우세; D. 시기: 때, 곳, 땅; E. 선박: 화물선, 선장, 배).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM2], say=[0, 1])]),
        card("한자어 복습 2: the word that includes all three (my answers)", "Choose from the box (기간, 어업, 선박, 산업, 추세) the word that includes the three words of each line:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _CAT2], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L2X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH2], k=3) + _tr(_HJW2, k=3) + _tr(_L2X, k=4) + _tr([(a, b) for a, b, c in _PAIR2], k=3)
        + [M("What does the syllable 船 (선) mean?", "ship; boat", ["period of time", "business", "power"], "어선."), M("What does the syllable 期 (기) mean?", "period of time; term", ["ship", "business", "power"], "분기."), M("What does the syllable 業 (업) mean?", "business; work; occupation", ["ship", "period", "power"], "기업."), M("What does the syllable 勢 (세) mean?", "power; influence; force", ["ship", "period", "business"], "추세."), M("What does the syllable 進 (진) mean?", "go forward; progress", ["ship", "period", "power"], "진로.")
           , M("Which word is similar to 진급?", "승진", ["진입", "진학", "후진"], "Promotion."), M("Which word is similar to 강세?", "우세", ["증세", "약세", "열세"], "Superiority."), M("Which word covers 유조선, 어선, 군함?", "선박", ["어업", "산업", "기간"], "Vessels."), M("Which word covers 장기, 만기, 단기?", "기간", ["선박", "산업", "추세"], "Period."), M("Which word covers 강세, 약세, 열세?", "추세", ["기간", "선박", "어업"], "Trend."), M("Which word covers 공업, 서비스업, 무역업?", "산업", ["선박", "기간", "추세"], "Industries.")
           , F("신용카드를 ___하다. (to issue)", "발급", ["투자", "교환"], "발급하다."), F("주식에 ___하다. (to invest)", "투자", ["발급", "요구"], "투자하다."), F("물건을 ___하다. (to exchange)", "교환", ["구입", "낭비"], "교환하다."), F("환불을 ___하다. (to demand)", "요구", ["투자", "급등"], "요구하다."), F("학비를 은행에서 ___받다. (to borrow a loan)", "대출", ["교환", "발급"], "대출받다.")]
        + [read_q("신용카드를 발급하다"), read_q("주식에 투자하다"), read_q("학비를 은행에서 대출받다"), read_q("환불을 요구하다")]
    ),
)

# ================================================================== L2 Part 1
_GOLD2 = [
    ("재테크 수익률 금이 최고, 은행 예금, 부동산은 저조", "Gold is the best return on financial investment; bank deposits and real estate are low"),
    ("올해 들어 현재까지 최고 수익률을 나타낸 재테크 상품은 금투자였던 것으로 나타났다.", "It turned out that the financial investment product that has shown the highest return so far this year was gold investment."),
    ("구 일 대신증권이 주요 재테크 상품의 수익률을 비교한 결과 금이 팔 점 영육 퍼센트로 가장 높았다.", "As a result of Daishin Securities comparing the returns of major financial investment products on the 9th, gold was the highest at 8.06 percent."),
    ("비교시점은 이천구 년 말 대비 올해 팔 월 오 일 기준이다.", "The comparison point is as of August 5 this year, against the end of 2009."),
    ("한국금거래소에서 제공하는 국내 금 거래 도매가격 삼 점 칠오 그램, 한 돈 기준은 지난 오 일 현재 십팔만 사천이백오십 원을 기록해 지난해 십이 월 삼십일 일 십칠만 오백 원보다 만 삼천칠백오십 원 올랐다.", "The wholesale price of domestic gold trading provided by the Korea Gold Exchange (3.75 grams, one don) recorded 184,250 won as of the 5th, up 13,750 won from 170,500 won on December 31 last year."),
]
_SPEAK2 = [("여윳돈을 어떻게 관리하고 투자하면 좋은지 서로 이야기해 보세요.", "Tell each other how it is good to manage and invest extra money."), ("미국의 경제 대공황기에 어떤 일이 있었는지, 또 어려움을 극복하기 위해 어떤 일이 있었는지 아는 대로 이야기해 보세요.", "Talk, as far as you know, about what happened during the Great Depression in the United States and what was done to overcome the difficulties.")]
L2 = lesson(
    "U18 L2 · Part 1 (도입 학습): gold, the best financial investment of the year",
    "도입 학습 · 재테크 · 수익률 · 금투자 · 예금 · 부동산 · 도매가격 · 저조하다 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: a newspaper article on returns on investment (Kyunghyang)", "The book asks: (1) how investors got the best return; (2) using the article as an example, compare the advantages and disadvantages of savings, stocks and real estate and share your thoughts with a neighbor. The headline has “…” and “•”, which I replaced by commas; the numbers and dates are spelled in Hangul. The article, with my English:", examples=passage(_GOLD2)),
        card("My answers to 학습활동 3", "1. By investing in gold: gold returned 8.06 percent, the highest of the major products so far this year (between the end of 2009 and August 5 of the year). 2. (My own summary, since the article gives only the gold figure and the headline) Gold had the best return this year; bank deposits and real estate returned little. Deposits are safe but earn low interest; stocks and real estate can earn more but carry more risk; gold’s price can rise, as here, but it also moves."),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts; it adds the English “extra money” after 여윳돈 and “Great Depression” after 경제 대공황기, which I dropped (the English is mine):", examples=passage(_SPEAK2)),
        card("Activities left out", "학습활동 1: three posters or pictures about the economy (from Kobaco and edunet4u.net), for each of which you tick the fitting title (the book’s choices: 저축의 생활화, 올바른 소비 습관, 과소비; 아파트 건설 붐, 부동산 대책, 국민의 경제 회복 노력; 경제에서 정부 역할, 무역: 수출과 수입, 다양한 경제 활동). They are pictures, so I cannot tell which is right. 학습활동 2 (Listening, track 001): an MBC news item, to choose which of four sentences best describes it. 학습활동 4 (Listening, track 002): an edunet4u.net clip: you write its main idea and fill a table of the efforts of the company and of the people. They are audio."),
    ],
    exercises=uniq(
        _tr(_GOLD2, k=3)
        + [M("Which product had the highest return so far this year?", "Gold investment", ["Bank deposits", "Real estate", "Stocks"], "금투자."), M("What was the return of gold?", "8.06 percent", ["80.6 percent", "0.86 percent", "18 percent"], "팔 점 영육 퍼센트."), M("Which company compared the returns?", "Daishin Securities", ["A gold exchange", "A bank", "The government"], "대신증권."), M("What is the unit of 3.75 grams called?", "One don", ["One kilogram", "One ounce", "One pound"], "한 돈."), M("How much did the gold wholesale price rise?", "13,750 won", ["170,500 won", "184,250 won", "1,375 won"], "만 삼천칠백오십 원."), M("What does 저조하다 mean?", "To be low; to be poor", ["To be high", "To be rapid", "To be abundant"], "저조.")]
        + [F("올해 들어 최고 ___을 나타낸 재테크 상품은 금투자였다. (rate of return)", "수익률", ["수요", "물가"], "수익률."), F("한국금거래소에서 제공하는 국내 금 거래 ___가격. (wholesale)", "도매", ["소매", "원"], "도매가격."), F("은행 예금과 ___은 저조했다. (real estate)", "부동산", ["금투자", "수익률"], "부동산."), F("비교___은 이천구 년 말 대비 올해 팔 월 오 일 기준이다. (point in time)", "시점", ["기간", "수익"], "비교시점.")]
        + [read_q("올해 들어 최고 수익률을 나타낸 재테크 상품은 금투자였다"), read_q("은행 예금과 부동산은 저조했다"), read_q("금이 팔 점 영육 퍼센트로 가장 높았다"), read_q("여윳돈을 어떻게 관리하고 투자하면 좋은지 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 3", [
        ("저조하다", "(低調) to be low; to be poor", "이번 선거 참가율이 아주 저조합니다.", "낮다 / 고조"),
    ]),
    ("학습활동 4", [
        ("구조 조정", "(構造 調整) restructuring company size (often through layoffs)", "구조 조정으로 회사의 규모를 줄여야 한다."),
        ("외환", "(外換) foreign currency", "한국은 천구백구십칠 년에 외환 위기를 겪었다."),
        ("효율", "(效率) efficiency; effectiveness", "업무 효율을 높이기 위한 방안을 생각해 봅시다.", "능률, 효과 / 효율적"),
    ]),
]
L3 = lesson(
    "U18 L2 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 저조하다 · 구조 조정 · 외환 · 효율",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book lists 고조 and 낮다 beside 저조하다 without saying which is which; 고조 (a high point; a rise) is the opposite and 낮다 (to be low) the similar word, as I understand them, so I wrote them “낮다 / 고조”. 효율 lists 능률, 효과 as similar words and 효율적 as a derived form (separated by a slash). The book writes 1997년 in digits, which I spelled out.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=4, nread=4) + [M("What does 구조 조정 mean?", "Restructuring company size, often through layoffs", ["A foreign currency", "Efficiency", "A low point"], "구조 조정."), M("What does 외환 mean?", "Foreign currency", ["Efficiency", "Restructuring", "A loan"], "외환."), M("What does 효율 mean?", "Efficiency; effectiveness", ["Foreign currency", "Restructuring", "To be low"], "효율."), M("Which word is similar to 효율?", "능률", ["외환", "구조", "저조"], "능률, 효과.")]),
)

# ================================================================== L4 Part 2
_CON2 = [
    ("물건을 살 때 확신이 없는 경우라면 현금보다 신용카드로 결제하는 것이 좋다.", "If you are not sure when buying something, it is better to pay by credit card than by cash."),
    ("만약 판매하는 쪽에서 환불을 절대 해 줄 수 없다고 하더라도 신용카드사에 연락해 지불 거부를 신청할 수 있기 때문이다.", "That is because, even if the seller says it absolutely cannot give a refund, you can contact the credit card company and apply for a refusal of payment."),
    ("제품에 하자가 있거나 판매자가 사전에 공지했던 약속을 지키지 않았을 경우에는 법으로 보장된 교환, 환불 기간이 지나도 교환, 환불을 요구할 수 있다.", "If the product has a defect or the seller did not keep a promise announced in advance, you can demand an exchange or a refund even after the exchange and refund period guaranteed by law has passed."),
    ("상품권은 상법에 명시된 소멸 기간인 오 년이 지나지 않았다면 환불이 가능하다.", "A gift certificate can be refunded if the five-year expiration period stated in the commercial law has not passed."),
    ("한국소비자원에 상담 신청하기.", "Apply for counseling at the Korea Consumer Agency."),
    ("이리저리 뛰어 봐도 힘없는 소비자의 요구가 받아들여지지 않는다면 결국 소비자원이나 한국소비자연맹 등의 힘을 빌리는 수밖에 없다.", "If, however much you run about, the demands of a powerless consumer are not accepted, in the end there is nothing for it but to borrow the strength of the Consumer Agency or the Korea Consumers Union."),
    ("한국소비자원의 소비자상담팀에서는 소비생활과 관련된 피해나 불만을 상담, 처리해 준다.", "The consumer counseling team of the Korea Consumer Agency counsels on and handles damage or complaints related to consumer life."),
    ("전화, 팩스, 인터넷 등을 통해 불만 내용을 접수하면 된다.", "You can just file the content of your complaint by telephone, fax, the internet and so on."),
]
_SIT2 = [
    ("한 달 전에 백화점에서 가방을 샀습니다. 가방의 색깔이 한 달이 지난 후에 점점 변하고 손잡이가 떨어져 나갔습니다. 제품 보증 기간은 구매 후 이 주일입니다.", "I bought a bag at a department store a month ago. After a month, the color of the bag gradually changed and the handle came off. The product warranty period is two weeks after purchase."),
    ("새로 산 바지가 한 번 세탁을 한 후에 길이가 줄어서 회사의 고객 센터에 전화를 했는데 회사에서 응답이 없고 바꾸어 주지도 않습니다.", "My newly bought trousers shrank in length after one wash, so I called the company’s customer center, but the company does not respond and does not exchange them."),
    ("친구에게서 구두 회사의 상품권을 받았습니다. 그런데 전 구두가 너무 많아서 이것을 돈으로 바꾸어 다른 것을 사고 싶습니다.", "I received a gift certificate of a shoe company from a friend. But I have too many shoes, so I want to change it into money and buy something else."),
]
_ADV2 = [
    ("제품에 하자가 있으니 보증 기간이 지났어도 백화점에 교환이나 환불을 요구하세요. 그래도 안 되면 한국소비자원에 상담 신청을 하면 됩니다.", "Since the product has a defect, demand an exchange or a refund from the department store even if the warranty period has passed. If that still doesn’t work, you can just apply for counseling at the Korea Consumer Agency."),
    ("회사에서 응답이 없으면 한국소비자원에 전화나 인터넷으로 불만 내용을 접수하세요. 소비자원에서 상담하고 처리해 줄 겁니다.", "If the company doesn’t respond, file your complaint with the Korea Consumer Agency by telephone or the internet. The Agency will counsel you and handle it."),
    ("상품권은 소멸 기간인 오 년이 지나지 않았다면 환불이 가능하니까 돈으로 바꿔 달라고 요구하면 됩니다.", "A gift certificate can be refunded if its five-year expiration period has not passed, so you can just ask them to change it into money."),
]
_SPEAK2B = [("물건을 잘 못 사거나 속아서 산 경험 때문에 소비자 센터에 신고한 경험이 있으면 반에서 이야기해 보세요.", "If you have ever reported to a consumer center because of an experience of buying the wrong thing or buying after being deceived, tell the class."), ("소비자의 권리를 보호하기 위해 어떤 제도적 장치가 필요한지 반에서 토론해 보세요.", "Discuss in class what institutional mechanisms are needed to protect consumers’ rights.")]
L4 = lesson(
    "U18 L2 · Part 2 (본 학습): consumer rights, refunds and exchanges",
    "본 학습 · 소비자 권리 · 신용카드 결제 · 환불 · 교환 · 상품권 · 한국소비자원 · 하자 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: a newspaper article on consumers’ rights (Kyunghyang)", "The book asks: (1) summarize in English what consumers can do in each of the four situations (the four bullets); (2) for the three occurrences in a table, give advice in Korean using endings such as -(으)세요 and -(으)면 됩니다. The web address and the telephone number printed at the end are left out. The article, with my English:", examples=passage(_CON2)),
        card("My answers to 학습활동 3, task 1", "#1: If you are unsure when you buy, pay by credit card rather than cash, because even if the seller refuses a refund you can apply for a refusal of payment through the credit card company. #2: If the product has a defect or the seller broke a promise announced in advance, you can demand an exchange or refund even after the legal period. #3: A gift certificate can be refunded if the five-year expiration period in the commercial law has not passed. #4: Apply for counseling at the Korea Consumer Agency (or the Korea Consumers Union) by telephone, fax or the internet."),
        card("Task 2: the three occurrences of the book’s table", "The book gives these three occurrences in the left column of the table (the English is mine):", examples=passage(_SIT2)),
        card("Task 2: my advice in Korean", "The advice column is blank in the book. Here is my advice for each occurrence, in the order above:", examples=passage(_ADV2)),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts (the English is mine; the book writes 경험때문에 without a space in the first, which I corrected):", examples=passage(_SPEAK2B)),
        card("Activities left out", "학습활동 1 (Reading and writing): a public-interest advertisement poster from Kobaco, for which you make a fitting title in Korean and tick the sentences related to the poster’s suggestions (using scrap paper in the office; commuting by private car; commuting together in one car with colleagues; turning off the computer when not in use). It is a picture. 학습활동 2 (Listening and writing, track 003): an edunet4u.net clip with three cases: you choose its title (A. the convenience of parcel delivery; B. internet group buying; C. the good points of home shopping; D. consumer damage), fill a table of the three cases and write in Korean what you would do in the situation of the boy in an illustration. It is audio and a picture."),
    ],
    exercises=uniq(
        _tr(_CON2, k=3) + _tr(_ADV2, k=3)
        + [M("What payment method does the article recommend when you are unsure?", "A credit card", ["Cash", "A check", "A gift certificate"], "신용카드로 결제."), M("What can you apply for through the credit card company?", "A refusal of payment", ["A new card", "A loan", "A discount"], "지불 거부."), M("When can you demand an exchange or refund after the legal period?", "When the product has a defect or the seller broke a promise", ["Never", "When you change your mind", "When the shop closes"], "하자."), M("How long is the expiration period of gift certificates in the commercial law?", "Five years", ["One year", "Ten years", "Two weeks"], "오 년."), M("Where can you apply for counseling in the end?", "The Korea Consumer Agency", ["The police", "A bank", "A school"], "한국소비자원."), M("How can you file a complaint?", "By telephone, fax or the internet", ["Only in person", "Only by letter", "Only by e-mail"], "전화, 팩스, 인터넷.")]
        + [F("제품에 ___가 있으면 교환을 요구할 수 있다. (a defect)", "하자", ["상법", "공지"], "하자."), F("판매자가 사전에 ___했던 약속을 지키지 않았다. (to announce)", "공지", ["환불", "접수"], "공지하다."), F("상품권은 소멸 ___이 지나지 않았다면 환불이 가능하다. (period)", "기간", ["수익", "효율"], "소멸 기간."), F("불만 내용을 ___하면 된다. (to file)", "접수", ["환불", "교환"], "접수하다.")]
        + [read_q("물건을 살 때 확신이 없는 경우라면 신용카드로 결제하는 것이 좋다"), read_q("상품권은 소멸 기간인 오 년이 지나지 않았다면 환불이 가능하다"), read_q("전화나 팩스나 인터넷으로 불만 내용을 접수하면 된다"), read_q("소비자의 권리를 보호하기 위해 어떤 제도적 장치가 필요한지 토론해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 2", [
        ("택배", "(宅配) a parcel (delivery) service; a door-to-door delivery service", "택배로 물건을 부치면 두 시간 후에 받을 수 있습니다.", "퀵서비스"),
    ]),
    ("학습활동 3", [
        ("공지(하다)", "(公知) public announcement; notice (to make an announcement; to notify)", "채용 정보에 대한 공지 보셨어요?", "공고, 통지, 통보"),
        ("상법", "(商法) commercial law", "이번 학기에는 상법을 들어야 합니다."),
        ("상품권", "(賞品券) a gift card; a gift certificate; a merchandise bond/coupon", "경품에 당첨되시면 오만 원 상당의 상품권을 드립니다."),
    ]),
]
L5 = lesson(
    "U18 L2 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 택배 · 공지 · 상법 · 상품권",
    requires=[],
    cards=[card("A note on the Korean in this list", "택배 lists 퀵서비스 (“quick service”) as a related word. 공지 lists 공고, 통지, 통보 as similar words. The book writes 5만 원 in the example of 상품권 in digits, which I spelled out.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=4, nread=4)),
)

# ================================================================== L6 Part 3
_LOAN2 = [
    ("청년 신용불량의 덫 등록금 대출", "The trap of “youth credit delinquency”: tuition loans"),
    ("한 대학 졸업생은 지난해 팔 월만 해도 장밋빛 꿈을 꾸었던 평범한 대학 졸업생이었다.", "A university graduate was, as recently as last August, an ordinary university graduate who dreamed rosy dreams."),
    ("다른 학생과 차이가 있다면 가정형편으로 한 캐피털회사로부터 지난 사 년간 학자금 대출을 받았고 우여곡절 끝에 대학을 졸업했다는 점이다.", "If there was a difference from other students, it is that, because of family circumstances, he took out tuition loans from a capital company over the last four years and graduated from university after many twists and turns."),
    ("이 졸업생은 일 년에 천만 원 가까운 학자금 대출로 모두 사천여만 원, 이자 제외의 빚을 졌다.", "He ran up debts of about 40 million won in all, excluding interest, with tuition loans of nearly 10 million won a year."),
    ("문제는 대학졸업 후 취업을 기대했지만 취업난으로 십 개월간 본의 아니게 백수생활을 했다.", "The problem is that, although he expected to find a job after graduating, he lived an idle life for ten months against his will because of the job shortage."),
    ("결국 학자금 대출 상환을 제때 하지 못해 장기 연체자가 됐고, 얼마 지나지 않아 신용불량자로 전락했다.", "In the end, he could not repay the tuition loan on time, became a long-term delinquent, and before long fell into the status of a credit delinquent."),
    ("이 졸업생은 지인의 도움으로 한 중소업체에 어렵게 취업을 했다.", "With the help of an acquaintance, he found a job with difficulty at a small company."),
    ("하지만 신용불량자라는 사실이 뒤늦게 밝혀지면서 어렵사리 취업한 회사에서 쫓겨났다.", "But when the fact that he was a credit delinquent was revealed belatedly, he was kicked out of the company where he had found work with such difficulty."),
    ("그는 “대학 재학 당시 학자금 대출은 어려운 가정형편에서 대학을 졸업할 수 있다는 꿈 같은 제도였다”면서 “성적증명서 등 기본적인 여건만 충족하면 대부분 대출에 문제가 없었다”라고 말했다.", "He said, “While I was at university, the tuition loan was a dreamlike system that meant I could graduate from university in difficult family circumstances,” and, “If you met basic conditions such as a transcript, there was mostly no problem with the loan.”"),
    ("그는 “차라리 대학에 진학하지 않았으면 등록금을 대출받지 않았을 것”이라면서 “대출로 꿀맛 같았던 대학생활이 지금의 독이 되었다”라고 하소연했다.", "He complained, “If I had rather not gone on to university, I would not have taken out a loan for tuition,” and, “The university life that was as sweet as honey thanks to the loan has become poison now.”"),
    ("이처럼 학자금 대출로 대학을 졸업한 상당수가 취업을 못 해 신용불량자로 전락하고 결국엔 백수의 길로 접어드는 경우가 심심찮게 나타나고 있다.", "Cases are appearing not infrequently in which, like this, a considerable number of those who graduated from university with tuition loans cannot find work, fall into credit delinquency and finally enter the path of the jobless."),
]
_SPEAK2C = [("경제가 어려워지면 많은 사람들이 가계 규모를 줄입니다.", "When the economy gets difficult, many people reduce the scale of their household."), ("구체적으로 절약하는 방법에 대해 서로 이야기해 보세요.", "Tell each other concretely about ways of saving.")]
L6 = lesson(
    "U18 L2 · Part 3 (심화 학습): tuition loans and youth credit delinquency",
    "심화 학습 · 학자금 대출 · 신용불량 · 취업난 · 백수 · 연체자 · 전락 · 하소연 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a newspaper article on tuition loans (Kyunghyang)", "The book asks: (1) skim the article and circle the words that describe the borrower’s circumstances; (2) write in English a paragraph about what happened to him; (3) translate the underlined sentence (the underline is not marked in the text, so I give an English version of every sentence). The book names the graduate by his family name; because he is a private person, I wrote “a university graduate” and “he”. The figures are spelled in Hangul and the headline’s quotation marks are dropped. The article, with my English:", examples=passage(_LOAN2)),
        card("My answers to 학습활동 1", "1. The words I would circle: 장밋빛 꿈, 학자금 대출, 취업난, 백수생활, 장기 연체자, 신용불량자, 쫓겨났다. 2. A university graduate from a family in difficult circumstances took out tuition loans for four years, running up debts of about 40 million won excluding interest. After graduating he could not find work for ten months because of the job shortage, so he could not repay on time and became a long-term delinquent and then a credit delinquent. An acquaintance helped him find a job at a small company, but he was dismissed when his status was discovered. He says the loan was a dream-like system but that the university life it paid for has now become poison."),
        card("말해 봅시다! (speaking)", "The book’s prompt (two sentences; the English is mine):", examples=passage(_SPEAK2C)),
        card("Activities left out", "학습활동 2 (Listening, track 004): a YTN news item on credit cards: you write in English the reasons the two interviewees use credit cards and write in Korean the three types of business (first, second and third place) represented by the bars of a graph. 학습활동 3 (Listening, track 005): a commentary from the Donga on the structure of the Korean economy: you mark four statements true or false (the domestic economy has been improving because of a stronger job market; the unemployment rate of the middle class has been dropping; to strengthen the economy manufacturing jobs need to be decreased; many people have incurred debt in daily life), write two problems the middle class might face after the crisis, and list the commentator’s suggestions for helping the public overcome it. They are audio."),
    ],
    exercises=uniq(
        _tr(_LOAN2, k=3)
        + [M("What kind of loan did the graduate take out?", "A tuition (school expenses) loan", ["A housing loan", "A car loan", "A business loan"], "학자금 대출."), M("For how many months was he unemployed after graduation?", "Ten months", ["Four months", "One year", "Three months"], "십 개월."), M("What status did he fall into?", "A credit delinquent", ["A bankrupt company", "A student leader", "A scholarship holder"], "신용불량자."), M("What happened when the new company found out?", "He was dismissed", ["He was promoted", "He was transferred", "He was paid more"], "쫓겨났다."), M("How did he call his university life that the loan paid for?", "It has become poison", ["It was boring", "It was cheap", "It was too short"], "독이 되었다."), M("What did he say about the conditions for the loan?", "Basic conditions such as a transcript were mostly enough", ["Strict guarantors were needed", "It was very hard to get", "A job was required"], "기본적인 여건만.")]
        + [F("취업난으로 십 개월간 본의 아니게 ___생활을 했다. (idle, jobless)", "백수", ["학자금", "대출"], "백수."), F("학자금 대출 ___을 제때 하지 못해 장기 연체자가 됐다. (repayment)", "상환", ["충족", "하소연"], "상환."), F("신용불량자로 ___했다. (to fall)", "전락", ["충족", "대출"], "전락하다."), F("대출로 ___ 같았던 대학생활이 지금의 독이 되었다. (honey taste)", "꿀맛", ["하소연", "여건"], "꿀맛.")]
        + [read_q("학자금 대출로 대학을 졸업했다"), read_q("취업난으로 백수생활을 했다"), read_q("학자금 대출 상환을 제때 하지 못해 신용불량자로 전락했다"), read_q("구체적으로 절약하는 방법에 대해 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("꿀맛(이다)", "deliciousness; “honey taste” (to be sweet; to be delicious)", "배가 고플 때는 맛없는 음식도 꿀맛이다."),
        ("대출(하다/받다)", "(貸出) loan (to loan/to get a loan)", "이 대출 상품은 서민들을 위해 만들어졌습니다.", "융자"),
        ("백수(건달)", "(白手) (slang) a bum; a loafer; an idler; a person who is out of work", "해고 후에 백수 생활을 한 지 삼 개월이 되어 갑니다.", "실업자, 무직자"),
        ("여건", "(與件) a given condition", "집이 너무 작아서 공부할 여건이 안 됩니다.", "조건"),
        ("전락(하다)", "(轉落) downfall; degradation (to fall; to degrade)", "그 야구 팀은 지난해에 정규 리그 일 위를 했지만, 올해는 최하위로 전락하고 말았습니다.", "떨어지다, 하락하다"),
        ("충족(하다)", "(充足) satisfying (to satisfy; to meet)", "모든 조건을 충족하는 후보자를 찾고 있습니다."),
        ("하소연하다", "to complain; to appeal", "하소연할 수 있는 가족이 있어서 행복합니다."),
        ("학자금", "(學資金) school expenses; educational expenses; tuition", "저는 방학 때마다 학자금을 마련하기 위해 아르바이트를 합니다.", "학비, 교육비"),
    ]),
    ("학습활동 2", [
        ("간편하다", "(簡便) to be simple; to be convenient; to be easy; “to be simple and convenient”", "좀 간편한 방법을 찾아 봅시다.", "간단하다"),
        ("광범위하다", "(廣範圍) to be wide; to be broad; to be extensive", "이 식물은 한반도 주변에 광범위하게 분포되어 있다."),
        ("번거롭다", "to be cumbersome; to be inconvenient", "외국으로 송금하는 일은 매우 번거롭다.", "복잡하다"),
        ("세분화(하다/되다)", "(細分化) subdividing; classifying (to subdivide; to classify/to be subdivided; to be classified)", "현대사회는 직업들이 점점 세분화되는 경향이 있다."),
    ]),
    ("학습활동 3", [
        ("가계", "(家計) household finance", "요즘은 너무 어려워서 가계 지출을 줄이고 있습니다."),
        ("내수", "(內需) domestic demand/consumption", "내수가 살아나지 않으면 경기회복이 어렵습니다."),
        ("노숙자", "(露宿者) a homeless person", "경기불황으로 노숙자 수가 급증했다고 합니다."),
        ("실직(하다/되다)", "(失職) unemployment (to lose a job/to be unemployed)", "실직자들이 노숙자가 되는 경우가 많습니다.", "실업"),
        ("의존(하다)", "(依存) dependence (to depend)", "우리 경제는 수출에 너무 크게 의존하고 있습니다.", "의지하다"),
        ("자산", "(資産) assets; property", "사람은 중요한 자산입니다.", "재산"),
        ("중산층", "(中産層) the middle class", "최근 들어 중산층이 줄어들고 있다고 합니다.", "부유층, 서민층, 빈곤층"),
        ("파산(하다)", "(破産) bankruptcy (to go bankrupt; to go broke)", "재정난 때문에 파산절차를 밟고 있습니다."),
        ("활력", "(活力) vitality; energy; vigor", "운동은 삶에 큰 활력을 줍니다.", "활기"),
    ]),
]
L7 = lesson(
    "U18 L2 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 꿀맛 · 대출 · 백수 · 여건 · 전락 · 충족 · 하소연 · 학자금 · 간편하다 · 광범위하다 · 번거롭다 · 세분화 · 가계 · 내수 · 노숙자 · 실직 · 의존 · 자산 · 중산층 · 파산 · 활력",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 하소연하다’s synonym but gives one for 하소연하다 itself, and none for 간편하다 beyond the phrase. 백수(건달) has a homonym 百獸, “all kinds of animals”, and lists 실업자, 무직자 as similar words. 대출 lists 융자 as a similar word; 전락 lists 떨어지다, 하락하다. 중산층 lists 부유층, 서민층, 빈곤층 as related (the rich, ordinary and poor classes). The book writes 1위 in the example of 전락 in digits, which I spelled out (일 위).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 2: Economic Activities (경제활동)", [L1, L2, L3, L4, L5, L6, L7])
