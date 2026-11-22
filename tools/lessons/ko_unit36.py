"""Unit 36: KBC Semester 2, Unit 8, Chapter 29 - Common Ailments and Symptoms (병과 증상).
Original lessons; the scope follows the DLIFLC Korean Basic Course, Semester 2, Unit 8, Student's Edition (Validation Edition).
Audio, video clips, pictures, newspaper ads and notes that are images, SMART Board activities, games, role-plays, partner and
class activities are left out.
The book gives no English for its dialogs and texts and leaves the answers to its exercises blank: every translation of a
dialog or text sentence and every answer key is mine; the vocabulary meanings and the notes are the book's."""
import ko_rom as _K
from ko_kbc import *
from ko_kbc import _base_ao
from ko_unit21 import _kn, _won
from ko_unit24 import _clean, _tr, _strip, _show, _kit, passage, dlg
from ko_unit25 import _fk

# ---- the core vocabulary of Chapter 29 (meanings and examples are the book's; digits and Latin letters respelled)
_CV_A = [
    ("가렵다", "to be itchy", "다친 곳이 가려워서 잠을 잘 수 없었어요."),
    ("고생", "(苦生) hardship; suffering; toil; to suffer hardship; to suffer; to work hard (~하다)", "이가 아파서 먹지도 못하고 고생했어요."),
    ("구역질", "(嘔逆) nausea; to feel nauseated (~[이] 나다)", "어제 술을 너무 많이 마셔서 구역질이 나요."),
    ("긁다", "to scratch; to scrape", "가려운 곳을 너무 긁어서 피가 났어요."),
    ("넘다", "to exceed; to go over; to be more than", "송 선생님은 예순이 훨씬 넘으셨어요."),
    ("독감", "(毒感) influenza; the flu; “severe cold”", "독감이 유행할 때에는 사람이 많은 곳에 가지 마세요."),
    ("두통", "(頭痛) a headache", "두통에는 어떤 약이 좋아요?"),
    ("목이 쉬다", "to get hoarse; to lose one’s voice", "노래 연습을 많이 해서 목이 쉬었어요."),
    ("몸살", "a body ache (from fatigue or overwork); to ache all over (from fatigue or overwork) (~[이] 나다)", "밤새도록 일을 해서 몸살이 났어요."),
    ("바르다", "to apply", "상처가 난 곳에 연고를 발랐어요."),
    ("복통", "(腹痛) a stomachache", "어제 저녁을 먹은 후부터 복통이 심해요."),
    ("소리", "a sound", "큰 소리로 친구를 불렀어요."),
    ("식욕", "(食慾) an appetite; “food desire”", "감기에 걸리면 식욕이 없어요."),
    ("알레르기 / 알러지", "allergy", "김 선생님은 고양이 알레르기가 있습니다."),
    ("어지럽다", "to be dizzy", "며칠 동안 밥을 못 먹어서 어지러워요."),
    ("연고", "(軟膏) an ointment", "이 연고를 하루에 세 번씩 바르세요."),
    ("이 / 이빨", "a tooth (이빨 is the lower-register word)", "이가 아파서 음식을 못 먹겠어요."),
    ("임신", "(姙娠) pregnancy; to become pregnant (~하다)", "임신을 하면 약을 조심해서 먹어야 합니다."),
    ("참다", "to bear; to endure; to be patient", "잠이 오는 것을 참고 행군을 했어요."),
    ("치통", "(齒痛) a toothache", "치통 때문에 너무 고생했어요."),
]
_CV_B = [
    ("검사", "(檢査) examination; inspection; checkup; to examine / to test / to inspect (~하다/받다)", "어제 병원에 가서 여러 가지 검사를 받았습니다."),
    ("결과", "(結果) result; outcome; consequence", "검사 결과는 다음 주에 알 수 있습니다."),
    ("내과", "(內科) internal medicine; “in(side) department”", "감기 증상이 있으면 먼저 내과에 가 보세요."),
    ("물리치료", "(物理治療) physical therapy", "교통 사고를 당한 후 일주일에 한 번씩 물리치료를 받고 있습니다."),
    ("산부인과", "(産婦人科) obstetrics and gynecology; “birth women department”", "간호사의 실수로 산부인과에서 아기가 바뀌었어요."),
    ("소아과", "(小兒科) pediatrics; “small child department”", "봄에는 소아과를 찾는 어린이 환자가 늘어납니다."),
    ("수술", "(手術) a surgery; to perform a surgical operation for / to receive a surgical operation for (~하다/받다)", "성형수술을 받으러 외국 사람이 한국으로 많이 옵니다."),
    ("안과", "(眼科) ophthalmology; “eye department”", "안과 전문의가 눈의 건강에 대해서 설명합니다."),
    ("외과", "(外科) the department of surgery; “outside department”", "다리가 부러져서 외과에서 치료를 받았어요."),
    ("우선", "(于先) first (of all); above all; for now; for the time being", "우선 밥을 먹고 일을 합시다."),
    ("이비인후과", "(耳鼻咽喉科) ear, nose, and throat (ENT); otolaryngology", "알레르기 때문에 콧물이 많이 나서 이비인후과에서 치료를 받고 있어요."),
    ("이상", "(異常) disorder; abnormality; “different from the usual” (있다/없다)", "몸에 이상을 느끼면 의사에게 가 보세요."),
    ("입원", "(入院) hospitalization; “entering an institute”; to be hospitalized (~하다)", "교통사고를 당한 환자들이 근처 병원에 입원해서 치료를 받고 있습니다."),
    ("진료", "(診療) medical examination and treatment; to examine and treat / to get treatment (~하다/받다)", "저희 병원은 토요일에는 진료를 안 합니다."),
    ("진찰", "(診察) medical examination; to examine / to get a medical exam (~하다/받다)", "의사가 환자를 진찰하는 데 걸리는 시간은 보통 오 분 정도입니다."),
    ("치과", "(齒科) dentistry; “tooth department”", "육 개월에 한 번씩 꼭 치과에 가서 스케일링을 하세요."),
    ("치료", "(治療) treatment; care; cure; to treat (an injury) / to get treatment (~하다/받다)", "한 달에 한 번씩 오셔서 정기적으로 치료를 받으세요."),
    ("퇴원", "(退院) discharge from the hospital; “leaving an institute”; to be discharged from the hospital (~하다)", "최 선생님은 일주일 동안 병원에 계시다 어제 퇴원했습니다."),
    ("피부과", "(皮膚科) dermatology; “skin department”", "온몸이 가려워서 피부과에 갔다 왔어요."),
    ("환자", "(患者) a patient", "보험이 없는 환자들은 진료비를 현금으로 내야 합니다."),
]
_CV_C = [
    ("간", "(肝) a liver", "간이 안 좋습니다. 술을 끊으세요."),
    ("검진", "(檢診) a medical checkup; to give a medical examination / to receive a medical examination (~하다/받다)", "검진 열 시간 전에는 아무 것도 드시면 안 됩니다."),
    ("대변", "(大便) stool; feces; “big excrement”; to have a bowel movement; “see big excrement” (~보다)", "건강한 사람은 보통 하루에 한 번 대변을 봅니다."),
    ("살이 찌다", "to put on weight; “the flesh fattens”", "살이 찌면 여러 가지 병에 걸리기 쉽습니다."),
    ("맥박", "(脈搏) pulsation; pulse", "운동할 때에는 맥박수가 증가합니다."),
    ("살이 빠지다", "to lose weight; “the flesh is lost”", "걷기만 해도 살이 빠져요?"),
    ("소변", "(小便) urine; “small excrement”; to urinate; “see small excrement” (~보다)", "소변 검사로 여러 병을 알아낼 수 있어요."),
    ("수치", "(數値) numerical value; numerical figure", "콜레스테롤 수치가 높으면 음식을 조심해서 먹어야 합니다."),
    ("스트레스", "stress", "스트레스를 운동으로 푸는 사람들이 많습니다."),
    ("신장", "(身長) height; “body length”", "요즘 아이들의 신장이 커지고 있어요."),
    ("재다", "to measure", "제 친구는 언제나 운동 후에 몸무게를 잽니다."),
    ("정상", "(正常) normality; to be normal (~이다)", "혈압약 복용 후 혈압이 정상이 되었어요."),
    ("체중 / 몸무게", "(體重) body weight", "요즘 살이 쪄서 체중이 많이 늘었어요. 키는 백육십이 센티미터이고, 몸무게는 사십팔 킬로그램입니다."),
    ("체온", "(體溫) body temperature", "사람의 정상 체온은 삼십육 점 오 도입니다."),
    ("측정", "(測定) measurement; to measure (~하다)", "혈압 환자들은 혈압 측정을 자주 하는 것이 좋습니다."),
    ("콜레스테롤", "cholesterol", "콩으로 만든 음식에는 콜레스테롤이 없습니다."),
    ("혈압", "(血壓) blood pressure", "화를 내면 혈압이 올라갑니다. 화내지 말고 웃으세요."),
    ("혈액", "(血液) blood; “blood fluid”", "운동선수들은 시합 전에 혈액검사를 받습니다."),
]
_CV_GR = [
    ("-도록 하다", "to make sure (see the grammar)", "하루에 세 번 이 약을 먹도록 하세요."),
    ("-(으)ㄴ/는 김에", "because; since; as (see the grammar)", "도서관에 간 김에 책도 빌렸어요."),
    ("-(으)ㄴ 지 ~(이/가) 되다", "It has been ... since ... (see the grammar)", "한국말을 공부한 지 칠 개월이 되었어요."),
    ("ㅅ 불규칙 동사", "ㅅ irregular verbs (see the grammar)", "감기가 다 나았어요. 발이 많이 부었어요. 줄을 그으세요. 커피를 저으세요. 집을 지었어요."),
]
_CV_SINO = [("병원", "(病院) hospital; “illness house”", "병명, 피부병, 병실, 학원, 입원, 퇴원"), ("통증", "(痛症) pain; “pain symptom”", "치통, 두통, 진통제, 증상, 불면증, 증후군"), ("혈압", "(血壓) blood pressure", "혈액, 수혈, 혈액형, 고혈압, 저혈압, 압력")]
_ALL = {r[0]: r for r in _CV_A + _CV_B + _CV_C + _CV_GR + _CV_SINO}
_ALL["혈압 (Sino)"] = _CV_SINO[2]
_EXTRA = {"알레르기 / 알러지": "allergy", "이 / 이빨": "a tooth", "체중 / 몸무게": "body weight", "목이 쉬다": "to get hoarse; to lose one’s voice", "-도록 하다": "to make sure", "-(으)ㄴ/는 김에": "because; since; as", "-(으)ㄴ 지 ~(이/가) 되다": "It has been ... since ...", "ㅅ 불규칙 동사": "ㅅ irregular verbs",
          "고생": "hardship; suffering", "구역질": "nausea", "몸살": "a body ache (from fatigue or overwork)", "임신": "pregnancy", "검사": "examination; inspection; checkup", "수술": "a surgery", "이상": "disorder; abnormality", "입원": "hospitalization", "진료": "medical examination and treatment", "진찰": "medical examination", "치료": "treatment; care; cure", "퇴원": "discharge from the hospital", "검진": "a medical checkup", "대변": "stool; feces", "소변": "urine", "정상": "normality", "측정": "measurement",
          "병원": "hospital", "통증": "pain; “pain symptom”", "병실": "a sickroom; an infirmary", "병석": "a sickbed; “sickness place”", "병사": "a death from sickness", "학원": "an educational institute; an academy; “learning house”", "양로원": "a nursing home", "법원": "a courthouse; “law house”", "상원": "the Upper House; the Senate", "하원": "the Lower House; the House of Representatives", "원장": "the director (of a hospital); “hospital chief”",
          "신경통": "neuralgia; “nerve pain”", "불면증": "insomnia; “no sleeping symptom”", "우울증": "the blues; mental depression; “melancholy symptom”", "증상": "symptoms; the condition (of a patient); “symptom and condition”", "혈관": "a blood vessel; a vein; “blood tube”", "혈색": "a complexion; “blood color”", "수혈": "blood transfusion", "고혈압": "hypertension; high blood pressure", "수압": "hydraulic pressure; “water pressure”", "압력": "pressure; “pressing power”", "고압": "high pressure; high tension; high voltage", "중압감": "a feeling of oppression; “heavy pressing feeling”", "저혈압": "low blood pressure", "혈액형": "blood type"}
