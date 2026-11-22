"""Unit 21: KBC Semester 1, Unit 4, Chapter 14 - Public Transportation in Korea (한국의 대중 교통).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 4, Student's Edition (2022).
Audio, video clips, photos, maps, signs, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _B_IRR, _base_ao

_DG = "공일이삼사오육칠팔구"


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


def _g4(n):
    out = ""
    for val, unit in ((1000, "천"), (100, "백"), (10, "십")):
        d, n = divmod(n, val)
        if d:
            out += ("" if d == 1 else _DG[d]) + unit
    return out + (_DG[n] if n else "")


def _kn(n):
    """Sino-Korean number with four-digit groups: 9500 -> 구천오백, 130000 -> 십삼만"""
    if n == 0:
        return "영"
    parts = []
    for name, val in (("억", 10 ** 8), ("만", 10 ** 4)):
        g, n = divmod(n, val)
        if g:
            parts.append(("" if (g == 1 and name == "만") else _g4(g)) + name)
    if n:
        parts.append(_g4(n))
    return " ".join(parts)


def _won(n):
    return f"{_kn(n)} 원"


def _last(w):
    return _K.decompose(stem(w)[-1])[2]


# ---- the core vocabulary of Chapter 14 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_PT = [
    ("공항철도", "(空港鐵道) airport railroad express", "인천공항에서 공항철도를 타고 김포공항까지 가세요."),
    ("내리다", "to get off", "롯데백화점에 가려면 다음 역에서 내리세요."),
    ("~대", "(臺) counter for electronics/vehicles", "지난 주말에 텔레비전을 한 대 샀습니다."),
    ("대중교통", "(大衆交通) public transportation", "지하철, 버스, 택시는 대중교통입니다."),
    ("요금", "(料金) fare", "집에서 학교까지 버스 요금이 천 원입니다."),
    ("운행", "(運行) operation (~하다/되다: to operate/to be operated)", "공항 버스 운행 시간이 어떻게 됩니까?"),
    ("전철", "(電鐵) a subway", "백화점이 전철역에서 가까워요?"),
    ("편리", "(便利) convenience (~하다: to be convenient)", "집 앞에 슈퍼마켓이 있어서 편리합니다."),
    ("표지판", "(標識板) a sign; a post", "운전할 때는 교통 표지판을 잘 보세요."),
    ("~ 호선", "(號線) (subway) line", "공항에 가려면 지하철 몇 호선을 타야 합니까?"),
]
_CV_SUB = [
    ("계단", "(階段) stairs", "에스컬레이터가 운행되지 않습니다. 계단을 이용하십시오."),
    ("금연", "(禁煙) no smoking; “prohibited smoking”", "지하철 안에서는 금연입니다."),
    ("나가다", "to go out", "오 번 출구로 나가세요."),
    ("매표소", "(賣票所) a ticket booth; “ticket purchasing place”", "표를 사러 매표소에 갔습니다."),
    ("~ 방면", "(方面) direction, bound", "여기서 이 호선 충무로 방면으로 다시 갈아타세요."),
    ("승강장", "(昇降場) a platform", "승강장에 줄을 서서 전동차를 탑니다."),
    ("승차권", "(乘車券) a boarding ticket", "저기 매표소에서 승차권을 사십시오."),
    ("자동판매기", "(自動販賣機) a vending machine; “automatic selling machine”", "자동판매기에서 승차권을 샀습니다."),
    ("전동차", "(電動車) a subway train; “a car that moves on electricity”", "지하철 역에서 전동차를 기다리고 있습니다."),
    ("정거장", "(停車場) a station", "여기서 세 정거장만 더 가면 강남역입니다."),
    ("줄", "a line; a rope", "사람이 많아서 정류장에 줄이 깁니다."),
    ("출입금지", "(出入禁止) no trespassing; no entry; (entering) is prohibited", "여자 기숙사는 남학생 출입금지입니다."),
    ("~행", "(行) bound", "이번 역에서 잠실행 열차를 타시면 됩니다."),
]
_CV_TRF = [
    ("보행자", "(步行者) a pedestrian", "보행자에게 길을 양보하세요."),
    ("승용차", "(乘用車) a passenger car", "승용차에는 보통 다섯 명까지 탈 수 있습니다."),
    ("양보", "(讓步) yield (~하다: to yield)", "할머니에게 자리를 양보하세요."),
    ("(운전)기사", "(技士) a driver; a vehicle operator; “a (driving) engineer”", "한국의 택시 운전기사들은 아주 친절합니다."),
    ("일방통행", "(一方通行) one-way traffic", "그 길은 일방통행이기 때문에 들어갈 수 없습니다."),
    ("전용", "(專用) exclusive use", "이 길은 자전거 전용 도로입니다."),
    ("차도 / 차로", "(車路 / 車道) a (car) lane", "버스를 타면 버스전용차로로 가서 더 빨리 가요."),
    ("횡단보도", "(橫斷步道) a pedestrian crossing", "길을 건널 때는 횡단보도를 이용하세요."),
]
_CV_LOAN = [
    ("리무진", "a limousine", "졸업 파티에 갈 때 리무진을 탑니다."),
    ("엘리베이터", "an elevator", "엘리베이터를 타고 지하 일 층으로 내려가세요."),
    ("택시", "a taxi cab", "서울에는 택시와 버스가 많습니다."),
    ("터널", "a tunnel", "몬트레이에서 피지로 가는 길에 터널이 있어요."),
]
_CV_OTH = [
    ("건너다", "to cross (a road or line)", "도서관에 가려면 길을 건너가세요."),
    ("걷다", "to walk", "저는 매일 아침 집에서 학교까지 걸어갑니다."),
    ("고등학교", "a high school", "제 동생은 고등학교에 다닙니다."),
    ("-고 있다 / 계시다", "to be -ing (계시다 is marked ↑, honorific, in the book)", "지금 충무로행 열차가 들어오고 있습니다."),
    ("금지", "(禁止) prohibition (~하다/되다: to forbid/to be forbidden)", "저쪽에 출입금지 표지판이 있습니다."),
    ("-기(를) 바라다", "please …; it is desirable that; it is advised that; I wish you to …", "시청으로 가실 손님은 이번 역에서 이 호선으로 갈아타시기 바랍니다."),
    ("나다", "to occur; to break out", "큰 도시에서는 교통사고가 많이 납니다."),
    ("내려가다", "to go down; to descend", "지하 일 층으로 내려가시면 식당이 있습니다."),
    ("대학교", "(大學校) a college; a university", "제 동생은 내년에 대학교에 갑니다."),
    ("들어오다", "to enter", "지금 전동차가 역으로 들어오고 있습니다."),
    ("따라가다", "to follow", "길을 잘 모르시면 저 분을 따라가세요."),
    ("~마다", "each; every; per", "지하철이 오 분마다 한 대씩 옵니다."),
    ("사고", "(事故) an accident (~나다: [for an accident] to occur)", "교통사고 때문에 차가 막힙니다."),
    ("승강기", "(昇降機) an elevator", "이 건물에 승강기가 어디 있습니까?"),
    ("시청", "(市廳) a city hall", "서울시청은 서울 시내에 있습니다."),
    ("~씩", "each; respectively", "한 사람당 물 한 병씩 주세요."),
    ("안내소", "(案內所) an information desk", "우리 안내소에 가서 물어 봅시다."),
    ("~원", "won; Korean currency unit", "백 달러를 한국 돈으로 환전해서 십삼만 원을 받았습니다."),
    ("-(으)니까", "because", "길이 막히니까 지하철을 타고 갈까요?"),
    ("지하도", "(地下道) an underground passage; an underpass", "지하철을 타려면 지하도로 내려가세요."),
    ("출근", "(出勤) going to work (~하다: to go to work)", "서울은 출근 시간에 차가 늘 막힙니다."),
    ("퇴근", "(退勤) leaving one’s work; punching out (~하다: to leave one’s work)", "우리 아버지는 저녁 여섯 시에 퇴근하십니다."),
]
_CV_SINO = [
    ("금", "(禁) forbid; abstain; ban", "금연, 출입 금지, 통행 금지"),
    ("도", "(道) a road; a way", "지하도, 고속도로, 차도"),
    ("차", "(車) a vehicle on wheels", "승용차, 자동차, 기차, 열차"),
]
_ALL = {r[0]: r for r in _CV_PT + _CV_SUB + _CV_TRF + _CV_LOAN + _CV_OTH}


def _en(word):
    t = _re.sub(r"^\([^)]*(\([^)]*\))?[^)]*\) ", "", _ALL[word][1])
    return _clean(_re.sub(r" \(~[^)]*\)", "", t))


def _pairs(words):
    return [(w, _en(w)) for w in words]


def _rows(words):
    return [(w, _ALL[w][1]) for w in words]


# ================================================================== Vocabulary builder: etymology
_ETY = [("승무원", "乘 승 (to ride) + 務 무 (work) + 員 원 (a member/personnel)", "a crew member; a flight, train, bus or ship attendant"),
        ("승차", "乘 승 (to ride) + 車 차 (a vehicle on wheels)", "to get on a vehicle"),
        ("사무실", "事 사 (matter) + 務 무 (work) + 室 실 (a room)", "an office"),
        ("공무원", "公 공 (public) + 務 무 (work) + 員 원 (a member)", "a public servant"),
        ("병원", "病 병 (sickness) + 院 원 (a house)", "a hospital")]
L1 = lesson(
    "Ch 14 · Vocabulary builder: study the origins of words",
    "한국의 대중 교통 · 승무원 · 승차 · 사무실 · 공무원 · 병원 · 한자 (Hanja)",
    requires=[],
    cards=[
        card("What Chapter 14 teaches (한국의 대중 교통)",
             "Chapter 14, “Public Transportation in Korea”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: ask for information about public transportation in Korea; read subway line maps and signs to get around using the subway system; comprehend and respond to public announcements in the subway; read traffic signs; ask for and give directions; and talk about public transportation in Korea.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -고 있다, which is used to express an action in progress; -기 바라다, which is used to give public instruction (please …); the conjunctive ending -(으)니까 (because); ㄷ irregular verbs; and the Sino-Korean syllables 차 (車), 금 (禁), and 도 (道)."),
        card("Strategy: study the origins of words (etymology)",
             "Sino-Korean words make up about 60% of the Korean vocabulary (H. Sohn, The Korean Language, Cambridge University Press 2001). Therefore, knowledge of Sino-Korean roots is a must for systematically expanding and retaining Korean words. Recall the Sino-Korean word 승무원 (乘務員), meaning a crew member or flight/train/bus/ship attendant, which we learned in Chapter 13. Each individual syllable of the word has a meaning: 승 (乘) means to ride, 무 (務) work, and 원 (員) a member. Once we get to know the meanings of these individual syllables, it is not difficult to figure out the meanings of newly encountered words that contain one of the syllables. For example, when we encounter the words 승차, 사무실 and 공무원, we can figure out their meanings relatively easily.",
             tables=[table(["Word", "Syllables", "Meaning"], [[a, b, c] for a, b, c in _ETY[:4]], say=[0])]),
        card("The same sound, different Chinese characters",
             "Depending on what Chinese character the syllable comes from, however, the syllable can be interpreted differently. For example, 원 in 공무원 (a public servant) or 승무원 (a crew member) is interpreted as a member because it comes from the Chinese character 員 (원), whereas 원 in 병원 (a hospital) is interpreted as a house because it comes from the Chinese character 院 (원). Notice that both are spelled the same in Korean, although their Chinese characters are different and thus their meanings are different. This is why the book provides Hanja (Chinese characters) next to every Sino-Korean core vocabulary item in the Core Vocabulary sections from Unit 4 on. (The 病 in 병원 and the 室 in 사무실 are mine; the book gives the Hanja only for 員 and 院.)",
             tables=[table(["Word", "Syllables", "Meaning"], [[a, b, c] for a, b, c in [_ETY[3], _ETY[0], _ETY[4]]], say=[0])]),
        card("Activities left out",
             "The vocabulary slide show, the two SMART Board activities and Activity 3 (a Monopoly game, 모노폴리 게임) are picture, game or computer activities."),
    ],
    exercises=uniq(
        [M(f"What does {a} mean?", c, [x for _, _, x in _ETY if x != c][:3], f"{a}: {b}.") for a, b, c in _ETY]
        + [M(f"Which word means “{c}”?", a, [x for x, _, _ in _ETY if x != a][:3], f"{a}: {b}.") for a, b, c in _ETY]
        + [M("What does the Sino-Korean syllable 승 (乘) mean?", "to ride", ["work", "a member", "a room"], "승무원, 승차."), M("What does the Sino-Korean syllable 무 (務) mean?", "work", ["to ride", "a member", "a room"], "승무원, 사무실, 공무원."),
           M("What does the Sino-Korean syllable 원 (員) mean?", "a member; personnel", ["a house", "work", "to ride"], "승무원, 공무원."), M("What does the Sino-Korean syllable 원 (院) mean in 병원?", "a house; an institution", ["a member", "work", "to ride"], "병원 = hospital."),
           M("What does the Sino-Korean syllable 차 (車) mean?", "a vehicle on wheels", ["a room", "to ride", "work"], "승차, 자동차, 기차."), M("What does the Sino-Korean syllable 공 (公) mean?", "public", ["work", "a member", "a room"], "공무원 = public + work + member."),
           M("About how much of the Korean vocabulary is Sino-Korean?", "About 60%", ["About 10%", "About 30%", "About 95%"], "Sino-Korean words make up about 60% of the Korean vocabulary."), M("Why does the book give Hanja next to the Sino-Korean core vocabulary?", "The same Korean spelling can come from different characters with different meanings", ["Because Koreans write Hanja every day", "Because Hanja are easier than Hangul", "Because the book has no English"], "원 in 공무원 and 원 in 병원 are spelled the same but come from 員 and 院."),
           M("Which words contain the same syllable 원 meaning “a member”?", "승무원 and 공무원", ["승무원 and 병원", "공무원 and 병원", "사무실 and 병원"], "승무원 and 공무원 contain 員."), M("Which word contains the same syllable 무 (work) as 승무원?", "사무실", ["병원", "자동차", "기차"], "사무실 = matter + work + room."),
           read_q("승무원"), read_q("공무원"), read_q("사무실"), read_q("병원"), read_q("승차")]
    ),
)

# ================================================================== Topic A
_A_DLG = [
    ("앤더슨 상병", "저기요. 시청 앞 조선호텔까지 가려면 어떻게 가요?", "Excuse me. How do I get to the Chosun Hotel in front of City Hall?"),
    ("안내소 직원", "대중교통을 이용하시면 편리합니다. 공항 리무진 버스, 택시, 그리고 공항철도가 있어요.", "If you use public transportation, it is convenient. There are the airport limousine bus, taxis, and the airport railroad."),
    ("앤더슨 상병", "음… 리무진 버스는 얼마나 자주 와요?", "Hmm… how often does the limousine bus come?"),
    ("안내소 직원", "삼십 분마다 한 대씩 운행됩니다.", "One runs every thirty minutes."),
    ("앤더슨 상병", "그럼, 공항철도는 어때요?", "Then how about the airport railroad?"),
    ("안내소 직원", "열차가 삼 분에 한 대씩 옵니다.", "A train comes every three minutes."),
    ("앤더슨 상병", "그래요? 공항철도 열차는 어디에서 탑니까?", "Is that so? Where do I get on the airport railroad train?"),
    ("안내소 직원", "네, 지하 일 층에서 타실 수 있습니다.", "Yes, you can get on at the first basement floor."),
    ("앤더슨 상병", "거기까지 어떻게 가요?", "How do I get there?"),
    ("안내소 직원", "저기 승강기로 지하까지 내려가세요. 승강기에서 내리면 바로 공항철도 표지판이 보입니다. 그 표지판을 따라가세요.", "Go down to the basement with that elevator over there. When you get off the elevator, you will see the airport railroad sign right away. Follow that sign."),
    ("앤더슨 상병", "네, 감사합니다.", "Yes, thank you."),
]
_A_WORDS = ["공항철도", "내려가다", "내리다", "~대", "대중교통", "따라가다", "리무진", "~마다", "승강기", "엘리베이터", "시청", "~씩", "안내소", "요금", "운행", "~원", "택시", "편리", "표지판"]
_A_PH = [("저기요", "Excuse me. (to get the attention of someone you do not know; “over there”)"), ("여기요", "Excuse me. (“over here”)")]
L2 = lesson(
    "Ch 14 · Topic A: At the airport information desk",
    "공항 안내소에서 · 대중교통 · 공항철도 · 리무진 버스 · 삼십 분마다 한 대씩",
    requires=[],
    cards=[
        card("Topic A: At the airport information desk",
             "SPC Anderson is asking for transportation information at the Incheon International Airport information desk. (The English is mine; the book writes 30분마다, 3분에 and 지하 1층, spelled out here. Footnote of the book: 저기요 (over there) and 여기요 (over here) are commonly used to get the attention of someone you do not know. The book spells the counter 씩 with a space: 한 대 씩.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter). The book lists 승강기 / 엘리베이터 together, and 운행(하다 / 되다) and 편리하다 with their verb endings; they are split and shortened here.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Getting someone’s attention",
             "The two expressions of the book’s footnote:",
             tables=[ktable(_A_PH)]),
        card("Activities left out",
             "The SMART Board activities and Follow-up 1 (listening to three short conversations to find the form of transportation each passenger took to Incheon International Airport: a. 공항철도, b. 공항 리무진 버스, c. 택시) are game or audio activities. Follow-up 2 is in the next lesson. The Useful Links (the Incheon airport traffic guide and the airport railroad) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not w.startswith("~")]))
        + _tr(_strip(_A_DLG)) + _tr(_A_PH)
        + [M("Where does SPC Anderson want to go?", "The Chosun Hotel in front of City Hall", ["Incheon airport", "Seoul Station", "Lotte Hotel"], "시청 앞 조선호텔까지 가려면."), M("Which means of transportation does the employee list?", "The airport limousine bus, taxis and the airport railroad", ["Subway, bus and bicycle", "Taxi only", "Train and ferry"], "공항 리무진 버스, 택시, 그리고 공항철도."),
           M("How often does the limousine bus run?", "Every thirty minutes", ["Every three minutes", "Every hour", "Every ten minutes"], "삼십 분마다 한 대씩."), M("How often does the airport railroad train come?", "Every three minutes", ["Every thirty minutes", "Every hour", "Every ten minutes"], "열차가 삼 분에 한 대씩 옵니다."),
           M("Where can he get the airport railroad train?", "On the first basement floor", ["On the second floor", "Outside the terminal", "At the bus stop"], "지하 일 층에서 타실 수 있습니다."), M("How does he get to the airport railroad platform?", "By the elevator down to the basement, then following the sign", ["By bus", "By taxi", "By walking outside"], "승강기로 지하까지 내려가세요."),
           M("What should he follow after getting off the elevator?", "The airport railroad sign", ["The taxi driver", "The limousine bus", "A guide"], "그 표지판을 따라가세요."), M("Which word means “public transportation”?", "대중교통", ["운행", "표지판", "요금"], "대중교통 = public transportation."),
           M("Which word means “a sign”?", "표지판", ["요금", "안내소", "시청"], "표지판 = a sign; a post."), M("Which word means “an information desk”?", "안내소", ["표지판", "시청", "택시"], "안내소 = an information desk."),
           F("대중교통을 이용하시면 ___합니다. (convenient)", "편리", ["편안", "복잡"], "편리하다 = to be convenient."), F("삼십 분___ 한 대씩 운행됩니다. (every)", "마다", ["씩", "에서"], "~마다 = each; every."),
           F("열차가 삼 분에 한 대___ 옵니다. (each)", "씩", ["마다", "도"], "~씩 = each; respectively."), F("저기 ___로 지하까지 내려가세요. (elevator)", "승강기", ["표지판", "요금"], "승강기 = an elevator."),
           F("그 표지판을 ___. (Follow)", "따라가세요", ["내리세요", "올라가세요"], "따라가다 = to follow."), F("승강기에서 ___ 바로 공항철도 표지판이 보입니다. (when you get off)", "내리면", ["타면", "가면"], "내리다 + -(으)면 = 내리면."),
           read_q("공항철도"), read_q("대중교통"), read_q("리무진 버스"), read_q("승강기"), read_q("안내소")]
    ),
)

# ================================================================== Activities A
_PORTAL = [
    ("제목: 서울역에서 인천공항까지", "Title: From Seoul Station to Incheon Airport"),
    ("서울역에서 인천공항까지 이용할 수 있는 대중교통은 여러 가지가 있습니다.", "There are several kinds of public transportation you can use from Seoul Station to Incheon Airport."),
    ("빨리 가고 싶으면 공항철도를 이용하세요.", "If you want to go fast, use the airport railroad."),
    ("서울역에서 인천공항까지 사십삼 분 만에 도착할 수 있어요.", "You can arrive from Seoul Station to Incheon Airport in forty-three minutes."),
    ("그런데 공항역에서 출국장까지 멀어서 많이 걸어야 해요.", "But it is far from the airport station to the departure hall, so you have to walk a lot."),
    (f"공항철도 요금은 {_won(9500)}입니다.", "The airport railroad fare is 9,500 won."),
    ("짐이 많으면 서울역에서 공항 리무진 버스를 타세요.", "If you have a lot of baggage, take the airport limousine bus from Seoul Station."),
    ("한 번에 공항까지 갈 수 있어서 편리해요.", "It is convenient because you can go to the airport in one go."),
    (f"요금은 {_won(16000)}이에요.", "The fare is 16,000 won."),
    ("그렇지만, 보통 이십 분마다 한 대씩 운행하기 때문에 좀 기다려야 합니다.", "However, a bus usually runs only every twenty minutes, so you have to wait a little."),
    ("그리고 택시는 편하지만 요금이 비쌉니다.", "And a taxi is comfortable, but the fare is expensive."),
    (f"{_kn(80000)} 원 정도 나올 거예요.", "It will come to about 80,000 won."),
]
_LOTTE = [
    ("답변", "Reply"),
    ("저희 롯데호텔을 이용해 주셔서 감사합니다.", "Thank you for using our Lotte Hotel."),
    ("인천공항에서 저희 호텔로 오시는 방법은 여러 가지가 있습니다.", "There are several ways to come from Incheon Airport to our hotel."),
    ("먼저 인천공항에서 택시를 이용하실 수 있습니다.", "First, you can use a taxi from Incheon Airport."),
    (f"그런데 요금이 {_won(130000)}으로 조금 비쌉니다.", "But the fare is a little expensive at 130,000 won."),
    ("또 인천공항에서 케이에이엘 리무진을 타실 수 있습니다.", "Also, you can take the KAL limousine from Incheon Airport."),
    ("케이에이엘 리무진은 공항 케이에이엘 정류장에서 타실 수 있고 삼십 분마다 출발합니다.", "You can take the KAL limousine at the airport KAL bus stop, and it leaves every thirty minutes."),
    ("교통이 복잡하지 않으면 호텔까지 보통 한 시간 이십 분 정도 걸립니다.", "If the traffic is not congested, it usually takes about one hour and twenty minutes to the hotel."),
    (f"요금은 {_won(18000)} 정도입니다.", "The fare is about 18,000 won."),
    ("승차권은 인천공항에 있는 케이에이엘 안내 데스크에서 사실 수 있습니다.", "You can buy the ticket at the KAL information desk at Incheon Airport."),
    ("그리고 공항철도도 이용하실 수 있습니다.", "And you can also use the airport railroad."),
    ("먼저 인천공항에서 김포공항까지 공항철도를 타고 오신 후 지하철로 갈아타시면 됩니다.", "First, take the airport railroad from Incheon Airport to Gimpo Airport and then transfer to the subway."),
    ("공항철도는 십 분마다 한 대씩 운행합니다.", "The airport railroad runs one train every ten minutes."),
    ("호텔까지 한 시간쯤 걸립니다.", "It takes about an hour to the hotel."),
    (f"요금은 {_won(7000)} 정도입니다.", "The fare is about 7,000 won."),
]
_ACT_MODEL = [("인천공항에서 택시를 타고 시청에 가고 싶어요.", "I want to go to City Hall from Incheon Airport by taxi."), (f"시청까지 요금은 {_won(55000)}이고 약 한 시간 정도 걸립니다.", "The fare to City Hall is 55,000 won and it takes about an hour."), ("택시는 비싸지만 편합니다.", "A taxi is expensive but comfortable.")]
_ACT_W = [("방법", "a method; how to"), ("정류장", "a bus stop (mine)"), ("갈아타다", "to transfer (mine)"), ("출국장", "a departure hall (mine)"), ("교통", "traffic (mine)"), ("복잡하다", "to be complicated; to be congested (mine)"), ("비싸다", "to be expensive (mine)"), ("이용하다", "to use (mine)")]
L3 = lesson(
    "Ch 14 · Activities A: getting from the airport to Seoul",
    "서울역에서 인천공항까지 · 롯데호텔 답변 · 요금 · 공항철도와 리무진 버스",
    requires=[],
    cards=[
        card("Topic A, Follow-up 2 (Reading): from Seoul Station to Incheon Airport",
             "The book shows information from an internet portal website about the forms of transportation one can take to Incheon International Airport from Seoul Station and asks you to fill in a table in English (the strong points and weak points of each). The text is the book’s; the numbers are spelled out in Hangul and the English is mine.",
             examples=passage(_PORTAL)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Form of transportation", "Strong points", "Weak points"], [["Airport railroad", "Fast: 43 minutes from Seoul Station to Incheon Airport; fare 9,500 won", "A long walk from the airport station to the departure hall"],
                                                                                         ["Airport limousine bus", "Convenient, one ride to the airport (good for a lot of baggage); fare 16,000 won", "Runs only about every 20 minutes, so you have to wait"],
                                                                                         ["Taxi", "Comfortable", "Expensive (about 80,000 won)"]])]),
        card("Activity 2 (Reading): the Lotte Hotel’s e-mail reply",
             "PFC Anderson is going to stay at the Lotte Hotel in Seoul. He e-mailed the hotel to ask about public transportation from Incheon International Airport to the hotel. The book asks you to fill in a table in English (the form of transportation, the interval of operation, the fare and the length of the trip). The text is the book’s with the numbers spelled out and KAL written 케이에이엘; the English is mine. The book’s note: 방법 means “a method; how to”.",
             examples=passage(_LOTTE)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Form of transportation", "Interval of operation", "Fare", "Length of trip"], [["Taxi", "—", "130,000 won", "—"], ["KAL limousine", "Every 30 minutes", "About 18,000 won", "About 1 hour 20 minutes if the traffic is not congested"], ["Airport railroad (transfer to the subway at Gimpo Airport)", "Every 10 minutes", "About 7,000 won", "About 1 hour"]])]),
        card("Activity 3 (Speaking): a model report",
             "You and a friend decide which way to go from Incheon International Airport to Seoul (airport railroad or limousine service), using a sheet with missing information, and report your choice and your reasons to the class. The book’s model (the English is mine; 55,000원 is spelled out):",
             examples=passage(_ACT_MODEL)),
        card("Words in the two texts",
             "The book glosses only 방법; the other meanings are mine.",
             tables=[ktable(_ACT_W)]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and listening to three announcements about public transportation from Incheon airport to Seoul), the information sheets with missing information for two partners of Activity 3 and the Useful Links (the Incheon airport traffic guide and the airport railroad) are audio, game, partner or website activities."),
    ],
    exercises=uniq(
        _tr(_PORTAL[1:] + _LOTTE[1:] + _ACT_MODEL + _ACT_W)
        + [M("Which transportation is the fastest from Seoul Station to the airport?", "The airport railroad", ["The limousine bus", "The taxi", "The KAL limousine"], "공항철도 = 43 minutes."), M("What is a weak point of the airport railroad in the portal text?", "A long walk from the station to the departure hall", ["The fare is expensive", "It runs rarely", "It does not go to the airport"], "공항역에서 출국장까지 멀어서."),
           M("When is the limousine bus recommended?", "When you have a lot of baggage", ["When you are in a hurry", "When you have little money", "When it rains"], "짐이 많으면 … 리무진 버스를 타세요."), M("How often does the limousine bus run in the portal text?", "About every twenty minutes", ["Every three minutes", "Every hour", "Every ten minutes"], "이십 분마다 한 대씩."),
           M("Which transportation is the most expensive in the portal text?", "The taxi (about 80,000 won)", ["The airport railroad", "The limousine bus", "They cost the same"], "택시는 … 요금이 비쌉니다."), M("What does the Lotte Hotel say about the taxi?", "The fare is 130,000 won, a little expensive", ["It is the cheapest way", "It takes an hour", "It leaves every 30 minutes"], "요금이 십삼만 원으로 조금 비쌉니다."),
           M("Where can you buy the KAL limousine ticket?", "At the KAL information desk at Incheon Airport", ["On the bus", "At the hotel", "At Gimpo Airport"], "케이에이엘 안내 데스크에서 사실 수 있습니다."), M("How often does the KAL limousine leave?", "Every thirty minutes", ["Every ten minutes", "Every hour", "Every three minutes"], "삼십 분마다 출발합니다."),
           M("How long does the KAL limousine take if the traffic is not congested?", "About one hour and twenty minutes", ["About one hour", "About forty minutes", "About three hours"], "한 시간 이십 분 정도."), M("Where do you transfer to the subway on the airport railroad route?", "Gimpo Airport", ["Seoul Station", "Incheon Airport", "City Hall"], "김포공항까지 공항철도를 타고 오신 후 지하철로 갈아타시면."),
           M("How much is the airport railroad in the Lotte Hotel’s e-mail?", "About 7,000 won", ["About 18,000 won", "About 130,000 won", "About 9,500 won"], "요금은 칠천 원 정도입니다."), M("Why is the taxi chosen in the book’s model report?", "It is comfortable, although expensive", ["It is cheap", "It is fast", "It runs every ten minutes"], "택시는 비싸지만 편합니다."),
           F("빨리 가고 싶___ 공항철도를 이용하세요. (if you want)", "으면", ["면", "은데"], "싶다 ends in a consonant: 싶으면."), F("서울역에서 인천공항까지 사십삼 분 ___ 도착할 수 있어요. (in … minutes)", "만에", ["마다", "씩"], "~ 만에 = in (a time)."),
           F("요금은 구천오백 ___입니다. (won)", "원", ["대", "호선"], "~원 = won."), F("공항철도는 십 분___ 한 대씩 운행합니다. (every)", "마다", ["씩", "만에"], "~마다 = every."),
           F("지하철로 ___ 됩니다. (you should transfer)", "갈아타시면", ["내리시면", "타시면"], "갈아타다 = to transfer."), F("택시는 편하___ 요금이 비쌉니다. (but)", "지만", ["고", "니까"], "-지만 = but."),
           read_q("서울역에서 인천공항까지"), read_q("롯데호텔"), read_q("구천오백 원"), read_q("갈아타시면"), read_q("공항 리무진 버스")]
    ),
)

# ================================================================== Topic B
_B_DLG1 = [
    ("앤더슨 상병", "저, 실례합니다. 서울대학교 입구까지 어떻게 가요?", "Excuse me. How do I get to the entrance of Seoul National University?"),
    ("지하철 직원", "먼저 공항철도를 타고 김포공항역에서 내리세요. 거기서 광화문 방면으로 가는 지하철 오 호선으로 갈아타세요.", "First take the airport railroad and get off at Gimpo Airport Station. From there, transfer to the Line 5 subway that goes in the direction of Gwanghwamun."),
    ("앤더슨 상병", "그럼, 오 호선을 탄 후에는 어디서 내려요?", "Then, where do I get off after taking Line 5?"),
    ("지하철 직원", "영등포구청역에서 내려서 이 호선으로 갈아타세요.", "Get off at Yeongdeungpo-gu Office Station and transfer to Line 2."),
    ("앤더슨 상병", "그럼, 거기서 서울대학교 입구까지 얼마나 걸려요?", "Then how long does it take from there to the entrance of Seoul National University?"),
    ("지하철 직원", "영등포구청역에서 한 여덟 정거장만 더 가시면 됩니다.", "From Yeongdeungpo-gu Office Station you only need to go about eight more stations."),
    ("앤더슨 상병", "아, 네. 그런데 매표소는 어디에 있어요? 승차권을 사야 해요.", "Oh, I see. By the way, where is the ticket booth? I have to buy a ticket."),
    ("지하철 직원", "교통카드 필요하세요? 저기 자동판매기에서 사세요. 지금 줄이 길지 않네요.", "Do you need a transportation card? Buy it at the vending machine over there. The line isn’t long now."),
]
_B_ANN = [
    ("지금 시청행 열차가 들어오고 있습니다.", "A train bound for City Hall is entering the station now."),
    ("손님 여러분, 이 역은 전동차와 승강장 사이가 넓습니다.", "Passengers, at this station the gap between the train and the platform is wide."),
    ("타실 때 조심하시기 바랍니다.", "Please be careful when you get on."),
]
_B_WORDS = ["계단", "-고 있다 / 계시다", "고등학교", "-기(를) 바라다", "금연", "나가다", "대학교", "들어오다", "매표소", "~ 방면", "승강장", "승차권", "자동판매기", "전동차", "전철", "정거장", "줄", "출입금지", "~행", "~ 호선"]
_JRN = [
    (f"{month_ko(2)} {day_ko(1)}", "February 1"),
    ("날씨: 흐림", "Weather: cloudy"),
    ("명동에 가려고 아침 일찍 호텔에서 나왔습니다.", "I left the hotel early in the morning to go to Myeongdong."),
    ("그런데 시내버스 정류장에 사람이 너무 많았습니다.", "But there were too many people at the city bus stop."),
    ("그래서 지하철을 타고 갔습니다.", "So I went by subway."),
    ("매표소에 줄이 너무 길어서 자동판매기에서 표를 샀습니다.", "The line at the ticket booth was too long, so I bought a ticket at the vending machine."),
    ("승강장에서 오 분쯤 기다린 후에 일 호선 지하철을 탔습니다.", "After waiting about five minutes on the platform, I took the Line 1 subway."),
    ("그런데 빈 자리가 없어서 서울역까지 서서 갔습니다.", "But there was no empty seat, so I stood all the way to Seoul Station."),
    ("서울역에서 내려서 사 호선으로 갈아탔습니다.", "I got off at Seoul Station and transferred to Line 4."),
    ("두 정거장 후에 명동역에서 내렸습니다.", "Two stations later I got off at Myeongdong Station."),
    ("명동까지 한 시간이 걸렸습니다.", "It took an hour to get to Myeongdong."),
    ("지하철을 오래 타서 조금 피곤했습니다.", "I rode the subway for a long time, so I was a little tired."),
    ("그렇지만 시내에서 구경도 많이 하고 쇼핑도 해서 재미있었습니다.", "But I did a lot of sightseeing and shopping downtown, so it was fun."),
]
_SINO_CHA = [("자동차", "an automobile; “self-moving car”"), ("전동차", "a subway; an electric car; “electricity moving car”"), ("기차", "a train; “steam car”"), ("무개차", "a convertible; “no cover car”")]
_SINO_CHA_G = [("차도", "a road for cars; a roadway (mine)"), ("차창", "a car window (mine)"), ("차선", "a traffic lane (mine)"), ("소형차", "a small car (mine)"), ("차비", "a fare; money for transportation (mine)")]
L4 = lesson(
    "Ch 14 · Topic B: At the subway station",
    "지하철역에서 · 공항철도 · 오 호선으로 갈아타세요 · 줄이 길지 않네요 · 차 (車) · 지하철도",
    requires=[],
    cards=[
        card("Topic B, part I: at the ticket booth",
             "SPC Anderson is talking to a subway employee at a ticket booth in the Incheon International Airport Railroad station. (The English is mine; the book writes 5호선 and 2호선, spelled out as 오 호선 and 이 호선.)",
             examples=dlg(_B_DLG1)),
        card("Topic B, part II: an announcement",
             "An announcement at a platform in the Gimpo Airport subway station. (The English is mine.)",
             examples=passage(_B_ANN)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter).",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Follow-up 2 (Reading): Sarah Kim’s journal",
             "Sarah Kim’s journal entry is about her experience of taking the subway in Seoul for the first time. The book asks you to fill in a table in English (destination, transportation used, how the ticket was purchased, route and time to the destination). The text is the book’s with the numbers spelled out; the English is mine.",
             examples=passage(_JRN)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer"], [["Destination", "Myeongdong"], ["Transportation used by Sarah Kim", "The subway (the city bus stop was too crowded)"], ["How the ticket was purchased", "From a vending machine (the line at the ticket booth was too long)"],
                                                    ["Route to the destination", "Line 1 to Seoul Station, then transfer to Line 4 and ride two stations to Myeongdong Station; she stood all the way to Seoul Station"], ["Time to the destination", "One hour"]])]),
        card("Sino-Korean in use: 차 (車)",
             "The Chinese character 車 of the syllable depicts the shape of a cart seen from above: the two parallel horizontal lines are wheels and the vertical line is the axle, which carries the body (box) of the cart. Thus the meaning of this syllable is a cart, car, or vehicle on wheel(s), as in 자동차 (an automobile; “self-moving car”), 전동차 (a subway; an electric car; “electricity moving car”), 기차 (a train; “steam car”), 무개차 (a convertible; “no cover car”), etc. The book asks you to guess the meaning of 차도, 차창, 차선, 소형차 and 차비; my answers are in the second table.",
             tables=[ktable(_SINO_CHA), ktable(_SINO_CHA_G)]),
        card("North Korea report",
             "The subway is called 지하철도 (underground railroad) in North Korea. Pyongyang Metro is an important part of the transportation infrastructure in the capital of North Korea. It was constructed with close attention to security and was first opened in September 1973. It is connected to secret underground military facilities; as a result, the system can serve as a bunker. However, relatively little is known about the Metro outside the country, as few visitors are able to investigate the system.",
             tables=[ktable([("지하철도", "the subway in North Korea; “underground railroad”"), ("지하철", "the subway in South Korea (mine)")])]),
        card("Activities left out",
             "The SMART Board activities, Follow-up 1 (listening to four announcements for subway passengers to circle the most appropriate answer: which line to transfer to for the Chamsil area; the next stop; what passengers should do; what is announced) are audio or game activities, and the Useful Link (Seoul Metro) is a website. The blanks in the book’s dialog are underlined words with notes; the dialog is given here complete."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("~", "-"))]))
        + _tr(_strip(_B_DLG1) + _B_ANN + _JRN[1:] + _SINO_CHA + _SINO_CHA_G[:3])
        + [M("Where does SPC Anderson want to go?", "The entrance of Seoul National University", ["City Hall", "Myeongdong", "Gimpo Airport"], "서울대학교 입구까지 어떻게 가요?"), M("Where does the employee tell him to get off the airport railroad?", "Gimpo Airport Station", ["Seoul Station", "City Hall", "Yeongdeungpo-gu Office Station"], "김포공항역에서 내리세요."),
           M("Which line does he transfer to at Gimpo Airport?", "Line 5", ["Line 2", "Line 1", "Line 4"], "오 호선으로 갈아타세요."), M("Where does he transfer to Line 2?", "Yeongdeungpo-gu Office Station", ["Gimpo Airport Station", "Gwanghwamun", "Seoul Station"], "영등포구청역에서 내려서 이 호선으로 갈아타세요."),
           M("How many more stations does he need to go on Line 2?", "About eight", ["About two", "About eighteen", "About eighty"], "한 여덟 정거장만 더."), M("Where can he buy a ticket?", "At the vending machine", ["At the hotel", "On the train", "At the bus stop"], "저기 자동판매기에서 사세요."),
           M("Why does the employee suggest the vending machine?", "The line is not long now", ["The ticket booth is closed", "The machine is cheaper", "There is no ticket booth"], "지금 줄이 길지 않네요."), M("What does the platform announcement ask the passengers?", "To be careful when getting on", ["To get off the train", "To buy a ticket", "To wait outside"], "타실 때 조심하시기 바랍니다."),
           M("What is wide at that station?", "The gap between the train and the platform", ["The stairs", "The platform", "The ticket booth"], "전동차와 승강장 사이가 넓습니다."), M("Why did Sarah Kim take the subway?", "There were too many people at the city bus stop", ["The subway is cheaper", "She likes the subway", "It was raining"], "시내버스 정류장에 사람이 너무 많았습니다."),
           M("Why did she buy a ticket at the vending machine?", "The line at the ticket booth was too long", ["The booth was closed", "She had a card", "She liked machines"], "매표소에 줄이 너무 길어서."), M("How long did she wait on the platform?", "About five minutes", ["About fifteen minutes", "About an hour", "She did not wait"], "오 분쯤 기다린 후에."),
           M("Why did she stand to Seoul Station?", "There was no empty seat", ["She wanted to", "She was tired", "The train was empty"], "빈 자리가 없어서."), M("How long did the trip to Myeongdong take?", "One hour", ["Five minutes", "Two hours", "Thirty minutes"], "한 시간이 걸렸습니다."),
           M("What is the subway called in North Korea?", "지하철도", ["지하철", "전철", "전동차"], "지하철도 = “underground railroad”."), M("When did Pyongyang Metro first open?", "September 1973", ["September 1993", "March 1973", "September 1953"], "It was first opened in September 1973."),
           F("먼저 공항철도를 타고 김포공항역에서 ___. (get off)", "내리세요", ["타세요", "나가세요"], "내리다 = to get off."), F("오 호선으로 ___. (transfer)", "갈아타세요", ["내리세요", "나가세요"], "갈아타다 = to transfer."),
           F("자동판매기에서 ___ 사세요. (the ticket)", "승차권을", ["승강장을", "매표소를"], "승차권 = a boarding ticket."), F("영등포구청역에서 한 여덟 ___만 더 가시면 됩니다. (stations)", "정거장", ["승강장", "매표소"], "정거장 = a station."),
           F("지금 시청___ 열차가 들어오고 있습니다. (bound for)", "행", ["대", "원"], "~행 = bound."), F("승강장에서 오 분쯤 기다린 ___ 지하철을 탔습니다. (after)", "후에", ["전에", "동안"], "-(으)ㄴ 후에 = after."),
           read_q("전동차"), read_q("승강장"), read_q("매표소"), read_q("영등포구청역"), read_q("자동판매기")]
    ),
)

# ================================================================== Grammar A: -고 있다
_GI_V = [("먹다", "to eat"), ("자다", "to sleep"), ("보다", "to see; to watch"), ("하다", "to do"), ("읽다", "to read"), ("공부하다", "to study"), ("운동하다", "to exercise"), ("가다", "to go"), ("마시다", "to drink"), ("듣다", "to listen"), ("얘기하다", "to talk"), ("춤추다", "to dance"), ("기다리다", "to wait"), ("만나다", "to meet")]
_GI_EX = [
    ("지금 신문을 보고 있어요.", "I am reading the newspaper now."), ("지금 점심식사를 하고 있어요.", "I am having lunch now."), ("아버님이 신문을 보고 계십니다.", "Father is reading the newspaper."), ("선생님이 점심식사를 하고 계십니다.", "The teacher is having lunch."),
    ("어제 두 시에는 체육관에서 운동하고 있었어요.", "I was working out at the gym yesterday at 2 o’clock."), ("내일 두 시에는 체육관에서 운동하고 있을 거예요.", "I will be working out at the gym tomorrow at 2 o’clock."),
    ("철수야, 지금 뭐하고 있어?", "Chulsoo, what are you doing now?"), ("지금 저녁 먹고 있어.", "I am eating dinner now."), ("내가 어제 전화했을 때 왜 안 받았어요?", "Why didn’t you answer my call when I called you yesterday?"), ("아, 그때 샤워하고 있었어요.", "Oh, I was taking a shower at that time."),
    ("내일 아침 여덟 시에 운동하러 갑시다.", "Let’s go exercise tomorrow morning at 8:00 a.m."), ("못 가요. 전 그때, 시험보고 있을 거예요.", "I can’t. I will be taking a test then."),
]
_GI_FU = [("모두 기다리고 있어요.", "Everyone is waiting. (the students answer their teacher)", "기다리다"), ("어, 나 그때 공부하고 있었어.", "Oh, I was studying at that time. (Yeongsu, to a friend)", "공부하다"), ("할아버지 지금 거실에서 신문 읽고 계세요.", "Grandfather is reading the newspaper in the living room now. (honorific)", "읽다"), ("어, 그래? 그때 친구를 만나고 있었어.", "Oh, really? I was meeting a friend at that time.", "만나다")]
_GI_Q = [("A", "누가 달리기를 하고 있습니까?", "Who is running?"), ("B", "구승민 씨가 달리기를 하고 있습니다.", "Mr. Gu Seung-min is running.")]
_GI_MODEL = [("어제 열 시에 영화를 보고 있었어요.", "I was watching a movie at ten o’clock yesterday.")]


def _go(verb):
    """(-고 있습니다, -고 있어요, -고 있었어요, -고 있을 거예요, honorific -고 계세요)"""
    st = stem(verb)
    return st + "고 있습니다", st + "고 있어요", st + "고 있었어요", st + "고 있을 거예요", st + "고 계세요"


L5 = lesson(
    "Ch 14 · Grammar A: an action in progress with -고 있다",
    "보고 있어요 · 먹고 있어요 · 공부하고 있었어요 · 운동하고 있을 거예요 · 보고 계세요",
    requires=[],
    cards=[
        card("Expressing an action in progress",
             "In English we commonly use “to be -ing” to express an action in progress, as in “I am working” or “Thomas is driving”. In Korean we use -고 있다 (added to the stem of an action verb): 지금 신문을 보고 있어요 (I am reading the newspaper now); 지금 점심식사를 하고 있어요 (I am having lunch now).\n\n"
             "계시다 is the honorific form of 있다. Thus we can use -고 계시다 to describe an action being done by a person we have to show respect to: 아버님이 신문을 보고 계십니다 (Father is reading the newspaper); 선생님이 점심식사를 하고 계십니다 (The teacher is having lunch). -고 있었다 is used for a past progressive action and -고 있을 것이다 for a future progressive action.",
             tables=[table(["Condition", "Rule", "Example"], [["After the stem of an action verb", "add 고 있다", "먹다 → 먹고 있다; 자다 → 자고 있다"]], title="action verb stem + 고 있다")],
             examples=[D(a, b) for a, b in _GI_EX[:6]]),
        card("More examples",
             "The book’s further examples (the English is the book’s; the times 8:00 a.m. and 2 o’clock are spelled out).",
             examples=[D(a, b) for a, b in _GI_EX[6:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Dictionary form", "Meaning", "Is -ing (formal)", "Is -ing (informal)", "Was -ing", "Will be -ing", "Honorific"], [[v, m, *_go(v)] for v, m in _GI_V], say=[0, 2, 3, 4, 5, 6])]),
        card("Follow-up 1: a time word and a verb",
             "In the book Student A reads a time word (어제, 지금 or 내일) from one pot and Student B makes a sentence with a verb from the other pot (공부하다, 영화를 보다, 운동하다, 가다, 책을 읽다, 술을 마시다, 춤추다, 음악을 듣다, 먹다, 얘기하다, 자다) and -고 있다. The book’s model (the English is mine; the time “10시” is spelled out):",
             examples=[D(a, b) for a, b in _GI_MODEL]),
        card("Follow-up 2a: complete the sentences",
             "The book gives four short dialogs with a blank to fill in with -고 있다 and the verb in brackets, asking you to keep the right tense and honorific. The answers are mine.",
             tables=[table(["Answer", "Meaning (mine)", "Verb"], [list(r) for r in _GI_FU], say=[0, 2])]),
        card("Follow-up 5: who is doing what?",
             "In the book partners ask each other the name of the person in a picture by describing the activity with -고 있다. The book’s model (the English is mine):",
             examples=dlg(_GI_Q)),
        card("Activities left out",
             "Follow-up 2b (listening to four short conversations to identify the actions in progress and the tense) and the picture handouts of Follow-up 5 are audio or picture activities."),
    ],
    exercises=uniq(
        [M(f"Which means “am/is {m.split(';')[0].replace('to ', '', 1)}ing” in informal speech ({v})?", _go(v)[1], [_go(v)[2], _go(v)[3], informal(v)], f"{v} → {_go(v)[1]}.") for v, m in _GI_V]
        + [M(f"Which is the past progressive of {v}?", _go(v)[2], [_go(v)[1], _go(v)[3], past_forms(v)[1]], f"{v} → {_go(v)[2]}.") for v, m in _GI_V[:10]]
        + [M(f"Which is the future progressive of {v}?", _go(v)[3], [_go(v)[1], _go(v)[2], future_(v)[1]], f"{v} → {_go(v)[3]}.") for v, m in _GI_V[:8]]
        + _tr(_GI_EX + _GI_MODEL + _GI_Q[:0] + _strip(_GI_Q))
        + [F("아버님이 신문을 보___ 계십니다. (is reading)", "고", ["면", "서"], "-고 계시다 = is -ing (honorific)."), F("선생님이 점심식사를 하고 ___. (is having; honorific)", "계십니다", ["있습니다", "있어요"], "계시다 is the honorific of 있다."), F("지금 철수는 저녁을 먹고 ___. (is eating)", "있어요", ["있었어요", "있을 거예요"], "지금 = now: present progressive."),
           F("어제 두 시에는 체육관에서 운동하고 ___. (was)", "있었어요", ["있어요", "있을 거예요"], "어제 = yesterday: past progressive."), F("내일 두 시에는 체육관에서 운동하고 ___. (will be)", "있을 거예요", ["있어요", "있었어요"], "내일 = tomorrow: future progressive."), F("그때 샤워하고 ___. (I was)", "있었어요", ["있어요", "있을 거예요"], "그때 (that time, past): 있었어요."),
           F("할아버지 지금 거실에서 신문 읽고 ___. (is reading; honorific)", "계세요", ["있어요", "있었어요"], "Grandfather: 계세요."), F("모두 기다리___ 있어요. (are waiting)", "고", ["면", "서"], "기다리다 + 고 있다."),
           M("What does -고 있다 express?", "An action in progress", ["A condition", "A plan", "A reason"], "-고 있다 = is -ing."), M("What is the honorific form of 있다?", "계시다", ["드시다", "주무시다", "계세요다"], "계시다 = the honorific form of 있다."),
           M("Which ending expresses a past progressive action?", "-고 있었다", ["-고 있을 것이다", "-고 있다", "-고 계시다"], "-고 있었다 = was -ing."), M("Which ending expresses a future progressive action?", "-고 있을 것이다", ["-고 있었다", "-고 있다", "-고 있어서"], "-고 있을 것이다 = will be -ing."),
           read_q("보고 있어요"), read_q("먹고 있어요"), read_q("하고 계십니다"), read_q("운동하고 있었어요"), read_q("시험보고 있을 거예요")]
    ),
)

# ================================================================== Grammar B: -기(를) 바라다
def _gb(verb):
    """honorific public instruction: 이용하다 -> 이용하시기 바랍니다; ㄹ stems drop ㄹ before 시"""
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    if t == "ㄹ":
        st = st[:-1] + _K.compose(l, v, "")
        return st + "시기 바랍니다"
    return st + ("으시기 바랍니다" if t else "시기 바랍니다")


_GB_V = [("이용하다", "to use"), ("기다리다", "to wait"), ("서다", "to stand"), ("갈아타다", "to transfer"), ("사다", "to buy"), ("나가다", "to go out"), ("사용하다", "to use"), ("조심하다", "to be careful"), ("건강하다", "to be healthy"), ("앉다", "to sit"), ("내리다", "to get off"), ("타다", "to get on; to ride")]
_GB_EX = [
    ("에스컬레이터를 이용하시기를 바랍니다.", "Please use the escalator."), ("안전선에서 기다리시기를 바랍니다.", "Please wait at the safety line."), ("건강하시기를 바랍니다.", "I wish you to be healthy. / I hope you are healthy."),
    ("자동판매기를 사용하시기를 바랍니다.", "Please use the vending machines."), ("자동판매기를 사용하시기 바랍니다.", "Please use the vending machines. (the object marker is deleted)"), ("자동판매기를 사용하시길 바랍니다.", "Please use the vending machines. (-기를 contracted to -길)"),
]
_GB_FU = [("입구가 아주 복잡합니다. 손님들은 줄을 서시기 바랍니다.", "The entrance is very crowded. Customers, please stand in line.", "서다"), ("에스컬레이터가 운행되지 않습니다. 손님들은 계단을 이용하시기 바랍니다.", "The escalator is not running. Customers, please use the stairs.", "이용하다"),
          ("시청역으로 가실 분들은 이 역에서 갈아타시기 바랍니다.", "Those going to City Hall Station, please transfer at this station.", "갈아타다"), ("이 역은 자동판매기가 없습니다. 매표소에서 표를 사시기 바랍니다.", "This station has no vending machines. Please buy a ticket at the ticket booth.", "사다"),
          ("시청으로 가실 손님은 이 번 출구로 나가시기 바랍니다.", "Customers going to City Hall, please go out by exit number 2.", "나가다")]
L6 = lesson(
    "Ch 14 · Grammar B: public instructions with -기(를) 바라다",
    "이용하시기 바랍니다 · 기다리시기를 바랍니다 · 갈아타시기 바랍니다 · 건강하시기를 바랍니다",
    requires=[],
    cards=[
        card("Giving instructions using -기(를) 바라다",
             "-기(를) 바라다 literally means “(I) hope (you) to …” and we can say it to an individual to mean “I wish you to …” or “I hope that you …”, as in 건강하시기(를) 바랍니다 (“I wish you to be healthy” or “I hope you are healthy”). However, we often hear -기(를) 바라다 in announcements made at public places like an airport, subway station, or department store. In this case, we can interpret it as an instruction that can be translated as “it is desirable that”, “we advise you that”, or “please”; for example, 에스컬레이터를 이용하시기(를) 바랍니다 (Please use the escalator) and 자동판매기를 사용하시기 바랍니다 (Please use the vending machines).\n\n"
             "Note that the honorific form -(으)시기 바라다 is normally used for a public announcement. Note also that the object marker can be deleted (as in -기 바라다). In addition, -기를 is often contracted to -길 in speaking.",
             tables=[table(["Condition", "Rule", "Example"], [["After a verb stem", "add 기(를) 바라다", "이용하다 → 이용하기(를) 바라다; 기다리다 → 기다리기(를) 바라다"]], title="verb stem + 기(를) 바라다")],
             examples=[D(a, b) for a, b in _GB_EX]),
        card("Honorific forms for announcements",
             "The forms below are mine, made by the book’s rule with the honorific -(으)시-: 이용하시기 바랍니다.",
             tables=[table(["Dictionary form", "Meaning", "Public instruction"], [[v, m, _gb(v)] for v, m in _GB_V], say=[0, 2])]),
        card("Follow-up 3: complete the announcements",
             "The book gives five incomplete transcriptions of announcements over the subway public announcement system and asks you to complete the sentences with -기 바라다, using the given verb (서다, 이용하다, 갈아타다, 사다, 나가다). The sentences are the book’s; the completions and the English are mine. The book’s “2번 출구” is spelled out as 이 번 출구.",
             examples=[D(a, b) for a, b, _ in _GB_FU]),
        card("Activities left out",
             "Follow-up 4 (listening to four announcements over the public announcement system to write the place and the instruction in English) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the polite public instruction for “{m.split(';')[0]}” ({v})?", _gb(v), [stem(v) + "세요", stem(v) + "기 때문에", stem(v) + "고 있습니다"], f"{v} → {_gb(v)}.") for v, m in _GB_V]
        + _tr(_GB_EX + [(a, b) for a, b, _ in _GB_FU])
        + [F("입구가 아주 복잡합니다. 손님들은 줄을 ___ 바랍니다. (please stand)", "서시기", ["서기", "서세요"], "서다 + 시기 바랍니다 = 서시기 바랍니다."), F("에스컬레이터가 운행되지 않습니다. 계단을 이용하___ 바랍니다. (please use)", "시기", ["기", "세요"], "이용하다 + 시기 바랍니다."),
           F("시청역으로 가실 분들은 이 역에서 갈아타___ 바랍니다. (please transfer)", "시기", ["기", "세요"], "갈아타다 + 시기 바랍니다."), F("매표소에서 표를 사___ 바랍니다. (please buy)", "시기", ["기", "세요"], "사다 + 시기 바랍니다."),
           F("이 번 출구로 나가시___ 바랍니다. (please go out)", "기", ["길", "세요"], "나가시기 바랍니다."), F("자동판매기를 사용하시___ 바랍니다. (the contracted form of -기를)", "길", ["기를", "고"], "-기를 is often contracted to -길 in speaking."),
           F("건강하시기___ 바랍니다. (I wish you … with the object marker)", "를", ["가", "도"], "-기(를) 바라다: the object marker 를 can be dropped."), F("안전선에서 기다리___ 바랍니다. (please wait)", "시기를", ["세요를", "고를"], "기다리다 + 시기를 바랍니다."),
           M("What does -기(를) 바라다 literally mean?", "“(I) hope (you) to …”", ["“(I) know (you) to …”", "“(I) want to …”", "“(I) will …”"], "바라다 = to hope."), M("Where do we often hear -기(를) 바라다?", "In announcements at public places", ["In casual speech to friends", "Only in letters", "Only in the army"], "airport, subway station, department store."),
           M("Which form of -기(를) 바라다 is normally used for a public announcement?", "The honorific -(으)시기 바라다", ["The blunt -기 바란다", "The informal -기 바라", "The past -기 바랐다"], "-(으)시기 바라다 is normally used."), M("What may be dropped from -기를 바라다?", "The object marker 를", ["The verb stem", "The honorific -시-", "바라다"], "-기 바라다."),
           M("What is -기를 often contracted to in speaking?", "-길", ["-기가", "-게", "-기도"], "-기를 → -길."), M("How would you translate 이용하시기 바랍니다?", "Please use it.", ["You used it.", "I will use it.", "Don’t use it."], "-기 바랍니다 = please."),
           read_q("이용하시기 바랍니다"), read_q("기다리시기를 바랍니다"), read_q("갈아타시기 바랍니다"), read_q("사용하시길 바랍니다"), read_q("조심하시기 바랍니다")]
    ),
)

# ================================================================== Activities B
_OSAN = [
    ("지난 주말에 지하철을 타고 이대 앞에 사는 친구 집에 갔습니다.", "Last weekend I went by subway to the home of a friend who lives in front of Ewha Women’s University.", 1),
    ("먼저 오산 지하철역에 도착해서 자동판매기에서 승차권을 샀습니다.", "First I arrived at Osan subway station and bought a ticket at the vending machine.", 2),
    ("승차권을 산 후에 에스컬레이터를 타고 승강장으로 내려갔습니다.", "After buying the ticket, I went down to the platform by escalator.", 3),
    ("승강장에서 줄을 서서 기다린 후에 서울역 방면 일 호선 전동차를 탔습니다.", "After standing in line and waiting on the platform, I took the Line 1 train toward Seoul Station.", 4),
    ("일 호선을 타고 한 시간쯤 후에 신도림역에서 내렸습니다.", "After about an hour on Line 1, I got off at Sindorim Station.", 5),
    ("신도림역에서 내린 후에 갈아타는 곳 표지판을 따라 시청방면 이 호선으로 갈아탔습니다.", "After getting off at Sindorim Station, I followed the transfer sign and transferred to Line 2 toward City Hall.", 6),
    ("이 호선을 타고 몇 정거장을 더 간 후에 이대역에서 내렸습니다.", "After riding Line 2 for a few more stations, I got off at Ewha Women’s University Station.", 7),
    ("이대역에서 내린 후 일 번 출구로 나갔습니다.", "After getting off at Ewha Station, I went out through exit number 1.", 8),
]
_AD = [("명화당 찾아 오시는 길", "How to get to Myeonghwadang"), ("지하철 이용시: 사 호선 명동입구역이나 이 호선 을지로입구역에서 내리시면 됩니다.", "By subway: you can get off at Myeongdong-ipgu Station on Line 4 or Euljiro-ipgu Station on Line 2."),
       ("버스 이용시: 명동이나 외환은행 정거장에서 내리시면 됩니다.", "By bus: you can get off at the Myeongdong or Foreign Exchange Bank stop.")]
_AD_MODEL = [("진수야, 그 식당에 가려면, 논현역에서 먼저 칠 호선을 타고 건대입구 방면으로 가.", "Jinsu, to get to that restaurant, first take Line 7 at Nonhyeon Station and go toward Konkuk University Station.")]
L7 = lesson(
    "Ch 14 · Activities B: a subway trip and how to get to a restaurant",
    "오산에서 이대까지 · 갈아타는 곳 표지판을 따라 · 명화당 찾아 오시는 길 · 논현역에서 칠 호선",
    requires=[],
    cards=[
        card("Activity 1 (Reading and writing): photos of the Seoul subway",
             "The book shows eight photos from the Seoul Metropolitan Subway stations and asks you to write, in Korean and English, what each photo shows. The photos are pictures; the words that go with such signs are in the Core Vocabulary lessons of this chapter (금연, 출입금지, 승강장, 매표소, 자동판매기, 계단, 줄, 정거장)."),
        card("Activity 1b (Reading): a student’s subway trip from Osan to Ewha",
             "The passage is about a student’s experience using the Seoul Metro Subway from Osan to E-Dae (Ewha Women’s University) station. The book gives the eight sentences in scrambled order and asks you to arrange them in the order in which they occurred; three are done for you (the first, 5, and the last, 8). The sentences are the book’s (the numbers 1, 2 are spelled out); the English is mine, and the order is shown here in the right sequence.",
             examples=[D(ko, f"{en} (sentence {n})") for ko, en, n in _OSAN]),
        card("The order (mine)",
             "The numbers below are the right order of the actions.",
             tables=[table(["Number", "Sentence"], [[str(n), ko] for ko, en, n in _OSAN], say=[1])]),
        card("Activity 3 (Reading and writing): how to get to a famous restaurant",
             "The book shows an advertisement for a famous restaurant and asks you to circle the stations at which you should get off to get to it. The text is the book’s (the restaurant’s street address and telephone number are left out; 4호선 and 2호선 are spelled out). The answer (mine): Myeongdong-ipgu Station (Line 4) or Euljiro-ipgu Station (Line 2).",
             examples=passage(_AD)),
        card("Giving directions to a friend (Activity 3c)",
             "You want to recommend the restaurant to your friend 진수, and write the subway route he must take, using the subway map of the SMART Board activity. The book’s model begins as follows (the rest depends on the map, which is a picture; the English is mine):",
             examples=passage(_AD_MODEL)),
        card("Activities left out",
             "Activity 2 (listening to four subway announcements to say whether they are at a platform or in a train), Activity 3b (a SMART Board activity), Activity 4 (listening to subway directions from Apgujeong Station on Line 3 to Seoul Arts Center, Millennium Shopping Center, Gyeongbokgung and Lotte Department Store, and giving directions to Seoul Station, Hongik University Station, Korea University and Yongsan; the subway map is a picture) are audio, map, game or partner activities."),
    ],
    exercises=uniq(
        _tr([(ko, en) for ko, en, _ in _OSAN] + _AD + _AD_MODEL)
        + [M("Which is the first sentence of the Osan trip?", "지난 주말에 지하철을 타고 이대 앞에 사는 친구 집에 갔습니다.", ["이대역에서 내린 후 일 번 출구로 나갔습니다.", "먼저 오산 지하철역에 도착해서 자동판매기에서 승차권을 샀습니다.", "승차권을 산 후에 에스컬레이터를 타고 승강장으로 내려갔습니다."], "The trip starts with the first sentence, which tells that he/she went by subway to a friend’s house."),
           M("What did the student do right after arriving at Osan station?", "Bought a ticket at the vending machine", ["Took the escalator down", "Got off at Sindorim", "Went out through exit 1"], "먼저 오산 지하철역에 도착해서 자동판매기에서 승차권을 샀습니다."), M("What did the student do after buying the ticket?", "Went down to the platform by escalator", ["Transferred to Line 2", "Got off at Ewha", "Waited in line"], "승차권을 산 후에 에스컬레이터를 타고 승강장으로 내려갔습니다."),
           M("Which line did the student take from Osan?", "Line 1, toward Seoul Station", ["Line 2, toward City Hall", "Line 4", "Line 5"], "서울역 방면 일 호선 전동차."), M("Where did the student get off Line 1?", "Sindorim Station", ["Seoul Station", "Ewha Station", "City Hall"], "신도림역에서 내렸습니다."),
           M("What did the student follow to transfer?", "The transfer sign", ["A guide", "The crowd", "A map on the phone"], "갈아타는 곳 표지판을 따라."), M("Which line did the student transfer to?", "Line 2, toward City Hall", ["Line 1", "Line 4", "Line 7"], "시청방면 이 호선으로 갈아탔습니다."),
           M("How did the student leave Ewha Station?", "Through exit number 1", ["Through exit number 2", "By escalator to the bus", "By taxi"], "일 번 출구로 나갔습니다."), M("About how long was the ride on Line 1?", "About an hour", ["About five minutes", "About ten minutes", "About three hours"], "한 시간쯤 후에 신도림역에서 내렸습니다."),
           M("Where can you get off the train to get to Myeonghwadang?", "Myeongdong-ipgu (Line 4) or Euljiro-ipgu (Line 2)", ["City Hall (Line 1)", "Seoul Station (Line 4)", "Gimpo Airport"], "사 호선 명동입구역이나 이 호선 을지로입구역."), M("Where can you get off the bus?", "Myeongdong or the Foreign Exchange Bank stop", ["Seoul Station", "City Hall", "Gimpo Airport"], "명동이나 외환은행 정거장."),
           M("Which line does Jinsu take first at Nonhyeon Station in the model?", "Line 7", ["Line 2", "Line 4", "Line 3"], "논현역에서 먼저 칠 호선을 타고."), M("Which direction does Jinsu go on Line 7 in the model?", "Toward Konkuk University Station", ["Toward City Hall", "Toward Seoul Station", "Toward the airport"], "건대입구 방면으로 가."),
           F("승강장에서 줄을 서서 기다린 ___ 전동차를 탔습니다. (after)", "후에", ["전에", "동안"], "-(으)ㄴ 후에 = after."), F("이 호선을 타고 몇 정거장을 더 간 ___ 이대역에서 내렸습니다. (after)", "후에", ["전에", "동안"], "후에 = after."),
           F("서울역 ___ 일 호선 전동차를 탔습니다. (toward)", "방면", ["행", "대"], "~ 방면 = direction; bound."), F("신도림역에서 내린 후에 갈아타는 곳 표지판을 ___ 갈아탔습니다. (following)", "따라", ["내려", "올라"], "따라가다 = to follow."),
           F("명동입구역이나 을지로입구역에서 내리시___ 됩니다. (if you get off)", "면", ["고", "서"], "내리시면 됩니다 = you should get off."), F("그 식당에 가___ 논현역에서 먼저 칠 호선을 타. (if you want to go)", "려면", ["으면", "고"], "가다 → 가려면."),
           read_q("갈아타는 곳"), read_q("명화당"), read_q("을지로입구역"), read_q("신도림역"), read_q("일 번 출구")]
    ),
)

# ================================================================== Topic C
_C_DLG = [
    ("앤더슨 상병", "도로에 차가 왜 이렇게 많아요?", "Why are there so many cars on the road?"),
    ("택시 기사", "지금 출근 시간이어서 교통이 아주 복잡해요. 그리고 사고가 나서 더 막혀요.", "It is rush hour now, so the traffic is very congested. And because of an accident it is even more jammed."),
    ("앤더슨 상병", "여기서 코엑스까지 멀어요?", "Is it far from here to COEX?"),
    ("택시 기사", "아니요. 별로 안 멀어요. 걸어서 한 십오 분쯤 가면 돼요.", "No. It is not very far. It takes about fifteen minutes on foot."),
    ("앤더슨 상병", "그럼, 여기에서 내리겠습니다. 코엑스 가는 길 좀 가르쳐 주시겠어요?", "Then I will get off here. Could you tell me the way to COEX?"),
    ("택시 기사", "여기 횡단보도를 건너서 곧장 가세요. 그리고 지하도로 내려가시면 코엑스 입구가 나옵니다.", "Cross this crosswalk and go straight. And if you go down into the underpass, you will come to the COEX entrance."),
    ("앤더슨 상병", "네, 감사합니다. 그런데, 오후에 제가 이태원에 가려고 하는데 코엑스에서 어떻게 가요?", "Yes, thank you. By the way, I am going to go to Itaewon in the afternoon; how do I get there from COEX?"),
    ("택시 기사", "코엑스 앞에서 버스를 타세요. 지하철은 두 번 갈아타니까 버스가 더 편해요.", "Take a bus in front of COEX. You have to transfer twice on the subway, so the bus is more convenient."),
]
_C_WORDS = ["건너다", "걷다", "금지", "(운전)기사", "나다", "-(으)니까", "보행자", "사고", "승용차", "양보", "일방통행", "전용", "지하도", "차도 / 차로", "출근", "터널", "퇴근", "횡단보도"]
_SIGNS = [("일방통행", "one-way traffic"), ("횡단보도", "a pedestrian crossing"), ("버스전용차로", "a bus-only lane (mine)"), ("자동차전용도로", "a motor-vehicles-only road (mine)"), ("보행자전용도로", "a pedestrians-only road (mine)"), ("자전거전용도로", "a bicycles-only road (mine)"),
          ("좌회전", "a left turn (mine)"), ("우회전", "a right turn (mine)"), ("정지", "stop (mine)"), ("양보", "yield"), ("터널", "a tunnel"), ("도로공사 중", "road under construction (mine)"), ("통행금지", "no passage (mine)"), ("주차금지", "no parking (mine)"), ("자동차통행금지", "no motor vehicles (mine)")]
_TAN = [
    ("저는 오늘 친구들과 함께 롯데월드에 갔습니다.", "Today I went to Lotte World with my friends."),
    ("우리는 길을 잘 몰라서 택시를 탔습니다.", "We did not know the way well, so we took a taxi."),
    ("택시는 편했습니다.", "The taxi was comfortable."),
    ("그런데 가는 길에 앞 차가 교통사고가 났습니다.", "But on the way, the car ahead had a traffic accident."),
    ("차가 많이 막히고 복잡했습니다.", "The traffic was very jammed and congested."),
    ("택시 요금이 너무 비싸서 우리는 택시에서 내렸습니다.", "The taxi fare was too expensive, so we got out of the taxi."),
    ("그리고 버스를 탔습니다.", "And we took a bus."),
    ("버스는 버스 전용차로로 가니까 막히지 않았습니다.", "The bus went in the bus-only lane, so it was not stuck."),
    ("하지만 사람이 많아서 앉을 자리가 없었습니다.", "But there were many people, so there was no seat to sit in."),
    ("그래서 호텔로 돌아오는 길에는 지하철을 탔습니다.", "So on the way back to the hotel we took the subway."),
    ("지하철에는 사람이 많고 조금 복잡했습니다.", "There were many people on the subway and it was a little crowded."),
    ("그렇지만 깨끗하고 빨랐습니다.", "But it was clean and fast."),
    ("버스와 지하철 모두 교통카드를 사용할 수 있어서 편리했습니다.", "Both the bus and the subway accept the transportation card, so it was convenient."),
]
_SINO_GEUM = [("금연", "no smoking; “forbidding smoke”"), ("금주", "no drinking; “forbidding liquor”"), ("출입 금지", "Do not enter"), ("주차 금지", "No parking")]
_SINO_DO = [("도로", "a street; “road way”"), ("차도", "a road; “a road for cars”"), ("인도", "a walkway; “a road for people”"), ("하수도", "sewer; “under water way”"), ("상수도", "water supply; “above water way”"), ("태권도", "tae kwon do; “way of stepping and punching”"), ("유도", "judo; “way of flow”"), ("경기도", "Gyeonggi Province"), ("제주도", "Jeju Province (Jeju Island)")]
L8 = lesson(
    "Ch 14 · Topic C: Traffic is congested because of an accident",
    "사고가 나서 교통이 아주 복잡해요 · 횡단보도를 건너서 곧장 가세요 · 교통 안전 표지 · 금 (禁) · 도 (道)",
    requires=[],
    cards=[
        card("Topic C: Traffic is congested because of an accident",
             "SPC Anderson is talking with a taxi driver on the way to COEX (Convention and Exhibition center) in Seoul. (The English is mine; the book writes 코엑스(COEX) and 15분, here 코엑스 and 십오 분.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter). The book lists 금지(하다 / 되다), 사고(나다) and 차도 / 차로 with the optional parts in parentheses; they are kept in the meanings here.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Traffic safety signs (교통 안전 표지)",
             "The book shows these signs as pictures and asks you to write the English term under each sign (Presentation Activity c). The Korean names of the signs are the book’s; the English meanings are mine, except 일방통행, 횡단보도, 양보 and 터널, which are in the Core Vocabulary.",
             tables=[ktable(_SIGNS)]),
        card("Cultural notes: 교통카드",
             "교통카드 is a pre-paid card for the public transportation system in Korea. You can purchase and recharge various types of 교통카드 at many kiosks, nearly all convenience stores, and subway ticket booths."),
        card("Sino-Korean in use: 금 (禁)",
             "This Sino-Korean syllable means forbid or ban, as in 금연 (no smoking; “forbidding smoke”), 금주 (no drinking; “forbidding liquor”), 출입 금지 (Do not enter), 주차 금지 (No parking), etc. The book asks: can you explain why 여학생 기숙사 (a dorm for female students) is often referred to as 금남의 집? My answer: 금남 means “forbidding men” (남 = male), so a 금남의 집 is a house where men are not allowed.",
             tables=[ktable(_SINO_GEUM + [("금남의 집", "a house where men are forbidden (mine); a women’s dormitory"), ("여학생 기숙사", "a dorm for female students")])]),
        card("Sino-Korean in use: 도 (道)",
             "This Sino-Korean syllable means a road or way, as in 도로 (a street; “road way”), 차도 (a road; “a road for cars”), 인도 (a walkway; “a road for people”), 하수도 (sewer; “under water way”), 상수도 (water supply; “above water way”), 태권도 (tae kwon do; “way of stepping and punching”), 유도 (judo; “way of flow”), etc. The same syllable is also used for the proper names of Korean provinces, as in 경기도 and 제주도.",
             tables=[ktable(_SINO_DO)]),
        card("Follow-up 1 (Reading): SPC Tanner’s journal",
             "The book asks you to read SPC Tanner’s journal and fill in a table in English (the positive and negative aspects of the taxi, the bus and the subway). The text is the book’s; the English is mine.",
             examples=passage(_TAN)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Form of transportation", "Positive aspect(s)", "Negative aspect(s)"], [["Taxi", "Comfortable", "The car ahead had an accident and the traffic was jammed; the fare was too expensive"], ["Bus", "It used the bus-only lane, so it was not stuck; it accepts the transportation card", "So many people that there was no seat"], ["Subway", "Clean and fast; it accepts the transportation card", "Many people, a little crowded"]])]),
        card("Activities left out",
             "The SMART Board activity, the role-play preparation of Presentation Activity d (Group A as SPC Anderson, Group B as the taxi driver) and Follow-up 2 (listening to two conversations in which a woman asks a man for directions on the street, to write the destination and direction) are game, audio or partner activities. The Useful Links (the transportation card and the traffic safety signs) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith(("-", "~"))]))
        + _tr(_strip(_C_DLG) + _SIGNS[:4] + _SIGNS[10:11] + _TAN + _SINO_GEUM + _SINO_DO[:7])
        + [M("Why is the traffic so congested?", "It is rush hour and there was an accident", ["The road is under construction", "It is a holiday", "It is snowing"], "출근 시간이어서 … 사고가 나서 더 막혀요."), M("How far is COEX on foot?", "About fifteen minutes", ["About five minutes", "About an hour", "About two hours"], "걸어서 한 십오 분쯤."),
           M("What does the driver tell Anderson to cross?", "A crosswalk", ["A bridge", "A tunnel", "A river"], "횡단보도를 건너서 곧장 가세요."), M("How does Anderson reach the COEX entrance after crossing?", "Go down the underpass", ["Take the elevator", "Take a taxi", "Take the subway"], "지하도로 내려가시면 코엑스 입구가 나옵니다."),
           M("Where does Anderson want to go in the afternoon?", "Itaewon", ["Lotte World", "Seoul Station", "Myeongdong"], "오후에 제가 이태원에 가려고 하는데."), M("Why does the driver recommend the bus to Itaewon?", "The subway needs two transfers", ["The bus is cheaper", "The subway is closed", "The bus is faster"], "지하철은 두 번 갈아타니까 버스가 더 편해요."),
           M("Where did SPC Tanner go?", "Lotte World", ["COEX", "Itaewon", "Myeongdong"], "롯데월드에 갔습니다."), M("Why did Tanner and friends get out of the taxi?", "The taxi fare was too expensive", ["The taxi broke down", "They arrived", "They wanted to walk"], "택시 요금이 너무 비싸서 우리는 택시에서 내렸습니다."),
           M("Why was the bus not stuck?", "It went in the bus-only lane", ["It was empty", "It went through a tunnel", "It was early"], "버스는 버스 전용차로로 가니까 막히지 않았습니다."), M("What was bad about the bus?", "There was no seat because there were many people", ["It was slow", "It was expensive", "It was dirty"], "사람이 많아서 앉을 자리가 없었습니다."),
           M("How did they return to the hotel?", "By subway", ["By taxi", "By bus", "On foot"], "호텔로 돌아오는 길에는 지하철을 탔습니다."), M("What was good about both the bus and the subway?", "Both accept the transportation card", ["Both are free", "Both are empty", "Both are faster than a taxi"], "교통카드를 사용할 수 있어서 편리했습니다."),
           M("What does the Sino-Korean syllable 금 (禁) mean?", "to forbid; to ban", ["a road; a way", "a vehicle", "to ride"], "금연, 금주, 출입 금지, 주차 금지."), M("What does the Sino-Korean syllable 도 (道) mean?", "a road; a way", ["to forbid", "a vehicle", "to ride"], "도로, 차도, 인도, 태권도."),
           M("Which word means “no smoking”?", "금연", ["금주", "금남", "금지"], "금연 = prohibited smoking."), M("Which words end with 도 meaning “a road; a way”?", "하수도 and 상수도", ["도로 and 하수도", "경기도 and 제주도", "차도 and 차창"], "하수도 and 상수도 end with 道 meaning way."),
           F("지금 출근 시간이어서 교통이 아주 ___. (congested)", "복잡해요", ["편해요", "깨끗해요"], "복잡하다 = to be congested."), F("횡단보도를 ___ 곧장 가세요. (cross, and then)", "건너서", ["건너고", "건너면"], "건너다 + -아서 = 건너서."),
           F("사고가 ___ 더 막혀요. (occurred, so)", "나서", ["가서", "와서"], "사고가 나다 = an accident occurs."), F("버스는 버스 전용차로로 가___ 막히지 않았습니다. (because)", "니까", ["아서", "기"], "가니까 = because it goes."),
           F("그 길은 ___이기 때문에 들어갈 수 없습니다. (one-way)", "일방통행", ["횡단보도", "지하도"], "일방통행 = one-way traffic."), F("길을 건널 때는 ___를 이용하세요. (crosswalk)", "횡단보도", ["일방통행", "터널"], "횡단보도 = a pedestrian crossing."),
           read_q("횡단보도"), read_q("교통 안전 표지"), read_q("출근 시간"), read_q("일방통행"), read_q("교통카드")]
    ),
)

# ================================================================== Grammar C: ㄷ irregular verbs
_D_VERBS = [("묻다", "to ask", True), ("믿다", "to believe", False), ("듣다", "to hear; to listen", True), ("싣다", "to load", True), ("걷다", "to walk", True), ("받다", "to receive", False), ("닫다", "to close", False), ("얻다", "to get; to obtain", False)]


def _dform(verb, irregular):
    """(-습니다/ㅂ니다, -아요/어요, -았/었어요, -을 거예요, -으면): ㄷ becomes ㄹ before a vowel for the four ㄷ irregular verbs"""
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    assert t == "ㄷ", verb
    base = st[:-1] + _K.compose(l, v, "ㄹ") if irregular else st
    ao = "아" if v in ("ㅏ", "ㅗ") else "어"
    inf = base + ao
    return st + "습니다", inf + "요", inf[:-1] + _K.compose(*_K.decompose(inf[-1])[:2], "ㅆ") + "어요", base + "을 거예요", base + "으면"


_D_EX = [("학교에 어떻게 가요?", "How do you get to school?"), ("걸어서 가요.", "I walk to school."), ("이 짐을 어떻게 할까요?", "What do you want me to do with this luggage?"), ("자동차 트렁크에 실어 주세요.", "Please load it in the trunk."),
         ("여기에서 강남역에 어떻게 가요?", "How can I get to Gangnam station from here?"), ("글쎄요. 저는 잘 몰라요. 다른 사람에게 물어 보세요.", "Well, I do not know. Please ask others.")]
L9 = lesson(
    "Ch 14 · Grammar C: ㄷ irregular verbs",
    "걷다 → 걸어요 · 묻다 → 물어요 · 듣다 → 들어요 · 싣다 → 실어요 · 받다 → 받아요",
    requires=[],
    cards=[
        card("ㄷ irregular verbs",
             "There are quite a few action verbs whose stem ends in ㄷ, such as 걷다 (to walk), 싣다 (to load), and 받다 (to receive). Among these action verbs, there are a few, namely 걷다 (to walk), 묻다 (to ask), 듣다 (to hear/to listen), and 싣다 (to load), that do not follow the regular conjugation rule. When these verbs are followed by a vowel such as 아 / 어, ㄷ changes to ㄹ. They are commonly known as ㄷ irregular verbs. (The regular ㄷ verbs, such as 받다 and 믿다, keep their ㄷ.)",
             tables=[table(["Verb", "Stem", "ㄷ to ㄹ", "Add verb ending"], [["걷다", "걷", "걸", "걸어요, 걸었어요, …"], ["묻다", "묻", "물", "물어요, 물었어요, …"], ["듣다", "듣", "들", "들어요, 들었어요, …"], ["싣다", "싣", "실", "실어요, 실었어요, …"]], title="ㄷ irregular verb change", say=[0, 1, 2, 3])],
             examples=[D(a, b) for a, b in _D_EX]),
        card("Follow-up 1: conjugate the ㄷ verbs",
             "The stems of all the verbs in the first column of the book’s table end in ㄷ; some are ㄷ irregular. The book gives the verbs 묻다, 믿다, 듣다, 싣다, 걷다 and 받다 and asks you to conjugate them in -습니다/ㅂ니다, -아요/어요, -을 거예요 and -으면. The answers are mine (I added the past tense and two regular ㄷ verbs, 닫다 and 얻다). Note that 믿다 and 받다 are regular.",
             tables=[table(["Verb", "Meaning", "-습니다", "-아요/어요", "-았/었어요", "-을 거예요", "-으면", "Irregular?"], [[v, m, *_dform(v, irr), "ㄷ irregular" if irr else "regular"] for v, m, irr in _D_VERBS], say=[0, 2, 3, 4, 5, 6])]),
        card("Activities left out",
             "Follow-up 2 (listening to three short dialogs to identify what the male speaker did yesterday and to transcribe the ㄷ irregular verbs) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the informal polite form of {v} ({m})?", _dform(v, irr)[1], [x for x in dict.fromkeys([_dform(v, not irr)[1], stem(v) + "어요", stem(v) + "아요"]) if x != _dform(v, irr)[1]][:3], f"{v} → {_dform(v, irr)[1]}.{' ㄷ → ㄹ before a vowel.' if irr else ' A regular ㄷ verb keeps ㄷ.'}") for v, m, irr in _D_VERBS]
        + [M(f"Which is the past tense of {v} ({m})?", _dform(v, irr)[2], [x for x in dict.fromkeys([_dform(v, not irr)[2], stem(v) + "었어요", stem(v) + "았어요"]) if x != _dform(v, irr)[2]][:3], f"{v} → {_dform(v, irr)[2]}.") for v, m, irr in _D_VERBS]
        + [M(f"Which is the “if” form (-으면) of {v}?", _dform(v, irr)[4], [x for x in dict.fromkeys([_dform(v, not irr)[4], stem(v) + "면", stem(v)[:-1] + "ㄹ면"]) if x != _dform(v, irr)[4]][:2], f"{v} → {_dform(v, irr)[4]}.") for v, m, irr in _D_VERBS if irr or v in ("받다", "믿다")]
        + _tr(_D_EX)
        + [M(f"Is {v} ({m}) a ㄷ irregular verb?", "Yes", ["No"], f"{v} changes ㄷ to ㄹ before a vowel.") for v, m, irr in _D_VERBS if irr] + [M(f"Is {v} ({m}) a ㄷ irregular verb?", "No, it is regular", ["Yes"], f"{v} keeps ㄷ: {_dform(v, irr)[1]}.") for v, m, irr in _D_VERBS if not irr]
        + [F("학교에 ___ 가요. (on foot)", "걸어서", ["걷어서", "걷고"], "걷다 → 걸어서 (ㄷ → ㄹ)."), F("자동차 트렁크에 ___ 주세요. (load it)", "실어", ["싣어", "실려"], "싣다 → 실어 주세요."), F("다른 사람에게 ___ 보세요. (ask)", "물어", ["묻어", "무러"], "묻다 → 물어 보세요."),
           F("저는 매일 음악을 ___요. (listen)", "들어", ["듣어", "드러"], "듣다 → 들어요."), F("친구한테 선물을 ___요. (receive)", "받아", ["발라", "받어"], "받다 is regular: 받아요."), F("저는 그 사람을 ___요. (believe)", "믿어", ["밀어", "미더"], "믿다 is regular: 믿어요."),
           F("어제 한 시간 ___ 었어요. (walked: 걷 + 었)", "걸", ["걷", "거"], "걷다 → 걸었어요."), F("물어 ___ 한국말을 잘 하는 사람이 있어요. (if I ask)", "보면", ["보고", "봐서"], "묻다 → 물어 보면."),
           M("What happens to ㄷ in 걷다, 묻다, 듣다, 싣다 before a vowel such as 아 or 어?", "ㄷ changes to ㄹ", ["ㄷ is dropped", "ㄷ changes to ㄴ", "Nothing happens"], "걷다 → 걸어요."), M("Which verb is a regular ㄷ verb?", "받다", ["걷다", "듣다", "묻다"], "받다 keeps ㄷ."),
           M("Which verb is a regular ㄷ verb?", "믿다", ["싣다", "걷다", "듣다"], "믿다 keeps ㄷ."), M("Which verb means “to hear; to listen”?", "듣다", ["묻다", "걷다", "싣다"], "듣다 = to hear/to listen."),
           read_q("걸어요"), read_q("물어요"), read_q("들어요"), read_q("실어요"), read_q("받아요")]
    ),
)

# ================================================================== Grammar D: -(으)니까
def _nikka(verb):
    """-(으)니까: 니까 after a vowel, 으니까 after a consonant; ㄹ stems drop ㄹ; ㅂ irregular stems take 우: 춥다 -> 추우니까"""
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    if t == "ㄹ":
        return st[:-1] + _K.compose(l, v, "") + "니까"
    if verb in _B_IRR:
        return _base_ao(verb)[:-1] + "우니까"
    return st + ("으니까" if t else "니까")


_NK_V = [("오다", "to come"), ("가다", "to go"), ("바쁘다", "to be busy"), ("피곤하다", "to be tired"), ("막히다", "to be congested"), ("좋다", "to be good"), ("많다", "to be many"), ("있다", "to exist; to have"), ("없다", "to not exist; to not have"),
         ("춥다", "to be cold"), ("덥다", "to be hot"), ("어렵다", "to be difficult"), ("놀다", "to play; to have fun"), ("알다", "to know"), ("먹다", "to eat")]
_NK_EX = [
    ("날씨가 좋으니까 산책했어요.", "I took a walk because the weather was nice."), ("피곤하니까 일찍 잤어요.", "I went to bed early because I was tired."), ("날씨가 좋으니까 산책합시다.", "Let’s take a walk because the weather is nice. (suggestion)"),
    ("날씨가 좋으니까 산책하세요.", "Take a walk because the weather is nice. (advice)"), ("밖이 추우니까 창문을 닫아 주세요.", "Please close the window because it is cold outside. (request)"),
    ("추우니까 창문 좀 닫아 주세요.", "Please close the window because it is cold."), ("길에 차가 많으니까 조심하세요.", "Be careful because there are many cars in the road."), ("늦었으니까 빨리 해.", "Hurry up because we are late."),
    ("길이 막히니까 지하철을 탑시다.", "Let’s take a subway because the road is congested."), ("비가 오니까 따뜻한 커피가 마시고 싶어요.", "I would like to drink hot coffee because it is raining."),
    ("이 영화는 봤으니까 다른 영화를 봅시다.", "Because I have seen this movie, let’s see another one."), ("김 선생님께서 한식을 좋아하시니까 한국식당으로 갈까요?", "Because Mr. Kim likes Korean food, shall we go to the Korean restaurant?"),
]
_NK_STAR = [("날씨가 좋아서 산책합시다.", "-아서/어서 cannot be followed by a suggestion (use 좋으니까)"), ("날씨가 좋기 때문에 산책합시다.", "-기 때문에 cannot be followed by a suggestion (use 좋으니까)"), ("날씨가 좋아서 산책하세요.", "-아서/어서 cannot be followed by advice or a command (use 좋으니까)"),
            ("날씨가 좋기 때문에 산책하세요.", "-기 때문에 cannot be followed by advice or a command (use 좋으니까)"), ("밖이 추워서 창문을 닫아 주세요.", "-아서/어서 cannot be followed by a request (use 추우니까)"), ("밖이 춥기 때문에 창문을 닫아 주세요.", "-기 때문에 cannot be followed by a request (use 추우니까)")]
_NK_MATCH = [("날씨가 춥습니다.", "날씨가 추우니까 잠바를 입으세요."), ("배가 고픕니다.", "배가 고프니까 빨리 밥을 먹읍시다."), ("바쁩니다.", "바쁘니까 등산은 다음에 갑시다."), ("지하철이 고장이 났습니다.", "지하철이 고장이 났으니까 버스를 타세요."),
             ("숙제가 어렵습니다.", "숙제가 어려우니까 친구하고 같이 할까요?"), ("피곤합니다.", "피곤하니까 집에서 쉬어야겠어요."), ("비가 옵니다.", "비가 오니까 따뜻한 커피를 마시고 싶어요."), ("차가 막힙니다.", "차가 막히니까 걸어서 갈까요?")]
_NK_MEAN = ["Because it is cold, put on a jacket.", "Because I am hungry, let’s eat quickly.", "Because I am busy, let’s go hiking another time.", "Because the subway broke down, take a bus.", "Because the homework is difficult, shall we do it together with a friend?",
            "Because I am tired, I think I should rest at home.", "Because it is raining, I want to drink hot coffee.", "Because the traffic is congested, shall we go on foot?"]
L10 = lesson(
    "Ch 14 · Grammar D: a reason with -(으)니까",
    "비가 오니까 · 날씨가 좋으니까 · 추우니까 · 늦었으니까 · 길이 막히니까",
    requires=[],
    cards=[
        card("Expressing a reason using -(으)니까",
             "Like the two conjunctive endings -아서/어서 and -기 때문에, which you learned in earlier chapters, the conjunctive ending -(으)니까 is used to express a reason, and can be translated as “because” or “since”. However, -(으)니까 is normally used to express a logical reason. In 날씨가 좋으니까 산책했어요 (I took a walk because the weather was nice), 날씨가 좋으니까 is a logical reason for taking a walk; in 피곤하니까 일찍 잤어요 (I went to bed early because I was tired), 피곤하니까 is a logical reason for going to bed early.\n\n"
             "Therefore -(으)니까 is readily followed by a request, advice, command, or suggestion that is based on a logical reason, whereas the other two conjunctive endings are not.",
             tables=[table(["Condition", "Rule", "Example"], [["After a verb stem ending with a vowel", "add 니까", "비가 오다 → 비가 오니까"], ["After a verb stem ending with a consonant", "add 으니까", "날씨가 좋다 → 날씨가 좋으니까"]], title="verb stem + (으)니까")],
             examples=[D(a, b) for a, b in _NK_EX[:5]]),
        card("The ungrammatical sentences (marked * in the book)",
             "The sentences below are ungrammatical (the asterisk * means that the sentence is ungrammatical): -아서/어서 and -기 때문에 cannot be followed by a suggestion, advice, a request or a command. (The reasons are mine.)",
             tables=[table(["Ungrammatical sentence", "Why"], [[a, b] for a, b in _NK_STAR])]),
        card("More examples",
             "The book’s further examples, including the honorific and tense markers that can be added to the verb stem if needed (이 영화는 봤으니까; 한식을 좋아하시니까).",
             examples=[D(a, b) for a, b in _NK_EX[5:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule; stems ending in ㄹ drop it before ㄴ (놀다 → 노니까), and the ㅂ irregular verbs 춥다, 덥다 and 어렵다 change ㅂ to 우 (추우니까, 더우니까, 어려우니까).",
             tables=[table(["Dictionary form", "Meaning", "-(으)니까"], [[v, m, _nikka(v)] for v, m in _NK_V], say=[0, 2])]),
        card("Follow-up 3: connect the sentences that have a cause-and-effect relationship",
             "The book gives eight reasons on the left and eight results on the right (빨리 밥을 먹읍시다, 집에서 쉬어야겠어요, 걸어서 갈까요?, 잠바를 입으세요, 친구하고 같이 할까요?, 등산은 다음에 갑시다, 버스를 타세요, 따뜻한 커피를 마시고 싶어요) and says the answers may vary. These matches, joined with -(으)니까, are mine.",
             tables=[table(["Reason (the book)", "Joined sentence (mine)", "Meaning (mine)"], [[a, b, c] for (a, b), c in zip(_NK_MATCH, _NK_MEAN)], say=[0, 1])]),
        card("Follow-up 5: a partial sentence",
             "In the book each student writes the first part of a sentence with -(으)니까 and classmates add the second part. The book’s model: 오늘은 시간이 많으니까 (Because I have a lot of time today, …) → 오늘은 시간이 많으니까 백화점에 쇼핑갑시다 (Because I have a lot of time today, let’s go shopping at the department store) or 영화 볼까요? (shall we see a movie?).",
             examples=[D("오늘은 시간이 많으니까 백화점에 쇼핑갑시다.", "Because I have a lot of time today, let’s go shopping at the department store."), D("오늘은 시간이 많으니까 영화 볼까요?", "Because I have a lot of time today, shall we see a movie?")]),
        card("Activities left out",
             "Follow-up 4 (listening to three short conversations in which the second person gives a reason and a suggestion, to complete a table in English) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the -(으)니까 form of {v} ({m})?", _nikka(v), [x for x in dict.fromkeys([stem(v) + "니까", stem(v) + "으니까", if_(v), stem(v) + "아서"]) if x != _nikka(v)][:3], f"{v} → {_nikka(v)}.") for v, m in _NK_V]
        + _tr(_NK_EX + [(b, c) for (a, b), c in zip(_NK_MATCH, _NK_MEAN)])
        + [F("날씨가 좋___ 산책합시다. (because)", "으니까", ["아서", "기 때문에"], "A suggestion follows, so use -(으)니까: 좋으니까."), F("밖이 추___ 창문을 닫아 주세요. (because)", "우니까", ["워서", "기 때문에"], "A request follows: 춥다 → 추우니까."),
           F("길에 차가 많___ 조심하세요. (because)", "으니까", ["아서", "기 때문에"], "Advice follows: 많으니까."), F("비가 ___ 따뜻한 커피가 마시고 싶어요. (because it rains)", "오니까", ["와서", "오기"], "오다 + 니까 = 오니까."),
           F("늦었___ 빨리 해. (because we are late)", "으니까", ["아서", "기 때문에"], "The past stem 늦었 ends in a consonant: 늦었으니까."), F("길이 막히___ 지하철을 탑시다. (because)", "니까", ["으니까", "아서"], "막히다 ends in a vowel: 막히니까."),
           F("김 선생님께서 한식을 좋아하시___ 한국식당으로 갈까요? (because)", "니까", ["으니까", "아서"], "좋아하시 ends in a vowel: 좋아하시니까."), F("이 영화는 봤___ 다른 영화를 봅시다. (because I have seen)", "으니까", ["니까", "아서"], "봤 ends in a consonant: 봤으니까."),
           M("Which ending is normally used for a logical reason followed by a request or suggestion?", "-(으)니까", ["-아서/어서", "-기 때문에", "-고"], "-(으)니까 can be followed by a request, advice, command or suggestion."), M("Which sentence is ungrammatical?", "날씨가 좋아서 산책합시다.", ["날씨가 좋으니까 산책합시다.", "날씨가 좋아서 산책했어요.", "날씨가 좋으니까 산책하세요."], "-아서 cannot be followed by a suggestion."),
           M("Which sentence is ungrammatical?", "밖이 추워서 창문을 닫아 주세요.", ["밖이 추우니까 창문을 닫아 주세요.", "밖이 추워서 창문을 닫았어요.", "추우니까 창문 좀 닫아 주세요."], "-아서 cannot be followed by a request."), M("What does -(으)니까 mean?", "because; since", ["if", "but", "in order to"], "-(으)니까 = because; since."),
           M("Which ending is added to a verb stem ending in a vowel?", "니까", ["으니까", "으면", "려고"], "오다 → 오니까."), M("Which ending is added to a verb stem ending in a consonant?", "으니까", ["니까", "으면", "려고"], "좋다 → 좋으니까."),
           M("Which sentence means “Let’s take a subway because the road is congested”?", "길이 막히니까 지하철을 탑시다.", ["길이 막혀서 지하철을 탑시다.", "길이 막히면 지하철을 탔어요.", "길이 막히지만 지하철을 탑시다."], "막히니까 + suggestion."),
           read_q("비가 오니까"), read_q("날씨가 좋으니까"), read_q("추우니까"), read_q("늦었으니까"), read_q("길이 막히니까")]
    ),
)

# ================================================================== Activities C
_MATCH = [("사람들이 길을 건너는 곳입니다.", "횡단보도", "a pedestrian crossing"), ("다른 차들이 먼저 가야 합니다. 기다리세요.", "양보", "yield"), ("일하러 갑니다.", "출근", "going to work"), ("길에서 걸어 다니는 사람들입니다.", "보행자", "a pedestrian"), ("여기서는 차들이 한 방향으로만 갑니다.", "일방통행", "one-way traffic")]
_MAIL = [
    ("친구들, 안녕?", "Friends, hello!"), ("서울 시내는 너무 복잡해서 길을 잘 모르겠어.", "Downtown Seoul is so congested that I don’t know the way well."), ("내일 한 시까지 연세대학교 정문 앞에서 친구를 만나야 해.", "I have to meet a friend in front of the main gate of Yonsei University by one o’clock tomorrow."),
    ("어떻게 가는지 좀 가르쳐 줘.", "Please tell me how to get there."), ("시청에서 출발할 거야.", "I will start from City Hall."), ("어떻게 가?", "How do I get there?"),
]
_ROUTES = [("이메일 일", "시청 → 충정로 → 신촌 → 연세대학교 (and walking for 15 minutes)"), ("이메일 이", "시청 → 합정동 → 홍익대학교 → 연세대학교")]
_BUS = [("빨강버스", "the red bus: connects the Seoul metropolitan area to some areas in Kyung-ki Province"), ("파랑버스", "the blue bus"), ("녹색버스", "the green bus"), ("노랑버스", "the yellow bus")]
L11 = lesson(
    "Ch 14 · Activities C: traffic words, an e-mail asking for directions, and the buses of Seoul",
    "횡단보도 · 양보 · 출근 · 보행자 · 일방통행 · 시청에서 출발할 거야 · 빨강버스 · 파랑버스",
    requires=[],
    cards=[
        card("Activity 1 (Reading): match the description with the word",
             "The book gives five descriptions on the left and five words on the right (양보, 횡단보도, 출근, 일방통행, 보행자) and asks you to match them by drawing lines. The descriptions are the book’s; the matches and the English are mine.",
             tables=[table(["Description (the book)", "Word (mine)", "Meaning"], [[a, b, c] for a, b, c in _MATCH], say=[0, 1])]),
        card("Activity 4 (Reading): SPC Anderson’s e-mail",
             "SPC Anderson has been stationed in Korea. He e-mailed two of his Korean friends to ask for help. The book asks you to identify, in English, the information he needs help with. The text is the book’s (the e-mail addresses are left out; 1시 is spelled out as 한 시); the English is mine. The answer (mine): he needs to know how to get from City Hall to the front of the main gate of Yonsei University by one o’clock tomorrow.",
             examples=passage(_MAIL)),
        card("The two replies",
             "The book gives two reply e-mails (이메일 1 and 이메일 2) as pictures; only the routes drawn in boxes can be read: the first goes from City Hall through Chungjeongno and Sinchon to Yonsei University, with a walk of 15 minutes; the second from City Hall through Hapjeong-dong and Hongik University to Yonsei University. The book asks you to write the forms of transportation, the total fare and other information; these are in the pictures and cannot be given here.",
             tables=[table(["E-mail", "Route (as drawn in the book)"], [[a, b] for a, b in _ROUTES])]),
        card("Notes: the buses of Seoul",
             "There are four different types of bus systems in Seoul, such as 빨강, 파랑, 녹색, and 노랑 버스, depending on their operation routes. 빨강버스 is the one that connects the Seoul metropolitan area to some areas in Kyung-ki Province. (The colors blue, green and yellow are mine, from the names; the book gives only the red bus’s route.)",
             tables=[ktable(_BUS)]),
        card("Activities left out",
             "Activity 2 (listening to three radio traffic reports to identify the problem and the suggestion), Activity 3 (a radio traffic report and a map of central Seoul, to choose a route from Midopa department store to Dongdaemun stadium) and the partner steps of Activity 4 (sharing the e-mail information and deciding which transportation to take) are audio, map or partner activities."),
    ],
    exercises=uniq(
        [M(f"Which word matches “{en}”?", ko, [x for _, x, _ in _MATCH if x != ko][:3], f"{ko} = {en}.") for d, ko, en in _MATCH]
        + [M(f"What does {d} describe?", ko, [x for _, x, _ in _MATCH if x != ko][:3], f"{d} → {ko}.") for d, ko, en in _MATCH]
        + _tr(_MAIL[1:] + _BUS[:1])
        + [M("What does SPC Anderson need help with?", "How to get from City Hall to Yonsei University by 1 o’clock tomorrow", ["Where to buy a ticket", "Where to find a hotel", "How to call a taxi"], "시청에서 출발할 거야. 어떻게 가?"), M("Where does Anderson have to meet a friend?", "In front of the main gate of Yonsei University", ["At City Hall", "At Seoul Station", "At Hongik University"], "연세대학교 정문 앞에서 친구를 만나야 해."),
           M("When does Anderson have to meet his friend?", "By one o’clock tomorrow", ["By noon today", "By nine tomorrow", "Next week"], "내일 한 시까지."), M("Where does Anderson start from?", "City Hall", ["Seoul Station", "Yonsei University", "Sinchon"], "시청에서 출발할 거야."),
           M("Why doesn’t Anderson know the way?", "Downtown Seoul is very congested", ["He is a tourist", "He lost his map", "He is lost at the airport"], "서울 시내는 너무 복잡해서 길을 잘 모르겠어."), M("Which station comes after Chungjeongno in the first route?", "Sinchon", ["Hapjeong-dong", "Hongik University", "City Hall"], "시청 → 충정로 → 신촌 → 연세대학교."),
           M("Which station comes after Hapjeong-dong in the second route?", "Hongik University", ["Sinchon", "Chungjeongno", "City Hall"], "시청 → 합정동 → 홍익대학교."), M("How many kinds of bus systems are there in Seoul?", "Four", ["Two", "Three", "Five"], "빨강, 파랑, 녹색, 노랑."),
           M("What does the red bus connect?", "The Seoul metropolitan area and some areas in Kyung-ki Province", ["Seoul and Busan", "The airport and City Hall", "Two subway lines"], "빨강버스는 … 경기도 일부 지역."),
           F("사람들이 길을 건너는 곳은 ___입니다. (pedestrian crossing)", "횡단보도", ["일방통행", "지하도"], "횡단보도 = a pedestrian crossing."), F("다른 차들이 먼저 가야 합니다. ___하세요. (yield)", "양보", ["출근", "퇴근"], "양보하다 = to yield."),
           F("저는 아침 여덟 시에 ___합니다. (go to work)", "출근", ["퇴근", "양보"], "출근하다 = to go to work."), F("길에서 걸어 다니는 사람들은 ___입니다. (pedestrians)", "보행자", ["승객", "기사"], "보행자 = a pedestrian."),
           F("여기서는 차들이 한 방향으로만 갑니다. ___ 도로입니다. (one-way)", "일방통행", ["횡단보도", "차도"], "일방통행 = one-way traffic."), F("어떻게 가는지 좀 가르쳐 ___. (please tell me; informal)", "줘", ["주세요", "줬어"], "가르쳐 줘 is the informal request."),
           read_q("횡단보도"), read_q("일방통행"), read_q("연세대학교"), read_q("빨강버스"), read_q("충정로")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_SECS = [("Public transportation", _CV_PT), ("At the subway station", _CV_SUB), ("Traffic and transportation", _CV_TRF), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_ALL = [r for _, rows in _CV_SECS[:-1] for r in rows]
L12 = lesson(
    "Ch 14 · Core vocabulary and self-evaluation",
    "주요 단어 · 대중교통 · 지하철역 · 교통과 운송 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Optional parts, such as (~하다/되다), are kept in the meanings.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (1000원 → 천 원, 5번 출구 → 오 번 출구, 5명 → 다섯 명, 5분마다 → 오 분마다, 6시 → 여섯 시, 130,000원 → 십삼만 원); 몬트레이에서 PG로 → 몬트레이에서 피지로. The book’s related words (the synonyms, antonyms and related words in the last column) are not repeated. The book’s Additional Vocabulary table is empty: it is for your own words."),
    ] + [card(name, "Italicized English words in the book are grammatical terms, not the meaning of a Korean word." if name == "Other words" else "", tables=[vt(rows)]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: ask for information about public transportation; read subway line maps and signs to get around using the subway system; comprehend and respond to public announcements in the subway; read traffic signs; ask for and give directions; talk about public transportation in Korea.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -고 있다, which is used to express an action in progress; -기 바라다, which is used to give public instruction (please …); the conjunctive ending -(으)니까 (because); ㄷ irregular verbs; the Sino-Korean syllables 차 (車), 금 (禁), and 도 (道)."),
    ],
    exercises=uniq(
        vocab_exercises([(r[0], _en(r[0])) for r in _CV_ALL if not r[0].startswith(("~", "-", "(")) and "/" not in r[0]])
        + [M("What does the Sino-Korean syllable 차 (車) mean?", "a vehicle on wheels", ["a road; a way", "to forbid; to ban", "to ride"], "승용차, 자동차, 기차, 열차."), M("What does the Sino-Korean syllable 금 (禁) mean?", "to forbid; to abstain; to ban", ["a road; a way", "a vehicle on wheels", "to ride"], "금연, 출입 금지, 통행 금지."),
           M("What does the Sino-Korean syllable 도 (道) mean?", "a road; a way", ["to forbid", "a vehicle on wheels", "to ride"], "지하도, 고속도로, 차도."), M("What does ~대 count?", "electronics and vehicles", ["people", "books", "cups"], "텔레비전을 한 대."),
           M("What does ~마다 mean?", "each; every; per", ["only", "even", "about"], "오 분마다 = every five minutes."), M("What does ~씩 mean?", "each; respectively", ["every", "about", "only"], "한 병씩 = one bottle each."),
           M("What does ~행 mean?", "bound (for)", ["from", "via", "past"], "잠실행 열차 = a train bound for Jamsil."), M("What does ~ 호선 count?", "subway lines", ["train cars", "stations", "tickets"], "몇 호선 = which line."),
           M("What does -기(를) 바라다 express?", "A polite request or instruction (please …)", ["A past event", "A condition", "A purpose"], "-기 바랍니다 = please."), M("What does -(으)니까 mean?", "because", ["if", "although", "in order to"], "길이 막히니까 = because the road is congested."),
           M("What does -고 있다 express?", "An action in progress", ["A purpose", "A wish", "A reason"], "들어오고 있습니다 = is entering."), M("What does ~원 mean?", "won; Korean currency unit", ["dollar", "person", "floor"], "십삼만 원 = 130,000 won.")]
        + [read_q("주요 단어"), read_q("승강장"), read_q("전동차"), read_q("횡단보도"), read_q("지하도")]
    ),
)

UNIT = unit("Semester 1 · Unit 4 · Chapter 14: Public Transportation in Korea (한국의 대중 교통)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
