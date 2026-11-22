"""Unit 25: KBC Semester 1, Unit 5, Chapter 18 - Shopping (물건 사기).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 5, Student's Edition (2022).
Audio, video clips, photos, pictures, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg


def _fk(items, fn, label, wrong):
    """one question per item: which is the <label> form of <item>?"""
    out = []
    for it, m in items:
        c = fn(it)
        ws = list(dict.fromkeys(x for x in wrong(it) if x != c))[:3]
        out.append(M(f"What is the {label} form of {it} ({m})?", c, ws, f"{it} → {c}."))
    return out


# ---- the core vocabulary of Chapter 18 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_STORE = [
    ("고객", "(顧客) a customer; a patron", "저희 백화점을 방문해 주신 고객 여러분, 감사합니다."),
    ("교환", "(交換) exchange; trade (~하다: to exchange; to trade)", "어제 산 바지가 마음에 안 들어요. 그래서 오늘 교환할 거예요."),
    ("구매", "(購買) purchase (~하다: to purchase; to buy)", "이번 백화점 세일 때 컴퓨터를 구매했습니다."),
    ("구입", "(購入) purchase (~하다: to purchase; to buy)", "신용카드로 겨울 코트를 하나 구입했어요."),
    ("매장", "(賣場) a shop; a store", "요즘 백화점 스포츠 매장에서 운동복을 세일해요."),
    ("사은품", "(謝恩品) a free gift; a promotional gift", f"저희 백화점에서 {_kn(100000)} 원 이상을 구매하시면 사은품을 드립니다."),
    ("상품권", "(商品券) a gift certificate", "생일 선물로 백화점 상품권을 받았어요."),
    ("신상품", "(新商品) newly released products", "이번 세일에서 봄 신상품은 할인을 하지 않습니다."),
    ("영수증", "(領收證) a receipt", "백화점에서 물건을 사고 영수증을 꼭 받으세요."),
    ("~용품", "(用品) ~supplies; ~ware; ~goods; “items used for~”", "스포츠용품 매장에서 스노우 보드를 샀어요."),
]
_CV_CAT = [
    ("가구", "(家具) furniture", f"가구 매장에서 침대를 {sino(20)} 퍼센트 할인 판매합니다."),
    ("가전제품", "(家電製品) a home appliance; “home electric product”", "가전제품을 사러 백화점에 갔어요."),
    ("숙녀복", "(淑女服) women’s apparel", "숙녀복 매장에서 세일하는 블라우스를 하나 샀어요."),
    ("신사복", "(紳士服) men’s apparel", "우리 백화점 신사복 매장에 가서 양복 좀 구경할까?"),
    ("의류 / ~복", "(衣類/服) clothing; apparel", "백화점 의류 매장에 겨울 코트를 사려는 사람들이 많아요."),
    ("잡화", "(雜貨) general merchandise; miscellaneous goods", "백화점에서는 여러 가지 잡화를 판매합니다."),
    ("화장품", "(化粧品) cosmetics", "여자 친구 생일 선물로 화장품을 샀습니다."),
]
_CV_APP = [
    ("냉장고", "(冷藏庫) a refrigerator", "야채는 냉장고에 넣으세요."),
    ("다리미", "an iron", "군복을 다리미로 다립니다."),
    ("선풍기", "(扇風機) an electric fan", "더울 때는 선풍기를 켭니다."),
    ("세탁기", "(洗濯機) a washer", "빨래를 세탁기에 넣었어요."),
    ("식기세척기", "(食器洗滌器) a dishwasher", "설거지를 식기세척기로 했어요."),
    ("전기밥솥", "an electric rice cooker", "새로 산 전기밥솥으로 밥을 하니까 참 맛있어요."),
    ("전자레인지", "a microwave oven; “electronic range”", "전자레인지로 팝콘을 만들 수 있습니다."),
    ("진공청소기", "(眞空淸掃機) a (vacuum) cleaner", "새로 산 진공청소기가 고장 났어요."),
]
_CV_PAY = [
    ("무이자", "(無利子) (no) interest; (free of) interest", f"요즘 은행에서 일 년 동안 무이자로 돈을 빌릴 수 있습니다."),
    ("일시불", "(一時拂) a lump-sum payment; one-time payment", "할인을 해 주어서 컴퓨터를 일시불로 샀어요."),
    ("할부", "(割賦) payment in installments", "자동차를 할부로 샀어요."),
]
_CV_PROD = [
    ("감자", "a potato", "김 선생님은 감자 요리는 다 좋아해요."),
    ("공짜(로)", "free of charge", "학교 앞 서점에서 책을 사면 공짜로 볼펜을 줍니다."),
    ("당근", "a carrot", "당근은 비타민 에이가 많은 채소예요."),
    ("배 (pear)", "a pear", "한국 배는 아주 달고 맛있어요."),
    ("복숭아", "a peach", "저는 복숭아 알레르기가 있어서 복숭아를 못 먹어요."),
    ("수박", "a watermelon", "여름에는 시원한 수박이 참 맛있어요."),
    ("시금치", "spinach", "저는 아침마다 시금치 샐러드를 먹어요."),
    ("시장", "(市場) an (open-air) market", "저는 시장 구경하는 것을 좋아해요."),
    ("신선하다", "to be fresh", "저희 가게 과일은 언제나 신선해요."),
    ("야채 / 채소", "a vegetable", "신선한 야채 샐러드를 먹고 싶어요."),
    ("양파", "an onion", "냄새 때문에 저는 양파를 잘 안 먹어요."),
    ("오이", "a cucumber", "오이로도 김치를 만들 수 있어요."),
    ("옥수수", "corn", "시장에서 옥수수 한 봉지를 샀어요."),
    ("파", "a green onion", "우리 딸은 파를 잘 안 먹어요."),
]
_CV_CNT = [
    ("~ 단", "a bundle (of spinach, green onions, etc.)", f"파는 한 단에 오백 원입니다."),
    ("봉지", "(封紙) a bag", "비닐 봉지에 이 토마토 좀 넣어 주세요."),
    ("상자", "(箱子) a box", "배를 한 상자 샀어요."),
    ("~ 송이", "a bunch (of grapes, bananas etc.); counter for flowers or mushrooms", f"포도 열 송이에 오천 원입니다."),
    ("~ 통", "counter for watermelons, heads of cabbage, etc.", f"요즘 수박 값이 비싸요. 한 통에 {_kn(15000)} 원이에요."),
]
_CV_LOAN = [
    ("가스레인지", "a gas stove; “gas range”", "가스레인지가 고장 나서 요리를 못 해요."),
    ("박스", "a box", "과일을 박스로 사면 더 싸요."),
    ("에어컨", "an air conditioner", "에어컨을 사서 이번 여름은 시원하게 보내겠어요."),
    ("토마토", "a tomato", "이 토마토는 아주 싱싱하네요."),
]
_CV_OTH = [
    ("똑같다 / 같다", "to be (exactly) the same as", "아내와 저는 똑같은 시계가 있어요."),
    ("-기로 하다", "to decide to", "다음 주에 친구랑 쇼핑을 가기로 했어요."),
    ("남성", "(男性) male; a man", "남성 의류매장에서 와이셔츠를 샀습니다."),
    ("되다", "to be possible; to be okay", "신용카드도 됩니까?"),
    ("~만큼", "(as …) as ~", "저는 형만큼 많이 먹어요."),
    ("배달", "(配達) delivery (~하다: to deliver)", "큰 가전제품은 무료로 배달해 드립니다."),
    ("보증", "(保證) warranty; guarantee (~하다: to guarantee)", f"이 물건의 보증기간은 일 년입니다."),
    ("비슷하다", "to be similar", "이 모자와 저 모자는 모양이 비슷해요."),
    ("생활", "(生活) life; living (~하다: to live)", "지하 생활용품 코너에서 샴푸와 린스를 구입하세요."),
    ("아동", "(兒童) a child; boys and girls; preschoolers", f"백화점 {sino(6)} 층에서 아동복을 판매합니다."),
    ("아저씨", "mister; sir; “an uncle”", "식당 주인 아저씨가 아주 친절해요."),
    ("아주머니 / 아줌마", "a lady; a woman; “an aunt”", "제가 다니는 과일 가게 주인 아주머니는 서비스를 많이 줍니다."),
    ("여성", "(女性) female; a woman", "여성 의류코너에서 치마와 스웨터를 샀습니다."),
    ("-(으)ㄹ게요", "will", "제가 식품점에서 야채를 사 올게요."),
    ("주방", "(廚房) a kitchen", "토요일에 백화점에서 주방용품을 할인 판매합니다."),
    ("품질", "(品質) quality of a product", "백화점 물건은 보통 품질이 좋아요."),
    ("훨씬", "by far", "시장 물건 값이 백화점보다 훨씬 더 쌉니다."),
]
_CV_SINO = [("전", "(電) electric(ity); lighting", "전기, 전화, 전선")]
_ALL = {r[0]: r for r in _CV_STORE + _CV_CAT + _CV_APP + _CV_PAY + _CV_PROD + _CV_CNT + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"백화점": "a department store (mine)", "넥타이": "a necktie (mine)", "색": "a color (mine)", "파란색": "blue (mine)", "고객 센터": "the customer center (mine)", "식당": "a restaurant; a dining hall (mine)", "식품": "food; groceries (mine)", "스포츠": "sports (mine)", "생활용품": "daily necessities (mine)", "주방용품": "kitchenware (mine)",
          "판매하다": "to sell (mine)", "핸드백": "a handbag (mine)", "운동화": "sports shoes; sneakers (mine)", "양복": "a (men’s) suit (mine)", "청소기": "a vacuum cleaner (mine)", "색깔": "a color (mine)", "회색": "gray (mine)", "가격": "a price (mine)", "보증 기간": "a warranty period (mine)", "냉장고": "a refrigerator",
          "전기": "electricity; “electric energy”", "전자": "electron; electronics; “electric son”", "전선": "an electric wire; a cord (mine)", "전화기": "a telephone (mine)", "전구": "a light bulb (mine)", "전차": "a streetcar; an electric train (mine)", "전파": "radio waves (mine)", "전력": "electric power (mine)",
          "과일 가게": "a fruit store (mine)", "주인": "an owner (mine)", "깎다": "to cut; to give a discount (mine)", "포도": "a grape (mine)", "계절 과일": "seasonal fruit (mine)", "주문": "an order (mine)", "할인": "a discount (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)


# ================================================================== Objectives and the Sino-Korean syllable 전
_JEON = [("전기", "electricity; “electric energy”"), ("전자", "electron; electronics; “electric son”"), ("전선", "an electric wire; a cord (mine; 線 = a line, a cord)"), ("전화기", "a telephone (mine)"), ("전구", "a light bulb (mine; 球 = a ball, a globe)"),
         ("전차", "a streetcar; an electric train (mine)"), ("전파", "radio waves (mine; 波 = wave)"), ("전력", "electric power (mine; 力 = power)"), ("전화", "a telephone; a telephone call (the book’s example in the Core Vocabulary; English mine)")]
L1 = lesson(
    "Ch 18 · What the chapter teaches and the Sino-Korean syllable 전",
    "물건 사기 · 백화점 · 시장 · 전 (電) · 전기 · 전자 · 전화기",
    requires=[],
    cards=[
        card("What Chapter 18 teaches (물건 사기)",
             "Chapter 18, “Shopping”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: inquire about basic information when shopping for items at a department store and market; ask for a refund and exchange items; place an order and request a delivery; and negotiate and bargain for a discount.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; indicating the object in a mutual relationship with the subject; ~만큼 (as … as); -기로 하다 (to decide to); -(으)ㄹ게요 (will); and the Sino-Korean syllable 전 (電)."),
        card("Sino-Korean in use: 전 (電)",
             "This Sino-Korean syllable means electricity or electric, as in 전기 (electricity; “electric energy”) and 전자 (electron; electronics; “electric son”). The upper part of the Chinese character depicts rain. The lower part depicts lightning, or the source of natural electricity. The book asks you to guess the meaning of 전선, 전화기, 전구, 전차, 전파 and 전력, with the hints 선 (線): a line, a cord; 구 (球): a ball, a globe; 파 (波): wave; 력 (力): power. The answers are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _JEON], say=[0])]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board activities) and Activity 3 (the “Peril!” game, which the teacher starts) are picture or game activities."),
    ],
    exercises=uniq(
        _tr(_JEON)
        + [M(f"Which word means “{b.split(';')[0].split(' (')[0]}”?", a, [x for x, _ in _JEON if x != a][:3], f"{a}: {b}.") for a, b in _JEON[:8] if b.split(';')[0].split(' (')[0] not in ("electricity", "electron")]
        + [M("What does the Sino-Korean syllable 전 (電) mean?", "electricity; electric", ["a gathering", "not; no", "a type"], "전기, 전자, 전화."), M("What does 전자 literally mean?", "“electric son”", ["“electric energy”", "“electric line”", "“electric power”"], "전자 = electron; electronics."),
           M("What does 전기 literally mean?", "“electric energy”", ["“electric son”", "“electric line”", "“electric power”"], "전기 = electricity."), M("What does 선 (線) mean?", "a line; a cord", ["a ball", "a wave", "power"], "전선 = an electric wire."),
           M("What does 구 (球) mean?", "a ball; a globe", ["a line", "a wave", "power"], "전구 = a light bulb."), M("What does 파 (波) mean?", "wave", ["a line", "a ball", "power"], "전파 = radio waves."), M("What does 력 (力) mean?", "power", ["a line", "a ball", "wave"], "전력 = electric power."),
           read_q("전기"), read_q("전자"), read_q("전화기"), read_q("전구"), read_q("전력")]
    ),
)

# ================================================================== Topic A
_A_DLG = [
    ("점원", "어서 오세요. 어떻게 도와 드릴까요?", "Welcome. How may I help you?"),
    ("태민", "제가 어제 이 매장에서 넥타이를 샀어요. 그런데 색이 마음에 안 들어서 바꾸고 싶어요.", "I bought a necktie at this shop yesterday. But I don’t like the color, so I want to exchange it."),
    ("점원", "그러세요? 영수증 있으세요?", "I see. Do you have the receipt?"),
    ("태민", "네. 여기 있어요.", "Yes. Here it is."),
    ("점원", "감사합니다. 무슨 색으로 교환해 드릴까요?", "Thank you. What color would you like to exchange it for?"),
    ("태민", "파란색으로 바꿔 주세요.", "Please change it to blue."),
    ("점원", "네. 여기 파란색 넥타이 있습니다. 또 필요한 것 없으세요?", "Yes. Here is a blue necktie. Do you need anything else?"),
    ("태민", "상품권도 한 장 주세요.", "Please give me a gift certificate, too."),
    ("점원", "고객님, 상품권은 일 층 고객 센터에서 판매합니다.", "Customer, gift certificates are sold at the customer center on the first floor."),
    ("태민", "그래요? 감사합니다.", "Is that so? Thank you."),
]
_A_WORDS = ["가구", "가전제품", "고객", "교환", "구매", "구입", "남성", "매장", "사은품", "상품권", "생활", "숙녀복", "신사복", "신상품", "아동", "여성", "영수증", "~용품", "의류 / ~복", "잡화", "주방", "화장품"]
_FLOORS = [["7층", "칠 층", "식당", "restaurants"], ["6층", "육 층", "가전제품, 가구", "home appliances, furniture"], ["5층", "오 층", "주방용품, 생활용품", "kitchenware, daily necessities"], ["4층", "사 층", "스포츠, 아동 의류", "sports, children’s clothing"],
           ["3층", "삼 층", "남성 의류, 신사복", "men’s clothing (men’s apparel)"], ["2층", "이 층", "여성 의류, 숙녀복", "women’s clothing (women’s apparel)"], ["1층", "일 층", "잡화, 화장품", "general merchandise, cosmetics"], ["지하 1층", "지하 일 층", "식품", "food; groceries"]]
_SITU = [("이번 주말에 집에서 생일 파티를 할 거예요. 그래서 여러 가지 음식을 요리해야 해요. 또 청소기를 며칠 전에 샀는데 고장이 났어요. 그래서 다른 청소기로 교환하고 싶어요. 그리고 지금 세일하니까 핸드백을 하나 사고 싶어요.",
          "This weekend I am going to have a birthday party at home. So I have to cook various foods. Also, I bought a vacuum cleaner a few days ago, but it broke. So I want to exchange it for another vacuum cleaner. And since there is a sale now, I want to buy a handbag.", "주성연 씨"),
         ("이번 주말에 친구들과 농구를 합니다. 그래서 운동화를 사고 싶습니다. 그리고 내일이 여자 친구 생일이에요. 그래서 생일 선물로 엠피쓰리 플레이어를 사주고 싶습니다. 또 이번 봄에 대학교에 들어가니까 양복도 사고 싶어요.",
          "This weekend I am going to play basketball with my friends. So I want to buy sports shoes. And tomorrow is my girlfriend’s birthday. So I want to buy her an MP3 player as a birthday present. Also, since I am entering university this spring, I want to buy a suit, too.", "김주환 씨")]
L2 = lesson(
    "Ch 18 · Topic A: Please exchange this for a blue tie",
    "파란색 넥타이로 바꿔 주세요 · 백화점 · 매장 · 영수증 · 상품권 · 층별 안내",
    requires=[],
    cards=[
        card("Topic A: Please exchange this for a blue tie (파란색 넥타이로 바꿔 주세요)",
             "Taemin is talking with an employee at the men’s apparel section in a department store. (The English is mine; the book gives none. The book writes 1층; it is spelled 일 층.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional endings are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Follow-up 2 (Reading): the store directory (층별 안내)",
             "The book shows the directory of a department store (하나 백화점) as a picture and gives two situations, asking which floors the two people need to go to. The directory is read from the picture; the English is mine.",
             tables=[table(["Floor", "Floor (read)", "Departments", "Meaning (mine)"], _FLOORS, say=[1, 2])]),
        card("The situations and the floors (mine)",
             "The situations are the book’s (the book writes MP3, spelled 엠피쓰리 here); the English and the answers are mine, from the directory above.",
             examples=[e for ko, en, who in _SITU for e in passage([(who, who)] + [(s.strip() + ".", "") for s in []])][:0] + passage([(ko, en) for ko, en, who in _SITU]),
             tables=[table(["Person", "Need", "Floor (mine)"], [["주성연 씨", "cooking food → groceries", "지하 일 층"], ["주성연 씨", "exchange a vacuum cleaner → home appliances", "육 층"], ["주성연 씨", "buy a handbag → general merchandise", "일 층"],
                                                      ["김주환 씨", "sports shoes → sports", "사 층"], ["김주환 씨", "an MP3 player → home appliances", "육 층"], ["김주환 씨", "a suit → men’s apparel", "삼 층"]], say=[0])]),
        card("Activities left out",
             "The SMART Board activities, Follow-up 1 (listening to three short dialogs at a department store and checking exchange or refund) and Follow-up 3 (listening to three department store announcements and writing the sale items and free gifts in English) are audio or computer activities. The Useful Links (Shinsegae, Galleria and Hyundai department stores) are websites."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if not w.startswith("~")]))
        + _tr(_strip(_A_DLG))
        + [M("What did Taemin buy yesterday?", "A necktie", ["A tie pin", "A shirt", "A gift certificate"], "넥타이를 샀어요."), M("Why does Taemin want to exchange it?", "He doesn’t like the color", ["It is too expensive", "It is broken", "It is too small"], "색이 마음에 안 들어서."),
           M("What does the clerk ask for?", "The receipt", ["The credit card", "The ID", "The ticket"], "영수증 있으세요?"), M("What color does Taemin want?", "Blue", ["Red", "Gray", "Black"], "파란색으로 바꿔 주세요."),
           M("What else does Taemin ask for?", "A gift certificate", ["A receipt", "A bag", "A discount"], "상품권도 한 장 주세요."), M("Where are gift certificates sold?", "At the customer center on the first floor", ["On the second floor", "At the men’s section", "In the basement"], "일 층 고객 센터에서 판매합니다."),
           M("Which floor is the restaurant on?", "The 7th floor", ["The 1st floor", "The 4th floor", "The basement"], "칠 층 식당."), M("Which floor sells home appliances and furniture?", "The 6th floor", ["The 5th floor", "The 4th floor", "The 3rd floor"], "육 층 가전제품, 가구."),
           M("Which floor has men’s apparel?", "The 3rd floor", ["The 2nd floor", "The 4th floor", "The 1st floor"], "삼 층 남성 의류, 신사복."), M("Which floor has women’s apparel?", "The 2nd floor", ["The 3rd floor", "The 1st floor", "The 4th floor"], "이 층 여성 의류, 숙녀복."),
           M("Which floor has cosmetics?", "The 1st floor", ["The 2nd floor", "The 7th floor", "The basement"], "일 층 잡화, 화장품."), M("Where is the food department?", "The basement (first basement floor)", ["The 1st floor", "The 7th floor", "The 6th floor"], "지하 일 층 식품."),
           M("Which floor does Jusungyeon go to for the vacuum cleaner?", "The 6th floor", ["The 1st floor", "The 3rd floor", "The 4th floor"], "청소기 = home appliance: 육 층."), M("Which floor does Kimjuhwan go to for sports shoes?", "The 4th floor", ["The 3rd floor", "The 6th floor", "The 1st floor"], "운동화 = sports: 사 층."),
           F("어떻게 ___ 드릴까요? (help)", "도와", ["가", "봐"], "돕다 → 도와 드리다."), F("무슨 색으로 ___ 드릴까요? (exchange)", "교환해", ["구매해", "판매해"], "교환하다 = to exchange."), F("상품권은 일 층 고객 센터에서 ___합니다. (sell)", "판매", ["교환", "구매"], "판매하다 = to sell."),
           F("고객님, ___ 있으세요? (receipt)", "영수증", ["사은품", "상품권"], "영수증 = a receipt."), F("백화점에서 십만 원 이상 구매하시면 ___을 드립니다. (a free gift)", "사은품", ["영수증", "고객"], "사은품 = a free gift."), F("가구와 ___은 육 층에 있어요. (home appliances)", "가전제품", ["화장품", "신상품"], "가전제품 = home appliances."),
           read_q("백화점"), read_q("영수증"), read_q("상품권"), read_q("교환해 드릴까요"), read_q("고객 센터")]
    ),
)

# ================================================================== Activities A
_MATCH10 = [("가전제품", "home appliances"), ("아동", "a child"), ("교환하다", "to exchange"), ("주방용품", "kitchenware"), ("신사복", "men’s apparel"), ("구매하다", "to purchase"), ("사은품", "a free gift (with purchase)"), ("판매하다", "to sell"), ("상품권", "a gift certificate"), ("영수증", "a receipt")]
_QA = [
    ("작성자: 김선환, 작성 일시: 삼월 팔일 오후 네 시 삼십이 분", "Writer: Kim Seonhwan; written on March 8 at 4:32 p.m."),
    ("지난 주말에 서울에 있는 아시아 백화점에서 넥타이를 하나 구입했습니다. 그런데 디자인이 조금 마음에 안 드네요. 환불을 받고 싶은데, 저희 집이 부산이에요. 이 넥타이를 부산에 있는 아시아 백화점에서 환불을 받을 수 있습니까?", "Last weekend I bought a necktie at the Asia Department Store in Seoul. But I don’t like the design a little. I want a refund, but my home is in Busan. Can I get a refund for this necktie at the Asia Department Store in Busan?"),
    ("작성자: 이선자, 작성 일시: 삼월 팔일 오후 여섯 시 팔 분", "Writer: Lee Seonja; written on March 8 at 6:08 p.m."),
    ("어제 아버지 생신 선물로 구두를 샀습니다. 그런데 구두가 좀 커서 다른 구두로 교환하고 싶어요. 어떻게 해야 합니까?", "Yesterday I bought dress shoes as a birthday present for my father. But the shoes are a little big, so I want to exchange them for other shoes. What should I do?"),
    ("작성자: 길용우, 작성 일시: 삼월 팔일 오후 아홉 시 이십팔 분", "Writer: Gil Yongwoo; written on March 8 at 9:28 p.m."),
    ("얼마 전에 친구에게서 아시아 백화점 상품권을 선물 받았습니다. 이 상품권을 환불받고 싶어요. 상품권도 환불받을 수 있어요?", "Not long ago I received an Asia Department Store gift certificate as a present from a friend. I want a refund for this gift certificate. Can I get a refund for a gift certificate, too?"),
]
_ANS = [
    ("영수증이 있으면 상품권도 환불이 가능합니다. 구입한 날로부터 육십 일 후까지 환불받으실 수 있습니다.", "If you have the receipt, a refund is also possible for a gift certificate. You can get a refund until 60 days after the day of purchase."),
    ("교환은 아무 곳에서나 하실 수 있습니다. 하지만 환불은 구입하신 곳에서만 받으실 수 있습니다.", "You can exchange at any place. But you can get a refund only at the place where you bought it."),
    ("아직 신지 않으셨으면 칠 일 이내에 교환이나 환불받으실 수 있습니다. 하지만 이미 신으셨으면 환불이나 교환하실 수 없습니다.", "If you have not worn them yet, you can get an exchange or a refund within 7 days. But if you have already worn them, you cannot get a refund or an exchange."),
]
_QA_W = [("환불", "a refund (mine)"), ("디자인", "design (mine)"), ("구두", "dress shoes (mine)"), ("생신", "a birthday (honorific) (mine)"), ("선물", "a present; a gift (mine)"), ("신다", "to wear (shoes) (mine)"), ("이미", "already (mine)"), ("이내", "within (mine)"), ("가능", "possibility (mine)")]
L3 = lesson(
    "Ch 18 · Activities A: matching words and customer questions to a department store",
    "교환 · 환불 · 구매하다 · 판매하다 · 영수증 · 상품권 · 아시아 백화점",
    requires=[],
    cards=[
        card("Activity 1 (Reading): match the Korean words with their English meanings",
             "The book gives ten Korean words in the left column and ten English meanings in the right column in a different order and asks you to draw lines between them. The pairs below are the book’s words with their meanings (the answers to the matching are mine).",
             tables=[ktable(_MATCH10)]),
        card("Activity 2 (Reading): customer questions on a department store’s website",
             "The book gives three customer questions from the website of a department store called 아시아백화점, and three answers in a box; match each question with the appropriate response. The texts are the book’s (the dates and times are spelled out in Hangul); the English is mine.",
             examples=passage(_QA)),
        card("The three answers",
             "The book’s answers 1, 2 and 3 (the English is mine):",
             examples=passage(_ANS)),
        card("The matching (mine)",
             "The book leaves the answers blank; these are my answers.",
             tables=[table(["Question", "Answer"], [["Kim Seonhwan (refund for a necktie, home in Busan)", "Answer 2: exchange at any place, but a refund only where you bought it"], ["Lee Seonja (exchange shoes that are too big)", "Answer 3: within 7 days if not worn yet"], ["Gil Yongwoo (refund for a gift certificate)", "Answer 1: possible with the receipt, until 60 days after purchase"]])]),
        card("Words of the questions and answers",
             "These meanings are mine (the book does not gloss them).",
             tables=[ktable(_QA_W)]),
        card("Activities left out",
             "Activity 1 (b) (listening to four dialogs at a department store and checking purchase, exchange or refund) is an audio activity; Activity 3 (visiting the Shinsegae website and designing a newspaper advertisement for a spring sale on a flip chart, with pairs, a wall display and a star rating) is a website, partner and class activity."),
    ],
    exercises=uniq(
        vocab_exercises(_MATCH10) + _tr(_QA + _ANS + _QA_W)
        + [M("Where did Kim Seonhwan buy the necktie?", "At the Asia Department Store in Seoul", ["At the Asia Department Store in Busan", "At a market", "On the internet"], "서울에 있는 아시아 백화점."), M("What does Kim Seonhwan want?", "A refund", ["An exchange", "A discount", "A gift certificate"], "환불을 받고 싶은데."),
           M("What did Lee Seonja buy?", "Dress shoes as a present for her father", ["A necktie", "A gift certificate", "A bag"], "아버지 생신 선물로 구두를 샀습니다."), M("What is wrong with the shoes?", "They are a little big", ["They are broken", "They are old", "They are dirty"], "구두가 좀 커서."),
           M("What did Gil Yongwoo receive from a friend?", "A gift certificate", ["A necktie", "A ticket", "A receipt"], "상품권을 선물 받았습니다."), M("Which answer fits Kim Seonhwan’s question?", "A refund only at the place where you bought it", ["Within 7 days if not worn", "With the receipt for 60 days", "Not possible"], "환불은 구입하신 곳에서만 받으실 수 있습니다."),
           M("Which answer fits Lee Seonja’s question?", "An exchange within 7 days if not worn", ["A refund only where you bought it", "With the receipt for 60 days", "Not possible"], "아직 신지 않으셨으면 칠 일 이내에."), M("Until when can the gift certificate be refunded?", "Until 60 days after the purchase", ["Until 7 days after", "Until a year after", "It cannot be refunded"], "육십 일 후까지."),
           F("교환은 아무 곳에서___ 하실 수 있습니다. (at any place)", "나", ["이나", "도"], "곳에서나 = at any place (나 added after 에서)."), F("환불은 구입하신 곳에서___ 받으실 수 있습니다. (only)", "만", ["도", "나"], "에서만 = only at."), F("이미 신으셨으면 환불이나 교환하실 수 ___. (cannot)", "없습니다", ["있습니다", "합니다"], "수 없다 = cannot."),
           read_q("환불을 받고 싶어요"), read_q("아시아 백화점"), read_q("구두가 좀 커서"), read_q("상품권도 환불"), read_q("영수증이 있으면")]
    ),
)

# ================================================================== Topic B
_B_DLG = [
    ("손님", "냉장고 좀 보여주세요.", "Please show me a refrigerator."),
    ("판매원", "어떤 냉장고를 찾으세요?", "What kind of refrigerator are you looking for?"),
    ("손님", "저희 집 냉장고가 너무 작아서요. 좀 큰 것이 필요해요.", "Our refrigerator at home is too small. I need a bigger one."),
    ("판매원", "그럼 이 냉장고는 어떠세요?", "Then how about this refrigerator?"),
    ("손님", "좋은데, 색깔이 저희 집 냉장고하고 똑같아요. 다른 색깔은 없어요?", "It’s good, but the color is the same as our refrigerator at home. Don’t you have another color?"),
    ("판매원", "그럼, 이 회색 냉장고는 어떠세요?", "Then how about this gray refrigerator?"),
    ("손님", "아, 네, 좋아요. 품질은 어때요?", "Oh, yes, that’s good. How is the quality?"),
    ("판매원", "품질은 아주 좋습니다. 그리고, 품질 보증 기간도 일 년입니다.", "The quality is very good. And the quality warranty period is also one year."),
    ("손님", "가격은 얼마예요?", "How much is the price?"),
    ("판매원", f"{_kn(1200000)} 원입니다. 원하시면 무이자 할부로도 구입하실 수 있습니다.", "It is 1,200,000 won. If you wish, you can also buy it with an interest-free installment plan."),
    ("손님", "그래요? 현금이나 일시불로 사면 할인이 좀 돼요?", "Is that so? If I buy with cash or a lump-sum payment, can I get a discount?"),
    ("판매원", "죄송합니다, 손님. 이 제품은 할인이 안 됩니다. 그렇지만, 배달을 무료로 해 드릴게요.", "I’m sorry, customer. This product cannot be discounted. But I will deliver it for free."),
    ("손님", "좋아요. 그럼 일시불로 해 주세요.", "All right. Then please make it a lump-sum payment."),
]
_B_WORDS = ["가스레인지", "냉장고", "다리미", "똑같다 / 같다", "되다", "무이자", "배달", "보증", "비슷하다", "선풍기", "세탁기", "식기세척기", "에어컨", "-(으)ㄹ게요", "일시불", "전기밥솥", "전자레인지", "진공청소기", "품질", "할부"]
L4 = lesson(
    "Ch 18 · Topic B: The quality of the product is very good",
    "품질은 아주 좋습니다 · 냉장고 · 가전제품 · 무이자 할부 · 일시불 · 무료 배달",
    requires=[],
    cards=[
        card("Topic B: The quality of the product is very good (품질은 아주 좋습니다)",
             "A customer is talking with a salesperson about buying a refrigerator at a home appliance store. (The English is mine; the book gives none. The book writes 120만 원 and 1년; they are spelled out here.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened. The book shows pictures of the home appliances 전자레인지, 가스레인지, 진공청소기, 세탁기, 전기밥솥, 다리미, 식기세척기 and 선풍기; the pictures are left out.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Activities left out",
             "The SMART Board activities, the sentence strips of the Presentation Activity (partners arrange the strips in a logical order) and Follow-up 2 (listening to four conversations at a home appliance store and filling in a table about payment, discount, warranty or delivery) are audio, computer, partner or class activities. Follow-up 1 is in the next lesson. The Sino-Korean syllable 전 is in the first lesson of the chapter."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("-", "~")) and "/" not in w]))
        + _tr(_strip(_B_DLG))
        + [M("What does the customer want to buy?", "A refrigerator", ["A washer", "A microwave", "A fan"], "냉장고 좀 보여주세요."), M("Why does the customer need a new refrigerator?", "The one at home is too small", ["The one at home is broken", "The one at home is old", "It is too big"], "저희 집 냉장고가 너무 작아서요."),
           M("What is the problem with the first refrigerator?", "Its color is the same as the one at home", ["It is too small", "It is too expensive", "It is broken"], "색깔이 저희 집 냉장고하고 똑같아요."), M("What color is the second refrigerator?", "Gray", ["White", "Blue", "Black"], "회색 냉장고."),
           M("How long is the warranty?", "One year", ["Two years", "Six months", "Ten years"], "보증 기간도 일 년."), M("How much is the refrigerator?", "1,200,000 won", ["120,000 won", "2,100,000 won", "12,000,000 won"], "백이십만 원."),
           M("What payment option does the salesperson mention?", "An interest-free installment plan", ["A lump sum only", "A bank transfer", "A check"], "무이자 할부로도 구입하실 수 있습니다."), M("Can the customer get a discount?", "No, this product cannot be discounted", ["Yes, 10%", "Yes, if he pays cash", "Yes, if he is a student"], "이 제품은 할인이 안 됩니다."),
           M("What does the salesperson offer instead?", "Free delivery", ["A free gift", "A gift certificate", "A longer warranty"], "배달을 무료로 해 드릴게요."), M("How does the customer decide to pay?", "A lump-sum payment", ["Installments", "Cash", "A credit card"], "일시불로 해 주세요."),
           F("저희 집 냉장고하고 ___. (the same)", "똑같아요", ["달라요", "작아요"], "똑같다 = to be exactly the same."), F("품질 ___ 기간도 일 년입니다. (warranty)", "보증", ["배달", "할부"], "보증 = warranty."), F("원하시면 무이자 ___로도 구입하실 수 있습니다. (installments)", "할부", ["일시불", "배달"], "할부 = payment in installments."),
           F("이 제품은 할인이 안 ___. (is not possible)", "됩니다", ["합니다", "갑니다"], "되다 = to be possible."), F("배달을 무료로 해 드___요. (I will)", "릴게", ["릴까", "릴지"], "-(으)ㄹ게요: 드리다 → 드릴게요."), F("현금이나 ___로 사면 할인이 좀 돼요? (lump-sum payment)", "일시불", ["할부", "무이자"], "일시불 = a lump-sum payment."),
           read_q("품질은 아주 좋습니다"), read_q("무이자 할부"), read_q("일시불"), read_q("전자레인지"), read_q("식기세척기")]
    ),
)

# ================================================================== Activities B
_WASH = [
    ("세탁기 대 할인", "A big sale on washers"), (f"{sino(25)} 퍼센트 할인 판매!", "On sale at 25% off!"), ("무이자 할부 육 개월", "Interest-free installments for 6 months"),
    ("품질 보증 기간 일 년", "Quality warranty period: one year"), ("품질 보증기간 안에 고장이 나면 무료로 고쳐 드립니다.", "If it breaks within the quality warranty period, we will repair it for free."),
    (f"서울 시내 {sino(24)} 시간내 무료 배달", "Free delivery within 24 hours in the city of Seoul"), (f"가격: {_kn(780000)} 원에서 {_kn(663000)} 원으로", "Price: from 780,000 won to 663,000 won (the book’s arrow is read 에서 … 으로, mine)"),
]
_STAR_CAT = [("영상 음향", "video and audio (mine)"), ("생활용품", "daily necessities (the book’s heading; English mine)"), ("컴퓨터", "computers (mine)"), ("프린터 팩스", "printers and fax machines (mine)"), ("주방용품", "kitchenware (mine)")]
_STAR = [("디지털 카메라", "digital camera"), ("캠코더", "camcorder"), ("홈시어터", "home theater"), ("에어컨", "air conditioner"), ("세탁기", "washer"), ("선풍기", "electric fan"), ("진공청소기", "vacuum cleaner"), ("식기세척기", "dishwasher"),
         ("노트북", "laptop computer"), ("데스크탑", "desktop computer"), ("모니터", "monitor"), ("레이저 프린터", "laser printer"), ("팩스", "fax machine"), ("냉장고", "refrigerator"), ("가스오븐레인지", "stove/oven"), ("전자레인지", "microwave")]
L5 = lesson(
    "Ch 18 · Activities B: a washer advertisement and a product list",
    "세탁기 대 할인 · 무이자 할부 · 품질 보증 기간 · 무료 배달 · 스타 전자 · 제품 정보",
    requires=[],
    cards=[
        card("Topic B, Follow-up 1 (Reading): an advertisement for a washer",
             "The book gives an advertisement for a washing machine and asks you to fill in a table in English (discount, financing, warranty, delivery). The text is the book’s (figures are spelled out in Hangul); the English is mine.",
             examples=passage(_WASH)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Discount", "Financing", "Warranty", "Delivery"], [["25% off (780,000 won → 663,000 won)", "Interest-free installments for 6 months", "One year; free repair if it breaks during the warranty period", "Free delivery within 24 hours in the city of Seoul"]])]),
        card("Activities, Activity 2 (Reading): the Star Electronics product list",
             "The book shows the product list posted on the website of the Star Electronics Company (스타 전자: 제품 정보, “생활이 즐거워집니다!”, “Life becomes enjoyable!”, mine) and asks you to circle the English equivalents in a box. The Korean products with their English equivalents (the answers are mine):",
             tables=[ktable(_STAR), ktable(_STAR_CAT, title="The headings of the list")]),
        card("Activities left out",
             "Follow-up 2 of Topic B and Activity 2 (b) (listening to conversations at a home appliance store and filling in the product, the payment method, the delivery fee and the warranty period) are audio activities; Activity 1 (a SMART Board activity) and Activity 3 (two partners read two advertisement flyers, compare the stores, report to the class and role-play customer and salesperson) are computer, partner or class activities."),
    ],
    exercises=uniq(
        _tr(_WASH + _STAR_CAT) + vocab_exercises(_STAR)
        + [M("How much is the discount?", "25%", ["10%", "5%", "50%"], "이십오 퍼센트 할인."), M("How long is the interest-free installment plan?", "6 months", ["12 months", "3 months", "1 year"], "육 개월."), M("How long is the warranty period?", "One year", ["Six months", "Two years", "Three months"], "일 년."),
           M("What happens if it breaks within the warranty period?", "It is repaired for free", ["It is exchanged", "It is refunded", "Nothing"], "무료로 고쳐 드립니다."), M("Where is the delivery free?", "In the city of Seoul, within 24 hours", ["Everywhere in Korea", "Only in Busan", "Only on weekends"], "서울 시내 이십사 시간내 무료 배달."),
           M("What was the price after the discount?", "663,000 won", ["780,000 won", "585,000 won", "66,300 won"], "육십육만 삼천 원."),
           F("세탁기 대 ___ (a big sale)", "할인", ["보증", "배달"], "대 할인 = a big sale."), F("품질 ___ 기간 안에 고장이 나면 무료로 고쳐 드립니다. (warranty)", "보증", ["할인", "배달"], "보증 = warranty."), F("서울 시내 이십사 시간내 무료 ___ (delivery)", "배달", ["보증", "할부"], "배달 = delivery."),
           F("무이자 ___ 육 개월 (installments)", "할부", ["일시불", "배달"], "할부 = payment in installments."),
           read_q("세탁기 대 할인"), read_q("무이자 할부 육 개월"), read_q("스타 전자"), read_q("제품 정보"), read_q("무료 배달")]
    ),
)

# ================================================================== Grammar A: the object in a mutual relationship
_MU_EX = [("톰이 제인과 데이트합니다.", "Tom dates Jane."), ("제인이 톰과 데이트합니다.", "Jane dates Tom."), ("한국말은 일본말과 비슷합니다.", "Korean is similar to Japanese."), ("일본말은 한국말과 비슷합니다.", "Japanese is similar to Korean."),
          ("톰과 제인이 데이트합니다.", "Tom and Jane date (each other)."), ("한국말과 일본말은 비슷합니다.", "Korean and Japanese are similar (to each other).")]
_MU_RULE = [("톰은 제인과 결혼했습니다.", "Tom has married Jane."), ("한국어는 영어와 다릅니다.", "Korean is different from English."), ("제 모자랑 김 선생님 모자가 같습니다.", "My hat is the same as Mr. Kim’s hat.")]
_MU_FU1 = [("제인 옷이 수잔 옷하고 똑같아요.", "Jane’s clothes are the same as Susan’s clothes. (the book’s model)"), ("제인 옷하고 수잔 옷이 똑같아요.", "Jane’s clothes and Susan’s clothes are the same. (the book’s model)"),
           ("왼쪽 문이 오른쪽 문과 비슷해요.", "The door on the left is similar to the door on the right."), ("흰색 세탁기가 파란색 세탁기와 달라요.", "The white washer is different from the blue washer."),
           ("쉘 주유소 기름 가격이 쉐브론 주유소 기름 가격과 달라요.", "The oil price at the Shell gas station is different from the oil price at the Chevron gas station."), ("왼쪽 창문이 오른쪽 창문과 비슷해요.", "The window on the left is similar to the window on the right.")]
_MU_N = [("모자", "a hat"), ("옷", "clothes"), ("세탁기", "a washer"), ("냉장고", "a refrigerator"), ("한국말", "Korean"), ("영어", "English"), ("차", "a car"), ("가방", "a bag")]
L6 = lesson(
    "Ch 18 · Grammar A: the object in a “mutual” relationship with the subject",
    "한국말은 일본말과 비슷합니다 · 와/과 · 하고 · (이)랑 · 같다 · 다르다 · 결혼하다",
    requires=[],
    cards=[
        card("Indicating the object in a “mutual” relationship with the subject",
             "Consider the relationship between the two nouns in “Tom dates Jane” and “Korean is similar to Japanese”. Although one is the subject and the other is the object (of a verb or preposition), the nouns are in a “mutual” relationship: Tom and Jane date each other, and Korean and Japanese are similar to each other. Therefore, it is possible to reverse the two nouns without affecting the meanings of the sentences.\n\n"
             "You can reverse the two nouns in a mutual relationship in Korean as well. In such cases, we attach the noun connector 와/과, 하고, or (이)랑 to the second noun, although the second noun is considered to be the object (of a verb or preposition).",
             examples=passage(_MU_EX)),
        card("The rule",
             "object + 와/과, 하고, (이)랑.",
             tables=[table(["Connector", "After a consonant", "After a vowel"], [["와/과", "과", "와"], ["(이)랑", "이랑", "랑"], ["하고", "하고", "하고"]])],
             examples=passage(_MU_RULE)),
        card("Forms (mine)",
             "The connectors are added by the book’s rule.",
             tables=[table(["Noun", "Meaning", "와/과", "(이)랑", "하고"], [[n, m, conn(n, "과/와"), conn(n, "(이)랑"), conn(n, "하고")] for n, m in _MU_N], say=[0, 2, 3, 4])]),
        card("Follow-up 1 (Reading): make a sentence with the given words",
             "The book shows four pictures with words (왼쪽 문, 오른쪽 문, 비슷하다; 흰색 세탁기, 파란색 세탁기, 다르다; the oil prices of two gas stations, 다르다; 왼쪽 창문, 오른쪽 창문, 비슷하다) and asks you to make a sentence with 와/과, 하고 or (이)랑. The book’s model is the first two sentences; the other four are my answers (the English is mine).",
             examples=passage(_MU_FU1)),
        card("Activities left out",
             "Follow-up 2 (listening to six statements and identifying two objects being compared as the same, different or similar) is an audio activity. The book’s pictures are left out."),
    ],
    exercises=uniq(
        [M(f"Which is {n} + 와/과 (the book’s rule)?", conn(n, "과/와"), [n + ("와" if has_final(n) else "과"), n + "이랑" if not has_final(n) else n + "랑"], f"{n} ends in a {'consonant' if has_final(n) else 'vowel'}: {conn(n, '과/와')}.") for n, m in _MU_N]
        + [M(f"Which is {n} + (이)랑?", conn(n, "(이)랑"), [n + ("랑" if has_final(n) else "이랑"), n + ("와" if has_final(n) else "과")], f"{n}: {conn(n, '(이)랑')}.") for n, m in _MU_N]
        + _tr(_MU_EX + _MU_RULE + _MU_FU1)
        + [F("한국어는 영어___ 다릅니다. (is different from)", "와", ["과", "이랑"], "영어 ends in a vowel: 영어와."), F("톰은 제인___ 결혼했습니다. (married)", "과", ["와", "랑"], "제인 ends in a consonant (ㄴ): 제인과."), F("제 모자___ 김 선생님 모자가 같습니다. (and)", "랑", ["이랑", "과"], "모자 ends in a vowel: 모자랑."),
           F("한국말은 일본말과 ___. (similar)", "비슷합니다", ["데이트합니다", "결혼했습니다"], "비슷하다 = to be similar."), F("제인 옷이 수잔 옷하고 ___. (the same)", "똑같아요", ["달라요", "비슷해요"], "똑같다 = to be exactly the same."), F("흰색 세탁기가 파란색 세탁기와 ___. (different)", "달라요", ["똑같아요", "비슷해요"], "다르다 → 달라요."),
           M("What can you do with two nouns in a mutual relationship?", "Reverse them without changing the meaning", ["Never reverse them", "Drop the verb", "Make them negative"], "톰이 제인과 데이트합니다 = 제인이 톰과 데이트합니다."), M("Which connectors does the book list?", "와/과, 하고 and (이)랑", ["은/는 and 이/가", "에서 and 에게", "도 and 만"], "와/과, 하고, (이)랑."),
           M("Which sentence means “Korean and Japanese are similar”?", "한국말과 일본말은 비슷합니다.", ["한국말은 일본말과 다릅니다.", "한국말과 일본말은 같습니다.", "일본말은 한국말을 비슷합니다."], "A와 B는 비슷합니다."),
           read_q("제인과 데이트합니다"), read_q("일본말과 비슷합니다"), read_q("모자랑 같습니다"), read_q("영어와 다릅니다"), read_q("수잔 옷하고 똑같아요")]
    ),
)

# ================================================================== Grammar B: -(으)ㄹ게요
def _gae(verb):
    """-(으)ㄹ게요 and -(으)ㄹ게: 읽다 -> 읽을게요, 읽을게; 가다 -> 갈게요; 만들다 -> 만들게요"""
    base = future_(verb)[0].split(" ")[0]
    return base + "게요", base + "게"


_GAE_V = [("전화하다", "to call"), ("앉다", "to sit"), ("차리다", "to set (a table)"), ("초대하다", "to invite"), ("만들다", "to make"), ("읽다", "to read"), ("가다", "to go"), ("빌리다", "to borrow; to rent"), ("사다", "to buy"), ("준비하다", "to prepare"), ("먹다", "to eat"), ("찾다", "to find; to look for")]
_GAE_EX = [("제가 오늘 저녁에 전화할게요.", "I will give you a call tonight."), ("내가 오늘 저녁에 전화할게.", "I will give you a call tonight. (blunt)"), ("제가 여기에 앉을게요.", "I will sit here."), ("내가 여기에 앉을게.", "I will sit here. (blunt)"),
           ("제가 상을 차릴게요.", "I will set the table."), ("내가 상을 차릴게.", "I will set the table. (blunt)"), ("제 친구 수영이도 초대할게요.", "I will invite my friend Sooyoung as well."), ("제가 케이크를 만들게요.", "I will make the cake."),
           ("책을 읽다 → 제가 책을 읽을게요.", "(the book’s model for Follow-up 3) I will read the book."), ("차는 제가 빌릴게요.", "I will rent the car. (the book’s model)"), ("아시아 박물관 표는 제가 살게요.", "I will buy the Asia Museum tickets. (the book’s model)")]
_GAE_EX = [(a.split(" → ")[1] if " → " in a else a, b) for a, b in _GAE_EX]
_GAE_PH = [("책을 읽다", "to read a book"), ("케이크를 만들다", "to make a cake"), ("여기에 앉다", "to sit here"), ("상을 차리다", "to set the table"), ("친구를 초대하다", "to invite a friend"), ("차를 빌리다", "to rent a car"), ("표를 사다", "to buy a ticket"), ("음식을 준비하다", "to prepare food")]
L7 = lesson(
    "Ch 18 · Grammar B: first-person intention in informal settings, -(으)ㄹ게요",
    "제가 전화할게요 · 제가 앉을게요 · 제가 만들게요 · 제가 살게요 · 내가 할게",
    requires=[],
    cards=[
        card("Expressing first-person intention in informal settings",
             "In Chapter 11, you learned that the verb infix 겠 is used to express the first-person speaker’s strong intention, as in 한국에 가겠습니다 (I will go to Korea) or 내년에 결혼하겠어요 (I will get married next year). In this lesson, you learn about another way to express the first-person speaker’s strong intention: the verb ending -(으)ㄹ게(요). Like 겠, -(으)ㄹ게요 expresses the speaker’s strong intention, but only in informal settings and only in statements. -(으)ㄹ게 is a blunt form of -(으)ㄹ게요, and it is used between people in close relationship.",
             examples=passage(_GAE_EX[:2])),
        card("The rule",
             "action verb stem + (으)ㄹ게요.",
             tables=[table(["Condition", "Rule", "Example"], [["If the verb stem ends in a consonant", "verb stem + 을게요", "여기에 앉다 → 제가 여기에 앉을게요 → 내가 여기에 앉을게"], ["If the verb stem ends in a vowel", "verb stem + ㄹ게요", "상을 차리다 → 제가 상을 차릴게요 → 내가 상을 차릴게"]])],
             examples=passage(_GAE_EX[2:8])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (verbs whose stem ends in ㄹ keep the ㄹ: 만들다 → 만들게요).",
             tables=[table(["Verb", "Meaning", "-(으)ㄹ게요", "-(으)ㄹ게"], [[v, m, *_gae(v)] for v, m in _GAE_V], say=[0, 2, 3])]),
        card("Follow-up 3 and 5: phrases and plans",
             "In Follow-up 3 partners read phrases from List A or B and make a sentence with -(으)ㄹ게요 and the subject 제가 or 저는 (the book’s model: 책을 읽다 → 제가 책을 읽을게요). In Follow-up 5 partners decide who will bring or prepare each thing for a weekend plan (models: 차는 제가 빌릴게요; 아시아 박물관 표는 제가 살게요). Sentences for eight phrases (mine):",
             tables=[table(["Phrase", "Sentence", "Meaning"], [[p, "제가 " + " ".join(p.split(" ")[:-1] + [_gae(p.split(" ")[-1])[0]]), m] for p, m in _GAE_PH], say=[0, 1])],
             examples=passage(_GAE_EX[8:])),
        card("Activities left out",
             "Follow-up 3 (partner activity with verb cards), Follow-up 4 (listening to three conversations about plans for the weekend and what he and she will do) and Follow-up 5 (partners plan a weekend activity and decide who prepares what) are audio or partner activities."),
    ],
    exercises=uniq(
        _fk(_GAE_V, lambda v: _gae(v)[0], "-(으)ㄹ게요", lambda v: [stem(v) + "게요", stem(v) + "을게요", stem(v) + "ㄹ게요" if False else stem(v) + "겠어요", stem(v) + "는게요"])
        + _fk(_GAE_V[:8], lambda v: _gae(v)[1], "blunt -(으)ㄹ게", lambda v: [stem(v) + "게", stem(v) + "을게", stem(v) + "겠어", stem(v) + "는게"])
        + _tr(_GAE_EX)
        + [M(f"How do you say “I will {m.replace('to ', '', 1)}” with 제가?", "제가 " + " ".join(p.split(" ")[:-1] + [_gae(p.split(" ")[-1])[0]]), ["제가 " + " ".join(p.split(" ")[:-1] + [stem(p.split(" ")[-1]) + "습니다"]), "제가 " + " ".join(p.split(" ")[:-1] + [stem(p.split(" ")[-1]) + "고 싶어요"])], f"{p} → {_gae(p.split(' ')[-1])[0]}.") for p, m in _GAE_PH[:6]]
        + [F("제가 오늘 저녁에 전화___요. (I will)", "할게", ["하게", "할까"], "전화하다 → 전화할게요."), F("제가 여기에 앉___요. (I will sit)", "을게", ["ㄹ게", "게"], "앉다 ends in a consonant: 앉을게요."), F("제가 케이크를 만___요. (I will make)", "들게", ["들을게", "드를게"], "만들다 keeps ㄹ: 만들게요."),
           F("차는 제가 빌___요. (I will rent)", "릴게", ["리게", "릴까"], "빌리다 → 빌릴게요."), F("표는 제가 ___요. (I will buy)", "살게", ["사게", "살까"], "사다 → 살게요."), F("내가 오늘 저녁에 전화할___. (blunt)", "게", ["게요", "까"], "-(으)ㄹ게 is the blunt form."),
           M("In which situations can -(으)ㄹ게요 be used?", "Informal settings, in statements only", ["Formal settings", "Questions", "Commands"], "Like 겠 but informal and only in statements."), M("What is -(으)ㄹ게 to -(으)ㄹ게요?", "Its blunt form", ["Its formal form", "Its honorific form", "Its question form"], "Used between close people."),
           M("What do 겠 and -(으)ㄹ게요 both express?", "The first-person speaker’s strong intention", ["A past event", "A question", "A command"], "내가 할게 = I will do it."),
           read_q("제가 전화할게요"), read_q("제가 앉을게요"), read_q("제가 상을 차릴게요"), read_q("제가 케이크를 만들게요"), read_q("제가 살게요")]
    ),
)

# ================================================================== Topic C
_C_TEXT = [
    ("과일하고 채소를 사러 시장에 갔다.", "I went to the market to buy fruits and vegetables."),
    ("먼저 과일 가게에 가서 수박 한 통하고 복숭아 다섯 개를 샀다.", "First I went to a fruit store and bought one watermelon and five peaches."),
    (f"모두 {_kn(21000)} 원이었는데 주인 아저씨가 천 원을 깎아주셨다.", "It was 21,000 won in all, but the owner (a man) gave me a discount of 1,000 won."),
    ("그다음에 채소 파는 가게에 갔다.", "Then I went to a store that sells vegetables."),
    ("거기에서 시금치 세 단하고 감자 한 상자를 샀다.", "There I bought three bundles of spinach and a box of potatoes."),
    ("주인 아주머니께서 양파 한 봉지를 공짜로 주셨다.", "The owner (a woman) gave me a bag of onions for free."),
    ("시장 물건이 백화점 물건보다 훨씬 더 쌌다.", "The goods at the market were far cheaper than the goods at the department store."),
    ("그렇지만 품질은 백화점 물건만큼 좋았다.", "But the quality was as good as the goods at the department store."),
    ("그리고 가게 주인 아주머니, 아저씨들이 친절하고 좋으셨다.", "And the store owners, the women and the men, were kind and nice."),
    ("시장 구경하는 것이 아주 재미있었다.", "Looking around the market was very fun."),
    ("그래서 다른 시장도 구경하기로 했다.", "So I decided to look around other markets, too."),
]
_C_WORDS = ["감자", "공짜(로)", "-기로 하다", "~ 단", "당근", "~만큼", "박스", "배 (pear)", "복숭아", "봉지", "상자", "~ 송이", "수박", "시금치", "시장", "신선하다", "아저씨", "아주머니 / 아줌마", "양파", "오이", "옥수수", "야채 / 채소", "토마토", "~ 통", "파", "훨씬"]
_FRUIT = [("수박", "a watermelon"), ("포도", "a grape (mine)"), ("배", "a pear"), ("복숭아", "a peach"), ("토마토", "a tomato"), ("시금치", "spinach"), ("양파", "an onion"), ("오이", "a cucumber"), ("옥수수", "corn"), ("감자", "a potato"), ("파", "a green onion"), ("당근", "a carrot")]
_CNT_EX = [("학생 두 명", "two students"), ("선생님 세 분", "three teachers"), ("사과 다섯 개", "five apples"), ("학생 두 명이 있어요.", "There are two students. (subject)"), ("학생이 두 명 있어요.", "There are two students. (subject)"), ("학생 두 명을 만났어요.", "I met two students. (object)"), ("학생을 두 명 만났어요.", "I met two students. (object)")]
_CNT_ALL = [("한 통", "one watermelon (a head)"), ("복숭아 다섯 개", "five peaches"), ("시금치 세 단", "three bundles of spinach"), ("감자 한 상자", "one box of potatoes"), ("양파 한 봉지", "one bag of onions"), ("포도 열 송이", "ten bunches of grapes")]
L8 = lesson(
    "Ch 18 · Topic C: I went to the open-air market to buy fruits and vegetables",
    "과일하고 채소를 사러 시장에 갔다 · 수박 한 통 · 시금치 세 단 · 감자 한 상자 · 양파 한 봉지",
    requires=[],
    cards=[
        card("Topic C: I went to the open-air market to buy fruits and vegetables (과일하고 채소를 사러 시장에 갔다)",
             "The text is Michael’s journal entry about his experience at an open-air market. (The English is mine; the book gives none. The book writes 21,000원 and 1,000원; they are spelled out here.)",
             examples=passage(_C_TEXT)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Fruits and vegetables (여러 가지 과일과 채소)",
             "The book shows pictures of twelve fruits and vegetables with their names (the English is the book’s from the Core Vocabulary, except 포도, which is mine).",
             tables=[ktable(_FRUIT)]),
        card("Notes: counters",
             "So far, you have learned several counters used for counting nouns: 명 and 분 for counting people, 개 for counting things in general, etc. We use them in the following order: noun + number + counter. When we use a noun with a counter as a subject or an object, we can add a marker to the noun or the counter.",
             examples=passage(_CNT_EX)),
        card("Counters of the text (the book’s, with the English mine)",
             "The counters of this chapter are 통 (watermelons, heads of cabbage, etc.), 단 (a bundle), 상자 (a box), 봉지 (a bag), 송이 (a bunch of grapes, bananas, etc.) and 개.",
             tables=[ktable(_CNT_ALL)]),
        card("Cultural notes: open-air markets",
             "In Korea, an open-air market is known as (재래) 시장 (a traditional market), such as 남대문시장, 동대문시장, 광장시장, or 통인시장. Many small stores line alleyways and offer a variety of goods such as clothing, cosmetics, accessories, shoes, fabrics, foods, and agricultural products. Unlike department stores, where prices are fixed and there is no haggling, you can negotiate and bargain at an open-air market.",
             tables=[ktable([("재래시장", "a traditional market (the book’s 재래 시장)"), ("남대문시장", "Namdaemun Market"), ("동대문시장", "Dongdaemun Market"), ("광장시장", "Gwangjang Market"), ("통인시장", "Tongin Market")])]),
        card("Activities left out",
             "The SMART Board activities and the reporter-and-writer activity of the Presentation Activity (the text is posted outside the classroom, the reporter reports in Korean, the writer writes it, then the pair switches roles and checks the text with a red pen) are computer, partner or class activities. Follow-up 1 is in the next lesson; Follow-up 2 (listening to four segments of a conversation between a mother and her daughter about grocery shopping, filling in the groceries and the quantities) is an audio activity."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith(("-", "~")) and "/" not in w]))
        + _tr(_C_TEXT + _CNT_EX + _CNT_ALL + _FRUIT)
        + [M("Where did Michael go?", "To the market", ["To a department store", "To a school", "To a bank"], "시장에 갔다."), M("What did he buy at the fruit store?", "A watermelon and five peaches", ["Spinach and potatoes", "Grapes and pears", "Onions and carrots"], "수박 한 통하고 복숭아 다섯 개."),
           M("How much was the discount at the fruit store?", "1,000 won", ["2,000 won", "500 won", "No discount"], "천 원을 깎아주셨다."), M("What did he buy at the vegetable store?", "Three bundles of spinach and a box of potatoes", ["A watermelon", "Peaches", "Corn"], "시금치 세 단하고 감자 한 상자."),
           M("What did the owner give for free?", "A bag of onions", ["A watermelon", "A box of potatoes", "A bunch of grapes"], "양파 한 봉지를 공짜로 주셨다."), M("How were the market prices compared with the department store?", "Far cheaper", ["The same", "A little more expensive", "Far more expensive"], "훨씬 더 쌌다."),
           M("How was the quality of the market goods?", "As good as the department store’s", ["Worse", "Better", "Much worse"], "백화점 물건만큼 좋았다."), M("What did Michael decide at the end?", "To look around other markets, too", ["To buy at the department store", "To stop shopping", "To go home"], "다른 시장도 구경하기로 했다."),
           M("Which counter is used for a watermelon?", "통", ["단", "송이", "봉지"], "수박 한 통."), M("Which counter is used for spinach and green onions?", "단", ["통", "송이", "봉지"], "시금치 세 단."), M("Which counter is used for grapes?", "송이", ["통", "단", "상자"], "포도 열 송이."),
           M("What can you do at an open-air market but not at a department store?", "Bargain for a discount", ["Pay by credit card", "Get a refund", "Buy furniture"], "Prices are fixed at department stores; you can bargain at an open-air market."),
           F("시금치 세 ___하고 감자 한 상자를 샀다. (bundles)", "단", ["통", "송이"], "단 = a bundle."), F("양파 한 ___를 공짜로 주셨다. (bag)", "봉지", ["상자", "통"], "봉지 = a bag."), F("수박 한 ___하고 복숭아 다섯 개를 샀다. (watermelon counter)", "통", ["단", "송이"], "통 = counter for watermelons."),
           F("시장 물건이 백화점 물건보다 ___ 더 쌌다. (by far)", "훨씬", ["아주", "미리"], "훨씬 = by far."), F("품질은 백화점 물건___ 좋았다. (as good as)", "만큼", ["보다", "처럼만"], "만큼 = as … as."), F("다른 시장도 구경하___ 했다. (decided to)", "기로", ["는 것", "고"], "-기로 하다 = to decide to."),
           read_q("과일하고 채소를 사러 시장에 갔다"), read_q("수박 한 통"), read_q("시금치 세 단"), read_q("양파 한 봉지"), read_q("재래시장")]
    ),
)

# ================================================================== Activities C
_FLY1 = [("싱싱 청과", "Singsing Fruits and Vegetables"), ("신선한 과일과 채소를 찾으십니까? 최고의 품질! 최고의 서비스! 싼 가격!", "Are you looking for fresh fruits and vegetables? The best quality! The best service! Cheap prices!"), ("각종 과일 및 채소 전문", "Specialists in all kinds of fruits and vegetables"),
         (f"온라인 주문 시 {sino(5)} 퍼센트 할인", "5% off for online orders"), ("복숭아, 포도 등 계절 과일", "Seasonal fruits such as peaches and grapes"), (f"한 박스 이상 구입 시 {sino(10)} 퍼센트 할인", "10% off when you buy one box or more"), ("가락동 가락시장 내", "Inside Garak Market in Garak-dong")]
_FLY2 = [("우리 청과", "Uri Fruits and Vegetables"), ("농장에서 바로 가져온 싱싱한 과일!", "Fresh fruits brought straight from the farm!"), ("배, 수박, 토마토 등 맛있는 계절 상품", "Delicious seasonal products such as pears, watermelons and tomatoes"), ("최고의 맛과 품질", "The best taste and quality"),
         (f"과일 한 박스 이상 구입할 때 {sino(10)} 퍼센트 할인", "10% off when you buy one box or more of fruit"), ("전화 주문 시 전국 무료 배달 서비스", "A free nationwide delivery service for phone orders"), (f"청계천 시장 내 우리 청과 {sino(90)} 호", "Uri Fruits and Vegetables, No. 90, inside Cheonggyecheon Market")]
_DESC = [("돈을 내지 않고 무료로 받는다.", "You receive it for free without paying money.", "공짜"), ("가게나 수퍼마켓에서 물건을 살 때 보통 이 안에 물건을 넣는다.", "When you buy things at a store or a supermarket, you usually put the things in this.", "봉지"),
         ("여러 가지 물건을 사고 판다. 백화점에 비해 가격이 싸다.", "Various things are bought and sold. The prices are cheap compared with a department store.", "시장"), ("야채나 과일, 생선 등이 오래되지 않고 싱싱하다.", "Vegetables, fruits, fish and so on are not old but fresh.", "신선하다")]
_NAM_A = [("남대문시장은 서울을 대표하는 시장으로 남대문 부근에 있다.", "Namdaemun Market is a market that represents Seoul, and it is near Namdaemun."), ("남대문시장에 가려면 지하철이 편리하다.", "To go to Namdaemun Market, the subway is convenient."),
          ("지하철 사 호선을 타면 회현역에서 내리면 된다.", "If you take subway line 4, you can get off at Hoehyeon Station."), ("지하철 일 호선을 타면 서울역에서 내려야 한다.", "If you take subway line 1, you have to get off at Seoul Station."),
          ("또, 남대문이나 서울역 가는 버스를 타도 된다.", "Also, you can take a bus that goes to Namdaemun or Seoul Station."), ("이 시장에는 여성복, 남성복, 아동복, 모자, 악세서리, 신발, 구두 등 없는 물건이 없다.", "At this market there is nothing that they do not have: women’s clothes, men’s clothes, children’s clothes, hats, accessories, shoes, dress shoes and so on."),
          (f"보통 모든 물건을 백화점보다 {sino(20)}에서 {sino(30)} 퍼센트 싸게 살 수 있다.", "Usually you can buy all the goods 20 to 30% cheaper than at a department store.")]
_NAM_B = [("또한 야영 텐트, 배낭, 물놀이 용품과 수영복도 싸게 파는 가게가 많다.", "Also, there are many stores that sell camping tents, backpacks, water play goods and swimsuits cheaply."), (f"잘 하면 {sino(50)} 퍼센트 이상 깎을 수도 있다.", "If you do well, you may even get 50% or more off."),
          ("또한 시장 안과 길거리에는 여러 가지 음식을 파는 음식점과 가게들이 많다.", "Also, inside the market and on the streets there are many restaurants and stores that sell various foods."), ("시장에서 파는 음식을 사 먹으면서 이것저것 구경하면 재미있다.", "It is fun to buy and eat the food sold at the market while looking at this and that."),
          ("가게마다 문 여는 시간과 쉬는 날이 조금씩 다르기 때문에 가게 영업하는 날과 시간을 먼저 확인하고 시장에 방문하는 것이 좋다.", "Since the opening hours and days off differ a little from store to store, it is good to check the business days and hours of the store first and then visit the market.")]
L9 = lesson(
    "Ch 18 · Activities C: market flyers, word matching and Namdaemun Market",
    "싱싱 청과 · 우리 청과 · 공짜 · 봉지 · 시장 · 신선하다 · 남대문시장 · 지하철 사 호선",
    requires=[],
    cards=[
        card("Topic C, Follow-up 1 (Reading): two flyers about open-air market stores",
             "The book gives two flyers and asks you to fill in a table in English (name of store, items mentioned, special offer). The texts are the book’s (percentages and the store number are spelled out in Hangul; the web address and the telephone numbers are left out); the English is mine.",
             examples=passage(_FLY1) + passage(_FLY2)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Name of store", "Items mentioned", "Special offer"], [["싱싱 청과", "Fruits and vegetables; seasonal fruits such as peaches and grapes", "5% off for online orders; 10% off for one box or more"], ["우리 청과", "Fruits; seasonal products such as pears, watermelons and tomatoes", "10% off for one box or more; free nationwide delivery for phone orders"]], say=[0])]),
        card("Activities, Activity 1 (a) (Reading): match the descriptions with the words",
             "The book gives four descriptions and five words (a. 시장 b. 봉지 c. 아줌마 d. 공짜 e. 신선하다); one word does not have a match. The descriptions are the book’s; the English and the answers are mine (the unused word is 아줌마).",
             tables=[table(["Description (the book)", "Meaning (mine)", "Word (mine)"], [list(r) for r in _DESC], say=[0, 2])]),
        card("Activity 2 (Reading): an article about Namdaemun Market, part A",
             "The book gives an article about the Namdaemun Market in Seoul in two halves, A and B (partners read one half each and fill in a table in English). The text is the book’s (line numbers and percentages are spelled out in Hangul); the English is mine.",
             examples=passage(_NAM_A)),
        card("Part B",
             "The book glosses 영업 as “business; operation”. The English is mine.",
             examples=passage(_NAM_B)),
        card("The table filled in (mine)",
             "The book’s table has three columns (directions and transportation; special features; information related to business hours); these are my answers.",
             tables=[table(["Column", "Answer (mine)"], [["Directions / transportation", "Subway line 4 to Hoehyeon Station, or subway line 1 to Seoul Station; a bus to Namdaemun or Seoul Station also works"], ["Special features", "Everything is sold (clothes, hats, accessories, shoes, dress shoes); 20 to 30% cheaper than department stores; cheap camping and water play goods and swimsuits; you may bargain 50% or more; many food stores"], ["Business hours", "Opening hours and days off differ a little from store to store, so check them first"]])]),
        card("Activities left out",
             "Activity 1 (b) (listening to five conversations between a store owner and a customer, filling in the item, the quantity and the Korean counter) is an audio activity; Activity 3 (a role-play of an open-air market transaction between a produce vendor and a customer buying vegetables and fruit for a camping trip, with situation cards; the model: 아줌마, 파 한 단에 얼마예요? — 파 한 단에 천 원이에요. 아주 신선해요.) is a partner activity.",
             examples=[D("아줌마, 파 한 단에 얼마예요?", "Ma’am, how much is a bundle of green onions? (the book’s model; English mine)"), D("파 한 단에 천 원이에요. 아주 신선해요.", "A bundle of green onions is 1,000 won. They are very fresh. (the book’s model; English mine)")]),
    ],
    exercises=uniq(
        _tr(_FLY1 + _FLY2 + _NAM_A + _NAM_B + [(a, b) for a, b, c in _DESC])
        + [M(f"Which word fits “{b.rstrip('.')}”?", c, [x for _, _, x in _DESC if x != c] + ["아줌마"], f"{c}: {b}") for a, b, c in _DESC]
        + [M("Which store gives 5% off for online orders?", "싱싱 청과", ["우리 청과", "Both stores", "Neither store"], "온라인 주문 시 오 퍼센트 할인."), M("Which store has free delivery for phone orders?", "우리 청과", ["싱싱 청과", "Both stores", "Neither store"], "전화 주문 시 전국 무료 배달 서비스."),
           M("What discount do both stores give for one box or more?", "10%", ["5%", "20%", "50%"], "한 박스 이상 십 퍼센트 할인."), M("Where is 싱싱 청과?", "Inside Garak Market", ["Inside Cheonggyecheon Market", "Inside Namdaemun Market", "In a department store"], "가락시장 내."),
           M("Which subway station do you get off at on line 4 for Namdaemun Market?", "Hoehyeon Station", ["Seoul Station", "Gangnam Station", "City Hall Station"], "사 호선 회현역."), M("Which station do you get off at on line 1?", "Seoul Station", ["Hoehyeon Station", "Gangnam Station", "Jongno Station"], "일 호선 서울역."),
           M("How much cheaper than department stores is Namdaemun Market usually?", "20 to 30%", ["5 to 10%", "50%", "Not cheaper"], "이십에서 삼십 퍼센트."), M("How much may you get off if you do well?", "50% or more", ["10%", "20%", "Nothing"], "오십 퍼센트 이상 깎을 수도 있다."),
           M("What should you check before you visit the market?", "The business days and hours of the store", ["The weather", "The prices", "The subway lines"], "영업하는 날과 시간을 먼저 확인."),
           F("파 한 ___에 천 원이에요. (bundle)", "단", ["통", "송이"], "단 = a bundle."), F("아줌마, 파 한 단에 ___예요? (how much)", "얼마", ["몇", "누구"], "얼마예요? = how much is it?"), F("야채나 과일이 오래되지 않고 ___. (fresh)", "싱싱하다", ["무섭다", "비슷하다"], "싱싱하다 = fresh."),
           read_q("싱싱 청과"), read_q("우리 청과"), read_q("남대문시장"), read_q("파 한 단에 얼마예요"), read_q("지하철 사 호선")]
    ),
)

# ================================================================== Grammar C: ~만큼
_MK_EX = [("중국은 미국만큼 커요.", "China is as big as the U.S."), ("톰은 브라이언만큼 많이 먹어요.", "Tom eats as much as Brian does."), ("이 냉장고는 저 냉장고만큼 비싸요.", "This refrigerator is as expensive as that refrigerator."),
          ("김 병장은 장 일병만큼 키가 커요.", "SGT Kim is as tall as PFC Chang. (the book writes (키가), with the subject optional)"), ("잔은 마이크만큼 한국말을 잘 해요.", "John speaks Korean as fluently as Mike does."),
          ("이 냉장고는 저 냉장고만큼 안 비싸요.", "This refrigerator is not as expensive as that refrigerator."), ("이 냉장고는 저 냉장고만큼 비싸지 않아요.", "This refrigerator is not as expensive as that refrigerator.")]
_MK_MODEL = [("한국 음식이 맛있어요.", "Korean food is delicious. (A, the book’s model)"), ("한국 음식이 멕시코 음식만큼 맛있어요.", "Korean food is as delicious as Mexican food. (B, the book’s model)")]
_MK_NEG = [("비싸다", "to be expensive"), ("크다", "to be big"), ("작다", "to be small"), ("싸다", "to be cheap"), ("좋다", "to be good"), ("빠르다", "to be fast"), ("많다", "to be many; much")]
_MK_N = [("미국", "the U.S."), ("브라이언", "Brian"), ("저 냉장고", "that refrigerator"), ("형", "an older brother"), ("백화점 물건", "department store goods")]
L10 = lesson(
    "Ch 18 · Grammar C: comparison of equals with ~만큼",
    "중국은 미국만큼 커요 · 저 냉장고만큼 비싸요 · 안 비싸요 · 비싸지 않아요",
    requires=[],
    cards=[
        card("Expressing comparison of equals",
             "In English, we use the grammar pattern as … as to compare two “objects” (persons, places, things or concepts) of similar or equal value, as in “China is as big as the U.S.” and “Tom eats as much as Brian (does)”. The second “object” is placed after as … as.\n\n"
             "In Korean we use ~만큼 + verb to compare two objects of similar or equal value, and the object compared with is placed right before 만큼. Notice that in each sentence ~만큼 is followed by a verb: 미국만큼 is followed by the verb 커요, and 브라이언만큼 is followed by the verbal phrase 많이 먹어요.",
             examples=passage(_MK_EX[:2])),
        card("The rule",
             "noun + 만큼 + … verb.",
             examples=passage(_MK_EX[2:5])),
        card("Negation",
             "We can negate these sentences by adding either 안 or -지 않다 to the verbs.",
             examples=passage(_MK_EX[5:])),
        card("Forms (mine)",
             "Nouns with 만큼 (no space; 만큼 is attached to the noun) and the negative forms of some stative verbs made by the book’s two ways.",
             tables=[table(["Noun", "Meaning", "+ 만큼"], [[n, m, n + "만큼"] for n, m in _MK_N], say=[0, 2]), table(["Verb", "Meaning", "안 + verb", "-지 않아요"], [[v, m, "안 " + informal(v) if v not in ("빠르다",) else "안 빨라요", stem(v) + "지 않아요"] for v, m in _MK_NEG], say=[0, 2, 3])]),
        card("Follow-up 1 (Reading and speaking)",
             "Partners read a sentence aloud and the other makes a sentence of comparison by adding a noun followed by 만큼. The book’s model:",
             examples=passage(_MK_MODEL)),
        card("Activities left out",
             "Follow-up 1 (partner sentence lists), Follow-up 2 (listening to four conversations in which a speaker compares two objects and writing the objects and the verb) and Follow-up 5 of the next grammar point (New Year’s resolutions) are audio, partner or class activities."),
    ],
    exercises=uniq(
        [M(f"What is “as … as {m}” with ~만큼 (the noun {n})?", n + "만큼", [n + "보다", n + "처럼은", n + "하고만"], f"{n} + 만큼 = {n}만큼.") for n, m in _MK_N]
        + _tr(_MK_EX + _MK_MODEL)
        + [M(f"How do you say “not as {m.replace('to be ', '')}” with 안?", "안 " + (informal(v) if v != "빠르다" else "빨라요"), ["안 " + stem(v) + "다", stem(v) + "지 않다", "안 " + stem(v) + "습니다"], f"안 + {informal(v) if v != '빠르다' else '빨라요'}.") for v, m in _MK_NEG[:5]]
        + [F("중국은 미국___ 커요. (as … as)", "만큼", ["보다", "처럼"], "만큼 = as … as."), F("톰은 브라이언만큼 많이 ___. (eats)", "먹어요", ["먹고", "먹는"], "먹다 → 먹어요."), F("이 냉장고는 저 냉장고만큼 ___. (is not expensive)", "안 비싸요", ["안 비싼", "비싸요 안"], "안 + verb."),
           F("이 냉장고는 저 냉장고만큼 비싸___ 않아요. (not)", "지", ["고", "서"], "-지 않다 = not."), F("한국 음식이 멕시코 음식___ 맛있어요. (as … as)", "만큼", ["보다", "하고"], "만큼 = as … as."), F("잔은 마이크___ 한국말을 잘 해요. (as … as Mike)", "만큼", ["보다", "처럼"], "마이크만큼."),
           M("Where is the object compared with placed?", "Right before 만큼", ["After the verb", "At the end of the sentence", "After 안"], "미국만큼 커요."), M("What follows ~만큼?", "A verb", ["A noun", "A number", "Nothing"], "미국만큼 커요."), M("In what two ways can you negate a ~만큼 sentence?", "With 안 or -지 않다", ["With 못 only", "With 없다 only", "You cannot"], "안 비싸요 / 비싸지 않아요."),
           read_q("미국만큼 커요"), read_q("브라이언만큼 많이 먹어요"), read_q("저 냉장고만큼 비싸요"), read_q("멕시코 음식만큼 맛있어요"), read_q("비싸지 않아요")]
    ),
)

# ================================================================== Grammar D: -기로 하다
def _dec(verb):
    """-기로 하다 / -기로 했어요: 사다 -> 사기로 했어요"""
    return stem(verb) + "기로 했어요"


_DEC_EX = [("내년에 한국에 가기로 했어요.", "I (have) decided to go to Korea next year."), ("내일부터 열심히 공부하기로 했어요.", "I have decided to study hard from tomorrow on."), ("내일 여기서 모이기로 한다.", "Our decision is to get together here tomorrow."),
           (f"{sino(5)} 분만 쉬기로 합시다.", "Let’s take a break for five minutes."), ("이번 토요일에 블라우스를 사기로 했어요.", "I have decided to buy a blouse this Saturday."), ("오늘은 한국 식당에서 점심을 먹기로 했어요.", "We have decided to eat lunch at a Korean restaurant today.")]
_DEC_A = [("이번 토요일에 남대문시장에 가다", "to go to Namdaemun Market this Saturday"), ("오늘부터 고기를 안 먹다", "to not eat meat from today"), ("매일 아침 테니스를 치다", "to play tennis every morning"), ("올해는 책을 많이 읽다", "to read many books this year"),
          (f"세탁기는 {sino(10)} 개월 할부로 사다", "to buy the washer with a 10-month installment plan"), ("이번 겨울에 스키를 배우다", "to learn skiing this winter")]
_DEC_B = [("수업 후에 도서관에서 공부하다", "to study in the library after class"), ("옷 색깔이 마음에 안 들어서 교환하다", "to exchange the clothes because I don’t like the color"), ("저녁에 친구하고 커피숍에서 만나다", "to meet a friend at a coffee shop in the evening"), ("직원이 냉장고를 집까지 배달해 주다", "the employee will deliver the refrigerator to my home")]
_DEC_M = [("저는 한국 사람만큼 한국말을 잘 하고 싶어요.", "I want to speak Korean as well as a Korean."), ("그래서 오늘부터 한국말만 하기로 했어요.", "So I have decided to speak only Korean from today."), ("또 매일 한국 뉴스를 보기로 했어요.", "Also, I have decided to watch the Korean news every day.")]
L11 = lesson(
    "Ch 18 · Grammar D: expressing a decision with -기로 하다",
    "한국에 가기로 했어요 · 공부하기로 했어요 · 쉬기로 합시다 · 오늘부터 한국말만 하기로 했어요",
    requires=[],
    cards=[
        card("Expressing a decision",
             "In English, when we express an intention or a decision that we (have) made, we say decided to or (have) decided to, followed by a verb in the infinitive form. To express this in Korean, we use -기로 했다 (the past tense form of -기로 하다).\n\n"
             "When we want to show that both the speaker and the listener(s) must adhere to the agreed-upon decision, however, we use the present tense: 내일 여기서 모이기로 한다 (Our decision is to get together here tomorrow); 오 분만 쉬기로 합시다 (Let’s take a break for five minutes).",
             examples=passage(_DEC_EX)),
        card("The rule",
             "action verb stem + 기로 하다.",
             tables=[table(["Condition", "Rule", "Example"], [["With action verbs", "add 기로 하다", "사다 → 사기로 하다; 먹다 → 먹기로 하다"]])]),
        card("Follow-up 3: sentences to read and translate",
             "Partners read a sentence from List A or List B, conjugating the verb into -기로 했다, and the partner translates it. The sentences below are the book’s phrases with -기로 했어요 (mine) and the English (mine).",
             tables=[table(["Phrase (the book)", "-기로 했어요 (mine)", "Meaning (mine)"], [[p, " ".join(p.split(" ")[:-1] + [_dec(p.split(" ")[-1])]), m] for p, m in _DEC_A + _DEC_B], say=[1])]),
        card("Follow-up 5: New Year’s resolutions (오늘부터 한국말만 하기로 했어요)",
             "You think about two things you would like to be better at, write them in English, and share your resolutions with three classmates using ~만큼 and -기로 했어요. The book’s model (the English is mine):",
             examples=passage(_DEC_M)),
        card("Activities left out",
             "Follow-up 4 (listening to four dialogs in which one speaker expresses a decision, and filling in a table in English) is an audio activity; Follow-up 5 (writing resolutions and sharing them with three classmates) is a class activity."),
    ],
    exercises=uniq(
        _fk([(p.split(" ")[-1], m) for p, m in _DEC_A + _DEC_B][:0] + [(v, m) for v, m in [("사다", "to buy"), ("먹다", "to eat"), ("가다", "to go"), ("공부하다", "to study"), ("모이다", "to gather"), ("쉬다", "to take a break"), ("읽다", "to read"), ("배우다", "to learn")]], _dec, "-기로 했어요", lambda v: [stem(v) + "기로 해요", stem(v) + "으로 했어요", stem(v) + "기를 했어요", stem(v) + "고 했어요"])
        + _tr(_DEC_EX + _DEC_M + _DEC_A + _DEC_B)
        + [F("내년에 한국에 가___ 했어요. (decided to)", "기로", ["는 것", "고"], "-기로 하다 = to decide to."), F("내일부터 열심히 공부하기로 ___. (I decided)", "했어요", ["해요", "합니다"], "-기로 했어요 = I have decided to."), F("오 분만 쉬기로 ___. (let’s)", "합시다", ["했어요", "해요"], "-기로 합시다 = let’s decide to."),
           F("내일 여기서 모이기로 ___. (our decision is)", "한다", ["했다", "하고"], "The present tense shows both must adhere."), F("이번 토요일에 블라우스를 사___ 했어요. (decided to buy)", "기로", ["기를", "기가"], "사다 + 기로 하다."), F("오늘부터 한국말만 하___ 했어요. (decided to speak)", "기로", ["는 것", "고"], "하다 + 기로 했어요."),
           M("Which tense do you use to show that both the speaker and the listener must adhere to the decision?", "The present tense", ["The past tense", "The future tense", "No tense"], "내일 여기서 모이기로 한다."), M("What does -기로 했다 express?", "A decision that was made", ["A past experience", "A wish", "A command"], "가기로 했어요 = I decided to go."),
           M("What does 오늘부터 한국말만 하기로 했어요 mean?", "I have decided to speak only Korean from today.", ["I speak Korean today.", "I can only speak Korean.", "I will teach Korean."], "-기로 했어요 = have decided to."),
           read_q("한국에 가기로 했어요"), read_q("열심히 공부하기로 했어요"), read_q("쉬기로 합시다"), read_q("블라우스를 사기로 했어요"), read_q("한국말만 하기로 했어요")]
    ),
)

# ================================================================== Core vocabulary and self-evaluation
_CV_SECS = [("Department store", _CV_STORE), ("General categories of merchandise", _CV_CAT), ("Home appliances", _CV_APP), ("Payment", _CV_PAY), ("Produce", _CV_PROD), ("Counters", _CV_CNT), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not r[0].startswith(("~", "-")) and "/" not in r[0] and "~" not in r[0]]
L12 = lesson(
    "Ch 18 · Core vocabulary and self-evaluation",
    "주요 단어 · 백화점 · 가전제품 · 과일과 채소 · 단위 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits or Latin letters are respelled in Hangul (10만원 → 십만 원, 20% → 이십 퍼센트, 15,000원 → 만 오천 원, 500원 → 오백 원, 1년 → 일 년, 6층 → 육 층, 비타민 A → 비타민 에이, 10송이 → 열 송이, 5,000원 → 오천 원). The book’s (똑)같다, (무)이자, (진공)청소기, 야채/채소, 아주머니/아줌마 and 의류/~복 are shown with the forms written out (똑같다 / 같다, 무이자, 진공청소기, 야채 / 채소, 아주머니 / 아줌마, 의류 / ~복); the book’s 배 appears twice (pear here; the belly in Chapter 20). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the Additional Vocabulary section of the book is blank."),
    ] + [card(name, "Italicized English words in the book are grammatical terms, not the meaning of a Korean word." if name == "Other words" else "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: inquire about basic information when shopping for items at a department store and market; ask for a refund and exchange items; place an order and request a delivery; and negotiate and bargain for a discount.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; indicating the object in a mutual relationship with the subject; ~만큼 (as … as); -기로 하다 (to decide to); -(으)ㄹ게요 (will); and the Sino-Korean syllable 전 (電)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does the Sino-Korean syllable 전 (電) mean?", "electric(ity); lighting", ["a gathering", "not; no", "a type"], "전기, 전화, 전선."), M("What does ~만큼 mean?", "(as …) as ~", ["more than ~", "less than ~", "because of ~"], "저는 형만큼 많이 먹어요."),
           M("What does -기로 하다 mean?", "to decide to", ["to want to", "to have done", "to be able to"], "다음 주에 친구랑 쇼핑을 가기로 했어요."), M("What does -(으)ㄹ게요 express?", "The speaker’s intention (I will)", ["A question", "A past event", "A command"], "제가 식품점에서 야채를 사 올게요."),
           M("What is “a lump-sum payment”?", "일시불", ["할부", "무이자", "사은품"], "일시불 = a lump-sum payment."), M("What is “payment in installments”?", "할부", ["일시불", "무이자", "배달"], "할부 = payment in installments."),
           M("What is “a free gift”?", "사은품", ["상품권", "영수증", "신상품"], "사은품 = a free gift."), M("What is “a gift certificate”?", "상품권", ["사은품", "영수증", "신상품"], "상품권 = a gift certificate."),
           M("What is “a receipt”?", "영수증", ["상품권", "사은품", "고객"], "영수증 = a receipt.")]
        + [read_q("주요 단어"), read_q("물건 사기"), read_q("가전제품"), read_q("무이자 할부"), read_q("전기밥솥")]
    ),
)

UNIT = unit("Semester 1 · Unit 5 · Chapter 18: Shopping (물건 사기)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
