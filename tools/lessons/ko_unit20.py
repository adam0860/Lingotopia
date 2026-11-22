"""Unit 20: KBC Semester 1, Unit 4, Chapter 13 - Welcome to Korea (한국에 오신 것을 환영합니다).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 4, Student's Edition (2022).
Audio, video clips, pictures, forms, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, k=3):
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


def _strip(lines):
    return [(l[1], l[2]) for l in lines]


def _na(a, b):
    """noun connector ~(이)나: 이나 after a consonant, 나 after a vowel"""
    return a + ("이나" if has_final(a) else "나") + " " + b


def _ryeo(verb, what="고"):
    """-(으)려고 / -(으)려면: 려 after a vowel or ㄹ, 으려 after another consonant"""
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    return st + ("려" if t in ("", "ㄹ") else "으려") + what


# ---- the core vocabulary of Chapter 13 (meanings and example sentences are the book's; digits and Latin letters respelled)
_CV_AIR = [
    ("국제(선)", "(國際(線)) international (lines)", "외국으로 갈 때는 국제선 비행기를 타야 합니다."),
    ("면세점", "(免稅店) a duty-free shop", "면세점이 백화점보다 물건 값이 싸요."),
    ("면세품", "(免稅品) a duty-free item", "국제선 손님만 면세품을 살 수 있습니다."),
    ("여권", "(旅券) a passport", "외국으로 여행을 하려면 여권이 필요합니다."),
    ("연착", "(延着) late arrival; delay in arrival (~하다/되다: to be delayed; to be late)", "눈이 많이 와서 비행기가 연착되었습니다."),
    ("이륙", "(離陸) taking off; “off the land” (~하다: to take off)", "비행기가 이륙하기 전에 핸드폰을 꺼 주세요."),
    ("착륙", "(着陸) landing; “on the land” (~하다: to land)", "착륙하기 전에 자리에 꼭 앉으셔야 합니다."),
    ("탑승", "(搭乘) boarding (~하다: to board)", "오지공사오편 비행기가 곧 탑승을 시작하겠습니다."),
    ("탑승구", "(搭乘口) a boarding gate", "팔 번 탑승구가 어디에 있어요?"),
    ("탑승권", "(搭乘券) a boarding pass", "항공사 카운터에서 비행기 표를 보여주고 탑승권을 받았습니다."),
    ("~편", "(便) a flight number", "대한항공 케이이공이사편으로 부모님이 한국에서 오십니다."),
    ("항공(사)", "(航空(社)) an airline (company)", "아시아나항공편으로 한국에 갈 겁니다."),
]
_CV_PLANE = [
    ("기내(식)", "(機內(食)) in-flight (meal)", "대한항공 기내식은 아주 맛있습니다."),
    ("두고 내리다", "to leave ~ behind; “to place and get off”", "택시에 지갑을 두고 내렸습니다."),
    ("설명", "(說明) explanation (~하다: to explain)", "이번 주말 스케줄에 대해서 설명해 주세요."),
    ("승객", "(乘客) a passenger", "비행기에 승객들이 많아서 조금 복잡했습니다."),
    ("승무원", "(乘務員) a crew member; a flight attendant; a train attendant", "비행기 안에서 승무원이 커피를 갖다 주었습니다."),
    ("안전", "(安全) safety (~하다: to be safe)", "비행기는 빠르고 안전합니다."),
    ("좌석", "(座席) a seat; seating", "승객 여러분, 좌석 벨트를 매 주세요."),
    ("착용", "(着用) wearing; putting on (~하다: to wear; to put on)", "운전을 할 때에는 항상 안전 벨트를 착용해야 합니다."),
]
_CV_CUST = [
    ("기간", "(期間) duration; period", "방문 기간이 짧아서 관광을 못했어요."),
    ("내다", "to submit; to turn in", "세관을 통과하기 전에 출입국 신고서를 냈습니다."),
    ("목적", "(目的) purpose", "미국 방문 목적이 무엇입니까?"),
    ("물어보다/묻다", "to ask", "모르는 것이 있으면 저한테 물어보세요."),
    ("세관", "(稅關) customs; customs house", "세관을 쉽게 통과했습니다."),
    ("신고", "(申告) report; declaration (~하다: to report; to declare)", "신고할 물건이 아무것도 없었습니다."),
    ("신고서", "(申告書) a declaration form", "비행기에서 세관 신고서를 썼습니다."),
    ("입국", "(入國) entry into a country (~하다: to enter a country)", "입국하려면 여권과 비자가 있어야 합니다."),
    ("출국", "(出國) departure from the country (~하다: to depart from the country)", "출국하기 전에 카운터에서 짐을 먼저 부칩니다."),
    ("출입국", "(出入國) the leaving and entering of a country", "입국할 때 출입국 신고서를 내야 합니다."),
    ("통과", "(通過) passing through (~하다: to pass through)", "세관을 통과할 때 세관 신고서를 내세요."),
]
_CV_BAG = [
    ("가방", "a bag", "가방에 책을 넣으세요."),
    ("배낭", "(背囊) a backpack", "등산 갈 때 배낭을 가지고 갑니다."),
    ("잃어버리다", "to lose", "버스에서 지갑을 잃어버렸어요."),
    ("짐", "luggage; baggage", "공항에 도착하면 먼저 항공사 카운터에서 짐을 부치세요."),
]
_CV_SHAPE = [
    ("네모", "a rectangle (~나다: to be rectangular)", "저 네모난 모양의 선글라스가 마음에 듭니다."),
    ("녹색", "(綠色) green (color)", "아일랜드 사람은 녹색을 좋아합니다."),
    ("동그랗다", "to be round", "햄버거는 동그란 모양입니다."),
    ("모양", "(模樣/貌樣) a shape", "아이파드는 네모난 모양입니다."),
    ("보라(색)", "purple (color)", "저는 보라색 바이올렛 꽃을 좋아합니다."),
    ("세모", "a triangle (~나다: to be triangular)", "트라이앵글은 세모난 모양입니다."),
    ("주황(색)", "(朱黃(色)) orange (color)", "오렌지는 주황색입니다."),
]
_CV_LOAN = [
    ("비자", "a visa", "미국 사람이 캐나다를 갈 때는 비자가 필요 없습니다."),
    ("센터", "a center", "물어보고 싶은 것이 있으면 저희 안내 센터로 오세요."),
    ("카운터", "a counter", "공항에 간 후 먼저 항공사 카운터로 갔습니다."),
    ("터미널", "a terminal", "국제선 비행기를 타려면 국제선 터미널로 가야 합니다."),
]
_CV_OTH = [
    ("담요", "a blanket", "너무 추워요. 담요 한 장만 갖다 주세요."),
    ("들르다", "to stop by", "백화점에 들러서 동생 선물을 사야 합니다."),
    ("들어가다", "to go in; to enter", "우리 이 가게에 들어가서 선물을 삽시다."),
    ("~등", "and so forth; etc.", "면세점에서 핸드백, 지갑 등을 팝니다."),
    ("바꾸다", "to exchange", "달러를 한국 돈으로 바꾸고 싶습니다."),
    ("빨리", "quickly; fast", "시간이 없어요. 빨리 오세요."),
    ("아무", "any", "돈이 없어서 아무것도 살 수 없습니다."),
    ("안내", "(案內) guidance (~하다: to guide; to inform)", "승무원이 제 자리를 안내해 주었습니다."),
    ("~에 대해서", "about", "오늘은 날씨에 대해서 배우겠어요."),
    ("-(으)려고", "(in order) to", "운동하려고 체육관에 갔습니다."),
    ("-(으)려면", "if [you] intend to; (in order) to", "환전하려면 은행이나 환전소에 가야 합니다."),
    ("~(이)나", "or (as a noun connector)", "버스나 기차로 엘에이에 갑시다."),
    ("~중(에/에서)", "among; between", "이것 두 개 중에서 하나만 골라 보세요."),
    ("지하", "(地下) underground; “land below”", "일 층에서 아래로 한 층만 더 가면 지하 일 층입니다."),
    ("직원", "(職員) an employee", "제 형은 뱅크 오브 아메리카 은행 직원입니다."),
    ("확인", "(確認) confirmation (~하다/되다: to confirm/to be confirmed)", "탑승권을 다시 한번 확인해 주시기 바랍니다."),
    ("환전", "(換錢) money exchange (~하다: to exchange money)", "미국 달러를 영국 파운드로 환전합니다."),
    ("환전소", "(換錢所) a currency exchange office/booth", "돈을 바꾸려면 일 층에 있는 환전소로 가세요."),
]
_CV_SINO = [
    ("승", "(乘) to ride on", "탑승, 탑승구, 승차"),
    ("권", "(券) a document; a ticket; a bill", "탑승권, 입장권, 상품권"),
    ("착", "(着) arrival", "착용, 착륙, 연착"),
    ("면", "(免) to exempt; to avoid", "면세, 면제, 면역"),
]
_ALL = {r[0]: r for r in _CV_AIR + _CV_PLANE + _CV_CUST + _CV_BAG + _CV_SHAPE + _CV_LOAN + _CV_OTH}


def _en(word):
    t = _re.sub(r"^\([^)]*(\([^)]*\))?[^)]*\) ", "", _ALL[word][1])
    return _clean(_re.sub(r" \(~[^)]*\)", "", t))


def _pairs(words):
    return [(w, _en(w)) for w in words]


def _rows(words):
    return [(w, _ALL[w][1]) for w in words]


# ================================================================== Topic A
_A_TXT = [
    ("샌프란시스코 공항에 도착해서 국제선 터미널로 갔습니다.", "I arrived at San Francisco airport and went to the international terminal."),
    ("대한항공 카운터로 가서 항공사 직원한테 여권을 보여주었습니다.", "I went to the Korean Air counter and showed my passport to the airline employee."),
    ("그리고 케이이공이사편 탑승권을 받았습니다.", "And I received a boarding pass for flight KE024."),
    ("카운터에서 짐을 부친 후 비행기를 타러 갔습니다.", "After checking my baggage at the counter, I went to take the plane."),
    ("가는 길에 친구 선물을 사려고 면세점에 들렀습니다.", "On the way, I stopped by a duty-free shop to buy a present for a friend."),
    ("면세점에서 친구 선물을 산 후 탑승구로 갔습니다.", "After buying a present for my friend at the duty-free shop, I went to the boarding gate."),
    ("탑승구에 도착한 후 항공사 직원에게 탑승권을 주었습니다.", "After arriving at the boarding gate, I gave my boarding pass to the airline employee."),
    ("그리고 비행기 안으로 들어갔습니다.", "And I went into the plane."),
    ("승무원이 좌석을 안내해 주었습니다.", "A flight attendant showed me to my seat."),
    ("자리에 앉아서 안전벨트를 착용하고, 안전여행에 대해서 설명을 들었습니다.", "I sat down in my seat, fastened my seat belt, and listened to an explanation about a safe flight."),
    ("그리고 비행기가 이륙했습니다.", "And the plane took off."),
]
_A_WORDS = ["국제(선)", "들르다", "들어가다", "면세점", "설명", "승객", "승무원", "안내", "안전", "~에 대해서", "여권", "-(으)려고", "이륙", "좌석", "직원", "짐", "착용", "카운터", "탑승", "탑승구", "탑승권", "터미널", "~편", "항공(사)"]
_SINO_A = [("승차", "getting on a vehicle; boarding a car or train (mine)"), ("승마", "horseback riding (mine)"), ("승선", "boarding a ship (mine)"), ("할인권", "a discount coupon (mine)"), ("탑승권", "a boarding pass")]
_SINO_A2 = [("탑승", "boarding; embarkation"), ("승객", "a passenger; “riding guest”"), ("승용차", "a car; “vehicle for riding use”"), ("승무원", "a crew member; a flight attendant; “riding and working member”"),
            ("여권", "a passport; “travel document”"), ("입장권", "an admission ticket; “entrance ticket”"), ("상품권", "a gift certificate; “commodity bill”")]
L1 = lesson(
    "Ch 13 · Topic A: At the International Terminal",
    "국제선 터미널에서 · 탑승권 · 여권 · 면세점 · 탑승구 · 승무원 · 승 (乘) · 권 (券)",
    requires=[],
    cards=[
        card("What Chapter 13 teaches (한국에 오신 것을 환영합니다)",
             "Chapter 13, “Welcome to Korea”, opens Unit 4 of the Semester 1 Student’s Edition (A Visit to Korea, 한국 방문). It has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about flight information including date, time, and flight number; comprehend and respond to flight announcements; understand the boarding procedures at an international airport; answer questions at the customs and immigration office; request in-flight services; request information about airport facilities and services; and describe the size, color, and shape of objects.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the noun connector ~(이)나 (or); expressing total negation with 아무 ~도; the conjunctive ending -(으)려고 (in order to; so as to); the conjunctive ending -(으)려면 (if one intends to, if one plans to); and the Sino-Korean syllables 권 (券), 승 (乘), 착 (着), and 면 (免)."),
        card("Topic A: At the International Terminal",
             "The text is SPC Anderson’s journal entry about his first international flight experience at San Francisco International Airport. (The English is mine. The book writes the flight number as KE024편; Latin letters and digits are respelled in Hangul here, 케이이공이사편.)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter).",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Sino-Korean in use: 승 (乘)",
             "This Sino-Korean syllable means riding or getting on (a flight, ship, bus, rollercoaster, horse, etc.), as in 탑승 (boarding; embarkation), 승객 (a passenger; “riding guest”), 승용차 (a car; “vehicle for riding use”), and 승무원 (a crew member; a flight attendant; “riding and working member”). The book asks you to guess the meaning of 승차, 승마 and 승선; my answers are in the last card.",
             tables=[ktable(_SINO_A2[:4])]),
        card("Sino-Korean in use: 권 (券)",
             "This Sino-Korean syllable means a document, a ticket, or a bill, as in 여권 (a passport; “travel document”), 입장권 (an admission ticket; “entrance ticket”), and 상품권 (a gift certificate; “commodity bill”). The book asks you to guess the meaning of 할인권 and 탑승권.",
             tables=[ktable(_SINO_A2[4:])]),
        card("Guess the meaning (my answers)",
             "The book leaves the blanks empty; these answers are mine, worked out from the syllables.",
             tables=[ktable(_SINO_A)]),
        card("Activities left out",
             "The vocabulary slide show, the SMART Board activities, the Taboo game, the paired phrase-translation sets, the sentence-strip sequencing activity, Follow-up 1 (listening to six narratives about boarding an international flight and numbering the pictures) and Follow-up 2 (listening to three conversations to decide whether they take place in flight, at the duty-free shop or at the ticket counter) are picture, audio, game or partner activities. The Useful Links (Incheon International Airport, Korean Air, Asiana Airlines) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if w != "-(으)려고" and w != "~에 대해서"]))
        + _tr(_A_TXT)
        + _tr(_SINO_A2)
        + [M("Where did SPC Anderson go first after arriving at the airport?", "The international terminal", ["The boarding gate", "The duty-free shop", "The hotel"], "국제선 터미널로 갔습니다."),
           M("What did Anderson show the airline employee at the counter?", "His passport", ["His boarding pass", "His visa", "His luggage"], "항공사 직원한테 여권을 보여주었습니다."),
           M("What did Anderson receive at the counter?", "A boarding pass", ["A visa", "A seat belt", "A blanket"], "탑승권을 받았습니다."),
           M("What did Anderson do after checking in his baggage?", "He went to take the plane", ["He went home", "He went to the hotel", "He called a friend"], "짐을 부친 후 비행기를 타러 갔습니다."),
           M("Why did Anderson stop by the duty-free shop?", "To buy a present for a friend", ["To exchange money", "To buy a ticket", "To look for his seat"], "친구 선물을 사려고 면세점에 들렀습니다."),
           M("Where did he give his boarding pass to the airline employee?", "At the boarding gate", ["At the counter", "In the plane", "At the duty-free shop"], "탑승구에 도착한 후 항공사 직원에게 탑승권을 주었습니다."),
           M("Who showed Anderson to his seat?", "A flight attendant", ["A passenger", "An airline employee at the gate", "A friend"], "승무원이 좌석을 안내해 주었습니다."),
           M("What did Anderson listen to after sitting down?", "An explanation about a safe flight", ["An announcement about customs", "A movie", "A song"], "안전여행에 대해서 설명을 들었습니다."),
           M("Which Sino-Korean syllable means “to ride on”?", "승 (乘)", ["권 (券)", "착 (着)", "면 (免)"], "탑승, 승객, 승무원."), M("Which Sino-Korean syllable means “a document; a ticket; a bill”?", "권 (券)", ["승 (乘)", "착 (着)", "면 (免)"], "여권, 입장권, 상품권."),
           M("Which word means “a boarding pass”?", "탑승권", ["탑승구", "여권", "입장권"], "탑승 + 권 = boarding + ticket."), M("Which word means “a passport”?", "여권", ["탑승권", "상품권", "입장권"], "여권 = travel document."),
           M("Which word means “a passenger”?", "승객", ["승무원", "직원", "승용차"], "승객 = riding guest."), M("Which word means “a flight attendant”?", "승무원", ["승객", "직원", "터미널"], "승무원 = riding and working member."),
           M("Which word means “a boarding gate”?", "탑승구", ["탑승권", "터미널", "카운터"], "탑승구 = boarding gate."), M("Which word means “a gift certificate”?", "상품권", ["입장권", "여권", "탑승권"], "상품권 = commodity bill."),
           F("공항에 도착해서 국제선 ___로 갔습니다. (terminal)", "터미널", ["카운터", "탑승구"], "터미널 = a terminal."), F("항공사 직원한테 ___을 보여주었습니다. (passport)", "여권", ["탑승구", "좌석"], "여권 = a passport."),
           F("카운터에서 ___을 부친 후 비행기를 타러 갔습니다. (baggage)", "짐", ["담요", "여권"], "짐 = luggage."), F("친구 선물을 ___ 면세점에 들렀습니다. (in order to buy)", "사려고", ["사러", "사면"], "사다 + -(으)려고 = 사려고."),
           F("면세점에서 선물을 산 후 ___로 갔습니다. (boarding gate)", "탑승구", ["탑승권", "터미널"], "탑승구 = a boarding gate."), F("___이 좌석을 안내해 주었습니다. (flight attendant)", "승무원", ["승객", "직원한테"], "승무원 = flight attendant."),
           F("비행기가 ___했습니다. (took off)", "이륙", ["착륙", "탑승"], "이륙 = taking off."), F("자리에 앉아서 안전벨트를 ___하고 … (wear)", "착용", ["안내", "설명"], "착용하다 = to wear; to put on."),
           read_q("국제선 터미널"), read_q("탑승권"), read_q("승무원"), read_q("면세점"), read_q("안전벨트")]
    ),
)

# ================================================================== Activities A
_ACT_A = [
    ("공항에 도착하시면 삼 층 안내 모니터에서 항공사의 카운터를 확인하세요.", "When you arrive at the airport, check the airline counter on the information monitor on the third floor.", 1),
    ("탑승할 항공사의 카운터로 가세요.", "Go to the counter of the airline you will board.", 2),
    ("항공사 카운터에서 짐을 부치고 탑승권을 받으세요.", "Check your baggage and receive your boarding pass at the airline counter.", 3),
    ("출발 삼십 분 전부터 탑승을 시작합니다. 탑승시간 삼십 분 전까지 탑승구 앞으로 와 주세요.", "Boarding begins thirty minutes before departure. Please come to the front of the boarding gate thirty minutes before boarding time.", 4),
]
_ACT_A4 = [
    ("대한항공 케이이공이사편으로 한국에 가겠습니다.", "I will go to Korea on Korean Air flight KE024."),
    ("요금이 싸기 때문입니다.", "It is because the fare is cheap."),
    (f"이 비행기는 시카고 공항에서 {month_ko(10)} {day_ko(5)} 오전 {clock(11, 15)}에 출발합니다.", "This plane leaves Chicago airport at 11:15 a.m. on October 5."),
    (f"그리고 인천국제공항에 {month_ko(10)} {day_ko(6)} 오후 {clock(5)}쯤 도착합니다.", "And it arrives at Incheon International Airport around 5 p.m. on October 6."),
    ("시카고에서 한국까지 열세 시간쯤 걸립니다.", "It takes about thirteen hours from Chicago to Korea."),
    ("비행기 표는 천칠백 달러입니다.", "The plane ticket is 1,700 dollars."),
]
L2 = lesson(
    "Ch 13 · Activities A: boarding instructions and choosing a flight",
    "탑승하시기 전에 · 짐을 부치고 탑승권을 받으세요 · 한국에 가겠습니다 · 요금이 싸기 때문입니다",
    requires=[],
    cards=[
        card("Activity 2 (Reading): before boarding",
             "The book shows check-in and boarding instructions written on the back of a boarding pass and asks you to put the steps in order. The four steps below are the book’s (shown here in the order of the book’s boxes, which is scrambled; digits are respelled in Hangul); the English and the order are mine.",
             examples=[D("탑승하시기 전에", "Before boarding")] + [D(ko, f"{en} (step {n})") for ko, en, n in sorted(_ACT_A, key=lambda x: {2: 0, 3: 1, 4: 2, 1: 3}[x[2]])]),
        card("The right order (mine)",
             "The step that is already numbered in the book is step 1 (arriving at the airport and checking the monitor on the third floor).",
             tables=[table(["Step", "Instruction"], [[str(n), ko] for ko, en, n in _ACT_A], say=[1])]),
        card("Activity 4 (Speaking): a model report on the flight you choose",
             "The book asks you to fill in incomplete flight information with a partner, decide which flight to take and report it to the class. Its model report is below (the English is mine; the numbers and the flight code are respelled in Hangul: 십월 오일 is the book’s 10월 5일, 오전 열한 시 십오 분 is 오전 11시 15분, and so on).",
             examples=passage(_ACT_A4)),
        card("Activities left out",
             "The SMART Board activity, Activity 1b (listening to three announcements at the airport or on a plane and saying whom they are for), Activity 3 (a video clip of a passenger asking for flight information at Incheon airport) and the tables of incomplete flight information for two partners are audio, video or partner activities."),
    ],
    exercises=uniq(
        _tr(_strip([(0, k, e) for k, e, _ in _ACT_A]))
        + _tr(_ACT_A4)
        + [M("Which is the first step of the boarding instructions?", "Check the airline counter on the monitor on the third floor", ["Check your baggage and receive your boarding pass", "Come to the boarding gate", "Go to the airline counter"], "공항에 도착하시면 … 확인하세요 is step 1."),
           M("Which step comes right after checking the monitor?", "Go to the counter of the airline you will board", ["Come to the boarding gate", "Receive your boarding pass", "Board the plane"], "탑승할 항공사의 카운터로 가세요 is step 2."),
           M("What do you do at the airline counter?", "Check your baggage and receive your boarding pass", ["Show your passport at the gate", "Buy duty-free items", "Exchange money"], "짐을 부치고 탑승권을 받으세요."),
           M("When does boarding begin?", "Thirty minutes before departure", ["At departure", "An hour before departure", "Ten minutes before departure"], "출발 삼십 분 전부터 탑승을 시작합니다."),
           M("Where should you be thirty minutes before boarding time?", "In front of the boarding gate", ["At the airline counter", "At the duty-free shop", "In the plane"], "탑승구 앞으로 와 주세요."),
           M("Which flight does the model report choose?", "Korean Air KE024", ["Asiana Airlines OZ045", "Asiana Airlines KE024", "Korean Air OZ045"], "대한항공 케이이공이사편으로 한국에 가겠습니다."),
           M("Why does the model report choose that flight?", "The fare is cheap", ["The seat is big", "It is the fastest", "The food is good"], "요금이 싸기 때문입니다."),
           M("Where does the model flight depart from?", "Chicago", ["San Francisco", "Seoul", "Los Angeles"], "시카고 공항에서 출발합니다."),
           M("Where does the model flight arrive?", "Incheon International Airport", ["Gimpo airport", "Chicago airport", "Busan airport"], "인천국제공항에 도착합니다."),
           M("How long does the flight take from Chicago to Korea?", "About thirteen hours", ["About three hours", "About thirty hours", "About eleven hours"], "열세 시간쯤 걸립니다."),
           M("How much is the plane ticket in the model report?", "1,700 dollars", ["700 dollars", "1,070 dollars", "17,000 dollars"], "천칠백 달러 = 1,700 dollars."),
           F("탑승 시간 삼십 분 ___ 탑승구 앞으로 와 주세요. (until)", "전까지", ["후에", "동안"], "전까지 = until (before)."), F("비행기 표는 ___ 달러입니다. (1,700)", "천칠백", ["칠백", "천칠십"], "천칠백 = 1,700."),
           F("요금이 싸기 ___입니다. (because)", "때문", ["동안", "마다"], "-기 때문입니다 = it is because …"), F("한국에 ___. (I will go)", "가겠습니다", ["갑니다", "갔습니다"], "-겠습니다 expresses a firm intention."),
           F("항공사 카운터에서 짐을 ___ 탑승권을 받으세요. (check, and)", "부치고", ["부치면", "부쳐서"], "부치다 + -고 = 부치고."), F("이 비행기는 시카고 공항에서 ___에 출발합니다. (at 11:15 a.m.)", "오전 열한 시 십오 분", ["오후 열한 시 십오 분", "오전 십일 시 십오 분"], "Hour: native 열한 시; minute: Sino-Korean 십오 분."),
           read_q("탑승하시기 전에"), read_q("출발합니다"), read_q("인천국제공항"), read_q("요금이 싸기 때문입니다"), read_q("부치고")]
    ),
)

# ================================================================== Topic B
_B_TXT = [
    ("비행기가 이륙했습니다.", "The plane took off."),
    ("세 시간쯤 후에 기내식이 나왔습니다.", "About three hours later the in-flight meal came out."),
    ("비빔밥이나 불고기 중에서 하나를 고를 수 있었습니다.", "I was able to choose one of bibimbap or bulgogi."),
    ("식사를 한 후 한국 영화를 봤습니다.", "After eating, I watched a Korean movie."),
    ("그리고 기내에서 파는 면세품을 샀습니다.", "And I bought duty-free items sold in the plane."),
    ("비행기가 착륙하기 전에 승무원이 출입국 신고서를 갖다 주었습니다.", "Before the plane landed, the flight attendant brought me an arrival and departure card."),
    ("비행기가 연착돼서 한 시간쯤 늦게 인천국제공항에 도착했습니다.", "The plane was delayed, so I arrived at Incheon International Airport about an hour late."),
    ("출입국 사무소 직원에게 비자, 여권, 세관 신고서를 보여주었습니다.", "I showed my visa, passport and customs declaration form to the employee at the immigration office."),
    ("그리고 입국 신고서도 냈습니다.", "And I also turned in my entry card."),
    ("직원이 방문 목적과 방문 기간 등을 물어보았습니다.", "The employee asked about the purpose and the length of my visit and so on."),
    ("짐을 찾은 후에 세관을 통과했습니다.", "After I found my baggage, I passed through customs."),
    ("세관에 신고할 물건이 아무것도 없어서 세관을 빨리 통과할 수 있었습니다.", "I had nothing to declare at customs, so I was able to pass through customs quickly."),
]
_B_WORDS = ["기내(식)", "기간", "내다", "담요", "~등", "면세품", "목적", "물어보다/묻다", "비자", "빨리", "세관", "신고", "신고서", "아무", "연착", "~(이)나", "입국", "~중(에/에서)", "착륙", "출국", "출입국", "통과"]
_SINO_B = [("착륙", "landing; “come into contact with land”"), ("착용", "putting on a safety belt; “putting on and using”"), ("도착", "arrival"), ("연착", "delayed arrival")]
_SINO_B2 = [("면세", "tax exemption"), ("면역", "immunity; “exemption from diseases”"), ("면허", "a license; a permit; “exempt from permission”"), ("운전면허", "a driver’s license"), ("사업면허", "a business license")]
L3 = lesson(
    "Ch 13 · Topic B: The plane has been delayed",
    "비행기가 연착되었습니다 · 기내식 · 출입국 신고서 · 세관 · 착 (着) · 면 (免)",
    requires=[],
    cards=[
        card("Topic B: The plane has been delayed",
             "The text is SPC Anderson’s diary entry about the in-flight service and the arrival at Incheon International Airport. The first paragraph is about the flight, the second about immigration and customs. (The English is mine.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter). The book writes 기내(식), 신고(하다), 연착(하다/되다), 입국(하다), 착륙(하다), 출국(하다), 통과(하다) and 물어보다 / 묻다 with the optional parts in parentheses; the optional parts are kept in the meanings here.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Sino-Korean in use: 착 (着)",
             "The underlying meaning of this Sino-Korean syllable is physical contact or touch (with a larger object). Depending on the context it can translate to touch, stick to, put on (clothes, hat, shoes, etc.), or arrive, as in 착륙 (landing; “come into contact with land”), 착용 (putting on a safety belt; “putting on and using”), 도착 (arrival), 연착 (delayed arrival), etc.",
             tables=[ktable(_SINO_B)]),
        card("Sino-Korean in use: 면 (免)",
             "This Sino-Korean syllable means escape, avoid, or exempt, as in 면세 (tax exemption), 면역 (immunity; “exemption from diseases”), and 면허 (a license; a permit; “exempt from permission”). Note that 면허, which literally means “exempt from permission”, refers to a license or permit, as in 운전면허 (driver’s license) and 사업면허 (business license). How can this be? When you get 면허, you are exempt from further permission from authorities and you have your own license to enjoy!",
             tables=[ktable(_SINO_B2)]),
        card("Activities left out",
             "The SMART Board activities, Follow-up 1 (listening to four conversations in flight or at the airport and writing each question and answer in English) and Follow-up 2 (filling in the entry card 입국 신고서, k-eta.go.kr, and the traveler’s customs declaration 여행자 휴대품 신고서, customs.go.kr, in Korean) are audio, picture or website activities; the two forms are pictures."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if w not in ("~(이)나", "~중(에/에서)", "~등")]))
        + _tr(_B_TXT)
        + _tr(_SINO_B + _SINO_B2)
        + [M("When did the in-flight meal come out?", "About three hours after takeoff", ["Right after takeoff", "Before takeoff", "Before landing"], "세 시간쯤 후에 기내식이 나왔습니다."),
           M("What could Anderson choose from for the in-flight meal?", "Bibimbap or bulgogi", ["Kimchi or rice", "Noodles or soup", "Chicken or beef"], "비빔밥이나 불고기 중에서 하나를 고를 수 있었습니다."),
           M("What did Anderson do after the meal?", "He watched a Korean movie", ["He slept", "He read a book", "He bought a blanket"], "식사를 한 후 한국 영화를 봤습니다."),
           M("What did the flight attendant bring before landing?", "An arrival and departure card", ["A blanket", "A visa", "A boarding pass"], "출입국 신고서를 갖다 주었습니다."),
           M("Why did the plane arrive late?", "It was delayed", ["It took off late", "It landed in the wrong place", "The weather was good"], "비행기가 연착돼서 한 시간쯤 늦게 도착했습니다."),
           M("How late did the plane arrive?", "About one hour", ["About three hours", "About thirty minutes", "It was on time"], "한 시간쯤 늦게 도착했습니다."),
           M("What did Anderson show the immigration office employee?", "His visa, passport and customs declaration form", ["His boarding pass", "His baggage", "His ticket and money"], "비자, 여권, 세관 신고서를 보여주었습니다."),
           M("What did the employee ask about?", "The purpose and the length of his visit", ["His hometown", "His family", "His baggage"], "방문 목적과 방문 기간 등을 물어보았습니다."),
           M("When did Anderson pass through customs?", "After he found his baggage", ["Before he got his baggage", "Before landing", "Before the immigration office"], "짐을 찾은 후에 세관을 통과했습니다."),
           M("Why could Anderson pass through customs quickly?", "He had nothing to declare", ["He was a soldier", "He had no baggage", "The customs was closed"], "신고할 물건이 아무것도 없어서 빨리 통과할 수 있었습니다."),
           M("Which word means “landing”?", "착륙", ["이륙", "도착", "탑승"], "착륙 = landing."), M("Which word means “arrival”?", "도착", ["출발", "착륙", "이륙"], "도착 = arrival."),
           M("Which word means “tax exemption”?", "면세", ["면역", "면허", "납세"], "면세 = tax exemption."), M("Which word means “a driver’s license”?", "운전면허", ["사업면허", "여권", "비자"], "운전면허 = driver’s license."),
           M("Which Sino-Korean syllable means “arrival; to touch”?", "착 (着)", ["승 (乘)", "권 (券)", "면 (免)"], "착륙, 착용, 도착, 연착."), M("Which Sino-Korean syllable means “to exempt; to avoid”?", "면 (免)", ["착 (着)", "승 (乘)", "권 (券)"], "면세, 면역, 면허."),
           M("Which word means “departure from the country”?", "출국", ["입국", "통과", "신고"], "출국 = leaving a country."), M("Which word means “entry into a country”?", "입국", ["출국", "통과", "신고"], "입국 = entering a country."),
           F("비빔밥___ 불고기 중에서 하나를 고를 수 있었습니다. (or)", "이나", ["나", "을"], "비빔밥 ends in a consonant: 이나."), F("비행기가 ___돼서 한 시간 늦게 도착했습니다. (delayed)", "연착", ["착륙", "도착"], "연착되다 = to be delayed."),
           F("직원이 방문 ___과 방문 기간 등을 물어보았습니다. (purpose)", "목적", ["신고", "통과"], "목적 = purpose."), F("세관에 신고할 물건이 ___ 없어서 … (nothing)", "아무것도", ["아무도", "하나만"], "아무것도 = nothing (with a negative)."),
           F("짐을 찾은 후에 세관을 ___했습니다. (passed through)", "통과", ["신고", "입국"], "통과하다 = to pass through."), F("입국 신고서를 ___습니다. (turned in)", "냈", ["찾았", "탔"], "내다 = to submit; 내 + ㅆ = 냈."),
           read_q("비행기가 연착되었습니다"), read_q("출입국 신고서"), read_q("세관"), read_q("물어보았습니다"), read_q("방문 기간")]
    ),
)

# ================================================================== Grammar A: (이)나
_NA_EX = [("샌프란시스코나 산호세", "(either) San Francisco or San Jose"), ("한국말이나 일본말", "(either) Korean or Japanese"), ("한식이나 일식", "(either) Korean food or Japanese food (mine)"), ("지갑이나 벨트", "a wallet or a belt (mine)"), ("사과나 배", "an apple or a pear (mine)")]
_NA_DLG = [
    ("A", "저녁에 보통 뭐 드세요?", "What do you usually eat for dinner?"), ("B", "보통 한식이나 일식을 먹어요.", "I usually eat Korean or Japanese food."),
    ("A", "이번 주말에 어디에 갈까요?", "Where shall we go this weekend?"), ("B", "샌프란시스코나 산호세에 갑시다.", "Let’s go to San Francisco or San Jose."),
]
_NA_LIST = [("책", "연필"), ("편지", "이메일"), ("음료수", "아이스크림"), ("달리기", "테니스"), ("여름", "겨울"), ("산", "바다"), ("수영", "스키"), ("비행기", "기차"), ("커피숍", "서점"), ("백화점", "공원")]
_NA_EN = {"책": "a book", "연필": "a pencil", "편지": "a letter", "이메일": "an e-mail", "음료수": "a drink", "아이스크림": "ice cream", "달리기": "running", "테니스": "tennis", "여름": "summer", "겨울": "winter", "산": "a mountain", "바다": "the sea",
          "수영": "swimming", "스키": "skiing", "비행기": "an airplane", "기차": "a train", "커피숍": "a coffee shop", "서점": "a bookstore", "백화점": "a department store", "공원": "a park"}
_NA_SEN = [("A", "책이나 연필 주세요.", "Please give me a book or a pencil."), ("A", "여름이나 겨울에 가세요.", "Go in summer or winter. (mine)"), ("A", "산이나 바다에 갑시다.", "Let’s go to the mountains or the sea. (mine)"),
           ("A", "수영이나 스키를 좋아해요.", "I like swimming or skiing. (mine)"), ("A", "비행기나 기차로 갑시다.", "Let’s go by plane or by train. (mine)"), ("A", "커피숍이나 서점에서 만나요.", "Let’s meet at a coffee shop or a bookstore. (mine)")]
L4 = lesson(
    "Ch 13 · Grammar A: the noun connector ~(이)나",
    "한식이나 일식 · 지갑이나 벨트 · 사과나 배 · 샌프란시스코나 산호세",
    requires=[],
    cards=[
        card("The noun connector ~(이)나 (or)",
             "As the name suggests, the noun connector ~(이)나 is used to connect nouns and is translated as “or” or “either … or”: 샌프란시스코나 산호세 ((either) San Francisco or San Jose), 한국말이나 일본말 ((either) Korean or Japanese). When a noun ends in a consonant add 이나 (한식이나 일식, 지갑이나 벨트, 사과나 배); when a noun ends in a vowel add 나 (샌프란시스코나 산호세).",
             tables=[table(["Condition", "Rule", "Example"], [["A noun ends in a consonant", "add 이나", "한식이나 일식; 지갑이나 벨트"], ["A noun ends in a vowel", "add 나", "샌프란시스코나 산호세; 사과나 배"]], title="noun + (이)나 + noun", say=[2])],
             examples=[D(a, b) for a, b in _NA_EX[:2]]),
        card("Two model dialogs",
             "The book’s two examples (the English is mine).",
             examples=dlg(_NA_DLG)),
        card("Follow-up 1: add (이)나 and a noun",
             "In the book Student A reads a noun from List A and Student B adds (이)나 and a noun from List B; Student A then makes a sentence with both nouns and an appropriate verb. The two lists are the book’s (책–연필, 편지–이메일, 음료수–아이스크림, 달리기–테니스, 여름–겨울, 산–바다, 수영–스키, 비행기–기차, 커피숍–서점, 백화점–공원); the phrases below are made by the rule (mine). The only sentence the book gives is the model 책이나 연필 주세요.",
             tables=[table(["List A", "List B", "With (이)나", "Meaning"], [[a, b, _na(a, b), f"{_NA_EN[a]} or {_NA_EN[b]}"] for a, b in _NA_LIST], say=[0, 1, 2])]),
        card("Sentences with (이)나 (mine, from the book’s lists)",
             "The book leaves the verb to the student. These sentences are my examples; the first one is the book’s model.",
             examples=[D(k, e) for _, k, e in _NA_SEN]),
        card("Activities left out",
             "Follow-up 2 (listening to four conversations in which one person offers choices and another responds, to write the choices, the choice and the reason in English) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Add ~(이)나 to join {a} and {b}.", _na(a, b), [b + ("나" if has_final(b) else "이나") + " " + a if False else (a + ("나" if has_final(a) else "이나") + " " + b), a + "을 " + b if False else a + ("은" if has_final(a) else "는") + " " + b][:2], f"{a} ends in a {'consonant' if has_final(a) else 'vowel'}, so it takes {'이나' if has_final(a) else '나'}.") for a, b in _NA_LIST]
        + [F(f"{a}___ {b} 주세요. (or)", "이나" if has_final(a) else "나", ["나" if has_final(a) else "이나"], f"{a} ends in a {'consonant' if has_final(a) else 'vowel'}: {'이나' if has_final(a) else '나'}.") for a, b in _NA_LIST]
        + _tr([(a, b) for a, b in _NA_EX[:2]] + _strip(_NA_DLG) + [(k, e.replace(" (mine)", "")) for _, k, e in _NA_SEN])
        + [M("What does ~(이)나 mean between two nouns?", "or; either … or", ["and; with", "only", "also"], "한식이나 일식 = Korean or Japanese food."), M("Which is added to a noun that ends in a vowel?", "나", ["이나", "은", "를"], "샌프란시스코나 산호세."),
           M("Which is added to a noun that ends in a consonant?", "이나", ["나", "는", "가"], "한식이나 일식."), M("What do you usually eat for dinner? How does B answer in the book?", "보통 한식이나 일식을 먹어요.", ["보통 한식이랑 일식을 먹어요.", "보통 한식만 먹어요.", "보통 안 먹어요."], "한식이나 일식 = Korean or Japanese food."),
           M("Where does B suggest going this weekend?", "San Francisco or San Jose", ["San Francisco and San Jose", "Only San Jose", "Los Angeles"], "샌프란시스코나 산호세에 갑시다."), M("Which phrase means “a wallet or a belt”?", "지갑이나 벨트", ["지갑과 벨트", "지갑이 벨트", "지갑도 벨트"], "지갑 + 이나 + 벨트."),
           M("Which phrase means “an apple or a pear”?", "사과나 배", ["사과이나 배", "사과을 배", "사과는 배"], "사과 ends in a vowel: 나."), M("Which phrase is correct?", "비행기나 기차", ["비행기이나 기차", "비행기은 기차", "비행기를 기차"], "비행기 ends in a vowel."),
           M("Which phrase is correct?", "백화점이나 공원", ["백화점나 공원", "백화점은 공원", "백화점를 공원"], "백화점 ends in a consonant."), M("Which phrase is correct?", "달리기나 테니스", ["달리기이나 테니스", "달리기는 테니스", "달리기을 테니스"], "달리기 ends in a vowel."),
           read_q("한식이나 일식"), read_q("지갑이나 벨트"), read_q("사과나 배"), read_q("산이나 바다"), read_q("커피숍이나 서점")]
    ),
)

# ================================================================== Grammar B: total negation
_TN_EX = [
    ("지난 주말에 아무도 안 만났어요.", "Last weekend, I didn’t meet anyone."), ("지난 주말에 아무 책도 안 읽었어요.", "Last weekend, I didn’t read any books."), ("지난 주말에 아무 데도 안 갔어요.", "Last weekend, I didn’t go anywhere."),
    ("지난 주말에 아무것도 안 했어요.", "Last weekend, I didn’t do anything."), ("교실에 아무도 없어요.", "There is no one in the classroom."), ("아무도 한국말을 못해요.", "No one speaks Korean."),
    ("교실에 아무것도 없어요.", "There is nothing in the classroom."), ("저는 아무 취미도 없어요.", "I don’t have any hobbies."), ("저는 취미가 하나도 없어요.", "I don’t have even one hobby."), ("교실에 학생이 한 명도 없어요.", "There isn’t even one student in the classroom."),
]
_TN_MK = [("아무한테도", "(not) … to any one"), ("아무 곳에서도", "(not) … at any place"), ("아무 펜으로도", "(not) … with any pen")]
_TN_FILL = [("어제 저녁에 비가 많이 왔어요. 그래서 파티에 사람이 ___ 안 왔어요.", "한 명도", "아무도", "Last night it rained a lot, so not a single person came to the party. (아무도 also works)"),
            ("이번 주말에 너무 피곤했어요. 그래서 ___ 안 하고 집에서 쉬었어요.", "아무것도", "한 개도", "I was too tired this weekend, so I did nothing and rested at home."),
            ("이번 크리스마스에 쇼핑을 많이 했어요. 그래서 돈이 없어서 ___ 못 갔어요.", "아무 데도", "아무도", "I did a lot of shopping this Christmas, so I have no money and could not go anywhere."),
            ("지난 주에 너무 바빠서 식품점에 못 갔어요. 그래서 지금 집에 먹을 것이 ___ 없어요.", "아무것도", "한 개도", "Last week I was too busy and could not go to the grocery store, so now there is nothing to eat at home. (한 개도 also works)")]
_TN_SURV = [("A", "몇 명이 세븐 업이나 콜라를 마셨습니까?", "How many people drank 7 Up or cola?"), ("B", "십오 명이 세븐 업이나 콜라를 마셨습니다.", "Fifteen people drank 7 Up or cola."),
            ("A", "몇 명이 지갑이나 핸드백을 샀습니까?", "How many people bought a wallet or a handbag?"), ("B", "지갑이나 핸드백은 아무도 안 샀습니다.", "No one bought a wallet or a handbag.")]
L5 = lesson(
    "Ch 13 · Grammar B: total negation with 아무 ~도",
    "아무도 · 아무것도 · 아무 데도 · 아무 책도 · 하나도 · 한 명도",
    requires=[],
    cards=[
        card("Partial and total negation",
             "Compare the two English sentences “We do not need all the apples for the pie” and “We do not need any apples for the pie”. The first indicates that some but not all apples are needed, which is a partial negation; the second indicates that no apples are needed, which is a total negation.\n\nIn Korean we can express a total negation as: 아무도 / 아무 noun도 … negative verb. Since 아무 means “anyone” or “any” and the marker 도 means “even” or “also”, the translations are “… not meet … even one person”, “… not read … even one book”, “… not go … even one place” and “… not do … even one thing”.",
             tables=[table(["Pattern", "Meaning"], [["아무도 … negative verb", "no one; not anyone"], ["아무 noun도 … negative verb", "not any (noun)"], ["아무것도 … negative verb", "nothing; not anything"], ["아무 데도 … negative verb", "nowhere; not anywhere"]], title="Expressing total negation")],
             examples=[D(a, b) for a, b in _TN_EX[:4]]),
        card("More examples",
             "교실에 아무도 없어요 (There is no one in the classroom); 아무도 한국말을 못해요 (No one speaks Korean); 교실에 아무것도 없어요 (There is nothing in the classroom); 저는 아무 취미도 없어요 (I don’t have any hobbies).",
             examples=[D(a, b) for a, b in _TN_EX[4:8]]),
        card("Adding another marker",
             "If we have to add an additional marker, such as 에서, 에, 한테, or (으)로, to 아무 (noun)도, the marker comes right before 도: 아무한테도 ((not) … to any one), 아무 곳에서도 ((not) … at any place), 아무 펜으로도 ((not) … with any pen).",
             tables=[ktable(_TN_MK)]),
        card("하나도 and 한 명도",
             "We can also express a total negation by using 하나도 (even one), 한 명도 (even one person), etc.: 저는 취미가 하나도 없어요 (I don’t have even one hobby); 교실에 학생이 한 명도 없어요 (There isn’t even one student in the classroom).",
             examples=[D(a, b) for a, b in _TN_EX[8:]]),
        card("Follow-up 3: fill in the blanks",
             "The book gives the box 아무것도 · 한 개도 · 한 명도 · 아무 데도 · 아무도 and says some sentences may have more than one answer. The sentences are the book’s; the answers are mine.",
             tables=[table(["Completed sentence", "Answer", "Also possible", "Meaning (mine)"], [[s.replace("___", a), a, b, e] for s, a, b, e in _TN_FILL], say=[0])]),
        card("Follow-up 5: the survey (model questions)",
             "The book shows survey results of 100 passengers about in-flight services (meals, beverages, duty-free items); partners ask each other for the missing information and write the results in Korean. The two models are below (the English is mine; 15명 is spelled out as 십오 명).",
             examples=dlg(_TN_SURV)),
        card("Activities left out",
             "Follow-up 4 (listening to four conversations between a passenger and an immigration officer to translate the sentence with 아무 (noun)도) is an audio activity, and the survey tables (Survey Results A and B) are partner activities."),
    ],
    exercises=uniq(
        _tr(_TN_EX + _TN_MK + _strip(_TN_SURV))
        + [F(s, a, [b2 for b2 in ("아무도", "아무것도", "아무 데도", "한 명도") if b2 not in (a, b)][:2], f"{e}") for s, a, b, e in _TN_FILL]
        + [F("교실에 ___ 없어요. (no one)", "아무도", ["아무것도", "아무 데도"], "아무도 = no one."), F("교실에 ___ 없어요. (nothing)", "아무것도", ["아무도", "아무 데도"], "아무것도 = nothing."), F("주말에 ___ 안 갔어요. (anywhere)", "아무 데도", ["아무것도", "아무도"], "아무 데도 = anywhere (not)."),
           F("저는 ___ 취미도 없어요. (any)", "아무", ["하나", "한"], "아무 + noun + 도."), F("교실에 학생이 ___ 없어요. (not even one)", "한 명도", ["한 개도", "아무것도"], "한 명도 = not even one person."), F("저는 취미가 ___ 없어요. (not even one)", "하나도", ["한 명도", "아무도"], "하나도 = not even one."),
           F("지난 주말에 ___ 안 만났어요. (anyone)", "아무도", ["아무것도", "아무 데도"], "아무도 안 만났어요."), F("아무___ 말하지 않았어요. (to anyone)", "한테도", ["도", "에서도"], "The marker 한테 comes before 도: 아무한테도."), F("아무 곳___ 안 갔어요. (to any place)", "에도", ["도", "한테도"], "에 + 도 = 에도."),
           F("아무 펜___ 안 썼어요. (with any pen)", "으로도", ["에도", "한테도"], "(으)로 + 도 = 으로도."), F("아무 곳에서___ 안 놀았어요. (at any place)", "도", ["는", "가"], "에서 + 도 = 에서도."),
           M("What does 아무 mean?", "any; anyone", ["all", "every", "some"], "아무 = any."), M("What does the marker 도 mean in 아무도?", "even; also", ["only", "and", "if"], "도 = even; also."),
           M("What kind of verb must come after 아무도 / 아무 noun도?", "A negative verb", ["A positive verb", "A past verb only", "A question"], "아무도 안 만났어요; 아무것도 없어요."), M("Which sentence is a TOTAL negation?", "아무도 안 왔어요.", ["다 안 왔어요.", "다 왔어요.", "조금 왔어요."], "아무도 안 왔어요 = no one came."),
           M("Where does an extra marker such as 에서 go?", "Right before 도", ["After 도", "Before 아무", "It is dropped"], "아무 곳에서도."), M("Which sentence means “There isn’t even one student in the classroom”?", "교실에 학생이 한 명도 없어요.", ["교실에 학생이 아무것도 없어요.", "교실에 아무도 있어요.", "교실에 학생이 많아요."], "한 명도 없어요 = not even one person."),
           read_q("아무도"), read_q("아무것도"), read_q("아무 데도"), read_q("한 명도"), read_q("아무한테도")]
    ),
)

# ================================================================== Activities B
_DF = [
    ("국제선 비행기를 타면 기내 면세점 서비스를 이용할 수 있습니다.", "If you take an international flight, you can use the in-flight duty-free shop service."),
    ("기내 면세품으로는 화장품이 가장 많고 액세서리(시계, 목걸이), 담배, 초콜릿, 볼펜 등도 있습니다.", "Among in-flight duty-free items, cosmetics are the most, and there are also accessories (watches, necklaces), cigarettes, chocolate, ballpoint pens and so on."),
    ("기내 면세품 카탈로그는 좌석 앞쪽 포켓에 있습니다.", "The catalog of in-flight duty-free items is in the pocket in front of your seat."),
    ("면세품은 보통 첫 번째 기내식 후에 살 수 있습니다.", "You can usually buy duty-free items after the first in-flight meal."),
]
_DF_W = [("화장품", "cosmetics (mine)"), ("액세서리", "accessories (mine)"), ("시계", "a watch; a clock (mine)"), ("목걸이", "a necklace (mine)"), ("담배", "cigarettes (mine)"), ("초콜릿", "chocolate (mine)"), ("볼펜", "a ballpoint pen (mine)"), ("카탈로그", "a catalog (mine)"), ("앞쪽", "the front side (mine)"), ("포켓", "a pocket (mine)")]
L6 = lesson(
    "Ch 13 · Activities B: in-flight duty-free shopping and the survey",
    "기내 면세점 서비스 · 화장품 · 목걸이 · 카탈로그 · 첫 번째 기내식 후에",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a traveler’s guide on in-flight duty-free items",
             "The excerpt is from a traveler’s guide. The book asks you to answer four questions in English: list at least four items sold in-flight; where you can find a catalog of duty-free items; when you can start buying; and to translate the underlined sentence (which one is underlined cannot be seen in the text, so all four sentences are translated below). The text is the book’s; the English is mine.",
             examples=passage(_DF)),
        card("The answers (mine)",
             "1. Items sold in-flight: cosmetics (the most), accessories (watches, necklaces), cigarettes, chocolate and ballpoint pens. 2. The catalog is in the pocket in front of the seat. 3. You can usually start buying after the first in-flight meal.\n\n"
             "The book does not translate the words of the excerpt; the meanings below are mine.",
             tables=[ktable(_DF_W)]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and listening to four short dialogs to say whether they take place in flight or at the customs counter and what the requests are), Activity 2b (listening to three conversations overheard in flight or at the customs counter), Activity 3 (a drama video clip about an in-flight scene) and Activity 4 (the in-flight role-play with situation cards A and B) are audio, video, game or partner activities."),
    ],
    exercises=uniq(
        _tr(_DF)
        + _tr(_DF_W)
        + [M("Who can use the in-flight duty-free shop service?", "People on international flights", ["People on domestic flights", "Only crew members", "People at the airport"], "국제선 비행기를 타면 … 이용할 수 있습니다."),
           M("Which duty-free item is the most common?", "Cosmetics", ["Chocolate", "Cigarettes", "Ballpoint pens"], "화장품이 가장 많고."), M("Which are examples of accessories in the guide?", "Watches and necklaces", ["Cigarettes and chocolate", "Pens and pockets", "Blankets and seats"], "액세서리(시계, 목걸이)."),
           M("Where is the duty-free catalog?", "In the pocket in front of the seat", ["With the flight attendant", "At the airport counter", "On the boarding pass"], "좌석 앞쪽 포켓에 있습니다."), M("When can you usually buy duty-free items?", "After the first in-flight meal", ["Before takeoff", "Before the in-flight meal", "After landing"], "첫 번째 기내식 후에 살 수 있습니다."),
           F("기내 면세품으로는 ___이 가장 많습니다. (cosmetics)", "화장품", ["초콜릿", "볼펜"], "화장품 = cosmetics."), F("기내 면세품 ___는 좌석 앞쪽 포켓에 있습니다. (catalog)", "카탈로그", ["담배", "시계"], "카탈로그 = catalog."),
           F("면세품은 보통 첫 번째 기내식 ___에 살 수 있습니다. (after)", "후", ["전", "중"], "후 = after."), F("국제선 비행기를 ___ 기내 면세점 서비스를 이용할 수 있습니다. (if you take)", "타면", ["타고", "탔어"], "타다 + -(으)면 = 타면."),
           F("기내 면세점 서비스를 이용할 ___ 있습니다. (can)", "수", ["거", "것"], "-(으)ㄹ 수 있다 = can."), F("볼펜 ___도 있습니다. (and so on)", "등", ["중", "후"], "~등 = and so forth."),
           read_q("기내 면세점"), read_q("화장품"), read_q("목걸이"), read_q("카탈로그"), read_q("첫 번째 기내식")]
    ),
)

# ================================================================== Topic C
_C_DLG = [
    ("항공사 직원", "무엇을 도와 드릴까요?", "How may I help you?"),
    ("존슨", "제 짐이 아직 안 나왔어요. 보라색 가방하고 주황색 배낭이에요.", "My baggage hasn’t come out yet. It is a purple bag and an orange backpack."),
    ("항공사 직원", "그래요? 잠시만요… 여기에는 없습니다. 공항서비스센터에 가시면 잃어버린 물건을 찾으실 수 있습니다.", "Is that so? One moment… It isn’t here. If you go to the Airport Service Center, you can find lost items."),
    ("존슨", "네. 또, 제가 선글라스를 기내에 두고 내렸어요.", "Yes. Also, I left my sunglasses on the plane."),
    ("항공사 직원", "어떤 선글라스입니까?", "What kind of sunglasses are they?"),
    ("존슨", "녹색이고 동그란 모양이에요.", "They are green and round in shape."),
    ("항공사 직원", "잠시만 기다려 주세요. 제가 확인해 보겠습니다.", "Please wait a moment. I will check."),
]
_C_DLG2 = [
    ("존슨", "그리고 제가 돈을 바꾸고 싶어요. 환전하려면 어디로 가야 해요?", "And I want to change money. Where should I go to exchange currency?"),
    ("항공사 직원", "네, 지하 일 층에 가시면 환전소가 있어요.", "Yes, if you go to the first basement floor, there is a currency exchange office."),
    ("존슨", "그럼 핸드폰은 어디에서 빌려요?", "Then where do I rent a cell phone?"),
    ("항공사 직원", "이 층에 가시면 바로 왼쪽에 핸드폰 빌리는 곳이 있습니다.", "If you go to the second floor, there is a place to rent cell phones right on the left."),
    ("존슨", "네, 알겠습니다.", "Yes, I understand."),
]
_C_WORDS = ["가방", "네모", "녹색", "동그랗다", "두고 내리다", "모양", "바꾸다", "배낭", "보라(색)", "세모", "센터", "-(으)려면", "잃어버리다", "주황(색)", "지하", "확인", "환전", "환전소"]
_C_SH = [("네모난 모양", "a rectangular shape (mine)"), ("세모난 모양", "a triangular shape (mine)"), ("동그란 모양", "a round shape (mine)"), ("녹색", "green"), ("보라색", "purple"), ("주황색", "orange")]
L7 = lesson(
    "Ch 13 · Topic C: Where should I go to exchange currency?",
    "환전하려면 어디로 가야 해요? · 짐이 안 나왔어요 · 녹색이고 동그란 모양 · 환전소 · 손전화",
    requires=[],
    cards=[
        card("Topic C: Where should I go to exchange currency?",
             "Mr. Johnson is talking with an airline employee at the baggage claim center. (The English is mine; the book writes 지하 1층 and 2층, spelled out here as 지하 일 층 and 이 층. 가시면 and 찾으실 수 있습니다 are honorific forms: the employee honors the customer.)",
             examples=dlg(_C_DLG)),
        card("Second part: at the desk",
             "While the airline employee is checking the computer at the desk, Mr. Johnson goes on. (The English is mine; the book’s scene note is in English only.)",
             examples=dlg(_C_DLG2)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter). The words for shapes and colors are 네모(나다), 세모(나다), 동그랗다, 모양, 녹색, 보라색 and 주황색; -(으)려면 is explained in a grammar lesson of this chapter.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Describing shape and color",
             "The dialog describes the sunglasses with a color and a shape: 녹색이고 동그란 모양이에요 (they are green and round in shape). The adjective forms are the book’s examples: 저 네모난 모양의 선글라스, 햄버거는 동그란 모양입니다, 아이파드는 네모난 모양입니다, 트라이앵글은 세모난 모양입니다.",
             tables=[ktable(_C_SH)]),
        card("North Korea report",
             "A cellular phone is called 손전화 (“hand phone”) in North Korea, where the use of such phones has been restricted for residents. Foreign tourists who travel there are required to surrender their mobile phones upon arrival. These phones are then sealed and returned only when departing the country. In early 2009, North Korea launched a new cellular phone service that restricts communication to within North Korea only. Subscribers are not able to call or accept calls from outside the country.",
             tables=[ktable([("손전화", "a cell phone in North Korea; “hand phone”"), ("핸드폰", "a cell phone (South Korea)"), ("휴대폰", "a cell phone (South Korea)")])]),
        card("Activities left out",
             "The SMART Board activities, Follow-up 1 (a SMART Board listening activity) and the Useful Links (cell phone rental and roaming services, the airport limousine bus, currency exchange offices; websites) are audio, game or website activities. PFC Hickman’s journal entry (Follow-up 2) is a handwritten picture; it is written out in the activities lesson of this chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if w != "-(으)려면"]))
        + _tr(_strip(_C_DLG + _C_DLG2))
        + _tr(_C_SH[:3])
        + [M("What does Mr. Johnson say first about his baggage?", "It hasn’t come out yet", ["It was lost on the plane", "It is too heavy", "It was stolen"], "제 짐이 아직 안 나왔어요."),
           M("What does Mr. Johnson’s baggage look like?", "A purple bag and an orange backpack", ["A green bag and a purple backpack", "A round bag", "A blue suitcase"], "보라색 가방하고 주황색 배낭이에요."),
           M("Where does the employee say he can find lost items?", "The Airport Service Center", ["The duty-free shop", "The immigration office", "The airline counter"], "공항서비스센터에 가시면 잃어버린 물건을 찾으실 수 있습니다."),
           M("What else did Mr. Johnson leave behind?", "His sunglasses on the plane", ["His passport on the plane", "His cell phone at the hotel", "His backpack at home"], "선글라스를 기내에 두고 내렸어요."),
           M("What do the sunglasses look like?", "Green and round", ["Purple and square", "Orange and triangular", "Black and round"], "녹색이고 동그란 모양이에요."),
           M("What does Mr. Johnson want to do?", "Change money", ["Rent a car", "Buy a ticket", "Check in baggage"], "제가 돈을 바꾸고 싶어요."),
           M("Where is the currency exchange office?", "On the first basement floor", ["On the second floor", "On the first floor", "Next to the gate"], "지하 일 층에 가시면 환전소가 있어요."),
           M("Where can he rent a cell phone?", "On the second floor, right on the left", ["On the first basement floor", "At the gate", "At the baggage claim"], "이 층에 가시면 바로 왼쪽에 핸드폰 빌리는 곳이 있습니다."),
           M("What is a cell phone called in North Korea?", "손전화", ["핸드폰", "휴대폰", "전화기"], "손전화 = “hand phone”."), M("What happens to tourists’ mobile phones when they arrive in North Korea (per the report)?", "They are sealed and returned on departure", ["They are free to use", "They are thrown away", "They are rented out"], "The phones are sealed and returned only when departing."),
           F("제 짐이 ___ 안 나왔어요. (yet)", "아직", ["벌써", "다시"], "아직 안 = not yet."), F("제가 선글라스를 기내에 ___ 내렸어요. (left behind)", "두고", ["잃어", "바꿔"], "두고 내리다 = to leave behind."),
           F("제가 돈을 ___ 싶어요. (change)", "바꾸고", ["바꾸면", "바꿔서"], "바꾸다 + -고 싶다."), F("녹색이고 ___ 모양이에요. (round)", "동그란", ["동그랗다", "동그랗는"], "동그랗다 → 동그란 before a noun."),
           F("___난 모양의 선글라스가 마음에 듭니다. (rectangular)", "네모", ["세모", "동그라"], "네모나다 = to be rectangular."), F("트라이앵글은 ___난 모양입니다. (triangular)", "세모", ["네모", "동그라"], "세모나다 = to be triangular."),
           F("오렌지는 ___입니다. (orange color)", "주황색", ["보라색", "녹색"], "주황색 = orange."), F("저는 ___ 바이올렛 꽃을 좋아합니다. (purple)", "보라색", ["주황색", "녹색"], "보라색 = purple."),
           read_q("환전소"), read_q("공항서비스센터"), read_q("잃어버린 물건"), read_q("동그란 모양"), read_q("선글라스")]
    ),
)

# ================================================================== Grammar C: -(으)려고
_RY_V = [("타다", "to ride; to take"), ("사다", "to buy"), ("가다", "to go"), ("예약하다", "to reserve"), ("배우다", "to learn"), ("살다", "to live"), ("만들다", "to make"), ("놀다", "to play; to have fun"),
         ("찾다", "to look for; to find"), ("먹다", "to eat"), ("읽다", "to read"), ("앉다", "to sit"), ("받다", "to receive")]
_RY_EX = [
    ("한국말을 공부하려고 컴퓨터를 샀어요.", "I bought a computer to learn Korean."), ("점심을 먹으려고 자바 카페에 갔어요.", "I went to the Java Cafe to eat lunch."),
    ("선글라스를 찾으려고 공항서비스센터에 전화했어요.", "I called the airport service center to look for my sunglasses."), ("비행기 표를 사려고 여행사에 갔어요.", "I went to a travel agency to buy a plane ticket."),
]
_RY_FU = [("호텔에 가다", "호텔에 가려고", "버스를 탔습니다", "I took a bus to go to the hotel."), ("비행기표를 예약하다", "비행기표를 예약하려고", "여행사에 전화를 했어요", "I called a travel agency to reserve a plane ticket."),
          ("한국어를 배우다", "한국어를 배우려고", "학원에 갔습니다", "I went to a language school to learn Korean."), ("선물을 사다", "선물을 사려고", "면세점에 들렀습니다", "I stopped by a duty-free shop to buy a present."),
          ("친구하고 같이 먹다", "친구하고 같이 먹으려고", "불고기를 만들었어요", "I made bulgogi to eat with my friend.")]
L8 = lesson(
    "Ch 13 · Grammar C: -(으)려고 (in order to)",
    "타려고 · 살려고 · 찾으려고 · 먹으려고 · 사려고 · 예약하려고",
    requires=[],
    cards=[
        card("Conjunctive endings that express a purpose or intention: -(으)려고",
             "In Chapter 6 you learned that the conjunctive ending -(으)러 is used to express a purpose or intention, as in 식당에 식사하러 오다 (come to the restaurant to eat) and 숙제하러 도서관에 가다 (go to the library to do homework). However, -(으)러 works only with verbs like 가다, 오다 or 다니다. To express a purpose or intention that can work with any action verb (containing 가다, 오다 and 다니다 in the main clause), we can use the conjunctive ending -(으)려고, translated as “(in order) to; so as to”.\n\n"
             "When a verb stem ends in a vowel or ㄹ add 려고 (타다 → 타려고; 살다 → 살려고); when it ends in a consonant other than ㄹ add 으려고 (찾다 → 찾으려고; 먹다 → 먹으려고).",
             tables=[table(["Condition", "Rule", "Example"], [["A verb stem ends in a vowel or ㄹ", "add 려고", "타다 → 타려고; 살다 → 살려고"], ["A verb stem ends in a consonant other than ㄹ", "add 으려고", "찾다 → 찾으려고; 먹다 → 먹으려고"]], title="action verb stem + (으)려고")],
             examples=[D(a, b) for a, b in _RY_EX]),
        card("Forms",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Dictionary form", "Meaning", "-(으)려고"], [[v, m, _ryeo(v)] for v, m in _RY_V], say=[0, 2])]),
        card("Follow-up 1: Column A to Column B, and match with Column C",
             "The book gives five clauses in Column A (호텔에 가다 …), asks you to change them into -(으)려고 in Column B, and to match each with a main clause of Column C (학원에 갔습니다, 버스를 탔습니다, 여행사에 전화를 했어요, 불고기를 만들었어요, 면세점에 들렀습니다). The matches and the English are mine; the book gives the first as the example (호텔에 가려고).",
             tables=[table(["Column A", "Column B", "Matching main clause (mine)", "Meaning (mine)"], [[a, b, c, e] for a, b, c, e in _RY_FU], say=[0, 1, 2])]),
        card("Activities left out",
             "Follow-up 2 (listening to three narrations about an experience at the airport to write the passenger’s intent in English) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the -(으)려고 form of {v} ({m})?", _ryeo(v), [stem(v) + "고", stem(v) + ("러" if _K.decompose(stem(v)[-1])[2] in ("", "ㄹ") else "으러"), stem(v) + ("으려고" if _K.decompose(stem(v)[-1])[2] in ("", "ㄹ") else "려고")], f"{v} → {_ryeo(v)}.") for v, m in _RY_V]
        + _tr(_RY_EX)
        + _tr([(f"{b} {c}.", e) for a, b, c, e in _RY_FU])
        + [F("한국말을 공부___ 컴퓨터를 샀어요. (in order to)", "하려고", ["하으려고", "하러고"], "공부하다 → 공부하려고."), F("점심을 먹___ 자바 카페에 갔어요. (in order to)", "으려고", ["려고", "러고"], "먹다 ends in a consonant: 으려고."), F("선글라스를 찾___ 공항서비스센터에 전화했어요. (in order to)", "으려고", ["려고", "러고"], "찾다 → 찾으려고."),
           F("비행기 표를 사___ 여행사에 갔어요. (in order to)", "려고", ["으려고", "러고"], "사다 ends in a vowel: 려고."), F("친구하고 같이 먹___ 불고기를 만들었어요. (in order to)", "으려고", ["려고", "러고"], "먹다 → 먹으려고."), F("한국어를 배우___ 학원에 갔습니다. (in order to)", "려고", ["으려고", "러고"], "배우다 → 배우려고."),
           F("서울에서 ___려고 집을 찾고 있어요. (in order to live)", "살", ["사", "살으"], "ㄹ stems take 려고 and keep the ㄹ: 살려고."), F("김치를 ___려고 배추를 샀어요. (in order to make)", "만들", ["만드", "만들으"], "만들다 → 만들려고."),
           M("When can -(으)러 be used?", "Only with verbs like 가다, 오다 and 다니다 in the main clause", ["With any verb in the main clause", "Only in the past tense", "Only in questions"], "-(으)러 works only with 가다, 오다, 다니다."), M("What does -(으)려고 express?", "A purpose or intention (in order to)", ["A condition (if)", "Ability (can)", "A reason (because)"], "-(으)려고 = in order to; so as to."),
           M("Which is added to a stem ending in a vowel or ㄹ?", "려고", ["으려고", "러고", "으러"], "타려고, 살려고."), M("Which is added to a stem ending in a consonant other than ㄹ?", "으려고", ["려고", "러고", "으러"], "찾으려고, 먹으려고."),
           M("Which sentence means “I went to a travel agency to buy a plane ticket”?", "비행기 표를 사려고 여행사에 갔어요.", ["비행기 표를 사서 여행사에 갔어요.", "비행기 표를 사면 여행사에 갔어요.", "비행기 표를 샀지만 여행사에 갔어요."], "사려고 = in order to buy."),
           read_q("타려고"), read_q("살려고"), read_q("찾으려고"), read_q("먹으려고"), read_q("예약하려고")]
    ),
)

# ================================================================== Grammar D: -(으)려면
_RM_EX = [
    ("약을 먹으려면 물하고 같이 드세요.", "If you would like to take medicine, please take it with water."), ("핸드폰을 빌리려면 어디로 갑니까?", "If I would like to rent a cellular phone, where should I go?"),
    ("리무진 버스를 타려면 일 층으로 가세요.", "If you intend to take a limousine bus, go to the first floor."), ("예약하려면 무엇이 필요합니까?", "What do I need if I intend to make a reservation?"),
]
_RM_V = [("타다", "to ride; to take"), ("살다", "to live"), ("가다", "to go"), ("빌리다", "to rent; to borrow"), ("예약하다", "to reserve"), ("환전하다", "to exchange money"), ("찾다", "to look for; to find"), ("먹다", "to eat"), ("읽다", "to read"), ("잘하다", "to do well")]
_RM_CHAIN = [("타다", "타려고 하면", "타려면"), ("살다", "살려고 하면", "살려면"), ("찾다", "찾으려고 하면", "찾으려면"), ("먹다", "먹으려고 하면", "먹으려면")]
_RM_DLG = [("A", "한국말을 잘하고 싶어요. 한국말을 잘하려면 어떻게 해야 해요?", "I want to speak Korean well. What should I do to speak Korean well?"), ("B", "한국말을 잘하려면 한국 친구를 많이 만나세요.", "If you want to speak Korean well, meet a lot of Korean friends."),
           ("B", "한국말을 잘하려면 한국 친구를 많이 만나야 합니다.", "To speak Korean well, you must meet a lot of Korean friends.")]
L9 = lesson(
    "Ch 13 · Grammar D: -(으)려면 (if one intends to)",
    "타려면 · 살려면 · 찾으려면 · 먹으려면 · 환전하려면 어떻게 해야 해요?",
    requires=[],
    cards=[
        card("Conditional with intention or wish: -(으)려면",
             "In Chapter 9 you learned that the conjunctive ending -(으)면 expresses a conditional (“if” or “when”), as in 약을 먹으면 (if I take medicine). -(으)려면 is another conjunctive ending that expresses a conditional, but one with intention or wish; it can be translated as “if [the subject] plans to / intends to / would like to / wishes to”. It is a contraction of -(으)려고 하면.\n\n"
             "When a verb stem ends in a vowel or ㄹ add 려면 (타다 → 타려고 하면 → 타려면; 살다 → 살려고 하면 → 살려면); when it ends in a consonant other than ㄹ add 으려면 (찾다 → 찾으려고 하면 → 찾으려면; 먹다 → 먹으려고 하면 → 먹으려면).",
             tables=[table(["Dictionary form", "-(으)려고 하면", "-(으)려면"], [list(r) for r in _RM_CHAIN], title="action verb stem + (으)려면", say=[0, 1, 2])],
             examples=[D(a, b) for a, b in _RM_EX]),
        card("Forms",
             "The forms below are mine, made by the book’s rule.",
             tables=[table(["Dictionary form", "Meaning", "-(으)려면"], [[v, m, _ryeo(v, "면")] for v, m in _RM_V], say=[0, 2])]),
        card("Follow-up 3: join two phrases with -(으)려면",
             "In the book one partner reads a verbal phrase from a list and the other finds a phrase to combine it with, conjugating the first with -(으)려면 (the lists themselves are not in the text; only the model is). The model: A reads 잃어버린 선글라스를 찾다 and B answers 어떻게 해야 합니까? → 잃어버린 선글라스를 찾으려면 어떻게 해야 합니까? (If I would like to find the lost sunglasses, what should I do?)",
             examples=[D("잃어버린 선글라스를 찾으려면 어떻게 해야 합니까?", "If I would like to find the lost sunglasses, what should I do?")]),
        card("Follow-up 5: a wish list and a suggestion",
             "The book asks you to write three wishes, ask a partner for a suggestion with -(으)려면 어떻게 해야 합니까, and write two wishes with the partner’s suggestions in Korean. Its models (the English is mine):",
             examples=dlg(_RM_DLG)),
        card("Activities left out",
             "Follow-up 4 (listening to airline greeting messages that announce different services, to write the service next to each phone button) is an audio activity; the wish-list table is a partner activity."),
    ],
    exercises=uniq(
        [M(f"Which is the -(으)려면 form of {v} ({m})?", _ryeo(v, "면"), [x for x in dict.fromkeys([if_(v), _ryeo(v), stem(v) + ("려면" if _K.decompose(stem(v)[-1])[2] not in ("", "ㄹ") else "으려면")]) if x != _ryeo(v, "면")], f"{v} → {_ryeo(v, '면')}.") for v, m in _RM_V]
        + [M(f"What is the short form of {c[1]}?", c[2], [c[1].replace(" 하면", "고"), _ryeo(c[0]), if_(c[0])], f"-(으)려고 하면 is shortened to -(으)려면: {c[2]}.") for c in _RM_CHAIN]
        + _tr(_RM_EX + _strip(_RM_DLG))
        + [F("약을 먹___ 물하고 같이 드세요. (if you intend to)", "으려면", ["려면", "으면"], "먹다 ends in a consonant: 으려면."), F("핸드폰을 빌리___ 어디로 갑니까? (if I intend to)", "려면", ["으려면", "으면"], "빌리다 ends in a vowel: 려면."), F("리무진 버스를 타___ 일 층으로 가세요. (if you intend to)", "려면", ["으려면", "으면"], "타다 → 타려면."),
           F("예약하___ 무엇이 필요합니까? (if I intend to)", "려면", ["으려면", "으면"], "예약하다 → 예약하려면."), F("한국말을 잘하___ 어떻게 해야 해요? (if I want to)", "려면", ["으려면", "으면"], "잘하다 → 잘하려면."), F("환전하___ 어디로 가야 해요? (if I want to)", "려면", ["으려면", "으면"], "환전하다 → 환전하려면."),
           F("서울에서 살___ 집을 구해야 해요. (if you intend to live)", "려면", ["으려면", "을려면"], "ㄹ stems take 려면: 살려면."), F("선글라스를 찾___ 센터에 전화하세요. (if you want to find)", "으려면", ["려면", "으면"], "찾다 → 찾으려면."),
           M("What is the difference between -(으)면 and -(으)려면?", "-(으)려면 adds an intention or a wish", ["-(으)려면 is the past tense", "-(으)려면 is a question", "There is no difference"], "-(으)려면 = if one intends to."), M("Which word does -(으)려면 attach to?", "An action verb stem", ["A noun", "A time word", "A particle"], "action verb stem + (으)려면."),
           M("Which sentence means “If you intend to take a limousine bus, go to the first floor”?", "리무진 버스를 타려면 일 층으로 가세요.", ["리무진 버스를 타면 일 층으로 가세요.", "리무진 버스를 타러 일 층으로 가세요.", "리무진 버스를 탔으면 일 층으로 가세요."], "타려면 = if you intend to take."),
           M("What is -(으)려면 short for?", "-(으)려고 하면", ["-(으)러 하면", "-(으)려고 해서", "-(으)면 하려고"], "타려고 하면 → 타려면."),
           read_q("타려면"), read_q("살려면"), read_q("찾으려면"), read_q("먹으려면"), read_q("환전하려면 어디로 가야 해요")]
    ),
)

# ================================================================== Activities C
_QA_META = [("작성자", "홍정균", "작성일", f"{year_ko(2022)} {month_ko(10)} {day_ko(10)}", "조회수", "이백사십 회"),
            ("작성자", "관리자", "작성일", f"{year_ko(2022)} {month_ko(10)} {day_ko(11)}", "조회수", "이백구십삼 회")]
_QA1 = [
    ("제목: 짐을 잃어 버렸어요.", "Title: I lost my baggage."),
    ("안녕하세요.", "Hello."),
    (f"저는 {month_ko(10)} {day_ko(9)}에 샌프란시스코에서 아시아나항공 공일오편으로 입국했습니다.", "I entered the country from San Francisco on October 9 on Asiana Airlines flight 015."),
    ("그런데 제 짐 하나가 나오지 않았어요.", "But one of my pieces of baggage did not come out."),
    ("큰 주황색 여행가방은 나왔는데, 작은 녹색 배낭은 나오지 않았어요.", "The big orange suitcase came out, but the small green backpack did not."),
    ("제 짐을 찾으려면 어떻게 해야 합니까?", "What should I do to find my baggage?"),
    ("짐을 못 찾아서 아주 불편합니다.", "I can’t find my baggage, so it is very inconvenient."),
]
_QA2 = [
    ("제목: 저희 센터에 가방이 있습니다.", "Title: We have bags at our center."),
    ("안녕하십니까?", "Hello. (formal)"),
    ("저희 서비스센터에 배낭이 몇 개 있습니다.", "We have several backpacks at our service center."),
    ("먼저, 저희 센터로 전화를 주세요.", "First, please call our center."),
    ("저희 센터는 인천국제공항 지하 일 층 환전소 옆에 있습니다.", "Our center is on the first basement floor of Incheon International Airport, next to the currency exchange office."),
]
_QA_W = [("작성자", "the writer (mine)"), ("작성일", "the date written (mine)"), ("조회수", "the number of views (mine)"), ("제목", "a title; a subject line (mine)"), ("관리자", "an administrator; a manager (mine)"), ("여행가방", "a suitcase; a travel bag (mine)"),
         ("불편하다", "to be inconvenient; to be uncomfortable (mine)"), ("저희", "we; our (humble) (mine)"), ("먼저", "first; before (mine)"), ("옆", "beside; next to (mine)")]
_JR = [
    (f"{month_ko(12)} {day_ko(20)}", "December 20"),
    ("어제 저녁에 아시아나항공편으로 인천공항에 도착했습니다.", "Yesterday evening I arrived at Incheon airport on an Asiana Airlines flight."),
    ("짐을 찾으려고 짐 찾는 곳에서 기다렸습니다.", "I waited at the baggage claim to pick up my baggage."),
    ("그런데 제 가방이 안 나왔습니다.", "But my bag did not come out."),
    ("그래서 공항서비스센터에 가서 잃어버린 가방을 찾았습니다.", "So I went to the Airport Service Center and found the bag I had lost."),
    ("그 다음에 지하 일 층 환전소에 가서 오백 달러를 한국 돈으로 바꿨습니다.", "After that I went to the currency exchange office on the first basement floor and changed 500 dollars into Korean money."),
    ("직원이 육십만 원으로 환전해 주었습니다.", "The employee exchanged it for 600,000 won."),
    ("또 이 층에 가서 핸드폰도 하나 빌렸습니다.", "Also I went to the second floor and rented a cell phone too."),
    ("저녁 아홉 시쯤에 택시를 타고 용산호텔에 왔습니다.", "Around nine in the evening I took a taxi and came to the Yongsan Hotel."),
]
_JR_ORDER = [("arrived at Incheon International airport", 1), ("waited for his baggage at the baggage claim", 2), ("found his baggage at the airport service center", 3), ("exchanged money", 4), ("leased a cellular phone", 5), ("arrived at the hotel by taxi", 6)]
L10 = lesson(
    "Ch 13 · Activities C: a lost-and-found Q&A and PFC Hickman’s journal",
    "짐을 잃어 버렸어요 · 저희 센터에 가방이 있습니다 · 오백 달러를 바꿨습니다 · 택시를 타고 호텔에 왔습니다",
    requires=[],
    cards=[
        card("Activity 3 (Reading): the Airport Service Center Q&A",
             "The text is from the Q&A section of the Lost & Found department of the Airport Service Center website. The book asks you to fill in a table in English (the writer’s concern, the actions requested, the items mentioned by the center, the location and the number of the center). The text is the book’s; the English and the answers are mine. The writers’ e-mail addresses and the center’s telephone number are left out, and the dates and view counts are spelled out in Hangul.",
             tables=[table(["Field", "Value"], [[a, b], [c, d], [e, f]], say=[0, 1]) for a, b, c, d, e, f in _QA_META[:1]], examples=passage(_QA1)),
        card("The center’s answer",
             "The second post is the administrator’s answer, written the next day.",
             tables=[table(["Field", "Value"], [[a, b], [c, d], [e, f]], say=[0, 1]) for a, b, c, d, e, f in _QA_META[1:]], examples=passage(_QA2)),
        card("The table filled in (mine)",
             "Writer’s concern: one piece of baggage, a small green backpack, did not come out (the big orange suitcase did); it is inconvenient. Action requested: how to find the baggage. Items mentioned by the center: several backpacks. Location and contact: the center is on the first basement floor of Incheon International Airport next to the currency exchange office, and the writer should call first (the number is left out here).",
             tables=[ktable(_QA_W)]),
        card("Follow-up 2 (Reading): PFC Hickman’s journal entry",
             "The journal entry about his first day in Korea is handwritten in the book (a picture), so the text below is read from it; the numbers are respelled in Hangul (500달러 → 오백 달러, 60만 원 → 육십만 원, 9시 → 아홉 시). The English is mine. The book asks you to underline each phrase and number it in the order of the actions; the first (arrived at Incheon airport, 1) and the last (arrived at the hotel by taxi, 6) are done for you.",
             examples=passage(_JR)),
        card("The order of the actions",
             "The numbers 2 to 5 are my answers from the journal.",
             tables=[table(["Number", "Phrase"], [[str(n), p] for p, n in _JR_ORDER])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), Activity 2 (listening to conversations between an employee and a customer at the airport and ticking the available services), Activity 4 (the information-desk role-play with situation cards) and the Useful Links (cell phone rental and roaming, the airport limousine bus, currency exchange offices) are audio, partner or website activities."),
    ],
    exercises=uniq(
        _tr(_QA1[1:] + _QA2[1:])
        + _tr(_JR[1:])
        + _tr(_QA_W)
        + [M("What did Mr. Hong lose?", "A small green backpack", ["A big orange suitcase", "A purple bag", "His passport"], "작은 녹색 배낭은 나오지 않았어요."), M("What came out at the baggage claim?", "A big orange suitcase", ["A small green backpack", "Nothing", "A purple bag"], "큰 주황색 여행가방은 나왔는데."),
           M("What did Mr. Hong ask in his post?", "What he should do to find his baggage", ["Where the hotel is", "How to exchange money", "When the flight leaves"], "제 짐을 찾으려면 어떻게 해야 합니까?"), M("When did Mr. Hong enter the country?", "October 9", ["October 10", "October 11", "December 20"], f"{month_ko(10)} {day_ko(9)}에 … 입국했습니다."),
           M("Which flight did Mr. Hong arrive on?", "Asiana Airlines flight 015", ["Korean Air flight 015", "Asiana Airlines flight 024", "Korean Air flight 024"], "아시아나항공 공일오편."), M("Who answered Mr. Hong?", "The administrator", ["A flight attendant", "An immigration officer", "Another passenger"], "작성자: 관리자."),
           M("What does the center say first?", "It has several backpacks", ["It has no backpacks", "It lost the bag", "It is closed"], "저희 서비스센터에 배낭이 몇 개 있습니다."), M("What does the center ask Mr. Hong to do first?", "Call the center", ["Visit the website", "Wait a week", "Write another post"], "먼저, 저희 센터로 전화를 주세요."),
           M("Where is the Airport Service Center?", "On the first basement floor, next to the currency exchange office", ["On the second floor", "Next to the gate", "In the duty-free shop"], "지하 일 층 환전소 옆에 있습니다."),
           M("What did PFC Hickman do while waiting at the baggage claim?", "He waited for his baggage", ["He exchanged money", "He rented a phone", "He took a taxi"], "짐 찾는 곳에서 기다렸습니다."), M("Where did PFC Hickman find his lost bag?", "At the Airport Service Center", ["At the hotel", "At the baggage claim", "On the plane"], "공항서비스센터에 가서 잃어버린 가방을 찾았습니다."),
           M("How much money did PFC Hickman exchange?", "500 dollars", ["600 dollars", "50 dollars", "60,000 won"], "오백 달러를 한국 돈으로 바꿨습니다."), M("How many won did he receive?", "600,000 won", ["60,000 won", "500,000 won", "6,000,000 won"], "육십만 원 = 600,000 won."),
           M("Where did he rent a cell phone?", "On the second floor", ["On the first basement floor", "At the hotel", "At the gate"], "이 층에 가서 핸드폰도 하나 빌렸습니다."), M("How did he get to the hotel?", "By taxi", ["By limousine bus", "By subway", "On foot"], "택시를 타고 용산호텔에 왔습니다."),
           M("About what time did he arrive at the hotel?", "About nine in the evening", ["About nine in the morning", "About six in the evening", "About midnight"], "저녁 아홉 시쯤."), M("Which action came first in the journal?", "He arrived at Incheon airport", ["He rented a phone", "He exchanged money", "He took a taxi"], "도착했습니다 is the first action."),
           M("Which action came right before exchanging money?", "Finding his bag at the service center", ["Renting a phone", "Taking a taxi", "Waiting at the baggage claim"], "그 다음에 지하 일 층 환전소에 가서 …"), M("Which action came right after exchanging money?", "Renting a cell phone", ["Taking a taxi", "Finding his bag", "Arriving at the airport"], "또 이 층에 가서 핸드폰도 하나 빌렸습니다."),
           F("제 짐을 찾___ 어떻게 해야 합니까? (if I intend to)", "으려면", ["려면", "으면"], "찾다 → 찾으려면."), F("짐을 못 찾아서 아주 ___. (inconvenient)", "불편합니다", ["편합니다", "좋습니다"], "불편하다 = to be inconvenient."), F("저희 센터는 환전소 ___에 있습니다. (next to)", "옆", ["앞", "위"], "옆 = beside."),
           F("저는 시월 구일에 ___했습니다. (entered the country)", "입국", ["출국", "통과"], "입국하다 = to enter a country."), F("오백 달러를 한국 돈으로 ___습니다. (exchanged)", "바꿨", ["빌렸", "찾았"], "바꾸다 → 바꿨습니다."), F("핸드폰도 하나 ___습니다. (rented)", "빌렸", ["바꿨", "찾았"], "빌리다 → 빌렸습니다."),
           read_q("공항서비스센터"), read_q("조회수"), read_q("여행가방"), read_q("용산호텔"), read_q("육십만 원")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_SECS = [("At an airport", _CV_AIR), ("On the plane", _CV_PLANE), ("Customs formalities", _CV_CUST), ("At a baggage claim area", _CV_BAG), ("Colors and shapes", _CV_SHAPE), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_ALL = [r for _, rows in _CV_SECS[:-1] for r in rows]
L11 = lesson(
    "Ch 13 · Core vocabulary and self-evaluation",
    "주요 단어 · 공항에서 · 비행기에서 · 세관 · 짐 · 색과 모양 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. In the book the optional parts, such as (~하다/되다) or (선), are written in parentheses; they are kept in the meaning cells here.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (OZ045편 → 오지공사오편, KE024편 → 케이이공이사편, 8번 → 팔 번, 1층 → 일 층); the book’s English glosses inside a few examples, such as 외국(foreign country), are left out. The book spells “iPad” 아이파드; that spelling is kept. The book’s Additional Vocabulary table is empty: it is for your own words."),
    ] + [card(name, "Italicized English words in the book are grammatical terms, not the meaning of a Korean word." if name == "Other words" else "", tables=[vt(rows)]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about flight information including date, time, and flight number; comprehend and respond to flight announcements; understand the boarding procedures at an international airport; answer questions at the customs and immigration office; request in-flight services; request information about airport facilities and services; describe the size, color, and shape of objects.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the noun connector ~(이)나 (or); expressing total negation with 아무 ~도; the conjunctive ending -(으)려고 (in order to; so as to); the conjunctive ending -(으)려면 (if one intends to, if one plans to); the Sino-Korean syllables 권 (券), 승 (乘), 착 (着), and 면 (免)."),
    ],
    exercises=uniq(
        vocab_exercises([(r[0], _en(r[0])) for r in _CV_ALL if not r[0].startswith(("~", "-(")) and r[0] not in ("물어보다/묻다", "두고 내리다")])
        + [M("What does the Sino-Korean syllable 승 (乘) mean?", "to ride on", ["a document; a ticket; a bill", "arrival", "to exempt; to avoid"], "탑승, 탑승구, 승차."), M("What does the Sino-Korean syllable 권 (券) mean?", "a document; a ticket; a bill", ["to ride on", "arrival", "to exempt; to avoid"], "탑승권, 입장권, 상품권."),
           M("What does the Sino-Korean syllable 착 (着) mean?", "arrival", ["to ride on", "a document; a ticket; a bill", "to exempt; to avoid"], "착용, 착륙, 연착."), M("What does the Sino-Korean syllable 면 (免) mean?", "to exempt; to avoid", ["to ride on", "arrival", "a document; a ticket; a bill"], "면세, 면제, 면역."),
           M("What does ~(이)나 mean?", "or (as a noun connector)", ["and; with", "only", "also"], "버스나 기차로 = by bus or by train."), M("What does -(으)려고 mean?", "(in order) to", ["if you intend to", "because", "although"], "운동하려고 = in order to exercise."),
           M("What does -(으)려면 mean?", "if [you] intend to", ["(in order) to", "because", "although"], "환전하려면 = if you intend to exchange money."), M("What does ~에 대해서 mean?", "about", ["among", "any", "quickly"], "날씨에 대해서 = about the weather."),
           M("What does ~중(에/에서) mean?", "among; between", ["about", "any", "or"], "두 개 중에서 하나 = one of two."), M("What does 아무 mean?", "any", ["quickly", "about", "among"], "아무것도 = nothing."),
           M("What does ~편 count?", "a flight number", ["a seat", "a passport", "a gate"], "오지공사오편 = flight OZ045."), M("What does ~등 mean?", "and so forth; etc.", ["among", "about", "any"], "핸드백, 지갑 등 = handbags, wallets, etc.")]
        + [read_q("주요 단어"), read_q("탑승구"), read_q("환전소"), read_q("출입국"), read_q("동그랗다")]
    ),
)

UNIT = unit("Semester 1 · Unit 4 · Chapter 13: Welcome to Korea (한국에 오신 것을 환영합니다)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])
