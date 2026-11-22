"""Unit 27: KBC Semester 1, Unit 5, Chapter 20 - Body and Health (우리 몸과 건강).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 1, Unit 5, Student's Edition (2022).
Audio, video clips, photos, pictures, SMART Board activities, games, role-plays, partner and class activities are left
out. The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation
of a dialog or text sentence and every answer key is mine; the vocabulary meanings are the book's."""
import re as _re

import ko_rom as _K
from ko_kbc import *
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk


# ---- the core vocabulary of Chapter 20 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_BODY = [
    ("가슴", "the chest", "갑자기 달리기를 해서 가슴이 좀 아파요."),
    ("귀", "an ear", "김 일병은 귀가 커요."),
    ("눈", "an eye", "컴퓨터를 많이 해서 눈이 아픕니다."),
    ("다리", "a leg", "달리기하기 전에 다리 운동을 하세요."),
    ("등", "the back", "무거운 것을 많이 들어서 등이 아파요."),
    ("목", "a neck", "컴퓨터를 한 다음에는 꼭 목 운동을 하세요."),
    ("몸", "the body", "술과 담배는 몸에 안 좋아요."),
    ("무릎", "a knee", "등산을 한 후에 무릎이 아파요."),
    ("발", "a foot", "김 일병은 발이 커서 큰 사이즈의 신발을 신습니다."),
    ("발가락", "a toe", "회사에서는 발가락이 보이는 신발을 신지 마세요."),
    ("발목", "an ankle; “foot neck”", "저는 걷다가 발목을 잘 삐어요."),
    ("배", "the belly; the stomach", "점심을 많이 먹어서 배가 너무 불러요."),
    ("손", "a hand", "김 일병은 손이 참 예뻐요."),
    ("손목", "a wrist; “hand neck”", "컴퓨터를 오래 해서 손목이 아파요."),
    ("손가락", "a finger", "보통 피아니스트들은 손가락이 길어요."),
    ("어깨", "the shoulder", "수영 선수들은 보통 어깨가 넓어요."),
    ("얼굴", "a face", "한국의 여자 배우들은 보통 얼굴이 작아요."),
    ("입", "a mouth", "이 아이는 입이 참 작고 예쁘군요."),
    ("코", "a nose", "감기에 걸리면 코가 자주 막힙니다."),
    ("키", "the height (of a person or an animal)", "농구 선수들은 대부분 키가 커요."),
    ("팔", "an arm", "야구 선수들은 팔을 자주 다칩니다."),
    ("허리", "the lower back; the waist", "이 바지는 허리 사이즈가 안 맞아요."),
]
_CV_PHARM = [
    ("낫다", "to recover; to get well", "쉬면 감기가 빨리 낫습니다."),
    ("복용", "(服用) taking medicine (~하다: to take medicine)", "이 기침약을 하루에 세 번 복용하세요."),
    ("붕대", "(繃帶) a bandage; dressing (~하다: to apply a bandage)", "팔이 부러져서 붕대를 했습니다."),
    ("소화제", "(消化劑) an antacid; a digestive pill; “digestion medicine”", "햄버거를 많이 먹어서 소화제가 필요해요."),
    ("식전", "(食前) before a meal", "이 약은 식전에 드세요."),
    ("식후", "(食後) after a meal", f"이 소화제를 식후 {sino(30)} 분에 두 알씩 드세요."),
    ("알", "a tablet; pellet; “egg”", "배가 아프면 소화제를 한 알 드세요."),
    ("약사", "(藥師) a pharmacist", "약사가 감기약을 주었습니다."),
    ("진통제", "(鎭痛劑) a painkiller; a pain reliever; “pain-suppressing medicine”", "허리가 너무 아파요. 진통제 좀 주세요."),
    ("처방", "(處方) a prescription (~하다: to prescribe a medicine)", "진통제를 처방해 드리겠습니다."),
    ("해열제", "(解熱劑) fever reducer; fever medication; “fever-solving medicine”", "열이 있을 때 해열제를 먹습니다."),
]
_CV_SYM = [
    ("감기", "(感氣) a cold", "감기 때문에 학교를 며칠 못 나갔어요."),
    ("기침", "a cough (~하다/나다: to cough)", "기침을 많이 해서 목이 아파요."),
    ("배탈", "an upset stomach; a stomach disorder; “stomach trouble” (~나다: to suffer from stomach trouble)", "찬 음식을 먹어서 배탈이 났어요."),
    ("설사", "(泄瀉) diarrhea (~하다/나다: to have diarrhea)", "설사를 할 때는 따뜻한 물을 많이 드세요."),
    ("아프다", "to have/feel pain; to hurt; to be ill", "이가 아파서 음식을 잘 못 먹어요."),
    ("~(에) 걸리다", "to get (a cold, disease, etc.); “to be snagged”", "감기에 걸리면 잘 쉬는 것이 좋아요."),
    ("열", "(熱) a fever; heat (~나다: to have a fever)", "오늘 열이 나서 학교에 못 갔어요."),
    ("증상", "(症狀) a symptom", "기침과 콧물이 나는 증상이 있으면 감기약을 드세요."),
    ("콧물", "nasal discharge; “nose water” (~나다: to have a runny nose)", "어제부터 콧물이 많이 나요."),
    ("토하다", "(吐) to vomit", "저는 술을 많이 마시면 토합니다."),
    ("통증", "(痛症) a pain; “pain symptom”", "어제 통증이 심해서 잠을 잘 못 잤어요."),
]
_CV_INJ = [
    ("구급차", "(救急車) an ambulance; “first-aid vehicle”", "자동차 사고가 나서 구급차가 왔어요."),
    ("넘어지다", "to fall (over); to trip (over)", "어제 계단에서 넘어졌어요."),
    ("다치다", "to hurt oneself; to be injured", "스키 타다가 다쳤어요."),
    ("떨어지다", "to fall", "나무에서 떨어져서 발목을 다쳤어요."),
    ("베다", "to cut (a part of the body)", "종이에 손을 베었어요."),
    ("부딪치다 / 부딪히다", "to hit; to bump into", "자전거를 타고 가다가 차와 부딪쳤어요."),
    ("부러지다", "to be broken; to fracture", "축구를 하다가 다리가 부러졌어요."),
    ("붓다", "to swell; to become swollen", "어제 잠을 못 자서 얼굴이 부었어요."),
    ("뼈", "a bone", "스케이트를 타다가 다리 뼈가 부러졌어요."),
    ("삐다", "to sprain; to twist", "야구하다가 허리를 삐었어요."),
    ("상처", "(傷處) a wound; an injury (~나다/입다: to be wounded; to be injured)", "넘어져서 무릎에 상처가 났어요."),
    ("응급실", "(應急室) an emergency room", "팔이 부러져서 응급실에 갔어요."),
    ("풀다", "to unwrap; to unpack", "내일 깁스를 풀러 병원에 가요."),
]
_CV_LOAN = [
    ("피", "blood (~나다: to bleed)", "손가락을 베어서 피가 났어요."),
    ("깁스", "a cast (from the German word “gips” meaning plaster or gypsum) (~하다: to wear a cast)", "팔이 부러져서 팔에 깁스를 했어요."),
    ("앰뷸런스", "an ambulance", "도로에서 사고가 나면 앰뷸런스가 와요."),
    ("엑스레이", "x-ray (~찍다: to take an x-ray)", "다리 뼈를 다쳐서 엑스레이를 찍었어요."),
]
_CV_OTH = [
    ("가볍다", "to be light", "문에 부딪쳐서 가벼운 상처가 났어요."),
    ("-다가", "while (doing something)", "농구하다가 넘어졌어요."),
    ("다행히", "fortunately; luckily", "넘어졌지만 다행히 다치지 않았어요."),
    ("담배", "a cigarette", "술과 담배는 몸에 좋지 않습니다."),
    ("목발", "crutches; “wooden feet/legs”", "발목을 심하게 삐어서 목발을 쓰고 있어요."),
    ("며칠", "a few days; how many days", "며칠 전에 샌프란시스코에 갔다 왔어요. / 며칠 동안 한국에 머물렀어요?"),
    ("생기다", "to look; to appear; “to come into being”", "김 선생님 동생은 어떻게 생겼어요?"),
    ("심하다", "to be severe; to be extreme", "자전거를 타다가 넘어져서 심하게 다쳤어요."),
    ("외출", "(外出) going out; outing (~하다: to go out)", "부모님은 외출하셔서 지금 집에 안 계십니다."),
    ("-(으)ㄹ 뻔하다", "almost (did something); nearly (did something)", "앞 차와 부딪칠 뻔했어요."),
    ("-자마자", "as soon as; right after", "집에 돌아오자마자 샤워를 합니다."),
    ("잠", "sleep; slumber", "어젯밤에 잠을 잘 못 자서 오늘 피곤해요."),
    ("칼", "a knife", "칼에 손을 베었어요."),
    ("피하다", "to avoid; to keep away from", "다이어트를 하려면 단 음식을 피하세요."),
]
_CV_SINO = [("약", "(藥) medicine", "약국, 약사, 감기약, 농약")]
_ALL = {r[0]: r for r in _CV_BODY + _CV_PHARM + _CV_SYM + _CV_INJ + _CV_LOAN + _CV_OTH + _CV_SINO}
_EXTRA = {"머리": "the head; hair or hairstyle; the brain (the book’s note on 머리)", "약국": "a pharmacy; a drugstore; “medicine bureau” (the book’s example)", "약방": "a pharmacy; a drugstore; “medicine room” (the book’s example)", "마약": "an illegal drug (the book’s example)", "한약": "Korean traditional herbal medicine; “Korean medicine” (the book’s example)",
          "양약": "Western medicine; “medicine from the ocean” (the book’s example)", "감기약": "cold medicine (mine)", "치약": "toothpaste; “tooth medicine” (mine)", "한약방": "a Korean herbal medicine shop (mine)", "농약": "a pesticide; “farming medicine” (mine)", "안경": "glasses (mine)", "염색": "dyeing (mine)", "붕대를 하다": "to apply a bandage",
          "잘생기다": "to be good-looking (mine)", "넓다": "to be wide; to be broad (mine)", "짧다": "to be short (mine)", "크다": "to be big; to be tall (mine)", "작다": "to be small (mine)", "길다": "to be long (mine)", "갈색": "brown (mine)", "약사": "(藥師) a pharmacist", "유행하다": "to be popular; to be going around (mine)", "술": "alcohol; liquor (mine)",
          "하루": "a day; one day (mine)", "이틀": "two days (mine)", "사흘": "three days (mine)", "일주일": "a week (mine)", "연휴": "a long holiday; a long weekend (mine)", "방학": "a school break; vacation (mine)", "계단": "stairs (mine)", "엑스레이를 찍다": "to take an x-ray", "처방전": "a prescription (mine)", "회사원": "an office worker (mine)", "따뜻하다": "to be warm (mine)", "치료": "treatment (mine)"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)


# ================================================================== L1: objectives and the Sino-Korean syllable 약
_YAK = [("약국", "a pharmacy; a drugstore; “medicine bureau” (the book’s example)"), ("약방", "a pharmacy; a drugstore; “medicine room” (the book’s example)"), ("마약", "an illegal drug (the book’s example)"), ("한약", "Korean traditional herbal medicine; “Korean medicine” (the book’s example)"), ("양약", "Western medicine; “medicine from the ocean” (the book’s example)"),
        ("약사", "a pharmacist (the book’s core word; 師 = a master, mine)"), ("감기약", "cold medicine (mine)"), ("치약", "toothpaste; “tooth medicine” (mine; 치 (齒) = tooth)"), ("한약방", "a Korean herbal medicine shop (mine)"), ("농약", "a pesticide; “farming medicine” (mine)")]
