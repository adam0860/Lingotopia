"""Unit 54: KBC Semester 2, Unit 12, Chapter 47 - Social Issues I (사회 문제 1).
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

# ---- the core vocabulary of Chapter 47 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("가치(관)", "(價値(觀)) values; (one’s) sense of values; “view of value”", "시대에 따라 가치관이 달라집니다."),
    ("개설", "(開設) opening; establishing (to open; to establish/to be opened; to be established) (~하다/되다)", "최근 한국어 수업을 개설하는 외국 대학이 늘고 있습니다."),
    ("경쟁력", "(競爭力) competitiveness; competitive edge; “competition power”", "연구개발 투자는 기업의 경쟁력을 높여 줍니다."),
    ("꼴찌", "the last (in ranking); the bottom", "저는 학교에서 체육은 꼴찌였지만, 영어는 항상 일등이었습니다."),
    ("무상", "(無償) free of charge; without cost; “without repaying”", "유럽에서는 국민들이 무상으로 고등교육을 받을 수 있습니다."),
    ("미혼", "(未婚) single; unmarried; “not married”", "이십 대 삼십 대 젊은 미혼 남녀를 대상으로 설문조사를 실시했습니다."),
    ("배려", "(配慮) consideration; care (to be considerate; to care [about]) (~하다)", "저는 남을 잘 배려해 주는 사람이 좋습니다."),
    ("배우자", "(配偶者) a spouse", "요즘은 인터넷에서 배우자를 찾는 미혼 남녀들이 늘고 있습니다."),
    ("보육", "(保育) childcare; “preserving and bringing up” (to take care of children) (~하다)", "정부에서 운영하는 보육 시설이 맞벌이 부부에게 인기가 있습니다."),
    ("생산성", "(生産性) productivity", "기계가 인간의 노동을 대신하면서 생산성이 높아졌습니다."),
    ("설문조사", "(說問調査) a survey", "저희 회사는 오는 이십 일부터 온라인 설문조사를 실시합니다. 많은 참여 부탁 드립니다."),
    ("약하다", "(弱) to be weak; to be feeble; to be light", "저는 어렸을 때부터 몸이 약해서 병원에 자주 입원했습니다."),
    ("유급", "(有給) paid", "일 년 중 유급휴가가 며칠이나 됩니까?"),
    ("유도", "(誘導) an inducement (to induce/to be induced) (~하다/되다)", "학생이 공부를 열심히 할 수 있도록 분위기를 유도했습니다."),
    ("잠재력", "(潛在力) potential; potentiality; “potential power”", "저는 아이의 잠재력을 개발하기 위해 책을 많이 읽어 주고 있습니다."),
    ("전액", "(全額) full amount (of money); total amount", "성적이 좋은 학생들에게는 학비 전액을 지원할 계획입니다."),
    ("제시", "(提示) suggestion; proposal; presentation; showing (to suggest; to propose/to be suggested; to be proposed) (~하다/되다)", "정부가 제시한 경제정책에 문제점이 많습니다."),
    ("지속적", "(持續的) continuous", "환경을 보호하기 위해 지속적인 노력이 필요합니다."),
    ("짝", "a pair; a mate", "제 아들이 아직 미혼인데 좋은 짝을 만나면 좋겠습니다."),
    ("출산", "(出産) childbirth; delivery (of a child) (to give birth) (~하다)", "아이 출산 예정일이 언제입니까?"),
    ("취학", "(就學) enrollment in school; entering school (to enroll in school/to enroll someone in school) (~하다/시키다)", "한국에서 초등학교 취학연령이 몇 살입니까? 한국의 중고등학교 취학률은 대단히 높은 편이다."),
    ("혜택", "(惠澤) a benefit", "친환경 소재를 사용해서 집을 지으면 세금혜택이 있습니다."),
    ("확대", "(擴大) expansion; enlargement (to expand/to be expanded; to be enlarged) (~하다/되다)", "오늘 사진관에 가서 이 사진을 확대해야겠어요."),
]
_CV_B = [
    ("견디다", "to endure; to bear", "몸이 아파서 견디기가 힘들어요."),
    ("기러기", "a wild goose", "저는 아이를 캐나다에서 공부시키기 위해서 기러기 아빠가 되었습니다."),
    ("기준", "(基準) standards; criteria", "한국어 몰입교육 대상을 뽑는 기준이 무엇입니까?"),
    ("끼니", "a meal", "북한에는 끼니를 거르는 사람들이 많습니다."),
    ("떨어지다", "to be (physically) separated", "우리 형은 서울에서 직장생활을 하기 때문에 가족과 떨어져서 지냅니다."),
    ("무시", "(無視) disregard; neglect; “without seeing” (to disregard; to neglect; to ignore) (~하다)", "신호를 무시하고 달리던 차가 사고를 냈습니다."),
    ("사례", "(事例) an example", "우리 학교에서도 문제학생이 다른 학생의 돈을 빼앗은 사례가 있었습니다."),
    ("송금", "(送金) remittance; “sending money” (to wire or send money) (~하다)", "오늘 오전에 은행에 가서 부모님께 송금을 했습니다."),
    ("실망", "(失望) disappointment; “losing hope” (to be disappointed) (~하다)", "수학시험 성적이 나빠 대단히 실망을 했습니다."),
    ("실제(로)", "(實際) in reality; actually", "그 남자는 실제로 키가 아주 컸습니다."),
    ("열풍", "(烈風) a fever; a frenzy; fever pitch; bandwagon", "요즘 태국에 한국 드라마 열풍이 불고 있습니다."),
    ("원어민", "(原語民) a native speaker; “original language person”", "강원도지역 학교에는 원어민 영어교사가 부족합니다."),
    ("이별", "(離別) a parting; a farewell (to part) (~하다)", "모든 만남은 이별의 시작입니다."),
    ("입시", "(入試) an entrance examination", "서울시에서는 입시가 끝난 학생들을 위해 문화공연을 마련했습니다."),
    ("전담", "(專擔) being in full charge; “exclusively carrying (a burden on the shoulders)” (to be in full charge; to be in exclusive charge) (~하다)", "경찰서마다 학교폭력을 전담하는 부서가 설치됐습니다."),
    ("조기", "(早期) early (period)", "암은 조기에 발견하는 것이 중요합니다."),
    ("중(요)시하다", "(重(要)視) to put emphasis on; to put importance on; to lay stress on", "요즘은 회사에서 채용을 할 때 면접을 중시합니다."),
    ("평가", "(評價) evaluation (to evaluate/to be evaluated) (~하다/받다)", "이번 시험은 학생들의 영어회화 능력을 평가합니다."),
    ("헤어지다", "to part; to break up (with someone)", "어제 여자 친구와 헤어졌습니다."),
]
_CV_C = [
    ("가계", "(家計) a household budget; “household counting”", "경제가 좋지 않아서 가계 지출도 줄어들고 있습니다."),
    ("가득", "fully (to be full; to be filled up) (~하다)", "먼 길을 가야 돼서 차에 기름을 가득 채웠어요."),
    ("과소비", "(過消費) excessive spending; overspending (to spend excessively; to overspend) (~하다)", "일부 부유층의 과소비가 사회문제가 되고 있습니다."),
    ("과시", "(誇示) showing off (to show off) (~하다)", "중국이 첨단 신무기 개발로 군사력을 과시하고 있다."),
    ("과시욕", "(誇示慾) a desire for showing off", "일부 사람들은 남에게 보이고 싶은 과시욕 때문에 비싼 물건을 삽니다."),
    ("관계", "(關係) a relation; connection", "김 대리는 동료들과 관계가 좋아요."),
    ("낭비", "(浪費) waste; squandering (to waste; to squander) (~하다)", "뷔페에서는 접시에 먹을 수 있는 만큼만 덜어야 음식 낭비를 막을 수 있다."),
    ("만연", "(蔓延) rampancy (to be rampant) (~하다/되다)", "이런 과소비 문화는 세대에 관계없이 사회 전체에 만연돼 있습니다."),
    ("매출", "(賣出) sales; “selling out”", "백화점 매출이 지난해보다 십오 퍼센트 증가했습니다."),
    ("무분별", "(無分別) indiscretion; imprudence; recklessness (to be indiscreet; to be imprudent; to be reckless) (~하다)", "자녀들이 무분별하게 컴퓨터를 오래 사용하지 않도록 하세요."),
    ("반영", "(反映) reflection (to reflect/to be reflected) (~하다/되다)", "이번 채용결정에는 면접시험결과도 반영됩니다."),
    ("부유층", "(富裕層) the rich; the upper class; the haves", "저희 삼촌 댁은 부유층이라 돈도 잘 쓰시고 여행도 자주 다니세요."),
    ("브랜드", "a brand; a make", "제가 좋아하는 가방 브랜드는 샤넬이에요."),
    ("사치", "(奢侈) a luxury; an extravagance (to be luxurious; to be extravagant) (~하다)", "사치한 생활을 즐기면 돈을 모을 수 없어요."),
    ("성별", "(性別) gender; sex", "이력서에 성별도 쓰셔야 합니다."),
    ("심지어", "even; what’s worse", "어제부터 갑자기 추워지더니 오늘은 심지어 눈까지 오네요."),
    ("심화", "(深化) deepening (to deepen; to intensify/to be deepened; to be intensified) (~시키다/되다)", "북한과 중국은 경제협력 심화를 위해 서로 노력하기로 했습니다."),
    ("애용", "(愛用) habitual/frequent use (of a certain item because you like it); “love using” (to use favorably) (~하다)", "저는 화장품은 외국 제품을 애용해요."),
    ("약화", "(弱化) weakening (to weaken/to be weakened) (~시키다/되다)", "독감에 걸린 이후로 체력이 많이 약화되었어요."),
    ("~ 정도", "(程度) degree; limit", "이 정도의 일은 별로 힘들지 않아요."),
    ("채우다", "to fill (in); to pack", "컵마다 물을 다 채웠어요."),
]
_CV_GR = [
    ("an attributive form + 것처럼/같이", "just like; as if (see Grammar in Focus)", "친구는 아주 멀리 가는 사람처럼 슬픈 얼굴로 나를 찾아 왔어요."),
    ("loanwords", "see Grammar in Focus", "라디오, 컴퓨터, 패션, 브랜드, 월드컵, 올림픽"),
]
_CV_SINO = [("저출산", "(低出産) low birthrate", "저온, 고저, 저체중, 외출, 출국, 출구, 생산, 산지, 농산물"), ("전담", "(專擔) exclusive charge", "전력, 전임, 전용, 담당, 담임교사, 부담"), ("명품 선호", "(名品 選好) a preference for famous name-brand merchandise", "유명, 명소, 무명, 상품, 식품, 기념품, 선택, 선수, 선발, 호황, 호인, 호평")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"가치관": "values", "출산율": "birthrate", "조기유학": "early study abroad", "기러기 아빠": "a wild goose daddy", "명품": "a famous name-brand item", "선호": "preference", "저출산": "low birthrate", "외래어": "a loanword"}
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
_S1G = [("저개발", "underdevelopment; “low development”"), ("저속", "low speed"), ("저임금", "low wages"), ("저혈압", "hypotension; “low blood pressure”"), ("출국", "leaving a country"), ("출항", "leaving a port; sailing"), ("초산", "one’s first childbirth")]
_S1 = [("저온", "low temperature"), ("생산", "production"), ("저체중", "low body weight"), ("농산물", "agricultural products"), ("외출", "going out"), ("고저", "high and low"), ("산지", "a place of production"), ("출구", "an exit")]
_S2G = [("전문가", "a specialist")]
_S2 = [("전용", "exclusive use"), ("전력", "all one’s strength"), ("전임", "full-time (post)"), ("담임 선생님", "a homeroom teacher"), ("부담", "a burden"), ("담당", "being in charge")]
_S3G = [("성명", "one’s full name"), ("명함", "a business card; “name holder”"), ("익명", "anonymous; “hidden name”"), ("무명", "unknown; obscure; “without name”"), ("식품", "food; “eating item”"), ("공산품", "industrial products"), ("선물", "a gift; a present; “selected item”"), ("선거", "an election"), ("호의", "goodwill; kindness"), ("호감", "an attraction; “favorable feeling”")]
_S3 = [("유명", "famous"), ("호황", "an economic boom"), ("선택", "choice; selection"), ("상품", "merchandise; a product"), ("기념품", "a souvenir"), ("명소", "a famous place"), ("호평", "a favorable review"), ("선발", "selection (of people)")]

L1 = lesson(
    "Ch 47 · What the chapter teaches, 저출산 · 전담 · 명품 선호",
    "사회 문제 · 저출산 · 전담 · 명품 선호 · 低出産 · 專擔 · 名品 選好 · 것처럼 · 외래어",
    requires=[],
    cards=[
        card("What Chapter 47 teaches (사회 문제 1)",
             "Chapter 47, “Social Issues I”, has a vocabulary builder, three topic presentations (Busan’s measures against the low birthrate, a “goose daddy”, the excessive preference for name brands) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss the low birthrate trend in Korea, its causes and effects, and incentives for reversing it; identify and discuss the trend of young Koreans studying abroad; and understand and discuss the trend of people preferring famous name-brand merchandise and how the trend has affected the Korean economy.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; an attributive form + 것처럼/같이 (like; as if); loanwords in Korean; and the Sino-Korean syllables within 저출산 (低出産), 전담 (專擔), and 명품 선호 (名品 選好)."),
        card("Sino-Korean in use: 저출산 (低出産)",
             "The first syllable 저 (低) means low, and when it is placed in front of a word, it functions like the English prefix under- or hypo-, as in 저개발 (underdevelopment; “low development”), 저속(도) (low speed), 저임금 (low wages), 저혈압 (hypotension; “low blood pressure”), etc. Thus the word 저출산 means low birthrate or low delivery rates (of children). The noun 출산 itself means delivery (of a baby) or childbirth; the syllable 출 (出) means (come/go) out or leaving, as in 출국 and 출항. The syllable 산 (産) means produce or give a birth, as in 초산 (one’s first childbirth). Thus, the literal meaning of 저출산 is “low (child) producing” or “low childbirth.” The book asks you to guess 저온, 생산, 저체중, 농산물, 외출, 고저, 산지 and 출구 (my answers; the glosses of the book’s examples 출국, 출항 and 저속 are mine):",
             tables=[ktable(_S1G), ktable(_S1)]),
        card("Sino-Korean in use: 전담 (專擔)",
             "The syllable 전 (專) means only, exclusive, or specialized, as in 전문가 (a specialist). The syllable 담 (擔) means carrying (a burden) on the shoulder. Thus the literal meaning of the Sino-Korean word is “exclusively carrying (a burden) on the shoulder,” and the word means (being in) exclusive charge or complete charge. The verb 전담하다, which derives from the word 전담, means to be in complete charge or to be in exclusive charge. The book asks you to guess 전용, 전력, 전임, 담임 선생님, 부담 and 담당 (my answers):",
             tables=[ktable(_S2G), ktable(_S2)]),
        card("Sino-Korean in use: 명품 선호 (名品 選好)",
             "This Sino-Korean word is made up of the two words, 명품 (name brand) and 선호 (preference). Thus 명품 선호 means a preference for name-brand merchandise. The first syllable 명 (名) means a name, as in 성명 (one’s full name) and 명함 (a business card; “name holder”), 익명 (anonymous; “hidden name”), 무명 (unknown; obscure; “without name”), etc. The syllable 품 (品) means item or goods, as in 식품 (food; “eating item”) and 공산품 (industrial products). 선 (選) means select or selective, as in 선물 (a gift; a present; “selected item”) and 선거 (an election). The last syllable 호 (好), whose Chinese character depicts a woman (女) holding her son (子), means good or like or likable, as in 호의 (goodwill; kindness) and 호감 (an attraction; “favorable feeling”). The book asks you to guess 유명, 호황, 선택, 상품, 기념품, 명소, 호평 and 선발 (the book glosses 평 [評]: evaluation; my answers):",
             tables=[ktable(_S3G), ktable(_S3)]),
    ],
    exercises=uniq(
        _tr(_S1G + _S1 + _S2G + _S2 + _S3G + _S3, k=3)
        + [M("What does 저 (低) mean?", "low", ["high", "out", "produce"], "저온."), M("What does 출 (出) mean?", "(come/go) out; leaving", ["low", "produce", "only"], "출국."), M("What does 산 (産) mean?", "produce; give birth", ["out", "low", "name"], "초산."), M("What does 전 (專) mean?", "only; exclusive; specialized", ["low", "name", "good"], "전문가."), M("What does 담 (擔) mean?", "carrying (a burden) on the shoulder", ["select", "goods", "only"], "부담."), M("What does 명 (名) mean?", "a name", ["goods", "select", "good"], "성명."), M("What does 품 (品) mean?", "item; goods", ["name", "select", "low"], "식품."), M("What does 선 (選) mean?", "select; selective", ["goods", "name", "exclusive"], "선택."), M("What does 호 (好) mean?", "good; like; likable", ["goods", "select", "low"], "호감."), M("What is the literal meaning of 저출산?", "“low (child) producing” or “low childbirth”", ["“exclusively carrying a burden”", "“preference for name brands”", "“early childbirth”"], "저 + 출 + 산."), M("What is the literal meaning of 전담?", "“exclusively carrying (a burden) on the shoulder”", ["“low childbirth”", "“selected item”", "“hidden name”"], "전 + 담."), M("What does 명품 선호 mean?", "a preference for name-brand merchandise", ["low birthrate", "exclusive charge", "an early stage"], "명품 + 선호."),
           F("저___도는 낮은 속도를 말합니다. (low)", "속", ["산", "담"], "저속."), F("___국은 나라를 떠나는 것입니다. (leaving)", "출", ["산", "저"], "출국."), F("식___은 먹는 물건입니다. (food)", "품", ["명", "호"], "식품."), F("유___한 가수의 공연이 열립니다. (famous)", "명", ["품", "산"], "유명."), F("호___은 좋게 하는 평가입니다. (favorable review)", "평", ["감", "황"], "호평."),
           read_q("저출산"), read_q("전담"), read_q("명품 선호"), read_q("담당"), read_q("기념품")]
    ),
)

# ================================================================== L2 Vocabulary builder
_VB1 = [("전액", "whole amount of money", "total amount; the sum"), ("무상", "without reward; “pay off”", "free of charge"), ("송금", "send money", "remittance; sending money"), ("입시", "enter (school) exam/test", "an entrance exam"), ("전담", "exclusive responsibility", "exclusive charge/responsibility"), ("조기", "early period", "an early stage/period"), ("실망", "lose hope", "disappointment")]
_VB2 = [("이별", "leave and separate", "parting; separation"), ("애용", "love to use", "using favorably"), ("낭비", "wasteful spending", "waste; squander"), ("성별", "sex/gender separation", "(by) sex/gender"), ("가계", "house count", "household budget"), ("약화", "weak change/-ization", "weaken"), ("미혼", "not (yet) marriage", "single; unmarried")]
_VB3 = [("저출산", "low birth", "low birthrate"), ("생산성", "producing characteristics", "productivity"), ("잠재력", "potential power", "potential (ability)"), ("경쟁력", "competing power", "competitiveness"), ("가치관", "value view", "values (of life)"), ("원어민", "original language people", "a native speaker")]
L2 = lesson(
    "Ch 47 · Vocabulary Builder: words and their literal meanings",
    "전액 · 무상 · 송금 · 입시 · 전담 · 조기 · 실망 · 이별 · 애용 · 낭비 · 성별 · 가계 · 약화 · 미혼 · 저출산 · 생산성 · 잠재력 · 경쟁력 · 가치관 · 원어민",
    requires=[],
    cards=[
        card("새 단어 a: match the words, their literal meanings and their English meanings",
             "The following words are some of the core vocabulary you will learn in Chapter 47. The book asks you to match each word with its literal meaning and then the literal meaning with its English meaning (three tables of words). The pairs are the book’s two lists; the matches are mine to confirm from the literal meanings.",
             tables=[table(["Word", "Literal meaning", "English meaning"], [list(r) for r in _VB1], say=[0]), table(["Word", "Literal meaning", "English meaning"], [list(r) for r in _VB2], say=[0]), table(["Word", "Literal meaning", "English meaning"], [list(r) for r in _VB3], say=[0])]),
        card("Activities left out", "The book’s step b (compare with your neighbor and check with the teacher), Activities 1, 2 and 3 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 4 (the “Peril!” game, started by the teacher with a PowerPoint) are computer and game activities."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _VB1 + _VB2 + _VB3], k=3)
        + [M("What is the literal meaning of 송금?", "send money", ["lose hope", "early period", "enter exam"], "送金."), M("What is the literal meaning of 실망?", "lose hope", ["send money", "whole amount", "exclusive"], "失望."), M("What is the literal meaning of 조기?", "early period", ["lose hope", "send money", "pay off"], "早期."), M("What is the literal meaning of 입시?", "enter (school) exam/test", ["early period", "send money", "pay off"], "入試."), M("What is the literal meaning of 미혼?", "not (yet) marriage", ["leave and separate", "house count", "love to use"], "未婚."), M("What is the literal meaning of 가계?", "house count", ["not yet marriage", "wasteful spending", "weak change"], "家計."), M("What is the literal meaning of 낭비?", "wasteful spending", ["house count", "love to use", "leave and separate"], "浪費."), M("What is the literal meaning of 잠재력?", "potential power", ["competing power", "value view", "low birth"], "潛在力."), M("What is the literal meaning of 경쟁력?", "competing power", ["potential power", "value view", "producing characteristics"], "競爭力."), M("What is the literal meaning of 가치관?", "value view", ["competing power", "potential power", "original language people"], "價値觀."), M("What is the literal meaning of 원어민?", "original language people", ["value view", "low birth", "producing characteristics"], "原語民."), M("What is the literal meaning of 생산성?", "producing characteristics", ["potential power", "competing power", "low birth"], "生産性."),
           F("부모님께 은행에서 ___을 했습니다. (remittance)", "송금", ["입시", "낭비"], "송금."), F("대학 ___를 준비하느라 바쁩니다. (entrance exam)", "입시", ["송금", "전액"], "입시."), F("학비 ___을 지원해 준다고 합니다. (the full amount)", "전액", ["가계", "미혼"], "전액."), F("음식 ___를 줄여야 합니다. (waste)", "낭비", ["애용", "이별"], "낭비."), F("이 도시는 ___ 남녀가 많습니다. (single)", "미혼", ["기혼", "성별"], "미혼."),
           read_q("전액"), read_q("무상"), read_q("송금"), read_q("입시"), read_q("가치관")]
    ),
)


# ================================================================== L3 Topic A
_A_TXT = [
    ("지난 이천팔 년 기준으로 부산의 출산율은 영 점 구팔 명으로 전국 광역 지자체 가운데 꼴찌를 기록했습니다.", "As of 2008, Busan’s birthrate was 0.98 per woman, recording the last place among the metropolitan local governments nationwide."),
    ("안삼달 부산시 여성정책 담당", "An Sam-dal, in charge of women’s policy at the city of Busan (the interview)"),
    ("지속적으로 인구가 감소하게 되면 생산성이 떨어지게 되고 결국 생산성이 떨어지면 경제 잠재력이 약해지고 그다음 국가 경쟁력이 떨어지게 됩니다.", "If the population continues to decrease, productivity will fall, and in the end, if productivity falls, economic potential weakens and then national competitiveness falls."),
    ("출산율 하락의 원인은 미혼율 상승입니다.", "The cause of the fall in the birthrate is the rise in the rate of unmarried people."),
    ("부산시는 우선 지역 내 미혼 남녀들이 원하는 짝을 만날 수 있는 기회를 제공할 계획입니다.", "The city of Busan plans first to provide an opportunity for unmarried men and women in the area to meet the partner they want."),
    ("또, 결혼과 출산에 대한 젊은이들의 가치관을 변화시키기 위해 지역 대학에서 관련 교양과목을 개설하기로 했습니다.", "Also, in order to change young people’s values about marriage and childbirth, it decided to open related general-education courses at local universities."),
    ("이미 부산시는 둘째 이후 자녀에게는 취학 전까지 보육료 전액을 지원하고 셋째 이후 자녀에게는 보육료뿐만 아니라 초, 중, 고 무상교육과 대학 첫 등록금까지 지원하는 등 적극적인 출산 유도 정책을 제시하고 있습니다.", "Busan has already been presenting active childbirth-inducing policies, such as supporting the full childcare fee until school age for a second and later child, and supporting for a third and later child not only the childcare fee but also free elementary, middle and high school education and even the first university tuition."),
]
_A_WORDS = ["가치(관)", "개설", "경쟁력", "꼴찌", "무상", "미혼", "배려", "배우자", "보육", "생산성", "설문조사", "약하다", "유급", "유도", "잠재력", "전액", "제시", "지속적", "짝", "출산", "취학", "혜택", "확대"]
_RYEOK = [("노동력", "labor force"), ("경쟁력", "competitive edge; competitive power"), ("기억력", "memory; memory power"), ("생활력", "ability to maintain one’s livelihood"), ("생산력", "productivity; “production power”"), ("잠재력", "potentiality; “latent power”")]
_SLOG = [("적게 낳아 잘 기르면 부모 좋고 자식 좋다.", "The fewer children, the better for parents and children."), ("아들 딸 구별 말고 둘만 낳아 잘 기르자.", "Son or daughter, let’s have just two and raise them well."), ("아빠, 혼자는 싫어요. 엄마, 동생을 갖고 싶어요.", "Dad, I don’t want to be alone. Mom, I want to have a sibling.")]
L3 = lesson(
    "Ch 47 · Topic A: Busan’s measures against the low birthrate (부산시 저출산 대책)",
    "부산시 저출산 대책 · 출산율 · 미혼율 · 보육료 · 무상교육 · 잠재력 · 경쟁력 · 력 (力) · 가족계획",
    requires=[],
    cards=[
        card("Topic A: Busan’s measures against the low birthrate (부산시 저출산 대책)",
             "The following excerpt is from a news report (YTN) about efforts by the city of Busan to reverse the low birthrate. (The English is mine; the book gives none. The text is the book’s with the numbers spelled out: 2008년 is 이천팔 년, 0.98명 is 영 점 구팔 명, 초.중.고 is written with commas. The line with the interviewee’s name is the caption of the interview; the news screenshot overlaps one line of the printed text, so the words around “미혼 남녀들이” are as far as the Korean can be read. The book’s footnotes: 1 기준 means standards, criteria, or basis; the phrase ~을/를 기준으로 means [something] as a basis for or on the basis of [something]. 2 광역시 refers to a city with a population of 1 million or more; 지자체 is an acronym of 지방자치단체, which refers to a local [autonomous] government; thus 광역지자체 refers to local [autonomous] government within 광역시.)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_A_WORDS)),
        card("한국어에는: 력 (力)",
             "The Sino-Korean syllable 력 (力), which means power or ability, is often attached to other Sino-Korean nouns, as in 노동력 (labor force), 경쟁력 (competitive edge; competitive power), 기억력 (memory; memory power), 생활력 (ability to maintain one’s livelihood), 생산력 (productivity; “production power”), 잠재력 (potentiality; “latent power”), etc.",
             tables=[ktable(_RYEOK)]),
        card("한국에서는: Korea’s birthrate and policy changes",
             "In the early 1950s, Korea’s birthrate exceeded six children per woman. In 1962, the Korean government started its national family planning campaign known as 가족계획 to reduce the birthrate. The motto of the campaign was 적게 낳아 잘 기르면 부모 좋고 자식 좋다. (The fewer children, the better for parents and children.) The program aimed to reduce the birthrate to three children per woman. In the 1970s, the campaign for having only three children turned into a campaign for having only two. The motto of the campaign changed to 아들 딸 구별 말고 둘만 낳아 잘 기르자. (Son or daughter, let’s have just two and raise them well.) In the 1980s, a two-child family was considered too big. Because of the continued low birthrate (a historically low rate of 1.08 children per woman in 2005), the Korean government launched a very different campaign. It is now encouraging each household to have more children. The motto of the campaign is 아빠, 혼자는 싫어요. 엄마, 동생을 갖고 싶어요. (Dad, I don’t want to be alone. Mom, I want to have a sibling.) The Korean government has implemented various policies to increase the birthrate, such as providing financial incentives for having more than one child.",
             examples=passage(_SLOG)),
        card("Presentation step c: the table filled in (mine)",
             "The book asks you to use Topic A to fill in a table in English (the effects of continued low birthrate, the causes of low birthrate, the measures for increasing the birthrate). My answers from the news report:",
             tables=[table(["Effects of continued low birthrate", "Causes of low birthrate", "Measures for increasing the birthrate"], [["The population keeps decreasing; productivity falls; economic potential weakens; national competitiveness falls", "A rising rate of unmarried people", "Giving unmarried men and women chances to meet a partner; opening university courses to change young people’s values about marriage and childbirth; paying the full childcare fee until school age for a second child and later; for a third child and later also free elementary to high school education and the first university tuition"]])]),
        card("Activities left out", "Presentation steps a and b (the teacher starts a PowerPoint; listening to the topic) and d (review with the teacher) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT, k=3) + _tr(_RYEOK + _SLOG, k=3)
        + [M("What place did Busan’s birthrate record in 2008?", "The last among the metropolitan local governments", ["The first", "The middle", "The second"], "꼴찌."), M("What is the cause of the fall in the birthrate according to the report?", "A rise in the rate of unmarried people", ["Rising prices", "War", "A rise in marriage"], "미혼율 상승."), M("What happens if the population continues to decrease?", "Productivity falls", ["Productivity rises", "Prices fall", "Nothing"], "생산성이 떨어지게 된다."), M("What does Busan plan to provide for unmarried men and women?", "An opportunity to meet the partner they want", ["A house", "A job", "A car"], "짝을 만날 수 있는 기회."), M("What will local universities open?", "Related general-education courses", ["New dormitories", "A hospital", "A ministry"], "교양과목."), M("For a second child, what does Busan pay until school age?", "The full childcare fee", ["Nothing", "Half the tuition", "A house"], "보육료 전액."), M("For a third child, what is free?", "Elementary, middle and high school education", ["Only kindergarten", "Only meals", "Nothing"], "무상교육."), M("What does 력 (力) mean?", "power; ability", ["love", "year", "road"], "노동력."), M("What did the 1962 campaign called 가족계획 aim at?", "Reducing the birthrate", ["Raising the birthrate", "Raising taxes", "Building schools"], "The book’s note."), M("What does the present campaign encourage?", "Each household to have more children", ["Having no children", "Having two children only", "Having only sons"], "The book’s note."),
           F("부산의 출산율은 전국에서 ___를 기록했습니다. (last place)", "꼴찌", ["일등", "첫째"], "꼴찌."), F("지속적으로 인구가 감소하면 ___이 떨어집니다. (productivity)", "생산성", ["경쟁력", "잠재력"], "생산성."), F("젊은이들의 ___을 변화시키기 위해 교양과목을 개설합니다. (values)", "가치관", ["경쟁력", "입시"], "가치관."), F("보육료 ___을 지원합니다. (the full amount)", "전액", ["일부", "가계"], "전액."), F("셋째 이후 자녀에게는 ___교육을 합니다. (free)", "무상", ["유급", "조기"], "무상."),
           read_q("부산시 저출산 대책"), read_q("부산의 출산율은 꼴찌를 기록했습니다"), read_q("출산율 하락의 원인은 미혼율 상승입니다"), read_q("보육료 전액을 지원합니다"), read_q("노동력")]
    ),
)

# ================================================================== L4 Follow-ups A
_ART1 = [
    ("충북 괴산군에서 지난해까지 이천만 원이던 셋째 아이 이상 출산장려금을 올해 오천만 원으로 올렸다.", "Goesan County in North Chungcheong raised the childbirth incentive for a third child or more, which was 20 million won until last year, to 50 million won this year."),
    ("출산장려금은 출산 육아수당 천만 원, 첫만남이용권 이백만 원이 포함된 것으로 오 년간 열 번으로 나눠 지급한다.", "The childbirth incentive includes a 10 million won childbirth and child-rearing allowance and a 2 million won First Meeting Voucher, and is paid in ten installments over five years."),
    ("군 관계자는 양육비와 교육비 부담 등이 출산을 꺼리는 가장 큰 이유라며 출산 가정의 경제적 부담을 덜어주고 다산을 유도하기 위해 셋째 아이 이상 출산장려금을 인상한 것이라고 말했다.", "A county official said that the burden of child-rearing and education costs is the biggest reason for avoiding childbirth, and that the incentive for a third child or more was raised to lighten the economic burden of families that give birth and to induce having many children."),
]
_ACT1 = [("취학하는 어린이의 수가 점점 줄어든다.", "The number of children entering school gradually decreases.", "b", "effect"), ("대학에 결혼과 출산에 대한 가치관을 가르치는 교양과목을 개설한다.", "Universities open general-education courses that teach values about marriage and childbirth.", "c", "countermeasure"), ("보육료, 교육비 등의 경제적인 부담이 많다.", "The economic burden of childcare fees, education costs and so on is heavy.", "a", "cause"), ("직장생활 하면서 아이를 키우기 어렵다.", "It is hard to raise a child while working at a job.", "a", "cause"), ("아이를 꼭 낳지 않아도 된다고 생각한다.", "People think they do not have to have a child.", "a", "cause"), ("인구 감소로 인해 잠재적으로 국가 경쟁력이 약해진다.", "Because of the population decrease, national competitiveness potentially weakens.", "b", "effect"), ("미혼율이 지속적으로 증가한다.", "The rate of unmarried people keeps increasing.", "a", "cause"), ("고등학교까지의 교육을 무상으로 한다.", "Education up to high school is made free.", "c", "countermeasure"), ("배우자에게도 유급 출산휴가를 준다.", "Paid childbirth leave is also given to the spouse.", "c", "countermeasure"), ("정부에서 미혼 남녀들이 짝을 만날 수 있도록 결혼프로그램을 만든다.", "The government makes marriage programs so that unmarried men and women can meet a partner.", "c", "countermeasure")]
_ART3 = [
    ("한국보건사회연구원은 십일 일 서울 프라자 호텔에서 열린 전국 결혼 및 출산에 대한 조사 결과 보고 및 학술 세미나에서 기혼여성이 가장 원하는 정부의 저출산 대책은 지속적인 자녀의 양육, 교육비 지원이라고 밝혔다.", "The Korea Institute for Health and Social Affairs announced, at the seminar on the results of a nationwide survey on marriage and childbirth held at the Plaza Hotel in Seoul on the 11th, that the low-birthrate measure of the government that married women want most is continued support for child-rearing and education costs."),
    ("보사연이 전국의 이십 세에서 사십사 세 기혼여성 삼천오백팔십오 명을 대상으로 조사한 결과 기혼여성이 가장 원하는 정책은 지속적인 양육, 교육비 지원 오십오 점 일 퍼센트, 보육시설 지원 정책 십육 점 칠 퍼센트, 주택 지원 구 점 이 퍼센트 등의 순이었다.", "As a result of a survey of 3,585 married women aged 20 to 44 nationwide, the policies that married women want most were, in order, continued child-rearing and education cost support (55.1%), childcare facility support policy (16.7%), housing support (9.2%) and so on."),
    ("한편, 제안하고 싶은 정책을 묻는 말에 대해서는 참가자의 대부분이 자녀를 둔 사원에 대한 기업의 배려라고 답했다.", "Meanwhile, to the question asking what policy they would like to propose, most participants answered: companies’ consideration for employees with children."),
    ("또 배우자의 출산휴가를 유급으로 바꾸고 기간도 늘릴 것을 제시했다.", "They also suggested changing the spouse’s childbirth leave to paid leave and lengthening the period."),
]
L4 = lesson(
    "Ch 47 · Follow-ups A and activities: causes, effects and countermeasures",
    "출산장려금 · 저출산의 원인 · 저출산의 영향 · 저출산의 대책 · 양육비 · 교육비 · 보육시설 · 출산휴가",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a news article without a title",
             "The following excerpt is from a news article (연합뉴스) and is missing a title. The book asks you to read the article, underline the sentence that contains the topic, and write a fitting title in English. The text is the book’s with the numbers spelled out (2천만 원 is 이천만 원; 5년간 10회 is 오 년간 열 번); the English is mine. The book glosses 수당: allowance, 장려: encouraging; promotion and 꺼리다: avoid; and its note *첫만남이용권 means a system to support buying the goods needed in the early period after birth. My answers: the topic sentence is the first sentence (the raised incentive); a title could be “Goesan County raises the childbirth incentive for a third child to 50 million won.”",
             examples=passage(_ART1)),
        card("Activity 1 (Reading): cause, effect or countermeasure?",
             "Read each sentence and choose, from the phrases a. 저출산의 원인 (cause of the low birthrate), b. 저출산의 영향 (effect of the low birthrate) and c. 저출산의 대책 (countermeasure against the low birthrate), the most appropriate description. The sentences are the book’s; the answers and the English are mine.",
             tables=[table(["Sentence", "Letter (mine)", "Meaning of the letter (mine)"], [[a, c, d] for a, b, c, d in _ACT1], say=[0]), table(["English of the sentence (mine)"], [[b] for a, b, c, d in _ACT1])]),
        card("Activity 3 (Reading): the survey on married women’s wishes",
             "The following article is about Korea’s low birthrate. The text is the book’s with the numbers spelled out (11일 is 십일 일; 20~44세 is 이십 세에서 사십사 세; 3,585명 is 삼천오백팔십오 명; 55.1% is 오십오 점 일 퍼센트; the dots in 양육·교육비 are commas); the English is mine.",
             examples=passage(_ART3)),
        card("The tasks answered (mine)",
             "a. The title that fits is the third: 저출산 대책 선호도와 제안 정책 (the preference for low-birthrate measures and the proposed policies). b. The table:",
             tables=[table(["Participants in the survey", "What the percent indicates", "Suggestions made by participants"], [["3,585 married women aged 20 to 44 nationwide", "55.1%: continued support for child-rearing and education costs; 16.7%: childcare facility support policy; 9.2%: housing support", "Companies’ consideration for employees with children; changing the spouse’s childbirth leave to paid leave and lengthening the period"]])]),
        card("Activities left out",
             "Follow-up 2 (listening to two news clips, YTN and KBS, about Korea’s birthrate: the reasons for not having [more] children), Activity 2 (listening to four YTN news clips and watching the videos: checking whether each is about an effect, a cause or a countermeasure and writing the main idea) and Activity 4 (listening to an interview with a recently married couple: their work, their thoughts on having children and their concerns about raising children; exchanging the information in Korean, discussing incentives for the couple to have children, writing in the class notebook [MS TEAMS], presenting and choosing the best idea) are audio, video and pair activities."),
    ],
    exercises=uniq(
        _tr(_ART1 + _ART3, k=3) + _tr([(a, b) for a, b, c, d in _ACT1], k=3)
        + [M("How much was the incentive for a third child raised to?", "50 million won", ["20 million won", "10 million won", "2 million won"], "오천만 원."), M("How many installments is the incentive paid in?", "Ten, over five years", ["One", "Five, over ten years", "Twenty"], "오 년간 열 번."), M("What did the county official say is the biggest reason for avoiding childbirth?", "The burden of child-rearing and education costs", ["War", "Housing", "Crime"], "양육비와 교육비 부담."), M("Which category is 미혼율이 지속적으로 증가한다?", "A cause", ["An effect", "A countermeasure", "A title"], "a."), M("Which category is 취학하는 어린이의 수가 점점 줄어든다?", "An effect", ["A cause", "A countermeasure", "A cost"], "b."), M("Which category is 배우자에게도 유급 출산휴가를 준다?", "A countermeasure", ["A cause", "An effect", "A result"], "c."), M("Which category is 직장생활 하면서 아이를 키우기 어렵다?", "A cause", ["An effect", "A countermeasure", "A law"], "a."), M("Which category is 인구 감소로 인해 잠재적으로 국가 경쟁력이 약해진다?", "An effect", ["A cause", "A countermeasure", "A fee"], "b."), M("What policy do married women want most?", "Continued child-rearing and education cost support", ["Housing support", "Childcare facility support", "A new school"], "오십오 점 일 퍼센트."), M("How many married women were surveyed?", "3,585", ["5,000", "355", "20"], "삼천오백팔십오 명."), M("What did participants suggest about the spouse’s childbirth leave?", "Make it paid and lengthen it", ["Cancel it", "Shorten it", "Make it unpaid"], "유급으로 바꾸고 기간도 늘릴 것."),
           F("셋째 아이 이상 ___장려금을 올렸다. (childbirth)", "출산", ["입시", "취학"], "출산장려금."), F("양육비와 교육비 ___ 때문에 출산을 꺼립니다. (burden)", "부담", ["혜택", "배려"], "부담."), F("배우자에게도 ___ 출산휴가를 줍니다. (paid)", "유급", ["무상", "미혼"], "유급."), F("기혼여성이 가장 원하는 정책은 지속적인 양육비 ___입니다. (support)", "지원", ["평가", "무시"], "지원."), F("기업의 ___로 자녀를 둔 사원을 도웁니다. (consideration)", "배려", ["송금", "낭비"], "배려."),
           read_q("셋째 아이 이상 출산장려금을 올렸습니다"), read_q("양육비와 교육비 부담이 가장 큰 이유입니다"), read_q("미혼율이 지속적으로 증가합니다"), read_q("배우자에게도 유급 출산휴가를 줍니다"), read_q("저출산 대책 선호도")]
    ),
)


# ================================================================== L5 Topic B
_B_TXT = [
    ("한도현 씨는 기러기 아빠입니다.", "Mr. Han Do-hyeon is a goose daddy."),
    ("두 자녀가 캐나다 토론토에서 학교에 다닙니다.", "His two children go to school in Toronto, Canada."),
    ("부인도 그곳에서 아이들과 함께 생활합니다.", "His wife also lives there with the children."),
    ("가족이 떨어져 지낸 기간이 올해로 벌써 삼 년째입니다.", "As of this year the period the family has lived apart is already the third year."),
    ("자녀를 조기유학을 보낸 가장 큰 이유는 영어였습니다.", "The biggest reason he sent his children for early study abroad was English."),
    ("요즘은 학교와 직장마다 영어 열풍이 불고 있습니다.", "These days an English fever is blowing at every school and workplace."),
    ("진학이나 취업을 할 때 영어가 가장 중요한 평가 기준이 되었습니다.", "English has become the most important evaluation standard when advancing to a higher school or getting a job."),
    ("그래서 한 씨는 두 자녀를 영어를 쓰는 나라에서 공부시키고 싶었습니다.", "So Mr. Han wanted to have his two children study in a country that uses English."),
    ("또 다른 이유는 한국 교육에 대한 실망입니다.", "Another reason is disappointment in Korean education."),
    ("학생들의 개성을 무시하고 입시경쟁만 중시하기 때문입니다.", "It is because it ignores students’ individuality and emphasizes only entrance-exam competition."),
    ("아이들을 위해 기러기 아빠가 됐지만 견디기 어려울 때가 많습니다.", "He became a goose daddy for the children, but there are many times when it is hard to endure."),
    ("회사의 월급 대부분을 캐나다에 송금하기 때문에 경제적으로 늘 어렵습니다.", "Because he sends most of his company salary to Canada, he is always in economic difficulty."),
    ("혼자 있다 보니 끼니를 거를 때가 많습니다.", "Since he is alone, there are many times he skips meals."),
    ("그래서 건강도 많이 나빠졌습니다.", "So his health has also become much worse."),
    ("무엇보다도 사랑하는 가족과 헤어져 있는 것이 너무 힘듭니다.", "Above all, being parted from his beloved family is too hard."),
    ("한도현 씨는 가끔 자신이 혼자인 것처럼 생각될 때가 있습니다.", "Mr. Han Do-hyeon sometimes comes to feel as if he were alone."),
]
_B_WORDS = ["견디다", "기러기", "기준", "끼니", "떨어지다", "무시", "사례", "송금", "실망", "실제(로)", "열풍", "원어민", "이별", "입시", "전담", "조기", "중(요)시하다", "평가", "헤어지다"]
_TTL = [("사과가 나무에서 떨어졌어요.", "An apple fell off the tree."), ("지난 주에 기름값이 떨어졌어요.", "The gas price dropped last week."), ("기름이 떨어졌어요.", "I’ve run out of gas."), ("아내와 일 년 동안 떨어져 있었어요.", "I was away from my wife for a year."), ("시험에 떨어졌어요.", "I failed in the exam.")]
L5 = lesson(
    "Ch 47 · Topic B: “I am a goose daddy” (저는 기러기 아빠입니다)",
    "기러기 아빠 · 조기유학 · 영어 열풍 · 입시경쟁 · 송금 · 떨어지다 · 견디다 · 끼니 · 헤어지다",
    requires=[],
    cards=[
        card("Topic B: “I am a goose daddy” (저는 기러기 아빠입니다)",
             "The following magazine article is about a father whose family lives abroad. (The English is mine; the book gives none. The text is the book’s with 3년째 spelled 삼 년째; the news photo overlaps one line, so the words near “실망입니다” are as far as the Korean can be read. The book’s footnote: the marker ~로(써) in 올해로 specifies a designated time frame as an end point of a certain period; it translates to “as of”, e.g. 수업은 오늘로 끝납니다 [As of today, the instruction ends].)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists an attributive form + 것처럼/같이, which is the grammar of this chapter.", tables=_words(_B_WORDS)),
        card("한국어에는: the verb 떨어지다",
             "Depending on the context, the verb 떨어지다 can be translated as one of the following: 1) to fall (off) or drop, as in 사과가 나무에서 떨어졌어요 (An apple fell off the tree) and 지난 주에 기름값이 떨어졌어요 (The gas price dropped last week); 2) to run out of (money, gas, food, etc.), as in 기름이 떨어졌어요 (I’ve run out of gas); 3) to be (physically) separated or to be away from (a person), as in 아내와 1년 동안 떨어져 있었어요 (I was away from my wife for a year); 4) to fail (in the exam) as in 시험에 떨어졌어요 (I failed in the exam). (The number is spelled 일 년 below.)",
             examples=passage(_TTL)),
        card("한국에서는: 기러기 아빠",
             "기러기 아빠, whose literal meaning is “wild goose daddy,” refers to a father who remains in his home country and works while his wife and children live abroad, for the sake of the children’s education. The term likens married couples, who remain loyal to each other despite vast physical distances, to geese, which migrate seasonally and mate for life. To support their families abroad, the “left-behind” fathers work very hard and endure great loneliness and sadness."),
        card("Activities left out", "Presentation steps a (the teacher starts a PowerPoint), b (reading and listening), c (SMART Board) and d (review with the teacher) are audio and computer activities. The Sino-Korean word 전담 (專擔) is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT, k=3) + _tr(_TTL, k=3)
        + [M("Where do Mr. Han’s children go to school?", "In Toronto, Canada", ["In Seoul", "In Sydney", "In London"], "캐나다 토론토."), M("How long has the family lived apart?", "It is already the third year", ["One month", "Ten years", "Just a week"], "삼 년째."), M("What was the biggest reason for early study abroad?", "English", ["Cooking", "Sports", "Music"], "영어."), M("What has become the most important evaluation standard for advancing or getting a job?", "English", ["Looks", "Sports", "Age"], "영어."), M("What is the other reason?", "Disappointment in Korean education", ["A job transfer", "A family dispute", "Illness"], "한국 교육에 대한 실망."), M("What does Korean education ignore, according to Mr. Han?", "Students’ individuality", ["Entrance exams", "English", "Salaries"], "개성을 무시."), M("Why is he always in economic difficulty?", "He sends most of his salary to Canada", ["He lost his job", "He bought a house", "He travels a lot"], "월급 대부분을 송금."), M("What does he often do because he is alone?", "Skip meals", ["Cook big meals", "Go out to eat", "Take trips"], "끼니를 거르다."), M("What is hardest for him above all?", "Being parted from his beloved family", ["Work", "Cooking", "Commuting"], "가족과 헤어져 있는 것."), M("In 아내와 일 년 동안 떨어져 있었어요, what does 떨어지다 mean?", "to be separated from", ["to fall", "to run out", "to fail"], "Meaning 3."), M("In 시험에 떨어졌어요, what does 떨어지다 mean?", "to fail", ["to fall", "to run out", "to be separated"], "Meaning 4."), M("What does 기러기 아빠 literally mean?", "wild goose daddy", ["goose egg father", "flying father", "lonely uncle"], "The book’s note."),
           F("한도현 씨는 ___ 아빠입니다. (goose)", "기러기", ["독수리", "참새"], "기러기."), F("두 자녀를 ___유학을 보냈습니다. (early)", "조기", ["후기", "단기"], "조기유학."), F("영어가 가장 중요한 ___ 기준이 되었습니다. (evaluation)", "평가", ["송금", "이별"], "평가."), F("월급 대부분을 캐나다에 ___하기 때문에 어렵습니다. (send money)", "송금", ["평가", "무시"], "송금."), F("혼자 있다 보니 ___를 거를 때가 많습니다. (a meal)", "끼니", ["기준", "열풍"], "끼니."),
           read_q("저는 기러기 아빠입니다"), read_q("자녀를 조기유학을 보낸 가장 큰 이유는 영어였습니다"), read_q("학생들의 개성을 무시하고 입시경쟁만 중시합니다"), read_q("월급 대부분을 캐나다에 송금합니다"), read_q("가족과 헤어져 있는 것이 너무 힘듭니다")]
    ),
)

# ================================================================== L6 Follow-ups B
_STA = [
    ("제 아들은 초등학교 삼 학년입니다.", "My son is in the third grade of elementary school."),
    ("오는 칠 월에 캐나다로 삼, 사 년 정도 조기유학을 보내기로 했습니다.", "I decided to send him for early study abroad to Canada for about three or four years this coming July."),
    ("어렸을 때부터 영어를 쓰는 나라에서 공부하면 영어를 따로 공부하지 않아도 잘할 수 있지 않을까요?", "If he studies in a country that uses English from an early age, won’t he be able to do well in English without studying it separately?"),
    ("그러면 나중에 진학할 때나 커서 취직할 때 유리할 거라고 생각합니다.", "Then I think it will be advantageous later when he goes on to a higher school or gets a job when grown up."),
    ("하지만, 그곳의 학비와 생활비가 비싸서 벌써 걱정입니다.", "But the tuition and living costs there are expensive, so I am already worried."),
    ("제가 버는 돈을 거의 모두 송금해야 할 것 같습니다.", "I think I will have to send almost all the money I earn."),
]
_STB = [
    ("제 딸과 아내가 다음 달에 호주로 출국합니다.", "My daughter and wife leave for Australia next month."),
    ("중학교에 다니는 딸이 호주에 있는 사립학교에 다닐 예정입니다.", "My daughter, who goes to middle school, is going to attend a private school in Australia."),
    ("아이의 개성을 무시하고 경쟁만을 중요시하는 한국 교육에 아이가 너무 힘들어하더군요.", "I noticed that my child was finding Korean education, which ignores a child’s individuality and values only competition, too hard."),
    ("그래서 아이를 유학 보내기로 했습니다.", "So I decided to send her abroad to study."),
    ("하지만, 우리 딸이 언어가 다르고 문화가 다른 곳에서 잘 적응할 수 있을지 걱정입니다.", "But I worry whether our daughter can adapt well in a place where the language and culture are different."),
    ("조기유학을 하는 아이 중에 적응하지 못해 문제아가 되는 일도 있다고 합니다.", "They say that among children studying abroad early, some fail to adapt and become problem children."),
]
L6 = lesson(
    "Ch 47 · Follow-ups B: two fathers’ stories on early study abroad",
    "조기유학 · 유학 · 적응 · 학비 · 생활비 · 영어 · 경쟁 · 문제아 · 걱정",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): Story A",
             "The following stories are about a father who plans to send his child abroad to study. The book asks you to read them and fill in a table in English (the foreign country, the reason for early study abroad, the concerns). The stories are the book’s with the numbers spelled out (3학년 is 삼 학년; 7월 is 칠 월; 3, 4년 is 삼, 사 년); the English is mine.",
             examples=passage(_STA)),
        card("Follow-up 1 (Reading): Story B", "", examples=passage(_STB)),
        card("The table filled in (mine)",
             "",
             tables=[table(["", "Story A", "Story B"], [["Foreign country", "Canada", "Australia"], ["Reason for early study abroad", "To have the son study in an English-speaking country from an early age so that he does well in English, which would be advantageous when advancing to a higher school or getting a job", "The daughter is finding Korean education, which ignores individuality and values only competition, too hard"], ["Concerns", "The tuition and living costs are expensive, so almost all the father’s income would have to be sent", "Whether the daughter can adapt in a place where the language and culture differ; some children fail to adapt and become problem children"]])]),
        card("Activities left out", "Follow-up 2 (listening to a conversation between a married couple and checking each parent’s opinion on early study abroad, pro or con, with the reason) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_STA + _STB, k=3)
        + [M("Which country will the son in Story A go to?", "Canada", ["Australia", "Japan", "England"], "캐나다."), M("Which country will the daughter in Story B go to?", "Australia", ["Canada", "Japan", "England"], "호주."), M("What grade is the son in Story A in?", "The third grade of elementary school", ["Middle school", "High school", "College"], "초등학교 삼 학년."), M("When will the son go to Canada?", "This coming July", ["Next month", "Next year", "Tomorrow"], "오는 칠 월."), M("How long will he study abroad?", "About three or four years", ["One month", "Ten years", "A week"], "삼, 사 년 정도."), M("What is the father in Story A worried about?", "The expensive tuition and living costs", ["His son’s friends", "The weather", "The language"], "학비와 생활비."), M("What school will the daughter in Story B attend?", "A private school in Australia", ["A public school in Canada", "A Korean school", "A college"], "사립학교."), M("Why is the daughter going abroad?", "Korean education ignores individuality and values only competition", ["She wants a job", "She likes cold weather", "Her friends left"], "개성을 무시하고 경쟁만."), M("What does the father in Story B worry about?", "Whether she can adapt to a different language and culture", ["The price of the ticket", "Her grades", "Her food"], "적응."), M("What can happen to children who fail to adapt?", "They can become problem children", ["They become teachers", "They return as champions", "Nothing"], "문제아."),
           F("제 아들은 초등학교 ___ 학년입니다. (third)", "삼", ["사", "일"], "삼 학년."), F("영어를 쓰는 나라에서 공부하면 ___할 때 유리합니다. (advancing to a higher school)", "진학", ["송금", "평가"], "진학."), F("그곳의 학비와 생활비가 비싸서 ___입니다. (worry)", "걱정", ["실망", "열풍"], "걱정."), F("딸이 새로운 곳에서 잘 ___할 수 있을지 걱정입니다. (adapt)", "적응", ["이별", "견딜"], "적응."), F("개성을 ___하고 경쟁만 중요시하는 교육입니다. (ignore)", "무시", ["평가", "송금"], "무시."),
           read_q("제 아들은 초등학교 삼 학년입니다"), read_q("칠 월에 캐나다로 조기유학을 보내기로 했습니다"), read_q("학비와 생활비가 비싸서 걱정입니다"), read_q("제 딸과 아내가 다음 달에 호주로 출국합니다"), read_q("적응하지 못해 문제아가 되는 일도 있습니다")]
    ),
)


# ================================================================== L7 Grammar: attributive form + geotcheoreom/gachi
_GN = [("마이클 잭슨처럼", "like Michael Jackson"), ("한국 사람같이", "like Korean people"), ("손을 씻는 것처럼", "as if washing hands (손을 씻는 것같이)"), ("한국사람인 것처럼", "as if (one) is a Korean (한국사람인 것같이)")]
_G1 = [("조금 전에 안내자가 설명한 것처럼 이 박물관은 천구백오 년에 지어졌습니다.", "As the guide explained just now, this museum was built in 1905."), ("형이 열심히 공부한 것처럼 너도 열심히 해야 한다.", "Just as your brother studied hard, you have to study hard."), ("아버지가 여행을 좋아하시는 것처럼 저도 여행을 좋아합니다.", "I like traveling as much as my father does.")]
_G2 = [("태수가 유학 갈 것처럼 말했어요.", "Taesoo talked as if he would go abroad for study."), ("동생이 일주일 동안 굶은 것처럼 밥을 먹었어요.", "My younger brother ate as if he hadn’t eaten for a week."), ("민지는 아픈 것처럼 보였어요.", "Minji looked like she was ill.")]
_GF = [("씻는 것처럼", "as if (one) washes"), ("씻은 것처럼", "as if (one) washed"), ("갈 것처럼", "as if (one) would go"), ("아픈 것처럼", "as if (one) is ill"), ("좋아하시는 것처럼", "as (one) likes (honorific)"), ("설명한 것처럼", "as (one) explained")]
L7 = lesson(
    "Ch 47 · Grammar in Focus: an attributive form + 것처럼/같이",
    "문법 탐구 · 것처럼 · 것같이 · 관형형 · like · as · as if · 처럼 · 같이",
    requires=[],
    cards=[
        card("The conjunctive ending: an attributive form + 것처럼/같이",
             "In an earlier chapter, you learned that ~처럼/같이 (like) is preceded by a noun, as in 마이클 잭슨처럼 (like Michael Jackson) and 한국 사람같이 (like Korean people). 처럼/같이 can also be preceded by a verb or verbal phrase. In this case, however, the verb must be in an attributive form + 것. For example: 손을 씻다 → 손을 씻는 것처럼/손을 씻는 것같이; 한국사람이다 → 한국사람인 것처럼/한국사람인 것같이. An attributive form + 것처럼/같이 can mean like, as, or as if, depending on the context.",
             tables=[ktable(_GN), ktable(_GF)]),
        card("I. “Like” or “as”",
             "When an attributive form + 것처럼/같이 comes before a clause, the attributive form + 것처럼/같이 translates to like, as, or as much as. (The year 1905년 is spelled out; the English is the book’s.)",
             examples=passage(_G1)),
        card("II. “As if”",
             "When an attributive form + 것처럼/같이 comes right before a verb or a short verb phrase, it tends to mean as if. If the verb is 보이다, the whole phrase may be interpreted as look like.",
             examples=passage(_G2)),
        card("Activities left out", "Follow-up 1 (a pair task: the teacher gives lists of nouns and verb phrases; Student A reads one from List A, Student B makes a sentence with an attributive form + 것처럼/같이 and a concluding clause; the book’s model is in the next lesson), Follow-up 2 (listening to four short narrations and choosing “like, as” or “as if”, then translating) and Follow-up 4 (the friend Cheolmin who moved away suddenly: writing four things he did or said with 것처럼/같이, and giving clues in a circle) are pair, audio and group activities."),
    ],
    exercises=uniq(
        _tr(_G1 + _G2 + _GN + _GF, k=3)
        + [M("What does 것처럼/같이 mean after an attributive form?", "like; as; as if", ["because", "although", "after"], "The book’s note."), M("What must the verb be before 처럼/같이?", "An attributive form + 것", ["A bare stem", "A past stem only", "A noun"], "The book’s note."), M("When does 것처럼 mean “as if”?", "When it comes right before a verb or short verb phrase", ["When it comes before a clause", "After a noun", "At the end of a sentence"], "The book’s note."), M("What does the phrase mean if the verb is 보이다?", "look like", ["as much as", "because", "although"], "The book’s note."), M("What does 아버지가 여행을 좋아하시는 것처럼 저도 여행을 좋아합니다 mean?", "I like traveling as much as my father does", ["My father likes traveling because I do", "I do not like traveling", "My father looks like me"], "like; as much as."), M("What does 태수가 유학 갈 것처럼 말했어요 mean?", "Taesoo talked as if he would go abroad for study", ["Taesoo went abroad", "Taesoo did not talk", "Taesoo studied abroad last year"], "as if."), M("What does 민지는 아픈 것처럼 보였어요 mean?", "Minji looked like she was ill", ["Minji was in the hospital", "Minji looked at the sick", "Minji felt happy"], "보이다 = look like."), M("What does 동생이 일주일 동안 굶은 것처럼 밥을 먹었어요 mean?", "My younger brother ate as if he hadn’t eaten for a week", ["My brother fasted for a week", "My brother ate for a week", "My brother cooked rice"], "as if."),
           F("형이 열심히 공부한 ___ 너도 열심히 해야 한다. (just as)", "것처럼", ["것까지", "것보다"], "것처럼."), F("태수가 유학 갈 ___ 말했어요. (as if)", "것처럼", ["것까지", "것보다"], "것처럼."), F("민지는 아픈 것처럼 ___. (looked)", "보였어요", ["봤어요", "만났어요"], "보이다."), F("손을 씻는 ___ 했어요. (as if)", "것처럼", ["것까지", "것보다"], "것처럼."), F("한국 사람___ 말을 잘해요. (like)", "같이", ["부터", "까지"], "같이."),
           read_q("조금 전에 안내자가 설명한 것처럼 이 박물관은 천구백오 년에 지어졌습니다"), read_q("형이 열심히 공부한 것처럼 너도 열심히 해야 합니다"), read_q("태수가 유학 갈 것처럼 말했어요"), read_q("동생이 일주일 동안 굶은 것처럼 밥을 먹었어요"), read_q("민지는 아픈 것처럼 보였어요")]
    ),
)

# ================================================================== L8 Follow-ups and activities: the forum, the English town, early English
_FORUM = [
    ("주제 영어 열풍과 조기 유학", "Topic: the English fever and early study abroad"),
    ("요즘 한국에는 영어 열풍과 조기 유학 때문에 가족과 떨어져 사는 부모들이 상당히 많은 것 같습니다.", "These days in Korea there seem to be quite a lot of parents living apart from their families because of the English fever and early study abroad."),
    ("그래서 요즘 자주 뉴스에 보도되는 것처럼 기러기 아빠가 큰 사회 문제가 되고 있습니다.", "So, as is often reported in the news these days, goose daddies are becoming a big social problem."),
    ("이것은 영어가 모든 것인 것처럼 생각하는 우리 사회 때문인 것 같아요.", "I think this is because of our society, which thinks as if English were everything."),
    ("어제는 회사 직원들하고 같이 회식 후에 술집에 갔어요.", "Yesterday I went to a bar with the company staff after a company dinner."),
    ("거기서 사십 대로 보이는 남자가 혼자 앉아 있었는데 참 외로워 보였어요.", "There a man who looked to be in his forties was sitting alone, and he looked really lonely."),
    ("기러기 아빠인 것 같이 보였어요.", "He looked like a goose daddy."),
    ("아이들과 부인이 조기 유학 때문에 해외에 있는 것처럼 얘기했어요.", "He spoke as if his children and wife were overseas because of early study abroad."),
]
_MODEL2 = [("제 언니가 육군이 된 것처럼 저도 육군에 입대하고 싶어요.", "Just as my older sister became an army soldier, I want to join the army, too."), ("철민이가 며칠 전에 뉴욕에 갈 것처럼 말했어요.", "Cheolmin talked a few days ago as if he would go to New York."), ("철민이가 여행가는 것처럼 가방을 쌌어요.", "Cheolmin packed a bag as if he were going on a trip.")]
_ENG = [
    ("조기유학 이렇게 줄인다", "This is how early study abroad is reduced"),
    ("학교 수업과 생활을 할 때 영어만을 쓰도록 하는 영어 전용타운이 제주도에 만들어진다.", "An English-only town, where only English is used for school classes and daily life, is being built on Jeju Island."),
    ("해외로 빠져나가는 조기유학 수요를 국내로 돌리겠다는 것이다.", "The aim is to turn the demand for early study abroad that flows overseas back to the country."),
    ("이번에 제주도 서귀포시에 조성되는 영어 전용타운은 준비 기간이 적어도 일 년 이상이다.", "The English-only town being created this time in Seogwipo, Jeju, needs a preparation period of at least one year."),
    ("또한, 원어민 영어 교사도 계속 채용해 모든 중학교에 한 명씩 원어민 교사가 배치되도록 할 예정이다.", "In addition, it plans to keep hiring native English-speaking teachers so that one native teacher is assigned to every middle school."),
    ("정부가 이렇게 영어 교육에 중점을 두는 이유는 조기유학이나 해외 연수로 해외로 빠져나가는 학생들을 국내에서 소화하기 위해서이다.", "The reason the government puts the emphasis on English education like this is to absorb at home the students who flow overseas through early study abroad or overseas training."),
]
_COL = [
    ("한 살이라도 어릴 때 시키자", "Let’s start even a year earlier (the column’s title)"),
    ("최근 조기영어교육 열풍이 불면서 어린 나이에 영어를 가르치는 사례를 많이 볼 수 있다.", "Recently, as a fever for early English education blows, many cases of teaching English at a young age can be seen."),
    ("조기영어교육 열풍은 영어를 잘해야 학교나 직장 등에서 성공할 수 있고, 이러한 외국어 학습은 빠를수록 좋다고 생각하기 때문이다.", "The fever for early English education is because people think that one can succeed at school or a workplace only by being good at English, and that the earlier such foreign-language learning is, the better."),
    ("특히, 어린이들은 호기심이 많아 외국어를 쉽게 배울 수 있고, 세계화 시대에 영어를 빨리 가르치면 경쟁력을 키울 수 있다.", "In particular, children have much curiosity and can learn a foreign language easily, and teaching English early in the age of globalization can raise competitiveness."),
    ("그러나 이러한 조기영어교육으로 인해 여러 가지 문제도 생기고 있다.", "However, various problems are also arising because of such early English education."),
    ("모국어가 아직 서투른 아이들에게 외국어를 가르쳐 언어장애가 생기는 예도 있다.", "There are also cases in which language disorders arise from teaching a foreign language to children who are still unskilled in their mother tongue."),
    ("또한, 영어 교육으로 인해 사교육비가 급등해 가정경제에 어려움을 주고 있기도 하다.", "In addition, private education costs rise sharply because of English education, causing difficulty for household economies."),
]
L8 = lesson(
    "Ch 47 · Follow-ups and activities: the forum, the English-only town, early English",
    "토론방 · 영어 열풍 · 조기 유학 · 영어 전용타운 · 원어민 교사 · 조기영어교육 · 사교육비 · 것처럼",
    requires=[],
    cards=[
        card("Follow-up 3 (Reading): the discussion forum",
             "The following excerpt is from a website’s discussion forum about the “fever” for learning English in Korea and studying abroad. The book asks you to underline all the sentences that contain an attributive form + 것처럼/같이, to say what the writer thinks triggers the 영어 열풍 and 조기 유학, to say in detail what is mentioned about the man in his 40s, and to translate 자주 뉴스에 보도되는 것처럼 기러기 아빠가 큰 사회 문제가 되고 있습니다. The text is the book’s with 40대 spelled 사십 대; the English is mine.",
             examples=passage(_FORUM)),
        card("The tasks answered (mine)",
             "1. The sentences with 것처럼/같이: 그래서 요즘 자주 뉴스에 보도되는 것처럼 …; 이것은 영어가 모든 것인 것처럼 생각하는 우리 사회 때문인 것 같아요; 기러기 아빠인 것 같이 보였어요; 아이들과 부인이 조기 유학 때문에 해외에 있는 것처럼 얘기했어요. 2. The writer thinks it is triggered by a society that thinks as if English were everything. 3. A man who looked to be in his forties was sitting alone in a bar, looked really lonely, looked like a goose daddy and spoke as if his children and wife were overseas because of early study abroad. 4. “As is often reported in the news these days, goose daddies are becoming a big social problem.”"),
        card("Models of the pair and club tasks",
             "The book’s models for Follow-up 1 (A gives “언니/육군이 되었다”) and Follow-up 4 (what Cheolmin did or said). The English is mine.",
             examples=passage(_MODEL2)),
        card("Activity 3 (Reading): the English-only town",
             "The following excerpt is from a news article about two countermeasures the Korean government will use to solve a social issue related to English-language education. The text is the book’s with the numbers spelled out (1년 is 일 년; 1명 is 한 명); the English is mine. My answers: a. the two policies are constructing an English-only town and having a native English-speaking teacher in every middle school; b. the government emphasizes English education in order to absorb at home the students who would go overseas through early study abroad or overseas training.",
             examples=passage(_ENG)),
        card("Activity 4 (Reading): a column on early English education",
             "In this activity, you share views on early English-language education by reading a text and adding more ideas (Group A finds the positive points and Group B the negative points of the column below, then each adds ideas and presents; each person writes whether they are for or against with one supporting fact, with the model 저는 조기영어교육에 찬성합니다. 왜냐하면 …). The column is the book’s; the English is mine.",
             examples=passage(_COL)),
        card("Activity 4 answered (mine)",
             "",
             tables=[table(["Positive points (Group A)", "Negative points (Group B)"], [["One can succeed at school or work with good English; the earlier foreign-language learning is, the better; children are curious and learn easily; teaching English early in the age of globalization raises competitiveness", "Language disorders can arise in children still unskilled in their mother tongue; private education costs rise sharply and burden household economies"]])]),
        card("Activities left out", "Activity 1 (SMART Board) and Activity 2 (listening to two YTN news clips and watching the videos: identifying the social issue [goose family, excessive private education fees or early English-language education] and writing the clue words in Korean) are computer, audio and video activities."),
    ],
    exercises=uniq(
        _tr(_FORUM + _ENG + _COL + _MODEL2, k=3)
        + [M("According to the writer, what triggers the English fever and early study abroad?", "A society that thinks as if English were everything", ["The weather", "Low salaries", "A new law"], "영어가 모든 것인 것처럼 생각하는 우리 사회."), M("How did the man in the bar look?", "Lonely, like a goose daddy", ["Happy", "Angry", "Sleepy"], "외로워 보였어요."), M("How old did the man look?", "In his forties", ["In his twenties", "In his seventies", "A teenager"], "사십 대."), M("Where is the English-only town being built?", "Seogwipo, Jeju Island", ["Seoul", "Busan", "Daegu"], "제주도 서귀포시."), M("How long is the preparation period for the English-only town?", "At least one year", ["One month", "Ten years", "A week"], "적어도 일 년 이상."), M("How many native teachers will every middle school get?", "One", ["Two", "None", "Ten"], "한 명씩."), M("Why does the government stress English education?", "To absorb at home the students who would go overseas", ["To lower taxes", "To build roads", "To raise birthrates"], "국내에서 소화하기 위해서."), M("According to the column, why can children learn a foreign language easily?", "They have much curiosity", ["They are tall", "They are rich", "They are older"], "호기심이 많아."), M("What problem can early English education cause?", "Language disorders and higher private education costs", ["Lower prices", "Fewer schools", "Better health"], "언어장애, 사교육비."),
           F("영어 열풍 때문에 ___ 아빠가 큰 사회 문제가 되고 있다. (goose)", "기러기", ["독수리", "비둘기"], "기러기."), F("제주도에 영어 ___타운이 만들어진다. (exclusive)", "전용", ["전담", "전액"], "전용."), F("모든 중학교에 ___ 교사가 배치된다. (native-speaker)", "원어민", ["외국인", "전담"], "원어민."), F("조기영어교육으로 ___비가 급등했다. (private education)", "사교육", ["보육", "입시"], "사교육비."), F("그 남자는 혼자인 ___ 보였어요. (as if)", "것처럼", ["것까지", "것보다"], "것처럼."),
           read_q("영어 열풍과 조기 유학"), read_q("제주도에 영어 전용타운이 만들어집니다"), read_q("모든 중학교에 원어민 교사가 한 명씩 배치됩니다"), read_q("조기영어교육 열풍이 불고 있습니다"), read_q("영어 교육으로 사교육비가 급등했습니다")]
    ),
)


# ================================================================== L9 Topic C
_C_TXT = [
    ("서울에서 직장을 다니는 스물아홉 살 최 모 씨는 값비싼 브랜드의 제품을 선호하고 애용한다.", "Mr. Choi, 29, who works at a company in Seoul, prefers and habitually uses products of expensive brands."),
    ("그래서 최 씨는 월급의 절반 이상을 명품 구입에 낭비하고 있다.", "So Mr. Choi wastes more than half of his salary on buying name-brand goods."),
    ("대학생 스물세 살 박 모 씨도 명품을 사기 위해 과외 등 아르바이트를 두세 개씩 하고 있다.", "Mr. Park, 23, a university student, also does two or three part-time jobs, such as tutoring, in order to buy name-brand goods."),
    ("박 씨는 대학에서 편하게 공부만 하고 싶지만 원하는 명품을 갖기 위해서 그 정도는 견딜 수 있다고 말했다.", "Mr. Park said, “I want to just study comfortably at university, but to have the name-brand goods I want, I can endure that much.”"),
    ("이 같은 명품 선호 분위기는 이제 나이, 성별, 수입에 관계없이 사회 전체에 만연해 있다.", "This kind of preference for name-brand goods is now rampant throughout the whole of society regardless of age, gender and income."),
    ("심지어 명품 구입을 위해 적금을 들거나 범죄를 저지르는 일도 있다.", "There are even cases of opening an installment savings account or committing a crime in order to buy name-brand goods."),
    ("이런 명품 선호 현상의 이유 중 하나는 남에게 보이고 싶은 과시욕 때문이다.", "One of the reasons for this phenomenon of preferring name-brand goods is the desire to show off to others."),
    ("무분별한 명품 소비는 가계에 부담을 주고 국가 경쟁력을 약화시킬 수 있다.", "Reckless consumption of name-brand goods can burden households and weaken national competitiveness."),
]
_C_WORDS = ["가계", "가득", "과소비", "과시", "과시욕", "관계", "낭비", "만연", "매출", "무분별", "반영", "부유층", "브랜드", "사치", "성별", "심지어", "심화", "애용", "약화", "~ 정도", "채우다"]
_NUMS = [("사람 두세 명", "two or three people"), ("사과 서너 개", "three or four apples (서너/세네)"), ("고양이 네댓 마리", "four or five cats (네댓/너덧/네다섯)"), ("수박 대여섯 개", "five or six watermelons"), ("자동차 예닐곱 대", "six or seven cars")]
L9 = lesson(
    "Ch 47 · Topic C: the excessive preference for name brands (한국인의 지나친 명품 선호)",
    "한국인의 지나친 명품 선호 · 명품 · 과시욕 · 과소비 · 낭비 · 부유층 · 가계 · 약화 · 두세 명 · 서너 개",
    requires=[],
    cards=[
        card("Topic C: the excessive preference for name brands (한국인의 지나친 명품 선호)",
             "The following article, written by a news columnist (YTN), is about the craze in a certain segment of Korean society for famous name-brand merchandise. (The English is mine; the book gives none. The text is the book’s with the ages in brackets written as ages [29 is 스물아홉 살; 23 is 스물세 살] and 2~3개 spelled 두세 개. The book’s footnotes: 4 ~에 관계없이 [regardless of]; 5 적금을 들다 [to open a savings account; “enter into installment savings”].)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_C_WORDS)),
        card("한국어에는: two sequential numbers",
             "In Korea, when you need to mention two sequential numbers, as in “two or three people” or “three or four apples,” you will say the following: two or three people: (사람) 두세 명; three or four apples: (사과) 서너/세네 개; four or five cats: (고양이) 네댓/너덧/네다섯 마리; five or six watermelons: (수박) 대여섯 개; six or seven cars: (자동차) 예닐곱 대.",
             tables=[ktable(_NUMS)]),
        card("Activities left out", "Presentation steps a (the teacher starts a PowerPoint), b (reading and listening), c (SMART Board) and d (review with the teacher) are audio and computer activities. The Sino-Korean word 명품 선호 (名品 選好) is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT, k=3) + _tr(_NUMS, k=3)
        + [M("What does Mr. Choi spend more than half his salary on?", "Name-brand goods", ["Rent", "Food", "Travel"], "월급의 절반 이상."), M("Why does Mr. Park do two or three part-time jobs?", "To buy name-brand goods", ["To pay tuition", "To travel", "To save for a house"], "명품을 사기 위해."), M("Regardless of what is the preference rampant in society?", "Age, gender and income", ["Region only", "Season", "Nationality"], "나이, 성별, 수입에 관계없이."), M("What do some people do to buy name-brand goods?", "Open installment savings or even commit a crime", ["Move abroad", "Quit their jobs", "Sell cars"], "적금을 들거나 범죄를."), M("What is one reason for the phenomenon?", "The desire to show off to others", ["Low prices", "Good weather", "Boredom"], "과시욕."), M("What can reckless consumption of name-brand goods do?", "Burden households and weaken national competitiveness", ["Raise exports", "Lower prices", "Create jobs"], "가계에 부담, 국가 경쟁력 약화."), M("How do you say “two or three people”?", "두세 명", ["서너 명", "대여섯 명", "예닐곱 명"], "두세."), M("How do you say “five or six watermelons”?", "대여섯 개", ["두세 개", "서너 개", "예닐곱 개"], "대여섯."), M("How do you say “six or seven cars”?", "예닐곱 대", ["두세 대", "서너 대", "대여섯 대"], "예닐곱."), M("How do you say “three or four apples”?", "서너 개", ["두세 개", "네댓 개", "대여섯 개"], "서너."),
           F("최 씨는 월급의 절반 이상을 명품 구입에 ___하고 있다. (waste)", "낭비", ["송금", "평가"], "낭비."), F("명품 선호는 남에게 보이고 싶은 ___ 때문이다. (desire to show off)", "과시욕", ["경쟁력", "생산성"], "과시욕."), F("이런 분위기는 사회 전체에 ___해 있다. (rampant)", "만연", ["심화", "약화"], "만연."), F("무분별한 소비는 국가 경쟁력을 ___시킬 수 있다. (weaken)", "약화", ["심화", "개설"], "약화."), F("아르바이트를 ___ 개씩 하고 있다. (two or three)", "두세", ["서너", "대여섯"], "두세 개."),
           read_q("한국인의 지나친 명품 선호"), read_q("월급의 절반 이상을 명품 구입에 낭비합니다"), read_q("명품 선호는 사회 전체에 만연해 있습니다"), read_q("명품을 사기 위해 아르바이트를 두세 개씩 합니다"), read_q("무분별한 명품 소비는 가계에 부담을 줍니다")]
    ),
)

# ================================================================== L10 Follow-ups C and activities: fake bags and magazines
_MAG = [
    ("일부 부유층의 명품 선호 분위기는 이제 나이에 관계없이 사회 전체에 만연해 있다.", "The preference for name-brand goods among some of the rich is now rampant throughout society regardless of age."),
    ("이런 분위기 때문에 심지어 청소년들까지 명품 구매에 관심이 많다.", "Because of this atmosphere, even teenagers have a lot of interest in buying name-brand goods."),
    ("일부 청소년들은 돈을 모아서 가짜 명품을 사기도 한다.", "Some teenagers save money and even buy fake name-brand goods."),
    ("이런 현상은 남에게 보여 주기 위한 과시욕 때문으로 생각된다.", "This phenomenon is thought to be due to the desire to show off to others."),
    ("고등학교 일 학년 열일곱 살 송 모 양도 최근에 동대문 시장에서 가짜 샤넬 가방을 샀다.", "Ms. Song, 17, a first-year high school student, also recently bought a fake Chanel bag at the Dongdaemun market."),
    ("송 양은 이런 자신의 명품 선호에 대해 다른 친구들과 다르다는 것을 보여 줄 수 있어서 좋다고 말했다.", "About her own preference for name-brand goods, Ms. Song said, “I like it because I can show I am different from the other friends.”"),
    ("또한 친구들이 부러워하면 내가 특별해진 것 같아서 좋다고 밝혔다.", "She also said, “When my friends envy me, I like it because I feel as if I have become special.”"),
]
_MAG3 = [
    ("최근 십 대와 이십 대 여성들을 대상으로 하는 여성잡지가 쏟아지면서 여성들의 과소비가 증가하고 있다.", "As magazines aimed at women in their teens and twenties have been pouring out recently, women’s overspending is increasing."),
    ("예전에 있던 많은 잡지뿐만 아니라 최근 많은 수의 외국 라이센스 잡지들이 유행처럼 생겨나면서 십 대와 이십 대에게 다양한 광고와 제안을 하고 있다.", "Not only the many magazines that existed before but also a large number of foreign-licensed magazines recently appearing like a fad are making various advertisements and suggestions to teens and twenty-somethings."),
    ("이들 잡지의 내용은 주로 화장법, 옷 코디, 헤어스타일 등의 뷰티와 패션 관련 내용과 화장품이나 옷들의 소비에 집중되어 있다.", "The content of these magazines is concentrated on beauty and fashion topics such as makeup methods, clothing coordination and hairstyles, and on the consumption of cosmetics and clothes."),
    ("이런 잡지를 읽는 십, 이십 대 여성들은 대부분 특별한 소득 없이 부모들로부터 용돈을 받거나 아르바이트로 돈을 벌어서 사용하는 세대들이다.", "The women in their teens and twenties who read such magazines are mostly a generation that receives allowances from their parents or earns money from part-time jobs, without special income."),
    ("그런데도 잡지들에 나오는 옷들이나 화장품, 액세서리 등이 개당 가격이 수십만 원을 넘는 명품들로 소개되고 있어서 명품 소비를 통한 과소비를 유발하고 있다.", "Even so, the clothes, cosmetics, accessories and so on that appear in the magazines are introduced as name-brand goods costing over several hundred thousand won each, inducing overspending through name-brand consumption."),
    ("또 이 같은 잡지에 소개되는 고가의 상품을 대부분 신용카드로 구입하기 때문에 신용불량 등의 원인으로 지적되고 있다.", "Also, because most of the expensive goods introduced in such magazines are bought with credit cards, they are pointed out as a cause of bad credit and so on."),
]
L10 = lesson(
    "Ch 47 · Follow-ups C and activities: a fake Chanel bag and fashion magazines",
    "명품 · 가짜 · 청소년 · 과시욕 · 잡지 · 신용카드 · 신용불량 · 과소비 · 유발 · 부러워하다",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a magazine article on a social trend",
             "The following magazine article is about a recent social trend in Korea. The book asks you to underline the main idea, to write in English the biographical information of the person used as an example and the action she took, and to write two reasons she gives for liking being part of the trend. The text is the book’s with the age and grade written out (1학년 is 일 학년; 17 is 열일곱 살); the quotation marks are removed. The English is mine.",
             examples=passage(_MAG)),
        card("Follow-up 1 answered (mine)",
             "a. The main idea is the first sentence: the preference for name-brand goods is now rampant throughout society regardless of age. b. Ms. Song is a 17-year-old first-year high school student; recently she bought a fake Chanel bag at the Dongdaemun market. c. Two reasons: she can show that she is different from her other friends; when her friends envy her she feels as if she has become special."),
        card("Activity 3 (Reading): overspending and women’s magazines",
             "The following news article addresses issues associated with purchasing famous name-brand merchandise in Korea. The text is the book’s with 10대 and 20대 spelled 십 대 and 이십 대. The English is mine.",
             examples=passage(_MAG3)),
        card("Activity 3 answered (mine)",
             "a. 1. Women in their teens and twenties are most affected. 2. The cause is the flood of women’s magazines that introduce expensive name-brand goods. b. The order in which the points appear: 1 introduction of new fashions, makeup, coordination of clothes and hairstyles; 2 buying merchandise with a parental allowance or income from part-time jobs; 3 introduction of expensive merchandise over several hundred dollars (the article says several hundred thousand won); 4 bad credit ratings caused by the overuse of credit cards."),
        card("Activities left out",
             "Follow-up 2 (listening to a YTN report about a survey on name-brand merchandise: choosing the title, “mothers with daughters buy more name-brand goods”, “mothers with sons buy more” or “mothers with no children buy more”, and saying what the numbers 103,260 people, 52% and 23 times refer to), Activity 1 (SMART Board), Activity 2 (a YTN news clip on name-brand markets in Korea: the main idea and three true/false statements: the market for name-brand goods has suffered because of the financial crisis; it has been growing rapidly; only department stores sell name-brand goods) and Activity 4 (groups read Text A or Text B about the preference for name-brand goods, noting the people, brands, items and reasons, writing and presenting in Korean; the two texts are not printed in the student text) are audio, video, computer and group activities."),
    ],
    exercises=uniq(
        _tr(_MAG + _MAG3, k=3)
        + [M("What is the main idea of the magazine article?", "The preference for name brands is rampant in society regardless of age", ["Only the rich buy goods", "Fake goods are cheap", "Teenagers dislike brands"], "나이에 관계없이."), M("What did Ms. Song buy?", "A fake Chanel bag", ["A real Chanel bag", "A watch", "Shoes"], "가짜 샤넬 가방."), M("Where did she buy it?", "At the Dongdaemun market", ["At a department store", "Online", "In Paris"], "동대문 시장."), M("How old is Ms. Song?", "17", ["23", "29", "40"], "열일곱 살."), M("What is her first reason for liking it?", "She can show she is different from her friends", ["It is cheap", "It is useful", "It is light"], "다른 친구들과 다르다는 것."), M("What is her second reason?", "She feels special when her friends envy her", ["She feels rich", "She feels safe", "She feels tired"], "내가 특별해진 것 같아서."), M("Who are most affected by the overspending in Activity 3?", "Women in their teens and twenties", ["Men in their fifties", "Children", "Retirees"], "십 대와 이십 대 여성."), M("What causes the overspending according to the article?", "Magazines introducing expensive name-brand goods", ["Cheap goods", "Low prices", "Rising salaries"], "잡지."), M("How do these readers get money?", "Allowances from parents or part-time jobs", ["Salaries", "Pensions", "Stocks"], "용돈 또는 아르바이트."), M("What does buying expensive goods with credit cards cause?", "Bad credit ratings", ["Higher salaries", "More savings", "Lower prices"], "신용불량."),
           F("일부 청소년들은 ___ 명품을 사기도 한다. (fake)", "가짜", ["진짜", "새"], "가짜."), F("송 양은 친구들이 ___하면 특별해진 것 같아서 좋다고 했다. (envy)", "부러워", ["무시", "송금"], "부러워하다."), F("이런 현상은 남에게 보여 주기 위한 ___ 때문이다. (desire to show off)", "과시욕", ["경쟁력", "생산성"], "과시욕."), F("잡지들이 명품 소비를 통한 ___를 유발하고 있다. (overspending)", "과소비", ["절약", "송금"], "과소비."), F("고가의 상품을 신용카드로 구입해서 ___의 원인이 된다. (bad credit)", "신용불량", ["입시", "열풍"], "신용불량."),
           read_q("일부 부유층의 명품 선호는 사회 전체에 만연해 있습니다"), read_q("송 양은 가짜 샤넬 가방을 샀습니다"), read_q("친구들이 부러워하면 내가 특별해진 것 같아서 좋습니다"), read_q("여성잡지가 과소비를 유발하고 있습니다"), read_q("신용카드로 구입해서 신용불량이 됩니다")]
    ),
)


# ================================================================== L11 Grammar: loanwords
_LW1 = [("골프", "golf"), ("테니스", "tennis"), ("기타", "guitar"), ("피아노", "piano"), ("나이트 클럽", "night club"), ("냅킨", "napkin"), ("네트워크", "network"), ("넥타이", "necktie"), ("디자인", "design"), ("레이저", "laser"), ("로비", "lobby"), ("마라톤", "marathon"), ("모델", "model"), ("에어백", "air bag"), ("트렁크", "trunk"), ("햄버거", "hamburger"), ("컴퓨터", "computer")]
_LW2 = [("가이드", "a guide; Korean equivalent 안내"), ("그린벨트", "a green belt; Korean equivalent 녹지"), ("디저트", "dessert; Korean equivalent 후식"), ("랭킹", "ranking; Korean equivalent 순위"), ("레이스", "a race; Korean equivalent 경주"), ("멤버", "a member; Korean equivalent 회원"), ("박스", "a box; Korean equivalent 상자"), ("빌딩", "a building; Korean equivalent 건물"), ("신드롬", "a syndrome; Korean equivalent 증후군"), ("와인", "wine; Korean equivalent 포도주"), ("타이어", "a tire; Korean equivalent 바퀴")]
_LW3 = [("미팅", "a group blind date; “meeting”"), ("핫도그", "a corn dog; “hot dog”"), ("사이다", "clear soda like Sprite™; “cider”"), ("개런티", "payment to an actor; “guarantee”"), ("스킨 로션", "toner; “skin lotion”"), ("비닐", "plastic; “vinyl”"), ("원피스", "a dress; “one piece”"), ("콘도", "time-shared property; “condo”"), ("탤런트", "a TV actor/actress; “talent”"), ("핸드폰", "a cell phone; “hand phone”")]
_LWT = [("gown", "가운", "까운"), ("doughnut", "도넛", "도너츠"), ("video tape", "비디오테이프", "비디오테잎"), ("flash", "플래시", "후레쉬"), ("champion", "챔피언", "챔피온")]
L11 = lesson(
    "Ch 47 · Grammar in Focus: revisiting English loanwords (외래어)",
    "문법 탐구 · 외래어 · 콩글리쉬 · 골프 · 컴퓨터 · 가이드 · 미팅 · 핸드폰 · 외래어 표기",
    requires=[],
    cards=[
        card("Revisiting English loanwords",
             "Loanwords (외래어), words adopted from the West, are one of the three major components of the Korean vocabulary, along with Sino-Korean words and native Korean words. There are over 20,000 loanwords, and the number keeps growing. Although many of these loanwords are technical or scientific, the loanwords are found in almost every aspect of Korean life. Fortunately, a great majority of them are from English, and you can learn them with little difficulty. Loanwords can be categorized into one of the following three groups (the English glosses of the words are mine):"),
        card("1. Loanwords with no Korean equivalents", "골프, 테니스, 기타, 피아노, 나이트 클럽, 냅킨, 네트워크, 넥타이, 디자인, 레이저, 로비, 마라톤, 모델, 에어백, 트렁크, 햄버거, 컴퓨터, etc.", tables=[ktable(_LW1)]),
        card("2. Loanwords with Korean equivalents", "가이드 (안내), 그린벨트 (녹지), 디저트 (후식), 랭킹 (순위), 레이스 (경주), 멤버 (회원), 박스 (상자), 빌딩 (건물), 신드롬 (증후군), 와인 (포도주), 타이어 (바퀴), etc.", tables=[ktable(_LW2)]),
        card("3. Loanwords whose meanings have been localized",
             "미팅 (a group blind date; “meeting”), 핫도그 (a corn dog; “hot dog”), 사이다 (clear soda like Sprite™; “cider”), 개런티 (payment to an actor; “guarantee”), 스킨 로션 (toner; “skin lotion”), 비닐 (plastic; “vinyl”), 원피스 (dress; “one piece”), 콘도 (time-shared property; “condo”), 탤런트 (TV actors/actresses; “talent”), 핸드폰 (a cell phone; “hand phone”), etc. The loanwords in the last category are often called 콩글리쉬 (“Konglish”), which means “Korean English.”",
             tables=[ktable(_LW3)]),
        card("Writing loanwords: official and nonofficial transcription",
             "Although Koreans change the pronunciation of loanwords only slightly to make the words easier to speak in Korean, some loanwords are written in Korean uniformly, while others are not. For example, piano is consistently spelled 피아노, whereas agenda is spelled 아젠다, 아젠더, or 어젠다. In order to reduce the confusion and promote consistent transcription, 국립국어연구원 established transcription rules (1986), some of which you learned in the Introductory Unit. You can find Korean transcriptions of frequently used loanwords on the website 한글사랑 서울사랑 기본 외래어 표기. Some examples follow.",
             tables=[table(["Original word", "Official transcription", "Nonofficial transcription"], [list(r) for r in _LWT], say=[1, 2])]),
        card("English words that are not yet loanwords",
             "Koreans also use many English words which have not yet become part of the Korean language. These English words are readily found in all aspects of daily life. As the use of foreign language spreads rapidly, even Korean native speakers have a hard time keeping up with the changes. After a while, some foreign words will become standard loanwords, while others will fade away."),
        card("Activities left out", "Follow-up 1 (searching naver.com or daum.net for two minutes and writing as many loanwords as possible in Korean and English), Follow-up 2 (SMART Board) and Follow-up 3 (listening to a YTN news clip about an event held in Busan and writing the loanwords in Korean with their English meanings) are web, computer and audio activities."),
    ],
    exercises=uniq(
        _tr(_LW1 + _LW3 + [(a, b) for a, b in [("가이드", "a guide"), ("랭킹", "ranking"), ("레이스", "a race"), ("멤버", "a member"), ("박스", "a box"), ("빌딩", "a building"), ("와인", "wine"), ("타이어", "a tire")]], k=3)
        + [M("What are the three major components of the Korean vocabulary?", "Native Korean, Sino-Korean and loanwords", ["Only Sino-Korean", "English, French and German", "Slang and dialect"], "The book’s note."), M("About how many loanwords are there?", "Over 20,000", ["About 200", "About 2,000", "About 20"], "The book’s note."), M("From which language does the great majority of loanwords come?", "English", ["French", "Chinese", "Russian"], "The book’s note."), M("What is 콩글리쉬?", "“Korean English”", ["Chinese English", "A new alphabet", "A Korean dialect"], "The book’s note."), M("What does 핸드폰 mean in Korea?", "a cell phone", ["a hand fan", "a telephone booth", "a glove"], "“hand phone”."), M("What does 미팅 mean in Korea?", "a group blind date", ["a business meeting", "a class", "a game"], "Localized."), M("What does 사이다 mean in Korea?", "clear soda like Sprite", ["apple cider", "beer", "water"], "Localized."), M("What does 원피스 mean?", "a dress", ["one piece of cake", "a puzzle", "a shirt"], "Localized."), M("Which is the official transcription of “doughnut”?", "도넛", ["도너츠", "도나또", "도누트"], "The book’s table."), M("Which is the official transcription of “champion”?", "챔피언", ["챔피온", "챔프", "참피언"], "The book’s table."), M("Which is the official transcription of “flash”?", "플래시", ["후레쉬", "플레쉬", "플래쉬"], "The book’s table."), M("Which loanword has the Korean equivalent 순위?", "랭킹", ["레이스", "가이드", "박스"], "The book’s list."), M("Which loanword has the Korean equivalent 회원?", "멤버", ["박스", "빌딩", "와인"], "The book’s list."),
           F("저는 매일 ___로 일해요. (computer)", "컴퓨터", ["피아노", "테니스"], "컴퓨터."), F("주말마다 ___를 칩니다. (tennis)", "테니스", ["골프", "피아노"], "테니스."), F("회사에 갈 때 ___를 맵니다. (necktie)", "넥타이", ["냅킨", "트렁크"], "넥타이."), F("저는 ___ 하나를 시켰어요. (hamburger)", "햄버거", ["핫도그", "와인"], "햄버거."), F("___ 하나만 들고 여행을 갔어요. (a cell phone)", "핸드폰", ["컴퓨터", "라디오"], "핸드폰."),
           read_q("외래어"), read_q("컴퓨터"), read_q("핸드폰"), read_q("햄버거"), read_q("콩글리쉬")]
    ),
)

# ================================================================== L12 Daegu article, practice, self-evaluation
_DAE = [
    ("대구시는 설 명절을 맞아 대구를 방문하는 국내외 관광객들이 다양하게 체험하고 즐길 수 있는 대구 관광여행 이벤트를 실시한다고 십칠 일 밝혔다.", "The city of Daegu announced on the 17th that, for the Lunar New Year holiday, it will hold a Daegu tourist-trip event that domestic and foreign tourists visiting Daegu can experience and enjoy in various ways."),
    ("이 이벤트의 첫 번째 프로그램은 대구에 숨겨진 생태자원을 관광하며 일상에 지친 마음을 치유하고 선물도 받을 수 있는 내추럴 대구 숨은 힐링 찾기 스탬프 투어다.", "The first program of this event is the “Natural Daegu Hidden Healing Finding Stamp Tour,” in which you can tour the hidden ecological resources of Daegu, heal a mind tired of daily life and also receive a gift."),
    ("십팔 일부터 이 월 십오 일까지 운영하는 이 프로그램은 모바일 앱 스탬프 투어를 이용해 십사 개의 생태자원 코스 중 두 개 이상의 스탬프를 획득 미션 일하고, 이어 십사 개의 일반관광지 코스 중 다섯 개 이상의 스탬프를 획득 미션 이해 각각 소재 페이지의 선물 신청 버튼을 누르면 된다.", "This program, which runs from the 18th to February 15, uses the mobile app “Stamp Tour”: you obtain two or more stamps out of 14 ecological resource courses (Mission 1), then obtain five or more stamps out of 14 general tourist-spot courses (Mission 2), and press the gift application button on each page."),
    ("시티투어 탑승객을 대상으로 추가 이벤트도 진행한다.", "An additional event is also held for city tour passengers."),
    ("시티투어 버스를 타고 일반 관광코스 최소 한 개를 여행한 후 탑승권 또는 영수증과 함께 스탬프 투어 앱의 후기 게시판에 여행 후기를 남기면 선착순 백오십 명에게 모바일 음료 기프티콘을 제공한다.", "If you ride the city tour bus, travel at least one general tourist course, and leave a travel review on the “Stamp Tour” app’s review board together with your boarding pass or receipt, a mobile beverage gifticon is provided to the first 150 people."),
]
_LWFOUND = [("이벤트", "event"), ("프로그램", "program"), ("내추럴", "natural"), ("힐링", "healing"), ("스탬프", "stamp"), ("투어", "tour"), ("모바일", "mobile"), ("앱", "app"), ("미션", "mission"), ("코스", "course"), ("페이지", "page"), ("버튼", "button"), ("시티투어", "city tour"), ("버스", "bus"), ("기프티콘", "gifticon (gift + icon)")]
_OP3 = [("그 사람은 한국 사람인 것처럼 한국말을 잘해요.", "That person speaks Korean well as if he were a Korean."), ("친구가 부자인 것처럼 명품만 사요.", "My friend buys only name-brand goods as if he were rich."), ("부모님이 말씀하신 것처럼 영어는 중요합니다.", "As my parents said, English is important."), ("아이가 아픈 것처럼 보여서 병원에 갔어요.", "The child looked as if he were sick, so I went to the hospital."), ("그 아빠는 혼자인 것처럼 외로워 보였어요.", "That father looked lonely, as if he were alone.")]
L12 = lesson(
    "Ch 47 · Activities: a Daegu event with loanwords, practice, and self-evaluation",
    "대구 관광여행 이벤트 · 스탬프 투어 · 외래어 · 설 명절 · 자기 평가 · 것처럼",
    requires=[],
    cards=[
        card("Follow-up 4 (Reading): skim for loanwords",
             "Skim the following text about an event that Daegu City plans to hold. The book asks you to write in English, as quickly as you can, the loanwords or foreign-language words you recognize (including proper nouns). The text is the book’s (chosun.com) with the numbers spelled out (17일 is 십칠 일; 18일부터 2월15일까지 is 십팔 일부터 이 월 십오 일까지; 14개 is 십사 개; 미션1 is 미션 일; 150명 is 백오십 명); the brackets around 스탬프 투어, 미션 일 and 미션 이 and the dash-like marks are dropped. The book glosses 생태: ecological; eco, 선착순: in the order of arrival; first-come first-served, 지치다: to be exhausted, 추가하다: to add, 획득하다: to obtain and 후기: review. The English is mine.",
             examples=passage(_DAE)),
        card("The loanwords found (mine)", "", tables=[ktable(_LWFOUND)]),
        card("More practice sentences (mine)", "Sample sentences of my own that combine an attributive form + 것처럼 with the chapter’s vocabulary (the English is mine):", examples=passage(_OP3)),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so that they can provide other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and discuss the low birthrate trend in Korea, its causes and effects, and incentives for reversing it; identify and discuss the trend of young Koreans studying abroad; and understand and discuss the trend of people preferring famous name-brand merchandise and how the trend has affected the Korean economy.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; an attributive form + 것처럼/같이 (like; as if); loanwords in Korean; and the Sino-Korean syllables within 저출산 (低出産), 전담 (專擔), and 명품 선호 (名品 選好)."),
        card("Activities left out", "The loanword activities that use naver.com or daum.net and the Busan audio clip are in the previous lesson’s notes; the chapter’s other Activities (SMART Board, listening and video clips, group readings and presentations) are left out as noted in the earlier lessons."),
    ],
    exercises=uniq(
        _tr(_DAE, k=3) + _tr(_LWFOUND, k=3) + _tr(_OP3, k=3)
        + [M("When does the Daegu event take place?", "Around the Lunar New Year holiday", ["In summer", "At Christmas", "All year"], "설 명절."), M("What is the first program of the event?", "A stamp tour of hidden ecological resources", ["A food festival", "A concert", "A marathon"], "스탬프 투어."), M("How many stamps are needed from the ecological courses in Mission 1?", "Two or more", ["Five or more", "One", "Fourteen"], "두 개 이상."), M("How many stamps are needed from the general tourist courses in Mission 2?", "Five or more", ["Two or more", "One", "Fourteen"], "다섯 개 이상."), M("What do the first 150 reviewers of the city tour receive?", "A mobile beverage gifticon", ["A free ticket", "A bus pass", "A cash prize"], "기프티콘."), M("What is 힐링?", "healing", ["hearing", "heeling", "hailing"], "Loanword."), M("What is 기프티콘?", "a gifticon (gift + icon)", ["a gift shop", "a coupon book", "a postcard"], "Loanword."), M("What does 그 사람은 한국 사람인 것처럼 한국말을 잘해요 mean?", "That person speaks Korean well as if he were a Korean", ["That person is not Korean", "That person looks Korean", "That person lives in Korea"], "것처럼."),
           F("대구시는 ___ 명절을 맞아 이벤트를 실시한다. (Lunar New Year)", "설", ["추석", "단오"], "설."), F("모바일 앱 ___ 투어를 이용합니다. (stamp)", "스탬프", ["미션", "버튼"], "스탬프."), F("여행 ___를 게시판에 남기면 선물을 줍니다. (review)", "후기", ["영수증", "탑승권"], "후기."), F("선착순 백오십 명에게 ___합니다. (provide)", "제공", ["획득", "추가"], "제공."), F("그 아빠는 혼자인 ___ 외로워 보였어요. (as if)", "것처럼", ["것까지", "것보다"], "것처럼."),
           read_q("대구 관광여행 이벤트"), read_q("스탬프 투어"), read_q("친구가 부자인 것처럼 명품만 삽니다"), read_q("아이가 아픈 것처럼 보였습니다"), read_q("부모님이 말씀하신 것처럼 영어는 중요합니다")]
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
    "Ch 47 · Core vocabulary",
    "주요 단어 · 저출산 · 조기유학 · 명품 · 것처럼 · 외래어 · 저출산 · 전담 · 명품 선호",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. The Loan Words section repeats 브랜드, which I list once; the Grammar Features section lists the grammar of the chapter; the last section lists the Sino-Korean related words of 저출산, 전담 and 명품 선호 as the book gives them.\n\n"
             "The example sentences with digits and letters are respelled in Hangul (20일 → 이십 일; 20대 30대 → 이십 대 삼십 대; 15% → 십오 퍼센트; 1년 → 일 년; the book’s R&D in the example of 경쟁력 is dropped)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 출산 mean?", "childbirth; delivery", ["a meal", "a pair", "a benefit"], "出産."), M("What does 미혼 mean?", "single; unmarried", ["married", "paid", "free of charge"], "未婚."), M("What does 배우자 mean?", "a spouse", ["a mate of animals", "a friend", "a teacher"], "配偶者."), M("What does 보육 mean?", "childcare", ["education", "a meal", "a benefit"], "保育."), M("What does 무상 mean?", "free of charge", ["paid", "weak", "early"], "無償."), M("What does 유급 mean?", "paid", ["free of charge", "single", "weak"], "有給."), M("What does 경쟁력 mean?", "competitiveness", ["productivity", "values", "potential"], "競爭力."), M("What does 잠재력 mean?", "potential", ["competitiveness", "productivity", "values"], "潛在力."), M("What does 생산성 mean?", "productivity", ["competitiveness", "potential", "values"], "生産性."), M("What does 조기 mean?", "early (period)", ["late", "a meal", "a pair"], "早期."), M("What does 송금 mean?", "remittance", ["a meal", "a benefit", "a brand"], "送金."), M("What does 열풍 mean?", "a fever; a frenzy", ["a cold wind", "a breeze", "a storm"], "烈風."), M("What does 원어민 mean?", "a native speaker", ["a foreigner", "a teacher", "a student"], "原語民."), M("What does 과소비 mean?", "excessive spending", ["saving", "a loan", "a gift"], "過消費."), M("What does 과시욕 mean?", "a desire for showing off", ["a desire to learn", "a desire to rest", "a desire to eat"], "誇示慾."), M("What does 부유층 mean?", "the rich; the upper class", ["the poor", "the middle class", "students"], "富裕層."), M("What does 만연 mean?", "rampancy", ["a shortage", "a rest", "a cure"], "蔓延."), M("What does 심지어 mean?", "even; what’s worse", ["because", "however", "after"], "심지어."), M("What does 낭비 mean?", "waste; squandering", ["saving", "a gift", "a tip"], "浪費."), M("What does an attributive form + 것처럼/같이 mean?", "just like; as if", ["because", "although", "only"], "The grammar of the chapter."),
           F("한국의 ___ 연령은 만 여섯 살입니다. (entering school)", "취학", ["출산", "보육"], "취학."), F("인구가 줄면 국가 ___이 약해집니다. (competitiveness)", "경쟁력", ["생산성", "잠재력"], "경쟁력."), F("태국에 한국 드라마 ___이 불고 있습니다. (fever)", "열풍", ["기준", "사례"], "열풍."), F("남에게 보이고 싶은 ___ 때문에 비싼 물건을 삽니다. (desire to show off)", "과시욕", ["생산성", "배우자"], "과시욕."), F("이런 문화는 사회 전체에 ___돼 있습니다. (rampant)", "만연", ["개설", "제시"], "만연."),
           read_q("주요 단어"), read_q("출산"), read_q("미혼"), read_q("열풍"), read_q("과소비")]
    ),
)

UNIT = unit("Semester 2 · Unit 12 · Chapter 47: Social Issues I (사회 문제 1)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])
