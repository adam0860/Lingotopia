"""Unit 67: KBC Semester III, Unit 16, Lesson 2 - Food and Travel (음식과 여행).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 16, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_FOOD2 = [("볶다", "to stir-fry"), ("싱겁다", "to be bland; to be not salty enough"), ("썰다", "to slice; to chop"), ("국", "soup"), ("마늘", "garlic"), ("후식", "dessert")]
_TRAV2 = [("숙박비", "lodging costs"), ("면세점", "a duty-free shop"), ("편도", "one way"), ("환전", "currency exchange"), ("명소", "a famous place; a scenic spot"), ("탑승구", "a boarding gate")]
_PLACES2 = [("공항", "an airport"), ("지하철역", "a subway station"), ("관광명소", "a tourist attraction"), ("휴게소", "a rest stop"), ("버스", "a bus"), ("기내", "inside an airplane")]
_HJ2 = [("禁 금", "forbid; abstain; ban", "금연, 금지"), ("券 권", "document; ticket; bill", "여권, 초대권"), ("乘 승", "ride on", "탑승, 승차권"), ("室 실", "room; chamber", "침실, 실내"), ("金 금", "metal; gold; money", "금속, 요금")]
_HJW2 = [("금연", "quitting smoking; no smoking"), ("금지", "forbidding"), ("여권", "a passport"), ("초대권", "an invitation ticket"), ("탑승", "boarding"), ("승차권", "a boarding ticket"), ("침실", "a bedroom"), ("실내", "inside the room; indoors"), ("금속", "metal"), ("요금", "a fee")]
_SIM2 = [("금액", "액수", "an amount of money"), ("저금", "저축", "saving"), ("모금", "성금", "fund-raising: a contribution"), ("승차권", "차표", "a boarding ticket: a ticket")]
_OPP2 = [("벌금", "상금", "a fine: a prize"), ("금연석", "흡연석", "a no-smoking seat: a smoking seat"), ("승차", "하차", "getting on: getting off"), ("실내", "실외", "indoors: outdoors"), ("금지", "허락", "forbidding: permitting")]
_L2X = [("액수", "an amount"), ("저축", "saving"), ("성금", "a contribution"), ("차표", "a ticket (for a bus or train)"), ("벌금", "a fine"), ("상금", "a prize (money)"), ("흡연석", "a smoking seat"), ("하차", "getting off"), ("실외", "outdoors"), ("허락", "permission"), ("금액", "an amount of money"), ("저금", "saving (money)"), ("모금", "fund-raising"), ("예금", "a deposit"), ("입금", "paying into an account"), ("송금", "sending money")]
L1 = lesson(
    "U16 L2 · Review: food and travel words and Sino-Korean 禁 券 乘 室 金",
    "음식과 여행 · 단어 복습 · 한자어 복습 · 볶다 · 싱겁다 · 숙박비 · 면세점 · 환전 · 탑승구 · 禁 券 乘 室 金",
    requires=[],
    cards=[
        card("단어 복습 1: sorting the words (my answers)", "The book gives twelve words and two categories, food-related and travel-related. My answers:", tables=[table(["Category", "Words"], [["Food-related words", "볶다, 싱겁다, 썰다, 국, 마늘, 후식"], ["Travel-related words", "숙박비, 면세점, 편도, 환전, 명소, 탑승구"]], say=[1]), ktable(_FOOD2 + _TRAV2)]),
        card("단어 복습 2: announcements", "The book plays five short announcements (tracks 001 to 005), asks where each one is heard (from the box) and which key words you hear. The listening is audio and is left out; the box of places is:", tables=[ktable(_PLACES2)]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ2], say=[2]), ktable(_HJW2)]),
        card("한자어 복습 1: the most similar word (my answers)", "Circle the word closest in meaning to the word on the left (A. 금액: 액수, 현금, 금품; B. 저금: 축의금, 임금, 저축; C. 모금: 예금, 성금, 입금; D. 승차권: 시간표, 여권, 차표).", tables=[table(["Word", "Similar word (my answer)", "Meaning"], [list(r) for r in _SIM2], say=[0, 1])]),
        card("한자어 복습 2: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 벌금: 송금, 요금, 상금; B. 금연석: 좌석, 흡연석, 예약석; C. 승차: 승합차, 탑승, 하차; D. 실내: 실수, 실격, 실외; E. 금지: 세관, 허락, 환전).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP2], say=[0, 1])]),
        card("More words from these exercises", "", tables=[ktable(_L2X)]),
    ],
    exercises=uniq(
        _tr(_FOOD2 + _TRAV2, k=3) + _tr(_PLACES2, k=3) + _tr(_HJW2, k=3) + _tr(_L2X, k=3)
        + [M("What does the syllable 禁 (금) mean?", "forbid; abstain; ban", ["ticket", "ride on", "room"], "금지."), M("What does the syllable 券 (권) mean?", "document; ticket; bill", ["forbid", "ride on", "room"], "여권."), M("What does the syllable 乘 (승) mean?", "ride on", ["forbid", "ticket", "room"], "탑승."), M("What does the syllable 室 (실) mean?", "room; chamber", ["forbid", "ticket", "ride on"], "침실."), M("What does the syllable 金 (금) mean in 요금?", "money", ["room", "ticket", "ban"], "요금."),
           M("Which word is similar to 금액?", "액수", ["현금", "금품", "상금"], "An amount."), M("Which word is similar to 저금?", "저축", ["축의금", "임금", "벌금"], "Saving."), M("Which word is similar to 모금?", "성금", ["예금", "입금", "송금"], "A contribution."), M("Which word is similar to 승차권?", "차표", ["시간표", "여권", "탑승구"], "A ticket."),
           M("Which word is the opposite of 벌금?", "상금", ["송금", "요금", "예금"], "A prize."), M("Which word is the opposite of 금연석?", "흡연석", ["좌석", "예약석", "금지석"], "Smoking seat."), M("Which word is the opposite of 승차?", "하차", ["탑승", "승합차", "승객"], "Getting off."), M("Which word is the opposite of 실내?", "실외", ["실수", "실격", "실력"], "Outdoors."), M("Which word is the opposite of 금지?", "허락", ["세관", "환전", "탑승"], "Permission."),
           F("여권과 ___을 보여 주세요. (a boarding ticket)", "승차권", ["침실", "금속"], "승차권."), F("이 곳에서는 ___이 금지되어 있습니다. (smoking)", "흡연", ["하차", "예약"], "흡연."), F("공항에서 ___을 했습니다. (currency exchange)", "환전", ["금연", "저금"], "환전."), F("비행기를 타는 ___는 이십 번입니다. (gate)", "탑승구", ["침실", "후식"], "탑승구."), F("국이 ___ 소금을 더 넣었습니다. (bland)", "싱거워서", ["매워서", "뜨거워서"], "싱겁다."),
           read_q("공항에서 환전을 했습니다"), read_q("여권과 승차권을 보여 주세요"), read_q("실내에서는 금연입니다"), read_q("후식으로 과일을 먹었습니다"), read_q("마늘을 썰어서 볶았습니다")]
    ),
)

# ================================================================== L2 Part 1
_ITIN = [
    ("아홉 시 삼십 분 가이드 안내에 따라 창덕궁 관람", "9:30 — viewing Changdeokgung Palace, following the guide’s directions."),
    ("열한 시 이십 분 서울 을지로로 이동", "11:20 — move to Euljiro in Seoul."),
    ("낮 열두 시 비빔밥 식사", "12:00 noon — eating bibimbap."),
    ("오후 한 시 명동쇼핑 (비비 크림 등 화장품, 어머니께 부탁 받은 김 등 구입)", "1:00 p.m. — shopping in Myeongdong (buying cosmetics such as BB cream, and laver that her mother asked her for, and so on)."),
]
_WP = [
    ("워터파크가 할인을 시작했다.", "The water parks have started discounts."),
    ("오션월드는 최대 오십 퍼센트 할인에 셔틀버스, 구명조끼 무료 이벤트를 벌인다.", "Ocean World holds a free shuttle bus and life vest event with a discount of up to 50 percent."),
    ("이십구 일까지 초, 중, 고 대학생은 주중 삼만 원, 주말 삼만 오천 원.", "Until the 29th, elementary, middle, high school and university students pay 30,000 won on weekdays and 35,000 won on weekends."),
    ("하루 선착순 천 명 온라인 사전결제를 할 경우 오십 퍼센트 할인을 받을 수 있다.", "If the first 1,000 people per day pay in advance online, they can get a 50 percent discount."),
    ("토요일은 제외다.", "Saturdays are excluded."),
    ("주한 외국인도 토요일을 제외하고 이십구 일까지 오십 퍼센트 할인해준다.", "Foreigners residing in Korea are also given a 50 percent discount until the 29th, excluding Saturdays."),
    ("농협 엔에이치 채움카드 소지자는 이십일 일 야간권이 공짜다.", "Holders of the Nonghyup NH Chaeum Card get the night ticket free on the 21st."),
]
_SPEAK2 = [("지금까지 먹어 본 한국 음식 중에서 제일 좋아하는 것이 무엇입니까?", "Of the Korean foods you have eaten so far, what is your favorite?"), ("그 음식에 들어가는 재료가 무엇인지 또 어떤 맛이 나는지 친구와 이야기해 보세요.", "Talk with a friend about what ingredients go into that food and what it tastes like."), ("가장 최근에 갔다 온 여행에 대해 이야기해 보세요.", "Talk about the most recent trip you went on."), ("언제 어디에 가서 무엇을 했는지 여행 일정에 대해서 자세히 친구에게 이야기해 주세요.", "Tell a friend in detail about the itinerary: when you went where and what you did.")]
_REC = [
    ("채소비빔밥", "Vegetable bibimbap (the title)"),
    ("밥 두 공기, 쇠고기 육십 그램, 표고버섯 두 개, 콩나물 팔십 그램, 애호박 사 분의 일 개, 달걀 두 개, 식용유 적당량, 소금 약간", "2 bowls of rice, 60 g beef, 2 shiitake mushrooms, 80 g soybean sprouts, 1/4 zucchini, 2 eggs, a suitable amount of cooking oil, a little salt."),
    ("간장 양념 (간장 한 큰 술, 설탕 이 분의 일 큰 술, 다진 파와 참기름 한 작은 술씩, 다진 마늘 이 분의 일 작은 술, 깨소금과 후춧가루 약간씩)", "Soy sauce seasoning (1 tablespoon soy sauce, 1/2 tablespoon sugar, 1 teaspoon each of minced green onion and sesame oil, 1/2 teaspoon minced garlic, a little each of ground sesame and pepper)."),
    ("콩나물 양념 (국간장, 다진 파, 다진 마늘, 참기름 이 분의 일 작은 술씩, 소금과 깨소금 약간씩)", "Soybean sprout seasoning (1/2 teaspoon each of soup soy sauce, minced green onion, minced garlic and sesame oil, a little each of salt and ground sesame)."),
    ("고추장 양념장 (고추장 두 큰 술, 통깨와 참기름 한 작은 술씩)", "Red pepper paste sauce (2 tablespoons red pepper paste, 1 teaspoon each of whole sesame seeds and sesame oil)."),
    ("밥은 고슬고슬하게 지어 준비한다.", "Cook the rice so that it is fluffy and prepare it. (Step 1)"),
    ("쇠고기, 표고버섯은 채 썰고 분량의 재료로 만든 간장 양념을 나눠 쇠고기와 표고버섯에 따로 양념한 뒤 달군 팬에 식용유를 두르고 각각 볶아 둔다.", "Cut the beef and shiitake mushrooms into strips, divide the soy sauce seasoning made with the measured ingredients, season the beef and mushrooms separately, then put oil in a heated pan and stir-fry each and set aside. (Step 2)"),
    ("콩나물은 꼬리를 떼고 끓는 물에 데친 뒤 물기를 빼고 분량의 콩나물 양념으로 무친다.", "Remove the tails of the soybean sprouts, parboil them in boiling water, drain the water and toss them with the measured soybean sprout seasoning. (Step 3)"),
    ("애호박은 반달 모양으로 썰어 달군 팬에 식용유를 두르고 소금으로 간해 볶고 달걀은 달군 팬에 식용유를 두르고 프라이한다.", "Slice the zucchini into half-moon shapes and stir-fry it seasoned with salt in a heated, oiled pan, and fry the eggs in a heated, oiled pan. (Step 4)"),
    ("그릇에 밥을 담고 준비한 이 단계, 삼 단계, 사 단계의 재료를 보기 좋게 얹은 뒤 고추장 양념장을 곁들여 낸다.", "Put the rice in a bowl, arrange the ingredients prepared in steps 2, 3 and 4 so that they look nice, and serve with the red pepper paste sauce. (Step 5)"),
]
L2 = lesson(
    "U16 L2 · Part 1 (도입 학습): a Seoul itinerary, a water park ad, and a bibimbap recipe",
    "도입 학습 · 서울 관광 일정 · 창덕궁 · 명동 · 워터파크 · 오션월드 · 사전결제 · 채소비빔밥 · 요리법 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading · Writing): a Japanese tourist’s Seoul itinerary",
             "The book gives the Seoul sightseeing schedule of a Japanese traveler, Chisato Yamase (© Kyunghyang), and asks you to fill in a table in English. The text lines of the schedule are the book’s with the times spelled out (9시 30분 → 아홉 시 삼십 분; BB 크림 → 비비 크림); the book’s 창덕국 is a slip for 창덕궁 (Changdeokgung Palace). The English is mine.",
             examples=passage(_ITIN)),
        card("학습활동 1: the table filled in (mine)", "The schedule in the picture is only partly given in text. Time and activity: 8:00–8:40 eating breakfast (given); 9:30–11:20 viewing Changdeokgung Palace with a guide; 12:00–1:00 eating bibimbap (the 11:20–12:00 slot is the move to Euljiro); 1:00–5:00 shopping in Myeongdong; 5:00–6:30 not given in the text (it is in the picture); 6:30–8:00 eating dinner (given); 8:00–10:30 watching a Nanta performance (given)."),
        card("학습활동 2 (Reading): an advertisement for the water parks",
             "The following is an advertisement about the water parks (Text and image © Kyunghyang), headed 워터파크. The text is the book’s with the numbers spelled out (50% → 오십 퍼센트; 29일 → 이십구 일; 3만원 → 삼만 원; 3만5000원 → 삼만 오천 원; 1000명 → 천 명; 21일 → 이십일 일; 농협NH채움카드 → 농협 엔에이치 채움카드); the web address and the telephone number of Ocean World are left out. The English is mine.",
             examples=passage(_WP)),
        card("학습활동 2: the questions answered (mine)", "A. The ad is about discounts and free events (a shuttle bus and life vests) at water parks, in particular Ocean World.\n\nB. Those who pay in advance online (first 1,000 people per day) get 50 percent off, except on Saturdays; foreigners living in Korea also get 50 percent off until the 29th, except on Saturdays; students pay 30,000 won on weekdays and 35,000 won on weekends until the 29th; holders of the Nonghyup NH Chaeum Card get the night ticket free on the 21st.\n\nC. The synonym of 무료 (free) in the passage is 공짜."),
        card("학습활동 3 (Reading): a bibimbap recipe",
             "The following is a bibimbap recipe from a magazine (Text and image © Kyunghyang). The text is the book’s with the quantities spelled out (2공기 → 두 공기; 60g → 육십 그램; 1/4개 → 사 분의 일 개; 1큰 술 → 한 큰 술; 1/2작은 술 → 이 분의 일 작은 술; and so on) and the step numbers dropped; in Step 5 the book’s step numbers, which did not come out in the text, are written as 이 단계, 삼 단계, 사 단계 (steps 2, 3 and 4). The English is mine.",
             examples=passage(_REC)),
        card("학습활동 3: the questions answered (mine)", "1. The soy sauce seasoning: soy sauce (1 tablespoon), sugar (1/2 tablespoon), minced green onion and sesame oil (1 teaspoon each), minced garlic (1/2 teaspoon), and a little each of ground sesame and pepper.\n\n2. Step 1: prepare fluffy steamed rice. Step 2: cut the beef and shiitake mushrooms into strips, season them separately with the soy sauce seasoning, and stir-fry each in a heated, oiled pan. Step 3: remove the tails of the soybean sprouts, parboil them, drain and toss them with the soybean sprout seasoning. Step 4: stir-fry half-moon slices of zucchini seasoned with salt, and fry the eggs. Step 5: put the rice in a bowl, arrange the ingredients from steps 2, 3 and 4 on it, and serve with the red pepper paste sauce."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK2)),
        card("Activities left out", "학습활동 2, Part 2 (Listening, track 006): an advertisement for the Everland amusement park — what the event is, where in the park it is held and what the fee is — and, with Part 1, choosing which park to recommend to a friend and discussing it in Korean. 학습활동 4 (Listening · Writing, track 007): a YTN news report on a Korean food exhibition in Toronto, Canada — the Korean foods served, a check-list of events (food samples, a display of the Chosun royal dining table, Chosun artifacts, a traditional dance, a traditional wedding demonstration, free cooking classes) and writing in Korean which event you would find the most interesting. They are audio."),
    ],
    exercises=uniq(
        _tr(_ITIN, k=3) + _tr(_WP, k=3) + _tr(_REC[5:], k=3) + _tr(_SPEAK2, k=3)
        + [M("Where does the guide take the traveler at 9:30?", "Changdeokgung Palace", ["Gyeongbokgung", "Namsan Tower", "Insadong"], "창덕궁."), M("What does she eat at noon?", "Bibimbap", ["Kimchi stew", "Pizza", "Noodles"], "비빔밥."), M("Where does she shop in the afternoon?", "Myeongdong", ["Gangnam", "Jamsil", "Hongdae"], "명동."), M("What did her mother ask her to buy?", "Laver", ["Tea", "Shoes", "Books"], "김."),
           M("What is the water park ad about?", "Discounts and free events", ["A closing", "A concert", "A lottery"], "할인."), M("Who gets 50 percent off with online advance payment?", "The first 1,000 people per day", ["Everyone", "Only children", "Only seniors"], "선착순 천 명."), M("Which day is excluded?", "Saturday", ["Sunday", "Monday", "Friday"], "토요일."), M("Which word is the synonym of 무료?", "공짜", ["할인", "이벤트", "카드"], "공짜."),
           M("How many bowls of rice does the recipe use?", "Two", ["Four", "One", "Ten"], "밥 두 공기."), M("What is done to the soybean sprouts?", "Their tails are removed and they are parboiled", ["They are deep-fried", "They are frozen", "They are ground"], "데치다."), M("How is the zucchini cut?", "Into half-moon shapes", ["Into cubes", "Whole", "Into rings"], "반달 모양."), M("What is served on the side?", "Red pepper paste sauce", ["Soy milk", "Honey", "Jam"], "고추장 양념장."),
           F("국을 끓인 후 소금으로 ___을 하세요. (seasoning)", "간", ["깨", "술"], "간."), F("팬에 식용유를 ___ 볶는다. (put around)", "두르고", ["다지고", "데치고"], "기름을 두르다."), F("콩나물은 끓는 물에 ___ 물기를 뺀다. (parboil)", "데친 뒤", ["달군 뒤", "다진 뒤"], "데치다."), F("마늘을 ___ 간장과 섞는다. (mince)", "다져서", ["데쳐서", "무쳐서"], "다지다."), F("오션월드는 ___ 결제를 하면 할인된다. (advance)", "사전", ["사후", "현장"], "사전결제."),
           read_q("창덕궁을 관람한 뒤 비빔밥을 먹었습니다"), read_q("워터파크가 할인을 시작했습니다"), read_q("밥은 고슬고슬하게 지어 준비합니다"), read_q("콩나물은 끓는 물에 데칩니다"), read_q("제일 좋아하는 한국 음식이 무엇입니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("구명조끼", "(救命) a life vest; “lifesaving vest”", ""),
        ("사전결제(하다/되다)", "(事前決濟) advance payment (to pay in advance/to be paid in advance)", "이 캠핑장을 사용하시려면 사전결제를 하셔야 합니다."),
    ]),
    ("학습활동 3", [
        ("간(하다)", "seasoning (with salt, soy sauce, etc.) (to season with salt, soy sauce, etc.)", "국을 다 끓인 후 소금으로 간을 하세요.", "간 (肝) a liver"),
        ("기름을 두르다", "to put oil around (in a pan); to grease (a pan)", ""),
        ("깨", "a sesame seed", "", "깨소금, 통깨"),
        ("다지다", "to mince; to hash", "먼저 마늘과 양파를 다져서 간장과 섞으세요."),
        ("달구다", "to heat up (cooking utensils)", "기름을 두르고 삼 분 정도 프라이팬을 달구세요."),
        ("데치다", "to parboil (vegetables)", "시금치를 데칠 때는 소금을 넣으면 좋아요."),
        ("무치다", "to mix (vegetables/potherbs) with seasonings", "여러 가지 양념을 넣고 나물을 무쳤어요."),
        ("버섯", "a mushroom", ""),
        ("~술", "a unit of measure, especially in cookery", "마지막으로 참기름을 한 술 넣으세요.", "큰 술 (tablespoon), 작은 술 (teaspoon)"),
        ("식용유", "(食用油) cooking oil; “eating-purpose oil”", "", "참기름, 콩기름, 들기름, 올리브유"),
        ("(애)호박", "a (young) squash or zucchini", ""),
        ("참기름", "sesame seed oil; “true oil”", ""),
        ("콩나물", "soybean sprouts; “soybean potherbs”", "", "숙주나물"),
    ]),
    ("학습활동 4", [
        ("궁중요리", "(宮中料理) (royal/imperial) court cuisine", "이 식당은 궁중요리를 잘하기로 유명합니다."),
        ("뜻 깊다", "to be meaningful; to have a profound meaning", "저는 이 돈을 뜻 깊은 일에 쓰고 싶습니다.", "의미 있다"),
        ("복식", "(服飾) dress and its ornaments", "이 그림은 조선시대의 복식문화를 잘 보여주고 있습니다.", "옷, 의류"),
        ("성황을 이루다", "(盛況) (a meeting or an event) to be a great success", ""),
        ("수라상", "(水刺床) a royal food table", ""),
        ("시식(하다)", "(試食) food tasting; food sampling; “testing food” (to taste food)", "다음주에 경복궁에서 전통 음식 시식행사를 합니다.", "시연, 시승"),
        ("시연(하다)", "(試演) a demonstration of a new product; a trial performance of a play; “testing performance” (to demonstrate; to give a trial performance)", "오늘 삼성전자에서 신제품 시연회를 한다고 합니다.", "시식, 시승"),
        ("주걱", "a paddle or spatula used for scooping rice", "", "국자"),
        ("즉석에서", "(卽席) offhand; impromptu; (right) off the bat", "즉석에서 원하는 대로 비빔밥을 만들어 드립니다."),
        ("흥을 돋구다", "(興) to add to the fun or amusement; to heighten the interest; to spice up", "이번 행사에는 인기 가수들도 출연해서 참가자들의 흥을 돋구었습니다."),
    ]),
]
L3 = lesson(
    "U16 L2 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 구명조끼 · 사전결제 · 간 · 기름을 두르다 · 다지다 · 달구다 · 데치다 · 무치다 · 식용유 · 호박 · 참기름 · 콩나물 · 궁중요리 · 뜻 깊다 · 시식 · 시연 · 주걱 · 즉석",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 달구다 has 3분 (written 삼 분 here). The book lists 깨소금, 통깨 and 참기름 etc. as related words; they are kept as printed.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=14, nread=12)),
)

# ================================================================== L4 Part 2 texts
_CAMP = [
    ("도심으로 캠핑 가자", "Let’s go camping in the city center (the title)."),
    ("캠핑이라고 하면 산첩첩 물겹겹 수려한 골짜기나 강줄기를 떠올리게 마련인데, “웬 도시에 캠핑장?” 하고 의아해 하는 사람들도 있을 것이다.", "When one says camping, one naturally thinks of beautiful valleys or river courses with mountains piled on mountains and waters upon waters, so there will also be people who wonder, “A campground in the city, of all places?”"),
    ("하지만 최근 들어 도시에도 캠핑장이 들어서고 있는 추세다.", "But recently there is a trend of campgrounds being built in cities too."),
    ("그나저나 도시에서 무슨 흥으로 캠핑할 수 있나 싶겠지만 산에서 못 느끼는 묘한 재미가 있다.", "Anyway, you may wonder what fun there can be in camping in a city, but there is a strange pleasure that you cannot feel in the mountains."),
    ("지난 오 월 개장한 서울 월드컵공원 노을캠핑장에 다녀왔다.", "I visited the Noeul Campground at Seoul World Cup Park, which opened last May."),
    ("장점과 단점을 꼽아 봤다.", "I listed the advantages and disadvantages."),
    ("와, 이런 데가!", "Wow, a place like this! (a subheading)"),
    ("경관 참 좋다. 야경도 좋다.", "The scenery is really good. The night view is good too."),
    ("전망대에서 내려다보면 한강과 도시의 빌딩들이 한눈에 들어온다.", "Looking down from the observatory, the Han River and the city’s buildings come into view at a glance."),
    ("가깝다. 캠핑은 텐트 치는 것만 해도 한 시간은 족히 걸린다.", "It is close. In camping, just pitching the tent takes a good hour."),
    ("캠핑장까지 가서도 해야 할 일이 많다.", "Even after getting to the campground there is a lot to do."),
    ("서울 도심 한가운데 있는 캠핑장이라면 퇴근하고 들를 수도 있다.", "If the campground is in the middle of downtown Seoul, you can even stop by after leaving work."),
    ("가까워 시간이 절약된다.", "Because it is close, time is saved."),
    ("다 빌려 준다. 노을 캠핑장의 장점은 쉽게, 초보자들도 할 수 있도록 다 빌려 준다는 것이다.", "They lend everything. The advantage of the Noeul campground is that they lend everything so that even beginners can do it easily."),
    ("텐트와 매트리스도 빌려 주고, 석쇠, 장작, 숯, 번개탄도 현장에서 살 수 있다.", "They lend tents and mattresses too, and you can buy grills, firewood, charcoal and fire-starter briquettes on the spot."),
    ("아이들에겐 딱이다. 아이들이 잔디밭에 뛰놀 수 있다.", "It is just right for children. Children can run and play on the lawn."),
    ("옆에 자연물 놀이터도 있다.", "There is also a nature playground next to it."),
    ("목재 등 자연물을 가지고 노는 공간이다.", "It is a space for playing with natural objects such as wood."),
    ("뭐야, 이거?", "What is this? (a subheading)"),
    ("캠핑장이 왜 이리 멀어.", "Why is the campground so far?"),
    ("가뜩이나 더운 날씨에 캠핑장은 언덕 꼭대기에 있고, 캠핑장까지는 골프카트를 끌고 가야 한다.", "In the already hot weather, the campground is at the top of a hill, and you have to pull a golf cart to get to it."),
    ("팔백 미터다.", "It is 800 meters."),
    ("그늘이 없다. 캠핑은 여름이든 겨울이든 땀을 쏟아내는 일이다.", "There is no shade. Camping, whether summer or winter, is work that makes you pour out sweat."),
    ("텐트 한 동 치고 나면 땀이 줄줄 흐른다.", "After pitching one tent, sweat runs down in streams."),
    ("잔디밭은 좋은데 그늘은 없다.", "The lawn is good, but there is no shade."),
    ("샤워장 없다. 요즘 새로 짓는 캠핑장은 온수 샤워장과 화장실에 신경을 쓴다.", "There is no shower room. Campgrounds newly built these days pay attention to hot-water shower rooms and toilets."),
    ("왜냐고. 캠핑도 쾌적해야 하니까.", "Why? Because camping should also be pleasant."),
    ("서울시, 아니 서울특별시에서 지은 캠핑장인데 왜 샤워실을 안 만들어 놓았을까 의아하다.", "It is a campground built by the city of Seoul — no, the Seoul Special City — so I wonder why they did not make a shower room."),
]
_SPEAK2B = [("캠핑을 해 본 적이 있습니까?", "Have you ever been camping?"), ("언제 어디를 누구와 갔었는지 또 무엇을 했는지 친구와 이야기해 보세요.", "Talk with a friend about when, where and with whom you went and what you did."), ("캠핑을 처음 가는 사람에게 무엇을 어떻게 준비해야 하는지 그 과정에 대해서 이야기해 주세요.", "Tell a first-time camper what to prepare and how, going through the process.")]
_PROCON = [("경관과 야경이 좋다", "Good scenery and night view"), ("가까워서 시간이 절약된다", "Close, so time is saved"), ("다 빌려 준다", "Everything is lent, even to beginners"), ("아이들이 뛰놀기 좋다", "Good for children to run around")]
_CONS = [("캠핑장이 멀다", "The campground is far (800 m, up a hill, by golf cart)"), ("그늘이 없다", "There is no shade"), ("샤워장이 없다", "There is no shower room")]
L4 = lesson(
    "U16 L2 · Part 2 (본 학습): city camping",
    "본 학습 · 도시 캠핑 · 노을캠핑장 · 장점과 단점 · 경관 · 야경 · 그늘 · 샤워장 · 캠핑카 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1 (Reading · Writing): an account of city camping",
             "The following is an account of an experience of camping in the city (Text and image © Kyunghyang). The text is the book’s with the numbers spelled out (5월 → 오 월; 800 m → 팔백 미터); the numbered lists are written as sentences and the equals sign in each heading is written as a full stop (for example “경관 참 좋다 = 야경도 좋다” becomes “경관 참 좋다. 야경도 좋다.”). The English is mine.",
             examples=passage(_CAMP)),
        card("학습활동 1: the advantages and disadvantages (my table)", "The book asks you to find the advantages and disadvantages in the account and fill in a table.", tables=[table(["장점 (advantage)", "Meaning"], [list(r) for r in _PROCON], say=[0]), table(["단점 (disadvantage)", "Meaning"], [list(r) for r in _CONS], say=[0])]),
        card("학습활동 1: my answer to question 2 (a sample)", "Question 2 asks whether you would choose city camping as a vacation plan, with at least two reasons, in Korean. A sample: 저는 도시 캠핑을 하고 싶습니다. 서울 도심에 있어서 가깝고, 텐트와 매트리스를 다 빌려 줘서 초보자도 쉽게 할 수 있기 때문입니다. (I would like to go city camping, because it is in downtown Seoul so it is close, and because they lend the tents and mattresses so even a beginner can do it easily.)"),
        card("학습활동 2 (Listening · Writing, track 008): news about camping and travel", "A YTN news video on camping and travel: what an RV is called in Korean, how much it costs per day to rent one, the positive aspects of RV camping (at least two), and a table comparing travel by camping car (캠핑카를 이용한 여행) with travel by hotel (호텔을 이용한 여행), with your choice and reasons. The table heading gives the Korean answer to the first question: an RV is called a 캠핑카. The rest is audio/video and is left out."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK2B)),
    ],
    exercises=uniq(
        _tr(_CAMP[1:], k=3) + _tr(_SPEAK2B, k=2) + _tr(_PROCON + _CONS, k=3)
        + [M("Which campground does the article visit?", "Noeul Campground at Seoul World Cup Park", ["A Jirisan valley campground", "A Jeju beach campground", "A Busan campground"], "노을캠핑장."), M("When did it open?", "Last May", ["Last January", "Last December", "Last April"], "지난 오 월 개장."), M("What can be seen from the observatory?", "The Han River and the city buildings", ["The sea", "A forest", "Mount Halla"], "한강과 도시의 빌딩."), M("What can be bought on the spot?", "Grills, firewood, charcoal, fire-starter briquettes", ["Cars", "Tickets", "Phones"], "석쇠, 장작, 숯, 번개탄."), M("How far is the campground, up the hill?", "800 meters", ["80 meters", "8 kilometers", "Next door"], "팔백 미터."), M("How do you get there from the entrance?", "By pulling a golf cart", ["By train", "By helicopter", "By boat"], "골프카트."), M("What is missing at the campground?", "Shade and a shower room", ["A lawn", "A playground", "A view"], "그늘, 샤워장."), M("What is an RV called in Korean?", "캠핑카", ["캠핑룸", "여행차", "텐트차"], "캠핑카."),
           F("캠핑은 텐트 치는 것만 해도 한 시간은 ___ 걸린다. (a good)", "족히", ["딱", "불쑥"], "족히."), F("서울 도심에 있어서 ___ 시간이 절약된다. (close)", "가까워", ["멀어", "높아"], "가깝다."), F("아이들에겐 ___이다. (just right)", "딱", ["널리", "불쑥"], "딱."), F("새로 짓는 캠핑장은 ___ 샤워장에 신경을 쓴다. (hot-water)", "온수", ["냉수", "취수"], "온수."), F("캠핑도 ___해야 하니까. (pleasant)", "쾌적", ["혼잡", "고행"], "쾌적하다."),
           read_q("도심으로 캠핑을 가자"), read_q("전망대에서 한강과 빌딩들이 한눈에 들어옵니다"), read_q("텐트와 매트리스도 빌려 줍니다"), read_q("잔디밭은 좋은데 그늘은 없습니다"), read_q("캠핑을 해 본 적이 있습니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("강줄기", "(江) the course of a river; “river stream”", "강줄기가 세차게 흘러갑니다."),
        ("경관", "(景觀) landscape; scenery", "이 야영장은 자연 경관이 아름답습니다.", "경치, 풍경"),
        ("골짜기", "a valley", "이번 여름에는 지리산 골짜기에 가서 야영을 합시다.", "계곡"),
        ("그늘", "shade", "햇빛이 너무 뜨거우니까 그늘을 찾아보자.", "(햇)볕"),
        ("딱", "exactly; just; precisely; perfectly", "옷이 저한테 딱 맞아요."),
        ("야경", "(夜景) night view; night scene", "남산 타워에 올라가면 서울의 야경이 한 눈에 들어옵니다.", "경치, 경관"),
        ("온수", "(溫水) hot or warm water", "아파트 보일러가 고장 나서 온수가 안 나와요.", "냉수"),
        ("의아하다/의아해하다", "(疑訝) to be dubious; to be suspicious/to wonder", "이번 사건에 대해 많은 사람들이 의아해 하고 있다."),
        ("잔디", "grass; lawn", "잔디에 물을 줘야 합니다."),
        ("쾌적하다", "(快適) (feeling, environment, etc.) to be pleasant; to be nice", "날씨가 운동하기에 아주 쾌적합니다."),
    ]),
    ("학습활동 2", [
        ("동시에", "(同時) at the same time; simultaneously", "여러 사람이 동시에 말하지 말고 한 사람씩 이야기하세요."),
        ("취사 기구", "(炊事器具) cooking utensils", "캠핑 갈 때는 취사 기구를 꼭 챙겨야 합니다.", "취사 도구"),
        ("밤샘 주차", "(駐車) overnight parking", "이 야영장은 밤샘 주차를 할 공간이 충분해서 아주 좋습니다."),
        ("투입(하다/되다)", "(投入) adding ([resources] where they are needed); “throwing in” (to add [resources]/to be added into)", "이번 달에 추가로 각 학교에 셔틀버스 두 대씩을 투입할 예정입니다."),
        ("동트다", "(東) to dawn; (the day) to break", "저희 아버지는 매일 동트기 전에 일어나세요.", "날이 밝다, 해가 뜨다 | 해가 지다"),
        ("만끽하다", "(滿喫) to fully enjoy; to enjoy to the fullest", "이번 여행 동안 자연의 아름다움을 만끽할 수 있었어요.", "즐기다"),
    ]),
]
L5 = lesson(
    "U16 L2 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 강줄기 · 경관 · 골짜기 · 그늘 · 딱 · 야경 · 온수 · 의아하다 · 잔디 · 쾌적하다 · 동시에 · 취사 기구 · 밤샘 주차 · 투입 · 동트다 · 만끽하다",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the book’s example for 동트다 the words 매일동트기 are run together; they are written 매일 동트기 here. The book’s two-line examples for 동시에 and 투입 are joined into one example.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=12, nread=10)),
)

# ================================================================== L6 Part 3 texts
_HANSIK = [
    ("세계적으로 웰빙과 건강에 대한 관심이 고조되면서 식품산업에 대한 경쟁 또한 가히 “전쟁”이라 할 만하다.", "As interest in well-being and health rises worldwide, the competition in the food industry too can well be called a “war.”"),
    ("세계식품시장의 규모가 아이티 산업의 다섯 배, 자동차 산업의 이 점 오 배에 이르다 보니 그냥 두고 볼 일이 아니다.", "Since the size of the world food market reaches five times the IT industry and 2.5 times the automobile industry, it is not something to just look on at."),
    ("일본은 “스시”, 이탈리아는 “피자”로 세계인의 입맛을 이끌어가고 있으며 태국도 탁신 전 총리의 전격적인 지원 아래 식품세계화를 추진하여 세계 사 대 식품국 대열에 합류했다.", "Japan is leading the world’s tastes with “sushi” and Italy with “pizza,” and Thailand too, under the sweeping support of former Prime Minister Thaksin, pushed for food globalization and joined the ranks of the world’s four great food countries."),
    ("우리도 “세계인이 즐기는 우리 한식”이라는 비전하에 한식세계화추진단을 꾸리고 칠백만 재외동포 네트워크를 가동하는 등 박차를 가하고 있다.", "We too, under the vision of “our Korean food enjoyed by the people of the world,” are spurring ahead by forming a Korean food globalization promotion group and operating the network of seven million overseas Koreans."),
    ("세계 오 대 식품강국으로 가는 지름길을 생각해 보자.", "Let us think about the shortcut to becoming one of the world’s five great food powers."),
    ("우선 “건강, 웰빙식” “채소 위주의 다이어트 식단”이란 특성을 가진 한식은 맛과 영양에서 그 우수성을 세계적으로 이미 인정받은 셈이다.", "First of all, Korean food, with the characteristics of being “healthy, well-being food” and a “vegetable-centered diet menu,” has in effect already been recognized worldwide for its superiority in taste and nutrition."),
    ("미국 로스앤젤레스의 한 병원에서는 한식을 영양적으로 가장 적절한 음식이라고 평가하여 일부 환자들에게 치료식으로 제공하고 있으며, 영국 파이낸셜 타임스지는 가공음식으로 인하여 비만이 증가하는 현대사회에서 한국음식은 적절한 영양적 균형을 보여 주는 모범적인 사례라고 소개하였다.", "A hospital in Los Angeles in the United States evaluates Korean food as the nutritionally most appropriate food and provides it to some patients as therapeutic food, and Britain’s Financial Times introduced Korean food as an exemplary case showing an appropriate nutritional balance in a modern society where obesity is increasing because of processed foods."),
    ("물론 입맛은 얼굴만큼이나 다양해 세계화가 쉬운 일은 아니다.", "Of course, tastes are as varied as faces, so globalization is not an easy thing."),
    ("하지만 하루 아침에 우리 젊은이들의 입맛을 사로잡은 이탈리아 피자를 보면 실마리를 찾을 수 있다.", "But we can find a clue by looking at Italian pizza, which captured the tastes of our young people overnight."),
    ("한국에 입성한 피자는 김치피자, 고구마피자 등 본래의 피클과 핫소스마저 바꾸어가며 수십 가지 형태로 변해가면서 우리 입맛을 유혹하고 있다.", "Pizza, having entered Korea, is luring our tastes by changing into dozens of forms such as kimchi pizza and sweet potato pizza, even changing the original pickles and hot sauce."),
    ("음식은 입소문 마케팅이 중요하기 때문에 한식 세계화는 지금이 기회다.", "Because word-of-mouth marketing is important for food, now is the chance for the globalization of Korean food."),
    ("금년은 “한국방문의 해”인데다 각국에서 육만여 명이 방문할 것으로 예상되는 에프원 국제자동차대회 등 대규모 국제행사가 예정되어 있고 특히 지 이십 서울정상회의가 이제 백 일 앞으로 다가왔다.", "This year is the “Year of Visiting Korea,” and in addition large-scale international events such as the F1 international auto race, which is expected to be visited by some 60,000 people from various countries, are scheduled, and in particular the G20 Seoul Summit has now come within 100 days."),
    ("식품시장은 부가가치도 크지만 고용창출 효과가 큰 산업이다.", "The food market is an industry with a large added value and also a large job-creation effect."),
    ("한식의 확산과 세계화는 농식품의 생산 및 수출증대로 이어져 일거다득의 효과를 기대할 수 있다.", "The spread and globalization of Korean food leads to increased production and export of agri-food, so the effect of “many gains in one act” can be expected."),
]
_SPEAK2C = [("한국 음식이 중국 음식이나 이탈리아 음식처럼 세계화될 수 있다고 생각합니까?", "Do you think Korean food can be globalized like Chinese food or Italian food?"), ("본인이 가지고 있는 의견에 대해 친구에게 이야기해 주고 왜 그렇게 생각하는지도 말해 보세요.", "Tell a friend your opinion and also say why you think so.")]
L6 = lesson(
    "U16 L2 · Part 3 (심화 학습): globalizing Korean food",
    "심화 학습 · 한식 세계화 · 웰빙 · 식품산업 · 입소문 · 김치피자 · 고구마피자 · 일거다득 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2 (Reading · Writing): a reader’s opinion in a newspaper",
             "The following is a reader’s opinion from a newspaper (© Kyunghyang). The text is the book’s with the numbers and abbreviations spelled out (IT → 아이티; 5배 → 다섯 배; 2.5배 → 이 점 오 배; 4대 → 사 대; 700만 → 칠백만; 5대 → 오 대; 6만여 명 → 육만여 명; F1 → 에프원; G20 → 지 이십; 100일 → 백 일); the abbreviation (LA) after Los Angeles is left out; the quotation marks “ ” are kept as printed. The English is mine.",
             examples=passage(_HANSIK)),
        card("학습활동 2: the questions answered (mine)",
             "1. B — Let’s make the “Year of Visiting Korea” an opportunity for the globalization of Korean food (the text says: since word-of-mouth marketing is important, now is the chance, because this year is the Year of Visiting Korea and big international events are scheduled).\n\n"
             "2. The author uses 전쟁 (war) to imply how fierce, all-out and high-stakes the competition in the food industry has become worldwide: the world food market is five times the IT industry and 2.5 times the automobile industry, so countries fight for it like a war.\n\n"
             "3. Positive aspects (phrases in the passage): 건강, 웰빙식 (healthy, well-being food); 채소 위주의 다이어트 식단 (a vegetable-centered diet menu); 맛과 영양에서 우수성을 인정받았다 (recognized for taste and nutrition); 영양적으로 가장 적절한 음식 (the nutritionally most appropriate food, served as therapeutic food in an L.A. hospital); 적절한 영양적 균형을 보여 주는 모범적인 사례 (an exemplary case of a proper nutritional balance, per the Financial Times).\n\n"
             "4. Because Italian pizza is the clue for globalization: after entering Korea it captured young Koreans’ tastes by changing into dozens of local forms such as kimchi pizza and sweet potato pizza, even changing its original pickles and hot sauce — localization.\n\n"
             "5. The Year of Visiting Korea, the F1 international auto race (some 60,000 foreign visitors expected) and the G20 Seoul Summit (100 days away) are mentioned because they bring many foreigners to Korea, and since word of mouth matters for food, now is the chance to spread Korean food.\n\n"
             "6. The ripple effect: the food market has a large added value and job-creation effect, and the spread of Korean food would lead to increased production and exports of agri-food products — “killing many birds with one stone” (일거다득)."),
        card("학습활동 1 (Listening · Speaking, tracks 009 and 010): an interview about globalizing Korean food", "A YTN interview with a university president who works hard to globalize Korean food: Part 1 — why she promotes Korean food worldwide, why the “Korean wrap” (쌈) might appeal to foreigners (the reasons the interviewee does not use), and a pair discussion of other Korean foods that could spread; Part 2 — what she observed about Korean restaurants in Europe and why, a definition in Korean of the localization (현지화) of Korean food, and strategies for popularizing Korean food. It is audio and the discussions are pair work; both are left out. The vocabulary of the activity is in the next lesson."),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK2C)),
    ],
    exercises=uniq(
        _tr(_HANSIK, k=3) + _tr(_SPEAK2C, k=2)
        + [M("What does the author compare the food industry competition to?", "A war", ["A festival", "A school", "A dance"], "전쟁."), M("Which country leads world tastes with sushi?", "Japan", ["Italy", "Thailand", "France"], "일본."), M("Which country leads with pizza?", "Italy", ["Japan", "Spain", "Korea"], "이탈리아."), M("Which Asian country joined the world’s four great food countries?", "Thailand", ["Vietnam", "India", "China"], "태국."), M("How many overseas Koreans form the network?", "Seven million", ["Seven thousand", "Seventy", "Seven hundred million"], "칠백만."), M("What does a Los Angeles hospital serve to some patients?", "Korean food as therapeutic food", ["Pizza", "Sushi", "Fast food"], "치료식."), M("What magazine introduced Korean food as an exemplary case?", "The Financial Times", ["Time", "Vogue", "Forbes"], "파이낸셜 타임스지."), M("What changed pizza’s form in Korea?", "Kimchi and sweet potato toppings", ["Rice", "Chocolate", "Cheese only"], "김치피자, 고구마피자."), M("Which summit is mentioned as coming within 100 days?", "The G20 Seoul Summit", ["The Olympics", "The World Cup", "The APEC"], "지 이십 서울정상회의."), M("What kind of marketing matters for food?", "Word of mouth", ["TV only", "Mail", "Billboards"], "입소문 마케팅."),
           F("한식은 맛과 영양에서 ___을 인정받았다. (superiority)", "우수성", ["일회성", "정체성"], "우수성."), F("한식 세계화에 ___를 가하고 있다. (spur)", "박차", ["유혹", "합류"], "박차를 가하다."), F("피자는 우리 입맛을 ___하고 있다. (lure)", "유혹", ["운반", "확립"], "유혹."), F("식품시장은 ___가치가 큰 산업이다. (added)", "부가", ["가공", "현지"], "부가가치."), F("한식 세계화는 ___의 효과를 기대할 수 있다. (many gains in one)", "일거다득", ["일거양실", "일일신우"], "일거다득."),
           read_q("한식 세계화는 지금이 기회입니다"), read_q("피자는 우리 입맛을 유혹하고 있습니다"), read_q("식품시장은 부가가치가 큰 산업입니다"), read_q("한식은 건강 웰빙식으로 인정받았습니다"), read_q("한국 음식이 세계화될 수 있다고 생각합니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("간편하다", "(簡便) to be simple and convenient", "이 핸드폰은 사용이 간편합니다.", "복잡하다 | 간단하다"),
        ("깻잎", "a sesame leaf", "", "상추"),
        ("다시마", "(edible) kelp", "", "미역, 김"),
        ("떠오르다", "to strike upon (an idea or inspiration); to occur to", "좋은 생각이 떠올랐어요."),
        ("무궁무진하다", "(無窮無盡) to be infinite; to be endless; to be unlimited", "그 회사는 발전 가능성이 무궁무진합니다."),
        ("밀 전병", "a wheat wrap", ""),
        ("사로잡다", "to captivate; to fascinate; to win (one’s heart)", "이번에 새로 나온 피자의 맛이 젊은 사람들의 입맛을 사로잡았다."),
        ("상추", "a (head of) lettuce", "", "깻잎"),
        ("세계화", "(世界化) globalization", "이 원장은 한식을 세계화하기 위해 노력하고 있습니다.", "국제화"),
        ("쌈", "a wrap (using lettuce, cabbage, seaweed, etc.)", "오늘 저녁은 상추쌈을 먹고 싶습니다."),
        ("안타깝다", "to be regretful; to feel sorry", "열심히 하던 학생이 시험에 떨어져서 참 안타깝습니다."),
        ("운반(하다/되다)", "(運搬) transportation; transport (to transport; to carry/to be transported; to be carried)", "책상이 너무 무거워서 운반이 어렵겠어요.", "옮기다"),
        ("응용(하다/되다)", "(應用) application (to apply/to be applied)", "미래에는 나노 기술을 응용한 전자 제품이 많이 나올 겁니다.", "적용, 사용"),
        ("정체성", "(正體性) identity", "미국에서 자라는 한국인 이 세들은 자라면서 정체성 문제로 고민을 많이 합니다."),
        ("퍼지다", "to spread", "그 소문은 금방 학교 전체에 퍼졌어요.", "확산되다"),
        ("해조류", "(海藻類) marine plants", "", "미역, 김, 다시마"),
        ("현지화", "(現地化) localization", "피자는 각 나라 사람들의 입맛에 맞게 현지화가 잘 되었어요."),
        ("확립(하다/되다)", "(確立) establishment (to establish/to be established)", "청소년기에는 자기 정체성을 확립하는 것이 중요하다.", "세우다"),
    ]),
    ("학습활동 2", [
        ("가공음식", "(加工飮食) processed food; instant food", "가공음식은 건강에 좋지 않습니다.", "인스턴트 음식"),
        ("가동(하다/되다)", "(稼動) operation (to operate/to be operated)", "에어컨 가동이 중단돼서 너무 더워요."),
        ("고조(되다)", "(高調) upsurge; heightening (of tension) (to heighten; to rise; to mount)", "최근 남북간에 긴장이 고조되고 있습니다.", "완화되다"),
        ("대열", "(隊列) a file; the ranks", "선진국 대열에 합류하기 위해서 모두 노력해야 합니다."),
        ("모범", "(模範) a (good) example", "한국은 경제 위기를 극복한 좋은 모범 사례로 소개되고 있습니다."),
        ("박차를 가하다", "(拍車) to spur; to expedite; to accelerate; “to add a spur”", "그 회사는 신기술 개발에 박차를 가하고 있다."),
        ("부가가치", "(附加價値) added value", "식품산업은 부가가치가 높은 산업이다."),
        ("실마리", "a clue", "문제해결의 실마리를 찾았어요."),
        ("유혹(하다)", "(誘惑) temptation (to attract; to lure)", "그는 돈의 유혹을 이기지 못하고 범죄를 저지르고 말았습니다."),
        ("이끌다", "to lead; to guide", "선생님은 학생들을 바른 길로 이끌어야 합니다."),
        ("일거다득", "(一擧多得) (idiom) killing many birds with one stone", "이 방법은 여러모로 도움이 되어 일거다득입니다.", "일거양득"),
        ("적절하다", "(適切) to be appropriate; to be proper", "그 말은 이 상황에는 적절하지 않습니다.", "부적절하다 | 적당하다"),
        ("합류(하다)", "(合流) joining; “adding flows” (to join)", "김 대리가 오늘부터 우리 팀에 합류하기로 했어요."),
    ]),
]
L7 = lesson(
    "U16 L2 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 간편하다 · 깻잎 · 다시마 · 쌈 · 세계화 · 운반 · 응용 · 정체성 · 현지화 · 확립 · 가공음식 · 고조 · 모범 · 박차 · 부가가치 · 실마리 · 유혹 · 일거다득 · 적절하다 · 합류",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book’s example for 정체성 has 2세 (written 이 세 here). The book lists the related words of 해조류 as the examples 미역, 김, 다시마, which are kept as printed.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=20, nread=16)),
)

UNIT = unit("Semester III · Unit 16 · Lesson 2: Food and Travel (음식과 여행)", [L1, L2, L3, L4, L5, L6, L7])
