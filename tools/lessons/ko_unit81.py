"""Unit 81: KBC Semester III, Unit 17, Lesson 6 - Modern Diseases II (현대병 II).
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
_MATCH6 = [("기절하다", "to faint; to pass out", "놀라서 기절하다"), ("치료하다", "to give medical treatment", "의사가 환자를 치료하다"), ("참다", "to bear; to endure; to be patient", "고통을 참다"), ("어지럽다", "to be dizzy", "머리가 어지럽다"), ("검진하다", "to give a medical examination", "환자를 검진하다"), ("수술하다", "to operate (surgery)", "암환자를 수술하다"), ("감염되다", "to be infected", "감기에 감염되다"), ("입원하다", "to be hospitalized", "병원에 입원하다"), ("긁다", "to scratch; to scrape", "상처 부위를 긁다"), ("복용하다", "to take (medicine)", "두통약을 복용하다")]
_HJ6 = [("炎 염", "flame; inflammation", "염증, 폭염"), ("定 정", "set", "결정, 측정"), ("體 체", "body", "체격, 체온"), ("處 처", "place; spot", "처벌, 상처"), ("態 태", "situation; condition", "중태, 상태")]
_HJW6 = [("염증", "infection; inflammation"), ("폭염", "a heat wave"), ("결정", "decision; decision making"), ("측정", "measurement"), ("체격", "the frame of a body; body structure"), ("체온", "body temperature"), ("처벌", "punishment"), ("상처", "an injury; a scar; a bruise"), ("중태", "a serious condition"), ("상태", "a situation; a condition")]
_SIM6 = [("상처", "외상", "wound: external injury"), ("한정", "제한", "limitation: restriction"), ("체중", "몸무게", "body weight: weight"), ("태도", "자세", "attitude: posture; stance")]
_REL6 = [("A", "염증", "비염, 간염, 기관지염", "inflammation"), ("B", "온도", "체온, 기온, 수온", "temperature"), ("C", "신체검사", "신장측정, 체중검사, 시력측정", "a physical examination"), ("D", "부상", "경상, 중상, 상처", "an injury")]
_L6X = [("처방", "a prescription"), ("처치", "treatment; dealing with"), ("외상", "an external injury"), ("정기", "regular (periodic)"), ("질환", "an ailment"), ("한정", "limitation"), ("제한", "restriction"), ("사태", "a situation; an affair"), ("자세", "a posture; an attitude"), ("검진", "a medical examination"), ("인정", "recognition; acceptance"), ("태도", "an attitude"), ("몸살", "aches from fatigue or a cold"), ("키", "height"), ("신장", "height; the kidney"), ("몸무게", "body weight"), ("체중", "body weight"), ("비염", "rhinitis"), ("간염", "hepatitis"), ("기관지염", "bronchitis"), ("기온", "air temperature"), ("수온", "water temperature"), ("신장측정", "height measurement"), ("체중검사", "a weight check"), ("시력측정", "an eyesight test"), ("경상", "a minor injury"), ("중상", "a serious injury"), ("부상", "an injury"), ("신체검사", "a physical examination"), ("감정", "feeling"), ("온도", "temperature"), ("동맥경화", "arteriosclerosis"), ("신종플루", "the new flu"), ("폐암", "lung cancer"), ("당뇨병", "diabetes"), ("비만", "obesity")]
L1 = lesson(
    "U17 L6 · Review: treatment words and Sino-Korean 炎 定 體 處 態",
    "현대병 II · 단어 복습 · 한자어 복습 · 기절 · 치료 · 검진 · 수술 · 감염 · 입원 · 복용 · 炎 定 體 處 態",
    requires=[],
    cards=[
        card("단어 복습 1: the underlined words (the book’s matching)", "The book gives ten phrases with one word underlined and asks you to connect each underlined word with its English meaning on the right. The underline is not marked in the text; the pairs are:", tables=[table(["Word", "Meaning", "Phrase"], [list(r) for r in _MATCH6], say=[0, 2])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ6], say=[2]), ktable(_HJW6)]),
        card("한자어 복습 1: the most similar word (my answers)", "Circle the word with the most similar meaning to the word on the left (A. 상처: 처방, 처치, 외상, 감염; B. 한정: 정기, 질환, 제한, 상태; C. 체중: 몸살, 키, 몸무게, 신장; D. 태도: 사태, 자세, 검진, 인정).", tables=[table(["Word", "Similar (my answer)", "Meaning"], [list(r) for r in _SIM6], say=[0, 1])]),
        card("한자어 복습 2: the word that holds all three (my answers)", "Choose from the box (신체검사, 염증, 부상, 감정, 온도) the word that can include all three words; 감정 is left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Meaning"], [list(r) for r in _REL6], say=[1, 2])]),
        card("Activities left out", "단어 복습 2 (Listening, tracks 001 to 005): five audio descriptions of diseases and their symptoms, which you connect with the disease names 동맥경화, 신종플루, 폐암, 당뇨병 and 비만. The disease words are in the next card."),
        card("More words from these exercises", "", tables=[ktable(_L6X)]),
    ],
    exercises=uniq(
        _tr([(a, b) for a, b, c in _MATCH6], k=3) + _tr(_HJW6, k=3) + _tr(_L6X, k=3) + _tr([(a, c) for a, b, c in _SIM6], k=3)
        + [M("What does the syllable 炎 (염) mean?", "flame; inflammation", ["set", "body", "place"], "염증."), M("What does the syllable 定 (정) mean?", "set", ["flame", "body", "place"], "측정."), M("What does the syllable 體 (체) mean?", "body", ["flame", "set", "situation"], "체온."), M("What does the syllable 處 (처) mean?", "place; spot", ["flame", "set", "body"], "상처."), M("What does the syllable 態 (태) mean?", "situation; condition", ["flame", "set", "body"], "상태.")
           , M("Which word is similar to 상처?", "외상", ["처방", "처치", "감염"], "External injury."), M("Which word is similar to 한정?", "제한", ["정기", "질환", "상태"], "Restriction."), M("Which word is similar to 체중?", "몸무게", ["몸살", "키", "신장"], "Weight."), M("Which word is similar to 태도?", "자세", ["사태", "검진", "인정"], "Posture."), M("Which word holds 비염, 간염, 기관지염?", "염증", ["온도", "부상", "신체검사"], "Inflammation."), M("Which word holds 체온, 기온, 수온?", "온도", ["염증", "부상", "신체검사"], "Temperature."), M("Which word holds 경상, 중상, 상처?", "부상", ["염증", "온도", "신체검사"], "Injury.")
           , F("놀라서 ___했습니다. (to faint)", "기절", ["복용", "검진"], "기절하다."), F("두통약을 ___합니다. (to take medicine)", "복용", ["입원", "수술"], "복용하다."), F("암환자를 ___합니다. (to operate)", "수술", ["입원", "복용"], "수술하다."), F("병원에 ___합니다. (to be hospitalized)", "입원", ["기절", "치료"], "입원하다."), F("고통을 ___. (to endure)", "참습니다", ["긁습니다", "복용합니다"], "참다.")]
        + [read_q("놀라서 기절했습니다"), read_q("의사가 환자를 치료합니다"), read_q("감기에 감염되었습니다"), read_q("두통약을 복용합니다")]
    ),
)

# ================================================================== L2 Part 1
_NK6 = [("닭알", "계란, 달걀", "egg (North Korean; South Korean)"), ("손전화", "핸드폰", "mobile phone"), ("도마도", "토마토", "tomato")]
_SPEAK6A = [("건강한 생활을 하기 위해서 어떤 생활습관이 필요한지 반 친구들과 이야기해보세요.", "Talk with your classmates about what lifestyle habits are needed to live a healthy life.")]
L2 = lesson(
    "U17 L6 · Part 1 (도입 학습): North and South Korean words and a speaking prompt",
    "도입 학습 · 닭알 · 손전화 · 도마도 · 솔잎 · 솔꽃가루 · 생활습관 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 4: North Korean words and their South Korean equivalents", "The activity is a North Korean health-tips broadcast (track 008) on how pine needles and pine pollen are good for health. Before it, the book asks you to match each North Korean term with its South Korean equivalent. My answers:", tables=[table(["North Korean", "South Korean", "Meaning"], [list(r) for r in _NK6], say=[0, 1])]),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK6A)),
        card("Activities left out", "학습활동 1 (Reading): three pictures about disease, with three choices each to tick. Picture 1 (edunet4u.net): cancers many Koreans get; cancers many Korean women get; cancers many children get. Picture 2 (Kyunghyang): causes of women’s cancers; regular cancer screening; women’s big three cancers. Picture 3 (Kyunghyang): the effects of regular exercise; exercise that guards against dementia; physical and mental exercise. The pictures are not in the text, so I cannot tell which choices are right. 학습활동 2 (Listening, tracks 006 and 007): YTN news items about diseases, with a table of the disease and the case. 학습활동 3: a partner activity on rules for preventing cancer (each partner holds a different picture and explains the blanks in Korean). 학습활동 4 (Listening): a North Korean broadcast; you list the nutritional content and value of pine needles and pollen, and at least three diseases they are said to cure. They are audio, pictures or pair work."),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _NK6], k=3)
        + [M("What is the South Korean word for the North Korean 손전화?", "핸드폰", ["토마토", "달걀", "솔잎"], "Mobile phone."), M("What is the South Korean word for the North Korean 도마도?", "토마토", ["핸드폰", "달걀", "솔꽃"], "Tomato."), M("What is the South Korean word for the North Korean 닭알?", "달걀", ["핸드폰", "토마토", "알약"], "Egg."), M("What does the North Korean broadcast introduce?", "How pine needles and pine pollen are good for health", ["How to cook kimchi", "How to buy a mobile phone", "How to cure a cold"], "솔잎.")]
        + [read_q("닭알은 북한에서 쓰는 말입니다"), read_q("건강한 생활을 하기 위해서 어떤 생활습관이 필요합니까")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 2", [
        ("결핵", "(結核) tuberculosis", ""),
        ("고혈압", "(高血壓) high blood pressure", "", "저혈압"),
        ("뇌혈관", "(腦血管) cerebrovascular; “brain blood vessel”", ""),
        ("신장암", "(腎臟癌) cancer of the kidney", ""),
        ("자각(하다)", "(自覺) self-awareness (to realize)", "그 사람은 자신이 범죄를 저지르고 있다는 사실을 자각하지 못했습니다.", "깨닫다, 알다"),
        ("자궁암", "(子宮癌) uterine cancer", ""),
    ]),
    ("학습활동 3", [
        ("과도하다", "(過度) to be excessive", "과도한 음주는 건강에 해롭다.", "지나치다"),
        ("그을다", "to coat or cover with soot; to soot", "연기가 나서 프라이팬이 까맣게 그을었습니다.", "그을음"),
        ("편식(하다)", "(偏食) picky eating; “one-sided eating” (to eat only what one wants)", "편식하는 버릇은 어릴 때 고쳐야 합니다."),
    ]),
    ("학습활동 4", [
        ("간염", "(肝炎) hepatitis", ""),
        ("솔꽃", "a pine flower", "", "솔나무의 꽃"),
        ("솔꽃가루", "pine pollen; “pine flower powder”", ""),
        ("신경통", "(神經痛) neuralgia", ""),
        ("알약", "a tablet; a pill", "우리 아이는 너무 어려서 아직 알약을 못 먹습니다."),
        ("위질환", "(胃疾患) gastropathy; “stomach disease”", ""),
        ("취장염", "(膵臟炎) pancreatitis", "", "췌장염"),
        ("효소", "(酵素) enzyme", ""),
    ]),
]
L3 = lesson(
    "U17 L6 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 결핵 · 고혈압 · 뇌혈관 · 신장암 · 자각 · 자궁암 · 과도하다 · 그을다 · 편식 · 간염 · 솔꽃가루 · 신경통 · 알약 · 위질환 · 취장염 · 효소",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for most of the disease words (결핵, 고혈압, 뇌혈관, 신장암, 자궁암, 간염, 솔꽃, 솔꽃가루, 신경통, 위질환, 취장염, 효소); 솔꽃 is explained as “솔나무의 꽃”. The book prints 취장염 and gives 췌장염 beside it; 췌장염 is the usual spelling.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=8)),
)

# ================================================================== L4 Part 2
_KIM6 = [
    ("김치는 암을 일으키는가? 암 예방에 좋은가?", "Does kimchi cause cancer? Is it good for cancer prevention?"),
    ("우리나라의 김치는 섬유질이 풍부한 저지방 다이어트 음식이어서 일본의 콩, 인도의 렌틸 콩, 스페인의 올리브 오일, 그리스의 요구르트와 더불어 세계 오대 건강식품으로 선정되었다고 해서 화제다.", "It is the talk of the town that our country’s kimchi, being a low-fat diet food rich in fiber, was chosen as one of the world’s five great health foods along with Japan’s soybeans, India’s lentils, Spain’s olive oil and Greece’s yogurt."),
    ("김치에는 비타민 에이, 비, 씨 등 비타민과 유산균도 많고, 이것들이 암세포 증식도 막아 주기 때문이라고 한다.", "They say this is because kimchi has many vitamins such as A, B and C and lactic acid bacteria, and these also block the proliferation of cancer cells."),
    ("김치 속에 들어 있는 마늘, 식이섬유, 고추 성분 등이 각각 항암효과를 보일 것이라는 해석도 있다.", "There is also an interpretation that the garlic, dietary fiber and red-pepper components in kimchi each show an anti-cancer effect."),
    ("물론 반갑고 즐거운 소식이다. 그러나 학자의 입장에서 보면 아직 부족한 부분이 있다.", "Of course it is welcome and pleasant news. But from a scholar’s point of view, there is still something lacking."),
    ("김치가 건강에 좋고 특히 암을 예방한다는 주장은 근거가 희박하기 때문이다.", "This is because the claim that kimchi is good for health and especially prevents cancer has thin grounds."),
    ("김치에 항산화작용을 하는 비타민이 많은 것은 사실이고 유산균도 있지만 암 발생을 억제할 수도 있다는 동물실험, 혹은 실험실적 연구결과만이 있을 뿐이지 정말 인간에게서 암을 예방한다는 증거는 없기 때문이다.", "It is true that kimchi has many vitamins that act as antioxidants and it has lactic acid bacteria too, but there are only animal experiments or laboratory research results saying it might suppress cancer; there is no evidence that it really prevents cancer in humans."),
    ("한국인이 유독 많이 먹고 있기 때문에 오히려 반대로 김치는 암, 특히 위암을 일으킬 수 있다는 주장도 있다. 김치에는 항산화물질뿐만 아니라 염분도 많기 때문이다.", "Because Koreans eat it in particularly large amounts, there is even an opposite claim that kimchi can cause cancer, especially stomach cancer. That is because kimchi has a lot of salt as well as antioxidants."),
    ("김치에서 짠 성분만 줄이는 노력을 계속한다면, 김치는 충분히 전 세계인이 더욱 좋아할 수 있는 건강식품이 될 것이라고 확신한다.", "I am sure that if efforts to reduce only the salty component continue, kimchi can well become a health food that people all over the world like even more."),
]
_SPEAK6B = [("미국에서는 어떤 암이 가장 많이 발병하고 있는지 알아보고 친구들과 이야기해 보세요.", "Find out which cancer occurs most in the United States and talk with your friends."), ("암에 걸리지 않기 위해서 어떤 예방책이 필요한지 친구들과 이야기해 보세요.", "Talk with your friends about what preventive measures are needed so as not to get cancer.")]
_PREV6 = [("항산화 식품이나 발효 식품을 먹는다.", "Eat antioxidant foods or fermented foods. (given in the book)"), ("좋은 식습관을 가진다.", "Have good eating habits. (given in the book)"), ("담배를 피우지 않는다.", "Do not smoke. (given in the book)"), ("적정 체중을 유지한다.", "Maintain a proper weight. (given in the book)")]
L4 = lesson(
    "U17 L6 · Part 2 (본 학습): kimchi and cancer, and prevention measures",
    "본 학습 · 김치 · 항암 · 유산균 · 염분 · 위암 · 암 예방 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: does kimchi cause cancer? Is it good for prevention? (a Kyunghyang article)", "The article, with my English (the book writes the vitamins as A, B, C in capitals, written here in Korean). Answers: 1. The main topic: D, there is controversy over whether kimchi is a cancer-fighting food. 2. Reasons kimchi might help prevent cancer: it is rich in fiber and low in fat; it has vitamins A, B and C and lactic acid bacteria, which block the proliferation of cancer cells; and its garlic, dietary fiber and red-pepper components might each have an anti-cancer effect. 3. The ingredient to reduce is salt (염분, the salty component).", examples=passage(_KIM6)),
        card("학습활동 3: seven cancer-prevention measures (the four the book gives)", "In the interview (audio) seven measures are described; the book prints four of them in English and asks you to write the other three. The four given, put into Korean by me:", examples=passage(_PREV6)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK6B)),
        card("Activities left out", "학습활동 2 (Listening, track 009): a KBS news item about cancer with two patient cases; you summarize the two cases, say what “10 years” refers to, and choose the tone of the clip (pessimistic, passionate, optimistic or sympathetic). 학습활동 3 (Listening, tracks 010 and 011): a YTN interview on cancer countermeasures and prescriptions, with a table of the four major cancers and the cancer causes, the three additional cancers affecting men and women, and the other three of the seven preventive measures, plus a task of translating three measures into Korean. They are audio."),
    ],
    exercises=uniq(
        _tr(_KIM6[1:], k=3) + _tr(_PREV6, k=3)
        + [M("What is the main topic of the kimchi article?", "Whether kimchi fights cancer is controversial", ["Kimchi is the best food for cancer prevention", "Kimchi is a popular diet food only", "Kimchi is not healthy at all"], "D."), M("Which ingredient should be reduced to make kimchi healthier?", "Salt", ["Garlic", "Red pepper", "Vitamins"], "염분."), M("Why is the claim that kimchi prevents cancer weak?", "There is only animal and laboratory evidence, not evidence in humans", ["It is too new", "Nobody eats kimchi", "Kimchi has no vitamins"], "근거가 희박."), M("Which foods were chosen as the world’s five health foods with kimchi?", "Soybeans, lentils, olive oil and yogurt", ["Rice and tea", "Beef and pork", "Bread and cheese"], "세계 오대 건강식품.")]
        + [F("김치는 ___이 풍부한 저지방 다이어트 음식이다. (fiber)", "섬유질", ["염분", "근거"], "섬유질."), F("김치에는 ___도 많아서 위암을 일으킬 수 있다는 주장도 있다. (salt)", "염분", ["유산균", "효소"], "염분."), F("김치가 암을 예방한다는 주장은 근거가 ___하다. (thin)", "희박", ["억제", "실험"], "희박하다.")]
        + [read_q("김치는 섬유질이 풍부한 저지방 다이어트 음식입니다"), read_q("김치에는 염분도 많습니다"), read_q("담배를 피우지 않는 것이 좋습니다"), read_q("암에 걸리지 않기 위해서 어떤 예방책이 필요합니까")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("근거(하다)", "(根據) grounds; basis (to be based on)", "그런 근거도 없는 소문은 믿지 마세요."),
        ("섬유질", "(纖維質) fiber", "채소는 다량의 섬유질을 함유하고 있다."),
        ("성분", "(成分) ingredient; component", "제품의 성분을 검사하고 있습니다."),
        ("실험(하다)", "(實驗) experiment; test (to conduct an experiment; to test)", "저는 동물실험을 하지 않은 샴푸만 사용합니다."),
        ("억제(하다/되다)", "(抑制) suppress; control (to suppress; to control; to restrain/to be suppressed; to be controlled; to be restrained)", "불필요한 지출을 억제하고 있습니다."),
        ("염분", "(鹽分) salt; salinity", "염분이 많이 들어간 음식은 건강에 안 좋습니다.", "소금"),
        ("유산균", "(乳酸菌) lactobacillus; lactic acid bacteria", ""),
        ("항산화", "(抗酸化) the process of inhibiting oxidation", "산화란 물질이 산소와 결합하는 과정을 말한다."),
        ("희박하다", "(稀薄) to be rare; to be remote; to be thin", "이 일은 성공할 가능성이 아주 희박합니다.", "드물다"),
    ]),
    ("학습활동 2", [
        ("거뜬히", "easily; without difficulty", "이 정도 일은 저 혼자도 거뜬히 할 수 있어요.", "거뜬하다"),
        ("마감(하다/되다)", "closing; ending (to close; to end; to finish/to be closed; to be finished)", "원서 접수 마감은 이번 주말까지입니다."),
        ("마무리(하다)", "finishing; wrapping up (to finish; to wrap up)", "숙제를 오늘 오후까지 마무리해야 합니다.", "마치다, 끝내다"),
        ("생존(하다)", "(生存) survival (to survive)", "요즘은 암에 걸려도 생존 확률이 높습니다."),
        ("의지(하다)", "(依支) dependence (to depend on; to rely on; to lean on/against)", "그는 지팡이에 의지하여 걸었다."),
        ("진단(하다/받다)", "(診斷) diagnosis (to diagnose/to be diagnosed)", "아버지는 암 진단을 받으시고 수술을 결심하셨습니다."),
    ]),
    ("학습활동 3", [
        ("난치병", "(難治病) an intractable disease; a rare disease; “disease (that is) hard to cure”", "신약이 개발되면서 난치병 치료의 길이 열렸습니다.", "불치병"),
        ("대장암", "(大腸癌) colon cancer; “big intestine cancer”", ""),
        ("불치병", "(不治病) an incurable disease", "그 아이는 어린 나이에 불치병에 걸려 고생하고 있습니다.", "난치병"),
        ("예산", "(豫算) budget", "이번 달은 예산을 초과해서 절약을 해야 할 것 같습니다."),
        ("완치(율)", "(完治率) full recovery; complete recovery (rate of complete recovery/cure)", "위암은 완치율이 높은 것으로 알려져 있습니다."),
        ("유방암", "(乳房癌) breast cancer", ""),
    ]),
]
L5 = lesson(
    "U17 L6 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 근거 · 섬유질 · 실험 · 억제 · 유산균 · 항산화 · 희박하다 · 거뜬히 · 마감 · 생존 · 의지 · 진단 · 난치병 · 대장암 · 불치병 · 완치 · 유방암",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 유산균, 대장암 and 유방암. 난치병 and 불치병 list each other as related words. 거뜬히’s related word is 거뜬하다.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=12, nread=10)),
)

# ================================================================== L6 Part 3
_PAT6 = [
    ("오 년 뒤 폐암이 완치되면 딸과 함께 전국 오지를 다닐 거예요. 나는 아코디언 연주하고 딸은 어르신들 이발해 드리고.", "“In five years, once my lung cancer is cured, I’ll travel the remote areas around the country with my daughter. I’ll play the accordion and my daughter will cut the elders’ hair.”"),
    ("한 폐암 환자는 가늘고 쉰 목소리로 힘주어 말했다. 지난 오 월 폐암 진단을 받고 항암 치료 중인 그는 넉 달 만에 몸무게가 십육 킬로그램이 줄어 이제 사십구 킬로그램밖에 안 된다.", "A lung cancer patient said emphatically in a thin, hoarse voice. Diagnosed with lung cancer last May and undergoing anti-cancer treatment, he lost 16 kg in four months and now weighs only 49 kg."),
    ("하지만 그는 오 년 전에 딸과 한 약속을 꼭 지키고 싶다고 했다. 승합차를 마련해 딸과 함께 전국 산골을 다니며 노인들에게 음악과 미용 봉사를 하자는 것이었다.", "But he said he very much wants to keep the promise he made with his daughter five years ago: to get a van and travel the mountain villages across the country with her, doing music and beauty volunteer work for the elderly."),
    ("그래서 한날한시에 아버지는 색소폰 학원에, 딸은 미용학원에 등록했다. 지난 십 일 한 주민센터에서 만난 그는 할 수 있다는 말을 거듭했다.", "So on the same day and hour, the father enrolled in a saxophone school and the daughter in a beauty school. Meeting him at a community center on the 10th, he repeated the words “I can do it”."),
    ("십이 년 전부터 형편이 어려운 학생들에게 해마다 이백만 원에서 삼백만 원씩 교복값을 건네고, 오 년째 노인요양병원에 다니며 케이크와 과일 등을 선물하고 멋진 색소폰 연주도 들려 주고 있다.", "Since twelve years ago, he has handed two to three million won every year to students in difficult circumstances for school uniforms, and for five years he has visited nursing hospitals for the elderly, giving cakes and fruit and playing the saxophone for them."),
    ("우리 아이들한테 봉사를 가르쳐 주고 싶었어요. 하지만 그는 이제 색소폰을 손에서 놓아야 한다.", "“I wanted to teach my children volunteering.” But now he has to put the saxophone down."),
    ("폐암 발병으로 숨이 가빠져 더는 연주가 어렵다. 서너 곡만 부르면 숨이 막힌다. 그래서 대신 아코디언을 들었다.", "With the onset of lung cancer he has become short of breath and can no longer play. After only three or four pieces he cannot breathe. So he took up the accordion instead."),
    ("돈은 일시적인 거예요. 만남이 중요합니다. 서로 만남이 이뤄져야 관계가 평생 이어지는 거죠.", "“Money is temporary. Meeting people is what matters. Only when people meet does a relationship last a lifetime.”"),
    ("그는 한가위를 앞두고 지난주 이웃 돕기 성금으로 오백만 원을 선뜻 기탁했다. 어려운 이웃들을 생각하는 마음은 폐암 투병의 어려움 속에서 오히려 더 커졌다.", "Ahead of Chuseok, last week he readily donated five million won as a fund to help neighbors. His heart for neighbors in need grew even bigger amid the hardship of his fight against lung cancer."),
    ("아내와 삼 남매를 앉혀 놓고 물어봤죠. 오백만 원을 내놓고 싶다고 했어요. 반대할 줄 알았는데, 모두들 흔쾌히 찬성하더라고요. 감동받았죠.", "“I sat my wife and three children down and asked them. I said I wanted to give five million won. I thought they would object, but everyone agreed gladly. I was moved.”"),
    ("그는 금세 눈시울이 뜨거워지며 말을 잇지 못했다.", "His eyes quickly grew hot with tears and he could not go on."),
]
_DEM6 = [
    ("네 가지 조건만 갖추면 치매도 피할 수 있다.", "Dementia too can be avoided if only four conditions are met."),
    ("육 일 에이에프피통신 등에 따르면 프랑스 국립의학연구소의 카렌 리트시 박사는 당뇨병과 우울증을 피하고 교육수준을 높이고 과일과 채소를 많이 섭취하면 치매를 사십 퍼센트까지 막을 수 있다고 밝혔다.", "According to AFP and others on the 6th, Dr. Karen Ritchie of the French National Institute of Medical Research said that avoiding diabetes and depression, raising the level of education and eating plenty of fruit and vegetables can prevent dementia by up to 40 percent."),
    ("리트시 박사는 프랑스 남부에 거주하는 육십오 세 이상의 건강한 노인 천사백삼십삼 명을 대상으로 조사 시작 때와 이 년, 사 년, 칠 년 후 모두 네 차례에 걸쳐 의료기록 및 교육수준, 식사습관, 소득, 음주, 흡연 등에 관한 개인자료를 조사하면서 치매와의 연관성을 분석한 결과 이 같은 결과를 얻었다고 말했다.", "Dr. Ritchie said she got this result by analyzing the link with dementia while surveying, on four occasions in all (at the start and after two, four and seven years), personal data on medical records, education level, eating habits, income, drinking and smoking from 1,433 healthy people aged 65 or over living in southern France."),
    ("이에 따라 당뇨병과 우울증을 피하고 과일과 채소를 많이 먹으면 치매위험이 평균 이십일 퍼센트 낮아지고, 교육수준이 높으면 이 한 가지 조건만으로도 치매위험이 십팔 퍼센트 줄어든다는 것.", "Accordingly, avoiding diabetes and depression and eating plenty of fruit and vegetables lower the risk of dementia by 21 percent on average, and a high level of education reduces the risk by 18 percent with this one condition alone."),
    ("한편 지금까지 알려진 치매관련 유전적 요인을 갖지 않는 것은 치매위험을 칠 퍼센트 정도 낮추는 효과밖에는 없는 것으로 나타났다.", "Meanwhile, not having the genetic factors related to dementia known so far turned out to have an effect of lowering the risk by only about 7 percent."),
    ("따라서 치매예방은 당뇨병 초기 단계에 나타나는 포도당 내성과 인슐린 저항을 철저히 검사해야 하는 것은 물론 우울증세가 있으면 즉각 치료하고 교육을 많이 받도록 하는 것에 초점을 맞춰야 한다고 리트시 박사는 지적했다.", "Dr. Ritchie pointed out that dementia prevention should focus not only on thoroughly testing for glucose tolerance and insulin resistance that appear in the early stage of diabetes, but also on treating depression at once if it is present and getting people to receive much education."),
]
_SPEAK6C = [("자신이나 주위 사람들이 경험한 건망증의 예에 대해서 이야기해 보세요.", "Talk about examples of forgetfulness experienced by you or people around you."), ("주위의 노인들이 치매를 예방하기 위해 어떤 것을 하고 있는지 아는 것이 있으면 이야기해 보세요.", "If you know what elderly people around you are doing to prevent dementia, talk about it.")]
L6 = lesson(
    "U17 L6 · Part 3 (심화 학습): a lung cancer patient’s promise and a dementia study",
    "심화 학습 · 폐암 · 봉사 · 기탁 · 치매 · 당뇨병 · 우울증 · 교육수준 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: “When I am cured, I’ll go on remote-area volunteering with my daughter” (Hankyoreh)", "The article, with my English. The book names the patient and his daughter, gives their ages and says where they met; because he is a private person with an illness, I dropped the names, ages and place and wrote “a lung cancer patient” (한 폐암 환자) and “the father”. The book writes the figures in digits (written out here). Answers: 1. In five years, once his lung cancer is cured, he plans to travel remote areas across the country with his daughter, doing music (accordion) and beauty (haircutting) volunteer work for the elderly. 2. He wants to teach his children to volunteer, and he believes that meeting people is what matters, not money. 3. Because lung cancer has left him short of breath, so after three or four pieces he cannot breathe.", examples=passage(_PAT6)),
        card("학습활동 2: four conditions that can prevent dementia (Kyunghyang)", "The article on Dr. Karen Ritchie’s study (a published researcher, name as in the book), with my English (the book writes her name in English in brackets and the figures in digits). Answer to the table: Conditions that prevent dementia: avoiding diabetes; avoiding depression; a high level of education; eating plenty of fruit and vegetables (not having the known genetic factors lowers the risk by only about 7 percent). Elements researched: medical records, education level, eating habits, income, drinking and smoking.", examples=passage(_DEM6)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompts (the English is mine):", examples=passage(_SPEAK6C)),
        card("Activities left out", "학습활동 3 (Listening, tracks 012 and 013): a YTN interview on dementia in two parts. In the first you list in English the symptoms of dementia described and the differences between dementia and forgetfulness; in the second you write what you think 젊은 치매 (“young dementia”) means and fill a table of its causes, symptoms and methods of prevention. It is video."),
    ],
    exercises=uniq(
        _tr(_PAT6[1:], k=3) + _tr(_DEM6[1:], k=3)
        + [M("What does the patient plan to do once he is cured?", "Travel remote areas with his daughter doing volunteer work", ["Retire abroad", "Open a school", "Play in a concert hall"], "오지 봉사."), M("Why did the patient stop playing the saxophone?", "He gets short of breath because of lung cancer", ["He lost it", "He dislikes it", "It broke"], "숨이 가빠져."), M("What does the patient think is important?", "Meeting people", ["Money", "Fame", "A big house"], "만남."), M("How much did he donate?", "Five million won", ["One million won", "Fifty thousand won", "Thirty million won"], "오백만 원."), M("Which is NOT one of the conditions that prevent dementia, according to the study?", "Sleeping long hours", ["Avoiding diabetes", "A high level of education", "Eating plenty of fruit and vegetables"], "Study."), M("By how much did a high education level reduce the risk of dementia?", "18 percent", ["7 percent", "21 percent", "40 percent"], "십팔 퍼센트.")]
        + [F("폐암 발병으로 ___가 가빠져 연주가 어렵다. (breath)", "숨", ["목", "손"], "숨이 가쁘다."), F("그는 이웃 돕기 성금으로 오백만 원을 ___ 기탁했다. (readily)", "선뜻", ["금세", "거듭"], "선뜻."), F("우울증이 있으면 ___ 치료해야 한다. (at once)", "즉각", ["겨우", "고작"], "즉각.")]
        + [read_q("폐암이 완치되면 딸과 함께 전국 오지를 다닐 겁니다"), read_q("우리 아이들한테 봉사를 가르쳐 주고 싶었습니다"), read_q("당뇨병과 우울증을 피하면 치매를 막을 수 있습니다"), read_q("자신이나 주위 사람들이 경험한 건망증의 예에 대해서 이야기해 보세요")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("기탁(하다)", "(寄託) donation (to donate)", "저는 장학금으로 백만 원을 기탁할까 합니다.", "기부하다"),
        ("눈시울이 뜨겁다", "to be (emotionally) moved to tears; “the edge of the eyelids is hot”", "아프리카 어린이들의 다큐멘터리를 보고 눈시울이 뜨거워졌다."),
        ("발병(하다)", "(發病) outbreak of a disease (to break out)", "발병 원인이 무엇이라고 보십니까?"),
        ("오지", "(奧地) backwoods; the outback; a remote area", "김 대리는 오지 근무를 자원했습니다."),
        ("요양(하다)", "(療養) recuperation; convalescence (to recuperate)", "이 곳은 공기가 좋아서 요양하러 오는 사람들이 많아요.", "요양지, 요양소"),
        ("형편", "(形便) circumstances; conditions", "집안 형편이 좋지 않아 대학에 진학하지 못했어요.", "사정, 상황"),
        ("흔쾌히", "(欣快) pleasantly; delightfully", "결혼식 초대를 흔쾌히 받아들였다."),
    ]),
    ("학습활동 2", [
        ("내성", "(耐性) tolerance (to a drug)", "같은 약을 계속 쓰면 환자에게 내성이 생긴다."),
        ("연관성", "(聯關性) relation; connection; association", "이 공장과 주민들의 집단 발병 간의 연관성을 찾을 수 없습니다.", "관련성"),
        ("저항(하다)", "(抵抗) resistance (to resist)", "새로 발표된 정책은 국민들의 거센 저항에 부딪쳤습니다."),
        ("초점", "(焦點) a focus; a focal point", "카메라의 초점을 아이들에게 맞췄다."),
        ("포도당", "(葡萄糖) grape sugar; glucose; dextrose", "포도당은 피로회복에 도움이 된다."),
    ]),
    ("학습활동 3", [
        ("건망증", "(健忘症) forgetfulness; absentmindedness", "요즘 아버지의 건망증이 심해져서 걱정입니다."),
        ("과격하다", "(過激) to be violent; to be aggressive", "수술후 과격한 운동은 삼가세요."),
        ("까먹다", "(slang) to forget; to eat up (money); “to peel and eat”", "약속을 까먹어서 회의에 참석하지 못했습니다.", "깜박하다"),
        ("뇌졸중", "(腦卒中) stroke; apoplexy", "", "중풍"),
        ("망가지다", "to be out of order; to break down; to be ruined", "컴퓨터를 새로 산 지 얼마 안 됐는데 금방 망가졌어요.", "고장나다"),
        ("세밀하다", "(細密) to be detailed", "그 실험은 세밀한 관찰이 필요하다."),
        ("소심하다", "(小心) to be timid; “small mind”", "그 남자는 소심해서 여자에게 데이트 신청도 못 한다."),
        ("치매", "(癡簞) dementia; Alzheimer’s disease", ""),
        ("판단(하다/되다)", "(判斷) judgment; decision (to judge/to be judged)", "저는 상황 판단을 잘 못 하겠어요.", "결정하다"),
    ]),
]
L7 = lesson(
    "U17 L6 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 기탁 · 눈시울이 뜨겁다 · 발병 · 오지 · 요양 · 형편 · 흔쾌히 · 내성 · 연관성 · 저항 · 초점 · 포도당 · 건망증 · 과격하다 · 까먹다 · 뇌졸중 · 망가지다 · 세밀하다 · 소심하다 · 치매 · 판단",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 뇌졸중 (related word 중풍) and 치매. The book prints the Hanja of 치매 as 癡簞; the usual Sino-Korean for the word is 癡呆, and I keep the book’s form. In the example for 기탁 the book has 100만 원 (written 백만 원 here).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=12, nread=10)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 6: Modern Diseases II (현대병 II)", [L1, L2, L3, L4, L5, L6, L7])