L1 = lesson(
    "Ch 20 · What the chapter teaches and the Sino-Korean syllable 약",
    "우리 몸과 건강 · 약 (藥) · 약국 · 약사 · 감기약 · 치약 · 한약 · 농약",
    requires=[],
    cards=[
        card("What Chapter 20 teaches (우리 몸과 건강)",
             "Chapter 20, “Body and Health”, has three topic presentations, grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: describe a person’s physical appearance using the names for parts of the body; describe physical discomfort and the symptoms of common illnesses; ask for basic services at a drug store; describe the causes and symptoms of common injuries; and ask for basic medical services at a doctor’s office and hospital.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary; the conjunctive ending -는 동안(에) (while; during); the conjunctive ending -자마자 (as soon as; right after); the conjunctive ending -다가 (while; in the middle of); -(으)ㄹ 뻔하다, which is used to express near misses or close calls; and the Sino-Korean syllable 약 (藥)."),
        card("Sino-Korean in use: 약 (藥)",
             "This Sino-Korean syllable means medicine or drug, as in 약국 / 약방 (a pharmacy; a drugstore; “medicine bureau / room”), 마약 (illegal drug), 한약 (Korean traditional herbal medicine; “Korean medicine”) and 양약 (Western medicine; “medicine from the ocean”). The book asks you to guess the meaning of 약사, 감기약, 치약, 한약방 and 농약, with the hint 치 (齒): tooth. The answers are mine.",
             tables=[table(["Word", "Meaning"], [list(r) for r in _YAK], say=[0])]),
        card("Activities left out",
             "The vocabulary slide show, Activities 1 and 2 (SMART Board activities) and Activity 3 (the “Hot Seat” game, which the teacher starts) are picture, computer or game activities."),
    ],
    exercises=uniq(
        _tr(_YAK)
        + [M("What does the Sino-Korean syllable 약 (藥) mean?", "medicine; drug", ["a tooth", "a person", "a farm"], "약국, 약사, 감기약."), M("What does 치 (齒) mean?", "a tooth", ["medicine", "a farm", "a cold"], "치약 = toothpaste."), M("What does 약국 mean?", "a pharmacy", ["a hospital", "a school", "a market"], "약국 = a pharmacy; a drugstore."),
           M("What does 감기약 mean?", "cold medicine", ["a painkiller", "toothpaste", "a pesticide"], "감기 + 약."), M("What does 치약 mean?", "toothpaste", ["cold medicine", "a pesticide", "a pharmacist"], "치 (tooth) + 약."), M("What does 농약 mean?", "a pesticide", ["toothpaste", "cold medicine", "Korean herbal medicine"], "농 (farming) + 약."),
           M("What does 한약 mean?", "Korean traditional herbal medicine", ["Western medicine", "an illegal drug", "toothpaste"], "한약 = “Korean medicine”."), M("What does 양약 mean?", "Western medicine", ["Korean herbal medicine", "an illegal drug", "toothpaste"], "양약 = “medicine from the ocean”."), M("What does 마약 mean?", "an illegal drug", ["Western medicine", "a painkiller", "a vitamin"], "마약 = an illegal drug."),
           F("약을 파는 곳은 ___입니다. (a pharmacy)", "약국", ["극장", "시장"], "약국 = a pharmacy."), F("이를 닦을 때 ___을 씁니다. (toothpaste)", "치약", ["감기약", "농약"], "치약 = toothpaste."), F("감기에 걸리면 ___을 먹습니다. (cold medicine)", "감기약", ["치약", "농약"], "감기약 = cold medicine."),
           read_q("약국"), read_q("약사"), read_q("감기약"), read_q("치약"), read_q("한약방")]
    ),
)

# ================================================================== L2: Topic A
_A_TEXT = [
    ("지훈 씨는 키가 크고 어깨가 넓어요.", "Jihoon is tall and has broad shoulders."),
    ("키는 한 백팔십오 센티미터 정도 돼요.", "His height is about 185 centimeters."),
    ("머리는 짧고 갈색입니다.", "His hair is short and brown."),
    ("머리를 염색했어요.", "He dyed his hair."),
    ("그리고 안경을 썼어요.", "And he wears glasses."),
    ("지훈 씨는 얼굴은 작지만 눈, 코, 입이 모두 큽니다.", "Jihoon’s face is small, but his eyes, nose and mouth are all big."),
    ("아주 잘 생겼어요.", "He is very good-looking."),
    ("참, 지훈 씨는 며칠 전에 손을 다쳤어요.", "Oh, Jihoon hurt his hand a few days ago."),
    ("그래서 왼손에 붕대를 하고 있어요.", "So he has a bandage on his left hand."),
]
_A_WORDS = ["가슴", "귀", "넘어지다", "눈", "다리", "다치다", "등", "며칠", "목", "몸", "무릎", "발", "발가락", "발목", "배", "붕대", "생기다", "손", "손가락", "손목", "아프다", "어깨", "얼굴", "입", "코", "키", "팔", "허리"]
_BODY = [("머리", "the head; hair; the brain"), ("눈", "an eye"), ("코", "a nose"), ("입", "a mouth"), ("귀", "an ear"), ("얼굴", "a face"), ("목", "a neck"), ("어깨", "the shoulder"), ("가슴", "the chest"), ("등", "the back"), ("팔", "an arm"), ("손목", "a wrist"), ("손", "a hand"), ("손가락", "a finger"),
         ("허리", "the lower back; the waist"), ("배", "the belly; the stomach"), ("다리", "a leg"), ("무릎", "a knee"), ("발목", "an ankle"), ("발", "a foot"), ("발가락", "a toe")]
_HEAD = [("머리가 아파요.", "I have a headache. (the head)"), ("제 머리가 너무 길어요.", "My hair is too long. (hair or hairstyle)"), ("제 남동생은 머리가 좋아요.", "My younger brother is smart. (the brain)")]
L2 = lesson(
    "Ch 20 · Topic A: What does he look like?",
    "어떻게 생겼어요? · 얼굴 · 눈 · 코 · 입 · 귀 · 어깨 · 손 · 발 · 몸의 이름",
    requires=[],
    cards=[
        card("Topic A: What does he look like? (어떻게 생겼어요?)",
             "A man is describing the physical appearance of his friend Jihoon to his female co-worker, who is going on a blind date with Jihoon this weekend. (The English is mine; the book gives none. The book writes 185 cm; it is spelled out here.)",
             examples=passage(_A_TEXT)),
        card("Core words and phrases of Topic A",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_A_WORDS))]),
        card("Our body (우리 몸)",
             "The book shows a picture of the body with the names of its parts. The labels (the English is the book’s, from the Core Vocabulary; 머리 is from the book’s note):",
             tables=[ktable(_BODY)]),
        card("Note on 머리",
             "In Korean, 머리 can refer to one of the following: 1) the head, as in 머리가 아파요 (I have a headache); 2) hair or hairstyle, as in 제 머리가 너무 길어요 (My hair is too long); and 3) “the brain”, as in 제 남동생은 머리가 좋아요 (My younger brother is smart).",
             examples=passage(_HEAD)),
        card("Activities left out",
             "The SMART Board activities and the listening of the Presentation Activity, Follow-up 1 a (listening to three segments of a conversation about the physical appearance of three newly hired people) and b (listening to conversations about the area of discomfort and its cause) are computer or audio activities. Follow-up 2 (the “코, 코, 코” game: the teacher points to a body part and says a word, and the students point to the part named; the last student left takes over) is a class game."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _A_WORDS if w not in ("며칠", "생기다", "붕대", "아프다", "넘어지다", "다치다")] + ["머리"]))
        + _tr(_A_TEXT + _HEAD)
        + [M("How tall is Jihoon?", "About 185 centimeters", ["About 165 centimeters", "About 195 centimeters", "About 175 centimeters"], "한 백팔십오 센티미터 정도."), M("What is Jihoon’s hair like?", "Short and brown", ["Long and black", "Short and gray", "Long and brown"], "머리는 짧고 갈색입니다."),
           M("What did Jihoon do to his hair?", "He dyed it", ["He cut it", "He lost it", "He covered it"], "머리를 염색했어요."), M("What does Jihoon wear on his face?", "Glasses", ["A mask", "Sunglasses", "A hat"], "안경을 썼어요."),
           M("Which parts of Jihoon’s face are big?", "Eyes, nose and mouth", ["Ears", "Chin", "Forehead"], "눈, 코, 입이 모두 큽니다."), M("What is small about Jihoon?", "His face", ["His eyes", "His shoulders", "His height"], "얼굴은 작지만."),
           M("What happened to Jihoon a few days ago?", "He hurt his hand", ["He fell ill", "He dyed his hair", "He broke his leg"], "며칠 전에 손을 다쳤어요."), M("Which hand has a bandage?", "The left hand", ["The right hand", "Both hands", "Neither"], "왼손에 붕대를 하고 있어요."),
           M("Which does 머리가 좋아요 mean?", "He or she is smart (the brain)", ["He or she has a headache", "His or her hair is long", "He or she is tall"], "머리 can mean the head, hair or the brain."), M("Which does 머리가 아파요 mean?", "I have a headache", ["I am smart", "My hair is long", "My hair hurts"], "머리 = the head."),
           F("지훈 씨는 키가 크고 ___가 넓어요. (shoulders)", "어깨", ["무릎", "손목"], "어깨 = the shoulder."), F("얼굴은 작지만 눈, 코, ___이 모두 큽니다. (mouth)", "입", ["귀", "손"], "입 = a mouth."), F("왼손에 ___를 하고 있어요. (a bandage)", "붕대", ["깁스", "안경"], "붕대 = a bandage."),
           F("지훈 씨는 며칠 전에 손을 ___. (hurt)", "다쳤어요", ["넘어졌어요", "아팠어요"], "다치다 = to hurt oneself."), F("아주 잘 ___. (is good-looking)", "생겼어요", ["넘어졌어요", "다쳤어요"], "생기다 = to look; to appear."),
           read_q("어깨가 넓어요"), read_q("머리는 짧고 갈색입니다"), read_q("안경을 썼어요"), read_q("붕대를 하고 있어요"), read_q("아주 잘 생겼어요")]
    ),
)

# ================================================================== L3: Activities A
_GROUPS = [("얼굴과 머리", "the face and the head", [("머리", "the head; hair; the brain"), ("얼굴", "a face"), ("눈", "an eye"), ("코", "a nose"), ("입", "a mouth"), ("귀", "an ear")]), ("팔과 손", "the arm and the hand", [("어깨", "the shoulder"), ("팔", "an arm"), ("손목", "a wrist"), ("손", "a hand"), ("손가락", "a finger")]),
           ("몸통", "the trunk", [("목", "a neck"), ("가슴", "the chest"), ("등", "the back"), ("배", "the belly; the stomach"), ("허리", "the lower back; the waist")]), ("다리와 발", "the leg and the foot", [("다리", "a leg"), ("무릎", "a knee"), ("발목", "an ankle"), ("발", "a foot"), ("발가락", "a toe")])]
