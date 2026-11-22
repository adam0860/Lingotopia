"""Unit 56: KBC Semester III, Unit 15, Lesson 1 - Accidents (사고).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 15, Student's Edition.
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain

# ================================================================== L1 review
_W1 = [("죽다; 숨지다", "사망하다"), ("떨어지다", "추락하다"), ("(사건, 일이) 일어나다", "발생하다"), ("법을 어기다; 불법", "위반하다"), ("부딪치다; 부딪히다", "충돌하다"), ("차량이 뒤집히다", "전복되다"), ("차를 몰다", "운전하다")]
_W1E = [("사망하다", "to die; to pass away"), ("추락하다", "to fall; to crash"), ("발생하다", "to occur; to happen"), ("위반하다", "to violate; to break (a law)"), ("충돌하다", "to collide; to crash into"), ("전복되다", "to be overturned"), ("운전하다", "to drive")]
_W2 = [("목격자", "진술하다"), ("구조대", "출동하다"), ("선박", "침몰하다"), ("부상", "입다; 당하다"), ("안전벨트", "착용하다; 매다"), ("횡단보도", "건너다"), ("화재", "진화되다; 꺼지다"), ("음주운전", "금지되다")]
_W2E = [("목격자", "an eyewitness"), ("구조대", "a rescue team"), ("선박", "a ship; a vessel"), ("부상", "an injury; a wound"), ("안전벨트", "a seat belt"), ("횡단보도", "a crosswalk"), ("화재", "a fire"), ("음주운전", "drunk driving")]
_W2E2 = [("진술하다", "to state; to testify"), ("출동하다", "to be dispatched; to turn out"), ("침몰하다", "to sink"), ("착용하다", "to wear; to put on"), ("건너다", "to cross"), ("진화되다", "to be put out (a fire)"), ("금지되다", "to be prohibited")]
_HJ = [("車 차", "vehicle (on wheels); car", "주차장, 차도"), ("傷 상", "injury; scar", "상처, 부상"), ("線 선", "line", "차선, 중앙선"), ("速 속", "speed; velocity", "고속도로, 속력"), ("全 전", "whole; complete", "전국, 전부")]
_HJW = [("주차장", "a parking lot; “parking vehicle place”"), ("차도", "a road; “vehicle way”"), ("상처", "a scar"), ("부상", "a wound"), ("차선", "a (traffic) lane; “vehicle line”"), ("중앙선", "a center line; a median"), ("고속도로", "a highway; “high speed road”"), ("속력", "speed"), ("전국", "nationwide"), ("전부", "all; “whole part”")]
_OPP = [("대형차", "소형차", "a large car → a small car"), ("고속", "저속", "high speed → low speed"), ("완전", "불완전", "complete → incomplete"), ("국제선", "국내선", "an international route → a domestic route"), ("사망", "생존", "death → survival")]
_BOX3 = [("견인차, 소방차, 중형차", "차량", "a vehicle; vehicles"), ("중상, 화상, 경상", "부상", "an injury"), ("고속, 과속, 저속", "속도", "speed")]
_L1_EXTRA = [("대형차", "a large car"), ("소형차", "a small car"), ("고속", "high speed"), ("저속", "low speed"), ("과속", "speeding"), ("완전", "complete; perfect"), ("불완전", "incomplete"), ("국제선", "an international route"), ("국내선", "a domestic route"), ("사망", "death"), ("생존", "survival"), ("중상", "a serious injury"), ("경상", "a slight injury"), ("화상", "a burn"), ("견인차", "a tow truck"), ("소방차", "a fire engine"), ("중형차", "a mid-size car"), ("승용차", "a passenger car"), ("차량", "a vehicle"), ("속도", "speed"), ("증상", "a symptom"), ("단속", "a crackdown; regulation"), ("자가용", "a private car"), ("승합차", "a van"), ("전동차", "an electric train"), ("전복", "an overturn"), ("안전", "safety"), ("전역", "the whole region"), ("차선", "a (traffic) lane"), ("일호선", "Line 1")]
L1 = lesson(
    "U15 L1 · Review: accident words and Sino-Korean 車 傷 線 速 全",
    "사고 · 단어 복습 · 한자어 복습 · 사망하다 · 추락하다 · 충돌하다 · 전복되다 · 車 傷 線 速 全",
    requires=[],
    cards=[
        card("What Lesson 1 teaches", "Unit 15 (Semester III) is titled “Military, Security, and Geography” (군사, 안보 및 지리). Its ten lessons are Accidents, Accidents and Crimes, Crimes, Weather and Natural Disasters, Natural Disasters, Environment, World News, North Korea I, North Korea II and Military. Each lesson has a review of earlier words and Sino-Korean syllables (단어 및 한자어 복습), Part 1 (도입 학습, introduction), Part 2 (본 학습, main study) and Part 3 (심화 학습, advanced study), and each part ends with a list of the words and expressions of its activities (학습활동별 단어 및 표현). Lesson 1 is “Accidents” (사고)."),
        card("단어 복습 1: words with the same meaning (my answers)", "The book asks you to connect the words with the same meaning. The left side is the meaning from earlier semesters and the right side the word:", tables=[table(["Meaning", "Matching word"], [[a, b] for a, b in _W1], say=[1]), ktable(_W1E)]),
        card("단어 복습 2: words often used together (my answers)", "The book asks you to connect the words that are often used together:", tables=[table(["Word", "Word often used with it"], [[a, b] for a, b in _W2], say=[0]), ktable(_W2E), ktable(_W2E2)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ], say=[2]), ktable(_HJW)]),
        card("한자어 복습 1: the opposite word (my answers)", "The book asks you to circle the word whose meaning is the opposite of the word on the left (the book’s note: 상대적 can mean relative or opposite; here it means opposite). The options are listed with each row; my answers:", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [[a, b, c] for a, b, c in _OPP], say=[0, 1])]),
        card("한자어 복습 2: the word that includes all three (my answers)", "Read the three words and choose from the box the word that can include them all. The box: 승용차, 부상, 차량, 속도, 증상, 단속.", tables=[table(["The three words", "The word that includes them", "Meaning"], [[a, b, c] for a, b, c in _BOX3], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L1_EXTRA)]),
    ],
    exercises=uniq(
        _tr(_W1E, k=3) + _tr(_W2E, k=3) + _tr(_W2E2, k=3) + _tr(_HJW, k=3) + _tr([(a, b) for a, b in _L1_EXTRA], k=3)
        + [M("Which word means “to fall; to crash”?", "추락하다", ["충돌하다", "전복되다", "위반하다"], "떨어지다 = 추락하다."), M("Which word goes with 목격자?", "진술하다", ["출동하다", "침몰하다", "건너다"], "A witness states."), M("Which word goes with 구조대?", "출동하다", ["진술하다", "침몰하다", "착용하다"], "A rescue team turns out."), M("Which word goes with 선박?", "침몰하다", ["출동하다", "금지되다", "건너다"], "A ship sinks."), M("Which word goes with 안전벨트?", "착용하다", ["진술하다", "건너다", "금지되다"], "Wear a seat belt."), M("Which word goes with 횡단보도?", "건너다", ["착용하다", "진화되다", "침몰하다"], "Cross a crosswalk."), M("Which word goes with 화재?", "진화되다", ["건너다", "금지되다", "출동하다"], "A fire is put out."), M("Which word goes with 음주운전?", "금지되다", ["건너다", "진술하다", "진화되다"], "Drunk driving is prohibited."), M("What is the opposite of 저속?", "고속", ["과속", "속도", "속력"], "low speed ↔ high speed."), M("What is the opposite of 사망?", "생존", ["부상", "중상", "경상"], "death ↔ survival."), M("What is the opposite of 국내선?", "국제선", ["차선", "중앙선", "전복"], "domestic ↔ international."), M("What does the syllable 車 (차) mean?", "vehicle (on wheels); car", ["injury", "line", "speed"], "주차장."), M("What does the syllable 傷 (상) mean?", "injury; scar", ["line", "speed", "whole"], "상처."), M("What does the syllable 線 (선) mean?", "line", ["speed", "whole", "car"], "차선."), M("What does the syllable 速 (속) mean?", "speed; velocity", ["whole", "line", "injury"], "고속도로."), M("What does the syllable 全 (전) mean?", "whole; complete", ["car", "speed", "scar"], "전국."),
           F("목격자는 사고 상황을 ___. (to state)", "진술하다", ["출동하다", "침몰하다"], "진술하다."), F("구조대가 사고 현장에 ___. (turned out)", "출동했다", ["진술했다", "침몰했다"], "출동하다."), F("안전벨트를 꼭 ___ 하세요. (wear)", "착용", ["침몰", "진화"], "착용."), F("과속은 ___를 높이는 것입니다. (speed)", "속도", ["증상", "단속"], "속도."), F("고속도로는 속도가 ___ 도로입니다. (high)", "빠른", ["느린", "넓은"], "고속."),
           read_q("차량이 전복되었습니다"), read_q("선박이 침몰했습니다"), read_q("목격자가 사고를 진술했습니다"), read_q("고속도로에서 과속은 위험합니다"), read_q("안전벨트를 착용하세요")]
    ),
)


# ================================================================== L2 Part 1 texts
_SIGN = [("Using a cell phone while driving is dangerous.", "Do not drive after drinking alcohol.", "Buy this new hands-free device for safer driving."), ("Be aware of the damaging effects of wildfires.", "Pay attention to fire hazards and always be safe.", "Use matches instead of lighters to reduce greenhouse gases."), ("Looking for a missing vehicle", "Hiring an experienced driver", "Looking for a witness to an accident")]
_BLOG = [
    ("어제 오후에 저는 사촌언니 집에 가기 위해 오이도행 지하철을 탔어요.", "Yesterday afternoon I took a subway bound for Oido to go to my cousin’s (older sister’s) house."),
    ("한 시 사십 분께 금정역에 열차가 들어설 때 갑자기 열차가 흔들리더니 멈췄어요.", "At about 1:40, when the train was pulling into Geumjeong Station, the train suddenly shook and then stopped."),
    ("다들 놀라서 웅성웅성하는데, 기관사가 전동차가 선로를 이탈했다고 알려 주었어요.", "Everyone was startled and murmuring, and the engineer told us that the train had left the track."),
    ("다행히 지하철이 역으로 들어서기 위해 서행하고 있어서 크게 흔들리지는 않았어요.", "Fortunately the subway was moving slowly to enter the station, so it did not shake much."),
    ("그래서 다친 사람은 없는 것 같았어요.", "So it seemed that no one was hurt."),
    ("열차 안에서 삼십 분쯤을 기다리니까 열차 문이 열리더니 기관사가 내리라고 했어요.", "After I waited about thirty minutes inside the train, the train doors opened and the engineer told us to get off."),
    ("저는 내린 후 사촌언니한테 전화를 하고 다른 승객들과 같이 다음 열차를 탔는데, 어떤 사람들은 버스를 타기 위해 환불을 받기도 했어요.", "After getting off I phoned my cousin and took the next train with the other passengers, and some people even got a refund in order to take a bus."),
    ("집에 돌아와서 뉴스를 보니까 사고 소식이 나왔어요.", "When I came home and watched the news, the news of the accident was on."),
    ("아직 사고 원인은 알려지지 않았대요.", "They say the cause of the accident has not been made known yet."),
    ("사고는 정말 누구한테나 일어날 수 있나 봐요.", "It seems an accident can really happen to anyone."),
    ("그래도 큰 사고가 아니고 다친 사람도 없어서 너무 다행이에요.", "Still, it was not a big accident and no one was hurt, so I am very relieved."),
]
_SPEAK1 = [("최근에 일어난 사고나 아직도 기억하는 사고 뉴스가 있으면 이야기해 보세요.", "If there is an accident that happened recently or an accident news item you still remember, talk about it."), ("고향에서 자주 일어나는 사고를 생각해 보고 이야기해 보세요.", "Think about accidents that often happen in your hometown and talk about them.")]
L2 = lesson(
    "U15 L1 · Part 1 (도입 학습): signs and a blog about a train accident",
    "도입 학습 · 열차 사고 · 기관사 · 선로 이탈 · 서행 · 환불 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading): three pictures with signs",
             "The book shows three pictures with texts (a Kobaco ad and two edunet4u.net pictures) and asks you to check the English description that fits each picture best. The pictures and their Korean texts are not in the text of the book, so I cannot give the answers; the English choices are:",
             tables=[table(["Picture", "Choice 1", "Choice 2", "Choice 3"], [[str(i + 1), a, b, c] for i, (a, b, c) in enumerate(_SIGN)])]),
        card("학습활동 3 (Reading): a blog post, “열차 사고가 있었어요”",
             "The following text is from a blog (a notebook post dated 2010/07/24, 21:17). The book asks three questions in English. The English translation is mine; 1시 40분께 is written 한 시 사십 분께 and 30분쯤 is 삼십 분쯤.",
             examples=passage(_BLOG)),
        card("The three questions answered (mine)",
             "1. What happened yesterday? Include the time, location, and type of accident. At about 1:40 in the afternoon, at Geumjeong Station, the subway bound for Oido (the writer was going to her cousin’s house) suddenly shook and stopped: the train left the track (derailed) as it was pulling into the station.\n\n"
             "2. What did the passengers do after they got off the train? They waited about thirty minutes in the train, then got off when the doors opened; the writer phoned her cousin and took the next train with the other passengers, and some people got a refund to take a bus.\n\n"
             "3. Why were there no injuries? Because the subway was moving slowly to enter the station, so it did not shake much."),
        card("말해 봅시다! (speaking)", "Two speaking prompts of the book (the English is mine):", examples=passage(_SPEAK1)),
        card("Activities left out", "학습활동 2 (listening to three accident news clips from YTN, filling in the type of accident, its results and possible causes, then watching the video to check) is an audio and video activity."),
    ],
    exercises=uniq(
        _tr(_BLOG, k=3)
        + [M("What kind of vehicle did the writer take?", "A subway bound for Oido", ["A bus to Seoul", "A taxi", "A ferry"], "오이도행 지하철."), M("At what time did the train stop, roughly?", "About 1:40", ["About 4:10", "About 9:30", "About 11:00"], "한 시 사십 분께."), M("Where did it happen?", "Geumjeong Station", ["Seoul Station", "Incheon Airport", "Busan"], "금정역."), M("What did the engineer announce?", "The train had left the track", ["The train was late", "The doors were broken", "There was a fire"], "선로를 이탈했다."), M("Why was the shaking not big?", "The subway was moving slowly to enter the station", ["The train was empty", "The track was new", "The brakes were new"], "서행."), M("How long did the writer wait in the train?", "About thirty minutes", ["About three minutes", "About two hours", "About a day"], "삼십 분쯤."), M("What did the writer do after getting off?", "Phoned her cousin and took the next train", ["Walked home", "Called a taxi", "Went back inside"], "사촌언니한테 전화."), M("What did some passengers get to take a bus?", "A refund", ["A free ticket", "A taxi", "A meal"], "환불."), M("Was the cause of the accident known yet?", "No", ["Yes, a fire", "Yes, a storm", "Yes, a crash"], "알려지지 않았대요."), M("How does the writer feel at the end?", "Relieved that nobody was hurt", ["Angry", "Bored", "Afraid"], "다행이에요."),
           F("기관사가 전동차가 선로를 ___했다고 알려 주었어요. (left the track)", "이탈", ["충돌", "추락"], "선로를 이탈."), F("지하철이 역으로 들어서기 위해 ___하고 있었어요. (moving slowly)", "서행", ["급행", "완행"], "서행."), F("어떤 사람들은 버스를 타기 위해 ___을 받았어요. (a refund)", "환불", ["진술", "단속"], "환불."), F("아직 사고 ___은 알려지지 않았대요. (cause)", "원인", ["결과", "소식"], "원인."), F("다친 사람이 없어서 너무 ___이에요. (a relief)", "다행", ["부상", "사고"], "다행."),
           read_q("어제 오후에 오이도행 지하철을 탔어요"), read_q("열차가 갑자기 흔들리더니 멈췄어요"), read_q("기관사가 전동차가 선로를 이탈했다고 알려 주었어요"), read_q("다친 사람이 없어서 너무 다행이에요"), read_q("사고는 정말 누구한테나 일어날 수 있나 봐요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("기관장", "(機關長) a chief engineer (of a ship)", "부산 앞바다 해역에서 발생한 선박사고로 김 모 기관장 등 다섯 명이 사망했습니다.", "기관사"),
        ("기름띠", "oil spill (on the surface of the water); “oil belt” or “oil streak”", "바다의 기름띠를 제거하기 위해 정부와 환경단체가 노력하고 있다."),
        ("당시", "(當時) a point in the past; at that time; then", "그 당시 저는 출근하는 길이었습니다. 사고가 나던 당시 저는 운전석 옆에 앉아 있었어요."),
        ("뚫다", "to punch (a hole); to perforate; to penetrate; to pierce", "추락한 비행기 파편들이 주변 건물의 지붕을 뚫고 떨어졌습니다."),
        ("~(으)로 미뤄", "judging by; judging from", "목격자의 진술로 미뤄 사고가 한 시에서 한 시 반 사이에 일어난 것 같다."),
        ("비탈길", "a slope; an incline; a hill; “slope road”", "눈이 와서 길이 미끄러워요. 특히 집 앞 비탈길에서는 각별히 조심하세요."),
        ("빗길", "a wet road; “rain road”", "빗길에 차가 미끄러지면서 사고가 났습니다."),
        ("합선(하다/되다)", "(合線) short circuit; “joined wires” (to short-circuit/to be short-circuited)", "경찰은 이번 화재가 호텔 오 층에서 전기 합선으로 발생한 것으로 보고 있다.", "누전"),
    ]),
    ("학습활동 3", [
        ("서행(하다)", "(徐行) going slowly; crawling; driving/cruising slowly (to go slowly; to drive slowly)", "학교 앞에서는 서행해야 합니다.", "주행, 급행, 완행"),
        ("웅성웅성하다", "to be noisy; to be astir; to be in a (state of) commotion", "사람들이 웅성웅성하는 소리가 나서 가 보니 어린 아이가 쓰러져 있었어요.", "웅성거리다"),
        ("~행", "(行) heading to/for; bound", "서울발 부산행 열차 미국행 비행기", "~발"),
    ]),
]
L3 = lesson(
    "U15 L1 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 기관장 · 기름띠 · 당시 · 뚫다 · 빗길 · 합선 · 서행 · 웅성웅성하다 · ~행",
    requires=[],
    cards=vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=6, nread=6)),
)


# ================================================================== L4 Part 2 texts
_BR = [("잠실대교", "Jamsil Bridge"), ("반포대교", "Banpo Bridge"), ("성산대교", "Seongsan Bridge"), ("한남대교", "Hannam Bridge"), ("성수대교", "Seongsu Bridge"), ("마포대교", "Mapo Bridge"), ("영동대교", "Yeongdong Bridge"), ("인천대교", "Incheon Bridge")]
_INC = [
    ("삼 일 오후 한 시 십 분께 인천시 중구 운서동 인천대교 공항 방향 영종 아이씨 톨게이트를 삼백 미터가량 지난 지점에서 운전사 정 모 (쉰다섯 살) 씨 등 스물네 명이 탑승한 고속버스가 도로 밑으로 추락해 열두 명이 숨지고 열두 명이 부상했다.", "On the 3rd at about 1:10 in the afternoon, at a point about 300 meters past the Yeongjong IC tollgate in the airport direction of the Incheon Bridge in Unseo-dong, Jung-gu, Incheon, an express bus carrying 24 people including the driver Mr. Jung (55) fell off the road; 12 people died and 12 were injured."),
    ("사고가 난 고속버스는 경북 포항을 출발해 인천국제공항으로 향하고 있었다.", "The express bus that had the accident had left Pohang, North Gyeongsang, and was heading for Incheon International Airport."),
    ("경찰과 소방 당국은 현재까지 사망자 열두 명 가운데 설해용 (예순 살), 임찬호 (마흔두 살), 이시형 (마흔여섯 살) 씨 등 세 명의 신원을 확인했다.", "The police and fire authorities have so far confirmed the identities of three of the 12 dead, including Mr. Seol Hae-yong (60), Mr. Im Chan-ho (42) and Mr. Lee Si-hyeong (46)."),
    ("경찰은 사상자 신원을 계속 확인하는 한편 정확한 사고 경위를 조사 중이다.", "While continuing to confirm the identities of the casualties, the police are investigating the exact circumstances of the accident."),
]
_ROAD = [
    ("도로 위에서 차량이 멈춰 서면 어떻게 해야 할까?", "What should you do if a vehicle stops on the road?"),
    ("고장이나 타이어 펑크, 연료 부족으로 차가 멈추면 갓길 등 안전한 장소로 차를 옮기는 것이 우선이다.", "If the car stops because of a breakdown, a flat tire or lack of fuel, the first thing is to move the car to a safe place such as the shoulder."),
    ("교차로나 건널목에서 시동이 꺼지면, 기어를 중립에 놓고 차를 밖에서 밀어서 옮겨야 한다.", "If the engine dies at an intersection or a railroad crossing, you must put the gear in neutral and push the car from outside to move it."),
    ("타이어가 펑크 났을 때는 비상경고 등을 켜고 운전대를 손으로 강하게 잡은 상태에서 엔진 브레이크를 이용해 속도를 떨어뜨린 뒤 가볍게 브레이크를 밟아 정지하는 것이 좋다.", "When a tire goes flat, it is good to turn on the hazard lights, use the engine brake with your hands gripping the steering wheel firmly to reduce speed, and then lightly step on the brake to stop."),
    ("고속도로나 자동차 전용도로에선 비상경고 등을 켜고 안전삼각대를 설치해야 한다.", "On a highway or a motorway you must turn on the hazard lights and set up a safety triangle."),
    ("안전삼각대 설치 뒤엔 가드레일 밖 안전지대로 나가, 경찰이나 보험사에 전화로 연락하면 된다.", "After setting up the safety triangle, go out to a safe zone outside the guard rail and contact the police or the insurance company by phone."),
]
_ROADT = [["The engine has died at an intersection", "Put the gear in neutral and push the car out from outside to move it"], ["The car got a flat tire", "Turn on the hazard lights, grip the steering wheel firmly with both hands, use the engine brake to reduce speed, then lightly step on the brake and stop"], ["The car has a problem on the highway", "Turn on the hazard lights and set up the safety triangle, then go to a safe zone outside the guard rail and phone the police or the insurance company"]]
_SPEAK2 = [("교통사고를 당해 본 적이 있습니까?", "Have you ever been in a traffic accident?"), ("교통사고를 목격한 적이 있습니까?", "Have you ever witnessed a traffic accident?"), ("언제 어디서 어떤 일이 있었는지 친구와 말해 보세요.", "Tell a friend when and where it happened and what happened.")]
L4 = lesson(
    "U15 L1 · Part 2 (본 학습): bridges, a bus crash on Incheon Bridge and car trouble",
    "본 학습 · ~대교 · 인천대교 · 고속버스 추락 · 신원 확인 · 갓길 · 비상경고 등 · 안전삼각대",
    requires=[],
    cards=[
        card("알아봅시다: ~대교",
             "In traffic reports about Seoul and Incheon, you often hear words that end with ~교 or ~대교, as in 잠실대교, 반포대교, 성산대교, 한남대교, 성수대교, 마포대교, 영동대교, 인천대교, etc. They all refer to bridges; ~교 means “a bridge” and ~대교 means “a large bridge.” All these bridges but 인천대교 are on the Han River, which cuts through Seoul. As the name suggests, 인천대교 is in Incheon and connects Incheon International Airport, which is on an island, with the mainland. The bridge opened in October 2009, and the direct access between the airport and the mainland reduces travel time from Seoul by as much as an hour.",
             tables=[ktable(_BR)]),
        card("학습활동 1 (Reading): a news article about a traffic accident on Incheon Bridge",
             "The following is a newspaper article (Yonhapnews) about a traffic accident on Incheon Bridge. The book asks you to read it and summarize it in English. The text is the book’s with the numbers spelled out (3일 is 삼 일, 1시10분께 is 한 시 십 분께, 영종IC is 영종 아이씨, 300 m is 삼백 미터, ages as 살, 24명 is 스물네 명, 12명 is 열두 명); the English is mine.",
             examples=passage(_INC)),
        card("My summary of the article", "On the afternoon of the 3rd, an express bus from Pohang heading for Incheon International Airport fell off Incheon Bridge about 300 m past the Yeongjong IC tollgate. Twenty-four people were aboard; 12 died and 12 were injured. The police and fire authorities had confirmed the identities of three of the dead and were investigating the exact circumstances."),
        card("학습활동 3 (Reading): a newspaper article on road traffic safety",
             "The following newspaper article is about road traffic safety (Hankyoreh). The book asks you to choose the phrase that can replace the underlined 멈춰 서면 (A. 세우면, B. 정지하면, C. 정거하면, D. 착륙하면) and to write in a table the suggested action for three car problems. The English is mine.",
             examples=passage(_ROAD)),
        card("The questions answered (mine)", "1. 멈춰 서면 (comes to a stop) can be replaced by B. 정지하면 (stops): 세우면 means to stop something, 정거하면 is to stop at a station and 착륙하면 is to land.\n\n2. The table:", tables=[table(["Car problem", "Suggested action"], [list(r) for r in _ROADT])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK2)),
        card("Activities left out", "학습활동 2 (an interview about the accident from YTN: identifying the interviewee, then completing four sentences with the missing words from the video and numbering them in time order) is an audio and video activity."),
    ],
    exercises=uniq(
        _tr(_BR, k=3) + _tr(_INC, k=3) + _tr(_ROAD, k=3)
        + [M("What do ~교 and ~대교 mean?", "A bridge and a large bridge", ["A road and a highway", "A river and a lake", "A station and a stop"], "The book’s note."), M("Which of the bridges is not on the Han River?", "인천대교", ["잠실대교", "마포대교", "한남대교"], "인천대교 is in Incheon."), M("What does 인천대교 connect?", "Incheon International Airport and the mainland", ["Seoul and Busan", "Two islands", "Jeju and the mainland"], "The book’s note."), M("When did 인천대교 open?", "October 2009", ["October 1999", "May 2012", "March 2005"], "The book’s note."), M("What happened on 인천대교?", "An express bus fell off the road", ["A train derailed", "A ship sank", "A plane crashed"], "추락해."), M("How many people were aboard the bus?", "24", ["12", "55", "300"], "스물네 명."), M("How many died?", "12", ["24", "3", "55"], "열두 명이 숨지고."), M("Where was the bus coming from?", "Pohang", ["Incheon", "Seoul", "Busan"], "포항."), M("Where was it going?", "Incheon International Airport", ["Seoul Station", "Pohang", "Busan"], "인천국제공항."), M("How many dead had been identified?", "Three", ["Twelve", "All", "None"], "세 명."), M("What is the first thing to do when a car stops?", "Move the car to a safe place such as the shoulder", ["Call a friend", "Leave the car", "Turn off the lights"], "우선."), M("What should you do if the engine dies at an intersection?", "Put the gear in neutral and push the car out", ["Keep driving", "Honk", "Call a friend"], "중립."), M("What should you turn on when a tire goes flat?", "The hazard lights", ["The radio", "The wipers", "The heater"], "비상경고 등."), M("What must you set up on a highway?", "A safety triangle", ["A tent", "A sign of the shop", "A flag"], "안전삼각대."), M("Whom should you contact after reaching the safe zone?", "The police or the insurance company", ["The school", "The post office", "A hotel"], "경찰이나 보험사."),
           F("인천대교 공항 방향 영종 아이씨 ___를 삼백 미터가량 지난 지점. (tollgate)", "톨게이트", ["갓길", "기어"], "톨게이트."), F("경찰은 사상자 ___을 계속 확인하고 있다. (identity)", "신원", ["지점", "경위"], "신원."), F("차를 안전한 장소로 옮기는 것이 ___이다. (first)", "우선", ["중립", "경고"], "우선."), F("기어를 ___에 놓고 차를 밀어서 옮겨야 한다. (neutral)", "중립", ["우선", "경고"], "중립."), F("고속도로에서는 ___를 설치해야 한다. (safety triangle)", "안전삼각대", ["톨게이트", "룸미러"], "안전삼각대."),
           read_q("인천대교에서 고속버스가 추락했습니다"), read_q("경찰은 사고 경위를 조사하고 있습니다"), read_q("차가 멈추면 갓길로 옮기는 것이 우선입니다"), read_q("기어를 중립에 놓고 차를 밀어서 옮기세요"), read_q("안전삼각대를 설치해야 합니다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("신원", "(身元) identity", "신원이 확실하지 않으면 취직할 때 어렵다."),
        ("지점", "(地點) a spot (on the ground); a place; “earth spot”", "사고 지점이 확실하지 않습니다."),
        ("톨게이트", "a toll gate", "", "(통행) 요금소"),
    ]),
    ("학습활동 2", [
        ("급정거(하다)", "(急停車) sudden stop (of a vehicle); screeching halt; “urgent halt of a vehicle” (to come to a screeching halt)", "버스가 급정거하는 바람에 사고가 났습니다.", "급정차"),
        ("덮치다", "to raid; to attack; to swoop; to strike", "거대한 쓰나미가 해안가 마을을 덮쳤습니다."),
        ("룸미러", "a rearview mirror; “room mirror”", "", "백미러 (“back mirror”)"),
        ("미처", "yet; before (This adverb is used only in negative sentences.)", "청소도 미처 다 끝내기 전에 손님들이 도착했다. 뒤에서 오는 차를 미처 보지 못했다.", "아직"),
        ("박다", "to slam into; to drive into", "화물차가 도로 난간을 박고 십 미터 아래로 떨어졌습니다.", "들이박다"),
        ("부근", "(附近) vicinity; neighborhood", "이 부근에 우체국이 어디 있어요?", "근처, 인근"),
        ("인제", "filler in colloquial language", "우리 밥 먹었으니까 인제 후식을 먹읍시다.", "이제"),
        ("정차(하다)", "(停車) stopping (of a car) (to stop a car; to come to a stop)", "이 열차는 다음 역에서 삼 분간 정차하겠습니다.", "정거, 주차"),
        ("튀다", "to spring up; to bounce", "축구공이 튀어서 제 얼굴을 때렸어요."),
        ("튕겨 나가다", "to be hurled out; to be catapulted out; to bounce out", "충돌 순간 몸이 차 밖으로 튕겨 나갔습니다.", "튕기다"),
        ("틀다", "to turn; to twist", "라디오를 틀어 사고 소식을 들었습니다. 몸을 틀어서 사고 차량의 유리 파편을 피했습니다."),
        ("하여튼", "anyway; at any rate", "하여튼 곧 연락드릴 테니 기다려 주세요.", "여하튼, 어쨌든"),
        ("휘청하다", "to lurch; to stagger", "앞에 가던 남자가 휘청하더니 쓰러졌다."),
        ("IC/인터체인지", "a highway ramp; “interchange”", "화성 아이씨 오산 아이씨", "나들목"),
    ]),
    ("학습활동 3", [
        ("갓길", "the shoulder (of a road); “side road”", "차에 문제가 생겨서 갓길에 세워야겠어요."),
        ("경고(하다)", "(警告) warning (to warn)", "물에 들어가지 말라는 경고를 무시하고 수영을 하던 사람이 익사사고를 당했습니다."),
        ("기어", "a gear", "후진 기어를 넣고 천천히 차를 뒤로 빼세요."),
        ("떨어뜨리다", "to drop (a thing or person to the ground)", "이 랩톱 컴퓨터를 땅에 떨어뜨리지 마세요."),
        ("밀다", "to push", "뒤에서 어떤 사람이 저를 밀어서 넘어졌어요.", "당기다"),
        ("밟다", "to step on", "운전하는데 갑자기 어린아이가 뛰어 나와서 급하게 브레이크를 밟았어요."),
        ("(안전)삼각대", "((安全)三脚臺) a warning triangle; “(safety) tripod”", "자동차가 길에서 멈추면 반드시 안전삼각대를 세워야 한다."),
        ("우선", "(于先) first; above all", "우선 회원들의 의견을 다 들어 보고 결정합시다.", "먼저, 무엇보다도"),
        ("중립", "(中立) neutral(ity)", "자동차 기어를 중립에 놓으세요. 스위스는 중립국가입니다."),
    ]),
]
L5 = lesson(
    "U15 L1 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 급정거 · 덮치다 · 미처 · 박다 · 정차 · 튕겨 나가다 · 갓길 · 밟다 · 안전삼각대 · 중립",
    requires=[],
    cards=vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=10, nread=8)),
)


# ================================================================== L6 Part 3 text
_MOTO = [
    ("교통경찰관으로 오토바이 사고 신고를 접하면 가슴부터 쓸어내린다.", "As a traffic police officer, when I receive a report of a motorcycle accident, my heart sinks first."),
    ("오토바이 사고는 일반 승용차와 비교해 부상 정도가 크고 조금만 충격을 받아도 사망에 이르는 경우가 많기 때문이다.", "This is because motorcycle accidents, compared with ordinary passenger cars, involve a greater degree of injury, and in many cases even a slight impact leads to death."),
    ("올해 들어 해운대 경찰서 관할에서 오토바이로 인한 교통사고만 사십일 건이 발생했다.", "So far this year, 41 traffic accidents caused by motorcycles alone have occurred in the jurisdiction of Haeundae Police Station."),
    ("이 가운데 네 명이 소중한 생명을 잃었다.", "Of these, four people lost their precious lives."),
    ("오토바이 사고를 줄이는 방법은 결코 복잡하지 않다.", "The way to reduce motorcycle accidents is by no means complicated."),
    ("아주 단순하다.", "It is very simple."),
    ("우선 규정속도를 지키도록 하자.", "First, let us keep to the speed limit."),
    ("또한 차선을 바꿀 때는 반드시 좌우측 지시등(깜박이)을 사용하는 것도 자신의 생명을 안전하게 지킬 수 있는 좋은 방법이다.", "Also, always using the left and right turn signals (blinkers) when changing lanes is another good way to keep your own life safe."),
    ("이와 함께 오토바이를 탈 때는 어떤 경우에도 안전모를 써야 한다.", "Along with this, when riding a motorcycle you must wear a safety helmet in any case."),
    ("젊은이들은 헤어 스타일이 구겨진다거나 답답하다는 이유 등을 들어 안전모를 기피하는 일이 많다.", "Young people often avoid helmets, citing reasons such as that their hairstyle gets crushed or that it feels stuffy."),
    ("하지만 안전모 착용이라는 불편과 생명 두 가지를 놓고 생각해 보면 어떤 게 현명한 일인지 자명하다.", "But if you think about the two things, the inconvenience of wearing a helmet and life, which is the wise thing is obvious."),
    ("일인당 국민소득 일만 달러 시대를 살아가면서 오토바이 운전자들이 좀 더 성숙되고 자발적인 준법정신과 자기 생명의 존귀함을 마음에 새겼으면 하는 바람 간절하다.", "Living in an era of 10,000 dollars of national income per person, I earnestly hope that motorcycle drivers will engrave in their hearts a more mature and voluntary law-abiding spirit and the nobility of their own lives."),
]
_SPEAK3 = [("여름철과 겨울철에 가장 많이 발생하는 안전사고는 뭐라고 생각합니까?", "What do you think are the safety accidents that occur most in summer and in winter?"), ("원인과 예방책을 말해 봅시다.", "Let us talk about the causes and preventive measures."), ("오토바이나 자동차 사고를 줄이기 위해 어떤 방법을 실행해야 할까요?", "What methods should be put into practice to reduce motorcycle and car accidents?"), ("반 친구들과 토론해 보세요.", "Discuss it with your classmates.")]
L6 = lesson(
    "U15 L1 · Part 3 (심화 학습): a reader’s column on motorcycle accidents",
    "심화 학습 · 오토바이 사고 · 안전모 · 규정속도 · 지시등 · 준법정신",
    requires=[],
    cards=[
        card("학습활동 3 (Reading): a column by a traffic police officer",
             "The following is a reader’s column in a newspaper (Hankyoreh). The book asks four questions in English (the best title, the advice given, a translation of the underlined sentence, and the article’s purpose). The text is the book’s with the numbers spelled out (41건 is 사십일 건, 4명 is 네 명, 1인당 is 일인당, 1만 달러 is 일만 달러); the English is mine. The underlined sentence is not marked in the text of the book.",
             examples=passage(_MOTO)),
        card("The questions answered (mine)",
             "1. The most appropriate title: B. How to protect yourself from motorcycle accidents (the options were A. how to get a motorcycle driver’s license, C. why motorcycle accidents are more harmful than others, D. why young drivers are involved in motorcycle accidents).\n\n"
             "2. The instructions and advice given: keep to the speed limit; always use the left and right turn signals when changing lanes; always wear a safety helmet when riding a motorcycle.\n\n"
             "3. The sentence that most likely carries the underline is the one comparing the inconvenience of a helmet with life (translated above: “if you think about the two things … which is the wise thing is obvious”).\n\n"
             "4. The purpose of the article: A. to persuade."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK3)),
        card("Activities left out", "학습활동 1 (a YTN news segment about escalator accidents in summer: categories of accidents, advice, and the meaning of the percentages 32.1%, 87.0% and 69.5%) and 학습활동 2 (a KBS accident news clip: the type and cause of the accident and what the 경비원 and the 119 구조대 did) are audio activities."),
    ],
    exercises=uniq(
        _tr(_MOTO, k=3)
        + [M("Who wrote the column?", "A traffic police officer", ["A doctor", "A teacher", "A bus driver"], "교통경찰관."), M("Why are motorcycle accidents so serious?", "Injuries are bigger and even a slight impact often causes death", ["Roads are narrow", "Motorcycles are fast only", "Drivers are young"], "부상 정도가 크고."), M("How many motorcycle accidents happened in Haeundae this year?", "41", ["4", "14", "400"], "사십일 건."), M("How many people died of those?", "Four", ["Forty-one", "Fourteen", "None"], "네 명."), M("What is the first piece of advice?", "Keep to the speed limit", ["Wear a helmet", "Buy a new bike", "Drive at night"], "규정속도를 지키도록 하자."), M("What should be used when changing lanes?", "Turn signals", ["The horn", "The brake", "The helmet"], "지시등."), M("What must a rider always wear?", "A safety helmet", ["A raincoat", "Gloves only", "A jacket"], "안전모."), M("Why do young people avoid helmets?", "They think it ruins their hairstyle or feels stuffy", ["They are too expensive", "They are heavy", "They are illegal"], "헤어 스타일이 구겨진다거나."), M("What does the writer hope for?", "A more mature, voluntary law-abiding spirit and respect for life", ["Higher incomes", "More roads", "Cheaper bikes"], "준법정신과 존귀함."), M("What is the purpose of the article?", "To persuade", ["To describe", "To reproach", "To debate"], "A."),
           F("오토바이를 탈 때는 어떤 경우에도 ___를 써야 한다. (safety helmet)", "안전모", ["지시등", "고무"], "안전모."), F("우선 ___속도를 지키도록 하자. (the speed limit)", "규정", ["단순", "성숙"], "규정속도."), F("차선을 바꿀 때는 반드시 ___을 사용해야 한다. (turn signals)", "지시등", ["안전모", "기어"], "지시등."), F("오토바이 사고를 줄이는 방법은 아주 ___. (simple)", "단순하다", ["복잡하다", "위험하다"], "단순하다."), F("오토바이 사고는 부상 ___가 크다. (degree)", "정도", ["지점", "원인"], "정도."),
           read_q("오토바이 사고는 부상 정도가 큽니다"), read_q("규정속도를 지키도록 하자"), read_q("차선을 바꿀 때는 반드시 지시등을 사용해야 합니다"), read_q("오토바이를 탈 때는 안전모를 써야 합니다"), read_q("안전모를 쓰는 것이 현명한 일입니다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("가급적", "(可及的) as … as possible", "가급적 빨리 일을 끝내세요."),
        ("각별하다", "(各別) to be special; to be particular", "이 선물은 저에게 아주 각별합니다.", "특별하다"),
        ("고무", "rubber", "설거지할 때는 꼭 고무장갑을 끼고 하세요."),
        ("습기", "(濕氣) moisture; humidity", "장마철에는 집안에 습기가 가득 차니까 환기를 자주 시켜야 해요."),
        ("영·유아", "(嬰·幼兒) infants and toddlers", "이 동네에 영·유아들을 위한 보육 시설이 생긴다고 합니다.", "소아"),
        ("얇다", "to be thin", "날씨가 많이 쌀쌀해졌으니까 얇은 옷을 입지 말고 더 따뜻하게 입으세요.", "두껍다"),
        ("~에 끼이다", "to become jammed in; to become stuck in", "손이 자동차 문에 끼였다."),
        ("재질", "(材質) the quality (of materials like wood, iron, plastic, etc.); “material quality”", "재질이 좋은 가구는 값이 비쌉니다."),
    ]),
    ("학습활동 2", [
        ("남의 일 같지 않다", "to be (too) important (to be ignored); to feel it is one’s own business; “feel like it is not other people’s business”", "이웃집 아이가 다쳤는데, 정말 남의 일 같지 않아서 걱정이 많이 돼요."),
        ("무려", "(無慮) whopping (a word that emphasizes a number when preceding it)", "이번 세일기간에 무려 삼십만 명의 고객이 우리 백화점을 찾았습니다."),
        ("배기가스", "(排氣) exhaust emission; “emitted gas”", "서울시는 자동차의 배기가스 배출량을 줄이기 위해 노력하고 있습니다."),
        ("순찰(하다)", "(巡察) patrolling (to patrol)", "경찰이 저녁마다 이 구역을 순찰합니다."),
        ("시기", "(時期) a time; a period", "장마가 오는 시기에는 전염병을 조심해야 합니다."),
        ("아찔하다", "to be dizzy; to be giddy; to be faint", "버스가 가드레일에 충돌한 아찔한 사건이 있었습니다."),
        ("유독가스", "(有毒) toxic gas; “poison gas”", "공장에서 발생한 화재에 유독가스 배출이 많아서 인명 피해가 많다고 합니다."),
        ("일산화탄소", "(一酸化炭素) carbon monoxide", "앞으로는 모든 가정에 일산화탄소 측정기를 달아야 합니다.", "이산화탄소"),
        ("작동(하다)", "(作動) operation (of a machine) (to operate; to work)", "오늘 하루 종일 사무실의 에어컨이 작동하지 않았습니다."),
        ("중태", "(重態) critical condition; “serious condition”", "교통사고 환자가 중태입니다."),
        ("화를 부르다", "(禍) to cause trouble/a disaster; “call for disaster”", "정부의 조치가 화를 불렀다."),
    ]),
    ("학습활동 3", [
        ("간절하다", "(懇切) to be ardent; to be earnest", "아버님이 암을 극복했으면 하는 마음이 간절합니다."),
        ("규정", "(規定) a rule; a regulation", "여기서 담배를 피우는 것은 규정을 어기는 것입니다."),
        ("단순하다", "(單純) to be simple; to be simpleminded; “simple and pure”", "이 일은 너무 복잡하게 생각하지 말고 단순하게 생각해 봅시다."),
        ("마음에 새기다", "to take something to heart; to commit to; “engrave in one’s heart”", "선생님의 충고를 마음에 새기세요."),
        ("성숙(하다)", "(成熟) maturity (to be mature)", "이 아이는 나이에 비해서 굉장히 성숙해 보입니다."),
        ("안전모 착용", "(安全帽 着用) wearing a safety helmet", "자전거를 타거나 오토바이를 탈 때는 꼭 안전모를 착용하세요."),
        ("오토바이", "a motorcycle; “autobi(ke)”", "오토바이 사고는 인명 피해가 크니까 조심하세요."),
        ("자명하다", "(自明) to be self-explanatory; to be obvious", "이 일은 실패할 것이 자명합니다.", "분명하다"),
        ("자발적", "(自發的) voluntary", "시민들의 자발적 참여를 유도하기 위해 홍보를 하고 있습니다."),
        ("접하다", "(接) to be in touch with; to be in contact with; to adjoin; to border", "독서를 통해 다른 나라의 문화를 접할 수 있습니다."),
        ("존귀(하다)", "(尊貴) nobility; “noble and precious” (to be noble)", "불교에서는 모든 생명을 존귀하게 여깁니다.", "존엄하다"),
        ("준법", "(遵法) law-abiding", "어렸을 때부터 준법정신에 대한 교육을 받아야 합니다."),
        ("충격", "(衝擊) a shock; an impact", "아버지는 사업의 실패로 충격을 받으셨어요."),
        ("현명(하다)", "(賢明) wisdom; good sense (to be wise; to be sensible)", "어려움을 해결하기 위해서는 현명한 결정이 필요합니다.", "지혜롭다"),
    ]),
]
L7 = lesson(
    "U15 L1 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가급적 · 습기 · 재질 · 무려 · 배기가스 · 순찰 · 유독가스 · 중태 · 규정 · 자명하다 · 충격",
    requires=[],
    cards=vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=14, nread=8)),
)

UNIT = unit("Semester III · Unit 15 · Lesson 1: Accidents (사고)", [L1, L2, L3, L4, L5, L6, L7])