_en, _pairs, _rows = _kit(_ALL, _EXTRA)
_PLAIN = lambda ws: [w for w in ws if not any(c in w for c in "~(-/ㅅ") and " " not in w]

_SPEC = [("내과", "internal medicine"), ("외과", "the department of surgery"), ("소아과", "pediatrics"), ("산부인과", "obstetrics and gynecology"), ("안과", "ophthalmology"), ("이비인후과", "ear, nose, and throat (ENT); otolaryngology"), ("치과", "dentistry"), ("피부과", "dermatology")]
_BYUNG = [("병실", "a sickroom; an infirmary"), ("병석", "a sickbed; “sickness place”"), ("병사", "a death from sickness"), ("학원", "an educational institute; an academy; “learning house”"), ("양로원", "a nursing home"), ("법원", "a courthouse; “law house”"), ("상원", "the Upper House; the Senate"), ("하원", "the Lower House; the House of Representatives"), ("입원", "admission into a hospital; hospitalization"), ("퇴원", "leaving the hospital; discharge from the hospital"), ("원장", "the director (of a hospital); “hospital chief”")]
_TONG = [("두통", "a headache"), ("치통", "a toothache"), ("복통", "a stomachache"), ("신경통", "neuralgia; “nerve pain”"), ("불면증", "insomnia; “no sleeping symptom”"), ("우울증", "the blues; mental depression; “melancholy symptom”"), ("증상", "symptoms; the condition (of a patient); “symptom and condition”")]
_HYUL = [("혈관", "a blood vessel; a vein; “blood tube”"), ("혈색", "a complexion; “blood color”"), ("혈액", "blood; “blood fluid”"), ("수혈", "blood transfusion"), ("고혈압", "hypertension; high blood pressure"), ("수압", "hydraulic pressure; “water pressure”"), ("압력", "pressure; “pressing power”"), ("고압", "high pressure; high tension; high voltage"), ("중압감", "a feeling of oppression; “heavy pressing feeling”")]

# ================================================================== L1: objectives, specialties, Sino-Korean
L1 = lesson(
    "Ch 29 · What the chapter teaches, medical specialties, and 병 (病) 원 (院) 통 (痛) 증 (症) 혈 (血) 압 (壓)",
    "병과 증상 · 내과 · 외과 · 소아과 · 산부인과 · 안과 · 이비인후과 · 치과 · 피부과 · 병원 · 통증 · 혈압",
    requires=[],
    cards=[
        card("What Chapter 29 teaches (병과 증상)",
             "Unit 8 is 건강, “Health”. Chapter 29, “Common Ailments and Symptoms”, has a vocabulary builder, three topic presentations with grammar in focus, activities, a self-evaluation and the core vocabulary.\n\n"
             "When you finish the chapter you will be able to: identify and describe general health conditions, common ailments, and symptoms; identify and talk about basic medical and clinical specialties; and ask about common ailments and provide treatment suggestions.\n\n"
             "You will become familiar with: the new words and phrases in the Core Vocabulary section; ㅅ irregular verbs; –도록 하다 (to make sure …; to see to it that …); –(으)ㄴ 지 ~(이/가) 되다 (It has been … since …); the conjunctive ending –(으)ㄴ/는 김에 (because; since; as); and the Sino-Korean syllables within 병원 (病院), 통증 (痛症), and 혈압 (血壓)."),
        card("Medical specialties", "The book’s list of medical specialties (the meanings are the book’s, from the Core Vocabulary). A doctor of a specialty is 과 + 의사, as in 치과 의사 (a dentist).", tables=[ktable(_SPEC)]),
        card("Sino-Korean in use: 병원 (病院)",
             "This Sino-Korean word means a hospital or medical clinic. The first syllable 병 (病) means sickness, illness, or disease, as in 병실 (a sickroom; an infirmary), 병석 (a sickbed; “sickness place”), and 병사 (a death from sickness). The second syllable 원 (院) means public building or house, as in 학원 (an educational institute; an academy; “learning house”), 양로원 (a nursing home), 법원 (a courthouse; “law house”), 상원 (the Upper House; the Senate), and 하원 (the Lower House; the House of Representatives). Thus the literal meaning of 병원 is “illness house” or “disease house”, and the word refers to a hospital or medical clinic, even a doctor’s office.\n\n"
             "Keep in mind that 원 in the following words represents 병원: 입원 (admission into a hospital; hospitalization), 퇴원 (leaving the hospital; discharge from the hospital), and 원장 (the director [of a hospital]; “hospital chief”).",
             tables=[ktable(_BYUNG)]),
        card("Sino-Korean in use: 통증 (痛症)",
             "This Sino-Korean word means a (physical) pain. The first syllable 통 (痛) means ache or pain, as in 두통 (a headache), 치통 (a toothache), 복통 (a stomachache), and 신경통 (neuralgia; “nerve pain”). The second syllable 증 (症) means symptom, as in 불면증 (insomnia; “no sleeping symptom”), 우울증 (the blues; mental depression; “melancholy symptom”), and 증상 (symptoms; the condition [of a patient]; “symptom and condition”). Thus the literal meaning of 통증 is “pain symptom” and the word means a physical pain, an ache, a pang, or pricking.",
             tables=[ktable(_TONG)]),
        card("Sino-Korean in use: 혈압 (血壓)",
             "This Sino-Korean word means blood pressure. The first syllable 혈 (血) means blood, as in 혈관 (a blood vessel; a vein; “blood tube”), 혈색 (a complexion; “blood color”), 혈액 (blood; “blood fluid”), and 수혈 (blood transfusion). The second syllable 압 (壓) means pressure or pressing, as in 고혈압 (hypertension; high blood pressure), 수압 (hydraulic pressure; “water pressure”), 압력 (pressure; “pressing power”), 고압 (high pressure; high tension; high voltage), and 중압감 (a feeling of oppression; “heavy pressing feeling”).\n\n"
             "The book asks you to guess the meaning of 저혈압 and 혈액형 (my answers: low blood pressure; blood type).",
             tables=[ktable(_HYUL)]),
        card("Activities left out", "The SMART Board activities, the Sino-Korean PowerPoint presentation and the picture-based Writing activity naming the specialty in each picture are computer and picture activities."),
    ],
    exercises=uniq(
        _tr(_SPEC + _BYUNG + _TONG + _HYUL, k=3)
        + [M("What does 병 (病) mean?", "sickness; illness; disease", ["a house", "pain", "blood"], "병실, 병석."), M("What does 원 (院) mean?", "a public building or house", ["sickness", "pressure", "a symptom"], "학원, 법원, 병원."), M("What does 통 (痛) mean?", "ache or pain", ["blood", "a house", "a symptom"], "두통, 치통."), M("What does 증 (症) mean?", "a symptom", ["pain", "blood", "pressure"], "증상, 불면증."), M("What does 혈 (血) mean?", "blood", ["pressure", "a house", "pain"], "혈액, 혈관."), M("What does 압 (壓) mean?", "pressure; pressing", ["blood", "a symptom", "a house"], "고혈압, 압력."),
           M("What is the literal meaning of 병원?", "“illness house”", ["“skin department”", "“pain symptom”", "“blood fluid”"], "병 + 원."), M("What is the literal meaning of 통증?", "“pain symptom”", ["“illness house”", "“blood fluid”", "“eye department”"], "통 + 증."), M("What does 원 stand for in 입원, 퇴원 and 원장?", "병원", ["학원", "법원", "양로원"], "The book’s note."), M("What is a 치과 의사?", "a dentist", ["an eye doctor", "a surgeon", "a pediatrician"], "치과 = dentistry."),
           F("눈이 아파서 ___에 갔어요. (ophthalmology)", "안과", ["치과", "내과"], "안과 = eye."), F("이가 아파서 ___에 갔어요. (dentistry)", "치과", ["안과", "외과"], "치과 = tooth."), F("아기가 아파서 ___에 갔어요. (pediatrics)", "소아과", ["산부인과", "내과"], "소아과 = small child."), F("다리가 부러져서 ___에서 치료를 받았어요. (surgery)", "외과", ["내과", "피부과"], "외과."), F("머리가 아프면 ___이 있어요. (a headache)", "두통", ["치통", "복통"], "두통 = headache."),
           read_q("병원"), read_q("통증"), read_q("혈압"), read_q("이비인후과"), read_q("피부과")]
    ),
)

