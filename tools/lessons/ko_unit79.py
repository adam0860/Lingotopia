"""Unit 79: KBC Semester III, Unit 17, Lesson 4 - Health and Common Ailments (건강과 질병).
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
_DEPT4 = [("소화도 잘 안 되고 배도 자주 아픕니다. 건강검진을 받아 봐야 할 것 같아요.", "내과", "internal medicine (the book’s example)"), ("어제 수영장에 다녀온 후로 눈이 아픕니다.", "안과", "ophthalmology"), ("구역질이 자꾸 납니다. 임신한 것 같아요.", "산부인과", "obstetrics and gynecology"), ("이가 많이 아픕니다.", "치과", "dentistry"), ("온 몸에 뭐가 나서 가렵습니다.", "피부과", "dermatology"), ("세 살짜리 우리 아이가 열이 나고 아픕니다.", "소아과", "pediatrics"), ("배가 아파서 병원에 갔는데 수술을 받아야 한다고 합니다.", "외과", "surgery"), ("귀가 많이 아픕니다.", "이비인후과", "ear, nose and throat"), ("이번 겨울에 쌍꺼풀 수술을 받기로 했어요.", "성형외과", "plastic surgery")]
_VERBS4 = [("감기에", "걸리다", "to catch a cold"), ("엑스레이를", "찍다", "to take an X-ray"), ("붕대를", "감다", "to wrap a bandage"), ("연고를", "바르다", "to apply ointment"), ("배탈이", "나다", "to have an upset stomach")]
_HJ4 = [("痛 통", "ache; pain", "두통, 치통"), ("症 증", "symptom", "통증, 증상"), ("血 혈", "blood", "혈액, 헌혈"), ("壓 압", "pressure; pressing", "혈압, 압력"), ("藥 약", "medicine", "약사, 약국")]
_HJW4 = [("두통", "a headache"), ("치통", "a toothache"), ("통증", "a pain"), ("증상", "a symptom"), ("혈액", "blood"), ("헌혈", "blood donation"), ("혈압", "blood pressure"), ("압력", "pressure"), ("약사", "a pharmacist"), ("약국", "a pharmacy")]
_ODD4 = [("진통, 치통, 통증, 복통, 교통", "교통", "traffic (the 통 here is a different syllable)"), ("증상, 증후군, 우울증, 염증, 증가", "증가", "an increase (a different 증)"), ("혈압, 고기압, 압축, 압수, 압력", "압수", "seizure (a different 압)"), ("약국, 약사, 약방, 예약, 농약", "예약", "a reservation (a different 약)")]
_REL4 = [("A", "약", "해열제, 소화제, 진통제", "medicine"), ("B", "통증", "치통, 복통, 두통", "pain"), ("C", "압력", "혈압, 기압, 압축", "pressure")]
_L4X = [("진통", "labor pains; pain relief"), ("복통", "a stomachache"), ("교통", "traffic"), ("증후군", "a syndrome"), ("우울증", "depression"), ("염증", "inflammation"), ("증가", "an increase"), ("고기압", "high atmospheric pressure"), ("압축", "compression"), ("압수", "seizure"), ("약방", "a medicine shop"), ("예약", "a reservation"), ("농약", "agricultural chemicals"), ("해열제", "a fever reducer"), ("소화제", "a digestive medicine"), ("진통제", "a painkiller"), ("저혈압", "low blood pressure"), ("기압", "air pressure"), ("내과", "internal medicine"), ("안과", "ophthalmology"), ("산부인과", "obstetrics and gynecology"), ("소아과", "pediatrics"), ("외과", "surgery"), ("이비인후과", "ear, nose and throat clinic"), ("피부과", "dermatology"), ("치과", "dentistry"), ("성형외과", "plastic surgery"), ("붕대", "a bandage"), ("연고", "ointment"), ("엑스레이", "an X-ray"), ("배탈", "an upset stomach"), ("감기", "a cold"), ("구역질", "nausea"), ("건강검진", "a health checkup"), ("쌍꺼풀 수술", "double-eyelid surgery"), ("임신", "pregnancy")]
L1 = lesson(
    "U17 L4 · Review: clinics, ailments and Sino-Korean 痛 症 血 壓 藥",
    "건강과 질병 · 단어 복습 · 한자어 복습 · 내과 · 안과 · 산부인과 · 소아과 · 외과 · 이비인후과 · 피부과 · 치과 · 성형외과 · 痛 症 血 壓 藥",
    requires=[],
    cards=[
        card("단어 복습 1: which hospital department (my answers)", "Write the department from the box (안과, 내과, 산부인과, 소아과, 외과, 이비인후과, 피부과, 치과, 성형외과) that fits each sentence; the first (내과) is the book’s example. The book writes 3살짜리 in figures (세 살짜리 here).", tables=[table(["Sentence", "Department (my answer)", "Meaning"], [list(r) for r in _DEPT4], say=[0, 1])]),
        card("단어 복습 2: nouns with their verbs (my answers)", "Connect each noun with the verb often used with it (찍다, 나다, 바르다, 감다, 걸리다) and write the right marker in the brackets; the first (감기에 걸리다) is the book’s example:", tables=[table(["Noun with marker (my answer)", "Verb", "Meaning"], [list(r) for r in _VERBS4], say=[0, 1])]),
        card("한자어 복습: Sino-Korean syllables", "The book reviews five Sino-Korean syllables you learned in earlier semesters, each with two example words:", tables=[table(["Syllable", "Meaning", "Examples"], [list(r) for r in _HJ4], say=[2]), ktable(_HJW4)]),
        card("한자어 복습 1: the odd syllable out (my answers)", "In each row circle the word whose underlined syllable has a different meaning from the one in the word on the left (the underline is not marked in the text; the words are A. 진통 and so on, B. 증상, C. 혈압, D. 약국). My answers:", tables=[table(["The row", "Odd one out (my answer)", "Why"], [list(r) for r in _ODD4], say=[0, 1])]),
        card("한자어 복습 2: the word that holds all three (my answers)", "Choose from the box (증후군, 저혈압, 약, 통증, 압력, 우울증) the word that can include all three words; 증후군, 저혈압 and 우울증 are left over. My answers:", tables=[table(["", "Word from the box (my answer)", "The three words", "Meaning"], [list(r) for r in _REL4], say=[1, 2])]),
        card("More words from these exercises", "", tables=[ktable(_L4X)]),
    ],
    exercises=uniq(
        _tr([(a, c) for a, b, c in _DEPT4[:0]] + [(b, c) for a, b, c in _DEPT4], k=4) + _tr(_HJW4, k=3) + _tr(_L4X, k=3) + _tr([(a + " " + b, c) for a, b, c in _VERBS4], k=3)
        + [M("What does the syllable 痛 (통) mean?", "ache; pain", ["symptom", "blood", "medicine"], "통증."), M("What does the syllable 症 (증) mean?", "symptom", ["ache", "blood", "medicine"], "증상."), M("What does the syllable 血 (혈) mean?", "blood", ["ache", "symptom", "medicine"], "혈액."), M("What does the syllable 壓 (압) mean?", "pressure; pressing", ["ache", "symptom", "blood"], "압력."), M("What does the syllable 藥 (약) mean?", "medicine", ["ache", "symptom", "blood"], "약국.")
           , M("Which department do you go to for eye pain?", "안과", ["치과", "피부과", "소아과"], "Eyes."), M("Which department do you go to for a toothache?", "치과", ["안과", "외과", "내과"], "Teeth."), M("Which department do you go to for itchy skin?", "피부과", ["안과", "치과", "외과"], "Skin."), M("Which department do you go to for a child’s fever?", "소아과", ["산부인과", "치과", "안과"], "Children."), M("Which department do you go to for ear pain?", "이비인후과", ["안과", "치과", "피부과"], "Ear, nose and throat."), M("Which department do you go to for double-eyelid surgery?", "성형외과", ["내과", "소아과", "치과"], "Plastic surgery."),
           M("Which word holds 해열제, 소화제, 진통제?", "약", ["통증", "압력", "증후군"], "Medicine."), M("Which word holds 치통, 복통, 두통?", "통증", ["약", "압력", "저혈압"], "Pain."), M("Which word holds 혈압, 기압, 압축?", "압력", ["약", "통증", "우울증"], "Pressure.")
           , F("감기에 ___. (to catch)", "걸립니다", ["찍습니다", "바릅니다"], "걸리다."), F("엑스레이를 ___. (to take)", "찍습니다", ["걸립니다", "감습니다"], "찍다."), F("붕대를 ___. (to wrap)", "감습니다", ["바릅니다", "찍습니다"], "감다."), F("연고를 ___. (to apply)", "바릅니다", ["감습니다", "나옵니다"], "바르다."), F("배탈이 ___. (to have)", "났습니다", ["걸렸습니다", "찍었습니다"], "나다.")]
        + [read_q("이가 많이 아픕니다"), read_q("구역질이 자꾸 납니다"), read_q("연고를 바릅니다"), read_q("세 살짜리 우리 아이가 열이 나고 아픕니다")]
    ),
)

# ================================================================== L2 Part 1
_HEAT4 = [
    ("일사병은 열에 의한 스트레스로 염분과 수분이 소실돼 생기는 질환이다.", "Heatstroke is a disease caused by the loss of salt and water through stress from heat."),
    ("노인에게서 흔한데, 증상은 땀을 많이 흘리고 창백하며, 두통과 구토, 어지럼증 등을 호소한다.", "It is common in the elderly; the symptoms are heavy sweating and paleness, and complaints of headache, vomiting, dizziness and so on."),
    ("피부가 차고 젖어 있으며 체온은 크게 상승하지 않는다.", "The skin is cold and wet, and body temperature does not rise much."),
    ("만약 일사병이 의심되면 서늘한 곳에 쉬도록 하면서 시원한 음료, 염분이 포함된 음료, 를 마시도록 하는 게 좋다.", "If heatstroke is suspected, it is good to have the person rest in a cool place and drink a cool beverage (one that contains salt)."),
    ("하지만 알코올이 포함된 음료는 피해야 한다.", "But beverages that contain alcohol should be avoided."),
    ("차가운 물로 샤워를 하거나 목욕을 하는 것도 좋고, 심한 증상에는 병원에서 수분과 염분을 보충하면 도움이 된다.", "Taking a shower or a bath in cold water is also good, and for severe symptoms, replenishing water and salt at a hospital helps."),
]
_SPEAK4A = [("더운 여름철에 건강하게 생활하려면 어떻게 해야 할까요? 옆 사람과 이야기해 봅시다.", "What should you do to live healthily in the hot summer? Let’s talk with the person next to you.")]
L2 = lesson(
    "U17 L4 · Part 1 (도입 학습): heatstroke and a speaking prompt",
    "도입 학습 · 일사병 · 염분 · 수분 · 창백하다 · 구토 · 두통 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 3: an article on heatstroke (일사병) (Yonhap News)", "The article, with my English (the book’s English table is completed from it). Answers: Cause of the ailment: loss of salt and water through stress from heat. Symptoms: heavy sweating, paleness, headache, vomiting, dizziness; the skin is cold and wet and body temperature does not rise much. Recommended treatment: rest in a cool place and drink a cool beverage that contains salt, avoid alcohol, take a cold shower or bath, and for severe symptoms have water and salt replenished at a hospital.", examples=passage(_HEAT4)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK4A)),
        card("Activities left out", "학습활동 1 (Reading, Kobaco public-service posters): two posters (pictures) for which you choose from four or three English choices what the advertisement is about. The choices for the first are: helping children form the habit of washing hands before meals; hand washing and disease prevention; washing hands after playing outside; washing hands before getting a shot. The choices for the second are: the increased number of smokers; difficulty quitting smoking; secondhand smoke. The posters are pictures, so I cannot tell which choices are right. 학습활동 2 (Listening, track 001): a part of a drama (MBC America); you fill in a table of the patient, the doctor’s diagnosis and the doctor’s recommendations in English. 학습활동 4 (Listening, track 002): information from YTN on rules for the rainy season, with a table of health advice."),
    ],
    exercises=uniq(
        _tr(_HEAT4, k=3)
        + [M("What causes heatstroke?", "Loss of salt and water through stress from heat", ["Eating too much", "Cold weather", "Lack of sleep"], "열에 의한 스트레스."), M("Who is heatstroke common in?", "The elderly", ["Babies only", "Athletes only", "Teachers only"], "노인."), M("Which symptom is NOT described?", "A high fever", ["Heavy sweating", "Paleness", "Headache and vomiting"], "체온은 크게 상승하지 않는다."), M("What should you avoid drinking if heatstroke is suspected?", "Beverages that contain alcohol", ["Cool drinks", "Drinks with salt", "Water"], "알코올."), M("Where should a person with suspected heatstroke rest?", "In a cool place", ["In the sun", "In a hot room", "In a car"], "서늘한 곳.")]
        + [F("일사병의 증상은 땀을 많이 흘리고 ___하다. (pale)", "창백", ["서늘", "한가"], "창백하다."), F("심한 증상에는 병원에서 수분과 염분을 ___하면 도움이 된다. (replenish)", "보충", ["호소", "구토"], "보충하다."), F("일사병이 의심되면 ___ 곳에 쉬도록 한다. (cool)", "서늘한", ["창백한", "번거로운"], "서늘하다.")]
        + [read_q("일사병은 열에 의한 스트레스로 생기는 질환입니다"), read_q("서늘한 곳에 쉬도록 하세요"), read_q("알코올이 포함된 음료는 피해야 합니다"), read_q("더운 여름철에 건강하게 생활하려면 어떻게 해야 할까요")]
    ),
)

# ================================================================== L3 Part 1 vocabulary
_V1 = [
    ("학습활동 3", [
        ("구토(하다)", "(嘔吐) vomiting (to vomit)", "구토가 심해지면 이 약을 드세요.", "토하다"),
        ("보충(하다/되다)", "(補充) supplement; replenishment (to replenish; to make up for/to be replenished; to be supplemented)", "눈이 피로하면 비타민 씨를 보충하는 것이 좋아요."),
        ("서늘하다", "to be cool; to be chilly; to be chilled", "몬트레이는 아침 저녁으로 날씨가 서늘합니다."),
        ("수분", "(水分) moisture; water; “water part”", "수분이 많은 과일을 많이 드세요."),
        ("염분", "(鹽分) salt; salinity; “salt part”", "혈압이 높아요. 염분 섭취를 좀 줄이도록 하세요."),
        ("일사병", "(日射病) sunstroke; heatstroke", "노약자는 밖에 너무 오래 있으면 일사병에 걸릴 수 있으니까 조심하세요."),
        ("창백하다", "(蒼白) to be pale", "제 아내는 그 소식을 듣고 얼굴이 창백해졌습니다."),
        ("호소(하다)", "(呼訴) appeal for; plea (to appeal; to plead; to complain)", "환자가 복통을 호소하면 이 약을 먹이십시오."),
    ]),
    ("학습활동 4", [
        ("곰팡이", "mold; mildew", "장마철에는 곰팡이를 조심해야 합니다."),
        ("눅눅하다", "to be damp; to be humid; to be soggy", "비가 많이 와서 이불이 눅눅해졌어요."),
        ("번거롭다", "to be cumbersome; to be inconvenient", "명절에 고향에 내려가려고 했지만 너무 번거로워서 가지 않기로 했어요."),
        ("번식(하다)", "(繁殖) breeding; reproduction (to breed; to reproduce)", "습기가 있으면 세균이 더 빨리 번식합니다."),
        ("세균", "(細菌) germ; bacteria", "상처 부위가 세균에 감염되지 않게 주의하세요.", "균"),
        ("수칙", "(守則) rules; regulations; advice; “keeping rules”", "안전 수칙을 꼭 준수하시기 바랍니다.", "규정, 규칙"),
    ]),
]
L3 = lesson(
    "U17 L4 · Part 1: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 구토 · 보충 · 서늘하다 · 수분 · 염분 · 일사병 · 창백하다 · 호소 · 곰팡이 · 눅눅하다 · 번식 · 세균 · 수칙",
    requires=[],
    cards=[card("A note on the Korean in this list", "In the example for 보충 the book has Vitamin C (written 비타민 씨 here). The book gives 곰팡이 under 학습활동 4 without Hanja.")] + vocab_cards(_V1),
    exercises=uniq(vocab_exs(_V1, nf=10, nread=8)),
)

# ================================================================== L4 Part 2
_SPEAK4B = [("이제까지 병원에 입원했거나 많이 아팠던 경험이 있으면 친구와 이야기를 나눠 보세요.", "If you have ever been in hospital or been very sick, talk with a friend about the experience.")]
_VIB4 = [("비브리오 패혈증은 여름에 자주 발생하는 병입니다.", "Vibrio vulnificus sepsis is a disease that often occurs in summer. (The sentence is mine, from the book’s English footnote.)"), ("어패류는 껍질이 열린 뒤 오 분 동안 더 끓여야 합니다.", "Shellfish should be boiled for five minutes more after the shells open. (From the book’s English prevention list, put into Korean by me.)"), ("증기로 요리할 때는 구 분 더 익혀야 합니다.", "When steam cooking, cook nine minutes longer. (From the book’s English prevention list, put into Korean by me.)")]
L4 = lesson(
    "U17 L4 · Part 2 (본 학습): vibrio sepsis notes and a speaking prompt",
    "본 학습 · 비브리오 패혈증 · 어패류 · 증기 · 치과 · 소아청소년과 · 속설 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: vibrio vulnificus sepsis (the book’s English notes)", "This activity is a YTN news report (track 003) on vibrio vulnificus sepsis (비브리오 패혈증), for which you fill a table of the cause of the disease and the preventive measures in English. The book prints the first two measures: boil shellfish for 5 minutes after the shells open; cook 9 minutes longer when steam cooking. Its footnote reads: “Vibrio vulnificus sepsis is a fatal illness caused by the vibrio vulnificus bacteria. Infections often occur from eating raw or undercooked shellfish during the summer.” The rest of the answers are in the audio. My Korean versions of the book’s English notes:", examples=passage(_VIB4)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK4B)),
        card("Activities left out", "학습활동 2 (Reading): a health-page cartoon (four panels, a Hankyoreh picture) in which a dentist advises a patient; you choose what advice he gives: A. brush your teeth within 30 minutes after each meal; B. within 30 minutes after drinking carbonated drinks; C. approximately 30 minutes after drinking beer; D. approximately 30 minutes before going to bed. The cartoon is a picture, so I cannot tell which is right. 학습활동 3 (Listening, track 004): a YTN video interview with a professor of pediatrics and adolescent medicine; you say what comparison he makes between North and South Koreans and fill a table of the myths the male interviewer mentions and the professor’s corrections. It is video."),
    ],
    exercises=uniq(
        _tr(_VIB4, k=3)
        + [M("How long should shellfish be boiled after the shells open?", "5 minutes", ["1 minute", "9 minutes", "30 minutes"], "오 분."), M("How much longer should you cook when steam cooking?", "9 minutes", ["5 minutes", "1 minute", "30 minutes"], "구 분."), M("When do vibrio infections often occur?", "From eating raw or undercooked shellfish in summer", ["From drinking milk in winter", "From eating bread", "From swimming in winter"], "Summer shellfish."), M("What is 비브리오 패혈증?", "A fatal illness caused by vibrio vulnificus bacteria", ["A kind of skin spot", "A type of flu", "A kind of food"], "Fatal illness.")]
        + [read_q("이제까지 병원에 입원했거나 많이 아팠던 경험이 있습니까"), read_q("어패류는 날로 먹지 마세요")]
    ),
)

# ================================================================== L5 Part 2 vocabulary
_V2 = [
    ("학습활동 1", [
        ("간염", "(肝炎) hepatitis; “liver inflammation”", ""),
        ("껍질", "skin; bark; peel; rind; shell", "사과는 껍질을 벗기지 않고 먹는 것이 좋습니다."),
        ("날로", "raw; uncooked", "생선을 날로 먹을 때는 신선한 것인지 꼭 확인을 해야 합니다.", "날것으로"),
        ("보관(하다)", "(保管) storage; custody; storing (to store; to keep)", "인터넷에서 물건을 산 후에 영수증을 보관하는 것이 좋습니다."),
        ("어패류", "(魚貝類) seafood; fish and shellfish", ""),
        ("증기", "(蒸氣) steam", "이 엔진은 증기로 움직입니다."),
        ("피서지", "(避暑地) a summer resort; “heat-avoiding place”", "요즘 젊은이들 사이에 인기 있는 피서지가 어디입니까?", "피서, 피서 가다, 여름 휴가"),
    ]),
    ("학습활동 2", [
        ("너무하다", "to be harsh; to be extreme", "주말에도 일을 해야 하고, 이 회사는 정말 너무한 것 같아요.", "심하다"),
        ("바로", "immediately", "저는 항상 퇴근하자마자 바로 집에 갑니다.", "금방"),
        ("양치액", "(養齒液) a liquid used for gargling; “gargling liquid”", "양치액은 살균 효과가 있습니다.", "양치질, 양치하다"),
        ("탄산음료", "(炭酸飮料) a soft drink; a carbonated beverage", "탄산음료를 너무 마시지 마세요.", "음료수"),
    ]),
    ("학습활동 3", [
        ("대충", "approximately; roughly", "이 자료를 대충 한 번 읽어 보고 오세요.", "대강"),
        ("분비(하다/되다)", "(分泌) secretion (to secrete/to be secreted)", "당뇨병은 인슐린 분비에 문제가 생기는 병입니다."),
        ("성장판", "(成長板) a growth plate (areas of developing cartilage tissue near the ends of long bones)", "성장판이 닫히면 키가 더 자라지 않습니다."),
        ("속설", "(俗說) a myth; a popular belief", "그 속설은 사실로 판명되었어요.", "정설, 속담"),
        ("숙면", "(熟眠) deep sleep; sound sleep", "숙면을 취했더니 오늘은 몸이 아주 가뿐하네요.", "수면, 잠"),
        ("숨이 차다", "to be out of breath; “breath fills up”", "오랜만에 달리기를 했더니 숨이 찹니다."),
        ("역행(하다)", "(逆行) retrogression; reverse movement (to go against)", "정부가 발표한 여성정책은 시대에 역행하는 것입니다."),
        ("자극(하다)", "(刺戟) stimulation; provoking (to stimulate; to provoke)", "이 화장품은 피부를 자극하지 않아서 좋아요."),
        ("줄넘기(하다)", "rope jumping (to jump rope)", "줄넘기를 많이 하면 키가 많이 큽니다."),
        ("종족", "(種族) a race; a kind; a species", "그 나라에서는 종족간 갈등이 심합니다."),
        ("호르몬", "a hormone", "사춘기가 되면 호르몬 분비가 왕성해집니다."),
    ]),
]
L5 = lesson(
    "U17 L4 · Part 2: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 간염 · 껍질 · 날로 · 보관 · 어패류 · 증기 · 피서지 · 양치액 · 탄산음료 · 분비 · 성장판 · 속설 · 숙면 · 자극 · 줄넘기 · 호르몬",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 간염 and 어패류. The example for 너무하다 has “…” in the book, written as a comma here. Under 피서지 the book prints the related words after a stray form 피한지, which I leave out. The book lists 정설 and 속담 together under 속설 as related words. 간염 and 어패류 appear in the audio-based activity 1.")] + vocab_cards(_V2),
    exercises=uniq(vocab_exs(_V2, nf=12, nread=10)),
)

# ================================================================== L6 Part 3
_SKIN4 = [
    ("영화 페르시아의 왕자의 알라무트 공주, 영화 맨발의 꿈의 동티모르 유소년축구팀 감독 등 주인공들은 외모에 공통적인 특징이 있다.", "The leads, such as Princess Tamina of the film Prince of Persia and the coach of the East Timor youth football team in the film Barefoot Dream, have a common feature in their looks. (I added the word “film” before the titles, which the book sets in angle brackets.)"),
    ("얼굴 눈가 주위에 기미와 주근깨가 뚜렷이 보이는 것이다.", "Liver spots and freckles are clearly visible around the eyes on the face."),
    ("기미와 주근깨 등 피부의 색소침착은 햇볕에 많이 노출됐을 때 일어난다.", "Pigmentation of the skin, such as liver spots and freckles, occurs when it is exposed to much sunlight."),
    ("영화의 주인공들이 어릴 적 자외선에 노출되는 생활을 했다는 이야기다.", "It means the film’s leads lived lives exposed to ultraviolet rays when they were young."),
    ("알라무트의 공주가 사는 사막지대는 뜨거운 햇볕과 모래바람이 있는 환경이다.", "The desert zone where the princess of Alamut lives is an environment with hot sunshine and sandy winds."),
    ("축구팀 감독은 선수시절 뙤약볕 아래서 열심히 공을 찼을 것이다.", "The football coach must have kicked the ball hard under the scorching sun in his playing days."),
    ("알게 모르게 햇볕에 노출되는 시간이 많았지만 자외선 대책을 소홀히 한 탓에 한결같이 기미와 주근깨가 생긴 것으로 추론할 수 있다.", "We can infer that they were exposed to the sun for long hours, knowingly or not, and because they neglected UV measures, they all developed liver spots and freckles."),
    ("주근깨는 표피층 얕은 곳에 위치하고 있어, 레이저 치료 한 번이면 대개 좋아진다.", "Freckles are located in a shallow part of the epidermis, so one laser treatment usually makes them better."),
    ("그러나 기미는 치료법 적용이 주근깨보다 더 복잡하고 치료 효과면에서도 논란이 적지 않다.", "But for liver spots, applying a treatment is more complicated than for freckles, and there is no small controversy over the treatment’s effect as well."),
    ("피부과 전문의 신학철 원장은 사실 기미는 어떤 치료를 해도 재발할 수 있기 때문에 완벽한 치료를 장담할 수 없다며 따라서 치료보다 예방이 중요하다고 강조한다.", "The dermatologist Dr. Shin Hak-cheol, the clinic director, stresses that “in fact liver spots can come back whatever treatment is used, so a perfect cure cannot be guaranteed; therefore prevention is more important than treatment”."),
]
_COL4 = [
    ("십여 년 전인 이십 대 초반, 중반만 해도 내 몸은 그럭저럭 봐 줄 만했다.", "Even ten-odd years ago, in my early and mid twenties, my body was passable."),
    ("백육십이 센티미터에 오십삼 킬로그램. 마르지도 뚱뚱하지도 않은 보통 체격이었으니까.", "162 cm and 53 kg: an ordinary build, neither thin nor fat."),
    ("내 몸의 변화는 정확히 스물다섯 살 고개를 넘기면서 찾아왔다.", "The change in my body came exactly as I passed twenty-five."),
    ("언제부터인가 뛰는 것은 물론이고 걸을 때조차 숨이 찼다.", "From some point on I was out of breath not only when running but even when walking."),
    ("운동 외에, 선택의 여지가 남아 있지 않았다.", "Apart from exercise, there was no room for choice left."),
    ("매일 새벽 여섯 시 출근도장을 찍은 다음 한 시간 삼십 분씩 유산소 및 근력 운동을 병행하고 있다.", "Every day after punching in at six in the morning, I do aerobic and weight exercise together for an hour and thirty minutes."),
    ("운동, 정말 힘들다. 그러나 이 고통을 이겨내면 새로운 세상이 열린다.", "Exercise is really hard. But if you overcome this pain, a new world opens."),
    ("몸과 마음이 편해지니, 사는 게 즐겁다. 피로와 스트레스도 풀린다.", "As body and mind get comfortable, living is enjoyable. Fatigue and stress are relieved too."),
    ("모든 일을 긍정적으로 받아들이게 되니, 표정도 더 밝아졌다. 요즘은 젊어졌다는 소리도 듣는다. 남편과도 사이가 좋아졌다. 게다가 체중도 칠 킬로그램씩이나 줄었다.", "As I came to take everything positively, my expression brightened too. These days I even hear that I look younger. My relationship with my husband has improved. On top of that, I lost as much as seven kilograms."),
    ("하루 한 시간 남짓 운동의 효과치고 꽤나 크다. 몸이 건강해지고 있다는 건 더 큰 수확이다.", "It is quite big for the effect of a little over an hour of exercise a day. That my body is getting healthier is an even bigger harvest."),
    ("적정체중 유지와 규칙적인 운동은 생활습관병을 예방하고 건강을 지키는 지름길이다.", "Keeping an optimal weight and exercising regularly is the shortcut to preventing lifestyle diseases and protecting your health."),
    ("혹시 누군가는 바쁜 일상에서 무슨 운동이냐고, 젊을 때 더 벌고 더 높은 지위에 올라야 한다고 반문할지도 모르겠다.", "Perhaps someone may retort, “What exercise, in a busy daily life? When you are young you have to earn more and rise to a higher position.”"),
    ("건강해야 돈도 벌 수 있고, 명예도 좇을 수 있다. 건강을 잃었는데, 돈과 명예가 무슨 소용이 있으랴. 운동합시다.", "Only when you are healthy can you earn money and chase honor. Having lost your health, what use are money and honor? Let’s exercise."),
]
_SPEAK4C = [("요즘 한국에는 청소년들의 비만이 큰 사회문제가 되고 있습니다. 청소년들의 비만문제를 해결하기 위해서 정부가 어떤 조치를 취하면 좋을지 생각해 보고 친구들과 의견을 나눠 보세요.", "These days in Korea, teenage obesity has become a big social problem. Think about what measures the government should take to solve the problem of teenage obesity and share your opinions with friends.")]
L6 = lesson(
    "U17 L4 · Part 3 (심화 학습): liver spots and a reader’s column on exercise",
    "심화 학습 · 기미 · 주근깨 · 자외선 · 운동 · 유산소 · 근력운동 · 청소년 비만 · 말해 봅시다",
    requires=[],
    cards=[
        card("학습활동 1: an article from the health page on liver spots and freckles", "The article, with my English. Answers: 1. The writer uses the film leads as examples because both live or lived in strong sunlight (a desert, a sunny football pitch) and, neglecting UV protection, developed liver spots and freckles around the eyes; so they show that pigmentation comes from sun exposure. 2. According to Dr. Shin, liver spots can recur whatever treatment is used, so a perfect cure cannot be guaranteed; therefore prevention is more important than treatment.", examples=passage(_SKIN4)),
        card("학습활동 3: a reader’s column on exercise (Hankyoreh)", "The column, by a woman reader whose name the book does not give, with my English (the book writes her height and weight and the times in figures; I wrote them out). Answers: 1. The best description of the writer’s recommendation: D, exercise regularly to live a healthier life. 2. Since she began exercising: body and mind are more comfortable and life is enjoyable; fatigue and stress are relieved; she takes everything positively and her expression is brighter; people say she looks younger; her relationship with her husband is better; she lost 7 kg. 3. The underline is not marked in the text; my best guess is “건강해야 돈도 벌 수 있고, 명예도 좇을 수 있다”: only when you are healthy can you earn money and chase honor.", examples=passage(_COL4)),
        card("말해 봅시다! (speaking)", "The book’s speaking prompt (the English is mine):", examples=passage(_SPEAK4C)),
        card("Activities left out", "학습활동 2 (Listening, track 005): a Donga editorial on swine influenza. The questions ask what the purpose of the editorial is (choose among educating the public about the danger, urging the government to act, conveying specific information, discouraging travel abroad), what action the World Health Organization took, and how the United States, Japan and China responded. It is audio."),
    ],
    exercises=uniq(
        _tr(_SKIN4[1:], k=3) + _tr(_COL4, k=3)
        + [M("Why does the writer mention the film leads?", "Both developed liver spots and freckles from sun exposure", ["Both are doctors", "Both love football", "Both had surgery"], "자외선."), M("Why is prevention more important than treatment for liver spots?", "They can recur whatever treatment is used", ["Treatment is free", "They never recur", "Treatment is easy"], "재발."), M("How is a freckle treated, according to the article?", "Usually one laser treatment improves it", ["Surgery", "A new diet", "Cold showers"], "레이저 치료."), M("What does the column’s writer recommend?", "Exercise regularly to live a healthier life", ["Earn more money young", "Eat less", "Work longer hours"], "운동합시다."), M("How much weight did the writer lose?", "7 kg", ["3 kg", "10 kg", "53 kg"], "칠 킬로그램."), M("What does she do every day after punching in at work?", "Aerobic and weight exercise together", ["Sleep", "Study English", "Swim only"], "유산소 및 근력 운동.")]
        + [F("기미는 어떤 치료를 해도 ___할 수 있다. (to recur)", "재발", ["노출", "장담"], "재발하다."), F("자외선 대책을 ___히 한 탓에 기미가 생겼다. (negligently)", "소홀", ["적절", "유망"], "소홀히."), F("매일 유산소 운동과 근력 운동을 ___하고 있다. (do together)", "병행", ["반문", "장담"], "병행하다.")]
        + [read_q("기미는 어떤 치료를 해도 재발할 수 있습니다"), read_q("치료보다 예방이 중요합니다"), read_q("운동을 하면 몸과 마음이 편해집니다"), read_q("건강을 잃었는데 돈과 명예가 무슨 소용이 있습니까")]
    ),
)

# ================================================================== L7 Part 3 vocabulary
_V3 = [
    ("학습활동 1", [
        ("노출(하다/되다)", "(露出) exposure; disclosure (to expose; to disclose/to be exposed; to be disclosed)", "방사능에 노출된 환자가 발생했습니다."),
        ("논란", "(論難) controversy; dispute", "이 문제는 논란의 여지가 많습니다.", "논쟁"),
        ("대개", "(大槪) usually; generally; mostly", "저는 퇴근 후에는 대개 테니스를 칩니다.", "보통, 일반적으로"),
        ("모래", "sand", "우리 아이는 모래로 장난하는 것을 좋아합니다."),
        ("소홀히 하다", "to neglect; to pay little attention to; to overlook", "건강을 소홀히 하면 나중에 후회해요."),
        ("자외선", "(紫外線) UV rays; ultraviolet rays; “out-of-violet (color) line”", "", "햇볕, 햇빛, 적외선"),
        ("장담(하다)", "(壯談) assurance; “assured talk” (to guarantee; to assure)", "이번 올림픽에서 한국팀이 금메달을 다섯 개 이상 딸 것을 장담합니다. 확실하지 않으면 장담하지 마세요."),
        ("재발(하다)", "(再發) recurrence; relapse (to recur; to have a relapse)", "피부병이 재발해서 다시 병원에 갔어요."),
        ("~(으)ㄹ 적", "when", "어렸을 적에 여기에서 자주 친구들과 놀았어요.", "~(으)ㄹ 때"),
        ("적용(하다/되다)", "(適用) application (to apply/to be applied)", "정부가 새로 발표한 법안이 올 십이 월부터 적용된다고 합니다.", "사용"),
        ("지대", "(地帶) a zone; an area", "이곳은 지대가 낮아서 홍수에 취약합니다.", "지역"),
        ("햇볕", "the warmth given by the sun’s rays; sunshine", "햇볕이 너무 따가워요. 그늘로 갑시다.", "햇빛, 볕"),
    ]),
    ("학습활동 2", [
        ("가려내다", "to sort out; to distinguish; to differentiate; identify", "한국 사람과 일본사람을 가려내기가 쉽지는 않습니다.", "구분하다, 구별하다"),
        ("경각심", "(警覺心) sense of alertness", "일본의 원전사고는 전 세계인들에게 경각심을 불러일으켰습니다."),
        ("국경", "(國境) a national border; a border between countries; “nation boundary”", "미국과 멕시코는 국경을 접하고 있습니다."),
        ("대응(하다)", "(對應) response; “counter response” (to respond; deal with)", "축구시합에서는 상대의 공격에 빠르게 대응해야 합니다.", "대처, 대책"),
        ("미온적", "(微溫的) lukewarm; tepid", "홍수로 큰 피해가 발생했지만 정부의 대책은 미온적입니다."),
        ("사실", "(事實) fact; truth; in fact", "거짓없이 사실대로 얘기해 주세요.", "현실"),
        ("상대적(으로)", "(相對的) relative(ly)", "우리 아이는 친구들에 비해 상대적으로 키가 작습니다.", "절대적(으로)"),
        ("선포(하다)", "(宣布) declaration; proclamation (to declare; to proclaim)", "정부는 청소년범죄와의 전쟁을 선포했어요."),
        ("세계보건기구", "(世界保健機構) World Health Organization; WHO", ""),
        ("시급하다", "(時急) to be urgent; to be pressing", "이재민들에게 깨끗한 물을 공급하는 것이 시급합니다."),
        ("시행(하다/되다)", "(施行) enforcement; implementation (to enforce; to implement/to be enforced; to be implemented; to be carried out)", "새 법률은 다음 달부터 시행에 들어간다고 합니다.", "실행하다"),
        ("유입(되다)", "(流入) inflow; influx (to flow in)", "낙동강에 폐수가 유입되어 경찰이 조사에 나섰습니다.", "유출"),
        ("조류독감", "(鳥類毒感) avian influenza; bird flu", ""),
        ("중증급성 호흡기증후군", "(重症急性 呼吸器症候群) SARS (Severe Acute Respiratory Syndrome, 사스)", ""),
        ("즉각", "(卽刻) immediately; instantly", "미국은 북한에 대하여 핵개발을 즉각 중지할 것을 요구했습니다.", "바로"),
        ("차단(하다/되다)", "(遮斷) blocking; shutting off (to block; to shut off/to be cut off)", "강한 햇빛을 차단하기 위해서 커튼이 필요해요."),
        ("촉발(하다/되다)", "(觸發) triggering; causing (to trigger; to cause/to be triggered; to be caused)", "이집트에서의 시위가 아랍 전체의 반정부시위를 촉발시켰습니다."),
        ("최소한", "(最小限) at least", "피해 복구에 최소한 오 년은 걸릴 것으로 보입니다.", "최대한"),
        ("한가하다", "(閑暇) to be free; to be idle", "비가 오는 날은 식당이 한가한 편이에요."),
    ]),
    ("학습활동 3", [
        ("고통", "(苦痛) pain; agony; torment", "암 환자들은 극심한 고통을 호소합니다."),
        ("그럭저럭", "one way or another; somehow", "우리 집은 부자는 아니지만 그럭저럭 생활할 수 있습니다."),
        ("근력운동", "(筋力運動) weight workout; weight training; “muscle power workout”", "", "유산소운동"),
        ("명예", "(名譽) honor", "이번 일을 저에게 맡겨 주신 것을 큰 명예라고 생각합니다."),
        ("반문하다", "(反問) to reply; to answer; to retort", "노동자들은 생산량이 많아졌으니 임금이 올라야 하지 않느냐고 반문했습니다."),
        ("병행(하다)", "(竝行) doing two different things at the same time; “parallel moving” (to handle two different things at the same time)", "집안일과 직장일을 병행하는 것은 쉽지 않습니다."),
        ("여지", "(餘地) room to move; leeway", "이번 일은 논란의 여지가 있습니다.", "여유"),
        ("~ 외에", "(外) besides; except for; other than; “outside”", "토요일과 일요일 외에 쉬는 날이 있습니까?", "~말고, ~밖에"),
        ("유산소 운동", "(有酸素 運動) aerobic exercise; “exercise with oxygen”", "", "근력운동, 무산소 운동"),
        ("~(으)랴", "rhetorical expression; poetic expression used in the past (mostly used in written language)", "대학에 가지 못할 이유가 무엇이랴. 떠나는 것이 아름답기만 하랴."),
        ("~(으)ㄹ지도 모르다", "might; could", "오후에 비가 올지도 모르니까 우산을 준비하세요."),
        ("적정", "(適正) optimal; reasonable", "시민단체는 물가를 적정 수준으로 맞춰 달라고 정부에 요구하고 있습니다.", "적당하다, 알맞다"),
        ("좇다", "to pursue; to seek; to chase", "자신의 꿈을 좇아 사는 인생은 행복합니다."),
        ("지름길", "a shortcut", "늦었으니까 지름길로 갑시다."),
        ("체격", "(體格) physique; build", "우리 아이는 체격이 좋아서 운동을 시키면 좋을 것 같아요.", "체질"),
        ("최대한", "(最大限) maximum; at the highest; as much as possible; “the biggest”", "휴가를 최대한 며칠까지 쓸 수 있습니까?", "최소한"),
        ("(얼굴) 표정", "(表情) a facial expression", "그는 그 얘기를 듣자 얼굴 표정이 갑자기 바뀌었다."),
    ]),
]
L7 = lesson(
    "U17 L4 · Part 3: words and expressions of the activities",
    "학습활동별 단어 및 표현 · 노출 · 논란 · 소홀히 하다 · 자외선 · 장담 · 재발 · 경각심 · 국경 · 대응 · 미온적 · 선포 · 시급하다 · 유입 · 즉각 · 차단 · 촉발 · 고통 · 병행 · 여지 · 적정 · 좇다 · 지름길 · 체격",
    requires=[],
    cards=[card("A note on the Korean in this list", "The book has no example for 자외선 (its related words are 햇볕, 햇빛, 적외선), 세계보건기구, 조류독감, 중증급성 호흡기증후군, 근력운동 and 유산소 운동 (these two list each other as related words; the book adds “exercise without oxygen” for 무산소 운동). 장담 and ~(으)랴 have two examples each, joined here. The examples have 5개 (written 다섯 개), 12월 (십이 월) and 5년 (오 년).")] + vocab_cards(_V3),
    exercises=uniq(vocab_exs(_V3, nf=16, nread=14)),
)

UNIT = unit("Semester III · Unit 17 · Lesson 4: Health and Common Ailments (건강과 질병)", [L1, L2, L3, L4, L5, L6, L7])
