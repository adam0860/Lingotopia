"""Unit 57: KBC Semester III, Unit 15, Lesson 2 - Accidents and Crimes (사고와 범죄).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 15, Student's Edition.
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain

# ================================================================== L1 review
_M1 = [("이탈", "breakaway; derailment"), ("붕괴", "collapsing"), ("탈선", "a runaway (train)"), ("긴급", "emergency"), ("신고", "declaration; report"), ("위반", "a violation; a breach"), ("해역", "an ocean area"), ("통제", "control; regulation"), ("즉시", "immediately")]
_TYPES = [("탈선", "derailment"), ("익사", "drowning"), ("침몰", "sinking"), ("전복", "an overturn"), ("화재", "a fire"), ("붕괴", "collapse")]
_HJ2 = [("人 인", "people; human", "인명, 타인"), ("大 대", "big; large; great", "대교, 대중교통"), ("海 해", "sea", "해양, 해경"), ("告 고", "inform; report", "경고, 고발"), ("死 사", "die; pass away", "사망, 사인")]
_HJW2 = [("인명", "human life"), ("타인", "others"), ("대교", "a big bridge"), ("대중교통", "public transportation"), ("해양", "the sea; the ocean"), ("해경", "Coast Guard; “sea police”"), ("경고", "a warning"), ("고발", "an accusation; a charge"), ("사망", "death"), ("사인", "cause of death")]
_SIM = [("대교", "다리", "a big bridge ≈ a bridge"), ("해양", "바다", "the ocean ≈ the sea"), ("고발", "신고", "an accusation ≈ a report"), ("경고", "주의", "a warning ≈ caution")]
_BOX4 = [("택시, 버스, 지하철", "대중교통", "public transportation"), ("사망, 경상, 중상", "사상자", "casualties"), ("일일구, 일일이, 일일삼", "신고", "a report (emergency numbers 119, 112, 113)"), ("원고, 피고, 증인", "재판", "a trial")]
_L1X = [("붕괴하다", "to collapse"), ("익사", "drowning"), ("다리", "a bridge; a leg"), ("바다", "the sea"), ("주의", "caution; attention"), ("광고", "an advertisement"), ("피고", "a defendant"), ("원고", "a plaintiff"), ("증인", "a witness"), ("재판", "a trial"), ("사상자", "casualties"), ("택시", "a taxi"), ("지하철", "a subway"), ("가드레일", "a guard rail"), ("좌석", "a seat"), ("수심", "water depth"), ("경상", "a slight injury"), ("중상", "a serious injury")]
L1 = lesson(
    "U15 L2 · Review: accident and crime words and Sino-Korean 人 大 海 告 死",
    "사고와 범죄 · 단어 복습 · 한자어 복습 · 이탈 · 붕괴 · 탈선 · 긴급 · 신고 · 人 大 海 告 死",
    requires=[],
    cards=[
        card("단어 복습 1: matching the meanings (my answers)", "The book asks you to connect each word on the left with its English meaning on the right (the book’s meanings; my matching):", tables=[ktable(_M1)]),
        card("단어 복습 2: types of accident (listening)", "The book plays four accident news clips and asks you to write the type of accident from the box (탈선, 익사, 침몰, 전복, 화재, 붕괴). The clips are audio and are left out; the words of the box:", tables=[ktable(_TYPES)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ2], say=[2]), ktable(_HJW2)]),
        card("한자어 복습 1: the word with a similar meaning (my answers)", "The book asks you to circle the word with a meaning similar to the word on the left (A. 대교: 이탈, 가드레일, 다리, 좌석; B. 해양: 바다, 해경, 침몰, 수심; C. 고발: 사고, 광고, 신고, 피고; D. 경고: 익사, 주의, 붕괴, 부상). My answers:", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [[a, b, c] for a, b, c in _SIM], say=[0, 1])]),
        card("한자어 복습 2: the related word (my answers)", "Read the three words and choose from the box the word related to them (the box: 재판, 사상자, 신고, 속도, 대중교통). The emergency numbers 119, 112 and 113 are read 일일구, 일일이, 일일삼. My answers:", tables=[table(["The three words", "The related word", "Meaning"], [[a, b, c] for a, b, c in _BOX4], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L1X)]),
    ],
    exercises=uniq(
        _tr(_M1, k=3) + _tr(_TYPES, k=3) + _tr(_HJW2, k=3) + _tr(_L1X, k=3)
        + [M("What does 이탈 mean?", "breakaway; derailment", ["collapsing", "emergency", "control"], "이탈."), M("What does 붕괴 mean?", "collapsing", ["a violation", "immediately", "an ocean area"], "붕괴."), M("What does 긴급 mean?", "emergency", ["control", "immediately", "a report"], "긴급."), M("What does 해역 mean?", "an ocean area", ["a violation", "emergency", "a report"], "해역."), M("What does 통제 mean?", "control; regulation", ["immediately", "emergency", "collapsing"], "통제."), M("What does 즉시 mean?", "immediately", ["emergency", "a report", "a violation"], "즉시."), M("What does the syllable 人 (인) mean?", "people; human", ["sea", "inform; report", "die"], "인명."), M("What does the syllable 大 (대) mean?", "big; large; great", ["sea", "die", "people"], "대교."), M("What does the syllable 海 (해) mean?", "sea", ["die", "big", "people"], "해양."), M("What does the syllable 告 (고) mean?", "inform; report", ["sea", "die", "big"], "경고."), M("What does the syllable 死 (사) mean?", "die; pass away", ["sea", "inform", "people"], "사망."), M("Which word is similar to 대교?", "다리", ["이탈", "가드레일", "좌석"], "A big bridge is a bridge."), M("Which word is similar to 해양?", "바다", ["해경", "침몰", "수심"], "The ocean is the sea."), M("Which word is similar to 고발?", "신고", ["사고", "광고", "피고"], "A charge is a report."), M("Which word is similar to 경고?", "주의", ["익사", "붕괴", "부상"], "A warning is caution."), M("Which word relates to 택시, 버스, 지하철?", "대중교통", ["재판", "신고", "속도"], "Public transportation."), M("Which word relates to 원고, 피고, 증인?", "재판", ["신고", "사상자", "속도"], "A trial."),
           F("한강의 다리를 ___라고도 합니다. (a big bridge)", "대교", ["해양", "경고"], "대교."), F("화재가 나면 즉시 ___해야 합니다. (report)", "신고", ["경고", "고발"], "신고."), F("사고 때문에 도로를 ___하고 있습니다. (control)", "통제", ["이탈", "붕괴"], "통제."), F("열차가 선로를 ___했습니다. (broke away from)", "이탈", ["통제", "신고"], "이탈."), F("한국의 ___은 바다를 지키는 해양경찰입니다. (Coast Guard)", "해경", ["사인", "타인"], "해경."),
           read_q("긴급 상황이 발생했습니다"), read_q("화재를 즉시 신고하세요"), read_q("해경이 해역을 통제하고 있습니다"), read_q("열차가 탈선했습니다"), read_q("대중교통을 이용하세요")]
    ),
)

# ================================================================== L2 Part 1 texts
_GAE = [
    ("지난 이 일 저녁 비가 내리는 가운데 개성공단에서 북쪽 노동자들을 태운 출퇴근용 버스 두 대가 충돌하는 사고가 일어난 것으로 뒤늦게 확인됐다.", "It was belatedly confirmed that, on the evening of the 2nd, in the rain, an accident occurred at the Gaesung Industrial Park in which two commuter buses carrying North Korean workers collided."),
    ("이종주 통일부 부대변인은 칠 일 브리핑에서 지난 이 일 저녁 일곱 시 사십 분께 개성공단에서 버스 두 대의 충돌사고가 발생했다며 운전자와 탑승자는 모두 북쪽 인원이라고 밝혔다.", "Assistant spokesperson Lee Jong-ju of the Ministry of Unification said at a briefing on the 7th that a collision between two buses occurred at the Gaesung Industrial Park at about 7:40 on the evening of the 2nd and that the drivers and passengers were all North Korean personnel."),
    ("이 부대변인은 공단 안에서 발생한 사고이고 관련자가 모두 북쪽 인원이라 사고 직후 현장 통제와 부상자 이송 등 필요한 조처는 북쪽이 하고 있다고 말했다.", "Assistant spokesperson Lee said that since it was an accident that occurred inside the industrial park and all those concerned were North Korean personnel, the North is taking the necessary measures such as controlling the site and transferring the injured right after the accident."),
    ("이와 관련해 개성공단에 인접한 파주경찰서는 이 사고로 북쪽 노동자 열 명이 숨지고 마흔여섯 명이 다쳐 치료를 받고 있는 것으로 파악하고 있는 것으로 전해졌다.", "In this connection, it was reported that Paju Police Station, which is adjacent to the Gaesung Industrial Park, understands that in this accident ten North Korean workers died and forty-six were injured and are receiving treatment."),
    ("파주경찰서 관계자는 경의선 남북출입사무소를 통해 개성공단을 오가는 노동자를 통해 사고 내용을 파악했다고 말했다.", "An official of Paju Police Station said they grasped the content of the accident through workers going back and forth to the Gaesung Industrial Park via the Gyeongui Line South-North Transit Office."),
    ("하지만 통일부의 이 부대변인은 빗길 사고로 판단되지만 정확한 사고 원인이나 인명 피해 규모는 파악된 게 없다고 밝혔다.", "But assistant spokesperson Lee of the Ministry of Unification said that although it is judged to be a wet-road accident, nothing has been confirmed about the exact cause or the scale of the human casualties."),
    ("통일부 당국자는 북쪽 노동자를 태운 퇴근버스와 야근자용 출근버스가 충돌해 두 차량이 전파된 것으로 알고 있다고 말했다.", "A Ministry of Unification official said he understands that a bus carrying North Korean workers home and a bus taking night-shift workers to work collided and both vehicles were totaled."),
    ("개성공단에선 이천사 년 십이 월 시범단지 가동 이래 이번 사고 이전에 사망사고 세 건을 포함해 모두 열세 차례의 크고 작은 교통사고가 있었고, 모두 보험 처리됐다.", "At the Gaesung Industrial Park, since the model complex started operating in December 2004, before this accident there had been a total of thirteen traffic accidents large and small, including three fatal accidents, and all were handled by insurance."),
]
_EEI = [["When", "The evening of the 2nd, at about 7:40 (confirmed late; announced on the 7th)"], ["Where", "The Gaesung Industrial Park, North Korea"], ["Who", "North Korean workers (drivers and passengers were all North Korean); 10 died and 46 were injured according to Paju police"], ["What", "Two commuter buses (one taking workers home, one taking night-shift workers to work) collided; both vehicles were totaled"], ["How/Why", "Judged to be a wet-road accident (it was raining); the exact cause and scale of casualties were not confirmed"]]
_PROV = [("그림의 떡", "a pie in the sky; something attractive but out of reach"), ("누워서 침 뱉기", "spitting while lying down; (like) spitting in one’s own face, harming oneself by harming others"), ("바늘 도둑이 소 도둑 된다", "a needle thief becomes a cow thief; small wrongdoings grow into big crimes")]
_SPEAK4 = [("자기 자신이나 가족 등 가까운 사람의 교통법규 위반 사례에 대해서 서로 이야기해 보세요.", "Talk with each other about cases of traffic-law violations by yourself or by people close to you, such as family."), ("미국에서 자주 발생하는 범죄에 대해서 이야기해 보세요.", "Talk about the crimes that often occur in the United States.")]
L2 = lesson(
    "U15 L2 · Part 1 (도입 학습): the Gaesung Industrial Park and a bus collision",
    "도입 학습 · 개성공업지구 · 버스 충돌 · 통일부 · 속담 · 말해 봅시다",
    requires=[],
    cards=[
        card("알아봅시다: 개성공업지구 (Gaesung Industrial Region)",
             "Gaesung Industrial Region is a specially designated industrial site in North Korea’s Gaesung City, 10 km (6 mi) north of the demilitarized zone (DMZ). 개성공단, or Gaesung Industrial Park, refers to the industrial complex created in the region, which was developed and is being operated in collaboration with South Korea. The construction began in 2002 and the first site of the model complex (시범단지) opened in 2004. Since its opening, the Park has expanded to include many hundreds of South Korean companies, employing hundreds of thousands of North Koreans. Under a 50-year lease contract between a designated South Korean committee and North Korea, the operation of 개성공단 has been adversely affected by political issues, including U.S. economic sanctions against North Korea, policies of the South Korean government, and incidents such as the killing of a South Korean tourist by the North Korean Coast Guard at 금강산 in 2007."),
        card("학습활동 2 (Reading): a newspaper article on a bus collision in Gaesung",
             "The following is a newspaper article about a traffic accident in North Korea’s Gaesung Industrial Region (Hankyoreh). The book asks you to fill in the EEIs (essential elements of information) in English, summarize the accident, and choose which of four points the article explains. The text is the book’s with the numbers spelled out (2일 is 이 일, 7시 40분께 is 일곱 시 사십 분께, 버스 2대 is 버스 두 대, 10명 is 열 명, 46명 is 마흔여섯 명, 2004년 12월 is 이천사 년 십이 월, 3건 is 세 건, 13차례 is 열세 차례); the quotation marks are removed. The English is mine.",
             examples=passage(_GAE)),
        card("The questions answered (mine)", "1. The EEIs and the summary:", tables=[table(["EEI", "Summary of the accident"], [list(r) for r in _EEI])]),
        card("The multiple-choice question (mine)", "2. The point explained in the article is A. The facts of the accident were confirmed by word of mouth (the police learned of it from workers going back and forth through the transit office). B is wrong because there had been thirteen earlier accidents; C is wrong because the North took the measures; D is wrong because no official report with the cause and casualties had been released."),
        card("학습활동 3 (Listening): the proverbs", "The book asks you to study three Korean proverbs, write the meaning or English equivalent, and circle the one that best fits an audio clip about traffic offenses. My meanings (the audio is left out, so I do not choose):", tables=[ktable(_PROV)]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK4)),
        card("Activities left out", "학습활동 1 (listening to six news clips from YTN about incidents, accidents and crimes: checking the topic and writing Korean key words, and a second set of two clips with a summary) and 학습활동 3 (listening to a clip about traffic offenses from the Seoul Education Research & Information Institute: the typical sequence of offenses of repeat violators and why they occur in that sequence) are audio activities."),
    ],
    exercises=uniq(
        _tr(_GAE, k=3) + _tr(_PROV, k=2)
        + [M("Where did the bus accident happen?", "Gaesung Industrial Park", ["Seoul", "Paju", "Incheon"], "개성공단."), M("What collided?", "Two commuter buses", ["Two trains", "Two taxis", "Two ships"], "버스 두 대."), M("Who were in the buses?", "North Korean workers", ["South Korean tourists", "Soldiers", "Students"], "북쪽 노동자."), M("When did the accident happen?", "About 7:40 in the evening", ["Early morning", "At noon", "At midnight"], "일곱 시 사십 분께."), M("Who announced it at the briefing?", "Assistant spokesperson Lee of the Ministry of Unification", ["The police chief", "A bus driver", "The president"], "통일부 부대변인."), M("How many died, according to Paju police?", "10", ["46", "13", "3"], "열 명."), M("How many were injured, according to Paju police?", "46", ["10", "13", "3"], "마흔여섯 명."), M("What was the apparent cause?", "A wet-road accident", ["A fire", "A bomb", "A flood"], "빗길 사고."), M("How many traffic accidents had there been earlier, including three fatal ones?", "13", ["3", "46", "10"], "열세 차례."), M("When did the model complex begin operating?", "December 2004", ["April 2007", "June 2002", "May 1999"], "이천사 년 십이 월."), M("How were the earlier accidents handled?", "By insurance", ["By the court", "By the army", "They were ignored"], "보험 처리."), M("What does the proverb 그림의 떡 mean?", "A pie in the sky; out of reach", ["Spitting upward", "A needle thief", "A rice cake gift"], "그림의 떡."), M("What does the proverb 바늘 도둑이 소 도둑 된다 mean?", "Small wrongdoings grow into big crimes", ["A thief is caught", "Needles are valuable", "Cows are cheap"], "바늘 도둑."),
           F("개성공단에서 버스 두 대가 ___했다. (collided)", "충돌", ["붕괴", "침몰"], "충돌."), F("통일부 ___은 브리핑에서 사고를 밝혔다. (assistant spokesperson)", "부대변인", ["조교", "기관사"], "부대변인."), F("사고 직후 현장 ___과 부상자 이송 등이 필요하다. (control)", "통제", ["이탈", "신고"], "통제."), F("파주경찰서는 개성공단에 ___해 있다. (is adjacent)", "인접", ["연계", "도하"], "인접."), F("두 차량이 ___되었다. (totaled)", "전파", ["반파", "침몰"], "전파."),
           read_q("개성공단에서 버스 두 대가 충돌했습니다"), read_q("북쪽 노동자 열 명이 숨졌습니다"), read_q("통일부 부대변인이 브리핑에서 밝혔습니다"), read_q("빗길 사고로 판단됩니다"), read_q("모두 보험 처리됐습니다")]
    ),
)


# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("귀금속", "(貴金屬) precious metals; jewelry", "어머니에게 귀금속을 좀 선물해 드리고 싶어요.", "보석"),
        ("금은방", "(金銀房) a jewelry store; “gold and silver room”", "우리 아버지는 금은방을 운영하고 계십니다.", "보석방, 보석 가게, 귀금속상"),
        ("다세대 주택", "(多世帶 住宅) multiunit housing; “multiple-household housing”", "서울시내 다세대 주택에서 화재가 발생했습니다.", "공동 주택, 연립 주택, 아파트"),
        ("부조종사", "(副操縱士) a co-pilot; “deputy pilot”", "항공사 기장들이 비행시간을 줄여 달라며 파업을 벌였습니다.", "부기장"),
        ("잇따라", "one after another; consecutively", "요즘 살인사건이 잇따라 발생하면서 치안에 비상이 걸렸습니다.", "연달아, 연이어, 계속해서 | 잇달다, 잇따르다"),
        ("현역", "(現役) (on) active duty; “currently serving” (This word normally refers to a serviceman or an athlete.)", "한국의 현역 축구 선수 중 누가 가장 유명합니까?", "예비역, 퇴역"),
    ]),
    ("학습활동 2", [
        ("~ 건", "(件) counter for incidents (e.g., accidents, crimes, occurrences)", "어제 서울에서 강도사건이 다섯 건 발생했습니다."),
        ("공단", "(工團) an industrial complex", "서울의 구로 공단이 천구백칠십 년대 한국의 경제발전을 이끌었다.", "(an acronym of) 공업단지"),
        ("뒤늦게", "belated; late", "이 제안의 문제점을 뒤늦게 발견했습니다.", "늦게, 일찍, 미리"),
        ("부대변인", "(副代辯人) an assistant spokesperson; “deputy spokesperson”", "이번 사건에 대해 민주당의 부대변인이 성명을 발표했습니다."),
        ("조처(하다)", "(措處) measure (to take); a step (taken in dealing with an issue, etc.)", "같은 지역에 수해가 계속 발생하는데 당국은 아무런 조처를 취하지 않고 있습니다.", "조치"),
        ("인접(하다)", "(隣接) contiguity; adjacency; proximity; “touch with a neighbor” (to be adjacent; to border on)", "우리 아파트는 학교와 편의시설이 인접해 있습니다.", "가깝다 | 인접국가, 인접마을"),
        ("전파(되다)", "(全破) total destruction (to be destroyed completely; to be totaled)", "이번 사고로 버스가 전파되었습니다.", "반파 | 전파 (傳播) spread; propagation; 전파 (電波) radio wave; electromagnetic signal"),
        ("시범 단지", "(示範 團地) a piloting site (of a new development, complex, etc.); a model complex", "친환경 에너지를 홍보하기 위해 풍력발전 시범단지를 조성하기로 했습니다."),
        ("가동(하다/되다)", "(稼動) operation (to operate/to be operated)", "화재 위험 때문에 발전소 가동이 중단됐다."),
        ("~ 이래", "(以來) since; after", "역사이래 가장 큰 사건이 터졌다.", "이후 | 이전"),
    ]),
    ("학습활동 3", [
        ("국선 변호사", "(國選 辯護士) a public defender; a court-appointed lawyer", "피의자가 경제적으로 어려움을 겪고 있어서 국선 변호사를 선임하기로 했습니다.", "민선 변호사"),
        ("돌이키다", "to reverse; to look back; to recover", "돌이켜 생각해 보니 내 어린 시절이 가장 행복했던 때이다."),
        ("돌이킬 수 없다", "to be irrevocable", "돌이킬 수 없는 잘못을 저지르고 후회하는 사람이 많다."),
        ("무면허", "(無免許) without license; “no license”", "김 모 씨가 무면허로 의료 행위를 하다 적발되었습니다."),
        ("반성(하다)", "(反省) reflection; regret; reconsideration (to reflect upon; to regret; to reconsider)", "교회에 가면 잘못한 일을 반성하게 된다.", "후회하다"),
        ("뺑소니(치다)", "a hit-and-run (to hit and run)", "노인을 치고 달아났던 뺑소니 운전자가 어제 경찰에 자수했다."),
        ("처하다", "(處) to be in (a certain situation)", "위험에 처할 때는 무엇보다 먼저 침착해야 한다."),
        ("특이하다", "(特異) to be peculiar; to be singular; to be remarkable; “to be specially different”", "이 제품은 디자인이 특이해서 인기가 많을 것 같아요."),
        ("현명하다", "(賢明) to be wise", "현명한 사람은 하나를 들으면 열을 안다."),
    ]),
]
L3 = lesson(
    "U15 L2 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 귀금속 · 금은방 · 부조종사 · 잇따라 · 현역 · 공단 · 부대변인 · 전파 · 가동 · 뺑소니 · 무면허",
    requires=[],
    cards=vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=12, nread=8)),
)

# ================================================================== L4 Part 2 texts
_K21 = [
    ("이십구 일 오후 한 시 오십 분께 전남 장성군 삼서면 상무대 육군기계화학교 수상조종 훈련장에서 육군 전투장갑차(케이이십일)가 저수지에 빠져 부사관 한 명이 숨졌다.", "On the 29th at about 1:50 in the afternoon, at the amphibious driving training ground of the Army Mechanized School at Sangmudae, Samseo-myeon, Jangseong-gun, South Jeolla, an army infantry fighting vehicle (K21) fell into a reservoir and one noncommissioned officer died."),
    ("이날 사고는 장갑차 제조업체 디귿사 직원이 교관인 김 아무개 (스물세 살) 중사(진급 예정)와 조교 임무를 수행할 예정인 이등병을 대상으로 교육을 하던 중 일어났다.", "The accident that day happened while an employee of company D, the armored vehicle manufacturer, was giving training to the instructor Sergeant Kim (23) (to be promoted) and a private second class who was to carry out the duties of an assistant instructor."),
    ("사고 직후 제조업체 직원과 현역 이등병은 탈출했지만, 조종을 맡았던 김 중사는 안에 갇혀 장갑차 바닥에서 숨진 채 발견됐다.", "Right after the accident the manufacturer’s employee and the active-duty private escaped, but Sergeant Kim, who had been at the controls, was trapped inside and was found dead on the floor of the armored vehicle."),
    ("육군기계화학교는 최근 케이이십일 장갑차 다섯 대를 배치받아 열여섯 명을 대상으로 이십팔 일부터 강을 건너는 도하훈련을 실시하고 있었다.", "The Army Mechanized School had recently been assigned five K21 armored vehicles and had been carrying out river-crossing training for sixteen people since the 28th."),
    ("케이이십일 장갑차는 우리 기술로 개발돼 지난해부터 실전에 배치됐다.", "The K21 armored vehicle was developed with our technology and has been deployed for real operations since last year."),
    ("지난해에도 도하훈련 도중 엔진이 정지한 적이 있어 장비 결함 가능성도 제기되고 있다.", "Last year too there was an occasion when the engine stopped during river-crossing training, so the possibility of an equipment defect is also being raised."),
]
_EEI2 = [["When", "The 29th, about 1:50 in the afternoon (the training had begun on the 28th)"], ["Where", "The amphibious driving training ground of the Army Mechanized School, Sangmudae, Jangseong-gun, South Jeolla"], ["Who", "Sergeant Kim (23, the instructor, to be promoted), who was at the controls, died; a manufacturer’s employee and an active-duty private escaped"], ["What", "An army K21 infantry fighting vehicle fell into a reservoir and one noncommissioned officer died"], ["How/Why", "It happened during river-crossing (도하) training led by an employee of the manufacturer; the sergeant was trapped inside; an equipment defect is suspected because the engine had stopped in a training exercise last year"]]
_DI1 = [
    ("삼 월 삼 일 화요일 흐림", "Tuesday, March 3, cloudy"),
    ("오늘 체육 시간에 손 씻는 습관에 대해 배웠다.", "Today in P.E. class I learned about the habit of washing hands."),
    ("건강을 지키는데 자주 손을 씻는 것만큼 좋을 것이 없다고 한다.", "They say there is nothing as good for keeping healthy as washing your hands often."),
    ("자주 씻는 것도 중요하지만 제대로 씻는 것이 더 중요하다.", "Washing often is important, but washing properly is more important."),
    ("먼저 시계나 반지는 풀고 씻는 것이 좋다.", "First, it is good to take off your watch or ring before washing."),
    ("흐르는 물에 비누를 이용해서 닦고, 손가락 하나하나와 손등 손바닥을 잘 문질러서 닦아야 한다.", "You should wash with soap under running water, rubbing each finger, the back of the hand and the palm well."),
    ("나는 일 년 내내 감기에 자주 걸리는 편인데 이번에 배운 대로 손 씻는 습관을 바꿔 봐야겠다.", "I tend to catch colds often all year round, so I should try changing my hand-washing habit as I learned this time."),
    ("감기 뚝", "Goodbye, colds!"),
]
_DI2 = [
    ("칠 월 팔 일 일요일 장맛비", "Sunday, July 8, monsoon rain"),
    ("오늘은 내가 사랑의 신발 정리를 했다.", "Today I did the shoe-tidying of love."),
    ("식구들의 신발의 흙과 먼지를 털고 깨끗이 닦아서 잘 놓았다.", "I shook off the soil and dust from my family’s shoes, wiped them clean and arranged them well."),
    ("난 행복했다.", "I was happy."),
    ("선생님이 말씀하셨다.", "The teacher said:"),
    ("현관에 신발이 어지럽게 놓여 있는 집은 도둑질 하기가 쉽고, 신발 정리가 잘 된 집은 주인에게 붙잡힐 확률이 많아 도둑이 포기한다고 했다.", "A house where shoes are left in a mess at the entrance is easy to burgle, while at a house where the shoes are tidy, the thief is more likely to be caught by the owner, so the thief gives up."),
    ("신발 정리를 하니 내 기분이 좋아졌다.", "I felt better after tidying the shoes."),
    ("우리 식구들이 신발을 신고 나처럼 기분 좋아했으면 좋겠다.", "I hope my family will put on the shoes and feel good like me."),
]
_DI3 = [
    ("십이 월 십이 일 목요일 맑음", "Thursday, December 12, clear"),
    ("오늘은 책 정리를 했다.", "Today I tidied my books."),
    ("그동안 읽었던 책 중에서 다시 읽고 싶은 것들만 따로 책꽂이에 놓고, 다 읽거나 불필요한 책들은 따로 싸 두었다.", "Of the books I had read, I put only those I want to read again on the bookshelf, and packed the ones I finished or do not need separately."),
    ("책상을 정리하니까 기분이 좋고 공부도 더 잘 되는 것 같다.", "I feel good after tidying the desk, and studying seems to go better too."),
    ("내일은 싸 둔 책들을 학교에 가지고 가려고 한다.", "Tomorrow I plan to take the packed books to school."),
    ("학교에서는 모은 책들을 고아원이나 가난한 아이들에게 보내줄 것이다.", "At school they will send the collected books to orphanages or poor children."),
    ("내 책이 다른 아이들에게 도움이 되길 바란다.", "I hope my books will help other children."),
]
_SPEAK5 = [("미국에서 발생했던 군 장비 관련 사고 뉴스에 대해 서로 이야기해 보세요.", "Talk with each other about news of accidents related to military equipment that occurred in the United States."), ("북한이 일으키는 군사적 도발에 대해 한국과 미국, 그리고 국제사회가 어떻게 대응할지 서로 이야기해 보세요.", "Talk with each other about how South Korea, the United States and the international community will respond to the military aggression North Korea causes.")]
L4 = lesson(
    "U15 L2 · Part 2 (본 학습): a K21 armored vehicle accident and three diaries",
    "본 학습 · 장갑차 사고 · 도하훈련 · 저수지 · 일기 · 손 씻기 · 신발 정리 · 책 정리",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): an article on an army accident",
             "The following is a newspaper article about an accident in the army (Hankyoreh). The book asks you to pull out the EEIs and summarize the article. The text is the book’s with the numbers and letters spelled out (29일 is 이십구 일, 1시50분께 is 한 시 오십 분께, K21 is 케이이십일, 1명 is 한 명, ㄷ사 is 디귿사, 23 is 스물세 살, 5대 is 다섯 대, 16명 is 열여섯 명, 28일 is 이십팔 일); the English is mine.",
             examples=passage(_K21)),
        card("The EEIs and the summary (mine)", "", tables=[table(["EEI", "Summary of the article"], [list(r) for r in _EEI2])]),
        card("학습활동 3 (Listening): three diary entries",
             "The book prints three diary entries (journal entries) and asks you to decide, after listening to an audio clip, which one most closely reflects the message of the clip. The clip is left out, but the three entries are in the book’s text; the dates are written out and the English is mine. The first entry is about washing hands:",
             examples=passage(_DI1)),
        card("The second diary entry: tidying shoes", "", examples=passage(_DI2)),
        card("The third diary entry: tidying books", "", examples=passage(_DI3)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK5)),
        card("Activities left out", "학습활동 2 (a commentary by North Korean TV, Korean Central Broadcasting, on the March 2010 sinking of the South Korean navy ship Cheonan: translating four phrases with North Korean words, checking the speculated causes, North Korea’s position and the argument likely to follow) and the audio part of 학습활동 3 (what two examples the speaker uses, the message, and which entry reflects it) are audio activities."),
    ],
    exercises=uniq(
        _tr(_K21, k=3) + _tr(_DI1[1:7] + _DI2[1:] + _DI3[1:], k=3)
        + [M("What fell into the reservoir?", "An army K21 infantry fighting vehicle", ["A bus", "A helicopter", "A truck"], "전투장갑차."), M("How many died?", "One noncommissioned officer", ["Five", "Sixteen", "None"], "부사관 한 명."), M("Who was giving the training?", "An employee of the manufacturer", ["A general", "A police officer", "A teacher"], "제조업체 직원."), M("Who was found dead on the floor of the vehicle?", "Sergeant Kim, who was at the controls", ["The private", "The manufacturer’s employee", "The reporter"], "김 중사."), M("What was the training?", "River-crossing (도하) training", ["Parachute training", "Shooting training", "Marching"], "도하훈련."), M("How many K21 vehicles had the school been assigned?", "Five", ["Sixteen", "Two", "Twenty-nine"], "다섯 대."), M("What possibility is being raised?", "An equipment defect", ["Sabotage", "A storm", "Drinking"], "장비 결함."), M("What did the first diary entry learn about?", "The habit of washing hands", ["Tidying shoes", "Tidying books", "Colds in winter"], "손 씻는 습관."), M("What should you take off before washing hands?", "A watch or ring", ["Shoes", "A coat", "Glasses"], "시계나 반지."), M("What does the second diary entry say about messy shoes at the entrance?", "The house is easy to burgle", ["The house is clean", "The house is cheap", "The house is cold"], "도둑질 하기가 쉽다."), M("What did the writer of the third entry do with books?", "Packed the unneeded books to send to children", ["Burned them", "Sold them", "Lost them"], "고아원이나 가난한 아이들."),
           F("장갑차가 ___에 빠져 부사관이 숨졌다. (reservoir)", "저수지", ["공단", "철길"], "저수지."), F("강을 건너는 ___훈련을 실시하고 있었다. (river-crossing)", "도하", ["가동", "이탈"], "도하."), F("장비 ___ 가능성도 제기되고 있다. (defect)", "결함", ["통제", "붕괴"], "결함."), F("김 중사는 안에 ___ 숨진 채 발견됐다. (trapped)", "갇혀", ["박혀", "튀어"], "갇히다."), F("오늘은 책 ___를 했다. (tidying)", "정리", ["통제", "신고"], "정리."),
           read_q("육군 전투장갑차가 저수지에 빠졌습니다"), read_q("강을 건너는 도하훈련을 실시하고 있었습니다"), read_q("장비 결함 가능성도 제기되고 있습니다"), read_q("자주 씻는 것도 중요하지만 제대로 씻는 것이 더 중요하다"), read_q("신발 정리가 잘 된 집은 도둑이 포기한다")]
    ),
)


# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("갇히다", "to be locked in; to be imprisoned", "아이가 아파서 저는 주말 내내 집에 갇혀 있었어요."),
        ("결함", "(缺陷) a flaw", "제품에 결함이 발견되어 회수 조치를 취하기로 했습니다."),
        ("도하", "(渡河) crossing a river", "강물이 녹아서 도하가 어렵습니다."),
        ("저수지", "(貯水池) a reservoir", "오랜 가뭄 때문에 저수지의 물이 다 말랐습니다."),
        ("전투 장갑차", "(戰鬪 裝甲車) an infantry fighting vehicle (IFV); “armored vehicle for battle”", "정부는 새로운 전투 장갑차를 개발하기로 했습니다."),
        ("조교", "(助敎) an assistant (instructor)", "저는 지금 대학에서 조교로 일하고 있습니다."),
    ]),
    ("학습활동 2", [
        ("간주하다", "(看做) to regard", "의견을 말하지 않으면 찬성하는 것으로 간주하겠습니다."),
        ("괴뢰", "(傀儡) a puppet (referring to the South Korean government)", "남한 괴뢰 정부"),
        ("군사 론평원", "(軍事 論評院) a Board of Military Commentary (a North Korean organization equivalent to the DoD’s Official Spokesperson)", "천안함 사태에 대해 북한의 군사 론평원에서 성명을 발표했습니다."),
        ("기관실", "(機關室) an engine room; a machinery room", "지금부터 기관실 안전 수칙에 대해 설명하도록 하겠다."),
        ("기뢰", "(機雷) a floating mine; a naval mine; “ship mine”", "이 근처 해역에 기뢰가 있습니다."),
        ("날조(하다/되다)", "(捏造) fabrication; concoction (to fabricate/to be fabricated)", "그 기사는 모두 날조된 것으로 판명되었습니다."),
        ("동족", "(同族) the same nation; the same race; the same tribe; the same blood", "남과 북은 같은 역사를 가진 동족입니다."),
        ("반잠수정", "(半潛水艇) a North Korean mini-submarine; “half submarine”", "북한은 반잠수정을 통해 간첩을 남파했습니다."),
        ("불상사", "(不祥事) a disaster; an unfortunate event; a misfortune", "다섯 살짜리 어린 아이가 사망하는 불상사가 발생했습니다."),
        ("불시에", "(不時) all of a sudden; suddenly; “at no time”", "경찰이 불법 도박장을 불시에 기습했습니다.", "갑자기, 예고 없이"),
        ("수중", "(水中) underwater; aquatic; waterborne; “middle of water”; 수중 (手中) in one’s hands", "요즘 스킨스쿠버 등 수중 스포츠가 인기입니다."),
        ("숱하다", "to be many; to be plenty in number", "사상 최악의 지진으로 숱한 인명피해가 발생했다."),
        ("암초", "(暗礁) an underwater rock; a hidden reef", "선박이 암초에 걸려 좌초되었습니다."),
        ("어뢰", "(魚雷) a torpedo; “fish thunder”", "잠수함이 어뢰의 공격을 받았습니다."),
        ("여론", "(輿論) public opinion; public sentiment", "이 사안에 대해 언론이 여론을 조성하고 있습니다."),
        ("연계(하다/되다)", "(連繫) association (to associate/to be associated)", "이 인턴 프로그램은 기업과 연계되어 있어서 프로그램을 마치면 기업에 취업이 될 가능성이 높습니다."),
        ("연유 탕크", "a fuel tank", "연유탕크 폭발사고로 기름이 흘러 나와 강물을 오염시켰다.", "연료 탱크"),
        ("유감스럽다", "(有感) to be regrettable; to be sorry", "초대해 주셔서 감사합니다. 유감스럽지만 이번에는 참석하지 못할 것 같습니다."),
        ("유포(하다;시키다)", "(流布) spreading; circulation; dissemination (to spread)", "허위 사실 유포로 고소를 당했습니다."),
        ("잠수정", "(潛水艇) a small-size submarine", "사고 해역에 무인 잠수정을 배치해 사고 원인을 조사하기로 했습니다.", "잠수함"),
        ("조선", "(朝鮮) Korea; Korean Peninsula; 조선 (造船) shipbuilding", "북과 남은 조선반도 비핵화에 합의하기로 하였다."),
        ("침몰(시키다/하다;되다)", "(沈沒) sinking (to sink/to be sunk)", "선박이 좌초되어 침몰했습니다."),
        ("탄약고", "(彈藥庫) an arsenal; “ammunition storehouse”", "경기도 지역에서 산사태로 탄약고가 붕괴되어 위험합니다.", "화약고"),
        ("함선", "(艦船) a corvette; a warship", "뉴스에서는 함선의 침몰 사건을 보도했습니다."),
        ("해저", "(海底) underwater; sea bottom; seabed", "먼 바다 해저 깊은 곳에서 지진이 발생해 지상에서는 큰 피해가 없었습니다.", "해상, 수중"),
    ]),
    ("학습활동 3", [
        ("도둑맞다", "to have something stolen", "새로 산 시계를 도둑맞았어요."),
        ("망가지다", "to break down; to be out of order", "컴퓨터를 산 지 얼마 안 됐는데 다 망가졌어요.", "고장나다, 부서지다 | 망가뜨리다, 고장 내다, 부수다"),
        ("언뜻", "suddenly; by chance", "김 선생님이 결혼한다는 소리를 언뜻 들었습니다."),
        ("정리 정돈(하다)", "(整理 整頓) tidying up; proper arrangement (to tidy up; to arrange neatly)", "이제 새 학기가 되었으니까 방 정리 정돈을 잘하고 싶어요."),
        ("한결", "by far; a lot", "샤워를 하고 나니 기분이 한결 좋아졌습니다.", "한층, 훨씬"),
        ("형편없다", "(形便) to be terrible; to be awful", "홍수 피해로 농작물의 값이 형편없습니다."),
        ("흉악범죄", "(凶惡犯罪) a gruesome crime; a violent crime", "최근 흉악범죄의 발생률이 상승하고 있어 대책 마련이 시급합니다.", "강력범죄"),
    ]),
]
L5 = lesson(
    "U15 L2 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 갇히다 · 결함 · 도하 · 저수지 · 조교 · 괴뢰 · 기뢰 · 어뢰 · 암초 · 침몰 · 함선 · 해저 · 흉악범죄",
    requires=[],
    cards=vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=14, nread=10)),
)


# ================================================================== L6 Part 3 text
_F5 = [
    ("최근 공군의 에프 오 전투기 사고가 부쩍 늘면서 국민적 우려와 의혹의 시선이 모이고 있다.", "As accidents of the Air Force’s F-5 fighters have recently increased remarkably, the public’s worry and gaze of suspicion are gathering."),
    ("이는 당연한 결과이기도 하다.", "This is also a natural result."),
    ("그렇지 않아도 천안함 사태로 군의 전비태세가 논란이 되고 있는데, 우리의 영공 방위를 책임지는 전투기, 그것도 숫자로 볼 때 가장 많은 비중을 차지하는 에프 오가 연이어 사고를 당했기 때문이다.", "Even without this, the military’s readiness for war is in controversy because of the Cheonan incident, and it is because the F-5, a fighter responsible for the defense of our airspace and the one that accounts for the largest share in number, has had accidents one after another."),
    ("이천 년대 이후 공군에서 발생한 열한 건의 사고 가운데 여덟 건이 에프 오 사고다.", "Of the eleven accidents that occurred in the Air Force since the 2000s, eight were F-5 accidents."),
    ("이는 단순한 기체 노후화의 문제인가, 아니면 다른 구조적인 문제가 있는 것일까?", "Is this a simple matter of the aging of the airframe, or is there some other structural problem?"),
    ("이 글에서는 에프 오 사고와 관련된 환경적 요인을 분석하고 대책을 제시하고자 한다.", "In this article I intend to analyze the environmental factors related to the F-5 accidents and present countermeasures."),
    ("최근 강원도 강릉의 에프 오 사고는 여러 정황으로 보아 사고 원인을 예단하기가 쉽지 않아 보인다.", "The recent F-5 accident in Gangneung, Gangwon Province, seems hard to judge in advance as to its cause, judging from the various circumstances."),
    ("그러나 다행스럽게도 기체가 온전히 수거됐기 때문에 시간이 걸리더라도 좀더 정확한 원인 규명이 가능할 것으로 예상된다.", "But, fortunately, because the airframe was recovered intact, it is expected that a more accurate determination of the cause will be possible even if it takes time."),
    ("에프 오는 비록 노후한 전투기지만, 안전관리 여부에 따라 사전에 충분히 사고를 막을 수 있다.", "Although the F-5 is an aged fighter, accidents can be sufficiently prevented in advance depending on whether safety is managed."),
    ("이번 기회에 한국에서도 비행 안전을 전담하는 기구가 설립되기를 기대한다.", "I hope that on this occasion an organization dedicated to flight safety will also be established in Korea."),
    ("그래서 앞으로 발생할 비행 사고의 위험으로부터 많은 생명과 재산을 지켜 낼 수 있기를 바란다.", "So I hope that many lives and much property can be protected from the danger of flight accidents that will occur in the future."),
]
_F5T = [["Accidents related to F-5s", "Eight of the eleven Air Force accidents since the 2000s were F-5 accidents; the recent F-5 accident in Gangneung, Gangwon Province (cause hard to judge, but the airframe was recovered intact)"], ["Writer’s suggestion", "Safety management can prevent accidents even with an aged fighter; establish an organization dedicated to flight safety in Korea, so that lives and property can be protected from future flight accidents"]]
_SPEAK6 = [("최근에 일어난 사고나 아직도 기억하는 사고 뉴스가 있으면 이야기해 보세요.", "If there is an accident that happened recently or an accident news item you still remember, talk about it."), ("군대에서 범죄가 발생하면 어떻게 처리하는지 서로 이야기해 보세요.", "Talk with each other about how crimes that occur in the military are handled.")]
L6 = lesson(
    "U15 L2 · Part 3 (심화 학습): a commentary on F-5 fighter accidents",
    "심화 학습 · 에프 오 전투기 · 공군 사고 · 천안함 · 안전관리 · 비행 안전",
    requires=[],
    cards=[
        card("학습활동 2 (Reading): a commentary in a news weekly",
             "The following is a commentary in a news weekly about F-5 fighter accidents (Hankyoreh). The book asks you to read the introductory and concluding paragraphs below, list the accidents related to F-5s and summarize the writer’s suggestion (and, in pairs, to summarize part of the article on the characteristics and defects of the F-5; that part is not printed in the text). The text is the book’s with the numbers and letters spelled out (F5 is 에프 오, 2000년대 is 이천 년대, 11건 is 열한 건, 8건 is 여덟 건); the English is mine.",
             examples=passage(_F5)),
        card("The table answered (mine)", "", tables=[table(["", "Answer"], [list(r) for r in _F5T])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK6)),
        card("Activities left out", "학습활동 1 (an interview with a railroad employee from the Seoul Education Research & Information Institute: his biographical information, a summary of his responses and reconstructing the reporter’s questions in Korean), 학습활동 3 (a lawyer’s story about a verdict: information on the son, father, mother and judge, and writing and performing a courtroom skit with a judge, mother, son, lawyer and prosecutor) and 학습활동 4 (a story about an incident involving a railroad employee: what happened and why, and which English proverb fits) are audio, skit and group activities."),
    ],
    exercises=uniq(
        _tr(_F5, k=3)
        + [M("What has increased remarkably, according to the article?", "Air Force F-5 fighter accidents", ["Ship accidents", "Train accidents", "Car accidents"], "에프 오 전투기 사고."), M("How many of the eleven Air Force accidents since the 2000s were F-5 accidents?", "Eight", ["Eleven", "Three", "Five"], "여덟 건."), M("Why is the public concerned?", "The F-5 is responsible for airspace defense and has had accidents one after another", ["It is a new plane", "It is cheap", "It is slow"], "연이어 사고."), M("What is the writer’s question about the cause?", "Is it simple aging of the airframe or another structural problem?", ["Was it the weather?", "Was it the pilot’s age?", "Was it the price?"], "단순한 기체 노후화."), M("Why is a more accurate determination of the cause expected for the Gangneung accident?", "The airframe was recovered intact", ["There were witnesses", "A black box was sold", "It was reported early"], "온전히 수거."), M("What does the writer say about the aged F-5?", "Accidents can be prevented in advance with safety management", ["It must be scrapped", "It cannot be fixed", "It is the safest"], "안전관리 여부."), M("What does the writer hope will be established?", "An organization dedicated to flight safety", ["A new air base", "A museum", "A flying school"], "비행 안전을 전담하는 기구."), M("What incident has already put the military’s readiness in controversy?", "The Cheonan incident", ["A flood", "A fire", "An election"], "천안함 사태."),
           F("에프 오 사고가 ___ 늘었다. (remarkably)", "부쩍", ["한결", "언뜻"], "부쩍."), F("공군의 에프 오 전투기 사고에 국민적 ___가 모이고 있다. (worry)", "우려", ["여론", "의혹"], "우려."), F("기체가 온전히 ___되어 원인 규명이 가능하다. (recovered)", "수거", ["가동", "탑재"], "수거."), F("사고 원인을 ___하기가 쉽지 않아 보인다. (to prejudge)", "예단", ["수거", "탑재"], "예단."), F("비행 안전을 ___하는 기구가 필요하다. (dedicated to)", "전담", ["예단", "의혹"], "전담."),
           read_q("에프 오 전투기 사고가 부쩍 늘었습니다"), read_q("기체가 온전히 수거되었습니다"), read_q("비행 안전을 전담하는 기구가 설립되기를 기대합니다"), read_q("천안함 사태로 군의 전비태세가 논란이 되고 있습니다"), read_q("노후한 전투기도 안전관리로 사고를 막을 수 있습니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("고비", "the critical moment; the climax; the peak; the crisis", "큰 수술을 받았지만 다행히 어려운 고비를 넘겼습니다."),
        ("마라톤", "marathon", "이번 마라톤 대회를 어디에서 개최합니까?"),
        ("슬기롭다", "to be wise; to be sensible", "온 국민이 힘을 모아 이번 위기를 슬기롭게 이겨냅시다.", "지혜롭다"),
        ("이겨내다", "to get through something despite hardship; to tough out something", "저희 어머니는 암을 이겨내고 건강을 되찾으셨습니다.", "극복하다"),
        ("인연", "(因緣) fate (in human relationships); destiny; karma", "우리가 이렇게 만난 것도 다 인연입니다.", "우연"),
        ("철길", "(鐵) a railroad; a railway; “iron/steel road”", "철길을 건널 때는 각별히 주의해야 합니다.", "철도, 철로"),
        ("철도원", "(鐵道員) a railroad worker; a railroad employee", "우리 아버지는 철도원으로 사십 년 동안 근무하셨습니다.", "철도 역무원"),
        ("철로변", "(鐵路邊) the side(s) of a railroad; a railroad shoulder", "철로변에서 아이들이 놀지 못하게 하세요.", "철도변 | 도로변, 고속도로변, 노변, 강변"),
        ("투병(하다)", "(鬪病) a fight/struggle against a disease (to fight/struggle against a disease)", "암 환자의 투병에 가장 어려운 것은 고통입니다."),
    ]),
    ("학습활동 2", [
        ("경량", "(輕量) lightweight", "국방부는 초경량 비행기 개발에 성공했습니다.", "중량"),
        ("공대공 미사일", "(空對空) an air-to-air missile", "전투기에는 공대공 미사일이 장착되어 있습니다.", "지대공, 지대지"),
        ("기관포", "(機關砲) a machine gun", "그 기관포의 구경은 얼마나 됩니까?"),
        ("기체", "(機體) the body of a plane; a fuselage; 기체 (氣體) gas", "기체에 결함이 발견되어 비행이 취소되었습니다."),
        ("낙후(성)", "(落後(性)) obsoleteness", "이 병원은 낙후된 장비를 모두 교체하기로 했습니다."),
        ("노후(화)", "(老朽(化)) aging; becoming obsolete", "이 근처 건물은 모두 지은 지 오래되어서 노후 정도를 검사하기로 했습니다.", "고령(화)"),
        ("논란", "(論難) controversy", "새로 개발된 약에 대해서 논란이 많습니다."),
        ("대만", "(臺灣) Taiwan", "이번 휴가에 대만에 다녀올 계획입니다."),
        ("마하", "Mach (air speed)", "전투기는 마하로 그 속도를 측정합니다."),
        ("부쩍", "remarkably; quickly", "박 일병의 한국말 실력이 부쩍 늘었다."),
        ("블랙박스", "black box", "비행기 사고가 났는데 블랙박스가 발견되지 않아 사고 원인을 밝히기가 어렵습니다."),
        ("수거(하다/되다)", "(收去) removal; taking away (to remove; to take away/to be removed)", "자원을 재활용하기 위해 안 쓰는 핸드폰을 수거하고 있다고 합니다."),
        ("시선", "(視線) one’s gaze; a glance; attention", "시선을 선생님에게 집중하세요!"),
        ("영공", "(領空) territorial air/sky; sovereign space", "이곳은 대한민국의 영공입니다.", "영토, 영해"),
        ("예단(하다)", "(豫斷) a prediction; forejudging; prejudging (to predict; to forejudge; to prejudge)", "이 사건의 범인에 관해 함부로 예단하는 것은 위험한 일입니다."),
        ("우려(하다)", "(憂慮) worry; concern (to worry about)", "이 프로그램의 폭력성에 대해 우려의 목소리가 높습니다."),
        ("위성항법장치", "(衛星航法裝置) a Global Positioning System; a global navigation satellite system; an electronic navigator", "요즘은 위성항법장치가 장착된 자동차가 많습니다."),
        ("의혹", "(疑惑) suspicion", "김 모 씨의 사망 원인에 대해 의혹이 많습니다.", "의심"),
        ("전담(하다)", "(專擔) exclusive responsibility; being in full charge (to bear exclusive responsibility)", "정 경관이 이번 사건을 전담하도록 하세요."),
        ("전비태세", "(戰備態勢) readiness for possible war", "해군의 전비태세를 검열하고 있습니다."),
        ("정황", "(情況) circumstances", "사건의 정황으로 볼 때 타살일 가능성이 높습니다."),
        ("조종사 사출", "(操縱士 射出) emergency ejection of a pilot", "조종사 사출 좌석이 작동이 되지 않는 전투기가 있어 안전이 우려되고 있습니다."),
        ("탑재(하다/되다)", "(搭載) loading; carrying (to load/to be loaded)", "이 핸드폰에는 스마트 칩이 탑재되어 있습니다."),
        ("항법 장비", "(航法 裝備) navigation system/equipment", "전투기의 항법 장비를 현대화하기 위해 국방부에서는 특별 예산을 편성하기로 했습니다."),
    ]),
    ("학습활동 3", [
        ("고백(하다)", "(告白) confession (to confess; to admit [one’s] guilt)", "내 친구에게 비밀을 고백했어요.", "자백"),
        ("다스리다", "to govern; to control; to punish", "저는 그때 화를 다스리기 위해서 숨을 크게 내쉬었습니다."),
        ("법정", "(法廷) a (legal) court", "당사자들끼리 문제를 해결하지 못해 법정으로 가서 해결하기로 했습니다."),
        ("분개(하다)", "(憤慨) indignation (to get indignant)", "새로운 법률 개정에 대해 분개하는 사람들이 많습니다."),
        ("불효(하다)", "(不孝) impiety/disobedience to one’s parents (to be impious/disobedient to one’s parents)", "부모님의 뜻을 거스르는 불효를 저지르지 마세요.", "효, 효도, 효심 | 불효자, 효자, 효녀"),
        ("순순히", "(諄諄) meekly; tamely; obediently", "제 뜻을 순순히 따라 주셔서 감사합니다."),
        ("심장마비", "(心臟痲痺) a heart attack; heart failure", "사인은 심장마비로 밝혀졌습니다."),
        ("애초(에)", "at first; at the start", "그 계획은 애초부터 잘못된 것이었습니다."),
        ("자수(하다)", "(自首) self-surrender (to surrender oneself to the authorities)", "그는 경찰에 자수하기로 결정했습니다."),
        ("절도", "(竊盜) theft; robbery", "최근에 발생한 차량 절도사건의 범인이 잡혔습니다.", "도둑(질)"),
        ("중벌", "(重罰) a severe punishment", "그런 흉악범에게는 중벌을 내려야 한다고 생각해요."),
        ("추궁(하다)", "(追窮) close interrogation; pressing hard (to interrogate closely; to press hard)", "경찰은 범인을 추궁해 자백을 받아 냈습니다."),
    ]),
    ("학습활동 4", [
        ("기적", "(奇蹟) a miracle", "삼 년 동안 식물인간으로 계시던 어머니가 깨어나시는 기적이 일어났어요."),
        ("냉동차", "(冷凍車) a refrigeration car; a refrigerated boxcar", ""),
        ("두들기다", "to pound; to knock; to beat", "문을 너무 세게 두들기지 마세요. 시끄러워요.", "두드리다"),
        ("몸부림(치다)", "a violent struggle; squirming (to struggle violently; to squirm)", "저는 성공하려고 몸부림쳤지만 실패하고 말았어요."),
        ("사체", "(死體) a dead body; a corpse", "강가에서 사체가 발견되었습니다.", "시체, 시신, 주검"),
        ("역경", "(逆境) adversity; adverse circumstances", "김 선생님은 온갖 역경을 이겨내고 성공했습니다.", "환경"),
        ("온도계", "(溫度計) a thermometer; “temperature calculating”", ""),
        ("절망(하다)", "(絶望) despair; hopelessness; “cut hope” (to despair; to lose hope)", "힘든 환경 속에서도 절망하지 않고 노력해서 성공을 이루었습니다.", "희망"),
        ("지탱(하다)", "(支撑) supporting; propping up; maintaining (to support; to prop up; to maintain)", "높은 인건비 때문에 점포를 지탱할 수 없어서 폐업 신고를 냈습니다.", "유지하다"),
        ("철도 역무원", "(鐵道 驛務員) a railroad employee; a railroader", "", "철도원"),
        ("한여름", "the middle of summer; midsummer", "한여름에는 시원한 냉면이 좋습니다.", "한겨울, 한밤(중)"),
    ]),
]
L7 = lesson(
    "U15 L2 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 철도원 · 투병 · 노후 · 영공 · 예단 · 의혹 · 전담 · 전비태세 · 자수 · 절도 · 중벌 · 역경 · 절망",
    requires=[],
    cards=vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=10)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 2: Accidents and Crimes (사고와 범죄)", [L1, L2, L3, L4, L5, L6, L7])