# ================================================================== L2: Vocabulary Builder
_VB = [("가렵다", "to be itchy"), ("내과", "internal medicine"), ("맥박", "pulsation; pulse"), ("몸살", "a body ache (from fatigue or overwork)"), ("콜레스테롤", "cholesterol"), ("체중 / 몸무게", "body weight"), ("외과", "the department of surgery"), ("혈압", "blood pressure"), ("신장", "height; “body length”"), ("안과", "ophthalmology; “eye department”"), ("목이 쉬다", "to get hoarse; to lose one’s voice"), ("이비인후과", "ear, nose, and throat (ENT); otolaryngology"), ("어지럽다", "to be dizzy"), ("피부과", "dermatology; “skin department”"), ("치과", "dentistry; “tooth department”"), ("구역질", "nausea"), ("소변", "urine; “small excrement”"), ("독감", "influenza; the flu; “severe cold”")]
_GRP = [("Symptoms and illnesses", ["가렵다", "몸살", "목이 쉬다", "어지럽다", "구역질", "독감"]), ("Medical specialties", ["내과", "외과", "안과", "이비인후과", "피부과", "치과"]), ("Checkup measurements and tests", ["맥박", "혈압", "신장", "체중 / 몸무게", "소변", "콜레스테롤"])]
L2 = lesson(
    "Ch 29 · Vocabulary Builder: grouping the words, and a study strategy",
    "가렵다 · 맥박 · 몸살 · 콜레스테롤 · 체중 · 목이 쉬다 · 어지럽다 · 구역질 · 소변 · 독감",
    requires=[],
    cards=[
        card("Vocabulary Builder: the new words",
             "In the Vocabulary Builder of Unit 8 you no longer work with picture-based presentations; instead you discover patterns in the core vocabulary. The book gives the words below and asks you to divide them into columns by the patterns you find, to give each column a title in English, and to write the meanings (dictionary allowed); then to compare your work with your classmates and your teacher.",
             tables=[ktable(_VB)]),
        card("One way to group them (mine)", "The book leaves the grouping to you; this is my grouping.",
             tables=[ktable([(w, _en(w)) for w in ws]) for _, ws in _GRP]),
        card("Vocabulary Learning Strategy: use new words in meaningful ways",
             "Many language experts agree that the best way to learn and memorize new words is to repeatedly use them in meaningful ways. Here are a few tips: read and listen to the new words in a sentence or paragraph; say the new words aloud to activate your auditory memory; relate the new words to words you already know; make up a sentence or create a story using the new words; and use the new words in an actual conversation."),
        card("Activities left out", "Activities 1, 2 and 4 (SMART Board), Activity 3 (a listening activity in which you circle the word matching each description, to reach a destination) and Activity 5 (making up a story in groups, with word lists the teacher gives) are computer, audio and group activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(["가렵다", "맥박", "몸살", "콜레스테롤", "체중 / 몸무게", "목이 쉬다", "어지럽다", "구역질", "소변", "독감", "혈압", "신장"]))
        + _tr(_VB, k=3)
        + [M("Which group do 내과, 외과 and 안과 belong to?", "Medical specialties", ["Symptoms", "Measurements", "Body parts"], "과 = department."), M("Which group do 맥박, 혈압 and 신장 belong to?", "Checkup measurements", ["Medical specialties", "Symptoms", "Drinks"], "Measured at a checkup."), M("Which group do 가렵다, 어지럽다 and 구역질 belong to?", "Symptoms", ["Medical specialties", "Measurements", "Hospitals"], "증상."),
           M("What does the strategy advise?", "Use new words in meaningful ways", ["Memorize without use", "Avoid speaking", "Only read"], "Repeated meaningful use."), M("Which tip activates your auditory memory?", "Say the new words aloud", ["Write them once", "Skip them", "Read silently"], "The book’s tip."),
           F("감기에 걸리면 ___이 없어요. (appetite)", "식욕", ["소리", "연고"], "식욕 = appetite."), F("며칠 동안 밥을 못 먹어서 ___. (I’m dizzy)", "어지러워요", ["가려워요", "아파요"], "어지럽다."), F("피부가 ___ 긁었어요. (itchy)", "가려워서", ["어지러워서", "쉬어서"], "가렵다."), F("노래 연습을 많이 해서 ___. (my voice got hoarse)", "목이 쉬었어요", ["목이 아팠어요", "목을 쉬었어요"], "목이 쉬다."),
           read_q("가렵다"), read_q("어지럽다"), read_q("목이 쉬다"), read_q("콜레스테롤"), read_q("몸살")]
    ),
)

# ================================================================== L3: Topic A
_A_DLG = [
    ("민아", "오랜만이야. 요즘 잘 지내?", "It’s been a long time. How have you been lately?"),
    ("주희", "응. 근데, 지난주에 독감에 걸려서 고생했어.", "Yeah. By the way, last week I caught the flu and had a hard time."),
    ("민아", "이제 괜찮아?", "Are you okay now?"),
    ("주희", "독감은 다 나았어. 그런데 이제는 알레르기 때문에 힘들어.", "I’ve recovered from the flu. But now I’m having a hard time because of allergies."),
    ("민아", "알레르기?", "Allergies?"),
    ("주희", "응. 여기 저기 가려워 죽겠어.", "Yeah. I’m so itchy all over, I could die."),
    ("민아", "그럼, 연고 좀 바르지.", "Then why don’t you put on some ointment?"),
    ("주희", "발랐어. 그런데 발라도 가려우니까 계속 긁어. 이제는 긁은 데가 아프기 시작해.", "I did. But even when I apply it, it’s itchy, so I keep scratching. Now the places I scratched are starting to hurt."),
    ("민아", "나도 어제 못 잤어.", "I couldn’t sleep yesterday either."),
    ("주희", "왜? 너도 어디 아파?", "Why? Are you sick somewhere, too?"),
    ("민아", "아니, 나 임신했어.", "No, I’m pregnant."),
    ("주희", "어머! 축하해. 얼마나 됐어?", "Oh my! Congratulations. How far along are you?"),
    ("민아", "이제 삼 개월 조금 넘었어. 요즘은 어지럽고 구역질도 나서 힘들어. 식욕도 없고.", "It’s just a little over three months now. These days I’m dizzy and I feel nauseated, so it’s hard. I have no appetite either."),
    ("주희", "그래? 그래도 임신했을 때는 잘 먹어야 해.", "Is that so? Still, when you’re pregnant you have to eat well."),
]
_A_WORDS = ["가렵다", "고생", "구역질", "긁다", "넘다", "독감", "두통", "목이 쉬다", "몸살", "바르다", "복통", "소리", "식욕", "알레르기 / 알러지", "어지럽다", "연고", "이 / 이빨", "임신", "참다", "치통"]
L3 = lesson(
    "Ch 29 · Topic A: I had a hard time with the flu (독감에 걸려서 고생했어)",
    "독감에 걸려서 고생했어 · 알레르기 · 연고 · 긁어 · 임신했어 · 어지럽고 구역질도 나서",
    requires=[],
    cards=[
        card("Topic A: I had a hard time with the flu (독감에 걸려서 고생했어)",
             "A woman who is suffering from allergies and her pregnant friend are discussing their physical conditions. (The English is mine; the book gives none. The book writes 나… and 식욕도 없고… with ellipses; they are left out, and 3개월 is spelled out.)",
             examples=dlg(_A_DLG)),
        card("Core words and phrases of Topic A", "The meanings are the book’s (from the Core Vocabulary of the chapter); 고생(하다), 구역질(이 나다), 몸살(나다) and 임신(하다) take the forms in parentheses.", tables=[ktable(_rows(_A_WORDS))]),
        card("Activities left out", "The SMART Board activities, Follow-up 1 (listening to three dialogs and writing the symptoms) and Follow-up 2 (newspaper ads for medicine, which are pictures) are computer, audio and picture activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_A_WORDS)))
        + _tr(_strip(_A_DLG), k=3)
        + [M("What did 주희 have last week?", "The flu", ["A toothache", "A broken leg", "A headache"], "독감에 걸려서 고생했어."), M("What is 주희 having a hard time with now?", "Allergies", ["The flu", "Pregnancy", "A toothache"], "알레르기 때문에 힘들어."), M("What does 주희 do to her itchy skin?", "She applies ointment but keeps scratching", ["She takes a bath", "She sleeps", "She sees a dentist"], "발랐어. 계속 긁어."), M("What has started to hurt?", "The places she scratched", ["Her head", "Her teeth", "Her back"], "긁은 데가 아프기 시작해."),
           M("What is 민아’s news?", "She is pregnant", ["She has the flu", "She has allergies", "She is leaving"], "임신했어."), M("How far along is 민아?", "A little over three months", ["One week", "Eight months", "A year"], "삼 개월 조금 넘었어."), M("What are 민아’s symptoms?", "Dizziness, nausea and no appetite", ["Itchiness", "A fever", "A cough"], "어지럽고 구역질도 나서. 식욕도 없고."), M("What does 주희 advise?", "Eat well when pregnant", ["Take medicine", "Rest all day", "See a doctor"], "잘 먹어야 해."),
           F("지난주에 독감에 걸려서 ___. (I had a hard time)", "고생했어", ["참았어", "발랐어"], "고생하다."), F("여기 저기 ___ 죽겠어. (I’m itchy)", "가려워", ["어지러워", "아파"], "가렵다."), F("연고 좀 ___. (put on)", "바르지", ["긁지", "참지"], "연고를 바르다."), F("가려운 곳을 너무 ___ 피가 났어요. (scratched)", "긁어서", ["발라서", "참아서"], "긁다."), F("임신했을 때는 잘 ___ 해. (must eat)", "먹어야", ["먹었어야", "먹고 싶어야"], "-아/어야 해."),
           read_q("독감에 걸려서 고생했어"), read_q("알레르기 때문에 힘들어"), read_q("여기 저기 가려워 죽겠어"), read_q("연고 좀 바르지"), read_q("임신했을 때는 잘 먹어야 해")]
    ),
)

# ================================================================== L4: Topic A activities (symptom table)
_SYM = [("열이 나고 기침을 한다.", "has a fever and coughs", "독감"), ("피부가 가렵다.", "the skin is itchy", "알레르기"), ("어지럽고 식욕이 없다.", "dizzy and has no appetite", "임신"), ("몸이 여기 저기 아프다.", "the body aches all over", "몸살"), ("눈이 붓고 빨갛다.", "the eyes are swollen and red", "알레르기"), ("목이 붓고 목소리가 쉬었다.", "the throat is swollen and the voice is hoarse", "독감"), ("구역질이 난다.", "feels nauseated", "임신")]
_MORE = {"열이 나고 기침을 한다.": "독감, 몸살", "피부가 가렵다.": "알레르기", "어지럽고 식욕이 없다.": "임신, 독감", "몸이 여기 저기 아프다.": "몸살, 독감", "눈이 붓고 빨갛다.": "알레르기", "목이 붓고 목소리가 쉬었다.": "독감", "구역질이 난다.": "임신, 독감"}
L4 = lesson(
    "Ch 29 · Topic A activity: which illness shows which symptoms?",
    "열이 나고 기침을 한다 · 피부가 가렵다 · 눈이 붓고 빨갛다 · 목이 붓고 목소리가 쉬었다 · 독감 · 몸살 · 임신 · 알레르기",
    requires=[],
    cards=[
        card("Activity 1 (Reading): the symptoms table",
             "The book gives a table of physical discomforts and asks you to read each symptom and tick the conditions in which it appears (독감 · 몸살 · 임신 · 알레르기); more than one answer is possible, and the first one is done for you. The symptoms are the book’s; the ticks (my answers; the book’s check marks do not survive in the text) and the English are mine.",
             tables=[table(["Symptom", "English (mine)", "Condition(s) (mine)"], [[s, e, _MORE[s]] for s, e, _ in _SYM], say=[0])]),
        card("Useful pairs (mine)", "The flu (독감) and a body ache (몸살) bring a fever, a cough, a sore throat and aching; allergies (알레르기) bring itching and red, swollen eyes; pregnancy (임신) brings dizziness, nausea and loss of appetite (Topic A’s dialog)."),
        card("Activities left out", "Activity 2 (family members’ sticky-note messages to an ill relative, which are pictures), Activity 3 (listening to three family conversations) and Activity 4 (listening to three callers’ complaints, then group work giving advice in Korean) are picture, audio and group activities."),
    ],
    exercises=uniq(
        _tr([(s, e) for s, e, _ in _SYM], k=3)
        + [M("Which condition fits “" + s + "” best?", c, [x for x in ["독감", "알레르기", "임신", "몸살"] if x != c][:3], "The table.") for s, e, c in _SYM]
        + [M("In which condition is the skin itchy?", "알레르기", ["임신", "몸살", "독감"], "피부가 가렵다."), M("Which condition brings dizziness and no appetite in the dialog?", "임신", ["알레르기", "독감", "몸살"], "어지럽고 식욕이 없다."),
           F("열이 나고 ___을 한다. (cough)", "기침", ["구역질", "두통"], "기침 = a cough."), F("눈이 ___ 빨갛다. (swollen and)", "붓고", ["가렵고", "쉬고"], "붓다."), F("목이 붓고 목소리가 ___. (hoarse)", "쉬었다", ["넘었다", "발랐다"], "목소리가 쉬다."), F("몸이 여기 저기 ___. (aches)", "아프다", ["가렵다", "붓다"], "아프다."),
           read_q("열이 나고 기침을 한다"), read_q("피부가 가렵다"), read_q("어지럽고 식욕이 없다"), read_q("눈이 붓고 빨갛다"), read_q("목이 붓고 목소리가 쉬었다")]
    ),
)

# ================================================================== L5: Topic B
_B_DLG = [
    ("현수", "정인아, 어제 수업에 왜 안 왔어?", "Jeongin, why didn’t you come to class yesterday?"),
    ("정인", "허리가 너무 아파서 외과에 갔다 왔어. 컴퓨터를 너무 오래 해서 아픈 것 같아.", "My lower back hurt so much that I went to the surgery department. I think it hurts because I used the computer too long."),
    ("현수", "그래? 의사 선생님이 뭐래?", "Really? What did the doctor say?"),
    ("정인", "엑스레이를 찍었는데 허리에 조금 이상이 있대.", "I had an X-ray taken, and they say there is a slight abnormality in my lower back."),
    ("현수", "그럼, 어떻게 해야 해?", "Then what do you have to do?"),
    ("정인", "여러 가지 검사를 받아보고 검사 결과가 나쁘면 수술을 받아야 해.", "I have to take various tests, and if the test results are bad, I have to have surgery."),
    ("현수", "그럼, 어제는 병원에 가서 엑스레이를 찍고 진찰만 받았어?", "Then yesterday you went to the hospital, had an X-ray and only had an exam?"),
    ("정인", "아니, 진찰 받은 후에 물리치료도 받고 왔어.", "No, after the exam I also got physical therapy before coming back."),
    ("현수", "의사 선생님이 약도 처방해 주었어?", "Did the doctor prescribe medicine, too?"),
    ("정인", "응. 우선 진통제를 처방해 주었어. 그래서 통증이 심할 때 먹고 있어.", "Yes. First of all, the doctor prescribed painkillers. So I take them when the pain is severe."),
    ("현수", "힘들겠다. 허리가 나을 때까지 컴퓨터를 조금만 하도록 해.", "That must be hard. Make sure to use the computer only a little until your back gets better."),
    ("정인", "응. 알았어. 걱정해 줘서 고마워.", "Okay. Got it. Thanks for worrying about me."),
]
_B_WORDS = ["검사", "결과", "내과", "-도록 하다", "물리치료", "산부인과", "소아과", "수술", "안과", "외과", "우선", "이비인후과", "이상", "입원", "진료", "진찰", "치과", "치료", "퇴원", "피부과", "환자"]
L5 = lesson(
    "Ch 29 · Topic B: My lower back really hurts (허리 통증이 심해요)",
    "허리 통증이 심해요 · 외과 · 엑스레이 · 검사 결과 · 수술 · 물리치료 · 진통제 · 처방",
    requires=[],
    cards=[
        card("Topic B: My lower back really hurts (허리 통증이 심해요)",
             "Two college students, Hyunsoo and Jeongin, are talking about Jeongin’s hospital visit for her severe lower back pain. (The English is mine; the book gives none.)",
             examples=dlg(_B_DLG)),
        card("Core words and phrases of Topic B", "The meanings are the book’s (from the Core Vocabulary of the chapter); –도록 하다 is explained in the grammar.",
             tables=[ktable(_rows([w for w in _B_WORDS if w != "-도록 하다"])), table(["Pattern", "Meaning"], [["-도록 하다", "to make sure (see the next lessons)"]])]),
        card("Activities left out", "The vocabulary table (filling in the Korean or English meanings of 외과, 이상, 검사, 우선, 결과, 물리치료 and –도록 하다), the SMART Board activity, Follow-up 1 (writing the specialty shown in six pictures) and Follow-up 2 (listening to doctor–patient conversations) are picture, audio and computer activities, and the “useful websites” (Severance Hospital and Seoul National University Hospital) are web pages."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_B_WORDS)))
        + _tr(_strip(_B_DLG), k=3)
        + [M("Why did 정인 miss class?", "She went to the hospital for her back pain", ["She had a cold", "She was on a trip", "She overslept"], "허리가 너무 아파서 외과에 갔다 왔어."), M("What does 정인 think caused the pain?", "Using the computer too long", ["Carrying a bag", "Sports", "Cold weather"], "컴퓨터를 너무 오래 해서."), M("What did the doctor find on the X-ray?", "A slight abnormality in the lower back", ["A broken bone", "Nothing", "A tumor"], "허리에 조금 이상이 있대."), M("When must she have surgery?", "If the test results are bad", ["Right away", "Never", "If she skips class"], "검사 결과가 나쁘면 수술을 받아야 해."),
           M("What did she get after the exam?", "Physical therapy", ["Surgery", "A cast", "A shot only"], "물리치료도 받고 왔어."), M("What did the doctor prescribe first?", "Painkillers", ["Antibiotics", "Ointment", "Vitamins"], "진통제."), M("When does she take the medicine?", "When the pain is severe", ["Every hour", "Before bed only", "Never"], "통증이 심할 때."), M("What does 현수 advise?", "Use the computer only a little until her back gets better", ["Quit school", "Have surgery now", "Stay in bed forever"], "나을 때까지 컴퓨터를 조금만 하도록 해."),
           F("허리가 너무 아파서 ___에 갔다 왔어. (surgery department)", "외과", ["안과", "치과"], "외과."), F("의사 선생님이 약도 ___ 주었어? (prescribed)", "처방해", ["진찰해", "퇴원해"], "처방하다."), F("진찰 받은 후에 ___도 받고 왔어. (physical therapy)", "물리치료", ["수술", "입원"], "물리치료."), F("검사 ___가 나쁘면 수술을 받아야 해. (results)", "결과", ["이상", "환자"], "검사 결과."), F("허리에 조금 ___이 있대. (abnormality)", "이상", ["결과", "우선"], "이상 = abnormality."),
           read_q("허리 통증이 심해요"), read_q("엑스레이를 찍었어요"), read_q("검사 결과가 나쁘면 수술을 받아야 해"), read_q("진통제를 처방해 주었어"), read_q("컴퓨터를 조금만 하도록 해")]
    ),
)

