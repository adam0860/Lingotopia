"""Unit 90: KBC Semester III, Unit 18, Lesson 5 - The World Financial Crisis and Recession (금융위기와 경기침체).
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
_MATCH5 = [("금융", "finance", "미국 금융회사들의 한국 투자가 증가하다"), ("위기", "crisis", "유럽국가들의 경제위기가 심각하다"), ("적자", "deficit", "수출기업의 적자가 커지다"), ("경기", "an economic condition", "경기가 나빠서 식당에 손님이 없다"), ("개발도상국", "a developing country", "개발도상국의 수출이 빠르게 증가하다"), ("실업률", "unemployment rate", "실업률이 높아지자 정부가 일자리 마련에 나서다"), ("성장률", "growth rate", "상반기에 이 퍼센트의 성장률을 기록하다"), ("부동산", "real estate", "부동산 가격의 폭락으로 경제가 불안하다")]
_OPP5 = [("성장", "하락", "growth: decline"), ("단기적", "장기적", "short-term: long-term"), ("취업", "실업", "getting a job: unemployment"), ("적절", "부적절", "appropriate: inappropriate"), ("적자", "흑자", "deficit: surplus")]
_HJ5 = [("家 가", "house; household; family", "가계, 가전제품"), ("苦 고", "bitter; painful; distressed", "고생, 고통"), ("不 부/불", "not; non", "불황, 부동산"), ("危 위", "dangerous; risky", "위기, 위험"), ("長 장", "long; big; chief", "장기, 학장")]
_HJW5 = [("가계", "household economy"), ("가전제품", "home appliances"), ("고생", "suffering"), ("고통", "pain; agony; distress"), ("불황", "an economic recession"), ("부동산", "an immovable piece of property; “not moving property”"), ("위기", "a crisis"), ("위험", "a danger"), ("장기", "long-term"), ("학장", "a dean; “school chief”")]
_SIM5 = [("가난", "생활고", "poverty: hardship of living"), ("고생", "어려움", "suffering: difficulty"), ("부정부패", "비리", "corruption: irregularities"), ("위해물", "유해물", "a hazardous object: a harmful object")]
_ODD5 = [("가계, 지출, 가능, 수입", "가능", "household, spending, possible, income"), ("고생, 경제난, 고발, 고통", "고발", "hardship, economic difficulty, accusation, pain"), ("부동산, 주식, 땅, 건물", "주식", "real estate, stock, land, building"), ("장수, 건강, 채식, 장남", "장남", "longevity, health, vegetarian diet, eldest son")]
_L5X = [("부유", "wealth"), ("하락", "a fall"), ("호황", "an economic boom"), ("일시적", "temporary"), ("자연적", "natural"), ("제조업", "manufacturing"), ("영업", "business; sales"), ("실업", "unemployment"), ("적합", "suitability"), ("적당", "appropriateness"), ("흑자", "a surplus"), ("전자", "electronics"), ("가난", "poverty"), ("생활고", "hardship of living"), ("침체", "stagnation"), ("개도국", "a developing country"), ("고민", "worry"), ("잔고", "a balance (in an account)"), ("부정부패", "corruption"), ("긍정적", "positive"), ("비리", "an irregularity; corruption"), ("위해물", "a hazardous object"), ("재해", "a disaster"), ("유해물", "a harmful object"), ("폐기물", "waste"), ("지출", "spending"), ("수입", "income"), ("경제난", "economic difficulty"), ("고발", "an accusation"), ("땅", "land"), ("건물", "a building"), ("장수", "longevity"), ("건강", "health"), ("채식", "a vegetarian diet"), ("장남", "the eldest son")]
L1 = lesson(
    "U18 L5 · Review: crisis words and Sino-Korean 家 苦 不 危 長",
    "금융위기와 경기침체 · 단어 복습 · 한자어 복습 · 금융 · 위기 · 적자 · 경기 · 개발도상국 · 실업률 · 성장률 · 부동산 · 家 苦 不 危 長",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its meaning", "The book gives eight sentences with a word underlined and eight English meanings. The underline is not marked in the text; the pairs below are my reading (the book’s 2퍼센트 is spelled 이 퍼센트):", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH5], say=[0, 2])]),
        card("단어 복습 2: the word with the opposite meaning (my answers)", "Circle the word opposite in meaning to the word on the left (A. 성장: 부유, 하락, 호황; B. 단기적: 일시적, 장기적, 자연적; C. 취업: 제조업, 영업, 실업; D. 적절: 부적절, 적합, 적당; E. 적자: 혹자, 흑자, 전자). The book prints 혹자 in E, probably a typo for 흑자 (a surplus).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP5], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ5], say=[2]), ktable(_HJW5)]),
        card("한자어 복습 1: the word closest in meaning (my answers)", "Choose the word closest in meaning to the word on the left (A. 가난: 생활고, 침체, 개도국; B. 고생: 고민, 어려움, 잔고; C. 부정부패: 부족, 긍정적, 비리; D. 위해물: 재해, 유해물, 폐기물).", tables=[table(["Word", "Closest (my answer)", "Meaning"], [list(r) for r in _SIM5], say=[0, 1])]),
        card("한자어 복습 2: the word unrelated to the others (my answers)", "Circle the word that is not related to the other three:", tables=[table(["Four words", "Odd one out", "Meaning"], [list(r) for r in _ODD5], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L5X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH5], k=3) + _tr(_HJW5, k=3) + _tr(_L5X, k=4)
        + [M("What does the syllable 家 (가) mean?", "house; household; family", ["bitter; painful", "not; non", "dangerous"], "가계."), M("What does the syllable 苦 (고) mean?", "bitter; painful; distressed", ["house", "not; non", "long; big"], "고생."), M("What does the syllable 不 (부/불) mean?", "not; non", ["house", "dangerous", "long; big"], "불황."), M("What does the syllable 危 (위) mean?", "dangerous; risky", ["bitter", "not; non", "long; big"], "위기."), M("What does the syllable 長 (장) mean?", "long; big; chief", ["house", "bitter", "dangerous"], "장기.")
           , M("Which word is the opposite of 성장?", "하락", ["부유", "호황", "침체"], "Decline."), M("Which word is the opposite of 취업?", "실업", ["제조업", "영업", "경기"], "Unemployment."), M("Which word is the opposite of 적자?", "흑자", ["전자", "부자", "수출"], "Surplus."), M("Which word is closest to 부정부패?", "비리", ["부족", "긍정적", "부유"], "Corruption."), M("Which word is unrelated to 부동산, 주식, 땅, 건물?", "주식", ["땅", "건물", "부동산"], "Stock is not immovable property."), M("Which word is unrelated to 가계, 지출, 가능, 수입?", "가능", ["가계", "지출", "수입"], "가능 is “possible”.")
           , F("___가 나빠서 식당에 손님이 없다. (the economy)", "경기", ["성장", "금융"], "경기."), F("수출기업의 ___가 커지다. (a deficit)", "적자", ["흑자", "성장"], "적자."), F("___률이 높아지자 정부가 일자리 마련에 나서다. (unemployment)", "실업", ["성장", "취업"], "실업률."), F("___ 가격의 폭락으로 경제가 불안하다. (real estate)", "부동산", ["금융", "수출"], "부동산.")]
        + [read_q("유럽국가들의 경제위기가 심각하다"), read_q("개발도상국의 수출이 빠르게 증가하다"), read_q("실업률이 높아지자 정부가 일자리 마련에 나서다"), read_q("부동산 가격의 폭락으로 경제가 불안하다")]
    ),
)

# ================================================================== L2 Part 1
_HOME5 = [
    ("미국 노숙 가족 이 년 연속 증가세", "Homeless families in the United States rise for the second year in a row"),
    ("미국에서 집 없는 설움을 견뎌야 하는 노숙 가족들이 늘고 있다.", "In the United States, homeless families, who must endure the sorrow of having no home, are increasing."),
    ("서브프라임모기지, 즉 비우량 주택담보대출 부실 사태와 그로 인해 촉발된 글로벌 금융위기는 더 많은 부모들로 하여금 어린 자녀들을 데리고 길거리에 나앉게 만들고 있다.", "The subprime mortgage, that is, non-prime housing-secured loan, insolvency crisis and the global financial crisis triggered by it are making more parents go out onto the street with their young children."),
    ("미 주택도시개발부, 에이치유디가 십육 일 의회에 제출한 보고서에 따르면 지난해 미 전체 노숙인 수는 백오십육만 명으로 전년 백육십만 명에 비해 오 퍼센트 감소했다.", "According to a report that the US Department of Housing and Urban Development (HUD) submitted to Congress on the 16th, the total number of homeless people in the US last year was 1,560,000, a 5 percent decrease from 1,600,000 the year before."),
    ("하지만 노숙 가족 수는 전년 십오만 구천백사십이 가구에서 십칠만 백이십구 가구로 증가했다.", "But the number of homeless families rose from 159,142 households the year before to 170,129 households."),
    ("서브프라임모기지 사태가 불거진 이천칠 년, 십삼만 구백육십팔 가구 이래 이 년 연속 증가세를 보였다.", "It has shown an upward trend for two years in a row since 2007, when the subprime mortgage crisis broke out (130,968 households)."),
    ("전체 노숙인 가운데 오십삼만 오천 명이 노숙 가족의 구성원들이다.", "Among all homeless people, 535,000 are members of homeless families."),
    ("에이치유디는 노숙인을 최소 하루 이상을 길거리나 보호시설에서 체류한 사람, 노숙 가족은 그 가운데 성인과 아동 각각 한 명 이상으로 구성된 가족 한 세대로 분류했다.", "HUD classified a homeless person as one who stayed on the street or in a shelter for at least a day, and a homeless family as one household among them made up of at least one adult and one child each."),
    ("노숙 가족들이 보호시설에서 체류한 기간도 이천팔 년 평균 삼십 일에서 지난해 삼십육 일로 늘어났다.", "The period that homeless families stayed in shelters also grew from an average of 30 days in 2008 to 36 days last year."),
    ("노숙 가족의 아동은 절반 이상이 여섯 살 이하의 어린 아이들이었다.", "More than half of the children of homeless families were young children of six or under."),
    ("에이치유디의 숀 도노번 장관은 어린 아이들이 있는 노숙 가족들이 점점 늘고 있다면서 이러한 자료를 바탕으로 노숙인들을 위한 우리의 대처도 달라질 것이라고 말했다.", "HUD Secretary Shaun Donovan said that homeless families with young children are increasing, and that on the basis of this data our response for the homeless will change."),
    ("도노번은 경기침체가 지속되면서 친척이나 친구들의 집에 살다가 보호시설로 나온 가족들, 이십구 점 사 퍼센트가 많아졌다면서 앞으로 노숙 가족들이 더 늘어날 것으로 전망했다.", "Donovan said that, as the recession continues, families who had lived in the homes of relatives or friends and came out to shelters (29.4 percent) have increased, and forecast that homeless families will increase further."),
    ("그는 다만 이들 가족이 길거리보다는 보호시설에서 지내는 경우, 육십 퍼센트가 더 많았다고 덧붙였다.", "He added, however, that there were more cases of these families living in shelters rather than on the street (60 percent)."),
]
_SPEAK5 = [("최근에 티브이나 인터넷 등에서 본 경제 관련 뉴스가 있으면 이야기해 보세요.", "If there is any economic news you recently saw on TV or the internet, talk about it."), ("주변에 미국의 경제 위기로 타격을 받은 사람이 있습니까?", "Is there anyone around you who was hit by America’s economic crisis?"), ("있으면 그 사람이 받은 타격에 대해 자세히 이야기해 보세요.", "If so, tell in detail about the blow that person received.")]
L2 = lesson(
    "U18 L5 · Part 1 (도입 학습): homeless families in the United States",
    "도입 학습 · 금융위기 · 경기침체 · 노숙 가족 · 노숙인 · 서브프라임모기지 · 보호시설 · 길거리에 나앉다 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: a news article on homeless families (Kyunghyang)", "The book asks three questions in English: what the article is about; the English meanings of 노숙인 and 노숙 가족; and what 535,000, 36 days and 60% indicate. The numbers, dates and HUD are spelled in Hangul and the quotation marks are dropped; the article names the US official by his public title and name, which I kept. The article, with my English:", examples=passage(_HOME5)),
        card("My answers to 학습활동 3", "1. It is about the rising number of homeless families in the United States, whom the subprime mortgage crisis and the global financial crisis have pushed onto the street. 2. 노숙인: a person who stayed on the street or in a shelter for at least a day; 노숙 가족: one household among those, made up of at least one adult and one child. 3. 535,000: the number of homeless people who are members of homeless families; 36 days: the average period that homeless families stayed in shelters last year (up from 30 days in 2008); 60%: the share of these families who stayed in shelters rather than on the street."),
        card("말해 봅시다! (speaking)", "The book’s two prompts, which I split into three sentences; the book writes TV, which I spelled 티브이 (the English is mine):", examples=passage(_SPEAK5)),
        card("Activities left out", "학습활동 1 (Reading): charts of the Korean economy (from Kyunghyang), each of which you label with one of eight titles (A. unemployment rate; B. real growth rate; C. number of bankrupt companies; D. number of people filing for bankruptcy; E. foreign exchange rate; F. rate of unpaid loans; G. legal disputes over personal loans; H. number of start-up companies). They are pictures. 학습활동 2 (Listening, track 001): a YTN news item on the US recession: you choose what the National Bureau of Economic Research announced (A. the recession ended last year; B. it will not end until June; C. employment has been increasing since December; D. a double-dip recession in the next six months), name two areas Americans are still concerned about and say why Americans will keep having a hard time for a while. It is audio."),
    ],
    exercises=uniq(
        _tr(_HOME5, k=3) + _tr(_SPEAK5, k=2)
        + [M("What kind of people are increasing in the United States, according to the article?", "Homeless families", ["Retired couples", "Immigrants", "Students"], "노숙 가족."), M("By how much did the total number of homeless people fall?", "5 percent", ["50 percent", "15 percent", "0.5 percent"], "오 퍼센트."), M("How many members of homeless families are there among the homeless?", "535,000", ["156,000", "170,129", "1,600,000"], "오십삼만 오천 명."), M("What was the average stay of homeless families in shelters last year?", "36 days", ["30 days", "60 days", "Six months"], "삼십육 일."), M("How old were more than half of the children of homeless families?", "Six or under", ["About ten", "Teenagers", "Over twelve"], "여섯 살 이하."), M("What does the idiom 길거리에 나앉다 mean?", "To become homeless", ["To start a business", "To take a walk", "To go abroad"], "길거리에 나앉다.")]
        + [F("서브프라임모기지 ___ 사태가 금융위기를 촉발했다. (insolvency)", "부실", ["부도", "파산"], "부실."), F("그는 앞으로 노숙 가족들이 더 늘어날 것으로 ___했다. (to forecast)", "전망", ["촉발", "분류"], "전망하다."), F("에이치유디가 의회에 ___한 보고서. (submitted)", "제출", ["촉발", "체류"], "제출하다."), F("그는 이들 가족이 보호시설에서 지내는 경우가 더 많았다고 ___. (to add)", "덧붙였다", ["밝혔다", "달라졌다"], "덧붙이다.")]
        + [read_q("미국에서 집 없는 설움을 견뎌야 하는 노숙 가족들이 늘고 있다"), read_q("노숙 가족 수는 십칠만 백이십구 가구로 증가했다"), read_q("노숙 가족의 아동은 절반 이상이 여섯 살 이하였다"), read_q("경기침체가 지속되면서 노숙 가족들이 더 늘어날 것으로 전망했다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("부도(나다)", "(不渡) bankruptcy (to go bankrupt)", "아버지 사업이 부도가 나서 저는 학교를 그만두어야 했습니다.", "파산"),
        ("실질(적)", "(實質的) real; actual", "그가 이번 사건의 실질적 책임자다.", "실질소득"),
        ("업체", "(業體) a business; an enterprise", "정부는 이번 공사를 민간 업체에 맡기겠다고 했습니다.", "회사, 기업"),
        ("추이", "(推移) the development or progress (of an incident or an affair)", "환자의 회복 추이를 보고 수술을 결정합시다.", "상황"),
        ("파산(하다)", "(破産) bankruptcy; failure (to go bankrupt; to fail)", "그 회사는 이미 파산한 것이나 다름없습니다.", "부도"),
    ]),
    ("학습활동 2", [
        ("고통", "(苦痛) pain; agony; torment; suffering", "남자친구와 헤어진 것은 저에게 큰 고통이었습니다."),
        ("급등(하다)", "(急騰) jump; sharp rise; surge; skyrocketing (to jump; to rise suddenly)", "태풍 때문에 쌀값이 급등했습니다.", "급락"),
        ("다우", "Dow Jones", ""),
        ("대공황", "(大恐慌) the Great Depression", ""),
        ("더디다", "to be slow; to be tardy", "경제 회복이 더뎌 많은 사람들이 고통을 받고 있습니다.", "느리다"),
        ("선언(하다/되다)", "(宣言) announcement; declaration (to declare/to be declared)", "야당 지도자들이 국회 앞에서 선언문을 발표한다고 합니다."),
        ("우려(하다/되다)", "(憂慮) fear; concern; worry (to fear/to be feared)", "대통령은 경제문제에 대해 깊은 우려를 표시했습니다."),
        ("전망(하다/되다)", "(展望) a prospect; an outlook; a forecast (to forecast/to be forecasted)", "내년도 경제 전망이 밝지 않다고 합니다."),
        ("종료(하다/되다)", "(終了) an end; a close (to end/to be over; to come to an end)", "서비스를 종료합니다."),
        ("증(권)시(장)", "(證券市場) the stock market", "증시가 강세를 돌아섰습니다."),
        ("지연(시키다/되다)", "(遲延) a delay; a postponement (to delay/to be delayed)", "악천후로 이륙이 지연되고 있습니다.", "늦어지다"),
        ("진정(되다)", "(鎭靜) cooling down; calming down (to cool down; to calm down)", "화만 내지 말고 좀 진정하세요."),
        ("체감경기", "(體感景氣) the business sentiment; economic condition being felt by households or people; “economic condition felt by body”", "경기지표는 상승했지만 체감경기는 아직도 나아지지 않았습니다.", "체감온도, 체감지수"),
        ("회복(하다/되다)", "(恢復) recovery; restoration (to recover; to restore; to regain/to be recovered)", "환자는 지금 빠른 속도로 회복하고 있습니다."),
    ]),
    ("학습활동 3", [
        ("길거리에 나앉다", "(idiom) to become homeless; to be forced out onto the street; “to go out and sit on the street”", "아버지의 사업실패로 가족들이 길거리에 나앉게 되었다."),
        ("덧붙이다", "to add", "제 말은 다 끝났습니다. 더 덧붙이실 말씀 있으십니까?"),
        ("의회", "(議會) an assembly; the National Assembly; Parliament; Congress", "새 법안이 의회를 통과했습니다."),
        ("촉발(하다/되다)", "(觸發) trigger; contact detonation (to detonate by contact/to be detonated)", "제이 차 세계대전이 어떻게 촉발되었습니까?"),
    ]),
]
L3 = lesson(
    "U18 L5 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 부도 · 실질 · 업체 · 추이 · 파산 · 고통 · 급등 · 대공황 · 더디다 · 우려 · 전망 · 종료 · 증시 · 지연 · 진정 · 체감경기 · 회복 · 길거리에 나앉다 · 덧붙이다 · 의회 · 촉발",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book prints the Hanja of 증(권)시(장) with the optional parts in parentheses (證(券)市(場)); I wrote 證券市場. 급등 lists 급락 as its opposite. The example of 촉발 has 2차 세계대전 in digits, which I spelled out (제이 차 세계대전). 다우 and 대공황 have no example in the book; 다우 has no Hanja because it is the English name “Dow Jones”. 부도 and 파산 list each other as similar words.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=12)),
)

# ================================================================== L4 Part 2
_IRE5 = [
    ("빈집만 삼십만 채, 부동산 거품 꺼지며 이민 행렬", "300,000 empty houses alone; as the real estate bubble bursts, a line of emigrants"),
    ("영국의 식민 지배를 받았던 섬나라 아일랜드는 오랫동안 서유럽 최빈국으로 불렸다.", "Ireland, an island country that was ruled as a colony by Britain, was long called the poorest country in Western Europe."),
    ("가난과 절망의 대명사인 아일랜드의 이미지를 결정적으로 굳힌 건 십구 세기 중반 인구 육백오십만 명 중 백만 명이 굶어 죽은 감자 대기근이다.", "What decisively fixed the image of Ireland, a byword for poverty and despair, was the Great Potato Famine in the mid-19th century, in which a million of a population of 6,500,000 starved to death."),
    ("서민들의 주식인 감자가 마름병 유행으로 수확량이 급감하면서 백만 명은 살 길을 찾아 미국 등지로 떠났다.", "As the harvest of potatoes, the common people’s staple food, dropped sharply with an epidemic of blight, a million people left for the United States and other places to find a way to live."),
    ("이후 흉년과 경기불황이 덮치면서 아일랜드인들은 외국행 배를 타는 전통을 따랐다.", "After that, as bad harvests and economic slumps struck, the Irish followed the “tradition” of boarding ships bound for foreign countries."),
    ("가난의 굴레를 못 벗을 것 같던 아일랜드는 천구백구십 년대에 놀라운 경제성장으로 주목받기 시작한다.", "Ireland, which seemed unable to throw off the yoke of poverty, began to attract attention in the 1990s with astonishing economic growth."),
    ("적극적 투자유치책과 서유럽 자본의 합작 결과로 켈틱, 즉 켈트족 호랑이라는 별명까지 얻었다.", "As a result of an active investment-attraction policy and collaboration with Western European capital, it even earned the nickname “Celtic (Celt) tiger.”"),
    ("천구백팔십 년대에 불황을 피해 이민을 간 아일랜드인들은 귀국길에 올랐고, 동유럽 노동자들도 몰려 왔다.", "Irish people who had emigrated in the 1980s to escape the slump started back home, and Eastern European workers also flocked in."),
    ("소득 수준은 식민 종주국이던 영국을 앞질렀다.", "Its income level surpassed that of Britain, its former colonial ruler."),
    ("세계 각지의 경제와 경영 연구자들과 기자들이 성공 비결을 배우려고 몰려든 것은 당연한 일이었다.", "It was natural that economics and management researchers and reporters from around the world swarmed in to learn the secret of its success."),
    ("그러나 신화는 이십일 일 아일랜드 정부의 구제금융 수용 선언으로 막을 내리는 분위기다.", "But the mood is that the myth is coming to an end with the Irish government’s declaration on the 21st that it would accept a bailout."),
    ("은행 부실로 올해 국내총생산, 지디피의 삼십이 퍼센트까지 솟을 것으로 예상되는 재정적자에 정부가 마침내 백기를 든 것이다.", "The government finally raised the white flag to a fiscal deficit expected to soar to 32 percent of this year’s gross domestic product (GDP) because of bank insolvency."),
    ("아일랜드의 처지를 급반전 시킨 주범은 부동산 거품과 은행 부실이다.", "The main culprits that suddenly reversed Ireland’s position are the real estate bubble and bank insolvency."),
    ("십여 년 전부터 저금리에 편승한 부동산 투자 붐이 휩쓸었고, 은행들은 외국에서 조달한 자금으로 거품을 키웠다.", "From more than ten years ago a real estate investment boom riding on low interest rates swept the country, and banks inflated the bubble with funds raised abroad."),
    ("그러나 이천팔 년 부동산 거품 붕괴와 금융위기로 대출 부실이 은행권을 덮쳤다.", "But with the collapse of the real estate bubble and the financial crisis in 2008, bad loans struck the banking sector."),
    ("최대 은행인 앵글로 아이리시가 지난해 일 월 국유화됐고, 지난 구 월에는 이 위 은행 얼라이드 아이리시가 뒤를 따랐다.", "The largest bank, Anglo Irish, was nationalized in January last year, and in September the second-ranked bank, Allied Irish, followed."),
    ("거품 투자의 부산물인 빈집이 삼십만 채에 이른다.", "Empty houses, a by-product of bubble investment, number 300,000."),
    ("뉴욕 타임스는 지난해 육만 오천 명이 떠난 데 이어 올해에는 십이만 명이 이민 행렬에 오를 것으로 예상된다고 보도했다.", "The New York Times reported that, following 65,000 who left last year, 120,000 are expected to join the line of emigrants this year."),
    ("광산 개발로 건설 일자리가 많은 오스트레일리아 등이 경제 난민을 맞고 있다.", "Countries such as Australia, with many construction jobs because of mine development, are receiving “economic refugees.”"),
    ("브라이언 카우언 총리는 구제금융 수용 방침을 밝히면서 다시 한번 회복하고 번영할 수 있는 우리의 능력을 믿어야 한다며 훗날을 기약하자는 메시지를 내놨다.", "Prime Minister Brian Cowen, announcing the policy of accepting the bailout, put out a message promising a later day, saying that we must believe in our ability to recover and prosper once again."),
]
_SPEAK5B = [("미국의 현재 경제 상황에 대해서 아는 것이 있으면 이야기해 보세요.", "If you know anything about the current economic situation of the United States, talk about it."), ("미국의 주정부들이 재정적자를 줄일 수 있는 방법에 대해 친구와 이야기해 보세요.", "Talk with a friend about ways in which US state governments can reduce fiscal deficits.")]
L4 = lesson(
    "U18 L5 · Part 2 (본 학습): Ireland, from the Celtic tiger to the bailout",
    "본 학습 · 아일랜드 · 감자 대기근 · 켈틱 호랑이 · 부동산 거품 · 은행 부실 · 구제금융 · 이민 행렬 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: an article on Ireland (Hankyoreh)", "The book asks four questions: to summarize in English Ireland’s economic conditions before the 1990s and in the 1990s; what caused its economy to collapse; why the writer added the underlined sentences (the choices are A. to show examples opposing the previous content; B. to summarize what was written before; C. to make new points with a topic transition; D. to provide specific examples of the previous content); and how the present condition affects the lives of Irish people. The numbers are spelled in Hangul, 국내총생산 with the abbreviation GDP as 지디피, 켈틱 (켈트족) as “켈틱, 즉 켈트족”, the “•” in 경제•경영 as 와. The article, with my English:", examples=passage(_IRE5)),
        card("My answers to 학습활동 3", "1. Before the 1990s: a former British colony long called the poorest country in Western Europe, hit in the mid-19th century by the potato famine in which a million of 6.5 million died and a million emigrated, and later by bad harvests and slumps that kept people emigrating. In the 1990s: astonishing growth thanks to investment attraction and Western European capital, earning the name “Celtic tiger”; emigrants returned, Eastern European workers came, and income surpassed Britain’s. 2. A real estate bubble fed by low interest rates and money borrowed abroad burst in 2008, and the financial crisis left banks with bad loans; the resulting fiscal deficit forced the government to accept a bailout. 3. The underlined sentences are not marked in the text, so I cannot tell which they are; I would guess D if they are examples (the nationalized banks and the empty houses give specifics of the collapse). 4. Many Irish people are emigrating again (65,000 last year, 120,000 expected this year, for example to Australia), and 300,000 houses stand empty."),
        card("말해 봅시다! (speaking)", "The book’s two prompts (the English is mine):", examples=passage(_SPEAK5B)),
        card("Activities left out", "학습활동 1 (Listening, Reading, track 002): a YTN video on Greece: you write what message the reporter tried to convey by interviewing people at a market, two statistics about Greece’s economy and, from the Korean subtitles of the professor’s interview, what Greece’s biggest problem is. 학습활동 2 (Listening, track 003): a YTN news item on Ireland, which you summarize. They are video and audio."),
    ],
    exercises=uniq(
        _tr(_IRE5, k=3) + _tr(_SPEAK5B, k=2)
        + [M("What was long said of Ireland’s wealth?", "It was the poorest country in Western Europe", ["It was the richest in Europe", "It had no banks", "It was a great empire"], "서유럽 최빈국."), M("What happened in the Irish potato famine?", "A million people starved to death", ["Potatoes became too expensive to export", "The government fell", "Ireland joined a war"], "감자 대기근."), M("What nickname did Ireland earn in the 1990s?", "The Celtic tiger", ["The Irish bear", "The green dragon", "The island eagle"], "켈틱 호랑이."), M("What were the main culprits of Ireland’s collapse?", "The real estate bubble and bank insolvency", ["Floods and war", "A potato blight", "Low exports and a strong currency"], "부동산 거품과 은행 부실."), M("How many empty houses are there?", "300,000", ["30,000", "650,000", "120,000"], "삼십만 채."), M("Where do many Irish emigrants go, according to the article?", "Places such as Australia", ["Germany", "Spain", "Japan"], "오스트레일리아.")]
        + [F("정부가 마침내 ___를 든 것이다. (to surrender)", "백기", ["의회", "자본"], "백기를 들다."), F("부동산 ___가 꺼지며 이민 행렬이 이어졌다. (a bubble)", "거품", ["신화", "자본"], "거품."), F("최대 은행이 지난해 일 월 ___화됐다. (nationalization)", "국유", ["민영", "사유"], "국유화."), F("감자가 마름병으로 수확량이 ___했다. (to drop sharply)", "급감", ["급등", "급락"], "급감하다.")]
        + [read_q("영국의 식민 지배를 받았던 섬나라 아일랜드는 서유럽 최빈국으로 불렸다"), read_q("부동산 거품과 은행 부실이 아일랜드의 처지를 급반전시켰다"), read_q("아일랜드 정부는 구제금융 수용을 선언했다"), read_q("미국의 현재 경제 상황에 대해서 이야기해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("강도", "(强度) (the degree of) strength; solidity; intensity", "해병대는 아주 강도 높은 훈련을 받습니다."),
        ("경기", "(景氣) economic condition", "올 연말부터 경기가 다시 살아날 것이라는 전망이다.", "불경기, 호황, 불황"),
        ("긴축", "(緊縮) belt-tightening; (management of) retrenchment", "각 주정부들이 재정적자를 줄이기 위해 긴축정책을 실시하려고 한다.", "긴축정책, 긴축예산, 긴축재정"),
        ("돌다", "to circulate; to spin", "돈이 잘 돌아야 경제가 살아납니다."),
        ("사회보장제도", "(社會保障制度) a social security system", ""),
        ("시위(하다)", "(示威) demonstration; protest (to demonstrate; to protest)", "서울역 광장 앞에 모인 시위대들이 늘어나고 있습니다.", "데모하다"),
        ("유럽공동체", "(共同體) European Community; EC", "", "유럽연합"),
        ("재래시장", "(在來市場) a traditional market; an open-air market", "재래시장에 가면 훨씬 싸게 물건을 살 수 있습니다."),
        ("주머니 사정이 나쁘다", "to not have enough money; to have financial difficulties; “pocket condition is bad”", "요즘 주머니 사정이 나빠 점심 때에는 싼 식당을 찾아 다닌다."),
        ("항의(하다)", "(抗議) a protest (to protest)", "국가의 연금정책에 항의하는 시위가 열리고 있습니다."),
    ]),
    ("학습활동 2", [
        ("공공지출", "(公共支出) public expenditure; public spending", "정부는 공공지출을 늘려 경기를 부양하겠다고 했습니다."),
        ("공동성명", "(共同聲明) a joint statement", "이 문제에 대해 여야 대표가 공동성명을 발표했습니다."),
        ("늘리다", "to increase; to extend", "저는 한국어 어휘력을 늘리기 위해 매일 한국 책을 읽습니다.", "줄이다, 축소하다"),
        ("백기를 들다", "(白旗) to surrender; “to raise the white flag”", "이제 백기를 들고 제 뜻을 따라 주세요."),
        ("세금", "(稅金) tax", "정부는 부자들에 대해 세금을 더 걷겠다고 했습니다."),
        ("승인(하다/되다)", "(承認) approval (to give one’s approval/to be approved)", "금년도 예산안이 국회의 승인을 받았습니다."),
        ("예고(하다/되다)", "(豫告) an advance notice; a notice (to give [advance] notice/to be noticed in advance)", "이 선생님은 예고 없이 시험을 봅니다."),
        ("유럽연합", "(聯合) European Union (EU)", "", "유럽공동체"),
        ("축소(하다/되다)", "(縮小) reduction; cut; downsizing (to reduce; to cut; to downsize/to be reduced; to be cut; to be downsized)", "기업은 내년도 신규채용 규모를 축소하겠다고 했습니다.", "늘리다, 확대하다"),
    ]),
    ("학습활동 3", [
        ("거품", "bubble; foam", "주택 시장의 거품이 빠지며 주택 가격이 급락하고 있습니다."),
        ("광산", "(鑛山) a mine; “mineral mountain”", "이 광산에서는 금이 많이 나옵니다.", "광업, 광부"),
        ("국유화(하다/되다)", "(國有化) nationalization (to nationalize/to be nationalized)", "정부는 이 일대 토지를 국유화하겠다고 발표했습니다.", "민영화하다, 사유화하다"),
        ("굶어 죽다", "to die of hunger", "아프리카에는 굶어 죽는 아이들이 많습니다.", "아사하다 / 기근, 기아"),
        ("귀국길에 오르다", "(歸國) to take a trip/journey back to one’s homeland; to start on one’s journey home", "김수연 씨는 삼 년 간의 망명 생활을 끝내고 오늘 귀국길에 오릅니다."),
        ("기근", "(饑饉) famine", "몇 달째 가뭄이 계속되더니 이제 기근이 이어지고 있습니다."),
        ("덮치다", "to raid; to attack", "경찰이 범인을 뒤에서 덮쳐 잡았다."),
        ("마름병", "blight; “drying disease”", ""),
        ("막을 내리다", "to end; to be over; “to lower the curtain”", "부산영화제가 어제 막을 내렸습니다."),
        ("맞다", "to greet; to welcome; to receive", "손님을 맞을 준비를 하느라고 다들 바쁘다."),
        ("붕괴(하다/되다)", "(崩壞) collapse (to collapse)", "주식시장의 붕괴가 금융시장의 혼란을 가져왔습니다."),
        ("살 길을 찾다", "to seek/find a way to make a living; “to look for a way to live”", "이제 더 이상 도와줄 수 없으니 각자 살 길을 찾으세요."),
        ("수용(하다/되다)", "(受容) acceptance; embrace (to accept; to embrace/to be accepted)", "북한이 남한 측의 제안을 수용하면 다시 남북관계가 열릴 수 있을 것이다.", "받아들이다"),
        ("신화", "(神話) a mythology; a legend; “god story”", "그 사람은 이 분야에서 성공 신화를 이루었습니다."),
        ("앞지르다", "to pass; to surpass; to outdo", "뒤에서 달리던 선수가 다섯 명의 선수들을 앞질러 일 등을 했다.", "뒤쳐지다"),
        ("자본", "(資本) capital", "사업을 시작하려는데 자본금이 부족합니다."),
        ("주식", "(主食) staple food; staple diet", "한국인들의 주식은 밥입니다.", "간식"),
        ("최빈국", "(最貧國) the poorest country", "국제사회는 최빈국들을 돕기 위해 자금을 마련한다고 합니다.", "최부국"),
        ("합작(하다)", "(合作) collaboration; joint venture; joint production (to collaborate; to work together)", "이 영화는 한국과 미국이 합작한 것이다.", "합작회사"),
        ("흉년", "(凶年) a bad year; a year of poor harvest; a year of famine; “unlucky year”", "올해는 흉년이 들어서 쌀값이 비쌉니다.", "풍년"),
    ]),
]
L5 = lesson(
    "U18 L5 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 강도 · 경기 · 긴축 · 시위 · 재래시장 · 주머니 사정 · 항의 · 공공지출 · 공동성명 · 백기를 들다 · 세금 · 승인 · 예고 · 유럽연합 · 축소 · 거품 · 광산 · 국유화 · 굶어 죽다 · 귀국길 · 기근 · 마름병 · 막을 내리다 · 붕괴 · 수용 · 신화 · 앞지르다 · 자본 · 주식 · 최빈국 · 합작 · 흉년",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives homonyms: 강도 (强盜), “a robber”; and 주식 (株式), “stock, share”, beside 주식 (主食), the staple food. 유럽연합 is printed with the Hanja 聯合 only. The book lists 앞지르다’s counterpart as 뒤쳐지다 (printed with this spelling; the standard spelling is 뒤처지다). The example of 앞지르다 has 1등, and the example of 귀국길에 오르다 has 3년, in digits; I spelled them out (일 등, 삼 년). In 막을 내리다 the book writes “(~이/가) 막을 내리다”, which I wrote without the particle marker. 주식 lists 간식 (a snack) as its counterpart; 최빈국 lists 최부국 (the richest country). 굶어 죽다 lists 아사하다 as similar and 기근, 기아 as related.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=22, nread=18)),
)

# ================================================================== L6 Part 3
_FDR5 = [
    ("어제의 오늘, 천구백사십 년 프랭클린 루스벨트, 미국 최초 대통령 삼 선", "Today in yesterday: Franklin Roosevelt in 1940, the first US president elected to a third term"),
    ("미국의 삼십이 대 대통령.", "The 32nd president of the United States."),
    ("임기 중 대공황과 제이 차 세계대전을 경험하며 이십 세기 격변의 역사 한 가운데 서 있었던 인물이기도 하다.", "He is also a figure who experienced the Great Depression and the Second World War during his term and stood in the middle of the upheaval of 20th-century history."),
    ("미국 대통령 중에서 처음이자 마지막으로 네 번이나 대통령직에 당선돼 십이 년간 백악관을 지켰다.", "Elected to the presidency four times, the first and last among US presidents, he kept the White House for twelve years."),
    ("천구백삼십 년대 미국을 휩쓴 대공황을 극복하기 위한 그의 뉴딜정책은 이천팔 년 세계를 강타한 미국발 금융위기로 세기를 뛰어넘어 오늘날 다시금 주목받고 있다.", "His New Deal policy for overcoming the Great Depression that swept America in the 1930s is attracting attention again today, across the century, because of the financial crisis originating in the US that hit the world in 2008."),
    ("천구백이십일 년 삼십구 세의 나이에 찾아온 소아마비를 극복하고 정계에 복귀한 그는 두 차례에 걸친 뉴욕 주지사 업무를 성공적으로 마친 뒤 천구백삼십이 년 민주당 대통령 후보로 지명됐다.", "Having overcome polio that struck him in 1921 at the age of 39 and returned to politics, he successfully finished two terms of work as governor of New York and was nominated as the Democratic presidential candidate in 1932."),
    ("천구백이십구 년 갑자기 몰아닥친 대공황으로 수많은 실업자들이 거리로 쏟아지던 당시 미국 국민들은 뉴딜정책을 공약으로 내건 그를 압도적 지지로 대통령에 당선시켰다.", "At that time, when countless unemployed people poured into the streets because of the Great Depression that suddenly hit in 1929, the American people elected him president with overwhelming support, as he had put the New Deal policy forward as his pledge."),
    ("뉴딜정책은 테네시강 개발과 같은 대규모 공공사업과 각종 경제 개혁 정책을 통해 실업문제를 해결하고 경기를 부양하기 위한 적극적인 정부 개입 정책으로 그의 취임 후 미국 경제는 파국을 벗어나 조금씩 안정돼 갔다.", "The New Deal was an active government-intervention policy to solve the unemployment problem and boost the economy through large-scale public works such as the development of the Tennessee River and various economic reform policies, and after his inauguration the American economy escaped catastrophe and gradually stabilized."),
    ("이 과정에서 루스벨트 대통령은 천구백삼십삼 년부터 사십사 년까지 모두 삼십 차례에 걸쳐 라디오방송에 출연해 뉴딜정책을 비롯한 정부 정책을 설명하고 대공황으로 실의에 빠진 국민들의 동의를 구했다.", "In this process, President Roosevelt appeared on radio broadcasts a total of 30 times from 1933 to 1944 to explain government policies, beginning with the New Deal, and to seek the consent of a people fallen into despondency because of the Great Depression."),
    ("마침내 루스벨트 대통령은 천구백삼십육 년 재선을 거쳐 사십 년 십일 월 오 일 삼 선에 성공했다.", "At last President Roosevelt, after being re-elected in 1936, succeeded in winning a third term on November 5, 1940."),
    ("하지만 미국의 대공황은 생각보다 오래 지속됐고 미국이 천구백사십일 년 제이 차 세계대전에 참전할 때까지도 미국 경제가 완벽한 회복 국면으로 접어들지는 못한 상태였다.", "But the American Great Depression lasted longer than expected, and even until the United States joined the Second World War in 1941, the American economy had not entered a phase of complete recovery."),
    ("제이 차 세계대전에 의한 군수산업 호황이 없었다면 루스벨트의 뉴딜정책도 큰 효과를 발휘할 수 없었을 것이란 분석이 일각에서 제기되는 배경이다.", "This is the background to the analysis raised in some quarters that, without the armaments-industry boom caused by the Second World War, Roosevelt’s New Deal too could not have shown a great effect."),
]
_SPEAK5C = [("경제 위기 속에서 가정 또는 개인의 경제를 지키기 위한 방법은 무엇인지 옆 사람과 이야기해 보세요.", "Talk with the person next to you about what ways there are to protect the economy of a family or an individual in an economic crisis.")]
L6 = lesson(
    "U18 L5 · Part 3 (심화 학습): Roosevelt and the New Deal",
    "심화 학습 · 루스벨트 · 뉴딜정책 · 대공황 · 삼 선 · 공공사업 · 정부 개입 · 군수산업 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: an article on President Roosevelt (Kyunghyang)", "The book asks four questions in English: to translate the underlined phrase of the first paragraph and say why Roosevelt is described in this way; why he is receiving attention now; what the New Deal was; and whether it solved the economic problems. The headline is “[어제의 오늘] 1940년 프랭클린 루스벨트, 미국 최초 대통령 3선”; the numbers are spelled in Hangul and the brackets of the heading are dropped. The article, with my English:", examples=passage(_FDR5)),
        card("My answers to 학습활동 2", "1. The underline is not marked in the text; I take it to be 역사 한 가운데 서 있었던 인물, “a figure who stood in the middle of history”, because he lived through the Great Depression and the Second World War. 2. His New Deal against the Great Depression is attracting renewed attention because of the 2008 financial crisis that began in the United States. 3. The New Deal was an active policy of government intervention to solve unemployment and boost the economy through large public works such as the development of the Tennessee River and various economic reform policies. 4. Only partly: the economy stabilized little by little, but the Depression lasted longer than expected and full recovery had not come even when the US entered the war in 1941; some argue that without the armaments boom of the Second World War the New Deal could not have had a great effect."),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine):", examples=passage(_SPEAK5C)),
        card("Activities left out", "학습활동 1 (Listening, tracks 004–006): a KBS report on the world economy: you summarize the economic conditions of Europe, Japan and China, check your answers by watching the video and summarize the question and answer of a second report. 학습활동 3 (Listening, track 007): a Donga commentary on small but strong European countries: you fill in blanks about a survey of the Swiss institute for management development (Denmark ranked top in one area; first in the reaction of two groups to crises; eighth in another area) and choose what we need to learn from these countries (A. make laws to protect foreign investors; B. provide aid to high-tech venture companies; C. regulate speculative investment of foreign capital; D. open markets and reform their regulations). They are audio."),
    ],
    exercises=uniq(
        _tr(_FDR5, k=3)
        + [M("How many times was Roosevelt elected president?", "Four times", ["Twice", "Three times", "Five times"], "네 번."), M("Which policy did Roosevelt put forward as his pledge?", "The New Deal", ["The Fair Deal", "The Great Society", "The Marshall Plan"], "뉴딜정책."), M("What did the New Deal include?", "Large-scale public works and economic reform", ["Tax cuts and deregulation", "War spending only", "Closing banks"], "공공사업과 개혁 정책."), M("How often did Roosevelt appear on radio to explain policies?", "30 times", ["3 times", "300 times", "Once a year"], "삼십 차례."), M("Why is Roosevelt receiving attention again today?", "Because of the 2008 financial crisis", ["Because of a new election", "Because of an anniversary of the war", "Because of a book"], "이천팔 년 금융위기."), M("What did some analysts say about the New Deal’s effect?", "It needed the armaments boom of the war to be effective", ["It solved everything by 1936", "It made the Depression worse", "It was never carried out"], "군수산업 호황.")]
        + [F("루스벨트의 ___정책은 대공황을 극복하기 위한 것이었다. (New Deal)", "뉴딜", ["공공", "긴축"], "뉴딜정책."), F("대규모 ___사업을 통해 실업문제를 해결했다. (public works)", "공공", ["군수", "민간"], "공공사업."), F("정부 ___ 정책으로 경기를 부양했다. (intervention)", "개입", ["개혁", "대응"], "정부 개입."), F("군수산업 ___이 없었다면 효과가 크지 않았을 것이다. (a boom)", "호황", ["불황", "붕괴"], "호황.")]
        + [read_q("루스벨트는 미국의 삼십이 대 대통령이다"), read_q("뉴딜정책은 대공황을 극복하기 위한 정책이었다"), read_q("루스벨트 대통령은 삼 선에 성공했다"), read_q("경제 위기 속에서 가정의 경제를 지키는 방법을 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("거인", "(巨人) a giant; “large man”", "그 사람은 아이티업계의 거인입니다."),
        ("거침(이) 없다", "to be unhindered; to be free from impediment; to be without hesitation", "그 사람은 항상 거침없이 하고 싶은 말을 다 합니다."),
        ("구원투수", "(救援投手) a relief pitcher", "우리가 어렵던 시기에 그 사람이 구원투수 역할을 해 주었습니다."),
        ("치명타(를 입다)", "(致命打) a fatal blow; a mortal blow; a serious blow (to receive a fatal blow)", "그 영화배우는 스캔들 때문에 인기에 치명타를 입었다."),
        ("한 치 앞이 어둡다", "(idiom) even what will happen in the very near future is unclear; “one inch ahead is dark”", ""),
        ("횡보세", "(橫步勢) flat market trend; “sidling along trend”", "현재 주식시장은 횡보세를 이어가고 있습니다."),
        ("힘을 얻다", "to be encouraged; to gain courage; to be emboldened; “to gain strength”", "주식시장은 구제금융에 힘을 얻어 상승세로 돌아섰습니다."),
    ]),
    ("학습활동 2", [
        ("강타(하다)", "(强打) a heavy blow; a hard hit (to hit hard)", "태풍이 전라도 지역을 강타했습니다."),
        ("개입(하다/되다)", "(介入) intervention (to intervene/to be intervened; to be involved)", "이번 사건에 몇몇 정치인이 개입되어 있다."),
        ("개혁(하다)", "(改革) reform; reformation (to reform)", "현재 정치권에 개혁의 바람이 불고 있습니다."),
        ("공공사업", "(公共事業) a public undertaking; public works", "정부는 공공사업에 자금을 더 투입하기로 했습니다."),
        ("군수산업", "(軍需産業) war industry; the armaments industry", "세계의 군수산업을 이끌고 있는 나라는 미국입니다."),
        ("발휘하다", "(發揮) display (of one’s talent or ability); exhibition (to display [one’s ability])", "이번 프로젝트에서 여러분의 능력을 마음껏 발휘해 보세요."),
        ("부양(하다)", "(扶養) support (to support; to provide for)", "저는 혼자 벌어서 여섯 식구를 부양해야 합니다."),
        ("완벽(하다)", "(完璧) perfection (to be perfect)", "그 사람은 불어를 완벽하게 구사합니다."),
        ("일각에서 제기되다", "(一角 提起) (issue, question, etc.) to be brought up by some people; to be raised by some people; “(something) is brought up from one angle”", "김 씨의 사망에 대해 타살 가능성이 일각에서 제기되고 있다."),
        ("호황", "(好況) an economic boom", "요즘 아이티산업이 호황입니다.", "불황, 불경기"),
    ]),
    ("학습활동 3", [
        ("겁내다", "to fear; to be scared of", "아이가 겁을 내며 울고 있어요."),
        ("규제(하다)", "(規制) regulation; control; restriction (to regulate; to control)", "정부는 이번에 개발된 신약의 사용을 규제하고 있습니다."),
        ("대응(하다)", "(對應) action; maneuver (to deal with; to respond to; to take action against)", "운전자의 신속한 대응이 사고를 막았습니다."),
        ("소극적", "(消極的) passive; half-hearted", "저는 소극적이어서 친구가 많지 않습니다.", "적극적"),
        ("슬기롭다", "to be wise; to be sensible", "우리 어머니는 어려운 일이 있을 때마다 슬기롭게 잘 대처하셨습니다."),
        ("제약", "(制約) a restriction (on); a limitation (on)", "외국인이 국내에 투자할 때는 제약이 있다."),
        ("충격", "(衝擊) an impact; a shock", "저는 처음에 미국에 와서 문화적 충격을 받았습니다."),
        ("혁신", "(革新) innovation", "이 제품의 컨셉은 혁신입니다."),
    ]),
]
L7 = lesson(
    "U18 L5 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 거인 · 거침없다 · 구원투수 · 치명타 · 횡보세 · 힘을 얻다 · 강타 · 개입 · 개혁 · 공공사업 · 군수산업 · 발휘 · 부양 · 완벽 · 일각에서 제기되다 · 호황 · 겁내다 · 규제 · 대응 · 소극적 · 슬기롭다 · 제약 · 충격 · 혁신",
    requires=[],
    cards=[card("A note on the Korean in this list", "부양 has a homonym 부양 (浮揚), “floating”, in the book (my remark, not the book’s: 경기를 부양하다, “to boost the economy”, in the lesson text uses the 浮揚 meaning). The examples had “IT” in the book (IT업계, IT산업), which I spelled 아이티. 한 치 앞이 어둡다 has no example. 일각에서 제기되다 is printed as two entries’ worth of Hanja (一角, 提起); I joined them in one set of parentheses. 소극적 lists 적극적 as its opposite and 호황 lists 불황, 불경기. 혁신’s example is printed with the word 컨셉 (concept) as in the book.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=18, nread=15)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 5: The World Financial Crisis and Recession (금융위기와 경기침체)", [L1, L2, L3, L4, L5, L6, L7])