_DESC = [("a. 이 사람은 코가 작고 눈도 작습니다. 그렇지만 귀가 큽니다.", "a. This person has a small nose and small eyes, too. But the ears are big."), ("b. 이 사람은 눈과 입이 크고, 목이 깁니다.", "b. This person has big eyes and a big mouth, and a long neck."),
         ("c. 이 사람은 코가 크고 눈이 작습니다. 얼굴이 좀 깁니다.", "c. This person has a big nose and small eyes. The face is a little long."), ("d. 이 사람은 눈과 입이 작습니다. 머리가 깁니다.", "d. This person has small eyes and a small mouth. The hair is long.")]
_DESC = [(_re.sub(r"^[a-d]\. ", "", a), b) for a, b in _DESC]
_MODEL = [("범인이 어떻게 생겼습니까?", "What does the suspect look like? (the book’s model)"), ("키가 크고 머리가 갈색입니다.", "He is tall and his hair is brown. (the book’s model)")]
L3 = lesson(
    "Ch 20 · Activities A: parts of the body and describing faces",
    "몸의 이름 · 눈과 입이 크고 목이 깁니다 · 범인이 어떻게 생겼습니까?",
    requires=[],
    cards=[
        card("Activity 1 (Writing): the Korean words for parts of the body",
             "The book shows drawings of the body and asks you to fill in the boxes with the Korean words for parts of the body. The drawings are left out; the answers are the words of the previous lesson, which I group here (the grouping is mine).",
             tables=[table(["Group", "Meaning (mine)", "Words"], [[a, b, ", ".join(w for w, _ in c)] for a, b, c in _GROUPS], say=[0, 2])]),
        card("Activity 3 (Reading): four descriptions of facial features",
             "The book gives four descriptions and four pictures of faces and asks you to write the appropriate description letter under each picture. The descriptions are the book’s (the letters a to d are left off the lines below and given in the English); the pictures are left out, so the matching key is not possible here. The English is mine.",
             examples=passage(_DESC)),
        card("Activity 4: What does the suspect look like?",
             "In this activity you investigate a possible criminal act: a suspect left a brown box in front of the main entrance of a hospital. You have four eyewitness descriptions of the suspect’s physical appearance (two written descriptions and two recordings), compare your notes in Korean and draw a picture of the suspect. The book’s model for Step c:",
             examples=passage(_MODEL)),
        card("Activities left out",
             "Activity 2 (listening to conversations about physical discomfort and its causes and filling in a table) is an audio activity; Activity 4 (the written descriptions and the recordings of the suspect, group work, drawing a picture and posting it) is a group and class activity; the descriptions are not in the book’s text."),
    ],
    exercises=uniq(
        _tr(_DESC + _MODEL) + vocab_exercises([w for _, _, c in _GROUPS for w in c][:12])
        + [M("Which description has big eyes, a big mouth and a long neck?", "b", ["a", "c", "d"], "눈과 입이 크고, 목이 깁니다."), M("Which description has a small nose, small eyes and big ears?", "a", ["b", "c", "d"], "코가 작고 눈도 작습니다. 그렇지만 귀가 큽니다."), M("Which description has a big nose, small eyes and a long face?", "c", ["a", "b", "d"], "코가 크고 눈이 작습니다. 얼굴이 좀 깁니다."),
           M("Which description has small eyes, a small mouth and long hair?", "d", ["a", "b", "c"], "눈과 입이 작습니다. 머리가 깁니다."), M("What is left in front of the hospital’s main entrance in Activity 4?", "A brown box", ["A red bag", "A black car", "A letter"], "A brown box."),
           M("Which group contains 어깨, 팔 and 손?", "The arm and the hand", ["The leg and the foot", "The face and the head", "The trunk"], "어깨, 팔, 손목, 손, 손가락."), M("Which group contains 무릎, 발목 and 발가락?", "The leg and the foot", ["The arm and the hand", "The face and the head", "The trunk"], "다리, 무릎, 발목, 발, 발가락."),
           F("이 사람은 눈과 입이 크고, 목이 ___. (is long)", "깁니다", ["작습니다", "넓습니다"], "길다 → 깁니다."), F("이 사람은 코가 작고 눈도 ___. (small)", "작습니다", ["큽니다", "깁니다"], "작다 → 작습니다."), F("범인이 어떻게 ___? (does he look)", "생겼습니까", ["넘어졌습니까", "다쳤습니까"], "생기다 = to look."),
           F("키가 크고 머리가 ___입니다. (brown)", "갈색", ["파랑", "하양"], "갈색 = brown."),
           read_q("범인이 어떻게 생겼습니까"), read_q("눈과 입이 크고 목이 깁니다"), read_q("코가 크고 눈이 작습니다"), read_q("얼굴이 좀 깁니다"), read_q("귀가 큽니다")]
    ),
)

