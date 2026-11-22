"""Unit 17: KBC Semester 1, Unit 3, Chapter 10 - On the Way to Los Angeles (로스앤젤레스 가는 길에).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 3, Student's Edition (2022).
Audio, video clips, pictures, maps, SMART Board activities, games, role-plays, partner and class activities are
left out. The book gives no English for its dialogs and leaves the answers to its exercises blank: every translation
of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


def _ig(n):
    return particle(n, ("이", "가"))


# ================================================================== Vocabulary builder and means of transportation
_WORDMAP = [("1", "A new vocabulary word", "비싸다"), ("3", "A description of the picture", "옷이 너무 비싸요. 옷이 칠백 달러예요."), ("4", "Your own Korean definition of the new word", "가격이 높아요."), ("5", "An antonym or a synonym (the book writes ↔ 싸다)", "싸다")]
_TRANS = [["비행기", "공항"], ["기차/열차", "역"], ["버스", "정류장"], ["지하철", "역"], ["고속버스", "터미널"], ["배", "항구"]]
_BINGO = [("비행기 타는 곳입니다.", "공항"), ("아주 빠른 버스입니다.", "고속버스"), ("사거리에 있는 등입니다.", "신호등"), ("고속도로에서 나가는 곳입니다.", "출구"), ("기름을 넣는 곳입니다.", "주유소"), ("어머니의 아버지입니다.", "외할아버지"),
          ("형님의 아내입니다.", "형수"), ("아버지 동생의 부인입니다.", "작은어머니"), ("어머니의 언니입니다.", "이모"), ("이모의 아들입니다.", "사촌"), ("형의 아들입니다.", "조카"), ("지하철이나 기차를 타는 곳입니다.", "역")]
_BINGO_EN = {"공항": "an airport", "고속버스": "an express bus", "신호등": "a traffic signal light", "출구": "an exit", "주유소": "a gas station", "외할아버지": "a maternal grandfather", "형수": "an older brother’s wife", "작은어머니": "the wife of a father’s younger brother",
             "이모": "a mother’s sister", "사촌": "a cousin", "조카": "a nephew; a niece", "역": "a station"}
L1 = lesson(
    "Ch 10 · Vocabulary builder: a word map card and means of transportation",
    "로스앤젤레스 가는 길에 · 교통 수단 · 타는 곳 · 비싸다 ↔ 싸다 · 빙고",
    requires=[],
    cards=[
        card("What Chapter 10 teaches (로스앤젤레스 가는 길에)",
             "Chapter 10, “On the Way to Los Angeles”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about trip planning, including the means of transportation; compare two things or people; give and understand directions; and use the proper kinship terms for an extended family.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the comparative 보다 (더) (more … than; …er than); the conjunctive ending -기 때문에 (because); ~때문에 (because of); the attributive forms of action verbs -는, -(으)ㄴ and -(으)ㄹ; and the Sino-Korean syllables 부 (父), 모 (母), 출 (出), 입 (入) and 구 (口)."),
        card("Strategy: organize a word map card",
             "Earlier you were introduced to flash cards. They work because the words are easy to access and you can review them readily and repeatedly. As you become more proficient in Korean you may want more than an example sentence on a card: your own Korean definition, antonyms, synonyms, and a drawing that illustrates the new word. One possible layout has five elements: 1. a new vocabulary word; 2. a simple picture or clip art you can describe with the new word; 3. a description of the picture; 4. your own Korean definition of the new word; 5. an antonym or a synonym.\n\n"
             "The book’s model card is for 비싸다: the picture shows something expensive (the book suggests an Apple computer or a BMW), the description is 옷이 너무 비싸요 plus the price of the clothes ($700), the definition is 가격이 높아요, and the antonym is 싸다. Choose one of the words of the chapter and make a card with all five elements; for other words use a larger index card (at least 4 by 6 inches).",
             tables=[table(["Element", "What it is", "In the book’s model"], [[a, b, c] for a, b, c in _WORDMAP], say=[2])]),
        card("Means of transportation and where you board",
             "The book’s Topic Presentation A has this table of 교통 수단 (means of transportation) and 타는 곳 (the place where you board). The book writes 항(구); it is written 항구 here. 기차/열차 are two words for a train.",
             tables=[table(["Means of transportation", "Where you board"], _TRANS, say=[0, 1])]),
        card("Activity 3: the bingo definitions",
             "The book’s Bingo game gives twelve definitions in Korean and asks you to write the word that fits each (then you play bingo with a partner, explaining words in Korean without saying them). The definitions are the book’s. The answers are mine; 형님 is the honorific of 형 and is not glossed in the book, and 사촌 here is the son of a mother’s sister.",
             tables=[table(["Definition", "Word", "Meaning"], [[d, w, _BINGO_EN[w]] for d, w in _BINGO], say=[0, 1])]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board) and the bingo card with its pair-work rules (each partner chooses nine words and calls definitions) are SMART Board or partner activities."),
    ],
    exercises=uniq(
        [M(f"Which word fits this definition? {d}", w, [x for _, x in _BINGO if x != w][:3], f"{d} = {w} ({_BINGO_EN[w]}).") for d, w in _BINGO]
        + [M(f"What does {d} describe?", _BINGO_EN[w], [_BINGO_EN[x] for _, x in _BINGO if x != w][:3], f"{d} → {w}.") for d, w in _BINGO]
        + [M("Where do you board a plane?", "공항", ["역", "정류장", "항구"], "비행기 → 공항."), M("Where do you board a train?", "역", ["공항", "정류장", "항구"], "기차/열차 → 역."), M("Where do you board a bus?", "정류장", ["공항", "역", "항구"], "버스 → 정류장."),
           M("Where do you board an express bus?", "터미널", ["정류장", "역", "공항"], "고속버스 → 터미널."), M("Where do you board a ship?", "항구", ["공항", "역", "정류장"], "배 → 항(구)."), M("Where do you board a subway?", "역", ["공항", "정류장", "터미널"], "지하철 → 역."),
           M("What is the antonym of 비싸다 in the book’s model card?", "싸다", ["높다", "가격", "옷"], "비싸다 ↔ 싸다."), M("What is the book’s Korean definition of 비싸다?", "가격이 높아요.", ["가격이 낮아요.", "옷이 작아요.", "비행기가 빨라요."], "가격이 높아요 = the price is high."),
           M("How many elements does the word map card have?", "Five", ["Two", "Three", "Eight"], "Word, picture, description, definition, antonym/synonym."), M("What does the second element of the card hold?", "A simple picture or clip art", ["An antonym", "A description", "A definition"], "2 = picture."),
           M("What does 기차/열차 mean?", "a train", ["a bus", "a plane", "a ship"], "기차 and 열차 both mean a train."),
           F("비행기는 ___에서 탑니다. (airport)", "공항", ["역", "정류장"], "공항 = airport."), F("버스는 ___에서 탑니다. (bus stop)", "정류장", ["공항", "항구"], "정류장 = a bus stop."), F("배는 ___에서 탑니다. (harbor)", "항구", ["역", "공항"], "항구 = harbor."),
           read_q("공항"), read_q("정류장"), read_q("터미널"), read_q("고속버스"), read_q("신호등")]
    ),
)

# ================================================================== Topic A
_A_DLG = [
    ("존스 일병", "김 이병, 우리 로스앤젤레스에 어떻게 갈까?", "PV2 Kim, how shall we go to Los Angeles?"), ("김 이병", "몬트레이 공항에서 비행기 타고 갈까?", "Shall we take a plane from the Monterey airport?"),
    ("존스 일병", "비행기로 가면 빠르고 편해. 하지만 너무 비싸.", "Going by plane is fast and comfortable. But it’s too expensive."), ("김 이병", "그럼 기차 타고 갈까? 기차가 비행기보다 더 싸.", "Then shall we take a train? A train is cheaper than a plane."),
    ("존스 일병", "그럼, 기차는 어디에서 타?", "Then where do we take the train?"), ("김 이병", "여기서 가장 가까운 역은 살리나스 역이야.", "The station nearest from here is Salinas Station."),
    ("존스 일병", "그래? 그럼 살리나스까지 운전하고 가야 해?", "Is that so? Then do we have to drive to Salinas?"), ("김 이병", "그렇지. 아니면 공항 버스를 타고 가야 해.", "Right. Or we have to go by airport bus."),
    ("존스 일병", "버스는 느리고 불편해.", "The bus is slow and inconvenient."), ("김 이병", "그럼 어떻게 할까?", "Then what shall we do?"), ("존스 일병", "내 차로 가자. 비용도 적게 들 거야.", "Let’s go in my car. The cost will be low too."),
]
_A_PAIRS = [
    ("가장", "the most; the -est"), ("고속버스", "an express bus; “high-speed bus”"), ("공항", "an airport"), ("기차", "a train"), ("열차", "a train"), ("너무", "too; overly"), ("느리다", "to be slow"), ("더", "more"), ("들다", "to cost"), ("렌터카", "a rental car"),
    ("배", "a ship; a boat"), ("버스", "a bus"), ("보다", "more … / -er … than (as ~보다 (더))"), ("불편하다", "to be uncomfortable; to be inconvenient"), ("비싸다", "to be expensive; “to be not cheap”"), ("비용", "expense; cost; expenditure"), ("빌리다", "to borrow; to rent"),
    ("빠르다", "to be fast; to be quick"), ("싸다", "to be cheap"), ("역", "a train station; a subway station"), ("적게", "few; little"), ("적다", "to be few; to be little"), ("정류장", "a (bus/taxi) stop"), ("지하철", "a subway; “underground steel”"),
    ("터미널", "a terminal"), ("항구", "a harbor; a port"),
]
L2 = lesson(
    "Ch 10 · Topic A: Let’s take my car",
    "내 차로 가자 · 비행기 · 기차 · 버스 · 비용 · 가장 가까운 역",
    requires=[],
    cards=[
        card("Dialog: Let’s take my car",
             "PFC Jones and PV2 Kim are discussing the means of transportation they will use when they go to Los Angeles during the Christmas holidays. (The English is mine.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary, which lists them under Transportation, Time, Loan Words and Other Words). The book writes 기차/열차, 항(구) and ~보다 (더) as groups; they are split here (보다 is written without ~).",
             tables=[ktable(_A_PAIRS)]),
        card("Activities left out",
             "The vocabulary slide show, the SMART Board activities, the instruction to study the dialog and to read parts aloud with a partner, and Follow-up 1 (listening to four dialogs about a trip, to write in English the means of transportation and the reason for each choice) are audio, SMART Board or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS if k not in ("열차", "보다", "더")])
        + _tr(_strip(_A_DLG))
        + [M("How does PV2 Kim first suggest going to Los Angeles?", "By plane from the Monterey airport", ["By train", "By bus", "In a car"], "몬트레이 공항에서 비행기 타고 갈까?"), M("What is wrong with the plane, according to PFC Jones?", "It is too expensive", ["It is slow", "It is uncomfortable", "It is too far"], "하지만 너무 비싸."),
           M("What is cheaper than a plane?", "A train", ["A bus", "A car", "A ship"], "기차가 비행기보다 더 싸."), M("Which station is nearest to them?", "Salinas Station", ["Monterey Station", "Los Angeles Station", "San Jose Station"], "살리나스 역."), M("How could they get to Salinas?", "Drive or take the airport bus", ["Walk", "Take a ship", "Fly"], "운전하고 가야 해. 아니면 공항 버스를 타고 가야 해."),
           M("What does PFC Jones say about the bus?", "It is slow and inconvenient", ["It is fast and cheap", "It is comfortable", "It is expensive"], "버스는 느리고 불편해."), M("How do they decide to go?", "In PFC Jones’s car", ["By plane", "By train", "By bus"], "내 차로 가자."), M("Why does PFC Jones like his car?", "The cost will be low", ["It is fast", "It is new", "It is big"], "비용도 적게 들 거야."),
           F("기차가 비행기___ 더 싸. (than)", "보다", ["도", "만"], "~보다 = than."), F("여기서 ___ 가까운 역은 살리나스 역이야. (nearest)", "가장", ["너무", "아직"], "가장 = the most."), F("비행기로 가면 빠르고 편해. 하지만 ___ 비싸. (too)", "너무", ["가장", "다시"], "너무 = too."), F("버스는 ___ 불편해. (slow)", "느리고", ["빠르고", "싸고"], "느리다 = to be slow."),
           F("비용도 ___ 들 거야. (little)", "적게", ["많이", "너무"], "적게 = little."), F("내 차___ 가자. (by)", "로", ["를", "도"], "차로 = by car."),
           read_q("비행기"), read_q("기차"), read_q("불편하다"), read_q("가장"), read_q("빌리다")]
    ),
)

# ================================================================== Activities A
_IT1 = [("서부 관광 사박오일", "A western U.S. tour, four nights and five days (the book writes 4박 5일)"), ("(라스베가스, 그랜드 캐년, 유니버설 스튜디오, 디즈니랜드 관광, 기차 여행)", "(Las Vegas, the Grand Canyon, Universal Studios, a Disneyland tour, a train trip)"),
        ("기간: 사박오일", "Period: four nights and five days"), ("매주 수 출발", "Departs every Wednesday"), ("비용: 육백오십 달러", "Cost: $650 (the book writes $650)"),
        ("일일 산호세 공항에서 비행기로 라스베가스 도착.", "Day 1: Arrive at Las Vegas by plane from the San Jose airport."), ("이일 라스베가스 관광. 버스를 타고 그랜드 캐년으로 출발.", "Day 2: Las Vegas tour. Leave for the Grand Canyon by bus."),
        ("삼일 그랜드 캐년 관광. 관광 후 버스를 타고 로스앤젤레스로 출발.", "Day 3: Grand Canyon tour. After the tour, leave for Los Angeles by bus."), ("사일 유니버설 스튜디오, 디즈니랜드 관광.", "Day 4: Universal Studios and Disneyland tour."),
        ("오일 기차를 타고 산호세 기차역 도착.", "Day 5: Arrive at the San Jose train station by train.")]
_IT2 = [("울릉도 관광 사박오일", "An Ulleungdo tour, four nights and five days (the book writes 4박 5일)"), ("매주 월 금 출발", "Departs every Monday and Friday"), ("비용 십삼만 원", "Cost 130,000 won (the book writes 13만원)"),
        ("일일 포항항에서 배로 출발. 울릉도 항구 도착.", "Day 1: Leave Pohang Port by ship. Arrive at the Ulleungdo harbor."), ("이일 버스를 타고 울릉도 관광.", "Day 2: Tour Ulleungdo by bus."), ("삼일 울릉도 항구 출발. 포항항 도착.", "Day 3: Leave the Ulleungdo harbor. Arrive at Pohang Port.")]
_TRAIN = [["KTX 119", "Seoul", "Busan", "05:30", "08:27", "51,200", "weekends"], ["무궁화 121", "Seoul", "Busan", "06:15", "11:54", "26,500", "Mon, Wed, Fri"], ["무궁화 123", "Seoul", "Busan", "07:20", "12:57", "27,700", "weekends"], ["새마을 1003", "Seoul", "Busan", "13:18", "18:16", "39,300", "Mon, Wed, Fri"]]
_TT_AIR = [["서울 (Seoul)", "대구 (Daegu)", "07:05", "08:00", "68,400"], ["청주 (Cheongju)", "제주 (Jeju)", "14:45", "15:45", "70,680"], ["서울 (Seoul)", "광주 (Gwangju)", "19:45", "20:35", "62,900"], ["서울 (Seoul)", "부산 (Busan)", "06:20", "07:15", "47,900"]]
_TT_BUS = [["광주 (Gwangju)", "완도 (Wando)", "11:30", "15:40", "18,100"], ["서울 (Seoul)", "대전 (Daejeon)", "06:40", "08:40", "19,500"], ["부산 (Busan)", "여수 (Yeosu)", "10:30", "13:40", "12,700"], ["울산 (Ulsan)", "전주 (Jeonju)", "08:45", "13:15", "16,800"]]
_TT_TRAIN = [["대구 (Daegu)", "부산 (Busan)", "09:54", "11:50", "7,500"], ["서울 (Seoul)", "대전 (Daejeon)", "09:50", "11:10", "20,500"], ["대전 (Daejeon)", "목포 (Mokpo)", "10:12", "12:27", "24,300"], ["서울 (Seoul)", "광주 (Gwangju)", "06:05", "10:38", "21,400"]]
_TT_SHIP = [["완도 (Wando)", "제주 (Jeju)", "16:30", "19:20", "19,800"], ["부산 (Busan)", "제주 (Jeju)", "12:50", "23:58", "38,400"], ["목포 (Mokpo)", "제주 (Jeju)", "14:30", "19:20", "30,700"], ["여수 (Yeosu)", "제주 (Jeju)", "14:50", "22:50", "28,900"]]
_MODEL4 = [("기차로 서울에서 부산까지 갑니다.", "I go from Seoul to Busan by train."), ("기차를 타고 서울에서 부산까지 갑니다.", "I take a train and go from Seoul to Busan."), ("아홉 시에 기차로 서울을 출발, 열두 시에 부산에 도착합니다.", "I leave Seoul by train at nine and arrive in Busan at twelve."),
           ("비행기는 배보다 더 편합니다.", "A plane is more comfortable than a ship."), ("배를 타면 비행기보다 더 쌉니다.", "If you take a ship, it is cheaper than a plane.")]
_ROUTE1 = [("여섯 시 오 분에 기차로 서울을 출발해서 열 시 삼십팔 분에 광주에 도착합니다.", "I leave Seoul by train at 6:05 and arrive in Gwangju at 10:38."), ("열한 시 삼십 분에 고속버스로 광주를 출발해서 세 시 사십 분에 완도에 도착합니다.", "I leave Gwangju by express bus at 11:30 and arrive in Wando at 3:40."),
           ("네 시 삼십 분에 배로 완도를 출발해서 일곱 시 이십 분에 제주도에 도착합니다.", "I leave Wando by ship at 4:30 and arrive on Jeju Island at 7:20.")]
_ROUTE2 = [("여섯 시 이십 분에 비행기로 서울을 출발해서 일곱 시 십오 분에 부산에 도착합니다.", "I leave Seoul by plane at 6:20 and arrive in Busan at 7:15."), ("열 시 삼십 분에 고속버스로 부산을 출발해서 한 시 사십 분에 여수에 도착합니다.", "I leave Busan by express bus at 10:30 and arrive in Yeosu at 1:40."),
           ("두 시 오십 분에 배로 여수를 출발해서 열 시 오십 분에 제주도에 도착합니다.", "I leave Yeosu by ship at 2:50 and arrive on Jeju Island at 10:50.")]
L3 = lesson(
    "Ch 10 · Activities A: travel itineraries and timetables",
    "서부 관광 · 울릉도 관광 · 기차로 갑니다 · 배를 타고 출발 · 제주도에 도착합니다",
    requires=[],
    cards=[
        card("Activity 2: two itineraries from a travel agency",
             "The book gives two itineraries and asks you to write the means of transportation for each leg, in English. The Korean is the book’s; the book writes 4박 5일, $650, 13만원 and the day numbers 1일–5일, which are spelled out here (일일 = day 1, 이일 = day 2 and so on). The English is mine. Itinerary 2 says four nights and five days but lists only three days; that is how the book has it.",
             examples=passage(_IT1) + passage(_IT2)),
        card("Activity 2: the legs and the means of transportation (mine)",
             "My answers to the book’s two tables.",
             tables=[table(["Itinerary", "Leg", "Means of transportation"], [["1", "San Jose → Las Vegas", "An airplane (비행기)"], ["1", "Las Vegas → Grand Canyon", "A bus (버스)"], ["1", "Grand Canyon → Los Angeles", "A bus (버스)"], ["1", "Los Angeles → San Jose", "A train (기차)"],
                                                                                   ["2", "Pohang → Ulleungdo", "A ship (배)"], ["2", "Ulleungdo sightseeing", "A bus (버스)"], ["2", "Ulleungdo → Pohang", "A ship (배)"]])]),
        card("Activity 3: the Seoul–Busan train schedule",
             "The book’s train table, for the three narrations that you listen to (the audio is left out). 요금 means “fee” in the book’s gloss. The names are the book’s (the book writes 무궁화121 and 새마을1003 without a space); the English is mine.",
             tables=[table(["Train", "From", "To", "Departs", "Arrives", "Fare (won)", "Runs on"], _TRAIN)]),
        card("Activity 4: Jeju Island by public transportation",
             "You are stationed in Seoul and are going sightseeing on Jeju Island with your friend next weekend. You must leave Seoul on Saturday morning and arrive on Jeju the same day, using three different means of public transportation; you plan the route on a map, negotiate with a partner, and present it on a flip chart. The book’s four timetables are below (the English names of the cities are mine; 출발지 = departure place, 도착지 = arrival place, 출항 = leaving port, 입항 = entering port).",
             tables=[table(["Flights", "To", "Departs", "Arrives", "Fare (won)"], _TT_AIR, title="비행기 운항 시간표 (airplane schedule)"), table(["Express buses", "To", "Departs", "Arrives", "Fare (won)"], _TT_BUS, title="고속버스 운행 시간표 (express bus schedule)"),
                     table(["Trains", "To", "Departs", "Arrives", "Fare (won)"], _TT_TRAIN, title="기차 운행 시간표 (train schedule)"), table(["Ships", "To", "Leaves port", "Enters port", "Fare (won)"], _TT_SHIP, title="배 운항 시간표 (ship schedule)")]),
        card("Activity 4: the book’s model sentences",
             "The book’s model sentences for the presentation. The English is mine; the book writes 9시 and 12시, which are spelled out here.",
             examples=passage(_MODEL4)),
        card("Activity 4: two routes that work (mine)",
             "The book leaves the itinerary to you. Two of the possible routes that use three different means of transportation and reach Jeju the same day are shown here; the times are from the timetables above. Route 1: train Seoul → Gwangju (6:05–10:38, 21,400 won), express bus Gwangju → Wando (11:30–15:40, 18,100 won), ship Wando → Jeju (16:30–19:20, 19,800 won), 59,300 won in all. Route 2: plane Seoul → Busan (6:20–7:15, 47,900 won), express bus Busan → Yeosu (10:30–13:40, 12,700 won), ship Yeosu → Jeju (14:50–22:50, 28,900 won), 89,500 won in all.",
             examples=passage(_ROUTE1) + passage(_ROUTE2)),
        card("Activities left out",
             "Activity 1 (a SMART Board reading and listening activity) and the three narrations of Activity 3 (people in Seoul planning a train trip to Busan, to choose the right train for each) are audio or SMART Board activities. The map, the flip chart and the pair negotiation of Activity 4 are partner and class activities."),
    ],
    exercises=uniq(
        _tr(_IT1[3:4] + _IT1[5:] + _IT2[1:2] + _IT2[3:])
        + _tr(_MODEL4)
        + _tr(_ROUTE1 + _ROUTE2)
        + [M("How does the first itinerary start?", "By plane from the San Jose airport to Las Vegas", ["By train to Las Vegas", "By bus to Las Vegas", "By ship to Las Vegas"], "산호세 공항에서 비행기로 라스베가스 도착."), M("How do the travelers go from Las Vegas to the Grand Canyon?", "By bus", ["By plane", "By train", "By ship"], "버스를 타고 그랜드 캐년으로 출발."),
           M("How does the first itinerary end?", "By train to the San Jose train station", ["By plane", "By bus", "By ship"], "기차를 타고 산호세 기차역 도착."), M("How do the travelers go from Pohang to Ulleungdo?", "By ship", ["By plane", "By train", "By bus"], "포항항에서 배로 출발."),
           M("How do the travelers tour Ulleungdo?", "By bus", ["By ship", "By train", "On foot"], "버스를 타고 울릉도 관광."), M("When does the Ulleungdo tour leave?", "Every Monday and Friday", ["Every Wednesday", "Every Saturday", "Every day"], "매주 월 금 출발."),
           M("When does the western U.S. tour leave?", "Every Wednesday", ["Every Monday", "Every Friday", "Every day"], "매주 수 출발."), M("Which fare is the cheapest Seoul–Busan train in the schedule?", "26,500 won (무궁화 121)", ["51,200 won (KTX 119)", "27,700 won (무궁화 123)", "39,300 won (새마을 1003)"], "무궁화 121 costs 26,500 won."),
           M("Which Seoul–Busan train is the fastest?", "KTX 119 (about three hours)", ["무궁화 121", "무궁화 123", "새마을 1003"], "05:30 → 08:27."), M("Which train runs only on Monday, Wednesday and Friday and costs 39,300 won?", "새마을 1003", ["KTX 119", "무궁화 121", "무궁화 123"], "새마을 1003: Mon, Wed, Fri, 39,300 won."),
           M("Which train, bus and ship reach Jeju the same day from Seoul (route 1)?", "Train to Gwangju, express bus to Wando, ship to Jeju", ["Plane to Daegu, train to Busan, ship to Jeju", "Express bus to Daejeon, train to Mokpo, ship to Jeju", "Plane to Gwangju, bus to Wando, ship to Jeju"], "06:05 → 10:38; 11:30 → 15:40; 16:30 → 19:20."),
           M("Why can’t you take the evening Seoul–Gwangju flight in route 1?", "It leaves at 19:45, after the ship has left Wando", ["It is too expensive", "It goes to Daegu", "It is a bus"], "The ship from Wando leaves at 16:30."),
           M("What does 비행기는 배보다 더 편합니다 mean?", "A plane is more comfortable than a ship.", ["A ship is more comfortable than a plane.", "A plane is cheaper than a ship.", "A plane is slower than a ship."], "~보다 더 = more than."),
           F("기차___ 서울에서 부산까지 갑니다. (by)", "로", ["를", "도"], "기차로 = by train."), F("기차___ 타고 서울에서 부산까지 갑니다. (object marker)", "를", ["로", "가"], "기차를 타고."), F("배를 ___ 비행기보다 더 쌉니다. (If you take)", "타면", ["타서", "타고"], "배를 타면 = if you take a ship."),
           read_q("울릉도"), read_q("제주도"), read_q("출발"), read_q("도착합니다"), read_q("고속버스로")]
    ),
)

# ================================================================== Grammar A: comparison
_CMP_EX = [("한국말이 쉬워요.", "Korean is easy."), ("한국말이 더 쉬워요.", "Korean is easier."), ("한국말이 일본말보다 더 쉬워요.", "Korean is easier than Japanese."), ("한국말이 일본말보다 (더) 쉬워요.", "Korean is easier than Japanese. (더 can be left out when 보다 is there.)"),
           ("일본말보다 한국말이 더 쉬워요.", "Korean is easier than Japanese. (the nouns swapped; the meaning is the same)"), ("미국이 멕시코보다 (더) 커요.", "The U.S. is larger than Mexico."), ("이 옷이 더 아름다워요.", "This dress is more beautiful. (mine; the book writes 더 아름다워요 as an example)"),
           ("비행기가 기차보다 더 빨라요.", "A plane is faster than a train. (mine)")]
_CMP_FU2 = [("메인 주", "알래스카 주", "춥다", False, "Alaska is colder than Maine."), ("백화점", "시장", "싸다", False, "A market is cheaper than a department store."), ("카멜 강", "미시시피 강", "길다", False, "The Mississippi River is longer than the Carmel River."),
            ("텍사스", "캘리포니아", "덥다", True, "Texas is hotter than California."), ("생선", "고기", "맛있다", True, "Fish is tastier than meat. (a matter of taste)"), ("몬트레이 공항", "샌프란시스코 공항", "작다", True, "The Monterey airport is smaller than the San Francisco airport."),
            ("스웨터", "티셔츠", "따뜻하다", True, "A sweater is warmer than a T-shirt."), ("비행기", "기차", "빠르다", True, "A plane is faster than a train."), ("컴퓨터 게임", "집안 일", "재미있다", True, "A computer game is more fun than housework.")]


def _cmp(n1, n2, v, first, swap=False):
    a, b = (n1, n2) if first else (n2, n1)
    if swap:
        a, b = b, a
    return f"{a}{_ig(a)} {b}보다 더 {adj_inf(v)}."


_CMP_ADJ = [("쉽다", "to be easy"), ("크다", "to be big"), ("작다", "to be small"), ("춥다", "to be cold"), ("덥다", "to be hot"), ("싸다", "to be cheap"), ("비싸다", "to be expensive"), ("길다", "to be long"), ("빠르다", "to be fast"), ("느리다", "to be slow"), ("편하다", "to be comfortable"), ("불편하다", "to be uncomfortable"),
            ("맛있다", "to be delicious"), ("재미있다", "to be fun"), ("따뜻하다", "to be warm"), ("복잡하다", "to be complicated"), ("귀엽다", "to be cute"), ("좋다", "to be good")]
L4 = lesson(
    "Ch 10 · Grammar A: comparing with ~보다 (더)",
    "일본말보다 더 쉬워요 · 더 · 보다 · 가장 · 비행기가 기차보다 더 빨라요",
    requires=[],
    cards=[
        card("Expressing comparison",
             "Look at 한국말이 쉬워요 (Korean is easy), 한국말이 더 쉬워요 (Korean is easier) and 한국말이 일본말보다 더 쉬워요 (Korean is easier than Japanese). 더 is the counterpart of the English -er or “more”, but it comes before the adjective or adverb (더 쉬워요, 더 아름다워요). 보다 is the counterpart of “than”, and it comes after the second noun being compared.\n\n"
             "Markers attached to nouns show the grammatical function of the nouns, so swapping the two nouns does not change the meaning: 한국말이 일본말보다 더 쉬워요 = 일본말보다 한국말이 더 쉬워요. As long as the noun with ~보다 is in the sentence, 더 can be left out.",
             examples=[D(a, b) for a, b in _CMP_EX]),
        card("Forms",
             "The informal polite forms below are mine (ㅂ and 르 stems change: 춥다 → 추워요, 빠르다 → 빨라요). The superlative 가장 (“the most; the -est”) is in the book’s Core Vocabulary, with the example 미국에서 알래스카 주가 가장 큽니다.",
             tables=[table(["Dictionary form", "Meaning", "Informal", "With 더"], [[v, m, adj_inf(v), "더 " + adj_inf(v)] for v, m in _CMP_ADJ], say=[0, 2, 3])],
             examples=[D("미국에서 알래스카 주가 가장 큽니다.", "In the U.S., Alaska is the biggest.")]),
        card("Follow-up 2: make comparison statements",
             "In the book partners take turns making a comparison aloud from two nouns and a stative verb; the book’s model is 알래스카 주가 메인 주보다 더 추워요 or 메인 주보다 알래스카 주가 더 추워요. The nouns and verbs are the book’s (it adds “market” for 시장). Which noun comes out ahead is a matter of fact or opinion; the sentences below are my sample key, and the other order of the nouns, with the opposite meaning, is also grammatical.",
             tables=[table(["Noun 1", "Noun 2", "Verb", "Sample sentence", "Meaning"], [[a, b, v, _cmp(a, b, v, f), e] for a, b, v, f, e in _CMP_FU2], say=[0, 1, 2, 3])]),
        card("Activities left out",
             "Follow-up 1 (listening to five short statements that compare two objects or persons, to circle the superior one and write the adjective used) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which says “{e.split(' (')[0].rstrip('.')}”?", _cmp(a, b, v, f), [_cmp(a, b, v, f, True), _cmp(a, b, v, f)[:-1] + "?", _cmp(a, b, v, f).replace("보다 더", "도 더")], f"~보다 comes after the noun that is compared against: {_cmp(a, b, v, f)}") for a, b, v, f, e in _CMP_FU2]
        + [M(f"What does {_cmp(a, b, v, f)} mean?", e.split(" (")[0], [x.split(" (")[0] for _, _, _, _, x in _CMP_FU2 if x != e][:3], f"{_cmp(a, b, v, f)} = {e}") for a, b, v, f, e in _CMP_FU2]
        + [M(f"What does {a} mean?", b, [x for _, x in _CMP_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _CMP_EX[:6]]
        + [M(f"What is the informal polite form of {v} ({m})?", adj_inf(v), [x for x in (stem(v) + "어요", stem(v) + "아요", formal(v)) if x != adj_inf(v)], f"{v} → {adj_inf(v)}.") for v, m in _CMP_ADJ if v in ("춥다", "덥다", "쉽다", "빠르다", "귀엽다", "크다", "느리다")]
        + [F("한국말이 일본말___ 더 쉬워요. (than)", "보다", ["도", "만"], "~보다 = than."), F("한국말이 일본말보다 ___ 쉬워요. (more)", "더", ["가장", "너무"], "더 = more."), F("미국이 멕시코보다 ___ 커요. (more; optional)", "더", ["가장", "너무"], "더 can also be left out."),
           F("미국에서 알래스카 주가 ___ 큽니다. (the most)", "가장", ["더", "너무"], "가장 = the most; the -est."), F("비행기가 기차보다 더 ___. (faster)", "빨라요", ["빠르요", "빨라"], "빠르다 → 빨라요 (르 stem)."), F("제주도가 서울보다 더 ___. (warmer)", "따뜻해요", ["따뜻해", "따뜻하요"], "따뜻하다 → 따뜻해요."),
           M("Where does 더 go in the sentence?", "Before the adjective or adverb", ["After the adjective", "After 보다", "At the end of the sentence"], "더 쉬워요."), M("Where does 보다 go?", "After the second noun being compared", ["Before the first noun", "After the verb", "Before 더"], "일본말보다."),
           M("What happens when the two nouns are swapped?", "The meaning stays the same", ["The meaning reverses", "The sentence is wrong", "더 must be dropped"], "Markers show the function of the nouns."), M("When can 더 be left out?", "When a noun with ~보다 is in the sentence", ["Always", "Never", "Only in questions"], "한국말이 일본말보다 (더) 쉬워요."),
           M("Which means “the most”?", "가장", ["더", "너무", "아직"], "가장 = the most."), M("Which is the correct form of “cheap” in informal polite?", "싸요", ["쌉니다요", "싸어요", "싼요"], "싸다 + 아요 → 싸요."),
           read_q("일본말보다 더 쉬워요"), read_q("더 빨라요"), read_q("가장 큽니다"), read_q("더 따뜻해요"), read_q("더 비싸요")]
    ),
)

# ================================================================== Topic B
_B_DLG = [
    ("존스 일병", "백 일병, 지금 어디야?", "PFC Baek, where are you now?"), ("백 일병", "응. 엘에이 우리 집이야. 오늘 오후에 도착했어. 넌 언제 올 거야?", "Yes. I’m at our house in L.A. I arrived this afternoon. When will you come?"),
    ("존스 일병", "난 김 이병하고 내일 아침에 출발할 거야. 오늘 차에 기름도 넣었어. 백 일병, 너희 집에 어떻게 가?", "I’m leaving tomorrow morning with PV2 Kim. I put gas in the car today too. PFC Baek, how do we get to your house?"),
    ("백 일병", "먼저 육십팔 번 길로 살리나스로 가. 첫 번째 사거리에서 우회전해. 계속 곧장 가면 백일 번 고속도로 입구가 나와.", "First take Road 68 to Salinas. Turn right at the first intersection. If you keep going straight, you will come to the entrance of Highway 101."),
    ("존스 일병", "거기까지는 잘 알아. 백일 번 고속도로로 얼마나 가야 해?", "I know that part well. How long do we have to go on Highway 101?"),
    ("백 일병", "한 네 시간 정도. 엘에이에 도착하면 버몬트 출구가 나와. 거기 공사 중이고 복잡하기 때문에 조심해야 해.", "About four hours. When you get to L.A., the Vermont exit comes up. It is under construction and congested there, so you have to be careful."),
    ("존스 일병", "응, 알았어. 그 다음에는?", "Okay, got it. What next?"), ("백 일병", "첫 번째 신호등에서 좌회전해. 조금 더 오면 오른쪽에 편의점이 있어. 거기서 우리 집이 아주 가까워.", "At the first traffic light turn left. A bit farther on there is a convenience store on your right. From there our house is very close."),
    ("존스 일병", "그래, 알았어. 혹시 길을 잃으면 전화할게.", "Okay. If I get lost I’ll call you."),
]
_B_PAIRS = [
    ("갈아타다", "to transfer (means of transportation); to get on (to a different road); “change and ride”"), ("값", "price"), ("가격", "price"), ("계속", "continuously"), ("고속도로", "highway; “high-speed road”"), ("공사 중", "under construction; “in the middle of construction”"), ("내다", "to pay (money)"),
    ("내일", "tomorrow; “coming day”"), ("떨어지다", "to be out of; to run out of; “fall/drop”"), ("복잡하다", "to be complicated; (road) to be congested"), ("세우다", "to stop; to park; to pull over"), ("신호등", "a traffic signal light; “signal lamp”"), ("오늘", "today"),
    ("길을 잃다", "to get lost; to be lost (in direction); “lose the way”"), ("입구", "an entrance; “entering mouth”"), ("조심", "care; caution"), ("조심하다", "to be careful; to be cautious"), ("지금", "now"), ("출구", "an exit; “exiting mouth”"), ("편의점", "a convenience store"), ("혹시", "by any chance"),
]
_DIRW = [("우회전하다", "to turn right"), ("좌회전하다", "to turn left"), ("사거리", "an intersection; “four-way street”"), ("곧장", "straight"), ("오른쪽", "the right side"), ("첫 번째", "the first"), ("길", "a road; a way"), ("기름을 넣다", "to put in gas; “to put in oil”")]
_PRON_H = [("하나", "하나", "one"), ("할머니", "할머니", "a grandmother"), ("한국 사람", "한국 사람", "a Korean person"), ("많이", "마니", "a lot; many"), ("넣어요", "너어요", "(I) put in"), ("않고", "안코", "not … and"), ("넣다", "너타", "to put in"), ("좋지", "조치", "isn’t it good"), ("입학", "이팍", "entering a school")]
_SINO_CH = [("출국", "departure from a country; “leaving a nation”"), ("출항", "departure from a port; “leaving a port”"), ("입국", "entry into a country; “entering a nation”"), ("입항", "entry into a port; “entering a port”"), ("출입", "coming in and out; entrance and exit; ingress and egress; departing and entering")]
_SINO_GU = [("비상구", "an emergency exit (the book gives 비상 = emergency)"), ("출구", "an exit"), ("입구", "an entrance")]
_KEYS = [("한 네 시간 정도.", "It takes about four hours."), ("혹시 길을 잃으면 전화할게.", "I will call you if I get lost."), ("거기 공사 중이고 복잡하기 때문에 조심해야 해.", "You should be careful because that area is under construction (and congested)."), ("백 일병, 너희 집에 어떻게 가?", "How do I get to your house?"),
         ("조금 더 오면 오른쪽에 편의점이 있어.", "Drive a bit farther and there will be a convenience store on your right."), ("첫 번째 사거리에서 우회전해.", "Make a right turn at the first intersection."), ("백일 번 고속도로로 얼마나 가야 해?", "How long should we go by freeway?")]
_DIR_SUM = [["From Monterey to Salinas", "Take Road 68 (육십팔 번 길)"], ["Turn right at …", "the first intersection (첫 번째 사거리)"], ["Go straight till …", "the entrance of Highway 101 (백일 번 고속도로 입구)"], ["Drive for …", "about four hours"], ["Exit at …", "Vermont (버몬트 출구)"],
            ["Turn left at …", "the first traffic light (첫 번째 신호등)"], ["Will see a …", "convenience store (편의점) on the right side (오른쪽)"]]
_DIR_PAT = [("A", "백 일병, 너희 집에 어떻게 가?", "PFC Baek, how do we get to your house?"), ("B", "먼저, 육십팔 번 길로 가야 해.", "First, you have to take Road 68."), ("A", "그 길로 어떻게 가?", "How do I go on that road?"), ("B", "거기서 첫 번째 사거리에서 우회전해.", "From there, turn right at the first intersection."),
            ("A", "그 다음에는?", "What next?"), ("B", "계속 곧장 가면 백일 번 고속도로 입구가 나와.", "If you keep going straight, you come to the entrance of Highway 101.")]
L5 = lesson(
    "Ch 10 · Topic B: PFC Baek, how do we get to your place?",
    "너희 집에 어떻게 가? · 우회전 · 좌회전 · 신호등 · 출구 · 입구 · 출입 (出入) · 구 (口)",
    requires=[],
    cards=[
        card("Dialog: asking for directions",
             "PFC Jones is calling PFC Baek, who has already arrived in L.A., to ask for directions to his home. (The English is mine. The book writes L.A., 68번, 101번 and Vermont; they are spelled out here, and the Latin spelling of Vermont is dropped.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary). The book writes 값/가격, 조심(하다) and (길을) 잃다 in the forms shown; 값 and 가격 are split, and 길을 잃다 has the 길을 added. -기 때문에/~때문에 has its own grammar lesson.",
             tables=[ktable(_B_PAIRS)]),
        card("Words for directions",
             "These words come from the dialog; the book does not gloss them in its Core Vocabulary, so the English is mine.",
             tables=[ktable(_DIRW)]),
        card("Pronunciation guide: ㅎ",
             "At the beginning of a word, ㅎ is pronounced like the English h, as in 하나, 할머니 and 한국 사람. ㅎ is often silent in the middle of a word or when it is followed by a vowel: 실례합니다 is said /실례암니다/, 안녕히 계세요 /안녕이 게세요/, 많이 /마니/ and 넣어요 /너어요/. When ㅎ is followed or preceded by ㄱ, ㄷ, ㅂ or ㅈ, the two consecutive consonants are pronounced as ㅋ, ㅌ, ㅍ or ㅊ, respectively: 않고 /안코/, 넣다 /너타/, 좋지 /조치/, 입학 /이팍/.",
             tables=[ptable(_PRON_H), table(["Korean", "Said (book)", "Meaning"], [["실례합니다", "[실례암니다]", "Excuse me"], ["안녕히 계세요", "[안녕이 게세요]", "Goodbye (to the person who stays)"]], say=[0])]),
        card("Sino-Korean in use: 출입 (出入)",
             "The first syllable 출 (出) basically means (coming/going) out or leaving (a place), as in 출국 and 출항. The second syllable 입 (入) basically means (coming/going) in or entering (a place), as in 입국 and 입항. So the literal meaning of 출입 is “(coming/going) out and in”; depending on the context it can be translated as coming in and out, entrance and exit, ingress and egress, or departing and entering.",
             tables=[ktable(_SINO_CH)]),
        card("Sino-Korean in use: 구 (口)",
             "This Chinese character depicts an opening; it means a mouth or an opening. The book asks you to guess the meaning of 비상구, 출구 and 입구 (비상 = emergency). My answers are below; 출구 and 입구 are the book’s, from the Core Vocabulary.",
             tables=[ktable(_SINO_GU)]),
        card("Follow-up 1: the key sentences and their translations",
             "The book asks you to listen to seven sentences and match each with its English translation (a–g). The seven English sentences are the book’s; the Korean sentences are the lines of the dialog that they translate (the matching is mine).",
             tables=[table(["Korean", "English (the book’s)"], [[k, e] for k, e in _KEYS], say=[0])]),
        card("The directions to PFC Baek’s home in L.A.",
             "In the book you listen to the dialog and fill in the gaps of a summary of the directions; the answers below are mine.",
             tables=[table(["Step", "Answer"], _DIR_SUM)]),
        card("The book’s dialog pattern for asking for and giving directions",
             "In the book one partner takes the role of PFC Baek and the other of PFC Jones and they ask for and give directions with the pattern A: 백 일병, 너희 집에 어떻게 가? B: 먼저, ___로 가/가야 해. A: 그 길로/거기서 어떻게 가? B: 거기서 ___. A: 그 다음에는? B: ___. The filled-in version below is mine.",
             examples=dlg(_DIR_PAT)),
        card("Activities left out",
             "The SMART Board activities, listening to the dialog to fill in the summary, the pair role-play, and Follow-up 2 (listening to two phone conversations in which Sunghyun asks Mijin for directions to her house, to write the directions in English) are audio, SMART Board or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS if k not in ("가격",)])
        + vocab_exercises([(k, _clean(e)) for k, e in _DIRW])
        + _tr(_strip(_B_DLG))
        + _tr(_KEYS)
        + [M(f"What does {a} mean?", b, [x for _, x in _SINO_CH + _SINO_GU if x != b][:3], f"{a}: {b}.") for a, b in _SINO_CH + _SINO_GU]
        + [M("What does the Sino-Korean syllable 출 (出) mean?", "out; leaving", ["in; entering", "a mouth", "a father"], "출국, 출항, 출발."), M("What does the Sino-Korean syllable 입 (入) mean?", "in; entering", ["out; leaving", "a mouth", "a mother"], "입국, 입항, 입학."),
           M("What does the Sino-Korean syllable 구 (口) mean?", "a mouth; an opening", ["out; leaving", "in; entering", "a machine"], "입구, 출구, 비상구."), M("Which word means “an entrance”?", "입구", ["출구", "비상구", "출국"], "입 = enter; 구 = opening."),
           M("Which word means “an exit”?", "출구", ["입구", "입국", "입항"], "출 = out; 구 = opening."), M("Which word means “departure from a country”?", "출국", ["입국", "출항", "입항"], "출 + 국 (nation)."),
           M("Where does PFC Baek say to turn right?", "At the first intersection", ["At the first traffic light", "At the convenience store", "At the Vermont exit"], "첫 번째 사거리에서 우회전해."), M("Where does PFC Baek say to turn left?", "At the first traffic light", ["At the first intersection", "At the entrance of Highway 101", "At the airport"], "첫 번째 신호등에서 좌회전해."),
           M("How long is the drive on Highway 101?", "About four hours", ["About an hour", "About ten hours", "About two days"], "한 네 시간 정도."), M("Why should they be careful near the Vermont exit?", "It is under construction and congested", ["It is dark", "There is snow", "It is a toll road"], "공사 중이고 복잡하기 때문에 조심해야 해."),
           M("What will they see on the right near PFC Baek’s house?", "A convenience store", ["A gas station", "A school", "A park"], "오른쪽에 편의점이 있어."), M("What does PFC Jones say he will do if he gets lost?", "Call", ["Stop at a gas station", "Turn around", "Take a train"], "길을 잃으면 전화할게."),
           M("When will PFC Jones leave?", "Tomorrow morning", ["This afternoon", "Tonight", "Next week"], "내일 아침에 출발할 거야."), M("What did PFC Jones do to the car today?", "Put gas in it", ["Washed it", "Sold it", "Rented it"], "오늘 차에 기름도 넣었어."),
           F("첫 번째 사거리에서 ___해. (turn right)", "우회전", ["좌회전", "출발"], "우회전 = turn right."), F("첫 번째 신호등에서 ___해. (turn left)", "좌회전", ["우회전", "도착"], "좌회전 = turn left."), F("계속 ___ 가면 백일 번 고속도로 입구가 나와. (straight)", "곧장", ["너무", "아직"], "곧장 = straight."),
           F("거기 공사 중이고 복잡하기 때문에 ___해야 해. (be careful)", "조심", ["출발", "운전"], "조심하다 = to be careful."), F("혹시 길을 ___ 전화할게. (If I get lost)", "잃으면", ["잃어서", "잃고"], "잃다 → 잃으면."), F("백일 번 고속도로 ___로 나가세요. (exit)", "출구", ["입구", "정류장"], "출구 = an exit."),
           read_q("우회전"), read_q("좌회전"), read_q("고속도로"), read_q("편의점"), read_q("출입")]
    ),
)

# ================================================================== Grammar B: 때문에
_BC_EX = [("비 때문에 길이 막혀요.", "Because of rain, the road is congested."), ("비가 오기 때문에 축구를 못 해요.", "Because it is raining, we cannot play soccer."), ("숙제 때문에 못 놀아요.", "I can’t play because of homework. (mine)"), ("너 때문에 행복해요.", "I’m happy because of you. (mine)"),
          ("날씨 때문에 비행기가 늦게 도착했어요.", "Because of the weather, the plane arrived late. (mine)"), ("숙제를 하기 때문에 바빠요.", "I am busy because I am doing homework. (mine)"), ("많이 먹기 때문에 살이 쪄요.", "I gain weight because I eat a lot. (mine)")]
_BC_V = [("오다", "to come (rain, snow)"), ("피곤하다", "to be tired"), ("바쁘다", "to be busy"), ("춥다", "to be cold"), ("덥다", "to be hot"), ("어렵다", "to be difficult"), ("복잡하다", "to be congested"), ("비싸다", "to be expensive"), ("먹다", "to eat"), ("가다", "to go"), ("공부하다", "to study"), ("심심하다", "to be bored")]
_BC_FU3 = [("피곤합니다.", "피곤하기 때문에", "집에서 쉽니다.", "Because I am tired, I rest at home."), ("배가 고픕니다.", "배가 고프기 때문에", "밥을 먹습니다.", "Because I am hungry, I eat a meal."), ("날씨가 쌀쌀합니다.", "날씨가 쌀쌀하기 때문에", "코트를 입습니다.", "Because the weather is chilly, I wear a coat."),
           ("머리가 깁니다.", "머리가 길기 때문에", "이발합니다.", "Because my hair is long, I get a haircut."), ("숙제가 어렵습니다.", "숙제가 어렵기 때문에", "친구하고 같이 합니다.", "Because the homework is difficult, I do it with a friend."),
           ("매운 음식을 못 먹습니다.", "매운 음식을 못 먹기 때문에", "불고기를 시킵니다.", "Because I can’t eat spicy food, I order bulgogi."), ("심심합니다.", "심심하기 때문에", "한국 친구에게 전화합니다.", "Because I am bored, I call a Korean friend.")]
_GAS_US = [("미국은 기름값이 쌉니다.", "In the U.S. gas is cheap."), ("일 갤런에 사 불 정도입니다.", "It is about four dollars a gallon."), ("미국 주유소는 보통 셀프 서비스입니다.", "U.S. gas stations are usually self-service."), ("손님이 직접 기름을 넣습니다.", "The customer puts in the gas himself or herself."),
           ("미국 주유소에는 보통 편의점이 있습니다.", "U.S. gas stations usually have a convenience store."), ("거기에서 물이나 커피 등 음료수를 살 수 있습니다.", "You can buy drinks such as water or coffee there."), ("어떤 주유소에는 자동 세차 서비스도 있습니다.", "Some gas stations have an automatic car wash service too.")]
_GAS_KR = [("한국 주유소에서는 리터를 씁니다.", "Korean gas stations use liters."), ("일 리터는 영점 이이 갤런입니다.", "One liter is 0.22 gallons."), ("기름값이 일 리터에 이천 원 정도입니다.", "Gas is about 2,000 won per liter."), ("기름값이 비쌉니다.", "Gas is expensive."),
           ("한국은 보통 주유소 직원이 기름을 넣어 줍니다.", "In Korea a gas station employee usually puts in the gas for you."), ("또 직원이 자동차 유리도 닦아 줍니다.", "The employee also wipes the car windows."), ("엔진 오일도 체크해 줍니다.", "The employee also checks the engine oil."),
           ("크리넥스나 물 등을 서비스로 줍니다.", "They give tissues, water and so on as a service."), ("한국에서도 주유소에서 자동 세차를 할 수 있습니다.", "In Korea too you can use an automatic car wash at a gas station.")]
_GAS_SAMPLE = [("미국은 한국보다 기름값이 더 쌉니다.", "Gas is cheaper in the U.S. than in Korea."), ("한국은 직원이 기름을 넣어 주기 때문에 편합니다.", "In Korea it is convenient because an employee puts in the gas for you."), ("미국은 셀프 서비스이기 때문에 손님이 직접 기름을 넣습니다.", "In the U.S. the customer puts in the gas himself or herself because it is self-service.")]
L6 = lesson(
    "Ch 10 · Grammar B: “because” with (-기) 때문에",
    "비 때문에 · 비가 오기 때문에 · 피곤하기 때문에 · 숙제 때문에 · 주유소 이야기",
    requires=[],
    cards=[
        card("Expressing a reason using (-기) 때문에",
             "English has many words for a reason: because, because of, since, for, on account of, due to, now that. Korean has several conjunctive endings that express a reason; you learned -아서/어서 in Chapter 7. Unlike -아서/어서, which has multiple meanings, ~때문에 is used exclusively to mean “because of”. It is always preceded by a noun: 숙제 때문에 (because of the homework), 너 때문에 (because of you), 날씨 때문에 (because of the weather). To use a verb or a clause with 때문에 you must use -기 때문에, because -기 is a “gerund-maker” that turns a verb or a verbal phrase into a noun or noun phrase: 숙제를 하기 때문에 (because of doing homework), 많이 먹기 때문에 (because of eating a lot).",
             tables=[table(["Condition", "Rule", "Example"], [["After a noun", "add 때문에", "비 때문에"], ["After a verb", "add 기 때문에", "비가 오기 때문에"]], title="noun + 때문에; verb stem + 기 때문에")],
             examples=[D(a, b) for a, b in _BC_EX]),
        card("Forms",
             "The forms below are mine, made by the book’s rule; 기 is added directly to the stem, whatever the last letter is.",
             tables=[table(["Dictionary form", "Meaning", "-기 때문에"], [[v, m, stem(v) + "기 때문에"] for v, m in _BC_V], say=[0, 2])]),
        card("Follow-up 3: cause and effect",
             "In the book you connect seven sentences that have a cause-and-effect relation (the answers may vary), and then combine each pair with -기 때문에, as in 피곤하기 때문에 집에서 쉽니다. The sentences are the book’s; the matches below are mine. The book’s right-hand column also has 파마를 못 합니다, 중국 요리를 주문합니다 and 히터를 켭니다 (a perm, ordering Chinese food, turning on the heater): these fit as well (머리가 길기 때문에 파마를 못 합니다 is possible; 매운 음식을 못 먹기 때문에 중국 요리를 주문합니다; 날씨가 쌀쌀하기 때문에 히터를 켭니다), so the answers may vary. 시키다 and 주문하다 both mean “to order”, and 이발하다 means “to get a haircut” (mine).",
             tables=[table(["Cause", "With -기 때문에", "Effect", "Meaning"], [[c, f"{cc} {e}", e, en] for c, cc, e, en in _BC_FU3], say=[0, 1, 2])]),
        card("Follow-up 5: gas stations in America",
             "The book gives two passages about gas stations, in Korea and in America, and asks you to fill in a Venn diagram in Korean and write two or three sentences comparing them. The passages are the book’s; the book writes 1갤런(gallon), 4불, 1리터, 0.22갤런 and 2,000원, which are spelled out here. The English is mine. The book also glosses 세차 (to wash a car), 직원 (an employee), 자동 (automatic), 현금 (cash).",
             examples=passage(_GAS_US)),
        card("Follow-up 5: gas stations in Korea",
             "The second passage of the book.",
             examples=passage(_GAS_KR)),
        card("Follow-up 5: the Venn diagram (mine)",
             "My key to the book’s Venn diagram, in English.",
             tables=[table(["American gas stations only", "Both", "Korean gas stations only"], [["Gas is cheap (about $4 a gallon); usually self-service; a convenience store with drinks such as water and coffee", "Some stations have an automatic car wash", "Liters are used (1 liter = 0.22 gallons); gas is expensive (about 2,000 won a liter); an employee puts in the gas, wipes the windows, checks the engine oil and gives tissues or water as a service"]])]),
        card("Follow-up 5b: comparing the gas stations",
             "The book asks for two or three sentences with -(기) 때문에 and ~보다 더. My sample sentences:",
             examples=passage(_GAS_SAMPLE)),
        card("Activities left out",
             "Follow-up 4 (listening to three conversations about housing, to check apartment or house and write the reason) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the -기 때문에 form of {v} ({m})?", stem(v) + "기 때문에", [stem(v) + "아서", informal(v), formal(v)], f"{v} → {stem(v)}기 때문에.") for v, m in _BC_V]
        + [M(f"What does {a} mean?", b, [x for _, x in _BC_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _BC_EX]
        + [M(f"What does {cc} {e} mean?", en, [x for _, _, _, x in _BC_FU3 if x != en][:3], f"{cc} {e} = {en}") for c, cc, e, en in _BC_FU3]
        + [M(f"Which effect fits “{c}”?", e, [x for _, _, x, _ in _BC_FU3 if x != e][:3], f"{c} → {e}") for c, cc, e, en in _BC_FU3]
        + _tr(_GAS_US) + _tr(_GAS_KR[:5]) + _tr(_GAS_SAMPLE)
        + [M("Which gas stations are usually self-service?", "U.S. gas stations", ["Korean gas stations", "Both", "Neither"], "미국 주유소는 보통 셀프 서비스입니다."), M("Which unit do Korean gas stations use?", "Liters", ["Gallons", "Pounds", "Miles"], "한국 주유소에서는 리터를 씁니다."),
           M("In which country is gas cheaper, according to the passages?", "The U.S.", ["Korea", "They cost the same", "The passages do not say"], "미국은 기름값이 쌉니다. 한국은 기름값이 비쌉니다."), M("Who puts in the gas at a Korean gas station?", "An employee", ["The customer", "A robot", "A taxi driver"], "직원이 기름을 넣어 줍니다."),
           M("What can you buy at the convenience store of a U.S. gas station?", "Drinks such as water or coffee", ["Gasoline", "A car", "Train tickets"], "물이나 커피 등 음료수를 살 수 있습니다."), M("What do Korean gas station employees give as a service?", "Tissues and water", ["Cash", "A map", "A haircut"], "크리넥스나 물 등을 서비스로 줍니다."),
           F("비 ___ 길이 막혀요. (because of)", "때문에", ["기 때문에", "아서"], "After a noun: 때문에."), F("비가 오___ 때문에 축구를 못 해요. (because it rains)", "기", ["는", "을"], "After a verb: 기 때문에."), F("숙제 ___ 못 놀아요. (because of the homework)", "때문에", ["기 때문에", "해서"], "After a noun: 때문에."),
           F("너 ___ 행복해요. (because of you)", "때문에", ["기 때문에", "아서"], "After a noun: 때문에."), F("피곤하___ 때문에 집에서 쉽니다. (because I am tired)", "기", ["는", "은"], "피곤하다 → 피곤하기 때문에."), F("머리가 길___ 때문에 이발합니다. (because it is long)", "기", ["는", "은"], "길다 → 길기 때문에."),
           M("Which ending is used exclusively to mean “because of”?", "~때문에", ["-아서/어서", "-고", "-(으)면"], "~때문에 = because of."), M("What does -기 do to a verb?", "Turns it into a noun (a gerund)", ["Makes it past", "Makes it honorific", "Makes it a question"], "기 is a gerund-maker."),
           M("What comes before 때문에?", "A noun", ["A verb stem", "A particle only", "Nothing"], "숙제 때문에."), M("What comes before 기 때문에?", "A verb stem", ["A noun", "A number", "Nothing"], "비가 오기 때문에."),
           read_q("비 때문에"), read_q("비가 오기 때문에"), read_q("피곤하기 때문에"), read_q("어렵기 때문에"), read_q("못 먹기 때문에")]
    ),
)

# ================================================================== Activities B
_DIR21 = [
    ("안녕하십니까?", "Hello."), ("저희 부대로 오시는 길은 다음과 같습니다.", "The way to our unit is as follows."), ("대전 방향으로 경부고속도로를 타십시오.", "Take the Gyeongbu Expressway toward Daejeon."),
    ("두 시간쯤 후에 호남고속도로 광주 방향으로 갈아타십시오.", "After about two hours, transfer to the Honam Expressway toward Gwangju."), ("한 시간쯤 후에 정읍 출구가 보입니다.", "After about an hour you will see the Jeongeup exit."), ("그 출구로 나가십시오.", "Take that exit."),
    ("첫 번째 신호등에서 좌회전 하십시오.", "Turn left at the first traffic light."), ("조금만 더 오시면 오른쪽에 우체국이 나옵니다.", "If you come a little farther, a post office appears on the right."), ("그 다음 사거리에서 좌회전하시면 저희 이십일 사단이 있습니다.", "If you turn left at the next intersection, our 21st Division is there."),
    ("이십일 사단 작전과 중위 박용우", "Operations Section, 21st Division, First Lieutenant Park Yongwoo"),
]
_INC = [("기름값이 싼 주유소", "a gas station with cheap gas"), ("세차장이 있는 주유소", "a gas station with a car wash (세차장 = a car wash, the book’s gloss)"), ("편의점이 있는 주유소", "a gas station with a convenience store"), ("집에서 가까운 주유소", "a gas station close to home")]
_INC_MODEL = [("편의점이 (더) 크기 때문에 저는 세븐 일레븐 주유소가 쉘 주유소보다 좋아요.", "Because the convenience store is (bigger), I like the Seven Eleven gas station better than the Shell gas station."),
              ("가격이 (더) 싸기 때문에 저는 파일럿 주유소가 쉐브론 주유소보다 좋아요.", "Because the price is (cheaper), I like the Pilot gas station better than the Chevron gas station.")]
L7 = lesson(
    "Ch 10 · Activities B: directions to a unit and gas stations",
    "저희 부대로 오시는 길 · 경부고속도로 · 갈아타십시오 · 주유소 · 기름값이 싼 주유소",
    requires=[],
    cards=[
        card("Activity 2 (Reading): directions to the 21st Division",
             "Your unit in Korea plans a joint FTX (field training exercise) with the ROK Army at its camp next week. The directions you received are in Korean; the book asks you to translate the underlined ones into English (the underlining is not shown in my copy of the text). The Korean is the book’s; the book writes 2시간쯤, 1시간쯤 and 21사단, which are spelled out here. The English is mine.",
             examples=passage(_DIR21)),
        card("Activity 2: the directions summarized (mine)",
             "The book’s note box, “Directions to the 21st Division”, is blank bullets; my answers:",
             tables=[table(["Step", "Direction"], [["1", "Take the Gyeongbu Expressway toward Daejeon"], ["2", "After about two hours, transfer to the Honam Expressway toward Gwangju"], ["3", "After about an hour, you will see the Jeongeup exit"], ["4", "Take that exit"], ["5", "Turn left at the first traffic light"],
                                                      ["6", "A little farther, a post office appears on the right"], ["7", "Turn left at the next intersection: the 21st Division is there"]])]),
        card("Activity 4 (Reading, writing, speaking): which gas station do you like?",
             "The book lists four incentives that gas stations use to attract customers and asks you to rate each on a scale of 1 to 4 (1 = the most attractive), then to write about two gas stations you often use and say which you like better and why, using ~보다 and -기 때문에, and to interview three classmates. The incentives are the book’s (the English is mine); the two model sentences are the book’s (the English is mine; the brand names are written in Hangul as in the book).",
             tables=[table(["Incentive", "Meaning"], [list(r) for r in _INC], say=[0])],
             examples=passage(_INC_MODEL)),
        card("Activities left out",
             "Activity 1 (listening to three students describe a weekend trip, to fill in the destination, direction and drive time), Activity 3 (two advertisements of Korean gas stations that are shown as pictures, and a conversation about two gas stations, 강남 주유소 and 서울 주유소, to listen to) and the interviews of Activity 4 are audio, picture or partner activities."),
    ],
    exercises=uniq(
        _tr(_DIR21[1:9]) + _tr(_INC) + _tr(_INC_MODEL)
        + [M("Which expressway should you take toward Daejeon?", "The Gyeongbu Expressway", ["The Honam Expressway", "Highway 101", "Highway 1"], "대전 방향으로 경부고속도로를 타십시오."), M("When do you transfer to the Honam Expressway?", "After about two hours", ["After about an hour", "After ten minutes", "After five hours"], "두 시간쯤 후에."),
           M("Which exit do you see after about an hour?", "The Jeongeup exit", ["The Daejeon exit", "The Vermont exit", "The Gwangju exit"], "정읍 출구가 보입니다."), M("Where do you turn left first?", "At the first traffic light", ["At the post office", "At the exit", "At the gate"], "첫 번째 신호등에서 좌회전."),
           M("What is on the right a little farther on?", "A post office", ["A school", "A convenience store", "A hospital"], "오른쪽에 우체국이 나옵니다."), M("Who wrote the directions?", "First Lieutenant Park Yongwoo of the Operations Section", ["A general", "A civilian", "A sergeant"], "작전과 중위 박용우."),
           F("대전 방향으로 경부고속도로를 ___. (Take)", "타십시오", ["타세요", "탑니다"], "타다 → 타십시오 (formal request)."), F("호남고속도로로 ___십시오. (transfer)", "갈아타", ["갈아타서", "갈아탔"], "갈아타다 → 갈아타십시오."), F("조금만 더 오시면 오른쪽에 우체국이 ___. (appears)", "나옵니다", ["나옵니까", "나오세요"], "나오다 → 나옵니다."),
           F("편의점이 더 크기 ___ 저는 이 주유소가 좋아요. (because)", "때문에", ["아서", "고"], "크기 때문에 = because it is bigger."), F("가격이 싸기 때문에 이 주유소가 저 주유소___ 좋아요. (than)", "보다", ["도", "만"], "~보다 = than."),
           M("What does 세차장 mean?", "a car wash", ["a gas station", "a parking lot", "a bus stop"], "세차장 = a car wash."), M("Which incentive is “a gas station close to home”?", "집에서 가까운 주유소", ["기름값이 싼 주유소", "세차장이 있는 주유소", "편의점이 있는 주유소"], "집에서 가깝다 = close to home."),
           read_q("경부고속도로"), read_q("우체국"), read_q("갈아타십시오"), read_q("주유소"), read_q("세차장")]
    ),
)


# ================================================================== Topic C
_C_PASS = [
    ("저와 존스 일병은 백 일병 부모님 댁을 방문했어요.", "PFC Jones and I visited PFC Baek’s parents’ home."), ("먼저, 백 일병 아버지와 어머니께 인사를 드렸어요.", "First, we greeted PFC Baek’s father and mother."),
    ("백 일병의 아버지는 올해 환갑이시고 어머니는 내년에 환갑이 되십니다.", "PFC Baek’s father turns sixty this year, and his mother will turn sixty next year."), ("백 일병 집에는 작은아버지와 작은어머니, 이모와 이모부가 오셨어요.", "His uncle (father’s younger brother) and his wife, and his aunt (mother’s sister) and her husband came to PFC Baek’s house."),
    ("그리고 뉴욕에 사는 사촌들도 왔습니다.", "And the cousins who live in New York came too."), ("또, 백 일병의 형과 형수는 조카를 데리고 왔습니다.", "Also, PFC Baek’s older brother and sister-in-law brought their baby (nephew/niece)."),
    ("백 일병의 조카는 작년에 태어났습니다.", "PFC Baek’s nephew/niece was born last year."), ("아주 귀여웠습니다.", "He/she was very cute."), ("백 일병 가족과 친척들은 여러 가지 선물을 가지고 왔습니다.", "PFC Baek’s family and relatives brought various gifts."),
    ("환갑잔치에서 우리는 아주 즐거운 시간을 보냈습니다.", "At the 60th birthday party we had a very pleasant time."),
]
_C_PAIRS = [
    ("가지고 가다", "to take something somewhere; “to possess and go”"), ("가지고 오다", "to bring something; “to possess and come”"), ("고모", "father’s sister"), ("고모부", "husband of the father’s sister"), ("귀엽다", "to be cute"), ("내년", "next year; “coming year”"),
    ("데리고 가다", "to take someone somewhere"), ("모시고 가다", "to take someone somewhere (↑ honorific)"), ("데리고 오다", "to bring someone"), ("모시고 오다", "to bring someone (↑ honorific)"), ("되다", "to become; to be"), ("방문", "visit"), ("방문하다", "to visit"),
    ("사촌", "cousin; a child of the father’s siblings; “fourth relationship”"), ("여러", "various (여러 가지: various types of)"), ("올해", "this year"), ("금년", "this year"), ("외삼촌", "mother’s brother"), ("외할머니", "maternal grandmother"), ("외할아버지", "maternal grandfather"),
    ("이모", "mother’s sister"), ("이모부", "husband of the mother’s sister"), ("작년", "last year"), ("작은아버지", "father’s married younger brother; “little father”"), ("작은어머니", "wife of the father’s married younger brother; “little mother”"), ("조카", "a nephew; a niece; a sibling’s child"),
    ("큰아버지", "a father’s married older brother; “big father”"), ("큰어머니", "the wife of a father’s married older brother; “big mother”"), ("태어나다", "to be born"), ("형수", "a man’s older brother’s wife"),
]
_FAM = [("할아버지", "a grandfather (father’s side; the label of the book’s family tree)"), ("할머니", "a grandmother (father’s side; the label of the book’s family tree)"), ("외할아버지", "maternal grandfather"), ("외할머니", "maternal grandmother"), ("아버지", "a father"), ("어머니", "a mother"), ("나", "I; me"),
        ("큰아버지", "a father’s married older brother"), ("큰어머니", "the wife of a father’s married older brother"), ("작은아버지", "father’s married younger brother"), ("작은어머니", "wife of the father’s married younger brother"), ("고모", "father’s sister"), ("고모부", "husband of the father’s sister"),
        ("외삼촌", "mother’s brother"), ("이모", "mother’s sister"), ("이모부", "husband of the mother’s sister")]
_TAKE = [("데리고 가다/오다", "take/bring (a person or an animal)"), ("모시고 가다/오다", "take/bring (a person that you show respect to)"), ("가지고 가다/오다", "take/bring (an inanimate object)")]
_TAKE_EX = [("동생을 친구 생일파티에 데리고 갔어요.", "I took my younger sibling to my friend’s birthday party."), ("내일 학교에 부모님을 모시고 오세요.", "Please bring your parents to school tomorrow."), ("학교에 오자마자 숙제를 가지고 오세요.", "Please bring your homework as soon as you come to school.")]
_SINO_BM = [("부자", "father and son"), ("부녀", "father and daughter"), ("모자", "mother and son"), ("모녀", "mother and daughter"), ("부모", "father and mother; parents"), ("조부모", "grandparents (the book’s hint: 조 祖 = grand-)"), ("모국", "one’s mother country; “mother nation” (mine)"),
            ("모친", "one’s mother (formal) (mine)"), ("부친", "one’s father (formal) (mine)"), ("부자간", "between father and son (mine)")]
_FU2C = [("우리 외할머니는 일흔이시고 뉴저지주에 사십니다.", "My maternal grandmother is seventy and lives in New Jersey."), ("외할아버지는 안 계십니다.", "My maternal grandfather is not here (he has passed away or is not with us).")]
L8 = lesson(
    "Ch 10 · Topic C: We visited PFC Baek’s parents’ home",
    "백 일병 부모님 댁을 방문했습니다 · 큰아버지 · 작은아버지 · 이모부 · 사촌 · 조카 · 부 (父) · 모 (母)",
    requires=[],
    cards=[
        card("Reading: a visit to PFC Baek’s parents’ home",
             "PV2 Kim is talking about his visit to PFC Baek’s parents’ home in Hollywood to attend Baek’s father’s 60th birthday celebration. (The English is mine.)",
             examples=passage(_C_PASS)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary, which lists them under Kinship Terms, Time Expressions and Other Words). The book writes 데리고 가다/모시고 가다 (↑), 데리고 오다/모시고 오다 (↑), 방문(하다), 올해/금년 and 여러 (가지) as groups; they are split here. -는/(으)ㄴ/(으)ㄹ has its own grammar lesson.",
             tables=[ktable(_C_PAIRS)]),
        card("The family tree (가계도)",
             "The book shows a family tree with these labels: 고모부, 고모, 외삼촌, 큰아버지, 이모, 큰어머니, 이모부, 할아버지, 할머니, 외할아버지, 외할머니, 아버지, 나 and 어머니 (the picture is left out). The terms are below, with the book’s meanings from the Core Vocabulary; 할아버지, 할머니, 아버지, 어머니 and 나 are not glossed there, so their English is mine.",
             tables=[ktable(_FAM)]),
        card("To take or bring: 데리고, 모시고, 가지고",
             "Koreans use 가다 and 오다 to show movement from one place to another. Because “take” and “bring” involve movement, Koreans express these verbs with a compound verb that includes 가다 or 오다. Three different verbs can be used, and the type of object decides which: (~을/를) 데리고 가다/오다 for a person or an animal, (~을/를) 모시고 가다/오다 for a person you show respect to, and (~을/를) 가지고 가다/오다 for an inanimate object.",
             tables=[ktable(_TAKE)], examples=[D(a, b) for a, b in _TAKE_EX]),
        card("Cultural note: 환갑 (the 60th birthday)",
             "환갑 (or 회갑), the 60th birthday, is considered the most important birthday. The number 60 means completing one zodiacal cycle and beginning another in one’s lifespan. In the past the average life expectancy was much lower than today, so 환갑 also meant a celebration of longevity, and the party is a wish for an even longer and more prosperous life. In the traditional 환갑 celebration, children honor their parents by throwing a big party with a large feast and much merrymaking; children and grandchildren typically wear hanbok (한복) and bow to the parents to pay their respects. Today, with longer lives, the celebration has become simpler and less significant: many Koreans eat out with close friends and family or take a trip with the family. The 70th birthday, called 칠순 or 고희, and the 80th birthday, called 팔순, are celebrated as well."),
        card("Sino-Korean in use: 부모 (父母)",
             "The first syllable 부 (父) means father or paternal, as in 부자 (father and son) and 부녀 (father and daughter), while the second syllable 모 (母) means mother or maternal, as in 모자 (mother and son) and 모녀 (mother and daughter). Hence 부모 means father and mother, or parents. The book asks you to guess the meaning of 조부모 (조 祖 = grand-) and 모국; its Core Vocabulary also lists 모친, 부친 and 부자간 without meanings, so those are mine.",
             tables=[ktable(_SINO_BM)]),
        card("Follow-up 2: talking about your family",
             "In the book you think about your extended family members (yourself, your spouse and children if married, siblings, parents, aunts and uncles, and grandparents on both sides), including their age, occupation and residence, and exchange the information with a partner. The book’s model is below (the English is mine). 일흔 is the native number for seventy.",
             examples=passage(_FU2C)),
        card("Activities left out",
             "The SMART Board activity, the reporter-and-writer activity (reading a text posted outside the classroom and reporting it to a partner who writes it down), and Follow-up 1 (listening to three narrations about family occasions, to identify the occasion and who attends) are audio, SMART Board or partner activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS if k not in ("금년", "모시고 가다", "모시고 오다")])
        + _tr(_C_PASS) + _tr(_TAKE_EX) + _tr(_FU2C)
        + [M(f"What does {a} mean?", b, [x for _, x in _SINO_BM if x != b][:3], f"{a}: {b}.") for a, b in _SINO_BM[:7]]
        + [M("Who is a father’s sister?", "고모", ["이모", "외삼촌", "큰어머니"], "고모 = father’s sister."), M("Who is a mother’s sister?", "이모", ["고모", "외삼촌", "작은어머니"], "이모 = mother’s sister."), M("Who is a mother’s brother?", "외삼촌", ["작은아버지", "큰아버지", "고모부"], "외삼촌 = mother’s brother."),
           M("Who is a father’s older brother?", "큰아버지", ["작은아버지", "외삼촌", "이모부"], "큰아버지 = big father."), M("Who is a father’s younger brother?", "작은아버지", ["큰아버지", "외삼촌", "이모부"], "작은아버지 = little father."), M("Who is the husband of a father’s sister?", "고모부", ["이모부", "큰아버지", "외삼촌"], "고모부."),
           M("Who is the husband of a mother’s sister?", "이모부", ["고모부", "큰아버지", "작은아버지"], "이모부."), M("Who is the wife of a father’s older brother?", "큰어머니", ["작은어머니", "이모", "형수"], "큰어머니."), M("Who is the wife of a father’s younger brother?", "작은어머니", ["큰어머니", "이모", "형수"], "작은어머니."),
           M("Who is a man’s older brother’s wife?", "형수", ["큰어머니", "이모", "조카"], "형수."), M("Who is a sibling’s child?", "조카", ["사촌", "형수", "외삼촌"], "조카 = nephew or niece."), M("Who is the father of your mother?", "외할아버지", ["할아버지", "큰아버지", "외삼촌"], "외 = maternal."),
           M("Which verb do you use to bring a person you respect?", "모시고 오다", ["데리고 오다", "가지고 오다", "보내다"], "모시고 = respectfully accompany."), M("Which verb do you use to take a friend or an animal?", "데리고 가다", ["모시고 가다", "가지고 가다", "보내다"], "데리고 = accompany (person or animal)."),
           M("Which verb do you use to take an inanimate object?", "가지고 가다", ["데리고 가다", "모시고 가다", "보내다"], "가지고 = possess."), M("Which birthday is the most important in Korea?", "The 60th (환갑)", ["The 1st", "The 40th", "The 100th"], "환갑 = the 60th birthday."), M("What is the 70th birthday called?", "칠순 or 고희", ["환갑", "팔순", "회갑"], "칠순/고희 = 70th."),
           M("What is the 80th birthday called?", "팔순", ["칠순", "환갑", "고희"], "팔순 = 80th."), M("Who came to PFC Baek’s house?", "Uncles, aunts and cousins", ["Only his father", "Only his teacher", "Nobody"], "작은아버지, 이모, 사촌들."), M("When was PFC Baek’s nephew/niece born?", "Last year", ["This year", "Next year", "Ten years ago"], "작년에 태어났습니다."),
           F("백 일병의 형과 형수는 조카를 ___ 왔습니다. (brought, a baby)", "데리고", ["가지고", "모시고"], "A baby is a person: 데리고."), F("내일 학교에 부모님을 ___ 오세요. (bring, respect)", "모시고", ["데리고", "가지고"], "Parents → 모시고."), F("학교에 오자마자 숙제를 ___ 오세요. (bring, object)", "가지고", ["데리고", "모시고"], "Homework is an object → 가지고."),
           F("어머니는 ___에 환갑이 되십니다. (next year)", "내년", ["작년", "올해"], "내년 = next year."), F("백 일병의 조카는 ___에 태어났습니다. (last year)", "작년", ["내년", "올해"], "작년 = last year."), F("백 일병 가족과 친척들은 ___ 가지 선물을 가지고 왔습니다. (various)", "여러", ["너무", "가장"], "여러 가지 = various."),
           read_q("큰아버지"), read_q("작은어머니"), read_q("외할아버지"), read_q("사촌"), read_q("환갑잔치에서")]
    ),
)

# ================================================================== Grammar C: attributive forms
_AT_V = [("먹다", "음식"), ("자다", "사람"), ("읽다", "책"), ("가다", "곳"), ("만나다", "친구"), ("사다", "옷"), ("보다", "영화"), ("공부하다", "학생"), ("노래하다", "사람"), ("타다", "버스"), ("살다", "집"), ("만들다", "음식"), ("알다", "사람"), ("놀다", "친구")]
_AT_EX = [
    ("공부하는 학생", "a student who studies / is studying"), ("공부한 학생", "a student who studied"), ("공부할 학생", "a student who will study"), ("도서관에서 공부하는 학생", "a student who studies in the library"), ("매일 도서관에서 공부하는 학생", "a student who studies in the library every day"),
    ("도서관에서 공부하는 학생은 제 친구예요.", "The student who studies in the library is my friend."), ("내가 공부하는 언어는 한국어입니다.", "The language I am studying is Korean."), ("내가 자주 가는 카페는 몬트레이에 있습니다.", "The cafe that I often go to is in Monterey."),
    ("어제 파티에서 먹은 음식이 맛있었어요.", "The food that I ate at the party yesterday was delicious."), ("파티에서 만난 사람들도 친절했어요.", "The people I met at the party were also friendly."), ("이번 주말에 읽을 책이 많아요.", "I’ve got a lot of books to read this weekend."), ("그리고 할 일도 많아요.", "And I also have a lot of work to do."),
]
_AT_PH = [("지금 읽는 책", "the book I am reading now"), ("매일 가는 카페", "the cafe I go to every day"), ("어제 읽은 책", "the book I read yesterday"), ("어제 먹은 음식", "the food I ate yesterday"), ("어제 만난 친구", "the friend I met yesterday"), ("어제 간 곳", "the place I went yesterday"),
          ("내일 읽을 책", "the book I will read tomorrow"), ("내일 먹을 음식", "the food I will eat tomorrow"), ("내일 할 일", "the work I will do tomorrow"), ("내일 갈 곳", "the place I will go tomorrow")]
_AT_FU2 = [("지금 노래하는 사람이 누구예요?", "노래하다", "노래하는", "Who is the person singing now?"), ("어제 백화점에서 산 옷이에요.", "사다", "산", "These are clothes that I bought at the department store yesterday."), ("내일 학교에 올 학생 있어요?", "오다", "올", "Is there a student who will come to school tomorrow?"),
           ("요즘 지하철을 타는 사람들이 많아요.", "타다", "타는", "These days there are many people who ride the subway."), ("뉴욕에 사는 사촌이 두 명 있어요.", "살다", "사는", "I have two cousins who live in New York.")]
_AT_NOTE = [("서현아,", "Seohyun,"), ("오늘은 해야 할 숙제가 너무 많아.", "Today I have too much homework to do."), ("내일 만나자.", "Let’s meet tomorrow."), ("시내에 있는 카페에서 다섯 시 어때?", "How about five o’clock at the cafe downtown?"),
            ("그리고 어제 너랑 먹은 음식이 맛있었어.", "And the food I ate with you yesterday was delicious."), ("내일도 그 식당에 가자.", "Let’s go to that restaurant tomorrow too."), ("그럼, 내일 봐.", "Then see you tomorrow."), ("민호가", "From Minho")]
L9 = lesson(
    "Ch 10 · Grammar C: attributive forms of action verbs -는, -(으)ㄴ, -(으)ㄹ",
    "공부하는 학생 · 공부한 학생 · 공부할 학생 · 먹는 음식 · 먹은 음식 · 먹을 음식",
    requires=[],
    cards=[
        card("Attributive forms of action verbs",
             "Look at the English phrases “a crying baby”, “a baby who is sleeping in the crib”, “time to sleep”, “a place for eating kimchi” and “a reason why John learned Korean”: the italicized words or phrases modify the nouns and function as adjectives. In Korean we express all of them with attributive forms. In Chapter 4 you learned the attributive forms of stative verbs (싼 컴퓨터, 좋은 컴퓨터), made by adding (으)ㄴ to the stem. Action verbs have three attributive forms, one for each tense: 공부하는 학생 (a student who studies/is studying; present), 공부한 학생 (a student who studied; past) and 공부할 학생 (a student who will study; future). Each form modifies the noun that comes right after it, and can be expanded by adding more elements in front: 공부하는 학생 → 도서관에서 공부하는 학생 → 매일 도서관에서 공부하는 학생. The modified noun is still a noun and is used as part of the sentence.",
             examples=[D(a, b) for a, b in _AT_EX[:6]]),
        card("The three attributive forms",
             "Present: verb stem + 는 (an ongoing or habitual action), as in 지금 읽는 책 and 매일 가는 카페. Past: verb stem + (으)ㄴ (a completed action): 은 after a consonant (어제 읽은 책, 어제 먹은 음식), ㄴ after a vowel (어제 만난 친구, 어제 간 곳). Future: verb stem + (으)ㄹ (an anticipated action): 을 after a consonant (내일 읽을 책, 내일 먹을 음식), ㄹ after a vowel (내일 할 일, 내일 갈 곳). A stem that ends in ㄹ drops the ㄹ before 는 and ㄴ (살다 → 사는, 산) and takes the future form as it is (살 → 살); this is the ordinary rule for ㄹ stems, not stated in the book, so the forms of 살다, 만들다, 알다 and 놀다 below are mine.",
             tables=[table(["Tense", "Condition", "Rule", "Examples"], [["Present", "any verb stem", "add 는", "(지금) 읽는 책; (매일) 가는 카페"], ["Past", "stem ends in a consonant", "add 은", "(어제) 읽은 책; (어제) 먹은 음식"], ["Past", "stem ends in a vowel", "add ㄴ", "(어제) 만난 친구; (어제) 간 곳"],
                                                                         ["Future", "stem ends in a consonant", "add 을", "(내일) 읽을 책; (내일) 먹을 음식"], ["Future", "stem ends in a vowel", "add ㄹ", "(내일) 할 일; (내일) 갈 곳"]])],
             examples=[D(a, b) for a, b in _AT_EX[6:]]),
        card("Phrases from the book’s table",
             "The ten phrases of the book’s three tables; the English is mine.",
             tables=[ktable(_AT_PH)]),
        card("Follow-up 1: three attributive forms",
             "The book’s model: A: 먹다 / 음식 B: 먹는 음식, 먹은 음식, 먹을 음식; and B: 자다 / 사람 A: 자는 사람, 잔 사람, 잘 사람. In the book the teacher gives each pair a set of noun and verb cards; the first two pairs are the book’s, the other pairs are mine.",
             tables=[table(["Verb / noun", "Present (-는)", "Past (-(으)ㄴ)", "Future (-(으)ㄹ)"], [[f"{v} / {n}", *[f"{a} {n}" for a in attr(v)]] for v, n in _AT_V], say=[1, 2, 3])]),
        card("Follow-up 2: change the verb and translate",
             "The book gives five sentences with the verb in parentheses; you change it into the right attributive form and translate. The answers and the English are mine.",
             tables=[table(["Sentence", "Verb", "Form", "Meaning"], [[s, v, f, e] for s, v, f, e in _AT_FU2], say=[0])]),
        card("Follow-up 4: Minho’s note to Seohyun",
             "The book gives a short note from Minho to his girlfriend Seohyun and asks you to underline the attributive forms, circle the nouns they modify and translate the underlined phrases. The note is the book’s (the book writes 5시, which is spelled out); the English is mine. The attributive phrases I find are 해야 할 숙제 (homework that I must do), 시내에 있는 카페 (a cafe that is downtown) and 너랑 먹은 음식 (the food I ate with you).",
             examples=passage(_AT_NOTE)),
        card("Activities left out",
             "Follow-up 3 (listening to three sentences, to circle the attributive form and write the noun it modifies) and Follow-up 5 (partners each hold a picture of six people and describe what some of them are doing with 는/(으)ㄴ to find out the kinship terms) are audio or picture-and-partner activities. The noun and verb cards of Follow-up 1 are the teacher’s."),
    ],
    exercises=uniq(
        [M(f"What is the present attributive form of {v} (before {n})?", attr(v)[0], [attr(v)[1], attr(v)[2], stem(v) + "고"], f"{v} → {attr(v)[0]} {n}.") for v, n in _AT_V]
        + [M(f"What is the past attributive form of {v} (before {n})?", attr(v)[1], [attr(v)[0], attr(v)[2], stem(v) + "었"], f"{v} → {attr(v)[1]} {n}.") for v, n in _AT_V]
        + [M(f"What is the future attributive form of {v} (before {n})?", attr(v)[2], [attr(v)[0], attr(v)[1], stem(v) + "고"], f"{v} → {attr(v)[2]} {n}.") for v, n in _AT_V]
        + [M(f"What does {a} mean?", b, [x for _, x in _AT_PH if x != b][:3], f"{a} means “{b}”.") for a, b in _AT_PH]
        + _tr(_AT_EX[5:]) + _tr([(s, e) for s, _, _, e in _AT_FU2]) + _tr(_AT_NOTE[1:7])
        + [F(f"{s.replace(f, '___', 1)} ({v})".replace(" (", " (", 1), f, [x for x in attr(v) if x != f][:2], f"{v} → {f}.") for s, v, f, e in _AT_FU2]
        + [F("어제 파티에서 ___ 음식이 맛있었어요. (ate)", "먹은", ["먹는", "먹을"], "A completed action: 먹은."), F("내가 매일 ___ 카페는 몬트레이에 있어요. (go)", "가는", ["간", "갈"], "A habitual action: 가는."), F("이번 주말에 ___ 책이 많아요. (to read)", "읽을", ["읽는", "읽은"], "An anticipated action: 읽을."),
           F("내일 ___ 일이 많아요. (to do)", "할", ["하는", "한"], "Future: 할."), F("어제 파티에서 ___ 사람들이 친절했어요. (met)", "만난", ["만나는", "만날"], "Past: 만난."), F("지금 책을 ___ 학생은 제 친구예요. (is reading)", "읽는", ["읽은", "읽을"], "Present: 읽는."),
           M("Which attributive form is for an ongoing or habitual action?", "-는", ["-(으)ㄴ", "-(으)ㄹ", "-고"], "Present: 는."), M("Which attributive form is for a completed action?", "-(으)ㄴ", ["-는", "-(으)ㄹ", "-고"], "Past: (으)ㄴ."), M("Which attributive form is for an anticipated action?", "-(으)ㄹ", ["-는", "-(으)ㄴ", "-고"], "Future: (으)ㄹ."),
           M("What does 공부하는 학생 mean?", "a student who studies", ["a student who studied", "a student who will study", "a student’s study"], "는 = present."), M("What does 공부할 학생 mean?", "a student who will study", ["a student who studies", "a student who studied", "a student’s study"], "ㄹ = future."),
           M("What comes right after an attributive form?", "The noun it modifies", ["A particle", "A verb", "A number"], "공부하는 학생."), M("Which ending turns a stative verb into an attributive form?", "-(으)ㄴ", ["-는", "-(으)ㄹ", "-고"], "싼 컴퓨터, 좋은 컴퓨터."),
           read_q("먹는 음식"), read_q("먹은 음식"), read_q("먹을 음식"), read_q("공부하는 학생"), read_q("시내에 있는 카페")]
    ),
)


# ================================================================== Activities C: Chaeho's e-mail
_EM = [
    ("삼촌,", "Uncle,"), ("지난주에 어머니 환갑이었어요.", "Last week was my mother’s 60th birthday."), ("그래서 가족들이 모두 같이 여행을 다녀왔어요.", "So the whole family went on a trip together."),
    ("제주도로 삼박사일 동안 갔다 왔어요.", "We went to Jeju Island for three nights and four days."), ("어머니, 아버지, 형 가족, 이모, 이모부, 그리고 나, 이렇게 모두 여덟 명이 갔어요.", "My mother, my father, my brother’s family, my aunt, her husband and I, eight people in all, went."),
    ("형은 형수와 지난 유월에 태어난 조카를 데리고 왔어요.", "My older brother brought my sister-in-law and the baby who was born last June."), ("제주도에서는 이것저것 구경할 게 아주 많았어요.", "In Jeju there was a lot to see of this and that."),
    ("그런데 날씨가 안 좋았어요.", "But the weather was not good."), ("그래서 아버지께서 좋아하시는 등산은 못 했어요.", "So we couldn’t do the hiking that my father likes."), ("여행하는 동안 기념품도 사고 사진도 많이 찍었어요.", "During the trip we bought souvenirs and took a lot of photos."),
    ("아주 재미있었어요.", "It was a lot of fun."), ("삼촌, 제가 나중에 전화할게요.", "Uncle, I’ll call you later."), ("재호가", "From Chaeho"),
]
L10 = lesson(
    "Ch 10 · Activities C: an e-mail about a family trip",
    "어머니 환갑여행 · 제주도로 삼박사일 · 조카를 데리고 왔어요",
    requires=[],
    cards=[
        card("Activity 3 (Reading): Chaeho’s e-mail to his uncle",
             "Chaeho sent this e-mail to his uncle Hyunchae, who lives in the U.S.; the subject line is 어머니 환갑여행 (a trip for my mother’s 60th birthday). The book asks you to fill in a table in English with the occasion, the time and duration, the location, the participants and the activities. The text is the book’s, with 3박 4일 and 6월 spelled out in Hangul; the sender and recipient lines with e-mail addresses are left out. The English is mine.",
             examples=passage(_EM)),
        card("The e-mail: the table filled in",
             "My key to the book’s table.",
             tables=[table(["Occasion", "Time & duration", "Location", "Participants", "Activities"], [["Chaeho’s mother’s 60th birthday (환갑)", "Last week; three nights and four days", "Jeju Island (제주도)", "Eight people: his mother, father, older brother’s family (brother, sister-in-law and baby), aunt (이모), her husband (이모부) and Chaeho", "Sightseeing, buying souvenirs, taking photos; no hiking because of the weather"]])]),
        card("Grammar and words to notice",
             "The e-mail uses several things from this chapter and earlier: 환갑 (the 60th birthday); 데리고 오다 (to bring a person); the attributive form 태어난 (born) in 유월에 태어난 조카, and 좋아하시는 (that he likes, honorific) in 아버지께서 좋아하시는 등산; 동안 (during, for) in 삼박사일 동안 and 여행하는 동안; the negative 못 했어요 (couldn’t do). 이것저것 means “this and that”; 등산 is hiking and 기념품 is a souvenir (the meanings of these three are mine; the book does not gloss them here)."),
        card("Activities left out",
             "Activity 1 (SMART Board), Activity 2 (a video clip from the TV sitcom 거침없이 하이킥, in which a woman tries to arrange a lunch over the phone and her sister-in-law keeps making excuses involving relatives; you fill in a table in English with days of the week, the kinship terms mentioned and the occasion) and Activity 4 (listening to two customers’ phone messages to an event planner in Seoul, noting the purpose of the call, the event date and the contact number, then planning an event program in pairs, writing it on a flip chart and presenting it) are video, audio, SMART Board or partner activities."),
    ],
    exercises=uniq(
        _tr(_EM[1:12])
        + [M("What was the occasion of the trip?", "His mother’s 60th birthday", ["His own wedding", "A school break", "His father’s retirement"], "어머니 환갑이었어요."), M("Where did the family go?", "Jeju Island", ["Seoul", "Busan", "Hawaii"], "제주도로 갔다 왔어요."),
           M("How long was the trip?", "Three nights and four days", ["Two nights and three days", "Four nights and five days", "A week"], "삼박사일."), M("How many people went?", "Eight", ["Six", "Seven", "Nine"], "모두 여덟 명이 갔어요."),
           M("Who did Chaeho’s older brother bring?", "His wife and the baby", ["His parents", "His cousins", "His teacher"], "형수와 조카를 데리고 왔어요."), M("Why couldn’t they go hiking?", "The weather was bad", ["They had no time", "The baby was sick", "It was too expensive"], "날씨가 안 좋았어요."),
           M("What did they do on the trip?", "Bought souvenirs and took photos", ["Went swimming", "Studied", "Stayed in the hotel"], "기념품도 사고 사진도 많이 찍었어요."), M("Who likes hiking?", "Chaeho’s father", ["Chaeho’s mother", "Chaeho’s brother", "Chaeho’s uncle"], "아버지께서 좋아하시는 등산."),
           M("When will Chaeho call his uncle?", "Later", ["Tomorrow", "Right now", "Next year"], "나중에 전화할게요."),
           F("제주도로 삼박사일 ___ 갔다 왔어요. (for)", "동안", ["보다", "때문에"], "동안 = during/for."), F("형은 형수와 조카를 ___ 왔어요. (brought)", "데리고", ["가지고", "모시고"], "A baby: 데리고."), F("아버지께서 ___ 등산은 못 했어요. (that he likes)", "좋아하시는", ["좋아하신", "좋아할"], "Present attributive, honorific."),
           F("날씨가 안 좋았어요. ___ 등산은 못 했어요. (So)", "그래서", ["그런데", "그리고"], "그래서 = so."), F("지난주에 어머니 ___이었어요. (60th birthday)", "환갑", ["내년", "조카"], "환갑 = the 60th birthday."),
           read_q("환갑이었어요"), read_q("삼박사일"), read_q("태어난 조카"), read_q("기념품도 사고")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
def _uo(*texts):
    """possessive 의 after a person word is said 에"""
    over = {}
    for t in texts:
        for w in _re.findall(r"[가-힣]+의", t):
            over[w] = _K.pron(w[:-1] + "에")
    return over


_V_TR = [("고속버스", "an express bus; “high-speed bus”", "그레이하운드 고속버스로 샌디에고에 갑니다."), ("공항", "an airport", "몬트레이 공항에서 비행기를 탑니다."), ("기차", "a train", "몬트레이에는 기차가 없습니다."), ("열차", "a train", "몬트레이에는 열차가 없습니다."),
         ("느리다", "to be slow", "자동차가 비행기보다 느립니다."), ("떨어지다", "to be out of; to run out of; “fall/drop”", "기름이 떨어져서 주유소에 들렀어요."), ("배", "a ship; a boat", "부산 앞 바다에 배가 많습니다."), ("빠르다", "to be fast; to be quick", "비행기는 아주 빠릅니다."),
         ("역", "a train station; a subway station", "서울역 앞에서 버스를 탔습니다."), ("정류장", "a (bus/taxi) stop", "버스 정류장에서 버스를 탑니다."), ("지하철", "a subway; “underground steel”", "뉴욕과 샌프란시스코에는 지하철이 있습니다."),
         ("항구", "a harbor; a port", "부산항에는 배가 많습니다."), ("항", "a harbor; a port (the short form of 항(구))", "부산항에는 배가 많습니다.")]
_V_DIR = [("갈아타다", "to transfer (means of transportation); to get on (to a different road); “change and ride”", "일 번 고속도로에서 백일 번 고속도로로 갈아타고 산호세에 갑니다."), ("고속도로", "highway; “high-speed road”", "백일 번 고속도로로 가면 더 빠릅니다."),
          ("복잡하다", "to be complicated; (road) to be congested", "주말에는 길이 아주 복잡합니다."), ("세우다", "to stop; to park; to pull over", "운전중 전화가 오면 길 옆에 차를 세우고 전화를 받습니다."), ("신호등", "a traffic signal light; “signal lamp”", "큰 사거리에는 신호등이 있어요."),
          ("입구", "an entrance; “entering mouth”", "열 시에 백화점 입구에서 만납시다."), ("길을 잃다", "to get lost; to be lost (in direction); “lose the way”", "큰 도시에 가면 길을 자주 잃어요."), ("출구", "an exit; “exiting mouth”", "일 번 고속도로에서 몬트레이 출구로 나오면 공원이 있습니다.")]
_V_KIN = [("고모", "father’s sister", "아버지는 여자 형제가 두 명 있어요. 그래서 저는 고모가 두 분입니다."), ("고모부", "husband of the father’s sister", "고모부는 고모의 남편입니다."), ("사촌", "cousin; a child of the father’s siblings; “fourth relationship”", "아버지 형제는 자녀가 많습니다. 그래서 저는 사촌이 많습니다."),
          ("외삼촌", "mother’s brother", "제 외삼촌은 중학교 선생님이십니다."), ("외할머니", "maternal grandmother", "외할머니는 올해 연세가 예순이십니다."), ("외할아버지", "maternal grandfather", "외할아버지는 어머니의 아버지입니다."), ("이모", "mother’s sister", "제 큰이모는 캐나다에 삽니다."),
          ("이모부", "husband of the mother’s sister", "이모부는 이모의 남편입니다."), ("작은아버지", "father’s married younger brother; “little father”", "작은아버지는 의사이십니다."), ("작은어머니", "wife of the father’s married younger brother; “little mother”", "작은아버지와 작은어머니는 삼 년 전에 결혼했습니다."),
          ("조카", "a nephew; a niece; a sibling’s child", "제 형은 딸이 두 명 있어요. 그래서 저는 조카가 두 명이에요."), ("큰아버지", "a father’s married older brother; “big father”", "제 아버지는 올해 연세가 쉰이시고, 큰아버지는 쉰 넷이십니다."),
          ("큰어머니", "the wife of a father’s married older brother; “big mother”", "큰어머니는 큰아버지의 부인입니다."), ("형수", "a man’s older brother’s wife", "형 두 명이 모두 결혼해서 저는 형수님이 두 분 계십니다.")]
_V_TIME = [("내년", "next year; “coming year”", "내년에 유럽을 여행하고 싶어요."), ("내일", "tomorrow; “coming day”", "내일 비가 올 거예요."), ("오늘", "today", "오늘은 쉬는 날입니다."), ("올해", "this year", "올해 연세가 어떻게 되십니까?"),
           ("금년", "this year", "금년 연세가 어떻게 되십니까?"), ("작년", "last year", "작년 겨울에는 눈이 많이 왔습니다."), ("지금", "now", "지금 몇 시입니까?")]
_V_LOAN = [("렌터카", "a rental car", "렌터카 회사에서 차를 빌렸습니다."), ("버스", "a bus", "카멜 가는 버스를 어디에서 타요?"), ("터미널", "a terminal", "고속버스 터미널에서 고속버스를 탈 수 있어요.")]
_V_OTH = [("가장", "the most; the -est", "미국에서 알래스카 주가 가장 큽니다."), ("가지고 가다", "to take something somewhere; “to possess and go”", "친구 생일파티에 선물을 가지고 갔습니다."), ("가지고 오다", "to bring something; “to possess and come”", "내일 학교에 아이패드를 가지고 오세요."),
          ("값", "price", "캘리포니아는 집값이 비싸요."), ("가격", "price", "캘리포니아는 집 가격이 비싸요."), ("계속", "continuously", "일 번 고속도로로 계속 가면 백오십육 번 고속도로를 만납니다."), ("공사 중", "under construction; “in the middle of construction”", "학교 앞 도로가 공사 중이어서 아주 복잡합니다."),
          ("귀엽다", "to be cute", "제 동생은 한 살인데 아주 귀엽습니다."), ("-기 때문에", "because", "비가 오기 때문에 길이 많이 막혀요."), ("~ 때문에", "because of", "비 때문에 길이 많이 막혀요."), ("내다", "to pay (money)", "미국 식당에서는 팁을 십 퍼센트에서 십오 퍼센트 정도 냅니다."),
          ("너무", "too; overly", "로스앤젤레스에서 뉴욕까지는 너무 멀어요."), ("더", "more", "반찬 좀 더 주세요."), ("데리고 가다", "to take someone somewhere", "도서관에 동생을 데리고 갔어요."), ("모시고 가다", "to take someone somewhere (↑)", "도서관에 부모님을 모시고 갔어요."),
          ("데리고 오다", "to bring someone", "파티에 여자친구를 데리고 왔어요."), ("모시고 오다", "to bring someone (↑)", "파티에 부모님을 모시고 왔어요."), ("되다", "to become; to be", "제 동생은 공군장교가 되고 싶어해요."), ("들다", "to cost", "엘에이까지 차로 가면 비용이 얼마나 들어요?"),
          ("방문", "visit", "저는 이틀 동안 뉴욕에 사는 친구를 방문했어요."), ("방문하다", "to visit", "저는 이틀 동안 뉴욕에 사는 친구를 방문했어요."), ("~보다 (더)", "more … than; …er than", "뉴욕이 몬트레이보다 더 큽니다."), ("불편하다", "to be uncomfortable; to be inconvenient", "차가 없어서 불편해요."),
          ("비싸다", "to be expensive; “to be not cheap”", "애플 컴퓨터가 피씨보다 더 비쌉니다."), ("비용", "expense; cost; expenditure", "인터넷으로 예약하면 여행 비용이 적게 들어요."), ("빌리다", "to borrow; to rent", "결혼식에 입을 웨딩드레스를 빌렸습니다."), ("싸다", "to be cheap", "달러트리에서는 모든 물건이 일 달러입니다. 아주 쌉니다."),
          ("여러", "various", "어제 여러 가지 크리스마스 선물을 샀어요."), ("여러 가지", "various (types of)", "어제 여러 가지 크리스마스 선물을 샀어요."), ("적게", "few; little", "저는 음식을 적게 먹어요."), ("적다", "to be few; to be little", "우리 반은 학생 수가 적어요."),
          ("조심", "care; caution", "눈이 오면 운전을 조심하세요."), ("조심하다", "to be careful; to be cautious", "눈이 오면 운전을 조심하세요."), ("태어나다", "to be born", "저는 " + year_ko(1987) + " " + month_ko(1) + " " + day_ko(1) + "에 태어났어요."), ("편의점", "a convenience store", "집 앞에 편의점이 있어서 편해요."),
          ("혹시", "by any chance", "혹시 국방외국어대학 학생입니까?")]
_V_ATTR = [["-는 (present)", "attributive forms of action verbs", "저기가 제가 매일 운동하는 체육관입니다."], ["-(으)ㄴ (past)", "attributive forms of action verbs", "점심에 먹은 음식이 맛있었어요."], ["-(으)ㄹ (future)", "attributive forms of action verbs", "내일 할 일이 많아요."]]
_V_SINO = [("구", "(口) a mouth; a door", "입구, 출구, 비상구"), ("모", "(母) a mother", "부모, 모친, 모국"), ("부", "(父) a father", "조부모, 부친, 부자간"), ("입", "(入) entering; (getting) in", "입학, 입국, 입대"), ("출", "(出) exit; (getting) out", "출국, 출발, 출항")]
_V_ALL = _V_TR + _V_DIR + _V_KIN + _V_TIME + _V_LOAN + _V_OTH
_V_OVER = _uo(*[e for _, _, e in _V_ALL])
_V_SKIP = ("-기 때문에", "~ 때문에", "~보다 (더)", "열차", "항", "금년", "가격", "모시고 가다", "모시고 오다", "여러 가지")
L11 = lesson(
    "Ch 10 · Core vocabulary and self-evaluation",
    "주요 단어 · 교통 · 길 · 친척 · 시간 · 구 · 모 · 부 · 입 · 출 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). The book writes pairs together (기차/열차, 항(구), 올해/금년, 값/가격, 여러 (가지), 방문(~하다), 조심(~하다), 데리고 가다/모시고 가다 (↑)); they are split here. Two of the book’s sentences have two versions (이 의자가 좀 불편해요 / 차가 없어서 불편해요; 책 살 돈이 없어요… / 결혼식에 입을 웨딩드레스를 빌렸습니다) and only the second is shown. The book’s Additional Vocabulary section is a blank list for words you add yourself.\n\n"
             "Where a split word has no sentence of its own, it reuses the book’s sentence with the variant substituted (열차, 금년, 가격, 모시고 가다/오다 with a respected person). Digits are respelled in Hangul (1번 고속도로 → 일 번 고속도로, 101번 → 백일 번, 156번 → 백오십육 번, 10시 → 열 시, 3년 → 삼 년, 10-15% → 십 퍼센트에서 십오 퍼센트, 1달러 → 일 달러, 1987년 1월 1일 → 천구백팔십칠년 일월 일일); LA is said 엘에이, PC 피씨; the possessive 의 after a person is said 에."),
        card("Transportation", "", tables=[vt(_V_TR, over=_V_OVER)]),
        card("Directions", "", tables=[vt(_V_DIR, over=_V_OVER)]),
        card("Kinship terms", "", tables=[vt(_V_KIN, over=_V_OVER)]),
        card("Time expressions", "", tables=[vt(_V_TIME, over=_V_OVER)]),
        card("Loan words", "", tables=[vt(_V_LOAN, over=_V_OVER)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_V_OTH, over=_V_OVER)]),
        card("The attributive forms", "The book lists the attributive forms of action verbs, -는/-(으)ㄴ/-(으)ㄹ, with one sentence for each form; the grammar lesson explains them.", tables=[table(["Form", "Meaning", "Example"], _V_ATTR, say=[2])]),
        card("Sino-Korean vocabulary", "", tables=[vt(_V_SINO)]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about trip planning, including the means of transportation; compare two things or people; give and understand directions; use proper kinship terms for an extended family.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; comparative 보다 (더) (more … than; …er than); the conjunctive ending -기 때문에 (because); ~때문에 (because of); the attributive forms of action verbs -는, -(으)ㄴ and -(으)ㄹ; the Sino-Korean syllables 부 (父), 모 (母), 출 (出), 입 (入) and 구 (口)."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _V_ALL if k not in _V_SKIP])
        + [M(f"What does {k} mean?", e.split(" ", 1)[1].rstrip(), [x for _, x, _ in _V_SINO if x != e][:3] if False else [x.split(" ", 1)[1] for _, x, _ in _V_SINO if x != e][:3], f"{k} {e}.") for k, e, _ in _V_SINO]
        + [M("What does ~ 때문에 mean?", "because of", ["because", "if", "than"], "비 때문에 = because of the rain."), M("What does -기 때문에 mean?", "because", ["because of", "if", "than"], "비가 오기 때문에 = because it rains."), M("What does ~보다 (더) mean?", "more … than; …er than", ["because of", "the most", "too much"], "몬트레이보다 더 큽니다."),
           M("Which word is an antonym of 싸다?", "비싸다", ["빠르다", "느리다", "귀엽다"], "싸다 ↔ 비싸다."), M("Which word is an antonym of 빠르다?", "느리다", ["싸다", "복잡하다", "귀엽다"], "빠르다 ↔ 느리다."), M("Which word is an antonym of 많다 (many) in the chapter’s vocabulary?", "적다", ["더", "너무", "가장"], "적다 = to be few."),
           M("Which Sino-Korean syllable is in 입구, 출구 and 비상구?", "구 (口)", ["모 (母)", "부 (父)", "입 (入)"], "구 = mouth; door."), M("Which Sino-Korean syllable is in 입학, 입국 and 입대?", "입 (入)", ["출 (出)", "구 (口)", "부 (父)"], "입 = entering."), M("Which Sino-Korean syllable is in 출국, 출발 and 출항?", "출 (出)", ["입 (入)", "구 (口)", "모 (母)"], "출 = exit."),
           M("Which Sino-Korean syllable is in 부모, 모친 and 모국?", "모 (母)", ["부 (父)", "구 (口)", "출 (出)"], "모 = mother."), M("Which Sino-Korean syllable is in 조부모, 부친 and 부자간?", "부 (父)", ["모 (母)", "구 (口)", "입 (入)"], "부 = father."),
           F("비가 오기 ___ 길이 많이 막혀요. (because)", "때문에", ["보다", "동안"], "-기 때문에 = because."), F("비 ___ 길이 많이 막혀요. (because of)", "때문에", ["보다", "동안"], "Noun + 때문에 = because of."), F("뉴욕이 몬트레이___ 더 큽니다. (than)", "보다", ["때문에", "에서"], "~보다 더 = more than."),
           F("자동차가 비행기보다 ___. (slow)", "느립니다", ["빠릅니다", "비쌉니다"], "느리다 = to be slow."), F("저는 이틀 동안 뉴욕에 사는 친구를 ___. (visited)", "방문했어요", ["빌렸어요", "냈어요"], "방문하다 = to visit."), F("제 동생은 한 살인데 아주 ___. (cute)", "귀엽습니다", ["불편합니다", "복잡합니다"], "귀엽다 = to be cute."),
           F("백일 번 고속도로로 가면 더 ___. (fast)", "빠릅니다", ["느립니다", "복잡합니다"], "빠르다 = to be fast.")]
        + [read_q("갈아타다"), read_q("복잡하다"), read_q("신호등"), read_q("정류장"), read_q("때문에")]
    ),
)

UNIT = unit("Semester 1 · Unit 3 · Chapter 10: On the Way to Los Angeles (로스앤젤레스 가는 길에)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])