# ================================================================== L6: Grammar A: ㅅ irregular verbs
_SI = [("낫다", "to recover (from sickness)", "나았어요", "나아서", "나으면", "나을 때"), ("붓다", "to swell; to become swollen; to pour", "부었어요", "부어서", "부으면", "부을 때"), ("짓다", "to build; to compose", "지었어요", "지어서", "지으면", "지을 때"), ("젓다", "to stir", "저었어요", "저어서", "저으면", "저을 때"), ("긋다", "to draw (a line)", "그었어요", "그어서", "그으면", "그을 때"), ("잇다", "to connect", "이었어요", "이어서", "이으면", "이을 때")]
_SI_REG = [("벗다", "to take off", "벗었어요", "벗어서", "벗으면", "벗을 때"), ("씻다", "to wash", "씻었어요", "씻어서", "씻으면", "씻을 때"), ("웃다", "to smile; to laugh", "웃었어요", "웃어서", "웃으면", "웃을 때")]
_SI_S = [("감기 다 나았어요?", "Have you recovered from your cold?"), ("다쳐서 팔이 많이 부었어요.", "My arm is very swollen because I got injured."), ("내년에 우리 집을 새로 지을 거예요.", "I will build a new house next year."), ("국이 끓으면 한두 번 저으세요.", "When the broth is simmering, stir it once or twice."), ("운동복을 벗어서 세탁기에 넣으세요.", "Take off your gym suit and put it in the washing machine.")]
_SI_Q = [("일주일 동안 배탈이 나서 힘들었어요. 그런데 이제 다 ___. (낫다)", "나았어요", ["낫았어요", "낫어요"], "My stomach ache: recovered."), ("어제 축구 하다가 발목을 삐었어요. 좀 ___ 아파요. (붓다)", "부었는데", ["붓었는데", "붓는데"], "swollen"), ("자, 여기에 줄을 똑바로 ___. (긋다)", "그으세요", ["긋으세요", "그세요"], "draw a line"), ("저녁 먹기 전에 먼저 ___. (씻다)", "씻어", ["씨어", "씼어"], "wash (regular)"), ("이 약을 이틀 동안 드세요. 그 후에도 ___ 않으면 병원에 가 보세요. (낫다)", "낫지", ["나지", "나으지"], "before a consonant: 낫지"), ("옆집에 새로 이사 온 사람이 저한테 ___ 인사했어요. (웃다)", "웃으면서", ["우면서", "웃어면서"], "웃다 is regular")]
L6 = lesson(
    "Ch 29 · Grammar A: ㅅ irregular verbs (낫다, 붓다, 짓다, 젓다, 긋다, 잇다)",
    "ㅅ 불규칙 · 나았어요 · 부었어요 · 지었어요 · 저으세요 · 그으세요 · 이어요",
    requires=[],
    cards=[
        card("ㅅ irregular verbs",
             "You have learned a few verbs whose stem ends in ㅅ, such as 낫다, 붓다, 벗다, and 씻다. Some of these verbs lose ㅅ when their stem is followed by a vowel. Take 낫다 (to get well): 낫 + 았어요 → 나았어요; 낫 + 아서 → 나아서; 낫 + 으면 → 나으면; 낫 + (으)ㄹ 때 → 나을 때.\n\n"
             "Verbs that lose ㅅ when their stem is followed by a vowel are commonly known as “ㅅ irregular verbs”. However, not all verbs whose stem ends in ㅅ are ㅅ irregular verbs. For example, 벗다 is not an ㅅ irregular verb and does not lose ㅅ even when the stem is followed by a vowel, as in 운동복을 벗어서 세탁기에 넣으세요 (Take off your gym suit and put it in the washing machine). Only the following verbs, including 낫다, are ㅅ irregular verbs: 낫다 (to recover [from sickness]), 붓다 (to swell; to become swollen; to pour), 짓다 (to build; to compose), 젓다 (to stir), 긋다 (to draw [a line]) and 잇다 (to connect).",
             tables=[table(["Verb", "Meaning", "-았/었어요", "-아/어서", "-(으)면", "-(으)ㄹ 때"], [list(r) for r in _SI], say=[0, 2, 3, 4, 5])]),
        card("Regular ㅅ verbs for contrast (mine)", "벗다, 씻다 and 웃다 keep the ㅅ.",
             tables=[table(["Verb", "Meaning", "-았/었어요", "-아/어서", "-(으)면", "-(으)ㄹ 때"], [list(r) for r in _SI_REG], say=[0, 2, 3, 4, 5])]),
        card("The book’s example sentences", "In the book’s example sentences these verbs lose ㅅ when a vowel comes after the stem (the English is the book’s):", examples=passage(_SI_S)),
        card("Follow-up 1 (Reading and writing): complete the sentences", "The book gives six sentences and asks you to complete them with the verb in parentheses (낫다, 붓다, 긋다, 씻다, 낫다, 웃다). The answers are mine; the six fill-in exercises below use the book’s sentences."),
        card("Activities left out", "Follow-up 2 (reading Yuna’s note to her friend about a pharmacist’s advice on an eye infection, finding the ㅅ verbs and writing their meanings) uses a note that is a picture."),
    ],
    exercises=uniq(
        _tr(_SI_S, k=3)
        + [F(a, b, c, d) for a, b, c, d in _SI_Q]
        + [M("Which verbs are ㅅ irregular?", "낫다, 붓다, 짓다, 젓다, 긋다, 잇다", ["벗다, 씻다, 웃다", "먹다, 마시다", "가다, 오다"], "The book’s list."), M("Which verb is NOT ㅅ irregular?", "벗다", ["낫다", "붓다", "짓다"], "벗어서 keeps ㅅ."), M("What does 낫다 become before 았어요?", "나았어요", ["낫았어요", "낫었어요", "낫아요"], "낫 + 았어요."), M("What does 짓다 become before 을 거예요?", "지을 거예요", ["짓을 거예요", "짓을 거에요", "지울 거예요"], "짓 + 을 → 지을."), M("What does 젓다 become before 으세요?", "저으세요", ["젓으세요", "저세요", "저여요"], "젓 + 으세요."), M("What does 붓다 become before 었어요?", "부었어요", ["붓었어요", "붓어요", "부웠어요"], "붓 + 었어요."),
           M("What does 낫다 mean?", "to recover (from sickness)", ["to build", "to stir", "to connect"], "나았어요."), M("What does 짓다 mean?", "to build; to compose", ["to swell", "to stir", "to draw"], "집을 짓다."), M("What does 긋다 mean?", "to draw (a line)", ["to connect", "to build", "to pour"], "줄을 긋다."), M("What does 잇다 mean?", "to connect", ["to stir", "to draw", "to swell"], "잇다."),
           F("감기가 다 ___. (recovered)", "나았어요", ["낫았어요", "나서요"], "낫다."), F("내년에 우리 집을 새로 ___ 거예요. (build)", "지을", ["짓을", "지울"], "짓다."), F("국이 끓으면 한두 번 ___. (stir)", "저으세요", ["젓으세요", "저어요"], "젓다."), F("다쳐서 팔이 많이 ___. (swollen)", "부었어요", ["붓었어요", "부웠어요"], "붓다."),
           read_q("감기 다 나았어요"), read_q("다쳐서 팔이 많이 부었어요"), read_q("내년에 우리 집을 새로 지을 거예요"), read_q("국이 끓으면 한두 번 저으세요"), read_q("운동복을 벗어서 세탁기에 넣으세요")]
    ),
)

