"""Unit 89: KBC Semester III, Unit 18, Lesson 4 - Trade (무역).
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
_MATCH4 = [("투자", "investment", "첨단산업에 대한 투자가 필요하다"), ("무역수지", "trade balance", "상반기 무역수지가 적자를 기록했다"), ("수요", "demand", "가전제품의 수요가 급증하고 있다"), ("원자재", "raw materials", "원자재 가격의 상승으로 가격이 오르고 있다"), ("적자", "deficit; loss", "적자가 계속되자 회사는 결국 폐업했다"), ("호황", "economic boom", "반도체 시장이 호황이다"), ("수출", "export", "남미 시장에 자동차 수출이 증가하고 있다"), ("강세", "a bullish tendency; a strong tone", "달러의 강세가 계속되고 있다")]
_HJ4 = [("輸 수", "transport", "수송, 수입"), ("易 역", "trade", "무역, 교역"), ("稅 세", "tax", "면세, 관세"), ("換 환", "exchange", "교환, 환율"), ("資 자", "property; asset", "투자, 자원")]
_HJW4 = [("수송", "transportation"), ("수입", "import; “transport in”"), ("무역", "trade"), ("교역", "trade (between nations)"), ("면세", "duty-free"), ("관세", "customs duties"), ("교환", "exchange"), ("환율", "exchange rate"), ("투자", "investment"), ("자원", "a resource")]
_SIM4 = [("무역", "교역", "trade: trade between nations"), ("수송", "운송", "transportation: carriage")]
_OPP4 = [("수입", "수출", "import: export"), ("면세", "과세", "duty-free: taxation")]
_L4X = [("첨단산업", "a high-tech industry"), ("상반기", "the first half of a year"), ("가전제품", "a home appliance"), ("폐업", "closing a business"), ("반도체", "a semiconductor"), ("남미", "South America"), ("소포", "a parcel"), ("차량", "a vehicle"), ("화물", "cargo"), ("출입", "going in and out"), ("출구", "an exit"), ("반출", "carrying out"), ("과세", "taxation"), ("면제", "exemption"), ("세금", "a tax"), ("운송", "carriage; shipping")]
L1 = lesson(
    "U18 L4 · Review: trade words and Sino-Korean 輸 易 稅 換 資",
    "무역 · 단어 복습 · 한자어 복습 · 투자 · 무역수지 · 수요 · 원자재 · 적자 · 호황 · 수출 · 강세 · 輸 易 稅 換 資",
    requires=[],
    cards=[
        card("단어 복습 1: connect the underlined word with its English meaning", "The book gives eight sentences with a word underlined and eight English meanings. The underline is not marked in the text; the pairs below are my reading (the second sentence contains both 무역수지 and 적자, and the fifth sentence 적자 again, so I took 무역수지 for the second):", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH4], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ4], say=[2]), ktable(_HJW4)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "Circle the word closest in meaning to the word on the left (A. 무역: 수출, 수입, 교역, 투자; B. 수송: 소포, 운송, 차량, 화물).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM4], say=[0, 1])]),
        card("한자어 복습 2: the word with the opposite meaning (my answers)", "Circle the word opposite in meaning to the word on the left (A. 수입: 출입, 출구, 수출, 반출; B. 면세: 관세, 과세, 면제, 세금).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP4], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L4X)]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001–003): three radio news items on Korea’s imports and exports, for each of which you mark 흑자 (surplus) or 적자 (deficit) for the trade balance and write in English which export or import item it concerns. It is audio."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH4], k=3) + _tr(_HJW4, k=3) + _tr(_L4X, k=4)
        + [M("What does the syllable 輸 (수) mean?", "transport", ["trade", "tax", "exchange"], "수송."), M("What does the syllable 易 (역) mean?", "trade", ["transport", "tax", "property"], "무역."), M("What does the syllable 稅 (세) mean?", "tax", ["transport", "trade", "exchange"], "관세."), M("What does the syllable 換 (환) mean?", "exchange", ["tax", "property", "transport"], "환율."), M("What does the syllable 資 (자) mean?", "property; asset", ["exchange", "tax", "trade"], "자원.")
           , M("Which word is similar to 무역?", "교역", ["수출", "수입", "투자"], "Trade."), M("Which word is similar to 수송?", "운송", ["소포", "차량", "화물"], "Carriage."), M("Which word is the opposite of 수입?", "수출", ["출입", "출구", "반출"], "Export."), M("Which word is the opposite of 면세?", "과세", ["관세", "면제", "세금"], "Taxation.")
           , F("첨단산업에 대한 ___가 필요하다. (investment)", "투자", ["수요", "적자"], "투자."), F("가전제품의 ___가 급증하고 있다. (demand)", "수요", ["투자", "호황"], "수요."), F("반도체 시장이 ___이다. (a boom)", "호황", ["적자", "강세"], "호황."), F("달러의 ___가 계속되고 있다. (a strong tone)", "강세", ["호황", "수출"], "강세."), F("원___ 가격의 상승으로 가격이 오르고 있다. (raw materials)", "자재", ["자원", "투자"], "원자재.")]
        + [read_q("첨단산업에 대한 투자가 필요하다"), read_q("상반기 무역수지가 적자를 기록했다"), read_q("남미 시장에 자동차 수출이 증가하고 있다"), read_q("달러의 강세가 계속되고 있다")]
    ),
)

# ================================================================== L2 Part 1
_PERU = [
    ("한국이 페루와 자유무역협정, 에프티에이 체결에 가서명했다.", "Korea initialed the conclusion of a free trade agreement (FTA) with Peru."),
    ("이로써 한국은 여덟 번째 에프티에이를 체결하게 됐고 체결대상국도 사십오 개국으로 늘었다.", "With this, Korea will conclude its eighth FTA, and the number of countries concerned has grown to 45."),
    ("정부는 한국과 페루 간 에프티에이가 이행되면 페루의 에너지와 자원, 자동차, 티브이 등 부문에서 새 시장을 확보할 수 있을 것으로 설명했다.", "The government explained that once the Korea-Peru FTA is implemented, it will be able to secure new markets in sectors such as Peru’s energy and resources, cars and TVs."),
    ("다만 오징어 등 농수산물 등의 분야는 시장개방으로 인한 어려움이 예상된다.", "However, difficulties from the opening of the market are expected in fields such as agricultural and marine products, including squid."),
    ("한국과 페루 에프티에이에 따르면 협정 발효 뒤 십 년 이내 모든 공산품의 관세가 철폐된다.", "According to the Korea-Peru FTA, the customs duties on all manufactured goods will be abolished within ten years after the agreement takes effect."),
    ("페루로 수출되는 삼천 시시 이상 대형차와 티브이의 관세, 구 퍼센트는 발효 뒤 즉시 철폐되며, 천오백 시시에서 삼천 시시 중형차에 대한 관세는 오 년 내, 기타 승용차는 십 년 내에 관세가 단계적으로 철폐된다.", "The 9 percent duties on large cars of 3,000 cc or more and TVs exported to Peru will be abolished immediately after it takes effect, while the duties on medium-sized cars of 1,500 to 3,000 cc will be abolished in stages within five years and those on other passenger cars within ten years."),
    ("이번 협정은 한국이 그 동안 체결한 에프티에이 중 처음으로 에너지와 자원협력을 명문화했다.", "This agreement, for the first time among the FTAs Korea has concluded so far, stipulates energy and resource cooperation."),
    ("원유, 가스 및 광물자원 탐사, 개발, 생산 분야에서 양국 간 협력활동의 개발과 촉진을 규정했다.", "It stipulates the development and promotion of cooperative activities between the two countries in the exploration, development and production of crude oil, gas and mineral resources."),
    ("중남미의 자원부국인 페루는 은 일 위, 아연 이 위, 구리와 주석 삼 위 등 광물자원이 매장량 기준으로 세계 삼 위 이내이며, 석유와 가스 매장량도 각각 삼십팔 위, 사십이 위이다.", "Peru, a resource-rich country of Latin America, is within the top three in the world by reserves of mineral resources, such as silver (first), zinc (second) and copper and tin (third), and its oil and gas reserves rank 38th and 42nd respectively."),
    ("농수산물의 경우 우리 측의 민감한 품목인 쌀, 쇠고기, 분유, 고추, 마늘, 양파, 사과, 배, 감귤, 명태, 민어 등 백칠 개는 양허 대상에서 제외되거나 현행 관세를 유지키로 했다.", "As for agricultural and marine products, 107 items, including our side’s sensitive ones such as rice, beef, powdered milk, red pepper, garlic, onions, apples, pears, tangerines, pollock and croaker, were excluded from the concession targets or will keep the current duties."),
    ("농림수산식품부 측은 피해가 우려되는 수산업 분야 경쟁력 제고를 위한 대책을 마련 중이라며 특히 피해가 예상되는 오징어를 중심으로 지속적으로 보완대책을 강구하고 있다고 밝혔다.", "The Ministry for Food, Agriculture, Forestry and Fisheries said that it is preparing measures to boost the competitiveness of the fisheries field where damage is feared and, centering on squid in particular, where damage is expected, is continuously working out supplementary measures."),
    ("페루, 칠레 등의 남미국가들은 미국과 에프티에이를 체결했으며 친미국가로 분류된다.", "South American countries such as Peru and Chile have concluded FTAs with the United States and are classified as pro-American countries."),
]
_SPEAK4 = [("한국의 주요 수출품에 대해서 아는 것을 말해 보세요.", "Say what you know about Korea’s main exports."), ("직접 사용해 본 경험이 있으면 어땠는지 이야기해 보세요.", "If you have used them yourself, tell how it was."), ("미국의 주요 수출 품목과 수입 품목에 대해 이야기해 보세요.", "Talk about the main export and import items of the United States."), ("환율이 변동하면 어떤 영향이 있는지 이야기해 보세요.", "Talk about what effects there are when the exchange rate fluctuates."), ("개인 여행자와 수출입업자를 예를 들어 이야기해 보세요.", "Use an individual traveler and an exporter-importer as examples.")]
L2 = lesson(
    "U18 L4 · Part 1 (도입 학습): the Korea-Peru free trade agreement",
    "도입 학습 · 자유무역협정 · 에프티에이 · 가서명 · 관세 철폐 · 공산품 · 광물자원 · 매장량 · 농수산물 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: a newspaper article on the Korea-Peru FTA (Hankyoreh and Kyunghyang)", "The book asks you to mark six statements true (T) or false (F) after the article. The article’s numbers and abbreviations are spelled in Hangul (FTA as 에프티에이, TV as 티브이, 3000 cc as 삼천 시시); “한·페루” is written 한국과 페루, “에너지·자원” 에너지와 자원, and the quotation marks of the ministry’s words are dropped. The article, with my English:", examples=passage(_PERU)),
        card("My answers to the six statements", "A. Peru is the eighth country to engage in an FTA with Korea: T (it is Korea’s eighth FTA). B. The article discusses Korea’s first FTA under which Peru and Korea will cooperate to develop energy and natural resources: T. C. When the FTA goes into effect, Korea and Peru will abolish customs duties on manufactured goods within 10 years: T. D. Goods used for agriculture and fishing will have the same customs duties as before: F (only 107 sensitive items are excluded or keep their current duties, and the book’s “goods used for” is not what the article says). E. Korean squid fishermen will welcome the FTA the most: F (damage to squid is expected). F. Peru and Chile support the United States and the three countries will sign the FTA soon: F (they have already concluded FTAs with the United States)."),
        card("말해 봅시다! (speaking)", "The book’s three prompts, which I split into five sentences (the English is mine):", examples=passage(_SPEAK4)),
        card("Activities left out", "학습활동 1: two pictures (edunet4u.net) of Korea’s main exports and imports, which you describe to a friend. They are pictures. 학습활동 2 (Listening, track 004): a conversation between the trade ministry representatives of two countries (edunet4u.net): you choose its main topic (A. the imbalance of resources; B. the mutual benefits of trade; C. the necessity of removing trade barriers; D. the importance of technology and human resources) and fill a table with each country’s advantages and disadvantages in English. 학습활동 4 (Listening, track 005): a KBS video on exchange rate changes: in English, what is happening to the currency rates (with the monetary units), two causes of the change, and who will be victimized and why. They are audio."),
    ],
    exercises=uniq(
        _tr(_PERU, k=3) + _tr(_SPEAK4, k=3)
        + [M("Which number FTA is the one with Peru for Korea?", "The eighth", ["The first", "The 45th", "The tenth"], "여덟 번째."), M("How many countries are Korea’s FTA partners now, according to the article?", "45", ["8", "107", "10"], "사십오 개국."), M("Within how many years will duties on all manufactured goods be abolished?", "Ten years", ["Five years", "One year", "Thirty years"], "십 년 이내."), M("What does the agreement stipulate for the first time among Korea’s FTAs?", "Energy and resource cooperation", ["Labor rights", "Tourism", "Rice imports"], "에너지와 자원협력."), M("Which Peruvian mineral ranks first in the world by reserves?", "Silver", ["Zinc", "Copper", "Tin"], "은 일 위."), M("Which fish does the ministry single out as damaged?", "Squid", ["Pollock", "Croaker", "Mackerel"], "오징어.")]
        + [F("협정 ___ 뒤 십 년 이내 모든 공산품의 관세가 철폐된다. (taking effect)", "발효", ["이행", "규정"], "발효."), F("관세가 ___적으로 철폐된다. (in stages)", "단계", ["지속", "전반"], "단계적."), F("페루의 석유와 가스 ___량도 각각 삼십팔 위, 사십이 위이다. (reserves)", "매장", ["생산", "수출"], "매장량."), F("에너지와 자원협력을 ___했다. (to stipulate)", "명문화", ["가서명", "탐사"], "명문화."), F("한국이 페루와 에프티에이 체결에 ___했다. (to initial)", "가서명", ["명문화", "철폐"], "가서명.")]
        + [read_q("한국이 페루와 자유무역협정 체결에 가서명했다"), read_q("협정 발효 뒤 십 년 이내 모든 공산품의 관세가 철폐된다"), read_q("페루는 광물자원이 매장량 기준으로 세계 삼 위 이내이다"), read_q("환율이 변동하면 어떤 영향이 있는지 이야기해 보세요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("구리", "copper", "", "동"),
        ("꽁치", "a mackerel; a pike", ""),
        ("꽃게", "a blue crab; “a flower crab”", "", "게, 대게, 왕게"),
        ("농기계", "(農機械) a farming machine; agricultural machinery", ""),
        ("명태", "(明太) a pollock (fish)", "", "동태, 황태"),
        ("석탄", "(石炭) coal; “stone charcoal”", "", "석유, 화석연료"),
        ("수산자원", "(水産資原) marine (sea) resources", "독도 근처에는 수산자원이 풍부합니다.", "해양자원, 지하자원, 광물자원"),
        ("철", "(鐵) iron; steel", "", "쇠, 강철"),
        ("풍족(하다)", "(豊足) abundance; richness (to be abundant; to be rich)", "한국의 경제가 발전하면서 생활이 풍족하게 되었습니다."),
        ("해산물", "(海産物) marine products; “sea products”", "이 식당은 해산물 요리로 유명합니다.", "수산물, 농산물, 농수산물, 공산품"),
    ]),
    ("학습활동 3", [
        ("가서명(하다)", "(假署名) initialing (an agreement, a treaty, etc.); “provisional signing” (to initialize an agreement; to sign a draft)", "이번에 가서명한 협약은 아직 대통령의 서명과 국회 동의의 절차가 남아 있다."),
        ("감귤", "(柑橘) a tangerine; a mandarin", "", "귤"),
        ("공산품", "(工産品) manufactured goods", "올해 우리나라의 공산품 생산이 줄었습니다."),
        ("광물자원", "(鑛物資源) mineral resources", "이 지방은 여러 가지 광물자원이 풍부합니다.", "광산 자원, 광산물"),
        ("규정(하다)", "(規定) regulation; ruling (to regulate; to stipulate; to prescribe)", "기숙사 규정으로 외출은 열두 시까지만 할 수 있다."),
        ("농수산물", "(農水産物) agricultural and marine products", "우리나라의 농수산물 시장을 개방하기로 했습니다."),
        ("단계적", "(段階的) phased; in stages", "해외에 주둔하고 있는 군대를 단계적으로 철수하기로 결정했다."),
        ("매장량", "(埋藏量) reserves; deposits (of natural resources); “amount of deposit”", "중동지역의 석유 매장량은 세계 일 위이다."),
        ("명문화(하다/되다)", "(明文化) stipulation; putting in a statutory form (to stipulate/to be stipulated)", "국민의 알 권리는 헌법에 명문화되어 있다.", "명시하다"),
        ("민감하다", "(敏感) to be sensitive", "나는 피부가 민감해서 알레르기가 심하다."),
        ("민어", "(民魚) a croaker (fish)", ""),
        ("발효(하다/되다)", "(發效) taking effect; coming into effect (to take effect; to come into effect/to be put into effect)", "새 법은 일 월 일 일부터 발효됩니다."),
        ("보완 대책", "(補完 對策) a supplementary measure/step", "새 법안에 부족한 점이 많습니다. 보완 대책이 절실합니다."),
        ("분유", "(粉乳) (powdered) formula; dried milk", "신생아에게는 분유보다는 모유가 더 좋습니다.", "우유"),
        ("오징어", "a squid; a cuttlefish", ""),
        ("이행(하다/되다)", "(履行) fulfillment; implementation (to fulfill; to implement/to be fulfilled; to be implemented)", "약속을 이행하지 않으면 신용이 떨어집니다.", "수행하다"),
        ("자유무역협정", "(自由貿易協定) Free Trade Agreement; FTA", "에프티에이, 즉 자유무역협정은 양자간 협정이고, 더블유티오, 즉 세계무역기구는 다자간 협상 기구이다."),
        ("제고(하다)", "(提高) boosting; enhancing (to boost; to enhance)", "기업들은 이미지를 제고하기 위해 이미지 광고를 많이 하고 있습니다."),
        ("촉진(하다/되다)", "(促進) acceleration (of the process or progress of something) (to accelerate; to expedite/to be accelerated; to be expedited)", "정부가 수출을 촉진하기 위한 정책을 발표했다."),
        ("친미", "(親美) pro-American", "중동 여러 국가의 친미정권들이 붕괴하고 있습니다.", "반미 / 친일, 반일, 친북, 반북, 친한, 반한"),
        ("탐사(하다/되다)", "(探査) exploring (for resources, space, etc.) (to explore/to be explored)", "석유를 탐사하던 중 폭발 사고가 발생했다."),
    ]),
    ("학습활동 4", [
        ("곤두박질치다", "to fall headlong; to plunge", "가격이 곤두박질치면서 제품을 생산한 업체들이 큰 손해를 봤다."),
        ("과도하다", "(過度) to be excessive", "과도한 음주는 건강을 해칠 수 있습니다.", "지나치다"),
        ("급락(하다)", "(急落) collapse; plunging; plummeting (to collapse; to plunge; to plummet)", "전쟁 소식으로 전세계 주가가 급락했다.", "폭락 / 급등, 폭등"),
        ("매물", "(賣物) an item for sale", "이 아파트는 어제 매물로 부동산 시장에 나왔다."),
        ("변동(하다)", "(變動) a change; fluctuation (to change; to fluctuate)", "환율 변동은 증권 시장에 큰 영향을 미친다.", "변화"),
        ("변수", "(變數) a variable; “changing number”", "다양한 변수들이 실험 결과에 영향을 미칠 수 있습니다."),
        ("새해 벽두", "(劈頭) the very beginning of New Year’s Day", "새해 벽두부터 물가가 폭등하고 있습니다."),
        ("약세", "(弱勢) a weakening trend; a bear market", "원화가 달러에 대해 약세를 보이고 있습니다.", "강세"),
        ("이만저만이 아니다", "to be extreme; to be extraordinary; “(It is) not to this or that extent”", "폭풍우 속을 운전하느라고 고생이 이만저만이 아니었습니다."),
        ("재개(하다/되다)", "(再開) resumption; reopening (to resume; to reopen/to be reopened)", "곧 육 자 회담이 재개될 거라고 합니다.", "다시 시작하다"),
        ("주춤하다", "to falter; to slow down", "백화점 판매가 주춤하면서 소비가 줄고 있습니다."),
        ("최저치", "(最低値) the lowest record", "주가가 연일 최저치를 기록하고 있습니다.", "최고치"),
        ("타격", "(打擊) a blow; a hit; an impact", "유가의 폭등으로 항공사들이 큰 타격을 받았습니다."),
    ]),
]
L3 = lesson(
    "U18 L4 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 구리 · 꽁치 · 꽃게 · 농기계 · 명태 · 석탄 · 수산자원 · 가서명 · 감귤 · 공산품 · 광물자원 · 규정 · 단계적 · 매장량 · 명문화 · 민감하다 · 발효 · 보완 대책 · 이행 · 자유무역협정 · 제고 · 촉진 · 친미 · 탐사 · 곤두박질치다 · 급락 · 변동 · 변수 · 약세 · 재개 · 타격",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book lists 동 under 구리 with the example 금, 은, 동메달; I give 동 as the related word. 수산자원’s Hanja are printed 水産資原 in the book (the usual form is 水産資源); I kept the book’s. 발효 has a homonym 발효 (醱酵), “fermentation”. 친미 lists 반미 as its opposite and 친일/반일, 친북/반북, 친한/반한 as related pairs (I joined them with a slash). 급락 lists 폭락 as similar and 급등, 폭등 as opposites. The examples had digits in the book (12시, 1위, 1월 1일, 6자 회담, FTA, WTO), which I spelled out in Hangul. Many entries have no example in the book.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=22, nread=18)),
)

# ================================================================== L4 Part 2
_NK3 = [
    ("제이 차 평양 가을철 국제상품 전람회 진행", "The 2nd Pyongyang Autumn International Trade Fair is held"),
    ("지난 구 월 이십오 일부터 이십팔 일까지 삼대혁명전시관에서 제이 차 평양가을철국제상품전람회가 성황리에 진행되었다.", "From the 25th to the 28th of last September, the 2nd Pyongyang Autumn International Trade Fair was held successfully at the Three Revolutions Exhibition Hall."),
    ("이번 전시회에는 우리 나라와 중국, 인도네시아, 스위스, 영국, 타이, 이딸리아, 벨라루씨, 중국홍콩 등지에서 온 팔십여 개의 회사들이 각종 제품들을 출품하여 참관자들의 이목을 끌었다.", "At this exhibition, more than 80 companies from our country, China, Indonesia, Switzerland, Britain, Thailand, Italy, Belarus, China-Hong Kong and other places entered various products and drew the attention of visitors."),
    ("전시회가 진행되는 기간 국내외의 많은 사람들은 최신공작기계들과 강철제품들, 새로 개발된 의약품들, 석유화학제품들, 전기 및 전자제품들, 여러 가지 식료품들과 일용품들을 돌아보면서 나라들 사이의 친선관계를 두터이하고 다방면적인 경제기술교류와 협조, 무역거래활동을 심화시켰다.", "During the exhibition, many people at home and abroad toured the latest machine tools, steel products, newly developed medicines, petrochemical products, electric and electronic products, and various foods and daily necessities, strengthening friendly relations among countries and deepening many-sided economic and technical exchange, cooperation and trading activities."),
    ("이번 전시회에서 특징적인 것은 조국의 회사들이 우수한 제품들을 많이 전시한 것이다.", "What was characteristic of this exhibition was that companies of the homeland displayed many excellent products."),
    ("이번 전시회에는 여러 회사들에서 사람의 건강장수에 이바지하는 새로운 의약품들과 건강식품들도 만들어 내놓아 이채를 띠였다.", "At this exhibition, several companies also made and put out new medicines and health foods that contribute to people’s health and longevity, which stood out."),
    ("미국에서 온 한 교포는 전시회장을 돌아보고 자기의 소감을 이렇게 피력하였다.", "A compatriot who had come from the United States toured the exhibition hall and expressed his impressions like this."),
    ("신심이 생긴다. 고국경제는 잠재력이 있으며 과학기술은 매우 높은 수준이다.", "“I feel confident. The homeland’s economy has potential and its science and technology are at a very high level."),
    ("미국이 요즘 아무리 고국을 제재한다고 기를 쓰지만 어림도 없다는 것이 전람회장을 돌아본 나의 느낌이다.", "However hard the United States tries these days to put sanctions on the homeland, it is out of the question — that is my feeling from touring the exhibition hall.”"),
    ("전람회는 삼 박 사 일밖에 진행되지 않았다.", "The exhibition was held for only three nights and four days."),
    ("그러나 수많은 해외동포들과 외국사람들이 전람회를 돌아보고 조국경제의 발전수준에 감탄을 표시하였다.", "But many overseas compatriots and foreigners toured the exhibition and expressed admiration for the level of development of the homeland’s economy."),
]
_SPEAK4B = [("북한의 경제에 대해서 아는 것을 이야기해 보세요.", "Talk about what you know of North Korea’s economy."), ("북한 경제에 대해 뉴스에서 들은 것이 있으면 요약해서 말해 보세요.", "If you have heard anything about North Korea’s economy in the news, summarize it and say it.")]
L4 = lesson(
    "U18 L4 · Part 2 (본 학습): a North Korean trade fair article",
    "본 학습 · 평양 국제상품 전람회 · 출품 · 참관자 · 교포 · 제재 · 잠재력 · 감탄 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: an article from a North Korean site", "The book prints an article from the North Korean website uriminzokkiri.com and asks four questions in English: the name, place and time of the event; who took part; what items could be seen; and a translation of the visitor’s underlined quote. The article uses North Korean spelling and vocabulary (조국, 고국, 이딸리아, 벨라루씨, 띠였다) and is a state-media text: its claims are the article’s, not mine or the book’s. The numbers are spelled in Hangul and the quotation marks 《 》 are dropped (the visitor’s words are the two sentences after the quote opens). The English is mine:", examples=passage(_NK3)),
        card("My answers to 학습활동 3", "1. The 2nd Pyongyang Autumn International Trade Fair, held at the Three Revolutions Exhibition Hall from September 25 to 28 (three nights and four days). 2. More than 80 companies from North Korea, China, Indonesia, Switzerland, Britain, Thailand, Italy, Belarus, China-Hong Kong and other places, and many visitors at home and abroad, including overseas Koreans. 3. The latest machine tools, steel products, newly developed medicines, petrochemical products, electric and electronic products, various foods and daily necessities, and new medicines and health foods for longevity. 4. The underlined quote (I take it to be the visitor’s statement about the United States): “However hard the United States tries these days to impose sanctions on the homeland, it is out of the question; that is how I felt after touring the exhibition hall.”"),
        card("말해 봅시다! (speaking)", "The book’s prompt (the English is mine; the book has no space after the first period, which I added):", examples=passage(_SPEAK4B)),
        card("Activities left out", "학습활동 1 (Listening, track 006): a public-interest advertisement (edunet4u.net): you choose its purpose (A. to promote trade between the two Koreas; B. to publicize the success of the Gaesung Industrial Complex; C. to advertise the two Koreas’ joint products for the U.S. market; D. to emphasize the necessity of a Korea–United States FTA). 학습활동 2 (Listening, track 007): a KBS news report on alcoholic-beverage trade: in English you write its topic and fill a table (item; importing country; exporting country; imported quantity; price and competing item; marketing plan). 학습활동 4 (Listening, track 008): an item from the Seoul Education Research & Information Institute: in English what happened in August last year, what dilemma the Korean Customs Administration faced, and how it solved it, who took part and what they did. They are audio."),
    ],
    exercises=uniq(
        _tr(_NK3, k=3)
        + [M("Where was the trade fair held?", "The Three Revolutions Exhibition Hall", ["A hotel in Seoul", "A port", "A university"], "삼대혁명전시관."), M("How many days did the fair last?", "Three nights and four days", ["A week", "Two days", "A month"], "삼 박 사 일."), M("About how many companies took part?", "More than 80", ["More than 800", "About 8", "About 20"], "팔십여 개."), M("What did the exhibitors’ new medicines and health foods contribute to?", "People’s health and longevity", ["Faster travel", "Cheaper food", "Military use"], "건강장수."), M("Where did the visitor who gave his impressions come from?", "The United States", ["China", "Italy", "Belarus"], "미국에서 온 한 교포."), M("What does 이딸리아 mean?", "Italy", ["Belarus", "Switzerland", "Thailand"], "North Korean spelling.")]
        + [F("전시회는 ___리에 진행되었다. (successfully)", "성황", ["유예", "단독"], "성황리에."), F("새로운 의약품들이 ___를 띠였다. (to stand out)", "이채", ["이목", "신심"], "이채를 띠다."), F("참관자들의 ___을 끌었다. (attention)", "이목", ["이채", "소감"], "이목을 끌다."), F("수많은 해외___들이 전람회를 돌아보았다. (compatriots)", "동포", ["참관자", "근로자"], "해외동포.")]
        + [read_q("제이 차 평양 가을철 국제상품 전람회가 성황리에 진행되었다"), read_q("팔십여 개의 회사들이 각종 제품들을 출품했다"), read_q("전람회는 삼 박 사 일밖에 진행되지 않았다"), read_q("북한의 경제에 대해서 아는 것을 이야기해 보세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("개성공단", "(開城工團) Gaesung Industrial Complex", ""),
        ("근로자", "(勤勞者) a worker; a wage earner; an employee", "근로자들의 권익을 보호합시다.", "노동자, 일꾼, 종업원"),
        ("누비다/누비고 다니다", "to crisscross; to go (all) around; to go here and there", "자전거로 전국을 누비고 다녔다."),
        ("한반도", "(韓半島) the Korean Peninsula", "요즘 한반도에 긴장감이 고조되고 있습니다."),
    ]),
    ("학습활동 2", [
        ("강냉이", "corn", "", "옥수수"),
        ("도수", "(度數) proof (of liquor); “number of degree”", "위스키 도수. 안경 도수."),
        ("민간 차원", "(民間 次元) private/civilian level; nongovernmental; “civilian dimension”", "정부는 민간 차원의 남북 교류는 허용한다는 방침입니다."),
        ("부리다/부려지다", "to unload; to discharge (cargo)/to be discharged", "이삿짐이 많지 않아서 짐을 부리기 쉬웠습니다."),
        ("북미 교역", "(北美 交易) trade between the United States and North Korea", "삼 월 북미 교역의 대부분은 구호물자가 대부분을 차지했습니다.", "북미무역"),
        ("소량", "(少量 or 小量) a small quantity/amount", "매일 섭취하는 소량의 알코올은 치매예방에 효과가 있다고 합니다.", "다량, 대량"),
        ("소주", "(燒酒) Soju; a distilled Korean liquor", "저는 소주는 너무 독해서 못 마셔요."),
        ("시판(하다/되다)", "(市販) coming to the market; going on sale (to sell in the market/to be sold in the market)", "새로 나온 아이파드가 어제부터 시판되었다."),
        ("신뢰(하다)", "(信賴) trust (to trust)", "저는 친구 사이에는 신뢰가 가장 중요하다고 생각해요.", "믿음, 믿다 / 불신하다"),
        ("조성(하다/되다)", "(造成) constructing; making (to construct; to make/to be constructed; to be made)", "이곳에 과학연구단지를 조성한다고 합니다."),
        ("증류식", "(蒸溜式) by distillation method; distilled", "소주는 증류식으로 만든 술입니다."),
        ("질", "(質) quality", "새로 나온 휴대폰은 이 전 모델에 비해 질이 상당히 떨어집니다.", "양, 량"),
        ("찹쌀", "glutinous rice; sweet rice; (extra) sticky rice", ""),
        ("통관절차", "(通關節次) customs clearance; a customs procedure", "통관절차가 까다롭습니다.", "세관통과절차"),
    ]),
    ("학습활동 3", [
        ("감탄(하다)", "(感歎) admiration; wonder; awe (to admire; to marvel at)", "경치가 아름다워 저절로 감탄이 나옵니다."),
        ("기를 쓰다", "(氣) to exert oneself to the utmost; to do one’s best", "기를 쓰고 달렸지만 열차를 놓치고 말았다.", "최선을 다하다"),
        ("동포", "(同胞) a compatriot; a fellow countryman", "해외에 거주하는 우리 동포들도 이제 선거를 할 수 있게 되었습니다."),
        ("벨라루씨", "Belarus", "", "벨라루스, 백러시아"),
        ("성황리에", "(盛況裏) successfully", "얼마 전 한국인의 날 축제가 엘에이에서 성황리에 막을 내렸습니다."),
        ("신심", "(信心) faith; trust", ""),
        ("어림도 없다", "to be nonsense; to be impossible; to be highly objectionable", "나한테 돈을 빌려 달라고? 어림도 없는 소리."),
        ("이딸리아", "Italy", "", "이탈리아, 이태리"),
        ("이목을 끌다", "(耳目) to draw attention; “to draw (one’s) ears and eyes”", "신제품 삼디 티브이가 소비자들의 이목을 끌고 있습니다.", "관심을 끌다, 주의를 끌다"),
        ("이바지하다", "to contribute", "미군은 한반도의 평화에 크게 이바지하고 있다.", "공헌하다"),
        ("이채를 띠다", "(異彩) to be conspicuous; to be eye-catching; to stand out", "이 작품은 현대 문학 작품 중에서도 이채를 띠고 있습니다."),
        ("잠재력", "(潛在力) a potential; a latent power", "인도가 성장 잠재력이 높은 나라라고 합니다."),
        ("전람회", "(展覽會) an exhibit; an exhibition", "그 전람회가 며칠 동안 열립니까?", "전시회, 박람회"),
        ("제재(하다)", "(制裁) sanctions; restriction (to impose sanctions)", "국제사회는 북한에 대해 경제제재를 하겠다고 발표했습니다."),
        ("조국", "(祖國) one’s native country; homeland; fatherland; “grandfather country”", "저는 조국을 위해 군대에 입대하고 싶습니다."),
        ("참관자", "(參觀者) an observer; a visitor", "세계 박람회 참관자 수가 칠천만 명을 넘어섰다고 합니다.", "참가자"),
        ("출품(하다)", "(出品) entry/submission (of an item into a contest, etc.) (to enter; to submit)", "그 영화가 해외 영화제에 출품되었습니다."),
        ("혁명", "(革命) a revolution", "최근 중동 지역 여러 나라의 혁명은 튀니지와 이집트에서 시작되었습니다."),
    ]),
    ("학습활동 4", [
        ("기발하다", "(奇拔) to be brilliant; to be ingenious; to be extraordinary", "그 신입사원은 기발한 제안으로 상을 받았다."),
        ("만만치 않다/만만찮다", "to be difficult; to be tough; “(it) is not easy (to deal with)”", "이번 시합은 만만치 않은 상대와 하게 되어 긴장됩니다.", "만만하다, 쉽다"),
        ("말끔하다", "to be neat; to be tidy", "대청소를 했더니 방이 말끔해졌다."),
        ("모방(하다)", "(模倣) imitation; copying (to imitate; to copy)", "아이들은 부모를 모방합니다."),
        ("모조품", "(模造品) an imitation; a counterfeit", "이 모조품은 아주 정교해서 진품과 구별하기 어렵습니다.", "정품, 진품 / 짝퉁, 가짜"),
        ("밀반입", "(密搬入) smuggling; illegal entry of goods", "마약을 밀반입한 일당이 검찰에 검거되었습니다.", "밀수입, 밀수"),
        ("밋밋하다", "to be dull; to be plain; to be bland", "영화가 너무 밋밋하고 재미가 없었다."),
        ("뻔하다", "to be obvious; to be evident", "이 이야기는 너무 뻔해서 별로 재미가 없어요."),
        ("산뜻하다", "to be fresh and bright; to be refreshing", "봄이 되어 산뜻한 색의 옷을 입는 여성이 많다."),
        ("총장", "(總長) the president (of a university); the chancellor; a secretary-general", "대학부정입학 때문에 총장이 사퇴하겠다고 발표했습니다."),
        ("켤레", "a counter for pairs of shoes, socks, gloves, etc.", "백화점 세일에서 구두를 두 켤레 샀다."),
    ]),
]
L5 = lesson(
    "U18 L4 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 개성공단 · 근로자 · 한반도 · 도수 · 소주 · 시판 · 신뢰 · 질 · 통관절차 · 감탄 · 동포 · 성황리에 · 이목을 끌다 · 이바지하다 · 이채를 띠다 · 잠재력 · 전람회 · 제재 · 조국 · 참관자 · 출품 · 혁명 · 모방 · 모조품 · 밀반입 · 총장 · 켤레",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book prints the example of 시판 with the product name 아이파드 (probably meant as the iPad), which I kept as printed. 질 has the example 이 전 모델 (written with a space in the book) and lists 양/량 as its counterpart. 신뢰 lists 믿음 (믿다) as similar and 불신(하다) as the opposite. 모조품 lists 정품, 진품 as the genuine article and 짝퉁, 가짜 as fakes. 소량’s Hanja are printed 少量/小量, which I wrote as “(少量 or 小量)”. The examples contained digits and Latin letters (3월, LA, 3D TV, 7000만 명), which I spelled out; the exclamation mark in the example of 어림도 없다 became a period. The book gives no example for 개성공단, 강냉이, 찹쌀, 벨라루씨, 이딸리아 and 신심.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=22, nread=18)),
)

# ================================================================== L6 Part 3
_ARG4 = [
    ("관세가 없어지면 그만큼 수출회사는 많은 돈을 벌게 됩니다. 또 미국이라는 세계적으로 큰 시장과 거래한다면 큰 시장을 안정적으로 확보하게 되니까 우리나라 경쟁력도 높아질 것입니다.", "A. When the customs duties disappear, export companies earn that much more money. Also, if we trade with a market as large as the United States, we will secure a large market stably, so our country’s competitiveness will rise too."),
    ("한미 에프티에이가 협상되면 우리나라 농업은 완전히 망하게 됩니다. 미국에서 값싼 쌀들이 들어오면 누가 비싼 우리 쌀을 사 먹겠습니까? 그러다 보면 우리나라 농부들이 농사를 짓지 않게 될 것입니다. 우리나라가 전혀 쌀농사를 하지 않으면 미국은 이때다 하고 쌀값을 아주 비싸게 올릴 것입니다. 그럼 우리는 농사를 짓지 않기 때문에 그 비싼 쌀을 사 먹을 수밖에 없습니다.", "B. If the Korea-US FTA is negotiated, our country’s agriculture will be completely ruined. If cheap rice comes in from the United States, who will buy our expensive rice? Then our farmers will stop farming. If our country does no rice farming at all, the United States will say “this is the time” and raise the price of rice very high. Then, since we do not farm, we have no choice but to buy that expensive rice."),
    ("미국에 많은 협조를 하고 있는 일본조차도 에프티에이 협상을 미루고 있다고 합니다. 즉 손해가 이익보다 많기 때문에 신중하게 고려하고 있는 것이지요. 그런데 왜 우리나라는 서두르려고 할까요?", "C. They say that even Japan, which cooperates a lot with the United States, is putting off FTA negotiations. That is, it is considering carefully because the losses are greater than the benefits. Then why does our country try to hurry?"),
    ("무역을 잘하는 나라는 당연히 잘 살 수밖에 없습니다. 우물 안 개구리처럼 우리 혼자 살 수 있는 것도 아니고 무역은 꼭 필요한 것 아닙니까?", "D. A country that trades well naturally cannot help but live well. We cannot live alone like a frog in a well, and isn’t trade absolutely necessary?"),
]
_COUNTER4 = [
    ("우리는 지금 에프티에이를 맺지 않았지만 미국과 교역을 하고 있습니다. 모든 나라들이 에프티에이를 하는 것처럼 얘기하는데 일본, 스위스와 같은 나라들은 아직 에프티에이를 하지 않고 있습니다. 즉 그만큼 이익보다는 손해가 더 많기 때문이지요.", "A. We are not in an FTA now, but we trade with the United States. You talk as if every country does an FTA, but countries such as Japan and Switzerland have not yet done one. That is, it is because the losses are greater than the benefits to that extent."),
    ("대기업의 경우 지금보다 많은 이익을 얻을 수도 있겠죠. 하지만 중소기업과 같이 작은 회사들은 미국의 큰 회사들과 싸우기에는 힘이 모자라서 망할 위험이 높습니다.", "B. In the case of big companies, they may get more profit than now. But small companies, like small and medium-sized businesses, lack the strength to fight America’s big companies, so the risk that they will go under is high."),
    ("우리는 지금 세계적으로 가장 비싼 쌀을 사 먹고 있습니다. 하지만 같은 질에 많은 양을 싸게 먹을 수 있다면 소비자는 그런 쌀을 사 먹을 권리가 있습니다. 농민 측에서만 생각하고 있는데 소비자의 입장에서도 생각해 줄 필요가 있습니다. 가난해서 쌀을 못 먹던 사람들도 쌀이 싸지면 사 먹을 수 있게 됩니다.", "C. We are now buying the most expensive rice in the world. But if we can eat a large amount of the same quality cheaply, consumers have the right to buy such rice. You are thinking only from the farmers’ side, but it is necessary to think from the consumers’ standpoint too. Even people who could not eat rice because they were poor can buy it when rice becomes cheap."),
    ("일본과 미국이 그렇다고 해서 우리나라까지 따라 할 필요는 없다고 생각합니다. 유럽의 독일, 프랑스, 오스트리아와 같은 선진국가들은 에프티에이를 통해 서로 많은 도움을 주며 무역을 하고 있습니다.", "D. I think there is no need for our country to follow just because Japan and the United States are so. Advanced countries of Europe such as Germany, France and Austria trade while giving each other a lot of help through FTAs."),
]
_SPEAK4C = [("미국과 중국의 무역에 대해서 이야기해 보세요.", "Talk about trade between the United States and China."), ("주요 수출품과 수입품을 아는 대로 이야기하고, 무역 불균형 등 문제점에 대해서도 말해 보세요.", "Say what you know of the main exports and imports, and also tell about problems such as trade imbalance."), ("두 그룹으로 나누어 미국이 중국과 자유무역협정을 체결하는 것에 대해서 찬반토론을 해 보세요.", "Divide into two groups and debate for and against the United States concluding a free trade agreement with China."), ("분야별로 미국의 이익과 손해에 대해서 설명하세요.", "Explain the benefits and losses of the United States field by field.")]
L6 = lesson(
    "U18 L4 · Part 3 (심화 학습): arguments for and against the Korea-US FTA",
    "심화 학습 · 한미 에프티에이 · 찬성 · 반대 · 관세 · 쌀 · 중소기업 · 소비자 · 우물 안 개구리 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2, step 1: four arguments (edunet4u.net)", "The book lists four arguments, A to D, in a table and asks you to mark each pro (찬성) or con (반대) and write its key points in English. The text is from a summary of Korean students’ debate; FTA is written 에프티에이. The arguments, with my English:", examples=passage(_ARG4)),
        card("My answers to step 1", "A: pro (no duties means more export profit and a stable big market, so competitiveness rises). B: con (cheap American rice would drive Korean farmers out; later the US could raise rice prices and Korea would have to buy). C: con (even Japan, which cooperates with the US, is delaying; the losses may exceed the benefits, so why hurry?). D: pro (a country that trades well prospers, and Korea cannot live alone like a frog in a well)."),
        card("학습활동 2, step 2: four counterarguments", "The book lists four counterarguments, each with a check box for pro or con and the letters A–D of the argument it relates to. The counterarguments, with my English:", examples=passage(_COUNTER4)),
        card("My answers to step 2", "The circles are not marked, so the relations are my reading. Counterargument A: con; it answers argument D (we already trade with the US without an FTA, and countries such as Japan and Switzerland have not done one). B: con; it answers argument A (big companies may gain, but small ones risk going under). C: pro; it answers argument B (consumers have a right to cheap rice). D: pro; it answers argument C (Japan and the US are not models; advanced European countries help each other through FTAs)."),
        card("말해 봅시다! (speaking)", "The book’s two prompts, which I split into four sentences (the English is mine):", examples=passage(_SPEAK4C)),
        card("Activities left out", "학습활동 1 (Listening, track 009): an interview with an economics professor (edunet4u.net): you choose what it is about (A. Korea’s export boom; B. exportation problems in Korea; C. Korea’s major export items; D. the importance of Korea’s trading partners in Europe) and write in English why it is unfavorable to have only a limited number of trading partners. 학습활동 3 (Listening, Speaking, track 010): a YTN interview with an economic expert on the outlook after the Korea-US FTA: in English you list the three benefits the anchorman summarizes, two industries that will suffer, the two sectors that will benefit with prospects and reasons, choose which suggestion (A. differentiate Korean products from imported goods; B. emulate US mass production; C. lower prices; D. encourage consumers to use Korean-made items) best matches the interviewee’s, and fill a before/after table of Korea’s and the US’s situation. They are audio."),
    ],
    exercises=uniq(
        _tr(_ARG4, k=3) + _tr(_COUNTER4, k=3)
        + [M("Which argument says export companies earn more when duties disappear?", "A", ["B", "C", "D"], "관세가 없어지면."), M("Which argument fears that Korean agriculture will be ruined?", "B", ["A", "C", "D"], "농업은 완전히 망하게 됩니다."), M("Which argument points to Japan delaying FTA talks?", "C", ["A", "B", "D"], "일본조차도."), M("What does 우물 안 개구리 describe?", "A person of limited scope", ["A person who hurries", "A person who trades well", "A person who is poor"], "A frog in a well."), M("What does counterargument C say consumers have?", "The right to buy cheap rice", ["The duty to buy Korean rice", "A discount on duties", "Access to loans"], "소비자는 사 먹을 권리."), M("Which European countries does counterargument D name?", "Germany, France and Austria", ["Spain, Italy and Greece", "Britain, Ireland and Norway", "Sweden, Denmark and Finland"], "독일, 프랑스, 오스트리아.")]
        + [F("값싼 쌀들이 들어오면 우리나라 농업은 완전히 ___게 됩니다. (to be ruined)", "망하", ["서두르", "모자라"], "망하다."), F("손해가 이익보다 많기 때문에 ___하게 고려하고 있는 것이지요. (carefully)", "신중", ["대량", "과도"], "신중하게."), F("중소기업은 큰 회사와 싸우기에는 힘이 ___서 망할 위험이 높습니다. (to be short)", "모자라", ["서두르", "망하"], "모자라다."), F("일본조차도 에프티에이 협상을 ___고 있다고 합니다. (to put off)", "미루", ["서두르", "망하"], "미루다.")]
        + [read_q("관세가 없어지면 수출회사는 많은 돈을 벌게 됩니다"), read_q("값싼 쌀들이 들어오면 우리나라 농업은 망하게 됩니다"), read_q("일본조차도 에프티에이 협상을 미루고 있다고 합니다"), read_q("무역은 꼭 필요한 것 아닙니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("기울이다", "to devote; to direct (one’s efforts/attention); “to lean”", "학생들은 시험준비에 노력을 기울이고 있습니다."),
        ("다양(하다)", "(多樣) variety; diversity (to be various; to be diverse)", "이 식당에는 다양한 메뉴가 있습니다."),
        ("응하다", "(應) to accept; to accede; to respond", "초대를 받았지만 응하지 않았다."),
        ("의존(하다)", "(依存) dependence; reliance (to depend; to rely)", "그 나라의 경제는 관광 수입에 의존하고 있다.", "의지하다"),
        ("주력(하다)", "(注力) concentration (of one’s efforts, energy, resources, etc); devotion; exertion (to concentrate; to devote; to exert)", "경찰이 증거를 찾는 데 주력하고 있다."),
        ("한정(하다/되다)", "(限定) restriction; limit (to restrict; to limit/to be restricted; to be limited)", "이번에 새로 나온 음반은 삼천 장 한정 판매를 한다고 합니다.", "제한"),
    ]),
    ("학습활동 2", [
        ("교역(하다)", "(交易) trade (with foreign countries); commerce (to trade)", "한반도의 긴장으로 남북교역이 크게 줄고 있다.", "무역, 상업, 상거래, 거래"),
        ("망하다", "(亡) to go bankrupt; to go out of business", "불경기로 인해 많은 중소기업이 망하고 있다.", "실패하다, 도산하다"),
        ("모자라다", "to be short; to be insufficient", "시간이 모자라서 문제를 다 풀지 못했다.", "부족하다 / 남다, 넘치다, 충분하다"),
        ("서두르다", "to rush; to hasten; to be in haste", "서두른다고 해결될 일이 아닙니다."),
        ("스위스", "Switzerland; “Swiss”", ""),
        ("우물 안 개구리", "(proverb) a babe in the woods; a man of limited scope; “a frog in a well”", "우물 안 개구리처럼 살지 말고 넓은 세상으로 나가라."),
    ]),
    ("학습활동 3", [
        ("고부가가치", "(高附加價値) high (added) value; highly added value", "케이팝과 같은 한류문화 상품이 고부가가치를 얻고 있다."),
        ("농수산업", "(農水産業) agriculture and fisheries", "한국은 천구백육십 년대까지는 농수산업이 성행했습니다.", "농업, 어업, 수산업, 공업, 광업, 서비스업"),
        ("농축산물", "(農畜産物) agricultural and stockbreeding products; agro and livestock products", "수입 장벽이 철폐되어 농축산물의 가격이 크게 하락할 것으로 보입니다.", "농산물, 수산물, 축산물"),
        ("대량생산(하다/되다)", "(大量生産) mass production; “production in big amount” (to mass produce/to be massed produced)", "공장에서 기계로 물건을 생산하기 시작하면서 대량생산이 가능해졌습니다."),
        ("범용 제품", "(汎用 製品) an item for wide use; a general-purpose item; “common use item”", "이제 컴퓨터와 핸드폰은 범용 제품이 되었습니다."),
        ("집약(하다/시키다/되다)", "(集約) integration; convergence (to integrate; to converge/to be intensive)", "로봇 생산은 첨단 기술이 집약되는 산업이다."),
        ("짚다", "to place one’s hands on; to use (a stick/cane for balance); to point out; to deal with", "발목을 다쳐서 한동안 목발을 짚고 다녔습니다. 이 시간에는 최근 발생한 문제의 원인을 짚어 보겠습니다."),
        ("차별화(하다/되다)", "(差別化) differentiation (to differentiate/to be differentiated)", "제품 경쟁에서 이기려면 가격 차별화와 품질 차별화가 동시에 필요합니다."),
        ("창출(하다/되다)", "(創出) creation (to create/to be created)", "정부의 일자리 만들기 프로그램으로 이만 개의 일자리가 창출되었다고 합니다.", "생성, 창조, 만들다, 생기다"),
        ("침투(하다/되다)", "(浸透) infiltration; penetration (to infiltrate; to penetrate/to be infiltrated; to be penetrated)", "무장한 간첩이 비무장지대를 통해 서울로 침투한 사건이 발생했다.", "침입"),
        ("카리브 해", "(海) the Caribbean Sea", "내가 좋아하는 영화는 카리브 해의 해적 시리즈입니다."),
        ("토지", "(土地) land (used for farming or residences)", "이 지역의 토지는 국가 소유입니다.", "대지, 땅, 흙"),
        ("호소(하다)", "(呼訴) appeal; plea; complaint; plead (to appeal; to plea; to complain; to plead)", "경제가 나빠지면서 생활의 어려움을 호소하는 사람들이 늘고 있다."),
    ]),
]
L7 = lesson(
    "U18 L4 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 기울이다 · 다양 · 응하다 · 의존 · 주력 · 한정 · 교역 · 망하다 · 모자라다 · 서두르다 · 우물 안 개구리 · 고부가가치 · 농수산업 · 농축산물 · 대량생산 · 범용 제품 · 집약 · 짚다 · 차별화 · 창출 · 침투 · 카리브 해 · 토지 · 호소",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book gives 짚다 two examples; I joined them. 농수산업 lists 농업, 어업, 수산업, 공업, 광업, 서비스업 as related words and 농축산물 lists 농산물, 수산물, 축산물; 모자라다 lists 부족하다 as similar and 남다, 넘치다, 충분하다 as opposites (separated by a slash). The examples had digits and Latin letters in the book (3,000장, K-pop, 1960년대, 2만 개), which I spelled out (삼천 장, 케이팝, 천구백육십 년대, 이만 개), and the film title in the example of 카리브 해 had quotation marks, which I dropped. The book gives no example for 스위스. 우물 안 개구리 is called a proverb in the book; its English glosses “a babe in the woods” and “a frog in a well” are the book’s.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=18, nread=15)),
)

UNIT = unit("Semester III · Unit 18 · Lesson 4: Trade (무역)", [L1, L2, L3, L4, L5, L6, L7])
