"""Unit 52: KBC Semester 2, Unit 12, Chapter 45 - Economy (경제).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 12, Student's Edition (2022).
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 45 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("강세", "(强勢) strong trend (in stock, currency exchange rate, or price); “strong force”", "요즘 미국 달러가 강세를 보이고 있습니다."),
    ("공업", "(工業) the manufacturing industry", "공업 지역의 오염을 줄이기 위한 노력이 계속되고 있습니다."),
    ("구조", "(構造) structure", "그 집은 깨끗하고 가격도 적당한데 구조가 마음에 안 들어요."),
    ("국내총생산", "(國內總生産) Gross Domestic Product (GDP)", "국내총생산은 증가했으나 일인당 국민소득은 거의 오르지 않았습니다."),
    ("국민", "(國民) a people; citizens (of a nation); “nation people”", "연구 결과에 따르면 세계에서 가장 행복한 국민은 북유럽 사람들이다."),
    ("내다보다", "to foresee; “look out”", "전문가들은 지구온난화로 바닷가 도시들이 물에 잠길 것이라고 내다봤습니다."),
    ("~년대", "(年代) (decade of) the ~s, as in 구십 년대 (the ’90s); 년(도) the year ~, as in 구십 년도 (the year 1990)", "저는 칠십 년대와 팔십 년대의 음악을 좋아합니다."),
    ("농업", "(農業) agriculture", "선진국 국민들은 친환경 농업에 대한 관심이 높습니다."),
    ("로봇", "a robot", "병원에서 의사들이 로봇을 사용하여 수술하기도 합니다."),
    ("반도체", "(半導體) a semiconductor", "많은 전자제품에 반도체가 사용됩니다."),
    ("비중", "(比重) relative importance; “relative weight”", "많은 기업에서 여성 관리자의 비중이 점점 커지고 있습니다."),
    ("산업", "(産業) industry", "스위스나 프랑스는 관광 산업으로 많은 돈을 법니다."),
    ("서비스업", "a service industry", "고등학교 졸업자의 칠십 퍼센트가 서비스업에서 일을 한다는 조사 결과가 나왔습니다."),
    ("선진국", "(先進國) an advanced country; “front-moving country”", "한국은 아주 빠르게 인터넷 선진국이 되었습니다."),
    ("성장", "(成長) growth (to grow) (~하다)", "사람 몸의 성장은 보통 열여섯 살에서 열일곱 살에 끝납니다."),
    ("수준", "(水準) a level", "이 책은 우리 아이 수준에 맞지 않는 것 같아요. 좀 쉬운 것으로 주세요."),
    ("약세", "(弱勢) weak trend (in stock, currency exchange rate, or price); “weak force”", "경제가 나빠지면서 전 세계적으로 부동산 시장이 계속 약세입니다."),
    ("어업", "(漁業) fishery; fishing industry", "어업을 하는 사람들은 일기예보를 잘 들어야 합니다."),
    ("일인당", "(1人당) per person; per capita", "음식 값이 모두 오만 원 나왔습니다. 다섯 명이니까 일인당 만 원씩 냅시다."),
    ("전자", "(電子) electronic(s)", "제 오빠는 전자공학을 전공하고 지금은 엘지전자에서 일합니다."),
    ("정부", "(政府) a government", "오바마 정부가 새로운 건강보험 제도를 시작했습니다."),
    ("제조업", "(製造業) a manufacturing industry", "광주 지역의 경제가 대기업의 투자로 농업 중심에서 제조업 중심으로 바뀌고 있습니다."),
    ("조", "(兆) trillion", "정부는 앞으로 오 년간 스마트 모바일 사업에 일 조 오천억 원을 투자하겠다고 밝혔습니다."),
    ("조선", "(造船) shipbuilding", "요즘 중국이 조선업에 많은 투자를 하고 있습니다."),
    ("주요", "(主要) main; principal; major", "저는 신문에서 주요 기사만 읽습니다."),
    ("차지하다", "to take (up); to occupy; to account for", "제 생활비 지출에서 식비가 가장 많은 비중을 차지합니다."),
    ("첨단기술", "(尖端技術) cutting-edge technology; state-of-the-art technology", "전자제품 박람회에서는 첨단기술을 이용한 여러 제품들이 전시됩니다."),
    ("투자", "(投資) investment (to invest) (~하다)", "저는 부동산과 주식에 조금씩 투자하고 있습니다."),
]
_CV_B = [
    ("개척", "(開拓) pioneering; developing (to pioneer; to develop/to be pioneered; to be developed) (~하다/되다)", "수출을 늘리기 위해 우리나라의 기업들은 중동과 중남미에서 새로운 시장을 개척하고 있습니다."),
    ("급감", "(急減) rapid decrease (to decrease rapidly) (~하다)", "요즘 경제가 좋지 않아 백화점을 찾는 사람 수가 급감했다."),
    ("급증", "(急增) rapid increase (to increase rapidly) (~하다)", "요즘 어린이 비만에 걸리는 아이들이 급증하고 있습니다."),
    ("기계", "(機械) a machine", "저는 대학에서 기계공학을 전공하고 싶어요."),
    ("농산물", "(農産物) agricultural products", "한국이 외국에서 수입하는 농산물이 점점 늘고 있습니다."),
    ("무역수지", "(貿易收支) trade balance", "지난해 우리나라의 무역수지는 흑자를 기록했습니다."),
    ("~분기", "(分期) a quarter (of a year)", "올 이 분기 수출은 이억 달러를 기록했습니다."),
    ("불황", "(不況) economic recession; economic slump", "세계경제의 불황으로 한국경제도 영향을 받고 있습니다."),
    ("석유", "(石油) oil; petroleum; “stone oil”", "석유는 중동에서 많이 납니다."),
    ("섬유", "(纖維) fiber; textiles", "한국에서는 천구백칠십 년대에 섬유산업이 크게 성장했습니다."),
    ("수요", "(需要) demand", "신제품의 수요가 늘어나면서 값이 오르고 있습니다."),
    ("순위/~위", "(順位) ranking; ~th place", "우리나라의 수출품목 일 위는 반도체입니다."),
    ("원유", "(原油) crude oil; “raw oil”", "최근 경제가 나빠지면서 원유가격이 크게 하락했습니다."),
    ("원자재", "(原資材) raw materials", "한국이 주로 수입하는 원자재는 원유입니다."),
    ("적자", "(赤字) a deficit; a loss; “red letter”", "정부는 무역적자를 줄이기 위해 노력하고 있습니다."),
    ("전반적", "(全般的) overall; general", "그 영화는 분위기가 전반적으로 우울합니다."),
    ("통계", "(統計) statistics", "최근 통계에 따르면, 여성 취업률이 올라가고 있다고 합니다."),
    ("평균", "(平均) average; mean", "한국인의 평균 결혼 나이는 남자가 서른한 살, 여자가 스물여덟 살인 것으로 나타났습니다."),
    ("품목", "(品目) an item", "핸드폰은 한국의 주요 수출품목입니다."),
    ("하락", "(下落) drop; fall; decrease (to fall) (~하다)", "최근 집값이 계속 하락하고 있습니다."),
    ("호황", "(好況) an economic boom", "천구백팔십 년대의 경제호황으로 한국경제가 급성장했습니다."),
    ("흑자", "(黑字) a surplus; “black letter”", "수출이 꾸준히 늘고 있어 흑자를 기록했습니다."),
]
_CV_C = [
    ("거래", "(去來) a business transaction; a trade; a deal (to do business with; to transact/to be traded) (~하다/되다)", "우리 회사는 외국은행과 거래합니다."),
    ("계좌", "(計座) an account (i.e. with a bank or other financial institution)", "온라인 뱅킹을 하면 한 은행 계좌에서 다른 은행 계좌로 돈을 쉽게 보낼 수 있습니다."),
    ("금액", "(金額) an amount (of money)", "은행에 큰 금액을 저축했습니다."),
    ("금융기관", "(金融機關) a financial institution", "졸업을 한 후에 금융기관에 취직할 생각입니다."),
    ("단기(적)", "(短期(的)) short-term", "단기적으로 저축하면 이자가 작습니다."),
    ("땅", "land; ground", "이 지역의 땅은 가격이 비쌉니다."),
    ("만기", "(滿期) expiration; maturity; “full period”", "적금이 만기되면 그 돈으로 차를 사고 싶어요."),
    ("보통예금", "(普通預金) a regular savings account", "돈을 자주 찾으려면 보통예금이 편합니다."),
    ("손해", "(損害) a loss; damage; harm (i.e. financial)", "주식가격이 내려서 손해를 봤습니다."),
    ("수수료", "(手數料) a commission; a fee; a charge", "신용카드를 쓸 때는 수수료를 내야 합니다."),
    ("수익(성)", "(收益(性)) a profit (profitability)", "수익성이 낮은 제품은 팔지 않습니다."),
    ("예금", "(預金) savings; deposit (to save money in the bank) (~하다)", "오늘 오후에 은행에 가서 예금했어요."),
    ("이(자)율", "(利(子)率) an interest rate", "이 은행의 적금은 이율이 너무 낮아요."),
    ("일정하다", "(一定) to be fixed; to be regular", "저는 매달 일정한 돈을 부모님께 드립니다."),
    ("입금", "(入金) deposit (to deposit/to be deposited) (~하다/되다)", "오후 네 시까지 돈을 입금해야 합니다."),
    ("장기(적)", "(長期(的)) long-term", "부동산 투자는 장기적인 투자입니다."),
    ("적금(에/을 들다)", "(積金) installment savings (to save money in an installment savings account) (~에/을 들다)", "매달 월급에서 십만 원씩 적금에 들어갑니다."),
    ("적합하다", "(適合) to be suitable", "이 음악은 결혼식에 적합하지 않습니다."),
    ("정기예금", "(定期預金) a certificate of deposit", "이 년 후에 유럽 여행을 가려고 이백만 원을 정기 예금했어요."),
    ("주식/증권", "(株式/證券) stock", "제 친구는 주식증권에 투자해서 큰돈을 벌었습니다."),
    ("지급", "(支給) payment (to pay/to be paid) (~하다/되다)", "회사에서는 직원들에게 보너스로 삼십만 원씩 지급했습니다."),
    ("추세", "(趨勢) a trend; a tendency", "요즘은 부동산에 투자하는 추세입니다."),
    ("통장", "(通帳) a bankbook", "우체국 통장을 만들어 두면 편리할 때가 많습니다."),
    ("펀드", "a fund", "펀드에 퇴직금을 투자했습니다."),
]
_CV_GR = [
    ("~에도/–(으)ㄴ/는데도 (불구하고)", "in spite of; despite", "공부를 열심히 했는데도 불구하고 성적이 좋지 않아요."),
    ("–(으)려던 참이다", "I was just about to do …", "방금 숙제를 하려던 참이었어요."),
]
_CV_SINO = [("조선업", "(造船業) shipbuilding industry", "위조, 모조품, 조화, 어선, 유조선, 선원, 개업, 수산업, 업소"), ("약세", "(弱勢) weak trend; weak force", "강약, 약점, 노약자, 강세, 우세, 세력"), ("하락", "(下落) drop; decrease", "지하, 영하, 하반기, 추락, 폭락, 낙하산"), ("급감", "(急減) rapid decrease", "급증, 급락, 급성장, 감소, 감원, 가감"), ("장단점", "(長短點) strength and weakness", "연장, 단축, 시점, 교장, 단시간, 점수, 장남, 단문, 문제점")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"단기": "short-term", "장기": "long-term", "수익": "profit", "이율": "interest rate", "적금": "installment savings", "순위": "ranking", "주식": "stock", "증권": "securities; stock certificate", "성장": "growth", "하락": "drop; fall", "입금": "deposit", "출금": "withdrawal", "예금": "savings; deposit", "투자": "investment", "금융": "finance", "관세": "customs duty; tariff", "수출": "exports", "수입": "imports", "환율": "exchange rate", "신발": "shoes", "관광업": "tourism industry", "호텔업": "hotel business", "금융업": "financial industry", "공업": "the manufacturing industry"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/") and " " not in w]
_HG = lambda s: "가" <= s[0] <= "힣"


def _words(keys):
    pl = _PLAIN(keys)
    out = [ktable(_rows(pl))]
    rest = [k for k in keys if k not in pl]
    if rest:
        out.append(table(["Word", "Meaning"], [[k, _en(k)] for k in rest]))
    return out


# ---- Sino-Korean notes
_S1G = [("조어", "a coined word; “made word”"), ("선장", "skipper; captain; “boat chief”"), ("선원", "a ship crew member"), ("어업", "fishery; “fishing business”"), ("광업", "mining; “mine industry”")]
_S1 = [("위조", "counterfeiting; forgery"), ("모조품", "an imitation; a fake"), ("조화", "an artificial flower"), ("어선", "a fishing boat"), ("유조선", "an oil tanker"), ("개업", "opening a business"), ("수산업", "the marine products industry; fisheries"), ("업소", "a place of business; an establishment")]
_S2G = [("약자", "a weak person; the weak"), ("강약", "loud and soft (in music); dynamics; “strong and weak”"), ("추세", "tendency; trend; “running force”")]
_S2 = [("약화", "weakening"), ("강세", "a strong trend"), ("약점", "a weak point; a weakness"), ("우세", "superiority; the upper hand"), ("노약자", "the old and the weak"), ("세력", "power; influence; force")]
_S3G = [("지하철", "subway; “underground railroad”"), ("하녀", "a female servant; “low woman”"), ("낙엽", "fallen leaves"), ("낙마", "falling from a horse")]
_S3 = [("하수도", "a sewer; a drain"), ("영하", "below zero"), ("하반기", "the second half of the year"), ("추락", "a fall; a crash"), ("낙선", "losing an election"), ("낙하산", "a parachute")]
_S4G = [("급류", "a rapid; a torrent; “rapid flow”"), ("급사", "a sudden death; an untimely death"), ("감하다", "to reduce; to subtract"), ("감세", "reduction of taxes")]
_S4 = [("급증", "a sudden increase"), ("급락", "a sharp fall; a plunge"), ("급성장", "rapid growth"), ("감소", "a decrease"), ("감원", "staff reduction; downsizing"), ("가감", "addition and subtraction; adjustment")]
_S5G = [("장거리", "long distance"), ("장남", "the eldest son; “big man”"), ("병장", "a sergeant; “head of soldiers”"), ("사장", "a company president; “company chief”"), ("단거리", "short distance"), ("단문", "a short sentence; a short composition; “short letter”"), ("점수", "score; a mark; a grade; “number of points”"), ("종점", "the last stop; the terminal; “ending point”")]
_S5 = [("장문", "a long sentence; a long text"), ("출발점", "a starting point"), ("문제점", "a problem; a point at issue"), ("단음", "a short sound"), ("장음", "a long sound")]

L1 = lesson(
    "Ch 45 · What the chapter teaches, 조선업 · 약세 · 하락 · 급감 · 장단점",
    "경제 · 조선업 · 약세 · 하락 · 급감 · 장단점 · 造船業 · 弱勢 · 下落 · 急減 · 長短點",
    requires=[],
    cards=[
        card("What Chapter 45 teaches (경제)",
             "Chapter 45, “Economy”, has a vocabulary builder, three topic presentations (the structure of the Korean economy, Korean trade, investment) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss sectors of the Korean economy including the gross domestic product (GDP), economic growth rate, trade volume, trading partners, etc.; identify and discuss major types of financial investments and their characteristics; and read and say large numbers in Korean.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; ~에도 (불구하고) or –(으)ㄴ/는데도 (불구하고) (in spite of; despite); –(으)려던 참이다 (I was about to do something); and the Sino-Korean syllables within 조선업 (造船業), 약세 (弱勢), 하락 (下落), 급감 (急減), and 장단점 (長短點)."),
        card("Sino-Korean in use: 조선업 (造船業)",
             "This Sino-Korean word means shipbuilding business or shipbuilding industry. The first syllable 조 (造) means make or build, as in 조어 (coined word; “made word”). The second syllable 선 (船) means a ship or a boat, as in 선장 (skipper; captain; “boat chief”) and 선원 (ship crew member). The last syllable 업 (業) means business, work, or occupation, as in 어업 (fishery; “fishing business”) and 광업 (mining; “mine industry”). The book asks you to guess the meaning of 위조, 모조품, 조화, 어선, 유조선, 선원, 개업, 수산업 and 업소 (the book glosses 모 [模]: imitate, model; 화 [花]: a flower; my answers):",
             tables=[ktable(_S1G), ktable(_S1)]),
        card("Sino-Korean in use: 약세 (弱勢)",
             "The first syllable 약 (弱) means weak(ness) or feeble(ness), as in 약자 (a weak person; the weak) and 강약 (loud and soft [in music]; dynamics; “strong and weak”). The second syllable 세 (勢) means power, influence, or force, as in 추세 (tendency; trend; “running force”). Thus, the literal meaning of the word 약세 is “weak force” or “weak influence,” and the word means bearish (falling) trend or weak tendency (in stock, currency exchange rate, price). The book asks you to guess 약화, 강세, 약점, 우세, 노약자 and 세력 (the book glosses 우 [優]: tender, outstanding, sufficient; my answers):",
             tables=[ktable(_S2G), ktable(_S2)]),
        card("Sino-Korean in use: 하락 (下落)",
             "The syllable 하 (下) means under, below, low, or bottom, as in 지하철 (subway; “underground railroad”) and 하녀 (a female servant; “low woman”). 락/낙 (落) means drop or fall, as in 낙엽 (fallen leaves) or 낙마 (falling from a horse). Keep in mind that 락 changes to 낙 at the beginning of a word. Thus, the literal meaning of the word 하락 is “falling below,” and it means drop or decrease (in number or amount). The book asks you to guess 하수도, 영하, 하반기, 추락, 낙선 and 낙하산 (the book glosses 산 [傘]: umbrella; 선 [選]: election; my answers):",
             tables=[ktable(_S3G), ktable(_S3)]),
        card("Sino-Korean in use: 급감 (急減)",
             "The first syllable 급 (急) means urgent, sudden, or rapid, as in 급류 (a rapid; a torrent; “rapid flow”) and 급사 (a sudden death; an untimely death). The second syllable 감 (減) means decrease, reduction, or subtraction, as in 감하다 (to reduce; to subtract) and 감세 (reduction of taxes). Thus, the literal meaning of 급감 is “sudden decrease” or “rapid reduction,” and it means sudden decrease or sharp decrease (in number or amount). The book asks you to guess 급증, 급락, 급성장, 감소, 감원 and 가감 (the book glosses 원 [員]: personnel; 가 [加]: adding; my answers):",
             tables=[ktable(_S4G), ktable(_S4)]),
        card("Sino-Korean in use: 장단점 (長短點)",
             "This Sino-Korean word means strengths and weaknesses, strong and weak points, pros and cons, merits and demerits, or advantages and disadvantages. The first syllable 장 (長), which was discussed in Chapter 25, means long, big, or chief/head, as in 장거리 (long distance), 장남 (the eldest son; “big man”), 병장 (a sergeant; “head of soldiers”), and 사장 (a company president; “company chief”). The second syllable 단 (短) means short, as in 단거리 (short distance) or 단문 (a short sentence; a short composition; “short letter”). The last syllable 점 (點), discussed in Chapter 33, means point or score, as in 점수 (score; a mark; a grade; “number of points”) and 종점 (the last stop; the end of the route; the terminal; “ending point”). Thus the literal meaning of the word is “long and short point.” The book asks you to guess 장문, 출발점, 문제점, 단음 and 장음 (my answers):",
             tables=[ktable(_S5G), ktable(_S5)]),
    ],
    exercises=uniq(
        _tr(_S1G + _S1 + _S2G + _S2 + _S3G + _S3 + _S4G + _S4 + _S5G + _S5, k=3)
        + [M("What does 조 (造) mean?", "make; build", ["boat", "business", "weak"], "조선."), M("What does 선 (船) mean?", "a ship; a boat", ["make", "business", "power"], "선원."), M("What does 업 (業) mean?", "business; work; occupation", ["ship", "weak", "fall"], "어업."), M("What does 약 (弱) mean?", "weak; feeble", ["strong", "sudden", "short"], "약자."), M("What does 세 (勢) mean?", "power; influence; force", ["weak", "drop", "point"], "추세."), M("What does 하 (下) mean?", "under; below; low", ["up", "sudden", "long"], "지하철."), M("What does 락/낙 (落) mean?", "drop; fall", ["rise", "make", "point"], "낙엽."), M("What does 급 (急) mean?", "urgent; sudden; rapid", ["slow", "weak", "short"], "급류."), M("What does 감 (減) mean?", "decrease; reduction", ["increase", "ship", "business"], "감세."), M("What does 장 (長) mean?", "long; big; chief", ["short", "weak", "sudden"], "장거리."), M("What does 단 (短) mean?", "short", ["long", "chief", "fall"], "단문."), M("What does 점 (點) mean?", "point; score", ["ship", "line", "business"], "점수."), M("What is the literal meaning of 약세?", "“weak force” or “weak influence”", ["“strong force”", "“sudden decrease”", "“falling below”"], "약 + 세."), M("What is the literal meaning of 급감?", "“sudden decrease” or “rapid reduction”", ["“weak force”", "“falling below”", "“ship business”"], "급 + 감."), M("What is the literal meaning of 하락?", "“falling below”", ["“sudden decrease”", "“weak force”", "“long and short point”"], "하 + 락."), M("What is the literal meaning of 장단점?", "“long and short point”", ["“big and small”", "“strong and weak force”", "“falling below”"], "장 + 단 + 점."), M("Which becomes 낙 at the beginning of a word?", "락", ["락 never changes", "업", "급"], "The book’s note."),
           F("조___업은 배를 만드는 산업입니다. (ship)", "선", ["어", "약"], "조선업."), F("생선을 잡는 산업은 ___업입니다. (fishing)", "어", ["농", "광"], "어업."), F("경제가 나빠지면서 부동산 시장이 ___세입니다. (weak)", "약", ["강", "우"], "약세."), F("집값이 계속 ___락하고 있습니다. (fall)", "하", ["상", "급"], "하락."), F("백화점을 찾는 사람 수가 ___감했습니다. (rapidly)", "급", ["약", "하"], "급감."),
           read_q("조선업"), read_q("약세"), read_q("하락"), read_q("급감"), read_q("장단점")]
    ),
)

# ================================================================== L2 Vocabulary builder
_IND = [("공업", "manufacturing industry"), ("농업", "agriculture industry"), ("어업", "fishing industry"), ("조선업", "shipbuilding industry"), ("섬유업", "textile industry"), ("전자업", "electronics industry"), ("석유화학 공업", "petrochemical industry"), ("금융업", "financial industry")]
_ODD = [("제조업", "섬유, 반도체, 펀드, 신발", "펀드", "섬유, 반도체 and 신발 are manufacturing; 펀드 is finance"), ("서비스업", "금융업, 관광업, 호텔업, 농업", "농업", "금융업, 관광업 and 호텔업 are service industries; 농업 is agriculture"), ("무역", "수출, 관세, 적금, 환율", "적금", "수출, 관세 and 환율 are trade; 적금 is a savings account"), ("펀드", "수준, 수익, 주식, 투자", "수준", "수익, 주식 and 투자 relate to funds; 수준 is a level"), ("금융", "예금, 석유, 적금, 은행", "석유", "예금, 적금 and 은행 are finance; 석유 is oil")]
L2 = lesson(
    "Ch 45 · Vocabulary Builder: industries and money",
    "공업 · 농업 · 어업 · 조선업 · 섬유업 · 전자업 · 석유화학 공업 · 금융업 · 제조업 · 서비스업 · 무역 · 펀드 · 금융",
    requires=[],
    cards=[
        card("새 단어 a: names of industries",
             "Review the names of industries in Column A and match each with its English meaning in Column B (the book’s eight pairs; the matches are the book’s own list, mine to confirm):",
             tables=[ktable(_IND)]),
        card("새 단어 b: which word does not belong?",
             "Skim each row of the numbered words and circle the one that does NOT correspond with the category (the book’s rows; the odd ones out are my answers):",
             tables=[table(["Category", "Words", "Odd one out (mine)", "Why (mine)"], [[a, b, c, d] for a, b, c, d in _ODD])]),
        card("Activities left out", "Activities 1, 2 and 3 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 4 (“Grab the Word”: words are taped on the back wall of the classroom; two teams each send a member to grab the word that matches a description read aloud on the SMART Board within ten seconds) are computer and game activities."),
    ],
    exercises=uniq(
        _tr(_IND, k=3)
        + [M("What does 어업 mean?", "fishing industry", ["agriculture", "shipbuilding", "textiles"], "어업."), M("What does 금융업 mean?", "the financial industry", ["the textile industry", "tourism", "mining"], "금융업."), M("Which does NOT belong to 제조업?", "펀드", ["섬유", "반도체", "신발"], "My answer."), M("Which does NOT belong to 서비스업?", "농업", ["금융업", "관광업", "호텔업"], "My answer."), M("Which does NOT belong to 무역?", "적금", ["수출", "관세", "환율"], "My answer."), M("Which does NOT belong to 펀드?", "수준", ["수익", "주식", "투자"], "My answer."), M("Which does NOT belong to 금융?", "석유", ["예금", "적금", "은행"], "My answer."),
           F("쌀과 채소를 기르는 산업은 ___입니다. (agriculture)", "농업", ["어업", "공업"], "농업."), F("배를 만드는 산업은 ___입니다. (shipbuilding)", "조선업", ["섬유업", "전자업"], "조선업."), F("옷감을 만드는 산업은 ___입니다. (textile)", "섬유업", ["조선업", "금융업"], "섬유업."), F("은행과 증권사가 하는 산업은 ___입니다. (financial)", "금융업", ["공업", "어업"], "금융업."), F("반도체와 휴대폰을 만드는 산업은 ___입니다. (electronics)", "전자업", ["농업", "어업"], "전자업."),
           read_q("공업"), read_q("농업"), read_q("어업"), read_q("조선업"), read_q("금융업")]
    ),
)

# ================================================================== L3 Topic A
_A_TXT = [
    ("한국의 경제 구조", "The structure of Korea’s economy"),
    ("천구백육십 년대 초까지 한국은 농업 중심의 국가였다.", "Until the early 1960s, Korea was a country centered on agriculture."),
    ("천구백육십이 년에 시작된 경제개발 오 개년 계획은 한국의 경제구조를 공업 중심으로 바꾸었다.", "The five-year economic development plan that began in 1962 changed Korea’s economic structure to be centered on industry."),
    ("구십 년대까지 계속된 경제개발계획을 통해 한국의 경제는 선진국 수준에 가깝게 급성장했다.", "Through the economic development plans that continued until the 1990s, Korea’s economy grew rapidly to near the level of advanced countries."),
    ("올해 한국의 국내총생산 지디피는 일 조 육천억 달러이며, 오이씨디 국가 중 십삼 위이다.", "This year Korea’s gross domestic product (GDP) is 1.6 trillion dollars, and it is 13th among OECD countries."),
    ("또, 일인당 국민소득은 약 삼만 이천 불이다.", "Also, the per capita national income is about 32,000 dollars."),
    ("세계은행은 내년 한국의 경제성장률이 일 점 오 퍼센트가 될 것으로 내다보고 있다.", "The World Bank foresees Korea’s economic growth rate next year to be 1.5 percent."),
    ("한국의 주요 산업은 자동차, 조선, 전자 등의 제조업과 반도체 등의 첨단기술 산업이다.", "Korea’s main industries are manufacturing such as automobiles, shipbuilding and electronics, and cutting-edge technology industries such as semiconductors."),
    ("최근에는 로봇, 친환경 에너지 등의 미래형 산업에 대한 투자와 지원이 늘고 있다.", "Recently, investment in and support for futuristic industries such as robots and eco-friendly energy are increasing."),
    ("한편, 경제 발전에 비해 서비스업이 국가 경제에서 차지하는 비중은 낮은 편이다.", "Meanwhile, compared with economic development, the share that service industries account for in the national economy is on the low side."),
    ("따라서 한국 정부는 경제를 서비스업이 강세인 선진국형으로 발전시키기 위해 노력하고 있다.", "Therefore, the Korean government is making efforts to develop the economy into the advanced-country type in which service industries are strong."),
]
_A_WORDS = ["강세", "공업", "구조", "국내총생산", "국민", "내다보다", "~년대", "농업", "로봇", "반도체", "비중", "산업", "서비스업", "선진국", "성장", "수준", "약세", "어업", "일인당", "전자", "정부", "제조업", "조", "조선", "주요", "차지하다", "첨단기술", "투자"]
L3 = lesson(
    "Ch 45 · Topic A: The structure of the Korean economy (한국의 경제 구조)",
    "한국의 경제 구조 · 경제개발 5개년 계획 · 국내총생산 · 국민소득 · 제조업 · 서비스업",
    requires=[],
    cards=[
        card("Topic A: The structure of the Korean economy (한국의 경제 구조)",
             "The following excerpt from a high school student’s homework provides an overview of the Korean economy. (The English is mine; the book gives none. The text is the book’s with the numbers and letters spelled out [GDP is 지디피, OECD is 오이씨디]. The book’s footnotes: –(으)며 can be replaced with the conjunctive ending –고. OECD is the Organization for Economic Cooperation and Development. 세계은행 [the World Bank] provides loans and grants to developing countries.)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter). 일인당 is the book’s 1인당; 조 means trillion, 억 hundred million and 만 ten thousand.", tables=_words(_A_WORDS)),
        card("한국어에는: 형 (型)",
             "The Sino-Korean syllable 형 (型) means shape, type, model, or style. It is often used as a word suffix: 미래형 자동차 (a futuristic-style car), 최신형 스마트폰 (a newest-style smartphone), and B형/O형 혈액 (Type B/Type O in ABO blood group system)."),
        card("한국에서는: 경제개발 5개년 계획",
             "경제개발 5개년 계획 is a government-led plan that was implemented seven times between the 1960s and 1990s. Each development plan had a different focus. For example, 제1차 경제개발 5개년 계획 (1962–1966) was aimed at securing sources of energy, increasing the income of farmers, and building infrastructure. Manufacturing, production, and exports increased noticeably. During 제3차 (1972–1976) and 제4차 경제개발 5개년 계획 (1977–1981), investment in heavy industries increased, and the development of technology strengthened the nation’s competitiveness in the global economy.\n\n"
             "경제개발 5개년 계획 continued until 1996. However, rapid expansion focusing on quantitative growth resulted in many problems: uneven development among different regions, falling participation in agriculture by young people, a growing gap between the rich and poor, etc. Having recognized these issues, the Korean government is now making efforts to improve the quality of life for its people. At the same time, the government is attempting to grow its GDP and make advancements in cutting-edge technologies."),
        card("Activities left out", "The presentation steps of Topic A (SMART Board; reading and listening along; reviewing with the teacher) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT, k=3)
        + [M("What was Korea centered on until the early 1960s?", "Agriculture", ["Industry", "Services", "Fishing"], "농업 중심."), M("What changed the economic structure toward industry?", "The five-year economic development plan", ["A war", "A treaty", "A new currency"], "경제개발 5개년 계획."), M("What is Korea’s GDP this year?", "1.6 trillion dollars", ["16 billion dollars", "160 trillion dollars", "1.6 million dollars"], "일 조 육천억."), M("Where does Korea rank among OECD countries?", "13th", ["3rd", "30th", "1st"], "십삼 위."), M("What is the per capita national income?", "About 32,000 dollars", ["About 3,200 dollars", "About 320,000 dollars", "About 2,000 dollars"], "삼만 이천 불."), M("What growth rate does the World Bank foresee?", "1.5 percent", ["15 percent", "0.5 percent", "5 percent"], "일 점 오."), M("What are Korea’s main industries?", "Automobiles, shipbuilding, electronics and semiconductors", ["Farming and fishing", "Mining and textiles", "Tourism and finance"], "제조업과 첨단기술."), M("What share is low?", "Service industries’ share of the national economy", ["Manufacturing", "Exports", "Investment"], "서비스업 비중."),
           F("한국은 ___ 중심의 국가에서 공업 중심의 국가로 바뀌었다. (agriculture)", "농업", ["어업", "서비스업"], "농업."), F("한국의 주요 산업은 조선, 전자 등의 ___입니다. (manufacturing)", "제조업", ["서비스업", "어업"], "제조업."), F("서비스업이 국가 경제에서 차지하는 ___은 낮은 편이다. (share)", "비중", ["수준", "구조"], "비중."), F("한국 정부는 경제를 선진국형으로 ___시키기 위해 노력하고 있다. (develop)", "발전", ["하락", "급감"], "발전."), F("세계은행은 내년 경제성장률을 일 점 오 퍼센트로 ___ 있다. (foresees)", "내다보고", ["차지하고", "투자하고"], "내다보다."),
           read_q("한국의 경제 구조"), read_q("한국은 농업 중심의 국가였습니다"), read_q("일인당 국민소득은 약 삼만 이천 불입니다"), read_q("서비스업이 차지하는 비중은 낮은 편입니다"), read_q("첨단기술 산업")]
    ),
)

# ================================================================== L4 Follow-ups A: large numbers
_FC = [
    ("정부는 올해 우리 경제가 오 퍼센트 성장해, 오이씨디 국가 중 최고 수준의 성장률을 보일 것으로 예상한다.", "The government expects our economy to grow 5 percent this year and show the highest level of growth rate among OECD countries."),
    ("반도체와 자동차 등 기존의 주요 산업은 물론 에너지와 녹색산업이 크게 성장할 것으로 전망하고 있다.", "It forecasts that, not to mention the existing major industries such as semiconductors and automobiles, energy and green industries will grow greatly."),
    ("그렇지만 경제전문가들은 두 가지 문제점이 계속될 것으로 본다.", "However, economic experts think two problems will continue."),
    ("첫째는 일자리 부족 문제이다.", "The first is the problem of a shortage of jobs."),
    ("특히 이십 대에서 삼십 대 젊은이들의 취업이 계속 어려울 것으로 본다.", "In particular, they think employment for young people in their twenties and thirties will continue to be difficult."),
    ("둘째, 전문가들은 대기업 중심의 경제구조가 바뀌지는 않을 것으로 예상한다.", "Second, the experts expect that the big-company-centered economic structure will not change."),
    ("대기업 중심의 경제구조는 중소기업의 성장과 발전을 어렵게 하기 때문에 문제가 된다는 것이다.", "The point is that the big-company-centered economic structure becomes a problem because it makes the growth and development of small and medium-sized companies difficult."),
]
_NUM = [("만", "10,000 (ten thousand)"), ("억", "100,000,000 (one hundred million)"), ("조", "1,000,000,000,000 (one trillion)")]
_NX = [("삼만 이천", "32,000"), ("오만", "50,000"), ("십만", "100,000"), ("백만", "1,000,000"), ("이백만", "2,000,000"), ("천만", "10,000,000"), ("오천만", "50,000,000"), ("일억", "100,000,000"), ("오억", "500,000,000"), ("이십억", "2,000,000,000"), ("육천억", "600,000,000,000"), ("일 조", "1,000,000,000,000"), ("일 조 육천억", "1,600,000,000,000"), ("일 조 오천억", "1,500,000,000,000")]
L4 = lesson(
    "Ch 45 · Follow-ups A: large numbers and forecasts",
    "만 · 억 · 조 · 큰 수 읽기 · 경제 전망 · 일자리 부족 · 대기업 중심의 경제구조",
    requires=[],
    cards=[
        card("Reading large numbers: 만, 억, 조",
             "One objective of the chapter is to read and say large numbers in Korean. The Korean number system groups digits by units of ten thousand: 만 (10,000), 억 (100,000,000) and 조 (1,000,000,000,000), the last of which the chapter’s core vocabulary lists (조 [兆]: trillion). This table is my own summary of the numbers that appear in the chapter (the sample amounts are the book’s or typical of its examples).",
             tables=[ktable(_NUM), table(["Korean", "Number"], [[a, b] for a, b in _NX], say=[0])]),
        card("Follow-up 2 (Reading): forecasts for the Korean economy",
             "The following passage is about forecasts for the Korean economy (the book glosses nothing here). The book asks you to list two forecasts made by the government and two forecasts made by the experts. The passage is the book’s with the numbers spelled out (20–30대 is 이십 대에서 삼십 대); the English and the answers are mine.",
             examples=passage(_FC)),
        card("The answers (mine)", "",
             tables=[table(["Question", "Answer (mine)"], [["1. Two forecasts made by the government", "The economy will grow 5% this year, the highest growth rate among OECD countries; energy and green industries will grow greatly, as well as the existing major industries such as semiconductors and automobiles"], ["2. Two forecasts made by the experts", "The shortage of jobs will continue, with employment hard especially for people in their 20s and 30s; the big-company-centered economic structure will not change, which makes the growth of small and medium-sized companies difficult"]])]),
        card("Activities left out", "Follow-up 1 (a SMART Board activity and a listening activity: a news report about the recent Korean economy, filling in the GDP, the gross national income [GNI] and the per capita national income, each with the world ranking and the amount in dollars, and saying how this year’s per capita income compares with last year’s) is audio and computer work."),
    ],
    exercises=uniq(
        _tr(_FC, k=3)
        + [M("How much is 만?", "10,000", ["1,000", "100,000", "1,000,000"], "만."), M("How much is 억?", "100,000,000", ["10,000", "1,000,000,000", "1,000,000"], "억."), M("How much is 조?", "1,000,000,000,000", ["100,000,000", "10,000,000,000", "1,000,000"], "조."), M("What is 삼만 이천?", "32,000", ["3,200", "320,000", "30,002"], "삼만 이천."), M("What is 일 조 육천억?", "1.6 trillion", ["16 billion", "160 billion", "1.06 trillion"], "일 조 육천억."), M("What is 오천만?", "50,000,000", ["5,000,000", "500,000", "5,000"], "오천만."), M("What does the government expect for growth this year?", "5%, the highest among OECD countries", ["1.5%", "0%", "10%"], "오 퍼센트."), M("What problem do experts say will continue?", "A shortage of jobs", ["Too many jobs", "High prices only", "Low taxes"], "일자리 부족."), M("Why is a big-company-centered structure a problem?", "It makes the growth of small and medium companies difficult", ["It lowers exports", "It raises taxes", "It closes banks"], "중소기업의 성장."),
           F("일인당 국민소득은 약 ___ 불입니다. (32,000)", "삼만 이천", ["삼천 이백", "삼십이만"], "삼만 이천."), F("일 조 오천억 원은 정말 큰 ___입니다. (amount)", "금액", ["수준", "구조"], "금액."), F("정부는 올해 우리 경제가 오 퍼센트 ___할 것으로 예상한다. (grow)", "성장", ["하락", "급감"], "성장."), F("두 가지 ___이 계속될 것으로 본다. (problems)", "문제점", ["장점", "단점"], "문제점."), F("대기업 중심의 ___가 바뀌지는 않을 것이다. (structure)", "경제구조", ["일자리", "취업"], "경제구조."),
           read_q("일 조 육천억 달러"), read_q("삼만 이천 불"), read_q("경제가 오 퍼센트 성장합니다"), read_q("일자리 부족 문제가 계속됩니다"), read_q("대기업 중심의 경제구조")]
    ),
)


# ================================================================== L5 Activities A: sectors
_SEC = [
    ("제 삼촌은 배를 만드는 회사에서 근무합니다.", "My uncle works at a company that builds ships.", "c. 조선업", "shipbuilding industry"),
    ("우리 큰 형은 올해 쌀 수확량이 줄어들어 속상해합니다.", "My eldest brother is upset because this year’s rice harvest has decreased.", "b. 농업", "agriculture"),
    ("동생은 전자 제품을 만드는 회사에서 일합니다.", "My younger sibling works at a company that makes electronic products.", "d. 제조업", "manufacturing industry"),
    ("저는 배를 타고 바다에서 물고기를 잡는 일을 합니다.", "I ride a boat and catch fish at sea.", "e. 어업", "fishing industry"),
    ("누나는 대한 호텔에서 과장으로 일합니다.", "My older sister works as a section chief at the Daehan Hotel.", "a. 서비스업", "service industry"),
]
_IST = [
    ("경제구조가 주로 농업위주이다.", "The economic structure is mainly agriculture-centered.", "no"),
    ("정보통신기술과 첨단기술 산업이 강세이다.", "Information and communication technology and cutting-edge technology industries are strong.", "yes"),
    ("일인당 국민소득이 매우 낮다.", "The per capita national income is very low.", "no"),
    ("미래형 로봇이나 반도체 산업이 발전되어 있다.", "Futuristic robot and semiconductor industries are developed.", "yes"),
    ("국내총생산이 아주 높고 오이씨디에 가입되어 있다.", "The gross domestic product is very high and it is a member of the OECD.", "yes"),
]
L5 = lesson(
    "Ch 45 · Activities A: sectors and industrialized countries",
    "제조업 · 서비스업 · 어업 · 농업 · 조선업 · 산업화된 국가 · 경제구조",
    requires=[],
    cards=[
        card("Activity 1 (Reading) a: which sector?",
             "The following sentences are about various industry sectors in which a person’s family member works. The book asks you to choose the sector from the box (a. 서비스업 b. 농업 c. 조선업 d. 제조업 e. 어업). The sentences are the book’s (the numerals are dropped); the English and the answers are mine.",
             tables=[table(["Sentence", "Sector (mine)", "English"], [[a, c, d] for a, b, c, d in _SEC], say=[0]), table(["English of the sentence (mine)"], [[b] for a, b, c, d in _SEC])]),
        card("Activity 1 (Reading) b: industrialized countries",
             "Read the sentences and check those that describe industrialized countries (the sentences are the book’s; my answers and the English):",
             tables=[table(["Sentence", "Describes an industrialized country? (mine)", "English (mine)"], [[a, c, b] for a, b, c in _IST], say=[0])]),
        card("Activities left out", "Activity 2 (listening to three presentations in which a student reports about a country’s economy, filling in the expected economic growth rate, next year’s GDP and the growing industry; the book glosses 인공지능: AI and 벗어나다: to get out) and Activity 3 (“한국의 경제가 이렇게 달라졌어요”: two partners each read a part of an article about changes in Korea’s economic structure from the 1960s to the present, filling in the major industries and trend and the per capita national income for the 1960s–1980s and the 1990s–2020s, exchanging the information, and presenting; the article itself is not printed in the student book text) are audio and pair activities."),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c, d in _SEC] + [(a, b) for a, b, c in _IST], k=3)
        + [M("Which sector does 배를 만드는 회사 belong to?", "조선업", ["농업", "어업", "서비스업"], "c."), M("Which sector does 쌀 수확량 belong to?", "농업", ["어업", "제조업", "조선업"], "b."), M("Which sector does 전자 제품을 만드는 회사 belong to?", "제조업", ["서비스업", "어업", "농업"], "d."), M("Which sector does 바다에서 물고기를 잡는 일 belong to?", "어업", ["농업", "조선업", "제조업"], "e."), M("Which sector does 호텔 belong to?", "서비스업", ["제조업", "농업", "어업"], "a."), M("Does 경제구조가 주로 농업위주이다 describe an industrialized country?", "No", ["Yes", "Only in Asia", "Only in the past"], "My answer."), M("Does 정보통신기술과 첨단기술 산업이 강세이다 describe an industrialized country?", "Yes", ["No", "Only in Asia", "Only in the past"], "My answer."), M("Does 일인당 국민소득이 매우 낮다 describe an industrialized country?", "No", ["Yes", "Only in cities", "Only in the past"], "My answer."),
           F("제 삼촌은 배를 만드는 ___에서 근무합니다. (shipbuilding)", "조선업", ["어업", "농업"], "조선업."), F("저는 배를 타고 바다에서 물고기를 잡는 ___을 합니다. (fishing)", "어업", ["농업", "공업"], "어업."), F("동생은 전자 제품을 만드는 ___에서 일합니다. (manufacturing)", "제조업", ["어업", "농업"], "제조업."), F("누나는 대한 호텔에서 ___으로 일합니다. (section chief)", "과장", ["사장", "차장"], "과장."), F("우리 큰 형은 올해 쌀 ___이 줄어들어 속상해합니다. (harvest)", "수확량", ["수입량", "수출량"], "수확량."),
           read_q("제 삼촌은 배를 만드는 회사에서 근무합니다"), read_q("저는 바다에서 물고기를 잡는 일을 합니다"), read_q("동생은 전자 제품을 만드는 회사에서 일합니다"), read_q("누나는 호텔에서 과장으로 일합니다"), read_q("국내총생산이 아주 높습니다")]
    ),
)

# ================================================================== L6 Topic B
_B_TXT = [
    ("한국의 무역", "Korea’s trade"),
    ("한국무역협회 케이아이티에이의 통계에 따르면, 우리나라의 무역량은 꾸준히 증가해 왔다.", "According to the statistics of the Korea International Trade Association (KITA), our country’s trade volume has been increasing steadily."),
    ("천구백사십육 년 우리나라의 수출액은 삼백오십사만 달러 수준이었으나 천구백육십사 년 일억 달러로 증가했고, 이천십팔 년에는 처음으로 육천억 달러를 넘었다.", "In 1946 our country’s export amount was at the level of 3.54 million dollars, but it increased to 100 million dollars in 1964 and, in 2018, exceeded 600 billion dollars for the first time."),
    ("특히 지난 오 년간 우리나라의 수출 증가율은 연평균 삼 점 육 퍼센트로 세계 수출 순위 육 위에서 칠 위에 오르기도 했다.", "In particular, over the past five years our country’s export growth rate was 3.6 percent on a yearly average, and it even reached 6th to 7th place in world export rankings."),
    ("우리나라의 무역수지는 전 세계적인 경제불황에도 불구하고 전반적으로 흑자를 기록했다.", "Our country’s trade balance recorded a surplus overall in spite of the worldwide economic recession."),
    ("그러나 최근 이상기후나 전쟁 등에 따른 글로벌 경제 환경의 변화는 앞으로 우리나라의 무역수지에 적지 않은 영향을 줄 것으로 예상된다.", "However, recent changes in the global economic environment due to abnormal weather, wars and so on are expected to have no small influence on our country’s trade balance in the future."),
    ("우리나라의 수출 대상국은 천구백칠십 년대 백삼십칠 개국에서 이천 년대 이백이십팔 개국으로 증가했다.", "The number of our country’s export destination countries increased from 137 countries in the 1970s to 228 countries in the 2000s."),
    ("천구백칠십 년대와 팔십 년대에는 미국과 일본이 전체 수출의 육십 퍼센트 이상을 차지했다.", "In the 1970s and 1980s, the U.S. and Japan accounted for more than 60 percent of total exports."),
    ("그러나 천구백구십 년대에는 미국과 일본의 비중이 삼십 퍼센트로 하락했다.", "But in the 1990s the share of the U.S. and Japan fell to 30 percent."),
    ("이천 년 이후 중남미와 중국 등 새로운 시장을 개척하면서 수출 대상국이 꾸준히 늘어나고 있다.", "Since 2000, as new markets such as Central and South America and China have been developed, the number of export destination countries has been steadily increasing."),
    ("천구백칠십 년대 우리나라의 주요 수출 품목은 섬유, 신발 등이었다.", "In the 1970s, our country’s main export items were textiles, shoes and so on."),
    ("팔십 년대에는 전기 전자 분야의 수출이 급증했다.", "In the 1980s, exports in the electrical and electronics field increased rapidly."),
    ("주요 수출 품목은 반도체와 컴퓨터, 가전제품이었다.", "The main export items were semiconductors, computers and home appliances."),
    ("구십 년대부터 반도체, 기계, 자동차, 선박 등이 꾸준히 주요 수출 품목이 되었다.", "From the 1990s, semiconductors, machinery, automobiles, ships and so on steadily became main export items."),
    ("현재 우리나라의 주요 수입 품목은 원유 등 원자재와 농산물이다.", "Currently our country’s main import items are raw materials such as crude oil, and agricultural products."),
]
_B_WORDS = ["개척", "급감", "급증", "기계", "농산물", "무역수지", "~분기", "불황", "석유", "섬유", "수요", "순위/~위", "원유", "원자재", "적자", "전반적", "통계", "평균", "품목", "하락", "호황", "흑자"]
L6 = lesson(
    "Ch 45 · Topic B: Korea’s trade (한국의 무역)",
    "한국의 무역 · 수출 · 수입 · 무역수지 · 흑자 · 적자 · 수출 대상국 · 주요 수출 품목",
    requires=[],
    cards=[
        card("Topic B: Korea’s trade (한국의 무역)",
             "The following excerpt is from Korea’s trade report. (The English is mine; the book gives none. The text is the book’s with the numbers spelled out [KITA is 케이아이티에이; 1970~1980년대 is 천구백칠십 년대와 팔십 년대]. The book’s footnote: KITA [한국무역협회] stands for the Korea International Trade Association.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists ~에도/–(으)ㄴ/는데도 불구하고 (see the grammar).", tables=_words(_B_WORDS)),
        card("한국에서는: A Look at Korea’s Exports",
             "Korea has seen a dramatic shift in its major exports in recent decades. In the 1950s, its primary exports consisted of mining products like tungsten, graphite, and iron. During the 1960s, “light” (labor-intensive) industry products, such as shoes and wigs became leading exports, with textile products accounting for 40% of the total. The Korean government’s promotion of the heavy and chemical industries in the 1970s resulted in products such as steel and plastic goods becoming major export items in the 1980s. Other major export items during that decade included electronics, automobiles, and ships. Semiconductors took the lead in the 1990s, and in the 2000s, Korea expanded into consumer electronics, such as cellular phones and LCD monitors. Today, Korea stands as a major exporter of electrical machinery, equipment, and parts in the world, holding a 5.8% share of global exports in 2020. It also ranked ninth in exports of machinery, mechanical appliances, nuclear reactors, and boilers in the same year."),
        card("Presentation step b: the three paragraphs (mine)",
             "The book asks you to read the topic and fill in, in English, a title and the trend or changes for each paragraph. My answers:",
             tables=[table(["", "Title (mine)", "Overall trend and changes (mine)"], [["First paragraph", "Growth of trade volume and the trade balance", "Trade has increased steadily: exports rose from 3.54 million dollars (1946) to 100 million (1964) to over 600 billion (2018); export growth averaged 3.6% a year over five years; a surplus overall despite the recession, but global changes may affect it"], ["Second paragraph", "Export destinations", "Destination countries grew from 137 (1970s) to 228 (2000s); the U.S. and Japan took over 60% in the 1970s–80s but 30% in the 1990s; new markets (Central/South America, China) since 2000"], ["Third paragraph", "Main export and import items", "1970s textiles, shoes; 1980s electronics surged (semiconductors, computers, home appliances); from the 1990s semiconductors, machinery, cars, ships; imports now crude oil and other raw materials, and farm products"]])]),
        card("Activities left out", "The presentation steps of Topic B (SMART Board; reading and listening along; reviewing with the teacher) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT, k=3)
        + [M("What does the statistics say about the trade volume?", "It has been steadily increasing", ["It has been falling", "It is unchanged", "It doubled last year"], "꾸준히 증가."), M("How large were the 2018 exports?", "Over 600 billion dollars", ["About 354 million dollars", "100 million dollars", "6 trillion dollars"], "육천억 달러."), M("What was the trade balance overall?", "A surplus", ["A deficit", "Zero", "Unknown"], "흑자."), M("How many export destination countries in the 2000s?", "228", ["137", "60", "30"], "이백이십팔 개국."), M("What share did the U.S. and Japan have in the 1970s–80s?", "More than 60 percent", ["About 30 percent", "About 10 percent", "All"], "육십 퍼센트 이상."), M("What happened to their share in the 1990s?", "It fell to 30 percent", ["It rose", "It stayed", "It vanished"], "삼십 퍼센트로 하락."), M("What new markets were developed since 2000?", "Central and South America and China", ["Europe only", "Africa only", "Russia only"], "중남미와 중국."), M("What surged in the 1980s?", "Electrical and electronics exports", ["Textile exports", "Rice exports", "Shoe exports"], "전기 전자."), M("What are the main import items now?", "Raw materials such as crude oil, and agricultural products", ["Cars", "Semiconductors", "Ships"], "원유 등 원자재와 농산물."),
           F("우리나라의 무역___는 전반적으로 흑자를 기록했다. (trade balance)", "수지", ["수요", "수준"], "무역수지."), F("경제불황에도 ___하고 흑자를 기록했다. (in spite of)", "불구", ["상관", "대비"], "불구하고."), F("팔십 년대에는 전기 전자 분야의 수출이 ___했다. (increased rapidly)", "급증", ["급감", "하락"], "급증."), F("주요 수입 품목은 원유 등 ___와 농산물이다. (raw materials)", "원자재", ["섬유", "기계"], "원자재."), F("우리나라의 수출 ___은 연평균 삼 점 육 퍼센트였다. (growth rate)", "증가율", ["수익률", "이자율"], "증가율."),
           read_q("한국의 무역"), read_q("우리나라의 무역량은 꾸준히 증가해 왔습니다"), read_q("무역수지는 흑자를 기록했습니다"), read_q("중남미와 중국 등 새로운 시장을 개척했습니다"), read_q("주요 수출 품목은 반도체와 컴퓨터와 가전제품이었습니다")]
    ),
)

# ================================================================== L7 Follow-ups B: trade balance
_TQ = [
    ("올해 일 분기 무역수지는 적자, 이 분기 무역수지는 흑자를 기록했다.", "This year’s first-quarter trade balance recorded a deficit, and the second-quarter trade balance recorded a surplus."),
    ("일 분기 수출은 기계, 선박 등이 강세를 보였지만, 석유 등 원자재와 농산물 수입이 급증하면서 적자를 기록했다.", "In the first quarter, exports of machinery, ships and so on were strong, but a deficit was recorded as imports of raw materials such as oil and of agricultural products rapidly increased."),
    ("지역별로는 중남미 국가에서의 수입이 오십팔 퍼센트나 증가했다.", "By region, imports from Central and South American countries increased by as much as 58 percent."),
    ("이 분기에는 수출이 강세를 보이며 흑자를 기록했다.", "In the second quarter, exports were strong and a surplus was recorded."),
    ("품목별로는 섬유와 기계 수출이 급증했고, 농산물 수입이 증가세를 보였다.", "By item, exports of textiles and machinery increased rapidly, and imports of agricultural products showed an upward trend."),
    ("국가별로는 미국, 유럽 등 전반적으로 선진국으로의 수출이 강세를 보였다.", "By country, exports to advanced countries overall, such as the U.S. and Europe, were strong."),
]
L7 = lesson(
    "Ch 45 · Follow-ups B: a quarterly trade balance report",
    "분기 무역수지 · 적자 · 흑자 · 수출 강세 · 수입 급증 · 중남미 · 선진국",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a news report about Korea’s trade balance",
             "The following news report is about Korea’s trade balance. The book asks you to check whether each quarter’s trade balance was a deficit or a surplus and to fill in the trade items in English. The report is the book’s with the numbers spelled out (1분기 is 일 분기); the English and the answers are mine.",
             examples=passage(_TQ)),
        card("The table filled in (mine)", "",
             tables=[table(["", "Trade balance", "Exports (mine)", "Imports (mine)"], [["1st quarter", "Deficit", "Machinery, ships (strong)", "Raw materials such as oil, and agricultural products (rapid increase; imports from Central and South America up 58%)"], ["2nd quarter", "Surplus", "Textiles, machinery (rapid increase); exports to advanced countries such as the U.S. and Europe strong", "Agricultural products (upward trend)"]])]),
        card("Activities left out", "Follow-up 2 (listening to a news report about trade and checking surplus or deficit, writing the export and import trends and items), Activities 1 and 2 on the Activities pages (SMART Board; listening to a YTN news clip about Korea’s international trade and, with the book’s glosses 신흥: newly risen and 주력: major, filling in the amount of the trade balance and the influencing factors; then checking with the video) and Activity 3 (two partners with Korea’s 2022 annual international trade report: one holds the export report and the other the import report, they fill in the trends in trade during 2021 vs. 2022, the factors, the major trading partners and the major trade products, exchange the information in Korean, write a report with charts in the class notebook and present it) are audio, video, pair and group activities."),
    ],
    exercises=uniq(
        _tr(_TQ, k=3)
        + [M("What was the first quarter’s trade balance?", "A deficit", ["A surplus", "Zero", "Unknown"], "적자."), M("What was the second quarter’s trade balance?", "A surplus", ["A deficit", "Zero", "Unknown"], "흑자."), M("Why did the first quarter record a deficit?", "Imports of raw materials and farm products increased rapidly", ["Exports collapsed", "Prices fell", "A holiday"], "수입 급증."), M("By how much did imports from Central and South America rise?", "58 percent", ["8 percent", "5.8 percent", "580 percent"], "오십팔 퍼센트."), M("What exports increased rapidly in the second quarter?", "Textiles and machinery", ["Oil and rice", "Ships only", "Shoes"], "섬유와 기계."), M("To whom were exports strong?", "Advanced countries such as the U.S. and Europe", ["Africa", "Antarctica", "Neighbors only"], "선진국."),
           F("올해 일 분기 무역수지는 ___를 기록했다. (deficit)", "적자", ["흑자", "호황"], "적자."), F("이 분기에는 수출이 강세를 보이며 ___를 기록했다. (surplus)", "흑자", ["적자", "불황"], "흑자."), F("석유 등 원자재와 농산물 수입이 ___하면서 적자를 기록했다. (rapidly increased)", "급증", ["급감", "하락"], "급증."), F("___별로는 섬유와 기계 수출이 급증했다. (by item)", "품목", ["지역", "국가"], "품목별."), F("국가별로는 선진국으로의 수출이 ___를 보였다. (strength)", "강세", ["약세", "불황"], "강세."),
           read_q("올해 일 분기 무역수지는 적자를 기록했습니다"), read_q("이 분기에는 흑자를 기록했습니다"), read_q("농산물 수입이 급증했습니다"), read_q("섬유와 기계 수출이 급증했습니다"), read_q("선진국으로의 수출이 강세를 보였습니다")]
    ),
)


# ================================================================== L8 Grammar A: ~에도 (불구하고)
_PG1 = [("불황에도 불구하고 수출은 증가했습니다.", "In spite of the recession, exports have increased."), ("매일 열심히 운동함에도 불구하고 체중이 줄지 않아요.", "In spite of working out diligently every day, I am not losing weight."), ("매일 열심히 운동하는데도 불구하고 체중이 줄지 않아요.", "In spite of working out diligently every day, I am not losing weight.")]
_PG2 = [("주중임에도 불구하고 놀이공원에 사람이 많습니다.", "Despite its being a weekday, there are many people in the amusement park."), ("건물이 큰데도 불구하고 짓는 데 시간이 별로 안 걸렸습니다.", "Despite the fact that the building is big, it did not take long to build."), ("공부를 열심히 하는데도 불구하고 성적이 별로 안 좋아요.", "In spite of my studying diligently, my grades are not very good."), ("여러 번 실패했는데도 불구하고 포기하지 않았다.", "Despite the fact that he had failed several times, he did not give up."), ("부상을 입었는데도 불구하고 경기에 나갔습니다.", "Despite being injured, she went out to compete.")]
_PGM = [("감기약을 복용했는데도 계속 기침해요.", "I keep coughing even though I took cold medicine."), ("비가 오는데도 야구 경기를 계속 해요.", "They keep playing the baseball game even though it is raining."), ("물가가 오르는데도 비싼 수입품이 잘 팔려요.", "Expensive imported goods sell well even though prices are rising."), ("휴일인데도 출근해야 해요.", "I have to go to work even though it is a holiday."), ("주말에 푹 쉬었는데도 여전히 피곤해요.", "I am still tired even though I rested well on the weekend."), ("불황에도 월급은 오르지 않아요.", "Even in a recession, salaries do not go up."), ("공부를 열심히 하는데도 성적이 안 올라요.", "My grades do not go up even though I study hard."), ("원유 가격이 하락했는데도 기름값이 비싸요.", "Gas is expensive even though the crude oil price has fallen.")]
_KY = [
    ("김연아는 이십칠 일 한국시간 밤 이탈리아 토리노 팔라벨라 빙상장에서 치러진 대회 여자 싱글 프리스케이팅에서 몇 차례 실수에도 불구하고 백삼십 점 사구를 받아 은메달을 따냈다.", "Kim Yuna, at the women’s singles free skating of the competition held at the Palavela ice rink in Turin, Italy, on the night of the 27th (Korean time), won the silver medal by receiving 130.49 points despite several mistakes."),
    ("전날 칠 위에 그쳤던 쇼트프로그램과 합계 점수는 백구십 점 칠구로 일본의 아사다 마오 선수에 이어 이 위를 기록했다.", "Her total score with the short program, in which she had stopped at 7th place the day before, was 190.79, recording second place after Japan’s Asada Mao."),
    ("김연아 선수는 많은 어려움을 겪은 시즌이었다.", "Skater Kim Yuna said, “It was a season in which I went through many difficulties.”"),
    ("쇼트프로그램에서 잘 못했는데 은메달을 따서 기쁘다며 웃었다.", "She smiled, saying, “I did not do well in the short program, but I am glad to have won the silver medal.”"),
]
_LT = [("김 이병을 이달의 학생으로 추천합니다.", "I recommend Pvt. Kim as the “student of the month.”"), ("김 이병은 얼마 전에 독감에 걸려서 아주 고생했어요.", "Pvt. Kim recently caught the flu and had a very hard time."), ("그래서 며칠간 학교에도 못 나왔어요.", "So he could not even come to school for a few days."), ("기숙사에서 공부를 열심히 해서 시험도 잘 봤습니다.", "He studied hard in the dormitory and did well on the exam too."), ("김 이병은 독감에 걸렸는데도 불구하고 시험 성적이 좋았습니다.", "Despite having caught the flu, Pvt. Kim’s exam results were good."), ("그래서 김 이병이 이달의 학생으로 뽑히면 좋겠습니다.", "So I hope Pvt. Kim is chosen as the “student of the month.”")]
L8 = lesson(
    "Ch 45 · Grammar A: ~에도 (불구하고) and –(으)ㄴ/는데도 (불구하고)",
    "~에도 불구하고 · -(으)ㄴ/는데도 불구하고 · -(으)ㅁ에도 · 불황에도 · 부상을 입었는데도 · 이달의 학생",
    requires=[],
    cards=[
        card("In spite of; despite",
             "Both ~에도 (불구하고) and –(으)ㄴ/는데도 (불구하고) can be translated as in spite of or despite. However, ~에도 (불구하고) is preceded by a noun or a gerund form –(으)ㅁ, and –데도 (불구하고) is preceded by an attributive form of a verb. Keep in mind that 불구하고 can be omitted. For example (the English is the book’s; the book writes 불구하고 in parentheses and I write it in full):",
             examples=passage(_PG1)),
        card("The patterns",
             "“In spite of/despite”: noun/–(으)ㅁ + 에도 (불구하고); verb + (으)ㄴ/는데도 (불구하고). More examples (the English is the book’s):",
             examples=passage(_PG2)),
        card("Follow-up 1 (Reading and speaking): connect the phrases",
             "a. Find two phrases that can be connected with “~에도/–(으)ㄴ/는데도 (불구하고)” and draw a line (there may be more than one correct answer). The book’s left phrases are 감기약을 복용하다, 비가 오다, 물가가 오르다, 휴일이다, 주말에 푹 쉬었다, 불황, 공부를 열심히 하다 and 원유 가격이 하락했다; the right phrases are 비싼 수입품이 잘 팔리다, 성적이 안 오르다, 기름값이 비싸다, 계속 기침하다, 야구 경기를 계속 하다, 월급은 오르지 않는다, 출근해야 하다 and 여전히 피곤하다. My pairings, each as a sentence (the English is mine):",
             examples=passage(_PGM)),
        card("Follow-up 3 (Reading): a figure skater in a competition",
             "The following news article is about a figure skater who participated in a competition. The book asks you to fill in her final performance result, her reaction to the result and the English translation of the underlined sentence. The article is the book’s with the numbers spelled out (130.49점 is 백삼십 점 사구; the quotation marks are dropped); the English is mine.",
             examples=passage(_KY)),
        card("The table filled in (mine)", "",
             tables=[table(["Her final performance result", "Her reaction", "The underlined sentence (mine)"], [["Silver medal in the women’s singles free skating with 130.49 points; total 190.79, second after Japan’s Asada Mao", "She smiled; it was a season with many difficulties and she was glad to win silver after doing poorly in the short program", "“Despite several mistakes, she received 130.49 points and won the silver medal.”"]])]),
        card("Follow-up 4 (Writing and speaking): a letter of recommendation",
             "You write a letter of five to six sentences recommending a classmate who has overcome many obstacles as “student of the month”, with at least one sentence including ~에도/–(으)ㄴ/는데도 (불구하고), and some background information on the candidate; then you post the letters on the wall, read others’ and choose a student. The book’s model (the English is mine; the quotation marks are dropped):",
             examples=passage(_LT)),
        card("Activities left out", "Follow-up 2 (listening to four news clips and translating them into English; the book glosses 폐수: waste water) is an audio activity; the pair practice of Follow-up 1 b and the wall-posting of Follow-up 4 are speaking activities."),
    ],
    exercises=uniq(
        _tr(_PG1 + _PG2 + _PGM + _KY + _LT, k=3)
        + [M("What does ~에도 (불구하고) mean?", "in spite of; despite", ["because of", "after", "instead of"], "The book’s note."), M("What precedes ~에도 (불구하고)?", "A noun or the gerund –(으)ㅁ", ["An attributive form", "A past stem", "A particle"], "The book’s note."), M("What precedes –(으)ㄴ/는데도 (불구하고)?", "An attributive form of a verb", ["A noun", "The gerund –(으)ㅁ", "A particle"], "The book’s note."), M("What can be omitted?", "불구하고", ["에도", "데도", "Nothing"], "The book’s note."), M("What does 불황에도 불구하고 수출은 증가했습니다 mean?", "In spite of the recession, exports increased", ["Because of the recession, exports fell", "After the recession, exports rose", "There was no recession"], "The book’s example."), M("What does 주중임에도 불구하고 놀이공원에 사람이 많습니다 mean?", "Despite its being a weekday, there are many people", ["Because it is a weekday, there are few", "On weekends there are many", "Weekday crowds are small"], "The book’s example."), M("How did Kim Yuna do in the free skating?", "She won the silver medal despite several mistakes", ["She won gold", "She lost", "She withdrew"], "은메달."), M("Who took first place over Kim Yuna in the total score?", "Japan’s Asada Mao", ["Kim Yuna herself", "An American skater", "A Russian skater"], "아사다 마오."),
           F("비가 오___ 야구 경기를 계속 해요. (even though)", "는데도", ["니까", "면서"], "-는데도."), F("휴일___ 출근해야 해요. (even though it is a holiday)", "인데도", ["이니까", "이라서"], "-인데도."), F("불황___ 불구하고 수출은 증가했습니다. (in spite of)", "에도", ["때문에", "마다"], "~에도."), F("독감에 ___ 불구하고 시험 성적이 좋았습니다. (caught)", "걸렸는데도", ["걸려서", "걸리면"], "-는데도."), F("매일 열심히 운동함에도 ___ 체중이 줄지 않아요. (in spite)", "불구하고", ["때문에", "생각하고"], "불구하고."),
           read_q("불황에도 불구하고 수출은 증가했습니다"), read_q("공부를 열심히 하는데도 성적이 별로 안 좋아요"), read_q("여러 번 실패했는데도 포기하지 않았다"), read_q("부상을 입었는데도 경기에 나갔습니다"), read_q("김 이병은 독감에 걸렸는데도 시험 성적이 좋았습니다")]
    ),
)

# ================================================================== L9 Topic C
_C_BRO = [
    ("보통예금", "Regular savings deposit"), ("기간 및 금액에 제한이 없음", "No limit on period or amount"), ("입금과 출금이 자유로움", "Free to deposit and withdraw"), ("이자율이 낮음", "Low interest rate"),
    ("정기예금", "Fixed-term deposit"), ("예금 후에 계약 기간 동안 찾지 않음", "After depositing, you do not withdraw during the contract period"), ("이자율이 높음", "High interest rate"),
    ("주식 투자", "Stock investment"), ("원하는 회사의 증권을 구입", "Buy the securities of a company you want"), ("수익성이 높음", "High profitability"),
    ("적금", "Installment savings"), ("계약 기간 동안 매월 일정 금액을 저축", "Save a fixed amount every month during the contract period"), ("계약 만기 후에 목돈 마련", "A lump sum is made after the contract matures"),
    ("펀드", "Fund"), ("투자 전문 회사를 통한 간접 투자", "Indirect investment through an investment specialist company"), ("투자 수수료가 높음", "High investment fee"),
    ("부동산 투자", "Real estate investment"), ("건물이나 땅을 구입", "Buy a building or land"), ("투자 비용이 높음", "High investment cost"), ("장기적인 투자로 적합", "Suitable as a long-term investment"),
]
_C_QA = [
    ("예금을 하려던 참이었다면?", "If you were just about to make a deposit?"),
    ("계좌를 열기 전에 먼저 이율을 비교하세요.", "Before opening an account, first compare interest rates."),
    ("은행마다 예금의 종류와 기간에 따라 이자율이 다릅니다.", "Each bank’s interest rate differs according to the type and period of the deposit."),
    ("수익성이 높은 투자는?", "Investments with high profitability?"),
    ("주식과 펀드가 있습니다.", "There are stocks and funds."),
    ("특히, 요즘은 펀드가 인기를 얻는 추세입니다.", "In particular, funds are gaining popularity these days."),
    ("펀드는 경험이 많은 전문가에게 투자를 맡긴다는 것이 장점입니다.", "The advantage of funds is that you entrust your investment to experienced experts."),
    ("하지만 주식과 펀드는 손해를 볼 위험성도 높습니다.", "But stocks and funds also carry a high risk of taking a loss."),
    ("부동산 투자의 장단점은?", "The strengths and weaknesses of real estate investment?"),
    ("부동산 투자는 수익성도 좋고 안정적이지만 현금화하는 데 시간이 걸립니다.", "Real estate investment is both profitable and stable, but it takes time to turn into cash."),
    ("거래 비용이 높다는 것도 단점입니다.", "The high transaction cost is also a drawback."),
]
_C_WORDS = ["거래", "계좌", "금액", "금융기관", "단기(적)", "땅", "만기", "보통예금", "손해", "수수료", "수익(성)", "예금", "이(자)율", "일정하다", "입금", "장기(적)", "적금(에/을 들다)", "적합하다", "정기예금", "주식/증권", "지급", "추세", "통장", "펀드"]
_BANK = [["Central bank", "한국은행"], ["Commercial banks", "케이비 국민은행, 하나은행, 신한은행, 우리은행, 외환은행"], ["Specialized banks", "농협, 수협, 산업은행, 중소기업은행"]]
L9 = lesson(
    "Ch 45 · Topic C: Where should I invest? (어디에 투자를 할까요?)",
    "보통예금 · 정기예금 · 주식 투자 · 적금 · 펀드 · 부동산 투자 · 이율 · 수수료 · 한국의 은행",
    requires=[],
    cards=[
        card("Topic C: Where should I invest? (어디에 투자를 할까요)",
             "The following brochure is adopted from an investment company’s guide. The brochure’s six boxes are listed first, then its three questions and answers. (The English is mine; the book gives none; the book’s “?” in the title is dropped, and “및” in the first line is kept; the box bullets “입/출금이 자유로움” is written 입금과 출금이 자유로움.)",
             examples=passage(_C_BRO) + passage(_C_QA)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –(으)려던 참이다 (see the grammar).", tables=_words(_C_WORDS)),
        card("한국에서는: 한국의 은행",
             "한국은행 functions similarly to the Federal Reserve Board in the United States. The primary function of 한국은행 is issuing currency, formulating and implementing monetary and credit policy, and managing foreign exchange reserves. Special banks, such as 농협 (농업협동조합) and 중소기업은행, are set up and owned by the Korean government to provide financial support to specific economic endeavors. In Korea, 우체국 not only provides mail services, but also financial services for the public, such as savings and insurance. (The book’s table of banks, with KB written 케이비:)",
             tables=[table(["Type", "Name"], _BANK)]),
        card("한국에서는: 예금의 종류",
             "There are three types of bank accounts used in Korea. 보통예금 (regular savings) is similar to a checking account in the United States. Customers can freely deposit and withdraw funds. 정기예금 is a time-deposit account and is similar to a CD (certificate of deposit). Customers have to deposit a specific amount for a specific period of time, based on a contract. 적금 is an installment savings account in which customers deposit a fixed amount each month during a specific contract period. Customers who open 정기예금 and 적금 cannot withdraw funds until the contract expires (만기), unless they close the account earlier, which results in a major loss of interest. In Korean banking, 통장 (a bankbook) is issued when the account is opened. For all banking transactions using 통장, either a stamp or the account holder’s signature is used."),
        card("Presentation step a: investment types and related words (mine)",
             "The first column of the book’s table lists investment types (보통예금, 적금, 주식, 펀드, 부동산); from the box 1. 금융기관 2. 장기적 3. 땅 4. 입금 5. 출금 6. 손해 7. 수수료 8. 이율 9. 만기 you choose the related words. My answers:",
             tables=[table(["Investment", "Related words (mine)"], [["보통예금", "1 (금융기관), 4 (입금), 5 (출금), 8 (이율)"], ["적금", "1 (금융기관), 4 (입금), 8 (이율), 9 (만기)"], ["주식", "6 (손해)"], ["펀드", "6 (손해), 7 (수수료)"], ["부동산", "2 (장기적), 3 (땅), 7 (거래 비용)"]])]),
        card("Activities left out", "The presentation steps of Topic C (reading and listening along, SMART Board, reviewing with the teacher) are audio and computer activities; Follow-up 1 (listening to a conversation between a financial consultant and an investor and checking whether the consultant’s opinion on 보통예금 and 주식 is positive or negative, with the reason) is an audio activity."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_BRO + _C_QA, k=3)
        + [M("Which account has a low interest rate and no limits?", "보통예금", ["정기예금", "적금", "펀드"], "이자율이 낮음."), M("Which account is not withdrawn during the contract period?", "정기예금", ["보통예금", "주식", "부동산"], "계약 기간 동안 찾지 않음."), M("Which investment buys the securities of a company?", "주식 투자", ["적금", "펀드", "부동산 투자"], "증권을 구입."), M("Which saves a fixed amount every month?", "적금", ["보통예금", "주식", "펀드"], "매월 일정 금액."), M("Which is an indirect investment through a specialist company?", "펀드", ["주식", "적금", "보통예금"], "간접 투자."), M("Which needs a lot of money and suits the long term?", "부동산 투자", ["보통예금", "펀드", "적금"], "건물이나 땅."), M("What should you compare before opening an account?", "Interest rates", ["Bank names", "Addresses", "Office hours"], "이율을 비교."), M("What is the advantage of funds?", "Entrusting experienced experts with the investment", ["No risk", "Very low fees", "Instant cash"], "전문가에게 맡긴다."), M("What is a drawback of real estate investment?", "It takes time to turn into cash and has high transaction costs", ["Low stability", "Low profitability", "Short term only"], "현금화하는 데 시간."),
           F("은행마다 예금의 종류와 기간에 따라 ___이 다릅니다. (interest rate)", "이자율", ["수수료", "금액"], "이자율."), F("적금은 계약 ___ 후에 목돈을 마련할 수 있습니다. (maturity)", "만기", ["손해", "거래"], "만기."), F("보통예금은 ___과 출금이 자유롭습니다. (deposit)", "입금", ["지급", "투자"], "입금."), F("펀드는 투자 ___가 높습니다. (fee)", "수수료", ["이율", "만기"], "수수료."), F("부동산은 건물이나 ___을 구입하는 투자입니다. (land)", "땅", ["통장", "계좌"], "땅."),
           read_q("어디에 투자를 할까요"), read_q("계좌를 열기 전에 먼저 이율을 비교하세요"), read_q("펀드는 인기를 얻는 추세입니다"), read_q("주식과 펀드는 손해를 볼 위험성도 높습니다"), read_q("부동산 투자는 장기적인 투자입니다")]
    ),
)


# ================================================================== L10 Follow-ups C: investment plans
_PA = [("삼 년 후에 직장을 그만두고 외국에 유학을 갈 생각입니다.", "In three years I plan to quit my job and go abroad to study."), ("유학준비를 위해 월급에서 일정금액을 모아 두고 싶습니다.", "To prepare for studying abroad, I want to set aside a fixed amount from my salary."), ("그래서 적금을 들기로 했어요.", "So I decided to open an installment savings account."), ("매달 얼마씩 은행에 꾸준히 돈을 넣으면 삼 년 후 계약 만기에는 목돈을 마련할 수 있으니까요.", "Because if I steadily put some money into the bank every month, I can make a lump sum at the contract’s maturity three years later.")]
_PB = [("제 남편이 받은 퇴직금을 투자할 생각입니다.", "I plan to invest the retirement allowance my husband received."), ("돈을 늘려서 나중에 전원주택을 사고 싶어요.", "I want to increase the money and buy a country house later."), ("그런데 남편과 저는 금융투자에 대해 잘 모릅니다.", "But my husband and I do not know much about financial investment."), ("그래서 펀드에 투자할 생각입니다.", "So I plan to invest in a fund."), ("펀드회사의 전문가가 투자를 대신해 주니까 좋아요.", "It is good because an expert at the fund company invests on my behalf."), ("수익성도 높은 편이더군요.", "I found the profitability is on the high side too.")]
_IC = [
    ("돈을 입금하거나 찾는 것이 자유롭지만 이자율이 낮다. 투자 금액과 기간에도 제한이 없다.", "Depositing or withdrawing money is free, but the interest rate is low. There is no limit on the investment amount and period either.", "c. 보통예금"),
    ("회사의 증권을 개인이 직접 사고 판다. 증권 값이 올라가면 돈을 쉽게 벌 수 있지만 값이 떨어지면 투자한 돈을 잃는다.", "Individuals buy and sell company securities directly. If the securities’ price goes up, you can make money easily, but if the price falls, you lose the money you invested.", "b. 주식 투자"),
    ("아파트나 집, 건물, 또는 땅에 투자한다. 많은 돈이 필요하고 투자 기간이 길다.", "You invest in an apartment, a house, a building, or land. A lot of money is needed and the investment period is long.", "e. 부동산 투자"),
    ("전문가가 개인을 대신해서 주식이나 증권에 투자한다. 개인이 투자하는 것보다 안전한 편이다.", "An expert invests in stocks or securities on behalf of an individual. It is on the safer side than an individual investing.", "d. 펀드 투자"),
    ("매달 정해진 금액을 계약한 기간 동안 입금한다. 이자율이 높은 편이고 계약 기간이 끝나면 목돈을 찾을 수 있다.", "You deposit a set amount every month during the contracted period. The interest rate is on the high side, and when the contract period ends you can withdraw a lump sum.", "a. 적금"),
]
_FA = [
    ("주식", "개인이 직접 주식에 투자한다. 위험성이 따르며 특히 주식에 대해서 잘 모르면 위험성이 더 크다. 경기 추세에 따라 가격이 오르면 짧은 기간 안에 많은 수익을 낼 수 있다. 하지만 주식 값이 떨어지면 손해를 볼 수 있다.", "An individual invests in stocks directly. It carries risk, and the risk is greater especially if you do not know much about stocks. If the price rises according to the economic trend, you can make a lot of profit in a short period. But if stock prices fall, you may take a loss."),
    ("주택적금", "집이 없는 사람이 주택 구입을 위해 저축하는 정기 적금이다. 주택은행에서만 들 수 있다. 정해진 계약 기간 동안 매월 일정 금액을 입금한다. 이자율이 높으며 주택 구입에 필요한 목돈을 마련할 수 있다.", "This is fixed-term installment savings that a person without a house saves for buying a home. You can open it only at the housing bank. You deposit a fixed amount every month during the set contract period. The interest rate is high and you can make the lump sum needed to buy a home."),
    ("펀드 투자", "개인 대신에 전문가가 주식이나 증권에 투자해 준다. 수수료를 지급해야 한다. 전문가가 투자하기 때문에 위험성이 낮은 편이다. 수익성도 좋은 편이지만 시장의 추세에 따라 손해를 볼 수도 있다.", "An expert invests in stocks or securities instead of the individual. You have to pay a fee. Because an expert invests, the risk is on the low side. Profitability is also good, but you may take a loss according to the market trend."),
    ("부동산 투자", "집이나 아파트, 건물, 또는 땅을 구입하는 재산 투자이다. 장기 투자이며 비교적 안정적인 투자이다. 특히 개발가능성이 있는 곳에 땅이나 건물을 사 두면 몇 년 후에 좋은 수익을 올릴 수도 있다.", "This is a property investment of buying a house, an apartment, a building, or land. It is a long-term and relatively stable investment. In particular, if you buy land or a building in a place with development potential, you may earn a good profit a few years later."),
]
L10 = lesson(
    "Ch 45 · Follow-ups C: investment plans and characteristics",
    "투자 계획 · 적금 · 펀드 · 주식 · 주택적금 · 부동산 투자 · 투자의 특징",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): two investment plans",
             "The book asks you to read two investment plans and fill in, in English, the type of investment, the advantage of the investment and the purpose of the investment for each. The plans are the book’s with the numbers spelled out (3년 is 삼 년); the English is mine.",
             examples=passage(_PA) + passage(_PB)),
        card("The table filled in (mine)", "",
             tables=[table(["", "Investment Plan A", "Investment Plan B"], [["Type of investment", "Installment savings (적금)", "A fund (펀드)"], ["Advantage of investment", "By depositing steadily every month, a lump sum is made at the contract’s maturity", "An expert at the fund company invests on the investor’s behalf; profitability is high"], ["Purpose of investment", "To prepare for studying abroad after quitting her job in three years", "To increase the husband’s retirement allowance and later buy a country house"]])]),
        card("Activity 1 (Reading): types of investment",
             "The following sentences describe the characteristics of different types of investment. The book asks you to write the letter of the type (a. 적금 b. 주식 투자 c. 보통예금 d. 펀드 투자 e. 부동산 투자) before each sentence. The sentences are the book’s; the answers and the English are mine.",
             tables=[table(["Sentence", "Type (mine)", "English (mine)"], [[a, c, b] for a, b, c in _IC], say=[0])]),
        card("Activity 3 b (Reading): ways to manage money",
             "The following text from a financial advisor is about ways to manage money (1. 주식 2. 주택적금 3. 펀드 투자 4. 부동산 투자). The book asks you to fill in the characteristics of each investment or type of savings in English. The text is the book’s (the table cells are read as four short paragraphs); the English is mine, and my summary follows.",
             examples=passage([(b, c) for a, b, c in _FA])),
        card("The characteristics filled in (mine)", "",
             tables=[table(["Type", "Characteristics (mine)"], [["1. Stocks", "Direct investment by an individual; risky, especially without knowledge; big profit in a short time if prices rise, loss if they fall"], ["2. Housing installment savings", "Fixed-term installment savings for people without a house; only at the housing bank; fixed monthly deposits; high interest; makes the lump sum for a home purchase"], ["3. Fund investment", "An expert invests for you; a fee must be paid; relatively low risk; good profitability but a loss is possible with market trends"], ["4. Real estate investment", "Buying a house, apartment, building or land; long-term and relatively stable; may bring good profit later if the place has development potential"]])]),
        card("Activities left out", "Activity 2 (a news report from MBC about investments: writing the topic, then a video with the percent of Koreans investing in stocks or funds, a table of percent against amount, and true/false statements about the profits) and Activity 3 a/c/d (listening to two callers seeking financial advice on a talk show, then discussing in Korean the best way for each caller to invest or save and summarizing the recommendation in the class notebook) are audio, video, pair and group activities."),
    ],
    exercises=uniq(
        _tr(_PA + _PB + [(a, b) for a, b, c in _IC] + [(b, c) for a, b, c in _FA], k=3)
        + [M("What is Plan A’s purpose?", "To prepare for studying abroad", ["To buy a house", "To start a business", "To retire"], "유학준비."), M("What type of investment is Plan A?", "Installment savings", ["A fund", "Stocks", "Real estate"], "적금."), M("What is Plan B’s purpose?", "To increase money and later buy a country house", ["To study abroad", "To pay debts", "To buy a car"], "전원주택."), M("What type of investment is Plan B?", "A fund", ["Installment savings", "Stocks", "Regular savings"], "펀드."), M("Why does Plan B’s writer like funds?", "An expert invests on her behalf", ["They are risk-free", "They have no fees", "They are short-term"], "전문가가 투자를 대신."), M("Which type is ‘free to deposit and withdraw, low interest’?", "보통예금", ["적금", "펀드", "주식"], "c."), M("Which type is ‘directly buy and sell securities’?", "주식 투자", ["펀드 투자", "적금", "부동산 투자"], "b."), M("Which type needs a lot of money and a long period?", "부동산 투자", ["보통예금", "펀드 투자", "적금"], "e."), M("Which type has an expert investing for you?", "펀드 투자", ["주식 투자", "적금", "보통예금"], "d."), M("Which type has a fixed monthly deposit and a lump sum at the end?", "적금", ["보통예금", "주식 투자", "부동산 투자"], "a."),
           F("그래서 ___을 들기로 했어요. (installment savings)", "적금", ["투자", "대출"], "적금."), F("펀드회사의 ___가 투자를 대신해 주니까 좋아요. (expert)", "전문가", ["고객", "직원"], "전문가."), F("주택적금은 주택___에서만 들 수 있다. (bank)", "은행", ["회사", "기관"], "주택은행."), F("펀드 투자는 ___를 지급해야 한다. (fee)", "수수료", ["이자", "세금"], "수수료."), F("부동산 투자는 ___ 투자이며 비교적 안정적이다. (long-term)", "장기", ["단기", "일정"], "장기."),
           read_q("유학준비를 위해 월급에서 일정금액을 모아 두고 싶습니다"), read_q("그래서 적금을 들기로 했어요"), read_q("펀드회사의 전문가가 투자를 대신해 주니까 좋아요"), read_q("주식 값이 떨어지면 손해를 볼 수 있다"), read_q("부동산 투자는 장기 투자입니다")]
    ),
)

# ================================================================== L11 Grammar B: -(으)려던 참이다
_RT1 = [("뭐 해?", "What are you doing?"), ("응, 아침을 먹으려던 참이었어.", "Uh, I was just about to eat breakfast.")]
_RT2 = [("아침을 먹으려던 참에 친구가 방문했다.", "When I was about to eat breakfast, a friend of mine visited (me)."), ("버스를 타려던 참에 친구를 만났어요.", "When I was about to get on the bus, I met a friend.")]
_RT3 = [("민호야, 같이 점심 먹자.", "Minho, let’s have lunch together."), ("그래. 나도 점심 먹으려던 참이었어.", "OK. I was about to have lunch, too."), ("김 일병, 이거 공책에 썼어요?", "PFC Kim, did you write in the notebook?"), ("지금 쓰려던 참이에요.", "I was just about to write."), ("엄마한테 전화했어?", "Did you call mom?"), ("아니. 막 전화하려는 참이었어.", "No. I was about to call her.")]
_RT4 = [("김 일병, 지금 뭐 해요?", "PFC Kim, what are you doing now?"), ("아침을 먹으려던 참이에요.", "I was just about to eat breakfast."), ("아침을 먹으려고 해요.", "I am about to eat breakfast.")]
_RTS = [("김 일병, 뭐 해?", "PFC Kim, what are you doing?"), ("지금 우체국에 가려던 참이야.", "I was just about to go to the post office."), ("나도 소포를 부치러 우체국에 가려던 참이었어.", "I was about to go to the post office to send a package, too."), ("그래? 내가 대신 부쳐 줄까?", "Really? Shall I send it for you?"), ("응. 고마워.", "Yes. Thanks.")]
_RTN = [("인희 씨, 제가 우체국에 가려던 참에 고향에서 친구가 왔어요.", "Inhui, just when I was about to go to the post office, a friend came from my hometown."), ("미안하지만 이 소포 좀 부쳐 주시겠어요?", "I am sorry, but could you send this package for me?"), ("나중에 커피 살게요.", "I will buy you coffee later."), ("진호 씨, 핸드폰을 하나 새로 장만하려던 참에 핸드폰을 선물로 주셨네요.", "Jinho, just when I was about to get a new cell phone, you gave me a cell phone as a gift."), ("고마워요. 잘 쓸게요.", "Thank you. I will use it well."), ("현수 씨, 적금을 들려고 하던 참에 현수 씨가 좋은 투자 상품을 소개해 주었어요.", "Hyunsu, just when I was going to open an installment savings account, you introduced me to a good investment product."), ("고마워요. 다음에도 좋은 조언 부탁 드릴게요.", "Thank you. I will ask you for good advice next time too.")]
_RMX = [("숙제를 하려던 참이에요.", "I was just about to do my homework."), ("지금 막 나가려던 참이었어요.", "I was just about to go out right now."), ("샤워를 하려던 참에 전화가 왔어요.", "Just when I was about to take a shower, a phone call came."), ("저녁을 준비하려던 참이에요.", "I am just about to prepare dinner."), ("자려던 참에 친구가 찾아왔어요.", "Just when I was about to go to sleep, a friend came to see me.")]
L11 = lesson(
    "Ch 45 · Grammar B: –(으)려던 참이다, I was just about to do something",
    "-(으)려던 참이다 · -(으)려던 참에 · 아침을 먹으려던 참이었어 · 우체국에 가려던 참에",
    requires=[],
    cards=[
        card("“I was just about to do something”",
             "In Korean, the grammar pattern –(으)려던 참이다 is used to convey the meaning of “I was just about (to do something).” For example (over the phone; the English is the book’s):",
             examples=passage(_RT1)),
        card("The tenses and the conjunctive ending",
             "–(으)려던 참이다, which comes from –(으)려고 하던 참이다, literally means “(It) is the moment I intended to do (something).” This grammar pattern can be expressed either in the present tense –(으)려던 참이다 or the past tense –(으)려던 참이었다, although the past tense version is used more often. On the other hand, when –(으)려던 참에 is a conjunctive ending, it can be translated as when I was about to do something or at the moment I intended to do something. For example (the English is the book’s):",
             examples=passage(_RT2)),
        card("The pattern",
             "Expressing “I was just about to do something”: action verb stem + (으)려던 참이다. More examples (the English is the book’s):",
             examples=passage(_RT3)),
        card("Follow-up 1 (Speaking): on the phone",
             "Partner A asks what Partner B is doing now. Partner B picks up a topic card and answers using the topic and either –(으)려던 참이다 or –(으)려고 하다. The book’s model (the English is mine):",
             examples=passage(_RT4)),
        card("Follow-up 3 (Reading): Miyoung’s sticky notes",
             "The following messages are sticky notes Miyoung (미영) left for her colleagues; the book asks you to fill in a table in English (note; what she was about to do; what happened). The notes are the book’s (the signatures “이미영” are dropped); the English is mine.",
             examples=passage(_RTN)),
        card("The table filled in (mine)", "",
             tables=[table(["Note", "What she was about to do (mine)", "What happened (mine)"], [["1", "Go to the post office", "A friend came from her hometown, so she asks Inhui to send her package"], ["2", "Buy a new cell phone", "Jinho gave her a cell phone as a gift"], ["3", "Open an installment savings account", "Hyunsu introduced her to a good investment product"]])]),
        card("Follow-up 4 (Speaking): a role-play model",
             "One partner makes a request and the other responds using –(으)려던 참이다 or –(으)려고 하다. The book’s model dialog (the book writes “가려던 참이야/가려고 해” and I use the first; the English is mine):",
             examples=passage(_RTS)),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_RMX)),
        card("Activities left out", "Follow-up 2 (watching a video clip from the sitcom 거침없이 하이킥 and writing what the person was about to do) is a video activity; the situation-card role-plays of Follow-up 4 are pair activities."),
    ],
    exercises=uniq(
        _tr(_RT1 + _RT2 + _RT3 + _RT4 + _RTS + _RTN + _RMX, k=3)
        + [M("What does –(으)려던 참이다 express?", "I was just about to do something", ["I want to do it", "I have done it", "I must do it"], "The book’s note."), M("Which tense is used more often?", "The past: –(으)려던 참이었다", ["The present", "The future", "They are equal"], "The book’s note."), M("What does –(으)려던 참에 mean as a conjunctive ending?", "when I was about to do something", ["after I did it", "because I did it", "if I do it"], "The book’s note."), M("What does it come from?", "–(으)려고 하던 참이다", ["–(으)ㄹ 참이다", "–(으)ㄹ까 하다", "–고 싶던 참이다"], "The book’s note."), M("What does 아침을 먹으려던 참이었어 mean?", "I was just about to eat breakfast", ["I ate breakfast", "I will skip breakfast", "I want breakfast"], "The book’s example."), M("What does 버스를 타려던 참에 친구를 만났어요 mean?", "When I was about to get on the bus, I met a friend", ["I met a friend on the bus", "I missed the bus", "I will take the bus"], "The book’s example."), M("Why did Miyoung ask Inhui to send her package?", "A friend came from her hometown just as she was about to go", ["She was sick", "She was on vacation", "She had no stamps"], "고향에서 친구가 왔어요."), M("What did Miyoung thank Hyunsu for?", "Introducing a good investment product", ["A gift", "A coffee", "A ride"], "투자 상품."),
           F("응, 아침을 먹___ 참이었어. (was about to)", "으려던", ["으려는", "은"], "–(으)려던 참."), F("지금 쓰___ 참이에요. (was about to write)", "려던", ["는", "은"], "쓰려던."), F("버스를 타려던 ___ 친구를 만났어요. (just when)", "참에", ["참을", "참이"], "–(으)려던 참에."), F("나도 점심 먹으려던 참이___. (was)", "었어", ["어", "야"], "참이었어."), F("엄마한테 전화하___ 참이었어. (was about to)", "려던", ["는", "고"], "전화하려던 참."),
           read_q("아침을 먹으려던 참이었어"), read_q("지금 쓰려던 참이에요"), read_q("막 전화하려던 참이었어"), read_q("버스를 타려던 참에 친구를 만났어요"), read_q("우체국에 가려던 참에 고향에서 친구가 왔어요")]
    ),
)


# ================================================================== L12 Activities + self-evaluation
_OP = [("저는 잠을 푹 잤는데도 피곤해요.", "I am tired even though I slept well."), ("값이 비싼데도 잘 팔려요.", "It sells well even though the price is expensive."), ("주말인데도 일을 해야 해요.", "I have to work even though it is the weekend."), ("지금 막 투자 상담을 받으려던 참이에요.", "I was just about to get investment advice right now."), ("은행에 가려던 참에 비가 왔어요.", "Just when I was about to go to the bank, it rained.")]
L12 = lesson(
    "Ch 45 · Activities and self-evaluation",
    "경제 · 무역 · 투자 · 자기 평가 · 연습 문장",
    requires=[],
    cards=[
        card("More practice sentences (mine)", "Sample sentences of my own that combine the chapter’s grammar with its vocabulary (the English is mine):", examples=passage(_OP)),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so that they can provide other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and discuss sectors of the Korean economy including the gross domestic product (GDP), economic growth rate, trade volume, trading partners, etc.; identify and discuss major types of financial investments and their characteristics; and read and say large numbers in Korean.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; ~에도 (불구하고) or –(으)ㄴ/는데도 (불구하고) (in spite of; despite); –(으)려던 참이다 (I was just about to do something); and the Sino-Korean syllables within 조선업 (造船業), 약세 (弱勢), 하락 (下落), 급감 (急減), and 장단점 (長短點)."),
        card("Activities left out", "The chapter’s Activities pages (the sector and investment readings are in the earlier lessons) also hold SMART Board activities, listening activities (country economies, trade news, investment news, callers seeking financial advice) and pair or group writing and speaking tasks. They are audio, computer and group activities and are left out."),
    ],
    exercises=uniq(
        _tr(_OP, k=3)
        + [M("What should you do if you tick “No” in the self-evaluation?", "Review on your own, study with a partner, tell your advisor or team leader", ["Skip it", "Retake the course", "Nothing"], "The book’s advice."), M("What does 값이 비싼데도 잘 팔려요 mean?", "It sells well even though the price is expensive", ["It sells because it is cheap", "It does not sell", "It is cheap"], "-는데도."), M("What does 은행에 가려던 참에 비가 왔어요 mean?", "Just when I was about to go to the bank, it rained", ["I went to the bank in the rain", "It rained after the bank", "I did not go"], "-(으)려던 참에."),
           F("저는 잠을 푹 잤___ 피곤해요. (even though)", "는데도", ["으니까", "으면"], "-는데도."), F("주말___ 일을 해야 해요. (even though it is the weekend)", "인데도", ["이니까", "이라서"], "-인데도."), F("지금 막 투자 상담을 받으___ 참이에요. (about to)", "려던", ["는", "은"], "-(으)려던 참."),
           read_q("저는 잠을 푹 잤는데도 피곤해요"), read_q("값이 비싼데도 잘 팔려요"), read_q("주말인데도 일을 해야 해요"), read_q("지금 막 투자 상담을 받으려던 참이에요"), read_q("은행에 가려던 참에 비가 왔어요")]
    ),
)

# ================================================================== L13 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0] and "…" not in r[0] and "–" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 45 · Core vocabulary",
    "주요 단어 · 경제 · 무역 · 투자 · 불구하고 · 참이다",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. The Loan Words section repeats 로봇 and 펀드, which I list once. The last section lists the Sino-Korean related words of 조선업, 약세, 하락, 급감 and 장단점 as the book gives them.\n\n"
             "The example sentences with digits and letters are respelled in Hangul (70년대 → 칠십 년대; 1조 5000억 원 → 일 조 오천억 원; LG전자 → 엘지전자; 16-17세 → 열여섯 살에서 열일곱 살; 1인당 → 일인당; the book’s key 1인당 is written 일인당)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 흑자 mean?", "a surplus", ["a deficit", "a boom", "a recession"], "黑字."), M("What does 적자 mean?", "a deficit", ["a surplus", "a boom", "a profit"], "赤字."), M("What does 호황 mean?", "an economic boom", ["a recession", "a deficit", "a surplus"], "好況."), M("What does 불황 mean?", "an economic recession", ["a boom", "a surplus", "a trend"], "不況."), M("What does 수요 mean?", "demand", ["supply", "income", "interest"], "需要."), M("What does 손해 mean?", "a financial loss", ["a profit", "a fee", "an account"], "損害."), M("What does 만기 mean?", "maturity; expiration", ["a start", "a fee", "an amount"], "滿期."), M("What does 추세 mean?", "a trend", ["a level", "a share", "a structure"], "趨勢."),
           F("지난해 우리나라의 무역수지는 ___를 기록했습니다. (surplus)", "흑자", ["적자", "호황"], "흑자."), F("매달 월급에서 십만 원씩 ___에 들어갑니다. (installment savings)", "적금", ["통장", "계좌"], "적금."), F("우체국 ___을 만들어 두면 편리할 때가 많습니다. (bankbook)", "통장", ["계좌", "금액"], "통장."), F("신용카드를 쓸 때는 ___를 내야 합니다. (fee)", "수수료", ["이율", "만기"], "수수료."), F("요즘은 부동산에 투자하는 ___입니다. (trend)", "추세", ["수준", "구조"], "추세."),
           read_q("주요 단어"), read_q("흑자"), read_q("적자"), read_q("통장"), read_q("추세")]
    ),
)

UNIT = unit("Semester 2 · Unit 12 · Chapter 45: Economy (경제)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])
