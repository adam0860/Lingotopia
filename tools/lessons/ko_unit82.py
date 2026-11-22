"""Unit 82: KBC Semester III, Unit 17, Lesson 7 - Healthy Living (건강한 생활).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester III, Unit 17, Student's Edition.
Audio, video, pictures, charts, SMART Board activities, role-plays, games, partner and group activities are left out.
The book gives no English for its texts and leaves the answers to its exercises blank: every translation of a
text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_s3 import *
from ko_s3 import _tr, _show, _sp, _mean, _plain
from ko_unit21 import _kn

# ================================================================== L1 review
_MATCH7 = [("편식", "an unbalanced diet; “skewed eating”", "편식을 하면 몸에 좋지 않습니다"), ("지방", "fat", "지방이 많은 음식은 피하도록 하세요"), ("식품", "food", "요즘은 웰빙식품이 인기가 있습니다"), ("건강", "health", "적당한 운동은 건강에 좋습니다"), ("환경", "an environment", "환경오염으로 인한 피해가 심각합니다"), ("섭취", "intake; ingestion", "영양소를 골고루 섭취해야 합니다"), ("농약", "insecticide; pesticide; “agricultural medicine”", "과일에 농약이 많습니다. 꼭 씻어 드세요"), ("농산물", "agricultural products", "농산물을 싸게 살 수 있는 곳이 어디예요"), ("채소", "vegetable", "우리 아이가 채소를 싫어해 걱정이에요"), ("유기농", "organic (farming)", "여기에서 유기농 제품을 싸게 팝니다")]
_HJ7 = [("生 생", "birth; living; occurrence", "인생, 평생"), ("活 활", "living; vitalizing; active", "재활, 활동"), ("運 운", "moving; carrying; operating", "운동, 운송"), ("養 양", "growing; raising; cultivating", "영양, 양육"), ("健 건", "strong; healthy; solid", "건강, 보건")]
_HJW7 = [("인생", "(one’s) life"), ("평생", "lifetime"), ("재활", "rehabilitation"), ("활동", "an activity"), ("운동", "an exercise; a workout"), ("운송", "transportation"), ("영양", "nutrition"), ("양육", "bringing up; raising"), ("건강", "health"), ("보건", "public health")]
_SIM7 = [("양육", "보육", "raising: child care"), ("운송", "운반", "transportation: carrying"), ("발생하다", "일어나다", "to occur: to happen")]
_OPP7 = [("생물", "무생물", "living thing: nonliving thing"), ("생산", "소비", "production: consumption"), ("출생", "사망", "birth: death")]
_L7X = [("교육", "education"), ("교양", "culture; refinement"), ("체육", "physical education"), ("운전", "driving"), ("운행", "running (a vehicle)"), ("생활하다", "to live"), ("고생하다", "to suffer hardship"), ("재생하다", "to play back; to regenerate"), ("미생물", "a microorganism"), ("동물", "an animal"), ("식물", "a plant"), ("양산", "mass production"), ("재산", "property; assets"), ("출산", "childbirth"), ("보존", "preservation"), ("의존", "dependence"), ("생성", "creation; generation"), ("웰빙식품", "well-being food"), ("영양소", "a nutrient"), ("환경오염", "environmental pollution"), ("유기농 제품", "an organic product"), ("보육", "child care"), ("운반", "carrying")]
L1 = lesson(
    "U17 L7 · Review: healthy-living words and Sino-Korean 生 活 運 養 健",
    "건강한 생활 · 단어 복습 · 한자어 복습 · 편식 · 지방 · 식품 · 건강 · 환경 · 섭취 · 농약 · 농산물 · 채소 · 유기농 · 生 活 運 養 健",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives ten sentences with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs below are my best reading of which word is meant:", tables=[table(["Word", "Meaning", "Sentence"], [list(r) for r in _MATCH7], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ7], say=[2]), ktable(_HJW7)]),
        card("한자어 복습 1: the similar word (my answers)", "Circle the word with a similar meaning to the word on the left (A. 양육: 보육, 교육, 교양, 체육; B. 운송: 운반, 운전, 운동, 운행; C. 발생하다: 일어나다, 생활하다, 고생하다, 재생하다).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM7], say=[0, 1])]),
        card("한자어 복습 2: the opposite word (my answers)", "Circle the word with the opposite meaning of the word on the left (A. 생물: 미생물, 동물, 식물, 무생물; B. 생산: 소비, 양산, 재산, 출산; C. 출생: 사망, 보존, 의존, 생성).", tables=[table(["Word", "Opposite (my answer)", "Meaning"], [list(r) for r in _OPP7], say=[0, 1])]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 004): four spoken lifestyle habits, for each of which you write H (healthy) or U (unhealthy). It is audio."),
        card("More words from these exercises", "", tables=[ktable(_L7X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH7], k=3) + _tr(_HJW7, k=3) + _tr(_L7X, k=3) + _tr([(a, c) for a, b, c in _OPP7], k=3)
        + [M("What does the syllable 生 (생) mean?", "birth; living; occurrence", ["vitalizing", "moving", "healthy"], "인생."), M("What does the syllable 活 (활) mean?", "living; vitalizing; active", ["birth", "moving", "healthy"], "활동."), M("What does the syllable 運 (운) mean?", "moving; carrying; operating", ["birth", "growing", "healthy"], "운동."), M("What does the syllable 養 (양) mean?", "growing; raising; cultivating", ["birth", "moving", "healthy"], "영양."), M("What does the syllable 健 (건) mean?", "strong; healthy; solid", ["birth", "moving", "growing"], "건강.")
           , M("Which word is similar to 양육?", "보육", ["교육", "교양", "체육"], "Child care."), M("Which word is similar to 운송?", "운반", ["운전", "운동", "운행"], "Carrying."), M("Which word is similar to 발생하다?", "일어나다", ["생활하다", "고생하다", "재생하다"], "To occur."), M("Which word is the opposite of 생물?", "무생물", ["미생물", "동물", "식물"], "Nonliving thing."), M("Which word is the opposite of 생산?", "소비", ["양산", "재산", "출산"], "Consumption."), M("Which word is the opposite of 출생?", "사망", ["보존", "의존", "생성"], "Death.")
           , F("영양소를 골고루 ___해야 합니다. (to take in)", "섭취", ["배출", "추출"], "섭취하다."), F("과일에 ___이 많습니다. 꼭 씻어 드세요. (pesticide)", "농약", ["지방", "채소"], "농약."), F("여기에서 ___ 제품을 싸게 팝니다. (organic)", "유기농", ["가공", "유전자"], "유기농."), F("___을 하면 몸에 좋지 않습니다. (unbalanced diet)", "편식", ["섭취", "운동"], "편식."), F("___이 많은 음식은 피하도록 하세요. (fat)", "지방", ["채소", "농산물"], "지방.")]
        + [read_q("편식을 하면 몸에 좋지 않습니다"), read_q("영양소를 골고루 섭취해야 합니다"), read_q("과일에 농약이 많습니다"), read_q("여기에서 유기농 제품을 싸게 팝니다")]
    ),
)

# ================================================================== L2 Part 1
_STRESS7 = [
    ("아침에 십오 분만 일찍 일어나라.", "Get up just fifteen minutes earlier in the morning."),
    ("시간 계획을 짜서 행동하라.", "Make a time plan and act on it."),
    ("책을 가지고 다니면서 틈틈이 읽어라.", "Carry a book with you and read it in your spare moments."),
    ("어려움이 생기면 누구에게든 의논하라.", "When difficulties arise, talk them over with anyone."),
    ("용모에 신경을 써라.", "Pay attention to your appearance."),
    ("나만의 공간을 가져라.", "Have a space of your own."),
    ("걱정거리를 머리로만 생각하지 말고 종이에 구체적으로 써 보라.", "Don’t just think about your worries in your head; write them down concretely on paper."),
    ("하기 싫은 일을 미루지 말라.", "Don’t put off things you don’t want to do."),
    ("목욕을 하고 충분한 수면을 취하라.", "Take a bath and get enough sleep."),
    ("땀이 날만큼 운동을 하라.", "Exercise enough to break a sweat."),
]
_SPEAK7A = [("자신이 가진 생활습관 중에 건강에 좋은 습관과 나쁜 습관에 대해 생각해 보고 옆 친구와 이야기해 보세요.", "Think about your own good and bad habits for health and talk with the friend next to you."), ("스트레스를 푸는 데 도움이 되는 방법 세 가지를 골라서, 왜 그 방법이 나에게 맞는지 이야기해 보세요.", "Pick the three methods that help you relieve stress, and talk about why those methods suit you.")]
L2 = lesson(
    "U17 L7 · Part 1 (도입 학습): ten pieces of advice for getting out of stress",
    "도입 학습 · 스트레스 · 충고 · 건강한 식생활 · 걷기 · 웃음 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 2: from “Ten pieces of advice for getting out of stress” (YTN)", "The book asks you to circle the three that work best for you, write other strategies you use in Korean and discuss why they work with a classmate. The ten pieces of advice, with my English:", examples=passage(_STRESS7)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt and the instruction of 학습활동 2 (the English is mine):", examples=passage(_SPEAK7A)),
        card("Activities left out", "학습활동 1 (Reading, edunet4u.net): two cartoons (pictures). In the first you tick which healthy eating habits are mentioned (buy only organic produce; buy produce directly from the farmers; buy local produce; eat fruits and vegetables that are in season; eat only low-fat foods; minimize the use of canned or processed food); in the second you tick the main message (the importance of organic farming; the risks of pesticides; the risks of genetically modified produce). The cartoons are pictures, so I cannot tell which choices are right. 학습활동 3 (Listening, track 005): a YTN item on why laughter is good for health; you fill an English table of health benefits (it gives boosting the immune system and improving digestion). 학습활동 4 (Listening, track 006): a YTN item on walking; you write its health benefits in English. They are audio."),
    ],
    exercises=uniq(
        _tr(_STRESS7, k=3)
        + [M("What does the first piece of advice say?", "Get up fifteen minutes earlier", ["Sleep late", "Skip breakfast", "Work overtime"], "십오 분."), M("What should you do with your worries?", "Write them down concretely on paper", ["Keep them in your head", "Ignore them", "Post them online"], "종이에 써 보라."), M("What should you do about things you don’t want to do?", "Don’t put them off", ["Put them off", "Give them to others", "Forget them"], "미루지 말라."), M("How much should you exercise?", "Enough to break a sweat", ["Only a little", "Never", "Only at weekends"], "땀이 날만큼.")]
        + [F("어려움이 생기면 누구에게든 ___하라. (to consult)", "의논", ["충고", "미루"], "의논하다."), F("하기 싫은 일을 ___지 말라. (to put off)", "미루", ["의논하", "배제하"], "미루다."), F("책을 가지고 다니면서 ___ 읽어라. (in spare moments)", "틈틈이", ["제철", "수시로"], "틈틈이.")]
        + [read_q("아침에 십오 분만 일찍 일어나라"), read_q("나만의 공간을 가져라"), read_q("하기 싫은 일을 미루지 말라"), read_q("땀이 날만큼 운동을 하라")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 1", [
        ("가공식품", "(加工食品) processed food", "가공식품은 너무 자주 먹지 마세요."),
        ("고장(나다)", "(故障) trouble; breakdown (of machinery) (to stop working; to break down)", "제 차가 고장 나서 안 움직여요."),
        ("배제(하다/되다)", "(排除) exclusion (to exclude/to be excluded)", "김 씨가 범인일 가능성을 전혀 배제할 수는 없습니다.", "포함하다"),
        ("유사(하다)", "(類似) similarity; resemblance (to be similar)", "신제품의 기능이 기존 제품과 아주 유사합니다.", "비슷하다, 유사품"),
        ("유전자 조작", "(遺傳子 操作) genetic manipulation or modification", "유전자 조작 식품은 식용이 아니라 공업용으로 사용하는 경우가 많습니다."),
        ("자급자족(하다)", "(自給自足) self-sufficiency; “self-supply (and) self-sufficiency” (to be self-sufficient)", "우리나라는 식량을 자급자족합니다."),
        ("재배(하다/되다)", "(栽培) cultivation (of plants) (to grow; to cultivate/to be cultivated)", "이 작물은 남쪽 지방에서 재배됩니다.", "기르다"),
        ("제철", "in season; seasonal", "제철 과일"),
        ("조리(하다/되다)", "(調理) cooking (to cook/to be cooked)", "약한 불에서 한 삼십 분 정도 조리해 주세요.", "요리하다"),
    ]),
    ("학습활동 2", [
        ("공간", "(空間) space; room", "이 집에 그렇게 큰 가구를 넣을 공간은 없어요."),
        ("미루다", "to delay; to postpone; to put off", "갑자기 급한 일이 생겼어요. 약속시간을 좀 미룰 수 있을까요?"),
        ("용모", "(容貌) appearance (of a person); looks; features", "나는 용모에 대해 크게 고민해 본 적이 없다."),
        ("충고(하다)", "(忠告) advice (to advise)", "제 충고를 무시하지 마시고 잘 들어 주세요."),
        ("틈틈이", "in between times (in a busy schedule)", "저는 시간이 나면 틈틈이 운동을 합니다."),
    ]),
    ("학습활동 3", [
        ("근육", "(筋肉) muscle", "저는 근육을 키우기 위해 운동을 열심히 하고 있습니다.", "뼈"),
        ("내장기관", "(內臟器官) (internal) organs", ""),
        ("뇌", "(腦) brain", ""),
        ("복식호흡", "(腹式呼吸) abdominal breathing or respiration", ""),
        ("분비(하다/되다)", "(分泌) secretion (to secrete/to be secreted)", "십 대가 되면 호르몬이 왕성하게 분비됩니다.", "나오다"),
        ("산소", "(酸素) oxygen", ""),
        ("소화액", "(消化液) digestive fluid or juice", ""),
        ("완화(하다/되다)", "(緩和) relaxation; relief; alleviation (to relax; to relieve; to alleviate; to ease/to be relaxed; to be relieved; to be alleviated)", "정부는 국민들의 충격을 완화하기 위한 조치를 취했다."),
        ("자극(하다/받다)", "(刺戟) stimulation (to stimulate/to be stimulated)", "음식냄새가 식욕을 자극합니다."),
        ("침", "saliva; spit", "우표에 침을 발라 봉투에 붙입니다."),
        ("턱", "chin; (lower) jaw", "공이 날아와서 턱에 맞았어요."),
        ("항우울 호르몬", "(抗憂鬱) antidepressant hormone", ""),
        ("혈류", "(血流) bloodstream", "양파는 혈류를 원활하게 합니다."),
    ]),
    ("학습활동 4", [
        ("~ 보", "(步) a counter for a step or pace", "건강을 위해서 하루에 만 보씩 걸으세요."),
        ("간격", "(間隔) (time) interval; (space) distance or gap", "버스가 삼십 분 간격으로 운행됩니다."),
        ("물질대사", "(物質代謝) metabolism", "갑상선은 물질대사를 조절하는 호르몬을 분비합니다.", "신진대사"),
        ("벌리다", "to open; to spread", "지하철에서 다리를 벌리고 앉지 마세요."),
        ("보폭", "(步幅) a stride; a step; a pace; “step width”", "제 동생은 다리가 길어서 보폭이 넓어요."),
        ("복근", "(腹筋) abdominal muscles; abs", "저는 지금 복근 운동을 열심히 하고 있습니다."),
        ("엉덩이", "buttock; the back of the hip", "계속 앉아 있었더니 엉덩이가 아픕니다."),
        ("잡아당기다", "to pull; to draw; “to grab and pull”", "누가 옷을 잡아당겨서 뒤돌아 보았다."),
        ("정수리", "the crown (top) of the head", "저는 정수리 부분에 특히 흰 머리가 많이 납니다."),
        ("주먹", "a fist", "보통 심장의 크기는 자신의 주먹만 합니다."),
        ("혈액순환", "(血液循環) blood circulation", "운동을 하면 혈액순환도 잘 되고 건강에 좋습니다."),
    ]),
]
L3 = lesson(
    "U17 L7 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 가공식품 · 배제 · 유사 · 유전자 조작 · 자급자족 · 재배 · 제철 · 조리 · 미루다 · 용모 · 충고 · 틈틈이 · 근육 · 복식호흡 · 분비 · 완화 · 혈류 · 간격 · 물질대사 · 보폭 · 복근 · 주먹 · 혈액순환",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 내장기관, 뇌, 복식호흡, 산소, 소화액 and 항우울 호르몬. In the examples the book has 30분 (written 삼십 분 here), 10대 (십 대) and 30분 간격 (삼십 분 간격); the example of ~ 보 has 만 보 (ten thousand steps). 제철’s example is the phrase 제철 과일.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=16, nread=14)),
)

# ================================================================== L4 Part 2
_GARDEN7 = [
    ("실내 야채텃밭 가꾸기", "Tending an indoor vegetable garden"),
    ("주말농장이 부럽거나 텃밭을 갖고 싶지만, 마땅히 시작할 형편이 안 된다면 우선 실내에 새싹채소밭을 꾸며 보자.", "If you envy a weekend farm or want a vegetable plot but are in no position to start one, first set up a sprout-vegetable garden indoors."),
    ("베란다, 주방 등 실내에 채소밭을 꾸밀 때는 미니채소, 허브, 새싹채소가 제격이다.", "When you set up a vegetable garden indoors, such as on the veranda or in the kitchen, mini vegetables, herbs and sprouts are just right."),
    ("뿌리가 짧고, 크게 자라지 않고, 재배기간이 일반 채소보다 짧아 화분으로 손쉽게 기를 수 있기 때문이다.", "That is because their roots are short, they don’t grow big, and their growing period is shorter than that of ordinary vegetables, so they can easily be raised in pots."),
    ("화분에서 잘 자라는 채소는 수시로 잎을 떼어 사용하는 샐러드용과 뿌리를 먹을 수 있는 채소들이다.", "The vegetables that grow well in pots are those for salads, whose leaves you pick off whenever you like, and those whose roots you can eat."),
    ("직접 길러 먹기 때문에 방부제나 농약 걱정이 없어 씻을 때의 부담감도 덜어 준다.", "Because you grow and eat them yourself, there is no worry about preservatives or pesticides, which also takes away the burden of washing them."),
    ("다양한 품종으로 쉽고, 빠르게 수확의 기쁨을 맛보려면 새싹채소를 길러 보자.", "If you want to taste the joy of harvest easily and quickly with a variety of kinds, try growing sprout vegetables."),
    ("풍성한 계절, 가을에 앞서 새싹채소밭을 가꾸면 보는 맛, 키우는 맛, 먹는 맛을 모두 느낄 수 있다.", "If you tend a sprout garden ahead of the bountiful season, autumn, you can enjoy all of the pleasure of looking, of growing and of eating."),
]
_POLL7 = [
    ("외식비를 모아 유기농산물을 먹자.", "Let’s save up our money for eating out and eat organic produce."),
    ("환경호르몬을 피하는 가장 좋은 방법은 유기농산물을 먹는 것이다.", "The best way to avoid environmental hormones is to eat organic produce."),
    ("농약이나 화학비료를 사용하지 않은 깨끗한 농작물은 맛도 좋고 영양가도 상당히 높다.", "Clean crops grown without pesticides or chemical fertilizers taste good and are considerably high in nutritional value."),
    ("바쁘다는 이유로 자주 하는 외식.", "Eating out, which we often do because we are busy."),
    ("그 돈이면 유기농산물로 우리 가족 일주일치 식탁을 꾸릴 수 있다.", "With that money you can set our family’s table for a week with organic produce."),
    ("환경호르몬 농축 고기, 근해 생선보다는 원활한 배출을 돕는 채소를.", "Rather than meat and coastal-sea fish that concentrate environmental hormones, vegetables that help smooth discharge."),
    ("채소에 포함된 비타민, 미네랄 등은 몸속의 독소 배출을 원활하게 하기 때문에 환경호르몬을 비롯한 장애 물질들을 어느 정도 몸 밖으로 흘려보낸다.", "The vitamins, minerals and so on contained in vegetables make the discharge of toxins from the body smooth, so they flush hindering substances, including environmental hormones, out of the body to some extent."),
    ("만약 고기를 먹게 된다면 지방이 적은 부위를 택해 섭취하는 것이 좋다.", "If you do end up eating meat, it is good to choose and eat a part with little fat."),
]
_SPEAK7B = [
    ("주변에 환경호르몬을 유발시키는 음식에는 어떤 것이 있는 생각해 보고 열거해 보세요.", "Think about what foods around you cause environmental hormones, and list them."),
    ("그리고 환경호르몬 섭취를 줄이기 위해서 어떤 노력이 필요할지 이야기해 보세요.", "Then talk about what effort is needed to reduce your intake of environmental hormones."),
    ("현재 섭취하고 있는 비타민이나 건강 보조 식품이 있습니까?", "Are there any vitamins or health supplements you are taking now?"),
    ("비타민이나 건강 보조 식품 섭취에 대해서 어떤 의견을 가지고 있는지 이야기해 보세요.", "Talk about what opinion you have of taking vitamins or health supplements."),
    ("집에서 채소나 과일을 길러 본 경험에 대해 친구들과 이야기해 보세요.", "Talk with your friends about your experiences growing vegetables or fruit at home."),
]
L4 = lesson(
    "U17 L7 · Part 2 (본 학습): an indoor vegetable garden and organic produce",
    "본 학습 · 실내 야채텃밭 · 새싹채소 · 화분 · 방부제 · 농약 · 환경호르몬 · 유기농산물 · 외식비 · 배출 · 독소 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: a magazine article “Tending an indoor vegetable garden” (Kyunghyang)", "The book asks four questions: (1) who would be interested in an indoor vegetable garden; (2) which vegetables are recommended and why; (3) what the benefits are; (4) discuss in Korean your experiences growing vegetables or fruit. The article, with my English, and my answers:", examples=passage(_GARDEN7)),
        card("My answers to 학습활동 1", "1. People who envy weekend farms or want a vegetable plot but are in no position to start one. 2. Mini vegetables, herbs and sprout vegetables, because their roots are short, they do not grow big, and their growing period is shorter than that of ordinary vegetables, so they are easily grown in pots; vegetables for salads (picked leaf by leaf) and root vegetables also grow well in pots. 3. No worry about preservatives or pesticides, which lightens the burden of washing; an easy and quick joy of harvest with a variety of kinds; the pleasure of looking, growing and eating."),
        card("학습활동 3: “Let’s save up our money for eating out and eat organic produce” (Kyunghyang)", "The book asks you to fill an English table (suggestion for reducing pollutant intake / reasons) and to list in Korean ideas for reducing your intake of pollutants (“environmental hormone”) and discuss them as a class. The title and the sentence beginning “환경호르몬 농축 고기” are headings in the book; the book ends the title with “!” and the heading with “…!”, which I changed to periods because they cannot be read aloud as such:", examples=passage(_POLL7)),
        card("My answers to 학습활동 3", "Suggestion: eat organic produce (spend the eating-out money on organic produce for the family’s week). Reasons: clean crops grown without pesticides or chemical fertilizers taste good and are high in nutrition; vegetables’ vitamins and minerals help discharge toxins, including environmental hormones; and if you eat meat, choose parts with little fat."),
        card("말해 봅시다! (speaking) and 학습활동 1, task 4", "The book’s two speaking prompts of Part 2 (the first is typed “있는 생각해 보고” in the book, where “있는지” is meant; I kept the book’s text), followed by the task of 학습활동 1 (the English is mine):", examples=passage(_SPEAK7B)),
        card("Activities left out", "학습활동 2 (Listening, tracks 007 to 009): a YTN interview in three parts about vitamins. You summarize in English how vitamins function by the interviewee’s car-engine comparison, answer why people take multivitamins and what he recommends, and fill a table of who should take additional vitamins (pregnant women, people on a diet, smokers, drinkers, people taking aspirin for arthritis) and why. It is audio. The cartoon pictures of Part 1 are also left out."),
    ],
    exercises=uniq(
        _tr(_GARDEN7[1:], k=3) + _tr(_POLL7[1:], k=3)
        + [M("Who is the article of the indoor garden for?", "People who want a vegetable plot but cannot start one", ["Professional farmers", "Restaurant owners", "Children only"], "형편이 안 된다면."), M("Which kinds of plants does the article call just right for indoors?", "Mini vegetables, herbs and sprout vegetables", ["Large fruit trees", "Rice and wheat", "Sweet potatoes only"], "제격이다."), M("Why are they easy to raise in pots?", "Short roots, small growth and a short growing period", ["They need no water", "They grow only in autumn", "They are sold in pots"], "뿌리가 짧고."), M("What worry does growing your own vegetables remove?", "Worry about preservatives and pesticides", ["Worry about the price of seeds", "Worry about the weather", "Worry about the neighbors"], "방부제나 농약 걱정."), M("What does the second article say is the best way to avoid environmental hormones?", "Eating organic produce", ["Eating out often", "Eating more meat", "Eating coastal fish"], "유기농산물을 먹는 것."), M("What should you do if you eat meat?", "Choose a part with little fat", ["Choose the fattest part", "Eat it every day", "Eat it raw"], "지방이 적은 부위."), M("What does the article say vegetables’ vitamins and minerals do?", "Help flush toxins out of the body", ["Add fat to the body", "Cause environmental hormones", "Raise the price of meals"], "독소 배출.")]
        + [F("뿌리가 짧고 크게 자라지 않아 ___로 손쉽게 기를 수 있다. (a pot)", "화분", ["텃밭", "베란다"], "화분."), F("직접 길러 먹기 때문에 ___나 농약 걱정이 없다. (preservative)", "방부제", ["허브", "독소"], "방부제."), F("농약이나 ___를 사용하지 않은 깨끗한 농작물은 맛도 좋다. (chemical fertilizer)", "화학비료", ["새싹채소", "환경호르몬"], "화학비료."), F("채소는 몸속의 ___ 배출을 원활하게 한다. (toxin)", "독소", ["방부제", "근해"], "독소."), F("고기를 먹게 된다면 ___이 적은 부위를 택하는 것이 좋다. (fat)", "지방", ["단백질", "철분"], "지방.")]
        + [read_q("실내에 새싹채소밭을 꾸며 보자"), read_q("직접 길러 먹기 때문에 방부제나 농약 걱정이 없다"), read_q("환경호르몬을 피하는 가장 좋은 방법은 유기농산물을 먹는 것이다"), read_q("지방이 적은 부위를 택해 섭취하는 것이 좋다")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("방부제", "(防腐劑) preservative", "이 빵에는 방부제가 너무 많이 들어 있어요."),
        ("뿌리", "root", "감자나 고구마는 뿌리를 먹는 음식입니다."),
        ("허브", "herb", "두통이 있을 때 허브를 방에 놓아 두면 도움이 됩니다."),
        ("화분", "(花盆) a flowerpot; a pot", "화분에 물을 좀 주세요."),
    ]),
    ("학습활동 2", [
        ("관절염", "(關節炎) arthritis; joint inflammation", ""),
        ("구성성분", "(構成成分) a constituent; an element; a component", "혈액의 구성성분이 무엇입니까?"),
        ("단백질", "(蛋白質) protein", ""),
        ("대사작용", "(代謝作用) metabolism", "인체는 날씨에 따라 대사작용을 합니다.", "물질대사"),
        ("미네랄", "mineral", ""),
        ("보충(하다/되다)", "(補充) supplement (to supplement/to be supplemented)", "부족한 영양분을 보충하기 위해 보조식품을 먹습니다."),
        ("세포", "(細胞) cell (in the body)", ""),
        ("원활하다", "(圓滑) to be smooth (in operation)", "일이 원활하게 진행되고 있습니다."),
        ("윤활유", "(潤滑油) lubricant; lubricating oil", "자동차 윤활유를 바꿔야 합니다."),
        ("임산부", "(姙産婦) a pregnant woman", "버스에 임산부 전용좌석이 있습니다."),
        ("짚다", "to point; to address", "이 문제는 꼭 짚고 넘어갑시다."),
        ("철분", "(鐵分) iron", ""),
        ("촉매", "(觸媒) catalyst", "주가 하락이 유가 상승의 촉매 역할을 했습니다."),
        ("탄수화물", "(炭水化物) carbohydrate", ""),
        ("합성(하다/되다)", "(合成) composition; synthesis (to compose; to synthesize/to be composed; to be synthesized)", "비타민은 우리 몸에서 합성되지 않습니다."),
    ]),
    ("학습활동 3", [
        ("근해", "(近海) adjacent (neighboring) seas; coastal (home) waters", "이 근해에서는 고등어가 많이 잡힙니다."),
        ("독소", "(毒素) toxin; poisonous substance (matter)", "우리 몸은 음식물의 독소를 제거할 수 있습니다."),
    ]),
]
L5 = lesson(
    "U17 L7 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 방부제 · 뿌리 · 허브 · 화분 · 관절염 · 구성성분 · 단백질 · 대사작용 · 미네랄 · 보충 · 세포 · 원활하다 · 윤활유 · 임산부 · 짚다 · 철분 · 촉매 · 탄수화물 · 합성 · 근해 · 독소",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 관절염, 단백질, 미네랄, 세포, 철분 and 탄수화물. 대사작용 has 물질대사 as a related word; 짚다 is glossed “to point; to address”, as in the example, where it means to deal with a problem before moving on.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=12, nread=10)),
)

# ================================================================== L6 Part 3
_GMO7 = [
    ("유전자조작농산물이 최초로 등장한 것은 천구백구십사 년이다.", "Genetically modified agricultural products first appeared in 1994."),
    ("미국 칼진사는 얼지 않는 성질을 가진 넙치의 유전자를 떼어 내 토마토에 이식함으로써 ‘무르지 않는 토마토’를 개발했다.", "The American company Calgene developed a “tomato that does not turn soft” by taking a gene of a flounder, which has the property of not freezing, and transplanting it into a tomato."),
    ("지엠오 식품은 ‘프랑켄슈타인 식품’으로도 불린다.", "GMO food is also called “Frankenstein food”."),
    ("천팔백십팔 년 발표된 영국 소설 ‘프랑켄슈타인’에서 괴물을 만들어 낸 물리학자 프랑켄슈타인에 비유한 것을 보면 자연의 섭리를 거스르는 데 대한 충격과 공포 등 불안심리가 반영된 것으로 보인다.", "Seeing that it is compared to the physicist Frankenstein, who made a monster in the English novel “Frankenstein” published in 1818, it seems to reflect anxiety, such as shock and fear at going against the principles of nature."),
    ("이후 십여 년 동안 ‘식량증산’을 구실로 한 지엠오 개발 경쟁은 가속화했다.", "For more than ten years after that, the competition to develop GMOs, with “increased food production” as the pretext, accelerated."),
    ("콩, 옥수수, 목화, 카놀라가 대표적인 지엠오로 자리잡았다.", "Soybeans, corn, cotton and canola became established as the representative GMOs."),
    ("지엠오 재배가 시작된 구십육 년 이후 재배면적이 육십칠 배 늘고, 지엠오 식품 수도 크게 증가했다.", "Since 1996, when GMO cultivation began, the cultivated area has grown 67 times, and the number of GMO foods has also increased greatly."),
    ("하지만 지엠오가 확산됐다 해서 인체 유해성 논란이 사그라든 것은 아니다.", "But the spread of GMOs has not made the controversy over harm to the human body die down."),
    ("‘안전성이 확실하게 검증되지 않는 한 먹어서는 안 된다. 유해성이 이 대, 삼 대에 걸쳐 나타날 수 있다’는 환경론자들의 주장과 ‘인체에 유해하다는 것이 밝혀진 바 없다’는 찬성론자 간의 논란은 계속되고 있다.", "The dispute continues between the environmentalists’ claim that “you must not eat it unless its safety is verified for certain; the harm may appear over two or three generations” and the supporters’ claim that “it has not been shown to be harmful to the human body.”"),
    ("우리나라 전분당 시장의 구십 퍼센트를 점유하는 대상 등 네 개 회사가 오 월부터 지엠오 옥수수를 들여와 전분당 원료로 쓰겠다고 발표해 안전성 논란이 재연되고 있다.", "The safety controversy has flared up again because four companies, including Daesang, which holds 90 percent of the domestic starch-sugar market, announced that from May they would bring in GMO corn and use it as a raw material for starch sugar."),
    ("비지엠오 옥수수 값이 폭등한 데다 구하기도 어려워 지엠오 옥수수 수입이 불가피하다는 것이 회사측 얘기다.", "The companies say that importing GMO corn is unavoidable because the price of non-GMO corn has soared and it is also hard to obtain."),
    ("전분당은 과자, 음료수, 빙과류 등 거의 모든 가공식품과 음식조리에 들어가는 원재료여서 파장이 클 수밖에 없다.", "Starch sugar is a raw material that goes into almost all processed foods and cooking, such as snacks, beverages and frozen confections, so the ripple effect cannot help being large."),
    ("문제는 가공과정의 특성상 지엠오 옥수수 전분당을 넣더라도 완제품에서는 지엠오 성분이 검출되지 않아 소비자가 알 수 없다는 점이다.", "The problem is that, owing to the nature of the processing, even if GMO corn starch sugar is put in, no GMO component is detected in the finished product, so consumers cannot know."),
    ("식품표시제를 강화하든 어떤 형태로든지 소비자의 ‘먹지 않을 권리’를 보장하는 방안을 찾아야 한다.", "Whether by strengthening the food labeling system or in some other form, a way must be found to guarantee consumers’ “right not to eat”."),
]
_SPEAK7C = [("유전자조작식품의 여러 사례를 열거해 보세요.", "List various examples of genetically modified food."), ("그리고 유전자조작식품의 장단점에 대해 비교해서 이야기해 보세요.", "Then compare and talk about the advantages and disadvantages of genetically modified food.")]
L6 = lesson(
    "U17 L7 · Part 3 (심화 학습): genetically modified agricultural products",
    "심화 학습 · 유전자조작농산물 · 지엠오 · 프랑켄슈타인 식품 · 토마토 · 전분당 · 검출 · 먹지 않을 권리 · 식품표시제",
    requires=[],
    cards=[
        card("학습활동 3: an article on genetically modified agricultural products (Kyunghyang)", "The book writes GMO in Latin letters, years and numbers in digits, and uses “•” between the crops; for reading aloud I spelled them in Hangul (지엠오 for GMO) and used commas. The article, with my English:", examples=passage(_GMO7)),
        card("My answers to 학습활동 3", "1. The figurative word is 프랑켄슈타인 식품 (“Frankenstein food”): GMO food is compared to the physicist Frankenstein, who made a monster in the 1818 English novel, which reflects the anxiety, shock and fear at going against the principles of nature. 2. The first was a tomato that does not turn soft (1994, with a flounder gene), followed by soybeans, corn, cotton and canola; since 1996 the cultivated area has grown 67 times and the number of GMO foods has increased greatly. 3. D (starch sugar is the raw material of almost all processed foods; the companies announced that they will import GMO corn, not that they won’t). The book says “cornstarch” where the text has 전분당, “sugar from starch”. 4. Four companies holding 90 percent of the market announced that they would use imported GMO corn, so the safety controversy flared up again. 5. Even if GMO corn starch sugar is used, no GMO component is detected in the finished product, so consumers cannot know. 6. The author argues that the food labeling system must be strengthened, or some other way found, so as to guarantee the consumers’ “right not to eat”."),
        card("말해 봅시다! (speaking)", "", examples=passage(_SPEAK7C)),
        card("Activities left out", "학습활동 1 (Listening, track 010): a YTN news report about vitamin rice (비타민 쌀): you answer in English how it is produced, fill a table on the health benefits of orange rice and red rice, say why it takes five to six years for it to reach the market, and what its industrial benefits are. 학습활동 2 (Listening, track 011): a YTN video about genetically modified agricultural products: you fill an English table on the researcher’s biographical information, the experimental method, and the result and implication of the research. They are audio."),
    ],
    exercises=uniq(
        _tr(_GMO7, k=3)
        + [M("When did genetically modified produce first appear, according to the article?", "1994", ["1818", "1996", "1967"], "천구백구십사 년."), M("Which gene went into the tomato?", "A flounder’s gene (not freezing)", ["A rice gene", "A corn gene", "A potato gene"], "넙치."), M("What is GMO food also called?", "Frankenstein food", ["Monster crop", "Bio tomato", "Organic food"], "프랑켄슈타인 식품."), M("Which of these is not named as a representative GMO crop?", "Rice", ["Soybeans", "Corn", "Cotton"], "콩, 옥수수, 목화, 카놀라."), M("Why do the companies say GMO corn imports are unavoidable?", "Non-GMO corn became very expensive and hard to get", ["GMO corn tastes better", "Consumers asked for it", "It is cheaper to ship"], "값이 폭등한 데다."), M("What is the consumers’ problem with starch sugar made from GMO corn?", "No GMO component is detected in the finished product, so they cannot know", ["It is too sweet", "It is not sold in Korea", "It contains no starch"], "검출되지 않아."), M("What does the author want to guarantee?", "Consumers’ right not to eat", ["Companies’ right to import", "Farmers’ right to export", "A lower price for corn"], "먹지 않을 권리.")]
        + [F("지엠오 식품은 ‘프랑켄슈타인 식품’으로도 ___. (is called)", "불린다", ["만든다", "먹는다"], "불리다."), F("지엠오가 확산됐다 해서 유해성 ___이 사그라든 것은 아니다. (controversy)", "논란", ["섭리", "권리"], "논란."), F("완제품에서는 지엠오 성분이 ___되지 않아 소비자가 알 수 없다. (be detected)", "검출", ["폭등", "합성"], "검출."), F("소비자의 ‘먹지 않을 ___’를 보장하는 방안을 찾아야 한다. (a right)", "권리", ["충격", "괴물"], "권리.")]
        + [read_q("프랑켄슈타인 식품으로도 불린다"), read_q("인체 유해성 논란이 사그라든 것은 아니다"), read_q("완제품에서는 성분이 검출되지 않아 소비자가 알 수 없다"), read_q("소비자의 먹지 않을 권리를 보장해야 한다")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("결합(하다/되다)", "(結合) combination; union; fusion (to combine; to unite/to be combined; to be united)", "이 영화는 훌륭한 음악과 아름다운 영상이 결합된 작품입니다."),
        ("고추", "pepper", ""),
        ("관여(하다)", "(關與) involvement; intervention (to have a part in; to involve; to intervene; to be concerned)", "저는 이 일에 별로 관여하고 싶지 않아요."),
        ("노화(하다; 되다)", "(老化) aging; “getting old” (to age)", "과학자들은 노화현상에 대해 연구하고 있습니다.", "늙다, 나이가 들다"),
        ("변형(하다/되다)", "(變形) modification (to modify; to transform into/to be modified; to be transformed)", "그 화가는 같은 주제를 다양하게 변형해서 그림을 그립니다.", "바뀌다, 변화하다"),
        ("성분", "(成分) an ingredient; a component; a constituent", "유기농 우유와 일반 우유가 성분은 같다고 합니다."),
        ("추구(하다)", "(追求) pursuit (to pursue; to seek)", "모든 사람은 행복을 추구할 권리가 있다."),
        ("추출(하다/되다)", "(抽出) extraction (to extract/to be extracted)", "이 전분은 감자에서 추출해서 만들었습니다."),
        ("항산화", "(抗酸化) antioxidant", "항산화 물질, 항산화제", "산화"),
    ]),
    ("학습활동 2", [
        ("생물학자", "(生物學者) a biologist", ""),
        ("손상(되다)", "(損傷) damage (to be damaged)", "아버지는 교통사고로 뇌가 조금 손상되었다고 합니다."),
        ("실험", "(實驗) an experiment", "그 기술은 아직 실험 단계에 있습니다."),
        ("위축(되다)", "(萎縮) shrinking; withering; contracting (to be shrunken; to be intimidated; to be contracted)", "저는 아버지 앞에만 가면 위축되어 말을 잘 못 합니다."),
        ("입증(하다/되다)", "(立證) proof (to prove/to be proved)", "피고의 결백이 입증되었습니다."),
        ("장", "(腸) intestine", "장 운동이 활발하지 못해 변비에 걸립니다.", "대장, 소장, 십이지장"),
        ("장기간", "(長期間) long time; long period", "", "단기간"),
        ("저명하다", "(著名) to be famous; to be well known", "이 분은 세계적으로 저명한 과학자입니다.", "유명하다"),
        ("채취(하다/되다)", "(採取) gathering; collecting; taking (of blood, fingerprints, etc.) (to gather; to collect; to take/to be gathered; to be collected; to be taken; to be extracted)", "경찰은 범행 현장에 남겨진 혈액을 채취하여 용의자를 찾고 있습니다."),
        ("치명적", "(致命的) fatal; mortal; deadly; lethal", "치명적 바이러스 때문에 보건에 비상이 걸렸습니다."),
        ("해충", "(害蟲) harmful insect; vermin", "올해는 해충 때문에 농사가 잘 되지 않았어요."),
    ]),
    ("학습활동 3", [
        ("강화(하다/되다)", "(强化) reinforcement (to reinforce; to strengthen/to be reinforced; to be strengthened)", "경찰은 불법 주차 단속을 강화하겠다고 발표했습니다.", "약화되다"),
        ("거스르다", "to counter; to resist; to go against", "그것은 법을 거스르는 일입니다."),
        ("검증(하다/되다)", "(檢證) verification (to verify/to be verified)", "이 이론은 실제에서 검증되지 않았습니다.", "입증하다"),
        ("검출(하다/되다)", "(檢出) detection (of a chemical substance) (to detect/to be detected)", "이 지역 수돗물에서 방사능이 검출되었다고 합니다."),
        ("괴물", "(怪物) a monster", "그는 나를 괴물을 보는 것처럼 쳐다봤다."),
        ("권리", "(權利) a right", "모든 국민은 알 권리가 있습니다."),
        ("넙치", "a flounder; a flatfish; a halibut", ""),
        ("목화", "(木花) cotton (flower/plant); “tree flower”", ""),
        ("무르다", "to be overripe (fruits or vegetables); to be weak; to be softhearted", "토마토가 너무 익어서 다 물렀어요."),
        ("불가피하다", "(不可避) to be inevitable; to be unavoidable", "불가피한 사정으로 회의를 연기할 수밖에 없습니다."),
        ("비유(하다/되다)", "(比喩) figure of speech; comparison (to figuratively express; to compare/to be figuratively expressed; to be compared)", "흔히 착한 사람을 천사에 비유합니다."),
        ("섭리", "(攝理) principles and rules governing nature; providence", "신의 섭리. 자연의 섭리."),
        ("전분당", "(澱粉糖) sugar from starch", ""),
        ("충격", "(衝擊) impact; shock", "저는 처음에 유학 와서 문화적 충격이 아주 심했습니다."),
        ("카놀라", "canola", ""),
        ("폭등(하다)", "(暴騰) soaring; sudden price increase (to soar; to skyrocket; to increase suddenly)", "추위로 농산물 가격이 폭등했습니다.", "급등하다 / 폭락하다, 급락하다"),
    ]),
]
L7 = lesson(
    "U17 L7 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 결합 · 관여 · 노화 · 변형 · 성분 · 추구 · 추출 · 항산화 · 손상 · 실험 · 위축 · 입증 · 장기간 · 저명하다 · 채취 · 치명적 · 해충 · 강화 · 거스르다 · 검증 · 검출 · 괴물 · 권리 · 넙치 · 불가피하다 · 비유 · 섭리 · 전분당 · 충격 · 폭등",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 고추, 생물학자, 장기간, 넙치, 목화, 전분당 and 카놀라. In the book 항산화 has “항산화 물질, 항산화제” as its example and 산화 as a related word; 섭리 has two example phrases; 폭등하다 lists 급등하다 as similar and 폭락하다, 급락하다 as opposites (written here with a slash). 목화 is glossed “tree flower”, which is the literal meaning of its two characters.")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 7: Healthy Living (건강한 생활)", [L1, L2, L3, L4, L5, L6, L7])
