"""Unit 23: KBC Semester 1, Unit 4, Chapter 16 - Touring in Korea (한국에서 여행하기).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 4, Student's Edition (2022).
Audio, video clips, photos, maps, diagrams, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _B_IRR, _base_ao
from ko_unit21 import _kn, _won


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


_IRR = _B_IRR + ("더럽다", "뜨겁다", "차갑다", "무섭다", "외롭다", "아름답다")
_D_IRR = ("듣다", "걷다", "묻다", "싣다")


def _ao(verb):
    if verb in _IRR:
        st = stem(verb)
        l, v, t = _K.decompose(st[-1])
        return st[:-1] + _K.compose(l, v, "") + "워"
    return informal(verb)[:-1]


def _show(key):
    """the Korean word shown for a dictionary key such as '연기 (smoke)'"""
    return key.split(" (")[0] if " (" in key and not key.startswith("(") else key


# ---- the core vocabulary of Chapter 16 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_TRAVEL = [
    ("가능", "(可能) possibility (~하다: to be possible)", "출발 이십사 시간 전까지 취소가 가능합니다."),
    ("관광", "(觀光) a tour; sightseeing (~하다: to sightsee)", "방학 동안 유럽 관광을 할 거예요."),
    ("국내선", "(國內線) a domestic (air)line", "국내선 요금은 별로 안 비쌉니다."),
    ("날짜", "a date", "출발 날짜가 몇 월 며칠이에요?"),
    ("변경", "(變更) change (~하다/되다: to change/to be changed)", "공연 날짜는 변경될 수 있습니다."),
    ("불가능", "(不可能) impossibility (~하다: to be impossible)", "이 상품은 사용하시면 환불이 불가능합니다."),
    ("상품", "(商品) goods; merchandise; a product; “merchant item”", "백화점 상품이 시장보다 비싸요."),
    ("성인", "(成人) an adult", "미술관 입장료가 성인 만 원, 어린이 오천 원입니다."),
    ("어린이", "a child; a kid", f"한국에서 {month_ko(5)} {day_ko(5)}은 어린이날입니다."),
    ("여행사", "(旅行社) a travel agency", "어제 여행사에 전화해서 비행기표를 예약했습니다."),
    ("연기 (postponement)", "(延期) postponement; delay (~하다/되다: to postpone/to be postponed)", "시험 날짜가 이틀 연기되었습니다."),
    ("왕복", "(往復) a round-trip", "제주도 왕복 항공권을 예약하고 싶어요."),
    ("지불", "(支拂) payment (~하다/되다: to pay/to be paid)", "요금은 신용카드로 지불하겠습니다."),
    ("취소", "(取消) cancellation (~하다/되다: to cancel/to be canceled)", "출발 이십사 시간 전까지만 취소하실 수 있습니다."),
    ("편도", "(片道) a one-way (trip)", f"한국에서 샌프란시스코까지 편도 비행기표 값은 {_kn(750000)} 원입니다."),
    ("포함", "(包含) inclusion (~하다/되다: to include/to be included)", "여행 요금에 호텔과 아침 식사가 포함되어 있습니다."),
    ("현금", "(現金) cash", "저희 가게는 현금만 받습니다."),
    ("환불", "(還拂) a refund; return; reimbursement (~하다/되다: to refund/to be refunded)", "이 옷 한달 전에 샀는데 환불돼요?"),
    ("휴게소", "(休憩所) a rest stop; a rest area", "부산 가는 길에 휴게소에서 잠깐 쉬었어요."),
]
_CV_RENT = [
    ("대형", "(大型) full-size; “big type”", "짐이 많아서 대형차를 빌렸습니다."),
    ("돌려주다", "to return", "빌린 책을 도서관에 돌려주었습니다."),
    ("보험", "(保險) insurance", "운전을 하려면 자동차 보험이 있어야 합니다."),
    ("소형", "(小型) small-size; “small type”", "일본은 소형차를 많이 만듭니다."),
    ("수동식", "(手動式) manual; a manual shift", "나는 수동식 차를 운전할 줄 모릅니다."),
    ("자동식", "(自動式) automatic; an automatic shift", "자동식 차는 운전하기가 쉽습니다."),
    ("중형", "(中型) medium-size; “middle type”", "중형차는 가족이 있는 사람들이 좋아합니다."),
    ("열쇠 / 키", "a key", "열쇠가 없어서 문을 열 수 없습니다."),
    ("운전면허증", "(運轉免許證) a driver’s license (certificate)", "운전을 하려면 운전면허증이 있어야 합니다."),
    ("원하다", "to want; to hope; to wish", "손님, 어떤 자동차를 원하십니까?"),
]
_CV_REPAIR = [
    ("견인차", "(牽引車) a tow truck", "차가 고속도로에서 섰어요. 그래서 견인차를 불렀습니다."),
    ("고장", "(故障) malfunction (~나다: to malfunction; to break down)", "갑자기 컴퓨터가 고장 나서 숙제를 못 했어요."),
    ("고치다", "to repair; to fix", "고장 난 텔레비전을 오늘 고쳤어요."),
    ("서다", "to come to a stop; to stall; to stand up", "갑자기 시동이 꺼지면서 차가 섰습니다."),
    ("시동", "(始動) starting (an engine); “start moving” (~걸다: to start an engine)", "차 배터리가 나가서 시동이 걸리지 않습니다."),
    ("연기 (smoke)", "(煙氣) smoke (~나다: to smoke)", "방 안에 연기가 찼어요."),
    ("정비소", "(整備所) an auto repair shop; a maintenance shop", "고장난 차를 고치러 정비소에 갔습니다."),
]
_CV_BUD = [
    ("불교", "(佛敎) Buddhism", "한국은 옛날에 불교 국가였어요."),
    ("~사", "(寺) a Buddhist temple", "불국사와 해인사는 유명한 절입니다."),
    ("절", "a Buddhist temple", "불국사는 오래된 절입니다."),
    ("탑", "(塔) a pagoda; a tower; a steeple", "불국사에 가면 탑이 있습니다."),
]
_CV_TOUR = [
    ("경치", "(景致) a scene; scenery", "몬트레이는 아름다운 경치로 유명합니다."),
    ("~궁", "(宮) a palace", "프랑스에 가면 베르사이유 궁을 구경하고 싶어요."),
    ("명소", "(名所) a famous tourist attraction; a well-known spot", "엠파이어 스테이트 빌딩은 뉴욕의 관광명소입니다."),
    ("문화재", "(文化財) a cultural asset; a cultural property", "경주 박물관에는 중요한 문화재가 많습니다."),
    ("온천", "(溫泉) a hot spring; “a warm spring”", "온천에 가고 싶으시면 팜스프링스에 가세요."),
    ("유적지", "(遺跡地) a historic site", "페루에는 잉카 유적지가 있습니다."),
]
_CV_OTH = [
    ("갑자기", "suddenly", "퇴근 길에 갑자기 눈이 내려서 길이 막혔어요."),
    ("경험", "(經驗) an experience (~하다: to experience)", "여행을 하면 많은 경험을 할 수 있어요."),
    ("낮", "the daytime; day", "겨울에는 낮이 짧고 밤이 길어요."),
    ("-네요", "exclamatory verb ending", "아이가 아주 예쁘네요!"),
    ("-(는)군요", "exclamatory verb ending", "오늘은 날씨가 참 좋군요!"),
    ("마지막", "the last; the end; the final", "교실에서 마지막으로 나가는 사람이 컴퓨터를 끄세요."),
    ("멋있다", "to be cool/awesome; to be handsome; to be stylish", "파리의 에펠탑은 정말 멋있습니다."),
    ("세계적", "(世界的) world-renowned; worldwide", "타이거 우즈는 세계적으로 유명한 골프 선수입니다."),
    ("아무 ~(이)나", "any ~; anyone", "전 아무 음식이나 잘 먹어요. 이 영화는 아무나 볼 수 있어요."),
    ("역사", "(歷史) history", "한국의 역사는 약 오천 년 전에 시작되었습니다."),
    ("옛날", "old days; the past", "할머니들은 옛날 이야기를 잘 해 주십니다."),
    ("-(으)면서", "while doing (something) simultaneously; while being", "저는 보통 운전하면서 음악을 듣습니다."),
    ("-(으)ㄹ 줄 모르다", "to not know how to do something", "저는 한국말을 할 줄 몰라요."),
    ("-(으)ㄹ 줄 알다", "to know how to do something", "최 상병은 일본어를 할 줄 알아요."),
    ("짓다", "to build", "신라 때 절을 많이 지었어요."),
]
_CV_LOAN = [
    ("렌터카 / 렌트카", "a rental car", "공항 렌터카 사무실에서 차를 빌렸어요."),
    ("밧데리 / 배터리", "a battery", "밧데리가 오래돼서 시동이 잘 안 걸려요."),
    ("엔진", "an engine", "자동차 엔진에서 연기가 나요."),
    ("키", "a key", "키가 없어서 문을 열 수 없습니다."),
    ("펑크", "a puncture (~나다: to have a flat tire)", "아침에 타이어가 펑크 났습니다."),
]
_CV_SINO = [
    ("불 / 부", "(不) not; no; non-; in-; im-; il-; ir-", "불편, 불법, 불가능, 불합격"),
    ("적", "(的) -ic; -ive; a suffix that changes a noun into an adjective", "역사적, 인상적, 세계적"),
    ("형", "(型) a type; a model", "소형, 중형, 신형, 구형"),
]
_ALL = {r[0]: r for r in _CV_TRAVEL + _CV_RENT + _CV_REPAIR + _CV_BUD + _CV_TOUR + _CV_OTH + _CV_LOAN}
_EXTRA = {"대형차": "a full-size car (mine)", "소형차": "a small car (mine)", "중형차": "a medium-size car (mine)", "비행기표": "a plane ticket (mine)", "패키지": "a package (mine)", "신용카드": "a credit card (mine)", "항공편": "a flight; air service (mine)", "출발": "departure (~하다: to depart) (mine)",
          "버스 관광": "a bus tour (mine)", "예약": "a reservation (mine)", "렌터카": "a rental car"}


def _en(word):
    if word in _EXTRA:
        return _EXTRA[word]
    t = _re.sub(r"^\([^)]*(\([^)]*\))?[^)]*\) ", "", _ALL[word][1])
    return _clean(_re.sub(r" \(~[^)]*\)", "", t))


def _pairs(words):
    return [(_show(w), _en(w)) for w in words]


def _rows(words):
    return [(_show(w), _EXTRA[w] if w in _EXTRA else _ALL[w][1]) for w in words]


# ================================================================== Objectives and the Sino-Korean syllables
_BUL = [("불법", "illegal; “not law”"), ("불친절", "unkindness; “not kind”"), ("불합격", "failure in an entrance exam; “not passing”"), ("불면증", "insomnia; “no sleeping symptom”"), ("불편", "inconvenience; discomfort (the book’s example in the Core Vocabulary)"),
        ("불가능", "impossibility (the book’s example in the Core Vocabulary)"), ("부동산", "immovable property"), ("부주의", "carelessness; “no attention”"), ("부족하다", "to be insufficient")]
_HYUNG = [("소형", "small-size; “small type”"), ("구형", "old type"), ("원형", "a prototype; “original type”"), ("대형", "full-size; “big type”"), ("중형", "medium-size; “middle type”"), ("신형", "a new type (mine)")]
_JEOK = [("목적", "a goal; “eye target”"), ("적중", "hitting the bull’s eye; “middle of target”"), ("역사적", "historic; historical"), ("인상적", "impressive"), ("한국적", "unique to Korea"), ("일시적", "temporary; “of one time”"),
         ("세계적", "world-renowned; worldwide"), ("미국적", "American; typical of America (mine)"), ("부분적", "partial; “of a part” (mine)")]
L1 = lesson(
    "Ch 16 · What the chapter teaches and the Sino-Korean syllables 불/부, 형 and 적",
    "한국에서 여행하기 · 불/부 (不) · 형 (型) · 적 (的) · 불법 · 소형 · 역사적",
    requires=[],
    cards=[
        card("What Chapter 16 teaches (한국에서 여행하기)",
             "Chapter 16, “Touring in Korea”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: make a domestic flight reservation; ask for and give information about a travel package; ask for and give information about renting a car; report simple car problems; identify simple automotive parts; and talk about well-known tourist attractions in Korea.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; 아무나 or 아무 ~(이)나 in the affirmative (any ~) and in the negative (not just any ~); -(으)ㄹ 줄 알다 (know how to) and -(으)ㄹ 줄 모르다 (not know how to); the exclamatory verb endings -군요 and -네요; the conjunctive ending -(으)면서, used to express simultaneous actions or conditions; and the Sino-Korean syllables 불/부 (不), 적 (的), and 형 (型)."),
        card("Sino-Korean in use: 불/부 (不)",
             "This Sino-Korean syllable means not or no and functions like the English prefixes in-, im-, il-, and ir-, as in inability, impossible, illegal, and irregular; for example, 불법 (illegal; “not law”), 불친절 (unkindness; “not kind”), 불합격 (failure in entrance exam; “not passing”), and 불면증 (insomnia; “no sleeping symptom”). 불 changes into 부 when the syllable comes before the consonant ㄷ or ㅈ, as in 부동산 (immovable property), 부주의 (carelessness; “no attention”), and 부족하다 (to be insufficient).",
             tables=[table(["Word", "Meaning"], [list(r) for r in _BUL], say=[0])]),
        card("Sino-Korean in use: 형 (型)",
             "This Sino-Korean syllable means type or model, as in 소형 (small-size; “small type”), 구형 (old type), and 원형 (prototype; “original type”). The book asks you to guess the meaning of 대형, 중형 and 신형; the answers are the book’s own meanings of the Core Vocabulary (대형, 중형) and mine (신형).",
             tables=[table(["Word", "Meaning"], [list(r) for r in _HYUNG], say=[0])]),
        card("Sino-Korean in use: 적 (的)",
             "This Sino-Korean syllable normally means a target, as in 목적 (goal; “eye target”) and 적중 (hitting the bull’s eye; “middle of target”). However, when 적 (的) is attached to a Sino-Korean noun, it functions as an “adjective maker,” just like the English suffixes -ic or -ive, as in realistic, historic, creative, active, etc. When used this way, 적 can be translated as “of (the noun)”; for example, 역사적 (historic; historical), 인상적 (impressive), 한국적 (unique to Korea), 일시적 (temporary; “of one time”). The book asks you to guess the meaning of 세계적, 미국적 and 부분적; the answer for 세계적 is the book’s (world-renowned; worldwide), the others are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _JEOK], say=[0])]),
        card("Vocabulary Builder, Activity 4: a model sentence",
             "In the book’s “Be a creative writer!” activity you receive two word strips and make a sentence with the two words. The book’s model: the words 예약 and 취소 give the sentence 호텔 예약을 취소했어요. (I canceled the hotel reservation. The English is mine.)",
             examples=[D("호텔 예약을 취소했어요.", "I canceled the hotel reservation.")]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1–3 (SMART Board activities) and the class steps of Activity 4 (posting the sentences on the wall and correcting them) are picture, game or class activities."),
    ],
    exercises=uniq(
        _tr(_BUL + _HYUNG + _JEOK)
        + [M(f"Which word means “{b.split(';')[0].replace(' (mine)', '')}”?", a, [x for x, _ in (_BUL + _HYUNG + _JEOK) if x != a][:3], f"{a}: {b}.") for a, b in (_BUL[:4] + _HYUNG[:5] + _JEOK[:6])]
        + [M("What does the Sino-Korean syllable 불/부 (不) mean?", "not; no", ["type; model", "target", "sea"], "불법 = illegal; “not law”."), M("What does the Sino-Korean syllable 형 (型) mean?", "type; model", ["not; no", "target", "a room"], "소형 = small type."),
           M("What does 적 (的) do when it is attached to a Sino-Korean noun?", "It makes an adjective (-ic; -ive)", ["It makes a verb", "It negates the noun", "It makes a place"], "역사적, 인상적, 세계적."), M("When does 불 change into 부?", "Before the consonants ㄷ and ㅈ", ["Before ㅂ and ㅁ", "Before vowels", "After a final consonant"], "부동산, 부주의, 부족하다."),
           M("Which word contains the changed form 부 of 不?", "부주의", ["불법", "불편", "불가능"], "불 → 부 before ㅈ."), M("Which English prefixes does 不 work like?", "in-, im-, il-, ir-", ["re-, pre-, con-", "pro-, anti-, sub-", "co-, ex-, de-"], "inability, impossible, illegal, irregular."),
           M("What does 목적 literally mean?", "“eye target”", ["“goal eye”", "“big type”", "“not law”"], "목적 = goal; “eye target”."), M("Which pair of words contains 형 (型)?", "소형 and 대형", ["소형 and 세계적", "불법 and 대형", "역사적 and 중형차"], "소형, 중형, 대형, 신형, 구형."),
           M("How do you say “I canceled the hotel reservation”?", "호텔 예약을 취소했어요.", ["호텔 예약을 포함했어요.", "호텔 예약을 지불했어요.", "호텔 예약을 환불했어요."], "취소하다 = to cancel."),
           read_q("불법"), read_q("불합격"), read_q("소형"), read_q("역사적"), read_q("호텔 예약을 취소했어요")]
    ),
)

# ================================================================== Topic A
_A_DLG = [
    ("앤더슨 상병", "경주로 여행 가고 싶어요. 어떤 여행 상품이 있어요?", "I want to travel to Gyeongju. What kind of travel packages are there?"),
    ("여행사 직원", f"네, 이 박 삼 일 패키지 상품이 있어요. 성인은 일 인당 {_kn(200000)} 원이에요.", "Yes, there is a 2-night, 3-day package. For an adult it is 200,000 won per person."),
    ("앤더슨 상병", "그 상품에 무엇이 포함됩니까?", "What is included in that package?"),
    ("여행사 직원", "네, 왕복 항공편, 호텔, 버스 관광이 다 포함됩니다.", "Yes, the round-trip flight, the hotel and the bus tour are all included."),
    ("앤더슨 상병", "그래요? 그런데, 관광은 렌터카로 하고 싶어요.", "Is that so? But I want to do the sightseeing by rental car."),
    ("여행사 직원", f"아, 그러세요? 그럼 비행기표하고 호텔만 예약하세요. 이 박 삼 일에 일 인당 {_kn(150000)} 원이에요.", "Oh, I see. Then book only the plane ticket and the hotel. For 2 nights and 3 days it is 150,000 won per person."),
    ("앤더슨 상병", "언제 출발합니까?", "When does it depart?"),
    ("여행사 직원", "매주 금요일 아침에 떠납니다.", "It leaves every Friday morning."),
    ("앤더슨 상병", "네, 좋아요.", "Yes, that’s good."),
    ("여행사 직원", "그런데, 예약하시면 취소와 환불이 불가능합니다.", "However, if you make a reservation, cancellation and refund are impossible."),
    ("앤더슨 상병", "그래요? 그럼, 날짜는 바꿀 수 있어요?", "Is that so? Then can I change the date?"),
    ("여행사 직원", "네, 출발 사십팔 시간 전까지 변경이 가능합니다.", "Yes, a change is possible until 48 hours before departure."),
    ("앤더슨 상병", "네, 알겠습니다. 예약해 주세요.", "Yes, I understand. Please make the reservation."),
    ("여행사 직원", f"그럼, {_kn(150000)} 원 되겠습니다. 어떻게 지불하시겠어요?", "Then it will be 150,000 won. How will you pay?"),
    ("앤더슨 상병", "신용카드 받으세요?", "Do you accept credit cards?"),
    ("여행사 직원", "네, 신용카드와 현금 다 받습니다.", "Yes, we accept both credit cards and cash."),
]
_A_WORDS = ["가능", "관광", "국내선", "날짜", "렌터카 / 렌트카", "변경", "불가능", "상품", "성인", "어린이", "여행사", "연기 (postponement)", "왕복", "지불", "취소", "편도", "포함", "현금", "환불"]
L2 = lesson(
    "Ch 16 · Topic A: At a travel agency",
    "여행사에서 · 여행 상품 · 왕복 항공편 · 취소와 환불 · 변경이 가능합니다",
    requires=[],
    cards=[
        card("Topic A: At a travel agency (여행사에서)",
             "SPC Anderson is making a reservation at a travel agency for his trip to Gyeongju. (The English is mine; the book gives none. The book writes 2박 3일, 1인당 20만 원, 15만 원 and 48시간; they are spelled out here.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Reading “2박 3일”",
             "2박 3일 (“two nights and three days”) is read 이 박 삼 일 (Sino-Korean numbers for the nights and the days), and 1인당 (“per person”) is read 일 인당. (The reading and the English are mine.)",
             tables=[ktable([("이 박 삼 일", "two nights and three days (mine)"), ("일 인당", "per person (mine)"), ("매주 금요일", "every Friday (mine)")])]),
        card("Activities left out",
             "The SMART Board activities, Follow-up Activity 2 (listening to three phone conversations in which a customer makes a flight reservation and asks about things that can be changed, and filling in a table) and the Presentation Activity’s pair role-play and class performance are audio, computer, partner or class activities. Follow-up 1 is in the next lesson. The Useful Links (four travel agencies) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if "/" not in w]))
        + _tr(_strip(_A_DLG)[:14])
        + [M("Where does SPC Anderson want to travel?", "Gyeongju", ["Jeju", "Busan", "Seoul"], "경주로 여행 가고 싶어요."), M("How long is the package?", "Two nights and three days", ["Three nights and two days", "One day", "One week"], "이 박 삼 일."),
           M("How much is the package for an adult?", "200,000 won per person", ["150,000 won per person", "250,000 won per person", "20,000 won per person"], "일 인당 이십만 원."), M("What is included in the package?", "A round-trip flight, a hotel and a bus tour", ["Only a hotel", "Meals and a rental car", "Only the flight"], "왕복 항공편, 호텔, 버스 관광."),
           M("How does Anderson want to do the sightseeing?", "By rental car", ["By bus tour", "By taxi", "On foot"], "관광은 렌터카로 하고 싶어요."), M("What does the agent suggest then?", "Booking only the plane ticket and the hotel", ["Another city", "A cheaper bus tour", "No reservation"], "비행기표하고 호텔만 예약하세요."),
           M("How much is the plane ticket and hotel package?", "150,000 won per person", ["200,000 won per person", "250,000 won per person", "50,000 won per person"], "일 인당 십오만 원."), M("When does it depart?", "Every Friday morning", ["Every Monday morning", "Every day", "Every Friday night"], "매주 금요일 아침에 떠납니다."),
           M("What is impossible once you make a reservation?", "Cancellation and refund", ["Payment by card", "Departure on Friday", "Hotel use"], "취소와 환불이 불가능합니다."), M("Until when can the date be changed?", "Until 48 hours before departure", ["Until the day before", "Until one week before", "Never"], "출발 사십팔 시간 전까지 변경이 가능합니다."),
           M("How can Anderson pay?", "By credit card or cash", ["Cash only", "Credit card only", "By check"], "신용카드와 현금 다 받습니다."), M("How many won does Anderson pay in the end?", "150,000 won", ["200,000 won", "250,000 won", "15,000 won"], "십오만 원 되겠습니다."),
           F("성인은 일 ___ 이십만 원이에요. (per person)", "인당", ["명당", "사람이"], "1인당 = per person."), F("그 상품에 무엇이 ___됩니까? (included)", "포함", ["취소", "환불"], "포함되다 = to be included."), F("예약하시면 취소와 ___이 불가능합니다. (refund)", "환불", ["포함", "현금"], "환불 = a refund."),
           F("출발 사십팔 시간 전까지 변경이 ___합니다. (possible)", "가능", ["불가능", "취소"], "가능하다 = to be possible."), F("신용카드와 ___ 다 받습니다. (cash)", "현금", ["성인", "상품"], "현금 = cash."), F("어떻게 ___하시겠어요? (pay)", "지불", ["취소", "연기"], "지불하다 = to pay."),
           M("What does 왕복 mean?", "a round-trip", ["a one-way trip", "a domestic line", "a refund"], "왕복 항공편 = a round-trip flight."), M("What does 편도 mean?", "a one-way trip", ["a round-trip", "a domestic line", "cash"], "편도 = a one-way trip."),
           read_q("여행사"), read_q("왕복 항공편"), read_q("취소와 환불"), read_q("변경이 가능합니다"), read_q("신용카드")]
    ),
)

# ================================================================== Activities A
_JEJU_AD = [
    ("고품격 제주 일주 여행", "A high-class round-the-island trip to Jeju"),
    ("여행기간 (이 박 삼 일)", "Trip duration (2 nights and 3 days)"),
    ("매주 화요일 아홉 시 출발", "Departs every Tuesday at 9:00"),
    ("포함 비용", "Included expenses"),
    ("왕복 항공", "Round-trip flight"), ("신라호텔 이 박", "Shilla Hotel, 2 nights"), ("아침 식사 두 번", "Breakfast, 2 times"), ("점심 식사 두 번", "Lunch, 2 times"), ("관광지 입장료", "Admission fees to tourist attractions"),
    ("불포함 비용", "Excluded expenses"),
    ("저녁식사", "Dinner"), ("옵션 관광", "Optional tours"),
    ("상품 가격", "Price of the package"),
    (f"성인 (십이 세 이상) {_kn(375000)} 원", "Adult (12 years old and above): 375,000 won"),
    (f"어린이 (십이 세 미만) {_kn(320000)} 원", "Child (under 12 years old): 320,000 won"),
    ("이 상품은 취소와 환불이 불가능합니다.", "For this package, cancellation and refund are impossible."),
    ("예약 날짜 변경 시 여행 요금의 십 퍼센트를 더 내셔야 합니다.", "If you change the reservation date, you have to pay 10% of the trip fare more."),
]
_NOTICE = [
    ("예약하신 후 출발 사십팔 시간 전까지만 환불이 가능합니다.", "After you make the reservation, a refund is possible only until 48 hours before departure."),
    ("국내선 편도 비행기표는 날짜 변경이 불가능합니다.", "For a domestic one-way plane ticket, changing the date is impossible."),
    ("탑승 세 시간 전에 공항에 나오시면 원하시는 좌석에 앉으실 수 있습니다.", "If you come out to the airport three hours before boarding, you can sit in the seat you want."),
]
_AD_W = [("탑승", "boarding (mine)"), ("좌석", "a seat (mine)"), ("입장료", "an admission fee (mine)"), ("옵션 관광", "an optional tour (mine)"), ("일주", "a trip around (mine)"), ("이상", "~ and above (the book’s note)"), ("미만", "under ~ (the book’s note)"), ("무료", "free of charge (mine)")]
L3 = lesson(
    "Ch 16 · Activities A: a travel package and a flight notice",
    "제주 일주 여행 · 포함 비용 · 불포함 비용 · 환불이 가능합니다 · 날짜 변경이 불가능합니다",
    requires=[],
    cards=[
        card("Topic A, Follow-up 1 (Reading): the Jeju travel advertisement",
             "The book shows a travel advertisement and asks you to fill in a table in English with information about the travel package (destination, trip duration, included expenses, excluded expenses, price, terms and conditions). The text is the book’s (the figures are spelled out in Hangul, the web address is left out; the book writes 취소/환불 불가능합니다, here 취소와 환불이 불가능합니다); the English is mine. The book’s note: ~ 이상 means “~ and above” and ~미만 means “under ~”.",
             examples=passage(_JEJU_AD)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Destination", "Jeju"], ["Trip duration", "2 nights and 3 days; departs every Tuesday at 9:00"], ["Included expenses", "Round-trip flight; 2 nights at the Shilla Hotel; 2 breakfasts; 2 lunches; admission fees to tourist attractions"], ["Excluded expenses", "Dinner; optional tours"],
                                                                 ["Price", "Adult (12 and above): 375,000 won; child (under 12): 320,000 won"], ["Terms & conditions", "No cancellation or refund; changing the reservation date costs 10% of the trip fare more"]])]),
        card("Activity 2b (Reading): a notice about the conditions of a domestic flight",
             "A customer who has made a reservation for a domestic flight receives a notice about the conditions and requirements. The book asks you to read the three sentences and write their English translations; the sentences are the book’s (the figures are spelled out in Hangul), the translations are mine.",
             examples=passage(_NOTICE)),
        card("Words of the two texts",
             "The book glosses only ~ 이상 and ~미만; the other meanings are mine.",
             tables=[ktable(_AD_W)]),
        card("Activities left out",
             "Activity 1 (SMART Board reading and listening activities), Activity 2a (listening to three dialogs between a travel agent and a customer about what is and is not possible and filling in a table) and Activity 3 (a role-play at a travel agency in Seoul: filling out the reservation forms and acting out three situation cards for a domestic flight reservation, a change and a cancellation) are audio, computer, form or role-play activities."),
    ],
    exercises=uniq(
        _tr(_JEJU_AD[1:3] + _JEJU_AD[4:9] + _JEJU_AD[10:12] + _JEJU_AD[13:] + _NOTICE + _AD_W)
        + [M("Where is the trip in the advertisement?", "Jeju", ["Gyeongju", "Seoul", "Busan"], "제주 일주 여행."), M("On which day of the week does the trip depart?", "Tuesday", ["Friday", "Monday", "Sunday"], "매주 화요일 아홉 시 출발."), M("How many nights does the trip last?", "Two nights", ["Three nights", "One night", "Five nights"], "이 박 삼 일."),
           M("Which is included in the price?", "A round-trip flight", ["Dinner", "Optional tours", "A rental car"], "왕복 항공 is under 포함 비용."), M("Which is NOT included in the price?", "Dinner", ["Breakfast", "Lunch", "Admission fees"], "저녁식사 is under 불포함 비용."), M("How many lunches are included?", "Two", ["One", "Three", "None"], "점심 식사 두 번."),
           M("How much is the trip for an adult?", "375,000 won", ["320,000 won", "250,000 won", "12,000 won"], "성인 삼십칠만 오천 원."), M("How much is the trip for a child under 12?", "320,000 won", ["375,000 won", "250,000 won", "12,000 won"], "어린이 삼십이만 원."),
           M("What happens if you change the reservation date?", "You pay 10% of the trip fare more", ["Nothing", "You pay half", "You cannot change the date"], "여행 요금의 십 퍼센트를 더 내셔야 합니다."), M("Can you get a refund on the Jeju package?", "No, cancellation and refund are impossible", ["Yes, anytime", "Yes, within 48 hours", "Only for children"], "취소와 환불이 불가능합니다."),
           M("Until when is a refund possible according to the notice?", "Until 48 hours before departure", ["Until 3 hours before boarding", "Until the day after", "Anytime"], "출발 사십팔 시간 전까지만 환불이 가능합니다."), M("What is impossible for a domestic one-way ticket?", "Changing the date", ["Boarding", "Paying", "Buying"], "날짜 변경이 불가능합니다."),
           M("When should you come to the airport to get the seat you want?", "Three hours before boarding", ["One hour before boarding", "The day before", "At boarding time"], "탑승 세 시간 전에 공항에 나오시면."),
           F("이 상품은 취소와 환불이 ___합니다. (impossible)", "불가능", ["가능", "포함"], "불가능 = impossibility."), F("___ 비용에는 저녁식사와 옵션 관광이 있습니다. (excluded)", "불포함", ["포함", "가능"], "불포함 = not included."), F("성인 (십이 세 ___) 삼십칠만 오천 원 (and above)", "이상", ["미만", "이하"], "이상 = and above."),
           F("어린이 (십이 세 ___) 삼십이만 원 (under)", "미만", ["이상", "이하"], "미만 = under."), F("국내선 편도 비행기표는 날짜 변경이 ___합니다. (impossible)", "불가능", ["가능", "포함"], "불가능하다."), F("예약하신 후 출발 사십팔 시간 전까지만 환불이 ___합니다. (possible)", "가능", ["불가능", "포함"], "가능하다."),
           read_q("제주 일주 여행"), read_q("포함 비용"), read_q("불포함 비용"), read_q("환불이 가능합니다"), read_q("좌석")]
    ),
)

# ================================================================== Topic B
_B_DLG = [
    ("앤더슨 상병", "저… 차를 좀 빌리고 싶어요.", "Um… I would like to rent a car."),
    ("렌터카 직원", "네, 며칠 동안 쓰실 겁니까?", "Yes, for how many days will you use it?"),
    ("앤더슨 상병", "오늘부터 삼 일 동안 빌리고 싶어요.", "I want to rent it for three days from today."),
    ("렌터카 직원", "어떤 차를 원하세요?", "What kind of car do you want?"),
    ("앤더슨 상병", "아무 차나 괜찮아요. 저는 수동식도 운전할 줄 알아요.", "Any car is fine. I know how to drive a manual one, too."),
    ("렌터카 직원", "네, 잠시만요. 손님, 소형차도 괜찮으세요?", "Yes, just a moment. Sir, is a small car also OK?"),
    ("앤더슨 상병", "네, 괜찮아요.", "Yes, that’s fine."),
    ("렌터카 직원", "그럼 소형차로 드리겠습니다. 운전면허증 있으세요?", "Then I will give you a small car. Do you have a driver’s license?"),
    ("앤더슨 상병", "네, 국제 운전면허증도 괜찮습니까?", "Yes, is an international driver’s license also OK?"),
    ("렌터카 직원", f"그럼요. 보험 포함해서 모두 {_kn(250000)} 원입니다.", "Of course. Including insurance, it is 250,000 won in total."),
    ("앤더슨 상병", "예. 그런데, 차는 몇 시까지 돌려주어야 합니까?", "Okay. By the way, by what time do I have to return the car?"),
    ("렌터카 직원", "낮 열두 시까지 차 열쇠하고 같이 돌려주시면 됩니다.", "You can return it with the car key by 12 o’clock in the daytime."),
    ("앤더슨 상병", "그런데 차가 고장 나면 어떻게 해야 하나요?", "But what should I do if the car breaks down?"),
    ("렌터카 직원", "저희 회사에 전화해 주세요. 그럼 저희가 정비소에 연락해서 견인차를 보내드립니다.", "Please call our company. Then we will contact the repair shop and send a tow truck."),
]
_B_WORDS = ["갑자기", "견인차", "고장", "고치다", "낮", "대형", "돌려주다", "밧데리 / 배터리", "보험", "서다", "소형", "수동식", "시동", "아무 ~(이)나", "엔진", "연기 (smoke)", "열쇠 / 키", "운전면허증", "원하다", "-(으)ㄹ 줄 모르다", "-(으)ㄹ 줄 알다", "자동식", "정비소", "중형", "펑크", "휴게소"]
_PARTS = [("엔진", "an engine"), ("브레이크", "a brake"), ("방향 지시등 / 깜빡이", "signal lights"), ("밧데리", "a battery"), ("엑셀", "an accelerator"), ("핸들 / 운전대", "the steering wheel; 핸들 is “handle”"), ("백미러", "a rear-view mirror; “back mirror”"), ("본네트", "the hood"), ("타이어 / 바퀴", "a tire"), ("펑크나다 / 빵꾸나다", "to have a flat tire")]
L4 = lesson(
    "Ch 16 · Topic B: I would like to rent a car",
    "차를 빌리고 싶은데요 · 렌터카 · 소형차 · 운전면허증 · 보험 · 견인차 · 자동차 부속품",
    requires=[],
    cards=[
        card("Topic B: I would like to rent a car (차를 빌리고 싶은데요)",
             "SPC Anderson is renting a car at the Ulsan airport. (The English is mine; the book gives none. The book writes 3일, 25만 원 and 낮 12시; they are spelled out here.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened. The book lists 시동 (걸다), 고장 (나다), 연기 (나다) and 펑크 (나다) with the verb in brackets. 연기 here is “smoke” (煙氣), not “postponement” (延期).",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Automobile parts (자동차 부속품)",
             "The book labels the parts of a car in a picture. The Korean words and the English glosses are the book’s; the book’s footnote says that 펑크나다/빵꾸나다 (flat tire): “This word is not standard Korean (nor is it found in a dictionary), yet it is commonly used to describe a flat tire.” (The footnote belongs to 빵꾸나다.)",
             tables=[ktable(_PARTS)]),
        card("Cultural notes: 휴게소 (highway rest stops)",
             "All highways in Korea charge a toll, and drivers who leave the highway are charged again to re-enter. Thus, the Korea Expressway Corporation provides rest stops on the highways for the convenience of drivers so they don’t have to exit the highway for basic services. Therefore, if you are on a highway in Korea, you will see many 휴게소 signs. The literal translation of 휴게소 is a rest place. It is a public rest area or service area where drivers and passengers can rest, eat, refuel, and shop. Most of these rest areas have good food courts, coffee shops, convenience stores, and even auto repair shops. These days, many rest areas offer additional services such as batting cages, spas, lodging, and other amenities."),
        card("Activities left out",
             "The SMART Board activities, the Presentation Activity’s pair reading of the dialog, Follow-up 2 (listening to four phone conversations in which a driver describes a car problem to an auto repair shop, and filling in the type of problem) and the website link of the rest stops are audio, computer, partner or website activities. Follow-up 1 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("-", "아무")) and "/" not in w]))
        + _tr(_strip(_B_DLG)[:13]) + _tr(_PARTS)
        + [M("Where is SPC Anderson renting a car?", "At the Ulsan airport", ["At the Incheon airport", "In Gyeongju", "In Seoul"], "SPC Anderson is renting a car at the Ulsan airport."), M("For how many days does he want to rent it?", "Three days", ["One day", "Two days", "A week"], "오늘부터 삼 일 동안."),
           M("What kind of car does he say is fine?", "Any car", ["Only a big car", "Only a small car", "An automatic car only"], "아무 차나 괜찮아요."), M("What can Anderson drive?", "A manual car, too", ["Only automatic cars", "No cars", "Only trucks"], "수동식도 운전할 줄 알아요."),
           M("What kind of car does the agent give him?", "A small car", ["A medium-size car", "A full-size car", "A truck"], "소형차로 드리겠습니다."), M("Which license does Anderson have?", "An international driver’s license", ["A Korean license", "No license", "A student license"], "국제 운전면허증."),
           M("How much is the rental in total?", "250,000 won, including insurance", ["150,000 won", "200,000 won without insurance", "25,000 won"], "보험 포함해서 모두 이십오만 원."), M("By when must he return the car?", "By 12 o’clock in the daytime, with the key", ["By evening", "By 9 a.m.", "Tomorrow"], "낮 열두 시까지 차 열쇠하고 같이."),
           M("What should he do if the car breaks down?", "Call the rental company", ["Call the police", "Fix it himself", "Leave it"], "저희 회사에 전화해 주세요."), M("Who will the company contact?", "An auto repair shop, which sends a tow truck", ["The airport", "A hotel", "A taxi company"], "정비소에 연락해서 견인차를 보내드립니다."),
           M("What is a 휴게소?", "A rest stop on a highway", ["A toll gate", "A gas pump", "A police station"], "휴게소 = a rest stop; a rest area."), M("Why are there rest stops on Korean highways?", "Drivers who exit are charged the toll again", ["Highways are free", "Cars must stop every hour", "To check licenses"], "Drivers who leave the highway are charged again to re-enter."),
           F("저… 차를 좀 ___ 싶어요. (rent)", "빌리고", ["돌려주고", "고치고"], "빌리다 = to borrow; to rent."), F("그럼 ___로 드리겠습니다. (small car)", "소형차", ["대형차", "수동식"], "소형차 = a small car."), F("보험 ___해서 모두 이십오만 원입니다. (including)", "포함", ["취소", "연기"], "포함하다 = to include."),
           F("차는 몇 시까지 ___주어야 합니까? (return)", "돌려", ["고쳐", "서"], "돌려주다 = to return."), F("차가 ___ 나면 어떻게 해야 하나요? (breaks down)", "고장", ["연기", "시동"], "고장 나다 = to break down."), F("정비소에 연락해서 ___를 보내드립니다. (tow truck)", "견인차", ["열쇠", "엔진"], "견인차 = a tow truck."),
           F("저는 수동식도 운전할 ___ 알아요. (know how to)", "줄", ["수", "것"], "-(으)ㄹ 줄 알다 = to know how to."), F("어떤 차를 ___ 하세요? (want; the agent asks politely)", "원", ["고장", "시동"], "원하다 = to want."),
           M("Which part is “the hood”?", "본네트", ["엔진", "브레이크", "엑셀"], "본네트 = the hood."), M("Which part is “the accelerator”?", "엑셀", ["브레이크", "핸들", "백미러"], "엑셀 = an accelerator."), M("Which part is “a rear-view mirror”?", "백미러", ["핸들", "타이어", "엔진"], "백미러 = “back mirror”."),
           read_q("렌터카"), read_q("운전면허증"), read_q("견인차"), read_q("휴게소"), read_q("자동차 부속품")]
    ),
)

# ================================================================== Activities B
_RENT_AD = [
    ("한국 렌트카", "Hanguk Rent-a-Car"),
    ("소형차, 중형차, 대형차 모두 있습니다.", "Small, medium and full-size cars are all available."),
    ("손님이 원하시는 곳으로 자동차를 갖다 드립니다.", "We bring the car to the place the customer wants."),
    ("예약은 전화로만 받습니다.", "Reservations are taken by phone only."),
    ("다음에 다시 저희 렌트카를 이용하시면 하루는 무료입니다.", "If you use our rental cars again next time, one day is free."),
    ("저희 렌트카와 함께 즐거운 여행하세요!", "Have a pleasant trip with our rental cars!"),
]
_RENT_AD2 = [
    ("한국 렌터카", "Hanguk Rent-a-Car"),
    ("최고의 서비스를 찾으십니까?", "Are you looking for the best service?"),
    ("주말에 차를 빌리시는 분께는 이십 퍼센트 할인을 해 드립니다.", "To those who rent a car on the weekend we give a 20% discount."),
    ("소형, 중형, 대형, 여러분께서 찾으시는 모든 차가 준비되어 있습니다.", "Small, medium, full-size: every car you are looking for is ready."),
    ("보험을 포함해서 아주 싼 가격에 빌려드립니다.", "Including insurance, we rent at a very cheap price."),
    ("지금 바로 전화 주십시오.", "Please call right now."),
    ("항상 최고의 서비스로 모시겠습니다.", "We will always serve you with the best service."),
]
_GRID = [list("고가견지형조"), list("장인나자동식"), list("차운열다라휴"), list("영쇠전정국게"), list("보험미면비소"), list("임성포함허소"), list("고치다마바증")]
_WS = [("a tow truck", "견인차", "diagonal, from 견 at the top down to 차 at the left"), ("to fix", "고치다", "bottom row, from the left"), ("an automatic", "자동식", "second row, on the right"), ("an auto repair shop", "정비소", "diagonal, from 정 down to 소"), ("malfunction", "고장", "first column, at the top"),
       ("a key", "열쇠", "diagonal, from 열 down to 쇠"), ("inclusion", "포함", "sixth row, in the middle"), ("a driver’s license", "운전면허증", "diagonal, from 운 down to 증"), ("insurance", "보험", "fifth row, on the left"), ("a rest place", "휴게소", "last column, from 휴 down to 소")]
_RENT_W = [("갖다 드리다", "to bring (to someone) (mine)"), ("무료", "free of charge (mine)"), ("이용하다", "to use (mine)"), ("할인", "a discount (mine)"), ("서비스", "service (mine)"), ("가격", "a price (mine)"), ("빌려드리다", "to rent out; to lend (mine)"), ("모시다", "to serve; to attend (humble) (mine)")]
L5 = lesson(
    "Ch 16 · Activities B: car rental advertisements and the word search",
    "한국 렌트카 · 예약은 전화로만 · 하루는 무료 · 이십 퍼센트 할인 · 견인차 · 정비소",
    requires=[],
    cards=[
        card("Topic B, Follow-up 1 (Reading): a car rental advertisement",
             "The book shows a car rental advertisement and asks you to fill in a table in English (types of rental cars, how to reserve, special offer). The text is the book’s (the phone number is left out); the English is mine.",
             examples=passage(_RENT_AD)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Types of rental cars available", "Small, medium and full-size cars"], ["How to reserve", "By phone only"], ["Special offer", "One day free if you use their rental cars again next time (also: they bring the car to the place the customer wants)"]])]),
        card("Activity 2 (Reading): a car rental advertisement from a business directory",
             "The book gives a car rental advertisement from a Korean business directory (the book writes 20%, spelled 이십 퍼센트 here; the telephone, fax and address are left out) and asks three questions. The English is mine.",
             examples=passage(_RENT_AD2)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are mine. The underlined sentence of the book is 보험을 포함해서 아주 싼 가격에 빌려드립니다.",
             tables=[table(["Question (the book)", "Answer (mine)"], [["To whom is the agency offering a discount?", "To those who rent a car on the weekend (20% off)"], ["What kinds of cars can be rented?", "Small, medium and full-size cars: every car the customer wants"], ["Translate the underlined sentence.", "Including insurance, we rent at a very cheap price."]])]),
        card("Words of the advertisements",
             "These meanings are mine (the book does not gloss them).",
             tables=[ktable(_RENT_W)]),
        card("Activity 1 (Reading): the word search",
             "The book gives ten English words and phrases (a tow truck, to fix, an automatic, an auto repair shop, malfunction, a key, inclusion, a driver’s license, insurance, a rest place) and a puzzle of Hangul syllables in which to find and circle their Korean equivalents; one (견인차) is done for you. The puzzle is below (each word is a straight line, horizontal, vertical or diagonal); the places of the words are my answer key.",
             tables=[table(["1", "2", "3", "4", "5", "6"], [list(r) for r in _GRID], title="Word search"), table(["English", "Korean", "Where (mine)"], [list(r) for r in _WS], say=[1])]),
        card("Activities left out",
             "Activity 3 (listening to three dialogs in which a customer reports problems with her rental car, writing the problems and the actions to be taken) and Activity 4 (two role-plays: a car rental agent and a customer, and an auto repair shop mechanic and a customer, with situation cards) are audio or role-play activities."),
    ],
    exercises=uniq(
        _tr(_RENT_AD[1:] + _RENT_AD2[1:] + _RENT_W)
        + [M(f"What is “{e}” in Korean (word search)?", k, [x for _, x, _ in _WS if x != k][:3], f"{k} = {e}.") for e, k, _ in _WS]
        + [M("Which cars can be rented at 한국 렌트카?", "Small, medium and full-size cars", ["Only small cars", "Only buses", "Only sports cars"], "소형차, 중형차, 대형차 모두 있습니다."), M("Where do they bring the car?", "To the place the customer wants", ["Only to the airport", "Only to hotels", "Nowhere"], "손님이 원하시는 곳으로."),
           M("How can you reserve?", "By phone only", ["On the Internet only", "At the airport only", "By mail"], "예약은 전화로만 받습니다."), M("What is the special offer for coming again?", "One day is free", ["A 20% discount", "A free tow", "Free insurance"], "하루는 무료입니다."),
           M("Who gets a 20% discount in the business directory ad?", "Those who rent a car on the weekend", ["Those who rent for a week", "Soldiers", "Foreigners"], "주말에 차를 빌리시는 분께는 이십 퍼센트 할인."), M("What does the directory ad say about insurance?", "It is included in a very cheap price", ["It costs extra", "It is not available", "It is optional"], "보험을 포함해서 아주 싼 가격에 빌려드립니다."),
           F("예약은 전화로___ 받습니다. (only)", "만", ["도", "나"], "~만 = only."), F("다음에 다시 저희 렌트카를 이용하시면 하루는 ___입니다. (free)", "무료", ["할인", "보험"], "무료 = free of charge."), F("보험을 ___해서 아주 싼 가격에 빌려드립니다. (including)", "포함", ["취소", "환불"], "포함하다 = to include."),
           F("주말에 차를 빌리시는 분께는 이십 퍼센트 ___을 해 드립니다. (discount)", "할인", ["보험", "환불"], "할인 = a discount."), F("차가 고속도로에서 섰어요. 그래서 ___를 불렀습니다. (tow truck)", "견인차", ["열쇠", "엔진"], "견인차 = a tow truck."),
           F("갑자기 시동이 꺼지면서 차가 ___. (stalled)", "섰습니다", ["섭니다", "서요"], "서다 = to come to a stop; to stall."), F("자동차 엔진에서 ___가 나요. (smoke)", "연기", ["고장", "시동"], "연기 = smoke."), F("아침에 타이어가 ___ 났습니다. (punctured)", "펑크", ["고장", "시동"], "펑크 나다 = to have a flat tire."),
           read_q("한국 렌트카"), read_q("예약은 전화로만 받습니다"), read_q("하루는 무료입니다"), read_q("보험을 포함해서"), read_q("정비소")]
    ),
)

# ================================================================== Grammar A: 아무나 / 아무 ~(이)나
def _aa(noun):
    """아무 + noun + (이)나: 이나 after a consonant, 나 after a vowel"""
    return f"아무 {noun}" + ("이나" if has_final(noun) else "나")


_AA_N = [("일", "a task; work"), ("식당", "a restaurant"), ("차", "a car"), ("컴퓨터", "a computer"), ("음식", "food"), ("커피", "coffee"), ("선생님", "a teacher"), ("영화", "a movie"), ("책", "a book"), ("옷", "clothes")]
_AA_EX = [
    ("저는 아무 문제도 없어요.", "I do not have any problems. (Chapter 13 review)"), ("저는 방학 때 아무 데도 안 갔어요.", "I did not go anywhere during the school break. (Chapter 13 review)"),
    ("저는 아무 음식이나 잘 먹어요.", "I (can) eat any food."), ("저는 아무 음식이나 안 먹어요.", "I do not eat just any food."), ("저는 아무 커피나 마셔요.", "I drink any coffee."), ("저는 아무 커피나 안 마셔요.", "I do not drink just any coffee."),
]
_AA_EX2 = [
    ("무슨 식당에 갈까요?", "What restaurant shall we go to?"), ("아무 식당이나 괜찮아요.", "Any restaurant is OK."), ("어떤 차를 운전하시겠습니까?", "Which car would you like to drive?"), ("저는 아무 차나 운전할 수 있어요.", "I can drive any car."),
    ("어떤 차를 운전하세요?", "Which car do you drive?"), ("저는 아무 차나 운전하지 않아요.", "I do not drive just any car."), ("저는 스포츠카만 운전해요.", "I drive sports cars only."),
]
_AA_MK = [("아무 식당에서나 먹읍시다.", "Let’s eat at any restaurant."), ("아무 식당으로나 갈까요?", "Shall we go to any restaurant?"), ("아무 선생님한테나 가세요.", "Go to any teacher."), ("아무하고나 얘기하세요.", "Talk to anyone.")]
_AA_FU = [("A: 내일이 토요일인데, 어디에 놀러 갈까?  B: 나는 ___ 괜찮아.", "아무 데나", "Tomorrow is Saturday; where shall we go to have fun?  I’m fine with anywhere.", ["아무 데도", "아무 때나"]),
          ("A: 그럼 롯데백화점에 갈까?  B: 좋아. 그럼 몇 시에 만날까?  A: ___ 괜찮아.", "아무 때나", "Then shall we go to Lotte Department Store?  Good. Then what time shall we meet?  Any time is fine.", ["아무 때도", "아무 데나"]),
          ("A: 선생님, 그 파티에 ___ 가도 돼요?  B: 그럼요, 우리 반 학생은 다 올 수 있어요.", "아무나", "Teacher, can anyone go to that party?  Of course, everyone in our class can come.", ["아무도", "아무 거나"]),
          ("A: 김 일병, 지금 여덟 시인데, 왜 아직 ___ 안 왔어요?  B: 잘 모르겠어요.", "아무도", "Private First Class Kim, it is eight o’clock now; why hasn’t anyone come yet?  I don’t know.", ["아무나", "아무 때도"]),
          ("A: 집에 먹을 것이 ___ 없어요. 오늘은 나가서 먹읍시다.  B: 그럼 어디로 갈까요?", "아무 것도", "There is nothing to eat at home. Let’s go out and eat today.  Then where shall we go?", ["아무 거나", "아무 데도"]),
          ("A: (그럼 어디로 갈까요?)  B: ___ 갑시다.  A: 좋아요. 그럼 무엇을 먹을까요?", "아무 데나", "Let’s go anywhere.  Good. Then what shall we eat?", ["아무 데도", "아무 때나"]),
          ("A: 배가 고프니까 ___ 먹읍시다.", "아무 거나", "Because we are hungry, let’s eat anything.", ["아무 것도", "아무 때도"])]
_AA_FU5 = [("무슨 요리를 잘 해요? 아무 요리나 다 할 줄 알아요?", "What dishes do you cook well? Do you know how to cook every dish?"), ("스파게티와 파스타는 잘 해요.", "I am good at spaghetti and pasta."),
           ("박 일병은 아무 운동이나 다 잘 해요. 라켓볼, 야구, 농구 등을 할 줄 알아요. 그렇지만 요리는 아무 것도 못 해요.", "Private First Class Park is good at any sport. He knows how to play racquetball, baseball, basketball and so on. But he cannot cook anything at all.")]
L6 = lesson(
    "Ch 16 · Grammar A: “any” and “not just any” with 아무나 and 아무 ~(이)나",
    "아무 차나 · 아무 식당이나 · 아무나 · 아무 데나 · 아무 때나 · 아무 거나 · 아무 것도",
    requires=[],
    cards=[
        card("Expressing “any” and “not just any”",
             "In Chapter 13, you learned about the grammar feature 아무 + (noun) + 도 followed by a negative verb, which is used to express total negation. For example: 저는 아무 문제도 없어요 (I do not have any problems); 저는 방학 때 아무 데도 안 갔어요 (I did not go anywhere during the school break).\n\n"
             "Keep in mind that 아무 ~ 도 can work only in a negative sentence (or a sentence with a negative verb). However, when 아무 ~ takes the marker (이)나, it can work with affirmative and negative sentences, though their meanings are quite different.",
             examples=[D(a, b) for a, b in _AA_EX[2:]]),
        card("The two meanings",
             "Note that 아무 ~(이)나 in an affirmative sentence (or a sentence that does not have a negative verb) translates to any ~, as in anyone, anything, any kimchi, any coffee, anywhere, etc. On the other hand, 아무 ~(이)나 in a negative sentence translates to not just any ~, as in not just anyone, not just anything, not just any kimchi, not just any coffee, not just any place, etc.",
             tables=[table(["Pattern", "Meaning"], [["아무나 or 아무 ~(이)나 in the affirmative", "“Any ~”"], ["아무나 or 아무 ~(이)나 in the negative", "“Not just any ~”"]]), table(["Condition", "Rule", "Example"], [["When a noun ends in a consonant", "add 이나", "아무 일이나; 아무 식당이나"], ["When a noun ends in a vowel", "add 나", "아무 차나; 아무 컴퓨터나"]], title="아무 + noun + (이)나")]),
        card("Examples with questions",
             "The book’s examples:",
             examples=[D(a, b) for a, b in _AA_EX2]),
        card("Adding another marker",
             "When we need to add an additional marker to 아무 ~(이)나, we place it in front of (이)나, as follows:",
             examples=[D(a, b) for a, b in _AA_MK]),
        card("Forms",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Noun", "Meaning", "아무 ~(이)나"], [[n, m, _aa(n)] for n, m in _AA_N], say=[0, 2]), table(["Word", "Meaning (mine)"], [["아무나", "anyone"], ["아무 데나", "anywhere"], ["아무 때나", "any time"], ["아무 거나", "anything"], ["아무도", "no one (with a negative verb)"], ["아무 데도", "nowhere (with a negative verb)"], ["아무 때도", "never; at no time (with a negative verb)"], ["아무 것도", "nothing (with a negative verb)"]], say=[0])]),
        card("Follow-up 1: fill in the blanks",
             "The book gives four dialogs (seven blanks) and a box of eight words (아무 거나, 아무 때나, 아무 데나, 아무나, 아무 것도, 아무 때도, 아무 데도, 아무도) and says that some may have multiple answers. The answers are mine; the book’s box has no other answers, but some blanks can take more than one of the words.",
             tables=[table(["Dialog (the book)", "Answer (mine)", "Meaning (mine)"], [[a, b, c] for a, b, c, d in _AA_FU], say=[1])]),
        card("Follow-up 5: do you know how to cook every dish?",
             "In the book you fill in a table of what you can do in four categories (운동, 게임, 외국어, 요리), interview two classmates, and report the results. The book’s models (the English is mine):",
             examples=[D(a, b) for a, b in _AA_FU5]),
        card("Activities left out",
             "Follow-up 2 (listening to four segments of a conversation about renting a car, writing the phrases with 아무 + noun + 나 and their English meaning) is an audio activity; the table, interviews and class presentation of Follow-up 5 are class activities."),
    ],
    exercises=uniq(
        [M(f"Which is “any {m.replace('a ', '').replace('an ', '')}” with 아무 ~(이)나 ({n})?", _aa(n), [f"아무 {n}" + ("나" if has_final(n) else "이나"), f"아무 {n}도", f"아무 {n}만"], f"{n} ends in a {'consonant' if has_final(n) else 'vowel'}: {_aa(n)}.") for n, m in _AA_N]
        + _tr(_AA_EX + _AA_EX2 + _AA_MK + _AA_FU5)
        + [F(q.replace("___", "___"), a, d, f"{a} = {tr}") for q, a, tr, d in [(x[0], x[1], x[2], x[3]) for x in _AA_FU[:5]] if q.count("___") == 1]
        + [F("A: (어디로 갈까요?)  B: ___ 갑시다. (anywhere)", "아무 데나", ["아무 데도", "아무 때나"], "Let’s go anywhere: 아무 데나."), F("A: 배가 고프니까 ___ 먹읍시다. (anything)", "아무 거나", ["아무 것도", "아무 때도"], "Let’s eat anything: 아무 거나."),
           F("저는 ___ 음식이나 잘 먹어요. (any)", "아무", ["무슨", "어떤"], "아무 음식이나 = any food."), F("저는 아무 차___ 운전할 수 있어요. (any car)", "나", ["이나", "도"], "차 ends in a vowel: 아무 차나."), F("아무 식당___ 괜찮아요. (any restaurant)", "이나", ["나", "도"], "식당 ends in a consonant: 아무 식당이나."),
           F("아무 식당___ 먹읍시다. (let’s eat at any restaurant)", "에서나", ["이나에서", "에서도"], "The marker 에서 goes in front of (이)나."), F("아무 선생님___ 가세요. (go to any teacher)", "한테나", ["이나한테", "한테도"], "한테 + 나."), F("저는 방학 때 아무 데___ 안 갔어요. (nowhere)", "도", ["나", "이나"], "아무 ~도 + negative verb = total negation."),
           M("What does 저는 아무 차나 운전할 수 있어요 mean?", "I can drive any car.", ["I cannot drive any car.", "I do not drive just any car.", "I drive no car."], "Affirmative 아무 ~(이)나 = any ~."), M("What does 저는 아무 차나 운전하지 않아요 mean?", "I do not drive just any car.", ["I can drive any car.", "I do not drive any car at all.", "I drive every car."], "Negative 아무 ~(이)나 = not just any ~."),
           M("What does 저는 아무 차도 운전하지 않아요 mean?", "I do not drive any car at all.", ["I can drive any car.", "I do not drive just any car.", "I drive every car."], "아무 ~도 + negative = total negation."), M("Which pattern works only in a negative sentence?", "아무 ~도", ["아무 ~(이)나", "아무나", "아무 데나"], "아무 ~도 + negative verb."),
           M("Which pattern works in affirmative and negative sentences?", "아무 ~(이)나", ["아무 ~도", "아무것도", "아무 ~만"], "아무 ~(이)나 can take both, with different meanings."), M("Where does an additional marker go?", "In front of (이)나", ["After (이)나", "It is not allowed", "In front of 아무"], "아무 식당에서나."),
           M("What does 아무 거나 mean?", "anything", ["anywhere", "any time", "anyone"], "거 = thing."), M("What does 아무 데나 mean?", "anywhere", ["anything", "any time", "anyone"], "데 = place."), M("What does 아무 때나 mean?", "any time", ["anything", "anywhere", "anyone"], "때 = time."),
           read_q("아무 차나"), read_q("아무 식당이나"), read_q("아무 데나"), read_q("아무 때나"), read_q("아무 식당에서나")]
    ),
)

# ================================================================== Grammar B: -(으)ㄹ 줄 알다 / 모르다
def _jul(verb):
    """-(으)ㄹ 줄: 수영하다 -> 수영할 줄, 읽다 -> 읽을 줄, 만들다 -> 만들 줄"""
    return can_(verb)[:-1] + "줄"


_JUL_V = [("수영하다", "to swim"), ("고치다", "to repair; to fix"), ("읽다", "to read"), ("찾다", "to look for"), ("치다", "to play (piano, tennis)"), ("하다", "to do; to speak (a language)"), ("운전하다", "to drive"), ("만들다", "to make"), ("먹다", "to eat"), ("쓰다", "to write"), ("타다", "to ride"), ("요리하다", "to cook")]
_JUL_EX = [("수영할 줄 알아요?", "Do you know how to swim?"), ("아니요, 저는 수영할 줄 몰라요.", "No, I don’t (know how to swim)."), ("불어 읽을 줄 알아요?", "Do you know how to read French?"), ("네, 읽을 줄 알아요.", "Yes, I know (how to read it)."),
           ("저는 수동식도 운전할 줄 알아요.", "I know how to drive a manual one, too. (from Topic B)"), ("저는 한국말을 할 줄 몰라요.", "I do not know how to speak Korean. (the book’s example in the Core Vocabulary; English mine)"), ("최 상병은 일본어를 할 줄 알아요.", "Corporal Choi knows how to speak Japanese. (the book’s example in the Core Vocabulary; English mine)"), ("나는 수동식 차를 운전할 줄 모릅니다.", "I do not know how to drive a manual car. (the book’s example in the Core Vocabulary; English mine)")]
_JUL_PH = [("피아노를", "치다"), ("테니스를", "치다"), ("일본어를", "하다"), ("", "운전하다"), ("한국 신문을", "읽다"), ("영화를", "다운로드하다"), ("차를", "고치다"), ("파스타를", "만들다"), ("윈드서핑을", "하다")]
_JUL_PH_EN = ["to play the piano", "to play tennis", "to speak Japanese", "to drive", "to read a Korean newspaper", "to download a movie", "to fix a car", "to make pasta", "to windsurf"]
_JUL_MODEL = [("김 이병, 피아노 칠 줄 알아요?", "Private Kim, do you know how to play the piano?"), ("네. 저는 피아노 칠 줄 알아요. 최 이병도 피아노 칠 줄 알아요?", "Yes. I know how to play the piano. Private Choi, do you know how to play the piano, too?"), ("아니요. 저는 피아노 칠 줄 몰라요.", "No. I do not know how to play the piano.")]


def _jul_ask(obj, verb):
    return (obj + " " if obj else "") + _jul(verb) + " 알아요?"


L7 = lesson(
    "Ch 16 · Grammar B: “know how to” and “not know how to” with -(으)ㄹ 줄 알다/모르다",
    "수영할 줄 알아요 · 수영할 줄 몰라요 · 읽을 줄 알아요 · 고칠 줄 알아요 · 운전할 줄 알아요",
    requires=[],
    cards=[
        card("Expressing “know how to” and “not know how to”",
             "In English, we often use “know how to …” or “not know how to …” to express ability or inability to do something. Likewise, Koreans use the expressions -(으)ㄹ 줄 알다 (know how to) and -(으)ㄹ 줄 모르다 (not know how to).",
             tables=[table(["Pattern", "Meaning"], [["verb stem + (으)ㄹ 줄 알다", "“Know how to”"], ["verb stem + (으)ㄹ 줄 모르다", "“Not know how to”"]]),
                     table(["Condition", "Rule", "Example"], [["When a verb stem ends in a vowel", "add ㄹ 줄 알다 / 모르다", "수영하다 → 수영할 줄 알다 / 수영할 줄 모르다; 차를 고치다 → 고칠 줄 알다 / 고칠 줄 모르다"], ["When a verb stem ends in a consonant", "add 을 줄 알다 / 모르다", "책을 읽다 → 읽을 줄 알다 / 읽을 줄 모르다; 사전을 찾다 → 찾을 줄 알다 / 찾을 줄 모르다"]], title="verb stem + (으)ㄹ 줄 알다/모르다")],
             examples=[D(a, b) for a, b in _JUL_EX[:4]]),
        card("More examples",
             "The sentence of Topic B and the examples of the Core Vocabulary (the English is mine for the Core Vocabulary sentences):",
             examples=[D(a, b) for a, b in _JUL_EX[4:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule (a stem ending in ㄹ keeps it: 만들다 → 만들 줄).",
             tables=[table(["Dictionary form", "Meaning", "-(으)ㄹ 줄", "Know how to", "Not know how to"], [[v, m, _jul(v), _jul(v) + " 알아요", _jul(v) + " 몰라요"] for v, m in _JUL_V], say=[0, 2, 3, 4])]),
        card("Follow-up 3: ask what your partner can do",
             "In the book partners take turns choosing a verbal phrase from a box of nine and ask with -(으)ㄹ 줄 알다 what the partner can do. The book’s model is below (the English is mine); the nine questions are mine.",
             examples=dlg([("A", *_JUL_MODEL[0]), ("B", *_JUL_MODEL[1]), ("A", *_JUL_MODEL[2])]),
             tables=[table(["Phrase (the book)", "Question (mine)", "Meaning (mine)"], [[(o + " " if o else "") + v, _jul_ask(o, v), f"Do you know how {e}?"] for (o, v), e in zip(_JUL_PH, _JUL_PH_EN)], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 4 (listening to five dialogs in which a man asks a woman if she can do something, writing the question in English and checking affirmative or negative) is an audio activity. The speaking part of Follow-up 3 is a partner activity."),
    ],
    exercises=uniq(
        [M(f"How do you say “know how to {m.replace('to ', '', 1)}” with {v}?", _jul(v) + " 알아요", [_jul(v) + " 몰라요", can_(v) + " 있어요", stem(v) + "고 있어요"], f"{v} → {_jul(v)} 알아요.") for v, m in _JUL_V]
        + [M(f"How do you say “do not know how to {m.replace('to ', '', 1)}” with {v}?", _jul(v) + " 몰라요", [_jul(v) + " 알아요", can_(v) + " 없어요", stem(v) + "지 않아요"], f"{v} → {_jul(v)} 몰라요.") for v, m in _JUL_V[:8]]
        + _tr(_JUL_EX + _JUL_MODEL)
        + [M(f"Which question asks “Do you know how {e}?”", _jul_ask(o, v), [_jul_ask(o2, v2) for (o2, v2) in _JUL_PH if _jul_ask(o2, v2) != _jul_ask(o, v)][:3], f"{o} {v} → {_jul_ask(o, v)}") for (o, v), e in zip(_JUL_PH, _JUL_PH_EN)]
        + [F("수영할 ___ 알아요? (know how to)", "줄", ["수", "것"], "-(으)ㄹ 줄 알다 = know how to."), F("아니요, 저는 수영할 ___ 몰라요. (do not know how to)", "줄", ["수", "것"], "-(으)ㄹ 줄 모르다 = not know how to."), F("불어 읽을 줄 ___? (do you know)", "알아요", ["몰라요", "있어요"], "알다 → 알아요."),
           F("저는 한국말을 할 줄 ___. (do not know)", "몰라요", ["알아요", "없어요"], "모르다 → 몰라요."), F("차를 ___ 줄 알아요? (fix)", "고칠", ["고쳐", "고치는"], "고치다 ends in a vowel: 고칠 줄."), F("한국 신문을 읽___ 줄 알아요? (read)", "을", ["ㄹ", "는"], "읽다 ends in a consonant: 읽을 줄."),
           F("저는 수동식도 ___ 줄 알아요. (drive)", "운전할", ["운전하는", "운전해"], "운전하다 → 운전할 줄."), F("나는 수동식 차를 운전할 줄 ___. (do not know; formal)", "모릅니다", ["몰라요", "알아요"], "모르다 + ㅂ니다 = 모릅니다."),
           M("What does 수영할 줄 알아요 ask?", "Whether you know how to swim", ["Whether you swam", "Whether you will swim", "Whether you like swimming"], "-(으)ㄹ 줄 알다 = know how to."), M("What does 저는 수영할 줄 몰라요 mean?", "I do not know how to swim.", ["I will not swim.", "I swam yesterday.", "I do not like swimming."], "-(으)ㄹ 줄 모르다 = not know how to."),
           M("Which ending is added to a verb stem that ends in a vowel?", "ㄹ 줄", ["을 줄", "는 줄", "고 줄"], "수영하다 → 수영할 줄."), M("Which ending is added to a verb stem that ends in a consonant?", "을 줄", ["ㄹ 줄", "는 줄", "고 줄"], "읽다 → 읽을 줄."),
           read_q("수영할 줄 알아요"), read_q("읽을 줄 몰라요"), read_q("고칠 줄 알아요"), read_q("피아노 칠 줄 알아요"), read_q("운전할 줄 알아요")]
    ),
)

# ================================================================== Topic C
_C_DLG = [
    ("안내원", "여기가 불국사입니다. 세계적인 관광 명소입니다. 신라 때 지은 절이에요.", "This is Bulguksa. It is a world-renowned tourist attraction. It is a temple built in the Silla period."),
    ("앤더슨 상병", "정말 인상적이군요! 경치도 아주 좋아요. 그런데 한국에는 절이 많아요?", "It is really impressive! The scenery is also very good. By the way, are there many temples in Korea?"),
    ("안내원", "네, 한국은 옛날에 불교 국가였어요.", "Yes, Korea was a Buddhist country in the old days."),
    ("앤더슨 상병", "그렇군요. 그런데, 저건 뭐예요?", "I see. By the way, what is that over there?"),
    ("안내원", "탑입니다. 왼쪽이 다보탑이고 오른쪽이 석가탑이에요.", "It is a pagoda. The one on the left is Dabotap and the one on the right is Seokgatap."),
    ("앤더슨 상병", "탑이 아주 멋있네요!", "The pagodas are very cool!"),
    ("안내원", "네. 그럼 다음에는 경주 박물관을 관광하겠습니다. 거기에는 신라 문화재가 많습니다. 또 박물관 근처에도 많은 유적지가 있습니다.", "Yes. Then next we will tour the Gyeongju Museum. There are many Silla cultural assets there. Also there are many historic sites near the museum."),
    ("앤더슨 상병", "와, 오늘 경주 관광하면서 신라 역사에 대해서 많이 배우겠어요.", "Wow, I will learn a lot about Silla history while touring Gyeongju today."),
    ("안내원", "그리고 마지막으로 경주 온천을 가겠습니다.", "And finally we will go to the Gyeongju hot spring."),
    ("앤더슨 상병", "네, 아주 좋은 경험이 되겠네요.", "Yes, it will be a very good experience."),
]
_C_WORDS = ["경치", "경험", "-(는)군요", "-네요", "~궁", "마지막", "멋있다", "명소", "문화재", "불교", "~사", "세계적", "-(으)면서", "절", "짓다", "역사", "온천", "옛날", "유적지", "탑"]
_GJ = [("불국사", "Bulguksa"), ("석가탑", "Seokgatap"), ("다보탑", "Dabotap"), ("석굴암", "Seokguram"), ("첨성대", "Cheomseongdae (the Observatory)"), ("경주 국립 박물관", "Gyeongju National Museum")]
L8 = lesson(
    "Ch 16 · Topic C: there are many famous tourist attractions in Gyeongju",
    "경주에는 유명한 관광 명소가 많네요 · 불국사 · 다보탑 · 석가탑 · 박물관 · 온천",
    requires=[],
    cards=[
        card("Topic C: there are many famous tourist attractions in Gyeongju! (경주에는 유명한 관광 명소가 많네요!)",
             "SPC Anderson is talking with a tour guide at Bulguksa, Gyeongju. (The English is mine; the book gives none. The book’s footnotes: 신라 is “Silla”, and 저건 is a contracted form of 저것은.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Gyeongju tourist attractions (경주 관광 명소)",
             "The book shows photographs with these captions (the English is the book’s where it gives one, otherwise mine):",
             tables=[ktable(_GJ)]),
        card("Cultural notes: Buddhism and temples",
             "Buddhism was introduced to the Korean Peninsula via China in 372 c.e. 절 is the native Korean term for a Buddhist temple. Each temple has its own name, which invariably ends with 사 (a temple), as in 불국사, 해인사, 법주사, etc. There are several hundred temples scattered throughout Korea, some more than 1,500 years old. (The book also shows a map titled “The Three Kingdoms of Korea”, which is left out.)",
             tables=[ktable([("불국사", "Bulguksa (temple)"), ("해인사", "Haeinsa (temple)"), ("법주사", "Beopjusa (temple)")])]),
        card("Activities left out",
             "The SMART Board activities, the Presentation Activity’s reading aloud of the dialog in pairs, Follow-up 2 (listening to three conversations in which two people talk about Gyeongju and filling in the recommendation and the reason in English) and the Useful Links (Gyeongju culture and tourism, Bulguksa, Gyeongbokgung, Onyang hot spring) are audio, computer, partner or website activities. Follow-up 1 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith(("-", "~"))]))
        + _tr(_strip(_C_DLG)) + _tr(_GJ)
        + [M("Where is SPC Anderson with the tour guide?", "At Bulguksa in Gyeongju", ["At the Gyeongju Museum", "At a hot spring", "In Seoul"], "여기가 불국사입니다."), M("When was Bulguksa built?", "In the Silla period", ["In the Joseon period", "Last year", "In the Goryeo period"], "신라 때 지은 절이에요."),
           M("What was Korea in the old days?", "A Buddhist country", ["A Christian country", "A Confucian country only", "A kingdom of islands"], "한국은 옛날에 불교 국가였어요."), M("Which pagoda is on the left?", "Dabotap", ["Seokgatap", "Cheomseongdae", "Seokguram"], "왼쪽이 다보탑."),
           M("Which pagoda is on the right?", "Seokgatap", ["Dabotap", "Cheomseongdae", "Seokguram"], "오른쪽이 석가탑."), M("Where will they go next?", "The Gyeongju Museum", ["The hot spring", "Seoul", "A beach"], "다음에는 경주 박물관을 관광하겠습니다."),
           M("What is in the Gyeongju Museum?", "Many Silla cultural assets", ["Modern art", "Cars", "Nothing"], "신라 문화재가 많습니다."), M("What is near the museum?", "Many historic sites", ["A beach", "A mountain", "A harbor"], "박물관 근처에도 많은 유적지가 있습니다."),
           M("What will Anderson learn while touring?", "A lot about Silla history", ["Cooking", "Driving", "English"], "신라 역사에 대해서 많이 배우겠어요."), M("Where will they go at the end?", "The Gyeongju hot spring", ["The museum", "Bulguksa", "The airport"], "마지막으로 경주 온천을 가겠습니다."),
           M("When was Buddhism introduced to the Korean Peninsula?", "In 372 c.e., via China", ["In 1372", "In 72 c.e.", "In 1950"], "Buddhism was introduced to the Korean Peninsula via China in 372 c.e."), M("What do temple names invariably end with?", "사", ["절", "탑", "궁"], "불국사, 해인사, 법주사."),
           F("여기가 불국사입니다. ___인 관광 명소입니다. (world-renowned)", "세계적", ["역사적", "인상적"], "세계적 = world-renowned."), F("신라 때 지은 ___이에요. (a temple)", "절", ["탑", "궁"], "절 = a Buddhist temple."), F("정말 인상적이___! (exclamation: I realize)", "군요", ["어요", "네"], "이다 + 군요 = 이군요 (here 인상적이군요)."),
           F("탑이 아주 멋있___! (exclamation)", "네요", ["어요", "는군요"], "멋있다 + 네요 = 멋있네요."), F("한국은 옛날에 ___ 국가였어요. (Buddhist)", "불교", ["기독교", "유교"], "불교 = Buddhism."), F("경주 박물관에는 신라 ___가 많습니다. (cultural assets)", "문화재", ["유적지", "온천"], "문화재 = a cultural asset."),
           F("경주 관광하___ 신라 역사에 대해서 많이 배우겠어요. (while)", "면서", ["으면서", "는데"], "관광하다 ends in a vowel: 관광하면서."), F("___으로 경주 온천을 가겠습니다. (finally)", "마지막", ["처음", "다음"], "마지막으로 = finally."),
           read_q("불국사"), read_q("다보탑"), read_q("석가탑"), read_q("경주 박물관"), read_q("경주 온천")]
    ),
)

# ================================================================== Activities C
_JOURNAL = [
    ("경주 관광 첫째 날 오후에는 경주 박물관을 방문했다.", "On the afternoon of the first day of the Gyeongju tour, I visited the Gyeongju Museum."),
    ("박물관에는 많은 신라 문화재가 있었다.", "There were many Silla cultural assets in the museum."),
    ("박물관 일 층에는 신라 시대의 그림이 많았다.", "On the first floor of the museum there were many paintings of the Silla period."),
    ("그리고 이 층과 삼 층에는 신라 시대의 옷과 물건, 그리고 다른 문화재가 있었다.", "And on the second and third floors there were clothes and objects of the Silla period, and other cultural assets."),
    ("박물관을 구경한 후에는 첨성대를 관광했다.", "After seeing the museum, I toured Cheomseongdae (the Observatory)."),
    (f"첨성대는 {_kn(647)}년 신라 때 지었다.", "Cheomseongdae was built in 647, in the Silla period."),
    ("이 첨성대는 아시아에서 가장 오래된 것이다.", "This Cheomseongdae is the oldest one in Asia."),
    ("아주 인상적이었다.", "It was very impressive."),
]
_SITES = [("경주에 있는 불국사를 방문해 보세요. 불국사에는 유명한 석굴암이 있습니다. 또, 다보탑과 석가탑도 있습니다.", "Visit Bulguksa in Gyeongju. At Bulguksa there is the famous Seokguram. Also, there are Dabotap and Seokgatap.", "불국사", "Bulguksa", "불국사, 석굴암, 다보탑, 석가탑"),
          ("한국의 곳곳에는 온천이 많이 있습니다. 특히 온양온천이 유명합니다. 온양온천 근처에는 문화재와 유적지도 많습니다.", "There are many hot springs all over Korea. Onyang hot spring is especially famous. Near Onyang hot spring there are also many cultural assets and historic sites.", "온양온천", "Onyang hot spring", "온천, 온양온천, 문화재, 유적지"),
          ("서울에서 경복궁을 방문해 보세요. 특히 경복궁은 가장 큰 궁입니다. 경복궁에는 박물관도 있습니다.", "Visit Gyeongbokgung in Seoul. Gyeongbokgung in particular is the biggest palace. There is also a museum at Gyeongbokgung.", "경복궁", "Gyeongbokgung", "경복궁, 가장 큰 궁, 박물관")]
_CW = [("첫째 날", "the first day (mine)"), ("시대", "a period; an era (mine)"), ("그림", "a painting; a picture (mine)"), ("물건", "an object; a thing (mine)"), ("첨성대", "Cheomseongdae; the Observatory (the book’s gloss)"), ("곳곳", "everywhere; all over (mine)"), ("특히", "especially (mine)"), ("가장", "the most (mine)")]
L9 = lesson(
    "Ch 16 · Activities C: a journal about Gyeongju and the tourist spots",
    "경주 박물관 · 첨성대 · 신라 시대 · 불국사 · 온양온천 · 경복궁",
    requires=[],
    cards=[
        card("Topic C, Follow-up 1 (Reading): SPC Anderson’s journal about his trip to Gyeongju",
             "The book gives an excerpt from SPC Anderson’s journal and asks you to fill in a table in English (when, place visited, detailed description of the place). The text is the book’s (1층, 2층, 3층 and 647년 are spelled out in Hangul); the English is mine. The book glosses 첨성대 as “Observatory”.",
             examples=passage(_JOURNAL)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["When", "Place visited", "Detailed description of the place"], [["The afternoon of the first day", "Gyeongju Museum", "Many Silla cultural assets; paintings of the Silla period on the first floor; clothes, objects and other cultural assets of the Silla period on the second and third floors"], ["After the museum", "Cheomseongdae (the Observatory)", "Built in 647 in the Silla period; the oldest one in Asia; very impressive"]])]),
        card("Activity 1 (Reading): match each description with its place",
             "The book gives three descriptions and three pictures: match each description with its picture by writing the number, then circle the key words that are clues. The pictures are left out; the descriptions are the book’s. The place of each description and its key words are mine.",
             tables=[table(["Description (the book)", "Meaning (mine)", "Place (mine)", "Key words (mine)"], [[a, b, d, e] for a, b, c, d, e in _SITES], say=[0])]),
        card("Words of the texts",
             "The book glosses only 첨성대; the other meanings are mine.",
             tables=[ktable(_CW)]),
        card("Activities left out",
             "Activity 2 (listening to three radio advertisements for tourist destinations and filling in the admission fee, services for foreigners and other information) is an audio activity; Activity 3 (a pamphlet about a Korean tourist spot, made in pairs from attraction cards and websites, on a flip chart, and presented) is a partner, website and class activity."),
    ],
    exercises=uniq(
        _tr(_JOURNAL + [(a, b) for a, b, *_ in _SITES] + _CW)
        + [M("On which day of the tour did Anderson visit the museum?", "The first day", ["The second day", "The last day", "The third day"], "경주 관광 첫째 날 오후."), M("What was on the first floor of the museum?", "Paintings of the Silla period", ["Clothes", "Objects", "Nothing"], "일 층에는 신라 시대의 그림이 많았다."),
           M("What was on the second and third floors?", "Clothes, objects and other cultural assets of the Silla period", ["Only paintings", "A cafe", "Nothing"], "이 층과 삼 층에는 신라 시대의 옷과 물건."), M("What did Anderson tour after the museum?", "Cheomseongdae", ["Bulguksa", "The hot spring", "Gyeongbokgung"], "박물관을 구경한 후에는 첨성대를 관광했다."),
           M("When was Cheomseongdae built?", "In 647, in the Silla period", ["In 1647", "In 947", "In 1950"], "육백사십칠 년 신라 때 지었다."), M("What is special about Cheomseongdae?", "It is the oldest one in Asia", ["It is the biggest in Korea", "It is a palace", "It is a hot spring"], "아시아에서 가장 오래된 것이다."),
           M("Which place has the famous Seokguram?", "Bulguksa", ["Gyeongbokgung", "Onyang hot spring", "The museum"], "불국사에는 유명한 석굴암이 있습니다."), M("Which place is especially famous for hot springs?", "Onyang", ["Gyeongju", "Seoul", "Jeju"], "특히 온양온천이 유명합니다."),
           M("Which is the biggest palace in the description?", "Gyeongbokgung", ["Bulguksa", "Cheomseongdae", "Onyang"], "경복궁은 가장 큰 궁입니다."), M("Where is Gyeongbokgung?", "In Seoul", ["In Gyeongju", "On Jeju", "In Onyang"], "서울에서 경복궁을 방문해 보세요."),
           F("박물관 ___에는 신라 시대의 그림이 많았다. (the first floor)", "일 층", ["이 층", "삼 층"], "1층 = 일 층."), F("첨성대는 아시아에서 가장 ___ 것이다. (oldest)", "오래된", ["아름다운", "큰"], "오래되다 = to be old (objects)."), F("경복궁은 가장 큰 ___입니다. (palace)", "궁", ["절", "탑"], "궁 = a palace."),
           F("온양온천 근처에는 문화재와 ___도 많습니다. (historic sites)", "유적지", ["온천", "박물관"], "유적지 = a historic site."), F("___ 온양온천이 유명합니다. (especially)", "특히", ["가장", "또"], "특히 = especially."),
           read_q("경주 관광 첫째 날"), read_q("첨성대"), read_q("신라 시대의 그림"), read_q("온양온천"), read_q("경복궁")]
    ),
)

# ================================================================== Grammar C: -(으)면서
def _ms(verb):
    """-(으)면서: 면서 after a vowel or ㄹ, 으면서 after a consonant; ㄷ irregular: 듣다 -> 들으면서; ㅂ irregular: 춥다 -> 추우면서"""
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    if verb in _D_IRR:
        return st[:-1] + _K.compose(l, v, "ㄹ") + "으면서"
    if verb in _IRR:
        return _ao(verb)[:-1] + "우면서"
    if t and t != "ㄹ":
        return st + "으면서"
    return st + "면서"


_MS_V = [("샤워하다", "to take a shower"), ("노래하다", "to sing"), ("읽다", "to read"), ("마시다", "to drink"), ("듣다", "to listen"), ("걷다", "to walk"), ("운전하다", "to drive"), ("먹다", "to eat"), ("보다", "to watch"), ("놀다", "to play"), ("싸다", "to be cheap"), ("예쁘다", "to be pretty"), ("이야기하다", "to talk"), ("일하다", "to work")]
_MS_EX = [("저는 샤워하면서 노래해요.", "I sing while taking a shower."), ("장 선생님은 의사이면서 교수이십니다.", "Mr. Chang is a doctor and (at the same time) a professor."), ("저는 노래하면서 샤워해요.", "I take a shower while singing."),
          ("지금 책을 읽으면서 커피 마셔요.", "I am drinking coffee while reading a book."), ("이 가방은 싸면서 예쁩니다.", "This bag is pretty as well as inexpensive."), ("저는 보통 운전하면서 음악을 듣습니다.", "I usually listen to music while driving. (the book’s example in the Core Vocabulary; English mine)"),
          ("갑자기 시동이 꺼지면서 차가 섰습니다.", "Suddenly the engine went off and the car stopped. (the book’s example in the Core Vocabulary; English mine)"), ("오늘 경주 관광하면서 신라 역사에 대해서 많이 배우겠어요.", "I will learn a lot about Silla history while touring Gyeongju today. (from Topic C)")]
_MS_CHAIN = [("철수", "샤워합니다.", "I take a shower."), ("영희", "샤워하면서 음악을 듣습니다.", "I listen to music while taking a shower."), ("민수", "음악을 들으면서 커피를 마십니다.", "I drink coffee while listening to music."), ("지영", "커피를 마시면서 친구와 이야기합니다.", "I talk with a friend while drinking coffee.")]
_MS_A = ["군인이다", "학생이다", "선생님이다", "공무원이다", "주부이다"]
_MS_B = ["아내이다", "간호사이다", "아들이다", "아버지이다", "의사이다"]
_MS_MY = [("군인이다", "군인이면서 아들입니다", "김 상병은 군인이면서 아들입니다.", "Corporal Kim is a soldier and a son."), ("학생이다", "학생이면서 간호사입니다", "박 씨는 학생이면서 간호사입니다.", "Mr. Park is a student and a nurse."), ("선생님이다", "선생님이면서 아버지이십니다", "이 선생님은 선생님이면서 아버지이십니다.", "Mr. Lee is a teacher and a father."),
          ("공무원이다", "공무원이면서 아내입니다", "최 씨는 공무원이면서 아내입니다.", "Ms. Choi is a public servant and a wife."), ("주부이다", "주부이면서 의사입니다", "한 씨는 주부이면서 의사입니다.", "Ms. Han is a housewife and a doctor.")]
_MS_N = [("의사", "의사이면서"), ("교수", "교수이면서"), ("군인", "군인이면서"), ("학생", "학생이면서"), ("주부", "주부이면서")]
L10 = lesson(
    "Ch 16 · Grammar C: simultaneous actions or conditions with -(으)면서",
    "샤워하면서 노래해요 · 책을 읽으면서 커피 마셔요 · 의사이면서 교수 · 싸면서 예뻐요",
    requires=[],
    cards=[
        card("Expressing simultaneous actions or conditions",
             "In English, we often express concurrent actions or conditions by using while or at the same time, as in “He is having breakfast while watching TV” or “He is lazy but, at the same time, smart.” In Korean, we express simultaneous actions or conditions by using the conjunctive ending -(으)면서: 저는 샤워하면서 노래해요 (I sing while taking a shower); 장 선생님은 의사이면서 교수이십니다 (Mr. Chang is a doctor and (at the same time) a professor).\n\n"
             "Keep in mind that -(으)면서 is used only when multiple actions or conditions are done by or exist for the same subject.",
             tables=[table(["Condition", "Rule", "Example"], [["When a verb stem ends in a vowel", "add 면서", "샤워하다 + 노래하다 → 샤워하면서 노래하다"], ["When a verb stem ends in a consonant", "add 으면서", "책을 읽다 + 커피 마시다 → 책을 읽으면서 커피 마시다"]], title="verb stem + (으)면서")],
             examples=[D(a, b) for a, b in _MS_EX[:5]]),
        card("More examples",
             "The two examples of the Core Vocabulary and the sentence of Topic C (the English is mine for these):",
             examples=[D(a, b) for a, b in _MS_EX[5:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule (a stem ending in ㄹ keeps it before 면서: 놀다 → 놀면서; the ㄷ irregular verbs 듣다 and 걷다 change ㄷ to ㄹ: 들으면서, 걸으면서). After a noun the copula 이다 is used: 의사이면서.",
             tables=[table(["Dictionary form", "Meaning", "-(으)면서"], [[v, m, _ms(v)] for v, m in _MS_V], say=[0, 2]), table(["Noun", "Noun + 이면서"], [list(r) for r in _MS_N], say=[0, 1])]),
        card("Follow-up 1: a chain of simultaneous actions",
             "In the book the students sit in a circle: the first starts with a simple phrase like 샤워합니다; the next changes it to 샤워하면서 and adds another phrase, and so on. The book’s model, with the students A–D named 철수, 영희, 민수 and 지영 here (the English is mine):",
             examples=dlg(_MS_CHAIN)),
        card("Follow-up 2: two lists",
             "In the book one partner reads a phrase from List A, the other changes it into -(으)면서 and adds a phrase from List B (the sentence must make sense). List A: 군인이다, 학생이다, 선생님이다, 공무원이다, 주부이다; List B: 아내이다, 간호사이다, 아들이다, 아버지이다, 의사이다. The book’s model: 군인이다 → 이 병장은 군인이면서 학생입니다. (Sergeant Lee is a soldier and a student.) The five sentences below are mine.",
             examples=[D("이 병장은 군인이면서 학생입니다.", "Sergeant Lee is a soldier and a student.")],
             tables=[table(["List A phrase", "Sentence (mine)", "Meaning (mine)"], [[a, c, d] for a, b, c, d in _MS_MY], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 3 (listening to a person talk about things he usually does simultaneously and filling in a table in English) is an audio activity. The circle of Follow-up 1 and the partner work of Follow-up 2 are class and partner activities."),
    ],
    exercises=uniq(
        [M(f"Which is the -(으)면서 form of {v} ({m})?", _ms(v), [x for x in dict.fromkeys([stem(v) + "면서", stem(v) + "으면서", stem(v) + "는데", stem(v) + "고"]) if x != _ms(v)][:3], f"{v} → {_ms(v)}.") for v, m in _MS_V]
        + [M(f"Which noun + 이면서 form is right for {n}?", b, [n + "면서", n + "으면서", n + "인데"], f"{n} + 이다 → {b}.") for n, b in _MS_N]
        + _tr(_MS_EX + [(b, c) for a, b, c in _MS_CHAIN] + [(c, d) for a, b, c, d in _MS_MY])
        + [F("저는 샤워하___ 노래해요. (while)", "면서", ["으면서", "는데"], "샤워하다 ends in a vowel: 샤워하면서."), F("지금 책을 읽___ 커피 마셔요. (while)", "으면서", ["면서", "는데"], "읽다 ends in a consonant: 읽으면서."), F("장 선생님은 의사___ 교수이십니다. (is a doctor and)", "이면서", ["면서", "으면서"], "의사 + 이다 → 의사이면서."),
           F("이 가방은 싸___ 예쁩니다. (as well as)", "면서", ["으면서", "는데"], "싸다 ends in a vowel: 싸면서."), F("음악을 ___ 커피를 마십니다. (while listening)", "들으면서", ["듣면서", "들면서"], "듣다 is a ㄷ irregular verb: 들으면서."), F("커피를 ___ 친구와 이야기합니다. (while drinking)", "마시면서", ["마시으면서", "마시는데"], "마시다 ends in a vowel: 마시면서."),
           F("저는 보통 운전하면서 ___을 듣습니다. (music)", "음악", ["커피", "신문"], "음악을 듣다 = to listen to music."), F("갑자기 시동이 꺼지___ 차가 섰습니다. (while)", "면서", ["으면서", "는데"], "꺼지다 ends in a vowel: 꺼지면서."),
           M("What does -(으)면서 express?", "Simultaneous actions or conditions (while)", ["A reason", "A purpose", "A wish"], "-(으)면서 = while doing; at the same time."), M("When is -(으)면서 used?", "Only when the actions are done by the same subject", ["Only for different subjects", "Only in the past", "Only with nouns"], "Same subject only."),
           M("Which ending follows a verb stem that ends in a vowel?", "면서", ["으면서", "는데", "려고"], "샤워하다 → 샤워하면서."), M("Which ending follows a verb stem that ends in a consonant?", "으면서", ["면서", "는데", "려고"], "읽다 → 읽으면서."),
           M("Which sentence means “I take a shower while singing”?", "저는 노래하면서 샤워해요.", ["저는 샤워하면서 노래해요.", "저는 노래하고 샤워해요.", "저는 샤워해서 노래해요."], "The action that is the main one comes last."), M("Which sentence means “I sing while taking a shower”?", "저는 샤워하면서 노래해요.", ["저는 노래하면서 샤워해요.", "저는 샤워하고 노래해요.", "저는 노래해서 샤워해요."], "샤워하면서 = while taking a shower."),
           read_q("샤워하면서"), read_q("읽으면서"), read_q("의사이면서"), read_q("들으면서"), read_q("운전하면서")]
    ),
)

# ================================================================== Grammar D: -(는)군요 / -네요
def _gun(verb, action):
    """(-(는)군요, -네요): action verbs in the present take 는군요 / 네요; stative verbs, 있다/없다 and 이다 take 군요 / 네요"""
    st = stem(verb)
    if action:
        l, v, t = _K.decompose(st[-1])
        if t == "ㄹ":
            d = st[:-1] + _K.compose(l, v, "")
            return d + "는군요", d + "네요"
        return st + "는군요", st + "네요"
    return st + "군요", st + "네요"


_GU_A = [("치다", "to play (piano)"), ("마시다", "to drink"), ("먹다", "to eat"), ("가다", "to go"), ("읽다", "to read"), ("하다", "to do"), ("공부하다", "to study")]
_GU_S = [("멋있다", "to be cool"), ("예쁘다", "to be pretty"), ("재미있다", "to be fun"), ("좋다", "to be good"), ("많다", "to be many"), ("크다", "to be big"), ("춥다", "to be cold"), ("따뜻하다", "to be warm"), ("있다", "to exist; to have"), ("없다", "to not exist; to not have")]
_GU_EX = [("한국말이 재미있어요.", "Korean is fun. (a simple statement: the speaker already knows)"), ("한국말이 재미있군요!", "(Wow) Korean is fun! (with -군요)"), ("한국말이 재미있네요!", "(Wow) Korean is fun! (with -네요)"),
          ("여기 경치가 참 멋있네요!", "The scenery is really great here!"), ("이 꽃은 정말 예쁘군요!", "This flower is very pretty!"), ("어머님이 의사이시군요!", "Your mother is a doctor!"), ("김 선생님은 피아노도 잘 치시네요!", "Mr. Kim plays piano well, too!"), ("매일 커피를 많이 마시는군요!", "You drink lots of coffee every day!"),
          ("정말 인상적이군요!", "It is really impressive! (from Topic C)"), ("탑이 아주 멋있네요!", "The pagodas are very cool! (from Topic C)"), ("네, 아주 좋은 경험이 되겠네요.", "Yes, it will be a very good experience. (from Topic C)"),
          ("아이가 아주 예쁘네요!", "The child is very pretty! (the book’s example in the Core Vocabulary; English mine)"), ("오늘은 날씨가 참 좋군요!", "The weather is really good today! (the book’s example in the Core Vocabulary; English mine)")]
_GU_NOUN = [("학생", "학생이군요", "학생이네요"), ("의사", "의사군요", "의사네요")]
_GU_FU5 = [("와! 김 일병은 자전거 타면서 커피도 마시네요!", "Wow! Private First Class Kim drinks coffee while riding a bicycle!"), ("저는 자전거 타면서 커피 마실 수 있어요.", "I can drink coffee while riding a bicycle.")]
L11 = lesson(
    "Ch 16 · Grammar D: realization and discovery with -(는)군요 and -네요",
    "재미있군요 · 재미있네요 · 멋있네요 · 예쁘군요 · 의사이시군요 · 마시는군요",
    requires=[],
    cards=[
        card("Verb endings that express realization or discovery",
             "In English, when we come to a realization or discover a certain fact, we often say something like, “Wow, she is beautiful!” or “Wow, this is strange!” Koreans express this by using -(는)군요 or -네요. Compare the following sentences:",
             examples=[D(a, b) for a, b in _GU_EX[:3]]),
        card("What the endings imply",
             "The first sentence is a simple statement that implies the speaker already knows that Korean is fun. However, the last two sentences, which end in -(는)군요 and -네요, tell us that the speaker just realized or discovered that Korean is fun. This implies that the speaker did not know that Korean was fun until the moment of the utterance.",
             tables=[table(["Condition", "Rule", "Example"], [["With stative verbs and 이다/아니다 or 있다/없다", "add 군요 / 네요", "멋있다 → 멋있군요 / 멋있네요!; 예쁘다 → 예쁘군요 / 예쁘네요!; 학생이다 → 학생이군요 / 학생이네요!"], ["With an action verb in the present tense", "add 는군요 / 네요", "피아노를 잘 치다 → 피아노를 잘 치는군요 / 치네요!; 커피를 마시다 → 커피를 마시는군요 / 마시네요!"]], title="verb stem + (는)군요 / 네요!")],
             examples=[D(a, b) for a, b in _GU_EX[3:8]]),
        card("More examples",
             "The sentences of Topic C and the two examples of the Core Vocabulary (the English is mine for these):",
             examples=[D(a, b) for a, b in _GU_EX[8:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule (the ending 는군요 goes after an action verb; 있다 and 없다 take 군요 as the book’s rule says; after a noun the copula 이다 gives 이군요/이네요, and after a noun that ends in a vowel the 이 can contract: 의사군요 as well as 의사이군요, mine).",
             tables=[table(["Dictionary form", "Meaning", "-(는)군요", "-네요"], [[v, m, *_gun(v, True)] for v, m in _GU_A] + [[v, m, *_gun(v, False)] for v, m in _GU_S], say=[0, 2, 3]), table(["Noun", "Noun + 이다 + 군요", "Noun + 이다 + 네요"], [list(r) for r in _GU_NOUN], say=[0, 1, 2])]),
        card("Follow-up 5: talents",
             "In the book you write two or more things you can do simultaneously, tell classmates about your talents while asking about theirs, and respond with -(는)군요 or -네요 to what you learn. The book’s title and model (the English is mine):",
             examples=[D(a, b) for a, b in _GU_FU5]),
        card("Activities left out",
             "Follow-up 4 (a PowerPoint activity) and the classmate interviews and class reports of Follow-up 5 are computer or class activities."),
    ],
    exercises=uniq(
        [M(f"Which is the -(는)군요 form of {v} ({m})?", _gun(v, True)[0], [x for x in dict.fromkeys([stem(v) + "군요", stem(v) + "어요", stem(v) + "네요"]) if x != _gun(v, True)[0]][:3], f"{v}: action verb → {_gun(v, True)[0]}.") for v, m in _GU_A]
        + [M(f"Which is the -네요 form of {v} ({m})?", _gun(v, True)[1], [x for x in dict.fromkeys([stem(v) + "는네요", stem(v) + "군요", stem(v) + "는군요"]) if x != _gun(v, True)[1]][:3], f"{v} → {_gun(v, True)[1]}.") for v, m in _GU_A[:5]]
        + [M(f"Which is the -군요 form of {v} ({m})?", _gun(v, False)[0], [x for x in dict.fromkeys([stem(v) + "는군요", stem(v) + "어요", stem(v) + "네요"]) if x != _gun(v, False)[0]][:3], f"{v}: stative verb → {_gun(v, False)[0]}.") for v, m in _GU_S]
        + [M(f"Which is the -네요 form of {v} ({m})?", _gun(v, False)[1], [x for x in dict.fromkeys([stem(v) + "는네요", stem(v) + "는군요", stem(v) + "군요"]) if x != _gun(v, False)[1]][:3], f"{v} → {_gun(v, False)[1]}.") for v, m in _GU_S[:6]]
        + _tr(_GU_EX + _GU_FU5)
        + [F("한국말이 재미있___! (wow, I realize)", "군요", ["는군요", "어요"], "재미있다 is treated as a stative verb: 재미있군요."), F("여기 경치가 참 멋있___! (wow)", "네요", ["는네요", "어요"], "멋있다 + 네요 = 멋있네요."), F("이 꽃은 정말 예쁘___! (wow)", "군요", ["는군요", "어요"], "예쁘다 + 군요 = 예쁘군요."),
           F("어머님이 의사이시___! (your mother is a doctor)", "군요", ["는군요", "어요"], "이시 + 군요."), F("김 선생님은 피아노도 잘 치시___! (wow)", "네요", ["는네요", "어요"], "치시다 + 네요 = 치시네요."), F("매일 커피를 많이 마시___! (you drink)", "는군요", ["군요", "어요"], "An action verb in the present takes 는군요."),
           F("정말 인상적이___! (it is impressive)", "군요", ["는군요", "었어요"], "인상적이다 + 군요."), F("네, 아주 좋은 경험이 되겠___. (it will be)", "네요", ["는군요", "어요"], "되겠다 + 네요."),
           M("What do -(는)군요 and -네요 express?", "Realization or discovery", ["A reason", "A plan", "A past event"], "The speaker has just realized or discovered something."), M("What does 한국말이 재미있군요 imply?", "The speaker just realized that Korean is fun", ["The speaker already knew", "Korean was fun yesterday", "The speaker is asking"], "It implies the speaker did not know until the moment of the utterance."),
           M("Which ending follows an action verb in the present?", "는군요 / 네요", ["군요 only", "는군요 only", "는네요"], "마시다 → 마시는군요 / 마시네요."), M("Which ending follows a stative verb?", "군요 / 네요", ["는군요", "는네요", "을군요"], "예쁘다 → 예쁘군요 / 예쁘네요."),
           M("Which sentence is a simple statement without surprise?", "한국말이 재미있어요.", ["한국말이 재미있군요!", "한국말이 재미있네요!", "한국말이 재미있겠네요!"], "-어요 is a simple statement."),
           read_q("재미있군요"), read_q("멋있네요"), read_q("예쁘군요"), read_q("의사이시군요"), read_q("마시는군요")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_SECS = [("Travel", _CV_TRAVEL), ("Car rental", _CV_RENT), ("Auto repair", _CV_REPAIR), ("Buddhism", _CV_BUD), ("Tourism", _CV_TOUR), ("Other words", _CV_OTH), ("Loan words", _CV_LOAN), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not r[0].startswith(("~", "-")) and "/" not in r[0] and "~" not in r[0]]
L12 = lesson(
    "Ch 16 · Core vocabulary and self-evaluation",
    "주요 단어 · 여행 · 렌터카 · 자동차 수리 · 불교 · 관광 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Optional parts, such as (~하다/되다), are kept in the meanings.\n\n"
             "The example sentences with digits are respelled in Hangul (24시간 → 이십사 시간, 10,000원 → 만 원, 5,000원 → 오천 원, 5월 5일 → 오월 오일, 75만원 → 칠십오만 원, 5천 → 오천); the book’s 연기 appears twice (延期, postponement, and 煙氣, smoke) and is shown once for each meaning. The book’s related words (the synonyms, antonyms and related words in the last column) are not repeated. The book’s Additional Vocabulary table is empty: it is for your own words."),
    ] + [card(name, "Italicized English words in the book are grammatical terms, not the meaning of a Korean word." if name == "Other words" else "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: make a domestic flight reservation; ask for and give information about a travel package; ask for and give information about renting a car; report simple car problems; identify simple automotive parts; talk about well-known tourist attractions in Korea.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; 아무나 or 아무 ~(이)나 in the affirmative (any ~); 아무나 or 아무 ~(이)나 in the negative (not just any ~); -(으)ㄹ 줄 알다 (know how to); -(으)ㄹ 줄 모르다 (not know how to); the exclamatory verb endings -군요 and -네요; the conjunctive ending -(으)면서, used to express simultaneous actions or conditions; the Sino-Korean syllables 불/부 (不), 적 (的), and 형 (型)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does the Sino-Korean syllable 불/부 (不) mean?", "not; no; non-; in-; im-; il-; ir-", ["a type; a model", "-ic; -ive", "sea"], "불편, 불법, 불가능, 불합격."), M("What does the Sino-Korean syllable 적 (的) do?", "It changes a noun into an adjective (-ic; -ive)", ["It means not", "It means a type", "It means sea"], "역사적, 인상적, 세계적."),
           M("What does the Sino-Korean syllable 형 (型) mean?", "a type; a model", ["not; no", "-ic; -ive", "sea"], "소형, 중형, 신형, 구형."), M("What does -(으)면서 mean?", "while doing (something) simultaneously", ["because", "if", "in order to"], "저는 보통 운전하면서 음악을 듣습니다."),
           M("What does -(으)ㄹ 줄 알다 mean?", "to know how to do something", ["to be able to go", "to want to do", "to have done"], "최 상병은 일본어를 할 줄 알아요."), M("What does -(으)ㄹ 줄 모르다 mean?", "to not know how to do something", ["to be unable to go", "to not want to do", "to have not done"], "저는 한국말을 할 줄 몰라요."),
           M("What do -네요 and -(는)군요 express?", "Realization or discovery (exclamatory)", ["A reason", "A wish", "A past event"], "아이가 아주 예쁘네요!"), M("What does 아무 ~(이)나 mean?", "any ~; anyone", ["no ~", "every ~ only", "some ~"], "전 아무 음식이나 잘 먹어요."),
           M("What does 연기 (延期) mean?", "postponement; delay", ["smoke", "a tow truck", "a key"], "시험 날짜가 이틀 연기되었습니다."), M("What does 연기 (煙氣) mean?", "smoke", ["postponement; delay", "a tow truck", "a key"], "방 안에 연기가 찼어요."),
           M("What is “a one-way trip”?", "편도", ["왕복", "국내선", "현금"], "편도 = a one-way (trip)."), M("What is “a tow truck”?", "견인차", ["정비소", "엔진", "열쇠"], "견인차 = a tow truck.")]
        + [read_q("주요 단어"), read_q("관광 명소"), read_q("세계적"), read_q("정비소"), read_q("온천")]
    ),
)

UNIT = unit("Semester 1 · Unit 4 · Chapter 16: Touring in Korea (한국에서 여행하기)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