# ================================================================== L7: Grammar B: -도록 하다
_DO1 = [("앞으로 조심하도록 하겠습니다.", "I will make sure to be cautious from now on."), ("전기를 아껴 쓰도록 할게요.", "I will make sure to save electricity.")]
_DO2 = [("이 약을 하루에 세 번씩 드시도록 하세요.", "Make sure you take this medication three times a day."), ("아침에 일찍 일어나도록 하세요.", "Make sure you get up early in the morning.")]
_DO3 = [("선생님께서 학생들이 말하기 연습을 많이 하도록 하셨어요.", "My teacher made sure that students practiced speaking a lot.")]
_DOP = [("감기에 걸리지 않다", "not to catch a cold"), ("약을 하루에 세 번 먹다", "to take the medicine three times a day"), ("일찍 자다", "to go to bed early"), ("매일 운동하다", "to exercise every day"), ("물을 많이 마시다", "to drink a lot of water"), ("스트레스를 받지 않다", "not to get stressed"), ("손을 자주 씻다", "to wash your hands often")]
_DOP_E = {"감기에 걸리지 않다": ("Make sure you do not catch a cold.", "I will make sure not to catch a cold."), "약을 하루에 세 번 먹다": ("Make sure you take the medicine three times a day.", "I will make sure to take the medicine three times a day."), "일찍 자다": ("Make sure you go to bed early.", "I will make sure to go to bed early."), "매일 운동하다": ("Make sure you exercise every day.", "I will make sure to exercise every day."), "물을 많이 마시다": ("Make sure you drink a lot of water.", "I will make sure to drink a lot of water."), "스트레스를 받지 않다": ("Make sure you do not get stressed.", "I will make sure not to get stressed."), "손을 자주 씻다": ("Make sure you wash your hands often.", "I will make sure to wash your hands often.".replace("your", "my"))}
_DOC = [("요즘 체중이 늘었어요.", "I have gained weight lately."), ("다이어트를 하도록 하세요.", "Make sure you go on a diet."), ("매일 아침 달리기를 하도록 하세요.", "Make sure you run every morning.")]
L7 = lesson(
    "Ch 29 · Grammar B: –도록 하다, to make sure; to see to it that",
    "-도록 하다 · 조심하도록 하겠습니다 · 드시도록 하세요 · 일어나도록 하세요 · 하도록 하셨어요",
    requires=[],
    cards=[
        card("–도록 하다: make sure …; see to it that …",
             "–도록 하다 is equivalent to the English phrases “to make sure …” or “to see to it that …”. When the speaker is the subject, the future tense is used with –도록 하다 to indicate the speaker’s will. –도록 하다 can also be used to offer suggestions or advice. It also expresses the idea of causing or influencing an action that has taken place. (The English is the book’s.)",
             examples=passage(_DO1)),
        card("As a suggestion or advice", "", examples=passage(_DO2)),
        card("Causing or influencing an action that has taken place", "", examples=passage(_DO3)),
        card("Forms (mine)", "The phrases in the book’s model are made with the verb stem + 도록: –도록 하세요 (advice) and –도록 하겠어요 (the speaker’s will). The book’s own phrase list is the teacher’s; these phrases are mine except the first (the book’s model).",
             tables=[table(["Phrase", "-도록 하세요", "-도록 하겠어요", "English (mine)"], [[p, p[:-1] + "도록 하세요", p[:-1] + "도록 하겠어요", _DOP_E[p][0]] for p, _ in _DOP], say=[0, 1, 2])]),
        card("Follow-up 5 (Writing, speaking and reading): the model",
             "The book asks you to write a concern in Korean, post it on the classroom wall, and have classmates write advice with –도록 하세요. The book’s model (the English is mine):",
             examples=passage(_DOC)),
        card("Activities left out", "Follow-up 4 (listening to doctor–patient conversations about checkup results) and the partner and class activities of Follow-ups 3 and 5 need partners, the teacher’s lists and a classroom wall."),
    ],
    exercises=uniq(
        _tr(_DO1 + _DO2 + _DO3 + _DOC, k=3)
        + [M("What does –도록 하다 mean?", "to make sure …; to see to it that …", ["to want to …", "to be able to …", "to try …"], "The book’s note."), M("How do you say “I will make sure to …” with –도록 하다?", "-도록 하겠습니다 / -도록 할게요", ["-도록 하세요", "-도록 했어요", "-도록 하지 마세요"], "Future for the speaker’s will."), M("How do you give advice with –도록 하다?", "-도록 하세요", ["-도록 하겠어요", "-도록 했어요", "-도록 할까요"], "아침에 일찍 일어나도록 하세요."), M("What does 학생들이 말하기 연습을 많이 하도록 하셨어요 express?", "The teacher made sure students practiced", ["The students asked", "The teacher practiced", "Students did not practice"], "Causing an action."),
           M("What does 감기에 걸리지 않도록 하세요 mean?", "Make sure you do not catch a cold", ["I will not catch a cold", "I caught a cold", "Catch a cold"], "Model."), M("What does 앞으로 조심하도록 하겠습니다 mean?", "I will make sure to be cautious from now on", ["Be cautious", "I was cautious", "Don’t be cautious"], "The speaker’s will."),
           F("아침에 일찍 일어나___ 하세요. (make sure)", "도록", ["려고", "기로"], "-도록 하세요."), F("이 약을 하루에 세 번씩 드시___ 하세요. (make sure)", "도록", ["려고", "지는"], "-도록."), F("앞으로 조심하도록 ___. (I will make sure)", "하겠습니다", ["하세요", "했어요"], "-도록 하겠습니다."), F("매일 아침 달리기를 하도록 ___. (Make sure)", "하세요", ["하겠습니다", "했어요"], "하세요."),
           read_q("앞으로 조심하도록 하겠습니다"), read_q("전기를 아껴 쓰도록 할게요"), read_q("이 약을 하루에 세 번씩 드시도록 하세요"), read_q("아침에 일찍 일어나도록 하세요"), read_q("감기에 걸리지 않도록 하세요")]
    ),
)

