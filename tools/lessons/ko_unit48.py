"""Unit 48: KBC Semester 2, Unit 11, Chapter 41 - Korean Culture I (한국의 문화 1).
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

# ---- the core vocabulary of Chapter 41 (meanings and examples are the book's; digits respelled)
_CV_A = [
    ("계층", "(階層) (social) class", "옛날에는 계층이 다른 사람과 결혼할 수 없었어요."),
    ("기본(적)(으로)", "(基本(的)) a basis (basic) (basically)", "택시 기본 요금이 얼마입니까?"),
    ("기혼", "(旣婚) married; “already married”", "요즘은 직업을 가진 기혼 여성이 많습니다."),
    ("내의/속옷", "(內衣) underwear; underclothes; “inside clothes”", "부모님께 드릴 선물로 내의를 샀어요. 내일 백화점에서 속옷 패션쇼를 합니다."),
    ("동양", "(東洋) the East; “east ocean”", "동양과 서양의 문화는 조금 달라요."),
    ("따르다", "to follow; to comply with", "저는 유행을 따르지 않고 제가 좋아하는 옷을 입어요."),
    ("맞추다", "to have (an object) custom-made; to match; to assemble", "예전에는 양복점에서 양복을 맞췄어요. 색깔을 잘 맞춰 입으면 보기 좋아요. 퍼즐을 잘 맞춰 보세요."),
    ("~ 벌", "counter for clothes", "남자 양복 정장 한 벌에 얼마입니까?"),
    ("분홍색", "(粉紅色) pink (color)", "어머니 선물로 분홍색 스웨터를 샀어요."),
    ("새로", "newly", "새로 산 가방이 마음에 들어요?"),
    ("서양", "(西洋) the West; “west ocean”", "서양에서는 젓가락을 쓰지 않지요?"),
    ("스타일", "a style", "새 머리 스타일이 마음에 듭니다."),
    ("연하다", "(軟) to be light; to be soft; to be pale", "제 자동차는 연한 회색입니다."),
    ("영향", "(影響) an influence; an effect; an impact", "역사적으로 한국의 문화가 일본 문화에 많은 영향을 주었습니다."),
    ("장식", "(裝飾) an ornament; a decoration (to decorate) (~하다)", "이 방에서 생일 파티를 하려고 해요. 어떻게 장식할까요?"),
    ("저고리", "an upper garment of traditional Korean clothes", "보통 여자 저고리는 짧고 남자 저고리는 길어요."),
    ("캐주얼", "casual clothes (to be casual [in attire]) (~하다)", "내일은 금요일이니까 회사에 캐주얼을 입고 가야겠어요."),
    ("편안하다", "(便安) to be comfortable; to be peaceful", "바다를 보니까 마음이 편안합니다."),
    ("평상시", "(平常時) (at) ordinary times; (at) usual times", "평상시 부모님과 자주 연락합니까?"),
    ("화려하다", "(華麗) to be colorful; to be fancy; to be splendid", "아버지는 화려한 색깔의 넥타이를 좋아하십니다."),
    ("희다/하얗다", "to be white", "저는 흰색 옷을 자주 입어요. 저는 하얀 고양이가 두 마리 있습니다."),
]
_CV_B = [
    ("고춧가루", "red pepper powder", "대부분의 김치에 고춧가루가 들어갑니다."),
    ("굽다", "to bake; to roast; to grill", "김 일병은 손님을 대접하기 위해 고기를 굽습니다."),
    ("김장", "making kimchi for the winter (to make kimchi for the winter) (~하다)", "한국에서는 보통 십일월에 김장을 합니다."),
    ("끓다/끓이다", "(liquid) to (be) boil(ing) / to (bring a liquid to a) boil", "차를 마시기 위해 물을 끓이고 있습니다."),
    ("담그다", "to make (kimchi); to pickle (vegetables, fish); “to soak”", "김치를 담그는 것이 쉽지 않습니다."),
    ("대접", "(待接) treatment; reception (to treat/to be treated) (~하다/받다)", "설날에 손님을 초대해서 대접하려고 합니다."),
    ("뒤집다", "to turn over; to flip over; to turn upside down", "스테이크를 요리할 때 자주 뒤집으면 안돼요."),
    ("마늘", "garlic", "요즘은 미국사람들도 요리할 때 마늘을 많이 사용해요."),
    ("모습", "(貌襲) an image, look, appearance (of a thing, sight, person)", "한복을 입은 모습이 아주 예뻐요."),
    ("문화", "(文化) culture", "외국어를 배울 때 그 나라의 문화를 알면 더 쉽습니다."),
    ("미역국", "seaweed soup", "아들 생일이어서 아침에 미역국을 끓였습니다."),
    ("배추", "napa cabbage; Chinese cabbage", "김장을 하려고 배추를 많이 샀습니다."),
    ("볶다", "to pan fry; to stir fry", "잡채를 만들 때 여러 가지 야채를 잘 볶으세요."),
    ("붓다", "to pour", "물 여덟 컵 정도를 냄비에 부으세요."),
    ("살짝", "slightly; lightly", "시금치는 살짝 삶으세요."),
    ("삶다", "to boil (food); to simmer", "샐러드를 만들려고 계란을 삶아요."),
    ("섞다/섞이다", "to mix; to blend / to be mixed; to be blended", "여러 가지 재료를 큰 그릇에 넣고 잘 섞으세요. 재료가 잘 섞이지 않으면 음식 맛이 없어요."),
    ("썰다", "to cut; to chop; to slice", "먼저 당근과 양파를 써세요."),
    ("이웃", "a neighbor; the neighborhood", "저희 가족은 이웃하고 아주 친해요."),
    ("익다/익히다", "to be ripe; to mature; to age; to be done/to mature (food); to age (food); to cook", "고기가 푹 익을 때까지 기다리세요. 돼지고기는 잘 익혀서 먹어야 합니다."),
    ("재료", "(材料) an ingredient; material", "김밥을 만들 때 필요한 재료가 뭐예요?"),
    ("절다/절이다", "to be salted; to be seasoned; to be soaked / to preserve; to salt; to pickle", "김치를 담글 때 먼저 배추를 소금에 절여야 합니다."),
    ("젓다", "to stir; to whip; to beat", "커피에 설탕과 크림을 넣고 잘 저으세요."),
    ("찌다", "to steam", "만두는 쪄서 먹으면 더 맛있습니다."),
    ("튀기다", "to deep fry", "튀긴 음식은 맛있지만 건강에 나빠요."),
    ("푹", "thoroughly; entirely", "야채는 너무 푹 삶으면 안 돼요."),
]
_CV_C = [
    ("가옥", "(家屋) a house; “family house”", "한국의 전통가옥은 아주 아름답습니다."),
    ("공예(품)", "(工藝(品)) craft(work)", "저는 나무로 만든 공예품을 좋아합니다."),
    ("~구", "(區) gu (administrative district of a large city)", "한옥마을은 종로구에 있습니다."),
    ("그릇", "a bowl; a container; a dish; a plate", "손님이 많이 올 거니까 그릇이 더 필요해요."),
    ("그림", "a picture; a drawing; a painting", "저는 주말에 그림 전시회에 갈 겁니다."),
    ("기와", "roof tiles used for a traditional Korean house", "한옥의 지붕은 기와입니다."),
    ("(녹)차", "((綠)茶) (green) tea", "커피보다는 건강에 좋은 녹차를 드세요."),
    ("대문", "(大門) a front gate; a main gate; a main entrance; “big door”", "우리 집 대문은 파란색입니다."),
    ("~동", "(洞) dong (administrative division of a city)", "청담동에는 고급 음식점과 옷 가게가 많아요."),
    ("둘러보다", "to look around; to browse around", "주말에 시간이 나면 백화점을 둘러보려고 합니다."),
    ("매우", "very; extremely; greatly", "한국의 여름은 매우 덥습니다."),
    ("목이 마르다", "to be thirsty", "오래 뛰었더니 목이 말라요. 물을 좀 마셔야겠어요."),
    ("베개", "a pillow", "베개가 불편해서 잠을 잘 못 잤어요."),
    ("세면도구", "(洗面道具) toiletries; “face-washing tool”", "여행 짐을 쌀 때 세면도구를 제일 먼저 넣습니다."),
    ("숙소", "(宿所) lodging; accommodations; a place to stay", "우리 숙소는 경주 시내에 있는 호텔입니다."),
    ("신기하다", "(新奇) to be amazing; to be awesome", "동물원에 가서 신기한 동물을 봤어요."),
    ("약도", "(略圖) a rough map; “rough diagram”", "약도를 보면 쉽게 그 건물을 찾을 수 있어요."),
    ("~ 여", "(餘) over; slightly more than", "이번 축제에 이백여 명이 참가했습니다."),
    ("위치", "(位置) a position; a location; a site (to be located; to be situated) (~하다)", "그 극장 위치 좀 알려 주세요."),
    ("이불", "blanket (i.e. comforter, bedding)", "이불이 너무 무거워요. 가벼운 이불을 사야겠어요."),
    ("종이", "paper", "종이에 이름과 주소를 쓰세요."),
    ("~ 채", "counter for a building", "이 동네에는 한옥이 오십 채 정도 됩니다."),
    ("한옥", "(韓屋) a hanok; a traditional Korean-style house", "저는 한옥을 직접 본 적이 없습니다."),
]
_CV_GR = [
    ("~와/과/하고 달리", "unlike", "한국과 달리 미국은 대중교통 요금이 비쌉니다."),
    ("~을/를 포함해(서)", "including", "아버지를 포함해서 우리 가족 모두가 피아노를 연주합니다."),
    ("이/히/리", "transitive verbs with causative infixes", "요리하기 전에 쇠고기를 먼저 녹이세요."),
    ("~ 중에서/가운데서/에서", "among; of", "최근에 나온 영화 중에서 뭐가 제일 재미있어요?"),
]
_CV_SINO = [("서양", "(西洋) the West; Europe", "서부, 서독, 서해, 동양, 양복, 양식"), ("음식", "(飮食) food", "음료수, 음주, 과음, 소식, 식품, 식당"), ("한옥", "(韓屋) hanok; a traditional Korean-style house", "한반도, 한식, 한복, 가옥, 양옥, 옥상")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C}
_EXTRA = {"내의": "underwear; underclothes; “inside clothes”", "~ 벌": "counter for clothes", "~ 여": "over; slightly more than", "~ 채": "counter for a building", "~구": "gu", "~동": "dong", "~ 중에서/가운데서/에서": "among; of"}
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
_W1 = [("동서양", "East and West; the Orient and the Occident"), ("서양화가", "a Western-style painter"), ("양배추", "cabbage; “Western cabbage”"), ("양복점", "a tailor shop; a store selling suits"), ("서양화", "Western painting; Westernization (서양화하다: to Westernize)"), ("오대양", "the five oceans")]
_W1B = [("서부", "western part; the west"), ("서해", "the West Sea; a western sea"), ("서풍", "a west wind"), ("대양", "the ocean; “big ocean”"), ("태평양", "the Pacific Ocean"), ("대서양", "the Atlantic Ocean; “big western ocean”"), ("인도양", "the Indian Ocean"), ("양식", "Western food"), ("양복", "a suit; Western clothes"), ("양화점", "a shoe store; “Western shoes”"), ("양옥", "a Western-style house"), ("양담배", "a foreign cigarette; “Western cigarette”")]
_W2 = [("음료수", "a beverage; a drink"), ("음주운전", "drunk driving; “drinking liquor and driving”"), ("음식점", "a restaurant; “food store”"), ("과식", "overeating"), ("과음", "drinking too much"), ("식품점", "a grocery store; “food store”")]
_W2B = [("음주", "drinking; “drinking liquor”"), ("음용수", "drinking water; “water for drinking use”"), ("식당", "a restaurant"), ("한식", "Korean food; Korean dish")]
_W3 = [("양옥", "a Western-style house"), ("영한사전", "an English-Korean dictionary"), ("한국화", "Korean painting"), ("옥외 주차장", "an outdoor parking lot"), ("한반도", "the Korean Peninsula"), ("옥내 주차장", "an indoor parking lot")]
_W3B = [("한국", "Korea"), ("북한", "North Korea"), ("옥상", "the rooftop; the housetop"), ("옥외", "outside the house; the outdoors; the open (air)"), ("한식", "Korean food"), ("한복", "traditional Korean clothes")]

# ================================================================== L1
L1 = lesson(
    "Ch 41 · What the chapter teaches, 서양 · 음식 · 한옥",
    "한국의 문화 · 서양 · 음식 · 한옥 · 동양 · 식당 · 양옥",
    requires=[],
    cards=[
        card("What Chapter 41 teaches (한국의 문화 1)",
             "Chapter 41, “Korean Culture I”, has a vocabulary builder, three topic presentations (clothing, kimchi making, hanok houses) with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and extract information about traditional and modern clothing in Korea, and describe a person’s outfit; discuss food-related culture in Korea, including making kimchi; talk about basic cooking methods; and identify traditional and modern Korean houses, and compare them.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; ~을/를 포함해(서) (including); ~와/과 달리 or ~하고 달리 (unlike); transitive verbs with a causative infix; ~ 중에서/가운데서 (among) and ~에서 (at; on; in) in the superlative form; and the Sino-Korean syllables within 서양 (西洋), 음식 (飮食), and 한옥 (韓屋)."),
        card("Sino-Korean in use: 서양 (西洋)",
             "This Sino-Korean word means the West, Western (world/society), or Occident, as in 서양 문학 (Western literature) and 서양 음악 (Western music). Thus its counterpart is 동양 (the East, Eastern [world/society], or Orient), as in 동양 문학 (Eastern literature) and 동양 음악 (Eastern music). The first syllable 서 (西) means west or western, as in 서부 (western part; the west), 서해 (the West sea; a western sea), and 서풍 (a west wind). The second syllable 양 (洋) means ocean, as in 대양 (the ocean; “big ocean”), 태평양 (the Pacific Ocean), 대서양 (the Atlantic Ocean; “big western ocean”), and 인도양 (the Indian Ocean). Thus the literal meaning of the word 서양 is “west ocean” or “western ocean,” and the word refers to the West or Europe because the West is located west of Korea (or China) across the ocean. Note that the syllable 양 of the word 서양 can mean Western or foreign when it is used as a prefix, as in 양식 (Western food), 양복 (a suit; a dress; Western clothes), 양화점 (a shoe store; “Western shoes”), 양옥 (a Western-style house), and 양담배 (a foreign cigarette; American tobacco; “Western cigarette”). The book asks you to guess the meaning of 동서양, 서양화가, 양배추, 양복점, 서양화(하다) and 오대양 (my answers):",
             tables=[ktable(_W1B), ktable(_W1)]),
        card("Sino-Korean in use: 음식 (飮食)",
             "This Sino-Korean word means food (and drink) or a meal. The first syllable 음 (飮) means drinking, as in 음주 (drinking; “drinking liquor”) and 음용수 (drinking water; “water for drinking use”). The second syllable 식 (食) means food or eating, as in 식당 (a restaurant) and 한식 (Korean food; Korean dish). Thus the literal meaning of the word 음식 is “drinking and eating,” and the word refers to food (and drink), eatables (and drinkables), or a meal. The book asks you to guess the meaning of 음료수, 음주운전, 음식점, 과식, 과음 and 식품점 (my answers):",
             tables=[ktable(_W2B), ktable(_W2)]),
        card("Sino-Korean in use: 한옥 (韓屋)",
             "This Sino-Korean word means a traditional Korean-style house. As in words like 한국 and 북한, the first syllable 한 (韓) means Korea(n). The second syllable 옥 (屋) means house or house roof, as in 양옥 (a Western-style house; “Western house”), 옥상 (the rooftop; the housetop), and 옥외 (outside the house; the outdoors; the open [air]). Thus the literal meaning of the word 한옥 is “Korean house.” The book asks you to guess the meaning of 양옥, 한국화, 한반도, 영한사전, 옥외 주차장 and 옥내 주차장 (my answers):",
             tables=[ktable(_W3B), ktable(_W3)]),
    ],
    exercises=uniq(
        _tr(_W1 + _W1B + _W2 + _W2B + _W3 + _W3B, k=3)
        + [M("What does 서 (西) mean?", "west; western", ["east", "ocean", "house"], "서부."), M("What does 양 (洋) mean?", "ocean (as a prefix: Western; foreign)", ["house", "food", "drinking"], "대양, 양복."), M("What does 음 (飮) mean?", "drinking", ["eating", "house", "west"], "음주."), M("What does 식 (食) mean?", "food; eating", ["drinking", "house", "Korea"], "식당."), M("What does 한 (韓) mean?", "Korea; Korean", ["west", "house", "food"], "한국."), M("What does 옥 (屋) mean?", "house; house roof", ["ocean", "food", "Korea"], "옥상."), M("What is the literal meaning of 서양?", "“west ocean” or “western ocean”", ["“drinking and eating”", "“Korean house”", "“big door”"], "서 + 양."), M("What is the literal meaning of 음식?", "“drinking and eating”", ["“west ocean”", "“Korean house”", "“big ocean”"], "음 + 식."), M("What is the literal meaning of 한옥?", "“Korean house”", ["“west ocean”", "“drinking and eating”", "“Western house”"], "한 + 옥."), M("What is the counterpart of 서양?", "동양 (the East)", ["대양", "양옥", "한식"], "동양 and 서양."),
           F("한국에서는 쌀로 만든 ___식을 많이 먹는다. (Korean food)", "한", ["양", "서"], "한식."), F("이 가게는 ___복점이라서 양복을 맞출 수 있다. (Western clothes)", "양", ["한", "음"], "양복점."), F("___주운전은 위험합니다. (drinking)", "음", ["식", "양"], "음주운전."), F("___옥에는 기와지붕이 있습니다. (Korean)", "한", ["양", "서"], "한옥."), F("아침에 ___식당에서 밥을 먹었어요. (restaurant)", "식", ["음", "양"], "식당."),
           read_q("서양"), read_q("동양"), read_q("음식"), read_q("한옥"), read_q("양복점")]
    ),
)

# ================================================================== L2 Vocabulary builder
_VB = [("맞추다", "to have (an object) custom-made; to match; to assemble", "Clothing and fitting"), ("볶다", "to pan fry; to stir fry", "Cooking"), ("베개", "a pillow", "Bedding"), ("삶다", "to boil (food); to simmer", "Cooking"), ("장롱", "a wardrobe; a clothes chest (my gloss)", "Bedding and furniture"), ("이불", "blanket (i.e. comforter, bedding)", "Bedding"), ("캐주얼", "casual clothes", "Clothing and fitting"), ("튀기다", "to deep fry", "Cooking"), ("한옥", "a hanok; a traditional Korean-style house", "House"), ("편안하다", "to be comfortable; to be peaceful", "Describing"), ("끓이다", "to bring a liquid to a boil", "Cooking"), ("화려하다", "to be colorful; to be fancy; to be splendid", "Describing"), ("굽다", "to bake; to roast; to grill", "Cooking"), ("대문", "a front gate; a main gate", "House"), ("저고리", "an upper garment of traditional Korean clothes", "Clothing and fitting"), ("내의", "underwear; underclothes; “inside clothes”", "Clothing and fitting")]
_VBG = [("Cooking", ["볶다", "삶다", "튀기다", "끓이다", "굽다"]), ("Clothing", ["맞추다", "캐주얼", "저고리", "내의"]), ("House and bedding", ["베개", "장롱", "이불", "한옥", "대문"]), ("Describing", ["편안하다", "화려하다"])]
L2 = lesson(
    "Ch 41 · Vocabulary Builder: sorting sixteen words",
    "맞추다 · 볶다 · 베개 · 삶다 · 장롱 · 이불 · 캐주얼 · 튀기다 · 한옥 · 편안하다 · 끓이다 · 화려하다 · 굽다 · 대문 · 저고리 · 내의",
    requires=[],
    cards=[
        card("새 단어: sixteen words to group",
             "The book gives sixteen words from the chapter (맞추다, 볶다, 베개, 삶다, 장롱, 이불, 캐주얼, 튀기다, 한옥, 편안하다, 끓이다, 화려하다, 굽다, 대문, 저고리, 내의) and asks you to look for patterns, create a table dividing the words into groups, label each group in English, and copy the Korean words with their English meaning (using a dictionary as needed). The meanings are the book’s (장롱 is not in the chapter glossary: the gloss is mine); the grouping is my answer.",
             tables=[ktable([(w, m) for w, m, g in _VB])]),
        card("My groups",
             "One way to group them:",
             tables=[table(["Group (mine)", "Words"], [[g, ", ".join(ws)] for g, ws in _VBG], say=[1])]),
        card("Activities left out", "Activities 1, 2, 3 and 4 (SMART Board), the PowerPoint Sino-Korean presentation, step b (comparing with a partner and getting the teacher’s feedback), and Activity 5 (two teams write as many topic-related words as possible on the classroom wall and cross out unrelated words; the team with the most words wins) are computer, group and game activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["맞추다", "볶다", "베개", "삶다", "이불", "캐주얼", "튀기다", "한옥", "편안하다", "화려하다", "굽다", "대문", "저고리", "내의"]))
        + [M("Which group does 튀기다 belong to?", "Cooking", ["Clothing", "House and bedding", "Describing"], "My grouping."), M("Which group does 저고리 belong to?", "Clothing", ["Cooking", "House and bedding", "Describing"], "My grouping."), M("Which group does 베개 belong to?", "House and bedding", ["Cooking", "Clothing", "Describing"], "My grouping."), M("Which group does 화려하다 belong to?", "Describing", ["Cooking", "Clothing", "House and bedding"], "My grouping."), M("Which group does 끓이다 belong to?", "Cooking", ["Clothing", "House and bedding", "Describing"], "My grouping."), M("Which group does 대문 belong to?", "House and bedding", ["Cooking", "Clothing", "Describing"], "My grouping."), M("What does 장롱 mean?", "a wardrobe; a clothes chest", ["a pillow", "a blanket", "a front gate"], "My gloss."),
           F("물을 ___ 차를 마시려고 합니다. (boil)", "끓여서", ["볶아서", "굽고"], "끓이다."), F("야채를 기름에 ___ 먹어요. (stir fry)", "볶아서", ["삶아서", "끓여서"], "볶다."), F("달걀을 ___ 샐러드를 만듭니다. (boil)", "삶아서", ["튀겨서", "구워서"], "삶다."), F("고기를 불에 ___ 먹었어요. (grilled)", "구워서", ["삶아서", "끓여서"], "굽다."), F("감자를 기름에 ___ 감자튀김을 만듭니다. (deep fry)", "튀겨서", ["삶아서", "끓여서"], "튀기다."),
           read_q("맞추다"), read_q("볶다"), read_q("삶다"), read_q("튀기다"), read_q("저고리")]
    ),
)

# ================================================================== L3 Topic A
_A_P1 = [("한국사람들은 옛날에 한복을 입었다.", "Koreans wore hanbok in the old days."), ("기본적으로 남자는 바지와 저고리, 여자는 치마와 저고리를 입었다.", "Basically, men wore trousers and a jeogori, and women wore a skirt and a jeogori."), ("또, 입는 사람과 목적에 따라 한복의 모양과 색이 다양했다.", "Also, the shape and color of hanbok were varied according to the wearer and the purpose."), ("계층이 높은 사람들은 색이 화려하거나 장식이 많은 옷을 입었다.", "People of high social class wore clothes that were colorful or had many decorations."), ("계층이 낮은 사람들은 흰 옷을 입었다.", "People of low social class wore white clothes."), ("현대 한국인들은 서양 문화의 영향으로 평상시에는 한복을 잘 입지 않는다.", "Modern Koreans, under the influence of Western culture, do not often wear hanbok in ordinary times."), ("한복은 주로 명절이나 결혼식과 같은 특별한 때에 입는다.", "Hanbok is mostly worn on special occasions such as holidays or weddings.")]
_A_P2 = [("송은지 씨는 스물여덟 살의 기혼 직장 여성이다.", "Ms. Song Eunji is a 28-year-old married working woman."), ("송은지 씨의 직장에서는 보통 정장을 입고 구두를 신어야 한다.", "At Ms. Song’s workplace, you usually have to wear a suit and shoes."), ("그러나 금요일에는 캐주얼한 옷을 입어도 된다.", "But on Fridays, you may wear casual clothes."), ("그래서 그날은 유행하는 스타일의 편안한 옷을 입는다.", "So on that day she wears comfortable clothes in a trendy style."), ("다음 주 화요일은 설날이다.", "Next Tuesday is Lunar New Year’s Day."), ("설날에 송은지 씨 부부는 한복을 입고 시댁에 간다.", "On Lunar New Year’s Day, Ms. Song and her husband wear hanbok and go to her husband’s family’s home."), ("올해는 새로 맞춘 한복을 입고 가려고 한다.", "This year they intend to go wearing newly custom-made hanbok."), ("송은지 씨는 분홍색, 남편은 연한 파란색 한복을 입을 것이다.", "Ms. Song will wear pink and her husband will wear light blue hanbok."), ("시부모님께는 따뜻한 내의를 한 벌씩 선물해 드릴 생각이다.", "She plans to give her parents-in-law a set of warm underwear each as a present.")]
_A_WORDS = ["계층", "기본(적)(으로)", "기혼", "내의/속옷", "동양", "따르다", "맞추다", "~ 벌", "분홍색", "새로", "서양", "스타일", "연하다", "영향", "장식", "저고리", "캐주얼", "편안하다", "평상시", "화려하다", "희다/하얗다"]
_NK = [("80년대 중반까지 북한 여성들은 검정 치마에 흰 저고리를 주로 입었다.".replace("80년대", "팔십 년대"), "Until the mid-1980s, North Korean women mostly wore a black skirt with a white jeogori."), ("그 이후에 원피스, 투피스, 블라우스, 스웨터 등과 같은 다양한 서양식 옷을 입기 시작했다.", "After that they began to wear various Western-style clothes such as one-piece dresses, two-piece suits, blouses and sweaters."), ("천구백구십 년대에도 계속 서양식 옷을 입었다.", "They kept wearing Western-style clothes in the 1990s too."), ("그러나 짧은 치마와 영어가 쓰여 있는 옷, 청바지는 단속 대상이 되었다.", "But short skirts, clothes with English written on them, and jeans became targets of crackdowns."), ("북한에도 패션 잡지가 있는데 무역이라고 한다.", "North Korea also has a fashion magazine, called “Trade”."), ("최근에는 북한 신세대들이 남한의 인기 드라마에 나오는 탤런트들의 패션을 따르고 있다.", "Recently, the North Korean new generation has been following the fashion of the actors who appear in popular South Korean dramas."), ("이들은 높은 계층의 자녀들인데 남한 탤런트들의 옷, 머리 스타일, 머리 염색까지 따라 하고 있다.", "They are children of the high classes, and they are copying even the South Korean actors’ clothes, hairstyles and hair dyeing."), ("신세대들은 컴퓨터나 몰래 들여온 남한 드라마를 보고 남한 패션을 배운다.", "The new generation learns South Korean fashion by watching computers or South Korean dramas that were secretly brought in.")]
_GN = [("설맞이 외국인 한복 입기 체험 행사 열려", "A hanbok-wearing experience event for foreigners to welcome the Lunar New Year is held"), ("서울 강남구는 설을 맞아 강남시티투어에 참여한 외국인들을 대상으로 한복 입기와 세배하기 체험행사를 열었습니다.", "Gangnam-gu, Seoul, held a hanbok-wearing and New Year’s bow experience event for foreigners who took part in the “Gangnam City Tour” to welcome the Lunar New Year."), ("이번 행사에서 외국인들은 한국의 예절과 한복에 대한 설명을 듣고 직접 한복을 입어 보고 세배도 했습니다.", "At this event, the foreigners listened to explanations of Korean etiquette and hanbok, tried on hanbok themselves, and also did the New Year’s bow."), ("강남구는 이번 행사를 통해 외국인들이 우리 전통문화를 체험해 한국에 대한 뜻깊은 추억을 만들 것으로 기대한다고 밝혔습니다.", "Gangnam-gu said it hopes that through this event, foreigners will experience our traditional culture and make meaningful memories of Korea.")]
L3 = lesson(
    "Ch 41 · Topic A: When do people wear hanbok? (한복은 언제 입을까요?)",
    "한복 · 저고리 · 정장과 캐주얼 · 내의 선물 · 북한의 패션 · 한복 체험 행사",
    requires=[],
    cards=[
        card("Topic A: When do people wear hanbok? (한복은 언제 입을까요?)",
             "The following article is about clothing worn by Koreans in the past and today. (The English is mine; the book gives none.)",
             examples=passage(_A_P1)),
        card("Ms. Song Eunji’s clothes", "The second text of Topic A (the English is mine; her age is spelled out in Hangul):", examples=passage(_A_P2)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_A_WORDS)),
        card("한국에서는: 내의 (內衣)",
             "내의 (內衣), which literally means “inside clothes,” refers to underwear. In certain contexts, 내의 can also refer to thermal underwear known as 내복 (內服). It has been a tradition for grown children to buy parents thermal 내의 or 내복 when they get their first paycheck. Giving 내의 to parents is not limited to that occasion, however. 내의 has been a popular and practical gift item for parents or any elderly relative on birthdays or traditional holidays. Although this tradition is not as common now as in the past, it is still practiced today."),
        card("Follow-up 2 (Reading): fashion in North Korea",
             "The following article is about fashion in North Korea; the book asks you to read it and fill in a table in English with North Korean fashion (early 1980s), North Korean fashion (late 1980s), forbidden fashions, and fashion of North Korea’s new generation. The book glosses 대상: a target, an object; 몰래: secretly. The article is the book’s with the years spelled out in Hangul (the book’s quotation marks around the magazine title are dropped); the English is mine.",
             examples=passage(_NK)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["North Korean fashion (early 1980s)", "A black skirt with a white jeogori (until the mid-1980s)"], ["North Korean fashion (late 1980s)", "Began to wear Western-style clothes: one-piece, two-piece, blouses, sweaters (and kept doing so in the 1990s)"], ["Forbidden fashions", "Short skirts, clothes with English written on them, and jeans"], ["Fashion of North Korea’s new generation", "Following South Korean TV actors’ clothes, hairstyles and hair dyeing; children of high classes; learning from computers and secretly brought-in South Korean dramas"]])]),
        card("Activity 2 (Reading): a Lunar New Year event",
             "The following excerpt is from a Korean newspaper article about an event held on Lunar New Year. The book asks you to skim the title, write in English the type of event that was held, and fill in a table (Participants / What participants did). The book glosses 추억: memory, remembrance. The article is the book’s (the quotation marks are dropped); the English is mine.",
             examples=passage(_GN)),
        card("The answers (mine)", "",
             tables=[table(["Question", "Answer (mine)"], [["Type of event", "A hanbok-wearing and New Year’s bow experience event for foreigners, to welcome the Lunar New Year"], ["Participants", "Foreigners who took part in the Gangnam City Tour"], ["What participants did", "Listened to explanations of Korean etiquette and hanbok, tried on hanbok, and did the New Year’s bow"]])]),
        card("Activities left out", "The presentation steps of Topic A (SMART Board and listening), Follow-up 1 (listening to three conversations between a man and a woman at work about women’s clothing and the occasion), Activity 1 (SMART Board) and Activity 3 (listening to three conversations in which a man asks a woman for tips about dressing for an occasion, and checking traditional Korean clothing, formal clothing or casual wear) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_A_P1 + _A_P2 + _NK + _GN, k=3)
        + [M("What did men basically wear in hanbok?", "Trousers and a jeogori", ["A skirt and a jeogori", "A suit", "A coat"], "남자는 바지와 저고리."), M("What did people of low class wear?", "White clothes", ["Colorful clothes", "Silk", "Suits"], "흰 옷."), M("When is hanbok mostly worn today?", "On holidays and at weddings", ["Every day", "At work", "At school"], "명절이나 결혼식."), M("What does Ms. Song wear on Fridays?", "Comfortable casual clothes in a trendy style", ["A hanbok", "A suit", "Sportswear"], "금요일에는 캐주얼."), M("What color hanbok will Ms. Song wear?", "Pink", ["Light blue", "White", "Black"], "분홍색."), M("What will Ms. Song give her parents-in-law?", "Warm underwear", ["Hanbok", "Shoes", "Tea"], "따뜻한 내의."), M("What did North Korean women mostly wear until the mid-1980s?", "A black skirt with a white jeogori", ["Jeans", "Suits", "Hanbok in pink"], "검정 치마에 흰 저고리."), M("What event did Gangnam-gu hold?", "A hanbok-wearing experience for foreigners", ["A fashion show", "A cooking contest", "A marathon"], "한복 입기와 세배하기 체험행사."),
           F("계층이 높은 사람들은 색이 ___ 옷을 입었다. (colorful)", "화려한", ["연한", "편안한"], "화려하다."), F("올해는 새로 ___ 한복을 입고 가려고 한다. (custom-made)", "맞춘", ["산", "만든"], "맞추다."), F("서양 문화의 ___으로 한복을 잘 입지 않는다. (influence)", "영향", ["장식", "스타일"], "영향."), F("송은지 씨는 ___ 직장 여성이다. (married)", "기혼", ["미혼", "연한"], "기혼."), F("한복은 ___시에는 잘 입지 않는다. (ordinary times)", "평상", ["평소", "특별"], "평상시."),
           read_q("한복은 언제 입을까요"), read_q("남자는 바지와 저고리를 입었습니다"), read_q("금요일에는 캐주얼한 옷을 입어도 됩니다"), read_q("올해는 새로 맞춘 한복을 입고 가려고 합니다"), read_q("부모님께 따뜻한 내의를 선물해 드릴 생각입니다")]
    ),
)

# ================================================================== L4 Activities A: clothing consultants
_CONS = [("제안 일", "보통 회사에서 정장을 많이 하니까 양복을 여러 벌 준비하시면 좋습니다. 양복이 많으면 셔츠나 넥타이를 고르기도 쉽습니다. 유행하는 스타일에 따라서 다양하게 준비하세요. 요즘은 짙은 색깔이 유행하니까 짙은 색깔의 넥타이를 사시면 어떨까요? 그리고 금요일에는 분홍색 셔츠보다는 연한 파랑이나 검은색을 추천합니다.", "Since people usually wear suits at companies, it is good to prepare several suits. If you have many suits, it is also easy to choose shirts and ties. Prepare a variety according to the trendy style. These days dark colors are trendy, so how about buying a dark-colored tie? And on Fridays, I recommend light blue or black rather than a pink shirt."), ("제안 이", "우선 정장은 좋은 제품으로 두 벌 정도 사세요. 그리고 셔츠와 넥타이를 여러 색깔로 사세요. 셔츠는 연한 색깔이 넥타이와 맞춰서 입기 쉬워요. 그러니까 연한 색깔로 고르세요. 그리고 신입사원이니까 청바지는 피하세요. 다른 캐주얼 바지가 좋을 것 같습니다.", "First, buy about two suits of good quality. And buy shirts and ties in various colors. Shirts in light colors are easy to wear matched with ties. So choose light colors. And since you are a new employee, avoid jeans. Other casual trousers seem good."), ("제안 삼", "양복은 계절에 따라 겨울, 봄과 가을, 여름 양복으로 세 벌 정도 준비하시면 어때요? 색깔은 검정, 파랑, 회색이면 좋을 것 같습니다. 젊으시니까 넥타이는 화려한 색깔이 좋을 것 같습니다. 금요일에는 캐주얼하게 분홍색 셔츠와 청바지가 좋을 것 같아요.", "How about preparing about three suits, for winter, spring and fall, and summer, according to the season? Black, blue and gray seem good for colors. Since you are young, a colorful tie seems good. On Fridays, a pink shirt and jeans seem good as casual wear.")]
L4 = lesson(
    "Ch 41 · Activities A: What should I wear? Three clothing consultants",
    "어떤 옷을 입어야 할까요 · 양복 · 셔츠와 넥타이 · 금요일의 캐주얼 · 신입사원",
    requires=[],
    cards=[
        card("Activity 4: What should I wear? (어떤 옷을 입어야 할까요?)",
             "You will listen to a phone message in which a college graduate asks about suitable clothing for work (audio: the caller’s facts and questions are in the recording and are left out). Three different clothing consultants write back with suggestions. The book asks you to rank the suggestions, write the reasons in English, discuss in Korean with a partner, choose the best, and present it. The three suggestions are the book’s (the labels are spelled out in Hangul: 제안 일, 이, 삼); the English is mine.",
             examples=dlg(_CONS)),
        card("What each consultant says (mine)",
             "The ranking depends on the caller’s facts in the recording, so I give the points of each suggestion instead:",
             tables=[table(["Suggestion", "Main points (mine)"], [["1", "Several suits; many suits make choosing shirts and ties easy; follow trends, with dark colors and dark ties; on Fridays light blue or black rather than pink"], ["2", "About two good-quality suits; shirts and ties in various colors; light-colored shirts match ties easily; avoid jeans as a new employee; choose other casual trousers"], ["3", "About three suits by season (winter, spring/fall, summer); black, blue or gray; a colorful tie because you are young; a pink shirt and jeans on Fridays"]])]),
        card("Activities left out", "The phone message (audio), ranking with reasons, the pair discussion in Korean, writing the choice in the class notebook (MS Teams), presenting in Korean and getting feedback are listening, pair and presentation activities."),
    ],
    exercises=uniq(
        _tr(_strip(_CONS), k=3)
        + [M("Which suggestion tells the caller to avoid jeans as a new employee?", "Suggestion 2", ["Suggestion 1", "Suggestion 3", "None of them"], "신입사원이니까 청바지는 피하세요."), M("Which suggestion tells the caller to prepare suits by season?", "Suggestion 3", ["Suggestion 1", "Suggestion 2", "None of them"], "계절에 따라."), M("Which suggestion recommends dark ties because they are trendy?", "Suggestion 1", ["Suggestion 2", "Suggestion 3", "None of them"], "짙은 색깔이 유행."), M("What does Suggestion 2 say about light-colored shirts?", "They are easy to wear matched with ties", ["They are too casual", "They are expensive", "They are for Fridays only"], "연한 색깔이 넥타이와 맞춰서 입기 쉬워요."), M("What does Suggestion 3 recommend for Fridays?", "A pink shirt and jeans", ["A black shirt", "A light blue shirt", "A hanbok"], "금요일에는 분홍색 셔츠와 청바지."),
           F("셔츠는 연한 색깔이 넥타이와 ___ 입기 쉬워요. (matching)", "맞춰서", ["따라서", "섞어서"], "맞추다."), F("요즘은 ___ 색깔이 유행합니다. (dark)", "짙은", ["연한", "흰"], "짙다."), F("신입사원이니까 청바지는 ___. (avoid)", "피하세요", ["입으세요", "사세요"], "피하다."), F("양복은 계절에 ___ 준비하세요. (according to)", "따라", ["대해", "위해"], "에 따라."), F("젊으시니까 넥타이는 ___ 색깔이 좋을 것 같습니다. (colorful)", "화려한", ["연한", "편안한"], "화려하다."),
           read_q("양복을 여러 벌 준비하시면 좋습니다"), read_q("셔츠와 넥타이를 여러 색깔로 사세요"), read_q("신입사원이니까 청바지는 피하세요"), read_q("계절에 따라 양복을 준비하세요"), read_q("금요일에는 캐주얼하게 입으세요")]
    ),
)

# ================================================================== L5 Topic B
_B_TXT = [("김치는 한국의 대표적인 음식이다.", "Kimchi is a representative food of Korea."), ("여러 종류의 김치가 있지만, 그중에서 배추김치가 가장 흔하다.", "There are many kinds of kimchi, but among them napa cabbage kimchi is the most common."), ("김치 양념에는 고춧가루를 포함해서 여러 가지가 들어간다.", "Various things go into the kimchi seasoning, including red pepper powder."), ("보통 십일월에 겨울 동안 먹을 김치를 담근다.", "Usually in November they make the kimchi to eat during the winter."), ("이것을 김장이라고 한다.", "This is called gimjang."), ("예전과 달리 요즘은 김장을 안 하는 사람도 많다.", "Unlike in the past, there are many people these days who do not make gimjang."), ("그렇지만, 주부 오선희 씨는 전통적인 김장 문화를 지키고 싶어 한다.", "However, the housewife Ms. Oh Seonhee wants to keep the traditional gimjang culture."), ("이웃끼리 서로 도우며 김장을 하는 모습이 아름답기 때문이다.", "This is because the sight of neighbors helping each other and making gimjang is beautiful."), ("올해에도 오선희 씨는 십일월 중순에 이웃과 함께 김장을 할 예정이다.", "This year too, Ms. Oh plans to make gimjang with her neighbors in mid-November."), ("김장이 끝난 후에는 도와준 이웃에게 저녁을 대접할 생각이다.", "After the gimjang is over, she plans to treat the neighbors who helped to dinner."), ("그리고 그다음 주에는 이웃집 김장을 도와주러 갈 것이다.", "And the following week she will go to help with her neighbor’s gimjang.")]
_B_WORDS = ["고춧가루", "굽다", "김장", "끓다/끓이다", "담그다", "대접", "뒤집다", "마늘", "모습", "문화", "미역국", "배추", "볶다", "붓다", "살짝", "삶다", "섞다/섞이다", "썰다", "이웃", "익다/익히다", "재료", "절다/절이다", "젓다", "찌다", "튀기다", "푹"]
_KIM = [("배추김치", "napa cabbage kimchi"), ("총각김치", "ponytail radish kimchi (“bachelor kimchi”, small whole radishes)"), ("오이김치", "cucumber kimchi"), ("깍두기", "cubed radish kimchi"), ("부추김치", "chive kimchi"), ("파김치", "green onion kimchi"), ("동치미", "radish water kimchi"), ("백김치", "white kimchi (without red pepper)")]
_SGK = [("이영희 씨는 직장생활을 한다.", "Ms. Lee Younghee has a job."), ("또한, 마당이 없는 아파트에 살기 때문에 매년 김장이 고민이다.", "Also, because she lives in an apartment without a yard, gimjang is a worry every year."), ("이웃들도 모두 바빠서 도움을 받기도 어렵다.", "Her neighbors are all busy too, so it is hard to get help."), ("그래서 이영희 씨는 매년 백화점에서 절임 배추를 주문했다.", "So every year Ms. Lee ordered “salted cabbage” from a department store."), ("절임 배추는 집에서 양념만 하면 되기 때문이다.", "This is because with salted cabbage, you only have to do the seasoning at home."), ("그렇지만 올해는 맞춤 김치를 주문하려고 한다.", "However, this year she intends to order “custom kimchi”."), ("절임 배추보다 조금 더 비싸지만 양념까지 다 해주기 때문이다.", "It is a little more expensive than salted cabbage, but they even do all the seasoning."), ("또한 자신이 좋아하는 양념과 맛을 고를 수도 있다.", "Also, she can choose the seasoning and taste she likes."), ("이영희 씨는 직장을 다니는 동안에는 계속 김장을 주문할 생각이다.", "Ms. Lee plans to keep ordering gimjang as long as she works at a job.")]
L5 = lesson(
    "Ch 41 · Topic B: Korean gimjang culture (한국의 김장 문화)",
    "김치 · 김장 · 배추 · 고춧가루 · 이웃 · 절임 배추 · 맞춤 김치 · 요리 방법",
    requires=[],
    cards=[
        card("Topic B: Korean gimjang culture (한국의 김장 문화)",
             "The following text is about the traditions involved when making kimchi in Korea. (The English is mine; the book gives none; the month is spelled out in Hangul.)",
             examples=passage(_B_TXT)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_B_WORDS)),
        card("한국에서는: 김장",
             "김장 refers to making kimchi (for the winter). It was traditionally an important annual event for Koreans because it allowed them to eat vegetables throughout the winter when fresh vegetables were not readily available. In early winter, every household used to make kimchi using various vegetables but mainly napa cabbage and radishes. The kimchi was stored in jars called 김장독/김칫독 and buried in the ground, which functioned much like a refrigerator. Because 김장 is very labor intensive, Koreans used to invite their neighbors to help. These days, with the availability of good-quality commercial 김치 and fresh vegetables throughout the winter, 김장 is not as common as in the past. Today, with 김치 냉장고, which can preserve kimchi for long periods, the practice of burying 김장독 in the ground is no longer common."),
        card("김치의 종류 (kinds of kimchi)", "The book shows pictures of eight kinds of kimchi (the English is mine):", tables=[ktable(_KIM)]),
        card("Follow-up 1 (Listening): cooking methods", "The book asks you to listen to four segments in which a chef talks about a dish (스파게티, 불고기, 김밥, 감자 튀김) and how to make it, and to choose the cooking method(s) from a list: 1. steaming; 2. boiling; 3. frying; 4. cutting; 5. salting; 6. deep-frying; 7. baking; 8. turning over; 9. stirring; 10. mixing/blending (the book glosses 말다: to roll; 얇다: to be thin). This is an audio activity and is left out; the methods match the verbs 찌다, 삶다, 볶다, 썰다, 절이다, 튀기다, 굽다, 뒤집다, 젓다 and 섞다 of the core vocabulary."),
        card("Follow-up 2 (Reading): a younger generation’s gimjang",
             "The following passage is an excerpt from a news article about a younger generation homemaker (the book glosses 절임 배추: salted cabbage for kimchi). The book asks you to mark three statements True or False. The passage is the book’s (the quotation marks are dropped); the English is mine.",
             examples=passage(_SGK)),
        card("The answers (mine)", "",
             tables=[table(["Statement", "True / False (mine)"], [["1. It is hard for Mrs. Lee to make 김장 because she lives in an apartment.", "True (she has no yard; her neighbors are busy too)"], ["2. The department store offers salted cabbage for younger generation homemakers.", "True (she orders it from a department store every year)"], ["3. It takes less time to make kimchi when using salted cabbage.", "True (only the seasoning is left to do at home)"]])]),
        card("Activities left out", "The presentation steps of Topic B (SMART Board and the pair translation exercise) and Activity 3 (listening to two families’ kimchi-making stories and comparing participants, size, other activities after making kimchi and types of kimchi made, with a Venn diagram, group and pair work) are audio, computer and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_B_TXT + _SGK + _KIM, k=3)
        + [M("Which kimchi is the most common?", "Napa cabbage kimchi", ["Cucumber kimchi", "Green onion kimchi", "White kimchi"], "배추김치가 가장 흔하다."), M("What goes into kimchi seasoning?", "Red pepper powder and other things", ["Only salt", "Only sugar", "Rice"], "고춧가루를 포함해서."), M("What is 김장?", "Making kimchi for the winter", ["Making soup", "Buying vegetables", "A holiday"], "겨울 동안 먹을 김치를 담근다."), M("How does Ms. Oh want to make gimjang?", "In the traditional way with her neighbors", ["Alone", "By ordering it", "At a restaurant"], "이웃과 함께."), M("What will Ms. Oh do after the gimjang?", "Treat the neighbors who helped to dinner", ["Sell the kimchi", "Go on a trip", "Rest"], "저녁을 대접."), M("Why does Ms. Lee order salted cabbage?", "She lives in an apartment, works, and neighbors are busy", ["She dislikes kimchi", "It is free", "She has a big yard"], "직장, 아파트, 바쁜 이웃."), M("What does “custom kimchi” include that salted cabbage does not?", "All the seasoning", ["The jar", "The delivery", "The recipe"], "양념까지 다 해주기 때문."), M("What kimchi jars were buried in the ground?", "김장독", ["김치 냉장고", "그릇", "봉투"], "김장독/김칫독."),
           F("배추를 소금에 ___ 김치를 담근다. (salt)", "절여서", ["삶아서", "끓여서"], "절이다."), F("김치를 ___ 때 제일 중요한 것은 양념입니다. (make)", "담글", ["굽을", "삶을"], "담그다."), F("도와준 이웃에게 저녁을 ___ 생각이다. (treat)", "대접할", ["섞을", "뒤집을"], "대접하다."), F("올해에도 십일월 ___에 김장을 할 예정이다. (mid-month)", "중순", ["초순", "하순"], "중순."), F("이웃끼리 서로 도우며 김장을 하는 ___이 아름답다. (sight)", "모습", ["재료", "문화"], "모습."),
           read_q("김장"), read_q("배추김치"), read_q("고춧가루"), read_q("이웃과 함께 김장을 합니다"), read_q("김장이 끝난 후에는 이웃에게 저녁을 대접합니다")]
    ),
)

# ================================================================== L6 Grammar A: unlike
_UN1 = [("형과 달리 저는 농구를 잘 합니다.", "Unlike my older brother, I play basketball well."), ("형하고 달리 저는 농구를 잘 합니다.", "Unlike my older brother, I play basketball well. (~하고 달리)"), ("형과는 달리 저는 농구를 좋아합니다.", "Unlike my older brother, I like basketball."), ("형하고는 달리 저는 농구를 좋아해요.", "Unlike my older brother, I like basketball.")]
_UN2 = [("한국인들은 미국인들하고 달리 생일날 미역국을 먹습니다.", "Unlike Americans, Koreans eat seaweed soup on their birthdays."), ("구세대와 달리 신세대는 변화를 좋아합니다.", "Unlike the older generation, the younger generation likes change."), ("작년과 달리 올해는 장마가 빨리 시작됐습니다.", "Unlike last year, the rainy season started earlier this year."), ("이 의자는 다른 의자와 달리 아주 편합니다.", "Unlike other chairs, this chair is very comfortable.")]
_UN3 = [("몬트레이는 뉴욕과 달리 겨울에 눈이 안 와요.", "Unlike New York, it does not snow in Monterey in winter."), ("몬트레이는 뉴욕하고 달리 겨울에 눈이 안 와요.", "Unlike New York, it does not snow in Monterey in winter.")]
_UN4 = [("한국과 일본의 음식문화는 비슷한 점도 있고 다른 점도 있습니다.", "The food cultures of Korea and Japan have both similarities and differences."), ("일본사람들도 한국사람들처럼 야채와 생선을 많이 먹습니다.", "Japanese people, like Koreans, eat a lot of vegetables and fish."), ("그렇지만 일본음식은 한국음식과 달리 매운 음식이 별로 없습니다.", "However, unlike Korean food, Japanese food has few spicy dishes."), ("또 일본사람들도 한국사람들처럼 식사할 때 젓가락을 씁니다.", "Also, Japanese people, like Koreans, use chopsticks when they eat."), ("그렇지만 한국사람들은 일본사람들과 다르게 밥을 먹을 때도 젓가락을 잘 사용하지 않습니다.", "However, unlike Japanese people, Koreans do not often use chopsticks even when they eat rice."), ("한국에서는 젓가락으로 밥을 먹는 것은 예의가 아닙니다.", "In Korea, eating rice with chopsticks is not polite.")]
L6 = lesson(
    "Ch 41 · Grammar A: expressing “unlike”, ~와/과 달리 and ~하고 달리",
    "~와/과 달리 · ~하고 달리 · ~와/과는 달리 · 형과 달리 · 작년과 달리 · 한국과 일본의 음식문화",
    requires=[],
    cards=[
        card("Recall ~처럼, then “unlike”",
             "Recall the grammar feature ~처럼 that you learned about in Chapter 34. Its function and use are similar to the English preposition like, as in 우리 형처럼 저는 농구를 잘 해요 (Like my older brother, I am good at basketball). 우리 형처럼 (like my older brother) tells us that the speaker’s older brother is good at basketball and so is the speaker.\n\n"
             "How then do we express “unlike my older brother” in Korean? Note the following sentences (the English is the book’s):",
             examples=passage(_UN1[:2])),
        card("달리 and the topic marker",
             "Note that 달리 in ~와/과 달리 and ~하고 달리 come from the verb 다르다 (to be different). Note also that 달리 is preceded by ~와/과 or ~하고. The topic marker 은/는 can be added to ~와/과 and ~하고, as shown in the following examples:",
             examples=passage(_UN1[2:])),
        card("Expressing “unlike”: ~와/과 달리, ~하고 달리", "More examples (the English is the book’s):", examples=passage(_UN2)),
        card("Follow-up 1 (Speaking): the model",
             "Student A makes a sentence using the grammar feature ~와/과 달리 and the words on the strip. Student B then repeats Student A’s entire sentence, replacing ~와/과 달리 with ~하고 달리. The book’s model (the strip says 몬트레이 vs. 뉴욕; the English is mine):",
             examples=dlg([("A", _UN3[0][0], _UN3[0][1]), ("B", _UN3[1][0], _UN3[1][1])])),
        card("Follow-up 2 (Reading): food culture in Korea and Japan",
             "The following passage compares food culture in Korea and Japan; the book asks you to read it and fill in a table (Similarity / Difference). The passage is the book’s; the English is mine.",
             examples=passage(_UN4)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Similarity", "Both eat a lot of vegetables and fish; both use chopsticks when eating"], ["Difference", "Japanese food has few spicy dishes, unlike Korean food; Koreans often do not use chopsticks even when eating rice, and eating rice with chopsticks is impolite in Korea"]])]),
    ],
    exercises=uniq(
        _tr(_UN1 + _UN2 + _UN3 + _UN4, k=3)
        + [M("What does 달리 come from?", "The verb 다르다 (to be different)", ["The verb 달리다", "The noun 달", "The verb 달다"], "The book’s note."), M("What precedes 달리?", "~와/과 or ~하고", ["~을/를", "~에서", "~도"], "The book’s note."), M("What can be added to ~와/과 and ~하고?", "The topic marker 은/는", ["The subject marker", "The object marker", "Nothing"], "형과는 달리."), M("What does ~처럼 mean?", "like", ["unlike", "including", "among"], "Chapter 34."), M("What does 구세대와 달리 신세대는 변화를 좋아합니다 mean?", "Unlike the older generation, the younger generation likes change", ["Like the older generation, the young like change", "The older generation likes change", "The young dislike change"], "The book’s example."), M("What does 이 의자는 다른 의자와 달리 아주 편합니다 mean?", "Unlike other chairs, this chair is very comfortable", ["Like other chairs", "This chair is expensive", "Other chairs are comfortable"], "The book’s example."),
           F("형___ 달리 저는 농구를 잘 합니다. (unlike)", "과", ["이", "을"], "형과 달리."), F("미국인들___ 달리 한국인들은 생일날 미역국을 먹습니다. (unlike)", "하고", ["보다", "처럼"], "하고 달리."), F("작년과 ___ 올해는 장마가 빨리 시작됐습니다. (unlike)", "달리", ["같이", "처럼"], "과 달리."), F("일본음식은 한국음식과 ___ 매운 음식이 별로 없습니다. (unlike)", "달리", ["같이", "처럼"], "과 달리."), F("형과___ 달리 저는 농구를 좋아합니다. (topic marker)", "는", ["도", "만"], "과는 달리."),
           read_q("형과 달리 저는 농구를 잘 합니다"), read_q("구세대와 달리 신세대는 변화를 좋아합니다"), read_q("작년과 달리 올해는 장마가 빨리 시작됐습니다"), read_q("이 의자는 다른 의자와 달리 아주 편합니다"), read_q("일본음식은 한국음식과 달리 매운 음식이 별로 없습니다")]
    ),
)

# ================================================================== L7 Grammar B: including
_IN1 = [("국방외국어대학에서는 한국어를 포함해(서) 많은 언어를 가르칩니다.", "Many languages, including Korean, are taught at DLI."), ("김 일병을 포함해(서) 많은 학생이 한국에 갑니다.", "Many students are going to Korea, including PFC Kim.")]
_IN2 = [("세탁기와 냉장고를 포함해서 다양한 가전제품을 세일합니다.", "Various home appliances, including washers and refrigerators, are on sale."), ("팔십팔 년 서울 올림픽에는 미국을 포함해 백오십구 개국이 참가했습니다.", "One hundred fifty-nine countries, including the U.S., participated in the Seoul Olympic Games in 1988.")]
_CONT = [("아시아", "중국, 일본, 한국, 인도, 베트남, 태국"), ("유럽", "영국, 프랑스, 독일, 이탈리아, 스페인"), ("남아메리카", "브라질, 아르헨티나, 칠레, 페루"), ("북아메리카", "미국, 캐나다, 멕시코"), ("오스트레일리아", "오스트레일리아, 뉴질랜드, 파푸아뉴기니, 피지"), ("아프리카", "이집트, 케냐, 나이지리아, 남아프리카공화국")]
_IN3 = [("아시아에는 어떤 나라가 있어요?", "What countries are there in Asia?"), ("중국, 일본 등을 포함해서 여러 나라가 있어요.", "There are several countries, including China, Japan, etc.")]
_IN4 = [("요즘 한국 음식을 먹는 외국인들이 점점 늘어나고 있습니다.", "These days the number of foreigners who eat Korean food is gradually increasing."), ("비빔밥을 포함해 불고기, 김치찌개 등이 특히 인기가 있습니다.", "Including bibimbap, bulgogi, kimchi stew, etc. are especially popular."), ("한국의 대표적인 음식인 김치도 많은 외국인이 좋아합니다.", "Many foreigners also like kimchi, a representative Korean food."), ("대부분의 외국인들은 처음에는 김치를 잘 못 먹습니다.", "Most foreigners cannot eat kimchi well at first."), ("하지만, 김치는 먹을수록 맛있다고 합니다.", "But they say that the more you eat kimchi, the tastier it is."), ("김치는 종류가 아주 많습니다.", "There are very many kinds of kimchi."), ("배추김치를 포함하여 오이김치, 파김치 등 다양한 종류의 김치가 있습니다.", "There are various kinds of kimchi, including napa cabbage kimchi, cucumber kimchi, green onion kimchi, etc."), ("김치를 담글 때 제일 중요한 것은 양념입니다.", "The most important thing when making kimchi is the seasoning."), ("김치 양념에는 고춧가루를 포함해서 파, 마늘, 양파 등이 들어갑니다.", "In the kimchi seasoning, green onion, garlic, onion, etc. go in, including red pepper powder.")]
_IN5 = [("제게 가장 기억에 남는 파티는 열 살 생일 파티입니다.", "The party that remains most in my memory is my 10th birthday party."), ("그 파티에는 제 친구 스티브를 포함해서 많은 친구가 왔습니다.", "Many friends came to that party, including my friend Steve."), ("친구들이 선물을 많이 주었습니다.", "My friends gave me a lot of presents."), ("저는 옷을 포함해서 구두, 책, 게임기 등을 선물로 받았습니다.", "I received shoes, books, game consoles, etc. as presents, including clothes.")]
L7 = lesson(
    "Ch 41 · Grammar B: expressing “including”, ~을/를 포함해(서)",
    "~을/를 포함해(서) · 한국어를 포함해서 · 김 일병을 포함해 · 대륙과 나라 · 한국 음식 · 기억에 남는 생일파티",
    requires=[],
    cards=[
        card("Expressing “including”",
             "Look closely at the underlined phrases in the following sentences to see how Koreans express “including something/somebody.” (The English is the book’s.)",
             examples=passage(_IN1)),
        card("Note", "Note that ~을/를 포함해서 is preceded by a noun and 서 in ~을/를 포함해서 can be deleted. More examples (the numbers are spelled out; the English is the book’s):", examples=passage(_IN2)),
        card("Follow-up 3 (Writing and speaking): countries on a continent",
             "In Korean, write the names of countries that are part of the continent listed in your column (Student A: 아시아, 남아메리카, 오스트레일리아; Student B: 유럽, 북아메리카, 아프리카). Then take turns asking each other what countries are part of the continents, using ~을/를 포함해(서). The book’s model (the English is mine):",
             examples=dlg([("A", _IN3[0][0], _IN3[0][1]), ("B", _IN3[1][0], _IN3[1][1])])),
        card("Some countries on each continent (mine)", "My sample answers:", tables=[table(["Continent", "Countries (mine)"], [[a, b] for a, b in _CONT], say=[0, 1])]),
        card("Follow-up 4 (Reading): Korean food and foreigners",
             "Read the following passage about Korean food and circle the grammar feature ~을/를 포함해(서); the book asks you to fill in a table in English. The passage is the book’s; the English is mine.",
             examples=passage(_IN4)),
        card("The table filled in (mine)", "",
             tables=[table(["Column", "Answer (mine)"], [["Popular Korean foods for foreigners", "Bibimbap, bulgogi, kimchi stew, etc."], ["Different types of kimchi", "Napa cabbage kimchi, cucumber kimchi, green onion kimchi, etc."], ["Ingredients for kimchi", "Red pepper powder, green onion, garlic, onion, etc."]])]),
        card("Follow-up 5 (Writing and speaking): the most memorable birthday party",
             "Recall your most memorable birthday party (who attended, what foods were served, the presents) and fill in the table in English; then write at least five sentences using ~을/를 포함해(서) as many times as you can. The book’s model is the one below (the number of years is missing in the printed text: 살 생일 파티; I have written 열 살; the English is mine). You then present in Korean and get feedback.",
             examples=passage(_IN5)),
    ],
    exercises=uniq(
        _tr(_IN1 + _IN2 + _IN3 + _IN4 + _IN5, k=3)
        + [M("What does ~을/를 포함해(서) mean?", "including", ["unlike", "among", "like"], "The book’s note."), M("What precedes ~을/를 포함해서?", "A noun", ["A verb stem", "A particle ~에서", "A number only"], "The book’s note."), M("What can be deleted in ~을/를 포함해서?", "서", ["를", "포함", "해"], "The book’s note."), M("What does 한국어를 포함해(서) 많은 언어를 가르칩니다 mean?", "Many languages, including Korean, are taught", ["Only Korean is taught", "Korean is not taught", "Korean was taught"], "The book’s example."), M("What goes into kimchi seasoning, including what?", "Red pepper powder", ["Rice", "Sugar only", "Soy sauce only"], "고춧가루를 포함해서."), M("How many countries took part in the 1988 Seoul Olympics?", "159", ["88", "100", "200"], "백오십구 개국."),
           F("국방외국어대학에서는 한국어___ 포함해 많은 언어를 가르칩니다. (object marker)", "를", ["가", "에"], "를 포함해."), F("김 일병___ 포함해서 많은 학생이 한국에 갑니다. (object marker)", "을", ["이", "에"], "을 포함해."), F("세탁기와 냉장고를 ___ 다양한 가전제품을 세일합니다. (including)", "포함해서", ["달리", "처럼"], "포함해서."), F("미국을 포함해 백오십구 ___이 참가했습니다. (countries)", "개국", ["개월", "개씩"], "개국."), F("중국, 일본 등을 포함해서 여러 ___가 있어요. (countries)", "나라", ["도시", "사람"], "나라."),
           read_q("한국어를 포함해서 많은 언어를 가르칩니다"), read_q("김 일병을 포함해서 많은 학생이 한국에 갑니다"), read_q("세탁기와 냉장고를 포함해서 가전제품을 세일합니다"), read_q("중국과 일본 등을 포함해서 여러 나라가 있어요"), read_q("고춧가루를 포함해서 파와 마늘이 들어갑니다")]
    ),
)

# ================================================================== L8 Activities B: recipes
_RMY = [("내일은 내 룸메이트의 생일이다.", "Tomorrow is my roommate’s birthday."), ("그래서 룸메이트를 위해서 미역국과 불고기를 만들기로 했다.", "So I decided to make seaweed soup and bulgogi for my roommate."), ("처음 만드는 음식이지만 만드는 법이 생각보다 쉬웠다.", "It is the first time I am making these foods, but the way to make them was easier than I thought.")]
_RMG = [("미역국 끓이는 법", "How to boil seaweed soup"), ("재료 미역, 소고기, 마늘, 양념 후추, 소금, 간장, 참기름", "Ingredients: seaweed, beef, garlic, seasoning (pepper, salt, soy sauce, sesame oil)"), ("일 마른 미역을 물에 넣고 불린다.", "1. Put dry seaweed in water and soak it."), ("이 소고기를 썬다. 소고기에 후추, 소금을 조금 뿌려 놓는다.", "2. Cut the beef. Sprinkle a little pepper and salt on the beef."), ("삼 십 분 후에, 미역을 물에서 꺼내서 소고기, 마늘, 참기름과 함께 넣고 볶는다.".replace("삼 십 분", "십 분"), "3. After 10 minutes, take the seaweed out of the water and put it in with the beef, garlic and sesame oil and fry it."), ("사 물을 붓고 오랫동안 끓인다.", "4. Pour in water and boil it for a long time."), ("오 마지막으로 소금과 간장을 조금 넣는다.", "5. Lastly, add a little salt and soy sauce.")]
_RBG = [("불고기 만드는 법", "How to make bulgogi"), ("재료 소고기, 양파, 파, 마늘, 양념 후추, 소금, 참기름, 설탕, 간장", "Ingredients: beef, onion, green onion, garlic, seasoning (pepper, salt, sesame oil, sugar, soy sauce)"), ("일 소고기 양파, 파를 잘게 썬다.", "1. Chop the beef, onion and green onion finely."), ("이 소고기에 소금과 후추를 조금 넣는다.", "2. Add a little salt and pepper to the beef."), ("삼 십 분 후에 참기름, 설탕, 간장, 마늘을 넣는다.", "3. After 10 minutes, add sesame oil, sugar, soy sauce and garlic."), ("사 세 시간 후에 고기를 양파, 파와 함께 볶는다.", "4. After three hours, fry the meat together with the onion and green onion.")]
L8 = lesson(
    "Ch 41 · Activities B: a blog with two recipes, 미역국 and 불고기",
    "미역국 끓이는 법 · 불고기 만드는 법 · 재료 · 순서 · 룸메이트의 생일",
    requires=[],
    cards=[
        card("Activity 2 (Reading): a personal blog",
             "The following excerpt is from a personal blog; the book asks you to read it and fill in a table in English (the dish and its ingredients), and then to write the name of each dish in Korean and number the steps in the order of making (the first step is given). The book glosses 참기름: sesame oil. The blog is the book’s with the numbers of the steps and the minutes spelled out (the steps are numbered 일, 이, 삼, 사, 오 in Hangul; the recipe lines keep their printed numbering as words); the English is mine.",
             examples=passage(_RMY + _RMG + _RBG)),
        card("The ingredient table filled in (mine)", "The table has blanks in the ingredients list (beef, ( ), pepper, salt, ( ), sesame oil, soy sauce / beef, salt, pepper, sesame oil, ( ), soy sauce, ( ), onion, ( )); my answers:",
             tables=[table(["Dish", "Missing ingredients (mine)"], [["미역국 (seaweed soup)", "seaweed (미역), garlic (마늘)"], ["불고기 (bulgogi)", "sugar (설탕), garlic (마늘), green onion (파)"]])]),
        card("The recipe order filled in (mine)", "The book’s nine mixed-up steps, sorted by dish (mine):",
             tables=[table(["Dish", "Order (mine)"], [["미역국", "1. Soak dry seaweed in water. 2. Cut up beef; add salt and pepper. 3. Let sit for 10 minutes, then add garlic and sesame oil and fry. 4. Pour water and boil it for a while. 5. Add salt and soy sauce."], ["불고기", "1. Slice beef, onion, and green onion. 2. Add a little salt and pepper to beef. 3. Combine sesame oil, sugar, soy sauce, and garlic. 4. After three hours, fry meat with onion and green onion."]])]),
        card("Activities left out", "Activity 1 (listening and reading with the SMART Board) is a computer and audio activity."),
    ],
    exercises=uniq(
        _tr(_RMY + _RMG + _RBG, k=3)
        + [M("Why is the writer making these dishes?", "For the roommate’s birthday", ["For a party at work", "For a contest", "For the holiday"], "룸메이트의 생일."), M("What is the first step of 미역국?", "Soak the dry seaweed in water", ["Fry the beef", "Add salt", "Boil water"], "마른 미역을 물에 넣고 불린다."), M("What is the last step of 미역국?", "Add a little salt and soy sauce", ["Boil the beef", "Fry the garlic", "Pour water"], "마지막으로."), M("What is the first step of 불고기?", "Chop the beef, onion and green onion finely", ["Add sugar", "Fry the meat", "Boil water"], "잘게 썬다."), M("How long do you wait before adding seasoning to the bulgogi?", "10 minutes", ["3 hours", "1 hour", "No wait"], "십 분 후에."), M("How long after seasoning do you fry the bulgogi?", "Three hours", ["10 minutes", "One hour", "Right away"], "세 시간 후에."), M("Which ingredient is in 불고기 but not in 미역국?", "Sugar", ["Garlic", "Salt", "Sesame oil"], "설탕."), M("Which ingredient is in 미역국 but not in 불고기?", "Seaweed", ["Onion", "Sugar", "Green onion"], "미역."),
           F("마른 미역을 물에 넣고 ___ . (soak)", "불린다", ["볶는다", "삶는다"], "불리다."), F("소고기를 ___ . (cut)", "썬다", ["붓는다", "젓는다"], "썰다."), F("물을 ___ 오랫동안 끓인다. (pour)", "붓고", ["썰고", "굽고"], "붓다."), F("마지막으로 소금과 간장을 조금 ___ . (add)", "넣는다", ["붓는다", "썬다"], "넣다."), F("세 시간 후에 고기를 양파, 파와 함께 ___ . (fry)", "볶는다", ["삶는다", "끓인다"], "볶다."),
           read_q("미역국 끓이는 법"), read_q("불고기 만드는 법"), read_q("마른 미역을 물에 넣고 불린다"), read_q("소고기를 썰어서 소금과 후추를 뿌립니다"), read_q("마지막으로 소금과 간장을 조금 넣습니다")]
    ),
)

# ================================================================== L9 Topic C
_C_TXT = [("지난 주말에 한옥마을에 다녀왔다.", "Last weekend I went to a hanok village."), ("우리가 간 한옥마을은 전주시 완산구 풍남동에 위치하고 있었다.", "The hanok village we went to was located in Pungnam-dong, Wansan-gu, Jeonju."), ("친구들과 함께 약도를 보고 찾아갔다.", "I went with friends, looking at a rough map."), ("그곳에는 한국의 전통가옥이 팔백여 채나 모여 있다.", "More than 800 traditional Korean houses are gathered there."), ("먼저 공예품 전시를 보러 갔다.", "First we went to see the craftwork exhibition."), ("종이로 만든 공예품이 매우 아름다웠다.", "The crafts made of paper were very beautiful."), ("우리가 직접 그릇도 만들어 보았다.", "We also tried making bowls ourselves."), ("또 전통찻집에 가서 전통차도 마셨다.", "Also we went to a traditional teahouse and drank traditional tea."), ("한옥마을을 다 둘러보고 숙소로 갔다.", "After looking around the whole hanok village, we went to the lodging."), ("우리가 묵은 숙소는 한옥마을 집 중에서 가장 큰 집이었다.", "The lodging we stayed at was the biggest house among the hanok village houses."), ("그림으로만 보던 한옥을 직접 보니까 아주 신기했다.", "It was amazing to see in person the hanok that I had only seen in pictures."), ("대문과 마당이 크고 지붕은 기와지붕이었다.", "The front gate and the yard were big and the roof was a tiled roof."), ("화장실이 뒷마당에 따로 있는 것도 재미있었다.", "It was also fun that the bathroom was separate, in the back yard."), ("밤에는 온돌방에서 이불을 펴고 잤다.", "At night we spread out blankets and slept in an ondol room."), ("내가 옛날 사람이 된 것 같았다.", "I felt as if I had become a person of the old days.")]
_C_WORDS = ["가옥", "공예(품)", "~구", "그릇", "그림", "기와", "(녹)차", "대문", "~동", "둘러보다", "매우", "목이 마르다", "베개", "세면도구", "숙소", "신기하다", "약도", "~ 여", "위치", "이불", "종이", "~ 채", "한옥"]
_HAN = [("안채", "the building for women (in a hanok)"), ("사랑채", "the building for men and guests"), ("건넌방", "the room on the opposite side of 안방"), ("대청", "wooden floor"), ("안방", "master bedroom"), ("마당", "courtyard"), ("부엌", "kitchen"), ("창고", "storage room"), ("대문", "main entrance; main gate; “big door”"), ("사랑방", "main room in 사랑채"), ("방", "room; guest room")]
_CAMP = [("전주 한옥마을 여름 캠프", "Jeonju Hanok Village summer camp"), ("전주 한옥마을에서는 여름방학 동안 여름 캠프를 엽니다.", "Jeonju Hanok Village holds a summer camp during summer vacation."), ("참가자들은 이 박 삼 일 동안 전통가옥에서 전통문화를 체험할 수 있습니다.", "Participants can experience traditional culture in traditional houses for 3 days and 2 nights."), ("기간 이천이십삼 년 칠월 십팔 일부터 칠월 이십 일까지", "Period: July 18 to July 20, 2023"), ("대상 초등학교 일 학년부터 육 학년까지 어린이", "Target: children from first grade to sixth grade of elementary school"), ("행사 전통 공예품 만들기, 전통 그릇 만들기, 한옥생활 체험, 전통 음악 공연, 차 마시는 예절 배우기", "Events: making traditional crafts, making traditional bowls, a hanok-living experience, a traditional music performance, learning tea-drinking etiquette"), ("준비물 세면도구", "What to bring: toiletries"), ("전주 한옥마을은 전주시 완산구 풍남동에 위치하고 있습니다.", "Jeonju Hanok Village is located in Pungnam-dong, Wansan-gu, Jeonju city.")]
L9 = lesson(
    "Ch 41 · Topic C: I visited a hanok village (한옥마을에 다녀왔다)",
    "한옥마을 · 전통가옥 · 안채와 사랑채 · 온돌 · 기와 · 여름 캠프",
    requires=[],
    cards=[
        card("Topic C: I visited a hanok village (한옥마을에 다녀왔다)",
             "Jinsoo’s journal entry is about visiting a hanok village over the weekend. (The English is mine; the book gives none; 800 is spelled out in Hangul. The book’s footnote: 다녀오다 [to visit] is similar to 갔다 오다.)",
             examples=passage(_C_TXT)),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter).", tables=_words(_C_WORDS)),
        card("한국에서는: 한옥",
             "한옥 (韓屋), which literally means “Korean house,” refers to a traditional Korean house. Soil, timber, and rock are the main materials used to construct a 한옥. Usually, the roof of a 한옥 is made of clay tiles called 기와. 온돌 (a heated stone floor) and 대청 (a wooden floor) in 한옥 help residents cope with extreme cold and heat. The living area in a 한옥 is divided into two sections: 안채 and 사랑채. 안채 is the area where women reside and 사랑채 is the area for men and guests (the book shows the floor plan of each area in pictures)."),
        card("The floor plans (the labels the book gives)", "안채 구조 (floor plan of 안채 [building for women]): 1. 건넌방, 2. 대청, 3. 안방, 4. 마당, 5. 부엌, 6. 방/창고, 7. 대문. 사랑채 구조 (floor plan of 사랑채 [building for men and guests]): 1. 부엌, 2. 사랑방, 3. 대청, 4. 방 (guest room).",
             tables=[ktable(_HAN)]),
        card("Presentation c: the table filled in (mine)", "The book asks you to use Topic C to fill in a table (Places Jinsoo visited / Jinsoo’s activities / Description of where Jinsoo stayed). My answers:",
             tables=[table(["Column", "Answer (mine)"], [["Places Jinsoo visited", "A hanok village in Pungnam-dong, Wansan-gu, Jeonju; a craftwork exhibition; a traditional teahouse"], ["Jinsoo’s activities", "Went with friends using a rough map; saw the craftwork exhibition (paper crafts); made bowls himself; drank traditional tea at a teahouse; looked around the village; slept in an ondol room on spread-out blankets"], ["Description of where Jinsoo stayed", "The biggest house in the hanok village; big front gate and yard; tiled roof; a separate bathroom in the back yard; ondol room"]])]),
        card("Follow-up 2 (Reading): a summer camp advertisement",
             "The following newspaper advertisement is for a summer camp that will be held at a hanok village; the book asks three questions (the book glosses 대상: target audience; 내용: contents). The advertisement is the book’s with the numbers spelled out (the web address is left out); the English is mine.",
             examples=passage(_CAMP)),
        card("The answers (mine)", "",
             tables=[table(["Question", "Answer (mine)"], [["1. Who can participate in the camp?", "Elementary school children from first grade to sixth grade"], ["2. List five activities", "Making traditional crafts; making traditional bowls; a hanok-living experience; a traditional music performance; learning tea-drinking etiquette"], ["3. Where is the village located?", "Pungnam-dong, Wansan-gu, Jeonju"]])]),
        card("Activities left out", "The presentation steps of Topic C (SMART Board) and Follow-up 1 (listening to two conversations in which a man who visited a hanok village in Pildong and Angukdong talks about the village location, who accompanied him and his activities) are audio and computer activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_C_TXT + _CAMP + _HAN, k=3)
        + [M("Where is the hanok village Jinsoo visited?", "Pungnam-dong, Wansan-gu, Jeonju", ["Seoul", "Busan", "Jeju"], "전주시 완산구 풍남동."), M("How did Jinsoo and his friends find the village?", "Looking at a rough map", ["With a guide", "By taxi", "By asking"], "약도를 보고."), M("How many hanok are in the village?", "More than 800", ["About 80", "About 8", "About 8,000"], "팔백여 채."), M("What were the crafts made of?", "Paper", ["Wood", "Stone", "Clay"], "종이로 만든 공예품."), M("What was the lodging like?", "The biggest house in the village", ["The smallest house", "A hotel", "A tent"], "가장 큰 집."), M("What was fun about the bathroom?", "It was separate, in the back yard", ["It was gold", "It was inside", "It had no door"], "뒷마당에 따로 있는 것."), M("What is the roof of a hanok made of?", "Clay tiles (기와)", ["Straw only", "Glass", "Metal"], "기와지붕."), M("Who lives in the 안채?", "Women", ["Men and guests", "Children only", "Servants only"], "여자가 사는 곳."), M("Who can attend the summer camp?", "Elementary school children, grades 1–6", ["Adults", "Middle schoolers", "Only foreigners"], "초등학교 일 학년부터 육 학년까지."), M("What should campers bring?", "Toiletries", ["A tent", "Bowls", "Food"], "세면도구."),
           F("한옥마을은 전주시 완산구 풍남동에 ___하고 있다. (be located)", "위치", ["숙소", "약도"], "위치하다."), F("우리가 ___ 숙소는 가장 큰 집이었다. (stayed)", "묵은", ["간", "둘러본"], "묵다."), F("한옥마을을 다 ___ 숙소로 갔다. (looked around)", "둘러보고", ["찾아가고", "마시고"], "둘러보다."), F("전통가옥이 팔백여 ___나 모여 있다. (counter for houses)", "채", ["벌", "개"], "채."), F("밤에는 온돌방에서 ___을 펴고 잤다. (blanket)", "이불", ["베개", "종이"], "이불."),
           read_q("한옥마을에 다녀왔습니다"), read_q("약도를 보고 찾아갔습니다"), read_q("전통찻집에 가서 전통차를 마셨습니다"), read_q("한옥의 지붕은 기와지붕입니다"), read_q("밤에는 온돌방에서 이불을 펴고 잤습니다")]
    ),
)

# ================================================================== L10 Grammar C: transitive verbs with causative infixes
_CAU1 = [("먼저 물을 끓이세요.", "Please boil the water first. / “Please cause the water to boil.”"), ("물을 식히세요.", "Please cool the water. / “Please cause the water to cool down.”")]
_CAUT = [("끓이다", "to boil (something)", "끓다", "to boil (as in “Water boils.”)"), ("녹이다", "to thaw (something)", "녹다", "to thaw (as in “The ice has thawed.”)"), ("익히다", "to cook (something); to ripen", "익다", "to be cooked, to cook"), ("덥히다", "to warm (something); to heat (something)", "덥다", "to be warm"), ("식히다", "to cool (something)", "식다", "to cool (as in “The water cooled off.”)"), ("얼리다", "to freeze (something)", "얼다", "to be frozen")]
_CAUO = [("절이다", "to pickle vegetables, etc."), ("튀기다", "to fry"), ("데우다", "to warm food"), ("졸이다", "to boil down"), ("말리다", "to dry")]
_CAUS = [("찌개를 끓입니다.", "I boil the stew."), ("생선을 익힙니다.", "I cook the fish."), ("얼음을 녹입니다.", "I thaw the ice."), ("국을 데웁니다.", "I warm the soup."), ("차를 식힙니다.", "I cool the tea."), ("물을 얼립니다.", "I freeze the water."), ("배추를 절입니다.", "I pickle the napa cabbage."), ("감자를 튀깁니다.", "I deep fry the potatoes."), ("콩을 졸입니다.", "I boil down the beans."), ("오이를 절입니다.", "I pickle cucumbers in salt.")]
L10 = lesson(
    "Ch 41 · Grammar C: more transitive verbs with causative infixes (끓이다 · 녹이다 · 익히다)",
    "끓이다 · 녹이다 · 익히다 · 덥히다 · 식히다 · 얼리다 · 절이다 · 튀기다 · 데우다 · 졸이다 · 말리다",
    requires=[],
    cards=[
        card("Recall the causative infixes",
             "In Chapter 30, you learned that the Korean causative infixes 이, 히, 기, 리, 우, 구, and 추, when added to native Korean verbs (먹다, 입다, etc.), turn the verbs into causative verbs, as in 먹이다 (to feed; to cause someone to eat) and 입히다 (to cause someone to wear/put on). In cooking-related contexts, you will often encounter native verbs with these causative infixes. In these instances, the verbs function as transitive verbs. For example (the English is the book’s):",
             examples=passage(_CAU1)),
        card("Transitive and intransitive pairs",
             "Note that 끓이다 and 식히다 from the intransitive verbs 끓다 and 식다 respectively function as transitive verbs. The following table lists some of these transitive verbs you will encounter in cooking-related contexts (the book’s table).",
             tables=[table(["Transitive verb", "Meaning", "Intransitive/stative verb", "Meaning"], [[a, b, c, d] for a, b, c, d in _CAUT], say=[0, 2])]),
        card("Other transitive verbs", "Other transitive verbs include the following:", tables=[ktable(_CAUO)]),
        card("Follow-up 1 (Listening and speaking): short sentences",
             "Using the words in the table, make short sentences with a noun (object) and a verb; say your sentence aloud; your partner translates it into English. Objects: 찌개, 생선, 고기, 국, 물, 배추, 밥, 감자, 얼음, 차, 야채, 오이, 콩. Verbs: 끓이다, 녹이다, 익히다, 덥히다, 식히다, 얼리다, 절이다, 튀기다, 데우다, 졸이다, 재우다 (the book gives no meaning for 재우다: “to put to sleep”, in cooking “to let meat marinate”; my gloss). The book’s model is 오이를 절입니다 (I pickle cucumbers in salt). My sample sentences (the English is mine; word combinations may vary):",
             examples=passage(_CAUS)),
        card("Activities left out", "Follow-up 2 (listening to Jinhee’s mother’s instructions on how to prepare dinner and writing the causative verb for fish, beef, potatoes, rice and miso soup, with the first one, 녹이다 [to thaw], done for you) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_CAU1 + _CAUS + [(a, b) for a, b, c, d in _CAUT] + [(c, d) for a, b, c, d in _CAUT] + _CAUO, k=3)
        + [M("What kind of verbs do the causative infixes make in cooking contexts?", "Transitive verbs", ["Intransitive verbs", "Adjectives", "Nouns"], "The book’s note."), M("What is the intransitive verb of 식히다?", "식다", ["식이다", "식하다", "식리다"], "The book’s table."), M("What is the transitive verb of 얼다?", "얼리다", ["얼히다", "얼이다", "얼우다"], "The book’s table."), M("What does 익히다 mean?", "to cook (something); to ripen", ["to be cooked", "to cool", "to freeze"], "The book’s table."), M("What does 덥히다 mean?", "to warm (something)", ["to be warm", "to cool", "to dry"], "The book’s table."), M("What does 데우다 mean?", "to warm food", ["to dry", "to boil down", "to pickle"], "The book’s list."), M("What does 졸이다 mean?", "to boil down", ["to warm food", "to dry", "to fry"], "The book’s list."), M("What does 말리다 mean (in this list)?", "to dry", ["to boil down", "to warm food", "to pickle"], "The book’s list."),
           F("먼저 물을 ___. (Please boil)", "끓이세요", ["끓으세요", "익으세요"], "끓이다."), F("물을 ___. (Please cool)", "식히세요", ["식으세요", "덥히세요"], "식히다."), F("얼음이 ___. (has thawed)", "녹았습니다", ["녹였습니다", "녹이세요"], "녹다."), F("고기를 푹 ___ 먹어야 합니다. (cook)", "익혀서", ["익어서", "익고"], "익히다."), F("배추를 소금에 ___. (pickle)", "절입니다", ["절습니다", "졸입니다"], "절이다."),
           read_q("끓이다"), read_q("녹이다"), read_q("익히다"), read_q("식히다"), read_q("얼리다")]
    ),
)

# ================================================================== L11 Grammar D: superlative scope
_SU1 = [("러시아가 가장 큰 나라예요.", "Russia is the largest country."), ("최 병장이 제일 빨리 말해요.", "Sgt. Choi speaks the fastest.")]
_SU2 = [("제가 우리 학교에서 성적이 제일 좋아요.", "I have the highest GPA in my school."), ("제가 학생 중에서 가장 빨리 달려요.", "Of (all) the students, I run the fastest.")]
_SU3 = [("우리 식구 중에서 제 남동생이 제일 커요.", "My younger brother is the tallest of (all) my family members."), ("언어 가운데서 한국말이 제일 어려워요.", "Of (all) the languages, Korean is the most difficult."), ("이 식당에서 불고기가 제일 비싸요.", "Bulgogi is the most expensive (food) at this restaurant."), ("우리 반에서 이 병장이 노래를 제일 잘해요.", "SFC Lee is the best singer in our class.")]
_SU4 = [("에베레스트 산이 높다", "산 중에서 에베레스트 산이 제일 높아요.", "세계에서 에베레스트 산이 제일 높아요.", "Of mountains, Mount Everest is the highest. / In the world, Mount Everest is the highest.")]
_SU5 = [("가족이 어떻게 되세요?", "How many are in your family?"), ("어머니, 아버지, 저 셋입니다.", "My mother, my father and I, three."), ("가족에 대해서 얘기해 주세요.", "Please tell me about your family."), ("네. 저희 어머니는 식구 중에서 가장 노래를 잘 부르세요. 어머니 직장에서도 노래를 제일 잘 부르세요. 저희 아버지는 취미로 자동차 수리와 낚시, 음악감상을 하십니다. 그중에서 차 수리하는 것을 제일 좋아하세요. 저는 사진 찍기를 좋아해요. 제 친구들 중에서 사진을 제일 잘 찍어요.", "Yes. My mother sings the best of the family. She sings the best at her workplace too. My father does car repair, fishing and listening to music as hobbies. Among them he likes repairing cars the most. I like taking photos. Among my friends, I take photos the best.")]
_SUM = [("우리 가족 중에서 할머니가 제일 부지런하세요.", "Of my family, my grandmother is the most diligent."), ("우리 회사에서 김 과장님이 제일 일찍 오십니다.", "In our company, Section Chief Kim comes the earliest."), ("과일 중에서 저는 딸기를 제일 좋아해요.", "Of fruits, I like strawberries the most."), ("우리 반에서 제 친구가 한국어를 제일 잘해요.", "In our class, my friend speaks Korean the best.")]
L11 = lesson(
    "Ch 41 · Grammar D: the scope of comparisons in the superlative, ~ 중에서/가운데서 and ~에서",
    "가장 · 제일 · ~ 중에서 · ~ 가운데서 · ~에서 · 우리 반에서 · 식구 중에서 · 가족에 대한 이야기",
    requires=[],
    cards=[
        card("Recall the superlative",
             "Recall the superlative in which the adjective (or stative verb) or adverb is preceded by 가장 or 제일. For example (the English is the book’s):",
             examples=passage(_SU1)),
        card("The scope of comparisons",
             "Note that 제일 is more frequently used than 가장, especially in spoken language. Because the superlative is used for comparing more than two things or people, we often express the scope of comparisons using one of the following two phrases: (1) ~에서, as in 직장에서 (in my workplace) and 뉴욕에서 (in New York); (2) ~ 중에서/가운데서, as in 한국인 중에서 (among Koreans) and 책 가운데서 (among books). For example (the English is the book’s):",
             examples=passage(_SU2)),
        card("Which one follows what",
             "Note that ~에서 is preceded by a place and ~ 중에서/가운데서 is preceded by things or people. More examples (the English is the book’s):",
             examples=passage(_SU3)),
        card("Follow-up 3 (Listening, reading and speaking): the model",
             "On the teacher’s cue, Partner A reads a sentence aloud to Partner B (e.g. 에베레스트 산이 높다). Then Partner B makes it a superlative sentence, using ~ 중에서/가운데서. Partner A repeats the superlative sentence, this time using the ~에서 phrase. The book’s model (the English is mine):",
             examples=dlg([("A", _SU4[0][0], "Mount Everest is high."), ("B", _SU4[0][1], "Of mountains, Mount Everest is the highest."), ("A", _SU4[0][2], "In the world, Mount Everest is the highest.")])),
        card("Follow-up 5 (Listening and speaking): talk about your family",
             "Think about three family members who are good at something; ask about each other’s family members and discuss what each is good at in comparison with the others, using ~ 중에서/가운데에서/에서 with 가장/제일. The book’s model (the English is mine):",
             examples=dlg([("A", _SU5[0][0], _SU5[0][1]), ("B", _SU5[1][0], _SU5[1][1]), ("A", _SU5[2][0], _SU5[2][1]), ("B", _SU5[3][0], _SU5[3][1])])),
        card("More sentences (mine)", "Sample sentences of my own (the English is mine):", examples=passage(_SUM)),
        card("Activities left out", "Follow-up 4 (listening to a high school student who uses a superlative to describe each of his five family members, and writing the superlative phrase and its scope in English; the first one is: grandfather, likes golf the most, among sports) is an audio activity."),
    ],
    exercises=uniq(
        _tr(_SU1 + _SU2 + _SU3 + _SUM + [(b, d) for a, b, c, d in _SU4] + [(_SU5[3][0], _SU5[3][1])], k=3)
        + [M("Which is used more in speech, 가장 or 제일?", "제일", ["가장", "Both equally", "Neither"], "The book’s note."), M("What does ~에서 follow in a superlative?", "A place", ["A person", "A number", "A verb"], "The book’s note."), M("What does ~ 중에서/가운데서 follow?", "Things or people", ["A place only", "A time", "A verb"], "The book’s note."), M("What does 한국인 중에서 mean?", "Among Koreans", ["In Korea", "From Koreans", "To Koreans"], "The book’s note."), M("What does 언어 가운데서 한국말이 제일 어려워요 mean?", "Of all the languages, Korean is the most difficult", ["Korean is easy", "Korean is the oldest", "Languages are difficult"], "The book’s example."), M("What does 제가 학생 중에서 가장 빨리 달려요 mean?", "Of all the students, I run the fastest", ["I run slowly", "Students run fast", "I am a student who runs"], "The book’s example."),
           F("제가 우리 학교___ 성적이 제일 좋아요. (in)", "에서", ["중에서", "에게"], "학교 = place."), F("제가 학생 ___ 가장 빨리 달려요. (among)", "중에서", ["에서", "에게"], "학생 = people."), F("언어 ___ 한국말이 제일 어려워요. (among)", "가운데서", ["에서", "에게"], "언어 = things."), F("이 식당에서 불고기가 ___ 비싸요. (most)", "제일", ["조금", "아주 조금"], "제일."), F("우리 반에서 이 병장이 노래를 제일 ___. (sings well)", "잘해요", ["못해요", "해요"], "잘하다."),
           read_q("러시아가 가장 큰 나라예요"), read_q("제가 학생 중에서 가장 빨리 달려요"), read_q("언어 가운데서 한국말이 제일 어려워요"), read_q("이 식당에서 불고기가 제일 비싸요"), read_q("우리 식구 중에서 제 남동생이 제일 커요")]
    ),
)

# ================================================================== L12 Activities C + self-evaluation
L12 = lesson(
    "Ch 41 · Activities C: Jeonju village tour and choosing a house · and self-evaluation",
    "전통 마을 · 공예관 · 전통찻집 · 어느 집에서 살고 싶습니까 · 자기 평가",
    requires=[],
    cards=[
        card("Activity 1: making sentences with two new words",
             "The book asks you to get a card with two words from the teacher, make a sentence with them at the bottom of the card and have it checked (the model: 전통찻집, 차); then to read your sentence aloud to a partner until the partner translates it correctly, and to repeat with other students. A sample sentence of my own for the model (the English is mine):",
             examples=passage([("전통찻집에서 전통차를 마셨어요.", "I drank traditional tea at a traditional teahouse.")])),
        card("Activity 2: a tour of a traditional village in Jeonju", "Myung-su and a friend toured a traditional village in Jeonju last week. The book asks you to listen to his narration, number the order of the sites (Handicraft Gallery, Traditional Liquor Museum, Traditional Paper Museum, Traditional Teahouse, Restaurant [3]) and write what they did at each place. This is an audio activity and is left out."),
        card("Activity 3: Which house would you like to live in?", "With a partner, compare two houses in Seoul and decide which you would like to live in: two groups each receive a description of a Korean house (House A or House B; information to fill in: house type, when built/repaired, location; number of rooms, specific features; positive aspects; negative aspects), listen to the missing information, exchange information in Korean with a student from the other group, choose a house, and present the reasons in Korean. The descriptions and audio are not in the printed text I have, so this activity is left out."),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with.\n\n"
             "Now I am able to: identify and extract information about traditional and modern clothing in Korea, and describe a person’s outfit; discuss food-related culture in Korea, including making kimchi; talk about basic cooking methods; and identify traditional and modern Korean houses, and compare them.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; ~을/를 포함해(서) (including); ~와/과 달리 or ~하고 달리 (unlike); transitive verbs with a causative infix; ~ 중에서/가운데서 (among) and ~에서 (at; on; in) in the superlative form; and the Sino-Korean syllables within 서양 (西洋), 음식 (飮食), and 한옥 (韓屋)."),
    ],
    exercises=uniq(
        _tr([("전통찻집에서 전통차를 마셨어요.", "I drank traditional tea at a traditional teahouse.")] + [("한옥마을에서 공예품을 구경했어요.", "I looked at crafts at the hanok village."), ("한복을 입고 사진을 찍었어요.", "I wore hanbok and took photos."), ("김장을 하려고 배추를 샀어요.", "I bought napa cabbage to make gimjang."), ("불고기를 만들려고 소고기를 썰었어요.", "I sliced beef to make bulgogi.")], k=3)
        + [M("What does 전통찻집 mean?", "A traditional teahouse", ["A tea garden", "A palace", "A museum"], "Activity 1."), M("In the model, what are the two words?", "전통찻집 and 차", ["한복 and 차", "한옥 and 방", "김치 and 밥"], "The book’s model."), M("What should you do if you tick “No” in the self-evaluation?", "Review on your own, study with a partner, tell your advisor or team leader", ["Skip it", "Retake the course", "Nothing"], "The book’s advice."),
           F("전통찻집에서 전통___를 마셨어요. (tea)", "차", ["밥", "술"], "전통차."), F("한복을 입고 ___을 찍었어요. (photo)", "사진", ["그림", "종이"], "사진."), F("김장을 하려고 ___를 샀어요. (napa cabbage)", "배추", ["마늘", "고추"], "배추."), F("불고기를 만들려고 소고기를 ___. (sliced)", "썰었어요", ["삶았어요", "끓였어요"], "썰다."), F("한옥마을에서 ___을 구경했어요. (craftwork)", "공예품", ["세면도구", "약도"], "공예품."),
           read_q("전통찻집에서 전통차를 마셨어요"), read_q("한옥마을에서 공예품을 구경했어요"), read_q("김장을 하려고 배추를 샀어요"), read_q("불고기를 만들려고 소고기를 썰었어요"), read_q("한복을 입고 사진을 찍었어요")]
    ),
)

# ================================================================== L13 core vocabulary
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammar features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-/") and " " not in r[0]]


def _vtabs(rows):
    sp = [r for r in rows if _HG(r[0]) and "-" not in r[0] and "~" not in r[0] and "(" not in r[0] and "/" not in r[0] and " " not in r[0] and "," not in r[0] and "…" not in r[0]]
    ns = [r for r in rows if r not in sp]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L13 = lesson(
    "Ch 41 · Core vocabulary",
    "주요 단어 · 한복 · 김장 · 한옥 · 요리 · 포함해서 · 달리",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. The book’s related words (synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank. 스타일 and 캐주얼 are listed also as loan words; the last section lists the Sino-Korean related words of 서양, 음식 and 한옥 as the book gives them.\n\n"
             "The example sentences with digits are respelled in Hangul (물 8컵 → 물 여덟 컵; 11월 → 십일월; 200여 명 → 이백여 명; 50채 → 오십 채)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 김장 mean?", "making kimchi for the winter", ["a kind of soup", "a gate", "a pillow"], "김장."), M("What does 한옥 mean?", "a traditional Korean-style house", ["Western house", "an apartment", "a palace"], "韓屋."), M("What does 저고리 mean?", "an upper garment of traditional Korean clothes", ["trousers", "a skirt", "a coat"], "저고리."), M("What does 이웃 mean?", "a neighbor; the neighborhood", ["a relative", "a teacher", "a guest"], "이웃."), M("What does 기와 mean?", "roof tiles used for a traditional Korean house", ["a paper", "a gate", "a bowl"], "기와."), M("What does ~ 채 count?", "buildings", ["clothes", "people", "books"], "~ 채."), M("What does ~ 벌 count?", "clothes", ["buildings", "people", "cars"], "~ 벌."), M("What does 푹 mean?", "thoroughly; entirely", ["slightly", "quickly", "newly"], "푹."),
           F("김치를 담글 때 필요한 ___가 뭐예요? (ingredient)", "재료", ["그릇", "종이"], "재료."), F("한복을 입은 ___이 아주 예뻐요. (appearance)", "모습", ["영향", "문화"], "모습."), F("약도를 보면 쉽게 그 건물을 찾을 수 있어요. 약도는 ___ 지도입니다. (rough)", "간단한", ["큰", "비싼"], "略圖."), F("한옥의 지붕은 ___입니다. (roof tiles)", "기와", ["종이", "그릇"], "기와."), F("김밥을 만들 때 필요한 ___를 사야 해요. (ingredients)", "재료", ["베개", "대문"], "재료."),
           read_q("주요 단어"), read_q("김장"), read_q("한옥"), read_q("재료"), read_q("저고리")]
    ),
)

UNIT = unit("Semester 2 · Unit 11 · Chapter 41: Korean Culture I (한국의 문화 1)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13])
