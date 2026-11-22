"""Unit 28: KBC Semester 1, Unit 6, Chapter 21 - House Hunting and Moving (집 구하기와 이사하기).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 6, Student's Edition (2022).
Audio, video clips, photos, pictures, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk


def _sub(n):
    return n + ("이" if has_final(n) else "가")


def _obj(n):
    return n + ("을" if has_final(n) else "를")


# ---- the core vocabulary of Chapter 21 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_RE = [
    ("계약", "(契約) a contract; “knotting a promise” (~하다: to contract with)", "마음에 드는 집을 계약했어요."),
    ("계약금", "(契約金) a deposit; down payment", "집을 계약할 때 계약금은 얼마나 내야 해요?"),
    ("공인중개사", "(公認仲介士) a realtor; a real estate agent; “certified mediator”", "집을 사려고 공인중개사를 만났어요."),
    ("보증금", "(保證金) a security deposit; “guarantee money”", "이 아파트는 보증금이 오천만 원입니다."),
    ("부동산", "(不動産) immovable property; a real estate agency", "이사 갈 집을 찾으려면 부동산 사무실에 연락해 보세요."),
    ("월세", "(月貰) a lease (for a house, apartment, building, etc.) on monthly rent payment; “monthly rent”", "이 아파트는 월세여서 매달 돈을 내요."),
    ("전세", "(傳貰) a lease (for a house, apartment, building, etc.) on a large-sum deposit basis; “exclusive rent”", "아파트 전세 계약을 하러 부동산에 갔어요."),
]
_CV_HOUSE = [
    ("~평", "(坪) a traditional unit of area (approximately 3.3 m²)", "이 아파트는 사십오 평이어서 꽤 커요."),
    ("다용도실", "(多用途室) utility room; “multipurpose room”", "세탁기는 다용도실에 놓으세요."),
    ("단독주택", "(單獨住宅) a single-family home", "저는 마당이 있는 단독주택을 찾아요."),
    ("단지", "(團地) a (housing) development; a (housing, industrial, etc.) complex", "우리 아파트 단지에는 편의시설이 많아서 편리해요."),
    ("담(장)", "a fence; a wall", "이 집은 담장이 아주 낮습니다."),
    ("도시가스", "(都市) natural gas (for heating and cooking); “urban gas”", "이 집은 도시가스가 안 들어와서 불편합니다."),
    ("~동", "(洞) a counter for apartment buildings", f"여기 {_kn(1305)} 동이 어디예요?"),
    ("마루", "a wooden floor", "마루는 카펫보다 청소하기에 편해요."),
    ("바닥", "a floor", "바닥이 더러워서 걸레질을 해야겠어요."),
    ("벽", "(壁) a wall; a partition", "그 건물 벽은 회색입니다."),
    ("안방", "a main bedroom; a master bedroom; “inner room”", "우리집 안방은 작습니다."),
    ("온돌", "(溫突) Korean underfloor heating system", "온돌 바닥은 아주 따뜻해요."),
    ("전망", "(展望) a view; prospect", "그 방은 바다가 보여서 전망이 좋아요."),
    ("정원", "(庭園) a garden", "정원에 꽃과 나무가 많아요."),
    ("지붕", "a roof", "그 집의 지붕은 파란색입니다."),
    ("지역", "(地域) an area; zone; district; “land boundary”", "서울 경기 지역은 오늘 비가 오겠습니다."),
    ("천장", "(天障) a ceiling; “sky blocking”", "이 집은 천장이 높고 밝아요."),
    ("현관", "(玄關) the main entrance", "현관에 들어가면 신발을 벗으세요."),
    ("환경", "(環境) an environment; surroundings; a circumstance", "이 아파트는 주변 환경이 좋습니다."),
]
_CV_MOVE = [
    ("싸다", "to wrap; to pack", "여행 가기 하루 전에 짐을 싸세요."),
    ("이사", "(移徙) moving (~하다: to move to a new place)", "다음 달에 새 집으로 이사합니다."),
    ("이삿짐", "moving items; “moving load”", "이삿짐이 많아서 힘들었어요."),
    ("이삿짐 센터", "a moving company; “a moving load center”", "이삿짐 센터에서 이삿짐을 옮겨 줬어요."),
    ("정리", "(整理) arrangement; organization (~하다/되다: to arrange; to organize/to be arranged; to be organized)", "책상 위에 있는 책을 정리하세요."),
]
_CV_LOAN = [("가스", "gas", "우리 아파트는 엘피지 가스를 씁니다."), ("베란다 / 발코니", "a veranda; a balcony", "아파트에는 베란다가 있습니다.")]
_CV_OTH = [
    ("고층", "(高層) a high-rise; higher stories; “high floor”", "고층 아파트에 살고 싶어요."),
    ("공기", "(空氣) air", "공기가 없으면 우리는 살 수 없어요."),
    ("광고", "(廣告) an advertisement; “wide announcement”", "신문 광고를 보고 아파트를 찾았습니다."),
    ("구하다", "(求) to look for; to seek", "방 세 개짜리 아파트를 구하고 있어요."),
    ("꽤", "quite", "출퇴근 시간에는 교통이 꽤 복잡합니다."),
    ("나머지", "the rest, the remainder", "계약금을 십 퍼센트만 내고 나머지는 이사할 때 드리겠습니다."),
    ("낮다", "to be low", "오늘은 기온이 아주 낮습니다."),
    ("나중에", "later", "보증금을 먼저 내고 나머지는 나중에 내세요."),
    ("-(으)ㄴ/는 편이다", "to be “on the side of”", "요즘 학생들은 아침 식사를 안 하는 편입니다."),
    ("-(으)려고 하다", "to intend to; to plan to", "내년에 집을 사려고 합니다."),
    ("-(으)ㄹ까 하다", "to consider doing; might; could; may", "이번 주말에 동생하고 영화를 볼까 해."),
    ("모든", "all", "포장 이사를 하면 이삿짐 센터에서 모든 짐을 다 싸 줍니다."),
    ("멀리", "far away", "우리 아파트에서는 멀리 산이 보입니다."),
    ("밝다", "to be bright (in color, light or mood)", "벽이 흰색이어서 집이 아주 밝아요."),
    ("벌써", "already", "지난주에 벌써 이사했어요."),
    ("상가", "(商街) a shopping district; a commercial quarter; a shopping mall; “business street”", "이 지역 주변에 상가가 많아서 쇼핑하기 편리해요."),
    ("새~", "new", "다음 달에 새 아파트로 이사 갈 거예요."),
    ("신청", "(申請) an application; a request; a petition (~하다: to apply; to request)", "전화 서비스 신청은 전화국에 하세요."),
    ("(~이/가) 싫다", "to dislike", "매일 아침에 면도하는 것이 싫어요."),
    ("(~을/를) 싫어하다", "to dislike", "매일 아침에 면도하는 것을 싫어해요."),
    ("알리다", "to inform; to tell; to announce", "손님, 주소와 전화번호 좀 알려 주세요."),
    ("어둡다", "to be dark; to be dim (in color, light or mood)", "불을 켜지 않아서 방이 어두워요."),
    ("전화국", "(電話局) a telephone company", "전화가 고장이 나면 전화국에 연락하세요."),
    ("정하다", "(定) to decide", "이사 날짜 정하셨어요?"),
    ("정확하다", "(正確) to be exact; to be precise", "정확한 시간을 알고 싶으면 휴대폰 시계를 보세요."),
    ("특히", "(特) particularly", "이 집은 특히 마당이 넓어요."),
    ("편의시설", "(便宜施設) (residential) amenities; “convenience facilities”", "그 학교에는 어떤 편의시설이 있어요?"),
    ("평일", "(平日) weekdays; “regular day”", f"평일 오전에는 티켓이 {sino(10)} 퍼센트 할인됩니다."),
    ("한꺼번에", "all at the same time; all at once", f"한꺼번에 돈을 내시면 {sino(5)} 퍼센트 할인해 드립니다."),
]
_CV_SINO = [("다", "(多) many; numerous; multi-", "다용도실, 다소, 다량, 다수"), ("동", "(動) move; mobile", "자동차, 이동 전화, 부동산"), ("이", "(移) move; transfer", "이사, 이민, 이주, 이동")]
_ALL = {r[0]: r for r in _CV_RE + _CV_HOUSE + _CV_MOVE + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"욕실": "a bathroom (mine)", "화장실": "a restroom; a bathroom (mine)", "주방": "a kitchen (mine)", "거실": "a living room (mine)", "침실": "a bedroom (mine)", "아파트": "an apartment (mine)", "마당": "a yard (mine)", "원룸": "a studio apartment; “one room”", "오피스텔": "an officetel (a type of apartment; from office + hotel)", "조용하다": "to be quiet",
          "다문화 가정": "a multicultural family (mine)", "다소": "somewhat; more or less (mine)", "최다": "the largest number; the most (mine)", "다수": "a large number", "다량": "a large amount", "동물": "an animal; “moving thing”", "행동": "behavior; action (mine)", "동력": "power; motive force (mine)", "전동차": "an electric train car (mine)", "운동장": "an athletic field; a playground (mine)", "동영상": "a video; “moving image” (mine)",
          "이민": "immigration; emigration (mine)", "이주": "migration; moving one’s residence (mine)", "이동": "movement; transfer (mine)", "이동 통신": "mobile communication (mine)", "부엌": "a kitchen (mine)", "건너편": "the opposite side (mine)", "뒤쪽": "the back side (mine)", "주차장": "a parking lot (mine)", "빌라": "a villa (a type of low-rise apartment house) (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)


# ================================================================== L1: objectives and the Sino-Korean syllable 다
_DA = [("다수", "a large number (the book’s example)"), ("다량", "a large amount (the book’s example)"), ("다자회담", "a multiparty conference (the book’s example)"), ("다국적 기업", "a multinational enterprise (the book’s example)"), ("다문화 가정", "a multicultural family (mine)"),
       ("다용도실", "a utility room; “multipurpose room” (the book’s core word)"), ("다소", "somewhat; more or less (mine)"), ("최다", "the largest number; the most (mine)"), ("석", "evening (夕, the book’s note)")]
L1 = lesson(
    "Ch 21 · What the chapter teaches and the Sino-Korean syllable 다",
    "집 구하기와 이사하기 · 다 (多) · 다수 · 다량 · 다국적 기업 · 다용도실",
    requires=[],
    cards=[
        card("What Chapter 21 teaches (집 구하기와 이사하기)",
             "Chapter 21, “House Hunting and Moving”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: talk about two major types of housing, single-family homes and apartments; describe in a simple paragraph rooms and other components of a house or apartment; ask for basic information about renting a house; ask for basic information about moving, including moving services and types of moves; and give simple instructions about how to prepare for moving.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; -(으)려고 하다 (to intend to; to plan to); -(으)ㄴ/는 편이다 used to make a nonassertive statement; -(으)ㄹ까 하다 used to imply a speaker’s uncertainty; 좋다 vs. 좋아하다 (to like); 싫다 vs. 싫어하다 (to dislike); and the Sino-Korean syllables 다 (多), 동 (動) and 이 (移)."),
        card("Sino-Korean in use: 다 (多)",
             "This Sino-Korean syllable means many, much or numerous, as in 다수 (a large number) and 다량 (a large amount). If you look at the Chinese character 多, you will notice that the same shape 夕 repeats twice vertically. The shape alone stands as a complete character, with 석 (夕) meaning evening. 夕 originated from the shape of the crescent moon in the evening. Thus the meaning of 다 (多) came from “evening after evening, time after time, or a lot of time”. When the syllable is used as a prefix, it can be translated as multi-, as in 다자회담 (a multiparty conference) and 다국적 기업 (a multinational enterprise).\n\n"
             "The book asks you to guess the meaning of 다문화 가정, 다용도실, 다소 and 최다. The answers are mine, except 다용도실, which is a core word.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _DA], say=[0])]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board activities) and Activity 3 (the “Taboo” game, which the teacher starts) are picture, computer or game activities."),
    ],
    exercises=uniq(
        _tr(_DA)
        + [M("What does the Sino-Korean syllable 다 (多) mean?", "many; numerous; multi-", ["move; transfer", "medicine", "victory"], "다수, 다량, 다자회담."), M("What does 석 (夕) mean?", "evening", ["many", "a moon", "a rice plant"], "多 repeats 夕 twice."), M("What does 다수 mean?", "a large number", ["a large amount", "a small number", "a few"], "다수 = a large number."),
           M("What does 다량 mean?", "a large amount", ["a large number", "a small amount", "a few"], "다량 = a large amount."), M("What does 다국적 기업 mean?", "a multinational enterprise", ["a small shop", "a national bank", "a school"], "다 (multi-) + 국적 + 기업."), M("What does 다자회담 mean?", "a multiparty conference", ["a two-person talk", "a school meeting", "a phone call"], "다 (multi-) + 자 + 회담."),
           M("What does 다용도실 mean?", "a utility room; “multipurpose room”", ["a bedroom", "a kitchen", "a garden"], "다 + 용도 + 실."), M("What does 다문화 가정 mean?", "a multicultural family", ["a large family", "a happy family", "a new family"], "다 (multi-) + 문화 + 가정."),
           F("이 집에는 ___용도실이 있습니다. (multi-)", "다", ["동", "이"], "다용도실 = a utility room."), F("물건을 ___량 샀습니다. (a large amount)", "다", ["동", "이"], "다량 = a large amount."),
           read_q("다수"), read_q("다량"), read_q("다국적 기업"), read_q("다용도실"), read_q("다문화 가정")]
    ),
)

# ================================================================== L2: Topic A
_A_TEXT = [
    ("우리 가족은 지난주에 단독주택에서 아파트로 이사했습니다.", "My family moved from a single-family house to an apartment last week."),
    ("새 집에는 침실 세 개, 욕실, 거실 그리고 주방이 있습니다.", "The new home has three bedrooms, a bathroom, a living room and a kitchen."),
    ("현관으로 들어가면 오른쪽에 내 방과 거실이 있고 왼쪽에는 주방과 욕실이 있습니다.", "If you go in through the entrance, my room and the living room are on the right, and the kitchen and the bathroom are on the left."),
    ("욕실 옆에는 부모님이 쓰시는 안방이 있습니다.", "Next to the bathroom is the main bedroom that my parents use."),
    ("안방 바로 옆에는 오빠 방이 있습니다.", "Right next to the main bedroom is my older brother’s room."),
    ("그리고 주방 왼쪽에는 다용도실이 있고 거실 오른쪽에는 베란다가 있습니다.", "And to the left of the kitchen there is a utility room, and to the right of the living room there is a veranda."),
    ("거실 바닥은 마루이고 온돌입니다.", "The living room floor is a wooden floor, with ondol heating."),
    ("벽이 하얀색이어서 집이 아주 밝습니다.", "The walls are white, so the home is very bright."),
    ("특히, 아파트가 고층이어서 멀리 한강도 보입니다.", "In particular, the apartment is on a high floor, so I can even see the Han River far away."),
    ("아파트 단지 내에는 상가와 편의시설이 있어서 생활하기가 편리합니다.", "Within the apartment complex there are shops and amenities, so it is convenient to live."),
    ("정원이 없지만 단지 내에 공원이 있어서 가끔 가족들과 함께 산책을 합니다.", "There is no garden, but there is a park within the complex, so sometimes I take a walk with my family."),
    ("우리 가족 모두가 새 집을 좋아합니다.", "All of my family like the new home."),
]
_A_WORDS = ["고층", "다용도실", "단독주택", "단지", "담(장)", "마루", "멀리", "바닥", "밝다", "베란다 / 발코니", "벽", "상가", "새~", "안방", "어둡다", "온돌", "이사", "정원", "지붕", "천장", "특히", "편의시설", "현관"]
_ROOMS = [("욕실 / 화장실", "a bathroom / a restroom"), ("주방", "a kitchen"), ("다용도실", "a utility room"), ("현관", "the main entrance"), ("거실", "a living room"), ("침실", "a bedroom"), ("베란다", "a veranda")]
L2 = lesson(
    "Ch 21 · Topic A: My family has moved to a new apartment",
    "우리 가족은 새 아파트로 이사했습니다 · 침실 · 욕실 · 거실 · 주방 · 현관 · 온돌",
    requires=[],
    cards=[
        card("Topic A: My family has moved to a new apartment (우리 가족은 새 아파트로 이사했습니다)",
             "Jihyun describes her new apartment to her class. (The English is mine; the book gives none.)",
             examples=passage(_A_TEXT)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened. The book shows pictures of a single-family house and an apartment complex and a floor plan with the names of the rooms.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("The rooms (the floor plan)",
             "The names of the rooms on the book’s floor plan. The English is mine, except 다용도실, 현관 and 베란다, which are core words.",
             tables=[ktable(_ROOMS)]),
        card("Cultural note: Ondol and the sitting culture",
             "온돌 is a traditional Korean under-floor heating system that uses direct heat transfer from the kitchen fireplace or stove to the underside of a stone floor. 온돌 has long been an integral part of Korean culture and may date back to as early as 37 b.c.e.; it has remained in use for millennia in Korea and continues to be a typical feature of the Korean home. Nowadays, 온돌 refers to any type of under-floor heating system. 온돌 is widely credited for distinctive Korean customs, such as removing one’s shoes upon entering a home and sitting on the floor."),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity and Follow-up 1 (listening to four dialogs about a new home and filling in the type of housing and the reason it was chosen) are computer or audio activities. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not w.startswith("~") and "/" not in w and "(" not in w and w != "새~"]))
        + _tr(_A_TEXT + _ROOMS)
        + [M("What did Jihyun’s family move from, and to?", "From a single-family house to an apartment", ["From an apartment to a house", "From Seoul to Busan", "From a hotel to a house"], "단독주택에서 아파트로 이사했습니다."), M("How many bedrooms does the new home have?", "Three", ["Two", "Four", "One"], "침실 세 개."),
           M("What is on the right when you enter?", "Jihyun’s room and the living room", ["The kitchen and the bathroom", "The main bedroom", "The veranda"], "오른쪽에 내 방과 거실이 있고."), M("What is next to the bathroom?", "The main bedroom", ["The kitchen", "Her brother’s room", "The veranda"], "욕실 옆에는 부모님이 쓰시는 안방이 있습니다."),
           M("Whose room is right next to the main bedroom?", "Her older brother’s", ["Her sister’s", "Her own", "Her parents’"], "안방 바로 옆에는 오빠 방이 있습니다."), M("What is to the right of the living room?", "A veranda", ["A utility room", "A kitchen", "A bathroom"], "거실 오른쪽에는 베란다가 있습니다."),
           M("What is the living room floor?", "A wooden floor with ondol heating", ["A carpet", "A tile floor", "Stone"], "거실 바닥은 마루이고 온돌입니다."), M("Why is the home bright?", "The walls are white", ["The windows are huge", "It is a new building", "There is a garden"], "벽이 하얀색이어서."),
           M("What can Jihyun see far away?", "The Han River", ["A mountain", "The sea", "The airport"], "멀리 한강도 보입니다."), M("What is there within the complex?", "Shops, amenities and a park", ["A school and a hospital", "Only a parking lot", "Nothing"], "상가와 편의시설, 공원."),
           M("What is the garden situation?", "There is no garden, but there is a park in the complex", ["There is a big garden", "There is a garden on the roof", "There is no park"], "정원이 없지만 단지 내에 공원이 있어서."),
           F("현관으로 들어가면 ___에 내 방과 거실이 있고. (on the right)", "오른쪽", ["왼쪽", "앞쪽"], "오른쪽 = the right side."), F("안방 ___ 옆에는 오빠 방이 있습니다. (right)", "바로", ["벌써", "특히"], "바로 옆 = right next to."), F("아파트가 ___이어서 멀리 한강도 보입니다. (a high floor)", "고층", ["저층", "다용도실"], "고층 = a high-rise."),
           F("거실 ___은 마루이고 온돌입니다. (floor)", "바닥", ["벽", "천장"], "바닥 = a floor."), F("___이 하얀색이어서 집이 아주 밝습니다. (walls)", "벽", ["바닥", "지붕"], "벽 = a wall."), F("그 집에는 ___이 있어서 가끔 산책을 합니다. (a park)", "공원", ["정원", "담장"], "공원 = a park."),
           read_q("단독주택에서 아파트로 이사했습니다"), read_q("침실 세 개"), read_q("현관으로 들어가면"), read_q("다용도실"), read_q("벽이 하얀색이어서 집이 아주 밝습니다")]
    ),
)

# ================================================================== L3: Follow-up 2 article and Activities A
_ART = [
    ("아파트와 단독주택", "Apartments and single-family houses"),
    ("한국 사람들이 살고 싶어 하는 집은 아파트 오십 점 일 퍼센트, 단독주택 삼십이 점 일 퍼센트, 그리고 오피스텔 육 점 이 퍼센트, 빌라 십일 점 육 퍼센트 순이다.", "The homes Korean people want to live in are, in order, apartments 50.1%, single-family houses 32.1%, and officetels 6.2% and villas 11.6%. (the book’s order of the last two is as printed)"),
    ("사람들이 아파트를 좋아하는 이유는 무엇일까?", "Why do people like apartments?"), ("무엇보다 아파트는 편리하다.", "Above all, apartments are convenient."), ("아파트 단지에는 주차장이 있고 상가와 여러 가지 편의시설이 있다.", "In an apartment complex there is a parking lot, and there are shops and various amenities."),
    ("그럼, 사람들이 단독주택을 좋아하는 이유는 무엇일까?", "Then why do people like single-family houses?"), ("단독주택은 마당이 있어서 꽃이나 나무를 심을 수 있다.", "A single-family house has a yard, so you can plant flowers or trees."), ("또 아이들이 마당에서 놀 수 있다.", "Also, children can play in the yard."), ("그리고 집에서는 동물도 기를 수 있다.", "And you can also raise animals at home."),
]
_SJ = [
    ("저희 집은 녹원 아파트 십칠 층입니다.", "Our home is on the 17th floor of the Nokwon Apartments."), ("방은 세 개 있고 욕실은 한 개 있습니다.", "There are three rooms and one bathroom."), ("먼저 현관으로 들어가면 앞에 거실이 보입니다.", "First, if you go in through the entrance, you see the living room in front."),
    ("거실 바닥은 마루이고 벽은 노란색입니다.", "The living room floor is a wooden floor and the walls are yellow."), ("현관에서 오른쪽에 욕실이 있고 왼쪽에는 제 여동생 방이 있습니다.", "From the entrance, the bathroom is on the right, and my younger sister’s room is on the left."),
    ("제 여동생 방 바로 옆에 부엌이 있습니다.", "Right next to my younger sister’s room is the kitchen."), ("부엌 뒤쪽에 다용도실이 있는데 조금 작고 어둡습니다.", "Behind the kitchen is a utility room, which is a little small and dark."), ("또 부엌 옆에는 제 방이 있습니다.", "Also, next to the kitchen is my room."), ("제 방 건너편에 부모님 방이 있습니다.", "On the opposite side of my room is my parents’ room."),
]
_MODEL = [("방 네 개짜리 전세 아파트 있어요?", "Do you have a four-room 전세 apartment? (A)"), ("네, 있습니다. 오십 평 아파트가 하나 나왔어요. 방이 네 개, 화장실이 두 개예요.", "Yes, we do. A 50-pyeong apartment has come up. It has four rooms and two bathrooms. (B)"), ("그 지역 교통은 편리한가요?", "Is the transportation in that area convenient? (A)"), ("그럼요. 지하철 역이 아주 가까워요.", "Of course. The subway station is very close. (B)")]
L3 = lesson(
    "Ch 21 · Topic A, Follow-up 2 and Activities A: housing types and a parents’ apartment",
    "아파트와 단독주택 · 마당 · 주차장 · 녹원 아파트 · 거실 바닥은 마루 · 전세 아파트",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): an article on housing preferences",
             "The book gives an article about preferences for different types of housing and the reasons, and asks you to fill in a table in English (the percent of Korean people preferring each type, and the reasons). The text is the book’s (the percentages are spelled out in Hangul); the English is mine.",
             examples=passage(_ART)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["", "Single-family house", "Apartment"], [["Percent preferring", "32.1%", "50.1%"], ["Reasons", "A yard for planting flowers or trees; children can play in the yard; you can raise animals at home", "Convenient; parking lot, shops and various amenities in the complex"]])]),
        card("Activity 2 (Reading): Sungjoon’s parents’ apartment",
             "The passage is Sungjoon’s description of his parents’ apartment; the book asks three questions in English (how he describes the floor and walls of the living room; where the bathroom is; how he describes the multi-use room). The text is the book’s (17층 is spelled out); the English is mine.",
             examples=passage(_SJ)),
        card("The answers (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Question", "Answer (mine)"], [["How does he describe the floor and walls of the living room?", "The floor is wooden and the walls are yellow"], ["Where is the bathroom?", "To the right as you come in from the entrance"], ["How does he describe the multi-use room?", "It is behind the kitchen, and it is a little small and dark"]])]),
        card("Activity 4: renting an apartment (the model)",
             "In the role-play of Activity 4 (realtors and prospective renters visit each other’s booths) the book gives this model (the English is mine; the book writes 50평, spelled out here):",
             examples=passage(_MODEL)),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and listening to three short dialogs about a new home) and Activity 3 (listening to three conversations between a home owner and a visitor) are computer or audio activities. Activity 4 of this chapter’s first part (민박집 찾기: two homestay flyers for Jeju Island, whose texts are not in the book’s text, with a table of type of housing, number and size of rooms, house features, surrounding environment and additional information, in pairs) and the rental role-play with situation cards are partner and class activities."),
    ],
    exercises=uniq(
        _tr(_ART + _SJ + _MODEL)
        + [M("Which housing type do most Korean people want?", "An apartment", ["A single-family house", "An officetel", "A villa"], "아파트 오십 점 일 퍼센트."), M("What percent want a single-family house?", "32.1%", ["50.1%", "6.2%", "11.6%"], "단독주택 삼십이 점 일 퍼센트."),
           M("What is the main reason people like apartments?", "They are convenient", ["They are cheap", "They have a yard", "They are old"], "무엇보다 아파트는 편리하다."), M("What is in an apartment complex?", "A parking lot, shops and amenities", ["A farm", "A yard", "A river"], "주차장이 있고 상가와 여러 가지 편의시설이 있다."),
           M("Why do people like single-family houses?", "They have a yard, so you can plant things and children can play", ["They are tall", "They are near the subway", "They are cheap"], "마당이 있어서."), M("Which floor is Sungjoon’s family’s apartment on?", "The 17th floor", ["The 7th floor", "The 1st floor", "The 10th floor"], "십칠 층."),
           M("What color are the living room walls?", "Yellow", ["White", "Blue", "Gray"], "벽은 노란색입니다."), M("Where is Sungjoon’s younger sister’s room?", "On the left from the entrance", ["On the right from the entrance", "Behind the kitchen", "Across from his room"], "왼쪽에는 제 여동생 방이 있습니다."),
           M("Where is the utility room?", "Behind the kitchen", ["Next to the entrance", "Across from the living room", "Next to the bathroom"], "부엌 뒤쪽에 다용도실이 있는데."), M("Where are Sungjoon’s parents’ rooms?", "Across from his room", ["Next to the kitchen", "Behind the kitchen", "Next to the bathroom"], "제 방 건너편에 부모님 방이 있습니다."),
           F("아파트는 ___ 편리하다. (above all)", "무엇보다", ["특히", "벌써"], "무엇보다 = above all."), F("단독주택은 ___이 있어서 꽃이나 나무를 심을 수 있다. (a yard)", "마당", ["벽", "지붕"], "마당 = a yard."), F("제 방 ___에 부모님 방이 있습니다. (across)", "건너편", ["뒤쪽", "바로 옆"], "건너편 = the opposite side."),
           read_q("아파트와 단독주택"), read_q("편의시설"), read_q("현관에서 오른쪽에 욕실이 있습니다"), read_q("조금 작고 어둡습니다"), read_q("전세 아파트 있어요")]
    ),
)

# ================================================================== L4: Topic B
_B_DLG = [
    ("이희정", "아파트를 구하고 있는데 좋은 아파트 있어요?", "I am looking for an apartment. Do you have a good apartment?"),
    ("공인중개사", "월세를 원하세요? 전세를 원하세요?", "Do you want monthly rent? Do you want 전세?"),
    ("이희정", "전세 아파트를 찾고 있어요.", "I am looking for a 전세 apartment."),
    ("공인중개사", "네, 이 근처에 삼십사 평짜리가 하나 있어요. 방이 세 개이고 꽤 넓은 편이에요.", "Yes, there is a 34-pyeong one near here. It has three rooms and is rather spacious."),
    ("이희정", "몇 층에 있어요? 저는 낮은 층은 싫어요.", "Which floor is it on? I don’t like low floors."),
    ("공인중개사", "십일 층에 있어요.", "It is on the 11th floor."),
    ("이희정", "좋네요. 한번 볼 수 있어요? 근데 아파트 주변 환경은 어때요?", "That’s good. Can I see it once? By the way, how is the environment around the apartment?"),
    ("공인중개사", "아파트 단지 옆에 큰 공원이 있어요. 그래서 공기도 좋고 전망도 아주 좋아요.", "There is a big park next to the apartment complex. So the air is good and the view is very good, too."),
    ("이희정", "참, 교통은 편리해요?", "Oh, is the transportation convenient?"),
    ("공인중개사", "그럼요. 지하철 역과 버스 정류장이 아주 가까워요.", "Of course. The subway station and the bus stop are very close."),
    ("이희정", "그렇군요. 전세 보증금은 한꺼번에 내야 해요?", "I see. Do I have to pay the 전세 deposit all at once?"),
    ("공인중개사", "먼저 계약금을 내시고 나머지는 나중에 주시면 됩니다. 이사는 언제 하시려고요?", "First pay the down payment, and you can give the rest later. When are you planning to move?"),
    ("이희정", "다음 달에 이사를 가려고 해요.", "I plan to move next month."),
]
_B_WORDS = ["계약", "계약금", "공기", "공인중개사", "구하다", "꽤", "나머지", "나중에", "낮다", "-(으)려고 하다", "보증금", "부동산", "월세", "전망", "전세", "지역", "-(으)ㄴ/는 편이다", "~평", "한꺼번에", "환경"]
_DONG = [("동물", "an animal; “moving thing” (the book’s Chapter 19 word)"), ("자동차", "an automobile; “self-moving car” (the book’s example)"), ("부동산", "real estate; “not movable property” (the book’s example)"), ("행동", "behavior; action (mine)"), ("동력", "power; motive force (mine; 力 = power)"), ("전동차", "an electric train car (mine)"), ("운동장", "an athletic field; a playground (mine)"), ("동영상", "a video; “moving image” (mine)")]
_FILL = [("공인중개사", "a real estate agency; the book’s table gives “a real estate agency” for the first word (the book’s blank)"), ("공기", "air"), ("환경", "an environment"), ("전망", "a view"), ("지역", "an area; district"), ("꽤", "quite"), ("한꺼번에", "all at once"), ("보증금", "a security deposit"), ("계약", "a contract; to contract with"), ("월세", "monthly rent"), ("전세", "a lease on a large-sum deposit basis"), ("~평", "a traditional land measure in Korea")]
L4 = lesson(
    "Ch 21 · Topic B: What kind of apartment are you looking for?",
    "어떤 아파트를 구하세요? · 전세 · 월세 · 보증금 · 계약금 · 동 (動) · 평",
    requires=[],
    cards=[
        card("Topic B: What kind of apartment are you looking for? (어떤 아파트를 구하세요?)",
             "Heejeong, who is looking for an apartment, talks to a real estate agent. (The English is mine; the book gives none. The book writes 34평 and 11층; they are spelled out here.)",
             examples=dlg(_B_DLG)),
        card("The book’s footnotes",
             "1. 평 is traditionally a land unit measure in Korea. One 평 measures approximately 3.3 square meters or 35.5 square feet.\n2. As introduced in Chapter 5, 금 (金) refers to metal or gold. It is also translated as money or a fee, as in 요금, 보증금, 전세금, 계약금, etc."),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Cultural note: 전세 and 월세",
             "In Korea, there are two major types of rental arrangements for a house, an apartment, a store, a building, etc.: 전세 and 월세. 전세, whose literal meaning is exclusive rent, is the more common rental arrangement in which the renter pays approximately 60 to 80% of the property price as a deposit but pays no monthly rent. The deposit is paid back when the lease contract expires. 월세, which literally means monthly rent, is the combination of 전세 and a typical monthly rental in the U.S. You pay about 20% of the market value of the house as a deposit and a fixed amount each month as a rental charge."),
        card("Sino-Korean in use: 동 (動)",
             "This Sino-Korean syllable means move or mobile, as in 자동차 (an automobile; “self-moving car”) and 부동산 (real estate; “not movable property”). The shape of the Chinese character gives you some indication of the meaning, if you understand that 重 (중) means heavy and 力 (역/력) means power. In order to “move” heavy stuff, you need to add power. The book asks you to guess the meaning of 동물, 행동, 동력, 전동차, 운동장 and 동영상. The answers are mine, except those marked as the book’s.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _DONG], say=[0])]),
        card("Presentation Activity a: the vocabulary table",
             "The book gives a table of ten core words and English meanings with some blanks to fill in, in both directions (공인중개사, 공기, 전세, 지역, 꽤, 한꺼번에 and -(으)ㄴ/는 편이다; environment, a real estate agency, a view, a traditional land measure in Korea, a security deposit, monthly rent, a contract; to contract with). Its answers are the core words above; the matching of the pairs is mine:",
             tables=[ktable([("공인중개사", "a real estate agent"), ("공기", "air"), ("전세", "a lease on a large-sum deposit basis"), ("지역", "an area; district"), ("꽤", "quite"), ("한꺼번에", "all at once"), ("-(으)ㄴ/는 편이다", "to be “on the side of”"), ("환경", "an environment"), ("부동산", "a real estate agency"), ("전망", "a view"), ("~평", "a traditional land measure in Korea"), ("보증금", "a security deposit"), ("월세", "monthly rent"), ("계약", "a contract; to contract with")])]),
        card("Activities left out",
             "The SMART Board activity and the sentence strips of the Presentation Activity (the customer and the realtor, sorting the strips and arranging them into a conversation) are computer, partner or class activities. Follow-up 1 and 2 are in the next lesson (Follow-up 2 is a listening activity: phone conversations between a realtor and a customer)."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("-", "~"))]))
        + _tr(_strip(_B_DLG) + _DONG)
        + [M("What is Heejeong looking for?", "A 전세 apartment", ["A 월세 apartment", "A house", "A studio"], "전세 아파트를 찾고 있어요."), M("How big is the apartment the agent has?", "34 pyeong with three rooms", ["12 pyeong with one room", "50 pyeong with four rooms", "105 square meters"], "삼십사 평짜리, 방이 세 개."),
           M("Which floors does Heejeong dislike?", "Low floors", ["High floors", "The top floor", "The ground floor only"], "낮은 층은 싫어요."), M("Which floor is the apartment on?", "The 11th floor", ["The 1st floor", "The 3rd floor", "The 20th floor"], "십일 층."),
           M("What is next to the apartment complex?", "A big park", ["A school", "A market", "A river"], "큰 공원이 있어요."), M("How is the transportation?", "Convenient; the subway station and the bus stop are close", ["Inconvenient", "There is no bus", "Far from the subway"], "지하철 역과 버스 정류장이 아주 가까워요."),
           M("How can the 전세 deposit be paid?", "The down payment first and the rest later", ["All at once only", "Monthly", "After moving out"], "먼저 계약금을 내시고 나머지는 나중에."), M("When does Heejeong plan to move?", "Next month", ["Next year", "This week", "Tomorrow"], "다음 달에 이사를 가려고 해요."),
           M("In 전세, how much is the deposit, roughly?", "60 to 80% of the property price", ["About 20%", "10%", "100%"], "The book’s cultural note."), M("In 월세, how much is the deposit, roughly?", "About 20% of the market value", ["60 to 80%", "5%", "100%"], "The book’s cultural note."), M("What does 동 (動) mean?", "move; mobile", ["many", "medicine", "victory"], "자동차, 부동산."),
           F("먼저 ___을 내시고 나머지는 나중에 주시면 됩니다. (the down payment)", "계약금", ["보증금", "월세"], "계약금 = a deposit; down payment."), F("저는 ___ 층은 싫어요. (low)", "낮은", ["높은", "넓은"], "낮다 + ㄴ = 낮은."), F("전세 보증금은 ___ 내야 해요? (all at once)", "한꺼번에", ["나중에", "벌써"], "한꺼번에 = all at once."),
           F("꽤 넓은 ___이에요. (rather)", "편", ["평", "층"], "넓은 편이에요 = is rather spacious."), F("다음 달에 이사를 가___ 해요. (plan to)", "려고", ["는 것", "자마자"], "-(으)려고 하다 = to plan to."), F("이 근처에 삼십사 ___짜리가 하나 있어요. (pyeong)", "평", ["층", "동"], "평 = a unit of area."),
           read_q("전세 아파트를 찾고 있어요"), read_q("삼십사 평짜리"), read_q("꽤 넓은 편이에요"), read_q("전세 보증금"), read_q("계약금을 내시고")]
    ),
)

# ================================================================== L5: Topic B follow-up 1, Activities B
_RE_AD = [
    ("좋은 집을 구하실 때, 마음에 드는 집을 찾으실 때, 서울부동산", "When you look for a good house, when you look for a house you like: Seoul Real Estate"),
    ("단독주택, 연희동, 방 네 개, 욕실 두 개, 조용하고 밝은 집, 보증금 일억 원, 월세 오백만 원", "Single-family house, Yeonhui-dong, 4 rooms, 2 bathrooms, a quiet and bright house, deposit 100,000,000 won, monthly rent 5,000,000 won"),
    ("아파트, 백오 제곱미터, 상암동, 방 세 개, 욕실 두 개, 지하철 역 주변, 전세 오억 오천만 원", "Apartment, 105 m², Sangam-dong, 3 rooms, 2 bathrooms, near a subway station, 전세 550,000,000 won"),
    ("원룸, 십이 평, 이대 앞, 넓은 거실과 화장실, 지하철 역에서 오 분 거리, 월세 구십만 원, 보증금 이천만 원", "Studio, 12 pyeong, in front of Ewha Women’s University, a wide living room and a bathroom, 5 minutes from the subway station, monthly rent 900,000 won (deposit 20,000,000 won)"),
]
_JOURNAL = [
    ("팔월 이십사 일, 맑음", "August 24, sunny"), ("지난 주말에 새집으로 이사를 했다.", "Last weekend I moved to my new home."), ("방이 세 개짜리 월세 아파트인데, 꽤 넓은 편이다.", "It is a monthly-rent apartment with three rooms, and it is rather spacious."), ("특히 아파트 주변 환경이 아주 좋다.", "In particular, the environment around the apartment is very good."),
    ("아파트 단지에 공원이 있다.", "There is a park in the apartment complex."), ("그리고 가까운 곳에 산이 있어서 공기도 맑다.", "And there is a mountain nearby, so the air is clear, too."), ("지하철 역도 가깝고 주변에 편의시설도 많아서 아주 편리하다.", "The subway station is close, and there are many amenities around, so it is very convenient. (the underlined sentence)"),
]
_AD1 = [("월세", "Monthly rent (the book sets it between stars)"), ("주택 이 층 월세 놓습니다.", "A second floor of a house is for rent monthly."), ("주변에 나무가 많아 공기가 아주 좋고 전망도 좋습니다.", "There are many trees around, so the air is very good and the view is good, too."),
        ("방 두 개, 화장실 한 개, 이십이 평", "2 rooms, 1 bathroom, 22 pyeong"), ("버스 정류장과 가깝고, 구일 초등학교 바로 앞에 있습니다.", "It is close to a bus stop and right in front of Guil Elementary School."), ("보증금 칠천만 원, 월 팔십만 원", "Deposit 70,000,000 won, 800,000 won a month"), ("구로 부동산", "Guro Real Estate (the telephone number is left out)")]
_AD2 = [("전세 있음", "A 전세 is available"), ("삼십삼 평, 방 세 개, 화장실 두 개", "33 pyeong, 3 rooms, 2 bathrooms"), ("이 년 전에 지은 새 아파트", "A new apartment built two years ago"), ("팔 층, 전망 아주 좋음", "8th floor, a very good view"), ("서울 백화점 건너편에 위치", "Located across from the Seoul Department Store"),
        ("공원, 스포츠 센터 등 편의시설", "Amenities such as a park and a sports center"), ("전세 오억 사천", "전세: 540,000,000 (the book writes 5억 4천, without 만 원)"), ("목동 부동산", "Mokdong Real Estate (the telephone number is left out)")]
L5 = lesson(
    "Ch 21 · Topic B, Follow-up 1 and Activities B: real estate ads and a journal",
    "서울부동산 · 단독주택 · 아파트 · 원룸 · 월세 · 전세 · 보증금 · 상진의 일기",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): real estate ads",
             "The book gives an advertisement of 서울부동산 with three homes and asks you to fill in a table in English (type of housing, type of rent, rooms and baths, rental amount; the book gives three entries: month-to-month, 3 bed/2 bath, studio). The text was read from the page image (the figures are spelled out in Hangul; the address, the web address and the telephone number are left out). The English is mine. The book glosses 조용하다 as “to be quiet”.",
             examples=passage(_RE_AD)),
        card("The table filled in (mine)",
             "The book fills in three entries (“month-to-month”, “3 bed/2 bath” and “studio”); the rest is my answer.",
             tables=[table(["Type of housing", "Type of rent", "Rooms & baths", "Rental amount"], [["Single-family house", "month-to-month (the book’s)", "4 bed/2 bath", "Deposit 100,000,000 won; 5,000,000 won a month"], ["Apartment (105 m²)", "전세 (lump-sum deposit)", "3 bed/2 bath (the book’s)", "550,000,000 won"], ["Studio (12 pyeong)", "month-to-month", "A wide living room and a bathroom", "900,000 won a month (deposit 20,000,000 won)"]])]),
        card("Activity 1 (Reading): Sangjin’s journal",
             "The text is from Sangjin’s journal about moving into a new apartment. The book asks you to fill in a table in English (type of rent, rooms, surrounding environment) and to translate the underlined sentence into English. The text was read from the page image (the date is spelled out; the underlined sentence is the last one); the English is mine.",
             examples=passage(_JOURNAL)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Type of rent", "Rooms", "Surrounding environment"], [["Monthly rent (월세)", "Three rooms; rather spacious", "A park in the complex; a mountain nearby and clean air; the subway station is close; many amenities around"]])]),
        card("Activity 2 (Reading): two “for rent” ads",
             "The book gives two ads from the “For Rent” section of a daily newspaper and asks you to fill in a table in English (type of rent, size, rooms and baths, location, rental amount). The texts were read from the page image (the figures are spelled out; the telephone numbers and the picture credits are left out); the English is mine. Ad 1:",
             examples=passage(_AD1)),
        card("Ad 2",
             "The second ad (the English is mine):",
             examples=passage(_AD2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["", "Type of rent", "Size, rooms & baths", "Location", "Rental amount"], [["Ad 1", "Monthly rent", "22 pyeong; 2 rooms, 1 bath", "Second floor of a house; close to a bus stop and in front of Guil Elementary School; Guro", "Deposit 70,000,000 won; 800,000 won a month"], ["Ad 2", "전세", "33 pyeong; 3 rooms, 2 baths", "8th floor; across from the Seoul Department Store; Mokdong", "540,000,000 won (5억 4천)"]])]),
        card("Activities left out",
             "Follow-up 2 of Topic B (listening to phone conversations between a realtor and a customer) and Activity 3 (listening to dialogs between a prospective renter and a realtor) are audio activities; Activity 4 (the rental role-play with situation cards) is a partner activity."),
    ],
    exercises=uniq(
        _tr(_RE_AD + _JOURNAL + _AD1 + _AD2)
        + [M("Which home is rented with a large deposit and no monthly rent?", "The apartment in Sangam-dong", ["The house in Yeonhui-dong", "The studio near Ewha", "None of them"], "전세 오억 오천만 원."), M("How many rooms does the house in Yeonhui-dong have?", "Four", ["Three", "Two", "One"], "방 네 개, 욕실 두 개."),
           M("How far is the studio from the subway station?", "5 minutes", ["15 minutes", "1 hour", "Next to it"], "지하철 역에서 오 분 거리."), M("How much is the studio’s monthly rent?", "900,000 won", ["90,000 won", "9,000,000 won", "500,000 won"], "월세 구십만 원."),
           M("What kind of apartment is Sangjin’s?", "A three-room monthly-rent apartment", ["A 전세 apartment", "A studio", "A house"], "방이 세 개짜리 월세 아파트."), M("What is good about the surroundings of Sangjin’s apartment?", "A park, a mountain, a nearby subway station and many amenities", ["A beach", "A school only", "Nothing"], "공원, 산, 지하철 역, 편의시설."),
           M("Which ad is for a 월세?", "Ad 1", ["Ad 2", "Both", "Neither"], "Ad 1 is headed 월세."), M("Which floor is Ad 2’s apartment on?", "The 8th floor", ["The 2nd floor", "The 22nd floor", "The 33rd floor"], "팔 층."), M("How old is Ad 2’s apartment?", "Two years", ["Ten years", "A year", "Brand new"], "이 년 전에 지은 새 아파트."),
           M("How much is Ad 1’s deposit?", "70,000,000 won", ["7,000,000 won", "800,000 won", "700,000,000 won"], "보증금 칠천만 원."), M("Where is Ad 1’s home?", "Close to a bus stop and in front of an elementary school", ["Across from a department store", "Next to a park", "In an apartment complex"], "버스 정류장과 가깝고, 구일 초등학교 바로 앞."),
           F("보증금 칠천만 원, ___ 팔십만 원 (a month)", "월", ["일", "층"], "월 팔십만 원 = 800,000 won a month."), F("서울 백화점 ___에 위치 (across from)", "건너편", ["뒤쪽", "안쪽"], "건너편 = across."), F("지난 주말에 새집으로 ___를 했다. (the move)", "이사", ["정리", "계약"], "이사를 했다 = I moved."),
           read_q("서울부동산"), read_q("조용하고 밝은 집"), read_q("보증금 일억 원"), read_q("구로 부동산"), read_q("월세 놓습니다")]
    ),
)

# ================================================================== L6: Grammar A: -(으)려고 하다
def _ryo(verb):
    st = stem(verb)
    l, v, t = _K.decompose(st[-1])
    return st + ("려고 해요" if t in ("", "ㄹ") else "으려고 해요")


_RYO_V = [("가다", "to go"), ("팔다", "to sell"), ("찾다", "to look for"), ("먹다", "to eat"), ("사다", "to buy"), ("방문하다", "to visit"), ("이사하다", "to move"), ("읽다", "to read"), ("만들다", "to make"), ("구하다", "to look for"), ("계약하다", "to contract"), ("알리다", "to inform")]
_RYO_EX = [("한국에서 한국말을 공부하려고 해요.", "I intend to study Korean in Korea."), ("이번 주말에 고향에 가려고 해요.", "I plan to go to my hometown this weekend."), ("올해 집을 팔려고 해요.", "I plan to sell my house this year."), ("자바 카페에서 점심을 먹으려고 해요.", "I plan to eat lunch at the Java Cafe."), ("백화점에서 양복을 사려고 해요.", "I intend to buy a suit at a department store."),
           ("이번 주말에 친구를 방문하려고 해요.", "I intend to visit a friend this weekend. (the book’s model)"), ("저는 가족들과 라스베가스에 가려고 해요.", "I intend to go to Las Vegas with my family. (the book’s model)")]
_RYO_M = [("최 일병, 이번 여름에 뭐 할 거예요?", "PFC Choi, what are you going to do this summer? (A)"), ("저는 가족들과 라스베가스에 가려고 해요.", "I plan to go to Las Vegas with my family. (B)"), ("라스베가스에는 왜요?", "Why Las Vegas? (A)"), ("저희 가족들이 쇼핑을 좋아하는 편이에요. 그래서 가려고 해요.", "My family tends to like shopping. So I plan to go. (B)")]
L6 = lesson(
    "Ch 21 · Grammar A: “intend to” and “plan to” with -(으)려고 하다",
    "한국말을 공부하려고 해요 · 고향에 가려고 해요 · 집을 팔려고 해요 · 양복을 사려고 해요",
    requires=[],
    cards=[
        card("Expressing “intend to” or “plan to”",
             "In Chapter 13, you learned that the conjunctive endings -(으)려고 and -(으)려면 are used to express a purpose or intention, as in 한국말을 공부하려고 (in order to learn Korean) and 핸드폰을 빌리려면 (if you intend to rent a cell phone). However, when the conjunctive ending -(으)려고 is immediately followed by 하다, it functions as an auxiliary verb that can be interpreted as intend to or plan to.",
             examples=passage(_RYO_EX[:2])),
        card("The rule",
             "action verb stem + (으)려고 하다.",
             tables=[table(["Condition", "Rule", "Example"], [["When a verb stem ends in a vowel or ㄹ", "add 려고 하다", "가다 → 가려고 하다; 팔다 → 팔려고 하다"], ["When a verb stem ends in a consonant other than ㄹ", "add 으려고 하다", "찾다 → 찾으려고 하다; 먹다 → 먹으려고 하다"]])],
             examples=passage(_RYO_EX[2:5])),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-(으)려고 해요"], [[v, m, _ryo(v)] for v, m in _RYO_V], say=[0, 2])]),
        card("Follow-up 1 and 5: phrases and plans",
             "In Follow-up 1 partners read a verb phrase and the other conjugates it with -(으)려고 하다, adding adverbs if they like (the book’s model: 친구를 방문하다 → 이번 주말에 친구를 방문하려고 해요). In Follow-up 5 (이번 여름에 해수욕장에 가려고 해요) you think about summer plans for your family and exchange them with classmates using -(으)려고 하다 and -(으)ㄴ/는 편이다. The book’s model:",
             examples=passage(_RYO_M)),
        card("Activities left out",
             "Follow-up 1 (partner verb lists), Follow-up 2 (listening to four conversations and writing what the female speaker intends to do) and Follow-up 5 (writing and exchanging vacation plans) are partner, audio and class activities."),
    ],
    exercises=uniq(
        _fk(_RYO_V, _ryo, "-(으)려고 해요 (I plan to)", lambda v: [stem(v) + "려고 해요", stem(v) + "으려고 해요", stem(v) + "을까 해요", stem(v) + "고 싶어요"])
        + _tr(_RYO_EX + _RYO_M)
        + [F("한국에서 한국말을 공부하___ 해요. (intend to)", "려고", ["으려고", "는 것"], "공부하다 ends in a vowel: 려고."), F("올해 집을 팔___ 해요. (plan to sell)", "려고", ["으려고", "는 것"], "팔다 ends in ㄹ: 려고."), F("점심을 먹___ 해요. (plan to eat)", "으려고", ["려고", "는 것"], "먹다 ends in a consonant: 으려고."),
           F("이번 주말에 친구를 방문하___ 해요. (plan to visit)", "려고", ["으려고", "는 것"], "방문하다 + 려고."), F("백화점에서 양복을 사___ 해요. (intend to buy)", "려고", ["으려고", "는 것"], "사다 + 려고."), F("저는 가족들과 라스베가스에 가려고 ___. (I plan)", "해요", ["했어요", "하세요"], "-(으)려고 하다."),
           M("What does -(으)려고 하다 express?", "Intention or a plan", ["A past experience", "A near miss", "An uncertain thought"], "I intend to; I plan to."), M("What follows the stem of 팔다 (to sell)?", "려고 하다", ["으려고 하다", "을까 하다", "는 편이다"], "ㄹ-ending stems take 려고."), M("What follows the stem of 먹다?", "으려고 하다", ["려고 하다", "을까 하다", "는 편이다"], "Consonant stems take 으려고."),
           read_q("한국말을 공부하려고 해요"), read_q("집을 팔려고 해요"), read_q("점심을 먹으려고 해요"), read_q("양복을 사려고 해요"), read_q("친구를 방문하려고 해요")]
    ),
)

# ================================================================== L7: Grammar B: -(으)ㄴ/는 편이다
def _pyeon_s(verb):
    return attr(verb)[1] + " 편이에요"


def _pyeon_a(verb):
    return attr(verb)[0] + " 편이에요"


_PY_S = [("크다", "to be big"), ("예쁘다", "to be pretty"), ("넓다", "to be wide"), ("작다", "to be small"), ("길다", "to be long"), ("비싸다", "to be expensive"), ("많다", "to be many"), ("조용하다", "to be quiet"), ("낮다", "to be low"), ("밝다", "to be bright")]
_PY_A = [("잘하다", "to do well"), ("듣다", "to listen"), ("먹다", "to eat"), ("마시다", "to drink"), ("읽다", "to read"), ("자다", "to sleep"), ("보다", "to watch"), ("걷다", "to walk")]
_PY_EX = [("몬트레이가 작은 편입니다.", "Monterey is rather small."), ("저는 한국 음식을 자주 먹는 편입니다.", "I tend to eat Korean food often."), ("제 여자 친구는 머리가 긴 편이에요.", "My girlfriend has fairly long hair."), ("우리 교실은 작은 편입니다.", "Our classroom is rather small."),
          ("박 일병은 한국말을 잘하는 편이에요.", "PFC Park speaks Korean fairly well."), ("저는 음악을 자주 듣는 편이에요.", "I tend to listen to music a lot."), ("김 일병, 커피를 많이 마시는 편입니까?", "PFC Kim, do you tend to drink a lot of coffee? (the book’s model)"), ("아니요. 저는 커피를 잘 안 마시는 편입니다.", "No. I tend to not drink coffee much. (the book’s model)"),
          ("네, 커피를 많이 마시는 편입니다.", "Yes, I tend to drink a lot of coffee. (the book’s model)")]
_PY_PLAIN = [("몬트레이가 작아요.", "Monterey is small. (more assertive)"), ("저는 한국 음식을 자주 먹어요.", "I eat Korean food often. (more assertive)")]
_STUDIO = [
    ("원룸 월세!", "A studio for monthly rent!"), ("이 오피스텔은 지하철 역과 버스 정류장이 가깝습니다.", "This officetel is close to a subway station and a bus stop."), ("그래서 교통이 편리한 편입니다.", "So the transportation is rather convenient."), ("또 오피스텔 일 층에는 세탁소, 슈퍼마켓, 커피숍, 에이티엠 등 여러 편의 시설도 있습니다.", "Also, on the first floor of the officetel there are various amenities such as a laundry, a supermarket, a coffee shop and an ATM."),
    ("그리고 주변에 공원도 있고 나무도 많이 있습니다.", "And there are parks and many trees around."), ("그래서 공기가 좋은 편입니다.", "So the air is rather good."), ("저희 오피스텔은 원룸이지만 꽤 넓은 편입니다.", "Our officetel is a studio, but it is rather spacious."), ("또 창문이 커서 집 안이 밝은 편입니다.", "Also, the windows are big, so the inside of the home is rather bright."),
    ("이십오 층 건물의 십육 층입니다.", "It is the 16th floor of a 25-story building."), ("보증금은 오천만 원이고, 월세는 칠십만 원입니다.", "The deposit is 50,000,000 won, and the monthly rent is 700,000 won."), ("관심 있으시면 전화 주세요.", "If you are interested, please call. (the telephone number is left out)"),
]
L7 = lesson(
    "Ch 21 · Grammar B: the nonassertive statement with -(으)ㄴ/는 편이다",
    "작은 편입니다 · 자주 먹는 편입니다 · 머리가 긴 편이에요 · 잘하는 편이에요",
    requires=[],
    cards=[
        card("The usage of -(으)ㄴ/는 편이다",
             "The expression -(으)ㄴ/는 편이다, which is attached to the stem of a verb, literally means “to be on the side of” or “to be in the group of” because 편 means a side, group or direction. 몬트레이가 작은 편입니다 means Monterey is “on the smaller side”; 저는 한국 음식을 자주 먹는 편입니다 means I am “on the side of” eating Korean food often.\n\n"
             "This expression can be best understood in the context of two sides or two categories: right or wrong, big or small, good or bad, etc. The first sentence, for example, implies that there are two categories, bigger places and smaller places, and Monterey belongs to the latter. Likewise, the second sentence implies that there are two categories, those who eat Korean food often and those who don’t, and the speaker belongs in the former.",
             examples=passage(_PY_EX[:2])),
        card("Nonassertive, not conclusive",
             "Neither of the sentences is as assertive or conclusive as 몬트레이가 작아요 (Monterey is small) and 저는 한국 음식을 자주 먹어요 (I eat Korean food often). Therefore, this expression is mainly used to make a nonassertive or non-conclusive statement about some factual information. When the expression is attached to a stative verb, depending on the context, it can be translated as fairly, rather, kind of or somewhat. When it is used with an action verb, it can be translated as tend to or be inclined to.",
             examples=passage(_PY_PLAIN)),
        card("The rule",
             "verb stem + (으)ㄴ/는 편이다.",
             tables=[table(["Condition", "Rule", "Example"], [["When a stative verb stem ends in a vowel", "add ㄴ 편이다", "크다 → 큰 편이다; 예쁘다 → 예쁜 편이다"], ["When a stative verb stem ends in a consonant", "add 은 편이다", "넓다 → 넓은 편이다; 작다 → 작은 편이다"], ["With an action verb", "add 는 편이다", "잘하다 → 잘하는 편이다; 듣다 → 듣는 편이다"]])],
             examples=passage(_PY_EX[2:6])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (stems with ㄹ lose it before ㄴ and 는: 길다 → 긴, 살다 → 사는).",
             tables=[table(["Stative verb", "Meaning", "-(으)ㄴ 편이에요"], [[v, m, _pyeon_s(v)] for v, m in _PY_S], say=[0, 2]), table(["Action verb", "Meaning", "-는 편이에요"], [[v, m, _pyeon_a(v)] for v, m in _PY_A], say=[0, 2])]),
        card("Follow-up 3 and 4: questions and an ad",
             "In Follow-up 3 partners ask and answer questions with -(으)ㄴ/는 편이다 (the book’s model: 김 일병, 커피를 많이 마시는 편입니까? / 아니요. 저는 커피를 잘 안 마시는 편입니다. / 네, 커피를 많이 마시는 편입니다). In Follow-up 4 you read an ad for a studio apartment, circle all the verbal phrases that contain -(으)ㄴ/는 편이다 and translate them. The ad is the book’s (the figures are spelled out; the telephone number is left out; the book glosses 오피스텔 as “a type of apartment; from the words office + hotel” and 원룸 as “a studio apartment; one room”); the English is mine.",
             examples=passage(_PY_EX[6:]) + passage(_STUDIO)),
        card("The four phrases (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Phrase", "Translation (mine)"], [["교통이 편리한 편입니다", "the transportation is rather convenient"], ["공기가 좋은 편입니다", "the air is rather good"], ["꽤 넓은 편입니다", "it is rather spacious"], ["집 안이 밝은 편입니다", "the inside of the home is rather bright"]], say=[0])]),
        card("Activities left out",
             "Follow-up 3 (partner verb phrase strips) and Follow-up 5 (exchanging vacation plans) are partner and class activities."),
    ],
    exercises=uniq(
        _fk(_PY_S, lambda v: attr(v)[1] + " 편", "-(으)ㄴ 편 (rather)", lambda v: [stem(v) + " 편", attr(v)[0] + " 편", stem(v) + "은 편" if not has_final(stem(v)) else stem(v) + "ㄴ 편", attr(v)[2] + " 편"])
        + _fk(_PY_A, lambda v: attr(v)[0] + " 편", "-는 편 (tend to)", lambda v: [stem(v) + " 편", attr(v)[1] + " 편", stem(v) + "은 편", attr(v)[2] + " 편"])
        + _tr(_PY_EX + _PY_PLAIN + _STUDIO)
        + [F("몬트레이가 작___ 편입니다. (rather)", "은", ["ㄴ", "는"], "작다 ends in a consonant: 작은."), F("제 여자 친구는 머리가 긴 ___이에요. (rather)", "편", ["평", "층"], "긴 편이에요."), F("저는 음악을 자주 듣___ 편이에요. (tend to)", "는", ["은", "을"], "듣다 is an action verb: 듣는."),
           F("박 일병은 한국말을 잘하___ 편이에요. (tends to)", "는", ["은", "ㄴ"], "잘하다 is an action verb: 잘하는."), F("교통이 편리___ 편입니다. (rather convenient)", "한", ["하는", "할"], "편리하다 is a stative verb: 편리한."), F("집 안이 밝___ 편입니다. (rather bright)", "은", ["ㄴ", "는"], "밝다 ends in a consonant: 밝은."),
           M("What does 편 mean in -(으)ㄴ/는 편이다?", "a side; a group; a direction", ["a floor", "a time", "a place"], "“to be on the side of”."), M("How can -(으)ㄴ/는 편이다 be translated with a stative verb?", "fairly; rather; kind of; somewhat", ["tend to", "must", "almost"], "작은 편입니다 = rather small."), M("How can -(으)ㄴ/는 편이다 be translated with an action verb?", "tend to; be inclined to", ["fairly", "almost", "might"], "자주 먹는 편입니다 = tend to eat often."),
           M("How does 몬트레이가 작은 편입니다 differ from 몬트레이가 작아요?", "It is less assertive", ["It is more assertive", "It is about the past", "It is a question"], "A nonassertive statement."),
           read_q("작은 편입니다"), read_q("자주 먹는 편입니다"), read_q("머리가 긴 편이에요"), read_q("잘하는 편이에요"), read_q("교통이 편리한 편입니다")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("직원", "네, 대한 이삿짐센터입니다.", "Hello, this is Daehan Moving Center."),
    ("희정", "이사를 하려고 하는데, 비용을 좀 알고 싶어요.", "I am planning to move, and I would like to know the cost."),
    ("직원", "포장 이사를 하실 거예요? 일반 이사를 하실 거예요?", "Will you have a packed move? Will you have a regular move?"),
    ("희정", "저는 일반 이사를 할까 해요. 그런데, 포장 이사는 뭐가 좋아요?", "I am thinking of a regular move. But what is good about a packed move?"),
    ("직원", "포장 이사를 하시면 저희 직원들이 모든 이삿짐을 다 싸 드립니다. 또 이사한 후에는 짐을 풀어서 정리해 드립니다.", "If you have a packed move, our staff pack all of your moving items for you. Also, after the move, they unpack the things and arrange them for you."),
    ("희정", "그럼, 포장 이사는 비용이 얼마나 들어요?", "Then how much does a packed move cost?"),
    ("직원", "보통 팔십만 원에서 백이십만 원 정도 듭니다. 저희가 이삿짐을 보고 정확한 비용을 알려 드리겠습니다.", "Usually it costs about 800,000 to 1,200,000 won. We will look at your moving items and tell you the exact cost."),
    ("희정", "네, 알겠습니다.", "Yes, I understand."),
]
_C_BLOG = [
    ("이사 준비", "Preparation for moving"), ("먼저, 신문 광고나 인터넷에서 이삿짐 센터를 찾아서 연락하세요.", "First, find a moving company in a newspaper ad or on the internet and contact it."), ("그다음에, 이삿짐 센터 직원이 집을 방문하면 이삿짐을 보여 주세요.", "Then, when a staff member of the moving company visits your house, show your moving items."),
    ("그리고 이사 비용을 정하고 계약금을 지불하세요.", "And decide on the moving cost and pay the down payment."), ("은행과 우체국에 가서 주소도 변경하세요.", "Go to the bank and the post office and change your address, too."), ("또 도시가스와 전화국에 연락을 해서 이사 가는 집의 가스와 전화도 신청하세요.", "Also, contact the city gas company and the telephone company and apply for the gas and the telephone of the house you are moving to."),
]
_C_WORDS = ["광고", "도시가스", "~동", "모든", "벌써", "신청", "싸다", "알리다", "-(으)ㄹ까 하다", "(~을/를) 싫어하다", "(~이/가) 싫다", "이삿짐", "이삿짐 센터", "전화국", "정리", "정하다", "정확하다", "평일"]
_YI = [("이사", "moving; “house-moving” (the book’s example)"), ("이식", "transplantation; “moving and planting” (the book’s example)"), ("이민", "immigration; emigration (mine)"), ("이주", "migration; moving one’s residence (mine)"), ("이동", "movement; transfer (mine)"), ("이동 통신", "mobile communication (mine)")]
_SAT = [("어젯밤", "last night"), ("빗길", "a rainy road"), ("나뭇가지", "a tree branch")]
L8 = lesson(
    "Ch 21 · Topic C: I am considering moving next month",
    "다음 달에 이사를 할까 합니다 · 이삿짐 센터 · 포장 이사 · 일반 이사 · 이사 준비 · 이 (移)",
    requires=[],
    cards=[
        card("Topic C, Part I: I am considering moving next month (다음 달에 이사를 할까 합니다)",
             "Heejeong calls a moving company to make an appointment for her move. (The English is mine; the book gives none. The book writes 80만 원 and 120만 원; they are spelled out here. The book’s footnote says 이삿짐 comes from two words: 이사 (move) + 짐 (load).)",
             examples=dlg(_C_DLG)),
        card("Part II: Heejeong’s blog",
             "On her blog, Heejeong posted some tips, based on her own experiences, about how to prepare for moving. (The English is mine.)",
             examples=passage(_C_BLOG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Notes: moving companies and the inserted ㅅ",
             "1. Moving companies are called 이삿짐 센터, which literally means “moving load center”. Names for moving companies usually end with one of the following: … 이사 (moving), … 익스프레스 (express), … 통운 (transport), … 용달 이사 (small truck moving) or 트랜스 (transport).\n\n"
             "2. 이삿짐 is a compound noun derived from 이사 and 짐. As with 이삿짐, ㅅ is inserted in a compound noun when the following two conditions exist: a. At least one of the words is a native Korean word. b. The first word ends in a vowel and the second word begins with a stop sound. Examples: 어젯밤, 빗길 and 나뭇가지 (tree branch).",
             tables=[table(["Example", "Meaning"], [list(r) for r in _SAT], say=[0])]),
        card("Sino-Korean in use: 이 (移)",
             "This Sino-Korean syllable means move or transfer, as in 이사 (“house-moving”) and 이식 (transplantation; “moving and planting”). Note that the Chinese character is made up of 禾 (화) and 多 (다). 禾, depicting a rice plant (its ear, stem and roots), means rice. 多 means many or multiple, as you learned in the earlier part of this chapter. Thus the character 移 originated from the rice farming tradition of mass-transplanting rice seedlings from a rice seedbed to a rice field. The more seedlings you move or transfer in spring, the more harvest you get in fall. The book asks you to guess the meaning of 이민, 이주, 이동 and 이동 통신; the answers are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _YI], say=[0])]),
        card("Activities left out",
             "The SMART Board activities of the Presentation Activity (including completing the dialog) and Follow-up 1 (listening to two phone conversations to a moving company and filling in the type of move, the moving date and the rates) are computer or audio activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith(("-", "~", "("))]))
        + _tr(_strip(_C_DLG) + _C_BLOG + _YI + _SAT)
        + [M("What does Heejeong want to know?", "The cost of moving", ["The moving date", "The address", "The size of the truck"], "비용을 좀 알고 싶어요."), M("What kind of move is Heejeong considering?", "A regular move", ["A packed move", "A small truck move", "No move"], "저는 일반 이사를 할까 해요."),
           M("What do the staff do in a packed move?", "Pack everything, then unpack and arrange it after the move", ["Only carry the items", "Only drive the truck", "Only pack the items"], "모든 이삿짐을 다 싸 드립니다. 이사한 후에는 짐을 풀어서 정리해 드립니다."), M("How much does a packed move usually cost?", "800,000 to 1,200,000 won", ["80,000 to 120,000 won", "8,000,000 to 12,000,000 won", "Free"], "팔십만 원에서 백이십만 원."),
           M("When will the staff tell the exact cost?", "After they look at the moving items", ["Right now", "Next year", "After the move"], "이삿짐을 보고 정확한 비용을 알려 드리겠습니다."), M("What is the first tip on the blog?", "Find a moving company in an ad or on the internet and contact it", ["Pay the down payment", "Change your address", "Apply for gas"], "먼저, 신문 광고나 인터넷에서."),
           M("What should you do when the staff visit?", "Show the moving items", ["Pay the full cost", "Pack the items", "Go out"], "이삿짐을 보여 주세요."), M("Where do you go to change your address?", "The bank and the post office", ["The telephone company", "The gas company", "A hospital"], "은행과 우체국에 가서 주소도 변경하세요."), M("Whom do you contact to apply for gas and the telephone?", "The city gas company and the telephone company", ["The bank", "The post office", "The realtor"], "도시가스와 전화국."),
           M("What does 이 (移) mean?", "move; transfer", ["many", "medicine", "victory"], "이사, 이민, 이주, 이동."), M("What does 이삿짐 mean?", "moving items; “moving load”", ["a moving company", "a house", "a truck"], "이사 + 짐."),
           F("이삿짐 ___에 전화했습니다. (a moving company)", "센터", ["광고", "정리"], "이삿짐 센터 = a moving company."), F("먼저 신문 ___나 인터넷에서 이삿짐 센터를 찾으세요. (an ad)", "광고", ["신청", "정리"], "광고 = an advertisement."), F("직원들이 이삿짐을 다 ___ 드립니다. (pack)", "싸", ["풀", "정해"], "싸다 = to wrap; to pack."),
           F("이사 날짜를 ___ 계약금을 지불하세요. (decide on)", "정하고", ["신청하고", "알리고"], "정하다 = to decide."), F("저는 일반 이사를 하___ 해요. (am thinking of)", "ㄹ까", ["려고", "는 편"], "-(으)ㄹ까 하다 = to consider doing."), F("___한 비용을 알려 드리겠습니다. (exact)", "정확", ["특별", "편리"], "정확하다 = to be exact."),
           read_q("이삿짐 센터"), read_q("포장 이사"), read_q("일반 이사를 할까 해요"), read_q("계약금을 지불하세요"), read_q("주소도 변경하세요")]
    ),
)

# ================================================================== L9: Follow-up 2 and Activity 2: the steps of moving
_STEPS = [("이삿짐 센터에 연락해서 필요한 정보와 이사 비용에 대해서 물어 보세요.", "Contact a moving company and ask for the information you need and about the moving cost."), ("신문이나 인터넷에서 이삿짐 센터 광고를 찾으세요.", "Find the moving company ads in a newspaper or on the internet."), ("전화국과 도시가스에 전화해서 이사 갈 집의 전화와 가스를 신청하세요.", "Call the telephone company and the city gas company and apply for the phone and the gas of the house you are moving to."), ("이삿짐 센터가 마음에 들면 계약을 하고 계약금을 지불하세요.", "If you like a moving company, sign a contract and pay the down payment.")]
_TIPS = [("첫째, 신문 광고나 인터넷에서 이삿짐 센터를 찾아서 연락하세요.", "First, find a moving company in a newspaper ad or on the internet and contact it."), ("둘째, 이삿짐 센터 직원이 집을 방문하면 이사 비용을 정하세요.", "Second, when a staff member of the moving company visits your house, decide on the moving cost."), ("셋째, 이삿짐 센터 직원과 계약을 하고 계약금을 지불하세요.", "Third, sign a contract with the staff member of the moving company and pay the down payment."),
         ("넷째, 은행과 우체국에 가서 주소를 변경하세요.", "Fourth, go to the bank and the post office and change your address."), ("다섯째, 도시가스와 전화국에 연락을 해서 이사 들어갈 집의 가스와 전화를 신청하세요.", "Fifth, contact the city gas company and the telephone company and apply for the gas and the telephone of the house you are moving into.")]
_MODEL3 = [("포장 이사는 비용이 얼마나 듭니까?", "How much does a packed move cost? (the book’s title of Activity 3)")]
L9 = lesson(
    "Ch 21 · Topic C, Follow-up 2 and Activities C: the steps of moving",
    "이사 준비 · 첫째 · 둘째 · 셋째 · 넷째 · 다섯째 · 포장 이사는 비용이 얼마나 듭니까?",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): arrange the moving instructions in logical order",
             "The book gives four instructions about moving, in a mixed order, and asks you to number them. The sentences are the book’s (in the book’s mixed order); the English is mine.",
             examples=passage(_STEPS)),
        card("The logical order (mine)",
             "The book leaves the numbers blank; this is my order.",
             tables=[table(["Step", "Things to do"], [["1", "신문이나 인터넷에서 이삿짐 센터 광고를 찾으세요."], ["2", "이삿짐 센터에 연락해서 필요한 정보와 이사 비용에 대해서 물어 보세요."], ["3", "이삿짐 센터가 마음에 들면 계약을 하고 계약금을 지불하세요."], ["4", "전화국과 도시가스에 전화해서 이사 갈 집의 전화와 가스를 신청하세요."]], say=[1])]),
        card("Activity 2 (Reading): moving tips on a blog",
             "The book gives five moving tips with the ordinals 첫째 to 다섯째 and asks you to number five English sentences in the same order as their Korean counterparts. The Korean tips (the English is mine):",
             examples=passage(_TIPS)),
        card("The numbering (mine)",
             "The book’s English sentences are listed in a mixed order; these are my numbers for them (the book leaves them blank):",
             tables=[table(["The book’s English sentence", "Number (mine)"], [["Go to the bank and the post office for change-of-address forms.", "4"], ["Sign a contract with the company and pay the deposit.", "3"], ["Find a moving company on the internet or through a newspaper ad and contact the company.", "1"], ["Call the city gas and phone companies to request service for your new house.", "5"], ["Decide on your moving budget when a representative from the moving company visits your house.", "2"]])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity and listening to three conversations about one speaker’s experience with a moving company, checking full service or move only and listing the services and costs) is a computer and audio activity. Activity 3 (포장 이사는 비용이 얼마나 듭니까? A role-play with situation cards between a customer and a moving company employee) is a partner activity."),
    ],
    exercises=uniq(
        _tr(_STEPS + _TIPS)
        + [M("Which step comes first?", "Find the moving company ads", ["Pay the down payment", "Change your address", "Apply for gas"], "신문이나 인터넷에서 광고를 찾으세요."), M("Which step comes right after finding the ads?", "Contact a moving company and ask about the information and cost", ["Sign a contract", "Apply for gas", "Change your address"], "이삿짐 센터에 연락해서."),
           M("When do you sign a contract and pay the down payment?", "If you like a moving company", ["Before looking at ads", "After the move", "When you apply for gas"], "마음에 들면 계약을 하고 계약금을 지불하세요."), M("What is the fifth tip on the blog?", "Apply for the gas and the telephone of the new house", ["Change your address", "Sign a contract", "Decide the cost"], "다섯째."),
           M("Which tip is the fourth?", "Go to the bank and the post office and change your address", ["Sign a contract", "Decide the cost", "Find a moving company"], "넷째."), M("Which tip is the second?", "Decide on the moving cost when a staff member visits", ["Sign a contract", "Change your address", "Apply for gas"], "둘째."),
           M("What is ‘첫째’?", "First", ["Second", "Third", "Fifth"], "첫째 = first."), M("What is ‘셋째’?", "Third", ["Second", "Fourth", "Fifth"], "셋째 = third."), M("What is ‘다섯째’?", "Fifth", ["Fourth", "Third", "First"], "다섯째 = fifth."),
           F("___, 신문 광고나 인터넷에서 이삿짐 센터를 찾으세요. (first)", "첫째", ["둘째", "셋째"], "첫째 = first."), F("___, 이삿짐 센터 직원이 집을 방문하면 이사 비용을 정하세요. (second)", "둘째", ["첫째", "넷째"], "둘째 = second."), F("___, 은행과 우체국에 가서 주소를 변경하세요. (fourth)", "넷째", ["셋째", "다섯째"], "넷째 = fourth."),
           read_q("이사 준비"), read_q("첫째"), read_q("셋째"), read_q("다섯째"), read_q("주소를 변경하세요")]
    ),
)

# ================================================================== L10: Grammar C: -(으)ㄹ까 하다
def _ggah(verb):
    return attr(verb)[2] + "까 해요"


_GGA_V = [("이사하다", "to move"), ("사다", "to buy"), ("읽다", "to read"), ("먹다", "to eat"), ("가다", "to go"), ("보다", "to see; to watch"), ("만들다", "to make"), ("살다", "to live"), ("찾다", "to look for"), ("방문하다", "to visit")]
_GGA_EX = [("이번 주말에 등산을 하려고 합니다.", "I plan to go hiking this weekend."), ("이번 주말에 등산을 할까 합니다.", "I’m thinking of going hiking this weekend."), ("오늘 저녁에 영화를 볼까 합니다.", "I may see a movie tonight."), ("한국에 갈까 합니다.", "I am thinking about going to Korea."),
           ("다음 달에 아파트로 이사할까 해요.", "I might move to an apartment next month."), ("하와이에서 살까 합니다.", "I may live in Hawaii."), ("이베이에서 컴퓨터를 살까 해요.", "I am thinking about buying a computer on eBay."), ("저녁에 한국식당에서 먹을까 해요.", "I could eat at a Korean restaurant in the evening."),
           ("저는 등산을 좋아해서 요세미티에 갈까 해요.", "I like hiking, so I am thinking of going to Yosemite. (the book’s model)"), ("가서 등산도 하고 사진도 찍을까 해요.", "I might hike and take pictures when I get there. (the book’s model)")]
L10 = lesson(
    "Ch 21 · Grammar C: the speaker’s uncertainty with -(으)ㄹ까 하다",
    "등산을 할까 합니다 · 영화를 볼까 합니다 · 이사할까 해요 · 컴퓨터를 살까 해요",
    requires=[],
    cards=[
        card("Auxiliary verbs -(으)ㄹ까 하다",
             "Consider the following two sentences, both of which show the speaker’s intention of going hiking this weekend. -(으)려고 하다 in the first sentence implies the speaker has made up his mind about going hiking this weekend. However, -(으)ㄹ까 하다 in the second sentence implies the speaker has the intention of going hiking this weekend but has not made up his mind.\n\n"
             "As shown in the example, the auxiliary verb -(으)ㄹ까 하다 is used to imply a speaker’s uncertainty. For this reason, the auxiliary verb is often translated as may, might, could or (I’m) thinking about. Keep in mind that this auxiliary verb is not used in interrogatives.",
             examples=passage(_GGA_EX[:2])),
        card("The rule",
             "action verb stem + (으)ㄹ까 하다.",
             tables=[table(["Condition", "Rule", "Example"], [["When a verb stem ends in a vowel", "add ㄹ까 하다", "이사하다 → 이사할까 하다; 사다 → 살까 하다"], ["When a verb stem ends in a consonant", "add 을까 하다", "읽다 → 읽을까 하다; 먹다 → 먹을까 하다"]])],
             examples=passage(_GGA_EX[2:8])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (stems with ㄹ keep it: 살다 → 살까, 만들다 → 만들까).",
             tables=[table(["Verb", "Meaning", "-(으)ㄹ까 해요"], [[v, m, _ggah(v)] for v, m in _GGA_V], say=[0, 2])]),
        card("Follow-up 1 and 5: plans",
             "In Follow-up 1 partners read a verb phrase and the other conjugates it with -(으)ㄹ까 하다 (the book’s model: 친구를 방문하다 → 이번 주말에 친구를 방문할까 해요). In Follow-up 5 (저는 등산을 좋아해서 요세미티에 갈까 해요) you think about a destination and possible activities over the coming school break and exchange your plans with three classmates, using ~이/가 좋다, ~을/를 좋아하다 and -(으)ㄹ까 하다. The book’s model:",
             examples=passage([("김 일병, 이번 방학 때 뭐 할 거예요?", "PFC Kim, what are you going to do this school break? (A)")] + _GGA_EX[8:])),
        card("Activities left out",
             "Follow-up 1 (partner verb lists), Follow-up 2 (listening to four dialogs and checking whether the female speaker’s intention is certain or uncertain) and Follow-up 5 (exchanging vacation plans) are partner, audio and class activities."),
    ],
    exercises=uniq(
        _fk(_GGA_V, _ggah, "-(으)ㄹ까 해요 (I may)", lambda v: [stem(v) + "까 해요", stem(v) + "을까 해요", stem(v) + "려고 해요", stem(v) + "는까 해요"])
        + _tr(_GGA_EX)
        + [F("오늘 저녁에 영화를 보___ 합니다. (I may)", "ㄹ까", ["려고", "는 편"], "보다 ends in a vowel: 볼까."), F("저녁에 한국식당에서 먹___ 해요. (I could eat)", "을까", ["ㄹ까", "려고"], "먹다 ends in a consonant: 먹을까."), F("한국에 갈까 ___. (I am thinking about)", "합니다", ["했습니다", "하세요"], "-(으)ㄹ까 하다."),
           F("이번 주말에 등산을 ___ 합니다. (I plan to; I’ve made up my mind)", "하려고", ["할까", "하는 편"], "-(으)려고 하다 = a firm plan."), F("이번 주말에 등산을 ___ 합니다. (I’m thinking of; not yet decided)", "할까", ["하려고", "하는 편"], "-(으)ㄹ까 하다 = uncertain."), F("다음 달에 아파트로 이사___ 해요. (I might move)", "할까", ["하려고", "하는"], "이사하다 + ㄹ까 하다."),
           M("What does -(으)ㄹ까 하다 imply?", "The speaker’s uncertainty", ["A firm decision", "A past experience", "A near miss"], "I may…; I am thinking about…"), M("How does -(으)려고 하다 differ from -(으)ㄹ까 하다?", "-(으)려고 하다 implies the speaker has made up his mind", ["-(으)ㄹ까 하다 implies the speaker has made up his mind", "They mean the same", "-(으)려고 하다 is only for questions"], "려고 = decided; ㄹ까 = not decided."), M("Can -(으)ㄹ까 하다 be used in interrogatives?", "No", ["Yes", "Only with 요", "Only in the past"], "This auxiliary verb is not used in interrogatives."),
           read_q("등산을 할까 합니다"), read_q("영화를 볼까 합니다"), read_q("아파트로 이사할까 해요"), read_q("컴퓨터를 살까 해요"), read_q("한국식당에서 먹을까 해요")]
    ),
)

# ================================================================== L11: Grammar D: 좋다 vs 좋아하다, 싫다 vs 싫어하다
_LIKE_N = [("한국 음식", "Korean food"), ("김치", "kimchi"), ("한국 영화", "Korean movies"), ("등산", "hiking"), ("캘리포니아", "California"), ("일본 자동차", "Japanese cars"), ("애플 컴퓨터", "Apple computers"), ("몬트레이", "Monterey"), ("샌프란시스코", "San Francisco"), ("매운 음식", "spicy food")]
_LIKE_EX = [("나는 아이스크림을 좋아해요.", "I like ice cream."), ("나는 아이스크림이 좋아요.", "I like ice cream. (“For me, ice cream is good.”)"), ("나는 이 아이스크림을 싫어해요.", "I don’t like this ice cream."), ("나는 이 아이스크림이 싫어요.", "I don’t like this ice cream."), ("나는 한국 음식이 좋아요.", "I like Korean food."), ("나는 한국 음식을 좋아해요.", "I like Korean food."),
            ("우리는 매운 음식이 싫어요.", "We don’t like spicy food."), ("우리는 매운 음식을 싫어해요.", "We don’t like spicy food."), ("저는 멕시코 음식이 좋아요. 박 이병도 멕시코 음식을 좋아해요?", "I like Mexican food. Do you like Mexican food, too, Private Park? (the book’s model)"), ("아니요. 저는 멕시코 음식을 싫어해요.", "No. I don’t like Mexican food. (the book’s model)"), ("저도 멕시코 음식이 좋아요.", "I like Mexican food, too. (the book’s model)")]
_LIKE_NOTE = [("~이/가 밉다 / ~을/를 미워하다", "to hate a person"), ("~이/가 무섭다 / ~을/를 무서워하다", "to fear ~"), ("~이/가 그립다 / ~을/를 그리워하다", "to miss ~")]
L11 = lesson(
    "Ch 21 · Grammar D: likes and dislikes in two ways, 좋다 / 좋아하다 and 싫다 / 싫어하다",
    "아이스크림이 좋아요 · 아이스크림을 좋아해요 · 매운 음식이 싫어요 · 매운 음식을 싫어해요",
    requires=[],
    cards=[
        card("Expressing likes and dislikes in two different ways",
             "Consider the structural differences of 나는 아이스크림을 좋아해요 and 나는 아이스크림이 좋아요, both of which mean “I like ice cream”. In the first sentence, 좋아해요, whose dictionary form is 좋아하다 (to like), is an action verb that takes an object. Therefore the object 아이스크림 takes the object marker 을. In the second sentence, however, 좋아요, whose dictionary form is 좋다 (to be good; to be pleasant), is a stative verb. Thus 아이스크림 takes the subject marker 이, and the literal translation of the sentence is “For me, ice cream is good”. These two sentences are perfectly interchangeable.\n\n"
             "The same pattern is found in ~을/를 싫어하다 and ~이/가 싫다, both of which are used to mean “I do not like ~”.",
             examples=passage(_LIKE_EX[:4])),
        card("The rule",
             "~을/를 좋아하다 or ~이/가 좋다; ~을/를 싫어하다 or ~이/가 싫다.",
             tables=[table(["Meaning", "Action verb with an object", "Stative verb with a subject"], [["to like", "~을/를 좋아하다", "~이/가 좋다"], ["to dislike", "~을/를 싫어하다", "~이/가 싫다"]])],
             examples=passage(_LIKE_EX[4:8])),
        card("Forms (mine)",
             "The markers are made by the book’s rule.",
             tables=[table(["Noun", "Meaning", "~이/가 좋아요", "~을/를 좋아해요", "~이/가 싫어요", "~을/를 싫어해요"], [[n, m, _sub(n) + " 좋아요", _obj(n) + " 좋아해요", _sub(n) + " 싫어요", _obj(n) + " 싫어해요"] for n, m in _LIKE_N[:8]], say=[0, 2, 3, 4, 5])]),
        card("Notes: verbs with the same pattern",
             "The following sets of verbs follow the same pattern with ~을/를 좋아하다 and ~이/가 좋다. These verb sets will be covered in detail in a later chapter.",
             tables=[table(["Pattern", "Meaning"], [list(r) for r in _LIKE_NOTE], say=[])]),
        card("Follow-up 4: likes and dislikes",
             "Partner A chooses a word from List A (요리하는 것, 몬트레이, 일본 자동차, 애플 컴퓨터, 쇼핑하는 것, 캘리포니아) and expresses a like or dislike, and asks if Partner B likes the same thing; Partner B uses List B (김치, 숙제하는 것, 한국 영화, 샌프란시스코, 술 마시는 것, 등산). The book’s model:",
             examples=passage(_LIKE_EX[8:])),
        card("Activities left out",
             "Follow-up 3 (listening to four dialogs and checking whether ~이/가 or ~을/를 is used) is an audio activity; Follow-up 4 (partner lists) and Follow-up 5 (exchanging vacation plans) are partner and class activities."),
    ],
    exercises=uniq(
        [M(f"Which is “I like {m}” with 좋다?", "저는 " + _sub(n) + " 좋아요.", ["저는 " + _obj(n) + " 좋아요.", "저는 " + _sub(n) + " 좋아해요.", "저는 " + n + "에 좋아요."], f"좋다 takes the subject marker: {_sub(n)} 좋아요.") for n, m in _LIKE_N[:6]]
        + [M(f"Which is “I like {m}” with 좋아하다?", "저는 " + _obj(n) + " 좋아해요.", ["저는 " + _sub(n) + " 좋아해요.", "저는 " + _obj(n) + " 좋아요.", "저는 " + _sub(n) + " 좋아하요."], f"좋아하다 takes the object marker: {_obj(n)} 좋아해요.") for n, m in _LIKE_N[:6]]
        + [M(f"Which is “I don’t like {m}” with 싫다?", "저는 " + _sub(n) + " 싫어요.", ["저는 " + _obj(n) + " 싫어요.", "저는 " + _sub(n) + " 싫어해요.", "저는 " + _obj(n) + " 싫어하요."], f"싫다 takes the subject marker: {_sub(n)} 싫어요.") for n, m in _LIKE_N[:4]]
        + _tr(_LIKE_EX)
        + [F("나는 아이스크림___ 좋아요. (subject marker)", "이", ["을", "를"], "아이스크림 ends in a consonant (ㅁ), so the subject marker is 이: 아이스크림이 좋아요."), F("나는 아이스크림___ 좋아해요. (object marker)", "을", ["이", "가"], "아이스크림을 좋아해요."), F("우리는 매운 음식___ 싫어요. (subject marker)", "이", ["을", "를"], "음식이 싫어요."),
           F("우리는 매운 음식을 싫어___. (dislike; action verb)", "해요", ["요", "어요"], "싫어하다 → 싫어해요."), F("저도 멕시코 음식이 ___. (I like)", "좋아요", ["좋아해요", "좋아하요"], "음식이 좋아요."), F("저는 매일 아침에 면도하는 것을 ___. (dislike; action verb)", "싫어해요", ["싫어요", "싫다"], "것을 싫어해요."),
           M("Why does 좋다 take the subject marker 이/가?", "It is a stative verb", ["It is an action verb", "It is a noun", "It is a particle"], "“For me, ice cream is good.”"), M("Why does 좋아하다 take the object marker 을/를?", "It is an action verb that takes an object", ["It is a stative verb", "It is a noun", "It is a particle"], "좋아하다 = to like."), M("Are 아이스크림을 좋아해요 and 아이스크림이 좋아요 interchangeable?", "Yes, perfectly", ["No, they differ completely", "Only in questions", "Only in the past"], "Both mean “I like ice cream”."),
           read_q("아이스크림을 좋아해요"), read_q("아이스크림이 좋아요"), read_q("매운 음식이 싫어요"), read_q("매운 음식을 싫어해요"), read_q("멕시코 음식을 좋아해요")]
    ),
)

# ================================================================== L12: Core vocabulary and self-evaluation
_CV_SECS = [("Real estate", _CV_RE), ("Housing", _CV_HOUSE), ("Moving", _CV_MOVE), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not r[0].startswith(("~", "-", "(")) and "/" not in r[0] and r[0] != "새~"]
L12 = lesson(
    "Ch 21 · Core vocabulary and self-evaluation",
    "주요 단어 · 부동산 · 주택 · 이사 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (1305동 → 천삼백오 동, 45평 → 사십오 평, LPG가스 → 엘피지 가스, 10% → 십 퍼센트, 5% → 오 퍼센트). The book’s 베란다/발코니 is shown as 베란다 / 발코니. The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: talk about two major types of housing, single-family homes and apartments; describe in a simple paragraph rooms and other components of a house or apartment; ask for basic information about renting a house; ask for basic information about moving, including moving services and types of moves; and give simple instructions about how to prepare for moving.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; -(으)려고 하다; -(으)ㄴ/는 편이다; -(으)ㄹ까 하다; 좋다 vs. 좋아하다; 싫다 vs. 싫어하다; and the Sino-Korean syllables 다 (多), 동 (動) and 이 (移)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does -(으)려고 하다 mean?", "to intend to; to plan to", ["to consider doing; might", "to be “on the side of”", "to be able to"], "내년에 집을 사려고 합니다."), M("What does -(으)ㄹ까 하다 mean?", "to consider doing; might; could; may", ["to intend to; to plan to", "to be “on the side of”", "to finish doing"], "이번 주말에 동생하고 영화를 볼까 해."),
           M("What does -(으)ㄴ/는 편이다 mean?", "to be “on the side of”", ["to intend to", "to consider doing", "to be able to"], "요즘 학생들은 아침 식사를 안 하는 편입니다."), M("What is “a security deposit”?", "보증금", ["계약금", "월세", "전세"], "보증금 = a security deposit."), M("What is “a deposit; down payment”?", "계약금", ["보증금", "월세", "전세"], "계약금 = a deposit; down payment."),
           M("What is “a single-family home”?", "단독주택", ["아파트", "다용도실", "단지"], "단독주택 = a single-family home."), M("What is “a moving company”?", "이삿짐 센터", ["이삿짐", "이사", "부동산"], "이삿짐 센터 = a moving company."), M("What is “a view; prospect”?", "전망", ["환경", "지역", "정원"], "전망 = a view; prospect."), M("What is “weekdays”?", "평일", ["주말", "특히", "벌써"], "평일 = weekdays."),
           M("What is “already”?", "벌써", ["아직", "특히", "나중에"], "벌써 = already.")]
        + [read_q("주요 단어"), read_q("집 구하기와 이사하기"), read_q("공인중개사"), read_q("이삿짐 센터"), read_q("편의시설")]
    ),
)

UNIT = unit("Semester 1 · Unit 6 · Chapter 21: House Hunting and Moving (집 구하기와 이사하기)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