# ================================================================== L8: Topic C
_C_DLG = [
    ("김 과장", "박 과장, 건강 검진은 잘 받았어?", "Section Chief Park, did you get your health checkup well?"),
    ("박 과장", "응. 잘 받았어.", "Yes. I got it done well."),
    ("김 과장", "어떤 검사를 했는데?", "What tests did you do?"),
    ("박 과장", "혈액 검사하고 소변 검사.", "A blood test and a urine test."),
    ("김 과장", "다 정상이래?", "They say everything is normal?"),
    ("박 과장", "전에는 간이 좀 안 좋았었는데, 지금은 괜찮대.", "My liver wasn’t so good before, but they say it’s fine now."),
    ("김 과장", "콜레스테롤하고 혈압은 어때?", "How about your cholesterol and blood pressure?"),
    ("박 과장", "혈압은 정상인데 콜레스테롤 수치는 조금 높아.", "My blood pressure is normal, but my cholesterol level is a little high."),
    ("김 과장", "요즘 계속 살이 빠져서 나도 검진을 받을 생각이야.", "I keep losing weight these days, so I’m planning to get a checkup, too."),
    ("박 과장", "최근에 검진 받지 않았어?", "Didn’t you get a checkup recently?"),
    ("김 과장", "아니. 검진 받은 지 벌써 삼 년 됐어.", "No. It has already been three years since I had a checkup."),
    ("박 과장", "그래? 그럼 검진 받을 때가 됐구나!", "Is that so? Then it’s time for you to get a checkup!"),
    ("김 과장", "응. 이번에 검진 받는 김에 이것저것 다 받아 봐야겠어.", "Yes. Since I’m getting a checkup this time, I should try everything."),
]
_C_WORDS = ["간", "검진", "-(으)ㄴ/는 김에", "대변", "맥박", "살이 빠지다", "살이 찌다", "소변", "수치", "스트레스", "신장", "재다", "정상", "체온", "체중 / 몸무게", "측정", "콜레스테롤", "혈압", "혈액", "-(으)ㄴ 지 ~(이/가) 되다"]
L8 = lesson(
    "Ch 29 · Topic C: I had a health checkup (건강 검진을 받았어요)",
    "건강 검진을 받았어요 · 혈액 검사 · 소변 검사 · 콜레스테롤 수치 · 검진 받은 지 삼 년 · 검진 받는 김에",
    requires=[],
    cards=[
        card("Topic C: I had a health checkup (건강 검진을 받았어요)",
             "Two colleagues are conversing about the medical checkup one of them received recently. (The English is mine; the book gives none; 3년 is spelled out.)",
             examples=dlg(_C_DLG)),
        card("The book’s footnote", "이것저것 다 literally means “this thing, that thing, and all” and is translated as “everything”. When referring to every person or to everyone, we say 이 사람 저 사람 다."),
        card("Core words and phrases of Topic C", "The meanings are the book’s (from the Core Vocabulary of the chapter); 검진(하다/받다), 대변(보다), 소변(보다) and 측정(하다) take the forms in parentheses; the two patterns are explained in the grammar.",
             tables=[ktable(_rows([w for w in _C_WORDS if "-" not in w])), table(["Pattern", "Meaning"], [["-(으)ㄴ/는 김에", "because; since; as"], ["-(으)ㄴ 지 ~(이/가) 되다", "It has been ... since ..."]])]),
        card("Activities left out", "The SMART Board activities and the role-play (partners rehearse the dialog on cue cards and act it out for the teacher) are computer and partner activities."),
    ],
    exercises=uniq(
        vocab_exercises(_pairs(_PLAIN(_C_WORDS)))
        + _tr(_strip(_C_DLG), k=3)
        + [M("What tests did 박 과장 have?", "A blood test and a urine test", ["An X-ray and a dental test", "An eye test", "A hearing test"], "혈액 검사하고 소변 검사."), M("What was a little bad before?", "The liver", ["The heart", "The eyes", "The teeth"], "간이 좀 안 좋았었는데."), M("What is normal?", "His blood pressure", ["His cholesterol", "His weight", "His liver"], "혈압은 정상."), M("What is a little high?", "His cholesterol level", ["His blood pressure", "His pulse", "His weight"], "콜레스테롤 수치는 조금 높아."),
           M("What is 김 과장 noticing about himself?", "He keeps losing weight", ["He keeps gaining weight", "He cannot sleep", "He is dizzy"], "계속 살이 빠져서."), M("How long since 김 과장’s last checkup?", "Three years", ["One year", "Six months", "Ten years"], "삼 년 됐어."), M("What will 김 과장 do this time?", "Try everything while he is getting the checkup", ["Skip the checkup", "Take only one test", "Ask for surgery"], "받는 김에 이것저것 다."),
           F("혈액 ___하고 소변 검사. (test)", "검사", ["치료", "진료"], "검사."), F("혈압은 ___인데 콜레스테롤 수치는 조금 높아. (normal)", "정상", ["이상", "비정상"], "정상."), F("요즘 계속 살이 ___ 나도 검진을 받을 생각이야. (I lose weight)", "빠져서", ["쪄서", "넘어서"], "살이 빠지다."), F("검진 받은 ___ 벌써 삼 년 됐어. (since)", "지", ["김", "때"], "-(으)ㄴ 지."), F("검진 받는 ___ 이것저것 다 받아 봐야겠어. (while)", "김에", ["지가", "때에"], "-는 김에."),
           read_q("건강 검진은 잘 받았어"), read_q("혈액 검사하고 소변 검사"), read_q("혈압은 정상인데 콜레스테롤 수치는 조금 높아"), read_q("검진 받은 지 벌써 삼 년 됐어"), read_q("검진 받는 김에 이것저것 다 받아 봐야겠어")]
    ),
)

# ================================================================== L9: Q&A and brochure
_QA_Q = [("지난주에 돼지고기와 맥주를 마셨어요.", "Last week I had pork and beer."), ("그리고 잠을 잤는데 갑자기 복통이 시작되었습니다.", "Then I slept, and suddenly a stomachache began."), ("약국에서 소화제를 사 먹었는데 낫지를 않습니다.", "I bought and took a digestive medicine at a pharmacy, but it is not getting better."), ("어젯밤에는 배가 너무 아파서 잠도 잘 못 잤어요.", "Last night my stomach hurt so much that I could not sleep well."), ("계속 아랫배에 심한 통증이 있고 구역질이 납니다.", "I keep having severe pain in my lower abdomen and feel nauseated."), ("어제부터는 설사도 나기 시작했어요.", "Since yesterday I have also started to have diarrhea."), ("바빠서 병원에 가지 못하고 있습니다.", "I am busy and cannot go to the hospital."), ("어떻게 해야 할까요?", "What should I do?")]
_QA_A = [("환자분의 증상을 보면 단순한 소화불량이 아닌 것 같습니다.", "Judging from your symptoms, it does not seem to be simple indigestion."), ("먼저 가까운 병원의 내과를 방문하십시오.", "First, visit the internal medicine department of a nearby hospital."), ("그리고 진찰과 여러 가지 검사를 받도록 하세요.", "And make sure you get an examination and various tests."), ("의사의 처방 없이 약을 먹으면 증상이 더 나빠질 수 있습니다.", "If you take medicine without a doctor’s prescription, your symptoms can get worse."), ("병원에 가셔서 이상이 있는지 없는지를 빨리 확인하세요.", "Go to the hospital and quickly check whether there is anything wrong.")]
_BRO = [("영광병원 건강센터", "Yeonggwang Hospital Health Center"), ("건강 검진 안내", "Checkup information"),
        ("검진비는 남자 오십육만 원, 여자 육십만 원입니다.", "The checkup fee is 560,000 won for men and 600,000 won for women."), ("검사 항목은 의사 진찰, 신장, 체중, 체온, 맥박, 혈압 측정, 혈액형 검사, 콜레스테롤 검사, 소변 검사, 대변 검사, 부인과 검사, 엑스선 검사, 안과 검사, 치과 검사입니다.", "The test items are a doctor’s exam, measurement of height, weight, body temperature, pulse and blood pressure, blood type test, cholesterol test, urine test, stool test, gynecological test, X-ray test, eye test and dental test."),
        ("건강 검진 예약", "Checkup reservations"), ("온라인 예약은 홈페이지에 로그인한 후 예약하십시오.", "For an online reservation, log in to the homepage and then make the reservation."), ("전화 예약은 일오팔팔의 칠칠칠팔입니다.", "The reservation phone number is 1588-7778."), ("전화 예약 접수 시간은 월요일부터 금요일까지 오전 일곱 시 삼십 분부터 오후 네 시 삼십 분까지입니다.", "The phone reservation hours are Monday to Friday, from 7:30 a.m. to 4:30 p.m."),
        ("주의사항", "Precautions"), ("검진 전날 오후 아홉 시부터 검진일까지 아무것도 드시지 마십시오.", "From 9 p.m. the day before the checkup until the checkup day, do not eat anything."), ("신분증과 보험카드를 가져 오십시오.", "Bring your ID and insurance card."), ("검진비는 검진일에 모두 내셔야 합니다. 카드 결제도 가능합니다.", "You must pay the whole checkup fee on the checkup day. Card payment is possible."), ("병원 도착 시간은 오전 일곱 시 삼십 분에서 아홉 시 삼십 분까지로 해 주십시오.", "Please arrive at the hospital between 7:30 and 9:30 a.m.")]
