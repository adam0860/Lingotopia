"""Unit 14: KBC Semester 1, Unit 2, Chapter 7 - Downtown Monterey (몬트레이 시내에서).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 2, Student's Edition.
Audio, video clips, pictures, advertisements, maps, SMART Board activities, games, role-plays, partner and class
activities are left out. The book gives no English for its dialogs and leaves the answers to its exercises blank:
every translation of a dialog or example sentence and every answer key is mine; the vocabulary meanings are the book's."""
from ko_kbc import *

import re as _re


def _clean(en):
    return _re.sub(r"[;.] ?“[^”]*”\.?", "", en).rstrip(".")


def _tr(pairs, correct=None, k=3):
    """'What does X mean?' items taken from (Korean, English) pairs"""
    out = []
    for a, b in pairs:
        out.append(M(f"What does {a} mean?", b, [x for _, x in pairs if x != b][:k], f"{a} means “{b}”."))
    return out


# ================================================================== Topic A
_A_PASSAGE = [
    ("저는 몬트레이 시내에 자주 갑니다.", "I often go downtown to Monterey."),
    ("시내에는 가게가 많습니다.", "There are many stores downtown."),
    ("식당, 서점, 제과점, 약국, 은행 등이 있습니다.", "There are restaurants, bookstores, bakeries, pharmacies, banks and so on."),
    ("국방외국어 대학에서 몬트레이 시내까지 차로 오 분쯤 걸립니다.", "It takes about five minutes by car from the Defense Language Institute to downtown Monterey."),
    ("보통 토요일에는 은행에 갑니다.", "I usually go to the bank on Saturdays."),
    ("은행에서 돈을 찾습니다.", "I withdraw money at the bank."),
    ("그리고 친구들과 식당에서 저녁을 먹습니다.", "And I eat dinner with my friends at a restaurant."),
    ("일요일에는 델몬티 쇼핑센터에서 한국인 친구를 만납니다.", "On Sundays I meet a Korean friend at the Del Monte shopping center."),
    ("친구와 함께 옷가게에 가서 옷을 구경하고 영화관에서 영화를 봅니다.", "Together with my friend I go to a clothing store, look at clothes, and watch a movie at the movie theater."),
    ("영화를 본 후 커피숍에서 친구와 한국말로 얘기합니다.", "After watching the movie I chat with my friend in Korean at a coffee shop."),
]
_A_PAIRS = [
    ("가게", "a store; a shop"), ("걸리다", "to take (time)"), ("기름", "oil; gasoline"), ("꽃집", "a flower shop; “flower house”"), ("넣다", "to insert; to put in"), ("돈", "money"), ("등", "and so on; et cetera"),
    ("맡기다", "to entrust; to deposit"), ("물건", "a thing; stuff; goods"), ("백화점", "a department store"), ("사다", "to buy; to purchase"), ("생일", "a birthday"), ("생신", "a birthday (honorific)"),
    ("서점", "a bookstore"), ("세탁소", "a dry cleaner; a laundromat; “cleaning place”"), ("쇼핑센터", "a shopping center"), ("시내", "downtown; “in(side) city”"), ("약", "medicine; drug; medication"),
    ("약국", "a pharmacy; a drug store"), ("영화관", "a movie theater"), ("은행", "a bank"), ("이야기", "a chat; a talk; a story"), ("얘기", "a chat; a talk; a story (contraction of 이야기)"),
    ("이야기하다", "to have a chat; to have a talk"), ("제과점", "a bakery"), ("빵집", "a bakery; “bread house”"), ("주유소", "a gas station; “fueling place”"), ("찾다", "to withdraw (money); “to find”"), ("커피숍", "a coffee shop; a cafe"),
]
_SINO_SO = [("주유소", "a gas station; “fueling place”"), ("세탁소", "the cleaners; “cleaning place”"), ("이발소", "a barbershop; “haircut place”"), ("휴게소", "a rest area; a service area; “rest place”")]
_SINO_JEOM = [("점원", "a store clerk"), ("제과점", "a bakery; “confectionary shop”"), ("서점", "a bookstore"), ("백화점", "a department store; “store with hundred goods”"), ("주점", "a bar; a saloon; “liquor store”"), ("식품점", "a grocery store; “food store”")]
_ACT1 = [("은행", "c", "이곳에서 돈을 찾습니다.", "You withdraw money here."), ("서점", "f", "이곳에서 책을 삽니다.", "You buy books here."), ("슈퍼마켓", "e", "이곳에서 음료수와 음식을 삽니다.", "You buy drinks and food here."),
         ("제과점", "g", "빵과 커피를 삽니다.", "You buy bread and coffee."), ("주유소", "d", "자동차에 기름을 넣고 타이어에 바람을 넣습니다.", "You put gasoline in the car and air in the tires."),
         ("호텔", "a", "여행 가서 잠을 자고 쉽니다.", "You go on a trip and sleep and rest."), ("약국", "h", "약이 필요한 사람들이 갑니다.", "People who need medicine go."), ("세탁소", "b", "드라이 크리닝 옷을 맡깁니다.", "You leave dry-cleaning clothes.")]
_SITU = [("돈을 찾습니다.", "은행", "I withdraw money."), ("어머니 생신입니다. 꽃을 삽니다.", "꽃집", "It is my mother’s birthday. I buy flowers."), ("친구와 커피를 마십니다.", "커피숍", "I drink coffee with a friend."),
         ("배가 고픕니다. 밥을 먹습니다.", "식당", "I am hungry. I eat a meal."), ("한국어 책을 삽니다.", "서점", "I buy a Korean book.")]
_MAP = [("커피숍이 어디 있어요?", "Where is the coffee shop?"), ("커피숍은 영화관 건너편에 있어요.", "The coffee shop is across from the movie theater."),
        ("저는 이번 토요일 아침에 커피숍에서 커피를 마시고 영화관에 가서 영화를 보고 싶어요.", "This Saturday morning I want to drink coffee at the coffee shop and go to the movie theater and watch a movie."),
        ("그리고 요즘 날씨가 추워서 옷 가게에서 겨울 옷을 사고 싶어요.", "And because the weather is cold these days, I want to buy winter clothes at a clothing store."),
        ("저는 아파트 근처 제과점에서 아침에 빵을 삽니다.", "I buy bread in the morning at the bakery near my apartment."), ("주말에는 백화점에서 옷을 구경합니다.", "On weekends I look at clothes at the department store.")]
