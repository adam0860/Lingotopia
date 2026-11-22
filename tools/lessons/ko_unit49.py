"""Unit 49: KBC Semester 2, Unit 11, Chapter 42 - Korean Culture II (한국의 문화 2).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 11, Student's Edition (2022).
Audio, video, pictures, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the grammar notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 42 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("가수", "(歌手) a singer", "제 동생은 노래를 좋아하고 가수가 되고 싶어합니다."),
    ("거리", "a street", "일요일에는 거리에 차가 적습니다."),
    ("고속철(도)/KTX", "(高速鐵(道)) a high-speed train / Korea Train eXpress; “high-speed rail”", "대전에 갈 때 고속철을 이용하면 아주 빨리 갈 수 있어서 편리합니다."),
    ("군함", "(軍艦) a warship; “military battleship”", "서해 앞바다에 북한의 군함이 나타났다고 합니다."),
    ("기지", "(基地) a (military) base, a station", "내 친구는 수원의 미군 공군기지에서 카투사로 근무하고 있어요."),
    ("대여", "(貸與) rental (to rent) (~하다)", "도서관에서 한국어 책도 대여해 줍니다."),
    ("민박", "(民泊) lodging at a private residence", "민박을 하면 호텔이나 여관보다 돈을 절약할 수 있어요."),
    ("벚꽃", "cherry blossoms; “cherry flower”", "하얀 벚꽃이 눈처럼 많이 떨어집니다."),
    ("불꽃놀이", "fireworks; “fire flower play”", "화재 위험 때문에 불꽃놀이를 금지하는 곳이 많아요."),
    ("사관학교", "(士官學校) a military academy; “cadet school”", "장교가 되고 싶어서 사관학교에 지원했습니다."),
    ("사정", "(事情) circumstances; a situation", "제가 갑자기 사정이 생겨서 내일 학교에 올 수 없습니다."),
    ("여관", "(旅館) a Korean-style inn; “travelers’ place”", "해수욕장 근처에 여관이 많습니다."),
    ("열다/열리다", "to hold (an event) / to be held", "다음 올림픽은 어디에서 열립니까?"),
    ("임시", "(臨時) temporary", "설날 연휴 동안 임시열차가 운행됩니다."),
    ("자가용", "(自家用) a privately owned car; “private use”", "기름값이 올라서 자가용을 운전하는 사람이 줄고 있어요."),
    ("전야제", "(前夜祭) an event on the eve (of a festival, etc.)", "대학 축제 전야제에 보통 유명한 가수를 초대합니다."),
    ("참고", "(參考) a reference (i.e. source of information); (to use as a reference; to refer to) (~하다)", "시험 공부를 할 때 이 책을 참고하세요."),
    ("킬로미터", "a kilometer; km", "집에서 학교까지 약 이십 킬로미터입니다."),
    ("퍼레이드", "a parade", "해군의 퍼레이드가 끝나면 가수들의 공연이 시작됩니다."),
    ("펜션", "a pension; a small European-style hotel; a vacation house", "이번 여름 휴가를 위해 바닷가에 있는 펜션을 예약했어요."),
    ("해(산)물", "(海(産)物) seafood; “things from the sea”", "서울에서는 싱싱한 해산물을 어디에서 살 수 있나요?"),
    ("현지", "(現地) the (actual) locale; the actual place", "엘에이에서 근무하는 직원이 현지의 날씨와 소식을 알려주었다."),
]
_CV_B = [
    ("골동품", "(骨董品) an antique", "아버지는 취미로 골동품을 사 모으신다."),
    ("데이트", "dating (to date) (~하다)", "주중에는 공부하느라고 바빠서 데이트할 시간도 없어요."),
    ("독특하다", "(獨特) to be unique; to be peculiar", "그 선물가게에는 독특한 물건이 많아서 자주 갑니다."),
    ("~로", "(路) street; boulevard", "오늘 저녁 열 시부터 종로와 을지로 사이 교통이 통제됩니다."),
    ("맛집", "a restaurant well known for tasty food; “taste house”", "다음번에 한국 여행을 할 때는 맛집을 여러 곳 가 보고 싶어요."),
    ("무명", "(無名) unknown; not famous; “no name”", "그 선수는 무명이었지만 금메달을 따면서 하루 아침에 유명해졌다."),
    ("무용가", "(舞踊家) an (artistic) dancer", "러시아 발레단에 한국인 무용가가 세 명 있어요."),
    ("사랑", "love (to love/to be loved) (~하다/받다)", "대학로는 예술을 사랑하는 사람들이 자주 가는 곳이다. 한국 영화가 전세계에서 많은 사랑을 받고 있다."),
    ("소극장", "(小劇場) a small-scale theater", "주말에 소극장에 연극을 보러 갈 예정이다."),
    ("연인", "(戀人) a lover; a person in a romantic relationship", "주말에 덕수궁 주변에서 연인들을 많이 볼 수 있다."),
    ("예술", "(藝術) art; “artistic skill”", "유럽에 여행가서 여러 나라의 예술을 감상했어요."),
    ("이색적", "(異色的) exotic; different; unique", "이 요리는 독특한 재료를 사용한 이색적인 맛이다."),
    ("젊은이", "a youth; a young person", "대학로에서 한 젊은이가 거리공연을 하고 있었다."),
    ("중심", "(中心) the center; the heart", "시내 중심에는 대형호텔들이 있습니다."),
    ("추억", "(追憶) memory; recollection; reminiscence", "이 찻집은 대학교 때의 추억이 많은 곳입니다."),
    ("카페", "a cafe", "친구와 카페에서 식사를 간단히 하고 술을 마셨어요."),
    ("평생", "(平生) a lifetime; one’s (whole) life", "사람은 평생 배워야 해요."),
    ("화가", "(畫家) a painter; “picture professional”", "프랑스 거리에는 그림을 그리는 화가들이 많습니다."),
    ("화랑/갤러리", "(畫廊) an art gallery; “picture gallery”", "몬트레이 남쪽 카멜에는 작은 화랑들이 많아요."),
]
_CV_C = [
    ("그네타기", "riding a swing", "초등학생들은 쉬는 시간에 운동장에서 그네타기를 많이 한다."),
    ("그립다", "to miss; to yearn for", "고향에 계신 할아버지 할머니가 그립습니다."),
    ("남다", "to be left; to remain", "점심때까지 두 시간 남았습니다."),
    ("널뛰기", "Korean seesaw; “plank jumping”", "민속공연장에서 널뛰기 공연을 합니다."),
    ("뜨다", "to rise (the sun/the moon/a star)", "여름에는 해가 일찍 뜹니다."),
    ("민속", "(民俗) folk; traditional", "어제 친구들과 민속 박물관에 갔습니다."),
    ("별", "a star", "오늘 밤에는 별이 아주 많습니다."),
    ("(보름)달", "the (full) moon", "보름달이 떠서 아주 밝습니다."),
    ("씨름", "traditional Korean wrestling", "씨름은 한국의 전통 스포츠입니다."),
    ("아쉽다", "to be left wanting; to have a sense of regret; to be a shame; to be a bummer", "작년에 한국에 갔을 때 제주도를 구경하지 못해서 아쉬웠어요."),
    ("연날리기", "kite flying", "오늘은 바람이 불어서 연날리기 좋은 날입니다."),
    ("오곡밥", "(五穀) a five-grain meal (that consists of rice, barley, millet, bean, and proso millet)", "오곡밥은 건강에 좋습니다."),
    ("장터", "(場) a marketplace", "장터에 사람들이 많아서 복잡합니다."),
    ("전시품", "(展示品) an exhibit; a floor sample", "민속 박물관에는 조선시대의 전시품이 많습니다."),
    ("~(적/식)으로", "an adverbial suffix / an adverb “maker”", "민속촌에서는 정기적으로 문화행사가 열립니다. 집을 현대식으로 고쳤습니다."),
    ("절", "a traditional Korean bow; a deep bow (~하다)", "전통혼례식에서 신랑신부가 서로 절을 합니다."),
    ("정월 대보름", "(正月 大) the day of the first full moon in the lunar year", "정월 대보름은 음력 일월 십오 일입니다."),
    ("조선시대", "(朝鮮時代) the Joseon Dynasty period", "창덕궁은 조선시대에 지어졌습니다."),
    ("줄타기", "tightrope walking; “rope riding”", "민속촌에서 줄타기 공연을 관람했습니다."),
    ("지다", "to set (the sun/the moon/a star)", "겨울에는 해가 일찍 집니다."),
    ("초가집", "(草家) a thatched-roof house; thatched house", "옛날 농촌 사람들은 보통 초가집에 살았습니다."),
    ("파전", "green onion pancake; scallion pancake", "우리 엄마는 파전을 맛있게 만드십니다."),
    ("해", "the sun", "오늘은 날씨가 흐려서 해가 잘 안 보입니다."),
    ("혼례", "(婚禮) a (traditional) wedding", "전통 혼례식에서는 신랑 신부가 한복을 입습니다."),
]
_CV_GR = [
    ("~뿐(만) 아니라 ~도", "not only … but also …", "벚꽃축제에는 가족들뿐만 아니라 연인들도 많이 옵니다."),
    ("–(으)ㄹ 수밖에 없다", "there is no choice but; cannot help -ing", "아들이 계속 취직시험에서 떨어지니 아버지가 화가 날 수밖에 없지요."),
    ("stative verbs interpreted as transitive verbs in English", "special verbs", "나는 고향에 계신 할머니가 그리워요."),
    ("~(적/식)으로", "an adverbial suffix / an adverb “maker”", "민속촌에서는 정기적으로 문화행사가 열립니다. 집을 현대식으로 고쳤습니다."),
]
_CV_SINO = [("해(산)물", "(海産物) seafood", "동해, 해군, 해상, 생산, 산모, 산지, 동물, 식물, 물품"), ("무명", "(無名) unknown; unnamed", "무료, 무관심, 무사고, 유명, 성명, 별명"), ("혼례", "(婚禮) a (traditional) wedding", "결혼, 약혼, 기혼, 예의, 예절, 예복"), ("민속촌", "(民俗村) a folk village", "국민, 주민, 시민, 풍속, 민속, 속담, 지구촌, 장수촌, 농촌")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"화랑": "an art gallery; “picture gallery”", "갤러리": "an art gallery", "먹거리": "food; things to eat (my gloss)", "민속놀이": "a folk game; a traditional game (my gloss)", "~로": "street; boulevard"}
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
_S1G = [("남해", "the South Sea"), ("해녀", "a female diver; “marine woman”"), ("해군", "navy; a sailor; “sea military”"), ("산모", "a woman who has recently given birth; “birth-giving mother”"), ("중국산", "Chinese products"), ("동물", "animal; “moving object”"), ("고물", "an antique; secondary goods; “old thing”")]
_S1 = [("농산물", "agricultural products; farm produce"), ("동해", "the East Sea"), ("지중해", "the Mediterranean Sea"), ("서해", "the West Sea; the Yellow Sea"), ("해상 도시", "a city on the sea; a floating city"), ("식물", "a plant"), ("물품", "goods; articles"), ("생산", "production"), ("산지", "a place of production; “producing place”")]
_S2G = [("무명 용사", "an unknown soldier; “nameless warrior”"), ("무명 작가", "an obscure writer; a nameless writer"), ("유료", "paid; with a charge"), ("무료", "free of charge"), ("유인", "manned"), ("무인", "unmanned"), ("유해", "hazardous"), ("무해", "nonhazardous"), ("성명", "one’s full name"), ("유명하다", "to be famous; “to have a name”")]
_S2 = [("무선 전화", "a wireless phone; a cordless phone"), ("인명", "a person’s name (not 人命, human life)"), ("무관심", "indifference; lack of interest"), ("가명", "an alias; a fake name"), ("무사고", "no accidents; accident-free"), ("명단", "a list of names; a roster")]
_S3G = [("이혼", "a divorce; “leaving one’s marriage”"), ("약혼", "an engagement; “promising a marriage”"), ("재혼", "a second marriage; a remarriage"), ("미혼", "single; unmarried; “not married”"), ("기혼", "married; “already married”"), ("경례", "salutation; a military salute; “respect with manners”"), ("예물", "a wedding gift; “ceremony object”")]
_S3 = [("결혼", "marriage; a wedding"), ("미혼모", "an unmarried mother"), ("기혼자", "a married person"), ("예절", "etiquette; manners"), ("예복", "formal dress; ceremonial clothes"), ("무례", "rudeness; a lack of manners")]
_S4G = [("국민", "a nation; a people; “people of a nation”"), ("시민", "a citizen; an inhabitant of a city"), ("민요", "a folk song"), ("속어", "slang; secular language"), ("산촌", "a mountain village"), ("강촌", "a riverside village"), ("부촌", "a rich village; a wealthy village")]
_S4 = [("군민", "county residents; people of a county"), ("도민", "residents of a province"), ("어촌", "a fishing village"), ("농촌", "a farming village; a rural village"), ("장수촌", "a longevity village; a village known for long-living people"), ("속담", "a proverb; a saying")]

# ================================================================== L1
L1 = lesson(
    "Ch 42 · What the chapter teaches, 해산물 · 무명 · 혼례 · 민속촌",
    "한국의 문화 · 해산물 · 무명 · 혼례 · 민속촌 · 축제 · 관광",
    requires=[],
    cards=[
        card("What Chapter 42 teaches (한국의 문화 2)",
             "Chapter 42, “Korean Culture II”, has a vocabulary builder, three topic presentations (festivals, tourist attractions, the Korean Folk Village) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and discuss tourist attractions, festivals, transportation, and lodging; identify and describe cultural events, including traditional weddings and folk games; provide directions to a location; and narrate a past event in a simple paragraph.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; ~뿐(만) 아니라 ~도 (not only … but also …); –(으)ㄹ 수 밖에 없다 (there is no choice but; cannot help -ing); stative verbs that are interpreted as transitive verbs; the adverbial suffix 으로; and the Sino-Korean syllables within 해산물 (海産物), 무명 (無名), 혼례 (婚禮), and 민속촌 (民俗村)."),
        card("Sino-Korean in use: 해산물 (海産物)",
             "This Sino-Korean word means sea food or marine products. The first syllable 해 (海) means sea or marine, as in 남해 (the South Sea), 해녀 (a female diver; “marine woman”) and 해군 (navy; a sailor; “sea military”). The second syllable 산 (産) means producing or giving birth, as in 산모 (a woman who has [recently] given birth to a child; “birth-giving mother”) and 중국산 (Chinese products). The last syllable 물 (物) means object or thing, as in 동물 (animal; “moving object”) and 고물 (an antique; secondary goods; “old thing”). Thus the literal meaning of the word 해산물 is “things that the sea produces,” and the word refers to seafood or edible marine products, such as fish, shellfish, or seaweed. The book asks you to guess the meaning of 농산물, 동해, 지중해, 서해, 해상 도시, 식물, 물품, 생산 and (생)산지 (my answers):",
             tables=[ktable(_S1G), ktable(_S1)]),
        card("Sino-Korean in use: 무명 (無名)",
             "This Sino-Korean word means nameless or unknown, as in 무명 용사 (an unknown soldier; “nameless warrior”) and 무명 작가 (an obscure writer; a nameless writer). The first syllable 무 (無) means nonexistent, not having, or without, and it is similar to the English prefix a- in amoral, asexual, etc. In many combinations, this syllable contrasts with 유 (有), which means existing, having, or with. Some examples of contrasting pairs are 유료 vs. 무료 (paid vs. free of charge), 유인 vs. 무인 (manned vs. unmanned), and 유해 vs. 무해 (hazardous vs. nonhazardous). The second syllable 명 (名) means name, as in 성명 (one’s full name) and 유명하다 (to be famous; “to have a name”). Thus the literal meaning of the word is “not having a name” or “without a name.” The book asks you to guess the meaning of 무선 전화, 인명, 무관심, 가명, 무사고 and 명단 (the book glosses 가 [假]: fake, pseudo-; my answers):",
             tables=[ktable(_S2G), ktable(_S2)]),
        card("Sino-Korean in use: 혼례 (婚禮)",
             "This Sino-Korean word means a wedding (ceremony), a wedding, or nuptials. The first syllable 혼 (婚) means marriage, nuptial, or conjugal, as in 이혼 (a divorce; “leaving one’s marriage”), 약혼 (an engagement; “promising a marriage”), 재혼 (a second marriage; a remarriage), 미혼 (single; unmarried; “not married”), and 기혼 (married; “already married”). The second syllable 례/예 (禮) means ceremony or manners, as in 경례 (salutation; a military salute; “respect with manners”) and 예물 (a wedding gift; “ceremony object”). Note that 례 turns into 예 at the beginning of a word. Thus the literal meaning of the word is “marriage ceremony.” The book asks you to guess the meaning of 결혼, 미혼모, 기혼자, 예절, 예복 and 무례 (my answers):",
             tables=[ktable(_S3G), ktable(_S3)]),
        card("Sino-Korean in use: 민속촌 (民俗村)",
             "This Sino-Korean word means a folk village, a living museum type of tourist attraction. The first syllable 민 (民) means people or folk (of a country, nation, or kingdom), as in 국민 (a nation; a people; “people of a nation”), 시민 (a citizen; an inhabitant of a city), and 민요 (a folk song). The second syllable 속 (俗) means custom or secular, as in 속어 (slang; secular language). The last syllable 촌 (村) means village or -ville, as in 산촌 (a mountain village), 강촌 (a riverside village), and 부촌 (a rich village; a wealthy village). Just as there are American cities or towns whose names end in -ville (e.g., Castroville or Watsonville), there are Korean towns or cities whose names end in 촌, as in 점촌, 상촌, and 대촌. Thus the literal meaning of the word 민속촌 is “folk customs village,” and it refers to the Korean Folk Village, a living museum tourist attraction in the city of 용인. The village displays various elements of traditional Korean life and culture with numerous replicas of traditional houses of the different social classes and various regions. The book asks you to guess the meaning of 군민, 도민, 어촌, 농촌, 장수촌 and 속담 (the book glosses 어 [漁]: fishing, fishery; 담 [談]: saying, words; my answers):",
             tables=[ktable(_S4G), ktable(_S4)]),
    ],
    exercises=uniq(
        _tr(_S1 + _S1G + _S2 + _S2G + _S3 + _S3G + _S4 + _S4G, k=3)
        + [M("What does 해 (海) mean?", "sea; marine", ["mountain", "village", "name"], "해군."), M("What does 산 (産) mean?", "producing; giving birth", ["selling", "eating", "ocean"], "해산물."), M("What does 물 (物) mean?", "object; thing", ["name", "marriage", "village"], "동물."), M("What does 무 (無) mean?", "nonexistent; without", ["existing; with", "village", "sea"], "무명."), M("What does 유 (有) mean?", "existing; having; with", ["without", "name", "village"], "유료."), M("What does 명 (名) mean?", "name", ["village", "ceremony", "marriage"], "성명."), M("What does 혼 (婚) mean?", "marriage; nuptial", ["name", "folk", "sea"], "이혼."), M("What does 례/예 (禮) mean?", "ceremony; manners", ["village", "marriage", "folk"], "예물."), M("What does 민 (民) mean?", "people; folk", ["village", "custom", "name"], "국민."), M("What does 촌 (村) mean?", "village; -ville", ["custom", "folk", "sea"], "산촌."), M("What is the literal meaning of 해산물?", "“things that the sea produces”", ["“marriage ceremony”", "“folk customs village”", "“without a name”"], "해 + 산 + 물."), M("What is the literal meaning of 민속촌?", "“folk customs village”", ["“marriage ceremony”", "“things that the sea produces”", "“without a name”"], "민 + 속 + 촌."),
           F("___료 수영장은 돈을 안 내도 됩니다. (free of charge)", "무", ["유", "민"], "무료."), F("이 호텔은 ___료 서비스가 많습니다. (paid)", "유", ["무", "해"], "유료."), F("서해와 동해는 한국의 ___입니다. (seas)", "바다", ["마을", "시장"], "해."), F("이혼과 재혼에서 ___은 marriage를 뜻합니다. (syllable)", "혼", ["례", "촌"], "혼."), F("어촌과 농촌에서 ___은 village를 뜻합니다. (syllable)", "촌", ["혼", "례"], "촌."),
           read_q("해산물"), read_q("무명"), read_q("혼례"), read_q("민속촌"), read_q("농산물")]
    ),
)

# ================================================================== L2 Vocabulary builder
_VB = [("무용가", "an (artistic) dancer", "Art"), ("갤러리", "an art gallery", "Art"), ("화랑", "an art gallery; “picture gallery”", "Art"), ("예술", "art; “artistic skill”", "Art"), ("민박", "lodging at a private residence", "Lodging"), ("화가", "a painter; “picture professional”", "Art"), ("연날리기", "kite flying", "Korean folk game"), ("오곡밥", "a five-grain meal", "Food"), ("그네타기", "riding a swing", "Korean folk game"), ("펜션", "a pension; a small European-style hotel; a vacation house", "Lodging"), ("민속놀이", "a folk game; a traditional game (my gloss)", "Korean folk game"), ("여관", "a Korean-style inn", "Lodging"), ("먹거리", "food; things to eat (my gloss)", "Food"), ("가수", "a singer", "Art"), ("씨름", "traditional Korean wrestling", "Korean folk game"), ("파전", "green onion pancake; scallion pancake", "Food")]
L2 = lesson(
    "Ch 42 · Vocabulary Builder: art, food, lodging and Korean folk games",
    "무용가 · 갤러리 · 화랑 · 예술 · 민박 · 화가 · 연날리기 · 오곡밥 · 그네타기 · 펜션 · 민속놀이 · 여관 · 먹거리 · 가수 · 씨름 · 파전",
    requires=[],
    cards=[
        card("새 단어: sixteen words to sort",
             "The book gives sixteen words from the chapter (무용가, 갤러리, 화랑, 예술, 민박, 화가, 연날리기, 오곡밥, 그네타기, 펜션, 민속놀이, 여관, 먹거리, 가수, 씨름, 파전) and asks you to circle the ones you do not know, look them up and write the English meanings, then copy each word into its category in a table (Art / Food / Lodging / Korean Folk Game). The meanings are the book’s from the chapter glossary (먹거리 and 민속놀이 are not in the glossary: the glosses are mine); the sorting is my answer.",
             tables=[ktable([(w, m) for w, m, g in _VB])]),
        card("The table filled in (mine)", "",
             tables=[table(["Category", "Words (mine)"], [["Art", "무용가, 갤러리, 화랑, 예술, 화가, 가수"], ["Food", "오곡밥, 먹거리, 파전"], ["Lodging", "민박, 펜션, 여관"], ["Korean folk game", "연날리기, 그네타기, 민속놀이, 씨름"]], say=[1])]),
        card("Activities left out", "Activities 1, 2, 3 and 4 (SMART Board), the PowerPoint Sino-Korean presentation and Activity 5 (the “Speak Up Words” game that the teacher starts on the SMART Board) are computer and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["가수", "민박", "여관", "펜션", "씨름", "연날리기", "오곡밥", "그네타기", "화랑", "예술", "화가", "무용가", "파전"]))
        + [M("Which category does 씨름 belong to?", "Korean folk game", ["Art", "Food", "Lodging"], "My sorting."), M("Which category does 파전 belong to?", "Food", ["Art", "Lodging", "Korean folk game"], "My sorting."), M("Which category does 여관 belong to?", "Lodging", ["Art", "Food", "Korean folk game"], "My sorting."), M("Which category does 화가 belong to?", "Art", ["Food", "Lodging", "Korean folk game"], "My sorting."), M("Which category does 오곡밥 belong to?", "Food", ["Art", "Lodging", "Korean folk game"], "My sorting."), M("Which category does 펜션 belong to?", "Lodging", ["Art", "Food", "Korean folk game"], "My sorting."), M("What does 먹거리 mean?", "food; things to eat", ["a restaurant", "a cook", "a market"], "My gloss."),
           F("공원에서 ___를 하는 아이들이 많아요. (kite flying)", "연날리기", ["씨름", "파전"], "연날리기."), F("비 오는 날에는 ___이 먹고 싶어요. (green onion pancake)", "파전", ["씨름", "그네타기"], "파전."), F("바닷가에 있는 ___을 예약했어요. (pension)", "펜션", ["화랑", "씨름"], "펜션."), F("그 ___은 유명한 한국 무용가입니다. (dancer)", "무용가", ["화가", "가수"], "무용가."), F("인사동에는 ___이 많아요. (galleries)", "화랑", ["여관", "씨름"], "화랑."),
           read_q("민박"), read_q("여관"), read_q("씨름"), read_q("오곡밥"), read_q("파전")]
    ),
)

# ================================================================== L3 Topic A
_A_TXT = [("봄 가족여행으로 진해의 벚꽃 축제는 어떠세요?", "How about the Jinhae Cherry Blossom Festival for a spring family trip?"), ("유명한 벚꽃 거리를 구경하고 해군사관학교도 방문하세요.", "See the famous cherry blossom street and visit the Naval Academy too."), ("전야제에서는 인기가수의 공연과 불꽃놀이를 볼 수 있어요.", "At the eve-of-festival event you can see a popular singer’s performance and fireworks."), ("해군기지에서는 군함 타보기, 일 일 해군 되기 등의 행사가 열립니다.", "At the naval base, events such as riding a warship and being a sailor for a day are held."), ("그리고 시내에서는 퍼레이드를 포함해 다양한 행사들이 열립니다.", "And in the city, various events are held, including a parade."), ("진해항까지 자전거 타기도 있습니다.", "There is also cycling to Jinhae Port."), ("자전거는 무료로 대여해 줍니다.", "Bicycles are lent out free of charge."), ("진해항 주변 식당에서는 현지의 싱싱한 해산물도 맛볼 수 있습니다.", "At restaurants around Jinhae Port you can also taste the fresh local seafood."), ("행사가 열리는 동안 거리가 아주 복잡해요.", "While the events are held, the streets are very crowded."), ("주차장 사정도 안 좋습니다.", "The parking lot situation is not good either."), ("그래서 자가용보다 고속철도나 관광버스를 이용하시는 것이 좋습니다.", "So it is better to use the high-speed train or a tour bus than a private car."), ("그리고 시내 여관이나 호텔에 빈방이 없으면 주변 도시로 가 보세요.", "And if there are no vacant rooms in the inns or hotels in the city, try going to the surrounding cities."), ("임시버스로 약 십오 킬로미터만 가면 됩니다.", "You only have to go about 15 kilometers by temporary bus."), ("임시버스 정보는 시청 홈페이지를 참고하세요.", "For temporary bus information, refer to the city hall homepage.")]
_A_WORDS = ["가수", "거리", "고속철(도)/KTX", "군함", "기지", "대여", "민박", "벚꽃", "불꽃놀이", "사관학교", "사정", "여관", "열다/열리다", "임시", "자가용", "전야제", "참고", "킬로미터", "퍼레이드", "펜션", "해(산)물", "현지"]
_GN = [("유월 이십일 일부터 사흘간 강릉의 경포대 해수욕장에서 여름 바다 축제가 열린다.", "A summer sea festival is held at Gyeongpodae Beach in Gangneung for three days from June 21."), ("올해도 작년과 같이 많은 관광객이 찾을 것으로 예상된다.", "This year too, as last year, many tourists are expected to visit."), ("축제 기간에는 다양한 행사가 준비되어 있다.", "Various events are prepared during the festival period."), ("특히, 전야제에는 불꽃놀이와 인기가수의 공연도 있을 예정이다.", "In particular, the eve-of-festival event will also have fireworks and a popular singer’s performance."), ("강릉 경포대 해수욕장 주변은 관광철에 여관이나 호텔의 숙박비가 아주 비싼 편이다.", "Around Gyeongpodae Beach in Gangneung, the lodging prices of inns and hotels are quite expensive in the tourist season."), ("빈방을 찾기도 어렵다.", "It is also hard to find a vacant room."), ("그래서 숙박을 하려면 강릉 주변의 작은 마을에 있는 민박이나 펜션을 미리 예약하는 것이 좋다.", "So if you want to stay overnight, it is good to reserve in advance a minbak or pension in a small village around Gangneung."), ("야영을 하고 싶다면 경포대 해수욕장 옆에 있는 야영장을 이용하면 된다.", "If you want to camp, you can use the campsite next to Gyeongpodae Beach."), ("참고로 텐트가 없으면 야영장 관리사무실에서 대여받을 수 있다.", "For your reference, if you do not have a tent, you can rent one at the campsite management office."), ("가족 야영객을 위한 대형 텐트도 준비되어 있다고 한다.", "They say large tents for family campers are also prepared.")]
L3 = lesson(
    "Ch 42 · Topic A: Go to the cherry blossom festival (벚꽃 축제에 가 보세요)",
    "벚꽃 축제 · 진해 · 전야제 · 불꽃놀이 · 군함 · 자가용 · 고속철도 · 민박과 펜션 · 강릉 바다 축제",
    requires=[],
    cards=[
        card("Topic A: Go to the cherry blossom festival (벚꽃 축제에 가 보세요)",
             "The following blog entry is about the Cherry Blossom Festival in Jinhae. (The English is mine; the book gives none; 15 km and “1일” are spelled out in Hangul; the printed text has a blank before 호텔, which I left out.)",
             examples=passage(_A_TXT)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists 킬로미터 and 퍼레이드 as loan words.", tables=_words(_A_WORDS)),
        card("한국에서는: 1. The units of measure",
             "Korea uses the metric system to measure length, weight, and volume. 미터 (meter) is for measuring length, 그램 (gram) for weight, and 리터 (liter) for volume. 1 킬로미터 = 1000 미터 = 0.62 마일; 1 킬로그램 = 1000 그램 = 2.2 파운드; 1 리터 = 1000 밀리리터 = 0.26 갤론."),
        card("한국에서는: 2. 벚꽃축제 (the Cherry Blossom Festival)",
             "In Korea, cherry trees are in full bloom in early spring (late March and early April). During this period, many local governments (cities and towns) celebrate the cherry blossoms and sponsor festivals (벚꽃축제) that include various events. Many Koreans attend the cherry blossom festivals. The most popular cherry blossom festival is held in the City of Jinhae, home of the Korean Navy headquarters. Each spring, several hundred thousand people visit the city to see 벚꽃축제."),
        card("북한에서는",
             "In North Korea, large-scale cultural events are held to commemorate specific days, including the birthdays of the leaders Kim Il-Sung and Kim Jung-Il. These events are called 축전, which means festival. Often held as political propaganda, these events require people to participate in mass dances or mass games to show their support for the government and promote its political agenda. 연환모임 is closer to the Western notion of a festival. At these gatherings, which are more open and free, people share food and enjoy leisurely activities."),
        card("Follow-up 2 (Reading): a festival in Gangneung",
             "The following travel magazine article is about a famous festival held in a city on Korea’s east coast; the book asks you to fill in a table in English (Name of festival and date; Events; Location; Lodging information). The book glosses 예상하다: to expect, to anticipate, to predict. The article is the book’s with the date spelled out; the English is mine.",
             examples=passage(_GN)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Name of festival and date", "The summer sea festival (여름 바다 축제), for three days from June 21"], ["Location", "Gyeongpodae Beach, Gangneung"], ["Events", "Various events; fireworks and a popular singer’s performance at the eve-of-festival event"], ["Lodging information", "Inns and hotels are expensive and hard to book in the tourist season; reserve a minbak or pension in a small village around Gangneung in advance; the campsite next to the beach has tents to rent, including large family tents"]])]),
        card("Activities left out", "The presentation steps of Topic A (SMART Board and listening) and Follow-up 1 (listening to three radio reports in which a reporter describes a popular festival, choosing the festival from a. 벚꽃축제, b. 한옥축제, c. 다문화 축제, d. 해산물 축제 and filling in a table of period and events) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_TXT + _GN, k=3)
        + [M("What can you see at the eve-of-festival event in Jinhae?", "A popular singer’s performance and fireworks", ["A parade only", "A boat race", "A wrestling match"], "인기가수의 공연과 불꽃놀이."), M("What is held at the naval base?", "Riding a warship and being a sailor for a day", ["A parade", "A bicycle race", "A market"], "군함 타보기, 일 일 해군 되기."), M("How are the bicycles lent out?", "Free of charge", ["For a fee", "Only to locals", "Only in spring"], "무료로 대여."), M("Why use a high-speed train or tour bus instead of a private car?", "The streets are crowded and parking is poor", ["They are cheaper than walking", "Cars are banned", "There are no roads"], "거리가 복잡, 주차장 사정이 안 좋다."), M("What if there are no vacant rooms in the city?", "Go to a surrounding city by temporary bus", ["Sleep in the car", "Cancel the trip", "Wait a week"], "주변 도시로 가 보세요."), M("When is the Gangneung sea festival?", "Three days from June 21", ["All of July", "One day in May", "Two weeks in August"], "유월 이십일 일부터 사흘간."), M("Where can you camp in Gangneung?", "At the campsite next to Gyeongpodae Beach", ["On the beach itself", "In the hotel", "At the naval base"], "야영장."), M("What is the unit for measuring weight in Korea?", "그램 (gram)", ["미터", "리터", "마일"], "The book’s note."),
           F("행사가 ___ 동안 거리가 아주 복잡해요. (are held)", "열리는", ["여는", "열린"], "열리다."), F("자가용보다 ___를 이용하는 것이 좋습니다. (high-speed train)", "고속철도", ["군함", "펜션"], "고속철도."), F("임시버스 정보는 시청 홈페이지를 ___하세요. (refer to)", "참고", ["대여", "임시"], "참고하다."), F("진해항 주변 식당에서는 ___의 싱싱한 해산물도 맛볼 수 있습니다. (local)", "현지", ["사정", "기지"], "현지."), F("자전거는 무료로 ___해 줍니다. (rent)", "대여", ["참고", "열려"], "대여."),
           read_q("벚꽃 축제에 가 보세요"), read_q("전야제에서는 인기가수의 공연과 불꽃놀이를 볼 수 있어요"), read_q("자전거는 무료로 대여해 줍니다"), read_q("자가용보다 고속철도를 이용하는 것이 좋습니다"), read_q("민박이나 펜션을 미리 예약하는 것이 좋습니다")]
    ),
)

# ================================================================== L4 Activities A: Jindo blog
_JD = [("지난 주말에 우리 가족은 진도에 다녀왔다.", "Last weekend our family went to Jindo."), ("진도에서는 보통 삼월 말에서 사월 초에 사흘 동안 바닷길이 열린다.", "In Jindo, the sea path usually opens for three days from the end of March to the beginning of April."), ("우리는 자가용으로 갔는데 서울에서 진도까지 네 시간이 걸렸다.", "We went by private car, and it took four hours from Seoul to Jindo."), ("일 박 이 일 일정으로 가서 축제 행사장 근처 민박집에서 묵었다.", "We went on a two-day, one-night schedule and stayed at a minbak near the festival venue."), ("민박집은 시설이 깨끗했다.", "The facilities of the minbak were clean."), ("바닷길축제에는 다양한 문화공연행사와 체험행사가 있었다.", "The sea path festival had various cultural performance events and experience events."), ("전야제에서 불꽃놀이도 하고 가수들의 공연도 있었다.", "At the eve-of-festival event there were fireworks and singers’ performances."), ("그리고 진도 전통술 만들기, 떡 만들기 등 재미있는 행사가 많았다.", "And there were many fun events such as making Jindo traditional liquor and making rice cakes."), ("행사장 근처 식당에서는 맛있는 해물요리를 팔았다.", "Restaurants near the venue sold delicious seafood dishes."), ("우리 가족은 전야제에서 불꽃놀이 구경을 했다.", "Our family watched the fireworks at the eve-of-festival event."), ("아빠가 불꽃놀이 사진을 많이 찍었다.", "Dad took many pictures of the fireworks."), ("다음날에는 거리에서 열린 퍼레이드를 재미있게 봤다.", "The next day we enjoyed watching the parade held in the street."), ("그리고 바다가 두 편으로 열리는 바닷길을 걸어갔다.", "And we walked along the sea path where the sea opens in two directions."), ("너무 신기했다.", "It was so amazing."), ("그리고 바닷가 식당에서 해산물 요리를 먹었는데 아주 맛있었다.", "And we ate seafood dishes at a seaside restaurant, and it was very delicious."), ("내년에도 이 축제에 가고 싶다.", "I want to go to this festival next year too.")]
L4 = lesson(
    "Ch 42 · Activities A: a family trip to the Jindo sea path festival",
    "진도 바닷길축제 · 자가용 · 민박집 · 전야제 · 불꽃놀이 · 퍼레이드 · 해산물 요리",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a high school student’s blog",
             "The following high school student’s blog is about his family’s trip to a festival held in Jindo (진도). The book asks you to locate Jindo on an online map and fill in a table in English (Means of transportation; Lodging information; Events and activities offered; Family’s activities), with some answers given. The blog is the book’s with the numbers spelled out; the English is mine.",
             examples=passage(_JD)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Means of transportation", "A private car (four hours from Seoul)"], ["Lodging information", "A minbak near the festival venue; the facilities were clean (a two-day, one-night trip)"], ["Events and activities offered", "Cultural performances and experience events; fireworks and singers’ performances at the eve-of-festival event; making traditional liquor of Jindo; making rice cakes; a parade; seafood dishes at nearby restaurants"], ["Family’s activities", "Watched fireworks (dad took many photos); watched the parade; walked along the sea path; ate seafood at a seaside restaurant"]])]),
        card("Activity 3 (Planning): a festival tour",
             "You are planning to attend a festival and are leaving from Seoul. With a partner you visit the home page of the festival the teacher assigns (경남 진해 벚꽃축제, 충남 보령 머드축제, 전남 진도 바닷길축제 or 경북 안동 국제탈춤축제), fill in a table in English (basic festival information: time, place, admission fee, etc.; available transportation; available lodging; events and activities) and report your plan to the class. This needs the festival web sites and a partner and is left out."),
        card("Activities left out", "Activity 1 (listening to a conversation in which two people talk about the woman’s recent trip to a “water festival” in Jangheung [장흥], locating Jangheung on the Google map and filling in a table of means of transportation, type of lodging and activities) is an audio and online-map activity."),
    ],
    exercises=uniq(
        _tr(_JD, k=3)
        + [M("How did the family get to Jindo?", "By private car", ["By KTX", "By bus", "By plane"], "자가용으로."), M("How long did the trip take?", "Four hours", ["Two hours", "Eight hours", "One hour"], "네 시간이 걸렸다."), M("Where did the family stay?", "A minbak near the venue", ["A hotel", "A tent", "A pension far away"], "민박집."), M("How long is the sea path usually open?", "Three days", ["One day", "A month", "A week"], "사흘 동안."), M("What happens to the sea at the sea path?", "It opens in two directions", ["It freezes", "It dries up", "It turns red"], "바다가 두 편으로 열리는."), M("What did dad do at the fireworks?", "Took many pictures", ["Sang", "Danced", "Slept"], "사진을 많이 찍었다."), M("What did the family watch the next day?", "A parade in the street", ["A wrestling match", "A concert", "A play"], "퍼레이드."), M("What did they eat at the seaside restaurant?", "Seafood dishes", ["Pizza", "Pancakes", "Rice cakes"], "해산물 요리."),
           F("민박집은 ___이 깨끗했다. (facilities)", "시설", ["사정", "기지"], "시설."), F("일 박 이 일 ___으로 가서 민박집에서 묵었다. (schedule)", "일정", ["사정", "전시"], "일정."), F("행사장 근처 식당에서는 맛있는 ___요리를 팔았다. (seafood)", "해물", ["해군", "해수"], "해물요리."), F("다음날에는 거리에서 ___ 퍼레이드를 재미있게 봤다. (held)", "열린", ["여는", "열려"], "열리다."), F("내년에도 이 축제에 ___ 싶다. (want to go)", "가고", ["가서", "갔고"], "가고 싶다."),
           read_q("지난 주말에 우리 가족은 진도에 다녀왔습니다"), read_q("우리는 자가용으로 갔습니다"), read_q("민박집에서 묵었습니다"), read_q("바다가 두 편으로 열리는 바닷길을 걸어갔습니다"), read_q("내년에도 이 축제에 가고 싶습니다")]
    ),
)

# ================================================================== L5 Topic B
_B_DH = [("문화예술의 거리로서 대학로는 젊은이들이 즐겨 찾는다.", "As a street of culture and the arts, Daehak-ro is a place that young people enjoy visiting."), ("무명 가수나 배우, 무용가들이 야외 공연장이나 길거리에서 공연한다.", "Unknown singers, actors and dancers perform at outdoor stages or on the street."), ("또, 그림을 그리는 화가나 춤과 노래를 연습하는 젊은이들도 볼 수 있다.", "Also, you can see painters drawing pictures and young people practicing dance and song."), ("대학로 중심에 있는 마로니에 공원 근처에는 소극장뿐만 아니라 맛집이나 카페도 많다.", "Near Marronnier Park at the center of Daehak-ro there are not only small theaters but also many well-known restaurants and cafes."), ("그래서 대학로는 연인들의 데이트 장소로 유명하다.", "So Daehak-ro is famous as a dating place for lovers.")]
_B_IS = [("인사동은 서울의 대표적인 전통문화의 거리로 외국인들이 많이 찾는다.", "Insa-dong is a representative street of traditional culture in Seoul and many foreigners visit it."), ("골동품 가게와 화랑 등이 많고 한국의 이색적인 문화를 체험할 수 있다.", "There are many antique shops, galleries, etc., and you can experience Korea’s exotic culture."), ("전통 찻집에서 차도 마실 수 있고 떡집에서 떡도 직접 만들어 볼 수 있다.", "You can drink tea at traditional teahouses and also try making rice cakes yourself at rice cake shops."), ("그래서 외국인들이 인사동을 좋아할 수밖에 없다.", "So foreigners cannot help liking Insa-dong."), ("일요일에는 인사동 거리에서 다양한 축제도 열린다.", "On Sundays various festivals are also held on the street in Insa-dong."), ("인사동에 가면 평생 잊지 못할 추억을 만들 수 있다.", "If you go to Insa-dong, you can make memories you will never forget in your life.")]
_B_WORDS = ["골동품", "데이트", "독특하다", "~로", "맛집", "무명", "무용가", "사랑", "소극장", "연인", "예술", "이색적", "젊은이", "중심", "추억", "카페", "평생", "화가", "화랑/갤러리"]
_CD = [("창덕궁은 서울 종로구에 있으며 경복궁의 동쪽에 있다.", "Changdeokgung is in Jongno-gu, Seoul, and is located east of Gyeongbokgung."), ("궁 안에는 아름다운 한국 전통 정원이 있다.", "Inside the palace there is a beautiful Korean traditional garden."), ("천구백구십칠 년 유네스코 문화유산으로 등록되었다.", "It was registered as a UNESCO cultural heritage site in 1997."), ("남산은 높이 이백육십오 미터로 서울 중심에 위치한다.", "Namsan is 265 m high and is located in the center of Seoul."), ("남산은 연인들의 데이트 장소로도 유명하다.", "Namsan is also famous as a dating place for lovers."), ("남산에 있는 서울 타워에서는 서울 시내를 한눈에 볼 수 있다.", "From the Seoul Tower on Namsan you can see all of Seoul at a glance.")]
L5 = lesson(
    "Ch 42 · Topic B: Daehak-ro and Insa-dong (대학로와 인사동)",
    "대학로 · 인사동 · 소극장 · 골동품 · 화랑 · 전통 찻집 · 창덕궁 · 남산",
    requires=[],
    cards=[
        card("Topic B: Daehak-ro and Insa-dong (대학로와 인사동)",
             "The following general information is about two tourist attractions in Seoul: Daehak-ro and Insa-dong. (The English is mine; the book gives none. The book’s footnotes: ~로 [路] means street or boulevard and indicates the street name, as in 종로, 대학로, or 을지로; see 한국어에는 below for 즐겨.)",
             examples=passage(_B_DH) + passage(_B_IS)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter). The book also lists –(으)ㄹ 수밖에 없다 and ~뿐(만) 아니라 ~도 (see the grammar).", tables=_words(_B_WORDS)),
        card("한국어 발음은: reciprocal assimilation",
             "When the stop consonants ㄱ, ㄷ, and ㅂ come before ㄹ, they are nasalized and become ㅇ, ㄴ, and ㅁ, respectively. The ㄹ sound is also nasalized into ㄴ, because of the influence of the new nasalized sound. This phenomenon is called reciprocal assimilation. (See the Introductory Unit Appendix, page A.4, for more information.) Thus, 대학로 sounds like /대항노/. The book gives 율곡로 and 사직로 to listen to (audio); by the same rule they sound like /율공노/ and /사징노/ (my note)."),
        card("한국어에는: 집 and 즐겨",
             "1. 집 literally means “a house.” However, it often refers to a business, store, shop, or restaurant in different contexts, as in 꽃집 (a flower shop), 빵집 (a bakery), 찻집 (a teahouse), 맛집 (a restaurant well known for tasty food), and 떡집 (a rice cake store). 이 집이 음식을 잘 합니다 (This restaurant makes good food. / “This house does food well.”)\n\n"
             "2. 즐겨 + action verb. 즐겨 comes from the verb 즐기다, which means to enjoy, as in 저는 쇼핑을 즐겨요 (I enjoy shopping). 즐겨 is used to express “enjoy doing something” when it is combined with verbs such as 먹다, 보다, 듣다, or 입다.",
             examples=passage([("나는 한국 음식을 즐겨 먹어요.", "I enjoy (eating) Korean food."), ("나는 한국 영화를 즐겨 봐요.", "I enjoy (watching) Korean movies."), ("김 선생님은 청바지를 즐겨 입습니다.", "Mr. Kim enjoys (wearing) blue jeans.")])),
        card("한국에서는: 대학로 and 인사동",
             "대학로 (Daehak-ro), known as a street for young people, is located on the former campus of the Seoul National University. The school moved out in 1975 and many theater groups started moving to Daehak-ro in the 1980s as it developed into a cultural center. The center of Daehak-ro, Marronnier Park, is the site of live performances by young people.\n\n"
             "인사동 (Insa-dong), located at the heart of the capital, is a favorite shopping area because its main street branches into countless alleys of antique stores, galleries, traditional restaurants, teahouses, and cafes. In fact, more than 40% of the nation’s antique stores are in Insa-dong. Every Sunday, selected streets are blocked off from traffic. Insa-dong is especially popular with foreign tourists because they can experience traditional Korean culture and festivities."),
        card("Follow-up 1 (Reading): two attractions, 창덕궁 and 남산",
             "The following information is about two attractions in Seoul: A. 창덕궁 and B. 남산. The book asks you to match five English sentences with the place (the first is done: 1 = A). The information is the book’s with the numbers spelled out (the book’s “265 m” is read as in Korean); the English is mine.",
             examples=passage(_CD)),
        card("The matches (mine)", "",
             tables=[table(["Sentence", "Place (mine)"], [["1. This place was added to the UNESCO World Heritage List.", "A (창덕궁)"], ["2. This place is located in the center of Seoul.", "B (남산)"], ["3. This place is famous as a destination for lovers.", "B (남산)"], ["4. This place has a beautiful garden inside.", "A (창덕궁)"], ["5. This place is located to the east of Gyeongbokgung.", "A (창덕궁)"]])]),
        card("Useful websites", "The book lists two websites: 한국 관광 공사 (the Korea Tourism Organization) and 서울관광 (Seoul tourism)."),
        card("Activities left out", "The presentation steps of Topic B (SMART Board) and Follow-up 1 b (listening to two conversations in which a man asks for directions to 창덕궁 or 남산, identifying the place and writing the directions) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_DH + _B_IS + _CD, k=3)
        + [M("Who visits Daehak-ro?", "Young people", ["Only tourists", "Only soldiers", "Only children"], "젊은이들이 즐겨 찾는다."), M("Who performs in Daehak-ro?", "Unknown singers, actors and dancers", ["Famous singers only", "Orchestras", "Athletes"], "무명 가수나 배우, 무용가."), M("What is Daehak-ro famous for?", "A dating place for lovers", ["A seafood market", "A military base", "A beach"], "연인들의 데이트 장소."), M("What can you find in Insa-dong?", "Antique shops and galleries", ["Ski slopes", "Beaches", "Factories"], "골동품 가게와 화랑."), M("What can you do at a rice cake shop in Insa-dong?", "Try making rice cakes yourself", ["Buy a car", "Watch a movie", "Sleep"], "떡을 직접 만들어 볼 수 있다."), M("What happens on Insa-dong street on Sundays?", "Various festivals are held", ["It is closed", "A market opens", "Nothing"], "다양한 축제도 열린다."), M("What does 집 refer to in 빵집?", "A shop", ["A house to live in", "A hotel", "A school"], "The book’s note."), M("What does 즐겨 + verb mean?", "Enjoy doing", ["Stop doing", "Try to do", "Want to do"], "The book’s note."),
           F("대학로는 연인들의 ___ 장소로 유명하다. (dating)", "데이트", ["카페", "예술"], "데이트."), F("인사동에는 ___ 가게와 화랑이 많다. (antique)", "골동품", ["소극장", "맛집"], "골동품."), F("그 ___에서 맛있는 불고기를 먹었어요. (famous restaurant)", "맛집", ["화랑", "소극장"], "맛집."), F("저는 한국 영화를 ___ 봐요. (enjoy)", "즐겨", ["즐겁게", "즐기고"], "즐겨 + verb."), F("인사동에 가면 ___ 잊지 못할 추억을 만들 수 있다. (all one’s life)", "평생", ["평소", "평상시"], "평생."),
           read_q("대학로와 인사동"), read_q("대학로는 젊은이들이 즐겨 찾습니다"), read_q("인사동은 전통문화의 거리입니다"), read_q("연인들의 데이트 장소로 유명합니다"), read_q("평생 잊지 못할 추억을 만들 수 있습니다")]
    ),
)

# ================================================================== L6 Grammar A: cannot help -ing
_CH1 = [("숙제가 많아서 늦게 잘 수밖에 없어요.", "There is so much homework, I have no choice but to go to bed late."), ("숙제가 많아서 늦게 자지 않을 수 없어요.", "There is so much homework, I can’t help going to bed late.")]
_CH2 = [("신용카드 빚이 많아서 돈을 아낄 수밖에 없어.", "I have so much credit card debt, I have no choice but to be frugal with money."), ("약을 먹기 싫지만 먹을 수밖에 없다.", "I hate to take a pill, but I have no choice but to do it.")]
_CH3 = [("회의에 늦게 참석하다", "Attend the meeting late"), ("길이 많이 막혀서 회의에 늦게 참석할 수밖에 없었어요.", "The roads were so jammed that I had no choice but to attend the meeting late.")]
_CHS = [("비가 많이 와서 집에 있을 수밖에 없었어요.", "It rained a lot, so I had no choice but to stay home."), ("시험이 내일이라서 밤을 새울 수밖에 없어요.", "The exam is tomorrow, so I have no choice but to stay up all night."), ("차가 고장 나서 버스를 탈 수밖에 없었어요.", "My car broke down, so I had no choice but to take the bus."), ("아파서 병원에 가지 않을 수 없었어요.", "I was sick, so I could not help going to the hospital."), ("너무 웃겨서 웃지 않을 수 없었어요.", "It was so funny that I could not help laughing.")]
L6 = lesson(
    "Ch 42 · Grammar A: expressing “cannot help -ing”, –(으)ㄹ 수밖에 없다 and –지 않을 수 없다",
    "-(으)ㄹ 수밖에 없다 · -지 않을 수 없다 · 숙제가 많아서 늦게 잘 수밖에 없어요",
    requires=[],
    cards=[
        card("Expressing “cannot help -ing”",
             "In English, expressions like “cannot help -ing” or “have no choice but to” emphasize that there is no alternative, as in “I cannot help laughing” or “I have no choice but to sell it.” The Korean equivalents are the auxiliary verbs –(으)ㄹ 수밖에 없다 and –지 않을 수 없다. For example (the English is the book’s):",
             examples=passage(_CH1)),
        card("The patterns", "verb stem + (으)ㄹ 수밖에 없다; verb stem + 지 않을 수 없다. More examples (the English is the book’s):", examples=passage(_CH2)),
        card("Follow-up 1 (Listening, reading and speaking): the model",
             "Partner A chooses a verbal phrase from List A and reads it aloud to Partner B. Then Partner B makes a sentence using the auxiliary verb –(으)ㄹ 수밖에 없다 and adds reasons. The book’s model (the English is mine):",
             examples=dlg([("A", _CH3[0][0], _CH3[0][1]), ("B", _CH3[1][0], _CH3[1][1])])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_CHS)),
        card("Activities left out", "Follow-up 2 (listening to three segments in which a man talks about a situation in which he had no alternative, and writing the action he had to do and the reason in English) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_CH1 + _CH2 + _CH3 + _CHS, k=3)
        + [M("What does –(으)ㄹ 수밖에 없다 mean?", "There is no choice but to; cannot help -ing", ["Can do it easily", "Do not have to", "Would like to"], "The book’s note."), M("What other pattern has the same meaning?", "–지 않을 수 없다", ["–고 싶다", "–(으)면 안 되다", "–기 쉽다"], "The book’s note."), M("What does 약을 먹기 싫지만 먹을 수밖에 없다 mean?", "I hate to take a pill, but I have no choice but to do it", ["I like taking pills", "I will not take pills", "I took the pill"], "The book’s example."), M("What does 숙제가 많아서 늦게 자지 않을 수 없어요 mean?", "There is so much homework, I can’t help going to bed late", ["I go to bed early", "I have no homework", "I do my homework late"], "The book’s example."),
           F("신용카드 빚이 많아서 돈을 아낄 ___ 없어. (no choice but)", "수밖에", ["뿐만", "만큼"], "-(으)ㄹ 수밖에 없다."), F("길이 막혀서 회의에 늦게 참석할 ___ 없었어요. (no choice but)", "수밖에", ["뿐만", "대로"], "-(으)ㄹ 수밖에."), F("너무 웃겨서 웃지 않을 ___ 없었어요. (could not help)", "수", ["것", "때"], "-지 않을 수 없다."), F("아파서 병원에 가지 않을 수 ___. (could not help)", "없었어요", ["있었어요", "없다"], "-지 않을 수 없다."), F("차가 고장 나서 버스를 ___ 수밖에 없었어요. (take)", "탈", ["타는", "탄"], "-(으)ㄹ 수밖에."),
           read_q("숙제가 많아서 늦게 잘 수밖에 없어요"), read_q("약을 먹기 싫지만 먹을 수밖에 없다"), read_q("길이 막혀서 회의에 늦게 참석할 수밖에 없었어요"), read_q("너무 웃겨서 웃지 않을 수 없었어요"), read_q("비가 많이 와서 집에 있을 수밖에 없었어요")]
    ),
)

# ================================================================== L7 Grammar B: not only ... but also
_NB1 = [("나는 한국음식뿐(만) 아니라 멕시코음식도 좋아해요.", "I like not only Korean food but also Mexican food."), ("직장에서뿐(만) 아니라 집에서도 한국말을 합니다.", "I speak Korean not only at work but also at home.")]
_NB2 = [("나는 한국음식을 좋아할 뿐(만) 아니라 만들기도 합니다.", "I not only like Korean food but also make it.")]
_NB3 = [("김 선생님은 제주도뿐 아니라 하와이도 가 봤어요.", "Mr. Kim has been not only to Jeju Island but also to Hawaii."), ("불고기는 어른뿐만 아니라 아이들도 좋아합니다.", "Not only do adults like bulgogi, but children do as well."), ("김 일병은 춤을 잘 출 뿐만 아니라 노래도 잘 합니다.", "PFC Kim not only dances well but also sings well."), ("이 식당 음식은 맛있을 뿐 아니라 가격도 쌉니다.", "The food in this restaurant is not only tasty but also cheap.")]
_NBM = [("김 병장뿐만 아니라 이 상병도 운동을 잘 한다.", "Not only Sgt. Kim but also Cpl. Lee is good at sports.")]
_NBM2 = [("동생은 공부를 잘 할 뿐 아니라 가르치기도 잘한다.", "My younger brother is not only good at studying but also good at teaching.")]
_NBA = [("손뿐만 아니라 발도 커요.", "Not only the hands but also the feet are big."), ("미국뿐만 아니라 중국도 가 봤어요.", "I have been not only to America but also to China."), ("꽃뿐만 아니라 초콜릿도 샀어요.", "I bought not only flowers but also chocolate."), ("인사동뿐만 아니라 대학로도 유명해요.", "Not only Insa-dong but also Daehak-ro is famous.")]
_NBB = [("이 호텔은 시끄러울 뿐만 아니라 비싸기도 해요.", "This hotel is not only noisy but also expensive."), ("지하철은 쌀 뿐만 아니라 빠르기도 해요.", "The subway is not only cheap but also fast."), ("내 핸드폰은 예쁠 뿐만 아니라 편리하기도 해요.", "My cell phone is not only pretty but also convenient."), ("몬트레이는 날씨가 좋을 뿐만 아니라 경치도 좋아요.", "Monterey not only has good weather but also good scenery.")]
_NBH = [("제 고향은 뉴욕주입니다.", "My hometown is New York State."), ("뉴욕은 브로드웨이뿐만 아니라 타임스퀘어도 유명합니다.", "New York is famous for not only Broadway but also Times Square."), ("타임스퀘어에는 구경할 것이 많을 뿐만 아니라 좋은 식당도 많습니다.", "In Times Square there are not only many things to see but also many good restaurants.")]
L7 = lesson(
    "Ch 42 · Grammar B: expressing “not only … but also …”, ~뿐(만) 아니라 ~도",
    "~뿐(만) 아니라 ~도 · -(으)ㄹ 뿐(만) 아니라 -기도 하다 · 김 병장뿐만 아니라 · 내 고향의 관광지",
    requires=[],
    cards=[
        card("Not only … but also …",
             "In English, the correlative conjunction “not only … but also …” expresses two ideas of the same importance. For example: I like not only bananas but also apples. She is not only clever but also hardworking. I speak Korean not only at work but also at home. Note that the two italicized ideas in the conjunctive structures above can be nouns, adjectives, verbs, phrases, etc. The Korean equivalent of the correlative conjunction “not only … but also …” is ~뿐(만) 아니라 ~도. For example (the English is the book’s):",
             examples=passage(_NB1)),
        card("Two verbs",
             "To express two verbs of the same importance, however, we use –(으)ㄹ 뿐(만) 아니라 –기도 하다. For example (the English is the book’s):",
             examples=passage(_NB2)),
        card("Notes on the forms",
             "–(으)ㄹ in –(으)ㄹ 뿐(만) 아니라 is the attributive form of a verb and –기 in –기도 하다 is a gerund. If the second verb is made up of a noun and 하다, as in 공부하다, 운동하다, etc., we can use ~도 하다 instead of –기도 하다.\n\nnoun + 뿐(만) 아니라 noun + 도; verb stem + (으)ㄹ 뿐(만) 아니라 verb stem + 기도 하다. More examples (the English is the book’s):",
             examples=passage(_NB3)),
        card("Follow-up 3 (Listening and speaking): the models",
             "a. One student says a set of words to the other (e.g. 김 병장/이 상병/운동); the second student creates a complete sentence using ~뿐(만) 아니라 ~도. The sets are: 손/발/크다; 미국/중국/가보다; 꽃/초콜릿/사다; 인사동/대학로/유명하다. The book’s model and my answers for the four sets (the English is mine):",
             examples=passage(_NBM + _NBA)),
        card("Follow-up 3 b (the second set)",
             "b. The second set uses both ~뿐(만) 아니라 ~도 and –(으)ㄹ 뿐(만) 아니라 –기도 하다: the book’s model is 동생/공부를 잘 하다/가르치다. The sets are: 이 호텔/시끄럽다/비싸다; 지하철/싸다/빠르다; 내 핸드폰/예쁘다/편리하다; 몬트레이/날씨가 좋다/경치가 좋다. The book’s model and my answers (the English is mine):",
             examples=passage(_NBM2 + _NBB)),
        card("Follow-up 5 (Listening and speaking): two tourist attractions of your hometown",
             "Think of two tourist attractions in your hometown and two reasons each is famous (fill in a table in English); go around the classroom and exchange information with at least three classmates, using ~뿐만 아니라 ~도 and –(으)ㄹ 뿐만 아니라 –기도 하다; then present one attraction you learned about. The book’s model (the English is mine):",
             examples=passage(_NBH)),
        card("Activities left out", "Follow-up 4 (listening to four short conversations and transcribing the nouns or verbs connected by ~뿐(만) 아니라 ~도, then translating the sentence) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_NB1 + _NB2 + _NB3 + _NBM + _NBM2 + _NBA + _NBB + _NBH, k=3)
        + [M("What does ~뿐(만) 아니라 ~도 mean?", "not only … but also …", ["either … or …", "neither … nor …", "if … then …"], "The book’s note."), M("What do you use for two verbs of the same importance?", "–(으)ㄹ 뿐(만) 아니라 –기도 하다", ["~뿐(만) 아니라 ~도", "–(으)면 –(으)ㄹ 것이다", "–고 나서"], "The book’s note."), M("What is –기 in –기도 하다?", "A gerund", ["A tense marker", "A noun", "A particle"], "The book’s note."), M("What can replace –기도 하다 after a 하다 verb?", "~도 하다", ["–지 않다", "–고 있다", "–아/어 보다"], "The book’s note."), M("What does 불고기는 어른뿐만 아니라 아이들도 좋아합니다 mean?", "Not only adults but also children like bulgogi", ["Only adults like bulgogi", "Children dislike bulgogi", "Adults and children eat bulgogi at home"], "The book’s example."), M("What does 이 식당 음식은 맛있을 뿐 아니라 가격도 쌉니다 mean?", "The food is not only tasty but also cheap", ["The food is tasty but expensive", "The food is cheap but bad", "The restaurant is new"], "The book’s example."),
           F("한국음식___ 아니라 멕시코음식도 좋아해요. (not only)", "뿐(만)", ["밖에", "처럼"], "뿐(만) 아니라."), F("김 일병은 춤을 잘 출 ___ 노래도 잘 합니다. (not only)", "뿐만 아니라", ["수밖에", "대로"], "-(으)ㄹ 뿐만 아니라."), F("나는 한국음식을 좋아할 뿐 아니라 만들___ 합니다. (gerund + also)", "기도", ["고도", "지도"], "-기도 하다."), F("직장에서뿐 아니라 집에서___ 한국말을 합니다. (also)", "도", ["만", "를"], "~도."), F("김 선생님은 제주도뿐 아니라 하와이___ 가 봤어요. (also)", "도", ["만", "를"], "~도."),
           read_q("한국음식뿐 아니라 멕시코음식도 좋아해요"), read_q("직장에서뿐 아니라 집에서도 한국말을 합니다"), read_q("불고기는 어른뿐만 아니라 아이들도 좋아합니다"), read_q("김 일병은 춤을 잘 출 뿐만 아니라 노래도 잘 합니다"), read_q("이 식당 음식은 맛있을 뿐 아니라 가격도 쌉니다")]
    ),
)

# ================================================================== L8 Activities B: Insoo's Daehak-ro day
_IN = [("토요일에 고등학교 동창을 만나서 오랜만에 대학로에 갔다.", "On Saturday I met a high school classmate and went to Daehak-ro after a long time."), ("날씨는 따뜻했고 거리는 젊은이들로 붐볐다.", "The weather was warm and the streets were crowded with young people."), ("우리는 열 시쯤 마로니에 공원으로 갔다.", "We went to Marronnier Park at about 10 o’clock."), ("거기서 야외 조각 전시회와 전통춤 공연을 무료로 관람했다.", "There we watched an outdoor sculpture exhibition and a traditional dance performance free of charge."), ("열두 시에 어떤 맛집에 갔는데 손님이 많아서 이십 분 정도 기다려야 했다.", "At 12 o’clock we went to a well-known restaurant, and there were many customers, so we had to wait about 20 minutes."), ("점심을 먹고 두 시에 소극장에 가서 뮤지컬을 봤다.", "After lunch, at 2 o’clock, we went to a small theater and saw a musical."), ("무명배우들의 공연이었지만 아주 인상적이었다.", "It was a performance by unknown actors, but it was very impressive."), ("다섯 시에 공연이 끝나 우리는 극장 옆에 있는 찻집에 가서 차를 마시고 떡도 먹었다.", "At 5 o’clock the performance ended, and we went to a teahouse next to the theater and drank tea and ate rice cakes."), ("인테리어가 이색적이어서 데이트 장소로 사랑받는 곳이라고 했다.", "The interior was exotic, so they said it is a place loved as a dating spot."), ("일곱 시쯤 친구와 헤어져서 집으로 왔다.", "At about 7 o’clock I parted from my friend and came home."), ("오랜만에 동창하고 시간을 보내서 좋았다.", "It was nice to spend time with a classmate after a long time."), ("매월 마지막 토요일 오후 한 시부터 일곱 시까지 대학로는 자동차 없는 거리가 된다고 하니까 다음에 갈 때는 이 시간에 가야겠다.", "I heard that Daehak-ro becomes a car-free street from 1 p.m. to 7 p.m. on the last Saturday of every month, so next time I go I should go at this time.")]
L8 = lesson(
    "Ch 42 · Activities B: Insoo’s day in Daehak-ro",
    "대학로 · 마로니에 공원 · 소극장 · 뮤지컬 · 찻집 · 자동차 없는 거리 · 일기",
    requires=[],
    cards=[
        card("Activity 2 (Reading): Insoo’s blog",
             "The following blog entry is written by Insoo, who recently met a friend from high school. The book asks you to (1) fill in a table in English (time; what Insoo did; related comments) and (2) answer what Insoo wrote about visiting Insa-dong next time (the text actually says 대학로; see my answer). The book glosses 조각: sculpture; 헤어지다: to part from, to bid farewell. The blog is the book’s with the times spelled out in Hangul; the English is mine.",
             examples=passage(_IN)),
        card("The table filled in (mine)", "",
             tables=[table(["Time", "What Insoo did", "Related comments (mine)"], [["10:00 a.m.–noon", "Went to Marronnier Park; watched an outdoor sculpture exhibition and a traditional dance performance", "Free of charge (N/A in the book’s first row)"], ["Noon–5:00 p.m.", "Had lunch at a well-known restaurant; saw a musical at a small theater", "The restaurant was crowded (about a 20-minute wait); the actors were unknown, but the performance was very impressive"], ["After 5:00 p.m.", "Went to a teahouse next to the theater and drank tea and ate rice cakes; parted from the friend at about 7:00 and went home", "The interior was exotic; it is loved as a dating spot; he enjoyed time with a classmate after a long time"]])]),
        card("The answer to question 2 (mine)", "The text says that Daehak-ro becomes a car-free street from 1 p.m. to 7 p.m. on the last Saturday of every month, so next time Insoo plans to go at this time. (The book’s question says “Insa-dong”, but the text is about Daehak-ro.)"),
        card("Activities left out", "Activity 1 (the “story-chaining” game in which students sit in a circle, add sentences using the new words from Topic B and vote for the best story) and Activity 3 (listening to a Korean friend’s voice mail message, finding and recommending a place for a one-day tour of Seoul on the websites 서울 관광 명소, 서울시 추천 코스 10선 and 외국인의 추천 코스, summarizing it in Korean and presenting it) are audio, online and group activities."),
    ],
    exercises=uniq(
        _tr(_IN, k=3)
        + [M("Who did Insoo meet?", "A high school classmate", ["A coworker", "A teacher", "A cousin"], "고등학교 동창."), M("What did they watch in Marronnier Park?", "An outdoor sculpture exhibition and a traditional dance performance", ["A movie", "A baseball game", "A fashion show"], "야외 조각 전시회와 전통춤 공연."), M("How long did they wait at the restaurant?", "About 20 minutes", ["About 2 hours", "No wait", "About 5 minutes"], "이십 분 정도."), M("What did they see at the small theater?", "A musical", ["A play with famous actors", "A movie", "A concert"], "뮤지컬."), M("What did they do after 5:00?", "Drank tea and ate rice cakes at a teahouse", ["Went to a museum", "Went home", "Shopped"], "차를 마시고 떡도 먹었다."), M("When does Daehak-ro become a car-free street?", "The last Saturday of every month, 1–7 p.m.", ["Every Sunday", "The first Saturday", "Every day"], "매월 마지막 토요일."),
           F("거리는 젊은이들로 ___. (was crowded)", "붐볐다", ["넓었다", "조용했다"], "붐비다."), F("야외 조각 전시회를 무료로 ___했다. (watched)", "관람", ["대여", "참고"], "관람."), F("무명배우들의 공연이었지만 아주 ___이었다. (impressive)", "인상적", ["이색적", "독특"], "인상적."), F("일곱 시쯤 친구와 ___ 집으로 왔다. (parted)", "헤어져서", ["만나서", "찾아서"], "헤어지다."), F("오랜만에 ___하고 시간을 보내서 좋았다. (classmate)", "동창", ["연인", "화가"], "동창."),
           read_q("토요일에 고등학교 동창을 만나서 대학로에 갔습니다"), read_q("마로니에 공원에서 전통춤 공연을 관람했습니다"), read_q("소극장에 가서 뮤지컬을 봤습니다"), read_q("찻집에 가서 차를 마시고 떡도 먹었습니다"), read_q("매월 마지막 토요일에 대학로는 자동차 없는 거리가 됩니다")]
    ),
)

# ================================================================== L9 Topic C
_C_TXT = [("정월 대보름에 용인에 있는 한국민속촌에 갔다 왔다.", "On the Great Full Moon (Jeongwol Daeboreum) I went to the Korean Folk Village in Yongin."), ("민속촌은 민속 마을, 박물관, 공연 등 다양한 민속 문화를 체험할 수 있는 곳이다.", "The folk village is a place where you can experience various folk culture, such as folk villages, a museum and performances."), ("이곳에서는 정기적으로 다양한 민속 문화행사가 열린다.", "Various folk cultural events are held here regularly."), ("아침 일찍 서울을 출발해서 오전 열 시쯤 민속촌에 도착했다.", "I left Seoul early in the morning and arrived at the folk village at about 10 a.m."), ("먼저 민속마을에서 초가집과 기와집을 구경하고 조선시대의 전통생활을 체험해 보았다.", "First, in the folk village, I looked at thatched-roof houses and tiled-roof houses and tried experiencing the traditional life of the Joseon period."), ("민속 마을을 보고 난 후 전통 혼례식을 구경했다.", "After seeing the folk village, I watched a traditional wedding ceremony."), ("전통 혼례복을 입은 신랑 신부가 서로 절을 하고 술잔을 주고받았다.", "The bride and groom in traditional wedding clothes bowed to each other and exchanged wine cups."), ("점심에는 민속 장터에서 오곡밥과 파전을 먹었다.", "For lunch I ate five-grain rice and scallion pancake at the folk marketplace."), ("그리고 두 시부터는 공연장에서 민속 공연을 관람했다.", "And from 2 o’clock I watched folk performances at the performance hall."), ("널뛰기, 줄타기, 그네타기 공연을 보았다.", "I saw seesaw jumping, tightrope walking and swing riding performances."), ("민속 공연이 끝나고 민속촌의 다른 곳도 둘러보았다.", "After the folk performances ended, I also looked around other places in the folk village."), ("저녁 여섯 시부터는 정월 대보름 행사를 보았다.", "From 6 in the evening I watched the Great Full Moon events."), ("집에 돌아오는 길에는 보름달이 떠서 아주 밝았다.", "On the way home, the full moon had risen and it was very bright."), ("보름달을 보니까 고향에 계신 할머니가 그리워졌다.", "Seeing the full moon, I began to miss my grandmother in my hometown.")]
_C_WORDS = ["그네타기", "그립다", "남다", "널뛰기", "뜨다", "민속", "별", "(보름)달", "씨름", "아쉽다", "연날리기", "오곡밥", "장터", "전시품", "~(적/식)으로", "절", "정월 대보름", "조선시대", "줄타기", "지다", "초가집", "파전", "해", "혼례"]
_JJ = [("제주도 여행 셋째 날은 제주민속촌을 방문했다.", "On the third day of the Jeju trip, I visited the Jeju Folk Village."), ("아침 아홉 시쯤 호텔을 출발해서 열 시쯤 민속촌에 도착했다.", "I left the hotel at about 9 in the morning and arrived at the folk village at about 10."), ("제주민속촌은 제주도의 전통문화를 볼 수 있는 곳이다.", "The Jeju Folk Village is a place where you can see Jeju Island’s traditional culture."), ("먼저 민속촌박물관에 들어갔다.", "First I went into the folk village museum."), ("그곳에서 조선시대 제주도의 전통문화에 관한 전시품을 보았다.", "There I saw exhibits about the traditional culture of Jeju Island in the Joseon period."), ("그리고 민속마을에 가서 제주도의 다양한 전통생활을 체험해 보았다.", "And I went to the folk village and tried experiencing various traditional lifestyles of Jeju Island."), ("점심은 민속 장터에서 돼지불고기와 김치찌개를 먹었다.", "For lunch I ate pork bulgogi and kimchi stew at the folk marketplace."), ("오후 두 시부터는 공연장에서 민속공연을 관람했다.", "From 2 p.m. I watched folk performances at the performance hall."), ("줄타기, 그네뛰기, 전통춤 공연을 보았다.", "I saw tightrope walking, swing jumping and traditional dance performances."), ("그리고 오후 네 시쯤 민속촌을 떠나서 제주 공항으로 이동했다.", "And at about 4 p.m. I left the folk village and moved to Jeju Airport.")]
L9 = lesson(
    "Ch 42 · Topic C: I went to the Korean Folk Village (한국민속촌에 갔다 왔다)",
    "한국민속촌 · 초가집과 기와집 · 전통 혼례 · 오곡밥과 파전 · 널뛰기 · 줄타기 · 그네타기 · 정월 대보름",
    requires=[],
    cards=[
        card("Topic C: I went to the Korean Folk Village (한국민속촌에 갔다 왔다)",
             "This journal entry is about Yongsu’s visit to the Korean Folk Village. (The English is mine; the book gives none; the times are spelled out in Hangul. The book’s footnote: –기 in 널뛰기, 줄타기, and 그네타기 is a gerund “maker”; its English equivalent is -ing. The printed text has a stray blank after the line about bowing to each other, which I left out.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_C_WORDS)),
        card("한국에서는: 정월 대보름",
             "(정월) 대보름, which literally means “the great 15th day (of January),” is a traditional Korean holiday that celebrates the first full moon of the lunar new year. Koreans used to practice some unique traditions on this holiday. For example, people cracked nuts with their teeth. This practice, known as 부럼 깨기, is believed to make one’s teeth strong for the rest of the year. In the countryside, people climbed mountains to try to catch sight of the first full moonrise of the year. It is said that the first person to see the moonrise will have good luck all year. When the first full moon is near, people burn the dry grass on the slopes between the rice fields while children whirl cans full of burning charcoal. The whirling of many fire cans makes an impressive scene on a moonlit night. 쥐불놀이 (“rat fire play”) is a practice in which the cans are tossed high in the air and into the field. The resulting fire fertilizes the fields and destroys harmful pests, including rats."),
        card("Presentation c–d: the table and the order (mine)",
             "The book asks you to arrange the sentence strips of Topic C in order (the first and last are numbered for you) and to compare with the audio; the order is the order of the text above. The book also asks about the activities in a table; my answers for the visit:",
             tables=[table(["Time", "What Yongsu did (mine)"], [["Morning", "Left Seoul early; arrived at the folk village at about 10 a.m.; looked at thatched and tiled houses and tried traditional life in the folk village; watched a traditional wedding ceremony"], ["Lunch", "Ate five-grain rice and scallion pancake at the folk marketplace"], ["Afternoon", "From 2:00 watched folk performances (seesaw jumping, tightrope walking, swing riding); looked around other places"], ["Evening", "From 6:00 watched the Great Full Moon events; saw the bright full moon on the way home and missed his grandmother"]])]),
        card("Follow-up 2 (Reading): a folk village on Jeju Island",
             "Read the blog entry about a visit to a folk village on Jeju Island and number the writer’s activities in sequence (two are numbered for you: departed from the hotel 1; left the folk village 7). The blog is the book’s with the times spelled out; the English is mine.",
             examples=passage(_JJ)),
        card("The numbering (mine)", "",
             tables=[table(["What the writer did", "Number (mine)"], [["Departed from the hotel", "1"], ["Arrived at Jeju Folk Village", "2"], ["Went to Jeju Folk Museum and saw various exhibits", "3"], ["Experienced Jeju traditional life at the folk village", "4"], ["Ate kimchi stew and pork bulgogi for lunch", "5"], ["Watched folk performances", "6"], ["Left the folk village", "7"]])]),
        card("Useful website", "The book lists the website of 한국민속촌 (the Korean Folk Village)."),
        card("Activities left out", "The presentation steps of Topic C (SMART Board and listening) and Follow-up 1 (listening to three dialogs in which a teacher asks students about their class trip to the Korean Folk Village and checking the favorite site: folk marketplace, folk village or folk museum) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT + _JJ, k=3)
        + [M("When did Yongsu go to the Korean Folk Village?", "On the Great Full Moon", ["On New Year’s Day", "On Chuseok", "On his birthday"], "정월 대보름."), M("Where is the Korean Folk Village?", "Yongin", ["Seoul", "Jeju", "Busan"], "용인."), M("What did Yongsu watch after seeing the folk village?", "A traditional wedding ceremony", ["A parade", "A fireworks show", "A football match"], "전통 혼례식."), M("What did he eat for lunch?", "Five-grain rice and scallion pancake", ["Bulgogi", "Noodles", "Kimbap"], "오곡밥과 파전."), M("Which performances did he see?", "Seesaw jumping, tightrope walking, swing riding", ["Taekwondo", "Wrestling", "Kite flying"], "널뛰기, 줄타기, 그네타기."), M("Whom did the full moon make him miss?", "His grandmother", ["His friend", "His mother", "His teacher"], "할머니가 그리워졌다."), M("What did Jeju’s writer eat for lunch?", "Pork bulgogi and kimchi stew", ["Bibimbap", "Pancakes", "Seaweed soup"], "돼지불고기와 김치찌개."), M("Where did the Jeju writer go after leaving the folk village?", "Jeju Airport", ["The hotel", "A museum", "A market"], "제주 공항으로 이동."),
           F("정월 대보름에는 ___이 떠서 아주 밝습니다. (full moon)", "보름달", ["반달", "초승달"], "보름달."), F("전통 혼례복을 입은 신랑 신부가 서로 ___을 했다. (bow)", "절", ["널뛰기", "씨름"], "절."), F("민속 장터에서 오곡밥과 ___을 먹었다. (scallion pancake)", "파전", ["씨름", "그네"], "파전."), F("고향에 계신 할머니가 ___. (miss)", "그리워졌다", ["아쉬웠다", "남았다"], "그립다."), F("옛날 농촌 사람들은 보통 ___에 살았습니다. (thatched house)", "초가집", ["기와집", "아파트"], "초가집."),
           read_q("한국민속촌에 갔다 왔습니다"), read_q("민속 마을에서 초가집과 기와집을 구경했습니다"), read_q("전통 혼례식을 구경했습니다"), read_q("오곡밥과 파전을 먹었습니다"), read_q("보름달을 보니까 할머니가 그리워졌습니다")]
    ),
)

# ================================================================== L10 Grammar C: adverbial suffix 으로
_AD = [("역사적", "역사적으로", "historically"), ("세계적", "세계적으로", "globally"), ("국제적", "국제적으로", "internationally"), ("교육적", "교육적으로", "educationally"), ("규칙적", "규칙적으로", "regularly"), ("습관적", "습관적으로", "habitually"), ("긍정적", "긍정적으로", "positively")]
_AD2 = [("독서는 교육적으로 좋습니다.", "Reading is good educationally."), ("나는 매일 규칙적으로 운동합니다.", "I exercise regularly every day."), ("동아리 활동에 적극적으로 참여합니다.", "I actively participate in club activities."), ("태권도는 세계적으로 유명합니다.", "Taekwondo is “globally famous.”")]
_AD3 = [("한국식으로 절을 했습니다.", "I bowed in the Korean style.")]
_AD4 = [("저희 할머니는 지금 연세가 백육 세이시다.", "My grandmother is now 106 years old."), ("할머니께서는 항상 아침 일찍 일어나서 규칙적으로 운동하신다.", "She always gets up early in the morning and exercises regularly."), ("또 매일 채소를 가꾸는 일을 하시면서 습관적으로 몸을 부지런히 움직이신다.", "Also, while doing the work of growing vegetables every day, she habitually moves her body diligently."), ("그리고 손자, 손녀들을 보면서 늘 웃으며 아주 낙천적으로 사신다.", "And she lives very optimistically, always smiling as she looks at her grandsons and granddaughters.")]
_AD5 = [("저는 항상 긍정적으로 생각합니다.", "I always think positively."), ("저는 역사적으로 중요한 곳을 좋아해요.", "I like historically important places."), ("한국 음식은 세계적으로 인기가 있어요.", "Korean food is popular worldwide."), ("저는 습관적으로 아침에 커피를 마십니다.", "I habitually drink coffee in the morning.")]
L10 = lesson(
    "Ch 42 · Grammar C: the adverbial suffix 으로 (~적으로 and ~식으로)",
    "~적으로 · ~식으로 · 규칙적으로 · 긍정적으로 · 세계적으로 · 한국식으로",
    requires=[],
    cards=[
        card("Recall ~적, then add 으로",
             "Recall that the syllable 적 (的) turns a Sino-Korean noun into an adjective when it is attached to the noun: 역사적 (historical), 세계적 (worldwide; global), 국제적 (international), 교육적 (educational), etc. In other words, any Sino-Korean word that ends with the syllable 적 is equivalent to an English adjective that ends with -ic or -ive.\n\nThese adjectives can be turned into adverbs by adding 으로. For example (the English is the book’s):",
             tables=[table(["Adjective", "Adverb", "English"], [[a, b, c] for a, b, c in _AD], say=[0, 1])]),
        card("Sentences with adverbs ending in 으로", "Here are some sentences containing adverbs that end with 으로 (the English is the book’s):", examples=passage(_AD2)),
        card("참고: ~식으로",
             "When 으로 is added to a word ending with 식 (式), it means in the style of: 한국식 → 한국식으로; 자동식 → 자동식으로. (The English is the book’s.)",
             examples=passage(_AD3)),
        card("Follow-up 1 (Listening and speaking): the model",
             "Student A studies the Sino-Korean nouns in List A and Student B those in List B. On the teacher’s cue, Student A makes an adverb with a noun from the list, using ~적으로, and reads it aloud to Student B. Then Student B makes a sentence that includes the adverb. The book’s model is 긍정적으로 → 저는 항상 긍정적으로 생각합니다. My sample sentences (the English is mine):",
             examples=passage(_AD5)),
        card("Follow-up 2 (Reading): a grandmother",
             "Read the following paragraph and circle the adverbs; then translate the sentences containing ~적으로 into English. The paragraph is the book’s with the age spelled out; the English is mine.",
             examples=passage(_AD4)),
        card("The adverbs (mine)", "The adverbs are 규칙적으로 (regularly), 습관적으로 (habitually) and 낙천적으로 (optimistically). Also 항상, 일찍, 부지런히 and 늘 are adverbs, but they do not end with ~적으로. The sentences with ~적으로 are the second, third and fourth sentences above."),
    ],
    exercises=uniq(
        _tr(_AD2 + _AD3 + _AD4 + _AD5 + [(b, c) for a, b, c in _AD], k=3)
        + [M("What does 적 (的) do to a Sino-Korean noun?", "Turns it into an adjective", ["Turns it into a verb", "Makes it plural", "Makes it past"], "The book’s note."), M("What do you add to an adjective in ~적 to make an adverb?", "으로", ["이", "은", "를"], "The book’s note."), M("What does 으로 mean after 식?", "in the style of", ["because of", "toward", "with"], "The book’s note."), M("What does 규칙적으로 mean?", "regularly", ["habitually", "positively", "globally"], "The book’s list."), M("What does 습관적으로 mean?", "habitually", ["regularly", "positively", "educationally"], "The book’s list."), M("What does 긍정적으로 mean?", "positively", ["globally", "habitually", "historically"], "The book’s list."), M("What does 한국식으로 절을 했습니다 mean?", "I bowed in the Korean style", ["I bowed to Koreans", "I did a Korean bow later", "I did not bow"], "The book’s example."), M("What does 태권도는 세계적으로 유명합니다 mean?", "Taekwondo is famous worldwide", ["Taekwondo is new", "Taekwondo is Japanese", "Taekwondo is hard"], "The book’s example."),
           F("나는 매일 ___으로 운동합니다. (regularly)", "규칙적", ["긍정적", "교육적"], "규칙적으로."), F("태권도는 ___으로 유명합니다. (globally)", "세계적", ["규칙적", "습관적"], "세계적으로."), F("동아리 활동에 ___으로 참여합니다. (actively)", "적극적", ["소극적", "교육적"], "적극적으로."), F("독서는 ___으로 좋습니다. (educationally)", "교육적", ["세계적", "역사적"], "교육적으로."), F("한국___으로 절을 했습니다. (style)", "식", ["적", "인"], "한국식으로."),
           read_q("규칙적으로"), read_q("습관적으로"), read_q("긍정적으로"), read_q("세계적으로 유명합니다"), read_q("한국식으로 절을 했습니다")]
    ),
)

# ================================================================== L11 Grammar D: stative verbs interpreted as transitive
_ST1 = [("나는 한국말이 좋다.", "I like Korean.", "I like Korean."), ("나는 매운 김치가 싫다.", "I dislike spicy kimchi.", "I dislike spicy kimchi."), ("나는 우리 가족이 그립다.", "I miss my family.", "I miss my family.")]
_ST2 = [("나는 내 동생이 미워요.", "I hate my younger brother."), ("카메라를 안 가져 온 것이 아쉽다.", "I regret that I didn’t bring my camera."), ("나는 내 친구가 고맙다.", "I am thankful to my friend."), ("시간과 돈이 필요해요.", "I need time and money.")]
_ST3 = [("저는 불고기가 좋아요.", "I like bulgogi."), ("저는 피자가 싫어요.", "I dislike pizza.")]
_ST4 = [("나는 독서가 좋아요.", "I like reading."), ("나는 컴퓨터 게임이 좋아요.", "I like computer games."), ("나는 고양이가 싫어요.", "I hate cats."), ("나는 개가 좋아요.", "I like dogs."), ("나는 우리 개가 그리워요.", "I miss my dog.")]
_ST5 = [("난 사과가 좋아서 매일 먹습니다.", "I like apples, so I eat them every day."), ("사과가 건강에 좋지만 난 사과가 싫어요.", "Apples are good for health, but I dislike apples.")]
_STM = [("저는 가족이 그리워요.", "I miss my family."), ("저는 도움이 필요해요.", "I need help."), ("저는 친구가 고마워요.", "I am thankful to my friend."), ("저는 거짓말하는 사람이 미워요.", "I hate people who tell lies."), ("친구와 같이 못 간 것이 아쉬워요.", "I regret that I couldn’t go together with my friend.")]
L11 = lesson(
    "Ch 42 · Grammar D: stative verbs that are interpreted as transitive verbs (좋다 · 싫다 · 그립다)",
    "~이/가 좋다 · ~이/가 싫다 · ~이/가 그립다 · ~이/가 밉다 · ~이/가 아쉽다 · ~이/가 고맙다 · ~이/가 필요하다",
    requires=[],
    cards=[
        card("Compare the English and Korean sentences",
             "Carefully compare the grammatical differences between the following English sentences and their Korean counterparts (the English is the book’s).",
             examples=passage([(a, b) for a, b, c in _ST1])),
        card("Two differences",
             "There are two noticeable grammatical differences in the examples above.\n\n"
             "1. Verb Type: In the English sentences, the verbs are all transitive verbs (verbs that take an object). In the Korean sentences, their counterparts are all stative verbs (or adjectives). Note that the verbs in blunt formal form are made up of their stems and 다, a common feature of stative verbs.\n\n"
             "2. Functions of the Nouns: In the English sentences, Korean, spicy kimchi, and my family are objects of the verb. In the Korean sentences, their counterparts are all subjects, and the nouns are marked by the subject marker 이/가."),
        card("More verbs that “behave” this way",
             "There are a few more Korean stative verbs that “behave” like 좋다, 싫다, and 그립다. They are 밉다 (to hate a person; to be hateful), 아쉽다 (to be left wanting; to have a sense of regret), 고맙다 (to thank a person; to be thankful), and 필요하다 (to need a person/thing; to be necessary). Examples (the English is the book’s):",
             examples=passage(_ST2)),
        card("Follow-up 3 (Speaking and listening): the model",
             "Partner A studies List A (그립다, 싫다, 고맙다) and Partner B studies List B (좋다, 필요하다, 밉다). Partner A chooses a verb from the list and forms a sentence using the subject marker for objects. The book’s model (the English is mine):",
             examples=dlg([("A", _ST3[0][0], _ST3[0][1]), ("B", _ST3[1][0], _ST3[1][1])])),
        card("Follow-up 4 (Writing): Myoungsoo’s journal",
             "Read the following entry from Myoungsoo’s journal about an English institute in Korea (Basic English Class; Name: James Kim; “My English name is James. Let me introduce myself.”). Translate the underlined sentences into Korean, using ~이/가 for objects; the first sentence is done for you (나는 독서가 좋아요). The underlined sentences are: I like reading. I like computer games. I hate cats. I like dogs. (and the sentences about losing his dog last Saturday, of which the last is) I miss my dog. My translations:",
             examples=passage(_ST4)),
        card("Follow-up 5 (Speaking): a short story", "Two groups each get cards with verbs; each member makes a sentence with the object marked by ~이/가 to build a story. The book’s model (the English is mine):", examples=dlg([("A", _ST5[0][0], _ST5[0][1]), ("B", _ST5[1][0], _ST5[1][1])])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_STM)),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _ST1] + _ST2 + _ST3 + _ST4 + _ST5 + _STM, k=3)
        + [M("What type of verbs are 좋다, 싫다 and 그립다 in Korean?", "Stative verbs (adjectives)", ["Transitive verbs", "Passive verbs", "Causative verbs"], "The book’s note."), M("How is the thing liked or missed marked in Korean?", "With the subject marker 이/가", ["With the object marker 을/를", "With 에서", "With 와/과"], "The book’s note."), M("What does 밉다 mean?", "to hate a person; to be hateful", ["to thank", "to need", "to miss"], "The book’s note."), M("What does 아쉽다 mean?", "to be left wanting; to have a sense of regret", ["to thank", "to hate", "to need"], "The book’s note."), M("What does 고맙다 mean?", "to thank a person; to be thankful", ["to hate", "to regret", "to need"], "The book’s note."), M("What does 필요하다 mean?", "to need a person/thing; to be necessary", ["to hate", "to thank", "to miss"], "The book’s note."), M("What does 나는 우리 가족이 그립다 mean?", "I miss my family", ["My family misses me", "I miss the train", "I hate my family"], "The book’s example."), M("What does 시간과 돈이 필요해요 mean?", "I need time and money", ["I have time and money", "I waste time and money", "Time and money are cheap"], "The book’s example."),
           F("나는 한국말___ 좋다. (I like Korean)", "이", ["을", "에"], "이/가 좋다."), F("나는 매운 김치___ 싫다. (I dislike spicy kimchi)", "가", ["를", "에"], "이/가 싫다."), F("나는 우리 가족___ 그립다. (I miss my family)", "이", ["을", "에"], "이/가 그립다."), F("나는 내 동생___ 미워요. (I hate my brother)", "이", ["을", "에"], "이/가 밉다."), F("시간과 돈___ 필요해요. (I need)", "이", ["을", "에"], "이/가 필요하다."),
           read_q("나는 한국말이 좋다"), read_q("나는 매운 김치가 싫다"), read_q("나는 우리 가족이 그립다"), read_q("나는 내 친구가 고맙다"), read_q("시간과 돈이 필요해요")]
    ),
)

# ================================================================== L12 Activities C + self-eval
_FV = [("신랑 신부가 한복을 입고 서로 절을 합니다.", "f", "The bride and groom wear hanbok and bow to each other.", "A traditional wedding hall"), ("전통 식당에서 오곡밥과 파전을 먹습니다.", "a", "You eat five-grain rice and scallion pancake at a traditional restaurant.", "The marketplace folk restaurant"), ("조선시대 사람들이 살던 전통 가옥을 구경합니다.", "d", "You look at traditional houses where people of the Joseon period lived.", "The folk village"), ("널뛰기, 줄타기, 그네타기 같은 민속 공연을 관람합니다.", "b", "You watch folk performances such as seesaw jumping, tightrope walking and swing riding.", "The performance hall"), ("전통 공예품과 민속촌 엽서를 삽니다.", "c", "You buy traditional crafts and Folk Village postcards.", "The souvenir shop")]
L12 = lesson(
    "Ch 42 · Activities C: where to do what in the Folk Village · and self-evaluation",
    "민속마을 · 공연장 · 장터 · 전통 혼례식장 · 기념품 가게 · 자기 평가",
    requires=[],
    cards=[
        card("Activity 1 (Reading): where can each activity be done?",
             "The following sentences are about activities held at the Korean Folk Village (한국민속촌). The book asks you to read each sentence and identify, from the box, where each activity can be done: a. 장터 민속 음식점; b. 공연장; c. 기념품 가게; d. 민속마을; e. 민속촌 주차장; f. 전통 혼례식장. The sentences are the book’s; the matches and the English are mine.",
             examples=passage([(a, c) for a, b, c, d in _FV]),
             tables=[table(["No.", "Place (mine)"], [[str(i + 1), b + ". " + d] for i, (a, b, c, d) in enumerate(_FV)])]),
        card("The unused place", "Place e. 민속촌 주차장 (the Folk Village parking lot) is not used by any of the five sentences (my note)."),
        card("Activities left out",
             "Activity 2 (listening to Jinho’s narration of his trip to the Korean Folk Village and writing in English in order what he did with his friend: “arrived at the Korean Folk Village at 10:00 a.m.” and “had lunch of vegetable pancakes and five-grain meal at the marketplace” are given), Activity 3 (Sumi’s handwritten note about the activities she has planned for a visit to the Korean Folk Village, which is an image, with a table of places to visit and games to watch) and Activity 4 (the two-part information-gap story about the unexpected incident Yuna’s family experienced at the Korean Folk Village, with the parts not in the printed text I have) are audio, picture and group activities."),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: identify and discuss tourist attractions, festivals, transportation, and lodging; identify and describe cultural events, including traditional weddings and folk games; provide directions to a location; and narrate a past event in a simple paragraph.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; ~뿐(만) 아니라 ~도 (not only … but also …); –(으)ㄹ 수 밖에 없다 (there is no choice but; cannot help -ing); stative verbs that are interpreted as transitive verbs; the adverbial suffix 으로; and the Sino-Korean syllables within 해산물 (海産物), 무명 (無名), 혼례 (婚禮), and 민속촌 (民俗村)."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c, d in _FV], k=3)
        + [M("Where do the bride and groom bow to each other?", "A traditional wedding hall", ["The parking lot", "The marketplace", "The souvenir shop"], "전통 혼례식장."), M("Where can you eat five-grain rice and scallion pancake?", "The marketplace folk restaurant", ["The performance hall", "The souvenir shop", "The wedding hall"], "장터 민속 음식점."), M("Where do you look at traditional houses?", "The folk village", ["The performance hall", "The parking lot", "The restaurant"], "민속마을."), M("Where do you watch tightrope walking?", "The performance hall", ["The folk village", "The souvenir shop", "The restaurant"], "공연장."), M("Where do you buy postcards?", "The souvenir shop", ["The performance hall", "The restaurant", "The wedding hall"], "기념품 가게."), M("Which place is not used in the activity?", "The parking lot", ["The folk village", "The performance hall", "The souvenir shop"], "민속촌 주차장."), M("What should you do if you tick “No” in the self-evaluation?", "Review on your own, study with a partner, tell your advisor or team leader", ["Skip it", "Retake the course", "Nothing"], "The book’s advice."),
           F("신랑 신부가 한복을 입고 서로 ___을 합니다. (bow)", "절", ["널뛰기", "씨름"], "절."), F("민속 공연장에서 ___ 공연을 관람합니다. (tightrope walking)", "줄타기", ["파전", "초가집"], "줄타기."), F("조선시대 사람들이 살던 전통 ___를 구경합니다. (house)", "가옥", ["공연", "엽서"], "가옥."), F("전통 ___와 민속촌 엽서를 삽니다. (craftwork)", "공예품", ["골동품", "해산물"], "공예품."), F("전통 식당에서 오곡밥과 ___을 먹습니다. (scallion pancake)", "파전", ["씨름", "그네"], "파전."),
           read_q("신랑 신부가 서로 절을 합니다"), read_q("전통 식당에서 오곡밥과 파전을 먹습니다"), read_q("전통 가옥을 구경합니다"), read_q("민속 공연을 관람합니다"), read_q("전통 공예품을 삽니다")]
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
    "Ch 42 · Core vocabulary",
    "주요 단어 · 축제 · 관광 · 민속촌 · 혼례 · 뿐만 아니라 · 수밖에 없다",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. 데이트, 카페, 킬로미터, 펜션 and 퍼레이드 are listed also as loan words; the last section lists the Sino-Korean related words of 해(산)물, 무명, 혼례 and 민속촌 as the book gives them.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (약 20킬로미터 → 약 이십 킬로미터; 오늘 저녁 10시 → 오늘 저녁 열 시; 무용가가 3명 → 세 명; L.A. → 엘에이; 음력 1월 15일 → 음력 일월 십오 일; 한국인 무용가가 3명 → 세 명)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 벚꽃 mean?", "cherry blossoms", ["a cherry", "a flower shop", "a spring"], "벚꽃."), M("What does 전야제 mean?", "an event on the eve of a festival", ["a fireworks show", "a parade", "a festival day"], "前夜祭."), M("What does 민박 mean?", "lodging at a private residence", ["a hotel", "a tent", "a Korean-style inn"], "民泊."), M("What does 혼례 mean?", "a (traditional) wedding", ["a funeral", "a birthday", "a holiday"], "婚禮."), M("What does 오곡밥 mean?", "a five-grain meal", ["a bean soup", "seaweed soup", "kimbap"], "五穀."), M("What does 그립다 mean?", "to miss; to yearn for", ["to hate", "to thank", "to regret"], "그립다."), M("What does 아쉽다 mean?", "to be left wanting; to have a sense of regret", ["to be thankful", "to hate", "to miss"], "아쉽다."), M("What does 맛집 mean?", "a restaurant well known for tasty food", ["a cooking class", "a kitchen", "a cafe"], "맛집."),
           F("대학로는 연인들의 ___ 장소로 유명하다. (dating)", "데이트", ["카페", "예술"], "데이트."), F("서해 앞바다에 북한의 ___이 나타났다고 합니다. (warship)", "군함", ["기지", "사관학교"], "군함."), F("시험 공부를 할 때 이 책을 ___하세요. (refer to)", "참고", ["대여", "사정"], "참고."), F("정월 ___에는 보름달이 뜹니다. (the Great Full Moon)", "대보름", ["대문", "대접"], "정월 대보름."), F("작년에 제주도를 구경하지 못해서 ___. (it was a shame)", "아쉬웠어요", ["그리웠어요", "고마웠어요"], "아쉽다."),
           read_q("주요 단어"), read_q("벚꽃"), read_q("전야제"), read_q("혼례"), read_q("민속촌")]
    ),
)

UNIT = unit("Semester 2 · Unit 11 · Chapter 42: Korean Culture II (한국의 문화 2)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])