L9 = lesson(
    "Ch 29 · Reading: a hospital Q&A about a stomachache and a checkup brochure",
    "설사와 복통이 심합니다 · 소화불량 · 내과 · 영광병원 건강센터 · 건강 검진 안내 · 주의사항",
    requires=[],
    cards=[
        card("Activity 3 (Reading): the question on a hospital’s health counseling page",
             "The book shows a Q&A posted on the health counseling section of a hospital website (진료상담, 소화기내과): the title is 설사와 복통이 심합니다 (I have severe diarrhea and a stomachache), posted by 김진경. Read it and fill in a table in English. The text is the book’s with the form’s date and view count left out; the English is mine.",
             examples=passage(_QA_Q)),
        card("The answer", "", examples=passage(_QA_A)),
        card("The table filled in (mine)", "The book leaves the table blank; these are my answers.",
             tables=[table(["Information", "Answer (mine)"], [["Inquirer’s symptoms", "Sudden stomachache after pork and beer; severe pain in the lower abdomen; nausea; diarrhea since yesterday; poor sleep; a digestive medicine did not help"], ["Advice", "Visit a nearby internal medicine department; get an examination and several tests; do not take medicine without a prescription; quickly check whether anything is wrong"], ["Recommended medical specialty", "내과 (internal medicine)"]])]),
        card("Topic C, Follow-up 1 (Reading): a medical checkup brochure",
             "The book gives a brochure for a checkup program (영광병원 건강센터) and asks you (a) to translate the underlined parts into English and (b) to find in the brochure what patients must do on the day of the test. The book’s underlines do not survive in the text, so the whole brochure is given here with my English; the numbers are spelled out in Hangul, the headings and the numbered lists are written as sentences (the book’s “항목” = “an item”).",
             examples=passage(_BRO)),
        card("What patients must do on the checkup day (mine)", "The book leaves the answer blank; these are the four things in the brochure.",
             tables=[table(["What to do", "English (mine)"], [["아무것도 드시지 마십시오", "Do not eat anything from 9 p.m. the day before"], ["신분증과 보험카드를 가져 오십시오", "Bring your ID and insurance card"], ["검진비를 모두 내십시오", "Pay the whole checkup fee on the day (a card is possible)"], ["오전 일곱 시 삼십 분에서 아홉 시 삼십 분까지 도착하십시오", "Arrive between 7:30 and 9:30 a.m."]], say=[0])]),
        card("Activities left out", "Follow-up 2 (listening to three telephone messages in which a doctor reports test results), the activities 1 and 2 of the chapter (SMART Board; summarizing two newspaper articles A and B about checkups, which are not in the book’s text), Activity 3 (listening to the two checkup packages) and the partner activities are audio, picture and computer activities."),
    ],
    exercises=uniq(
        _tr(_QA_Q + _QA_A + _BRO[2:], k=3)
        + [M("What began suddenly?", "A stomachache", ["A headache", "A toothache", "A fever"], "갑자기 복통이 시작되었습니다."), M("What did the inquirer take?", "A digestive medicine from a pharmacy", ["A painkiller", "An ointment", "Nothing"], "소화제를 사 먹었는데."), M("Why hasn’t the inquirer gone to the hospital?", "Too busy", ["Afraid", "No insurance", "The hospital is closed"], "바빠서 병원에 가지 못하고 있습니다."), M("What does the doctor advise?", "Visit the internal medicine department and get tests", ["Take more medicine", "Wait a week", "Drink water only"], "내과를 방문하십시오. 검사를 받도록 하세요."),
           M("What can happen if you take medicine without a prescription?", "The symptoms can get worse", ["Nothing", "You get better faster", "You pay less"], "증상이 더 나빠질 수 있습니다."), M("How much is the checkup fee for women?", "600,000 won", ["560,000 won", "1,588,000 won", "100,000 won"], "육십만 원."), M("What must you not do from 9 p.m. the day before?", "Eat anything", ["Sleep", "Drink water only", "Walk"], "아무것도 드시지 마십시오."), M("What must you bring?", "ID and insurance card", ["A passport", "Cash only", "A friend"], "신분증과 보험카드."), M("When should you arrive?", "Between 7:30 and 9:30 a.m.", ["At noon", "At 4:30 p.m.", "At night"], "오전 일곱 시 삼십 분에서 아홉 시 삼십 분."),
           F("먼저 가까운 병원의 ___를 방문하십시오. (internal medicine)", "내과", ["치과", "안과"], "내과."), F("진찰과 여러 가지 검사를 받___ 하세요. (make sure)", "도록", ["고는", "지만"], "-도록 하세요."), F("의사의 ___ 없이 약을 먹으면 증상이 더 나빠질 수 있습니다. (prescription)", "처방", ["진찰", "치료"], "처방."), F("검진 전날 오후 아홉 시부터 아무것도 ___ 마십시오. (eat, honorific)", "드시지", ["먹지", "드시고"], "드시지 마십시오."),
           read_q("설사와 복통이 심합니다"), read_q("먼저 가까운 병원의 내과를 방문하십시오"), read_q("영광병원 건강센터"), read_q("신분증과 보험카드를 가져 오십시오"), read_q("검진비는 검진일에 모두 내셔야 합니다")]
    ),
)

# ================================================================== L10: Grammar C: -(으)ㄴ 지 ~(이/가) 되다
_JI_S = [("몬트레이에 온 지 일 년이 되었어요.", "It has been a year since I came to Monterey."), ("공군에 입대한 지 삼 년이 되었습니다.", "It has been three years since I became an airman."), ("그 친구를 만난 지 오래 되었어요.", "A long time has passed since I met my friend."), ("한국말을 공부한 지 벌써 오 개월이 됐습니다.", "Five months have already passed since I started to learn Korean."), ("몬트레이에 온 지 얼마나 되었습니까?", "How long has it been since you came to Monterey?"), ("공군에 입대한 지 몇 년 되었어요?", "How long has it been since you joined the air force?")]
_IV = ["건강검진을 받다", "여행하다", "햄버거를 먹다", "군대에 입대하다", "군화를 닦다", "영화를 보다", "고향을 방문하다", "치과에 가다", "가족을 만나다", "혈압을 측정하다"]
_IV_E = ["to get a health checkup", "to travel", "to eat a hamburger", "to enlist in the military", "to polish combat boots", "to watch a movie", "to visit one’s hometown", "to go to the dentist", "to meet one’s family", "to measure blood pressure"]


def _ji_q(ph):
    head, v = ph.rsplit(" ", 1) if " " in ph else ("", ph)
    return (head + " " if head else "") + attr(v)[1] + " 지 얼마나 되었어요?"


_JI_MODEL = [("A", "박 일병, 건강검진을 받은 지 얼마나 되었어요?", "Private Park, how long has it been since you had a health checkup?"), ("B", "일 년 되었어요.", "It has been one year.")]
_JI_HOME = [("고향에 안 간 지 이 년이나 되었어요.", "It has been as long as two years since I last went to my hometown."), ("그래서 이번 크리스마스 때 가족을 보러 고향에 갈 겁니다.", "So this Christmas I will go to my hometown to see my family."), ("고향에 간 김에 고향 친구들을 만날 거예요.", "Since I will be in my hometown, I will meet my hometown friends."), ("고향 친구들을 만난 김에 친구들과 함께 영화도 볼 거예요.", "Since I will have met my hometown friends, I will also watch a movie with them.")]
L10 = lesson(
    "Ch 29 · Grammar C: –(으)ㄴ 지 ~(이/가) 되다, how long it has been since …",
    "-(으)ㄴ 지 되다 · 온 지 일 년이 되었어요 · 입대한 지 삼 년 · 얼마나 되었어요 · 몇 년 되었어요",
    requires=[],
    cards=[
        card("Expressing the passage of time: –(으)ㄴ 지 ~(이/가) 되다",
             "In English, to express the passage of time since a certain event or action took place, we often use “it has been [length of time] since …” or “[length of time] have passed since …”, as in “It has been a year since I came to DLI”.\n\n"
             "In Korean, we express a passage of time with –(으)ㄴ 지 ~(이/가) 되다, as in 몬트레이에 온 지 일 년이 되었어요 (It has been a year since I came to Monterey). 되었어요 means “became” or “has become”, and the literal translation of the phrase is “it has become a year since I came to Monterey”. The particle (이/가) after the length of time may be dropped, as in 공군에 입대한 지 삼 년(이) 되었습니다. (The book writes the numbers in digits; they are spelled out in Hangul here.)",
             examples=passage(_JI_S[:4])),
        card("Asking about the passage of time", "To ask about the passage of time, we use 얼마나, which means “how long”, or 몇 ~, as in 몇 년 (how many years), 몇 시간 (how many hours), 며칠 (how many days), etc.", examples=passage(_JI_S[4:])),
        card("Forms (mine)", "The question 지 얼마나 되었어요? is made with the verb’s past attributive form (–(으)ㄴ) + 지, for the book’s ten interview phrases of Follow-up 1.",
             tables=[table(["Interview phrase", "English (mine)", "Question"], [[p, e, _ji_q(p)] for p, e in zip(_IV, _IV_E)], say=[0, 2])]),
        card("Follow-up 1 (Speaking and listening): the model", "The book asks you to interview two classmates with these phrases and to write their answers in English. The book’s model (the English is mine):", examples=dlg(_JI_MODEL)),
        card("Follow-up 5 (Speaking): a plan to see your family this holiday season", "The book asks you to think about how long it has been since you were in your hometown and what else you want to do when you are there, then to tell three classmates, using –(으)ㄴ 지 ~(이/가) 되다 and –는 김에. The book’s model (2년 is spelled out; the English is mine):", examples=passage(_JI_HOME)),
        card("Activities left out", "Follow-up 2 (listening to five sentences about the passage of time) and the partner interviews need audio and classmates."),
    ],
    exercises=uniq(
        _tr(_JI_S + _JI_HOME + [(k, e) for _, k, e in _JI_MODEL], k=3)
        + [M("What does –(으)ㄴ 지 ~(이/가) 되다 express?", "The passage of time since an event", ["A reason", "A wish", "A command"], "It has been … since …"), M("What does 되었어요 mean in this pattern?", "has become", ["is wanted", "was told", "will go"], "되다 = to become."), M("Which question word asks “how long”?", "얼마나", ["어디", "누가", "무엇"], "얼마나 되었습니까?"), M("Which expression asks “how many years”?", "몇 년", ["며칠", "몇 시간", "얼마"], "몇 년."), M("What does 몬트레이에 온 지 일 년이 되었어요 mean?", "It has been a year since I came to Monterey", ["I will come in a year", "I came a year ago for a day", "I am leaving in a year"], "Passage of time."),
           M("Which form of the verb comes before 지?", "The past attributive -(으)ㄴ", ["-는", "-(으)ㄹ", "-고"], "온 지, 입대한 지."), M("What does 고향에 안 간 지 이 년이나 되었어요 mean?", "It has been as long as two years since I last went to my hometown", ["I will go for two years", "I went twice", "I live in my hometown"], "Model."),
           F("공군에 입대한 ___ 삼 년이 되었습니다. (since)", "지", ["김", "때"], "-(으)ㄴ 지."), F("한국말을 공부한 지 벌써 오 개월이 ___. (has become)", "됐습니다", ["했습니다", "갔습니다"], "되다."), F("몬트레이에 온 지 ___ 되었습니까? (how long)", "얼마나", ["어디", "무엇"], "얼마나."), F("공군에 입대한 지 ___ 년 되었어요? (how many)", "몇", ["얼마", "무슨"], "몇 년."), F("그 친구를 ___ 지 오래 되었어요. (met)", "만난", ["만나는", "만날"], "만난 지."),
           read_q("몬트레이에 온 지 일 년이 되었어요"), read_q("공군에 입대한 지 삼 년이 되었습니다"), read_q("그 친구를 만난 지 오래 되었어요"), read_q("건강검진을 받은 지 얼마나 되었어요"), read_q("고향에 안 간 지 이 년이나 되었어요")]
    ),
)

