"""Unit 22: KBC Semester 1, Unit 4, Chapter 15 - The Korean Peninsula and the Korean War (한반도와 한국전쟁).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 4, Student's Edition (2022).
Audio, video clips, photos, maps, diagrams, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_kbc import _B_IRR, _base_ao


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


def _ao(verb):
    """the -아/어 base (without 요), including the ㅂ irregular verbs: 춥다 -> 추워, 예쁘다 -> 예뻐, 빠르다 -> 빨라"""
    if verb in _IRR:
        st = stem(verb)
        l, v, t = _K.decompose(st[-1])
        return st[:-1] + _K.compose(l, v, "") + "워"
    return informal(verb)[:-1]


def _jida(verb):
    """(-아/어지다, -아/어집니다, -아/어졌어요, -아/어질 거예요)"""
    b = _ao(verb)
    return b + "지다", b + "집니다", b + "졌어요", b + "질 거예요"


def _nde(verb, action):
    """-는데 after an action verb (and 있다, 없다); -(으)ㄴ데 after a stative verb: 가다 -> 가는데, 크다 -> 큰데, 좋다 -> 좋은데, 춥다 -> 추운데"""
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    if action:
        if t == "ㄹ":
            return st[:-1] + _K.compose(l, v, "") + "는데"
        return st + "는데"
    if verb in _IRR:
        return _ao(verb)[:-1] + "운데"
    if t == "ㄹ":
        return st[:-1] + _K.compose(l, v, "ㄴ") + "데"
    if t:
        return st + "은데"
    return st[:-1] + _K.compose(l, v, "ㄴ") + "데"


def _blunt(verb, action):
    """formal blunt present: action verbs -ㄴ다/는다, stative verbs -다"""
    st = stem(verb)
    if not action:
        return st + "다"
    l, v, t = _K.decompose(st[-1])
    if t == "ㄹ":
        return st[:-1] + _K.compose(l, v, "ㄴ") + "다"
    if t:
        return st + "는다"
    return st[:-1] + _K.compose(l, v, "ㄴ") + "다"


# ---- the core vocabulary of Chapter 15 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_GEO = [
    ("국가 / 나라", "(國家) a nation; a country", "프랑스, 영국, 독일은 유럽 국가입니다."),
    ("남부", "(南部) a southern region", "텍사스 주는 미국 남부에 있어요."),
    ("남한 / 대한민국", "(南韓 / 大韓民國) South Korea / Republic of Korea", "대한민국을 남한이라고도 합니다."),
    ("남해", "(南海) the South Sea", "남해에 아름다운 섬이 많습니다."),
    ("~도", "(道) a province; a road; a way", "남한에는 아홉 개의 도가 있습니다."),
    ("(도)시", "(都市) a city; an urban area", "샌프란시스코와 뉴욕은 큰 도시입니다."),
    ("동부", "(東部) an eastern region", "한국의 산은 주로 동부에 있다."),
    ("동해", "(東海) the East Sea", "사람들이 동해에 있는 해수욕장에 많이 갑니다."),
    ("북부", "(北部) a northern region", "북부 지방은 눈이 내리고 춥겠습니다."),
    ("북한 / 조선 민주주의 인민공화국", "(北韓 / 朝鮮 民主主義 人民共和國) North Korea / the Democratic People’s Republic of Korea (DPRK)", "북한의 공식적인 이름은 조선 민주주의 인민공화국이다."),
    ("서부", "(西部) a western region", "엘에이가 미국 서부에서 가장 큰 도시이다."),
    ("서해", "(西海) the West Sea; the Yellow Sea", "서해를 황해라고도 합니다."),
    ("섬", "an island", "하와이는 아름다운 섬입니다."),
    ("중부", "(中部) a central region", "중부 아메리카를 라틴 아메리카라고 한다."),
    ("지도", "a map", "길을 모를 때 지도를 보고 찾아갑니다."),
    ("지방", "a region", "내일 중부 지방에 비가 오겠습니다."),
    ("해수욕장", "a beach for swimming", "날씨가 더우니까 주말에 해수욕장에 놀러 가자."),
]
_CV_TEMP = [
    ("~도", "degree (of temperature)", "오늘은 기온이 구십 도예요. 덥겠어요."),
    ("기온", "(氣溫) atmospheric temperature", "여름은 기온이 높고 겨울은 기온이 낮습니다."),
    ("섭씨", "the Celsius scale (centigrade) for temperature", "십오 도 씨는 한국말로 “섭씨 십오 도”라고 읽는다."),
    ("영상", "(零上) above zero (in temperature)", "오늘은 기온이 영상이어서 아주 따뜻해요."),
    ("영하", "(零下) below zero (in temperature)", "한국은 겨울에는 보통 기온이 영하입니다."),
    ("최고", "(最高) the highest; best; maximum", "오늘 최고 기온은 영상 이십팔 도입니다."),
    ("최저", "(最低) the lowest; minimum", "오늘 최저 기온은 영하 이 도입니다."),
    ("화씨", "the Fahrenheit scale for temperature", "화씨 팔십육 도는 섭씨 삼십 도쯤 된다."),
]
_CV_WAR = [
    ("공동경비구역", "(共同警備區域) Joint Security Area (JSA)", "판문점의 공식적인 이름은 공동경비구역입니다."),
    ("미군", "(美軍) the U.S. armed forces; an American serviceman", "한국에 있는 미군의 숫자가 얼마나 돼요?"),
    ("분단", "(分斷) a division (of a country) (~되다: to be divided)", "한국은 남한과 북한으로 분단되었어요."),
    ("싸우다", "to fight; to combat; to quarrel", "육이오 전쟁 때 남북한이 싸웠어요."),
    ("육이오", "(六二五) the Korean War; “June 25”", f"육이오는 {year_ko(1950)} {month_ko(6)} {day_ko(25)}에 일어난 한국전쟁이에요."),
    ("일어나다", "to occur; to break out; to get up", f"베트남 전쟁은 {year_ko(1964)}에 일어났어요."),
    ("자유", "(自由) freedom", "북한에는 자유가 별로 없다."),
    ("전쟁", "(戰爭) a war", "한국전쟁을 육이오라고 합니다."),
    ("참전", "(參戰) participation in a war (~하다: to participate in a war)", "미국도 유엔군으로 한국전쟁에 참전했어요."),
    ("통일", "(統一) unification (~하다/되다: to unify/to be unified)", "남한과 북한이 빨리 통일이 되면 좋겠어요."),
    ("판문점", "(板門店) Panmunjom", "판문점은 비무장지대 안에 있어요."),
    ("평화", "(平和) peace", "한국에 있는 미군은 한국의 평화를 위해 일한다."),
    ("휴전", "(休戰) an armistice; a truce (~하다/되다: to arrive at a truce)", f"한국전쟁은 {year_ko(1950)}에 시작해서 {year_ko(1953)}에 휴전이 되었어요."),
    ("휴전선", "(休戰線) an armistice line; a truce line", "휴전선의 길이가 백오십오 마일입니다."),
]
_CV_LOAN = [
    ("미사일", "a missile", "이라크는 스커드 미사일을 가지고 있습니다."),
    ("탱크", "a tank", "한국전쟁 때 남한은 탱크가 한 대도 없었다."),
]
_CV_OTH = [
    ("공식(적)", "(公式(的)) formality; formal (~이다: to be formal; to be official)", "공식적인 회의에 가니까 양복을 입고 가세요."),
    ("관광객", "(觀光客) a tourist", "몬트레이에는 관광객들이 많이 옵니다."),
    ("(국)기", "((國)旗) a (national) flag; “(country) flag”", "태극기는 한국 국기입니다."),
    ("기념관", "(記念館 / 紀念館) a memorial hall", "워싱턴 디씨에는 전쟁기념관이 많습니다."),
    ("대표", "(代表) a representative; representation (~하다: to represent)", "누가 이번 올림픽 마라톤 국가대표가 되었어요?"),
    ("아름답다", "to be beautiful", "서울에는 아름다운 한강이 있다."),
    ("-아/어도", "(al)though; even if", "지난번 여행은 힘들었어도 정말 재미있었어요."),
    ("-아/어지다", "to become", "비가 온 뒤에 날씨가 추워졌어요."),
    ("안내원", "(案內員) a guide", "기념관에서 안내원의 설명을 들었어요."),
    ("가운데", "the middle", "판문점 가운데에 파란색 일 층 건물들이 있었다."),
    ("~에게서 / 한테서", "from (a person)", "안내원에게서 육이오에 대하여 설명을 들었습니다."),
    ("오래되다", "to be old (for inanimate objects)", "로마에는 오래된 건물이 많이 있어요."),
    ("외국인", "(外國人) a foreigner; “outside country person”", "몬트레이는 외국인 관광객들이 많이 방문합니다."),
    ("유명", "(有名) fame (~하다: to be famous)", "타이거 우즈는 골프 선수로 유명합니다."),
    ("-(으)ㄴ데 / 는데", "but; however; and", "날씨는 따뜻한데, 바람이 많이 불어요. 어제 샌프란시스코에 갔다 왔는데, 아주 재미있었어요."),
    ("인상(적)", "(印象(的)) an impression; impressive (~이다: to be impressive)", "판문점 여행은 아주 인상적이었어요."),
    ("주변", "(周邊) surrounding; around", "집 주변에 큰 공원이 있어요."),
    ("찍다", "to take (a photograph); “press”", "하와이에 놀러 가서 사진을 많이 찍었어요."),
    ("회의실", "(會議室) a conference room", "대표들이 회의실에 모여 있다."),
]
_CV_SINO = [
    ("부", "(部) part of an area; a region", "동부, 서부, 남부, 북부, 중부"),
    ("해", "(海) sea", "해군, 동해, 서해, 남해"),
]
_ALL = {r[0]: r for r in _CV_GEO + _CV_TEMP + _CV_WAR + _CV_LOAN + _CV_OTH}
_ALL["~도 (temperature)"] = _CV_TEMP[0]
_EXTRA = {"한반도": "the Korean Peninsula (mine)", "유명하다": "to be famous"}


def _en(word):
    if word in _EXTRA:
        return _EXTRA[word]
    t = _re.sub(r"^\([^)]*(\([^)]*\))?[^)]*\) ", "", _ALL[word][1])
    return _clean(_re.sub(r" \(~[^)]*\)", "", t))


def _pairs(words):
    return [(w, _en(w)) for w in words]


def _rows(words):
    return [(w.split(" (")[0] if w == "~도 (temperature)" else w, _EXTRA[w] if w in _EXTRA else _ALL[w][1]) for w in words]


# ================================================================== Objectives and Sino-Korean 해 and 부
_HAE = [("해군", "navy; “sea soldier”"), ("동해", "the East Sea"), ("해저", "the sea bottom; the seabed; “sea low”"), ("해수", "sea water (mine)"), ("서해", "the West Sea"), ("남해", "the South Sea"), ("해병대", "the Marine Corps (mine)")]
_BU = [("전부", "all; “whole part”"), ("일부", "a part; “one part”"), ("부분", "a portion; “part divided”"), ("대부분", "most; “large part”"), ("동부", "east area; “eastern region”"), ("서부", "the West; “western region”"),
       ("국방부", "the Ministry of National Defense"), ("환경부", "the Ministry of Environment"), ("부장", "a department chief"), ("유도부", "a judo club")]
L1 = lesson(
    "Ch 15 · What the chapter teaches and the Sino-Korean syllables 해 and 부",
    "한반도와 한국전쟁 · 해 (海) · 부 (部) · 동해 · 서해 · 남해 · 동부 · 서부 · 국방부",
    requires=[],
    cards=[
        card("What Chapter 15 teaches (한반도와 한국전쟁)",
             "Chapter 15, “The Korean Peninsula and the Korean War”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and locate provinces, major cities, and well-known tourist attractions in Korea; talk about weather; comprehend basic information about the Korean War; comprehend basic information about the Joint Security Area and its facilities in Korea; and describe a building in a simple paragraph.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -아/어지다, used to express changes of state or condition; the conjunctive ending -(으)ㄴ데/는데 (and; but; however); the conjunctive ending -아/어도 (even if; although); the formal blunt speech style verb ending; and the Sino-Korean syllables 해 (海) and 부 (部)."),
        card("Sino-Korean in use: 해 (海)",
             "This Sino-Korean syllable means sea, as in 해군 (navy; “sea soldier”), 동해 (East Sea), 해저 (sea bottom; seabed; “sea low”), etc. The book asks you to guess the meaning of 해수, 서해, 남해 and 해병대; the answers (and the English of 해수 and 해병대) are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _HAE], say=[0])]),
        card("Sino-Korean in use: 부 (部)",
             "The underlying meaning of this Sino-Korean syllable is a part, and it refers to one of several or many equal units which something is composed of or is divisible into. Depending on the context, 부 can be translated as a part, region, area, etc. This syllable is also used to refer to a part of an organization (company, government, school, etc.). When it is applied to an organization, it can be translated in various contexts as a department, ministry, or (school) club, as in 국방부, 환경부, 부장 and 유도부.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _BU], say=[0])]),
        card("Activities left out",
             "The vocabulary slide show of the Vocabulary Builder, its four SMART Board activities (Activities 1–3 and the Hot Seat game of Activity 4) and the SMART Board activities of the Presentation Activity are picture, game or computer activities."),
    ],
    exercises=uniq(
        _tr(_HAE + _BU)
        + [M(f"Which word means “{b.split(';')[0].replace(' (mine)', '')}”?", a, [x for x, _ in (_HAE + _BU) if x != a][:3], f"{a}: {b}.") for a, b in (_HAE + _BU)]
        + [M("What does the Sino-Korean syllable 해 (海) mean?", "sea", ["a part", "a road", "a vehicle"], "해군, 동해, 서해, 남해."), M("What does the Sino-Korean syllable 부 (部) mean?", "a part; a region", ["sea", "a road", "a vehicle"], "동부, 서부, 남부, 북부, 중부."),
           M("What does 부 mean in 국방부?", "a ministry (a part of the government)", ["sea", "east", "a room"], "국방부 = the Ministry of National Defense."), M("What does 부 mean in 유도부?", "a (school) club", ["a ministry", "sea", "a road"], "유도부 = a judo club."),
           M("Which word contains the syllable 해 (sea)?", "동해", ["동부", "전부", "일부"], "동해 = East Sea."), M("Which word contains the syllable 부 (part)?", "대부분", ["해군", "서해", "남해"], "대부분 = most."),
           M("Which word means “the East Sea”?", "동해", ["서해", "남해", "해저"], "동해 = East Sea."), M("Which word means “the West Sea”?", "서해", ["동해", "남해", "해군"], "서해 = West Sea."),
           read_q("동해"), read_q("서해"), read_q("남해"), read_q("해병대"), read_q("국방부")]
    ),
)

# ================================================================== Topic A
_A_DLG = [
    ("상준", "마이클, 다음 주말에 설악산에 놀러 갈까?", "Michael, shall we go to Mount Seorak for fun next weekend?"),
    ("마이클", "설악산? 설악산이 어디에 있어?", "Mount Seorak? Where is Mount Seorak?"),
    ("상준", "강원도에 있어. 여기 지도를 한번 봐.", "It is in Gangwon Province. Take a look at the map here."),
    ("마이클", "여기 찾았어! 속초시 근처에 있어. 그리고 북한하고도 가까워.", "I found it here! It is near Sokcho City. And it is also close to North Korea."),
    ("상준", "설악산은 동해도 가깝고 근처에 유명한 해수욕장도 많아.", "Mount Seorak is also close to the East Sea, and there are many famous beaches nearby."),
    ("마이클", "그래? 나 해수욕장에도 가고 싶어.", "Really? I want to go to a beach too."),
    ("상준", "좋아. 설악산 구경한 후에 경포대 해수욕장에 가자.", "Good. After seeing Mount Seorak, let’s go to Gyeongpodae Beach."),
    ("마이클", "재미있겠다. 상준아, 근데 한국에 산이 많아?", "That sounds fun. Sangjoon, by the way, are there many mountains in Korea?"),
    ("상준", "응. 특히 북부 지방과 동부 지방에 산이 많아.", "Yes. There are many mountains especially in the northern and eastern regions."),
    ("마이클", "그럼, 남한에서 가장 높은 산은 어디야?", "Then, where is the highest mountain in South Korea?"),
    ("상준", "한라산이야. 한라산은 제주도에 있어.", "It is Mount Halla. Mount Halla is on Jeju Island."),
    ("마이클", "제주도? 남해에 있는 아름다운 섬?", "Jeju Island? The beautiful island in the South Sea?"),
    ("상준", "응.", "Yes."),
    ("마이클", "그럼, 다음에 제주도에도 놀러 가자.", "Then let’s go to Jeju Island for fun next time, too."),
]
_A_WORDS = ["남부", "남한 / 대한민국", "남해", "~도", "(도)시", "동부", "동해", "북부", "서부", "서해", "섬", "아름답다", "유명하다", "중부", "지도", "지방", "해수욕장", "한반도", "북한 / 조선 민주주의 인민공화국"]
_JEJU = [("제주도", "Jeju Island; Jeju Province"), ("島 (도)", "an island"), ("道 (도)", "a province")]
L2 = lesson(
    "Ch 15 · Topic A: Mount Seorak is in Gangwon Province",
    "설악산은 강원도에 있어 · 지도 · 동해 · 해수욕장 · 제주도 · 한라산",
    requires=[],
    cards=[
        card("Topic A: Mount Seorak is in Gangwon Province (설악산은 강원도에 있어)",
             "Michael and Sangjoon are talking about their travel plans for the next weekend. (The English is mine; the book gives none.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter). The book lists 남한/대한민국 and 북한/조선 민주주의 인민공화국 together; 한반도 (the Korean Peninsula) is in the book’s list of Topic A without a gloss, so its meaning is mine.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Note: 제주도",
             "Jeju is the largest island and the smallest province of South Korea, located to the south of the mainland. However, Jeju is called 제주도, whether being referred to as Jeju Island or Jeju Province. 도 in 제주도 means both an island and a province, although they are from different Chinese characters: 島 (an island) and 道 (a province). So, whenever you hear a place name that ends in 도, other than 제주도, you know it could be either an island or a province.",
             tables=[ktable([("제주도", "Jeju Island; Jeju Province"), ("강원도", "Gangwon Province (from the dialog)")])]),
        card("Activities left out",
             "Follow-up 1 (a SMART Board activity), Follow-up 2 (listening to three short conversations about well-known tourist attractions in South Korea to complete a table of province and city) and the Presentation Activity’s SMART Board activities and review with your teacher are audio, game or computer activities. The Useful Links are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not w.startswith("~") and "/" not in w and not w.startswith("(")]))
        + _tr(_strip(_A_DLG)[:12])
        + [M("What are Michael and Sangjoon talking about?", "Their travel plans for the next weekend", ["A test", "A war", "The weather"], "다음 주말에 설악산에 놀러 갈까?"), M("Where is Mount Seorak?", "In Gangwon Province", ["On Jeju Island", "In Seoul", "In North Korea"], "강원도에 있어."),
           M("Which city is Mount Seorak near?", "Sokcho", ["Seoul", "Busan", "Jeju"], "속초시 근처에 있어."), M("Mount Seorak is close to which sea?", "The East Sea", ["The West Sea", "The South Sea", "No sea"], "동해도 가깝고."),
           M("Which beach do they plan to go to after Mount Seorak?", "Gyeongpodae Beach", ["Haeundae Beach", "Jeju Beach", "Sokcho Beach"], "경포대 해수욕장에 가자."), M("Where does Korea have many mountains?", "In the northern and eastern regions", ["In the southern region", "In the western region", "On Jeju only"], "북부 지방과 동부 지방에 산이 많아."),
           M("What is the highest mountain in South Korea?", "Mount Halla", ["Mount Seorak", "Mount Baekdu", "Mount Jiri"], "한라산이야."), M("Where is Mount Halla?", "On Jeju Island", ["In Gangwon Province", "In Seoul", "In the East Sea"], "한라산은 제주도에 있어."),
           M("In which sea is Jeju?", "The South Sea", ["The East Sea", "The West Sea", "The Yellow Sea only"], "남해에 있는 아름다운 섬."), M("What are the two meanings of 도 in 제주도?", "An island and a province", ["A road and a sea", "A city and a village", "A mountain and a river"], "島 (island) and 道 (province)."),
           M("Which Chinese character is 도 in “an island”?", "島", ["道", "海", "部"], "島 = island."), M("Which Chinese character is 도 in “a province”?", "道", ["島", "海", "部"], "道 = province."),
           F("한라산은 제주___ 있어. (the island)", "도에", ["시에", "산에"], "제주도 = Jeju Island."), F("여기 ___를 한번 봐. (a map)", "지도", ["지방", "도시"], "지도 = a map."), F("설악산은 동해도 가깝고 유명한 ___도 많아. (beaches)", "해수욕장", ["섬", "도시"], "해수욕장 = a beach for swimming."),
           F("특히 북부 ___과 동부 지방에 산이 많아. (region)", "지방", ["지도", "도시"], "지방 = a region."), F("제주도는 남해에 있는 아름다운 ___이야. (island)", "섬", ["산", "시"], "섬 = an island."), F("설악산 구경한 후에 경포대 해수욕장에 ___. (let’s go)", "가자", ["갈까", "가요"], "가다 + 자 = 가자 (informal blunt suggestion)."),
           read_q("설악산"), read_q("강원도"), read_q("제주도"), read_q("한라산"), read_q("해수욕장")]
    ),
)

# ================================================================== Activities A
_CLUES = [
    ("한국의 동쪽에 있는 바다의 이름이다.", "동해", "It is the name of the sea in the east of Korea."),
    ("남한과 북한에 각각 아홉 개가 있다. 미국의 주와 비슷하다.", "~도", "There are nine in each of South Korea and North Korea. It is similar to a state in the United States."),
    ("이곳은 크고 사람들이 많이 산다. 뉴욕, 시카고, 엘에이 등이 이것이다.", "도시", "This place is big and many people live here. New York, Chicago, Los Angeles and others are this."),
    ("주위가 모두 바다이다. 하와이, 괌, 제주도 등이 이것이다.", "섬", "It is all sea around it. Hawaii, Guam, Jeju Island and others are this."),
    ("이곳에서 수영할 수 있다.", "해수욕장", "You can swim here."),
]
L3 = lesson(
    "Ch 15 · Activities A: clue words",
    "동해 · ~도 · 도시 · 섬 · 해수욕장 · 문장 단서 (sentence clues)",
    requires=[],
    cards=[
        card("Activity 1 (Reading): sentence clues",
             "The book gives five sentence clues and asks you to write, in the space provided, the word from the box that best fits each description. The box: ~도, 해수욕장, 섬, 동해, 도시. The clues are the book’s (9개 is spelled 아홉 개); the English and the answers are mine.",
             tables=[table(["Clue (the book)", "Answer (mine)", "Meaning of the clue (mine)"], [[a, b, c] for a, b, c in _CLUES], say=[0, 1])]),
        card("The words of the box",
             "The meanings are the book’s.",
             tables=[ktable(_rows(["~도", "해수욕장", "섬", "동해", "(도)시"]))]),
        card("Activities left out",
             "Activity 2 (a SMART Board speaking and listening activity), Activity 3 (partners each read a text about a province, which the teacher hands out, and exchange the information in English: well-known cities and tourist attractions), Activity 4 (listening to three radio clips of a travel expert recommending summer vacation destinations, with a map of South Korea, a flip chart and a presentation) and the Useful Links (the administrative districts of South Korea and North Korea) are audio, partner, map or website activities."),
    ],
    exercises=uniq(
        [M("Which word fits the clue “" + c + "”?", b, [x for _, x, _ in _CLUES if x != b][:3], f"{b}: {en}") for (c, b, en) in [(a, b, c2) for a, b, c2 in _CLUES]]
        + [M(f"What does the clue “{a}” say?", c, [x for _, _, x in _CLUES if x != c][:3], f"{a} = {c}") for a, b, c in _CLUES]
        + [F("한국의 동쪽에 있는 바다의 이름은 ___이다. (the East Sea)", "동해", ["서해", "남해"], "동쪽 = east: 동해."), F("하와이, 괌, 제주도 등이 ___이다. (islands)", "섬", ["도시", "해수욕장"], "섬 = an island."),
           F("뉴욕, 시카고, 엘에이 등은 큰 ___이다. (cities)", "도시", ["섬", "지방"], "도시 = a city."), F("이곳에서 수영할 수 있다. ___이다. (a beach)", "해수욕장", ["섬", "동해"], "해수욕장 = a beach for swimming."),
           F("남한과 북한에 각각 아홉 개의 ___가 있다. (provinces)", "도", ["시", "섬"], "도 = a province."),
           M("Which word is similar to a state in the United States?", "~도", ["섬", "해수욕장", "동해"], "~도 = a province."), M("In which sea is Jeju Island according to Chapter 15’s dialog?", "남해", ["동해", "서해", "황해"], "남해에 있는 아름다운 섬."),
           read_q("동쪽"), read_q("아홉 개"), read_q("수영할 수 있다")]
    ),
)

# ================================================================== Topic B
_B_DLG = [
    ("앤더슨 상병", "오늘 날씨가 많이 따뜻해졌어요.", "The weather has gotten much warmer today."),
    ("지영", "그래요. 어제는 최고 기온이 영하 일 도였는데 오늘은 영상 오 도예요.", "Yes. Yesterday the highest temperature was 1 degree below zero, but today it is 5 degrees above zero."),
    ("앤더슨 상병", "그런데, 우리 지금 어디 가요?", "By the way, where are we going now?"),
    ("지영", "용산에 있는 전쟁 기념관에 가요.", "We are going to the War Memorial in Yongsan."),
    ("앤더슨 상병", "그래요? 기념관에서 무엇을 볼 수 있어요?", "Is that so? What can we see at the memorial?"),
    ("지영", "탱크나 미사일을 구경할 수 있어요. 그리고 한국전쟁에 대해서 알 수 있어요.", "You can see tanks and missiles. And you can learn about the Korean War."),
    ("앤더슨 상병", "그래요? 한국전쟁은 언제 일어났어요?", "Is that so? When did the Korean War break out?"),
    ("지영", f"{year_ko(1950)} {month_ko(6)} {day_ko(25)}에 일어났어요. 그래서 육이오라고 해요.", "It broke out on June 25, 1950. That is why it is called 육이오 (“June 25”)."),
    ("앤더슨 상병", "한국전쟁에 미국도 참전했어요?", "Did the United States also take part in the Korean War?"),
    ("지영", "그럼요. 미군도 유엔군으로 싸웠어요.", "Of course. The American forces also fought as United Nations forces."),
    ("앤더슨 상병", "그럼, 전쟁은 언제 끝났어요?", "Then, when did the war end?"),
    ("지영", f"{year_ko(1953)}에 휴전이 되었어요. 그리고 전쟁 후에 남한과 북한으로 분단되었어요.", "An armistice was reached in 1953. And after the war the country was divided into South Korea and North Korea."),
    ("앤더슨 상병", "한국이 빨리 통일이 되면 좋겠어요.", "I hope Korea will be unified soon."),
]
_B_WORDS = ["기념관", "기온", "국가 / 나라", "-(으)ㄴ데 / 는데", "~도 (temperature)", "미군", "미사일", "분단", "섭씨", "싸우다", "-아/어지다", "영상", "영하", "육이오", "일어나다", "전쟁", "참전", "최고", "최저", "탱크", "통일", "화씨", "휴전"]
_FOG = [("오늘은 안개가 끼었습니다.", "It is foggy today."), ("오늘은 구름이 끼었습니다.", "It is cloudy today."), ("구름이 낍니다.", "Clouds are forming (now)."), ("구름이 끼었습니다.", "Clouds have formed (and, as a result, it is cloudy).")]
L4 = lesson(
    "Ch 15 · Topic B: I went to the War Memorial of Korea",
    "전쟁기념관에 갔어요 · 따뜻해졌어요 · 영하 · 영상 · 육이오 · 휴전 · 분단 · 통일",
    requires=[],
    cards=[
        card("Topic B: I went to the War Memorial of Korea (전쟁기념관에 갔어요)",
             "SPC Anderson is talking to Jiyoung, his Korean friend, about the weather. They are on their way to the War Memorial of Korea in Yongsan, Seoul. (The English is mine; the book gives none. The book writes −1도, 5도, 1950년 6월 25일 and 1953년; they are spelled out here.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened. ~도 here means “degree (of temperature)”.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Note: 안개가 끼었습니다",
             "You will hear native speakers say 오늘은 안개가 끼었습니다, meaning it is foggy today, or 오늘은 구름이 끼었습니다, meaning it is cloudy today. Because 끼었습니다 is in the past tense, you may wonder why a Korean speaker would use the past tense to describe a present weather condition when using the verb 끼다. 끼다 literally means to form. So, when you say 구름이 낍니다, using the present tense, you are saying clouds are forming now. However, when you say 구름이 끼었습니다, the sentence implies that clouds have formed in the past and, as a result, it is cloudy.",
             examples=[D(a, b) for a, b in _FOG]),
        card("Presentation Activity: the vocabulary table",
             "The book gives a vocabulary table with half of the words missing and asks you to complete it with the Korean or the English word: 분단 (a division), 싸우다 (to fight), 육이오 (the Korean War), 영상 (above zero), 참전 (participation in a war), 최저 (the lowest), 기념관 (a memorial hall), 미사일 (a missile), 미군 (U.S. forces), 통일 (unification), 휴전 (an armistice; a truce), 일어나다 (to occur; to break out), 최고 (the highest), 탱크 (a tank), 영하 (below zero), -아/어지다 (to become) and -는데. The words are in the table above and in the exercises of this lesson."),
        card("Activities left out",
             "The SMART Board activity and the review with your teacher are computer or teacher activities. Follow-up 1 is in the next lesson; Follow-up 2 (listening to a conversation in which a man asks his female colleague about her weekend and filling in a table in English) is an audio activity; the Useful Links (the War Memorial of Korea and the Korea Meteorological Administration) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("~", "-")) and "/" not in w]))
        + _tr(_strip(_B_DLG)[:12]) + _tr(_FOG)
        + [M("Where are Anderson and Jiyoung going?", "To the War Memorial of Korea in Yongsan", ["To Mount Seorak", "To Panmunjom", "To Incheon airport"], "용산에 있는 전쟁 기념관에 가요."), M("What can they see at the memorial?", "Tanks and missiles", ["Boats and planes", "Mountains and beaches", "Flags and maps"], "탱크나 미사일을 구경할 수 있어요."),
           M("What was yesterday’s highest temperature?", "1 degree below zero", ["5 degrees above zero", "1 degree above zero", "5 degrees below zero"], "최고 기온이 영하 일 도였는데."), M("What is today’s temperature?", "5 degrees above zero", ["1 degree below zero", "5 degrees below zero", "1 degree above zero"], "오늘은 영상 오 도예요."),
           M("When did the Korean War break out?", "June 25, 1950", ["June 25, 1953", "June 5, 1950", "October 25, 1950"], "천구백오십년 유월 이십오일."), M("Why is the Korean War called 육이오?", "It broke out on June 25", ["It lasted for 25 months", "It started in 1925", "It was the 25th war"], "육이오 = “June 25”."),
           M("Who else fought in the war, according to Jiyoung?", "The American forces, as United Nations forces", ["Only Korean forces", "Chinese forces only", "Nobody else"], "미군도 유엔군으로 싸웠어요."), M("When was the armistice reached?", "1953", ["1950", "1945", "1964"], "천구백오십삼년에 휴전이 되었어요."),
           M("What happened to Korea after the war?", "It was divided into South Korea and North Korea", ["It was unified", "It joined the UN", "It became a province"], "남한과 북한으로 분단되었어요."), M("What does Anderson hope?", "That Korea will be unified soon", ["That the weather gets warmer", "That the war starts", "That he can visit the North"], "한국이 빨리 통일이 되면 좋겠어요."),
           M("What does 끼다 literally mean?", "to form", ["to fall", "to rise", "to blow"], "끼다 literally means to form."), M("What does 구름이 끼었습니다 imply?", "Clouds have formed and, as a result, it is cloudy", ["Clouds are forming now", "Clouds will form", "There were clouds yesterday only"], "The past tense implies a resulting state."),
           F("오늘 날씨가 많이 따뜻해___. (has become)", "졌어요", ["했어요", "있어요"], "따뜻하다 + -아/어지다 = 따뜻해졌어요."), F("한국전쟁은 언제 ___? (break out)", "일어났어요", ["일어나요", "일어날까요"], "일어나다 = to occur; to break out."),
           F("미군도 유엔군으로 ___. (fought)", "싸웠어요", ["싸워요", "싸울까요"], "싸우다 = to fight."), F("한국이 빨리 ___이 되면 좋겠어요. (unification)", "통일", ["분단", "휴전"], "통일 = unification."),
           F("전쟁 후에 남한과 북한으로 ___되었어요. (was divided)", "분단", ["통일", "참전"], "분단 = a division of a country."), F("천구백오십삼년에 ___이 되었어요. (an armistice)", "휴전", ["전쟁", "통일"], "휴전 = an armistice."),
           F("어제는 최고 기온이 ___ 일 도였어요. (below zero)", "영하", ["영상", "섭씨"], "영하 = below zero."), F("오늘은 ___ 오 도예요. (above zero)", "영상", ["영하", "화씨"], "영상 = above zero."),
           read_q("전쟁기념관"), read_q("영하 일 도"), read_q("영상 오 도"), read_q("한국전쟁"), read_q("휴전")]
    ),
)

# ================================================================== Weather forecast and temperature
def _deg(n):
    if n == 0:
        return "영 도"
    return ("영상 " if n > 0 else "영하 ") + sino(abs(n)) + " 도"


_FORECAST = [
    ("오늘 날씨입니다.", "This is today’s weather."),
    ("오늘은 전국이 흐리고 춥겠습니다.", "Today it will be cloudy and cold across the whole country."),
    ("서울과 중부지방은 오후 늦게나 밤부터 비가 오겠습니다.", "In Seoul and the central region it will rain from late afternoon or from night."),
    ("남부지방은 오전에 비가 온 후 오후부터 바람이 불고 추워지겠습니다.", "In the southern region, after rain in the morning, the wind will blow and it will get colder from the afternoon."),
    (f"오늘 중부지방의 최저 기온은 {_deg(-1)}에서 {_deg(3)}, 최고 기온은 {sino(5)} 도에서 {sino(8)} 도입니다.", "Today in the central region the lowest temperature is from 1 degree below zero to 3 degrees above zero, and the highest temperature is from 5 to 8 degrees."),
    ("주말에는 전국이 따뜻하고 맑겠습니다.", "Over the weekend it will be warm and clear across the whole country."),
    (f"최고 기온이 {_deg(10)} 정도로 등산이나 골프에 좋은 날씨가 되겠습니다.", "With the highest temperature at about 10 degrees above zero, it will be good weather for hiking or golf."),
]
_FC_Q = [("What is the weather like in the central region?", "Cloudy and cold; it will rain from late afternoon or night (in Seoul and the central region)."),
         ("What is the highest temperature in the central region today?", "Between 5 and 8 degrees."),
         ("What is the weather in the southern region this afternoon?", "After rain in the morning, the wind blows and it gets colder from the afternoon."),
         ("What will the weather be like over the weekend?", "Warm and clear across the whole country; about 10 degrees above zero at the highest, good for hiking or golf.")]
_FC_W = [("전국", "the whole country (mine)"), ("흐리다", "to be cloudy (mine)"), ("맑다", "to be clear (mine)"), ("비가 오다", "to rain (mine)"), ("바람이 불다", "the wind blows (mine)"), ("오전", "morning; a.m. (mine)"), ("오후", "afternoon; p.m. (mine)"), ("주말", "the weekend (mine)"), ("등산", "hiking; mountain climbing (mine)"), ("골프", "golf (mine)")]
_TEMPS = [-1, 5, 3, 8, 10, -2, 28, 15]
_TEMP_EX = [("오늘은 기온이 구십 도예요. 덥겠어요.", "Today the temperature is 90 degrees. It must be hot. (the book’s example for ~도; 90도 is spelled out)"), ("여름은 기온이 높고 겨울은 기온이 낮습니다.", "In the summer the temperature is high and in the winter the temperature is low."), ("오늘은 기온이 영상이어서 아주 따뜻해요.", "Today the temperature is above zero, so it is very warm."), ("한국은 겨울에는 보통 기온이 영하입니다.", "In Korea in the winter the temperature is usually below zero."),
            ("오늘 최고 기온은 영상 이십팔 도입니다.", "Today’s highest temperature is 28 degrees above zero."), ("오늘 최저 기온은 영하 이 도입니다.", "Today’s lowest temperature is 2 degrees below zero."), ("화씨 팔십육 도는 섭씨 삼십 도쯤 된다.", "86 degrees Fahrenheit is about 30 degrees Celsius.")]
L5 = lesson(
    "Ch 15 · Weather forecast and temperature",
    "오늘 날씨입니다 · 기온 · 영상 · 영하 · 최고 기온 · 최저 기온 · 섭씨 · 화씨",
    requires=[],
    cards=[
        card("Topic B, Follow-up 1 (Reading): the weather forecast",
             "The book gives a weather forecast and asks four questions, to be answered in English. The text is the book’s (the figures are spelled out in Hangul: −1도 → 영하 일 도, 3도 → 영상 삼 도, 5 도 → 오 도, 8도 → 팔 도, 10도 → 영상 십 도); the English is mine.",
             examples=passage(_FORECAST)),
        card("The four answers (mine)",
             "The book leaves the answers blank; these are mine.",
             tables=[table(["Question (the book)", "Answer (mine)"], [list(r) for r in _FC_Q])]),
        card("Words of the forecast",
             "These meanings are mine (the book does not gloss them).",
             tables=[ktable(_FC_W)]),
        card("Temperature words",
             "The book’s examples for the temperature words of the Core Vocabulary (the digits are spelled out in Hangul; the English is mine). The book’s note: 15° C is read in Korean as 섭씨 십오 도; in the example of 섭씨, the sentence is respelled here with 십오 도 씨.",
             examples=[D(a, b) for a, b in _TEMP_EX]),
        card("Reading temperatures",
             "Degrees are read with Sino-Korean numbers followed by 도: above zero is 영상, below zero is 영하. (The table is mine.)",
             tables=[table(["Temperature", "Korean"], [[("+" if n > 0 else "") + str(n) + " degrees", _deg(n)] for n in _TEMPS], say=[1])]),
    ],
    exercises=uniq(
        _tr(_FORECAST) + _tr(_TEMP_EX[1:] + [_TEMP_EX[0][:1] + ("Today the temperature is 90 degrees. It must be hot.",)]) + _tr(_FC_W)
        + [M(f"How do you say “{('+' if n > 0 else '')}{n} degrees” (temperature)?", _deg(n), list(dict.fromkeys(_deg(m) for m in (-n, n + 1, -n - 1, n + 2) if _deg(m) != _deg(n)))[:3], f"{'Above' if n > 0 else 'Below'} zero: {_deg(n)}.") for n in (-1, 5, 3, -2, 28, 10)]
        + [M(f"What does {_deg(n)} mean?", f"{abs(n)} degrees {'above' if n > 0 else 'below'} zero", [f"{abs(n)} degrees {'below' if n > 0 else 'above'} zero", f"{abs(n) + 1} degrees above zero", f"{abs(n) + 2} degrees below zero"], f"{'영상 = above' if n > 0 else '영하 = below'} zero.") for n in (-1, 5, 3, -2, 28, 10)]
        + [M("What is the weather in the whole country today?", "Cloudy and cold", ["Clear and warm", "Rainy and hot", "Snowy"], "전국이 흐리고 춥겠습니다."), M("When will it rain in Seoul and the central region?", "From late afternoon or night", ["In the morning", "All day", "Over the weekend"], "오후 늦게나 밤부터 비가 오겠습니다."),
           M("What will the southern region be like in the afternoon?", "Windy and colder after the morning rain", ["Hot and sunny", "Snowy", "Foggy"], "바람이 불고 추워지겠습니다."), M("What is the lowest temperature in the central region?", "From 1 degree below zero to 3 degrees above zero", ["From 5 to 8 degrees", "10 degrees above zero", "Below 5 degrees below zero"], "최저 기온은 영하 일 도에서 영상 삼 도."),
           M("What is the highest temperature in the central region?", "From 5 to 8 degrees", ["From 1 below to 3 above zero", "10 degrees above zero", "28 degrees"], "최고 기온은 오 도에서 팔 도."), M("What will the weekend be like?", "Warm and clear nationwide", ["Cold and cloudy", "Rainy in the south", "Snowy in the north"], "주말에는 전국이 따뜻하고 맑겠습니다."),
           M("What is the weather good for over the weekend?", "Hiking and golf", ["Swimming", "Skiing", "Staying home"], "등산이나 골프에 좋은 날씨."), M("Which scale is 섭씨?", "Celsius (centigrade)", ["Fahrenheit", "Kelvin", "Réaumur"], "섭씨 = the Celsius scale."), M("Which scale is 화씨?", "Fahrenheit", ["Celsius", "Kelvin", "Réaumur"], "화씨 = the Fahrenheit scale."),
           M("Which is “the highest temperature”?", "최고 기온", ["최저 기온", "영하 기온", "화씨 기온"], "최고 = the highest."), M("Which is “the lowest temperature”?", "최저 기온", ["최고 기온", "영상 기온", "섭씨 기온"], "최저 = the lowest."),
           F("오늘은 전국이 ___고 춥겠습니다. (cloudy)", "흐리", ["맑", "따뜻하"], "흐리다 = to be cloudy."), F("주말에는 전국이 따뜻하고 ___겠습니다. (clear)", "맑", ["흐리", "춥"], "맑다 = to be clear."), F("오후부터 ___이 불고 추워지겠습니다. (the wind)", "바람", ["구름", "안개"], "바람이 불다 = the wind blows."),
           F("오늘 최저 기온은 ___ 이 도입니다. (below zero)", "영하", ["영상", "섭씨"], "영하 = below zero."), F("오늘 최고 기온은 ___ 이십팔 도입니다. (above zero)", "영상", ["영하", "화씨"], "영상 = above zero."),
           read_q("오늘 날씨입니다"), read_q("전국이 흐리고 춥겠습니다"), read_q("영하 일 도"), read_q("영상 십 도"), read_q("섭씨 삼십 도")]
    ),
)

# ================================================================== Grammar A: -아/어지다
_JI_V = [("좋다", "to be good"), ("짧다", "to be short"), ("넓다", "to be wide"), ("길다", "to be long"), ("싸다", "to be cheap"), ("예쁘다", "to be pretty"), ("빠르다", "to be fast"), ("춥다", "to be cold"),
         ("따뜻하다", "to be warm"), ("더럽다", "to be dirty"), ("피곤하다", "to be tired"), ("맛있다", "to be delicious"), ("크다", "to be big"), ("덥다", "to be hot"), ("많다", "to be many"), ("어렵다", "to be difficult")]
_JI_EX = [("날씨가 따뜻해졌습니다.", "The weather got warm."), ("이번 주부터 날씨가 좋아질 거예요.", "From this week on, the weather is going to get better."), ("지난 주말부터 날씨가 추워졌어요.", "From last weekend on, the weather got colder."),
          ("설탕을 더 넣으니까 음식이 맛있어졌어요.", "Because I added more sugar, the food tasted better."), ("비가 온 뒤에 날씨가 추워졌어요.", "After it rained, the weather got cold. (the book’s example in the Core Vocabulary)")]
_JI_FU = [("봄이 되다 / 날씨가 따뜻하다", "봄이 되면 날씨가 따뜻해집니다.", "When spring comes, the weather gets warm. (the book’s own answer)"), ("할인하다 / 가격이 더 싸다", "할인하면 가격이 더 싸집니다.", "If it is discounted, the price gets cheaper."), ("겨울이 되다 / 춥다", "겨울이 되면 추워집니다.", "When winter comes, it gets cold."),
          ("청소를 안 하다 / 방이 더럽다", "청소를 안 하면 방이 더러워집니다.", "If you do not clean, the room gets dirty."), ("과일을 많이 먹다 / 예쁘다", "과일을 많이 먹으면 예뻐집니다.", "If you eat a lot of fruit, you get pretty."), ("운동을 많이 하다 / 피곤하다", "운동을 많이 하면 피곤해집니다.", "If you exercise a lot, you get tired.")]


def _ji_wrong(v):
    right = _jida(v)[0]
    cands = [stem(v) + "아지다", stem(v) + "어지다", stem(v) + "지다", informal(v) + "지다", stem(v) + "고 싶다"]
    return list(dict.fromkeys(c for c in cands if c != right))[:3]


L6 = lesson(
    "Ch 15 · Grammar A: a change of state with -아/어지다",
    "따뜻해졌습니다 · 좋아질 거예요 · 추워졌어요 · 맛있어졌어요 · 싸지다 · 예뻐지다 · 빨라지다",
    requires=[],
    cards=[
        card("Expressing a change of state or condition",
             "In English, when expressing a change of state or condition, we often use the verb become or get, followed by an adjective, as in “The weather got warm” or “He became happy.” In Korean, we use -아/어지다, which is attached to the stem of a stative verb. For example: 날씨가 따뜻해졌습니다 (The weather got warm).",
             tables=[table(["Condition", "Rule", "Example"], [["When the last syllable of a verb stem contains the vowels ㅏ or ㅗ", "add 아지다", "좋다 → 좋아지다; 짧다 → 짧아지다"], ["When the last syllable of a verb stem contains a vowel other than ㅏ or ㅗ", "add 어지다", "넓다 → 넓어지다; 길다 → 길어지다"]], title="stative verb stem + 아/어지다")],
             examples=[D(a, b) for a, b in _JI_EX[:4]]),
        card("Vowel contraction and deletion",
             "Keep in mind that when stative verbs ending in vowels like 싸다 or 예쁘다 are conjugated, they go through the same vowel contraction or deletion that occurs when they are conjugated using -아/어요 (informal speech style). The book’s examples:",
             tables=[table(["Dictionary form", "With -아/어요", "With -아/어지다"], [["싸다", "싸 + 아요 → 싸요", "싸 + 아지다 → 싸지다"], ["예쁘다", "예쁘 + 어요 → 예뻐요", "예쁘 + 어지다 → 예뻐지다"], ["빠르다", "빠르 + 아요 → 빨 + 라요 → 빨라요", "빠르 + 아지다 → 빨 + 라지다 → 빨라지다"], ["춥다", "춥 + 어요 → 추우 + 어요 → 추워요", "춥 + 어지다 → 추우 + 어지다 → 추워지다"]])],
             examples=[D(a, b) for a, b in _JI_EX[4:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule (the ㅂ irregular verbs 춥다, 덥다, 더럽다 and 어렵다 change ㅂ to 우 before the vowel: 추워지다, 더워지다, 더러워지다, 어려워지다).",
             tables=[table(["Dictionary form", "Meaning", "Become …", "Becomes (formal)", "Became (informal)", "Will become (informal)"], [[v, m, *_jida(v)] for v, m in _JI_V], say=[0, 2, 3, 4, 5])]),
        card("Follow-up 1: -(으)면 and -아/어지다",
             "The book gives six pairs of verbal phrases: revise the first with -(으)면 and the second with -아/어지다 to create a complete sentence (the first one is done for you in the book). The other five answers and the English are mine.",
             tables=[table(["Phrases (the book)", "Answer", "Meaning"], [list(r) for r in _JI_FU], say=[1])]),
        card("Activities left out",
             "Follow-up 2 (listening to four conversations about a changed state or condition, transcribing the phrase that contains -아/어지다 and translating it) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the -아/어지다 form of {v} ({m})?", _jida(v)[0], _ji_wrong(v), f"{v} → {_jida(v)[0]}.") for v, m in _JI_V]
        + [M(f"How do you say “became {m.replace('to be ', '')}” (informal polite) with {v}?", _jida(v)[2], [_jida(v)[1], _jida(v)[3], _jida(v)[0]], f"{v} → {_jida(v)[2]}.") for v, m in _JI_V]
        + [M(f"How do you say “will become {m.replace('to be ', '')}” (informal polite) with {v}?", _jida(v)[3], [_jida(v)[1], _jida(v)[2], _jida(v)[0]], f"{v} → {_jida(v)[3]}.") for v, m in _JI_V[:10]]
        + _tr(_JI_EX + [(b, c.replace(" (the book’s own answer)", "")) for a, b, c in _JI_FU])
        + [F("날씨가 따뜻해___. (got)", "졌습니다", ["집니다", "지겠습니다"], "따뜻하다 + -아/어지다 → 따뜻해졌습니다."), F("이번 주부터 날씨가 좋아___ 거예요. (is going to get)", "질", ["진", "지는"], "-아/어지다 + -(으)ㄹ 거예요 = 좋아질 거예요."), F("지난 주말부터 날씨가 추워___. (got)", "졌어요", ["질 거예요", "집니다"], "추워지다 → 추워졌어요."),
           F("설탕을 더 넣으니까 음식이 맛있어___. (became)", "졌어요", ["질 거예요", "집니다"], "맛있다 → 맛있어지다."), F("비가 온 뒤에 날씨가 추워___. (got)", "졌어요", ["질 거예요", "집니다"], "past: 추워졌어요."), F("봄이 되면 날씨가 따뜻해___. (gets)", "집니다", ["졌습니다", "지겠어요"], "Present formal: 따뜻해집니다."),
           F("청소를 안 하면 방이 더러워___. (gets)", "집니다", ["졌습니다", "지겠어요"], "더럽다 → 더러워지다."), F("운동을 많이 하면 피곤해___. (you get)", "집니다", ["졌습니다", "지겠어요"], "피곤하다 → 피곤해지다."),
           F("할인하면 가격이 더 싸___. (gets)", "집니다", ["졌습니다", "지겠어요"], "싸다 → 싸지다 (싸 + 아지다)."), F("과일을 많이 먹으면 예뻐___. (you become)", "집니다", ["졌습니다", "지겠어요"], "예쁘다 → 예뻐지다."),
           M("What does -아/어지다 express?", "A change of state or condition (to become)", ["An action in progress", "A reason", "A purpose"], "-아/어지다 = to become."), M("To what kind of verb is -아/어지다 attached?", "A stative verb", ["An action verb", "A noun", "A particle"], "stative verb stem + 아/어지다."),
           M("Which verb stem takes 아지다?", "좋다", ["넓다", "길다", "크다"], "The last vowel ㅗ takes 아지다."), M("Which verb stem takes 어지다?", "넓다", ["좋다", "짧다", "많다"], "The last vowel ㅓ takes 어지다."),
           M("What is 빠르다 + -아/어지다?", "빨라지다", ["빠르어지다", "빠라지다", "빠르아지다"], "빠르 + 아지다 → 빨 + 라지다 → 빨라지다."), M("What is 예쁘다 + -아/어지다?", "예뻐지다", ["예쁘어지다", "예쁘지다", "예쁘아지다"], "예쁘 + 어지다 → 예뻐지다."),
           M("What is 춥다 + -아/어지다?", "추워지다", ["춥어지다", "춥아지다", "추우지다"], "춥 + 어지다 → 추우 + 어지다 → 추워지다."), M("What is 싸다 + -아/어지다?", "싸지다", ["싸아지다", "싸어지다", "써지다"], "싸 + 아지다 → 싸지다."),
           read_q("따뜻해졌습니다"), read_q("좋아질 거예요"), read_q("추워졌어요"), read_q("맛있어졌어요"), read_q("빨라지다")]
    ),
)

# ================================================================== Grammar B: -(으)ㄴ데/는데
_ND_ACT = [("먹다", "to eat"), ("가다", "to go"), ("보다", "to see; to watch"), ("오다", "to come"), ("하다", "to do"), ("놀다", "to play; to have fun"), ("있다", "to exist; to have"), ("없다", "to not exist; to not have"), ("맛있다", "to be delicious"), ("재미있다", "to be fun")]
_ND_STA = [("크다", "to be big"), ("흐리다", "to be cloudy"), ("좋다", "to be good"), ("넓다", "to be wide"), ("춥다", "to be cold"), ("길다", "to be long"), ("많다", "to be many"), ("따뜻하다", "to be warm"), ("바쁘다", "to be busy"), ("어렵다", "to be difficult")]
_ND_EX = [
    ("날씨가 좋은데 산책합시다.", "The weather is good, so let’s take a walk."), ("날씨가 좋은데 집에 있을 거예요?", "The weather is good, but are you going to stay home?"),
    ("백화점에 가는데 부탁할 것 있어요?", "I’m going to the department store; do you need anything?"), ("이 옷이 좀 큰데 작은 것 있어요?", "These clothes are a little too big; do you have a smaller size?"),
    ("날씨가 좋은데 피크닉 갈까요?", "The weather is nice; shall we go on a picnic?"), ("겨울인데 날씨가 따뜻해요.", "It is winter, but the weather is warm."),
    ("날씨는 따뜻한데, 바람이 많이 불어요.", "The weather is warm, but the wind blows a lot. (the book’s example in the Core Vocabulary)"), ("어제 샌프란시스코에 갔다 왔는데, 아주 재미있었어요.", "I went to San Francisco yesterday, and it was very fun. (the book’s example in the Core Vocabulary)"),
    (f"어제는 최고 기온이 영하 일 도였는데 오늘은 영상 오 도예요.", "Yesterday the highest temperature was 1 degree below zero, but today it is 5 degrees above zero. (from Topic B)"),
]
_ND_PH = [("우체국에 가다", "우체국에 가는데"), ("내일이 토요일이다", "내일이 토요일인데"), ("주말에 쇼핑하다", "주말에 쇼핑하는데"), ("날씨가 좋다", "날씨가 좋은데"), ("운동을 하다", "운동을 하는데"), ("아침에 눈이 왔다", "아침에 눈이 왔는데"), ("내일 골프를 치다", "내일 골프를 치는데"), ("판문점에 가고 싶다", "판문점에 가고 싶은데"), ("어제 한국 음식을 먹었다", "어제 한국 음식을 먹었는데")]
_ND_N = [("겨울", "겨울인데"), ("토요일", "토요일인데"), ("주말", "주말인데"), ("학생", "학생인데")]
_ND_PAST = lambda v: past(v) + "는데"


def _nd_wrong(v, action):
    right = _nde(v, action)
    st = stem(v)
    cands = [st + "는데", st + "은데", st + "ㄴ데", if_(v), st + "고"]
    return list(dict.fromkeys(c for c in [st + "는데", st + "은데", st[:-1] + _K.compose(*_K.decompose(st[-1])[:2], "ㄴ") + "데", st + "지만"] if c != right))[:3]


L7 = lesson(
    "Ch 15 · Grammar B: background with -(으)ㄴ데/는데",
    "날씨가 좋은데 · 백화점에 가는데 · 이 옷이 큰데 · 겨울인데 · 갔는데",
    requires=[],
    cards=[
        card("The conjunctive ending -(으)ㄴ데/는데",
             "The conjunctive ending -(으)ㄴ데/는데 is unique in its usage. This conjunctive ending signals that the first clause is background information for (or the situation or circumstance leading to) the second clause. Therefore, we can only interpret the meaning of this conjunctive ending according to the content of the second clause. For example: 날씨가 좋은데 산책합시다 (The weather is good, so let’s take a walk); 날씨가 좋은데 집에 있을 거예요? (The weather is good, but are you going to stay home?).\n\n"
             "Note that the same conjunctive ending is interpreted differently according to how it relates to the content of the following clause. It is interpreted as so in the first sentence and as but in the second sentence. -(으)ㄴ데/는데 can also be interpreted to mean and, and thus, and then, however, or nevertheless in other contexts. Thus, from the listener’s perspective, the exact meaning of the first clause cannot be determined until the second clause is heard. For this reason, the conjunctive ending is often used as (1) an attention getter and as (2) a stage setter for the main idea the speaker is about to deliver. As a result, this conjunctive ending is used almost exclusively in speaking.",
             tables=[table(["Condition", "Rule", "Example"], [["Action verbs", "add 는데", "먹다 → 먹는데; 가다 → 가는데"], ["When the stem of a stative verb ends in a vowel", "add ㄴ데", "크다 → 큰데; 흐리다 → 흐린데"], ["When the stem of a stative verb ends in a consonant", "add 은데", "좋다 → 좋은데; 넓다 → 넓은데"]], title="action verb stem + 는데; stative verb stem + (으)ㄴ데")],
             examples=[D(a, b) for a, b in _ND_EX[:2]]),
        card("More examples",
             "The book’s further examples, and the two examples of the Core Vocabulary and the sentence of Topic B (the English is the book’s where the book gives it, otherwise mine).",
             examples=[D(a, b) for a, b in _ND_EX[2:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule. 있다 and 없다 (and 맛있다, 재미있다) take 는데 like action verbs (mine: this is the usual form but the book’s rule table does not say it); stems ending in ㄹ drop it before ㄴ (놀다 → 노는데, 길다 → 긴데); the ㅂ irregular verbs change ㅂ to 우 (춥다 → 추운데, 어렵다 → 어려운데). The past form adds -았/었 before -는데 for every kind of verb (갔는데, 좋았는데).",
             tables=[table(["Dictionary form", "Meaning", "-는데 / -(으)ㄴ데", "Past (-았/었는데)"], [[v, m, _nde(v, True), _ND_PAST(v)] for v, m in _ND_ACT] + [[v, m, _nde(v, False), _ND_PAST(v)] for v, m in _ND_STA], say=[0, 2, 3])]),
        card("After a noun: -인데",
             "After a noun the copula 이다 is used: 겨울인데 날씨가 따뜻해요 (It is winter, but the weather is warm). The book’s Follow-up 4 phrase 내일이 토요일이다 becomes 내일이 토요일인데. The table is mine.",
             tables=[table(["Noun", "Noun + 인데"], [list(r) for r in _ND_N], say=[0, 1])]),
        card("Follow-up 4: change the phrase with -(으)ㄴ데/는데",
             "In the book Partner A reads a verbal phrase, Partner B changes it with -(으)ㄴ데/는데 and Partner A adds information to make a meaningful sentence. The book’s model: A: 길이 막히다; B: 길이 막히는데; A: 길이 막히는데 지하철을 탈까요? (The roads are congested; shall we take the subway?) The changed phrases for the nine phrases of the book are mine.",
             tables=[table(["Phrase (the book)", "With -(으)ㄴ데/는데 (mine)"], [list(r) for r in _ND_PH], say=[0, 1])],
             examples=[D("길이 막히는데 지하철을 탈까요?", "The roads are congested; shall we take the subway?")]),
        card("Follow-up 5: 보고 싶은 영화가 있는데 …",
             "In the book you think of an activity you would like to do this weekend, list at least two, and ask classmates to join you with -(으)ㄴ데/는데. The book’s model (the English is mine):",
             examples=[D("보고 싶은 영화가 있는데 같이 영화 보러 갑시다.", "There is a movie that I want to see; let’s go to see it together."), D("보고 싶은 영화가 있는데 같이 영화 보러 갈까요?", "There is a movie that I want to see; shall we go to see it together?")]),
        card("Activities left out",
             "Follow-up 3 (listening to three conversations, transcribing the first clause with -(으)ㄴ데/는데 and translating the sentence) is an audio activity; in Follow-up 5 the list of your own activities and the walk around the room are class activities."),
    ],
    exercises=uniq(
        [M(f"Which is the -는데 form of {v} ({m})?", _nde(v, True), _nd_wrong(v, True), f"{v}: action verb → {_nde(v, True)}.") for v, m in _ND_ACT]
        + [M(f"Which is the -(으)ㄴ데 form of {v} ({m})?", _nde(v, False), _nd_wrong(v, False), f"{v}: stative verb → {_nde(v, False)}.") for v, m in _ND_STA]
        + [M(f"Which is the past form of {v} with -는데?", _ND_PAST(v), [x for x in dict.fromkeys([_nde(v, v in dict(_ND_ACT)), stem(v) + "는데", stem(v) + "았는데", stem(v) + "었는데"]) if x != _ND_PAST(v)][:3], f"{v} → {_ND_PAST(v)}.") for v, m in (_ND_ACT[:5] + _ND_STA[:4])]
        + _tr(_ND_EX + [("길이 막히는데 지하철을 탈까요?", "The roads are congested; shall we take the subway?")])
        + [M(f"Change “{a}” with -(으)ㄴ데/는데.", b, [x for _, x in _ND_PH if x != b][:3], f"{a} → {b}.") for a, b in _ND_PH]
        + [F("백화점에 가___ 부탁할 것 있어요? (I’m going; background)", "는데", ["은데", "인데"], "가다 is an action verb: 가는데."), F("날씨가 좋___ 산책합시다. (the weather is good)", "은데", ["는데", "ㄴ데"], "좋다 ends in a consonant: 좋은데."), F("이 옷이 좀 크___ 작은 것 있어요? (is a little too big)", "ㄴ데", ["는데", "은데"], "크다 ends in a vowel: 큰데."),
           F("겨울___ 날씨가 따뜻해요. (it is winter, but)", "인데", ["는데", "은데"], "A noun takes 인데."), F("어제 샌프란시스코에 갔다 왔___ 아주 재미있었어요. (I went and)", "는데", ["은데", "ㄴ데"], "The past stem 왔 + 는데."),
           F("어제는 최고 기온이 영하 일 도였___ 오늘은 영상 오 도예요. (but)", "는데", ["은데", "ㄴ데"], "The past of 이다: 였 + 는데."), F("날씨가 좋은데 피크닉 ___? (shall we go)", "갈까요", ["갑니다", "갔어요"], "A suggestion follows the background."),
           M("What does -(으)ㄴ데/는데 signal?", "That the first clause is background information for the second clause", ["That the action is finished", "That the first clause is the reason only", "That a wish follows"], "It sets the stage for the second clause."), M("How can -(으)ㄴ데/는데 be translated?", "so; but; and; however", ["only “because”", "only “if”", "only “in order to”"], "The meaning depends on the second clause."),
           M("In which situation is -(으)ㄴ데/는데 used almost exclusively?", "In speaking", ["In newspapers", "In laws", "In textbooks"], "It is used almost exclusively in speaking."), M("Which ending follows an action verb?", "는데", ["은데", "ㄴ데", "인데"], "먹다 → 먹는데."),
           M("Which ending follows a stative verb stem that ends in a consonant?", "은데", ["는데", "ㄴ데", "인데"], "좋다 → 좋은데."), M("Which ending follows a stative verb stem that ends in a vowel?", "ㄴ데", ["는데", "은데", "인데"], "크다 → 큰데."),
           read_q("날씨가 좋은데"), read_q("백화점에 가는데"), read_q("이 옷이 좀 큰데"), read_q("겨울인데"), read_q("길이 막히는데")]
    ),
)

# ================================================================== Topic C
_C_TXT = [
    ("주말에 판문점을 방문했다.", "I visited Panmunjom over the weekend."),
    ("한국인과 외국인 관광객이 많이 있었다.", "There were many Korean and foreign tourists."),
    ("판문점의 공식적인 이름은 판문점 공동경비구역이다.", "The official name of Panmunjom is Panmunjom Joint Security Area."),
    ("판문점에는 인상적인 건물이 많았다.", "There were many impressive buildings at Panmunjom."),
    ("판문점 가운데에는 파란색 일 층 건물들이 있었다.", "In the middle of Panmunjom there were blue one-story buildings."),
    ("건물 주변에는 한국군과 북한군이 서 있었다.", "Around the buildings, South Korean and North Korean soldiers were standing."),
    ("건물들은 오래되고 창문이 많았다.", "The buildings were old and had many windows."),
    ("건물 안 회의실에는 크고 긴 테이블이 있었고 의자가 많이 있었다.", "In the conference room inside the building there was a big, long table and there were many chairs."),
    ("판문점의 남쪽에는 자유의 집과 평화의 집이 있었다.", "In the south of Panmunjom there were Freedom House and Peace House."),
    ("북쪽에는 판문각과 통일각이 있었다.", "In the north there were Panmun-gak and Tongil-gak."),
    ("그렇지만 북쪽은 가고 싶어도 갈 수 없었다.", "But I could not go to the north even though I wanted to."),
    ("그래서 자유의 집에서 사진만 찍었다.", "So I only took pictures at Freedom House."),
]
_C_WORDS = ["가운데", "공식(적)", "관광객", "(국)기", "대표", "-아/어도", "안내원", "~에게서 / 한테서", "오래되다", "외국인", "인상(적)", "자유", "주변", "찍다", "판문점", "공동경비구역", "평화", "휴전선", "회의실"]
_JSA = [("판문점 공동경비구역", "Panmunjom Joint Security Area"), ("통일각", "Tongil-gak"), ("판문각", "Panmun-gak"), ("군사 정전 위원회", "Military Armistice Commission"), ("자유의 집", "Freedom House"), ("평화의 집", "Peace House"),
        ("군사분계선", "MDL (Military Demarcation Line)"), ("중립국 감시 위원회", "Neutral Nations Supervisory Commission")]
L8 = lesson(
    "Ch 15 · Topic C: I have visited Panmunjom",
    "판문점에 갔다 왔다 · 공동경비구역 · 자유의 집 · 평화의 집 · 휴전선 · 군사분계선",
    requires=[],
    cards=[
        card("Topic C: I have visited Panmunjom (판문점에 갔다 왔다)",
             "The following text is from SPC Anderson’s journal about his weekend visit to the Joint Security Area (JSA) in the Demilitarized Zone (DMZ). It is written in the formal blunt speech style (-다), which is taught later in this chapter. (The English is mine; the book gives none. The book writes 1층, spelled 일 층 here.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("The Joint Security Area: the words of the diagram",
             "The book shows a diagram of the Panmunjom Joint Security Area with these labels (the English is the book’s).",
             tables=[ktable(_JSA)]),
        card("Cultural notes",
             "Panmunjom is a portion of the Korean Demilitarized Zone (DMZ), and includes an 800-square-meter area designated as a Joint Security Area (JSA) by the UN and North Korea. Panmunjom is also called the “Truce Village” by the media. This area is outside administrative control of both South and North Korea, but is often used for diplomatic engagements between the two countries. Currently the UN and North Korea each operate six guard posts in the JSA and 35 security guards reside there. South and North Korean forces stand face-to-face in this area but cannot enter each other’s territory."),
        card("Presentation Activity: the vocabulary table",
             "The book gives a vocabulary table with half of the words missing and asks you to complete it with the Korean or the English word: 판문점 (Panmunjom), 공동경비구역 (Joint Security Area), 관광객 (a tourist), 주변 (surrounding; around), -아/어도 (although; even if), 가운데 (the middle), 회의실 (a conference room), 오래되다 (to be old), 인상적 (impressive), 공식적 (formal; official), 외국인 (a foreigner), 자유 (freedom), 찍다 (to take a picture) and 평화 (peace). The words are in the table above and in the exercises of this lesson."),
        card("Activities left out",
             "The SMART Board activity and the dialog of Follow-up 1 (a dialog between SPC Anderson and SPC Park on the SMART Board), the tour guide’s explanations of Follow-up 2a (listening and matching them to three pictures), the picture of 평화의 집 in Follow-up 2b (writing at least three Korean sentences about the building and its surroundings) and the Useful Link (Panmunjom) are audio, picture, game or website activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith(("~", "-", "("))] ))
        + _tr(_C_TXT) + _tr(_JSA)
        + [M("Where did SPC Anderson go for the weekend?", "Panmunjom", ["Mount Seorak", "Jeju Island", "The War Memorial"], "주말에 판문점을 방문했다."), M("Who was at Panmunjom?", "Many Korean and foreign tourists", ["Only soldiers", "Nobody", "Only guides"], "한국인과 외국인 관광객이 많이 있었다."),
           M("What is the official name of Panmunjom?", "Panmunjom Joint Security Area", ["Truce Village only", "The Blue House", "The DMZ"], "판문점 공동경비구역."), M("What color were the buildings in the middle?", "Blue", ["White", "Red", "Green"], "파란색 일 층 건물들."),
           M("Who was standing around the buildings?", "South Korean and North Korean soldiers", ["Tourists", "Guides", "Nobody"], "한국군과 북한군이 서 있었다."), M("What was in the conference room?", "A big, long table and many chairs", ["A map", "A flag", "A tank"], "크고 긴 테이블이 있었고 의자가 많이 있었다."),
           M("What was in the south of Panmunjom?", "Freedom House and Peace House", ["Panmun-gak and Tongil-gak", "A beach", "A hotel"], "남쪽에는 자유의 집과 평화의 집."), M("What was in the north of Panmunjom?", "Panmun-gak and Tongil-gak", ["Freedom House and Peace House", "A beach", "A hotel"], "북쪽에는 판문각과 통일각."),
           M("Why did Anderson take pictures only at Freedom House?", "He could not go to the north although he wanted to", ["He had no camera", "The north was closed for repairs", "He did not like the north"], "북쪽은 가고 싶어도 갈 수 없었다."), M("What is Panmunjom called by the media?", "The “Truce Village”", ["The “Blue House”", "The “Peace Village”", "The “Iron Gate”"], "Panmunjom is also called the “Truce Village”."),
           M("How many guard posts does each of the UN and North Korea operate in the JSA?", "Six", ["Two", "Twelve", "Thirty-five"], "each operate six guard posts."), M("How many security guards reside in the JSA?", "35", ["6", "800", "12"], "35 security guards reside there."),
           F("판문점의 ___ 이름은 판문점 공동경비구역이다. (official)", "공식적인", ["인상적인", "오래된"], "공식적 = formal; official."), F("판문점에는 ___ 건물이 많았다. (impressive)", "인상적인", ["공식적인", "오래된"], "인상적 = impressive."), F("건물들은 ___고 창문이 많았다. (old)", "오래되", ["아름답", "크"], "오래되다 = to be old (for objects)."),
           F("건물 ___에는 한국군과 북한군이 서 있었다. (around)", "주변", ["가운데", "안"], "주변 = surrounding; around."), F("판문점 ___에는 파란색 일 층 건물들이 있었다. (in the middle)", "가운데", ["주변", "남쪽"], "가운데 = the middle."), F("건물 안 ___에는 크고 긴 테이블이 있었다. (conference room)", "회의실", ["안내원", "관광객"], "회의실 = a conference room."),
           F("그래서 자유의 집에서 사진만 ___. (took)", "찍었다", ["찍는다", "찍을까"], "찍다 = to take (a photograph)."), F("한국인과 외국인 ___이 많이 있었다. (tourists)", "관광객", ["안내원", "대표"], "관광객 = a tourist."),
           read_q("판문점"), read_q("자유의 집"), read_q("평화의 집"), read_q("공동경비구역"), read_q("군사분계선")]
    ),
)

# ================================================================== Grammar C: -아/어도
_DO_V = [("좋다", "to be good"), ("오다", "to come"), ("멀다", "to be far"), ("맵다", "to be spicy"), ("춥다", "to be cold"), ("피곤하다", "to be tired"), ("바쁘다", "to be busy"), ("많다", "to be many"), ("먹다", "to eat"), ("가다", "to go"), ("있다", "to exist; to have"), ("어렵다", "to be difficult"), ("비싸다", "to be expensive"), ("크다", "to be big")]
_DO_EX = [
    ("한국말이 어려워도 배우겠습니다.", "I will learn Korean (even) though it is difficult. / I will learn Korean even if it is difficult."), ("오늘 날씨가 좋아도 집에 있습니다.", "Though the weather is good today, I am staying home."),
    ("내일 날씨가 좋아도 집에 있겠습니다.", "Even if the weather is good tomorrow, I will stay home."), ("김치가 매워도 아주 맛있어요.", "Although kimchi is spicy, it is very delicious."),
    ("체육관이 멀어도 그냥 걸어갔어요.", "I just walked to the gym, although it was far."), ("이번 토요일에 비가 와도 등산을 가고 싶어요.", "I’d like to go hiking even if it rains this Saturday."),
    ("제가 지금 가도 돼요?", "May I go now?"), ("제가 지금 가도 괜찮아요?", "May I go now?"), ("제가 지금 가도 좋아요?", "May I go now?"),
    ("지난번 여행은 힘들었어도 정말 재미있었어요.", "Although the last trip was hard, it was really fun. (the book’s example in the Core Vocabulary; English mine)"),
]
_DO_FU = [("날씨가 춥습니다", "날씨가 추워도", "날씨가 추워도 등산을 가겠습니다.", "Even if the weather is cold, I will go hiking."), ("피곤합니다", "피곤해도", "피곤해도 숙제를 해야 합니다.", "Even if I am tired, I have to do my homework."), ("주말입니다", "주말이어도", "주말이어도 학교에 갑니다.", "Even though it is the weekend, I go to school."),
          ("청소를 합니다", "청소를 해도", "청소를 해도 방이 더럽습니다.", "Even if I clean, the room is dirty."), ("친구가 많습니다", "친구가 많아도", "친구가 많아도 같이 갈 사람이 없어요.", "Even though I have many friends, there is nobody to go with.")]


def _do(v):
    return _ao(v) + "도"


def _do_wrong(v):
    right = _do(v)
    st = stem(v)
    return list(dict.fromkeys(c for c in (st + "아도", st + "어도", st + "도", _ao(v) + "서") if c != right))[:3]


L9 = lesson(
    "Ch 15 · Grammar C: although and even if with -아/어도",
    "어려워도 · 좋아도 · 매워도 · 멀어도 · 비가 와도 · 가도 돼요?",
    requires=[],
    cards=[
        card("The conjunctive ending -아/어도",
             "Consider the English sentences “I will learn Korean (even) though it is difficult” and “I will learn Korean even if it is difficult.” In the first sentence, the speaker knows that Korean is difficult but will learn it despite its being difficult. In the second sentence, however, the speaker does not know definitely whether or not Korean is difficult but will learn it in any event. Thus, (even) though expresses a concession and even if is a conditional.\n\n"
             "The conjunctive ending -아/어도 is used to express both (even) though and even if. Therefore, we can express the two English sentences by using the same Korean sentence: 한국말이 어려워도 배우겠습니다. If we hear this sentence out of context, we can interpret the sentence in both ways. When a context is given, however, the meaning of the conjunctive ending is either (even) though or even if, but not both. For example:",
             examples=[D(a, b) for a, b in _DO_EX[1:3]]),
        card("Time words show which meaning",
             "Note that both sentences have a time reference (오늘 or 내일). Thus, we know that the conjunctive ending in the first sentence is understood as a concession (though or although), whereas the same conjunctive ending in the second sentence is understood as a conditional (even if).",
             tables=[table(["Condition", "Rule", "Example"], [["When the last syllable of a verb stem contains the vowels ㅏ or ㅗ", "add 아도", "좋다 → 좋아도; 오다 → 오 + 아도 → 와도"], ["When the last syllable of a verb stem contains a vowel other than ㅏ or ㅗ", "add 어도", "멀다 → 멀어도; 맵다 → 매우 + 어도 → 매워도"]], title="verb stem + 아/어도")],
             examples=[D(a, b) for a, b in _DO_EX[3:6]]),
        card("The same ending in 아/어도 되다 (permission)",
             "You may now understand that the set pattern of -아/어도 되다 for permission (Chapter 12) is from the same conjunctive ending.",
             examples=[D(a, b) for a, b in _DO_EX[6:9]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule (the vowel contraction is the same as with -아/어요; the ㅂ irregular verbs change ㅂ to 우: 춥다 → 추워도, 어렵다 → 어려워도). The past form puts -았/었 before -어도: 힘들었어도 (the book’s example in the Core Vocabulary).",
             tables=[table(["Dictionary form", "Meaning", "-아/어도", "Past (-았/었어도)"], [[v, m, _do(v), past(v) + "어도"] for v, m in _DO_V], say=[0, 2, 3])],
             examples=[D(*_DO_EX[9])]),
        card("Follow-up 1: rewrite with -아/어도 and add a main clause",
             "The book gives five clauses (날씨가 춥습니다, 피곤합니다, 주말입니다, 청소를 합니다, 친구가 많습니다); you rewrite each with -아/어도 and write a second clause of your own. The rewritten clauses and the sample sentences are mine (after the noun + 이다 the form is 이어도, 주말이어도).",
             tables=[table(["Clause (the book)", "With -아/어도", "A sample sentence", "Meaning"], [list(r) for r in _DO_FU], say=[0, 1, 2])]),
        card("Activities left out",
             "Follow-up 2 (listening to four conversations and translating the sentences that use -아/어도) is an audio activity."),
    ],
    exercises=uniq(
        [M(f"Which is the -아/어도 form of {v} ({m})?", _do(v), _do_wrong(v), f"{v} → {_do(v)}.") for v, m in _DO_V]
        + [M(f"Which is the past form of {v} with -아/어도?", past(v) + "어도", [x for x in dict.fromkeys([_do(v), stem(v) + "었어도", stem(v) + "아도", past(v) + "서"]) if x != past(v) + "어도"][:3], f"{v} → {past(v)}어도.") for v, m in _DO_V[:8]]
        + _tr(_DO_EX[1:6] + [_DO_EX[6], _DO_EX[9]] + [(c, d) for a, b, c, d in _DO_FU])
        + [F("한국말이 어려___ 배우겠습니다. (even though)", "워도", ["어도", "아도"], "어렵다 (ㅂ irregular) → 어려워도."), F("김치가 매___ 아주 맛있어요. (although)", "워도", ["어도", "아도"], "맵다 → 매워도."), F("체육관이 멀___ 그냥 걸어갔어요. (although)", "어도", ["아도", "워도"], "멀다 → 멀어도."),
           F("이번 토요일에 비가 ___ 등산을 가고 싶어요. (even if)", "와도", ["오도", "와서"], "오다 → 오 + 아도 → 와도."), F("오늘 날씨가 좋___ 집에 있습니다. (though)", "아도", ["어도", "은데"], "좋다: last vowel ㅗ → 좋아도."), F("제가 지금 가___ 돼요? (may I)", "도", ["면", "서"], "-아/어도 되다 = may."),
           F("지난번 여행은 힘들었___ 정말 재미있었어요. (although)", "어도", ["아도", "으니까"], "힘들었 + 어도."), F("피곤___ 숙제를 해야 합니다. (even if I am tired)", "해도", ["하면", "해서"], "피곤하다 → 피곤해도."),
           F("내일 날씨가 좋아도 집에 ___. (I will stay)", "있겠습니다", ["있습니다", "있었습니다"], "내일 = tomorrow: 있겠습니다."),
           M("Which two meanings does -아/어도 express?", "(Even) though and even if", ["Because and so", "If and when", "In order to and for"], "-아/어도 expresses both."), M("How do you know whether -아/어도 means “though” or “even if”?", "By the context, such as a time word", ["By the verb ending", "By the speaker’s age", "It cannot be known"], "오늘 → though; 내일 → even if."),
           M("Which verb stem takes 아도?", "좋다", ["멀다", "먹다", "길다"], "The last vowel ㅗ takes 아도."), M("Which verb stem takes 어도?", "멀다", ["좋다", "가다", "많다"], "The last vowel ㅓ takes 어도."), M("What is 오다 + -아/어도?", "와도", ["오아도", "오어도", "오도"], "오 + 아도 → 와도."),
           M("What is 맵다 + -아/어도?", "매워도", ["맵어도", "맵아도", "매우도"], "맵다 → 매우 + 어도 → 매워도."), M("-아/어도 되다 expresses …", "permission", ["a reason", "a wish", "a past event"], "제가 지금 가도 돼요? = May I go now?"),
           read_q("어려워도"), read_q("비가 와도"), read_q("매워도"), read_q("가도 돼요"), read_q("추워도")]
    ),
)

# ================================================================== Grammar D: the formal blunt style
_FB_V = [("먹다", "to eat", True), ("찾다", "to look for", True), ("가다", "to go", True), ("돌아오다", "to return", True), ("읽다", "to read", True), ("쓰다", "to write; to use", True), ("자다", "to sleep", True), ("좋아하다", "to like", True),
         ("예쁘다", "to be pretty", False), ("춥다", "to be cold", False), ("많다", "to be many", False), ("크다", "to be big", False), ("있다", "to exist; to have", False), ("없다", "to not exist; to not have", False), ("재미있다", "to be fun", False), ("힘들다", "to be hard", False)]
_FB_EX = [("우리 가족은 저녁을 늘 같이 먹는다.", "My family always eats dinner together."), ("나는 아침마다 지하철로 학교에 간다.", "Every morning, I go to school by subway."), ("이번 주는 날씨가 춥다.", "This week the weather is cold."),
          ("우리 가족은 저녁을 늘 같이 먹었다.", "My family always ate dinner together."), ("어제는 따뜻했다.", "It was warm yesterday."), ("준호는 이제 대학생이다.", "Junho is a college student now."), ("우리 고향에는 산이 있다.", "There are mountains in my hometown.")]
_FB_T = [("입다", True), ("읽다", True), ("쓰다", True), ("좋아하다", True), ("자다", True), ("많다", False), ("재미있다", False), ("힘들다", False)]
_FB_MODEL = [("나라 식당은 한국 식당이다.", "Nara Restaurant is a Korean restaurant."), ("이 식당은 몬트레이 시내에 있다.", "This restaurant is in downtown Monterey.")]
_FB_STY = [("-ㅂ니다 / 습니다", "Formal speech style", "먹습니다"), ("-아요 / 어요", "Informal speech style", "먹어요"), ("-아 / 어", "Informal blunt speech style", "먹어"), ("-ㄴ다 / 는다 / 다", "Formal blunt speech style", "먹는다")]
L10 = lesson(
    "Ch 15 · Grammar D: the formal blunt speech style -ㄴ다/는다/다",
    "먹는다 · 간다 · 춥다 · 먹었다 · 대학생이다 · 산이 있다 · 일기 (journals)",
    requires=[],
    cards=[
        card("The fourth speech style: formal blunt",
             "So far, you have learned about three different speech styles and their verb endings: 1. -ㅂ니다/습니다 (Formal Speech Style); 2. -아요/어요 (Informal Speech Style); 3. -아/어 (Informal Blunt Speech Style). Now you will learn a fourth: the Formal Blunt Speech Style,¹ which is indicated by the verb ending -ㄴ다/는다/다. As its name suggests, this style is used in formal and “blunt” settings. In written language, this speech style is typically employed in newspapers, journals, and books. In spoken language, this speech style is used among friends or by those of a higher status in age or rank.\n\n¹ This style is also known as Formal Intimate, Formal Non-polite, or Formal Plain Speech Style.",
             tables=[table(["Ending", "Style", "Example (먹다), mine"], [list(r) for r in _FB_STY])]),
        card("The rule",
             "Action verbs take -ㄴ다/는다 and stative verbs take -다. The verbs 있다, 없다, 이다 and 아니다 act like stative verbs when they are conjugated into the formal blunt speech style (준호는 이제 대학생이다; 우리 고향에는 산이 있다).",
             tables=[table(["Condition", "Rule", "Example"], [["When an action verb stem ends in a consonant", "add 는다", "먹다 → 먹는다; 찾다 → 찾는다"], ["When an action verb stem ends in a vowel", "add ㄴ다", "가다 → 간다; 돌아오다 → 돌아온다"], ["When a stative verb stem ends in a consonant or a vowel", "add 다", "예쁘다 → 예쁘다; 춥다 → 춥다"], ["이다", "이다", "이다 → 이다"]], title="action verb stem + ㄴ다/는다; stative verb stem + 다")],
             examples=[D(a, b) for a, b in _FB_EX[:3]]),
        card("The past tense and more examples",
             "The formal blunt speech style in the past tense is -았다/었다.",
             examples=[D(a, b) for a, b in _FB_EX[3:]]),
        card("Forms",
             "The forms below are mine, made by the book’s rule (the past stem + 다: 먹었다, 갔다, 추웠다).",
             tables=[table(["Dictionary form", "Meaning", "Present blunt", "Past blunt"], [[v, m, _blunt(v, a), past(v) + "다"] for v, m, a in _FB_V], say=[0, 2, 3])]),
        card("Follow-up 3: fill in the table with correct verb endings",
             "The book gives eight dictionary forms; some forms are filled in for you (입었다, 읽는다, 좋아한다, 잤다, 재미있다, 힘들었다). The complete table below is mine.",
             tables=[table(["Dictionary form", "Present blunt form", "Past blunt form"], [[v, _blunt(v, a), past(v) + "다"] for v, a in _FB_T], say=[0, 1, 2])]),
        card("Follow-up 5: a restaurant review in the formal blunt style",
             "In the book you write a review of your favorite restaurant on a blog in the formal blunt speech style, including its specialty, price range, taste and other information. The book’s model (the English is mine):",
             examples=[D(a, b) for a, b in _FB_MODEL]),
        card("Activities left out",
             "Follow-up 4 (a “chain” story written together with classmates: each student begins a story with a sentence in the formal blunt style, trades papers and adds sentences until there are six), the information table, the flip chart, posting and the pair talk of Follow-up 5 are class activities.\n\n"
             "The chapter’s Activities: Activity 1 (a SMART Board activity and listening to three conversations of a man looking for a building, filling in the building and its description in English), Activity 2 (A1Cs Capano and Jackson’s postcards from the DMZ visit, read by two groups, drawn as pictures, described in Korean and the recommendations answered; the postcards themselves are not printed in the Student’s Edition) and Activity 3 (a SMART Board speaking and listening picture activity, 집이 어떻게 생겼습니까? “What does the house look like?”) are audio, picture, game or class activities."),
    ],
    exercises=uniq(
        [M(f"Which is the present formal blunt form of {v} ({m})?", _blunt(v, a), [x for x in dict.fromkeys([stem(v) + "는다", stem(v) + "다", stem(v) + "ㄴ다", formal(v), informal(v) if v not in _IRR else _ao(v) + "요"]) if x != _blunt(v, a)][:3], f"{v}: {'action verb' if a else 'stative verb'} → {_blunt(v, a)}.") for v, m, a in _FB_V]
        + [M(f"Which is the past formal blunt form of {v} ({m})?", past(v) + "다", [x for x in dict.fromkeys([_blunt(v, a), stem(v) + "았다", stem(v) + "었다", past(v) + "어요"]) if x != past(v) + "다"][:3], f"{v} → {past(v)}다.") for v, m, a in _FB_V[:10]]
        + _tr(_FB_EX + _FB_MODEL)
        + [F("우리 가족은 저녁을 늘 같이 먹___. (eats)", "는다", ["ㄴ다", "다"], "먹다 is an action verb ending in a consonant: 먹는다."), F("나는 아침마다 지하철로 학교에 ___. (go)", "간다", ["가는다", "가다"], "가다 is an action verb ending in a vowel: 간다."), F("이번 주는 날씨가 ___. (is cold)", "춥다", ["춥는다", "춥ㄴ다"], "Stative verbs take 다."),
           F("우리 가족은 저녁을 늘 같이 ___. (ate)", "먹었다", ["먹는다", "먹어요"], "Past blunt: 먹었다."), F("어제는 따뜻___. (it was)", "했다", ["하다", "한다"], "따뜻하다 → 따뜻했다."), F("준호는 이제 대학생___. (is)", "이다", ["인다", "이는다"], "이다 acts like a stative verb."),
           F("우리 고향에는 산이 ___. (there are)", "있다", ["있는다", "있ㄴ다"], "있다 acts like a stative verb: 있다."), F("나라 식당은 한국 식당___. (is)", "이다", ["인다", "이는다"], "noun + 이다."), F("이 식당은 몬트레이 시내에 ___. (is)", "있다", ["있는다", "있어요"], "있다 → 있다."),
           M("In which writings is the formal blunt style typically used?", "Newspapers, journals and books", ["Letters to a teacher", "Public announcements only", "Advertisements only"], "In written language: newspapers, journals, books."), M("Who uses the formal blunt style in speech?", "Friends, or those of a higher status in age or rank", ["Only children", "Only teachers to the president", "Shop clerks to customers"], "Used among friends or by those of higher status."),
           M("Which ending do action verbs that end in a consonant take?", "는다", ["ㄴ다", "다", "습니다"], "먹다 → 먹는다."), M("Which ending do action verbs that end in a vowel take?", "ㄴ다", ["는다", "다", "습니다"], "가다 → 간다."), M("Which ending do stative verbs take?", "다", ["는다", "ㄴ다", "어요"], "춥다 → 춥다."),
           M("Which verbs act like stative verbs in the formal blunt style?", "있다, 없다, 이다 and 아니다", ["Only 가다", "Only 먹다", "None of them"], "They act like stative verbs."), M("Which is the past formal blunt ending?", "-았다/었다", ["-는다", "-ㅂ니다", "-아요"], "어제는 따뜻했다."),
           M("Which is the formal blunt style of 쓰다 (to write)?", "쓴다", ["쓰는다", "쓰다", "써요"], "쓰다 ends in a vowel: 쓴다."), M("Which is the formal blunt style of 좋아하다?", "좋아한다", ["좋아하는다", "좋아하다", "좋아해요"], "하다 verb: 좋아한다."),
           read_q("먹는다"), read_q("간다"), read_q("춥다"), read_q("대학생이다"), read_q("어제는 따뜻했다")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_SECS = [("Geography", _CV_GEO), ("Temperature", _CV_TEMP), ("The Korean War", _CV_WAR), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for r in (_CV_GEO + _CV_WAR + _CV_LOAN + _CV_OTH) if not r[0].startswith(("~", "-", "(")) and "/" not in r[0]]
L11 = lesson(
    "Ch 15 · Core vocabulary and self-evaluation",
    "주요 단어 · 지리 · 기온 · 한국전쟁 · 외래어 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Optional parts, such as (~하다/되다), are kept in the meanings.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (9개 → 아홉 개, 90도 → 구십 도, 15° C and 86° F → 십오 도 씨 and 화씨 팔십육 도, 1950년 6월 25일 → 천구백오십년 유월 이십오일, 1964년 → 천구백육십사년, 155마일 → 백오십오 마일, 1층 → 일 층, L.A. → 엘에이, 워싱턴 D.C. → 워싱턴 디씨); the parentheses of the book’s 86° F and 30° C are left out. The book’s related words (the synonyms, antonyms and related words in the last column) are not repeated. The book’s Additional Vocabulary table is empty: it is for your own words."),
    ] + [card(name, "Italicized English words in the book are grammatical terms, not the meaning of a Korean word." if name == "Other words" else "", tables=[vt(rows)]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and locate provinces, major cities, well-known tourist attractions in Korea; talk about weather; comprehend basic information about the Korean War; comprehend basic information about the Joint Security Area and its facilities in Korea; describe a building in a simple paragraph.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -아/어지다, used to express changes of state or condition; the conjunctive ending -(으)ㄴ데/는데 (and; but; however); the conjunctive ending -아/어도 (even if; although); the formal blunt speech style verb ending; the Sino-Korean syllables 해 (海) and 부 (部)."),
    ],
    exercises=uniq(
        vocab_exercises([(r[0], _en(r[0])) for r in _CV_PLAIN])
        + [M("What does the Sino-Korean syllable 해 (海) mean?", "sea", ["part of an area", "a road", "a vehicle"], "해군, 동해, 서해, 남해."), M("What does the Sino-Korean syllable 부 (部) mean?", "part of an area; a region", ["sea", "a road", "a vehicle"], "동부, 서부, 남부, 북부, 중부."),
           M("What does -아/어지다 mean?", "to become", ["to be -ing", "because", "even if"], "비가 온 뒤에 날씨가 추워졌어요."), M("What does -아/어도 mean?", "(al)though; even if", ["to become", "because", "in order to"], "힘들었어도 재미있었어요."),
           M("What does -(으)ㄴ데/는데 mean?", "but; however; and", ["to become", "even if", "in order to"], "날씨는 따뜻한데, 바람이 많이 불어요."), M("What does ~에게서/한테서 mean?", "from (a person)", ["to (a person)", "with (a person)", "for (a person)"], "안내원에게서 설명을 들었습니다."),
           M("What does ~도 mean in 남한에는 아홉 개의 도가 있습니다?", "a province", ["a degree", "an island", "a road only"], "도 (道) = a province; a road; a way."), M("What does ~도 mean in 영상 오 도?", "degree (of temperature)", ["a province", "an island", "a way"], "도 = degree of temperature."),
           M("What does “(국)기” mean?", "a (national) flag", ["a country", "a memorial hall", "a tourist"], "태극기는 한국 국기입니다."), M("What does 일어나다 mean?", "to occur; to break out; to get up", ["to fight", "to take a photograph", "to be old"], "베트남 전쟁은 천구백육십사년에 일어났어요."),
           M("Which is the Korean name of the Korean War, meaning “June 25”?", "육이오", ["삼일절", "휴전선", "분단"], "육이오 = the Korean War; “June 25”."), M("Which word means “an armistice line”?", "휴전선", ["휴전", "전쟁", "분단"], "휴전선 = an armistice line; a truce line.")]
        + [read_q("주요 단어"), read_q("한반도"), read_q("판문점"), read_q("섭씨"), read_q("관광객")]
    ),
)

UNIT = unit("Semester 1 · Unit 4 · Chapter 15: The Korean Peninsula and the Korean War (한반도와 한국전쟁)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11])