L1 = lesson(
    "Ch 7 · Topic A: Businesses around town",
    "저는 몬트레이 시내에 자주 갑니다 · 가게 · 은행 · 제과점 · 약국 · 소 (所) · 점 (店)",
    requires=[],
    cards=[
        card("What Chapter 7 teaches (몬트레이 시내에서)",
             "Chapter 7, “Downtown Monterey”, has three topic presentations, four grammar points, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: list and discuss businesses around town; order food and drink at a restaurant; and ask for services at a hair salon or barber shop.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the negating adverbs 안 and 못; the conjunctive ending -아/어서 for cause and effect (and thus; because); the auxiliary verb -아/어 주다 used to express “the sense of providing service”; -(으)ㄹ까요? (Shall we …?); and the Sino-Korean syllables 소 (所), 음 (飮) and 점 (店)."),
        card("Strategy: construct a phrase or sentence from related words",
             "If you learn words in context, you are more likely to retain them longer and recognize them better. When you work on a set of new words, first group related words and then construct a phrase or sentence that uses them. For example, with the four new words 돈 (money), 기름 (gasoline), 찾다 (to withdraw) and 넣다 (to put in), group 돈 with 찾다 and 기름 with 넣다, and then build a phrase with each pair.",
             examples=[D("(은행에서) 돈을 찾다", "to withdraw money (at the bank)"), D("(주유소에서) 기름을 넣다", "to put in gasoline (at the gas station)")]),
        card("Reading: I often go downtown to Monterey",
             "In class, SPC Derstine is giving a presentation about his weekend activities. (The English is mine; the book writes 5분쯤, which is spelled out here.)",
             examples=passage(_A_PASSAGE)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s. The book lists 제과점/빵집, 생일/생신 and 이야기/얘기(하다) as pairs; they are split here.",
             tables=[ktable(_A_PAIRS)]),
        card("Sino-Korean in use: 소 (所)",
             "This Sino-Korean syllable has quite a few meanings, but it normally means a place or an office when it comes at the end of a noun.",
             tables=[ktable(_SINO_SO)]),
        card("Sino-Korean in use: 점 (店)",
             "This Sino-Korean syllable means a shop or store.",
             tables=[ktable(_SINO_JEOM)]),
        card("Activity 1: match each business with its description",
             "The book asks you to match the eight businesses with the descriptions a–h. The letters are my key (the English is mine; 필요한 is not in the core list).",
             tables=[table(["Business", "Letter", "Description", "Meaning"], [[b, l, d, e] for b, l, d, e in _ACT1], say=[0, 2])]),
        card("Follow-up 2: which business?",
             "The book prints advertisements and asks you to write the name of the business for each situation. The advertisements are pictures and are left out; the answers are my key.",
             tables=[table(["Situation", "Business", "Meaning"], [list(r) for r in _SITU], say=[0, 1])]),
        card("Activity 3 and the Monopoly game: models",
             "The book’s models for the Monopoly game and for asking where a store is (the maps are not reproduced). The English is mine; 근처 (near), 건너편 (across from) and 요즘 (these days) are not in the core list.",
             tables=[sent_table(_MAP)]),
        card("Activities left out",
             "The vocabulary slide show, the SMART Board activities, the Monopoly game, Follow-up 1 (listening to four conversations to name the business), the advertisements of Follow-up 2, Activity 2 (family errand notes and two voice mails), the pair map task and the hometown-downtown presentation of Activity 4 are audio, picture, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _A_PAIRS])
        + [mean("가게", "a store; a shop", ["a department store", "a bookstore", "a bank"]), mean("시내", "downtown", ["a shopping center", "a village", "a market"]), mean("서점", "a bookstore", ["a bank", "a bakery", "a pharmacy"]),
           mean("백화점", "a department store", ["a bookstore", "a flower shop", "a shopping center"]), mean("쇼핑센터", "a shopping center", ["a department store", "a bank", "a pharmacy"]), mean("영화관", "a movie theater", ["a coffee shop", "a bank", "a bookstore"]),
           mean("은행", "a bank", ["a pharmacy", "a bakery", "a bookstore"]), mean("약국", "a pharmacy", ["a bank", "a bakery", "a bookstore"]), mean("제과점", "a bakery", ["a bank", "a pharmacy", "a flower shop"]), mean("빵집", "a bakery", ["a bank", "a pharmacy", "a flower shop"]),
           mean("돈", "money", ["gasoline", "medicine", "a thing"]), mean("기름", "oil; gasoline", ["money", "medicine", "a thing"]), mean("약", "medicine", ["money", "gasoline", "a thing"]), mean("물건", "a thing; goods", ["money", "medicine", "a store"]),
           mean("넣다", "to insert; to put in", ["to withdraw", "to buy", "to entrust"]), mean("찾다", "to withdraw (money); to find", ["to put in", "to buy", "to entrust"]), mean("사다", "to buy", ["to put in", "to withdraw", "to entrust"]), mean("맡기다", "to entrust; to deposit", ["to buy", "to withdraw", "to put in"]),
           mean("걸리다", "to take (time)", ["to buy", "to withdraw", "to put in"]), mean("등", "and so on; et cetera", ["and then", "also", "only"]), mean("이야기", "a chat; a talk; a story", ["a plan", "a thing", "a reason"]), mean("생일", "a birthday", ["a holiday", "a weekend", "a year"]),
           mean("생신", "a birthday (honorific)", ["a holiday", "a weekend", "a name"])]
        + _tr([(a, b) for a, b in _A_PASSAGE[:9]])
        + [M(f"What does {k} mean?", e, [x for _, x in _SINO_SO + _SINO_JEOM if x != e][:3], f"{k} = {e}.") for k, e in _SINO_SO + _SINO_JEOM]
        + [M("Which Sino-Korean syllable means a place or an office at the end of a noun?", "소 (所)", ["점 (店)", "음 (飮)", "관 (館)"], "주유소, 세탁소, 이발소, 휴게소."), M("Which Sino-Korean syllable means a shop or store?", "점 (店)", ["소 (所)", "음 (飮)", "원 (院)"], "제과점, 서점, 백화점."),
           M("Which word ends with 소 (a place)?", "주유소", ["제과점", "서점", "백화점"], "주유소 = fueling place."), M("Which word ends with 점 (a shop)?", "서점", ["주유소", "세탁소", "이발소"], "서점 = bookstore."),
           M("What is a 점원?", "a store clerk", ["a store owner", "a customer", "a bank clerk"], "점원 = store clerk.")]
        + [M(f"Which business matches “{e.rstrip('.')}”?", b, [x[0] for x in _ACT1 if x[0] != b][:3], f"{d} → {b}.") for b, l, d, e in _ACT1]
        + [M(f"Which letter matches {b}?", l, [x[1] for x in _ACT1 if x[1] != l][:3], f"{b} → {l}: {d}") for b, l, d, e in _ACT1]
        + [M(f"Where would you go if “{e.rstrip('.')}”?", b, [x[1] for x in _SITU if x[1] != b][:3], f"{s} → {b}.") for s, b, e in _SITU]
        + [M("What does SPC Derstine do at the bank?", "Withdraws money", ["Buys bread", "Buys books", "Buys medicine"], "은행에서 돈을 찾습니다."), M("How long does it take from DLI to downtown Monterey?", "About five minutes by car", ["About fifty minutes by car", "About five minutes on foot", "About an hour by bus"], "차로 오 분쯤 걸립니다."),
           M("Where does he meet a Korean friend on Sundays?", "At the Del Monte shopping center", ["At the bank", "At a coffee shop", "At school"], "델몬티 쇼핑센터에서 한국인 친구를 만납니다."), M("Where does he talk with his friend in Korean?", "At a coffee shop, after the movie", ["At the bank", "At the movie theater", "At a restaurant"], "영화를 본 후 커피숍에서 친구와 한국말로 얘기합니다."),
           F("(은행에서) 돈을 ___", "찾습니다", ["넣습니다", "삽니다"], "돈을 찾다 = to withdraw money."), F("(주유소에서) 기름을 ___", "넣습니다", ["찾습니다", "삽니다"], "기름을 넣다 = to put in gasoline."),
           F("시내에는 가게가 ___.", "많습니다", ["높습니다", "맑습니다"], "가게가 많다."), F("몬트레이 시내까지 차로 오 분쯤 ___.", "걸립니다", ["넣습니다", "찾습니다"], "시간이 걸리다."),
           M("What does 식당, 서점, 제과점, 약국, 은행 등 mean?", "restaurants, bookstores, bakeries, pharmacies, banks and so on", ["only restaurants", "restaurants and banks", "a bookstore"], "등 = and so on."), read_q("꽃집"), read_q("백화점"), read_q("쇼핑센터"), read_q("세탁소"), read_q("주유소"), read_q("약국"), read_q("제과점")]
    ),
)

# ================================================================== Topic B
_B_DIALOG = [
    ("종업원", "뭐 드시겠어요?", "What would you like to have?"),
    ("진영", "토마스 씨, 매운 음식 괜찮아요?", "Thomas, is spicy food okay for you?"),
    ("토마스", "저는 매운 음식은 못 먹어요. 김치도 매워서 못 먹어요.", "I can’t eat spicy food. I can’t eat kimchi either because it is spicy."),
    ("진영", "그래요? 그럼, 불고기하고 비빔밥 어때요?", "Is that so? Then how about bulgogi and bibimbap?"),
    ("토마스", "네, 좋아요. 우리 만두도 시킵시다. 오늘은 아주 배가 고파요.", "Yes, good. Let’s order dumplings too. I am very hungry today."),
    ("진영", "그래요. 여기 불고기 일 인분, 만두 일 인분, 비빔밥 하나 주세요.", "Okay. Please give us one serving of bulgogi, one serving of dumplings and one bibimbap."),
    ("종업원", "네, 알겠습니다. 음료수는 뭐 드시겠어요?", "Yes, understood. What would you like to drink?"),
    ("진영", "저는 콜라 한 잔 주세요.", "I would like a glass of cola, please."),
    ("토마스", "저는 맥주 한 병 주세요. 그리고 물도 좀 갖다 주세요.", "I would like a bottle of beer, please. And please bring some water too."),
    ("진영", "여기 계산서 좀 주세요. 신용카드 받습니까?", "(After finishing the meal) Please give us the bill. Do you accept credit cards?"),
    ("종업원", "네, 받습니다. 계산서 여기 있습니다.", "Yes, we do. Here is your bill."),
]
_B_PAIRS = [
    ("갖다 주다", "to bring; to take"), ("계산서", "a bill; a check; “calculation paper”"), ("김밥", "gimbap; “seaweed rice roll”"), ("김치", "kimchi"), ("김치찌개", "kimchi stew"), ("만두", "dumplings; pot stickers"),
    ("맛있다", "to be tasty; to be delicious; “taste exists”"), ("맥주", "beer"), ("맵다", "to be spicy; to be hot"), ("물", "water"), ("반찬", "a side dish"), ("받다", "to receive; to take"),
    ("배가 고프다", "to be hungry; “the stomach is hungry”"), ("병", "a counter for bottles"), ("불고기", "bulgogi; Korean-style barbecued beef"), ("비빔밥", "bibimbap; rice mixed with vegetables and meat; “mixed rice”"),
    ("사이다", "soft drinks; soda pop; “cider”"), ("신용카드", "a credit card"), ("아서", "and thus; so; because (-아서/어서)"), ("음료수", "beverages; drinks; “drinking water”"), ("음식", "food"), ("인분", "a serving; “person’s portion”"),
    ("잔", "a counter for a glass or cup"), ("주다", "to give; to offer"), ("드리다", "to give; to offer (honorific)"), ("시키다", "to order (food or drinks)"), ("주문하다", "to order (food or drinks)"), ("콜라", "cola; Coke"),
]
_FOODNAME = [("한국음식", "Korean food", "한식"), ("미국음식", "American food", "-"), ("서양음식", "Western food", "양식"), ("일본음식", "Japanese food", "일식")]
_SINO_EUM = [("음식", "food; “drinking and eating”"), ("음주", "drinking; “drinking liquor”"), ("음료수", "drinking water; beverages"), ("폭음", "binge drinking; “explosive drinking”")]
L2 = lesson(
    "Ch 7 · Topic B: Ordering at a Korean restaurant",
    "뭐 드시겠어요? · 불고기 · 비빔밥 · 만두 · 맥주 · 계산서 · 음 (飮)",
    requires=[],
    cards=[
        card("Dialog: what would you like to eat?",
             "At a Korean restaurant, PFC Thomas and his Korean friend Jinyeong are about to place an order. The book’s footnote: 뭐 드시겠어요? is a common expression used at a restaurant and means “What would you like to have?”; 뭐 is a contracted form of 무엇. (The English is mine.)",
             examples=dlg(_B_DIALOG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s. The book lists 김치(찌개), 배(가) 고프다, ~병, ~인분, ~잔 and 주다/드리다, and the ending -아/어서, which is explained in the grammar lessons; 시키다/주문하다 is split here.",
             tables=[ktable(_B_PAIRS)]),
        card("Naming the food of a country",
             "When referring to food from different countries or regions, add 음식 after a country or regional name, as in 한국음식, 미국음식, 서양음식 (Western food) and 일본음식. 한국음식 is usually abbreviated as 한식, 서양음식 as 양식, and 일본음식 as 일식.",
             tables=[table(["Food", "Meaning", "Abbreviation"], [list(r) for r in _FOODNAME], say=[0, 2])]),
        card("Cultural note: kimchi",
             "Kimchi is a traditional Korean fermented dish made of vegetables with a variety of seasonings. It is the most common side dish served with Korean meals. Although Koreans make kimchi from many vegetables, the Napa cabbage kimchi (배추 김치) is the most common type. Koreans make dishes like kimchi stew (김치찌개), kimchi fried rice (김치볶음밥) and even kimchi pizza (김치피자). Despite its spicy flavor, many foreigners in Korea develop a taste for kimchi and find themselves missing it after returning home. The dish is so essential to Koreans that “space kimchi” was developed by the Korea Aerospace Research Institute for the first Korean astronaut."),
        card("Sino-Korean in use: 음 (飮)",
             "This Sino-Korean syllable means drink or swallow.",
             tables=[ktable(_SINO_EUM)]),
        card("Counting drinks and dishes",
             "In the dialog the customers order with the counters 병 (bottles), 잔 (glasses and cups) and 인분 (servings). The native numbers 한, 두, 세, 네 go before 병 and 잔; the Sino-Korean numbers 일, 이, 삼, 사 go before 인분 (the book’s examples are 불고기 일 인분, 맥주 한 병, 콜라 한 잔, 맥주 두 병, 불고기 사 인분하고 맥주 세 병).",
             tables=[table(["Order", "Meaning"], [["맥주 한 병", "one bottle of beer"], ["맥주 두 병", "two bottles of beer"], ["물 한 잔", "one glass of water"], ["콜라 한 잔", "one glass of cola"], ["불고기 일 인분", "one serving of bulgogi"], ["만두 이 인분", "two servings of dumplings"], ["불고기 사 인분", "four servings of bulgogi"]], say=[0])]),
        card("Activities left out",
             "The word-search puzzle of Presentation Activity b (a grid of 20 food and restaurant words with their English meanings; the words are the ones in the core list above), the SMART Board activities, the three-person role-play of the dialog and Follow-up 1 (listening to three short conversations at a restaurant) are audio, game or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _B_PAIRS])
        + [mean("김치", "kimchi", ["gimbap", "bulgogi", "bibimbap"]), mean("김치찌개", "kimchi stew", ["kimchi", "gimbap", "dumplings"]), mean("김밥", "gimbap; a seaweed rice roll", ["kimchi", "bulgogi", "bibimbap"]), mean("불고기", "bulgogi; Korean barbecued beef", ["kimchi", "gimbap", "bibimbap"]),
           mean("비빔밥", "bibimbap; mixed rice", ["kimchi", "gimbap", "bulgogi"]), mean("만두", "dumplings; pot stickers", ["kimchi", "gimbap", "bulgogi"]), mean("음식", "food", ["a drink", "a bill", "a side dish"]), mean("음료수", "beverages; drinks", ["food", "a bill", "a side dish"]),
           mean("반찬", "a side dish", ["a drink", "a bill", "food"]), mean("계산서", "a bill; a check", ["a menu", "a side dish", "a credit card"]), mean("신용카드", "a credit card", ["a bill", "a menu", "cash"]), mean("맥주", "beer", ["water", "cola", "soda pop"]),
           mean("물", "water", ["beer", "cola", "soda pop"]), mean("콜라", "cola; Coke", ["beer", "water", "soda pop"]), mean("사이다", "soft drinks; soda pop", ["beer", "water", "cola"]), mean("맵다", "to be spicy; to be hot", ["to be tasty", "to be hungry", "to be cold"]),
           mean("맛있다", "to be tasty; to be delicious", ["to be spicy", "to be hungry", "to be cold"]), mean("배가 고프다", "to be hungry", ["to be spicy", "to be tasty", "to be full"]), mean("받다", "to receive; to take", ["to give", "to order", "to bring"]),
           mean("주다", "to give; to offer", ["to receive", "to order", "to bring"]), mean("드리다", "to give; to offer (honorific)", ["to receive", "to order", "to bring"]), mean("시키다", "to order (food or drinks)", ["to receive", "to give", "to bring"]),
           mean("주문하다", "to order (food or drinks)", ["to receive", "to give", "to bring"]), mean("갖다 주다", "to bring; to take", ["to receive", "to give", "to order"]),
           mean("병", "a counter for bottles", ["a counter for glasses", "a counter for servings", "a counter for people"]), mean("잔", "a counter for a glass or cup", ["a counter for bottles", "a counter for servings", "a counter for people"]),
           mean("인분", "a serving", ["a bottle", "a glass", "a person"])]
        + _tr([(a, b) for _, a, b in _B_DIALOG[:10]])
        + [M(f"Which counter goes with {n} ({e})?", c, [x for x in ("병", "잔", "인분") if x != c], f"{n} → {c}.") for n, e, c in [("맥주", "beer", "병"), ("콜라", "cola", "잔"), ("물", "water", "잔"), ("불고기", "bulgogi", "인분"), ("사이다", "soda", "병"), ("만두", "dumplings", "인분")]]
        + [M(f"How do you say “{e}”?", ko, w, f"{ko} = {e}.") for ko, e, w in [("맥주 한 병", "one bottle of beer", ["맥주 하나 병", "맥주 일 병", "맥주 한 잔"]), ("맥주 두 병", "two bottles of beer", ["맥주 둘 병", "맥주 이 병", "맥주 두 잔"]), ("물 한 잔", "one glass of water", ["물 하나 잔", "물 일 잔", "물 한 병"]),
                                                          ("불고기 일 인분", "one serving of bulgogi", ["불고기 한 인분", "불고기 하나 인분", "불고기 한 병"]), ("만두 이 인분", "two servings of dumplings", ["만두 두 인분", "만두 둘 인분", "만두 이 병"]), ("불고기 사 인분", "four servings of bulgogi", ["불고기 네 인분", "불고기 넷 인분", "불고기 사 병"])]]
        + [M(f"What does {a} mean?", b, [x for _, x, _ in _FOODNAME if x != b][:3], f"{a} = {b}.") for a, b, _ in _FOODNAME]
        + [M("What is the usual abbreviation of 한국음식?", "한식", ["양식", "일식", "중식"], "한국음식 = 한식."), M("What is the usual abbreviation of 서양음식?", "양식", ["한식", "일식", "중식"], "서양음식 = 양식."), M("What is the usual abbreviation of 일본음식?", "일식", ["한식", "양식", "중식"], "일본음식 = 일식."),
           M("What does the Sino-Korean syllable 음 (飮) mean?", "drink; swallow", ["a shop", "a place", "food"], "음식, 음주, 음료수, 폭음.")]
        + [M(f"What does {k} mean?", e, [x for _, x in _SINO_EUM if x != e][:3], f"{k} = {e}.") for k, e in _SINO_EUM]
        + [M("Why can’t Thomas eat kimchi?", "Because it is spicy", ["Because he is full", "Because it is expensive", "Because he dislikes vegetables"], "김치도 매워서 못 먹어요."), M("What does Jinyeong suggest ordering for Thomas?", "Bulgogi and bibimbap", ["Kimchi stew", "Gimbap", "Dumplings only"], "불고기하고 비빔밥 어때요?"),
           M("What does Thomas want to order too?", "Dumplings", ["Kimchi", "Gimbap", "Cola"], "우리 만두도 시킵시다."), M("What does Jinyeong order to drink?", "A glass of cola", ["A bottle of beer", "A glass of water", "A bottle of cider"], "저는 콜라 한 잔 주세요."),
           M("What does Thomas order to drink?", "A bottle of beer (and some water)", ["A glass of cola", "A glass of cider", "Nothing"], "저는 맥주 한 병 주세요. 그리고 물도 좀 갖다 주세요."), M("What does Jinyeong ask at the end of the meal?", "For the bill, and whether credit cards are accepted", ["For more water", "For the menu", "For a side dish"], "여기 계산서 좀 주세요. 신용카드 받습니까?"),
           F("저는 콜라 한 ___ 주세요. (a glass)", "잔", ["병", "인분"], "잔 = glass."), F("저는 맥주 한 ___ 주세요. (a bottle)", "병", ["잔", "인분"], "병 = bottle."), F("여기 불고기 일 ___ 주세요.", "인분", ["병", "잔"], "인분 = serving."),
           F("신용카드 ___? (Do you accept…)", "받습니까", ["줍니까", "봅니까"], "받다 = to accept."), F("여기 ___ 좀 주세요. (the bill)", "계산서", ["반찬", "음료수"], "계산서 = bill."), read_q("계산서"), read_q("신용카드"), read_q("음료수"), read_q("비빔밥"), read_q("김치찌개"), read_q("맛있다")]
    ),
)

# ================================================================== Topic B extras
_MENU = [("불고기", "7,000", "bulgogi (1 serving)"), ("비빔밥", "7,000", "bibimbap"), ("김밥", "5,000", "gimbap (1 serving)"), ("만두", "5,000", "dumplings (1 serving)"), ("김치찌개", "7,000", "kimchi stew"), ("생선찌개", "8,000", "fish stew"), ("두부찌개", "6,000", "tofu stew")]
_DRINK = [("콜라", "한 병", "2,000", "cola (1 bottle)"), ("사이다", "한 병", "2,000", "soda (1 bottle)"), ("맥주", "한 병", "5,000", "beer (1 bottle)"), ("커피", "한 잔", "2,000", "coffee (1 cup)"), ("오렌지주스", "한 잔", "3,000", "orange juice (1 glass)"), ("녹차", "한 잔", "2,000", "green tea (1 cup)")]
_DISH = [("비빔밥", "assorted vegetables on rice with spicy sauce"), ("불고기", "Korean barbecued beef"), ("갈비", "marinated barbecued beef ribs"), ("냉면", "cold buckwheat noodles"), ("삼계탕", "ginseng chicken soup"), ("순두부찌개", "soft tofu stew"),
         ("해물파전", "seafood and green-onion pancake"), ("잡채", "stir-fried glass noodles with vegetables"), ("김치", "kimchi"), ("김밥", "gimbap; a seaweed rice roll")]
_SURVEY = [("미국인", "Americans", "갈비, 불고기, 순두부찌개"), ("일본인", "Japanese", "해물파전"), ("중국인", "Chinese", "삼계탕")]
_ROLE_C = [("이 식당은 무슨 음식이 맛있어요?", "What food is good at this restaurant?"), ("만두 이 인분 주세요.", "Two servings of dumplings, please."), ("여기 계산서 좀 갖다 주세요.", "Please bring the bill here."), ("신용카드 받습니까?", "Do you accept credit cards?")]
_ROLE_S = [("뭐 드시겠어요?", "What would you like to have?"), ("뭐 주문하시겠어요?", "What would you like to order?"), ("음료수는 뭐 드릴까요?", "What would you like to drink?"), ("맛있게 드셨어요?", "Did you enjoy your meal?"), ("계산서 여기 있습니다.", "Here is your bill.")]
_BLIND = [("아니요. 저는 코미디 영화는 별로 안 좋아해요. 액션 영화가 더 재미있어서 주로 액션영화를 봐요.", "No. I don’t really like comedy movies. Action movies are more fun, so I mostly watch action movies."),
          ("이번 주말에 시간 있으세요? 같이 콘서트 갈까요?", "Do you have time this weekend? Shall we go to a concert together?"), ("죄송해요. 제가 이번 주에 숙제가 많아서 못 가요.", "I’m sorry. I have a lot of homework this week, so I can’t go.")]
L3 = lesson(
    "Ch 7 · Topic B extras: the menu, Korean dishes and the restaurant role-play",
    "한식 메뉴 · 음료수 · 한국 음식 · 손님 · 종업원",
    requires=[],
    cards=[
        card("Follow-up 2: a Korean restaurant menu",
             "The book prints the menu of a local Korean restaurant (prices in won). The dishes and prices are the book’s; the English is mine.",
             tables=[table(["Dish", "Price (won)", "Meaning"], [list(r) for r in _MENU], say=[0]),
                     table(["Drink", "Amount", "Price (won)", "Meaning"], [list(r) for r in _DRINK], say=[0, 1])]),
        card("Activity 2: Korean dishes many Koreans enjoy",
             "The book lists ten dishes and asks you to look them up on the web (Google images and Wikipedia). The book gives the English only for 갈비 and 비빔밥; the other meanings are mine.",
             tables=[ktable(_DISH)]),
        card("Reading: a survey of the favorite dishes of foreigners in Korea",
             "The article, in the book: “한국 음식 베스트 10: 외국인은 어떤 한국 음식을 좋아할까요? 한국 관광 공사가 외국인 1635명에게 질문했습니다. 외국인들은 비빔밥 (63.2%), 불고기 (57.8%), 갈비 (46.7%), 냉면 (39.5%), 삼계탕 (39.1%), 순두부찌개 (32.4%), 해물파전 (26.4%), 잡채 (25.4%), 김치 (25.3%), 김밥 (17.8%)을 좋아합니다.” The book glosses 한국 관광 공사 as the Korean Tourism Organization and 질문하다 as “to ask a question; to inquire”. "
             "The rest of the article is below (the English is mine); the book asks you to write the dishes each nationality likes.",
             examples=[D("중국인은 삼계탕을 좋아하고 일본인들은 해물파전을 잘 먹습니다.", "Chinese people like samgyetang and Japanese people eat haemul pajeon well."), D("그리고 미국인은 갈비, 불고기, 순두부찌개를 좋아합니다.", "And Americans like galbi, bulgogi and sundubu jjigae.")],
             tables=[table(["Nationality", "Meaning", "Dishes"], [list(r) for r in _SURVEY], say=[0, 2])]),
        card("Activity 3: role-play expressions at a restaurant in Seoul",
             "The book’s role-play gives these expressions for the customer (손님) and the server (종업원). The English is mine; 드릴까요, 드셨어요 and 주문하시겠어요 use honorific or humble forms that are not explained in this chapter.",
             tables=[sent_table(_ROLE_C, title="손님 (customer)"), sent_table(_ROLE_S, title="종업원 (server)")]),
        card("Follow-up 5 (Grammar B): models for talking about likes, dislikes and excuses",
             "The book’s blind-date and invitation models (별로 = not really, 주로 = mostly and 죄송해요 = I’m sorry are not in the core list). The English is mine.",
             examples=[D(a, b) for a, b in _BLIND]),
        card("Activities left out",
             "Follow-up 1 (matching the food and beverage ordered in three spoken conversations), the menu planning of Follow-up 2b, Activity 1 (listening to three restaurant conversations), the web research and the role-play on the cue cards are audio, web or class activities."),
    ],
    exercises=uniq(
        _tr([(k, e) for k, e in _DISH if k not in ("김치", "김밥")])
        + [M(f"What does {k} cost?", f"{p} won", [f"{x} won" for x in ("5,000", "6,000", "7,000", "8,000", "9,000") if x != p][:3], f"{k}: {p} won.") for k, p, e in _MENU[:7]]
        + [M("What is the price of one bottle of beer on the menu?", "5,000 won", ["2,000 won", "3,000 won", "7,000 won"], "맥주 한 병: 5,000 won."), M("What is the price of a cup of coffee on the menu?", "2,000 won", ["3,000 won", "5,000 won", "7,000 won"], "커피 한 잔: 2,000 won."),
           M("What is the price of orange juice on the menu?", "3,000 won", ["2,000 won", "5,000 won", "7,000 won"], "오렌지주스 한 잔: 3,000 won."), M("Which dish is the most expensive on the menu?", "생선찌개", ["불고기", "김밥", "두부찌개"], "생선찌개: 8,000 won."),
           M("Which dish is the cheapest on the menu?", "김밥 (and 만두)", ["불고기", "김치찌개", "생선찌개"], "김밥 and 만두: 5,000 won."), M("Which counter does the menu use for coffee and green tea?", "잔", ["병", "인분", "명"], "커피 한 잔, 녹차 한 잔."),
           M("Which counter does the menu use for cola and cider?", "병", ["잔", "인분", "명"], "콜라 한 병, 사이다 한 병.")]
        + [M(f"What does {a} mean?", b, [x for _, x in _DISH if x != b][:3], f"{a} = {b}.") for a, b in _DISH]
        + [M(f"What does {a} mean?", b, [x for _, x in _ROLE_C + _ROLE_S if x != b][:3], f"{a} means “{b}”.") for a, b in _ROLE_C + _ROLE_S]
        + [M(f"What does {a} mean?", b, [x for _, x in _BLIND if x != b][:3], f"{a} means “{b}”.") for a, b in _BLIND]
        + [M("Which nationality likes samgyetang (삼계탕), according to the article?", "Chinese", ["Americans", "Japanese", "Koreans"], "중국인은 삼계탕을 좋아하고…"), M("Which nationality eats haemul pajeon well?", "Japanese", ["Americans", "Chinese", "Koreans"], "일본인들은 해물파전을 잘 먹습니다."),
           M("Which nationality likes galbi, bulgogi and sundubu jjigae?", "Americans", ["Japanese", "Chinese", "Koreans"], "미국인은 갈비, 불고기, 순두부찌개를 좋아합니다."), M("Which dish came first in the survey?", "비빔밥", ["불고기", "갈비", "김밥"], "비빔밥 (63.2%) was first."),
           M("Which dish came last in the survey?", "김밥", ["김치", "잡채", "불고기"], "김밥 (17.8%) was last."), M("What is the Korean Tourism Organization in Korean?", "한국 관광 공사", ["한국 외국어", "국방 대학", "한국 식당"], "한국 관광 공사."),
           M("What does 질문하다 mean?", "to ask a question; to inquire", ["to answer", "to order", "to eat"], "질문하다 = to ask a question."),
           F("만두 이 ___ 주세요.", "인분", ["병", "잔"], "인분 = serving."), F("이 식당은 무슨 음식이 ___?", "맛있어요", ["매워요", "배고파요"], "맛있다 = to be tasty."), F("여기 계산서 좀 ___ 주세요.", "갖다", ["받아", "시켜"], "갖다 주다 = to bring."),
           read_q("해물파전"), read_q("순두부찌개"), read_q("삼계탕")]
    ),
)

# ================================================================== Topic C
_C_DIALOG = [
    ("미용사", "어서 오세요. 몇 시 예약이세요?", "Welcome. What time is your reservation?"),
    ("박진수", "네, 세 시 예약입니다.", "Yes, I have a three o’clock reservation."),
    ("미용사", "아, 네. 손님, 저쪽으로 갈까요?", "Oh, yes. Sir, shall we go over there?"),
    ("미용사", "머리 어떻게 해 드릴까요?", "(After taking him to the chair) How would you like your hair done?"),
    ("박진수", "짧게 자르고 싶습니다. 그런데 앞머리는 좀 길게 해 주세요.", "I want to cut it short. But please make the bangs a little long."),
    ("미용사", "염색도 하세요. 요즘 갈색이 유행이에요.", "Please dye it too. Brown is in fashion these days."),
    ("박진수", "아, 그래요? 염색은 얼마예요?", "Oh, is that so? How much is the dye?"),
    ("미용사", "염색은 팔십오 달러예요.", "The dye is eighty-five dollars."),
    ("박진수", "그럼 짙은 갈색으로 해 주세요.", "Then please do a dark brown."),
    ("미용사", "샴푸도 해 드릴까요?", "Shall I shampoo your hair too?"),
    ("박진수", "네, 해 주세요.", "Yes, please."),
    ("미용사", "어머, 머리 염색이 예뻐요. 손님한테 잘 어울려요.", "(Thirty minutes later) Oh my, the hair dye looks pretty. It suits you well."),
    ("박진수", "네, 마음에 들어요. 감사합니다.", "Yes, I like it. Thank you."),
]
_C_PAIRS = [
    ("갈색", "brown (color)"), ("게", "adverb “maker”"), ("그런데", "by the way; however; but; and"), ("길다", "to be long"), ("길게", "long (adverb of 길다)"), ("남자", "a man; a male"), ("마음에 들다", "to like or be pleased with something; “to enter one’s heart”"),
    ("머리", "the head; hair"), ("미용실", "beauty salon"), ("머리방", "beauty salon; “hair room”"), ("샴푸", "a shampoo"), ("샴푸하다", "to shampoo"), ("손님", "a customer; a client"), ("아/어 주다", "auxiliary verb used to express the sense of providing service"),
    ("어서 오세요", "Welcome. Come on in."), ("어울리다", "to suit; to go well with"), ("얼마예요", "How much ~?"), ("여자", "a woman; a female"), ("염색", "dyeing"), ("염색하다", "to dye"), ("예쁘다", "to be pretty"),
    ("예약", "an appointment; a reservation"), ("예약하다", "to make an appointment; to make a reservation"), ("을까요", "Shall we …? (-(으)ㄹ까요?)"), ("유행", "a fashion; popularity; a trend"), ("좀", "a little (an abbreviation of 조금)"), ("짙다", "to be dark; to be dense; to be rich"),
    ("짧다", "to be short"), ("커트", "cut (hair)"), ("파마", "perm"), ("파마하다", "to have a perm"),
]
_ADV = [("짧다", "짧게", "short"), ("길다", "길게", "long"), ("예쁘다", "예쁘게", "pretty")]
_BANG = [("방", "노래방", "a karaoke bar"), ("방", "빨래방", "a laundromat"), ("방", "게임방", "a game room"), ("방", "꾸밈방", "a home interior shop"), ("방", "책방", "a bookstore")]
_PX_BIZ = [("이발소", "a barbershop"), ("은행", "a bank"), ("미용실", "a beauty salon"), ("극장", "a theater"), ("꽃집", "a flower shop"), ("약국", "a pharmacy"), ("제과점", "a bakery"), ("주유소", "a gas station"), ("서점", "a bookstore"),
           ("멕시코 식당", "a Mexican restaurant"), ("세탁소", "a dry cleaner"), ("커피숍", "a coffee shop"), ("백화점", "a department store"), ("호텔", "a hotel"), ("옷가게", "a clothing store")]
_PX_SVC = [("샴푸합니다", "shampoo"), ("머리를 자릅니다", "cut hair"), ("파마합니다", "give a perm"), ("염색합니다", "dye hair"), ("발 마사지합니다", "give a foot massage"), ("커트합니다", "cut (hair)")]
L4 = lesson(
    "Ch 7 · Topic C: At the hair salon",
    "머리 어떻게 해 드릴까요? · 미용실 · 예약 · 염색 · 파마 · 짧게 · 길게",
    requires=[],
    cards=[
        card("Dialog: how do you want your hair cut?",
             "Mr. Park is visiting a hair salon to get his hair cut. The book’s footnotes: 짧게 is the adverb of 짧다; simply by adding 게 to the stem of a stative verb we turn the verb into an adverb; 좀 is an abbreviation of 조금 (a little). (The English is mine.)",
             examples=dlg(_C_DIALOG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s. The book lists 길다/길게, 미용실/머리방, 샴푸(하다), 염색(하다), 예약(하다) and 파마(하다) as pairs; they are split here. 아/어 주다/드리다 and -(으)ㄹ까요? are explained in the grammar lessons, and 좀 is glossed in the dialog’s footnote.",
             tables=[ktable(_C_PAIRS)]),
        card("Making an adverb with -게",
             "Add 게 to the stem of a stative verb to turn it into an adverb: 짧다 → 짧게, 길다 → 길게, 예쁘다 → 예쁘게. The forms are mine, from the book’s 짧게 and 길게.",
             tables=[table(["Verb", "Adverb", "Meaning"], [list(r) for r in _ADV], say=[0, 1])],
             examples=[D("머리를 짧게 잘라 주세요.", "Please cut my hair short."), D("앞머리는 길게 해 주세요.", "Please make the bangs long."), D("예쁘게 숏 커트해 주세요.", "Please give me a pretty short cut.")]),
        card("Cultural notes: 방, 이발소 and 미용실",
             "머리방, whose literal meaning is “hair room”, is a popular term for 미용실 or 미장원 (a hair salon). Since the late 1990s many small businesses have dropped 실 (室), 원 (院) or 점 (店) and used the pure Korean 방 as part of their business names. Some of the popular 방’s in Korea are 노래방 (a karaoke bar), 빨래방 (a laundromat), 게임방, PC방, 꾸밈방 (a home interior shop) and 책방 (a bookstore).\n\n"
             "이발소 or 이용원 (a barbershop) is a place where men get a haircut and a shave, and 미용실, 미장원 or 머리방 (a beauty parlor or hair salon) is its counterpart for women. However, it is also common for a man to get a haircut at 미용실.",
             tables=[table(["Name", "Meaning"], [[b, c] for _, b, c in _BANG], say=[0])]),
        card("Follow-up 1: the businesses and the barbershop services at the Hilltop PX",
             "The book shows the directory of the Hilltop PX and asks you to circle the businesses and the barbershop services you can identify. The directory is a picture and is not reproduced; here are the words in the lists (the meanings are mine except where the book gives them elsewhere).",
             tables=[ktable(_PX_BIZ, title="Businesses"), ktable(_PX_SVC, title="Services")]),
        card("Activities left out",
             "The SMART Board activities, the listening activity (Follow-up 2: four conversations in a beauty salon, to write each customer’s request) and the study of the dialog with the recording are audio or class activities."),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e in _C_PAIRS])
        + [mean("그런데", "by the way; however; but", ["therefore", "and then", "also"]), mean("머리", "the head; hair", ["a hand", "a face", "a body"]), mean("남자", "a man; a male", ["a woman", "a child", "a customer"]), mean("여자", "a woman; a female", ["a man", "a child", "a customer"]),
           mean("유행", "a fashion; a trend", ["a plan", "a reservation", "a color"]), mean("짙다", "to be dark; to be dense; to be rich", ["to be short", "to be long", "to be pretty"]), mean("어울리다", "to suit; to go well with", ["to cut", "to like", "to dye"]),
           mean("얼마예요", "How much ~?", ["Welcome.", "Shall we …?", "What time is it?"]), mean("좀", "a little", ["a lot", "very", "often"]), mean("샴푸하다", "to shampoo", ["to dye", "to cut", "to have a perm"]), mean("염색하다", "to dye", ["to shampoo", "to cut", "to have a perm"]),
           mean("파마하다", "to have a perm", ["to shampoo", "to dye", "to cut"]), mean("예약하다", "to make a reservation", ["to cancel", "to pay", "to order"]), mean("커트", "cut (hair)", ["perm", "a shampoo", "dyeing"]), mean("파마", "perm", ["cut (hair)", "a shampoo", "dyeing"]), mean("염색", "dyeing", ["cut (hair)", "a shampoo", "perm"])]
        + _tr([(a, b) for _, a, b in _C_DIALOG[:12]])
        + [M(f"What is the adverb of {v}?", a, [x for _, x, _ in _ADV if x != a] + [v + "에", v[:-1] + "아"], f"{v} + 게 → {a}.") for v, a, _ in _ADV]
        + [F("머리를 ___ 잘라 주세요. (short)", "짧게", ["짧아", "짧고"], "짧다 + 게 = 짧게."), F("앞머리는 ___ 해 주세요. (long)", "길게", ["길어", "길고"], "길다 + 게 = 길게."), F("___ 숏 커트해 주세요. (pretty)", "예쁘게", ["예뻐", "예쁘고"], "예쁘다 + 게 = 예쁘게."),
           M("What does adding 게 to a stative verb stem do?", "Makes it an adverb", ["Makes it past tense", "Makes it a question", "Makes it a noun"], "짧다 → 짧게."), M("What is 좀?", "An abbreviation of 조금 (a little)", ["An abbreviation of 많이", "An abbreviation of 자주", "A question word"], "좀 = 조금."),
           M("What is the literal meaning of 머리방?", "hair room", ["head shop", "hair store", "beauty house"], "머리방 = “hair room”."), M("Where do men usually get a haircut and a shave?", "이발소 or 이용원 (a barbershop)", ["미용실 only", "머리방 only", "세탁소"], "이발소 or 이용원."),
           M("Which is a karaoke bar?", "노래방", ["빨래방", "게임방", "책방"], "노래방 = karaoke bar."), M("Which is a laundromat?", "빨래방", ["노래방", "게임방", "책방"], "빨래방 = laundromat."), M("What does 책방 mean?", "a bookstore", ["a karaoke bar", "a laundromat", "a game room"], "책방 = bookstore."),
           M("What time is Mr. Park’s reservation?", "Three o’clock", ["Two o’clock", "Four o’clock", "Ten o’clock"], "세 시 예약입니다."), M("How does Mr. Park want his hair cut?", "Short, with the bangs a little long", ["Long, with the bangs short", "Only a perm", "A shampoo only"], "짧게 자르고 싶습니다. 앞머리는 좀 길게 해 주세요."),
           M("Which color is in fashion, according to the hairdresser?", "Brown", ["Black", "Red", "Blonde"], "요즘 갈색이 유행이에요."), M("How much is the dye?", "Eighty-five dollars", ["Fifty dollars", "Eighty dollars", "Ninety-five dollars"], "염색은 팔십오 달러예요."),
           M("Which color does Mr. Park choose?", "Dark brown", ["Light brown", "Black", "Red"], "짙은 갈색으로 해 주세요."), M("What does the hairdresser offer at the end?", "A shampoo", ["A perm", "A massage", "A cut"], "샴푸도 해 드릴까요?"),
           M("What does 손님한테 잘 어울려요 mean?", "It suits you well", ["It is too short", "It is too dark", "It is expensive"], "어울리다 = to suit."), M("What does 마음에 들어요 mean?", "I like it", ["I am sorry", "I am hungry", "I want to go"], "마음에 들다 = to like."),
           read_q("미용실"), read_q("염색"), read_q("예약"), read_q("유행"), read_q("어울려요")]
    ),
)

# ================================================================== Grammar A: 안 / 못
_NEG_TBL = [("먹어요", "안 먹어요", "못 먹어요"), ("자요", "안 자요", "못 자요"), ("놀아요", "안 놀아요", "못 놀아요")]
_NEG_EX = [("김 선생님은 김치를 안 먹어요.", "Mr. Kim does not eat kimchi. (He chooses not to.)"), ("김 선생님은 김치를 못 먹어요.", "Mr. Kim cannot eat kimchi. (He is unable to.)"), ("밤에는 커피를 안 마셔요.", "I do not drink coffee at night."),
           ("제 기숙사 방은 안 넓어요.", "My dormitory room is not spacious."), ("아파서 오늘 파티에 못 가요.", "Because I am ill, I cannot go to the party today."), ("저는 피아노를 안 배워서 못 쳐요.", "Since I have not learned the piano, I cannot play it."),
           ("저는 주말에 청소 안 합니다.", "I do not clean my house on the weekend."), ("저는 주말에 청소 못 합니다.", "I cannot clean my house on the weekend."), ("저는 수영을 잘 못 합니다.", "I do not swim well. (I swim, but not well.)"),
           ("저는 수영을 빨리 못 합니다.", "I do not swim quickly. (I swim, but not quickly.)")]
_NEG_FU2 = [("김 중사는 한식을 안 좋아합니다.", "안", "Sergeant Kim does not like Korean food."), ("저는 패스트푸드를 안 좋아합니다. 그래서 햄버거는 안 먹어요.", "안, 안", "I do not like fast food. So I do not eat hamburgers. (못 먹어요 also works: I cannot eat them.)"),
            ("비가 많이 옵니다. 그래서 밖에서 운동을 못 합니다.", "못", "It is raining a lot. So I cannot exercise outside."), ("오늘 저녁에 숙제가 많습니다. 그래서 텔레비전을 못 봅니다.", "못", "I have a lot of homework tonight. So I cannot watch television. (안 봅니다 also works: I won’t watch.)")]
_NEGV = [("먹다", "to eat"), ("가다", "to go"), ("마시다", "to drink"), ("자다", "to sleep"), ("놀다", "to play"), ("읽다", "to read"), ("오다", "to come"), ("보다", "to watch"), ("만나다", "to meet")]
_NEGN = [("공부하다", "공부", "to study"), ("청소하다", "청소", "to clean"), ("운동하다", "운동", "to exercise"), ("수영하다", "수영", "to swim"), ("쇼핑하다", "쇼핑", "to shop")]
L5 = lesson(
    "Ch 7 · Grammar A: the negating adverbs 안 and 못",
    "안 먹어요 · 못 먹어요 · 공부 안 해요 · 잘 못 해요",
    requires=[],
    cards=[
        card("Negating with 안 and 못",
             "In English we use “not” to negate a verb, as in “He is not learning Japanese.” In Korean we negate a verb by placing 안 or 못 in front of it. 안 is translated as “not” and 못 as “cannot” or “unable to”.",
             tables=[table(["Verb", "Negated with 안", "Negated with 못"], [list(r) for r in _NEG_TBL], say=[0, 1, 2])],
             examples=[D(a, b) for a, b in _NEG_EX[:2]]),
        card("The difference",
             "The first sentence (안) implies that Mr. Kim chooses not to eat kimchi (although he could eat it), and the second (못) means that he is unable to eat kimchi. 안 can negate action verbs as well as stative verbs, but 못 usually negates only action verbs.",
             tables=[table(["Adverb", "Condition", "Rule", "Example"], [["안", "with action and stative verbs", "place 안 before a verb", "가다 → 안 가다; 넓다 → 안 넓다"], ["못", "with action verbs", "place 못 before an action verb", "가다 → 못 가다; 마시다 → 못 마시다"]])]),
        card("Examples",
             "The sentences are the book’s; the English is the book’s except where I added the clarifications in brackets.",
             examples=[D(a, b) for a, b in _NEG_EX[2:6]]),
        card("Note 1: verbs made of a noun + 하다",
             "To negate a verb constructed from “noun + 하다”, such as 공부하다 or 청소하다, place 안/못 between the noun and 하다. The book marks the wrong order with an asterisk: *저는 주말에 안 청소합니다 and *저는 주말에 못 청소합니다 are ungrammatical.",
             examples=[D(a, b) for a, b in _NEG_EX[6:8]],
             tables=[table(["Verb", "안", "못", "Meaning"], [[v, f"{n} 안 해요", f"{n} 못 해요", m] for v, n, m in _NEGN], say=[0, 1, 2])]),
        card("Note 2: when there is an adverb",
             "When there is an adverb in a sentence, 안 and 못 negate the adverb, not the verb.",
             examples=[D(a, b) for a, b in _NEG_EX[8:]]),
        card("Follow-up 2: 안 or 못?",
             "The book asks you to circle the fitting word in parentheses and translate; the book says both may work for some sentences. The answers and the English are my key.",
             tables=[table(["Sentence", "Answer", "Meaning"], [list(r) for r in _NEG_FU2], say=[0])]),
        card("Follow-up 1: question and answer",
             "In the book one partner turns a statement on a sentence strip into a question and the other answers with 안 or 못. The model is below; the strips are not printed. (The English is mine.)",
             examples=dlg([("A", "주중에 비디오 게임을 합니까?", "Do you play video games on weekdays?"), ("B", "저는 주중에 비디오 게임을 안 합니다.", "I do not play video games on weekdays."), ("B", "저는 주중에 비디오 게임을 못 합니다.", "I cannot play video games on weekdays.")])),
    ],
    exercises=uniq(
        [M(f"Which means “I don’t {m.replace('to ', '', 1)}” ({v})?", "안 " + informal(v), ["못 " + informal(v), informal(v) + " 안", "안 " + stem(v)], f"안 goes before the verb: 안 {informal(v)}.") for v, m in _NEGV]
        + [M(f"Which means “I can’t {m.replace('to ', '', 1)}” ({v})?", "못 " + informal(v), ["안 " + informal(v), informal(v) + " 못", "못 " + stem(v)], f"못 goes before the verb: 못 {informal(v)}.") for v, m in _NEGV]
        + [M(f"How do you say “I don’t {m.replace('to ', '', 1)}” with {v}?", f"{n} 안 해요", [f"안 {n}해요", f"{n} 못 해요", f"{n}해요 안"], f"For noun + 하다 the 안 goes between: {n} 안 해요.") for v, n, m in _NEGN]
        + [M(f"How do you say “I can’t {m.replace('to ', '', 1)}” with {v}?", f"{n} 못 해요", [f"못 {n}해요", f"{n} 안 해요", f"{n}해요 못"], f"For noun + 하다 the 못 goes between: {n} 못 해요.") for v, n, m in _NEGN]
        + [M(f"What does {a} mean?", b, [x for _, x in _NEG_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _NEG_EX]
        + [M(f"What does {a} mean?", c, [x for _, _, x in _NEG_FU2 if x != c][:3], f"{a} means “{c}”.") for a, _, c in _NEG_FU2]
        + [M("Which sentence is ungrammatical?", "저는 주말에 안 청소합니다.", ["저는 주말에 청소 안 합니다.", "저는 주말에 청소 못 합니다.", "저는 주말에 일해요."], "With noun + 하다 the 안 goes between the noun and 하다."),
           M("What does 안 mean?", "not", ["cannot", "very", "also"], "안 = not."), M("What does 못 mean?", "cannot; unable to", ["not", "very", "also"], "못 = cannot."),
           M("Which implies that the person chooses not to?", "안", ["못", "both", "neither"], "안 implies a choice."), M("Which implies that the person is unable to?", "못", ["안", "both", "neither"], "못 implies inability."),
           M("Which usually negates only action verbs?", "못", ["안", "both", "neither"], "못 negates action verbs."), M("Which can negate stative verbs too?", "안", ["못", "neither", "only 못"], "안 negates action and stative verbs."),
           M("When there is an adverb in the sentence, what does 안/못 negate?", "The adverb", ["The verb", "The noun", "Nothing"], "저는 수영을 잘 못 합니다."), M("What does 저는 수영을 잘 못 합니다 imply?", "I swim, but not well", ["I cannot swim at all", "I swim very well", "I do not swim"], "못 negates 잘."),
           M("Which is right for “My dormitory room is not spacious”?", "제 기숙사 방은 안 넓어요.", ["제 기숙사 방은 못 넓어요.", "제 기숙사 방은 넓어 안요.", "제 기숙사 방은 안 넓어."], "넓다 is stative: 안 only."),
           F("저는 주말에 청소 ___ 합니다. (do not)", "안", ["못"], "청소 안 합니다."), F("아파서 오늘 파티에 ___ 가요. (cannot)", "못", ["안"], "못 가요."), F("김 선생님은 김치를 ___ 먹어요. (is unable to)", "못", ["안"], "못 먹어요."),
           F("김 중사는 한식을 ___ 좋아합니다. (does not)", "안", ["못"], "좋아하다 → 안."), F("비가 많이 옵니다. 그래서 밖에서 운동을 ___ 합니다.", "못", ["안"], "비 때문에 못."),
           read_q("못 먹어요"), read_q("못 가요"), read_q("안 마셔요"), read_q("못 합니다")]
    ),
)

# ================================================================== Grammar B: -아서/어서 cause
_CAUSE_RULE = [["The last syllable of the verb stem contains ㅏ or ㅗ", "add 아서", "옷이 작다 → 옷이 작아서; 날씨가 좋다 → 날씨가 좋아서"], ["The last syllable contains a vowel other than ㅏ or ㅗ", "add 어서", "한식이 맛있다 → 한식이 맛있어서; 아침을 안 먹다 → 아침을 안 먹어서"]]
_CAUSE_EX = [("비가 와서 등산 못 가요.", "It is raining, and thus I can’t go hiking."), ("이 옷은 작아서 못 입어요.", "Because these clothes are small, I cannot wear them."), ("날씨가 좋아서 공원에 사람이 많아요.", "The weather is good, so there are many people in the park."),
             ("한식이 맛있어서 한국식당에 자주 가요.", "Korean food is delicious, and thus I often go to Korean restaurants."), ("아침을 안 먹어서 배가 고파요.", "Since I did not eat breakfast, I am hungry.")]
_FU3 = [("밥을 안 먹어서 너무 배가 고파요.", "Because I did not eat a meal, I am really hungry."), ("햄버거를 좋아해서 매일 맥도날드에 가요.", "Because I like hamburgers, I go to McDonald’s every day."), ("날씨가 더워서 시원한 주스가 마시고 싶어요.", "Because the weather is hot, I want to drink a cool juice."),
        ("영화를 좋아해서 극장에 자주 가요.", "Because I like movies, I often go to the theater."), ("비가 와서 바다에서 수영 못해요.", "Because it is raining, I can’t swim in the sea."), ("친구 생일이어서 케이크를 사러 가요.", "Because it is a friend’s birthday, I am going to buy a cake.")]
_CV = [("작다", "to be small"), ("좋다", "to be good"), ("맛있다", "to be tasty"), ("먹다", "to eat"), ("오다", "to come"), ("가다", "to go"), ("바쁘다", "to be busy"), ("아프다", "to be sick"), ("배우다", "to learn"), ("많다", "to be many"), ("있다", "to exist"), ("없다", "to not exist"), ("덥다", "to be hot"), ("춥다", "to be cold")]


def _cause(v):
    return b_irregular(v)[2] if v in ("덥다", "춥다") else seo(v)


L6 = lesson(
    "Ch 7 · Grammar B: giving reasons with -아서/어서 (and thus; because)",
    "비가 와서 · 작아서 · 맛있어서 · 안 먹어서 · 생일이어서",
    requires=[],
    cards=[
        card("-아서/어서 for cause and effect",
             "The conjunctive ending -아서/어서 can be interpreted as (1) “and then” (sequential events) and (2) “and thus” (cause and effect). The first meaning was covered in Chapter 5; here you meet the second. “It is raining and thus I can’t go hiking” is virtually the same as “Because it is raining, I can’t go hiking” or “Since it is raining, I can’t go hiking.” So -아서/어서 can be translated as “and therefore”, “so”, “because” or “since”. The first clause (비가 와서, it is raining, and thus …) is the cause and the second clause (등산 못 가요, I can’t go hiking) is the effect.",
             tables=[table(["Condition", "Rule", "Example"], _CAUSE_RULE, title="verb stem + 아서/어서")],
             examples=[D(a, b) for a, b in _CAUSE_EX]),
        card("Some forms",
             "The forms are mine (ㅂ irregular verbs: 덥다 → 더워서, 춥다 → 추워서; 이다 → 이어서 after a consonant, as in 친구 생일이어서).",
             tables=[table(["Dictionary form", "Meaning", "-아서/어서"], [[v, m, _cause(v)] for v, m in _CV], say=[0, 2])]),
        card("Follow-up 3: causes and effects",
             "The book prints six causes in Column A and six effects in Column B and asks you to match them and join the pairs with -아서/어서. Only the first match (밥을 안 먹다 → 너무 배가 고파요) is given in the book; the other matches and the joined sentences are my key (the English is mine; 시원한 and 너무 are not in the core list).",
             tables=[sent_table(_FU3)]),
        card("Activities left out",
             "Follow-up 3b (partners translating the sentences), Follow-up 4 (listening to four conversations where someone declines an invitation with an excuse) and Follow-up 5 (a blind-date role-play; its models are in the Topic B extras lesson) are audio or class activities."),
    ],
    exercises=uniq(
        [M(f"Which is the -아서/어서 form of {v} ({m})?", _cause(v), [x for x in {stem(v) + "아서", stem(v) + "어서", stem(v) + "고", stem(v) + "서", informal(v)} if x != _cause(v)][:3], f"{v} → {_cause(v)}.") for v, m in _CV]
        + [M(f"What does {a} mean?", b, [x for _, x in _CAUSE_EX + _FU3 if x != b][:3], f"{a} means “{b}”.") for a, b in _CAUSE_EX + _FU3]
        + [F("비가 ___ 등산 못 가요.", "와서", ["오서", "와고"], "오다 → 와서."), F("이 옷은 ___ 못 입어요. (small)", "작아서", ["작어서", "작고"], "작다: ㅏ → 작아서."), F("날씨가 ___ 공원에 사람이 많아요. (good)", "좋아서", ["좋어서", "좋고"], "좋다: ㅗ → 좋아서."),
           F("한식이 ___ 한국식당에 자주 가요. (tasty)", "맛있어서", ["맛있아서", "맛있고"], "맛있다: ㅣ → 맛있어서."), F("아침을 안 ___ 배가 고파요.", "먹어서", ["먹아서", "먹고"], "먹다: ㅓ → 먹어서."), F("친구 ___ 케이크를 사러 가요. (is a birthday)", "생일이어서", ["생일이아서", "생일이고"], "생일 + 이어서."),
           F("날씨가 ___ 시원한 주스가 마시고 싶어요. (hot)", "더워서", ["덥어서", "더우서"], "덥다 → 더워서."), F("오늘은 ___ 못 가요. (sick)", "아파서", ["아프서", "아퍼서"], "아프다 → 아파서."),
           M("What does -아서/어서 mean in a cause-and-effect sentence?", "and thus; so; because", ["and then", "if", "although"], "비가 와서 = it is raining, and thus…"), M("What did Chapter 5 teach about -아서/어서?", "“and then” (sequential events)", ["“because”", "“if”", "“although”"], "The first meaning is “and then”."),
           M("In 비가 와서 등산 못 가요, which clause is the cause?", "비가 와서", ["등산 못 가요", "Both", "Neither"], "비가 와서 = cause."), M("When is 아서 added?", "When the last syllable has ㅏ or ㅗ", ["When it has any other vowel", "Always", "Never"], "작아서, 좋아서."),
           M("When is 어서 added?", "When the last syllable has a vowel other than ㅏ or ㅗ", ["When it has ㅏ or ㅗ", "Always", "Never"], "맛있어서, 먹어서."),
           M("Which sentence means “Since I did not eat breakfast, I am hungry”?", "아침을 안 먹어서 배가 고파요.", ["아침을 먹고 배가 고파요.", "아침을 안 먹으러 배가 고파요.", "아침을 안 먹으면 배가 고파요."], "안 먹어서 = since I did not eat.")]
        + [read_q("작아서"), read_q("좋아서"), read_q("맛있어서"), read_q("먹어서")]
    ),
)

# ================================================================== Grammar C: -아/어 주다
_GIVE_EX = [("친구가 책을 읽어 줍니다.", "My friend reads a book (for someone)."), ("태권도를 가르쳐 주세요.", "Please teach me tae kwon do."), ("문 열어 주세요.", "Please open the door (for me)."), ("교실 문을 닫아 주세요.", "Please close the classroom door (for us)."),
            ("머리를 짧게 깎아 주세요.", "Please cut my hair short (for me)."), ("창문 좀 열어 주세요.", "Please open the window (for us).")]
_GIVE_PH = [("일어서다", "일어서 주세요", "stand up"), ("앉다", "앉아 주세요", "sit down"), ("한국말을 하다", "한국말을 해 주세요", "speak Korean"), ("책을 펴다", "책을 펴 주세요", "open the book"), ("조용히 하다", "조용히 해 주세요", "be quiet"),
            ("스마트보드를 끄다", "스마트보드를 꺼 주세요", "turn off the SMART Board"), ("창문을 열다", "창문을 열어 주세요", "open the window"), ("도서관에 가다", "도서관에 가 주세요", "go to the library"), ("창문을 닫다", "창문을 닫아 주세요", "close the window"),
            ("문을 열다", "문을 열어 주세요", "open the door"), ("컴퓨터를 켜다", "컴퓨터를 켜 주세요", "turn on the computer"), ("커피숍에 오다", "커피숍에 와 주세요", "come to the coffee shop"), ("큰 소리로 책을 읽다", "큰 소리로 책을 읽어 주세요", "read the book loudly")]
_GIVE_FU3 = [("차에 기름이 없다", "주유소에서 기름을 넣어 주세요.", "Please fill up at the gas station."), ("음식을 못 한다", "식당에서 음식을 주문해 주세요.", "Please order food at a restaurant."), ("은행에 못 간다", "은행에서 돈을 찾아 주세요.", "Please withdraw money at the bank."),
             ("빨래를 못 한다", "세탁소에 옷을 맡겨 주세요.", "Please leave the clothes at the cleaner’s."), ("핸드폰이 없다", "친구한테 전화해 주세요.", "Please call my friend.")]
_GIVE_V = [("읽다", "to read"), ("열다", "to open"), ("닫다", "to close"), ("가르치다", "to teach"), ("돕다", "to help"), ("알리다", "to inform"), ("넣다", "to put in"), ("찾다", "to withdraw; to find"), ("맡기다", "to entrust"), ("주문하다", "to order"), ("전화하다", "to call")]
_GIVE_SPECIAL = {"돕다": "도와", "알리다": "알려", "가르치다": "가르쳐"}


def _give(v):
    return (_GIVE_SPECIAL.get(v) or informal(v)[:-1]) + " 주세요"


L7 = lesson(
    "Ch 7 · Grammar C: asking for a service with -아/어 주세요",
    "열어 주세요 · 닫아 주세요 · 가르쳐 주세요 · 도와 주세요 · 해 주세요",
    requires=[],
    cards=[
        card("The auxiliary verb for providing service",
             "Earlier you learned that the verbs 주다 and 드리다 (the honorific of 주다) mean “to give”. However, when 주다 or 드리다 is used as part of the auxiliary verb -아/어 주다 or -아/어 드리다, it implies that the subject provides or offers a service, or does something for someone else’s benefit. 친구가 책을 읽어 줍니다/드립니다 implies that my friend is (providing the service of) reading a book to someone else. So if you want someone to do something for you, ask with -아/어 주세요. Stative verbs do not work with -아/어 주다 and -아/어 드리다.",
             tables=[table(["Condition", "Rule", "Example"], [["The last syllable of an action verb stem contains ㅏ or ㅗ", "add 아 + 주다 / 드리다", "문을 닫다 → 문을 닫아 주다 / 닫아 드리다"], ["The last syllable contains a vowel other than ㅏ or ㅗ", "add 어 + 주다 / 드리다", "문을 열다 → 문을 열어 주다 / 열어 드리다"]], title="action verb stem + 아/어 주다 / 드리다")],
             examples=[D(a, b) for a, b in _GIVE_EX]),
        card("Verbs that go with -아/어 주다 because of their meanings",
             "The following verbs are usually used with -아/어 주다 because of their intrinsic meanings: 돕다 (to help) → 도와 주다, 가르치다 (to teach) → 가르쳐 주다, 알리다 (to inform) → 알려 주다.",
             tables=[table(["Verb", "Meaning", "-아/어 주세요"], [[v, m, _give(v)] for v, m in [("돕다", "to help"), ("가르치다", "to teach"), ("알리다", "to inform")]], say=[0, 2])]),
        card("Follow-up 1: turn each phrase into a request",
             "The book gives two lists of phrases (List A and List B) to turn into -아/어 주세요 requests with a partner’s name; the model is 일어서다 → 김 일병, 일어서 주세요! The requests below are my key (the English is mine; 조용히, “quietly”, and 큰 소리로, “loudly”, are glossed in the book).",
             tables=[table(["Phrase", "Request", "Meaning"], [list(r) for r in _GIVE_PH], say=[0, 1])]),
        card("Follow-up 3: polite requests at businesses",
             "The book gives four situations and the phrases 옷을 맡기다, 전화하다, 음식을 주문하다 and 돈을 찾다, and asks you to write a request that names the facility, and translate it. The model is the first row; the other answers are my key.",
             tables=[table(["Situation", "Request", "Meaning"], [list(r) for r in _GIVE_FU3], say=[0, 1])]),
        card("Activities left out",
             "Follow-up 2 (listening to four conversations to write down the request) is an audio activity. (The book’s 깍아 in 머리를 짧게 깍아 주세요 is a typo for 깎아.)"),
    ],
    exercises=uniq(
        [M(f"Which is the request form (-아/어 주세요) of {v} ({m})?", _give(v), [x for x in {stem(v) + " 주세요", stem(v) + "아 주세요", stem(v) + "어 주세요", informal(v) + " 주세요"} if x != _give(v)][:3], f"{v} → {_give(v)}.") for v, m in _GIVE_V]
        + [M(f"How do you say “Please {m}”?", r, [x for _, x, _ in _GIVE_PH if x != r][:3], f"{p} → {r}.") for p, r, m in _GIVE_PH]
        + [M(f"What does {r} mean?", f"Please {m}", [f"Please {x}" for _, _, x in _GIVE_PH if x != m][:3], f"{r} means “Please {m}”.") for p, r, m in _GIVE_PH[:8]]
        + [M(f"What does {a} mean?", b, [x for _, x in _GIVE_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _GIVE_EX]
        + [M(f"What does {a} mean?", c, [x for _, _, x in _GIVE_FU3 if x != c][:3], f"{a} means “{c}”.") for _, a, c in _GIVE_FU3]
        + [M(f"Which request fits the situation “{s}”?", r, [x for _, x, _ in _GIVE_FU3 if x != r][:3], f"{s} → {r}") for s, r, _ in _GIVE_FU3]
        + [F("문을 열___ 주세요.", "어", ["아", "고"], "열 has ㅓ → 어."), F("문을 닫___ 주세요.", "아", ["어", "고"], "닫 has ㅏ → 아."), F("태권도를 가르쳐 ___. (Please…)", "주세요", ["줍니다", "드립니다"], "-아/어 주세요."), F("교실 문을 닫아 ___. (Please)", "주세요", ["줍니다", "받아요"], "-아/어 주세요."),
           F("돕다 → ___ 주다", "도와", ["돕아", "도우어"], "돕다 is ㅂ irregular → 도와."), F("알리다 → ___ 주다", "알려", ["알리어", "알리"], "알리다 → 알려."),
           M("What does 주다/드리다 mean on its own?", "to give", ["to receive", "to ask", "to order"], "주다 = to give."), M("What does -아/어 주다 imply?", "The subject does something for someone else’s benefit", ["The subject wants to do something", "The subject cannot do something", "The subject has done something"], "-아/어 주다 = providing a service."),
           M("Which verbs do NOT work with -아/어 주다?", "Stative verbs", ["Action verbs", "Verbs of motion", "Verbs of speech"], "Stative verbs don’t work."), M("What does 드리다 add to -아/어 주다?", "The honorific (humble) form", ["The past tense", "The negative", "A question"], "드리다 is the honorific of 주다."),
           M("Which is the polite request “Please open the window”?", "창문 좀 열어 주세요.", ["창문 좀 열어 줍니다.", "창문 좀 열고 싶어요.", "창문 좀 열까요?"], "-아/어 주세요 = please do for me.")]
        + [read_q("열어 주세요"), read_q("닫아 주세요"), read_q("가르쳐 주세요"), read_q("도와 주세요")]
    ),
)

# ================================================================== Grammar D: -(으)ㄹ까요?
_LKKA_EX = [("박 선생님, 우리 점심 식사 같이 할까요?", "Mr. Park, shall we have lunch together?"), ("오후에 (우리) 같이 축구 할까요?", "Shall we play soccer this afternoon?"), ("(우리) 어디에서 만날까요?", "Where shall we meet?"), ("(제가) 창문 좀 열까요?", "Shall I open the window?"),
            ("물 좀 갖다 줄까요?", "Shall I bring you some water?"), ("어떻게 도와드릴까요?", "How may I/we help you?"), ("(우리) 한국 식당에 갈까?", "Shall we go to a Korean restaurant?"), ("(내가) 스마트보드에 쓸까?", "Shall I write (it) on the SMART Board?")]
_LKV = [("먹다", "to eat"), ("가다", "to go"), ("보다", "to see; to watch"), ("만나다", "to meet"), ("열다", "to open"), ("하다", "to do"), ("읽다", "to read"), ("마시다", "to drink"), ("쓰다", "to write"), ("놀다", "to play"), ("앉다", "to sit")]
_FU4 = [("점심을 벨라스에서 먹다", "점심을 벨라스에서 먹을까요?", "Shall we eat lunch at Bella’s?"), ("주말에 영화를 보다", "주말에 영화를 볼까요?", "Shall we watch a movie on the weekend?"), ("체육관에서 운동하다", "체육관에서 운동할까요?", "Shall we exercise at the gym?"),
        ("서점에서 책을 읽다", "서점에서 책을 읽을까요?", "Shall we read books at the bookstore?"), ("몬트레이 시내 나이트클럽에 가다", "몬트레이 시내 나이트클럽에 갈까요?", "Shall we go to a nightclub in downtown Monterey?"), ("은행에서 돈을 찾다", "은행에서 돈을 찾을까요?", "Shall we withdraw money at the bank?")]
_TXT = [("영철", "우리 주말에 같이 테니스 칠까요?", "Shall we play tennis together on the weekend?"), ("수영", "좋아요. 그럼 몇 시에 만날까요?", "Sure. Then what time shall we meet?"), ("영철", "열 시 어때요?", "How about ten o’clock?"),
        ("수영", "좋아요! 그럼 열 시에 테니스장 앞에서 봐요!", "Great! Then let’s meet in front of the tennis court at ten!"),
        ("지아", "오늘 저녁에 치킨하고 맥주 어때?", "How about chicken and beer this evening?"), ("유나", "좋아. 그럼 식당에 가서 먹을까?", "Sure. Then shall we go to a restaurant and eat?"), ("지아", "아니, 집에서 시켜 먹자.", "No, let’s order in and eat at home."),
        ("유나", "알았어! 그럼 내가 샐러드도 같이 시킬까?", "Okay! Then shall I order a salad too?"), ("지아", "그래!", "Yes!")]
L8 = lesson(
    "Ch 7 · Grammar D: “Shall we …?” and “Shall I …?” with -(으)ㄹ까요?",
    "먹을까요? · 갈까요? · 할까요? · 열까요? · 도와드릴까요? · 갈까?",
    requires=[],
    cards=[
        card("-(으)ㄹ까요?",
             "-(으)ㄹ까요? can be used when making an invitation or suggestion, when asking for thoughts or input, and when offering a service or favor. The subject of the sentence can be omitted when using -(으)ㄹ까요?.",
             tables=[table(["Condition", "Rule", "Example"], [["A verb stem ends in a consonant", "add 을까요?", "먹다 → 먹 + 을까요? → 먹을까요?"], ["A verb stem ends in a vowel", "add ㄹ까요?", "가다 → 가 + ㄹ까요? → 갈까요?"]], title="verb stem + (으)ㄹ까요?")]),
        card("Three uses",
             "1. Making an invitation or suggestion. 2. Asking for thoughts or offering a favor. In a situation where the speaker offers a favor or service to the listener, we often combine -아/어 주다/드리다 with the expression, as in -아/어 줄까요 / 드릴까요? (The English is the book’s except for the rows I added.)",
             examples=[D(a, b) for a, b in _LKKA_EX[:6]]),
        card("The blunt form: -(으)ㄹ까",
             "The blunt form of -(으)ㄹ까요 is -(으)ㄹ까.",
             examples=[D(a, b) for a, b in _LKKA_EX[6:]],
             tables=[table(["Dictionary form", "Meaning", "-(으)ㄹ까요?", "Blunt (-(으)ㄹ까?)"], [[v, m, lkka(v), lkka_blunt(v)] for v, m in _LKV], say=[0, 2, 3])]),
        card("Follow-up 4: change each phrase into a suggestion",
             "In the book one student changes the phrases into suggestions with -(으)ㄹ까요 and the partner answers with -(으)ㅂ시다. The book’s model: 한국 식당에 가다 → A: 한국 식당에 갈까요? B: 네, 갑시다. / 아니요, 이탈리아 식당에 갑시다. The six phrases and my answers (the English is mine):",
             tables=[table(["Phrase", "Suggestion", "Meaning"], [list(r) for r in _FU4], say=[0, 1])],
             examples=dlg([("A", "한국 식당에 갈까요?", "Shall we go to a Korean restaurant?"), ("B", "네, 갑시다.", "Yes, let’s go."), ("B", "아니요, 이탈리아 식당에 갑시다.", "No, let’s go to an Italian restaurant.")])),
        card("Follow-up 7: two text-message conversations",
             "The book asks you to underline the sentence with -(으)ㄹ까요 and translate it. The messages are the book’s (the English is mine); the sentences with -(으)ㄹ까(요) are 칠까요, 만날까요, 먹을까 and 시킬까.",
             examples=dlg(_TXT[:4]) + dlg(_TXT[4:])),
        card("Activities left out",
             "Follow-up 5 (listening to three conversations between co-workers: what one offers and whether the other accepts) and Follow-up 6 (a four-station role-play at a department store, a bakery, a cleaner’s and a gas station) are audio or class activities."),
    ],
    exercises=uniq(
        [M(f"Which means “Shall we {m.replace('to ', '', 1).split(';')[0]}?” ({v})?", lkka(v), [x for x in {stem(v) + "을까요?", stem(v) + "세요?", stem(v) + "까요?", informal(v) + "?"} if x != lkka(v)][:3], f"{v} → {lkka(v)}") for v, m in _LKV]
        + [M(f"Which is the blunt form of {lkka(v)}", lkka_blunt(v), [lkka(v), stem(v) + "자", informal(v)[:-1]], f"Drop 요: {lkka_blunt(v)}") for v, m in _LKV[:6]]
        + [M(f"What does {a} mean?", b, [x for _, x in _LKKA_EX if x != b][:3], f"{a} means “{b}”.") for a, b in _LKKA_EX]
        + [M(f"What does {a} mean?", c, [x for _, _, x in _FU4 if x != c][:3], f"{a} means “{c}”.") for _, a, c in _FU4]
        + [M(f"What does {a} mean?", c, [x for _, _, x in _TXT if x != c][:3], f"{a} means “{c}”.") for _, a, c in _TXT]
        + [F("점심(을) 먹___? (Shall we eat)", "을까요", ["ㄹ까요", "자요"], "먹 ends in a consonant → 을까요."), F("한국 식당에 갈___? (Shall we go)", "까요", ["을까요", "자요"], "가 + ㄹ까요 = 갈까요."), F("(제가) 창문 좀 열___? (Shall I open)", "까요", ["을까요", "자요"], "열 ends in ㄹ → 열까요."),
           F("몇 시에 만날___?", "까요", ["을까요", "자요"], "만나 + ㄹ까요 = 만날까요."), F("물 좀 갖다 ___? (Shall I bring…)", "줄까요", ["주세요", "줍니다"], "-아/어 줄까요?"), F("어떻게 도와___? (How may I help you)", "드릴까요", ["드립니까", "주세요"], "도와 드릴까요?"),
           M("When is 을까요 added?", "When the verb stem ends in a consonant", ["When it ends in a vowel", "Always", "Never"], "먹을까요."), M("When is ㄹ까요 added?", "When the verb stem ends in a vowel", ["When it ends in a consonant", "Always", "Never"], "갈까요."),
           M("Which uses does -(으)ㄹ까요? have?", "Invitation, asking for thoughts, offering a favor", ["Only questions about the past", "Only commands", "Only wishes"], "-(으)ㄹ까요? covers three uses."), M("What is the blunt form of -(으)ㄹ까요?", "-(으)ㄹ까", ["-(으)ㄹ까요", "-자", "-세요"], "한국 식당에 갈까?"),
           M("How do you offer a service with -(으)ㄹ까요?", "Combine -아/어 주다/드리다 with it", ["Add 안", "Add 못", "Use -고 싶다"], "물 좀 갖다 줄까요? 어떻게 도와드릴까요?"), M("Can the subject be omitted with -(으)ㄹ까요?", "Yes", ["No", "Only with 우리", "Only with 제가"], "The subject can be omitted."),
           M("Which sentence means “Shall we go to a Korean restaurant?”", "(우리) 한국 식당에 갈까?", ["(우리) 한국 식당에 가자.", "(우리) 한국 식당에 가요.", "(우리) 한국 식당에 갔어."], "-(으)ㄹ까 = blunt shall we.")]
        + [read_q("먹을까요"), read_q("갈까요"), read_q("만날까요"), read_q("도와드릴까요")]
    ),
)

# ================================================================== Activities: hair salon
_Q_A = [("여자 커트하고 파마 잘 하는 미용실이 어디 있어요?", "Where is a hair salon that is good at cuts and perms for women?"), ("산호세에 한국 미용실이 많습니다.", "There are many Korean hair salons in San Jose."),
        ("좋은 미용실은 박민철 헤어입니다!", "A good hair salon is Park Minchul Hair!"), ("박민철 헤어에서 커트나 파마하세요.", "Get a cut or a perm at Park Minchul Hair."), ("마음에 드실 거예요.", "You will like it."),
        ("미용사들이 머리를 잘 해요.", "The hairdressers do hair well."), ("그래서 보통 사람들이 많습니다.", "So there are usually many people."), ("꼭 예약을 하세요.", "Be sure to make a reservation.")]
_JM = [("이번 주 토요일에 머리 하고 싶습니다.", "I want to get my hair done this Saturday."), ("요즘 유행하는 머리가 어떤 머리예요?", "What kind of hairstyle is in fashion these days?"), ("저는 파마하고 염색을 하고 싶습니다.", "I want to get a perm and a dye."), ("얼마예요?", "How much is it?"),
       ("또 몇 시에 문을 열고 몇 시에 문을 닫아요?", "Also, what time do you open and what time do you close?"), ("어떻게 예약해요?", "How do I make a reservation?"), ("제 이름은 김정민입니다.", "My name is Kim Jeongmin."), ("전화 좀 부탁드립니다.", "Please call me.")]
_RP = [("어서 오세요.", "Welcome."), ("몇 시 예약이세요?", "What time is your reservation?"), ("머리 어떻게 해 드릴까요?", "How would you like your hair done?"), ("마음에 드세요?", "Do you like it?"), ("다시 오세요.", "Please come again."),
       ("네 시 예약이에요.", "I have a four o’clock reservation."), ("머리 짧게 잘라 주세요.", "Please cut my hair short."), ("파마하고 갈색으로 염색해 주세요.", "Please give me a perm and dye it brown."), ("앞머리는 길게 해 주세요.", "Please make the bangs long."),
       ("송혜교처럼 파마해 주세요.", "Please give me a perm like Song Hye-kyo’s.")]
L9 = lesson(
    "Ch 7 · Activities: the hair salon",
    "한국어 활용 · 미용실 질문과 답변 · 정민의 질문 · 미용사와 손님",
    requires=[],
    cards=[
        card("Activity 2: a question and an answer on a Korean-American website",
             "Jungmin wants to get her hair done this weekend. On the “Koreans in America” website she finds this question and answer. The book glosses 추천하다 as “to recommend”. The English is mine; the book’s three comprehension questions have my answers below the text.",
             examples=passage(_Q_A),
             tables=[table(["Question", "Answer"], [["Which hair salon was recommended?", "Park Minchul Hair (박민철 헤어), in San Jose."], ["Why is that salon a good choice?", "The hairdressers do hair well, so you will like it (and it is usually busy)."], ["What is Jungmin advised to do before going, and why?", "Make a reservation, because there are usually many people."]])]),
        card("Activity 2b: Jungmin’s questions to the website",
             "Jungmin posts some questions to get more information. The post is headed 작성자: 김정민 (the writer) and 제목: 미용실 (the title). The post gives her phone number, which is left out. The book asks you to translate the questions; my translations:",
             examples=[D(a, b) for a, b in _JM]),
        card("Activity 3: useful expressions for the hairstylist and the customer",
             "The book’s expressions for the role-play at a hair salon. (The book writes the reservation as 4시; it is spelled out here. 처럼, “like”, is glossed in the book. The English is mine.)",
             tables=[sent_table(_RP[:5], title="미용사 (hairstylist) — the first five are the hairstylist’s lines"), sent_table(_RP[5:], title="손님 (customer)")]),
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with so they can offer other activities tailored to your learning style and needs.\n\n"
             "Now I am able to: list and discuss businesses around town; order food and drink at a restaurant; ask for services at a hair salon or barber shop.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the negating adverbs 안 and 못; the conjunctive ending -아/어서 for cause and effect (and thus; because); the auxiliary verb -아/어 주다 used to express “the sense of providing service”; and the Sino-Korean syllables 소 (所), 음 (飮) and 점 (店)."),
        card("Activities left out",
             "Activity 1 (listening to three dialogs between a male hairstylist and a female customer and matching hairstyle pictures), Activity 2c (two voice mails), the hairstyle pictures and celebrity photos of Activity 3, and the role-play cards are audio, picture or class activities."),
    ],
    exercises=uniq(
        _tr(_Q_A)
        + _tr(_JM)
        + _tr(_RP)
        + [M("Which hair salon is recommended in the answer?", "박민철 헤어", ["산호세 헤어", "한국 미용실", "델몬티 헤어"], "좋은 미용실은 박민철 헤어입니다!"), M("Where are there many Korean hair salons?", "San Jose (산호세)", ["Monterey", "Seoul", "Big Sur"], "산호세에 한국 미용실이 많습니다."),
           M("Why is the salon usually crowded?", "The hairdressers do hair well", ["It is cheap", "It is new", "It is near the school"], "미용사들이 머리를 잘 해요. 그래서 보통 사람들이 많습니다."), M("What should you be sure to do before going?", "Make a reservation", ["Wash your hair", "Bring money", "Call a friend"], "꼭 예약을 하세요."),
           M("What does Jungmin want to get done?", "A perm and a dye", ["A cut only", "A shampoo only", "Nothing"], "저는 파마하고 염색을 하고 싶습니다."), M("What does 어떻게 예약해요? ask?", "How do I make a reservation?", ["When do you open?", "How much is it?", "Where is the salon?"], "어떻게 예약해요?"),
           F("꼭 ___을 하세요. (a reservation)", "예약", ["염색", "파마"], "예약을 하다."), F("이번 주 토요일에 머리 하고 ___. (I want to)", "싶습니다", ["싶어합니다", "있습니다"], "-고 싶다 for 1st person."), F("박민철 헤어에서 커트나 ___하세요.", "파마", ["예약", "가게"], "파마하다."),
           F("머리 짧게 ___ 주세요. (cut)", "잘라", ["자르어", "잘어"], "자르다 → 잘라."), F("미용사: 머리 어떻게 해 ___? (shall I do)", "드릴까요", ["줍니까", "주세요"], "해 드릴까요?"), F("손님: 파마하고 갈색으로 염색해 ___.", "주세요", ["드릴까요", "줍니다"], "염색해 주세요."),
           M("Who says 머리 어떻게 해 드릴까요?", "The hairstylist", ["The customer", "A friend", "The cashier"], "해 드릴까요 = shall I do it for you?"), M("Who says 머리 짧게 잘라 주세요?", "The customer", ["The hairstylist", "A friend", "The cashier"], "잘라 주세요 = please cut for me."),
           read_q("예약을 하세요"), read_q("마음에 드실"), read_q("염색해 주세요")]
    ),
)

# ================================================================== Core vocabulary
_CV_TOWN = [("가게", "a store; a shop", "델몬티 쇼핑 센터에 가게들이 많습니다."), ("꽃집", "a flower shop; “flower house”", "발렌타인 데이에 꽃집에서 부케를 주문합니다."), ("백화점", "a department store", "이번 주말에 백화점에서 세일을 해요."),
            ("서점", "a bookstore", "주말에는 보통 보더스 서점에 가서 책을 봅니다."), ("세탁소", "a dry cleaner; a laundromat; “cleaning place”", "피엑스에 세탁소가 있어요. 저는 그곳에 군복을 맡겨요."), ("시내", "downtown; “in(side) city”", "금요일 밤 몬트레이 시내 나이트클럽에 사람들이 많습니다."),
            ("약국", "a pharmacy; a drug store", "지금 타이레놀을 사러 약국에 갑니다."), ("은행", "a bank", "몬트레이 시내에 웰스 파고 은행이 있습니다."), ("제과점", "a bakery", "아침으로 제과점에서 커피와 빵을 먹어요."), ("빵집", "a bakery", "아침으로 빵집에서 커피와 빵을 먹어요."),
            ("주유소", "a gas station; “fueling place”", "저는 쉘 주유소에서 기름을 넣어요.")]
_CV_REST = [("갖다 주다", "to bring; to take", "여기 김치 좀 더 갖다 주세요."), ("계산서", "a bill; a check; “calculation paper”", "여기 계산서 주세요."), ("김밥", "gimbap; “seaweed rice roll”", "민 일병은 김밥을 아주 좋아합니다."),
            ("김치", "kimchi", "한국 사람들은 식사 때마다 김치를 먹습니다."), ("김치찌개", "kimchi stew", "한국 사람들은 식사 때마다 김치를 먹습니다."), ("만두", "dumplings; pot stickers", "만두에는 보통 채소와 고기가 들어 있어요."),
            ("맛있다", "to be tasty; to be delicious; “taste exists”", "비빔밥이 조금 맵지만 맛있어요."), ("맥주", "beer", "저는 독일 맥주를 좋아합니다."), ("맵다", "to be spicy; to be hot", "김치는 너무 매워요."), ("물", "water", "여기 물 좀 주세요."),
            ("반찬", "a side dish", "한국음식은 보통 반찬이 많이 나옵니다."), ("받다", "to receive; to take", "이 식당은 비자카드와 마스터 카드만 받습니다."), ("배가 고프다", "to be hungry; “the stomach is hungry”", "아침을 못 먹어서 너무 배가 고파요."),
            ("병", "a counter for bottles", "여기 맥주 두 병 주세요."), ("불고기", "bulgogi; Korean-style barbecued beef", "이 식당은 불고기가 맛있어요."), ("비빔밥", "bibimbap; rice mixed with vegetables and meat; “mixed rice”", "여기 불고기 이 인분하고 비빔밥 하나 주세요."),
            ("시키다", "to order (food or drinks)", "손님, 뭐 시키시겠습니까?"), ("주문하다", "to order (food or drinks)", "무슨 음식을 주문하시겠습니까?"), ("신용카드", "a credit card", "신용카드 받습니까? 네, 비자, 마스터, 아메리칸 익스프레스 카드, 다 받습니다."),
            ("음료수", "beverages; drinks; “drinking water”", "저는 음료수는 안 마셔요."), ("음식", "food", "중국 음식 좋아하세요?"), ("인분", "a serving; “person’s portion”", "불고기 사 인분하고 맥주 세 병 주세요."), ("잔", "a counter for a glass or cup", "여기 물 한 잔 주세요."),
            ("주다", "to give; to offer", "여기 메뉴 좀 주세요."), ("드리다", "to give; to offer (honorific)", "무슨 음식 드릴까요?")]
_CV_SALON = [("갈색", "brown (color)", "요즘 갈색 머리가 유행이에요."), ("길다", "to be long", "앞머리가 너무 길어서 조금 자르고 싶어요."), ("마음에 들다", "to like or be pleased with something; “to enter one’s heart”", "몬트레이 날씨가 아주 마음에 들어요."),
             ("머리", "the head; hair", "오늘 머리가 좀 아파요."), ("머리 2", "the head; hair", "머리 좀 잘라 주세요."), ("미용실", "beauty salon", "미용실에 보통 머리를 자르고 파마하러 갑니다."), ("머리방", "beauty salon", "미용실에 보통 머리를 자르고 파마하러 갑니다."),
             ("손님", "a customer; a client", "주말에는 미용실에 파마 손님이 많아요."), ("어서 오세요", "Welcome. Come on in.", "손님, 어서 오세요. 몇 분이십니까?"), ("어울리다", "to suit; to go well with", "저에게는 긴 머리가 잘 어울립니다."),
             ("얼마예요", "How much ~?", "이 책 얼마예요?"), ("염색", "dyeing", "머리를 갈색으로 염색해 주세요."), ("염색하다", "to dye", "머리를 갈색으로 염색해 주세요."), ("영화관", "a movie theater", "어제 친구와 영화관에 갔다 왔어요."),
             ("예쁘다", "to be pretty", "예쁘게 숏 커트해 주세요."), ("예약", "an appointment; a reservation", "그 식당은 늘 손님이 많아요. 가기 전에 예약하세요."), ("예약하다", "to make an appointment; to make a reservation", "그 식당은 늘 손님이 많아요. 가기 전에 예약하세요."),
             ("유행", "a fashion; popularity; a trend", "요즘은 긴 머리가 유행이에요."), ("자르다", "to cut", "앞 머리는 짧게 잘라 주세요."), ("짧다", "to be short", "군인의 머리는 짧아요."), ("짙다", "to be dark; to be dense; to be rich", "머리 색깔이 아주 짙어요.")]
_CV_LOAN = [("사이다", "soft drinks; soda pop; “cider”", "저는 사이다 한 잔 주세요."), ("샴푸", "a shampoo", "샴푸도 해 드릴까요?"), ("샴푸하다", "to shampoo", "샴푸도 해 드릴까요?"), ("쇼핑센터", "a shopping center", "주말에 보통 델몬티 쇼핑센터에 가서 쇼핑합니다."),
            ("커트", "cut (hair)", "저는 짧은 커트 머리가 좋아요."), ("커피숍", "a coffee shop; a cafe", "스타벅스 커피숍에서 한 시에 만날까요?"), ("콜라", "cola; Coke", "음료수로는 콜라 주세요."), ("파마", "perm", "제 머리를 파마해 주세요."), ("파마하다", "to have a perm", "제 머리를 파마해 주세요.")]
_CV_OTH = [("걸리다", "to take (time)", "몬트레이에서 샌프란시스코까지 두 시간 정도 걸립니다."), ("게", "adverb “maker”", "머리를 짧게 잘랐습니다."), ("그런데", "by the way; however; but; and", "그런데 파마는 얼마예요?"), ("기름", "oil; gasoline", "차에 기름이 없어서 지금 주유소에 가요."),
           ("남자", "a man; a male", "요즘은 미용실에 가는 남자들이 많아요."), ("넣다", "to insert; to put in", "주유소에서 기름을 넣습니다."), ("돈", "money", "새 컴퓨터를 사서 돈이 없어요."), ("등", "and so on; et cetera", "백화점에서 옷, 넥타이 등을 삽니다."),
           ("맡기다", "to entrust; to deposit", "토요일마다 세탁소에 군복을 맡깁니다."), ("물건", "a thing; stuff; goods", "백화점에 물건들이 많아요."), ("사다", "to buy; to purchase", "저는 스낵 바에서 아침마다 커피를 사서 마십니다."),
           ("생일", "a birthday", "제 친구 생일이어서 생일 카드를 삽니다."), ("생신", "a birthday (honorific)", "어머니 생신이어서 케이크를 삽니다."), ("아/어 주다", "auxiliary verb used to express the sense of providing service", "문 좀 열어 주세요."),
           ("아/어 드리다", "auxiliary verb used to express the sense of providing service (honorific)", "문 좀 열어 드릴까요?"), ("아서/어서", "and thus; so; because", "아침을 안 먹어서 너무 배가 고파요."), ("약", "medicine; drug; medication", "약국에서 약을 삽니다."),
           ("여자", "a woman; a female", "요즘은 여자 경찰관도 많아요."), ("이야기", "a chat; a talk; a story", "저는 엄마하고 전화로 자주 얘기합니다."), ("얘기", "a chat; a talk; a story", "저는 엄마하고 전화로 자주 얘기합니다."),
           ("이야기하다", "to have a chat; to have a talk", "저는 엄마하고 전화로 자주 얘기합니다."), ("을까요", "Shall we …?", "산호세 가서 한국 음식 먹을까요?"), ("찾다", "to withdraw (money); “to find”", "저는 보통 한 달에 한 번 돈을 찾습니다.")]
_CV_SINO = [("소", "(所) a place; an office", "세탁소; 주유소; 휴게소"), ("음", "(飮) drink; swallow", "음식; 음주; 음료수"), ("점", "(店) a shop; a store", "제과점; 백화점; 서점")]
_CV_ALL = _CV_TOWN + _CV_REST + _CV_SALON + _CV_LOAN + _CV_OTH
_CV_SKIP = ("머리 2", "아/어 주다", "아/어 드리다", "아서/어서", "을까요", "게", "얼마예요", "어서 오세요", "병", "잔", "인분", "시키다", "주문하다", "주다", "드리다", "김치", "김치찌개", "음식", "음료수", "받다", "맛있다", "맵다", "물", "갖다 주다",
            "가게", "시내", "서점", "백화점", "영화관", "은행", "돈", "기름", "넣다", "찾다", "사다", "등", "이야기", "얘기", "이야기하다", "걸리다", "맡기다", "약", "약국", "물건", "제과점", "빵집", "생일", "생신", "머리방", "그런데", "머리", "짙다", "유행", "남자", "여자", "어울리다", "샴푸",
            "샴푸하다", "염색", "염색하다", "예약", "예약하다", "파마", "파마하다", "커트", "마음에 들다", "쇼핑센터", "콜라", "맥주", "사이다", "신용카드", "계산서", "반찬", "배가 고프다", "김밥", "불고기", "비빔밥", "만두")
L10 = lesson(
    "Ch 7 · Core vocabulary",
    "주요 단어 · 몬트레이 시내에서 · 소 (所) · 음 (飮) · 점 (店)",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences are the book’s; the book gives no English for them). Pairs the book writes together (제과점/빵집, 생일/생신, 이야기/얘기(하다), 미용실/머리방, 시키다/주문하다, 주다/드리다) are on separate rows, and the grammar endings are written without the leading hyphen and parentheses: 게, 아/어 주다, 아/어 드리다, 아서/어서, 을까요. "
             "The few example sentences with digits or Latin letters are respelled in Hangul (1시 → 한 시, 2인분 → 이 인분, 4인분 → 사 인분), 머리 좀 아파요(ache) is shortened to 머리가 좀 아파요, and the second example of 머리 and the 제과점 example of 빵집 are mine."),
        card("Around town", "", tables=[vt(_CV_TOWN)]),
        card("At the restaurant", "", tables=[vt(_CV_REST)]),
        card("At the hair salon", "", tables=[vt([r if r[0] != "머리 2" else ("머리", r[1], r[2]) for r in _CV_SALON if r[0] != "머리 2"] + [("머리", "the head; hair", "머리 좀 잘라 주세요.")])]),
        card("Loan words", "", tables=[vt(_CV_LOAN)]),
        card("Other words", "Italicized English words in the book are grammatical terms, not the meaning of a Korean word.", tables=[vt(_CV_OTH)]),
        card("Sino-Korean vocabulary", "", tables=[vt(_CV_SINO)]),
    ],
    exercises=uniq(
        vocab_exercises([(k, _clean(e)) for k, e, _ in _CV_ALL if k != "머리 2"])
        + [mean("가게", "a store; a shop", ["a department store", "a bookstore", "a bank"]), mean("시내", "downtown", ["a shopping center", "a village", "a market"]), mean("영화관", "a movie theater", ["a coffee shop", "a bank", "a bookstore"]),
           mean("신용카드", "a credit card", ["a bill", "a menu", "cash"]), mean("계산서", "a bill; a check", ["a menu", "a side dish", "a credit card"]), mean("배가 고프다", "to be hungry", ["to be spicy", "to be tasty", "to be full"]),
           mean("마음에 들다", "to like; to be pleased with", ["to dislike", "to want", "to suit"]), mean("어울리다", "to suit; to go well with", ["to cut", "to like", "to dye"]), mean("유행", "a fashion; a trend", ["a plan", "a reservation", "a color"]),
           mean("머리", "the head; hair", ["a hand", "a face", "a body"]), mean("커트", "cut (hair)", ["perm", "a shampoo", "dyeing"]), mean("파마", "perm", ["cut (hair)", "a shampoo", "dyeing"]), mean("염색", "dyeing", ["cut (hair)", "a shampoo", "perm"]),
           mean("예약", "an appointment; a reservation", ["a bill", "a menu", "a cut"]), mean("돈", "money", ["gasoline", "medicine", "a thing"]), mean("기름", "oil; gasoline", ["money", "medicine", "a thing"]), mean("약", "medicine", ["money", "gasoline", "a thing"]),
           mean("넣다", "to insert; to put in", ["to withdraw", "to buy", "to entrust"]), mean("찾다", "to withdraw (money); to find", ["to put in", "to buy", "to entrust"]), mean("사다", "to buy", ["to put in", "to withdraw", "to entrust"]),
           mean("맡기다", "to entrust; to deposit", ["to buy", "to withdraw", "to put in"]), mean("걸리다", "to take (time)", ["to buy", "to withdraw", "to put in"]), mean("그런데", "by the way; however; but", ["therefore", "and then", "also"]),
           mean("김치", "kimchi", ["gimbap", "bulgogi", "bibimbap"]), mean("김밥", "gimbap; a seaweed rice roll", ["kimchi", "bulgogi", "bibimbap"]), mean("불고기", "bulgogi; Korean barbecued beef", ["kimchi", "gimbap", "bibimbap"]), mean("비빔밥", "bibimbap; mixed rice", ["kimchi", "gimbap", "bulgogi"]),
           mean("맥주", "beer", ["water", "cola", "soda pop"]), mean("콜라", "cola; Coke", ["beer", "water", "soda pop"]), mean("사이다", "soft drinks; soda pop", ["beer", "water", "cola"]), mean("물", "water", ["beer", "cola", "soda pop"]),
           mean("맵다", "to be spicy; to be hot", ["to be tasty", "to be hungry", "to be cold"]), mean("맛있다", "to be tasty; to be delicious", ["to be spicy", "to be hungry", "to be cold"]), mean("병", "a counter for bottles", ["a counter for glasses", "a counter for servings", "a counter for people"]),
           mean("잔", "a counter for a glass or cup", ["a counter for bottles", "a counter for servings", "a counter for people"]), mean("인분", "a serving", ["a bottle", "a glass", "a person"]), mean("남자", "a man; a male", ["a woman", "a child", "a customer"]), mean("여자", "a woman; a female", ["a man", "a child", "a customer"]),
           mean("물건", "a thing; goods", ["money", "medicine", "a store"]), mean("등", "and so on; et cetera", ["and then", "also", "only"]), mean("약국", "a pharmacy", ["a bank", "a bakery", "a bookstore"]), mean("은행", "a bank", ["a pharmacy", "a bakery", "a bookstore"]),
           mean("서점", "a bookstore", ["a bank", "a bakery", "a pharmacy"]), mean("백화점", "a department store", ["a bookstore", "a flower shop", "a shopping center"]), mean("쇼핑센터", "a shopping center", ["a department store", "a bank", "a pharmacy"]),
           mean("제과점", "a bakery", ["a bank", "a pharmacy", "a flower shop"]), mean("빵집", "a bakery", ["a bank", "a pharmacy", "a flower shop"]), mean("생일", "a birthday", ["a holiday", "a weekend", "a year"]), mean("이야기", "a chat; a talk; a story", ["a plan", "a thing", "a reason"]),
           mean("시키다", "to order (food or drinks)", ["to receive", "to give", "to bring"]), mean("주문하다", "to order (food or drinks)", ["to receive", "to give", "to bring"]), mean("받다", "to receive; to take", ["to give", "to order", "to bring"]), mean("주다", "to give; to offer", ["to receive", "to order", "to bring"]),
           mean("짙다", "to be dark; to be dense; to be rich", ["to be short", "to be long", "to be pretty"]), mean("음식", "food", ["a drink", "a bill", "a side dish"]), mean("음료수", "beverages; drinks", ["food", "a bill", "a side dish"]), mean("반찬", "a side dish", ["a drink", "a bill", "food"]),
           mean("샴푸", "a shampoo", ["a perm", "a cut", "dyeing"]), mean("염색하다", "to dye", ["to shampoo", "to cut", "to have a perm"]), mean("예약하다", "to make a reservation", ["to cancel", "to pay", "to order"]), mean("파마하다", "to have a perm", ["to shampoo", "to dye", "to cut"]),
           mean("샴푸하다", "to shampoo", ["to dye", "to cut", "to have a perm"]), mean("이야기하다", "to have a chat; to have a talk", ["to make a plan", "to give", "to buy"]),
           M("What does the Sino-Korean syllable 소 (所) mean?", "a place; an office", ["a shop", "drink", "food"], "주유소, 세탁소, 휴게소."), M("What does the Sino-Korean syllable 음 (飮) mean?", "drink; swallow", ["a shop", "a place", "a ball"], "음식, 음주, 음료수."),
           M("What does the Sino-Korean syllable 점 (店) mean?", "a shop; a store", ["a place", "drink", "a ball"], "제과점, 백화점, 서점."), M("What does 아/어 주다 express?", "The sense of providing service", ["A wish", "A reason", "A suggestion"], "문 좀 열어 주세요."),
           M("What does 아서/어서 mean as a cause?", "and thus; so; because", ["and then", "if", "although"], "아침을 안 먹어서 배가 고파요."), M("What does 을까요 mean?", "Shall we …?", ["Please do", "I want to", "Let’s"], "산호세 가서 한국 음식 먹을까요?")]
    ),
)

UNIT = unit("Semester 1 · Unit 2 · Chapter 7: Downtown Monterey (몬트레이 시내에서)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10])