# ================================================================== L4: Topic B
_B_DLG = [
    ("약사", "어떻게 오셨어요?", "What brings you here?"),
    ("영호", "어제부터 목이 아프고 열이 나요.", "Since yesterday I have a sore throat and a fever."),
    ("약사", "다른 증상은 없으세요?", "Do you have any other symptoms?"),
    ("영호", "음, 기침도 하고 콧물도 조금 나요.", "Um, I cough and have a little runny nose, too."),
    ("약사", "요즘 유행하는 감기에 걸리셨네요!", "You have caught the cold that is going around these days!"),
    ("영호", "그런 것 같아요. 약 좀 주세요.", "I think so. Please give me some medicine."),
    ("약사", "네, 여기 있어요. 이 약을 하루에 세 번, 두 알씩 드세요.", "Yes, here you are. Take this medicine three times a day, two tablets at a time."),
    ("영호", "식전에요? 식후에요?", "Before meals? After meals?"),
    ("약사", "식후 삼십 분 후에 드세요. 약을 복용하는 동안에는 술과 담배를 피하셔야 합니다.", "Take it 30 minutes after meals. While you are taking the medicine, you have to avoid alcohol and cigarettes."),
    ("영호", "네. 그리고 소화제도 좀 주세요.", "Yes. And please give me some digestive medicine, too."),
    ("약사", "배탈도 나셨군요!", "You have an upset stomach, too!"),
    ("영호", "네. 오늘 아침에 토하고 설사도 했어요.", "Yes. This morning I vomited and had diarrhea, too."),
    ("약사", "그럼, 이 약을 드세요.", "Then take this medicine."),
    ("영호", "감기약하고 같이 먹어도 돼요?", "May I take it together with the cold medicine?"),
    ("약사", "아니요. 이 약은 아침에 일어나자마자 드셔야 합니다. 이틀 정도 복용하시면 나으실 거예요.", "No. You must take this medicine as soon as you get up in the morning. If you take it for about two days, you will get better."),
]
_B_WORDS = ["감기", "~(에) 걸리다", "기침", "낫다", "담배", "배탈", "복용", "소화제", "설사", "식전", "식후", "알", "약사", "열", "-자마자", "증상", "콧물", "토하다", "피하다", "해열제"]
_B_TABLE = [["Symptoms", "Sore throat, fever, cough, a little runny nose, upset stomach, vomiting, diarrhea"], ["Medicines and instructions", "Cold medicine: three times a day, two tablets each, 30 minutes after meals; avoid alcohol and cigarettes while taking it. Digestive medicine: take it as soon as you get up in the morning (not together with the cold medicine); about two days of taking it should cure it."]]
L4 = lesson(
    "Ch 20 · Topic B: Take this cold medicine three times a day",
    "이 감기약을 하루에 세 번 드세요 · 약국 · 감기 · 기침 · 콧물 · 소화제 · 식후",
    requires=[],
    cards=[
        card("Topic B: Take this cold medicine three times a day (이 감기약을 하루에 세 번 드세요)",
             "Youngho is consulting with a pharmacist at a drugstore. (The English is mine; the book gives none. The book writes 30분; it is spelled out here. The book’s title says 이 감기약을, while the pharmacist in the dialog says 이 약을; I keep both as in the book.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened. The book shows pictures of 해열제, 진통제, 감기약 and 소화제; the pictures are left out.",
             tables=[ktable(_rows(_B_WORDS))]),
        card("Presentation Activity d: the symptoms and the medicines (mine)",
             "The book asks you to determine the customer’s symptoms, the medicines and the pharmacist’s instructions, and to write them in English in a table; the book leaves the table blank. These are my answers.",
             tables=[table(["", "Answer (mine)"], _B_TABLE)]),
        card("Activities left out",
             "The SMART Board activity, the sentence strips of the Presentation Activity (sorting the strips into the parts of a customer and a pharmacist), the recording check and Follow-up 1 (listening to three conversations between a customer and a pharmacist, writing two symptoms each) are computer, partner or audio activities. Follow-up 2 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _B_WORDS if not w.startswith(("-", "~"))]))
        + _tr(_strip(_B_DLG))
        + [M("Since when does Youngho have a sore throat?", "Since yesterday", ["Since last week", "Since this morning", "Since last month"], "어제부터 목이 아프고."), M("Which other symptoms does Youngho have?", "Cough and a little runny nose", ["Headache and backache", "A broken arm", "A rash"], "기침도 하고 콧물도 조금 나요."),
           M("What does the pharmacist say about the cold?", "It is the one that is going around these days", ["It is not a cold", "It is very rare", "It is a serious illness"], "요즘 유행하는 감기에 걸리셨네요."), M("How should he take the medicine?", "Three times a day, two tablets at a time", ["Once a day, one tablet", "Twice a day, three tablets", "Five times a day"], "하루에 세 번, 두 알씩."),
           M("When should he take it?", "30 minutes after meals", ["Before meals", "At bedtime", "With the meal"], "식후 삼십 분 후에."), M("What must he avoid while taking the medicine?", "Alcohol and cigarettes", ["Coffee and tea", "Meat", "Sports"], "술과 담배를 피하셔야 합니다."),
           M("What other medicine does Youngho ask for?", "Digestive medicine", ["Fever reducer", "A painkiller", "A bandage"], "소화제도 좀 주세요."), M("What other symptoms does Youngho have this morning?", "Vomiting and diarrhea", ["Fever", "A cough", "A rash"], "토하고 설사도 했어요."),
           M("When should he take the digestive medicine?", "As soon as he gets up in the morning", ["Together with the cold medicine", "At bedtime", "Before dinner"], "아침에 일어나자마자."), M("How long should he take it?", "About two days", ["About a week", "One day", "A month"], "이틀 정도 복용하시면."),
           F("어제부터 목이 아프고 ___이 나요. (fever)", "열", ["약", "알"], "열이 나다 = to have a fever."), F("기침도 하고 ___도 조금 나요. (runny nose)", "콧물", ["설사", "배탈"], "콧물이 나다 = to have a runny nose."), F("감기에 ___ 같아요. (I have caught)", "걸린 것", ["걸리는 것", "걸릴 것"], "감기에 걸리다 = to catch a cold."),
           F("약을 복용하는 ___에는 술과 담배를 피하셔야 합니다. (while)", "동안", ["다음", "전"], "-는 동안에 = while."), F("아침에 일어나___ 드셔야 합니다. (as soon as)", "자마자", ["다가", "는 동안"], "-자마자 = as soon as."), F("배___도 나셨군요! (an upset stomach)", "탈", ["통", "증"], "배탈 = an upset stomach."),
           read_q("목이 아프고 열이 나요"), read_q("기침도 하고 콧물도 나요"), read_q("두 알씩 드세요"), read_q("식후에요"), read_q("일어나자마자 드세요")]
    ),
)

# ================================================================== L5: Follow-up 2 (Q&A) and Activity 2 (family notes)
_QA = [
    ("약사 선생님 안녕하세요? 저는 회사원입니다.", "Hello, pharmacist. I am an office worker."),
    ("며칠 전부터 열이 나고 기침을 합니다.", "For the last few days I have had a fever and a cough."),
    ("그래서 감기약을 먹고 있습니다.", "So I have been taking cold medicine."),
    ("그런데 아직 낫지를 않습니다.", "But I am still not getting better."),
    ("그리고 지금은 토하고 설사까지 합니다.", "And now I even vomit and have diarrhea."),
    ("어떻게 하면 될까요?", "What should I do?"),
]
_QA_A = [
    ("요즘 유행하는 감기에 걸리신 것 같습니다.", "You seem to have caught the cold that is going around these days."),
    ("이 감기는 쉽게 낫지 않습니다.", "This cold does not get better easily."),
    ("나으려면 먼저 많이 쉬셔야 합니다.", "To get better, first you must rest a lot."),
    ("토하고 설사를 하시면 따뜻한 물을 많이 마시는 것이 좋습니다.", "If you vomit and have diarrhea, it is good to drink a lot of warm water."),
    ("그리고 감기약과 소화제를 함께 드시는 것이 좋을 것 같습니다.", "And it seems good to take the cold medicine and the digestive medicine together."),
    ("증상이 계속되면 병원에 가 보시기 바랍니다.", "If the symptoms continue, please go to a hospital."),
]
_FAM = [
    ("여보, 나, 오늘 몸이 좀 안 좋아. 기침도 하고 콧물도 나. 약국에 가서 감기약 좀 사다 줘. 그럼 회사 다녀올게.", "Honey, I don’t feel so well today. I cough and have a runny nose, too. Please go to the pharmacy and buy me some cold medicine. Well then, I will go to work and be back.", "남편"),
    ("엄마, 어젯밤부터 배가 아파요. 음식을 잘못 먹은 것 같아요. 오늘 아침에는 설사도 했어요. 집에 소화제가 없어요. 소화제 좀 사다 주세요.", "Mom, my stomach has hurt since last night. I think I ate something wrong. This morning I had diarrhea, too. There is no digestive medicine at home. Please buy me some digestive medicine.", "아들 영진"),
    ("엄마, 오늘 열이 조금 있는 것 같아요. 기침도 하구요. 해열제를 찾아봤는데 찾을 수가 없어요. 엄마가 해열제 좀 찾아 주세요. 잠깐 나갔다 올게요.", "Mom, I think I have a little fever today. And I cough, too. I looked for a fever reducer, but I can’t find it. Please find me a fever reducer. I will go out for a moment and come back.", "딸 수미"),
]
L5 = lesson(
    "Ch 20 · Topic B, Follow-up 2 and Activities: a pharmacy Q&A and notes from the family",
    "약사 선생님 안녕하세요 · 낫지를 않습니다 · 소화제 좀 사다 주세요 · 해열제 좀 찾아 주세요",
    requires=[],
    cards=[
        card("Follow-up 2 (Reading): a question to a pharmacy’s website",
             "Hyunsoo has been taking cold medicine for the last few days, but his condition is not improving. Because he does not have time to see a doctor, he posted a question on a pharmacy’s website Q&A section. The book asks you to fill in a table in English (the patient’s symptoms and the pharmacist’s advice). The texts are the book’s (the book marks them Q and A); the English is mine. The question:",
             examples=passage(_QA)),
        card("The pharmacist’s reply",
             "The reply (the English is mine):",
             examples=passage(_QA_A)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Patient’s symptoms", "Pharmacist’s advice"], [["Fever and cough for a few days, not getting better with cold medicine; now vomiting and diarrhea", "Rest a lot; drink a lot of warm water if vomiting and having diarrhea; take the cold medicine and the digestive medicine together; go to a hospital if the symptoms continue"]])]),
        card("Activity 2 (Reading): three family notes",
             "The book gives three notes in which three ill family members each make a request, and asks you to fill in a table in English (family member, symptoms, request). The notes were read from the page image (the notes are signed 남편, 아들 영진 and 딸 수미); the English is mine. The husband’s note:",
             examples=passage([(a, b) for a, b, c in _FAM[:1]])),
        card("The son’s and the daughter’s notes",
             "The other two notes:",
             examples=passage([(a, b) for a, b, c in _FAM[1:]])),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Family member", "Symptoms", "Request"], [["남편 (husband)", "Not feeling well; cough and a runny nose", "Go to the pharmacy and buy cold medicine"], ["아들 영진 (son Youngjin)", "Stomach ache since last night, maybe from wrong food; diarrhea this morning", "Buy digestive medicine"], ["딸 수미 (daughter Sumi)", "A little fever; a cough", "Find a fever reducer"]])]),
        card("Activities left out",
             "Activity 1 (a SMART Board activity), Activity 3 (listening to two conversations between a customer and a pharmacist and filling in the illness, symptoms, pharmacist’s advice and dosage) and Activity 4 (a role-play with situation cards: a friend with symptoms and a friend giving remedies, in pairs) are computer, audio or partner activities."),
    ],
    exercises=uniq(
        _tr(_QA + _QA_A + [(a, b) for a, b, c in _FAM])
        + [M("What is Hyunsoo’s job?", "An office worker", ["A pharmacist", "A doctor", "A teacher"], "저는 회사원입니다."), M("What medicine has he been taking?", "Cold medicine", ["A painkiller", "A digestive pill", "Vitamins"], "감기약을 먹고 있습니다."), M("What symptoms does Hyunsoo have now besides fever and cough?", "Vomiting and diarrhea", ["A rash", "A broken bone", "A toothache"], "토하고 설사까지 합니다."),
           M("What does the pharmacist say you must do first to get better?", "Rest a lot", ["Go to the hospital", "Exercise", "Take more medicine"], "나으려면 먼저 많이 쉬셔야 합니다."), M("What is good to drink if you vomit and have diarrhea?", "Warm water", ["Cold water", "Coffee", "Juice"], "따뜻한 물을 많이 마시는 것이 좋습니다."),
           M("What does the pharmacist say about the cold medicine and the digestive medicine?", "It is good to take them together", ["Never take them together", "Take the digestive one only", "Take the cold one only"], "함께 드시는 것이 좋을 것 같습니다."), M("What should he do if the symptoms continue?", "Go to a hospital", ["Stop the medicine", "Go on a trip", "Call his mother"], "병원에 가 보시기 바랍니다."),
           M("What does the husband ask his wife to do?", "Buy cold medicine at the pharmacy", ["Make dinner", "Call the doctor", "Pick him up"], "약국에 가서 감기약 좀 사다 줘."), M("What does the son (Youngjin) ask his mother to do?", "Buy digestive medicine", ["Buy cold medicine", "Find a fever reducer", "Cook"], "소화제 좀 사다 주세요."),
           M("What does the daughter (Sumi) ask her mother to do?", "Find a fever reducer", ["Buy cold medicine", "Buy digestive medicine", "Call the doctor"], "해열제 좀 찾아 주세요."), M("Why does the son’s stomach hurt?", "He thinks he ate the wrong food", ["He fell", "He has a cold", "He didn’t sleep"], "음식을 잘못 먹은 것 같아요."),
           F("감기약 좀 ___ 줘. (buy and bring)", "사다", ["사서", "사고"], "사다 주다 = to buy and bring."), F("아직 낫지를 ___. (not)", "않습니다", ["합니다", "있습니다"], "-지 않다 = not."), F("증상이 계속되면 ___에 가 보시기 바랍니다. (a hospital)", "병원", ["약국", "학교"], "병원 = a hospital."),
           read_q("약사 선생님 안녕하세요"), read_q("토하고 설사까지 합니다"), read_q("따뜻한 물을 많이 마시는 것이 좋습니다"), read_q("소화제 좀 사다 주세요"), read_q("해열제를 찾아봤어요")]
    ),
)

# ================================================================== L6: Grammar A: -는 동안(에)
def _dong(verb):
    return attr(verb)[0] + " 동안"


_DONG_V = [("공부하다", "to study"), ("기다리다", "to wait"), ("읽다", "to read"), ("먹다", "to eat"), ("자다", "to sleep"), ("보다", "to watch"), ("살다", "to live"), ("만들다", "to make"), ("있다", "to be (somewhere); to stay"), ("운동하다", "to work out")]
_DONG_EX = [("한국에 있는 동안에 한국말을 배우겠습니다.", "I will learn Korean while (I am) in Korea."), ("친구가 운동하는 동안에 나는 공부합니다.", "I study while my friend works out."), ("점심 시간 동안", "during the lunch hour"), ("두 시간 동안", "for two hours"),
            ("삼십 초 동안", "for 30 seconds"), ("오 분 동안", "for 5 minutes"), ("한 시간 동안", "for 1 hour"), ("이틀 동안", "for 2 days"),
            ("기다리시는 동안에 이 잡지 좀 보세요.", "While waiting, please read this magazine."), ("한국에 있는 동안에 많은 것을 배웠어요.", "While I was in Korea, I learned many things."), ("여름 방학 동안에 유럽에 갈 거예요.", "During summer vacation, I am going to Europe."), ("이 약을 이틀 동안 복용하세요.", "Please take this medicine for two days.")]
_DONG_NOUN = [("연휴", "a long holiday"), ("수업", "a class"), ("이틀", "two days"), ("일주일", "a week"), ("사흘", "three days"), ("겨울 방학", "winter vacation")]
_DONG_F1 = [("이십 분 동안 책을 읽었습니다.", "I read a book for 20 minutes. (the book’s model)"), ("방학 동안 고향에 다녀왔습니다.", "During the school break I went to my hometown and came back. (the book’s model)"), ("제가 책을 읽는 동안에 김 일병은 설거지를 합니다.", "While I read a book, PFC Kim does the dishes. (the book’s model)")]
_LA = ["연휴", "일주일", "사흘", "수업시간", "한 시간", "겨울방학"]
_LB = ["여름방학", "삼십 분", "주말", "한 달", "점심시간", "일 년 육 개월"]
_VA = [("요리하다", "to cook"), ("공부하다", "to study"), ("잠을 자다", "to sleep"), ("신문을 보다", "to read the newspaper"), ("컴퓨터 게임을 하다", "to play computer games")]
_VB = [("청소하다", "to clean"), ("음악을 듣다", "to listen to music"), ("영화를 보다", "to watch a movie"), ("뉴스를 듣다", "to listen to the news"), ("숙제를 하다", "to do homework")]
_EMAIL = [
    ("성수야, 잘 지내?", "Seongsu, are you doing well?"), ("시험 공부하는 동안에 밥은 잘 먹고 있어?", "Are you eating well while studying for your tests?"), ("누나는 일주일 동안 감기로 아팠어.", "I (your older sister) was sick with a cold for a week."), ("목도 아프고 기침도 많이 하고 그랬어.", "My throat hurt and I coughed a lot, and so on. (the book ends the line with an ellipsis; the wording here is mine)"),
    ("이번 감기가 쉽게 낫지 않는 것 같아.", "It seems this cold doesn’t get better easily."), ("이번 겨울 동안 다시 감기에 걸리지 않으려면 매일 운동을 해.", "To not catch a cold again this winter, exercise every day."), ("누나도 매일 한 시간 동안 수영을 할 거야.", "I am also going to swim for an hour every day."),
    ("다음 달이 겨울방학이니까 집에 오지?", "Next month is the winter vacation, so you are coming home, right?"), ("네가 집에 와 있는 동안 누나가 맛있는 음식을 많이 만들어 줄게.", "While you are at home, I will make lots of delicious food for you."), ("보고 싶다.", "I miss you."),
]
L6 = lesson(
    "Ch 20 · Grammar A: “while” and “during” with -는 동안(에) and ~ 동안(에)",
    "한국에 있는 동안 · 이틀 동안 · 점심 시간 동안 · 여름 방학 동안 · 약을 복용하는 동안",
    requires=[],
    cards=[
        card("Expressing “while” or “during”",
             "In English, we use the conjunction while or the preposition during to express an action or event that takes place simultaneously with another action or event: “I will learn Korean while (I stay) in Korea” and “I will learn Korean during my stay in Korea”. In Korean, we express simultaneous actions or events by using the conjunctive ending -는 동안(에).\n\n"
             "동안 literally means an interval or a space of time. Thus the literal translation of -는 동안에 is “for an interval when” or “in the space of time when”. ~ 동안(에) also can be preceded by a noun that denotes time, as in 점심 시간 동안(에) (during the lunch hour) and 두 시간 동안 (for two hours); in this case ~ 동안(에) can be translated as during or for.",
             examples=passage(_DONG_EX[:4])),
        card("The 에",
             "The time marker 에 in -는 동안에 or ~ 동안에 is optional. However, 에 has to be deleted if 동안에 is preceded by a noun that shows a time length, as in 30초 동안 (for 30 seconds), 5분 동안 (for 5 minutes), 한 시간 동안 (for 1 hour) and 이틀 동안 (for 2 days). (The book writes the digits; they are spelled out here.)",
             examples=passage(_DONG_EX[4:8])),
        card("The rule",
             "action verb stem + 는 동안(에); noun + 동안(에).",
             tables=[table(["Condition", "Rule", "Example"], [["After an action verb stem", "add 는 동안(에)", "공부하다 → 공부하는 동안(에); 기다리다 → 기다리는 동안(에)"], ["After a noun", "add 동안(에)", "연휴 → 연휴 동안(에); 수업 → 수업 동안(에); 이틀 → 이틀 동안"]])],
             examples=passage(_DONG_EX[8:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (verbs with an ㄹ-ending stem lose ㄹ before 는: 살다 → 사는, 만들다 → 만드는).",
             tables=[table(["Verb", "Meaning", "-는 동안"], [[v, m, _dong(v)] for v, m in _DONG_V], say=[0, 2]), table(["Noun", "Meaning", "+ 동안"], [[n, m, n + " 동안"] for n, m in _DONG_NOUN], say=[0, 2])]),
        card("Follow-up 1: nouns and verbs",
             f"Partners pick a noun with 동안(에) and make a sentence (the book’s models below). Lists: List A: {', '.join(_LA)}; List B: {', '.join(_LB)}. In Step b, partners combine a verb of List A with a verb of List B with -는 동안(에). List A verbs: 요리하다, 공부하다, 잠을 자다, 신문을 보다, 컴퓨터 게임을 하다. List B verbs: 청소하다, 음악을 듣다, 영화를 보다, 뉴스를 듣다, 숙제를 하다. (The book writes 30분 and 1년 6개월; they are spelled out here.)",
             examples=passage(_DONG_F1)),
        card("Follow-up 2 (Reading): an e-mail from an older sister",
             "The book gives an e-mail from a woman to her younger brother who lives in a college dormitory and asks you to identify five sentences that contain ~ 동안(에) or -는 동안(에), underline and number them (the first one is done for you) and translate the phrases into English. The e-mail is the book’s (the address is left out); the English is mine.",
             examples=passage(_EMAIL)),
        card("The five phrases (mine)",
             "The book gives the first answer, “while studying for a test”; the others are my answers.",
             tables=[table(["Phrase with 동안(에)", "Translation"], [["시험 공부하는 동안에", "while studying for a test (the book’s)"], ["일주일 동안", "for a week"], ["이번 겨울 동안", "during this winter"], ["한 시간 동안", "for an hour"], ["네가 집에 와 있는 동안", "while you are at home"]], say=[0])]),
        card("Activities left out",
             "Follow-up 1 (partner activities with lists) is a partner activity; Follow-up 2’s underlining is not repeated."),
    ],
    exercises=uniq(
        _fk(_DONG_V, _dong, "“while” (-는 동안)", lambda v: [stem(v) + " 동안", stem(v) + "은 동안", stem(v) + "고 동안", attr(v)[1] + " 동안"])
        + _tr(_DONG_EX + _DONG_F1 + _EMAIL)
        + [M(f"How do you say “for {m}”?", n + " 동안", [n + " 동안에", n + "는 동안", n + "에서"], f"{n} + 동안.") for n, m in [("이틀", "two days"), ("일주일", "a week"), ("사흘", "three days")] if True][:0]
        + [F("한국에 있___ 동안에 한국말을 배우겠습니다. (while)", "는", ["은", "을"], "있다 + 는 동안에."), F("친구가 운동하는 ___에 나는 공부합니다. (while)", "동안", ["다음", "전"], "-는 동안에 = while."), F("이 약을 이틀 ___ 복용하세요. (for)", "동안", ["동안에", "전에"], "에 is deleted after a time length."),
           F("여름 방학 ___에 유럽에 갈 거예요. (during)", "동안", ["다음", "전"], "여름 방학 동안에."), F("점심 시간 ___ (during the lunch hour)", "동안", ["다음", "후"], "점심 시간 동안."), F("기다리시는 ___에 이 잡지 좀 보세요. (while)", "동안", ["다음", "전"], "기다리시는 동안에."),
           M("What does 동안 literally mean?", "An interval or a space of time", ["A place", "A person", "A reason"], "동안 = an interval of time."), M("When must 에 be deleted in 동안에?", "After a noun that shows a time length", ["After a verb", "Always", "Never"], "이틀 동안, 한 시간 동안."), M("Which is correct for “for two days”?", "이틀 동안", ["이틀 동안에", "이틀 는 동안", "이틀 동안은에"], "에 is deleted after a time length."),
           M("What does 일주일 동안 mean?", "for a week", ["after a week", "in a week", "a week ago"], "일주일 동안 = for a week."), M("How do you say “while waiting” politely?", "기다리시는 동안에", ["기다리신 동안에", "기다리고 동안에", "기다려서 동안에"], "-(으)시는 동안(에)."),
           read_q("한국에 있는 동안에"), read_q("이틀 동안"), read_q("점심 시간 동안"), read_q("공부하는 동안에"), read_q("약을 복용하는 동안")]
    ),
)

# ================================================================== L7: Grammar B: -자마자
def _jama(verb):
    return stem(verb) + "자마자"


_JAMA_V = [("일어나다", "to get up"), ("도착하다", "to arrive"), ("끝나다", "to end"), ("나오다", "to come out"), ("먹다", "to eat"), ("돌아오다", "to come back"), ("가다", "to go"), ("열다", "to open"), ("보다", "to see"), ("들어가다", "to go in")]
_JAMA_EX = [("아침에 일어나자마자 샤워합니다.", "As soon as I get up in the morning, I take a shower."), ("수업이 끝나자마자 체육관에 갔습니다.", "Right after class (ended), I went to the gym."), ("집에 도착하자마자 비가 왔어요.", "As soon as I arrived at home, it rained."), ("새 핸드폰이 나오자마자 샀어요.", "As soon as the new cell phone came out (on the market), I bought it.")]
_JAMA_CH = [("아침에 일어납니다.", "I get up in the morning. (A, the book’s model)"), ("일어나자마자 아침을 먹습니다.", "As soon as I get up, I eat breakfast. (B)"), ("아침을 먹자마자 학교에 갑니다.", "As soon as I eat breakfast, I go to school. (C)"), ("학교에 가자마자 문을 엽니다.", "As soon as I go to school, I open the door. (D)")]
_JAMA_F5 = [("점심시간 동안에 뭐 해요?", "What do you do during lunchtime? (the book’s model)"), ("점심시간 동안에 밥을 먹어요.", "During lunchtime I eat. (the book’s model)"), ("밥 먹고 뭐 해요?", "What do you do after eating? (the book’s model)"), ("밥 먹자마자 이를 닦아요.", "As soon as I eat, I brush my teeth. (the book’s model)"),
            ("김 일병은 점심시간 동안에 밥을 먹어요. 그리고 밥을 먹자마자 이를 닦아요.", "PFC Kim eats during lunchtime. And as soon as he eats, he brushes his teeth. (the book’s model for reporting)")]
L7 = lesson(
    "Ch 20 · Grammar B: “as soon as” and “right after” with -자마자",
    "일어나자마자 · 도착하자마자 · 수업이 끝나자마자 · 새 핸드폰이 나오자마자",
    requires=[],
    cards=[
        card("Expressing “as soon as” or “right after”",
             "In English, we use phrases like as soon as, right after or immediately after to express an action immediately following another, as in “As soon as I am up, I take a shower” or “I take a shower right after I get up”. In Korean, we use the conjunctive ending -자마자 to express this, as in 일어나자마자 (as soon as I get up) or 샤워하자마자 (right after taking a shower).",
             examples=passage(_JAMA_EX[:2])),
        card("The rule",
             "action verb stem + 자마자.",
             tables=[table(["Condition", "Rule", "Example"], [["After an action verb stem", "add 자마자", "일어나다 → 일어나자마자; 도착하다 → 도착하자마자"]])],
             examples=passage(_JAMA_EX[2:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-자마자"], [[v, m, _jama(v)] for v, m in _JAMA_V], say=[0, 2])]),
        card("Follow-up 3: the chain game, and Follow-up 5: the daily routine",
             "In Follow-up 3 the class sits in a circle; each student repeats the previous student’s activity with -자마자 and adds another action. The book’s model:",
             examples=passage(_JAMA_CH)),
        card("Follow-up 5: -는 동안 and -자마자 together",
             "Partners ask what the other does during the time periods (연휴, 점심시간, 방학, 주말) with ~ 동안 and what he or she does right after, with -자마자. The book’s models:",
             examples=passage(_JAMA_F5)),
        card("Activities left out",
             "Follow-up 3 (a class chain game), Follow-up 4 (listening to three dialogs and writing the two actions of the -자마자 sentence in English) and Follow-up 5 (partner and class work, tables of two actions) are class, audio or partner activities."),
    ],
    exercises=uniq(
        _fk(_JAMA_V, _jama, "“as soon as” (-자마자)", lambda v: [stem(v) + "자", stem(v) + "고마자", stem(v) + "다마자", stem(v) + "자마다"])
        + _tr(_JAMA_EX + _JAMA_CH + _JAMA_F5)
        + [F("아침에 일어나___ 샤워합니다. (as soon as)", "자마자", ["다가", "는 동안"], "-자마자 = as soon as."), F("수업이 끝나___ 체육관에 갔습니다. (right after)", "자마자", ["다가", "는 동안"], "끝나다 + 자마자."), F("집에 도착하___ 비가 왔어요. (as soon as)", "자마자", ["다가", "는 동안"], "도착하다 + 자마자."),
           F("새 핸드폰이 나오자마자 ___. (I bought it)", "샀어요", ["사요", "살 거예요"], "사다 → 샀어요."), F("밥 먹___ 이를 닦아요. (as soon as)", "자마자", ["다가", "는 동안"], "먹다 + 자마자."), F("학교에 가자마자 문을 ___. (I open)", "엽니다", ["엽니까", "열어요"], "열다 → 엽니다."),
           M("What does -자마자 express?", "An action immediately following another", ["Two simultaneous actions", "An interrupted action", "A near miss"], "일어나자마자 = as soon as I get up."), M("Which verb ending follows an action verb stem to mean “as soon as”?", "-자마자", ["-는 동안", "-다가", "-(으)ㄹ 뻔하다"], "stem + 자마자."), M("How do you say “right after class ended”?", "수업이 끝나자마자", ["수업이 끝나는 동안", "수업이 끝나다가", "수업이 끝날 뻔"], "끝나다 + 자마자."),
           read_q("일어나자마자 샤워합니다"), read_q("수업이 끝나자마자"), read_q("도착하자마자 비가 왔어요"), read_q("핸드폰이 나오자마자 샀어요"), read_q("밥 먹자마자 이를 닦아요")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("의사", "어디가 불편하세요?", "Where does it bother you?"),
    ("우진", "어제 아침에 지하철 계단을 내려가다가 넘어질 뻔했어요. 그때 발을 다친 것 같아요.", "Yesterday morning I almost fell while going down the subway stairs. I think I hurt my foot then."),
    ("의사", "발이 부었군요! 많이 아프세요?", "Your foot is swollen! Does it hurt a lot?"),
    ("우진", "네, 너무 아파서 걷기가 힘들어요.", "Yes, it hurts so much that walking is hard."),
    ("의사", "먼저 발목 엑스레이를 찍어 봅시다. 다행히 뼈는 부러지지 않았습니다. 발목을 심하게 삐었습니다.", "First let’s take an x-ray of the ankle. Fortunately the bone is not broken. You sprained your ankle badly. (the book marks a pause, “later”, after the first sentence)"),
    ("우진", "깁스를 해야 합니까?", "Do I have to wear a cast?"),
    ("의사", "네. 한 이 주 정도 하는 것이 좋겠습니다.", "Yes. It would be good to wear it for about two weeks."),
    ("우진", "외출할 때는 어떻게 해야 합니까?", "What should I do when I go out?"),
    ("의사", "목발을 쓰시면 됩니다.", "You can use crutches."),
    ("우진", "통증은 어떻게 해요? 어제는 아파서 잠도 못 잤어요.", "What about the pain? Yesterday it hurt so much that I couldn’t even sleep."),
    ("의사", "진통제를 처방해 드리겠습니다. 삼사 일간 드시면 괜찮아질 겁니다.", "I will prescribe a painkiller. If you take it for three or four days, you will be fine."),
    ("우진", "알겠습니다. 언제 병원에 다시 올까요?", "I understand. When should I come to the hospital again?"),
    ("의사", "이 주 후에 깁스 풀러 오세요.", "Come in two weeks to take the cast off."),
]
_C_WORDS = ["가볍다", "구급차", "앰뷸런스", "깁스", "-다가", "다행히", "떨어지다", "목발", "베다", "부딪치다 / 부딪히다", "부러지다", "붓다", "-(으)ㄹ 뻔하다", "뼈", "삐다", "상처", "심하다", "엑스레이", "외출", "응급실", "잠", "진통제", "처방", "칼", "통증", "풀다", "피"]
_CAP = [("문에 부딪쳐서 머리에 상처가 났어요.", "I bumped into the door and got a wound on my head."), ("나무에서 떨어져서 팔이 부러졌어요.", "I fell from a tree and broke my arm."), ("칼에 베어서 손에서 피가 나요.", "I cut myself with a knife and my hand is bleeding.")]
L8 = lesson(
    "Ch 20 · Topic C: I fell while going down the stairs",
    "계단을 내려가다가 넘어졌어요 · 깁스 · 목발 · 진통제 · 엑스레이 · 응급실 · 상처",
    requires=[],
    cards=[
        card("Topic C: I fell while going down the stairs (계단을 내려가다가 넘어졌어요)",
             "Woojin is seeing a doctor at a clinic for his physical discomfort. (The English is mine; the book gives none. The book writes 한 2주, 3, 4일간 and 2주 후에; they are spelled out here. The book’s title says 넘어졌어요, while in the dialog Woojin says 넘어질 뻔했어요; I keep both as in the book. The book marks the doctor’s next lines as “(later)”.)",
             examples=dlg(_C_DLG)),
        card("Core words and phrases of Topic C",
             "The meanings are the book’s (from the Core Vocabulary of the chapter); optional parts are shortened.",
             tables=[ktable(_rows(_C_WORDS))]),
        card("Injury captions (the book’s pictures)",
             "The book shows three pictures with captions (the pictures are left out):",
             examples=passage(_CAP)),
        card("Activities left out",
             "The SMART Board activities and the partner role-play (Woojin and the doctor) of the Presentation Activity and Follow-up 2 (listening to four conversations between a doctor and a patient and filling in the injury, the cause, the symptoms and the treatment) are computer, partner or audio activities. Follow-up 1 is in the next lesson."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs([w for w in _C_WORDS if not w.startswith("-") and "/" not in w]))
        + _tr(_strip(_C_DLG) + _CAP)
        + [M("Where did Woojin almost fall?", "On the subway stairs", ["On a bus", "In the office", "On the street"], "지하철 계단을 내려가다가 넘어질 뻔했어요."), M("What part of his body does he think he hurt?", "His foot", ["His hand", "His knee", "His back"], "발을 다친 것 같아요."), M("What does the doctor notice?", "The foot is swollen", ["The foot is cut", "The foot is cold", "The foot is dirty"], "발이 부었군요."),
           M("Why is walking hard for Woojin?", "It hurts a lot", ["He is tired", "He has no shoes", "It is raining"], "너무 아파서 걷기가 힘들어요."), M("What does the doctor do first?", "Takes an x-ray of the ankle", ["Gives a shot", "Puts on a cast", "Prescribes medicine"], "발목 엑스레이를 찍어 봅시다."),
           M("What is the result of the x-ray?", "The bone is not broken, but the ankle is badly sprained", ["The bone is broken", "The ankle is cut", "Nothing is wrong"], "뼈는 부러지지 않았습니다. 발목을 심하게 삐었습니다."), M("How long should he wear a cast?", "About two weeks", ["About a month", "About three days", "A year"], "한 이 주 정도."),
           M("What can he use when he goes out?", "Crutches", ["A wheelchair", "A cane", "A bandage"], "목발을 쓰시면 됩니다."), M("What does the doctor prescribe?", "A painkiller", ["A cold medicine", "A digestive pill", "A vitamin"], "진통제를 처방해 드리겠습니다."),
           M("How long should he take the painkiller?", "Three or four days", ["One day", "Two weeks", "A month"], "삼사 일간."), M("When should he come back?", "In two weeks, to take the cast off", ["Tomorrow", "In a month", "Never"], "이 주 후에 깁스 풀러 오세요."),
           M("What happened in “나무에서 떨어져서 팔이 부러졌어요”?", "He fell from a tree and broke his arm", ["He cut his arm with a knife", "He bumped into a door", "He sprained his arm"], "떨어지다 + 부러지다."),
           F("계단을 내려가___ 넘어질 뻔했어요. (while)", "다가", ["자마자", "는 동안"], "-다가 = while; in the middle of."), F("계단에서 넘어질 ___했어요. (almost)", "뻔", ["때", "것"], "-(으)ㄹ 뻔하다 = almost did."), F("발이 ___군요! (is swollen)", "부었", ["부러졌", "삐었"], "붓다 → 부었다."),
           F("다행히 뼈는 ___ 않았습니다. (was not broken)", "부러지지", ["다치지", "붓지"], "부러지다 = to be broken."), F("발목을 심하게 ___. (sprained)", "삐었습니다", ["베었습니다", "부었습니다"], "삐다 = to sprain."), F("___을 쓰시면 됩니다. (crutches)", "목발", ["깁스", "붕대"], "목발 = crutches."),
           read_q("계단을 내려가다가 넘어질 뻔했어요"), read_q("발이 부었군요"), read_q("깁스를 해야 합니까"), read_q("진통제를 처방해 드리겠습니다"), read_q("칼에 베어서 피가 나요")]
    ),
)

# ================================================================== L9: Follow-up 1 text and Activities C
_FU1 = [
    ("안녕하십니까?", "Hello."), ("제가 한 달 전에 농구를 하다가 오른쪽 손목을 다쳤습니다.", "A month ago, while playing basketball, I hurt my right wrist."), ("뼈는 부러지지 않았지만 이 주간 깁스를 해야 했습니다.", "The bone was not broken, but I had to wear a cast for two weeks."),
    ("그런데 깁스를 풀고 이 주가 지났지만 아직도 손목이 아픕니다.", "But two weeks have passed since I took off the cast, and my wrist still hurts."), ("특히 컴퓨터를 할 때 통증이 심합니다.", "Especially when I use the computer, the pain is severe."), ("다시 병원에 가서 치료를 받아야 합니까?", "Should I go to the hospital again and get treatment?"),
]
_HEALTH = [
    ("제가 지난주에 문에 부딪쳐서 무릎을 다쳤어요.", "Last week I bumped into a door and hurt my knee."), ("뼈는 부러지지 않았지만 너무 아파서 걸을 수 없었어요.", "The bone was not broken, but it hurt so much that I couldn’t walk."), ("그런데 다음 날부터 무릎이 붓기 시작했습니다.", "But from the next day my knee began to swell."), ("그래서 동네 병원에 갔습니다.", "So I went to a neighborhood hospital."),
    ("엑스레이는 안 찍었고, 의사선생님께 처방받은 약을 먹었습니다.", "I did not take an x-ray, and I took the medicine prescribed by the doctor."), ("하지만 무릎이 낫지 않고 통증이 계속되어서 걱정입니다.", "But my knee is not getting better and the pain continues, so I am worried."), ("그리고 아직까지 걷는 것이 불편해요.", "And walking is still uncomfortable."),
    ("특히 계단을 올라가고 내려갈 때는 너무 아픕니다.", "Especially when going up and down stairs, it hurts too much."), ("다른 병원에 가서 엑스레이를 찍어봐야 할까요?", "Should I go to another hospital and take an x-ray?"),
]
_HEALTH_A = [("빨리 큰 병원에 가서 엑스레이를 찍어 보는 것이 좋을 것 같습니다.", "It seems good to go quickly to a big hospital and take an x-ray."), ("빨리 나으시기 바랍니다.", "I hope you get well soon.")]
L9 = lesson(
    "Ch 20 · Topic C, Follow-up 1 and Activities: a wrist injury and a health consultation",
    "손목을 다쳤는데 너무 아파요 · 건강상담 · 무릎이 붓기 시작했습니다 · 엑스레이를 찍어 보다",
    requires=[],
    cards=[
        card("Follow-up 1 (Reading): a post on a health website",
             "The text is from a health website on which the writer is soliciting advice about treatment for his injury. The book asks you to extract the essential elements of information (EEIs) and fill in a table in English (how the person was injured, the symptoms, the treatment, the current concern). The title is 손목을 다쳤는데 너무 아파요 (“I hurt my wrist and it hurts so much”; mine); the text is the book’s (the book writes 2주간 and 2주; they are spelled out here); the English is mine.",
             examples=passage(_FU1)),
        card("The table filled in (mine)",
             "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["How was the person injured?", "He hurt his right wrist while playing basketball a month ago"], ["What are the symptoms?", "The wrist still hurts two weeks after the cast came off; the pain is severe when he uses the computer"], ["What treatment did the person get?", "The bone was not broken, but he wore a cast for two weeks"], ["What is the writer’s current concern?", "Whether he should go back to the hospital for treatment"]])]),
        card("Activity 2 (Reading): a health counseling Q&A",
             "The book gives a Q&A posted on the health counseling section of a university hospital’s website (the heading 건강상담, the user name and the date are left out; the hint: if you meet unknown words, focus on the words you know and use your dictionary) and three tasks: fill in a table in English (the injury and its cause, the symptoms, what the patient did after the injury); translate two sentences; and find the patient’s question and the doctor’s answer. The text is the book’s; the English is mine.",
             examples=passage(_HEALTH)),
        card("The doctor’s answer",
             "The answer (the English is mine):",
             examples=passage(_HEALTH_A)),
        card("The tasks done (mine)",
             "The book leaves the answers blank; these are my answers. The two sentences of the translation task are 문에 부딪쳐서 무릎을 다쳤어요 (“I bumped into a door and hurt my knee”) and 다음 날부터 무릎이 붓기 시작했습니다 (“From the next day my knee began to swell”).",
             tables=[table(["Task", "Answer (mine)"], [["Injury and cause", "A knee injury from bumping into a door last week"], ["Symptoms", "Pain, so he could not walk; the knee swelled; the pain continues and walking is still uncomfortable, especially on stairs"], ["What the patient did after the injury", "Went to a neighborhood hospital without an x-ray and took the prescribed medicine"], ["The patient’s question", "Should he go to another hospital and take an x-ray?"], ["The doctor’s answer", "It seems good to go quickly to a big hospital and take an x-ray"]])]),
        card("Activities left out",
             "Activity 3 (listening to conversations in which a patient and a doctor discuss injuries) is an audio activity; Activity 4 (a role-play with situation cards in which you describe your injury or illness to a friend and get advice, in pairs) is a partner activity. Activity 1 (listening to conversations and matching nine pictures with audio clips) is an audio and picture activity."),
    ],
    exercises=uniq(
        _tr(_FU1 + _HEALTH + _HEALTH_A)
        + [M("How was the writer injured?", "While playing basketball", ["While skiing", "In a car accident", "At work"], "농구를 하다가 오른쪽 손목을 다쳤습니다."), M("Which wrist did he hurt?", "The right wrist", ["The left wrist", "Both wrists", "His ankle"], "오른쪽 손목."), M("How long did he wear a cast?", "Two weeks", ["A month", "Three days", "A year"], "이 주간 깁스."),
           M("When is the pain severe?", "When he uses the computer", ["When he sleeps", "When he walks", "When he eats"], "컴퓨터를 할 때 통증이 심합니다."), M("What is the writer’s question?", "Whether to go back to the hospital for treatment", ["Whether to buy a cast", "Whether to play basketball", "Whether to see a pharmacist"], "다시 병원에 가서 치료를 받아야 합니까?"),
           M("How did sunshine73 hurt the knee?", "By bumping into a door", ["By falling from a tree", "By skiing", "By running"], "문에 부딪쳐서 무릎을 다쳤어요."), M("What happened to the knee the next day?", "It began to swell", ["It healed", "It was cut", "It was cold"], "다음 날부터 무릎이 붓기 시작했습니다."),
           M("What did the patient not do at the neighborhood hospital?", "Take an x-ray", ["Take medicine", "See a doctor", "Go home"], "엑스레이는 안 찍었고."), M("When does it hurt especially?", "Going up and down the stairs", ["Sitting", "Sleeping", "Eating"], "계단을 올라가고 내려갈 때는 너무 아픕니다."), M("What does the doctor recommend?", "Going quickly to a big hospital for an x-ray", ["Resting at home", "Taking more medicine", "Doing exercises"], "빨리 큰 병원에 가서 엑스레이를 찍어 보는 것이 좋을 것 같습니다."),
           F("농구를 하___ 오른쪽 손목을 다쳤습니다. (while)", "다가", ["자마자", "는 동안"], "농구를 하다가."), F("뼈는 ___ 않았지만 깁스를 해야 했습니다. (was not broken)", "부러지지", ["다치지", "붓지"], "부러지다."), F("무릎이 ___ 시작했습니다. (began to swell)", "붓기", ["삐기", "베기"], "붓기 시작하다 = to begin to swell."),
           read_q("오른쪽 손목을 다쳤습니다"), read_q("깁스를 풀고"), read_q("통증이 심합니다"), read_q("무릎이 붓기 시작했습니다"), read_q("엑스레이를 찍어 보는 것이 좋습니다")]
    ),
)

# ================================================================== L10: Grammar C: -다(가)
def _daga(verb):
    return stem(verb) + "다가"


_DAGA_V = [("먹다", "to eat"), ("타다", "to ride"), ("가다", "to go"), ("운전하다", "to drive"), ("읽다", "to read"), ("걷다", "to walk"), ("공부하다", "to study"), ("등산하다", "to hike"), ("달리다", "to run"), ("수영하다", "to swim")]
_DAGA_EX = [("저녁을 먹다가 전화를 받았어요.", "While eating dinner, I got a phone call."), ("스키를 타다가 다쳤습니다.", "While skiing, I got hurt."), ("가다가 사거리에서 왼쪽으로 돌았어요.", "While going (down the road), I turned left at the intersection."),
            ("음악을 듣다가 잠이 들었어요.", "While listening to music, I fell asleep."), ("운전을 하다가 사고를 냈어요.", "While driving, I had an accident."), ("학교에 가다가 친구를 만났어요.", "On the way to school, I bumped into a friend."), ("학교에 갔다가 친구를 만났어요.", "I went to school, and (there) I ran into a friend.")]
_DAGA_F2 = [("빌려 준 책 다 읽었어요?", "Did you finish reading the book I lent you? (A)"), ("아니요. 읽다가 잤어요.", "No. I fell asleep while reading. (B, the book’s example)"), ("밥 다 먹었어요?", "Did you finish eating? (A)"), ("아니요. 먹다가 전화 받았어요. 그래서 다 못 먹었어요.", "No. I got a phone call while eating. So I couldn’t finish. (B; the blank is mine)"),
            ("팔이 왜 그래요?", "What’s wrong with your arm? (A)"), ("어제 운전하다가 사고가 났어요.", "Yesterday I had an accident while driving. (B; the blank is mine, from the pictures of two cars in a crash)"), ("발을 다쳤어요?", "Did you hurt your foot? (A)"), ("네, 자전거를 타다가 발을 삐었어요.", "Yes, I sprained my foot while riding a bicycle. (B; the blank is mine, from the pictures of a bicycle)")]
_DAGA_F1 = [("수영하다가 감기에 걸렸어요.", "I caught a cold while swimming. (the book’s model)")]
L10 = lesson(
    "Ch 20 · Grammar C: “switching gears” with -다(가)",
    "저녁을 먹다가 전화를 받았어요 · 스키를 타다가 다쳤습니다 · 갔다가 · 읽다가 잤어요",
    requires=[],
    cards=[
        card("The conjunctive ending -다(가) expressing “switching gears” or changing direction",
             "The conjunctive ending -다(가), which is usually translated as while or in the middle of, is used to express “switching gears” or “changing direction”. It is used to express the idea that the first action in progress switches to the second action without the first being completed.\n\n"
             "The first sentence implies the speaker was eating, which he stopped doing to answer the phone call. The second sentence implies the speaker was skiing and got hurt in the process. The third sentence implies the speaker was going down the road before he came to the intersection, where he turned left.",
             examples=passage(_DAGA_EX[:3])),
        card("The rule",
             "verb stem + 다(가).",
             tables=[table(["Condition", "Rule", "Example"], [["When a verb is an action verb", "add 다(가)", "샤워를 하다 → 샤워를 하다(가); 비가 오다 → 비가 오다(가)"]])],
             examples=passage(_DAGA_EX[3:6])),
        card("Note: 았/었 before -다가",
             "There are a few occasions when 았/었 is inserted before the conjunctive ending -다가 (e.g. 갔다가 or 왔다가). In these cases the conjunctive ending indicates that the second action takes place after the first action has been completed. Compare 학교에 가다(가) 친구를 만났어요 (On the way to school, I ran into a friend) and 학교에 갔다(가) 친구를 만났어요 (I went to school, and (there) I ran into a friend).",
             examples=passage(_DAGA_EX[5:])),
        card("Forms (mine)",
             "The forms are made by the book’s rule.",
             tables=[table(["Verb", "Meaning", "-다가", "-았/었다가"], [[v, m, _daga(v), (past(v) + "다가") if v != "걷다" else "걸었다가"] for v, m in _DAGA_V], say=[0, 2, 3])]),
        card("Follow-up 1 and 2: completing the sentences",
             "In Follow-up 1 partners pick a verb from List A (공부하다, 영화를 보다, 걷다, 등산하다, 달리다) and complete the sentence with a verb of List B (자다, 스키 타다, 문을 열다, 요리하다, 운전하다) or any other verb; the book’s model is 수영하다가 감기에 걸렸어요. In Follow-up 2 the left picture shows an action in progress and the right one an unexpected event, and you complete the dialogs with -다가. The book does the first (읽다가); the others were read from the pictures, and the blanks are my answers.",
             examples=passage(_DAGA_F1 + _DAGA_F2)),
        card("Activities left out",
             "Follow-up 1 (partner verb lists) and Follow-up 2 b (listening to three dialogs about what happened to a man while he was engaged in an activity, and filling in a table in English) are partner and audio activities. The book’s pictures are left out."),
    ],
    exercises=uniq(
        _fk(_DAGA_V, _daga, "“while” (-다가)", lambda v: [stem(v) + "다", stem(v) + "고가", stem(v) + "다고", stem(v) + "자가"])
        + _tr(_DAGA_EX + _DAGA_F1 + _DAGA_F2)
        + [F("저녁을 먹___ 전화를 받았어요. (while eating)", "다가", ["자마자", "는 동안"], "-다가 = while; in the middle of."), F("스키를 타___ 다쳤습니다. (while skiing)", "다가", ["자마자", "는 동안"], "타다 + 다가."), F("운전을 하다가 사고를 ___. (I caused an accident)", "냈어요", ["났어요", "갔어요"], "사고를 내다 = to cause an accident."),
           F("학교에 ___ 친구를 만났어요. (went and then, after completing)", "갔다가", ["가다가", "가자마자"], "았/었 + 다가 = after completing the first action."), F("학교에 ___ 친구를 만났어요. (on the way, still in progress)", "가다가", ["갔다가", "가자마자"], "가다가 = on the way."), F("읽다가 ___. (I fell asleep)", "잤어요", ["자요", "잘 거예요"], "자다 → 잤어요."),
           M("What does -다가 express?", "The first action in progress switches to a second action", ["Two simultaneous actions", "An action right after another", "A near miss"], "“Switching gears”."), M("What does 갔다가 mean compared with 가다가?", "The first action is completed before the second", ["The first action is not completed", "The two actions are the same", "The second action never happens"], "았/었 + 다가."),
           M("Which sentence means “I fell asleep while listening to music”?", "음악을 듣다가 잠이 들었어요.", ["음악을 듣자마자 잠이 들었어요.", "음악을 듣는 동안 잠이 들었어요.", "음악을 들을 뻔했어요."], "듣다 + 다가."),
           read_q("저녁을 먹다가 전화를 받았어요"), read_q("스키를 타다가 다쳤습니다"), read_q("학교에 가다가 친구를 만났어요"), read_q("운전하다가 사고가 났어요"), read_q("자전거를 타다가 발을 삐었어요")]
    ),
)

# ================================================================== L11: Grammar D: -(으)ㄹ 뻔하다
def _ppeon(phrase):
    """verb phrase -> -(으)ㄹ 뻔했어요: 넘어지다 -> 넘어질 뻔했어요; 컴퓨터를 사다 -> 컴퓨터를 살 뻔했어요"""
    parts = phrase.split(" ")
    return " ".join(parts[:-1] + [attr(parts[-1])[2] + " 뻔했어요"])


_PP_V = [("넘어지다", "to fall (over)"), ("지다", "to lose"), ("잃다", "to lose; to miss"), ("먹다", "to eat"), ("늦다", "to be late"), ("다치다", "to hurt oneself"), ("울다", "to cry; to weep"), ("부딪치다", "to hit; to bump into"), ("떨어지다", "to fall"), ("토하다", "to vomit")]
_PP_EX = [("앞차와 부딪칠 뻔했어요.", "I almost hit the car in front of me."), ("아침에 늦게 일어나서 학교에 늦을 뻔했어.", "I got up late, so I was almost late for school."), ("어제 교통사고가 나서 크게 다칠 뻔했어요.", "A car accident occurred yesterday, and I was almost seriously hurt."), ("영화를 보다가 울 뻔했어요.", "While watching a movie, I almost wept. (the book’s translation says TV)"),
          ("운동하다가 발을 삘 뻔했어요.", "I almost sprained my foot while exercising. (the book’s title of Follow-up 6)"), ("김 일병은 초등학교 때 록키 산을 등산하다가 높은 곳에서 떨어질 뻔했어요.", "When PFC Kim was in elementary school, he almost fell from a high place while hiking in the Rocky Mountains. (the book’s model)"), ("다칠 뻔했어요.", "I almost got hurt. (the book’s model)")]
_PP_A = [("컴퓨터를 사다", "to buy a computer"), ("숙제를 안 하다", "to not do homework"), ("한국말을 하다", "to speak Korean"), ("나무에서 떨어지다", "to fall from a tree"), ("이라크에 가다", "to go to Iraq")]
_PP_B = [("교통사고가 나다", "to have a car accident"), ("토하다", "to vomit"), ("문에 부딪치다", "to bump into the door"), ("넘어지다", "to fall (over)"), ("교실에서 영어를 하다", "to speak English in the classroom")]
L11 = lesson(
    "Ch 20 · Grammar D: near misses with -(으)ㄹ 뻔하다",
    "넘어질 뻔했어요 · 늦을 뻔했어 · 크게 다칠 뻔했어요 · 앞차와 부딪칠 뻔했어요",
    requires=[],
    cards=[
        card("Expressing near misses or close calls",
             "In English, we often use adverbs such as nearly, almost and barely to indicate a close call, as in “The car almost ran over my foot” or “I almost failed the test”. In Korean, we convey this meaning by using -(으)ㄹ 뻔하다, as in 앞차와 부딪칠 뻔했어요 (I almost hit the car in front of me).",
             examples=passage(_PP_EX[:1])),
        card("The rule",
             "action verb stem + (으)ㄹ 뻔하다.",
             tables=[table(["Condition", "Rule", "Example"], [["When an action verb stem ends in a vowel", "add ㄹ 뻔하다", "넘어지다 → 넘어질 뻔하다; 경기에 지다 → 경기에 질 뻔하다"], ["When an action verb stem ends in a consonant", "add 을 뻔하다", "잃다 → 잃을 뻔하다; 먹다 → 먹을 뻔하다"]])],
             examples=passage(_PP_EX[1:4])),
        card("Forms (mine)",
             "The forms are made by the book’s rule (verbs with an ㄹ-ending stem keep a single ㄹ: 울다 → 울 뻔하다).",
             tables=[table(["Verb", "Meaning", "-(으)ㄹ 뻔했어요"], [[v, m, _ppeon(v)] for v, m in _PP_V], say=[0, 2])]),
        card("Follow-up 3: the verb lists",
             "Student 1 reads each verb of List A and Student 2 conjugates it with -(으)ㄹ 뻔하다; then Student 2 reads List B and Student 1 conjugates (the book’s model: 다치다 → 다칠 뻔했어요). The book’s lists with my conjugations:",
             tables=[table(["List A", "Meaning", "-(으)ㄹ 뻔했어요"], [[p, m, _ppeon(p)] for p, m in _PP_A], say=[0, 2]), table(["List B", "Meaning", "-(으)ㄹ 뻔했어요"], [[p, m, _ppeon(p)] for p, m in _PP_B], say=[0, 2])]),
        card("Follow-up 6: close calls",
             "You think about at least two close calls you have had while engaged in an activity, share them with three classmates and present the most interesting story to the class, using -다(가) and -(으)ㄹ 뻔 하다. The book’s title and model (the English is mine):",
             examples=passage(_PP_EX[4:])),
        card("Activities left out",
             "Follow-up 4 (listening to four dialogs about what nearly happened), Follow-up 5 (a SMART Board activity) and Follow-up 6 (sharing close calls with classmates and presenting a story) are audio, computer and class activities."),
    ],
    exercises=uniq(
        _fk(_PP_V, lambda v: attr(v)[2] + " 뻔", "-(으)ㄹ 뻔 (almost)", lambda v: [stem(v) + " 뻔", stem(v) + "는 뻔", stem(v) + "은 뻔", attr(v)[1] + " 뻔"])
        + [M(f"How do you say “I almost {m.replace('to ', '', 1)}” (the phrase {p})?", _ppeon(p), [" ".join(p.split(" ")[:-1] + [attr(p.split(" ")[-1])[1] + " 뻔했어요"]), " ".join(p.split(" ")[:-1] + [stem(p.split(" ")[-1]) + "고 싶어요"]), " ".join(p.split(" ")[:-1] + [stem(p.split(" ")[-1]) + "는 중이에요"])], f"{p} → {_ppeon(p)}.") for p, m in (_PP_A + _PP_B)[:8]]
        + _tr(_PP_EX)
        + [F("앞차와 부딪칠 ___했어요. (almost)", "뻔", ["때", "것"], "-(으)ㄹ 뻔하다 = almost did."), F("학교에 늦___ 뻔했어. (almost late)", "을", ["ㄹ", "는"], "늦다 ends in a consonant: 늦을."), F("크게 다___ 뻔했어요. (almost hurt)", "칠", ["친", "치는"], "다치다 ends in a vowel: 다칠."),
           F("영화를 보다가 울 ___했어요. (almost wept)", "뻔", ["때", "것"], "울다 → 울 뻔하다."), F("나무에서 떨어___ 뻔했어요. (almost fell)", "질", ["진", "지는"], "떨어지다 → 떨어질."), F("경기에 ___ 뻔했어요. (almost lost)", "질", ["진", "지는"], "지다 → 질 뻔하다."),
           M("What does -(으)ㄹ 뻔하다 express?", "A near miss or close call", ["A simultaneous action", "A past experience", "A wish"], "앞차와 부딪칠 뻔했어요."), M("What is added to a verb stem that ends in a vowel?", "ㄹ 뻔하다", ["을 뻔하다", "는 뻔하다", "ㄴ 뻔하다"], "넘어지다 → 넘어질 뻔하다."), M("What is added to a verb stem that ends in a consonant?", "을 뻔하다", ["ㄹ 뻔하다", "는 뻔하다", "ㄴ 뻔하다"], "먹다 → 먹을 뻔하다."),
           read_q("넘어질 뻔했어요"), read_q("앞차와 부딪칠 뻔했어요"), read_q("학교에 늦을 뻔했어"), read_q("크게 다칠 뻔했어요"), read_q("발을 삘 뻔했어요")]
    ),
)

# ================================================================== L12: Core vocabulary and self-evaluation
_CV_SECS = [("Parts of the body", _CV_BODY), ("At a pharmacy", _CV_PHARM), ("Symptoms of illness", _CV_SYM), ("Injuries and treatment", _CV_INJ), ("Loan words", _CV_LOAN), ("Other words", _CV_OTH), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [r for _, rows in _CV_SECS[:-1] for r in rows if not r[0].startswith(("~", "-")) and "/" not in r[0]]
L12 = lesson(
    "Ch 20 · Core vocabulary and self-evaluation",
    "주요 단어 · 몸 · 약국 · 증상 · 부상과 치료 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning.\n\n"
             "The example sentences with digits are respelled in Hangul (30분 → 삼십 분). The book’s 부딪치다/부딪히다 and ~(에) 걸리다 are shown with the forms written out; the book’s 며칠 has two example sentences (both kept, joined by a slash). The book’s related words (the synonyms, antonyms and related words in the last column) are left out; the book’s Additional Vocabulary section is blank. The book’s Glossary at the end of the unit (the word index for Chapters 17 to 20) repeats these words."),
    ] + [card(name, "", tables=[vt([(_show(r[0]), r[1], r[2]) for r in rows])]) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: describe a person’s physical appearance using the names for parts of the body; describe physical discomfort and the symptoms of common illnesses; ask for basic services at a drug store; describe the causes and symptoms of common injuries; and ask for basic medical services at a doctor’s office and hospital.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary; the conjunctive ending -는 동안(에) (while; during); the conjunctive ending -자마자 (as soon as; right after); the conjunctive ending -다가 (while; in the middle of); -(으)ㄹ 뻔하다, which is used to express near misses or close calls; and the Sino-Korean syllable 약 (藥)."),
    ],
    exercises=uniq(
        vocab_exercises([(_show(r[0]), _en(r[0])) for r in _CV_PLAIN])
        + [M("What does -는 동안(에) mean?", "while; during", ["as soon as", "almost", "in the middle of"], "한국에 있는 동안에."), M("What does -자마자 mean?", "as soon as; right after", ["while", "almost", "because"], "집에 돌아오자마자 샤워를 합니다."), M("What does -다가 mean?", "while (doing something); in the middle of", ["as soon as", "almost", "after"], "농구하다가 넘어졌어요."),
           M("What does -(으)ㄹ 뻔하다 mean?", "almost (did something); nearly (did something)", ["as soon as", "while", "must"], "앞 차와 부딪칠 뻔했어요."), M("What does the Sino-Korean syllable 약 (藥) mean?", "medicine", ["a farm", "a person", "victory"], "약국, 약사, 감기약, 농약."),
           M("What is “an ankle”?", "발목", ["손목", "무릎", "허리"], "발목 = an ankle; “foot neck”."), M("What is “a wrist”?", "손목", ["발목", "무릎", "어깨"], "손목 = a wrist; “hand neck”."), M("What is “a fever reducer”?", "해열제", ["진통제", "소화제", "감기약"], "해열제 = fever reducer."),
           M("What is “a painkiller”?", "진통제", ["해열제", "소화제", "감기약"], "진통제 = a painkiller."), M("What is “crutches”?", "목발", ["깁스", "붕대", "칼"], "목발 = crutches."), M("What is “to sprain”?", "삐다", ["베다", "붓다", "부러지다"], "삐다 = to sprain; to twist.")]
        + [read_q("주요 단어"), read_q("우리 몸과 건강"), read_q("응급실"), read_q("엑스레이"), read_q("앰뷸런스")]
    ),
)

UNIT = unit("Semester 1 · Unit 5 · Chapter 20: Body and Health (우리 몸과 건강)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