# ================================================================== L11: Grammar D: -(으)ㄴ/는 김에
_GI_S = [("집청소하는 김에 빨래도 했어요.", "Since I was doing house cleaning, I did laundry as well."), ("한국어를 배우는 김에 한국 역사도 배우고 싶어요.", "Because I am learning Korean, I’d also like to learn Korean history."), ("시장에 가는 김에 술 좀 사다 주세요.", "Because you are going to the market, please get me some liquor."), ("피자를 주문하는 김에 음료수도 시킵시다.", "While we are ordering pizza, let’s order drinks as well."), ("한국어를 배운 김에 한국 역사도 배우고 싶어요.", "Because I have learned Korean, I’d like to learn Korean history also.")]
_GI_V = [("청소하다", "to clean"), ("가다", "to go"), ("배우다", "to learn"), ("주문하다", "to order"), ("만들다", "to make"), ("먹다", "to eat"), ("읽다", "to read")]
_GI_ROAD = [("시내에 가는 길에 반 친구를 만났어요.", "On my way downtown, I met my classmate."), ("학교에 오는 길에 도서관에 들렀어요.", "On my way to school, I stopped at the library.")]
_GI_C = [("시내에 간 김에 친구를 만났어요.", "Since I went downtown, I met a friend."), ("친구를 만난 김에 점심을 같이 먹었어요.", "Since I met my friend, we had lunch together.")]
L11 = lesson(
    "Ch 29 · Grammar D: the conjunctive ending –(으)ㄴ/는 김에",
    "-는 김에 · -ㄴ 김에 · 집청소하는 김에 빨래도 · 시장에 가는 김에 · 가는 길에",
    requires=[],
    cards=[
        card("The conjunctive ending –(으)ㄴ/는 김에",
             "While engaging in a certain intended activity, we often take advantage of the activity to do another activity that is not originally intended. The conjunctive ending –는 김에 is used in this context. In the first example the speaker’s main activity was doing house cleaning, and while doing it the speaker “took advantage” and also did laundry, an activity not originally intended. Likewise, in the second the speaker takes advantage of the opportunity of learning Korean and wants to learn Korean history as well. For this reason the ending works only with an action verb and, depending on the context, it can be translated as “because”, “since”, “as” or “while”.",
             examples=passage(_GI_S[:4])),
        card("–(으)ㄴ 김에", "–(으)ㄴ 김에 can be used as well, but it implies that after the intended activity has been completed, the originally unintended activity is engaged in:", examples=passage(_GI_S[4:])),
        card("Forms (mine)", "Verb stem + 는 김에 (a stem ending in ㄹ drops the ㄹ: 만들다 → 만드는 김에) for the activity in progress, and –(으)ㄴ 김에 after it is completed.",
             tables=[table(["Verb", "Meaning", "-는 김에", "-(으)ㄴ 김에"], [[v, m, attr(v)[0] + " 김에", attr(v)[1] + " 김에"] for v, m in _GI_V], say=[0, 2, 3])]),
        card("Note: do not confuse it with –가는/오는 길에", "This conjunctive ending should not be confused with –가는/오는 길에 (on one’s way to), as in:", examples=passage(_GI_ROAD)),
        card("Follow-up 3 (Speaking and listening): the sentence chain", "The book’s circle game: the instructor begins with a –(으)ㄴ/는 김에 sentence, and the next student builds a new one with the last verb. The book’s example (the English is mine):", examples=passage(_GI_C)),
        card("Activities left out", "Follow-up 3 (the circle game), Follow-up 4 (listening to two husband–wife conversations, to write the main and secondary activities), Activity 1 (SMART Board), Activity 2 (summarizing two checkup articles and exchanging information with a partner) and Activity 3 (listening to two checkup packages and recommending one) are audio, computer and partner activities."),
    ],
    exercises=uniq(
        _tr(_GI_S + _GI_ROAD + _GI_C, k=3)
        + [M("What does –는 김에 express?", "Taking advantage of one activity to do another unintended one", ["A cause and effect only", "A contrast", "A past habit"], "집청소하는 김에 빨래도 했어요."), M("What kind of verbs does –(으)ㄴ/는 김에 work with?", "Action verbs", ["Adjectives", "Nouns", "Only the copula"], "The book’s note."), M("What does –(으)ㄴ 김에 imply?", "After the intended activity was completed, another is done", ["During the activity", "Before the activity", "Instead of the activity"], "한국어를 배운 김에."), M("What does 가는 길에 mean?", "on one’s way to", ["because", "instead of", "if"], "시내에 가는 길에."),
           M("How is –는 김에 translated?", "Because; since; as; while", ["If; when", "Although", "In order to"], "Depending on the context."), M("What does 시장에 가는 김에 술 좀 사다 주세요 mean?", "Because you are going to the market, please get me some liquor", ["Please do not go to the market", "I went to the market", "Liquor is at the market"], "Taking advantage."),
           F("집청소하___ 김에 빨래도 했어요. (while doing)", "는", ["은", "을"], "-는 김에."), F("한국어를 배운 ___ 한국 역사도 배우고 싶어요. (since I have learned)", "김에", ["길에", "지가"], "배운 김에."), F("학교에 오는 ___ 도서관에 들렀어요. (on my way)", "길에", ["김에", "때에"], "오는 길에."), F("피자를 주문하는 ___ 음료수도 시킵시다. (while)", "김에", ["지에", "길에"], "주문하는 김에."), F("친구를 만난 김에 점심을 같이 ___. (ate)", "먹었어요", ["먹겠어요", "먹어요?"], "past."),
           read_q("집청소하는 김에 빨래도 했어요"), read_q("한국어를 배우는 김에 한국 역사도 배우고 싶어요"), read_q("시장에 가는 김에 술 좀 사다 주세요"), read_q("피자를 주문하는 김에 음료수도 시킵시다"), read_q("학교에 오는 길에 도서관에 들렀어요")]
    ),
)

# ================================================================== L12: core vocabulary and self-evaluation
_CV_SECS = [("Topic Presentation A", _CV_A), ("Topic Presentation B", _CV_B), ("Topic Presentation C", _CV_C), ("Grammatical features", _CV_GR), ("Sino-Korean vocabulary", _CV_SINO)]
_CV_PLAIN = [(r[0].split(" / ")[0], _en(r[0])) for _, rows in _CV_SECS[:3] for r in rows if not any(c in r[0] for c in "~(-")]


def _vtabs(rows):
    sp = [r for r in rows if "-" not in r[0] and "ㅅ" not in r[0]]
    ns = [r for r in rows if "-" in r[0] or "ㅅ" in r[0]]
    out = [vt([(_show(r[0]), r[1], r[2]) for r in sp])] if sp else []
    if ns:
        out.append(table(["Pattern", "Meaning", "Example"], [[r[0], r[1], r[2]] for r in ns], say=[2]))
    return out


L12 = lesson(
    "Ch 29 · Core vocabulary and self-evaluation",
    "주요 단어 · 병과 증상 · 독감 · 진찰 · 치료 · 검진 · 자기 평가",
    requires=[],
    cards=[
        card("How to use this list",
             "The book’s Core Vocabulary lists the core words of the chapter with an example sentence for each (the sentences and the English meanings are the book’s; the book gives no English for the sentences). The Hanja of the Sino-Korean words are in parentheses before the meaning. Where the book writes two forms together (for example 알레르기/알러지 or 체중/몸무게), the forms are written with a slash. The book’s related words (the synonyms, antonyms and related words in the last column) are left out, and the book’s Additional Vocabulary section is blank.\n\n"
             "The example sentences with digits are respelled in Hangul (162 cm → 백육십이 센티미터, 48 kg → 사십팔 킬로그램, 36.5도 → 삼십육 점 오 도, 6개월 → 육 개월, 10시간 → 열 시간, 5분 → 오 분, 7개월 → 칠 개월)."),
    ] + [card(name, "", tables=_vtabs(rows)) for name, rows in _CV_SECS] + [
        card("Self-evaluation",
             "Recall the objectives of the chapter and ask yourself whether you have achieved them (the book asks you to tick Yes or No). If you tick “No” for any item, the book suggests: review that section on your own; find a study partner and review it as a pair or group; and tell your academic advisor or team leader which areas you need more help with, so that they can provide activities tailored to your learning style and needs.\n\n"
             "Now I am able to: identify and describe general health conditions, common ailments, and symptoms; identify and talk about basic medical and clinical specialties; and ask about common ailments and provide treatment suggestions.\n\n"
             "Now I have a clear understanding of: the new words and phrases in the Core Vocabulary section; ㅅ irregular verbs; –도록 하다; –(으)ㄴ 지 ~(이/가) 되다; the conjunctive ending –(으)ㄴ/는 김에; and the Sino-Korean syllables within 병원 (病院), 통증 (痛症), and 혈압 (血壓)."),
    ],
    exercises=uniq(
        vocab_exercises(_CV_PLAIN)
        + [M("What does 병원 literally mean?", "“illness house”", ["“pain symptom”", "“blood fluid”", "“skin department”"], "병 + 원."), M("What does 통증 literally mean?", "“pain symptom”", ["“illness house”", "“blood fluid”", "“tooth department”"], "통 + 증."), M("What does 혈압 mean?", "blood pressure", ["blood type", "pulse", "body weight"], "혈 + 압."),
           M("What is 소아과?", "pediatrics", ["obstetrics and gynecology", "dentistry", "dermatology"], "소아과."), M("What is 산부인과?", "obstetrics and gynecology", ["pediatrics", "ophthalmology", "internal medicine"], "산부인과."), M("What is 이비인후과?", "ear, nose, and throat", ["eye department", "skin department", "tooth department"], "이비인후과."), M("What does 살이 찌다 mean?", "to put on weight", ["to lose weight", "to measure", "to cure"], "살이 찌다."), M("What does 살이 빠지다 mean?", "to lose weight", ["to put on weight", "to be dizzy", "to scratch"], "살이 빠지다."),
           F("몸에 ___을 느끼면 의사에게 가 보세요. (an abnormality)", "이상", ["결과", "정상"], "이상."), F("교통사고를 당한 환자들이 근처 병원에 ___해서 치료를 받고 있습니다. (are hospitalized)", "입원", ["퇴원", "진찰"], "입원."), F("최 선생님은 일주일 동안 병원에 계시다 어제 ___했습니다. (was discharged)", "퇴원", ["입원", "수술"], "퇴원."), F("혈압 환자들은 혈압 ___을 자주 하는 것이 좋습니다. (measurement)", "측정", ["검사", "치료"], "측정."), F("우리 병원은 토요일에는 ___를 안 합니다. (medical care)", "진료", ["수술", "환자"], "진료."),
           read_q("주요 단어"), read_q("독감"), read_q("진찰"), read_q("치료"), read_q("검진")]
    ),
)

UNIT = unit("Semester 2 · Unit 8 · Chapter 29: Common Ailments and Symptoms (병과 증상)", [L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12])
