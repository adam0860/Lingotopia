"""Unit 85: KBC Semester III, Unit 17, Lesson 10 - Alternative Energy (대체 에너지).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 17, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH10 = [("연료", "fuel", "최근 각국에서 바이오 연료를 개발하기 위해 많은 투자를 합니다"), ("풍력", "wind-powered", "정부에서는 풍력, 수력 등 자연 에너지원을 개발하기 위해 투자를 하고 있습니다"), ("수소", "hydrogen", "수소를 에너지원으로 활용할 수 있습니다"), ("태양광", "sunlight; solar", "태양광 에너지가 새로운 에너지원으로 떠오르고 있습니다"), ("전지", "a battery", "대기업이 연료 효율성이 높은 전지 개발에 큰 투자를 하고 있습니다"), ("재생", "reproduction", "태양광, 수력발전 등 재생에너지의 종류는 다양합니다"), ("발전소", "a power plant", "바람이 많은 제주도에 풍력 발전소를 건설할 계획이라고 합니다"), ("원자력", "nuclear energy", "원자력 발전소의 안전성에 대해 논란이 많습니다"), ("폐수", "wastewater", "최근 폐수 불법 배출 단속에 걸린 공장이 많습니다")]
_HJ10 = [("境 경", "boundary; situation", "환경, 경계선"), ("光 광", "light", "태양광, 영광"), ("代 대", "replace; substitute", "대변인, 대신에"), ("熱 열", "heat", "해열제, 열풍"), ("原 원", "origin(al)", "자원, 원목")]
_HJW10 = [("환경", "environment"), ("경계선", "a boundary line"), ("태양광", "sunlight"), ("영광", "honor; glory"), ("대변인", "a spokesperson"), ("대신에", "instead of"), ("해열제", "antipyretic (fever reducer)"), ("열풍", "a fever; a craze; a bandwagon; “heated wind”"), ("자원", "resources"), ("원목", "log; lumber; “original wood”")]
_SIM10 = [("열중", "열심", "absorption: earnestness"), ("원래", "본래", "originally: originally"), ("대체", "대신", "substitution: instead")]
_CAT10 = [("수력, 원자력, 풍력", "발전소", "water, nuclear and wind power: power plant"), ("경차, 전기차, 수소연료", "친환경", "small car, electric car, hydrogen fuel: eco-friendly"), ("토양, 수질, 대기", "오염", "soil, water quality, air: pollution")]
_L10X = [("바이오 연료", "biofuel"), ("자연 에너지원", "a natural energy source"), ("에너지원", "an energy source"), ("재생에너지", "renewable energy"), ("풍력 발전소", "a wind-power plant"), ("원자력 발전소", "a nuclear power plant"), ("수력발전", "hydroelectric power"), ("투자", "investment"), ("열심", "earnestness"), ("열량", "calories; heat quantity"), ("과열", "overheating"), ("본래", "originally"), ("장래", "the future"), ("거래", "a transaction"), ("대량", "a large quantity"), ("환대", "a warm welcome"), ("경차", "a small car"), ("전기차", "an electric car"), ("수소연료", "hydrogen fuel"), ("토양", "soil"), ("수질", "water quality"), ("대기", "the air; the atmosphere"), ("오염", "pollution"), ("친환경", "eco-friendly"), ("홍보", "publicity")]
L1 = lesson(
    "U17 L10 · Review: energy words and Sino-Korean 境 光 代 熱 原",
    "대체 에너지 · 단어 복습 · 한자어 복습 · 연료 · 풍력 · 수소 · 태양광 · 전지 · 재생 · 발전소 · 원자력 · 폐수 · 境 光 代 熱 原",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives nine sentences with a word underlined and asks you to connect each with its English meaning. The underline is not marked in the text; the pairs below are my best reading:", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH10], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ10], say=[2]), ktable(_HJW10)]),
        card("한자어 복습 1: the similar word (my answers)", "Circle the word with a similar meaning to the word on the left (A. 열중: 열심, 열량, 과열; B. 원래: 본래, 장래, 거래; C. 대체: 대량, 대신, 환대).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM10], say=[0, 1])]),
        card("한자어 복습 2: the word that links the three (my answers)", "Read the three words and choose from the box (오염, 친환경, 발전소, 홍보) the word that relates them:", tables=[table(["Three words", "Answer", "Meaning"], [list(r) for r in _CAT10], say=[0, 1])]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 004): four spoken sentences, for each of which you circle it if it helps protect the environment and mark X if it does not. It is audio."),
        card("More words from these exercises", "", tables=[ktable(_L10X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH10], k=3) + _tr(_HJW10, k=3) + _tr(_L10X, k=4)
        + [M("What does the syllable 境 (경) mean?", "boundary; situation", ["light", "heat", "origin"], "환경."), M("What does the syllable 光 (광) mean?", "light", ["boundary", "heat", "replace"], "태양광."), M("What does the syllable 代 (대) mean?", "replace; substitute", ["light", "heat", "origin"], "대신에."), M("What does the syllable 熱 (열) mean?", "heat", ["light", "boundary", "replace"], "열풍."), M("What does the syllable 原 (원) mean?", "origin(al)", ["light", "heat", "boundary"], "자원.")
           , M("Which word is similar to 열중?", "열심", ["열량", "과열", "열풍"], "Earnestness."), M("Which word is similar to 원래?", "본래", ["장래", "거래", "자원"], "Originally."), M("Which word is similar to 대체?", "대신", ["대량", "환대", "대변인"], "Instead."), M("Which word links 수력, 원자력, 풍력?", "발전소", ["오염", "친환경", "홍보"], "Power plant."), M("Which word links 경차, 전기차, 수소연료?", "친환경", ["오염", "발전소", "홍보"], "Eco-friendly."), M("Which word links 토양, 수질, 대기?", "오염", ["친환경", "발전소", "홍보"], "Pollution.")
           , F("최근 각국에서 바이오 ___를 개발하기 위해 많은 투자를 합니다. (fuel)", "연료", ["전지", "폐수"], "연료."), F("___를 에너지원으로 활용할 수 있습니다. (hydrogen)", "수소", ["폐수", "연료"], "수소."), F("대기업이 연료 효율성이 높은 ___ 개발에 큰 투자를 하고 있습니다. (battery)", "전지", ["폐수", "수소"], "전지."), F("최근 ___ 불법 배출 단속에 걸린 공장이 많습니다. (wastewater)", "폐수", ["연료", "전지"], "폐수."), F("___ 발전소의 안전성에 대해 논란이 많습니다. (nuclear)", "원자력", ["풍력", "수력"], "원자력.")]
        + [read_q("최근 각국에서 바이오 연료를 개발하기 위해 많은 투자를 합니다"), read_q("수소를 에너지원으로 활용할 수 있습니다"), read_q("태양광 에너지가 새로운 에너지원으로 떠오르고 있습니다"), read_q("원자력 발전소의 안전성에 대해 논란이 많습니다")]
    ),
)

# ================================================================== L2 Part 1
_WIND10 = [
    ("태풍 갈매기가 지나간 뒤 부는 청명한 바닷바람을 맞으며 이십삼 일 밤 경북 영덕군 영덕읍 창포리 영덕풍력발전단지의 발전기가 힘차게 돌아가고 있다.", "Facing the clear sea breeze that blows after Typhoon Kalmaegi has passed, the generators of the Yeongdeok Wind Power Complex in Changpo-ri, Yeongdeok-eup, Yeongdeok-gun, North Gyeongsang Province, turn vigorously on the night of the 23rd."),
    ("연일 고유가 행진이 거듭되면서 전력거래의 평균시장가격도 킬로와트시 당 지난해 팔십삼 점 칠오 원에 비해 올해는 상반기에만 백칠 점 칠칠 원으로 급등했는데, 풍력발전은 고유가 행진 속에 대체 에너지 생산과 매출 증대에 한몫하고 있다.", "As high oil prices continue day after day, the average market price of electricity trading has also soared from 83.75 won per kilowatt-hour last year to 107.77 won in the first half of this year alone, and wind power is playing a part in producing alternative energy and increasing sales amid the high oil prices."),
]
_YEOSU10 = [
    ("여수박람회조직위, 태양광발전소 건립키로", "The Yeosu Expo Organizing Committee to build a solar power plant"),
    ("해양을 주제로 하는 이천십이 여수세계박람회장 인접지에 상당 규모의 태양광발전소가 건립된다.", "A fairly large solar power plant will be built on land adjacent to the site of the 2012 Yeosu World Expo, whose theme is the “ocean”."),
    ("이천십이 세계박람회조직위는 무공해 전력 생산, 친환경 이벤트, 저탄소 녹색성장 교육을 동시에 할 수 있는 에너지파크를 국내 처음으로 박람회장 인접지에 조성키 위해 십삼 일 조직위 사무실에서 한국중부발전 주식회사 측과 설비용량 이 메가와트의 태양광발전소 건설과 운영에 관한 실시협약을 체결했다고 밝혔다.", "The 2012 World Expo Organizing Committee announced that, to create on land adjacent to the expo site, for the first time in Korea, an Energy Park where pollution-free power generation, eco-friendly events and low-carbon green growth education can be done at once, it concluded, on the 13th at the committee’s office, an implementation agreement with Korea Midland Power Co. on the construction and operation of a solar power plant with an installed capacity of 2 megawatts."),
    ("여수세계박람회 에너지파크는 여수시 덕충동에 팔만 오백삼십구 제곱미터 부지에 조성되며, 연간 이백육십삼만 킬로와트시의 태양광 발전소와 태양 빛을 활용한 에너지 오케스트라, 피아노 분수 등이 조성된다.", "The Yeosu World Expo Energy Park will be created on a site of 80,539 square meters in Deokchung-dong, Yeosu, with a solar power plant producing 2.63 million kilowatt-hours a year, an energy orchestra using sunlight, a piano fountain and so on."),
    ("여수박람회 에너지파크에는 또 무공해 에너지를 활용한 댄스플로어, 에너지트리, 대형스크린 등이 설치되어 초등학생과 중학생 단체관람객들이 저탄소 녹색성장의 중요함을 직접 체험할 수 있는 교육장으로도 활용된다.", "The Energy Park will also have a dance floor, an energy tree, a large screen and so on using pollution-free energy installed, so it will also be used as an educational site where group visitors of elementary and middle school students can directly experience the importance of low-carbon green growth."),
    ("에너지파크에 조성되는 태양광 발전소는 약 칠백 가구에 전력을 공급할 수 있는 양으로 온실가스를 연간 천육백 톤 감축하고, 이백칠십 헥타르의 산림을 가꾸는 것과 같은 효과를 거둘 것으로 기대된다.", "The solar power plant to be built in the Energy Park, in an amount that can supply power to about 700 households, is expected to cut greenhouse gases by 1,600 tons a year and to have the same effect as nurturing 270 hectares of forest."),
    ("여수박람회조직위 조명현 환경에너지 과장은 “태양광 발전과 이벤트, 교육이 조화된 에너지파크는 정부의 녹색성장정책과 친환경 여수세계박람회의 주제를 가장 잘 나타내는 장소가 될 것”이라고 말했다.", "Jo Myeong-hyeon, the head of the environment and energy section of the Yeosu Expo Organizing Committee, said, “The Energy Park, in which solar power generation, events and education are in harmony, will be the place that best shows the government’s green growth policy and the theme of the eco-friendly Yeosu World Expo.”"),
]
_SPEAK10A = [("대체 에너지의 종류에는 무엇이 있고 각각의 장단점은 무엇인지 아는 대로 친구와 함께 이야기해 보세요.", "Talk with a friend, as far as you know, about what kinds of alternative energy there are and what the advantages and disadvantages of each are."), ("자신이 생각하기에 가장 적절한 대체 에너지는 무엇인지, 왜 그렇게 생각하는지 친구와 함께 이야기해 보세요.", "Talk with a friend about which alternative energy you think is the most suitable, and why you think so.")]
L2 = lesson(
    "U17 L10 · Part 1 (도입 학습): wind power and the Yeosu Expo solar plant",
    "도입 학습 · 저탄소 녹색성장 · 풍력발전 · 고유가 · 대체 에너지 · 여수박람회 · 태양광발전소 · 에너지파크 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 (Let’s find out): 저탄소 녹색성장정책", "저탄소 녹색성장, which literally translates to “low carbon green growth”, is a slogan of the Korean government at the time of the book. It means that Korea will continue to grow economically while protecting the environment. This goal can be achieved by reducing greenhouse gas emissions and developing clean, alternative energy. Developing new energy sources will, in turn, lead to new jobs in the field and boost the economy."),
        card("학습활동 2: a photograph and its caption (Hankyoreh)", "The book asks (1) what the three lighted objects in the picture are and where they are located, and (2) the purpose of the article and the picture (A. to recruit people to work at this facility; B. to inform the public about an alternative source of energy; C. to educate the public on the importance of recycling; D. to announce the increase of the power rates this year). The caption writes the unit as KWh and the prices with decimals, which I spelled out in Hangul. The caption, with my English:", examples=passage(_WIND10)),
        card("My answers to 학습활동 2", "1. I cannot see the picture; from the caption, the lighted objects must be the generators (wind turbines) of the Yeongdeok Wind Power Complex, located at Changpo-ri, Yeongdeok-eup, Yeongdeok-gun, North Gyeongsang Province. 2. B, to inform the public about an alternative source of energy (wind power)."),
        card("학습활동 3: a newspaper article on the solar power plant of the Yeosu Expo (Kyunghyang)", "The book asks: (1) what is going to be built in 여수; (2) what is special about the Energy Park according to the first paragraph; (3) what would be a useful spot for students to visit and why; (4) how the plant will help protect the environment, specifically. The book writes the year, the date, MW, m2, KWh, “(주)”, ha and the numbers in digits and Latin letters; I spelled them in Hangul, and “초∙중생” (elementary and middle school students) is written out as 초등학생과 중학생. The name of the committee’s section head is that of a quoted official. The article, with my English:", examples=passage(_YEOSU10)),
        card("My answers to 학습활동 3", "1. A solar power plant (and the Energy Park around it) next to the site of the 2012 Yeosu World Expo. 2. It will be the first in Korea: an Energy Park where pollution-free power generation, eco-friendly events and low-carbon green growth education can be done at once, on land adjacent to the expo site. 3. My choice: the educational facilities of the Energy Park (the dance floor, energy tree and large screen using pollution-free energy), because elementary and middle school groups can directly experience the importance of low-carbon green growth. 4. The plant can supply power to about 700 households, cut greenhouse gases by 1,600 tons a year, and has the same effect as nurturing 270 hectares of forest."),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts (the English is mine):", examples=passage(_SPEAK10A)),
        card("Activities left out", "학습활동 1 (Reading): three graphs (energy consumption per person, dependence on energy from foreign countries, energy consumption per person by country) to be joined with their descriptions; they are charts. 학습활동 4 (Listening, tracks 005 to 007): a YTN news item on the use of eco-friendly energy, in which you fill a table with the type of energy and its use, and the project timeline. It is audio."),
    ],
    exercises=uniq(
        _tr(_WIND10, k=3) + _tr(_YEOSU10[1:], k=3)
        + [M("What is the theme of the 2012 Yeosu World Expo?", "The ocean", ["Space", "Food", "Cities"], "해양."), M("What kind of plant will be built next to the expo site?", "A solar power plant", ["A nuclear plant", "A coal plant", "A water plant"], "태양광발전소."), M("What is the installed capacity of the plant?", "2 megawatts", ["2 kilowatts", "20 megawatts", "200 megawatts"], "이 메가와트."), M("About how many households can the plant supply?", "About 700", ["About 70", "About 7,000", "About 70,000"], "약 칠백 가구."), M("How many tons of greenhouse gas will it cut a year?", "1,600 tons", ["160 tons", "16,000 tons", "16 tons"], "천육백 톤."), M("Who is expected to experience the importance of green growth at the park?", "Group visitors of elementary and middle school students", ["Only foreign tourists", "Only engineers", "Only farmers"], "초등학생과 중학생."), M("What has soared in the caption’s first-half-year report?", "The average market price of electricity trading", ["The speed of the wind", "The number of typhoons", "The price of rice"], "평균시장가격.")]
        + [F("연일 ___ 행진이 거듭되면서 전력거래의 평균시장가격이 급등했다. (high oil prices)", "고유가", ["고성능", "고수익"], "고유가 행진."), F("풍력발전은 대체 에너지 생산과 매출 ___에 한몫하고 있다. (increase)", "증대", ["감소", "교체"], "증대."), F("무공해 전력 생산, 친환경 이벤트, 녹색성장 교육을 동시에 할 수 있는 ___를 조성한다. (Energy Park)", "에너지파크", ["여수박람회", "태양광발전소"], "에너지파크."), F("약 칠백 가구에 전력을 ___할 수 있는 양이다. (to supply)", "공급", ["감축", "체결"], "공급하다.")]
        + [read_q("영덕풍력발전단지의 발전기가 힘차게 돌아가고 있다"), read_q("풍력발전은 대체 에너지 생산에 한몫하고 있다"), read_q("태양광발전소가 건립된다"), read_q("친환경 여수세계박람회의 주제를 가장 잘 나타내는 장소가 될 것이다")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("고유가 행진", "(高油價 行進) sustained high oil price; “high oil price marching”", "중동에서 석유 생산량을 줄이면서 고유가 행진이 계속되고 있습니다."),
        ("대체(하다/되다)", "(代替) substitution; replacement (to substitute; to replace/to be replaced)", "대체 에너지", "교체"),
        ("전력", "(電力) electricity; electric power", "수출을 증대하기 위한 방안이 무엇입니까?"),
        ("증대(하다)", "(增大) increase (to increase)", "", "감소"),
        ("한몫하다", "to play a role", "우리 당이 선거에서 이기는 데 선거운동원들이 한몫을 했다."),
    ]),
    ("학습활동 3", [
        ("건설(하다/되다)", "(建設) construction; building (to construct/to be constructed)", "천구백칠십 년대에서 팔십 년대에는 건설업이 호황을 누렸습니다.", "세우다, 짓다"),
        ("분수", "(噴水) a water fountain", "우리 아파트 앞에 분수대가 생겨서 아주 시원하고 좋아요."),
        ("산림을 가꾸다", "(山林) to nurture a forest", "", "산림을 조성하다, 숲을 조성하다"),
        ("실시협약", "(實施協約) an agreement to implement", ""),
        ("인접지", "(隣接地) the adjacent land", "서울 인접지는 집값이 아주 비쌉니다."),
        ("조직위", "(組織委 or 組織委員會) an organizing committee (the full form is 조직위원회)", ""),
    ]),
    ("학습활동 4", [
        ("교체(하다/되다)", "(交替) change; replacement; shift (to replace/to be replaced)", "자동차의 배터리를 교체해야 할 것 같습니다."),
        ("소각열", "(燒却熱) heat produced from trash incineration; “incineration heat”", ""),
        ("하수열", "(下水熱) heat produced from sewage; “underwater heat”", ""),
    ]),
]
L3 = lesson(
    "U17 L10 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 고유가 행진 · 대체 · 전력 · 증대 · 한몫하다 · 건설 · 분수 · 산림 · 실시협약 · 인접지 · 조직위 · 교체 · 소각열 · 하수열",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 증대, 산림을 가꾸다, 실시협약, 조직위, 소각열 and 하수열. 전력’s example in the book (“What is the plan to increase exports?”) is really an example of 증대, which was printed under 전력. 분수 has a homonym 分數, “discretion; good sense; propriety”. The book lists 조직위 / 조직위원회 together (組織委 / 組織委員會). The related words of 증대 (감소, “decrease”) and of 대체 (교체) are as in the book. The book writes 1970~80년대 in digits, which I spelled in Hangul.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=9)),
)

# ================================================================== L4 Part 2
_METH10 = [
    ("미국은 에탄올, 중국은 메탄올에 눈독", "The US has its eye on ethanol, China on methanol"),
    ("중국이 석유를 대체할 에너지로 메탄올에 눈독을 들이고 있다.", "China has its eye on methanol as an energy to replace oil."),
    ("석탄이나 천연가스에서 추출하는 메탄올은 사탕수수나 옥수수에서 뽑아내는 에탄올보다 생산원가가 싸고, 에너지 효율이 높은 장점이 있다.", "Methanol, extracted from coal or natural gas, has the advantages of a cheaper production cost and higher energy efficiency than ethanol drawn from sugar cane or corn."),
    ("미국과 브라질이 풍부한 생물자원을 활용해 에탄올 개발을 서두르는 동안, 중국은 네이멍구 등 주요 석탄 산지에 대규모 메탄올 공장을 짓고 있다.", "While the United States and Brazil hurry to develop ethanol using their abundant biological resources, China is building large-scale methanol plants in major coal-producing areas such as Inner Mongolia."),
    ("중국은 한때 대체 에너지로 풍력과 생물에너지에 주목했으나, 최근 들어 메탄올로 방향을 틀었다.", "China once paid attention to wind power and bioenergy as alternative energy, but recently it has turned its direction to methanol."),
    ("풍력은 에너지 축적이 불가능해 미래 에너지 구조에서 중요한 위치를 차지하기 힘들다는 게 중국 전문가들의 일반적인 판단이다.", "The general judgment of Chinese experts is that wind power, since it cannot store energy, will have a hard time taking an important place in the future energy structure."),
    ("국무원 산하 에너지연구소 왕쭝잉 주임은 한 인터뷰에서 “생물에너지는 원료 생산 및 수집, 운반에 드는 원가가 높다”고 말했다.", "Wang Zongying, the director of the Energy Research Institute under the State Council, said in an interview, “Bioenergy has a high cost in the production, collection and transport of raw materials.”"),
    ("최근 중국의 메탄올 생산기지로 급부상하는 곳이 네이멍구 오르도스이다.", "The place that has recently risen rapidly as China’s methanol production base is Ordos in Inner Mongolia."),
    ("오르도스에선 연간 메탄올 생산량이 백만 톤을 넘는 대형 공장이 여섯 개나 건설되고 있다.", "In Ordos, as many as six large plants with an annual methanol output of more than one million tons are being built."),
    ("이천십 년까지 모든 공사가 마무리되면 오르도스는 연간 천만 톤이 넘는 메탄올 생산능력을 갖추게 된다.", "When all the construction is finished by 2010, Ordos will have a methanol production capacity of more than ten million tons a year."),
    ("이 가운데 가장 규모가 큰 공장은 연간 사백이십만 톤의 메탄올을 생산하게 된다.", "Of these, the largest plant will produce 4.2 million tons of methanol a year."),
    ("오르도스가 이처럼 뜨는 이유는 메탄올 생산에 유리한 조건을 갖추고 있기 때문이다.", "The reason Ordos is rising like this is that it has conditions favorable to methanol production."),
    ("오르도스엔 메탄올 생산에 필요한 석탄과 천연가스가 풍부하다.", "Ordos is rich in the coal and natural gas needed for methanol production."),
    ("오르도스의 석탄 매장량은 확인된 것만 천사백구십육억 톤에 이른다.", "Ordos’s coal reserves reach 149.6 billion tons for the confirmed part alone."),
    ("이는 네이멍구 석탄 매장량의 절반, 중국의 십칠 퍼센트에 해당한다.", "This corresponds to half of Inner Mongolia’s coal reserves and 17 percent of China’s."),
]
_SPEAK10B = [("대체 에너지를 사용하여 집을 짓는 것에 대해 어떻게 생각합니까?", "What do you think about building houses using alternative energy?"), ("옆 사람과 같이 이야기해 보세요.", "Talk about it with the person next to you."), ("태양광 등 대체 에너지를 활용할 수 있는 집이나 건물을 지을 때 정부가 지원금을 주는 것에 대해 찬성합니까 반대합니까?", "Do you agree or disagree with the government giving subsidies when houses or buildings that can use alternative energy such as solar power are built?")]
L4 = lesson(
    "U17 L10 · Part 2 (본 학습): China’s methanol and the US ethanol",
    "본 학습 · 에탄올 · 메탄올 · 석탄 · 천연가스 · 생산원가 · 에너지 효율 · 풍력 · 생물에너지 · 오르도스 · 네이멍구 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: a newspaper article on China’s energy development (Hankyoreh)", "The book asks: (1) compare how China and the US are developing new energy; (2) what disadvantages China sees in wind power and bioenergy; (3) list two pieces of information about 오르도스. The numbers are in digits in the book (100만 t, 6개, 2010년, 1000만 t, 420만 t, 1496억 t, 17%); I spelled them in Hangul and wrote 톤 for t. The name of the researcher is that of an expert quoted in the article. The article, with my English:", examples=passage(_METH10)),
        card("My answers to 학습활동 2", "1. The US (and Brazil) hurry to develop ethanol drawn from sugar cane and corn using their abundant biological resources, while China builds large methanol plants (methanol extracted from coal or natural gas, with a cheaper production cost and higher energy efficiency) in coal-producing areas such as Inner Mongolia. 2. Wind power: it cannot store energy, so it is hard for it to take an important place in the future energy structure. Bioenergy: the cost of producing, collecting and transporting the raw materials is high. 3. A: Ordos is rising as China’s methanol production base, with six large plants of more than a million tons a year under construction and a capacity of over ten million tons a year when finished in 2010. B: Its confirmed coal reserves are 149.6 billion tons, half of Inner Mongolia’s and 17 percent of China’s."),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts of Part 2 (the second one has two sentences; the English is mine):", examples=passage(_SPEAK10B)),
        card("Activities left out", "학습활동 1 (Listening and video, tracks 008 and 009): a YTN news item about local governments of Gyeonggi Province: you answer what is increasing, how Ms. Park benefited from the newly installed device, and what contributed to the 50% increase in installations of the device, and then check your answers with the video. 학습활동 3 (Listening, tracks 010 and 011): an interview with the head of the Korea Petroleum Association: you answer in English the advantages of a diesel hybrid bus, when it uses diesel and when electricity, the advantage of clean diesel buses over gasoline and natural gas buses, fill a table with the plans for production (first round) and distribution (second round) of the diesel hybrid buses, and summarize how hybrid buses will help the national economy. They are audio and video."),
    ],
    exercises=uniq(
        _tr(_METH10, k=3)
        + [M("Which energy does China have its eye on, according to the title?", "Methanol", ["Ethanol", "Solar power", "Hydrogen"], "메탄올."), M("What is methanol extracted from, according to the article?", "Coal or natural gas", ["Sugar cane or corn", "Wind", "Seawater"], "석탄이나 천연가스."), M("What are the advantages of methanol over ethanol?", "A cheaper production cost and higher energy efficiency", ["A better smell", "More sugar", "Fewer factories"], "생산원가가 싸고."), M("Why do Chinese experts doubt wind power?", "It cannot store energy", ["It is too expensive", "It makes noise", "It needs oil"], "에너지 축적이 불가능."), M("What is the problem of bioenergy, according to the director?", "The cost of producing, collecting and transporting raw materials is high", ["It is not green", "It is not safe", "There is no demand"], "원가가 높다."), M("Which place is rising as China’s methanol production base?", "Ordos in Inner Mongolia", ["Beijing", "Shanghai", "Hainan"], "오르도스."), M("What share of China’s coal reserves is in Ordos?", "17 percent", ["50 percent", "7 percent", "70 percent"], "십칠 퍼센트.")]
        + [F("중국은 대체 에너지에서 메탄올로 ___을 틀었다. (direction)", "방향", ["온도", "원가"], "방향을 틀다."), F("석탄이나 천연가스에서 ___하는 메탄올. (to extract)", "추출", ["축적", "운반"], "추출하다."), F("오르도스의 석탄 ___량은 확인된 것만 매우 많다. (reserves)", "매장", ["생산", "수집"], "매장량."), F("풍력은 에너지 ___이 불가능하다. (storing up)", "축적", ["추출", "운반"], "축적하다.")]
        + [read_q("중국이 석유를 대체할 에너지로 메탄올에 눈독을 들이고 있다"), read_q("풍력은 에너지 축적이 불가능하다"), read_q("오르도스에는 석탄과 천연가스가 풍부하다"), read_q("태양광 등 대체 에너지를 활용할 수 있는 집을 지을 때 정부가 지원금을 주는 것에 찬성합니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("늘리다", "to increase", "호텔의 객실 수를 늘립시다.", "줄이다 / 증가시키다, 확대하다"),
        ("발을 맞추다", "to be in sync with/in line with; to cooperate; to join; “to keep step with”", "소비자들의 다양한 기호에 발을 맞추어 백화점들도 다양한 추석선물을 선보이고 있다."),
        ("설비", "(設備) facilities and equipment", "그 공장은 최신식 설비를 갖추고 있습니다.", "시설"),
        ("예산", "(豫算) budget", "예산이 부족해서 그 계획을 시행할 수 없습니다."),
        ("지자체", "(地自體 or 地方自治團體) a local autonomous entity; a local government (the full form is 지방자치단체)", ""),
        ("편성(하다/되다)", "(編成) organization; formation (to organize; to form/to be organized)", "각 방송국들이 변하는 시청자들의 요구에 발 맞추어 프로그램을 새롭게 편성하고 있다."),
        ("한계", "(限界) limits; limitations", "그 등산가는 에베레스트를 정복함으로써 인간의 한계를 극복했습니다."),
    ]),
    ("학습활동 2", [
        ("급부상(하다)", "(急浮上) rapid rising (to the surface); “rapid surfacing” (to rise/emerge rapidly)", "중국이 신경제대국으로 급부상하고 있습니다.", "뜨다"),
        ("눈독을 들이다", "to have one’s eyes on (with desire)", "내가 새로 산 자동차에 동생이 눈독을 들이고 있다."),
        ("뜨다", "to float; to rise; to emerge", "요트가 물에 떠 있습니다. 요즘 새로운 인기 스타로 뜨고 있는 사람이 누구입니까?", "가라앉다 / 부상하다"),
        ("매장량", "(埋藏量) (the amount of) reserves deposit", "전 세계에 석유 매장량이 얼마나 됩니까?"),
        ("방향을 틀다", "(方向) to change the direction", "그 회사는 소프트웨어가 잘 안 되자 하드웨어로 방향을 틀었다."),
        ("산지", "(産地) place of production; home; producing area", "제주도는 귤 산지로 유명합니다.", "원산지"),
        ("서두르다", "to hurry; to rush; to hasten", "결혼식이 얼마 남지 않았어요. 결혼 준비를 서두릅시다."),
        ("석탄", "(石炭) coal", ""),
        ("수집(하다/되다)", "(收集) collection (to collect; to gather/to be collected)", "저는 골동품을 수집하는 것이 취미입니다."),
        ("운반(하다/되다)", "(運搬) transportation; transport (to transport; to carry/to be transported)", "이 가방을 차로 좀 운반해 주시겠어요?"),
        ("원가", "(原價) production cost; prime cost", "더 깎으시면 원가보다도 더 싸게 사시는 거예요."),
        ("원료", "(原料) raw material", "아크릴의 원료가 무엇입니까?", "재료"),
        ("추출(하다/되다)", "(抽出) extraction (of a substance, element, etc., in chemistry) (to extract/to be extracted)", "이 음료수는 각종 과일을 추출해서 만들었습니다."),
        ("축적(하다/되다)", "(蓄積) accumulation (to accumulate/to be accumulated)", "저희 제품은 몸에 축적된 독소를 제거합니다."),
        ("효율", "(效率) efficiency", "저희 회사는 업무 효율성을 높이기 위해 아이디어를 공모한다고 했습니다.", "비효율"),
    ]),
    ("학습활동 3", [
        ("감속(하다)", "(減速) reduction of speed (to reduce speed)", "비가 올 때는 감속하세요."),
        ("경유", "(輕油) diesel", "", "휘발유"),
        ("고양(하다/시키다/되다)", "uplift (to enhance; to boost; to raise/to be enhanced; to be boosted)", "우리 제품의 해외 인지도를 고양시키기 위해 최선을 다하고 있습니다."),
        ("동력원", "(動力源) source of power", "이 차의 주요 동력원은 전기입니다."),
        ("수급구조", "(需給構造) the structure of supply and demand", "농산물의 수급구조를 개선해야 합니다."),
        ("저감(하다)", "(低減) reduction; decrease (to reduce; to diminish)", "자동차에서 배출되는 탄소량을 저감시키기 위한 방법이 무엇이 있을까요?"),
        ("절감(하다/되다)", "(節減) reduction (to cut down; to reduce/to be cut down)", "휴가 비용 절감을 위해 식사는 직접 해 먹기로 했어요."),
        ("정유", "(精油) oil refining", "국내 정유회사들이 기름값을 올리고 있습니다."),
        ("정차(하다)", "(停車) stopping a vehicle (to stop a vehicle)", "이 구역에서는 주차, 정차를 하실 수 없습니다."),
        ("주행(하다)", "(走行) driving; running a vehicle (to drive; to run a vehicle)", "운전 면허를 받으려면 먼저 실기 시험을 보고 주행 시험에 합격해야 합니다.", "주행거리"),
        ("취지", "(趣旨) a purpose; an object; an aim", "이번 콘서트의 취지는 다문화 가정의 아이들에 대한 편견을 없애고자 하는 것이다."),
        ("편견", "(偏見) a prejudice; a bias", "아직은 다문화가정에 대한 편견이 존재합니다."),
        ("효과", "(效果) effect; effectiveness", "새 법안이 어떤 효과를 가져올지 궁금합니다.", "효과적"),
        ("휘발유", "(揮發油) gasoline", "", "경유, 등유, 석유, 원유"),
    ]),
]
L5 = lesson(
    "U17 L10 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 늘리다 · 발을 맞추다 · 설비 · 예산 · 지자체 · 편성 · 한계 · 급부상 · 눈독을 들이다 · 뜨다 · 매장량 · 방향을 틀다 · 산지 · 서두르다 · 석탄 · 수집 · 운반 · 원가 · 원료 · 추출 · 축적 · 효율 · 감속 · 경유 · 고양 · 동력원 · 수급구조 · 저감 · 절감 · 정유 · 정차 · 주행 · 취지 · 편견 · 효과 · 휘발유",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 경유, 석탄 and 휘발유. In the book 지자체 is listed with its full form 지방자치단체 (地方自治團體). 늘리다 has 줄이다 as an opposite and 증가시키다, 확대하다 as similar words (separated here by a slash). 뜨다 has two examples, one for each meaning, and 가라앉다 (to sink) and 부상하다 as related words; 급부상하다 lists 뜨다 as a similar word. 고양(하다/시키다/되다) has no Hanja in the book. The book writes the example of 정차 with “주, 정차” (parking and stopping), which I wrote as 주차, 정차. The related words after the comma are as in the book.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=18, nread=14)),
)

# ================================================================== L6 Part 3
_NUC10 = [
    ("청소년들의 원자력 이해 높이기 위해 행사 마련", "An event arranged to raise young people’s understanding of nuclear power"),
    ("국내 유일의 원자력 홍보기관인 한국원자력문화재단 이재환 이사장은 오 일 서울 신라호텔에서 기자를 만나자마자 행사 안내장부터 꺼내 들었다.", "Lee Jae-hwan, chairman of the Korea Nuclear Culture Foundation, the only nuclear power publicity organization in Korea, took out the event leaflet first thing when he met the reporter at the Shilla Hotel in Seoul on the 5th."),
    ("팔 일 경기 과천 서울대공원에서 개막하는 이천십 년 행복한 원자력 페스티벌을 알리는 내용이다.", "It announces the “2010 Happy Nuclear Power Festival”, opening on the 8th at Seoul Grand Park in Gwacheon, Gyeonggi Province."),
    ("이번 행사는 관람객들이 엑스레이 원리를 체험하면서 원자력 에너지가 실생활에 어떻게 사용되는지를 느낄 수 있도록 준비했다.", "This event was prepared so that visitors, while experiencing the principle of the X-ray, can feel how nuclear energy is used in real life."),
    ("또 지난해 십이 월 아랍에미리트에 수출한 차세대 원전 모형을 직접 살펴 보면서 원자력 에너지 생산 과정을 한눈에 이해하도록 하는 원전 수출산업관도 만들었다고 한다.", "They also say that they made a “nuclear plant export industry hall” where, looking directly at a model of the next-generation nuclear plant exported to the United Arab Emirates last December, visitors can understand the process of producing nuclear energy at a glance."),
    ("이 이사장은 “원자력 홍보에서 가장 어려운 점은 방사성 폐기물 처리의 안전성을 어떻게 국민들에게 정확히 알리느냐는 것”이라고 지적했다.", "Chairman Lee pointed out, “The most difficult point in promoting nuclear power is how to inform the public accurately about the safety of radioactive waste disposal.”"),
    ("그는 “아랍에미리트 원전 수주 이후 원전이 비선호시설에서 자동차, 반도체에 이은 신성장동력으로 급부상해 국민들의 인식 변화가 일어나고 있는 점이 고무적인 현상”이라고 밝혔다.", "He said, “After winning the order for the nuclear plant in the United Arab Emirates, nuclear plants have risen rapidly from an unpopular facility to a new growth engine following cars and semiconductors, and the change in the public’s perception is an encouraging phenomenon.”"),
]
_YAM10 = [
    ("폐식용유 활용 식물성 차로 지구 한바퀴", "Around the Earth in a “plant-based car” using waste cooking oil"),
    ("일본인 여행가 야마다 슈세이", "Yamada Shusei, a Japanese traveler"),
    ("석유 한 방울 없이 자동차로 세계 일주를 할 수 있을까.", "Can one travel around the world by car without a single drop of oil?"),
    ("일본인 여행가 야마다 슈세이는 “가능하다”고 말한다.", "The Japanese traveler Yamada Shusei says, “It is possible.”"),
    ("그는 지난 이천칠 년부터 한 해 동안 폐식용유만을 이용한 바이오 디젤 자동차로 세계를 한 바퀴 돌았다.", "From 2007, for a year, he went once around the world in a biodiesel car that used only waste cooking oil."),
    ("이십일 일 녹색연합 주최로 서울 종로구 통인동 참여연대에서 열린 강연에서 야마다는 “폐식용유는 이산화탄소를 배출하지 않는 청정 에너지원”이라며 “바이오 디젤의 가능성을 전 세계에 알리고 싶어 세계 일주 프로젝트를 시작했다”고 말했다.", "At a lecture held on the 21st at the People’s Solidarity for Participatory Democracy in Tongin-dong, Jongno-gu, Seoul, hosted by the Green Korea United, Yamada said, “Waste cooking oil is a clean energy source that does not emit carbon dioxide,” and, “I started the round-the-world project because I wanted to tell the whole world about the possibility of biodiesel.”"),
    ("이십오 살에 오토바이로 사하라 사막을 종단한 오지 여행가 야마다가 처음부터 바이오 디젤을 신뢰한 것은 아니었다.", "Yamada, a traveler of remote regions who crossed the Sahara Desert by motorcycle at twenty-five, did not trust biodiesel from the start."),
    ("이천육 년 칠 월 바이오 디젤 제조기를 장착한 사륜 구동 차량을 타고 일본 남단 가고시마를 출발할 때만 해도 폐식용유가 자동차를 망가뜨리지는 않는지 한번 보자는 심정이었다.", "Even when he set out from Kagoshima, at the southern end of Japan, in July 2006 in a four-wheel-drive vehicle fitted with a biodiesel maker, he felt like seeing whether waste cooking oil would ruin the car."),
    ("바이오 디젤은 폐식용유, 유채꽃, 해바라기씨 등 식물에서 기름을 추출해 자동차 연료로 쓰는 경유 대체 에너지다.", "Biodiesel is an alternative to diesel that extracts oil from plants such as waste cooking oil, rapeseed flowers and sunflower seeds and uses it as car fuel."),
    ("바이오 디젤과 경유의 혼합 비율에 따라 바이오 디젤이 오 퍼센트 섞인 비디 오, 이십 퍼센트 섞인 비디 이십 등이 사용되는데, 야마다가 자동차에 사용한 것은 폐식용유 백 퍼센트, 비디 백이었다.", "Depending on the mixing ratio of biodiesel and diesel, BD5, with 5 percent biodiesel mixed in, BD20, with 20 percent, and so on are used, and what Yamada used in his car was 100 percent waste cooking oil, BD100."),
    ("이천칠 년 십이 월 일본을 출발해 캐나다와 미국을 거쳐 유럽, 중앙아시아, 러시아로 향했다.", "Leaving Japan in December 2007, he headed through Canada and the United States to Europe, Central Asia and Russia."),
    ("연료인 폐식용유는 현지에서 조달받았다.", "The fuel, waste cooking oil, was obtained locally."),
    ("가정집과 식당의 문을 두드려 폐식용유를 얻고, 자동차 안의 제조기로 디젤 연료로 바꿨다.", "He knocked on the doors of homes and restaurants to get waste cooking oil and turned it into diesel fuel with the maker inside the car."),
    ("못 쓰는 기름이 연료로 변신하는 과정을 보면서 사람들은 기꺼이 폐식용유를 부어 주었다.", "Watching the process in which oil that could not be used transformed into fuel, people willingly poured in their waste cooking oil."),
    ("한 번 가득 채우면 사백사십 리터. 주유 없이 삼천 킬로미터를 달릴 수 있었다.", "A full fill is 440 liters. He could run 3,000 kilometers without refueling."),
    ("튀김을 많이 먹는 남유럽에서는 폐식용유가 넉넉했지만, 식용유 값이 비싸 좀처럼 내버리지 않는 아프리카에선 연료 조달에 애를 먹었다.", "In southern Europe, where people eat a lot of fried food, waste cooking oil was plentiful, but in Africa, where cooking oil is expensive and hardly ever thrown away, he had a hard time obtaining fuel."),
    ("수은주가 영하 사십 도로 떨어지는 시베리아에선 애써 얻어온 식용유가 얼어붙는 바람에 발전기를 돌려 녹이느라 고생하기도 했다.", "In Siberia, where the mercury falls to forty degrees below zero, he also had trouble running a generator to melt the cooking oil he had worked to get, because it froze."),
    ("그러나 그는 “주유소는 없어도 사람은 있다. 사람이 있으면 기름을 얻을 수 있기 때문에 연료 걱정은 크게 하지 않았다”고 말했다.", "But he said, “There may be no gas stations, but there are people. If there are people, I can get oil, so I didn’t worry much about fuel.”"),
]
_SPEAK10C = [("대체 에너지 개발이 왜 중요한지, 환경 및 경제에 미치는 영향은 무엇인지 생각해 보고 옆 사람과 이야기해 보세요.", "Think about why developing alternative energy is important and what its effects on the environment and the economy are, and talk about it with the person next to you.")]
L6 = lesson(
    "U17 L10 · Part 3 (심화 학습): nuclear power and a round-the-world trip on waste oil",
    "심화 학습 · 원자력 · 원전 수출 · 방사성 폐기물 · 신성장동력 · 바이오 디젤 · 폐식용유 · 세계 일주 · 야마다 슈세이 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: an article on a nuclear-power event held in Seoul (Kyunghyang)", "The book asks: (1) what two things visitors can experience at the event; (2) the main difficulty in promoting nuclear power; (3) what triggered the change in Korea’s perception of nuclear power. The book gives the chairman’s age after his name, which I dropped, and writes the dates, “2010년”, “X레이” and “아랍에미리트(UAE)” in digits and Latin letters, which I spelled out (UAE is written 아랍에미리트). The article, with my English:", examples=passage(_NUC10)),
        card("My answers to 학습활동 2", "1. A: the principle of the X-ray, and how nuclear energy is used in real life. B: a model of the next-generation nuclear plant exported to the United Arab Emirates, to understand the process of producing nuclear energy at a glance. 2. How to inform the public accurately about the safety of radioactive waste disposal. 3. Winning the order for the nuclear plant in the United Arab Emirates: nuclear plants went from an unpopular facility to a new growth engine following cars and semiconductors."),
        card("학습활동 3: an article about a man who travelled the world without using a drop of oil (Kyunghyang)", "The book asks: (1) what Yamada used for the trip and what motivated him; (2) what biodiesel and BD100 are; (3) translate the underlined sentence into English (the underline is not marked in the text; every sentence below has my English, so use the one you think the book means); (4) where he had difficulty getting fuel and why. The book gives his age after his name, which I dropped; the figures (2007년, 21일, 25살, 2006년 7월, 5%, 20%, 100%, 440 ℓ, 3000 km, 영하 40도) are written in digits in the book, and BD5, BD20 and BD100 in Latin letters; I wrote them out in Hangul (비디 오, 비디 이십, 비디 백). The article, with my English:", examples=passage(_YAM10)),
        card("My answers to 학습활동 3", "1. A biodiesel car using only waste cooking oil; he wanted to tell the whole world about the possibility of biodiesel. 2. Biodiesel: an alternative to diesel in which oil is extracted from plants such as waste cooking oil, rapeseed flowers and sunflower seeds and used as car fuel. BD100: biodiesel made from 100 percent waste cooking oil. 4. A: Africa, because cooking oil is expensive and hardly ever thrown away. B: Siberia (the cooking oil he had obtained froze at forty below zero, and he had to run a generator to melt it); the book’s question is about getting fuel, and the text names Africa explicitly, so Siberia is my second guess."),
        card("말해 봅시다! (speaking)", "", examples=passage(_SPEAK10C)),
        card("Activities left out", "학습활동 1 (Listening, track 012): a promotional video by the chairman of the Korea Nuclear Culture Foundation: you answer in English what his evaluation of nuclear energy is, why he believes it will play a role in the country’s growth and what his plans are. 학습활동 4 (Listening, tracks 013 to 015): a commentary on eco-friendly cars (Donga) in three parts: you answer what problem the speaker points out (with specific numbers), why the government made the purchase of environment-friendly cars mandatory for all its agencies, what the world trends are for hybrid and hydrogen-powered cars, why the speaker feels frustrated about Korea’s present state and what the speaker’s main point is. They are audio."),
    ],
    exercises=uniq(
        _tr(_NUC10[1:], k=3) + _tr(_YAM10[2:], k=3)
        + [M("Who is quoted in the nuclear-power article?", "The chairman of the Korea Nuclear Culture Foundation", ["A farmer", "A taxi driver", "A pilot"], "이사장."), M("What principle can visitors experience at the event?", "The X-ray", ["The telescope", "The battery", "The radio"], "엑스레이."), M("What is the hardest part of promoting nuclear power?", "Informing the public accurately about the safety of radioactive waste disposal", ["Finding a venue", "Raising money", "Training pilots"], "방사성 폐기물 처리의 안전성."), M("What changed the perception of nuclear plants, according to the chairman?", "The order won from the United Arab Emirates", ["A new law", "A famous film", "A festival"], "수주."), M("What did Yamada’s car run on?", "Waste cooking oil", ["Gasoline", "Electricity", "Hydrogen"], "폐식용유."), M("What is BD100?", "Biodiesel made from 100 percent waste cooking oil", ["A diesel with 100 additives", "A car model", "A 100-liter tank"], "폐식용유 백 퍼센트."), M("Where did Yamada have trouble getting fuel because oil is expensive and rarely thrown away?", "Africa", ["Southern Europe", "Canada", "Russia"], "아프리카."), M("How far could a full tank of 440 liters take him?", "3,000 kilometers", ["30 kilometers", "300 kilometers", "30,000 kilometers"], "삼천 킬로미터.")]
        + [F("연료인 폐식용유는 현지에서 ___받았다. (to obtain)", "조달", ["혼합", "신뢰"], "조달하다."), F("사람들은 기꺼이 폐식용유를 ___ 주었다. (to pour)", "부어", ["돌려", "믿어"], "붓다."), F("아프리카에선 연료 조달에 ___을 먹었다. (a hard time)", "애", ["눈독", "발"], "애를 먹다."), F("폐식용유는 이산화탄소를 배출하지 않는 ___ 에너지원이다. (clean)", "청정", ["고성능", "비선호"], "청정."), F("원전이 비선호시설에서 신성장동력으로 ___했다. (rose rapidly)", "급부상", ["도약", "교체"], "급부상하다.")]
        + [read_q("원자력 홍보에서 가장 어려운 점은 방사성 폐기물 처리의 안전성이다"), read_q("폐식용유는 이산화탄소를 배출하지 않는 청정 에너지원이다"), read_q("석유 한 방울 없이 자동차로 세계 일주를 할 수 있을까"), read_q("주유소는 없어도 사람은 있다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("각광을 받다", "(脚光) to be in the spotlight; to be highly recognized; “to receive the spotlight”", "새로 출시된 스마트폰이 소비자들의 각광을 받고 있다."),
        ("대안", "(代案) an alternative (plan/idea)", "이 문제에 대해 좋은 대안이 떠오르지 않습니다."),
        ("도약(하다)", "(跳躍) leap; jump (to leap; to jump)", "앞으로 우리 경제는 신성장동력을 바탕으로 크게 도약을 할 것입니다."),
        ("신뢰(하다)", "(信賴) trust (to trust)", "사람과의 관계는 서로 신뢰를 바탕으로 해야 합니다.", "믿다"),
        ("원전", "(原電 or 原子力發電) nuclear power generation (the full form is 원자력발전)", ""),
    ]),
    ("학습활동 2", [
        ("꺼내 들다", "to take out and lift", "관광객들은 지도를 꺼내 들고 다음 목적지를 확인했다."),
        ("고무적이다", "(鼓舞的) to be encouraging", "이번 조사 결과는 우리에게 아주 고무적입니다."),
        ("관건", "(關鍵) a key; something crucial", "창업에서 성공은 맛과 가격의 경쟁력이 관건이다."),
        ("모형", "(模型) a model; a replica", "조각을 하기 전에 먼저 모형을 만들어 봤어요."),
        ("밀봉(하다)", "(密封) sealing up (to seal)", "포장이 끝나면 냄새가 새지 않게 꼭 밀봉해 주세요."),
        ("방사성", "(放射性) radioactivity", "식수에서 방사성 물질이 검출되었어요.", "방사능"),
        ("수주(하다)", "(受注) winning (a contract/project) (to win [a contract/project])", "세계 최고층 건물의 건축을 한국의 건설회사가 수주했다."),
        ("원리", "(原理) a principle; a fundamental", "이 기계가 작동하는 원리를 이해하지 못하겠습니다."),
        ("유일", "(唯一) one and only", "이 선생님의 유일한 아들이 크게 다쳐서 크게 놀라셨겠습니다.", "유일신"),
        ("이사장", "(理事長) the chairman of the board", ""),
        ("재단", "(財團) a foundation; an organization funded by an endowment", ""),
    ]),
    ("학습활동 3", [
        ("기꺼이", "willingly", "박 선생님이 부탁을 하시면 언제든 기꺼이 도와드리겠습니다."),
        ("돌리다", "to run; to operate; “to crank”", "전기가 나간 후 아파트 단지에서는 임시 발전기를 돌렸다."),
        ("망가뜨리다", "to break; to ruin", "형의 시계를 동생이 망가뜨려서 형이 화가 많이 났다."),
        ("사륜구동", "(四輪驅動) four-wheel drive", "", "전륜구동 / 이륜구동, 삼륜구동"),
        ("세계일주", "(世界一周) a trip around the world; a world tour", "나중에 돈을 많이 벌면 부모님을 모시고 세계일주를 하고 싶습니다."),
        ("시베리아", "Siberia", ""),
        ("식용유", "(食用油) cooking oil", "올리브로 만든 식용유가 건강에 좋다고 합니다."),
        ("애를 먹다", "to have a hard time; “to eat an anxiety”", "사원들이 협조해 주지 않아서 새로운 규칙을 시행하는 데 애를 먹었다."),
        ("오지", "(奧地) the outback; a remote area; backwoods", "저는 언젠가 오지를 탐험하고 싶습니다."),
        ("조달(하다)", "(調達) procurement; obtaining; raising; delivering (to obtain; to raise; to deliver)", "오지에 살면 물자 조달이 가장 큰 문제입니다."),
        ("청정", "(淸淨) clean and clear", "이 지역은 청정 호수로 유명합니다."),
        ("혼합(하다)", "(混合) mixture; blend (to mix; to blend)", "터키는 동서양의 문화가 혼합돼 있어서 아름답습니다."),
    ]),
    ("학습활동 4", [
        ("감세", "(減稅) tax reduction", "에너지 효율이 높은 가전 제품을 구입하면 감세 혜택이 있습니다."),
        ("고성능", "(高性能) high performance; high-powered", "고성능 폭탄. 고성능 스피커."),
        ("공공기관", "(公共機關) a public institution; a public organization", "에너지 절약을 위해 공공기관부터 에어컨을 끄기로 했습니다."),
        ("기존", "(旣存) existing", "기존 방법대로 하면 이 일을 성공할 수 없습니다."),
        ("대비(하다)", "(對備) preparation; provision (to prepare; to make provision)", "늘 전쟁 상황에 대비하고 있어야 한다."),
        ("정부 부처", "(政府 部處) a government department", ""),
        ("사활을 건 경쟁", "(死活 競爭) a serious competition", "업체들이 사활을 건 경쟁을 벌이고 있습니다."),
        ("세제혜택", "(稅制惠澤) tax benefits", "직원을 새로 고용하는 업체에는 세제혜택을 주기로 했습니다."),
        ("상용화(하다/되다)", "(商用化) commercialization (to commercialize/to be commercialized)", "수소연료전지차가 언제쯤 상용화될 수 있을까요?"),
        ("수소연료전지차", "(水素燃料電池車) a hydrogen fuel cell vehicle", ""),
        ("시판(하다/되다)", "(市販) selling at the market (to sell at the market/to be sold at the market)", "전기차가 얼마 전에 시판에 들어갔습니다.", "출시하다"),
        ("안타깝다", "to be regrettable; to be frustrated; to be heartbreaking; to be distressing", "그 학생은 열심히 공부하는데 성적이 오르지 않아 참 안타깝다."),
        ("외면하다", "(外面) to look away; to turn away; to avoid", "그 제품은 가격이 너무 높아 소비자들이 외면하고 있습니다."),
        ("일으키다", "to develop; to promote", "정부는 국가 경제를 다시 일으키기 위해 노력하고 있습니다."),
        ("한 발 늦다", "to come a bit late; to miss an opportunity; to fall a step behind", "제가 한 발 늦었군요. 사람들이 다 가고 없네요."),
        ("행동(하다)", "(行動) an act; an action; a behavior (to act; to behave)", "공공 장소에서는 그렇게 행동하지 마세요.", "행위"),
    ]),
]
L7 = lesson(
    "U17 L10 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 각광 · 대안 · 도약 · 신뢰 · 원전 · 고무적 · 관건 · 모형 · 밀봉 · 방사성 · 수주 · 원리 · 유일 · 이사장 · 재단 · 기꺼이 · 돌리다 · 망가뜨리다 · 사륜구동 · 세계일주 · 식용유 · 애를 먹다 · 오지 · 조달 · 청정 · 혼합 · 감세 · 고성능 · 공공기관 · 기존 · 대비 · 상용화 · 시판 · 안타깝다 · 외면 · 일으키다 · 행동",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 원전, 이사장, 재단, 사륜구동, 시베리아, 정부 부처 and 수소연료전지차. 방사성 has 방사능 (“radioactivity”) as a related word. The book lists 원전 and 원자력발전 together (原電 / 原子力發電), and writes “(정부)부처” with the parentheses, which I wrote as 정부 부처. The example of 고성능 is given by two phrases, 고성능 폭탄 and 고성능 스피커. 사륜구동 lists 전륜구동 (front-wheel drive) and, after the slash, 이륜구동, 삼륜구동 (two- and three-wheel drive) as related words. 모형 is glossed here “a model; a replica”, slightly differently from the same word in the previous lesson.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=22, nread=18)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 10: Alternative Energy (대체 에너지)", [L1, L2, L3, L4, L5, L6, L7])
