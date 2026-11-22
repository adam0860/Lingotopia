"""Unit 84: KBC Semester III, Unit 17, Lesson 9 - Science and Inventions (과학과 발명).
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
_MATCH9 = [("달성하다", "to achieve; to accomplish", "목표를 달성하다"), ("지배하다", "to rule; to dominate", "자동차 시장을 지배하다"), ("준공하다", "to complete construction", "빌딩을 준공하다"), ("개방하다", "to open", "자국의 시장을 개방하다"), ("보급하다", "to supply; to disseminate", "재료를 식당에 보급하다"), ("파악하다", "to grasp; to understand", "내용을 파악하다"), ("주목하다", "to pay attention", "선생님 말에 주목하다"), ("연결하다", "to connect; to link", "인터넷을 연결하다"), ("양산하다", "to produce in large quantity", "전자제품을 양산하다"), ("활성화하다", "to vitalize; to galvanize", "경제를 활성화하다")]
_HJ9 = [("動 동", "movement; vibration", "운동, 동력"), ("發 발", "sprouting; blooming", "발달, 발전소"), ("航 항", "ship", "결항, 항공기"), ("破 파", "break; destroy", "파괴, 돌파"), ("煙 연", "smoke; fog", "흡연, 연기")]
_HJW9 = [("운동", "exercise"), ("동력", "power; electric power"), ("발달", "development"), ("발전소", "a power station"), ("결항", "suspension (of flight/ship service); cancelling a flight or ship"), ("항공기", "an aircraft"), ("파괴", "destruction"), ("돌파", "a breakthrough"), ("흡연", "smoking"), ("연기", "smoke")]
_OPP9 = [("파괴", "건설", "destruction: construction"), ("발전", "후퇴", "development: retreat"), ("운항", "결항", "operation of a service: cancellation of a service"), ("금연", "흡연", "no smoking: smoking")]
_CAT9 = [("풍력, 수력, 원자력", "동력", "wind, water and nuclear power: power"), ("비행기, 항로, 조종사", "항공", "airplane, air route, pilot: aviation"), ("개발, 연구, 훈련", "발달", "development, research, training: my best guess"), ("방법, 계획, 방식", "전략", "method, plan, way: strategy")]
_L9X = [("태양광", "solar light"), ("대체 연료", "an alternative fuel"), ("수력", "water power"), ("풍력", "wind power"), ("원자력", "nuclear power"), ("에너지 전략", "an energy strategy"), ("기동", "mobility"), ("건설", "construction"), ("수동", "manual operation"), ("이동", "movement"), ("출시", "putting on the market"), ("호황", "a boom"), ("후퇴", "retreat"), ("유출", "an outflow"), ("운항", "operation (of a ship or flight)"), ("항로", "an air or sea route"), ("계기", "an opportunity; a trigger"), ("침체", "stagnation"), ("금연", "no smoking"), ("연료", "fuel"), ("금지", "a ban"), ("비행기", "an airplane"), ("조종사", "a pilot"), ("개발", "development"), ("연구", "research"), ("훈련", "training"), ("방법", "a method"), ("계획", "a plan"), ("방식", "a way; a style"), ("지능", "intelligence"), ("전략", "a strategy"), ("항공", "aviation")]
L1 = lesson(
    "U17 L9 · Review: science words and Sino-Korean 動 發 航 破 煙",
    "과학과 발명 · 단어 복습 · 한자어 복습 · 달성 · 지배 · 준공 · 개방 · 보급 · 파악 · 주목 · 연결 · 양산 · 활성화 · 動 發 航 破 煙",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives ten phrases with a verb underlined and asks you to connect each with its English meaning; the underline is not marked in the text, so the pairs below are my best reading (the verb of each phrase):", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH9], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ9], say=[2]), ktable(_HJW9)]),
        card("한자어 복습 1: the opposite word (my answers)", "Circle the word with the opposite meaning (A. 파괴: 기동, 건설, 수동, 이동; B. 발전: 출시, 호황, 후퇴, 유출; C. 운항: 항로, 계기, 침체, 결항; D. 금연: 연료, 금지, 연기, 흡연).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP9], say=[0, 1])]),
        card("한자어 복습 2: the word most closely related to the three words (my answers)", "Choose from the box (지능, 발달, 동력, 항공, 전략) the word most closely related to the words in each line:", tables=[table(["Words", "Answer", "Meaning"], [list(r) for r in _CAT9], say=[0, 1])]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 005): five spoken explanations about energy, each to be connected with solar power (태양광), an alternative fuel (대체 연료), water power (수력), wind power (풍력) or an energy strategy (에너지 전략). It is audio."),
        card("More words from these exercises", "", tables=[ktable(_L9X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH9], k=3) + _tr(_HJW9, k=3) + _tr(_L9X, k=4)
        + [M("What does the syllable 動 (동) mean?", "movement; vibration", ["sprouting", "ship", "smoke"], "동력."), M("What does the syllable 發 (발) mean?", "sprouting; blooming", ["movement", "ship", "break"], "발달."), M("What does the syllable 航 (항) mean?", "ship", ["movement", "sprouting", "break"], "항공기."), M("What does the syllable 破 (파) mean?", "break; destroy", ["ship", "smoke", "movement"], "파괴."), M("What does the syllable 煙 (연) mean?", "smoke; fog", ["ship", "break", "sprouting"], "흡연.")
           , M("Which word is the opposite of 파괴?", "건설", ["기동", "수동", "이동"], "Construction."), M("Which word is the opposite of 발전?", "후퇴", ["출시", "호황", "유출"], "Retreat."), M("Which word is the opposite of 운항?", "결항", ["항로", "계기", "침체"], "Cancellation."), M("Which word is the opposite of 금연?", "흡연", ["연료", "금지", "연기"], "Smoking."), M("Which word goes with 풍력, 수력, 원자력?", "동력", ["지능", "항공", "전략"], "Power."), M("Which word goes with 비행기, 항로, 조종사?", "항공", ["지능", "동력", "전략"], "Aviation."), M("Which word goes with 방법, 계획, 방식?", "전략", ["지능", "발달", "동력"], "Strategy.")
           , F("목표를 ___하다. (to achieve)", "달성", ["지배", "개방"], "달성하다."), F("자동차 시장을 ___하다. (to dominate)", "지배", ["달성", "준공"], "지배하다."), F("빌딩을 ___하다. (to complete construction)", "준공", ["개방", "연결"], "준공하다."), F("자국의 시장을 ___하다. (to open)", "개방", ["보급", "파악"], "개방하다."), F("전자제품을 ___하다. (to mass-produce)", "양산", ["주목", "연결"], "양산하다.")]
        + [read_q("목표를 달성하다"), read_q("자동차 시장을 지배하다"), read_q("자국의 시장을 개방하다"), read_q("경제를 활성화하다")]
    ),
)

# ================================================================== L2 Part 1
_ACR9 = [("태정태세문단세", "the chant for the first seven kings of the Chosun Dynasty"), ("월화수목금토일", "the chant for the seven days of the week")]
_PLUTO9 = [
    ("이천육 년 팔 월 이십사 일 천문학 역사에 남을 결정이 내려졌다.", "On August 24, 2006, a decision that will remain in the history of astronomy was made."),
    ("천문학의 국제적 조직인 국제천문연맹 총회에서 태양계의 행성의 정의가 처음으로 내려진 것이다.", "At the general assembly of the International Astronomical Union, the international organization of astronomy, a definition of the planets of the solar system was given for the first time."),
    ("그 결과, 태양계의 가장 바깥쪽에 있는 제구 행성 명왕성이 행성에서 제외되었다.", "As a result, Pluto, the ninth planet, which lies on the outermost side of the solar system, was excluded from the planets."),
    ("새로 설정된 왜소 행성으로 분류된 것이다.", "It was classified as the newly established dwarf planet."),
    ("오랫동안 행성으로 친하게 여겨졌던 명왕성이 행성에서 제외된 것은 충격적인 사건이었다.", "That Pluto, which had long been regarded familiarly as a planet, was excluded from the planets was a shocking “event”."),
    ("그 이유로, 명왕성이 다른 행성에 비해 상당히 작다는 점을 들 수 있다.", "As the reason, one can point out that Pluto is considerably small compared with the other planets."),
    ("명왕성의 적도 지름은 약 이천삼백 킬로미터.", "Pluto’s equatorial diameter is about 2,300 kilometers."),
    ("명왕성이 빠지면서 가장 작은 행성이 된 수성의 지름이 약 사천팔백팔십 킬로미터이므로, 명왕성은 그 절반 정도였다.", "Since the diameter of Mercury, which became the smallest planet when Pluto dropped out, is about 4,880 kilometers, Pluto was about half of that."),
    ("참고로 지구의 위성인 달의 지름은 삼천사백칠십육 킬로미터로, 명왕성은 달보다도 작은 것이다.", "For reference, the diameter of the Moon, the Earth’s satellite, is 3,476 kilometers, so Pluto is even smaller than the Moon."),
    ("둘째로는, 태양의 주위를 도는 궤도가 비정상적이라는 점이다.", "Second, its orbit around the sun is “abnormal”."),
    ("태양계 행성의 궤도는 완전하지는 않지만 대개 원에 가깝다.", "The orbits of the planets of the solar system are not perfect but mostly close to a circle."),
    ("그런데 명왕성의 궤도는 상당히 찌부러진 타원이다.", "But Pluto’s orbit is a considerably squashed oval."),
    ("더욱이 각 행성은 태양 주위를 돌 때, 대개 같은 하나의 평면 위를 지나고 있다.", "Moreover, when each planet goes around the sun, it mostly passes over the same single plane."),
    ("그러나 명왕성의 궤도만은 이 평면에서 극단적으로 벗어나 기울어져 있다.", "But only Pluto’s orbit is tilted, deviating extremely from this plane."),
    ("셋째로는 최근에 명왕성 가까이에서 명왕성에 필적하는 크기의 천체가 여럿 발견되었다는 점이다.", "Third, several heavenly bodies rivaling Pluto in size have recently been discovered near Pluto."),
]
_STEM9 = [
    ("버락 오바마 미국 대통령이 배아 줄기세포 연구에 연방정부의 재정지원을 허용하는 행정명령에 서명했다.", "US President Barack Obama signed an executive order allowing federal funding for embryonic stem cell research."),
    ("조지 부시 전 대통령은 이천일 년 팔 월 당시까지 이미 만들어진 배아 줄기세포를 이용한 연구에만 연방정부의 재정지원을 할 수 있도록 제한했다.", "Former President George Bush had limited federal funding to research using only the embryonic stem cells already made as of August 2001."),
    ("오바마 대통령은 이런 제한을 폐지한 것이다.", "President Obama has abolished this limit."),
    ("오바마는 “이념이 아니라 사실에 근거해 과학적 정책 결정을 내리겠다”고 덧붙였다.", "Obama added, “I will make scientific policy decisions based on facts, not ideology.”"),
    ("뉴욕 타임스는 십 일 “그동안 민간자금이나 주정부 지원만 받았던 줄기세포 연구에 연방자금이 지원돼 관련 연구가 영국과 아시아처럼 크게 활성화될 전망”이라고 보도했다.", "On the 10th, the New York Times reported, “With federal funds now supporting stem cell research that had only received private money or state-government support, related research is expected to be greatly invigorated, as in Britain and Asia.”"),
    ("오바마는 논란을 우려해, “인간 복제에는 절대 문을 열어 주지 않을 것”이라고 강조했다.", "Worrying about controversy, Obama stressed, “We will never open the door to human cloning.”"),
    ("과학계는 그동안 인간 배아 줄기세포 연구가 알츠하이머병 등 난치병 치료를 위해 필요하다고 밝혀 왔다.", "The scientific community has said all along that human embryonic stem cell research is necessary for treating intractable diseases such as Alzheimer’s."),
    ("이번 조처는 곧바로 논란을 불러일으켰다.", "This measure immediately stirred up controversy."),
    ("인간의 생명은 수정 순간부터 시작되므로, 인간 배아를 파괴하는 줄기세포 연구는 살인이라고 보수진영은 반발했다.", "The conservative camp objected that, since human life begins from the moment of fertilization, stem cell research that destroys human embryos is murder."),
    ("반면, 민주당 등은 인간의 고통을 덜어 주는 게 더 중요하다고 반박했다.", "On the other hand, the Democratic Party and others rebutted that relieving human suffering is more important."),
]
_SPEAK9A = [("세계적으로 또는 역사적으로 유명한 과학자의 이름을 서로 이야기해 보세요.", "Tell each other the names of scientists famous in the world or in history."), ("그 중 한 과학자를 선택하여 그의 업적과 공헌에 대해 한국말로 발표하세요.", "Choose one of them and give a presentation in Korean on his achievements and contributions.")]
L2 = lesson(
    "U17 L9 · Part 1 (도입 학습): Pluto and stem cell research",
    "도입 학습 · 알아봅시다 · 태정태세문단세 · 월화수목금토일 · 태양계 · 명왕성 · 왜소 행성 · 줄기세포 · 배아 · 오바마 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 (Let’s find out): Korean acronyms for a sequential list", "The book recalls Korean acronyms made of the initial syllables of a compound term, such as 외고 for 외국어 고등학교 (foreign language high school) and 과기대 for 과학기술대학교 (university of science and technology). They are often used in schools as memory aids and usually carry no literal meaning; students memorize them, often by chanting. Korean children chant 태정태세문단세 to remember the first seven kings of the Chosun Dynasty (태조, 정종, 태종, 세종대왕, 문종, 단종, 세조), which helps them remember that King Sejong, the creator of 한글, was the fourth king. Kindergartners chant 월화수목금토일 to remember the seven days of the week. Your teacher may introduce similar acronyms from other subjects.", examples=passage(_ACR9)),
        card("학습활동 2: an article about the planets of the solar system (edunet4u.net)", "The book asks: (1) what decision the IAU made; (2) the reasons for it; (3) a video about the area in which Korean elementary students surpass their Chinese and Japanese counterparts (left out). The text gives the abbreviation and the English name of the union in Latin letters (IAU: International Astronomical Union) and the English term “dwarf planet” beside 왜소 행성, which I dropped from the Korean; the dates and numbers are spelled in Hangul. The article, with my English:", examples=passage(_PLUTO9)),
        card("My answers to 학습활동 2", "1. The IAU gave a definition of the planets of the solar system for the first time, and as a result Pluto was removed from the planets and classified as a dwarf planet. 2. Pluto is considerably smaller than the other planets (its equatorial diameter is about 2,300 km, about half of Mercury’s and smaller than the Moon’s); its orbit around the sun is abnormal (a squashed oval, tilted far from the common plane of the other planets); and several heavenly bodies rivaling Pluto in size have been found near it."),
        card("학습활동 3: an article about the Obama administration’s support for embryonic stem cell research (Hankyoreh)", "The book asks: (1) compare the position of the Obama administration with that of the Bush administration; (2) summarize the differing opinions about the new decision. The newspaper’s name is printed between angle brackets, which I removed, and the dates are spelled in Hangul. The article, with my English:", examples=passage(_STEM9)),
        card("My answers to 학습활동 3", "1. The Bush administration limited federal funding to research using the embryonic stem cells already made as of August 2001; the Obama administration abolished this limit and allowed federal funding, saying it would base scientific policy on facts, not ideology, while never opening the door to human cloning. 2. Scientists say the research is needed to treat intractable diseases such as Alzheimer’s; the conservative camp objects that it is murder because life begins at fertilization; the Democratic Party and others reply that relieving human suffering is more important."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine; the book writes “achievements” and “contributions” in English after 업적 and 공헌, which I dropped):", examples=passage(_SPEAK9A)),
        card("Activities left out", "학습활동 1 (Listening, track 006): an edunet4u.net report on the top six promising future technologies, in which you fill an English table with the names and descriptions of the technologies: the book gives 정보 기술 (IT) as the example, then lists them as … 기술 (BT), … 기술 (NT) (“scientific technology that operates, analyzes and controls at the molecular and atomic level”), 우주항공 기술 (AT), … 기술 (ET) and … 기술 (CT) (“technologies that will develop digital, media-based cultural arts”). It is audio. 학습활동 2, task 3 (video, track 007): a YTN clip about the area in which Korean elementary students surpass their Chinese and Japanese counterparts, and why."),
    ],
    exercises=uniq(
        _tr(_PLUTO9, k=3) + _tr(_STEM9, k=3)
        + [M("Which planet was excluded from the planets in 2006?", "Pluto", ["Mercury", "Neptune", "Mars"], "명왕성."), M("What was Pluto classified as?", "A dwarf planet", ["A star", "A moon", "A comet"], "왜소 행성."), M("Which planet became the smallest when Pluto dropped out?", "Mercury", ["Venus", "Mars", "Earth"], "수성."), M("What shape is Pluto’s orbit, according to the article?", "A squashed oval", ["A perfect circle", "A straight line", "A square"], "찌부러진 타원."), M("What did Obama abolish?", "The limit on federal funding for embryonic stem cell research", ["The ban on human cloning", "The funding of space research", "The state-government support"], "제한을 폐지."), M("What did Obama promise never to do?", "Open the door to human cloning", ["Fund any research", "Follow scientists’ advice", "Talk to the press"], "인간 복제."), M("Why did the conservative camp object?", "They hold that life begins at fertilization and call embryo destruction murder", ["They dislike the cost", "They think it is too slow", "They support cloning"], "살인."), M("What does 월화수목금토일 help children remember?", "The seven days of the week", ["The seven kings", "The seven planets", "The seven seas"], "The chant.")]
        + [F("명왕성의 궤도는 상당히 찌부러진 ___이다. (an oval)", "타원", ["평면", "지름"], "타원."), F("명왕성의 적도 ___은 약 이천삼백 킬로미터이다. (diameter)", "지름", ["궤도", "행성"], "지름."), F("인간 배아를 파괴하는 줄기세포 연구는 살인이라고 보수진영은 ___했다. (to object)", "반발", ["허용", "서명"], "반발하다."), F("민주당 등은 인간의 고통을 덜어 주는 게 더 중요하다고 ___했다. (to rebut)", "반박", ["우려", "보도"], "반박하다.")]
        + [read_q("명왕성이 행성에서 제외되었다"), read_q("명왕성의 궤도는 상당히 찌부러진 타원이다"), read_q("오바마 대통령은 이런 제한을 폐지한 것이다"), read_q("월화수목금토일")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("나노", "nano; 1 billionth", "나노 기술"),
        ("무병장수", "(無病長壽) disease-free longevity; “long life with no disease”", "무병장수는 인류의 오랜 꿈입니다.", "만수무강"),
        ("발사체", "(發射體) a projectile", ""),
        ("복원(하다/되다)", "(復元 or 復原) restoration (to restore/to be restored)", "이천팔 년 화재로 타 버린 국보 제일 호 남대문이 원형대로 복원되고 있습니다."),
        ("분자", "(分子) a molecule", ""),
        ("원동력", "(原動力) a driving force; an impetus", "한국의 교육열이 경제발전의 가장 큰 원동력이다.", "동력"),
        ("원자", "(原子) an atom", ""),
        ("위성체", "(衛星體) a satellite (body)", ""),
        ("저감(하다)", "(低減) lowering and reduction (to lower and reduce)", "정부는 탄소 배출량은 저감시키기 위해 새 법안을 발표했습니다.", "낮추다, 줄이다"),
        ("제고(하다/되다)", "(提高) improvement; enhancement (to improve; to enhance/to be improved; to be enhanced)", "경제가 나빠지면서 기업들이 생산성을 제고하려고 노력하고 있다."),
        ("주도(하다/되다)", "(主導) leading (to lead/to be led)", "한국의 경제를 주도하는 것은 수출입니다."),
        ("질", "(質) quality", "제겐 질보다 양이 중요합니다. 많이만 주세요.", "양"),
        ("총칭(하다)", "(總稱) a general name; a collective term; a generic term (to name generically; to name generally)", "포유류는 사람, 고래, 쥐 등을 총칭하는 말입니다."),
        ("향상(하다/되다)", "(向上) improvement; progress (to improve/to be improved)", "한국인 친구 덕분에 제 한국어 실력이 많이 향상되었습니다."),
    ]),
    ("학습활동 2", [
        ("궤도", "(軌道) an orbit; a track", ""),
        ("극단적", "(極端的) extreme; radical", "그의 생각은 너무 극단적입니다."),
        ("금성", "(金星) Venus", ""),
        ("명왕성", "(冥王星) Pluto", ""),
        ("모자라다", "to be short of", "손님이 너무 많이 와서 음식이 모자라요.", "부족하다 / 남다, 넘치다, 충분하다"),
        ("목성", "(木星) Jupiter", ""),
        ("무려", "(無慮) as much/many as (referring to a great amount or number)", "그 인기 가수의 공연에 입장권이 무려 이천 장이나 팔렸대요."),
        ("수성", "(水星) Mercury", ""),
        ("왜소 행성", "(矮小 行星) a dwarf planet", ""),
        ("외우다", "to memorize", "영어 단어를 외우는 것이 너무 어렵습니다.", "암기하다"),
        ("적도", "(赤道) the equator; “red way”", ""),
        ("정의(하다)", "(定義) definition (to define)", "행복의 정의는 사람마다 다릅니다."),
        ("지구", "(地球) the Earth; “sphere of earth”", ""),
        ("지름", "diameter", "", "직경 / 반지름, 반경"),
        ("찌부러지다", "to be crushed; to be warped", "축구공이 바람이 다 빠져서 완전히 찌부러졌다."),
        ("천문학", "(天文學) astronomy; “study of the sky”", "", "점성술"),
        ("천왕성", "(天王星) Uranus", ""),
        ("천체", "(天體) a heavenly body; a celestial body", "천체망원경"),
        ("총회", "(總會) a general assembly; a plenary session", ""),
        ("충격적", "(衝擊的) shocking", "이 사건은 정말 충격적입니다."),
        ("타원", "(楕圓) an oval", ""),
        ("태양계", "(太陽系) the solar system", "태양계에는 몇 개의 행성이 있습니까?", "은하계"),
        ("토성", "(土星) Saturn", ""),
        ("평면", "(平面) a plane; flat (surface)", "평면 티브이"),
        ("필적하다", "(匹敵) to equal; to rival; to be equal to", "현 유에프씨 헤비급 챔피언은 대단히 강해서 필적할 상대가 없다."),
        ("해왕성", "(海王星) Neptune", ""),
        ("행성", "(行星) a planet; “moving star”", "우주에 우리 지구처럼 생명이 존재하는 행성이 또 있을까요?", "별"),
        ("호흡(하다)", "(呼吸) a breath (to breathe)", "환자의 호흡이 정상으로 돌아왔습니다."),
        ("화성", "(火星) Mars", ""),
    ]),
    ("학습활동 3", [
        ("논란", "(論難) a controversy", "이 영화는 논란의 중심에 있습니다."),
        ("덜어 주다", "to relieve", "친구의 따뜻한 말이 제 고민을 덜어 주었어요."),
        ("반박(하다)", "(反駁) verbal refutation; retort; rebuttal (to retort)", "그 사람의 말은 반박의 여지가 없습니다."),
        ("반발(하다)", "(反撥) a backlash; repulsion (to repulse; to resist; to oppose)", "시간이 가면서 사람들의 반발이 거세지고 있습니다."),
        ("배아", "(胚芽) an embryo", ""),
        ("보수진영", "(保守陣營) the conservative side/camp", "보수진영에서는 줄기세포연구를 반대하고 있습니다.", "보수파 / 진보진영, 진보파"),
        ("복제(하다/되다)", "(複製) cloning; “duplicate making” (to clone/to be cloned)", "이 비디오는 불법 복제되었습니다."),
        ("줄기세포", "(細胞) a stem cell", ""),
        ("허용(하다/되다)", "(許容) permission (to permit; to allow/to be permitted; to be allowed)", "자동차 배기가스 배출량이 허용치를 넘어섰습니다."),
    ]),
]
L3 = lesson(
    "U17 L9 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 나노 · 무병장수 · 복원 · 분자 · 원동력 · 원자 · 저감 · 제고 · 주도 · 총칭 · 향상 · 궤도 · 금성 · 명왕성 · 목성 · 수성 · 화성 · 토성 · 천왕성 · 해왕성 · 지구 · 태양계 · 행성 · 타원 · 논란 · 반박 · 반발 · 배아 · 보수진영 · 복제 · 허용",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 발사체, 분자, 원자, 위성체, 궤도, the planet names, 왜소 행성, 적도, 지구, 지름, 천문학, 천왕성, 총회, 타원, 배아 and 줄기세포. In the book the planet names and 지구 are the whole list of the solar system: 수성 (Mercury), 금성 (Venus), 지구 (Earth), 화성 (Mars), 목성 (Jupiter), 토성 (Saturn), 천왕성 (Uranus), 해왕성 (Neptune) and 명왕성 (Pluto). 복원(하다/되다) has two possible Hanja, 復元 or 復原. 분자 has a homonym 分子, “a numerator”. 천문학 has 점성술 (“astrology”) as a related word. The related words with a slash separate the similar words (before the slash) from the opposite words (after it), as in the book: 부족하다 / 남다, 넘치다, 충분하다; 직경 / 반지름, 반경; 보수파 / 진보진영, 진보파. The book writes 2008년, 1호 and 2천 장 in digits, and the examples of 평면 and 필적하다 have TV and UFC in Latin letters; I spelled them in Hangul. The book’s example of 저감하다 has 배출량은 where 배출량을 is meant.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=20, nread=16)),
)

# ================================================================== L4 Part 2
_INV9 = [
    ("백구십 도까지 찍히는 어안렌즈", "A fish-eye lens that shoots up to 190 degrees"),
    ("어안렌즈.", "The fish-eye lens."),
    ("물고기가 바라본 세상과 비슷하다고 해서 이름 붙여진 어안렌즈는 사람의 시야각인 백오십 도보다 삼십 도나 더 넓은 백팔십 도까지 볼 수 있어요.", "The fish-eye lens, so named because it resembles the world seen by a fish, can see up to 180 degrees, as much as 30 degrees wider than the human viewing angle of 150 degrees."),
    ("그런데 이번에 발명된 어안렌즈는 기존의 어안렌즈보다 시야각이 십 도나 더 커져 백구십 도까지 볼 수 있다고 하니, 더 넓은 세상을 담을 수 있겠죠?", "But the newly invented fish-eye lens has a viewing angle as much as 10 degrees larger than the existing ones and can see up to 190 degrees, so it can hold a wider world, right?"),
    ("또, 이 어안렌즈는 카메라뿐만 아니라 씨씨티브이, 휴대폰, 무인항공기, 스포츠 경기장 등 다양한 곳에서 활용할 수 있을 거라고 기대되고 있대요.", "Also, this fish-eye lens is expected to be usable not only in cameras but in various places such as CCTV, cell phones, unmanned aircraft and sports stadiums."),
    ("이만하면 나처럼 사진 찍기를 좋아하는 사람들에게 최고의 발명품이라고 할 수 있겠죠?", "Given this much, it can be called the best invention for people who like taking photos, like me, right?"),
    ("손가락에 끼우고 사용하는 미니 마우스", "A mini mouse you wear on your finger"),
    ("발명특허대전에는 저의 눈길을 확 사로잡는 제품이 있었어요.", "At the Invention and Patent Expo there was a product that caught my eye at once."),
    ("바로 손가락 움직임만으로 커서를 움직일 수 있는 미니 마우스.", "It was the mini mouse with which you can move the cursor with just the movement of a finger."),
    ("손가락 하나 굵기만한 이 제품에는 좌우 클릭 버튼과 휠이 달려 있어, 손가락에 끼운 후 손가락을 움직이기만 하면 편하게 사용할 수 있어요.", "This product, as thick as one finger, has left and right click buttons and a wheel attached, so once you put it on your finger you can use it comfortably just by moving your finger."),
    ("무선 마우스와 기본 원리는 같지만 손가락으로 가리키면 커서가 이동하고, 톡톡 두드리면 더블 클릭이 되니, 손가락 하나로 우아하게 노트북을 쓸 수 있죠.", "Its basic principle is the same as a wireless mouse, but the cursor moves when you point with your finger and a double click happens when you tap, so you can use a laptop elegantly with one finger."),
    ("공간을 차지하지 않는 스피커는?", "A speaker that takes up no space?"),
    ("발명특허대전에 출시된 획기적인 스피커는 내 고민을 확 날려 주었어요.", "The groundbreaking speaker put on the market at the Invention and Patent Expo blew my worries away."),
    ("얇고 투명한 필름 형태를 하고 있는 이 스피커는 두께가 영 점 영팔 밀리미터밖에 되지 않아서 거의 공간을 차지하지 않아요.", "This speaker, in the form of a thin, transparent film, is only 0.08 millimeters thick, so it takes up almost no space."),
    ("게다가 투명한 재질이라 거울이나 액자 등 다른 제품과 결합해 쓸 수도 있고, 예쁜 외관 덕분에 디자인 소품으로도 활용할 수 있지요.", "Besides, because the material is transparent, it can be combined with other products such as mirrors or picture frames, and thanks to its pretty appearance it can also be used as a design accessory."),
    ("더군다나 소리 나는 필름은 제조과정도 간단해 저렴하기까지 하니, 정말 대박 아이템이죠?", "What’s more, the sound-making film is even cheap because its manufacturing process is simple, so it is truly a jackpot item, isn’t it?"),
    ("기자의 주장", "The reporter’s claim"),
    ("조그맣고 귀여운 모습 때문에 성능이 떨어질 것 같다고?", "Do you think its performance must be poor because of its small, cute look?"),
    ("천만의 말씀.", "Not at all."),
    ("무선 통신으로 더 먼 거리에서도 정교하게 움직일 수 있거든.", "Because with wireless communication it can move precisely even from a farther distance."),
    ("디자인과 성능, 두 마리 토끼를 모두 잡은 최고의 발명품이지.", "It is the best invention, catching both rabbits, design and performance."),
]
_FALL9 = [("A", "비행기가 바다에 떨어져서 사상자가 많이 발생했다.", "to fall"), ("B", "여자 친구랑 오래 떨어져 있어서 사랑이 식었어요.", "to be apart; to be away from"), ("C", "계속 오르던 기름값이 조금 떨어지고 있습니다.", "to drop (prices)"), ("D", "차에 기름이 거의 다 떨어졌네요. 주유소로 갑시다.", "to run out"), ("E", "대학입학시험에 떨어졌어요. 재수를 할 겁니다.", "to fail (an exam)"), ("F", "그 가게의 물건들은 값은 싸지만 질이 떨어집니다.", "to be inferior; to decline (in quality)"), ("G", "잠을 많이 잤더니 감기가 떨어졌어요.", "to go away; to be cured (a cold)")]
_SPEAK9B = [("지금까지 나온 중요한 발명품들로는 어떤 것들이 있는지 서로 이야기해 보세요.", "Tell each other what important inventions have come out so far."), ("그 중 가장 훌륭하다고 생각하는 것을 한 가지만 골라서 그 이유와 함께 발표해 보세요.", "Choose just one that you think is the best of them and present it with your reason.")]
L4 = lesson(
    "U17 L9 · Part 2 (본 학습): three new inventions",
    "본 학습 · 어안렌즈 · 미니 마우스 · 필름 스피커 · 발명특허대전 · 시야각 · 무선 · 투명 · 떨어지다 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a science-magazine article on three new inventions (edunet4u.net)", "The book asks: (1) summarize the unique features of each invention; (2) which does the reporter consider the best, and what clues help you decide; (3) pick one and present it to the class as if you were its inventor (you may draw it and add details); (4) which sentence matches the underlined 떨어지다 and the English meaning of each. In the text “!” and “~” and “?” follow some words (어안렌즈!, 확~, 천만의 말씀!): I changed “!” to a period and dropped “~”, and degrees and millimeters are spelled in Hangul (CCTV is 씨씨티브이). The article, with my English:", examples=passage(_INV9)),
        card("My answers to 학습활동 1, tasks 1 and 2", "1. Fish-eye lens: a viewing angle up to 190 degrees (10 degrees more than existing fish-eye lenses and wider than the human 150), usable in cameras, CCTV, cell phones, unmanned aircraft and stadiums. Mini mouse: worn on one finger, with left and right click buttons and a wheel; the cursor follows the finger, a tap gives a double click; wireless. Speaker: a thin transparent film only 0.08 mm thick, takes almost no space, can be combined with mirrors and frames, usable as decoration, simple and cheap to make. 2. The reporter considers the mini mouse the best: the “reporter’s claim” answers the doubt that its small, cute shape means poor performance, and says that wireless communication lets it move precisely even from far away, “catching both rabbits, design and performance”; this follows the description of the mini mouse."),
        card("4. 떨어지다: the seven sentences and my answers", "The underlined word of the reporter’s claim is 성능이 떨어질 것 같다 (the performance seems to drop). It matches sentence F (quality is inferior). The meanings of each 떨어지다 are my answers:", tables=[table(["", "Sentence", "떨어지다 means (my answer)"], [list(r) for r in _FALL9], say=[1])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK9B)),
        card("Activities left out", "학습활동 2 (Listening, track 008): a YTN news item on Korea’s Invention and Patent Expo: you fill a table about the technology that won first prize (the capability and shortcoming of existing fish-eye lenses and the new technology developed by Honam University), say how the first interviewee, Professor Kyungil Kwon, says the new technology can be used in daily life, and what help a person with innovative ideas can find at the expo. 학습활동 3 (Listening, track 009): a YTN video on adult stem cells: you answer what the narrator says about them, what the interviewee’s restaurant analogy refers to and the advantages of adult stem cells. They are audio and video."),
    ],
    exercises=uniq(
        _tr(_INV9[1:], k=3)
        + [M("How wide a view can the new fish-eye lens take?", "190 degrees", ["150 degrees", "180 degrees", "100 degrees"], "백구십 도."), M("Which device does the mini mouse move?", "The cursor", ["The speaker", "The screen", "The camera"], "커서."), M("What does a tap give on the mini mouse?", "A double click", ["A scroll", "A shutdown", "A photo"], "더블 클릭."), M("How thick is the film speaker?", "0.08 millimeters", ["8 millimeters", "0.8 millimeters", "80 millimeters"], "영 점 영팔."), M("What can the film speaker be combined with?", "Mirrors or picture frames", ["Cars", "Cooking pots", "Shoes"], "거울이나 액자."), M("Which invention does the reporter praise as catching both rabbits?", "The mini mouse", ["The fish-eye lens", "The film speaker", "All of them equally"], "두 마리 토끼."), M("In the sentence “성능이 떨어질 것 같다”, what does 떨어지다 mean?", "To be inferior; to decline", ["To fall down", "To run out", "To fail an exam"], "질이 떨어집니다.")]
        + [F("손가락 움직임만으로 ___를 움직일 수 있는 미니 마우스. (a cursor)", "커서", ["필름", "스피커"], "커서."), F("얇고 ___한 필름 형태를 하고 있는 스피커. (transparent)", "투명", ["우아", "정교"], "투명하다."), F("무선 통신으로 더 먼 거리에서도 ___하게 움직일 수 있다. (precisely)", "정교", ["우아", "획기적"], "정교하다."), F("그 스피커는 ___인 제품이다. (groundbreaking)", "획기적", ["극단적", "충격적"], "획기적.")]
        + [read_q("손가락 움직임만으로 커서를 움직일 수 있다"), read_q("얇고 투명한 필름 형태를 하고 있는 스피커"), read_q("디자인과 성능, 두 마리 토끼를 모두 잡은 최고의 발명품이지"), read_q("지금까지 나온 중요한 발명품들")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("굵기", "thickness", "파를 같은 굵기로 좀 썰어 주세요."),
        ("눈길을 사로잡다", "to catch someone’s eyes; to attract (a person’s) attention; “arrest the line of vision”", "이 제품은 출시되자마자 사람들의 눈길을 사로잡았습니다.", "시선을 끌다"),
        ("대박", "a jackpot; a big fortune", "새 영화가 꼭 대박나길 바래요."),
        ("무선", "(無線) wireless", "저희 카페에서는 손님들에게 무선 인터넷 서비스를 제공하고 있습니다.", "유선"),
        ("무인항공기", "(無人航空機) unmanned aircraft", ""),
        ("성능", "(性能) capacity; performance", "이 제품이 가격 대비 성능 면에서 최고입니다."),
        ("소품", "(小品) a trivial article; a prop", "인테리어 소품 수집이 제 취미입니다."),
        ("시야각", "(視野角) “visibility angle”", ""),
        ("액자", "(額子) a frame (for a picture/photo)", "사진이 많이 상했어요. 액자에 넣어 둡시다."),
        ("어안렌즈", "(魚眼) a fish-eye camera lens", ""),
        ("외관", "(外觀) (outward) appearance", "사람을 외관으로만 판단해서는 안 됩니다.", "내관"),
        ("우아하다", "(優雅) to be elegant", "그분은 항상 우아하게 말씀하십니다."),
        ("정교하다", "(精巧) to be exquisite", "이 조각품은 정말 정교한 솜씨로 만들어졌습니다."),
        ("출시(하다/되다)", "(出市) putting out (a product in the market) (to put [something] out in the market/[something] to be put on the market for sale)", "신형 아이패드가 언제 출시됩니까?"),
        ("커서", "a (blinking) cursor", ""),
        ("투명하다", "(透明) to be transparent", "저도 투명한 피부를 갖고 싶어요.", "불투명, 반투명"),
        ("획기적", "(劃期的) groundbreaking; epochal; momentous", "전기의 발명은 인간의 생활에 획기적인 변화를 가져왔다."),
        ("휠", "a wheel", ""),
    ]),
    ("학습활동 2", [
        ("각도", "(角度) angle", "헤드라이트의 각도가 맞지 않아 라이트를 켜도 잘 안 보입니다."),
        ("수상작", "(受賞作) award-winning work", "이 사진은 퓰리처상 수상작입니다."),
        ("복원(하다/되다)", "(復元) restoration (to restore/to be restored)", "지금 남대문 복원작업이 한창입니다.", "복구"),
        ("영상", "(映像) an image; a picture", "이 영화는 영상이 아주 아름답습니다."),
        ("왜곡(하다/되다)", "(歪曲) distortion (to distort/to be distorted)", "제 뜻을 왜곡하지 말아 주세요."),
        ("출원", "(出願) registering (a patent)", ""),
        ("특허", "(特許) a patent", ""),
    ]),
    ("학습활동 3", [
        ("골수", "(骨髓) bone marrow", ""),
        ("냉면", "(冷麵) a cold Korean noodle dish", ""),
        ("뇌경색", "(腦梗塞) cerebral infarction", ""),
        ("미량", "(微量) a small amount", "이 독성은 미량이라도 인체에 치명적입니다.", "소량"),
        ("버거(씨) 병", "(病) Buerger’s Disease; inflammation of arteries and veins", ""),
        ("분화(하다/되다)", "(分化) division (of a cell) (to divide/to be divided)", "직업의 종류가 세밀하게 분화되고 있습니다."),
        ("성체줄기세포", "(成體 細胞) an adult stem cell", ""),
        ("임상치료", "(臨床治療) a clinical treatment", ""),
        ("탯줄", "an umbilical cord", ""),
        ("혈액", "(血液) blood", "먼저 혈액검사를 해 봅시다.", "피, 혈압, 혈당, 수혈"),
    ]),
]
L5 = lesson(
    "U17 L9 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 굵기 · 눈길을 사로잡다 · 대박 · 무선 · 무인항공기 · 성능 · 소품 · 시야각 · 액자 · 어안렌즈 · 외관 · 우아하다 · 정교하다 · 출시 · 커서 · 투명하다 · 획기적 · 휠 · 각도 · 수상작 · 복원 · 영상 · 왜곡 · 출원 · 특허 · 골수 · 뇌경색 · 미량 · 분화 · 성체줄기세포 · 임상치료 · 탯줄 · 혈액",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 무인항공기, 시야각, 어안렌즈, 커서, 휠, 출원, 특허, 골수, 냉면, 뇌경색, 버거(씨) 병, 성체줄기세포, 임상치료 and 탯줄. 영상 has a homonym 零上, “above the freezing temperature”. The related words with commas are as in the book (불투명, 반투명 for 투명하다; 피, 혈압, 혈당, 수혈 for 혈액). In the book 신형 아이패드 is in the example of 출시; 휠 is the loan word for “wheel” and 커서 for “cursor”. For 버거(씨) 병 the book gives only 病 (disease) in Hanja, since the first part is a name. The book spaces 가져 왔다 in the example of 획기적, which I joined.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=16, nread=14)),
)

# ================================================================== L6 Part 3
_INVT9 = [("측우기", "a rain gauge (a canister that measures rainfall)"), ("수표", "a water gauge (a calibrated stone column measuring the water in a river or stream)"), ("거북선", "the Turtle Ship (a large warship of the Goryo and Chosun dynasties)"), ("임진왜란", "the Imjin War, the Japanese invasion of 1592 to 1598"), ("금속활자", "movable metal type"), ("상정고금예문", "a set of ritual books printed with the first movable type (1234)"), ("직지심경", "Jikji, a Buddhist text printed in 1377, the oldest surviving book printed with movable type"), ("한글", "the Korean phonetic writing system")]
_EMB9 = [
    ("배아 복제의 문제는 배아를 인간으로 보느냐 아니면 그냥 세포로만 보느냐의 관점에 따라 달라진다.", "The problem of embryo cloning differs according to whether one sees the embryo as a human being or just as a cell."),
    ("많은 과학자들은 인류의 건강 증진과 의학 발전을 위해 인간 배아 복제 기술을 제한적으로 허용해야 한다며 배아는 기관으로 분화하지 않은 상태이기 때문에 그냥 하나의 세포로 보면 된다고 주장한다.", "Many scientists argue that human embryo cloning technology should be allowed in a limited way for the improvement of human health and the advance of medicine, and that an embryo, being in a state that has not differentiated into organs, can simply be seen as a single cell."),
    ("그러나 일부 과학자들과 시민 단체, 종교계에서는 배아도 잠재적인 인간이기 때문에 이러한 세포를 실험에 사용한다는 것은 엄연한 인간성에 대한 도전이라고 주장하고 있다.", "However, some scientists, civic groups and the religious world argue that, since an embryo is also a potential human being, using such cells in experiments is a clear challenge to humanity."),
    ("종교지도자들, 사회학자들, 인권론자들과 일부 과학자들은 배아복제에 대해 반대하는 의견을 가지고 있다.", "Religious leaders, sociologists, human-rights activists and some scientists hold opinions against embryo cloning."),
    ("정자와 난자가 만나 수정란이 된 직후부터 이미 생명은 시작되었다고 볼 수 있으며, 인간의 배아를 함부로 다루는 것은 심각한 인권 침해에 해당한다고 주장한다.", "They argue that life can be seen as having already begun right after the sperm and egg meet and become a fertilized egg, and that handling human embryos carelessly amounts to a serious violation of human rights."),
    ("인간 배아 복제기술이 개체복제를 의미하는 것이 아니지만, 이 기술은 잠재적인 위험을 내포하고 있다.", "Although human embryo cloning technology does not mean the cloning of an individual, this technology carries a potential danger."),
    ("배아 복제가 인간개체 복제로 이어졌을 경우 그 파장은 이루 말할 수 없이 크다.", "If embryo cloning leads to the cloning of a human individual, the repercussions are indescribably large."),
    ("개인적인 정체성의 문제뿐만이 아니라 가정 파괴 및 사회 혼란 등 현재 예상 가능한 문제들만 하더라도 헤아릴 수 없이 많다.", "Not only problems of personal identity but also the family breakdown and social confusion and other problems that can be foreseen even now are innumerable."),
    ("생명과학기술의 발달은 인류의 손에 인간의 생명을 조작할 수 있는 기술을 쥐어 주었다.", "The development of life-science technology has put into humankind’s hands the technology to manipulate human life."),
    ("비록 배아 복제의 기술이 인류에게 가져올 크나큰 혜택이 있음에 분명하더라도, 그것이 미칠 사회적 윤리적 중요성을 생각할 때 사회 여러 분야의 동의와 합의 하에 진행되어야 할 것이다.", "Even if the embryo cloning technology will clearly bring great benefits to humankind, considering the social and ethical importance it will have, it should proceed with the consent and agreement of various fields of society."),
]
_PH9 = [("정자와 난자가 만나 수정란이 된 직후부터 이미 생명은 시작되었다", "Life has already begun right after the sperm and egg meet and become a fertilized egg", "(b), the second paragraph"), ("배아 복제가 인간개체 복제로 이어졌을 경우 그 파장은 이루 말할 수 없이 크다", "If embryo cloning leads to the cloning of a human individual, the repercussions are indescribably large", "(c), the third paragraph"), ("인류의 건강 증진과 의학 발전을 위해 인간 배아 복제 기술을 제한적으로 허용해야 한다", "Human embryo cloning technology should be allowed in a limited way for the improvement of human health and the advance of medicine", "(a), the first paragraph")]
_SPEAK9C = [("앞으로 어떤 새로운 발명품이 나왔으면 좋겠는지 서로 이야기해 보세요.", "Tell each other what new inventions you hope will come out in the future."), ("과학과 기술의 발달이 인간에게 미친 좋은 영향과 나쁜 영향에 대해서 서로 이야기해 보세요.", "Tell each other about the good and bad effects that the development of science and technology has had on humans."), ("생활에 도움이 된 작거나 유용한 발명품에 대해 생각해 보고 한국말로 반 친구들에게 설명하세요.", "Think about small, useful inventions that have helped your daily life and describe them to your classmates in Korean.")]
L6 = lesson(
    "U17 L9 · Part 3 (심화 학습): Korean inventions and human embryo cloning",
    "심화 학습 · 알아봅시다 · 측우기 · 수표 · 거북선 · 금속활자 · 직지심경 · 한글 · 배아 복제 · 찬반 · 인권 침해 · 정체성 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다 (Let’s find out): Korean inventions in history", "Korea is a leader in modern science and technology, and Korean inventions have bettered people’s lives throughout history. The book presents four examples: (1) 측우기 and 수표 (rain gauge and water gauge), invented by the scientist and astronomer Jang Young-shil in the reign of King Sejong of the Chosun Dynasty to help agriculture, which depended heavily on irrigation in droughts; (2) 거북선 (the Turtle Ship), a large warship of the Royal Korean Navy in the Goryo and Chosun dynasties, especially important in the 1592 to 1598 Imjin War against the invading Japanese navy; its design is credited to Admiral Lee Soon-shin, and its deck was covered with iron spikes and a dragon’s head mounted on the bow; (3) 금속활자 and 직지심경 (movable type and Jikji): the world’s first movable-type printing was invented in the Goryo Dynasty in 1234, supposedly printing a set of ritual books (상정고금예문), examples of which are shown in the Library of Congress; Jikji, about Buddhism, is the oldest surviving book, printed in 1377, designated a World Cultural Heritage by UNESCO in 2001 (precedes the Gutenberg Bible by 78 years, kept in the National Museum of France); (4) 한글, the phonetic writing system invented by scholars commissioned by Sejong the Great, which most Koreans consider the most important invention in Korean history: in a 2003 Ministry of Science and Technology survey, 80% named 한글, followed by 금속활자 (9%), 거북선 (6%) and 측우기 (3%); in 2010 an Indonesian tribe officially adopted 한글 to write its language.", tables=[ktable(_INVT9)]),
        card("학습활동 2: a text on the pros and cons of human embryo cloning (edunet4u.net)", "In the book’s text three phrases are cut out (marked ⒜, ⒝, ⒞) and listed in a table: you translate each and match it with its place. Here is the text with the phrases put back in their places by my matching (the first, in the opening paragraph, is the scientists’ view; the second in the paragraph of the opponents; the third after the sentence about the potential danger):", examples=passage(_EMB9)),
        card("The three missing phrases (my translation and matching)", "", tables=[table(["Missing phrase", "English", "Place (my matching)"], [list(r) for r in _PH9], say=[0])]),
        card("My answers to 학습활동 2", "2. The conclusion: even if embryo cloning technology will clearly bring great benefits to humankind, it should proceed with the consent and agreement of various fields of society, considering its social and ethical importance. 3. (Debate: one group the pros, one group the cons, using the passage’s points and your own ideas.)"),
        card("말해 봅시다! (speaking)", "The book’s two speaking prompts and the task 3 of 학습활동 3 (the English is mine):", examples=passage(_SPEAK9C)),
        card("Activities left out", "학습활동 1 (Listening, track 010): an expert explains the movable type printing press invented separately in Korea and Germany: you choose the speaker’s tone toward Korean inventions (A. condescending, B. objective, C. regretful, D. persuasive) and fill an English table comparing the year of invention, the inventor, the printed material and the records and data of the Korean and German inventions. 학습활동 3 (Listening, tracks 011 and 012): an interview with a high-school student inventor: you write his general information, summarize his answers to five questions (his interests and extracurricular activities, how many times he won invention contests, his most memorable invention, his motivation for college and his plan for the future; the book gives the start of two answers: “I was interested in radios and motors” and “I want to go to college to gain theoretical knowledge about the things I have invented in the past 3 years”). They are audio."),
    ],
    exercises=uniq(
        _tr(_EMB9, k=3) + _tr(_INVT9, k=3)
        + [M("What does 측우기 measure?", "Rainfall", ["Wind speed", "Temperature", "Time"], "Rain gauge."), M("Who is credited with the design of the Turtle Ship?", "Admiral Lee Soon-shin", ["King Sejong", "Jang Young-shil", "Gutenberg"], "The hero admiral."), M("In what year was Jikji printed?", "1377", ["1234", "1592", "2001"], "Oldest surviving movable-type book."), M("Which invention did most Koreans name in the 2003 survey?", "한글", ["금속활자", "거북선", "측우기"], "80%."), M("How do many scientists say the embryo should be seen?", "As a single cell not yet differentiated into organs", ["As a full human being", "As a machine", "As a tissue sample only"], "하나의 세포."), M("What do opponents say begins right after fertilization?", "Life", ["Cloning", "A disease", "A law"], "생명."), M("What does the passage conclude?", "The technology should proceed with the consent and agreement of various fields of society", ["The technology must be banned", "The technology needs no discussion", "Only scientists should decide"], "동의와 합의 하에."), M("Which phrase belongs in the first paragraph, by my matching?", "Embryo cloning technology should be allowed in a limited way", ["Life has begun at fertilization", "The repercussions are indescribably large", "Cloning is cheap"], "제한적으로 허용.")]
        + [F("배아도 ___인 인간이기 때문에 실험에 사용하는 것은 도전이다. (potential)", "잠재적", ["제한적", "극단적"], "잠재적."), F("인간의 배아를 함부로 다루는 것은 심각한 인권 ___에 해당한다. (infringement)", "침해", ["증진", "진척"], "침해."), F("개인적인 ___의 문제뿐만이 아니라 가정 파괴 등 문제가 많다. (identity)", "정체성", ["인간성", "창의성"], "정체성."), F("생명과학기술의 발달은 인간의 생명을 ___할 수 있는 기술을 주었다. (to manipulate)", "조작", ["증명", "인쇄"], "조작하다.")]
        + [read_q("배아 복제의 문제는 배아를 인간으로 보느냐에 따라 달라진다"), read_q("정자와 난자가 만나 수정란이 된 직후부터 생명은 시작되었다"), read_q("사회 여러 분야의 동의와 합의 하에 진행되어야 할 것이다"), read_q("앞으로 어떤 새로운 발명품이 나왔으면 좋겠는지 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("금속활자", "(金屬活字) movable type printing press; “metal type”", ""),
        ("모형", "(模型) a model; a mold; a pattern", "아이 생일 선물로 모형 비행기를 사 줄까 합니다."),
        ("성분", "(成分) an ingredient; a component; an element", "아이들 분유에서 유해 성분이 검출되었습니다."),
        ("성서", "(聖書) the Bible; “holy book”", "", "성경, 경전, 불경, 코란"),
        ("인쇄(하다/되다)", "(印刷) printing (to print/to be printed)", "제 명함이 다 떨어졌어요. 더 인쇄해야겠어요."),
        ("종주국", "(宗主國) a country of origin", "김치의 종주국은 한국이다."),
        ("증명(하다/되다)", "(證明) proving; proof (to prove/to be proven)", "그럼 김 선생님이 하신 말씀이 사실이라는 것을 증명해 주세요."),
        ("직지", "(直旨) the abbreviated title of a Korean Buddhist document: Anthology of Zen Teachings of Great Buddhist Priests", ""),
        ("추정(하다/되다)", "(推定) presumption; assumption; inference; estimation (to presume; to infer/to be presumed; to be inferred)", "이번 화재 사건은 방화인 것으로 추정됩니다.", "추측하다, 추론하다"),
    ]),
    ("학습활동 2", [
        ("난자", "(卵子) an ovum; an egg", ""),
        ("덩어리", "a lump; a chunk; a clot", "집에 먹을 것이 빵 한 덩어리밖에 없어요."),
        ("수정란", "(受精卵) a fertilized egg", "", "미수정란"),
        ("얽매다", "to bind; to tie up; to fasten", "너무 공부에만 얽매이지 말고 주말에는 친구들도 좀 만나세요."),
        ("엄연하다", "(儼然) to be clear; to be undeniable", "남북이 대립하고 있다는 엄연한 현실을 잊어서는 안 된다."),
        ("인간성", "(人間性) humanity", "현대인들은 인간성을 상실해가고 있는 듯 합니다."),
        ("인권 침해", "(人權 侵害) infringement of human rights", "인권이 침해되는 경우가 종종 보도되고 있습니다."),
        ("인권론자", "(人權論者) a human-rights activist; a proponent of human rights", ""),
        ("인류", "(人類) human race", "핵이 인류를 풍요롭게 할지, 재앙에 빠뜨릴지 모르겠어요."),
        ("잠재적", "(潛在的) potential; latent", "아이들은 잠재적인 능력이 많습니다."),
        ("정자", "(精子) sperm", "", "난자"),
        ("정체성", "(正體性) identity", "십 대들은 자기의 정체성을 찾고 싶어 합니다."),
        ("제한적", "(制限的) limited; restrictive", "화재 이후 그 건물의 출입은 제한적으로만 허용되고 있다."),
        ("조작(하다/되다)", "(造作) fabrication; invention (to fabricate; to invent/to be fabricated)", "유전자 조작 식품을 먹어도 됩니까?"),
        ("증진(하다/되다)", "(增進) promotion; enhancement (to promote; to enhance/to be enhanced)", "건강 증진을 위해서는 규칙적인 식사와 운동을 해야 한다."),
        ("진척(하다/되다)", "(進陟) progress; advancement (to make progress/to be advanced)", "지금 그 일의 진척 상황이 어떻게 되고 있습니까?"),
        ("파장", "(波長) wavelength; repercussion", "그 사건은 사회 전반에 큰 파장을 가져왔다."),
        ("헤아릴 수 없이 많다", "to be innumerable; indefinite", "", "수없이 많다, 무수히 많다"),
        ("혜택", "(惠澤) benefit", "군대에 입대하면 혜택이 많습니다."),
    ]),
    ("학습활동 3", [
        ("고무", "rubber; gum", ""),
        ("공업고등학교", "(工業高等學校) a technical high school", "", "공고, 상업고등학교, 실업계 고등학교, 인문계 고등학교"),
        ("구체적", "(具體的) concrete; specific; detailed", "구체적인 실천 방법을 말해 보세요."),
        ("깔끔하다", "to be neat; to be arranged well", "페인트를 새로 칠해서 집이 아주 깔끔해졌어요."),
        ("동력기", "(動力機) a motor; “a power machine”", ""),
        ("멀티탭", "power strip; “multitap”", ""),
        ("발명특허", "(發明特許) a patent for an invention", ""),
        ("배경", "(背景) background", "이 사건의 배경이 무엇입니까?"),
        ("선두주자", "(先頭走者) a front-runner", "천구백칠십 년대 애플사는 개인 컴퓨터 사업의 선두주자였습니다."),
        ("소질", "(素質) a talent; an aptitude", "나는 음악과 미술 같은 예술에는 전혀 소질이 없습니다.", "적성"),
        ("수상자", "(受賞者) a winner (of a prize or an award)", "이번 대회의 수상자가 총 몇 명입니까?", "입상자"),
        ("수상하다", "(受賞) to win (a prize or an award)", "대상을 수상하신 것, 정말 축하 드립니다."),
        ("실용적", "(實用的) practical; pragmatic", "저는 제가 배운 것을 실용적으로 잘 활용하고 싶어요."),
        ("외관상", "(外觀上) in appearance; externally", "그 부부는 외관상으로는 아무런 문제가 없습니다."),
        ("이론적", "(理論的) theoretical", "그 일은 이론적으로는 가능합니다."),
        ("장래", "(將來) future", "장래 희망이 무엇입니까?", "미래, 장차"),
        ("창의성", "(創意性) creativity", "아이들이 창의성을 발휘할 수 있도록 지도하고 싶습니다."),
        ("특활", "(特活) an extracurricular activity", "저는 학교에서 특활시간이 가장 재미있어요.", "특별활동"),
        ("평범하다", "(平凡) to be ordinary", "저는 반에서 눈에 띄지 않는 평범한 아이였어요.", "비범하다"),
        ("획득(하다)", "(獲得) acquisition (to acquire)", "그 회사는 특허를 획득했어요.", "얻다"),
    ]),
]
L7 = lesson(
    "U17 L9 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 금속활자 · 모형 · 성서 · 인쇄 · 종주국 · 증명 · 직지 · 추정 · 난자 · 정자 · 수정란 · 엄연하다 · 인간성 · 인권 침해 · 인류 · 잠재적 · 정체성 · 제한적 · 조작 · 증진 · 진척 · 파장 · 혜택 · 구체적 · 동력기 · 발명특허 · 선두주자 · 소질 · 수상자 · 실용적 · 창의성 · 특활 · 평범하다 · 획득",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 금속활자, 직지, 난자, 수정란, 인권론자, 정자, 헤아릴 수 없이 많다, 고무, 공업고등학교, 동력기, 멀티탭 and 발명특허. In the book 수상하다 has a homonym 殊常, “to be suspicious”; the book lists 공고 as the short form of 공업고등학교 and 상업고등학교, 실업(계) 고등학교, 인문(계) 고등학교 as related, which I wrote without the parentheses. 헤아릴 수 없이 many is split in the book as “헤아릴 수 없이 / 많다”, with 수없이 많다, 무수히 많다 as related. The book writes 10대들은 and 1970년대 in digits, which I spelled in Hangul. 멀티탭 means a power strip; the book explains it as “multitap”.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=20, nread=16)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 9: Science and Inventions (과학과 발명)", [L1, L2, L3, L4, L5, L6, L7])
